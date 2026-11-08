"""Stage 4 of the speech loop: text-to-speech (TTS). reply.json -> reply.wav + tts.json

Run it (from the speech/ folder):
    uv run python -m speech.tts                         # speak the most recent reply
    uv run python -m speech.tts runs/<session>/turn_01  # a specific turn
    uv run python -m speech.tts --no-play               # only write reply.wav

Uses Kokoro, a small (82 million numbers) open text-to-speech model that runs on this laptop.
It first turns text into phonemes (the sounds of the words; unknown words go through espeak-ng),
then turns the phonemes into audio at 24,000 samples per second.
It also reports when each word starts and ends in the audio. Those word times are what will
let gestures line up with speech later (plan step 7).
"""

import argparse
import json
import time
import warnings
from pathlib import Path

import numpy as np

from speech.audio import describe, find_device, play, save_wav
from speech.config import latest_turn, load_config

KOKORO_SAMPLE_RATE = 24000


class TextToSpeech:
    def __init__(self, cfg: dict):
        start = time.monotonic()
        self.cfg = cfg
        self.pipelines = {}  # one per accent, all sharing the same loaded model
        self._pipeline(cfg["voice"])
        self.load_seconds = time.monotonic() - start

    def _pipeline(self, voice: str):
        """Kokoro voice names start with an accent letter: am_michael = American male,
        bm_george = British male. The accent decides how words are pronounced, so each accent
        gets its own pipeline (cheap: they share the one 82M-number model)."""
        lang = voice[0]
        if lang not in self.pipelines:
            with warnings.catch_warnings():  # Kokoro's libraries print harmless warnings on import
                warnings.simplefilter("ignore")
                from kokoro import KPipeline
                shared = next(iter(self.pipelines.values())).model if self.pipelines else True
                self.pipelines[lang] = KPipeline(lang_code=lang, repo_id="hexgrad/Kokoro-82M",
                                                 model=shared, device=self.cfg.get("device", "cpu"))
        return self.pipelines[lang]

    def synthesize(self, text: str, voice: str | None = None) -> tuple[np.ndarray, dict]:
        """Text -> (float32 samples at 24 kHz, info with word timings and timing).

        voice: override config.toml's voice (used by the voice sampler).
        """
        voice = voice or self.cfg["voice"]
        if "cpu_threads" in self.cfg:
            import torch
            # How many CPU threads the model math uses. Set right before every use, because other
            # libraries change it when they load (Kokoro's resets it to 14, Silero VAD's sets 1).
            # More is not faster on this laptop: its CPU mixes fast and slow cores; 4 was best.
            torch.set_num_threads(self.cfg["cpu_threads"])
        start = time.monotonic()
        # Kokoro splits long text into chunks and yields one result per chunk. Word times inside a
        # result count from that chunk's start, so we add the length of the audio before it.
        chunks, words, offset = [], [], 0.0
        for result in self._pipeline(voice)(text, voice=voice):
            audio = result.audio.numpy()
            for token in result.tokens or []:
                if token.start_ts is not None and token.end_ts is not None:
                    words.append({"word": token.text, "start": round(offset + token.start_ts, 3),
                                  "end": round(offset + token.end_ts, 3)})
            chunks.append(audio)
            offset += len(audio) / KOKORO_SAMPLE_RATE
        audio = np.concatenate(chunks) if chunks else np.zeros(0, dtype=np.float32)
        info = {
            "text": text,
            "voice": voice,
            "sample_rate": KOKORO_SAMPLE_RATE,
            "audio_seconds": round(len(audio) / KOKORO_SAMPLE_RATE, 3),
            "synthesize_seconds": round(time.monotonic() - start, 3),
            "words": words,
        }
        return audio, info


def main() -> None:
    parser = argparse.ArgumentParser(description="Speak a turn's reply.json; save reply.wav + tts.json.")
    parser.add_argument("turn", nargs="?", type=Path, help="turn folder (default: most recent)")
    parser.add_argument("--no-play", action="store_true", help="only write the files")
    args = parser.parse_args()
    turn = args.turn or latest_turn()

    reply = turn / "reply.json"
    if not reply.exists():
        raise SystemExit(f"No {reply}. Run the LLM first: uv run python -m speech.llm")
    text = json.loads(reply.read_text())["text"]

    cfg = load_config()
    tts = TextToSpeech(cfg["tts"])
    print(f"model loaded in {tts.load_seconds:.1f} s (only happens once per program start)")
    audio, info = tts.synthesize(text)

    save_wav(turn / "reply.wav", audio, KOKORO_SAMPLE_RATE)
    (turn / "tts.json").write_text(json.dumps(info, indent=2, ensure_ascii=False))
    print(f'robot says: "{text}"')
    print(f"made {info['audio_seconds']:.1f} s of speech in {info['synthesize_seconds']:.2f} s "
          f"({describe(audio, KOKORO_SAMPLE_RATE)})")
    print(f"saved {turn / 'reply.wav'} and {turn / 'tts.json'}")

    if not args.no_play:
        play(audio, KOKORO_SAMPLE_RATE, find_device(cfg["audio"]["output_device"], "output"))


if __name__ == "__main__":
    main()
