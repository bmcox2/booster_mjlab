# CLAUDE.md

Context for AI assistants working in this repo. Keep this file current; it is read at the start of every session.

## Who / what
- Owner: Boston Cox (UIUC CS junior), SIGRobotics club, Booster K1 humanoid.
- New to RL, mjlab, and WandB. Explain concepts plainly, tie them back to DeepMimic where possible, and prefer concise, step-by-step answers.
- Project: **co-speech gesture tracking on the Booster K1**. Long-term vision: a K1 that talks and gestures naturally (tutor / presenter).
- Anchor paper: "Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots" (arXiv 2512.17183, Unitree G1). Background: DeepMimic (arXiv 1804.02717).

## Milestone plan
1. **Milestone 1 (current):** K1 tracks 5–10 retargeted gestures in mjlab sim, full clip, no falls (50 rollouts/gesture), using mjlab's default action space and rewards. Sim only.
2. Milestone 2: default vs residual (reference + bounded correction) actions; LLM picks gestures from the SeG library.
3. Milestone 3+: speech in the loop (BEAT2 data), gestures while walking (ExBody2), gaze/presenting, sim-to-real.

Data plan: AMASS clips found via HumanML3D text labels (SMPL-X) → GMR retargeting (`booster_k1` config, SMPL-X input only) → `upload-motion` → tracking. Missing gestures: phone video → GVHMR → GMR.

K1 constraints: ~0.95 m, 22 DoF; head 2 (yaw, pitch), arms 4 each (shoulder ×3, elbow), legs 6 each. **No wrists, no waist, no hands.**

## Repo
- Fork of IntelligentRoboticsLab/booster_mjlab. `origin` = bmcox2/booster_mjlab, `upstream` = IntelligentRoboticsLab.
- Work on branch `gesture-tracking`; keep `main` matching upstream. Never open PRs to upstream.
- `notes/log.md` = run log. Update it every session and push.
- Also in `notes/`: `proposal.md` (project plan), `wandb-guide.md` (how to read training charts / when to stop), `papers.md` (DeepMimic + anchor paper mapped to code), `glossary.md` (RL terms).
- Slash commands in `.claude/commands/`: `/log-session` (write log entry), `/analyze-run` (read WandB charts).
- Never commit `logs/`, `wandb/`, `data/`, checkpoints, or datasets.

Key paths:
- `src/booster_mjlab/tasks/tracking/tracking_env_cfg.py`: K1 tracking task (modifies mjlab's base tracking cfg; rewards/obs/terminations come from `mjlab.tasks.tracking.tracking_env_cfg` in `.venv`).
- `src/booster_mjlab/tasks/tracking/config/k1/`: `env_cfgs.py`, `rl_cfg.py`.
- `src/booster_mjlab/robots/booster_k1/`: robot model (`xmls/`), constants, actuators.
- `src/booster_mjlab/motion/`: motion loading.
- `src/booster_mjlab/scripts/`: `train`, `play`, `upload_motion`, `visualize_motions`.
- `docs/motion_preparation.md`: converting/uploading GMR `.pkl` / BeyondMimic `.csv` clips.

## Commands
```
uv run list_envs
uv run train <TASK> --env.scene.num-envs 4096
uv run play <TASK> --wandb-run-path bmcox2-university-of-illinois-urbana-champaign/mjlab/<run-id>
uv run visualize-motions --dataset whirlwind-ams/lafan_locomotion_k1 --task <TASK>
uv run upload-motion --input-file <clip.pkl> --entity bmcox2-university-of-illinois-urbana-champaign
uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name <artifact printed by upload-motion> --env.scene.num-envs 4096
```
Tasks used: `Mjlab-Velocity-Flat-Amp-DA-Muon-Booster-K1` (baseline), `Mjlab-Tracking-Flat-Booster-K1` (project).

## Environment gotchas
- WandB entity must be the **team**: `WANDB_ENTITY=bmcox2-university-of-illinois-urbana-champaign` (not `bmcox2`, not the `-org` name). Set in `~/.bashrc`.
- Hardware: Dell XPS 15, RTX 4070 Laptop 8 GB, Ubuntu 24.04 (dual boot). GPU power capped ~35 W; dGPU has dropped out intermittently and the laptop has overheated before. Check `nvidia-smi` before runs; stop if GPU sustains >~87 °C. Prefer the club GPU for long runs.
- 4096 envs fits in 8 GB (~3k iterations ≈ 2.5 h for the velocity task).

## Status
- 2026-10-13: setup done; velocity baseline trained (WandB run `2wagxxko`, healthy).
- Next: tracking task on one LAFAN clip (`whirlwind-ams/lafan_locomotion_k1`), then a first gesture clip.
- Open questions for lead: club GPU access; which K1 ankle model (standard vs `-Parallel`).
