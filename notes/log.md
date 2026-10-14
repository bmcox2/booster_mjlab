# K1 Co-Speech Gesture Project: Run Log

## 2026-10-13: booster_mjlab setup + first velocity training

**Setup**
- Ubuntu 24.04, RTX 4070 Laptop (8 GB), NVIDIA driver 595.84 / CUDA 13.2
- Installed uv, cloned IntelligentRoboticsLab/booster-mjlab
- `uv run list_envs` → 41 tasks, including `Mjlab-Tracking-Flat-Booster-K1`
  and `Mjlab-Velocity-Flat-Amp-DA-Muon-Booster-K1`

**WandB setup issues (resolved)**
- `entity bmcox2 not found` → username is not a valid run entity
- `may not log runs directly to your organization` → `-org` name is the org, not the team
- Fix: `WANDB_ENTITY=bmcox2-university-of-illinois-urbana-champaign` (team name), set in ~/.bashrc

**Run 1: velocity, 1024 envs**
- `uv run train Mjlab-Velocity-Flat-Amp-DA-Muon-Booster-K1 --env.scene.num-envs 1024`
- ~1.0 s/iteration, GPU ~62°C, 2.2 GB VRAM, power capped at 35 W
- Ran a few minutes only (pipeline test)

**Run 2: velocity, 4096 envs**
- `uv run train Mjlab-Velocity-Flat-Amp-DA-Muon-Booster-K1 --env.scene.num-envs 4096`
- WandB run: `2wagxxko`
- ~3k iterations (~2.5 hr), stopped manually
- Results:
  - mean_reward: ~0 → ~30, flattening
  - mean_episode_length: maxed at ~1000 by ~2k iterations
  - illegal_contact / fell_over: → ~0; time_out rising
  - track_linear_velocity ~1.1, track_angular_velocity ~1.0, still rising slowly
  - style_reward (AMP): plateaued ~2
  - Policy/mean_std: 1.0 → ~0.44, stable (still exploring)
  - Curriculum step at ~1k iterations (soft_landing drop, reward plateau then second climb)
  - Penalty terms grew more negative, expected with longer episodes and faster commanded speeds
- Verdict: healthy run, good baseline
- In `play`: ___ (walks without falling? follows forward/back/side/turn commands? gait natural?)

**Reference data**
- Velocity task does NOT imitate a specific clip. Commands set the goal, AMP sets the style
- AMP reference: whirlwind-ams/lafan_locomotion_k1 (7 LAFAN1 walk/run clips retargeted to K1)
- Viewed with `uv run visualize-motions --dataset whirlwind-ams/lafan_locomotion_k1 --task Mjlab-Velocity-Flat-Amp-DA-Muon-Booster-K1`

**Notes / takeaways**
- Laptop GPU power-capped at 35 W; try Ubuntu Performance power mode
- Keep long runs off the laptop when possible (overheating history); club GPU for full runs

## 2026-10-14: repo + VS Code setup
- Forked to bmcox2/booster_mjlab via `gh repo fork --remote` (origin = fork, upstream = IntelligentRoboticsLab)
- Working branch: `gesture-tracking` (main kept matching upstream)
- Added `data/` to .gitignore (logs/ and wandb/ already ignored)
- VS Code opened on repo, interpreter set to `.venv/bin/python`

## Next
- Tracking task on one LAFAN clip: download dataset → `upload-motion` → train `Mjlab-Tracking-Flat-Booster-K1`
- Ask lead: club GPU access; which K1 ankle model (standard vs `-Parallel`)