"""Hook to the gesture service (notes/gesture_plan.md step 6, main repo: `uv run gesture serve`).

Two services answer on the same address, and /health says which one is running:

- `uv run gesture serve` (step 6, offline): after each reply, the turn folder is posted, and the
  service makes the K1 motion for it in <turn>/gesture/.
- `uv run gesture live` (step 7): the K1 gestures live in a MuJoCo window. The reply's pieces are
  sent as they are voiced (`live_event`, called by streaming.stream_reply), each with the moment it
  will play, so its motion can start before its audio.

Everything is posted from background threads, so it never delays the conversation; if no service is
running, one warning is printed and the conversation carries on without motion. Settings:
[gesture] in config.toml.
"""

from __future__ import annotations

import base64
import json
import queue
import threading
import urllib.request
from pathlib import Path


class GestureClient:
    def __init__(self, cfg: dict):
        self.enabled = bool(cfg.get("enabled", False))
        self.url = str(cfg.get("url", "http://127.0.0.1:8765")).rstrip("/")
        self.timeout = float(cfg.get("timeout_s", 60))
        self.warned = False
        self.threads: list[threading.Thread] = []
        self.live = False
        self.turn_name = ""
        self.events: queue.Queue = queue.Queue()
        if self.enabled:
            try:
                with urllib.request.urlopen(self.url + "/health", timeout=2) as r:
                    h = json.load(r)
                self.live = bool(h.get("live"))
                print(f"[gesture] {'live' if self.live else 'offline'} service ready "
                      f"({h.get('units')} units, persona {h.get('speaker')})")
                if self.live:
                    threading.Thread(target=self._send_events, daemon=True).start()
            except Exception:
                print(f"[gesture] no service at {self.url}: replies won't get motion "
                      "(start it in the main repo: uv run gesture serve)")
                self.warned = True

    def start_turn(self, turn: Path) -> None:
        self.turn_name = f"{turn.parent.name}/{turn.name}"

    def live_event(self, kind: str, data: dict) -> None:
        """streaming.stream_reply's on_event: queue it for the live service (sent in order by one
        background thread; called from the TTS thread, so it must return at once)."""
        if not self.live:
            return
        body = {**data, "turn": self.turn_name}
        if "audio" in body:  # float32 samples -> 16-bit, base64 (a 3 s piece is ~190 kB)
            import numpy as np

            pcm = (np.clip(body["audio"], -1, 1) * 32767).astype("<i2")
            body["audio"] = base64.b64encode(pcm.tobytes()).decode()
        self.events.put((kind, body))

    def _send_events(self) -> None:
        while True:
            kind, body = self.events.get()
            req = urllib.request.Request(f"{self.url}/{kind}", data=json.dumps(body).encode(),
                                         headers={"Content-Type": "application/json"}, method="POST")
            try:
                urllib.request.urlopen(req, timeout=2).read()
            except Exception as e:
                if not self.warned:
                    print(f"[gesture] live service unreachable ({type(e).__name__}): no more live motion")
                    self.warned = True

    def submit(self, turn: Path) -> None:
        """Ask for this turn's motion, without waiting (offline service only)."""
        if not self.enabled or self.live or not (turn / "reply.wav").exists():
            return
        t = threading.Thread(target=self._post, args=(turn.resolve(),), daemon=True)
        t.start()
        self.threads.append(t)

    def _post(self, turn: Path) -> None:
        req = urllib.request.Request(self.url + "/reply", data=json.dumps({"turn": str(turn)}).encode(),
                                     headers={"Content-Type": "application/json"}, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                res = json.load(r)
            if not res.get("ok"):
                print(f"[gesture] {turn.name}: {res.get('error')}")
        except Exception as e:
            if not self.warned:
                print(f"[gesture] service unreachable ({type(e).__name__}): replies won't get motion")
                self.warned = True

    def wait(self, timeout: float = 30.0) -> None:
        """At the end of a session: let pending requests finish."""
        for t in self.threads:
            t.join(timeout)
