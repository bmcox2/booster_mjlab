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

## 2026-10-15: eval script (`eval-tracking`) + milestone eval of 4zzjocm6

**Built** `src/booster_mjlab/scripts/eval_tracking.py` (entry point `uv run eval-tracking`); guide in `notes/eval-guide.md`
- 50 parallel rollouts, frame 0 → last frame, play config (no pushes / obs noise) but per-robot physics randomization + ±0.1 rad start jitter
- Fail = task terminations fire before clip end; reports success k/n with 95% lower bound, failure reasons/times, hand/body/joint errors, height, drift, foot tilt; saves JSON to `logs/eval/`
- Bugs caught while validating: ran one step past the clip end (motion wrapped → robots teleported, drift read 0.0) → stop at the last frame; start-pose jitter made hands jump ~16 cm in the first 5 steps → errors skip first 0.5 s
- Checks: untrained `model_0.pt` fails 50/50 at ~0.6 s (`ee_body_pos`); numbers match an independent rollout (height −1.1 cm, drift ~2.4 cm)

**Result: 4zzjocm6 (model_4999) on wave_000508 :v2**
- `uv run eval-tracking --wandb-run-path bmcox2-university-of-illinois-urbana-champaign/mjlab/4zzjocm6`
- **50/50 full clip, no falls → PASS** (95% lower bound 92.9%). With `--push`: also 50/50
- Hands 2.1 cm mean (8.4 cm worst moment); body 1.3 cm; joints arms 1.7° / head 1.8° / legs 3.3°
- Trunk −1.1 cm vs ref; drift 2.4 cm; foot tilt L 1.6°, **R 23.1°** (right-foot roll, the thing `:v3` should fix)

## 2026-10-15: wave_000508 on flattened clip (run me9exatd): milestone bar met

**Run**
- `uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name bmcox2-university-of-illinois-urbana-champaign/motion_upload/wave_000508-tracking:v3 --env.scene.num-envs 1024`
- WandB run: `me9exatd`, stopped at 3,625 iterations (43 min, ~35k env-steps/s). `--agent.max-iterations` wasn't passed, so max was the default 30,000
- `:v3` checked: feet 0.0° tilt, floor gap 0.0 mm; trunk 2.1 cm lower than `:v2` (bent knees)

**Training charts vs 4zzjocm6 (same iteration, smoothed)**
- Learns faster: reward 43.8 vs 39.1 at 250 it; episode length at max by ~500
- Plateau ~2,000 it: reward 64.7–65.0 (4zzjocm6 64.2)
- error_body_pos 0.0105 vs 0.0170 m (−38%); error_joint_pos 0.21 vs 0.35 (−40%); anchor_pos same (~0.085)
- mean_std 0.18, value loss ~0.005: healthy. Verdict: **done**

**Eval (`uv run eval-tracking --wandb-run-path .../me9exatd`, model_3500)**

| | 4zzjocm6 (v2) | me9exatd (v3) |
|---|---|---|
| Full clip, no falls | 50/50 | 50/50 (with pushes 50/50; 300/300 with pushes, seed 1 → ≥98.7%) |
| Hand error mean / worst | 2.1 / 8.4 cm | **1.5 / 5.7 cm** |
| Body error | 1.3 cm | **0.6 cm** |
| Joint error arms / head / legs | 1.7 / 1.8 / 3.3° | 1.4 / 1.6 / **1.3°** |
| Trunk height vs ref | −1.1 cm | **0.0 cm** |
| Drift at clip end | 2.4 cm | 2.4 cm |
| Max foot tilt L / R | 1.6 / **23.1°** | 2.3 / **5.0°** |

**Takeaways**
- Flattening the feet fixed the right-ankle roll (23° → 5°) and the height gap, and improved every tracking error, including the arms
- Lesson: most of the remaining error was in the data, not the RL. Fix the reference before tuning rewards
- wave_000508 meets milestone 1's bar (full clip, no falls, 50 rollouts). `me9exatd` is the keeper policy for gesture 1
- ~2,000–2,500 iterations is enough for a ~4 s gesture at 1024 envs (~30 min)

## 2026-10-16: gesture 2, fast wave wave_001104 (run pqh0whw0): passes

**Run**
- `uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name bmcox2-university-of-illinois-urbana-champaign/motion_upload/wave_001104-tracking:v2 --env.scene.num-envs 1024 --agent.max-iterations 2500`
- WandB run: `pqh0whw0`, 2,500 iterations in 29 min (~36.6k env-steps/s). Clip: 2.9 s, flattened feet (`:v2`)

**Training charts**
- reward 46.0 (250 it) → 62.7 (1k) → 64.0 (2.5k), still creeping up by ~0.1–0.3 per 500 it; episode length at max by ~500
- error_body_pos 0.0108 m, error_joint_pos 0.239 (≈ me9exatd: 0.0105 / 0.21); terminations ~0
- mean_std 0.19, value loss 0.005: healthy. Verdict: **done** (2,500 was enough)

**Eval**

| | wave_000508 (me9exatd) | wave_001104 (pqh0whw0) |
|---|---|---|
| Full clip, no falls | 50/50; 300/300 with pushes | **50/50; 300/300 with pushes** (≥98.7%) |
| Hand error mean / worst | 1.5 / 5.7 cm | 1.7 / 5.8 cm |
| Body error | 0.6 cm | 0.6 cm |
| Joint error arms / head / legs | 1.4 / 1.6 / 1.3° | 1.8 / 1.9 / 1.2° |
| Trunk height vs ref | 0.0 cm | −0.1 cm |
| Drift at clip end | 2.4 cm | 3.1 cm |
| Max foot tilt L / R | 2.3 / 5.0° | 3.0 / 3.3° (push: 5.8 / 4.9°) |

**Takeaways**
- Faster arms cost very little: hands +0.2 cm, arm joints +0.4°; balance unaffected
- The pipeline (GMR → ground_clip with foot flattening → 2,500 it → eval) worked first try on a new clip
- **2 of 5–10 gestures done** for milestone 1

## 2026-10-16: roadmap revised, BEAT2 converter, first club-GPU run (e2p0f89y)

**Roadmap**
- New `notes/roadmap.md`; `notes/plan.md` is now the Slice 0 checklist (old phases A–E are done or superseded)
- Milestone 1 is now "K1 tracks real conversational motion": BEAT2 talking data replaces more isolated AMASS gestures; the two waves are kept for the later semantic layer

**BEAT2 → GMR converter: `tools/beat2_to_gmr.py`**
- Data: 5 Scott takes (5.6 min) in `~/robotics/data/BEAT2/beat_english_v2.0.0/` (`smplxflame_30/`, `wave16k/`)
- BEAT2 format: keys `betas(300)`, `poses(N,165)`, `expressions(N,100)`, `trans`, `model`, `gender`, `mocap_frame_rate`; 30 fps; **Y-up** (AMASS/GMR are Z-up); audio is 16 kHz **32-bit float**
- Fixes to the first draft:
  - betas 10 → **16**: GMR's SMPL-X uses 16; with 10 it crashes in `lbs` (`einsum` size 26 vs 20)
  - Y-up → Z-up: SMPL-X rotates about the pelvis, so `trans` must be rotated as `fix(trans + j0) - j0`; rotating `trans` alone put the body ~36 cm below the floor (j0 read from `SMPLX_<GENDER>.npz`)
  - audio: stdlib `wave` can't read float WAVs (`unknown format: 3`) → `scipy.io.wavfile`
- Checked: round trip through GMR's loader matches the source joints exactly; full test clip retargets to a 22-DoF K1 `.pkl`
- Converted `2_scott_0_1_1` 10–30 s, but that window has walking: each ankle travels ~1 m, pelvis drops 18 cm at ~4 s → not usable for Slice 0
- Open check: in `2_scott_0_1_1` the audio is 64.1 s and the motion 63.5 s; the converter assumes both start together. Verify sync on the video

**`--find-still`** (same script): drops windows where either ankle strays > 10 cm from its median, ranks the rest by wrist speed relative to the pelvis (so standing silently with arms down ranks last)
- `~/projects/GMR/.venv/bin/python tools/beat2_to_gmr.py --find-still --window 20 ~/robotics/data/BEAT2/beat_english_v2.0.0/smplxflame_30/2_scott_*.npz`

| Window | Windows with feet < 10 cm | Best |
|---|---|---|
| 20 s | 0 (stillest 13 cm) | none |
| 15 s | 0 (stillest 13 cm) | none |
| 10 s | 4 | `2_scott_0_1_1` 34–44 s: arms 61 cm/s (median window 37), feet 3.7 cm |

- **Finding: Scott shifts his feet every 5–10 s** (take 5: 24 foot moves in 80 s, 6–42 cm each, 0.2–0.7 s long). Stepping is normal talking behaviour, not an edge case → the general tracker and `ground_clip` (which plants both feet) must handle it

**Run: first training on the club GPU**
- Host `sigrobotics`, RTX 5070 Ti. WandB run `e2p0f89y`
- Settings from the WandB config: `uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name bmcox2-university-of-illinois-urbana-champaign/motion_upload/wave_000508-tracking:v3 --env.scene.num-envs 4096 --agent.max-iterations 2500`
- 2,500 iterations in 25 min, **~169k env-steps/s (4.8× the laptop's ~35k)**

**Training charts vs me9exatd (same clip, laptop, 1024 envs; raw values)**

| Iteration | e2p0f89y reward / body err / joint err | me9exatd |
|---|---|---|
| 250 | 62.2 / 0.0163 / 0.47 | 51.1 / 0.0220 / 0.63 |
| 1,000 | 65.5 / 0.0095 / 0.23 | 64.1 / 0.0098 / 0.23 |
| 2,500 | 66.1 / 0.0085 / 0.19 | 65.1 / 0.0084 / 0.20 |

- mean_std 0.147, value loss 0.002, episode length at max from the start: healthy

**Eval** (`eval-tracking` on `e2p0f89y` model_2499, no pushes)

| | me9exatd (model_3500) | e2p0f89y (model_2499) |
|---|---|---|
| Full clip, no falls | 50/50 | **50/50** (≥92.9%) |
| Hand error mean / worst | 1.5 / 5.7 cm | 1.4 / 5.1 cm |
| Body error | 0.6 cm | 0.5 cm |
| Joint error arms / head / legs | 1.4 / 1.6 / 1.3° | 1.4 / 1.4 / 1.3° |
| Trunk height vs ref | 0.0 cm | +0.1 cm |
| Drift at clip end | 2.4 cm | 2.3 cm |
| Max foot tilt L / R | 2.3 / 5.0° | 2.4 / 3.3° |

**Takeaways**
- The club GPU works and reproduces the laptop result, slightly better, in 25 min instead of 43, with 4× the envs
- 4096 envs learns faster per iteration (reward 62 vs 51 at 250 it) and ends at the same quality → long BEAT2 clips can go to the club GPU

## 2026-10-16: Slice 0, first BEAT2 talking clip (run z17z0n1q)

**Clip**
- `2_scott_0_1_1` 34–44 s (the `--find-still` 10 s pick: arms 61 cm/s, ankles within 3.7 cm) → `beat2_to_gmr.py` → GMR → uploaded as `talk_scott_1_1_t34-44-tracking:v0`
- 10 s = 500 steps, the same as the task's 10 s episode length

**Run**
- Club GPU (`sigrobotics`, RTX 5070 Ti). WandB run `z17z0n1q`
- Settings from the WandB config: `uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name bmcox2-university-of-illinois-urbana-champaign/motion_upload/talk_scott_1_1_t34-44-tracking:v0 --env.scene.num-envs 4096 --agent.max-iterations 5000`
- 5,000 iterations in 52 min (~162k env-steps/s)

**Training charts** (raw values; e2p0f89y = wave_000508, 3.7 s clip, same setup)

| | z17z0n1q at 1k / 3k / 5k it | e2p0f89y at 2.5k |
|---|---|---|
| mean_reward | 64.9 / 65.5 / 66.1 | 66.1 |
| error_body_pos (m) | 0.0127 / 0.0107 / 0.0096 | 0.0085 |
| error_joint_pos | 0.34 / 0.24 / 0.22 | 0.19 |
| error_body_rot | 0.075 / 0.060 / 0.055 | 0.047 |
| error_anchor_pos (m) | 0.093 / 0.094 / 0.090 | 0.076 |
| action_rate_l2 (smoothness penalty) | −0.171 / −0.163 / −0.137 | −0.134 |

- Episode length at max (500) from ~250 it; `ee_body_pos` terminations rare (~0.005 vs time_out ~8.2) but ~25× the wave's
- Adaptive sampling stayed uniform (sampling_entropy ~1.0, top bin ~11% ≈ 1/10): no part of the 10 s is much harder than the rest
- mean_std 0.53 → 0.16, flat over the last 1k; value loss ~0.003; `Loss/entropy` negative (−9), normal once std is small
- Verdict: **done** (reward +0.6 over the last 2k it; joint error still sliding slowly, 0.24 → 0.22)

**Eval** (`uv run eval-tracking --wandb-run-path bmcox2-university-of-illinois-urbana-champaign/mjlab/z17z0n1q`, model_4999, no pushes)

| | e2p0f89y (wave, 3.7 s) | z17z0n1q (talking, 9.9 s) |
|---|---|---|
| Full clip, no falls | 50/50 | **50/50 → PASS** (≥92.9%) |
| Hand error mean / worst | 1.4 / 5.1 cm | 2.2 / 7.3 cm |
| Body error | 0.5 cm | 0.8 cm |
| Joint error arms / head / legs | 1.4 / 1.4 / 1.3° | 2.1 / 1.7 / 1.7° |
| Trunk height vs ref | +0.1 cm | −0.1 cm |
| Drift at clip end | 2.3 cm | 2.2 cm |
| Max foot tilt L / R | 2.4 / 3.3° | 4.1 / 1.5° |

- Simulated in 88.8 s vs 1.5 s for the wave eval: it ran on CPU (laptop dGPU was out, so eval's device fell back to `cpu`); a CPU re-run gave identical numbers in 76.7 s

**Takeaways**
- **First talking clip passes: 50/50, no falls.** Same reward plateau as the waves; it needs ~3k it to settle instead of ~1–2k
- Arms are where talking costs: hand error 2.2 vs 1.4 cm (+57%), arm joints 2.1 vs 1.4°. Legs and balance barely change
- Drift did not grow with clip length (2.2 cm over 9.9 s vs 2.3 cm over 3.7 s)
- Smoothness penalty matches the wave's → no sign yet that constant small talking motions make the policy jittery (confirm in `play`)
- ~~`eval-tracking` would cut clips longer than 10 s short~~ **Wrong** (corrected 2026-10-16, next entry): eval loads the play config, whose episode length is ~infinite, so long clips were always fine. Eval now also sets the episode length from the clip length explicitly

## 2026-10-16: multi-clip tracking (MultiMotionCommand)

**Built** (mjlab untouched; design and diff in `notes/multi-clip.md`)
- `src/booster_mjlab/tasks/tracking/multi_motion_command.py`: `MultiMotionCommand(MotionCommand)` + cfg. Per robot: `clip_ids` + `clip_frames`; lookup row `clip_starts[clip] + frame` stored in mjlab's `time_steps`, so obs/rewards/terminations/ONNX are unchanged. A robot at its clip's last frame is resampled, never steps into the next clip. Adaptive sampling: ~1 s bins per clip (smoothing stops at clip ends). Per-clip W&B metrics: `Metrics/motion/clip/{error_body_pos,error_joint_pos,error_anchor_pos,fail_rate,sample_share}/<clip>`
- Wired into `Mjlab-Tracking-Flat-Booster-K1` (`tracking_env_cfg.py`); same train command, single `--registry-name`. Single-clip files behave exactly like before
- `uv run combine-motions`: W&B artifacts / tracking `.npz` / GMR `.pkl` → one `motion.npz` with `clip_lengths`, `clip_names`, `clip_sources` → one W&B artifact (`--no-upload --output` for local)
- `eval-tracking`: every clip of a combined file at once (50 robots per clip), one row per clip, `--clips` to pick; episode length set from the longest clip

**Tests** (all CPU; laptop dGPU still out)
- 2-clip file: `uv run combine-motions .../wave_000508-tracking:v3 .../wave_001104-tracking:v2 --output logs/motions/waves_2clip.npz --no-upload` → 188 + 147 frames, bins 4 + 3
- `uv run --with pytest pytest tests/test_multi_motion.py -q`: **9 passed** (1 min 44 s): rows stay inside their own clip (all 3 sampling modes, command-only and full env with falls), adaptive bins and smoothing stay within a clip, single-clip sampling identical to mjlab's (same seeds), per-clip metrics logged. Mutation check: putting the wrap back to "end of file" fails the boundary test
- CPU training: `WANDB_MODE=offline uv run train Mjlab-Tracking-Flat-Booster-K1 --env.commands.motion.motion-file logs/motions/waves_2clip.npz --env.scene.num-envs 64 --agent.max-iterations 10 --gpu-ids None` → ran, ~34 s/it, per-clip metrics in the console, checkpoint + ONNX export saved
- Regression: `eval-tracking` on `z17z0n1q` (CPU) reproduces the earlier result exactly (50/50, hands 2.2/7.3 cm, ...)

**Eval: one-clip policy on two clips** (`uv run eval-tracking --wandb-run-path .../e2p0f89y --motion-file logs/motions/waves_2clip.npz --device cpu`)

| Clip | No falls | Hands mean / worst | Body | Joints arms/head/legs | Drift |
|---|---|---|---|---|---|
| wave_000508 (trained on) | 50/50 | 1.4 / 4.7 cm | 0.5 cm | 1.4 / 1.3 / 1.3° | 2.2 cm |
| wave_001104 (never seen) | **1/50** | 12.5 / 31.0 cm | 6.4 cm | 9.9 / 8.5 / 10.4° | — |

- Failures on wave_001104: `ee_body_pos` 35, `anchor_pos` 8, both 6; at 1.2–2.8 s

**Takeaways**
- A one-clip policy doesn't transfer even to another wave → multi-clip training is needed before held-out speakers mean anything
- Starts are weighted by clip length (uniform floor): long BEAT2 takes will dominate short gestures unless adaptive sampling or a per-clip weight corrects it; watch `clip/sample_share`
- Correction: the ">10 s eval bug" in the previous entry didn't exist (play config ~infinite episode)

## 2026-10-16: multi-clip sanity run (8ku1opzv): one policy, two waves

**Run**
- Club GPU (`sigrobotics`, RTX 5070 Ti). WandB run `8ku1opzv` (`multiclip-sanity`)
- `uv run combine-motions .../wave_000508-tracking:v3 .../wave_001104-tracking:v2 --artifact-name waves-2clip` → `waves-2clip:v0` (188 + 147 frames)
- Settings from the WandB config: `uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name bmcox2-university-of-illinois-urbana-champaign/motion_upload/waves-2clip:v0 --env.scene.num-envs 4096 --agent.max-iterations 2500 --agent.run-name multiclip-sanity`
- 2,500 iterations in 25.5 min, ~166k env-steps/s (single-clip `e2p0f89y`: 169k → no overhead from MultiMotionCommand)

**Training charts** (raw, at 2,450 it)
- reward 41.9 (100 it) → 60.8 (250) → 64.6 (1k) → 65.6, +0.2 over the last 500; episode length at max by 250
- `ee_body_pos` terminations 0.17 → 0.0009; `anchor_pos` 0; mean_std 0.52 → 0.16; value loss 0.0026

| Per clip | body err | joint err | fail_rate | sample_share |
|---|---|---|---|---|
| wave_000508 | 0.0085 m (`e2p0f89y`: 0.0087) | 0.190 (0.190) | 0.0000 | 0.57 |
| wave_001104 | 0.0094 m (`pqh0whw0`: 0.0107) | 0.204 (0.239) | 0.0002 | 0.43 |

- sample_share stayed at the length share (4/7, 3/7; sampling_entropy 0.9999): neither clip is hard. Brief wobble to 0.55/0.45 around 1k it = adaptive sampling reacting to wave_001104's few failures (fail_rate 0.0016)

**Eval** (`uv run eval-tracking --wandb-run-path .../8ku1opzv`, model_2499, laptop CPU)

| Clip | 8ku1opzv (multi) | single-clip policy |
|---|---|---|
| wave_000508 | 50/50, hands 1.5 / 5.0 cm, body 0.5, joints 1.4 / 1.3 / 1.2°, drift 2.2, tilt 3.4 / 2.5° | `e2p0f89y`: 50/50, 1.4 / 5.1, 0.5, 1.4 / 1.4 / 1.3°, 2.3, 2.4 / 3.3° |
| wave_001104 | 50/50, hands 1.6 / 4.5 cm, body 0.5, joints 1.5 / 1.4 / 0.9°, drift 3.0, tilt 3.8 / 3.7° | `pqh0whw0`: 50/50, 1.7 / 5.8, 0.6, 1.8 / 1.9 / 1.2°, 3.1, 3.0 / 3.3° |

**Takeaways**
- **Multi-clip works:** one policy matches both single-clip policies on both clips, in the same 2,500 it and the same wall time. Sharing a policy between two waves costs nothing
- Compare: `e2p0f89y` (wave_000508 only) gets 1/50 on wave_001104; this policy gets 50/50 on both
- wave_001104 slightly better than `pqh0whw0`, but that run had 1024 envs (laptop), so not a fair comparison
- Per-clip metrics, fail_rate and sample_share all log and read as expected on a real GPU run

## 2026-10-16: BEAT2 batch: 152 clips, QC, train / held-out artifacts

**Built**
- `tools/beat2_batch.py`: per take, `--find-still` (10 s windows, ankles within 10 cm, top 2 non-overlapping by arm activity) → `beat2_to_gmr` convert → headless GMR → `ground_clip` → QC on booster's K1 → `notes/beat2-qc.md` → `combine-motions` train + held-out. Every stage cached per clip (rerun = only new takes); files written atomically; `--exclude {none,severe,flagged}`
- `tools/gmr_retarget.py`: GMR retarget with no viewer (GMR's venv). Keeps frame 0 (GMR's script skips it, so audio was 1 frame off) and warms the IK up on it; otherwise matches GMR's output to 0.0002 rad. 3 s per 10 s clip
- `beat2_to_gmr.py`: `top_non_overlapping()` pulled out of `--find-still` (same output)

**Run**
- `uv run python tools/beat2_batch.py --train 2_scott 1_wayne 3_solomon 4_lawrence 7_sophie 9_miranda --heldout 11_nidal 21_ayana --exclude severe --entity bmcox2-university-of-illinois-urbana-champaign`
- Artifacts: **`beat2-10s-train:v0`** (98 clips, 16.3 min) and **`beat2-10s-heldout:v0`** (42 clips, 7.0 min)
- Full pipeline ~45 min for 152 clips on the laptop CPU (GMR 3 s/clip, ground ~1.5 s/clip, combine ~5 s/clip FK)

| Speaker | Split | Takes | Clips | Kept | Median K1 hand speed |
|---|---|---|---|---|---|
| scott | train | 15 | 3 | 2 | 16.0 cm/s |
| wayne | train | 15 | 25 | 24 | 5.7 |
| solomon | train | 15 | 14 | 13 | 10.1 |
| lawrence | train | 15 | 24 | 22 | 11.8 |
| sophie | train | 15 | 28 | 24 | 5.3 |
| miranda | train | 7 | 14 | 13 | 9.5 |
| nidal | held-out | 15 | 30 | 29 | 5.3 |
| ayana | held-out | 7 | 14 | 13 | 9.8 |

**QC** (calibrated on clips that trained to 50/50: K1 feet ≤ 1.8 cm, trunk ≤ 1.8 cm, knees 14–36°, 0 limit frames)
- Severe → excluded (12): upper-arm twist at its limit > 50% of frames (9; straight arm, so GMR's IK drifts the twist to the limit), ground_clip IK failure (2), trunk-drop outlier (2)
- Kept: head or shoulder held at a limit (valid K1 motion, just clipped), little arm motion (< 5 cm/s), knee outliers
- Fixes while calibrating: a straight elbow (elbow bend at 0) is a normal pose, not a limit hit; K1 feet flag 5 → 8 cm (K1 is ~0.6× human, so the 10 cm human filter allows ~6 cm); dropped feet from the batch-relative outlier test (median 1 cm, long normal tail → flagged 31 normal weight shifts)

**Held-out skew** (share of clips)

| | Train | Held-out | Nidal | Ayana |
|---|---|---|---|---|
| Head at limit | 6% | 9% | 3% | 21% |
| Shoulder at limit | 21% | 18% | 10% | 36% |
| Upper-arm twist | 7% | 5% | 3% | 7% |
| Hands < 5 cm/s | 15% | **32%** | **43%** | 7% |

**Takeaways**
- Held-out is **not** skewed by retargeting limits overall (rates match training); the two speakers are opposite ends: Ayana hits head/shoulder limits most of anyone, Nidal least
- The real skew is arm activity: Nidal is a calm speaker (43% low-motion clips) → pooled held-out numbers would flatter the policy. **Always read held-out eval per speaker:** Ayana = hard test, Nidal = easy one
- Scott steps too much for 10 s still windows (3 clips from 15 takes): training is uneven across speakers (Sophie 24 kept, Scott 2)
- Only 5 takes have audio downloaded; fine for training, needed only for dubbed videos
- Process: a `pkill -f` pattern matched its own shell and killed the command before it ran; kill by PID

## 2026-10-16: left arm held back in BEAT2 clips: GMR IK start, fixed → beat2-10s-*:v1

**Symptom:** in visualize-motions many BEAT2 clips (e.g. sophie_0_15_15_t53-63, lawrence_0_1_1_t9-19) had the K1's left arm held straight back, never the right

**Not a mapping bug** (checked every link)
- GMR `K1_serial.xml` vs booster `k1.xml`: every head/arm joint's axis (local and in the trunk frame), range, parent-body pose, and zero position match; renamed `ALeft_Shoulder_Pitch` = `Left_Shoulder_Pitch`
- GMR loads `K1_serial.xml` and its .pkl columns follow its joint order, which ground_clip assumes; booster's xml joint order is the same, so upload-motion's by-position write is right
- FK on real frames: hand positions in the trunk frame identical for raw .pkl on GMR's model, raw .pkl on booster's model, and grounded .pkl

**Cause: GMR's IK start.** GMR's raw output already had the arm back (K1 left hand −0.17 / −0.11 m behind the trunk; human left wrist +0.20 / +0.26 m in front). GMR starts the IK from the zero pose (a T-pose); on frame 0 the left arm can settle swung back (Sophie: left shoulder pitch at its +70° limit) and the warm start keeps it there for the whole clip. A fresh solve at frame 150 gave the correct arm. Starting from the K1's arms-down standing pose fixed it: GMR IK error 7.16 → 1.25 (Sophie), 7.05 → 1.76 (Lawrence); control clip identical
- Prevalence in v0: 20/152 clips had the K1 left hand behind while the human's was in front (right: 2). 9 were already excluded as "upper-arm twist", **11 were in the v0 artifacts**
- Why left and not right: not pinned down (IK config, ranges and arm frames are all left/right symmetric). The fix doesn't depend on it

**Fix**
- `tools/gmr_retarget.py`: seed the IK with the arms of booster's `HOME_KEYFRAME` (shoulder roll ±1.4, elbow ±0.4) before the frame-0 warm-up
- `tools/beat2_batch.py`: new severe QC flag "arm behind body (human's in front)": mean K1 hand > 5 cm behind the trunk while the human wrist is > 5 cm in front of the pelvis
- Re-ran the batch with `--force` (~17 min) and re-uploaded: **`beat2-10s-train:v1`** (106 clips, 17.7 min) and **`beat2-10s-heldout:v1`** (44 clips, 7.3 min)

| QC | v0 | v1 |
|---|---|---|
| Flagged | 62 | 43 |
| Severe (excluded) | 12 | 2 (wayne_0_10_10_t49-59 right arm behind; lawrence_0_4_4_t1-11 trunk-drop outlier) |
| Upper-arm twist at limit / head at limit / ground IK failures | 9 / 9 / 2 clips | 0 / 0 / 0 |
| Left arm behind body | 20 | 0 |

**Sanity clips unaffected:** waves 000113/000508/001104 and talk_scott_1_1_t34-44 re-retargeted with the fix are identical to the originals after frame 10 (0.00 cm hands, ≤ 0.01° joints; first frames differ ≤ 1.5 cm). Their artifacts and the policies trained on them (me9exatd, pqh0whw0, e2p0f89y, z17z0n1q, 8ku1opzv) stay valid

**Takeaways**
- Most of v0's twist / head-limit flags were the same IK problem, not the speakers' poses
- GMR's K1 config tracks the human **elbow** with the K1's hand (`left_hand_link` ↔ `left_elbow`) and the shoulder with `Left_Arm_3`: the K1 arm copies the human upper arm, the forearm is ignored. For co-speech gestures (forearm/hand in front, elbow at the side) this loses much of the gesture. Worth an IK-config experiment (hand ↔ scaled wrist) later
- Any training run on `beat2-10s-train:v0` should be redone on `:v1`

## 2026-10-17: first general tracker (0lg80c7d) stuck on one bad clip → beat2-10s-*:v2

**Run**
- Club GPU (`sigrobotics`). WandB run `0lg80c7d` (`beat2-general`), `beat2-10s-train:v1` (106 clips, 17.7 min), 4096 envs, 30,000 iterations, 6.5 h (~158k env-steps/s)
- (`xzaq29gw` on `:v0` was killed at it 14)

**Training charts** (raw, averaged ±200 it)

| Iteration | 250 | 1k | 2.5k | 10k | 20k | 30k |
|---|---|---|---|---|---|---|
| mean_reward | 36.0 | 54.4 | 56.6 | 56.0 | 56.6 | 55.0 |
| error_body_pos (m) | 0.058 | 0.023 | 0.019 | 0.020 | 0.021 | 0.020 |
| error_joint_pos | 1.85 | 0.56 | 0.46 | 0.46 | 0.45 | 0.47 |
| `ee_body_pos` terminations | 3.2 | 0.55 | 0.38 | 0.41 | 0.44 | 0.31 |

- Flat from ~2.5k it: 27k iterations added nothing. mean_std 0.48 → ~0.35 (single clip: 0.16); value loss 0.04–0.07; small wobble in the last few hundred it (value loss 0.17, action_rate −0.71)
- **`sampling_top1_prob` 0.6–0.75 the whole run**: `wayne_0_9_9_t12-22` got 62% of starts by 500 it and 70–77% after; the only clip with fail_rate > 0 (0.07). Other 105 clips: median sample_share 0.002 (uniform 0.0094) → each trained ~4–5× less than it should
- Verdict: **stuck**. Not checked in `play`

**Eval** (model_29999, club GPU, `--device cuda:0`)
- `uv run eval-tracking --wandb-run-path .../0lg80c7d --registry-name .../beat2-10s-heldout:v1 --device cuda:0` (+ `--push`), and on the train set (no `--registry-name`)

| Set | Pass | Hand err (mean of clip means) |
|---|---|---|
| Held-out | 43/44 clips, 2150/2200 rollouts | 6.7 cm (Nidal 5.8, Ayana 8.7) |
| Held-out + pushes | 43/44 (same) | same within ~0.3 cm |
| Train | 103/106 clips, 5295/5300 | 5.8 cm (Sophie 4.2, Wayne 4.5, Lawrence 6.5, Miranda 7.3, Solomon 7.7, Scott 9.7) |

- Only held-out failure: `nidal_0_3_3_t0-10`, 0/50, `ee_body_pos` at 0.44–0.52 s. 5 train failures, all at t = 0.10 s (start jitter)
- Same clip, specialist vs generalist: `scott_0_1_1_t34-44` hands 2.2 cm (`z17z0n1q`) vs 12.7 cm here. The over-sampled `wayne_0_9_9_t12-22` is the best clip (2.3 cm mean, 25 cm at its jump)
- Foot tilt on floor 10–38° on many clips (train too); height within ~1.5 cm; drift 2–4 cm (≤ 13 cm worst)
- Train ≈ held-out → **underfitting, not memorizing**

**Problems & fixes**
- **GMR joint jumps.** `nidal_0_3_3_t0-10`: BEAT2 motion smooth (≤ 0.16 rad/frame) but GMR holds the K1 left arm in a wrong pose (hand 0.59–0.68 m high) for 0.7 s, then `Left_Elbow_Pitch` snaps 1.57 rad in one frame (hand moves 42 cm in 1/50 s). Max per-frame joint step over all 152 clips: 4 glitches at 0.92–1.57 rad (all `*_Elbow_Pitch`, the upper-arm twist; wayne's is a one-frame spike 0.20 → −0.72 → 0.19), everything else ≤ 0.52 rad (median 0.13). New severe QC flag `joint jump` (> 0.6 rad per 1/30 s frame) in `tools/beat2_batch.py`. Not a motor limit (arm R14 motors: 33.5 rad/s ≈ 1.1 rad/frame), just the gap in the data
- **Adaptive sampling takeover.** A bin's weight = recent failures per step (scales with num_envs) + `adaptive_uniform_ratio`/bins; mjlab's 0.1 is too weak with 4096 envs and a never-trackable clip. K1 `env_cfgs.py`: `motion_cmd.adaptive_uniform_ratio = 1.0`. Written up in `multi-clip.md`
- Re-ran `uv run python tools/beat2_batch.py --train 2_scott 1_wayne 3_solomon 4_lawrence 7_sophie 9_miranda --heldout 11_nidal 21_ayana --exclude severe` (cached; QC + combine only, ~11 min) → **`beat2-10s-train:v2`** (103 clips, 17.2 min) and **`beat2-10s-heldout:v2`** (43 clips, 7.2 min). Excluded: the 4 jump clips + `wayne_0_10_10_t49-59`, `lawrence_0_4_4_t1-11` (as in v1)
- **`eval-tracking` crashed with > 4096 rollouts** ("Inplace update to inference tensor outside InferenceMode") on the second batch's `env.reset()`. Fixed: reset under `torch.inference_mode()` too. Workaround on old code: `--max-envs 5300`
- Laptop dGPU dropped off the PCI bus again (`lspci` shows only the Intel iGPU) → evals ran on the club GPU
- Club GPU WandB: `source ~/bmcox2/.wandb_env` (shared `booster` account; no `wandb login`)

**Takeaways**
- One bad clip can wreck a multi-clip run through adaptive sampling. Watch `sampling_top1_prob` early; if it's far above 1/(bins), look at that clip's `sample_share` and its reference
- The general tracker generalizes (held-out ≈ train, pushes don't matter) but is ~3× worse than single-clip policies; first see how much fair sampling recovers before changing the network or observations (no future frames in the obs; 512-256-128)

## 2026-10-17: general tracker on clean data (s5cdzms7): fair sampling fixes the plateau

**Run**
- Club GPU (`sigrobotics`). WandB run `s5cdzms7` (`beat2-general-v2`), 10,000 it in 2.6 h (~160k env-steps/s), seed 42
- `uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-10s-train:v2 --env.scene.num-envs 4096 --agent.max-iterations 10000 --agent.run-name beat2-general-v2` (config confirms `adaptive_uniform_ratio = 1`)

**Training charts vs 0lg80c7d** (raw, averaged ±150 it)

| | s5cdzms7 at 1k / 2.5k / 5k / 8.5k | 0lg80c7d at 10k | 0lg80c7d at 30k | z17z0n1q (1 clip) at 5k |
|---|---|---|---|---|
| mean_reward | 63.1 / 64.8 / 65.3 / 65.5 | 55.9 | 55.0 | 66.1 |
| error_body_pos (m) | 0.0167 / 0.0127 / 0.0116 / 0.0114 | 0.0202 | 0.0195 | 0.0096 |
| error_joint_pos | 0.49 / 0.31 / 0.28 / 0.27 | 0.46 | 0.47 | 0.22 |
| error_body_rot | 0.109 / 0.075 / 0.070 / 0.071 | 0.128 | 0.128 | 0.055 |
| `ee_body_pos` terminations | 0.021 / 0.005 / 0.009 / ~0.01 | 0.40 | 0.31 | ~0.005 |
| action_rate_l2 | −0.24 / −0.18 / −0.16 / −0.17 | −0.54 | −0.71 | −0.14 |
| mean_std | 0.22 / 0.18 / 0.175 / 0.173 | 0.36 | 0.40 | 0.16 |
| sampling_top1_prob | 0.006 / 0.002 / 0.004 / 0.003 | 0.62 | 0.65 | |

- Episode length 499/500 from ~1k it. Sampler spread evenly (sampling_entropy ~0.999; top clip at end `miranda_0_13_13_t25-35` 1.9% vs uniform 0.97%); every clip's fail_rate 0 at the end
- Per clip (final): median error_body_pos 0.0105 m; worst `lawrence_0_7_7_t53-63` 0.031, `solomon_0_1_1_t18-28` 0.029, `sophie_0_14_14_t52-62` 0.028, `lawrence_0_6_6_t71-81` 0.027
- Mostly flat after ~5k it (body err 0.0116 → 0.0114 at 8.5k)
- **Two instability episodes**, ~6.9k–7.5k (recovered) and 9.0k–end (not recovered): mean_std rises first (0.173 → 0.21–0.26), then joint error (0.27 → 0.34–0.59), `ee_body_pos` terminations (0.01 → 0.2–0.7), and only then the sampler concentrates (top1 0.003 → 0.06–0.16). Reward 65.5 → 61.4 (median, last 500 it). Likely PPO noise drift (entropy bonus 0.005 pushing std up once tracking is good), with adaptive sampling amplifying it; not confirmed
- Training errors include the exploration noise; eval uses the noise-free policy, so model_9999 may still be fine. Best stretch: 8.0k–9.0k → `model_8500.pt`
- Verdict: **done**; use `model_8500.pt` (eval below). Not checked in `play` yet

**Eval** (club GPU; `uv run eval-tracking --wandb-run-path .../s5cdzms7 --checkpoint-name model_8500.pt --registry-name .../beat2-10s-heldout:v2 --device cuda:0`, same for model_9999, train set, held-out `--push`)

| Hand error, mean of clip means (cm) | s5cdzms7 model_8500 | 0lg80c7d model_29999 |
|---|---|---|
| Held-out, all | **3.05** (42/43 clips, 2149/2150 rollouts) | 6.7 (43/44) |
| Nidal / Ayana | **2.3 / 4.6** | 5.8 / 8.7 |
| Train, all | **2.46** (100/103 clips, 5145/5150) | 5.8 (103/106) |
| Sophie / Wayne / Miranda / Lawrence / Solomon / Scott | **1.95 / 1.95 / 2.6 / 2.9 / 3.1 / 4.1** | 4.2 / 4.5 / 7.3 / 6.5 / 7.7 / 9.7 |

- **model_8500 beats model_9999**: held-out 3.05 vs 3.19 cm, 42 vs 41 clips at 50/50, Ayana max foot tilt 28 vs 38°. Use model_8500
- Pushes change nothing (mean +0.00 cm; same single failure)
- No train clip above 5 cm (0lg80c7d: most). `scott_0_1_1_t34-44`: 5.0 cm (0lg80c7d 12.7; single-clip `z17z0n1q` 2.2)
- Failures: held-out 1 rollout, `ayana_0_14_14_t36-46` at 6.3 s (`ee_body_pos`; with pushes `anchor_ori` at 6.9 s). Train 5 rollouts on `lawrence_0_12_12_t26-36` (3), `lawrence_0_13_13_t21-31`, `solomon_0_15_15_t43-53`, all at t = 0.08–0.10 s: the same 3 clips and time as in 0lg80c7d → start-of-clip issue with these references + the ±0.1 rad start jitter, not the policy
- Generalization gap now visible: train 2.5 vs held-out 3.05 cm; Nidal (low motion) ≈ train, Ayana (expressive) 4.6 cm, worst `ayana_0_13_13_t38-48` 6.6 cm
- Body error 0.7–1.5 cm, arm joints 2–5°, drift ~3 cm (Solomon 5.5)
- **Foot tilt still high**: max tilt on floor > 10° on Lawrence 20/22, Solomon 13/13, Nidal 15/29 clips; worst ~29°. Main open quality / sim-to-real issue

**Takeaways**
- Clean data + `adaptive_uniform_ratio = 1.0` halved the general tracker's errors in a third of the iterations: hands 5.8 → 2.5 cm (train), 6.7 → 3.05 cm (held-out). Single-clip policies: 1.4–2.2 cm
- A general BEAT2 tracker that passes 142/146 clips at 50/50 (the rest 47–49/50) with ~2.5–3 cm hands; Ayana-style expressive motion is the hardest
- Watch mean_std late in runs: a rise from its plateau came before both dips

## 2026-10-17: Slice 0 video with the general policy; K1 leans back → torso IK config prototype

**Video** (Slice 0 step G)
- `play` gained headless-video settings (`src/booster_mjlab/scripts/play.py`, commit `0db3089`): camera 1.8 m / 45° fovy / −8° (mjlab's 2.8 m left the K1 at 1/3 of the frame), 1920×1080, x264 qp 18 (~7 Mbit/s vs ~0.5), `--hide-overlays` (no reference ghost / foot-height rays); `--video-*` flags override
- `uv run play Mjlab-Tracking-Flat-Booster-K1 --wandb-run-path .../s5cdzms7 --wandb-checkpoint-name model_8500.pt --registry-name .../talk_scott_1_1_t34-44-tracking:v0 --num-envs 1 --video True --video-length 500 --hide-overlays` → `logs/rsl_rl/k1_tracking/wandb_checkpoints/s5cdzms7/videos/play/rl-video-step-0.mp4`; audio: `ffmpeg -i video.mp4 -i ~/robotics/data/beat2_batch/smplx/scott_0_1_1_t34-44.wav -c:v copy -c:a aac -shortest out.mp4`
- Gotchas: `--video True` (not a bare flag); the mp4 is written only after `--video-length` steps, so don't Ctrl-C early (first try: 328/500 frames, 6.6 s)
- Looks: "not too bad", but lots of arm motion and the K1 leans back

**Why it leans back: GMR's K1 config makes the trunk copy the human pelvis**
- `smplx_to_k1.json`: `Trunk ← pelvis` (orientation). The K1 has no waist; when Scott rocks back his pelvis tilts back but his spine bends ~8° forward, so his torso stays upright. K1 reference trunk lean = Scott's pelvis tilt to 0.3° (mean −15°, −34…+2°) vs his torso (pelvis→neck) mean −6.5° (−24…+18°)
- **Correction:** `*_hand_link` starts at the K1 *elbow*, so `hand_link ← elbow` is right, and its orientation target makes the forearm follow the human forearm. Earlier notes ("forearm ignored", "K1 hands 16 cm/s vs human 61") measured the elbow. The forearm *tip* sweeps 60/53 cm vs Scott's wrists ×0.59 49/48 cm (42 vs 36 cm/s): arms are slightly *bigger* than Scott's, scaled (K1 forearm 0.20 m vs ~0.15 m scaled human). The QC "arms K1" column is elbow speed too

**Prototype** (Scott clip, `tools/gmr_retarget.py --ik-config`; massless `*_hand_end` bodies added to a temp copy of GMR's K1 model, GMR files untouched; neutral offsets for bodies without a table-1 task)

| Trunk orientation from | Trunk lean mean [range] | Hand-tip sweep L/R |
|---|---|---|
| pelvis (GMR) | −15.2° [−34, +2] | 60 / 53 cm |
| **spine1** | **−6.0° [−25, +21]** | 59 / 53 |
| spine2 | +0.2° [−12, +25] | 58 / 54 |
| spine3 | +4.4° [−11, +31] | 58 / 52 |
| Scott's torso | −6.5° [−24, +18] | 49 / 48 (×0.59) |

- Wrist position targets on the forearm tips (`*_hand_end ← *_wrist`, weight 10): no change (61 / 54 cm). Dropped
- spine1 vs pelvis after `ground_clip`: feet 1.8 / 1.8 cm, trunk drop 1.5 / 1.8 cm, no limits, max joint step 0.23 rad both; **CoM over the feet** (mean −0.2 cm vs −1.4 cm behind the feet centre)
- Saved as `tools/ik_configs/smplx_to_k1_torso.json` (GMR's config with `Trunk ← spine1`, position weight 0: hips/feet place the trunk). `beat2_batch.py --ik-config` passes it through. Without `--ik-config` the output is unchanged (0.0 diff vs the cached v2 clip)

## 2026-10-18: parallel BEAT2 pipeline (~45 min → 3 min); torso-config data → beat2-10s-*:v3

**Parallel pipeline** (`--workers`, default 12; commit below)
- Timing (laptop, serial): GMR 1.9 s/clip + ~4 s startup, ground < 1 s, windows 0.7 s/take, QC wrist 0.3 s/clip, **combine-motions 3.3 s/clip on one core** (builds a one-robot sim per clip + per-frame Python FK) → most of the ~45 min. i9-13900H: 20 threads, 31 GB
- `beat2_batch.py --workers N`: windows / convert / ground / QC-wrist in a `ProcessPoolExecutor` (spawn context, one `Grounder` per worker via initializer); GMR split across N `gmr_retarget.py` processes (`todo[i::n]`); `combine-motions --workers N` converts .pkl clips in parallel, order kept
- Processes, not threads (GIL; GMR/FK loops are Python). spawn, not fork (torch / warp thread pools + fork = inherited locked mutexes). No shared mutable state: one solver/sim per clip or worker, one output file per clip, tmp + `os.replace` writes, each stage waits for all workers before the next. ~1.5 GB RAM per worker
- Verified bit-identical: from-scratch parallel run on 2_scott + 21_ayana (17 clips) == serial v2 files (smplx, k1, grounded, combined held-out frames, QC flags). combine 12 clips: 44 s → 15 s (worker import ~8 s each)

**v3 data** (torso IK config)
- `uv run python tools/beat2_batch.py --train 2_scott 1_wayne 3_solomon 4_lawrence 7_sophie 9_miranda --heldout 11_nidal 21_ayana --exclude severe --ik-config tools/ik_configs/smplx_to_k1_torso.json --out-dir ~/robotics/data/beat2_batch_torso --qc notes/beat2-qc-torso.md --workers 12` (smplx/ copied from v2 with `cp -a`, so convert was cached): **189 s**
- **`beat2-10s-train:v3`** (105 clips) / **`beat2-10s-heldout:v3`** (43 clips). Excluded: the same 4 joint-jump clips. Back in vs v2: `wayne_0_10_10_t49-59` (elbow 5.4 → 2.9 cm behind the trunk; threshold 5) and `lawrence_0_4_4_t1-11` (trunk-drop robust z fell under 3.5; 3.2 cm range). Both were borderline, not IK failures
- All 152 clips, mean trunk lean: human torso −4.8°, v2 (pelvis) −7.9°, v3 (spine1) −2.8°. Per-clip |K1 − human|: median 3.4° → 2.5°, v3 closer on 104/152. CoM vs feet centre −0.9 → −0.2 cm. v3 is now ~2° too upright on average (Scott was the best case)

## 2026-10-18: full BEAT2 dataset, phase 1 (human side): splits, segments, spec pipeline, Gate 1 QC

Plan: "K1 Co-Speech Gesture: Full BEAT2 Dataset Plan" (Oct 18). Phase 2 (retarget → upload → train) waits for the v3 GMR config.

**BEAT2 split file** (`train_test_split.csv`, no HF login needed): 1,620 takes, 25 speakers
- 9 big speakers (1–4, 6, 7, 9, 11, 21): 95 `train` / 8 `val` (takes 9–16) / 15 `test` (1–8, 65, 73, 81, 87, 95, 103, 111) / 12 `additional`; Carla 63 / 0 / 7 / 12, Miranda + Ayana 7 test (1–8 missing)
- 16 small speakers: 13–19 `train`, 0–2 `val` (9–10), 8–9 `test` (1, 2, 65, …); 5_stewart + 10_kieks: 7 train / 8 val / 15 test
- Hours (motion): train 19.4, val 2.1, test 5.2, **additional 26.4**. The v1–v3 artifacts used takes 1–15: all official val/test (leakage check: 103/103 train clips)
- **`additional` = session 1 = the 10-min conversation recordings** (7–12 min each; 12 per big speaker, 3 per small). Same bodies, standing, 58–87% speech, silences up to 28 s (instructor was remote, only the speaker recorded → silences are listening). Lawrence wanders (947° of turning), Scott steps; the rest stand. Tier A keeps 72% of the 7 training speakers' sample takes (≈15 h over all 21 h)
- Downloaded: all 1,464 session-0 takes (4.3 GB, 5 min) + one session-1 take and transcript per big speaker. `gender` is `neutral` in every file; genders from BEAT Table 9 (arXiv 2203.05297), whose IDs disagree with BEAT2 on durations for 21 and 28

**Held-out speakers:** 11_nidal, 21_ayana, **20_li (M), 27_yingqing (F)**. 5_stewart/10_kieks (most eval takes) were first pick, but they are calm (arms 15 cm/s, still feet) like Nidal (14); Li 21 / Yingqing 24 ≈ training median 22

**Segments** (`tools/beat2_segments.py`, replaces top-k windows; report `notes/beat2-full-segments.md`)
- Tier A: maximal stretches with ankles within 10 cm of their median, cut at planted frames (ankles < 0.1 m/s), 4–20 s clips (even split). Tier B: the foot shifts between them inside 25 cm stretches, ±2 s of standing, names `_shift`; overlaps A by the padding, so A stays the same whether B is admitted
- Training (official train takes, 21 speakers): **11.6 h Tier A** (3,451 clips, 22% of time rejected) + 2.8 h Tier B. No speaker > 15% (Solomon 12.9% max). Scott loses 87%, Jorge 100% (steps 20–60 cm every ~1 s, real)
- Eval: train-speaker val 74 min / test 188 min; held-out val 27 min / test 47 min (Tier A)
- GPU memory: ~0.27 GB/h at 50 Hz (369 floats/frame) → 3.2 GB for A, 4.0 GB A+B; + session 1 ≈ 7 GB

**Spec pipeline:** `tools/datasets/beat2_full.toml` + `uv run python tools/beat2_batch.py --spec <toml> [--stages segment]`: segment → convert → GMR → ground → QC → one combined file per set (train, train-shift, val, heldout-val, test, heldout-test) → leakage check on the written file → upload. `build.json` refuses to mix clips built with other segment limits / IK configs. Smoke test (3 speakers, 33 clips, no upload): 70 s end to end

**Gate 1** (`tools/clip_qc.py`; calibration `notes/gate1-calibration.md` on the 152 v1 clips + torso clips)
- Joint jump: plan's 0.3 rad flags 11 (7 are normal arm motion ≤ 0.52) → keep **0.6** (the 4 GMR flips)
- New **trunk turn > 6°/frame**: real ≤ 4°; flips 14–33°, plus `ayana_0_12_12_t20-30` 7.6° (human pelvis 0.1°: a small GMR flip). Trunk move > 3 cm/frame
- Joint speed > no-load limit > 0.1 s, floor > 5 mm, format, quaternion: 0 clips (30 fps steps only exceed limits inside a flip; ground_clip guarantees the floor). Kept as guards
- Foot slide: plan's 1 cm/frame flags 21 (1–2 frame weight-shift pivots, Lawrence/Solomon) → planted = within 2 mm, **> 1 cm/frame for ≥ 0.1 s or > 3 cm in a frame**: 1 + the wayne flip. Smoke test: 4/33 new clips, all real (human foot lifts or stays still, K1 foot skids: small steps fall under ground_clip's stance threshold at 0.6 scale)
- Self-collision: no arm–trunk overlaps; only hand into hip/thigh (≤ 25 mm, `scott_0_1_1_t34-44` 0.6 s, trained 50/50) → info only; any other pair severe
- Severe on v1: 8 (4 flips, Ayana flip, Lawrence slide, wayne arm-behind, lawrence trunk drop). "Little arm motion" flag dropped (no arm floor now)

## 2026-10-18: run fsyy1c2w on torso data (v3): same pace, better held-out tracking

**Run**
- Club GPU. WandB run `fsyy1c2w` (`beat2-general-v3`), `beat2-10s-train:v3`, 4096 envs, planned 10k it; **stopped by accident at 3,708 it** (1.1 h). Last checkpoint `model_3500.pt`
- Speed 133–141k env-steps/s (s5cdzms7: 160k), 45k right before the stop: something else was probably on the club GPU

**Training charts vs s5cdzms7 (v2) at the same iteration** (raw medians ±150 it)

| | 1k | 2.5k | ~3.7k (s5: 4k) |
|---|---|---|---|
| error_body_pos v3 / v2 (m) | 0.0173 / 0.0166 | 0.0129 / 0.0127 | 0.0126 / 0.0123 |
| error_joint_pos v3 / v2 | 0.49 / 0.49 | 0.32 / 0.32 | 0.31 / 0.31 |

- Healthy: episode length 500, ~0 terminations, sampling_top1 ≤ 0.012, mean_std 0.19. Torso data is no harder to learn

**Eval** (held-out, same iteration: `uv run eval-tracking --wandb-run-path .../fsyy1c2w --checkpoint-name model_3500.pt --registry-name .../beat2-10s-heldout:v3 --device cuda:0`; s5cdzms7 model_3500 on `:v2`)

| Held-out | fsyy1c2w model_3500 (v3) | s5cdzms7 model_3500 (v2) | s5cdzms7 model_8500 (v2) |
|---|---|---|---|
| Hand err all (cm) | **3.08** | 3.42 | 3.05 |
| Nidal / Ayana | **2.44 / 4.41** | 2.52 / 5.29 | 2.3 / 4.6 |
| Body err (cm) / head joints | **0.88 / 2.6°** | 1.06 / 3.3° | |
| Clips 50/50 | 42/43 | 43/43 | 42/43 |
| Clips with foot tilt > 10° / worst | 13 / 19.6° | 12 / 41.6° | |

- v3 better on 29/43 clips (mean −0.34 cm); most gain on Ayana. Only failures: `ayana_0_14_14_t36-46` 48/50 at 7.2–8.7 s (`anchor_pos`, `ee_body_pos`), the clip where s5cdzms7 model_8500 also failed once
- **model_3500 on torso data ≈ the best v2 policy (model_8500)** with less than half the training, and its reference leans like the human

**Takeaways**
- The torso IK config is strictly better: more human-like posture and easier to track (CoM over the feet)
- s5cdzms7 gained ~10% from 3.5k to 8.5k; resuming fsyy1c2w to ~6k should give the best general tracker so far

## 2026-10-18: resume mix-up; WandB cleanup

**Resuming fsyy1c2w**
- First try `hhlreous` started from scratch (iteration 0, reward 5.5, mean_std 0.64): my command had `--wandb-run-path ... --wandb-checkpoint-name model_3500.pt` but not **`--agent.resume True`**. mjlab's train only loads a checkpoint when resume is on; otherwise those flags are silently ignored
- With it, rsl_rl restores the weights *and* the iteration counter, and `--agent.max-iterations` counts **additional** iterations (3,500 + 2,500 = 6,000). `cx1b6hgi` resumed correctly but wasn't in tmux → restarted in tmux as **`0j0flpxj`**
- First logged iteration of a resume shows a bogus error_body_pos ~2.0 m (robots measured in their spawn pose before the first reset); from the next iteration it's back to the checkpoint's level. Ignore it

**WandB cleanup** (via the API)
- `mjlab`: deleted 12 aborted / duplicate runs (`s2adpiqw`, 7 setup attempts from 10-14, `gusmftiz`, `xzaq29gw`, `hhlreous`, `cx1b6hgi`); 12 runs left
- Kept runs renamed `MM-DD what-it-is`, tagged (`velocity`/`tracking`, `single-clip`/`multi-clip`/`general`, `wave`/`beat2`, `keep`/`milestone`/`superseded`, `torso-ik`), with a one-line result note. Run IDs unchanged
- `motion_upload`: every version has a description (bad / superseded / use this); aliases `pelvis-ik` (beat2 v2), `torso-ik` + `current` (beat2 v3), `current` on the wave clips. Old versions kept (runs reference them). `booster-mjlab` project is empty (delete in the web UI; the API can't)

## 2026-10-18: run 0j0flpxj (torso data, resumed to 6k): best general tracker so far

**Run**
- Resume of `fsyy1c2w` from model_3500: `uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name .../beat2-10s-train:v3 --env.scene.num-envs 4096 --agent.resume True --wandb-run-path .../fsyy1c2w --wandb-checkpoint-name model_3500.pt --agent.max-iterations 2500 --agent.run-name beat2-general-v3-resume` (tmux, club GPU), 3.5k → 6k it, 51 min, ~160k env-steps/s
- Reward ~65.3, episode length 500, ~0 terminations, sampler even (top1 ≤ 0.018), every clip fail_rate 0
- Best stretch 5.0–5.5k: error_body_pos 0.0117 m, joint 0.28, action_rate −0.16. **mean_std drifted 0.173 → 0.211 from ~5.6k** (s5cdzms7: from ~6.9k), errors and action_rate up with it; run ended in the dip
- Verdict: done. WandB: `10-18 general v3 torso-IK resume to 6k`, tag `keep`

**Eval** (club GPU; model_5500 and model_5999 on `beat2-10s-heldout:v3`, model_5500 on train `:v3` and held-out `--push`)

| Held-out | model_5999 | model_5500 | s5cdzms7 model_8500 (v2) |
|---|---|---|---|
| Clips 50/50 | **43/43** | 42/43 | 42/43 |
| Hand err all (cm) | 2.85 | **2.73** | 3.05 |
| Nidal / Ayana | 2.02 / 4.58 | **1.89 / 4.46** | 2.29 / 4.62 |
| Body err / arms / head | 0.82 cm / 3.2° / 3.4° | 0.84 / 3.3° / 2.8° | 0.91 / 3.8° / 3.0° |
| Clips with foot tilt > 10° / worst | 12 / 23° | 9 / 51° | 20 / 28° |

- model_5500's 3 failures (5.7–6.6 s, `ee_body_pos`) and the 51° tilt are all on `ayana_0_14_14_t36-46` (5/50 rollouts > 30°); model_5999 does that clip 50/50, hand 4.3 cm, tilt ≤ 10°. Elsewhere 5500 is slightly better (5999 better on 14/43 clips, +0.13 cm mean)
- **Use model_5999** (all clips pass, no extreme foot roll; costs 0.12 cm)
- model_5500 train `:v3`: 101/105 clips, 5244/5250 (5 at t ≤ 0.12 s on the 3 known start-of-clip clips + `miranda_0_9_9_t0-10` at 6.5 s), hands 2.53 cm (Scott 3.73, Wayne 2.17, Solomon 3.05, Lawrence 2.88, Sophie 2.15, Miranda 2.64), foot tilt > 10° on 45/105 (s5cdzms7 v2: 54/103). Pushes: no change (2.73 cm, 1 failure)
- Torso data vs pelvis data: held-out hands −10% (better on 32/43 clips), **Nidal at single-clip level (~1.9 cm)**, foot-tilt clips roughly halved on held-out, train/held-out gap 2.53 / 2.73 cm (was 2.46 / 3.05)

**Takeaways**
- The torso IK config improves posture, tracking, generalization and feet at once: keep it as the default retarget for the K1
- Late-run mean_std drift is now reproducible (2 runs). Next long run: lower `entropy_coef` (`rl_cfg.py`, 0.005 → ~0.001) or cap the std, instead of picking checkpoints around it

## 2026-10-18: Slice 0 video with the torso policy: lean fixed

- Single-clip torso version of the Scott clip: `talk_scott_1_1_t34-44-torso:v0` (trunk lean mean −6.0° [−25, +21] vs −15.1° [−34, +2] in `talk_scott_1_1_t34-44-tracking:v0`)
- Club GPU: `uv run play Mjlab-Tracking-Flat-Booster-K1 --wandb-run-path .../0j0flpxj --wandb-checkpoint-name model_5999.pt --registry-name .../talk_scott_1_1_t34-44-torso:v0 --num-envs 1 --video True --video-length 500 --hide-overlays` → `logs/rsl_rl/k1_tracking/wandb_checkpoints/0j0flpxj/videos/play/rl-video-step-0.mp4`; scp to the laptop, `ffmpeg ... -c:v copy -c:a aac -shortest` with `scott_0_1_1_t34-44.wav` → `logs/videos/0j0flpxj_scott_audio.mp4`; before/after: `ffmpeg ... hstack` → `logs/videos/scott_before_after.mp4`
- Boston: **"considerably better and more natural. The weird lean back is gone."**
- Gotchas: shell variables like `$R` exist only in the shell that set them (on the laptop `$R` was empty → "Unrecognized options: model_5500.pt"). Laptop dGPU still off the PCI bus: `play` works on CPU, evals go to the club GPU
- Slice 0 (`plan.md`): A–G done except the sync check; left: sync check, the "what step 1 must handle" list, EMAGE (optional)

## 2026-10-18: full BEAT2 build (torso config) → beat2-full-torso-train-a / -train-b

**Decisions** (from the plan review): include session-1 conversations as their own sets; hold out 6 speakers (Nidal, Ayana, 20_li, 27_yingqing + 5_stewart, 10_kieks: calm natives, nearly free to hold out); Tier B decided by an A vs A+B comparison after a ground_clip fix. GMR config: torso (`smplx_to_k1_torso.json`) until v3 exists

**Fixes found on the way**
- **Tier B skids:** GMR moves the K1 foot 3–6 cm on a step but lifts it only 5–15 mm (human 3–6 cm), so planting turned steps into slides. `ground_clip` now lifts a foot that travels ≥ 3 cm on a half-sine arc (0.25 × step, 1–3 cm). Waves + Scott clip unchanged; 31/152 v1 clips change, planted skating −24%, slide flags gone, knees +2°
- **GPU memory:** mjlab's MotionLoader kept all 25 bodies *and* an indexed copy on the GPU (2× the file). `LeanMotionLoader` in MultiMotionCommand moves only the tracked bodies: same tensors (new test), ~0.27 GB per hour of reference. train-a ≈ 6.3 GB, A+B ≈ 7.8 GB on the 16 GB club GPU
- **combine-motions:** streams to `--output` one array at a time (peak RAM ~1.3× instead of ~3×); **batched FK** (one sim per worker, 256 frames per forward) is bit-identical and ~25× faster (combine of all 16k clips: ~5 min instead of ~2 h)
- **Laptop heat:** numpy threads × 10 workers pinned the CPU at 100 °C. Single-thread workers (`OMP_NUM_THREADS=1`) + a profile-cycling governor (balanced until chassis 65 °C, power-saver until 52 °C; ~3× power-saver speed) + watchdog. One core at full turbo always reads 100 °C on this laptop; chassis sensors are the real limit. Run future builds on the club PC
- `pkill -f`/`pgrep -f` matched their own shell twice (killed or stopped the command): use PIDs or `[x]`-patterns

**Build:** 1,378 takes → 16,155 clips, 45 h (segments → convert → GMR → ground → QC → combine). Gate 1 recalibrated on the full build (arm-behind severe only > 10 cm: 77% of flags were Sophie's clasped hands just past 5 cm; trunk-drop outlier severe only > 5 cm; self-overlap severe only > 25 mm) → 1,167 severe (GMR flips, ground IK failures 672, feet crossing, 84 real left-arm-behind)
- **Missed by Gate 1, found before training: whole-clip trunk lean.** Two Hailing conversation takes (`23_hailing_1_2_2`, `_1_3_3`) have the pelvis ~33° from vertical for the whole take (head only 10 cm lower: a mocap offset or leaning on something); with the torso config the K1 trunk copies it at 25°. Over all clips the K1's median trunk tilt is 5° (p99 23°, max 136°). New severe check `trunk leans > 15°` (median over the clip): 251 clips → **1,290 severe excluded**. `:v0` artifacts contain these clips; use **`:v1`**. QC table `notes/beat2-full-qc.md`
- Load test: the training env builds from train-a:v1 on CPU in 10 s (7,223 clips, 87,604 bins, 6.18 GB of reference tensors, peak RSS 10 GB), 60 steps fine

| set | clips | hours |
|---|---|---|
| train-a:v1 (Tier A, train + conversation takes, 19 speakers) | 7,223 | 23.3 |
| train-b:v1 (Tier B) | 3,644 | 5.7 |
| val:v0 / heldout-val:v0 | 474 / 194 | 1.3 / 0.8 |
| test:v1 / heldout-test:v1 | 1,298 / 406 | 3.5 / 1.4 |
| heldout-conv:v1 | 1,626 | 5.9 |

- Leakage check clean on both training files. Uploaded with `tools/upload_combined.py` (~6–11 MB/s); club PC: 91 GB free (disk 95% full, shared): clean up downloads after

## 2026-10-19: A vs A+B comparison runs started (club GPU); handoff

**State when this session ended (00:15, Oct 19)**
- Club GPU (`sigrobotics`, `~/bmcox2/booster_mjlab`, tmux session `train`): queued/started run **A** (`train-a:v1`) then **A+B** (local `logs/motions/beat2-full-torso-train-ab.npz` = train-a:v1 + train-b:v1, built with combine-motions), chained with `;`. Both: 4096 envs, 6,000 it, seed 42, `entropy_coef 0.001` (was 0.005; for the late mean_std drift), ~1.6 h each
- W&B names get a timestamp prefix: `2026-10-19_<HH-MM-SS>_10-19-beat2-full-A` / `..._10-19-beat2-full-AB`. Three earlier attempts crashed at startup with CUDA OOM because another user's job (`keshav`, `train_router.py`, 10.4 GB) held the GPU: **`2h7ih3ij`, `kxzph3yx`, `vbsmv80n` are dead** (tagged `oom-crashed`, `superseded`; W&B may show them "running" until it times them out). The real runs are the ones with steps climbing
- Shared GPU: before a run, `nvidia-smi`; A needs ~10 GB (6.2 GB reference + sim), A+B ~11.7 GB, so neither fits next to another 10 GB job. Queue with `until [ "$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits)" -lt 1000 ]; do sleep 120; done; <train ...>`

**Artifacts** (`bmcox2-university-of-illinois-urbana-champaign/motion_upload/`; local copies in `~/robotics/data/beat2_full_torso/combined/`)
- Training: `beat2-full-torso-train-a:v1`, `beat2-full-torso-train-b:v1` (**not `:v0`**: v0 still has the 25° trunk-lean clips)
- Eval: `beat2-full-torso-val:v0`, `-heldout-val:v0` (unchanged by the lean fix), `-test:v1`, `-heldout-test:v1`, `-heldout-conv:v1`. `val` picks checkpoints; `test` is scored once at the end
- Rebuild / inspect: `uv run python tools/beat2_batch.py --spec tools/datasets/beat2_full.toml --no-upload` (all stages cached: ~8 min, mostly segmentation). QC per clip: `~/robotics/data/beat2_full_torso/qc.json`, table `notes/beat2-full-qc.md`. Upload a combined file as-is: `tools/upload_combined.py`

## Next
**1. When both runs finish: compare A vs A+B** (club GPU; ~40k rollouts per val set, batched)
```
source ~/bmcox2/.wandb_env; E=bmcox2-university-of-illinois-urbana-champaign
for RUN in <A-run-id> <AB-run-id>; do for SET in val heldout-val; do
  uv run eval-tracking --wandb-run-path $E/mjlab/$RUN --checkpoint-name model_5999.pt \
    --registry-name $E/motion_upload/beat2-full-torso-$SET:v0 --device cuda:0
done; done
uv run python tools/eval_summary.py logs/eval/<A>_model_5999_beat2-full-torso-val_v0.json logs/eval/<AB>_..._val_v0.json   # per tier + speaker
```
- Decide Tier B: A+B should match A on tier A clips and beat it on `_shift` clips. Also check charts (`/analyze-run`), mean_std with entropy_coef 0.001, and earlier checkpoints on val
- This is also the plan's **Gate 3 probe**: eval the winner on its own training set, watch every clip that fails, remove only artifacts (bad retarget, impossible pose), re-upload, then the final run (longer; stop by val)
- Milestone bars (plan): held-out ≥ 95% clips with no falls and hands ≤ 1.5× training error; training speakers' test ≥ 97%; no regression on the 3 waves + Scott 34–44 s (within 20% of each specialist, 50/50); 5 held-out clips in `play` dubbed with audio look right

**2. Cleanup**
- Club PC (disk 95% full, shared; 91 GB free on Oct 18): after the A+B run `rm logs/motions/beat2-full-torso-train-ab.npz` (7.7 GB) unless still evaluating on it; `rm -rf artifacts/beat2-full-torso-train-b:v1` (1.5 GB, only needed to build A+B); `wandb artifact cache cleanup 1GB`
- Laptop: `wandb artifact cache cleanup 1GB` (`~/.cache/wandb` is 21 GB of upload staging copies). Keep `~/robotics/data/beat2_full_torso` (14 GB: per-clip cache, needed to rebuild/re-flag without re-running GMR) until the v3 rebuild. `~/robotics/data/beat2_full/` (3 MB, segments only) can go
- W&B: delete the 3 `oom-crashed` runs if they clutter; move the `current` alias to the dataset versions in use; tag the comparison runs (`tracking`, `general`, `beat2`)

**3. Data follow-ups (before the v3 rebuild)**
- Gate 2 (not done): histograms per split + watch 20 random + worst clips in `visualize-motions` (step-lift arcs, conversation takes, Tier B). Gate 1 missed the trunk lean; it can miss other things
- ground_clip IK failures: 672 clips (mostly Tier B / conversations) excluded; find why leg IK fails there
- 84 clips with the left arm > 10 cm behind the trunk (GMR IK-start bug signature) despite the HOME-arms seed
- 5–10 cm "arm behind" clips (mostly Sophie's low clasped hands) are now in training as info only: the K1 loses that pose
- v3 GMR config → new `out_dir` + `name` in the spec, rerun. Prefer the club PC (needs GMR + its venv at `~/projects/GMR`); on the laptop use `OMP_NUM_THREADS=1` workers and `tools/laptop_build_governor.sh`
- Build order: training sets first (`--sets train-a train-b`) so runs can start while eval sets build

**4. Older items**
- Slice 0 wrap-up: check audio sync on a stressed word; write the "what step 1 must handle" list (`plan.md` I)
- QC "arms K1" column measures the elbow: switch it to the forearm tip (`*_hand_end_ball`)
- Foot tilt (> 10° on many Lawrence / Solomon clips): check references' foot orientation vs robot; consider a foot-flatness reward
- The 3 clips that fail at t = 0.1 s in eval (`lawrence_0_12_12_t26-36`, `lawrence_0_13_13_t21-31`, `solomon_0_15_15_t43-53`): look at their first frames
- If hands stay well above single-clip: future reference frames in the obs (GMT uses ~2 s) and/or a bigger network
- Why GMR's IK flips the upper-arm twist (`*_Elbow_Pitch`); fixing it would recover the joint-jump clips
- Tell the lead about the milestone 1 change; update `proposal.md` once agreed
- `play` + record videos of me9exatd and pqh0whw0 for the lead
- Still open with lead: K1 ankle model (standard vs `-Parallel`)
