# K1 Co-Speech Gesture Project: Run Log

October 2026 (setup → BEAT2 tracker → deploy prep): `notes/archive/log_2026-10.md`. Newest entry last; open work in "Next" at the bottom.

## 2026-11-05: deploy audit against the club's `booster_deploy`

Analysis only, no code changed, nothing trained. Full findings: **`notes/deploy_audit.md`**. Reference clone at `~/projects/booster_deploy` (`main` `9a677ad`, `hoi-dev` `295ce53`).

**Results**
- Verdict: **needs config fixes on `y1r48dhc`**, not deployable as-is. `1de2pner` needs retraining (it observes `motion_anchor_pos_b` and `base_lin_vel`)
- Found run **`y1r48dhc`** (`deploy-nse-train-ab`, No-State-Estimation task, `train-ab:v0`, 6k it, finished 2026-10-29, not logged here until now). `policy.onnx`: `obs [1, 122]` → `actions [1, 22]`, normalizer baked in, no history. **No eval or sim2sim from standing yet**
- `booster_deploy` `main` has `tasks/beyond_mimic/`, a K1 motion-tracking task: use it as the playback template and `mjlab_velocity` as the config template. Not reusable unchanged: Isaac joint order (`sim_joint_names`), 119 inputs (no `projected_gravity`), action scale from `K1_CFG` (arms 0.875 vs 0.35)
- `K1_CFG` mismatches to override: default pose, Kp/Kd (training head 4/0.25, arms 20/2, legs 80/4, ankles 50/2), effort limits, `prepare_mode`. Matches: joint order by position, 50 Hz, 50 fps clips, link masses and inertias
- Real K1 bags on `hoi-dev` (`/low_state`, 500 Hz): home pose in the expected order and signs. **Ankles are physically parallel, but the interface is serial**: drive motors match `parallel_ankle_ik.py` to ~1 mrad. Keep training serial
- `tests/test_deploy.py`: 2 passed

**Open risk**
- How the firmware applies ankle `kp`/`kd`. Per motor, at the home pose, ankle roll would be 12.7 / 0.51 instead of the trained 50 / 2, far outside the ±20% randomization, and that could force a retrain. Ask the lead or test on the gantry (`deploy_audit.md`)

**Sim2sim from standing** (`y1r48dhc` `policy.onnx`, plain MuJoCo, 15 held-out clips, CPU; table in `deploy_audit.md`)
- **0 falls in 225 runs**, hands 3.05–3.11 cm, drift ~5 cm: with prepare-pose hold, actuator lag up to 40 ms, sensor delay, pushes, and the ankle what-ifs
- **The old `sim2sim` default fell (15/15 at ~0.75 s), an artifact:** `--settle-s` 1.0 held home at the policy's gains and the robot tipped 22° before the policy started. Default changed to 0 in `scripts/sim2sim.py`. Checked with the CLI on 3 clips that used to fall (no falls; Stewart with 40 ms delay + pushes 3/3); `tests/test_deploy.py` still passes
- Ankle what-ifs (gains if applied per motor, linkage inertia and torque, home-pose values in the serial model): no falls, action rate up about a third. Lowers the retrain risk without removing it
- Quick-check sweep scripts were scratch only, not in the repo

**Eval: `y1r48dhc` vs `1de2pner`** (`model_5999`, `heldout-val:v0`, club GPU, `tools/eval_summary.py`)

| group | `1de2pner` | `y1r48dhc` |
|---|---|---|
| all | 194/194, 3.46 cm | 193/194, 3.82 cm |
| tier A | 162/162, 3.39 | 161/162, 3.76 |
| tier B | 32/32, 4.48 | 32/32, 4.55 |
| ayana | 47/47, 3.75 | 47/47, 4.23 |
| kieks | 31/31, 3.07 | 30/31 (99.9% of rollouts), 3.81 |
| li | 28/28, 3.47 | 28/28, 3.80 |
| nidal | 44/44, 3.34 | 44/44, 2.88 |
| stewart | 30/30, 3.52 | 30/30, 4.51 |
| yingqing | 14/14, 4.13 | 14/14, 4.81 |

- Dropping the two sim-only inputs cost 0.36 cm of hand error overall (~10%) and one clip with a failed rollout. Stewart is worst (+1.0 cm); Nidal improved
- `kieks_0_9_9_t19-38`: 1/50 failed, at 0.52 s (`ee_body_pos`), so near the start. The lead-in on the robot avoids the eval's jittered start

**Eval on `val:v1`** (472 clips, ~5 min each on the club GPU; `1de2pner` rerun, its older `val` numbers were on `v0`)

| group | `1de2pner` | `y1r48dhc` |
|---|---|---|
| all | 466/472, 99.5% of rollouts, 4.39 cm | 468/472, 99.3%, 4.57 cm |
| tier A | 281/282, 3.97 | 281/282, 4.25 |
| tier B | 185/190, 5.48 | 187/190, 5.40 |

- Hand error +0.18 cm (~4%). Speakers vary: worst Kexin (2.77 → 4.26) and Katya (4.31 → 5.89); several improve (Zhao, Lawrence, Goto, Solomon, Scott, Lu, Jorge)
- `y1r48dhc` failures, all `ee_body_pos`:

| clip | `y1r48dhc` failed | `1de2pner` failed | first failure |
|---|---|---|---|
| `solomon_0_13_13_t29-40_shift` | 50/50 | 50/50 | ~10.2 s, both |
| `solomon_0_16_16_t19-23_shift` | 50/50 | 50/50 | ~3.1 s, both |
| `solomon_0_16_16_t59-67_shift` | 50/50 | 10/50 | ~7.7 s, both |
| `lawrence_0_12_12_t26-38` | 6/50 | 7/50 | 0.08 s, both |

- The clips look like the problem: both policies first fail at the same moment on all four. `t59-67` is new to the notes and `y1r48dhc` handles it worse (50/50 vs 10/50). `solomon_0_12_12_t58-77_shift`, in the older watch list, isn't in `val:v1`
- `1de2pner` alone also failed 1/50 on `solomon_0_14_14_t0-15_shift` and `lawrence_0_12_12_t65-72_shift`
- **Decision: `y1r48dhc` `model_5999` is the deployment candidate.** No retrain needed from these evals

**Demo clip candidates** (held-out Tier A; arm motion from the local `heldout-val` file)
- Lowest hand error is a poor way to pick: the 25 lowest-error clips of the 72 that pass 50/50 with foot tilt ≤ 10° are mostly quiet Nidal and Kieks clips (hand speed above 0.4 m/s < 5% of the time for most). The strongest motion (Ayana, Yingqing) often exceeds `Right_Elbow_Yaw`'s real limit, by up to 0.19 rad
- Shortlist, none tested with `eval-tracking --push` yet:

| clip | length | mean hand speed | hands fast | over limit | `eval-tracking` |
|---|---|---|---|---|---|
| `ayana_0_15_15_t75-95` | 19.9 s | 0.20 m/s | 26% | 0.006 rad, 4% of frames | 50/50, 3.1 cm, tilt 8.9° |
| `ayana_0_11_11_t8-23` | 15.2 s | 0.16 m/s | 20% | none | 50/50, 3.1 cm, tilt 6.6° |
| `ayana_0_9_9_t52-69` | 17.2 s | 0.22 m/s | 30% | none | not checked (outside the top 25) |

- Sim from standing, 6 candidates incl. `ayana_0_16_16_t15-30`, `yingqing_0_9_9_t48-59`, `kieks_0_14_14_t18-35`: repo MuJoCo 72 runs (lag 25/40 ms, pushes, ankle what-ifs), 0 falls; `booster_deploy` controller 12 runs (0/40 ms command lag), 0 falls, targets never clamped. `ayana_0_16_16_t15-30` dropped: a torque limit reached on ~14% of steps (others 1–3%; which joint not checked)
- Audio: only 5 Scott takes are downloaded (`wave16k/`), so these clips have no audio on disk yet

**Deploy task** (`~/projects/booster_deploy`, local branch `gesture-tracking`, not committed; guide: `docs/k1_gesture_deploy.md` there)
- `tasks/gesture_tracking/`: task `k1_gesture_tracking`. Observation order from the ONNX metadata, training gains, no joint remapping, lead-in + end hold, heading alignment, targets clamped to `k1.xml` limits, tilt safety stop, `exit_mode="damping"`. `scripts/deploy.py` and `render_video.py` got `--motion`
- This repo: `tools/export_deploy_clip.py` (one clip per file, with joint and body names), `tools/make_deploy_golden.py` (numbers from `booster_mjlab.deploy` for the task's tests)
- Tests: `tests/test_gesture_tracking.py` 2 passed: observation (1e-5) and reference match `booster_mjlab.deploy`
- Refuses at startup: 128-input `1de2pner`, velocity `baseline.onnx`, combined motion file, `K1_CFG` default gains, wrong default pose
- `booster_deploy`'s `MujocoController` on `K1_22dof.xml` (ground friction 0.4, condim 1, unlike training), 3 held-out clips, each with 0 / 20 / 40 ms command lag: 9/9 no falls, drift ≤ 5 cm, max trunk tilt 11.6° (`li` Tier B)
- Not tested: the real-robot controller path (needs ROS and the robot); parallel-ankle model (the `ParallelAnkle` code is on `hoi-dev`)
- Decided: the ankle `kp`/`kd` question is deferred; keep trained gains and deal with it if bring-up shows a problem

## 2026-11-08: dry-run mode and demo audio

**Audio**
- Downloaded 4 BEAT2 takes' audio (`H-Liu1997/BEAT2`, same source as the motion): `21_ayana_0_15_15`, `21_ayana_0_11_11`, `21_ayana_0_9_9`, `27_yingqing_0_9_9`
- `tools/export_deploy_clip.py --audio`: writes `<clip>.wav` (16-bit, 16 kHz), the exact segment span from `segments.json`. Lengths match the motion to 0.01 s
- Clips + audio for the 4 candidates in `booster_deploy/tasks/gesture_tracking/motions/` (gitignored)
- Dubbed sim videos: `logs/videos/<clip>_audio.mp4` (sim2sim from standing, audio delayed 3 s for the lead-in). 4/4 no falls, hands 2.2–3.1 cm

**`booster_deploy` (branch `gesture-tracking`, not committed yet)**
- `deploy.py --audio <wav>`: plays it with `aplay` on the machine running the policy, starting at the clip's first frame (checked in MuJoCo: frame 150, after the 3 s lead-in). A missing player prints a warning and the motion continues
- `deploy.py --dry-run` (robot only): reads `/low_state` and runs the policy, but never publishes `/joint_ctrl` and never changes the robot's mode. Logs every step to `logs/dry_run_<task>_<time>.npz`
- `scripts/check_dry_run.py`: loop timing, stale `/low_state`, trunk tilt, joint limits, and the gap between the first 0.1 s of targets and the joints
- Tested without a robot, using faked ROS / `booster_interface` modules and simulated `/low_state` at 500 Hz: 0 publishes and 0 mode-change calls, 50 Hz loop (p99 22 ms), log written. Correct wiring: first targets ≤ 0.22 rad, passes. Left/right shoulder roll swapped: 1.18 rad, flagged
- Not tested on the robot; the real ROS path runs for the first time at bring-up

**Demo clip ranking** (watched the dubbed videos): 1. `ayana_0_9_9_t52-69`, 2. `ayana_0_15_15_t75-95`, 3. `yingqing_0_9_9_t48-59`, 4. `ayana_0_11_11_t8-23`
- The top pick has no `eval-tracking` numbers checked yet (it wasn't in the top-25 list), so it needs the normal eval and the `--push` eval before the robot. Couldn't ssh to the club GPU today
- `logs/videos/*_audio.mp4` also matches the older `0j0flpxj_scott_audio.mp4` / `s5cdzms7_scott_audio.mp4`, which play in the same loop

## 2026-11-08: speech loop v0 (speech_plan step 1) + first benchmarks

**Setup**
- `speech/`: own uv project (Python 3.12). `uv sync`; Groq key in `speech/.env` (gitignored). Stages `speech.audio|stt|llm|tts`, the loop `speech.loop`, voice sampler `speech.voices`; each reads/writes files in `speech/runs/<session>/turn_NN/` and runs alone on saved files. Usage: `speech/README.md`
- Models: STT faster-whisper `small.en` int8 on CPU; LLM Groq `openai/gpt-oss-20b` (reasoning low) via the OpenAI-compatible API; TTS Kokoro-82M on CPU, voice **`bm_daniel`** (picked from the 13 English male voices)
- Audio: laptop mic + laptop speakers through PipeWire (`config.toml` device `pipewire` = the choice in Settings → Sound)

**Results**
- Step 1 exit criteria met: 6-turn spoken conversation with history, every artifact opens, LLM/voice switch in `config.toml`
- Wait per turn ~3.5–6 s: STT 1.6–2.2 s, LLM 0.2–0.4 s, TTS 1.5–3.9 s (grows with reply length)
- Benchmarks (`speech/bench/stt.py`, `tts.py`; tables in `notes/speech_bench.md`): **Groq whisper-large-v3 0.29 s median vs local small.en 1.58 s, and better**; all 3 Groq LLMs < 0.5 s to the whole reply; Kokoro first sentence ~1.0 s at 4 threads (faster than the default 14). Streamed estimate with Groq STT: ~2 s; the rest must come from TTS + end-of-turn

**Problems & fixes**
- AirPods silent on playback once their mic was used (Bluetooth call mode, HFP mSBC) → laptop mic + speakers
- faster-whisper 1.2.1 broke on `av` 19 (`metadata_errors`) → pinned `av<16`
- Kokoro re-downloaded spaCy `en_core_web_sm` every run → added as a URL dependency (hatch `allow-direct-references`)
- Groq dropped Llama 3.1 8B; models on 2026-11-08: gpt-oss-20b/120b, qwen3.8-27b, Whisper, Orpheus TTS
- Whisper mishears project words ("Booster Lab" → "Ibusa Lab")
- dGPU still missing after two reboots (`lspci` shows no NVIDIA), so everything runs on CPU

## 2026-11-08: speech step 2 (instrumentation, test set, latency budget)

**Built** (`speech/`)
- STT providers: Groq Whisper (default, now `whisper-large-v3-turbo`) with automatic fallback to local `small.en` (tested with a bad key); hint words `prompt` (Booster K1, Booster Lab, SIGRobotics, mjlab)
- Kokoro `cpu_threads = 4`
- `timing.py`: events on one monotonic clock (0 = speech end) → `timing.json` per turn + `runs/latency.jsonl`; `speech.latency` = median / p90 / max per stage, grouped by setup label
- `speech.testset record|run`: 12 scripted recordings (WAVs gitignored, repo is public; references in `testset/testset.json`), replayed with `--set key=value` overrides; scores word error rate (`metrics.py`, fillers dropped, digits = number words)
- `loop.py` refactored into `Pipeline.run_turn` (shared by the live loop and the test set); LLM stage reports first-sentence time

**Results** (tables in `notes/speech_bench.md`)
- Current setup on the test set: STT 0.35 s, LLM 0.29 s, **TTS 2.95 s median / 4.83 s p90**, reply ready 3.58 / 5.54 s. TTS = 82% of the wait
- STT: Groq turbo 0.33 s, 3.8% word errors; large-v3 0.35 s, 10.1%; local small.en 1.60 s, 8.1%
- Streaming estimate (first chunk): 1.62 s median / 2.01 s p90. Kokoro on CPU needs ≥ 0.72 s for even "Sure thing." → < 1 s needs GPU Kokoro or a cloud TTS
- Latency budget written (end of turn 0.25, STT 0.30, LLM 0.25, TTS 0.15, hand-off 0.05)

**Problems & fixes**
- A bad edit (empty-string replace) blew `config.toml` up to 18,906 lines; rebuilt from git with exact-match edits
- Setup label didn't include the hint prompt, so a no-hints run got grouped with the hints run; label now ends in `+hints`
- Test-set references probably wrong for `pause_short` and `point` (all 4 STT runs agree on different words); listen and fix

## 2026-11-10: plan review against the field (2025–2026) + new next steps

Analysis only: no code changed, nothing trained. Reviewed the repo notes and recent papers, then re-ordered the plan (`roadmap.md` updated, reading list in `papers.md`). Some papers' middle sections were read through summaries: check the PDF before relying on a number.

**What the field does**
- **RoboGesture** (arXiv 2608.28693, Aug 2026, G1): streaming flow-matching generator in 1 s chunks (~0.25 s per chunk), outputs **robot joints directly** (upper body + hands; human motion retargeted offline with GMR for training). Legs use Unitree's built-in standing controller. Its dominant delay is LLM + TTS + chunking, not motion. No code found
- **PhysDrift** (2606.19935, G1): BEAT2 retargeted offline, generator outputs G1 joint space directly. No code found
- **GenTrack** (2608.01410, sim only): generated motion differs from mocap mainly in jerk, foot skating, root height, foot clearance. Frozen SONIC completes 92.6% of generated references; fix trains the tracker on 50/50 mocap + generated references (and the generator against the tracker)
- **EMAGE is offline only** (needs the whole utterance; marked non-streaming by both papers below). Streaming BEAT2 generators: LiveGesture (2604.10927; 200 ms chunks, zero look-ahead, first output 250 ms) and GestureFAR (2609.21576; ~4× real time on a MacBook Air). No code found for either
- **What Matters in Humanoid General Motion Tracking?** (2607.19903; YAHMP, open source on mjlab, `github.com/hucebot/yahmp`; G1, zero-shot real): removing observation history raised base errors 38–50% and key-body ~10%; History-20 no better than History-10; residual actions ~5% better key-body; teacher-student only small gains
- **SONIC / GR00T-WholeBodyControl**: weights, training code and deploy stack released, G1 only. Architecture: one tracker as the interface, planners and a VLA on top

**Decisions**
- Goal: a working system first (experience, resume); a paper is a bonus. Generator and TTS can run on the club GPU. Plan without hands
- **Speech pauses after step 3 live test 2.** Step 4 (streaming) waits until the pieces are connected live; step 5 (barge-in) waits for the K1 mic check. The generator can use saved TTS WAVs from `speech/runs/`
- **Main work: the gesture generator.** EMAGE offline smoke test first (milestone 2), then a **retrieval generator v0**: match TTS audio windows to BEAT2 K1 clips by rhythm/energy, crossfade (~0.3 s), idle stretches, fixed standing lower body. Uses only motion the tracker already passes
- **History experiment** before the final run: No-State-Estimation task with the actor group's `history_length` = 10 (mjlab `ObservationGroupCfg`), same data, compare with `y1r48dhc` on `heldout-val`. If adopted, `deploy/build_observation` and the `booster_deploy` task must stack past frames
- Runtime contract: a **50 Hz K1 reference stream** (joint pos/vel, trunk orientation; later a root velocity command). Keep GMR/`ground_clip` (whole-clip, offline) out of the runtime path

**New risks recorded** (`roadmap.md`): continuous operation (minutes of idle → gesture → idle; drift ~5 cm per clip, heading checked over 8 s only), no listening behaviour, robot self-noise for barge-in, no observation history.

**Built: observation-history experiment** (code only, no real training yet)
- Task **`Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation-History10`**: `booster_k1_flat_tracking_env_cfg(actor_history_length=10)` sets the actor group's `history_length` (critic unchanged). Actor input 1220 = 122 × 10
- mjlab's layout (read from `observation_manager.py` / `circular_buffer.py`): per term, frames oldest → newest (`[A_t-9..A_t, B_t-9..B_t, ...]`); after a reset the first frame fills every slot
- `policy.onnx` metadata gains `observation_history_length` (`observation_dims` stay the stacked sizes the network sees). `TrackingPolicy.history_length` / `.frame_dims`; new `deploy.ObservationHistory` stacks one-frame observations in mjlab's order; `sim2sim` uses it (no change for history 0)
- `tests/test_deploy.py::test_observation_history_matches_mjlab`: deploy stacking vs mjlab for 15 steps incl. a mid-run reset, 1e-5. Suite: 18 passed (CPU, 110 s)
- CPU smoke run (`WANDB_MODE=offline uv run train ...-History10 --env.commands.motion.motion-file logs/motions/waves_2clip.npz --env.scene.num-envs 64 --agent.max-iterations 2 --gpu-ids None`): trains, exports `policy.onnx` (obs 1220, history 10, frame dims sum 122); `sim2sim --policy` on it runs (falls at 1.18 s, expected after 2 iterations)
- `booster_deploy`'s `k1_gesture_tracking` refuses a history policy at startup (its size check expects `command` 44, gets 440). Teach it `ObservationHistory` only if history wins

## 2026-11-11: speech step 4 (streaming) + fixes; speech paused

**Built** (`speech/src/speech/streaming.py`, on by default via `[stream]` in `speech/config.toml`)
- LLM stream → `Chunker` (cut at `, ; : . ! ?` + space; first piece ≥ 2 words, later ≥ 6) → TTS worker thread (Kokoro) → `Player` (one open 24 kHz output stream, plays pieces back to back, measures gaps and when each piece started). Captions print each piece when it starts playing. `tts.json` lists every piece (text, start sample, ready / played times): the hook for gesture sync
- Kokoro padding trimmed (~0.25 s before + ~0.45 s after each piece made 0.7 s pauses); natural pause appended to the end of each piece (300 ms after `. ! ?`, 150 ms after `, ; :`)
- End of turn: Smart Turn needs ≥ 0.95 during the first 800 ms of a pause, then 0.8 (`smart_turn_strict_*`)
- LLM: `<think>` blocks stripped from qwen's stream; an empty reply is retried once with a nudge, then "Mm-hm."; empty replies left out of the history

**Results** (details in `notes/speech_bench.md`)
- Live test 1 with streaming (14 turns): **response 1.79 s median / 2.24 s p90** (was 3.71 / 8.50 s); measured gaps 0; voicing the first piece 0.71 s
- Complaints → fixes: 0.7 s pauses between pieces (Kokoro padding, above); 5 cut-offs in 14 turns at pauses ("...talking about" scored 0.81) → strict threshold (replay of 30 live turns: the 6 cut-offs wait ≥ 1.1 s, finished turns still 0.22 s median)
- Live test 2 (17 turns): fewer cut-offs, pauses more natural; voice still sounds robotic (Kokoro; later). Robot silent on 2 turns: qwen3.8-27b returned 1 token and no text after a statement, and the empty reply in the history primed the next one → retry + history filter above. Replaying that request 5×: 1 empty, retried, answered

**Left for when speech resumes:** barge-in (step 5: you keep talking, the robot stops; also the real fix for pauses > 1 s after a complete sentence), a less robotic voice (Orpheus / ElevenLabs / Cartesia, or GPU Kokoro), < 1 s needs faster first audio than Kokoro on CPU (0.65–1.1 s), Pipecat spike (not done)

## 2026-11-11: gesture step 1 (BEAT2 audio + sync check)

(Moved here from "Next" on 2026-11-13.) Plan: `gesture_plan.md` step 1.

- **Audio downloaded:** Wayne, Lawrence, Miranda (most Tier A training hours with fair arm motion; Scott has only 0.5 h Tier A, Solomon/Sophie have data issues). `uv run hf download H-Liu1997/BEAT2 --repo-type dataset --local-dir ~/robotics/data/BEAT2 --include "beat_english_v2.0.0/wave16k/1_wayne_*.wav" ...` (one `--include` per speaker): 382 files, 1.4 GB. Every take has audio, none shorter than its motion. Library from them: **2,564 `train-a` clips, 8.0 h** (Wayne 2.3, Lawrence 2.6, Miranda 3.2). Only `train`/`additional` takes are in `train-a`; their `val`/`test` takes are extra test audio for step 5
- **WAVs are mixed int16 and float32**: convert to float (int16 / 32768) before any feature
- **Sync check done 2026-11-11** (`tools/gesture_sync_check.py`: loudness (RMS dB, 50 Hz) vs hand speed relative to the trunk, cross-correlation over ±1 s; `--dir` for exported clips, `--motion-file` for library clips). Dubbed `sim2sim --start reference` videos of 3 Scott `test` clips in `logs/sync/`: watched, nothing visibly off, looks fairly natural in short clips (naturalness judged later on full conversations, step 5). **Step 1 done**
  - Video playback from VS Code's terminal: VS Code is a snap and its terminal passes snap GTK variables, so `xdg-open` → VLC crashes (`symbol lookup error ... /snap/core20/...libpthread`). Open from Files, use `ffplay`, or `env -u GTK_PATH -u GTK_EXE_PREFIX -u GIO_MODULE_DIR -u LOCPATH vlc <file>`
  - 3 Scott clips alone: noise (corr 0.03–0.23, lags −0.4 to +0.3 s). Use many clips
  - **Hands lead loudness by ~0.4 s**: Wayne + Lawrence, 400 clips, pooled peak −0.44 s (corr 0.13; 0.05 at 0 s). Their audio is in sync (jaw check below), so this is how people gesture, not an offset. Retrieval keeps it automatically (units carry their own audio), but the generator needs ≥ ~0.5 s of audio ahead of the motion it plays
  - **Loudness alone is a weak predictor** (corr ~0.1): expected; step 2 must test onsets / pitch too
  - Jaw check, first version (jaw **angle** vs loudness): Wayne, Lawrence, Scott −33 ms, Miranda session 1 0 ms, Miranda session 0 0.5–1.9 s off. **Corrected the same day (step 2): that Miranda result was wrong.** With jaw opening **speed** (syllable rate) her session-0 takes are in sync (median +33 ms, 84% within 67 ms); the slow jaw angle also opens to breathe in before a phrase, which fooled the first check
  - ~~Decision: library drops Miranda session 0~~ (withdrawn). The per-take jaw-speed gate (±0.2 s) drops 12 takes instead: Miranda 10 (−0.27 to −0.80 s), Wayne 2

## 2026-11-11: gesture step 2 (features, units, library, does audio predict motion?)

**Built** (`src/booster_mjlab/gesture/`, CLI `uv run gesture build-library | report | analyze`, tests `tests/test_gesture.py`)
- `audio.py`: speech features at 50 fps, each window centered on its motion frame: loudness (RMS dB, 40 ms), onset strength (spectral flux on 40 log bands), voicing + pitch (autocorrelation with window correction, Boersma 1993; shortest-period peak within 90% of the best, to avoid octave errors), speech/pause. Pitch checked against librosa pYIN (installed temporarily with `uv run --with librosa`, not a dependency) on 30 s of Wayne, Lawrence, Miranda (both sessions) and Kokoro: medians within 2–4%, 84–90% of frames within 1 semitone, octave errors 0–3.5%, voicing agreement 77–91%
- `motion.py`: hand speed + position in the **trunk frame**; `cut_units`: cut where the hands pause (dip ≥ 0.1 m/s and at least halving the speed), 0.5–3 s
- `sync.py`: per-take jaw gate (jaw opening **speed** vs loudness, |lag| ≤ 0.2 s)
- `library.py`: per-take features cached in `~/robotics/data/gesture/features/v1/`; library `~/robotics/data/gesture/library_v0.npz` (build 25 s, rebuild 4 s)
- `analysis.py`: the predictability report (`logs/gesture/analysis_v0.json` / `.png`)
- Tests: 7 synthetic-signal tests (frame centering, +20 dB for 10× amplitude, pitch 90–330 Hz within 2% and noise unvoiced, onsets within 1 frame, pauses, unit cuts); full suite 25 passed

**Library v0:** Wayne, Lawrence, Miranda; 310 takes, 12 fail the jaw gate (Miranda 10 at −0.27 to −0.80 s, Wayne 2) → **2,487 clips, 7.77 h, 20,514 units** (median 1.26 s)
- Unit rule: cutting at every speed minimum gave 31,953 units (median 0.82 s) with cuts in mid-movement (p90 0.45 m/s) and on noise while still. The dip rule: median 1.26 s, cuts at median 0.10 / p90 0.34 m/s (`logs/gesture/units_v0.png` vs `units_v1.png`)
- 5 random units rendered with their audio: `logs/gesture/units/*_audio.mp4` (sim2sim `y1r48dhc`, 0 falls); not watched yet

**Does audio predict hand motion?** (`uv run gesture analyze`, 2.5 min; target = mean hand speed z-scored per take; baselines = same model on shuffled labels)

| test | r held out | shuffled |
|---|---|---|
| 1 s windows, unseen takes (ridge) | 0.21 | 0.00 ± 0.03 |
| 1 s windows, unseen speaker (ridge) | 0.19 (Wayne 0.20, Lawrence 0.28, Miranda 0.16) | 0.01 ± 0.05 |
| 1 s windows, unseen speaker, nearest neighbours (retrieval) | 0.15 | 0.00 ± 0.01 |
| units, unseen speaker, nearest neighbours | 0.13 | 0.00 ± 0.01 |

- **Real but weak**: consistent across speakers and to an unseen voice, ~4% of the variation. 2 s windows no better than 1 s
- Hands lead the audio: best lag −0.44 s (loudness r 0.12, onset 0.10, speech 0.11, pitch 0.03). Miranda's lag is shorter (−0.16 s) than Wayne/Lawrence (~−0.5 s)
- Useful features: onset (rhythm) and peak loudness (ridge weights 0.18, 0.14). **Pitch adds nothing**: its −0.15 was a voicing confound (partial r 0.02)
- **Pauses are the clearest signal**: mostly-pause windows −0.49 sd hand activity vs +0.10 during speech
- **Timing:** strong accents (loudness ≥ 2 sd above surroundings) are 1.16–1.25× more likely near a stroke's **end** (hand arriving, ~−0.1 s) than at random; looser accents or the speed peak give ~1.1×

**Implications for step 3** (`gesture_plan.md`)
- Retrieval should beat random clearly in *when* the hands rest (pauses) and modestly in *how much* they move; don't expect audio matching alone to make gestures fit the words
- Match on onset_mean, loud_max, loud_mean, speech_frac (drop pitch); shift motion −0.44 s
- Add an explicit timing term: time-fit units so stroke ends land on strong accents
- The step 5 viewer test (retrieval vs random) decides whether this is enough; words/semantics (BEAT2 TextGrids, LLM tags) are the likely next lever

## 2026-11-11: gesture step 3 (matching + stitching): TTS reply -> K1 reference

**Built** (`src/booster_mjlab/gesture/generate.py`; CLI `uv run gesture generate | render | check`)
- `generate --reply speech/runs/<session>/turn_NN [--random-baseline]` -> `logs/gesture/replies/<session>_<turn>/`: `reference.npz` (combined layout, 50 fps), `motion.pkl` / `motion_grounded.pkl`, `reply.wav`, `plan.json` (segments, units, costs, crossfades, QC, timings)
- Pipeline: reply features (`analysis.recording_features`, same normalization as the library; test added) -> segments at word starts / pauses (~1.3 s) -> per-segment candidates (audio match on onset/peak/mean loudness/speech share; stretch <= 15%; intensity target = activity of the 50 most similar-sounding units; calm units only in mostly-pause segments; reply accents vs the unit's stroke ends) -> Viterbi with transition cost (joints, legs x2, hands, trunk twist relative to the feet, speaker switch) -> stitch the source GMR pkls at 30 fps (time-stretch, heading/position continuity, crossfade using frames past each cut) -> **foot lock** -> `ground_clip` -> `clip_qc` -> `convert_batched`
- `render --dir <ref> [--push --obs-delay-steps 2 --runs 5 --no-video]`: `sim2sim` from standing (`y1r48dhc`, 2 s blend + 1 s hold), reply audio dubbed with delay 3 s + 0.44 s -> `sim_audio.mp4`
- `check --dirs logs/gesture/replies/*`: seams, feet travel, Gate 1, hand speed, accent hits vs chance, pause vs talk
- Speed: features 13–32 ms, search 4–16 ms, stitch 3–36 ms per reply (< 100 ms); foot lock 0.1–0.2 s; library index load 2.8 s once

**Problems found and fixed (in order)**
- Feet slid 17–20 cm per reply (every unit brings its own stance; Gate 1 "K1 feet move 11 cm") -> **foot lock**: one stance per reply, trunk pose kept relative to the feet, legs by IK
- Foot-lock IK diverged on one reply (2.5 m miss -> joint jump -> fall): `Grounder.solve_leg` wants position and full foot orientation; with the trunk twisted against locked feet the hip hit its limit -> own IK with exact position, level sole, soft foot angle, hold the previous legs if unreachable
- A knee flicked at 3.2 rad/s where two units twist the trunk 16° differently relative to the feet -> stance smoothed over 0.8 s in the foot lock + twist term in the transition cost (library now stores per-frame `twist`; trunk vs feet within about ±25° for 90% of frames)
- Forearm spun at 5.5 rad/s at a seam (hands alike, elbow yaw 0.8 rad apart) -> crossfade length per seam so no joint exceeds 2 rad/s (0.3–1.0 s)
- **Replies were subdued** (chosen units −0.70 sd activity): the pause term leaked into speech (`(1 − speech share) × activity`), and units that fit ~1.3 s segments are calmer (short units are quick beats: 0.5–0.8 s +0.34 sd, 2.5–3 s −0.40) -> pause term only below 50% speech + intensity target from audio neighbours -> −0.07 sd; shorter segments not needed
- Mixed speakers within a reply (Lawrence then Miranda) -> speaker-switch cost

**Results** (5 real speech-loop replies, 5.6–13.2 s, + random baselines; `gesture check`)

| | matched | random (audio ignored) |
|---|---|---|
| Strong accents with a stroke end within 0.14 s | **16/19 (84%)**, chance 26% | 7/19 (37%), chance 21% |
| Hand speed | 0.38 m/s (library 0.40) | 0.30 m/s |
| Worst seam | 3.7 rad/s (not above that reply's other motion) | 5.8 rad/s |
| Feet travel | ≤ 0.1 cm | 0 |
| Gate 1 severe | 0 (1 mild: elbow bend at limit 24%) | 0 |
| sim2sim from standing | 5/5, + pushes & 40 ms delay 25/25, hands 2.0–4.5 cm | 5/5, 25/25 |

- The timing number is the term the search optimizes, so it shows the mechanism works, not that it looks natural (step 5 decides)
- Pauses: Kokoro replies barely pause (0.3–1.3 s each), so the pause effect can't be judged here; long pauses are step 4 (idle)
- Lower-body rule: **foot lock** (feet fixed, trunk keeps its sway and lean) replaces the plan's "whole body vs fixed legs" choice; a rigid-trunk version wasn't built
- **Watched by Boston (informal, not blind; step 5 does it properly):** matched clearly better than random on all 5 pairs
  - Matched: "looks very natural" (11-52-04 turn 2), "pretty natural" (joke, but "could have gestured harder on the punch line"), natural "solely based on the way it spoke, not the words" (outfit explanation; could have pointed at parts of its body), "kept its hands in front and moved slightly on the beats" (16-44-29 turn 3), "really liked" 16-57-05 turn 8 ("big movements at the beginning, smaller at the end")
  - Random: "very bad, gestures make no sense, isolated from the audio", "didn't really gesture, just stood there swinging its arms", "just stood there and twitched"; two "not glaringly bad but clearly not great"
  - Nothing glaringly wrong against the rhythm and sound of the speech. **Missing: context**: gestures that follow the words (pointing, self-reference, emphasis on the important part)
  - Concern raised: context matching must not over-gesture or illustrate every word

## 2026-11-11: gesture step 4 (idle, whole conversations, 2- and 10-minute runs)

**Built**
- `uv run gesture conversation --sessions speech/runs/<s1> [<s2> ...] [--max-minutes 10] [--speaker 9_miranda]` -> `logs/gesture/conversations/<name>/`: a speech-loop session replayed on its real timeline (`timing.json`: listen = `input_audio_seconds`, wait = `playback_start` − `endpoint`, then the reply) as one query. Idle while listening/waiting, matched gestures while speaking; one search, one stitch, one foot lock for the whole conversation. Audio track: the user's voice while the robot listens, the reply while it speaks
- Idle units: mean hand speed < 0.10 m/s and never > 0.25 m/s (1,806 units, 53 min in library v0), ~2 s idle segments, calmer preferred plus randomness for variety
- **Persona:** conversations default to one speaker (`9_miranda`: least trunk twist, most calm units)
- Library: per-frame `twist` and `trunk_over_feet`; units whose trunk goes > 8 cm sideways (over one leg) are skipped when the feet are locked
- `sim2sim`: max trunk drift, foot slip and heading error per run, and `--trace <npz>` (positions over time)
- `gesture check`: hand speed while idle; test for conversation segmentation (idle and speech never mixed in a segment)

**Problems found and fixed**
- Idle units looped (10 distinct units for 44 idle segments): the search fixed one repeat per pass, 10 passes. Now forbids all too-early repeats each pass until none are left; rule = no unit back within 60 s
- Mixing speakers broke the foot lock (299 frames unreachable, feet jumped): stances differ (Lawrence twists ~2x Miranda) -> persona
- 10-min Miranda run: foot lock failed on 3,246 frames (worst 78 cm) and Gate 1 found the feet colliding. Not twist or side shift: one unreachable moment and then a **cascade** (every later frame started from the stuck legs; left leg unsolved for 106 s). Fix: retry from fresh starts (that frame's own legs, last good pose) before holding -> 65 frames, all in two units of one clip with the trunk 12 cm over one leg -> side-shift filter -> 0
- Note for later: the reference's stance-direction estimate (line between the feet) differs from the trunk by up to 47°; the feet's own headings agree better (p95 22° vs 36°). Not needed now

**Results** (`gesture conversation`, `render`, `check`; policy `y1r48dhc`)

| | 2.4 min (1 session, 7 replies) | 10.1 min (5 sessions, 49 replies) |
|---|---|---|
| Build | 21 s | ~60 s (search 0.4 s, foot lock 9 s) |
| Gate 1 | clean | clean |
| Falls: plain + 3 runs with pushes and 40 ms delay | 0/4 | 0/4 |
| Max trunk drift, plain / pushes | 6.3 / 7.2 cm | 8.0 / 17.2 cm |
| Max heading error | 6.4° | 7.8° |
| Hand speed idle / talking | 0.05 / 0.36 m/s | 0.06 / 0.34 m/s |
| Strong accents hit (chance) | 50% (14%) | 56% (14%) |

- Drift trace (`conv_10min/drift.png`, previous mixed-speaker version): heading wanders ±6° but doesn't accumulate (the policy sees its orientation); **position creeps** with no steps (trunk 1.0 / 3.4 / 4.5 cm at 2 / 5 / 10 min), with pushes one real step (~5 cm) then ~1 cm/min. The policy can't sense its position, so nothing pulls it back. Fine for 10-min conversations; watch on the robot; **final tracker run: consider a foot-slip penalty** (feet moving while in contact)
- Step 4 exit met: 2-min run with no fall and drift < 10 cm; 10-min run done, no fall. Stitched-clip training is **not** needed for falls; for drift, see above
- Video to watch: `logs/gesture/conversations/conv_2026-11-10_18-19-53_2min/sim_audio.mp4` (user's voice while it listens). The 10-min run has no video (render takes long)

## 2026-11-11: streaming-session video + audio levels

- `gesture conversation --sessions speech/runs/2026-11-11_16-57-05` (the streaming session, 17 turns, 2.6 min): video `logs/gesture/conversations/conv_2026-11-11_16-57-05_streaming/sim_audio.mp4`. No fall, drift 5.8 cm, heading within 7°, idle 0.06 / talking 0.32 m/s
- Turns without a reply (13–14, the glitch) used to be dropped with the user's words; now they play as listening
- **Audio levels:** the laptop mic recorded the user at −10 dBFS speech level (peaks at 0 dBFS in most turns: likely clipping) vs Kokoro −23 dBFS, so the user sounded ~4x louder. `audio.match_level` brings each voice block to −20 dBFS (active speech only, peak guard 0.95); conversation videos now match (both −20.0). Test added
- **Watched by Boston:** transitions between listening and speaking "really well", no issues; stays fairly still on some replies and more expressive on others. What feels least natural is **speech-side**: streaming timing, the voice, the LLM's replies. Context (LLM tags) will help gestures. Wants **context-dependent listening reactions** (nods, surprise): design in `gesture_plan.md` step 7
- Speech-loop to-do: lower the mic input gain (Settings → Sound → Input: volume) so it stops clipping; check whether clipping hurts STT

## 2026-11-11: gesture step 6 (speech loop -> K1 motion per reply)

**Built**
- `uv run gesture serve` (`gesture/serve.py`): local HTTP service (127.0.0.1:8765), library loaded once (2.9 s), warm-up reply at start (ready in ~8 s), persona `9_miranda`. `POST /reply {"turn": <path>}` -> `<turn>/gesture/` (reference.npz, plan.json, pkl, reply.wav, query.npz, `serve.json` with timings); `GET /health`
- Speech loop: `speech/src/speech/gesture.py` (`GestureClient`, stdlib only): posts each finished turn from a background thread after playback ends, never blocks; one warning if the service isn't running. Hooked into `Pipeline.run_turn` (streaming and batch paths); test-set runs wait for pending requests. `[gesture]` in `speech/config.toml` (on by default)
- `uv run gesture replay --session speech/runs/<session> [--no-video]`: conversation + render + check in one command
- `generate`'s `plan.json` times every stage: features, search, stitch, foot lock, ground (runtime path) + qc, convert (offline extras)
- Docs: `speech/README.md` (two-terminal setup)

**Fixed on the way (speech side)**
- Groq refused every `qwen/qwen3.8-27b` request: no `max_tokens`, so Groq assumed a 1,272-token reply, over the free tier's 1,000 output tokens per minute. `llm.py` passes `max_tokens` if set; `config.toml` `max_tokens = 400` (replies ~40 tokens, room for thinking). Checked on 2 test-set items: both answered
- The service's log was empty when redirected to a file (Python buffers output that isn't a terminal) -> line buffering in `serve`

**Results** (test-set replay of 2 items through the real speech loop + service)
- Both turns got motion (Gate 1 ok). 6.3 s reply -> motion 0.86 s after posting; 4.0 s -> 0.59 s
- Per stage (6.3 s / 4.0 s reply): features 26 / 13 ms, search 7 / 4, stitch 6 / 2 (**choosing: 20–40 ms**, under the 100 ms target), foot lock 114 / 76, **ground 240 / 153** (largest runtime stage; mostly redundant after foot lock: feet already planted and level), qc 212 / 165, convert 118 / 73 (offline only)
- Not done yet: a live laptop conversation with the service running (needs Boston). Motion is made after each reply is spoken (offline); playing it live and before its audio is the streaming step

## 2026-11-11: first standard live test (step 6 exit)

- `tools/live_test.sh` (service + speech loop + video) with the standard script `notes/live_test_script.md`; session `speech/runs/2026-11-11_21-34-08`, video `logs/gesture/conversations/conv_2026-11-11_21-34-08/sim_audio.mp4`
- **All 10 turns got motion** while talking (service log `logs/gesture_serve_2026-11-11_21-33-15.txt`); motion ready 0.60 s median / 0.92 s max after each reply was posted (runtime path 278 ms median); Gate 1 clean
- Speech: response (end of user speech -> robot audio) **1.47 s median / 2.08 s max**; line 4's mid-sentence pause not cut off; all 10 lines transcribed correctly; joke has a setup and punch line; replies short and on topic (qwen3.8-27b with `max_tokens = 400`)
- Conversation check: 53 segments, strong accents hit 59% (chance 15%), hands idle 0.08 / talking 0.34 m/s
- **Boston:** "Gesturing is doing really good and looks natural." Context (LLM tags) will still help. Happy with how it's coming together
- **Step 6 exit met** (live conversation, every turn writes a reference, replay video in sync)

## 2026-11-11: gesture step 7 (streaming): the K1 gestures live, motion before its audio

**Built**
- `uv run gesture live` (`gesture/live.py`): one process with three threads. Control loop: policy `y1r48dhc` in plain MuJoCo (`sim2sim`'s robot) in real time, one reference frame per 20 ms, shown in a MuJoCo window. Planner: keeps 3 s of idle planned ahead and turns speech events into motion. HTTP server on the offline service's address (127.0.0.1:8765), answers at once
- `gesture/stream.py`, `MotionStream`: the session timeline of 50 Hz frames (joint positions, velocities, trunk orientation: all the policy sees). A plan (a few units) replaces the timeline from its first frame: stitched at 50 fps from the source clips, crossfaded with what was there, foot-locked, published. Viterbi with the unit playing at the splice fixed; no unit back within 60 s across the session
- Speech loop: `streaming.stream_reply(on_event=...)` reports `begin` (first words exist), `piece` (voiced; audio, word times, when it will play = end of the previous piece or now, + output latency), `end` (when each piece really played). `speech/gesture.py` posts them from a background thread; `/health` says whether the live or the offline service is running, no config change
- `--replay-session speech/runs/<session>`: re-sends a recorded session's events with their recorded timing (no mic needed; `--replay-audio` plays the replies, `--no-viewer --push --obs-delay-steps 2` for checks). Each run: `logs/gesture/live/<time>/` (`pieces.jsonl`, `summary.json`, `timeline.npz`)
- `tools/live_test.sh` now starts `gesture live` (`--offline` = step 6's `gesture serve`) and prints the live timing summary. Tests: `tests/test_gesture_stream.py` (4)

**Decisions and problems (in order)**
- **Stance fixed for the session**, not per reply: each foot's median place in the stance frame over 300 of the persona's units (feet 17.9 cm apart), fixed height, level soles. **`ground_clip` dropped** (feet move 0.002 mm, lowest foot point 0.00 mm)
- Stance smoothing is a **trailing** 0.8 s average (step 3's was centered, which needs 0.4 s of future): replacing the timeline from frame f never changes what was sent before f
- First spoken unit: knee at 0.03 rad, feet missed by 1.3 cm on 19 frames, legs held, then an 11.7 rad/s jump. The unit stood narrower with straight knees, so from its own trunk height the session's wider stance is out of reach -> trunk height adjusted per frame so neither leg is longer than in the unit's own pose -> 0 unreachable frames
- Planning took 140-190 ms per piece (foot lock ~0.7 ms per frame), so plans could only change the timeline from now + 0.25 s -> foot lock + publish in 0.5 s chunks: first frames out in 30-50 ms, **margin 0.1 s**
- **First piece** (plays the moment it is voiced): pre-start gesture at `begin`, chosen without audio (units ~0.3 sd livelier than their take's mean). A first version waited for the estimated play time and started 0.05 s *after* the audio (Kokoro is faster than the estimate: ~0.25 s per second of speech) -> starts at once
- MuJoCo window crashed at start under Wayland (GLib: settings key 'antialiasing') -> `PYGLFW_LIBRARY_VARIANT=x11`, set in `live`
- Speech features per piece: loudness / onsets z-scored with running statistics of the session's voice (`RunningFeatures`); the session's very first piece is scored on itself

**Results** (session `2026-11-11_21-34-08` re-sent with its recorded timing: 10 replies, 21 pieces, 82 s; pushes + 40 ms delay)

| | |
|---|---|
| Falls | 0; max drift 4.5 cm |
| Control loop late | p99 0.0 ms, max 0.7 ms; 0 frames without a reference, 0 plans too late |
| Pieces after the first: motion ready before its audio | **1.22 s median**, min 0.35 s (2 of 11 under 0.44 s: a short first piece leaves little time); all started on time (within 0.04 s) |
| First piece: matched motion | starts 0.09 s after its audio (0.53 s later than ideal) |
| First piece: pre-start gesture | begins **0.43 s median before the audio** (0.25-0.62 s) |
| Planning per piece | ~100 ms median, 175 ms max |

- Real `stream_reply` + real Kokoro + a silent stand-in for the speaker (4 replies): all pieces got motion, pre-start 0.44-0.90 s before the audio
- **Not tested yet:** the standard live test with the microphone (needs Boston): how it looks, and whether response time stays <= 1.47 s median with the sim running next to Kokoro. Step 7's exit criteria wait on that
- Not built: barge-in cancel; a video of the live motion itself (`live_test.sh`'s video is made again offline, so its gestures differ); priming the voice statistics from an earlier session
- Laptop: `nvidia-smi` failed tonight (no driver; see CLAUDE.md gotchas). `gesture live` doesn't need the GPU

## 2026-11-11: second standard live test, with live gestures (step 7 exit)

- `tools/live_test.sh` (now `gesture live`): session `speech/runs/2026-11-11_22-12-58`, live log `logs/gesture_live_2026-11-11_22-12-43.txt`, run `logs/gesture/live/2026-11-11_22-12-50/`
- **Motion:** all 10 replies / 20 pieces got motion live; 0 falls, drift 4.3 cm; 0 plans too late, 0 frames without a reference, foot lock never unreachable; control loop max 12 ms late (p99 0)
- Pieces after the first: motion ready **1.33 s median before its audio, min 0.71 s** (0 of 10 under 0.44 s). First pieces: matched motion 0.04-0.08 s after the audio; **pre-start gesture 0.67 s median before the audio** (min 0.46)
- **Boston:** "did pretty well in the moment", nothing glaring (attention was on reading the script, so not a close look)
- **Response 1.59 s median / 2.16 s max** (first live test 1.47 / 2.08): Kokoro voiced 0.36 s per second of speech vs 0.25 in the first test, so the first piece took 0.70 s vs 0.52 (a faster LLM, 0.22 vs 0.34 s, made up part of it). All 10 lines transcribed right; line 4's pause not cut off; no gaps
- Cause found: **onnxruntime's default thread pool spun at ~350% CPU** for a 0.07 ms network (`gesture live` idle: 190%). `TrackingPolicy` now uses 1 thread, no spinning: 0.11 ms per step, `gesture live` 7% CPU headless / 24% with the window. Bench (Kokoro, 15 lines): alone 0.20 s per s of speech; with `gesture live` + window 0.23 before and 0.22 after the fix. The bench didn't reproduce the live test's +43%, so part of it was likely the laptop's state (GPU with no driver tonight runs at full power and heats the machine; see CLAUDE.md). Same fix matters on the robot's CPU (check `booster_deploy`'s own onnxruntime session)
- Re-sent the session with pushes + 40 ms delay after the fix: 0 falls, motion 1.31 s median before its audio
- **Step 7 exit:** met except response time (+0.12 s); re-check on the next live test with the fix. What you see live isn't recorded (the after-video is generated again offline), which is why the live look was only a glance

## 2026-11-11: filming live runs (`gesture live-video`)

- Screen recording rejected: GNOME's recorder has no sound on Wayland and would take CPU from Kokoro
- `uv run gesture live-video --run logs/gesture/live/<time>` (`gesture/live_video.py`): runs the tracker again on the frames the live run read (`timeline.npz`: plans only replace frames after "now", so these are exactly what it tracked), renders 960x720 at 50 fps, and dubs both voices at their real times on the shared monotonic clock (reply pieces at their measured play times from `pieces.jsonl`, the user's `input.wav` ending at the turn's endpoint; both brought to -20 dBFS). The control step is now one `Tracker` class used by `live` and `live-video`
- Exactness: a 27 s replay with pushes + 40 ms delay re-ran to the identical final state (difference 0.0). `live` now saves `t0_monotonic`, `steps`, `final_qpos`; for the earlier run (no `t0`) it is recovered from the first speaking frame of each reply (10/10 agree exactly). That run used multi-threaded onnxruntime, so its film may differ from what was on screen by rounding
- Cost: ~1 min per 90 s of conversation. `tools/live_test.sh` now films the live run after Ctrl-C (instead of the offline replay; `--offline` keeps step 6's video)
- Film of the second live test: `logs/gesture/live/2026-11-11_22-12-50/live.mp4`

## 2026-11-11: robot session prep (sim to real ready for 2026-11-12)

- **Demo clips, sim2sim from standing, 10 runs each with pushes + 40 ms delay:** 40/40 no fall (`ayana_0_9_9_t52-69` hands 3.1 cm, `ayana_0_15_15_t75-95` 2.4, `yingqing_0_9_9_t48-59` 2.7, `ayana_0_11_11_t8-23` 2.2). The top pick's push check (open since 11-08) is done
- **Robot code's own simulator** (`booster_deploy` `render_video.py`, Booster's `K1_22dof.xml`; needed `booster_assets`, cloned to `~/projects/booster_assets`, installed editable): all 4 clips play with no safety stop. Videos `logs/videos/bd_*.mp4`
- **onnxruntime fix in `booster_deploy`** (`policy_runner.py`, one thread, no spinning), the same 350% CPU problem as `TrackingPolicy`, here on the robot's own computer
- **`booster_deploy/scripts/fake_robot.py`:** runs `deploy.py`'s real-robot path against a simulated K1 (stand-ins for `rclpy` and `booster_interface`; booster_mjlab's training K1 answers `/low_state`, `joint_ctrl` in Custom mode over a localhost socket, mode RPCs). Rehearsed: dry run (50 Hz, 0 commands, no mode change, `check_dry_run.py` "no problems found"); swapped shoulder-roll motors (flagged, 1.17 rad); full X -> A -> clip -> Ctrl-C on the floor (Custom, 1 priming + 500 ramp + 1,243 policy commands, Damping at the end, no fall, max tilt 6°)
- Booster's `K1_22dof.xml` **tips forward within 2 s at the stiff prepare gains without the policy**; booster_mjlab's K1 stands (< 1°). The fake robot uses booster_mjlab's model. On the floor: press A soon after X
- **`booster_deploy/scripts/sync_to_robot.sh`:** `--check` (environments with onnxruntime + torch, ROS setup, speakers, mics, disk) and copy to `~/booster_deploy_gesture` (33 MB; leaves the club's checkout alone); tested into a local folder, and the fake-robot dry run passes from the copy. Robot not reachable tonight (off campus)
- **Demo clip `demo_intro`:** a self-introduction voiced by Kokoro (`speech/runs/_demo/turn_01`), gestures from `gesture generate` (persona Miranda): sim2sim 10/10 with pushes + delay, hands 1.9 cm; exported with its audio (0.44 s silence first: the motion leads the voice); plays in the robot code's simulator and on the fake robot with `--audio`. Video `logs/gesture/replies/demo_intro/sim_audio.mp4`
- **Session card: `notes/archive/robot_session_2026-11-12.md`** (what runs where, rehearsal, the steps with commands and stop rules, measurements, questions for the lead, troubleshooting)
- `booster_deploy` commit `e72b603` on its local `gesture-tracking` branch (not pushed: club repo)

## 2026-11-11: speech: cloud TTS engines + blind voice test (Kokoro vs Orpheus vs ElevenLabs vs Cartesia)

Goal: a less robotic voice without slower responses (now 1.5-1.6 s, Kokoro `bm_daniel` CPU 0.5-0.7 s for the first piece live).

### Setup
- `speech/src/speech/tts.py`: one interface, 4 engines (`[tts] engine` in `speech/config.toml`): `kokoro`, `orpheus` (Groq, same key), `elevenlabs`, `cartesia`. All 24 kHz + word times; a failed / rate-limited cloud call voices that piece with Kokoro (`fallback = "kokoro"`, `"engine"` in tts.json). Streaming pieces and `gesture live` unchanged (same `synthesize` output)
- Keys `ELEVENLABS_API_KEY`, `CARTESIA_API_KEY` added to `speech/.env` (gitignored; pasted in chat, rotate later)
- Kokoro on GPU not possible: dGPU off the PCI bus again (`nvidia-smi` fails, not in `lspci`)
- Orpheus gives no word times (the gesture generator cuts at word starts): `estimate_word_times` spreads words over the voiced audio by syllables (+1 before punctuation). Vs Kokoro's real times on 60 live pieces (`speech/bench/word_times.py`): **55 ms median / 160 ms p90** start error (even spread 159 / 350)

### Results
- `uv run python bench/tts_compare.py` (first piece of 12 live replies; `runs/_bench/tts_compare.json`):

| Engine | First piece median / p90 | First bytes | Word times |
|---|---|---|---|
| Kokoro `bm_daniel` (CPU, idle) | 0.36 / 0.46 s (live 0.65) | n/a | real |
| Groq Orpheus `daniel` | 0.35 / 0.47 s | 0.17 s | estimated |
| ElevenLabs Flash v2.5 (George) | **0.20 / 0.29 s** | 0.20 s | real (letters) |
| Cartesia Sonic 3.6 (Archie) | 0.23 / 0.39 s | 0.14 s | real |

- **Blind listening test** (`--listen-only`, 3 live replies, level-matched): **Boston: Cartesia and Orpheus "by far the best, both sound very human"; Kokoro and ElevenLabs Flash "very robotic".** Little difference between the two; choice = which voice he likes
- **Orpheus free tier = 10 requests/min** (429 message), plus 100/day, 1,200 characters/min (headers count characters). A live reply is ~3 pieces = 1 request each, so ~3 turns/min would hit it. Cartesia free: 20k characters/month (~250 turns). No student plans found (Groq, Cartesia); ElevenLabs has an AI Student Pack (not pursued). Groq pay-as-you-go Orpheus $22 / M characters (~$0.02 per 10-turn conversation); Cartesia Pro $5/month for 100k
- `uv run python -m speech.voices --engine orpheus | cartesia [--list]`: voice sampler for the cloud engines; samples (Orpheus 6 voices, Cartesia 8 shortlisted) cached in `speech/runs/_voices/`, replay costs no requests
- Live test (`tools/live_test.sh`) not run: voice not chosen yet

### Takeaways
- Cloud whole-piece time is close to idle Kokoro; the live gain comes from Kokoro slowing under load (0.65 s) and from the voice itself. Playing from the first bytes would save another ~0.1 s (not built)
- Recommendation: Orpheus as the free main voice with 2 pieces per reply (first piece + the rest) to stay under 10 requests/min; Cartesia for demos (faster, real word times)

## 2026-11-12: speech: qwen cut replies short → gpt-oss-120b; Orpheus free-tier limits

Live test (`speech/runs/2026-11-12_14-51-16`, 10 turns in 80 s, Orpheus `troy`) sounded off: the last reply was "Sounds good. Talk to", then `[tts] orpheus failed (rate limited for 6 s ... RPM Limit 10, Used 10)` and the rest played in Kokoro's voice.

### Problems & fixes
- **The cut-off came from the LLM, not TTS**: `reply.json` already says "Sounds good. Talk to" (6 tokens, `finish_reason` stop). Same session: turns 7–8 lost their final "?" / ".", turn 1 "thank you you". Re-sending turns 7–10 to `qwen/qwen3.8-27b` 3× each: **9/12 cut off**; `reasoning_effort = "none"` 8/12; with the cut-off assistant replies in the history repaired (period added) 7/12 (5/12 with effort none, first token 2.3 s) and garbled text ("pretty strong strength that powerful muscles strong")
- Groq models on this key: only qwen3.8-27b, gpt-oss-20b / -120b (no llama). gpt-oss on turns 8–10 4× each: **0/12 cut off** for both; 120b first token 0.40 s, 20b 0.26 s but writes dashes against the prompt
- **LLM → `openai/gpt-oss-120b`, `reasoning_effort = "low"`** (`speech/config.toml`). All 90 recorded turns (6 sessions, 2026-11-11/12) re-sent through `ChatModel`: **0/90 cut off, 11 words median (max 25), first token 0.35 s median** (max 2.15; qwen ~0.26)
- gpt-oss writes em dashes ("Got it—just a chat"), non-breaking hyphens and curly quotes: `speakable()` in `speech/src/speech/llm.py` turns dashes into commas (word timing splits "it—just" correctly) on every streamed piece
- **Orpheus free tier is the "credits" limit**: 10 requests/min and 100/day (headers: `x-ratelimit-limit-requests 100`, 80 left after this test). This session made ~20 requests (2 pieces per reply + warm-up) in 80 s. When limited, the remaining pieces switch to Kokoro's British voice mid-reply. Options: Groq Dev tier (pay-as-you-go, $22 / M characters), Cartesia main, Kokoro for testing / Orpheus for demos, or 1 request per reply (+~0.25 s; Orpheus synthesis ≈ 0.29 s + ~0.04 s/word). **Decision: leave as is for now**

### Takeaways
- Check `reply.json` before blaming TTS: it holds exactly what the LLM said
- The bot has no name in the system prompt: gpt-oss calls itself "ChatGPT" / "RoboChat"

## 2026-11-12: robot session: gesture tracker on the real K1 (floor)

First session on the real robot (card: `notes/archive/robot_session_2026-11-12.md`). Policy `y1r48dhc`
(`Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation`), task `k1_gesture_tracking` in `~/projects/booster_deploy`.
Laptop work, analysis and the logging change were done with Claude over SSH; the runs were done by Boston at the robot.

### Setup
- **Robot computer:** hostname `robot`, Jetson Orin NX, Ubuntu 22.04.5, aarch64. User `booster`; **password in
  `secrets/k1_access.md` (gitignored: this repo is public)**. Laptop shortcuts in `~/.ssh/config`: `ssh k1`, `ssh k1-cable`
- **Cable:** robot port `enP9p1s0` = `192.168.10.102` (Booster's default). Laptop USB-C Ethernet set to static
  `192.168.10.10/24`, no gateway (`nmcli con mod "Wired connection 1" ipv4.method manual ipv4.addresses 192.168.10.10/24 ipv4.gateway ""`).
  Before that the laptop had no IPv4 on the cable; `ping -6 ff02::1%eth0` found the robot by its IPv6 link-local address
- **Wi-Fi:** IllinoisNet, robot at **`10.193.195.162`** (DHCP, may change; `hostname -I` over the cable), reachable from
  the laptop on IllinoisNet (ping 22–102 ms), robot has internet (chrony synced)
- **Robot clock was 6 days behind** (Fri Nov 6 10:26): no RTC battery (RTC reads 1970); `fake-hwclock` +
  `fix-clock-after-rtc.service` restore the last saved time at boot, `chrony` only fixes it once online. Set by hand
  from the laptop: `sudo date -s @$(date +%s)` (laptop's epoch), then `sudo fake-hwclock save`
- `scripts/sync_to_robot.sh --check`: ROS setup `/opt/booster/BoosterRos2Interface/install/setup.bash`; **system
  python3 OK** (onnxruntime 1.22.0, torch 2.7.0; no venv needed), also `~/booster_deploy/.venv` OK; 364 GB free.
  `scripts/sync_to_robot.sh` copied 34 MB to `~/booster_deploy_gesture`. `pytest tests/test_gesture_tracking.py`: 2 passed

### Runs
- **Dry run 1** (`--dry-run`, 18:45:59): `check_dry_run.py` → 3 CHECKs, all from the robot **sitting** (hip pitch −1.99,
  knees 0.0, trunk tilt 21°, nothing moving), not from a bug. Loop 20.0 ms median, `/low_state` 491 Hz
- **Dry run 2** (18:47:43, robot standing under Booster's controller): all ok (tilt 1.8°, inside limits) except the
  first-target CHECK: knees 0.47–0.56 rad, right elbow yaw 0.35 (limit 0.3). Booster stands straight-legged (hips 0.00,
  knees 0.11), the policy's home is a crouch (hips −0.4, knees 0.8); a real run ramps to home with X first. Left/right
  pairs symmetric (shoulder roll −1.46 / +1.45, elbow yaw −0.51 / +0.50): no joint order or sign problem visible
- **Skipped** (Boston's call, time): Step 6 arm sign check, Steps 7–8 gantry. Straight to the floor
- **Floor, 4 runs, no falls**, spotter's hand close but not holding; robot stood on its own:

  | Time | Clip | Exit | Notes |
  |---|---|---|---|
  | 18:52 | `demo_intro` `--audio` | Damping (old default) | no sound (below) |
  | 18:57 | `ayana_0_9_9_t52-69` | Walking | not filmed |
  | 19:00 | `ayana_0_11_11_t8-23` `--audio` | Walking | filmed `IMG_6338`; no sound |
  | 19:00:45 | `demo_intro` `--audio` | Walking | filmed `IMG_6339`; no sound |

  Every run: policy 50.0 Hz (max step 26–31 ms), `/low_state` 487–496 Hz, Walking ~0.5 s after Ctrl-C.
  Boston: "the movements aren't very dynamic" (BEAT2 gestures are small; Ayana 11_11 is the calmest pick on purpose)
- Command: `python3 scripts/deploy.py --task k1_gesture_tracking --motion $M/<clip>.npz [--audio $M/<clip>.wav]`, `x`, then `r`

### Audio
- **Speaker:** C-Media USB adapter = ALSA card 0, `PCM` 37/37 (100%). `/etc/asound.conf` makes `aplay`'s default the
  Jetson's internal `APE` (no speaker), so `--audio` was silent. `aplay -D plughw:0,0 demo_intro.wav` played,
  **very loud**. Lower it first next time: `amixer -c 0 set PCM 60%`
- **Mic: iFlytek XFM-DP-V0.0.18** (USB, high speed, port `1-2.2.1`, ALSA **card 1**; PulseAudio source mono 16 kHz).
  It **dropped off USB** at 18:42:32 (back after 1 s with `buffer overrun`) and again at **18:44:15 for good**, between the
  dry runs while the robot was being moved: card 1 vanished, PulseAudio recorded pure zeros, `APE` capture hung.
  **A reboot brought it back.** Loose cable or power dip, unknown
- Quiet recording after the reboot (`arecord -D plughw:1,0 -d 15 -f S16_LE -r 16000 -c 1 ~/mic_quiet.wav`, nobody
  near, someone talking ~5 m away): mean −65 dBFS, loudest 0.1 s −48.5, quietest −94, **14% exact-zero samples** (the
  board likely gates silence itself), no clipping. Not tested: voice at 1 m, motors running, echo of its own speaker
- Booster's `booster-audio` logs `perception file parse error: missing or invalid Audio field` (falls back to
  PulseAudio) and `boosteraec_playback not found`. `booster-rtc-speech` (their voice assistant) is running
- Files on the laptop: `logs/robot_session_2026-11-12/` (`mic_quiet.wav`, both dry-run logs)

### Robot facts for the onboard work
- **Network interfaces:** `enP9p1s0` = `192.168.10.102` (the cable port), `enP8p1s0` = `192.168.13.101`,
  `usb_eth0` = `192.168.127.101` (internal; one of these is the DDS interface the Booster SDK's
  `ChannelFactory.Init(0, <net if>)` needs: check which `booster_deploy` / ROS use), `wlP1p1s0` = Wi-Fi.
  Saved Wi-Fi besides IllinoisNet: `SigRobotics_5G` (out of range in the lab)
- **Booster audio stack:** `booster-audio` (`/opt/booster/BoosterAudio/bin/`) publishes mic audio on its own channels
  `/booster/audio/capture/slot_1..8`, ships a wake-word + direction-of-arrival library (`libduerwen_wakeup_DOA*.so`), and
  its script `ensure-booster-alsa-config` **manages `/etc/asound.conf`** (and `/etc/alsa/conf.d/99-booster-audio.conf`):
  pick devices by name in our code, don't hand-edit those files. `/opt/booster/perception_info.yaml` lists only
  `Camera: BoosterMipi`. Other Booster services running: `booster-rtc-speech`, `booster-lui`, `booster-agent-manager`
- **Mic channels:** PulseAudio offers the mic as `mono-fallback` 16 kHz; the SDK docs say its raw stream is 3-channel.
  Only mono was recorded: check `arecord -D hw:1,0 --dump-hw-params` for the real channel count
- **The mic shares an internal USB hub with `/dev/ttyACM0`** (WCH USB serial, `1-2.2.3`, possibly part of the control
  system), so a software USB reset of the mic's port was not tried while the robot was powered
- Robot has Firefox (snap), `xwininfo`, X11 forwarding on; user `booster` is in `sudo` and `audio`

### Videos
- `logs/robot_session_2026-11-12/videos/`: `IMG_6338.MOV` / `IMG_6339.MOV` (iPhone, 4K 60 fps) and **dubbed 1080p**
  `k1_real_ayana_0_11_11_t8-23_dubbed.mp4`, `k1_real_demo_intro_dubbed.mp4` (clip audio in place of room sound)
- Alignment: arm-region frame differences vs the clip's arm joint speed. Ayana: clip start **2.02 s** into the video
  (r 0.62; the phone/robot timestamps said 1.9 s). demo_intro: two peaks (4.80 s r 0.61, 6.26 s r 0.57); the timestamps
  (offset calibrated on Ayana) allow 5.9–7.9 s → **6.26 s**. Run logs now record the clip start time, so next time
  this is exact
- Dubbing command (`D` = clip start in ms):
  `ffmpeg -i IMG.MOV -i <clip>.wav -filter_complex "[0:v]scale=-2:1920,fps=30[v];[1:a]adelay=D:all=1,apad[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 20 -c:a aac -shortest out.mp4`.
  ffmpeg 6.1 ends this with "No space left on device" (exit 228) although the file is complete (`apad` + `-shortest`
  quirk; disk had 88 GB free): check with `ffmpeg -v error -i out.mp4 -f null -`

### Problems & fixes
- **IllinoisNet down:** `EAP-MSCHAPV2: Password expired (error 648)` for the robot's NetID (PEAP; server certificate
  accepted). Fixed by Boston; the robot still logs in with PEAP. Illinois' certificate renewal (JoinNow, SecureW2
  "IllinoisNet-TLS") is due **before 2026-12-18**. Its Linux client (`linux/SecureW2_JoinNow.run`, Python, console UI)
  logs in through Firefox and reads the result from window titles, so it needs `ssh -X` on the robot (has Firefox +
  `xwininfo`, X11 forwarding on). Copied to `~/SecureW2_JoinNow.run` on the robot
- **Ctrl-C went limp** (`exit_mode="damping"`): `k1_gesture_tracking` now exits to **Walking**; a safety stop still damps;
  `--exit-mode damping` on the gantry. Worked on 3 floor runs
- **No run data from real runs** (only dry runs logged): every real run now writes `logs/run_<task>_<time>.npz`
  (`--no-log` to skip): joint state, torques, targets, IMU, wall-clock time, tracked reference frame. Saved in 5 s parts,
  merged at the end; killed runs recoverable. `scripts/check_run.py`: timing, video-sync times, tilt, tracking error
  per body part, torques + ankle chatter, near-limit time. Tested on `fake_robot.py` (50.0 Hz, max step 22 ms; killed
  run recovered; dry run still 0 commands). `booster_deploy` commit `2ed4b62` (local branch), **not yet on the robot**
- Silent `--audio`: device (above); `--audio` doesn't pick card 0 yet
- Wi-Fi SSH timed out once right after a sync, then worked: keep the cable in for floor runs (an SSH drop stops the run)

### Takeaways
- The sim → real path works: same policy, no retraining, stood and gestured on the floor, clean handover to Walking
- Booster's standing pose ≠ the policy's home pose: the dry run's first-target CHECK under Booster's controller is expected
- Mic and speaker exist and work as plain ALSA devices (cards 1 and 0), which the onboard plan needs; the mic's USB link
  is fragile under motion
- Still untested on hardware: arm joint signs (Step 6), ankle gains / chatter (now measurable from run logs), gantry

## 2026-11-13: plan: full conversation onboard the K1 by Thursday 2026-11-19

Plan: **`notes/onboard_plan.md`**.

- **Decision (Boston): deployment goes all in on the robot.** Speech loop, gesture generator and tracker all run on
  the K1, with its own mic array and speaker. The laptop is for SSH, tests and rehearsal only (no frame streaming
  from the laptop, no laptop speaker). My first proposal (generator on the laptop streaming frames over Wi-Fi) was
  dropped
- Layout on the K1: P1 `deploy.py --task k1_gesture_live` (ROS 2, system Python) reads 50 Hz frames from shared
  memory written by P2 `gesture live --robot`; P3 the speech loop posts pieces to P2 over localhost (same clock, as on
  the laptop). Separate processes because of the GIL (planning bursts would stall the 50 Hz loop), Python versions,
  and so a speech crash doesn't stop the body
- **Booster SDK has a full audio service** (`booster_robotics_sdk_python` 1.6.3 on PyPI, aarch64 wheels, example
  `sdk_pybind_audio_example.py`): `AudioCaptureStream` (mic frames by callback: `raw` 16 kHz 3-channel "BoosterAEC" and
  an echo-cancelled `naec` stream, backend-dependent), `AudioPlayer` (PCM stream), `AudioLocalizer.GetDoaAngle()`
  (voice direction), `AiClient.StartAiChat/StopAiChat` (Booster's assistant). Plan: plain ALSA via sounddevice first
  (the loop finds devices by name); the SDK adapter only if the mics aren't in ALSA
- Gesture runtime imports only numpy / scipy / mujoco (portable to the Jetson); the speech venv needs a slim robot
  install (Silero through onnxruntime without torch, no faster-whisper / Kokoro), so **no Kokoro fallback onboard**:
  the cloud TTS must not run out (Groq Dev tier or Cartesia)
- Order: robot runtime + laptop rehearsal with `fake_robot.py` in the robot's exact process layout; in parallel,
  context gestures in sim (emphasis tags, then wave / point_you / point_self); robot time: probe → audio alone →
  canned clip → conversation on the gantry → floor
- K1 manual (Feishu export): wired SSH `booster@192.168.10.102`, Orin NX; datasheets disagree on 8 vs 16 GB

## Next
Current step: **full conversation onboard the K1 by Thursday 2026-11-19: `notes/onboard_plan.md`** (its work list is this week's to-do; decided 2026-11-13: speech loop, gesture generator and tracker all on the robot, its own mics + speaker). First: `gesture live --robot` (frames to shared memory) + `booster_deploy` task `k1_gesture_live`, rehearsed with `fake_robot.py`; `tools/robot_probe.sh` (to write) for the first robot access; then context gestures in sim (emphasis, wave / point). Tracker on the real K1: 4 floor runs 2026-11-12, no falls.

**1. Robot**
- **Next robot access (before anything else):** `cd ~/projects/booster_deploy && ROBOT=booster@10.193.195.162 scripts/sync_to_robot.sh` (run logs + Walking exit, commit `2ed4b62`); `amixer -c 0 set PCM 60%` before any sound; check `cat /proc/asound/cards` shows card 1 (iFlytek mic) after moving the robot
- Follow-ups from 2026-11-12: Step 6 arm sign check (gantry, `--dry-run`); film `ayana_0_9_9_t52-69` (the energetic clip) with a run log → `scripts/check_run.py` (ankle chatter, tracking, real vs reference size); mic at 1 m, motors on, own-speaker echo; `--audio` → card 0 by name (`plughw:CARD=Device,DEV=0`); SDK arms + head while Booster holds the legs; compute module (`free -h`)
- Ask the lead (details in `deploy_audit.md`): mic cable (dropped out under motion); how the firmware applies ankle `kp`/`kd`, firmware version, real joint limits, Ctrl-C exit mode; milestone 1 change + the speech/LLM extension (then update `proposal.md`); battery, Booster's Doubao assistant
- **IllinoisNet certificate renewal (JoinNow) before 2026-12-18** for the robot (`~/SecureW2_JoinNow.run`, run over `ssh -X` as `booster`, not root); credentials in `secrets/k1_access.md`

**2. After Thursday**
- Gesture: barge-in cancel, listening nods, `gesture_plan.md` step 5 (blind viewer test vs random + real mocap); EMAGE comparison optional (step 0, deferred)
- History experiment, club GPU (`git pull` first; same settings as `y1r48dhc` except the task, so the comparison is fair):
  ```
  source ~/bmcox2/.wandb_env; E=bmcox2-university-of-illinois-urbana-champaign
  uv run train Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation-History10 \
    --registry-name $E/motion_upload/beat2-full-torso-train-ab:v0 \
    --env.scene.num-envs 4096 --agent.max-iterations 6000 --agent.seed 42 \
    --agent.run-name history10-nse-train-ab 2>&1 | tee logs/train_history10.txt
  ```
  Then `eval-tracking --task Mjlab-Tracking-Flat-Booster-K1-No-State-Estimation-History10 ...` on `heldout-val:v0` + `val:v1`, `tools/eval_summary.py` vs `y1r48dhc` (193/194, 3.82 cm; val 468/472, 4.57 cm), and `sim2sim` from standing on the 15 held-out clips. Adopt if clearly better; watch iteration time (input 1220 vs 122)

**3. Tracker (criteria 1–7)**
- Data: watch the 3 Solomon val clips that fail in every run (`solomon_0_13_13_t29-40_shift` 10.2 s, `solomon_0_16_16_t19-23_shift` 3.1 s, `solomon_0_12_12_t58-77_shift` ~13.5 s) and `lawrence_0_12_12_t26-38` in `visualize-motions`; drop or fix them in val. Bad clips found later go into `[qc] exclude_clips` in `tools/datasets/beat2_full.toml`, then rerun `beat2_batch.py` (cached up to QC, ~50 min with uploads)
- Arm-joint speed: confirm the shoulder-singularity guess (angle between upper arm and shoulder-pitch axis vs arm-joint speed, failing windows vs controls). If confirmed: a QC flag on arm-joint speed > ~10 rad/s, and a fix in the GMR IK config (penalize shoulder-pitch / elbow-yaw velocity)
- Optional: trim ~0.5 s off Tier A clip ends that stop at a step onset (`beat2_segments.py`)
- After each run: eval the flagged clips (`eval-tracking --clips ...`, 20 rollouts) and review only the ones still failing (harness calibration done 2026-10-21)
- Criterion 2: `eval-tracking --push` on heldout-val; ranges beyond training; observation latency/noise if missing
- Criterion 6: action-rate / jerk metric in `eval-tracking`
- Criterion 5: design transitions (idle hold, clip-to-clip, return to idle); likely stitched training clips with idle stretches
- Milestone checks with `1de2pner`: no regression on the 3 waves + Scott 34–44 s (within 20% of each specialist, 50/50); 5 held-out clips in `play` dubbed with audio
- Final run (after hands-on K1 + ankle model): A+B data **`beat2-full-torso-train-ab:v0`** (`--registry-name`; replaces the hand-combined `logs/motions/beat2-full-torso-train-ab.npz` on the club PC), longer, pick the checkpoint by heldout-val, score `test` / `heldout-test` / `heldout-conv` once

**4. Speech loop on the laptop** (no robot; `speech_plan.md`, numbers in `speech_bench.md`). Steps 1–4 done (2026-11-08 → 2026-11-11): hands-free, streaming, response 1.8 s median. **Paused.** When it resumes:
- Step 5 barge-in (talk over the robot to stop it; PipeWire echo cancel on laptop speakers; needs the K1 mic check for the robot)
- Voice: less robotic (Groq Orpheus is fast but 100 req/day free; ElevenLabs / Cartesia free tiers; GPU Kokoro when the dGPU is back). < 1 s needs first audio ≤ ~0.15 s
- Watch: empty replies (retry logs `retried_empty` in reply.json; seen with qwen, LLM is gpt-oss-120b since 2026-11-12), short replies waiting 0.8 s under the strict end-of-turn rule
- Orpheus free tier (10/min, 100/day) runs out in fast chats; when it matters: Groq Dev tier or Cartesia, and keep one voice per reply (no mid-reply switch to Kokoro)
- Give the bot a name in the system prompt (gpt-oss calls itself "ChatGPT")
- Personality / system prompt; step 6 tool calls; Pipecat spike (optional)

**5. Cleanup**
- Club PC (disk 97% full, shared): `rm logs/motions/beat2-full-torso-train-ab.npz` (7.7 GB, superseded by `train-ab:v0`); `rm -rf artifacts/beat2-full-torso-train-b:v1` (1.5 GB); `wandb artifact cache cleanup 1GB`
- Laptop: `wandb artifact cache cleanup 1GB` (`~/.cache/wandb` ~21 GB). Keep `~/robotics/data/beat2_full_torso` (per-clip cache) until the next rebuild; `~/robotics/data/beat2_full/` can go
- W&B: tag `1de2pner` `keep`, `wbitlbqw` `superseded`; tag the dead runs (`2h7ih3ij`, `kxzph3yx`, `vbsmv80n`, `rm0fhes8`, `jf0opr8t`, `aorrbkep`, `y3k07rwu`, `4vldt40m`) `superseded`; move dataset `current` aliases to the versions in use
- Unexplained: run `y3k07rwu` died at it 244 (log cut at `Exception in thread Thread-1`). Train output is `tee`d to `logs/train_*.txt` now

**6. Data follow-ups (before the v3 rebuild)**
- Gate 2 (not done): histograms per split + watch 20 random + worst clips in `visualize-motions` (step-lift arcs, conversation takes, Tier B). Gate 1 missed the trunk lean; it can miss other things
- ground_clip IK failures: 672 clips (mostly Tier B / conversations) excluded; find why leg IK fails there
- 84 clips with the left arm > 10 cm behind the trunk (GMR IK-start bug signature) despite the HOME-arms seed
- 5–10 cm "arm behind" clips (mostly Sophie's low clasped hands) are now in training as info only: the K1 loses that pose
- v3 GMR config → new `out_dir` + `name` in the spec, rerun. Prefer the club PC (needs GMR + its venv at `~/projects/GMR`); on the laptop use `OMP_NUM_THREADS=1` workers and `tools/laptop_build_governor.sh`
- Build order: training sets first (`--sets train-a train-b`) so runs can start while eval sets build

**7. Older items**
- QC "arms K1" column measures the elbow: switch it to the forearm tip (`*_hand_end_ball`)
- Foot tilt (> 10° on many Lawrence / Solomon clips): check references' foot orientation vs robot; consider a foot-flatness reward
- Clips that fail at t = 0.1–0.2 s in eval (old: `lawrence_0_12_12_t26-36`, `lawrence_0_13_13_t21-31`, `solomon_0_15_15_t43-53`; full BEAT2: `lawrence_0_12_12_t26-38`, `ayana_0_13_13_*`): look at their first frames vs the ±0.1 rad start jitter
- If hands stay well above single-clip: future reference frames in the obs (GMT uses ~2 s) and/or a bigger network
- Why GMR's IK flips the upper-arm twist (`*_Elbow_Pitch`); fixing it would recover the joint-jump clips
- `play` + record videos of me9exatd and pqh0whw0 for the lead
