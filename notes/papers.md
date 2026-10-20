# Paper Notes

## DeepMimic (Peng et al., 2018), arXiv 1804.02717
Physics-based character learns to copy a reference motion clip using RL (PPO).

**State:** link positions, rotations, velocities in the root (pelvis) frame, plus a **phase** variable φ ∈ [0,1] telling the policy where it is in the clip. Global position/heading excluded so skills work anywhere.

**Action:** PD target joint angles (not torques). PD controller turns targets into torque. Policy at 30 Hz, physics at 1200 Hz.

**Reward:** 0.7 × imitation + 0.3 × task. Imitation = pose 0.65 + end-effector 0.15 + velocity 0.1 + center of mass 0.1. Each term is exp(−error): 1 at a perfect match, decays smoothly, never negative.

**Reference State Initialization (RSI):** start episodes at random points in the clip, so the policy practices every phase (e.g. the landing) from day one. Without it, the backflip policy learned a backward hop and never flipped (return 0.379 vs 0.791).

**Early termination (ET):** end the episode when the torso/head hits the ground. Removes the "flailing on the floor" local optimum and keeps training data focused on useful states.

**Training cost (2018):** ~60M samples, ~2 days on an 8-core CPU, per skill. GPU-parallel sim (mjlab) collapses this to hours.

**Limitations:** linear phase (can't adapt timing), hand-tuned PD gains, hand-designed similarity reward, multi-clip doesn't scale, no sim-to-real.

## Anchor paper: Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots (Zhang, Dec 2025), arXiv 2512.17183
Full pipeline on the Unitree G1 (29 DoF): speech → gesture motion → retarget → tracking policy → real robot.

**Data:** ZEGGS (2 h, one speaker, 19 styles) and BEAT ("resources including": the full list isn't given); SeG library (208 semantic gesture types) for retrieval. No code or data released.

**Retargeting (§3.2):** GMR: key-body matching, scaling, two-stage IK.

**Gesture generation (§3.3):** RVQ-VAE turns motion into discrete tokens; Motion-GPT (GPT-2) predicts the next motion token from previous tokens + audio features (rhythm → beat gestures); an LLM reads the transcript and retrieves meaningful gestures from SeG, blended in.

**Tracking policy (§3.4):** "imitation learning" here = RL motion tracking (DeepMimic-style), not behavior cloning. Uses MotionTracker from Any2Track (arXiv 2509.13833): stage 1 general tracker, stage 2 history-based adapter for disturbances.
- **Residual actions:** target = reference pose + scale_j × tanh(a). The network outputs only a bounded correction, so it starts out following the reference, explores around it, and can track new, unseen gestures. Tradeoff: only as good as the reference.

**Results:** low tracking RMSE (Table 2); highest error at the wrists. Real G1 demo stays balanced.

**Limitations / future work:** better LLM timing (prosody), better blending than stroke-phase alignment, multi-party conversation. Evaluation is thin: no baselines, no user study.

## How this maps to the code (booster_mjlab / mjlab)
| Concept | In the code / output |
|---|---|
| PD target actions | `joint_pos` action term (22 dims for K1) |
| Early termination | `fell_over`, `illegal_contact` terminations |
| RSI | `reset_robot_from_motion` reset event |
| Policy / value networks | Actor / Critic MLPs (512-256-128, ELU), Gaussian action noise |
| Domain randomization (not in DeepMimic) | `push_robot`, `foot_friction`, `pd_gains`, `body_mass`... |
| Tracking task config | `src/booster_mjlab/tasks/tracking/tracking_env_cfg.py` (on top of `mjlab.tasks.tracking.tracking_env_cfg`) |

## Related, for later
- **AMP:** learned style reward from a discriminator (used in the velocity task).
- **BeyondMimic:** modern tracking with sim-to-real; mjlab's tracking task builds on it.
- **ExBody2:** expressive upper body while walking (milestone: gesturing while walking).
- **GMR, AMASS, HumanML3D, SeG, BEAT2:** data and retargeting (see proposal).

## Next reading (2026-10-20 direction)
- **SayCan** (Ahn et al., 2022) and **Code as Policies** (Liang et al., 2022): LLM → robot skills, the pattern for the tool-call layer.
- **EMAGE** (Liu et al., CVPR 2024): BEAT2's audio → full-body gesture model; candidate gesture generator. Check whether it can run in chunks.
- **ExBody / ExBody2**: expressive upper body on top of locomotion.
- **BeyondMimic**: the tracking method mjlab's task comes from; its sim-to-real and deploy pipeline are the model for criteria 2–3.
- **GMT** (General Motion Tracking): a general tracker over many clips; uses future reference frames (~2 s) in the observation.
