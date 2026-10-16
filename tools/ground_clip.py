"""Shift a GMR robot-motion .pkl so the robot's lowest collision point sits exactly on the floor.

Forward kinematics is run on booster-mjlab's own K1 model (the one training uses),
so the offset is measured, not guessed.

Usage (from ~/projects/booster-mjlab):
    uv run python tools/ground_clip.py <GMR K1 xml> <booster-mjlab K1 xml> <in.pkl> <out.pkl>
"""
import pickle
import sys

import mujoco
import numpy as np

gmr_xml, robot_xml, src, dst = sys.argv[1:5]

with open(src, "rb") as f:
    motion = pickle.load(f)

# GMR's K1 model names a few joints differently from booster-mjlab's.
RENAME = {
    "AAHead_yaw": "Head_Yaw",
    "Head_pitch": "Head_Pitch",
    "ALeft_Shoulder_Pitch": "Left_Shoulder_Pitch",
    "ARight_Shoulder_Pitch": "Right_Shoulder_Pitch",
}

FREE = mujoco.mjtJoint.mjJNT_FREE
JOINT = mujoco.mjtObj.mjOBJ_JOINT


def hinge_names(model):
    return [mujoco.mj_id2name(model, JOINT, j) for j in range(model.njnt) if model.jnt_type[j] != FREE]


# GMR's dof_pos columns follow the joint order of GMR's own K1 model.
gmr = mujoco.MjModel.from_xml_path(gmr_xml)
gmr_joints = hinge_names(gmr)
n_dof = motion["dof_pos"].shape[1]
if len(gmr_joints) != n_dof:
    sys.exit(f"GMR model has {len(gmr_joints)} joints but clip has {n_dof} dof columns")

# Map each GMR joint, by name, onto booster-mjlab's model.
rob = mujoco.MjModel.from_xml_path(robot_xml)
data = mujoco.MjData(rob)
free_ids = [j for j in range(rob.njnt) if rob.jnt_type[j] == FREE]
if not free_ids:
    sys.exit("robot xml has no free joint (floating base)")
root_adr = rob.jnt_qposadr[free_ids[0]]

missing, dof_adr = [], []
for name in gmr_joints:
    jid = mujoco.mj_name2id(rob, JOINT, RENAME.get(name, name))
    if jid < 0:
        missing.append(name)
    else:
        dof_adr.append(rob.jnt_qposadr[jid])
if missing:
    print("Robot xml joints:", hinge_names(rob))
    sys.exit(f"These GMR joints are not in the robot xml: {missing}")

# Collision geoms only (skip visual-only geoms and anything attached to the world, e.g. the floor).
geoms = [
    g for g in range(rob.ngeom)
    if rob.geom_bodyid[g] != 0 and (rob.geom_contype[g] or rob.geom_conaffinity[g])
]

lowest = []
for root_pos, root_xyzw, dof in zip(motion["root_pos"], motion["root_rot"], motion["dof_pos"]):
    data.qpos[:] = rob.qpos0
    data.qpos[root_adr:root_adr + 3] = root_pos
    data.qpos[root_adr + 3:root_adr + 7] = np.asarray(root_xyzw)[[3, 0, 1, 2]]  # GMR saves xyzw; MuJoCo wants wxyz
    data.qpos[dof_adr] = dof
    mujoco.mj_kinematics(rob, data)

    frame_min = np.inf
    for g in geoms:
        z_row = data.geom_xmat[g].reshape(3, 3)[2]          # world-z row of the geom's rotation
        center, half = rob.geom_aabb[g][:3], rob.geom_aabb[g][3:]
        z = data.geom_xpos[g][2] + z_row @ center - np.abs(z_row) @ half
        frame_min = min(frame_min, z)
    lowest.append(frame_min)

lowest = np.array(lowest)
dz = -lowest.min()
print(f"lowest point per frame (m): min {lowest.min():+.4f}  median {np.median(lowest):+.4f}  max {lowest.max():+.4f}")
print(f"shifting root z by {dz:+.4f} m so the lowest point touches the floor")

motion["root_pos"] = np.array(motion["root_pos"], dtype=float)
motion["root_pos"][:, 2] += dz
with open(dst, "wb") as f:
    pickle.dump(motion, f)
print(f"saved -> {dst}")