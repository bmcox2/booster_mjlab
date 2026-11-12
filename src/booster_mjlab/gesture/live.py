"""``uv run gesture live``: the K1 gesturing live while the speech loop talks (gesture_plan.md step 7).

One process, three threads:

- **control loop** (main thread): the tracking policy in plain MuJoCo (``sim2sim``'s robot), in real
  time: every 20 ms it reads one reference frame from the session timeline (``stream.MotionStream``),
  builds the observation the robot would build, and steps the physics. A MuJoCo window shows it.
  On the robot this loop becomes the deploy code; the rest stays.
- **planner**: keeps a few seconds of idle motion planned ahead of "now", and turns each event from
  the speech loop into motion on the timeline.
- **HTTP server** (localhost): receives the events and answers at once; the speech loop never waits.

Events (``speech/src/speech/gesture.py`` sends them; times are ``time.monotonic()``, which all
processes on one machine share):

    POST /begin  {turn, text, t}                      the reply's first words exist (not voiced yet)
    POST /piece  {turn, index, text, audio, sample_rate, words, play_time}   a voiced piece, queued to play
    POST /end    {turn, played: [...], ended}         the reply finished; when each piece really played
    GET  /health                                      {"ok": true, "live": true, ...}

Motion belongs 0.44 s *before* its audio (hands lead the voice). Pieces after the first are voiced
seconds before they play, so that's easy. The first piece plays the moment it is voiced: its motion
would start late, so at ``/begin`` (about 0.7 s earlier: the text exists, Kokoro is still voicing
it) a **pre-start** gesture begins, chosen without audio; the real piece takes over when it arrives.

Each run writes ``logs/gesture/live/<time>/``: ``pieces.jsonl`` (per piece: when its motion was ready
vs when its audio played), ``summary.json``, ``timeline.npz`` (the reference that was sent).

    uv run gesture live                                              # then start the speech loop
    uv run gesture live --replay-session speech/runs/<session> --replay-audio   # no mic: re-send a recorded session
    uv run gesture live --replay-session ... --no-viewer --push      # headless check
"""

from __future__ import annotations

import base64
import json
import queue
import subprocess
import sys
import threading
import time
from collections import deque
from dataclasses import dataclass
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import numpy as np
from scipy.signal import resample_poly

from booster_mjlab.gesture.generate import FPS, LEAD_S, GenCfg, Units
from booster_mjlab.gesture.stream import MotionStream, StreamCfg


@dataclass
class LiveCfg:
    wandb_run_path: str = "bmcox2-university-of-illinois-urbana-champaign/mjlab/y1r48dhc"
    policy: Path | None = None
    """policy.onnx (default: logs/sim2sim/<run>/policy.onnx, downloaded from W&B if missing)."""
    task: str = "Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation"
    host: str = "127.0.0.1"
    port: int = 8765
    library: Path = GenCfg.library
    speaker: str | None = "9_miranda"
    viewer: bool = True
    """Show the robot in a MuJoCo window."""
    pre_start: bool = True
    """Start gesturing when the reply's first words exist, before they are voiced."""
    margin_s: float = 0.1
    """A new plan only changes the timeline this far past now (its first frames are out in 30-50 ms)."""
    lookahead_s: float = 3.0
    """Idle motion is kept planned this far ahead."""
    fade_in_s: float = 2.0
    """At start: blend the reference from the standing pose to the timeline over this long."""
    push: bool = False
    """Random trunk pushes like training (every 1.5-4 s, up to 0.14 m/s)."""
    obs_delay_steps: int = 0
    """Sensor latency in control steps (20 ms each)."""
    replay_session: Path | None = None
    """Instead of a live speech loop: re-send this recorded session's events with their real timing."""
    replay_gap_s: float = 1.5
    """Replay: listening time between turns."""
    replay_audio: bool = False
    """Replay: play each reply's audio (paplay), to judge the sync by eye and ear."""
    replay_turns: int | None = None
    out_dir: Path = Path("logs/gesture/live")
    seed: int = 0


def _policy_path(cfg: LiveCfg) -> Path:
    if cfg.policy:
        return cfg.policy
    out = Path("logs/sim2sim") / cfg.wandb_run_path.split("/")[-1]
    if not (out / "policy.onnx").exists():
        import wandb

        wandb.Api().run(cfg.wandb_run_path).file("policy.onnx").download(root=str(out), replace=True)
    return out / "policy.onnx"


def _post(url: str, body: dict) -> None:
    import urllib.request

    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}, method="POST")
    urllib.request.urlopen(req, timeout=5).read()


def replay_events(session: Path, gap_s: float, max_turns: int | None = None) -> list[dict]:
    """A recorded speech-loop session as the events the live loop would have sent, with their
    recorded timing (``tts.json``: when each piece was ready and when it played). ``at``: seconds
    from the start of the replay."""
    from booster_mjlab.gesture import audio as A

    events, t = [], 2.0
    turns = sorted(session.glob("turn_*"), key=lambda p: int(p.name.split("_")[1]))
    for turn in turns[:max_turns]:
        if not (turn / "tts.json").exists() or not (turn / "timing.json").exists():
            continue
        tts = json.loads((turn / "tts.json").read_text())
        ev = json.loads((turn / "timing.json").read_text())["events"]
        chunks = tts.get("chunks") or []
        if not chunks or chunks[0].get("played_s") is None:
            continue
        x, rate = A.load_audio(turn / "reply.wav")
        base = t + gap_s  # the moment the user stopped talking
        name = f"{session.name}/{turn.name}"
        events.append({"at": base + ev.get("llm_first_chunk", chunks[0]["ready_s"] - 0.7), "path": "/begin",
                       "body": {"turn": name, "text": chunks[0]["text"]}})
        for c in chunks:
            a = c["start_sample"]
            b = a + round(c["audio_seconds"] * rate)
            pcm = (np.clip(x[a:b], -1, 1) * 32767).astype("<i2")
            words = [{"word": w["word"], "start": w["start"] - a / rate, "end": w["end"] - a / rate}
                     for w in tts["words"] if a / rate <= w["start"] < b / rate]
            events.append({"at": base + c["ready_s"], "path": "/piece", "play_at": base + c["played_s"],
                           "body": {"turn": name, "index": c["index"], "text": c["text"], "sample_rate": rate,
                                    "audio": base64.b64encode(pcm.tobytes()).decode(), "words": words}})
        end = base + ev.get("playback_end", chunks[-1]["played_s"] + chunks[-1]["audio_seconds"])
        events.append({"at": end, "path": "/end", "played_at": [base + c["played_s"] for c in chunks],
                       "body": {"turn": name}, "wav": str(turn / "reply.wav"), "wav_at": base + chunks[0]["played_s"]})
        t = end
    return sorted(events, key=lambda e: e["at"])


def live(cfg: LiveCfg) -> dict:
    sys.stdout.reconfigure(line_buffering=True)
    sys.setswitchinterval(0.001)  # the planner (Python) must not hold up the 20 ms control loop for long
    import mujoco

    import booster_mjlab.tasks  # noqa: F401  (first: fills the task registry; other import orders hit a circular import)
    from booster_mjlab.deploy import ObservationHistory, RefFrame, TrackingPolicy, build_observation
    from booster_mjlab.deploy import observation as ob
    from booster_mjlab.robots.booster_k1.k1_constants import HOME_KEYFRAME
    from booster_mjlab.scripts.sim2sim import build_sim, measure, physics_step

    t_load = time.perf_counter()
    policy = TrackingPolicy(_policy_path(cfg))
    sim = build_sim(cfg.task, policy)
    units = Units(cfg.library)
    gen = GenCfg(reply=Path("."), library=cfg.library, speaker=cfg.speaker, seed=cfg.seed)
    stream = MotionStream(units, policy.joint_names, gen, StreamCfg(margin_s=cfg.margin_s), seed=cfg.seed)
    while stream.n < round((cfg.lookahead_s + 2.0) * FPS):
        stream.extend_idle()
    print(f"[live] ready in {time.perf_counter() - t_load:.1f} s ({len(units.a)} units, persona {cfg.speaker}, "
          f"policy {policy.path.parent.name})")

    out = cfg.out_dir / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    out.mkdir(parents=True, exist_ok=True)
    dt = policy.control_dt
    clock = {"t0": None, "k": 0}
    jobs: queue.Queue = queue.Queue()
    stop = threading.Event()
    turns: dict[str, dict] = {}
    pieces: list[dict] = []
    stats = {"idle_plans": 0, "late_plans": 0, "plan_s": []}

    def now_frame() -> float:
        return (time.monotonic() - clock["t0"]) / dt

    def frame_time(f: float) -> float:
        return clock["t0"] + f * dt

    # ------------------------------------------------------------------------------- planner

    def handle(job: dict) -> None:
        kind, body, recv = job["kind"], job["body"], job["recv"]
        turn = turns.setdefault(body.get("turn", "?"), {"pieces": {}})
        if kind == "begin":
            if not cfg.pre_start:
                return
            # Long enough to cover voicing the first piece (~0.7 s) and the piece itself (~0.3 s per
            # word), in case the real piece never arrives.
            speech_s = 0.7 + max(1.0, 0.3 * len(body.get("text", "").split()))
            info = stream.pre_start(round(speech_s * FPS), int(now_frame()))
            if info:
                turn["pre_start"] = {"motion_start": frame_time(info["start_frame"]), "committed": time.monotonic(), "recv": recv}
            return
        if kind == "piece":
            pcm = np.frombuffer(base64.b64decode(body["audio"]), "<i2").astype(np.float64) / 32767
            rate = int(body["sample_rate"])
            if rate != 16000:
                g = np.gcd(rate, 16000)
                pcm = resample_poly(pcm, 16000 // g, rate // g)
            words = [(w["word"], float(w["start"]), float(w["end"])) for w in body.get("words", [])]
            play = float(body["play_time"])
            nf = int(now_frame())
            info = stream.speak(pcm, words, round((play - clock["t0"]) / dt), nf)
            done = time.monotonic()
            rec = {"turn": body["turn"], "index": int(body["index"]), "text": body.get("text", ""),
                   "audio_s": len(pcm) / 16000, "recv": recv, "committed": done, "play_expected": play,
                   "plan_s": done - job["start"], "queue_s": job["start"] - recv, "motion": info is not None}
            if info:
                rec.update(motion_start=frame_time(info["start_frame"]), first_changed=frame_time(info["first_frame"]),
                           late_frames=info["late_frames"], units=len(info["units"]),
                           stages_ms={k[:-2]: round(1000 * info[k]) for k in ("features_s", "search_s", "stitch_s", "foot_lock_s")})
                if info["first_publish"] > frame_time(info["first_frame"]):  # the loop had passed frames this plan changed
                    stats["late_plans"] += 1
                    rec["late_plan"] = True
                stats["plan_s"].append(rec["plan_s"])
            turn["pieces"][rec["index"]] = rec
            return
        if kind == "end":
            played = body.get("played") or []
            rows = []
            for i, rec in sorted(turn["pieces"].items()):
                play = played[i] if i < len(played) and played[i] is not None else rec["play_expected"]
                rec["play"] = play
                rec["ready_before_audio_s"] = play - rec["committed"]
                if rec["motion"]:
                    # > 0: the matched motion starts this long after where it belongs (0.44 s before the audio)
                    rec["start_late_s"] = rec["motion_start"] - (play - LEAD_S)
                if i == 0 and "pre_start" in turn:
                    rec["pre_start_before_audio_s"] = play - turn["pre_start"]["motion_start"]
                rec["rel"] = {k: round(rec[k] - play, 3) for k in ("recv", "committed", "motion_start") if k in rec}
                rows.append(rec)
                pieces.append(rec)
            with open(out / "pieces.jsonl", "a") as f:
                for rec in rows:
                    f.write(json.dumps(rec) + "\n")
            if rows:
                first = rows[0]
                pre = f", pre-start {first['pre_start_before_audio_s']:.2f} s before" if "pre_start_before_audio_s" in first else ""
                rest = [r["ready_before_audio_s"] for r in rows[1:]]
                worst = max((r.get("start_late_s", 0.0) for r in rows[1:]), default=0.0)
                print(f"[live] {body.get('turn')}: {len(rows)} pieces | first: matched motion "
                      f"{first.get('start_late_s', float('nan')) - LEAD_S:+.2f} s vs its audio{pre}"
                      + (f" | later pieces ready {min(rest):.2f}-{max(rest):.2f} s before their audio"
                         + (f" (one starts {worst:.2f} s late)" if worst > 0.02 else "") if rest else "")
                      + f" | planning {1000 * max(r['plan_s'] for r in rows):.0f} ms max")

    def planner() -> None:
        while not stop.is_set():
            try:
                job = jobs.get(timeout=0.02)
            except queue.Empty:
                job = None
            if clock["t0"] is None:
                if job:
                    jobs.put(job)
                    time.sleep(0.02)
                continue
            try:
                if job:
                    job["start"] = time.monotonic()
                    handle(job)
                nf = now_frame()
                if stream.n - nf < cfg.lookahead_s * FPS:
                    stream.extend_idle(int(nf) + round(cfg.margin_s * FPS))
                    stats["idle_plans"] += 1
            except Exception:
                import traceback

                traceback.print_exc()

    # ------------------------------------------------------------------------------- HTTP

    class Handler(BaseHTTPRequestHandler):
        def _send(self, code: int, body: dict) -> None:
            data = json.dumps(body).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):  # noqa: N802
            if self.path == "/health":
                self._send(200, {"ok": True, "live": True, "units": int(len(units.a)), "speaker": cfg.speaker})
            else:
                self._send(404, {"ok": False, "error": "unknown path"})

        def do_POST(self):  # noqa: N802
            recv = time.monotonic()
            try:
                body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
            except Exception as e:
                self._send(400, {"ok": False, "error": str(e)})
                return
            kind = self.path.strip("/")
            if kind in ("begin", "piece", "end"):
                jobs.put({"kind": kind, "body": body, "recv": recv})
                self._send(200, {"ok": True})
            elif kind == "reply":  # the offline service's request: motion is already made live
                self._send(200, {"ok": True, "live": True})
            else:
                self._send(404, {"ok": False, "error": "unknown path"})

        def log_message(self, *args):
            pass

    server = ThreadingHTTPServer((cfg.host, cfg.port), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    threading.Thread(target=planner, daemon=True).start()
    url = f"http://{cfg.host}:{cfg.port}"

    def replayer() -> None:
        events = replay_events(cfg.replay_session, cfg.replay_gap_s, cfg.replay_turns)
        start = time.monotonic()
        print(f"[live] replaying {cfg.replay_session} ({sum(e['path'] == '/end' for e in events)} replies, "
              f"{events[-1]['at']:.0f} s)")
        played = set()
        for e in events:
            time.sleep(max(0.0, start + e["at"] - time.monotonic()))
            body = dict(e["body"])
            if e["path"] == "/begin":
                body["t"] = time.monotonic()
            elif e["path"] == "/piece":
                body["play_time"] = start + e["play_at"]
                if cfg.replay_audio and body["turn"] not in played and body["index"] == 0:
                    played.add(body["turn"])
                    wav = next(x["wav"] for x in events if x["path"] == "/end" and x["body"]["turn"] == body["turn"])
                    delay = max(0.0, start + e["play_at"] - time.monotonic())
                    threading.Timer(delay, lambda w=wav: subprocess.Popen(["paplay", w])).start()
            else:
                body["played"] = [start + p for p in e["played_at"]]
            _post(url + e["path"], body)
        time.sleep(3.0)
        stop.set()

    # ------------------------------------------------------------------------------- control loop

    def reset_robot() -> None:
        d = sim.data
        mujoco.mj_resetData(sim.model, d)
        d.qpos[:3] = HOME_KEYFRAME.pos
        d.qpos[3:7] = (1, 0, 0, 0)
        d.qpos[sim.qadr] = policy.default_joint_pos
        d.ctrl[sim.ctrl] = policy.default_joint_pos
        mujoco.mj_forward(sim.model, d)

    reset_robot()
    viewer = None
    if cfg.viewer:
        import mujoco.viewer

        viewer = mujoco.viewer.launch_passive(sim.model, sim.data, show_left_ui=False, show_right_ui=False)
        viewer.cam.type = mujoco.mjtCamera.mjCAMERA_TRACKING
        viewer.cam.trackbodyid = sim.trunk
        viewer.cam.distance, viewer.cam.elevation, viewer.cam.azimuth = 2.2, -10.0, 150.0

    rng = np.random.default_rng(cfg.seed)
    history = ObservationHistory(policy.frame_dims, policy.history_length)
    states: deque = deque(maxlen=cfg.obs_delay_steps + 1)
    last_action = np.zeros(policy.num_joints)
    fade_from, fade_k0 = policy.default_joint_pos.copy(), 0
    fade_n = round(cfg.fade_in_s * FPS)
    next_push = rng.uniform(1.5, 4.0)
    lateness, falls, drift, skipped = [], [], 0.0, 0
    start_xy = sim.data.xpos[sim.trunk][:2].copy()
    clock["t0"] = time.monotonic()
    if cfg.replay_session:
        threading.Thread(target=replayer, daemon=True).start()
    print(f"[live] running; events on {url}" + ("" if cfg.replay_session else " (start the speech loop; Ctrl-C to stop)"))
    import signal

    # `kill` (tools/live_test.sh) and Ctrl-C both end the loop cleanly, so the summary is written.
    # (A process started in the background by a script has Ctrl-C switched off unless set here.)
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, lambda *_: stop.set())
    k = 0
    try:
        while not stop.is_set() and (viewer is None or viewer.is_running()):
            target = clock["t0"] + k * dt
            wait = target - time.monotonic()
            if wait > 0:
                time.sleep(wait)
            elif wait < -0.5:  # far behind (the laptop stalled): skip ahead instead of racing to catch up
                jump = int(-wait / dt)
                k += jump
                skipped += jump
                continue
            lateness.append(max(0.0, -wait))
            clock["k"] = k
            jp, jv, aq = stream.frame(k)
            if k - fade_k0 < fade_n:  # from the standing pose into the timeline
                w = (k - fade_k0) / fade_n
                w = w * w * (3 - 2 * w)
                jp, jv = (1 - w) * fade_from + w * jp, w * jv
            states.append(measure(sim))
            obs = history(build_observation(policy.observation_names, policy.frame_dims, states[0],
                                            RefFrame(jp, jv, aq), last_action, policy.default_joint_pos))
            last_action = policy.act(obs)
            sim.data.ctrl[sim.ctrl] = policy.joint_targets(last_action)
            for _ in range(sim.decimation):
                physics_step(sim)
            k += 1
            t = k * dt
            if cfg.push and t >= next_push:
                sim.data.qvel[0:2] += rng.uniform(-0.14, 0.14, 2)
                next_push = t + rng.uniform(1.5, 4.0)
            d = sim.data
            drift = max(drift, float(np.linalg.norm(d.xpos[sim.trunk][:2] - start_xy)))
            if d.xpos[sim.trunk][2] < 0.30 or ob.quat_to_matrix(d.xquat[sim.trunk])[2, 2] < 0.5:
                falls.append(round(t, 2))
                print(f"[live] FELL at {t:.1f} s; standing the robot up again")
                reset_robot()
                history.reset()
                states.clear()
                last_action[:] = 0
                fade_k0 = k
            if viewer is not None and time.monotonic() - target < dt:
                viewer.sync()
    except KeyboardInterrupt:
        pass
    stop.set()
    server.shutdown()
    if viewer is not None:
        viewer.close()

    # ------------------------------------------------------------------------------- summary
    late = np.array(lateness) if lateness else np.zeros(1)
    later = [p["ready_before_audio_s"] for p in pieces if p["index"] > 0]
    first = [p for p in pieces if p["index"] == 0]
    first_late = [p["start_late_s"] for p in first if "start_late_s" in p]
    pre = [p["pre_start_before_audio_s"] for p in first if "pre_start_before_audio_s" in p]
    summary = {
        "seconds": k * dt, "falls": falls, "max_drift_cm": 100 * drift, "replies": len(first), "pieces": len(pieces),
        "pieces_without_motion": sum(not p["motion"] for p in pieces),
        "later_pieces_ready_before_audio_s": {"min": min(later), "median": float(np.median(later))} if later else None,
        "later_pieces_under_lead": sum(x < LEAD_S for x in later),
        "later_pieces_start_late_s": sorted(round(p["start_late_s"], 3) for p in pieces if p["index"] > 0 and p.get("start_late_s", 0) > 0.02),
        "first_piece_matched_start_vs_ideal_s": {"median": float(np.median(first_late)), "max": max(first_late)} if first_late else None,
        "pre_start_before_audio_s": {"median": float(np.median(pre)), "min": min(pre)} if pre else None,
        "planning_ms": {"median": 1000 * float(np.median(stats["plan_s"])), "max": 1000 * max(stats["plan_s"])} if stats["plan_s"] else None,
        "plans_too_late": stats["late_plans"], "frames_without_reference": stream.starved, "foot_lock_unreachable": stream.lock_fails,
        "loop_late_ms": {"median": 1000 * float(np.median(late)), "p99": 1000 * float(np.percentile(late, 99)), "max": 1000 * float(late.max())},
        "frames_skipped": skipped, "pre_start": cfg.pre_start, "push": cfg.push, "obs_delay_steps": cfg.obs_delay_steps,
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=1))
    np.savez(out / "timeline.npz", **stream.snapshot(k))
    print(f"[live] {summary['seconds']:.0f} s, {len(first)} replies, {len(pieces)} pieces | falls {len(falls)}, "
          f"max drift {summary['max_drift_cm']:.1f} cm | loop late p99 {summary['loop_late_ms']['p99']:.1f} ms")
    if later:
        print(f"[live] pieces after the first: motion ready {np.median(later):.2f} s before its audio (median; min {min(later):.2f}; "
              f"{summary['later_pieces_under_lead']} of {len(later)} under {LEAD_S} s)")
    if first_late:
        print(f"[live] first pieces: matched motion starts {np.median(first_late):.2f} s later than ideal (max {max(first_late):.2f})"
              + (f"; pre-start begins {np.median(pre):.2f} s before the audio (min {min(pre):.2f})" if pre else ""))
    print(f"[live] -> {out}")
    return summary
