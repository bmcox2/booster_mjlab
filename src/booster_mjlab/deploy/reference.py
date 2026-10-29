"""A reference clip played at the control rate, with a lead-in, an end hold, and heading alignment.

The tracker has never practiced starting from rest or stopping (training starts robots *on* the
reference, mid-clip, and teleports them at clip ends; roadmap criterion 5). For a demo the safest
way in and out is through poses it has seen: the lead-in blends the joints from the robot's standing
pose to the clip's first frame while the trunk holds the first frame's orientation, then holds that
frame; the end holds the last frame. ``scripts/sim2sim.py`` checks that this works before a robot
ever runs it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from booster_mjlab.deploy import observation as ob


@dataclass
class RefFrame:
    joint_pos: np.ndarray  # (J,) rad
    joint_vel: np.ndarray  # (J,) rad/s
    anchor_quat: np.ndarray  # (4,) w, x, y, z: reference trunk orientation (world <- trunk)


@dataclass
class Reference:
    joint_pos: np.ndarray  # (T, J)
    joint_vel: np.ndarray  # (T, J)
    anchor_quat: np.ndarray  # (T, 4)
    fps: float
    name: str = ""
    body_pos: np.ndarray | None = None  # (T, B, 3) world, for metrics only (not seen by the policy)
    body_names: list[str] = field(default_factory=list)
    clip_start: int = 0  # first frame of the clip itself (after the lead-in)
    clip_end: int = 0  # one past its last frame (before the end hold)

    def __post_init__(self) -> None:
        if not self.clip_end:
            self.clip_end = len(self)

    def __len__(self) -> int:
        return len(self.joint_pos)

    @property
    def seconds(self) -> float:
        return len(self) / self.fps

    @classmethod
    def from_npz(cls, path: str | Path, clip: str | None = None, anchor_body: int = 0,
                 body_names: list[str] | None = None) -> Reference:
        """One clip of a (combined) motion .npz. ``anchor_body``: index of the trunk in body_pos_w /
        body_quat_w (0 for files written by combine-motions / upload-motion: the robot's bodies in
        model order, trunk first)."""
        path = Path(path)
        with np.load(path) as z:
            lengths = z["clip_lengths"] if "clip_lengths" in z.files else np.array([len(z["joint_pos"])])
            names = [str(n) for n in z["clip_names"]] if "clip_names" in z.files else [path.stem]
            if clip is None:
                i = 0
            elif clip in names:
                i = names.index(clip)
            else:
                raise SystemExit(f"clip {clip!r} not in {path.name} ({len(names)} clips, e.g. {names[:3]})")
            s = int(np.sum(lengths[:i]))
            e = s + int(lengths[i])
            return cls(
                joint_pos=np.asarray(z["joint_pos"][s:e], np.float64),
                joint_vel=np.asarray(z["joint_vel"][s:e], np.float64),
                anchor_quat=np.asarray(z["body_quat_w"][s:e, anchor_body], np.float64),
                fps=float(np.asarray(z["fps"]).reshape(-1)[0]),
                name=names[i],
                body_pos=np.asarray(z["body_pos_w"][s:e], np.float64),
                body_names=list(body_names or []),
            )

    def frame(self, i: int) -> RefFrame:
        i = min(max(i, 0), len(self) - 1)
        return RefFrame(self.joint_pos[i], self.joint_vel[i], self.anchor_quat[i])

    def with_lead_in(self, start_joint_pos: np.ndarray, blend_s: float, hold_s: float) -> Reference:
        """Prepend: joints blend (smoothstep) from ``start_joint_pos`` to frame 0 over ``blend_s``,
        then frame 0 is held for ``hold_s``. The trunk keeps frame 0's orientation throughout."""
        nb, nh = round(blend_s * self.fps), round(hold_s * self.fps)
        t = np.linspace(0.0, 1.0, nb, endpoint=False) if nb else np.zeros(0)
        w = (t * t * (3 - 2 * t))[:, None]
        blend = (1 - w) * start_joint_pos[None] + w * self.joint_pos[0][None]
        pos = np.concatenate([blend, np.repeat(self.joint_pos[:1], nh, 0), self.joint_pos])
        vel = np.concatenate([np.gradient(blend, 1 / self.fps, axis=0) if nb > 1 else np.zeros((nb, pos.shape[1])),
                              np.zeros((nh, pos.shape[1])), self.joint_vel])
        n = nb + nh
        return Reference(
            pos, vel, np.concatenate([np.repeat(self.anchor_quat[:1], n, 0), self.anchor_quat]), self.fps, self.name,
            None if self.body_pos is None else np.concatenate([np.repeat(self.body_pos[:1], n, 0), self.body_pos]),
            self.body_names, self.clip_start + n, self.clip_end + n,
        )

    def with_end_hold(self, hold_s: float) -> Reference:
        """Append ``hold_s`` of the last frame, standing still."""
        n = round(hold_s * self.fps)
        J = self.joint_pos.shape[1]
        return Reference(
            np.concatenate([self.joint_pos, np.repeat(self.joint_pos[-1:], n, 0)]),
            np.concatenate([self.joint_vel, np.zeros((n, J))]),
            np.concatenate([self.anchor_quat, np.repeat(self.anchor_quat[-1:], n, 0)]),
            self.fps, self.name,
            None if self.body_pos is None else np.concatenate([self.body_pos, np.repeat(self.body_pos[-1:], n, 0)]),
            self.body_names, self.clip_start, self.clip_end,
        )

    def aligned_to(self, robot_trunk_quat: np.ndarray) -> Reference:
        """Turn the whole clip about the vertical so its first frame faces where the robot faces (the
        robot's heading is arbitrary; only the policy's relative orientation matters)."""
        dq = ob.yaw_quat(ob.yaw_of(robot_trunk_quat) - ob.yaw_of(self.anchor_quat[0]))
        quats = np.stack([ob.quat_mul(dq, q) for q in self.anchor_quat])
        body = None
        if self.body_pos is not None:
            R = ob.quat_to_matrix(dq)
            body = self.body_pos @ R.T
        return Reference(self.joint_pos, self.joint_vel, quats, self.fps, self.name, body, self.body_names,
                         self.clip_start, self.clip_end)
