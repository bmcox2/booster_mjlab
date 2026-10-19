# Multi-Clip Tracking (`MultiMotionCommand`)

One policy that tracks many reference clips, instead of one policy per clip. This is roadmap step 1
(the general tracker). Code: `src/booster_mjlab/tasks/tracking/multi_motion_command.py`.

## Why
DeepMimic trained one policy per clip, and so far so have we (one run per wave). To follow motion it
has never seen (BEAT2 speakers, then EMAGE output), a policy has to train on many clips. Proof that a
one-clip policy doesn't transfer: `e2p0f89y` (trained on `wave_000508`) passes 50/50 on its own clip
but **1/50 on `wave_001104`**, a different wave.

## Workflow
```
uv run combine-motions <entity>/motion_upload/wave_000508-tracking:v3 \
    <entity>/motion_upload/wave_001104-tracking:v2 --artifact-name waves-2clip
uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name <entity>/motion_upload/waves-2clip:v0 --env.scene.num-envs 4096
uv run eval-tracking --wandb-run-path <entity>/mjlab/<run-id>        # one row per clip
```
`combine-motions` takes W&B artifacts, local tracking `.npz` files, or grounded GMR `.pkl` clips (any
mix). `--no-upload --output <file>.npz` builds a local file only; train on it with
`--env.commands.motion.motion-file <file>.npz`. Same task, same train command: a plain single-clip
artifact still works and behaves exactly as before.

## The combined file
upload-motion's format (`fps`, `joint_pos`, `joint_vel`, `body_*_w`), with every clip's frames
concatenated end to end, plus a clip table:

| Key | Example (waves_2clip) |
|---|---|
| `clip_lengths` | `[188, 147]` frames (at 50 fps) |
| `clip_names` | `["wave_000508", "wave_001104"]` (used in W&B metric names) |
| `clip_sources` | the artifact or file each clip came from |

```
row:      0 ........................ 187 | 188 ................... 334
          wave_000508 (188 frames)       | wave_001104 (147 frames)
          clip_starts[0] = 0             | clip_starts[1] = 188
```

## How it works
**Per-robot state:** `clip_ids` (which clip) and `clip_frames` (frame within that clip). The row a
robot reads is `clip_starts[clip_id] + frame`, written into mjlab's own `time_steps`. Every reference
lookup in mjlab goes through `time_steps` (`joint_pos`, `body_pos_w`, `anchor_*`...), so observations,
rewards, terminations, metrics, the viewer ghost and the ONNX export all read the right frame without
being changed.

**End of a clip:** when a robot's frame reaches its clip's length, it is resampled: teleported to a
new start, the same way mjlab handles the end of its single clip. It never steps into the next clip.
(Stepping from frame 187 to row 188 would mean jumping from the end of one wave into the middle of a
different motion: a teleporting reference.)

**Picking starts** (DeepMimic's *reference state initialization*: start episodes at random points in
the clip, not only at frame 0):
- `uniform`: a uniformly random row of the whole file, then look up its clip. Same draw as mjlab.
- `adaptive` (training default, from BeyondMimic): mjlab cuts the clip into ~1 s bins, counts recent
  failures per bin, and starts more robots in bins where robots fail. Here **each clip gets its own
  bins** (`wave_000508` 4, `wave_001104` 3: 7 bins total) in one shared distribution. A sampled bin
  gives both the clip and the frame. The smoothing kernel (when `adaptive_kernel_size` > 1) looks
  ahead only within the same clip, so failures at the start of one clip don't push starts toward the
  end of the clip before it.
- `start` (play and eval): frame 0 of the robot's clip. At the end of a clip the robot moves on to the
  next clip, so `play` shows all clips in order. Robot *i* starts on clip *i* mod (number of clips).

**Weighting:** with no failures, every bin is equally likely, so a clip gets starts in proportion to
its length. A 60 s BEAT2 take gets ~20× the starts of a 3 s wave. Adaptive sampling then shifts starts
toward clips that fail. If short gestures get neglected when mixed with long talking clips, this is
the knob to change (e.g. weight clips equally).

**One bad clip can take over (run `0lg80c7d`).** A bin's weight is its recent failures *per step*
(more envs → more failures) plus a uniform floor, `adaptive_uniform_ratio / bins` (total floor = the
ratio). With mjlab's 0.1 and 4096 envs, one clip whose reference teleports (a GMR IK jump, never
trackable) got 70–77% of all starts for 30k iterations; the other 105 clips got ~0.2% each instead of
~0.9%, and the run plateaued at ~2.5k iterations. Fixes: the `joint jump` severe QC flag in
`tools/beat2_batch.py` drops such clips, and the K1 config sets `adaptive_uniform_ratio = 1.0`.
**Watch `Metrics/motion/sampling_top1_prob`**: if it sits far above 1/(number of bins), check which
clip's `sample_share` is high and look at that clip.

## Diff from mjlab's `MotionCommand`
mjlab stays pinned and unedited; `MultiMotionCommand` subclasses it.

| Method | mjlab does | Changed |
|---|---|---|
| `__init__` | Loads the file (`MotionLoader`), `time_steps = 0`, ~1 s bins over the whole file | Calls mjlab's init (frames loaded once), then reads the clip table and rebuilds bins **per clip** |
| `_uniform_sampling` | Random row of the file | Same draw; also records the clip and frame |
| `_adaptive_sampling` | Bin by failures → random frame in bin | Bins per clip; failures binned by (clip, frame); smoothing stops at clip ends; failures added (`+=`) instead of assigned |
| `_resample_command` | Pick a frame by mode, teleport onto it with small random offsets | Only the frame picking (`start` = frame 0 of *own* clip, where mjlab used frame 0 of the file). Teleport code copied unchanged |
| `_update_command` | +1 frame; past the end of the **file** → resample; refresh; EMA of failures | +1 frame within the clip; past the end of **its clip** → resample (`start` mode: next clip). Rest unchanged |
| `reset` | Logs metric means over resetting robots, then resamples | Adds per-clip metrics, computed before the robots change clip |
| `reset_to_frame` | Exact reference state at a row (viewer scrubber) | Also records which clip that row is in |

Unchanged: the policy network, observations (the policy sees the next reference frame, not a clip ID),
rewards, terminations, PPO settings, the ONNX export.

`_resample_command` is overridden whole because mjlab's `start` branch hard-codes `time_steps = 0`
inside the same method as the teleport, so the teleport half can't be reused on its own.

## Per-clip metrics in W&B
Only logged when the file has 2+ clips. Search the charts for `clip/` (or `clip/error_body_pos` to put
all clips' charts side by side).

| Key | Meaning | Read it as |
|---|---|---|
| `Metrics/motion/clip/error_body_pos/<clip>` | Same as `error_body_pos`, only for robots on that clip | Which clips the policy tracks worst |
| `Metrics/motion/clip/error_joint_pos/<clip>` | Same, joint angles | |
| `Metrics/motion/clip/error_anchor_pos/<clip>` | Same, trunk position vs reference | Balance/drift trouble on that clip |
| `Metrics/motion/clip/fail_rate/<clip>` | Of that clip's episode endings, the fraction that were falls/terminations (not time-outs) | Should drop toward 0 for every clip |
| `Metrics/motion/clip/sample_share/<clip>` | Chance a new start lands on this clip right now | Rises above its length share when adaptive sampling is focusing on a hard clip |

How the numbers are made (same as mjlab's own `Metrics/motion/*`): when a robot's episode ends, the
error *at that moment* is recorded, averaged over the robots on each clip that reset that step, then
averaged over the iteration. Episodes that end in a fall end with a big error, so `error_*` mixes
"how well" and "how often it fails". Read errors together with `fail_rate`.

Healthy multi-clip run: every clip's `fail_rate` → ~0 and its errors flatten. One clip staying high
while the others drop = that clip is hard (or the data is bad); its `sample_share` should be rising.
With many clips (hundreds of BEAT2 takes) each clip gets only a few resets per iteration, so its
curves are noisy; smooth them in W&B.

## Sampling safety harness

Adaptive sampling weights each ~1 s bin by its recent falls plus a floor (`adaptive_uniform_ratio / bins`). The floor sums to 1.0 over *all* bins while the falls sum to hundreds, so in practice there is no floor, and it is a feedback loop: more starts on a bin → more falls there → more starts. One bad clip can take over (`0lg80c7d`: `wayne_0_9_9` 70–77% of starts; 10-19 full-A: one second of `lawrence_0_101_101_t42-55`, a 0.46 rad shoulder jump, 39%; reward and episode length crashed from ~it 200).

The harness (`limit_clip_shares`, `MultiMotionCommandCfg`):
- **Cap:** a clip gets at most `max_clip_share_ratio` (20) × its length share of starts (full BEAT2, 13 s clip: ~0.3%). Mass over the cap goes to the other clips in proportion. A real hard clip still gets 20× practice.
- **Quarantine:** a clip held at its cap for `quarantine_after_steps` (2400 steps ≈ 100 iterations) in a row is quarantined: its fall counts are cleared and it is sampled at `quarantine_share_ratio` (1.0) × its length share for the rest of the run (0 = never start there). A clean hard clip gets learned and drops below the cap; a broken one stays there.
- **Review list:** each quarantine prints `[sampler] Quarantined <clip> ... most falls near X s` and is written to `flagged_clips.json` next to the checkpoints (and the W&B run's files). Look at those seconds in `visualize-motions`; fix or drop the clip in the next dataset build.
- **W&B:** `Metrics/motion/sampling_top1_clip_share` (biggest clip's share of starts), `sampling_capped_clips`, `sampling_quarantined_clips`. A rising quarantined count means the dataset has problems Gate 1 missed.
- Off: `max_clip_share_ratio = inf` and `quarantine_after_steps = 0`. Quarantine state is not in checkpoints: a resumed run re-detects.

## Eval
`eval-tracking` on a combined file gives one row per clip (see `eval-guide.md`). It sets the episode
length from the longest clip (+1 s), so long clips are never cut short.

(Correction to the 2026-10-16 log: eval loads the *play* config, which already sets the episode length
to ~infinity, so long single clips were never cut short. The explicit setting just makes that not
depend on play mode.)

## Tests
`uv run --with pytest pytest tests/test_multi_motion.py -q` (CPU, ~2 min; needs
`logs/motions/waves_2clip.npz`, see the test file's docstring). Checks:
- every robot's row stays inside its own clip, with only +1 steps or a resample at the clip's last
  frame (command-only, 600 steps × 64 robots, all three modes; and full env steps with random actions,
  so falls and resets mix in)
- an adaptive bin always samples inside its own clip; smoothing doesn't leak across clips
- with one clip, the samples equal mjlab's `MotionCommand` exactly (same seeds)
- per-clip metrics reach the log

Checked that the boundary test fails if the wrap is put back to mjlab's "end of the file".

## Limits
- **ONNX export** bundles all clips concatenated; on the robot, the time step fed to it must be the
  row (`clip start + frame`). Fine for now (sim only).
- **Viewer scrubber** moves over rows of the whole file; "Start Here" works (it knows the clip), but
  scrubbing while paused shows rows without changing the robot's clip.
- Clip names become W&B keys: keep them short and unique (`combine-motions --names`).
