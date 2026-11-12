"""``uv run gesture live-video --run logs/gesture/live/<time>``: film a ``gesture live`` run afterwards.

Nothing is recorded during the conversation (rendering frames live would take CPU from Kokoro).
Instead, ``live`` saves every reference frame the tracker read (``timeline.npz``), in order. A plan
only ever replaces frames after "now", so these are exactly the frames the robot tracked; running
the same ``Tracker`` on them again (same start, same seed, deterministic physics) gives the same motion,
which is then rendered at 50 fps. ``final_qpos`` (saved at the end of the run) checks it.

The soundtrack is put together from the speech-loop session on the same clock (``time.monotonic()``):
each reply piece at the moment it really played (``pieces.jsonl``), and the user's voice (``input.wav``)
ending where the speech loop decided the turn was over. Both voices are brought to the same level.

Output: ``<run>/live.mp4`` (with sound) and ``<run>/live_silent.mp4``.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.signal import resample_poly

from booster_mjlab.gesture import audio as A
from booster_mjlab.gesture.generate import FPS

RATE = 24000  # soundtrack sample rate (Kokoro's)


@dataclass
class LiveVideoCfg:
    run: Path
    """A folder written by ``gesture live`` (logs/gesture/live/<time>)."""
    runs_dir: Path = Path("speech/runs")
    width: int = 960
    height: int = 720
    user_voice: bool = True
    """Put the user's voice in the soundtrack too (from each turn's input.wav)."""


def _t0(run: Path, z, pieces: list[dict]) -> float:
    """The run's clock start (monotonic). Runs before 2026-11-11 22:30 didn't save it: recover it from
    the first speaking frame of each reply, whose time ``pieces.jsonl`` records (``motion_start``)."""
    if "t0_monotonic" in z.files:
        return float(z["t0_monotonic"])
    kind = z["kind"]
    starts = np.flatnonzero((kind[1:] == 1) & (kind[:-1] != 1)) + 1  # into "speaking" from idle / pre-start
    firsts = [p for p in pieces if p["index"] == 0 and "motion_start" in p]
    est = []
    for f in starts:  # match each piece-0 start to the kind change nearest its own estimate
        for p in firsts:
            est.append(p["motion_start"] - f / FPS)
    est = np.array(est)
    # The right t0 is the value shared by every reply (one per reply); wrong pairings scatter.
    best = max(est, key=lambda e: np.sum(np.abs(est - e) < 1e-3))
    n = int(np.sum(np.abs(est - best) < 1e-3))
    if n < max(1, len(firsts) // 2):
        raise SystemExit(f"{run}: no t0_monotonic and couldn't recover it ({n} of {len(firsts)} replies agree)")
    return float(np.median(est[np.abs(est - best) < 1e-3]))


def soundtrack(run: Path, t0: float, seconds: float, cfg: LiveVideoCfg, replay: bool) -> np.ndarray:
    pieces = [json.loads(line) for line in (run / "pieces.jsonl").read_text().splitlines() if line.strip()]
    track = np.zeros(int(seconds * RATE) + RATE)

    def put(x: np.ndarray, at: float) -> None:
        a = int(round((at - t0) * RATE))
        if a < 0:
            x, a = x[-a:], 0
        n = max(0, min(len(x), len(track) - a))
        track[a:a + n] += x[:n]

    by_turn: dict[str, list[dict]] = {}
    for p in pieces:
        by_turn.setdefault(p["turn"], []).append(p)
    missing = []
    for name, ps in by_turn.items():
        turn = cfg.runs_dir / name
        if not (turn / "tts.json").exists():
            missing.append(name)
            continue
        tts = json.loads((turn / "tts.json").read_text())
        timing = json.loads((turn / "timing.json").read_text())
        reply, rate = A.load_audio(turn / "reply.wav")
        if rate != RATE:
            g = np.gcd(rate, RATE)
            reply = resample_poly(reply, RATE // g, rate // g)
        reply = A.match_level(reply, rate=RATE)
        chunks = {c["index"]: c for c in tts["chunks"]}
        for p in ps:
            c = chunks[p["index"]]
            a = round(c["start_sample"] * RATE / tts["sample_rate"])
            put(reply[a:a + round(c["audio_seconds"] * RATE)], p["play"])
        if cfg.user_voice and (turn / "input.wav").exists():
            # The turn's clock starts at the user's last sound. A live piece's play time includes the
            # speaker's output latency; a replayed one doesn't.
            p0 = min(ps, key=lambda p: p["index"])
            latency = 0.0 if replay else float(timing.get("output_latency_s", 0.0))
            speech_end = p0["play"] - chunks[p0["index"]]["played_s"] - latency
            x, r = A.load_audio(turn / "input.wav")
            if r != RATE:
                g = np.gcd(r, RATE)
                x = resample_poly(x, RATE // g, r // g)
            end = speech_end + timing["events"].get("endpoint", 0.0)  # the recording runs to the turn's end
            put(A.match_level(x, rate=RATE), end - len(x) / RATE)
    if missing:
        print(f"[live-video] no session files for {len(missing)} turns (e.g. {missing[0]}): their audio is missing")
    return np.clip(track[: int(seconds * RATE)], -1, 1)


def live_video(cfg: LiveVideoCfg) -> Path:
    import mujoco

    import booster_mjlab.tasks  # noqa: F401  (fills the task registry first; see live.py)
    from booster_mjlab.deploy import TrackingPolicy
    from booster_mjlab.gesture.live import Tracker
    from booster_mjlab.scripts.sim2sim import build_sim

    run = cfg.run
    summary = json.loads((run / "summary.json").read_text())
    z = np.load(run / "timeline.npz")
    pieces = [json.loads(line) for line in (run / "pieces.jsonl").read_text().splitlines() if line.strip()] \
        if (run / "pieces.jsonl").exists() else []
    if summary.get("frames_skipped"):
        print(f"[live-video] warning: the live loop skipped {summary['frames_skipped']} frames (stalled); the film won't match there")
    policy = TrackingPolicy(Path(summary.get("policy", "logs/sim2sim/y1r48dhc/policy.onnx")))
    sim = build_sim(summary.get("task", "Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation"), policy)
    sim.model.vis.global_.offwidth = max(sim.model.vis.global_.offwidth, cfg.width)
    sim.model.vis.global_.offheight = max(sim.model.vis.global_.offheight, cfg.height)
    tracker = Tracker(policy, sim, summary.get("push", False), summary.get("obs_delay_steps", 0),
                      summary.get("seed", 0), summary.get("fade_in_s", 2.0))
    jp, jv, aq = z["joint_pos"], z["joint_vel"], z["anchor_quat"]
    steps = int(z["steps"]) if "steps" in z.files else len(jp)
    renderer = mujoco.Renderer(sim.model, cfg.height, cfg.width)
    cam = mujoco.MjvCamera()
    cam.distance, cam.elevation, cam.azimuth = 2.2, -10.0, 150.0
    silent = run / "live_silent.mp4"
    ffmpeg = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                               "-s", f"{cfg.width}x{cfg.height}", "-r", str(FPS), "-i", "-", "-c:v", "libx264",
                               "-pix_fmt", "yuv420p", "-crf", "20", str(silent)], stdin=subprocess.PIPE)
    print(f"[live-video] {run.name}: {steps / FPS:.0f} s, re-running the tracker on the frames it read and rendering...")
    for k in range(steps):
        if k < len(jp):
            tracker.step(k, jp[k], jv[k], aq[k])
        else:  # past the published end: the live loop held the last frame, standing still
            tracker.step(k, jp[-1], np.zeros_like(jv[-1]), aq[-1])
        cam.lookat[:] = sim.data.xpos[sim.trunk] - [0, 0, 0.2]
        renderer.update_scene(sim.data, cam)
        ffmpeg.stdin.write(renderer.render().tobytes())
    ffmpeg.stdin.close()
    ffmpeg.wait()
    if "final_qpos" in z.files:
        err = float(np.abs(sim.data.qpos - z["final_qpos"]).max())
        print(f"[live-video] same motion as live: {'yes' if err < 1e-6 else 'NO'} (largest difference at the end {err:.1e})")
    if tracker.falls != summary.get("falls", []):
        print(f"[live-video] warning: falls differ (live {summary.get('falls')}, now {tracker.falls})")

    out = run / "live.mp4"
    if not pieces:
        silent.replace(out)
        print(f"[live-video] no replies in this run: no sound -> {out}")
        return out
    t0 = _t0(run, z, pieces)
    track = soundtrack(run, t0, steps / FPS, cfg, bool(summary.get("replay")))
    wav = run / "live_audio.wav"
    from scipy.io import wavfile

    wavfile.write(wav, RATE, (track * 32767).astype(np.int16))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(silent), "-i", str(wav), "-c:v", "copy",
                    "-c:a", "aac", "-shortest", str(out)], check=True)
    print(f"[live-video] -> {out}\n[live-video] watch: ffplay -autoexit {out}")
    return out
