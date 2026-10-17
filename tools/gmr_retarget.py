"""Retarget AMASS-style SMPL-X .npz clips (e.g. from beat2_to_gmr.py) to the K1 with GMR, without the viewer.

Same as GMR's `scripts/smplx_to_robot.py --robot booster_k1 --save_path ...` (same loader, 30 fps
alignment, IK, and .pkl format), minus the MuJoCo viewer, so it runs headless and in batches. Two
differences, both about the first frame:
- smplx_to_robot never solves frame 0 (its loop increments before use), so its clips start one frame
  late. Here frame 0 is kept, so the motion stays aligned with the window's trimmed audio.
- GMR's IK runs at most 10 iterations per frame, warm-started from the previous frame. The first
  frame has no previous frame, so it is solved WARMUP_ROUNDS times before anything is recorded,
  starting from the K1's arms-down standing pose (ARMS_DOWN) instead of GMR's zero pose (a T-pose).
  From the T-pose, frame 0 can settle with an arm swung behind the body (e.g. left shoulder pitch at
  its +70 deg limit) and the warm start then keeps it there for the whole clip: 20/152 BEAT2 clips had
  the K1's left hand behind the trunk while the human's was in front (notes/log.md, 2026-10-16).

Must run with GMR's venv (GMR, smplx, mink are installed there):
    ~/projects/GMR/.venv/bin/python tools/gmr_retarget.py in_a.npz out_a.pkl [in_b.npz out_b.pkl ...]
"""
import os
import pickle
import sys
import time
from pathlib import Path

import mujoco
import numpy as np

from general_motion_retargeting import GeneralMotionRetargeting as GMR
from general_motion_retargeting.utils.smpl import get_smplx_data_offline_fast, load_smplx_file

GMR_ROOT = Path.home() / "projects/GMR"
SMPLX_FOLDER = GMR_ROOT / "assets" / "body_models"
ROBOT = "booster_k1"
TGT_FPS = 30  # what smplx_to_robot uses
WARMUP_ROUNDS = 5
# booster_mjlab's HOME_KEYFRAME arm joints (k1_constants.py); same names in GMR's K1_serial.xml.
ARMS_DOWN = {"Left_Shoulder_Roll": -1.4, "Left_Elbow_Yaw": -0.4, "Right_Shoulder_Roll": 1.4, "Right_Elbow_Yaw": 0.4}


def retarget_clip(src: Path, dst: Path) -> None:
    smplx_data, body_model, smplx_output, human_height = load_smplx_file(str(src), SMPLX_FOLDER)
    frames, fps = get_smplx_data_offline_fast(smplx_data, body_model, smplx_output, tgt_fps=TGT_FPS)
    retarget = GMR(actual_human_height=human_height, src_human="smplx", tgt_robot=ROBOT)
    model, q = retarget.configuration.model, retarget.configuration.q.copy()
    for name, value in ARMS_DOWN.items():
        q[model.jnt_qposadr[mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, name)]] = value
    retarget.configuration.update(q)
    for _ in range(WARMUP_ROUNDS):
        retarget.retarget(frames[0])
    qpos = np.array([retarget.retarget(f) for f in frames])
    motion = {
        "fps": fps,
        "root_pos": qpos[:, :3],
        "root_rot": qpos[:, [4, 5, 6, 3]],  # GMR's qpos is wxyz; its .pkl format is xyzw
        "dof_pos": qpos[:, 7:],
        "local_body_pos": None,
        "link_body_list": None,
    }
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_name(dst.name + ".tmp")  # rename when complete: an interrupted run never leaves a half-written .pkl
    with open(tmp, "wb") as f:
        pickle.dump(motion, f)
    os.replace(tmp, dst)


def main() -> None:
    args = sys.argv[1:]
    if not args or len(args) % 2:
        sys.exit(__doc__)
    pairs = [(Path(a), Path(b)) for a, b in zip(args[::2], args[1::2])]
    for i, (src, dst) in enumerate(pairs, 1):
        t0 = time.time()
        retarget_clip(src, dst)
        print(f"[gmr {i}/{len(pairs)}] {src.name} -> {dst.name} ({time.time() - t0:.1f} s)", flush=True)


if __name__ == "__main__":
    main()
