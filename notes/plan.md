# Milestone 1 Plan: K1 Tracks One Gesture in Sim

Milestone 1 = the K1 tracks one gesture in sim without falling. Training is only the
last step. Getting a clean gesture clip onto the K1 runs on CPU, so most of it can be
done now.

## High-level plan

| Phase | Goal | Needs GPU? |
|---|---|---|
| A. Source data | Find 3–5 candidate gesture clips in AMASS | No |
| B. Retarget | Convert one clip to K1 motion with GMR | No (GMR runs on CPU) |
| C. Verify + upload | Confirm it looks right on the K1, then push it to WandB | No |
| D. Train + evaluate | LAFAN baseline first, then train on the gesture | Yes |
| E. Expand | Repeat B–D for 5–10 gestures | Yes |

A–C is this week's work, and it's what blocks training anyway.

## A. Source data

- [x] **A1. Register for the datasets.** Make accounts on the AMASS and SMPL-X sites.
  Both need a license sign-up and approval isn't always instant, so do this first.
- [x] **A2. Download the SMPL-X body models** into GMR's `assets/body_models/smplx/`
  (neutral, female, male).
- [x] **A3. Download AMASS in SMPL-X format.** GMR says not to use the SMPL+H version.
  Start with one or two subsets, not all of them.
- [x] **A4. Find gesture clips with HumanML3D.** It has text descriptions for AMASS clips
  plus an index with start/end frames. Grep the texts for "wave", "point", "gesture",
  "shrug", etc., then map the hits back to AMASS files.
- [x] **A5. Pick candidates** using these filters:
  - Feet stay planted; the upper body does the work.
  - 2–6 s long, or can be trimmed to that.
  - The gesture doesn't depend on fingers or wrist rotation. GMR's K1 model has 4 DoF
    per arm (no wrist) and the robot has no hands. A point or wave from the elbow works;
    a thumbs-up doesn't.

**Done when:** 3–5 candidates are listed in `notes/log.md`, each with file path and frame range.

## B. Retarget (one clip)

- [x] **B1. Install GMR** in its own environment, separate from booster_mjlab's. It's
  tested on Python 3.10: `uv venv --python 3.10`.
- [x] **B2. Retarget one clip:**
  ```
  python scripts/smplx_to_robot.py --smplx_file <clip>.npz --robot booster_k1 --save_path out/<name>.pkl --rate_limit
  ```
  A MuJoCo window shows the result as it runs.
- [ ] **B3. Trim** to the gesture segment if the clip has walking or idling at the start or end.

**Done when:** one `.pkl` looks like the gesture in GMR's viewer.

## C. Verify + upload

- [ ] **C1. Watch it in booster_mjlab's viewer** with `uv run visualize-motions`. This is
  the important check: it confirms GMR's K1 model and booster_mjlab's K1 agree on joints
  and ankle setup. Look for flipped joints, feet sliding or going through the floor, and
  self-collision.
- [x] **C2. Upload it:**
  ```
  uv run upload-motion --input-file out/<name>.pkl --entity bmcox2-university-of-illinois-urbana-champaign
  ```
  Save the artifact name in the log.
- [ ] **C3. Define metrics now, before training:** tracking error and falls over 50
  rollouts (as in `proposal.md`). That way results are judged against a target set in advance.

**Done when:** the clip plays cleanly in booster_mjlab and the artifact name is in the log.

## D. Train + evaluate (when GPU time is available)

- [ ] **D1. Run the LAFAN baseline first.** Train tracking on one LAFAN walking clip
  (`whirlwind-ams/lafan_locomotion_k1`). If the gesture run fails later, this tells you
  the problem is the clip, not the pipeline.
- [ ] **D2. Train on the gesture clip.** Same command, with the artifact name as the registry name:
  ```
  uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name <artifact> --env.scene.num-envs 4096
  ```
- [ ] **D3. Evaluate.** Watch it with `uv run play`, then record tracking error and falls.
- [ ] **D4. Ask about the club GPU** if the laptop is too slow or overheats.

**Done when:** the K1 performs the gesture in `play` without falling. That completes the
single-gesture goal.

## E. Expand

- [ ] Run B–D for the remaining gestures.
- [ ] Decide between per-gesture policies and one multi-clip policy (the proposal says one
  policy for the library).
- [ ] Present results to the club.

## Next up

Tonight: submit the AMASS and SMPL-X registrations (A1), since everything else waits on
them. Then install GMR (B1).
