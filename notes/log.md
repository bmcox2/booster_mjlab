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

## 2026-10-15: first gesture tracking run + floor-offset fix

**Run: wave_000508 tracking (pre-fix clip)**
- Task `Mjlab-Tracking-Flat-Booster-K1`, 1024 envs, motion `wave_000508-tracking:v0`
- WandB run: `w77drafm` (2026-10-15_18-56-22)
- 2,559 of 5,000 max iterations in ~36 min, then stopped manually
- **GPU speed: ~0.84 s/iteration, ~31–37k env-steps/s.** Fast enough to iterate on the laptop (vs ~1.0 s/it for the velocity task at 1024 envs)
- Results (final values):
  - mean_reward: 5.8 → 58.8, still creeping up slowly after ~800 iterations
  - mean_episode_length: 500 (max) from ~800 iterations on
  - Terminations: anchor_pos / ee_body_pos → ~0 after ~800 iterations; nearly all episodes end by time_out
  - error_body_pos 0.189 → 0.052 m; error_anchor_pos 0.425 → 0.105 m; error_joint_pos 0.42 rad
  - Policy/mean_std: 0.62 → 0.18
- Verdict: learns to track the clip without falling, but it trained on the **sunk v0 clip** (see below). Part of the ~0.1 m anchor error is probably the ~6.7 cm height offset the robot can't physically match. Treat this as a "before" baseline, not the milestone result
- In `play`: ___

**Problem: retargeted clips sit below the floor**
- GMR K1 clips put the robot's lowest collision point 6.0–6.5 cm below the floor (wave_000508 −6.52, wave_000113 −6.05, wave_001104 −6.42 cm; lowest part is always the foot mesh)
- Cause, in part: GMR retargets with its own `K1_serial.xml`; in booster-mjlab's `k1.xml` the legs attach 1.5 cm lower (checked by running FK on both models with the same pose: head/arms/trunk match exactly, every leg body is 1.5 cm lower)
- A fixed guess (`shift_height.py`, +2 cm) was far too small, so it was deleted

**Fix: `tools/ground_clip.py`**
- Runs forward kinematics on booster-mjlab's `k1.xml` (the model training uses), finds the lowest collision point over the whole clip, and shifts root z so it touches the floor. Measured per clip, not guessed
- First version used each part's bounding box, which overestimates the drop when a foot tilts (2.6 / 4.0 / 12 mm on 508 / 113 / 1104), so grounded clips hovered slightly. Now computes each shape's lowest point exactly (sphere/capsule/cylinder/box/ellipsoid/mesh vertices) and prints which part is lowest
- Verified: joint mapping matches (22 joints, 4 renamed); re-running on a grounded clip gives a 0 shift; MuJoCo's `mj_geomDistance` to a floor plane gives 0.00 mm on all three grounded clips
- Magenta spheres in the training viewer are `foot_height_scan` ray hits, not contact geoms (K1 feet are meshes)
- Batch mode: `uv run python tools/ground_clip.py ~/robotics/data/k1_motions [--upload] [--force]`
  - writes `<name>_grounded.pkl`, skips clips already up to date
  - `--upload` names the artifact after the original clip, so the fixed wave becomes `wave_000508-tracking:v1`
- Documented in `docs/motion_preparation.md` ("Ground the clips first")
- Moved a stray manual-shift clip `wave_000508_z.pkl` to Trash

**Takeaways**
- Always ground GMR clips before uploading; never train on raw `.pkl` uploads
- Pin artifact versions explicitly (`:v1`) in `--registry-name` so runs record which clip they used

## 2026-10-15: wave_000508 tracking on grounded clip (run 4zzjocm6)

**Run**
- `uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name bmcox2-university-of-illinois-urbana-champaign/motion_upload/wave_000508-tracking:v2 --env.scene.num-envs 1024`
- WandB run: `4zzjocm6` (2026-10-15_20-15-14), finished all 5,000 iterations in 61 min (~0.73 s/it, ~35k env-steps/s)
- Motion versions: `:v1` = first ground_clip (bounding boxes, hovered 2–6 mm), `:v2` = exact ground_clip (floor gap 0.0 min / 2.8 median / 4.3 max mm). This run used `:v2`

**Results (final; vs w77drafm on sunk v0)**
- mean_reward 64.7 (vs 58.8); flat since ~2k iterations (63.7 → 64.7 over the last 3k)
- mean_episode_length 500 (max) from ~900 iterations; anchor_pos / anchor_ori / ee_body_pos terminations ~0
- error_body_pos 0.016 m (vs 0.052, ~3× better); error_anchor_pos 0.080 m (vs 0.105); error_joint_pos 0.35 rad (vs 0.42)
- mean_std 0.78 → 0.17, smooth; value loss ~0.003
- Verdict: **done**. Learned, stable, no falls; more iterations won't help much

**Height check ("robot looks too high")**
- Headless rollout of `model_4999.pt`, 64 envs × 550 steps, play config: 0 resets
- Simulated trunk is **1.1 cm lower** than the reference (p10–p90: −1.2 to −1.0 cm); trunk xy drift 2.4 cm mean
- Not a grounding bug: v2 reference touches the floor exactly; simulated feet sink only ~1 mm into the floor (normal soft contact)
- Cause: the reference feet are **tilted 6–9° the whole clip** (GMR retargeting artifact), so the clip stands on foot edges. The policy plants the left foot flat (0.2°) and sits ~1 cm lower. It also rolls the right foot more than the reference (16.5° vs 9.1°; Right_Ankle_Roll −0.12 rad)
- Largest joint errors: Left_Knee_Pitch +0.17, Right_Ankle_Roll −0.12, Left_Hip_Pitch −0.11 rad (legs, not arms)

**Takeaways**
- Grounding fixed the big error (6.5 cm sink → body error 3× lower). The remaining 1 cm gap comes from tilted feet in the retargeted clip
- Arms (the gesture) track well; remaining error is in leg/foot posture

## 2026-10-15: foot flattening in ground_clip.py

**Problem**
- `play` on 4zzjocm6 confirmed the right foot (under the waving arm) rolls onto its outer edge: 16.5° mean, 25° max
- Cause is the data: GMR copies the human foot angle, so every wave clip stands on tilted feet (6–12°)

**Fix: `tools/ground_clip.py` now flattens stance feet (default; `--keep-foot-tilt` to skip)**
1. Re-solve ankle pitch/roll per frame so each sole is level (feet near the floor only; blended for feet in the air)
2. Ground the clip (exact lowest point, as before)
3. Flat feet can hover (wave_000508 right foot: 9.5 mm) on a nearly straight leg that can't reach further. So: lower the trunk by one constant amount for the clip (+3 mm margin), then leg IK bends each knee so both feet sit on the floor
- Bugs hit on the way: lowering the hovering foot directly diverged (straight leg can't extend); IK found a backwards knee (−0.31 rad) → start knee bent + clamp to limits; per-frame trunk drop caused knee jitter (1.6° ↔ 12° on 000113) because near a straight knee a tiny height change needs a big angle change → constant drop + margin

**Result (all three wave clips)**

| Clip | Foot tilt before → after | Trunk lowered | Knees after |
|---|---|---|---|
| wave_000508 | L 6.2°/R 9.1° → 0.0° | 13.5 mm | L ~28°, R ~16° |
| wave_000113 | L 9.1°/R 5.0° → 0.0° | 7.2 mm | ~15–21° |
| wave_001104 | L 7.8°/R 9.0° → 0.0° | 11.4 mm | ~16–27° |

- Verified with MuJoCo (`mj_geomDistance` to a floor plane): both feet 0.00 mm gap every frame, no other part below the floor; upper-body joints and trunk rotation unchanged; foot xy unchanged; all joints in limits; joint jitter ≤ original GMR clips
- Trade-off: the reference now stands with bent knees, ~1 cm lower. The 4zzjocm6 policy bent its knees on its own anyway

## Next
- Re-ground real clips with flattening, check in `visualize-motions`, upload (wave_000508 → `:v3`)
- Retrain on `:v3`; compare to 4zzjocm6 (right-foot roll, leg joint errors, height gap); check feet in `play`
- 50-rollout eval on the better run (milestone 1 metric)
- Phase E: train wave_001104, then find more gestures
- Ask lead: club GPU access; which K1 ankle model (standard vs `-Parallel`)
