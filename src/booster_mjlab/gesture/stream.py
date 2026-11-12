"""Streaming gesture motion: one session timeline of 50 Hz K1 reference frames (gesture_plan.md step 7).

``generate.py`` makes a whole reply at once, after it was spoken. Here motion is made **while the
conversation runs**: the timeline always holds a few seconds of idle ahead of "now", and each spoken
piece replaces the timeline from just before its audio plays. The tracker reads one frame per
control step (``live.py``).

What a frame is: joint positions, joint velocities, trunk orientation: all the policy observes of
the reference (``deploy.RefFrame``). No forward kinematics of the whole body, no Gate 1, no files.

How a plan (a few units in a row) is put on the timeline, ``MotionStream.place``:

1. **Stitch** at 50 fps straight from the units' source clips. A new unit is turned and moved so its
   trunk continues from the timeline's pose at its first frame, and crossfaded with what was there
   (the crossfade is centered on the seam when there is time, otherwise it starts at the earliest
   frame that may still change).
2. **Foot lock** on one stance for the whole session, fixed at start from the persona's typical
   stance (``generate.foot_lock`` uses one stance per reply). The stance frame (between the feet) is
   smoothed with a *trailing* 0.8 s average, which needs no future frames: replacing the timeline
   from frame f never changes what was sent before f.
3. Feet go to a fixed height with level soles, so ``ground_clip`` isn't needed.

Speech features are normalized with running statistics of the session's voice (``RunningFeatures``):
a 2 s piece is too short to z-score on its own.
"""

from __future__ import annotations

import threading
import time
from dataclasses import dataclass

import mujoco
import numpy as np

from booster_mjlab.gesture import audio as A
from booster_mjlab.gesture.analysis import strong_accents
from booster_mjlab.gesture.generate import (
    FPS,
    LEAD_S,
    GenCfg,
    Reply,
    Units,
    _heading,
    _load_pkl,
    _quat_mul,
    _sample,
    _slerp,
    _solve_leg_soft,
    _tool,
    _wrap,
    _yaw,
    _yaw_quat,
    candidates,
    search,
    segment,
)

LEAD = round(LEAD_S * FPS)  # frames the motion runs ahead of its audio


@dataclass
class StreamCfg:
    margin_s: float = 0.1
    """A new plan may only change frames this far past "now": the time until its first frames are
    published (features + search + stitch + the first chunk of foot lock: 30-50 ms), plus a little."""
    publish_chunk_s: float = 0.5
    idle_chunk_s: float = 2.0
    """Idle is planned in chunks of this length (~50 ms each: a piece that arrives meanwhile waits)."""
    stance_smooth_s: float = 0.8
    min_piece_s: float = 0.4
    """A piece with less than this left to gesture (it arrived late) gets no motion of its own."""
    blind_activity: float = 0.3
    """Pre-start (text known, audio not): pick units about this lively (sd above the take's mean)."""
    max_residual_m: float = 0.005
    stance_samples: int = 300


class RunningFeatures:
    """``analysis.recording_features`` for pieces of one voice arriving one at a time: loudness and
    onset strength are z-scored with the mean and spread of all speech heard so far this session."""

    def __init__(self) -> None:
        self.n = 0
        self.s = np.zeros(2)
        self.ss = np.zeros(2)

    def __call__(self, x: np.ndarray, rate: int = 16000) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        hop = rate / FPS
        n = max(1, int(len(x) / hop))
        # Silence around the piece, as in a whole reply: the speech mask measures loudness against
        # the quietest 5% of the recording, and a piece that is all voice has no quiet part.
        k = round(0.3 * FPS)
        pad = np.zeros(round(k * hop))
        raw = A.speech_features(np.concatenate([pad, x, pad]), rate, FPS)[k:k + n]
        loud, onset, voiced, pitch, speech = (raw[:, j].astype(np.float64) for j in range(5))
        onset = np.log1p(onset)
        sp = speech > 0 if np.any(speech > 0) else np.ones(n, bool)
        v = np.stack([loud[sp], onset[sp]], 1)
        self.n += len(v)
        self.s += v.sum(0)
        self.ss += (v ** 2).sum(0)
        mean = self.s / self.n
        sd = np.sqrt(np.maximum(self.ss / self.n - mean ** 2, 0.0)) + 1e-9
        feats = np.zeros((n, 5))
        feats[:, 0] = (loud - mean[0]) / sd[0]
        feats[:, 1] = (onset - mean[1]) / sd[1]
        feats[:, 2] = voiced
        feats[:, 4] = speech
        p = np.where(pitch != 0, pitch, np.nan)
        ok = ~np.isnan(p)
        if ok.sum() >= 2:
            p = np.interp(np.arange(n), np.flatnonzero(ok), p[ok])
        feats[:, 3] = np.where(speech > 0, np.nan_to_num(p), 0.0)
        return feats, (pitch != 0) & (voiced > 0), pitch


class MotionStream:
    """The session timeline. One planner thread calls ``extend_idle`` / ``speak`` / ``pre_start``;
    any thread may call ``frame`` (the control loop). Frame k is the reference at k / 50 s after the
    session clock started."""

    def __init__(self, units: Units, joint_names: list[str], gen: GenCfg, cfg: StreamCfg | None = None, seed: int = 0):
        self.units, self.gen, self.cfg = units, gen, cfg or StreamCfg()
        self.rng = np.random.default_rng(seed)
        gc = _tool("ground_clip")
        self.g = gc.Grounder(gc.DEFAULT_GMR_XML, gc.DEFAULT_ROBOT_XML)
        gmr = [gc.RENAME.get(n, n) for n in self.g.gmr_joints]
        self.to_policy = np.array([gmr.index(n) for n in joint_names])  # policy joint -> dof_pos column
        self.features = RunningFeatures()
        self.cache: dict = {}
        self.used: dict[int, int] = {}  # unit -> frame it last started at
        self.lock = threading.Lock()
        self.n = 0  # frames planned (planner thread)
        self.n_pub = 0  # frames the control loop may read
        self.starved = 0
        self.last_piece = None
        self.q_good: dict[str, np.ndarray] = {}
        self.lock_fails = 0
        self._a: dict[str, np.ndarray] = {}
        for name, width in (("raw_pos", 3), ("raw_rot", 4), ("raw_dof", 22), ("smid", 2), ("out_dof", 22), ("out_rot", 4), ("out_pos", 3),
                            ("jp", 22), ("jv", 22), ("aq", 4)):
            self._a[name] = np.zeros((4096, width))
        self._a["syaw"] = np.zeros(4096)
        self._a["leg"] = np.zeros((4096, 2))  # hip-to-foot distance of the stitched pose, per side
        m = self.g.rob
        m_data = self.g.data
        self.g.set_pose(np.zeros(3), np.array([0.0, 0.0, 0.0, 1.0]), np.zeros(22))
        self.hip_local = {}  # hip joint position in the trunk frame (fixed: the hip is on the trunk)
        for side in self.g.feet:
            j = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_JOINT, f"{side.title()}_Hip_Pitch")
            self.hip_local[side] = m_data.xanchor[j].copy()
        self._a["unit"] = np.full(4096, -1)
        self._a["kind"] = np.zeros(4096, np.int8)  # 0 idle, 1 speaking, 2 pre-start
        self._calibrate_stance()

    # ------------------------------------------------------------------------------------ set-up

    def _allowed(self) -> np.ndarray:
        u = self.units
        ok = u.side_shift <= self.gen.max_side_shift
        if self.gen.speaker:
            ok &= u.speaker == self.gen.speaker
        return ok

    def _feet(self) -> dict:
        d = self.g.data
        return {s: (d.xpos[f["body"]].copy(), d.xmat[f["body"]].reshape(3, 3).copy()) for s, f in self.g.feet.items()}

    @staticmethod
    def _stance(feet: dict) -> tuple[np.ndarray, float]:
        """The stance frame of one pose: the point between the feet, x forward (perpendicular to the
        line from the right foot to the left)."""
        l, r = feet["left"][0][:2], feet["right"][0][:2]
        across = l - r
        return (l + r) / 2, float(np.arctan2(across[1], across[0]) - np.pi / 2)

    @staticmethod
    def _rot(q: np.ndarray) -> np.ndarray:
        """Rotation matrix of an x y z w quaternion."""
        x, y, z, w = q
        return np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)],
                         [2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)],
                         [2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)]])

    def _calibrate_stance(self) -> None:
        """The session's stance: each foot's median position and heading in the stance frame, and its
        height, over a sample of the persona's units (their source clips are grounded, feet flat)."""
        u = self.units
        pool = np.flatnonzero(self._allowed())
        pick = self.rng.choice(pool, size=min(self.cfg.stance_samples, len(pool)), replace=False)
        xy = {s: [] for s in self.g.feet}
        yaw = {s: [] for s in self.g.feet}
        z = {s: [] for s in self.g.feet}
        for i in pick:
            clip = _load_pkl(str(u.source[u.clip[i]]), self.cache)
            pos, rot, dof = _sample(clip, np.array([u.a[i] / FPS]))
            self.g.set_pose(pos[0], rot[0], dof[0])
            feet = self._feet()
            mid, sy = self._stance(feet)
            c, s_ = np.cos(-sy), np.sin(-sy)
            for s, (p, R) in feet.items():
                d = p[:2] - mid
                xy[s].append([c * d[0] - s_ * d[1], s_ * d[0] + c * d[1]])
                yaw[s].append(_wrap(_heading(R) - sy))
                z[s].append(p[2])
        self.canon = {s: np.median(xy[s], axis=0) for s in xy}
        self.canon_yaw = {s: float(np.angle(np.mean(np.exp(1j * np.array(yaw[s]))))) for s in yaw}
        self.foot_z = {s: float(np.median(z[s])) for s in z}

    def _grow(self, n: int) -> None:
        cap = len(self._a["syaw"])
        if n <= cap:
            return
        new = max(n, 2 * cap)
        with self.lock:  # the control loop reads jp / jv / aq
            for k, v in self._a.items():
                w = np.zeros((new, *v.shape[1:]), v.dtype)
                w[:cap] = v
                self._a[k] = w

    # ------------------------------------------------------------------------------------ stitching

    @staticmethod
    def _frames(piece: tuple, f: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """A placed unit's pose at timeline frames f (also before its start and past its end: the
        source clip's neighbouring frames, held at the clip's ends)."""
        clip, f0, ua, stretch, dyaw, Rz, offset = piece
        pos, rot, dof = _sample(clip, ua + (np.asarray(f) - f0) / FPS / stretch)
        pos = np.column_stack([pos[:, :2] @ Rz.T + offset, pos[:, 2]])
        rot = _quat_mul(np.repeat(_yaw_quat(dyaw)[None], len(pos), 0), rot)
        return pos, rot, dof

    def _extend(self, upto: int) -> None:
        """Continue the last unit past its end (for crossfades and gaps)."""
        if upto <= self.n:
            return
        self._grow(upto)
        f = np.arange(self.n, upto)
        a = self._a
        a["raw_pos"][f], a["raw_rot"][f], a["raw_dof"][f] = self._frames(self.last_piece, f)
        a["unit"][f], a["kind"][f] = a["unit"][self.n - 1], a["kind"][self.n - 1]
        self.n = upto

    def place(self, segs: list[tuple[int, int]], chosen: list[int], earliest: int, kind: int) -> dict:
        """Put units on the timeline: ``segs`` are frame ranges in a row, and everything from the
        first one on is replaced. Frames before ``earliest`` stay as they are. Returns what changed."""
        t0 = time.perf_counter()
        u, a, gen = self.units, self._a, self.gen
        dirty = None
        for (fa, fb), i in zip(segs, chosen):
            clip = _load_pkl(str(u.source[u.clip[i]]), self.cache)
            ua = u.a[i] / FPS
            stretch = (fb - fa) / u.length[i]
            p0, r0, d0 = _sample(clip, np.array([ua]))
            self._grow(fb)
            if self.n == 0:  # the very first unit: at the origin, facing +x
                dyaw = -_yaw(r0[0])
                c, s = np.cos(dyaw), np.sin(dyaw)
                Rz = np.array([[c, -s], [s, c]])
                piece = (clip, fa, ua, stretch, dyaw, Rz, -Rz @ p0[0, :2])
                f = np.arange(fa, fb)
                a["raw_pos"][f], a["raw_rot"][f], a["raw_dof"][f] = self._frames(piece, f)
                w0 = fa
                dirty = fa if dirty is None else dirty
            else:
                before = self.n
                self._extend(fa + 1)
                dyaw = _yaw(a["raw_rot"][fa]) - _yaw(r0[0])
                c, s = np.cos(dyaw), np.sin(dyaw)
                Rz = np.array([[c, -s], [s, c]])
                piece = (clip, fa, ua, stretch, dyaw, Rz, a["raw_pos"][fa, :2] - Rz @ p0[0, :2])
                # Crossfade long enough that no joint moves faster than max_seam_speed because of it.
                d = np.abs(a["raw_dof"][fa] - d0[0]).max()
                T = float(np.clip(1.5 * d / gen.max_seam_speed, gen.crossfade_s, min(gen.max_crossfade_s, (fb - fa) / FPS)))
                h = max(1, round(T / 2 * FPS))
                w0 = min(max(fa - h, earliest, 1), fa)
                w1 = min(w0 + 2 * h, fb)
                self._extend(w1)
                f = np.arange(w0, fb)
                pos, rot, dof = self._frames(piece, f)
                m = f < w1
                w = (f[m] - w0 + 1) / (w1 - w0 + 1)
                w = (w * w * (3 - 2 * w))[:, None]
                pos[m] = (1 - w) * a["raw_pos"][f[m]] + w * pos[m]
                dof[m] = (1 - w) * a["raw_dof"][f[m]] + w * dof[m]
                rot[m] = _slerp(a["raw_rot"][f[m]], rot[m], w[:, 0])
                a["raw_pos"][f], a["raw_rot"][f], a["raw_dof"][f] = pos, rot, dof
                dirty = min(w0, before) if dirty is None else min(dirty, w0)
            a["unit"][fa:fb], a["kind"][fa:fb] = i, kind
            self.n, self.last_piece = fb, piece
            self.used[int(i)] = fa
        t_stitch = time.perf_counter() - t0
        # Foot lock is the slow part (~0.7 ms per frame), so the control loop gets the plan half a
        # second of motion at a time: the first frames are out ~20 ms after stitching, and the rest
        # is locked ~30x faster than it plays.
        first_publish = None
        step = round(self.cfg.publish_chunk_s * FPS)
        for lo in range(dirty, self.n, step):
            hi = min(lo + step, self.n)
            self._foot_lock(lo, hi)
            self._publish(lo, hi)
            first_publish = first_publish or time.monotonic()
        return {"first_frame": int(dirty), "start_frame": int(segs[0][0]), "end_frame": int(self.n),
                "units": [int(i) for i in chosen], "stitch_s": t_stitch, "first_publish": first_publish,
                "foot_lock_s": time.perf_counter() - t0 - t_stitch}

    # ------------------------------------------------------------------------------------ foot lock

    def _foot_lock(self, lo: int, n: int) -> None:
        """Frames lo..n-1 of the stitched motion onto the session's stance (see the module docstring)."""
        a, g = self._a, self.g
        sides = list(g.feet)
        for f in range(lo, n):
            g.set_pose(a["raw_pos"][f], a["raw_rot"][f], a["raw_dof"][f])
            feet = self._feet()
            mid, yaw = self._stance(feet)
            a["smid"][f] = mid
            R = self._rot(a["raw_rot"][f])
            a["leg"][f] = [np.linalg.norm(feet[s][0] - (a["raw_pos"][f] + R @ self.hip_local[s])) for s in sides]
            a["syaw"][f] = yaw if f == 0 else a["syaw"][f - 1] + _wrap(yaw - a["syaw"][f - 1])
        w = max(1, round(self.cfg.stance_smooth_s * FPS))
        for f in range(lo, n):
            k = max(0, f - w + 1)
            yaw = a["syaw"][k:f + 1].mean()
            mid = a["smid"][k:f + 1].mean(axis=0)
            c, s = np.cos(-yaw), np.sin(-yaw)
            d = a["raw_pos"][f, :2] - mid
            pos = np.array([c * d[0] - s * d[1], s * d[0] + c * d[1], a["raw_pos"][f, 2]])
            rot = _quat_mul(_yaw_quat(-yaw), a["raw_rot"][f])[0]
            # Trunk height: keep each leg no longer than it was in the unit's own stance. A unit that
            # stood narrower with straight knees can't reach the session's stance from its own height
            # (knee at 0.03 rad, feet missing by 1.3 cm, legs held and then jumping at 11 rad/s).
            R = self._rot(rot)
            drop = -np.inf
            for j, side in enumerate(sides):
                hip = pos + R @ self.hip_local[side]
                r2 = ((hip[:2] - self.canon[side]) ** 2).sum()
                reach = np.sqrt(max(a["leg"][f, j] ** 2 - r2, 1e-6))
                drop = max(drop, (hip[2] - self.foot_z[side]) - reach)
            pos[2] -= float(np.clip(drop, -0.05, 0.05))
            g.set_pose(pos, rot, a["raw_dof"][f])
            out = a["raw_dof"][f].copy()
            for side in sides:
                foot = g.feet[side]
                cols = foot["leg_cols"]
                target = np.array([*self.canon[side], self.foot_z[side]])
                seeds = [a["out_dof"][f - 1, cols] if f else a["raw_dof"][f, cols], a["raw_dof"][f, cols]]
                if side in self.q_good:
                    seeds.append(self.q_good[side])
                q, res = None, np.inf
                for seed in seeds:  # the previous frame's legs first; fresh starts only if that fails
                    q2, r2 = _solve_leg_soft(g, foot, target, self.canon_yaw[side], seed)
                    if r2 < res:
                        q, res = q2, r2
                    if res <= self.cfg.max_residual_m:
                        break
                if res > self.cfg.max_residual_m:  # unreachable: hold the last good legs rather than jump
                    self.lock_fails += 1
                    q = self.q_good.get(side, seeds[0])
                else:
                    self.q_good[side] = q
                g.data.qpos[foot["leg_adr"]] = q
                out[cols] = q
            a["out_dof"][f] = out
            a["out_rot"][f], a["out_pos"][f] = rot, pos

    def _publish(self, lo: int, n: int) -> None:
        """Frames lo..n-1 to the control loop (and the velocity of frame lo - 1, which until now had no
        next frame to difference against)."""
        a = self._a
        k = max(lo - 1, 0)
        jp = a["out_dof"][k:n][:, self.to_policy]
        ctx = a["out_dof"][max(k - 1, 0):n][:, self.to_policy]
        jv = np.gradient(ctx, 1 / FPS, axis=0)[-len(jp):] if len(ctx) > 1 else np.zeros_like(jp)
        with self.lock:  # the control loop sees a plan all at once
            a["jp"][k:n], a["jv"][k:n] = jp, jv
            a["aq"][lo:n] = a["out_rot"][lo:n][:, [3, 0, 1, 2]]  # GMR x y z w -> w x y z
            self.n_pub = n

    # ------------------------------------------------------------------------------------ planning

    def _choose(self, cands: list[np.ndarray], costs: list[np.ndarray], segs: list[tuple[int, int]]) -> list[int]:
        """``generate.search`` with the timeline's history: the unit playing at the first frame is
        fixed (transition cost into the first segment), and units used in the last ``reuse_gap_s``
        are out."""
        u, gen = self.units, self.gen
        costs = [c.copy() for c in costs]
        if self.n:
            prev = int(self._a["unit"][min(segs[0][0], self.n) - 1])
            costs[0] += gen.w_transition * u.transition(np.array([prev]), cands[0]) / u.trans_scale
        gap = gen.reuse_gap_s * FPS
        for s, (fa, _) in enumerate(segs):
            costs[s] += 1e6 * np.array([fa - self.used.get(int(i), -10 ** 9) < gap for i in cands[s]])
        return search(u, cands, costs, gen, [fa / FPS for fa, _ in segs])

    def extend_idle(self, earliest: int = 0) -> dict:
        """Add one chunk of idle (listening) motion at the end of the timeline."""
        t0 = time.perf_counter()
        k = max(1, round(self.cfg.idle_chunk_s / self.gen.idle_seg_s))
        cuts = np.linspace(self.n, self.n + round(self.cfg.idle_chunk_s * FPS), k + 1).round().astype(int)
        segs = list(zip(cuts[:-1].tolist(), cuts[1:].tolist()))
        cc = [candidates(self.units, None, (0, b - a), self.gen, self.rng, idle=True) for a, b in segs]
        chosen = self._choose([c[0] for c in cc], [c[1] for c in cc], segs)
        t_search = time.perf_counter() - t0
        return {**self.place(segs, chosen, earliest, 0), "search_s": t_search}

    def speak(self, audio: np.ndarray, words: list[tuple[str, float, float]], play_frame: int, now_frame: int) -> dict | None:
        """Motion for one spoken piece: 16 kHz ``audio`` whose first sample plays at timeline frame
        ``play_frame``. The motion belongs ``LEAD`` frames earlier; whatever of it lies before
        now + margin is skipped (``late_frames``). None if too little is left."""
        t0 = time.perf_counter()
        feats, voiced, pitch = self.features(audio)
        n = len(feats)
        f0 = play_frame - LEAD
        earliest = now_frame + round(self.cfg.margin_s * FPS)
        r = max(0, earliest - f0)
        if n - r < round(self.cfg.min_piece_s * FPS):
            return None
        acc = strong_accents(feats, FPS)
        sub = Reply(None, feats[r:], voiced[r:], pitch[r:], acc[acc >= r] - r,
                    [(w, s - r / FPS, e - r / FPS) for w, s, e in words if s >= r / FPS], (n - r) / FPS)
        rel = segment(sub, self.gen)
        t_feat = time.perf_counter() - t0
        cc = [candidates(self.units, sub, seg, self.gen, self.rng) for seg in rel]
        segs = [(f0 + r + a, f0 + r + b) for a, b in rel]
        chosen = self._choose([c[0] for c in cc], [c[1] for c in cc], segs)
        t_search = time.perf_counter() - t0 - t_feat
        return {**self.place(segs, chosen, earliest, 1), "features_s": t_feat, "search_s": t_search,
                "late_frames": int(r), "ideal_start_frame": int(f0), "accents": int(len(acc))}

    def pre_start(self, frames: int, now_frame: int) -> dict | None:
        """The reply's first words are known but not voiced yet: start gesturing right away (the
        voice follows in ~0.7 s, and hands lead the voice anyway), with fairly lively units chosen
        without audio. The real piece replaces the rest when it arrives."""
        t0 = time.perf_counter()
        u, gen = self.units, self.gen
        start = now_frame + round(self.cfg.margin_s * FPS)
        k = max(1, round(frames / (gen.seg_target_s * FPS)))
        cuts = np.linspace(start, start + frames, k + 1).round().astype(int)
        segs = list(zip(cuts[:-1].tolist(), cuts[1:].tolist()))
        cands, costs = [], []
        allowed = self._allowed()
        for a, b in segs:
            stretch = (b - a) / u.length
            idx = np.flatnonzero(allowed & (np.abs(np.log(stretch)) <= np.log1p(gen.max_stretch)))
            if len(idx) < gen.k:
                idx = np.flatnonzero(allowed)[np.argsort(np.abs(np.log(stretch[allowed])))[: gen.k * 4]]
            cost = (gen.w_activity * np.abs(u.activity[idx] - self.cfg.blind_activity)
                    + gen.w_length * np.abs(np.log(stretch[idx])) / np.log1p(gen.max_stretch)
                    + self.rng.uniform(0, 0.3, len(idx)))
            order = np.argsort(cost)[: gen.k]
            cands.append(idx[order])
            costs.append(cost[order])
        chosen = self._choose(cands, costs, segs)
        t_search = time.perf_counter() - t0
        return {**self.place(segs, chosen, start, 2), "search_s": t_search}

    # ------------------------------------------------------------------------------------ reading

    def frame(self, k: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """(joint positions, joint velocities, trunk quaternion w x y z) at frame k, in the policy's
        joint order. Past the planned end the last frame is held (counted in ``starved``)."""
        with self.lock:
            if k >= self.n_pub:
                self.starved += 1
                k = self.n_pub - 1
                return self._a["jp"][k].copy(), np.zeros(22), self._a["aq"][k].copy()
            return self._a["jp"][k].copy(), self._a["jv"][k].copy(), self._a["aq"][k].copy()

    def snapshot(self, upto: int) -> dict:
        with self.lock:
            n = min(upto, self.n_pub)
            return {"joint_pos": self._a["jp"][:n].copy(), "joint_vel": self._a["jv"][:n].copy(),
                    "anchor_quat": self._a["aq"][:n].copy(), "unit": self._a["unit"][:n].copy(),
                    "kind": self._a["kind"][:n].copy(), "fps": FPS}
