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

- [ ] Accept the license and download **one or two English speakers only** (SMPL-X motion
  + matching audio), not all 60 hours.
- [ ] Read the dataset README and open one motion file. Note:
  - frame rate
  - which way is up (Y-up or Z-up; AMASS is Z-up)
  - what the file keys and body-shape size are, compared with an AMASS SMPL-X file GMR already reads
  - how motion files pair with audio files (same name? same start time?)
- [ ] Note typical clip lengths. They'll be much longer than the 3–4 s waves.

**Done when:** you can say exactly how a BEAT2 motion file differs from the AMASS files GMR
already accepts.

## B. Pick a clip

- [ ] Listen to and watch a few clips. Pick one where the speaker:
  - stands in place (few or no steps)
  - gestures clearly with the arms (beats, open palms) and moves the head
  - doesn't rely mainly on fingers or wrist twists
- [ ] Choose a **20–30 s window** with clear speech. Use the full clip later, as a stretch goal.
- [ ] Record the speaker, file, and frame/time range in the log, so the audio can be cut
  to exactly the same window later.

**Done when:** one clip and window are picked and logged.

## C. Retarget with GMR

- [ ] Check whether GMR reads the BEAT2 file as-is. If not, write a small converter to the
  AMASS-style format (axis convention, body-shape size, frame-rate field). Most of the
  risk in this phase is here.
- [ ] Retarget and watch it in GMR's viewer. Check:
  - Does it still look like someone talking, or just like idling? Small motions may nearly
    disappear at K1 scale.
  - Do head nods and turns come through? The head is the K1's extra channel.
  - What's lost: fingers, wrist twist, spine and torso lean (the K1 has no waist).
  - Do the hands pass through the torso during gestures near the belly?

**Done when:** the K1 clip in GMR's viewer reads as "talking with hands."

## D. Ground, verify, upload

- [ ] Run `ground_clip` on it. **New risk:** it plants both feet and flattens stance feet,
  but talking has weight shifts and small steps. Check whether it turns those into foot
  sliding, knee pops, or an error.
- [ ] Watch it in `visualize-motions`: feet on the floor, no sliding, no self-collision, no
  flipped joints.
- [ ] Upload and save the artifact name in the log.

**Done when:** the grounded window plays cleanly in booster_mjlab.

## E. Train

- [ ] Train the single-clip tracker on the 20–30 s window, the same task as the waves.
- [ ] Budget more iterations than the waves' 2,500, since there's ~8× more motion to learn.
  Use `wandb-guide.md` / `/analyze-run` to decide when to stop, not a fixed count.
- [ ] Watch for parts of the clip that keep failing (DeepMimic-style early termination
  plus adaptive start sampling will keep sending training back to the hard parts).
- [ ] Check the GPU temperature. If the window needs hours, it's a club GPU job.

**Done when:** reward and errors level off with terminations near zero.

## F. Evaluate

- [ ] Before trusting `eval-tracking`, check that it handles a clip longer than the training
  episode length (it was built and tested on 3–4 s clips).
- [ ] Run it. Compare with the waves: falls, hand error, joint error, foot tilt, and
  especially **drift** (it was ~3 cm over 3 s; does it keep growing over 30 s?).
- [ ] Note *when* in the clip failures and error spikes happen, and what the speaker is
  doing at those moments.
- [ ] Watch `play` at real speed for jitter and foot shuffling. If it's visibly jittery but
  the numbers look fine, note that eval needs a smoothness metric (feeds step 1).

**Done when:** numbers are logged next to the waves' table, with notes on where it struggles.

## G. Video with audio

- [ ] Record the sim with `play`'s recording option.
- [ ] Cut the original audio to the same window and dub it onto the video.
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
- [ ] Update `CLAUDE.md` status.

## Slice 0 is done when

1. The K1 tracks a 20–30 s BEAT2 window with no falls in `eval-tracking`.
2. There's a synced video with the original audio.
3. The "what step 1 must handle" list is written.
