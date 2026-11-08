"""Text-to-speech (Kokoro) benchmark on the robot's saved replies (runs/2026*/turn_*/reply.json).

Run (from speech/):  uv run python bench/tts.py
For each CPU thread count: time to speak the whole reply vs only its first sentence.
The first-sentence time is roughly the text-to-speech wait once replies are streamed
sentence by sentence (speech_plan step 4).
Results: runs/_bench/tts.json (rewritten after each setting).
"""
import json, re, statistics, warnings
from pathlib import Path

import torch

warnings.simplefilter("ignore")
from speech.config import load_config  # noqa: E402
from speech.tts import TextToSpeech  # noqa: E402

SPEECH = Path(__file__).resolve().parents[1]
OUT = SPEECH / "runs/_bench/tts.json"
OUT.parent.mkdir(parents=True, exist_ok=True)

texts = [json.loads(p.read_text())["text"] for p in sorted(SPEECH.glob("runs/2026*/turn_*/reply.json"))]
cfg = load_config()["tts"]
default_threads = torch.get_num_threads()
print(len(texts), "replies, voice", cfg["voice"], "| default torch threads", default_threads, flush=True)
tts = TextToSpeech(cfg)


def first_sentence(text):
    return re.split(r"(?<=[.!?])\s+", text.strip())[0]


rows = []
for threads in [default_threads, 4, 8, 14]:
    torch.set_num_threads(threads)
    tts.synthesize("Warm up.")
    full, first, audio_s = [], [], []
    for text in texts:
        _, info = tts.synthesize(text)
        full.append(info["synthesize_seconds"])
        audio_s.append(info["audio_seconds"])
        first.append(tts.synthesize(first_sentence(text))[1]["synthesize_seconds"])
    rows.append({"threads": threads, "full_median_s": statistics.median(full), "full_max_s": max(full),
                 "reply_audio_median_s": statistics.median(audio_s),
                 "first_sentence_median_s": statistics.median(first), "first_sentence_max_s": max(first),
                 "s_per_audio_s": statistics.median(f / a for f, a in zip(full, audio_s))})
    OUT.write_text(json.dumps(rows, indent=1))
    print(json.dumps(rows[-1]), flush=True)
