# CLAUDE.md

Context for AI assistants working in this repo. Keep this file current; it is read at the start of every session.

## Who / what
- Owner: Boston Cox (UIUC CS junior), SIGRobotics club, Booster K1 humanoid.
- New to RL, mjlab, and WandB. Explain concepts plainly, tie them back to DeepMimic where possible, and prefer concise, step-by-step answers.
- Project: **co-speech gesture tracking on the Booster K1**. Long-term vision: a K1 that talks and gestures naturally (tutor / presenter).
- Anchor paper: "Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots" (arXiv 2512.17183, Unitree G1). Background: DeepMimic (arXiv 1804.02717).

## Roadmap (revised 2026-10-16; full version in `notes/roadmap.md`)
Pipeline: audio → [1] gesture generator (borrow pretrained EMAGE) → SMPL-X → [2] GMR + ground_clip → [3] RL tracker (the focus). Milestone 1 is now "K1 tracks real conversational motion" (was: 5–10 AMASS gestures).
0. **Slice 0 (current):** one BEAT2 talking clip → GMR → ground_clip → single-clip tracker → sim video with the original audio. Plan: `notes/plan.md`.
1. General tracker: MultiMotionCommand, trained on BEAT2 + AMASS gestures, evaluated on held-out speakers. Club GPU.
2. Product v1: any audio → EMAGE → GMR → tracker, offline.
3. Real-time streaming + latency, then an LLM picking SeG gestures (AMASS waves/points are kept for this).
4. Sim-to-real in parallel: ankle model, domain randomization, policy export.

Data: BEAT2 (SMPL-X + audio) is the tracker's main training data. AMASS via HumanML3D labels for isolated gestures. Missing gestures: phone video → GVHMR → GMR.

K1 constraints: ~0.95 m, 22 DoF; head 2 (yaw, pitch), arms 4 each (shoulder ×3, elbow), legs 6 each. **No wrists, no waist, no hands.**

## Repo
- Fork of IntelligentRoboticsLab/booster_mjlab. `origin` = bmcox2/booster_mjlab, `upstream` = IntelligentRoboticsLab.
- Work on branch `gesture-tracking`; keep `main` matching upstream. Never open PRs to upstream.
- `notes/log.md` = run log. Update it every session and push.
- Also in `notes/`: `roadmap.md` (whole-project steps), `eval-guide.md` (how to run/read `eval-tracking`), `multi-clip.md` (MultiMotionCommand design, diff from mjlab, per-clip metrics), `beat2-full-segments.md` / `gate1-calibration.md` (full BEAT2 dataset), `plan.md` (current step's checklist: Slice 0), `proposal.md` (project plan), `wandb-guide.md` (how to read training charts / when to stop), `papers.md` (DeepMimic + anchor paper mapped to code), `glossary.md` (RL terms).
- Slash commands in `.claude/commands/`: `/log-session` (write log entry), `/analyze-run` (read WandB charts).
- Never commit `logs/`, `wandb/`, `data/`, checkpoints, or datasets.

Key paths:
- `src/booster_mjlab/tasks/tracking/tracking_env_cfg.py`: K1 tracking task (modifies mjlab's base tracking cfg; rewards/obs/terminations come from `mjlab.tasks.tracking.tracking_env_cfg` in `.venv`). Swaps in `MultiMotionCommandCfg`.
- `src/booster_mjlab/tasks/tracking/multi_motion_command.py`: `MultiMotionCommand` (subclass of mjlab's `MotionCommand`; never edit mjlab, it is pinned).
- `src/booster_mjlab/tasks/tracking/config/k1/`: `env_cfgs.py`, `rl_cfg.py`.
- `src/booster_mjlab/robots/booster_k1/`: robot model (`xmls/`), constants, actuators.
- `src/booster_mjlab/motion/`: motion loading.
- `src/booster_mjlab/scripts/`: `train`, `play`, `upload_motion`, `combine_motions`, `visualize_motions`, `eval_tracking`.
- `tests/test_multi_motion.py`: `uv run --with pytest pytest tests/ -q` (CPU, needs `logs/motions/waves_2clip.npz`).
- `tools/ground_clip.py`: ground + flatten feet of GMR clips before upload.
- `tools/beat2_to_gmr.py`: BEAT2 take → GMR input (`--find-still` ranks windows). Runs with GMR's venv or the booster venv.
- `tools/gmr_retarget.py`: headless GMR retarget (no viewer). Must run with `~/projects/GMR/.venv/bin/python`. `--ik-config tools/ik_configs/<cfg>.json` for a custom K1 IK config.
- `tools/beat2_batch.py`: dataset spec → segments → GMR → ground_clip → Gate 1 QC → one combined file per set → leakage check → upload. Cached per stage, `--workers` (default 12). `uv run python tools/beat2_batch.py --spec tools/datasets/beat2_full.toml [--stages segment] [--no-upload]`. (The old `--train/--heldout` 10 s-window version built v0–v3; it is in git before 2026-10-18.)
- `tools/datasets/beat2_full.toml`: full BEAT2 spec (held-out speakers, split types and tiers per set, IK config, QC limits).
- `tools/beat2_segments.py`: human-side segmentation: Tier A (ankles within 10 cm) / Tier B (foot shifts ≤ 25 cm, `_shift`) 4–20 s clips, per-speaker report.
- `tools/clip_qc.py`: Gate 1 checks on grounded K1 clips (jumps, trunk turn, speed, floor, foot slide, self-collision, limits, arm-behind, leakage); `LIMITS` calibrated in `notes/gate1-calibration.md`.
- `docs/motion_preparation.md`: converting/uploading GMR `.pkl` / BeyondMimic `.csv` clips.

## Commands
```
uv run list_envs
uv run train <TASK> --env.scene.num-envs 4096
uv run play <TASK> --wandb-run-path bmcox2-university-of-illinois-urbana-champaign/mjlab/<run-id>
uv run visualize-motions --dataset whirlwind-ams/lafan_locomotion_k1 --task <TASK>
uv run upload-motion --input-file <clip.pkl> --entity bmcox2-university-of-illinois-urbana-champaign
uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name <artifact printed by upload-motion> --env.scene.num-envs 4096
uv run combine-motions <artifact> <artifact> ... --artifact-name <name>   # multi-clip file, same train command
uv run eval-tracking --wandb-run-path bmcox2-university-of-illinois-urbana-champaign/mjlab/<run-id>   # one row per clip
```
Tasks used: `Mjlab-Velocity-Flat-Amp-DA-Muon-Booster-K1` (baseline), `Mjlab-Tracking-Flat-Booster-K1` (project).

## Environment gotchas
- WandB entity must be the **team**: `WANDB_ENTITY=bmcox2-university-of-illinois-urbana-champaign` (not `bmcox2`, not the `-org` name). Set in `~/.bashrc`.
- Hardware: Dell XPS 15, RTX 4070 Laptop 8 GB, Ubuntu 24.04 (dual boot). GPU power capped ~35 W; dGPU has dropped out intermittently and the laptop has overheated before. Check `nvidia-smi` before runs; stop if GPU sustains >~87 °C. Prefer the club GPU for long runs.
- 4096 envs fits in 8 GB (~3k iterations ≈ 2.5 h for the velocity task).
- SSH: `ssh booster@10.193.169.55` (private campus IP, so it only works on the campus network or VPN).
- **Resume training:** add `--agent.resume True` with `--wandb-run-path <entity>/mjlab/<run> --wandb-checkpoint-name model_N.pt`, or it silently starts from scratch. `--agent.max-iterations` = additional iterations. Run long jobs on the club GPU inside `tmux` (`tmux new -s train`, detach `Ctrl-b d`).
- **WandB conventions:** name runs `MM-DD what-it-is`, tag them (`tracking`, `general`, `beat2`, `keep`/`superseded`...), one-line result note; dataset versions get a description, and the `current` alias moves to the version in use.
- Club GPU WandB: shared `booster` account, so no `wandb login`. Run `source ~/bmcox2/.wandb_env` in each new shell before `uv run train` / `eval-tracking` / `play`.

## Status
- 2026-10-13: setup done; velocity baseline trained (WandB run `2wagxxko`, healthy).
- 2026-10-14: gesture pipeline A–C mostly done. GMR at `~/projects/GMR` (own uv venv, SMPL-X models in `assets/body_models/smplx/`); data in `~/robotics/data/` (HumanML3D, amass/BMLmovi, k1_motions). First gesture: BMLmovi wave `wave_000508` (HumanML3D 000508), uploaded as `bmcox2-university-of-illinois-urbana-champaign/motion_upload/wave_000508-tracking:v0`.
- 2026-10-15: first tracking run `w77drafm` (wave_000508 v0, 1024 envs, ~0.84 s/it) learned without falls, but v0 clips were 6–7 cm below the floor. Fix: `tools/ground_clip.py` (run on every GMR clip before upload).
- 2026-10-15: run `4zzjocm6` on grounded `wave_000508-tracking:v2`: done, no falls, body error 0.016 m. Robot sits 1.1 cm below the reference because the GMR clip's feet are tilted 6–9°.
- 2026-10-15: `ground_clip.py` now flattens stance feet (GMR clips stood on 6–12° tilted feet; policy rolled the right ankle). Default on; `--keep-foot-tilt` to skip.
- 2026-10-15: `uv run eval-tracking` built (guide: `notes/eval-guide.md`). 4zzjocm6 on wave_000508 v2: 50/50 PASS, hands 2.1 cm, right foot rolls 23°.
- 2026-10-15: run `me9exatd` (wave_000508 `:v3`, flattened feet): 50/50 (300/300 with pushes), hands 1.5 cm, foot tilt 5°. **Gesture 1 meets milestone 1 bar.**
- 2026-10-16: gesture 2 `wave_001104` (run `pqh0whw0`, `:v2`): 50/50, 300/300 with pushes, hands 1.7 cm. **2 of 5–10 gestures done.**
- 2026-10-16: roadmap revised (`notes/roadmap.md`): BEAT2 talking data replaces more AMASS gestures. Next: Slice 0 (`notes/plan.md`).
- 2026-10-16: `tools/beat2_to_gmr.py` converts BEAT2 (Y-up, float WAV) to GMR input; `--find-still` ranks still, gesturing windows. BEAT2 Scott data in `~/robotics/data/BEAT2/beat_english_v2.0.0/`. Scott steps every 5–10 s, so no 20 s still window; best 10 s: `2_scott_0_1_1` 34–44 s.
- 2026-10-16: club GPU works: host `sigrobotics` (RTX 5070 Ti), ~169k env-steps/s at 4096 envs (4.8× laptop). Run `e2p0f89y` (wave_000508 `:v3`, 2,500 it, 25 min): 50/50, hands 1.4 cm.
- 2026-10-16: Slice 0 first run `z17z0n1q` (`talk_scott_1_1_t34-44-tracking:v0`, 10 s, 5k it, club GPU): **50/50 PASS**, hands 2.2 cm (waves 1.4–1.7), drift 2.2 cm. Video pending.
- 2026-10-16: multi-clip tracking built (`MultiMotionCommand`, `combine-motions`, per-clip `eval-tracking`; `notes/multi-clip.md`). Tests pass on CPU. `e2p0f89y` (one wave) fails 49/50 on the other wave → next: first multi-clip run on the club GPU.
- 2026-10-16: multi-clip sanity run `8ku1opzv` (`waves-2clip:v0`, 4096 envs, 2,500 it, club GPU): 50/50 on both waves, matching the single-clip policies (hands 1.5 / 1.6 cm). Multi-clip works.
- 2026-10-16: BEAT2 batch (`tools/beat2_batch.py`, QC in `notes/beat2-qc.md`): 152 clips, 12 severe excluded → `beat2-10s-train:v0` (98 clips, 16.3 min, 6 speakers) and `beat2-10s-heldout:v0` (42 clips, 7.0 min; Nidal, Ayana). Read held-out eval per speaker (Nidal is low-motion). Next: first general-tracker run.
- 2026-10-16: fixed GMR IK start (left arm stuck behind the body in 20/152 BEAT2 clips; seeded with HOME arms in `tools/gmr_retarget.py`). Use **`beat2-10s-train:v1`** (106 clips, 17.7 min) / **`beat2-10s-heldout:v1`** (44 clips, 7.3 min); v0 is bad.
- 2026-10-17: first general tracker `0lg80c7d` (`beat2-10s-train:v1`, 30k it) **stuck** at ~2.5k it: adaptive sampling gave one GMR-glitch clip (`wayne_0_9_9_t12-22`, arm joint snaps 0.9 rad in one frame) 70–77% of starts. Eval: held-out 43/44, train 103/106, hands 6.7 / 5.8 cm (single-clip ~2). Fixes: `joint jump` severe QC flag, `adaptive_uniform_ratio = 1.0` (K1 env_cfgs). Use **`beat2-10s-train:v2`** (103 clips, 17.2 min) / **`beat2-10s-heldout:v2`** (43 clips, 7.2 min).
- 2026-10-17: run `s5cdzms7` (`beat2-10s-train:v2`, 10k it, 2.6 h): plateau fixed. **Use `model_8500.pt`** (beats model_9999; late-run policy std drift). Eval hands: train 2.5 cm (100/103 clips 50/50), held-out 3.05 cm (Nidal 2.3, Ayana 4.6; 42/43), pushes no effect; 0lg80c7d was 5.8 / 6.7. Open: foot tilt > 10° on most Lawrence/Solomon clips.
- 2026-10-17: Slice 0 video recorded (`s5cdzms7`, Scott clip, audio dubbed; `play --video True --hide-overlays`, 1080p). K1 leans back: GMR's K1 config makes the trunk copy the human **pelvis** (no waist). `tools/ik_configs/smplx_to_k1_torso.json` (`Trunk ← spine1`) matches Scott's torso lean (−6.0° vs −6.5°; pelvis: −15°); `beat2_batch.py --ik-config`. Arms are fine (forearm follows the human forearm).
- 2026-10-18: `beat2_batch.py --workers` / `combine-motions --workers` (process pools, bit-identical): full BEAT2 build ~45 min → 3 min. Torso-config data: **`beat2-10s-train:v3`** (105 clips) / **`beat2-10s-heldout:v3`** (43) in `~/robotics/data/beat2_batch_torso` (QC `notes/beat2-qc-torso.md`); lean error vs human median 3.4° → 2.5°. Next: train on v3.
- 2026-10-18: full BEAT2 phase 1 (human side). All session-0 takes downloaded. Official split respected (v1–v3 used only val/test takes). Held out: Nidal, Ayana, 20_li, 27_yingqing. Training Tier A 11.6 h (+2.8 h Tier B), segments in `notes/beat2-full-segments.md`. Session-1 `additional` takes = 10-min conversations (26 h, ~15 h Tier A for training speakers), not downloaded yet (decision pending). Gate 1 calibrated. Phase 2 waits for the v3 GMR config.
- 2026-10-18: run `fsyy1c2w` (`beat2-10s-train:v3`, torso data) stopped at 3.7k it. **`model_3500` held-out hands 3.08 cm** (Nidal 2.44, Ayana 4.41) vs s5cdzms7 model_3500 3.42 / model_8500 3.05: torso data is better. Next: resume to ~6k, full evals, re-record video.
- Open questions for lead: which K1 ankle model (standard vs `-Parallel`).
