"""Gate 1 checks for grounded K1 clips (GMR -> ground_clip .pkl), on booster-mjlab's K1 model.

One row of numbers per clip, then flags. A *severe* flag means the reference itself is suspect
(`--exclude severe` in beat2_batch drops it); other flags are information. Checks:

- format: NaN/inf, wrong joint count, fps, root quaternion norm
- jumps: a joint (or the root) moving further in one frame than real motion does (GMR's IK flipping)
- joint speed: a joint faster than its motor's no-load speed for longer than `speed_run_s`
- floor: any collision geom below the floor
- foot sliding: a foot on the floor moving sideways
- self-collision: two K1 collision geoms overlapping (the tracking task simulates self-collision)
- joint limits, knees, trunk drop, K1 feet, arm behind the body (the GMR IK-start bug)
- leakage (per artifact, not per clip): held-out speakers or non-training takes in a training file

Calibrate the limits on clips that are known to be good or bad (usage below), then set them in
the dataset spec's [qc] table; anything not set there uses LIMITS here.

Usage (from ~/projects/booster-mjlab):
    # numbers + flags for every clip of an existing batch folder (reads <dir>/qc.json for the human side)
    uv run python tools/clip_qc.py ~/robotics/data/beat2_batch --report notes/gate1-calibration.md \\
        --leakage ~/robotics/data/beat2_batch/combined/beat2-10s-train.npz --spec tools/datasets/beat2_full.toml
"""
from __future__ import annotations

import argparse
import json
import multiprocessing
import os
import pickle
import re
import sys
from concurrent.futures import ProcessPoolExecutor
from datetime import date
from pathlib import Path

import mujoco
import numpy as np

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
from ground_clip import BODY, DEFAULT_GMR_XML, DEFAULT_ROBOT_XML, GEOM, JOINT, RENAME, Grounder  # noqa: E402

# No-load speed (rad/s) and torque knee point (full torque only below it) per joint, from
# src/booster_mjlab/robots/booster_k1/k1_constants.py (copied: importing it pulls in mjlab, ~5 s per worker).
VELOCITY_LIMITS = (  # (joint-name regex, no-load speed, knee point)
    (r".*_Knee_Pitch", 12.57, 2.09),
    (r".*_Hip_Yaw", 17.59, 7.85),
    (r".*_Ankle_.*", 17.59, 7.85),
    (r".*_Hip_Pitch", 14.66, 1.88),
    (r".*_Hip_Roll", 12.57, 2.62),
    (r".*_(Shoulder|Elbow)_.*", 33.51, 5.24),
    (r"Head_.*", 7.85, 7.85),
)

LIMITS = {
    # format
    "fps": 30.0,
    "quat_norm_err": 1e-3,
    # Joint jump: GMR's IK flipping branch. Among the 152 v1 clips the 4 glitches were 0.92-1.57 rad;
    # real fast motion stayed <= 0.52 rad (see notes/gate1-calibration.md).
    "joint_jump_rad": 0.6,
    "root_jump_cm": 3.0,          # trunk moving > 3 cm in 1/30 s (0.9 m/s) while standing: a teleport
    # Trunk turning > 6 deg in 1/30 s. Real motion stayed <= 4 deg/frame; GMR's flips turned the trunk
    # 7.6-33 deg in one frame while the human pelvis turned < 5 deg (calibration on v1 and torso clips).
    "root_turn_deg": 6.0,
    # Trunk lean: the K1 trunk's median tilt from vertical over the clip. Normal speakers ~5 deg
    # (99th pct 23); two Hailing conversation takes have the pelvis tilted ~33 deg for the whole take
    # (a mocap offset or leaning on something) and the K1 copies it at 25 deg; max 136 deg. Severe.
    "trunk_lean_deg": 15.0,
    # joint speed above the no-load limit for longer than this
    "speed_run_s": 0.1,
    # floor: lowest collision point below the floor
    "floor_mm": 5.0,
    # Foot sliding: a foot within `planted_mm` of the floor (ground_clip puts stance feet exactly on it)
    # moving sideways > slide_cm_frame for at least slide_run_s, or > slide_jump_cm in one frame.
    # 1-2 frame slides of 1-1.5 cm/frame are weight-shift pivots (Lawrence, Solomon) and trained fine.
    "planted_mm": 2.0,
    "slide_cm_frame": 1.0,
    "slide_run_s": 0.1,
    "slide_jump_cm": 3.0,
    # Self-collision: two geoms overlapping deeper than `self_depth_mm` for longer than `self_run_s`.
    # A hand pressing into the hip / thigh (the K1 is ~0.6x human, so a hand resting on the leg sinks
    # in up to 25 mm) is information only: talk_scott_1_1_t34-44 does it for 0.6 s and trained to 50/50.
    "self_depth_mm": 5.0,
    "self_run_s": 0.1,
    # Severe only deeper than this: on the full BEAT2 build, hands resting on the belly overlapped the
    # trunk by ~12 mm (median) for ~0.6 s, the same kind of contact as the hand-on-leg case above.
    # Feet crossing into each other (median 47 mm for 3.8 s) stay severe.
    "self_severe_mm": 25.0,
    "self_info_pairs": r"(left|right)_hand.* / \1_(hip|shank).*",
    # Feet overlapping at all (> self_depth_mm for > self_run_s) is severe: crossed legs (mostly Katya's
    # conversation takes). 21 training clips, 48% quarantined by the 10-19 full-BEAT2 runs' sampler.
    "feet_pair": r"left_foot.* / right_foot.*",
    # A foot held off the floor in a standing clip (median height over the clip, from ground_clip's log):
    # a broken leg retarget (wayne_0_33_33_t7-20: 27 cm up, 89 deg tilt, human standing normally) or a
    # human foot resting on its toes, which the toeless K1 turns into standing on one leg (Katya).
    # >= 30 mm: 71 training clips, 17-100% quarantined (1.9% below 10 mm). notes/log.md 2026-10-20.
    "foot_gap_mm": 30.0,
    # older checks (beat2_batch QC); clips that trained to 50/50: K1 feet <= 1.8 cm, trunk <= 1.8 cm,
    # knees 14-36 deg, 0 joint-limit frames
    "feet_k1_cm": 8.0,            # K1 is ~0.6x human: the 10 cm human filter allows ~6 cm
    "feet_k1_cm_b": 18.0,         # Tier B (foot shifts, human <= 25 cm): ~15 cm on the K1
    "trunk_drop_cm": 5.0,
    "knee_max_deg": 60.0,
    "limit_frac": 0.05,           # a joint group within 1 deg of a limit on more than this share of frames
    "twist_severe_frac": 0.5,     # upper-arm twist at its limit on more than this share: severe
    "arm_behind_m": 0.05,         # K1 hand this far behind the trunk while the human's wrist is
    "human_front_m": 0.05,        # ... this far in front of the pelvis: arm pose lost (info)
    # Severe beyond this: GMR's IK-start bug held the hand 11-17 cm behind. On the full build 77% of
    # flags sat within 2 cm of the 5 cm limit (mostly Sophie's low clasped hands, which the K1 lets hang).
    "arm_behind_severe_m": 0.10,
    "robust_z": 3.5,              # batch-relative outlier (median / MAD) on arms, trunk, knees
}
LIMIT_MARGIN = np.radians(1.0)
# Joint-limit hits, grouped by what they mean. The elbow bend (Elbow_Yaw) at 0 is a straight arm, a
# normal pose, so that side is not counted.
LIMIT_KINDS = (
    ("Elbow_Pitch", "upper-arm twist"),  # straight arm: twist doesn't move the hand, so GMR's IK drifts to the limit
    ("Head", "head"),                    # the speaker looks further than the K1's head can: nods get clipped
    ("Shoulder", "shoulder"),            # arm pose clipped
    ("Elbow_Yaw", "elbow bend"),         # fully bent
    ("", "leg"),                         # hips, knees, ankles
)
# Feet are left out of the outlier test: K1 foot motion is ~1 cm for most clips with a long tail of
# normal weight shifts; the fixed feet_k1_cm limit covers them.
MAD_FLOOR = {"arms_k1_cm_s": 2.0, "trunk_drop_cm": 0.5, "knee_max_deg": 3.0}


def R_from_xyzw(q: np.ndarray) -> np.ndarray:
    """(T, 4) scipy-order (x, y, z, w) quaternions -> (T, 3, 3) rotation matrices."""
    from scipy.spatial.transform import Rotation
    return Rotation.from_quat(q).as_matrix()


def longest_run(mask: np.ndarray) -> tuple[int, int]:
    """Length and start index of the longest run of True."""
    if not mask.any():
        return 0, -1
    edges = np.flatnonzero(np.diff(np.r_[0, mask.astype(int), 0]))
    lens = edges[1::2] - edges[::2]
    i = int(lens.argmax())
    return int(lens[i]), int(edges[2 * i])


class K1Checker:
    """Gate 1 numbers for a grounded clip, on booster-mjlab's K1 model (the one training uses)."""

    def __init__(self, grounder: Grounder | None = None, limits: dict | None = None):
        self.L = {**LIMITS, **(limits or {})}
        self.g = g = grounder or Grounder(DEFAULT_GMR_XML, DEFAULT_ROBOT_XML)
        rob = g.rob
        self.joint_names = [RENAME.get(n, n) for n in g.gmr_joints]  # .pkl column order
        self.limits = np.array([rob.jnt_range[mujoco.mj_name2id(rob, JOINT, n)] for n in self.joint_names])
        self.knees = [self.joint_names.index(f"{s}_Knee_Pitch") for s in ("Left", "Right")]
        self.elbow_bend = np.array(["Elbow_Yaw" in n for n in self.joint_names])
        self.vmax, self.vknee = (np.array([next(v[i] for rx, *v in VELOCITY_LIMITS if re.fullmatch(rx, n))
                                           for n in self.joint_names]) for i in (0, 1))
        self.body = {b: mujoco.mj_name2id(rob, BODY, b)
                     for b in ("Trunk", "left_hand_link", "right_hand_link", "left_foot_link", "right_foot_link")}
        self.foot_geoms = [g.feet[s]["geom"] for s in ("left", "right")]
        self.geom_name = {i: mujoco.mj_id2name(rob, GEOM, i) for i in g.geoms}

    def check(self, path: Path) -> dict:
        with open(path, "rb") as f:
            m = pickle.load(f)
        g, data, b = self.g, self.g.data, self.body
        fps = float(m["fps"])
        root_pos, root_rot, dof = (np.asarray(m[k], dtype=float) for k in ("root_pos", "root_rot", "dof_pos"))
        T = len(dof)
        out = {
            "frames": T, "fps": fps, "n_dof": int(dof.shape[1]), "n_dof_expected": len(self.joint_names),
            "finite": bool(np.isfinite(root_pos).all() and np.isfinite(root_rot).all() and np.isfinite(dof).all()),
            "quat_norm_err": float(np.abs(np.linalg.norm(root_rot, axis=1) - 1).max()),
        }
        if not out["finite"] or out["n_dof"] != out["n_dof_expected"]:
            return out  # nothing else is meaningful

        feet, hands, foot_h, lowest = [], [], [], []
        self_depth = {}  # (geom a, geom b) -> per-frame overlap depth, m
        for t, frame in enumerate(zip(root_pos, root_rot, dof)):
            g.set_pose(*frame)
            R, o = data.xmat[b["Trunk"]].reshape(3, 3), data.xpos[b["Trunk"]]
            hands.append([R.T @ (data.xpos[b[h]] - o) for h in ("left_hand_link", "right_hand_link")])
            feet.append([data.xpos[b[f]][:2].copy() for f in ("left_foot_link", "right_foot_link")])
            foot_h.append([g.geom_lowest_z(i) for i in self.foot_geoms])
            lowest.append(min(g.geom_lowest_z(i) for i in g.geoms))
            mujoco.mj_collision(g.rob, data)  # robot geoms only (no floor in this model); parent-child pairs are skipped
            for c in data.contact[:data.ncon]:
                key = tuple(sorted((self.geom_name[c.geom1], self.geom_name[c.geom2])))
                depth = self_depth.setdefault(key, np.zeros(T))
                depth[t] = max(depth[t], -c.dist)
        feet, hands, foot_h, lowest = np.array(feet), np.array(hands), np.array(foot_h), np.array(lowest)

        # joint limits (as before)
        lo, hi = self.limits[:, 0], self.limits[:, 1]
        straight_lo, straight_hi = self.elbow_bend & (lo == 0), self.elbow_bend & (hi == 0)
        near = ((dof <= lo + LIMIT_MARGIN) & ~straight_lo) | ((dof >= hi - LIMIT_MARGIN) & ~straight_hi)
        kinds = {}
        for j in np.flatnonzero(near.any(axis=0)):
            kind = next(k for key, k in LIMIT_KINDS if key in self.joint_names[j])
            kinds.setdefault(kind, np.zeros(T, bool))
            kinds[kind] |= near[:, j]
        knee = np.degrees(dof[:, self.knees])

        # jumps and speed
        step = np.abs(np.diff(dof, axis=0))
        jf, jj = np.unravel_index(step.argmax(), step.shape)
        root_step = np.linalg.norm(np.diff(root_pos, axis=0), axis=1)
        trunk_up = R_from_xyzw(root_rot) @ np.array([0.0, 0.0, 1.0])
        lean = np.degrees(np.arccos(np.clip(trunk_up[:, 2], -1.0, 1.0)))
        q = root_rot / np.linalg.norm(root_rot, axis=1, keepdims=True)
        turn = np.degrees(2 * np.arccos(np.clip(np.abs(np.sum(q[1:] * q[:-1], axis=1)), 0, 1)))
        vel = step * fps
        over = vel > self.vmax
        runs = [longest_run(over[:, j]) for j in range(dof.shape[1])]
        sj = int(np.argmax([r[0] for r in runs]))
        ratio = vel / self.vmax
        rf, rj = np.unravel_index(ratio.argmax(), ratio.shape)

        # foot sliding: both frames on the floor (relative to the clip's floor, which ground_clip put at 0)
        L = self.L
        planted = foot_h < L["planted_mm"] / 1000
        both = planted[1:] & planted[:-1]
        slide = np.linalg.norm(np.diff(feet, axis=0), axis=-1) * both  # (T-1, 2) m/frame
        sf, ss = np.unravel_index(slide.argmax(), slide.shape)
        slide_runs = [longest_run(slide[:, k] > L["slide_cm_frame"] / 100) for k in (0, 1)]
        sr = int(np.argmax([r[0] for r in slide_runs]))

        # self-collision: longest overlap per pair deeper than self_depth_mm; hand-on-leg pairs are info only
        pairs = {}
        for key, depth in self_depth.items():
            run, start = longest_run(depth > L["self_depth_mm"] / 1000)
            pairs[" / ".join(key)] = [run / fps, float(depth.max() * 1000), (start / fps if start >= 0 else None)]

        def worst(items):
            return max(items, key=lambda kv: (kv[1][0], kv[1][1]), default=(None, [0.0, 0.0, None]))

        info = re.compile(L["self_info_pairs"])
        hard = worst((k, v) for k, v in pairs.items() if not info.fullmatch(k))
        soft = worst((k, v) for k, v in pairs.items() if info.fullmatch(k))

        out.update({
            "feet_k1_cm": float(np.linalg.norm(feet - np.median(feet, axis=0), axis=-1).max() * 100),
            "arms_k1_cm_s": float(np.linalg.norm(np.diff(hands, axis=0), axis=-1).mean() * fps * 100),
            "hand_fwd_k1_m": [float(v) for v in hands[:, :, 0].mean(axis=0)],
            "trunk_drop_cm": float(np.ptp(root_pos[:, 2]) * 100),
            "knee_range_deg": [[float(a), float(c)] for a, c in zip(knee.min(axis=0), knee.max(axis=0))],
            "knee_max_deg": float(knee.max()),
            "limit_frac": float(near.any(axis=1).mean()),
            "limit_kinds": {k: float(v.mean()) for k, v in kinds.items()},
            "joint_jump_rad": float(step.max()),
            "joint_jump_at": [self.joint_names[jj], float((jf + 1) / fps)],
            "root_jump_cm": float(root_step.max() * 100),
            "root_turn_deg": float(turn.max()),
            "trunk_lean_deg": float(np.median(lean)),           # median tilt of the trunk from vertical
            "trunk_lean_p95_deg": float(np.percentile(lean, 95)),
            "speed_ratio_max": float(ratio.max()),          # fastest joint / its no-load speed
            "speed_ratio_at": [self.joint_names[rj], float((rf + 1) / fps)],
            "speed_over_s": runs[sj][0] / fps,               # longest stretch above the no-load speed
            "speed_over_at": [self.joint_names[sj], float((runs[sj][1] + 1) / fps)],
            "derated_frac": float((vel > self.vknee).any(axis=1).mean()),  # frames with some joint past its torque knee
            "floor_min_mm": float(lowest.min() * 1000),
            "planted_frac": [float(v) for v in planted.mean(axis=0)],
            "slide_cm_frame": float(slide.max() * 100),
            "slide_at": [("left", "right")[ss], float((sf + 1) / fps)],
            "slide_run_s": slide_runs[sr][0] / fps,                  # longest slide above slide_cm_frame
            "slide_run_at": [("left", "right")[sr], float((slide_runs[sr][1] + 1) / fps)],
            "slide_total_cm": float(slide.sum(axis=0).max() * 100),  # foot that skates furthest while planted
            "self_pairs": pairs,
            "self_run_s": float(hard[1][0]),                          # body parts overlapping (not hand on leg)
            "self_depth_mm": float(hard[1][1]),
            "self_worst": [hard[0], hard[1][2]],
            "hand_leg_run_s": float(soft[1][0]),
            "hand_leg_depth_mm": float(soft[1][1]),
            "hand_leg_worst": [soft[0], soft[1][2]],
        })
        return out


# ---------------------------------------------------------------------------------------- flags

def flag(rows: list[dict], limits: dict | None = None) -> None:
    """Set r['flags'] and r['severe'] on every row: fixed limits plus outliers relative to this batch."""
    L = {**LIMITS, **(limits or {})}
    stats = {}
    for k, floor in MAD_FLOOR.items():
        v = np.array([r[k] for r in rows if k in r])
        if len(v):
            stats[k] = (np.median(v), max(1.4826 * np.median(np.abs(v - np.median(v))), floor))
    for r in rows:
        f, severe = [], []

        def add(msg, is_severe=False):
            f.append(msg)
            if is_severe:
                severe.append(msg)

        if not r["finite"]:
            add("NaN/inf in the clip", True)
        if r["n_dof"] != r["n_dof_expected"]:
            add(f"{r['n_dof']} joints (expected {r['n_dof_expected']})", True)
        if abs(r["fps"] - L["fps"]) > 1e-6:
            add(f"fps {r['fps']:g} (expected {L['fps']:g})", True)
        if r["quat_norm_err"] > L["quat_norm_err"]:
            add(f"root quaternion norm off by {r['quat_norm_err']:.1e}", True)
        if severe:
            r["flags"], r["severe"] = f, severe
            continue

        if r.get("feet_human_cm", 0) > r.get("max_foot_move_cm", np.inf):
            add("human steps")
        if r["feet_k1_cm"] > L["feet_k1_cm" if r.get("tier", "A") == "A" else "feet_k1_cm_b"]:
            add(f"K1 feet move {r['feet_k1_cm']:.0f} cm")
        if r["trunk_drop_cm"] > L["trunk_drop_cm"]:
            add(f"trunk drop {r['trunk_drop_cm']:.0f} cm")
        if r["knee_max_deg"] > L["knee_max_deg"]:
            add(f"knee {r['knee_max_deg']:.0f} deg")
        for kind, frac in r["limit_kinds"].items():
            if frac > L["limit_frac"]:
                add(f"{kind} at limit {frac:.0%}", kind == "upper-arm twist" and frac > L["twist_severe_frac"])
        if r.get("ik_fail_frames"):
            add(f"ground IK failed {r['ik_fail_frames']} frames", True)
        for k, (med, sd) in stats.items():
            z = (r[k] - med) / sd
            if abs(z) > L["robust_z"]:
                # A trunk-drop outlier is severe only if it also breaks the fixed limit: with 16k clips and
                # foot shifts, 3.8-5 cm drops are outliers of the batch but normal weight shifts.
                add(f"outlier {k.rsplit('_', 1)[0].replace('_', ' ')} (z {z:+.1f})",
                    k == "trunk_drop_cm" and z > 0 and r["trunk_drop_cm"] > L["trunk_drop_cm"])
        if r["joint_jump_rad"] > L["joint_jump_rad"]:
            joint, t = r["joint_jump_at"]
            add(f"joint jump {r['joint_jump_rad']:.2f} rad ({joint} at {t:.1f} s)", True)
        if r["root_jump_cm"] > L["root_jump_cm"]:
            add(f"root jump {r['root_jump_cm']:.1f} cm/frame", True)
        if r["root_turn_deg"] > L["root_turn_deg"]:
            add(f"root turn {r['root_turn_deg']:.0f} deg/frame", True)
        if r.get("trunk_lean_deg", 0.0) > L["trunk_lean_deg"]:
            add(f"trunk leans {r['trunk_lean_deg']:.0f} deg (median)", True)
        if r["speed_over_s"] > L["speed_run_s"]:
            joint, t = r["speed_over_at"]
            add(f"{joint} over its speed limit for {r['speed_over_s']:.2f} s (at {t:.1f} s)", True)
        if r["floor_min_mm"] < -L["floor_mm"]:
            add(f"{-r['floor_min_mm']:.0f} mm below the floor", True)
        if r["slide_run_s"] >= L["slide_run_s"] - 1e-9:
            side, t = r["slide_run_at"]
            add(f"{side} foot slides > {L['slide_cm_frame']:g} cm/frame for {r['slide_run_s']:.2f} s (at {t:.1f} s)", True)
        elif r["slide_cm_frame"] > L["slide_jump_cm"]:
            side, t = r["slide_at"]
            add(f"{side} foot slides {r['slide_cm_frame']:.1f} cm in one frame (at {t:.1f} s)", True)
        if r["self_run_s"] > L["self_run_s"]:
            pair, t = r["self_worst"]
            add(f"self-collision {pair} {r['self_run_s']:.1f} s (at {t:.1f} s, {r['self_depth_mm']:.0f} mm)",
                r["self_depth_mm"] > L["self_severe_mm"])
        feet_pair = re.compile(L["feet_pair"])
        for pair, (run, depth, start) in (r.get("self_pairs") or {}).items():
            if feet_pair.fullmatch(pair) and run > L["self_run_s"]:
                add(f"feet overlap {depth:.0f} mm for {run:.1f} s (at {start:.1f} s)", True)
        if r.get("foot_gap_mm", 0.0) >= L["foot_gap_mm"]:
            add(f"foot held {r['foot_gap_mm']:.0f} mm off the floor (median)", True)
        if r["hand_leg_run_s"] > L["self_run_s"]:
            pair, t = r["hand_leg_worst"]
            add(f"hand presses into leg {r['hand_leg_depth_mm']:.0f} mm for {r['hand_leg_run_s']:.1f} s (at {t:.1f} s)")
        for side, k1, human in zip(("left", "right"), r["hand_fwd_k1_m"], r.get("hand_fwd_human_m") or (None, None)):
            if human is not None and k1 < -L["arm_behind_m"] and human > L["human_front_m"]:
                add(f"{side} arm behind body {-k1 * 100:.0f} cm (human's in front)", k1 < -L["arm_behind_severe_m"])
        r["flags"], r["severe"] = f, severe


# ---------------------------------------------------------------------------------------- leakage

def take_of(clip: str, split: dict[str, str]) -> str | None:
    """Clip name -> BEAT2 take id: scott_0_1_1_t34-44[_shift] -> 2_scott_0_1_1."""
    m = re.match(r"([a-z]+)_(\d+)_(\d+)_(\d+)_t\d+-\d+", clip)
    if not m:
        return None
    ids = {t.split("_")[1]: t.split("_")[0] for t in split}  # speaker name -> id
    name = m.group(1)
    return f"{ids[name]}_{name}_{m.group(2)}_{m.group(3)}_{m.group(4)}" if name in ids else None


def leakage(clips: list[str], split: dict[str, str], heldout: set[str], allowed_types: set[str]) -> list[str]:
    """Problems with a training file's clips: held-out speakers, takes of other split types, unknown takes."""
    problems = []
    for c in clips:
        take = take_of(c, split)
        if take is None or take not in split:
            problems.append(f"{c}: not a known BEAT2 take")
            continue
        spk = "_".join(take.split("_")[:2])
        if spk in heldout:
            problems.append(f"{c}: held-out speaker {spk}")
        if split[take] not in allowed_types:
            problems.append(f"{c}: {split[take]} take {take}")
    return problems


def combined_clip_names(npz: Path) -> list[str]:
    with np.load(npz, allow_pickle=False) as d:
        return [str(n) for n in d["clip_names"]]


# ---------------------------------------------------------------------------------------- calibration CLI

_CHECKER: K1Checker | None = None


def _init(limits: dict | None = None) -> None:
    global _CHECKER
    _CHECKER = K1Checker(limits=limits)


def _check(path: Path) -> dict:
    return _CHECKER.check(path)


def check_all(paths: list[Path], workers: int, limits: dict | None = None) -> list[dict]:
    """K1Checker.check on every clip, `workers` processes at once (same output as 1)."""
    if workers <= 1 or len(paths) <= 1:
        _init(limits)
        return [_check(p) for p in paths]
    ctx = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(min(workers, len(paths)), mp_context=ctx, initializer=_init, initargs=(limits,)) as pool:
        return list(pool.map(_check, paths, chunksize=4))


def calibration_report(rows: list[dict], leaks: dict[str, list[str]], path: Path, src: str) -> None:
    """Distribution of every Gate 1 number over the batch, and what each limit flags."""
    checks = [  # (metric, limit key, direction, plan's limit, what it means)
        ("joint_jump_rad", "joint_jump_rad", 1, 0.3, "largest one-frame joint step, rad"),
        ("root_jump_cm", "root_jump_cm", 1, None, "largest one-frame trunk move, cm"),
        ("root_turn_deg", "root_turn_deg", 1, None, "largest one-frame trunk turn, deg"),
        ("speed_ratio_max", None, 1, None, "fastest joint / its no-load speed (1 = at the limit, one frame)"),
        ("speed_over_s", "speed_run_s", 1, 0.1, "longest time a joint is over its no-load speed, s"),
        ("derated_frac", None, 1, None, "share of frames with a joint past its torque knee point (less torque)"),
        ("floor_min_mm", "floor_mm", -1, 5.0, "lowest collision point vs the floor, mm"),
        ("slide_cm_frame", "slide_jump_cm", 1, 1.0, "fastest planted-foot slide, cm/frame"),
        ("slide_run_s", "slide_run_s", 1, None, "longest planted-foot slide above 1 cm/frame, s"),
        ("slide_total_cm", None, 1, None, "total planted-foot slide over the clip, cm"),
        ("self_run_s", "self_run_s", 1, 0.1, "longest self-overlap deeper than 5 mm (not hand on leg), s"),
        ("self_depth_mm", None, 1, None, "deepest self-overlap (not hand on leg), mm"),
        ("hand_leg_run_s", "self_run_s", 1, 0.1, "longest hand-into-leg overlap deeper than 5 mm, s (info)"),
        ("quat_norm_err", "quat_norm_err", 1, 1e-3, "root quaternion |norm - 1|"),
    ]
    ok = [r for r in rows if r.get("finite") and r["n_dof"] == r["n_dof_expected"]]
    lines = [
        "# Gate 1 calibration",
        "",
        f"Generated {date.today()} by `tools/clip_qc.py` on `{src}` ({len(rows)} grounded clips). "
        "Each check's distribution over the batch, how many clips the plan's limit and the limit in "
        "`clip_qc.LIMITS` flag, and the flagged clips.",
        "",
        f"- **Format:** {len(rows) - len(ok)} clips with NaN/inf or the wrong joint count; "
        f"fps {sorted({r['fps'] for r in rows})}; max quaternion norm error {max(r['quat_norm_err'] for r in rows):.1e}",
        "",
        "| check | median | p95 | max | plan limit → clips | `LIMITS` → clips |",
        "|---|---|---|---|---|---|",
    ]
    for metric, key, sign, plan, what in checks:
        v = np.array([r[metric] for r in ok])
        if sign < 0:
            pct = (np.median(v), np.percentile(v, 5), v.min())
            n_plan = int((v < -plan).sum()) if plan is not None else None
            n_lim = int((v < -LIMITS[key]).sum()) if key else None
            lim = -LIMITS[key] if key else None
        else:
            pct = (np.median(v), np.percentile(v, 95), v.max())
            n_plan = int((v > plan).sum()) if plan is not None else None
            n_lim = int((v > LIMITS[key]).sum()) if key else None
            lim = LIMITS[key] if key else None
        fmt = (lambda x: f"{x:.1e}") if metric == "quat_norm_err" else (lambda x: f"{x:.3g}")
        lines.append(f"| {what} | {fmt(pct[0])} | {fmt(pct[1])}{' (p5)' if sign < 0 else ''} | {fmt(pct[2])} | "
                     f"{'—' if n_plan is None else f'{plan:g} → {n_plan}'} | {'—' if n_lim is None else f'{lim:g} → {n_lim}'} |")

    lines += ["", "## Flagged clips (`LIMITS`)", "",
              "Severe flags in **bold**. Older checks (joint limits, knees, feet, outliers) included for context.", "",
              "| clip | flags |", "|---|---|"]
    for r in sorted(rows, key=lambda r: (-len(r["severe"]), r["name"])):
        if r["flags"]:
            lines.append(f"| `{r['name']}` | " + "; ".join(f"**{x}**" if x in r["severe"] else x for x in r["flags"]) + " |")
    pairs = {}
    for r in ok:
        for pair, (run, depth, _) in r["self_pairs"].items():
            p = pairs.setdefault(pair, [0, 0.0, 0.0])
            p[0] += 1
            p[1], p[2] = max(p[1], run), max(p[2], depth)
    if pairs:
        lines += ["", "## Self-contacts by pair", "", "| pair | clips touching | longest > 5 mm, s | deepest, mm |", "|---|---|---|---|"]
        lines += [f"| {k} | {v[0]} | {v[1]:.2f} | {v[2]:.0f} |" for k, v in sorted(pairs.items(), key=lambda kv: -kv[1][0])]
    for npz, problems in leaks.items():
        lines += ["", f"## Leakage: `{npz}`", "", f"{len(problems)} problem(s)" + (":" if problems else ".")]
        kinds = {}
        for p in problems:
            kinds.setdefault(p.split(": ", 1)[1].split(" ")[0], []).append(p)
        for k, ps in kinds.items():
            lines.append(f"- {len(ps)} × {k}: " + "; ".join(ps[:6]) + (" …" if len(ps) > 6 else ""))
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("batch_dir", type=Path, help="a beat2_batch out-dir (k1/*_grounded.pkl, qc.json)")
    ap.add_argument("--report", type=Path, required=True)
    ap.add_argument("--leakage", type=Path, nargs="*", default=[], help="combined training .npz files to check")
    ap.add_argument("--spec", type=Path, default=None, help="dataset spec: held-out speakers and training take types")
    ap.add_argument("--workers", type=int, default=min(12, os.cpu_count() or 1))
    args = ap.parse_args()

    paths = sorted((args.batch_dir / "k1").glob("*_grounded.pkl"))
    human = {}
    if (args.batch_dir / "qc.json").exists():
        human = {c["name"]: c for c in json.loads((args.batch_dir / "qc.json").read_text())["clips"]}
    rows = []
    for p, r in zip(paths, check_all(paths, args.workers)):
        name = p.stem.removesuffix("_grounded")
        h = human.get(name, {})
        r.update(name=name, **{k: h[k] for k in ("hand_fwd_human_m", "ik_fail_frames", "feet_human_cm", "max_foot_move_cm") if k in h})
        rows.append(r)
    flag(rows)

    leaks = {}
    if args.leakage:
        import beat2_segments as bs
        spec = bs.load_spec(args.spec)
        split = bs.load_split(spec["beat2_dir"])
        heldout = {s for s, g in bs.speaker_groups(spec, split).items() if g == "heldout"}
        allowed = set(spec["sets"]["train"]["takes"])
        for npz in args.leakage:
            leaks[str(npz)] = leakage(combined_clip_names(npz), split, heldout, allowed)
    calibration_report(rows, leaks, args.report, str(args.batch_dir))
    (args.batch_dir / "gate1.json").write_text(json.dumps(rows, indent=1, default=str))  # every number, per clip
    print(f"[qc] {len(rows)} clips, {sum(bool(r['flags']) for r in rows)} flagged, "
          f"{sum(bool(r['severe']) for r in rows)} severe -> {args.report}")


if __name__ == "__main__":
    main()
