# Deploy audit: gesture tracker on the real K1 through `booster_deploy`

Date: 2026-11-05. Analysis only: no code changed, nothing trained. Compared `gesture-tracking` (`c454ee7`) with `anatulya/booster_deploy` (`main` `9a677ad`, `hoi-dev` `295ce53`) and `BoosterRobotics/booster_assets` (`12a9751`).

## Summary

- **`Mjlab-Tracking-Flat-Booster-K1` (`1de2pner`) can't run on the robot.** Two of its nine policy inputs need measurements the K1 doesn't have.
- **The fix is already trained.** W&B run **`y1r48dhc`** (`deploy-nse-train-ab`, finished 2026-10-29, 6k it, `train-ab:v0`) uses the no-state-estimation task. Its `policy.onnx` has the right shape. It wasn't in `notes/log.md` before this audit. Evaluated since: 193/194 held-out clips, hands 3.82 cm (`1de2pner`: 194/194, 3.46 cm).
- **`booster_deploy` has a closer template than the velocity and HOI tasks:** `tasks/beyond_mimic/` on `main` already plays reference motion on the K1. It can't be reused unchanged: wrong joint order, no `projected_gravity`, wrong action scale.
- **Your serial-ankle training fits the robot's interface.** The ankles are physically parallel, but the firmware accepts and reports serial pitch/roll. Real bag data confirms this.
- **One open risk could force a retrain:** what the firmware does with ankle `kp`/`kd`.

## How this was checked

| Evidence | What it is |
|---|---|
| Training envs | Built both tasks on CPU and dumped the real terms, shapes, gains and action scales, instead of reading configs alone |
| ONNX files | `1de2pner`, `y1r48dhc` and `baseline.onnx`: graph, shapes, metadata |
| `tests/test_deploy.py` | 2 passed: `deploy/` rebuilds mjlab's actor observation to 1e-5 |
| **Real K1 bags** | Two `/low_state` rosbags on `hoi-dev` (`logs/k1_mjlab_velocity_flat_20261001-*`), 8.0 s and 7.5 s |
| MJCF comparison | `k1.xml`, `K1_22dof.xml` and GMR's `K1_serial.xml`, by position |

Not done:
- No `booster_deploy` code was executed (only read), so its ONNX loader was checked by reading it and calling `onnxruntime` directly.
- Nothing ran on the robot or in `booster_deploy`'s MuJoCo.
- The bags contain no `/joint_ctrl` messages, so the gains actually sent to the motors aren't recorded.
- Collision geoms weren't compared.

---

# Audit 1: Observation deployability

## Policy (actor) terms

The list comes from three layers: mjlab's base (`.venv/.../mjlab/tasks/tracking/tracking_env_cfg.py:47-80`), your `projected_gravity` addition (`src/booster_mjlab/tasks/tracking/tracking_env_cfg.py:24-27`), and the removal in the deployable variant (`config/k1/env_cfgs.py:188-190`).

`MultiMotionCommand` adds no terms. It only moves `time_steps`, so every term reads the right clip through inherited properties. No clip ID or phase reaches the policy, which is why it can follow any reference, including generated motion later.

| Term | Shape | What it measures | Source | Verdict | Why |
|---|---|---|---|---|---|
| `command` | 44 | Reference joint positions (22, absolute) and velocities (22) | `generated_commands` → `MotionCommand.command` (`mdp/commands.py:127`) | **AVAILABLE** | Comes from the clip the deploy task replays |
| `motion_anchor_pos_b` | 3 | Where the reference trunk is, relative to the robot's trunk | `mdp/observations.py:18` | **SIM-ONLY** | Needs the robot's position in the room. `/low_state` has none, and `booster_robot_controller.py:231` writes zeros |
| `motion_anchor_ori_b` | 6 | Reference trunk orientation in the robot's trunk frame (first 2 columns of the rotation matrix) | `mdp/observations.py:31` | **AVAILABLE** | IMU orientation + reference, once the clip's heading is aligned to the robot's |
| `base_lin_vel` | 3 | Trunk linear velocity | `builtin_sensor(imu_lin_vel)`, a MuJoCo velocimeter | **SIM-ONLY** | An IMU measures acceleration, not velocity. Line 234 also writes zeros |
| `base_ang_vel` | 3 | Trunk turn rate | `builtin_sensor(imu_ang_vel)` | **AVAILABLE** | `imu_state.gyro` |
| `joint_pos` | 22 | Joint angle minus default pose | `joint_pos_rel(biased=True)` | **AVAILABLE** | `motor_state_serial[i].q` minus the training default |
| `joint_vel` | 22 | Joint velocity | `joint_vel_rel` | **AVAILABLE** | `motor_state_serial[i].dq` |
| `actions` | 22 | The policy's previous raw output | `last_action` | **AVAILABLE** | The deploy task stores it |
| `projected_gravity` | 3 | Gravity direction in the trunk frame | `projected_gravity` (your override) | **AVAILABLE** | Computed from IMU roll/pitch. **`BeyondMimicPolicy` doesn't build it** |

| Task | Actor size | Deployable? |
|---|---|---|
| `Mjlab-Tracking-Flat-Booster-K1` | 128 | No, it has both sim-only terms |
| `...-No-State-Estimation` | **122** (44+6+3+22+22+22+3) | Yes |

**The silent failure to avoid.** On the robot, `root_pos_w` and `root_lin_vel_w` are zeros, while in `booster_deploy`'s MuJoCo controller they are true values. A policy wired to use them would look fine in sim2sim and get garbage on the robot, with no error.

**Hardware checks from the bags:**
- IMU: `acc` points opposite to the gravity computed from roll/pitch: (0.026, -0.006, 1.0) vs (-0.027, 0.006, -1.0). So the roll/pitch signs and the gravity term are right.
- Gyro: the sign agrees with the change in `rpy` on the axis that moved most (pitch, correlation 0.67 after smoothing). Roll and yaw barely moved, so those are weaker (0.39, 0.45).
- `dq`: tracks the change in `q` on hips, knees and ankles (correlation 0.87-0.99).
- Noise while standing: gyro std ≤ 0.005 rad/s (training noise ±0.2), joint velocity std ≤ 0.015 rad/s (training ±0.5). Well inside training, but this is standing only.
- Heading: `rpy` yaw started at 0.784 rad in both bags, so heading alignment is required. It didn't visibly drift over 8 s standing. Re-align at each clip start, and watch this for long conversations.

## Critic terms (training only)

355 values: `command` 44, `motion_anchor_pos_b` 3, `motion_anchor_ori_b` 6, `body_pos` 75, `body_ori` 150, `base_lin_vel` 3, `base_ang_vel` 3, `joint_pos` 22, `joint_vel` 22, `actions` 22, `projected_gravity` 3, `foot_height` 2.

The critic is the training-time network that estimates how good a state is, so that PPO can improve the actor. It may use sim-only data because it never runs on the robot. **Confirmed:** the exported ONNX contains only the actor (input `[1, 122]`, no 355-wide layer). This is why the deployable task keeps the sim-only terms in the critic: they help training and cost nothing at deployment.

## Is there a no-state-estimation variant?

Yes, in both places:
- mjlab: `has_state_estimation=False` for the G1 (`mjlab/tasks/tracking/config/g1/env_cfgs.py:74`).
- Your repo: `Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation` (`config/k1/__init__.py:18`).

Retraining means a fresh run. The input layer changes from 128 to 122, so `1de2pner`'s weights can't be loaded. The cost is about 2-3 h on the club GPU, and tracking may be somewhat worse because the policy no longer sees where the reference trunk is. Without that position feedback the robot can also slowly drift across the floor, which matters less for a stationary robot than for Tier B foot shifts.

**This run already exists. No new run is needed for this reason:**

| `y1r48dhc` | |
|---|---|
| Command | `train ...-No-State-Estimation --registry-name .../beat2-full-torso-train-ab:v0 --env.scene.num-envs 4096 --agent.max-iterations 6000 --agent.seed 42 --agent.run-name deploy-nse-train-ab` (host `sigrobotics`) |
| `policy.onnx` | `obs [1, 122]` → `actions [1, 22]`, `has_state_estimation: False` |
| End-of-training numbers | Episode length 500 (full 10 s), `error_body_pos` 0.016, `mean_std` 0.113, 0 terminations in the final summary |
| **Held-out eval** (2026-11-05, `heldout-val:v0`, 50 rollouts per clip) | 193/194 clips all-pass, 100.0% of rollouts (rounded), hands **3.82 cm**. `1de2pner`: 194/194, 100.0%, 3.46 cm |
| **Missing** | `val:v1` comparison |

---

# Audit 2: Training vs deployment config

## Comparison

"Deploy value" is `K1_CFG` (`booster_deploy/robots/k1.py`) unless stated. A task can override any of these, as `mjlab_velocity` does.

| Item | Training | Deploy | Status | What to do |
|---|---|---|---|---|
| Joint order (`joint_names`) | XML order: head, L arm, R arm, L leg, R leg | Same order, by position | **Match** | Verified below. Compare by position, because the names never match |
| Joint order (`sim_joint_names`) | XML order | Isaac breadth-first order, used by `beyond_mimic` | **Mismatch, dangerous** | Set `sim_joint_names = joint_names` in the new task |
| Joint names | `Head_Yaw`... | `aahead_yaw_joint`... (22 of 22 differ) | Mismatch, harmless | Don't map by name. Keep an explicit positional list and assert it |
| Default pose | Hip -0.4, knee 0.8, ankle -0.4, shoulder roll ∓1.4, elbow yaw ∓0.4 | Legs ~0, shoulder roll ∓1.3, elbow yaw 0 | **Mismatch** (up to 0.8 rad) | Override `default_joint_pos` and `prepare_state.joint_pos`, as `K1_MJLAB_HOME_POS` does |
| Prepare mode | Not applicable | `"walking"` (starts Booster's walk policy) | **Mismatch** | `prepare_mode="standing"` |
| Spawn height in MuJoCo | 0.5125 | `beyond_mimic` 0.57, velocity 0.5125 | Mismatch in `beyond_mimic` | Use 0.5125 |
| Kp, Kd | See the gains table | See the gains table | **Mismatch** | Override with the ONNX metadata values |
| Ankle Kd on hardware | 2 (joint space) | Meaning at the motors unclear | **Unknown, high stakes** | See "Ankle gains" |
| Effort limit | Hip 68/76/38.3, knee 112, ankle 38.3 | 30/35/20, 40, 20 | **Mismatch** in sim2sim | Override as velocity does. On the robot only `q`, `kp`, `kd` are sent, and the bag shows the knee at 43.7 N·m, above the config's 40, so this isn't a hard limit |
| Action to target | `default + scale * action`, no clipping | Same formula in velocity and `beyond_mimic` | **Match** | Keep raw `last_action`, don't clip |
| Action scale | Head 0.375, arm 0.35, hip 0.2125/0.2375/0.1197, knee 0.35, ankle 0.1915 | `beyond_mimic` computes 0.375, **0.875**, 0.094/0.109/0.0625, 0.125, 0.167 | **Mismatch** | Use the metadata values. They equal the velocity task's list exactly |
| Control rate | 50 Hz (5 ms × 4) | `policy_dt` 0.02 | **Match** | None |
| Physics step | 5 ms | MuJoCo 2 ms; robot firmware unknown | Fine | None |
| State rate | Not applicable | `/low_state` measured 500 Hz (p99 3.2 ms) | Fine | None |
| Latency | Trained on 10-40 ms actuator delay | Unknown on the robot; `main`'s MuJoCo has none | **Unknown** | Measure at bring-up. `hoi-dev`'s MuJoCo has delay and a torque-speed curve |
| Motion rate | 50 fps | One frame per policy step; bundled clips 50 fps | **Match** | Check `fps == 50` at load |
| Ankle model | Serial, `k1.xml` | Serial, `K1_22dof.xml`. Robot: parallel hardware, serial interface | **Match at the interface** | See "Ankle model" |
| Link masses, inertias, offsets | `k1.xml` | `K1_22dof.xml` | **Match** | 23 of 23 links identical, 19.666 kg, same armature |
| Joint limits | `k1.xml` | `K1_22dof.xml` | Small mismatch (up to 0.11 rad) | Shoulder roll differs most. Ask which is real; the assets file gives both shoulders the same range, which looks unmirrored |
| Normalization | Yes, running mean/std | Baked into ONNX (`Sub`, `Div`) | **Match** | Feed raw values. Don't normalize again |
| History/stacking | None (`history_length` 0) | None | **Match** | None |
| Export | `policy.onnx`, 1 input, 1 output | `CpuOnnxRunner` requires 1 input, 1 output | **Match** | Use `policy.onnx`, not mjlab's motion-bundled ONNX (2 inputs) |

## Joint order

Three name schemes exist, in one physical order:

| Source | Example names |
|---|---|
| `booster_mjlab` | `Head_Yaw`, `Head_Pitch`, `Left_Shoulder_Pitch`, `Right_Shoulder_Pitch` |
| GMR and `hoi-dev` `K1_CFG` | `AAHead_yaw`, `Head_pitch`, `ALeft_Shoulder_Pitch`, `ARight_Shoulder_Pitch` |
| `main` `K1_CFG` | `aahead_yaw_joint`, `aahead_pitch_joint`, `aaleft_shoulder_pitch_joint`... |

- **The 4 GMR name differences are confirmed**, and only those 4 (plus the floating-base joint's name). GMR's order and axes match, and clip columns are positional, so your data is unaffected.
- **`booster_mjlab` vs `K1_CFG`:** all 22 positions have the same axis and the same link, in the same order.
- **The real robot agrees.** In the bag, the robot starts within 0.017 rad of your home pose read in this order: `L_sh_roll` -1.41, `R_sh_roll` +1.41, `L_elb_yaw` -0.39, `R_elb_yaw` +0.40, hips -0.40, knees +0.81, ankles -0.41. That confirms order and signs for the joints with non-zero home values. The others sit near 0, so it says less about them.

**The trap is `sim_joint_names`.** `BeyondMimicPolicy` reorders observations and actions into Isaac's breadth-first order, because those policies were trained in Isaac. Your policy was not. Run unchanged, it would feed shuffled joints and send each action to the wrong joint. The 119 vs 122 size mismatch stops it today (ONNX Runtime rejected a 119-wide input), but adding `projected_gravity` alone would remove that protection, leaving the shuffle silent and dangerous. The velocity task avoids this with no remapping at all (`mjlab_velocity.py:22`).

## Gains

| Joints | **Training** | `K1_CFG` | `mjlab_velocity` | `k1_walk` | `k1_mj2` |
|---|---|---|---|---|---|
| Head | **4 / 0.25** | 4 / 1 | 4 / 0.25 | 4 / 1 | 10 / 2 |
| Arms | **20 / 2** | 4 / 1 | 10 / 1 | 20 / 2 | 4 / 1 |
| Hips, knees | **80 / 4** | 80 / 2 | 80 / 4 | 100 / 2 | 80 / 2 |
| Ankles | **50 / 2** | 30 / 2 | 50 / 2 | 65 / 1 | 30 / 2 |

Training also randomized gains by ±20%, so small differences are covered. Your arm gains aren't unusual: Booster's own `k1_walk` config uses 20 / 2. This partly answers `demo_plan.md` question 6.

The gains are also why action scale must not be recomputed. `hoi_track.py` makes the same warning: `0.25 * effort / kp` with deployed gains doesn't reproduce the training value. Your arms use a different factor (`0.5 * 14 / 20`), so even the right gains with the default formula would give half the trained scale.

## Ankle gains (the README's Kd note)

The README says `joint_damping` goes directly to the motors for parallel-actuated joints, so the training Kd shouldn't be reused, and gives `Kd = 2 * zeta * J_eq * (2 * pi * f_n)`. On the K1 the ankles are the parallel joints. `J_eq` is 0.0565 (twice the E4310's armature).

Think of the joint as a mass on a spring and damper: `f_n` is how fast it responds, and `zeta` is how much it's damped.

| Source | f_n (Hz) | zeta | Kp | Kd |
|---|---|---|---|---|
| **Your training** | 4.73 | 0.60 | 50 | 2 |
| Same stiffness, critically damped | 4.73 | 1.0 | 50 | 3.36 |
| `hoi-dev` K1 task (from `booster_train`) | 4 | 1.5 | 35.7 | 4.26 |
| `beyond_mimic` T2 recipe, applied to the K1 | 8 | 2 | 143 | 11.4 |

So your numbers already fit the formula, on the lightly damped side. The harder question is what the firmware does with them, and the code can't settle that:

- **If it runs the PD on the serial joint**, the robot behaves as trained.
- **If each motor gets the raw numbers**, the linkage changes them. Using the Jacobian from `parallel_ankle_ik.py` at the home pose:

| At home pose | Trained | If applied per motor |
|---|---|---|
| Pitch Kp / Kd | 50 / 2 | 61 / 2.45 |
| **Roll Kp / Kd** | 50 / 2 | **12.7 / 0.51** |

A 4× softer ankle roll is far outside the ±20% randomization and affects sideways balance. That case could require new gains and a retrain.

`hoi-dev`'s MuJoCo assumes the joint-space case (`mujoco_controller.py:545`), but that's a modeling choice, not evidence about the firmware. The club's velocity config uses 50 / 2 and its guide describes running that task on the robot, which is some reassurance, but the bags don't record the gains.

**Update (same day, sim only):** I ran `y1r48dhc` in plain MuJoCo with these ankle values, using the home-pose numbers in a serial model. There were 0 falls in 90 runs and hands stayed at 3.1 cm, but action rate rose about a third. See "Sim2sim from standing" below. This lowers the risk of a forced retrain without removing it: the numbers don't vary with pose, and it isn't the real linkage or the real robot.

**To do:** ask the lead first. If nobody knows, test on the gantry: hold the foot, command a small roll offset (0.05 rad), and read the torque. 50 × 0.05 = 2.5 N·m means joint space; about 0.64 N·m means per motor. `tau_est` may be a model estimate, so a free-foot step response is a useful second check.

## Ankle model

| Question | Answer | Evidence |
|---|---|---|
| What did you train on? | Serial | `k1.xml`: 22 hinges, no loop constraints |
| What does `K1_CFG.mjcf_path` use? | Serial | `K1_22dof.xml`, same structure. `K1_22dof_parallel.xml` also exists in the assets, but `main` doesn't use it |
| What is the real robot? | **Parallel hardware** | See below |
| What does software command? | **Serial pitch/roll** | `LowCmd.CMD_TYPE_SERIAL`, `motor_state_serial` (`booster_robot_controller.py:224, 270`) |

`/low_state` reports both sides, so this could be tested directly. The drive-motor values match your repo's closed-form linkage IK to about 1 mrad when given the measured serial angles:

| Bag, left ankle | Serial (pitch, roll) | Measured drives (A, B) | IK prediction |
|---|---|---|---|
| Home pose | -0.407, 0.004 | 0.337, 0.323 | 0.338, 0.324 |
| Prepare pose | -0.088, 0.003 | 0.075, 0.073 | 0.075, 0.073 |

The right ankle matches too: at home, measured (0.346, 0.329) against predicted (0.347, 0.330). All other joints read identically on both sides, so the ankles are the only parallel joints.

**Keep training serial.**
- It fits the interface: same 22 slots, and the firmware handles the linkage. This answers `demo_plan.md` question 4, pending the lead's confirmation.
- Booster's training does much the same: `hoi-dev`'s `actuator.py` (ported from `booster_train`) models the ankle as one axis with 2× armature.
- A `-Parallel` policy would be harder to deploy. Its ankle slots hold crank targets (`k1_parallel_constants.py`), while `booster_deploy` sends serial pitch/roll.

**What serial training gets wrong** (armature-only estimate at home pose, ignoring the foot's own inertia):

| | Trained | Real linkage (estimate) |
|---|---|---|
| Pitch reflected inertia | 0.0565 | ~0.035 |
| Roll reflected inertia | 0.0565 | ~0.007 (varies with pose, ~0.004-0.023) |
| Pitch peak torque | 38.3 N·m | ~60 N·m |
| **Roll peak torque** | 38.3 N·m | **~27 N·m** |

Roll has less torque available than the policy trained with. Quiet gesturing shouldn't need much, but Tier B foot shifts might. `K1_22dof_parallel.xml` with `hoi-dev`'s `ParallelAnkle` is a good sim2sim check for this.

## Export

`policy.onnx` meets the requirements:
- **Normalization is baked in.** The graph is `Sub, Div, Gemm, Elu, ...`, with mean and std of shape `(1, 122)`.
- **Shapes:** `obs [1, 122]` → `actions [1, 22]`, fixed. `baseline.onnx` has the same layout at 75 inputs.
- **Input order:** `command, motion_anchor_ori_b, base_ang_vel, joint_pos, joint_vel, actions, projected_gravity`. This differs from `beyond_mimic`, and `projected_gravity` comes last. Build it from the metadata (`observation_names`, `observation_dims`).
- **Metadata:** joint order, default pose, gains and action scale, to 8 decimals. `_check_onnx_metadata` in `mjlab_velocity.py:41` already refuses a checkpoint with mismatched values; reuse it.

The run's `policy.onnx` is written at every checkpoint, so it should be the last one (`model_5999`). For a different checkpoint: `uv run export-tracking-policy --wandb-run-path <run> --checkpoint-name model_N.pt`. The default task there is the deployable one. Older runs like `1de2pner` need `--task Mjlab-Tracking-Flat-Booster-K1`.

---

# How `booster_deploy` tasks work

**Layers:**
1. `RobotCfg`: joints, gains, default pose, prepare pose.
2. `ControllerCfg`: `policy_dt`, robot overrides, MuJoCo and exit settings.
3. `Policy`: `reset()` and `inference()`, which builds the observation, runs the model and returns joint targets.
4. `register_task("name", cfg)`: found automatically, run with `scripts/deploy.py --task name [--mujoco] [--checkpoint x.onnx] [--exit-mode damping]`.

**Runtime on the robot:** a ROS thread copies `/low_state` into shared memory (`rpy`, `gyro`, serial `q`, `dq`, `tau_est`). A separate process runs at 50 Hz: read state, run `inference()`, publish `q`, `kp`, `kd` on `joint_ctrl`. The motor drivers run the PD in between. X moves to the prepare pose, A starts the policy, Ctrl-C exits.

**Building observations:** every task reads `self.robot.data` (`joint_pos`, `joint_vel`, `root_quat_w`, `root_ang_vel_b`) in real joint order and concatenates in its own hard-coded order.

| Task | Branch | Inputs | Notes |
|---|---|---|---|
| `mjlab_velocity` | `main` | 75 | **Best config template:** trained in this repo, no remapping, right gains, ONNX metadata check |
| `beyond_mimic` | `main` | 119 | **Best policy template:** reference playback, heading alignment, tilt safety stop. Isaac-trained (`k1_mj2`'s `.pt` names `isaaclab_rl`). Both K1 `.pt` files have 119 inputs, from their tensor sizes |
| `hoi_track` | `hoi-dev` | 465 | Pre-baked reference, future frames, `motion_phase`. Most mature real-robot tooling |

`hoi-dev` has diverged a lot (about 6,900 lines added, `robots/` removed, different policy loader), so don't build on it or merge it. Copy these ideas instead: `StartTransition` / `hold_start_frame`, `ParallelAnkle`, actuator delay and torque-speed in MuJoCo, `lowstate_bag.py`, `analyze_log.py`, rosbag logging.

## What a gesture tracking task needs beyond these

| Need | State today | Plan |
|---|---|---|
| Observation layout | `beyond_mimic` is 3 short and in a different order | Build from ONNX metadata; add `projected_gravity` |
| No joint remapping | `beyond_mimic` remaps | `sim_joint_names = joint_names` |
| Multi-clip files | `MotionLoader` reads one motion and would treat `train-ab` as one huge clip | Export single clips to their own `.npz` (use `Reference.from_npz` logic), with `joint_names` included |
| Choosing a clip | The task config fixes the motion file | One task per clip, or a new CLI argument |
| Starting from rest | `beyond_mimic` jumps straight to frame 0. Your policy never trained on a standing start | Port `Reference.with_lead_in`. Keep the trunk reference at frame 0: `hoi-dev` notes that blending it made tracking policies fall |
| Ending a clip | Past the end it repeats the last frame **with its non-zero `joint_vel`** (`beyond_mimic.py:79-82`) | Port `with_end_hold` (zero velocity) |
| Exit behaviour | Code defaults to `exit_mode="walking"`, while the K1 guide says Ctrl-C returns to custom mode | Use `--exit-mode damping` on the gantry; ask the lead which is right |
| Timing | Frames advance per tick. The loop catches up after an overrun, so no lasting drift, but there's no time log | Log the frame index and overruns |
| Audio sync | None | A shared start event for clip and audio (demo), then generated-motion timing |
| Live generated motion | File-based only | Later: a streaming reference with smooth `joint_vel` |
| Safety | Tilt check only. No target clamp or stale-state check | Clamp targets to joint limits; stop if `/low_state` goes stale |
| `last_action` | `beyond_mimic` keeps the runner's output without copying; `CpuOnnxRunner` reuses that buffer | `.clone()`, as `mjlab_velocity.py:99` does |

---

# Sim2sim from standing (`y1r48dhc`)

Plain MuJoCo with the repo's `deploy/` code and the run's `policy.onnx`: 15 held-out clips (6 speakers, 12 Tier A + 3 Tier B). Each run is a 2 s lead-in from home, 1 s hold, the clip, then a 2 s hold. A clip's first frame is typically 1.4 rad from home (max 2.0 across the set), so the lead-in is a big move the policy never trained on.

**The old `sim2sim` default was misleading (fixed).** `--settle-s` defaulted to 1 s, which held the home pose at the policy's gains before it started. At those gains the robot tips: 22° at the hand-off, so all 15 runs fell at about 0.75 s. The real robot is held at `prepare_state` gains (ankle Kp 250), and the bag shows it upright. The default is now 0. The results below hold the pose at `prepare_state` gains for 1 s (0.2° tilt), then switch to the policy's gains.

| Case | Runs | Falls | Hands (cm) | Drift (m) |
|---|---|---|---|---|
| No settle (same as `--settle-s 0`) | 15 | 0 | 3.05 | 0.05 |
| Prepare gains, no delay | 15 | 0 | 3.05 | 0.05 |
| Actuator lag 10 / 25 / 40 ms | 45 | 0 | 3.05 / 3.07 / 3.11 | 0.05 |
| Lag 25 ms + sensor delay 20 ms | 15 | 0 | 3.07 | 0.06 |
| Lag 25 ms + pushes | 45 | 0 | 3.07 | 0.05 |
| Ankle gains if applied per motor, lag 25 ms | 15 | 0 | 3.09 | 0.05 |
| Ankle linkage inertia and torque, lag 25 ms | 15 | 0 | 3.07 | 0.06 |
| Both ankle changes, lag 25 ms | 15 | 0 | 3.10 | 0.06 |
| Both ankle changes, lag 25 ms + pushes | 45 | 0 | 3.10 | 0.06 |

Hands and drift are averaged over surviving runs.

Limits: one physics setup with no randomized friction, gains or masses; 15 of 194 held-out clips; ankle changes are constant home-pose values in a serial model, not the real linkage. It doesn't replace `eval-tracking`, or sim2sim in `booster_deploy` and on `K1_22dof_parallel.xml`.

---

# Verdict

**Needs config fixes, on the already-trained `y1r48dhc`. Not deployable as-is.**

| Policy | Verdict |
|---|---|
| `1de2pner` and any `Mjlab-Tracking-Flat-Booster-K1` run | **Needs retraining.** It needs position and velocity the robot doesn't have. `y1r48dhc` is that retraining |
| `y1r48dhc` | **Needs a deploy task with config fixes.** No retraining needed unless the ankle check or the remaining `val:v1` comparison says otherwise. Held-out eval: 193/194 clips, hands 3.82 cm |

## Next steps, in order

1. **Evaluate `y1r48dhc`.** `heldout-val:v0` done: 193/194 clips, 3.82 cm vs `1de2pner`'s 194/194, 3.46 cm. Left: `val:v1`, and find the one failing `kieks` clip.
2. **Sim2sim from standing: done on 15 clips, 0 falls in 225 runs** (section above).
3. **Ask the lead:** how the firmware applies ankle `kp`/`kd`; firmware version (the README says both ≥ 1.7.2 and ≥ 1.4); which joint limits are real; the Ctrl-C exit mode; gantry and e-stop. Update `demo_plan.md`: questions 1, 3 and 4 are mostly answered here.
4. **Settle the ankle gains** (lead's answer or gantry test), before spending more GPU time. Retrain only if they fall outside the ±20% randomization.
5. **Build the task** in `booster_deploy` from `main`: `mjlab_velocity`'s config + `beyond_mimic`'s playback + your `deploy/` logic. Add a golden test: the same state must give the same observation as `build_observation`.
6. **Sim2sim in `booster_deploy`:** `K1_22dof.xml`, then parallel ankles with delay (from `hoi-dev`).
7. **Bring-up, with the e-stop ready at every stage** (`demo_plan.md` section 6): compute without sending and check order and signs → gantry hold → gantry clip → floor with slack harness → demo. Record `/low_state` and `/joint_ctrl` in every run.
