"""Multi-clip motion tracking: one policy, many reference clips.

mjlab's ``MotionCommand`` tracks one clip: every robot reads row ``time_steps`` of one long
array of frames and jumps to a new random frame when it runs off the end. ``MultiMotionCommand``
loads a *combined* file (several clips concatenated end to end, plus a clip table) and keeps,
per robot, which clip it is on (``clip_ids``) and its frame within that clip (``clip_frames``).

The row it reads is ``clip_starts[clip_id] + frame``. That row is stored in mjlab's own
``time_steps``, so every inherited property (``joint_pos``, ``body_pos_w``, ...), and with them
every observation, reward, termination, metric, the viewer and the ONNX export, reads the right
frame without being changed.

Rules:
- A robot never reads past the end of its own clip: on its clip's last frame it is resampled
  (teleported to a new start), the same thing mjlab does at the end of its single clip.
- Adaptive sampling uses ~1 s bins per clip (no bin spans two clips), pooled into one
  distribution over all clips.
- A file without a clip table is one clip, and then everything behaves exactly like mjlab's.

Combined files are built by ``uv run combine-motions``. See notes/multi-clip.md.
"""

from __future__ import annotations

import contextlib
import math
from dataclasses import dataclass, fields
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np
import torch

import mjlab.tasks.tracking.mdp.commands as mjlab_commands
from mjlab.tasks.tracking.mdp.commands import MotionCommand, MotionCommandCfg
from mjlab.utils.lab_api.math import quat_from_euler_xyz, quat_mul, sample_uniform

if TYPE_CHECKING:
    from mjlab.envs import ManagerBasedRlEnv

# Errors also logged per clip, as Metrics/motion/clip/<error>/<clip name>.
PER_CLIP_ERRORS = ("error_body_pos", "error_joint_pos", "error_anchor_pos")


def read_clip_table(motion_file: str | Path) -> tuple[list[str], np.ndarray]:
    """Clip names and lengths (frames) in a motion .npz. A file without a table is one clip."""
    path = Path(motion_file)
    with np.load(path) as data:
        if "clip_lengths" in data.files:
            lengths = data["clip_lengths"].astype(np.int64)
            names = [str(n) for n in data["clip_names"]]
        else:
            lengths = np.array([data["joint_pos"].shape[0]], dtype=np.int64)
            names = [path.parent.name if path.name == "motion.npz" else path.stem]
    if len(names) != len(lengths):
        raise ValueError(f"{path}: {len(names)} clip names but {len(lengths)} clip lengths")
    return names, lengths


def bins_per_clip(lengths: np.ndarray, steps_per_second: float) -> np.ndarray:
    """mjlab's adaptive-sampling bin count (whole seconds + 1, equal-size bins), applied per clip."""
    return np.array([int(n // steps_per_second) + 1 for n in lengths], dtype=np.int64)


def kernel_index(clip_bin_counts: torch.Tensor, kernel_size: int) -> torch.Tensor:
    """(num_bins, kernel_size) gather index for smoothing failure counts with a look-ahead kernel.

    mjlab smooths bin b with bins b..b+K-1 and pads past the end of the file by repeating its
    last bin. Here the look-ahead stops at the last bin of b's own clip (that bin is repeated),
    so failures at the start of one clip never raise the end of the clip before it.
    """
    counts = clip_bin_counts
    device = counts.device
    clip_last_bin = torch.cumsum(counts, 0) - 1
    bin_clip = torch.repeat_interleave(torch.arange(len(counts), device=device), counts)
    b = torch.arange(int(counts.sum()), device=device)
    k = torch.arange(kernel_size, device=device)
    return torch.minimum(b[:, None] + k[None, :], clip_last_bin[bin_clip][:, None])


class LeanMotionLoader:
    """mjlab's MotionLoader with the same tensors, at about half the GPU memory.

    mjlab moves all bodies of every frame to the device, then indexes the tracked bodies out of
    them, which copies: the device holds every body array twice (~0.53 GB per hour of 50 Hz
    reference for the K1's 25 bodies). This picks the tracked bodies on the CPU and moves only
    them, so a ~30 h BEAT2 training file takes ~8 GB instead of ~16. Nothing reads the
    full-body arrays (``_body_*``) except MotionLoader itself.
    """

    def __init__(self, motion_file: str, body_indexes: torch.Tensor, device: str = "cpu") -> None:
        idx = body_indexes.cpu().numpy()
        with np.load(motion_file) as data:
            def put(key: str, bodies: bool = False) -> torch.Tensor:
                arr = data[key]
                return torch.tensor(arr[:, idx] if bodies else arr, dtype=torch.float32, device=device)

            self.joint_pos = put("joint_pos")
            self.joint_vel = put("joint_vel")
            self.body_pos_w = put("body_pos_w", True)
            self.body_quat_w = put("body_quat_w", True)
            self.body_lin_vel_w = put("body_lin_vel_w", True)
            self.body_ang_vel_w = put("body_ang_vel_w", True)
        self._body_indexes = body_indexes
        self.time_step_total = self.joint_pos.shape[0]


@contextlib.contextmanager
def _lean_motion_loader():
    """Make mjlab's MotionCommand.__init__ build a LeanMotionLoader (only while it runs)."""
    original = mjlab_commands.MotionLoader
    mjlab_commands.MotionLoader = LeanMotionLoader
    try:
        yield
    finally:
        mjlab_commands.MotionLoader = original


class MultiMotionCommand(MotionCommand):
    cfg: MultiMotionCommandCfg

    def __init__(self, cfg: MultiMotionCommandCfg, env: ManagerBasedRlEnv):
        """mjlab: loads the whole file into ``self.motion`` (MotionLoader), sets every robot's
        ``time_steps`` to 0, and builds ~1 s adaptive-sampling bins over the whole file.

        Changed: the frames are loaded once, by mjlab's own code, through LeanMotionLoader (same
        tensors, half the GPU memory). On top, this reads the clip table from the same file, gives
        each robot a (clip, frame) pair, and rebuilds the bins per clip so that no bin spans two clips.
        """
        with _lean_motion_loader():
            super().__init__(cfg, env)

        names, lengths = read_clip_table(cfg.motion_file)
        total = self.motion.time_step_total
        if int(lengths.sum()) != total:
            raise ValueError(f"{cfg.motion_file}: clip lengths sum to {int(lengths.sum())}, file has {total} frames")
        if (lengths < 2).any():
            raise ValueError(f"{cfg.motion_file}: every clip needs at least 2 frames")
        self.clip_names = names
        self.num_clips = len(names)
        self.clip_lengths = torch.tensor(lengths, dtype=torch.long, device=self.device)
        self.clip_starts = torch.cumsum(self.clip_lengths, 0) - self.clip_lengths

        # Per-robot state. In "start" mode (play/eval) robot i begins on clip i % num_clips.
        self.clip_ids = torch.arange(self.num_envs, device=self.device) % self.num_clips
        self.clip_frames = torch.zeros(self.num_envs, dtype=torch.long, device=self.device)
        self._sync_time_steps()

        # Adaptive-sampling bins, laid out clip after clip: bins [clip_bin_starts[c], +clip_bin_counts[c]).
        counts = bins_per_clip(lengths, 1.0 / env.step_dt)
        self.clip_bin_counts = torch.tensor(counts, dtype=torch.long, device=self.device)
        self.clip_bin_starts = torch.cumsum(self.clip_bin_counts, 0) - self.clip_bin_counts
        self.bin_count = int(counts.sum())
        self.bin_clip = torch.repeat_interleave(torch.arange(self.num_clips, device=self.device), self.clip_bin_counts)
        self.bin_failed_count = torch.zeros(self.bin_count, dtype=torch.float, device=self.device)
        self._current_bin_failed = torch.zeros(self.bin_count, dtype=torch.float, device=self.device)
        self._kernel_index = kernel_index(self.clip_bin_counts, self.cfg.adaptive_kernel_size)

    # ------------------------------------------------------------------ bookkeeping (new)

    def _sync_time_steps(self, env_ids: torch.Tensor | None = None) -> None:
        """Write each robot's lookup row (clip start + frame) into mjlab's ``time_steps``."""
        if env_ids is None:
            self.time_steps[:] = self.clip_starts[self.clip_ids] + self.clip_frames
        else:
            self.time_steps[env_ids] = self.clip_starts[self.clip_ids[env_ids]] + self.clip_frames[env_ids]

    def _bin_of(self, clip_ids: torch.Tensor, frames: torch.Tensor) -> torch.Tensor:
        """Global adaptive-sampling bin of a (clip, frame) pair."""
        n_bins = self.clip_bin_counts[clip_ids]
        local = torch.clamp((frames * n_bins) // self.clip_lengths[clip_ids], torch.zeros_like(n_bins), n_bins - 1)
        return self.clip_bin_starts[clip_ids] + local

    def _sampling_probabilities(self) -> torch.Tensor:
        """Adaptive-sampling distribution over all bins (mjlab's formula, smoothed within each clip)."""
        probs = self.bin_failed_count + self.cfg.adaptive_uniform_ratio / float(self.bin_count)
        probs = (probs[self._kernel_index] * self.kernel).sum(dim=-1)
        return probs / probs.sum()

    def clip_sampling_share(self) -> torch.Tensor:
        """(num_clips,) chance that a new start lands on each clip under the current sampling mode."""
        if self.cfg.sampling_mode == "adaptive":
            return torch.zeros(self.num_clips, device=self.device).index_add_(
                0, self.bin_clip, self._sampling_probabilities()
            )
        if self.cfg.sampling_mode == "uniform":
            return self.clip_lengths.float() / self.motion.time_step_total
        return torch.full((self.num_clips,), 1.0 / self.num_clips, device=self.device)

    # ------------------------------------------------------------------ sampling (overrides)

    def _start_sampling(self, env_ids: torch.Tensor) -> None:
        """mjlab has no method for this: its "start" branch sets ``time_steps = 0``, the first
        frame of the whole file. Here: frame 0 of the robot's own clip. (At the end of a clip,
        ``_update_command`` moves a "start"-mode robot on to the next clip first.)
        """
        self.clip_frames[env_ids] = 0
        self._sync_time_steps(env_ids)

    def _uniform_sampling(self, env_ids: torch.Tensor) -> None:
        """mjlab: a uniformly random row of the file.

        Unchanged: it is still a uniformly random row of the whole file (same random draw), so
        each clip is picked in proportion to its length. Added: work out which clip that row is
        in and the frame within it. A row belongs to exactly one clip, so this can't cross a
        boundary.
        """
        rows = torch.randint(0, self.motion.time_step_total, (len(env_ids),), device=self.device)
        clips = torch.searchsorted(self.clip_starts, rows, right=True) - 1
        self.clip_ids[env_ids] = clips
        self.clip_frames[env_ids] = rows - self.clip_starts[clips]
        self._sync_time_steps(env_ids)
        self.metrics["sampling_entropy"][:] = 1.0  # Maximum entropy for uniform.
        self.metrics["sampling_top1_prob"][:] = 1.0 / self.bin_count
        self.metrics["sampling_top1_bin"][:] = 0.5  # No specific bin preference.

    def _adaptive_sampling(self, env_ids: torch.Tensor) -> None:
        """mjlab: count failures per ~1 s bin of the file; pick a bin with probability that grows
        with its recent failure count (plus a uniform floor, smoothed by a look-ahead kernel so
        robots start a little *before* the hard part); then a random frame inside that bin.

        Changed: bins are per clip; a failure is binned by the robot's (clip, frame); the
        smoothing stops at clip ends (``kernel_index``); the sampled bin gives both the clip
        and the frame. Failures are added (+=) rather than assigned, so two resets between
        averaging steps both count. With one clip this is the same draw as mjlab's.
        """
        episode_failed = self._env.termination_manager.terminated[env_ids]
        if torch.any(episode_failed):
            failed = env_ids[episode_failed]
            fail_bins = self._bin_of(self.clip_ids[failed], self.clip_frames[failed])
            self._current_bin_failed += torch.bincount(fail_bins, minlength=self.bin_count)

        sampling_probabilities = self._sampling_probabilities()
        sampled_bins = torch.multinomial(sampling_probabilities, len(env_ids), replacement=True)
        clips = self.bin_clip[sampled_bins]
        local_bins = sampled_bins - self.clip_bin_starts[clips]
        frames = (
            (local_bins + sample_uniform(0.0, 1.0, (len(env_ids),), device=self.device))
            / self.clip_bin_counts[clips]
            * (self.clip_lengths[clips] - 1)
        ).long()
        self.clip_ids[env_ids] = clips
        self.clip_frames[env_ids] = frames
        self._sync_time_steps(env_ids)

        # Update metrics (unchanged; over all bins of all clips).
        H = -(sampling_probabilities * (sampling_probabilities + 1e-12).log()).sum()
        H_norm = H / math.log(self.bin_count) if self.bin_count > 1 else 1.0
        pmax, imax = sampling_probabilities.max(dim=0)
        self.metrics["sampling_entropy"][:] = H_norm
        self.metrics["sampling_top1_prob"][:] = pmax
        self.metrics["sampling_top1_bin"][:] = imax.float() / self.bin_count

    def _resample_command(self, env_ids: torch.Tensor) -> None:
        """mjlab: pick a frame (by ``sampling_mode``), then teleport the robot onto the reference
        at that frame plus small random offsets (``pose_range``, ``velocity_range``,
        ``joint_position_range``).

        Changed: only the frame picking. "start" means frame 0 of the robot's own clip, and all
        three modes set (clip, frame) as well as the row. Everything from "root_pos = ..." down
        is mjlab's code, unchanged; it reads the reference through ``time_steps``, which the
        samplers have just set.
        """
        if self.cfg.sampling_mode == "start":
            self._start_sampling(env_ids)
        elif self.cfg.sampling_mode == "uniform":
            self._uniform_sampling(env_ids)
        else:
            assert self.cfg.sampling_mode == "adaptive"
            self._adaptive_sampling(env_ids)

        root_pos = self.body_pos_w[env_ids, 0].clone()
        root_ori = self.body_quat_w[env_ids, 0].clone()
        root_lin_vel = self.body_lin_vel_w[env_ids, 0].clone()
        root_ang_vel = self.body_ang_vel_w[env_ids, 0].clone()

        range_list = [self.cfg.pose_range.get(key, (0.0, 0.0)) for key in ["x", "y", "z", "roll", "pitch", "yaw"]]
        ranges = torch.tensor(range_list, device=self.device)
        rand_samples = sample_uniform(ranges[:, 0], ranges[:, 1], (len(env_ids), 6), device=self.device)
        root_pos += rand_samples[:, 0:3]
        orientations_delta = quat_from_euler_xyz(rand_samples[:, 3], rand_samples[:, 4], rand_samples[:, 5])
        root_ori = quat_mul(orientations_delta, root_ori)
        range_list = [self.cfg.velocity_range.get(key, (0.0, 0.0)) for key in ["x", "y", "z", "roll", "pitch", "yaw"]]
        ranges = torch.tensor(range_list, device=self.device)
        rand_samples = sample_uniform(ranges[:, 0], ranges[:, 1], (len(env_ids), 6), device=self.device)
        root_lin_vel += rand_samples[:, :3]
        root_ang_vel += rand_samples[:, 3:]

        joint_pos = self.joint_pos[env_ids].clone()
        joint_vel = self.joint_vel[env_ids]

        joint_pos += sample_uniform(
            lower=self.cfg.joint_position_range[0],
            upper=self.cfg.joint_position_range[1],
            size=joint_pos.shape,
            device=joint_pos.device,  # type: ignore
        )

        self._write_reference_state_to_sim(
            env_ids, root_pos, root_ori, root_lin_vel, root_ang_vel, joint_pos, joint_vel
        )
        self._pending_forward = True

    # ------------------------------------------------------------------ stepping (override)

    def _update_command(self, env_ids: torch.Tensor | None = None):
        """mjlab: advance every robot one frame; robots past the end of the file are resampled;
        refresh physics if anything was teleported; recompute the reference re-anchored to each
        robot (``update_relative_body_poses``); fold this step's failures into the adaptive
        sampling average.

        Changed: the counter that advances is the frame within the robot's clip, and "past the
        end" means past the end of *its own* clip, so the row never enters the next clip. In
        "start" mode (play/eval) a robot that finishes a clip moves on to the next one instead
        of replaying the same clip. The rest is mjlab's code, unchanged.
        """
        if env_ids is None:
            self.clip_frames += 1
        else:
            self.clip_frames[env_ids] += 1
        wrap_ids = torch.where(self.clip_frames >= self.clip_lengths[self.clip_ids])[0]
        if wrap_ids.numel() > 0:
            if self.cfg.sampling_mode == "start":
                self.clip_ids[wrap_ids] = (self.clip_ids[wrap_ids] + 1) % self.num_clips
            self._resample_command(wrap_ids)
        self._sync_time_steps()

        # _resample_command writes qpos/qvel but does not refresh derived
        # quantities; forward() so update_relative_body_poses reads the
        # post-teleport robot anchor instead of the stale pre-resample pose.
        if self._pending_forward:
            self._pending_forward = False
            self._env.sim.forward()

        self.update_relative_body_poses()

        # Fold failure counts into the EMA only on the per-step update so
        # manual resets do not decay it faster.
        if env_ids is None and self.cfg.sampling_mode == "adaptive":
            self.bin_failed_count = (
                self.cfg.adaptive_alpha * self._current_bin_failed
                + (1 - self.cfg.adaptive_alpha) * self.bin_failed_count
            )
            self._current_bin_failed.zero_()

    # ------------------------------------------------------------------ small overrides

    def reset(self, env_ids: torch.Tensor | slice | None) -> dict[str, float]:
        """mjlab: for the robots being reset, log each metric's mean (W&B: Metrics/motion/<name>),
        zero the metrics, and resample the robots.

        Added: before the robots are resampled (and change clip), the same errors split by
        clip, plus each clip's early-termination rate and its share of new starts:
        Metrics/motion/clip/<error | fail_rate | sample_share>/<clip name>.
        """
        clip_extras = {}
        if self.cfg.log_per_clip_metrics and self.num_clips > 1 and isinstance(env_ids, torch.Tensor):
            clip_extras = self._per_clip_extras(env_ids)
        extras = super().reset(env_ids)
        extras.update(clip_extras)
        return extras

    def _per_clip_extras(self, env_ids: torch.Tensor) -> dict[str, float]:
        if len(env_ids) == 0:
            return {}
        clips = self.clip_ids[env_ids]
        zeros = torch.zeros(self.num_clips, device=self.device)
        rows = [torch.bincount(clips, minlength=self.num_clips).float()]
        rows += [zeros.clone().index_add_(0, clips, self.metrics[name][env_ids]) for name in PER_CLIP_ERRORS]
        failed = self._env.termination_manager.terminated[env_ids].float()
        rows.append(zeros.clone().index_add_(0, clips, failed))
        rows.append(self.clip_sampling_share())
        table = torch.stack(rows).tolist()  # one GPU->CPU copy per reset, not one per clip

        extras = {}
        for c, name in enumerate(self.clip_names):
            extras[f"clip/sample_share/{name}"] = table[-1][c]
            n = table[0][c]
            if n == 0:  # no robot on this clip reset this step; rsl_rl skips missing keys
                continue
            for i, metric in enumerate(PER_CLIP_ERRORS):
                extras[f"clip/{metric}/{name}"] = table[1 + i][c] / n
            extras[f"clip/fail_rate/{name}"] = table[-2][c] / n
        return extras

    def reset_to_frame(self, env_ids: torch.Tensor, frame: int) -> None:
        """mjlab: put robots exactly on the reference at row ``frame`` of the file, no random
        offsets (the viewer's frame scrubber uses this). Changed: also record which clip that
        row is in, so the robot carries on within that clip.
        """
        clip = int(torch.searchsorted(self.clip_starts, torch.tensor(frame, device=self.device), right=True)) - 1
        self.clip_ids[env_ids] = clip
        self.clip_frames[env_ids] = frame - self.clip_starts[clip]
        super().reset_to_frame(env_ids, frame)


@dataclass(kw_only=True)
class MultiMotionCommandCfg(MotionCommandCfg):
    log_per_clip_metrics: bool = True
    """Log errors, fail rate, and sampling share per clip (only when the file has 2+ clips)."""

    @classmethod
    def from_motion_cfg(cls, cfg: MotionCommandCfg) -> MultiMotionCommandCfg:
        """Same settings as an existing (mjlab) MotionCommandCfg."""
        return cls(**{f.name: getattr(cfg, f.name) for f in fields(cfg) if f.init})

    def build(self, env: ManagerBasedRlEnv) -> MultiMotionCommand:
        return MultiMotionCommand(self, env)
