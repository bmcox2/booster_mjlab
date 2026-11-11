# speech/: the K1's conversation loop (laptop)

mic → speech-to-text → LLM → text-to-speech → speaker. Plan and steps: `../notes/speech_plan.md`;
measurements: `../notes/speech_bench.md`. Own uv project/venv (separate from mjlab).

## Setup
```
cd speech
uv sync
echo 'GROQ_API_KEY=<key from console.groq.com>' > .env   # gitignored
```
Audio devices are chosen in Ubuntu Settings → Sound (`config.toml` uses `pipewire` = the system choice).

## Run (from `speech/`)
| Command | What it does | Reads → writes (in `runs/<session>/turn_NN/`) |
|---|---|---|
| `uv run python -m speech.loop` | Whole conversation, push-to-talk (Enter / Enter, `q` to quit) | everything below |
| `uv run python -m speech.audio` | Record + play back (`--play FILE`, `--devices`) | mic → `input.wav` |
| `uv run python -m speech.stt [TURN]` | Speech-to-text (faster-whisper) | `input.wav` → `transcript.json` |
| `uv run python -m speech.llm [TURN]` | Reply (Groq, OpenAI-compatible API) | `transcript.json` → `request.json`, `reply.json` |
| `uv run python -m speech.tts [TURN]` | Text-to-speech (Kokoro) + play (`--no-play`) | `reply.json` → `reply.wav`, `tts.json` (word times) |
| `uv run python -m speech.voices [NAMES]` | Compare Kokoro voices | → `runs/_voices/<voice>.wav` |
| `uv run python -m speech.loop --hands-free` | Conversation without Enter presses (VAD ends your turn after `[vad] silence_ms`) | same files + `vad` info in `timing.json` |
| `uv run python -m speech.vad [--testset] [--silence-ms N]` | Live speech detector (saves each utterance), or replay the test set to see cut sentences | → `runs/_vad/<time>/utt_NN.wav/.json` |
| `uv run python -m speech.latency [--mode testset] [--last N]` | Median / p90 time per stage, per setup | `runs/latency.jsonl` |
| `uv run python -m speech.testset record [--only ID]` | Record the fixed test set (12 scripts) | → `testset/<id>.wav`, `testset/testset.json` |
| `uv run python -m speech.testset run [--set stt.provider=local ...]` | Replay the test set through the pipeline (no mic/speaker), score transcripts | → `runs/_testset/<time>/<id>/`, `runs/latency.jsonl` |

`TURN` defaults to the most recent turn. Models, voice and provider: `config.toml`.
Every turn also writes `timing.json` (events on one clock, 0 = you stopped talking) and a line in `runs/latency.jsonl`.
Streaming (`[stream]` in `config.toml`, on by default): the reply is cut into pieces at commas / sentence ends and each piece is voiced and played while the rest is still being made (`streaming.py`); `tts.json` lists every piece with when it was ready and when it played. Set `enabled = false` for the old one-stage-at-a-time loop.
Speech-to-text: Groq Whisper by default, local faster-whisper as automatic fallback (`[stt]` in `config.toml`).
`testset/*.wav` is your voice and is gitignored (the repo is public); `testset/testset.json` holds the correct transcripts.

## Gotchas
- Bluetooth headsets: using their mic switches them to call mode (HFP); AirPods were silent in it. Use the laptop mic.
- `faster-whisper` 1.2.1 needs `av<16` (pinned).
- A `VIRTUAL_ENV` warning means the mjlab venv is active; harmless (`deactivate` to silence).
