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

**Deferred 2026-11-11: start at step 1.** Retrieval doesn't depend on this, and steps 3–4 test the
tracker on retrieval's own output. Step 2 holds the riskier question (does audio predict motion?).
Run this later as a third comparison in step 5, or before starting a neural generator.

**Why it's useful (when you get to it):** you've never seen *generated* gesture motion on the K1. One day with EMAGE shows
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
3. **Sync check** (left over from Slice 0, `archive/slice0_plan.md` G): for 3 clips, play the dubbed video and
   check that a stressed word lines up with its gesture stroke. Then measure it: the
   cross-correlation between audio loudness and hand speed should peak near zero lag. Do this
   across many clips, it's one function.
4. Pick the first speakers: expressive (hand speed in `segments.json`, `arms_human_cm_s`),
   well tracked (per-speaker eval tables in `log.md`), several hours each.

**Exit criteria:** audio on disk for the subset; measured audio–motion lag (expect within ~1–2
frames); a plot of loudness vs hand speed for 3 clips.

**Result (2026-11-11, `tools/gesture_sync_check.py`, then `gesture/sync.py`):** audio is in sync
for nearly all takes. Use jaw opening *speed*, not jaw angle: the angle check first flagged all of
Miranda's session 0 (it opens to breathe before phrases); the speed check keeps 298/310 takes and
drops 12 (Miranda 10, Wayne 2). Hands lead loudness by ~0.4 s (natural). Details in `log.md`.

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
4. Build the library file once (`uv run gesture build-library`) and cache it. **Gate each take on
   the jaw check** (`gesture/sync.py`): jaw opening *speed* (from `poses[:, 66:69]` in the BEAT2
   SMPL-X file) vs loudness must peak within ±0.2 s.
5. **Does audio predict motion at all?** Correlate loudness and onset rate with hand speed across
   the library. If the correlation is near zero, matching on these features is pointless and you
   need better features (pitch, word stress) before step 3. This is the most important number of
   the stage.

**Exit criteria:** library stats (number of units, length histogram, units per speaker); the
correlation table; 5 random units watched in `visualize-motions` to confirm they look like
whole gestures.

**Result (2026-11-11, `uv run gesture analyze`; full numbers in `log.md`):** library v0 = 2,487
clips, 7.8 h, 20,514 units (median 1.26 s, cut where the hands at least halve their speed).
Audio predicts hand activity **weakly but really**: r 0.21 on unseen takes, 0.19 on an unseen
speaker, 0.15 for nearest-neighbour retrieval, 0.13 for units (shuffled baselines ~0.00 ± 0.03).
Pauses are the clearest signal (hands 0.6 sd calmer); onsets and peak loudness carry the rest;
pitch adds nothing. Strong accents are ~1.2× more likely at a stroke's end than at random.
Units rendered for watching: `logs/gesture/units/*_audio.mp4`.

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
   features (after z-scoring), and a length mismatch penalty. Per step 2: use onset mean, peak
   and mean loudness, speech fraction (not pitch), with the unit's audio taken 0.44 s after its
   motion (the hands lead).
3. **Transition cost:** distance between the end pose of unit i and the start pose of unit i+1:
   arm joints, hand positions, and **foot positions relative to the trunk** (different stances
   make the feet slide during a crossfade).
4. **Search:** keep the best ~20 candidates per segment, then dynamic programming over the whole
   reply for the cheapest sequence. Penalize reusing a unit within 30 s.
5. **Time-fit:** stretch or squeeze each unit by up to ±15% to fill its segment (resample frames),
   choosing the stretch that puts the unit's stroke ends nearest the reply's strong accents (step 2:
   audio matching alone gets timing only slightly better than chance).
6. **Pauses:** in the reply's pauses, prefer low-motion units (step 2's clearest signal).
7. **Stitch** in GMR `.pkl` space (`root_pos`, `root_rot`, `dof_pos` at 30 fps): crossfade joints
   over ~0.3 s, interpolate trunk rotation with slerp (quaternion interpolation), rotate each unit
   so its heading continues from the previous one, and keep the root position continuous.
8. **Clean up:** run `ground_clip` (replants feet with leg IK) → convert to the 50 Hz `.npz`
   (`upload_motion`'s `convert_batched`, which also runs forward kinematics for body positions) →
   `clip_qc.py` Gate 1 checks.
9. **Check in sim:** `sim2sim` from standing with `--video`, the reply's audio dubbed on.
10. **Fixed-legs comparison:** the same replies with the legs (and so the trunk) held at a standing
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

**Result (2026-11-11, `uv run gesture generate | render | check`; details in `log.md`):** 5 real
replies + random baselines. 0 severe Gate 1 flags, 0 falls in 60 sim runs (incl. pushes + 40 ms
delay), feet fixed, no seam faster than the reply's other motion, matching < 100 ms. Matched
replies hit 84% of strong accents with a stroke end (chance 26%; random 37%) and move like the
library (0.38 vs 0.40 m/s). Changes from the plan above: **foot lock** (one stance per reply, legs by
IK; replaces the whole-body vs fixed-legs choice), trunk-twist and speaker terms in the transition
cost, crossfades lengthened per seam (no joint > 2 rad/s), and an intensity target from the audio
neighbours (without it the search drifted to calm units).

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

**Result (2026-11-11, `uv run gesture conversation`; details in `log.md`):** a whole speech-loop
session plays as one reference: calm units while listening (hands 0.05 vs 0.35 m/s talking),
matched gestures while speaking, one foot-locked stance, one speaker per conversation (persona).
2.4 min and 10.1 min: Gate 1 clean, no falls with pushes and 40 ms delay, drift 6–8 cm plain
(17 cm with pushes over 10 min), heading within 8°. Position creeps slowly because the policy can't
sense it (final tracker run: consider a foot-slip penalty). Found on the way: idle repeats (fixed:
no unit back within 60 s), mixed stances (persona), a foot-lock failure cascade (retries from
fresh starts), units with the trunk over one leg (skipped). Listening behaviour (nods, gaze) not
built.

## Step 5. Evaluation against baselines (2 sessions)

**Why:** "it looks good to me" isn't enough to decide anything, and the same set-up later judges a
neural generator.

**Tasks**
1. **Test audio:** held-out speakers' audio (never in the library) + 10 TTS replies.
2. **Three versions per test audio** (plus the context-rate versions once the context layer exists,
   see step 7: no / sparse / dense context gestures): retrieval; **random** retrieval (same units and stitching,
   audio ignored); and for held-out clips, the **real mocap** of that speaker on the K1
   (`heldout-val` file) as the upper bound. Optional fourth: **EMAGE** (step 0, deferred here),
   to see whether a neural model beats retrieval.
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

**Result (2026-11-11, `uv run gesture serve` + `speech/src/speech/gesture.py`; details in `log.md`):** each
finished reply is posted to a local service (library loaded once) and gets its motion in
`<turn>/gesture/` within ~0.6–0.9 s, without delaying the conversation; `uv run gesture replay`
turns a session into a dubbed video. Choosing takes 20–40 ms; foot lock (~0.1 s) and grounding
(~0.15–0.25 s, largely redundant after foot lock) are the runtime parts to trim before streaming.
Live test 2026-11-11 (`tools/live_test.sh`, standard script): all 10 turns got motion, Boston: "looks natural". **Step 6 done.**

## Step 7. Streaming: motion live, ready before its audio (done 2026-11-11; response time to re-check)

**Why:** today motion is made after the robot has finished speaking (step 6). A robot needs each
reply's motion *before* the matching audio plays, and the hands lead the voice by 0.44 s. Doing it
live on the laptop, with the K1 gesturing in a MuJoCo window as it talks, is the same path the
robot will use.

**What's known (measured 2026-11-11, `log.md`):**
- Speech streams a reply in pieces (`speech/src/speech/streaming.py`: chunker -> TTS worker -> `Player`);
  `tts.json` records each piece's ready and played times. **Piece 0 plays the moment it's ready** (no
  lookahead); later pieces were ready ~2.6 s before playing.
- Generator cost per reply: choosing (features + search + stitch) 20–40 ms; foot lock ~0.1 s; grounding
  (`ground_clip`) 0.15–0.25 s, largely redundant after foot lock; QC + forward-kinematics conversion are
  offline extras (the policy only needs joint positions, joint velocities and trunk orientation).
- The tracker takes 50 Hz references with no position input (`y1r48dhc`); `deploy/` has `Reference`,
  `build_observation`, `ObservationHistory`; `sim2sim.py` has the plain-MuJoCo loop.

**Design sketch (to refine in the new session):**
1. One process, `gesture live`: holds the library, a **session timeline** of 50 Hz reference frames
   (always a few seconds of idle ahead of "now"), and runs the policy in plain MuJoCo in real time
   with a viewer, reading the timeline.
2. The speech loop sends **piece events**: text, word timings, the piece's audio, and when it will play
   (`time.monotonic()`, shared by processes on one machine). Hook point: where `Player` queues a piece.
3. Per piece: segment, candidates, Viterbi with the previous unit fixed; replace the timeline from
   max(now + margin, play time − 0.44 s). Stitch and foot-lock incrementally on a stance fixed at
   session start; try dropping `ground_clip` (check the feet stay on the floor).
4. **The first piece has no lookahead.** Options: delay its playback ~0.3–0.5 s (costs latency), start
   its motion late, or begin an "about to speak" gesture at the LLM's first token (before audio exists).
   Measure, then choose.
5. Barge-in (speech step 5) later must cancel queued motion too.

**Exit criteria:** the standard live test (`tools/live_test.sh`, `notes/live_test_script.md`) with the
K1 gesturing live in a MuJoCo window, in sync with its voice; for pieces after the first, motion
ready ≥ 0.44 s before its audio; the first piece's lateness measured; no falls; the conversation's
response time not worse than 1.47 s median (first live test).

**Result (2026-11-11, `uv run gesture live`, `gesture/stream.py` + `gesture/live.py`; details in `log.md`):**
- Built as sketched: one process holds the library, the session timeline and the policy in plain MuJoCo
  with a window; the speech loop sends `/begin`, `/piece` (audio, word times, play time), `/end`.
- Per piece: planning ~100 ms in total, but the first half second of motion is out after 30–50 ms
  (foot lock is done and published in 0.5 s chunks), so a plan may change the timeline from now + 0.1 s.
- **`ground_clip` dropped:** the stream locks the feet on one stance for the whole session (fixed at start
  from the persona's units), at a fixed height with level soles. Feet move 0.002 mm, lowest foot point
  0.00 mm. The stance frame is smoothed with a trailing average, so nothing already sent changes.
- **First piece: option 3 (start at the LLM's first words).** Its matched motion can only start ~0.09 s
  after its audio (0.53 s later than ideal). The pre-start gesture (chosen without audio, fairly lively)
  begins 0.43 s median before the audio (0.25–0.62 s) and costs no latency.
- Measured by re-sending the first live test's session with its recorded timing (`--replay-session`):
  pieces after the first ready 1.22 s median before their audio, all started on time (within 0.04 s);
  0 falls with pushes + 40 ms delay; control loop never late (max 0.7 ms).
- **Live test with the mic (2026-11-11, session `2026-11-11_22-12-58`):** all 20 pieces on time (later pieces
  1.33 s median before their audio, min 0.71), pre-start 0.67 s before the first piece, 0 falls; Boston:
  nothing glaring. Response 1.59 s median vs 1.47 (Kokoro slower next to the sim; onnxruntime's spinning
  thread pool, 350% CPU, fixed since: `gesture live` 7-24% CPU). Re-check on the next live test.
- Filming a live run: `gesture live-video` (re-runs the tracker on the saved frames, exact; added 2026-11-11).
- Not built: barge-in cancel (task 5), keeping the pre-start unit to its end instead of cutting into it (try if starts look twitchy).

## Step 8. Later (notes only, don't build yet)

- **Context layer (semantic gestures + emphasis)**: design agreed 2026-11-11, after watching step 3
  (`log.md`: beats-only already reads as natural; what's missing is gestures that follow the words).
  Build after steps 4–5.
  - **Principle: sparse, on top of the beats, never instead of them.** People make meaning-carrying
    gestures only occasionally; most hand motion is beats. A missing context gesture looks fine, a
    wrong or excessive one looks robotic (a mime acting out every noun). When unsure, add nothing.
  - **Emphasis first (cheapest win):** the LLM marks the key phrase (`[emph]...[/emph]`); the generator
    raises that segment's intensity target and prefers units with a stroke on its strong accent. Fixes
    "could have gestured harder on the punch line" with machinery that already exists.
  - **Then a small closed vocabulary**, inline tags aligned to words with TTS word timings
    (`speech_plan.md` step 6): `point` (listener / self / left / right), a few named gestures (wave,
    "this big", shrug). The LLM only decides *whether* and *which*; it never produces motion. Each
    tag inserts a library unit at the tagged word, joined with the usual transition cost. Pointing and
    emphasis suit the K1; shape-drawing (iconic) gestures won't read without wrists or hands.
  - **Rate is a parameter**, e.g. at most one context gesture per sentence and only for phrases that
    clearly call for one, plus a cooldown so the same gesture doesn't repeat back to back.
  - **Starting rate from data:** check whether BEAT2 kept BEAT's semantic gesture annotations; if
    not, count meaning-carrying gestures by hand in ~20 clips.
  - **Final rate from viewers:** step 5's blind test with three versions of the same replies (no
    context gestures / sparse / dense); pick the rate where "natural" peaks.
  - Gesture sources: AMASS waves and points (kept for this), BEAT2 clips found via TextGrid word
    alignments, phone video -> GVHMR -> GMR for missing ones (e.g. self-pointing).
- **Listening reactions** (requested 2026-11-11 after the streaming-session video). Three levels, easiest first:
  1. **Backchannel nods while the user talks** (easy, 1–2 sessions): small head-pitch nods (K1 has head
     pitch) layered onto the idle motion, triggered at the user's phrase ends (short pauses found by the
     speech loop's VAD), rate-limited (e.g. at most one per ~5 s, not every pause). People nod at pauses
     and at low-pitch phrase ends (backchannel research, e.g. Ward & Tsukahara 2000). No LLM needed; the
     head is light, so the tracker should follow it easily (check in sim).
  2. **A reaction in the thinking gap** (medium): the 1.5–3.7 s between the user stopping and the reply
     starting is currently plain idle. The LLM can open its reply with a reaction tag (`[surprised]`,
     `[amused]`, `[thinking]`, `[agree]`) that plays right away, before any speech: it fills the wait
     and makes latency feel shorter. Needs a small reaction library (BEAT2 conversation takes, AMASS, or
     phone video -> GVHMR -> GMR) and the same sparse-rate rules as the context layer.
  3. **Reactions in the middle of the user's speech** (hard): needs streaming STT and something judging
     meaning on partial transcripts with low latency. Later, if 1–2 aren't enough.
  - Same principle as the context layer: a missing reaction looks fine, a wrong or constant one looks
    robotic. Judge with the step 5 viewer test.
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
