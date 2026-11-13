# CLAUDE.md

Read at the start of every session. Keep it **current, not historical**: it describes the project as it is now.
History goes in `notes/log.md`; the to-do list is "Next" at the bottom of `notes/log.md`.

## Who / what
- Owner: Boston Cox (UIUC CS junior), SIGRobotics club, Booster K1 humanoid. New to RL, mjlab, WandB and Linux tooling: explain plainly, tie RL ideas back to DeepMimic, give concise step-by-step answers.
- Project: **co-speech gesture tracking on the Booster K1** → a K1 that holds a spoken conversation and gestures in sync. Later: an LLM companion that also calls skills (walk_to, look_at, point, wave), tutoring / presenting. A working system first; a paper is a bonus (likely angle: K1-native streaming generator).
- Anchor paper: "Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots" (arXiv 2512.17183, Unitree G1). Background: DeepMimic (arXiv 1804.02717). Notes: `notes/papers.md`.
- K1: ~0.95 m, 22 DoF; head 2 (yaw, pitch), arms 4 each (shoulder ×3, elbow), legs 6 each. **No wrists, no waist, no hands** (the hardware group is building hands; plan without them).

## Current focus (2026-11-13)
**Full spoken conversation on the real K1, Thursday 2026-11-19, everything onboard** (`notes/onboard_plan.md`). Laptop = SSH, tests and rehearsal only. On the K1: P1 `deploy.py --task k1_gesture_live` (to build, in `booster_deploy`) ← 50 Hz frames over shared memory ← P2 `gesture live --robot` (to build) ← P3 speech loop (K1 mics + speaker, cloud STT / LLM / TTS). Rehearse with `fake_robot.py`; context gestures (emphasis, wave / point) in sim in parallel.

Stack (the LLM never controls joints): mics → STT → LLM (+ tool calls) → TTS → gesture generator → **50 Hz K1 reference stream** (the stable contract; legs on a fixed standing reference) → **RL tracker**. GMR stays offline (library / training data). Locomotion via Booster's SDK at first.

Roadmap (`notes/roadmap.md`): 1 canned clips on hardware **done** 2026-11-12 · 2 EMAGE smoke test (deferred) · 3 retrieval generator v0 **done in sim** incl. streaming (`notes/gesture_plan.md`; step 5 viewer test left) · 4 final tracker run (exit criteria, `history_length` 10 experiment, 10-min operation) · 5 speech (`notes/speech_plan.md`, steps 1–4 done, next barge-in) · **6 live on the robot: now** · 7 LLM tool calls · 8 neural generator if retrieval is repetitive, then mobility.

## What to use now
| Thing | Current | Notes |
|---|---|---|
| Deployable tracker | W&B run **`y1r48dhc`** (task `Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation`, 122 inputs) | Held-out-val 193/194 clips, hands 3.82 cm; 4 floor runs on the real K1, no falls |
| Sim-only tracker | `1de2pner` `model_5999.pt` (task `Mjlab-Tracking-Flat-Booster-K1`) | 194/194, 3.46 cm; observes anchor position + linear velocity, so it **can't deploy** |
| Training data | `beat2-full-torso-train-ab:v0` (10,776 clips, 28.8 h) | Eval: `heldout-val:v0` (194, main), `val:v1` (472); `test` / `heldout-test` / `heldout-conv` `:v2` scored once at the end. Local copies `~/robotics/data/beat2_full_torso/combined/` |
| Retarget config | `tools/ik_configs/smplx_to_k1_torso.json` (K1 trunk ← human spine1) | Default in `tools/datasets/beat2_full.toml`; GMR's stock config leans the K1 back |
| Gesture library | `~/robotics/data/gesture/library_v0.npz` (Wayne, Lawrence, Miranda; 7.8 h, 20.5k units) | Idle persona `9_miranda` |
| Speech | Groq Whisper turbo → Groq `openai/gpt-oss-120b` → **Orpheus `troy`** (Kokoro fallback), streamed in pieces | Response ~1.5–1.8 s median. Orpheus free tier 10 req/min, 100/day; **no Kokoro onboard**, so the cloud TTS must not run out |
| Robot deploy | `~/projects/booster_deploy` (club repo, local branch `gesture-tracking`, **not pushed**), task `k1_gesture_tracking` | Guide `docs/k1_gesture_deploy.md` there; `scripts/sync_to_robot.sh [--check]` → `~/booster_deploy_gesture` on the K1; runs write `logs/run_*.npz` (`scripts/check_run.py`); `scripts/fake_robot.py` rehearses on a simulated K1 |

K1 hardware facts: Orin NX, Ubuntu 22.04, hostname `robot`. Speaker = C-Media USB, ALSA card 0 (`aplay -D plughw:0,0`; very loud: `amixer -c 0 set PCM 60%` first). Mic = iFlytek XFM-DP USB, card 1 (dropped off USB under motion; check `cat /proc/asound/cards`). Booster SDK Python 1.6.3 has an audio API (`AudioCaptureStream`, `AudioPlayer`, DOA): `notes/onboard_plan.md`. Ctrl-C in `deploy.py` hands over to Walking.

## Repo
- Fork of IntelligentRoboticsLab/booster_mjlab: `origin` = bmcox2/booster_mjlab (**public**), `upstream` = IntelligentRoboticsLab. Work on `gesture-tracking`; `main` matches upstream. Never open PRs to upstream.
- Never commit `logs/`, `wandb/`, `data/`, `artifacts/`, `secrets/`, checkpoints or datasets. `secrets/k1_access.md` holds the robot password (gitignored).
- mjlab is pinned in `pyproject.toml`: never edit it; subclass or override in `src/booster_mjlab/`.
- Update `notes/log.md` every session and push (`/log-session`). `/analyze-run` reads WandB charts (`.claude/commands/`).

`notes/` map (bare names in notes are relative to `notes/`):
- **Working docs:** `log.md` (run log, newest last, to-do "Next" at the bottom; October in `archive/log_2026-10.md`), `roadmap.md`, `onboard_plan.md` (this week), `gesture_plan.md`, `speech_plan.md`, `speech_bench.md` (speech measurements), `deploy_audit.md` (policy vs `booster_deploy`: observations, ankles, open questions for the lead), `live_test_script.md`.
- **Guides / reference:** `eval-guide.md` (`eval-tracking`), `wandb-guide.md` (reading training charts), `multi-clip.md` (`MultiMotionCommand`, safety harness), `glossary.md` (RL terms), `papers.md`, `laptop_gpu.md` (driver / dGPU dropout fixes), `proposal.md` (approved plan; tell the lead before changing scope).
- **`reports/`:** written by tools, don't hand-edit: `beat2-full-qc.md` (800 KB; grep it, don't read it), `beat2-full-segments.md`, `gate1-calibration.md`.
- **`archive/`:** done plans: `slice0_plan.md`, `demo_plan.md` (SDK questions), `robot_session_2026-11-12.md` (runbook; template for the next robot session), old 10 s-window QC reports.

## Code map
- **Tracking task** `src/booster_mjlab/tasks/tracking/`: `tracking_env_cfg.py` (K1 changes on mjlab's base cfg; rewards / obs / terminations live in `mjlab.tasks.tracking.tracking_env_cfg` in `.venv`), `multi_motion_command.py` (`MultiMotionCommand`: many clips per policy + sampling safety harness: per-clip cap, quarantine, `flagged_clips.json`), `runner.py` (`K1MotionTrackingRunner`: skips mjlab's motion-bundled ONNX export above 1 GiB), `config/k1/` (`env_cfgs.py`, `rl_cfg.py`; tasks `...-K1`, `...-K1-No-State-Estimation`, `...-No-State-Estimation-History10`).
- **Deploy** `src/booster_mjlab/deploy/` (numpy + onnxruntime, robot-agnostic): `TrackingPolicy` (`policy.onnx` + metadata, 1 thread), `build_observation`, `ObservationHistory`, `Reference` (lead-in / end hold / heading). Checked against mjlab by `tests/test_deploy.py`.
- **Gesture generator** `src/booster_mjlab/gesture/` (`uv run gesture <cmd>`): `audio` (50 fps speech features), `motion` (trunk-frame hand features, `cut_units`), `sync`, `library`, `analysis`, `generate` (reply → K1 reference: retrieval, Viterbi, stitch, foot lock, QC), `stream` (`MotionStream`, incremental), `serve` (per-reply service), `live` (real-time tracker in MuJoCo + HTTP `/begin` `/piece` `/end`), `live_video`. Outputs in `logs/gesture/{replies,conversations,live}/`.
- **Speech loop** `speech/`: **own uv project** (`cd speech && uv run python -m speech.loop --hands-free`; `speech/README.md`). Settings `speech/config.toml`, API keys `speech/.env`, per-turn files `speech/runs/` (both gitignored). Gesture hook: `[gesture]` in config, client `speech/src/speech/gesture.py`.
- **Scripts** `src/booster_mjlab/scripts/` (entry points in `pyproject.toml`): `train`, `play`, `eval-tracking`, `sim2sim` (plain MuJoCo, robot-style loop; `--obs-delay-steps`, `--push`, `--video`, drift report), `export-tracking-policy`, `upload-motion`, `combine-motions`, `visualize-motions`.
- **Data pipeline** `tools/`: `beat2_batch.py` (spec → segments → GMR → `ground_clip` → Gate 1 QC → combined files → leakage check → upload; cached, `--workers`), spec `tools/datasets/beat2_full.toml` (held-out speakers, `[qc] exclude_clips`), `beat2_segments.py` (Tier A still / Tier B `_shift` clips), `beat2_to_gmr.py`, `gmr_retarget.py` (**run with `~/projects/GMR/.venv/bin/python`**), `ground_clip.py` (ground + flatten feet; run on every GMR clip), `clip_qc.py` (Gate 1, `LIMITS`), `upload_combined.py`.
- **Eval / live / robot tools** `tools/`: `eval_summary.py` (eval JSONs → per tier / speaker table), `gesture_sync_check.py`, `live_test.sh` (gesture service + speech loop + film, script in `notes/live_test_script.md`), `export_deploy_clip.py` (clip + `--audio` for `booster_deploy`), `make_deploy_golden.py` (golden file keeping `booster_deploy`'s torch port equal to `deploy/`; rerun when deploy code changes), `laptop_build_governor.sh`.
- **Tests:** `uv run --with pytest pytest tests/ -q` (CPU; `test_multi_motion.py` needs `logs/motions/waves_2clip.npz`).
- Data outside the repo: `~/robotics/data/` (BEAT2 incl. `wave16k/` audio, mixed int16 / float32; AMASS, HumanML3D; build caches), GMR at `~/projects/GMR`, `booster_assets` at `~/projects/booster_assets`. `docs/motion_preparation.md`: GMR `.pkl` / BeyondMimic `.csv` → upload.

## Commands
```
E=bmcox2-university-of-illinois-urbana-champaign
uv run train <TASK> --registry-name $E/motion_upload/<artifact> --env.scene.num-envs 4096 2>&1 | tee logs/train_<name>.txt
uv run play <TASK> --wandb-run-path $E/mjlab/<run-id>
uv run eval-tracking --wandb-run-path $E/mjlab/<run-id> [--task <TASK>] [--push] [--checkpoint-name model_N.pt]   # one row per clip
uv run sim2sim --wandb-run-path $E/mjlab/<run-id> --motion-file <npz> --clip <name>   # from standing, like the robot
uv run upload-motion --input-file <clip.pkl> --entity $E
uv run combine-motions <artifact> ... --artifact-name <name>
uv run python tools/beat2_batch.py --spec tools/datasets/beat2_full.toml [--stages segment] [--no-upload]
uv run gesture live [--replay-session speech/runs/<session> --replay-audio]   # K1 gesturing live in a MuJoCo window
tools/live_test.sh                                                            # whole live test + film
```
Tasks: `Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation` (deployable), `Mjlab-Tracking-Flat-Booster-K1` (sim-only), `Mjlab-Velocity-Flat-Amp-DA-Muon-Booster-K1` (velocity baseline `2wagxxko`).

## Environment gotchas
- **WandB entity is the team** `bmcox2-university-of-illinois-urbana-champaign` (not `bmcox2`, not the `-org` name); `WANDB_ENTITY` is set in `~/.bashrc`. Conventions: runs named `MM-DD what-it-is`, tagged (`tracking`, `beat2`, `keep` / `superseded`...), one-line result note; dataset versions get a description; the `current` alias moves to the version in use.
- **Resume training:** `--agent.resume True --wandb-run-path $E/mjlab/<run> --wandb-checkpoint-name model_N.pt`, or it silently starts from scratch. `--agent.max-iterations` counts *additional* iterations.
- **Club GPU PC** (`sigrobotics`, RTX 5070 Ti, x86, not the robot): `ssh booster@10.193.169.55` (campus network / VPN only). Shared account: no `wandb login`; run `source ~/bmcox2/.wandb_env` in every new shell. Check `nvidia-smi` first (full-BEAT2 run needs ~10–12 GB); long jobs in `tmux` (`tmux new -s train`, detach `Ctrl-b d`). Disk is nearly full.
- **The K1:** `ssh k1` (`booster@10.193.195.162`, IllinoisNet DHCP, may change) or `ssh k1-cable` (`192.168.10.102`; laptop Ethernet static `192.168.10.10/24`, no gateway). Password in `secrets/k1_access.md`. No RTC battery: if offline, `sudo date -s @<laptop epoch>`. IllinoisNet certificate renewal due 2026-12-18.
- **Laptop** (Dell XPS 15, RTX 4070 8 GB, Ubuntu 24.04): the dGPU drops out (hardware PCIe fault; BIOS can hide it for days) and `nvidia-smi` breaks after kernel updates: fixes in `notes/laptop_gpu.md`. Stop if the GPU sustains > ~87 °C. Prefer the club GPU for training.
- **Videos from VS Code's terminal:** VS Code is a snap, so `xdg-open` → VLC crashes. Open from Files, use `ffplay`, or `env -u GTK_PATH -u GTK_EXE_PREFIX -u GIO_MODULE_DIR -u LOCPATH vlc <file>`.

## Milestones (details in `notes/log.md` / `notes/archive/log_2026-10.md`)
- 2026-10-15/16: single-clip waves tracked (`me9exatd`, `pqh0whw0`: 50/50, hands 1.5–1.7 cm); multi-clip tracking works (`8ku1opzv`).
- 2026-10-18: torso IK config fixes the lean-back; first general BEAT2 tracker `0j0flpxj` (10 s windows).
- 2026-10-19/21: full BEAT2 (A+B tiers) → `1de2pner`; safety harness; dataset rebuilt as `train-ab:v0`.
- 2026-10-28 – 11-05: deployable task, policy-only ONNX, `deploy/` + `sim2sim`, deploy audit → `y1r48dhc`.
- 2026-11-08 – 11-12: speech loop steps 1–4 (streamed, ~1.5 s response); gesture generator steps 1–4, 6, 7 (live streaming in sim, 10-min conversation without falls); cloud TTS.
- 2026-11-12: **first robot session**: 4 floor runs of the gesture tracker, no falls.
- 2026-11-13: plan for the onboard conversation on 2026-11-19.
