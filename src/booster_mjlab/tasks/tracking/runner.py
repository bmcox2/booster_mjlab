"""Tracking runner that skips the bundled ONNX export for large motion files.

mjlab's ``MotionTrackingOnPolicyRunner.save`` exports an ONNX policy with the whole
reference motion baked in as constants, at every checkpoint (iteration 0 included).
For the full BEAT2 sets that is several GB: past ONNX's 2 GB protobuf limit, and the
CPU copy kills the process without a traceback. Above ``MAX_BUNDLED_MOTION_BYTES``
this runner saves the ``.pt`` checkpoint only (``play`` / ``eval-tracking`` load the
``.pt``) and still links the motion artifact to the W&B run, which ``play`` and
``eval-tracking`` use to find the motion when no ``--registry-name`` is given.
"""

from __future__ import annotations

from typing import cast

import wandb
from mjlab.rl.runner import MjlabOnPolicyRunner
from mjlab.tasks.tracking.mdp import MotionCommand
from mjlab.tasks.tracking.rl import MotionTrackingOnPolicyRunner

MAX_BUNDLED_MOTION_BYTES = 1 << 30  # 1 GiB, well under the 2 GB protobuf limit


def motion_bytes(motion) -> int:
    keys = ("joint_pos", "joint_vel", "body_pos_w", "body_quat_w", "body_lin_vel_w", "body_ang_vel_w")
    return sum(getattr(motion, k).numel() * getattr(motion, k).element_size() for k in keys)


class K1MotionTrackingRunner(MotionTrackingOnPolicyRunner):
    _skip_warned = False

    def save(self, path: str, infos=None) -> None:
        cmd = cast(MotionCommand, self.env.unwrapped.command_manager.get_term("motion"))
        size = motion_bytes(cmd.motion)
        if size <= MAX_BUNDLED_MOTION_BYTES:
            super().save(path, infos)
            return
        MjlabOnPolicyRunner.save(self, path, infos)
        if not self._skip_warned:
            print(f"[INFO] Motion reference is {size / 1e9:.1f} GB: skipping the bundled ONNX export (checkpoints only).")
            self._skip_warned = True
        if self.registry_name is not None and wandb.run is not None and self.cfg["upload_model"]:
            wandb.run.use_artifact(self.registry_name)
            self.registry_name = None
