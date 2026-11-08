"""Speech-to-text benchmark on your saved recordings (runs/2026*/turn_*/input.wav).

Run (from speech/):  uv run python bench/stt.py
Compares local faster-whisper sizes/settings on the CPU with Groq's hosted Whisper.
"Correct" words = Groq whisper-large-v3 (the largest model), so WER here means
"how many words differ from the big model", not true accuracy.
Results: runs/_bench/stt.json (rewritten after each setup, so partial results survive).
"""
import io, json, os, re, statistics, time
from pathlib import Path

import numpy as np
import soundfile as sf
from dotenv import load_dotenv
from faster_whisper import WhisperModel
from openai import OpenAI

SPEECH = Path(__file__).resolve().parents[1]
OUT = SPEECH / "runs/_bench/stt.json"
OUT.parent.mkdir(parents=True, exist_ok=True)
load_dotenv(SPEECH / ".env")

wavs = [p for p in sorted(SPEECH.glob("runs/2026*/turn_*/input.wav")) if sf.info(p).duration > 1]
audios = {str(p.relative_to(SPEECH)): sf.read(p, dtype="float32")[0] for p in wavs}
print(len(audios), "recordings,", round(sum(len(a) for a in audios.values()) / 16000, 1), "s total", flush=True)


def words(text):
    return re.sub(r"[^a-z0-9' ]", " ", text.lower().replace("-", " ")).split()


def wer(ref, hyp):
    """Word error rate: word insertions + deletions + substitutions, divided by reference length."""
    r, h = words(ref), words(hyp)
    d = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(h) + 1):
            prev, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, prev + (r[i - 1] != h[j - 1]))
    return d[len(h)] / max(len(r), 1)


results = {}


def save():
    ref = results.get("groq whisper-large-v3")
    rows = []
    for name, out in results.items():
        rows.append({
            "setup": name,
            "median_s": statistics.median(v["seconds"] for v in out.values()),
            "max_s": max(v["seconds"] for v in out.values()),
            "s_per_audio_s": statistics.median(v["seconds"] / (len(audios[p]) / 16000) for p, v in out.items()),
            "wer_vs_large_v3": statistics.mean(wer(ref[p]["text"], v["text"]) for p, v in out.items()) if ref else None,
        })
    OUT.write_text(json.dumps({"rows": rows, "results": results}, indent=1, ensure_ascii=False))
    print(json.dumps(rows[-1]), flush=True)


groq = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ["GROQ_API_KEY"])
for model in ["whisper-large-v3", "whisper-large-v3-turbo"]:
    out = {}
    for p, a in audios.items():
        buf = io.BytesIO()
        sf.write(buf, a, 16000, format="WAV", subtype="PCM_16")
        t = time.monotonic()
        r = groq.audio.transcriptions.create(model=model, file=("a.wav", buf.getvalue()), language="en")
        out[p] = {"text": r.text.strip(), "seconds": time.monotonic() - t}  # includes upload time
        time.sleep(3.5)  # stay under the free tier's 20 requests/minute
    results["groq " + model] = out
    save()

for name, threads, beam in [("small.en", 0, 5), ("small.en", 8, 5), ("small.en", 8, 1),
                            ("base.en", 8, 1), ("distil-large-v3", 8, 1), ("large-v3-turbo", 8, 1)]:
    m = WhisperModel(name, device="cpu", compute_type="int8", cpu_threads=threads)
    m.transcribe(np.zeros(16000, np.float32), language="en")  # warm-up
    out = {}
    for p, a in audios.items():
        t = time.monotonic()
        segs, _ = m.transcribe(a, language="en", beam_size=beam)
        out[p] = {"text": " ".join(s.text.strip() for s in segs), "seconds": time.monotonic() - t}
    results[f"cpu {name} threads={threads or 'default'} beam={beam}"] = out
    save()
