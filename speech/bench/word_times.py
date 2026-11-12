"""How good is estimate_word_times (used for Orpheus, which gives no word times)?

Run (from speech/):  uv run python bench/word_times.py
Voices the pieces of recent live replies with Kokoro, which reports real word times, then guesses
the times from Kokoro's audio alone and compares the word starts.
"""
import json, statistics, warnings
from pathlib import Path

import numpy as np

warnings.simplefilter("ignore")
from speech.config import load_config  # noqa: E402
from speech.streaming import trim_silence  # noqa: E402
from speech.tts import SAMPLE_RATE, KokoroEngine, estimate_word_times  # noqa: E402

SPEECH = Path(__file__).resolve().parents[1]
pieces = []
for p in sorted(SPEECH.glob("runs/2026-11-11_*/turn_*/tts.json")):
    pieces += [c["text"] for c in json.loads(p.read_text()).get("chunks", [])]
pieces = pieces[:60]
kokoro = KokoroEngine(load_config()["tts"])
errs, uniform, skipped = [], [], 0
for text in pieces:
    audio, info = kokoro.synthesize(text)
    audio, cut = trim_silence(audio, SAMPLE_RATE)  # the stream trims, so compare on trimmed audio
    real = [w["start"] - cut for w in info["words"] if w["word"][:1].isalnum()]
    est = [w["start"] for w in estimate_word_times(audio, SAMPLE_RATE, text)]
    if len(real) != len(est):
        skipped += 1
        continue
    errs += [abs(a - b) for a, b in zip(real, est)]
    # baseline: words spread evenly over the audio
    even = np.linspace(0, len(audio) / SAMPLE_RATE, len(est) + 1)[:-1]
    uniform += [abs(a - b) for a, b in zip(real, even)]
q = lambda x, p: float(np.percentile(x, p))
print(f"{len(pieces)} pieces, {len(errs)} words compared, {skipped} pieces skipped (word count differs)")
print(f"estimate: start error median {statistics.median(errs)*1000:.0f} ms, p90 {q(errs,90)*1000:.0f} ms, max {max(errs)*1000:.0f} ms")
print(f"even spread: median {statistics.median(uniform)*1000:.0f} ms, p90 {q(uniform,90)*1000:.0f} ms")
