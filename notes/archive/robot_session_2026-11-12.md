# Robot session runbook, Thursday 2026-11-12 (meeting at 6)

First time the gesture tracker runs on the real K1. Follow the steps in order; each one only starts if the one before
looked right. Every command is here. **[LAPTOP]** = type it in a terminal on your laptop. **[ROBOT]** = type it in
the SSH window, where it runs on the K1's own computer.

**Stop rules (any step):** Ctrl-C at once on buzzing or shaking joints (ankles first), a joint pressing into its stop,
a sudden jump, or the robot leaning away. Write down which joint and when. Don't go on to the next step until the
cause is understood. Someone other than you holds the e-stop / damping key: if your SSH connection drops, your Ctrl-C
can't reach the robot.

## How it works (one paragraph)

`deploy.py` runs on the K1. 50×/s it reads `/low_state` (joint angles and speeds, IMU tilt and gyro), runs the
policy `y1r48dhc` (it sees only what the robot measures), and sends 22 joint targets + gains; the motor drivers do
the PD control. Buttons: **X** (keyboard `x`) = take control from Booster's controller and ramp 1 s to the home pose
at stiff gains. **A** (keyboard `r`) = start the policy: 2 s blend to the clip's first frame, 1 s hold, the clip
(terminal prints `clip starts`), then hold the last frame. **Ctrl-C** = stop: the robot goes **limp** (Damping)
unless you passed `--exit-mode walking`. Built-in safety: trunk > 60° from the reference → stop + limp; targets
clamped to joint limits. Nothing listens to the mic tonight; nothing is generated live. All clips are fixed files.

---

## Part A: before you leave (laptop, ~30 min)

**A1. Rehearse on the fake robot** (the real `deploy.py` against a simulated K1; same buttons, type `x` then `r`).
[LAPTOP]
```
cd ~/projects/booster_deploy
R="uv run --project ../booster-mjlab --with evdev --with pyyaml --with-editable ../booster_assets python"
$R scripts/fake_robot.py --viewer -- --task k1_gesture_tracking --motion tasks/gesture_tracking/motions/ayana_0_9_9_t52-69.npz
```
Watch: `x` → 1 s ramp to home; `r` → blend, `clip starts`, gestures, end hold; Ctrl-C → slumps. Checked unattended
2026-11-12: 0 falls, max tilt 6°.

**A2. Watch what "normal" looks like** [LAPTOP] (VLC crashes from VS Code's terminal; use `ffplay`):
```
ffplay ~/projects/booster-mjlab/logs/gesture/replies/demo_intro/sim_audio.mp4
ffplay ~/projects/booster-mjlab/logs/videos/bd_ayana_0_9_9_t52-69.mp4
```
(Others: `logs/videos/bd_<clip>.mp4` for each demo clip below.)

**A3. Bring:** laptop **charged** + charger, **USB-C Ethernet adapter + cable** (the XPS has no Ethernet port),
phone to **film every run**, this runbook open.

---

## Part B: at the robot, before touching anything (ask the lead / Anatulya)

1. **How do I reach the K1's computer?** IP, user, password, which network (cable / robot Wi-Fi / campus)?
   Booster's defaults: cable, `booster@192.168.10.102`, password `123456` (or `booster123`).
   **Not 10.193.169.55**: that's the club GPU PC.
2. Where's the gantry, who holds the e-stop / damping key, who spots?
3. Off the gantry, at the end of a run: go limp (Damping, our default) or hand back to Booster's controller
   (`--exit-mode walking`)?
4. Ankles: does the firmware apply our joint_ctrl kp/kd per serial joint (pitch/roll) or per parallel motor?
   Firmware version?
5. Speaker on the K1 for `aplay`? Which mics?
6. Can the SDK drive arms + head while Booster's controller balances the legs?
7. Are the joint limits in `K1_22dof.xml` the real ones?

---

## Part C: connect and copy

**Step 1. Network.**
- *Cable:* plug in the adapter + cable. Settings → Network → the new **Wired / USB Ethernet** entry → gear icon →
  **IPv4** tab → **Manual**: Address `192.168.10.10`, Netmask `255.255.255.0`, Gateway **blank** (a gateway here
  can steal your internet from Wi-Fi) → Apply → switch the wired connection off and on.
- *Wi-Fi:* the robot's IP is in the Booster app; laptop on the same network.

[LAPTOP]
```
ping -c 3 192.168.10.102            # or the Wi-Fi IP. Replies = connected
```

**Step 2. Check the robot's software** (reads only, changes nothing). [LAPTOP]
```
cd ~/projects/booster_deploy
export ROBOT=booster@192.168.10.102  # or what the lead told you
scripts/sync_to_robot.sh --check
```
Read the output:
- The first line names the machine. If it says `sigrobotics`, the script stops: wrong machine.
- `ROS 2 / booster_interface setup`: must show the `setup.bash` path. Missing → ask the lead where it is.
- `system python3: OK ...` or an environment line ending `OK ...` = that Python can run the policy. **Note which.**
  None OK → ask the lead before installing anything (`pip install onnxruntime` into the club's environment).
- `speakers:` → whether demo audio can play on the robot. `microphones:` → card numbers for the mic recordings.

**Step 3. Copy your files** (into `~/booster_deploy_gesture`; the club's checkout isn't touched; 34 MB). [LAPTOP]
```
scripts/sync_to_robot.sh
```
Changed something on the laptop later? Run this again.

**Step 4. Log in and set up the shell.** [LAPTOP] `ssh $ROBOT`, then [ROBOT]:
```
cd ~/booster_deploy_gesture
source <environment marked OK>/bin/activate        # skip if only "system python3: OK"
source /opt/booster/BoosterRos2Interface/install/setup.bash
M=tasks/gesture_tracking/motions
python3 -m pytest tests/test_gesture_tracking.py -q  # expect "2 passed"; "No module named pytest" = skip it
```
Redo Step 4's last 3 `source`/`M=` lines in every new SSH window.

**Step 4b. Quiet mic recording** (baseline for later; motors not running). [ROBOT]
```
arecord -l                                           # lists mics: "card N ... device D"
arecord -d 15 -f S16_LE -r 16000 -c 1 ~/mic_quiet.wav     # add -D plughw:N,D to pick a mic; talk normally from 1 m
```

---

## Part D: bring-up ladder (one clip: `ayana_0_9_9_t52-69`)

**Step 5. Dry run, robot standing** (under Booster's controller, or hanging on the gantry). Sends **nothing**, never
changes the mode: zero risk. [ROBOT]
```
python3 scripts/deploy.py --task k1_gesture_tracking --motion $M/ayana_0_9_9_t52-69.npz --dry-run
```
Press **A** (or type `r`), wait ~10 s, Ctrl-C. Then:
```
python3 scripts/check_dry_run.py $(ls -t logs/dry_run_*.npz | head -1)
```
Good: `loop period median 20.0 ms`, `joint readings unchanged ... 0 of ...` (or a few), trunk tilt small,
first targets under 0.3 rad, **`RESULT: no problems found`**. Any `CHECK` line → **stop**; a large first target
on one left/right pair = joint order or sign mismatch (laptop rehearsal of exactly that: shoulder roll 1.17 rad).

**Step 6. Sign check: move an arm by hand** (gantry, robot limp / Damping so the arm moves freely). The one thing
the laptop can't check. [ROBOT]
```
python3 scripts/deploy.py --task k1_gesture_tracking --motion $M/ayana_0_9_9_t52-69.npz --dry-run
```
Press A, keep still 2 s, then a helper **slowly lifts the LEFT arm straight forward** (~45°), holds 2 s, lowers it.
Ctrl-C, then `python3 scripts/check_dry_run.py $(ls -t logs/dry_run_*.npz | head -1)` and read the last two sections:
- `Joints that moved`: only left-arm joints (mostly `aaleft_shoulder_pitch_joint`, going **negative**).
- `Hand movement`: `left hand  NN cm forward ... up`.
Repeat with the **right arm forward** (expect `right hand ... forward ... up`) and the **left arm out to the side**
(expect `left_shoulder_roll_joint` from about −1.4 toward 0, `left hand ... left ... up`).
A hand reported moving the opposite way = that joint's sign is flipped → **stop**. In this step a `CHECK` on the
first-target line is expected (a hanging robot isn't in its home pose); judge only the two movement sections.
If it says `hand directions need mujoco + the K1 model`, copy the log and check on the laptop: [LAPTOP]
```
scp "$ROBOT:booster_deploy_gesture/logs/dry_run_*.npz" ~/projects/booster_deploy/logs/
cd ~/projects/booster_deploy && $R scripts/check_dry_run.py $(ls -t logs/dry_run_*.npz | head -1)
```
(`$R` from A1.)

**Step 7. Gantry, hold only** (first time anything is commanded). [ROBOT]
```
python3 scripts/deploy.py --task k1_gesture_tracking --motion $M/ayana_0_9_9_t52-69.npz
```
Press **X only** (not A). Watch the 1 s ramp: smooth, no buzzing, holds still. Wait ~5 s, Ctrl-C → goes limp
(fine on the gantry).

**Step 8. Gantry, the clip.** Same command; **X**, then **A**. ~3 s blend + hold, `clip starts`, 17 s of gestures,
then it holds the last pose; Ctrl-C once it holds still. Film it. Watch:
- **ankles** (the firmware gain question): steady, no chatter;
- listen for buzzing; look for a joint pressing into a stop;
- arms should look like `bd_ayana_0_9_9_t52-69.mp4` (the legs dangle differently on the gantry; that's fine).

**Mic with motors on** (during a second Step 8 run): open a 2nd SSH window ([LAPTOP] `ssh $ROBOT`), and right after
pressing A in the first window: [ROBOT] `arecord -d 15 -f S16_LE -r 16000 -c 1 ~/mic_motors.wav` (same `-D` as 4b),
talking normally from 1 m.

**Step 9. Floor** (slack harness, spotter's hands near, exit mode decided in Part B). Robot standing under Booster's
controller first. [ROBOT]
```
python3 scripts/deploy.py --task k1_gesture_tracking --motion $M/ayana_0_9_9_t52-69.npz      # add --exit-mode walking if the lead said so
```
X, then **A within ~2 s** (Booster's model tipped forward within 2 s at the X pose; ours stood, but don't wait).
Watch the feet (flat, not sliding or rolling), sway, ankles. Ctrl-C after the end hold. Film it.

---

## Part E: demos (floor, after Step 9 went cleanly)

Same pattern for each: command, X, A, watch, Ctrl-C after the end hold. `--audio` plays the clip's sound on the
robot from the first clip frame. **No speaker on the robot** (Step 2)? Leave `--audio` out and, on the laptop, start
the sound the moment the robot's terminal prints `clip starts`: [LAPTOP]
`ffplay -nodisp -autoexit ~/projects/booster_deploy/tasks/gesture_tracking/motions/<clip>.wav`

The BEAT2 clips are real people talking (motion-captured, retargeted to the K1) from **held-out speakers the
policy never trained on**; their audio is the person's own voice. In sim, every demo: 10/10 runs without a fall with
pushes + 40 ms delay.

**Demo 1: `demo_intro`, the K1 introduces itself (11.8 s).** The only generated clip: Kokoro voice ("Hi everyone,
I'm K1. I'm learning to talk with my hands...") and gestures picked by our retrieval generator to match that voice
(persona Miranda). Made in advance, plays like any clip. The motion starts 0.44 s before the voice on purpose
(people's hands lead their speech). Sim: hands 1.9 cm off the reference (best of all clips).
Look for: do the gesture strokes land on the stressed words ("talk with my **hands**", "pretty **cool**")?
Does it read as talking, not as random arm waving? [ROBOT]
```
python3 scripts/deploy.py --task k1_gesture_tracking --motion $M/demo_intro.npz --audio $M/demo_intro.wav
```

**Demo 2: `ayana_0_11_11_t8-23`, calm speaker (15.2 s).** Ayana talking, the calmest of the picks (hands fast 20% of
the time), foot tilt 6.6° in eval (Demo 4: 8.9°), sim hands 2.2 cm. The safest clip: if something looked marginal earlier, use this one.
Look for: smooth, small gestures; feet completely still. [ROBOT]
```
python3 scripts/deploy.py --task k1_gesture_tracking --motion $M/ayana_0_11_11_t8-23.npz --audio $M/ayana_0_11_11_t8-23.wav
```

**Demo 3: `yingqing_0_9_9_t48-59`, another speaker (11.1 s).** Yingqing: a different person's gesture style, the
shortest clip. Sim hands 2.7 cm. Look for: a visibly different style from Ayana's; same steadiness. [ROBOT]
```
python3 scripts/deploy.py --task k1_gesture_tracking --motion $M/yingqing_0_9_9_t48-59.npz --audio $M/yingqing_0_9_9_t48-59.wav
```

**Demo 4: `ayana_0_15_15_t75-95`, the hardest (19.9 s).** Longest clip; the right elbow reaches its joint limit on
~4% of frames (the target is clamped there) and it had the most foot tilt in eval (8.9°). Sim hands 2.4 cm. Run it
last. Look for: the **right elbow** at its limit (pressing, buzzing?), the feet rolling. [ROBOT]
```
python3 scripts/deploy.py --task k1_gesture_tracking --motion $M/ayana_0_15_15_t75-95.npz --audio $M/ayana_0_15_15_t75-95.wav
```
(`ayana_0_9_9_t52-69` from Step 9 also has a `.wav`: the top-ranked clip, the most energetic: hands fast 30% of
the time, within joint limits, sim hands 3.1 cm.)

---

## Part F: measurements and wrap-up

**Round trip** (for later: the speech loop + gesture service may stay on the laptop and stream to the robot).
[LAPTOP] `ping -c 100 <k1-ip>`: note min / avg / max and losses, over cable and (if possible) Wi-Fi.

**Copy everything back.** [LAPTOP]
```
mkdir -p ~/projects/booster-mjlab/logs/robot_2026-11-12
scp -r "$ROBOT:booster_deploy_gesture/logs" ~/projects/booster-mjlab/logs/robot_2026-11-12/
scp "$ROBOT:mic_*.wav" ~/projects/booster-mjlab/logs/robot_2026-11-12/
```
Plus the phone videos. Write per step what you saw (worked / stopped, which joint, ankles, buzzing, audio sync),
then `/log-session` at home.

---

## If something goes wrong

| You see | Likely | Do |
|---|---|---|
| `sync_to_robot.sh` says it's the club GPU PC | wrong IP | get the K1's address (Part B 1) |
| `Permission denied` on ssh | wrong password / user | ask the lead |
| "Waiting for first '/low_state' message" forever | ROS setup not sourced, or another process holds the robot | Step 4's `source` line; ask the lead |
| `check_dry_run.py` flags a large first target | joint order or sign differs | stop; compare the flagged joints with `K1_CFG`'s order |
| Step 6: hand moves the wrong way | that joint's sign is flipped on this robot | stop; note the joint |
| "Failed to switch to Custom mode" | robot not in a mode that allows it | Prepare / standing with Booster's controller first |
| Buzzing / shaking joints | gains too high for the real motor (ankles first) | Ctrl-C; note which joint |
| Robot leans and the safety stop fires | tracking failed (real-robot gap) | gantry first; try Demo 2's calm clip; note when |
| Import error for onnxruntime / torch | wrong environment | Step 2 `--check`; the env marked OK |
| No sound with `--audio` | no speaker / `aplay` device | laptop `ffplay` at `clip starts` (Part E) |
