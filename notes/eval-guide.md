# Evaluating a Tracking Policy (`eval-tracking`)

Training charts tell you whether a run is *learning*. The eval tells you whether the result *works*:
does the K1 play the whole gesture without falling, every time, and how closely?

## Run it
```
uv run eval-tracking --wandb-run-path bmcox2-university-of-illinois-urbana-champaign/mjlab/<run-id>
uv run eval-tracking --wandb-run-path ... --push                       # stress test: training pushes on
uv run eval-tracking --wandb-run-path ... --checkpoint-name model_2000.pt  # an earlier checkpoint
uv run eval-tracking --wandb-run-path ... --registry-name <entity>/motion_upload/<clip>-tracking:vN  # other clip
```
Takes seconds. Results print and save to `logs/eval/<run>_<checkpoint>_<motion>[_push].json`.

## What one eval does
- 50 robots run in parallel, one rollout each, frame 0 → last frame of the clip.
- Each robot has its own randomized physics (friction, motor gains, masses, encoder bias) and a
  slightly jittered start pose (±0.1 rad per joint): 50 tries on 50 slightly different robots.
- No pushes, no sensor noise (unless `--push`).
- **Fail** = the task's own termination checks fire before the clip ends (trunk height/tilt, or a
  hand/foot height, off by more than the training thresholds; e.g. 25 cm in height).
- Errors skip the first 0.5 s (`--settle-s`): the jittered start makes the hands jump ~15 cm while
  the robot catches up. Failures still count from step 0.

## Reading the output
| Line | Meaning | Good (wave_000508, 4zzjocm6) |
|---|---|---|
| Full clip, no falls | k/50 that finished. Milestone 1 needs 50/50 | 50/50 |
| 95% confident ≥ X% | With 50 tries, 50/50 only proves the true rate is ≥ ~93%. Want more certainty → more rollouts | 92.9% |
| failures by reason | Which check fired, and when (`ee_body_pos` = hand/foot, `anchor_pos` = trunk height, `anchor_ori` = trunk tilt) | none |
| hand position error | How far the hands are from the reference: the gesture quality | 2.1 cm mean, 8.4 cm worst |
| all-body position err | Same as training's `error_body_pos`, in cm | 1.3 cm |
| joint angle error | Mean per joint, split into arms / head / legs | 1.7 / 1.8 / 3.3° |
| trunk height vs ref | Negative = robot stands lower than the reference | −1.1 cm |
| drift across floor | How far the trunk wandered from the reference by the end | 2.4 cm |
| max foot tilt on floor | Worst sole tilt while a foot is on the floor. >10° = standing on an edge | L 1.6°, R 23.1° (rolled) |

Hand/body errors are measured after re-anchoring the reference to the robot's current position and
heading (like training), so slow drift shows up only in the drift line, not twice.

## Combined (multi-clip) motion files
A file built by `combine-motions` is evaluated **clip by clip**: 50 robots per clip, all clips at once,
each robot counted only until the end of its own clip. Output is one row per clip (same columns as
above) plus `All clips: k/N pass`. For a single clip you get the detailed block above.
```
uv run eval-tracking --wandb-run-path ... --motion-file logs/motions/waves_2clip.npz   # every clip
uv run eval-tracking --wandb-run-path ... --clips wave_000508 wave_001104             # some clips
```
The JSON has `clips` (one summary per clip) and `rollouts` (each tagged with its `clip`). Episode
length is set from the longest clip, so long clips are never cut short. More: `multi-clip.md`.

## Comparing runs
Evaluate both on the **same motion version** (`--registry-name ...:vN`); otherwise you compare clips,
not policies. Compare the JSON `summary` blocks, or just the printed tables.

## Why these choices
- **Parallel envs instead of 50 sequential episodes:** same result, ~50× faster; each env is an independent try.
- **Play config, not training config:** training starts mid-clip with random pose/velocity kicks so
  the policy learns recovery; the milestone question is "start to finish, as performed".
- **Keep physics randomization:** without it all 50 rollouts are identical, and 50/50 would mean nothing.
- **Reuse the training terminations as the fail test:** they are exactly what the policy was trained
  to avoid, and they catch falls (a fall drops the trunk / hands by far more than 25 cm).
- **Hand error is the headline quality number:** for a gesture, where the hands go is what a viewer sees.
