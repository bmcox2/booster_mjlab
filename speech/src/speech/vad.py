"""Hands-free listening: voice activity detection (VAD) + endpointing. Step 3 of the plan.

Run it (from the speech/ folder):
    uv run python -m speech.vad                      # live: shows when it hears speech, saves each utterance
    uv run python -m speech.vad --testset            # replay the test set: does any sentence get cut?
    uv run python -m speech.vad --testset --silence-ms 400   # try another setting

Two separate questions:
    VAD          "is someone speaking in this 32 ms slice?"  -> Silero VAD, a tiny model (0.3 ms/slice)
    endpointing  "has the person finished their turn?"       -> here: N ms of silence after speech
                                                                (Smart Turn, a smarter judge, comes next)
Words used below:
    frame       512 samples = 32 ms of audio at 16 kHz, the size Silero wants
    threshold   Silero gives a speech probability 0..1 per frame; above `threshold` = speech starts
    hysteresis  once speaking, only a probability below `neg_threshold` (lower) counts as silence,
                so a soft syllable doesn't count as a pause
    pre-roll    the ~300 ms just *before* speech was detected, kept so the first syllable isn't clipped
    endpoint delay  time from your last word to the decision "your turn is over"
"""

import argparse
import collections
import json
import queue
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime

import numpy as np
import sounddevice as sd
import soundfile as sf

from speech.audio import find_device, save_wav
from speech.config import RUNS_DIR, load_config

SAMPLE_RATE = 16000
FRAME = 512  # samples per frame (32 ms)
FRAME_S = FRAME / SAMPLE_RATE


class SpeechDetector:
    """Silero VAD: one speech probability (0..1) per 32 ms frame."""

    def __init__(self):
        import torch
        from silero_vad import load_silero_vad
        self._torch = torch
        # ONNX version: runs on onnxruntime with its own thread, so it doesn't fight Kokoro for CPU.
        self.model = load_silero_vad(onnx=True)

    def prob(self, frame: np.ndarray) -> float:
        return float(self.model(self._torch.from_numpy(frame), SAMPLE_RATE))

    def reset(self) -> None:
        self.model.reset_states()  # Silero remembers recent audio; clear it between turns


@dataclass
class Utterance:
    audio: np.ndarray        # float32 16 kHz, pre-roll included, trailing silence trimmed
    speech_start: float      # times on the caller's clock (seconds)
    speech_end: float        # end of the last frame that sounded like speech
    endpoint: float          # when the decision "turn over" was made
    voiced_seconds: float
    reason: str              # "silence" or "max length"
    probs: list = field(default_factory=list)  # one probability per frame, for inspection

    @property
    def endpoint_delay(self) -> float:
        return self.endpoint - self.speech_end

    def info(self) -> dict:
        return {"seconds": round(len(self.audio) / SAMPLE_RATE, 3),
                "voiced_seconds": round(self.voiced_seconds, 3),
                "endpoint_delay_s": round(self.endpoint_delay, 3), "reason": self.reason,
                "speech_start": round(self.speech_start, 3), "speech_end": round(self.speech_end, 3),
                "endpoint": round(self.endpoint, 3)}


class Endpointer:
    """Feed it frames + probabilities one at a time; it returns an Utterance when a turn ends."""

    def __init__(self, cfg: dict):
        self.threshold = cfg["threshold"]
        self.neg_threshold = cfg["neg_threshold"]
        self.silence_s = cfg["silence_ms"] / 1000
        self.min_speech_s = cfg["min_speech_ms"] / 1000
        self.max_s = cfg["max_utterance_s"]
        self.tail_s = 0.2  # keep 200 ms after the last speech frame (word endings are soft)
        self.preroll = collections.deque(maxlen=max(1, round(cfg["preroll_ms"] / 1000 / FRAME_S)))
        self.reset()

    def reset(self) -> None:
        self.speaking = False
        self.frames, self.probs = [], []
        self.preroll.clear()

    def feed(self, frame: np.ndarray, prob: float, t_end: float) -> Utterance | None:
        """t_end = time at the end of this frame. Returns an Utterance when the turn is over."""
        if not self.speaking:
            if prob >= self.threshold:  # speech starts
                self.speaking = True
                self.frames = list(self.preroll) + [frame]
                self.probs = [prob]
                self.start = t_end - FRAME_S * len(self.frames)
                self.last_voiced = t_end
                self.voiced = FRAME_S
            else:
                self.preroll.append(frame)
            return None

        self.frames.append(frame)
        self.probs.append(prob)
        if prob >= self.neg_threshold:  # still speech (hysteresis: lower bar once speaking)
            self.last_voiced = t_end
            self.voiced += FRAME_S
        silence = t_end - self.last_voiced
        too_long = t_end - self.start >= self.max_s
        if silence < self.silence_s and not too_long:
            return None

        # Turn over (or just a noise blip that was too short to be speech).
        is_speech = self.voiced >= self.min_speech_s
        keep = len(self.frames) - max(0, round((silence - self.tail_s) / FRAME_S))
        utterance = Utterance(audio=np.concatenate(self.frames[:keep]), speech_start=self.start,
                              speech_end=self.last_voiced, endpoint=t_end,
                              voiced_seconds=self.voiced,
                              reason="max length" if too_long else "silence", probs=self.probs)
        self.reset()
        return utterance if is_speech else None


class Listener:
    """The microphone, always on, cut into utterances. pause()/resume() around the robot's own
    speech, so it doesn't hear itself through the laptop speakers (no echo cancellation yet)."""

    def __init__(self, cfg: dict, device: int):
        self.cfg = cfg
        self.detector = SpeechDetector()
        self.endpointer = Endpointer(cfg)
        self.frames: queue.Queue = queue.Queue()
        self.listening = True
        self.ignore_until = 0.0

        def callback(indata, n_frames, time_info, status):
            # Runs on the audio thread every 32 ms: only copy the frame + its arrival time.
            if self.listening:
                self.frames.put((indata[:, 0].copy(), time.monotonic()))

        self.stream = sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32",
                                     blocksize=FRAME, device=device, callback=callback)
        self.stream.start()

    def pause(self) -> None:
        self.listening = False

    def resume(self) -> None:
        while not self.frames.empty():  # drop anything recorded while paused
            self.frames.get_nowait()
        self.detector.reset()
        self.endpointer.reset()
        self.ignore_until = time.monotonic() + self.cfg["echo_tail_ms"] / 1000  # speaker ring-out
        self.listening = True

    def next_utterance(self, on_frame=None) -> Utterance:
        """Block until someone says something and stops. on_frame(prob, speaking) for live displays."""
        while True:
            frame, arrived = self.frames.get()
            if arrived < self.ignore_until:
                continue
            prob = self.detector.prob(frame)
            utterance = self.endpointer.feed(frame, prob, arrived)
            if on_frame:
                on_frame(prob, self.endpointer.speaking)
            if utterance is not None:
                utterance.endpoint = time.monotonic()  # decision time, after processing
                return utterance

    def close(self) -> None:
        self.stream.stop()
        self.stream.close()


def utterances_in_file(audio: np.ndarray, cfg: dict, trailing_silence_s: float = 2.0) -> list[Utterance]:
    """Run the same detector over a recording as if it were live (times = seconds into the file)."""
    detector, endpointer = SpeechDetector(), Endpointer(cfg)
    audio = np.concatenate([audio, np.zeros(int(trailing_silence_s * SAMPLE_RATE), np.float32)])
    found = []
    for i in range(0, len(audio) - FRAME + 1, FRAME):
        frame = audio[i:i + FRAME]
        u = endpointer.feed(frame, detector.prob(frame), (i + FRAME) / SAMPLE_RATE)
        if u is not None:
            found.append(u)
    return found


def bar(prob: float, speaking: bool) -> str:
    filled = int(prob * 30)
    return f"\r  {'SPEAKING' if speaking else 'quiet   '} [{'#' * filled}{' ' * (30 - filled)}] {prob:.2f}"


def live(cfg: dict) -> None:
    device = find_device(load_config()["audio"]["input_device"], "input")
    listener = Listener(cfg, device)
    out = RUNS_DIR / "_vad" / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print(f"Listening (silence to end a turn: {cfg['silence_ms']} ms). Talk, pause, talk. Ctrl+C to stop.\n")
    n = 0
    try:
        while True:
            u = listener.next_utterance(on_frame=lambda p, s: print(bar(p, s), end="", flush=True))
            n += 1
            save_wav(out / f"utt_{n:02d}.wav", u.audio, SAMPLE_RATE)
            (out / f"utt_{n:02d}.json").write_text(json.dumps({**u.info(), "config": cfg}, indent=2))
            print(f"\r  utterance {n}: {u.voiced_seconds:.1f} s of speech, turn ended "
                  f"{u.endpoint_delay * 1000:.0f} ms after your last sound ({u.reason})" + " " * 10)
    except KeyboardInterrupt:
        pass
    finally:
        listener.close()
    print(f"\n{n} utterances saved in {out}")


def testset(cfg: dict) -> None:
    from speech.testset import INDEX, TESTSET_DIR
    index = json.loads(INDEX.read_text())
    print(f"silence to end a turn: {cfg['silence_ms']} ms. Each recording is ONE sentence, so the "
          "right answer is 1 utterance.\n")
    print(f"{'item':12} {'utterances':>10} {'endpoint delay':>15}  pieces (s into the recording)")
    cut = 0
    for item_id in index:
        path = TESTSET_DIR / f"{item_id}.wav"
        if not path.exists():
            continue
        audio, _ = sf.read(path, dtype="float32")
        found = utterances_in_file(audio, cfg)
        cut += len(found) > 1
        pieces = ", ".join(f"{u.speech_start:.2f}-{u.speech_end:.2f}" for u in found)
        delay = f"{found[-1].endpoint_delay * 1000:.0f} ms" if found else "-"
        flag = "  <- CUT" if len(found) > 1 else ("  <- MISSED" if not found else "")
        print(f"{item_id:12} {len(found):10d} {delay:>15}  {pieces}{flag}")
    print(f"\n{cut} of {len(index)} sentences cut into pieces.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Voice activity detection + endpointing.")
    parser.add_argument("--testset", action="store_true", help="replay the test set instead of the mic")
    parser.add_argument("--silence-ms", type=int, help="override [vad] silence_ms")
    parser.add_argument("--threshold", type=float, help="override [vad] threshold")
    args = parser.parse_args()
    cfg = load_config()["vad"]
    if args.silence_ms is not None:
        cfg["silence_ms"] = args.silence_ms
    if args.threshold is not None:
        cfg["threshold"] = args.threshold
    testset(cfg) if args.testset else live(cfg)


if __name__ == "__main__":
    sys.exit(main())
