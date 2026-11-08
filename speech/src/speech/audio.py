"""Stage 1 of the speech loop: record from the mic, save a WAV, play audio back.

Run it (from the speech/ folder):
    uv run python -m speech.audio                 # record (Enter to start/stop), save, play back
    uv run python -m speech.audio --play FILE.wav # just play a saved file
    uv run python -m speech.audio --devices       # list the audio devices Python can see

Key ideas (see the walkthrough in chat / notes/speech_plan.md):
- Sound is stored as a list of numbers ("samples"): the microphone's reading taken many times a
  second. sample_rate = readings per second. 16,000 Hz is what Whisper (speech-to-text) expects.
- Mono = one channel (one list of numbers). Stereo = two (left, right).
- float32 samples go from -1.0 to 1.0. A WAV file usually stores int16 (-32768..32767) instead.
"""

import argparse
import queue
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import sounddevice as sd
import soundfile as sf

from speech.config import RUNS_DIR, load_config


def find_device(name: str, kind: str) -> int:
    """Return the device number whose name contains `name`.

    Device numbers change when you plug things in, so we always look devices up by name.
    kind is "input" (microphone) or "output" (speaker/headphones).
    """
    channels_key = "max_input_channels" if kind == "input" else "max_output_channels"
    for index, device in enumerate(sd.query_devices()):
        if name.lower() in device["name"].lower() and device[channels_key] > 0:
            return index
    sys.exit(f"No {kind} device named '{name}'. Run with --devices to see the list.")


def record_until_enter(sample_rate: int, device: int,
                       prompt: str = "Press Enter to START recording...") -> np.ndarray | None:
    """Record mono audio from Enter to Enter. Returns float32 samples in -1.0..1.0.

    Returns None if you type q (then Enter) instead of just Enter.
    """
    chunks: queue.Queue[np.ndarray] = queue.Queue()

    def callback(indata, frames, time_info, status):
        # sounddevice calls this on its own thread every few milliseconds with a new block of
        # samples. It must return fast (never print, sleep, or do heavy work here), or audio is
        # lost. So we only copy the block into a queue and handle it later.
        if status:
            chunks.put(status)  # e.g. "input overflow" = we were too slow and lost samples
        chunks.put(indata[:, 0].copy())  # column 0 = the single mono channel

    if input(prompt).strip().lower() == "q":
        return None
    with sd.InputStream(samplerate=sample_rate, channels=1, dtype="float32",
                        device=device, callback=callback):
        input("Recording... press Enter to STOP.")

    blocks, problems = [], []
    while not chunks.empty():
        item = chunks.get()
        (blocks if isinstance(item, np.ndarray) else problems).append(item)
    if problems:
        print(f"warning: audio problems while recording: {set(map(str, problems))}")
    return np.concatenate(blocks) if blocks else np.zeros(0, dtype=np.float32)


def describe(audio: np.ndarray, sample_rate: int) -> str:
    """One line of numbers that tell you if the recording is sane."""
    if audio.size == 0:
        return "empty recording"
    peak = float(np.max(np.abs(audio)))
    rms = float(np.sqrt(np.mean(audio**2)))  # average loudness
    to_db = lambda x: 20 * np.log10(max(x, 1e-10))  # dBFS: 0 = loudest possible, -60 = very quiet
    return (f"{audio.size / sample_rate:.2f} s, {audio.size} samples at {sample_rate} Hz, "
            f"peak {to_db(peak):.1f} dBFS, loudness (RMS) {to_db(rms):.1f} dBFS")


def save_wav(path: Path, audio: np.ndarray, sample_rate: int) -> None:
    """Save float32 samples as a 16-bit WAV (the common format every program can open)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(path, audio, sample_rate, subtype="PCM_16")


def play(audio: np.ndarray, sample_rate: int, device: int) -> None:
    """Play samples and wait until they finish."""
    sd.play(audio, sample_rate, device=device)
    sd.wait()


def main() -> None:
    parser = argparse.ArgumentParser(description="Record from the mic, save a WAV, play it back.")
    parser.add_argument("--play", type=Path, help="only play this WAV file")
    parser.add_argument("--devices", action="store_true", help="list audio devices and exit")
    args = parser.parse_args()

    if args.devices:
        print(sd.query_devices())
        return

    cfg = load_config()["audio"]
    out_dev = find_device(cfg["output_device"], "output")

    if args.play:
        audio, sample_rate = sf.read(args.play, dtype="float32")
        print(f"playing {args.play}: {describe(audio, sample_rate)}")
        play(audio, sample_rate, out_dev)
        return

    in_dev = find_device(cfg["input_device"], "input")
    sample_rate = cfg["sample_rate"]
    audio = record_until_enter(sample_rate, in_dev)
    if audio is None:
        return
    print(describe(audio, sample_rate))

    # One folder per session, one per turn (later stages add their files next to input.wav).
    session = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = RUNS_DIR / session / "turn_01" / "input.wav"
    save_wav(path, audio, sample_rate)
    print(f"saved {path}")

    print("playing it back...")
    play(audio, sample_rate, out_dev)


if __name__ == "__main__":
    main()
