# Gate 1 calibration

Generated 2026-10-18 by `tools/clip_qc.py` on `/home/boston/robotics/data/beat2_batch` (152 grounded clips). Each check's distribution over the batch, how many clips the plan's limit and the limit in `clip_qc.LIMITS` flag, and the flagged clips.

- **Format:** 0 clips with NaN/inf or the wrong joint count; fps [30.0]; max quaternion norm error 1.2e-15

| check | median | p95 | max | plan limit → clips | `LIMITS` → clips |
|---|---|---|---|---|---|
| largest one-frame joint step, rad | 0.129 | 0.356 | 1.57 | 0.3 → 11 | 0.6 → 4 |
| largest one-frame trunk move, cm | 0.41 | 0.881 | 4.35 | — | 3 → 1 |
| largest one-frame trunk turn, deg | 0.878 | 1.98 | 28.6 | — | 6 → 5 |
| fastest joint / its no-load speed (1 = at the limit, one frame) | 0.141 | 0.318 | 1.46 | — | — |
| longest time a joint is over its no-load speed, s | 0 | 0 | 0.0333 | 0.1 → 0 | 0.1 → 0 |
| share of frames with a joint past its torque knee point (less torque) | 0 | 0.0416 | 0.0836 | — | — |
| lowest collision point vs the floor, mm | -9.9e-05 | -9.99e-05 (p5) | -0.000101 | 5 → 0 | -5 → 0 |
| fastest planted-foot slide, cm/frame | 0.161 | 1.14 | 4.15 | 1 → 15 | 3 → 1 |
| longest planted-foot slide above 1 cm/frame, s | 0 | 0.0483 | 0.133 | — | 0.1 → 1 |
| total planted-foot slide over the clip, cm | 5.21 | 15.1 | 26.8 | — | — |
| longest self-overlap deeper than 5 mm (not hand on leg), s | 0 | 0 | 0 | 0.1 → 0 | 0.1 → 0 |
| deepest self-overlap (not hand on leg), mm | 0 | 0 | 0 | — | — |
| longest hand-into-leg overlap deeper than 5 mm, s (info) | 0 | 0 | 0.6 | 0.1 → 2 | 0.1 → 2 |
| root quaternion |norm - 1| | 1.1e-15 | 1.1e-15 | 1.2e-15 | 0.001 → 0 | 0.001 → 0 |

## Flagged clips (`LIMITS`)

Severe flags in **bold**. Older checks (joint limits, knees, feet, outliers) included for context.

| clip | flags |
|---|---|
| `wayne_0_9_9_t12-22` | **joint jump 0.92 rad (Left_Elbow_Pitch at 3.9 s)**; **root jump 4.4 cm/frame**; **root turn 26 deg/frame**; **right foot slides 4.2 cm in one frame (at 3.9 s)** |
| `lawrence_0_13_13_t42-52` | shoulder at limit 50%; **joint jump 1.17 rad (Right_Elbow_Pitch at 8.0 s)**; **root turn 14 deg/frame** |
| `nidal_0_3_3_t0-10` | shoulder at limit 8%; **joint jump 1.57 rad (Left_Elbow_Pitch at 0.8 s)**; **root turn 29 deg/frame** |
| `solomon_0_15_15_t21-31` | shoulder at limit 18%; **joint jump 1.26 rad (Right_Elbow_Pitch at 9.6 s)**; **root turn 18 deg/frame** |
| `ayana_0_12_12_t20-30` | **root turn 8 deg/frame** |
| `lawrence_0_3_3_t7-17` | **left foot slides > 1 cm/frame for 0.13 s (at 8.3 s)** |
| `lawrence_0_4_4_t1-11` | **outlier trunk drop (z +3.6)** |
| `wayne_0_10_10_t49-59` | **right arm behind body (human's in front)** |
| `ayana_0_12_12_t73-83` | elbow bend at limit 17% |
| `ayana_0_13_13_t38-48` | shoulder at limit 11% |
| `ayana_0_15_15_t72-82` | shoulder at limit 9% |
| `lawrence_0_10_10_t34-44` | shoulder at limit 7% |
| `lawrence_0_12_12_t26-36` | shoulder at limit 13% |
| `miranda_0_12_12_t3-13` | elbow bend at limit 7% |
| `scott_0_1_1_t34-44` | hand presses into leg 25 mm for 0.6 s (at 5.6 s) |
| `sophie_0_2_2_t45-55` | outlier knee max (z +4.8) |
| `wayne_0_11_11_t21-31` | outlier knee max (z -4.1) |
| `wayne_0_5_5_t31-41` | hand presses into leg 10 mm for 0.2 s (at 2.5 s) |

## Self-contacts by pair

| pair | clips touching | longest > 5 mm, s | deepest, mm |
|---|---|---|---|
| right_hand_collision / right_hip_roll_collision | 4 | 0.10 | 12 |
| left_hand_collision / left_hip_roll_collision | 3 | 0.03 | 6 |
| right_hand_end_collision / right_hip_yaw_collision | 3 | 0.10 | 22 |
| left_hand_end_collision / left_hip_yaw_collision | 2 | 0.60 | 25 |
| right_hand_end_collision / right_hip_roll_collision | 2 | 0.17 | 10 |
| left_hand_collision / left_hip_yaw_collision | 1 | 0.00 | 1 |

## Leakage: `/home/boston/robotics/data/beat2_batch/combined/beat2-10s-train.npz`

103 problem(s):
- 53 × val: scott_0_10_10_t31-41: val take 2_scott_0_10_10; wayne_0_10_10_t5-15: val take 1_wayne_0_10_10; wayne_0_11_11_t21-31: val take 1_wayne_0_11_11; wayne_0_11_11_t45-55: val take 1_wayne_0_11_11; wayne_0_12_12_t17-27: val take 1_wayne_0_12_12; wayne_0_12_12_t43-53: val take 1_wayne_0_12_12 …
- 50 × test: scott_0_1_1_t34-44: test take 2_scott_0_1_1; scott_0_5_5_t4-14: test take 2_scott_0_5_5; wayne_0_2_2_t25-35: test take 1_wayne_0_2_2; wayne_0_3_3_t28-38: test take 1_wayne_0_3_3; wayne_0_4_4_t52-62: test take 1_wayne_0_4_4; wayne_0_5_5_t8-18: test take 1_wayne_0_5_5 …
