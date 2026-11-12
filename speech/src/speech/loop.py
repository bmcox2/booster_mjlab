"""The whole v0 conversation: record -> speech-to-text -> LLM -> text-to-speech -> play, repeated.

Run it (from the speech/ folder):
    uv run python -m speech.loop

Press Enter, talk, press Enter. The robot answers out loud. Repeat. Type q + Enter to quit.
Each turn is saved in runs/<session>/turn_NN/ with the same files the single stages write, plus
timing.json (when each step finished). Every turn is also appended to runs/latency.jsonl;
summarize with: uv run python -m speech.latency

With [stream] enabled (step 4 of notes/speech_plan.md) the robot starts speaking the first
piece of its reply while the rest is still being written and voiced (speech/streaming.py).
Without it, each stage waits for the previous one to finish. The models are loaded once at the
start, so each turn only pays for the actual work.
"""

import json
import time
from datetime import datetime
from pathlib import Path

import numpy as np
import sounddevice as sd

from speech.audio import describe, find_device, record_until_enter, save_wav
from speech.config import RUNS_DIR, load_config
from speech.gesture import GestureClient
from speech.llm import ChatModel, session_history
from speech.metrics import word_error_rate
from speech.streaming import Player, stream_reply
from speech.stt import SpeechToText
from speech.timing import TurnTimer, config_label
from speech.tts import KOKORO_SAMPLE_RATE, TextToSpeech


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


class Pipeline:
    """The three models, loaded once, and one function that runs a whole turn."""

    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.label = config_label(cfg)
        self.stt = SpeechToText(cfg["stt"])  # loads + warms up its providers
        self.tts = TextToSpeech(cfg["tts"])
        self.llm = ChatModel(cfg["llm"])
        # Warm-up: the first use of a model is slower than the rest (memory setup, caches).
        self.tts.synthesize("Ready.")
        self.streaming = cfg.get("stream", {}).get("enabled", False)
        self.players: dict[int, Player] = {}  # one open speaker stream per output device
        self.gesture = GestureClient(cfg.get("gesture", {}))  # K1 motion per reply (gesture service)

    def player(self, device: int) -> Player:
        if device not in self.players:
            self.players[device] = Player(device, KOKORO_SAMPLE_RATE)
        return self.players[device]

    def close(self) -> None:
        self.gesture.wait()
        for p in self.players.values():
            p.close()

    def run_turn(self, audio: np.ndarray, turn: Path, timer: TurnTimer,
                 output_device: int | None, mode: str, history: list[dict] | None = None,
                 reference: str | None = None) -> dict:
        """input audio -> transcript -> reply -> speech (-> played if output_device is set).

        timer must already be started at the moment speech ended. reference = the correct text
        (test set only), to score the transcript. Returns the timing record.
        """
        sample_rate = self.cfg["audio"]["sample_rate"]
        turn.mkdir(parents=True, exist_ok=True)
        if "endpoint" not in timer.events:  # push-to-talk / replay: the turn ended at speech_end
            timer.mark("endpoint", timer.t0)
        meta = {"mode": mode, "label": self.label}

        transcript = self.stt.transcribe(audio)
        timer.mark("stt_done")
        save_wav(turn / "input.wav", audio, sample_rate)  # saving happens after the timestamp
        save_json(turn / "transcript.json", transcript)
        print(f'you: "{transcript["text"]}"')
        meta.update(stt_provider=transcript["provider"], fallback_used=transcript["fallback_used"],
                    input_audio_seconds=transcript["audio_seconds"])
        if reference is not None:
            meta["wer"] = round(word_error_rate(reference, transcript["text"]), 4)
        if not transcript["text"]:
            print(f"(heard nothing: {describe(audio, sample_rate)})")
            return timer.save(turn, {**meta, "skipped": "empty transcript"})

        if history is None:
            history = session_history(turn)
        messages = self.llm.build_messages(history, transcript["text"])
        if self.streaming:
            player = self.player(output_device) if output_device is not None else None
            reply, speech, tts_info = stream_reply(self.llm, self.tts, messages, timer,
                                                   self.cfg["stream"], player, KOKORO_SAMPLE_RATE)
            save_json(turn / "request.json", {"model": self.llm.cfg["model"], "messages": messages})
            save_json(turn / "reply.json", reply)
            save_wav(turn / "reply.wav", speech, KOKORO_SAMPLE_RATE)
            save_json(turn / "tts.json", tts_info)
            meta["reply_audio_seconds"] = tts_info["audio_seconds"]
            record = timer.save(turn, meta)
            print(f"[{summary_line(record)}]")
            self.gesture.submit(turn)
            return record

        llm_start = time.monotonic()
        reply = self.llm.reply(messages)
        timer.mark("llm_first_token", llm_start + reply["first_token_seconds"])
        timer.mark("llm_first_sentence", llm_start + reply["first_sentence_seconds"])
        timer.mark("llm_done", llm_start + reply["total_seconds"])
        save_json(turn / "request.json", {"model": self.llm.cfg["model"], "messages": messages})
        save_json(turn / "reply.json", reply)
        print(f'robot: "{reply["text"]}"')

        speech, tts_info = self.tts.synthesize(reply["text"])
        timer.mark("tts_done")
        save_wav(turn / "reply.wav", speech, KOKORO_SAMPLE_RATE)
        save_json(turn / "tts.json", tts_info)
        meta["reply_audio_seconds"] = tts_info["audio_seconds"]

        if output_device is not None:
            sd.play(speech, KOKORO_SAMPLE_RATE, device=output_device)  # returns immediately
            timer.mark("playback_start")
            # Output latency: how long the sound card's buffer takes to reach the speaker.
            timer.extra["output_latency_s"] = round(sd.get_stream().latency, 4)
            record = timer.save(turn, meta)  # save before waiting, so the record is written
            print(f"[{summary_line(record)}]")
            sd.wait()
            self.gesture.submit(turn)
            return record

        record = timer.save(turn, meta)
        print(f"[{summary_line(record)}]")
        self.gesture.submit(turn)
        return record


def summary_line(record: dict) -> str:
    s = record["stages"]
    if "first_audio" in s:  # streaming
        start = s.get("response", s["first_audio"])
        heard = "voice started" if "response" in s else "first audio ready"
        endpoint = f"end of turn {s['endpoint']:.2f}, " if s.get("endpoint") else ""
        gaps = record.get("gaps_s", 0)
        return (f"{heard} after {start:.2f} s: {endpoint}speech-to-text {s.get('stt', 0):.2f}, "
                f"LLM first piece {s.get('llm_first_chunk', 0):.2f}, "
                f"voicing first piece {s.get('tts_first_chunk', 0):.2f}; "
                f"{record.get('chunks', 0)} pieces, gaps {gaps:.2f} s"
                + ("" if record.get("gaps_measured", True) else " (simulated)"))
    reply_ready = s.get("response", record["events"].get("tts_done", 0.0))
    endpoint = f"end of turn {s['endpoint']:.2f}, " if s.get("endpoint") else ""
    return (f"answer after {reply_ready:.2f} s: {endpoint}speech-to-text {s.get('stt', 0):.2f}, "
            f"LLM {s.get('llm_total', 0):.2f} (first sentence {s.get('llm_first_sentence', 0):.2f}), "
            f"text-to-speech {s.get('tts', 0):.2f}")


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Talk with the robot.")
    parser.add_argument("--hands-free", action="store_true",
                        help="no Enter presses: the mic listens and detects when you stop (step 3)")
    args = parser.parse_args()
    cfg = load_config()
    in_dev = find_device(cfg["audio"]["input_device"], "input")
    out_dev = find_device(cfg["audio"]["output_device"], "output")
    sample_rate = cfg["audio"]["sample_rate"]

    print("loading models...")
    pipeline = Pipeline(cfg)
    print(f"ready ({pipeline.label})\n")

    session = RUNS_DIR / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if args.hands_free:
        hands_free(pipeline, cfg, in_dev, out_dev, session)
        return
    turn_number = 0
    while True:
        audio = record_until_enter(sample_rate, in_dev,
                                   prompt="Press Enter to talk (q + Enter to quit)... ")
        if audio is None:
            break
        timer = TurnTimer()  # you finished talking here: time 0 for this turn
        turn_number += 1
        pipeline.run_turn(audio, session / f"turn_{turn_number:02d}", timer, out_dev, mode="live")
        print()

    pipeline.close()
    print(f"saved {turn_number} turns in {session}")
    print("timing summary: uv run python -m speech.latency")


def hands_free(pipeline: "Pipeline", cfg: dict, in_dev: int, out_dev: int, session: Path) -> None:
    """Listen -> answer -> listen... The mic is ignored while the robot talks (half-duplex),
    because without echo cancellation the laptop mic would hear the robot and answer itself."""
    from speech.vad import Listener

    listener = Listener(cfg["vad"], in_dev)
    print("Hands-free: just talk; the robot answers when you're done. Ctrl+C to quit.\n")
    turn_number = 0
    try:
        while True:
            print("(listening...)", end="", flush=True)
            utterance = listener.next_utterance()
            print("\r" + " " * 15 + "\r", end="")
            listener.pause()
            timer = TurnTimer(start=utterance.speech_end)  # 0 = your last sound
            timer.mark("endpoint", utterance.endpoint)
            timer.extra["vad"] = utterance.info()
            turn_number += 1
            pipeline.run_turn(utterance.audio, session / f"turn_{turn_number:02d}", timer, out_dev,
                              mode="live")
            listener.resume()
            print()
    except KeyboardInterrupt:
        pass
    finally:
        listener.close()
        pipeline.close()
    print(f"\nsaved {turn_number} turns in {session}")
    print("timing summary: uv run python -m speech.latency --mode live")


if __name__ == "__main__":
    main()
