# Co-Speech Gesture Tracking on the Booster K1

Project proposal · Boston Cox · Oct 2, 2026

## Summary

For my project, I want to teach the K1 to gesture naturally while it talks. My first milestone is getting it to track 5–10 human co-speech gestures in mjlab without falling. I'm basing this on a December 2025 paper that built the same pipeline on the Unitree G1, and I'll use open tools (GMR, mjlab) and public gesture data, so most of the pieces already exist.

## Motivation

I'm interested in robots that can communicate with people, and speech alone isn't enough for that. When people talk, they gesture, point and nod, and those cues carry a lot of the meaning. If the K1 can do that, it opens up uses like tutoring or giving a presentation down the line.

## Background

| Work | How I'll use it |
| --- | --- |
| [DeepMimic](https://arxiv.org/abs/1804.02717) (2018) | The core method: PPO trains a policy to copy a reference motion, using a pose-matching reward, early termination and random start points in the clip |
| [Semantic Co-Speech Gesture Synthesis](https://arxiv.org/abs/2512.17183) (Dec 2025) | My anchor paper. It built the full speech-to-gesture pipeline on the G1, but released no code and only loosely described its data, so I'll rebuild it from open parts |
| [mjlab](https://github.com/mujocolab/mjlab) | The club's simulator. Its built-in motion-tracking task is based on DeepMimic, so I can start from it |
| K1 tracking code: booster_mjlab and Booster's booster_train | K1 motion tracking already exists. booster_mjlab runs it in mjlab and takes GMR clips directly; Booster's official booster_train has the same BeyondMimic tracking for the K1 in Isaac Lab, as a backup reference (links under Risks) |
| [GMR](https://github.com/YanjieZe/GMR) | Converts human motion to robot motion. It already supports the K1 (`booster_k1`) and takes SMPL-X data |
| [AMASS](https://amass.is.tue.mpg.de/) + [HumanML3D](https://github.com/EricGuo5513/HumanML3D) labels | Milestone 1 data. Large mocap library in GMR's native format; HumanML3D's text descriptions let me search for clips like "a person waves" |
| [SeG](https://github.com/LuMen-ze/Semantic-Gesticulator-Official) | Milestone 2 data. 208 gesture types labeled by meaning, the library the paper's LLM picked from. BVH format, so it needs converting |
| [BEAT2](https://pantomatrix.github.io/EMAGE/) | Milestone 3+ data. About 60 hours of people talking, in SMPL-X, for gestures timed to real speech |

## Gap

I can't just copy the paper, because the K1 is a much smaller robot with fewer joints than the G1.

| | Unitree G1 (paper) | Booster K1 |
| --- | --- | --- |
| Height | ~1.3 m | ~0.95 m |
| Total joints | 29 | 22 |
| Arm joints, each | 7 (incl. 3 wrist) | 4 (3 shoulder, 1 elbow) |
| Waist joints | 3 | 0 |
| Head joints | 0 | 2 (yaw, pitch) |

The missing wrists are the biggest problem: the paper's tracking error was highest at the wrists, which tells me that's where a lot of gesture detail lives. On the other hand, the K1 has a movable head, so nods and looking at someone are gestures the paper never used that I can add.

## Goal

By the end of milestone 1, I want the K1 to perform 5–10 gestures in mjlab simulation, start to finish, without falling. I'm keeping this milestone sim-only and will move to the real robot later.

## Approach

I'll use open tools end to end and stick with mjlab's default action space and reward functions, getting one gesture working before adding more.

```
AMASS gesture clips (SMPL-X, found via HumanML3D labels)
        │
        ▼
GMR retargeting (booster_k1 config)
        │
        ▼
K1 reference clips (one gesture first, then 5–10)
        │
        ▼
Train tracking policy (booster_mjlab K1 tracking task, PPO)
        │
        ▼
Evaluate each gesture (tracking RMSE, falls, training speed)
```

1. **Reproduce the baseline.** I'll run booster_mjlab's K1 tracking task unchanged on one of its example clips, so I know my setup works before I change anything.
2. **Get gesture data.** Search [AMASS](https://amass.is.tue.mpg.de/) using [HumanML3D](https://github.com/EricGuo5513/HumanML3D)'s text labels for 5–10 gestures (point, open palms, wave, shrug, nod). If one is missing, I'll record it on my phone and convert it with GVHMR, which GMR supports.
3. **Retarget to the K1** with GMR's existing `booster_k1` config.
4. **Train one gesture first** in mjlab's tracking task with PPO. Once it works, I'll expand to the full set.

## Success metrics

I'll count milestone 1 as done when every gesture plays through in simulation with no falls and low tracking error.

- **Falls:** zero across 50 full-clip rollouts of each gesture.
- **Tracking error:** per-joint RMSE between the robot and the reference, the same measure as the paper's Table 2. I'll use the paper's G1 arm numbers (about 0.02–0.09 rad) as a rough reference, not a hard target, since the K1 is a different robot.
- **Training speed:** training iterations until tracking error levels off, recorded as the baseline for the milestone 2 comparison.
- **Visual check:** the gestures still read as the intended gesture to a person watching.

## Risks and blockers

My biggest unknown is whether the existing K1 tracking code works for my gestures without much fixing.

| Risk | Why it matters | Fallback |
| --- | --- | --- |
| The K1 tracking code for mjlab may not work as-is | The only mjlab version, [booster_mjlab](https://github.com/IntelligentRoboticsLab/booster_mjlab), is a small project. Booster's official K1 tracking code ([booster_train](https://github.com/BoosterRobotics/booster_train)) is built for Isaac Lab, not mjlab | Port the K1 settings from Booster's official code; mjlab uses the same API as Isaac Lab |
| A gesture I want isn't in AMASS | AMASS is general motion, not conversation, so some gestures may be missing | Record it on my phone and convert it with GVHMR |
| No wrists or waist on the K1 | Some gestures lose their detail or look flat | Favor arm and head gestures (point, wave, nod); use the head as an added channel |
| Retargeted clips may be physically awkward | A much smaller body can produce self-collisions or poses it cannot balance | Inspect clips visually before training; drop bad ones |

## Timeline

I expect milestone 1 to take about four weeks, with one gesture working by the end of week 3.

1. **Week 1 (Oct 5):** Install booster_mjlab and run its K1 tracking task unchanged on one of its example clips. Start a run log.
2. **Week 2 (Oct 12):** Find gesture clips in AMASS, retarget one to the K1 with GMR, and check it in booster_mjlab's clip viewer.
3. **Week 3 (Oct 19):** Train tracking on that one gesture until the K1 performs it in sim without falling.
4. **Week 4+ (Oct 26):** Expand to 5–10 gestures, record tracking error and falls for each, and present the results to the club.

## Future work

Each later milestone builds on the tracking policy from milestone 1. I'd start milestone 2 by comparing default and residual actions.

1. **Text to gesture:** an LLM reads a sentence and picks which gestures to play and when, using the SeG gesture library.
2. **Speech in the loop:** microphone, speech-to-text, LLM reply, text-to-speech, with gestures timed to the audio, trained on BEAT2.
3. **Gesturing while walking:** legs follow a walking command while the arms gesture, building on [ExBody2](https://arxiv.org/abs/2412.13196).
4. **Gaze and presenting:** look at the listener, move around a stage, and give a short presentation.
5. **Sim to real:** deploy the gesture policy on the club's K1.

## References

- Peng et al., [DeepMimic](https://arxiv.org/abs/1804.02717), 2018
- Zhang, [Semantic Co-Speech Gesture Synthesis and Real-Time Control for Humanoid Robots](https://arxiv.org/abs/2512.17183), 2025
- [mjlab](https://github.com/mujocolab/mjlab)
- [booster_mjlab](https://github.com/IntelligentRoboticsLab/booster_mjlab) (K1 integration for mjlab)
- Booster Robotics, [booster_train](https://github.com/BoosterRobotics/booster_train) (official K1 training tasks, Isaac Lab)
- [GMR: General Motion Retargeting](https://github.com/YanjieZe/GMR)
- [AMASS](https://amass.is.tue.mpg.de/) and [HumanML3D](https://github.com/EricGuo5513/HumanML3D)
- Zhang et al., [Semantic Gesticulator and the SeG dataset](https://github.com/LuMen-ze/Semantic-Gesticulator-Official), 2024
- Liu et al., [EMAGE and the BEAT2 dataset](https://arxiv.org/html/2401.00374v4), CVPR 2024
- Booster Robotics, [K1 specifications](https://docs.booster.tech/docs/product-manual/k1/getting-started/specifications/)