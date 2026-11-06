"""Export clips of a combined motion .npz as one file each, for the robot's deploy task.

booster_deploy's tasks play one clip per file. Each file has the usual arrays (fps, joint_pos, joint_vel,
body_pos_w, body_quat_w, body_lin_vel_w, body_ang_vel_w), plus joint_names and body_names, so the deploy
task can check the order it reads them in instead of assuming it.

Usage (from ~/projects/booster-mjlab):
    uv run python tools/export_deploy_clip.py ~/robotics/data/beat2_full_torso/combined/beat2-full-torso-heldout-val.npz \\
        --clips nidal_0_13_13_t18-36 --out-dir ../booster_deploy/tasks/gesture_tracking/motions
"""
from __future__ import annotations

import argparse
from pathlib import Path

import mujoco
import numpy as np

K1_XML = Path(__file__).resolve().parents[1] / "src/booster_mjlab/robots/booster_k1/xmls/k1.xml"
ARRAYS = ("joint_pos", "joint_vel", "body_pos_w", "body_quat_w", "body_lin_vel_w", "body_ang_vel_w")


def k1_names() -> tuple[list[str], list[str]]:
    """Joint and body names in motion-file order: model order, without the floating base and the world."""
    model = mujoco.MjModel.from_xml_path(str(K1_XML))
    joints = [model.joint(j).name for j in range(1, model.njnt)]
    bodies = [model.body(b).name for b in range(1, model.nbody)]
    return joints, bodies


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("motion_file", type=Path)
    parser.add_argument("--clips", nargs="+", required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    joints, bodies = k1_names()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    with np.load(args.motion_file, allow_pickle=False) as data:
        names = [str(n) for n in data["clip_names"]]
        starts = np.concatenate([[0], np.cumsum(data["clip_lengths"])])
        missing = [c for c in args.clips if c not in names]
        if missing:
            raise SystemExit(f"not in {args.motion_file.name}: {missing}")
        arrays = {key: data[key] for key in ARRAYS}
        if arrays["joint_pos"].shape[1] != len(joints) or arrays["body_pos_w"].shape[1] != len(bodies):
            raise SystemExit(f"{args.motion_file.name} doesn't have the K1's {len(joints)} joints and {len(bodies)} bodies")
        for clip in args.clips:
            i = names.index(clip)
            s, e = int(starts[i]), int(starts[i + 1])
            out = args.out_dir / f"{clip}.npz"
            np.savez(out, fps=data["fps"], joint_names=np.array(joints), body_names=np.array(bodies),
                     **{key: value[s:e] for key, value in arrays.items()})
            print(f"{out} ({(e - s) / float(np.asarray(data['fps']).reshape(-1)[0]):.1f} s)")


if __name__ == "__main__":
    main()
