"""The gesture service: speech-loop replies in, K1 motion out (notes/gesture_plan.md step 6).

``uv run gesture serve`` keeps the library index loaded (2.8 s once) and listens on localhost. The speech
loop (``speech/src/speech/gesture.py``) posts each finished turn; the service generates that reply's
motion into ``<turn>/gesture/`` (the same files as ``gesture generate``) and writes the timings to
``<turn>/gesture/serve.json``.

Off-line for now: the speech loop posts after the robot has finished speaking, from a background
thread, so it never delays the conversation. Running motion live (and before its audio plays) is the
streaming step that comes next.

    GET  /health                      -> {"ok": true, "units": ...}
    POST /reply  {"turn": "<path>"}   -> {"ok": true, "dir": ..., "time_s": {...}} or {"ok": false, "error": ...}
"""

from __future__ import annotations

import json
import sys
import threading
import time
import traceback
from dataclasses import dataclass
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from booster_mjlab.gesture.generate import GenCfg, Units, generate


@dataclass
class ServeCfg:
    host: str = "127.0.0.1"
    port: int = 8765
    library: Path = GenCfg.library
    speaker: str | None = "9_miranda"
    """One persona for every reply, like ``gesture conversation``."""
    warm_up: bool = True
    """Generate one recorded reply at start, so the first real one isn't slowed by first-use setup."""


def serve(cfg: ServeCfg) -> None:
    sys.stdout.reconfigure(line_buffering=True)  # log lines appear right away, also when redirected to a file
    t0 = time.perf_counter()
    units = Units(cfg.library)
    lock = threading.Lock()  # one generation at a time (search and stitching use shared state)
    print(f"[serve] library loaded in {time.perf_counter() - t0:.1f} s ({len(units.a)} units)")

    def handle(turn: Path) -> dict:
        received = time.time()
        with lock:
            t1 = time.perf_counter()
            out = generate(GenCfg(reply=turn, library=cfg.library, out_dir=turn, speaker=cfg.speaker),
                           units=units, name="gesture")
            total = time.perf_counter() - t1
        plan = json.loads((out / "plan.json").read_text())
        ts = plan["time_s"]
        runtime = sum(ts[k] for k in ("features", "search", "stitch", "foot_lock", "ground"))
        info = {"ok": True, "dir": str(out), "received_unix": received, "total_s": total,
                "runtime_path_s": runtime, "time_s": ts, "reply_s": plan["reply_s"],
                "qc_severe": plan["qc"]["severe"], "segments": len(plan["segments"])}
        (out / "serve.json").write_text(json.dumps(info, indent=1))
        print(f"[serve] {turn.parent.name}/{turn.name}: {plan['reply_s']:.1f} s reply -> motion in {total:.2f} s "
              f"(runtime path {runtime * 1000:.0f} ms; QC {'ok' if not plan['qc']['severe'] else plan['qc']['severe']})")
        return info

    if cfg.warm_up:
        turns = sorted(p for p in Path("speech/runs").glob("*/turn_*") if (p / "tts.json").exists()
                       and not p.parent.name.startswith("_"))
        if turns:
            import shutil
            import tempfile

            with tempfile.TemporaryDirectory() as tmp:
                t = Path(tmp) / turns[-1].name
                shutil.copytree(turns[-1], t, ignore=shutil.ignore_patterns("gesture"))
                t1 = time.perf_counter()
                handle(t)
                print(f"[serve] warm-up done in {time.perf_counter() - t1:.1f} s")

    class Handler(BaseHTTPRequestHandler):
        def _send(self, code: int, body: dict) -> None:
            data = json.dumps(body).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):  # noqa: N802 (http.server's naming)
            if self.path == "/health":
                self._send(200, {"ok": True, "units": int(len(units.a)), "speaker": cfg.speaker})
            else:
                self._send(404, {"ok": False, "error": "unknown path"})

        def do_POST(self):  # noqa: N802
            if self.path != "/reply":
                self._send(404, {"ok": False, "error": "unknown path"})
                return
            try:
                body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
                turn = Path(body["turn"])
                if not (turn / "reply.wav").exists():
                    self._send(400, {"ok": False, "error": f"no reply.wav in {turn}"})
                    return
                self._send(200, handle(turn))
            except Exception as e:  # report to the speech loop instead of dying
                traceback.print_exc()
                self._send(500, {"ok": False, "error": f"{type(e).__name__}: {e}"})

        def log_message(self, *args):  # quiet: the [serve] lines say what happened
            pass

    server = ThreadingHTTPServer((cfg.host, cfg.port), Handler)
    print(f"[serve] listening on http://{cfg.host}:{cfg.port} (Ctrl-C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[serve] stopped")
