"""Stage 2 of the speech loop: speech-to-text (STT). input.wav -> transcript.json

Run it (from the speech/ folder):
    uv run python -m speech.stt                         # transcribe the most recent recording
    uv run python -m speech.stt runs/<session>/turn_01  # transcribe a specific turn
    uv run python -m speech.stt --provider local        # override config.toml for this run

Two providers, chosen in config.toml [stt]:
    groq  - OpenAI's Whisper large-v3 running on Groq's servers. Fast (~0.3 s) and accurate,
            needs internet; the free tier allows 2,000 requests a day.
    local - faster-whisper on this laptop (small.en on CPU: ~1.6 s). Works offline.
If the provider fails (no internet, rate limit), the fallback provider is used instead and the
transcript says so ("fallback_used").

Whisper listens to the audio and writes out the words it hears, with a start/end time per word.
The "prompt" (hint words) is text Whisper reads before listening; names in it get spelled right
more often ("Booster Lab" instead of "Ibiza Lab").
"""

import argparse
import io
import json
import os
import time
from pathlib import Path

import numpy as np
import soundfile as sf

from speech.config import latest_turn, load_config

WHISPER_SAMPLE_RATE = 16000


class GroqWhisper:
    def __init__(self, cfg: dict, prompt: str):
        from openai import OpenAI
        self.client = OpenAI(base_url=cfg["base_url"], api_key=os.environ[cfg["api_key_env"]],
                             timeout=10, max_retries=0)  # fail fast; the fallback takes over
        self.model, self.prompt = cfg["model"], prompt

    def transcribe(self, audio: np.ndarray) -> tuple[list[dict], str]:
        # The API takes a file, so we write the samples into an in-memory WAV file.
        wav = io.BytesIO()
        sf.write(wav, audio, WHISPER_SAMPLE_RATE, format="WAV", subtype="PCM_16")
        r = self.client.audio.transcriptions.create(
            model=self.model, file=("input.wav", wav.getvalue()), language="en",
            prompt=self.prompt or None, response_format="verbose_json",
            timestamp_granularities=["word", "segment"]).model_dump()
        # Groq returns words for the whole recording, separately from segments; put each word
        # into the segment it falls in, so both providers give the same shape.
        words = [{"word": w["word"].strip(), "start": round(w["start"], 3), "end": round(w["end"], 3)}
                 for w in r.get("words") or []]
        segments = []
        for s in r.get("segments") or []:
            segments.append({"start": round(s["start"], 3), "end": round(s["end"], 3),
                             "text": s["text"].strip(),
                             "words": [w for w in words if s["start"] <= w["start"] < s["end"]]})
        return segments, f"groq/{self.model}"


class LocalWhisper:
    def __init__(self, cfg: dict, prompt: str):
        from faster_whisper import WhisperModel
        self.model = WhisperModel(cfg["model"], device=cfg["device"], compute_type=cfg["compute_type"])
        self.name, self.prompt = cfg["model"], prompt
        self.model.transcribe(np.zeros(WHISPER_SAMPLE_RATE, dtype=np.float32))  # warm-up

    def transcribe(self, audio: np.ndarray) -> tuple[list[dict], str]:
        # The call is lazy: the real work happens while we loop over the segments.
        segments, _ = self.model.transcribe(audio, language="en", word_timestamps=True,
                                            initial_prompt=self.prompt or None)
        out = [{"start": round(s.start, 3), "end": round(s.end, 3), "text": s.text.strip(),
                "words": [{"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3),
                           "probability": round(w.probability, 3)} for w in s.words]}
               for s in segments]
        return out, f"local/{self.name}"


PROVIDERS = {"groq": GroqWhisper, "local": LocalWhisper}


class SpeechToText:
    """Load the providers once (slow), then transcribe many recordings (fast)."""

    def __init__(self, cfg: dict):
        start = time.monotonic()
        prompt = cfg.get("prompt", "")
        self.primary = PROVIDERS[cfg["provider"]](cfg[cfg["provider"]], prompt)
        fallback = cfg.get("fallback") or ""
        self.fallback = (PROVIDERS[fallback](cfg[fallback], prompt)
                         if fallback and fallback != cfg["provider"] else None)
        self.load_seconds = time.monotonic() - start

    def transcribe(self, audio: np.ndarray) -> dict:
        """audio: float32 mono samples at 16 kHz. Returns text, segments, words, and timing."""
        start = time.monotonic()
        error = None
        try:
            segments, provider = self.primary.transcribe(audio)
        except Exception as e:  # no internet, rate limit, server error...
            if self.fallback is None:
                raise
            error = f"{type(e).__name__}: {e}"[:300]
            print(f"(speech-to-text provider failed, using the fallback: {error})")
            segments, provider = self.fallback.transcribe(audio)
        return {
            "text": " ".join(s["text"] for s in segments).strip(),
            "segments": segments,
            "audio_seconds": round(len(audio) / WHISPER_SAMPLE_RATE, 3),
            "transcribe_seconds": round(time.monotonic() - start, 3),
            "provider": provider,
            "fallback_used": error is not None,
            "error": error,
        }


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe a turn's input.wav into transcript.json.")
    parser.add_argument("turn", nargs="?", type=Path, help="turn folder (default: most recent)")
    parser.add_argument("--provider", choices=sorted(PROVIDERS), help="override config.toml")
    args = parser.parse_args()
    turn = args.turn or latest_turn()

    audio, sample_rate = sf.read(turn / "input.wav", dtype="float32")
    if sample_rate != WHISPER_SAMPLE_RATE:
        raise SystemExit(f"{turn / 'input.wav'} is {sample_rate} Hz; Whisper needs {WHISPER_SAMPLE_RATE}.")

    cfg = load_config()["stt"]
    if args.provider:
        cfg["provider"] = args.provider
    stt = SpeechToText(cfg)
    print(f"loaded in {stt.load_seconds:.1f} s (only happens once per program start)")
    result = stt.transcribe(audio)

    (turn / "transcript.json").write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"transcribed {result['audio_seconds']:.1f} s of audio in {result['transcribe_seconds']:.2f} s "
          f"({result['provider']})")
    print(f'you said: "{result["text"]}"')
    print(f"saved {turn / 'transcript.json'}")


if __name__ == "__main__":
    main()
