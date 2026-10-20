# Roadmap: A Conversational, Gesturing K1

Updated 2026-10-20, after the full-BEAT2 tracker. Replaces the 2026-10-16 version (in git),
whose steps 0–1 (Slice 0, general tracker) are now mostly done. `proposal.md` is the approved
plan; the speech/LLM layer below is its planned extension (tell the lead before changing it).

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
| 4. Gesture generator: audio + text → SMPL-X | not started (EMAGE candidate) | GPU |
| 5. Retargeting: SMPL-X → K1 joints | **exists** (GMR + torso IK + `ground_clip`, offline) | must become streaming |
| 6. Tracker policy | **trained in sim** (`1de2pner`) | onboard |
| 7. Locomotion | Booster's controller via SDK | onboard |

- Beat gestures come from the audio (generator); semantic gestures (point, wave) come from LLM
  tags or a named gesture library (the AMASS waves/points are kept for this).

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
| 7 | Checkpoint frozen, config reproducible, eval numbers logged | Winner picked; final run pending (after the hardware questions below) |

## Steps

| # | Step | Done when |
|---|---|---|
| 1 | **Finish the tracker exit criteria** ← *current* (in parallel with 2) | All 7 rows above met in sim |
| 2 | **Speech loop on the laptop, no robot:** STT → LLM → TTS (plan: `speech_plan.md`) | End-to-end latency measured, target < ~1 s |
| 3 | **Gesture generator in sim:** TTS audio → generator → retarget → tracker | Any spoken reply → K1 gesturing in sim, in sync with the audio |
| 4 | **Hardware:** tracker with canned clips, then the live pipeline | Stationary conversational K1 on the real robot |
| 5 | **LLM tool calls:** look_at, wave, point, walk_to | The LLM triggers skills during a conversation |
| 6 | **Mobility + gesture, presenting** | Walks and gestures; gives a short talk |

## Key risks

- **Sim-to-real gap for the tracker.** Where most humanoid projects stall; expect it to take
  longer than everything so far.
- **Latency and sync.** EMAGE generates a whole utterance offline; the < 1 s target needs a
  generator that works in chunks (streaming), or LLM-tagged gestures that start right away
  while beat gestures follow. Gesture motion must stay in sync with TTS playback.
- **Streaming retargeting.** GMR + `ground_clip` run offline on whole clips today.
- **Walking + gesturing at once** is its own research problem (ExBody2).

## Open questions / to-dos

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
