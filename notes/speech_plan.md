# Speech + LLM Conversation Loop: Plan

Step 2 of `roadmap.md`. Laptop only (Ubuntu 24.04, RTX 4070 8 GB), no robot. Written 2026-10-20;
options and versions checked online that day (sources at the end). Plan only, no code yet.

**Goal of the stage:** talk to the laptop and get a spoken reply that starts **< ~1 s** after you
stop talking, can be interrupted, and can call fake robot skills. Built so that every stage's
output can be inspected and replayed on its own, the same way `beat2_batch.py` caches per stage.

## Decisions before starting

| Decision | Recommendation | Why |
|---|---|---|
| LLM provider | **Groq free tier** first (OpenAI-compatible API, very fast first token), **Gemini Flash-Lite free tier** as the second cloud option, **Ollama + Qwen3-8B** as the local/offline baseline. All behind one client interface, switched by config. | Free, and no dependence on one subscription. Note: **Claude Pro does not include API access**; the Claude API is billed separately per token, so it's the paid upgrade path (e.g. Haiku), not the start. Free-tier limits change often (Gemini cut its free tier in April 2026; Cerebras moved to a one-time credit), so the interface must make switching a one-line change. |
| STT | **Local faster-whisper** (`large-v3-turbo`) for v0, chosen by measurement after step 2. Candidates later: Parakeet TDT 0.6B v3 (faster batch), Nemotron Speech streaming 0.6B (streaming), Deepgram Nova-3 / Flux (cloud, $200 free credit). | Batch Whisper is the simplest correct baseline; streaming only matters once data says STT is on the critical path. |
| TTS | **Local Kokoro-82M** for v0. Cloud comparisons later: Cartesia (free credits), ElevenLabs Flash (~10k chars/month free), Deepgram Aura-2 (uses the $200 credit). | Kokoro is free, good quality, small enough to share the 8 GB GPU. Cloud TTS has lower, more consistent first-audio latency; measure before deciding. |
| Budget | **$0** until the step 2/4 numbers show a paid service is needed. Set a hard spend cap on any account that has a card attached. | Matches "start free, upgrade when needed." |
| Audio setup | Headset for steps 1–4, laptop speakers + mic from step 5 (your choice). | Faces echo cancellation on the laptop before the robot, where speaker and mics share a body. |
| Code location | New folder `speech/` in this repo with **its own uv project/venv** (like GMR), on `gesture-tracking`. | Keeps audio/LLM dependencies out of the pinned mjlab venv; one repo for the whole project. |
| Language | English only. | Simplifies STT/turn-detection choices; BEAT2 English matches. |

## Pipeline shape (all steps)

```
mic ─► [capture] ─► input.wav ─► [STT] ─► transcript.json ─► [LLM] ─► reply.json ─► [TTS] ─► reply.wav ─► [playback] ─► speaker
                                                                     (text, tool calls)       (+ word timings)
runs/<session>/turn_NN/   one folder per turn: every arrow above is a saved file + timing.json
```

Each stage is a small module with a CLI that runs on saved inputs (e.g. re-run TTS on a saved
`reply.json` without speaking). Streaming (step 4) keeps the same stage boundaries, but passes
chunks through queues; the artifacts are still written for inspection.

---

## Step 1. v0: one turn at a time, batch, raw parts (2–3 sessions)

**Why first:** get every component working and see the data at each boundary (audio arrays,
transcripts, chat messages, audio out) before optimizing anything. Push-to-talk sidesteps
turn-taking, which is its own problem (step 3).

**Tasks**
1. `speech/` uv project, a config file (provider + model per stage), the `runs/` artifact layout.
2. Audio I/O with `sounddevice`: push-to-talk (Enter to start/stop) at 16 kHz mono → `input.wav`;
   play a WAV on the headset. List devices; pick the headset by name, not index.
3. STT: faster-whisper on `input.wav` → `transcript.json` (text, segments, word timestamps).
4. LLM: one client for OpenAI-compatible APIs (Groq, Gemini's OpenAI endpoint, Ollama). System
   prompt: plain spoken English, 1–3 sentences, no markdown or lists. Keep conversation history.
   Save `request.json` / `reply.json`.
5. TTS: Kokoro → `reply.wav`; play it. Loop for several turns.
6. Each stage runnable alone from saved files.

**Exit criteria:** a 5-turn conversation works; every artifact opens and makes sense; switching the
LLM provider is a config change; re-running one stage from saved files reproduces its output.

**Learn just in time:** digital audio (sample rate, PCM, int16 vs float32, mono/stereo, frames);
how Whisper turns audio into text; chat API messages (system/user/assistant roles, tokens).
- Hugging Face Audio Course (units 1, 5, 6): https://huggingface.co/learn/audio-course
- python-sounddevice docs: https://python-sounddevice.readthedocs.io

**Pitfalls:** sample-rate mismatches (Whisper wants 16 kHz, Kokoro outputs 24 kHz, devices often
run at 48 kHz); device indices change when the headset is plugged in; first call includes model
loading (warm up at start); LLM replies with markdown or long paragraphs; STT + TTS + Ollama
together can exceed 8 GB of VRAM (and the dGPU has dropped out before: keep CPU fallbacks).

## Step 2. Instrumentation (1 session)

**Why here:** v0 is the baseline. Every later choice (streaming, cloud vs local, framework) should
be decided by numbers, the same way the tracker work was decided by `eval-tracking`.

**Tasks**
1. Timestamp every event on one monotonic clock: speech end, STT done, LLM first token, LLM done,
   TTS first audio, playback start/end. Write `timing.json` per turn and append to `latency.jsonl`.
2. A summary script: median and p90 per stage, and end-of-speech → first-audio.
3. A fixed test set: ~10 recorded utterances (short questions, long rambles, mid-sentence pauses).
   Replay them from WAV so runs are comparable.
4. Benchmark matrix on that set: STT {faster-whisper turbo, Parakeet v3} × LLM {Groq small, Groq
   large, Gemini Flash-Lite, Ollama Qwen3-8B} × TTS {Kokoro, one cloud}. Record quality notes
   (wrong words, awkward replies), not just times.
5. Once: check the logged numbers against a phone recording of you + the laptop speaker.

**Exit criteria:** a table of per-stage medians/p90; you know which stage dominates; a written
latency budget for < 1 s (target shape: end-of-turn ~200–300 ms + STT ~50–150 + LLM first token
~150–400 + TTS first audio ~100–200 + playback buffer ~50).

**Learn:** time-to-first-token vs total time; real-time factor; p50 vs p90; cold vs warm calls.
- Voice AI & Voice Agents primer (latency chapter): https://voiceaiandvoiceagents.com

**Pitfalls:** counting model load in the timings; network variance on campus Wi-Fi (run many
trials); free-tier rate limits during benchmarks (Groq's free tier is ~30 requests/min, shared by
all your keys).

## Step 3. Voice activity detection and turn-taking (2 sessions)

**Why now:** replaces push-to-talk, and the wait for "has the user finished?" is often the
largest hidden latency. Streaming (step 4) starts from the end of the turn, so this comes first.

**Tasks**
1. Continuous mic stream in 32 ms frames → **Silero VAD (v6.2.x)** → speech start/end events.
   Keep ~300 ms of audio from before speech starts (pre-roll).
2. Baseline endpointing: end the turn after N ms of silence (try 500–800 ms).
3. Add **Smart Turn v3.2** (Pipecat's open end-of-turn model, BSD-2, ~8 MB, runs on CPU in ~12 ms;
   usable without Pipecat): when VAD hears silence, ask "is this turn finished?" so a short
   silence suffices when the sentence is complete and pauses like "so, um..." don't cut you off.
4. Save every detected utterance as a WAV with its endpoint decision (inspectable).
5. Tune on a test set with mid-sentence pauses, short answers ("yes"), and background noise.

**Exit criteria:** on 20 test turns, at most 1 cut off mid-sentence; median endpoint delay
< ~400 ms after the last word; no false turns from 1 min of typing / fan noise.

**Learn:** VAD (is someone speaking?) vs end-of-turn detection (are they done?); hangover and
pre-roll; why audio callbacks must never block (hand frames to a queue).
- Silero VAD README: https://github.com/snakers4/silero-vad
- Smart Turn v3 announcement + repo: https://www.daily.co/blog/announcing-smart-turn-v3-with-cpu-inference-in-just-12ms/ , https://github.com/pipecat-ai/smart-turn

**Pitfalls:** clipping the first syllable (pre-roll); keyboard clicks triggering VAD; laptop fan
noise; blocking work in the audio callback causing dropped frames.

## Step 4. Streaming, and the framework decision (3–4 sessions)

**Why now:** with numbers (step 2) and a real end-of-turn (step 3), you know exactly which waits
to overlap. Streaming means the robot starts speaking the first sentence while the LLM is still
writing the rest.

**Tasks**
1. Rewrite the loop with `asyncio` and queues between stages: LLM token stream → phrase/sentence
   chunker → TTS per chunk → playback queue. Artifacts still written per turn.
2. Measure. If STT is on the critical path, try streaming STT (Nemotron Speech streaming 0.6B
   locally, or Deepgram Flux, which also does turn detection) against batch on your test set.
   For short utterances batch STT is often fine.
3. Log per-chunk timing: when each audio chunk was generated and when it actually played.
4. **Framework spike (half a day):** rebuild the same loop in Pipecat with the same components;
   compare latency, code size, and how easy it is to inspect and change each stage.

**Framework trade-offs**

| | Own pipeline | Pipecat (1.x; 1.10 in Sept 2026) | LiveKit Agents (1.x) |
|---|---|---|---|
| Learning | Highest: you write every part | Medium: you configure its pieces | Lowest for audio internals |
| Inspectability | Full (your artifacts) | Good: frame pipeline, Python, local audio transport | Less: agent runs in a WebRTC room |
| Built-in | Nothing | Turn detection (Smart Turn), interruptions, many STT/LLM/TTS services, tool calls | Turn detector model, interruptions, WebRTC transport, telephony |
| Infrastructure | None | None for local audio | A LiveKit server (self-host or cloud) |
| Robot fit | Custom audio/gesture sync is easy to add | Custom processors can carry gesture timing | Strong if clients are remote (browser/phone), extra layer on a robot |
| Cost of switching later | — | Moderate (Python, same components) | Higher |

**Recommendation:** keep your own pipeline through this step (learning, inspectable stages, and
the gesture sync in step 7 needs custom timing anyway). Do the Pipecat spike, and adopt Pipecat
if barge-in / echo / turn-taking plumbing starts to dominate your time. LiveKit only if you later
need remote clients over WebRTC.

**Exit criteria:** end-of-speech → first audio **median < 1.0 s, p90 < 1.5 s** over 20 turns, with
no audible gaps between sentences; framework decision with numbers written in `log.md`.

**Learn:** asyncio tasks and queues (producer/consumer, backpressure); streaming HTTP (server-sent
events); chunking text for natural speech; audio buffers and underruns.
- Python asyncio docs: https://docs.python.org/3/library/asyncio.html
- Pipecat docs (pipelines and frames): https://docs.pipecat.ai

**Pitfalls:** chunks too small sound choppy, too large add latency; blocking model calls inside
the event loop (run them in a thread); gaps between TTS chunks; rate limits hit faster when
streaming many small requests.

## Step 5. Interruptions / barge-in (2–3 sessions)

**Why now:** it needs the concurrent pipeline from step 4, and what "cancel" means depends on how
the stages stream.

**Tasks**
1. Keep the mic open during playback. User speech (VAD + minimum ~200–300 ms, so "mm-hm" and noise
   don't count) → cancel: flush the playback buffer, cancel the LLM stream and pending TTS.
2. Keep history honest: truncate the assistant's last message to what was actually played (track
   played samples → words via TTS word timings).
3. Switch to **laptop speakers**. Enable PipeWire's echo-cancel module (WebRTC AEC) so the
   assistant's own voice doesn't trigger barge-in.
4. Test: talk over replies, backchannels ("yeah", "right"), silence.

**Exit criteria:** playback stops within ~200 ms of you starting to talk (measured); history
matches what was heard; on laptop speakers, 0 self-interruptions over 10 replies and ≥ 9/10 real
interruptions caught.

**Learn:** acoustic echo cancellation (the playback signal is the "far-end" reference subtracted
from the mic); double-talk; task cancellation in asyncio; keeping conversation state consistent.
- PipeWire echo-cancel module: https://docs.pipewire.org/page_module_echo_cancel.html

**Pitfalls:** a reported PipeWire issue says AEC works worse when mic and speaker are the same
device (the robot's case); backchannels causing false interruptions; cancelled tasks leaving audio
in buffers; everything here needs re-tuning on the K1's mic array and speaker.

## Step 6. Tool calling with fake robot tools (2–3 sessions)

**Why now:** the speech loop is solid, so you can see how tool calls interact with latency and
interruptions. This interface becomes the **brain-to-body boundary**, so design it before any real
body exists.

**Interface design**
- **Semantic arguments, not coordinates.** `look_at(target)`, `point_at(target)`,
  `wave(kind="hello"|"goodbye")`, `walk_to(target, max_distance_m)`, where `target` is
  `"user" | "left" | "right" | "object:<name>"`. The body resolves targets with its own perception;
  the LLM never sees joint angles or camera frames.
- **Non-blocking.** Each call returns immediately: `started` with an `action_id`, or `rejected` with
  a reason. Completion comes back as an event. Speech continues while the body acts.
- **The body owns safety.** A validator decides what's allowed in the current mode (e.g. stationary
  mode rejects `walk_to`), rate-limits, and cancels actions on barge-in or e-stop.
- **Two timing channels.** Tool calls for actions (wave, walk); **inline tags in the spoken text**
  for gestures tied to a word, e.g. `"Put it [point_at:object:table] over there"`, aligned to the
  audio with TTS word timestamps. Both go through one `Body` interface; the fake body prints with
  timestamps and simulates durations.
- Few tools, typed JSON Schema, versioned, descriptions written for the model. Every call saved as
  an artifact.

**Tasks:** write the schema and the fake body; handle tool calls in the streaming loop (speech must
not wait for them); an eval set of ~20 prompts with the expected tool calls; compare models
(small vs large on Groq, Gemini, local Qwen3-8B).

**Exit criteria:** ≥ 18/20 correct tool and arguments on the chosen model; tool calls add no delay
to the start of speech; rejected calls produce a sensible spoken reply.

**Learn:** the function-calling protocol (tool schema → tool call → tool result message); the
agent loop; why skills beat raw control (SayCan, Code as Policies in `papers.md`).
- Anthropic, "Writing effective tools for agents": https://www.anthropic.com/engineering/writing-tools-for-agents
- Groq tool use docs: https://console.groq.com/docs/tool-use

**Pitfalls:** small models invent tools or arguments; the model says "I'm waving" without calling
the tool; tool calls emitted before any speech, delaying the reply; free-tier limits during evals.

## Step 7. Integration hooks for later (notes only, don't build)

- **Taps.** TTS emits a stream of `AudioChunk(samples, sample_rate, start_sample, text_span,
  word_timings)`. The same stream feeds playback and a `GestureSink` (a no-op now; later the
  gesture generator). Inline gesture tags feed a `SemanticGestureSink` (the AMASS waves/points).
- **One timeline.** Record the playback start time t0 on a monotonic clock; a chunk plays at
  `t0 + start_sample / sample_rate + output_latency`. Gestures are scheduled on the same timeline.
  Log per-chunk play times from step 4 on, so sync can be measured later.
- **Lookahead.** The generator needs audio *before* it is played. Playback must be delayable by D =
  generator + retarget + tracker latency, which eats into the < 1 s budget. EMAGE generates whole
  utterances offline, so this needs a chunked generator or a text-driven fallback (`roadmap.md`
  risk).
- **Cancellation reaches the body.** Barge-in stops gestures too, so the tracker needs a clean
  return to idle (tracker exit criterion 5).
- **Robot/laptop split.** If STT/LLM/TTS run off-robot, audio and gesture references travel
  together with timestamps, and the robot plays both against its own clock (sync clocks with
  chrony/NTP, or schedule relative to the robot's playback start).

## Assumptions to check on the K1

| Question | Why it matters | What's known (unverified) |
|---|---|---|
| Compute variant | What can run onboard (STT/TTS, tracker) | Sources conflict: one datasheet lists three variants (48 / 117 / 200 TOPS), the Feishu manual lists Jetson Orin NX 16 GB (157 TOPS); `roadmap.md` lists QCS8550 / Orin NX 8 GB / AGX Orin 32 GB. Check on the unit (`jtop`, `/etc/nv_tegra_release`). |
| Mic array access | Your STT/VAD/AEC need raw or beamformed audio | Circular 6-mic array + speaker. Unknown whether it appears as a normal ALSA/PipeWire device or only through Booster's voice service; whether an echo-cancelled channel exists. |
| Speaker access | Your TTS playback and its timing | Unknown whether you can play audio directly, and what the output latency is. |
| Doubao integration | May hold the mic/speaker; may be reusable | Datasheet: Doubao LLM included, 6 months free. The SDK has a built-in agent mode (`enter_agent("hi_chat")`). Check: can it be disabled; does it lock the audio devices; can its ASR/TTS be used alone. |
| SDK | Control and audio from your code | `booster_robotics_sdk_python` on PyPI (Python bindings for the network control interface), C++ and ROS 2. Firmware must be current for all SDK functions. |
| Network | Off-robot LLM/TTS latency | Measure round-trip time from the robot to the laptop, the club GPU, and the cloud APIs. |

## Definition of done (whole stage)

- Hands-free spoken conversation on the laptop, on its speakers (not just the headset).
- End-of-speech → first audio: median < 1.0 s, p90 < 1.5 s, from `latency.jsonl`.
- Barge-in works without self-interruption; history matches what was heard.
- Fake robot tools called correctly (≥ 18/20) without delaying speech.
- Every stage's artifacts are inspectable and replayable; providers switch by config; $0 or a
  deliberate, capped spend.
- The step 7 hooks are written down, and per-chunk audio timing is logged.
- Findings, numbers and the framework decision recorded in `log.md`.

## Sources checked (2026-10-20)

- STT: [Parakeet vs Whisper vs Nemotron (OpenWhispr)](https://openwhispr.com/blog/parakeet-vs-whisper-vs-nemotron); [Nemotron ASR streaming (Together AI)](https://www.together.ai/models/nemotron-3-asr-streaming-0-6b); [Building voice agents with NVIDIA open models (Daily)](https://www.daily.co/blog/building-voice-agents-with-nvidia-open-models/)
- LLM free tiers: [Groq free plan (CostBench)](https://costbench.com/software/llm-api-providers/groq/free-plan/); [Gemini API pricing changes (agentdeals)](https://agentdeals.dev/gemini-api-pricing-changes); [Cerebras free tier (BenchLM)](https://benchlm.ai/md/free-tier/cerebras.md); [Running Qwen3-8B with Ollama (Codersera)](https://codersera.com/blog/running-qwen3-8b-on-windows-a-comprehensive-guide/amp/)
- TTS: [Kokoro-82M streaming ONNX](https://huggingface.co/msgflux/Kokoro-82M-streaming-onnx); [TTS pricing compared (invideo)](https://invideo.io/blog/ai-voice-model-pricing/); [ElevenLabs vs Cartesia (Coval)](https://www.coval.dev/blog/elevenlabs-vs-cartesia-which-tts-provider-is-right-for-your-voice-ai-project); [Deepgram pricing 2026](https://diyai.io/ai-tools/speech-to-text/deepgram-pricing-2026/)
- VAD / turn-taking: [Silero VAD 6.2.1 (pypistats)](https://pypistats.com/packages/silero-vad); [Smart Turn v3](https://www.daily.co/blog/announcing-smart-turn-v3-with-cpu-inference-in-just-12ms/), [v3.2](https://www.daily.co/blog/smart-turn-v3-2-handling-noisy-environments-and-short-responses/); [LiveKit turn detection](https://docs.livekit.io/agents/v1/build/turn-detection)
- Frameworks: [Pipecat 1.10 (aicybr)](https://aicybr.com/blog/pipecat-1-10-openai3-speechmatics-deepseek-migration); [LiveKit Agents 1.6.4 forum post](https://community.livekit.io/t/possible-audio-turndetector-cancellation-stall-in-python-agents-1-6-4/1597)
- Echo cancellation: [PipeWire echo-cancel](https://docs.pipewire.org/page_module_echo_cancel.html); [same-device AEC issue](https://gitlab.freedesktop.org/pipewire/pipewire/-/issues/2165)
- K1: [Booster K1 overview (Generation Robots)](https://www.generationrobots.com/blog/en/k1-from-booster-robotics-the-small-humanoid-that-challenges-unitree-and-nao/); [K1 datasheet](https://a.storyblok.com/f/298593/x/b1cf8e0cc4/booster-k1_englisch.pdf); [K1 manual (Feishu)](https://booster.feishu.cn/wiki/E3q5wF5SnitXZgkY18Uc8odBnXb); [K1 software setup (RoboticsCenter)](https://www.roboticscenter.ai/ja/hardware/booster-k1/software)

Most free-tier numbers come from third-party trackers and disagree with each other. Check each
provider's own console before relying on a limit.
