"""Write the golden file that keeps booster_deploy's gesture task equal to this repo's deploy code.

tests/test_deploy.py checks booster_mjlab.deploy against mjlab's real observation. This file carries that
check across repos: seeded robot states, reference frames and a lead-in, with what booster_mjlab.deploy
makes of them. booster_deploy's tests/test_gesture_tracking.py compares its torch port to these numbers.
Rerun it if the deploy code changes.

Usage (from ~/projects/booster-mjlab):
    uv run python tools/make_deploy_golden.py ../booster_deploy/tests/data/gesture_tracking_golden.npz
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

import booster_mjlab.tasks  # noqa: F401, ensure task registry is populated.
from booster_mjlab.deploy import RefFrame, Reference, RobotState, build_observation

NAMES = ["command", "motion_anchor_ori_b", "base_ang_vel", "joint_pos", "joint_vel", "actions", "projected_gravity"]
DIMS = [44, 6, 3, 22, 22, 22, 3]
J = 22


def unit(q: np.ndarray) -> np.ndarray:
    return q / np.linalg.norm(q)


def main() -> None:
    out = Path(sys.argv[1])
    rng = np.random.default_rng(0)
    default = rng.uniform(-1, 1, J)

    obs_in: dict[str, list[np.ndarray]] = {k: [] for k in ("joint_pos", "joint_vel", "root_quat", "gyro", "ref_pos",
                                                            "ref_vel", "ref_quat", "last_action")}
    expected = []
    for _ in range(20):
        v = {"joint_pos": rng.uniform(-2, 2, J), "joint_vel": rng.uniform(-5, 5, J),
             "root_quat": unit(rng.normal(size=4)), "gyro": rng.uniform(-2, 2, 3), "ref_pos": rng.uniform(-2, 2, J),
             "ref_vel": rng.uniform(-5, 5, J), "ref_quat": unit(rng.normal(size=4)), "last_action": rng.uniform(-3, 3, J)}
        for k, value in v.items():
            obs_in[k].append(value)
        state = RobotState(v["joint_pos"], v["joint_vel"], v["root_quat"], v["gyro"])
        expected.append(build_observation(NAMES, DIMS, state, RefFrame(v["ref_pos"], v["ref_vel"], v["ref_quat"]),
                                          v["last_action"], default))

    # A short clip with a heading and a trunk tilt, led in from a different pose.
    frames, fps = 30, 50.0
    clip = Reference(rng.uniform(-1, 1, (frames, J)), rng.uniform(-3, 3, (frames, J)),
                     np.stack([unit(rng.normal(scale=0.1, size=4) + [0.7, 0, 0, -0.7]) for _ in range(frames)]), fps)
    start, robot_quat = rng.uniform(-1, 1, J), unit(np.array([0.9, 0.02, -0.03, 0.4]))
    blend_s, hold_start_s, hold_end_s = 0.5, 0.2, 0.3
    ref = clip.with_lead_in(start, blend_s, hold_start_s).with_end_hold(hold_end_s).aligned_to(robot_quat)

    out.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        out, names=np.array(NAMES), default_joint_pos=default, expected_obs=np.stack(expected),
        **{f"in_{k}": np.stack(v) for k, v in obs_in.items()},
        clip_joint_pos=clip.joint_pos, clip_joint_vel=clip.joint_vel, clip_anchor_quat=clip.anchor_quat, fps=fps,
        start_joint_pos=start, robot_quat=robot_quat, blend_s=blend_s, hold_start_s=hold_start_s, hold_end_s=hold_end_s,
        ref_joint_pos=ref.joint_pos, ref_joint_vel=ref.joint_vel, ref_anchor_quat=ref.anchor_quat,
        clip_start=ref.clip_start, clip_end=ref.clip_end,
    )
    print(f"{out}: {len(expected)} observations, reference of {len(ref)} frames")


if __name__ == "__main__":
    main()
