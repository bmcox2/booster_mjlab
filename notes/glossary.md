# Glossary

**RL basics**
- **Policy (π):** the network that picks actions from observations. "The actor."
- **Value function (V):** predicts expected future reward from a state. "The critic."
- **Advantage (A = Q − V):** how much better an action was than the policy's average in that state. Positive → do it more.
- **Return:** total (discounted) reward over one episode.
- **Discount (γ):** how much future reward counts. ~0.99 ≈ looks a few seconds ahead.
- **Episode:** one attempt, from reset until termination or time-out.
- **Rollout:** running the policy to collect experience.
- **Observation:** what the policy sees (joint positions/velocities, gravity direction, commands...).
- **Action:** what the policy outputs (here: target joint angles).
- **Reward term:** one weighted piece of the total reward (tracking, upright, foot slip...).

**PPO / training**
- **PPO:** on-policy policy-gradient algorithm. Collect data, compute advantages, do several updates, throw data away, repeat.
- **On-policy:** trains only on data from the current policy (no replay buffer).
- **Clipping:** PPO limits how far each update can move the policy (ratio kept in [1−ε, 1+ε]).
- **GAE:** the method used to estimate advantages.
- **Iteration:** one collect-then-update cycle. The "Step" axis in WandB.
- **Parallel envs (num-envs):** robots simulated at once (e.g. 4096). More = more data per iteration.
- **Checkpoint:** saved network weights (`model_*.pt`).
- **Seed:** random starting conditions. Same config, different seed can behave differently.
- **Entropy / noise std:** how much the policy still explores. Decreases over training.
- **Local optimum:** a bad-but-rewarding habit the policy gets stuck in.

**Control / sim**
- **PD controller:** turns a target angle into torque: kp × (target − current) − kd × velocity.
- **Residual action:** policy outputs a correction added to the reference pose instead of the full target.
- **Physics step vs env step:** physics 0.005 s (200 Hz); policy acts every 0.02 s (50 Hz).
- **Domain randomization:** randomizing friction, mass, gains, pushes in sim so the policy transfers to the real robot.
- **Sim-to-real:** moving a sim-trained policy onto hardware.
- **Curriculum:** making the task harder automatically as the policy improves.

**Motion / data**
- **Reference motion / clip:** the motion the robot should copy.
- **Motion tracking / imitation:** RL that rewards matching a reference clip (DeepMimic). Not behavior cloning.
- **Behavior cloning:** supervised learning from expert *actions*. Not what we're doing.
- **RSI:** Reference State Initialization: start episodes at random points in the clip.
- **Early termination:** end an episode on failure (fall).
- **Retargeting:** converting human motion to a robot's body (GMR does this).
- **SMPL-X:** standard human body model format (AMASS, BEAT2, GMR input).
- **BVH:** older skeleton motion format (ZEGGS, SeG).
- **AMP:** Adversarial Motion Priors: a discriminator rewards motion that looks like the reference data's style.
- **Phase variable:** DeepMimic's "where am I in the clip" input.

**Tools**
- **mjlab:** GPU robot-learning framework (Isaac Lab API on MuJoCo Warp).
- **booster_mjlab:** K1 robot + tasks for mjlab.
- **WandB:** experiment tracking (charts, checkpoints, motion artifacts). Entity = team name.
- **uv:** Python package/environment manager. `uv run <cmd>` runs inside the project's `.venv`.
- **viser:** browser-based 3D viewer used by `play` / `visualize-motions`.
