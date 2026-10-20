# Slice 0 Plan: Real Talking Motion on the K1

Step 0 of `roadmap.md`. About one week, mostly CPU. (The old milestone 1 phases A–E are
done or superseded; their history is in `log.md`.)

**Goal:** the K1 gestures along to one real BEAT2 speech clip in sim, with a video that has
the original audio dubbed over it.

**The real output is a list:** what conversational motion breaks or strains in the pipeline.
That list sets the requirements for the general tracker (step 1). Write things down as you
hit them, not just at the end.

## Overview

| Phase | Goal | Needs GPU? |
|---|---|---|
| 0. Admin | Tell the lead about the new milestone 1 | No |
| A. Get BEAT2 | One speaker's clips and audio, format understood | No |
| B. Pick a clip | One good talking clip, cut to a 20–30 s window | No |
| C. Retarget | BEAT2 → GMR → K1 clip that reads as talking | No |
| D. Ground + upload | `ground_clip` handles weight shifts; clip checked in the viewer | No |
| E. Train | Single-clip tracker on the window | Yes (laptop is fine for 20–30 s) |
| F. Evaluate | `eval-tracking` numbers + watch it | Yes (short) |
| G. Video with audio | Sim video, original audio dubbed in, in sync | No |
| H. EMAGE smoke test (optional) | Confirm the pretrained weights run; first look at generated motion | GPU helps |
| I. Write up | Log + "what step 1 must handle" list | No |

## 0. Admin

- [ ] Message the lead: milestone 1 becomes "track real conversational motion"; give the
  reason (the waves proved the pipeline; isolated gestures don't look like what box 1 will
  produce). Ask again about club GPU access, since step 1 depends on it.
- [ ] Update `proposal.md` (goal, approach, metrics, timeline) once the lead agrees.

## A. Get BEAT2

- [x] Accept the license and download **one or two English speakers only** (SMPL-X motion
  + matching audio), not all 60 hours.
- [x] Read the dataset README and open one motion file. Note:
  - frame rate
  - which way is up (Y-up or Z-up; AMASS is Z-up)
  - what the file keys and body-shape size are, compared with an AMASS SMPL-X file GMR already reads
  - how motion files pair with audio files (same name? same start time?)
- [x] Note typical clip lengths. They'll be much longer than the 3–4 s waves.

**Done when:** you can say exactly how a BEAT2 motion file differs from the AMASS files GMR
already accepts.

## B. Pick a clip

- [x] Listen to and watch a few clips. Pick one where the speaker:
  - stands in place (few or no steps)
  - gestures clearly with the arms (beats, open palms) and moves the head
  - doesn't rely mainly on fingers or wrist twists
- [x] Choose a **20–30 s window** with clear speech. Use the full clip later, as a stretch goal.
- [x] Record the speaker, file, and frame/time range in the log, so the audio can be cut
  to exactly the same window later.

**Done when:** one clip and window are picked and logged.

## C. Retarget with GMR

- [x] Check whether GMR reads the BEAT2 file as-is. If not, write a small converter to the
  AMASS-style format (axis convention, body-shape size, frame-rate field). Most of the
  risk in this phase is here.
- [x] Retarget and watch it in GMR's viewer. Check:
  - Does it still look like someone talking, or just like idling? Small motions may nearly
    disappear at K1 scale.
  - Do head nods and turns come through? The head is the K1's extra channel.
  - What's lost: fingers, wrist twist, spine and torso lean (the K1 has no waist).
  - Do the hands pass through the torso during gestures near the belly?

**Done when:** the K1 clip in GMR's viewer reads as "talking with hands."

## D. Ground, verify, upload

- [x] Run `ground_clip` on it. **New risk:** it plants both feet and flattens stance feet,
  but talking has weight shifts and small steps. Check whether it turns those into foot
  sliding, knee pops, or an error.
- [x] Watch it in `visualize-motions`: feet on the floor, no sliding, no self-collision, no
  flipped joints.
- [x] Upload and save the artifact name in the log.

**Done when:** the grounded window plays cleanly in booster_mjlab.

## E. Train

- [x] Train the single-clip tracker on the 20–30 s window, the same task as the waves.
- [x] Budget more iterations than the waves' 2,500, since there's ~8× more motion to learn.
  Use `wandb-guide.md` / `/analyze-run` to decide when to stop, not a fixed count.
- [x] Watch for parts of the clip that keep failing (DeepMimic-style early termination
  plus adaptive start sampling will keep sending training back to the hard parts).
- [x] Check the GPU temperature. If the window needs hours, it's a club GPU job.

**Done when:** reward and errors level off with terminations near zero.

## F. Evaluate

- [x] Before trusting `eval-tracking`, check that it handles a clip longer than the training
  episode length (it was built and tested on 3–4 s clips).
- [x] Run it. Compare with the waves: falls, hand error, joint error, foot tilt, and
  especially **drift** (it was ~3 cm over 3 s; does it keep growing over 30 s?).
- [x] Note *when* in the clip failures and error spikes happen, and what the speaker is
  doing at those moments.
- [x] Watch `play` at real speed for jitter and foot shuffling. If it's visibly jittery but
  the numbers look fine, note that eval needs a smoothness metric (feeds step 1).

**Done when:** numbers are logged next to the waves' table, with notes on where it struggles.

## G. Video with audio

- [x] Record the sim with `play`'s recording option.
- [x] Cut the original audio to the same window and dub it onto the video.
- [ ] Check sync at a sharp moment (a stressed word with a beat gesture). If it's off, check
  frame rates (BEAT2 vs the K1 clip) and the start offset.
- [ ] Optional: a side-by-side with the human reference.

**Done when:** a watchable video of the K1 gesturing to real speech, in sync. Share it with
the lead and the club.

## H. EMAGE smoke test (optional, half a day max)

- [ ] Install EMAGE and run its pretrained weights on the **same audio window**.
- [ ] Push its SMPL-X output through the converter → GMR → `ground_clip`, and view it next to
  the mocap version in `visualize-motions`. No training.
- [ ] Note how it differs from mocap: jitter, foot sliding, amplitude, odd poses.

**Done when:** you know the weights run (or what blocks them) and have a first look at what
generated motion will ask of the tracker.

## I. Write up

- [ ] `/log-session` with the run, eval table, and video link.
- [ ] Add a **"What step 1 must handle"** section to the log, grouped as:
  - data format / conversion
  - clip length and training cost
  - feet: weight shifts, steps, sliding
  - drift over long clips
  - smoothness / jitter
  - lost DoF (wrists, fingers, waist) and whether the motion still reads as talking
  - (from H) generated vs mocap differences
- [x] Update `CLAUDE.md` status.

## Status (2026-10-20)
- Superseded as the current step: the general tracker is trained (`1de2pner`); the current step is the tracker exit criteria in `roadmap.md`. Slice 0 leftovers below are still worth closing.

## Status (2026-10-18)
- A–F done (see `log.md`, 2026-10-16/17). The window is **10 s**, not 20–30 s: Scott steps every 5–10 s, so no longer still window exists (`--find-still`). The general tracker (`0j0flpxj` model_5999) tracks 146 such clips, so criterion 1 is met in spirit
- G: video recorded and dubbed (`0j0flpxj` model_5999, torso IK, `talk_scott_1_1_t34-44-torso:v0`): "considerably better and more natural, the lean back is gone". Sync check still to do
- Left: sync check (G), the "what step 1 must handle" list (I), EMAGE (H, optional), admin (0, Boston)

## Slice 0 is done when

1. The K1 tracks a 20–30 s BEAT2 window with no falls in `eval-tracking`.
2. There's a synced video with the original audio.
3. The "what step 1 must handle" list is written.
