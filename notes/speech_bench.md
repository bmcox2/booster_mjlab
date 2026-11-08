# Speech loop measurements

Numbers behind the choices in `speech_plan.md`. Laptop: i9-13900H, **CPU only** (the dGPU is
hidden by the BIOS since before 2026-11-08), campus Wi-Fi. Scripts in `speech/bench/`, raw results in
`speech/runs/_bench/` (gitignored). Test set so far: the 10 push-to-talk recordings from the first
session (4–19 s, 103 s total) and their replies. Step 2 replaces this with a fixed test set.

## 2026-11-08: v0 loop as built (per turn, from the 6-turn conversation)

| Stage | Time | Notes |
|---|---|---|
| STT (small.en, CPU, beam 5) | 1.55–2.23 s | Roughly constant per utterance |
| LLM (gpt-oss-20b, Groq) | 0.21–0.44 s (whole reply) | |
| TTS (Kokoro, CPU) | 1.45–3.86 s | Grows with reply length: ~0.4 s per second of speech |
| **End of speech → audio starts** | **~3.5–6 s** | Everything runs one after another |

## 2026-11-08: LLM on Groq (8 saved requests × 2, streamed)

| Model | First token median / p90 | First sentence median / p90 | Whole reply median | Reply words (median) |
|---|---|---|---|---|
| `openai/gpt-oss-20b` (reasoning low) | 0.23 / 0.33 s | 0.25 / 0.34 s | 0.25 s | 15 |
| `openai/gpt-oss-120b` (reasoning low) | 0.34 / 0.38 s | 0.35 / 0.42 s | 0.39 s | 20 |
| `qwen/qwen3.8-27b` | 0.29 / 0.50 s | 0.30 / 0.50 s | 0.32 s | 22 |

- **The LLM is not the bottleneck**: every model writes its whole 1–3 sentence reply in < 0.5 s.
  Streaming the LLM itself saves almost nothing; streaming *into TTS* is what matters.
- gpt-oss "thinks" ~12–14 hidden tokens first (reasoning low); qwen doesn't. All three keep to the
  1–3 sentence system prompt. Quality judgment needs the Step 6 eval set, not 16 replies.
- Groq free-tier limits (response headers, 2026-11-08), per model: **1,000 requests/day, 8,000
  tokens/minute**. A turn is ~200–1,000 tokens and grows with conversation history, so 8k TPM is
  the limit to watch in long conversations or benchmarks. Groq also hosts Whisper (STT, below).
- Groq's model list changed since the plan (Llama 3.1 8B gone). On 2026-11-08: gpt-oss-20b/120b,
  qwen3.8-27b, allam-2-7b, whisper-large-v3(-turbo), orpheus TTS (English + Arabic), prompt guards.

## 2026-11-08: STT (10 recordings, `speech/bench/stt.py`)

"Word diff" = word error rate against Groq `whisper-large-v3`, the biggest model. It is **not**
true accuracy: part of it is "um" kept or dropped, "two" vs "2", and punctuation. Real errors seen:
proper nouns ("Booster Lab" → "Ibusa Lab" / "Ibiza Lab" / "my booster lab"), dropped last words,
and cut-off endings on the one AirPods (Bluetooth call-mode) recording.

| Setup | Median | Max | Seconds per second of audio | Word diff |
|---|---|---|---|---|
| **Groq whisper-large-v3** (cloud, incl. upload) | **0.29 s** | 0.42 s | 0.035 | reference |
| Groq whisper-large-v3-turbo | 0.28 s | 0.39 s | 0.031 | 9.4% (drops last words twice) |
| CPU small.en, default threads, beam 5 (**current config**) | 1.58 s | 2.17 s | 0.18 | 11.9% |
| CPU small.en, 8 threads, beam 5 | 2.21 s | 2.82 s | 0.24 | 11.9% |
| CPU small.en, 8 threads, beam 1 | 2.38 s | 2.94 s | 0.23 | 11.5% |
| CPU base.en, 8 threads, beam 1 | 0.80 s | 1.51 s | 0.11 | 16.8% |
| CPU distil-large-v3, 8 threads | 10.8 s | 11.1 s | 1.22 | 9.8% |
| CPU large-v3-turbo, 8 threads | 11.2 s | 12.0 s | 1.21 | 10.1% |

- **Groq Whisper is ~5× faster than the current local setup and better**, on the same free key.
  Free tier: 2,000 transcription requests/day (headers; audio-seconds limits not shown in headers).
- On the CPU, `cpu_threads=8` and `beam_size=1` made small.en *slower*, not faster (the 13900H mixes
  fast P-cores and slow E-cores; the library's default does better). Large models are unusable on
  CPU (~11 s). The local fallback stays `small.en` with default settings until the GPU is back.
- Not tested yet: local GPU (dGPU missing), Parakeet / Nemotron (need NeMo; GPU), Whisper's
  `hotwords` / `initial_prompt` for "Booster", "K1", "SIGRobotics" (applies to Groq's `prompt` too).

## 2026-11-08: TTS (Kokoro `bm_daniel`, 8 replies, `speech/bench/tts.py`)

Replies are ~6 s of speech (median). "First sentence" = speaking only the first sentence, the
text-to-speech wait once speech is streamed sentence by sentence (plan step 4).

| torch threads | Whole reply median / max | First sentence median / max | Seconds per second of audio |
|---|---|---|---|
| 14 (default) | 2.28 / 3.49 s | 1.27 / 3.57 s | 0.39 |
| **4** | **1.99 / 3.09 s** | **1.00 / 3.07 s** | **0.34** |
| 8 | 2.94 / 4.34 s | 1.52 / 4.61 s | 0.50 |

(A second 14-thread pass gave 2.36 / 1.26 s, so run-to-run noise is ~5%.)

- **TTS is the bottleneck**, even streamed: ~1 s to the first sentence, up to 3 s when the first
  sentence is long. The < 1 s budget allows ~0.1–0.3 s here.
- 4 threads is fastest (same P-core/E-core effect as Whisper). Set `torch.set_num_threads(4)`.
- Ways to cut it, cheapest first: (1) first chunk = first clause / ~6–8 words, not a full sentence;
  (2) GPU once it's back; (3) a cloud TTS: Groq hosts Orpheus (`canopylabs/orpheus-v1-english`,
  same free key, **needs terms accepted in the Groq console**), or Cartesia / ElevenLabs / Deepgram
  free credits; (4) Kokoro ONNX build.

## Latency budget (2026-11-08 estimate, not measured end to end)

| Piece | v0 today | Streamed, best options measured | Plan target |
|---|---|---|---|
| End of turn (Enter today; VAD in step 3) | 0 | ~0.3–0.5 s | 0.2–0.3 s |
| STT | 1.6 s (CPU small.en) | **0.3 s** (Groq large-v3) | 0.05–0.15 s |
| LLM to first sentence | 0.25 s (waits for whole reply) | 0.25 s | 0.15–0.4 s |
| TTS to first audio | 2–4 s (whole reply) | **~1.0 s** (first sentence, 4 threads) | 0.1–0.2 s |
| **Total** | **~4–6 s** | **~1.9–2.1 s** | **< 1 s** |

So: switch STT to Groq and stream into TTS and we're at ~2 s; the last second has to come out of
TTS (shorter first chunk + GPU or cloud TTS) and the end-of-turn detector.

## 2026-11-08: Step 2, fixed test set (`speech.testset`, 12 recordings, laptop mic)

12 scripted items (`speech/testset/testset.json`): short questions, a one-word answer, project
names, fillers, 1 s and 2 s mid-sentence pauses, a 14 s ramble, a request needing a real answer,
a joke, a body request, and one from ~1 m away. Each replayed as its own one-turn conversation
(no mic, no speaker), so setups get identical audio. `speech_end` = the whole file is available,
like the second Enter in push-to-talk (no end-of-turn detection yet).

**STT, same audio, 12 items** (LLM gpt-oss-20b and Kokoro bm_daniel @ 4 threads in every run):

| STT setup | Median / p90 / max | Word errors (mean / worst) |
|---|---|---|
| Groq whisper-large-v3 + hints | 0.35 / 0.61 / 0.79 s | 10.1% / 60% |
| Groq whisper-large-v3, no hints | 0.33 / 0.41 / 0.49 s | 8.0% / 40% |
| **Groq whisper-large-v3-turbo + hints (new default)** | **0.33 / 0.41 / 0.43 s** | **3.8% / 20%** |
| Local small.en (CPU) + hints | 1.60 / 1.91 / 2.09 s | 8.1% / 40% |

- Two "errors" are likely the script, not Whisper: all 4 runs heard "how do you say what to say"
  (`pause_short`) and "look to the left" (`point`). Fix those references after listening; turbo
  then has ~1 real error in 12 items ("gestures" → "jesters").
- `short_wave` ("Can you wave at me?"): large-v3 heard "Can you hear any/me?" in 2/2 runs; turbo
  got it right. Short commands are where errors cost the most.
- Hints: "SIGRobotics" comes out as "SIG Robotics" with large-v3 either way; too few items to see
  a hint effect. Kept (cheap). The earlier 10-recording benchmark (no hints) had turbo dropping
  last words twice; not seen on the test set. Watch for it.
- Groq STT time doesn't grow much with length: 14 s ramble 0.34–0.61 s (upload included).

**Where the time goes (current setup, 12 items):** STT 0.35 s, LLM 0.29 s, **TTS 2.95 s (median),
4.83 s (p90), 6.01 s (max)**; reply ready 3.58 / 5.54 / 6.54 s. TTS = 82% of the median wait.
TTS time follows reply length, and the LLM ignores "short sentences" sometimes (`explain`: one
40-word sentence → 6 s of TTS).

**Streaming estimate** (same 12 replies; LLM first-sentence time + Kokoro on only the first piece):

| Speak first... | Reply ready median / p90 |
|---|---|
| whole reply (now) | 3.58 / 5.54 s |
| first sentence | 1.94 / 2.94 s |
| first chunk (first sentence, cut at a comma after ≥ 3 words or at 8 words) | **1.62 / 2.01 s** |

- **Kokoro on this CPU has a floor**: "Sure thing." (1.5 s of audio) takes 0.72 s; first chunks
  take 0.72–1.38 s. Later chunks keep up with playback (0.34–0.5 s per second of audio < 1), so
  streaming should play without gaps.
- So the floor today is ~0.35 (STT) + ~0.25 (LLM first sentence) + ~0.75 (TTS first chunk) ≈ 1.35 s,
  before end-of-turn detection (step 3) adds ~0.3–0.5 s.

## Latency budget (written 2026-11-08, after step 2)

Target: you stop talking → robot's voice starts, median < 1.0 s, p90 < 1.5 s.

| Piece | Measured now | Budget | How |
|---|---|---|---|
| End of turn | 0 (push-to-talk) | 0.25 s | Silero VAD + Smart Turn (step 3) |
| STT | 0.33 s (Groq turbo) | 0.30 s | Groq turbo; streaming STT only if this becomes the long pole |
| LLM to first sentence/chunk | 0.25–0.29 s | 0.25 s | Groq; prompt for a short opening phrase ("Sure.", "Good question.") |
| TTS to first audio | 0.72–1.4 s (CPU, first chunk) | **0.15 s** | **Needs GPU Kokoro or a cloud TTS**; CPU Kokoro can't |
| Hand-off to speaker | 0.035 s output latency | 0.05 s | |
| **Total** | **~1.6 s streamed estimate (without end of turn)** | **~1.0 s** | |

**Decision for step 4:** streaming to the first chunk is necessary but not enough; the TTS first
audio has to drop ~5×. Options to measure: (1) Kokoro on the GPU once it is back (expected
~0.05–0.1 s); (2) Groq Orpheus (`canopylabs/orpheus-v1-english`, same key, needs terms accepted);
(3) Cartesia / ElevenLabs Flash / Deepgram Aura free tiers (network ~0.1 s + model). Also: tell the
LLM to open with a short phrase, which shortens the first chunk for free.
