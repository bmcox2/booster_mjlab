# Roadmap: A Conversational, Gesturing K1

**2026-11-13:** step 1 done (4 floor runs 2026-11-12, no falls). **Step 6 (live conversation on the robot) is pulled
forward to Thursday 2026-11-19, all onboard** (speech loop, generator and tracker on the K1, its own mics and
speaker): `onboard_plan.md`. Steps 4 and 5 wait until after it.

Updated 2026-11-10, after a review against 2025–2026 work (`log.md` 2026-11-10, reading list in
`papers.md`): steps re-ordered so the gesture generator comes before more speech work. Previous
version 2026-10-20 (in git). `proposal.md` is the approved plan; the speech/LLM layer below is its
planned extension (tell the lead before changing it).

Priority: a **working system first** (experience, resume); a paper is a bonus. The likely paper
angle is a K1-native streaming generator (outputs K1 joints directly, trained on the ~29 h of
retargeted BEAT2 with audio). Plan without hands.

## Vision

- **First big goal (unchanged):** a stationary K1 that holds a spoken conversation on the real
  robot, gesturing in sync with its own speech.
- **Long term:** an LLM-driven, Jarvis-style companion. The LLM handles the conversation *and*
  calls robot skills beyond gestures (walk to, look at, point, wave).
- Still on the board: tutoring, presenting on a stage, walking while talking. Mobility comes
  after the stationary conversation works.

## Architecture (planned)

Layered; **the LLM never controls joints directly**, it calls skills (the SayCan / Code as
Policies pattern).

```
mic array ─► speech-to-text ─┐
camera ─► person location ───┼─► LLM (conversation + tool calls) ─► TTS audio ─► speaker
                             │        │ tool calls: walk_to, look_at, point_at, wave
                             │        ▼
                             │   gesture generator (TTS audio + text → SMPL-X; e.g. EMAGE)
                             │        ▼
                             │   GMR retarget + ground_clip ─► K1 reference ─► tracker policy ─► joints
                             └─► locomotion: Booster's built-in controller via SDK (at first)
```

| Layer | Status | Where it runs |
|---|---|---|
| 1. Perception: mics → STT; camera → person location | not started | robot / laptop |
| 2. LLM: conversation + skill tool calls | not started | off-robot (cloud API or club GPU over Wi-Fi) |
| 3. TTS: streamed speech audio | not started | off-robot or robot |
| 4. Gesture generator: TTS audio (+ text) → K1 reference | not started. **v0: retrieval** from the K1 BEAT2 clip library; EMAGE only as an offline smoke test (it needs the whole utterance) | club GPU |
| 5. Retargeting: SMPL-X → K1 joints | **exists** (GMR + torso IK + `ground_clip`, offline) | stays offline: builds the library / training data, not in the runtime path |
| 6. Tracker policy | **trained in sim** (`1de2pner`) | onboard |
| 7. Locomotion | Booster's controller via SDK | onboard |

- Beat gestures come from the audio (generator); semantic gestures (point, wave) come from LLM
  tags or a named gesture library (the AMASS waves/points are kept for this).
- **The stable contract is a 50 Hz K1 reference stream** (22 joint positions + velocities, trunk
  orientation; later a root velocity command for walking). Anything may produce it: retrieval, a
  neural generator, the semantic gesture library, a locomotion planner. Version the policy's
  observation layout (hands will change it). SONIC (arXiv 2511.07820) is built this way.
- **Stationary lower body:** the generator supplies arms, head and trunk tilt; the legs follow a
  fixed standing reference. This removes most of what breaks with generated motion (foot
  skating, root height, foot clearance; GenTrack, arXiv 2608.01410). RoboGesture (2608.28693)
  goes further and leaves the legs to the robot's own standing controller.

## Where things stand (2026-10-20)

- **Tracker trained on full BEAT2:** 19 training speakers, ~29 h (Tier A standing + Tier B
  foot shifts). Winner **`1de2pner` `model_5999.pt`** (A+B). On 6 held-out speakers
  (Ayana, Kieks, Li, Nidal, Stewart, Yingqing): **194/194 clips, 0 falls, hands 3.46 cm**.
  Training speakers' unseen takes (val): 466/474 clips, hands 4.43 cm. Details: `log.md` 10-19.
- Lesson that keeps holding: most failures are **bad data** (retarget glitches, impossible
  poses), not RL. The sampling safety harness quarantines such clips during training.
- Slice 0 (one Scott clip, video with audio): done except the sync check and the write-up.
- **Not yet touched the physical K1.** Real-world behavior is the biggest unknown.

## Tracker exit criteria ("done in sim")

Real "done" only after hardware deployment.

| # | Criterion | Status |
|---|---|---|
| 1 | Held-out speakers: zero falls, tracking error close to training | **Essentially met** (194/194, held-out hands below val). Left: fix or drop the 3 Solomon val clips that fail in every run + `lawrence_0_12_12_t26-38` (start-of-clip), final longer run chosen by `heldout-val`, score the `test` sets once |
| 2 | Robust under domain randomization (mass, friction, motor strength, latency, noise, pushes) | Training already randomizes friction, PD gains, body mass/inertia, encoder bias, pushes, actuator delay. Left: eval with `--push` and ranges *beyond* training; add observation latency/noise if missing |
| 3 | Sim2sim: plain MuJoCo at the real control rate, deploy observation pipeline | Not started. **Needs a policy-only ONNX export** (obs → actions, reference streamed in): `K1MotionTrackingRunner` skips mjlab's export for big sets because it bundles the whole dataset |
| 4 | Handles imperfect / generated motion (gate before connecting the generator) | Not started. EMAGE output → GMR → `eval-tracking`; expect jitter, foot sliding, impossible poses |
| 5 | Clean transitions: start, idle hold, clip-to-clip blending, return to idle | Not started; **probably the biggest tracker item left**. In training a finished clip teleports the robot to a new start, so it has never practiced idle → gesture → idle. Likely needs stitched clips with idle stretches |
| 6 | Smooth output, no jitter | Not measured. Add an action-rate / jerk metric to `eval-tracking` |
| 7 | Checkpoint frozen, config reproducible, eval numbers logged | Deployment candidate `y1r48dhc` (No-State-Estimation); final run pending (after rows 8–9 and the hardware questions) |
| 8 | Observation history (added 2026-11-10) | Experiment: actor `history_length` 10 vs `y1r48dhc` on `heldout-val`. A mjlab-based study (arXiv 2607.19903) found no history raised base errors 38–50%. Adopt if it wins; then `deploy/` must stack frames |
| 9 | Continuous operation (added 2026-11-10) | **Met in sim 2026-11-11** (`gesture conversation`, `y1r48dhc`): 10.1-min conversation, no fall (plain + 3 with pushes and 40 ms delay), drift 8 cm plain / 17 cm with pushes, heading within 8°. Position creeps ~0.5–1 cm/min (no position sensing): consider a foot-slip penalty in the final run; measure on the robot |

## Steps (re-ordered 2026-11-10)

| # | Step | Done when |
|---|---|---|
| 1 | **Hardware, canned clips** (**done 2026-11-12**: 4 floor runs, no falls, handover to Walking) | Dry run passes `check_dry_run.py`; one clip on the gantry, then the floor, `/low_state` + `/joint_ctrl` recorded. Also answer: SDK arms + head while Booster's controller holds the legs? K1 mics with motors running; laptop ↔ robot round trip; compute module |
| 2 | **Generated-motion smoke test** (~1 day; **deferred 2026-11-11** to `gesture_plan.md` step 5, as an extra comparison) | EMAGE offline on ~5 TTS replies → GMR → `ground_clip` → `eval-tracking` + `sim2sim`; failure causes listed |
| 3 | **Retrieval generator v0 in sim** (done 2026-11-11, incl. streaming; context gestures next); plan: `gesture_plan.md` | TTS WAV → 50 Hz K1 reference (matched BEAT2 clips, crossfades, idle, fixed legs); a `speech.loop` reply plays as a dubbed `sim2sim` video, synced within ~100 ms on stressed words; 2-minute continuous run, no fall |
| 4 | **Final tracker run** (after 1–3) | Exit criteria rows 1–9 met in sim: history if it wins, idle + stitched clips in training, fixed lower-body option |
| 5 | **Speech loop streaming** (`speech_plan.md` step 4; steps 1–3 done) | First audio < 1 s median on the test set |
| 6 | **Live conversation on the robot** ← *main work now, target 2026-11-19, all onboard* (`onboard_plan.md`) | 5-minute conversation, no fall, no manual restarts |
| 7 | **LLM tool calls:** look_at, wave, point (barge-in once the K1 audio allows it) | The LLM triggers a wave or point at the right word |
| 8 | **Neural generator** (only if retrieval looks repetitive; paper angle), then **mobility + presenting** | Beats retrieval in a blind viewer comparison; walks and gestures |

Deferred: more Tier B / data cleanup beyond known bad clips, a speech framework switch (Pipecat /
LiveKit), barge-in before the K1 mic check.

## Key risks (ranked 2026-11-10)

1. **No hardware contact yet.** Ankle gains, latency and the final run all depend on it.
   Sim-to-real is where most humanoid projects stall.
2. **No live generator.** EMAGE needs the whole utterance. Streaming BEAT2 models exist
   (LiveGesture 2604.10927, GestureFAR 2609.21576, RoboGesture 2608.28693) but no code was found
   for any. Retrieval v0 avoids the dependency and becomes the baseline.
3. **Continuous operation untested** (exit criterion 9): minutes of idle → gesture → idle, drift,
   heading. No listening behaviour (gaze, nods); BEAT2 is mostly talking.
4. **No observation history** in the policy (exit criterion 8).
5. **Latency is mostly speech** (TTS 82% of the wait; RoboGesture reports the same). Cover it
   with the body: an immediate head turn or posture shift when the user stops talking.
6. **Robot audio:** the K1 hears its own voice and motors; barge-in may fail there.
7. **Foot shifts:** not needed with a fixed lower-body reference; keep Tier B in training for
   robustness, stop investing in it.
8. **No wrists or hands:** palm orientation and hand shape are lost. Judge gestures by watching
   them (viewer ratings later); hand error in cm doesn't measure "natural".
- Later: **walking + gesturing at once** is its own research problem (ExBody2); routes are
  Booster's walk controller with arms overridden, a tracker with a velocity command, or a
  whole-body tracker fed by a planner. Not settled in the field.

## Open questions / to-dos

- **Can Booster's SDK command arms + head while its own standing/walking controller runs the
  legs?** If yes, that's a much simpler v1 fallback and the likely first mobility route.
- Network delay from the club GPU (generator, TTS) to the robot.
- **Hands-on time with the K1, before the final tracker run:** which compute variant the club
  has (QCS8550 / Orin NX 8 GB / AGX Orin 32 GB), SDK joint control, how a custom policy
  coexists with Booster's controller. These decide criteria 2, 3 and 7.
- **Ankle model** (standard vs `-Parallel`): decide with the lead before the final run; it
  picks the robot model the final checkpoint trains on.
- Confirm on the club's unit: 6-mic array + torso speaker, ~80 min battery, whether Booster's
  Doubao LLM integration is installed. Hands are being built by the hardware group (none yet).
- Tell the lead: milestone 1 changed to "tracks real conversational motion" (done in sim), and
  the speech/LLM layer is the planned extension. Then update `proposal.md`.
- Reading list: `papers.md` ("Next reading").

## K1 constraints

22 DoF: head 2 (yaw, pitch), each arm 4 (shoulder ×3, elbow), each leg 6. No wrists, no waist,
no hands yet. Gesture expressiveness comes from shoulders, elbows and head gaze.
