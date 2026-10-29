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

Every checkpoint also writes ``policy.onnx`` next to it (and to the W&B run's files): the policy
alone, observations -> actions, with no motion data inside. That is the file a robot or a sim2sim
loop runs; it feeds the reference frame by frame itself. Its metadata lists what that code needs:
joint order, default pose, PD gains, action scale, the observation terms and their sizes, and the
control period. ``uv run export-tracking-policy`` writes the same file for an existing checkpoint.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import cast

import wandb
from mjlab.envs import ManagerBasedRlEnv
from mjlab.rl.runner import MjlabOnPolicyRunner
from mjlab.tasks.tracking.mdp import MotionCommand
from mjlab.tasks.tracking.rl import MotionTrackingOnPolicyRunner

from booster_mjlab.rl.exporter_utils import attach_metadata_to_onnx, get_base_metadata

MAX_BUNDLED_MOTION_BYTES = 1 << 30  # 1 GiB, well under the 2 GB protobuf limit
DEPLOY_POLICY_FILE = "policy.onnx"


def deploy_metadata(env: ManagerBasedRlEnv, run_path: str) -> dict[str, list | str | float]:
    """ONNX metadata for a policy-only export: the repo's base metadata (joint order, default pose,
    PD gains, action scale, observation names) plus each actor observation term's size, the control
    period, and the tracking reference settings."""
    md = get_base_metadata(env, run_path)
    obs = env.observation_manager
    md["observation_dims"] = [int(math.prod(d)) for d in obs.group_obs_term_dim["actor"]]
    md["control_dt"] = float(env.step_dt)
    cmd = env.command_manager.get_term("motion")
    md["anchor_body_name"] = cmd.cfg.anchor_body_name
    md["has_state_estimation"] = str("motion_anchor_pos_b" in obs.active_terms["actor"])
    md["policy_inputs"] = "obs"
    md["policy_outputs"] = "actions (joint target = default_joint_pos + action_scale * action)"
    return md


def motion_bytes(motion) -> int:
    keys = ("joint_pos", "joint_vel", "body_pos_w", "body_quat_w", "body_lin_vel_w", "body_ang_vel_w")
    return sum(getattr(motion, k).numel() * getattr(motion, k).element_size() for k in keys)


class K1MotionTrackingRunner(MotionTrackingOnPolicyRunner):
    _skip_warned = False

    def export_deploy_policy(self, out_dir: str | Path, run_path: str = "local") -> Path:
        """Write ``policy.onnx`` (policy only, see the module docstring) into ``out_dir``."""
        out_dir = Path(out_dir)
        MjlabOnPolicyRunner.export_policy_to_onnx(self, str(out_dir), DEPLOY_POLICY_FILE)
        out = out_dir / DEPLOY_POLICY_FILE
        attach_metadata_to_onnx(str(out), deploy_metadata(self.env.unwrapped, run_path))
        return out

    def save(self, path: str, infos=None) -> None:
        cmd = cast(MotionCommand, self.env.unwrapped.command_manager.get_term("motion"))
        self._write_flagged_clips(cmd, Path(path).parent)
        run_path = wandb.run.path if wandb.run is not None else "local"
        out = self.export_deploy_policy(Path(path).parent, run_path)
        if wandb.run is not None:
            wandb.save(str(out), base_path=str(out.parent), policy="now")
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
