"""Tracking runner that skips the bundled ONNX export for large motion files.

mjlab's ``MotionTrackingOnPolicyRunner.save`` exports an ONNX policy with the whole
reference motion baked in as constants, at every checkpoint (iteration 0 included).
For the full BEAT2 sets that is several GB: past ONNX's 2 GB protobuf limit, and the
CPU copy kills the process without a traceback. Above ``MAX_BUNDLED_MOTION_BYTES``
this runner saves the ``.pt`` checkpoint only (``play`` / ``eval-tracking`` load the
``.pt``) and still links the motion artifact to the W&B run, which ``play`` and
``eval-tracking`` use to find the motion when no ``--registry-name`` is given.

It also writes ``flagged_clips.json`` (clips the sampling harness quarantined, see
``MultiMotionCommand``) next to the checkpoints and to the W&B run's files.
"""

from __future__ import annotations

import json
from pathlib import Path
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
        self._write_flagged_clips(cmd, Path(path).parent)
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

    @staticmethod
    def _write_flagged_clips(cmd: MotionCommand, log_dir: Path) -> None:
        flagged = getattr(cmd, "flagged_clips", None)
        if not flagged:
            return
        out = log_dir / "flagged_clips.json"
        out.write_text(json.dumps(flagged, indent=2))
        if wandb.run is not None:
            wandb.save(str(out), base_path=str(log_dir), policy="live")
