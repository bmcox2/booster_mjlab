# Gesture Generator: Plan

Step 3 of `roadmap.md` (step 2, the EMAGE smoke test, is step 0 here). Sim and laptop only, no
robot. Written 2026-11-11. Plan only, no code yet.

**Goal of the stage:** turn any spoken reply (the speech loop's `reply.wav` + `tts.json`) into a
50 Hz K1 reference that the tracker can follow, with gestures that look like they belong to the
speech. v0 is **retrieval**: reuse pieces of real BEAT2 motion, already retargeted to the K1,
chosen to match the reply's audio. No neural network is trained in this stage.

## Why retrieval first

- **No generated-motion gap.** Every frame comes from clips the tracker already passes
  (`train-ab:v0`). A neural generator would produce new poses, and GenTrack (arXiv 2608.01410)
  shows that's where trackers fail: jerk, foot skating, root height.
- **No dependency on code that doesn't exist.** EMAGE can't stream, and the streaming BEAT2
  generators (LiveGesture, GestureFAR, RoboGesture) have no released code.
- **It's the baseline any later model must beat.** If a neural generator (the possible paper
  angle) doesn't look better than retrieval in a blind test, it isn't worth deploying.
- **It streams naturally.** Choosing the next piece only needs the audio ahead of it, so moving
  from "whole reply" to "sentence by sentence" later is a small change.
- The idea is old and proven in animation: *motion graphs* (Kovar et al., SIGGRAPH 2002) and
  *motion matching* (Clavet, GDC 2016; used in games) both stitch real motion pieces together by
  searching a database.

## How it works (one reply)

```
reply.wav + tts.json ─► [audio features, 50 Hz] ─► [split into units] ─► [search library:     ─► [stitch: crossfade, ─► [ground_clip: ─► reference.npz ─► sim2sim / robot
  (speech loop)          energy, onsets, pauses     ~0.5–3 s each        audio match + smooth   yaw align, idle      replant feet,    (+ reply.wav)
                                                                         transitions (DP)]      at start/end]        FK → npz]
library (built once): every Tier A training clip → its audio span + the same features + motion features, cut into units
```

- **Unit:** a short piece of motion, ideally one gesture: preparation → stroke → hold →
  retraction (McNeill's gesture phases, *Hand and Mind*, 1992). Cut library clips where the hands
  are slowest, which is usually between gestures.
- **Matching:** for each piece of the reply's audio, find library units whose *own* audio looks
  similar (loud vs quiet, many vs few syllable onsets, pause vs speech). People gesture more, and
  faster, when they speak with more emphasis; that's what the match exploits.
- **Smooth transitions:** the search also scores how far the end of one unit is from the start of
  the next (joint angles, hand positions, foot placement). Picking the best sequence of units under
  both scores is a shortest-path problem, solved with dynamic programming (the Viterbi algorithm).
- **Stitching:** crossfade joints over ~0.3 s between units, turn each unit to the previous one's
  heading, then let `ground_clip` replant the feet. Joint velocities are recomputed from the final
  positions.

## Decisions before starting

| Decision | Recommendation | Why |
|---|---|---|
| Library data | **Tier A clips of training speakers** (`train-a`; 7,223 clips, 23 h). Start with a **subset of 3–4 speakers** to iterate fast, then grow | Tier A has planted feet, so the robot stays stationary. Held-out speakers stay out: their audio is the test set (step 5) |
| Where units come from | The grounded per-clip GMR `.pkl` files (`~/robotics/data/beat2_full_torso/k1/*_grounded.pkl`, 30 fps) + clip time spans from `segments.json` | They hold root position/rotation + 22 joints, the format `ground_clip` and `upload_motion`'s converter already read. Stitch at 30 fps, convert to the 50 Hz `.npz` at the end |
| Lower body | **v0: whole body from the units** (legs included). Compare with a "fixed legs" mode in step 3 | **The K1 has no waist**, so the trunk leans only by moving the legs. Fixed legs means a rigid trunk, which may look stiff. The roadmap's "fixed lower body" needs this check before it becomes the rule. Whole-body Tier A motion is also what the tracker trained on |
| Audio features | **Start with numpy/scipy only:** loudness (RMS energy), onset strength (spectral flux), speech vs pause. Add pitch later if needed | Each is ~10 lines, so you see exactly what is measured. `librosa` (an audio analysis library) only if something is missing |
| Feature scaling | **z-score per utterance** (subtract its mean, divide by its standard deviation) | Kokoro's voice is flatter and steadier than a human's. Comparing raw loudness would map all robot speech to "calm" |
| Code location | `src/booster_mjlab/gesture/` in this repo (main venv), CLI `uv run gesture ...` | Needs the motion files, `ground_clip` and `sim2sim`, all here. Only numpy/scipy/mujoco, so it can later run on the robot |
| Output | The combined-motion `.npz` (`clip_names`, `clip_lengths`, ...) + the reply WAV, one folder per reply | `sim2sim`, `eval-tracking` and `export_deploy_clip.py` already read that format |
| Speed target | **< 100 ms** for a 10 s reply on the laptop CPU | Retrieval is a table lookup plus a small search; it shouldn't touch the speech latency budget |

## Step 0. EMAGE smoke test (1 day, timebox it)

**Why first:** you've never seen *generated* gesture motion on the K1. One day with EMAGE shows
what a neural generator's output looks like, what breaks in the tracker, and gives a reference
point for judging retrieval later. It's the roadmap's step 2.

**Tasks**
1. Install EMAGE from [PantoMatrix](https://github.com/PantoMatrix/PantoMatrix) in its own venv
   (like GMR). Audio checkpoint: Hugging Face `H-Liu1997/emage_audio`. It needs the SMPL-X model
   files you already have in GMR.
2. Run it on ~5 `reply.wav` files from `speech/runs/` and 2 held-out BEAT2 takes (to compare with
   the real mocap of the same audio).
3. EMAGE writes BEAT2-style SMPL-X `.npz`, the same format `tools/beat2_to_gmr.py` reads → GMR
   (torso IK config) → `ground_clip` → `clip_qc.py` → `sim2sim --video`, audio dubbed.
4. Write down what breaks: jitter, foot sliding or stepping, joint limits, self-collision, falls,
   and how it *looks* next to the real mocap.

**Exit criteria:** dubbed videos of 5 EMAGE replies; a short list of failure causes in `log.md`.
If installation eats more than half the day, stop and move on: this step is optional.

**Pitfalls:** EMAGE generates the legs too (it may step or sway); its output frame rate is 30 fps;
it may want a transcript (TextGrid) for its text input, check whether an audio-only mode exists.

## Step 1. Library data: audio + sync check (1–2 sessions)

**Why:** retrieval matches audio to audio, so every library clip needs its speaker's audio, cut to
exactly the clip's time span. And if BEAT2's audio and motion are offset, every match is offset
too.

**Tasks**
1. Download BEAT2 audio (`wave16k`) for the chosen speakers' training takes, then the rest.
   Size: float32 at 16 kHz is ~64 kB/s, so all 1,236 training takes are **~9.3 GB** (40 h; 91 GB
   free on the laptop). Command pattern in `tools/export_deploy_clip.py`'s docstring.
2. Also download held-out audio for step 5 (142 takes, ~2 GB).
3. **Sync check** (left over from Slice 0, `plan.md` G): for 3 clips, play the dubbed video and
   check that a stressed word lines up with its gesture stroke. Then measure it: the
   cross-correlation between audio loudness and hand speed should peak near zero lag. Do this
   across many clips, it's one function.
4. Pick the first speakers: expressive (hand speed in `segments.json`, `arms_human_cm_s`),
   well tracked (per-speaker eval tables in `log.md`), several hours each.

**Exit criteria:** audio on disk for the subset; measured audio–motion lag (expect within ~1–2
frames); a plot of loudness vs hand speed for 3 clips.

**Learn:** audio as a 1-D array of samples; sample rate; frames and hops (one feature value per
20 ms window = 50 Hz, matching the motion); cross-correlation.

**Pitfalls:** BEAT2 audio is float32, not 16-bit PCM; a few takes may be missing audio
(`segments.json` lists `missing` takes); some clips start a fraction of a frame off the audio.

## Step 2. Features and units (2 sessions)

**Why:** this decides what "similar audio" and "one gesture" mean. Measure before matching.

**Tasks**
1. **Audio features at 50 Hz** (one value per 20 ms): RMS energy in dB, onset strength (spectral
   flux: how much the spectrum grows from one window to the next, high at syllable starts), and a
   speech/pause flag (threshold on energy, or reuse Silero VAD from `speech/`).
2. **Motion features** from the K1 body positions: left and right hand speed, hand height,
   hand distance from the trunk, plus the start and end pose of each unit (joint angles).
3. **Units:** cut each library clip at local minima of total hand speed, keeping units 0.5–3 s.
   Each unit stores: source clip, frame range, audio features, motion features, start/end pose.
4. Build the library file once (`uv run gesture build-library`) and cache it.
5. **Does audio predict motion at all?** Correlate loudness and onset rate with hand speed across
   the library. If the correlation is near zero, matching on these features is pointless and you
   need better features (pitch, word stress) before step 3. This is the most important number of
   the stage.

**Exit criteria:** library stats (number of units, length histogram, units per speaker); the
correlation table; 5 random units watched in `visualize-motions` to confirm they look like
whole gestures.

**Learn:** short-time Fourier transform (the spectrogram); RMS and decibels; spectral flux;
gesture phases; why per-speaker normalization matters (some people are always louder).

**Pitfalls:** cutting at speed minima makes many tiny units during holds (merge short ones);
units that start mid-step (Tier A allows ankles to move 10 cm); hand position must be measured
relative to the trunk, not the world.

## Step 3. Matching and stitching, offline (3–4 sessions)

**Why now:** with features and units, this is the core: reply audio in, K1 reference out.

**Tasks**
1. **Split the reply** into segments of about one unit length, at pauses and word boundaries
   (`tts.json` has word times).
2. **Cost per candidate:** distance between the segment's audio features and the unit's audio
   features (after z-scoring), and a length mismatch penalty.
3. **Transition cost:** distance between the end pose of unit i and the start pose of unit i+1:
   arm joints, hand positions, and **foot positions relative to the trunk** (different stances
   make the feet slide during a crossfade).
4. **Search:** keep the best ~20 candidates per segment, then dynamic programming over the whole
   reply for the cheapest sequence. Penalize reusing a unit within 30 s.
5. **Time-fit:** stretch or squeeze each unit by up to ±15% to fill its segment (resample frames).
6. **Stitch** in GMR `.pkl` space (`root_pos`, `root_rot`, `dof_pos` at 30 fps): crossfade joints
   over ~0.3 s, interpolate trunk rotation with slerp (quaternion interpolation), rotate each unit
   so its heading continues from the previous one, and keep the root position continuous.
7. **Clean up:** run `ground_clip` (replants feet with leg IK) → convert to the 50 Hz `.npz`
   (`upload_motion`'s `convert_batched`, which also runs forward kinematics for body positions) →
   `clip_qc.py` Gate 1 checks.
8. **Check in sim:** `sim2sim` from standing with `--video`, the reply's audio dubbed on.
9. **Fixed-legs comparison:** the same replies with the legs (and so the trunk) held at a standing
   pose, and only arms and head from the units. Watch both; decide the lower-body rule.

**Exit criteria:** 5 replies from `speech/runs/` → dubbed videos; 0 severe Gate 1 flags; 0 falls in
`sim2sim` (with `--push` and 40 ms delay too); no visible pops at seams; run time < 100 ms per
reply (stitching and grounding excluded if they're slower, note the number).

**Learn:** dynamic programming / Viterbi (the best path through a grid of choices); quaternions and
slerp; why joint-space crossfades are safe for limits (each joint's range is an interval, and a blend
of two values inside it stays inside) but not for collisions (arms can pass through the body).

**Pitfalls:**
- **Velocities must match positions.** The policy sees reference joint velocities. Recompute them
  from the stitched positions, never copy them from the units.
- **Heading jumps:** each BEAT2 clip faces its own direction. Without yaw alignment the reference
  trunk spins at a seam and the robot turns with it.
- Legs and trunk orientation can disagree after blending (feet not flat). `ground_clip` fixes most
  of it; Gate 1's foot checks catch the rest.
- Matching always picks the same few "average" units: the reuse penalty and a little randomness
  among near-equal candidates fix it.

## Step 4. Idle, start and end, continuous runs (2–3 sessions)

**Why:** a conversation is mostly *not* talking. The robot must look alive while listening, start
gesturing without a jump, and settle back. This is also tracker exit criteria 5 (transitions) and
9 (continuous operation).

**Tasks**
1. **Idle library:** low-motion windows (hands slow, small sway) from the same data. Some speakers
   (e.g. Nidal, held out, so use quiet training speakers) have long ones.
2. **Idle player:** loops idle units with crossfades, never repeating the same unit back to back.
3. **Reply in, reply out:** the reply's units are stitched onto the idle stream, with transitions
   from the current idle pose (the transition cost from step 3 picks a first unit close to it).
4. **Conversation sim:** a script replays a whole `speech/runs/<session>` (turns with gaps) as one
   reference: idle → reply 1 → idle → reply 2 ... Run 2 min, then 10 min, in `sim2sim`.
5. Measure: falls, drift (trunk position), heading change, seam smoothness (largest joint jump
   per frame, the Gate 1 rule).

**Exit criteria:** 2-minute run with no fall and drift under ~10 cm; 10-minute run attempted, and
the results decide whether the final tracker run needs stitched clips in training (`roadmap.md`).

**Learn:** why the tracker has never practiced this (training teleports robots between clips);
drift in a policy that can't see its position (No-State-Estimation).

**Pitfalls:** slow drift that only shows after minutes; idle that looks frozen or robotic; the
robot ending a reply mid-gesture when the audio stops (finish the unit, then retract).

## Step 5. Evaluation against baselines (2 sessions)

**Why:** "it looks good to me" isn't enough to decide anything, and the same set-up later judges a
neural generator.

**Tasks**
1. **Test audio:** held-out speakers' audio (never in the library) + 10 TTS replies.
2. **Three versions per test audio:** retrieval; **random** retrieval (same units and stitching,
   audio ignored); and for held-out clips, the **real mocap** of that speaker on the K1
   (`heldout-val` file) as the upper bound.
3. **Beat consistency (BC):** how often motion "beats" (moments the hands stop or change direction)
   fall near audio onsets. Used in the BEAT and EMAGE papers (arXiv 2401.00374); check their exact
   definition before comparing your numbers with theirs.
4. **Blind viewer test:** pairs of dubbed sim videos (retrieval vs random, retrieval vs real),
   5+ people, 10+ pairs each: "which one fits the speech better?"
5. **Diversity:** distinct units per minute; longest repeated pattern.

**Exit criteria:** retrieval beats random in BC and in the viewer test (≥ 60% preferred);
real mocap's lead over retrieval measured. Results in `log.md`.

**Learn:** why a baseline that ignores the input is the honest comparison; small-sample viewer
tests (a 60/40 split over 10 pairs is noise; you need many pairs or many viewers).

**Pitfalls:** viewers can be biased by the order of videos (shuffle it); Kokoro's voice and a
human's are different, so report TTS and human audio separately.

## Step 6. Connect to the speech loop, offline per turn (1–2 sessions)

**Why:** this closes the loop in sim: talk to the laptop, and each reply comes with a K1 reference.

**Tasks**
1. A `GestureSink` in `speech/` (the hook from `speech_plan.md` step 7): after TTS, write
   `gesture.npz` into the turn folder by calling the generator (a subprocess or a small local
   service, since `speech/` has its own venv).
2. `uv run gesture replay speech/runs/<session>`: plays the whole conversation in `sim2sim` with
   the audio (step 4's conversation sim, on live data).
3. Time it: the generator's time is added before playback can start.

**Exit criteria:** a live laptop conversation where every turn writes a reference; the replay
video shows the K1 gesturing in sync with its voice; added delay per turn measured (target
< 100 ms).

**Pitfalls:** the speech loop and the generator disagree about the audio's start time (Kokoro adds
silence at the start; use `tts.json`'s word times, which already include it).

## Step 7. Later (notes only, don't build yet)

- **Streaming:** when speech step 4 streams TTS sentence by sentence, run the search per sentence,
  with the previous sentence's last unit fixed. Retrieval needs no future audio beyond the sentence.
- **Semantic gestures:** LLM inline tags (`[wave]`, `[point_at:left]`, `speech_plan.md` step 6)
  insert a unit from the AMASS gesture clips at the tagged word, with the same transition cost.
  BEAT2's TextGrid word alignments would allow matching on words too.
- **Listening behaviour:** small nods and gaze toward the speaker while the user talks.
- **Neural generator (paper angle):** a K1-native model trained on the library itself (audio →
  K1 joints, ~23 h). Retrieval is its baseline (step 5 set-up). Only if retrieval looks repetitive.
- **On the robot:** the generator is CPU-light, so it can run on the K1 or the laptop; the
  reference and audio must share one clock (`speech_plan.md` step 7).

## Definition of done (whole stage)

- Any `reply.wav` → K1 reference in < 100 ms, from training-speaker motion only.
- Dubbed `sim2sim` videos where the gestures visibly follow the speech; 0 falls with pushes and
  delay; 0 severe Gate 1 flags.
- A 2-minute idle–reply–idle run without a fall; the 10-minute result recorded.
- Retrieval beats random audio-ignoring retrieval in BC and a blind viewer test.
- The lower-body rule (whole body vs fixed legs) decided by watching both.
- The speech loop writes a reference per turn; a conversation replays in sim with audio.
- Numbers and decisions in `log.md`.

## Sources (checked 2026-11-11 unless noted)

- EMAGE: [arXiv 2401.00374](https://arxiv.org/abs/2401.00374), code [PantoMatrix](https://github.com/PantoMatrix/PantoMatrix), checkpoint `H-Liu1997/emage_audio` on Hugging Face
- Generated motion vs trackers: GenTrack [arXiv 2608.01410](https://arxiv.org/abs/2608.01410)
- Streaming generators without released code (2026-11-10 review): LiveGesture [2604.10927](https://arxiv.org/abs/2604.10927), GestureFAR [2609.21576](https://arxiv.org/abs/2609.21576), RoboGesture [2608.28693](https://arxiv.org/abs/2608.28693)
- Background (from memory, not re-checked): motion graphs (Kovar, Gleicher, Pighin, SIGGRAPH 2002); motion matching (Clavet, GDC 2016); gesture phases (McNeill, *Hand and Mind*, 1992)
