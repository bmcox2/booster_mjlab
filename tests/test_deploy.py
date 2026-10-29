"""The deploy code (booster_mjlab.deploy) builds the same observation mjlab feeds the policy.

If these drift apart, sim2sim and the robot would run the policy on inputs it was never trained on.
Runs on CPU with the 2-clip waves file (logs/motions/waves_2clip.npz), like test_multi_motion.py.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest
import torch

import booster_mjlab.tasks  # noqa: F401
from booster_mjlab.deploy import RefFrame, Reference, RobotState, build_observation
from booster_mjlab.deploy import observation as ob
from mjlab.envs import ManagerBasedRlEnv
from mjlab.tasks.registry import load_env_cfg

TASK = "Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation"
MOTION = Path(__file__).resolve().parents[1] / "logs" / "motions" / "waves_2clip.npz"

pytestmark = pytest.mark.skipif(not MOTION.exists(), reason=f"needs {MOTION}")


@pytest.fixture(scope="module")
def env():
    cfg = load_env_cfg(TASK, play=True)  # play: no observation noise, so the obs is exact
    cfg.scene.num_envs = 4
    cfg.commands["motion"].motion_file = str(MOTION)
    cfg.commands["motion"].sampling_mode = "uniform"  # mid-clip frames, moving reference
    e = ManagerBasedRlEnv(cfg=cfg, device="cpu")
    e.reset()
    yield e
    e.close()


def test_observation_matches_mjlab(env):
    torch.manual_seed(0)
    obs_mgr = env.observation_manager
    names = obs_mgr.active_terms["actor"]
    dims = [int(np.prod(d)) for d in obs_mgr.group_obs_term_dim["actor"]]
    robot = env.scene["robot"]
    cmd = env.command_manager.get_term("motion")
    default = robot.data.default_joint_pos[0].numpy()
    for _ in range(5):
        env.step(0.3 * torch.randn(env.num_envs, env.action_manager.total_action_dim))
        expected = obs_mgr.compute_group("actor")
        for i in range(env.num_envs):
            state = RobotState(
                joint_pos=robot.data.joint_pos_biased[i].numpy(),  # the encoder reading (with its bias)
                joint_vel=robot.data.joint_vel[i].numpy(),
                trunk_quat=robot.data.root_link_quat_w[i].numpy(),
                gyro=env.scene["robot/imu_ang_vel"].data[i].numpy() if "robot/imu_ang_vel" in env.scene.sensors
                else robot.data.root_link_ang_vel_b[i].numpy(),
            )
            ref = RefFrame(cmd.joint_pos[i].numpy(), cmd.joint_vel[i].numpy(), cmd.anchor_quat_w[i].numpy())
            got = build_observation(names, dims, state, ref, env.action_manager.action[i].numpy(), default)
            np.testing.assert_allclose(got, expected[i].numpy(), atol=1e-5, err_msg=f"env {i}")


def test_reference_lead_in_and_alignment():
    ref = Reference.from_npz(MOTION)
    start = np.zeros(ref.joint_pos.shape[1])
    led = ref.with_lead_in(start, blend_s=1.0, hold_s=0.5).with_end_hold(1.0)
    n_lead = round(1.5 * ref.fps)
    assert len(led) == len(ref) + n_lead + round(1.0 * ref.fps)
    np.testing.assert_allclose(led.joint_pos[0], start)
    np.testing.assert_allclose(led.joint_pos[led.clip_start], ref.joint_pos[0])
    np.testing.assert_allclose(led.joint_pos[led.clip_end - 1], ref.joint_pos[-1])
    np.testing.assert_allclose(led.joint_pos[-1], ref.joint_pos[-1])
    # Heading alignment: the first frame faces the robot's heading, tilt unchanged.
    robot_q = ob.yaw_quat(1.2)
    al = led.aligned_to(robot_q)
    assert abs(ob.yaw_of(al.anchor_quat[0]) - 1.2) < 1e-6
    tilt = lambda q: ob.quat_to_matrix(q)[2, 2]  # noqa: E731
    np.testing.assert_allclose([tilt(q) for q in al.anchor_quat], [tilt(q) for q in led.anchor_quat], atol=1e-9)
