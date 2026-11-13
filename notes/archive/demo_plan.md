# Robot demo plan: BEAT2 tracker on the real K1

Goal: a short demo on the real K1. The robot stands, plays 2–3 talking-gesture clips (10–20 s each) with the speaker's audio from a laptop, and stops. It starts on a gantry or harness. No live speech yet.

## Why the current policy can't go on the robot

The tracking task inherited two observations from mjlab that a real K1 can't measure:
- `motion_anchor_pos_b` is where the reference trunk is relative to the robot's trunk. On the robot it needs the robot's position in the room.
- `base_lin_vel` is the trunk's linear velocity. The IMU only measures acceleration and turn rate.

BeyondMimic trained without both (mjlab's `has_state_estimation=False` for the G1). We do the same:
- **`Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation`** (added 2026-10-28).
- The policy sees the reference joints and joint velocities, the reference trunk orientation relative to its own, the gyro, gravity direction, joint positions and velocities, and its last action.
- The critic, which exists only in sim, still sees everything.

## Status

| Step | Status |
|---|---|
| Real-robot joint limits (upstream `d0b9567`) | **Merged.** Training data goes past them on 5.8% of frames, almost all `Right_Elbow_Yaw` > 2.25 rad (up to 0.19 rad over). The policy learns to stop at the limit. The data fix (GMR's K1 model with the real limits) belongs to the next GMR rebuild |
| Deployable task (no state estimation) | **Done.** A 20-iteration CPU smoke run trains and saves |
| Policy-only ONNX (`policy.onnx`: obs → actions, metadata for the robot) | **Done.** Written next to every checkpoint and to the W&B run files. `uv run export-tracking-policy` does the same for old checkpoints |
| Deploy code, robot-agnostic (`src/booster_mjlab/deploy/`: policy, observation builder, reference player) | **Done.** `tests/test_deploy.py`: observations match mjlab's to 1e-5 |
| Sim2sim in plain MuJoCo (`uv run sim2sim`) | **Done and validated.** `1de2pner` on 3 held-out clips: no falls, hands 2.3 / 2.9 / 3.2 cm (`eval-tracking`: 3.0–3.9). 40 ms sensor delay + pushes: 3/3, 2.8 cm. This used true positions and velocities (`--privileged`, sim only), which a robot can't have |
| **Train the deployable policy** | **Next week, after the lead's answers** (the ankle model may change the robot). Command below |
| Lead-in from standing / end hold | Code done (`Reference.with_lead_in` / `with_end_hold`). Testable only with the new policy |
| Pick demo clips + audio | After training |
| Robot backend (Booster SDK) | After the lead's answers |
| Bring-up on the robot | After that |

## Questions for the lead

1. **Existing deploy code?** Is there K1 deployment code from the velocity policy, or Booster example code for custom low-level control? Reusing it saves the most time.
2. **SDK low-level mode:**
   - How do we enter it from Booster's controller, and how do we hand back control?
   - What is in a command: per motor target position, velocity, kp, kd, feed-forward torque?
   - What rate does it run at, and does the motor driver run the PD loop?
   - What does the state message contain: joint positions and velocities, IMU quaternion and gyro, and their frames?
3. **Joint order and signs** in the SDK, compared with ours (`policy.onnx` metadata `joint_names`, which is `K1_JOINT_ORDER`).
4. **Ankle:** does the SDK expose serial ankle joints (pitch, roll) with the firmware handling the linkage, or the parallel motors? We train `k1.xml` (serial). If it's parallel, the tracking task needs a `k1_parallel` variant before training. Velocity already has one.
5. **Where does the policy run?** On the K1's computer (onnxruntime on ARM, Python version) or on the laptop over Ethernet (latency)? sim2sim tolerated 40 ms of sensor delay.
6. **PD gains:** our arm gains are kp 20 / kd 2 (the tracking task's `_TRACKING_ARMS`). Legs, head and ankles use the K1 defaults. Are these safe and accepted on the real motors?
7. **Safety:** gantry or harness availability, an e-stop or damping-mode key, and who spots.
8. **Demo:** where and when, how long, and whether audio from a laptop speaker is fine.

## Next week (after the answers)

**1. Train (club GPU, ~2–3 h).** If the ankle answer changes the robot model, change it first.
```
source ~/bmcox2/.wandb_env; E=bmcox2-university-of-illinois-urbana-champaign
uv run train Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation \
  --registry-name $E/motion_upload/beat2-full-torso-train-ab:v0 \
  --env.scene.num-envs 4096 --agent.max-iterations 6000 --agent.seed 42 \
  --agent.run-name deploy-nse-train-ab 2>&1 | tee logs/train_deploy_nse.txt
```
- `entropy_coef` 0.001 is now the default.
- The harness warm-up and per-step counting are in.
- Expect slightly worse tracking than `1de2pner`: the policy no longer sees where the reference trunk is.

**2. Evaluate:**
- `eval-tracking --task Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation ...` on `heldout-val:v0` and `val:v1`. Compare with `1de2pner` (194/194, 3.46 cm).
- Then evaluate the flagged clips and review only the ones that still fail.

**3. sim2sim from standing:**
```
uv run sim2sim --wandb-run-path $E/mjlab/<run> --motion-file <file.npz> --clip <name>             # stand -> lead-in -> clip -> hold
uv run sim2sim ... --obs-delay-steps 2 --push --runs 10
uv run sim2sim ... --video logs/videos/<clip>_sim2sim.mp4
```
The lead-in (2 s blend from the home pose + 1 s hold) is the part never trained. If it falls there, try a longer blend, or a clip whose first frame is closer to the home pose.

**4. Pick 2–3 demo clips:**
- 50/50 in `eval-tracking`, including `--push`, and clean in sim2sim from standing;
- within the real joint limits;
- Tier A (no steps), expressive, ideally from a held-out speaker;
- export the matching BEAT2 audio.

**5. Robot backend:** a `deploy/booster_sdk.py` that fills `RobotState` from the SDK state and sends `policy.joint_targets(action)` with the policy's kp and kd. It reuses `deploy/` unchanged, with the same loop as `scripts/sim2sim.py:run_once`. Reference heading: `Reference.aligned_to(imu_quat)` at the start. IMU yaw drift is negligible over 20 s.

**6. Bring-up on the robot**, e-stop ready at every step:
1. Gantry, dry run: compute actions without sending them. Check that joint order, signs and IMU readings match the sim.
2. Gantry: hold reference only.
3. Gantry: a full clip.
4. Feet on the floor with a slack harness: hold, then a clip.
5. Demo with audio started together with the clip. Record video.
