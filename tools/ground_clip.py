"""Shift GMR robot-motion .pkl clips so the robot's lowest collision point sits exactly on the floor.

Forward kinematics is run on booster-mjlab's own K1 model (the one training uses),
and each collision geom's lowest point is computed exactly from its shape (sphere, capsule,
cylinder, box, ellipsoid, or mesh vertices), so the offset is measured per clip, not guessed.

Each <name>.pkl is written to <name>_grounded.pkl next to it. Clips that are already
grounded (or whose _grounded.pkl is newer than the source) are skipped.

Usage (from ~/projects/booster-mjlab):
    uv run python tools/ground_clip.py ~/robotics/data/k1_motions            # every clip in a folder
    uv run python tools/ground_clip.py clip_a.pkl clip_b.pkl                 # specific clips
    uv run python tools/ground_clip.py ~/robotics/data/k1_motions --upload   # also upload-motion each one
"""
import argparse
import os
import pickle
import subprocess
import sys
from pathlib import Path

import mujoco
import numpy as np

REPO = Path(__file__).resolve().parents[1]
DEFAULT_GMR_XML = Path.home() / "projects/GMR/assets/booster_k1/K1_serial.xml"
DEFAULT_ROBOT_XML = REPO / "src/booster_mjlab/robots/booster_k1/xmls/k1.xml"
SUFFIX = "_grounded"

# GMR's K1 model names a few joints differently from booster-mjlab's.
RENAME = {
    "AAHead_yaw": "Head_Yaw",
    "Head_pitch": "Head_Pitch",
    "ALeft_Shoulder_Pitch": "Left_Shoulder_Pitch",
    "ARight_Shoulder_Pitch": "Right_Shoulder_Pitch",
}

FREE = mujoco.mjtJoint.mjJNT_FREE
JOINT = mujoco.mjtObj.mjOBJ_JOINT
GEOM = mujoco.mjtObj.mjOBJ_GEOM
BODY = mujoco.mjtObj.mjOBJ_BODY
G = mujoco.mjtGeom


def hinge_names(model):
    return [mujoco.mj_id2name(model, JOINT, j) for j in range(model.njnt) if model.jnt_type[j] != FREE]


class Grounder:
    def __init__(self, gmr_xml, robot_xml):
        # GMR's dof_pos columns follow the joint order of GMR's own K1 model.
        self.gmr_joints = hinge_names(mujoco.MjModel.from_xml_path(str(gmr_xml)))

        # Map each GMR joint, by name, onto booster-mjlab's model.
        rob = mujoco.MjModel.from_xml_path(str(robot_xml))
        free_ids = [j for j in range(rob.njnt) if rob.jnt_type[j] == FREE]
        if not free_ids:
            sys.exit("robot xml has no free joint (floating base)")
        self.root_adr = rob.jnt_qposadr[free_ids[0]]

        missing, self.dof_adr = [], []
        for name in self.gmr_joints:
            jid = mujoco.mj_name2id(rob, JOINT, RENAME.get(name, name))
            if jid < 0:
                missing.append(name)
            else:
                self.dof_adr.append(rob.jnt_qposadr[jid])
        if missing:
            print("Robot xml joints:", hinge_names(rob))
            sys.exit(f"These GMR joints are not in the robot xml: {missing}")

        # Collision geoms only (skip visual-only geoms and anything attached to the world, e.g. the floor).
        self.geoms = [
            g for g in range(rob.ngeom)
            if rob.geom_bodyid[g] != 0 and (rob.geom_contype[g] or rob.geom_conaffinity[g])
        ]
        self.rob, self.data = rob, mujoco.MjData(rob)

    def lowest_per_frame(self, motion):
        n_dof = motion["dof_pos"].shape[1]
        if len(self.gmr_joints) != n_dof:
            raise ValueError(f"GMR model has {len(self.gmr_joints)} joints but clip has {n_dof} dof columns")

        rob, data = self.rob, self.data
        lowest, lowest_geom = [], []
        for root_pos, root_xyzw, dof in zip(motion["root_pos"], motion["root_rot"], motion["dof_pos"]):
            data.qpos[:] = rob.qpos0
            data.qpos[self.root_adr:self.root_adr + 3] = root_pos
            data.qpos[self.root_adr + 3:self.root_adr + 7] = np.asarray(root_xyzw)[[3, 0, 1, 2]]  # GMR saves xyzw; MuJoCo wants wxyz
            data.qpos[self.dof_adr] = dof
            mujoco.mj_kinematics(rob, data)

            zs = [self.geom_lowest_z(g) for g in self.geoms]
            i = int(np.argmin(zs))
            lowest.append(zs[i])
            lowest_geom.append(self.geoms[i])
        return np.array(lowest), lowest_geom

    def geom_lowest_z(self, g):
        """Exact lowest world z of collision geom g in the current pose.

        A bounding box overestimates this when the part is tilted (up to ~1 cm on fast clips),
        so each shape is handled exactly.
        """
        rob, data = self.rob, self.data
        z0 = data.geom_xpos[g][2]
        r = data.geom_xmat[g].reshape(3, 3)[2]  # world-z row: z of local point p is z0 + r @ p
        s, t = rob.geom_size[g], rob.geom_type[g]
        if t == G.mjGEOM_SPHERE:
            return z0 - s[0]
        if t == G.mjGEOM_CAPSULE:                # radius s0, half-length s1 along local z
            return z0 - abs(r[2]) * s[1] - s[0]
        if t == G.mjGEOM_CYLINDER:               # radius s0, half-length s1 along local z
            return z0 - abs(r[2]) * s[1] - s[0] * np.sqrt(max(0.0, 1.0 - r[2] ** 2))
        if t == G.mjGEOM_BOX:
            return z0 - np.abs(r) @ s
        if t == G.mjGEOM_ELLIPSOID:
            return z0 - np.sqrt(np.sum((r * s) ** 2))
        if t == G.mjGEOM_MESH:                   # MuJoCo collides with the convex hull; its lowest point is a vertex
            m = rob.geom_dataid[g]
            a, n = rob.mesh_vertadr[m], rob.mesh_vertnum[m]
            return z0 + np.min(rob.mesh_vert[a:a + n] @ r)
        return np.inf                            # planes, height fields, etc. are not robot parts

    def ground(self, src, dst):
        with open(src, "rb") as f:
            motion = pickle.load(f)
        lowest, lowest_geom = self.lowest_per_frame(motion)
        k = int(np.argmin(lowest))
        g = lowest_geom[k]
        gname = mujoco.mj_id2name(self.rob, GEOM, g) or f"geom {g}"
        bname = mujoco.mj_id2name(self.rob, BODY, self.rob.geom_bodyid[g])
        dz = -lowest[k]
        print(f"  lowest point per frame (m): min {lowest.min():+.4f}  median {np.median(lowest):+.4f}  max {lowest.max():+.4f}")
        print(f"  lowest geom: {gname} on {bname} (frame {k})")
        print(f"  shifting root z by {dz:+.4f} m")

        motion["root_pos"] = np.array(motion["root_pos"], dtype=float)
        motion["root_pos"][:, 2] += dz
        with open(dst, "wb") as f:
            pickle.dump(motion, f)
        print(f"  saved -> {dst}")


def collect(paths):
    """Expand folders into their .pkl clips, skipping outputs of this script."""
    clips = []
    for p in map(Path, paths):
        if p.is_dir():
            clips += sorted(c for c in p.glob("*.pkl") if not c.stem.endswith(SUFFIX))
        elif p.stem.endswith(SUFFIX):
            print(f"skip {p.name}: already a grounded clip")
        else:
            clips.append(p)
    return clips


def upload(clip, entity):
    # Name the artifact after the original clip, so re-uploading a fixed clip bumps
    # e.g. wave_000508-tracking:v0 -> :v1 instead of creating wave_000508_grounded-tracking.
    name = clip.stem.removesuffix(SUFFIX) + "-tracking"
    cmd = ["upload-motion", "--input-file", str(clip), "--artifact-name", name]
    if entity:
        cmd += ["--entity", entity]
    print("  $", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help=".pkl clips and/or folders of them")
    ap.add_argument("--gmr-xml", type=Path, default=DEFAULT_GMR_XML, help="K1 model GMR retargeted with")
    ap.add_argument("--robot-xml", type=Path, default=DEFAULT_ROBOT_XML, help="K1 model training uses")
    ap.add_argument("--force", action="store_true", help="re-ground even if an up-to-date _grounded.pkl exists")
    ap.add_argument("--upload", action="store_true", help="run upload-motion on each newly grounded clip")
    ap.add_argument("--entity", default=os.environ.get("WANDB_ENTITY"), help="WandB entity (default: $WANDB_ENTITY)")
    args = ap.parse_args()

    clips = collect(args.paths)
    if not clips:
        sys.exit("no clips found")
    grounder = Grounder(args.gmr_xml, args.robot_xml)

    done, skipped, failed = [], [], []
    for src in clips:
        dst = src.with_name(src.stem + SUFFIX + ".pkl")
        if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime and not args.force:
            skipped.append(src.name)
            continue
        print(f"{src.name}")
        try:
            grounder.ground(src, dst)
            if args.upload:
                upload(dst, args.entity)
            done.append(src.name)
        except Exception as e:  # keep going so one bad clip doesn't stop the batch
            print(f"  FAILED: {e}")
            failed.append(src.name)

    print(f"\ngrounded {len(done)}, skipped {len(skipped)} (already up to date), failed {len(failed)}")
    if skipped:
        print("  skipped:", ", ".join(skipped), "(use --force to redo)")
    if failed:
        print("  failed:", ", ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
