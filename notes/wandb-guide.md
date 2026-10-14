# Reading Training Runs in WandB

How to tell whether a run is learning, done, stuck, or broken. Written for the booster_mjlab K1 tasks; metric names may differ slightly between tasks, so use the chart search box.

## WandB basics
- **Run list (left):** eye icon shows/hides a run on the charts. Use it to compare runs.
- **Sections:** charts are grouped by the prefix before `/` (`Train/`, `Episode_Reward/`, `Episode_Termination/`, `Loss/`...).
- **Smoothing (gear icon):** set ~0.6–0.8. The faint line behind is raw data.
- **X-axis:** `Step` = training iteration. Use **Relative Time (Wall)** to compare runs fairly (e.g. 1024 vs 4096 envs).
- **Run path for `play`:** from the URL `.../<entity>/<project>/runs/<id>` → `--wandb-run-path <entity>/<project>/<id>` (drop `runs/` and any `?...`).

## Tier 1: Is it learning?
| Chart | Healthy | Warning |
|---|---|---|
| `Train/mean_reward` | Climbs fast, then slows and flattens | Flat from the start; or climbs then crashes and stays down |
| `Train/mean_episode_length` | Rises to the episode cap (~1000 steps) and stays | Stays short (robots keep failing early) |

## Tier 2: How is it failing?
`Episode_Termination/*` shows why episodes end.
- `time_out`: reached the time limit. **The good ending.** Should rise.
- `fell_over`: should drop to ~0.
- `illegal_contact`: knees/torso touching the ground. Should drop to ~0.

## Tier 3: Is it doing the task well?
- **Velocity task:** `Metrics/twist/error_vel_xy`, `error_vel_yaw`: lower is better.
- **Tracking task:** per-body / per-joint tracking errors: lower is better.
- `Episode_Reward/*`: one chart per reward term.
  - Positive terms (tracking, `upright`) should rise.
  - Penalty terms (`foot_slip`, `action_rate_l2`, `self_collisions`...) are negative and small. They often get *more* negative as episodes get longer and commands get harder; that is normal if their size stays small next to total reward.
- `Episode_Metrics/Amp/style_reward` (AMP tasks): how human-like the motion looks. Should rise, then plateau.
- `Curriculum/*`: difficulty increases automatically. A step here often causes a temporary reward dip.

## Tier 4: Training health (glance)
- `Policy/mean_std` (or entropy): exploration. Should decrease slowly and level off (e.g. 1.0 → ~0.4). Near zero early = stopped exploring.
- `Loss/value_function`: spiky early, settles later.
- `Perf/*`: speed only.

## When to stop
**Done:** reward and episode length flat over the last ~20% of the run; falls/illegal contacts ~0; task error low; **and it looks right in `play`.**

**Stuck (local optimum):** reward flat at a low/middling level while episodes stay short, terminations stay high, or task error stays high; `mean_std` collapsed toward 0; `play` shows a consistent bad habit (standing still, shuffling, knee-walking). More training won't fix it.
- First try a different seed (`--seed 1`). If several seeds get stuck the same way, change the setup (rewards, curriculum, data) and ask the lead.

**Broken:** sudden crash that doesn't recover, `NaN`s, exploding losses. Stop; keep the last good checkpoint.

**Looks bad but is normal:** noisy curves; brief dips at curriculum steps; flat early reward before it "clicks"; bouncy losses.

**Always confirm with `play` before calling a run good.** Reward can look fine while the robot cheats (e.g. stands still collecting `upright` while ignoring commands).

## Checking mid-run
Run `play` in a second terminal while training continues. It loads the latest checkpoint and simulates one robot, so it barely slows training. Don't leave it running.

## Example: healthy velocity baseline (run 2wagxxko, 4096 envs, ~3k iterations)
- mean_reward 0 → ~30, flattening; episode length at cap by ~2k
- illegal_contact ~190 → 0; fell_over → 0
- style_reward plateau ~2; mean_std 1.0 → ~0.44 stable
- Curriculum step at ~1k (reward plateau, then second climb)
