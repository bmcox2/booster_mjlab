"""Load config.toml and .env so every stage reads the same settings."""

import tomllib
from pathlib import Path

from dotenv import load_dotenv

# speech/ folder (this file is speech/src/speech/config.py, so go up 3 levels).
SPEECH_DIR = Path(__file__).resolve().parents[2]
RUNS_DIR = SPEECH_DIR / "runs"


def latest_turn() -> Path:
    """The most recent runs/<session>/turn_NN folder (so stages can run on 'the last recording')."""
    turns = sorted(RUNS_DIR.glob("*/turn_*"))
    turns = [t for t in turns if not t.parent.name.startswith("_")]  # skip test folders like _setup_check
    if not turns:
        raise SystemExit(f"No recordings in {RUNS_DIR}. Record one first: uv run python -m speech.audio")
    return turns[-1]


def load_config() -> dict:
    """Read speech/config.toml into a dict, and put .env's keys (GROQ_API_KEY) in the environment."""
    load_dotenv(SPEECH_DIR / ".env")
    with open(SPEECH_DIR / "config.toml", "rb") as f:
        return tomllib.load(f)
