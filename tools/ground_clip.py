"""Shift GMR robot-motion .pkl clips so the robot's lowest collision point sits exactly on the floor.

Forward kinematics is run on booster-mjlab's own K1 model (the one training uses),
and each collision geom's lowest point is computed exactly from its shape (sphere, capsule,
cylinder, box, ellipsoid, or mesh vertices), so the offset is measured per clip, not guessed.

Before grounding, feet that are on the floor are flattened: ankle pitch/roll are re-solved so
each sole is level. After grounding, a flat foot can still hover (often on a straight leg, which
can't reach further), so the trunk is lowered by one constant amount for the clip and leg IK
puts each foot back on the floor by bending its knee. GMR copies the human's foot angle, which leaves K1 standing on foot edges
(6-9 deg on wave_000508); a policy trained on that learns to roll its ankle. Feet in the air are
left alone, with a smooth blend in between. Disable with --keep-foot-tilt.

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

# (foot body, collision geom, ankle pitch joint, ankle roll joint). GMR uses the same ankle names.
FEET = {
    "left": ("left_foot_link", "left_foot_collision", "Left_Ankle_Pitch", "Left_Ankle_Roll"),
    "right": ("right_foot_link", "right_foot_collision", "Right_Ankle_Pitch", "Right_Ankle_Roll"),
}
# A foot whose lowest point is within STANCE_LO of the floor gets fully flattened, above STANCE_HI
# it is left as is, and in between the correction is blended so swing feet don't snap.
STANCE_LO, STANCE_HI = 0.015, 0.04
# Extra trunk drop so no stance knee ends up fully straight: near full extension a tiny foot height
# change needs a large knee angle change, which turns mm-level differences into knee jitter.
KNEE_MARGIN = 0.003
LEG_JOINTS = ("Hip_Pitch", "Hip_Roll", "Hip_Yaw", "Knee_Pitch", "Ankle_Pitch", "Ankle_Roll")

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

        # Soles are level in the zero pose, so a foot is flat when its zero-pose "up" points up.
        data = self.data
        data.qpos[:] = rob.qpos0
        mujoco.mj_kinematics(rob, data)
        self.feet = {}
        for side, (body, geom, pitch, roll) in FEET.items():
            b = mujoco.mj_name2id(rob, BODY, body)
            jp, jr = (mujoco.mj_name2id(rob, JOINT, j) for j in (pitch, roll))
            self.feet[side] = dict(
                body=b,
                geom=mujoco.mj_name2id(rob, GEOM, geom),
                cols=[self.gmr_joints.index(pitch), self.gmr_joints.index(roll)],  # dof_pos columns
                adr=[rob.jnt_qposadr[jp], rob.jnt_qposadr[jr]],
                lo=rob.jnt_range[[jp, jr], 0],
                hi=rob.jnt_range[[jp, jr], 1],
                up_local=data.xmat[b].reshape(3, 3).T @ np.array([0.0, 0.0, 1.0]),
                leg_cols=[self.gmr_joints.index(f"{side.title()}_{j}") for j in LEG_JOINTS],
            )
            leg_ids = [mujoco.mj_name2id(rob, JOINT, f"{side.title()}_{j}") for j in LEG_JOINTS]
            self.feet[side].update(
                leg_adr=list(rob.jnt_qposadr[leg_ids]), leg_lo=rob.jnt_range[leg_ids, 0], leg_hi=rob.jnt_range[leg_ids, 1]
            )

    def set_pose(self, root_pos, root_xyzw, dof):
        data = self.data
        data.qpos[:] = self.rob.qpos0
        data.qpos[self.root_adr:self.root_adr + 3] = root_pos
        data.qpos[self.root_adr + 3:self.root_adr + 7] = np.asarray(root_xyzw)[[3, 0, 1, 2]]  # GMR saves xyzw; MuJoCo wants wxyz
        data.qpos[self.dof_adr] = dof
        mujoco.mj_kinematics(self.rob, data)

    def sole_normal(self, foot):
        return self.data.xmat[foot["body"]].reshape(3, 3) @ foot["up_local"]

    def tilt_deg(self, foot):
        return np.degrees(np.arccos(np.clip(self.sole_normal(foot)[2], -1.0, 1.0)))

    def solve_flat(self, foot):
        """Ankle (pitch, roll) that levels the sole in the current pose (Newton, finite-difference Jacobian)."""
        rob, data = self.rob, self.data
        q = data.qpos[foot["adr"]].copy()

        def residual(x):
            data.qpos[foot["adr"]] = x
            mujoco.mj_kinematics(rob, data)
            return self.sole_normal(foot)[:2]  # level sole <=> normal has no x/y component

        for _ in range(20):
            f = residual(q)
            if np.abs(f).max() < 1e-6:
                break
            eps = 1e-6
            J = np.column_stack([(residual(q + eps * e) - f) / eps for e in np.eye(2)])
            q = q - np.linalg.lstsq(J, f, rcond=None)[0]
        return q

    def solve_leg(self, foot, target_pos, target_quat, q0=None):
        """Leg joints that put the foot body at target_pos / target_quat (Newton, finite-difference Jacobian).

        Near a straight knee there are several solutions, so start from q0 (the previous frame's answer)
        to stay on the same one over time and avoid jitter.
        """
        rob, data = self.rob, self.data
        if q0 is None:
            q = data.qpos[foot["leg_adr"]].copy()
            knee = LEG_JOINTS.index("Knee_Pitch")
            q[knee] = max(q[knee], 0.05)  # start bent so we don't find the backwards-knee solution
        else:
            q = q0.copy()
        err = np.zeros(3)

        def residual(x):
            data.qpos[foot["leg_adr"]] = x
            mujoco.mj_kinematics(rob, data)
            mujoco.mju_subQuat(err, target_quat, data.xquat[foot["body"]])
            return np.concatenate([target_pos - data.xpos[foot["body"]], err])

        for _ in range(50):
            f = residual(q)
            if np.abs(f).max() < 1e-7:
                break
            eps = 1e-6
            J = np.column_stack([(residual(q + eps * e) - f) / eps for e in np.eye(len(q))])
            step = np.linalg.solve(J.T @ J + 1e-4 * np.eye(len(q)), J.T @ f)  # damped: stays sane near a straight knee
            q = np.clip(q - np.clip(step, -0.1, 0.1), foot["leg_lo"], foot["leg_hi"])
        return q, np.abs(residual(q)).max()

    def stance_weights(self, heights):
        floor = min(v.min() for v in heights.values())
        return {side: np.clip((STANCE_HI - (v - floor)) / (STANCE_HI - STANCE_LO), 0.0, 1.0) for side, v in heights.items()}

    def plant_feet(self, motion):
        """Put every (already flat) foot that is near the floor onto it.

        Lower the trunk by the clip's largest hover (plus KNEE_MARGIN), the same amount every frame,
        then use leg IK to put each foot at its target height (its own hover removed, scaled by its
        stance weight). Lowering the trunk means the IK only ever has to lift a foot, i.e. bend a
        knee, which is always reachable. A constant drop keeps the knee angles smooth over time.
        """
        heights = self.foot_heights(motion)
        weights = self.stance_weights(heights)
        root_pos = np.array(motion["root_pos"], dtype=float)
        dof_pos = np.array(motion["dof_pos"], dtype=float)
        drop = {side: weights[side] * np.maximum(heights[side], 0.0) for side in self.feet}
        d = max(v.max() for v in drop.values()) + KNEE_MARGIN
        failed = 0
        prev = {side: None for side in self.feet}  # warm start from the previous frame
        for t, root_xyzw in enumerate(motion["root_rot"]):
            self.set_pose(root_pos[t], root_xyzw, dof_pos[t])
            targets = {
                side: (self.data.xpos[f["body"]] - [0.0, 0.0, drop[side][t]], self.data.xquat[f["body"]].copy())
                for side, f in self.feet.items()
            }
            new_root = root_pos[t] - [0.0, 0.0, d]
            new_dof = dof_pos[t].copy()
            ok, solved = True, {}
            for side, foot in self.feet.items():
                self.set_pose(new_root, root_xyzw, new_dof)
                q, err = self.solve_leg(foot, *targets[side], q0=prev[side])
                ok &= err < 1e-5 and np.all(q >= foot["leg_lo"]) and np.all(q <= foot["leg_hi"])
                new_dof[foot["leg_cols"]] = solved[side] = q
            if ok:
                root_pos[t], dof_pos[t] = new_root, new_dof
                prev = solved
            else:
                failed += 1  # keep this frame as it was rather than write a bad pose
                prev = {side: None for side in self.feet}
        motion["root_pos"], motion["dof_pos"] = root_pos, dof_pos
        print(f"  planted feet: trunk lowered by {d * 1000:.1f} mm"
              + (f" | IK failed on {failed} frames (left unchanged)" if failed else ""))

    def foot_heights(self, motion):
        """Lowest world z of each foot, per frame."""
        h = {side: [] for side in self.feet}
        for frame in zip(motion["root_pos"], motion["root_rot"], motion["dof_pos"]):
            self.set_pose(*frame)
            for side, foot in self.feet.items():
                h[side].append(self.geom_lowest_z(foot["geom"]))
        return {side: np.array(v) for side, v in h.items()}

    def flatten_feet(self, motion):
        weights = self.stance_weights(self.foot_heights(motion))
        dof_pos = np.array(motion["dof_pos"], dtype=float)
        report = {side: dict(before=[], after=[], change=[], clamped=0, stance=0) for side in self.feet}

        for t, (root_pos, root_xyzw) in enumerate(zip(motion["root_pos"], motion["root_rot"])):
            for side, foot in self.feet.items():
                w = weights[side][t]
                self.set_pose(root_pos, root_xyzw, dof_pos[t])
                rep = report[side]
                rep["before"].append(self.tilt_deg(foot))
                if w > 0:
                    old = dof_pos[t, foot["cols"]].copy()
                    new = old + w * (self.solve_flat(foot) - old)
                    clipped = np.clip(new, foot["lo"], foot["hi"])
                    rep["clamped"] += int(np.any(clipped != new))
                    rep["stance"] += int(w == 1.0)
                    rep["change"].append(np.degrees(np.abs(clipped - old)).max())
                    dof_pos[t, foot["cols"]] = clipped
                    self.set_pose(root_pos, root_xyzw, dof_pos[t])
                rep["after"].append(self.tilt_deg(foot))

        motion["dof_pos"] = dof_pos
        n = len(dof_pos)
        for side, rep in report.items():
            change = max(rep["change"], default=0.0)
            print(f"  {side} foot tilt (deg): mean {np.mean(rep['before']):.1f} max {np.max(rep['before']):.1f}"
                  f" -> mean {np.mean(rep['after']):.1f} max {np.max(rep['after']):.1f}"
                  f" | on floor {rep['stance']}/{n} frames | max ankle change {change:.1f} deg"
                  + (f" | {rep['clamped']} frames hit joint limits" if rep["clamped"] else ""))

    def lowest_per_frame(self, motion):
        n_dof = motion["dof_pos"].shape[1]
        if len(self.gmr_joints) != n_dof:
            raise ValueError(f"GMR model has {len(self.gmr_joints)} joints but clip has {n_dof} dof columns")

        lowest, lowest_geom = [], []
        for frame in zip(motion["root_pos"], motion["root_rot"], motion["dof_pos"]):
            self.set_pose(*frame)
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

    def ground(self, src, dst, flatten=True):
        with open(src, "rb") as f:
            motion = pickle.load(f)
        if flatten:
            self.flatten_feet(motion)
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
        if flatten:
            self.plant_feet(motion)
        gaps = self.foot_heights(motion)
        print("  foot gap to floor (mm): " + "  ".join(
            f"{side} median {np.median(v) * 1000:.1f} max {v.max() * 1000:.1f}" for side, v in gaps.items()))
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
    ap.add_argument("--keep-foot-tilt", action="store_true", help="don't flatten feet that are on the floor")
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
            grounder.ground(src, dst, flatten=not args.keep_foot_tilt)
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
