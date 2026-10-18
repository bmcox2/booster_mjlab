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

Optional ``--ik-config PATH``: use this IK config instead of GMR's ``smplx_to_k1.json``, e.g.
``tools/ik_configs/smplx_to_k1_torso.json`` (the K1 trunk follows the human's lower spine instead of the
pelvis; see that file's entry in notes/log.md). GMR's K1 model has no body at the forearm tip (its
``*_hand_link`` starts at the elbow), so with a custom config the model also gets two massless bodies,
``left_hand_end`` / ``right_hand_end``, 0.203 m down the forearm (booster's ``*_hand_end_ball``), usable
as IK targets. They add no joints, so the .pkl columns are unchanged. GMR's files are not edited.

Must run with GMR's venv (GMR, smplx, mink are installed there):
    ~/projects/GMR/.venv/bin/python tools/gmr_retarget.py [--ik-config cfg.json] in_a.npz out_a.pkl [in_b.npz out_b.pkl ...]
"""
import os
import pickle
import sys
import tempfile
import time
from pathlib import Path

import mujoco
import numpy as np
from scipy.spatial.transform import Rotation

from general_motion_retargeting import GeneralMotionRetargeting as GMR
from general_motion_retargeting import params as gmr_params
from general_motion_retargeting.utils.smpl import get_smplx_data_offline_fast, load_smplx_file

GMR_ROOT = Path.home() / "projects/GMR"
SMPLX_FOLDER = GMR_ROOT / "assets" / "body_models"
ROBOT = "booster_k1"
TGT_FPS = 30  # what smplx_to_robot uses
WARMUP_ROUNDS = 5
# booster_mjlab's HOME_KEYFRAME arm joints (k1_constants.py); same names in GMR's K1_serial.xml.
ARMS_DOWN = {"Left_Shoulder_Roll": -1.4, "Left_Elbow_Yaw": -0.4, "Right_Shoulder_Roll": 1.4, "Right_Elbow_Yaw": 0.4}
# Forearm tips, in the *_hand_link frame (booster_mjlab k1.xml: *_hand_end_ball).
HAND_ENDS = {"left_hand_link": ("left_hand_end", (0, 0.203, 0)), "right_hand_link": ("right_hand_end", (0, -0.203, 0))}


def use_ik_config(ik_config: Path) -> None:
    """Point GMR at a custom K1 IK config and a K1 model with forearm-tip bodies (written to the temp dir)."""
    src = Path(gmr_params.ROBOT_XML_DICT[ROBOT])
    spec = mujoco.MjSpec.from_file(str(src))
    spec.meshdir = str(src.parent / spec.meshdir)  # absolute, so the copy can live anywhere
    for parent, (name, pos) in HAND_ENDS.items():
        spec.body(parent).add_body(name=name, pos=pos)
    xml = Path(tempfile.gettempdir()) / f"gmr_{ik_config.stem}_K1_serial.xml"
    xml.write_text(spec.to_xml())
    gmr_params.ROBOT_XML_DICT[ROBOT] = xml
    gmr_params.IK_CONFIG_DICT["smplx"][ROBOT] = ik_config


def retarget_clip(src: Path, dst: Path) -> None:
    smplx_data, body_model, smplx_output, human_height = load_smplx_file(str(src), SMPLX_FOLDER)
    frames, fps = get_smplx_data_offline_fast(smplx_data, body_model, smplx_output, tgt_fps=TGT_FPS)
    retarget = GMR(actual_human_height=human_height, src_human="smplx", tgt_robot=ROBOT)
    # GMR offsets every human body in its scale table by its table-1 offset, but only stores offsets for
    # bodies with a table-1 task: a body used only in table 2 (a wrist) or no longer used (the pelvis, when
    # the trunk follows the spine) would KeyError. Neutral offsets for those. No-op for GMR's own config.
    for body in retarget.human_scale_table:
        retarget.pos_offsets1.setdefault(body, np.zeros(3))
        retarget.rot_offsets1.setdefault(body, Rotation.identity())
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
    if args[:1] == ["--ik-config"]:
        use_ik_config(Path(args[1]).resolve())
        args = args[2:]
    if not args or len(args) % 2:
        sys.exit(__doc__)
    pairs = [(Path(a), Path(b)) for a, b in zip(args[::2], args[1::2])]
    for i, (src, dst) in enumerate(pairs, 1):
        t0 = time.time()
        retarget_clip(src, dst)
        print(f"[gmr {i}/{len(pairs)}] {src.name} -> {dst.name} ({time.time() - t0:.1f} s)", flush=True)


if __name__ == "__main__":
    main()
