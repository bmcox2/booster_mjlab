"""Checks for MultiMotionCommand on a real (CPU) K1 tracking env.

Needs a 2-clip combined file. Build it once with:
    uv run combine-motions bmcox2-university-of-illinois-urbana-champaign/motion_upload/wave_000508-tracking:v3 \\
        bmcox2-university-of-illinois-urbana-champaign/motion_upload/wave_001104-tracking:v2 \\
        --output logs/motions/waves_2clip.npz --no-upload
Run:
    uv run --with pytest pytest tests/test_multi_motion.py -q
"""

from __future__ import annotations

import dataclasses
import os
from pathlib import Path

import numpy as np
import pytest
import torch

import booster_mjlab.tasks  # noqa: F401, registers the K1 tasks
from booster_mjlab.tasks.tracking.multi_motion_command import LeanMotionLoader, MultiMotionCommand, kernel_index
from mjlab.envs import ManagerBasedRlEnv
from mjlab.tasks.registry import load_env_cfg
from mjlab.tasks.tracking.mdp.commands import MotionCommand, MotionCommandCfg, MotionLoader

MOTION = Path(os.environ.get("MULTI_MOTION_FILE", "logs/motions/waves_2clip.npz"))
TASK = "Mjlab-Tracking-Flat-Booster-K1"
NUM_ENVS = 64

pytestmark = pytest.mark.skipif(not MOTION.exists(), reason=f"{MOTION} missing; see module docstring")


@pytest.fixture(scope="module")
def env():
    cfg = load_env_cfg(TASK)  # training config: adaptive sampling, pushes, terminations
    cfg.scene.num_envs = NUM_ENVS
    cfg.commands["motion"].motion_file = str(MOTION)
    e = ManagerBasedRlEnv(cfg=cfg, device="cpu")
    e.reset()
    yield e
    e.close()


@pytest.fixture
def cmd(env) -> MultiMotionCommand:
    c = env.command_manager.get_term("motion")
    assert isinstance(c, MultiMotionCommand)
    mode = c.cfg.sampling_mode
    yield c
    c.cfg.sampling_mode = mode


def assert_rows_inside_own_clip(cmd: MultiMotionCommand) -> None:
    """The invariant: every robot's lookup row is clip_start + frame, with frame inside its clip."""
    lengths = cmd.clip_lengths[cmd.clip_ids]
    assert torch.equal(cmd.time_steps, cmd.clip_starts[cmd.clip_ids] + cmd.clip_frames)
    assert (cmd.clip_frames >= 0).all()
    assert (cmd.clip_frames < lengths).all(), "a robot's frame ran past the end of its clip"
    assert (cmd.time_steps < cmd.clip_starts[cmd.clip_ids] + lengths).all()


def test_clip_table(cmd):
    assert cmd.clip_names == ["wave_000508", "wave_001104"]
    assert cmd.clip_lengths.tolist() == [188, 147]
    assert cmd.clip_starts.tolist() == [0, 188]
    assert cmd.motion.time_step_total == 335
    # mjlab's bin formula per clip: 188 frames // 50 + 1 = 4 bins, 147 // 50 + 1 = 3 bins.
    assert cmd.clip_bin_counts.tolist() == [4, 3]
    assert cmd.bin_clip.tolist() == [0, 0, 0, 0, 1, 1, 1]


@pytest.mark.parametrize("mode", ["adaptive", "uniform", "start"])
def test_never_reads_across_clip_boundary(env, cmd, mode):
    """Step only the command (no physics, so no falls): every change of frame is +1 or a wrap at clip end."""
    cmd.cfg.sampling_mode = mode
    env.command_manager.reset(torch.arange(NUM_ENVS))
    wraps = 0
    for _ in range(600):  # > 3x the longest clip, so every robot hits clip ends repeatedly
        prev_clip, prev_frame = cmd.clip_ids.clone(), cmd.clip_frames.clone()
        cmd.compute(dt=env.step_dt)
        assert_rows_inside_own_clip(cmd)
        advanced = (cmd.clip_ids == prev_clip) & (cmd.clip_frames == prev_frame + 1)
        was_last = prev_frame == cmd.clip_lengths[prev_clip] - 1
        assert (advanced | was_last).all(), "a robot jumped without reaching its clip's end"
        assert not (advanced & was_last).any(), "a robot stepped from its last frame to frame len"
        if mode == "start":  # play/eval: finish a clip, then frame 0 of the next clip
            w = was_last
            assert (cmd.clip_frames[w] == 0).all()
            assert torch.equal(cmd.clip_ids[w], (prev_clip[w] + 1) % cmd.num_clips)
        wraps += int(was_last.sum())
    assert wraps > NUM_ENVS, "test never exercised the end of a clip"


def test_boundaries_hold_with_falls_and_resets(env, cmd):
    """Full env steps with random actions: robots fall, reset and wrap, and rows stay inside their clip."""
    torch.manual_seed(0)
    env.reset()
    resets, seen_keys = 0, set()
    for _ in range(300):
        prev_clip, prev_frame = cmd.clip_ids.clone(), cmd.clip_frames.clone()
        action = torch.randn(NUM_ENVS, env.action_manager.total_action_dim) * 2.0
        _, _, terminated, truncated, extras = env.step(action)
        assert_rows_inside_own_clip(cmd)
        reset = terminated | truncated
        advanced = (cmd.clip_ids == prev_clip) & (cmd.clip_frames == prev_frame + 1)
        was_last = prev_frame == cmd.clip_lengths[prev_clip] - 1
        assert (advanced | was_last | reset).all()
        resets += int(reset.sum())
        seen_keys |= set(extras.get("log", {}))
    assert resets > 0, "random actions should make some robots fall"
    # Per-clip metrics reach the log extras (W&B: Metrics/motion/clip/<metric>/<clip>).
    for name in cmd.clip_names:
        assert f"Metrics/motion/clip/error_body_pos/{name}" in seen_keys
        assert f"Metrics/motion/clip/fail_rate/{name}" in seen_keys
        assert f"Metrics/motion/clip/sample_share/{name}" in seen_keys


@pytest.mark.parametrize("target_bin", [3, 4])  # last bin of clip 0, first bin of clip 1
def test_adaptive_bin_lands_in_its_clip(cmd, target_bin):
    ratio = cmd.cfg.adaptive_uniform_ratio
    cmd.cfg.adaptive_uniform_ratio = 1e-9
    cmd.bin_failed_count.zero_()
    cmd.bin_failed_count[target_bin] = 1.0
    try:
        ids = torch.arange(NUM_ENVS)
        cmd._adaptive_sampling(ids)
        clip = int(cmd.bin_clip[target_bin])
        local = target_bin - int(cmd.clip_bin_starts[clip])
        n_bins, length = int(cmd.clip_bin_counts[clip]), int(cmd.clip_lengths[clip])
        lo, hi = local / n_bins * (length - 1), (local + 1) / n_bins * (length - 1)
        assert (cmd.clip_ids == clip).all()
        assert (cmd.clip_frames >= int(lo)).all() and (cmd.clip_frames <= hi).all()
        assert_rows_inside_own_clip(cmd)
    finally:
        cmd.cfg.adaptive_uniform_ratio = ratio
        cmd.bin_failed_count.zero_()


def test_smoothing_stops_at_clip_end(cmd):
    """With a 3-bin look-ahead kernel, failures at the start of clip 1 must not raise the end of clip 0."""
    kernel, index = cmd.kernel, cmd._kernel_index
    lam = cmd.cfg.adaptive_lambda
    cmd.kernel = torch.tensor([lam**i for i in range(3)])
    cmd.kernel = cmd.kernel / cmd.kernel.sum()
    cmd._kernel_index = kernel_index(cmd.clip_bin_counts, 3)
    cmd.bin_failed_count.zero_()
    cmd.bin_failed_count[4] = 1.0  # first bin of clip 1
    try:
        p = cmd._sampling_probabilities()
        floor = p[0]  # clip 0, far from any failure
        assert torch.allclose(p[:4], floor.expand(4)), "clip 0's bins got credit for clip 1's failure"
        assert p[4] > floor
        # mjlab's whole-file smoothing would have raised bins 2 and 3 (they look ahead into bin 4):
        flat = cmd.bin_failed_count + cmd.cfg.adaptive_uniform_ratio / cmd.bin_count
        padded = torch.nn.functional.pad(flat[None, None], (0, 2), mode="replicate")
        mjlab_style = torch.nn.functional.conv1d(padded, cmd.kernel.view(1, 1, -1)).view(-1)
        assert mjlab_style[3] > mjlab_style[0]
    finally:
        cmd.kernel, cmd._kernel_index = kernel, index
        cmd.bin_failed_count.zero_()


def test_single_clip_matches_mjlab(env, cmd, tmp_path):
    """A file with no clip table is one clip, and samples exactly like mjlab's MotionCommand."""
    with np.load(MOTION) as data:  # clip 0 only, saved in upload-motion's plain format
        n0 = int(data["clip_lengths"][0])
        keys = ("fps", "joint_pos", "joint_vel", "body_pos_w", "body_quat_w", "body_lin_vel_w", "body_ang_vel_w")
        np.savez(tmp_path / "motion.npz", **{k: data[k] if k == "fps" else data[k][:n0] for k in keys})

    multi_cfg = dataclasses.replace(cmd.cfg, motion_file=str(tmp_path / "motion.npz"))
    plain_cfg = MotionCommandCfg(**{f.name: getattr(multi_cfg, f.name) for f in dataclasses.fields(MotionCommandCfg) if f.init})
    multi, plain = MultiMotionCommand(multi_cfg, env), MotionCommand(plain_cfg, env)
    assert multi.num_clips == 1 and multi.bin_count == plain.bin_count

    ids = torch.arange(NUM_ENVS)
    failures = torch.rand(plain.bin_count)  # a non-uniform failure history
    plain.bin_failed_count[:] = failures
    multi.bin_failed_count[:] = failures
    for seed in range(5):
        torch.manual_seed(seed)
        plain._adaptive_sampling(ids)
        torch.manual_seed(seed)
        multi._adaptive_sampling(ids)
        assert torch.equal(plain.time_steps, multi.time_steps)
        torch.manual_seed(seed)
        plain._uniform_sampling(ids)
        torch.manual_seed(seed)
        multi._uniform_sampling(ids)
        assert torch.equal(plain.time_steps, multi.time_steps)


def test_lean_loader_matches_mjlab(cmd):
    """LeanMotionLoader holds exactly mjlab's tracked-body tensors (it only skips the full-body copies)."""
    lean, full = cmd.motion, MotionLoader(str(MOTION), cmd.body_indexes, device="cpu")
    assert isinstance(lean, LeanMotionLoader) and lean.time_step_total == full.time_step_total
    for key in ("joint_pos", "joint_vel", "body_pos_w", "body_quat_w", "body_lin_vel_w", "body_ang_vel_w"):
        assert torch.equal(getattr(lean, key), getattr(full, key)), key
    assert not hasattr(lean, "_body_pos_w")
