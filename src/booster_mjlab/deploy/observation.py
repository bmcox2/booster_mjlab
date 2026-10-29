"""The policy's observation vector from robot measurements + the reference, as mjlab builds it.

Each term below reproduces the mjlab function the training config uses (``mjlab.tasks.tracking``
and ``mjlab.envs.mdp``); ``tests/test_deploy.py`` checks them against the real env. Quaternions are
(w, x, y, z), world frame; the trunk is the anchor body and the K1's IMU sits at the trunk origin,
so the IMU orientation and gyro are the trunk's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from booster_mjlab.deploy.reference import RefFrame


@dataclass
class RobotState:
    """What the robot measures, in the policy's joint order (``TrackingPolicy.joint_names``)."""

    joint_pos: np.ndarray  # (J,) rad
    joint_vel: np.ndarray  # (J,) rad/s
    trunk_quat: np.ndarray  # (4,) w, x, y, z: IMU orientation (world <- trunk)
    gyro: np.ndarray  # (3,) rad/s, trunk frame


def quat_to_matrix(q: np.ndarray) -> np.ndarray:
    w, x, y, z = q / np.linalg.norm(q)
    return np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - w * z), 2 * (x * z + w * y)],
        [2 * (x * y + w * z), 1 - 2 * (x * x + z * z), 2 * (y * z - w * x)],
        [2 * (x * z - w * y), 2 * (y * z + w * x), 1 - 2 * (x * x + y * y)],
    ])


def quat_mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return np.array([
        aw * bw - ax * bx - ay * by - az * bz,
        aw * bx + ax * bw + ay * bz - az * by,
        aw * by - ax * bz + ay * bw + az * bx,
        aw * bz + ax * by - ay * bx + az * bw,
    ])


def yaw_of(q: np.ndarray) -> float:
    w, x, y, z = q
    return float(np.arctan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z)))


def yaw_quat(yaw: float) -> np.ndarray:
    return np.array([np.cos(yaw / 2), 0.0, 0.0, np.sin(yaw / 2)])


def _term(name: str, state: RobotState, ref: RefFrame, last_action: np.ndarray, default_joint_pos: np.ndarray,
          privileged: dict[str, np.ndarray] | None) -> np.ndarray:
    if privileged and name in privileged:  # sim only (see build_observation)
        return privileged[name]
    if name == "command":  # MotionCommand.command: reference joint positions, then velocities
        return np.concatenate([ref.joint_pos, ref.joint_vel])
    if name == "motion_anchor_ori_b":  # reference trunk orientation in the robot trunk frame, rotation
        rel = quat_to_matrix(state.trunk_quat).T @ quat_to_matrix(ref.anchor_quat)  # matrix columns 0-1
        return rel[:, :2].reshape(-1)
    if name == "base_ang_vel":  # gyro (IMU at the trunk origin)
        return state.gyro
    if name == "joint_pos":  # joint_pos_rel
        return state.joint_pos - default_joint_pos
    if name == "joint_vel":  # joint_vel_rel (default velocity is 0)
        return state.joint_vel
    if name == "actions":  # last_action: the raw policy output
        return last_action
    if name == "projected_gravity":  # world gravity direction in the trunk frame
        return quat_to_matrix(state.trunk_quat).T @ np.array([0.0, 0.0, -1.0])
    if name in ("motion_anchor_pos_b", "base_lin_vel"):
        raise ValueError(
            f"this policy observes {name}, which the robot can't measure without state estimation: "
            "train on Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation"
        )
    raise ValueError(f"unknown observation term {name}")


def build_observation(
    names: list[str],
    dims: list[int],
    state: RobotState,
    ref: RefFrame,
    last_action: np.ndarray,
    default_joint_pos: np.ndarray,
    privileged: dict[str, np.ndarray] | None = None,
) -> np.ndarray:
    """Concatenate the terms in the policy's order (``TrackingPolicy.observation_names`` / ``_dims``).

    ``privileged``: values for terms a robot can't measure (``motion_anchor_pos_b``, ``base_lin_vel``),
    which only a simulator knows. Only for checking the sim2sim model with a state-estimation policy.
    """
    parts = []
    for name, dim in zip(names, dims, strict=True):
        v = np.asarray(_term(name, state, ref, last_action, default_joint_pos, privileged), dtype=np.float64).reshape(-1)
        if v.size != dim:
            raise ValueError(f"observation term {name}: built {v.size} values, the policy expects {dim}")
        parts.append(v)
    return np.concatenate(parts).astype(np.float32)
