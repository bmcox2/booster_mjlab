# BEAT2 Clip QC

Generated 2026-10-18 by `tools/beat2_batch.py` (10 s windows, top 2 per take, ankles within 10 cm). One row per clip; rerun the script to refresh.

- **Clips:** 152 (108 train, 44 held-out), **43 flagged**, 4 severe (**bold**); 4 left out of the artifacts (`--exclude severe`)
- **Train speakers:** 2_scott (3 clips), 1_wayne (25 clips), 3_solomon (14 clips), 4_lawrence (24 clips), 7_sophie (28 clips), 9_miranda (14 clips)
- **Held-out speakers:** 11_nidal (30 clips), 21_ayana (14 clips)
- **Takes with fewer windows:** 2_scott_0_10_10 (only 1 still window(s) of 46); 2_scott_0_11_11 (only 0 still window(s) of 38); 2_scott_0_12_12 (only 0 still window(s) of 81); 2_scott_0_13_13 (only 0 still window(s) of 63); 2_scott_0_14_14 (only 0 still window(s) of 76); 2_scott_0_15_15 (only 0 still window(s) of 82); 2_scott_0_1_1 (only 1 still window(s) of 54); 2_scott_0_2_2 (only 0 still window(s) of 52); 2_scott_0_3_3 (only 0 still window(s) of 58); 2_scott_0_4_4 (only 0 still window(s) of 57); 2_scott_0_5_5 (only 1 still window(s) of 67); 2_scott_0_6_6 (only 0 still window(s) of 73); 2_scott_0_7_7 (only 0 still window(s) of 60); 2_scott_0_8_8 (only 0 still window(s) of 68); 2_scott_0_9_9 (only 0 still window(s) of 46); 1_wayne_0_1_1 (only 0 still window(s) of 59); 1_wayne_0_2_2 (only 1 still window(s) of 63); 1_wayne_0_3_3 (only 1 still window(s) of 63); 1_wayne_0_4_4 (only 1 still window(s) of 62); 3_solomon_0_10_10 (only 1 still window(s) of 56); 3_solomon_0_11_11 (only 0 still window(s) of 65); 3_solomon_0_12_12 (only 0 still window(s) of 75); 3_solomon_0_13_13 (only 1 still window(s) of 69); 3_solomon_0_14_14 (only 0 still window(s) of 73); 3_solomon_0_2_2 (only 0 still window(s) of 85); 3_solomon_0_3_3 (only 0 still window(s) of 68); 3_solomon_0_4_4 (only 0 still window(s) of 73); 3_solomon_0_9_9 (only 0 still window(s) of 63); 4_lawrence_0_10_10 (only 1 still window(s) of 55); 4_lawrence_0_14_14 (only 1 still window(s) of 82); 4_lawrence_0_3_3 (only 1 still window(s) of 75); 4_lawrence_0_5_5 (only 1 still window(s) of 89); 4_lawrence_0_9_9 (only 0 still window(s) of 63); 7_sophie_0_2_2 (only 1 still window(s) of 53); 7_sophie_0_3_3 (only 1 still window(s) of 52)
- **train artifact:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-10s-train:v3`
- **heldout artifact:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-10s-heldout:v3`

## Per speaker

| split | speaker | takes | clips | flagged | severe | head at limit | shoulder at limit | upper-arm twist | other |
|---|---|---|---|---|---|---|---|---|---|
| train | 2_scott | 15 | 3 | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) |
| train | 1_wayne | 15 | 25 | 7 (28%) | 1 (4%) | 0 (0%) | 0 (0%) | 0 (0%) | 7 (28%) |
| train | 3_solomon | 15 | 14 | 1 (7%) | 1 (7%) | 1 (7%) | 1 (7%) | 0 (0%) | 1 (7%) |
| train | 4_lawrence | 15 | 24 | 3 (12%) | 1 (4%) | 0 (0%) | 3 (12%) | 0 (0%) | 1 (4%) |
| train | 7_sophie | 15 | 28 | 11 (39%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 11 (39%) |
| train | 9_miranda | 7 | 14 | 2 (14%) | 0 (0%) | 0 (0%) | 0 (0%) | 0 (0%) | 2 (14%) |
| heldout | 11_nidal | 15 | 30 | 14 (47%) | 1 (3%) | 0 (0%) | 1 (3%) | 0 (0%) | 14 (47%) |
| heldout | 21_ayana | 7 | 14 | 5 (36%) | 0 (0%) | 3 (21%) | 2 (14%) | 0 (0%) | 1 (7%) |

## Columns
- **feet human / K1 (cm):** farthest an ankle (human, BEAT2) / foot (K1, after ground_clip) strays from its median spot
- **arms human / K1 (cm/s):** mean wrist speed relative to the pelvis (human) / hand speed relative to the trunk (K1)
- **trunk drop (cm):** K1 trunk height range over the clip
- **knees L / R (deg):** K1 knee angle range (0 = straight, limit 128)
- **joint limits:** share of frames with a joint within 1° of a limit, by group. *upper-arm twist*: with a straight arm, twist doesn't move the hand, so GMR's IK drifts to the limit (hand is right, arm is twisted); *head*: the speaker looks further than the K1 can, so nods are clipped; *shoulder* / *leg*: pose clipped. A straight elbow (elbow bend at 0) is normal and not counted

## Flags
Fixed: K1 feet > 8 cm, trunk drop > 5 cm, knee > 60°, a joint group at its limit > 5% of frames, K1 hands < 5 cm/s, any ground_clip IK failure. Clips that trained to 50/50 so far: K1 feet ≤ 1.8 cm, trunk ≤ 1.8 cm, knees 14–36°, 0 limit frames, hands 8–16 cm/s.
Outlier: more than 3.5 robust SDs (median / MAD) from this batch on arms, trunk, or knee (not feet: most clips move ~1 cm with a long tail of normal weight shifts; the fixed limit covers feet).
**Severe** (dropped by `--exclude severe`): upper-arm twist at its limit on > 50% of frames, any ground_clip IK failure, a trunk-drop outlier, or an arm on the wrong side (K1 hand > 5 cm behind the trunk while the human's wrist is > 5 cm in front), or a joint jump (a joint moving > 0.6 rad in one 1/30 s frame: GMR's IK flipping, the hand reference teleports). Head or shoulder held at a limit is not severe: the clipped pose is still valid K1 motion.

| split | clip | source | feet human / K1 (cm) | arms human / K1 (cm/s) | trunk drop (cm) | knees L / R (deg) | joint limits | flags |
|---|---|---|---|---|---|---|---|---|
| train | `scott_0_10_10_t31-41` | 2_scott_0_10_10 31–41 s | 6.5 / 1.4 | 46 / 13 | 1.4 | 14–35 / 15–43 | 0 | — |
| train | `scott_0_1_1_t34-44` | 2_scott_0_1_1 34–44 s | 3.7 / 1.8 | 61 / 16 | 1.5 | 19–40 / 15–25 | 0 | — |
| train | `scott_0_5_5_t4-14` | 2_scott_0_5_5 4–14 s | 0.7 / 0.6 | 43 / 11 | 0.6 | 21–36 / 14–16 | 0 | — |
| train | `wayne_0_10_10_t49-59` | 1_wayne_0_10_10 49–59 s | 0.3 / 0.4 | 13 / 5 | 0.3 | 18–27 / 30–34 | 0 | — |
| train | `wayne_0_10_10_t5-15` | 1_wayne_0_10_10 5–15 s | 0.8 / 0.3 | 10 / 3 | 0.3 | 14–23 / 29–35 | 0 | little arm motion |
| train | `wayne_0_11_11_t21-31` | 1_wayne_0_11_11 21–31 s | 0.2 / 0.2 | 16 / 6 | 0.1 | 14–21 / 18–23 | 0 | outlier knee max (z -3.9) |
| train | `wayne_0_11_11_t45-55` | 1_wayne_0_11_11 45–55 s | 0.3 / 0.2 | 16 / 6 | 0.1 | 29–32 / 18–21 | 0 | — |
| train | `wayne_0_12_12_t17-27` | 1_wayne_0_12_12 17–27 s | 4.4 / 0.8 | 22 / 8 | 0.4 | 15–23 / 28–35 | 0 | — |
| train | `wayne_0_12_12_t43-53` | 1_wayne_0_12_12 43–53 s | 9.9 / 6.9 | 20 / 8 | 0.9 | 26–35 / 16–22 | 0 | — |
| train | `wayne_0_13_13_t45-55` | 1_wayne_0_13_13 45–55 s | 7.8 / 3.8 | 22 / 7 | 0.9 | 21–30 / 18–31 | 0 | — |
| train | `wayne_0_13_13_t34-44` | 1_wayne_0_13_13 34–44 s | 1.6 / 0.7 | 20 / 8 | 0.8 | 29–34 / 15–28 | 0 | — |
| train | `wayne_0_14_14_t44-54` | 1_wayne_0_14_14 44–54 s | 0.3 / 1.0 | 19 / 5 | 0.5 | 15–24 / 28–32 | 0 | little arm motion |
| train | `wayne_0_14_14_t30-40` | 1_wayne_0_14_14 30–40 s | 4.3 / 2.5 | 12 / 5 | 0.5 | 22–30 / 16–26 | 0 | little arm motion |
| train | `wayne_0_15_15_t60-70` | 1_wayne_0_15_15 60–70 s | 6.3 / 4.4 | 19 / 8 | 0.4 | 28–34 / 17–25 | 0 | — |
| train | `wayne_0_15_15_t9-19` | 1_wayne_0_15_15 9–19 s | 3.5 / 1.7 | 12 / 5 | 0.6 | 14–30 / 25–33 | 0 | — |
| train | `wayne_0_2_2_t25-35` | 1_wayne_0_2_2 25–35 s | 9.5 / 1.5 | 23 / 8 | 1.3 | 17–30 / 21–36 | 0 | — |
| train | `wayne_0_3_3_t28-38` | 1_wayne_0_3_3 28–38 s | 6.6 / 3.6 | 13 / 5 | 1.0 | 23–35 / 14–26 | 0 | little arm motion |
| train | `wayne_0_4_4_t52-62` | 1_wayne_0_4_4 52–62 s | 1.6 / 1.4 | 15 / 5 | 0.3 | 15–26 / 31–36 | 0 | — |
| train | `wayne_0_5_5_t8-18` | 1_wayne_0_5_5 8–18 s | 5.1 / 1.6 | 41 / 12 | 0.8 | 23–36 / 14–32 | 0 | — |
| train | `wayne_0_5_5_t31-41` | 1_wayne_0_5_5 31–41 s | 8.6 / 4.5 | 28 / 11 | 0.7 | 24–35 / 15–30 | 0 | — |
| train | `wayne_0_6_6_t29-39` | 1_wayne_0_6_6 29–39 s | 0.3 / 0.2 | 20 / 7 | 0.2 | 30–35 / 19–23 | 0 | — |
| train | `wayne_0_6_6_t46-56` | 1_wayne_0_6_6 46–56 s | 1.0 / 0.5 | 15 / 5 | 1.0 | 27–34 / 19–28 | 0 | little arm motion |
| train | `wayne_0_7_7_t47-57` | 1_wayne_0_7_7 47–57 s | 6.6 / 1.6 | 17 / 7 | 1.0 | 18–35 / 15–35 | 0 | — |
| train | `wayne_0_7_7_t36-46` | 1_wayne_0_7_7 36–46 s | 2.5 / 0.7 | 14 / 6 | 1.1 | 30–35 / 17–27 | 0 | — |
| train | `wayne_0_8_8_t3-13` | 1_wayne_0_8_8 3–13 s | 1.1 / 0.5 | 18 / 7 | 1.2 | 25–33 / 17–30 | 0 | — |
| train | `wayne_0_8_8_t46-56` | 1_wayne_0_8_8 46–56 s | 0.4 / 0.2 | 14 / 6 | 0.5 | 26–33 / 19–31 | 0 | — |
| train | `wayne_0_9_9_t48-58` | 1_wayne_0_9_9 48–58 s | 0.5 / 0.3 | 17 / 6 | 0.2 | 28–30 / 17–22 | 0 | — |
| train | `wayne_0_9_9_t12-22` | 1_wayne_0_9_9 12–22 s | 6.5 / 4.8 | 9 / 5 | 0.9 | 14–35 / 26–32 | 0 | little arm motion; **joint jump 0.93 rad (Left_Shoulder_Roll at 3.9 s)** *(excluded)* |
| train | `solomon_0_10_10_t18-28` | 3_solomon_0_10_10 18–28 s | 5.5 / 2.7 | 40 / 10 | 1.2 | 14–35 / 14–25 | 0 | — |
| train | `solomon_0_13_13_t3-13` | 3_solomon_0_13_13 3–13 s | 6.1 / 4.2 | 69 / 17 | 0.9 | 14–35 / 15–32 | 0 | — |
| train | `solomon_0_15_15_t21-31` | 3_solomon_0_15_15 21–31 s | 8.5 / 6.2 | 62 / 19 | 3.1 | 16–42 / 14–28 | shoulder 16%, head 6% | head at limit 6%; shoulder at limit 16%; outlier arms k1 cm (z +3.7); **joint jump 0.93 rad (Right_Elbow_Pitch at 9.6 s)** *(excluded)* |
| train | `solomon_0_15_15_t43-53` | 3_solomon_0_15_15 43–53 s | 8.0 / 4.9 | 53 / 14 | 1.6 | 14–39 / 16–38 | 0 | — |
| train | `solomon_0_1_1_t18-28` | 3_solomon_0_1_1 18–28 s | 7.6 / 4.5 | 59 / 16 | 1.4 | 14–35 / 15–32 | 0 | — |
| train | `solomon_0_1_1_t56-66` | 3_solomon_0_1_1 56–66 s | 9.8 / 6.0 | 29 / 9 | 1.8 | 14–36 / 14–36 | 0 | — |
| train | `solomon_0_5_5_t32-42` | 3_solomon_0_5_5 32–42 s | 2.9 / 1.9 | 51 / 12 | 0.8 | 15–35 / 14–23 | 0 | — |
| train | `solomon_0_5_5_t6-16` | 3_solomon_0_5_5 6–16 s | 9.8 / 6.1 | 39 / 10 | 1.5 | 14–35 / 15–32 | 0 | — |
| train | `solomon_0_6_6_t20-30` | 3_solomon_0_6_6 20–30 s | 9.4 / 5.1 | 45 / 13 | 1.2 | 14–35 / 15–35 | 0 | — |
| train | `solomon_0_6_6_t59-69` | 3_solomon_0_6_6 59–69 s | 7.2 / 4.6 | 29 / 7 | 1.5 | 14–36 / 15–31 | 0 | — |
| train | `solomon_0_7_7_t13-23` | 3_solomon_0_7_7 13–23 s | 9.3 / 5.9 | 35 / 9 | 1.2 | 14–35 / 15–32 | 0 | — |
| train | `solomon_0_7_7_t3-13` | 3_solomon_0_7_7 3–13 s | 10.0 / 6.4 | 32 / 10 | 1.1 | 14–38 / 14–28 | 0 | — |
| train | `solomon_0_8_8_t72-82` | 3_solomon_0_8_8 72–82 s | 9.5 / 2.1 | 43 / 12 | 3.1 | 14–38 / 14–41 | 0 | — |
| train | `solomon_0_8_8_t5-15` | 3_solomon_0_8_8 5–15 s | 9.0 / 4.6 | 23 / 6 | 1.0 | 16–35 / 14–19 | 0 | — |
| train | `lawrence_0_10_10_t34-44` | 4_lawrence_0_10_10 34–44 s | 9.5 / 5.7 | 37 / 13 | 2.3 | 17–38 / 15–36 | shoulder 7% | shoulder at limit 7% |
| train | `lawrence_0_11_11_t18-28` | 4_lawrence_0_11_11 18–28 s | 4.8 / 2.0 | 36 / 15 | 2.4 | 15–38 / 15–31 | 0 | — |
| train | `lawrence_0_11_11_t57-67` | 4_lawrence_0_11_11 57–67 s | 9.4 / 5.6 | 34 / 9 | 2.6 | 15–38 / 15–38 | 0 | — |
| train | `lawrence_0_12_12_t12-22` | 4_lawrence_0_12_12 12–22 s | 5.3 / 2.2 | 37 / 14 | 2.5 | 23–35 / 17–33 | 0 | — |
| train | `lawrence_0_12_12_t26-36` | 4_lawrence_0_12_12 26–36 s | 2.4 / 1.5 | 33 / 11 | 1.5 | 16–35 / 26–38 | shoulder 14% | shoulder at limit 14% |
| train | `lawrence_0_13_13_t42-52` | 4_lawrence_0_13_13 42–52 s | 9.9 / 4.4 | 38 / 12 | 1.8 | 15–40 / 15–38 | shoulder 36% | shoulder at limit 36%; **joint jump 1.18 rad (Right_Elbow_Pitch at 8.0 s)** *(excluded)* |
| train | `lawrence_0_13_13_t21-31` | 4_lawrence_0_13_13 21–31 s | 9.5 / 5.1 | 32 / 14 | 2.6 | 17–36 / 14–36 | 0 | — |
| train | `lawrence_0_14_14_t7-17` | 4_lawrence_0_14_14 7–17 s | 9.8 / 5.6 | 32 / 12 | 2.0 | 19–35 / 14–25 | 0 | — |
| train | `lawrence_0_15_15_t65-75` | 4_lawrence_0_15_15 65–75 s | 2.1 / 0.7 | 34 / 11 | 1.9 | 24–37 / 17–25 | 0 | — |
| train | `lawrence_0_15_15_t26-36` | 4_lawrence_0_15_15 26–36 s | 5.9 / 1.1 | 33 / 12 | 1.8 | 15–39 / 15–37 | 0 | — |
| train | `lawrence_0_1_1_t32-42` | 4_lawrence_0_1_1 32–42 s | 3.0 / 2.2 | 30 / 12 | 2.0 | 25–36 / 17–31 | 0 | — |
| train | `lawrence_0_1_1_t9-19` | 4_lawrence_0_1_1 9–19 s | 9.7 / 4.3 | 24 / 9 | 2.0 | 19–40 / 15–31 | 0 | — |
| train | `lawrence_0_2_2_t38-48` | 4_lawrence_0_2_2 38–48 s | 9.0 / 5.1 | 25 / 10 | 2.0 | 23–38 / 14–27 | 0 | — |
| train | `lawrence_0_2_2_t14-24` | 4_lawrence_0_2_2 14–24 s | 6.6 / 4.0 | 24 / 10 | 1.8 | 24–38 / 15–28 | 0 | — |
| train | `lawrence_0_3_3_t7-17` | 4_lawrence_0_3_3 7–17 s | 9.1 / 4.7 | 25 / 10 | 1.8 | 16–42 / 15–29 | 0 | — |
| train | `lawrence_0_4_4_t1-11` | 4_lawrence_0_4_4 1–11 s | 9.5 / 5.2 | 31 / 12 | 3.2 | 17–45 / 15–35 | 0 | — |
| train | `lawrence_0_4_4_t45-55` | 4_lawrence_0_4_4 45–55 s | 5.9 / 3.6 | 30 / 12 | 2.6 | 27–42 / 15–31 | 0 | — |
| train | `lawrence_0_5_5_t27-37` | 4_lawrence_0_5_5 27–37 s | 1.1 / 0.6 | 22 / 9 | 1.3 | 20–38 / 15–29 | 0 | — |
| train | `lawrence_0_6_6_t71-81` | 4_lawrence_0_6_6 71–81 s | 7.4 / 4.1 | 36 / 12 | 0.6 | 16–34 / 15–36 | 0 | — |
| train | `lawrence_0_6_6_t41-51` | 4_lawrence_0_6_6 41–51 s | 9.0 / 5.3 | 34 / 14 | 2.3 | 22–38 / 14–30 | 0 | — |
| train | `lawrence_0_7_7_t9-19` | 4_lawrence_0_7_7 9–19 s | 6.9 / 4.4 | 34 / 13 | 2.0 | 18–36 / 15–29 | 0 | — |
| train | `lawrence_0_7_7_t53-63` | 4_lawrence_0_7_7 53–63 s | 0.5 / 0.6 | 28 / 10 | 0.7 | 29–38 / 16–25 | 0 | — |
| train | `lawrence_0_8_8_t78-88` | 4_lawrence_0_8_8 78–88 s | 3.6 / 0.9 | 29 / 9 | 2.5 | 26–37 / 15–29 | 0 | — |
| train | `lawrence_0_8_8_t50-60` | 4_lawrence_0_8_8 50–60 s | 1.8 / 1.1 | 27 / 12 | 1.5 | 21–36 / 24–38 | 0 | — |
| train | `sophie_0_10_10_t43-53` | 7_sophie_0_10_10 43–53 s | 3.4 / 2.4 | 21 / 5 | 1.8 | 19–34 / 16–35 | 0 | — |
| train | `sophie_0_10_10_t32-42` | 7_sophie_0_10_10 32–42 s | 1.5 / 0.5 | 20 / 5 | 1.1 | 18–34 / 16–35 | 0 | — |
| train | `sophie_0_11_11_t30-40` | 7_sophie_0_11_11 30–40 s | 1.3 / 0.6 | 19 / 6 | 0.6 | 15–27 / 21–35 | 0 | — |
| train | `sophie_0_11_11_t5-15` | 7_sophie_0_11_11 5–15 s | 1.2 / 0.4 | 17 / 5 | 0.2 | 15–26 / 24–32 | 0 | — |
| train | `sophie_0_12_12_t3-13` | 7_sophie_0_12_12 3–13 s | 1.5 / 0.5 | 26 / 7 | 0.8 | 15–25 / 23–35 | 0 | — |
| train | `sophie_0_12_12_t15-25` | 7_sophie_0_12_12 15–25 s | 5.8 / 2.7 | 24 / 7 | 0.8 | 15–32 / 15–35 | 0 | — |
| train | `sophie_0_13_13_t48-58` | 7_sophie_0_13_13 48–58 s | 1.8 / 0.3 | 21 / 6 | 1.0 | 20–33 / 16–35 | 0 | — |
| train | `sophie_0_13_13_t34-44` | 7_sophie_0_13_13 34–44 s | 0.9 / 0.4 | 19 / 5 | 0.5 | 17–30 / 16–35 | 0 | — |
| train | `sophie_0_14_14_t52-62` | 7_sophie_0_14_14 52–62 s | 1.2 / 0.4 | 24 / 6 | 0.4 | 18–32 / 22–34 | 0 | — |
| train | `sophie_0_14_14_t7-17` | 7_sophie_0_14_14 7–17 s | 1.5 / 0.5 | 21 / 6 | 0.5 | 17–32 / 19–35 | 0 | — |
| train | `sophie_0_15_15_t24-34` | 7_sophie_0_15_15 24–34 s | 1.5 / 0.6 | 21 / 6 | 0.6 | 15–27 / 19–36 | 0 | — |
| train | `sophie_0_15_15_t53-63` | 7_sophie_0_15_15 53–63 s | 0.6 / 0.3 | 21 / 5 | 0.3 | 14–29 / 15–27 | 0 | — |
| train | `sophie_0_1_1_t19-29` | 7_sophie_0_1_1 19–29 s | 0.6 / 0.2 | 21 / 6 | 0.4 | 15–24 / 25–32 | 0 | — |
| train | `sophie_0_1_1_t45-55` | 7_sophie_0_1_1 45–55 s | 2.9 / 0.6 | 19 / 5 | 0.9 | 15–35 / 14–35 | 0 | little arm motion |
| train | `sophie_0_2_2_t45-55` | 7_sophie_0_2_2 45–55 s | 9.3 / 2.1 | 15 / 5 | 1.4 | 15–47 / 16–35 | 0 | outlier knee max (z +4.0) |
| train | `sophie_0_3_3_t0-10` | 7_sophie_0_3_3 0–10 s | 9.3 / 3.2 | 14 / 4 | 1.0 | 14–38 / 14–35 | 0 | little arm motion |
| train | `sophie_0_4_4_t52-62` | 7_sophie_0_4_4 52–62 s | 8.4 / 4.7 | 18 / 5 | 0.9 | 15–41 / 17–35 | 0 | little arm motion |
| train | `sophie_0_4_4_t31-41` | 7_sophie_0_4_4 31–41 s | 1.4 / 0.4 | 16 / 5 | 0.9 | 17–31 / 21–35 | 0 | little arm motion |
| train | `sophie_0_5_5_t27-37` | 7_sophie_0_5_5 27–37 s | 1.2 / 0.4 | 19 / 5 | 0.9 | 16–32 / 15–35 | 0 | — |
| train | `sophie_0_5_5_t59-69` | 7_sophie_0_5_5 59–69 s | 1.6 / 0.6 | 18 / 5 | 0.4 | 16–35 / 19–35 | 0 | — |
| train | `sophie_0_6_6_t24-34` | 7_sophie_0_6_6 24–34 s | 5.9 / 3.3 | 18 / 5 | 0.8 | 14–38 / 14–36 | 0 | — |
| train | `sophie_0_6_6_t47-57` | 7_sophie_0_6_6 47–57 s | 9.1 / 5.1 | 18 / 4 | 1.3 | 15–31 / 15–35 | 0 | little arm motion |
| train | `sophie_0_7_7_t38-48` | 7_sophie_0_7_7 38–48 s | 1.5 / 0.5 | 18 / 5 | 0.9 | 15–29 / 16–35 | 0 | little arm motion |
| train | `sophie_0_7_7_t16-26` | 7_sophie_0_7_7 16–26 s | 1.1 / 0.5 | 16 / 4 | 1.5 | 17–35 / 17–26 | 0 | little arm motion |
| train | `sophie_0_8_8_t14-24` | 7_sophie_0_8_8 14–24 s | 1.1 / 0.5 | 21 / 6 | 0.6 | 18–30 / 23–36 | 0 | — |
| train | `sophie_0_8_8_t45-55` | 7_sophie_0_8_8 45–55 s | 0.6 / 0.2 | 18 / 5 | 0.2 | 20–23 / 29–35 | 0 | little arm motion |
| train | `sophie_0_9_9_t9-19` | 7_sophie_0_9_9 9–19 s | 2.7 / 1.4 | 18 / 5 | 1.2 | 15–31 / 14–36 | 0 | little arm motion |
| train | `sophie_0_9_9_t38-48` | 7_sophie_0_9_9 38–48 s | 1.1 / 0.4 | 17 / 5 | 0.5 | 17–34 / 15–35 | 0 | little arm motion |
| train | `miranda_0_10_10_t12-22` | 9_miranda_0_10_10 12–22 s | 0.4 / 0.5 | 31 / 9 | 0.4 | 14–28 / 14–35 | 0 | — |
| train | `miranda_0_10_10_t23-33` | 9_miranda_0_10_10 23–33 s | 1.1 / 0.6 | 25 / 7 | 1.1 | 15–27 / 16–32 | 0 | — |
| train | `miranda_0_11_11_t7-17` | 9_miranda_0_11_11 7–17 s | 1.8 / 0.6 | 27 / 8 | 1.1 | 14–20 / 14–35 | 0 | — |
| train | `miranda_0_11_11_t43-53` | 9_miranda_0_11_11 43–53 s | 0.4 / 0.4 | 26 / 9 | 0.2 | 15–30 / 22–35 | 0 | — |
| train | `miranda_0_12_12_t3-13` | 9_miranda_0_12_12 3–13 s | 4.6 / 2.1 | 62 / 16 | 1.3 | 16–35 / 16–28 | elbow bend 7% | elbow bend at limit 7% |
| train | `miranda_0_12_12_t59-69` | 9_miranda_0_12_12 59–69 s | 0.3 / 0.4 | 47 / 13 | 0.3 | 14–27 / 26–34 | elbow bend 1% | — |
| train | `miranda_0_13_13_t25-35` | 9_miranda_0_13_13 25–35 s | 1.4 / 0.7 | 49 / 18 | 0.4 | 14–25 / 27–33 | elbow bend 3% | outlier arms k1 cm (z +3.5) |
| train | `miranda_0_13_13_t12-22` | 9_miranda_0_13_13 12–22 s | 1.5 / 0.7 | 33 / 12 | 0.5 | 15–24 / 26–34 | 0 | — |
| train | `miranda_0_14_14_t3-13` | 9_miranda_0_14_14 3–13 s | 4.2 / 2.8 | 31 / 9 | 0.8 | 18–33 / 23–33 | 0 | — |
| train | `miranda_0_14_14_t24-34` | 9_miranda_0_14_14 24–34 s | 0.8 / 0.4 | 26 / 8 | 0.8 | 15–28 / 23–33 | 0 | — |
| train | `miranda_0_15_15_t17-27` | 9_miranda_0_15_15 17–27 s | 0.4 / 0.3 | 27 / 8 | 0.2 | 19–33 / 14–30 | 0 | — |
| train | `miranda_0_15_15_t35-45` | 9_miranda_0_15_15 35–45 s | 0.8 / 0.4 | 20 / 6 | 0.7 | 15–31 / 26–35 | 0 | — |
| train | `miranda_0_9_9_t0-10` | 9_miranda_0_9_9 0–10 s | 7.3 / 4.7 | 47 / 13 | 1.9 | 14–40 / 14–34 | leg 3% | — |
| train | `miranda_0_9_9_t40-50` | 9_miranda_0_9_9 40–50 s | 1.1 / 0.5 | 29 / 10 | 0.7 | 15–35 / 16–29 | 0 | — |
| heldout | `nidal_0_10_10_t73-83` | 11_nidal_0_10_10 73–83 s | 5.5 / 2.8 | 19 / 6 | 0.8 | 18–35 / 16–25 | 0 | — |
| heldout | `nidal_0_10_10_t43-53` | 11_nidal_0_10_10 43–53 s | 0.6 / 0.4 | 18 / 5 | 0.3 | 21–29 / 17–25 | 0 | little arm motion |
| heldout | `nidal_0_11_11_t35-45` | 11_nidal_0_11_11 35–45 s | 0.6 / 0.3 | 20 / 5 | 0.2 | 21–28 / 15–23 | 0 | little arm motion |
| heldout | `nidal_0_11_11_t57-67` | 11_nidal_0_11_11 57–67 s | 0.8 / 0.3 | 18 / 3 | 0.2 | 24–28 / 16–23 | 0 | little arm motion |
| heldout | `nidal_0_12_12_t49-59` | 11_nidal_0_12_12 49–59 s | 1.0 / 0.5 | 22 / 5 | 0.4 | 27–33 / 16–30 | 0 | little arm motion |
| heldout | `nidal_0_12_12_t64-74` | 11_nidal_0_12_12 64–74 s | 1.3 / 1.5 | 19 / 6 | 0.6 | 19–33 / 23–33 | 0 | — |
| heldout | `nidal_0_13_13_t98-108` | 11_nidal_0_13_13 98–108 s | 2.3 / 0.8 | 22 / 7 | 1.2 | 21–35 / 15–30 | 0 | — |
| heldout | `nidal_0_13_13_t8-18` | 11_nidal_0_13_13 8–18 s | 1.2 / 0.5 | 20 / 4 | 0.3 | 24–30 / 15–25 | 0 | little arm motion |
| heldout | `nidal_0_14_14_t81-91` | 11_nidal_0_14_14 81–91 s | 2.4 / 2.0 | 25 / 8 | 0.9 | 16–35 / 19–34 | 0 | — |
| heldout | `nidal_0_14_14_t28-38` | 11_nidal_0_14_14 28–38 s | 1.2 / 0.5 | 22 / 5 | 0.2 | 23–30 / 16–26 | 0 | — |
| heldout | `nidal_0_15_15_t55-65` | 11_nidal_0_15_15 55–65 s | 1.1 / 0.5 | 24 / 5 | 0.2 | 24–29 / 15–24 | 0 | — |
| heldout | `nidal_0_15_15_t4-14` | 11_nidal_0_15_15 4–14 s | 0.2 / 0.3 | 19 / 4 | 0.1 | 25–30 / 15–20 | 0 | little arm motion |
| heldout | `nidal_0_1_1_t61-71` | 11_nidal_0_1_1 61–71 s | 1.4 / 1.1 | 25 / 6 | 1.2 | 20–36 / 14–28 | 0 | — |
| heldout | `nidal_0_1_1_t14-24` | 11_nidal_0_1_1 14–24 s | 1.2 / 0.3 | 20 / 6 | 0.3 | 15–26 / 20–31 | 0 | — |
| heldout | `nidal_0_2_2_t51-61` | 11_nidal_0_2_2 51–61 s | 0.8 / 0.4 | 19 / 6 | 0.2 | 24–29 / 16–22 | 0 | — |
| heldout | `nidal_0_2_2_t63-73` | 11_nidal_0_2_2 63–73 s | 0.9 / 0.5 | 19 / 7 | 0.3 | 32–35 / 15–25 | 0 | — |
| heldout | `nidal_0_3_3_t0-10` | 11_nidal_0_3_3 0–10 s | 8.5 / 4.8 | 18 / 7 | 0.9 | 26–36 / 15–32 | shoulder 8% | shoulder at limit 8%; **joint jump 1.52 rad (Left_Elbow_Pitch at 0.8 s)** *(excluded)* |
| heldout | `nidal_0_3_3_t41-51` | 11_nidal_0_3_3 41–51 s | 1.1 / 0.5 | 17 / 5 | 0.2 | 21–26 / 15–26 | 0 | little arm motion |
| heldout | `nidal_0_4_4_t10-20` | 11_nidal_0_4_4 10–20 s | 0.7 / 0.3 | 18 / 5 | 0.2 | 26–32 / 17–24 | 0 | — |
| heldout | `nidal_0_4_4_t0-10` | 11_nidal_0_4_4 0–10 s | 3.2 / 2.3 | 16 / 5 | 0.7 | 23–35 / 15–27 | 0 | little arm motion |
| heldout | `nidal_0_5_5_t59-69` | 11_nidal_0_5_5 59–69 s | 1.2 / 0.5 | 24 / 6 | 0.2 | 15–30 / 16–30 | 0 | — |
| heldout | `nidal_0_5_5_t24-34` | 11_nidal_0_5_5 24–34 s | 1.7 / 0.7 | 23 / 7 | 0.3 | 20–28 / 16–27 | 0 | — |
| heldout | `nidal_0_6_6_t27-37` | 11_nidal_0_6_6 27–37 s | 0.3 / 0.3 | 17 / 5 | 0.2 | 26–31 / 15–24 | 0 | little arm motion |
| heldout | `nidal_0_6_6_t83-93` | 11_nidal_0_6_6 83–93 s | 1.2 / 0.4 | 16 / 4 | 0.3 | 31–33 / 15–25 | 0 | little arm motion |
| heldout | `nidal_0_7_7_t21-31` | 11_nidal_0_7_7 21–31 s | 0.5 / 0.4 | 18 / 4 | 0.2 | 27–31 / 15–23 | 0 | little arm motion |
| heldout | `nidal_0_7_7_t66-76` | 11_nidal_0_7_7 66–76 s | 0.2 / 0.3 | 18 / 5 | 0.1 | 28–33 / 15–22 | 0 | little arm motion |
| heldout | `nidal_0_8_8_t90-100` | 11_nidal_0_8_8 90–100 s | 0.5 / 0.5 | 18 / 6 | 0.4 | 29–34 / 15–26 | 0 | — |
| heldout | `nidal_0_8_8_t40-50` | 11_nidal_0_8_8 40–50 s | 0.2 / 0.2 | 17 / 5 | 0.1 | 29–32 / 15–20 | 0 | little arm motion |
| heldout | `nidal_0_9_9_t0-10` | 11_nidal_0_9_9 0–10 s | 5.6 / 2.9 | 20 / 5 | 1.1 | 20–35 / 15–24 | 0 | — |
| heldout | `nidal_0_9_9_t59-69` | 11_nidal_0_9_9 59–69 s | 0.5 / 0.4 | 19 / 7 | 0.4 | 18–27 / 16–24 | 0 | — |
| heldout | `ayana_0_10_10_t51-61` | 21_ayana_0_10_10 51–61 s | 0.4 / 0.5 | 36 / 13 | 0.7 | 14–23 / 15–38 | 0 | — |
| heldout | `ayana_0_10_10_t14-24` | 21_ayana_0_10_10 14–24 s | 0.3 / 0.3 | 20 / 5 | 0.2 | 14–22 / 15–35 | 0 | — |
| heldout | `ayana_0_11_11_t20-30` | 21_ayana_0_11_11 20–30 s | 1.2 / 1.4 | 31 / 8 | 0.9 | 14–30 / 19–32 | 0 | — |
| heldout | `ayana_0_11_11_t58-68` | 21_ayana_0_11_11 58–68 s | 0.9 / 1.1 | 24 / 9 | 1.2 | 15–24 / 25–33 | head 9%, elbow bend 3% | head at limit 9% |
| heldout | `ayana_0_12_12_t20-30` | 21_ayana_0_12_12 20–30 s | 0.6 / 0.6 | 40 / 13 | 0.3 | 14–25 / 26–35 | head 5% | — |
| heldout | `ayana_0_12_12_t73-83` | 21_ayana_0_12_12 73–83 s | 9.1 / 3.8 | 40 / 11 | 0.4 | 14–20 / 24–35 | elbow bend 18% | elbow bend at limit 18% |
| heldout | `ayana_0_13_13_t56-66` | 21_ayana_0_13_13 56–66 s | 0.4 / 0.2 | 34 / 9 | 0.1 | 14–26 / 24–31 | head 6% | head at limit 6% |
| heldout | `ayana_0_13_13_t38-48` | 21_ayana_0_13_13 38–48 s | 1.5 / 1.0 | 33 / 8 | 1.6 | 14–29 / 26–37 | head 12%, shoulder 11% | head at limit 12%; shoulder at limit 11% |
| heldout | `ayana_0_14_14_t36-46` | 21_ayana_0_14_14 36–46 s | 1.5 / 0.8 | 39 / 11 | 0.6 | 14–25 / 24–31 | 0 | — |
| heldout | `ayana_0_14_14_t24-34` | 21_ayana_0_14_14 24–34 s | 2.0 / 1.1 | 29 / 8 | 0.3 | 14–24 / 25–31 | elbow bend 3% | — |
| heldout | `ayana_0_15_15_t72-82` | 21_ayana_0_15_15 72–82 s | 1.0 / 0.7 | 30 / 9 | 1.0 | 14–33 / 24–36 | shoulder 8% | shoulder at limit 8% |
| heldout | `ayana_0_15_15_t21-31` | 21_ayana_0_15_15 21–31 s | 0.3 / 0.3 | 28 / 8 | 0.3 | 14–27 / 27–33 | elbow bend 0% | — |
| heldout | `ayana_0_9_9_t56-66` | 21_ayana_0_9_9 56–66 s | 0.6 / 0.4 | 35 / 10 | 0.2 | 14–26 / 22–29 | 0 | — |
| heldout | `ayana_0_9_9_t23-33` | 21_ayana_0_9_9 23–33 s | 0.5 / 0.3 | 26 / 9 | 0.2 | 14–25 / 25–32 | shoulder 2% | — |
