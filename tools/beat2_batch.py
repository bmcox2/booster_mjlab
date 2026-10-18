"""BEAT2 takes -> still, gesturing 10 s windows -> grounded K1 clips -> QC table -> train / held-out artifacts.

For every take of the listed speakers:
1. pick windows: beat2_to_gmr's --find-still scoring, per take: drop windows where an ankle moves more
   than --max-foot-move, rank the rest by arm activity, keep the top --per-take non-overlapping ones
2. convert each window (beat2_to_gmr: Y-up -> Z-up, 16 betas, trimmed audio .wav alongside)
3. retarget with GMR, headless (tools/gmr_retarget.py, run with GMR's venv)
4. ground_clip (flatten stance feet, plant them, put the lowest point on the floor)
5. QC every clip on booster-mjlab's K1 model and write a table to notes/ (--qc), flagging outliers
6. combine-motions twice: one artifact for the training speakers, one for the held-out speakers

Every stage skips clips that are already done, so re-running after downloading more speakers only
processes the new takes. Use --force to redo everything.

Usage (from ~/projects/booster-mjlab):
    uv run python tools/beat2_batch.py \\
        --train 2_scott 1_wayne 3_solomon 4_lawrence 7_sophie 9_miranda --heldout 11_nidal 21_ayana
    ... --no-upload        # build local combined files in <out-dir>/combined/ instead of uploading
    ... --exclude severe   # leave severely flagged clips out of the artifacts (see SEVERE; all stay in the QC table)
    ... --exclude flagged  # leave every flagged clip out
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

import mujoco
import numpy as np

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import beat2_to_gmr as b2g  # noqa: E402
from ground_clip import BODY, DEFAULT_GMR_XML, DEFAULT_ROBOT_XML, JOINT, RENAME, Grounder  # noqa: E402

GMR_PYTHON = Path.home() / "projects/GMR/.venv/bin/python"

# Fixed QC limits. Clips that trained to 50/50 (wave_000113/000508/001104, talk_scott_1_1_t34-44) are
# at most: K1 feet 1.8 cm, trunk height range 1.8 cm, knees 14-36 deg, 0 joint-limit frames.
QC_LIMITS = {
    # The K1 is ~0.6x human scale, so --max-foot-move's 10 cm on the human allows ~6 cm on the K1;
    # more than this means retargeting/grounding added foot motion.
    "feet_k1_cm": 8.0,
    "trunk_drop_cm": 5.0,      # trunk height range over the clip (squat, lunge, big weight shift)
    "knee_max_deg": 60.0,      # deep knee bend
    "limit_frac": 0.05,        # share of frames with a joint group within 1 deg of a limit (see LIMIT_KINDS)
    "arms_k1_cm_s": 5.0,       # below this the K1's hands barely move: not much gesture left
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
ROBUST_Z = 3.5  # also flag values this many robust SDs (median / MAD) from the batch
# Severe = the reference itself is suspect, so `--exclude severe` drops it. Head or shoulder held at a
# limit is not severe: the clipped pose is still valid K1 motion, only less expressive.
SEVERE_TWIST_FRAC = 0.5  # upper-arm twist at its limit on more than this share of frames
# Arm on the wrong side: the K1's hand is on average this far behind the trunk while the human's wrist is
# this far in front of the pelvis (GMR's IK stuck with the arm swung back). Severe: the reference is wrong.
ARM_BEHIND_M, HUMAN_FRONT_M = 0.05, 0.05
# Joint jump: a joint moves more than this in one 1/30 s frame. GMR's IK flipping branch (e.g. the
# upper-arm twist snapping 90 deg), not the speaker: the hand reference teleports, no policy can track
# it, and adaptive sampling then pours most training starts into that bin (run 0lg80c7d: 70-77% of
# starts on wayne_0_9_9_t12-22). Among 152 clips the 4 glitches were 0.92-1.57 rad; real fast motion
# (elbow bends, quick twists) stayed <= 0.52 rad. Severe.
JOINT_JUMP_RAD = 0.6
# Feet are left out: K1 foot motion is ~1 cm for most clips with a long tail of weight shifts (4-7 cm,
# within what --max-foot-move allows), so a batch-relative test flags normal speakers. The fixed
# feet_k1_cm limit still applies.
MAD_FLOOR = {"arms_k1_cm_s": 2.0, "trunk_drop_cm": 0.5, "knee_max_deg": 3.0}


def find_takes(beat2_dir: Path, speaker: str) -> list[Path]:
    """Takes of one speaker: '2_scott' matches 2_scott_*.npz; a bare 'scott' matches any id."""
    motion_dir = beat2_dir / "smplxflame_30"
    pattern = f"{speaker}_*.npz" if re.match(r"\d+_", speaker) else f"[0-9]*_{speaker}_*.npz"
    return sorted(motion_dir.glob(pattern))


def clip_name(take: Path, start: float, end: float) -> str:
    return f"{take.stem.split('_', 1)[1]}_t{start:.0f}-{end:.0f}"  # 2_scott_0_1_1 -> scott_0_1_1_t34-44


def newer(dst: Path, src: Path) -> bool:
    return dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime


# ---------------------------------------------------------------------------------------- stages

def pick_windows(take: Path, args) -> tuple[list[dict], str]:
    """Top --per-take non-overlapping still windows of one take, best arm activity first."""
    t = b2g.read_take(take, args.model_dir, None, verbose=False)
    if len(t["root_orient"]) / t["fps"] < args.window:
        return [], "shorter than the window"
    rows = b2g.score_windows(take, t, args.model_dir, args.window)
    still = sorted((r for r in rows if r["foot_move"] <= args.max_foot_move), key=lambda r: -r["arm"])
    picks = b2g.top_non_overlapping(still, args.per_take)
    note = "" if len(picks) == args.per_take else f"only {len(picks)} still window(s) of {len(rows)}"
    return picks, note


def convert(clips: list[dict], args) -> None:
    for c in clips:
        if newer(c["smplx"], c["take"]) and not args.force:
            continue
        wav = args.beat2_dir / "wave16k" / f"{c['take'].stem}.wav"
        ns = argparse.Namespace(start=c["start"], end=c["end"], up=None, wav=wav if wav.exists() else None,
                                model_dir=args.model_dir)
        with contextlib.redirect_stdout(io.StringIO()):  # converter is chatty; errors still raise
            b2g.convert(c["take"], c["smplx"], ns)


def retarget(clips: list[dict], args) -> None:
    todo = [c for c in clips if args.force or not newer(c["k1"], c["smplx"])]
    if not todo:
        return
    print(f"[gmr] retargeting {len(todo)} clip(s) headless with {GMR_PYTHON}")
    cmd = [str(GMR_PYTHON), str(TOOLS / "gmr_retarget.py")]
    if args.ik_config:
        cmd += ["--ik-config", str(args.ik_config.resolve())]
    cmd += [str(p) for c in todo for p in (c["smplx"], c["k1"])]
    env = {k: v for k, v in os.environ.items() if k not in ("DISPLAY", "WAYLAND_DISPLAY")}  # prove it's headless
    subprocess.run(cmd, check=True, env=env)


def ground(clips: list[dict], grounder: Grounder, args) -> None:
    for c in clips:
        log = c["grounded"].with_suffix(".txt")
        if newer(c["grounded"], c["k1"]) and log.exists() and not args.force:
            continue
        out = io.StringIO()
        tmp = c["grounded"].with_name(c["grounded"].stem + ".tmp.pkl")  # rename when complete (safe to interrupt)
        with contextlib.redirect_stdout(out):
            grounder.ground(c["k1"], tmp)
        os.replace(tmp, c["grounded"])
        log.write_text(out.getvalue())
        print(f"[ground] {c['name']}")


# ---------------------------------------------------------------------------------------- QC

class K1Checker:
    """QC numbers for a grounded clip, on booster-mjlab's K1 model (the one training uses)."""

    def __init__(self, grounder: Grounder):
        self.g = grounder
        rob = grounder.rob
        self.joint_names = [RENAME.get(n, n) for n in grounder.gmr_joints]  # .pkl column order
        self.limits = np.array([rob.jnt_range[mujoco.mj_name2id(rob, JOINT, n)] for n in self.joint_names])
        self.knees = [self.joint_names.index(f"{s}_Knee_Pitch") for s in ("Left", "Right")]
        # Elbow_Yaw is the elbow bend; its limit at 0 is a straight arm and isn't counted as a limit hit.
        self.elbow_bend = np.array(["Elbow_Yaw" in n for n in self.joint_names])
        self.body = {b: mujoco.mj_name2id(rob, BODY, b)
                     for b in ("Trunk", "left_hand_link", "right_hand_link", "left_foot_link", "right_foot_link")}

    def check(self, path: Path) -> dict:
        import pickle

        with open(path, "rb") as f:
            m = pickle.load(f)
        g, data, b = self.g, self.g.data, self.body
        fps = float(m["fps"])
        feet, hands = [], []
        for frame in zip(m["root_pos"], m["root_rot"], m["dof_pos"]):
            g.set_pose(*frame)
            R, o = data.xmat[b["Trunk"]].reshape(3, 3), data.xpos[b["Trunk"]]
            hands.append([R.T @ (data.xpos[b[h]] - o) for h in ("left_hand_link", "right_hand_link")])
            feet.append([data.xpos[b[f]][:2].copy() for f in ("left_foot_link", "right_foot_link")])
        feet, hands = np.array(feet), np.array(hands)  # (T, 2, 2), (T, 2, 3); hands: trunk frame, x forward
        dof = np.asarray(m["dof_pos"])
        lo, hi = self.limits[:, 0], self.limits[:, 1]
        straight_lo, straight_hi = self.elbow_bend & (lo == 0), self.elbow_bend & (hi == 0)  # straight-arm side
        near = ((dof <= lo + LIMIT_MARGIN) & ~straight_lo) | ((dof >= hi - LIMIT_MARGIN) & ~straight_hi)
        kinds = {}
        for j in np.flatnonzero(near.any(axis=0)):
            kind = next(k for key, k in LIMIT_KINDS if key in self.joint_names[j])
            kinds.setdefault(kind, np.zeros(len(dof), bool))
            kinds[kind] |= near[:, j]
        knee = np.degrees(dof[:, self.knees])
        step = np.abs(np.diff(dof, axis=0))
        jump_frame, jump_joint = np.unravel_index(step.argmax(), step.shape)
        return {
            "feet_k1_cm": float(np.linalg.norm(feet - np.median(feet, axis=0), axis=-1).max() * 100),
            "arms_k1_cm_s": float(np.linalg.norm(np.diff(hands, axis=0), axis=-1).mean() * fps * 100),
            "hand_fwd_k1_m": [float(v) for v in hands[:, :, 0].mean(axis=0)],
            "trunk_drop_cm": float(np.ptp(np.asarray(m["root_pos"])[:, 2]) * 100),
            "knee_min_deg": [float(v) for v in knee.min(axis=0)],
            "knee_max_deg": float(knee.max()),
            "knee_range_deg": [[float(lo), float(hi)] for lo, hi in zip(knee.min(axis=0), knee.max(axis=0))],
            "limit_frac": float(near.any(axis=1).mean()),
            "limit_kinds": {k: float(v.mean()) for k, v in kinds.items()},
            "limit_joints": {self.joint_names[j]: int(near[:, j].sum()) for j in np.flatnonzero(near.any(axis=0))},
            "joint_jump_rad": float(step.max()),
            "joint_jump_at": [self.joint_names[jump_joint], float((jump_frame + 1) / fps)],  # joint, seconds
        }


def human_wrist_forward(smplx_npz: Path, model_dir: Path) -> list[float]:
    """Mean (left, right) wrist position along the human's forward axis, relative to the pelvis, m."""
    take = b2g.read_take(smplx_npz, model_dir, "+z", verbose=False)
    pos, pelvis_rot = b2g.body_joint_positions(take, model_dir)
    return [float(pelvis_rot.inv().apply(pos[:, j] - pos[:, 0])[:, 2].mean())  # SMPL-X body +z = forward
            for j in (b2g.L_WRIST, b2g.R_WRIST)]


def ik_failures(log: Path) -> int:
    m = re.search(r"IK failed on (\d+) frames", log.read_text()) if log.exists() else None
    return int(m.group(1)) if m else 0


def flag(rows: list[dict]) -> None:
    """Fixed limits, plus robust outliers relative to this batch."""
    stats = {}
    for k, floor in MAD_FLOOR.items():
        v = np.array([r[k] for r in rows])
        stats[k] = (np.median(v), max(1.4826 * np.median(np.abs(v - np.median(v))), floor))
    for r in rows:
        f = []
        if r["feet_human_cm"] > r["max_foot_move_cm"]:
            f.append("human steps")
        if r["feet_k1_cm"] > QC_LIMITS["feet_k1_cm"]:
            f.append(f"K1 feet move {r['feet_k1_cm']:.0f} cm")
        if r["trunk_drop_cm"] > QC_LIMITS["trunk_drop_cm"]:
            f.append(f"trunk drop {r['trunk_drop_cm']:.0f} cm")
        if r["knee_max_deg"] > QC_LIMITS["knee_max_deg"]:
            f.append(f"knee {r['knee_max_deg']:.0f} deg")
        for kind, frac in r["limit_kinds"].items():
            if frac > QC_LIMITS["limit_frac"]:
                f.append(f"{kind} at limit {frac:.0%}")
        if r["arms_k1_cm_s"] < QC_LIMITS["arms_k1_cm_s"]:
            f.append("little arm motion")
        if r["ik_fail_frames"]:
            f.append(f"ground IK failed {r['ik_fail_frames']} frames")
        severe = []
        for k, (med, sd) in stats.items():
            z = (r[k] - med) / sd
            if abs(z) > ROBUST_Z:
                f.append(f"outlier {k.rsplit('_', 1)[0].replace('_', ' ')} (z {z:+.1f})")
                if k == "trunk_drop_cm" and z > 0:
                    severe.append(f[-1])
        if r["limit_kinds"].get("upper-arm twist", 0.0) > SEVERE_TWIST_FRAC:
            severe.append(next(x for x in f if x.startswith("upper-arm twist")))
        if r["ik_fail_frames"]:
            severe.append(next(x for x in f if x.startswith("ground IK failed")))
        if r["joint_jump_rad"] > JOINT_JUMP_RAD:
            joint, t = r["joint_jump_at"]
            f.append(f"joint jump {r['joint_jump_rad']:.2f} rad ({joint} at {t:.1f} s)")
            severe.append(f[-1])
        for side, k1, human in zip(("left", "right"), r["hand_fwd_k1_m"], r["hand_fwd_human_m"]):
            if k1 < -ARM_BEHIND_M and human > HUMAN_FRONT_M:
                f.append(f"{side} arm behind body (human's in front)")
                severe.append(f[-1])
        r["flags"], r["severe"] = f, severe


def speaker_rows(rows: list[dict], notes: dict) -> list[str]:
    """Per-speaker counts: how many clips, and how often each kind of flag fires (share of that speaker's clips)."""
    out = []
    for spk in dict.fromkeys(r["speaker"] for r in rows):
        rs = [r for r in rows if r["speaker"] == spk]
        n = len(rs)

        def share(test):
            k = sum(1 for r in rs if test(r))
            return f"{k} ({k / n:.0%})"

        def has(prefix):
            return lambda r: any(x.startswith(prefix) for x in r["flags"])

        other = lambda r: any(not x.startswith(("head", "shoulder", "upper-arm twist")) for x in r["flags"])  # noqa: E731
        out.append(f"| {rs[0]['split']} | {spk} | {notes['speaker_takes'].get(spk, 0)} | {n} | {share(lambda r: r['flags'])} | "
                   f"{share(lambda r: r['severe'])} | {share(has('head'))} | {share(has('shoulder'))} | "
                   f"{share(has('upper-arm twist'))} | {share(other)} |")
    return out


def write_qc(rows: list[dict], notes: dict, args, path: Path) -> None:
    def cell(r):
        knees = " / ".join(f"{lo:.0f}–{hi:.0f}" for lo, hi in r["knee_range_deg"])
        limits = ", ".join(f"{k} {v:.0%}" for k, v in sorted(r["limit_kinds"].items(), key=lambda kv: -kv[1])) or "0"
        return (f"| {r['split']} | `{r['name']}` | {r['take']} {r['start']:.0f}–{r['end']:.0f} s | "
                f"{r['feet_human_cm']:.1f} / {r['feet_k1_cm']:.1f} | {r['arms_human_cm_s']:.0f} / {r['arms_k1_cm_s']:.0f} | "
                f"{r['trunk_drop_cm']:.1f} | {knees} | {limits} | {flags(r)} |")

    def flags(r):
        text = "; ".join(f"**{x}**" if x in r["severe"] else x for x in r["flags"]) or "—"
        return text + (" *(excluded)*" if r["excluded"] else "")

    flagged = [r for r in rows if r["flags"]]
    by_split = {s: [r for r in rows if r["split"] == s] for s in ("train", "heldout")}
    lines = [
        "# BEAT2 Clip QC",
        "",
        f"Generated {date.today()} by `tools/beat2_batch.py` "
        f"({args.window:g} s windows, top {args.per_take} per take, ankles within {args.max_foot_move * 100:.0f} cm). "
        "One row per clip; rerun the script to refresh.",
        "",
        f"- **Clips:** {len(rows)} ({len(by_split['train'])} train, {len(by_split['heldout'])} held-out), "
        f"**{len(flagged)} flagged**, {sum(bool(r['severe']) for r in rows)} severe (**bold**); "
        f"{sum(r['excluded'] for r in rows)} left out of the artifacts (`--exclude {args.exclude}`)",
        "- **Train speakers:** " + ", ".join(f"{s} ({notes['speaker_clips'].get(s, 0)} clips)" for s in args.train),
        "- **Held-out speakers:** " + ", ".join(f"{s} ({notes['speaker_clips'].get(s, 0)} clips)" for s in args.heldout),
    ]
    if notes["missing_speakers"]:
        lines.append(f"- **No takes found (not downloaded?):** {', '.join(notes['missing_speakers'])}")
    if notes["short_takes"]:
        lines.append("- **Takes with fewer windows:** " + "; ".join(f"{t} ({n})" for t, n in notes["short_takes"]))
    for split, art in notes.get("artifacts", {}).items():
        lines.append(f"- **{split} artifact:** `{art}`")
    lines += [
        "",
        "## Per speaker",
        "",
        "| split | speaker | takes | clips | flagged | severe | head at limit | shoulder at limit | upper-arm twist | other |",
        "|---|---|---|---|---|---|---|---|---|---|",
        *speaker_rows(rows, notes),
        "",
        "## Columns",
        "- **feet human / K1 (cm):** farthest an ankle (human, BEAT2) / foot (K1, after ground_clip) strays from its median spot",
        "- **arms human / K1 (cm/s):** mean wrist speed relative to the pelvis (human) / hand speed relative to the trunk (K1)",
        "- **trunk drop (cm):** K1 trunk height range over the clip",
        "- **knees L / R (deg):** K1 knee angle range (0 = straight, limit 128)",
        "- **joint limits:** share of frames with a joint within 1° of a limit, by group. *upper-arm twist*: "
        "with a straight arm, twist doesn't move the hand, so GMR's IK drifts to the limit (hand is right, "
        "arm is twisted); *head*: the speaker looks further than the K1 can, so nods are clipped; "
        "*shoulder* / *leg*: pose clipped. A straight elbow (elbow bend at 0) is normal and not counted",
        "",
        "## Flags",
        f"Fixed: K1 feet > {QC_LIMITS['feet_k1_cm']:g} cm, trunk drop > {QC_LIMITS['trunk_drop_cm']:g} cm, "
        f"knee > {QC_LIMITS['knee_max_deg']:g}°, a joint group at its limit > {QC_LIMITS['limit_frac']:.0%} of frames, "
        f"K1 hands < {QC_LIMITS['arms_k1_cm_s']:g} cm/s, any ground_clip IK failure. Clips that trained to 50/50 "
        "so far: K1 feet ≤ 1.8 cm, trunk ≤ 1.8 cm, knees 14–36°, 0 limit frames, hands 8–16 cm/s.",
        f"Outlier: more than {ROBUST_Z:g} robust SDs (median / MAD) from this batch on arms, trunk, or knee "
        "(not feet: most clips move ~1 cm with a long tail of normal weight shifts; the fixed limit covers feet).",
        f"**Severe** (dropped by `--exclude severe`): upper-arm twist at its limit on > {SEVERE_TWIST_FRAC:.0%} of frames, "
        f"any ground_clip IK failure, a trunk-drop outlier, or an arm on the wrong side (K1 hand > {ARM_BEHIND_M * 100:.0f} cm "
        f"behind the trunk while the human's wrist is > {HUMAN_FRONT_M * 100:.0f} cm in front), or a joint jump (a joint moving > {JOINT_JUMP_RAD:g} rad "
        "in one 1/30 s frame: GMR's IK flipping, the hand reference teleports). Head or shoulder held at a limit is not severe: "
        "the clipped pose is still valid K1 motion.",
        "",
        "| split | clip | source | feet human / K1 (cm) | arms human / K1 (cm/s) | trunk drop (cm) | knees L / R (deg) "
        "| joint limits | flags |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    lines += [cell(r) for r in rows]
    path.write_text("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------------------- combine

def combine(split: str, clips: list[dict], args) -> str | None:
    if not clips:
        print(f"[combine] no {split} clips; skipping")
        return None
    name = f"{args.artifact_prefix}-{split}"
    cmd = ["uv", "run", "combine-motions", *[str(c["grounded"]) for c in clips]]
    if args.upload:
        cmd += ["--artifact-name", name] + (["--entity", args.entity] if args.entity else [])
    else:
        out = args.out_dir / "combined" / f"{name}.npz"
        cmd += ["--no-upload", "--output", str(out)]
    print(f"[combine] {split}: {len(clips)} clips -> {name}")
    res = subprocess.run(cmd, check=True, cwd=REPO, capture_output=True, text=True)
    print("\n".join(line for line in res.stdout.splitlines() if line.startswith(("     total", "[out]", "[upload]"))))
    m = re.search(r"Uploaded artifact: (\S+)", res.stdout)
    return m.group(1) if m else str(args.out_dir / "combined" / f"{name}.npz")


# ---------------------------------------------------------------------------------------- main

def main() -> None:
    home = Path.home()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--train", nargs="+", required=True, help="training speakers, e.g. 2_scott 1_wayne")
    ap.add_argument("--heldout", nargs="+", required=True, help="held-out speakers, e.g. 11_nidal 21_ayana")
    ap.add_argument("--beat2-dir", type=Path, default=home / "robotics/data/BEAT2/beat_english_v2.0.0")
    ap.add_argument("--out-dir", type=Path, default=home / "robotics/data/beat2_batch")
    ap.add_argument("--qc", type=Path, default=REPO / "notes/beat2-qc.md", help="QC table to write")
    ap.add_argument("--window", type=float, default=10.0, help="window length, seconds")
    ap.add_argument("--per-take", type=int, default=2, help="windows per take")
    ap.add_argument("--max-foot-move", type=float, default=0.10, help="m; see beat2_to_gmr --find-still")
    ap.add_argument("--model-dir", type=Path, default=b2g.DEFAULT_MODEL_DIR)
    ap.add_argument("--artifact-prefix", default="beat2-10s", help="artifacts: <prefix>-train, <prefix>-heldout")
    ap.add_argument("--entity", default=os.environ.get("WANDB_ENTITY"))
    ap.add_argument("--no-upload", dest="upload", action="store_false", help="write <out-dir>/combined/*.npz instead")
    ap.add_argument("--exclude", choices=("none", "severe", "flagged"), default="none",
                    help="leave clips out of the artifacts: severe flags only, or any flag (all stay in the QC table)")
    ap.add_argument("--ik-config", type=Path, default=None,
                    help="custom GMR IK config for the K1 (e.g. tools/ik_configs/smplx_to_k1_torso.json); "
                         "use a separate --out-dir, since cached clips are not redone when this changes")
    ap.add_argument("--force", action="store_true", help="redo every stage")
    args = ap.parse_args()

    overlap = set(args.train) & set(args.heldout)
    if overlap:
        sys.exit(f"Speakers in both splits: {sorted(overlap)}")
    if not GMR_PYTHON.exists():
        sys.exit(f"GMR's venv python not found: {GMR_PYTHON}")

    # 1. windows
    t0 = time.time()
    clips, notes = [], {"missing_speakers": [], "short_takes": [], "speaker_clips": {}, "speaker_takes": {}}
    for split, speakers in (("train", args.train), ("heldout", args.heldout)):
        for spk in speakers:
            takes = find_takes(args.beat2_dir, spk)
            if not takes:
                print(f"[warn] {spk}: no takes in {args.beat2_dir / 'smplxflame_30'}")
                notes["missing_speakers"].append(spk)
                continue
            notes["speaker_takes"][spk] = len(takes)
            for take in takes:
                try:
                    picks, note = pick_windows(take, args)
                except Exception as e:  # e.g. a take that is still downloading
                    picks, note = [], f"unreadable: {type(e).__name__}"
                    print(f"[warn] {take.name}: {e}")
                if note:
                    notes["short_takes"].append((take.stem, note))
                for w in picks:
                    name = clip_name(take, w["start"], w["end"])
                    clips.append({
                        "split": split, "speaker": spk, "take": take, "start": w["start"], "end": w["end"],
                        "name": name, "feet_human_cm": w["foot_move"] * 100, "arms_human_cm_s": w["arm"] * 100,
                        "pelvis_drop_human_cm": w["pelvis_drop"] * 100,
                        "smplx": args.out_dir / "smplx" / f"{name}.npz",
                        "k1": args.out_dir / "k1" / f"{name}.pkl",
                        "grounded": args.out_dir / "k1" / f"{name}_grounded.pkl",
                    })
                    notes["speaker_clips"][spk] = notes["speaker_clips"].get(spk, 0) + 1
            print(f"[windows] {spk} ({split}): {len(takes)} takes -> {notes['speaker_clips'].get(spk, 0)} clips")
    if not clips:
        sys.exit("No clips: check --beat2-dir and the speaker names")

    # 2-4. convert, retarget, ground
    convert(clips, args)
    print(f"[convert] {len(clips)} windows ready in {args.out_dir / 'smplx'}")
    retarget(clips, args)
    grounder = Grounder(DEFAULT_GMR_XML, DEFAULT_ROBOT_XML)
    ground(clips, grounder, args)

    # 5. QC
    checker = K1Checker(grounder)
    rows = []
    for c in clips:
        r = {k: v for k, v in c.items() if k not in ("smplx", "k1", "grounded")}
        r.update(take=c["take"].stem, max_foot_move_cm=args.max_foot_move * 100, ik_fail_frames=ik_failures(c["grounded"].with_suffix(".txt")),
                 hand_fwd_human_m=human_wrist_forward(c["smplx"], args.model_dir))
        r.update(checker.check(c["grounded"]))
        rows.append(r)
    flag(rows)
    for c, r in zip(clips, rows):
        c["flags"] = r["flags"]

    # 6. combine
    for c, r in zip(clips, rows):
        c["excluded"] = r["excluded"] = bool(
            (args.exclude == "severe" and r["severe"]) or (args.exclude == "flagged" and r["flags"]))
    keep = [c for c in clips if not c["excluded"]]
    notes["artifacts"] = {}
    for split in ("train", "heldout"):
        art = combine(split, [c for c in keep if c["split"] == split], args)
        if art:
            notes["artifacts"][split] = art

    write_qc(rows, notes, args, args.qc)
    (args.out_dir / "qc.json").write_text(json.dumps({"notes": notes, "clips": rows}, indent=2, default=str))
    flagged = [r for r in rows if r["flags"]]
    print(f"\n[qc] {len(rows)} clips, {len(flagged)} flagged -> {args.qc}")
    for r in flagged:
        mark = "EXCLUDED" if r["excluded"] else ("severe" if r["severe"] else "")
        print(f"  {r['split']:<7} {r['name']:<28} {mark:<8} {'; '.join(r['flags'])}")
    print(f"[done] {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
