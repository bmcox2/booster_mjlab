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

## Next
- First multi-clip GPU run (club GPU): `combine-motions` the 2 waves (+ `talk_scott_1_1_t34-44:v0`) → train → eval per clip; compare each clip with its single-clip run
- `play` `z17z0n1q` + record the video, dub in `scott_1_1_t34-44.wav`, check sync (Slice 0 step G)
- The 20 s stepping window (`--max-foot-move 0.15`)
- Optionally download more BEAT2 speakers and rerun `--find-still`
- Tell the lead about the milestone 1 change; update `proposal.md` once agreed
- `play` + record videos of me9exatd and pqh0whw0 for the lead
- Still open with lead: K1 ankle model (standard vs `-Parallel`)
