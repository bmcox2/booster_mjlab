# Robot session, Thursday 2026-11-12 (meeting at 6)

First time the gesture tracker runs on the real K1. Goal: a BEAT2 clip on the gantry, then on the floor, then the
K1 "introducing itself" with its own voice. Everything below was rehearsed on the laptop on 2026-11-11 (fake robot).

## What runs where

```
laptop ── ssh ──> K1's computer:  deploy.py  (booster_deploy, folder ~/booster_deploy_gesture)
                                     │  reads /low_state (500 Hz): joint angles + speeds, IMU roll/pitch/yaw + gyro
                                     │  policy y1r48dhc, 50 Hz: observation -> 22 joint targets
                                     └> sends joint_ctrl: per joint target + kp/kd; the motor drivers do the PD
Booster's own modes (RPC):  Walking / Prepare (Booster's controller holds it) -> Custom (we command) -> Damping (limp)
```

- **X** = go to Custom mode and ramp (1 s) to the home pose at **stiff** gains. **A** = start the policy: 2 s blend
  to the clip's first frame, 1 s hold, the clip, then hold the last frame. **Ctrl-C** = stop -> exit mode (default
  **Damping: the robot goes limp**).
- The policy only sees what the robot measures (no position, no linear velocity): that's why it's `y1r48dhc`.
- Safety stop built in: trunk > 60° from the reference -> policy stops -> Damping. Targets are clamped to joint limits.
- Never hold the robot at the **policy's** gains without the policy running: too soft, it tips (sim: 22° in 1 s).

## Before (laptop, 1–2 h)

1. Read this card and `~/projects/booster_deploy/docs/k1_gesture_deploy.md`.
2. Rehearse on the fake robot (same commands and buttons; type `x` / `r`):
   ```
   cd ~/projects/booster_deploy
   R="uv run --project ../booster-mjlab --with evdev --with pyyaml --with-editable ../booster_assets python"
   $R scripts/fake_robot.py --viewer -- --task k1_gesture_tracking --motion tasks/gesture_tracking/motions/ayana_0_9_9_t52-69.npz --dry-run
   $R scripts/check_dry_run.py $(ls -t logs/dry_run_*.npz | head -1)      # expect "RESULT: no problems found"
   $R scripts/fake_robot.py --viewer -- --task k1_gesture_tracking --motion tasks/gesture_tracking/motions/ayana_0_9_9_t52-69.npz
   $R scripts/fake_robot.py --swap left_shoulder_roll_joint,right_shoulder_roll_joint -- --task k1_gesture_tracking --motion tasks/gesture_tracking/motions/ayana_0_9_9_t52-69.npz --dry-run
   ```
   The last one is a deliberate wiring mistake: see what `check_dry_run.py` says when something is wrong.
3. Watch the clips you'll run: `logs/videos/bd_*.mp4` (robot code's own simulator) and
   `logs/gesture/replies/demo_intro/sim_audio.mp4` (the self-introduction, with its voice).
4. Charge the laptop. Bring the controller question list (below).

## At the robot

**0. Connect and copy** (campus network):
```
cd ~/projects/booster_deploy
scripts/sync_to_robot.sh --check     # which environment has onnxruntime + torch; speakers; mics
scripts/sync_to_robot.sh             # copies to ~/booster_deploy_gesture (the club's checkout isn't touched)
ssh booster@10.193.169.55
cd ~/booster_deploy_gesture && source <env marked OK>/bin/activate && source /opt/booster/BoosterRos2Interface/install/setup.bash
python -m pytest tests/test_gesture_tracking.py -q       # same results as on the laptop?
```
If no environment has onnxruntime: `pip install onnxruntime` into the club's environment only with the lead's OK.

**1. Dry run** (robot standing under Booster's controller, or hanging on the gantry). Sends nothing, never changes mode.
```
python scripts/deploy.py --task k1_gesture_tracking --motion tasks/gesture_tracking/motions/ayana_0_9_9_t52-69.npz --dry-run
```
Press **A**, wait ~10 s, Ctrl-C, then `python scripts/check_dry_run.py logs/dry_run_k1_gesture_tracking_<time>.npz`.
- Good: loop ~50 Hz, `/low_state` updating, "RESULT: no problems found", first targets within 0.3 rad of the joints.
- Then have someone move **one** arm joint by hand during a second dry run: only that row should change, in the
  direction you expect. That checks joint order **and signs**, the one thing the laptop can't.
- Anything flagged: **stop**. A large first target on one joint pair = order or sign mismatch.

**2. Gantry, hold only:** run without `--dry-run`, press **X**, don't press A. Watch the 1 s ramp: smooth, no buzzing.
Ctrl-C -> it goes limp (fine on the gantry).

**3. Gantry, clip:** X, then A. Watch the **ankles** (open question: does the firmware apply our ankle kp/kd per joint
or per motor?), listen for buzzing, look for a joint pressing into a stop. Stop on any of those.

**4. Floor, slack harness, spotter's hands near:** same clip. Before it: decide the exit mode with the lead
(`--exit-mode walking` hands back to Booster's controller instead of going limp, if that's how this firmware works).
Press A soon after X (in Booster's own model the robot tipped forward within 2 s at the X pose; ours stood fine).

**5. Demo:** the K1 introduces itself, gestures generated from its own voice:
```
python scripts/deploy.py --task k1_gesture_tracking --motion tasks/gesture_tracking/motions/demo_intro.npz \
    --audio tasks/gesture_tracking/motions/demo_intro.wav
```
The audio plays on the robot (needs a speaker: `--check` lists them). No speaker: play `demo_intro.wav` from the
laptop when the terminal prints `clip starts`. Other clips: `ayana_0_15_15_t75-95`, `yingqing_0_9_9_t48-59`,
`ayana_0_11_11_t8-23` (all with `.wav`).

## Measurements while you're there (roadmap step 1)

- **Mics with motors on** (for the speech loop on the robot): during a gantry clip,
  `arecord -d 15 -f S16_LE -r 16000 -c 1 ~/mic_motors.wav` on the robot (`arecord -l` lists the mics); copy it back.
- **Laptop ↔ robot round trip:** `ping -c 100 10.193.169.55` from the laptop (the speech loop + gesture service may
  stay on the laptop and stream references to the robot).
- **Arms only while Booster holds the legs?** Ask, or check whether the SDK has an upper-body mode.
- Keep every dry-run log and note what you saw per step (for `notes/log.md`).

## Questions for the lead

1. Ankles: does the firmware apply joint_ctrl kp/kd per serial joint (pitch/roll) or per parallel motor? Firmware version?
2. Exit mode off the gantry: Damping (limp) or back to Booster's controller?
3. Gantry, e-stop or damping key, who spots.
4. Does the K1 have a speaker for `aplay`, and which mics?
5. Can the SDK drive arms + head while Booster's controller balances the legs?
6. Are the joint limits in `K1_22dof.xml` the real ones?

## If something goes wrong

| You see | Likely | Do |
|---|---|---|
| `check_dry_run.py` flags a large first target | joint order or sign differs | stop; compare the flagged joints with K1_CFG's order |
| "Waiting for first '/low_state' message" forever | ROS setup not sourced, or another process holds the robot | `source /opt/booster/...setup.bash`; ask the lead |
| "Failed to switch to Custom mode" | robot not in a mode that allows it | put it in Prepare/standing with the controller first |
| Buzzing / shaking joints | gains too high for the real motor (ankles first) | Ctrl-C; note which joint |
| Robot leans and the safety stop fires | tracking failed (real-robot gap) | gantry first; try another clip; note when |
| Import error for onnxruntime / torch | wrong environment | `--check` again; the env marked OK |
