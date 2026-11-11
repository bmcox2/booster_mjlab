"""Timestamps for one turn, all on one clock, saved as timing.json + one line in runs/latency.jsonl.

Every event is "seconds since you stopped talking" (speech_end = 0), measured with
time.monotonic(): a clock that only moves forward and is not changed by the system clock syncing,
so differences between two readings are reliable.

Events (in order):
    speech_end       you stopped talking (push-to-talk: second Enter; hands-free: your last sound)
    endpoint         decided your turn is over (push-to-talk: same as speech_end; hands-free:
                     after silence_ms of silence)
    stt_done         transcript ready
    llm_first_token  first piece of the reply arrived
    llm_first_sentence  first full sentence arrived (when streamed TTS could start, step 4)
    llm_first_chunk  first speakable piece of the reply complete (streaming)
    tts_first_audio  first piece voiced (streaming): the robot can start talking
    llm_done         whole reply arrived
    tts_done         whole reply voiced
    playback_start   audio handed to the speaker; you hear it output_latency_s later
    playback_end     audio finished
"""

import json
import time
from pathlib import Path

from speech.config import RUNS_DIR

LATENCY_LOG = RUNS_DIR / "latency.jsonl"

# Stage name -> (from event, to event).
STAGES = {
    "endpoint": ("speech_end", "endpoint"),  # waiting to be sure you're done (0 with push-to-talk)
    "stt": ("endpoint", "stt_done"),
    "llm_first_token": ("stt_done", "llm_first_token"),
    "llm_first_sentence": ("stt_done", "llm_first_sentence"),
    "llm_total": ("stt_done", "llm_done"),
    "llm_first_chunk": ("stt_done", "llm_first_chunk"),
    "tts_first_chunk": ("llm_first_chunk", "tts_first_audio"),
    "first_audio": ("speech_end", "tts_first_audio"),  # streaming: audio could start here
    "tts": ("llm_done", "tts_done"),
    "reply_ready": ("speech_end", "tts_done"),  # = response minus the hand-off to the speaker
    "handoff": ("tts_done", "playback_start"),
    "response": ("speech_end", "playback_start"),  # the number to get under 1 s
}


class TurnTimer:
    def __init__(self, start: float | None = None):
        self.t0 = start if start is not None else time.monotonic()
        self.wall_start = time.time()  # calendar time, only for labeling
        self.events = {"speech_end": 0.0}
        self.extra = {}

    def mark(self, event: str, at: float | None = None) -> None:
        """Record that `event` happened now (or at monotonic time `at`)."""
        self.events[event] = round((at if at is not None else time.monotonic()) - self.t0, 4)

    def stages(self) -> dict:
        return {name: round(self.events[b] - self.events[a], 4)
                for name, (a, b) in STAGES.items() if a in self.events and b in self.events}

    def save(self, turn: Path, meta: dict) -> dict:
        """Write turn/timing.json and append the same record to runs/latency.jsonl."""
        record = {"session": turn.parent.name, "turn": turn.name,
                  "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.wall_start)),
                  **meta, "events": self.events, "stages": self.stages(), **self.extra}
        (turn / "timing.json").write_text(json.dumps(record, indent=2, ensure_ascii=False))
        LATENCY_LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(LATENCY_LOG, "a") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        return record


def config_label(cfg: dict) -> str:
    """Short name for the setup, so the summary can group turns run with the same settings."""
    stt = cfg["stt"]
    stt_name = (f"groq/{stt['groq']['model']}" if stt["provider"] == "groq"
                else f"local/{stt['local']['model']}")
    if stt.get("prompt"):
        stt_name += "+hints"
    stream = "+stream" if cfg.get("stream", {}).get("enabled") else ""
    return (f"stt={stt_name} | llm={cfg['llm']['model']} | "
            f"tts={cfg['tts']['voice']}@{cfg['tts'].get('cpu_threads', 'default')}threads{stream}")
