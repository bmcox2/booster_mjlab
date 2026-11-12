"""Hook to the gesture service (notes/gesture_plan.md step 6, main repo: `uv run gesture serve`).

After each reply, the turn folder is posted to the service, which makes the K1 motion for it in
<turn>/gesture/. Posting happens on a background thread after the robot has finished speaking, so it
never delays the conversation; if the service isn't running, one warning is printed and the
conversation carries on without motion. Settings: [gesture] in config.toml.
"""

from __future__ import annotations

import json
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
        if self.enabled:
            try:
                with urllib.request.urlopen(self.url + "/health", timeout=2) as r:
                    h = json.load(r)
                print(f"[gesture] service ready ({h.get('units')} units, persona {h.get('speaker')})")
            except Exception:
                print(f"[gesture] no service at {self.url}: replies won't get motion "
                      "(start it in the main repo: uv run gesture serve)")
                self.warned = True

    def submit(self, turn: Path) -> None:
        """Ask for this turn's motion, without waiting."""
        if not self.enabled or not (turn / "reply.wav").exists():
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
