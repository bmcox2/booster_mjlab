"""Convert a BEAT2 SMPL-X clip (smplxflame_30/*.npz) into the AMASS-style .npz that GMR reads.

GMR's smplx_to_robot.py loads AMASS SMPL-X files and reads `root_orient`, `pose_body`, `trans`,
`betas`, `gender`, and `mocap_frame_rate`. BEAT2 stores the whole pose in one `poses` array
(165 = 55 joints x 3, axis-angle) plus 300 shape betas and FLAME face expressions. This script:

- splits `poses` into root_orient (joint 0) and pose_body (joints 1-21); hands, jaw and eyes are dropped
  (K1 has no hands or face, and GMR zeroes them anyway)
- keeps the first 16 betas (GMR's SMPL-X model uses 16, like AMASS; other counts crash it)
- detects which world axis is "up" from the body's own up direction, and if it isn't +z
  (AMASS/GMR convention), rotates root orientation and translation so it is. SMPL-X rotates the
  body about the pelvis, not the origin, so the translation fix needs the pelvis rest position,
  which is read from the SMPL-X model file (--model-dir)
- optionally trims to a time window (BEAT2 takes are ~1 min; start with 20-30 s)

It also copies the matching 16 kHz audio segment if --wav is given, so a sim video can be dubbed later.

--find-still scans one or more takes for windows to convert instead: it drops windows where the
feet move (steps, walking) and ranks the rest by arm activity (wrist speed relative to the pelvis),
so the top pick is a speaker standing in place and gesturing, not standing silently with arms down.

Usage (any Python with numpy + scipy, e.g. GMR's venv):
    # 1. find a window: scan all of scott's takes for 20 s windows
    ~/projects/GMR/.venv/bin/python tools/beat2_to_gmr.py --find-still --window 20 \
        ~/robotics/data/BEAT2/beat_english_v2.0.0/smplxflame_30/2_scott_*.npz
    # 2. convert it
    ~/projects/GMR/.venv/bin/python tools/beat2_to_gmr.py \
        ~/robotics/data/BEAT2/beat_english_v2.0.0/smplxflame_30/2_scott_0_1_1.npz \
        ~/robotics/data/beat2_gmr/scott_1_1_t10-30.npz --start 10 --end 30 \
        --wav ~/robotics/data/BEAT2/beat_english_v2.0.0/wave16k/2_scott_0_1_1.wav
    # 3. retarget
    cd ~/projects/GMR && .venv/bin/python scripts/smplx_to_robot.py \
        --smplx_file ~/robotics/data/beat2_gmr/scott_1_1_t10-30.npz --robot booster_k1 \
        --save_path ~/robotics/data/k1_motions/talk_scott_1_1_t10-30.pkl
"""
import argparse
from pathlib import Path

import numpy as np
from scipy.io import wavfile
from scipy.spatial.transform import Rotation as R

# GMR builds SMPL-X with smplx's default of 16 shape betas (same as AMASS); any other count crashes in lbs.
NUM_BETAS = 16
DEFAULT_MODEL_DIR = Path.home() / "projects/GMR/assets/body_models/smplx"
AXES = {"+x": [1, 0, 0], "-x": [-1, 0, 0], "+y": [0, 1, 0], "-y": [0, -1, 0], "+z": [0, 0, 1], "-z": [0, 0, -1]}
# SMPL-X body joints used by --find-still (pelvis + 21 body joints are enough for these)
NUM_BODY_JOINTS = 22
L_ANKLE, R_ANKLE, L_WRIST, R_WRIST = 7, 8, 20, 21
MAX_WRIST_SPEED = 3.0  # m/s; faster is a mocap glitch, clipped so it can't win the ranking


def to_str(x) -> str:
    x = x.item() if isinstance(x, np.ndarray) else x
    return x.decode() if isinstance(x, bytes) else str(x)


def detect_up(root_orient: np.ndarray) -> tuple[str, np.ndarray, float]:
    """World axis the body's own up (SMPL-X model +y) points along, averaged over the clip."""
    body_up = R.from_rotvec(root_orient).apply([0.0, 1.0, 0.0]).mean(axis=0)
    name, vec = max(AXES.items(), key=lambda kv: float(np.dot(body_up, kv[1])))
    return name, body_up, float(np.dot(body_up / np.linalg.norm(body_up), vec))


def rotation_to_z_up(up: str) -> R:
    """Rotation taking the detected up axis to +z."""
    a = np.array(AXES[up], dtype=float)
    if np.allclose(a, [0, 0, 1]):
        return R.identity()
    if np.allclose(a, [0, 0, -1]):
        return R.from_euler("x", 180, degrees=True)
    axis = np.cross(a, [0, 0, 1])
    return R.from_rotvec(axis / np.linalg.norm(axis) * np.pi / 2)


def rest_skeleton(model_dir: Path, gender: str, betas: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Rest-pose body joint positions for these betas, and each joint's parent index."""
    path = model_dir / f"SMPLX_{gender.upper()}.npz"
    if not path.exists():
        raise SystemExit(f"Need {path} for the body's rest skeleton (set --model-dir)")
    m = np.load(path, allow_pickle=True)
    v = m["v_template"] + m["shapedirs"][:, :, : len(betas)] @ betas
    joints = m["J_regressor"][:NUM_BODY_JOINTS] @ v
    parents = m["kintree_table"][0, :NUM_BODY_JOINTS].astype(int)
    return joints, parents


def read_take(path: Path, model_dir: Path, up_override: str | None, verbose: bool = True) -> dict:
    """Load a BEAT2 (or AMASS-style) clip and rotate it to z-up. Not trimmed or recentered."""
    d = np.load(path, allow_pickle=True)
    if verbose:
        print(f"[in] {path.name}: " + ", ".join(f"{k}{d[k].shape}" for k in d.files))

    fps = float(d["mocap_frame_rate"]) if "mocap_frame_rate" in d.files else 30.0
    if "poses" in d.files:
        poses = d["poses"].reshape(len(d["poses"]), -1)
        root_orient, pose_body = poses[:, 0:3], poses[:, 3:66]
    elif "root_orient" in d.files and "pose_body" in d.files:  # already AMASS-style
        root_orient, pose_body = d["root_orient"], d["pose_body"]
    else:
        raise SystemExit(f"{path.name}: don't know this layout: keys {d.files}")
    trans = d["trans"].reshape(-1, 3)
    betas = np.zeros(NUM_BETAS)
    if "betas" in d.files:
        src_betas = np.asarray(d["betas"]).reshape(-1)[:NUM_BETAS]
        betas[: len(src_betas)] = src_betas
    gender = to_str(d["gender"]) if "gender" in d.files else "neutral"
    if gender not in ("neutral", "male", "female"):
        print(f"[gender] '{gender}' isn't a SMPL-X model name, using neutral")
        gender = "neutral"

    if up_override:
        up = up_override
    else:
        up, body_up, alignment = detect_up(root_orient)
        if verbose:
            print(f"[up] body up averages {np.round(body_up, 3)} -> world {up} (alignment {alignment:.3f})")
        if alignment < 0.9:
            print(f"[up] WARNING ({path.name}): weak alignment; the speaker may be leaning a lot. "
                  "Check in GMR's viewer.")
    if up != "+z":
        fix = rotation_to_z_up(up)
        # pelvis = j0 + trans, and the body rotates about it, so rotating the world means
        # rotating (j0 + trans); rotating trans alone would shift the body by fix(j0) - j0 (~36 cm)
        j0 = rest_skeleton(model_dir, gender, betas)[0][0]
        root_orient = (fix * R.from_rotvec(root_orient)).as_rotvec()
        trans = fix.apply(trans + j0) - j0
        if verbose:
            print(f"[up] rotated {up} -> +z")
    return dict(fps=fps, root_orient=root_orient, pose_body=pose_body, trans=trans, betas=betas, gender=gender)


def body_joint_positions(take: dict, model_dir: Path) -> tuple[np.ndarray, R]:
    """World positions of the 22 body joints per frame (N, 22, 3), plus the pelvis rotation.

    Forward kinematics on the rest skeleton; matches smplx's joint output for these joints.
    """
    rest, parents = rest_skeleton(model_dir, take["gender"], take["betas"])
    n = len(take["root_orient"])
    local = take["pose_body"].reshape(n, -1, 3)
    rots = [R.from_rotvec(take["root_orient"])]
    pos = np.zeros((n, NUM_BODY_JOINTS, 3))
    pos[:, 0] = rest[0] + take["trans"]
    for i in range(1, NUM_BODY_JOINTS):
        par = parents[i]
        pos[:, i] = pos[:, par] + rots[par].apply(rest[i] - rest[par])
        rots.append(rots[par] * R.from_rotvec(local[:, i - 1]))
    return pos, rots[0]


def score_windows(name: str, take: dict, model_dir: Path, window_s: float) -> list[dict]:
    """Stillness (feet) and arm activity for every window_s-long window, 1 s apart."""
    fps = take["fps"]
    pos, pelvis_rot = body_joint_positions(take, model_dir)
    pelvis = pos[:, 0]
    # wrists in the pelvis frame, so turning or swaying the whole body doesn't count as gesturing
    wrists = np.stack([pelvis_rot.inv().apply(pos[:, j] - pelvis) for j in (L_WRIST, R_WRIST)], axis=1)
    wrist_speed = np.clip(np.linalg.norm(np.diff(wrists, axis=0), axis=-1) * fps, 0, MAX_WRIST_SPEED)
    ankles_xy = pos[:, [L_ANKLE, R_ANKLE], :2]

    n, w = len(pos), int(round(window_s * fps))
    rows = []
    for s in range(0, n - w + 1, max(1, int(round(fps)))):
        a = ankles_xy[s : s + w]
        foot_move = np.linalg.norm(a - np.median(a, axis=0), axis=-1).max()  # farthest either ankle strays
        rows.append(dict(
            take=name, start=s / fps, end=(s + w) / fps,
            arm=wrist_speed[s : s + w - 1].mean(),
            foot_move=foot_move,
            pelvis_drop=np.ptp(pelvis[s : s + w, 2]),
        ))
    return rows


def find_still(paths: list[Path], args) -> None:
    rows, lengths = [], {}
    for path in paths:
        take = read_take(path, args.model_dir, args.up, verbose=False)
        lengths[path] = len(take["root_orient"]) / take["fps"]
        if lengths[path] < args.window:
            print(f"[skip] {path.name}: {lengths[path]:.1f} s, shorter than the {args.window:g} s window")
            continue
        rows += score_windows(path, take, args.model_dir, args.window)
    if not rows:
        raise SystemExit("No windows to score")
    print(f"[scan] {len(paths)} take(s), {sum(lengths.values()) / 60:.1f} min, {len(rows)} windows of {args.window:g} s")

    still = [r for r in rows if r["foot_move"] <= args.max_foot_move]
    if still:
        ranked = sorted(still, key=lambda r: -r["arm"])
        print(f"[rank] {len(still)} windows keep both ankles within {args.max_foot_move * 100:.0f} cm; "
              "ranked by arm activity:")
    else:
        ranked = sorted(rows, key=lambda r: r["foot_move"])
        print(f"[rank] WARNING: no window keeps the ankles within {args.max_foot_move * 100:.0f} cm "
              "(raise --max-foot-move or scan more takes). Stillest windows instead:")

    picks = []  # best first, no two overlapping in the same take
    for r in ranked:
        if all(p["take"] != r["take"] or r["end"] <= p["start"] or r["start"] >= p["end"] for p in picks):
            picks.append(r)
        if len(picks) == args.top:
            break

    print(f"\n  #  {'take':<22} {'window':>13}  {'arm cm/s':>8}  {'feet move cm':>12}  {'pelvis drop cm':>14}")
    for i, r in enumerate(picks, 1):
        print(f"  {i}  {r['take'].stem:<22} {r['start']:5.0f}-{r['end']:<5.0f}s  {r['arm'] * 100:8.1f}  "
              f"{r['foot_move'] * 100:12.1f}  {r['pelvis_drop'] * 100:14.1f}")
    arms = np.array([r["arm"] for r in rows]) * 100
    print(f"\n  arm activity over all windows: median {np.median(arms):.1f}, max {arms.max():.1f} cm/s")
    best = picks[0]
    print(f"\nConvert #1 with:\n  {best['take']} <dst>.npz --start {best['start']:g} --end {best['end']:g}")


def convert(src: Path, dst: Path, args) -> None:
    if dst.suffix != ".npz":
        raise SystemExit(f"dst must end in .npz (np.savez would add it and GMR would miss the file): {dst}")
    take = read_take(src, args.model_dir, args.up)
    fps = take["fps"]

    n = len(take["root_orient"])
    s = int(round(args.start * fps))
    e = n if args.end is None else min(n, int(round(args.end * fps)))
    if not 0 <= s < e:
        raise SystemExit(f"Empty window: clip is {n / fps:.1f} s, asked for {args.start}-{args.end}")
    root_orient, pose_body, trans = take["root_orient"][s:e], take["pose_body"][s:e], take["trans"][s:e]
    print(f"[time] {fps:g} fps, clip {n / fps:.1f} s, keeping {s / fps:.1f}-{e / fps:.1f} s ({e - s} frames)")
    trans = trans - np.array([trans[0, 0], trans[0, 1], 0.0])  # start at the origin in x/y; height is fixed later by ground_clip

    dst.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        dst,
        root_orient=root_orient.astype(np.float32),
        pose_body=pose_body.astype(np.float32),
        trans=trans.astype(np.float32),
        betas=take["betas"].astype(np.float32),
        gender=np.array(take["gender"]),
        mocap_frame_rate=np.array(fps),
    )
    print(f"[out] {dst}  trans z range {trans[:, 2].min():.2f}-{trans[:, 2].max():.2f} m, "
          f"x/y travel {np.ptp(trans[:, 0]):.2f} / {np.ptp(trans[:, 1]):.2f} m")

    if args.wav:
        # scipy, not the stdlib wave module: BEAT2's wave16k files are 32-bit float, which wave can't read
        rate, audio = wavfile.read(args.wav, mmap=True)
        a = min(int(round(s / fps * rate)), len(audio))
        b = min(int(round(e / fps * rate)), len(audio))
        wav_out = dst.with_suffix(".wav")
        wavfile.write(wav_out, rate, np.array(audio[a:b]))
        got, want = (b - a) / rate, (e - s) / fps
        print(f"[out] {wav_out} ({got:.1f} s of audio)")
        if abs(got - want) > 0.1:
            print(f"[wav] WARNING: audio is {got:.1f} s but motion is {want:.1f} s; is this the matching .wav?")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("paths", nargs="+", type=Path,
                   help="src .npz and dst .npz; with --find-still, one or more BEAT2 .npz takes to scan")
    p.add_argument("--start", type=float, default=0.0, help="start time, seconds")
    p.add_argument("--end", type=float, default=None, help="end time, seconds (default: clip end)")
    p.add_argument("--up", choices=list(AXES), default=None, help="override detected up axis")
    p.add_argument("--wav", type=Path, default=None, help="matching wave16k .wav to trim alongside")
    p.add_argument("--model-dir", type=Path, default=DEFAULT_MODEL_DIR, help="folder with SMPLX_<GENDER>.npz")
    g = p.add_argument_group("--find-still")
    g.add_argument("--find-still", action="store_true", help="rank windows to convert instead of converting")
    g.add_argument("--window", type=float, default=20.0, help="window length, seconds (default 20)")
    g.add_argument("--max-foot-move", type=float, default=0.10,
                   help="drop windows where either ankle strays farther than this, m (default 0.10)")
    g.add_argument("--top", type=int, default=5, help="how many windows to list (default 5)")
    args = p.parse_args()

    if args.find_still:
        find_still(args.paths, args)
    elif len(args.paths) == 2:
        convert(*args.paths, args)
    else:
        p.error("converting needs exactly two paths: src dst (or pass --find-still to scan takes)")


if __name__ == "__main__":
    main()
