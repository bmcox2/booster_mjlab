# Roadmap: Co-Speech Gestures on the Booster K1

Updated 2026-10-16. Replaces the "5–10 AMASS gestures" milestone 1 in `proposal.md`.

## The pipeline

```
audio ──► [1] gesture generator ──► SMPL-X motion ──► [2] GMR retarget ──► K1 reference ──► [3] RL tracker ──► K1 moves
           (borrow: EMAGE)                            (+ ground_clip)                       (build: mjlab)
```

- **Box 3 (the tracker) is the focus.** It's the robot-specific part, nobody has built one
  for co-speech motion on the K1, and it's what the club's mjlab and sim-to-real setup is for.
- **Box 1 is borrowed, not built.** Pretrained audio→SMPL-X models already exist (EMAGE, from
  the BEAT2 authors). Its output is GMR's input format.
- **Strategy:** get a rough version of the whole pipeline working first, so it's clear what
  the tracker actually has to handle. Then put the real effort into the tracker.

## Where things stand

- Done: the pipeline works on isolated AMASS gestures. Two waves (`me9exatd`, `pqh0whw0`)
  pass 50/50 with no falls and ~1.5 cm hand error.
- Lesson so far: most of the error came from the data (sunken clips, tilted feet), not the
  RL. Expect the same with talking data.

## Steps

| # | Step | Rough time | Compute | Done when |
|---|---|---|---|---|
| 0 | **Slice 0: real talking motion on the K1** ← *current* | ~1 week | Mostly CPU, laptop GPU | K1 gestures to one BEAT2 clip in sim; video with the real audio; list of problems for step 2 |
| 1 | **General tracker** (main RL work) | ~3–4 weeks | Club GPU | Low error, no falls on **held-out speakers** |
| 2 | **Product v1: plug in EMAGE** (offline) | ~1–2 weeks | GPU | Any audio file → K1 gesturing in sim |
| 3 | **Real-time, then semantic** | Later (spring) | GPU | Streaming audio with measured latency; LLM adds meaningful gestures |
| 4 | **Sim-to-real** (in parallel) | Club's timeline | Club | Policy runs on the club's K1 |

### 0. Slice 0: real talking motion on the K1 (current)

Take one BEAT2 clip (real mocap recorded with audio) and run it through GMR, then
`ground_clip`, then a single-clip tracker, the same way as the waves. Record a sim video with
the original audio dubbed over it.

- Why: it's the first result that looks like the end product, and it shows early what
  conversational motion does to the pipeline.
- Expect: long clips, constant small motions, weight shifts, and finger/wrist motion the K1
  can't do.
- Detailed steps: `plan.md`.

### 1. General tracker

- Build a **MultiMotionCommand**: one policy that samples from a library of clips (and start
  points within them), instead of mjlab's single-clip motion command.
- Training diet: many minutes of BEAT2 talking, plus the AMASS gestures.
- **Hold out whole speakers**, not just clips. That's the honest test of whether it follows
  motion it has never seen.
- New problems to expect: long continuous streams instead of 3 s clips, keeping the feet
  planted while the upper body moves freely, and smoothness. This is the research part.
- Extend `eval-tracking` to many clips, with results reported per speaker.

### 2. Product v1: plug in a pretrained box 1

- Any audio file → EMAGE → GMR → tracker → K1 gesturing in sim.
- Offline first: generate the whole motion, then play it back.
- Generated motion is messier than mocap (jitter, foot sliding, poses that aren't physically
  possible). This is where the tracker gets truly tested.

### 3. Real-time, then semantic

- Real-time: stream the audio in chunks and measure latency through all three boxes.
- Semantic: an LLM picks meaningful gestures from SeG for words like "hi" or "this one." The
  AMASS waves and points come back here.

### 4. Sim-to-real (in parallel, on the club's timeline)

- Pick the ankle model (standard vs `-Parallel`), add domain randomization, export the policy.

## What changed from the proposal

- **BEAT2 talking data replaces "5–10 AMASS gestures" as the tracker's main training data.**
  The two waves already proved the pipeline. More isolated gestures mostly re-prove it, and
  they don't look like what box 1 will produce.
- Keep a few AMASS gestures (point, wave) for the semantic layer.
- Milestone 1 becomes **"the K1 tracks real conversational motion."** Tell the lead, and
  update `proposal.md` so the two match.
