"""Stage 2 of the speech loop: speech-to-text (STT). input.wav -> transcript.json

Run it (from the speech/ folder):
    uv run python -m speech.stt                       # transcribe the most recent recording
    uv run python -m speech.stt runs/<session>/turn_01  # transcribe a specific turn

Uses faster-whisper, a fast re-implementation of OpenAI's Whisper model. Whisper listens to
up to 30 s of audio at a time and writes out the words it hears, with a start/end time per word.
Which Whisper size, and CPU or GPU, is set in config.toml [stt].
"""

import argparse
import json
import time
from pathlib import Path

import numpy as np
import soundfile as sf
from faster_whisper import WhisperModel

from speech.config import latest_turn, load_config

WHISPER_SAMPLE_RATE = 16000


class SpeechToText:
    """Load the model once (slow), then transcribe many recordings (fast)."""

    def __init__(self, cfg: dict):
        start = time.monotonic()
        self.model = WhisperModel(cfg["model"], device=cfg["device"], compute_type=cfg["compute_type"])
        self.load_seconds = time.monotonic() - start
        self.cfg = cfg

    def transcribe(self, audio: np.ndarray) -> dict:
        """audio: float32 mono samples at 16 kHz. Returns text, segments, words, and timing."""
        start = time.monotonic()
        # Whisper returns "segments" (roughly sentences). The call is lazy: the real work happens
        # while we loop over them below, so the timer must include the loop.
        segments, info = self.model.transcribe(audio, language="en", word_timestamps=True)
        segments = [
            {
                "start": round(s.start, 3),
                "end": round(s.end, 3),
                "text": s.text.strip(),
                "words": [{"word": w.word.strip(), "start": round(w.start, 3),
                           "end": round(w.end, 3), "probability": round(w.probability, 3)}
                          for w in s.words],
            }
            for s in segments
        ]
        return {
            "text": " ".join(s["text"] for s in segments),
            "segments": segments,
            "audio_seconds": round(len(audio) / WHISPER_SAMPLE_RATE, 3),
            "transcribe_seconds": round(time.monotonic() - start, 3),
            "model": self.cfg["model"],
            "device": self.cfg["device"],
        }


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe a turn's input.wav into transcript.json.")
    parser.add_argument("turn", nargs="?", type=Path, help="turn folder (default: most recent)")
    args = parser.parse_args()
    turn = args.turn or latest_turn()

    audio, sample_rate = sf.read(turn / "input.wav", dtype="float32")
    if sample_rate != WHISPER_SAMPLE_RATE:
        raise SystemExit(f"{turn / 'input.wav'} is {sample_rate} Hz; Whisper needs {WHISPER_SAMPLE_RATE}.")

    stt = SpeechToText(load_config()["stt"])
    print(f"model loaded in {stt.load_seconds:.1f} s (only happens once per program start)")
    result = stt.transcribe(audio)

    (turn / "transcript.json").write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"transcribed {result['audio_seconds']:.1f} s of audio in {result['transcribe_seconds']:.2f} s")
    print(f'you said: "{result["text"]}"')
    print(f"saved {turn / 'transcript.json'}")


if __name__ == "__main__":
    main()
