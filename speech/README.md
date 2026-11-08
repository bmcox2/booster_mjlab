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

`TURN` defaults to the most recent turn. Models, voice and provider: `config.toml`.

## Gotchas
- Bluetooth headsets: using their mic switches them to call mode (HFP); AirPods were silent in it. Use the laptop mic.
- `faster-whisper` 1.2.1 needs `av<16` (pinned).
- A `VIRTUAL_ENV` warning means the mjlab venv is active; harmless (`deactivate` to silence).
