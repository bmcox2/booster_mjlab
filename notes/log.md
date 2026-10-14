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

## 2026-10-14: gesture data pipeline (milestone 1, phases A–C)

**Plan:** A. source gesture data → B. retarget to K1 with GMR → C. verify in booster-mjlab + upload → D. train (LAFAN baseline first, then gesture) → E. expand to 5–10 gestures. A–C need no GPU.

**Data source decision**
- Kept AMASS + HumanML3D for milestone 1: clean mocap, SMPL-X (GMR's native input), text labels make clips searchable
- Limitation: AMASS gestures are deliberate (wave, point), not natural co-speech beats. Fine for proving the pipeline; BEAT2 still the plan for speech-timed gestures

**Coverage check (before downloading AMASS)**
- Cloned HumanML3D to ~/robotics/data/HumanML3D, grepped texts for wave/point/shrug/nod/clap/gesture
- ~1,260 AMASS clips matched (raw wc doubled by mirrored M* files; humanact12's 121 excluded, not AMASS)
- Hits per subset: KIT 357, BMLmovi 256, Eyes_Japan 237, CMU 221, HDM05 84, rest small
- BMLmovi is clean (~22/25 sampled are standing wave/clap/point). Eyes_Japan noisier (walking, compound, acted) but has some conversational gestures → save for milestone 2 variety
- Helper files: hits.txt, hits_by_subset.txt in ~/robotics/data/HumanML3D

**Downloads + setup**
- Layout: code in ~/projects/ (GMR, booster-mjlab), data in ~/robotics/data/ (HumanML3D, amass, k1_motions)
- SMPL-X v1.1 body models (neutral/female/male, NPZ + PKL) → ~/projects/GMR/assets/body_models/smplx/. Skipped the `ext` edit in smplx/body_models.py since .npz files are there; revisit only if loading fails
- AMASS BMLmovi (SMPL-X G) → ~/robotics/data/amass/BMLmovi/
- GMR in its own uv venv (Python 3.10) at ~/projects/GMR/.venv. Import works; harmless warnings (torch.jit deprecation, xrobotoolkit not found)
- GMR's `booster_k1` → K1_serial.xml (serial ankles). booster-mjlab has serial and `-Parallel` tasks; LAFAN K1 dataset uses parallel. Plan: train on plain `Mjlab-Tracking-Flat-Booster-K1`

**Wave candidates (BMLmovi, standing right-hand waves)**

| HumanML3D ID | AMASS file | Frames @20fps |
|---|---|---|
| 000113 | Subject_73_F_MoSh/Subject_73_F_15 | 0–81 (~4.0 s) |
| 000508 | Subject_87_F_MoSh/Subject_87_F_18 | 0–77 (~3.9 s) |
| 001104 | Subject_29_F_MoSh/Subject_29_F_6 | 0–60 (3.0 s) |

- Retargeted all three: `scripts/smplx_to_robot.py --robot booster_k1` → ~/robotics/data/k1_motions/wave_<id>.pkl. All looked good in GMR's viewer
- Gotcha: first attempt reused one save path, runs overwrote each other. Re-ran with a unique filename per clip
- **000508 = first training gesture** (slower, smoother → easier to track, less balance disturbance)
- 001104: faster wave, keep as later "fast wave" variant (speed vs tracking error)
- 000113: dropped, near-duplicate of 000508

**Upload**
- wave_000508.pkl → artifact `bmcox2-university-of-illinois-urbana-champaign/motion_upload/wave_000508-tracking:v0` (WandB run `dgtoro9t`)
- Train command for next GPU session (after LAFAN baseline):
  `uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name bmcox2-university-of-illinois-urbana-champaign/motion_upload/wave_000508-tracking:v0 --env.scene.num-envs 4096`

**Still to do**
- [ ] Check wave_000508.pkl in booster-mjlab `visualize-motions` before training (only check on serial-ankle/joint order)
- [x] Upload wave_000508.pkl (artifact above)
- [ ] Read docs/motion_preparation.md to confirm which K1 variant it expects from GMR clips
- [ ] Next GPU session: LAFAN walking-clip tracking baseline, then train on wave_000508
- [ ] Metrics: tracking error + falls over 50 rollouts

## Next
- `visualize-motions` check on wave_000508, then LAFAN tracking baseline → train on wave_000508
- Ask lead: club GPU access; which K1 ankle model (standard vs `-Parallel`)
