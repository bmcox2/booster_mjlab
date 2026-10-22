# BEAT2 Clip QC (Gate 1)

Generated 2026-10-21 by `tools/beat2_batch.py --spec tools/datasets/beat2_full.toml`. Checks and limits: `tools/clip_qc.py` (calibration: `notes/gate1-calibration.md`). All numbers per clip: `/home/boston/robotics/data/beat2_full_torso/qc.json`.

- **Clips:** 16155, **5274 flagged**, 1402 severe; 1402 left out (`exclude = severe`)
- **IK config:** `/home/boston/projects/booster-mjlab/tools/ik_configs/smplx_to_k1_torso.json`
- **train-a:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-full-torso-train-a:v2`
- **train-b:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-full-torso-train-b:v2`
- **train-ab:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-full-torso-train-ab:v0`
- **val:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-full-torso-val:v1`
- **heldout-val:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-full-torso-heldout-val:v0`
- **test:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-full-torso-test:v2`
- **heldout-test:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-full-torso-heldout-test:v2`
- **heldout-conv:** `bmcox2-university-of-illinois-urbana-champaign/motion_upload/beat2-full-torso-heldout-conv:v2`

## Per speaker

| group | speaker | tier | clips | minutes | flagged | severe | kept min |
|---|---|---|---|---|---|---|---|
| train | 1_wayne | A | 1156 | 178.9 | 174 | 111 | 157.1 |
| train | 1_wayne | B | 840 | 80.0 | 333 | 82 | 71.5 |
| train | 2_scott | A | 319 | 31.9 | 68 | 12 | 30.8 |
| train | 2_scott | B | 489 | 46.7 | 305 | 32 | 43.4 |
| train | 3_solomon | A | 802 | 178.5 | 91 | 46 | 170.2 |
| train | 3_solomon | B | 454 | 50.4 | 150 | 62 | 42.9 |
| train | 4_lawrence | A | 1150 | 182.1 | 189 | 55 | 174.0 |
| train | 4_lawrence | B | 848 | 82.3 | 474 | 53 | 76.8 |
| train | 6_carla | A | 893 | 118.9 | 155 | 101 | 103.8 |
| train | 6_carla | B | 451 | 37.5 | 363 | 143 | 25.7 |
| train | 7_sophie | A | 1050 | 210.0 | 476 | 33 | 204.8 |
| train | 7_sophie | B | 383 | 33.2 | 285 | 27 | 30.7 |
| train | 9_miranda | A | 777 | 213.2 | 117 | 37 | 204.0 |
| train | 9_miranda | B | 147 | 12.1 | 66 | 15 | 10.8 |
| train | 12_zhao | A | 206 | 30.0 | 53 | 23 | 26.9 |
| train | 12_zhao | B | 193 | 20.9 | 117 | 32 | 16.7 |
| train | 13_lu | A | 319 | 52.0 | 40 | 7 | 50.8 |
| train | 13_lu | B | 247 | 25.7 | 115 | 9 | 24.5 |
| train | 15_carlos | A | 249 | 61.0 | 45 | 4 | 59.9 |
| train | 15_carlos | B | 83 | 8.8 | 25 | 0 | 8.8 |
| train | 16_jorge | A | 25 | 2.9 | 5 | 1 | 2.8 |
| train | 16_jorge | B | 74 | 8.1 | 52 | 3 | 7.9 |
| train | 17_itoi | A | 282 | 50.8 | 58 | 11 | 49.1 |
| train | 17_itoi | B | 236 | 27.7 | 159 | 7 | 26.8 |
| train | 18_daiki | A | 150 | 38.0 | 92 | 2 | 37.4 |
| train | 18_daiki | B | 49 | 4.7 | 32 | 3 | 4.3 |
| train | 22_luqi | A | 268 | 42.1 | 77 | 26 | 36.7 |
| train | 22_luqi | B | 126 | 12.6 | 51 | 18 | 10.5 |
| train | 23_hailing | A | 242 | 61.6 | 109 | 90 | 41.5 |
| train | 23_hailing | B | 58 | 5.2 | 41 | 33 | 2.3 |
| train | 24_kexin | A | 238 | 68.3 | 5 | 0 | 68.3 |
| train | 24_kexin | B | 25 | 2.2 | 5 | 0 | 2.2 |
| train | 25_goto | A | 233 | 72.8 | 24 | 5 | 71.3 |
| train | 25_goto | B | 1 | 0.1 | 1 | 0 | 0.1 |
| train | 28_tiffnay | A | 241 | 65.0 | 49 | 32 | 55.9 |
| train | 28_tiffnay | B | 51 | 4.6 | 36 | 15 | 3.1 |
| train | 30_katya | A | 282 | 61.2 | 115 | 37 | 53.5 |
| train | 30_katya | B | 100 | 9.3 | 66 | 28 | 6.3 |
| heldout | 5_stewart | A | 194 | 52.1 | 9 | 4 | 51.1 |
| heldout | 5_stewart | B | 31 | 2.8 | 9 | 0 | 2.8 |
| heldout | 10_kieks | A | 211 | 43.5 | 44 | 12 | 41.4 |
| heldout | 10_kieks | B | 40 | 3.0 | 23 | 5 | 2.7 |
| heldout | 11_nidal | A | 530 | 154.1 | 19 | 8 | 152.2 |
| heldout | 11_nidal | B | 87 | 7.4 | 35 | 1 | 7.3 |
| heldout | 20_li | A | 222 | 33.9 | 26 | 16 | 31.6 |
| heldout | 20_li | B | 190 | 20.7 | 106 | 18 | 19.0 |
| heldout | 21_ayana | A | 491 | 137.3 | 137 | 43 | 126.7 |
| heldout | 21_ayana | B | 106 | 9.3 | 83 | 20 | 7.6 |
| heldout | 27_yingqing | A | 196 | 34.4 | 64 | 42 | 27.6 |
| heldout | 27_yingqing | B | 120 | 11.0 | 101 | 38 | 7.4 |

## Checks that fired

| flag | clips | severe |
|---|---|---|
| outlier knee max | 2993 | 0 |
| leg at limit #% | 682 | 0 |
| ground IK failed # frames | 672 | 672 |
| head at limit #% | 652 | 0 |
| elbow bend at limit #% | 633 | 0 |
| shoulder at limit #% | 422 | 0 |
| right arm behind body # cm | 421 | 6 |
| joint jump # rad | 376 | 376 |
| root turn # deg/frame | 339 | 339 |
| outlier trunk drop | 309 | 129 |
| knee # deg | 297 | 0 |
| human steps | 291 | 0 |
| trunk leans # deg | 251 | 251 |
| foot held # mm off the floor | 248 | 248 |
| K# feet move # cm | 213 | 0 |
| outlier arms k# cm | 192 | 0 |
| feet overlap # mm for # s | 163 | 163 |
| hand presses into leg # mm for # s | 130 | 0 |
| trunk drop # cm | 129 | 0 |
| root jump # cm/frame | 128 | 128 |
| self-collision left_foot_collision / right_foot_collision # s | 126 | 70 |
| left arm behind body # cm | 100 | 84 |
| self-collision right_hand_collision / trunk_collision # s | 100 | 8 |
| upper-arm twist at limit #% | 99 | 38 |
| self-collision left_shank_lower_collision / right_shank_lower_collision # s | 37 | 36 |
| self-collision left_hand_collision / trunk_collision # s | 32 | 2 |
| self-collision head_#_collision / right_hand_end_collision # s | 22 | 13 |
| excluded in the spec | 19 | 19 |
| self-collision left_hand_end_collision / right_hand_end_collision # s | 18 | 3 |
| self-collision right_hand_end_collision / trunk_collision # s | 14 | 4 |
| self-collision left_shank_collision / right_shank_lower_collision # s | 11 | 11 |
| self-collision left_hand_collision / right_hand_end_collision # s | 9 | 5 |
| right foot slides # cm in one frame | 6 | 6 |
| self-collision left_hand_end_collision / right_hand_collision # s | 6 | 2 |
| self-collision left_hand_end_collision / trunk_collision # s | 6 | 2 |
| self-collision head_#_collision / left_hand_end_collision # s | 6 | 3 |
| Head_Yaw over its speed limit for # s | 4 | 4 |
| Left_Ankle_Pitch over its speed limit for # s | 4 | 4 |
| Left_Knee_Pitch over its speed limit for # s | 3 | 3 |
| left foot slides > # cm/frame for # s | 3 | 3 |
| left foot slides # cm in one frame | 3 | 3 |
| self-collision left_hand_end_collision / waist_collision # s | 3 | 2 |
| self-collision left_hand_end_collision / right_arm_#_collision # s | 3 | 0 |
| self-collision right_shank_lower_collision / trunk_collision # s | 2 | 2 |
| self-collision right_hip_yaw_collision / trunk_collision # s | 2 | 0 |
| Right_Knee_Pitch over its speed limit for # s | 2 | 2 |
| self-collision left_hand_collision / right_hand_collision # s | 1 | 1 |
| self-collision left_hip_yaw_collision / trunk_collision # s | 1 | 1 |
| self-collision right_shank_collision / trunk_collision # s | 1 | 1 |
| self-collision left_foot_collision / left_hand_end_collision # s | 1 | 0 |
| self-collision right_hand_collision / waist_collision # s | 1 | 0 |
| self-collision left_shank_collision / right_shank_collision # s | 1 | 1 |
| Right_Ankle_Pitch over its speed limit for # s | 1 | 1 |
| self-collision head_#_collision / left_hand_collision # s | 1 | 0 |
| self-collision right_foot_collision / right_hand_end_collision # s | 1 | 1 |
| Right_Ankle_Roll over its speed limit for # s | 1 | 1 |
| Left_Ankle_Roll over its speed limit for # s | 1 | 1 |

## Flagged clips

Severe in **bold**.

| clip | tier | source | feet human / K1 (cm) | arms human / K1 (cm/s) | flags |
|---|---|---|---|---|---|
| `ayana_0_103_103_t23-27_shift` | B | 21_ayana_0_103_103 23.0–27.0 s | 14.2 / 6.5 | 26 / 10 | outlier knee max (z +5.3); **root turn 6 deg/frame** *(excluded)* |
| `ayana_0_103_103_t24-29` | A | 21_ayana_0_103_103 24.5–28.5 s | 3.0 / 2.7 | 28 / 10 | outlier knee max (z +5.3); **root turn 6 deg/frame** *(excluded)* |
| `ayana_0_103_103_t29-33_shift` | B | 21_ayana_0_103_103 29.1–33.3 s | 23.0 / 11.0 | 10 / 4 | head at limit 24%; outlier knee max (z +7.6); **trunk leans 17 deg (median)** *(excluded)* |
| `ayana_0_103_103_t34-41_shift` | B | 21_ayana_0_103_103 33.6–40.6 s | 24.3 / 11.2 | 21 / 7 | knee 67 deg; head at limit 28%; outlier knee max (z +10.2); **trunk leans 17 deg (median)** *(excluded)* |
| `ayana_0_103_103_t44-52` | A | 21_ayana_0_103_103 44.3–51.7 s | 0.6 / 0.5 | 25 / 8 | head at limit 10%; **trunk leans 17 deg (median)** *(excluded)* |
| `ayana_0_103_103_t60-65` | A | 21_ayana_0_103_103 60.2–64.9 s | 9.0 / 4.7 | 31 / 11 | outlier knee max (z +5.5); **trunk leans 16 deg (median)** *(excluded)* |
| `ayana_0_103_103_t66-71` | A | 21_ayana_0_103_103 65.7–71.3 s | 6.9 / 4.2 | 20 / 10 | head at limit 45%; outlier knee max (z +5.5); **trunk leans 16 deg (median)** *(excluded)* |
| `ayana_0_111_111_t17-33` | A | 21_ayana_0_111_111 17.1–33.3 s | 4.2 / 2.9 | 14 / 6 | outlier knee max (z +4.3); **joint jump 0.94 rad (Head_Yaw at 0.4 s)**; **root turn 9 deg/frame** *(excluded)* |
| `ayana_0_12_12_t17-34` | A | 21_ayana_0_12_12 17.0–33.9 s | 1.3 / 0.6 | 31 / 10 | shoulder at limit 8%; **root turn 8 deg/frame** *(excluded)* |
| `ayana_0_12_12_t50-67` | A | 21_ayana_0_12_12 50.4–67.1 s | 6.8 / 4.1 | 21 / 8 | upper-arm twist at limit 11%; **ground IK failed 3 frames**; **joint jump 0.79 rad (Right_Shoulder_Pitch at 12.8 s)**; **root turn 8 deg/frame**; self-collision left_hand_end_collision / trunk_collision 0.5 s (at 16.0 s, 20 mm) *(excluded)* |
| `ayana_0_15_15_t17-34` | A | 21_ayana_0_15_15 17.1–34.2 s | 0.9 / 1.7 | 24 / 8 | head at limit 7%; shoulder at limit 21%; **upper-arm twist at limit 77%**; elbow bend at limit 18%; leg at limit 20%; **ground IK failed 97 frames**; **joint jump 0.60 rad (Left_Knee_Pitch at 11.3 s)**; self-collision left_hand_end_collision / trunk_collision 1.7 s (at 8.4 s, 15 mm) *(excluded)* |
| `ayana_0_65_65_t0-4_shift` | B | 21_ayana_0_65_65 0.0–4.0 s | 9.9 / 3.3 | 51 / 20 | trunk drop 6 cm; knee 62 deg; head at limit 43%; outlier arms k1 cm (z +3.5); **outlier trunk drop (z +6.0)**; outlier knee max (z +8.7); **root jump 4.2 cm/frame** *(excluded)* |
| `ayana_0_65_65_t1-8` | A | 21_ayana_0_65_65 1.1–7.5 s | 8.3 / 5.1 | 48 / 17 | head at limit 30%; outlier trunk drop (z +3.9); outlier knee max (z +5.8); **root jump 3.0 cm/frame** *(excluded)* |
| `ayana_0_65_65_t40-54` | A | 21_ayana_0_65_65 39.7–53.8 s | 5.1 / 5.0 | 46 / 18 | head at limit 15%; outlier knee max (z +4.2); **root turn 6 deg/frame** *(excluded)* |
| `ayana_0_65_65_t8-16` | A | 21_ayana_0_65_65 7.5–16.4 s | 5.0 / 2.9 | 39 / 15 | head at limit 6%; **ground IK failed 1 frames**; outlier knee max (z +3.9) *(excluded)* |
| `ayana_0_73_73_t17-33` | A | 21_ayana_0_73_73 17.3–33.0 s | 5.8 / 2.1 | 38 / 13 | **joint jump 0.81 rad (Right_Elbow_Yaw at 10.8 s)** *(excluded)* |
| `ayana_0_73_73_t31-35_shift` | B | 21_ayana_0_73_73 31.0–35.2 s | 19.1 / 16.5 | 52 / 15 | head at limit 10%; outlier trunk drop (z +3.7); **joint jump 0.67 rad (Right_Elbow_Yaw at 2.7 s)**; **root jump 11.9 cm/frame**; **root turn 27 deg/frame** *(excluded)* |
| `ayana_0_73_73_t33-50` | A | 21_ayana_0_73_73 33.2–50.0 s | 8.3 / 3.2 | 39 / 15 | head at limit 12%; **joint jump 0.74 rad (Right_Elbow_Yaw at 2.3 s)** *(excluded)* |
| `ayana_0_95_95_t19-23_shift` | B | 21_ayana_0_95_95 18.5–22.5 s | 16.9 / 9.0 | 42 / 24 | head at limit 27%; **ground IK failed 1 frames**; outlier arms k1 cm (z +4.6) *(excluded)* |
| `ayana_0_95_95_t24-38` | A | 21_ayana_0_95_95 23.9–37.5 s | 4.6 / 0.6 | 22 / 9 | head at limit 7%; **root turn 7 deg/frame** *(excluded)* |
| `ayana_0_95_95_t51-65` | A | 21_ayana_0_95_95 51.1–64.8 s | 2.5 / 0.8 | 24 / 11 | head at limit 33%; shoulder at limit 30%; **joint jump 1.77 rad (Left_Shoulder_Pitch at 4.4 s)**; **root jump 3.2 cm/frame**; **root turn 18 deg/frame** *(excluded)* |
| `ayana_1_10_10_t1-5_shift` | B | 21_ayana_1_10_10 0.8–4.8 s | 11.6 / 5.6 | 26 / 15 | **joint jump 0.78 rad (Left_Elbow_Pitch at 0.4 s)**; **root turn 15 deg/frame** *(excluded)* |
| `ayana_1_10_10_t125-131_shift` | B | 21_ayana_1_10_10 125.2–130.7 s | 19.8 / 14.3 | 10 / 4 | knee 82 deg; **ground IK failed 3 frames**; outlier trunk drop (z +4.7); outlier knee max (z +15.3); **joint jump 1.19 rad (Left_Ankle_Pitch at 3.0 s)** *(excluded)* |
| `ayana_1_10_10_t210-230` | A | 21_ayana_1_10_10 210.4–230.2 s | 8.7 / 5.5 | 26 / 10 | **ground IK failed 8 frames** *(excluded)* |
| `ayana_1_10_10_t250-270` | A | 21_ayana_1_10_10 250.0–269.9 s | 6.3 / 3.4 | 26 / 8 | elbow bend at limit 9%; **ground IK failed 6 frames** *(excluded)* |
| `ayana_1_10_10_t336-356` | A | 21_ayana_1_10_10 336.0–355.8 s | 2.8 / 1.4 | 34 / 11 | shoulder at limit 8%; **joint jump 0.79 rad (Left_Shoulder_Pitch at 5.6 s)**; **root turn 7 deg/frame** *(excluded)* |
| `ayana_1_10_10_t591-608` | A | 21_ayana_1_10_10 591.5–608.1 s | 7.4 / 1.7 | 13 / 5 | head at limit 26%; shoulder at limit 100%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `ayana_1_11_11_t146-150_shift` | B | 21_ayana_1_11_11 145.6–150.0 s | 13.7 / 9.0 | 15 / 6 | outlier knee max (z +6.3); **root turn 6 deg/frame** *(excluded)* |
| `ayana_1_11_11_t296-313` | A | 21_ayana_1_11_11 295.7–313.2 s | 6.4 / 4.8 | 18 / 9 | **upper-arm twist at limit 57%**; shoulder at limit 33%; leg at limit 49%; **ground IK failed 253 frames**; **joint jump 0.79 rad (Left_Elbow_Pitch at 7.5 s)**; **root turn 7 deg/frame**; **self-collision right_hand_collision / trunk_collision 8.9 s (at 8.7 s, 41 mm)** *(excluded)* |
| `ayana_1_11_11_t372-386` | A | 21_ayana_1_11_11 372.0–385.7 s | 9.9 / 3.9 | 30 / 8 | shoulder at limit 90%; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `ayana_1_11_11_t414-418_shift` | B | 21_ayana_1_11_11 414.2–418.2 s | 21.5 / 9.8 | 32 / 13 | leg at limit 31%; **ground IK failed 11 frames**; outlier knee max (z +3.7); **trunk leans 17 deg (median)** *(excluded)* |
| `ayana_1_11_11_t490-496_shift` | B | 21_ayana_1_11_11 490.4–496.4 s | 11.8 / 3.4 | 62 / 17 | shoulder at limit 25%; upper-arm twist at limit 23%; outlier knee max (z +3.5); **root turn 7 deg/frame** *(excluded)* |
| `ayana_1_12_12_t54-71` | A | 21_ayana_1_12_12 53.7–71.0 s | 0.5 / 1.0 | 25 / 7 | head at limit 80%; shoulder at limit 87%; **trunk leans 31 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `ayana_1_12_12_t563-577` | A | 21_ayana_1_12_12 563.0–577.2 s | 8.8 / 5.4 | 15 / 7 | leg at limit 6%; **ground IK failed 23 frames** *(excluded)* |
| `ayana_1_12_12_t575-580_shift` | B | 21_ayana_1_12_12 575.2–579.9 s | 13.1 / 6.5 | 18 / 8 | leg at limit 21%; **ground IK failed 23 frames** *(excluded)* |
| `ayana_1_1_1_t247-259` | A | 21_ayana_1_1_1 247.3–259.2 s | 8.7 / 4.5 | 32 / 11 | leg at limit 25%; **ground IK failed 81 frames** *(excluded)* |
| `ayana_1_2_2_t381-400` | A | 21_ayana_1_2_2 380.9–400.1 s | 4.2 / 4.4 | 6 / 3 | **joint jump 0.84 rad (Right_Elbow_Yaw at 6.7 s)**; **root jump 11.5 cm/frame**; **root turn 18 deg/frame**; **left foot slides > 1 cm/frame for 0.10 s (at 6.7 s)** *(excluded)* |
| `ayana_1_3_3_t371-390` | A | 21_ayana_1_3_3 370.8–389.6 s | 7.1 / 3.9 | 26 / 10 | head at limit 8%; shoulder at limit 23%; **upper-arm twist at limit 72%**; elbow bend at limit 7%; **ground IK failed 5 frames**; self-collision left_hand_collision / trunk_collision 0.1 s (at 14.5 s, 11 mm) *(excluded)* |
| `ayana_1_4_4_t95-114` | A | 21_ayana_1_4_4 95.0–114.0 s | 1.7 / 1.1 | 27 / 8 | **root turn 8 deg/frame** *(excluded)* |
| `ayana_1_6_6_t519-539` | A | 21_ayana_1_6_6 519.5–538.7 s | 6.7 / 4.1 | 20 / 5 | outlier knee max (z +6.3); **trunk leans 16 deg (median)** *(excluded)* |
| `ayana_1_6_6_t539-557` | A | 21_ayana_1_6_6 538.7–556.8 s | 8.9 / 6.0 | 22 / 8 | trunk drop 7 cm; knee 65 deg; **outlier trunk drop (z +7.5)**; outlier knee max (z +9.8); **trunk leans 17 deg (median)** *(excluded)* |
| `ayana_1_7_7_t160-179` | A | 21_ayana_1_7_7 160.1–179.3 s | 1.1 / 0.3 | 7 / 4 | **root turn 6 deg/frame** *(excluded)* |
| `ayana_1_7_7_t20-33` | A | 21_ayana_1_7_7 19.7–32.8 s | 4.8 / 0.8 | 15 / 5 | outlier knee max (z +4.0); **root turn 10 deg/frame** *(excluded)* |
| `ayana_1_7_7_t237-256` | A | 21_ayana_1_7_7 236.6–255.7 s | 2.8 / 1.5 | 30 / 10 | shoulder at limit 5%; **ground IK failed 4 frames**; outlier knee max (z +3.7) *(excluded)* |
| `ayana_1_7_7_t256-275` | A | 21_ayana_1_7_7 255.7–274.8 s | 3.4 / 1.5 | 26 / 9 | **ground IK failed 10 frames** *(excluded)* |
| `ayana_1_7_7_t292-296_shift` | B | 21_ayana_1_7_7 291.9–295.9 s | 16.0 / 7.4 | 6 / 2 | knee 69 deg; leg at limit 27%; **ground IK failed 32 frames**; outlier knee max (z +11.2) *(excluded)* |
| `ayana_1_7_7_t422-441` | A | 21_ayana_1_7_7 422.1–441.3 s | 2.5 / 1.2 | 11 / 4 | shoulder at limit 16%; **ground IK failed 2 frames**; outlier trunk drop (z +4.2); outlier knee max (z +6.9) *(excluded)* |
| `ayana_1_8_8_t1-14` | A | 21_ayana_1_8_8 0.7–14.2 s | 7.9 / 3.4 | 20 / 7 | head at limit 90%; shoulder at limit 96%; **trunk leans 24 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `ayana_1_8_8_t168-187` | A | 21_ayana_1_8_8 168.0–186.9 s | 3.0 / 1.1 | 30 / 10 | trunk drop 5 cm; knee 60 deg; **outlier trunk drop (z +5.7)**; outlier knee max (z +8.1); **joint jump 1.04 rad (Right_Shoulder_Pitch at 5.7 s)**; **self-collision head_2_collision / left_hand_end_collision 2.8 s (at 11.5 s, 29 mm)** *(excluded)* |
| `ayana_1_8_8_t243-260` | A | 21_ayana_1_8_8 243.4–259.9 s | 9.4 / 9.2 | 25 / 11 | K1 feet move 9 cm; shoulder at limit 16%; **ground IK failed 22 frames**; outlier trunk drop (z +4.7); outlier knee max (z +6.0) *(excluded)* |
| `ayana_1_8_8_t28-41` | A | 21_ayana_1_8_8 27.6–41.0 s | 2.5 / 1.4 | 20 / 5 | head at limit 51%; shoulder at limit 94%; **trunk leans 20 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `ayana_1_8_8_t44-54` | A | 21_ayana_1_8_8 44.0–54.4 s | 0.7 / 1.3 | 25 / 11 | shoulder at limit 8%; upper-arm twist at limit 7%; **root turn 8 deg/frame** *(excluded)* |
| `ayana_1_8_8_t523-530_shift` | B | 21_ayana_1_8_8 523.4–530.2 s | 11.9 / 2.8 | 9 / 4 | head at limit 48%; shoulder at limit 92%; leg at limit 11%; **trunk leans 34 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `ayana_1_8_8_t533-542_shift` | B | 21_ayana_1_8_8 533.3–541.7 s | 20.0 / 8.4 | 12 / 6 | head at limit 47%; elbow bend at limit 20%; outlier knee max (z +5.9); **trunk leans 16 deg (median)** *(excluded)* |
| `ayana_1_8_8_t548-553_shift` | B | 21_ayana_1_8_8 548.1–552.9 s | 10.7 / 1.3 | 4 / 2 | head at limit 33%; **trunk leans 30 deg (median)** *(excluded)* |
| `ayana_1_9_9_t149-153_shift` | B | 21_ayana_1_9_9 149.0–153.4 s | 8.2 / 3.7 | 39 / 17 | shoulder at limit 32%; outlier knee max (z +3.6); self-collision left_foot_collision / right_foot_collision 0.3 s (at 2.2 s, 18 mm); **feet overlap 18 mm for 0.3 s (at 2.2 s)** *(excluded)* |
| `ayana_1_9_9_t151-170` | A | 21_ayana_1_9_9 151.4–169.8 s | 1.5 / 1.6 | 16 / 6 | shoulder at limit 15%; self-collision left_foot_collision / right_foot_collision 0.2 s (at 0.0 s, 9 mm); **feet overlap 9 mm for 0.2 s (at 0.0 s)** *(excluded)* |
| `ayana_1_9_9_t22-26_shift` | B | 21_ayana_1_9_9 22.2–26.2 s | 15.1 / 7.8 | 32 / 15 | trunk drop 6 cm; knee 63 deg; **outlier trunk drop (z +6.9)**; outlier knee max (z +9.1) *(excluded)* |
| `ayana_1_9_9_t364-369_shift` | B | 21_ayana_1_9_9 364.1–368.6 s | 13.4 / 7.1 | 18 / 6 | head at limit 58%; shoulder at limit 67%; **trunk leans 23 deg (median)**; **right arm behind body 15 cm (human's in front)** *(excluded)* |
| `ayana_1_9_9_t65-76` | A | 21_ayana_1_9_9 65.0–76.2 s | 10.0 / 4.4 | 7 / 2 | head at limit 72%; **trunk leans 31 deg (median)** *(excluded)* |
| `ayana_1_9_9_t7-22` | A | 21_ayana_1_9_9 6.8–21.5 s | 7.7 / 3.6 | 25 / 12 | **self-collision left_hand_end_collision / waist_collision 0.9 s (at 13.2 s, 35 mm)**; hand presses into leg 14 mm for 0.1 s (at 14.1 s) *(excluded)* |
| `ayana_1_9_9_t74-81_shift` | B | 21_ayana_1_9_9 74.2–81.3 s | 16.9 / 8.0 | 11 / 4 | head at limit 18%; outlier knee max (z +4.9); **root turn 7 deg/frame**; **trunk leans 17 deg (median)** *(excluded)* |
| `ayana_1_9_9_t79-85` | A | 21_ayana_1_9_9 79.3–85.3 s | 5.6 / 2.7 | 17 / 7 | **root turn 7 deg/frame** *(excluded)* |
| `carla_0_101_101_t21-28` | A | 6_carla_0_101_101 21.2–28.3 s | 1.4 / 0.8 | 7 / 3 | **root turn 7 deg/frame** *(excluded)* |
| `carla_0_103_103_t43-47_shift` | B | 6_carla_0_103_103 43.3–47.3 s | 9.1 / 2.2 | 22 / 6 | leg at limit 22%; **ground IK failed 4 frames**; outlier knee max (z +6.8) *(excluded)* |
| `carla_0_103_103_t48-53` | A | 6_carla_0_103_103 47.9–53.3 s | 1.6 / 0.8 | 14 / 6 | **root turn 7 deg/frame** *(excluded)* |
| `carla_0_104_104_t20-26_shift` | B | 6_carla_0_104_104 20.1–26.1 s | 9.2 / 4.7 | 18 / 6 | leg at limit 8%; **ground IK failed 9 frames**; outlier knee max (z +6.9) *(excluded)* |
| `carla_0_107_107_t0-4_shift` | B | 6_carla_0_107_107 0.0–4.1 s | 17.2 / 3.6 | 16 / 5 | trunk drop 5 cm; knee 65 deg; leg at limit 32%; **ground IK failed 31 frames**; **outlier trunk drop (z +5.5)**; outlier knee max (z +9.8) *(excluded)* |
| `carla_0_108_108_t14-18_shift` | B | 6_carla_0_108_108 14.3–18.3 s | 13.0 / 2.8 | 16 / 4 | leg at limit 8%; **ground IK failed 4 frames**; outlier knee max (z +6.2) *(excluded)* |
| `carla_0_108_108_t28-32_shift` | B | 6_carla_0_108_108 28.3–32.3 s | 14.7 / 4.0 | 36 / 9 | leg at limit 28%; **ground IK failed 25 frames**; outlier trunk drop (z +4.1); outlier knee max (z +7.4) *(excluded)* |
| `carla_0_108_108_t42-46_shift` | B | 6_carla_0_108_108 41.7–45.7 s | 23.5 / 6.1 | 35 / 9 | leg at limit 16%; **ground IK failed 18 frames**; outlier knee max (z +7.3) *(excluded)* |
| `carla_0_109_109_t8-12_shift` | B | 6_carla_0_109_109 7.6–11.6 s | 10.1 / 2.2 | 9 / 2 | **ground IK failed 1 frames** *(excluded)* |
| `carla_0_112_112_t49-53_shift` | B | 6_carla_0_112_112 48.7–52.7 s | 10.4 / 2.2 | 19 / 6 | leg at limit 12%; **ground IK failed 6 frames**; outlier knee max (z +6.4) *(excluded)* |
| `carla_0_115_115_t0-7` | A | 6_carla_0_115_115 0.0–6.9 s | 1.8 / 1.0 | 16 / 5 | shoulder at limit 97%; **trunk leans 26 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `carla_0_115_115_t9-13_shift` | B | 6_carla_0_115_115 9.4–13.4 s | 11.8 / 3.0 | 10 / 3 | leg at limit 10%; **ground IK failed 5 frames** *(excluded)* |
| `carla_0_118_118_t12-29` | A | 6_carla_0_118_118 11.8–29.0 s | 2.5 / 0.8 | 20 / 7 | **root turn 10 deg/frame** *(excluded)* |
| `carla_0_49_49_t26-32_shift` | B | 6_carla_0_49_49 25.6–31.5 s | 13.8 / 3.3 | 24 / 6 | knee 62 deg; leg at limit 56%; **ground IK failed 56 frames**; outlier knee max (z +8.7) *(excluded)* |
| `carla_0_50_50_t24-32_shift` | B | 6_carla_0_50_50 24.1–32.2 s | 12.1 / 6.7 | 19 / 5 | leg at limit 6%; **ground IK failed 12 frames**; outlier knee max (z +5.0) *(excluded)* |
| `carla_0_51_51_t18-23_shift` | B | 6_carla_0_51_51 17.6–23.3 s | 15.9 / 3.9 | 15 / 4 | leg at limit 26%; **ground IK failed 37 frames** *(excluded)* |
| `carla_0_52_52_t0-5_shift` | B | 6_carla_0_52_52 0.0–4.9 s | 8.8 / 2.7 | 16 / 5 | leg at limit 35%; **ground IK failed 50 frames**; outlier knee max (z +6.9) *(excluded)* |
| `carla_0_53_53_t6-10_shift` | B | 6_carla_0_53_53 5.8–9.8 s | 12.3 / 2.7 | 17 / 5 | leg at limit 15%; **ground IK failed 16 frames**; outlier knee max (z +3.7) *(excluded)* |
| `carla_0_54_54_t23-30` | A | 6_carla_0_54_54 23.2–29.8 s | 9.5 / 2.4 | 14 / 4 | leg at limit 5%; **ground IK failed 7 frames** *(excluded)* |
| `carla_0_54_54_t26-30_shift` | B | 6_carla_0_54_54 25.9–29.9 s | 8.9 / 2.3 | 10 / 3 | leg at limit 11%; **ground IK failed 10 frames** *(excluded)* |
| `carla_0_57_57_t13-17_shift` | B | 6_carla_0_57_57 13.3–17.3 s | 12.7 / 2.9 | 34 / 12 | leg at limit 7%; **ground IK failed 7 frames**; outlier knee max (z +5.8) *(excluded)* |
| `carla_0_57_57_t18-26` | A | 6_carla_0_57_57 18.1–25.5 s | 5.5 / 2.7 | 28 / 11 | upper-arm twist at limit 31%; **excluded in the spec (fails in training)** *(excluded)* |
| `carla_0_59_59_t11-16` | A | 6_carla_0_59_59 10.6–16.0 s | 9.8 / 2.4 | 17 / 5 | leg at limit 6%; **ground IK failed 3 frames** *(excluded)* |
| `carla_0_59_59_t12-16_shift` | B | 6_carla_0_59_59 12.4–16.4 s | 10.4 / 2.3 | 19 / 5 | leg at limit 18%; **ground IK failed 15 frames** *(excluded)* |
| `carla_0_61_61_t7-11_shift` | B | 6_carla_0_61_61 6.7–11.0 s | 18.7 / 10.2 | 10 / 5 | **ground IK failed 1 frames**; outlier knee max (z +5.9) *(excluded)* |
| `carla_0_61_61_t9-14` | A | 6_carla_0_61_61 9.2–13.5 s | 9.1 / 5.2 | 7 / 3 | leg at limit 11%; **ground IK failed 10 frames** *(excluded)* |
| `carla_0_64_64_t42-46` | A | 6_carla_0_64_64 41.5–46.1 s | 4.6 / 3.0 | 29 / 7 | outlier knee max (z +5.7); **foot held 41 mm off the floor (median)** *(excluded)* |
| `carla_0_65_65_t30-34_shift` | B | 6_carla_0_65_65 29.9–33.9 s | 20.1 / 9.4 | 25 / 9 | knee 62 deg; leg at limit 18%; **ground IK failed 9 frames**; outlier knee max (z +8.7) *(excluded)* |
| `carla_0_65_65_t35-39_shift` | B | 6_carla_0_65_65 34.6–39.4 s | 18.4 / 4.7 | 21 / 7 | trunk drop 5 cm; knee 66 deg; leg at limit 19%; **ground IK failed 23 frames**; **outlier trunk drop (z +5.6)**; outlier knee max (z +10.0); **foot held 40 mm off the floor (median)** *(excluded)* |
| `carla_0_65_65_t4-9_shift` | B | 6_carla_0_65_65 3.7–8.6 s | 13.9 / 2.9 | 29 / 8 | leg at limit 29%; **ground IK failed 40 frames** *(excluded)* |
| `carla_0_66_66_t13-18_shift` | B | 6_carla_0_66_66 12.9–18.0 s | 19.7 / 5.2 | 18 / 7 | leg at limit 7%; **ground IK failed 12 frames**; outlier trunk drop (z +3.9); outlier knee max (z +7.8) *(excluded)* |
| `carla_0_66_66_t34-39_shift` | B | 6_carla_0_66_66 34.1–38.8 s | 17.7 / 4.8 | 11 / 3 | leg at limit 14%; **ground IK failed 17 frames**; outlier knee max (z +6.2) *(excluded)* |
| `carla_0_69_69_t0-5` | A | 6_carla_0_69_69 0.3–5.1 s | 9.8 / 5.7 | 21 / 6 | head at limit 8%; shoulder at limit 20%; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `carla_0_69_69_t36-40_shift` | B | 6_carla_0_69_69 36.2–40.3 s | 15.7 / 3.2 | 21 / 5 | leg at limit 8%; **ground IK failed 5 frames**; outlier knee max (z +6.8) *(excluded)* |
| `carla_0_69_69_t49-54` | A | 6_carla_0_69_69 49.1–54.4 s | 7.8 / 3.2 | 20 / 4 | knee 63 deg; leg at limit 8%; outlier knee max (z +9.1); **foot held 46 mm off the floor (median)** *(excluded)* |
| `carla_0_70_70_t0-5_shift` | B | 6_carla_0_70_70 0.0–4.5 s | 22.6 / 6.5 | 21 / 6 | leg at limit 17%; **ground IK failed 7 frames**; outlier knee max (z +7.0) *(excluded)* |
| `carla_0_71_71_t21-25_shift` | B | 6_carla_0_71_71 20.8–24.8 s | 11.3 / 2.6 | 17 / 7 | leg at limit 35%; **ground IK failed 27 frames**; outlier knee max (z +7.1) *(excluded)* |
| `carla_0_75_75_t0-9` | A | 6_carla_0_75_75 0.0–9.3 s | 1.4 / 1.2 | 17 / 4 | head at limit 18%; shoulder at limit 87%; **trunk leans 25 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `carla_0_75_75_t14-20_shift` | B | 6_carla_0_75_75 13.8–19.6 s | 21.7 / 17.2 | 9 / 3 | knee 61 deg; outlier trunk drop (z +4.4); outlier knee max (z +8.4); **foot held 35 mm off the floor (median)** *(excluded)* |
| `carla_0_77_77_t11-16_shift` | B | 6_carla_0_77_77 11.2–16.3 s | 17.1 / 4.3 | 27 / 11 | leg at limit 29%; **ground IK failed 39 frames**; outlier knee max (z +5.6) *(excluded)* |
| `carla_0_79_79_t20-24_shift` | B | 6_carla_0_79_79 20.3–24.5 s | 9.8 / 2.5 | 33 / 8 | leg at limit 46%; **ground IK failed 7 frames**; outlier knee max (z +7.2); **foot held 41 mm off the floor (median)** *(excluded)* |
| `carla_0_79_79_t31-36` | A | 6_carla_0_79_79 31.0–35.6 s | 9.5 / 2.4 | 36 / 9 | leg at limit 5%; **ground IK failed 5 frames** *(excluded)* |
| `carla_0_80_80_t48-53_shift` | B | 6_carla_0_80_80 47.7–52.8 s | 11.0 / 4.5 | 36 / 8 | knee 61 deg; leg at limit 27%; **ground IK failed 17 frames**; outlier knee max (z +8.3) *(excluded)* |
| `carla_0_82_82_t25-29_shift` | B | 6_carla_0_82_82 25.1–29.1 s | 13.3 / 2.5 | 11 / 3 | leg at limit 22%; **ground IK failed 3 frames**; outlier trunk drop (z +3.6); outlier knee max (z +5.7) *(excluded)* |
| `carla_0_86_86_t2-12` | A | 6_carla_0_86_86 2.5–11.9 s | 1.3 / 0.8 | 14 / 3 | **root turn 6 deg/frame** *(excluded)* |
| `carla_0_87_87_t20-24_shift` | B | 6_carla_0_87_87 20.4–24.4 s | 12.1 / 4.6 | 11 / 5 | leg at limit 30%; **ground IK failed 23 frames**; outlier knee max (z +4.7) *(excluded)* |
| `carla_0_90_90_t41-45_shift` | B | 6_carla_0_90_90 41.3–45.3 s | 13.3 / 2.9 | 24 / 7 | leg at limit 17%; **ground IK failed 17 frames**; outlier knee max (z +5.4) *(excluded)* |
| `carla_0_91_91_t17-21_shift` | B | 6_carla_0_91_91 16.8–21.1 s | 8.7 / 2.2 | 18 / 7 | leg at limit 36%; **ground IK failed 7 frames**; outlier knee max (z +7.1); **foot held 32 mm off the floor (median)** *(excluded)* |
| `carla_1_10_10_t167-179` | A | 6_carla_1_10_10 167.2–178.8 s | 6.8 / 2.3 | 8 / 3 | **root turn 9 deg/frame** *(excluded)* |
| `carla_1_10_10_t261-265_shift` | B | 6_carla_1_10_10 261.3–265.3 s | 20.5 / 5.6 | 12 / 5 | leg at limit 37%; outlier trunk drop (z +4.7); outlier knee max (z +5.4); **foot held 34 mm off the floor (median)** *(excluded)* |
| `carla_1_10_10_t431-443` | A | 6_carla_1_10_10 430.6–442.7 s | 4.1 / 2.6 | 15 / 8 | **joint jump 2.00 rad (Right_Elbow_Yaw at 10.6 s)**; **root turn 12 deg/frame** *(excluded)* |
| `carla_1_10_10_t44-49_shift` | B | 6_carla_1_10_10 44.3–49.0 s | 17.0 / 6.5 | 11 / 4 | knee 63 deg; leg at limit 8%; **ground IK failed 3 frames**; outlier knee max (z +9.0) *(excluded)* |
| `carla_1_10_10_t530-535_shift` | B | 6_carla_1_10_10 529.6–535.0 s | 13.4 / 2.3 | 11 / 5 | leg at limit 9%; **ground IK failed 3 frames**; **foot held 32 mm off the floor (median)** *(excluded)* |
| `carla_1_10_10_t552-556_shift` | B | 6_carla_1_10_10 552.5–556.5 s | 17.1 / 5.6 | 3 / 1 | leg at limit 10%; outlier trunk drop (z +3.6); outlier knee max (z +4.1); **foot held 32 mm off the floor (median)** *(excluded)* |
| `carla_1_11_11_t13-17_shift` | B | 6_carla_1_11_11 12.8–17.2 s | 20.4 / 5.6 | 10 / 2 | knee 63 deg; leg at limit 15%; **ground IK failed 17 frames**; outlier knee max (z +9.1) *(excluded)* |
| `carla_1_11_11_t184-189_shift` | B | 6_carla_1_11_11 184.3–189.0 s | 21.5 / 6.6 | 11 / 3 | knee 70 deg; leg at limit 18%; **ground IK failed 24 frames**; outlier knee max (z +11.2) *(excluded)* |
| `carla_1_11_11_t220-225_shift` | B | 6_carla_1_11_11 220.0–225.2 s | 22.9 / 7.3 | 24 / 8 | leg at limit 27%; **ground IK failed 40 frames**; outlier knee max (z +5.9) *(excluded)* |
| `carla_1_11_11_t259-264_shift` | B | 6_carla_1_11_11 259.2–264.3 s | 22.9 / 6.1 | 9 / 3 | knee 77 deg; leg at limit 35%; **ground IK failed 45 frames**; outlier trunk drop (z +4.2); outlier knee max (z +13.6); **foot held 42 mm off the floor (median)** *(excluded)* |
| `carla_1_11_11_t275-279_shift` | B | 6_carla_1_11_11 274.5–278.9 s | 18.8 / 5.6 | 11 / 2 | leg at limit 15%; **ground IK failed 17 frames**; outlier knee max (z +6.0) *(excluded)* |
| `carla_1_11_11_t311-317` | A | 6_carla_1_11_11 310.9–316.9 s | 7.4 / 2.4 | 2 / 1 | leg at limit 48%; **ground IK failed 38 frames**; outlier knee max (z +8.0); **foot held 48 mm off the floor (median)** *(excluded)* |
| `carla_1_11_11_t389-394_shift` | B | 6_carla_1_11_11 389.4–393.8 s | 18.2 / 5.4 | 6 / 2 | leg at limit 27%; **ground IK failed 9 frames**; outlier trunk drop (z +4.6); outlier knee max (z +7.8) *(excluded)* |
| `carla_1_11_11_t421-425_shift` | B | 6_carla_1_11_11 421.4–425.4 s | 18.1 / 4.3 | 15 / 5 | leg at limit 9%; outlier trunk drop (z +4.9); outlier knee max (z +6.2); **foot held 46 mm off the floor (median)** *(excluded)* |
| `carla_1_11_11_t481-485` | A | 6_carla_1_11_11 481.0–485.0 s | 8.7 / 1.7 | 23 / 8 | leg at limit 7%; **ground IK failed 5 frames** *(excluded)* |
| `carla_1_11_11_t524-534` | A | 6_carla_1_11_11 524.5–533.6 s | 2.9 / 1.4 | 15 / 5 | **self-collision head_2_collision / right_hand_end_collision 4.3 s (at 4.9 s, 43 mm)** *(excluded)* |
| `carla_1_11_11_t540-544_shift` | B | 6_carla_1_11_11 539.7–544.4 s | 24.8 / 6.3 | 19 / 5 | trunk drop 5 cm; leg at limit 6%; **outlier trunk drop (z +5.3)**; outlier knee max (z +5.8); **foot held 31 mm off the floor (median)** *(excluded)* |
| `carla_1_11_11_t660-665_shift` | B | 6_carla_1_11_11 660.2–664.6 s | 18.0 / 5.5 | 37 / 11 | trunk drop 5 cm; leg at limit 23%; **ground IK failed 23 frames**; **outlier trunk drop (z +5.6)**; outlier knee max (z +7.5); **foot held 38 mm off the floor (median)** *(excluded)* |
| `carla_1_12_12_t123-130` | A | 6_carla_1_12_12 122.7–130.2 s | 6.2 / 1.9 | 16 / 5 | leg at limit 9%; **ground IK failed 4 frames** *(excluded)* |
| `carla_1_12_12_t296-300_shift` | B | 6_carla_1_12_12 295.6–299.8 s | 14.1 / 3.5 | 26 / 10 | leg at limit 7%; **ground IK failed 4 frames** *(excluded)* |
| `carla_1_12_12_t431-438` | A | 6_carla_1_12_12 430.9–437.6 s | 4.6 / 1.8 | 19 / 8 | head at limit 10%; shoulder at limit 71%; outlier trunk drop (z +4.3); **trunk leans 24 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `carla_1_12_12_t454-458_shift` | B | 6_carla_1_12_12 453.7–457.7 s | 10.1 / 4.1 | 17 / 5 | **ground IK failed 1 frames** *(excluded)* |
| `carla_1_12_12_t459-463` | A | 6_carla_1_12_12 458.8–463.1 s | 9.4 / 3.2 | 31 / 12 | **joint jump 0.92 rad (Right_Shoulder_Pitch at 1.9 s)**; **root turn 10 deg/frame** *(excluded)* |
| `carla_1_12_12_t527-540` | A | 6_carla_1_12_12 527.1–539.5 s | 6.4 / 5.5 | 13 / 4 | **root jump 3.0 cm/frame** *(excluded)* |
| `carla_1_12_12_t56-62_shift` | B | 6_carla_1_12_12 55.7–61.5 s | 20.7 / 5.6 | 10 / 3 | leg at limit 18%; **ground IK failed 4 frames**; outlier trunk drop (z +4.5); outlier knee max (z +6.1) *(excluded)* |
| `carla_1_1_1_t195-199_shift` | B | 6_carla_1_1_1 194.6–198.6 s | 17.4 / 4.1 | 6 / 2 | knee 63 deg; leg at limit 25%; **ground IK failed 27 frames**; outlier knee max (z +8.9) *(excluded)* |
| `carla_1_1_1_t199-217` | A | 6_carla_1_1_1 199.4–216.9 s | 6.8 / 3.2 | 8 / 4 | **joint jump 0.82 rad (Head_Yaw at 2.6 s)** *(excluded)* |
| `carla_1_1_1_t251-269` | A | 6_carla_1_1_1 250.9–268.9 s | 7.1 / 2.4 | 5 / 2 | leg at limit 100%; **ground IK failed 529 frames**; outlier knee max (z -3.8) *(excluded)* |
| `carla_1_1_1_t334-347` | A | 6_carla_1_1_1 334.4–347.2 s | 1.4 / 0.7 | 3 / 1 | leg at limit 100%; **ground IK failed 384 frames**; outlier knee max (z -6.0) *(excluded)* |
| `carla_1_1_1_t347-360` | A | 6_carla_1_1_1 347.2–360.0 s | 9.4 / 6.7 | 7 / 3 | leg at limit 100%; **ground IK failed 384 frames**; outlier knee max (z -6.4); **root turn 9 deg/frame** *(excluded)* |
| `carla_1_1_1_t358-364_shift` | B | 6_carla_1_1_1 358.0–363.8 s | 10.2 / 6.7 | 7 / 3 | head at limit 11%; leg at limit 100%; **ground IK failed 174 frames**; outlier knee max (z -6.4); **joint jump 1.01 rad (Head_Yaw at 4.5 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_1_1_t362-374` | A | 6_carla_1_1_1 361.8–373.7 s | 5.8 / 3.4 | 6 / 3 | head at limit 10%; leg at limit 100%; **ground IK failed 356 frames**; outlier knee max (z -5.3); **joint jump 1.01 rad (Head_Yaw at 0.7 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_1_1_t374-386` | A | 6_carla_1_1_1 373.7–385.6 s | 3.2 / 1.5 | 5 / 2 | leg at limit 100%; **ground IK failed 357 frames**; outlier knee max (z -6.5) *(excluded)* |
| `carla_1_1_1_t384-388_shift` | B | 6_carla_1_1_1 383.6–388.2 s | 7.5 / 5.6 | 3 / 2 | leg at limit 88%; **ground IK failed 80 frames** *(excluded)* |
| `carla_1_1_1_t386-396` | A | 6_carla_1_1_1 386.2–396.4 s | 9.8 / 6.0 | 10 / 6 | head at limit 13%; leg at limit 94%; **ground IK failed 251 frames**; **joint jump 0.95 rad (Head_Yaw at 2.3 s)**; **root turn 8 deg/frame** *(excluded)* |
| `carla_1_1_1_t396-407` | A | 6_carla_1_1_1 396.4–406.5 s | 1.2 / 0.5 | 3 / 2 | leg at limit 100%; **ground IK failed 303 frames** *(excluded)* |
| `carla_1_1_1_t444-462` | A | 6_carla_1_1_1 443.6–461.6 s | 8.3 / 3.9 | 9 / 3 | head at limit 51%; **joint jump 0.92 rad (Head_Yaw at 7.1 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_1_1_t510-527` | A | 6_carla_1_1_1 509.5–526.7 s | 2.4 / 1.7 | 7 / 2 | head at limit 47%; leg at limit 100%; **ground IK failed 516 frames**; outlier knee max (z -4.7) *(excluded)* |
| `carla_1_1_1_t527-544` | A | 6_carla_1_1_1 526.7–544.0 s | 1.8 / 0.9 | 8 / 3 | head at limit 55%; leg at limit 100%; **ground IK failed 517 frames**; outlier knee max (z -4.4); **root turn 9 deg/frame** *(excluded)* |
| `carla_1_1_1_t545-552` | A | 6_carla_1_1_1 545.3–552.2 s | 3.1 / 3.3 | 13 / 6 | head at limit 29%; **joint jump 0.96 rad (Head_Yaw at 1.2 s)**; **root turn 8 deg/frame** *(excluded)* |
| `carla_1_2_2_t100-104_shift` | B | 6_carla_1_2_2 100.4–104.4 s | 17.6 / 5.9 | 11 / 4 | leg at limit 26%; **ground IK failed 17 frames**; outlier knee max (z +6.7) *(excluded)* |
| `carla_1_2_2_t24-29_shift` | B | 6_carla_1_2_2 24.0–29.0 s | 18.1 / 4.7 | 17 / 5 | leg at limit 21%; **ground IK failed 31 frames**; outlier knee max (z +5.4) *(excluded)* |
| `carla_1_2_2_t334-341_shift` | B | 6_carla_1_2_2 334.4–341.5 s | 21.9 / 17.0 | 11 / 5 | leg at limit 6%; **ground IK failed 9 frames**; outlier knee max (z +7.4) *(excluded)* |
| `carla_1_2_2_t392-398_shift` | B | 6_carla_1_2_2 392.3–397.8 s | 22.3 / 16.6 | 14 / 7 | head at limit 8%; shoulder at limit 43%; outlier knee max (z +5.4); **joint jump 1.92 rad (Left_Elbow_Pitch at 3.4 s)**; **root turn 30 deg/frame**; left arm behind body 8 cm (human's in front) *(excluded)* |
| `carla_1_2_2_t411-415_shift` | B | 6_carla_1_2_2 411.3–415.3 s | 16.7 / 9.3 | 14 / 4 | head at limit 37%; shoulder at limit 78%; outlier knee max (z +3.9); **trunk leans 28 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `carla_1_2_2_t451-455_shift` | B | 6_carla_1_2_2 450.7–454.7 s | 16.0 / 3.9 | 14 / 4 | leg at limit 11%; **ground IK failed 10 frames**; outlier knee max (z +6.7) *(excluded)* |
| `carla_1_2_2_t460-467_shift` | B | 6_carla_1_2_2 460.4–466.9 s | 18.0 / 4.8 | 7 / 3 | leg at limit 35%; **ground IK failed 59 frames**; outlier trunk drop (z +3.8); outlier knee max (z +8.0); **foot held 34 mm off the floor (median)** *(excluded)* |
| `carla_1_2_2_t5-16_shift` | B | 6_carla_1_2_2 5.4–15.9 s | 15.4 / 5.0 | 17 / 5 | leg at limit 15%; **ground IK failed 24 frames**; outlier knee max (z +7.2) *(excluded)* |
| `carla_1_2_2_t525-529_shift` | B | 6_carla_1_2_2 524.7–529.2 s | 21.4 / 6.2 | 5 / 2 | leg at limit 15%; **ground IK failed 19 frames**; outlier knee max (z +7.0) *(excluded)* |
| `carla_1_2_2_t563-571_shift` | B | 6_carla_1_2_2 562.6–571.4 s | 14.1 / 3.9 | 15 / 4 | trunk drop 6 cm; knee 64 deg; leg at limit 41%; **ground IK failed 83 frames**; **outlier trunk drop (z +6.2)**; outlier knee max (z +9.5); **foot held 34 mm off the floor (median)** *(excluded)* |
| `carla_1_2_2_t57-61_shift` | B | 6_carla_1_2_2 56.6–60.6 s | 11.5 / 3.1 | 18 / 5 | **ground IK failed 1 frames**; outlier knee max (z +4.7) *(excluded)* |
| `carla_1_2_2_t586-590_shift` | B | 6_carla_1_2_2 586.1–590.1 s | 15.9 / 6.4 | 63 / 21 | leg at limit 9%; **ground IK failed 10 frames**; outlier arms k1 cm (z +4.0); outlier knee max (z +7.3) *(excluded)* |
| `carla_1_2_2_t644-650_shift` | B | 6_carla_1_2_2 643.7–649.8 s | 14.1 / 9.7 | 31 / 10 | shoulder at limit 7%; outlier knee max (z +5.7); **joint jump 1.37 rad (Left_Shoulder_Pitch at 0.8 s)**; **root jump 3.2 cm/frame**; **root turn 34 deg/frame** *(excluded)* |
| `carla_1_2_2_t86-90_shift` | B | 6_carla_1_2_2 85.6–90.1 s | 17.8 / 4.5 | 7 / 2 | leg at limit 15%; **ground IK failed 19 frames** *(excluded)* |
| `carla_1_3_3_t105-109_shift` | B | 6_carla_1_3_3 105.2–109.2 s | 19.2 / 4.0 | 18 / 7 | head at limit 14%; outlier knee max (z +5.6); **joint jump 0.75 rad (Head_Yaw at 2.4 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_3_3_t135-141_shift` | B | 6_carla_1_3_3 135.2–140.9 s | 24.7 / 7.0 | 11 / 5 | knee 63 deg; leg at limit 25%; **ground IK failed 40 frames**; outlier knee max (z +8.9) *(excluded)* |
| `carla_1_3_3_t142-149` | A | 6_carla_1_3_3 142.0–149.4 s | 4.3 / 2.3 | 13 / 5 | **joint jump 0.95 rad (Head_Yaw at 1.7 s)**; **root turn 7 deg/frame**; **Head_Yaw over its speed limit for 0.13 s (at 0.9 s)** *(excluded)* |
| `carla_1_3_3_t154-158_shift` | B | 6_carla_1_3_3 154.4–158.4 s | 22.3 / 21.8 | 13 / 3 | K1 feet move 22 cm; knee 69 deg; leg at limit 12%; **ground IK failed 12 frames**; outlier knee max (z +11.1) *(excluded)* |
| `carla_1_3_3_t164-169_shift` | B | 6_carla_1_3_3 163.9–169.3 s | 16.7 / 4.3 | 7 / 2 | leg at limit 16%; **ground IK failed 5 frames**; outlier knee max (z +7.6) *(excluded)* |
| `carla_1_3_3_t198-203_shift` | B | 6_carla_1_3_3 197.9–203.2 s | 10.8 / 6.7 | 24 / 8 | knee 62 deg; shoulder at limit 9%; outlier knee max (z +8.7); **joint jump 1.39 rad (Left_Shoulder_Pitch at 1.0 s)**; **root turn 33 deg/frame** *(excluded)* |
| `carla_1_3_3_t214-221` | A | 6_carla_1_3_3 214.2–220.6 s | 4.3 / 3.9 | 16 / 6 | head at limit 7%; shoulder at limit 98%; **trunk leans 31 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `carla_1_3_3_t232-236_shift` | B | 6_carla_1_3_3 232.4–236.4 s | 16.4 / 5.2 | 12 / 3 | knee 87 deg; leg at limit 9%; **ground IK failed 8 frames**; outlier trunk drop (z +3.6); outlier knee max (z +17.1); **joint jump 0.72 rad (Right_Ankle_Pitch at 3.6 s)** *(excluded)* |
| `carla_1_3_3_t521-528_shift` | B | 6_carla_1_3_3 521.0–527.5 s | 24.2 / 13.4 | 12 / 5 | head at limit 18%; outlier knee max (z +4.5); **joint jump 0.81 rad (Head_Yaw at 1.5 s)**; **root turn 8 deg/frame** *(excluded)* |
| `carla_1_3_3_t544-550` | A | 6_carla_1_3_3 543.5–549.5 s | 5.6 / 1.2 | 8 / 3 | **joint jump 1.04 rad (Head_Yaw at 0.5 s)**; **root turn 8 deg/frame** *(excluded)* |
| `carla_1_3_3_t571-577_shift` | B | 6_carla_1_3_3 570.8–576.6 s | 10.2 / 5.7 | 23 / 11 | head at limit 28%; **joint jump 1.09 rad (Head_Yaw at 0.2 s)**; **root turn 9 deg/frame** *(excluded)* |
| `carla_1_3_3_t59-63_shift` | B | 6_carla_1_3_3 59.4–63.4 s | 21.3 / 5.4 | 13 / 4 | leg at limit 22%; **ground IK failed 19 frames**; outlier trunk drop (z +4.2); outlier knee max (z +7.2) *(excluded)* |
| `carla_1_3_3_t596-600` | A | 6_carla_1_3_3 596.0–600.0 s | 9.8 / 2.8 | 7 / 3 | leg at limit 8%; **ground IK failed 6 frames** *(excluded)* |
| `carla_1_3_3_t597-601_shift` | B | 6_carla_1_3_3 596.8–600.8 s | 19.5 / 5.2 | 7 / 3 | leg at limit 30%; **ground IK failed 29 frames**; outlier trunk drop (z +4.2); outlier knee max (z +7.9) *(excluded)* |
| `carla_1_3_3_t607-611` | A | 6_carla_1_3_3 607.0–611.1 s | 4.6 / 1.7 | 5 / 2 | head at limit 43%; **joint jump 0.91 rad (Head_Yaw at 0.5 s)** *(excluded)* |
| `carla_1_3_3_t608-612_shift` | B | 6_carla_1_3_3 608.2–612.2 s | 20.6 / 6.0 | 7 / 2 | head at limit 72%; leg at limit 9%; **ground IK failed 2 frames**; outlier knee max (z +6.4) *(excluded)* |
| `carla_1_3_3_t613-621` | A | 6_carla_1_3_3 613.0–621.2 s | 8.8 / 1.7 | 9 / 4 | **root turn 6 deg/frame** *(excluded)* |
| `carla_1_3_3_t622-626` | A | 6_carla_1_3_3 622.3–626.3 s | 4.9 / 2.1 | 14 / 7 | **joint jump 1.01 rad (Head_Yaw at 1.3 s)** *(excluded)* |
| `carla_1_3_3_t624-630_shift` | B | 6_carla_1_3_3 624.3–629.5 s | 14.3 / 3.8 | 12 / 4 | leg at limit 37%; outlier trunk drop (z +4.8); outlier knee max (z +7.4); **foot held 36 mm off the floor (median)** *(excluded)* |
| `carla_1_3_3_t662-668` | A | 6_carla_1_3_3 662.1–668.3 s | 5.5 / 1.9 | 13 / 6 | head at limit 6%; **joint jump 1.00 rad (Head_Yaw at 0.9 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_3_3_t666-670_shift` | B | 6_carla_1_3_3 666.3–670.3 s | 17.3 / 4.6 | 5 / 4 | knee 62 deg; leg at limit 13%; **ground IK failed 14 frames**; outlier knee max (z +8.8); **joint jump 0.92 rad (Head_Yaw at 2.5 s)**; **root turn 6 deg/frame** *(excluded)* |
| `carla_1_3_3_t671-680` | A | 6_carla_1_3_3 671.0–680.4 s | 6.6 / 3.4 | 14 / 5 | head at limit 62%; **root turn 9 deg/frame** *(excluded)* |
| `carla_1_3_3_t691-697` | A | 6_carla_1_3_3 691.2–697.3 s | 5.5 / 4.9 | 16 / 8 | **joint jump 1.08 rad (Head_Yaw at 4.2 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_3_3_t712-717` | A | 6_carla_1_3_3 712.5–717.2 s | 9.0 / 1.9 | 21 / 7 | head at limit 44%; **ground IK failed 1 frames** *(excluded)* |
| `carla_1_3_3_t714-718_shift` | B | 6_carla_1_3_3 714.0–718.0 s | 13.8 / 3.0 | 22 / 9 | head at limit 52%; leg at limit 22%; **ground IK failed 24 frames**; **joint jump 1.08 rad (Head_Yaw at 3.9 s)**; **root turn 8 deg/frame** *(excluded)* |
| `carla_1_3_3_t719-725_shift` | B | 6_carla_1_3_3 718.9–725.0 s | 23.1 / 12.3 | 30 / 12 | outlier knee max (z +4.6); **joint jump 1.11 rad (Head_Yaw at 2.0 s)**; **root turn 9 deg/frame** *(excluded)* |
| `carla_1_3_3_t72-77_shift` | B | 6_carla_1_3_3 71.7–76.7 s | 22.5 / 5.4 | 11 / 3 | knee 61 deg; leg at limit 15%; **ground IK failed 16 frames**; outlier trunk drop (z +4.2); outlier knee max (z +8.2) *(excluded)* |
| `carla_1_3_3_t732-741` | A | 6_carla_1_3_3 732.4–740.7 s | 2.5 / 1.5 | 20 / 10 | head at limit 15%; **joint jump 0.96 rad (Head_Yaw at 3.1 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_3_3_t745-764` | A | 6_carla_1_3_3 745.2–763.8 s | 2.5 / 0.6 | 14 / 6 | **self-collision head_2_collision / right_hand_end_collision 1.1 s (at 2.5 s, 36 mm)** *(excluded)* |
| `carla_1_3_3_t84-88_shift` | B | 6_carla_1_3_3 83.8–88.3 s | 16.1 / 4.1 | 25 / 11 | leg at limit 16%; **ground IK failed 21 frames**; outlier knee max (z +3.9) *(excluded)* |
| `carla_1_4_4_t115-119_shift` | B | 6_carla_1_4_4 115.1–119.2 s | 14.3 / 3.4 | 7 / 4 | leg at limit 8%; **ground IK failed 6 frames**; outlier trunk drop (z +5.2); outlier knee max (z +6.9); **foot held 41 mm off the floor (median)** *(excluded)* |
| `carla_1_4_4_t124-128_shift` | B | 6_carla_1_4_4 123.8–128.5 s | 19.9 / 6.3 | 11 / 5 | leg at limit 14%; **ground IK failed 11 frames**; outlier knee max (z +6.6); **joint jump 0.87 rad (Head_Yaw at 0.0 s)** *(excluded)* |
| `carla_1_4_4_t190-194_shift` | B | 6_carla_1_4_4 190.1–194.1 s | 20.5 / 5.8 | 3 / 2 | leg at limit 15%; **ground IK failed 14 frames**; outlier knee max (z +7.4) *(excluded)* |
| `carla_1_4_4_t208-212_shift` | B | 6_carla_1_4_4 208.0–212.3 s | 8.6 / 1.8 | 3 / 1 | leg at limit 38%; **ground IK failed 44 frames**; outlier trunk drop (z +3.7); outlier knee max (z +5.4); **foot held 40 mm off the floor (median)** *(excluded)* |
| `carla_1_4_4_t250-255_shift` | B | 6_carla_1_4_4 250.1–254.7 s | 6.9 / 4.0 | 16 / 5 | outlier knee max (z +6.2); **joint jump 1.06 rad (Head_Yaw at 3.1 s)** *(excluded)* |
| `carla_1_4_4_t256-261_shift` | B | 6_carla_1_4_4 256.1–261.2 s | 18.7 / 4.6 | 20 / 6 | head at limit 11%; **ground IK failed 4 frames**; outlier knee max (z +5.4); **joint jump 0.89 rad (Head_Yaw at 4.9 s)** *(excluded)* |
| `carla_1_4_4_t262-269` | A | 6_carla_1_4_4 262.1–268.9 s | 3.7 / 1.8 | 8 / 4 | head at limit 55%; **root turn 12 deg/frame** *(excluded)* |
| `carla_1_4_4_t275-281` | A | 6_carla_1_4_4 275.1–280.8 s | 8.7 / 5.5 | 10 / 4 | **joint jump 0.78 rad (Head_Yaw at 0.7 s)** *(excluded)* |
| `carla_1_4_4_t286-293` | A | 6_carla_1_4_4 286.5–293.2 s | 2.4 / 1.3 | 15 / 5 | head at limit 6%; **joint jump 1.09 rad (Head_Yaw at 3.0 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_4_4_t331-335` | A | 6_carla_1_4_4 331.3–335.3 s | 9.7 / 2.3 | 21 / 11 | **joint jump 0.99 rad (Head_Yaw at 1.3 s)**; **root turn 6 deg/frame** *(excluded)* |
| `carla_1_4_4_t338-347` | A | 6_carla_1_4_4 337.7–347.2 s | 2.8 / 1.7 | 14 / 4 | head at limit 57%; **joint jump 0.76 rad (Head_Yaw at 0.3 s)** *(excluded)* |
| `carla_1_4_4_t353-358` | A | 6_carla_1_4_4 353.4–358.1 s | 8.8 / 5.0 | 22 / 8 | head at limit 13%; **joint jump 0.85 rad (Head_Yaw at 2.4 s)**; **root turn 6 deg/frame** *(excluded)* |
| `carla_1_4_4_t359-363_shift` | B | 6_carla_1_4_4 359.2–363.2 s | 21.7 / 5.5 | 12 / 7 | leg at limit 14%; **ground IK failed 14 frames**; outlier knee max (z +5.5); **joint jump 1.05 rad (Head_Yaw at 1.4 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_4_4_t41-52` | A | 6_carla_1_4_4 41.3–52.3 s | 5.6 / 2.4 | 11 / 6 | **joint jump 1.07 rad (Head_Yaw at 9.3 s)** *(excluded)* |
| `carla_1_4_4_t413-424` | A | 6_carla_1_4_4 412.6–423.9 s | 8.2 / 4.3 | 9 / 4 | head at limit 42%; **joint jump 1.09 rad (Head_Yaw at 6.1 s)**; **root turn 6 deg/frame** *(excluded)* |
| `carla_1_4_4_t425-430_shift` | B | 6_carla_1_4_4 424.6–429.9 s | 19.5 / 4.6 | 12 / 4 | trunk drop 5 cm; knee 62 deg; head at limit 16%; leg at limit 24%; **ground IK failed 15 frames**; **outlier trunk drop (z +5.4)**; outlier knee max (z +8.5); **joint jump 0.63 rad (Head_Yaw at 0.9 s)**; **root turn 6 deg/frame** *(excluded)* |
| `carla_1_4_4_t442-457` | A | 6_carla_1_4_4 442.0–457.1 s | 10.0 / 3.7 | 15 / 6 | head at limit 28%; outlier knee max (z +6.3); **root turn 8 deg/frame** *(excluded)* |
| `carla_1_4_4_t457-469` | A | 6_carla_1_4_4 457.1–469.3 s | 8.6 / 1.8 | 17 / 7 | **joint jump 1.03 rad (Head_Yaw at 0.7 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_4_4_t475-488` | A | 6_carla_1_4_4 474.7–488.3 s | 3.8 / 1.5 | 10 / 5 | **self-collision head_2_collision / right_hand_end_collision 1.4 s (at 1.0 s, 31 mm)** *(excluded)* |
| `carla_1_4_4_t503-510` | A | 6_carla_1_4_4 502.9–510.2 s | 2.9 / 3.8 | 5 / 2 | head at limit 65%; **joint jump 1.08 rad (Head_Yaw at 2.1 s)** *(excluded)* |
| `carla_1_4_4_t537-541_shift` | B | 6_carla_1_4_4 537.2–541.3 s | 12.7 / 4.0 | 11 / 5 | head at limit 16%; outlier knee max (z +6.6); **joint jump 1.07 rad (Head_Yaw at 3.2 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_4_4_t589-593_shift` | B | 6_carla_1_4_4 589.2–593.2 s | 18.9 / 4.7 | 8 / 2 | trunk drop 5 cm; leg at limit 35%; **ground IK failed 16 frames**; **outlier trunk drop (z +5.9)**; outlier knee max (z +6.8) *(excluded)* |
| `carla_1_4_4_t598-603_shift` | B | 6_carla_1_4_4 598.4–603.2 s | 16.2 / 4.6 | 13 / 3 | leg at limit 9%; **ground IK failed 10 frames**; outlier trunk drop (z +3.6) *(excluded)* |
| `carla_1_4_4_t627-632_shift` | B | 6_carla_1_4_4 626.7–632.3 s | 20.4 / 10.6 | 22 / 8 | **self-collision head_2_collision / right_hand_end_collision 1.2 s (at 0.0 s, 38 mm)** *(excluded)* |
| `carla_1_4_4_t637-645` | A | 6_carla_1_4_4 636.9–645.4 s | 2.4 / 2.0 | 7 / 5 | head at limit 29%; **joint jump 1.10 rad (Head_Yaw at 2.5 s)**; **root turn 8 deg/frame** *(excluded)* |
| `carla_1_4_4_t79-93` | A | 6_carla_1_4_4 79.1–93.1 s | 1.8 / 0.9 | 10 / 5 | **self-collision head_2_collision / right_hand_end_collision 2.0 s (at 1.2 s, 43 mm)** *(excluded)* |
| `carla_1_4_4_t94-99_shift` | B | 6_carla_1_4_4 94.2–99.2 s | 18.4 / 5.8 | 3 / 1 | knee 77 deg; leg at limit 15%; **ground IK failed 19 frames**; outlier knee max (z +13.8) *(excluded)* |
| `carla_1_5_5_t120-126` | A | 6_carla_1_5_5 119.9–125.6 s | 5.0 / 1.9 | 7 / 5 | **joint jump 1.02 rad (Head_Yaw at 2.9 s)**; **root turn 6 deg/frame** *(excluded)* |
| `carla_1_5_5_t127-137` | A | 6_carla_1_5_5 126.5–136.9 s | 1.2 / 0.7 | 16 / 6 | **self-collision head_2_collision / right_hand_end_collision 2.3 s (at 5.6 s, 35 mm)** *(excluded)* |
| `carla_1_5_5_t13-17_shift` | B | 6_carla_1_5_5 12.8–16.8 s | 17.0 / 6.3 | 7 / 2 | knee 61 deg; leg at limit 38%; **ground IK failed 38 frames**; outlier knee max (z +8.3) *(excluded)* |
| `carla_1_5_5_t160-177` | A | 6_carla_1_5_5 160.0–176.6 s | 7.8 / 8.3 | 8 / 3 | K1 feet move 8 cm; head at limit 10%; **joint jump 0.99 rad (Head_Yaw at 11.2 s)** *(excluded)* |
| `carla_1_5_5_t177-186` | A | 6_carla_1_5_5 177.4–185.6 s | 4.8 / 1.8 | 4 / 3 | head at limit 70%; **joint jump 1.06 rad (Head_Yaw at 0.8 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_5_5_t183-187_shift` | B | 6_carla_1_5_5 183.1–187.1 s | 16.9 / 4.7 | 6 / 3 | head at limit 53%; leg at limit 30%; **ground IK failed 16 frames**; outlier knee max (z +4.4); **joint jump 0.74 rad (Head_Yaw at 2.1 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_5_5_t213-218_shift` | B | 6_carla_1_5_5 213.1–218.2 s | 22.0 / 10.6 | 16 / 3 | knee 72 deg; leg at limit 34%; **ground IK failed 48 frames**; outlier knee max (z +12.2); **joint jump 1.21 rad (Right_Ankle_Pitch at 4.4 s)**; **Right_Ankle_Roll over its speed limit for 0.17 s (at 4.7 s)** *(excluded)* |
| `carla_1_5_5_t219-234` | A | 6_carla_1_5_5 219.0–234.0 s | 4.2 / 1.4 | 6 / 3 | **joint jump 1.03 rad (Head_Yaw at 11.6 s)**; **root turn 6 deg/frame** *(excluded)* |
| `carla_1_5_5_t247-253_shift` | B | 6_carla_1_5_5 246.9–252.9 s | 16.8 / 10.2 | 14 / 7 | shoulder at limit 29%; outlier knee max (z +6.2); **joint jump 1.33 rad (Left_Shoulder_Pitch at 1.7 s)**; **root turn 34 deg/frame** *(excluded)* |
| `carla_1_5_5_t269-274_shift` | B | 6_carla_1_5_5 269.1–274.1 s | 20.5 / 4.9 | 21 / 8 | head at limit 11%; outlier trunk drop (z +3.9); outlier knee max (z +5.9); **joint jump 0.92 rad (Head_Yaw at 1.1 s)** *(excluded)* |
| `carla_1_5_5_t275-285` | A | 6_carla_1_5_5 274.7–285.2 s | 6.6 / 4.0 | 21 / 7 | **joint jump 0.95 rad (Head_Yaw at 1.8 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_5_5_t309-323` | A | 6_carla_1_5_5 308.8–322.7 s | 3.4 / 0.6 | 7 / 4 | head at limit 28%; **joint jump 0.97 rad (Head_Yaw at 4.6 s)** *(excluded)* |
| `carla_1_5_5_t329-342` | A | 6_carla_1_5_5 329.2–341.7 s | 6.9 / 2.4 | 9 / 6 | head at limit 80%; **joint jump 0.77 rad (Head_Yaw at 10.0 s)**; **root turn 8 deg/frame** *(excluded)* |
| `carla_1_5_5_t343-357` | A | 6_carla_1_5_5 342.9–357.0 s | 9.4 / 3.2 | 11 / 4 | leg at limit 6%; **ground IK failed 10 frames**; **joint jump 0.76 rad (Head_Yaw at 11.1 s)**; **root turn 8 deg/frame** *(excluded)* |
| `carla_1_5_5_t353-357_shift` | B | 6_carla_1_5_5 353.4–357.4 s | 4.8 / 1.4 | 13 / 6 | head at limit 12%; leg at limit 17%; **ground IK failed 13 frames**; **joint jump 0.76 rad (Head_Yaw at 0.6 s)**; **root turn 8 deg/frame** *(excluded)* |
| `carla_1_5_5_t367-371_shift` | B | 6_carla_1_5_5 366.5–370.5 s | 18.5 / 5.0 | 8 / 2 | trunk drop 5 cm; leg at limit 11%; **outlier trunk drop (z +5.4)**; outlier knee max (z +4.8) *(excluded)* |
| `carla_1_5_5_t379-383_shift` | B | 6_carla_1_5_5 379.1–383.1 s | 15.4 / 4.2 | 12 / 5 | leg at limit 20%; **ground IK failed 17 frames**; outlier knee max (z +7.6) *(excluded)* |
| `carla_1_5_5_t399-403_shift` | B | 6_carla_1_5_5 398.5–402.5 s | 17.2 / 4.3 | 15 / 5 | knee 73 deg; leg at limit 38%; **ground IK failed 43 frames**; outlier knee max (z +12.5) *(excluded)* |
| `carla_1_5_5_t420-424_shift` | B | 6_carla_1_5_5 420.5–424.5 s | 18.3 / 4.6 | 43 / 13 | leg at limit 21%; **ground IK failed 2 frames**; outlier trunk drop (z +4.2); outlier knee max (z +7.3) *(excluded)* |
| `carla_1_5_5_t71-88` | A | 6_carla_1_5_5 71.0–87.8 s | 4.4 / 2.0 | 15 / 5 | **self-collision head_2_collision / left_hand_end_collision 1.0 s (at 1.0 s, 34 mm)** *(excluded)* |
| `carla_1_5_5_t94-98_shift` | B | 6_carla_1_5_5 93.6–97.6 s | 15.3 / 7.7 | 14 / 5 | leg at limit 35%; **ground IK failed 39 frames**; outlier knee max (z +6.9) *(excluded)* |
| `carla_1_6_6_t11-17` | A | 6_carla_1_6_6 11.2–17.1 s | 3.7 / 1.2 | 12 / 4 | head at limit 53%; **joint jump 0.77 rad (Head_Yaw at 1.2 s)** *(excluded)* |
| `carla_1_6_6_t128-135` | A | 6_carla_1_6_6 127.7–134.6 s | 3.6 / 1.9 | 2 / 4 | head at limit 29%; **joint jump 1.11 rad (Head_Yaw at 3.0 s)** *(excluded)* |
| `carla_1_6_6_t136-140` | A | 6_carla_1_6_6 135.6–140.3 s | 4.3 / 5.1 | 4 / 3 | **joint jump 0.95 rad (Head_Yaw at 0.4 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_6_6_t142-154` | A | 6_carla_1_6_6 141.9–154.0 s | 4.7 / 2.7 | 5 / 3 | **joint jump 1.02 rad (Head_Yaw at 1.5 s)** *(excluded)* |
| `carla_1_6_6_t212-221` | A | 6_carla_1_6_6 212.3–221.4 s | 5.0 / 2.0 | 21 / 10 | **joint jump 0.61 rad (Head_Yaw at 1.6 s)** *(excluded)* |
| `carla_1_6_6_t219-224_shift` | B | 6_carla_1_6_6 219.4–224.2 s | 24.3 / 14.4 | 21 / 6 | knee 60 deg; head at limit 76%; shoulder at limit 85%; outlier knee max (z +8.2); **trunk leans 28 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `carla_1_6_6_t234-240` | A | 6_carla_1_6_6 234.4–239.5 s | 7.7 / 4.6 | 11 / 4 | **joint jump 0.94 rad (Head_Yaw at 3.2 s)** *(excluded)* |
| `carla_1_6_6_t255-263` | A | 6_carla_1_6_6 255.2–263.4 s | 4.8 / 2.5 | 6 / 3 | **joint jump 1.09 rad (Head_Yaw at 7.5 s)** *(excluded)* |
| `carla_1_6_6_t26-33_shift` | B | 6_carla_1_6_6 26.1–33.5 s | 21.9 / 5.7 | 13 / 7 | outlier knee max (z +6.2); **joint jump 1.06 rad (Head_Yaw at 1.6 s)**; **Head_Yaw over its speed limit for 0.13 s (at 1.2 s)** *(excluded)* |
| `carla_1_6_6_t288-292` | A | 6_carla_1_6_6 287.9–292.1 s | 5.6 / 2.1 | 8 / 3 | **joint jump 1.05 rad (Head_Yaw at 1.2 s)** *(excluded)* |
| `carla_1_6_6_t289-293_shift` | B | 6_carla_1_6_6 289.2–293.2 s | 20.6 / 6.0 | 6 / 2 | leg at limit 22%; **ground IK failed 18 frames**; outlier knee max (z +4.1); **joint jump 0.98 rad (Head_Yaw at 0.1 s)** *(excluded)* |
| `carla_1_6_6_t294-309` | A | 6_carla_1_6_6 294.3–309.3 s | 5.1 / 2.1 | 7 / 4 | head at limit 10%; **joint jump 1.03 rad (Head_Yaw at 4.3 s)** *(excluded)* |
| `carla_1_6_6_t314-322_shift` | B | 6_carla_1_6_6 313.6–321.7 s | 10.3 / 7.2 | 15 / 4 | leg at limit 12%; **ground IK failed 13 frames**; outlier trunk drop (z +3.8); outlier knee max (z +3.9) *(excluded)* |
| `carla_1_6_6_t316-321` | A | 6_carla_1_6_6 316.3–320.9 s | 9.7 / 4.4 | 15 / 4 | leg at limit 21%; **ground IK failed 13 frames**; outlier trunk drop (z +3.5); outlier knee max (z +3.9) *(excluded)* |
| `carla_1_6_6_t353-359` | A | 6_carla_1_6_6 353.0–359.1 s | 7.4 / 2.8 | 19 / 5 | **joint jump 1.03 rad (Head_Yaw at 2.4 s)** *(excluded)* |
| `carla_1_6_6_t356-360_shift` | B | 6_carla_1_6_6 356.0–360.0 s | 22.8 / 5.8 | 10 / 4 | head at limit 8%; leg at limit 15%; **ground IK failed 14 frames**; outlier knee max (z +6.2); **joint jump 0.83 rad (Head_Yaw at 1.2 s)** *(excluded)* |
| `carla_1_6_6_t361-371` | A | 6_carla_1_6_6 360.9–371.1 s | 4.0 / 2.0 | 12 / 5 | **joint jump 1.07 rad (Head_Yaw at 9.6 s)**; **root turn 6 deg/frame** *(excluded)* |
| `carla_1_6_6_t372-376` | A | 6_carla_1_6_6 372.0–376.4 s | 8.4 / 2.7 | 10 / 6 | **joint jump 1.02 rad (Head_Yaw at 1.8 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_6_6_t373-377_shift` | B | 6_carla_1_6_6 373.0–377.0 s | 16.9 / 3.2 | 11 / 7 | **joint jump 1.02 rad (Head_Yaw at 0.8 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_6_6_t381-393` | A | 6_carla_1_6_6 381.1–393.3 s | 5.8 / 1.9 | 7 / 4 | head at limit 9%; **root turn 8 deg/frame**; **foot held 34 mm off the floor (median)** *(excluded)* |
| `carla_1_6_6_t391-397_shift` | B | 6_carla_1_6_6 391.3–397.1 s | 13.1 / 11.4 | 8 / 5 | shoulder at limit 38%; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `carla_1_6_6_t76-84_shift` | B | 6_carla_1_6_6 75.7–84.1 s | 19.5 / 9.5 | 34 / 12 | knee 62 deg; leg at limit 40%; **ground IK failed 99 frames**; outlier knee max (z +8.5) *(excluded)* |
| `carla_1_6_6_t99-104_shift` | B | 6_carla_1_6_6 99.2–104.5 s | 17.9 / 3.9 | 17 / 8 | knee 62 deg; leg at limit 20%; **ground IK failed 26 frames**; outlier knee max (z +8.8) *(excluded)* |
| `carla_1_7_7_t108-112_shift` | B | 6_carla_1_7_7 107.5–111.5 s | 19.9 / 5.4 | 5 / 1 | leg at limit 17%; **ground IK failed 17 frames**; outlier knee max (z +4.9) *(excluded)* |
| `carla_1_7_7_t127-132_shift` | B | 6_carla_1_7_7 127.1–131.5 s | 16.3 / 5.0 | 11 / 3 | leg at limit 14%; **ground IK failed 4 frames**; outlier trunk drop (z +3.6); outlier knee max (z +6.5) *(excluded)* |
| `carla_1_7_7_t132-141_shift` | B | 6_carla_1_7_7 132.3–141.3 s | 15.2 / 5.5 | 18 / 7 | knee 64 deg; leg at limit 17%; **ground IK failed 18 frames**; outlier trunk drop (z +4.5); outlier knee max (z +9.2) *(excluded)* |
| `carla_1_7_7_t164-168` | A | 6_carla_1_7_7 164.0–168.3 s | 3.7 / 2.4 | 21 / 12 | head at limit 30%; **joint jump 0.80 rad (Head_Yaw at 0.7 s)**; **root turn 11 deg/frame** *(excluded)* |
| `carla_1_7_7_t176-183` | A | 6_carla_1_7_7 175.7–183.3 s | 2.7 / 1.3 | 5 / 2 | head at limit 7%; **joint jump 0.94 rad (Head_Yaw at 6.5 s)**; **root turn 6 deg/frame** *(excluded)* |
| `carla_1_7_7_t199-205` | A | 6_carla_1_7_7 198.7–205.0 s | 9.9 / 2.6 | 17 / 7 | leg at limit 9%; **ground IK failed 10 frames** *(excluded)* |
| `carla_1_7_7_t205-213` | A | 6_carla_1_7_7 205.0–213.0 s | 9.0 / 4.2 | 33 / 12 | leg at limit 15%; **ground IK failed 36 frames**; outlier knee max (z +6.8) *(excluded)* |
| `carla_1_7_7_t214-218` | A | 6_carla_1_7_7 213.8–218.4 s | 2.0 / 1.5 | 30 / 14 | shoulder at limit 21%; leg at limit 7%; **ground IK failed 14 frames**; **joint jump 0.82 rad (Right_Elbow_Pitch at 3.9 s)**; **root turn 16 deg/frame** *(excluded)* |
| `carla_1_7_7_t265-270_shift` | B | 6_carla_1_7_7 265.4–270.1 s | 19.3 / 5.9 | 26 / 7 | leg at limit 9%; **ground IK failed 7 frames**; outlier trunk drop (z +4.0); outlier knee max (z +7.1) *(excluded)* |
| `carla_1_7_7_t302-306_shift` | B | 6_carla_1_7_7 301.7–305.7 s | 21.8 / 5.6 | 7 / 3 | outlier knee max (z +8.0); **joint jump 1.06 rad (Head_Yaw at 3.4 s)** *(excluded)* |
| `carla_1_7_7_t319-329` | A | 6_carla_1_7_7 318.6–329.2 s | 4.9 / 2.1 | 15 / 5 | **joint jump 0.84 rad (Head_Yaw at 10.4 s)** *(excluded)* |
| `carla_1_7_7_t326-330_shift` | B | 6_carla_1_7_7 326.2–330.2 s | 16.1 / 3.5 | 14 / 5 | knee 65 deg; head at limit 28%; outlier knee max (z +9.8); **joint jump 0.84 rad (Head_Yaw at 2.7 s)** *(excluded)* |
| `carla_1_7_7_t341-345` | A | 6_carla_1_7_7 340.6–345.5 s | 9.3 / 2.7 | 11 / 7 | **joint jump 0.99 rad (Head_Yaw at 4.6 s)** *(excluded)* |
| `carla_1_7_7_t342-346_shift` | B | 6_carla_1_7_7 341.5–345.5 s | 9.0 / 2.3 | 11 / 8 | **joint jump 0.99 rad (Head_Yaw at 3.7 s)** *(excluded)* |
| `carla_1_7_7_t349-367` | A | 6_carla_1_7_7 348.8–366.7 s | 3.3 / 2.1 | 5 / 2 | head at limit 39%; **joint jump 0.95 rad (Head_Yaw at 6.3 s)** *(excluded)* |
| `carla_1_7_7_t443-449` | A | 6_carla_1_7_7 443.4–448.6 s | 2.0 / 0.6 | 15 / 6 | leg at limit 100%; **ground IK failed 155 frames**; outlier knee max (z -5.3) *(excluded)* |
| `carla_1_7_7_t454-460` | A | 6_carla_1_7_7 454.0–460.1 s | 9.0 / 1.8 | 17 / 7 | head at limit 6%; **joint jump 0.76 rad (Head_Yaw at 5.6 s)** *(excluded)* |
| `carla_1_7_7_t461-468` | A | 6_carla_1_7_7 460.9–467.9 s | 4.7 / 1.0 | 16 / 6 | head at limit 38%; **joint jump 0.70 rad (Head_Yaw at 2.7 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_7_7_t529-534_shift` | B | 6_carla_1_7_7 528.6–533.9 s | 19.2 / 4.7 | 8 / 3 | leg at limit 16%; **ground IK failed 21 frames** *(excluded)* |
| `carla_1_7_7_t54-63` | A | 6_carla_1_7_7 53.8–62.7 s | 3.9 / 2.0 | 8 / 3 | head at limit 9%; **joint jump 1.11 rad (Head_Yaw at 1.9 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_7_7_t558-569` | A | 6_carla_1_7_7 557.7–569.1 s | 5.5 / 2.4 | 3 / 2 | head at limit 28%; **joint jump 1.10 rad (Head_Yaw at 3.1 s)** *(excluded)* |
| `carla_1_7_7_t584-592_shift` | B | 6_carla_1_7_7 583.9–592.3 s | 11.1 / 4.4 | 40 / 19 | trunk drop 7 cm; **ground IK failed 9 frames**; **outlier trunk drop (z +7.9)**; outlier knee max (z +7.8) *(excluded)* |
| `carla_1_8_8_t159-163_shift` | B | 6_carla_1_8_8 158.9–162.9 s | 19.1 / 4.2 | 32 / 11 | leg at limit 18%; **ground IK failed 22 frames**; outlier knee max (z +4.8) *(excluded)* |
| `carla_1_8_8_t227-231_shift` | B | 6_carla_1_8_8 226.8–230.8 s | 18.9 / 5.5 | 20 / 7 | leg at limit 10%; **ground IK failed 7 frames**; outlier trunk drop (z +3.8); outlier knee max (z +5.6) *(excluded)* |
| `carla_1_8_8_t298-302_shift` | B | 6_carla_1_8_8 297.9–302.5 s | 18.3 / 4.6 | 8 / 4 | leg at limit 11%; **ground IK failed 10 frames**; outlier knee max (z +5.8) *(excluded)* |
| `carla_1_8_8_t312-318_shift` | B | 6_carla_1_8_8 311.8–317.6 s | 17.4 / 3.8 | 37 / 12 | knee 60 deg; upper-arm twist at limit 27%; leg at limit 17%; **ground IK failed 25 frames**; outlier trunk drop (z +4.3); outlier knee max (z +8.2) *(excluded)* |
| `carla_1_8_8_t355-360` | A | 6_carla_1_8_8 355.3–360.3 s | 9.5 / 4.3 | 39 / 14 | **joint jump 0.75 rad (Left_Elbow_Pitch at 4.5 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_8_8_t357-361_shift` | B | 6_carla_1_8_8 357.1–361.1 s | 18.8 / 4.9 | 50 / 18 | outlier knee max (z +5.2); **joint jump 0.75 rad (Left_Elbow_Pitch at 2.7 s)**; **root turn 7 deg/frame** *(excluded)* |
| `carla_1_8_8_t417-421_shift` | B | 6_carla_1_8_8 416.7–420.9 s | 17.3 / 4.4 | 12 / 3 | trunk drop 7 cm; knee 60 deg; leg at limit 15%; **ground IK failed 9 frames**; **outlier trunk drop (z +7.4)**; outlier knee max (z +8.2); **joint jump 0.61 rad (Right_Knee_Pitch at 0.3 s)**; **foot held 41 mm off the floor (median)** *(excluded)* |
| `carla_1_8_8_t42-47_shift` | B | 6_carla_1_8_8 42.0–46.7 s | 17.0 / 3.8 | 12 / 2 | leg at limit 27%; **ground IK failed 17 frames**; outlier knee max (z +4.7) *(excluded)* |
| `carla_1_8_8_t510-515_shift` | B | 6_carla_1_8_8 510.1–515.0 s | 19.1 / 4.9 | 36 / 11 | outlier trunk drop (z +5.1); outlier knee max (z +6.9); **foot held 33 mm off the floor (median)** *(excluded)* |
| `carla_1_8_8_t558-562_shift` | B | 6_carla_1_8_8 557.5–561.5 s | 16.1 / 4.3 | 12 / 3 | leg at limit 27%; **ground IK failed 26 frames**; outlier trunk drop (z +3.6) *(excluded)* |
| `carla_1_8_8_t637-641_shift` | B | 6_carla_1_8_8 637.4–641.4 s | 12.3 / 3.2 | 16 / 5 | leg at limit 14%; **ground IK failed 16 frames** *(excluded)* |
| `carla_1_8_8_t658-667_shift` | B | 6_carla_1_8_8 657.9–667.1 s | 19.0 / 13.0 | 10 / 3 | **ground IK failed 9 frames**; outlier knee max (z +7.9) *(excluded)* |
| `carla_1_8_8_t95-102` | A | 6_carla_1_8_8 94.5–101.9 s | 1.3 / 0.7 | 8 / 3 | leg at limit 100%; **ground IK failed 221 frames**; outlier knee max (z -7.5) *(excluded)* |
| `carla_1_9_9_t122-126_shift` | B | 6_carla_1_9_9 121.8–125.8 s | 14.1 / 3.6 | 11 / 3 | leg at limit 24%; outlier trunk drop (z +5.2); outlier knee max (z +4.4); **foot held 39 mm off the floor (median)** *(excluded)* |
| `carla_1_9_9_t175-180_shift` | B | 6_carla_1_9_9 174.8–179.7 s | 22.4 / 6.1 | 13 / 5 | trunk drop 7 cm; leg at limit 25%; **ground IK failed 2 frames**; **outlier trunk drop (z +7.9)**; outlier knee max (z +7.4); **foot held 31 mm off the floor (median)** *(excluded)* |
| `carla_1_9_9_t186-199_shift` | B | 6_carla_1_9_9 185.8–199.4 s | 21.2 / 9.0 | 19 / 8 | trunk drop 7 cm; knee 61 deg; leg at limit 29%; **ground IK failed 66 frames**; **outlier trunk drop (z +8.0)**; outlier knee max (z +8.5) *(excluded)* |
| `carla_1_9_9_t492-496_shift` | B | 6_carla_1_9_9 491.9–495.9 s | 17.9 / 5.3 | 11 / 4 | knee 83 deg; leg at limit 13%; outlier trunk drop (z +4.6); outlier knee max (z +15.7); **foot held 41 mm off the floor (median)** *(excluded)* |
| `carla_1_9_9_t554-565_shift` | B | 6_carla_1_9_9 554.3–565.0 s | 22.3 / 14.5 | 17 / 7 | leg at limit 13%; **ground IK failed 11 frames**; outlier trunk drop (z +4.9); outlier knee max (z +4.3); **foot held 40 mm off the floor (median)** *(excluded)* |
| `carla_1_9_9_t615-620_shift` | B | 6_carla_1_9_9 615.3–619.5 s | 17.9 / 3.8 | 8 / 3 | leg at limit 16%; **ground IK failed 3 frames**; outlier trunk drop (z +5.0); outlier knee max (z +4.7) *(excluded)* |
| `carlos_0_15_15_t72-88` | A | 15_carlos_0_15_15 72.4–87.6 s | 7.6 / 4.3 | 23 / 8 | **self-collision right_hand_collision / trunk_collision 1.7 s (at 8.2 s, 27 mm)** *(excluded)* |
| `carlos_0_2_2_t0-19` | A | 15_carlos_0_2_2 0.0–18.9 s | 1.5 / 1.3 | 17 / 6 | **joint jump 1.48 rad (Left_Shoulder_Pitch at 1.0 s)**; **root turn 33 deg/frame** *(excluded)* |
| `carlos_0_4_4_t0-14` | A | 15_carlos_0_4_4 0.0–14.4 s | 1.3 / 1.4 | 19 / 7 | shoulder at limit 7%; **joint jump 1.50 rad (Left_Elbow_Pitch at 1.0 s)**; **root turn 32 deg/frame** *(excluded)* |
| `carlos_0_82_82_t51-69` | A | 15_carlos_0_82_82 51.4–68.6 s | 1.0 / 0.5 | 15 / 5 | **self-collision right_hand_collision / trunk_collision 3.7 s (at 11.7 s, 28 mm)** *(excluded)* |
| `daiki_0_4_4_t81-85_shift` | B | 18_daiki_0_4_4 81.2–85.4 s | 13.8 / 16.1 | 15 / 10 | head at limit 17%; **joint jump 0.77 rad (Left_Shoulder_Roll at 2.1 s)**; **root jump 20.2 cm/frame**; **root turn 17 deg/frame**; **left foot slides 5.9 cm in one frame (at 2.1 s)** *(excluded)* |
| `daiki_0_73_73_t5-21_shift` | B | 18_daiki_0_73_73 5.1–20.6 s | 18.2 / 9.8 | 29 / 10 | **root turn 6 deg/frame** *(excluded)* |
| `daiki_0_8_8_t27-32_shift` | B | 18_daiki_0_8_8 27.5–31.7 s | 12.5 / 18.8 | 40 / 12 | K1 feet move 19 cm; head at limit 32%; **ground IK failed 1 frames**; **root jump 16.4 cm/frame**; **root turn 30 deg/frame** *(excluded)* |
| `daiki_0_8_8_t30-49` | A | 18_daiki_0_8_8 29.7–48.9 s | 1.3 / 0.7 | 15 / 5 | head at limit 25%; **joint jump 1.47 rad (Left_Shoulder_Pitch at 0.3 s)**; **root jump 3.1 cm/frame**; **root turn 21 deg/frame** *(excluded)* |
| `daiki_0_9_9_t2-19` | A | 18_daiki_0_9_9 2.0–18.7 s | 2.0 / 0.7 | 22 / 7 | **root turn 8 deg/frame** *(excluded)* |
| `goto_0_14_14_t71-89` | A | 25_goto_0_14_14 71.2–89.0 s | 0.4 / 0.2 | 8 / 3 | **root turn 7 deg/frame** *(excluded)* |
| `goto_0_96_96_t16-33` | A | 25_goto_0_96_96 16.4–32.8 s | 0.5 / 0.3 | 12 / 5 | **joint jump 0.83 rad (Left_Shoulder_Roll at 16.0 s)** *(excluded)* |
| `goto_1_1_1_t106-126` | A | 25_goto_1_1_1 106.5–126.1 s | 0.6 / 1.2 | 9 / 4 | head at limit 25%; shoulder at limit 27%; **joint jump 1.32 rad (Left_Elbow_Yaw at 6.1 s)**; **root turn 42 deg/frame**; left arm behind body 5 cm (human's in front) *(excluded)* |
| `goto_1_1_1_t421-440` | A | 25_goto_1_1_1 420.7–440.4 s | 0.9 / 1.2 | 13 / 4 | head at limit 97%; shoulder at limit 98%; elbow bend at limit 8%; **trunk leans 30 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `goto_1_2_2_t274-294` | A | 25_goto_1_2_2 274.1–293.7 s | 0.7 / 1.0 | 10 / 3 | head at limit 98%; shoulder at limit 99%; **trunk leans 31 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `hailing_0_103_103_t0-19` | A | 23_hailing_0_103_103 0.0–19.2 s | 5.9 / 3.4 | 28 / 9 | shoulder at limit 6%; **joint jump 1.40 rad (Left_Shoulder_Pitch at 0.7 s)**; **root jump 3.8 cm/frame**; **root turn 28 deg/frame** *(excluded)* |
| `hailing_0_104_104_t0-17` | A | 23_hailing_0_104_104 0.0–16.6 s | 4.3 / 4.1 | 19 / 6 | head at limit 98%; shoulder at limit 100%; **trunk leans 32 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `hailing_0_104_104_t17-33` | A | 23_hailing_0_104_104 16.6–33.1 s | 7.2 / 3.5 | 23 / 8 | **joint jump 1.19 rad (Left_Elbow_Pitch at 2.7 s)**; **root turn 16 deg/frame** *(excluded)* |
| `hailing_0_111_111_t0-18` | A | 23_hailing_0_111_111 0.0–18.4 s | 5.1 / 4.2 | 26 / 9 | **joint jump 1.37 rad (Left_Shoulder_Pitch at 0.7 s)**; **root jump 4.3 cm/frame**; **root turn 28 deg/frame** *(excluded)* |
| `hailing_0_16_16_t42-56` | A | 23_hailing_0_16_16 42.2–56.3 s | 5.4 / 1.9 | 41 / 12 | **root turn 6 deg/frame** *(excluded)* |
| `hailing_0_65_65_t0-5_shift` | B | 23_hailing_0_65_65 0.0–4.5 s | 10.8 / 5.8 | 35 / 14 | shoulder at limit 14%; outlier knee max (z +3.5); **joint jump 1.39 rad (Left_Shoulder_Pitch at 0.8 s)**; **root jump 4.0 cm/frame**; **root turn 25 deg/frame** *(excluded)* |
| `hailing_0_81_81_t0-17` | A | 23_hailing_0_81_81 0.0–16.7 s | 3.3 / 1.6 | 26 / 8 | **joint jump 1.45 rad (Left_Shoulder_Pitch at 0.7 s)**; **root jump 3.7 cm/frame**; **root turn 23 deg/frame**; self-collision right_hand_collision / trunk_collision 1.2 s (at 15.5 s, 15 mm) *(excluded)* |
| `hailing_0_87_87_t0-20` | A | 23_hailing_0_87_87 0.0–19.9 s | 4.2 / 17.5 | 26 / 9 | K1 feet move 18 cm; shoulder at limit 6%; leg at limit 21%; **ground IK failed 37 frames**; outlier trunk drop (z +4.9); outlier knee max (z +7.8); **joint jump 1.43 rad (Left_Shoulder_Pitch at 0.5 s)**; **root jump 15.9 cm/frame**; **root turn 27 deg/frame**; self-collision right_hand_collision / trunk_collision 0.3 s (at 10.4 s, 10 mm); **foot held 32 mm off the floor (median)** *(excluded)* |
| `hailing_0_95_95_t0-16` | A | 23_hailing_0_95_95 0.0–15.9 s | 3.1 / 2.7 | 28 / 9 | **joint jump 1.45 rad (Left_Shoulder_Pitch at 0.7 s)**; **root jump 3.8 cm/frame**; **root turn 25 deg/frame** *(excluded)* |
| `hailing_1_2_2_t0-19` | A | 23_hailing_1_2_2 0.0–19.0 s | 6.2 / 3.1 | 23 / 8 | head at limit 100%; outlier knee max (z +3.9); **joint jump 1.71 rad (Left_Shoulder_Pitch at 0.3 s)**; **root turn 20 deg/frame**; **trunk leans 25 deg (median)**; **self-collision left_foot_collision / right_foot_collision 1.4 s (at 6.1 s, 27 mm)**; **feet overlap 27 mm for 1.4 s (at 6.1 s)** *(excluded)* |
| `hailing_1_2_2_t103-117` | A | 23_hailing_1_2_2 103.4–117.2 s | 6.6 / 2.8 | 21 / 9 | head at limit 100%; outlier knee max (z +6.7); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t115-120_shift` | B | 23_hailing_1_2_2 115.2–119.7 s | 8.8 / 4.6 | 27 / 11 | head at limit 100%; outlier knee max (z +7.0); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t118-126` | A | 23_hailing_1_2_2 117.7–126.1 s | 5.7 / 2.8 | 21 / 7 | head at limit 100%; **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t124-129_shift` | B | 23_hailing_1_2_2 124.1–128.7 s | 9.6 / 5.6 | 20 / 7 | knee 66 deg; head at limit 100%; outlier knee max (z +9.9); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t127-140` | A | 23_hailing_1_2_2 126.7–139.8 s | 4.8 / 2.0 | 17 / 7 | head at limit 100%; outlier knee max (z +5.4); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t140-153` | A | 23_hailing_1_2_2 139.8–153.0 s | 6.5 / 3.1 | 21 / 9 | head at limit 100%; outlier knee max (z +5.0); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t156-176` | A | 23_hailing_1_2_2 156.3–176.2 s | 8.3 / 3.7 | 19 / 8 | head at limit 100%; outlier knee max (z +5.1); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t176-196` | A | 23_hailing_1_2_2 176.2–196.2 s | 6.7 / 2.7 | 20 / 9 | head at limit 100%; outlier knee max (z +5.3); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t19-38` | A | 23_hailing_1_2_2 19.0–37.9 s | 2.8 / 1.9 | 16 / 8 | head at limit 100%; **trunk leans 24 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.6 s (at 3.9 s, 13 mm); **feet overlap 13 mm for 0.6 s (at 3.9 s)** *(excluded)* |
| `hailing_1_2_2_t196-216` | A | 23_hailing_1_2_2 196.2–216.2 s | 6.7 / 3.6 | 21 / 9 | head at limit 100%; outlier knee max (z +6.1); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t216-236` | A | 23_hailing_1_2_2 216.2–236.2 s | 7.6 / 3.3 | 25 / 12 | head at limit 100%; **ground IK failed 13 frames**; outlier trunk drop (z +4.5); outlier knee max (z +5.7); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t236-256` | A | 23_hailing_1_2_2 236.2–256.1 s | 6.0 / 2.6 | 22 / 11 | head at limit 100%; **ground IK failed 5 frames**; outlier trunk drop (z +4.8); outlier knee max (z +5.2); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t257-262_shift` | B | 23_hailing_1_2_2 257.0–261.6 s | 19.1 / 11.0 | 22 / 10 | head at limit 100%; leg at limit 12%; **ground IK failed 7 frames**; outlier knee max (z +6.9); **trunk leans 28 deg (median)** *(excluded)* |
| `hailing_1_2_2_t260-266` | A | 23_hailing_1_2_2 259.6–266.0 s | 10.0 / 4.8 | 26 / 13 | head at limit 100%; outlier knee max (z +6.0); **trunk leans 27 deg (median)** *(excluded)* |
| `hailing_1_2_2_t264-274_shift` | B | 23_hailing_1_2_2 264.0–273.5 s | 21.2 / 11.4 | 29 / 13 | head at limit 100%; leg at limit 7%; **ground IK failed 14 frames**; outlier trunk drop (z +4.7); outlier knee max (z +6.8); **trunk leans 25 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.9 s (at 7.5 s, 22 mm); **feet overlap 22 mm for 0.9 s (at 7.5 s)** *(excluded)* |
| `hailing_1_2_2_t274-281_shift` | B | 23_hailing_1_2_2 274.4–280.5 s | 17.2 / 11.6 | 25 / 11 | knee 60 deg; head at limit 100%; leg at limit 7%; **ground IK failed 7 frames**; outlier knee max (z +8.2); **trunk leans 27 deg (median)** *(excluded)* |
| `hailing_1_2_2_t279-293` | A | 23_hailing_1_2_2 278.5–293.0 s | 5.4 / 1.8 | 20 / 9 | head at limit 100%; outlier knee max (z +6.8); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t293-307` | A | 23_hailing_1_2_2 293.0–307.5 s | 10.0 / 3.6 | 18 / 9 | head at limit 100%; **ground IK failed 12 frames**; outlier trunk drop (z +5.0); outlier knee max (z +6.9); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t307-322` | A | 23_hailing_1_2_2 307.5–321.9 s | 9.6 / 3.8 | 20 / 7 | trunk drop 5 cm; head at limit 100%; shoulder at limit 98%; leg at limit 27%; **ground IK failed 90 frames**; **outlier trunk drop (z +5.3)**; outlier knee max (z +6.1); **trunk leans 43 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `hailing_1_2_2_t322-337` | A | 23_hailing_1_2_2 321.9–337.3 s | 5.1 / 2.6 | 31 / 10 | head at limit 100%; leg at limit 6%; outlier knee max (z +6.5); **trunk leans 28 deg (median)** *(excluded)* |
| `hailing_1_2_2_t337-353` | A | 23_hailing_1_2_2 337.3–352.8 s | 7.4 / 3.0 | 31 / 16 | head at limit 100%; leg at limit 9%; **ground IK failed 25 frames**; outlier trunk drop (z +4.9); outlier knee max (z +7.5); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t368-372` | A | 23_hailing_1_2_2 367.5–372.1 s | 3.9 / 2.3 | 37 / 12 | head at limit 100%; outlier knee max (z +3.5); **trunk leans 29 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.2 s (at 3.1 s, 8 mm); **feet overlap 8 mm for 0.2 s (at 3.1 s)** *(excluded)* |
| `hailing_1_2_2_t370-374_shift` | B | 23_hailing_1_2_2 370.1–374.2 s | 15.3 / 7.6 | 31 / 10 | head at limit 100%; leg at limit 12%; **ground IK failed 12 frames**; outlier knee max (z +3.7); **trunk leans 30 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.7 s (at 2.2 s, 20 mm); **feet overlap 20 mm for 0.7 s (at 2.2 s)** *(excluded)* |
| `hailing_1_2_2_t376-387` | A | 23_hailing_1_2_2 375.7–387.3 s | 9.0 / 5.9 | 15 / 6 | head at limit 100%; outlier knee max (z +5.4); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t38-57` | A | 23_hailing_1_2_2 37.9–56.9 s | 8.5 / 4.8 | 15 / 8 | head at limit 100%; leg at limit 9%; **ground IK failed 11 frames**; outlier trunk drop (z +4.6); outlier knee max (z +7.2); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t387-399` | A | 23_hailing_1_2_2 387.3–398.9 s | 1.9 / 1.3 | 10 / 4 | head at limit 100%; elbow bend at limit 16%; leg at limit 22%; **trunk leans 23 deg (median)** *(excluded)* |
| `hailing_1_2_2_t400-408` | A | 23_hailing_1_2_2 399.6–408.3 s | 4.5 / 2.1 | 13 / 8 | head at limit 100%; leg at limit 22%; **ground IK failed 53 frames**; **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t409-420` | A | 23_hailing_1_2_2 409.0–419.7 s | 2.8 / 1.6 | 23 / 13 | head at limit 100%; **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t420-438` | A | 23_hailing_1_2_2 420.4–437.6 s | 7.9 / 2.9 | 22 / 11 | head at limit 100%; **ground IK failed 2 frames**; outlier trunk drop (z +4.4); outlier knee max (z +6.6); **trunk leans 24 deg (median)**; self-collision left_foot_collision / right_foot_collision 2.0 s (at 1.1 s, 19 mm); **feet overlap 19 mm for 2.0 s (at 1.1 s)** *(excluded)* |
| `hailing_1_2_2_t438-455` | A | 23_hailing_1_2_2 437.6–454.7 s | 6.5 / 2.3 | 16 / 7 | head at limit 100%; elbow bend at limit 7%; outlier knee max (z +6.5); **trunk leans 25 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.4 s (at 11.3 s, 9 mm); **feet overlap 9 mm for 0.4 s (at 11.3 s)** *(excluded)* |
| `hailing_1_2_2_t453-457_shift` | B | 23_hailing_1_2_2 452.7–457.4 s | 12.2 / 6.2 | 15 / 7 | head at limit 100%; outlier knee max (z +3.5); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t455-469` | A | 23_hailing_1_2_2 455.4–469.2 s | 4.5 / 1.9 | 18 / 10 | head at limit 100%; leg at limit 8%; **ground IK failed 10 frames**; outlier knee max (z +4.1); **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_2_2_t469-483` | A | 23_hailing_1_2_2 469.2–483.1 s | 4.1 / 2.0 | 22 / 12 | head at limit 100%; outlier knee max (z +3.6); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t483-497` | A | 23_hailing_1_2_2 483.1–496.9 s | 4.6 / 1.1 | 19 / 10 | head at limit 100%; **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_2_2_t495-502_shift` | B | 23_hailing_1_2_2 494.9–502.3 s | 24.0 / 12.6 | 16 / 7 | head at limit 100%; elbow bend at limit 5%; leg at limit 6%; outlier knee max (z +5.4); **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_2_2_t500-517` | A | 23_hailing_1_2_2 500.3–517.1 s | 6.4 / 2.7 | 20 / 9 | head at limit 100%; outlier knee max (z +5.5); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t520-526` | A | 23_hailing_1_2_2 520.2–526.5 s | 1.9 / 0.9 | 14 / 6 | head at limit 100%; **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t523-527_shift` | B | 23_hailing_1_2_2 523.2–527.2 s | 22.6 / 14.3 | 17 / 6 | head at limit 100%; outlier knee max (z +6.1); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t530-548` | A | 23_hailing_1_2_2 530.3–547.8 s | 8.7 / 4.0 | 22 / 11 | head at limit 100%; outlier knee max (z +5.4); **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_2_2_t553-557_shift` | B | 23_hailing_1_2_2 552.8–556.8 s | 4.8 / 1.5 | 21 / 10 | head at limit 100%; outlier knee max (z +7.3); **trunk leans 24 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.6 s (at 3.2 s, 13 mm); **feet overlap 13 mm for 0.6 s (at 3.2 s)** *(excluded)* |
| `hailing_1_2_2_t553-563` | A | 23_hailing_1_2_2 553.0–562.9 s | 9.8 / 4.3 | 20 / 11 | knee 63 deg; head at limit 100%; outlier knee max (z +9.2); **trunk leans 26 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.6 s (at 3.0 s, 13 mm); **feet overlap 13 mm for 0.6 s (at 3.0 s)** *(excluded)* |
| `hailing_1_2_2_t563-576` | A | 23_hailing_1_2_2 562.9–576.1 s | 1.5 / 1.3 | 21 / 10 | head at limit 100%; **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_2_2_t57-76` | A | 23_hailing_1_2_2 56.9–75.9 s | 5.7 / 2.7 | 19 / 8 | head at limit 100%; outlier knee max (z +7.0); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t580-597` | A | 23_hailing_1_2_2 580.2–597.1 s | 9.7 / 4.5 | 15 / 7 | head at limit 100%; outlier knee max (z +7.1); **trunk leans 26 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.6 s (at 13.2 s, 12 mm); **feet overlap 12 mm for 0.6 s (at 13.2 s)** *(excluded)* |
| `hailing_1_2_2_t597-614` | A | 23_hailing_1_2_2 597.1–614.0 s | 1.9 / 1.4 | 16 / 9 | head at limit 100%; **trunk leans 25 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.3 s (at 2.6 s, 7 mm); **feet overlap 7 mm for 0.3 s (at 2.6 s)** *(excluded)* |
| `hailing_1_2_2_t614-631` | A | 23_hailing_1_2_2 614.0–630.9 s | 8.0 / 2.8 | 22 / 11 | head at limit 100%; outlier knee max (z +7.4); **trunk leans 25 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.7 s (at 12.1 s, 13 mm); **feet overlap 13 mm for 0.7 s (at 12.1 s)** *(excluded)* |
| `hailing_1_2_2_t636-640_shift` | B | 23_hailing_1_2_2 635.6–639.6 s | 17.3 / 8.9 | 19 / 8 | head at limit 100%; **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_2_2_t636-653` | A | 23_hailing_1_2_2 636.3–653.1 s | 9.2 / 2.6 | 18 / 8 | head at limit 100%; outlier knee max (z +7.2); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_2_2_t654-659_shift` | B | 23_hailing_1_2_2 654.2–659.1 s | 13.0 / 9.7 | 38 / 12 | head at limit 100%; outlier knee max (z +6.4); **trunk leans 26 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.5 s (at 4.0 s, 8 mm); **feet overlap 8 mm for 0.5 s (at 4.0 s)** *(excluded)* |
| `hailing_1_2_2_t657-662` | A | 23_hailing_1_2_2 657.1–662.2 s | 1.9 / 1.0 | 43 / 14 | head at limit 100%; **trunk leans 27 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.8 s (at 2.4 s, 15 mm); **feet overlap 15 mm for 0.8 s (at 2.4 s)** *(excluded)* |
| `hailing_1_2_2_t76-90` | A | 23_hailing_1_2_2 75.9–89.7 s | 6.5 / 2.3 | 18 / 7 | head at limit 100%; outlier knee max (z +6.1); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_2_2_t90-103` | A | 23_hailing_1_2_2 89.7–103.4 s | 4.3 / 2.6 | 13 / 6 | head at limit 100%; outlier knee max (z +3.9); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_3_3_t106-111_shift` | B | 23_hailing_1_3_3 106.2–110.9 s | 11.4 / 7.9 | 28 / 16 | head at limit 100%; outlier knee max (z +5.5); **trunk leans 27 deg (median)** *(excluded)* |
| `hailing_1_3_3_t112-119` | A | 23_hailing_1_3_3 111.7–118.8 s | 7.7 / 2.0 | 19 / 11 | head at limit 100%; **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t119-133` | A | 23_hailing_1_3_3 119.4–133.4 s | 6.6 / 2.6 | 17 / 7 | head at limit 100%; **ground IK failed 9 frames**; outlier trunk drop (z +3.9); outlier knee max (z +4.2); **trunk leans 27 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.5 s (at 4.5 s, 8 mm); **feet overlap 8 mm for 0.5 s (at 4.5 s)** *(excluded)* |
| `hailing_1_3_3_t134-138_shift` | B | 23_hailing_1_3_3 134.1–138.4 s | 11.3 / 6.6 | 11 / 6 | head at limit 100%; outlier knee max (z +5.7); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_3_3_t136-155` | A | 23_hailing_1_3_3 136.4–155.0 s | 1.1 / 1.1 | 16 / 7 | head at limit 100%; **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_3_3_t15-33` | A | 23_hailing_1_3_3 14.7–33.1 s | 6.7 / 3.5 | 17 / 6 | head at limit 100%; elbow bend at limit 7%; **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t155-174` | A | 23_hailing_1_3_3 155.0–173.6 s | 2.3 / 1.5 | 16 / 7 | head at limit 100%; **trunk leans 24 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.6 s (at 13.1 s, 11 mm); **feet overlap 11 mm for 0.6 s (at 13.1 s)** *(excluded)* |
| `hailing_1_3_3_t179-184_shift` | B | 23_hailing_1_3_3 179.4–183.6 s | 19.5 / 10.8 | 20 / 8 | head at limit 100%; leg at limit 15%; outlier knee max (z +5.9); **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t182-188` | A | 23_hailing_1_3_3 181.6–188.1 s | 9.5 / 5.1 | 22 / 9 | head at limit 100%; outlier knee max (z +7.2); **trunk leans 25 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.6 s (at 4.0 s, 20 mm); **feet overlap 20 mm for 0.6 s (at 4.0 s)** *(excluded)* |
| `hailing_1_3_3_t188-193` | A | 23_hailing_1_3_3 188.1–192.8 s | 1.4 / 1.1 | 17 / 8 | head at limit 100%; **trunk leans 23 deg (median)** *(excluded)* |
| `hailing_1_3_3_t191-199_shift` | B | 23_hailing_1_3_3 190.8–199.2 s | 14.8 / 7.5 | 12 / 5 | knee 65 deg; head at limit 100%; leg at limit 10%; **ground IK failed 4 frames**; outlier trunk drop (z +4.8); outlier knee max (z +9.8); **trunk leans 24 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.3 s (at 5.5 s, 12 mm); **feet overlap 12 mm for 0.3 s (at 5.5 s)** *(excluded)* |
| `hailing_1_3_3_t197-209` | A | 23_hailing_1_3_3 197.2–209.2 s | 8.3 / 4.1 | 23 / 9 | head at limit 100%; outlier knee max (z +5.7); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_3_3_t2-8` | A | 23_hailing_1_3_3 2.0–8.4 s | 9.3 / 5.2 | 8 / 3 | head at limit 100%; **trunk leans 29 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.4 s (at 2.1 s, 13 mm); **feet overlap 13 mm for 0.4 s (at 2.1 s)** *(excluded)* |
| `hailing_1_3_3_t207-213_shift` | B | 23_hailing_1_3_3 207.2–213.2 s | 12.4 / 3.9 | 30 / 16 | knee 62 deg; head at limit 100%; outlier knee max (z +8.7); **trunk leans 23 deg (median)** *(excluded)* |
| `hailing_1_3_3_t211-219` | A | 23_hailing_1_3_3 211.2–219.1 s | 9.1 / 3.4 | 23 / 11 | head at limit 100%; outlier knee max (z +5.5); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_3_3_t217-222_shift` | B | 23_hailing_1_3_3 217.1–222.2 s | 8.1 / 2.9 | 22 / 12 | knee 61 deg; head at limit 100%; **ground IK failed 1 frames**; outlier trunk drop (z +4.3); outlier knee max (z +8.3); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_3_3_t224-228_shift` | B | 23_hailing_1_3_3 223.6–228.0 s | 14.7 / 7.4 | 14 / 6 | head at limit 100%; outlier knee max (z +7.3); **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_3_3_t226-240` | A | 23_hailing_1_3_3 226.0–240.2 s | 2.1 / 1.3 | 18 / 9 | head at limit 100%; **trunk leans 24 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.2 s (at 3.4 s, 7 mm); **feet overlap 7 mm for 0.2 s (at 3.4 s)** *(excluded)* |
| `hailing_1_3_3_t240-254` | A | 23_hailing_1_3_3 240.2–254.4 s | 1.9 / 1.4 | 21 / 9 | head at limit 100%; **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_3_3_t255-259` | A | 23_hailing_1_3_3 255.4–259.4 s | 7.6 / 2.9 | 26 / 19 | head at limit 100%; elbow bend at limit 26%; **ground IK failed 6 frames**; outlier trunk drop (z +3.9); outlier knee max (z +5.2); **trunk leans 25 deg (median)**; self-collision head_2_collision / left_hand_end_collision 0.4 s (at 3.1 s, 12 mm) *(excluded)* |
| `hailing_1_3_3_t264-270` | A | 23_hailing_1_3_3 264.1–269.5 s | 2.4 / 1.3 | 19 / 5 | head at limit 100%; **trunk leans 27 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.3 s (at 4.9 s, 7 mm); **feet overlap 7 mm for 0.3 s (at 4.9 s)** *(excluded)* |
| `hailing_1_3_3_t268-272_shift` | B | 23_hailing_1_3_3 267.5–272.0 s | 12.9 / 6.5 | 24 / 5 | head at limit 100%; outlier knee max (z +7.8); **trunk leans 28 deg (median)**; **self-collision left_foot_collision / right_foot_collision 0.6 s (at 2.2 s, 28 mm)**; **feet overlap 28 mm for 0.6 s (at 2.2 s)** *(excluded)* |
| `hailing_1_3_3_t270-274` | A | 23_hailing_1_3_3 270.0–274.0 s | 5.0 / 5.8 | 33 / 11 | head at limit 100%; leg at limit 43%; **trunk leans 28 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.3 s (at 0.0 s, 22 mm); **feet overlap 22 mm for 0.3 s (at 0.0 s)** *(excluded)* |
| `hailing_1_3_3_t272-280_shift` | B | 23_hailing_1_3_3 272.0–279.7 s | 19.8 / 9.8 | 26 / 10 | knee 63 deg; head at limit 100%; leg at limit 15%; outlier knee max (z +9.1); **trunk leans 27 deg (median)** *(excluded)* |
| `hailing_1_3_3_t278-294` | A | 23_hailing_1_3_3 277.7–293.5 s | 3.0 / 5.7 | 11 / 7 | head at limit 100%; elbow bend at limit 11%; **trunk leans 24 deg (median)** *(excluded)* |
| `hailing_1_3_3_t294-309` | A | 23_hailing_1_3_3 293.5–309.3 s | 5.5 / 1.8 | 21 / 10 | head at limit 100%; outlier knee max (z +6.9); **trunk leans 27 deg (median)** *(excluded)* |
| `hailing_1_3_3_t309-325` | A | 23_hailing_1_3_3 309.3–325.0 s | 5.2 / 2.7 | 24 / 8 | head at limit 100%; shoulder at limit 71%; outlier knee max (z +7.2); **trunk leans 31 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.2 s (at 7.5 s, 6 mm); **feet overlap 6 mm for 0.2 s (at 7.5 s)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `hailing_1_3_3_t325-341` | A | 23_hailing_1_3_3 325.0–340.8 s | 4.4 / 1.9 | 24 / 12 | head at limit 100%; outlier knee max (z +7.2); **trunk leans 26 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.6 s (at 0.8 s, 14 mm); **feet overlap 14 mm for 0.6 s (at 0.8 s)** *(excluded)* |
| `hailing_1_3_3_t33-51` | A | 23_hailing_1_3_3 33.1–51.5 s | 6.7 / 3.1 | 20 / 9 | head at limit 100%; outlier knee max (z +5.6); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_3_3_t345-354` | A | 23_hailing_1_3_3 345.1–354.5 s | 4.4 / 1.6 | 21 / 10 | head at limit 100%; outlier knee max (z +4.4); **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t352-357_shift` | B | 23_hailing_1_3_3 352.5–357.2 s | 15.0 / 8.6 | 19 / 5 | knee 62 deg; head at limit 100%; shoulder at limit 79%; outlier knee max (z +8.6); **trunk leans 37 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `hailing_1_3_3_t355-374` | A | 23_hailing_1_3_3 355.2–373.8 s | 7.8 / 4.2 | 15 / 7 | head at limit 100%; elbow bend at limit 14%; leg at limit 18%; outlier knee max (z +3.6); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_3_3_t372-376_shift` | B | 23_hailing_1_3_3 371.8–376.1 s | 9.8 / 7.3 | 32 / 17 | knee 64 deg; head at limit 100%; leg at limit 5%; outlier knee max (z +9.3); **trunk leans 27 deg (median)** *(excluded)* |
| `hailing_1_3_3_t374-384` | A | 23_hailing_1_3_3 374.1–383.7 s | 6.1 / 6.1 | 25 / 13 | knee 64 deg; head at limit 100%; outlier knee max (z +9.3); **trunk leans 26 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.4 s (at 3.4 s, 12 mm); **feet overlap 12 mm for 0.4 s (at 3.4 s)** *(excluded)* |
| `hailing_1_3_3_t384-390` | A | 23_hailing_1_3_3 384.4–389.9 s | 5.1 / 2.2 | 22 / 10 | head at limit 100%; elbow bend at limit 7%; leg at limit 45%; **ground IK failed 42 frames**; **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_3_3_t386-390_shift` | B | 23_hailing_1_3_3 386.4–390.4 s | 10.8 / 4.1 | 25 / 12 | head at limit 100%; elbow bend at limit 9%; leg at limit 58%; **ground IK failed 48 frames**; outlier knee max (z +4.3); **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_3_3_t391-406` | A | 23_hailing_1_3_3 391.1–406.1 s | 2.3 / 1.9 | 17 / 8 | head at limit 100%; **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_3_3_t406-421` | A | 23_hailing_1_3_3 406.1–421.1 s | 0.7 / 1.1 | 17 / 8 | head at limit 100%; **trunk leans 25 deg (median)** *(excluded)* |
| `hailing_1_3_3_t421-436` | A | 23_hailing_1_3_3 421.1–436.0 s | 9.9 / 4.0 | 22 / 11 | head at limit 100%; **ground IK failed 3 frames**; outlier trunk drop (z +4.4); outlier knee max (z +7.1); **trunk leans 26 deg (median)**; self-collision left_foot_collision / right_foot_collision 1.1 s (at 11.6 s, 13 mm); **feet overlap 13 mm for 1.1 s (at 11.6 s)** *(excluded)* |
| `hailing_1_3_3_t436-440` | A | 23_hailing_1_3_3 436.0–440.1 s | 9.8 / 2.4 | 28 / 14 | knee 65 deg; head at limit 100%; outlier knee max (z +9.8); **trunk leans 29 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.7 s (at 0.0 s, 18 mm); **feet overlap 18 mm for 0.7 s (at 0.0 s)** *(excluded)* |
| `hailing_1_3_3_t440-452` | A | 23_hailing_1_3_3 440.1–451.7 s | 9.9 / 9.8 | 39 / 17 | K1 feet move 10 cm; head at limit 100%; outlier knee max (z +5.7); **trunk leans 26 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.3 s (at 11.2 s, 11 mm); **feet overlap 11 mm for 0.3 s (at 11.2 s)** *(excluded)* |
| `hailing_1_3_3_t452-467` | A | 23_hailing_1_3_3 451.7–466.7 s | 9.0 / 6.0 | 39 / 15 | head at limit 100%; leg at limit 12%; outlier knee max (z +5.7); **trunk leans 29 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.8 s (at 14.2 s, 16 mm); **feet overlap 16 mm for 0.8 s (at 14.2 s)** *(excluded)* |
| `hailing_1_3_3_t465-469_shift` | B | 23_hailing_1_3_3 464.7–468.9 s | 8.4 / 2.8 | 34 / 12 | knee 62 deg; head at limit 100%; outlier knee max (z +8.6); **trunk leans 28 deg (median)**; self-collision left_foot_collision / right_foot_collision 1.9 s (at 1.2 s, 17 mm); **feet overlap 17 mm for 1.9 s (at 1.2 s)** *(excluded)* |
| `hailing_1_3_3_t467-475` | A | 23_hailing_1_3_3 466.9–474.7 s | 9.1 / 2.7 | 29 / 10 | knee 62 deg; head at limit 100%; outlier knee max (z +8.6); **trunk leans 27 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.8 s (at 0.0 s, 17 mm); **feet overlap 17 mm for 0.8 s (at 0.0 s)** *(excluded)* |
| `hailing_1_3_3_t473-477_shift` | B | 23_hailing_1_3_3 472.7–477.0 s | 6.0 / 2.9 | 37 / 11 | knee 64 deg; head at limit 100%; outlier knee max (z +9.5); **trunk leans 28 deg (median)**; **self-collision left_foot_collision / right_foot_collision 2.3 s (at 1.9 s, 32 mm)**; **feet overlap 32 mm for 2.3 s (at 1.9 s)** *(excluded)* |
| `hailing_1_3_3_t475-479` | A | 23_hailing_1_3_3 475.0–479.2 s | 10.0 / 2.9 | 24 / 8 | knee 65 deg; head at limit 100%; outlier knee max (z +9.6); **trunk leans 27 deg (median)**; **self-collision left_foot_collision / right_foot_collision 1.9 s (at 0.0 s, 32 mm)**; **feet overlap 32 mm for 1.9 s (at 0.0 s)** *(excluded)* |
| `hailing_1_3_3_t477-488_shift` | B | 23_hailing_1_3_3 477.2–487.7 s | 12.4 / 4.7 | 15 / 7 | knee 70 deg; head at limit 100%; outlier knee max (z +11.5); **trunk leans 26 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.4 s (at 0.6 s, 14 mm); **feet overlap 14 mm for 0.4 s (at 0.6 s)** *(excluded)* |
| `hailing_1_3_3_t486-502` | A | 23_hailing_1_3_3 485.7–501.9 s | 5.6 / 2.8 | 16 / 7 | head at limit 100%; leg at limit 10%; outlier knee max (z +4.6); **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t502-518` | A | 23_hailing_1_3_3 501.9–518.0 s | 5.0 / 2.1 | 23 / 12 | head at limit 100%; outlier knee max (z +5.6); **trunk leans 27 deg (median)** *(excluded)* |
| `hailing_1_3_3_t51-70` | A | 23_hailing_1_3_3 51.5–69.9 s | 9.1 / 3.8 | 20 / 9 | head at limit 100%; leg at limit 11%; outlier knee max (z +7.1); **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t519-523_shift` | B | 23_hailing_1_3_3 518.6–523.1 s | 10.9 / 3.6 | 29 / 14 | head at limit 100%; leg at limit 9%; **ground IK failed 9 frames**; outlier knee max (z +4.6); **trunk leans 27 deg (median)** *(excluded)* |
| `hailing_1_3_3_t524-528` | A | 23_hailing_1_3_3 523.7–527.8 s | 3.5 / 1.8 | 24 / 10 | head at limit 100%; elbow bend at limit 6%; **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t526-532_shift` | B | 23_hailing_1_3_3 525.8–531.6 s | 12.2 / 5.0 | 29 / 12 | head at limit 100%; elbow bend at limit 6%; outlier knee max (z +7.6); **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t530-537` | A | 23_hailing_1_3_3 529.6–537.3 s | 3.6 / 1.6 | 31 / 16 | head at limit 100%; **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t538-544_shift` | B | 23_hailing_1_3_3 538.0–543.7 s | 16.1 / 9.3 | 41 / 14 | head at limit 100%; outlier knee max (z +5.6); **trunk leans 27 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.1 s (at 4.6 s, 7 mm); **feet overlap 7 mm for 0.1 s (at 4.6 s)** *(excluded)* |
| `hailing_1_3_3_t542-549` | A | 23_hailing_1_3_3 541.7–549.5 s | 1.4 / 0.7 | 20 / 8 | head at limit 100%; **trunk leans 28 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.2 s (at 7.3 s, 7 mm); **feet overlap 7 mm for 0.2 s (at 7.3 s)** *(excluded)* |
| `hailing_1_3_3_t547-553_shift` | B | 23_hailing_1_3_3 547.5–552.5 s | 15.7 / 5.9 | 36 / 11 | head at limit 100%; leg at limit 20%; **trunk leans 27 deg (median)**; self-collision left_foot_collision / right_foot_collision 0.2 s (at 1.6 s, 7 mm); **feet overlap 7 mm for 0.2 s (at 1.6 s)** *(excluded)* |
| `hailing_1_3_3_t68-72_shift` | B | 23_hailing_1_3_3 67.9–72.0 s | 4.3 / 1.7 | 23 / 12 | knee 63 deg; head at limit 100%; elbow bend at limit 16%; outlier knee max (z +8.9); **trunk leans 27 deg (median)** *(excluded)* |
| `hailing_1_3_3_t70-84` | A | 23_hailing_1_3_3 70.0–84.3 s | 6.5 / 2.5 | 24 / 10 | knee 61 deg; head at limit 100%; outlier knee max (z +8.2); **trunk leans 26 deg (median)** *(excluded)* |
| `hailing_1_3_3_t9-15` | A | 23_hailing_1_3_3 9.4–14.7 s | 9.9 / 5.1 | 14 / 5 | knee 70 deg; head at limit 100%; elbow bend at limit 63%; outlier knee max (z +11.3); **trunk leans 26 deg (median)**; self-collision left_foot_collision / right_foot_collision 2.3 s (at 0.0 s, 17 mm); **feet overlap 17 mm for 2.3 s (at 0.0 s)** *(excluded)* |
| `hailing_1_3_3_t90-108` | A | 23_hailing_1_3_3 89.8–108.2 s | 4.3 / 4.9 | 14 / 6 | head at limit 100%; **trunk leans 24 deg (median)** *(excluded)* |
| `itoi_0_13_13_t72-90` | A | 17_itoi_0_13_13 71.8–89.8 s | 5.3 / 2.6 | 36 / 12 | **upper-arm twist at limit 75%**; leg at limit 13%; **ground IK failed 64 frames**; **joint jump 0.60 rad (Left_Knee_Pitch at 16.4 s)**; **root turn 6 deg/frame**; **self-collision left_hand_collision / trunk_collision 1.1 s (at 9.6 s, 25 mm)**; **foot held 43 mm off the floor (median)** *(excluded)* |
| `itoi_0_3_3_t58-64_shift` | B | 17_itoi_0_3_3 58.0–64.2 s | 16.9 / 11.3 | 38 / 10 | outlier knee max (z +7.6); **trunk leans 17 deg (median)** *(excluded)* |
| `itoi_0_5_5_t24-29` | A | 17_itoi_0_5_5 24.4–29.2 s | 10.0 / 3.0 | 35 / 11 | **ground IK failed 4 frames**; outlier knee max (z +3.8) *(excluded)* |
| `itoi_0_5_5_t27-35_shift` | B | 17_itoi_0_5_5 27.2–34.7 s | 14.4 / 9.0 | 42 / 12 | leg at limit 12%; **ground IK failed 19 frames**; outlier knee max (z +5.5) *(excluded)* |
| `itoi_0_7_7_t25-29` | A | 17_itoi_0_7_7 24.8–29.4 s | 7.2 / 1.0 | 36 / 11 | **trunk leans 17 deg (median)** *(excluded)* |
| `itoi_0_7_7_t43-48` | A | 17_itoi_0_7_7 43.4–48.2 s | 10.0 / 1.6 | 20 / 8 | **trunk leans 15 deg (median)** *(excluded)* |
| `itoi_0_7_7_t61-76_shift` | B | 17_itoi_0_7_7 61.0–75.8 s | 20.1 / 12.5 | 32 / 9 | knee 61 deg; leg at limit 6%; outlier knee max (z +8.4); **excluded in the spec (fails in training)** *(excluded)* |
| `itoi_1_1_1_t515-519_shift` | B | 17_itoi_1_1_1 514.8–518.8 s | 22.2 / 12.0 | 14 / 8 | shoulder at limit 15%; outlier knee max (z +5.5); **joint jump 1.13 rad (Left_Elbow_Yaw at 1.0 s)**; **root turn 35 deg/frame** *(excluded)* |
| `itoi_1_2_2_t180-186_shift` | B | 17_itoi_1_2_2 180.2–186.2 s | 23.6 / 13.1 | 41 / 12 | **ground IK failed 7 frames** *(excluded)* |
| `itoi_1_2_2_t21-27` | A | 17_itoi_1_2_2 21.4–27.1 s | 4.3 / 1.3 | 35 / 15 | **trunk leans 17 deg (median)** *(excluded)* |
| `itoi_1_2_2_t211-219` | A | 17_itoi_1_2_2 210.9–218.7 s | 8.8 / 5.1 | 61 / 18 | shoulder at limit 5%; **joint jump 0.97 rad (Right_Elbow_Pitch at 5.1 s)**; **root turn 12 deg/frame**; hand presses into leg 36 mm for 0.1 s (at 4.9 s) *(excluded)* |
| `itoi_1_2_2_t247-254_shift` | B | 17_itoi_1_2_2 247.5–254.2 s | 14.0 / 9.0 | 22 / 7 | **trunk leans 16 deg (median)** *(excluded)* |
| `itoi_1_2_2_t288-294` | A | 17_itoi_1_2_2 287.9–294.0 s | 6.7 / 3.9 | 27 / 12 | shoulder at limit 8%; **joint jump 0.77 rad (Right_Elbow_Pitch at 2.7 s)**; **root turn 10 deg/frame** *(excluded)* |
| `itoi_1_2_2_t609-628` | A | 17_itoi_1_2_2 608.9–627.7 s | 9.5 / 2.8 | 24 / 8 | shoulder at limit 11%; **trunk leans 15 deg (median)** *(excluded)* |
| `itoi_1_2_2_t70-78` | A | 17_itoi_1_2_2 69.9–77.9 s | 2.9 / 0.6 | 15 / 5 | **trunk leans 16 deg (median)** *(excluded)* |
| `itoi_1_2_2_t704-720` | A | 17_itoi_1_2_2 704.0–720.4 s | 7.0 / 1.3 | 58 / 16 | **joint jump 0.68 rad (Right_Elbow_Pitch at 13.7 s)** *(excluded)* |
| `itoi_1_2_2_t735-747_shift` | B | 17_itoi_1_2_2 734.8–747.4 s | 20.5 / 12.3 | 34 / 12 | outlier knee max (z +4.3); **joint jump 1.31 rad (Left_Shoulder_Pitch at 0.7 s)**; **root jump 7.9 cm/frame**; **root turn 37 deg/frame** *(excluded)* |
| `itoi_1_3_3_t220-227` | A | 17_itoi_1_3_3 219.6–227.0 s | 7.5 / 5.2 | 13 / 3 | head at limit 86%; shoulder at limit 97%; **trunk leans 29 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `jorge_1_1_1_t11-15_shift` | B | 16_jorge_1_1_1 11.1–15.5 s | 16.9 / 6.1 | 17 / 4 | leg at limit 6%; **ground IK failed 1 frames** *(excluded)* |
| `jorge_1_2_2_t460-466_shift` | B | 16_jorge_1_2_2 459.9–465.7 s | 18.8 / 9.6 | 23 / 13 | elbow bend at limit 29%; **self-collision head_2_collision / right_hand_end_collision 1.3 s (at 4.2 s, 41 mm)**; hand presses into leg 10 mm for 0.4 s (at 1.2 s) *(excluded)* |
| `jorge_1_2_2_t554-561` | A | 16_jorge_1_2_2 554.1–561.4 s | 2.5 / 4.8 | 2 / 1 | **foot held 39 mm off the floor (median)** *(excluded)* |
| `jorge_1_3_3_t597-602_shift` | B | 16_jorge_1_3_3 597.2–601.7 s | 24.4 / 16.0 | 9 / 2 | **foot held 34 mm off the floor (median)** *(excluded)* |
| `katya_0_103_103_t0-4` | A | 30_katya_0_103_103 0.0–4.1 s | 0.6 / 1.6 | 24 / 5 | knee 64 deg; leg at limit 31%; outlier knee max (z +9.3); self-collision left_shank_lower_collision / right_shank_lower_collision 1.0 s (at 1.1 s, 7 mm); **foot held 67 mm off the floor (median)** *(excluded)* |
| `katya_0_12_12_t28-46` | A | 30_katya_0_12_12 28.0–45.8 s | 2.8 / 1.1 | 13 / 5 | **self-collision left_hand_end_collision / right_hand_end_collision 1.2 s (at 16.5 s, 41 mm)** *(excluded)* |
| `katya_0_12_12_t46-64` | A | 30_katya_0_12_12 45.8–63.5 s | 9.3 / 4.1 | 12 / 6 | shoulder at limit 9%; **root turn 9 deg/frame**; **self-collision left_hand_end_collision / right_hand_end_collision 0.6 s (at 0.0 s, 28 mm)** *(excluded)* |
| `katya_0_14_14_t17-22_shift` | B | 30_katya_0_14_14 17.2–21.7 s | 8.3 / 4.1 | 10 / 4 | leg at limit 8%; **ground IK failed 8 frames** *(excluded)* |
| `katya_0_14_14_t20-36` | A | 30_katya_0_14_14 19.7–36.2 s | 8.6 / 3.1 | 9 / 4 | leg at limit 11%; **ground IK failed 54 frames** *(excluded)* |
| `katya_0_1_1_t51-66` | A | 30_katya_0_1_1 51.5–66.5 s | 10.0 / 2.5 | 22 / 7 | leg at limit 15%; **ground IK failed 53 frames**; **joint jump 0.61 rad (Left_Knee_Pitch at 3.4 s)**; self-collision right_hand_collision / trunk_collision 2.6 s (at 8.7 s, 18 mm) *(excluded)* |
| `katya_0_2_2_t16-31` | A | 30_katya_0_2_2 15.7–31.4 s | 3.7 / 19.1 | 21 / 7 | K1 feet move 19 cm; **ground IK failed 1 frames**; outlier knee max (z -5.9); **joint jump 0.83 rad (Left_Hip_Yaw at 15.0 s)**; **root jump 19.5 cm/frame**; **root turn 56 deg/frame** *(excluded)* |
| `katya_0_4_4_t0-5` | A | 30_katya_0_4_4 0.0–5.4 s | 9.6 / 2.4 | 30 / 7 | elbow bend at limit 14%; leg at limit 11%; **ground IK failed 4 frames**; outlier knee max (z +6.5); **foot held 32 mm off the floor (median)** *(excluded)* |
| `katya_0_65_65_t0-18` | A | 30_katya_0_65_65 0.0–17.7 s | 8.5 / 2.2 | 41 / 16 | shoulder at limit 20%; **upper-arm twist at limit 83%**; elbow bend at limit 11%; leg at limit 12%; **ground IK failed 41 frames**; outlier knee max (z +4.4); **root turn 7 deg/frame**; **self-collision right_hand_collision / trunk_collision 1.2 s (at 15.3 s, 83 mm)** *(excluded)* |
| `katya_0_66_66_t0-20` | A | 30_katya_0_66_66 0.0–19.9 s | 5.1 / 1.4 | 35 / 12 | shoulder at limit 6%; **self-collision left_hand_end_collision / right_hand_end_collision 0.6 s (at 7.3 s, 29 mm)** *(excluded)* |
| `katya_0_66_66_t20-40` | A | 30_katya_0_66_66 19.9–39.8 s | 5.4 / 1.8 | 34 / 13 | **excluded in the spec (fails in training)** *(excluded)* |
| `katya_0_66_66_t38-43_shift` | B | 30_katya_0_66_66 37.8–43.0 s | 10.7 / 5.3 | 54 / 20 | **upper-arm twist at limit 71%**; elbow bend at limit 16%; outlier knee max (z +4.4); self-collision right_hand_collision / trunk_collision 0.3 s (at 3.2 s, 20 mm) *(excluded)* |
| `katya_0_7_7_t0-19` | A | 30_katya_0_7_7 0.0–19.2 s | 3.6 / 1.8 | 30 / 10 | elbow bend at limit 12%; **joint jump 1.10 rad (Left_Shoulder_Pitch at 2.6 s)**; **root turn 18 deg/frame** *(excluded)* |
| `katya_0_87_87_t10-22` | A | 30_katya_0_87_87 10.1–21.7 s | 5.8 / 2.9 | 16 / 6 | **foot held 44 mm off the floor (median)** *(excluded)* |
| `katya_0_87_87_t22-33` | A | 30_katya_0_87_87 21.7–33.4 s | 6.5 / 2.7 | 16 / 6 | **foot held 36 mm off the floor (median)** *(excluded)* |
| `katya_0_88_88_t18-35` | A | 30_katya_0_88_88 17.6–35.2 s | 8.9 / 13.5 | 17 / 8 | K1 feet move 14 cm; shoulder at limit 12%; **ground IK failed 1 frames**; **joint jump 0.61 rad (Right_Elbow_Yaw at 3.6 s)**; **root jump 6.9 cm/frame**; **root turn 7 deg/frame** *(excluded)* |
| `katya_1_1_1_t101-119` | A | 30_katya_1_1_1 101.1–119.2 s | 8.1 / 5.6 | 13 / 5 | elbow bend at limit 5%; **joint jump 1.09 rad (Right_Shoulder_Roll at 4.9 s)**; **root jump 8.1 cm/frame**; **root turn 24 deg/frame**; **right foot slides 6.5 cm in one frame (at 4.9 s)** *(excluded)* |
| `katya_1_1_1_t189-205` | A | 30_katya_1_1_1 189.3–205.3 s | 9.8 / 5.9 | 10 / 3 | leg at limit 6%; **ground IK failed 27 frames** *(excluded)* |
| `katya_1_1_1_t203-211_shift` | B | 30_katya_1_1_1 203.3–210.6 s | 28.1 / 14.3 | 25 / 7 | human steps; leg at limit 36%; **ground IK failed 62 frames**; outlier knee max (z +7.3) *(excluded)* |
| `katya_1_1_1_t257-270` | A | 30_katya_1_1_1 257.1–270.3 s | 5.1 / 2.7 | 20 / 6 | head at limit 49%; shoulder at limit 100%; leg at limit 6%; **ground IK failed 19 frames**; **trunk leans 20 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `katya_1_1_1_t290-295_shift` | B | 30_katya_1_1_1 289.7–295.4 s | 18.6 / 11.6 | 17 / 5 | **ground IK failed 6 frames**; outlier knee max (z +4.9) *(excluded)* |
| `katya_1_1_1_t306-314_shift` | B | 30_katya_1_1_1 306.5–314.5 s | 18.2 / 9.3 | 17 / 5 | outlier knee max (z +8.0); self-collision left_foot_collision / right_foot_collision 2.3 s (at 2.1 s, 20 mm); **feet overlap 20 mm for 2.3 s (at 2.1 s)** *(excluded)* |
| `katya_1_1_1_t357-363` | A | 30_katya_1_1_1 356.6–363.0 s | 4.0 / 1.6 | 16 / 5 | knee 67 deg; outlier knee max (z +10.4); **foot held 66 mm off the floor (median)** *(excluded)* |
| `katya_1_1_1_t378-382_shift` | B | 30_katya_1_1_1 377.8–382.2 s | 10.6 / 3.4 | 16 / 6 | knee 66 deg; outlier knee max (z +9.9); **foot held 48 mm off the floor (median)** *(excluded)* |
| `katya_1_1_1_t380-385` | A | 30_katya_1_1_1 380.2–384.6 s | 8.6 / 2.0 | 15 / 7 | knee 69 deg; outlier knee max (z +11.1); **foot held 77 mm off the floor (median)** *(excluded)* |
| `katya_1_1_1_t383-387_shift` | B | 30_katya_1_1_1 382.6–387.0 s | 8.3 / 4.9 | 17 / 9 | knee 70 deg; outlier trunk drop (z +4.2); outlier knee max (z +11.3); **foot held 44 mm off the floor (median)** *(excluded)* |
| `katya_1_1_1_t385-400` | A | 30_katya_1_1_1 385.0–399.9 s | 5.9 / 4.1 | 16 / 7 | elbow bend at limit 7%; leg at limit 6%; **ground IK failed 26 frames** *(excluded)* |
| `katya_1_1_1_t454-458` | A | 30_katya_1_1_1 453.9–457.9 s | 9.7 / 8.1 | 10 / 3 | K1 feet move 8 cm; **self-collision left_foot_collision / right_foot_collision 4.0 s (at 0.0 s, 38 mm)**; **feet overlap 38 mm for 4.0 s (at 0.0 s)** *(excluded)* |
| `katya_1_1_1_t454-458_shift` | B | 30_katya_1_1_1 454.4–458.4 s | 10.3 / 7.8 | 9 / 3 | **self-collision left_foot_collision / right_foot_collision 4.0 s (at 0.0 s, 39 mm)**; **feet overlap 39 mm for 4.0 s (at 0.0 s)** *(excluded)* |
| `katya_1_1_1_t500-510_shift` | B | 30_katya_1_1_1 500.3–510.0 s | 22.7 / 9.1 | 6 / 3 | knee 60 deg; leg at limit 17%; **ground IK failed 5 frames**; outlier trunk drop (z +3.9); outlier knee max (z +8.2); self-collision right_hand_collision / trunk_collision 0.8 s (at 7.3 s, 11 mm); **foot held 34 mm off the floor (median)** *(excluded)* |
| `katya_1_1_1_t599-610_shift` | B | 30_katya_1_1_1 599.2–610.1 s | 13.8 / 4.7 | 27 / 8 | knee 61 deg; leg at limit 19%; **ground IK failed 6 frames**; outlier trunk drop (z +3.5); outlier knee max (z +8.3) *(excluded)* |
| `katya_1_2_2_t176-185_shift` | B | 30_katya_1_2_2 176.1–184.9 s | 20.0 / 8.0 | 11 / 4 | knee 62 deg; leg at limit 22%; **ground IK failed 52 frames**; outlier trunk drop (z +4.2); outlier knee max (z +8.8); **joint jump 1.21 rad (Right_Ankle_Pitch at 5.2 s)**; **Right_Ankle_Pitch over its speed limit for 0.20 s (at 5.3 s)**; **foot held 45 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t197-205_shift` | B | 30_katya_1_2_2 197.4–205.3 s | 17.8 / 9.7 | 19 / 6 | elbow bend at limit 6%; outlier knee max (z +7.4); self-collision left_foot_collision / right_foot_collision 0.1 s (at 0.0 s, 7 mm); **feet overlap 7 mm for 0.1 s (at 0.0 s)** *(excluded)* |
| `katya_1_2_2_t222-232` | A | 30_katya_1_2_2 222.2–231.5 s | 3.3 / 0.8 | 16 / 5 | outlier knee max (z +7.4); **foot held 48 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t235-245_shift` | B | 30_katya_1_2_2 235.2–245.3 s | 16.9 / 7.7 | 15 / 6 | knee 61 deg; shoulder at limit 20%; leg at limit 24%; outlier knee max (z +8.3); **self-collision right_hand_end_collision / trunk_collision 2.2 s (at 7.5 s, 33 mm)** *(excluded)* |
| `katya_1_2_2_t243-258` | A | 30_katya_1_2_2 243.3–257.7 s | 5.5 / 6.2 | 33 / 10 | shoulder at limit 11%; **self-collision right_hand_end_collision / trunk_collision 1.6 s (at 0.0 s, 27 mm)** *(excluded)* |
| `katya_1_2_2_t256-266_shift` | B | 30_katya_1_2_2 255.7–266.2 s | 16.3 / 7.4 | 27 / 10 | knee 63 deg; leg at limit 9%; **ground IK failed 4 frames**; outlier knee max (z +9.2); **joint jump 1.13 rad (Right_Ankle_Pitch at 4.3 s)**; **foot held 44 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t284-290` | A | 30_katya_1_2_2 284.1–290.3 s | 4.6 / 1.1 | 35 / 12 | shoulder at limit 7%; outlier knee max (z +8.0); **foot held 41 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t411-415_shift` | B | 30_katya_1_2_2 410.8–414.8 s | 13.6 / 3.8 | 32 / 10 | leg at limit 27%; **ground IK failed 15 frames**; outlier knee max (z +3.7) *(excluded)* |
| `katya_1_2_2_t422-426_shift` | B | 30_katya_1_2_2 421.7–426.0 s | 10.3 / 2.6 | 4 / 2 | knee 60 deg; outlier knee max (z +8.1); **foot held 32 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t424-431` | A | 30_katya_1_2_2 424.0–431.4 s | 8.0 / 2.2 | 7 / 3 | outlier knee max (z +6.9); **foot held 52 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t429-434_shift` | B | 30_katya_1_2_2 429.4–434.3 s | 12.7 / 3.9 | 14 / 7 | knee 60 deg; leg at limit 27%; outlier knee max (z +8.1); **excluded in the spec (fails in training)** *(excluded)* |
| `katya_1_2_2_t432-449` | A | 30_katya_1_2_2 432.3–449.3 s | 9.9 / 5.2 | 8 / 4 | self-collision left_foot_collision / right_foot_collision 0.2 s (at 13.8 s, 9 mm); **feet overlap 9 mm for 0.2 s (at 13.8 s)** *(excluded)* |
| `katya_1_2_2_t447-457_shift` | B | 30_katya_1_2_2 447.3–456.6 s | 18.2 / 6.5 | 12 / 6 | knee 61 deg; leg at limit 20%; **ground IK failed 18 frames**; outlier knee max (z +8.5); **joint jump 0.61 rad (Left_Knee_Pitch at 6.1 s)** *(excluded)* |
| `katya_1_2_2_t462-469` | A | 30_katya_1_2_2 462.0–469.5 s | 2.2 / 2.0 | 4 / 2 | **self-collision left_foot_collision / right_foot_collision 7.5 s (at 0.0 s, 34 mm)**; **feet overlap 34 mm for 7.5 s (at 0.0 s)** *(excluded)* |
| `katya_1_2_2_t498-502_shift` | B | 30_katya_1_2_2 497.7–502.2 s | 10.4 / 2.4 | 14 / 6 | outlier knee max (z +6.5); **foot held 38 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t518-525` | A | 30_katya_1_2_2 518.2–525.2 s | 4.5 / 2.0 | 29 / 9 | **self-collision left_foot_collision / right_foot_collision 7.0 s (at 0.0 s, 36 mm)**; **feet overlap 36 mm for 7.0 s (at 0.0 s)** *(excluded)* |
| `katya_1_2_2_t60-64_shift` | B | 30_katya_1_2_2 59.5–64.1 s | 11.4 / 2.7 | 9 / 3 | knee 62 deg; outlier knee max (z +8.7); self-collision left_foot_collision / right_foot_collision 1.8 s (at 2.7 s, 12 mm); **feet overlap 12 mm for 1.8 s (at 2.7 s)**; **foot held 37 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t62-74` | A | 30_katya_1_2_2 62.1–73.8 s | 3.0 / 0.7 | 13 / 4 | outlier knee max (z +7.6); self-collision left_foot_collision / right_foot_collision 4.1 s (at 3.3 s, 18 mm); **feet overlap 18 mm for 4.1 s (at 3.3 s)**; **foot held 47 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t72-76_shift` | B | 30_katya_1_2_2 71.5–75.5 s | 19.1 / 3.9 | 12 / 4 | knee 62 deg; outlier knee max (z +8.7); self-collision left_foot_collision / right_foot_collision 2.4 s (at 0.2 s, 19 mm); **feet overlap 19 mm for 2.4 s (at 0.2 s)**; **foot held 42 mm off the floor (median)** *(excluded)* |
| `katya_1_2_2_t89-95` | A | 30_katya_1_2_2 88.6–95.2 s | 1.9 / 0.8 | 14 / 5 | outlier knee max (z +7.1); **foot held 57 mm off the floor (median)**; **excluded in the spec (fails in training)** *(excluded)* |
| `katya_1_3_3_t122-133` | A | 30_katya_1_3_3 122.3–133.0 s | 2.5 / 1.4 | 29 / 8 | **self-collision left_foot_collision / right_foot_collision 10.8 s (at 0.0 s, 36 mm)**; **feet overlap 36 mm for 10.8 s (at 0.0 s)** *(excluded)* |
| `katya_1_3_3_t244-256_shift` | B | 30_katya_1_3_3 244.4–256.4 s | 19.9 / 8.1 | 25 / 7 | shoulder at limit 20%; elbow bend at limit 11%; leg at limit 20%; outlier knee max (z +3.7); **self-collision right_hand_end_collision / trunk_collision 2.5 s (at 4.8 s, 36 mm)** *(excluded)* |
| `katya_1_3_3_t275-281_shift` | B | 30_katya_1_3_3 275.4–281.3 s | 17.9 / 12.1 | 54 / 17 | leg at limit 12%; **ground IK failed 16 frames**; **self-collision left_foot_collision / right_foot_collision 4.0 s (at 0.0 s, 27 mm)**; **feet overlap 27 mm for 4.0 s (at 0.0 s)** *(excluded)* |
| `katya_1_3_3_t3-14` | A | 30_katya_1_3_3 3.0–14.5 s | 3.6 / 2.2 | 28 / 10 | knee 70 deg; **ground IK failed 5 frames**; outlier knee max (z +11.3); **joint jump 1.21 rad (Right_Ankle_Pitch at 1.4 s)**; **self-collision left_shank_lower_collision / right_shank_lower_collision 11.5 s (at 0.0 s, 51 mm)**; **feet overlap 47 mm for 3.5 s (at 8.0 s)**; **foot held 77 mm off the floor (median)** *(excluded)* |
| `katya_1_3_3_t308-312_shift` | B | 30_katya_1_3_3 307.6–312.0 s | 10.5 / 4.4 | 3 / 2 | leg at limit 11%; **ground IK failed 11 frames** *(excluded)* |
| `katya_1_3_3_t310-326` | A | 30_katya_1_3_3 310.0–326.4 s | 8.6 / 2.5 | 18 / 6 | leg at limit 6%; **ground IK failed 25 frames**; outlier trunk drop (z +4.5); outlier knee max (z +4.4) *(excluded)* |
| `katya_1_3_3_t326-343` | A | 30_katya_1_3_3 326.4–342.9 s | 6.2 / 3.4 | 14 / 6 | elbow bend at limit 7%; leg at limit 49%; **ground IK failed 223 frames**; **Right_Knee_Pitch over its speed limit for 0.13 s (at 3.7 s)** *(excluded)* |
| `katya_1_3_3_t392-399_shift` | B | 30_katya_1_3_3 392.0–399.4 s | 18.0 / 13.4 | 21 / 9 | elbow bend at limit 27%; leg at limit 9%; **ground IK failed 17 frames**; self-collision left_hand_collision / trunk_collision 0.6 s (at 0.0 s, 8 mm) *(excluded)* |
| `katya_1_3_3_t450-454_shift` | B | 30_katya_1_3_3 449.8–454.1 s | 11.8 / 6.4 | 36 / 8 | leg at limit 22%; **ground IK failed 25 frames** *(excluded)* |
| `katya_1_3_3_t466-476` | A | 30_katya_1_3_3 465.9–476.3 s | 6.9 / 3.8 | 18 / 6 | leg at limit 13%; **ground IK failed 39 frames** *(excluded)* |
| `katya_1_3_3_t543-548_shift` | B | 30_katya_1_3_3 542.8–547.7 s | 12.7 / 4.2 | 8 / 3 | knee 67 deg; elbow bend at limit 12%; leg at limit 5%; **ground IK failed 4 frames**; outlier trunk drop (z +4.6); outlier knee max (z +10.5) *(excluded)* |
| `katya_1_3_3_t546-559` | A | 30_katya_1_3_3 545.7–559.5 s | 6.6 / 4.8 | 11 / 5 | knee 69 deg; leg at limit 41%; **ground IK failed 32 frames**; outlier knee max (z +10.9); **foot held 78 mm off the floor (median)** *(excluded)* |
| `katya_1_3_3_t557-562_shift` | B | 30_katya_1_3_3 557.5–562.1 s | 16.8 / 9.1 | 21 / 8 | knee 70 deg; leg at limit 38%; **ground IK failed 35 frames**; outlier trunk drop (z +4.2); outlier knee max (z +11.5); **Right_Knee_Pitch over its speed limit for 0.17 s (at 0.2 s)**; **foot held 32 mm off the floor (median)** *(excluded)* |
| `katya_1_3_3_t600-610` | A | 30_katya_1_3_3 600.3–610.4 s | 1.7 / 1.2 | 7 / 3 | knee 66 deg; leg at limit 91%; **ground IK failed 248 frames**; outlier knee max (z +10.0); **joint jump 1.21 rad (Left_Ankle_Pitch at 0.8 s)**; **Left_Ankle_Pitch over its speed limit for 0.27 s (at 2.6 s)**; **foot held 84 mm off the floor (median)** *(excluded)* |
| `kieks_0_95_95_t18-36` | A | 10_kieks_0_95_95 17.9–35.8 s | 7.8 / 12.7 | 36 / 11 | K1 feet move 13 cm; shoulder at limit 18%; **joint jump 1.08 rad (Right_Hip_Yaw at 12.7 s)**; **root jump 11.6 cm/frame**; **root turn 28 deg/frame**; **self-collision left_hand_collision / right_hand_collision 1.8 s (at 13.8 s, 28 mm)** *(excluded)* |
| `kieks_1_1_1_t19-24_shift` | B | 10_kieks_1_1_1 19.0–24.0 s | 23.2 / 7.3 | 14 / 5 | knee 65 deg; leg at limit 42%; **ground IK failed 2 frames**; outlier trunk drop (z +4.8); outlier knee max (z +9.7) *(excluded)* |
| `kieks_1_1_1_t25-32` | A | 10_kieks_1_1_1 25.3–31.6 s | 4.6 / 2.8 | 18 / 6 | **foot held 30 mm off the floor (median)** *(excluded)* |
| `kieks_1_1_1_t350-361` | A | 10_kieks_1_1_1 350.1–360.8 s | 5.0 / 2.3 | 20 / 6 | **foot held 40 mm off the floor (median)** *(excluded)* |
| `kieks_1_1_1_t387-398` | A | 10_kieks_1_1_1 386.5–397.6 s | 6.2 / 2.7 | 3 / 2 | **foot held 32 mm off the floor (median)** *(excluded)* |
| `kieks_1_1_1_t405-411` | A | 10_kieks_1_1_1 405.1–410.6 s | 4.3 / 3.0 | 24 / 9 | **foot held 40 mm off the floor (median)** *(excluded)* |
| `kieks_1_2_2_t182-186_shift` | B | 10_kieks_1_2_2 181.6–185.6 s | 12.0 / 3.6 | 7 / 2 | outlier knee max (z +3.6); **foot held 32 mm off the floor (median)** *(excluded)* |
| `kieks_1_2_2_t215-220` | A | 10_kieks_1_2_2 215.0–220.3 s | 4.8 / 1.4 | 3 / 1 | **foot held 45 mm off the floor (median)** *(excluded)* |
| `kieks_1_2_2_t476-487` | A | 10_kieks_1_2_2 475.5–487.4 s | 5.6 / 6.4 | 21 / 8 | **foot held 39 mm off the floor (median)** *(excluded)* |
| `kieks_1_2_2_t493-497_shift` | B | 10_kieks_1_2_2 493.1–497.1 s | 15.9 / 14.5 | 13 / 10 | trunk drop 10 cm; knee 128 deg; head at limit 100%; shoulder at limit 72%; leg at limit 100%; **ground IK failed 120 frames**; **outlier trunk drop (z +12.0)**; outlier knee max (z +30.6); **root turn 15 deg/frame**; **trunk leans 77 deg (median)**; **self-collision right_shank_lower_collision / trunk_collision 3.1 s (at 0.0 s, 103 mm)**; **foot held 368 mm off the floor (median)** *(excluded)* |
| `kieks_1_3_3_t230-245` | A | 10_kieks_1_3_3 229.8–245.4 s | 7.0 / 7.1 | 28 / 8 | **ground IK failed 5 frames** *(excluded)* |
| `kieks_1_3_3_t274-284` | A | 10_kieks_1_3_3 273.7–283.9 s | 2.7 / 1.9 | 18 / 7 | leg at limit 6%; **ground IK failed 10 frames**; self-collision right_hand_collision / trunk_collision 2.3 s (at 7.0 s, 23 mm); **foot held 31 mm off the floor (median)** *(excluded)* |
| `kieks_1_3_3_t324-328_shift` | B | 10_kieks_1_3_3 324.1–328.2 s | 24.7 / 14.7 | 10 / 3 | knee 67 deg; leg at limit 14%; **ground IK failed 11 frames**; outlier trunk drop (z +3.9); outlier knee max (z +10.4) *(excluded)* |
| `kieks_1_3_3_t445-461` | A | 10_kieks_1_3_3 444.6–460.9 s | 9.2 / 6.6 | 10 / 4 | **foot held 40 mm off the floor (median)** *(excluded)* |
| `kieks_1_3_3_t523-527_shift` | B | 10_kieks_1_3_3 523.4–527.4 s | 9.7 / 14.4 | 6 / 1 | knee 102 deg; head at limit 100%; shoulder at limit 100%; leg at limit 100%; **ground IK failed 120 frames**; outlier trunk drop (z +3.9); outlier knee max (z +22.0); **trunk leans 80 deg (median)**; **self-collision right_shank_lower_collision / trunk_collision 4.0 s (at 0.0 s, 67 mm)**; **foot held 377 mm off the floor (median)**; **right arm behind body 17 cm (human's in front)** *(excluded)* |
| `kieks_1_3_3_t603-608` | A | 10_kieks_1_3_3 602.6–607.6 s | 3.1 / 2.6 | 5 / 2 | leg at limit 60%; **ground IK failed 42 frames** *(excluded)* |
| `kieks_1_3_3_t74-84` | A | 10_kieks_1_3_3 73.7–84.4 s | 4.0 / 1.0 | 8 / 2 | **foot held 41 mm off the floor (median)** *(excluded)* |
| `lawrence_0_100_100_t39-44` | A | 4_lawrence_0_100_100 38.9–44.4 s | 7.8 / 3.5 | 57 / 19 | **ground IK failed 2 frames** *(excluded)* |
| `lawrence_0_101_101_t42-55` | A | 4_lawrence_0_101_101 42.4–54.9 s | 9.2 / 6.1 | 48 / 17 | upper-arm twist at limit 5%; **excluded in the spec (fails in training)** *(excluded)* |
| `lawrence_0_102_102_t36-40_shift` | B | 4_lawrence_0_102_102 35.9–39.9 s | 27.4 / 15.4 | 17 / 5 | human steps; shoulder at limit 100%; outlier knee max (z +3.7); **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `lawrence_0_103_103_t25-34` | A | 4_lawrence_0_103_103 24.8–33.6 s | 5.1 / 3.3 | 25 / 7 | shoulder at limit 78%; outlier knee max (z +5.9); **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `lawrence_0_103_103_t34-41` | A | 4_lawrence_0_103_103 33.9–41.0 s | 7.6 / 4.2 | 29 / 6 | head at limit 7%; shoulder at limit 98%; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `lawrence_0_104_104_t34-42_shift` | B | 4_lawrence_0_104_104 33.7–42.2 s | 22.7 / 13.4 | 27 / 11 | head at limit 9%; shoulder at limit 64%; upper-arm twist at limit 20%; outlier knee max (z +3.9); **joint jump 1.54 rad (Left_Shoulder_Roll at 5.8 s)**; **root turn 27 deg/frame**; left arm behind body 7 cm (human's in front) *(excluded)* |
| `lawrence_0_104_104_t48-52` | A | 4_lawrence_0_104_104 47.7–52.5 s | 4.5 / 2.9 | 23 / 9 | shoulder at limit 29%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `lawrence_0_105_105_t44-55_shift` | B | 4_lawrence_0_105_105 44.2–54.5 s | 28.8 / 16.2 | 43 / 13 | human steps; outlier knee max (z +4.7); **joint jump 0.84 rad (Right_Elbow_Yaw at 2.7 s)**; **root turn 8 deg/frame** *(excluded)* |
| `lawrence_0_106_106_t21-32_shift` | B | 4_lawrence_0_106_106 21.4–31.8 s | 23.5 / 15.1 | 46 / 18 | trunk drop 6 cm; knee 74 deg; **outlier trunk drop (z +7.1)**; outlier knee max (z +12.6) *(excluded)* |
| `lawrence_0_110_110_t38-52_shift` | B | 4_lawrence_0_110_110 38.3–51.8 s | 28.2 / 16.2 | 39 / 15 | human steps; upper-arm twist at limit 10%; outlier knee max (z +6.2); **root turn 9 deg/frame** *(excluded)* |
| `lawrence_0_113_113_t28-34_shift` | B | 4_lawrence_0_113_113 28.1–34.1 s | 19.3 / 12.1 | 47 / 14 | shoulder at limit 15%; **joint jump 1.57 rad (Left_Shoulder_Pitch at 1.1 s)**; **root turn 32 deg/frame** *(excluded)* |
| `lawrence_0_115_115_t26-34` | A | 4_lawrence_0_115_115 25.5–34.4 s | 8.2 / 5.0 | 30 / 7 | head at limit 34%; shoulder at limit 100%; **trunk leans 19 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `lawrence_0_13_13_t72-78` | A | 4_lawrence_0_13_13 72.4–77.9 s | 0.6 / 2.0 | 41 / 16 | shoulder at limit 63%; **joint jump 1.10 rad (Right_Elbow_Pitch at 3.6 s)**; **root turn 20 deg/frame**; **foot held 44 mm off the floor (median)** *(excluded)* |
| `lawrence_0_16_16_t64-68_shift` | B | 4_lawrence_0_16_16 63.7–68.2 s | 10.6 / 7.2 | 25 / 18 | shoulder at limit 37%; **joint jump 2.14 rad (Left_Shoulder_Roll at 0.5 s)**; **root turn 26 deg/frame** *(excluded)* |
| `lawrence_0_17_17_t33-37` | A | 4_lawrence_0_17_17 32.9–37.2 s | 2.2 / 0.8 | 21 / 8 | **root turn 7 deg/frame** *(excluded)* |
| `lawrence_0_17_17_t35-40_shift` | B | 4_lawrence_0_17_17 35.2–39.8 s | 9.2 / 5.5 | 21 / 8 | **root turn 7 deg/frame** *(excluded)* |
| `lawrence_0_25_25_t80-89` | A | 4_lawrence_0_25_25 80.4–89.4 s | 1.3 / 1.1 | 40 / 14 | **root turn 7 deg/frame** *(excluded)* |
| `lawrence_0_26_26_t31-38_shift` | B | 4_lawrence_0_26_26 31.2–38.5 s | 21.3 / 13.7 | 32 / 13 | upper-arm twist at limit 6%; outlier knee max (z +7.6); **joint jump 0.69 rad (Right_Shoulder_Pitch at 4.5 s)**; **root turn 17 deg/frame** *(excluded)* |
| `lawrence_0_27_27_t26-34` | A | 4_lawrence_0_27_27 26.5–34.0 s | 3.3 / 1.8 | 43 / 14 | **joint jump 0.77 rad (Right_Shoulder_Pitch at 7.2 s)** *(excluded)* |
| `lawrence_0_33_33_t32-36_shift` | B | 4_lawrence_0_33_33 31.8–36.3 s | 12.9 / 7.5 | 20 / 9 | shoulder at limit 10%; outlier knee max (z +4.5); **joint jump 0.98 rad (Right_Elbow_Pitch at 2.1 s)**; **root turn 10 deg/frame** *(excluded)* |
| `lawrence_0_39_39_t0-6_shift` | B | 4_lawrence_0_39_39 0.0–6.1 s | 19.3 / 10.2 | 35 / 11 | **ground IK failed 1 frames**; outlier knee max (z +5.2) *(excluded)* |
| `lawrence_0_52_52_t44-58` | A | 4_lawrence_0_52_52 44.1–57.8 s | 9.5 / 4.4 | 51 / 17 | **upper-arm twist at limit 73%** *(excluded)* |
| `lawrence_0_53_53_t14-30` | A | 4_lawrence_0_53_53 13.9–30.2 s | 10.0 / 5.1 | 34 / 14 | **joint jump 0.65 rad (Right_Elbow_Pitch at 2.6 s)** *(excluded)* |
| `lawrence_0_56_56_t16-31` | A | 4_lawrence_0_56_56 16.1–31.4 s | 6.1 / 3.4 | 35 / 12 | **ground IK failed 14 frames** *(excluded)* |
| `lawrence_0_57_57_t49-57` | A | 4_lawrence_0_57_57 48.8–56.8 s | 9.8 / 3.2 | 18 / 5 | **trunk leans 15 deg (median)** *(excluded)* |
| `lawrence_0_58_58_t10-17` | A | 4_lawrence_0_58_58 10.4–17.3 s | 9.4 / 5.0 | 54 / 15 | **joint jump 0.63 rad (Right_Elbow_Pitch at 0.6 s)** *(excluded)* |
| `lawrence_0_58_58_t8-12_shift` | B | 4_lawrence_0_58_58 8.1–12.4 s | 9.6 / 4.9 | 79 / 20 | shoulder at limit 7%; outlier arms k1 cm (z +3.6); **joint jump 0.63 rad (Right_Elbow_Pitch at 2.9 s)** *(excluded)* |
| `lawrence_0_59_59_t39-44` | A | 4_lawrence_0_59_59 38.9–44.0 s | 1.8 / 0.7 | 19 / 12 | shoulder at limit 55%; **joint jump 0.77 rad (Right_Elbow_Pitch at 3.2 s)**; **root turn 8 deg/frame** *(excluded)* |
| `lawrence_0_62_62_t6-24` | A | 4_lawrence_0_62_62 5.8–24.1 s | 5.7 / 3.5 | 30 / 9 | head at limit 23%; shoulder at limit 49%; **joint jump 1.62 rad (Left_Shoulder_Pitch at 9.7 s)**; **root turn 25 deg/frame**; left arm behind body 8 cm (human's in front) *(excluded)* |
| `lawrence_0_63_63_t37-54` | A | 4_lawrence_0_63_63 37.4–53.9 s | 8.4 / 5.3 | 36 / 11 | **joint jump 0.87 rad (Right_Elbow_Pitch at 0.7 s)**; **root turn 6 deg/frame** *(excluded)* |
| `lawrence_0_66_66_t5-10_shift` | B | 4_lawrence_0_66_66 4.9–9.7 s | 14.4 / 8.3 | 50 / 15 | **joint jump 1.59 rad (Left_Shoulder_Pitch at 1.2 s)**; **root jump 3.2 cm/frame**; **root turn 21 deg/frame** *(excluded)* |
| `lawrence_0_67_67_t15-30_shift` | B | 4_lawrence_0_67_67 14.9–30.0 s | 24.3 / 13.5 | 47 / 16 | **upper-arm twist at limit 77%**; **root turn 8 deg/frame** *(excluded)* |
| `lawrence_0_68_68_t23-33_shift` | B | 4_lawrence_0_68_68 23.2–32.7 s | 15.1 / 8.0 | 57 / 20 | upper-arm twist at limit 13%; outlier arms k1 cm (z +3.6); outlier knee max (z +4.0); **root turn 11 deg/frame** *(excluded)* |
| `lawrence_0_69_69_t20-31` | A | 4_lawrence_0_69_69 19.9–31.0 s | 5.3 / 3.0 | 42 / 13 | **joint jump 1.17 rad (Right_Elbow_Pitch at 10.2 s)**; **root turn 10 deg/frame** *(excluded)* |
| `lawrence_0_69_69_t34-44_shift` | B | 4_lawrence_0_69_69 33.7–43.7 s | 15.7 / 9.7 | 42 / 12 | upper-arm twist at limit 39%; **joint jump 0.63 rad (Right_Elbow_Pitch at 6.1 s)** *(excluded)* |
| `lawrence_0_70_70_t38-44` | A | 4_lawrence_0_70_70 38.0–44.5 s | 1.4 / 0.9 | 37 / 9 | head at limit 19%; shoulder at limit 96%; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `lawrence_0_70_70_t5-9` | A | 4_lawrence_0_70_70 4.5–9.5 s | 9.1 / 4.7 | 51 / 14 | head at limit 8%; shoulder at limit 82%; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `lawrence_0_71_71_t4-8` | A | 4_lawrence_0_71_71 3.8–8.2 s | 7.1 / 3.5 | 67 / 19 | shoulder at limit 42%; **joint jump 1.59 rad (Left_Shoulder_Pitch at 3.1 s)**; **root turn 10 deg/frame**; left arm behind body 8 cm (human's in front) *(excluded)* |
| `lawrence_0_71_71_t6-11_shift` | B | 4_lawrence_0_71_71 6.2–10.7 s | 12.6 / 7.5 | 68 / 19 | outlier knee max (z +3.5); **joint jump 1.20 rad (Right_Elbow_Pitch at 0.7 s)**; **root turn 12 deg/frame** *(excluded)* |
| `lawrence_0_72_72_t4-8_shift` | B | 4_lawrence_0_72_72 4.4–8.4 s | 18.9 / 11.1 | 34 / 6 | shoulder at limit 47%; outlier knee max (z +4.0); **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `lawrence_0_72_72_t5-15` | A | 4_lawrence_0_72_72 5.2–15.4 s | 4.6 / 1.6 | 37 / 10 | shoulder at limit 76%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `lawrence_0_78_78_t0-7_shift` | B | 4_lawrence_0_78_78 0.0–7.5 s | 18.0 / 10.3 | 44 / 14 | **joint jump 1.57 rad (Left_Shoulder_Pitch at 1.4 s)**; **root jump 3.4 cm/frame**; **root turn 21 deg/frame** *(excluded)* |
| `lawrence_0_79_79_t15-19_shift` | B | 4_lawrence_0_79_79 15.2–19.2 s | 9.2 / 6.1 | 13 / 5 | **root turn 7 deg/frame** *(excluded)* |
| `lawrence_0_79_79_t22-30_shift` | B | 4_lawrence_0_79_79 22.2–30.3 s | 15.9 / 9.1 | 62 / 18 | **upper-arm twist at limit 56%** *(excluded)* |
| `lawrence_0_86_86_t13-18_shift` | B | 4_lawrence_0_86_86 13.1–17.6 s | 8.3 / 5.5 | 54 / 19 | shoulder at limit 7%; **joint jump 1.64 rad (Left_Shoulder_Pitch at 1.3 s)**; **root jump 3.2 cm/frame**; **root turn 28 deg/frame** *(excluded)* |
| `lawrence_0_95_95_t59-63` | A | 4_lawrence_0_95_95 58.6–63.3 s | 8.8 / 4.4 | 59 / 14 | shoulder at limit 79%; **left arm behind body 12 cm (human's in front)** *(excluded)* |
| `lawrence_0_98_98_t26-36_shift` | B | 4_lawrence_0_98_98 26.4–36.1 s | 15.2 / 8.7 | 51 / 16 | upper-arm twist at limit 29%; **excluded in the spec (fails in training)** *(excluded)* |
| `lawrence_0_98_98_t41-45` | A | 4_lawrence_0_98_98 40.9–45.4 s | 2.6 / 3.4 | 65 / 17 | upper-arm twist at limit 18%; **excluded in the spec (fails in training)** *(excluded)* |
| `lawrence_0_98_98_t43-48_shift` | B | 4_lawrence_0_98_98 43.4–47.9 s | 10.9 / 8.4 | 63 / 16 | shoulder at limit 15%; **upper-arm twist at limit 73%**; outlier knee max (z +4.3) *(excluded)* |
| `lawrence_0_98_98_t46-50` | A | 4_lawrence_0_98_98 45.9–50.1 s | 0.9 / 1.4 | 54 / 19 | shoulder at limit 32%; **joint jump 1.94 rad (Left_Shoulder_Pitch at 1.6 s)**; **root jump 3.7 cm/frame**; **root turn 34 deg/frame** *(excluded)* |
| `lawrence_1_10_10_t127-133_shift` | B | 4_lawrence_1_10_10 126.9–132.7 s | 23.2 / 15.0 | 54 / 16 | head at limit 22%; shoulder at limit 5%; upper-arm twist at limit 23%; outlier knee max (z +3.8); hand presses into leg 10 mm for 0.1 s (at 4.4 s); **excluded in the spec (fails in training)** *(excluded)* |
| `lawrence_1_10_10_t161-171_shift` | B | 4_lawrence_1_10_10 160.7–171.2 s | 21.0 / 12.3 | 30 / 12 | trunk drop 13 cm; knee 91 deg; **outlier trunk drop (z +15.8)**; outlier knee max (z +18.4) *(excluded)* |
| `lawrence_1_10_10_t494-510` | A | 4_lawrence_1_10_10 494.0–509.8 s | 1.4 / 1.0 | 49 / 13 | shoulder at limit 16%; **joint jump 0.87 rad (Right_Elbow_Pitch at 5.1 s)**; **root turn 12 deg/frame** *(excluded)* |
| `lawrence_1_10_10_t542-554` | A | 4_lawrence_1_10_10 541.9–553.7 s | 10.0 / 5.2 | 17 / 5 | head at limit 5%; **foot held 42 mm off the floor (median)**; hand presses into leg 9 mm for 4.1 s (at 5.1 s) *(excluded)* |
| `lawrence_1_10_10_t552-556_shift` | B | 4_lawrence_1_10_10 551.7–555.7 s | 12.9 / 7.5 | 19 / 7 | head at limit 30%; **foot held 37 mm off the floor (median)** *(excluded)* |
| `lawrence_1_10_10_t609-617_shift` | B | 4_lawrence_1_10_10 608.9–617.0 s | 38.3 / 24.1 | 34 / 9 | human steps; K1 feet move 24 cm; shoulder at limit 7%; **joint jump 0.95 rad (Right_Elbow_Pitch at 5.0 s)**; **root turn 10 deg/frame** *(excluded)* |
| `lawrence_1_10_10_t611-616` | A | 4_lawrence_1_10_10 611.2–616.2 s | 4.0 / 2.4 | 33 / 10 | shoulder at limit 11%; **joint jump 0.95 rad (Right_Elbow_Pitch at 2.7 s)**; **root turn 10 deg/frame** *(excluded)* |
| `lawrence_1_10_10_t627-637_shift` | B | 4_lawrence_1_10_10 627.1–636.8 s | 19.1 / 16.7 | 32 / 10 | outlier knee max (z +5.2); **joint jump 1.23 rad (Right_Elbow_Pitch at 3.0 s)**; **root turn 13 deg/frame** *(excluded)* |
| `lawrence_1_11_11_t107-113` | A | 4_lawrence_1_11_11 106.8–113.0 s | 3.3 / 1.2 | 31 / 12 | shoulder at limit 38%; upper-arm twist at limit 20%; **joint jump 2.07 rad (Left_Shoulder_Roll at 2.4 s)**; **root turn 19 deg/frame** *(excluded)* |
| `lawrence_1_11_11_t149-159_shift` | B | 4_lawrence_1_11_11 148.7–158.7 s | 23.7 / 20.8 | 22 / 10 | K1 feet move 21 cm; trunk drop 5 cm; knee 83 deg; leg at limit 40%; **ground IK failed 95 frames**; **outlier trunk drop (z +5.9)**; outlier knee max (z +15.5); **foot held 39 mm off the floor (median)** *(excluded)* |
| `lawrence_1_12_12_t0-9` | A | 4_lawrence_1_12_12 0.0–9.2 s | 4.9 / 2.1 | 17 / 5 | **foot held 36 mm off the floor (median)** *(excluded)* |
| `lawrence_1_12_12_t241-245_shift` | B | 4_lawrence_1_12_12 240.6–245.3 s | 6.0 / 4.5 | 36 / 8 | outlier knee max (z +4.4); **foot held 34 mm off the floor (median)** *(excluded)* |
| `lawrence_1_12_12_t332-336_shift` | B | 4_lawrence_1_12_12 331.9–336.1 s | 17.0 / 16.3 | 25 / 9 | knee 87 deg; leg at limit 21%; **ground IK failed 10 frames**; outlier knee max (z +17.1) *(excluded)* |
| `lawrence_1_12_12_t377-392` | A | 4_lawrence_1_12_12 376.9–391.9 s | 4.8 / 1.2 | 4 / 2 | head at limit 36%; **foot held 42 mm off the floor (median)** *(excluded)* |
| `lawrence_1_1_1_t590-601` | A | 4_lawrence_1_1_1 590.0–600.6 s | 2.9 / 4.3 | 23 / 9 | leg at limit 6%; **ground IK failed 5 frames** *(excluded)* |
| `lawrence_1_1_1_t85-89_shift` | B | 4_lawrence_1_1_1 84.6–89.3 s | 21.1 / 9.9 | 57 / 14 | knee 65 deg; leg at limit 6%; **ground IK failed 6 frames**; outlier knee max (z +9.8) *(excluded)* |
| `lawrence_1_2_2_t325-329_shift` | B | 4_lawrence_1_2_2 324.8–329.1 s | 24.8 / 11.9 | 19 / 9 | knee 80 deg; head at limit 100%; shoulder at limit 100%; **upper-arm twist at limit 100%**; leg at limit 100%; **ground IK failed 128 frames**; outlier knee max (z +14.6); **trunk leans 57 deg (median)**; **foot held 42 mm off the floor (median)**; hand presses into leg 42 mm for 0.9 s (at 1.9 s); right arm behind body 8 cm (human's in front) *(excluded)* |
| `lawrence_1_2_2_t478-482_shift` | B | 4_lawrence_1_2_2 478.0–482.3 s | 22.2 / 12.6 | 11 / 3 | knee 60 deg; **ground IK failed 4 frames**; outlier knee max (z +8.2); **joint jump 0.62 rad (Left_Knee_Pitch at 1.8 s)** *(excluded)* |
| `lawrence_1_3_3_t254-258_shift` | B | 4_lawrence_1_3_3 253.8–258.5 s | 10.7 / 6.9 | 38 / 12 | head at limit 13%; outlier knee max (z +4.3); **joint jump 0.71 rad (Right_Shoulder_Pitch at 0.1 s)**; **root turn 10 deg/frame** *(excluded)* |
| `lawrence_1_3_3_t83-89` | A | 4_lawrence_1_3_3 82.8–88.8 s | 4.3 / 8.0 | 40 / 11 | K1 feet move 8 cm; knee 65 deg; head at limit 100%; shoulder at limit 100%; **upper-arm twist at limit 66%**; leg at limit 100%; **ground IK failed 180 frames**; outlier knee max (z +9.6); **trunk leans 54 deg (median)**; **foot held 67 mm off the floor (median)**; **right arm behind body 11 cm (human's in front)** *(excluded)* |
| `lawrence_1_4_4_t214-222_shift` | B | 4_lawrence_1_4_4 214.2–221.7 s | 14.4 / 18.3 | 44 / 7 | K1 feet move 18 cm; knee 97 deg; head at limit 100%; **upper-arm twist at limit 91%**; shoulder at limit 100%; leg at limit 100%; **ground IK failed 224 frames**; outlier trunk drop (z +5.0); outlier knee max (z +20.3); **root turn 7 deg/frame**; **trunk leans 87 deg (median)**; **left foot slides 4.0 cm in one frame (at 7.4 s)**; self-collision right_hip_yaw_collision / trunk_collision 1.0 s (at 6.3 s, 21 mm); **foot held 109 mm off the floor (median)**; **right arm behind body 16 cm (human's in front)** *(excluded)* |
| `lawrence_1_4_4_t227-236` | A | 4_lawrence_1_4_4 227.1–235.6 s | 5.0 / 5.3 | 34 / 10 | **ground IK failed 9 frames** *(excluded)* |
| `lawrence_1_4_4_t24-31` | A | 4_lawrence_1_4_4 23.5–31.3 s | 5.6 / 2.5 | 24 / 6 | head at limit 54%; shoulder at limit 100%; **upper-arm twist at limit 51%**; **trunk leans 45 deg (median)**; **foot held 58 mm off the floor (median)**; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `lawrence_1_4_4_t303-310_shift` | B | 4_lawrence_1_4_4 302.9–309.7 s | 15.1 / 3.7 | 48 / 14 | leg at limit 18%; **ground IK failed 34 frames**; outlier knee max (z +4.1) *(excluded)* |
| `lawrence_1_4_4_t316-321_shift` | B | 4_lawrence_1_4_4 315.8–320.7 s | 12.1 / 3.8 | 36 / 9 | knee 67 deg; leg at limit 25%; **ground IK failed 13 frames**; outlier knee max (z +10.4); **foot held 40 mm off the floor (median)** *(excluded)* |
| `lawrence_1_4_4_t319-325` | A | 4_lawrence_1_4_4 318.7–324.6 s | 7.3 / 8.3 | 18 / 5 | K1 feet move 8 cm; knee 67 deg; leg at limit 60%; **ground IK failed 75 frames**; outlier trunk drop (z +3.7); outlier knee max (z +10.4); **foot held 80 mm off the floor (median)** *(excluded)* |
| `lawrence_1_4_4_t323-327_shift` | B | 4_lawrence_1_4_4 322.6–327.1 s | 11.5 / 10.0 | 31 / 11 | knee 65 deg; leg at limit 19%; **ground IK failed 23 frames**; outlier knee max (z +9.8) *(excluded)* |
| `lawrence_1_4_4_t411-422` | A | 4_lawrence_1_4_4 411.4–422.0 s | 2.2 / 2.2 | 7 / 4 | shoulder at limit 45%; **left arm behind body 10 cm (human's in front)** *(excluded)* |
| `lawrence_1_4_4_t542-546` | A | 4_lawrence_1_4_4 542.1–546.1 s | 2.6 / 1.2 | 13 / 6 | shoulder at limit 40%; **self-collision left_hand_collision / right_hand_end_collision 3.1 s (at 0.5 s, 36 mm)** *(excluded)* |
| `lawrence_1_5_5_t134-138_shift` | B | 4_lawrence_1_5_5 133.8–137.8 s | 25.0 / 15.2 | 42 / 18 | shoulder at limit 87%; outlier knee max (z +6.7); **joint jump 2.28 rad (Left_Shoulder_Roll at 2.8 s)**; **root turn 14 deg/frame**; **left arm behind body 10 cm (human's in front)** *(excluded)* |
| `lawrence_1_5_5_t188-198` | A | 4_lawrence_1_5_5 187.5–197.8 s | 1.4 / 14.8 | 6 / 7 | K1 feet move 15 cm; trunk drop 6 cm; knee 113 deg; head at limit 81%; shoulder at limit 99%; **upper-arm twist at limit 100%**; leg at limit 100%; **ground IK failed 310 frames**; **outlier trunk drop (z +5.9)**; outlier knee max (z +25.7); **joint jump 0.79 rad (Right_Shoulder_Pitch at 8.4 s)**; **root turn 13 deg/frame**; **trunk leans 61 deg (median)**; **foot held 168 mm off the floor (median)**; hand presses into leg 57 mm for 0.2 s (at 6.3 s) *(excluded)* |
| `lawrence_1_5_5_t225-238` | A | 4_lawrence_1_5_5 224.7–238.0 s | 6.1 / 2.5 | 41 / 14 | shoulder at limit 32%; **joint jump 1.16 rad (Right_Elbow_Pitch at 12.3 s)**; **root turn 23 deg/frame**; **foot held 32 mm off the floor (median)** *(excluded)* |
| `lawrence_1_5_5_t331-343` | A | 4_lawrence_1_5_5 331.1–342.6 s | 5.7 / 4.8 | 35 / 13 | **joint jump 2.11 rad (Left_Shoulder_Pitch at 1.7 s)**; **root turn 16 deg/frame** *(excluded)* |
| `lawrence_1_5_5_t454-466` | A | 4_lawrence_1_5_5 453.7–466.0 s | 2.6 / 1.8 | 11 / 3 | head at limit 7%; shoulder at limit 100%; **trunk leans 20 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `lawrence_1_5_5_t83-87_shift` | B | 4_lawrence_1_5_5 82.7–86.7 s | 18.4 / 5.3 | 10 / 3 | knee 75 deg; **ground IK failed 4 frames**; outlier knee max (z +13.0); **joint jump 1.13 rad (Right_Ankle_Pitch at 2.9 s)**; **foot held 67 mm off the floor (median)** *(excluded)* |
| `lawrence_1_5_5_t84-90` | A | 4_lawrence_1_5_5 84.1–90.4 s | 2.4 / 1.5 | 24 / 7 | knee 74 deg; leg at limit 10%; **ground IK failed 1 frames**; outlier knee max (z +12.6); **joint jump 1.07 rad (Right_Ankle_Pitch at 1.5 s)**; **foot held 71 mm off the floor (median)** *(excluded)* |
| `lawrence_1_6_6_t211-218` | A | 4_lawrence_1_6_6 211.2–217.8 s | 5.0 / 0.7 | 28 / 7 | **foot held 34 mm off the floor (median)**; hand presses into leg 10 mm for 0.4 s (at 1.9 s) *(excluded)* |
| `lawrence_1_6_6_t493-505` | A | 4_lawrence_1_6_6 492.6–504.6 s | 3.0 / 1.3 | 26 / 8 | head at limit 9%; **foot held 36 mm off the floor (median)** *(excluded)* |
| `lawrence_1_6_6_t54-61` | A | 4_lawrence_1_6_6 54.3–60.5 s | 1.0 / 27.5 | 98 / 21 | K1 feet move 28 cm; trunk drop 18 cm; knee 104 deg; head at limit 98%; shoulder at limit 92%; elbow bend at limit 98%; **upper-arm twist at limit 61%**; leg at limit 100%; **ground IK failed 186 frames**; outlier arms k1 cm (z +3.9); **outlier trunk drop (z +23.1)**; outlier knee max (z +22.7); **joint jump 0.89 rad (Head_Yaw at 2.4 s)**; **root jump 8.5 cm/frame**; **root turn 25 deg/frame**; **trunk leans 61 deg (median)**; **self-collision left_hand_end_collision / trunk_collision 0.8 s (at 1.4 s, 54 mm)**; **foot held 82 mm off the floor (median)**; left arm behind body 6 cm (human's in front); **right arm behind body 12 cm (human's in front)** *(excluded)* |
| `lawrence_1_6_6_t612-628` | A | 4_lawrence_1_6_6 611.9–627.9 s | 7.2 / 1.5 | 44 / 12 | **foot held 32 mm off the floor (median)** *(excluded)* |
| `lawrence_1_7_7_t156-160_shift` | B | 4_lawrence_1_7_7 155.6–160.4 s | 6.6 / 2.7 | 28 / 11 | shoulder at limit 86%; **left arm behind body 13 cm (human's in front)** *(excluded)* |
| `lawrence_1_7_7_t436-446` | A | 4_lawrence_1_7_7 436.3–446.2 s | 9.2 / 5.1 | 58 / 17 | **upper-arm twist at limit 51%**; shoulder at limit 7%; leg at limit 28%; **ground IK failed 76 frames**; **joint jump 0.60 rad (Left_Elbow_Pitch at 4.7 s)**; **root turn 8 deg/frame**; **foot held 42 mm off the floor (median)** *(excluded)* |
| `lawrence_1_7_7_t452-458` | A | 4_lawrence_1_7_7 452.5–457.9 s | 3.9 / 4.1 | 11 / 4 | leg at limit 11%; **ground IK failed 8 frames** *(excluded)* |
| `lawrence_1_7_7_t506-510_shift` | B | 4_lawrence_1_7_7 506.1–510.1 s | 18.2 / 12.6 | 21 / 20 | trunk drop 8 cm; head at limit 21%; shoulder at limit 49%; **upper-arm twist at limit 97%**; leg at limit 40%; **ground IK failed 43 frames**; **outlier trunk drop (z +8.8)**; **joint jump 1.17 rad (Left_Shoulder_Pitch at 1.9 s)**; **root jump 8.0 cm/frame**; **root turn 36 deg/frame**; **foot held 106 mm off the floor (median)**; left arm behind body 6 cm (human's in front) *(excluded)* |
| `lawrence_1_7_7_t93-99` | A | 4_lawrence_1_7_7 93.3–99.1 s | 3.2 / 16.5 | 42 / 15 | K1 feet move 16 cm; trunk drop 13 cm; knee 113 deg; head at limit 87%; shoulder at limit 24%; leg at limit 100%; **ground IK failed 173 frames**; **outlier trunk drop (z +15.8)**; outlier knee max (z +25.6); **joint jump 1.56 rad (Right_Hip_Roll at 0.1 s)**; **root jump 31.3 cm/frame**; **root turn 64 deg/frame**; **trunk leans 71 deg (median)**; self-collision head_2_collision / left_hand_collision 0.2 s (at 3.5 s, 21 mm); **foot held 154 mm off the floor (median)** *(excluded)* |
| `lawrence_1_8_8_t154-159_shift` | B | 4_lawrence_1_8_8 154.4–159.2 s | 17.9 / 12.4 | 37 / 10 | **ground IK failed 4 frames**; **joint jump 0.62 rad (Left_Knee_Pitch at 2.4 s)** *(excluded)* |
| `lawrence_1_8_8_t205-209_shift` | B | 4_lawrence_1_8_8 204.6–208.6 s | 23.8 / 14.2 | 15 / 10 | shoulder at limit 24%; **joint jump 1.85 rad (Left_Shoulder_Pitch at 1.0 s)**; **root turn 27 deg/frame** *(excluded)* |
| `lawrence_1_8_8_t299-303_shift` | B | 4_lawrence_1_8_8 299.2–303.4 s | 17.1 / 12.3 | 59 / 15 | knee 94 deg; head at limit 15%; shoulder at limit 57%; leg at limit 100%; **ground IK failed 124 frames**; outlier knee max (z +19.4); **trunk leans 63 deg (median)**; **self-collision right_foot_collision / right_hand_end_collision 0.3 s (at 1.2 s, 30 mm)**; **foot held 164 mm off the floor (median)** *(excluded)* |
| `lawrence_1_8_8_t382-386` | A | 4_lawrence_1_8_8 381.7–386.1 s | 3.8 / 11.4 | 25 / 2 | K1 feet move 11 cm; knee 79 deg; head at limit 100%; shoulder at limit 100%; upper-arm twist at limit 8%; leg at limit 100%; **ground IK failed 130 frames**; outlier knee max (z +14.4); **trunk leans 67 deg (median)**; **foot held 42 mm off the floor (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `lawrence_1_8_8_t563-569` | A | 4_lawrence_1_8_8 562.5–568.8 s | 4.2 / 1.9 | 30 / 8 | **foot held 45 mm off the floor (median)** *(excluded)* |
| `lawrence_1_8_8_t630-636_shift` | B | 4_lawrence_1_8_8 629.9–635.8 s | 10.0 / 5.8 | 67 / 18 | shoulder at limit 24%; **joint jump 1.77 rad (Left_Shoulder_Pitch at 1.9 s)**; **root turn 24 deg/frame** *(excluded)* |
| `lawrence_1_9_9_t106-120` | A | 4_lawrence_1_9_9 106.5–120.3 s | 4.2 / 6.3 | 14 / 5 | **foot held 36 mm off the floor (median)** *(excluded)* |
| `lawrence_1_9_9_t14-18_shift` | B | 4_lawrence_1_9_9 13.5–18.1 s | 22.5 / 12.2 | 3 / 2 | head at limit 24%; outlier knee max (z +5.7); **foot held 41 mm off the floor (median)** *(excluded)* |
| `lawrence_1_9_9_t316-322_shift` | B | 4_lawrence_1_9_9 315.8–321.7 s | 24.1 / 14.5 | 50 / 21 | shoulder at limit 32%; outlier arms k1 cm (z +3.9); outlier knee max (z +6.7); **joint jump 1.66 rad (Left_Shoulder_Pitch at 2.5 s)**; **root turn 31 deg/frame** *(excluded)* |
| `lawrence_1_9_9_t34-42_shift` | B | 4_lawrence_1_9_9 34.4–42.3 s | 17.4 / 7.9 | 56 / 23 | trunk drop 7 cm; knee 69 deg; outlier arms k1 cm (z +4.3); **outlier trunk drop (z +7.3)**; outlier knee max (z +11.0); **foot held 34 mm off the floor (median)** *(excluded)* |
| `lawrence_1_9_9_t479-485` | A | 4_lawrence_1_9_9 478.7–484.6 s | 1.8 / 1.3 | 1 / 1 | knee 71 deg; head at limit 5%; leg at limit 51%; **ground IK failed 48 frames**; outlier knee max (z +11.7); **joint jump 1.21 rad (Left_Ankle_Pitch at 0.6 s)**; **foot held 80 mm off the floor (median)** *(excluded)* |
| `lawrence_1_9_9_t495-499_shift` | B | 4_lawrence_1_9_9 494.7–499.3 s | 13.7 / 11.0 | 26 / 9 | **foot held 40 mm off the floor (median)** *(excluded)* |
| `lawrence_1_9_9_t511-516_shift` | B | 4_lawrence_1_9_9 510.7–515.5 s | 18.9 / 12.5 | 30 / 8 | outlier knee max (z +3.9); **foot held 42 mm off the floor (median)** *(excluded)* |
| `li_1_1_1_t104-123` | A | 20_li_1_1_1 103.7–122.9 s | 7.8 / 5.2 | 28 / 10 | head at limit 13%; **joint jump 0.89 rad (Head_Yaw at 16.2 s)**; **root turn 11 deg/frame** *(excluded)* |
| `li_1_1_1_t121-126_shift` | B | 20_li_1_1_1 120.9–125.6 s | 11.4 / 7.7 | 24 / 7 | head at limit 38%; outlier knee max (z +4.3); **root turn 11 deg/frame** *(excluded)* |
| `li_1_1_1_t136-140` | A | 20_li_1_1_1 135.7–140.0 s | 5.5 / 2.4 | 46 / 13 | **foot held 32 mm off the floor (median)** *(excluded)* |
| `li_1_1_1_t14-28` | A | 20_li_1_1_1 13.5–28.4 s | 5.0 / 2.7 | 22 / 7 | **joint jump 0.93 rad (Head_Yaw at 8.9 s)**; **root turn 8 deg/frame** *(excluded)* |
| `li_1_1_1_t145-150_shift` | B | 20_li_1_1_1 145.4–150.1 s | 8.5 / 4.1 | 19 / 5 | head at limit 91%; shoulder at limit 100%; outlier knee max (z +4.2); **trunk leans 41 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `li_1_1_1_t3-16_shift` | B | 20_li_1_1_1 3.2–15.5 s | 21.6 / 13.1 | 69 / 18 | trunk drop 5 cm; head at limit 57%; shoulder at limit 62%; **upper-arm twist at limit 56%**; **outlier trunk drop (z +5.4)**; outlier knee max (z +4.1); **joint jump 0.71 rad (Right_Shoulder_Pitch at 2.5 s)**; **trunk leans 54 deg (median)** *(excluded)* |
| `li_1_1_1_t45-49_shift` | B | 20_li_1_1_1 44.7–49.2 s | 9.4 / 6.2 | 18 / 7 | head at limit 7%; **joint jump 0.93 rad (Head_Yaw at 2.9 s)**; **root turn 10 deg/frame** *(excluded)* |
| `li_1_1_1_t47-53` | A | 20_li_1_1_1 47.2–52.9 s | 0.7 / 0.6 | 14 / 6 | head at limit 12%; **joint jump 0.93 rad (Head_Yaw at 0.4 s)**; **root turn 13 deg/frame** *(excluded)* |
| `li_1_1_1_t471-477` | A | 20_li_1_1_1 471.2–477.4 s | 3.0 / 3.3 | 11 / 4 | head at limit 17%; **joint jump 0.73 rad (Head_Yaw at 5.2 s)** *(excluded)* |
| `li_1_1_1_t484-488_shift` | B | 20_li_1_1_1 483.6–488.2 s | 13.4 / 8.3 | 14 / 3 | head at limit 78%; shoulder at limit 87%; outlier knee max (z +5.1); **trunk leans 30 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `li_1_1_1_t50-54_shift` | B | 20_li_1_1_1 49.5–53.5 s | 27.6 / 16.5 | 12 / 5 | human steps; head at limit 13%; **joint jump 0.99 rad (Head_Yaw at 3.8 s)**; **root turn 13 deg/frame** *(excluded)* |
| `li_1_1_1_t53-58` | A | 20_li_1_1_1 53.5–58.5 s | 4.4 / 1.7 | 11 / 7 | head at limit 19%; **root turn 8 deg/frame** *(excluded)* |
| `li_1_1_1_t59-67_shift` | B | 20_li_1_1_1 59.1–66.8 s | 22.3 / 12.8 | 16 / 7 | head at limit 25%; outlier knee max (z +3.9); **joint jump 0.99 rad (Head_Yaw at 6.0 s)**; **root turn 12 deg/frame** *(excluded)* |
| `li_1_1_1_t65-71` | A | 20_li_1_1_1 64.8–70.8 s | 0.7 / 0.8 | 9 / 4 | head at limit 18%; **joint jump 0.99 rad (Head_Yaw at 0.2 s)**; **root turn 12 deg/frame**; **Head_Yaw over its speed limit for 0.13 s (at 4.3 s)** *(excluded)* |
| `li_1_1_1_t69-73_shift` | B | 20_li_1_1_1 68.8–73.2 s | 7.4 / 5.3 | 13 / 6 | head at limit 11%; **joint jump 0.73 rad (Head_Yaw at 0.4 s)**; **root turn 10 deg/frame**; **Head_Yaw over its speed limit for 0.13 s (at 0.4 s)** *(excluded)* |
| `li_1_1_1_t74-78_shift` | B | 20_li_1_1_1 73.6–78.1 s | 7.8 / 5.0 | 18 / 11 | **joint jump 0.79 rad (Head_Yaw at 2.5 s)**; **root turn 7 deg/frame** *(excluded)* |
| `li_1_1_1_t76-84` | A | 20_li_1_1_1 76.1–84.0 s | 1.8 / 0.6 | 24 / 12 | **joint jump 1.04 rad (Right_Elbow_Yaw at 6.7 s)**; **root turn 7 deg/frame** *(excluded)* |
| `li_1_1_1_t82-86_shift` | B | 20_li_1_1_1 82.0–86.4 s | 8.7 / 5.0 | 32 / 14 | **joint jump 1.04 rad (Right_Elbow_Yaw at 0.8 s)** *(excluded)* |
| `li_1_1_1_t84-104` | A | 20_li_1_1_1 84.4–103.7 s | 1.7 / 8.0 | 24 / 10 | K1 feet move 8 cm; head at limit 10%; **joint jump 1.24 rad (Right_Shoulder_Roll at 5.5 s)**; **root jump 4.7 cm/frame**; **root turn 11 deg/frame**; **left foot slides 5.3 cm in one frame (at 5.4 s)** *(excluded)* |
| `li_1_2_2_t120-130_shift` | B | 20_li_1_2_2 119.7–129.7 s | 24.4 / 13.8 | 10 / 3 | head at limit 85%; shoulder at limit 88%; outlier knee max (z +4.6); **trunk leans 36 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `li_1_2_2_t257-262` | A | 20_li_1_2_2 257.5–261.5 s | 1.0 / 1.8 | 24 / 6 | head at limit 44%; shoulder at limit 33%; **root turn 9 deg/frame**; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `li_1_2_2_t347-352_shift` | B | 20_li_1_2_2 347.4–351.9 s | 16.4 / 9.8 | 34 / 12 | shoulder at limit 7%; outlier knee max (z +3.6); **joint jump 1.64 rad (Left_Shoulder_Pitch at 1.2 s)**; **root jump 3.7 cm/frame**; **root turn 21 deg/frame** *(excluded)* |
| `li_1_2_2_t358-369` | A | 20_li_1_2_2 358.2–369.4 s | 2.6 / 1.2 | 15 / 5 | **joint jump 1.45 rad (Left_Shoulder_Pitch at 2.5 s)**; **root turn 29 deg/frame** *(excluded)* |
| `li_1_2_2_t495-503_shift` | B | 20_li_1_2_2 494.9–502.7 s | 25.5 / 16.5 | 10 / 4 | human steps; head at limit 5%; outlier knee max (z +6.5); **joint jump 0.82 rad (Head_Yaw at 3.6 s)**; **root turn 11 deg/frame** *(excluded)* |
| `li_1_2_2_t497-502` | A | 20_li_1_2_2 497.4–501.6 s | 6.8 / 1.9 | 9 / 5 | head at limit 9%; **joint jump 0.82 rad (Head_Yaw at 1.1 s)**; **root turn 11 deg/frame** *(excluded)* |
| `li_1_2_2_t502-514` | A | 20_li_1_2_2 502.2–514.0 s | 1.0 / 1.4 | 37 / 11 | **upper-arm twist at limit 60%**; **joint jump 0.78 rad (Left_Shoulder_Pitch at 2.9 s)**; **root turn 7 deg/frame** *(excluded)* |
| `li_1_3_3_t150-155` | A | 20_li_1_3_3 150.4–154.8 s | 1.5 / 0.5 | 32 / 11 | head at limit 13%; **joint jump 0.94 rad (Head_Yaw at 2.5 s)**; **root turn 8 deg/frame** *(excluded)* |
| `li_1_3_3_t153-157_shift` | B | 20_li_1_3_3 152.8–157.5 s | 15.3 / 11.0 | 28 / 10 | outlier knee max (z +6.3); **joint jump 0.94 rad (Head_Yaw at 0.1 s)**; **root turn 8 deg/frame** *(excluded)* |
| `li_1_3_3_t186-190_shift` | B | 20_li_1_3_3 185.9–190.5 s | 13.1 / 7.6 | 24 / 9 | outlier knee max (z +3.7); **joint jump 0.63 rad (Head_Yaw at 3.9 s)** *(excluded)* |
| `li_1_3_3_t188-193` | A | 20_li_1_3_3 188.5–193.4 s | 1.8 / 0.5 | 24 / 9 | **joint jump 0.63 rad (Head_Yaw at 1.3 s)** *(excluded)* |
| `li_1_3_3_t427-431_shift` | B | 20_li_1_3_3 426.9–431.4 s | 9.8 / 5.9 | 19 / 5 | outlier knee max (z +4.1); **joint jump 0.99 rad (Head_Yaw at 3.9 s)**; **root turn 8 deg/frame** *(excluded)* |
| `li_1_3_3_t429-438` | A | 20_li_1_3_3 429.4–438.1 s | 3.8 / 1.2 | 29 / 10 | **joint jump 0.99 rad (Head_Yaw at 1.4 s)**; **root turn 8 deg/frame** *(excluded)* |
| `li_1_3_3_t449-454_shift` | B | 20_li_1_3_3 448.9–453.5 s | 14.6 / 9.0 | 27 / 11 | shoulder at limit 7%; outlier knee max (z +4.6); **joint jump 1.59 rad (Left_Shoulder_Pitch at 0.9 s)**; **root jump 3.3 cm/frame**; **root turn 22 deg/frame** *(excluded)* |
| `li_1_3_3_t481-486_shift` | B | 20_li_1_3_3 480.9–486.5 s | 12.1 / 9.2 | 32 / 17 | outlier knee max (z +6.7); **joint jump 0.87 rad (Head_Yaw at 0.6 s)**; **root turn 7 deg/frame** *(excluded)* |
| `lu_0_14_14_t11-25` | A | 13_lu_0_14_14 11.1–24.7 s | 2.9 / 1.2 | 31 / 9 | head at limit 52%; shoulder at limit 100%; **trunk leans 26 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `lu_0_14_14_t56-74` | A | 13_lu_0_14_14 55.6–73.7 s | 6.5 / 3.6 | 30 / 9 | **root turn 9 deg/frame** *(excluded)* |
| `lu_0_15_15_t75-81_shift` | B | 13_lu_0_15_15 74.9–81.0 s | 22.9 / 12.9 | 26 / 9 | head at limit 33%; shoulder at limit 100%; outlier knee max (z +3.8); **trunk leans 25 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `lu_0_16_16_t62-73` | A | 13_lu_0_16_16 61.6–72.9 s | 6.9 / 3.7 | 28 / 10 | **joint jump 0.63 rad (Left_Elbow_Pitch at 9.7 s)**; **root turn 7 deg/frame** *(excluded)* |
| `lu_0_16_16_t73-84` | A | 13_lu_0_16_16 72.9–84.1 s | 1.8 / 0.8 | 27 / 10 | **joint jump 0.65 rad (Left_Shoulder_Pitch at 4.9 s)** *(excluded)* |
| `lu_0_1_1_t56-61` | A | 13_lu_0_1_1 56.5–60.9 s | 0.6 / 1.8 | 28 / 16 | head at limit 43%; shoulder at limit 80%; upper-arm twist at limit 16%; **trunk leans 22 deg (median)**; **left arm behind body 12 cm (human's in front)** *(excluded)* |
| `lu_0_5_5_t20-25` | A | 13_lu_0_5_5 19.7–25.1 s | 4.6 / 3.2 | 27 / 5 | head at limit 68%; shoulder at limit 100%; **trunk leans 29 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `lu_0_73_73_t0-16_shift` | B | 13_lu_0_73_73 0.0–16.2 s | 19.4 / 9.8 | 61 / 20 | outlier arms k1 cm (z +3.5); outlier knee max (z +6.6); **root turn 6 deg/frame** *(excluded)* |
| `lu_0_73_73_t38-45_shift` | B | 13_lu_0_73_73 38.1–44.8 s | 19.7 / 10.9 | 40 / 13 | outlier knee max (z +5.2); **root turn 8 deg/frame** *(excluded)* |
| `lu_1_1_1_t154-158_shift` | B | 13_lu_1_1_1 154.1–158.1 s | 13.8 / 11.0 | 72 / 12 | trunk drop 5 cm; knee 65 deg; head at limit 100%; shoulder at limit 100%; **upper-arm twist at limit 100%**; leg at limit 98%; **ground IK failed 116 frames**; **outlier trunk drop (z +5.8)**; outlier knee max (z +9.7); **trunk leans 35 deg (median)**; **foot held 71 mm off the floor (median)**; **left arm behind body 17 cm (human's in front)**; right arm behind body 9 cm (human's in front) *(excluded)* |
| `lu_1_1_1_t285-291_shift` | B | 13_lu_1_1_1 284.9–290.7 s | 19.1 / 10.3 | 39 / 13 | **upper-arm twist at limit 65%**; leg at limit 19%; **ground IK failed 29 frames**; outlier knee max (z +4.2) *(excluded)* |
| `lu_1_1_1_t300-308_shift` | B | 13_lu_1_1_1 300.1–308.4 s | 25.5 / 18.3 | 27 / 15 | human steps; K1 feet move 18 cm; upper-arm twist at limit 25%; **root turn 12 deg/frame** *(excluded)* |
| `lu_1_1_1_t309-318` | A | 13_lu_1_1_1 309.1–318.5 s | 9.7 / 4.9 | 21 / 9 | leg at limit 11%; **ground IK failed 24 frames** *(excluded)* |
| `lu_1_1_1_t316-320_shift` | B | 13_lu_1_1_1 315.6–319.6 s | 17.9 / 9.5 | 31 / 7 | leg at limit 28%; **ground IK failed 30 frames**; outlier knee max (z +6.7) *(excluded)* |
| `lu_1_1_1_t434-443_shift` | B | 13_lu_1_1_1 433.7–443.5 s | 14.3 / 8.7 | 30 / 10 | **root turn 7 deg/frame** *(excluded)* |
| `lu_1_3_3_t386-395_shift` | B | 13_lu_1_3_3 386.0–395.1 s | 28.4 / 19.1 | 22 / 7 | human steps; K1 feet move 19 cm; leg at limit 17%; **ground IK failed 42 frames**; outlier knee max (z +4.8) *(excluded)* |
| `luqi_0_103_103_t59-64` | A | 22_luqi_0_103_103 59.3–63.8 s | 2.1 / 1.8 | 12 / 4 | **trunk leans 16 deg (median)** *(excluded)* |
| `luqi_0_103_103_t62-66_shift` | B | 22_luqi_0_103_103 61.8–66.3 s | 13.5 / 9.1 | 17 / 6 | **trunk leans 16 deg (median)** *(excluded)* |
| `luqi_0_112_112_t13-23_shift` | B | 22_luqi_0_112_112 12.6–23.3 s | 15.7 / 9.2 | 18 / 7 | **self-collision right_hand_collision / trunk_collision 0.7 s (at 5.1 s, 37 mm)** *(excluded)* |
| `luqi_0_112_112_t21-26` | A | 22_luqi_0_112_112 21.3–26.0 s | 9.4 / 5.4 | 18 / 7 | **trunk leans 19 deg (median)** *(excluded)* |
| `luqi_0_4_4_t16-22_shift` | B | 22_luqi_0_4_4 15.9–22.0 s | 16.9 / 5.4 | 11 / 4 | **ground IK failed 3 frames**; outlier knee max (z +4.5); left arm behind body 5 cm (human's in front) *(excluded)* |
| `luqi_0_4_4_t43-47_shift` | B | 22_luqi_0_4_4 43.0–47.0 s | 14.2 / 1.8 | 13 / 5 | leg at limit 18%; **ground IK failed 7 frames**; outlier knee max (z +4.4) *(excluded)* |
| `luqi_0_65_65_t0-7_shift` | B | 22_luqi_0_65_65 0.0–6.6 s | 9.8 / 9.5 | 32 / 10 | leg at limit 8%; **ground IK failed 14 frames** *(excluded)* |
| `luqi_0_66_66_t53-63_shift` | B | 22_luqi_0_66_66 52.8–63.4 s | 16.9 / 7.8 | 19 / 7 | leg at limit 10%; **ground IK failed 29 frames** *(excluded)* |
| `luqi_0_73_73_t0-12_shift` | B | 22_luqi_0_73_73 0.0–11.6 s | 23.7 / 12.7 | 23 / 8 | **ground IK failed 1 frames**; outlier knee max (z +4.8) *(excluded)* |
| `luqi_0_74_74_t44-50_shift` | B | 22_luqi_0_74_74 43.5–50.3 s | 14.4 / 2.0 | 14 / 5 | **ground IK failed 3 frames** *(excluded)* |
| `luqi_0_74_74_t55-60` | A | 22_luqi_0_74_74 55.3–60.2 s | 3.7 / 1.3 | 27 / 11 | **trunk leans 15 deg (median)**; hand presses into leg 11 mm for 0.4 s (at 4.4 s) *(excluded)* |
| `luqi_0_81_81_t56-61_shift` | B | 22_luqi_0_81_81 55.6–60.9 s | 10.4 / 1.5 | 18 / 5 | leg at limit 6%; **ground IK failed 7 frames** *(excluded)* |
| `luqi_0_82_82_t47-52` | A | 22_luqi_0_82_82 47.3–51.6 s | 2.4 / 0.6 | 27 / 9 | shoulder at limit 13%; **self-collision right_hand_collision / trunk_collision 0.4 s (at 3.9 s, 26 mm)** *(excluded)* |
| `luqi_0_82_82_t50-61_shift` | B | 22_luqi_0_82_82 49.6–60.6 s | 14.7 / 4.7 | 19 / 7 | shoulder at limit 6%; **self-collision right_hand_collision / trunk_collision 1.0 s (at 1.6 s, 33 mm)** *(excluded)* |
| `luqi_0_87_87_t24-28_shift` | B | 22_luqi_0_87_87 24.0–28.0 s | 10.0 / 1.8 | 23 / 8 | **ground IK failed 2 frames** *(excluded)* |
| `luqi_0_87_87_t26-31` | A | 22_luqi_0_87_87 25.6–31.2 s | 9.6 / 1.7 | 24 / 7 | **ground IK failed 2 frames** *(excluded)* |
| `luqi_1_1_1_t536-549` | A | 22_luqi_1_1_1 536.1–549.1 s | 9.9 / 7.6 | 10 / 4 | **self-collision left_hand_end_collision / trunk_collision 2.9 s (at 5.6 s, 39 mm)**; hand presses into leg 37 mm for 0.2 s (at 10.7 s) *(excluded)* |
| `luqi_1_2_2_t104-122` | A | 22_luqi_1_2_2 104.4–121.5 s | 1.4 / 0.3 | 8 / 3 | **trunk leans 17 deg (median)**; self-collision left_hand_collision / trunk_collision 2.8 s (at 0.0 s, 23 mm) *(excluded)* |
| `luqi_1_2_2_t122-139` | A | 22_luqi_1_2_2 121.5–138.6 s | 3.3 / 1.5 | 11 / 5 | **self-collision left_hand_end_collision / right_hand_collision 1.2 s (at 15.9 s, 35 mm)** *(excluded)* |
| `luqi_1_2_2_t137-149_shift` | B | 22_luqi_1_2_2 136.6–148.6 s | 15.0 / 3.0 | 15 / 6 | shoulder at limit 6%; **self-collision left_hand_end_collision / right_hand_collision 1.8 s (at 0.8 s, 35 mm)** *(excluded)* |
| `luqi_1_2_2_t147-165` | A | 22_luqi_1_2_2 146.6–165.2 s | 1.6 / 0.6 | 4 / 2 | **trunk leans 16 deg (median)** *(excluded)* |
| `luqi_1_2_2_t212-217` | A | 22_luqi_1_2_2 212.4–216.9 s | 8.9 / 8.1 | 4 / 2 | K1 feet move 8 cm; **ground IK failed 2 frames** *(excluded)* |
| `luqi_1_2_2_t22-39` | A | 22_luqi_1_2_2 22.2–39.3 s | 2.7 / 0.6 | 8 / 3 | **trunk leans 15 deg (median)**; self-collision left_hand_collision / trunk_collision 7.5 s (at 2.3 s, 24 mm) *(excluded)* |
| `luqi_1_2_2_t245-250_shift` | B | 22_luqi_1_2_2 245.2–250.4 s | 17.2 / 6.1 | 19 / 7 | **ground IK failed 2 frames** *(excluded)* |
| `luqi_1_2_2_t301-312` | A | 22_luqi_1_2_2 301.5–312.3 s | 3.4 / 6.2 | 1 / 1 | **trunk leans 16 deg (median)** *(excluded)* |
| `luqi_1_2_2_t398-403_shift` | B | 22_luqi_1_2_2 398.4–403.1 s | 16.9 / 11.9 | 14 / 4 | **ground IK failed 4 frames**; outlier knee max (z +5.0); hand presses into leg 10 mm for 1.0 s (at 3.7 s) *(excluded)* |
| `luqi_1_2_2_t415-422_shift` | B | 22_luqi_1_2_2 414.8–422.5 s | 21.8 / 11.5 | 15 / 5 | shoulder at limit 57%; **ground IK failed 7 frames**; outlier knee max (z +6.2); **self-collision left_hand_collision / right_hand_end_collision 2.5 s (at 5.2 s, 36 mm)** *(excluded)* |
| `luqi_1_2_2_t420-438` | A | 22_luqi_1_2_2 420.5–438.5 s | 2.2 / 0.6 | 5 / 3 | shoulder at limit 15%; **trunk leans 15 deg (median)**; **self-collision left_hand_collision / right_hand_end_collision 2.3 s (at 0.0 s, 36 mm)** *(excluded)* |
| `luqi_1_2_2_t480-497` | A | 22_luqi_1_2_2 480.3–497.0 s | 5.9 / 11.0 | 10 / 4 | K1 feet move 11 cm; **ground IK failed 8 frames** *(excluded)* |
| `luqi_1_2_2_t499-514` | A | 22_luqi_1_2_2 499.2–513.9 s | 2.5 / 0.3 | 8 / 3 | **trunk leans 15 deg (median)** *(excluded)* |
| `luqi_1_2_2_t588-598` | A | 22_luqi_1_2_2 587.6–597.8 s | 2.0 / 0.7 | 7 / 3 | **trunk leans 16 deg (median)** *(excluded)* |
| `luqi_1_2_2_t598-607` | A | 22_luqi_1_2_2 598.4–606.9 s | 2.5 / 1.0 | 9 / 2 | shoulder at limit 91%; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `luqi_1_3_3_t145-164` | A | 22_luqi_1_3_3 145.4–164.2 s | 4.1 / 0.9 | 6 / 3 | **trunk leans 15 deg (median)** *(excluded)* |
| `luqi_1_3_3_t169-178` | A | 22_luqi_1_3_3 169.2–178.0 s | 1.9 / 0.5 | 17 / 4 | **trunk leans 17 deg (median)** *(excluded)* |
| `luqi_1_3_3_t199-218` | A | 22_luqi_1_3_3 198.9–218.1 s | 1.9 / 0.4 | 20 / 7 | **trunk leans 16 deg (median)** *(excluded)* |
| `luqi_1_3_3_t218-237` | A | 22_luqi_1_3_3 218.1–237.4 s | 3.2 / 0.9 | 15 / 6 | **trunk leans 15 deg (median)** *(excluded)* |
| `luqi_1_3_3_t373-377_shift` | B | 22_luqi_1_3_3 373.4–377.5 s | 12.2 / 17.0 | 10 / 3 | **foot held 40 mm off the floor (median)**; hand presses into leg 26 mm for 3.1 s (at 1.0 s) *(excluded)* |
| `luqi_1_3_3_t375-382` | A | 22_luqi_1_3_3 375.5–382.0 s | 0.1 / 0.5 | 3 / 1 | **foot held 39 mm off the floor (median)**; hand presses into leg 13 mm for 5.6 s (at 1.0 s) *(excluded)* |
| `luqi_1_3_3_t45-63` | A | 22_luqi_1_3_3 44.9–63.4 s | 2.3 / 0.4 | 10 / 5 | elbow bend at limit 8%; **trunk leans 16 deg (median)**; self-collision right_hand_collision / trunk_collision 1.4 s (at 16.1 s, 11 mm) *(excluded)* |
| `luqi_1_3_3_t548-552_shift` | B | 22_luqi_1_3_3 548.3–552.3 s | 8.3 / 4.4 | 13 / 4 | leg at limit 17%; **ground IK failed 17 frames** *(excluded)* |
| `luqi_1_3_3_t553-563` | A | 22_luqi_1_3_3 553.0–562.6 s | 3.0 / 2.0 | 28 / 10 | shoulder at limit 17%; **self-collision right_hand_collision / trunk_collision 2.2 s (at 3.5 s, 34 mm)** *(excluded)* |
| `luqi_1_3_3_t63-82` | A | 22_luqi_1_3_3 63.4–81.9 s | 0.8 / 0.2 | 3 / 1 | **trunk leans 16 deg (median)** *(excluded)* |
| `luqi_1_3_3_t82-100` | A | 22_luqi_1_3_3 81.9–100.4 s | 1.8 / 0.4 | 5 / 2 | **trunk leans 16 deg (median)** *(excluded)* |
| `luqi_1_3_3_t98-107_shift` | B | 22_luqi_1_3_3 98.4–107.1 s | 12.6 / 6.5 | 5 / 2 | **ground IK failed 6 frames** *(excluded)* |
| `miranda_0_113_113_t17-35` | A | 9_miranda_0_113_113 17.4–34.8 s | 0.4 / 0.4 | 21 / 7 | **root turn 7 deg/frame** *(excluded)* |
| `miranda_0_13_13_t0-5_shift` | B | 9_miranda_0_13_13 0.0–5.3 s | 13.0 / 7.4 | 35 / 11 | shoulder at limit 12%; outlier knee max (z +5.0); **joint jump 1.35 rad (Left_Shoulder_Pitch at 1.5 s)**; **root turn 33 deg/frame** *(excluded)* |
| `miranda_0_56_56_t0-18` | A | 9_miranda_0_56_56 0.0–18.4 s | 0.4 / 1.2 | 20 / 7 | shoulder at limit 8%; **joint jump 1.33 rad (Left_Shoulder_Pitch at 1.6 s)**; **root jump 3.8 cm/frame**; **root turn 30 deg/frame** *(excluded)* |
| `miranda_0_57_57_t15-30` | A | 9_miranda_0_57_57 14.9–29.9 s | 4.5 / 1.7 | 32 / 11 | head at limit 8%; **upper-arm twist at limit 85%**; **ground IK failed 27 frames**; **foot held 49 mm off the floor (median)**; hand presses into leg 18 mm for 0.4 s (at 11.9 s) *(excluded)* |
| `miranda_0_66_66_t17-34` | A | 9_miranda_0_66_66 16.9–33.9 s | 1.2 / 1.0 | 27 / 9 | **joint jump 1.10 rad (Right_Elbow_Pitch at 12.0 s)**; **root turn 14 deg/frame** *(excluded)* |
| `miranda_0_71_71_t15-30` | A | 9_miranda_0_71_71 15.2–30.5 s | 0.6 / 0.6 | 24 / 9 | **root turn 7 deg/frame** *(excluded)* |
| `miranda_0_71_71_t28-34_shift` | B | 9_miranda_0_71_71 28.5–34.1 s | 13.1 / 8.3 | 32 / 13 | **root turn 7 deg/frame** *(excluded)* |
| `miranda_0_75_75_t0-15` | A | 9_miranda_0_75_75 0.0–14.9 s | 5.6 / 4.1 | 19 / 6 | head at limit 21%; shoulder at limit 40%; **joint jump 1.30 rad (Left_Shoulder_Pitch at 6.0 s)**; **root turn 33 deg/frame**; left arm behind body 6 cm (human's in front) *(excluded)* |
| `miranda_0_84_84_t28-42` | A | 9_miranda_0_84_84 27.9–41.8 s | 7.8 / 8.5 | 12 / 5 | K1 feet move 9 cm; **ground IK failed 1 frames**; **joint jump 0.68 rad (Left_Elbow_Yaw at 8.6 s)**; **root jump 12.4 cm/frame**; **root turn 18 deg/frame** *(excluded)* |
| `miranda_1_10_10_t580-595` | A | 9_miranda_1_10_10 579.8–594.6 s | 9.6 / 4.8 | 28 / 13 | trunk drop 5 cm; head at limit 39%; **ground IK failed 3 frames**; **outlier trunk drop (z +5.4)**; outlier knee max (z +4.1); **joint jump 0.75 rad (Right_Shoulder_Pitch at 12.1 s)**; **root turn 16 deg/frame**; hand presses into leg 11 mm for 0.8 s (at 9.4 s) *(excluded)* |
| `miranda_1_10_10_t622-626_shift` | B | 9_miranda_1_10_10 622.0–626.0 s | 18.2 / 11.9 | 15 / 4 | knee 62 deg; leg at limit 21%; **ground IK failed 24 frames**; outlier knee max (z +8.7); **joint jump 1.21 rad (Left_Ankle_Pitch at 3.5 s)**; **Left_Ankle_Roll over its speed limit for 0.13 s (at 3.5 s)** *(excluded)* |
| `miranda_1_10_10_t627-635_shift` | B | 9_miranda_1_10_10 627.1–634.9 s | 15.7 / 12.8 | 27 / 7 | knee 70 deg; leg at limit 42%; **ground IK failed 74 frames**; outlier trunk drop (z +4.6); outlier knee max (z +11.5); **self-collision left_shank_lower_collision / right_shank_lower_collision 3.9 s (at 0.0 s, 57 mm)**; **feet overlap 34 mm for 1.4 s (at 0.9 s)** *(excluded)* |
| `miranda_1_10_10_t647-661` | A | 9_miranda_1_10_10 646.8–660.7 s | 2.2 / 2.7 | 26 / 9 | **joint jump 0.87 rad (Left_Shoulder_Pitch at 2.2 s)**; **root jump 4.8 cm/frame**; **root turn 37 deg/frame** *(excluded)* |
| `miranda_1_11_11_t103-120` | A | 9_miranda_1_11_11 102.8–120.3 s | 9.4 / 6.9 | 9 / 4 | trunk drop 11 cm; **ground IK failed 1 frames**; **outlier trunk drop (z +13.1)**; outlier knee max (z +4.0); **joint jump 1.11 rad (Right_Hip_Yaw at 6.2 s)**; **root jump 21.1 cm/frame**; **root turn 56 deg/frame**; **right foot slides 7.0 cm in one frame (at 6.2 s)**; **foot held 43 mm off the floor (median)** *(excluded)* |
| `miranda_1_11_11_t152-168` | A | 9_miranda_1_11_11 152.3–168.0 s | 2.0 / 1.0 | 20 / 7 | head at limit 8%; shoulder at limit 21%; **joint jump 2.55 rad (Left_Elbow_Pitch at 6.7 s)**; **root turn 12 deg/frame** *(excluded)* |
| `miranda_1_11_11_t189-194_shift` | B | 9_miranda_1_11_11 189.3–193.7 s | 23.2 / 19.3 | 13 / 4 | K1 feet move 19 cm; trunk drop 5 cm; knee 114 deg; **outlier trunk drop (z +5.7)**; outlier knee max (z +26.0); **self-collision left_shank_collision / right_shank_lower_collision 0.5 s (at 1.6 s, 25 mm)** *(excluded)* |
| `miranda_1_11_11_t488-492_shift` | B | 9_miranda_1_11_11 487.9–491.9 s | 21.1 / 14.3 | 13 / 6 | outlier knee max (z +5.0); **foot held 32 mm off the floor (median)** *(excluded)* |
| `miranda_1_12_12_t346-364` | A | 9_miranda_1_12_12 345.6–363.5 s | 4.2 / 1.7 | 40 / 15 | head at limit 8%; shoulder at limit 10%; **joint jump 0.91 rad (Right_Elbow_Pitch at 9.2 s)**; **root turn 19 deg/frame**; **foot held 49 mm off the floor (median)**; hand presses into leg 25 mm for 0.2 s (at 2.9 s) *(excluded)* |
| `miranda_1_1_1_t221-225_shift` | B | 9_miranda_1_1_1 220.7–225.1 s | 8.8 / 3.9 | 31 / 12 | shoulder at limit 5%; elbow bend at limit 27%; outlier knee max (z +4.0); **joint jump 1.24 rad (Left_Elbow_Yaw at 0.8 s)**; **root jump 3.6 cm/frame**; **root turn 32 deg/frame** *(excluded)* |
| `miranda_1_1_1_t307-326` | A | 9_miranda_1_1_1 307.4–325.7 s | 5.5 / 2.4 | 41 / 13 | upper-arm twist at limit 5%; **joint jump 1.00 rad (Left_Elbow_Pitch at 7.0 s)**; **root turn 15 deg/frame** *(excluded)* |
| `miranda_1_1_1_t326-344` | A | 9_miranda_1_1_1 325.7–344.0 s | 1.2 / 0.7 | 30 / 11 | **joint jump 0.67 rad (Right_Shoulder_Pitch at 0.0 s)**; **root turn 7 deg/frame** *(excluded)* |
| `miranda_1_1_1_t436-454` | A | 9_miranda_1_1_1 435.5–453.8 s | 1.1 / 0.6 | 41 / 19 | upper-arm twist at limit 7%; **joint jump 0.65 rad (Left_Elbow_Pitch at 12.8 s)**; **root turn 15 deg/frame** *(excluded)* |
| `miranda_1_1_1_t460-478` | A | 9_miranda_1_1_1 460.0–478.2 s | 1.4 / 1.3 | 34 / 12 | upper-arm twist at limit 12%; **joint jump 0.84 rad (Left_Shoulder_Pitch at 16.4 s)**; **root turn 12 deg/frame** *(excluded)* |
| `miranda_1_1_1_t585-590_shift` | B | 9_miranda_1_1_1 585.3–589.5 s | 15.4 / 15.1 | 34 / 13 | **ground IK failed 1 frames**; outlier trunk drop (z +4.7); **joint jump 1.23 rad (Left_Hip_Yaw at 2.1 s)**; **root jump 22.4 cm/frame**; **root turn 32 deg/frame**; **right foot slides 10.4 cm in one frame (at 2.1 s)** *(excluded)* |
| `miranda_1_1_1_t79-94` | A | 9_miranda_1_1_1 79.0–93.9 s | 0.5 / 1.6 | 36 / 14 | upper-arm twist at limit 28%; shoulder at limit 5%; **excluded in the spec (fails in training)** *(excluded)* |
| `miranda_1_2_2_t107-116` | A | 9_miranda_1_2_2 106.7–115.9 s | 7.6 / 6.0 | 7 / 2 | knee 67 deg; leg at limit 44%; **ground IK failed 92 frames**; outlier knee max (z +10.3); **self-collision left_shank_lower_collision / right_shank_lower_collision 9.2 s (at 0.0 s, 83 mm)**; **feet overlap 20 mm for 1.4 s (at 0.4 s)**; **foot held 56 mm off the floor (median)** *(excluded)* |
| `miranda_1_2_2_t387-403` | A | 9_miranda_1_2_2 387.4–402.8 s | 2.7 / 0.9 | 4 / 3 | knee 72 deg; leg at limit 66%; **ground IK failed 275 frames**; outlier knee max (z +12.1); **joint jump 1.21 rad (Left_Ankle_Pitch at 3.1 s)**; **Left_Ankle_Pitch over its speed limit for 0.13 s (at 6.3 s)**; **foot held 83 mm off the floor (median)** *(excluded)* |
| `miranda_1_2_2_t401-406_shift` | B | 9_miranda_1_2_2 400.8–406.0 s | 7.9 / 7.9 | 11 / 5 | knee 68 deg; leg at limit 24%; **ground IK failed 35 frames**; outlier trunk drop (z +3.7); outlier knee max (z +10.8); **joint jump 1.21 rad (Left_Ankle_Pitch at 0.5 s)** *(excluded)* |
| `miranda_1_3_3_t369-386` | A | 9_miranda_1_3_3 368.9–386.5 s | 4.0 / 2.9 | 24 / 10 | **upper-arm twist at limit 63%**; leg at limit 43%; **ground IK failed 230 frames**; **root turn 7 deg/frame** *(excluded)* |
| `miranda_1_3_3_t554-574` | A | 9_miranda_1_3_3 554.3–574.0 s | 3.3 / 3.2 | 33 / 13 | **joint jump 0.61 rad (Right_Elbow_Pitch at 6.7 s)** *(excluded)* |
| `miranda_1_3_3_t584-591` | A | 9_miranda_1_3_3 583.9–590.5 s | 2.0 / 1.3 | 62 / 19 | trunk drop 7 cm; knee 71 deg; **outlier trunk drop (z +8.2)**; outlier knee max (z +11.5) *(excluded)* |
| `miranda_1_3_3_t589-593_shift` | B | 9_miranda_1_3_3 588.5–592.9 s | 12.3 / 6.6 | 56 / 19 | trunk drop 7 cm; knee 66 deg; **outlier trunk drop (z +7.7)**; outlier knee max (z +10.1) *(excluded)* |
| `miranda_1_3_3_t591-596` | A | 9_miranda_1_3_3 590.9–596.5 s | 7.8 / 3.8 | 56 / 22 | trunk drop 6 cm; knee 66 deg; outlier arms k1 cm (z +4.1); **outlier trunk drop (z +6.1)**; outlier knee max (z +10.1); **trunk leans 24 deg (median)** *(excluded)* |
| `miranda_1_3_3_t78-86_shift` | B | 9_miranda_1_3_3 78.1–86.2 s | 15.2 / 7.3 | 29 / 12 | trunk drop 7 cm; knee 67 deg; **outlier trunk drop (z +8.1)**; outlier knee max (z +10.3) *(excluded)* |
| `miranda_1_3_3_t79-83` | A | 9_miranda_1_3_3 79.1–83.5 s | 2.9 / 5.1 | 34 / 14 | trunk drop 7 cm; knee 70 deg; **outlier trunk drop (z +8.1)**; outlier knee max (z +11.3); **trunk leans 17 deg (median)** *(excluded)* |
| `miranda_1_4_4_t187-203` | A | 9_miranda_1_4_4 187.1–203.3 s | 1.4 / 1.3 | 31 / 11 | **upper-arm twist at limit 53%** *(excluded)* |
| `miranda_1_4_4_t250-254_shift` | B | 9_miranda_1_4_4 249.9–254.1 s | 13.7 / 22.0 | 62 / 21 | K1 feet move 22 cm; **ground IK failed 1 frames**; outlier arms k1 cm (z +4.0); outlier knee max (z +5.0); **joint jump 1.65 rad (Right_Hip_Yaw at 2.1 s)**; **root jump 13.6 cm/frame**; **root turn 35 deg/frame** *(excluded)* |
| `miranda_1_4_4_t252-264` | A | 9_miranda_1_4_4 252.1–263.7 s | 1.9 / 0.7 | 37 / 11 | **joint jump 0.77 rad (Right_Elbow_Pitch at 4.9 s)** *(excluded)* |
| `miranda_1_4_4_t372-376_shift` | B | 9_miranda_1_4_4 371.5–375.5 s | 11.8 / 6.9 | 33 / 19 | leg at limit 83%; **ground IK failed 30 frames**; self-collision left_foot_collision / right_foot_collision 3.4 s (at 0.6 s, 17 mm); **feet overlap 17 mm for 3.4 s (at 0.6 s)** *(excluded)* |
| `miranda_1_4_4_t372-392` | A | 9_miranda_1_4_4 372.2–391.6 s | 8.2 / 4.2 | 26 / 10 | leg at limit 39%; **ground IK failed 77 frames**; **self-collision left_foot_collision / right_foot_collision 19.3 s (at 0.0 s, 37 mm)**; **feet overlap 37 mm for 19.3 s (at 0.0 s)** *(excluded)* |
| `miranda_1_4_4_t524-542` | A | 9_miranda_1_4_4 523.5–542.0 s | 0.4 / 1.1 | 36 / 13 | **joint jump 1.06 rad (Right_Shoulder_Pitch at 16.2 s)**; **root turn 16 deg/frame** *(excluded)* |
| `miranda_1_5_5_t128-137_shift` | B | 9_miranda_1_5_5 127.8–136.9 s | 17.1 / 13.7 | 26 / 8 | knee 69 deg; leg at limit 30%; **ground IK failed 71 frames**; outlier knee max (z +11.1); **joint jump 1.21 rad (Left_Ankle_Pitch at 6.1 s)**; **Left_Ankle_Pitch over its speed limit for 0.13 s (at 6.2 s)**; **foot held 76 mm off the floor (median)** *(excluded)* |
| `miranda_1_5_5_t135-145` | A | 9_miranda_1_5_5 134.9–145.3 s | 3.0 / 0.8 | 15 / 5 | knee 75 deg; leg at limit 90%; **ground IK failed 269 frames**; outlier trunk drop (z +4.6); outlier knee max (z +13.0); **joint jump 1.21 rad (Left_Ankle_Pitch at 3.6 s)**; **foot held 85 mm off the floor (median)** *(excluded)* |
| `miranda_1_5_5_t145-156` | A | 9_miranda_1_5_5 145.3–155.7 s | 2.3 / 1.3 | 22 / 7 | knee 75 deg; leg at limit 13%; **ground IK failed 31 frames**; outlier knee max (z +13.0); **joint jump 1.14 rad (Left_Ankle_Pitch at 2.5 s)** *(excluded)* |
| `miranda_1_5_5_t235-253` | A | 9_miranda_1_5_5 234.7–253.1 s | 7.5 / 4.9 | 28 / 14 | **joint jump 0.68 rad (Left_Shoulder_Roll at 4.8 s)**; **root turn 19 deg/frame**; **right foot slides 4.8 cm in one frame (at 4.8 s)** *(excluded)* |
| `miranda_1_5_5_t290-308` | A | 9_miranda_1_5_5 289.8–308.2 s | 4.0 / 1.3 | 18 / 5 | **joint jump 0.87 rad (Right_Elbow_Pitch at 15.1 s)**; **root turn 7 deg/frame** *(excluded)* |
| `miranda_1_5_5_t327-345` | A | 9_miranda_1_5_5 326.6–345.0 s | 1.4 / 0.7 | 35 / 11 | **joint jump 0.72 rad (Right_Shoulder_Pitch at 4.0 s)** *(excluded)* |
| `miranda_1_5_5_t45-53` | A | 9_miranda_1_5_5 44.9–52.9 s | 7.8 / 6.3 | 14 / 4 | knee 63 deg; leg at limit 98%; **ground IK failed 199 frames**; outlier trunk drop (z +3.5); outlier knee max (z +9.1); **joint jump 1.21 rad (Left_Ankle_Pitch at 5.2 s)**; **Left_Ankle_Pitch over its speed limit for 0.23 s (at 5.6 s)**; **self-collision left_shank_lower_collision / right_shank_lower_collision 7.3 s (at 0.0 s, 55 mm)**; **feet overlap 22 mm for 1.5 s (at 1.2 s)** *(excluded)* |
| `miranda_1_5_5_t489-493_shift` | B | 9_miranda_1_5_5 489.2–493.2 s | 12.5 / 5.8 | 25 / 7 | leg at limit 100%; **ground IK failed 117 frames**; **self-collision left_foot_collision / right_foot_collision 2.7 s (at 1.3 s, 30 mm)**; **feet overlap 30 mm for 2.7 s (at 1.3 s)** *(excluded)* |
| `miranda_1_5_5_t491-498` | A | 9_miranda_1_5_5 491.2–498.4 s | 5.7 / 3.1 | 6 / 2 | leg at limit 88%; **ground IK failed 176 frames**; outlier knee max (z +4.3); **self-collision left_shank_lower_collision / right_shank_lower_collision 7.2 s (at 0.0 s, 60 mm)**; **feet overlap 26 mm for 7.2 s (at 0.0 s)** *(excluded)* |
| `miranda_1_5_5_t92-111` | A | 9_miranda_1_5_5 92.2–111.0 s | 2.3 / 0.9 | 28 / 9 | shoulder at limit 11%; **joint jump 0.83 rad (Left_Elbow_Pitch at 16.9 s)**; **root turn 9 deg/frame** *(excluded)* |
| `miranda_1_8_8_t468-488` | A | 9_miranda_1_8_8 468.0–487.9 s | 0.7 / 0.3 | 27 / 10 | **root turn 6 deg/frame** *(excluded)* |
| `nidal_0_1_1_t0-18` | A | 11_nidal_0_1_1 0.0–17.8 s | 1.8 / 1.6 | 17 / 7 | **joint jump 1.36 rad (Left_Shoulder_Pitch at 0.6 s)**; **root turn 28 deg/frame** *(excluded)* |
| `nidal_0_3_3_t0-18` | A | 11_nidal_0_3_3 0.0–17.7 s | 7.9 / 5.6 | 17 / 6 | **joint jump 1.52 rad (Left_Elbow_Pitch at 0.8 s)**; **root turn 25 deg/frame** *(excluded)* |
| `nidal_1_10_10_t235-239_shift` | B | 11_nidal_1_10_10 234.6–238.6 s | 18.5 / 10.7 | 17 / 4 | **ground IK failed 2 frames** *(excluded)* |
| `nidal_1_12_12_t353-358` | A | 11_nidal_1_12_12 353.3–357.8 s | 0.3 / 2.3 | 36 / 8 | head at limit 18%; shoulder at limit 79%; leg at limit 19%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `nidal_1_4_4_t615-632` | A | 11_nidal_1_4_4 614.8–631.8 s | 0.6 / 0.9 | 34 / 8 | **joint jump 2.52 rad (Left_Elbow_Pitch at 0.6 s)**; **root turn 19 deg/frame**; hand presses into leg 57 mm for 0.2 s (at 0.3 s) *(excluded)* |
| `nidal_1_8_8_t303-308` | A | 11_nidal_1_8_8 303.4–307.7 s | 9.2 / 2.4 | 9 / 3 | leg at limit 14%; **ground IK failed 1 frames** *(excluded)* |
| `nidal_1_9_9_t216-233` | A | 11_nidal_1_9_9 216.5–232.8 s | 9.6 / 6.6 | 31 / 8 | **ground IK failed 1 frames** *(excluded)* |
| `nidal_1_9_9_t233-253` | A | 11_nidal_1_9_9 232.8–252.8 s | 8.1 / 4.9 | 26 / 7 | **ground IK failed 5 frames** *(excluded)* |
| `nidal_1_9_9_t337-353` | A | 11_nidal_1_9_9 337.5–353.3 s | 3.9 / 3.9 | 28 / 7 | leg at limit 8%; **ground IK failed 10 frames** *(excluded)* |
| `scott_0_115_115_t22-27_shift` | B | 2_scott_0_115_115 22.5–26.5 s | 16.7 / 9.8 | 71 / 22 | head at limit 10%; upper-arm twist at limit 18%; outlier arms k1 cm (z +4.2); outlier knee max (z +3.8); **root turn 7 deg/frame**; hand presses into leg 12 mm for 0.2 s (at 3.7 s) *(excluded)* |
| `scott_0_20_20_t47-52_shift` | B | 2_scott_0_20_20 46.8–51.9 s | 12.1 / 3.6 | 32 / 9 | leg at limit 5%; **ground IK failed 2 frames**; outlier knee max (z +6.8) *(excluded)* |
| `scott_0_27_27_t18-26_shift` | B | 2_scott_0_27_27 18.3–26.0 s | 24.1 / 14.6 | 67 / 18 | leg at limit 8%; **ground IK failed 15 frames** *(excluded)* |
| `scott_0_28_28_t9-14` | A | 2_scott_0_28_28 9.2–13.8 s | 7.5 / 0.9 | 29 / 11 | **foot held 34 mm off the floor (median)** *(excluded)* |
| `scott_0_31_31_t4-9_shift` | B | 2_scott_0_31_31 4.2–8.7 s | 17.4 / 10.3 | 96 / 28 | trunk drop 7 cm; knee 60 deg; outlier arms k1 cm (z +5.8); **outlier trunk drop (z +7.5)**; outlier knee max (z +8.2) *(excluded)* |
| `scott_0_34_34_t21-34_shift` | B | 2_scott_0_34_34 20.7–33.8 s | 24.0 / 16.0 | 51 / 15 | trunk drop 7 cm; **outlier trunk drop (z +7.7)**; outlier knee max (z +7.0); hand presses into leg 11 mm for 0.2 s (at 6.9 s) *(excluded)* |
| `scott_0_44_44_t38-45_shift` | B | 2_scott_0_44_44 38.5–45.4 s | 13.8 / 8.3 | 55 / 18 | **ground IK failed 4 frames**; outlier knee max (z +4.4) *(excluded)* |
| `scott_0_4_4_t25-30` | A | 2_scott_0_4_4 25.0–30.4 s | 8.7 / 4.9 | 23 / 10 | **root turn 6 deg/frame** *(excluded)* |
| `scott_0_4_4_t28-32_shift` | B | 2_scott_0_4_4 27.7–31.7 s | 18.8 / 12.5 | 38 / 13 | **root turn 6 deg/frame** *(excluded)* |
| `scott_0_62_62_t37-42_shift` | B | 2_scott_0_62_62 37.4–42.2 s | 14.1 / 4.0 | 53 / 14 | **joint jump 0.66 rad (Right_Elbow_Pitch at 0.7 s)**; **root turn 7 deg/frame** *(excluded)* |
| `scott_0_63_63_t34-38_shift` | B | 2_scott_0_63_63 33.8–38.1 s | 23.7 / 13.4 | 75 / 24 | outlier arms k1 cm (z +4.7); outlier knee max (z +5.1); **joint jump 0.66 rad (Right_Shoulder_Pitch at 3.9 s)** *(excluded)* |
| `scott_0_7_7_t60-64` | A | 2_scott_0_7_7 59.9–64.2 s | 4.8 / 1.8 | 50 / 15 | **foot held 30 mm off the floor (median)** *(excluded)* |
| `scott_0_80_80_t56-61` | A | 2_scott_0_80_80 56.3–60.8 s | 5.0 / 1.3 | 73 / 20 | trunk drop 9 cm; knee 65 deg; head at limit 21%; outlier arms k1 cm (z +3.5); **outlier trunk drop (z +11.2)**; outlier knee max (z +9.9) *(excluded)* |
| `scott_0_86_86_t16-24_shift` | B | 2_scott_0_86_86 16.3–23.6 s | 23.0 / 10.5 | 55 / 16 | trunk drop 5 cm; knee 62 deg; **outlier trunk drop (z +5.5)**; outlier knee max (z +8.8) *(excluded)* |
| `scott_0_88_88_t20-26` | A | 2_scott_0_88_88 20.5–26.1 s | 9.5 / 12.7 | 43 / 13 | K1 feet move 13 cm; trunk drop 6 cm; **outlier trunk drop (z +6.2)**; outlier knee max (z +7.8) *(excluded)* |
| `scott_0_88_88_t23-27_shift` | B | 2_scott_0_88_88 23.1–27.1 s | 20.8 / 12.2 | 66 / 19 | trunk drop 5 cm; leg at limit 6%; **outlier trunk drop (z +5.8)**; outlier knee max (z +7.2) *(excluded)* |
| `scott_0_88_88_t45-59_shift` | B | 2_scott_0_88_88 45.3–59.4 s | 23.3 / 16.7 | 54 / 15 | trunk drop 6 cm; knee 61 deg; **outlier trunk drop (z +6.8)**; outlier knee max (z +8.3) *(excluded)* |
| `scott_0_88_88_t57-64` | A | 2_scott_0_88_88 57.4–63.6 s | 8.5 / 4.8 | 52 / 16 | trunk drop 6 cm; knee 62 deg; **outlier trunk drop (z +6.2)**; outlier knee max (z +8.8) *(excluded)* |
| `scott_0_89_89_t10-15` | A | 2_scott_0_89_89 9.9–14.7 s | 1.3 / 1.4 | 42 / 14 | trunk drop 6 cm; **outlier trunk drop (z +6.0)**; outlier knee max (z +8.0); **trunk leans 19 deg (median)** *(excluded)* |
| `scott_0_89_89_t13-19_shift` | B | 2_scott_0_89_89 12.7–18.9 s | 23.7 / 9.2 | 55 / 15 | trunk drop 7 cm; **outlier trunk drop (z +7.9)**; outlier knee max (z +7.6) *(excluded)* |
| `scott_0_90_90_t40-51_shift` | B | 2_scott_0_90_90 40.1–51.1 s | 24.9 / 21.1 | 54 / 14 | K1 feet move 21 cm; outlier knee max (z +5.4); **root turn 7 deg/frame** *(excluded)* |
| `scott_0_91_91_t37-44_shift` | B | 2_scott_0_91_91 37.2–43.5 s | 24.2 / 14.8 | 68 / 22 | knee 61 deg; outlier arms k1 cm (z +4.0); outlier trunk drop (z +3.5); outlier knee max (z +8.2); **excluded in the spec (fails in training)** *(excluded)* |
| `scott_1_10_10_t182-188_shift` | B | 2_scott_1_10_10 182.1–188.0 s | 18.9 / 10.5 | 67 / 18 | trunk drop 6 cm; knee 61 deg; **outlier trunk drop (z +6.7)**; outlier knee max (z +8.4) *(excluded)* |
| `scott_1_11_11_t193-197_shift` | B | 2_scott_1_11_11 193.0–197.1 s | 12.0 / 3.8 | 24 / 8 | upper-arm twist at limit 12%; **root turn 7 deg/frame**; **foot held 31 mm off the floor (median)** *(excluded)* |
| `scott_1_1_1_t129-135` | A | 2_scott_1_1_1 129.4–135.0 s | 4.9 / 18.2 | 22 / 8 | K1 feet move 18 cm; trunk drop 21 cm; head at limit 100%; shoulder at limit 67%; **upper-arm twist at limit 100%**; leg at limit 100%; **ground IK failed 167 frames**; **outlier trunk drop (z +27.8)**; **joint jump 0.75 rad (Right_Shoulder_Pitch at 0.1 s)**; **root jump 12.0 cm/frame**; **root turn 28 deg/frame**; **trunk leans 112 deg (median)**; **self-collision left_hip_yaw_collision / trunk_collision 5.5 s (at 0.1 s, 64 mm)**; **foot held 399 mm off the floor (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `scott_1_1_1_t254-260_shift` | B | 2_scott_1_1_1 254.1–259.9 s | 23.6 / 11.6 | 39 / 14 | upper-arm twist at limit 27%; **excluded in the spec (fails in training)** *(excluded)* |
| `scott_1_2_2_t141-148_shift` | B | 2_scott_1_2_2 141.1–148.0 s | 14.7 / 9.3 | 13 / 6 | **trunk leans 23 deg (median)** *(excluded)* |
| `scott_1_2_2_t182-187_shift` | B | 2_scott_1_2_2 182.3–186.6 s | 11.4 / 9.8 | 51 / 17 | upper-arm twist at limit 49%; **excluded in the spec (fails in training)** *(excluded)* |
| `scott_1_3_3_t277-281_shift` | B | 2_scott_1_3_3 277.4–281.4 s | 11.4 / 7.3 | 57 / 22 | shoulder at limit 80%; outlier arms k1 cm (z +4.2); outlier knee max (z +3.7); **excluded in the spec (fails in training)** *(excluded)* |
| `scott_1_3_3_t394-399_shift` | B | 2_scott_1_3_3 393.8–398.8 s | 15.2 / 15.1 | 32 / 14 | shoulder at limit 9%; upper-arm twist at limit 17%; elbow bend at limit 11%; leg at limit 10%; **ground IK failed 15 frames**; outlier knee max (z +3.6); **joint jump 1.19 rad (Right_Shoulder_Pitch at 3.8 s)**; **root jump 7.5 cm/frame**; **root turn 20 deg/frame** *(excluded)* |
| `scott_1_4_4_t136-143` | A | 2_scott_1_4_4 135.7–143.3 s | 7.9 / 1.9 | 65 / 17 | upper-arm twist at limit 28%; **excluded in the spec (fails in training)** *(excluded)* |
| `scott_1_4_4_t17-23_shift` | B | 2_scott_1_4_4 17.2–22.9 s | 23.2 / 12.5 | 26 / 17 | **joint jump 0.94 rad (Right_Shoulder_Pitch at 4.6 s)**; **root turn 8 deg/frame** *(excluded)* |
| `scott_1_4_4_t176-183_shift` | B | 2_scott_1_4_4 176.4–182.5 s | 25.0 / 17.7 | 63 / 20 | head at limit 11%; shoulder at limit 38%; outlier arms k1 cm (z +3.7); outlier knee max (z +7.0); **joint jump 0.84 rad (Right_Elbow_Pitch at 4.7 s)**; **root turn 10 deg/frame** *(excluded)* |
| `scott_1_4_4_t241-249_shift` | B | 2_scott_1_4_4 241.4–249.1 s | 22.1 / 13.8 | 49 / 15 | shoulder at limit 10%; outlier knee max (z +6.7); **joint jump 1.13 rad (Left_Elbow_Yaw at 0.8 s)**; **root jump 3.2 cm/frame**; **root turn 37 deg/frame** *(excluded)* |
| `scott_1_4_4_t580-585` | A | 2_scott_1_4_4 579.7–585.0 s | 5.5 / 2.4 | 32 / 12 | **foot held 33 mm off the floor (median)** *(excluded)* |
| `scott_1_4_4_t62-66_shift` | B | 2_scott_1_4_4 62.0–66.0 s | 24.5 / 14.1 | 22 / 11 | shoulder at limit 17%; outlier knee max (z +7.6); **joint jump 1.31 rad (Left_Shoulder_Pitch at 3.0 s)**; **root jump 3.4 cm/frame**; **root turn 33 deg/frame**; **left arm behind body 11 cm (human's in front)** *(excluded)* |
| `scott_1_4_4_t81-86` | A | 2_scott_1_4_4 81.4–86.4 s | 4.3 / 6.3 | 15 / 6 | **ground IK failed 5 frames** *(excluded)* |
| `scott_1_5_5_t379-386` | A | 2_scott_1_5_5 379.2–385.6 s | 1.1 / 1.9 | 27 / 10 | upper-arm twist at limit 32%; **root turn 7 deg/frame** *(excluded)* |
| `scott_1_6_6_t165-170_shift` | B | 2_scott_1_6_6 164.9–169.6 s | 21.2 / 14.8 | 71 / 22 | trunk drop 5 cm; outlier arms k1 cm (z +4.3); **outlier trunk drop (z +5.3)**; outlier knee max (z +6.1) *(excluded)* |
| `scott_1_6_6_t286-293_shift` | B | 2_scott_1_6_6 285.6–293.3 s | 24.1 / 15.7 | 34 / 10 | shoulder at limit 16%; outlier knee max (z +5.9); **excluded in the spec (fails in training)** *(excluded)* |
| `scott_1_6_6_t53-57_shift` | B | 2_scott_1_6_6 52.9–57.3 s | 22.4 / 29.4 | 40 / 15 | K1 feet move 29 cm; knee 68 deg; head at limit 100%; shoulder at limit 100%; leg at limit 100%; **ground IK failed 132 frames**; outlier trunk drop (z +5.1); outlier knee max (z +10.6); **root turn 7 deg/frame**; **trunk leans 136 deg (median)**; **self-collision right_shank_collision / trunk_collision 4.4 s (at 0.0 s, 94 mm)**; **foot held 164 mm off the floor (median)**; hand presses into leg 39 mm for 1.8 s (at 1.9 s); left arm behind body 9 cm (human's in front); **right arm behind body 16 cm (human's in front)** *(excluded)* |
| `scott_1_6_6_t545-549_shift` | B | 2_scott_1_6_6 544.6–548.7 s | 12.2 / 14.7 | 22 / 8 | upper-arm twist at limit 46%; outlier knee max (z +3.7); **root turn 6 deg/frame** *(excluded)* |
| `scott_1_7_7_t77-81_shift` | B | 2_scott_1_7_7 76.8–80.9 s | 20.5 / 15.9 | 44 / 19 | knee 88 deg; head at limit 100%; shoulder at limit 100%; **upper-arm twist at limit 78%**; leg at limit 100%; **ground IK failed 122 frames**; outlier trunk drop (z +4.0); outlier knee max (z +17.2); **root turn 8 deg/frame**; **trunk leans 60 deg (median)**; self-collision left_foot_collision / left_hand_end_collision 0.2 s (at 2.5 s, 23 mm); **foot held 60 mm off the floor (median)**; hand presses into leg 57 mm for 1.1 s (at 1.9 s); right arm behind body 6 cm (human's in front) *(excluded)* |
| `scott_1_7_7_t86-94_shift` | B | 2_scott_1_7_7 85.5–93.6 s | 19.6 / 10.1 | 61 / 19 | shoulder at limit 22%; outlier knee max (z +3.5); **joint jump 1.92 rad (Left_Shoulder_Pitch at 1.8 s)**; **root turn 24 deg/frame** *(excluded)* |
| `solomon_0_106_106_t14-28` | A | 3_solomon_0_106_106 14.3–28.5 s | 4.7 / 2.3 | 27 / 8 | outlier knee max (z +5.5); **foot held 38 mm off the floor (median)** *(excluded)* |
| `solomon_0_106_106_t28-43` | A | 3_solomon_0_106_106 28.5–42.6 s | 0.8 / 0.9 | 33 / 7 | outlier knee max (z +4.5); **foot held 49 mm off the floor (median)** *(excluded)* |
| `solomon_0_118_118_t0-4` | A | 3_solomon_0_118_118 0.0–4.5 s | 1.3 / 0.4 | 36 / 11 | **foot held 37 mm off the floor (median)** *(excluded)* |
| `solomon_0_11_11_t7-17_shift` | B | 3_solomon_0_11_11 7.4–16.6 s | 18.6 / 12.1 | 58 / 19 | upper-arm twist at limit 8%; **joint jump 0.97 rad (Right_Shoulder_Pitch at 2.3 s)**; **root turn 17 deg/frame** *(excluded)* |
| `solomon_0_12_12_t47-57_shift` | B | 3_solomon_0_12_12 47.3–57.4 s | 21.8 / 15.6 | 47 / 16 | upper-arm twist at limit 9%; **joint jump 0.67 rad (Left_Elbow_Pitch at 9.2 s)**; **root turn 9 deg/frame** *(excluded)* |
| `solomon_0_12_12_t58-77_shift` | B | 3_solomon_0_12_12 58.3–77.2 s | 23.2 / 16.5 | 44 / 14 | upper-arm twist at limit 44%; outlier knee max (z +4.1); **foot held 43 mm off the floor (median)**; hand presses into leg 29 mm for 0.1 s (at 12.9 s) *(excluded)* |
| `solomon_0_13_13_t18-29_shift` | B | 3_solomon_0_13_13 18.0–29.1 s | 20.6 / 12.4 | 53 / 17 | **upper-arm twist at limit 73%**; elbow bend at limit 6%; leg at limit 21%; **ground IK failed 60 frames** *(excluded)* |
| `solomon_0_13_13_t44-48_shift` | B | 3_solomon_0_13_13 44.3–48.4 s | 23.4 / 12.6 | 75 / 23 | upper-arm twist at limit 46%; outlier arms k1 cm (z +4.3); **joint jump 1.06 rad (Left_Elbow_Pitch at 2.5 s)**; **root turn 17 deg/frame** *(excluded)* |
| `solomon_0_14_14_t43-47_shift` | B | 3_solomon_0_14_14 43.0–47.5 s | 15.8 / 8.3 | 25 / 10 | **foot held 33 mm off the floor (median)** *(excluded)* |
| `solomon_0_15_15_t22-32` | A | 3_solomon_0_15_15 21.6–32.2 s | 8.4 / 6.1 | 58 / 18 | head at limit 5%; shoulder at limit 15%; **joint jump 0.93 rad (Right_Elbow_Pitch at 9.1 s)**; **root turn 16 deg/frame** *(excluded)* |
| `solomon_0_15_15_t78-83_shift` | B | 3_solomon_0_15_15 77.8–82.8 s | 19.9 / 7.3 | 63 / 21 | upper-arm twist at limit 46%; elbow bend at limit 5%; leg at limit 15%; **ground IK failed 12 frames**; outlier arms k1 cm (z +3.8); **joint jump 0.90 rad (Right_Shoulder_Pitch at 4.7 s)**; **root jump 3.2 cm/frame**; **root turn 30 deg/frame** *(excluded)* |
| `solomon_0_17_17_t0-9_shift` | B | 3_solomon_0_17_17 0.0–9.0 s | 12.5 / 7.6 | 16 / 5 | shoulder at limit 14%; **joint jump 1.34 rad (Left_Shoulder_Pitch at 1.4 s)**; **root turn 29 deg/frame** *(excluded)* |
| `solomon_0_1_1_t0-14_shift` | B | 3_solomon_0_1_1 0.0–13.9 s | 18.9 / 10.9 | 31 / 9 | shoulder at limit 5%; outlier knee max (z +4.5); **joint jump 1.62 rad (Left_Elbow_Pitch at 0.9 s)**; **root turn 28 deg/frame** *(excluded)* |
| `solomon_0_22_22_t7-23` | A | 3_solomon_0_22_22 6.9–22.6 s | 8.6 / 4.2 | 26 / 9 | **upper-arm twist at limit 66%**; leg at limit 13%; **ground IK failed 32 frames**; **joint jump 0.60 rad (Right_Elbow_Pitch at 5.2 s)** *(excluded)* |
| `solomon_0_23_23_t17-30_shift` | B | 3_solomon_0_23_23 17.2–30.0 s | 22.4 / 14.1 | 55 / 15 | upper-arm twist at limit 44%; outlier knee max (z +4.4); **foot held 37 mm off the floor (median)**; **excluded in the spec (fails in training)** *(excluded)* |
| `solomon_0_25_25_t29-40` | A | 3_solomon_0_25_25 28.9–40.2 s | 7.2 / 4.3 | 61 / 17 | shoulder at limit 27%; **joint jump 2.35 rad (Left_Shoulder_Roll at 2.6 s)**; **root jump 3.1 cm/frame**; **root turn 12 deg/frame** *(excluded)* |
| `solomon_0_25_25_t78-82_shift` | B | 3_solomon_0_25_25 77.9–82.4 s | 9.4 / 6.9 | 69 / 18 | **upper-arm twist at limit 58%**; elbow bend at limit 5%; leg at limit 6% *(excluded)* |
| `solomon_0_2_2_t0-18_shift` | B | 3_solomon_0_2_2 0.0–17.5 s | 19.6 / 11.9 | 34 / 8 | shoulder at limit 13%; outlier knee max (z +4.2); **joint jump 1.46 rad (Left_Shoulder_Pitch at 2.6 s)**; **root turn 36 deg/frame** *(excluded)* |
| `solomon_0_32_32_t68-78_shift` | B | 3_solomon_0_32_32 67.7–78.2 s | 17.3 / 12.0 | 55 / 16 | upper-arm twist at limit 11%; leg at limit 7%; **ground IK failed 20 frames**; **joint jump 0.73 rad (Right_Elbow_Pitch at 9.3 s)** *(excluded)* |
| `solomon_0_38_38_t34-49` | A | 3_solomon_0_38_38 33.7–49.5 s | 9.1 / 5.7 | 47 / 15 | upper-arm twist at limit 46%; **joint jump 0.93 rad (Right_Shoulder_Pitch at 9.3 s)**; **root turn 12 deg/frame**; **foot held 35 mm off the floor (median)** *(excluded)* |
| `solomon_0_3_3_t0-5_shift` | B | 3_solomon_0_3_3 0.0–5.0 s | 19.7 / 11.7 | 24 / 7 | shoulder at limit 52%; **joint jump 2.30 rad (Left_Elbow_Pitch at 3.0 s)**; **root turn 22 deg/frame**; left arm behind body 9 cm (human's in front) *(excluded)* |
| `solomon_0_47_47_t31-46` | A | 3_solomon_0_47_47 30.7–46.0 s | 1.5 / 1.1 | 37 / 11 | **joint jump 0.66 rad (Right_Shoulder_Pitch at 7.3 s)** *(excluded)* |
| `solomon_0_56_56_t15-30` | A | 3_solomon_0_56_56 14.8–29.6 s | 1.0 / 1.9 | 37 / 11 | **excluded in the spec (fails in training)** *(excluded)* |
| `solomon_0_56_56_t28-32_shift` | B | 3_solomon_0_56_56 27.6–32.1 s | 8.3 / 6.2 | 55 / 15 | shoulder at limit 14%; **upper-arm twist at limit 69%**; leg at limit 8% *(excluded)* |
| `solomon_0_57_57_t30-41` | A | 3_solomon_0_57_57 29.9–40.8 s | 7.6 / 5.6 | 56 / 17 | upper-arm twist at limit 12%; **ground IK failed 9 frames**; **joint jump 1.00 rad (Left_Elbow_Pitch at 3.3 s)**; **root turn 13 deg/frame** *(excluded)* |
| `solomon_0_57_57_t5-17` | A | 3_solomon_0_57_57 4.7–17.3 s | 8.4 / 5.4 | 38 / 13 | **upper-arm twist at limit 66%**; elbow bend at limit 14%; leg at limit 20%; **ground IK failed 66 frames**; **joint jump 0.60 rad (Left_Knee_Pitch at 6.7 s)** *(excluded)* |
| `solomon_0_57_57_t55-60_shift` | B | 3_solomon_0_57_57 54.5–59.8 s | 10.9 / 8.0 | 63 / 15 | **upper-arm twist at limit 56%**; leg at limit 13%; **ground IK failed 16 frames** *(excluded)* |
| `solomon_0_60_60_t0-10` | A | 3_solomon_0_60_60 0.0–10.5 s | 5.4 / 3.4 | 61 / 17 | **joint jump 0.80 rad (Left_Shoulder_Pitch at 2.5 s)**; **root turn 13 deg/frame** *(excluded)* |
| `solomon_0_61_61_t17-34` | A | 3_solomon_0_61_61 17.0–34.0 s | 3.9 / 2.5 | 34 / 10 | upper-arm twist at limit 50%; leg at limit 8%; **ground IK failed 21 frames** *(excluded)* |
| `solomon_1_10_10_t430-436_shift` | B | 3_solomon_1_10_10 430.3–435.6 s | 15.0 / 8.2 | 40 / 11 | **ground IK failed 2 frames**; outlier trunk drop (z +3.8); **joint jump 0.72 rad (Left_Ankle_Pitch at 4.2 s)**; **root jump 17.0 cm/frame**; **root turn 13 deg/frame** *(excluded)* |
| `solomon_1_11_11_t104-112_shift` | B | 3_solomon_1_11_11 104.4–111.6 s | 24.5 / 26.2 | 20 / 7 | K1 feet move 26 cm; trunk drop 27 cm; knee 126 deg; leg at limit 90%; **ground IK failed 169 frames**; **outlier trunk drop (z +35.6)**; outlier knee max (z +30.0); **joint jump 1.10 rad (Right_Hip_Pitch at 3.4 s)**; **root jump 42.7 cm/frame**; **root turn 29 deg/frame**; **self-collision left_shank_lower_collision / right_shank_lower_collision 1.5 s (at 3.8 s, 68 mm)**; **feet overlap 72 mm for 0.2 s (at 0.9 s)**; **foot held 252 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t116-125_shift` | B | 3_solomon_1_11_11 115.9–124.8 s | 24.9 / 29.3 | 14 / 5 | K1 feet move 29 cm; trunk drop 30 cm; knee 103 deg; leg at limit 95%; **ground IK failed 234 frames**; **outlier trunk drop (z +40.0)**; outlier knee max (z +22.3); **joint jump 1.85 rad (Right_Hip_Yaw at 4.1 s)**; **root jump 34.9 cm/frame**; **root turn 27 deg/frame**; **self-collision left_shank_collision / right_shank_lower_collision 2.2 s (at 4.2 s, 75 mm)**; **foot held 390 mm off the floor (median)**; hand presses into leg 17 mm for 2.2 s (at 0.6 s) *(excluded)* |
| `solomon_1_11_11_t119-124` | A | 3_solomon_1_11_11 119.2–123.6 s | 8.4 / 28.4 | 12 / 5 | K1 feet move 28 cm; trunk drop 20 cm; knee 98 deg; leg at limit 91%; **ground IK failed 102 frames**; **outlier trunk drop (z +25.7)**; outlier knee max (z +20.8); **joint jump 1.18 rad (Right_Ankle_Pitch at 0.8 s)**; **root jump 33.2 cm/frame**; **root turn 16 deg/frame**; **self-collision left_shank_collision / right_shank_lower_collision 2.6 s (at 0.9 s, 67 mm)**; **feet overlap 78 mm for 0.2 s (at 0.1 s)**; **foot held 276 mm off the floor (median)**; hand presses into leg 59 mm for 0.2 s (at 0.3 s) *(excluded)* |
| `solomon_1_11_11_t125-130_shift` | B | 3_solomon_1_11_11 125.5–129.8 s | 9.9 / 15.8 | 29 / 9 | trunk drop 24 cm; leg at limit 67%; **ground IK failed 64 frames**; **outlier trunk drop (z +31.7)**; outlier knee max (z +5.6); **joint jump 0.70 rad (Right_Hip_Roll at 2.5 s)**; **root jump 17.9 cm/frame**; **root turn 13 deg/frame**; **self-collision left_foot_collision / right_foot_collision 0.8 s (at 1.7 s, 64 mm)**; **feet overlap 64 mm for 0.8 s (at 1.7 s)**; **foot held 230 mm off the floor (median)**; hand presses into leg 52 mm for 1.2 s (at 2.5 s) *(excluded)* |
| `solomon_1_11_11_t214-219_shift` | B | 3_solomon_1_11_11 214.4–219.0 s | 14.2 / 14.4 | 16 / 3 | trunk drop 7 cm; leg at limit 100%; **ground IK failed 139 frames**; **outlier trunk drop (z +8.6)**; outlier knee max (z -10.1); **trunk leans 16 deg (median)**; **foot held 426 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t227-234_shift` | B | 3_solomon_1_11_11 226.9–234.2 s | 16.1 / 12.1 | 27 / 8 | trunk drop 10 cm; leg at limit 100%; **ground IK failed 217 frames**; **outlier trunk drop (z +12.4)**; outlier knee max (z -5.2); **root jump 4.7 cm/frame**; **trunk leans 18 deg (median)**; **foot held 429 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t229-233` | A | 3_solomon_1_11_11 228.5–233.1 s | 2.3 / 3.2 | 25 / 8 | trunk drop 6 cm; leg at limit 100%; **ground IK failed 138 frames**; **outlier trunk drop (z +6.1)**; outlier knee max (z -7.7); **root jump 3.0 cm/frame**; **trunk leans 20 deg (median)**; **foot held 405 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t286-291_shift` | B | 3_solomon_1_11_11 286.0–290.8 s | 22.2 / 14.4 | 23 / 4 | trunk drop 8 cm; leg at limit 100%; **ground IK failed 143 frames**; **outlier trunk drop (z +9.0)**; outlier knee max (z -10.3); **trunk leans 16 deg (median)**; **foot held 407 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t299-306_shift` | B | 3_solomon_1_11_11 298.6–306.4 s | 23.1 / 27.8 | 18 / 4 | K1 feet move 28 cm; trunk drop 8 cm; leg at limit 100%; **ground IK failed 233 frames**; **outlier trunk drop (z +10.0)**; outlier knee max (z -7.7); **foot held 406 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t311-316_shift` | B | 3_solomon_1_11_11 311.4–316.3 s | 19.8 / 12.4 | 27 / 7 | trunk drop 9 cm; leg at limit 100%; **ground IK failed 148 frames**; **outlier trunk drop (z +11.0)**; outlier knee max (z -5.6); **root jump 7.3 cm/frame**; **root turn 10 deg/frame**; **trunk leans 15 deg (median)**; **foot held 429 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t385-393_shift` | B | 3_solomon_1_11_11 384.9–393.3 s | 15.7 / 25.3 | 12 / 4 | K1 feet move 25 cm; trunk drop 16 cm; leg at limit 99%; **ground IK failed 227 frames**; **outlier trunk drop (z +20.5)**; outlier knee max (z +6.7); **joint jump 1.01 rad (Right_Ankle_Pitch at 7.5 s)**; **root jump 18.7 cm/frame**; **root turn 16 deg/frame**; **self-collision left_shank_collision / right_shank_collision 1.9 s (at 5.4 s, 33 mm)**; **foot held 159 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t430-437` | A | 3_solomon_1_11_11 430.3–437.2 s | 8.4 / 6.8 | 22 / 5 | leg at limit 20%; **ground IK failed 54 frames**; **self-collision left_foot_collision / right_foot_collision 0.5 s (at 0.0 s, 30 mm)**; **feet overlap 30 mm for 0.5 s (at 0.0 s)** *(excluded)* |
| `solomon_1_11_11_t435-442_shift` | B | 3_solomon_1_11_11 435.2–441.8 s | 22.2 / 15.2 | 19 / 4 | leg at limit 72%; **ground IK failed 143 frames**; outlier knee max (z +5.2); **joint jump 1.00 rad (Right_Ankle_Pitch at 2.1 s)** *(excluded)* |
| `solomon_1_11_11_t446-452_shift` | B | 3_solomon_1_11_11 446.5–452.5 s | 23.2 / 18.9 | 26 / 5 | K1 feet move 19 cm; trunk drop 8 cm; leg at limit 100%; **ground IK failed 179 frames**; **outlier trunk drop (z +9.2)**; outlier knee max (z -3.7); **foot held 69 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t469-475_shift` | B | 3_solomon_1_11_11 468.9–475.2 s | 24.1 / 30.3 | 19 / 5 | K1 feet move 30 cm; trunk drop 20 cm; leg at limit 98%; **ground IK failed 182 frames**; **outlier trunk drop (z +25.5)**; outlier knee max (z +7.7); **joint jump 1.43 rad (Right_Hip_Roll at 5.8 s)**; **root jump 37.3 cm/frame**; **root turn 26 deg/frame**; **trunk leans 16 deg (median)**; **self-collision left_shank_collision / right_shank_lower_collision 0.3 s (at 5.9 s, 67 mm)**; **foot held 363 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t473-478` | A | 3_solomon_1_11_11 473.2–478.3 s | 6.1 / 26.0 | 21 / 6 | K1 feet move 26 cm; trunk drop 20 cm; knee 66 deg; leg at limit 96%; **ground IK failed 145 frames**; **outlier trunk drop (z +25.4)**; outlier knee max (z +9.9); **joint jump 1.44 rad (Right_Hip_Roll at 1.5 s)**; **root jump 37.3 cm/frame**; **root turn 28 deg/frame**; **self-collision left_shank_collision / right_shank_lower_collision 1.1 s (at 1.7 s, 70 mm)**; **foot held 254 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t490-494` | A | 3_solomon_1_11_11 489.6–494.2 s | 1.2 / 3.0 | 8 / 2 | leg at limit 100%; **ground IK failed 138 frames**; outlier trunk drop (z +4.8); outlier knee max (z -12.0); **foot held 405 mm off the floor (median)** *(excluded)* |
| `solomon_1_11_11_t519-525_shift` | B | 3_solomon_1_11_11 518.5–524.7 s | 22.6 / 10.6 | 15 / 3 | trunk drop 7 cm; knee 75 deg; leg at limit 82%; **ground IK failed 145 frames**; **outlier trunk drop (z +8.2)**; outlier knee max (z +13.0); **self-collision left_shank_collision / right_shank_lower_collision 6.2 s (at 0.0 s, 72 mm)**; **foot held 117 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t117-122` | A | 3_solomon_1_12_12 116.7–122.1 s | 8.1 / 28.5 | 19 / 4 | K1 feet move 28 cm; trunk drop 18 cm; knee 70 deg; leg at limit 100%; **ground IK failed 158 frames**; **outlier trunk drop (z +23.2)**; outlier knee max (z +11.3); **joint jump 1.38 rad (Right_Hip_Roll at 4.9 s)**; **root jump 42.6 cm/frame**; **root turn 21 deg/frame**; **trunk leans 17 deg (median)**; **self-collision left_shank_collision / right_shank_lower_collision 0.4 s (at 5.1 s, 56 mm)**; **foot held 378 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t183-191_shift` | B | 3_solomon_1_12_12 183.3–190.7 s | 17.4 / 27.0 | 22 / 5 | K1 feet move 27 cm; trunk drop 8 cm; leg at limit 100%; **ground IK failed 220 frames**; **outlier trunk drop (z +9.7)**; outlier knee max (z -7.6); **foot held 381 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t210-216_shift` | B | 3_solomon_1_12_12 210.2–215.7 s | 12.6 / 11.1 | 18 / 4 | trunk drop 8 cm; leg at limit 100%; **ground IK failed 165 frames**; **outlier trunk drop (z +9.4)**; outlier knee max (z -5.6); **trunk leans 17 deg (median)**; **foot held 433 mm off the floor (median)**; hand presses into leg 7 mm for 0.3 s (at 3.7 s) *(excluded)* |
| `solomon_1_12_12_t228-235` | A | 3_solomon_1_12_12 228.1–234.7 s | 4.6 / 5.1 | 22 / 4 | trunk drop 6 cm; leg at limit 100%; **ground IK failed 196 frames**; **outlier trunk drop (z +6.6)**; outlier knee max (z -12.0); **trunk leans 15 deg (median)**; **foot held 375 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t239-246` | A | 3_solomon_1_12_12 239.4–246.1 s | 2.9 / 4.7 | 18 / 4 | leg at limit 100%; **ground IK failed 203 frames**; outlier trunk drop (z +5.2); outlier knee max (z -11.9); **root jump 3.5 cm/frame**; **foot held 351 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t274-278_shift` | B | 3_solomon_1_12_12 274.2–278.2 s | 15.2 / 16.5 | 23 / 7 | trunk drop 11 cm; leg at limit 100%; **ground IK failed 120 frames**; **outlier trunk drop (z +13.0)**; **root jump 12.0 cm/frame**; **root turn 8 deg/frame**; **foot held 399 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t276-292` | A | 3_solomon_1_12_12 275.5–292.1 s | 4.6 / 17.9 | 20 / 6 | K1 feet move 18 cm; trunk drop 10 cm; leg at limit 100%; **ground IK failed 496 frames**; **outlier trunk drop (z +12.7)**; **joint jump 0.70 rad (Left_Ankle_Pitch at 5.2 s)**; **root jump 12.6 cm/frame**; **root turn 9 deg/frame**; **foot held 407 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t327-331_shift` | B | 3_solomon_1_12_12 326.7–330.7 s | 9.9 / 18.6 | 39 / 6 | K1 feet move 19 cm; trunk drop 8 cm; leg at limit 100%; **ground IK failed 120 frames**; **outlier trunk drop (z +9.5)**; **root jump 5.5 cm/frame**; **root turn 6 deg/frame**; **foot held 420 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t332-338_shift` | B | 3_solomon_1_12_12 331.7–338.5 s | 21.5 / 18.9 | 32 / 6 | K1 feet move 19 cm; trunk drop 8 cm; leg at limit 100%; **ground IK failed 202 frames**; **outlier trunk drop (z +9.7)**; outlier knee max (z -4.8); **root jump 3.9 cm/frame**; **trunk leans 19 deg (median)**; **foot held 447 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t336-354` | A | 3_solomon_1_12_12 336.5–354.2 s | 6.3 / 7.8 | 11 / 3 | trunk drop 7 cm; leg at limit 100%; **ground IK failed 531 frames**; **outlier trunk drop (z +8.3)**; outlier knee max (z -9.5); **root jump 3.7 cm/frame**; **trunk leans 17 deg (median)**; **foot held 420 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t354-372` | A | 3_solomon_1_12_12 354.2–371.9 s | 6.2 / 5.0 | 16 / 4 | trunk drop 8 cm; leg at limit 100%; **ground IK failed 530 frames**; **outlier trunk drop (z +8.9)**; outlier knee max (z -9.7); **root jump 4.8 cm/frame**; **foot held 409 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t37-41_shift` | B | 3_solomon_1_12_12 37.3–41.3 s | 17.5 / 30.6 | 23 / 7 | K1 feet move 31 cm; trunk drop 23 cm; knee 112 deg; leg at limit 99%; **ground IK failed 118 frames**; **outlier trunk drop (z +29.7)**; outlier knee max (z +25.3); **joint jump 1.57 rad (Right_Hip_Roll at 3.7 s)**; **root jump 40.8 cm/frame**; **root turn 21 deg/frame**; **trunk leans 15 deg (median)**; **foot held 432 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t372-390` | A | 3_solomon_1_12_12 371.9–389.5 s | 8.1 / 8.0 | 25 / 6 | trunk drop 11 cm; leg at limit 100%; **ground IK failed 529 frames**; **outlier trunk drop (z +13.3)**; outlier knee max (z -7.1); **root jump 7.9 cm/frame**; **root turn 12 deg/frame**; **trunk leans 16 deg (median)**; **foot held 432 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t39-48` | A | 3_solomon_1_12_12 38.6–48.3 s | 8.6 / 24.5 | 14 / 4 | K1 feet move 25 cm; trunk drop 21 cm; knee 128 deg; leg at limit 100%; **ground IK failed 281 frames**; **outlier trunk drop (z +27.3)**; outlier knee max (z +30.6); **joint jump 1.57 rad (Right_Hip_Roll at 2.4 s)**; **root jump 40.8 cm/frame**; **root turn 21 deg/frame**; **trunk leans 17 deg (median)**; **foot held 396 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t390-407` | A | 3_solomon_1_12_12 389.5–407.2 s | 8.2 / 6.8 | 24 / 6 | trunk drop 12 cm; leg at limit 100%; **ground IK failed 530 frames**; **outlier trunk drop (z +15.0)**; outlier knee max (z -6.8); **root jump 6.7 cm/frame**; **root turn 9 deg/frame**; **trunk leans 16 deg (median)**; **foot held 446 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t407-425` | A | 3_solomon_1_12_12 407.2–424.9 s | 12.8 / 10.7 | 20 / 5 | human steps; K1 feet move 11 cm; trunk drop 13 cm; leg at limit 100%; **ground IK failed 530 frames**; **outlier trunk drop (z +16.3)**; **root jump 7.1 cm/frame**; **root turn 12 deg/frame**; **trunk leans 18 deg (median)**; **foot held 459 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t425-443` | A | 3_solomon_1_12_12 424.9–442.6 s | 5.2 / 4.7 | 14 / 4 | trunk drop 6 cm; leg at limit 100%; **ground IK failed 530 frames**; **outlier trunk drop (z +6.7)**; outlier knee max (z -11.0); **trunk leans 15 deg (median)**; **foot held 432 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t441-445_shift` | B | 3_solomon_1_12_12 440.6–445.5 s | 16.3 / 9.9 | 8 / 3 | trunk drop 6 cm; leg at limit 100%; **ground IK failed 145 frames**; **outlier trunk drop (z +6.9)**; outlier knee max (z -4.7); **joint jump 0.75 rad (Left_Ankle_Pitch at 2.5 s)**; **root jump 6.8 cm/frame**; **root turn 8 deg/frame**; **foot held 428 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t443-455` | A | 3_solomon_1_12_12 443.5–454.7 s | 9.9 / 4.0 | 9 / 2 | trunk drop 7 cm; leg at limit 100%; **ground IK failed 336 frames**; **outlier trunk drop (z +8.5)**; outlier knee max (z -4.0); **foot held 423 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t453-457_shift` | B | 3_solomon_1_12_12 452.7–457.4 s | 15.8 / 14.3 | 26 / 5 | trunk drop 9 cm; leg at limit 100%; **ground IK failed 142 frames**; **outlier trunk drop (z +10.8)**; outlier knee max (z -4.0); **foot held 436 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t455-474` | A | 3_solomon_1_12_12 455.4–474.2 s | 3.6 / 7.5 | 18 / 4 | trunk drop 7 cm; leg at limit 100%; **ground IK failed 563 frames**; **outlier trunk drop (z +8.7)**; outlier knee max (z -9.1); **trunk leans 16 deg (median)**; **foot held 426 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t46-52_shift` | B | 3_solomon_1_12_12 46.3–52.4 s | 26.2 / 21.8 | 14 / 4 | human steps; K1 feet move 22 cm; trunk drop 24 cm; leg at limit 100%; **ground IK failed 184 frames**; **outlier trunk drop (z +31.2)**; outlier knee max (z -7.7); **joint jump 0.60 rad (Right_Hip_Roll at 3.3 s)**; **root jump 13.1 cm/frame**; **root turn 9 deg/frame**; **trunk leans 17 deg (median)**; **foot held 405 mm off the floor (median)**; hand presses into leg 15 mm for 0.5 s (at 3.8 s) *(excluded)* |
| `solomon_1_12_12_t474-493` | A | 3_solomon_1_12_12 474.2–492.9 s | 5.9 / 4.8 | 17 / 4 | trunk drop 11 cm; leg at limit 100%; **ground IK failed 560 frames**; **outlier trunk drop (z +13.0)**; **root jump 11.0 cm/frame**; **root turn 14 deg/frame**; **trunk leans 17 deg (median)**; **foot held 439 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t491-495_shift` | B | 3_solomon_1_12_12 490.9–495.4 s | 7.9 / 7.4 | 4 / 2 | trunk drop 7 cm; leg at limit 100%; **ground IK failed 134 frames**; **outlier trunk drop (z +7.8)**; outlier knee max (z -9.5); **trunk leans 16 deg (median)**; **foot held 435 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t493-500` | A | 3_solomon_1_12_12 493.4–499.8 s | 5.6 / 14.6 | 12 / 3 | K1 feet move 15 cm; trunk drop 10 cm; leg at limit 100%; **ground IK failed 193 frames**; **outlier trunk drop (z +12.7)**; **root jump 7.0 cm/frame**; **root turn 7 deg/frame**; **foot held 432 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t498-508_shift` | B | 3_solomon_1_12_12 497.8–508.0 s | 19.4 / 14.6 | 9 / 2 | trunk drop 8 cm; leg at limit 100%; **ground IK failed 305 frames**; **outlier trunk drop (z +9.7)**; outlier knee max (z -7.1); **trunk leans 15 deg (median)**; **foot held 427 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t508-518_shift` | B | 3_solomon_1_12_12 508.0–518.2 s | 26.9 / 20.0 | 22 / 4 | human steps; K1 feet move 20 cm; trunk drop 10 cm; leg at limit 100%; **ground IK failed 305 frames**; **outlier trunk drop (z +12.3)**; outlier knee max (z -6.5); **root jump 6.1 cm/frame**; **root turn 7 deg/frame**; **trunk leans 17 deg (median)**; **foot held 422 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t53-63` | A | 3_solomon_1_12_12 53.1–62.6 s | 2.3 / 28.9 | 30 / 7 | K1 feet move 29 cm; trunk drop 26 cm; knee 67 deg; leg at limit 99%; **ground IK failed 282 frames**; **outlier trunk drop (z +34.3)**; outlier knee max (z +10.5); **joint jump 1.15 rad (Right_Hip_Roll at 1.2 s)**; **root jump 32.6 cm/frame**; **root turn 24 deg/frame**; **self-collision left_shank_collision / right_shank_lower_collision 5.3 s (at 4.2 s, 66 mm)**; **foot held 301 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t531-537` | A | 3_solomon_1_12_12 531.2–537.2 s | 4.2 / 14.5 | 20 / 6 | K1 feet move 14 cm; trunk drop 10 cm; leg at limit 100%; **ground IK failed 180 frames**; **outlier trunk drop (z +12.3)**; **root jump 6.1 cm/frame**; **root turn 7 deg/frame**; **foot held 436 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t535-542_shift` | B | 3_solomon_1_12_12 535.2–541.6 s | 17.5 / 25.4 | 25 / 6 | K1 feet move 25 cm; trunk drop 9 cm; leg at limit 100%; **ground IK failed 190 frames**; **outlier trunk drop (z +10.4)**; **root jump 6.1 cm/frame**; **root turn 7 deg/frame**; **foot held 420 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t540-544` | A | 3_solomon_1_12_12 539.6–544.5 s | 3.3 / 3.9 | 33 / 7 | trunk drop 6 cm; leg at limit 100%; **ground IK failed 147 frames**; **outlier trunk drop (z +6.8)**; outlier knee max (z -9.2); **trunk leans 17 deg (median)**; **foot held 431 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t542-556_shift` | B | 3_solomon_1_12_12 542.5–555.7 s | 16.2 / 10.8 | 19 / 5 | trunk drop 12 cm; leg at limit 100%; **ground IK failed 396 frames**; **outlier trunk drop (z +14.4)**; **root jump 12.5 cm/frame**; **root turn 9 deg/frame**; **trunk leans 17 deg (median)**; **foot held 434 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t556-569_shift` | B | 3_solomon_1_12_12 555.7–568.8 s | 10.2 / 7.3 | 12 / 3 | trunk drop 9 cm; leg at limit 100%; **ground IK failed 392 frames**; **outlier trunk drop (z +11.4)**; outlier knee max (z -6.5); **root jump 7.3 cm/frame**; **root turn 11 deg/frame**; **trunk leans 18 deg (median)**; **foot held 447 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t567-578` | A | 3_solomon_1_12_12 566.8–578.5 s | 3.0 / 4.3 | 13 / 4 | trunk drop 6 cm; leg at limit 100%; **ground IK failed 350 frames**; **outlier trunk drop (z +7.2)**; outlier knee max (z -11.2); **root jump 6.3 cm/frame**; **root turn 7 deg/frame**; **trunk leans 19 deg (median)**; **foot held 418 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t578-590` | A | 3_solomon_1_12_12 578.5–590.2 s | 6.4 / 17.9 | 19 / 5 | K1 feet move 18 cm; trunk drop 25 cm; leg at limit 100%; **ground IK failed 349 frames**; **outlier trunk drop (z +32.9)**; **joint jump 1.34 rad (Right_Hip_Roll at 1.1 s)**; **root jump 39.2 cm/frame**; **root turn 21 deg/frame**; **trunk leans 15 deg (median)**; **foot held 437 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t588-593_shift` | B | 3_solomon_1_12_12 588.2–592.9 s | 6.7 / 4.4 | 23 / 5 | trunk drop 7 cm; leg at limit 100%; **ground IK failed 142 frames**; **outlier trunk drop (z +8.0)**; outlier knee max (z -8.0); **trunk leans 18 deg (median)**; **foot held 458 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t597-601_shift` | B | 3_solomon_1_12_12 596.6–600.6 s | 21.7 / 12.5 | 23 / 4 | trunk drop 7 cm; leg at limit 100%; **ground IK failed 120 frames**; **outlier trunk drop (z +8.3)**; outlier knee max (z -9.4); **foot held 435 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t598-603` | A | 3_solomon_1_12_12 597.9–602.7 s | 3.2 / 3.7 | 18 / 5 | trunk drop 6 cm; leg at limit 100%; **ground IK failed 144 frames**; **outlier trunk drop (z +6.3)**; outlier knee max (z -11.8); **root jump 5.3 cm/frame**; **foot held 410 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t601-611_shift` | B | 3_solomon_1_12_12 600.7–610.8 s | 18.3 / 13.0 | 35 / 9 | trunk drop 10 cm; leg at limit 100%; **ground IK failed 301 frames**; **outlier trunk drop (z +12.4)**; **root jump 7.1 cm/frame**; **root turn 10 deg/frame**; **trunk leans 16 deg (median)**; **foot held 451 mm off the floor (median)**; hand presses into leg 14 mm for 0.4 s (at 9.6 s) *(excluded)* |
| `solomon_1_12_12_t63-69_shift` | B | 3_solomon_1_12_12 63.1–68.8 s | 22.7 / 17.1 | 14 / 4 | trunk drop 23 cm; leg at limit 99%; **ground IK failed 167 frames**; **outlier trunk drop (z +31.0)**; **joint jump 1.45 rad (Right_Hip_Roll at 1.1 s)**; **root jump 39.3 cm/frame**; **root turn 17 deg/frame**; **trunk leans 17 deg (median)**; **foot held 421 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t67-74` | A | 3_solomon_1_12_12 66.8–74.0 s | 1.5 / 27.6 | 10 / 3 | K1 feet move 28 cm; trunk drop 18 cm; knee 69 deg; leg at limit 96%; **ground IK failed 201 frames**; **outlier trunk drop (z +24.0)**; outlier knee max (z +11.2); **joint jump 1.41 rad (Right_Hip_Roll at 2.7 s)**; **root jump 37.9 cm/frame**; **root turn 25 deg/frame**; **self-collision left_shank_collision / right_shank_lower_collision 2.5 s (at 4.7 s, 62 mm)**; **foot held 233 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t82-86_shift` | B | 3_solomon_1_12_12 81.6–86.2 s | 13.6 / 28.3 | 15 / 4 | K1 feet move 28 cm; trunk drop 20 cm; knee 78 deg; leg at limit 99%; **ground IK failed 138 frames**; **outlier trunk drop (z +26.5)**; outlier knee max (z +14.1); **joint jump 1.40 rad (Right_Hip_Roll at 3.1 s)**; **root jump 36.9 cm/frame**; **root turn 27 deg/frame**; **self-collision left_shank_collision / right_shank_lower_collision 1.5 s (at 3.1 s, 55 mm)**; **foot held 374 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t84-90` | A | 3_solomon_1_12_12 84.2–89.7 s | 6.7 / 30.4 | 20 / 5 | K1 feet move 30 cm; trunk drop 16 cm; knee 84 deg; leg at limit 99%; **ground IK failed 161 frames**; **outlier trunk drop (z +20.8)**; outlier knee max (z +15.9); **joint jump 1.40 rad (Right_Hip_Roll at 0.4 s)**; **root jump 36.9 cm/frame**; **root turn 27 deg/frame**; **self-collision left_shank_collision / right_shank_lower_collision 5.0 s (at 0.5 s, 58 mm)**; **foot held 238 mm off the floor (median)** *(excluded)* |
| `solomon_1_12_12_t92-98_shift` | B | 3_solomon_1_12_12 92.1–98.2 s | 13.4 / 12.6 | 12 / 4 | trunk drop 10 cm; leg at limit 99%; **ground IK failed 182 frames**; **outlier trunk drop (z +12.7)**; **joint jump 0.63 rad (Right_Hip_Roll at 5.2 s)**; **root jump 12.3 cm/frame**; **root turn 15 deg/frame**; **trunk leans 17 deg (median)**; **foot held 428 mm off the floor (median)** *(excluded)* |
| `solomon_1_3_3_t0-19` | A | 3_solomon_1_3_3 0.0–18.7 s | 1.7 / 1.3 | 10 / 3 | **joint jump 1.22 rad (Left_Shoulder_Pitch at 0.8 s)**; **root jump 3.4 cm/frame**; **root turn 29 deg/frame** *(excluded)* |
| `solomon_1_4_4_t625-633_shift` | B | 3_solomon_1_4_4 625.2–633.5 s | 18.0 / 11.5 | 21 / 6 | trunk drop 6 cm; **outlier trunk drop (z +6.9)** *(excluded)* |
| `solomon_1_6_6_t280-285_shift` | B | 3_solomon_1_6_6 280.4–285.4 s | 22.0 / 16.9 | 7 / 2 | outlier knee max (z +7.2); **self-collision left_foot_collision / right_foot_collision 1.2 s (at 3.8 s, 42 mm)**; **feet overlap 42 mm for 1.2 s (at 3.8 s)** *(excluded)* |
| `solomon_1_6_6_t283-288` | A | 3_solomon_1_6_6 283.4–287.6 s | 5.8 / 8.4 | 6 / 2 | K1 feet move 8 cm; **self-collision left_foot_collision / right_foot_collision 3.4 s (at 0.8 s, 52 mm)**; **feet overlap 52 mm for 3.4 s (at 0.8 s)** *(excluded)* |
| `solomon_1_6_6_t286-291_shift` | B | 3_solomon_1_6_6 285.6–291.4 s | 12.5 / 11.2 | 10 / 4 | **ground IK failed 4 frames**; **self-collision left_foot_collision / right_foot_collision 2.2 s (at 0.0 s, 52 mm)**; **feet overlap 52 mm for 2.2 s (at 0.0 s)** *(excluded)* |
| `solomon_1_7_7_t318-328_shift` | B | 3_solomon_1_7_7 318.2–327.7 s | 19.0 / 12.2 | 11 / 3 | **ground IK failed 5 frames**; outlier knee max (z +5.2); **self-collision left_foot_collision / right_foot_collision 3.4 s (at 1.8 s, 55 mm)**; **feet overlap 55 mm for 3.4 s (at 1.8 s)** *(excluded)* |
| `solomon_1_7_7_t426-432_shift` | B | 3_solomon_1_7_7 425.6–432.1 s | 18.9 / 15.0 | 14 / 4 | outlier knee max (z +4.7); **self-collision left_foot_collision / right_foot_collision 1.6 s (at 0.0 s, 41 mm)**; **feet overlap 41 mm for 1.6 s (at 0.0 s)** *(excluded)* |
| `solomon_1_7_7_t437-441_shift` | B | 3_solomon_1_7_7 437.0–441.3 s | 23.2 / 13.5 | 10 / 3 | **ground IK failed 3 frames**; outlier knee max (z +5.0); **self-collision left_foot_collision / right_foot_collision 2.3 s (at 2.0 s, 56 mm)**; **feet overlap 56 mm for 2.3 s (at 2.0 s)** *(excluded)* |
| `solomon_1_7_7_t439-444` | A | 3_solomon_1_7_7 439.3–443.7 s | 5.2 / 1.6 | 10 / 3 | leg at limit 45%; **ground IK failed 41 frames**; **self-collision left_foot_collision / right_foot_collision 4.4 s (at 0.0 s, 54 mm)**; **feet overlap 54 mm for 4.4 s (at 0.0 s)** *(excluded)* |
| `solomon_1_7_7_t442-448_shift` | B | 3_solomon_1_7_7 441.7–448.0 s | 16.8 / 17.9 | 11 / 4 | outlier knee max (z +4.0); **self-collision left_foot_collision / right_foot_collision 2.2 s (at 0.0 s, 39 mm)**; **feet overlap 39 mm for 2.2 s (at 0.0 s)** *(excluded)* |
| `solomon_1_8_8_t33-43_shift` | B | 3_solomon_1_8_8 33.3–43.1 s | 20.9 / 11.1 | 17 / 4 | **self-collision left_foot_collision / right_foot_collision 0.5 s (at 2.3 s, 48 mm)**; **feet overlap 48 mm for 0.5 s (at 2.3 s)** *(excluded)* |
| `solomon_1_8_8_t541-552_shift` | B | 3_solomon_1_8_8 541.0–551.8 s | 20.3 / 16.2 | 12 / 3 | **ground IK failed 1 frames**; **joint jump 0.62 rad (Left_Knee_Pitch at 6.6 s)**; **self-collision left_foot_collision / right_foot_collision 6.3 s (at 3.7 s, 54 mm)**; **feet overlap 54 mm for 6.3 s (at 3.7 s)** *(excluded)* |
| `solomon_1_8_8_t545-549` | A | 3_solomon_1_8_8 544.9–548.9 s | 8.4 / 5.5 | 13 / 2 | **trunk leans 16 deg (median)**; **self-collision left_foot_collision / right_foot_collision 4.0 s (at 0.0 s, 55 mm)**; **feet overlap 55 mm for 4.0 s (at 0.0 s)** *(excluded)* |
| `solomon_1_8_8_t554-558_shift` | B | 3_solomon_1_8_8 553.5–557.5 s | 11.3 / 7.2 | 12 / 3 | **self-collision left_foot_collision / right_foot_collision 2.4 s (at 0.7 s, 54 mm)**; **feet overlap 54 mm for 2.4 s (at 0.7 s)** *(excluded)* |
| `solomon_1_8_8_t554-559` | A | 3_solomon_1_8_8 554.5–559.2 s | 9.0 / 5.9 | 18 / 3 | **self-collision left_foot_collision / right_foot_collision 2.2 s (at 0.0 s, 49 mm)**; **feet overlap 49 mm for 2.2 s (at 0.0 s)** *(excluded)* |
| `solomon_1_9_9_t567-571_shift` | B | 3_solomon_1_9_9 567.5–571.5 s | 14.7 / 17.4 | 29 / 7 | outlier knee max (z +3.9); **root jump 3.6 cm/frame** *(excluded)* |
| `sophie_0_62_62_t0-6_shift` | B | 7_sophie_0_62_62 0.0–5.9 s | 11.3 / 5.5 | 15 / 4 | head at limit 62%; shoulder at limit 96%; **trunk leans 24 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `sophie_1_10_10_t0-6` | A | 7_sophie_1_10_10 0.0–6.0 s | 1.5 / 2.1 | 19 / 6 | head at limit 96%; shoulder at limit 99%; elbow bend at limit 7%; **joint jump 1.91 rad (Left_Elbow_Pitch at 6.0 s)**; **root jump 4.3 cm/frame**; **root turn 35 deg/frame**; **trunk leans 30 deg (median)**; **foot held 30 mm off the floor (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `sophie_1_10_10_t316-324` | A | 7_sophie_1_10_10 316.0–323.9 s | 1.6 / 1.2 | 9 / 3 | head at limit 10%; **foot held 36 mm off the floor (median)**; right arm behind body 6 cm (human's in front) *(excluded)* |
| `sophie_1_10_10_t403-416` | A | 7_sophie_1_10_10 402.9–416.2 s | 1.2 / 0.9 | 29 / 7 | elbow bend at limit 16%; **root turn 6 deg/frame** *(excluded)* |
| `sophie_1_10_10_t519-525_shift` | B | 7_sophie_1_10_10 519.4–525.3 s | 11.7 / 9.6 | 12 / 4 | knee 65 deg; elbow bend at limit 9%; outlier knee max (z +9.8); **joint jump 1.00 rad (Left_Ankle_Pitch at 3.1 s)** *(excluded)* |
| `sophie_1_10_10_t545-552` | A | 7_sophie_1_10_10 545.1–552.2 s | 1.3 / 1.4 | 23 / 7 | elbow bend at limit 13%; **root turn 7 deg/frame**; right arm behind body 6 cm (human's in front) *(excluded)* |
| `sophie_1_11_11_t28-36_shift` | B | 7_sophie_1_11_11 28.0–36.4 s | 28.9 / 15.8 | 19 / 7 | human steps; elbow bend at limit 23%; outlier knee max (z +7.8); **joint jump 0.71 rad (Right_Elbow_Pitch at 7.1 s)**; **root turn 13 deg/frame** *(excluded)* |
| `sophie_1_12_12_t30-36_shift` | B | 7_sophie_1_12_12 29.8–36.3 s | 18.3 / 15.4 | 18 / 4 | knee 65 deg; elbow bend at limit 7%; leg at limit 6%; **ground IK failed 4 frames**; outlier knee max (z +9.8); **joint jump 1.21 rad (Left_Ankle_Pitch at 3.2 s)** *(excluded)* |
| `sophie_1_1_1_t131-137` | A | 7_sophie_1_1_1 130.9–137.2 s | 8.6 / 1.5 | 19 / 6 | head at limit 15%; leg at limit 6%; **ground IK failed 4 frames** *(excluded)* |
| `sophie_1_1_1_t134-138_shift` | B | 7_sophie_1_1_1 134.0–138.0 s | 8.6 / 1.6 | 18 / 6 | head at limit 24%; leg at limit 30%; **ground IK failed 29 frames** *(excluded)* |
| `sophie_1_1_1_t340-347` | A | 7_sophie_1_1_1 339.6–347.4 s | 6.0 / 1.5 | 12 / 4 | leg at limit 39%; **ground IK failed 81 frames** *(excluded)* |
| `sophie_1_1_1_t345-350_shift` | B | 7_sophie_1_1_1 345.4–350.0 s | 13.5 / 7.2 | 13 / 5 | leg at limit 34%; **ground IK failed 30 frames**; outlier knee max (z +6.4) *(excluded)* |
| `sophie_1_1_1_t433-439_shift` | B | 7_sophie_1_1_1 433.5–438.9 s | 17.3 / 9.2 | 29 / 9 | elbow bend at limit 6%; leg at limit 6%; **ground IK failed 6 frames**; outlier knee max (z +6.2) *(excluded)* |
| `sophie_1_1_1_t446-450` | A | 7_sophie_1_1_1 445.8–450.4 s | 1.8 / 1.1 | 26 / 8 | **foot held 32 mm off the floor (median)** *(excluded)* |
| `sophie_1_1_1_t55-60_shift` | B | 7_sophie_1_1_1 55.1–59.8 s | 19.6 / 9.6 | 23 / 7 | leg at limit 9%; **ground IK failed 10 frames** *(excluded)* |
| `sophie_1_1_1_t77-83_shift` | B | 7_sophie_1_1_1 77.1–82.6 s | 21.6 / 9.6 | 23 / 8 | **ground IK failed 4 frames**; outlier knee max (z +7.9); right arm behind body 7 cm (human's in front) *(excluded)* |
| `sophie_1_2_2_t204-221` | A | 7_sophie_1_2_2 204.4–220.7 s | 1.7 / 1.1 | 19 / 7 | elbow bend at limit 9%; **foot held 40 mm off the floor (median)** *(excluded)* |
| `sophie_1_2_2_t248-255_shift` | B | 7_sophie_1_2_2 247.6–254.9 s | 11.1 / 4.3 | 18 / 8 | elbow bend at limit 9%; outlier knee max (z +7.7); **foot held 30 mm off the floor (median)** *(excluded)* |
| `sophie_1_2_2_t520-529` | A | 7_sophie_1_2_2 520.1–529.4 s | 1.4 / 1.5 | 16 / 7 | elbow bend at limit 15%; **foot held 30 mm off the floor (median)** *(excluded)* |
| `sophie_1_2_2_t587-592` | A | 7_sophie_1_2_2 587.4–591.6 s | 4.1 / 2.5 | 22 / 8 | elbow bend at limit 18%; outlier knee max (z +5.4); **foot held 38 mm off the floor (median)**; right arm behind body 6 cm (human's in front) *(excluded)* |
| `sophie_1_3_3_t117-124_shift` | B | 7_sophie_1_3_3 116.9–124.1 s | 13.0 / 2.6 | 18 / 7 | knee 63 deg; leg at limit 15%; **ground IK failed 16 frames**; outlier trunk drop (z +4.3); outlier knee max (z +9.1); **joint jump 1.21 rad (Right_Ankle_Pitch at 4.4 s)**; **foot held 44 mm off the floor (median)** *(excluded)* |
| `sophie_1_3_3_t144-150_shift` | B | 7_sophie_1_3_3 144.4–150.0 s | 10.4 / 2.1 | 17 / 8 | leg at limit 34%; **ground IK failed 47 frames**; outlier knee max (z +7.8); right arm behind body 5 cm (human's in front) *(excluded)* |
| `sophie_1_3_3_t17-21_shift` | B | 7_sophie_1_3_3 16.6–21.1 s | 16.3 / 9.3 | 7 / 3 | head at limit 75%; shoulder at limit 100%; **trunk leans 22 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `sophie_1_3_3_t217-223` | A | 7_sophie_1_3_3 216.6–223.0 s | 9.9 / 2.0 | 19 / 5 | head at limit 100%; shoulder at limit 100%; elbow bend at limit 7%; **trunk leans 32 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `sophie_1_3_3_t226-231` | A | 7_sophie_1_3_3 226.2–230.5 s | 7.6 / 4.3 | 26 / 9 | head at limit 8%; leg at limit 18%; **ground IK failed 19 frames**; **joint jump 0.60 rad (Left_Knee_Pitch at 1.4 s)** *(excluded)* |
| `sophie_1_3_3_t282-287` | A | 7_sophie_1_3_3 282.1–286.7 s | 0.9 / 1.0 | 15 / 5 | elbow bend at limit 31%; **foot held 30 mm off the floor (median)** *(excluded)* |
| `sophie_1_3_3_t331-338_shift` | B | 7_sophie_1_3_3 330.9–337.5 s | 14.2 / 2.4 | 24 / 8 | leg at limit 24%; **ground IK failed 45 frames**; outlier knee max (z +8.0) *(excluded)* |
| `sophie_1_3_3_t340-348_shift` | B | 7_sophie_1_3_3 339.5–347.9 s | 12.6 / 5.4 | 16 / 5 | knee 63 deg; head at limit 6%; leg at limit 12%; **ground IK failed 30 frames**; outlier trunk drop (z +4.1); outlier knee max (z +9.1); **root jump 3.2 cm/frame** *(excluded)* |
| `sophie_1_3_3_t385-389` | A | 7_sophie_1_3_3 385.0–389.2 s | 1.5 / 2.1 | 16 / 8 | **foot held 32 mm off the floor (median)** *(excluded)* |
| `sophie_1_3_3_t402-411` | A | 7_sophie_1_3_3 402.0–411.2 s | 1.4 / 1.5 | 21 / 7 | **ground IK failed 4 frames**; **root jump 3.1 cm/frame** *(excluded)* |
| `sophie_1_3_3_t501-508_shift` | B | 7_sophie_1_3_3 501.3–507.9 s | 21.4 / 14.7 | 17 / 6 | knee 67 deg; **ground IK failed 4 frames**; outlier knee max (z +10.2); **joint jump 1.20 rad (Left_Ankle_Pitch at 5.8 s)**; right arm behind body 6 cm (human's in front) *(excluded)* |
| `sophie_1_4_4_t0-9` | A | 7_sophie_1_4_4 0.0–9.0 s | 1.7 / 1.6 | 8 / 4 | **foot held 41 mm off the floor (median)** *(excluded)* |
| `sophie_1_4_4_t524-530_shift` | B | 7_sophie_1_4_4 524.3–530.5 s | 21.4 / 18.6 | 18 / 6 | K1 feet move 19 cm; knee 76 deg; outlier knee max (z +13.5); **foot held 34 mm off the floor (median)** *(excluded)* |
| `sophie_1_5_5_t370-382` | A | 7_sophie_1_5_5 370.3–381.5 s | 1.5 / 2.0 | 10 / 3 | head at limit 7%; elbow bend at limit 10%; **foot held 30 mm off the floor (median)** *(excluded)* |
| `sophie_1_5_5_t426-440` | A | 7_sophie_1_5_5 426.3–440.2 s | 1.4 / 1.4 | 19 / 6 | elbow bend at limit 6%; **foot held 35 mm off the floor (median)** *(excluded)* |
| `sophie_1_5_5_t466-472_shift` | B | 7_sophie_1_5_5 465.6–472.2 s | 13.4 / 4.4 | 17 / 4 | leg at limit 23%; **ground IK failed 42 frames**; outlier knee max (z +7.5); **root jump 3.3 cm/frame** *(excluded)* |
| `sophie_1_5_5_t470-479` | A | 7_sophie_1_5_5 470.2–478.8 s | 2.5 / 1.6 | 12 / 4 | **foot held 45 mm off the floor (median)** *(excluded)* |
| `sophie_1_5_5_t507-515` | A | 7_sophie_1_5_5 506.5–515.0 s | 1.7 / 1.2 | 9 / 4 | **foot held 43 mm off the floor (median)** *(excluded)* |
| `sophie_1_5_5_t522-526` | A | 7_sophie_1_5_5 521.5–526.5 s | 1.8 / 1.0 | 23 / 7 | **foot held 35 mm off the floor (median)** *(excluded)* |
| `sophie_1_5_5_t531-545` | A | 7_sophie_1_5_5 530.8–544.8 s | 2.3 / 1.4 | 4 / 1 | head at limit 47%; **foot held 36 mm off the floor (median)** *(excluded)* |
| `sophie_1_5_5_t545-559` | A | 7_sophie_1_5_5 544.8–558.8 s | 2.2 / 1.9 | 29 / 9 | **foot held 47 mm off the floor (median)** *(excluded)* |
| `sophie_1_5_5_t574-578_shift` | B | 7_sophie_1_5_5 574.0–578.0 s | 24.7 / 13.4 | 53 / 17 | shoulder at limit 43%; elbow bend at limit 18%; outlier knee max (z +6.6); **joint jump 1.95 rad (Left_Elbow_Pitch at 1.7 s)**; **root jump 4.0 cm/frame**; **root turn 33 deg/frame**; left arm behind body 5 cm (human's in front) *(excluded)* |
| `sophie_1_6_6_t114-128` | A | 7_sophie_1_6_6 113.8–127.6 s | 2.1 / 1.3 | 5 / 3 | head at limit 10%; **foot held 34 mm off the floor (median)** *(excluded)* |
| `sophie_1_6_6_t189-199` | A | 7_sophie_1_6_6 189.1–199.3 s | 3.2 / 4.0 | 10 / 4 | **root jump 3.4 cm/frame** *(excluded)* |
| `sophie_1_6_6_t344-349_shift` | B | 7_sophie_1_6_6 343.9–349.4 s | 24.8 / 13.3 | 22 / 7 | head at limit 48%; **ground IK failed 1 frames** *(excluded)* |
| `sophie_1_6_6_t431-436` | A | 7_sophie_1_6_6 430.6–436.0 s | 9.4 / 2.2 | 28 / 8 | leg at limit 7%; **ground IK failed 10 frames**; outlier knee max (z +7.1) *(excluded)* |
| `sophie_1_6_6_t448-460` | A | 7_sophie_1_6_6 447.9–459.8 s | 9.6 / 1.1 | 16 / 6 | elbow bend at limit 6%; **ground IK failed 1 frames** *(excluded)* |
| `sophie_1_6_6_t456-460_shift` | B | 7_sophie_1_6_6 455.9–459.9 s | 8.9 / 1.4 | 15 / 5 | elbow bend at limit 13%; leg at limit 6%; **ground IK failed 3 frames**; **trunk leans 15 deg (median)** *(excluded)* |
| `sophie_1_6_6_t573-578_shift` | B | 7_sophie_1_6_6 573.0–577.5 s | 19.2 / 11.1 | 22 / 5 | shoulder at limit 93%; elbow bend at limit 72%; outlier knee max (z +6.5); **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `sophie_1_6_6_t576-580` | A | 7_sophie_1_6_6 575.5–579.6 s | 1.8 / 1.6 | 21 / 5 | head at limit 39%; shoulder at limit 100%; elbow bend at limit 57%; **left arm behind body 14 cm (human's in front)** *(excluded)* |
| `sophie_1_6_6_t578-582_shift` | B | 7_sophie_1_6_6 577.6–582.1 s | 15.6 / 10.9 | 25 / 7 | head at limit 68%; shoulder at limit 99%; elbow bend at limit 26%; **trunk leans 19 deg (median)**; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `sophie_1_7_7_t412-429` | A | 7_sophie_1_7_7 411.5–429.4 s | 4.2 / 1.0 | 21 / 8 | head at limit 13%; elbow bend at limit 10%; **joint jump 0.80 rad (Left_Elbow_Yaw at 16.3 s)**; right arm behind body 6 cm (human's in front) *(excluded)* |
| `sophie_1_7_7_t427-432_shift` | B | 7_sophie_1_7_7 427.4–431.9 s | 10.2 / 5.9 | 20 / 11 | **joint jump 0.80 rad (Left_Elbow_Yaw at 0.4 s)**; right arm behind body 5 cm (human's in front) *(excluded)* |
| `sophie_1_7_7_t434-439_shift` | B | 7_sophie_1_7_7 434.5–439.1 s | 17.0 / 11.3 | 19 / 9 | elbow bend at limit 11%; outlier knee max (z +4.1); **foot held 40 mm off the floor (median)**; right arm behind body 6 cm (human's in front) *(excluded)* |
| `sophie_1_7_7_t437-441` | A | 7_sophie_1_7_7 437.1–441.3 s | 0.9 / 0.8 | 18 / 7 | elbow bend at limit 12%; **foot held 37 mm off the floor (median)**; right arm behind body 6 cm (human's in front) *(excluded)* |
| `sophie_1_7_7_t487-505` | A | 7_sophie_1_7_7 487.2–505.0 s | 5.4 / 2.4 | 19 / 8 | elbow bend at limit 17%; **root jump 5.2 cm/frame**; **root turn 28 deg/frame**; right arm behind body 6 cm (human's in front) *(excluded)* |
| `sophie_1_8_8_t48-65` | A | 7_sophie_1_8_8 47.8–64.5 s | 2.5 / 1.6 | 17 / 5 | elbow bend at limit 7%; **foot held 30 mm off the floor (median)** *(excluded)* |
| `sophie_1_8_8_t488-504` | A | 7_sophie_1_8_8 488.4–503.7 s | 1.5 / 1.2 | 21 / 7 | elbow bend at limit 7%; **joint jump 0.71 rad (Right_Shoulder_Pitch at 5.6 s)** *(excluded)* |
| `sophie_1_9_9_t102-107_shift` | B | 7_sophie_1_9_9 102.1–106.6 s | 22.4 / 13.2 | 19 / 9 | head at limit 6%; shoulder at limit 24%; elbow bend at limit 20%; outlier knee max (z +6.5); **joint jump 1.95 rad (Left_Elbow_Pitch at 1.1 s)**; **root turn 30 deg/frame** *(excluded)* |
| `sophie_1_9_9_t259-264_shift` | B | 7_sophie_1_9_9 258.9–264.3 s | 23.4 / 13.3 | 18 / 6 | head at limit 92%; shoulder at limit 100%; elbow bend at limit 11%; outlier knee max (z +6.0); **trunk leans 31 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `stewart_0_12_12_t40-52` | A | 5_stewart_0_12_12 39.7–52.3 s | 0.3 / 0.9 | 11 / 2 | shoulder at limit 100%; **trunk leans 23 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `stewart_0_87_87_t30-34` | A | 5_stewart_0_87_87 29.9–33.9 s | 3.3 / 0.7 | 29 / 4 | head at limit 7%; shoulder at limit 100%; **trunk leans 27 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `stewart_1_2_2_t339-359` | A | 5_stewart_1_2_2 339.3–358.6 s | 0.5 / 0.7 | 21 / 9 | **joint jump 1.14 rad (Right_Elbow_Pitch at 3.4 s)**; **root turn 13 deg/frame** *(excluded)* |
| `stewart_1_2_2_t455-474` | A | 5_stewart_1_2_2 454.7–474.0 s | 0.3 / 1.3 | 13 / 3 | head at limit 32%; shoulder at limit 100%; **trunk leans 26 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `tiffnay_0_103_103_t4-8_shift` | B | 28_tiffnay_0_103_103 3.6–7.8 s | 20.8 / 21.6 | 10 / 10 | K1 feet move 22 cm; trunk drop 5 cm; **outlier trunk drop (z +5.3)**; **joint jump 1.12 rad (Left_Hip_Yaw at 2.1 s)**; **root jump 14.4 cm/frame**; **root turn 75 deg/frame** *(excluded)* |
| `tiffnay_0_10_10_t15-27_shift` | B | 28_tiffnay_0_10_10 14.5–26.6 s | 12.6 / 7.8 | 15 / 8 | **joint jump 0.85 rad (Left_Elbow_Pitch at 7.7 s)**; **root turn 36 deg/frame**; **right foot slides 7.6 cm in one frame (at 7.6 s)** *(excluded)* |
| `tiffnay_0_14_14_t72-77_shift` | B | 28_tiffnay_0_14_14 72.3–76.5 s | 8.8 / 7.3 | 12 / 9 | **joint jump 0.87 rad (Right_Shoulder_Roll at 2.1 s)**; **root jump 16.3 cm/frame**; **root turn 33 deg/frame**; **foot held 40 mm off the floor (median)** *(excluded)* |
| `tiffnay_0_15_15_t29-33_shift` | B | 28_tiffnay_0_15_15 28.9–33.1 s | 11.4 / 11.7 | 14 / 6 | **root jump 16.3 cm/frame**; **root turn 22 deg/frame** *(excluded)* |
| `tiffnay_0_16_16_t18-22_shift` | B | 28_tiffnay_0_16_16 18.2–22.4 s | 18.8 / 25.9 | 20 / 11 | K1 feet move 26 cm; trunk drop 10 cm; **outlier trunk drop (z +11.6)**; **joint jump 0.83 rad (Left_Shoulder_Pitch at 2.1 s)**; **root jump 17.0 cm/frame**; **root turn 40 deg/frame** *(excluded)* |
| `tiffnay_0_16_16_t20-36` | A | 28_tiffnay_0_16_16 20.4–35.8 s | 6.0 / 25.3 | 12 / 6 | K1 feet move 25 cm; trunk drop 7 cm; **ground IK failed 1 frames**; **outlier trunk drop (z +7.6)**; **joint jump 0.69 rad (Left_Hip_Yaw at 13.4 s)**; **root jump 12.4 cm/frame**; **root turn 21 deg/frame** *(excluded)* |
| `tiffnay_0_16_16_t34-41_shift` | B | 28_tiffnay_0_16_16 33.8–40.9 s | 12.6 / 24.5 | 9 / 4 | K1 feet move 25 cm; trunk drop 7 cm; **ground IK failed 1 frames**; **outlier trunk drop (z +8.4)**; **joint jump 0.69 rad (Left_Hip_Yaw at 0.1 s)**; **root jump 12.4 cm/frame**; **root turn 21 deg/frame** *(excluded)* |
| `tiffnay_0_1_1_t35-39_shift` | B | 28_tiffnay_0_1_1 34.6–39.2 s | 8.8 / 3.7 | 17 / 6 | leg at limit 23%; **ground IK failed 29 frames** *(excluded)* |
| `tiffnay_0_1_1_t37-54` | A | 28_tiffnay_0_1_1 37.2–54.0 s | 5.8 / 1.6 | 7 / 3 | leg at limit 9%; **ground IK failed 42 frames** *(excluded)* |
| `tiffnay_0_1_1_t54-71` | A | 28_tiffnay_0_1_1 54.0–70.7 s | 6.5 / 3.4 | 8 / 3 | leg at limit 8%; **ground IK failed 29 frames** *(excluded)* |
| `tiffnay_0_3_3_t40-60` | A | 28_tiffnay_0_3_3 39.9–59.8 s | 8.5 / 2.1 | 6 / 3 | leg at limit 7%; **ground IK failed 35 frames** *(excluded)* |
| `tiffnay_0_3_3_t60-80` | A | 28_tiffnay_0_3_3 59.8–79.8 s | 5.3 / 2.1 | 7 / 3 | leg at limit 7%; **ground IK failed 35 frames** *(excluded)* |
| `tiffnay_0_5_5_t4-17` | A | 28_tiffnay_0_5_5 3.8–17.5 s | 2.1 / 0.7 | 5 / 3 | **root turn 8 deg/frame** *(excluded)* |
| `tiffnay_0_6_6_t39-48_shift` | B | 28_tiffnay_0_6_6 39.4–48.3 s | 7.7 / 4.4 | 6 / 3 | leg at limit 11%; **ground IK failed 3 frames** *(excluded)* |
| `tiffnay_0_73_73_t0-5_shift` | B | 28_tiffnay_0_73_73 0.0–5.3 s | 17.5 / 8.4 | 9 / 5 | trunk drop 20 cm; **ground IK failed 1 frames**; **outlier trunk drop (z +25.5)**; **joint jump 1.13 rad (Left_Hip_Yaw at 3.2 s)**; **root jump 43.9 cm/frame**; **root turn 52 deg/frame** *(excluded)* |
| `tiffnay_0_82_82_t42-58` | A | 28_tiffnay_0_82_82 41.7–58.2 s | 3.3 / 0.7 | 3 / 2 | leg at limit 48%; **ground IK failed 232 frames** *(excluded)* |
| `tiffnay_0_96_96_t0-11` | A | 28_tiffnay_0_96_96 0.0–11.4 s | 8.1 / 2.2 | 5 / 2 | **ground IK failed 3 frames** *(excluded)* |
| `tiffnay_1_1_1_t253-268` | A | 28_tiffnay_1_1_1 252.9–267.8 s | 7.5 / 2.9 | 13 / 5 | **ground IK failed 17 frames** *(excluded)* |
| `tiffnay_1_1_1_t40-56` | A | 28_tiffnay_1_1_1 40.2–55.6 s | 7.4 / 3.5 | 8 / 3 | **ground IK failed 17 frames** *(excluded)* |
| `tiffnay_1_1_1_t427-444` | A | 28_tiffnay_1_1_1 427.2–444.4 s | 6.4 / 2.4 | 8 / 3 | leg at limit 6%; **ground IK failed 21 frames** *(excluded)* |
| `tiffnay_1_1_1_t535-554` | A | 28_tiffnay_1_1_1 535.5–553.7 s | 6.3 / 2.3 | 11 / 4 | leg at limit 6%; **ground IK failed 26 frames** *(excluded)* |
| `tiffnay_1_2_2_t276-294` | A | 28_tiffnay_1_2_2 276.5–294.1 s | 7.6 / 2.5 | 10 / 4 | **ground IK failed 4 frames** *(excluded)* |
| `tiffnay_1_2_2_t3-8_shift` | B | 28_tiffnay_1_2_2 3.0–8.0 s | 22.6 / 15.5 | 7 / 3 | leg at limit 5%; **ground IK failed 8 frames**; outlier knee max (z +7.7); **joint jump 1.21 rad (Right_Ankle_Pitch at 0.0 s)** *(excluded)* |
| `tiffnay_1_2_2_t316-336` | A | 28_tiffnay_1_2_2 316.4–335.8 s | 7.3 / 4.8 | 8 / 3 | leg at limit 9%; **ground IK failed 45 frames** *(excluded)* |
| `tiffnay_1_2_2_t394-413` | A | 28_tiffnay_1_2_2 394.0–413.4 s | 6.2 / 3.2 | 6 / 2 | **ground IK failed 11 frames** *(excluded)* |
| `tiffnay_1_2_2_t512-531` | A | 28_tiffnay_1_2_2 512.0–530.9 s | 5.9 / 2.3 | 9 / 5 | elbow bend at limit 17%; **ground IK failed 16 frames** *(excluded)* |
| `tiffnay_1_2_2_t86-105` | A | 28_tiffnay_1_2_2 85.5–104.5 s | 7.0 / 3.5 | 5 / 3 | **ground IK failed 15 frames** *(excluded)* |
| `tiffnay_1_3_3_t120-135` | A | 28_tiffnay_1_3_3 119.7–134.9 s | 9.3 / 2.8 | 10 / 6 | elbow bend at limit 13%; leg at limit 11%; **ground IK failed 45 frames** *(excluded)* |
| `tiffnay_1_3_3_t160-180` | A | 28_tiffnay_1_3_3 160.0–179.8 s | 5.3 / 2.9 | 10 / 3 | **ground IK failed 11 frames**; **joint jump 0.61 rad (Left_Knee_Pitch at 3.2 s)** *(excluded)* |
| `tiffnay_1_3_3_t221-239` | A | 28_tiffnay_1_3_3 220.6–238.7 s | 5.9 / 2.4 | 8 / 4 | leg at limit 5%; **ground IK failed 24 frames** *(excluded)* |
| `tiffnay_1_3_3_t23-43` | A | 28_tiffnay_1_3_3 22.7–42.7 s | 6.6 / 1.8 | 9 / 5 | leg at limit 8%; **ground IK failed 28 frames** *(excluded)* |
| `tiffnay_1_3_3_t273-279_shift` | B | 28_tiffnay_1_3_3 272.9–279.3 s | 19.7 / 7.6 | 6 / 3 | leg at limit 7%; **ground IK failed 34 frames**; outlier knee max (z +4.9); **joint jump 1.21 rad (Right_Ankle_Pitch at 2.7 s)**; **foot held 42 mm off the floor (median)** *(excluded)* |
| `tiffnay_1_3_3_t277-297` | A | 28_tiffnay_1_3_3 277.3–297.0 s | 6.8 / 3.3 | 17 / 7 | leg at limit 6%; **ground IK failed 29 frames** *(excluded)* |
| `tiffnay_1_3_3_t297-317` | A | 28_tiffnay_1_3_3 297.0–316.7 s | 7.0 / 3.3 | 11 / 4 | **ground IK failed 25 frames** *(excluded)* |
| `tiffnay_1_3_3_t358-362_shift` | B | 28_tiffnay_1_3_3 357.9–362.4 s | 16.7 / 7.6 | 26 / 10 | **ground IK failed 5 frames**; outlier knee max (z +4.7) *(excluded)* |
| `tiffnay_1_3_3_t385-395` | A | 28_tiffnay_1_3_3 384.7–394.6 s | 9.7 / 2.9 | 12 / 5 | leg at limit 10%; **ground IK failed 27 frames** *(excluded)* |
| `tiffnay_1_3_3_t393-397_shift` | B | 28_tiffnay_1_3_3 392.6–397.0 s | 8.7 / 4.0 | 17 / 5 | leg at limit 23%; **ground IK failed 22 frames** *(excluded)* |
| `tiffnay_1_3_3_t395-415` | A | 28_tiffnay_1_3_3 395.0–414.7 s | 5.1 / 1.3 | 16 / 6 | elbow bend at limit 19%; leg at limit 6%; **ground IK failed 22 frames** *(excluded)* |
| `tiffnay_1_3_3_t415-434` | A | 28_tiffnay_1_3_3 414.7–434.5 s | 8.5 / 3.4 | 23 / 8 | elbow bend at limit 11%; leg at limit 14%; **ground IK failed 75 frames** *(excluded)* |
| `tiffnay_1_3_3_t434-454` | A | 28_tiffnay_1_3_3 434.5–454.3 s | 7.6 / 2.4 | 18 / 6 | leg at limit 5%; **ground IK failed 28 frames** *(excluded)* |
| `tiffnay_1_3_3_t472-481_shift` | B | 28_tiffnay_1_3_3 472.0–480.8 s | 14.2 / 7.4 | 13 / 5 | leg at limit 12%; **ground IK failed 31 frames** *(excluded)* |
| `tiffnay_1_3_3_t479-496` | A | 28_tiffnay_1_3_3 478.8–496.4 s | 5.4 / 1.3 | 22 / 8 | elbow bend at limit 20%; **ground IK failed 6 frames** *(excluded)* |
| `tiffnay_1_3_3_t496-514` | A | 28_tiffnay_1_3_3 496.4–514.0 s | 6.1 / 4.7 | 6 / 3 | elbow bend at limit 17%; **ground IK failed 18 frames** *(excluded)* |
| `tiffnay_1_3_3_t533-546` | A | 28_tiffnay_1_3_3 533.0–546.0 s | 9.5 / 4.1 | 33 / 10 | leg at limit 9%; **ground IK failed 33 frames**; **joint jump 1.09 rad (Left_Elbow_Pitch at 11.3 s)**; **root turn 23 deg/frame** *(excluded)* |
| `tiffnay_1_3_3_t551-567` | A | 28_tiffnay_1_3_3 550.7–566.7 s | 8.6 / 7.3 | 23 / 7 | leg at limit 7%; **ground IK failed 29 frames** *(excluded)* |
| `tiffnay_1_3_3_t565-571_shift` | B | 28_tiffnay_1_3_3 564.7–571.5 s | 9.9 / 7.8 | 31 / 8 | leg at limit 6%; **ground IK failed 13 frames** *(excluded)* |
| `tiffnay_1_3_3_t89-100` | A | 28_tiffnay_1_3_3 89.0–99.7 s | 7.3 / 2.9 | 14 / 6 | leg at limit 9%; **ground IK failed 28 frames** *(excluded)* |
| `wayne_0_100_100_t6-20` | A | 1_wayne_0_100_100 5.9–20.4 s | 7.6 / 4.2 | 41 / 16 | **joint jump 0.61 rad (Left_Shoulder_Pitch at 8.7 s)** *(excluded)* |
| `wayne_0_104_104_t60-70_shift` | B | 1_wayne_0_104_104 60.4–70.1 s | 19.3 / 12.2 | 15 / 6 | knee 63 deg; outlier knee max (z +9.1); self-collision left_foot_collision / right_foot_collision 0.2 s (at 4.3 s, 6 mm); **feet overlap 6 mm for 0.2 s (at 4.3 s)** *(excluded)* |
| `wayne_0_107_107_t0-6_shift` | B | 1_wayne_0_107_107 0.0–6.1 s | 19.3 / 11.3 | 29 / 8 | head at limit 5%; shoulder at limit 60%; **trunk leans 24 deg (median)**; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `wayne_0_10_10_t13-22_shift` | B | 1_wayne_0_10_10 13.0–22.4 s | 15.2 / 16.4 | 14 / 7 | trunk drop 6 cm; knee 66 deg; **outlier trunk drop (z +6.7)**; outlier knee max (z +9.9); **joint jump 1.27 rad (Left_Elbow_Pitch at 3.9 s)**; **root jump 11.8 cm/frame**; **root turn 21 deg/frame**; **foot held 58 mm off the floor (median)** *(excluded)* |
| `wayne_0_110_110_t2-14` | A | 1_wayne_0_110_110 2.1–13.5 s | 4.4 / 3.7 | 31 / 11 | **joint jump 0.75 rad (Right_Elbow_Pitch at 3.9 s)** *(excluded)* |
| `wayne_0_14_14_t13-18_shift` | B | 1_wayne_0_14_14 13.4–17.8 s | 5.7 / 1.9 | 21 / 8 | **root jump 3.6 cm/frame** *(excluded)* |
| `wayne_0_14_14_t16-20` | A | 1_wayne_0_14_14 15.8–20.1 s | 1.3 / 1.8 | 17 / 5 | **root jump 3.6 cm/frame** *(excluded)* |
| `wayne_0_17_17_t0-14` | A | 1_wayne_0_17_17 0.0–14.4 s | 0.8 / 7.2 | 16 / 6 | leg at limit 56%; **ground IK failed 193 frames**; **joint jump 0.76 rad (Left_Knee_Pitch at 6.4 s)**; **root jump 6.5 cm/frame**; **root turn 11 deg/frame**; **Left_Knee_Pitch over its speed limit for 0.13 s (at 10.6 s)** *(excluded)* |
| `wayne_0_17_17_t14-29` | A | 1_wayne_0_17_17 14.4–28.9 s | 6.0 / 2.0 | 15 / 5 | leg at limit 100%; **ground IK failed 333 frames** *(excluded)* |
| `wayne_0_17_17_t27-31_shift` | B | 1_wayne_0_17_17 26.9–31.2 s | 8.3 / 3.5 | 12 / 4 | leg at limit 69%; **ground IK failed 83 frames** *(excluded)* |
| `wayne_0_17_17_t29-47` | A | 1_wayne_0_17_17 29.2–47.4 s | 4.9 / 3.2 | 15 / 5 | leg at limit 7%; **ground IK failed 18 frames** *(excluded)* |
| `wayne_0_17_17_t45-50_shift` | B | 1_wayne_0_17_17 45.4–50.1 s | 8.7 / 4.9 | 12 / 4 | leg at limit 71%; **ground IK failed 78 frames** *(excluded)* |
| `wayne_0_17_17_t48-67` | A | 1_wayne_0_17_17 48.1–66.8 s | 7.4 / 1.5 | 11 / 4 | leg at limit 100%; **ground IK failed 483 frames** *(excluded)* |
| `wayne_0_18_18_t0-8` | A | 1_wayne_0_18_18 0.0–7.7 s | 0.3 / 0.7 | 10 / 4 | leg at limit 100%; **ground IK failed 230 frames**; outlier knee max (z -5.9) *(excluded)* |
| `wayne_0_18_18_t23-36` | A | 1_wayne_0_18_18 23.4–36.3 s | 0.5 / 0.9 | 12 / 5 | leg at limit 100%; **ground IK failed 386 frames**; outlier knee max (z -8.2); self-collision left_foot_collision / right_foot_collision 2.3 s (at 0.8 s, 17 mm); **feet overlap 17 mm for 2.3 s (at 0.8 s)** *(excluded)* |
| `wayne_0_18_18_t34-40_shift` | B | 1_wayne_0_18_18 34.3–39.8 s | 20.5 / 8.4 | 17 / 8 | leg at limit 67%; **ground IK failed 84 frames**; self-collision left_foot_collision / right_foot_collision 1.0 s (at 0.3 s, 13 mm); **feet overlap 13 mm for 1.0 s (at 0.3 s)** *(excluded)* |
| `wayne_0_18_18_t49-61` | A | 1_wayne_0_18_18 49.2–60.6 s | 4.7 / 4.2 | 9 / 4 | leg at limit 27%; **ground IK failed 83 frames** *(excluded)* |
| `wayne_0_18_18_t6-10_shift` | B | 1_wayne_0_18_18 5.7–10.1 s | 13.8 / 5.0 | 13 / 6 | leg at limit 69%; **ground IK failed 82 frames** *(excluded)* |
| `wayne_0_18_18_t8-23` | A | 1_wayne_0_18_18 8.1–22.7 s | 1.9 / 1.6 | 11 / 4 | leg at limit 14%; **ground IK failed 15 frames** *(excluded)* |
| `wayne_0_19_19_t0-7` | A | 1_wayne_0_19_19 0.0–7.3 s | 0.5 / 0.6 | 8 / 3 | leg at limit 100%; **ground IK failed 219 frames**; outlier knee max (z -7.5); self-collision left_foot_collision / right_foot_collision 7.3 s (at 0.0 s, 18 mm); **feet overlap 18 mm for 7.3 s (at 0.0 s)** *(excluded)* |
| `wayne_0_19_19_t13-18_shift` | B | 1_wayne_0_19_19 13.3–18.0 s | 12.8 / 8.6 | 19 / 8 | leg at limit 100%; **ground IK failed 114 frames** *(excluded)* |
| `wayne_0_19_19_t16-30` | A | 1_wayne_0_19_19 16.0–30.1 s | 1.0 / 1.4 | 13 / 5 | leg at limit 100%; **ground IK failed 423 frames**; outlier knee max (z -9.8) *(excluded)* |
| `wayne_0_19_19_t27-31_shift` | B | 1_wayne_0_19_19 26.7–30.7 s | 24.8 / 14.2 | 15 / 6 | leg at limit 100%; **ground IK failed 119 frames**; outlier knee max (z -3.5) *(excluded)* |
| `wayne_0_19_19_t31-35` | A | 1_wayne_0_19_19 30.6–35.2 s | 2.1 / 2.0 | 16 / 5 | leg at limit 100%; **ground IK failed 119 frames** *(excluded)* |
| `wayne_0_19_19_t36-55` | A | 1_wayne_0_19_19 36.0–54.5 s | 0.5 / 2.2 | 18 / 5 | leg at limit 100%; **ground IK failed 410 frames**; **self-collision left_foot_collision / right_foot_collision 3.1 s (at 3.6 s, 33 mm)**; **feet overlap 33 mm for 3.1 s (at 3.6 s)** *(excluded)* |
| `wayne_0_19_19_t55-71` | A | 1_wayne_0_19_19 55.1–70.8 s | 3.4 / 2.7 | 15 / 5 | leg at limit 10%; **ground IK failed 13 frames**; **Left_Knee_Pitch over its speed limit for 0.17 s (at 0.6 s)**; self-collision left_foot_collision / right_foot_collision 0.3 s (at 0.0 s, 13 mm); **feet overlap 13 mm for 0.3 s (at 0.0 s)** *(excluded)* |
| `wayne_0_19_19_t8-15` | A | 1_wayne_0_19_19 7.9–15.3 s | 2.1 / 1.6 | 14 / 5 | leg at limit 100%; **ground IK failed 43 frames** *(excluded)* |
| `wayne_0_1_1_t0-8_shift` | B | 1_wayne_0_1_1 0.0–7.6 s | 14.4 / 10.4 | 15 / 4 | head at limit 32%; shoulder at limit 100%; **trunk leans 28 deg (median)**; **left arm behind body 17 cm (human's in front)** *(excluded)* |
| `wayne_0_20_20_t0-14` | A | 1_wayne_0_20_20 0.2–14.1 s | 0.4 / 0.9 | 16 / 5 | leg at limit 99%; **ground IK failed 404 frames** *(excluded)* |
| `wayne_0_20_20_t14-28` | A | 1_wayne_0_20_20 14.1–27.9 s | 0.9 / 0.7 | 19 / 6 | leg at limit 100%; **ground IK failed 416 frames**; outlier knee max (z -10.4) *(excluded)* |
| `wayne_0_20_20_t25-29_shift` | B | 1_wayne_0_20_20 24.6–28.6 s | 24.9 / 13.2 | 34 / 9 | leg at limit 100%; **ground IK failed 107 frames**; outlier knee max (z +5.8) *(excluded)* |
| `wayne_0_20_20_t28-33` | A | 1_wayne_0_20_20 28.5–32.9 s | 1.9 / 1.5 | 13 / 5 | leg at limit 100%; **ground IK failed 24 frames**; **joint jump 0.60 rad (Left_Knee_Pitch at 4.0 s)** *(excluded)* |
| `wayne_0_20_20_t34-47` | A | 1_wayne_0_20_20 33.7–46.5 s | 0.8 / 0.8 | 12 / 4 | leg at limit 100%; **ground IK failed 386 frames**; outlier knee max (z -8.7); self-collision left_foot_collision / right_foot_collision 0.5 s (at 4.4 s, 9 mm); **feet overlap 9 mm for 0.5 s (at 4.4 s)** *(excluded)* |
| `wayne_0_20_20_t45-49_shift` | B | 1_wayne_0_20_20 44.5–49.0 s | 11.5 / 6.7 | 12 / 4 | leg at limit 87%; **ground IK failed 81 frames** *(excluded)* |
| `wayne_0_20_20_t47-63` | A | 1_wayne_0_20_20 47.0–62.8 s | 9.6 / 5.5 | 10 / 4 | leg at limit 90%; **ground IK failed 296 frames**; self-collision left_foot_collision / right_foot_collision 4.3 s (at 6.2 s, 20 mm); **feet overlap 20 mm for 4.3 s (at 6.2 s)** *(excluded)* |
| `wayne_0_21_21_t0-17` | A | 1_wayne_0_21_21 0.0–16.9 s | 6.6 / 2.5 | 10 / 4 | leg at limit 98%; **ground IK failed 476 frames** *(excluded)* |
| `wayne_0_21_21_t17-34` | A | 1_wayne_0_21_21 16.9–33.9 s | 0.2 / 0.9 | 6 / 2 | leg at limit 100%; **ground IK failed 451 frames** *(excluded)* |
| `wayne_0_21_21_t34-51` | A | 1_wayne_0_21_21 33.9–50.8 s | 1.7 / 2.1 | 8 / 3 | leg at limit 55%; **ground IK failed 270 frames** *(excluded)* |
| `wayne_0_22_22_t18-36` | A | 1_wayne_0_22_22 17.9–35.9 s | 7.8 / 4.8 | 13 / 4 | leg at limit 68%; **ground IK failed 297 frames** *(excluded)* |
| `wayne_0_22_22_t36-54` | A | 1_wayne_0_22_22 35.9–53.8 s | 0.2 / 1.2 | 12 / 4 | leg at limit 100%; **ground IK failed 539 frames**; outlier knee max (z -11.7) *(excluded)* |
| `wayne_0_22_22_t54-72` | A | 1_wayne_0_22_22 53.8–71.8 s | 6.5 / 3.7 | 11 / 4 | leg at limit 74%; **ground IK failed 356 frames** *(excluded)* |
| `wayne_0_23_23_t0-16` | A | 1_wayne_0_23_23 0.0–16.1 s | 7.7 / 3.6 | 11 / 4 | leg at limit 50%; **ground IK failed 231 frames** *(excluded)* |
| `wayne_0_23_23_t16-32` | A | 1_wayne_0_23_23 16.1–32.1 s | 2.3 / 2.1 | 14 / 6 | leg at limit 99%; **ground IK failed 471 frames** *(excluded)* |
| `wayne_0_23_23_t30-35_shift` | B | 1_wayne_0_23_23 30.1–34.7 s | 9.6 / 4.9 | 12 / 5 | leg at limit 38%; **ground IK failed 49 frames** *(excluded)* |
| `wayne_0_23_23_t54-58_shift` | B | 1_wayne_0_23_23 53.7–58.1 s | 9.0 / 5.6 | 5 / 2 | leg at limit 43%; **ground IK failed 51 frames**; self-collision left_foot_collision / right_foot_collision 1.1 s (at 3.3 s, 14 mm); **feet overlap 14 mm for 1.1 s (at 3.3 s)** *(excluded)* |
| `wayne_0_23_23_t56-63` | A | 1_wayne_0_23_23 56.1–62.8 s | 7.2 / 2.8 | 7 / 3 | leg at limit 99%; **ground IK failed 190 frames**; self-collision left_foot_collision / right_foot_collision 4.4 s (at 2.2 s, 15 mm); **feet overlap 15 mm for 4.4 s (at 2.2 s)** *(excluded)* |
| `wayne_0_24_24_t0-5_shift` | B | 1_wayne_0_24_24 0.0–5.3 s | 13.1 / 4.8 | 9 / 3 | leg at limit 100%; **ground IK failed 159 frames**; outlier trunk drop (z +3.9); outlier knee max (z -7.1); self-collision left_foot_collision / right_foot_collision 2.4 s (at 0.5 s, 11 mm); **feet overlap 11 mm for 2.4 s (at 0.5 s)** *(excluded)* |
| `wayne_0_24_24_t3-18` | A | 1_wayne_0_24_24 3.3–17.9 s | 9.2 / 4.1 | 14 / 5 | leg at limit 69%; **ground IK failed 296 frames** *(excluded)* |
| `wayne_0_24_24_t32-46` | A | 1_wayne_0_24_24 32.5–45.8 s | 3.5 / 1.4 | 13 / 5 | leg at limit 100%; **ground IK failed 400 frames**; outlier knee max (z -8.8) *(excluded)* |
| `wayne_0_24_24_t46-59` | A | 1_wayne_0_24_24 45.8–59.2 s | 2.8 / 19.5 | 14 / 7 | K1 feet move 20 cm; leg at limit 98%; **ground IK failed 383 frames**; **joint jump 1.25 rad (Right_Elbow_Pitch at 3.0 s)**; **root jump 10.5 cm/frame**; **root turn 37 deg/frame** *(excluded)* |
| `wayne_0_24_24_t57-64_shift` | B | 1_wayne_0_24_24 57.2–63.8 s | 16.7 / 8.0 | 22 / 6 | leg at limit 38%; **ground IK failed 43 frames** *(excluded)* |
| `wayne_0_25_25_t0-16` | A | 1_wayne_0_25_25 0.0–16.2 s | 1.1 / 14.5 | 17 / 5 | K1 feet move 14 cm; leg at limit 91%; **ground IK failed 443 frames**; outlier knee max (z +6.0); **joint jump 0.94 rad (Right_Knee_Pitch at 1.4 s)**; **root jump 5.5 cm/frame**; **root turn 11 deg/frame**; **self-collision left_shank_lower_collision / right_shank_lower_collision 14.8 s (at 1.4 s, 60 mm)**; **feet overlap 54 mm for 14.8 s (at 1.4 s)** *(excluded)* |
| `wayne_0_25_25_t16-32` | A | 1_wayne_0_25_25 16.2–32.4 s | 1.7 / 1.3 | 17 / 6 | leg at limit 100%; **ground IK failed 487 frames**; outlier knee max (z -8.1); **self-collision left_shank_lower_collision / right_shank_lower_collision 16.2 s (at 0.0 s, 62 mm)**; **feet overlap 55 mm for 16.2 s (at 0.0 s)** *(excluded)* |
| `wayne_0_25_25_t30-35_shift` | B | 1_wayne_0_25_25 30.4–34.9 s | 9.9 / 5.2 | 27 / 9 | leg at limit 92%; **ground IK failed 106 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 4.4 s (at 0.0 s, 79 mm)**; **feet overlap 68 mm for 4.4 s (at 0.0 s)** *(excluded)* |
| `wayne_0_25_25_t33-46` | A | 1_wayne_0_25_25 32.9–46.2 s | 9.5 / 5.0 | 30 / 8 | leg at limit 97%; **ground IK failed 373 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 13.3 s (at 0.0 s, 77 mm)**; **feet overlap 68 mm for 13.3 s (at 0.0 s)** *(excluded)* |
| `wayne_0_25_25_t46-60` | A | 1_wayne_0_25_25 46.2–59.6 s | 1.2 / 1.1 | 22 / 8 | leg at limit 100%; **ground IK failed 378 frames**; **self-collision left_foot_collision / right_foot_collision 13.4 s (at 0.0 s, 56 mm)**; **feet overlap 56 mm for 13.4 s (at 0.0 s)** *(excluded)* |
| `wayne_0_25_25_t58-62_shift` | B | 1_wayne_0_25_25 57.6–61.8 s | 1.1 / 2.5 | 22 / 7 | leg at limit 100%; **ground IK failed 86 frames**; **self-collision left_foot_collision / right_foot_collision 4.2 s (at 0.0 s, 61 mm)**; **feet overlap 61 mm for 4.2 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t0-4` | A | 1_wayne_0_26_26 0.0–4.1 s | 4.6 / 3.9 | 9 / 3 | leg at limit 18%; **ground IK failed 11 frames**; **self-collision left_foot_collision / right_foot_collision 4.1 s (at 0.0 s, 65 mm)**; **feet overlap 65 mm for 4.1 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t18-22_shift` | B | 1_wayne_0_26_26 17.7–22.1 s | 9.7 / 4.8 | 21 / 9 | leg at limit 62%; **ground IK failed 76 frames**; **self-collision left_foot_collision / right_foot_collision 4.4 s (at 0.0 s, 62 mm)**; **feet overlap 62 mm for 4.4 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t2-7_shift` | B | 1_wayne_0_26_26 2.1–6.7 s | 12.5 / 6.3 | 24 / 6 | leg at limit 72%; **ground IK failed 90 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 4.6 s (at 0.0 s, 73 mm)**; **feet overlap 72 mm for 4.6 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t20-39` | A | 1_wayne_0_26_26 20.1–38.8 s | 8.3 / 4.1 | 17 / 7 | leg at limit 79%; **ground IK failed 427 frames**; **self-collision left_foot_collision / right_foot_collision 18.7 s (at 0.0 s, 70 mm)**; **feet overlap 70 mm for 18.7 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t39-57` | A | 1_wayne_0_26_26 38.8–57.5 s | 2.0 / 3.0 | 19 / 7 | leg at limit 43%; **ground IK failed 218 frames**; **self-collision left_foot_collision / right_foot_collision 18.7 s (at 0.0 s, 63 mm)**; **feet overlap 63 mm for 18.7 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t5-20` | A | 1_wayne_0_26_26 4.7–19.7 s | 0.5 / 1.5 | 29 / 9 | leg at limit 99%; **ground IK failed 436 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 15.0 s (at 0.0 s, 76 mm)**; **feet overlap 60 mm for 15.0 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t57-76` | A | 1_wayne_0_26_26 57.5–76.2 s | 3.8 / 3.4 | 20 / 8 | leg at limit 68%; **ground IK failed 307 frames**; **self-collision left_foot_collision / right_foot_collision 18.7 s (at 0.0 s, 63 mm)**; **feet overlap 63 mm for 18.7 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t76-95` | A | 1_wayne_0_26_26 76.2–94.8 s | 3.4 / 2.1 | 18 / 7 | leg at limit 51%; **ground IK failed 197 frames**; **self-collision left_foot_collision / right_foot_collision 18.7 s (at 0.0 s, 63 mm)**; **feet overlap 63 mm for 18.7 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t93-97_shift` | B | 1_wayne_0_26_26 92.8–97.3 s | 12.5 / 7.9 | 17 / 8 | leg at limit 44%; **ground IK failed 57 frames**; outlier knee max (z +7.1); **self-collision left_foot_collision / right_foot_collision 4.5 s (at 0.0 s, 68 mm)**; **feet overlap 68 mm for 4.5 s (at 0.0 s)** *(excluded)* |
| `wayne_0_26_26_t95-101` | A | 1_wayne_0_26_26 95.3–100.5 s | 2.3 / 2.2 | 16 / 5 | leg at limit 99%; **ground IK failed 147 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 5.2 s (at 0.0 s, 85 mm)**; **feet overlap 64 mm for 5.2 s (at 0.0 s)** *(excluded)* |
| `wayne_0_27_27_t0-18` | A | 1_wayne_0_27_27 0.1–17.7 s | 5.0 / 2.8 | 14 / 6 | leg at limit 60%; **ground IK failed 312 frames**; **self-collision left_foot_collision / right_foot_collision 17.5 s (at 0.0 s, 62 mm)**; **feet overlap 62 mm for 17.5 s (at 0.0 s)** *(excluded)* |
| `wayne_0_27_27_t18-35` | A | 1_wayne_0_27_27 17.7–35.2 s | 4.8 / 2.6 | 28 / 9 | leg at limit 79%; **ground IK failed 347 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 17.6 s (at 0.0 s, 67 mm)**; **feet overlap 63 mm for 17.6 s (at 0.0 s)** *(excluded)* |
| `wayne_0_27_27_t35-53` | A | 1_wayne_0_27_27 35.2–52.8 s | 7.3 / 3.6 | 20 / 7 | leg at limit 99%; **ground IK failed 4 frames**; **self-collision left_foot_collision / right_foot_collision 17.6 s (at 0.0 s, 63 mm)**; **feet overlap 63 mm for 17.6 s (at 0.0 s)** *(excluded)* |
| `wayne_0_27_27_t53-70` | A | 1_wayne_0_27_27 52.8–70.3 s | 10.3 / 5.1 | 22 / 7 | human steps; leg at limit 21%; **ground IK failed 87 frames**; **self-collision left_foot_collision / right_foot_collision 17.5 s (at 0.0 s, 65 mm)**; **feet overlap 65 mm for 17.5 s (at 0.0 s)** *(excluded)* |
| `wayne_0_27_27_t68-77_shift` | B | 1_wayne_0_27_27 68.3–76.8 s | 16.7 / 7.4 | 19 / 6 | leg at limit 73%; **ground IK failed 166 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 8.4 s (at 0.0 s, 84 mm)**; **feet overlap 72 mm for 8.4 s (at 0.0 s)** *(excluded)* |
| `wayne_0_27_27_t71-76` | A | 1_wayne_0_27_27 70.8–76.0 s | 2.9 / 1.8 | 13 / 4 | leg at limit 74%; **ground IK failed 104 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 5.2 s (at 0.0 s, 84 mm)**; **feet overlap 60 mm for 5.2 s (at 0.0 s)** *(excluded)* |
| `wayne_0_28_28_t0-18` | A | 1_wayne_0_28_28 0.0–17.9 s | 0.6 / 1.1 | 14 / 5 | leg at limit 100%; **ground IK failed 512 frames**; **self-collision left_foot_collision / right_foot_collision 17.9 s (at 0.0 s, 61 mm)**; **feet overlap 61 mm for 17.9 s (at 0.0 s)** *(excluded)* |
| `wayne_0_28_28_t18-36` | A | 1_wayne_0_28_28 17.9–35.9 s | 11.3 / 6.7 | 17 / 6 | human steps; leg at limit 42%; **ground IK failed 188 frames**; **joint jump 0.62 rad (Right_Knee_Pitch at 4.1 s)**; **self-collision left_foot_collision / right_foot_collision 17.9 s (at 0.0 s, 69 mm)**; **feet overlap 69 mm for 17.9 s (at 0.0 s)** *(excluded)* |
| `wayne_0_28_28_t36-54` | A | 1_wayne_0_28_28 35.9–53.8 s | 7.9 / 3.5 | 21 / 8 | shoulder at limit 17%; leg at limit 64%; **ground IK failed 238 frames**; **self-collision left_foot_collision / right_foot_collision 18.0 s (at 0.0 s, 67 mm)**; **feet overlap 67 mm for 18.0 s (at 0.0 s)** *(excluded)* |
| `wayne_0_28_28_t54-72` | A | 1_wayne_0_28_28 53.8–71.8 s | 9.2 / 7.1 | 19 / 6 | leg at limit 56%; **ground IK failed 228 frames**; **self-collision left_foot_collision / right_foot_collision 17.9 s (at 0.0 s, 64 mm)**; **feet overlap 64 mm for 17.9 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t0-8_shift` | B | 1_wayne_0_29_29 0.0–7.8 s | 17.7 / 8.1 | 18 / 7 | leg at limit 42%; **ground IK failed 65 frames**; outlier knee max (z +3.8); **self-collision left_foot_collision / right_foot_collision 7.8 s (at 0.0 s, 66 mm)**; **feet overlap 66 mm for 7.8 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t1-5` | A | 1_wayne_0_29_29 0.9–5.2 s | 0.5 / 0.5 | 14 / 5 | leg at limit 100%; **ground IK failed 20 frames**; **self-collision left_foot_collision / right_foot_collision 4.3 s (at 0.0 s, 59 mm)**; **feet overlap 59 mm for 4.3 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t11-16_shift` | B | 1_wayne_0_29_29 11.2–15.6 s | 5.7 / 3.0 | 19 / 8 | leg at limit 100%; **ground IK failed 35 frames**; **self-collision left_foot_collision / right_foot_collision 4.5 s (at 0.0 s, 62 mm)**; **feet overlap 62 mm for 4.5 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t14-28` | A | 1_wayne_0_29_29 13.6–28.1 s | 4.9 / 3.0 | 23 / 9 | **self-collision left_foot_collision / right_foot_collision 14.5 s (at 0.0 s, 63 mm)**; **feet overlap 63 mm for 14.5 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t26-31_shift` | B | 1_wayne_0_29_29 26.1–30.6 s | 11.8 / 6.9 | 20 / 7 | leg at limit 37%; **ground IK failed 18 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 4.5 s (at 0.0 s, 72 mm)**; **feet overlap 72 mm for 4.5 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t29-43` | A | 1_wayne_0_29_29 28.6–43.2 s | 4.4 / 3.0 | 23 / 8 | leg at limit 100%; **ground IK failed 177 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 14.6 s (at 0.0 s, 72 mm)**; **feet overlap 62 mm for 14.6 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t41-46_shift` | B | 1_wayne_0_29_29 41.2–45.6 s | 8.1 / 4.7 | 9 / 3 | leg at limit 62%; **ground IK failed 58 frames**; outlier knee max (z +3.8); **self-collision left_shank_lower_collision / right_shank_lower_collision 4.4 s (at 0.0 s, 122 mm)**; **feet overlap 64 mm for 4.4 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t44-58` | A | 1_wayne_0_29_29 43.6–58.2 s | 3.2 / 1.6 | 18 / 6 | **self-collision left_foot_collision / right_foot_collision 14.6 s (at 0.0 s, 66 mm)**; **feet overlap 66 mm for 14.6 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t56-61_shift` | B | 1_wayne_0_29_29 56.2–60.6 s | 6.5 / 4.1 | 23 / 7 | leg at limit 52%; **ground IK failed 67 frames**; **self-collision left_foot_collision / right_foot_collision 4.4 s (at 0.0 s, 57 mm)**; **feet overlap 57 mm for 4.4 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t59-68` | A | 1_wayne_0_29_29 58.6–68.4 s | 0.6 / 3.7 | 20 / 8 | leg at limit 100%; **ground IK failed 119 frames**; **self-collision left_foot_collision / right_foot_collision 9.8 s (at 0.0 s, 60 mm)**; **feet overlap 60 mm for 9.8 s (at 0.0 s)** *(excluded)* |
| `wayne_0_29_29_t6-13` | A | 1_wayne_0_29_29 5.8–13.2 s | 5.2 / 3.1 | 15 / 6 | leg at limit 90%; **ground IK failed 152 frames**; **self-collision left_foot_collision / right_foot_collision 7.4 s (at 0.0 s, 67 mm)**; **feet overlap 67 mm for 7.4 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t0-13` | A | 1_wayne_0_30_30 0.2–12.8 s | 9.1 / 5.1 | 15 / 6 | leg at limit 43%; **self-collision left_foot_collision / right_foot_collision 12.6 s (at 0.0 s, 60 mm)**; **feet overlap 60 mm for 12.6 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t13-25` | A | 1_wayne_0_30_30 12.8–25.5 s | 9.9 / 6.0 | 24 / 8 | leg at limit 100%; **self-collision left_foot_collision / right_foot_collision 12.7 s (at 0.0 s, 57 mm)**; **feet overlap 57 mm for 12.7 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t22-26_shift` | B | 1_wayne_0_30_30 21.8–25.8 s | 10.2 / 6.7 | 17 / 7 | leg at limit 100%; **ground IK failed 6 frames**; **self-collision left_foot_collision / right_foot_collision 4.0 s (at 0.0 s, 56 mm)**; **feet overlap 56 mm for 4.0 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t27-37` | A | 1_wayne_0_30_30 26.5–37.5 s | 0.6 / 1.4 | 14 / 5 | leg at limit 100%; **ground IK failed 90 frames**; **self-collision left_foot_collision / right_foot_collision 10.9 s (at 0.0 s, 56 mm)**; **feet overlap 56 mm for 10.9 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t35-40_shift` | B | 1_wayne_0_30_30 35.5–39.9 s | 10.3 / 5.4 | 11 / 4 | leg at limit 69%; outlier knee max (z +4.8); **self-collision left_shank_lower_collision / right_shank_lower_collision 4.4 s (at 0.0 s, 64 mm)**; **feet overlap 63 mm for 4.4 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t38-55` | A | 1_wayne_0_30_30 37.9–55.1 s | 8.3 / 3.9 | 22 / 8 | leg at limit 41%; **ground IK failed 65 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 17.2 s (at 0.0 s, 79 mm)**; **feet overlap 66 mm for 17.2 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t53-58_shift` | B | 1_wayne_0_30_30 53.1–57.7 s | 11.2 / 5.2 | 19 / 7 | leg at limit 18%; outlier knee max (z +4.1); **self-collision left_shank_lower_collision / right_shank_lower_collision 4.6 s (at 0.0 s, 71 mm)**; **feet overlap 66 mm for 4.6 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t56-67` | A | 1_wayne_0_30_30 55.7–67.1 s | 0.6 / 1.0 | 22 / 9 | leg at limit 99%; **self-collision left_foot_collision / right_foot_collision 11.4 s (at 0.0 s, 57 mm)**; **feet overlap 57 mm for 11.4 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t65-70_shift` | B | 1_wayne_0_30_30 65.1–70.0 s | 17.6 / 8.9 | 20 / 9 | leg at limit 37%; **ground IK failed 18 frames**; outlier knee max (z +5.5); **self-collision left_foot_collision / right_foot_collision 4.9 s (at 0.0 s, 70 mm)**; **feet overlap 70 mm for 4.9 s (at 0.0 s)** *(excluded)* |
| `wayne_0_30_30_t68-73` | A | 1_wayne_0_30_30 68.0–72.8 s | 8.0 / 4.3 | 20 / 7 | leg at limit 99%; **ground IK failed 22 frames**; **self-collision left_shank_lower_collision / right_shank_lower_collision 4.8 s (at 0.0 s, 68 mm)**; **feet overlap 58 mm for 4.8 s (at 0.0 s)** *(excluded)* |
| `wayne_0_31_31_t0-8` | A | 1_wayne_0_31_31 0.0–8.2 s | 9.9 / 5.1 | 27 / 8 | leg at limit 47%; **ground IK failed 39 frames**; outlier trunk drop (z +5.1); **self-collision left_shank_lower_collision / right_shank_lower_collision 8.2 s (at 0.0 s, 83 mm)**; **feet overlap 63 mm for 8.2 s (at 0.0 s)** *(excluded)* |
| `wayne_0_31_31_t10-19` | A | 1_wayne_0_31_31 10.2–18.8 s | 0.7 / 1.2 | 21 / 8 | **self-collision left_foot_collision / right_foot_collision 8.6 s (at 0.0 s, 63 mm)**; **feet overlap 63 mm for 8.6 s (at 0.0 s)** *(excluded)* |
| `wayne_0_31_31_t17-26_shift` | B | 1_wayne_0_31_31 16.8–25.7 s | 21.8 / 10.5 | 14 / 5 | leg at limit 37%; **ground IK failed 56 frames**; outlier knee max (z +6.9); **self-collision left_shank_lower_collision / right_shank_lower_collision 8.8 s (at 0.0 s, 87 mm)**; **feet overlap 73 mm for 8.8 s (at 0.0 s)** *(excluded)* |
| `wayne_0_31_31_t24-33` | A | 1_wayne_0_31_31 23.7–33.3 s | 0.8 / 1.9 | 27 / 8 | **self-collision left_shank_lower_collision / right_shank_lower_collision 9.6 s (at 0.0 s, 76 mm)**; **feet overlap 61 mm for 9.6 s (at 0.0 s)** *(excluded)* |
| `wayne_0_31_31_t38-56` | A | 1_wayne_0_31_31 38.5–55.6 s | 8.1 / 4.1 | 26 / 10 | **self-collision left_shank_lower_collision / right_shank_lower_collision 17.1 s (at 0.0 s, 87 mm)**; **feet overlap 73 mm for 17.1 s (at 0.0 s)** *(excluded)* |
| `wayne_0_31_31_t56-73` | A | 1_wayne_0_31_31 55.6–72.8 s | 8.5 / 4.4 | 29 / 10 | leg at limit 28%; **ground IK failed 84 frames**; outlier knee max (z +3.8); **self-collision left_foot_collision / right_foot_collision 17.1 s (at 0.0 s, 69 mm)**; **feet overlap 69 mm for 17.1 s (at 0.0 s)** *(excluded)* |
| `wayne_0_31_31_t6-12_shift` | B | 1_wayne_0_31_31 6.2–12.2 s | 20.7 / 9.6 | 27 / 10 | leg at limit 13%; **ground IK failed 12 frames**; outlier knee max (z +4.3); **self-collision left_shank_lower_collision / right_shank_lower_collision 6.0 s (at 0.0 s, 77 mm)**; **feet overlap 74 mm for 6.0 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t0-14` | A | 1_wayne_0_32_32 0.0–14.3 s | 6.3 / 3.4 | 26 / 8 | **self-collision left_shank_lower_collision / right_shank_lower_collision 14.3 s (at 0.0 s, 86 mm)**; **feet overlap 63 mm for 14.3 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t12-21_shift` | B | 1_wayne_0_32_32 12.3–20.6 s | 9.7 / 4.1 | 26 / 9 | **self-collision left_shank_lower_collision / right_shank_lower_collision 8.3 s (at 0.0 s, 73 mm)**; **feet overlap 67 mm for 8.3 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t19-24` | A | 1_wayne_0_32_32 18.6–23.8 s | 2.8 / 2.8 | 49 / 21 | leg at limit 22%; **ground IK failed 20 frames**; outlier arms k1 cm (z +3.8); **self-collision left_shank_lower_collision / right_shank_lower_collision 5.2 s (at 0.0 s, 70 mm)**; **feet overlap 64 mm for 5.2 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t22-30_shift` | B | 1_wayne_0_32_32 21.8–29.6 s | 23.8 / 10.9 | 42 / 15 | leg at limit 16%; **ground IK failed 23 frames**; outlier knee max (z +5.7); **self-collision left_shank_lower_collision / right_shank_lower_collision 7.8 s (at 0.0 s, 85 mm)**; **feet overlap 77 mm for 3.8 s (at 3.9 s)** *(excluded)* |
| `wayne_0_32_32_t28-47` | A | 1_wayne_0_32_32 27.6–46.6 s | 9.5 / 4.3 | 27 / 9 | **self-collision left_shank_lower_collision / right_shank_lower_collision 19.0 s (at 0.0 s, 92 mm)**; **feet overlap 66 mm for 19.0 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t45-49_shift` | B | 1_wayne_0_32_32 44.6–49.4 s | 17.3 / 9.2 | 14 / 5 | outlier knee max (z +5.8); **self-collision left_foot_collision / right_foot_collision 4.8 s (at 0.0 s, 70 mm)**; **feet overlap 70 mm for 4.8 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t51-63` | A | 1_wayne_0_32_32 50.9–62.6 s | 6.6 / 3.2 | 25 / 8 | leg at limit 49%; **self-collision left_shank_lower_collision / right_shank_lower_collision 11.7 s (at 0.0 s, 94 mm)**; **feet overlap 62 mm for 11.7 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t61-65_shift` | B | 1_wayne_0_32_32 60.6–65.1 s | 15.0 / 8.5 | 25 / 8 | leg at limit 19%; **ground IK failed 3 frames**; outlier knee max (z +5.7); **self-collision left_foot_collision / right_foot_collision 4.5 s (at 0.0 s, 72 mm)**; **feet overlap 72 mm for 4.5 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t63-70` | A | 1_wayne_0_32_32 63.1–69.9 s | 2.3 / 1.5 | 19 / 7 | **self-collision left_shank_lower_collision / right_shank_lower_collision 6.8 s (at 0.0 s, 62 mm)**; **feet overlap 57 mm for 6.8 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t68-73_shift` | B | 1_wayne_0_32_32 67.9–72.6 s | 18.1 / 10.6 | 32 / 8 | leg at limit 13%; **ground IK failed 17 frames**; outlier knee max (z +4.2); **joint jump 0.69 rad (Left_Knee_Pitch at 2.6 s)**; **self-collision left_shank_lower_collision / right_shank_lower_collision 4.7 s (at 0.0 s, 80 mm)**; **feet overlap 76 mm for 4.7 s (at 0.0 s)** *(excluded)* |
| `wayne_0_32_32_t71-75` | A | 1_wayne_0_32_32 70.6–74.6 s | 6.8 / 5.4 | 29 / 6 | leg at limit 83%; **ground IK failed 3 frames**; **self-collision left_foot_collision / right_foot_collision 4.0 s (at 0.0 s, 62 mm)**; **feet overlap 62 mm for 4.0 s (at 0.0 s)** *(excluded)* |
| `wayne_0_33_33_t0-6` | A | 1_wayne_0_33_33 0.0–6.3 s | 7.5 / 27.7 | 23 / 8 | K1 feet move 28 cm; trunk drop 10 cm; leg at limit 60%; **ground IK failed 40 frames**; **outlier trunk drop (z +11.9)**; **joint jump 0.62 rad (Right_Knee_Pitch at 3.6 s)**; **root jump 8.1 cm/frame**; **foot held 62 mm off the floor (median)** *(excluded)* |
| `wayne_0_33_33_t18-23_shift` | B | 1_wayne_0_33_33 17.5–22.8 s | 21.5 / 9.7 | 23 / 9 | trunk drop 7 cm; leg at limit 7%; **ground IK failed 2 frames**; **outlier trunk drop (z +7.5)**; **foot held 212 mm off the floor (median)**; right arm behind body 6 cm (human's in front) *(excluded)* |
| `wayne_0_33_33_t21-40` | A | 1_wayne_0_33_33 20.8–40.0 s | 9.7 / 10.2 | 20 / 7 | K1 feet move 10 cm; trunk drop 9 cm; leg at limit 46%; **ground IK failed 181 frames**; **outlier trunk drop (z +10.3)**; **root jump 5.7 cm/frame**; **foot held 155 mm off the floor (median)** *(excluded)* |
| `wayne_0_33_33_t38-43_shift` | B | 1_wayne_0_33_33 38.0–42.6 s | 10.0 / 9.4 | 20 / 9 | trunk drop 10 cm; leg at limit 84%; **ground IK failed 107 frames**; **outlier trunk drop (z +12.0)**; **root jump 4.8 cm/frame**; **trunk leans 17 deg (median)**; **foot held 263 mm off the floor (median)** *(excluded)* |
| `wayne_0_33_33_t4-9_shift` | B | 1_wayne_0_33_33 4.3–8.8 s | 11.1 / 11.7 | 27 / 9 | leg at limit 11%; outlier trunk drop (z +4.6); **foot held 251 mm off the floor (median)**; **excluded in the spec (fails in training)** *(excluded)* |
| `wayne_0_33_33_t41-52` | A | 1_wayne_0_33_33 40.6–51.7 s | 0.7 / 5.7 | 19 / 7 | head at limit 8%; leg at limit 42%; **ground IK failed 84 frames**; outlier trunk drop (z +4.7); **joint jump 0.73 rad (Left_Knee_Pitch at 3.6 s)**; **trunk leans 19 deg (median)**; **foot held 267 mm off the floor (median)** *(excluded)* |
| `wayne_0_33_33_t52-63` | A | 1_wayne_0_33_33 51.7–62.7 s | 4.7 / 24.6 | 20 / 8 | K1 feet move 25 cm; trunk drop 14 cm; leg at limit 89%; **ground IK failed 244 frames**; **outlier trunk drop (z +18.3)**; **joint jump 0.72 rad (Left_Knee_Pitch at 0.9 s)**; **root jump 3.9 cm/frame**; **Left_Knee_Pitch over its speed limit for 0.20 s (at 7.7 s)**; self-collision left_foot_collision / right_foot_collision 0.3 s (at 3.6 s, 14 mm); **feet overlap 14 mm for 0.3 s (at 3.6 s)**; **foot held 109 mm off the floor (median)** *(excluded)* |
| `wayne_0_33_33_t7-20` | A | 1_wayne_0_33_33 6.8–19.5 s | 2.7 / 1.8 | 16 / 6 | **foot held 268 mm off the floor (median)**; right arm behind body 5 cm (human's in front) *(excluded)* |
| `wayne_0_37_37_t0-14` | A | 1_wayne_0_37_37 0.0–14.2 s | 4.7 / 4.5 | 22 / 5 | head at limit 13%; shoulder at limit 88%; **trunk leans 28 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `wayne_0_37_37_t29-33` | A | 1_wayne_0_37_37 28.8–33.3 s | 5.2 / 10.0 | 39 / 15 | K1 feet move 10 cm; outlier knee max (z +3.5); **root jump 4.1 cm/frame**; **self-collision left_foot_collision / right_foot_collision 0.3 s (at 4.2 s, 49 mm)**; **feet overlap 49 mm for 0.3 s (at 4.2 s)** *(excluded)* |
| `wayne_0_37_37_t31-43_shift` | B | 1_wayne_0_37_37 31.3–42.5 s | 23.7 / 13.1 | 26 / 11 | trunk drop 5 cm; **ground IK failed 2 frames**; **outlier trunk drop (z +5.4)**; outlier knee max (z +7.1); **joint jump 0.77 rad (Right_Knee_Pitch at 1.7 s)**; **root jump 5.1 cm/frame**; **root turn 8 deg/frame**; **self-collision left_foot_collision / right_foot_collision 0.4 s (at 1.7 s, 44 mm)**; **feet overlap 44 mm for 0.4 s (at 1.7 s)** *(excluded)* |
| `wayne_0_37_37_t41-45` | A | 1_wayne_0_37_37 40.5–45.1 s | 7.3 / 4.4 | 45 / 15 | leg at limit 33%; **ground IK failed 38 frames** *(excluded)* |
| `wayne_0_37_37_t43-52_shift` | B | 1_wayne_0_37_37 43.1–51.8 s | 16.7 / 8.3 | 37 / 15 | leg at limit 12%; **ground IK failed 26 frames**; outlier knee max (z +6.4) *(excluded)* |
| `wayne_0_38_38_t12-31` | A | 1_wayne_0_38_38 12.5–30.6 s | 8.1 / 5.1 | 25 / 8 | leg at limit 43%; **ground IK failed 66 frames** *(excluded)* |
| `wayne_0_38_38_t43-48` | A | 1_wayne_0_38_38 42.8–48.4 s | 1.6 / 1.4 | 22 / 7 | leg at limit 8%; **ground IK failed 8 frames** *(excluded)* |
| `wayne_0_38_38_t54-60` | A | 1_wayne_0_38_38 54.1–60.1 s | 3.7 / 1.0 | 12 / 5 | leg at limit 12%; **ground IK failed 16 frames** *(excluded)* |
| `wayne_0_39_39_t14-22` | A | 1_wayne_0_39_39 14.5–22.2 s | 4.1 / 8.8 | 30 / 11 | K1 feet move 9 cm; **self-collision left_foot_collision / right_foot_collision 0.9 s (at 6.8 s, 50 mm)**; **feet overlap 50 mm for 0.9 s (at 6.8 s)** *(excluded)* |
| `wayne_0_39_39_t20-25_shift` | B | 1_wayne_0_39_39 20.2–24.8 s | 14.0 / 11.9 | 35 / 15 | outlier knee max (z +6.1); **root jump 5.2 cm/frame**; **self-collision left_foot_collision / right_foot_collision 1.0 s (at 1.1 s, 63 mm)**; **feet overlap 63 mm for 1.0 s (at 1.1 s)** *(excluded)* |
| `wayne_0_39_39_t32-39` | A | 1_wayne_0_39_39 32.1–39.4 s | 5.6 / 3.2 | 26 / 10 | leg at limit 42%; **ground IK failed 20 frames**; self-collision left_foot_collision / right_foot_collision 0.1 s (at 2.3 s, 13 mm); **feet overlap 13 mm for 0.1 s (at 2.3 s)** *(excluded)* |
| `wayne_0_39_39_t51-56_shift` | B | 1_wayne_0_39_39 50.6–55.9 s | 28.7 / 15.4 | 22 / 9 | human steps; leg at limit 6%; **ground IK failed 1 frames**; outlier knee max (z +6.7); **joint jump 0.64 rad (Left_Knee_Pitch at 2.1 s)**; **root jump 4.0 cm/frame**; **self-collision left_foot_collision / right_foot_collision 0.3 s (at 2.6 s, 38 mm)**; **feet overlap 38 mm for 0.3 s (at 2.6 s)** *(excluded)* |
| `wayne_0_66_66_t36-49` | A | 1_wayne_0_66_66 36.2–49.2 s | 9.9 / 6.7 | 36 / 17 | outlier knee max (z +4.5); **joint jump 0.84 rad (Right_Elbow_Pitch at 1.0 s)**; **root turn 11 deg/frame** *(excluded)* |
| `wayne_0_67_67_t24-30` | A | 1_wayne_0_67_67 24.2–30.3 s | 5.4 / 0.9 | 64 / 22 | outlier arms k1 cm (z +4.1); **joint jump 0.63 rad (Right_Shoulder_Pitch at 4.7 s)** *(excluded)* |
| `wayne_0_69_69_t39-47_shift` | B | 1_wayne_0_69_69 38.6–47.5 s | 12.4 / 10.8 | 39 / 15 | **ground IK failed 8 frames**; **root jump 3.9 cm/frame** *(excluded)* |
| `wayne_0_72_72_t15-22` | A | 1_wayne_0_72_72 15.5–21.5 s | 5.2 / 2.7 | 32 / 15 | upper-arm twist at limit 9%; **joint jump 0.61 rad (Right_Elbow_Pitch at 5.5 s)** *(excluded)* |
| `wayne_0_72_72_t20-25_shift` | B | 1_wayne_0_72_72 19.5–25.1 s | 20.3 / 12.1 | 49 / 23 | **upper-arm twist at limit 74%**; outlier arms k1 cm (z +4.4); outlier knee max (z +7.7); **joint jump 0.61 rad (Right_Elbow_Pitch at 1.4 s)**; self-collision left_hand_collision / trunk_collision 0.6 s (at 3.2 s, 13 mm) *(excluded)* |
| `wayne_0_73_73_t10-17` | A | 1_wayne_0_73_73 10.0–16.7 s | 6.9 / 4.1 | 48 / 19 | shoulder at limit 14%; **joint jump 1.19 rad (Left_Elbow_Pitch at 1.3 s)**; **root turn 7 deg/frame** *(excluded)* |
| `wayne_0_73_73_t20-28_shift` | B | 1_wayne_0_73_73 20.0–28.4 s | 16.7 / 9.4 | 46 / 17 | trunk drop 5 cm; **outlier trunk drop (z +5.5)**; outlier knee max (z +7.3) *(excluded)* |
| `wayne_0_73_73_t7-12_shift` | B | 1_wayne_0_73_73 7.1–12.0 s | 13.0 / 7.8 | 40 / 14 | shoulder at limit 20%; **joint jump 1.19 rad (Left_Elbow_Pitch at 4.2 s)**; **root turn 7 deg/frame** *(excluded)* |
| `wayne_0_79_79_t1-19` | A | 1_wayne_0_79_79 1.4–18.9 s | 2.6 / 2.7 | 51 / 17 | **joint jump 0.62 rad (Right_Elbow_Yaw at 16.3 s)** *(excluded)* |
| `wayne_0_79_79_t17-21_shift` | B | 1_wayne_0_79_79 16.9–21.3 s | 7.3 / 6.7 | 122 / 35 | outlier arms k1 cm (z +7.7); **joint jump 0.62 rad (Right_Elbow_Yaw at 0.8 s)** *(excluded)* |
| `wayne_0_79_79_t39-47_shift` | B | 1_wayne_0_79_79 39.1–47.5 s | 25.6 / 17.0 | 47 / 16 | human steps; outlier knee max (z +4.2); **joint jump 0.77 rad (Right_Shoulder_Pitch at 8.3 s)** *(excluded)* |
| `wayne_0_79_79_t45-52` | A | 1_wayne_0_79_79 45.5–51.8 s | 6.4 / 5.1 | 45 / 14 | **joint jump 0.77 rad (Right_Shoulder_Pitch at 2.0 s)** *(excluded)* |
| `wayne_0_98_98_t22-26` | A | 1_wayne_0_98_98 22.2–26.4 s | 3.3 / 0.8 | 45 / 16 | outlier knee max (z +5.5); **foot held 44 mm off the floor (median)** *(excluded)* |
| `wayne_0_98_98_t32-37` | A | 1_wayne_0_98_98 31.5–36.8 s | 0.4 / 1.7 | 68 / 20 | **upper-arm twist at limit 52%**; shoulder at limit 8%; leg at limit 11%; **ground IK failed 11 frames**; outlier arms k1 cm (z +3.6); **root turn 8 deg/frame** *(excluded)* |
| `wayne_0_9_9_t9-28` | A | 1_wayne_0_9_9 8.6–27.8 s | 6.5 / 4.8 | 7 / 4 | **joint jump 0.93 rad (Left_Shoulder_Roll at 7.3 s)**; **root jump 5.1 cm/frame**; **root turn 33 deg/frame**; **right foot slides 4.1 cm in one frame (at 7.3 s)** *(excluded)* |
| `wayne_1_10_10_t413-421` | A | 1_wayne_1_10_10 413.2–421.1 s | 0.6 / 1.7 | 28 / 7 | head at limit 42%; shoulder at limit 84%; **trunk leans 28 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `wayne_1_12_12_t228-236_shift` | B | 1_wayne_1_12_12 228.3–236.2 s | 20.5 / 11.6 | 22 / 10 | **joint jump 0.75 rad (Right_Shoulder_Pitch at 4.7 s)**; **root turn 8 deg/frame** *(excluded)* |
| `wayne_1_12_12_t55-66` | A | 1_wayne_1_12_12 55.2–65.8 s | 5.7 / 3.6 | 43 / 14 | head at limit 8%; shoulder at limit 13%; upper-arm twist at limit 40%; leg at limit 16%; **ground IK failed 26 frames**; **foot held 52 mm off the floor (median)** *(excluded)* |
| `wayne_1_1_1_t356-365_shift` | B | 1_wayne_1_1_1 355.8–364.9 s | 22.0 / 18.9 | 27 / 10 | K1 feet move 19 cm; knee 67 deg; **ground IK failed 4 frames**; outlier knee max (z +10.3) *(excluded)* |
| `wayne_1_2_2_t174-179_shift` | B | 1_wayne_1_2_2 174.2–178.8 s | 12.9 / 7.7 | 43 / 9 | leg at limit 9%; **ground IK failed 3 frames**; outlier knee max (z +4.3); **joint jump 0.62 rad (Right_Knee_Pitch at 2.2 s)** *(excluded)* |
| `wayne_1_2_2_t562-573_shift` | B | 1_wayne_1_2_2 561.6–572.8 s | 22.5 / 21.0 | 35 / 13 | K1 feet move 21 cm; **ground IK failed 4 frames**; outlier knee max (z +5.2) *(excluded)* |
| `wayne_1_3_3_t148-153_shift` | B | 1_wayne_1_3_3 148.1–153.3 s | 18.3 / 7.6 | 23 / 10 | leg at limit 59%; **ground IK failed 83 frames**; **joint jump 0.62 rad (Right_Knee_Pitch at 2.6 s)**; **foot held 43 mm off the floor (median)** *(excluded)* |
| `wayne_1_3_3_t21-25_shift` | B | 1_wayne_1_3_3 20.6–24.6 s | 12.7 / 3.1 | 20 / 7 | leg at limit 20%; **ground IK failed 22 frames** *(excluded)* |
| `wayne_1_3_3_t232-243_shift` | B | 1_wayne_1_3_3 232.5–243.1 s | 19.1 / 8.4 | 33 / 11 | **ground IK failed 7 frames**; outlier knee max (z +6.7) *(excluded)* |
| `wayne_1_3_3_t251-260_shift` | B | 1_wayne_1_3_3 251.1–259.9 s | 21.1 / 16.9 | 39 / 14 | **ground IK failed 11 frames**; outlier knee max (z +5.7); **joint jump 0.60 rad (Left_Knee_Pitch at 4.3 s)** *(excluded)* |
| `wayne_1_3_3_t31-35_shift` | B | 1_wayne_1_3_3 31.4–35.4 s | 14.2 / 3.3 | 28 / 10 | leg at limit 11%; **ground IK failed 11 frames** *(excluded)* |
| `wayne_1_3_3_t364-369_shift` | B | 1_wayne_1_3_3 363.5–369.0 s | 13.8 / 5.4 | 26 / 9 | **ground IK failed 3 frames**; outlier knee max (z +5.2); **joint jump 0.60 rad (Right_Knee_Pitch at 1.3 s)** *(excluded)* |
| `wayne_1_4_4_t16-21_shift` | B | 1_wayne_1_4_4 16.4–20.8 s | 21.9 / 12.1 | 55 / 18 | **ground IK failed 1 frames**; **joint jump 0.91 rad (Left_Ankle_Pitch at 2.3 s)**; **root jump 22.5 cm/frame**; **root turn 10 deg/frame** *(excluded)* |
| `wayne_1_4_4_t170-179_shift` | B | 1_wayne_1_4_4 170.4–178.8 s | 24.9 / 18.8 | 22 / 8 | K1 feet move 19 cm; knee 64 deg; leg at limit 24%; **ground IK failed 26 frames**; outlier trunk drop (z +3.9); outlier knee max (z +9.4) *(excluded)* |
| `wayne_1_4_4_t219-224_shift` | B | 1_wayne_1_4_4 218.6–224.3 s | 10.7 / 3.3 | 20 / 7 | leg at limit 11%; **ground IK failed 17 frames** *(excluded)* |
| `wayne_1_4_4_t281-286_shift` | B | 1_wayne_1_4_4 280.9–285.8 s | 17.8 / 8.9 | 35 / 14 | **ground IK failed 3 frames** *(excluded)* |
| `wayne_1_4_4_t377-384_shift` | B | 1_wayne_1_4_4 376.7–383.8 s | 22.2 / 11.5 | 32 / 12 | **ground IK failed 7 frames**; outlier knee max (z +5.1); **joint jump 0.62 rad (Left_Knee_Pitch at 4.7 s)** *(excluded)* |
| `wayne_1_4_4_t38-43` | A | 1_wayne_1_4_4 37.5–43.1 s | 10.0 / 4.5 | 49 / 16 | shoulder at limit 5%; leg at limit 10%; **ground IK failed 6 frames** *(excluded)* |
| `wayne_1_4_4_t40-44_shift` | B | 1_wayne_1_4_4 39.9–43.9 s | 6.5 / 3.2 | 53 / 18 | shoulder at limit 8%; leg at limit 28%; **ground IK failed 22 frames**; **joint jump 0.61 rad (Right_Knee_Pitch at 3.8 s)** *(excluded)* |
| `wayne_1_5_5_t126-131_shift` | B | 1_wayne_1_5_5 126.1–130.7 s | 24.9 / 13.9 | 70 / 38 | shoulder at limit 9%; outlier arms k1 cm (z +8.4); **joint jump 0.71 rad (Right_Elbow_Pitch at 1.5 s)**; **root turn 13 deg/frame** *(excluded)* |
| `wayne_1_5_5_t13-20_shift` | B | 1_wayne_1_5_5 13.2–19.7 s | 21.5 / 13.7 | 22 / 8 | knee 67 deg; leg at limit 6%; **ground IK failed 1 frames**; outlier trunk drop (z +3.8); outlier knee max (z +10.3) *(excluded)* |
| `wayne_1_5_5_t162-170_shift` | B | 1_wayne_1_5_5 162.2–169.9 s | 34.0 / 20.1 | 23 / 8 | human steps; K1 feet move 20 cm; **ground IK failed 2 frames**; outlier knee max (z +4.0); **joint jump 0.63 rad (Right_Knee_Pitch at 5.3 s)** *(excluded)* |
| `wayne_1_5_5_t211-227_shift` | B | 1_wayne_1_5_5 210.9–226.5 s | 26.4 / 15.9 | 35 / 11 | human steps; **ground IK failed 4 frames**; outlier knee max (z +5.6) *(excluded)* |
| `wayne_1_5_5_t371-378_shift` | B | 1_wayne_1_5_5 370.5–377.8 s | 18.7 / 14.1 | 38 / 13 | leg at limit 9%; **ground IK failed 7 frames**; outlier knee max (z +4.1); **joint jump 0.60 rad (Right_Knee_Pitch at 7.0 s)** *(excluded)* |
| `wayne_1_6_6_t107-113_shift` | B | 1_wayne_1_6_6 107.4–112.8 s | 12.1 / 7.9 | 19 / 7 | leg at limit 16%; **ground IK failed 19 frames**; outlier knee max (z +5.7) *(excluded)* |
| `wayne_1_6_6_t128-133` | A | 1_wayne_1_6_6 127.7–132.8 s | 9.6 / 2.2 | 30 / 10 | leg at limit 10%; **ground IK failed 14 frames** *(excluded)* |
| `wayne_1_6_6_t131-137_shift` | B | 1_wayne_1_6_6 130.8–136.6 s | 10.0 / 2.4 | 36 / 13 | leg at limit 31%; **ground IK failed 48 frames** *(excluded)* |
| `wayne_1_6_6_t162-170_shift` | B | 1_wayne_1_6_6 162.3–169.9 s | 18.2 / 12.3 | 24 / 7 | **ground IK failed 5 frames**; outlier knee max (z +7.1); **joint jump 0.62 rad (Left_Knee_Pitch at 4.5 s)** *(excluded)* |
| `wayne_1_6_6_t223-228` | A | 1_wayne_1_6_6 222.6–228.2 s | 9.5 / 2.8 | 19 / 8 | leg at limit 6%; **ground IK failed 3 frames** *(excluded)* |
| `wayne_1_6_6_t360-365` | A | 1_wayne_1_6_6 360.2–364.8 s | 5.4 / 2.2 | 48 / 16 | leg at limit 28%; **ground IK failed 38 frames** *(excluded)* |
| `wayne_1_6_6_t480-485` | A | 1_wayne_1_6_6 480.0–485.0 s | 0.6 / 3.2 | 91 / 25 | **upper-arm twist at limit 58%**; leg at limit 7%; outlier arms k1 cm (z +5.1); self-collision right_hand_collision / trunk_collision 0.4 s (at 4.0 s, 10 mm); **foot held 38 mm off the floor (median)** *(excluded)* |
| `wayne_1_6_6_t5-18_shift` | B | 1_wayne_1_6_6 4.7–18.3 s | 24.8 / 16.7 | 26 / 11 | **ground IK failed 1 frames**; outlier knee max (z +5.9) *(excluded)* |
| `wayne_1_6_6_t84-94` | A | 1_wayne_1_6_6 83.6–94.4 s | 9.5 / 6.0 | 41 / 15 | trunk drop 6 cm; **outlier trunk drop (z +6.1)**; outlier knee max (z +7.8) *(excluded)* |
| `wayne_1_7_7_t205-209_shift` | B | 1_wayne_1_7_7 205.4–209.4 s | 48.5 / 27.6 | 8 / 3 | human steps; K1 feet move 28 cm; **ground IK failed 1 frames**; outlier knee max (z +5.7); **joint jump 0.62 rad (Left_Knee_Pitch at 3.3 s)** *(excluded)* |
| `wayne_1_7_7_t474-479` | A | 1_wayne_1_7_7 473.6–479.4 s | 7.4 / 3.0 | 27 / 10 | **ground IK failed 2 frames** *(excluded)* |
| `wayne_1_8_8_t323-329_shift` | B | 1_wayne_1_8_8 323.4–329.3 s | 12.3 / 8.0 | 30 / 17 | elbow bend at limit 30%; **joint jump 1.45 rad (Right_Shoulder_Pitch at 4.8 s)**; **root jump 3.2 cm/frame**; **root turn 17 deg/frame**; **self-collision head_2_collision / right_hand_end_collision 1.1 s (at 4.8 s, 26 mm)** *(excluded)* |
| `wayne_1_8_8_t327-331` | A | 1_wayne_1_8_8 327.3–331.4 s | 1.5 / 2.0 | 45 / 43 | elbow bend at limit 85%; outlier arms k1 cm (z +9.7); **joint jump 1.45 rad (Right_Shoulder_Pitch at 0.8 s)**; **root jump 3.2 cm/frame**; **root turn 17 deg/frame**; **self-collision head_2_collision / right_hand_end_collision 1.7 s (at 0.9 s, 35 mm)** *(excluded)* |
| `wayne_1_8_8_t329-334_shift` | B | 1_wayne_1_8_8 329.4–334.0 s | 10.0 / 6.4 | 42 / 27 | elbow bend at limit 35%; outlier arms k1 cm (z +5.4); **joint jump 1.32 rad (Right_Elbow_Pitch at 1.5 s)**; **root turn 17 deg/frame**; **self-collision head_2_collision / right_hand_end_collision 0.5 s (at 0.0 s, 35 mm)** *(excluded)* |
| `wayne_1_8_8_t363-367` | A | 1_wayne_1_8_8 363.1–367.4 s | 9.7 / 2.9 | 19 / 9 | leg at limit 6%; **ground IK failed 6 frames** *(excluded)* |
| `wayne_1_8_8_t365-372_shift` | B | 1_wayne_1_8_8 365.4–372.0 s | 21.7 / 11.7 | 18 / 7 | leg at limit 11%; **ground IK failed 2 frames** *(excluded)* |
| `wayne_1_8_8_t526-536_shift` | B | 1_wayne_1_8_8 526.5–535.5 s | 19.0 / 13.6 | 39 / 13 | knee 64 deg; **ground IK failed 3 frames**; outlier knee max (z +9.2); **joint jump 0.62 rad (Left_Knee_Pitch at 4.0 s)** *(excluded)* |
| `wayne_1_9_9_t406-416` | A | 1_wayne_1_9_9 405.7–416.1 s | 1.3 / 1.6 | 24 / 6 | head at limit 21%; shoulder at limit 88%; **trunk leans 21 deg (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `yingqing_0_103_103_t31-37` | A | 27_yingqing_0_103_103 31.3–37.4 s | 2.6 / 6.4 | 9 / 4 | trunk drop 27 cm; knee 128 deg; head at limit 17%; shoulder at limit 62%; leg at limit 32%; **ground IK failed 38 frames**; **outlier trunk drop (z +36.6)**; outlier knee max (z +30.6); self-collision right_hip_yaw_collision / trunk_collision 1.4 s (at 0.2 s, 14 mm) *(excluded)* |
| `yingqing_0_103_103_t39-47` | A | 27_yingqing_0_103_103 38.6–47.2 s | 1.6 / 1.1 | 16 / 6 | **joint jump 1.55 rad (Left_Shoulder_Pitch at 5.3 s)**; **root jump 3.7 cm/frame**; **root turn 32 deg/frame**; left arm behind body 6 cm (human's in front) *(excluded)* |
| `yingqing_0_1_1_t37-56` | A | 27_yingqing_0_1_1 36.7–56.0 s | 1.1 / 0.6 | 25 / 10 | **joint jump 0.62 rad (Left_Shoulder_Roll at 5.8 s)**; **self-collision left_hand_end_collision / waist_collision 2.0 s (at 8.0 s, 38 mm)**; hand presses into leg 49 mm for 2.3 s (at 7.9 s) *(excluded)* |
| `yingqing_0_1_1_t71-81` | A | 27_yingqing_0_1_1 70.7–81.3 s | 0.6 / 2.8 | 18 / 8 | head at limit 18%; shoulder at limit 30%; upper-arm twist at limit 9%; **ground IK failed 5 frames**; **joint jump 0.96 rad (Right_Shoulder_Roll at 6.5 s)**; **root turn 14 deg/frame** *(excluded)* |
| `yingqing_0_2_2_t45-59` | A | 27_yingqing_0_2_2 45.0–59.0 s | 0.4 / 0.9 | 27 / 12 | **joint jump 1.36 rad (Left_Shoulder_Roll at 3.3 s)**; **root turn 13 deg/frame**; hand presses into leg 23 mm for 0.6 s (at 11.3 s) *(excluded)* |
| `yingqing_0_81_81_t26-43` | A | 27_yingqing_0_81_81 26.3–43.2 s | 9.3 / 4.6 | 21 / 12 | **joint jump 1.44 rad (Left_Elbow_Pitch at 10.4 s)**; **root turn 15 deg/frame**; hand presses into leg 7 mm for 0.2 s (at 5.0 s) *(excluded)* |
| `yingqing_0_87_87_t16-21_shift` | B | 27_yingqing_0_87_87 15.8–21.2 s | 17.7 / 4.0 | 31 / 9 | knee 63 deg; **ground IK failed 2 frames**; outlier knee max (z +9.0); **foot held 41 mm off the floor (median)** *(excluded)* |
| `yingqing_0_87_87_t51-56` | A | 27_yingqing_0_87_87 50.7–56.0 s | 9.7 / 5.0 | 15 / 8 | head at limit 58%; shoulder at limit 95%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `yingqing_0_87_87_t54-58_shift` | B | 27_yingqing_0_87_87 53.9–57.9 s | 10.8 / 4.4 | 17 / 7 | leg at limit 13%; **ground IK failed 11 frames** *(excluded)* |
| `yingqing_0_87_87_t8-18` | A | 27_yingqing_0_87_87 7.6–17.8 s | 5.0 / 2.6 | 25 / 11 | self-collision left_hand_collision / right_hand_end_collision 4.9 s (at 1.1 s, 25 mm); **foot held 33 mm off the floor (median)** *(excluded)* |
| `yingqing_0_95_95_t19-24_shift` | B | 27_yingqing_0_95_95 18.6–23.6 s | 17.3 / 8.3 | 26 / 28 | shoulder at limit 42%; elbow bend at limit 43%; outlier arms k1 cm (z +5.8); outlier knee max (z +4.0); **joint jump 1.44 rad (Left_Elbow_Pitch at 4.8 s)**; **root turn 17 deg/frame**; self-collision head_2_collision / left_hand_end_collision 0.9 s (at 2.7 s, 12 mm) *(excluded)* |
| `yingqing_0_95_95_t25-31` | A | 27_yingqing_0_95_95 24.7–30.5 s | 1.0 / 1.0 | 22 / 14 | shoulder at limit 13%; elbow bend at limit 70%; **joint jump 1.16 rad (Left_Elbow_Yaw at 2.9 s)**; **root turn 10 deg/frame**; **self-collision head_2_collision / left_hand_end_collision 2.9 s (at 3.0 s, 42 mm)** *(excluded)* |
| `yingqing_0_95_95_t32-36_shift` | B | 27_yingqing_0_95_95 31.9–35.9 s | 18.8 / 10.7 | 35 / 17 | head at limit 48%; shoulder at limit 98%; **upper-arm twist at limit 62%**; **ground IK failed 1 frames**; **joint jump 0.81 rad (Left_Elbow_Yaw at 1.5 s)**; **root turn 19 deg/frame**; **trunk leans 18 deg (median)**; **foot held 39 mm off the floor (median)** *(excluded)* |
| `yingqing_0_95_95_t32-43` | A | 27_yingqing_0_95_95 32.4–43.0 s | 6.0 / 1.7 | 57 / 20 | head at limit 32%; shoulder at limit 49%; upper-arm twist at limit 39%; **ground IK failed 2 frames**; outlier arms k1 cm (z +3.5); **joint jump 0.96 rad (Left_Elbow_Pitch at 5.3 s)**; **root turn 19 deg/frame** *(excluded)* |
| `yingqing_0_95_95_t44-53` | A | 27_yingqing_0_95_95 44.1–53.0 s | 1.2 / 0.5 | 22 / 12 | **joint jump 0.76 rad (Right_Shoulder_Roll at 8.7 s)**; **root turn 6 deg/frame**; **self-collision right_hand_end_collision / trunk_collision 0.1 s (at 8.2 s, 54 mm)** *(excluded)* |
| `yingqing_1_1_1_t117-124` | A | 27_yingqing_1_1_1 117.0–123.8 s | 8.7 / 2.0 | 27 / 8 | **ground IK failed 7 frames** *(excluded)* |
| `yingqing_1_1_1_t125-133` | A | 27_yingqing_1_1_1 124.6–133.3 s | 3.0 / 2.1 | 13 / 4 | **foot held 32 mm off the floor (median)** *(excluded)* |
| `yingqing_1_1_1_t286-300` | A | 27_yingqing_1_1_1 285.7–300.3 s | 0.5 / 0.6 | 17 / 4 | shoulder at limit 100%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `yingqing_1_1_1_t322-329_shift` | B | 27_yingqing_1_1_1 321.8–329.4 s | 8.9 / 1.8 | 28 / 8 | leg at limit 32%; **ground IK failed 65 frames**; outlier knee max (z +7.2); **foot held 34 mm off the floor (median)** *(excluded)* |
| `yingqing_1_1_1_t351-355` | A | 27_yingqing_1_1_1 351.3–355.3 s | 1.0 / 1.0 | 1 / 2 | shoulder at limit 100%; **left arm behind body 14 cm (human's in front)** *(excluded)* |
| `yingqing_1_1_1_t359-365` | A | 27_yingqing_1_1_1 359.0–364.9 s | 5.4 / 0.8 | 3 / 1 | shoulder at limit 100%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `yingqing_1_1_1_t363-370_shift` | B | 27_yingqing_1_1_1 362.9–370.4 s | 20.0 / 10.6 | 19 / 4 | head at limit 41%; shoulder at limit 100%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `yingqing_1_1_1_t464-469_shift` | B | 27_yingqing_1_1_1 463.9–469.4 s | 17.5 / 8.7 | 20 / 5 | leg at limit 38%; **ground IK failed 58 frames**; outlier knee max (z +8.0) *(excluded)* |
| `yingqing_1_1_1_t467-474` | A | 27_yingqing_1_1_1 467.4–473.9 s | 1.0 / 1.3 | 13 / 6 | knee 65 deg; leg at limit 61%; **ground IK failed 80 frames**; outlier knee max (z +9.7); **trunk leans 17 deg (median)**; **foot held 51 mm off the floor (median)** *(excluded)* |
| `yingqing_1_1_1_t470-474_shift` | B | 27_yingqing_1_1_1 470.4–474.4 s | 13.8 / 4.9 | 16 / 8 | shoulder at limit 100%; leg at limit 89%; **ground IK failed 107 frames**; outlier knee max (z +7.7); **foot held 59 mm off the floor (median)**; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `yingqing_1_1_1_t475-481_shift` | B | 27_yingqing_1_1_1 475.1–480.8 s | 18.9 / 7.1 | 31 / 9 | knee 61 deg; leg at limit 16%; **ground IK failed 14 frames**; outlier knee max (z +8.4) *(excluded)* |
| `yingqing_1_1_1_t481-495` | A | 27_yingqing_1_1_1 481.3–495.2 s | 1.4 / 0.9 | 23 / 7 | shoulder at limit 95%; **joint jump 1.44 rad (Left_Shoulder_Pitch at 13.6 s)**; **root jump 3.8 cm/frame**; **root turn 33 deg/frame**; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `yingqing_1_1_1_t496-501_shift` | B | 27_yingqing_1_1_1 495.9–500.8 s | 19.0 / 4.4 | 36 / 11 | leg at limit 22%; **ground IK failed 31 frames**; outlier knee max (z +6.9) *(excluded)* |
| `yingqing_1_1_1_t515-529` | A | 27_yingqing_1_1_1 514.7–528.9 s | 1.0 / 1.2 | 9 / 3 | head at limit 46%; shoulder at limit 74%; **left arm behind body 14 cm (human's in front)** *(excluded)* |
| `yingqing_1_1_1_t72-83` | A | 27_yingqing_1_1_1 72.3–83.0 s | 9.3 / 1.6 | 12 / 4 | **ground IK failed 3 frames**; outlier knee max (z +4.1) *(excluded)* |
| `yingqing_1_1_1_t81-87_shift` | B | 27_yingqing_1_1_1 81.0–87.3 s | 10.6 / 1.7 | 12 / 6 | leg at limit 25%; **ground IK failed 44 frames**; outlier knee max (z +4.1) *(excluded)* |
| `yingqing_1_2_2_t102-109_shift` | B | 27_yingqing_1_2_2 101.6–108.5 s | 13.9 / 3.0 | 8 / 3 | leg at limit 18%; **ground IK failed 35 frames** *(excluded)* |
| `yingqing_1_2_2_t110-119_shift` | B | 27_yingqing_1_2_2 110.5–118.8 s | 11.9 / 2.7 | 12 / 5 | leg at limit 6%; **ground IK failed 7 frames**; outlier knee max (z +3.5) *(excluded)* |
| `yingqing_1_2_2_t135-141_shift` | B | 27_yingqing_1_2_2 134.8–141.0 s | 16.0 / 7.6 | 15 / 4 | leg at limit 16%; **ground IK failed 6 frames**; outlier knee max (z +5.1) *(excluded)* |
| `yingqing_1_2_2_t139-150` | A | 27_yingqing_1_2_2 139.0–150.3 s | 8.0 / 5.6 | 16 / 6 | leg at limit 9%; **ground IK failed 2 frames**; outlier knee max (z +4.6) *(excluded)* |
| `yingqing_1_2_2_t201-206_shift` | B | 27_yingqing_1_2_2 201.1–206.2 s | 21.4 / 8.7 | 30 / 9 | leg at limit 24%; **ground IK failed 29 frames**; outlier knee max (z +7.5); **foot held 35 mm off the floor (median)** *(excluded)* |
| `yingqing_1_2_2_t207-211_shift` | B | 27_yingqing_1_2_2 206.7–211.3 s | 15.5 / 11.1 | 35 / 10 | trunk drop 6 cm; knee 68 deg; leg at limit 46%; **ground IK failed 54 frames**; **outlier trunk drop (z +6.6)**; outlier knee max (z +10.7); **foot held 48 mm off the floor (median)** *(excluded)* |
| `yingqing_1_2_2_t209-221` | A | 27_yingqing_1_2_2 209.3–221.2 s | 3.3 / 1.0 | 30 / 9 | shoulder at limit 39%; **self-collision left_hand_collision / right_hand_end_collision 1.6 s (at 10.1 s, 40 mm)** *(excluded)* |
| `yingqing_1_2_2_t218-222_shift` | B | 27_yingqing_1_2_2 218.4–222.4 s | 25.6 / 13.5 | 13 / 5 | human steps; shoulder at limit 58%; outlier knee max (z +5.4); **self-collision left_hand_collision / right_hand_end_collision 1.6 s (at 1.1 s, 40 mm)** *(excluded)* |
| `yingqing_1_2_2_t236-240` | A | 27_yingqing_1_2_2 236.1–240.2 s | 2.5 / 0.7 | 21 / 7 | leg at limit 96%; **ground IK failed 109 frames**; **foot held 48 mm off the floor (median)** *(excluded)* |
| `yingqing_1_2_2_t238-243_shift` | B | 27_yingqing_1_2_2 238.2–242.7 s | 8.5 / 5.3 | 21 / 6 | leg at limit 46%; **ground IK failed 62 frames**; outlier knee max (z +5.2) *(excluded)* |
| `yingqing_1_2_2_t268-273_shift` | B | 27_yingqing_1_2_2 267.9–272.9 s | 11.6 / 2.1 | 15 / 6 | leg at limit 21%; **ground IK failed 23 frames**; outlier knee max (z +5.9) *(excluded)* |
| `yingqing_1_2_2_t277-282_shift` | B | 27_yingqing_1_2_2 276.7–282.2 s | 17.6 / 6.4 | 17 / 4 | leg at limit 35%; **ground IK failed 58 frames**; outlier knee max (z +7.1) *(excluded)* |
| `yingqing_1_2_2_t368-379` | A | 27_yingqing_1_2_2 367.9–379.1 s | 0.5 / 1.0 | 6 / 2 | head at limit 24%; shoulder at limit 100%; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `yingqing_1_2_2_t384-388_shift` | B | 27_yingqing_1_2_2 383.7–388.4 s | 10.6 / 2.2 | 10 / 3 | leg at limit 44%; **ground IK failed 58 frames**; outlier knee max (z +7.7) *(excluded)* |
| `yingqing_1_2_2_t386-395` | A | 27_yingqing_1_2_2 386.4–394.6 s | 9.5 / 2.9 | 13 / 4 | leg at limit 47%; **ground IK failed 107 frames**; outlier knee max (z +7.7) *(excluded)* |
| `yingqing_1_2_2_t422-426_shift` | B | 27_yingqing_1_2_2 421.7–426.1 s | 8.1 / 1.8 | 9 / 3 | leg at limit 49%; **ground IK failed 63 frames**; outlier knee max (z +4.8); **foot held 44 mm off the floor (median)** *(excluded)* |
| `yingqing_1_2_2_t424-430` | A | 27_yingqing_1_2_2 424.1–430.3 s | 9.9 / 2.2 | 13 / 4 | leg at limit 84%; **ground IK failed 152 frames**; outlier knee max (z +6.4); **foot held 49 mm off the floor (median)** *(excluded)* |
| `yingqing_1_2_2_t436-440_shift` | B | 27_yingqing_1_2_2 435.6–440.3 s | 11.4 / 2.7 | 9 / 3 | leg at limit 25%; **ground IK failed 30 frames**; outlier trunk drop (z +3.6); outlier knee max (z +6.5); **foot held 37 mm off the floor (median)** *(excluded)* |
| `yingqing_1_2_2_t444-460` | A | 27_yingqing_1_2_2 443.9–460.0 s | 0.7 / 0.4 | 14 / 4 | **root turn 7 deg/frame**; self-collision left_hand_end_collision / right_hand_end_collision 0.6 s (at 0.6 s, 7 mm) *(excluded)* |
| `yingqing_1_2_2_t460-473` | A | 27_yingqing_1_2_2 460.5–472.9 s | 9.7 / 2.9 | 18 / 5 | leg at limit 22%; **ground IK failed 86 frames**; outlier knee max (z +4.8) *(excluded)* |
| `yingqing_1_2_2_t5-13_shift` | B | 27_yingqing_1_2_2 4.8–13.0 s | 15.2 / 8.5 | 23 / 7 | elbow bend at limit 17%; **ground IK failed 6 frames**; outlier knee max (z +5.8) *(excluded)* |
| `yingqing_1_2_2_t58-63_shift` | B | 27_yingqing_1_2_2 58.0–62.6 s | 7.3 / 1.9 | 21 / 8 | leg at limit 48%; **ground IK failed 65 frames**; outlier knee max (z +5.1); **foot held 39 mm off the floor (median)** *(excluded)* |
| `yingqing_1_2_2_t61-74` | A | 27_yingqing_1_2_2 60.6–73.7 s | 2.2 / 1.2 | 16 / 6 | leg at limit 28%; **ground IK failed 86 frames**; outlier knee max (z +5.4); **foot held 49 mm off the floor (median)** *(excluded)* |
| `yingqing_1_3_3_t102-108_shift` | B | 27_yingqing_1_3_3 101.8–108.4 s | 22.6 / 17.8 | 11 / 5 | leg at limit 32%; **ground IK failed 62 frames**; outlier knee max (z +6.8) *(excluded)* |
| `yingqing_1_3_3_t124-131_shift` | B | 27_yingqing_1_3_3 124.4–131.4 s | 16.2 / 6.2 | 20 / 6 | leg at limit 30%; **ground IK failed 62 frames**; outlier knee max (z +7.4) *(excluded)* |
| `yingqing_1_3_3_t162-166` | A | 27_yingqing_1_3_3 161.9–166.4 s | 4.4 / 4.2 | 12 / 3 | **foot held 31 mm off the floor (median)** *(excluded)* |
| `yingqing_1_3_3_t194-200_shift` | B | 27_yingqing_1_3_3 194.3–200.3 s | 19.7 / 10.8 | 25 / 8 | leg at limit 42%; **ground IK failed 75 frames**; **foot held 38 mm off the floor (median)** *(excluded)* |
| `yingqing_1_3_3_t198-206` | A | 27_yingqing_1_3_3 198.3–206.1 s | 8.9 / 2.7 | 18 / 7 | leg at limit 90%; **ground IK failed 209 frames**; outlier knee max (z +5.5); **foot held 57 mm off the floor (median)** *(excluded)* |
| `yingqing_1_3_3_t231-237_shift` | B | 27_yingqing_1_3_3 230.8–236.7 s | 18.5 / 8.5 | 27 / 7 | leg at limit 20%; **ground IK failed 34 frames**; outlier knee max (z +5.6) *(excluded)* |
| `yingqing_1_3_3_t260-267_shift` | B | 27_yingqing_1_3_3 259.8–266.9 s | 14.5 / 2.6 | 20 / 6 | leg at limit 78%; **ground IK failed 164 frames**; outlier knee max (z +7.0); **foot held 53 mm off the floor (median)** *(excluded)* |
| `yingqing_1_3_3_t261-266` | A | 27_yingqing_1_3_3 260.9–266.0 s | 2.1 / 0.5 | 22 / 7 | leg at limit 99%; **ground IK failed 135 frames**; outlier knee max (z +4.9); **foot held 53 mm off the floor (median)** *(excluded)* |
| `yingqing_1_3_3_t290-298` | A | 27_yingqing_1_3_3 289.9–298.3 s | 1.1 / 1.8 | 16 / 5 | shoulder at limit 27%; **trunk leans 17 deg (median)**; self-collision left_hand_end_collision / right_arm_3_collision 1.3 s (at 1.7 s, 21 mm) *(excluded)* |
| `yingqing_1_3_3_t296-301_shift` | B | 27_yingqing_1_3_3 296.3–301.4 s | 15.9 / 9.8 | 32 / 11 | shoulder at limit 64%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `yingqing_1_3_3_t395-400_shift` | B | 27_yingqing_1_3_3 394.9–399.5 s | 8.2 / 3.4 | 5 / 3 | shoulder at limit 98%; **left arm behind body 14 cm (human's in front)** *(excluded)* |
| `yingqing_1_3_3_t43-50` | A | 27_yingqing_1_3_3 43.2–49.5 s | 1.2 / 1.2 | 21 / 7 | leg at limit 25%; **self-collision left_foot_collision / right_foot_collision 6.4 s (at 0.0 s, 28 mm)**; **feet overlap 28 mm for 6.4 s (at 0.0 s)** *(excluded)* |
| `yingqing_1_3_3_t438-443_shift` | B | 27_yingqing_1_3_3 437.7–443.2 s | 11.8 / 4.4 | 6 / 3 | leg at limit 52%; **ground IK failed 84 frames**; outlier knee max (z +5.3); **foot held 46 mm off the floor (median)** *(excluded)* |
| `yingqing_1_3_3_t452-461` | A | 27_yingqing_1_3_3 452.3–460.9 s | 1.1 / 0.6 | 3 / 1 | shoulder at limit 98%; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `yingqing_1_3_3_t462-466_shift` | B | 27_yingqing_1_3_3 461.6–466.0 s | 22.4 / 14.3 | 30 / 8 | shoulder at limit 93%; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `yingqing_1_3_3_t464-483` | A | 27_yingqing_1_3_3 464.0–483.0 s | 4.5 / 3.4 | 31 / 13 | leg at limit 6%; **ground IK failed 26 frames** *(excluded)* |
| `yingqing_1_3_3_t5-19` | A | 27_yingqing_1_3_3 5.4–18.9 s | 0.8 / 0.8 | 13 / 3 | shoulder at limit 99%; **left arm behind body 16 cm (human's in front)** *(excluded)* |
| `yingqing_1_3_3_t508-513_shift` | B | 27_yingqing_1_3_3 508.4–512.6 s | 14.5 / 6.5 | 18 / 6 | leg at limit 46%; **ground IK failed 57 frames**; outlier knee max (z +3.8); **foot held 42 mm off the floor (median)** *(excluded)* |
| `yingqing_1_3_3_t51-56_shift` | B | 27_yingqing_1_3_3 51.4–56.1 s | 12.5 / 4.3 | 25 / 8 | knee 63 deg; **ground IK failed 3 frames**; outlier knee max (z +9.2) *(excluded)* |
| `yingqing_1_3_3_t522-526` | A | 27_yingqing_1_3_3 521.5–526.1 s | 4.0 / 1.1 | 14 / 8 | shoulder at limit 91%; **left arm behind body 11 cm (human's in front)** *(excluded)* |
| `yingqing_1_3_3_t54-62` | A | 27_yingqing_1_3_3 54.1–61.5 s | 9.9 / 3.2 | 15 / 6 | leg at limit 17%; **ground IK failed 35 frames**; outlier knee max (z +5.7) *(excluded)* |
| `yingqing_1_3_3_t552-564` | A | 27_yingqing_1_3_3 551.9–564.4 s | 1.7 / 1.9 | 42 / 15 | head at limit 28%; shoulder at limit 88%; upper-arm twist at limit 30%; outlier knee max (z +3.5); **joint jump 2.78 rad (Left_Shoulder_Roll at 7.4 s)**; **root turn 8 deg/frame**; **foot held 46 mm off the floor (median)** *(excluded)* |
| `yingqing_1_3_3_t562-568_shift` | B | 27_yingqing_1_3_3 562.4–567.7 s | 23.3 / 13.2 | 44 / 14 | head at limit 22%; shoulder at limit 39%; upper-arm twist at limit 18%; leg at limit 58%; **ground IK failed 52 frames**; outlier knee max (z +7.1); **root turn 7 deg/frame** *(excluded)* |
| `yingqing_1_3_3_t575-584_shift` | B | 27_yingqing_1_3_3 575.0–583.6 s | 21.1 / 14.1 | 26 / 9 | knee 67 deg; leg at limit 12%; **ground IK failed 23 frames**; outlier trunk drop (z +3.9); outlier knee max (z +10.5); self-collision left_hand_collision / right_hand_end_collision 1.3 s (at 6.3 s, 16 mm) *(excluded)* |
| `yingqing_1_3_3_t586-592` | A | 27_yingqing_1_3_3 585.9–591.6 s | 1.2 / 1.1 | 29 / 10 | shoulder at limit 91%; **joint jump 1.48 rad (Left_Shoulder_Pitch at 5.6 s)**; **root jump 3.5 cm/frame**; **root turn 30 deg/frame**; **left arm behind body 15 cm (human's in front)** *(excluded)* |
| `yingqing_1_3_3_t73-80` | A | 27_yingqing_1_3_3 73.0–80.1 s | 1.4 / 0.4 | 16 / 7 | leg at limit 29%; **self-collision left_foot_collision / right_foot_collision 7.1 s (at 0.0 s, 33 mm)**; **feet overlap 33 mm for 7.1 s (at 0.0 s)** *(excluded)* |
| `zhao_0_103_103_t27-34_shift` | B | 12_zhao_0_103_103 26.6–34.4 s | 25.0 / 12.5 | 51 / 17 | trunk drop 11 cm; knee 85 deg; shoulder at limit 59%; leg at limit 9%; **ground IK failed 12 frames**; **outlier trunk drop (z +13.6)**; outlier knee max (z +16.4); **self-collision left_hand_collision / trunk_collision 2.5 s (at 3.5 s, 26 mm)**; **foot held 38 mm off the floor (median)** *(excluded)* |
| `zhao_0_103_103_t34-39_shift` | B | 12_zhao_0_103_103 34.4–38.5 s | 14.0 / 6.6 | 62 / 18 | trunk drop 6 cm; knee 73 deg; **ground IK failed 1 frames**; **outlier trunk drop (z +7.2)**; outlier knee max (z +12.3) *(excluded)* |
| `zhao_0_103_103_t62-70_shift` | B | 12_zhao_0_103_103 62.0–70.1 s | 21.5 / 9.1 | 106 / 27 | trunk drop 11 cm; knee 78 deg; head at limit 51%; leg at limit 8%; **ground IK failed 17 frames**; outlier arms k1 cm (z +5.5); **outlier trunk drop (z +14.3)**; outlier knee max (z +14.0); **trunk leans 17 deg (median)** *(excluded)* |
| `zhao_0_104_104_t24-36_shift` | B | 12_zhao_0_104_104 23.9–36.1 s | 16.2 / 9.8 | 36 / 13 | trunk drop 9 cm; knee 75 deg; head at limit 9%; shoulder at limit 53%; elbow bend at limit 17%; **outlier trunk drop (z +10.7)**; outlier knee max (z +13.1); self-collision left_hand_collision / trunk_collision 0.4 s (at 3.0 s, 9 mm) *(excluded)* |
| `zhao_0_104_104_t36-48_shift` | B | 12_zhao_0_104_104 36.1–48.3 s | 22.3 / 10.7 | 35 / 12 | trunk drop 6 cm; knee 66 deg; **outlier trunk drop (z +6.8)**; outlier knee max (z +10.0); self-collision left_hand_collision / trunk_collision 0.7 s (at 6.8 s, 21 mm) *(excluded)* |
| `zhao_0_104_104_t55-63_shift` | B | 12_zhao_0_104_104 54.6–62.8 s | 16.7 / 8.7 | 39 / 11 | head at limit 8%; shoulder at limit 6%; **ground IK failed 3 frames**; outlier knee max (z +6.5); self-collision left_hand_collision / trunk_collision 0.8 s (at 7.5 s, 18 mm) *(excluded)* |
| `zhao_0_10_10_t35-39_shift` | B | 12_zhao_0_10_10 35.1–39.4 s | 10.1 / 3.9 | 26 / 10 | leg at limit 14%; **ground IK failed 8 frames** *(excluded)* |
| `zhao_0_111_111_t63-70_shift` | B | 12_zhao_0_111_111 63.3–70.2 s | 21.9 / 12.5 | 88 / 21 | knee 62 deg; head at limit 19%; leg at limit 18%; **ground IK failed 31 frames**; outlier arms k1 cm (z +3.8); outlier trunk drop (z +4.0); outlier knee max (z +8.7) *(excluded)* |
| `zhao_0_11_11_t20-27_shift` | B | 12_zhao_0_11_11 19.6–27.1 s | 14.6 / 7.7 | 40 / 11 | leg at limit 10%; **ground IK failed 14 frames** *(excluded)* |
| `zhao_0_11_11_t35-43_shift` | B | 12_zhao_0_11_11 34.9–43.0 s | 18.1 / 9.0 | 64 / 15 | leg at limit 14%; **ground IK failed 30 frames**; **left foot slides > 1 cm/frame for 0.17 s (at 5.2 s)** *(excluded)* |
| `zhao_0_11_11_t4-10_shift` | B | 12_zhao_0_11_11 3.8–9.9 s | 12.3 / 6.9 | 65 / 14 | leg at limit 5%; **ground IK failed 2 frames** *(excluded)* |
| `zhao_0_11_11_t41-46` | A | 12_zhao_0_11_11 41.0–46.3 s | 9.3 / 3.2 | 45 / 11 | leg at limit 21%; **ground IK failed 32 frames** *(excluded)* |
| `zhao_0_11_11_t44-58_shift` | B | 12_zhao_0_11_11 44.3–58.1 s | 16.4 / 8.7 | 58 / 16 | leg at limit 8%; **ground IK failed 32 frames**; outlier knee max (z +4.7) *(excluded)* |
| `zhao_0_11_11_t58-72_shift` | B | 12_zhao_0_11_11 58.1–71.8 s | 17.5 / 8.9 | 52 / 13 | leg at limit 8%; **ground IK failed 17 frames**; outlier knee max (z +3.6) *(excluded)* |
| `zhao_0_11_11_t8-16` | A | 12_zhao_0_11_11 7.9–15.7 s | 8.1 / 4.6 | 48 / 11 | leg at limit 7%; **ground IK failed 12 frames** *(excluded)* |
| `zhao_0_12_12_t0-9_shift` | B | 12_zhao_0_12_12 0.0–8.8 s | 24.2 / 12.9 | 73 / 15 | leg at limit 6%; **ground IK failed 10 frames**; outlier knee max (z +4.3) *(excluded)* |
| `zhao_0_12_12_t25-30_shift` | B | 12_zhao_0_12_12 25.4–30.2 s | 9.1 / 3.4 | 67 / 19 | shoulder at limit 17%; leg at limit 26%; **ground IK failed 26 frames**; outlier knee max (z +3.7) *(excluded)* |
| `zhao_0_12_12_t80-84` | A | 12_zhao_0_12_12 79.8–83.8 s | 1.3 / 0.9 | 72 / 20 | shoulder at limit 13%; outlier arms k1 cm (z +3.6); **self-collision head_2_collision / right_hand_end_collision 1.4 s (at 2.6 s, 53 mm)** *(excluded)* |
| `zhao_0_13_13_t0-5` | A | 12_zhao_0_13_13 0.0–5.1 s | 8.0 / 5.2 | 46 / 19 | head at limit 5%; shoulder at limit 42%; upper-arm twist at limit 44%; **joint jump 0.92 rad (Right_Elbow_Pitch at 3.3 s)**; **root turn 20 deg/frame**; **self-collision head_2_collision / right_hand_end_collision 0.6 s (at 0.1 s, 41 mm)** *(excluded)* |
| `zhao_0_13_13_t12-19_shift` | B | 12_zhao_0_13_13 11.8–19.3 s | 11.9 / 6.1 | 53 / 13 | leg at limit 8%; **ground IK failed 8 frames**; outlier knee max (z +4.2) *(excluded)* |
| `zhao_0_13_13_t17-21` | A | 12_zhao_0_13_13 17.3–21.5 s | 6.6 / 2.0 | 58 / 13 | leg at limit 14%; **ground IK failed 8 frames**; **joint jump 0.60 rad (Left_Knee_Pitch at 0.1 s)** *(excluded)* |
| `zhao_0_13_13_t22-30` | A | 12_zhao_0_13_13 22.5–29.5 s | 9.7 / 4.4 | 56 / 14 | leg at limit 7%; **ground IK failed 12 frames** *(excluded)* |
| `zhao_0_13_13_t33-46_shift` | B | 12_zhao_0_13_13 32.9–46.3 s | 21.3 / 11.7 | 84 / 24 | **ground IK failed 8 frames**; outlier arms k1 cm (z +4.8); **joint jump 0.97 rad (Right_Shoulder_Roll at 8.5 s)**; **root jump 4.1 cm/frame**; **root turn 24 deg/frame**; **foot held 32 mm off the floor (median)** *(excluded)* |
| `zhao_0_13_13_t52-63` | A | 12_zhao_0_13_13 51.7–62.5 s | 7.5 / 4.5 | 47 / 12 | **ground IK failed 12 frames** *(excluded)* |
| `zhao_0_13_13_t75-81_shift` | B | 12_zhao_0_13_13 75.1–80.8 s | 15.4 / 8.2 | 62 / 18 | **self-collision head_2_collision / right_hand_end_collision 0.7 s (at 4.9 s, 35 mm)** *(excluded)* |
| `zhao_0_13_13_t8-14` | A | 12_zhao_0_13_13 8.5–13.8 s | 8.1 / 1.4 | 42 / 11 | leg at limit 17%; **ground IK failed 19 frames** *(excluded)* |
| `zhao_0_14_14_t0-6` | A | 12_zhao_0_14_14 0.0–6.5 s | 1.7 / 1.7 | 30 / 12 | shoulder at limit 8%; **joint jump 1.40 rad (Left_Elbow_Pitch at 6.0 s)**; **root jump 4.7 cm/frame**; **root turn 21 deg/frame**; **left arm behind body 12 cm (human's in front)**; right arm behind body 8 cm (human's in front) *(excluded)* |
| `zhao_0_14_14_t11-17_shift` | B | 12_zhao_0_14_14 11.1–16.5 s | 19.5 / 10.1 | 60 / 15 | leg at limit 8%; **ground IK failed 11 frames**; outlier knee max (z +3.7) *(excluded)* |
| `zhao_0_14_14_t4-10_shift` | B | 12_zhao_0_14_14 4.5–9.5 s | 10.9 / 1.9 | 59 / 20 | shoulder at limit 10%; outlier arms k1 cm (z +3.6); **joint jump 1.40 rad (Left_Elbow_Pitch at 1.5 s)**; **root jump 4.7 cm/frame**; **root turn 21 deg/frame**; hand presses into leg 34 mm for 0.1 s (at 2.7 s) *(excluded)* |
| `zhao_0_14_14_t52-57` | A | 12_zhao_0_14_14 52.3–57.0 s | 2.8 / 0.7 | 18 / 8 | leg at limit 8%; **ground IK failed 7 frames** *(excluded)* |
| `zhao_0_14_14_t58-64_shift` | B | 12_zhao_0_14_14 58.3–64.3 s | 13.9 / 8.5 | 52 / 14 | leg at limit 14%; **ground IK failed 16 frames**; **joint jump 0.61 rad (Left_Knee_Pitch at 2.3 s)** *(excluded)* |
| `zhao_0_14_14_t69-73_shift` | B | 12_zhao_0_14_14 69.3–73.3 s | 12.3 / 6.7 | 53 / 14 | leg at limit 17%; **ground IK failed 15 frames**; **joint jump 0.61 rad (Left_Knee_Pitch at 3.4 s)** *(excluded)* |
| `zhao_0_14_14_t71-78` | A | 12_zhao_0_14_14 70.9–78.3 s | 9.0 / 5.1 | 43 / 12 | leg at limit 14%; **ground IK failed 15 frames**; **joint jump 0.60 rad (Left_Knee_Pitch at 1.9 s)**; hand presses into leg 25 mm for 0.5 s (at 3.2 s) *(excluded)* |
| `zhao_0_15_15_t16-21_shift` | B | 12_zhao_0_15_15 15.6–20.7 s | 11.2 / 7.0 | 64 / 18 | leg at limit 17%; **ground IK failed 24 frames** *(excluded)* |
| `zhao_0_15_15_t22-30` | A | 12_zhao_0_15_15 21.8–30.1 s | 6.1 / 3.6 | 57 / 14 | **ground IK failed 1 frames** *(excluded)* |
| `zhao_0_15_15_t38-46_shift` | B | 12_zhao_0_15_15 38.2–46.2 s | 18.7 / 10.5 | 50 / 13 | leg at limit 7%; **ground IK failed 16 frames**; outlier knee max (z +3.8) *(excluded)* |
| `zhao_0_16_16_t0-14` | A | 12_zhao_0_16_16 0.0–14.0 s | 6.7 / 2.3 | 47 / 12 | leg at limit 6%; **ground IK failed 20 frames** *(excluded)* |
| `zhao_0_16_16_t12-28_shift` | B | 12_zhao_0_16_16 12.0–27.5 s | 23.8 / 12.8 | 71 / 21 | leg at limit 9%; **ground IK failed 36 frames**; outlier arms k1 cm (z +3.8); outlier knee max (z +4.8) *(excluded)* |
| `zhao_0_16_16_t35-41` | A | 12_zhao_0_16_16 35.1–40.7 s | 8.2 / 2.8 | 47 / 15 | leg at limit 9%; **ground IK failed 5 frames**; hand presses into leg 17 mm for 0.1 s (at 1.8 s) *(excluded)* |
| `zhao_0_16_16_t39-46_shift` | B | 12_zhao_0_16_16 38.7–46.5 s | 24.7 / 14.0 | 64 / 18 | knee 60 deg; shoulder at limit 18%; leg at limit 10%; **ground IK failed 22 frames**; outlier knee max (z +8.1) *(excluded)* |
| `zhao_0_2_2_t13-19` | A | 12_zhao_0_2_2 12.8–19.4 s | 8.9 / 5.6 | 50 / 12 | leg at limit 6%; **ground IK failed 4 frames** *(excluded)* |
| `zhao_0_2_2_t65-69` | A | 12_zhao_0_2_2 64.7–69.1 s | 9.1 / 3.5 | 31 / 13 | leg at limit 21%; **ground IK failed 26 frames** *(excluded)* |
| `zhao_0_3_3_t9-15_shift` | B | 12_zhao_0_3_3 9.1–15.4 s | 11.5 / 5.7 | 57 / 13 | leg at limit 7%; **ground IK failed 4 frames** *(excluded)* |
| `zhao_0_66_66_t15-19_shift` | B | 12_zhao_0_66_66 15.1–19.2 s | 21.3 / 10.5 | 77 / 19 | leg at limit 11%; **ground IK failed 8 frames**; outlier knee max (z +4.4); **joint jump 0.60 rad (Left_Knee_Pitch at 2.0 s)** *(excluded)* |
| `zhao_0_7_7_t0-7` | A | 12_zhao_0_7_7 0.0–6.6 s | 8.2 / 3.5 | 41 / 12 | leg at limit 8%; **ground IK failed 13 frames** *(excluded)* |
| `zhao_0_7_7_t5-10_shift` | B | 12_zhao_0_7_7 4.6–9.6 s | 18.5 / 9.3 | 65 / 21 | leg at limit 7%; **ground IK failed 11 frames**; outlier arms k1 cm (z +3.8) *(excluded)* |
| `zhao_0_81_81_t20-29_shift` | B | 12_zhao_0_81_81 20.0–29.1 s | 15.9 / 11.2 | 28 / 9 | outlier knee max (z +6.3); **left foot slides > 1 cm/frame for 0.10 s (at 0.7 s)**; self-collision left_hand_collision / trunk_collision 1.1 s (at 6.3 s, 16 mm) *(excluded)* |
| `zhao_0_87_87_t46-54_shift` | B | 12_zhao_0_87_87 46.2–53.5 s | 18.4 / 9.5 | 42 / 12 | **ground IK failed 7 frames**; outlier knee max (z +3.9); self-collision left_hand_collision / trunk_collision 0.5 s (at 5.2 s, 18 mm) *(excluded)* |
| `zhao_1_1_1_t20-29` | A | 12_zhao_1_1_1 19.8–29.2 s | 10.0 / 3.5 | 25 / 7 | shoulder at limit 24%; leg at limit 10%; **ground IK failed 26 frames** *(excluded)* |
| `zhao_1_1_1_t206-212` | A | 12_zhao_1_1_1 206.2–211.6 s | 9.4 / 3.4 | 43 / 12 | shoulder at limit 17%; leg at limit 18%; **ground IK failed 27 frames** *(excluded)* |
| `zhao_1_1_1_t382-387` | A | 12_zhao_1_1_1 381.5–386.9 s | 7.8 / 3.8 | 37 / 11 | head at limit 36%; shoulder at limit 45%; upper-arm twist at limit 21%; **root turn 7 deg/frame** *(excluded)* |
| `zhao_1_1_1_t535-546_shift` | B | 12_zhao_1_1_1 534.9–545.7 s | 24.8 / 13.9 | 40 / 12 | shoulder at limit 48%; **ground IK failed 6 frames**; outlier knee max (z +7.1) *(excluded)* |
| `zhao_1_2_2_t268-286` | A | 12_zhao_1_2_2 267.7–286.0 s | 1.5 / 2.5 | 36 / 10 | **upper-arm twist at limit 62%**; **root turn 16 deg/frame** *(excluded)* |
| `zhao_1_2_2_t286-304` | A | 12_zhao_1_2_2 286.0–304.3 s | 4.1 / 1.8 | 32 / 9 | **root turn 17 deg/frame** *(excluded)* |
| `zhao_1_3_3_t58-75` | A | 12_zhao_1_3_3 57.5–74.6 s | 1.7 / 2.1 | 52 / 18 | shoulder at limit 8%; upper-arm twist at limit 33%; **ground IK failed 8 frames**; **joint jump 0.97 rad (Right_Elbow_Pitch at 12.6 s)**; **root turn 18 deg/frame** *(excluded)* |
| `ayana_0_103_103_t18-22_shift` | B | 21_ayana_0_103_103 18.4–22.4 s | 10.7 / 5.3 | 7 / 3 | outlier knee max (z +4.1) |
| `ayana_0_103_103_t42-46_shift` | B | 21_ayana_0_103_103 41.8–46.3 s | 12.4 / 6.7 | 16 / 6 | outlier knee max (z +4.3) |
| `ayana_0_103_103_t50-59_shift` | B | 21_ayana_0_103_103 49.7–59.4 s | 17.8 / 8.0 | 19 / 8 | head at limit 17%; outlier knee max (z +5.9) |
| `ayana_0_103_103_t69-74_shift` | B | 21_ayana_0_103_103 69.3–73.8 s | 11.8 / 7.1 | 21 / 11 | head at limit 22%; outlier knee max (z +5.5) |
| `ayana_0_10_10_t31-46` | A | 21_ayana_0_10_10 30.9–46.3 s | 0.3 / 0.2 | 15 / 5 | elbow bend at limit 11% |
| `ayana_0_11_11_t4-10_shift` | B | 21_ayana_0_11_11 3.8–10.0 s | 20.8 / 10.9 | 36 / 12 | outlier knee max (z +6.0) |
| `ayana_0_11_11_t54-69` | A | 21_ayana_0_11_11 53.6–68.7 s | 0.8 / 1.1 | 23 / 8 | head at limit 10% |
| `ayana_0_11_11_t66-70_shift` | B | 21_ayana_0_11_11 65.8–69.8 s | 16.0 / 8.2 | 37 / 12 | head at limit 6% |
| `ayana_0_12_12_t0-17` | A | 21_ayana_0_12_12 0.0–17.0 s | 0.8 / 0.5 | 31 / 12 | head at limit 7%; elbow bend at limit 17% |
| `ayana_0_12_12_t32-37_shift` | B | 21_ayana_0_12_12 31.9–36.9 s | 24.0 / 12.2 | 31 / 11 | shoulder at limit 27%; outlier knee max (z +6.8) |
| `ayana_0_12_12_t35-49` | A | 21_ayana_0_12_12 34.9–49.4 s | 0.8 / 0.8 | 18 / 7 | shoulder at limit 34% |
| `ayana_0_12_12_t65-70_shift` | B | 21_ayana_0_12_12 65.1–70.0 s | 23.3 / 12.3 | 45 / 15 | outlier knee max (z +5.9) |
| `ayana_0_12_12_t68-86` | A | 21_ayana_0_12_12 68.0–85.8 s | 8.7 / 3.7 | 33 / 9 | elbow bend at limit 10% |
| `ayana_0_13_13_t32-48` | A | 21_ayana_0_13_13 32.2–48.4 s | 1.5 / 1.0 | 29 / 7 | head at limit 7%; shoulder at limit 9% |
| `ayana_0_13_13_t46-51_shift` | B | 21_ayana_0_13_13 46.4–51.3 s | 18.8 / 10.5 | 72 / 18 | head at limit 25%; shoulder at limit 28%; outlier knee max (z +6.4) |
| `ayana_0_13_13_t49-65` | A | 21_ayana_0_13_13 49.3–65.1 s | 0.7 / 0.3 | 37 / 10 | head at limit 6% |
| `ayana_0_14_14_t0-17` | A | 21_ayana_0_14_14 0.0–17.2 s | 0.5 / 0.3 | 21 / 7 | head at limit 6% |
| `ayana_0_14_14_t17-34` | A | 21_ayana_0_14_14 17.2–34.5 s | 2.0 / 1.1 | 23 / 7 | elbow bend at limit 23% |
| `ayana_0_14_14_t57-64_shift` | B | 21_ayana_0_14_14 57.3–63.9 s | 20.1 / 10.5 | 24 / 5 | outlier knee max (z +4.1) |
| `ayana_0_14_14_t67-71_shift` | B | 21_ayana_0_14_14 67.4–71.4 s | 21.0 / 10.0 | 27 / 6 | outlier knee max (z +5.1) |
| `ayana_0_15_15_t32-37_shift` | B | 21_ayana_0_15_15 32.2–37.1 s | 22.6 / 11.6 | 25 / 7 | outlier knee max (z +4.3) |
| `ayana_0_16_16_t28-38_shift` | B | 21_ayana_0_16_16 28.5–37.7 s | 15.3 / 7.4 | 29 / 8 | outlier knee max (z +5.1) |
| `ayana_0_16_16_t50-69` | A | 21_ayana_0_16_16 49.6–69.1 s | 7.1 / 3.5 | 26 / 8 | elbow bend at limit 8% |
| `ayana_0_16_16_t75-80` | A | 21_ayana_0_16_16 75.3–80.2 s | 0.6 / 0.5 | 21 / 7 | outlier knee max (z -3.8) |
| `ayana_0_65_65_t14-20_shift` | B | 21_ayana_0_65_65 14.4–19.5 s | 20.5 / 12.0 | 38 / 14 | head at limit 36%; outlier knee max (z +4.4) |
| `ayana_0_65_65_t22-31` | A | 21_ayana_0_65_65 22.5–31.1 s | 2.5 / 1.5 | 29 / 12 | head at limit 39%; elbow bend at limit 7%; outlier trunk drop (z +4.3); hand presses into leg 12 mm for 0.6 s (at 0.6 s) |
| `ayana_0_73_73_t47-51_shift` | B | 21_ayana_0_73_73 46.8–50.8 s | 21.4 / 10.3 | 47 / 21 | head at limit 14%; outlier arms k1 cm (z +4.0); outlier knee max (z +6.5) |
| `ayana_0_81_81_t0-16` | A | 21_ayana_0_81_81 0.0–15.9 s | 0.4 / 0.7 | 24 / 8 | head at limit 8% |
| `ayana_0_81_81_t16-32` | A | 21_ayana_0_81_81 15.9–31.9 s | 0.9 / 0.5 | 30 / 10 | head at limit 13%; elbow bend at limit 9% |
| `ayana_0_81_81_t32-48` | A | 21_ayana_0_81_81 31.9–47.8 s | 2.1 / 0.7 | 27 / 10 | head at limit 24% |
| `ayana_0_81_81_t48-64` | A | 21_ayana_0_81_81 47.8–63.8 s | 0.7 / 0.4 | 26 / 9 | head at limit 8% |
| `ayana_0_87_87_t10-18_shift` | B | 21_ayana_0_87_87 10.1–18.5 s | 14.6 / 8.6 | 11 / 4 | outlier knee max (z +4.7) |
| `ayana_0_95_95_t3-8_shift` | B | 21_ayana_0_95_95 3.5–7.9 s | 5.9 / 3.1 | 24 / 15 | head at limit 10% |
| `ayana_0_95_95_t38-51` | A | 21_ayana_0_95_95 37.5–51.1 s | 5.0 / 1.0 | 37 / 13 | head at limit 11% |
| `ayana_0_95_95_t6-21` | A | 21_ayana_0_95_95 5.9–21.1 s | 3.2 / 2.1 | 28 / 13 | head at limit 9%; outlier trunk drop (z +4.2); outlier knee max (z +3.5) |
| `ayana_1_10_10_t109-127` | A | 21_ayana_1_10_10 109.3–127.2 s | 3.1 / 1.2 | 19 / 6 | shoulder at limit 23% |
| `ayana_1_10_10_t178-194` | A | 21_ayana_1_10_10 177.6–193.8 s | 0.6 / 0.4 | 23 / 8 | shoulder at limit 26% |
| `ayana_1_10_10_t208-212_shift` | B | 21_ayana_1_10_10 208.1–212.4 s | 6.1 / 3.5 | 28 / 10 | leg at limit 6% |
| `ayana_1_10_10_t291-299_shift` | B | 21_ayana_1_10_10 290.7–298.6 s | 16.5 / 9.2 | 40 / 13 | outlier knee max (z +6.3) |
| `ayana_1_10_10_t316-336` | A | 21_ayana_1_10_10 316.3–336.0 s | 0.6 / 0.4 | 20 / 8 | shoulder at limit 9% |
| `ayana_1_10_10_t432-436_shift` | B | 21_ayana_1_10_10 432.0–436.4 s | 9.2 / 5.7 | 40 / 12 | outlier knee max (z +3.5) |
| `ayana_1_10_10_t434-442` | A | 21_ayana_1_10_10 434.4–441.6 s | 2.8 / 0.9 | 44 / 14 | outlier knee max (z +4.2) |
| `ayana_1_10_10_t440-444_shift` | B | 21_ayana_1_10_10 439.6–444.3 s | 16.7 / 8.2 | 76 / 23 | outlier arms k1 cm (z +4.3); outlier knee max (z +4.0) |
| `ayana_1_10_10_t538-544_shift` | B | 21_ayana_1_10_10 537.9–543.5 s | 20.5 / 10.5 | 16 / 5 | outlier knee max (z +7.8) |
| `ayana_1_10_10_t558-575` | A | 21_ayana_1_10_10 558.2–574.8 s | 3.4 / 1.4 | 27 / 11 | elbow bend at limit 26% |
| `ayana_1_10_10_t91-109` | A | 21_ayana_1_10_10 91.4–109.3 s | 0.6 / 1.1 | 22 / 7 | shoulder at limit 6%; upper-arm twist at limit 32% |
| `ayana_1_11_11_t0-18` | A | 21_ayana_1_11_11 0.0–18.2 s | 4.8 / 1.7 | 14 / 7 | elbow bend at limit 13% |
| `ayana_1_11_11_t141-145_shift` | B | 21_ayana_1_11_11 141.4–145.4 s | 26.4 / 12.0 | 20 / 7 | human steps; outlier knee max (z +7.8) |
| `ayana_1_11_11_t165-170_shift` | B | 21_ayana_1_11_11 165.3–169.9 s | 21.3 / 11.2 | 38 / 13 | elbow bend at limit 51% |
| `ayana_1_11_11_t168-180` | A | 21_ayana_1_11_11 167.9–180.4 s | 6.9 / 4.0 | 12 / 7 | elbow bend at limit 16% |
| `ayana_1_11_11_t193-205` | A | 21_ayana_1_11_11 193.2–205.0 s | 6.0 / 3.2 | 11 / 3 | shoulder at limit 47% |
| `ayana_1_11_11_t203-212_shift` | B | 21_ayana_1_11_11 203.0–212.3 s | 23.3 / 11.1 | 15 / 5 | shoulder at limit 17%; outlier knee max (z +5.6) |
| `ayana_1_11_11_t226-232_shift` | B | 21_ayana_1_11_11 226.0–231.5 s | 12.9 / 5.9 | 11 / 4 | outlier knee max (z +7.5) |
| `ayana_1_11_11_t249-269` | A | 21_ayana_1_11_11 249.1–268.7 s | 13.5 / 6.4 | 17 / 6 | human steps; outlier trunk drop (z +3.6); outlier knee max (z +5.7) |
| `ayana_1_11_11_t293-298_shift` | B | 21_ayana_1_11_11 292.6–297.7 s | 13.3 / 6.6 | 5 / 4 | outlier knee max (z +4.1) |
| `ayana_1_11_11_t311-318_shift` | B | 21_ayana_1_11_11 311.2–318.4 s | 12.2 / 5.8 | 14 / 5 | outlier knee max (z +4.3) |
| `ayana_1_11_11_t351-356_shift` | B | 21_ayana_1_11_11 351.0–355.6 s | 18.7 / 9.6 | 19 / 8 | outlier knee max (z +5.2) |
| `ayana_1_11_11_t357-361_shift` | B | 21_ayana_1_11_11 356.6–360.6 s | 21.6 / 10.3 | 45 / 12 | outlier trunk drop (z +4.2); outlier knee max (z +6.2) |
| `ayana_1_11_11_t358-372` | A | 21_ayana_1_11_11 358.3–372.0 s | 0.7 / 1.0 | 22 / 9 | outlier trunk drop (z +4.9); outlier knee max (z +6.1) |
| `ayana_1_11_11_t567-575_shift` | B | 21_ayana_1_11_11 567.3–574.7 s | 22.7 / 11.8 | 43 / 14 | outlier knee max (z +4.6) |
| `ayana_1_11_11_t89-96_shift` | B | 21_ayana_1_11_11 88.8–96.4 s | 19.2 / 10.0 | 28 / 11 | outlier knee max (z +6.6) |
| `ayana_1_12_12_t361-367_shift` | B | 21_ayana_1_12_12 361.4–367.3 s | 10.2 / 7.8 | 35 / 12 | outlier knee max (z +7.6) |
| `ayana_1_12_12_t378-386_shift` | B | 21_ayana_1_12_12 377.6–385.6 s | 16.9 / 5.0 | 14 / 6 | leg at limit 5%; outlier knee max (z +6.5) |
| `ayana_1_12_12_t532-537_shift` | B | 21_ayana_1_12_12 532.2–536.6 s | 10.0 / 7.6 | 35 / 15 | elbow bend at limit 7%; outlier knee max (z +5.5) |
| `ayana_1_12_12_t535-549` | A | 21_ayana_1_12_12 534.6–548.8 s | 9.8 / 7.1 | 17 / 8 | elbow bend at limit 6% |
| `ayana_1_1_1_t0-4_shift` | B | 21_ayana_1_1_1 0.0–4.0 s | 11.0 / 5.9 | 29 / 8 | outlier knee max (z +4.2) |
| `ayana_1_1_1_t142-146_shift` | B | 21_ayana_1_1_1 141.8–146.2 s | 16.1 / 8.1 | 8 / 4 | outlier knee max (z +5.0) |
| `ayana_1_1_1_t144-157` | A | 21_ayana_1_1_1 144.2–156.9 s | 10.0 / 5.7 | 13 / 7 | shoulder at limit 6% |
| `ayana_1_1_1_t170-184` | A | 21_ayana_1_1_1 170.3–183.8 s | 9.1 / 8.8 | 18 / 8 | K1 feet move 9 cm; elbow bend at limit 20% |
| `ayana_1_1_1_t184-188_shift` | B | 21_ayana_1_1_1 183.6–187.6 s | 19.5 / 11.7 | 19 / 9 | elbow bend at limit 21% |
| `ayana_1_1_1_t36-43_shift` | B | 21_ayana_1_1_1 35.9–42.6 s | 16.6 / 8.4 | 10 / 5 | outlier knee max (z +4.8) |
| `ayana_1_1_1_t625-633_shift` | B | 21_ayana_1_1_1 625.1–632.9 s | 18.1 / 9.0 | 16 / 6 | hand presses into leg 17 mm for 0.4 s (at 4.0 s) |
| `ayana_1_1_1_t649-666` | A | 21_ayana_1_1_1 648.7–666.4 s | 0.8 / 1.0 | 16 / 6 | shoulder at limit 10% |
| `ayana_1_1_1_t666-684` | A | 21_ayana_1_1_1 666.4–684.2 s | 2.3 / 3.6 | 26 / 10 | shoulder at limit 16% |
| `ayana_1_1_1_t684-702` | A | 21_ayana_1_1_1 684.2–702.0 s | 1.2 / 0.8 | 30 / 11 | shoulder at limit 8% |
| `ayana_1_1_1_t84-90_shift` | B | 21_ayana_1_1_1 84.3–90.0 s | 17.9 / 9.7 | 23 / 10 | outlier knee max (z +5.9) |
| `ayana_1_2_2_t20-39` | A | 21_ayana_1_2_2 19.7–39.5 s | 1.9 / 0.5 | 4 / 2 | outlier knee max (z +4.0) |
| `ayana_1_2_2_t205-223` | A | 21_ayana_1_2_2 205.4–222.9 s | 1.2 / 0.3 | 4 / 2 | elbow bend at limit 39%; self-collision head_2_collision / right_hand_end_collision 0.3 s (at 11.2 s, 6 mm) |
| `ayana_1_2_2_t223-240` | A | 21_ayana_1_2_2 222.9–240.4 s | 8.6 / 4.7 | 8 / 3 | outlier knee max (z +3.9) |
| `ayana_1_2_2_t238-244_shift` | B | 21_ayana_1_2_2 238.4–244.2 s | 19.4 / 9.8 | 9 / 4 | outlier knee max (z +6.9) |
| `ayana_1_2_2_t99-103_shift` | B | 21_ayana_1_2_2 99.3–103.3 s | 16.4 / 9.6 | 6 / 2 | outlier knee max (z +6.1) |
| `ayana_1_3_3_t0-4_shift` | B | 21_ayana_1_3_3 0.0–4.0 s | 19.4 / 10.2 | 34 / 10 | outlier trunk drop (z +4.7); outlier knee max (z +7.4) |
| `ayana_1_3_3_t115-134` | A | 21_ayana_1_3_3 114.9–133.7 s | 2.9 / 2.1 | 23 / 8 | shoulder at limit 5% |
| `ayana_1_3_3_t209-228` | A | 21_ayana_1_3_3 208.8–227.6 s | 0.9 / 0.4 | 15 / 5 | elbow bend at limit 7% |
| `ayana_1_3_3_t246-265` | A | 21_ayana_1_3_3 246.4–265.2 s | 10.3 / 5.1 | 23 / 8 | human steps; elbow bend at limit 8% |
| `ayana_1_3_3_t308-325` | A | 21_ayana_1_3_3 308.2–324.8 s | 2.1 / 1.2 | 9 / 4 | elbow bend at limit 6% |
| `ayana_1_3_3_t323-328_shift` | B | 21_ayana_1_3_3 322.8–327.8 s | 14.0 / 6.7 | 33 / 11 | outlier knee max (z +6.0) |
| `ayana_1_3_3_t336-343_shift` | B | 21_ayana_1_3_3 336.5–342.8 s | 12.2 / 6.5 | 20 / 8 | elbow bend at limit 23% |
| `ayana_1_3_3_t341-355` | A | 21_ayana_1_3_3 340.8–355.0 s | 0.4 / 0.5 | 9 / 3 | elbow bend at limit 33% |
| `ayana_1_3_3_t355-369` | A | 21_ayana_1_3_3 355.0–369.3 s | 0.9 / 0.5 | 27 / 10 | elbow bend at limit 25% |
| `ayana_1_3_3_t367-373_shift` | B | 21_ayana_1_3_3 367.3–372.8 s | 15.3 / 7.2 | 31 / 10 | elbow bend at limit 15%; outlier knee max (z +6.5) |
| `ayana_1_3_3_t390-408` | A | 21_ayana_1_3_3 389.6–408.4 s | 5.7 / 2.9 | 33 / 11 | elbow bend at limit 6% |
| `ayana_1_3_3_t408-427` | A | 21_ayana_1_3_3 408.4–427.1 s | 0.4 / 0.2 | 17 / 6 | elbow bend at limit 5% |
| `ayana_1_3_3_t57-76` | A | 21_ayana_1_3_3 57.3–75.7 s | 0.7 / 0.8 | 20 / 6 | shoulder at limit 8% |
| `ayana_1_3_3_t76-94` | A | 21_ayana_1_3_3 75.7–94.2 s | 4.7 / 2.1 | 19 / 6 | shoulder at limit 6% |
| `ayana_1_3_3_t92-98_shift` | B | 21_ayana_1_3_3 92.2–98.1 s | 20.8 / 10.8 | 28 / 10 | shoulder at limit 17%; outlier knee max (z +6.7) |
| `ayana_1_4_4_t202-214` | A | 21_ayana_1_4_4 202.0–214.0 s | 1.1 / 0.5 | 7 / 3 | elbow bend at limit 14% |
| `ayana_1_4_4_t253-272` | A | 21_ayana_1_4_4 252.7–271.9 s | 1.8 / 1.1 | 26 / 10 | shoulder at limit 6% |
| `ayana_1_4_4_t272-291` | A | 21_ayana_1_4_4 271.9–291.1 s | 0.5 / 0.5 | 33 / 12 | shoulder at limit 6% |
| `ayana_1_4_4_t444-464` | A | 21_ayana_1_4_4 444.5–463.7 s | 0.7 / 0.4 | 16 / 7 | elbow bend at limit 14% |
| `ayana_1_5_5_t15-22_shift` | B | 21_ayana_1_5_5 15.2–22.2 s | 18.0 / 9.5 | 15 / 4 | head at limit 11%; shoulder at limit 23%; elbow bend at limit 8%; outlier trunk drop (z +4.3); outlier knee max (z +8.0) |
| `ayana_1_5_5_t20-39` | A | 21_ayana_1_5_5 20.2–39.2 s | 1.0 / 1.2 | 23 / 9 | shoulder at limit 5%; elbow bend at limit 11% |
| `ayana_1_5_5_t507-526` | A | 21_ayana_1_5_5 507.3–526.4 s | 9.3 / 5.0 | 18 / 8 | elbow bend at limit 6% |
| `ayana_1_5_5_t534-539` | A | 21_ayana_1_5_5 534.0–539.3 s | 9.7 / 2.1 | 41 / 18 | shoulder at limit 13%; outlier knee max (z +4.6) |
| `ayana_1_5_5_t539-555` | A | 21_ayana_1_5_5 539.3–555.2 s | 9.7 / 4.1 | 42 / 14 | outlier knee max (z +4.5) |
| `ayana_1_5_5_t553-561_shift` | B | 21_ayana_1_5_5 553.2–561.2 s | 14.2 / 7.1 | 38 / 13 | outlier knee max (z +5.8) |
| `ayana_1_5_5_t58-77` | A | 21_ayana_1_5_5 58.2–77.2 s | 2.8 / 1.2 | 17 / 7 | elbow bend at limit 5% |
| `ayana_1_6_6_t0-5_shift` | B | 21_ayana_1_6_6 0.0–4.7 s | 12.2 / 4.7 | 16 / 6 | outlier knee max (z +3.5) |
| `ayana_1_6_6_t254-273` | A | 21_ayana_1_6_6 253.9–273.2 s | 5.3 / 4.3 | 23 / 8 | outlier knee max (z +4.8) |
| `ayana_1_6_6_t273-292` | A | 21_ayana_1_6_6 273.2–292.5 s | 6.3 / 3.2 | 15 / 6 | outlier knee max (z +4.6) |
| `ayana_1_6_6_t406-425` | A | 21_ayana_1_6_6 406.3–425.1 s | 2.0 / 0.4 | 19 / 7 | elbow bend at limit 11% |
| `ayana_1_6_6_t41-61` | A | 21_ayana_1_6_6 41.4–60.7 s | 0.8 / 0.4 | 27 / 12 | elbow bend at limit 7% |
| `ayana_1_6_6_t481-500` | A | 21_ayana_1_6_6 481.4–500.2 s | 9.6 / 5.9 | 5 / 2 | outlier knee max (z +4.2) |
| `ayana_1_6_6_t500-519` | A | 21_ayana_1_6_6 500.2–519.5 s | 9.0 / 6.1 | 12 / 4 | outlier knee max (z +5.0) |
| `ayana_1_6_6_t560-574` | A | 21_ayana_1_6_6 560.2–573.5 s | 8.5 / 6.4 | 18 / 7 | outlier trunk drop (z +3.5); outlier knee max (z +6.7) |
| `ayana_1_6_6_t574-587` | A | 21_ayana_1_6_6 573.5–586.8 s | 9.6 / 4.9 | 16 / 7 | outlier knee max (z +4.8) |
| `ayana_1_7_7_t0-6` | A | 21_ayana_1_7_7 0.0–6.5 s | 9.9 / 4.6 | 5 / 2 | outlier knee max (z +5.3) |
| `ayana_1_7_7_t103-107_shift` | B | 21_ayana_1_7_7 102.7–107.2 s | 11.3 / 5.7 | 12 / 4 | knee 63 deg; outlier trunk drop (z +4.8); outlier knee max (z +8.9) |
| `ayana_1_7_7_t105-113` | A | 21_ayana_1_7_7 105.2–112.8 s | 4.5 / 0.9 | 19 / 9 | knee 62 deg; outlier knee max (z +8.6) |
| `ayana_1_7_7_t141-160` | A | 21_ayana_1_7_7 141.0–160.1 s | 3.7 / 1.0 | 25 / 7 | outlier knee max (z +5.8) |
| `ayana_1_7_7_t218-237` | A | 21_ayana_1_7_7 217.5–236.6 s | 2.1 / 1.2 | 18 / 4 | shoulder at limit 8%; outlier knee max (z +3.8) |
| `ayana_1_7_7_t299-315` | A | 21_ayana_1_7_7 298.8–315.4 s | 8.9 / 8.4 | 7 / 3 | K1 feet move 8 cm; outlier knee max (z +3.7) |
| `ayana_1_7_7_t31-35_shift` | B | 21_ayana_1_7_7 30.8–35.3 s | 8.8 / 6.7 | 21 / 6 | knee 73 deg; elbow bend at limit 5%; outlier knee max (z +12.5) |
| `ayana_1_7_7_t315-332` | A | 21_ayana_1_7_7 315.4–331.9 s | 5.7 / 5.1 | 4 / 2 | outlier knee max (z +4.1) |
| `ayana_1_7_7_t33-51` | A | 21_ayana_1_7_7 33.3–51.2 s | 5.9 / 2.2 | 17 / 6 | outlier knee max (z +7.6) |
| `ayana_1_7_7_t330-334_shift` | B | 21_ayana_1_7_7 329.9–334.3 s | 5.6 / 4.6 | 10 / 6 | outlier trunk drop (z +3.9); outlier knee max (z +7.4) |
| `ayana_1_7_7_t332-337` | A | 21_ayana_1_7_7 332.3–337.4 s | 4.3 / 4.8 | 15 / 9 | outlier knee max (z +7.4) |
| `ayana_1_7_7_t335-339_shift` | B | 21_ayana_1_7_7 335.3–339.3 s | 28.4 / 16.8 | 15 / 7 | human steps; knee 69 deg; outlier trunk drop (z +3.8); outlier knee max (z +11.1) |
| `ayana_1_7_7_t365-384` | A | 21_ayana_1_7_7 364.6–383.7 s | 0.5 / 0.6 | 11 / 4 | shoulder at limit 25% |
| `ayana_1_7_7_t441-460` | A | 21_ayana_1_7_7 441.3–460.5 s | 2.7 / 0.8 | 17 / 6 | shoulder at limit 17% |
| `ayana_1_7_7_t499-518` | A | 21_ayana_1_7_7 498.9–518.1 s | 1.6 / 0.7 | 14 / 4 | shoulder at limit 46% |
| `ayana_1_7_7_t518-537` | A | 21_ayana_1_7_7 518.1–537.3 s | 1.3 / 0.5 | 23 / 7 | shoulder at limit 8% |
| `ayana_1_7_7_t87-105` | A | 21_ayana_1_7_7 86.9–104.7 s | 2.1 / 0.6 | 11 / 5 | outlier knee max (z +3.5) |
| `ayana_1_8_8_t149-168` | A | 21_ayana_1_8_8 149.2–168.0 s | 1.1 / 0.9 | 41 / 13 | shoulder at limit 7%; outlier knee max (z +6.4) |
| `ayana_1_8_8_t206-225` | A | 21_ayana_1_8_8 205.7–224.6 s | 0.9 / 0.7 | 26 / 9 | shoulder at limit 5% |
| `ayana_1_8_8_t225-243` | A | 21_ayana_1_8_8 224.6–243.4 s | 9.6 / 5.3 | 15 / 5 | shoulder at limit 26%; outlier trunk drop (z +3.8); outlier knee max (z +4.4) |
| `ayana_1_8_8_t336-354` | A | 21_ayana_1_8_8 335.8–353.9 s | 4.3 / 2.8 | 13 / 5 | outlier knee max (z +6.4) |
| `ayana_1_8_8_t39-46_shift` | B | 21_ayana_1_8_8 39.0–46.0 s | 17.8 / 9.5 | 18 / 6 | outlier knee max (z +6.0) |
| `ayana_1_8_8_t52-57_shift` | B | 21_ayana_1_8_8 52.4–57.0 s | 18.4 / 9.3 | 55 / 24 | shoulder at limit 19%; outlier arms k1 cm (z +4.6) |
| `ayana_1_8_8_t528-535` | A | 21_ayana_1_8_8 528.2–535.3 s | 6.6 / 2.8 | 6 / 3 | head at limit 38% |
| `ayana_1_8_8_t540-548` | A | 21_ayana_1_8_8 539.7–547.7 s | 6.7 / 3.5 | 4 / 2 | head at limit 33% |
| `ayana_1_8_8_t574-586` | A | 21_ayana_1_8_8 573.6–585.7 s | 3.0 / 1.6 | 31 / 12 | elbow bend at limit 7% |
| `ayana_1_8_8_t588-598_shift` | B | 21_ayana_1_8_8 588.2–597.8 s | 20.2 / 8.9 | 23 / 7 | knee 75 deg; outlier knee max (z +13.2) |
| `ayana_1_9_9_t0-5` | A | 21_ayana_1_9_9 0.0–4.7 s | 2.2 / 1.4 | 5 / 3 | head at limit 15% |
| `ayana_1_9_9_t135-151` | A | 21_ayana_1_9_9 135.5–151.0 s | 5.6 / 0.8 | 17 / 8 | shoulder at limit 34% |
| `ayana_1_9_9_t206-224` | A | 21_ayana_1_9_9 206.3–224.5 s | 1.5 / 0.8 | 19 / 8 | shoulder at limit 22% |
| `ayana_1_9_9_t224-243` | A | 21_ayana_1_9_9 224.5–242.6 s | 0.6 / 0.5 | 15 / 4 | shoulder at limit 9% |
| `ayana_1_9_9_t24-40` | A | 21_ayana_1_9_9 24.0–39.8 s | 9.7 / 7.7 | 19 / 8 | elbow bend at limit 6% |
| `ayana_1_9_9_t338-358` | A | 21_ayana_1_9_9 338.1–357.7 s | 1.6 / 0.7 | 6 / 3 | shoulder at limit 7% |
| `ayana_1_9_9_t356-360_shift` | B | 21_ayana_1_9_9 355.7–360.2 s | 17.2 / 10.7 | 4 / 3 | outlier knee max (z +5.3) |
| `ayana_1_9_9_t361-366` | A | 21_ayana_1_9_9 360.7–366.1 s | 1.1 / 0.5 | 16 / 8 | elbow bend at limit 38% |
| `ayana_1_9_9_t408-414_shift` | B | 21_ayana_1_9_9 408.5–414.2 s | 20.5 / 10.9 | 24 / 8 | shoulder at limit 11%; outlier knee max (z +7.4) |
| `ayana_1_9_9_t466-484` | A | 21_ayana_1_9_9 466.2–484.3 s | 0.4 / 0.6 | 16 / 8 | shoulder at limit 13% |
| `ayana_1_9_9_t502-520` | A | 21_ayana_1_9_9 502.3–520.3 s | 0.6 / 1.0 | 9 / 4 | shoulder at limit 17% |
| `ayana_1_9_9_t58-62_shift` | B | 21_ayana_1_9_9 57.9–61.9 s | 11.6 / 5.4 | 39 / 15 | head at limit 6%; shoulder at limit 6% |
| `ayana_1_9_9_t620-624_shift` | B | 21_ayana_1_9_9 619.9–624.5 s | 18.4 / 10.7 | 32 / 10 | outlier knee max (z +6.2) |
| `ayana_1_9_9_t63-67_shift` | B | 21_ayana_1_9_9 62.7–67.0 s | 10.8 / 5.2 | 30 / 9 | head at limit 24% |
| `carla_0_100_100_t10-15_shift` | B | 6_carla_0_100_100 9.6–14.9 s | 21.4 / 12.0 | 11 / 5 | outlier knee max (z +6.9) |
| `carla_0_100_100_t19-24_shift` | B | 6_carla_0_100_100 19.2–23.8 s | 15.6 / 9.4 | 6 / 1 | outlier knee max (z +6.9) |
| `carla_0_101_101_t33-38_shift` | B | 6_carla_0_101_101 33.2–37.7 s | 10.8 / 6.4 | 5 / 2 | outlier knee max (z +5.9) |
| `carla_0_101_101_t41-45_shift` | B | 6_carla_0_101_101 40.5–45.1 s | 15.3 / 9.4 | 8 / 3 | outlier knee max (z +5.5) |
| `carla_0_101_101_t47-56_shift` | B | 6_carla_0_101_101 47.1–55.9 s | 28.7 / 16.4 | 20 / 7 | human steps; outlier knee max (z +6.7) |
| `carla_0_101_101_t56-60_shift` | B | 6_carla_0_101_101 56.5–60.5 s | 18.0 / 11.4 | 11 / 3 | outlier knee max (z +6.4) |
| `carla_0_102_102_t34-38_shift` | B | 6_carla_0_102_102 34.3–38.3 s | 25.2 / 14.7 | 7 / 2 | human steps; outlier knee max (z +6.5) |
| `carla_0_103_103_t0-7_shift` | B | 6_carla_0_103_103 0.0–6.7 s | 24.2 / 14.1 | 7 / 4 | outlier knee max (z +7.8) |
| `carla_0_103_103_t18-22_shift` | B | 6_carla_0_103_103 18.1–22.2 s | 13.6 / 3.6 | 30 / 9 | knee 61 deg; leg at limit 8%; outlier knee max (z +8.2) |
| `carla_0_103_103_t26-30_shift` | B | 6_carla_0_103_103 25.8–30.2 s | 8.3 / 4.7 | 17 / 4 | outlier knee max (z +4.1) |
| `carla_0_103_103_t8-13_shift` | B | 6_carla_0_103_103 8.1–12.7 s | 12.8 / 6.3 | 4 / 1 | outlier knee max (z +4.5) |
| `carla_0_104_104_t10-19_shift` | B | 6_carla_0_104_104 10.2–18.5 s | 21.0 / 11.7 | 15 / 4 | outlier knee max (z +7.9) |
| `carla_0_104_104_t17-22` | A | 6_carla_0_104_104 16.5–22.1 s | 9.1 / 2.0 | 30 / 9 | outlier knee max (z +4.2) |
| `carla_0_104_104_t33-41` | A | 6_carla_0_104_104 32.9–40.8 s | 7.1 / 1.9 | 17 / 5 | outlier knee max (z +3.8) |
| `carla_0_104_104_t39-43_shift` | B | 6_carla_0_104_104 38.8–42.8 s | 14.3 / 6.5 | 21 / 6 | outlier knee max (z +3.8) |
| `carla_0_105_105_t18-23` | A | 6_carla_0_105_105 17.9–23.2 s | 9.8 / 2.3 | 16 / 4 | outlier knee max (z +4.2) |
| `carla_0_105_105_t19-23_shift` | B | 6_carla_0_105_105 19.3–23.3 s | 9.2 / 2.0 | 18 / 4 | outlier knee max (z +6.2) |
| `carla_0_106_106_t0-4_shift` | B | 6_carla_0_106_106 0.0–4.0 s | 17.1 / 9.7 | 12 / 3 | outlier knee max (z +4.0) |
| `carla_0_106_106_t13-18_shift` | B | 6_carla_0_106_106 13.2–17.8 s | 13.1 / 7.8 | 22 / 8 | outlier knee max (z +4.1) |
| `carla_0_106_106_t36-40_shift` | B | 6_carla_0_106_106 35.9–39.9 s | 20.3 / 10.8 | 15 / 3 | outlier knee max (z +4.2) |
| `carla_0_107_107_t28-32` | A | 6_carla_0_107_107 28.1–32.5 s | 7.2 / 1.7 | 30 / 7 | outlier knee max (z +4.3) |
| `carla_0_107_107_t30-35_shift` | B | 6_carla_0_107_107 30.5–34.9 s | 6.8 / 3.5 | 16 / 4 | outlier knee max (z +4.3) |
| `carla_0_107_107_t5-11` | A | 6_carla_0_107_107 4.8–11.4 s | 10.0 / 3.3 | 9 / 2 | outlier knee max (z +6.2) |
| `carla_0_109_109_t26-30_shift` | B | 6_carla_0_109_109 26.2–30.2 s | 15.5 / 2.8 | 26 / 7 | outlier knee max (z +4.2) |
| `carla_0_110_110_t11-20` | A | 6_carla_0_110_110 10.8–19.9 s | 6.6 / 1.7 | 29 / 9 | outlier knee max (z +5.7) |
| `carla_0_110_110_t17-21_shift` | B | 6_carla_0_110_110 17.0–21.0 s | 25.8 / 13.4 | 35 / 11 | human steps; outlier knee max (z +7.8) |
| `carla_0_111_111_t35-43_shift` | B | 6_carla_0_111_111 35.0–43.2 s | 14.9 / 8.2 | 13 / 3 | outlier knee max (z +4.9) |
| `carla_0_112_112_t26-31_shift` | B | 6_carla_0_112_112 26.2–31.4 s | 13.9 / 8.3 | 9 / 4 | outlier knee max (z +4.8) |
| `carla_0_113_113_t0-4_shift` | B | 6_carla_0_113_113 0.3–4.3 s | 12.1 / 7.3 | 27 / 5 | outlier knee max (z +4.5) |
| `carla_0_113_113_t24-29_shift` | B | 6_carla_0_113_113 24.4–29.1 s | 14.4 / 8.1 | 17 / 3 | outlier knee max (z +5.5) |
| `carla_0_114_114_t15-23_shift` | B | 6_carla_0_114_114 15.3–22.7 s | 22.4 / 13.1 | 35 / 10 | outlier knee max (z +5.3) |
| `carla_0_114_114_t21-31` | A | 6_carla_0_114_114 20.7–31.5 s | 9.0 / 2.1 | 33 / 8 | outlier knee max (z +5.7) |
| `carla_0_114_114_t29-34_shift` | B | 6_carla_0_114_114 29.5–34.2 s | 19.0 / 11.7 | 41 / 11 | outlier knee max (z +7.1) |
| `carla_0_114_114_t36-40_shift` | B | 6_carla_0_114_114 36.3–40.3 s | 21.9 / 9.8 | 29 / 7 | outlier knee max (z +4.0) |
| `carla_0_114_114_t45-49_shift` | B | 6_carla_0_114_114 45.5–49.5 s | 8.1 / 1.4 | 43 / 11 | outlier knee max (z +5.8) |
| `carla_0_115_115_t25-29_shift` | B | 6_carla_0_115_115 24.9–28.9 s | 15.5 / 4.0 | 23 / 5 | leg at limit 12%; outlier knee max (z +7.9) |
| `carla_0_115_115_t30-39` | A | 6_carla_0_115_115 29.5–39.3 s | 4.8 / 1.3 | 33 / 8 | outlier knee max (z +4.1) |
| `carla_0_115_115_t37-41_shift` | B | 6_carla_0_115_115 37.2–41.2 s | 16.2 / 6.7 | 14 / 4 | outlier knee max (z +4.4) |
| `carla_0_115_115_t58-62_shift` | B | 6_carla_0_115_115 57.8–61.8 s | 19.3 / 10.7 | 25 / 5 | outlier knee max (z +3.9) |
| `carla_0_116_116_t14-22_shift` | B | 6_carla_0_116_116 14.1–22.0 s | 31.5 / 18.4 | 21 / 5 | human steps; K1 feet move 18 cm; outlier knee max (z +6.7) |
| `carla_0_116_116_t35-40_shift` | B | 6_carla_0_116_116 35.2–39.9 s | 12.1 / 9.8 | 19 / 5 | outlier knee max (z +5.9) |
| `carla_0_116_116_t41-45_shift` | B | 6_carla_0_116_116 40.9–45.3 s | 8.4 / 4.0 | 37 / 8 | outlier knee max (z +4.2) |
| `carla_0_116_116_t5-12_shift` | B | 6_carla_0_116_116 5.3–12.2 s | 16.3 / 9.3 | 30 / 7 | outlier knee max (z +5.3) |
| `carla_0_116_116_t54-58_shift` | B | 6_carla_0_116_116 54.1–58.1 s | 16.0 / 3.6 | 25 / 5 | outlier knee max (z +5.4) |
| `carla_0_116_116_t60-64_shift` | B | 6_carla_0_116_116 59.8–63.8 s | 13.7 / 7.3 | 56 / 14 | outlier knee max (z +4.3) |
| `carla_0_117_117_t0-9_shift` | B | 6_carla_0_117_117 0.4–9.3 s | 19.3 / 10.8 | 13 / 4 | outlier knee max (z +7.7) |
| `carla_0_118_118_t0-8_shift` | B | 6_carla_0_118_118 0.3–7.5 s | 21.5 / 9.5 | 13 / 4 | outlier knee max (z +4.9) |
| `carla_0_118_118_t33-37_shift` | B | 6_carla_0_118_118 32.8–36.8 s | 13.9 / 3.6 | 30 / 8 | outlier knee max (z +6.5) |
| `carla_0_118_118_t8-12_shift` | B | 6_carla_0_118_118 7.9–12.0 s | 24.7 / 14.8 | 14 / 4 | outlier knee max (z +6.6) |
| `carla_0_49_49_t5-14_shift` | B | 6_carla_0_49_49 5.2–14.2 s | 14.9 / 8.7 | 15 / 5 | leg at limit 17%; outlier trunk drop (z +5.2); outlier knee max (z +4.4) |
| `carla_0_52_52_t15-19_shift` | B | 6_carla_0_52_52 14.9–18.9 s | 12.8 / 3.1 | 27 / 8 | outlier knee max (z +5.9) |
| `carla_0_54_54_t34-38_shift` | B | 6_carla_0_54_54 34.4–38.4 s | 19.9 / 10.1 | 33 / 10 | outlier knee max (z +4.3) |
| `carla_0_54_54_t6-11_shift` | B | 6_carla_0_54_54 6.1–10.6 s | 13.2 / 7.7 | 15 / 5 | outlier knee max (z +4.2) |
| `carla_0_55_55_t11-20` | A | 6_carla_0_55_55 11.2–19.6 s | 6.4 / 1.3 | 26 / 6 | outlier knee max (z +4.2) |
| `carla_0_55_55_t7-11_shift` | B | 6_carla_0_55_55 7.3–11.3 s | 25.0 / 15.0 | 13 / 6 | human steps; outlier knee max (z +6.1) |
| `carla_0_56_56_t11-15_shift` | B | 6_carla_0_56_56 10.8–14.8 s | 14.0 / 2.9 | 24 / 7 | outlier knee max (z +5.6) |
| `carla_0_57_57_t39-44_shift` | B | 6_carla_0_57_57 39.1–44.4 s | 17.4 / 4.6 | 15 / 5 | outlier knee max (z +7.4) |
| `carla_0_58_58_t16-20_shift` | B | 6_carla_0_58_58 16.1–20.3 s | 20.3 / 5.2 | 30 / 10 | outlier trunk drop (z +3.8); outlier knee max (z +5.6) |
| `carla_0_58_58_t21-27` | A | 6_carla_0_58_58 21.4–27.0 s | 6.8 / 1.4 | 14 / 4 | outlier knee max (z +4.1) |
| `carla_0_58_58_t25-32_shift` | B | 6_carla_0_58_58 25.0–31.8 s | 26.7 / 12.2 | 12 / 4 | human steps; outlier knee max (z +6.3) |
| `carla_0_59_59_t0-4_shift` | B | 6_carla_0_59_59 0.0–4.0 s | 16.4 / 9.1 | 11 / 5 | outlier knee max (z +5.1) |
| `carla_0_60_60_t20-28` | A | 6_carla_0_60_60 20.5–27.6 s | 9.7 / 2.2 | 16 / 4 | outlier knee max (z +5.7) |
| `carla_0_60_60_t24-28_shift` | B | 6_carla_0_60_60 23.9–27.9 s | 10.2 / 2.5 | 20 / 5 | outlier knee max (z +7.1) |
| `carla_0_61_61_t41-45_shift` | B | 6_carla_0_61_61 40.9–44.9 s | 11.6 / 2.7 | 7 / 3 | outlier knee max (z +6.9) |
| `carla_0_62_62_t3-7_shift` | B | 6_carla_0_62_62 3.4–7.4 s | 13.2 / 6.5 | 22 / 5 | outlier knee max (z +5.6) |
| `carla_0_62_62_t5-9` | A | 6_carla_0_62_62 4.6–9.4 s | 4.7 / 4.9 | 13 / 3 | outlier knee max (z +5.7) |
| `carla_0_63_63_t11-16_shift` | B | 6_carla_0_63_63 11.2–15.6 s | 12.7 / 6.7 | 30 / 6 | outlier knee max (z +5.0) |
| `carla_0_63_63_t32-43` | A | 6_carla_0_63_63 32.3–42.9 s | 7.8 / 2.6 | 19 / 6 | outlier knee max (z +7.4) |
| `carla_0_64_64_t16-21_shift` | B | 6_carla_0_64_64 15.7–20.7 s | 21.6 / 12.3 | 12 / 3 | outlier knee max (z +4.7) |
| `carla_0_64_64_t32-36_shift` | B | 6_carla_0_64_64 32.0–36.0 s | 25.9 / 14.6 | 8 / 3 | human steps; outlier knee max (z +4.8) |
| `carla_0_65_65_t15-22_shift` | B | 6_carla_0_65_65 15.4–21.7 s | 14.3 / 8.5 | 43 / 10 | outlier knee max (z +4.1) |
| `carla_0_65_65_t23-27_shift` | B | 6_carla_0_65_65 23.2–27.2 s | 25.8 / 13.9 | 21 / 6 | human steps; knee 65 deg; outlier knee max (z +9.7) |
| `carla_0_65_65_t9-15_shift` | B | 6_carla_0_65_65 9.3–14.8 s | 19.6 / 10.2 | 20 / 7 | outlier knee max (z +4.7) |
| `carla_0_66_66_t18-23` | A | 6_carla_0_66_66 18.5–23.4 s | 1.8 / 0.5 | 24 / 10 | outlier trunk drop (z +3.9); outlier knee max (z +6.7) |
| `carla_0_66_66_t45-49` | A | 6_carla_0_66_66 44.6–49.4 s | 5.7 / 1.8 | 12 / 4 | outlier knee max (z +4.0) |
| `carla_0_66_66_t47-53_shift` | B | 6_carla_0_66_66 47.4–52.7 s | 22.6 / 13.1 | 10 / 3 | outlier knee max (z +5.3) |
| `carla_0_67_67_t0-6` | A | 6_carla_0_67_67 0.3–6.3 s | 1.9 / 0.7 | 24 / 11 | outlier knee max (z +5.2) |
| `carla_0_67_67_t7-21_shift` | B | 6_carla_0_67_67 7.1–21.1 s | 21.9 / 11.8 | 20 / 5 | knee 65 deg; outlier knee max (z +9.6) |
| `carla_0_68_68_t2-9_shift` | B | 6_carla_0_68_68 2.2–8.7 s | 21.7 / 12.1 | 37 / 12 | outlier knee max (z +6.4) |
| `carla_0_68_68_t20-25_shift` | B | 6_carla_0_68_68 19.6–24.6 s | 24.2 / 13.8 | 21 / 5 | outlier knee max (z +5.8) |
| `carla_0_69_69_t12-17_shift` | B | 6_carla_0_69_69 12.0–16.5 s | 10.7 / 5.9 | 16 / 4 | outlier knee max (z +5.7) |
| `carla_0_69_69_t41-51_shift` | B | 6_carla_0_69_69 41.0–51.1 s | 14.7 / 8.4 | 23 / 7 | knee 63 deg; outlier knee max (z +9.0) |
| `carla_0_70_70_t20-32_shift` | B | 6_carla_0_70_70 19.8–31.8 s | 17.8 / 9.6 | 32 / 8 | upper-arm twist at limit 29%; outlier trunk drop (z +3.8); outlier knee max (z +5.3) |
| `carla_0_70_70_t30-36` | A | 6_carla_0_70_70 29.8–35.8 s | 8.7 / 2.2 | 27 / 8 | outlier knee max (z +4.2) |
| `carla_0_70_70_t34-38_shift` | B | 6_carla_0_70_70 33.8–38.4 s | 15.3 / 9.0 | 14 / 5 | outlier knee max (z +5.1) |
| `carla_0_70_70_t40-47_shift` | B | 6_carla_0_70_70 40.1–46.8 s | 19.9 / 11.1 | 14 / 4 | outlier knee max (z +6.1) |
| `carla_0_72_72_t16-20_shift` | B | 6_carla_0_72_72 15.8–19.8 s | 25.4 / 14.1 | 23 / 6 | human steps; knee 60 deg; outlier knee max (z +8.1) |
| `carla_0_72_72_t34-42` | A | 6_carla_0_72_72 34.4–41.8 s | 9.3 / 3.8 | 16 / 4 | outlier knee max (z +4.6) |
| `carla_0_72_72_t40-44_shift` | B | 6_carla_0_72_72 39.8–44.4 s | 7.0 / 1.8 | 22 / 5 | outlier knee max (z +4.8) |
| `carla_0_74_74_t44-49_shift` | B | 6_carla_0_74_74 43.9–48.8 s | 24.3 / 13.7 | 23 / 5 | outlier knee max (z +6.7) |
| `carla_0_75_75_t10-16` | A | 6_carla_0_75_75 9.8–15.8 s | 9.6 / 3.7 | 27 / 6 | outlier knee max (z +5.1) |
| `carla_0_75_75_t24-28_shift` | B | 6_carla_0_75_75 23.8–27.8 s | 37.5 / 21.2 | 21 / 5 | human steps; K1 feet move 21 cm; outlier knee max (z +6.5) |
| `carla_0_75_75_t7-12_shift` | B | 6_carla_0_75_75 7.3–11.8 s | 11.9 / 7.1 | 20 / 5 | outlier knee max (z +6.4) |
| `carla_0_76_76_t0-5_shift` | B | 6_carla_0_76_76 0.2–5.2 s | 21.3 / 13.7 | 16 / 4 | outlier knee max (z +5.0) |
| `carla_0_76_76_t14-19_shift` | B | 6_carla_0_76_76 14.4–18.6 s | 16.9 / 9.4 | 21 / 7 | outlier knee max (z +3.7) |
| `carla_0_76_76_t23-27_shift` | B | 6_carla_0_76_76 23.5–27.5 s | 17.1 / 9.7 | 33 / 8 | outlier knee max (z +4.5) |
| `carla_0_78_78_t29-37` | A | 6_carla_0_78_78 29.4–36.7 s | 9.6 / 2.7 | 25 / 7 | outlier knee max (z +4.9) |
| `carla_0_78_78_t33-37_shift` | B | 6_carla_0_78_78 33.3–37.3 s | 6.6 / 1.9 | 22 / 7 | outlier knee max (z +7.1) |
| `carla_0_78_78_t40-44_shift` | B | 6_carla_0_78_78 39.8–43.8 s | 16.1 / 8.7 | 19 / 5 | outlier knee max (z +6.8) |
| `carla_0_79_79_t2-7_shift` | B | 6_carla_0_79_79 1.7–7.2 s | 23.5 / 13.9 | 21 / 5 | outlier knee max (z +7.1) |
| `carla_0_79_79_t32-36_shift` | B | 6_carla_0_79_79 32.3–36.3 s | 12.1 / 2.9 | 37 / 10 | outlier knee max (z +5.0) |
| `carla_0_79_79_t47-51_shift` | B | 6_carla_0_79_79 46.9–50.9 s | 26.0 / 14.0 | 29 / 8 | human steps; outlier knee max (z +7.9) |
| `carla_0_80_80_t20-24_shift` | B | 6_carla_0_80_80 19.5–23.5 s | 11.5 / 4.7 | 24 / 4 | leg at limit 31% |
| `carla_0_81_81_t47-54_shift` | B | 6_carla_0_81_81 47.2–53.5 s | 22.1 / 13.2 | 12 / 3 | outlier knee max (z +7.3) |
| `carla_0_81_81_t7-12_shift` | B | 6_carla_0_81_81 7.4–11.8 s | 8.8 / 5.2 | 14 / 3 | outlier knee max (z +5.5) |
| `carla_0_83_83_t10-14_shift` | B | 6_carla_0_83_83 9.7–14.2 s | 14.3 / 8.1 | 26 / 6 | outlier knee max (z +4.5) |
| `carla_0_83_83_t12-23` | A | 6_carla_0_83_83 12.2–22.5 s | 9.9 / 5.0 | 22 / 6 | outlier knee max (z +6.4) |
| `carla_0_84_84_t5-9_shift` | B | 6_carla_0_84_84 4.9–9.4 s | 8.7 / 5.1 | 23 / 6 | outlier knee max (z +4.0) |
| `carla_0_85_85_t18-23_shift` | B | 6_carla_0_85_85 18.2–22.9 s | 11.3 / 7.2 | 13 / 5 | outlier knee max (z +5.3) |
| `carla_0_85_85_t9-13_shift` | B | 6_carla_0_85_85 8.9–13.5 s | 11.9 / 6.3 | 13 / 4 | outlier knee max (z +4.1) |
| `carla_0_86_86_t36-40_shift` | B | 6_carla_0_86_86 36.0–40.0 s | 25.8 / 14.2 | 21 / 5 | human steps; outlier knee max (z +7.0) |
| `carla_0_86_86_t46-50` | A | 6_carla_0_86_86 45.6–49.8 s | 5.1 / 1.0 | 23 / 5 | outlier knee max (z +4.2) |
| `carla_0_88_88_t32-36_shift` | B | 6_carla_0_88_88 31.9–35.9 s | 13.6 / 2.8 | 15 / 5 | outlier knee max (z +7.9) |
| `carla_0_88_88_t40-44_shift` | B | 6_carla_0_88_88 39.6–44.2 s | 9.2 / 4.9 | 20 / 6 | outlier knee max (z +4.8) |
| `carla_0_88_88_t6-10_shift` | B | 6_carla_0_88_88 6.0–10.0 s | 25.2 / 14.8 | 6 / 2 | human steps; outlier knee max (z +5.8) |
| `carla_0_88_88_t9-15` | A | 6_carla_0_88_88 9.4–14.6 s | 7.6 / 2.1 | 15 / 5 | outlier knee max (z +5.1) |
| `carla_0_89_89_t0-6_shift` | B | 6_carla_0_89_89 0.0–5.7 s | 20.2 / 11.8 | 7 / 2 | outlier knee max (z +3.8) |
| `carla_0_89_89_t32-36_shift` | B | 6_carla_0_89_89 31.8–36.4 s | 10.8 / 6.3 | 16 / 6 | outlier knee max (z +5.7) |
| `carla_0_89_89_t66-70_shift` | B | 6_carla_0_89_89 65.8–69.8 s | 18.4 / 10.7 | 18 / 4 | outlier knee max (z +4.4) |
| `carla_0_91_91_t33-37_shift` | B | 6_carla_0_91_91 32.6–36.6 s | 12.1 / 2.6 | 13 / 4 | outlier knee max (z +6.5) |
| `carla_0_92_92_t2-6_shift` | B | 6_carla_0_92_92 2.0–6.0 s | 8.5 / 1.3 | 12 / 4 | outlier knee max (z +5.1) |
| `carla_0_92_92_t29-36_shift` | B | 6_carla_0_92_92 29.4–35.5 s | 16.0 / 8.8 | 18 / 5 | outlier knee max (z +4.4) |
| `carla_0_93_93_t25-30_shift` | B | 6_carla_0_93_93 25.0–29.5 s | 8.1 / 5.7 | 18 / 5 | outlier knee max (z +5.3) |
| `carla_0_93_93_t48-52_shift` | B | 6_carla_0_93_93 48.5–52.5 s | 24.9 / 14.5 | 22 / 5 | outlier knee max (z +7.0) |
| `carla_0_95_95_t28-32_shift` | B | 6_carla_0_95_95 27.6–31.6 s | 12.2 / 2.6 | 14 / 4 | outlier knee max (z +6.2) |
| `carla_0_96_96_t24-28` | A | 6_carla_0_96_96 23.9–28.4 s | 9.0 / 2.3 | 14 / 5 | outlier knee max (z +3.9) |
| `carla_0_96_96_t26-32_shift` | B | 6_carla_0_96_96 26.4–31.6 s | 13.3 / 7.7 | 14 / 4 | outlier knee max (z +4.4) |
| `carla_0_97_97_t0-5_shift` | B | 6_carla_0_97_97 0.3–4.8 s | 24.3 / 13.8 | 6 / 3 | outlier knee max (z +4.8) |
| `carla_0_98_98_t22-26_shift` | B | 6_carla_0_98_98 22.0–26.0 s | 14.0 / 3.5 | 13 / 4 | outlier knee max (z +6.0) |
| `carla_0_99_99_t25-32_shift` | B | 6_carla_0_99_99 25.0–31.7 s | 18.9 / 10.5 | 6 / 2 | outlier knee max (z +6.7) |
| `carla_0_99_99_t32-41_shift` | B | 6_carla_0_99_99 32.4–41.0 s | 35.4 / 20.0 | 12 / 3 | human steps; K1 feet move 20 cm; outlier knee max (z +7.8) |
| `carla_0_99_99_t43-49_shift` | B | 6_carla_0_99_99 42.6–48.8 s | 30.4 / 17.1 | 8 / 2 | human steps; outlier knee max (z +5.2) |
| `carla_1_10_10_t177-182_shift` | B | 6_carla_1_10_10 176.8–181.6 s | 14.7 / 9.6 | 5 / 2 | outlier knee max (z +5.2) |
| `carla_1_10_10_t190-200_shift` | B | 6_carla_1_10_10 190.5–200.2 s | 17.6 / 11.8 | 10 / 3 | leg at limit 7%; outlier knee max (z +6.0) |
| `carla_1_10_10_t224-229_shift` | B | 6_carla_1_10_10 224.4–228.9 s | 12.0 / 4.5 | 8 / 3 | outlier knee max (z +6.4) |
| `carla_1_10_10_t285-289_shift` | B | 6_carla_1_10_10 285.0–289.0 s | 18.4 / 5.3 | 13 / 5 | outlier trunk drop (z +4.1); outlier knee max (z +4.9) |
| `carla_1_10_10_t295-300_shift` | B | 6_carla_1_10_10 295.2–300.3 s | 18.8 / 11.4 | 24 / 10 | outlier knee max (z +4.2) |
| `carla_1_10_10_t411-415_shift` | B | 6_carla_1_10_10 410.6–414.6 s | 14.1 / 7.7 | 6 / 2 | outlier knee max (z +3.9) |
| `carla_1_10_10_t443-455` | A | 6_carla_1_10_10 442.7–454.9 s | 7.8 / 3.8 | 11 / 5 | elbow bend at limit 7% |
| `carla_1_10_10_t486-490_shift` | B | 6_carla_1_10_10 486.2–490.2 s | 15.6 / 3.6 | 18 / 5 | outlier trunk drop (z +3.9); outlier knee max (z +7.1) |
| `carla_1_10_10_t557-562_shift` | B | 6_carla_1_10_10 557.5–562.2 s | 15.4 / 3.2 | 5 / 1 | outlier knee max (z +4.9) |
| `carla_1_10_10_t560-572` | A | 6_carla_1_10_10 560.2–571.7 s | 7.7 / 2.5 | 11 / 4 | leg at limit 10% |
| `carla_1_10_10_t569-573_shift` | B | 6_carla_1_10_10 568.7–572.7 s | 17.3 / 4.3 | 17 / 4 | leg at limit 32%; outlier knee max (z +4.1) |
| `carla_1_10_10_t72-85` | A | 6_carla_1_10_10 72.2–85.1 s | 8.5 / 8.3 | 14 / 4 | K1 feet move 8 cm |
| `carla_1_11_11_t108-112_shift` | B | 6_carla_1_11_11 107.7–111.7 s | 18.9 / 4.8 | 14 / 7 | knee 66 deg; outlier knee max (z +10.1) |
| `carla_1_11_11_t132-137_shift` | B | 6_carla_1_11_11 132.1–136.9 s | 18.9 / 9.6 | 10 / 2 | leg at limit 8%; outlier knee max (z +5.0) |
| `carla_1_11_11_t146-150_shift` | B | 6_carla_1_11_11 145.9–150.2 s | 24.5 / 14.1 | 26 / 9 | outlier knee max (z +6.5) |
| `carla_1_11_11_t158-163_shift` | B | 6_carla_1_11_11 158.3–162.6 s | 17.9 / 10.6 | 9 / 3 | leg at limit 11% |
| `carla_1_11_11_t161-170` | A | 6_carla_1_11_11 160.6–169.8 s | 5.0 / 4.4 | 4 / 1 | leg at limit 6% |
| `carla_1_11_11_t175-184` | A | 6_carla_1_11_11 175.0–183.5 s | 4.2 / 3.7 | 19 / 7 | leg at limit 6% |
| `carla_1_11_11_t243-247_shift` | B | 6_carla_1_11_11 243.4–247.4 s | 19.6 / 5.3 | 21 / 7 | outlier trunk drop (z +4.9); outlier knee max (z +3.7) |
| `carla_1_11_11_t249-253_shift` | B | 6_carla_1_11_11 248.5–253.2 s | 24.8 / 14.2 | 11 / 3 | outlier knee max (z +4.5) |
| `carla_1_11_11_t253-258_shift` | B | 6_carla_1_11_11 253.2–258.2 s | 15.2 / 3.5 | 11 / 4 | outlier knee max (z +6.6) |
| `carla_1_11_11_t307-313_shift` | B | 6_carla_1_11_11 306.6–312.9 s | 13.1 / 3.4 | 5 / 2 | leg at limit 18%; outlier trunk drop (z +3.8) |
| `carla_1_11_11_t346-350_shift` | B | 6_carla_1_11_11 346.2–350.2 s | 15.6 / 3.2 | 6 / 3 | outlier knee max (z +4.1) |
| `carla_1_11_11_t361-366` | A | 6_carla_1_11_11 361.3–366.3 s | 5.1 / 1.4 | 11 / 5 | self-collision left_hand_end_collision / right_hand_end_collision 0.8 s (at 4.2 s, 17 mm) |
| `carla_1_11_11_t364-368_shift` | B | 6_carla_1_11_11 363.5–367.5 s | 21.1 / 6.9 | 22 / 11 | outlier knee max (z +5.5); self-collision left_hand_end_collision / right_hand_end_collision 0.8 s (at 2.0 s, 17 mm) |
| `carla_1_11_11_t377-384` | A | 6_carla_1_11_11 377.2–384.0 s | 6.7 / 3.4 | 9 / 4 | outlier trunk drop (z +4.9) |
| `carla_1_11_11_t430-434_shift` | B | 6_carla_1_11_11 429.5–433.5 s | 22.7 / 9.8 | 8 / 2 | outlier knee max (z +3.6) |
| `carla_1_11_11_t486-490_shift` | B | 6_carla_1_11_11 486.2–490.4 s | 21.9 / 6.3 | 12 / 3 | outlier trunk drop (z +3.9); outlier knee max (z +5.2) |
| `carla_1_11_11_t566-570_shift` | B | 6_carla_1_11_11 565.7–569.7 s | 20.1 / 5.8 | 9 / 3 | outlier trunk drop (z +4.2); outlier knee max (z +7.0) |
| `carla_1_11_11_t636-642_shift` | B | 6_carla_1_11_11 636.4–641.5 s | 14.6 / 7.8 | 13 / 2 | outlier knee max (z +4.7) |
| `carla_1_12_12_t168-172_shift` | B | 6_carla_1_12_12 168.2–172.2 s | 19.1 / 7.5 | 30 / 7 | outlier knee max (z +3.7) |
| `carla_1_12_12_t231-238_shift` | B | 6_carla_1_12_12 230.7–238.5 s | 14.8 / 5.5 | 12 / 5 | outlier knee max (z +4.9) |
| `carla_1_12_12_t257-261_shift` | B | 6_carla_1_12_12 256.8–261.2 s | 12.5 / 7.3 | 15 / 4 | outlier knee max (z +4.7) |
| `carla_1_12_12_t301-309` | A | 6_carla_1_12_12 300.7–309.4 s | 5.7 / 5.0 | 37 / 11 | shoulder at limit 52% |
| `carla_1_12_12_t325-330_shift` | B | 6_carla_1_12_12 325.1–330.3 s | 14.2 / 6.5 | 19 / 6 | outlier knee max (z +4.3) |
| `carla_1_12_12_t341-346_shift` | B | 6_carla_1_12_12 341.5–345.5 s | 12.3 / 2.9 | 22 / 4 | outlier knee max (z +6.7) |
| `carla_1_12_12_t379-383_shift` | B | 6_carla_1_12_12 379.0–383.3 s | 20.6 / 5.6 | 3 / 1 | knee 63 deg; leg at limit 43%; outlier trunk drop (z +4.5); outlier knee max (z +8.9) |
| `carla_1_12_12_t418-424_shift` | B | 6_carla_1_12_12 417.9–423.9 s | 15.5 / 6.8 | 12 / 4 | head at limit 12%; leg at limit 7%; outlier knee max (z +4.9) |
| `carla_1_12_12_t425-433_shift` | B | 6_carla_1_12_12 424.6–432.9 s | 17.4 / 10.5 | 14 / 6 | head at limit 13%; elbow bend at limit 21% |
| `carla_1_12_12_t446-450_shift` | B | 6_carla_1_12_12 445.8–449.8 s | 13.0 / 2.9 | 4 / 1 | outlier knee max (z +4.3) |
| `carla_1_12_12_t487-491_shift` | B | 6_carla_1_12_12 486.6–490.6 s | 26.2 / 11.5 | 11 / 4 | human steps; outlier knee max (z +4.5) |
| `carla_1_12_12_t50-54_shift` | B | 6_carla_1_12_12 50.3–54.3 s | 17.6 / 4.2 | 9 / 4 | outlier knee max (z +3.6) |
| `carla_1_12_12_t504-509_shift` | B | 6_carla_1_12_12 503.8–509.0 s | 18.5 / 5.8 | 23 / 7 | leg at limit 5% |
| `carla_1_12_12_t83-87_shift` | B | 6_carla_1_12_12 83.2–87.2 s | 20.9 / 5.8 | 16 / 5 | leg at limit 12%; outlier trunk drop (z +5.0); outlier knee max (z +4.0) |
| `carla_1_1_1_t190-194_shift` | B | 6_carla_1_1_1 189.6–193.6 s | 24.5 / 14.2 | 10 / 4 | outlier knee max (z +5.9) |
| `carla_1_1_1_t270-277_shift` | B | 6_carla_1_1_1 270.1–276.7 s | 19.2 / 11.3 | 10 / 3 | outlier knee max (z +4.9) |
| `carla_1_1_1_t495-499_shift` | B | 6_carla_1_1_1 494.5–498.5 s | 26.8 / 16.6 | 3 / 1 | human steps; outlier knee max (z +6.0) |
| `carla_1_1_1_t550-555_shift` | B | 6_carla_1_1_1 550.2–554.9 s | 16.1 / 12.1 | 13 / 5 | outlier trunk drop (z +3.9); outlier knee max (z +7.8) |
| `carla_1_1_1_t581-592` | A | 6_carla_1_1_1 581.3–591.8 s | 0.5 / 0.3 | 1 / 1 | outlier knee max (z -3.9) |
| `carla_1_2_2_t174-185_shift` | B | 6_carla_1_2_2 173.5–185.1 s | 15.1 / 5.1 | 15 / 4 | outlier knee max (z +7.3) |
| `carla_1_2_2_t327-332_shift` | B | 6_carla_1_2_2 327.4–332.1 s | 17.1 / 10.7 | 12 / 4 | outlier knee max (z +6.7) |
| `carla_1_2_2_t342-350_shift` | B | 6_carla_1_2_2 342.2–349.9 s | 35.1 / 21.3 | 7 / 3 | human steps; K1 feet move 21 cm; outlier knee max (z +5.8) |
| `carla_1_2_2_t372-376` | A | 6_carla_1_2_2 372.3–376.4 s | 8.0 / 2.7 | 7 / 3 | knee 62 deg; outlier knee max (z +8.5) |
| `carla_1_2_2_t383-388_shift` | B | 6_carla_1_2_2 383.4–388.0 s | 14.7 / 9.9 | 17 / 3 | knee 64 deg; outlier knee max (z +9.4) |
| `carla_1_2_2_t386-394` | A | 6_carla_1_2_2 386.0–394.3 s | 5.9 / 6.4 | 14 / 5 | knee 60 deg; outlier knee max (z +8.0) |
| `carla_1_2_2_t425-432_shift` | B | 6_carla_1_2_2 425.3–432.4 s | 19.1 / 11.0 | 3 / 2 | outlier knee max (z +4.4) |
| `carla_1_2_2_t499-508` | A | 6_carla_1_2_2 498.7–508.4 s | 6.1 / 1.6 | 19 / 6 | self-collision head_2_collision / right_hand_end_collision 0.9 s (at 7.8 s, 13 mm) |
| `carla_1_2_2_t591-595_shift` | B | 6_carla_1_2_2 591.2–595.2 s | 24.2 / 13.5 | 23 / 6 | outlier knee max (z +6.0) |
| `carla_1_2_2_t629-633_shift` | B | 6_carla_1_2_2 629.5–633.5 s | 14.5 / 2.8 | 13 / 4 | outlier knee max (z +6.0) |
| `carla_1_3_3_t114-134` | A | 6_carla_1_3_3 114.4–134.1 s | 1.4 / 0.7 | 14 / 6 | self-collision head_2_collision / left_hand_end_collision 1.8 s (at 9.9 s, 19 mm) |
| `carla_1_3_3_t180-187_shift` | B | 6_carla_1_3_3 180.0–186.7 s | 18.4 / 13.0 | 18 / 6 | outlier knee max (z +4.0) |
| `carla_1_3_3_t211-216_shift` | B | 6_carla_1_3_3 211.4–216.2 s | 16.5 / 3.9 | 13 / 6 | outlier knee max (z +7.2) |
| `carla_1_3_3_t24-28_shift` | B | 6_carla_1_3_3 24.3–28.3 s | 24.9 / 13.8 | 10 / 3 | outlier knee max (z +5.1) |
| `carla_1_3_3_t257-267` | A | 6_carla_1_3_3 256.9–266.7 s | 9.4 / 2.8 | 9 / 3 | outlier knee max (z +5.7) |
| `carla_1_3_3_t349-358` | A | 6_carla_1_3_3 348.8–358.0 s | 8.1 / 2.1 | 13 / 4 | outlier knee max (z +3.5) |
| `carla_1_3_3_t356-361_shift` | B | 6_carla_1_3_3 356.0–360.9 s | 17.2 / 9.0 | 16 / 4 | outlier knee max (z +4.7) |
| `carla_1_3_3_t407-420` | A | 6_carla_1_3_3 406.7–419.6 s | 9.8 / 2.7 | 10 / 3 | outlier knee max (z +4.7) |
| `carla_1_3_3_t416-420_shift` | B | 6_carla_1_3_3 415.6–419.6 s | 9.2 / 2.0 | 6 / 2 | outlier knee max (z +3.6) |
| `carla_1_3_3_t430-438_shift` | B | 6_carla_1_3_3 430.4–437.5 s | 13.1 / 2.8 | 18 / 5 | outlier knee max (z +5.4) |
| `carla_1_3_3_t439-445_shift` | B | 6_carla_1_3_3 438.8–445.1 s | 13.7 / 5.3 | 13 / 4 | knee 61 deg; outlier knee max (z +8.4) |
| `carla_1_3_3_t44-48_shift` | B | 6_carla_1_3_3 44.0–48.0 s | 16.6 / 6.5 | 8 / 3 | knee 66 deg; leg at limit 14%; outlier knee max (z +10.0) |
| `carla_1_3_3_t477-481_shift` | B | 6_carla_1_3_3 476.8–480.8 s | 24.6 / 13.6 | 14 / 6 | outlier knee max (z +5.7) |
| `carla_1_3_3_t488-492_shift` | B | 6_carla_1_3_3 488.5–492.5 s | 22.5 / 12.9 | 18 / 7 | outlier knee max (z +3.7); self-collision head_2_collision / right_hand_end_collision 0.2 s (at 3.8 s, 11 mm) |
| `carla_1_3_3_t489-501` | A | 6_carla_1_3_3 489.3–500.7 s | 1.5 / 0.6 | 12 / 6 | self-collision head_2_collision / right_hand_end_collision 1.4 s (at 2.9 s, 21 mm) |
| `carla_1_3_3_t538-543` | A | 6_carla_1_3_3 537.8–542.7 s | 2.0 / 1.0 | 11 / 6 | elbow bend at limit 12% |
| `carla_1_3_3_t565-570_shift` | B | 6_carla_1_3_3 564.8–569.9 s | 7.6 / 2.6 | 11 / 5 | outlier knee max (z +3.7) |
| `carla_1_3_3_t678-682_shift` | B | 6_carla_1_3_3 677.9–681.9 s | 16.0 / 3.5 | 15 / 5 | leg at limit 13%; outlier knee max (z +5.9) |
| `carla_1_3_3_t94-99_shift` | B | 6_carla_1_3_3 94.0–98.8 s | 20.7 / 6.4 | 16 / 3 | knee 61 deg; outlier trunk drop (z +4.0); outlier knee max (z +8.2) |
| `carla_1_4_4_t26-31_shift` | B | 6_carla_1_4_4 26.0–30.6 s | 14.6 / 8.9 | 9 / 3 | outlier knee max (z +6.3) |
| `carla_1_4_4_t333-337_shift` | B | 6_carla_1_4_4 332.8–336.8 s | 20.2 / 10.1 | 20 / 8 | knee 81 deg; outlier knee max (z +15.1) |
| `carla_1_4_4_t36-43_shift` | B | 6_carla_1_4_4 36.2–43.3 s | 27.8 / 14.9 | 8 / 2 | human steps; outlier knee max (z +6.7) |
| `carla_1_4_4_t377-383_shift` | B | 6_carla_1_4_4 377.3–383.0 s | 7.3 / 2.3 | 23 / 7 | outlier knee max (z +5.0) |
| `carla_1_4_4_t530-535_shift` | B | 6_carla_1_4_4 530.0–534.7 s | 11.3 / 7.5 | 4 / 2 | outlier knee max (z +4.9) |
| `carla_1_4_4_t559-563_shift` | B | 6_carla_1_4_4 558.7–562.9 s | 15.9 / 4.9 | 13 / 3 | outlier knee max (z +7.7) |
| `carla_1_4_4_t616-620_shift` | B | 6_carla_1_4_4 615.9–619.9 s | 18.2 / 8.6 | 12 / 4 | outlier knee max (z +7.3) |
| `carla_1_4_4_t64-70` | A | 6_carla_1_4_4 64.2–70.2 s | 7.6 / 1.3 | 16 / 6 | outlier knee max (z +3.8) |
| `carla_1_5_5_t156-160_shift` | B | 6_carla_1_5_5 156.3–160.3 s | 24.9 / 13.7 | 13 / 4 | outlier knee max (z +4.0) |
| `carla_1_5_5_t196-200_shift` | B | 6_carla_1_5_5 196.2–200.2 s | 13.4 / 8.7 | 2 / 1 | outlier knee max (z +4.9) |
| `carla_1_5_5_t44-48_shift` | B | 6_carla_1_5_5 44.0–48.0 s | 18.0 / 4.5 | 8 / 2 | outlier knee max (z +5.6) |
| `carla_1_6_6_t175-186_shift` | B | 6_carla_1_6_6 175.4–186.2 s | 25.7 / 14.6 | 9 / 3 | human steps; outlier knee max (z +6.3) |
| `carla_1_6_6_t201-205_shift` | B | 6_carla_1_6_6 201.3–205.3 s | 7.7 / 1.9 | 17 / 7 | leg at limit 8%; outlier trunk drop (z +3.9); outlier knee max (z +4.1) |
| `carla_1_6_6_t224-229_shift` | B | 6_carla_1_6_6 224.2–228.6 s | 14.0 / 3.0 | 12 / 4 | outlier knee max (z +7.8) |
| `carla_1_6_6_t247-251_shift` | B | 6_carla_1_6_6 246.6–250.6 s | 15.7 / 7.9 | 7 / 2 | outlier knee max (z +3.5) |
| `carla_1_6_6_t281-286_shift` | B | 6_carla_1_6_6 281.4–286.5 s | 8.1 / 1.9 | 47 / 16 | outlier knee max (z +3.5) |
| `carla_1_6_6_t44-49_shift` | B | 6_carla_1_6_6 43.7–48.8 s | 15.9 / 8.6 | 20 / 7 | outlier knee max (z +7.6) |
| `carla_1_6_6_t82-94` | A | 6_carla_1_6_6 82.1–93.8 s | 9.8 / 2.2 | 29 / 9 | outlier knee max (z +5.1) |
| `carla_1_6_6_t90-94_shift` | B | 6_carla_1_6_6 89.9–93.9 s | 9.3 / 2.2 | 22 / 8 | outlier knee max (z +5.1) |
| `carla_1_7_7_t173-178_shift` | B | 6_carla_1_7_7 173.4–177.7 s | 14.8 / 3.6 | 12 / 3 | knee 64 deg; outlier knee max (z +9.5) |
| `carla_1_7_7_t21-27` | A | 6_carla_1_7_7 21.3–26.5 s | 9.9 / 2.2 | 11 / 5 | outlier knee max (z +5.1) |
| `carla_1_7_7_t227-231_shift` | B | 6_carla_1_7_7 227.1–231.1 s | 11.5 / 4.3 | 13 / 4 | outlier knee max (z +4.3) |
| `carla_1_7_7_t27-35` | A | 6_carla_1_7_7 26.5–35.1 s | 4.2 / 0.9 | 18 / 8 | self-collision head_2_collision / right_hand_end_collision 0.7 s (at 4.2 s, 13 mm) |
| `carla_1_7_7_t3-7_shift` | B | 6_carla_1_7_7 2.7–6.7 s | 24.7 / 14.0 | 12 / 3 | outlier knee max (z +5.1) |
| `carla_1_7_7_t316-321_shift` | B | 6_carla_1_7_7 316.0–320.6 s | 23.4 / 5.5 | 16 / 5 | outlier knee max (z +7.2) |
| `carla_1_7_7_t403-407_shift` | B | 6_carla_1_7_7 402.7–406.7 s | 19.8 / 6.5 | 39 / 13 | leg at limit 7%; outlier trunk drop (z +4.2) |
| `carla_1_7_7_t575-583` | A | 6_carla_1_7_7 575.3–582.6 s | 4.9 / 3.2 | 20 / 6 | elbow bend at limit 23% |
| `carla_1_8_8_t0-5` | A | 6_carla_1_8_8 0.0–5.1 s | 9.3 / 5.3 | 16 / 4 | outlier knee max (z +3.5) |
| `carla_1_8_8_t115-120_shift` | B | 6_carla_1_8_8 115.4–120.4 s | 15.7 / 6.4 | 22 / 6 | outlier knee max (z +6.8) |
| `carla_1_8_8_t171-176` | A | 6_carla_1_8_8 171.0–176.0 s | 4.3 / 2.2 | 19 / 6 | elbow bend at limit 17% |
| `carla_1_8_8_t22-26_shift` | B | 6_carla_1_8_8 21.5–26.0 s | 11.2 / 7.1 | 11 / 6 | outlier knee max (z +3.8) |
| `carla_1_8_8_t231-238` | A | 6_carla_1_8_8 231.5–237.7 s | 2.8 / 1.7 | 13 / 5 | elbow bend at limit 25% |
| `carla_1_8_8_t318-322_shift` | B | 6_carla_1_8_8 318.2–322.3 s | 22.2 / 13.5 | 20 / 4 | outlier knee max (z +4.1) |
| `carla_1_8_8_t320-325` | A | 6_carla_1_8_8 320.3–324.9 s | 9.9 / 1.9 | 19 / 5 | outlier knee max (z +4.6) |
| `carla_1_8_8_t38-42_shift` | B | 6_carla_1_8_8 38.0–42.0 s | 42.6 / 25.1 | 8 / 3 | human steps; K1 feet move 25 cm; outlier knee max (z +7.1) |
| `carla_1_8_8_t380-385` | A | 6_carla_1_8_8 380.0–385.5 s | 9.7 / 3.2 | 32 / 10 | outlier knee max (z +4.9) |
| `carla_1_8_8_t382-386_shift` | B | 6_carla_1_8_8 382.1–386.1 s | 11.2 / 3.7 | 31 / 8 | leg at limit 8%; outlier knee max (z +5.9) |
| `carla_1_8_8_t387-396_shift` | B | 6_carla_1_8_8 386.8–396.3 s | 24.2 / 13.2 | 19 / 8 | outlier knee max (z +6.6) |
| `carla_1_8_8_t403-409_shift` | B | 6_carla_1_8_8 403.4–409.4 s | 21.3 / 12.6 | 16 / 3 | outlier knee max (z +5.3) |
| `carla_1_8_8_t428-432_shift` | B | 6_carla_1_8_8 428.2–432.2 s | 17.5 / 4.5 | 11 / 3 | outlier trunk drop (z +4.2); outlier knee max (z +5.0) |
| `carla_1_8_8_t440-444_shift` | B | 6_carla_1_8_8 439.5–444.2 s | 21.8 / 7.8 | 13 / 3 | knee 62 deg; outlier knee max (z +8.7) |
| `carla_1_8_8_t455-460_shift` | B | 6_carla_1_8_8 455.3–459.6 s | 8.8 / 2.2 | 10 / 3 | outlier knee max (z +4.3) |
| `carla_1_8_8_t462-466_shift` | B | 6_carla_1_8_8 462.0–466.0 s | 15.0 / 4.2 | 11 / 3 | leg at limit 8%; outlier knee max (z +5.5) |
| `carla_1_8_8_t495-499_shift` | B | 6_carla_1_8_8 495.4–499.4 s | 12.2 / 4.5 | 6 / 2 | knee 71 deg; outlier knee max (z +11.6) |
| `carla_1_8_8_t589-594_shift` | B | 6_carla_1_8_8 589.2–593.8 s | 20.7 / 7.9 | 19 / 6 | knee 62 deg; outlier knee max (z +8.7) |
| `carla_1_8_8_t646-655_shift` | B | 6_carla_1_8_8 646.1–654.6 s | 12.5 / 8.3 | 16 / 4 | outlier knee max (z +4.7) |
| `carla_1_9_9_t16-20_shift` | B | 6_carla_1_9_9 16.0–20.0 s | 25.0 / 14.6 | 13 / 4 | outlier knee max (z +4.9) |
| `carla_1_9_9_t180-185_shift` | B | 6_carla_1_9_9 180.4–184.9 s | 17.7 / 3.5 | 34 / 11 | outlier knee max (z +6.6) |
| `carla_1_9_9_t19-25` | A | 6_carla_1_9_9 19.0–25.1 s | 7.9 / 3.6 | 13 / 4 | leg at limit 14% |
| `carla_1_9_9_t23-28_shift` | B | 6_carla_1_9_9 23.1–27.6 s | 14.4 / 8.3 | 12 / 4 | leg at limit 21%; outlier knee max (z +4.0) |
| `carla_1_9_9_t235-239_shift` | B | 6_carla_1_9_9 235.3–239.3 s | 17.4 / 5.3 | 17 / 3 | outlier trunk drop (z +3.7); outlier knee max (z +5.7) |
| `carla_1_9_9_t285-291_shift` | B | 6_carla_1_9_9 285.4–291.1 s | 17.7 / 8.2 | 9 / 3 | outlier trunk drop (z +3.7); outlier knee max (z +5.2) |
| `carla_1_9_9_t325-330_shift` | B | 6_carla_1_9_9 325.0–329.7 s | 14.0 / 9.6 | 24 / 8 | knee 66 deg; outlier knee max (z +10.1) |
| `carla_1_9_9_t365-370_shift` | B | 6_carla_1_9_9 365.2–370.3 s | 15.9 / 4.2 | 11 / 3 | outlier knee max (z +7.7) |
| `carla_1_9_9_t371-378_shift` | B | 6_carla_1_9_9 370.6–377.8 s | 13.8 / 3.5 | 15 / 5 | outlier knee max (z +4.6) |
| `carla_1_9_9_t386-390_shift` | B | 6_carla_1_9_9 385.9–390.4 s | 13.8 / 6.6 | 18 / 5 | knee 66 deg; outlier knee max (z +10.2) |
| `carla_1_9_9_t398-403_shift` | B | 6_carla_1_9_9 398.5–403.0 s | 20.8 / 11.5 | 13 / 3 | outlier knee max (z +5.2) |
| `carla_1_9_9_t412-428_shift` | B | 6_carla_1_9_9 411.7–427.8 s | 23.9 / 6.8 | 18 / 6 | outlier knee max (z +6.3) |
| `carla_1_9_9_t573-577_shift` | B | 6_carla_1_9_9 573.3–577.3 s | 18.3 / 5.8 | 20 / 5 | leg at limit 7%; outlier knee max (z +5.1) |
| `carla_1_9_9_t58-62_shift` | B | 6_carla_1_9_9 57.7–62.0 s | 12.0 / 3.1 | 20 / 6 | outlier knee max (z +6.0) |
| `carla_1_9_9_t608-612_shift` | B | 6_carla_1_9_9 608.2–612.2 s | 14.9 / 4.5 | 9 / 7 | knee 60 deg; outlier knee max (z +8.0) |
| `carla_1_9_9_t85-89_shift` | B | 6_carla_1_9_9 84.8–88.8 s | 25.3 / 14.1 | 9 / 2 | human steps; knee 61 deg; outlier knee max (z +8.2) |
| `carla_1_9_9_t88-95` | A | 6_carla_1_9_9 88.3–95.4 s | 5.2 / 2.0 | 11 / 4 | leg at limit 10% |
| `carla_1_9_9_t93-97_shift` | B | 6_carla_1_9_9 93.4–97.5 s | 7.8 / 5.8 | 11 / 4 | outlier knee max (z +3.9) |
| `carlos_0_103_103_t20-37` | A | 15_carlos_0_103_103 20.2–37.1 s | 1.3 / 0.8 | 8 / 3 | shoulder at limit 12%; self-collision right_hand_collision / trunk_collision 1.3 s (at 14.7 s, 8 mm) |
| `carlos_0_103_103_t71-88` | A | 15_carlos_0_103_103 70.9–87.8 s | 5.9 / 3.2 | 10 / 3 | self-collision right_hand_collision / trunk_collision 0.1 s (at 13.4 s, 7 mm) |
| `carlos_0_104_104_t19-38` | A | 15_carlos_0_104_104 18.8–37.7 s | 0.3 / 0.4 | 8 / 3 | elbow bend at limit 14% |
| `carlos_0_104_104_t57-75` | A | 15_carlos_0_104_104 56.5–75.4 s | 0.4 / 0.5 | 7 / 3 | self-collision right_hand_collision / trunk_collision 0.4 s (at 1.5 s, 7 mm) |
| `carlos_0_111_111_t59-75` | A | 15_carlos_0_111_111 58.6–74.8 s | 1.5 / 0.8 | 11 / 3 | self-collision right_hand_collision / trunk_collision 1.0 s (at 10.1 s, 10 mm) |
| `carlos_0_112_112_t0-17` | A | 15_carlos_0_112_112 0.0–17.4 s | 1.6 / 0.9 | 9 / 2 | self-collision right_hand_collision / trunk_collision 0.6 s (at 14.4 s, 11 mm) |
| `carlos_0_13_13_t52-69` | A | 15_carlos_0_13_13 51.7–69.0 s | 9.4 / 5.5 | 17 / 5 | outlier knee max (z +4.1) |
| `carlos_0_14_14_t44-59` | A | 15_carlos_0_14_14 43.7–59.2 s | 2.0 / 0.8 | 17 / 5 | self-collision right_hand_collision / trunk_collision 2.1 s (at 0.2 s, 15 mm) |
| `carlos_0_14_14_t57-68_shift` | B | 15_carlos_0_14_14 57.2–67.9 s | 13.8 / 7.5 | 27 / 6 | self-collision right_hand_collision / trunk_collision 0.4 s (at 0.1 s, 8 mm); hand presses into leg 9 mm for 0.3 s (at 3.9 s) |
| `carlos_0_14_14_t8-15_shift` | B | 15_carlos_0_14_14 7.8–14.8 s | 10.8 / 5.4 | 23 / 7 | elbow bend at limit 7% |
| `carlos_0_15_15_t17-30` | A | 15_carlos_0_15_15 17.0–30.4 s | 2.2 / 0.7 | 19 / 5 | self-collision right_hand_collision / trunk_collision 1.0 s (at 11.1 s, 12 mm); hand presses into leg 8 mm for 0.2 s (at 0.9 s) |
| `carlos_0_15_15_t88-103` | A | 15_carlos_0_15_15 87.6–102.8 s | 10.4 / 5.2 | 16 / 5 | human steps |
| `carlos_0_16_16_t39-59` | A | 15_carlos_0_16_16 39.3–59.0 s | 1.8 / 0.8 | 16 / 5 | elbow bend at limit 9% |
| `carlos_0_16_16_t79-98` | A | 15_carlos_0_16_16 78.6–98.3 s | 1.1 / 0.6 | 18 / 5 | hand presses into leg 22 mm for 0.6 s (at 19.1 s) |
| `carlos_0_1_1_t65-78` | A | 15_carlos_0_1_1 65.4–78.0 s | 1.2 / 1.0 | 20 / 8 | elbow bend at limit 17% |
| `carlos_0_1_1_t82-93` | A | 15_carlos_0_1_1 82.4–93.0 s | 4.9 / 0.9 | 17 / 5 | self-collision right_hand_collision / trunk_collision 2.1 s (at 2.9 s, 16 mm) |
| `carlos_0_66_66_t14-23_shift` | B | 15_carlos_0_66_66 14.3–22.6 s | 24.3 / 13.5 | 17 / 6 | outlier knee max (z +4.6) |
| `carlos_0_66_66_t29-36_shift` | B | 15_carlos_0_66_66 28.8–35.9 s | 22.0 / 9.9 | 30 / 8 | outlier knee max (z +3.9) |
| `carlos_0_66_66_t71-78_shift` | B | 15_carlos_0_66_66 71.1–77.7 s | 26.2 / 15.2 | 32 / 8 | human steps |
| `carlos_0_73_73_t30-46_shift` | B | 15_carlos_0_73_73 30.4–46.2 s | 14.3 / 8.5 | 45 / 11 | outlier knee max (z +5.4) |
| `carlos_0_74_74_t31-41` | A | 15_carlos_0_74_74 31.1–41.3 s | 1.2 / 0.8 | 24 / 6 | self-collision right_hand_collision / trunk_collision 0.9 s (at 6.6 s, 12 mm) |
| `carlos_0_74_74_t39-49_shift` | B | 15_carlos_0_74_74 39.3–48.7 s | 17.0 / 9.1 | 31 / 7 | self-collision right_hand_collision / trunk_collision 0.3 s (at 8.8 s, 11 mm) |
| `carlos_0_74_74_t47-55` | A | 15_carlos_0_74_74 46.7–55.0 s | 8.0 / 1.5 | 26 / 6 | self-collision right_hand_collision / trunk_collision 0.3 s (at 1.4 s, 11 mm) |
| `carlos_0_81_81_t26-46` | A | 15_carlos_0_81_81 26.1–45.5 s | 1.0 / 0.5 | 14 / 4 | self-collision right_hand_collision / trunk_collision 0.3 s (at 9.0 s, 11 mm) |
| `carlos_0_81_81_t46-65` | A | 15_carlos_0_81_81 45.5–65.0 s | 1.2 / 0.8 | 14 / 4 | self-collision right_hand_collision / trunk_collision 0.5 s (at 2.0 s, 11 mm) |
| `carlos_0_81_81_t65-84` | A | 15_carlos_0_81_81 65.0–84.5 s | 0.8 / 0.7 | 12 / 4 | self-collision right_hand_collision / trunk_collision 1.2 s (at 6.8 s, 22 mm) |
| `carlos_0_82_82_t0-17` | A | 15_carlos_0_82_82 0.0–17.1 s | 5.2 / 2.2 | 10 / 3 | self-collision right_hand_collision / trunk_collision 2.4 s (at 11.4 s, 13 mm) |
| `carlos_0_82_82_t17-34` | A | 15_carlos_0_82_82 17.1–34.3 s | 1.1 / 1.2 | 9 / 3 | self-collision right_hand_collision / trunk_collision 0.6 s (at 0.5 s, 11 mm) |
| `carlos_0_82_82_t34-51` | A | 15_carlos_0_82_82 34.3–51.4 s | 0.8 / 0.8 | 11 / 3 | self-collision right_hand_collision / trunk_collision 2.2 s (at 1.3 s, 18 mm) |
| `carlos_0_82_82_t69-86` | A | 15_carlos_0_82_82 68.6–85.7 s | 0.9 / 0.6 | 18 / 5 | self-collision right_hand_collision / trunk_collision 0.9 s (at 2.9 s, 25 mm) |
| `carlos_0_87_87_t36-54` | A | 15_carlos_0_87_87 35.9–53.9 s | 1.3 / 0.9 | 19 / 6 | self-collision right_hand_collision / trunk_collision 0.4 s (at 10.0 s, 6 mm) |
| `carlos_0_88_88_t36-54` | A | 15_carlos_0_88_88 35.9–53.8 s | 0.8 / 0.7 | 18 / 6 | self-collision right_hand_collision / trunk_collision 1.0 s (at 2.9 s, 22 mm) |
| `carlos_0_88_88_t54-72` | A | 15_carlos_0_88_88 53.8–71.8 s | 0.6 / 0.5 | 13 / 5 | self-collision right_hand_collision / trunk_collision 0.4 s (at 7.2 s, 11 mm) |
| `carlos_0_88_88_t72-90` | A | 15_carlos_0_88_88 71.8–89.7 s | 0.6 / 0.5 | 17 / 5 | self-collision right_hand_collision / trunk_collision 1.2 s (at 13.7 s, 21 mm) |
| `carlos_0_95_95_t28-43` | A | 15_carlos_0_95_95 27.9–42.5 s | 4.2 / 0.9 | 20 / 5 | self-collision right_hand_collision / trunk_collision 0.9 s (at 13.6 s, 19 mm) |
| `carlos_0_95_95_t41-47_shift` | B | 15_carlos_0_95_95 40.5–46.8 s | 14.9 / 7.9 | 25 / 6 | self-collision right_hand_collision / trunk_collision 0.9 s (at 0.9 s, 19 mm) |
| `carlos_0_95_95_t55-71` | A | 15_carlos_0_95_95 55.3–70.8 s | 1.3 / 0.7 | 20 / 6 | self-collision right_hand_collision / trunk_collision 0.4 s (at 6.6 s, 10 mm) |
| `carlos_0_9_9_t0-11` | A | 15_carlos_0_9_9 0.0–11.2 s | 3.5 / 2.8 | 19 / 6 | elbow bend at limit 9% |
| `carlos_0_9_9_t9-14_shift` | B | 15_carlos_0_9_9 9.2–14.3 s | 15.0 / 8.4 | 18 / 6 | elbow bend at limit 11% |
| `carlos_1_1_1_t119-130_shift` | B | 15_carlos_1_1_1 119.3–129.9 s | 23.6 / 12.4 | 12 / 4 | leg at limit 8%; outlier knee max (z +3.7) |
| `carlos_1_1_1_t163-180` | A | 15_carlos_1_1_1 163.0–180.5 s | 0.9 / 0.6 | 15 / 5 | elbow bend at limit 6% |
| `carlos_1_1_1_t231-241_shift` | B | 15_carlos_1_1_1 231.0–240.9 s | 15.1 / 6.5 | 5 / 2 | outlier knee max (z +4.1) |
| `carlos_1_1_1_t413-432` | A | 15_carlos_1_1_1 413.4–432.2 s | 7.8 / 3.7 | 13 / 4 | shoulder at limit 6% |
| `carlos_1_1_1_t542-550_shift` | B | 15_carlos_1_1_1 542.5–550.1 s | 24.1 / 12.7 | 11 / 3 | leg at limit 10%; outlier knee max (z +7.1) |
| `carlos_1_1_1_t606-610_shift` | B | 15_carlos_1_1_1 606.0–610.0 s | 24.6 / 12.7 | 20 / 5 | outlier knee max (z +5.0) |
| `carlos_1_2_2_t116-126` | A | 15_carlos_1_2_2 116.4–126.4 s | 3.8 / 1.4 | 11 / 5 | right arm behind body 5 cm (human's in front) |
| `carlos_1_2_2_t179-196` | A | 15_carlos_1_2_2 179.1–196.4 s | 1.5 / 1.3 | 11 / 5 | right arm behind body 5 cm (human's in front) |
| `carlos_1_2_2_t255-270` | A | 15_carlos_1_2_2 255.3–270.5 s | 0.3 / 0.3 | 11 / 4 | self-collision right_hand_collision / trunk_collision 0.2 s (at 9.5 s, 8 mm) |
| `carlos_1_2_2_t284-295_shift` | B | 15_carlos_1_2_2 283.7–295.3 s | 14.7 / 8.2 | 14 / 3 | leg at limit 19%; outlier knee max (z +4.9) |
| `carlos_1_2_2_t343-359` | A | 15_carlos_1_2_2 342.7–359.3 s | 3.3 / 1.6 | 3 / 1 | self-collision right_hand_collision / trunk_collision 4.3 s (at 6.9 s, 8 mm) |
| `carlos_1_2_2_t377-381_shift` | B | 15_carlos_1_2_2 376.6–381.3 s | 10.4 / 7.8 | 6 / 2 | outlier knee max (z +4.7) |
| `carlos_1_2_2_t404-410_shift` | B | 15_carlos_1_2_2 404.3–409.8 s | 16.2 / 10.3 | 29 / 9 | leg at limit 10%; outlier knee max (z +4.5) |
| `carlos_1_2_2_t449-463` | A | 15_carlos_1_2_2 449.1–463.3 s | 1.6 / 1.0 | 9 / 4 | self-collision right_hand_collision / trunk_collision 0.2 s (at 7.7 s, 7 mm) |
| `carlos_1_2_2_t478-492` | A | 15_carlos_1_2_2 477.5–491.7 s | 0.9 / 0.6 | 10 / 4 | self-collision right_hand_collision / trunk_collision 0.8 s (at 4.6 s, 10 mm) |
| `carlos_1_2_2_t543-559` | A | 15_carlos_1_2_2 543.0–558.6 s | 0.2 / 0.4 | 11 / 5 | outlier knee max (z -3.7); self-collision right_hand_collision / trunk_collision 0.2 s (at 10.1 s, 8 mm) |
| `carlos_1_2_2_t86-91_shift` | B | 15_carlos_1_2_2 86.1–91.4 s | 20.9 / 11.7 | 9 / 5 | outlier knee max (z +4.3) |
| `carlos_1_3_3_t0-10_shift` | B | 15_carlos_1_3_3 0.0–10.2 s | 14.3 / 8.5 | 12 / 3 | outlier knee max (z +5.1) |
| `carlos_1_3_3_t176-183_shift` | B | 15_carlos_1_3_3 175.7–183.2 s | 16.7 / 8.5 | 12 / 4 | outlier knee max (z +5.4) |
| `carlos_1_3_3_t378-393` | A | 15_carlos_1_3_3 378.1–393.2 s | 0.6 / 1.2 | 8 / 3 | shoulder at limit 9% |
| `carlos_1_3_3_t394-404_shift` | B | 15_carlos_1_3_3 393.7–403.9 s | 21.5 / 12.2 | 13 / 4 | outlier knee max (z +4.1) |
| `carlos_1_3_3_t489-495_shift` | B | 15_carlos_1_3_3 489.0–494.9 s | 23.9 / 14.5 | 7 / 2 | outlier knee max (z +4.6) |
| `carlos_1_3_3_t524-540` | A | 15_carlos_1_3_3 524.1–539.8 s | 1.3 / 0.4 | 6 / 2 | self-collision right_hand_collision / trunk_collision 0.3 s (at 14.4 s, 12 mm) |
| `carlos_1_3_3_t553-559_shift` | B | 15_carlos_1_3_3 553.4–559.4 s | 15.7 / 9.3 | 5 / 1 | outlier knee max (z +3.8) |
| `carlos_1_3_3_t602-606_shift` | B | 15_carlos_1_3_3 601.9–605.9 s | 30.7 / 16.7 | 27 / 8 | human steps; leg at limit 6% |
| `carlos_1_3_3_t606-610_shift` | B | 15_carlos_1_3_3 605.9–610.4 s | 18.8 / 9.9 | 21 / 6 | outlier knee max (z +5.5) |
| `carlos_1_3_3_t66-73_shift` | B | 15_carlos_1_3_3 65.6–73.4 s | 17.3 / 9.2 | 8 / 2 | leg at limit 8%; outlier knee max (z +3.7) |
| `daiki_0_103_103_t1-5_shift` | B | 18_daiki_0_103_103 1.2–5.2 s | 13.4 / 7.7 | 16 / 4 | outlier knee max (z +5.3) |
| `daiki_0_104_104_t52-69` | A | 18_daiki_0_104_104 52.1–69.4 s | 2.1 / 0.5 | 19 / 7 | head at limit 16% |
| `daiki_0_10_10_t17-26_shift` | B | 18_daiki_0_10_10 16.8–25.8 s | 14.1 / 8.6 | 26 / 7 | outlier knee max (z +5.6) |
| `daiki_0_10_10_t24-36` | A | 18_daiki_0_10_10 23.8–36.3 s | 2.2 / 0.4 | 26 / 7 | head at limit 10% |
| `daiki_0_10_10_t34-42_shift` | B | 18_daiki_0_10_10 34.3–41.8 s | 17.4 / 10.3 | 19 / 5 | head at limit 13%; outlier knee max (z +4.6) |
| `daiki_0_10_10_t51-63` | A | 18_daiki_0_10_10 51.3–62.8 s | 2.2 / 0.8 | 27 / 7 | head at limit 11% |
| `daiki_0_111_111_t37-56` | A | 18_daiki_0_111_111 37.4–56.1 s | 1.6 / 0.8 | 27 / 10 | head at limit 13% |
| `daiki_0_111_111_t56-75` | A | 18_daiki_0_111_111 56.1–74.8 s | 1.9 / 1.0 | 27 / 9 | head at limit 16% |
| `daiki_0_112_112_t0-4_shift` | B | 18_daiki_0_112_112 0.0–4.0 s | 18.2 / 10.6 | 30 / 8 | head at limit 42%; outlier knee max (z +4.8) |
| `daiki_0_112_112_t1-8` | A | 18_daiki_0_112_112 1.4–7.7 s | 2.0 / 0.6 | 27 / 12 | head at limit 13% |
| `daiki_0_112_112_t25-41` | A | 18_daiki_0_112_112 24.7–41.4 s | 2.5 / 0.6 | 29 / 10 | head at limit 26% |
| `daiki_0_112_112_t41-58` | A | 18_daiki_0_112_112 41.4–58.1 s | 2.9 / 1.6 | 35 / 14 | head at limit 29% |
| `daiki_0_112_112_t58-75` | A | 18_daiki_0_112_112 58.1–74.8 s | 2.0 / 1.1 | 29 / 10 | head at limit 19% |
| `daiki_0_112_112_t6-10_shift` | B | 18_daiki_0_112_112 5.7–10.1 s | 7.0 / 4.0 | 27 / 12 | head at limit 22% |
| `daiki_0_112_112_t8-25` | A | 18_daiki_0_112_112 8.1–24.7 s | 3.8 / 1.0 | 26 / 11 | head at limit 6% |
| `daiki_0_11_11_t40-51` | A | 18_daiki_0_11_11 40.2–50.9 s | 2.1 / 1.4 | 27 / 7 | head at limit 25% |
| `daiki_0_11_11_t51-62` | A | 18_daiki_0_11_11 50.9–61.7 s | 9.4 / 4.2 | 25 / 6 | head at limit 30% |
| `daiki_0_11_11_t60-65_shift` | B | 18_daiki_0_11_11 59.7–65.3 s | 11.0 / 6.0 | 33 / 8 | head at limit 43% |
| `daiki_0_11_11_t63-80` | A | 18_daiki_0_11_11 63.3–79.9 s | 2.4 / 1.1 | 27 / 7 | head at limit 20% |
| `daiki_0_12_12_t18-26_shift` | B | 18_daiki_0_12_12 18.3–26.3 s | 24.0 / 13.5 | 17 / 7 | head at limit 34%; outlier knee max (z +4.7) |
| `daiki_0_12_12_t2-20` | A | 18_daiki_0_12_12 2.3–20.3 s | 4.3 / 0.8 | 31 / 10 | head at limit 33% |
| `daiki_0_12_12_t24-39` | A | 18_daiki_0_12_12 24.3–39.4 s | 3.4 / 0.9 | 15 / 5 | head at limit 36% |
| `daiki_0_12_12_t36-40_shift` | B | 18_daiki_0_12_12 36.0–40.0 s | 24.9 / 14.7 | 19 / 7 | head at limit 32%; outlier knee max (z +5.4) |
| `daiki_0_12_12_t40-49_shift` | B | 18_daiki_0_12_12 40.0–49.4 s | 10.8 / 5.1 | 29 / 10 | head at limit 13% |
| `daiki_0_12_12_t47-67` | A | 18_daiki_0_12_12 47.4–66.9 s | 8.2 / 4.6 | 22 / 8 | head at limit 9% |
| `daiki_0_12_12_t67-86` | A | 18_daiki_0_12_12 66.9–86.5 s | 1.7 / 0.7 | 25 / 10 | head at limit 13% |
| `daiki_0_13_13_t17-31` | A | 18_daiki_0_13_13 16.9–30.7 s | 1.9 / 0.7 | 20 / 6 | head at limit 7% |
| `daiki_0_13_13_t3-17` | A | 18_daiki_0_13_13 3.2–16.9 s | 7.3 / 3.0 | 22 / 7 | head at limit 13% |
| `daiki_0_13_13_t31-44` | A | 18_daiki_0_13_13 30.7–44.5 s | 10.1 / 4.6 | 20 / 7 | human steps; head at limit 8% |
| `daiki_0_13_13_t44-61` | A | 18_daiki_0_13_13 44.5–60.9 s | 4.6 / 1.3 | 22 / 8 | head at limit 19% |
| `daiki_0_13_13_t61-77` | A | 18_daiki_0_13_13 60.9–77.4 s | 1.3 / 0.5 | 21 / 8 | head at limit 14% |
| `daiki_0_13_13_t75-80_shift` | B | 18_daiki_0_13_13 75.4–79.9 s | 12.0 / 7.7 | 21 / 8 | head at limit 10% |
| `daiki_0_13_13_t78-89` | A | 18_daiki_0_13_13 77.9–88.8 s | 9.5 / 4.3 | 23 / 9 | head at limit 8% |
| `daiki_0_14_14_t0-19` | A | 18_daiki_0_14_14 0.0–19.3 s | 3.8 / 2.3 | 22 / 7 | head at limit 23% |
| `daiki_0_14_14_t19-39` | A | 18_daiki_0_14_14 19.3–38.6 s | 3.2 / 0.9 | 29 / 10 | head at limit 33% |
| `daiki_0_14_14_t37-41_shift` | B | 18_daiki_0_14_14 36.6–41.1 s | 6.6 / 3.4 | 27 / 8 | head at limit 20% |
| `daiki_0_14_14_t39-53` | A | 18_daiki_0_14_14 39.1–52.6 s | 2.2 / 0.8 | 21 / 6 | head at limit 11% |
| `daiki_0_14_14_t53-66` | A | 18_daiki_0_14_14 52.6–66.2 s | 1.5 / 0.6 | 25 / 8 | head at limit 21% |
| `daiki_0_14_14_t66-80` | A | 18_daiki_0_14_14 66.2–79.8 s | 1.8 / 0.7 | 18 / 7 | head at limit 10% |
| `daiki_0_14_14_t78-82_shift` | B | 18_daiki_0_14_14 77.8–82.3 s | 15.8 / 9.4 | 21 / 7 | head at limit 10% |
| `daiki_0_14_14_t80-85` | A | 18_daiki_0_14_14 80.3–85.0 s | 2.6 / 0.8 | 24 / 8 | head at limit 8% |
| `daiki_0_14_14_t83-88_shift` | B | 18_daiki_0_14_14 83.0–87.6 s | 8.7 / 6.1 | 25 / 9 | head at limit 9% |
| `daiki_0_14_14_t86-94` | A | 18_daiki_0_14_14 85.6–93.8 s | 2.9 / 0.8 | 21 / 7 | head at limit 21% |
| `daiki_0_15_15_t0-6_shift` | B | 18_daiki_0_15_15 0.0–6.0 s | 11.7 / 6.7 | 25 / 8 | head at limit 45% |
| `daiki_0_15_15_t24-44` | A | 18_daiki_0_15_15 24.0–43.9 s | 3.4 / 1.8 | 23 / 6 | head at limit 28% |
| `daiki_0_15_15_t4-24` | A | 18_daiki_0_15_15 4.0–24.0 s | 2.3 / 0.9 | 13 / 4 | head at limit 46% |
| `daiki_0_15_15_t44-64` | A | 18_daiki_0_15_15 43.9–63.9 s | 2.0 / 0.8 | 35 / 11 | head at limit 21% |
| `daiki_0_15_15_t64-84` | A | 18_daiki_0_15_15 63.9–83.8 s | 4.1 / 1.8 | 25 / 7 | head at limit 66% |
| `daiki_0_15_15_t84-104` | A | 18_daiki_0_15_15 83.8–103.8 s | 1.7 / 0.7 | 31 / 9 | head at limit 18% |
| `daiki_0_16_16_t0-6` | A | 18_daiki_0_16_16 0.1–5.6 s | 3.3 / 2.3 | 27 / 8 | head at limit 22% |
| `daiki_0_16_16_t10-30` | A | 18_daiki_0_16_16 10.3–29.7 s | 3.6 / 1.1 | 22 / 6 | head at limit 12% |
| `daiki_0_16_16_t30-49` | A | 18_daiki_0_16_16 29.7–49.1 s | 7.0 / 3.6 | 24 / 7 | head at limit 24% |
| `daiki_0_16_16_t4-12_shift` | B | 18_daiki_0_16_16 3.6–12.3 s | 10.9 / 4.7 | 26 / 9 | head at limit 15% |
| `daiki_0_16_16_t49-69` | A | 18_daiki_0_16_16 49.1–68.6 s | 3.4 / 0.8 | 16 / 4 | head at limit 9% |
| `daiki_0_16_16_t69-88` | A | 18_daiki_0_16_16 68.6–88.0 s | 5.7 / 2.4 | 23 / 7 | head at limit 50% |
| `daiki_0_1_1_t14-21_shift` | B | 18_daiki_0_1_1 14.3–21.1 s | 14.5 / 8.0 | 14 / 5 | outlier knee max (z +4.3) |
| `daiki_0_1_1_t34-38_shift` | B | 18_daiki_0_1_1 34.0–38.0 s | 23.8 / 13.4 | 18 / 7 | head at limit 17% |
| `daiki_0_1_1_t38-43_shift` | B | 18_daiki_0_1_1 38.0–43.2 s | 17.5 / 10.2 | 18 / 4 | outlier knee max (z +4.4) |
| `daiki_0_2_2_t1-21` | A | 18_daiki_0_2_2 1.0–20.9 s | 5.7 / 3.5 | 16 / 4 | head at limit 6% |
| `daiki_0_2_2_t21-41` | A | 18_daiki_0_2_2 20.9–40.7 s | 1.5 / 0.6 | 16 / 4 | head at limit 6% |
| `daiki_0_2_2_t41-61` | A | 18_daiki_0_2_2 40.7–60.6 s | 1.8 / 0.7 | 13 / 4 | head at limit 6% |
| `daiki_0_2_2_t61-80` | A | 18_daiki_0_2_2 60.6–80.4 s | 1.6 / 0.7 | 14 / 4 | head at limit 11% |
| `daiki_0_2_2_t78-84_shift` | B | 18_daiki_0_2_2 78.4–83.8 s | 23.0 / 14.5 | 17 / 5 | knee 61 deg; head at limit 13%; outlier knee max (z +8.5) |
| `daiki_0_3_3_t0-14` | A | 18_daiki_0_3_3 0.0–13.7 s | 6.7 / 1.1 | 16 / 5 | head at limit 32% |
| `daiki_0_3_3_t14-27` | A | 18_daiki_0_3_3 13.7–27.4 s | 4.5 / 1.0 | 17 / 5 | head at limit 44% |
| `daiki_0_3_3_t25-34_shift` | B | 18_daiki_0_3_3 25.4–34.3 s | 16.3 / 8.3 | 23 / 7 | head at limit 16% |
| `daiki_0_3_3_t32-37` | A | 18_daiki_0_3_3 32.3–37.2 s | 1.2 / 0.6 | 22 / 7 | head at limit 9% |
| `daiki_0_3_3_t35-40_shift` | B | 18_daiki_0_3_3 35.2–39.6 s | 9.6 / 5.4 | 26 / 8 | head at limit 14% |
| `daiki_0_3_3_t50-62` | A | 18_daiki_0_3_3 49.8–61.9 s | 8.4 / 5.0 | 19 / 5 | head at limit 7% |
| `daiki_0_3_3_t62-77` | A | 18_daiki_0_3_3 62.4–76.6 s | 1.5 / 0.6 | 20 / 7 | head at limit 13% |
| `daiki_0_3_3_t77-91` | A | 18_daiki_0_3_3 76.6–90.8 s | 2.0 / 0.6 | 17 / 6 | head at limit 31% |
| `daiki_0_4_4_t0-9_shift` | B | 18_daiki_0_4_4 0.0–9.3 s | 20.0 / 11.4 | 18 / 6 | head at limit 30%; outlier knee max (z +3.8) |
| `daiki_0_4_4_t17-24_shift` | B | 18_daiki_0_4_4 17.3–23.6 s | 20.4 / 11.6 | 36 / 10 | head at limit 22% |
| `daiki_0_4_4_t22-32` | A | 18_daiki_0_4_4 21.6–31.7 s | 1.6 / 0.7 | 18 / 5 | head at limit 16% |
| `daiki_0_4_4_t35-51` | A | 18_daiki_0_4_4 35.3–51.3 s | 2.6 / 1.7 | 19 / 7 | head at limit 23% |
| `daiki_0_4_4_t51-67` | A | 18_daiki_0_4_4 51.3–67.2 s | 2.9 / 1.1 | 9 / 3 | head at limit 34% |
| `daiki_0_4_4_t67-83` | A | 18_daiki_0_4_4 67.2–83.2 s | 1.9 / 1.2 | 10 / 4 | head at limit 20% |
| `daiki_0_4_4_t7-17` | A | 18_daiki_0_4_4 7.3–16.7 s | 2.2 / 0.5 | 21 / 6 | head at limit 16% |
| `daiki_0_4_4_t83-100` | A | 18_daiki_0_4_4 83.4–99.8 s | 1.9 / 0.9 | 13 / 5 | head at limit 18% |
| `daiki_0_5_5_t0-18` | A | 18_daiki_0_5_5 0.0–18.2 s | 2.6 / 1.2 | 18 / 7 | head at limit 56% |
| `daiki_0_5_5_t36-54` | A | 18_daiki_0_5_5 36.3–54.5 s | 2.6 / 1.3 | 19 / 6 | head at limit 17% |
| `daiki_0_5_5_t54-73` | A | 18_daiki_0_5_5 54.5–72.6 s | 2.4 / 0.7 | 16 / 4 | head at limit 19% |
| `daiki_0_5_5_t73-91` | A | 18_daiki_0_5_5 72.6–90.8 s | 1.7 / 1.7 | 19 / 6 | head at limit 7% |
| `daiki_0_66_66_t59-75` | A | 18_daiki_0_66_66 58.9–75.1 s | 5.5 / 1.6 | 26 / 10 | head at limit 5% |
| `daiki_0_6_6_t0-11` | A | 18_daiki_0_6_6 0.0–11.2 s | 1.1 / 0.4 | 26 / 7 | head at limit 16% |
| `daiki_0_6_6_t11-22` | A | 18_daiki_0_6_6 11.2–22.4 s | 1.7 / 0.5 | 18 / 6 | head at limit 43% |
| `daiki_0_6_6_t19-23_shift` | B | 18_daiki_0_6_6 19.0–23.0 s | 24.4 / 14.3 | 19 / 6 | head at limit 62%; outlier knee max (z +5.2) |
| `daiki_0_6_6_t26-40` | A | 18_daiki_0_6_6 26.5–40.1 s | 1.9 / 0.9 | 20 / 5 | head at limit 35% |
| `daiki_0_6_6_t40-54` | A | 18_daiki_0_6_6 40.1–53.7 s | 1.5 / 0.5 | 7 / 2 | head at limit 64% |
| `daiki_0_6_6_t57-61_shift` | B | 18_daiki_0_6_6 56.8–60.8 s | 9.3 / 4.8 | 7 / 2 | head at limit 69% |
| `daiki_0_6_6_t59-73` | A | 18_daiki_0_6_6 58.6–73.1 s | 4.3 / 1.7 | 19 / 7 | head at limit 42% |
| `daiki_0_6_6_t73-88` | A | 18_daiki_0_6_6 73.1–87.6 s | 2.1 / 1.4 | 16 / 4 | head at limit 24% |
| `daiki_0_73_73_t29-34_shift` | B | 18_daiki_0_73_73 29.0–33.5 s | 15.7 / 9.9 | 30 / 9 | outlier knee max (z +3.6) |
| `daiki_0_73_73_t36-42_shift` | B | 18_daiki_0_73_73 35.6–42.3 s | 11.8 / 5.0 | 33 / 12 | outlier knee max (z +3.5) |
| `daiki_0_7_7_t0-20` | A | 18_daiki_0_7_7 0.0–19.7 s | 2.2 / 0.9 | 19 / 5 | head at limit 40% |
| `daiki_0_7_7_t20-39` | A | 18_daiki_0_7_7 19.7–39.4 s | 2.1 / 0.8 | 17 / 6 | head at limit 24% |
| `daiki_0_7_7_t39-59` | A | 18_daiki_0_7_7 39.4–59.1 s | 2.5 / 1.1 | 14 / 5 | head at limit 33% |
| `daiki_0_7_7_t59-79` | A | 18_daiki_0_7_7 59.1–78.8 s | 1.6 / 1.0 | 13 / 4 | head at limit 12% |
| `daiki_0_81_81_t0-5` | A | 18_daiki_0_81_81 0.0–5.4 s | 9.4 / 5.3 | 32 / 9 | head at limit 9% |
| `daiki_0_81_81_t34-53` | A | 18_daiki_0_81_81 33.6–53.2 s | 1.7 / 0.8 | 16 / 5 | head at limit 11% |
| `daiki_0_81_81_t53-73` | A | 18_daiki_0_81_81 53.2–72.7 s | 2.1 / 1.0 | 16 / 4 | head at limit 10% |
| `daiki_0_82_82_t0-16` | A | 18_daiki_0_82_82 0.3–16.4 s | 1.8 / 1.4 | 23 / 7 | head at limit 9% |
| `daiki_0_82_82_t16-32` | A | 18_daiki_0_82_82 16.4–32.4 s | 1.7 / 0.6 | 21 / 8 | head at limit 21% |
| `daiki_0_82_82_t32-48` | A | 18_daiki_0_82_82 32.4–48.4 s | 4.4 / 1.1 | 17 / 5 | head at limit 8% |
| `daiki_0_82_82_t48-64` | A | 18_daiki_0_82_82 48.4–64.5 s | 2.0 / 0.8 | 22 / 6 | head at limit 12% |
| `daiki_0_87_87_t60-76` | A | 18_daiki_0_87_87 59.5–75.6 s | 1.7 / 1.9 | 22 / 6 | head at limit 36% |
| `daiki_0_87_87_t76-92` | A | 18_daiki_0_87_87 75.6–91.8 s | 2.3 / 0.8 | 29 / 7 | head at limit 54% |
| `daiki_0_88_88_t0-18` | A | 18_daiki_0_88_88 0.0–18.3 s | 3.9 / 4.3 | 18 / 6 | head at limit 36% |
| `daiki_0_88_88_t18-37` | A | 18_daiki_0_88_88 18.3–36.6 s | 1.9 / 1.3 | 19 / 7 | head at limit 31% |
| `daiki_0_8_8_t0-15` | A | 18_daiki_0_8_8 0.0–14.7 s | 1.6 / 0.6 | 11 / 3 | head at limit 27% |
| `daiki_0_8_8_t15-29` | A | 18_daiki_0_8_8 14.7–29.5 s | 1.7 / 0.6 | 10 / 3 | head at limit 57% |
| `daiki_0_8_8_t49-68` | A | 18_daiki_0_8_8 48.9–68.1 s | 1.8 / 0.8 | 9 / 3 | head at limit 34% |
| `daiki_0_8_8_t68-87` | A | 18_daiki_0_8_8 68.1–87.3 s | 1.9 / 0.8 | 12 / 4 | head at limit 63% |
| `daiki_0_95_95_t33-39_shift` | B | 18_daiki_0_95_95 32.7–38.9 s | 23.4 / 12.7 | 19 / 8 | outlier knee max (z +3.8) |
| `daiki_0_96_96_t0-16` | A | 18_daiki_0_96_96 0.0–15.7 s | 1.0 / 0.6 | 22 / 6 | head at limit 6% |
| `daiki_0_9_9_t17-25_shift` | B | 18_daiki_0_9_9 16.7–24.7 s | 15.2 / 8.8 | 24 / 8 | outlier knee max (z +5.2) |
| `daiki_0_9_9_t23-35` | A | 18_daiki_0_9_9 22.7–34.7 s | 1.5 / 0.6 | 22 / 7 | head at limit 6% |
| `daiki_0_9_9_t47-58` | A | 18_daiki_0_9_9 47.0–58.4 s | 3.1 / 1.5 | 21 / 6 | head at limit 9% |
| `daiki_0_9_9_t58-70` | A | 18_daiki_0_9_9 58.4–69.8 s | 1.4 / 0.4 | 22 / 7 | head at limit 6% |
| `goto_0_104_104_t15-31` | A | 25_goto_0_104_104 15.3–30.5 s | 0.7 / 0.2 | 10 / 4 | leg at limit 6% |
| `goto_0_104_104_t31-46` | A | 25_goto_0_104_104 30.5–45.8 s | 9.9 / 5.3 | 6 / 2 | outlier knee max (z +5.0) |
| `goto_0_104_104_t85-104` | A | 25_goto_0_104_104 84.8–104.3 s | 0.4 / 0.2 | 8 / 3 | elbow bend at limit 7% |
| `goto_0_11_11_t19-38` | A | 25_goto_0_11_11 19.2–38.4 s | 0.4 / 0.2 | 6 / 2 | outlier knee max (z -3.5) |
| `goto_0_2_2_t0-20` | A | 25_goto_0_2_2 0.0–19.6 s | 0.6 / 0.2 | 15 / 4 | outlier knee max (z -3.6) |
| `goto_0_6_6_t0-20` | A | 25_goto_0_6_6 0.0–19.9 s | 0.5 / 0.3 | 11 / 3 | outlier knee max (z -3.8) |
| `goto_0_7_7_t53-71` | A | 25_goto_0_7_7 53.4–71.1 s | 0.5 / 0.2 | 7 / 2 | outlier knee max (z -3.9) |
| `goto_0_7_7_t71-89` | A | 25_goto_0_7_7 71.1–88.9 s | 0.5 / 0.2 | 11 / 4 | outlier knee max (z -4.1) |
| `goto_0_8_8_t19-39` | A | 25_goto_0_8_8 19.4–38.8 s | 0.4 / 0.1 | 11 / 3 | outlier knee max (z -4.3) |
| `goto_0_96_96_t33-49` | A | 25_goto_0_96_96 32.8–49.2 s | 0.6 / 0.3 | 16 / 8 | elbow bend at limit 9% |
| `goto_0_9_9_t0-17` | A | 25_goto_0_9_9 0.0–17.2 s | 0.4 / 0.2 | 13 / 4 | outlier knee max (z -4.0) |
| `goto_0_9_9_t69-86` | A | 25_goto_0_9_9 68.7–85.9 s | 0.4 / 0.2 | 9 / 2 | outlier knee max (z -3.9) |
| `goto_1_1_1_t440-460` | A | 25_goto_1_1_1 440.4–460.0 s | 0.6 / 0.4 | 10 / 5 | elbow bend at limit 16% |
| `goto_1_1_1_t45-50_shift` | B | 25_goto_1_1_1 45.1–49.5 s | 6.0 / 3.9 | 9 / 4 | outlier knee max (z +5.1) |
| `goto_1_2_2_t137-157` | A | 25_goto_1_2_2 137.1–156.6 s | 0.6 / 0.4 | 9 / 4 | elbow bend at limit 30% |
| `goto_1_2_2_t157-176` | A | 25_goto_1_2_2 156.6–176.2 s | 0.8 / 0.2 | 10 / 6 | elbow bend at limit 7% |
| `goto_1_2_2_t392-411` | A | 25_goto_1_2_2 391.6–411.2 s | 0.4 / 0.3 | 8 / 4 | elbow bend at limit 8%; self-collision right_hand_end_collision / trunk_collision 1.1 s (at 8.5 s, 8 mm) |
| `goto_1_2_2_t78-98` | A | 25_goto_1_2_2 78.3–97.9 s | 0.6 / 0.5 | 9 / 4 | elbow bend at limit 20% |
| `goto_1_3_3_t117-137` | A | 25_goto_1_3_3 117.3–136.9 s | 0.9 / 0.4 | 9 / 5 | elbow bend at limit 10% |
| `goto_1_3_3_t332-352` | A | 25_goto_1_3_3 332.4–351.9 s | 1.0 / 0.3 | 8 / 3 | elbow bend at limit 12% |
| `hailing_0_15_15_t38-56` | A | 23_hailing_0_15_15 38.2–56.0 s | 10.3 / 6.0 | 34 / 12 | human steps |
| `hailing_0_15_15_t59-67_shift` | B | 23_hailing_0_15_15 59.3–66.9 s | 16.2 / 8.7 | 34 / 9 | outlier knee max (z +3.7) |
| `hailing_0_16_16_t35-44_shift` | B | 23_hailing_0_16_16 35.4–44.2 s | 16.0 / 7.9 | 48 / 13 | outlier knee max (z +4.6) |
| `hailing_0_1_1_t55-63_shift` | B | 23_hailing_0_1_1 54.7–62.8 s | 28.4 / 14.1 | 30 / 8 | human steps; outlier knee max (z +4.9) |
| `hailing_0_3_3_t74-78_shift` | B | 23_hailing_0_3_3 73.9–78.5 s | 14.5 / 7.9 | 45 / 18 | outlier knee max (z +3.8) |
| `hailing_0_5_5_t73-80_shift` | B | 23_hailing_0_5_5 73.2–80.2 s | 20.7 / 11.2 | 29 / 8 | outlier knee max (z +4.5) |
| `hailing_0_65_65_t21-40` | A | 23_hailing_0_65_65 21.3–40.0 s | 7.2 / 4.1 | 31 / 12 | outlier knee max (z +4.8) |
| `hailing_0_6_6_t34-51` | A | 23_hailing_0_6_6 33.9–50.8 s | 10.9 / 6.3 | 39 / 13 | human steps |
| `hailing_0_7_7_t20-40` | A | 23_hailing_0_7_7 19.9–39.8 s | 13.3 / 7.3 | 28 / 9 | human steps |
| `hailing_0_7_7_t60-80` | A | 23_hailing_0_7_7 59.7–79.6 s | 12.0 / 6.6 | 35 / 11 | human steps |
| `hailing_0_81_81_t17-33` | A | 23_hailing_0_81_81 16.7–33.4 s | 3.6 / 1.0 | 22 / 8 | self-collision right_hand_collision / trunk_collision 0.8 s (at 7.5 s, 16 mm) |
| `hailing_0_81_81_t33-50` | A | 23_hailing_0_81_81 33.4–50.1 s | 7.5 / 5.1 | 19 / 7 | self-collision right_hand_collision / trunk_collision 0.5 s (at 13.5 s, 13 mm) |
| `hailing_0_81_81_t50-67` | A | 23_hailing_0_81_81 50.1–66.8 s | 4.4 / 2.6 | 15 / 5 | self-collision right_hand_collision / trunk_collision 0.7 s (at 5.7 s, 14 mm) |
| `hailing_0_82_82_t0-18` | A | 23_hailing_0_82_82 0.0–17.7 s | 4.1 / 2.6 | 24 / 7 | self-collision right_hand_collision / trunk_collision 0.4 s (at 11.1 s, 10 mm) |
| `hailing_0_82_82_t35-53` | A | 23_hailing_0_82_82 35.4–53.1 s | 5.0 / 2.4 | 24 / 8 | hand presses into leg 16 mm for 0.7 s (at 10.8 s) |
| `hailing_0_82_82_t53-71` | A | 23_hailing_0_82_82 53.1–70.8 s | 3.5 / 0.8 | 21 / 6 | self-collision right_hand_collision / trunk_collision 0.2 s (at 10.3 s, 8 mm) |
| `hailing_0_88_88_t35-52` | A | 23_hailing_0_88_88 34.7–52.1 s | 3.6 / 1.0 | 29 / 9 | self-collision right_hand_collision / trunk_collision 0.3 s (at 10.3 s, 12 mm) |
| `hailing_0_88_88_t69-87` | A | 23_hailing_0_88_88 69.4–86.8 s | 4.3 / 1.7 | 23 / 8 | self-collision right_hand_collision / trunk_collision 0.2 s (at 4.3 s, 16 mm) |
| `hailing_0_8_8_t0-5_shift` | B | 23_hailing_0_8_8 0.1–4.7 s | 15.7 / 10.3 | 21 / 10 | outlier knee max (z +6.7) |
| `hailing_0_96_96_t18-23_shift` | B | 23_hailing_0_96_96 18.2–22.6 s | 7.6 / 5.3 | 21 / 6 | self-collision right_hand_collision / trunk_collision 1.0 s (at 0.6 s, 23 mm) |
| `hailing_0_96_96_t9-20` | A | 23_hailing_0_96_96 8.6–20.2 s | 1.7 / 0.8 | 22 / 6 | self-collision right_hand_collision / trunk_collision 1.0 s (at 10.2 s, 23 mm) |
| `hailing_1_1_1_t207-225` | A | 23_hailing_1_1_1 207.0–225.4 s | 8.1 / 2.4 | 46 / 13 | shoulder at limit 10% |
| `hailing_1_1_1_t24-30_shift` | B | 23_hailing_1_1_1 23.9–29.9 s | 11.4 / 4.9 | 43 / 11 | outlier knee max (z +4.8) |
| `hailing_1_1_1_t28-45` | A | 23_hailing_1_1_1 27.9–44.7 s | 7.8 / 3.8 | 51 / 12 | outlier knee max (z +4.8) |
| `hailing_1_1_1_t302-321` | A | 23_hailing_1_1_1 301.9–320.7 s | 6.1 / 2.5 | 52 / 15 | shoulder at limit 9% |
| `hailing_1_1_1_t321-339` | A | 23_hailing_1_1_1 320.7–339.4 s | 5.1 / 0.7 | 48 / 14 | shoulder at limit 6% |
| `hailing_1_1_1_t464-482` | A | 23_hailing_1_1_1 464.2–481.7 s | 8.6 / 2.3 | 58 / 15 | outlier knee max (z +3.9) |
| `itoi_0_103_103_t39-57` | A | 17_itoi_0_103_103 38.8–56.6 s | 10.0 / 5.2 | 46 / 13 | outlier knee max (z +5.2) |
| `itoi_0_103_103_t54-58_shift` | B | 17_itoi_0_103_103 54.1–58.1 s | 13.1 / 6.0 | 97 / 29 | outlier arms k1 cm (z +6.2); outlier knee max (z +5.0) |
| `itoi_0_103_103_t66-70_shift` | B | 17_itoi_0_103_103 65.7–70.0 s | 10.2 / 5.2 | 55 / 22 | outlier arms k1 cm (z +4.1) |
| `itoi_0_104_104_t17-22_shift` | B | 17_itoi_0_104_104 17.4–22.2 s | 9.9 / 6.2 | 27 / 8 | outlier knee max (z +6.1) |
| `itoi_0_104_104_t20-34` | A | 17_itoi_0_104_104 20.2–33.6 s | 9.8 / 6.2 | 20 / 6 | outlier knee max (z +6.6) |
| `itoi_0_104_104_t32-36_shift` | B | 17_itoi_0_104_104 31.6–35.9 s | 7.3 / 2.2 | 29 / 10 | outlier knee max (z +4.9) |
| `itoi_0_104_104_t44-55_shift` | B | 17_itoi_0_104_104 43.9–55.4 s | 13.5 / 6.9 | 25 / 8 | outlier knee max (z +4.7) |
| `itoi_0_10_10_t63-67_shift` | B | 17_itoi_0_10_10 62.8–66.8 s | 17.5 / 10.2 | 46 / 15 | outlier knee max (z +4.2) |
| `itoi_0_111_111_t10-15_shift` | B | 17_itoi_0_111_111 10.1–14.7 s | 9.6 / 6.5 | 14 / 5 | outlier knee max (z +5.4) |
| `itoi_0_111_111_t15-22_shift` | B | 17_itoi_0_111_111 14.7–21.5 s | 17.8 / 10.3 | 11 / 4 | outlier knee max (z +4.1) |
| `itoi_0_111_111_t24-28_shift` | B | 17_itoi_0_111_111 23.9–28.3 s | 7.1 / 4.2 | 9 / 4 | outlier knee max (z +3.6) |
| `itoi_0_111_111_t26-40` | A | 17_itoi_0_111_111 26.3–40.2 s | 8.6 / 4.5 | 11 / 4 | outlier knee max (z +4.7) |
| `itoi_0_111_111_t38-42_shift` | B | 17_itoi_0_111_111 38.2–42.4 s | 12.0 / 4.4 | 14 / 4 | outlier knee max (z +4.9) |
| `itoi_0_111_111_t40-45` | A | 17_itoi_0_111_111 40.4–44.9 s | 6.8 / 1.5 | 18 / 6 | outlier knee max (z +4.3) |
| `itoi_0_111_111_t51-63` | A | 17_itoi_0_111_111 51.2–63.4 s | 10.0 / 3.3 | 20 / 8 | outlier knee max (z +6.5) |
| `itoi_0_112_112_t0-13_shift` | B | 17_itoi_0_112_112 0.0–13.1 s | 17.3 / 9.8 | 25 / 8 | outlier knee max (z +5.6) |
| `itoi_0_12_12_t20-29_shift` | B | 17_itoi_0_12_12 20.2–29.4 s | 18.9 / 10.3 | 43 / 10 | outlier knee max (z +4.2) |
| `itoi_0_12_12_t76-81_shift` | B | 17_itoi_0_12_12 76.2–81.4 s | 22.9 / 15.1 | 57 / 16 | outlier knee max (z +7.8) |
| `itoi_0_14_14_t0-14_shift` | B | 17_itoi_0_14_14 0.0–13.8 s | 19.0 / 10.4 | 24 / 6 | outlier knee max (z +6.2) |
| `itoi_0_14_14_t14-21_shift` | B | 17_itoi_0_14_14 13.9–21.2 s | 15.9 / 10.9 | 30 / 9 | outlier knee max (z +4.2) |
| `itoi_0_14_14_t39-58` | A | 17_itoi_0_14_14 38.7–58.3 s | 10.8 / 5.9 | 31 / 11 | human steps |
| `itoi_0_14_14_t60-76` | A | 17_itoi_0_14_14 60.4–75.6 s | 7.0 / 3.5 | 31 / 11 | outlier knee max (z +6.3) |
| `itoi_0_14_14_t76-91` | A | 17_itoi_0_14_14 75.6–90.8 s | 10.2 / 3.2 | 30 / 10 | human steps |
| `itoi_0_1_1_t17-21_shift` | B | 17_itoi_0_1_1 16.8–21.1 s | 17.8 / 7.3 | 77 / 22 | outlier arms k1 cm (z +4.0); outlier knee max (z +7.1) |
| `itoi_0_1_1_t46-54_shift` | B | 17_itoi_0_1_1 46.1–54.4 s | 18.0 / 10.4 | 44 / 14 | outlier knee max (z +6.5) |
| `itoi_0_1_1_t69-74_shift` | B | 17_itoi_0_1_1 68.8–74.5 s | 12.6 / 3.6 | 56 / 18 | outlier knee max (z +7.7) |
| `itoi_0_2_2_t19-23_shift` | B | 17_itoi_0_2_2 18.5–23.1 s | 15.6 / 11.9 | 44 / 13 | outlier knee max (z +4.2) |
| `itoi_0_2_2_t30-39_shift` | B | 17_itoi_0_2_2 29.8–38.7 s | 21.9 / 13.2 | 27 / 9 | outlier knee max (z +7.8) |
| `itoi_0_2_2_t39-45_shift` | B | 17_itoi_0_2_2 39.4–44.9 s | 17.0 / 7.5 | 37 / 9 | outlier knee max (z +7.0) |
| `itoi_0_2_2_t67-80_shift` | B | 17_itoi_0_2_2 67.0–80.3 s | 19.8 / 10.4 | 16 / 6 | outlier knee max (z +7.6) |
| `itoi_0_2_2_t85-89_shift` | B | 17_itoi_0_2_2 84.6–88.8 s | 14.4 / 10.9 | 36 / 10 | outlier knee max (z +6.8) |
| `itoi_0_3_3_t14-20_shift` | B | 17_itoi_0_3_3 14.2–20.0 s | 19.9 / 10.8 | 36 / 11 | outlier knee max (z +5.4) |
| `itoi_0_3_3_t21-27_shift` | B | 17_itoi_0_3_3 20.9–26.5 s | 24.8 / 11.8 | 14 / 5 | knee 64 deg; outlier knee max (z +9.5) |
| `itoi_0_3_3_t28-42_shift` | B | 17_itoi_0_3_3 28.4–41.8 s | 22.8 / 12.5 | 20 / 7 | outlier knee max (z +6.7) |
| `itoi_0_3_3_t44-48_shift` | B | 17_itoi_0_3_3 43.7–48.1 s | 9.7 / 4.8 | 28 / 7 | outlier knee max (z +3.7) |
| `itoi_0_3_3_t46-51` | A | 17_itoi_0_3_3 46.1–51.4 s | 9.1 / 4.6 | 21 / 7 | outlier knee max (z +5.2) |
| `itoi_0_3_3_t5-9` | A | 17_itoi_0_3_3 4.7–9.4 s | 9.6 / 3.9 | 22 / 6 | outlier knee max (z +4.5) |
| `itoi_0_3_3_t62-72` | A | 17_itoi_0_3_3 62.2–72.4 s | 9.3 / 4.1 | 27 / 8 | outlier knee max (z +6.0) |
| `itoi_0_3_3_t70-77_shift` | B | 17_itoi_0_3_3 70.4–77.1 s | 21.9 / 14.2 | 11 / 4 | outlier knee max (z +6.6) |
| `itoi_0_3_3_t77-85_shift` | B | 17_itoi_0_3_3 77.4–84.8 s | 16.2 / 8.5 | 37 / 12 | outlier knee max (z +5.5) |
| `itoi_0_4_4_t14-20_shift` | B | 17_itoi_0_4_4 13.6–19.6 s | 24.2 / 14.2 | 12 / 4 | outlier knee max (z +6.4) |
| `itoi_0_4_4_t22-27` | A | 17_itoi_0_4_4 21.7–27.2 s | 7.4 / 1.5 | 23 / 7 | outlier knee max (z +4.2) |
| `itoi_0_4_4_t25-33_shift` | B | 17_itoi_0_4_4 25.2–33.1 s | 15.8 / 9.6 | 18 / 5 | outlier knee max (z +4.4) |
| `itoi_0_4_4_t35-40_shift` | B | 17_itoi_0_4_4 35.5–39.7 s | 21.7 / 12.9 | 50 / 15 | outlier knee max (z +3.9) |
| `itoi_0_4_4_t40-50_shift` | B | 17_itoi_0_4_4 39.9–50.1 s | 20.6 / 12.1 | 34 / 10 | knee 63 deg; outlier knee max (z +9.0) |
| `itoi_0_4_4_t65-75_shift` | B | 17_itoi_0_4_4 65.5–75.3 s | 14.3 / 8.5 | 20 / 5 | outlier knee max (z +5.9) |
| `itoi_0_4_4_t7-13_shift` | B | 17_itoi_0_4_4 7.5–12.9 s | 12.7 / 4.3 | 37 / 8 | outlier knee max (z +6.7) |
| `itoi_0_5_5_t3-16_shift` | B | 17_itoi_0_5_5 2.9–16.4 s | 16.9 / 8.6 | 35 / 10 | outlier knee max (z +6.8) |
| `itoi_0_5_5_t33-37` | A | 17_itoi_0_5_5 32.7–36.9 s | 10.0 / 2.3 | 28 / 7 | outlier knee max (z +7.8) |
| `itoi_0_5_5_t35-49_shift` | B | 17_itoi_0_5_5 34.9–49.2 s | 22.8 / 14.4 | 35 / 10 | outlier knee max (z +7.8) |
| `itoi_0_5_5_t61-65_shift` | B | 17_itoi_0_5_5 60.8–64.8 s | 13.4 / 3.3 | 18 / 5 | outlier knee max (z +7.1) |
| `itoi_0_65_65_t15-20_shift` | B | 17_itoi_0_65_65 15.2–19.9 s | 13.4 / 7.3 | 117 / 30 | outlier arms k1 cm (z +6.2) |
| `itoi_0_65_65_t46-53_shift` | B | 17_itoi_0_65_65 45.8–52.8 s | 14.3 / 7.2 | 63 / 18 | outlier knee max (z +3.7) |
| `itoi_0_65_65_t63-67_shift` | B | 17_itoi_0_65_65 62.8–67.2 s | 9.4 / 7.0 | 28 / 9 | outlier knee max (z +5.8) |
| `itoi_0_65_65_t71-80_shift` | B | 17_itoi_0_65_65 71.1–79.7 s | 20.4 / 11.6 | 33 / 10 | outlier knee max (z +7.6) |
| `itoi_0_66_66_t10-16_shift` | B | 17_itoi_0_66_66 9.5–15.6 s | 14.3 / 8.0 | 46 / 13 | outlier knee max (z +6.5) |
| `itoi_0_66_66_t28-40_shift` | B | 17_itoi_0_66_66 27.7–39.7 s | 24.1 / 14.4 | 70 / 18 | outlier knee max (z +6.8) |
| `itoi_0_6_6_t22-36_shift` | B | 17_itoi_0_6_6 21.7–35.6 s | 18.8 / 10.0 | 31 / 9 | outlier knee max (z +7.3) |
| `itoi_0_6_6_t3-15_shift` | B | 17_itoi_0_6_6 3.4–15.3 s | 23.7 / 14.0 | 22 / 8 | outlier knee max (z +5.8) |
| `itoi_0_6_6_t36-44_shift` | B | 17_itoi_0_6_6 36.4–43.9 s | 20.8 / 9.3 | 20 / 6 | knee 62 deg; outlier knee max (z +8.6) |
| `itoi_0_6_6_t45-51_shift` | B | 17_itoi_0_6_6 44.6–51.0 s | 24.2 / 13.7 | 29 / 9 | outlier knee max (z +5.2) |
| `itoi_0_6_6_t49-59` | A | 17_itoi_0_6_6 49.0–59.1 s | 10.0 / 3.6 | 27 / 8 | outlier knee max (z +3.9) |
| `itoi_0_6_6_t59-79` | A | 17_itoi_0_6_6 59.1–78.9 s | 9.0 / 3.9 | 27 / 8 | outlier knee max (z +5.6) |
| `itoi_0_6_6_t83-89_shift` | B | 17_itoi_0_6_6 82.6–89.5 s | 10.1 / 4.9 | 39 / 11 | outlier knee max (z +8.0) |
| `itoi_0_73_73_t0-7_shift` | B | 17_itoi_0_73_73 0.0–7.2 s | 13.7 / 7.7 | 17 / 5 | outlier knee max (z +5.7) |
| `itoi_0_73_73_t10-18_shift` | B | 17_itoi_0_73_73 10.2–17.7 s | 17.8 / 11.4 | 15 / 5 | outlier knee max (z +5.7) |
| `itoi_0_73_73_t16-24` | A | 17_itoi_0_73_73 15.7–24.2 s | 8.8 / 5.1 | 16 / 5 | outlier knee max (z +3.5) |
| `itoi_0_73_73_t22-27_shift` | B | 17_itoi_0_73_73 22.2–27.2 s | 19.7 / 11.7 | 28 / 9 | outlier knee max (z +5.3) |
| `itoi_0_73_73_t29-43` | A | 17_itoi_0_73_73 29.3–43.4 s | 8.2 / 3.9 | 25 / 7 | outlier knee max (z +6.7) |
| `itoi_0_73_73_t43-58` | A | 17_itoi_0_73_73 43.4–57.5 s | 10.5 / 4.7 | 13 / 4 | human steps |
| `itoi_0_73_73_t5-12` | A | 17_itoi_0_73_73 5.2–12.2 s | 7.1 / 3.9 | 15 / 5 | outlier knee max (z +3.6) |
| `itoi_0_74_74_t52-62` | A | 17_itoi_0_74_74 52.1–62.3 s | 9.0 / 2.3 | 28 / 9 | outlier knee max (z +5.7) |
| `itoi_0_74_74_t70-75_shift` | B | 17_itoi_0_74_74 70.4–74.8 s | 17.9 / 9.1 | 9 / 4 | outlier knee max (z +5.0) |
| `itoi_0_7_7_t10-17_shift` | B | 17_itoi_0_7_7 9.7–16.8 s | 24.2 / 14.7 | 38 / 11 | outlier knee max (z +7.2) |
| `itoi_0_7_7_t18-27_shift` | B | 17_itoi_0_7_7 18.3–26.8 s | 17.5 / 11.7 | 33 / 11 | outlier knee max (z +6.2) |
| `itoi_0_7_7_t27-34_shift` | B | 17_itoi_0_7_7 27.4–34.3 s | 21.6 / 12.2 | 30 / 10 | outlier knee max (z +5.4) |
| `itoi_0_7_7_t32-37` | A | 17_itoi_0_7_7 32.3–37.5 s | 9.2 / 2.7 | 25 / 5 | outlier knee max (z +4.8) |
| `itoi_0_7_7_t35-41_shift` | B | 17_itoi_0_7_7 35.5–41.2 s | 25.6 / 14.6 | 35 / 9 | human steps; outlier knee max (z +7.7) |
| `itoi_0_7_7_t4-12` | A | 17_itoi_0_7_7 4.1–11.7 s | 8.7 / 2.9 | 18 / 7 | outlier knee max (z +5.2) |
| `itoi_0_7_7_t46-61_shift` | B | 17_itoi_0_7_7 46.2–61.0 s | 22.4 / 11.8 | 32 / 10 | outlier knee max (z +7.1) |
| `itoi_0_81_81_t52-70` | A | 17_itoi_0_81_81 52.3–69.8 s | 11.0 / 4.8 | 9 / 4 | human steps |
| `itoi_0_82_82_t35-40_shift` | B | 17_itoi_0_82_82 35.4–39.9 s | 10.1 / 5.6 | 28 / 9 | outlier knee max (z +3.7) |
| `itoi_0_87_87_t17-33` | A | 17_itoi_0_87_87 17.2–33.4 s | 10.0 / 5.6 | 21 / 7 | outlier knee max (z +5.1) |
| `itoi_0_87_87_t33-39` | A | 17_itoi_0_87_87 33.4–39.2 s | 9.8 / 2.1 | 15 / 4 | outlier knee max (z +5.1) |
| `itoi_0_87_87_t37-44_shift` | B | 17_itoi_0_87_87 37.2–43.7 s | 10.3 / 2.8 | 14 / 5 | outlier knee max (z +5.1) |
| `itoi_0_87_87_t82-87_shift` | B | 17_itoi_0_87_87 81.8–86.8 s | 14.4 / 9.6 | 9 / 3 | outlier knee max (z +5.8) |
| `itoi_0_87_87_t9-13_shift` | B | 17_itoi_0_87_87 9.2–13.2 s | 25.3 / 13.8 | 37 / 11 | human steps; outlier knee max (z +6.2) |
| `itoi_0_88_88_t23-30_shift` | B | 17_itoi_0_88_88 23.4–30.0 s | 11.7 / 7.2 | 20 / 5 | knee 61 deg; outlier knee max (z +8.2) |
| `itoi_0_88_88_t46-51_shift` | B | 17_itoi_0_88_88 46.5–51.1 s | 14.2 / 7.3 | 18 / 5 | outlier knee max (z +3.8) |
| `itoi_0_88_88_t49-58` | A | 17_itoi_0_88_88 49.1–57.5 s | 8.6 / 2.6 | 16 / 5 | outlier knee max (z +3.8) |
| `itoi_0_88_88_t56-60_shift` | B | 17_itoi_0_88_88 55.5–60.1 s | 14.2 / 8.0 | 22 / 7 | outlier knee max (z +6.2) |
| `itoi_0_88_88_t62-71_shift` | B | 17_itoi_0_88_88 62.1–70.6 s | 13.0 / 7.4 | 13 / 4 | outlier knee max (z +4.0) |
| `itoi_0_8_8_t12-16_shift` | B | 17_itoi_0_8_8 12.0–16.0 s | 24.4 / 12.1 | 32 / 9 | outlier knee max (z +6.0) |
| `itoi_0_8_8_t19-29_shift` | B | 17_itoi_0_8_8 19.0–29.3 s | 20.5 / 12.9 | 46 / 13 | outlier knee max (z +7.5) |
| `itoi_0_8_8_t41-51_shift` | B | 17_itoi_0_8_8 40.8–51.5 s | 14.4 / 8.4 | 63 / 15 | outlier knee max (z +7.7) |
| `itoi_0_8_8_t52-67_shift` | B | 17_itoi_0_8_8 52.0–66.7 s | 28.3 / 16.9 | 28 / 9 | human steps; outlier knee max (z +5.9) |
| `itoi_0_8_8_t78-88_shift` | B | 17_itoi_0_8_8 77.7–88.0 s | 15.6 / 7.2 | 56 / 17 | outlier knee max (z +5.6) |
| `itoi_0_95_95_t12-19` | A | 17_itoi_0_95_95 12.4–18.9 s | 9.9 / 5.5 | 6 / 2 | outlier knee max (z +5.2) |
| `itoi_0_95_95_t17-22_shift` | B | 17_itoi_0_95_95 16.9–21.9 s | 13.7 / 6.4 | 8 / 3 | outlier knee max (z +5.2) |
| `itoi_0_95_95_t27-35_shift` | B | 17_itoi_0_95_95 27.3–34.6 s | 23.3 / 14.3 | 47 / 12 | outlier knee max (z +3.9) |
| `itoi_0_95_95_t36-43_shift` | B | 17_itoi_0_95_95 36.3–42.9 s | 17.5 / 9.2 | 49 / 14 | outlier knee max (z +4.9) |
| `itoi_0_95_95_t4-8_shift` | B | 17_itoi_0_95_95 4.4–8.4 s | 18.0 / 10.5 | 13 / 4 | outlier knee max (z +7.0) |
| `itoi_0_95_95_t44-48_shift` | B | 17_itoi_0_95_95 43.8–48.3 s | 10.4 / 5.2 | 25 / 9 | outlier knee max (z +4.9) |
| `itoi_0_95_95_t6-12` | A | 17_itoi_0_95_95 6.0–12.2 s | 9.3 / 3.5 | 12 / 3 | outlier knee max (z +7.0) |
| `itoi_0_96_96_t33-50` | A | 17_itoi_0_96_96 33.3–49.9 s | 8.1 / 2.8 | 36 / 11 | outlier knee max (z +5.8) |
| `itoi_0_96_96_t48-54_shift` | B | 17_itoi_0_96_96 47.9–53.8 s | 8.5 / 2.0 | 73 / 20 | outlier arms k1 cm (z +3.7); outlier knee max (z +6.5) |
| `itoi_0_9_9_t24-43` | A | 17_itoi_0_9_9 24.5–42.6 s | 9.4 / 4.3 | 34 / 10 | outlier knee max (z +5.6) |
| `itoi_1_1_1_t0-6_shift` | B | 17_itoi_1_1_1 0.2–6.2 s | 21.5 / 12.3 | 25 / 6 | outlier knee max (z +6.6) |
| `itoi_1_1_1_t12-23_shift` | B | 17_itoi_1_1_1 12.4–23.4 s | 22.5 / 12.4 | 22 / 6 | outlier knee max (z +6.8) |
| `itoi_1_1_1_t134-139_shift` | B | 17_itoi_1_1_1 134.3–139.0 s | 11.8 / 9.4 | 22 / 7 | outlier knee max (z +3.5) |
| `itoi_1_1_1_t142-146_shift` | B | 17_itoi_1_1_1 142.1–146.1 s | 24.5 / 14.3 | 16 / 7 | outlier knee max (z +4.9) |
| `itoi_1_1_1_t149-153_shift` | B | 17_itoi_1_1_1 148.8–152.9 s | 12.9 / 8.0 | 25 / 10 | outlier knee max (z +4.9) |
| `itoi_1_1_1_t151-158` | A | 17_itoi_1_1_1 150.9–157.5 s | 7.1 / 3.4 | 16 / 6 | outlier knee max (z +6.4) |
| `itoi_1_1_1_t156-163_shift` | B | 17_itoi_1_1_1 155.5–163.4 s | 10.7 / 5.4 | 12 / 5 | outlier knee max (z +5.7) |
| `itoi_1_1_1_t179-189` | A | 17_itoi_1_1_1 178.7–189.0 s | 8.4 / 3.6 | 35 / 11 | outlier knee max (z +4.5) |
| `itoi_1_1_1_t187-197_shift` | B | 17_itoi_1_1_1 187.0–197.3 s | 21.0 / 12.2 | 34 / 10 | outlier knee max (z +5.9) |
| `itoi_1_1_1_t215-219_shift` | B | 17_itoi_1_1_1 215.0–219.0 s | 25.0 / 12.3 | 5 / 3 | outlier knee max (z +5.2) |
| `itoi_1_1_1_t219-227_shift` | B | 17_itoi_1_1_1 219.2–227.4 s | 13.5 / 5.9 | 11 / 4 | outlier knee max (z +5.3) |
| `itoi_1_1_1_t225-230` | A | 17_itoi_1_1_1 225.4–229.7 s | 9.9 / 3.4 | 15 / 6 | outlier knee max (z +5.4) |
| `itoi_1_1_1_t242-251_shift` | B | 17_itoi_1_1_1 242.5–250.8 s | 16.7 / 9.6 | 24 / 9 | outlier knee max (z +6.6) |
| `itoi_1_1_1_t294-302_shift` | B | 17_itoi_1_1_1 294.3–302.4 s | 14.8 / 8.7 | 29 / 10 | outlier knee max (z +3.8) |
| `itoi_1_1_1_t322-328_shift` | B | 17_itoi_1_1_1 322.4–328.4 s | 24.3 / 13.4 | 7 / 2 | outlier knee max (z +4.2) |
| `itoi_1_1_1_t331-344_shift` | B | 17_itoi_1_1_1 330.9–344.2 s | 22.4 / 14.8 | 7 / 2 | knee 75 deg; outlier knee max (z +13.0) |
| `itoi_1_1_1_t34-39_shift` | B | 17_itoi_1_1_1 33.9–38.5 s | 12.4 / 7.0 | 20 / 9 | outlier knee max (z +4.1) |
| `itoi_1_1_1_t344-357_shift` | B | 17_itoi_1_1_1 344.2–357.5 s | 17.8 / 8.9 | 12 / 3 | outlier knee max (z +5.1) |
| `itoi_1_1_1_t37-48` | A | 17_itoi_1_1_1 36.5–48.4 s | 8.2 / 3.9 | 17 / 6 | outlier knee max (z +4.5) |
| `itoi_1_1_1_t414-425_shift` | B | 17_itoi_1_1_1 414.1–425.0 s | 13.6 / 8.1 | 17 / 4 | outlier knee max (z +5.3) |
| `itoi_1_1_1_t426-430_shift` | B | 17_itoi_1_1_1 425.6–430.1 s | 7.7 / 5.6 | 12 / 4 | outlier knee max (z +3.8) |
| `itoi_1_1_1_t442-451_shift` | B | 17_itoi_1_1_1 442.2–450.7 s | 11.4 / 6.9 | 11 / 3 | outlier knee max (z +5.4) |
| `itoi_1_1_1_t452-465_shift` | B | 17_itoi_1_1_1 452.3–464.8 s | 20.3 / 11.9 | 23 / 7 | knee 65 deg; outlier knee max (z +9.6) |
| `itoi_1_1_1_t475-482_shift` | B | 17_itoi_1_1_1 475.4–481.7 s | 26.0 / 14.9 | 47 / 12 | human steps; outlier knee max (z +3.9) |
| `itoi_1_1_1_t482-486_shift` | B | 17_itoi_1_1_1 481.8–486.4 s | 12.3 / 9.0 | 38 / 11 | outlier knee max (z +5.4) |
| `itoi_1_1_1_t495-500_shift` | B | 17_itoi_1_1_1 495.2–500.1 s | 14.6 / 8.6 | 34 / 10 | outlier knee max (z +4.7) |
| `itoi_1_1_1_t525-540_shift` | B | 17_itoi_1_1_1 525.5–539.5 s | 16.9 / 10.3 | 11 / 4 | outlier knee max (z +5.2) |
| `itoi_1_1_1_t53-61_shift` | B | 17_itoi_1_1_1 52.9–61.2 s | 14.1 / 9.1 | 47 / 14 | outlier knee max (z +3.7) |
| `itoi_1_1_1_t544-558_shift` | B | 17_itoi_1_1_1 543.9–558.2 s | 18.9 / 10.8 | 23 / 7 | outlier knee max (z +6.8) |
| `itoi_1_1_1_t558-563_shift` | B | 17_itoi_1_1_1 558.3–562.9 s | 9.7 / 5.6 | 21 / 6 | outlier knee max (z +3.8) |
| `itoi_1_1_1_t561-573` | A | 17_itoi_1_1_1 560.9–572.7 s | 8.0 / 2.4 | 70 / 20 | outlier arms k1 cm (z +3.6) |
| `itoi_1_1_1_t574-589_shift` | B | 17_itoi_1_1_1 574.2–589.5 s | 17.6 / 9.8 | 47 / 14 | knee 63 deg; outlier knee max (z +9.0) |
| `itoi_1_1_1_t610-620_shift` | B | 17_itoi_1_1_1 610.2–620.4 s | 20.2 / 10.5 | 53 / 16 | outlier knee max (z +6.0) |
| `itoi_1_1_1_t69-78_shift` | B | 17_itoi_1_1_1 69.4–77.6 s | 15.9 / 9.0 | 36 / 13 | outlier knee max (z +4.4) |
| `itoi_1_1_1_t93-99_shift` | B | 17_itoi_1_1_1 93.2–98.8 s | 14.4 / 7.9 | 19 / 6 | outlier knee max (z +6.5) |
| `itoi_1_2_2_t0-4_shift` | B | 17_itoi_1_2_2 0.0–4.3 s | 19.4 / 11.2 | 17 / 4 | outlier knee max (z +4.3) |
| `itoi_1_2_2_t109-114_shift` | B | 17_itoi_1_2_2 108.6–113.7 s | 19.0 / 11.3 | 20 / 7 | outlier knee max (z +3.7) |
| `itoi_1_2_2_t112-118` | A | 17_itoi_1_2_2 111.7–118.3 s | 9.9 / 5.5 | 17 / 6 | outlier knee max (z +3.9) |
| `itoi_1_2_2_t15-23_shift` | B | 17_itoi_1_2_2 14.7–23.4 s | 12.4 / 6.0 | 21 / 6 | outlier knee max (z +4.9) |
| `itoi_1_2_2_t151-165` | A | 17_itoi_1_2_2 151.4–164.8 s | 8.9 / 5.5 | 38 / 13 | outlier knee max (z +3.9) |
| `itoi_1_2_2_t163-170_shift` | B | 17_itoi_1_2_2 162.8–170.5 s | 14.3 / 8.1 | 17 / 5 | outlier knee max (z +3.9) |
| `itoi_1_2_2_t223-242_shift` | B | 17_itoi_1_2_2 223.2–241.8 s | 17.7 / 10.1 | 36 / 12 | outlier knee max (z +5.4) |
| `itoi_1_2_2_t260-264_shift` | B | 17_itoi_1_2_2 259.7–264.4 s | 18.5 / 12.5 | 28 / 10 | outlier knee max (z +3.8) |
| `itoi_1_2_2_t278-286_shift` | B | 17_itoi_1_2_2 278.5–286.2 s | 24.9 / 14.1 | 34 / 12 | outlier knee max (z +5.3) |
| `itoi_1_2_2_t311-328_shift` | B | 17_itoi_1_2_2 310.9–328.1 s | 19.1 / 11.1 | 29 / 9 | outlier knee max (z +6.4) |
| `itoi_1_2_2_t342-350_shift` | B | 17_itoi_1_2_2 342.0–350.4 s | 9.4 / 5.9 | 27 / 8 | outlier knee max (z +4.3) |
| `itoi_1_2_2_t354-359_shift` | B | 17_itoi_1_2_2 354.5–359.1 s | 13.6 / 10.0 | 14 / 5 | outlier knee max (z +4.0) |
| `itoi_1_2_2_t370-375_shift` | B | 17_itoi_1_2_2 370.3–374.9 s | 22.4 / 13.1 | 18 / 5 | outlier knee max (z +5.2) |
| `itoi_1_2_2_t381-388_shift` | B | 17_itoi_1_2_2 381.0–387.9 s | 28.5 / 17.6 | 3 / 2 | human steps; outlier knee max (z +6.2) |
| `itoi_1_2_2_t395-404_shift` | B | 17_itoi_1_2_2 395.1–403.8 s | 20.7 / 11.4 | 7 / 3 | outlier knee max (z +5.3) |
| `itoi_1_2_2_t40-44_shift` | B | 17_itoi_1_2_2 39.9–44.3 s | 11.1 / 5.0 | 10 / 6 | outlier knee max (z +6.2) |
| `itoi_1_2_2_t411-427_shift` | B | 17_itoi_1_2_2 411.2–426.6 s | 16.5 / 9.7 | 46 / 12 | outlier knee max (z +6.9) |
| `itoi_1_2_2_t42-52` | A | 17_itoi_1_2_2 42.3–52.1 s | 8.1 / 4.0 | 34 / 13 | outlier knee max (z +6.0) |
| `itoi_1_2_2_t435-444_shift` | B | 17_itoi_1_2_2 434.5–443.8 s | 17.2 / 10.2 | 41 / 11 | outlier knee max (z +6.6) |
| `itoi_1_2_2_t444-451_shift` | B | 17_itoi_1_2_2 443.9–450.7 s | 14.7 / 10.4 | 34 / 8 | outlier knee max (z +4.0) |
| `itoi_1_2_2_t449-466` | A | 17_itoi_1_2_2 448.7–466.2 s | 10.0 / 3.6 | 26 / 7 | outlier knee max (z +5.3) |
| `itoi_1_2_2_t5-9_shift` | B | 17_itoi_1_2_2 4.7–9.2 s | 9.0 / 5.1 | 16 / 6 | outlier knee max (z +4.2) |
| `itoi_1_2_2_t61-66_shift` | B | 17_itoi_1_2_2 61.3–65.9 s | 8.1 / 4.6 | 43 / 16 | self-collision left_hand_collision / trunk_collision 0.6 s (at 2.0 s, 10 mm) |
| `itoi_1_2_2_t626-631_shift` | B | 17_itoi_1_2_2 625.7–630.7 s | 10.1 / 4.8 | 32 / 9 | outlier knee max (z +6.0) |
| `itoi_1_2_2_t631-641_shift` | B | 17_itoi_1_2_2 631.3–641.2 s | 18.3 / 8.5 | 41 / 10 | outlier knee max (z +6.2) |
| `itoi_1_2_2_t644-651_shift` | B | 17_itoi_1_2_2 644.0–651.1 s | 15.4 / 8.7 | 26 / 7 | outlier knee max (z +5.3) |
| `itoi_1_2_2_t662-666_shift` | B | 17_itoi_1_2_2 661.7–666.3 s | 12.7 / 8.5 | 28 / 7 | outlier knee max (z +5.4) |
| `itoi_1_2_2_t745-763` | A | 17_itoi_1_2_2 745.4–762.7 s | 8.9 / 4.5 | 25 / 8 | outlier knee max (z +3.6) |
| `itoi_1_2_2_t763-780` | A | 17_itoi_1_2_2 762.7–780.1 s | 13.8 / 7.7 | 23 / 7 | human steps |
| `itoi_1_2_2_t78-86` | A | 17_itoi_1_2_2 78.3–86.2 s | 5.5 / 2.3 | 19 / 5 | outlier knee max (z +4.2) |
| `itoi_1_2_2_t780-795` | A | 17_itoi_1_2_2 780.1–795.2 s | 7.9 / 3.9 | 20 / 7 | outlier knee max (z +5.3) |
| `itoi_1_2_2_t84-90_shift` | B | 17_itoi_1_2_2 84.2–90.0 s | 12.3 / 7.4 | 27 / 8 | outlier knee max (z +4.2) |
| `itoi_1_2_2_t96-106_shift` | B | 17_itoi_1_2_2 95.9–106.3 s | 28.8 / 15.8 | 13 / 4 | human steps; outlier knee max (z +6.4) |
| `itoi_1_3_3_t0-8_shift` | B | 17_itoi_1_3_3 0.0–7.8 s | 19.3 / 10.7 | 22 / 5 | outlier knee max (z +6.2) |
| `itoi_1_3_3_t10-18_shift` | B | 17_itoi_1_3_3 10.2–17.6 s | 16.7 / 7.7 | 19 / 7 | outlier knee max (z +4.9) |
| `itoi_1_3_3_t115-119_shift` | B | 17_itoi_1_3_3 114.9–119.5 s | 15.9 / 9.6 | 14 / 3 | outlier knee max (z +6.4) |
| `itoi_1_3_3_t120-126_shift` | B | 17_itoi_1_3_3 120.4–126.4 s | 20.5 / 13.8 | 15 / 5 | outlier knee max (z +3.6) |
| `itoi_1_3_3_t124-134` | A | 17_itoi_1_3_3 124.4–134.3 s | 9.1 / 2.6 | 6 / 2 | outlier knee max (z +4.1) |
| `itoi_1_3_3_t132-136_shift` | B | 17_itoi_1_3_3 131.8–135.8 s | 20.5 / 12.1 | 7 / 2 | outlier knee max (z +5.0) |
| `itoi_1_3_3_t140-148_shift` | B | 17_itoi_1_3_3 140.2–147.5 s | 13.2 / 5.5 | 15 / 5 | outlier knee max (z +3.9) |
| `itoi_1_3_3_t161-172_shift` | B | 17_itoi_1_3_3 161.2–171.6 s | 16.4 / 9.5 | 19 / 6 | outlier knee max (z +4.3) |
| `itoi_1_3_3_t180-188_shift` | B | 17_itoi_1_3_3 180.3–188.2 s | 15.4 / 8.5 | 14 / 4 | outlier knee max (z +4.7) |
| `itoi_1_3_3_t186-198` | A | 17_itoi_1_3_3 186.2–197.6 s | 9.9 / 5.6 | 10 / 3 | outlier knee max (z +4.4) |
| `itoi_1_3_3_t233-241_shift` | B | 17_itoi_1_3_3 233.0–241.1 s | 13.9 / 8.1 | 16 / 4 | outlier knee max (z +4.0) |
| `itoi_1_3_3_t24-32_shift` | B | 17_itoi_1_3_3 24.1–31.7 s | 12.1 / 6.5 | 31 / 8 | outlier knee max (z +3.9) |
| `itoi_1_3_3_t300-312` | A | 17_itoi_1_3_3 300.2–311.9 s | 10.3 / 5.8 | 13 / 4 | human steps |
| `itoi_1_3_3_t314-320_shift` | B | 17_itoi_1_3_3 313.9–320.4 s | 18.1 / 10.0 | 22 / 7 | outlier knee max (z +4.8) |
| `itoi_1_3_3_t401-411_shift` | B | 17_itoi_1_3_3 401.4–411.4 s | 20.6 / 11.4 | 10 / 3 | outlier knee max (z +3.7) |
| `itoi_1_3_3_t421-429_shift` | B | 17_itoi_1_3_3 420.9–429.1 s | 12.2 / 8.8 | 12 / 3 | knee 64 deg; outlier knee max (z +9.3) |
| `itoi_1_3_3_t430-449_shift` | B | 17_itoi_1_3_3 429.7–449.3 s | 16.1 / 9.4 | 16 / 5 | outlier knee max (z +5.5) |
| `itoi_1_3_3_t468-476_shift` | B | 17_itoi_1_3_3 468.5–476.1 s | 16.1 / 8.3 | 18 / 6 | outlier knee max (z +4.0) |
| `itoi_1_3_3_t480-488_shift` | B | 17_itoi_1_3_3 479.8–488.0 s | 15.6 / 8.5 | 18 / 5 | outlier knee max (z +5.3) |
| `itoi_1_3_3_t521-531_shift` | B | 17_itoi_1_3_3 521.2–531.2 s | 15.2 / 7.9 | 24 / 7 | outlier knee max (z +4.3) |
| `itoi_1_3_3_t565-573_shift` | B | 17_itoi_1_3_3 564.8–573.1 s | 12.0 / 7.5 | 17 / 5 | outlier knee max (z +3.9) |
| `itoi_1_3_3_t574-585_shift` | B | 17_itoi_1_3_3 573.6–584.8 s | 29.8 / 16.2 | 19 / 5 | human steps; outlier knee max (z +5.2) |
| `itoi_1_3_3_t595-600` | A | 17_itoi_1_3_3 594.8–599.8 s | 8.6 / 7.7 | 12 / 4 | outlier knee max (z +4.5) |
| `itoi_1_3_3_t598-605_shift` | B | 17_itoi_1_3_3 597.8–604.7 s | 19.4 / 11.0 | 14 / 6 | outlier knee max (z +4.5) |
| `jorge_0_10_10_t36-40_shift` | B | 16_jorge_0_10_10 36.0–40.3 s | 20.9 / 12.0 | 46 / 10 | outlier knee max (z +5.7) |
| `jorge_0_11_11_t16-32_shift` | B | 16_jorge_0_11_11 16.3–31.7 s | 22.8 / 13.4 | 45 / 9 | outlier knee max (z +5.0) |
| `jorge_0_16_16_t26-31_shift` | B | 16_jorge_0_16_16 26.5–31.0 s | 21.9 / 13.4 | 45 / 11 | outlier knee max (z +5.8) |
| `jorge_0_2_2_t0-5_shift` | B | 16_jorge_0_2_2 0.5–4.9 s | 19.8 / 9.9 | 15 / 3 | outlier knee max (z +4.9) |
| `jorge_0_2_2_t39-47_shift` | B | 16_jorge_0_2_2 38.6–46.9 s | 24.4 / 13.8 | 20 / 5 | outlier knee max (z +6.1) |
| `jorge_0_4_4_t13-17_shift` | B | 16_jorge_0_4_4 12.7–16.9 s | 22.9 / 11.7 | 17 / 4 | outlier knee max (z +5.4) |
| `jorge_0_4_4_t47-54_shift` | B | 16_jorge_0_4_4 46.7–53.5 s | 24.0 / 12.8 | 30 / 6 | outlier knee max (z +4.7) |
| `jorge_0_5_5_t29-33_shift` | B | 16_jorge_0_5_5 28.6–33.2 s | 20.8 / 11.3 | 43 / 9 | shoulder at limit 25%; outlier knee max (z +5.1) |
| `jorge_0_6_6_t33-41_shift` | B | 16_jorge_0_6_6 33.4–40.7 s | 20.3 / 11.0 | 19 / 4 | outlier knee max (z +5.7) |
| `jorge_0_6_6_t53-60_shift` | B | 16_jorge_0_6_6 53.1–59.8 s | 24.6 / 14.5 | 22 / 6 | outlier knee max (z +4.8) |
| `jorge_0_6_6_t6-24_shift` | B | 16_jorge_0_6_6 6.3–23.9 s | 23.8 / 13.6 | 41 / 8 | outlier knee max (z +5.2) |
| `jorge_0_7_7_t14-21_shift` | B | 16_jorge_0_7_7 13.8–21.1 s | 24.8 / 13.4 | 45 / 11 | outlier knee max (z +6.7) |
| `jorge_0_7_7_t27-45_shift` | B | 16_jorge_0_7_7 26.7–44.7 s | 22.2 / 12.4 | 35 / 8 | outlier knee max (z +7.7) |
| `jorge_0_7_7_t5-9_shift` | B | 16_jorge_0_7_7 5.1–9.1 s | 20.3 / 11.2 | 54 / 12 | outlier knee max (z +4.3) |
| `jorge_0_81_81_t28-36_shift` | B | 16_jorge_0_81_81 27.6–35.8 s | 20.6 / 13.4 | 18 / 5 | outlier knee max (z +6.4) |
| `jorge_0_81_81_t36-43_shift` | B | 16_jorge_0_81_81 36.5–43.1 s | 20.7 / 11.8 | 21 / 6 | outlier knee max (z +6.1); self-collision right_hand_collision / trunk_collision 0.2 s (at 4.6 s, 11 mm) |
| `jorge_0_81_81_t44-49_shift` | B | 16_jorge_0_81_81 44.0–49.0 s | 19.9 / 12.3 | 12 / 3 | outlier knee max (z +6.8) |
| `jorge_0_82_82_t35-39_shift` | B | 16_jorge_0_82_82 34.8–39.2 s | 15.2 / 5.5 | 29 / 7 | outlier knee max (z +6.6) |
| `jorge_0_82_82_t43-55_shift` | B | 16_jorge_0_82_82 42.7–54.8 s | 19.7 / 10.3 | 25 / 7 | outlier knee max (z +6.6) |
| `jorge_0_87_87_t47-57_shift` | B | 16_jorge_0_87_87 46.6–56.5 s | 20.3 / 11.7 | 50 / 14 | outlier knee max (z +3.5) |
| `jorge_0_88_88_t3-7_shift` | B | 16_jorge_0_88_88 2.8–7.1 s | 16.0 / 6.3 | 123 / 28 | outlier arms k1 cm (z +5.7) |
| `jorge_0_8_8_t0-6_shift` | B | 16_jorge_0_8_8 0.2–5.9 s | 19.3 / 11.5 | 30 / 6 | outlier knee max (z +4.6) |
| `jorge_0_8_8_t27-31_shift` | B | 16_jorge_0_8_8 26.6–30.6 s | 24.4 / 15.6 | 52 / 12 | outlier knee max (z +6.7) |
| `jorge_0_8_8_t51-55_shift` | B | 16_jorge_0_8_8 50.9–55.3 s | 22.2 / 12.0 | 28 / 6 | outlier knee max (z +5.0) |
| `jorge_0_8_8_t8-12_shift` | B | 16_jorge_0_8_8 7.8–12.1 s | 22.3 / 13.1 | 24 / 6 | outlier knee max (z +3.9) |
| `jorge_0_9_9_t41-46_shift` | B | 16_jorge_0_9_9 41.4–45.5 s | 23.0 / 15.8 | 37 / 8 | outlier knee max (z +5.0) |
| `jorge_1_1_1_t151-160_shift` | B | 16_jorge_1_1_1 151.2–159.5 s | 15.5 / 11.5 | 33 / 7 | outlier knee max (z +4.7) |
| `jorge_1_1_1_t291-300` | A | 16_jorge_1_1_1 290.5–299.6 s | 0.8 / 0.8 | 9 / 3 | hand presses into leg 17 mm for 2.9 s (at 1.1 s) |
| `jorge_1_1_1_t32-43_shift` | B | 16_jorge_1_1_1 31.7–42.6 s | 23.6 / 13.2 | 31 / 6 | outlier knee max (z +4.1) |
| `jorge_1_1_1_t335-340_shift` | B | 16_jorge_1_1_1 335.0–340.3 s | 22.1 / 13.8 | 12 / 3 | outlier knee max (z +3.9) |
| `jorge_1_1_1_t384-401_shift` | B | 16_jorge_1_1_1 383.7–401.1 s | 21.0 / 12.5 | 26 / 7 | outlier knee max (z +7.9) |
| `jorge_1_1_1_t412-417_shift` | B | 16_jorge_1_1_1 412.2–416.6 s | 24.5 / 14.1 | 26 / 7 | outlier knee max (z +6.0) |
| `jorge_1_1_1_t417-421_shift` | B | 16_jorge_1_1_1 416.6–421.3 s | 22.4 / 10.5 | 23 / 6 | outlier knee max (z +4.9); hand presses into leg 9 mm for 0.2 s (at 1.9 s) |
| `jorge_1_1_1_t493-499_shift` | B | 16_jorge_1_1_1 493.1–498.9 s | 10.8 / 6.6 | 45 / 9 | outlier knee max (z +4.7) |
| `jorge_1_1_1_t499-515_shift` | B | 16_jorge_1_1_1 499.0–514.8 s | 23.6 / 14.1 | 36 / 8 | outlier knee max (z +6.5) |
| `jorge_1_1_1_t553-558_shift` | B | 16_jorge_1_1_1 553.0–557.9 s | 21.1 / 18.7 | 30 / 9 | K1 feet move 19 cm; outlier knee max (z +6.7) |
| `jorge_1_1_1_t563-579_shift` | B | 16_jorge_1_1_1 562.9–579.4 s | 22.7 / 14.3 | 39 / 8 | shoulder at limit 28% |
| `jorge_1_1_1_t590-594_shift` | B | 16_jorge_1_1_1 589.5–593.8 s | 20.0 / 10.9 | 14 / 4 | outlier knee max (z +6.2) |
| `jorge_1_1_1_t77-82_shift` | B | 16_jorge_1_1_1 77.1–81.7 s | 23.7 / 16.5 | 9 / 2 | outlier knee max (z +5.6) |
| `jorge_1_2_2_t142-147_shift` | B | 16_jorge_1_2_2 142.0–146.6 s | 24.0 / 14.9 | 26 / 6 | shoulder at limit 7%; outlier knee max (z +3.7) |
| `jorge_1_2_2_t145-150` | A | 16_jorge_1_2_2 144.6–149.8 s | 8.9 / 4.1 | 32 / 7 | shoulder at limit 11% |
| `jorge_1_2_2_t186-192_shift` | B | 16_jorge_1_2_2 185.7–192.5 s | 18.3 / 11.2 | 21 / 5 | outlier knee max (z +3.7); hand presses into leg 12 mm for 0.3 s (at 4.1 s) |
| `jorge_1_2_2_t455-462` | A | 16_jorge_1_2_2 454.9–461.9 s | 4.4 / 4.7 | 18 / 7 | hand presses into leg 10 mm for 0.4 s (at 6.3 s) |
| `jorge_1_2_2_t500-508_shift` | B | 16_jorge_1_2_2 499.6–508.4 s | 24.1 / 12.7 | 36 / 8 | outlier knee max (z +6.3) |
| `jorge_1_2_2_t572-576_shift` | B | 16_jorge_1_2_2 572.0–576.3 s | 18.5 / 6.3 | 20 / 4 | outlier knee max (z +6.1) |
| `jorge_1_3_3_t294-298_shift` | B | 16_jorge_1_3_3 293.6–297.6 s | 15.5 / 9.9 | 5 / 2 | outlier knee max (z +4.9) |
| `jorge_1_3_3_t384-390_shift` | B | 16_jorge_1_3_3 384.1–389.7 s | 17.2 / 12.4 | 33 / 8 | knee 66 deg; outlier knee max (z +10.1) |
| `jorge_1_3_3_t429-436_shift` | B | 16_jorge_1_3_3 428.6–435.6 s | 16.7 / 9.6 | 25 / 7 | outlier knee max (z +3.9) |
| `jorge_1_3_3_t445-450_shift` | B | 16_jorge_1_3_3 445.0–449.6 s | 22.1 / 12.6 | 23 / 7 | outlier knee max (z +4.6) |
| `jorge_1_3_3_t550-554_shift` | B | 16_jorge_1_3_3 549.5–553.5 s | 15.0 / 8.8 | 17 / 7 | elbow bend at limit 87% |
| `jorge_1_3_3_t550-555` | A | 16_jorge_1_3_3 550.1–555.0 s | 1.5 / 0.6 | 13 / 8 | elbow bend at limit 73% |
| `jorge_1_3_3_t579-589_shift` | B | 16_jorge_1_3_3 579.2–589.0 s | 19.3 / 11.9 | 14 / 4 | outlier knee max (z +4.3); hand presses into leg 15 mm for 0.3 s (at 6.4 s) |
| `jorge_1_3_3_t590-594_shift` | B | 16_jorge_1_3_3 590.0–594.0 s | 24.9 / 11.6 | 4 / 1 | outlier knee max (z +4.8) |
| `katya_0_103_103_t68-84` | A | 30_katya_0_103_103 67.7–83.8 s | 0.5 / 0.3 | 13 / 5 | outlier knee max (z -4.7) |
| `katya_0_104_104_t0-16` | A | 30_katya_0_104_104 0.0–16.2 s | 6.5 / 4.6 | 11 / 4 | self-collision right_hand_collision / trunk_collision 0.1 s (at 9.7 s, 7 mm) |
| `katya_0_104_104_t32-49` | A | 30_katya_0_104_104 32.5–48.7 s | 3.5 / 1.7 | 10 / 4 | self-collision right_hand_collision / trunk_collision 0.2 s (at 14.2 s, 13 mm) |
| `katya_0_10_10_t11-22` | A | 30_katya_0_10_10 11.1–21.6 s | 1.5 / 0.8 | 17 / 6 | elbow bend at limit 6% |
| `katya_0_10_10_t54-69` | A | 30_katya_0_10_10 54.2–68.8 s | 2.0 / 0.9 | 14 / 6 | self-collision right_hand_collision / trunk_collision 0.8 s (at 2.5 s, 15 mm) |
| `katya_0_10_10_t9-13_shift` | B | 30_katya_0_10_10 8.6–13.1 s | 9.0 / 4.4 | 16 / 8 | elbow bend at limit 5% |
| `katya_0_112_112_t48-54_shift` | B | 30_katya_0_112_112 48.2–54.2 s | 19.2 / 10.7 | 28 / 11 | outlier knee max (z +5.3) |
| `katya_0_11_11_t32-47` | A | 30_katya_0_11_11 32.1–47.3 s | 5.5 / 1.6 | 14 / 6 | elbow bend at limit 12% |
| `katya_0_11_11_t47-63` | A | 30_katya_0_11_11 47.3–62.5 s | 5.0 / 1.7 | 13 / 4 | self-collision right_hand_collision / trunk_collision 0.2 s (at 2.3 s, 8 mm) |
| `katya_0_12_12_t64-75` | A | 30_katya_0_12_12 63.5–74.8 s | 9.9 / 1.9 | 13 / 5 | outlier knee max (z +3.8) |
| `katya_0_14_14_t69-86` | A | 30_katya_0_14_14 69.2–85.8 s | 3.4 / 2.9 | 16 / 6 | self-collision right_hand_collision / trunk_collision 0.3 s (at 1.5 s, 19 mm) |
| `katya_0_15_15_t11-17_shift` | B | 30_katya_0_15_15 11.5–17.3 s | 19.7 / 11.1 | 8 / 4 | outlier knee max (z +4.4) |
| `katya_0_15_15_t15-35` | A | 30_katya_0_15_15 15.3–35.1 s | 2.4 / 1.8 | 13 / 6 | self-collision right_hand_collision / trunk_collision 2.1 s (at 7.2 s, 15 mm) |
| `katya_0_16_16_t0-10` | A | 30_katya_0_16_16 0.0–10.1 s | 2.2 / 0.4 | 6 / 3 | self-collision right_hand_collision / trunk_collision 0.3 s (at 7.0 s, 7 mm) |
| `katya_0_1_1_t0-16` | A | 30_katya_0_1_1 0.0–16.1 s | 0.8 / 1.0 | 18 / 7 | elbow bend at limit 8% |
| `katya_0_1_1_t33-51` | A | 30_katya_0_1_1 32.8–51.5 s | 9.8 / 4.0 | 23 / 7 | leg at limit 13% |
| `katya_0_1_1_t66-74` | A | 30_katya_0_1_1 66.5–73.8 s | 3.9 / 1.4 | 27 / 9 | elbow bend at limit 5% |
| `katya_0_2_2_t61-65_shift` | B | 30_katya_0_2_2 60.7–65.3 s | 16.4 / 8.0 | 16 / 6 | self-collision right_hand_collision / trunk_collision 1.2 s (at 3.4 s, 12 mm) |
| `katya_0_2_2_t63-77` | A | 30_katya_0_2_2 63.3–76.8 s | 5.7 / 1.3 | 24 / 8 | self-collision right_hand_collision / trunk_collision 1.4 s (at 0.8 s, 12 mm) |
| `katya_0_3_3_t18-23_shift` | B | 30_katya_0_3_3 18.1–23.2 s | 10.0 / 5.4 | 22 / 7 | elbow bend at limit 9% |
| `katya_0_3_3_t21-37` | A | 30_katya_0_3_3 21.2–37.0 s | 2.3 / 2.0 | 14 / 6 | elbow bend at limit 5% |
| `katya_0_3_3_t65-77` | A | 30_katya_0_3_3 65.1–76.8 s | 5.1 / 1.4 | 23 / 8 | outlier knee max (z +7.7) |
| `katya_0_4_4_t25-45` | A | 30_katya_0_4_4 25.0–44.6 s | 4.4 / 1.0 | 18 / 6 | elbow bend at limit 10%; self-collision left_hand_end_collision / right_hand_end_collision 0.6 s (at 11.1 s, 15 mm) |
| `katya_0_5_5_t51-68` | A | 30_katya_0_5_5 50.9–67.8 s | 5.7 / 1.7 | 18 / 7 | self-collision left_hand_collision / trunk_collision 0.4 s (at 11.7 s, 11 mm) |
| `katya_0_5_5_t68-85` | A | 30_katya_0_5_5 67.8–84.8 s | 3.8 / 2.7 | 14 / 5 | elbow bend at limit 21% |
| `katya_0_65_65_t16-20_shift` | B | 30_katya_0_65_65 15.7–20.2 s | 11.9 / 4.7 | 39 / 16 | outlier knee max (z +3.8) |
| `katya_0_65_65_t21-26_shift` | B | 30_katya_0_65_65 21.3–25.7 s | 7.1 / 3.2 | 36 / 11 | shoulder at limit 16% |
| `katya_0_65_65_t24-30` | A | 30_katya_0_65_65 23.7–29.8 s | 4.6 / 1.0 | 39 / 14 | shoulder at limit 10% |
| `katya_0_65_65_t28-32_shift` | B | 30_katya_0_65_65 27.8–32.5 s | 15.1 / 8.2 | 21 / 8 | outlier knee max (z +5.1) |
| `katya_0_65_65_t30-46` | A | 30_katya_0_65_65 30.5–45.6 s | 7.7 / 4.1 | 29 / 12 | shoulder at limit 15%; outlier knee max (z +4.7) |
| `katya_0_65_65_t46-61` | A | 30_katya_0_65_65 45.6–60.8 s | 3.9 / 2.1 | 38 / 14 | shoulder at limit 5% |
| `katya_0_66_66_t41-47` | A | 30_katya_0_66_66 41.0–47.2 s | 9.0 / 5.5 | 30 / 11 | elbow bend at limit 11%; self-collision right_hand_end_collision / trunk_collision 0.2 s (at 5.0 s, 10 mm) |
| `katya_0_66_66_t45-49_shift` | B | 30_katya_0_66_66 45.2–49.3 s | 9.8 / 5.2 | 39 / 12 | self-collision right_hand_end_collision / trunk_collision 0.2 s (at 0.7 s, 10 mm) |
| `katya_0_66_66_t58-71` | A | 30_katya_0_66_66 57.6–71.3 s | 5.9 / 1.6 | 31 / 12 | shoulder at limit 22%; elbow bend at limit 17% |
| `katya_0_6_6_t34-50` | A | 30_katya_0_6_6 33.5–50.3 s | 4.8 / 1.0 | 13 / 5 | elbow bend at limit 9% |
| `katya_0_6_6_t67-84` | A | 30_katya_0_6_6 67.0–83.8 s | 3.3 / 0.8 | 17 / 5 | elbow bend at limit 6% |
| `katya_0_73_73_t0-20` | A | 30_katya_0_73_73 0.0–19.6 s | 6.7 / 0.9 | 24 / 9 | self-collision right_hand_end_collision / trunk_collision 1.2 s (at 2.5 s, 23 mm) |
| `katya_0_73_73_t32-37_shift` | B | 30_katya_0_73_73 32.5–37.1 s | 11.6 / 6.4 | 70 / 21 | outlier arms k1 cm (z +3.9) |
| `katya_0_74_74_t0-17` | A | 30_katya_0_74_74 0.0–17.2 s | 5.1 / 3.2 | 24 / 8 | elbow bend at limit 12% |
| `katya_0_74_74_t15-20_shift` | B | 30_katya_0_74_74 15.2–20.1 s | 12.5 / 9.1 | 22 / 10 | elbow bend at limit 12%; outlier knee max (z +4.3) |
| `katya_0_74_74_t18-36` | A | 30_katya_0_74_74 18.1–35.6 s | 4.5 / 1.3 | 24 / 10 | self-collision left_hand_end_collision / right_hand_end_collision 0.9 s (at 12.6 s, 13 mm) |
| `katya_0_7_7_t58-77` | A | 30_katya_0_7_7 57.6–76.8 s | 3.7 / 0.7 | 18 / 6 | shoulder at limit 10% |
| `katya_0_81_81_t0-18` | A | 30_katya_0_81_81 0.0–18.2 s | 0.3 / 0.3 | 16 / 5 | self-collision right_hand_collision / trunk_collision 0.9 s (at 3.6 s, 11 mm) |
| `katya_0_81_81_t36-55` | A | 30_katya_0_81_81 36.4–54.6 s | 0.5 / 0.2 | 13 / 4 | elbow bend at limit 9% |
| `katya_0_82_82_t0-15` | A | 30_katya_0_82_82 0.0–15.5 s | 3.2 / 1.3 | 17 / 8 | elbow bend at limit 12% |
| `katya_0_82_82_t15-31` | A | 30_katya_0_82_82 15.5–30.9 s | 2.7 / 0.7 | 20 / 8 | self-collision left_hand_collision / trunk_collision 0.4 s (at 15.1 s, 9 mm) |
| `katya_0_82_82_t29-33_shift` | B | 30_katya_0_82_82 28.9–33.3 s | 7.1 / 3.8 | 13 / 5 | self-collision left_hand_collision / trunk_collision 0.5 s (at 1.6 s, 9 mm) |
| `katya_0_82_82_t31-51` | A | 30_katya_0_82_82 31.3–50.9 s | 2.8 / 0.7 | 19 / 7 | self-collision right_hand_collision / trunk_collision 0.3 s (at 1.1 s, 7 mm) |
| `katya_0_87_87_t0-10` | A | 30_katya_0_87_87 0.0–9.6 s | 5.7 / 1.0 | 32 / 10 | elbow bend at limit 10% |
| `katya_0_87_87_t55-68` | A | 30_katya_0_87_87 54.7–68.3 s | 2.4 / 0.7 | 7 / 2 | elbow bend at limit 8% |
| `katya_0_87_87_t8-12_shift` | B | 30_katya_0_87_87 7.6–12.1 s | 11.9 / 7.6 | 20 / 8 | elbow bend at limit 26% |
| `katya_0_88_88_t70-88` | A | 30_katya_0_88_88 70.3–87.9 s | 2.4 / 0.7 | 28 / 10 | self-collision right_hand_collision / trunk_collision 0.2 s (at 5.5 s, 15 mm) |
| `katya_0_8_8_t0-19` | A | 30_katya_0_8_8 0.0–19.3 s | 9.0 / 4.2 | 15 / 6 | elbow bend at limit 21% |
| `katya_0_8_8_t19-39` | A | 30_katya_0_8_8 19.3–38.5 s | 4.8 / 2.3 | 24 / 10 | elbow bend at limit 14% |
| `katya_0_9_9_t18-31` | A | 30_katya_0_9_9 18.3–30.8 s | 5.5 / 2.6 | 10 / 4 | elbow bend at limit 20% |
| `katya_0_9_9_t45-49_shift` | B | 30_katya_0_9_9 45.0–49.0 s | 24.6 / 13.2 | 20 / 8 | outlier knee max (z +5.3) |
| `katya_0_9_9_t49-67` | A | 30_katya_0_9_9 48.7–67.3 s | 9.5 / 4.7 | 10 / 5 | elbow bend at limit 5% |
| `katya_1_1_1_t0-14` | A | 30_katya_1_1_1 0.0–14.3 s | 3.2 / 1.1 | 4 / 2 | self-collision right_hand_collision / trunk_collision 1.2 s (at 8.2 s, 12 mm) |
| `katya_1_1_1_t137-155` | A | 30_katya_1_1_1 137.2–154.6 s | 4.2 / 2.5 | 15 / 6 | elbow bend at limit 10% |
| `katya_1_1_1_t187-191_shift` | B | 30_katya_1_1_1 186.6–191.3 s | 14.7 / 6.3 | 10 / 4 | outlier knee max (z +4.6) |
| `katya_1_1_1_t219-234` | A | 30_katya_1_1_1 219.1–233.7 s | 8.7 / 2.9 | 15 / 7 | elbow bend at limit 19%; leg at limit 9% |
| `katya_1_1_1_t270-283` | A | 30_katya_1_1_1 270.3–283.5 s | 8.7 / 4.5 | 17 / 8 | leg at limit 8% |
| `katya_1_1_1_t332-345` | A | 30_katya_1_1_1 331.6–345.2 s | 8.4 / 4.2 | 13 / 6 | elbow bend at limit 11% |
| `katya_1_1_1_t400-415` | A | 30_katya_1_1_1 399.9–414.7 s | 7.0 / 2.8 | 15 / 7 | elbow bend at limit 27%; self-collision right_hand_collision / trunk_collision 0.4 s (at 12.9 s, 10 mm) |
| `katya_1_1_1_t428-433_shift` | B | 30_katya_1_1_1 427.5–432.7 s | 16.7 / 9.2 | 15 / 4 | outlier knee max (z +4.7) |
| `katya_1_1_1_t491-498_shift` | B | 30_katya_1_1_1 490.9–497.9 s | 13.6 / 3.6 | 9 / 4 | outlier knee max (z +3.8) |
| `katya_1_1_1_t496-502` | A | 30_katya_1_1_1 495.9–502.3 s | 9.6 / 3.0 | 3 / 1 | right arm behind body 5 cm (human's in front) |
| `katya_1_1_1_t508-513` | A | 30_katya_1_1_1 508.0–513.4 s | 3.2 / 2.9 | 6 / 3 | self-collision right_hand_collision / trunk_collision 0.4 s (at 0.0 s, 12 mm) |
| `katya_1_2_2_t107-119` | A | 30_katya_1_2_2 107.2–118.7 s | 12.7 / 4.5 | 14 / 7 | human steps; elbow bend at limit 5% |
| `katya_1_2_2_t125-129_shift` | B | 30_katya_1_2_2 124.8–128.8 s | 12.9 / 2.3 | 23 / 9 | outlier knee max (z +6.3) |
| `katya_1_2_2_t135-146_shift` | B | 30_katya_1_2_2 135.5–145.6 s | 21.3 / 7.2 | 26 / 7 | knee 61 deg; leg at limit 27%; outlier knee max (z +8.5) |
| `katya_1_2_2_t147-153_shift` | B | 30_katya_1_2_2 146.6–152.9 s | 19.0 / 5.4 | 21 / 8 | knee 62 deg; outlier knee max (z +8.7) |
| `katya_1_2_2_t163-168_shift` | B | 30_katya_1_2_2 163.1–167.9 s | 18.6 / 4.4 | 35 / 11 | outlier knee max (z +6.9) |
| `katya_1_2_2_t219-224_shift` | B | 30_katya_1_2_2 219.3–224.2 s | 11.5 / 2.7 | 11 / 3 | knee 61 deg; outlier knee max (z +8.2) |
| `katya_1_2_2_t22-28_shift` | B | 30_katya_1_2_2 22.3–28.5 s | 19.3 / 10.8 | 12 / 6 | outlier knee max (z +5.1) |
| `katya_1_2_2_t230-234_shift` | B | 30_katya_1_2_2 229.5–234.1 s | 11.4 / 3.0 | 10 / 3 | knee 60 deg; outlier knee max (z +8.1) |
| `katya_1_2_2_t275-286_shift` | B | 30_katya_1_2_2 275.1–286.1 s | 21.1 / 5.9 | 27 / 9 | outlier knee max (z +6.8) |
| `katya_1_2_2_t288-293_shift` | B | 30_katya_1_2_2 288.3–293.1 s | 11.5 / 2.5 | 34 / 11 | knee 63 deg; shoulder at limit 12%; leg at limit 26%; outlier knee max (z +9.1) |
| `katya_1_2_2_t291-310` | A | 30_katya_1_2_2 291.1–310.4 s | 9.9 / 5.7 | 19 / 7 | leg at limit 58% |
| `katya_1_2_2_t310-315` | A | 30_katya_1_2_2 310.4–314.6 s | 9.6 / 2.5 | 22 / 9 | elbow bend at limit 6% |
| `katya_1_2_2_t315-319` | A | 30_katya_1_2_2 314.6–319.3 s | 4.9 / 1.9 | 26 / 9 | shoulder at limit 29% |
| `katya_1_2_2_t337-349` | A | 30_katya_1_2_2 337.4–348.6 s | 3.3 / 3.0 | 12 / 6 | elbow bend at limit 13% |
| `katya_1_2_2_t360-372` | A | 30_katya_1_2_2 360.4–371.7 s | 10.4 / 7.5 | 15 / 7 | human steps |
| `katya_1_2_2_t416-424` | A | 30_katya_1_2_2 415.5–423.7 s | 8.3 / 4.3 | 9 / 3 | leg at limit 14% |
| `katya_1_2_2_t471-478` | A | 30_katya_1_2_2 471.2–477.6 s | 7.7 / 3.5 | 14 / 5 | leg at limit 14% |
| `katya_1_2_2_t48-62` | A | 30_katya_1_2_2 48.5–61.5 s | 6.2 / 4.0 | 16 / 5 | elbow bend at limit 12% |
| `katya_1_2_2_t503-511` | A | 30_katya_1_2_2 503.1–511.4 s | 4.5 / 3.2 | 18 / 9 | shoulder at limit 18%; self-collision right_hand_end_collision / trunk_collision 1.1 s (at 7.0 s, 20 mm) |
| `katya_1_2_2_t538-549` | A | 30_katya_1_2_2 538.0–548.7 s | 4.7 / 2.9 | 25 / 10 | elbow bend at limit 38% |
| `katya_1_2_2_t546-550_shift` | B | 30_katya_1_2_2 546.3–550.3 s | 23.1 / 12.4 | 47 / 15 | outlier knee max (z +4.2) |
| `katya_1_2_2_t561-572` | A | 30_katya_1_2_2 560.7–571.7 s | 9.2 / 2.6 | 15 / 7 | leg at limit 22% |
| `katya_1_2_2_t576-583` | A | 30_katya_1_2_2 576.1–583.3 s | 5.8 / 8.2 | 26 / 7 | K1 feet move 8 cm |
| `katya_1_2_2_t76-80_shift` | B | 30_katya_1_2_2 76.2–80.3 s | 24.8 / 12.4 | 17 / 5 | outlier knee max (z +4.0) |
| `katya_1_2_2_t84-91_shift` | B | 30_katya_1_2_2 84.4–90.6 s | 18.7 / 4.9 | 29 / 9 | knee 62 deg; outlier trunk drop (z +3.9); outlier knee max (z +8.6) |
| `katya_1_2_2_t93-98_shift` | B | 30_katya_1_2_2 93.2–97.8 s | 13.0 / 9.0 | 18 / 5 | knee 63 deg; elbow bend at limit 7%; outlier knee max (z +9.0) |
| `katya_1_2_2_t96-107` | A | 30_katya_1_2_2 95.8–107.2 s | 6.3 / 1.1 | 18 / 9 | shoulder at limit 8% |
| `katya_1_3_3_t115-120` | A | 30_katya_1_3_3 114.8–119.9 s | 5.7 / 3.3 | 30 / 10 | self-collision right_hand_collision / trunk_collision 0.1 s (at 2.2 s, 10 mm) |
| `katya_1_3_3_t148-154` | A | 30_katya_1_3_3 148.3–154.0 s | 9.7 / 7.9 | 11 / 6 | self-collision right_hand_end_collision / trunk_collision 0.2 s (at 5.1 s, 7 mm) |
| `katya_1_3_3_t163-172` | A | 30_katya_1_3_3 163.1–171.8 s | 7.3 / 3.3 | 45 / 12 | shoulder at limit 10% |
| `katya_1_3_3_t184-191_shift` | B | 30_katya_1_3_3 184.4–190.5 s | 12.5 / 4.2 | 33 / 9 | outlier knee max (z +7.5) |
| `katya_1_3_3_t19-24_shift` | B | 30_katya_1_3_3 18.8–24.1 s | 19.9 / 13.1 | 33 / 9 | leg at limit 11% |
| `katya_1_3_3_t232-236_shift` | B | 30_katya_1_3_3 232.5–236.5 s | 14.5 / 2.7 | 30 / 9 | leg at limit 38%; outlier knee max (z +6.5) |
| `katya_1_3_3_t361-377` | A | 30_katya_1_3_3 361.4–377.1 s | 8.2 / 4.3 | 24 / 8 | leg at limit 17% |
| `katya_1_3_3_t383-394` | A | 30_katya_1_3_3 383.0–394.0 s | 4.3 / 1.7 | 19 / 9 | elbow bend at limit 6%; self-collision left_hand_collision / trunk_collision 0.6 s (at 9.0 s, 9 mm) |
| `katya_1_3_3_t397-405` | A | 30_katya_1_3_3 397.4–404.8 s | 7.8 / 9.2 | 34 / 11 | K1 feet move 9 cm |
| `katya_1_3_3_t455-462` | A | 30_katya_1_3_3 454.8–461.6 s | 8.7 / 8.4 | 22 / 5 | K1 feet move 8 cm |
| `katya_1_3_3_t491-503` | A | 30_katya_1_3_3 490.7–502.7 s | 5.6 / 4.1 | 41 / 13 | elbow bend at limit 10% |
| `katya_1_3_3_t53-66` | A | 30_katya_1_3_3 53.0–65.9 s | 9.7 / 3.0 | 11 / 6 | leg at limit 16% |
| `katya_1_3_3_t537-545` | A | 30_katya_1_3_3 537.0–544.8 s | 5.7 / 2.2 | 14 / 8 | self-collision right_hand_end_collision / trunk_collision 0.5 s (at 1.9 s, 10 mm) |
| `katya_1_3_3_t564-576` | A | 30_katya_1_3_3 563.5–576.1 s | 3.7 / 2.7 | 11 / 5 | self-collision right_hand_collision / trunk_collision 1.3 s (at 9.0 s, 19 mm) |
| `katya_1_3_3_t574-582_shift` | B | 30_katya_1_3_3 574.1–581.8 s | 19.0 / 7.7 | 6 / 3 | self-collision right_hand_collision / trunk_collision 2.0 s (at 4.5 s, 11 mm); right arm behind body 6 cm (human's in front) |
| `katya_1_3_3_t580-599` | A | 30_katya_1_3_3 579.8–598.5 s | 6.6 / 3.6 | 12 / 4 | self-collision right_hand_collision / trunk_collision 8.2 s (at 2.4 s, 11 mm) |
| `katya_1_3_3_t596-600_shift` | B | 30_katya_1_3_3 595.7–599.7 s | 9.0 / 7.1 | 42 / 13 | shoulder at limit 20%; self-collision left_hand_end_collision / right_hand_end_collision 0.2 s (at 2.5 s, 21 mm) |
| `katya_1_3_3_t64-68_shift` | B | 30_katya_1_3_3 63.9–68.1 s | 10.1 / 2.4 | 10 / 5 | outlier knee max (z +5.8) |
| `katya_1_3_3_t75-80_shift` | B | 30_katya_1_3_3 75.1–79.7 s | 9.1 / 4.8 | 17 / 6 | elbow bend at limit 12% |
| `katya_1_3_3_t78-85` | A | 30_katya_1_3_3 77.7–85.3 s | 4.5 / 4.2 | 14 / 5 | elbow bend at limit 8% |
| `katya_1_3_3_t95-99_shift` | B | 30_katya_1_3_3 94.6–99.3 s | 6.6 / 3.6 | 29 / 11 | elbow bend at limit 11% |
| `kexin_0_65_65_t10-20` | A | 24_kexin_0_65_65 10.3–20.5 s | 1.6 / 2.2 | 14 / 5 | self-collision right_hand_collision / trunk_collision 0.4 s (at 9.8 s, 7 mm) |
| `kexin_0_66_66_t38-43_shift` | B | 24_kexin_0_66_66 38.4–43.3 s | 17.3 / 8.3 | 14 / 4 | outlier knee max (z +5.6) |
| `kexin_0_66_66_t41-55` | A | 24_kexin_0_66_66 41.3–55.1 s | 3.2 / 1.2 | 18 / 6 | self-collision right_hand_collision / trunk_collision 0.3 s (at 4.0 s, 8 mm) |
| `kexin_1_1_1_t274-292` | A | 24_kexin_1_1_1 274.3–291.8 s | 1.6 / 0.5 | 9 / 3 | self-collision right_hand_collision / trunk_collision 1.9 s (at 2.0 s, 12 mm) |
| `kexin_1_1_1_t292-309` | A | 24_kexin_1_1_1 291.8–309.3 s | 0.9 / 0.4 | 11 / 4 | self-collision right_hand_collision / trunk_collision 1.8 s (at 1.4 s, 9 mm) |
| `kexin_1_1_1_t360-365_shift` | B | 24_kexin_1_1_1 359.8–364.8 s | 17.3 / 8.3 | 5 / 2 | outlier knee max (z +3.8) |
| `kexin_1_2_2_t266-271_shift` | B | 24_kexin_1_2_2 266.0–271.0 s | 18.9 / 8.9 | 8 / 3 | outlier knee max (z +3.6) |
| `kexin_1_2_2_t386-405` | A | 24_kexin_1_2_2 386.0–404.8 s | 3.1 / 1.3 | 11 / 4 | self-collision right_hand_collision / trunk_collision 0.2 s (at 15.7 s, 5 mm) |
| `kexin_1_3_3_t431-436_shift` | B | 24_kexin_1_3_3 430.6–435.6 s | 17.3 / 7.4 | 5 / 3 | outlier knee max (z +4.0) |
| `kexin_1_3_3_t468-474_shift` | B | 24_kexin_1_3_3 468.0–473.7 s | 18.6 / 8.8 | 8 / 3 | outlier knee max (z +4.7) |
| `kieks_0_10_10_t0-7_shift` | B | 10_kieks_0_10_10 0.0–6.5 s | 22.5 / 12.7 | 4 / 2 | outlier knee max (z +7.8) |
| `kieks_0_11_11_t0-6_shift` | B | 10_kieks_0_11_11 0.0–5.5 s | 14.6 / 8.4 | 6 / 2 | outlier knee max (z +4.7) |
| `kieks_0_13_13_t32-49` | A | 10_kieks_0_13_13 32.4–48.6 s | 1.0 / 0.7 | 17 / 5 | elbow bend at limit 5% |
| `kieks_0_16_16_t38-57` | A | 10_kieks_0_16_16 37.8–56.7 s | 0.7 / 0.6 | 12 / 4 | elbow bend at limit 8% |
| `kieks_0_2_2_t0-17` | A | 10_kieks_0_2_2 0.0–17.2 s | 8.4 / 6.0 | 20 / 6 | outlier knee max (z +4.6) |
| `kieks_0_4_4_t17-34` | A | 10_kieks_0_4_4 17.1–34.2 s | 10.0 / 5.8 | 29 / 7 | human steps |
| `kieks_0_65_65_t21-25_shift` | B | 10_kieks_0_65_65 20.8–25.1 s | 5.6 / 4.0 | 28 / 9 | head at limit 29%; hand presses into leg 33 mm for 0.5 s (at 2.1 s) |
| `kieks_0_65_65_t23-36` | A | 10_kieks_0_65_65 23.1–36.4 s | 0.9 / 1.1 | 18 / 6 | hand presses into leg 14 mm for 0.3 s (at 0.0 s) |
| `kieks_0_65_65_t9-23` | A | 10_kieks_0_65_65 9.4–22.8 s | 2.6 / 0.7 | 20 / 7 | head at limit 6% |
| `kieks_0_73_73_t0-5_shift` | B | 10_kieks_0_73_73 0.0–4.9 s | 10.2 / 8.5 | 14 / 3 | outlier knee max (z +3.6) |
| `kieks_0_73_73_t18-34` | A | 10_kieks_0_73_73 18.5–34.1 s | 1.1 / 1.0 | 33 / 9 | head at limit 7% |
| `kieks_0_7_7_t38-58` | A | 10_kieks_0_7_7 38.5–57.8 s | 0.8 / 0.4 | 12 / 5 | elbow bend at limit 6% |
| `kieks_1_1_1_t120-127` | A | 10_kieks_1_1_1 120.2–127.1 s | 2.1 / 1.5 | 18 / 7 | leg at limit 6% |
| `kieks_1_1_1_t136-147` | A | 10_kieks_1_1_1 136.0–146.7 s | 8.0 / 13.3 | 7 / 3 | K1 feet move 13 cm |
| `kieks_1_1_1_t2-21` | A | 10_kieks_1_1_1 1.9–21.0 s | 8.9 / 4.3 | 8 / 3 | leg at limit 14% |
| `kieks_1_1_1_t200-207` | A | 10_kieks_1_1_1 200.0–207.4 s | 7.4 / 11.6 | 11 / 4 | K1 feet move 12 cm |
| `kieks_1_1_1_t218-222_shift` | B | 10_kieks_1_1_1 217.8–221.8 s | 18.8 / 10.7 | 22 / 9 | outlier knee max (z +3.5) |
| `kieks_1_1_1_t240-244_shift` | B | 10_kieks_1_1_1 239.7–243.7 s | 21.3 / 5.6 | 7 / 3 | outlier knee max (z +7.7) |
| `kieks_1_1_1_t289-297` | A | 10_kieks_1_1_1 288.9–297.4 s | 6.4 / 3.6 | 33 / 10 | leg at limit 6% |
| `kieks_1_1_1_t324-328_shift` | B | 10_kieks_1_1_1 324.4–328.4 s | 11.1 / 4.9 | 5 / 1 | outlier knee max (z +4.5) |
| `kieks_1_1_1_t370-378` | A | 10_kieks_1_1_1 370.4–378.3 s | 7.9 / 8.9 | 21 / 7 | K1 feet move 9 cm; hand presses into leg 16 mm for 0.5 s (at 0.6 s) |
| `kieks_1_1_1_t381-385_shift` | B | 10_kieks_1_1_1 380.6–385.4 s | 13.0 / 9.2 | 5 / 2 | outlier knee max (z +6.7) |
| `kieks_1_1_1_t418-424` | A | 10_kieks_1_1_1 418.5–423.8 s | 7.9 / 7.8 | 12 / 5 | leg at limit 10% |
| `kieks_1_1_1_t504-512_shift` | B | 10_kieks_1_1_1 504.3–512.3 s | 24.1 / 14.2 | 18 / 6 | outlier knee max (z +3.5) |
| `kieks_1_1_1_t51-55_shift` | B | 10_kieks_1_1_1 51.0–55.0 s | 23.1 / 6.1 | 4 / 2 | knee 61 deg; outlier knee max (z +8.2) |
| `kieks_1_1_1_t518-524` | A | 10_kieks_1_1_1 517.6–523.7 s | 8.9 / 15.1 | 17 / 5 | K1 feet move 15 cm |
| `kieks_1_1_1_t551-568` | A | 10_kieks_1_1_1 550.9–567.7 s | 6.8 / 9.0 | 6 / 3 | K1 feet move 9 cm |
| `kieks_1_1_1_t604-610_shift` | B | 10_kieks_1_1_1 604.2–609.9 s | 20.4 / 4.7 | 6 / 3 | knee 61 deg; outlier knee max (z +8.3) |
| `kieks_1_2_2_t179-184` | A | 10_kieks_1_2_2 179.2–183.9 s | 9.8 / 2.7 | 6 / 2 | outlier knee max (z +3.6) |
| `kieks_1_2_2_t202-213` | A | 10_kieks_1_2_2 201.8–212.9 s | 8.8 / 6.8 | 17 / 6 | hand presses into leg 22 mm for 0.3 s (at 0.2 s) |
| `kieks_1_2_2_t260-266` | A | 10_kieks_1_2_2 259.6–265.8 s | 8.4 / 13.1 | 20 / 7 | K1 feet move 13 cm |
| `kieks_1_2_2_t272-277_shift` | B | 10_kieks_1_2_2 272.3–276.7 s | 19.7 / 16.5 | 13 / 5 | outlier knee max (z +5.0) |
| `kieks_1_2_2_t396-400` | A | 10_kieks_1_2_2 396.5–400.5 s | 7.3 / 9.2 | 43 / 10 | K1 feet move 9 cm |
| `kieks_1_2_2_t428-434_shift` | B | 10_kieks_1_2_2 427.7–434.5 s | 22.5 / 14.7 | 20 / 5 | knee 63 deg; outlier knee max (z +9.2) |
| `kieks_1_2_2_t473-478_shift` | B | 10_kieks_1_2_2 473.2–477.5 s | 13.4 / 3.4 | 11 / 4 | outlier knee max (z +4.8) |
| `kieks_1_2_2_t53-68` | A | 10_kieks_1_2_2 53.4–67.5 s | 5.4 / 4.9 | 16 / 5 | leg at limit 7% |
| `kieks_1_2_2_t565-569` | A | 10_kieks_1_2_2 564.9–569.0 s | 5.2 / 9.0 | 21 / 6 | K1 feet move 9 cm; hand presses into leg 27 mm for 0.2 s (at 3.4 s) |
| `kieks_1_2_2_t94-107` | A | 10_kieks_1_2_2 94.1–106.8 s | 9.4 / 5.0 | 3 / 2 | leg at limit 5% |
| `kieks_1_3_3_t151-155_shift` | B | 10_kieks_1_3_3 151.3–155.3 s | 15.1 / 7.9 | 16 / 4 | outlier knee max (z +3.7) |
| `kieks_1_3_3_t170-174_shift` | B | 10_kieks_1_3_3 169.7–173.7 s | 19.6 / 11.7 | 15 / 4 | outlier knee max (z +5.6) |
| `kieks_1_3_3_t184-194` | A | 10_kieks_1_3_3 184.0–193.9 s | 5.7 / 6.5 | 26 / 10 | hand presses into leg 9 mm for 0.2 s (at 0.4 s) |
| `kieks_1_3_3_t264-274` | A | 10_kieks_1_3_3 263.5–273.7 s | 6.5 / 3.2 | 8 / 3 | hand presses into leg 37 mm for 1.1 s (at 0.7 s) |
| `kieks_1_3_3_t291-300` | A | 10_kieks_1_3_3 290.6–300.5 s | 10.0 / 9.0 | 3 / 1 | K1 feet move 9 cm |
| `kieks_1_3_3_t326-330` | A | 10_kieks_1_3_3 326.3–330.3 s | 6.9 / 9.7 | 11 / 3 | K1 feet move 10 cm |
| `kieks_1_3_3_t379-393` | A | 10_kieks_1_3_3 379.0–393.0 s | 8.6 / 11.4 | 10 / 4 | K1 feet move 11 cm; hand presses into leg 22 mm for 0.2 s (at 13.4 s) |
| `kieks_1_3_3_t436-440_shift` | B | 10_kieks_1_3_3 435.7–439.8 s | 11.7 / 11.8 | 42 / 12 | elbow bend at limit 11% |
| `kieks_1_3_3_t465-469_shift` | B | 10_kieks_1_3_3 464.7–468.7 s | 10.6 / 8.2 | 23 / 7 | leg at limit 29% |
| `kieks_1_3_3_t466-476` | A | 10_kieks_1_3_3 465.6–475.5 s | 5.7 / 4.2 | 28 / 8 | leg at limit 8% |
| `kieks_1_3_3_t592-600` | A | 10_kieks_1_3_3 591.9–600.5 s | 2.7 / 1.2 | 4 / 1 | leg at limit 12% |
| `kieks_1_3_3_t99-104` | A | 10_kieks_1_3_3 98.9–103.9 s | 5.5 / 8.3 | 7 / 2 | K1 feet move 8 cm |
| `lawrence_0_100_100_t16-20_shift` | B | 4_lawrence_0_100_100 16.5–20.5 s | 26.2 / 16.0 | 45 / 14 | human steps |
| `lawrence_0_100_100_t4-14_shift` | B | 4_lawrence_0_100_100 3.9–13.7 s | 13.1 / 7.8 | 69 / 20 | outlier arms k1 cm (z +3.7); outlier knee max (z +4.1) |
| `lawrence_0_100_100_t47-56` | A | 4_lawrence_0_100_100 47.3–56.1 s | 5.9 / 4.8 | 59 / 18 | outlier knee max (z +6.5) |
| `lawrence_0_101_101_t13-21` | A | 4_lawrence_0_101_101 13.4–21.2 s | 4.4 / 2.5 | 32 / 14 | outlier knee max (z +3.9) |
| `lawrence_0_101_101_t26-31_shift` | B | 4_lawrence_0_101_101 26.3–31.2 s | 7.9 / 4.4 | 29 / 13 | outlier knee max (z +4.1) |
| `lawrence_0_101_101_t6-13_shift` | B | 4_lawrence_0_101_101 6.4–13.0 s | 21.4 / 11.8 | 32 / 11 | outlier knee max (z +5.3) |
| `lawrence_0_101_101_t65-82_shift` | B | 4_lawrence_0_101_101 65.5–82.0 s | 15.6 / 8.5 | 38 / 12 | outlier knee max (z +4.2) |
| `lawrence_0_102_102_t12-16_shift` | B | 4_lawrence_0_102_102 11.8–16.4 s | 9.5 / 4.4 | 26 / 11 | outlier knee max (z +4.1) |
| `lawrence_0_102_102_t18-23_shift` | B | 4_lawrence_0_102_102 18.1–22.7 s | 13.9 / 8.5 | 39 / 17 | outlier knee max (z +3.5) |
| `lawrence_0_102_102_t25-29_shift` | B | 4_lawrence_0_102_102 25.0–29.5 s | 11.8 / 7.6 | 36 / 12 | outlier knee max (z +4.1) |
| `lawrence_0_102_102_t71-76` | A | 4_lawrence_0_102_102 71.4–75.7 s | 3.7 / 2.3 | 48 / 14 | head at limit 6% |
| `lawrence_0_102_102_t74-78_shift` | B | 4_lawrence_0_102_102 73.7–77.8 s | 18.3 / 10.5 | 63 / 14 | head at limit 6% |
| `lawrence_0_103_103_t22-27_shift` | B | 4_lawrence_0_103_103 22.5–26.8 s | 10.6 / 7.2 | 20 / 8 | outlier knee max (z +5.8) |
| `lawrence_0_103_103_t32-36_shift` | B | 4_lawrence_0_103_103 31.6–35.9 s | 8.5 / 4.8 | 20 / 6 | outlier knee max (z +5.8) |
| `lawrence_0_103_103_t39-48_shift` | B | 4_lawrence_0_103_103 39.0–48.2 s | 24.2 / 14.8 | 31 / 9 | outlier trunk drop (z +3.5); outlier knee max (z +6.5) |
| `lawrence_0_103_103_t63-78_shift` | B | 4_lawrence_0_103_103 63.1–78.2 s | 17.9 / 9.3 | 27 / 11 | outlier knee max (z +5.8) |
| `lawrence_0_104_104_t43-50_shift` | B | 4_lawrence_0_104_104 42.9–49.7 s | 21.9 / 13.4 | 30 / 11 | outlier knee max (z +5.6) |
| `lawrence_0_104_104_t52-63_shift` | B | 4_lawrence_0_104_104 52.3–63.4 s | 13.1 / 8.2 | 37 / 11 | outlier knee max (z +4.9) |
| `lawrence_0_105_105_t0-7_shift` | B | 4_lawrence_0_105_105 0.0–7.3 s | 16.0 / 9.5 | 23 / 8 | outlier knee max (z +5.1) |
| `lawrence_0_105_105_t16-22_shift` | B | 4_lawrence_0_105_105 15.9–22.0 s | 14.1 / 7.0 | 40 / 14 | outlier knee max (z +5.3) |
| `lawrence_0_105_105_t30-39_shift` | B | 4_lawrence_0_105_105 30.0–38.9 s | 20.1 / 12.2 | 41 / 11 | outlier knee max (z +4.6) |
| `lawrence_0_105_105_t9-15_shift` | B | 4_lawrence_0_105_105 9.0–15.1 s | 18.2 / 10.1 | 53 / 13 | outlier knee max (z +4.3) |
| `lawrence_0_107_107_t15-25_shift` | B | 4_lawrence_0_107_107 15.1–24.8 s | 16.4 / 9.2 | 22 / 10 | outlier knee max (z +6.6) |
| `lawrence_0_107_107_t43-56_shift` | B | 4_lawrence_0_107_107 43.4–55.8 s | 20.8 / 13.5 | 31 / 9 | outlier knee max (z +5.6) |
| `lawrence_0_108_108_t11-20` | A | 4_lawrence_0_108_108 10.8–20.0 s | 5.3 / 3.0 | 74 / 20 | outlier arms k1 cm (z +3.7) |
| `lawrence_0_108_108_t18-23_shift` | B | 4_lawrence_0_108_108 18.0–22.5 s | 8.1 / 5.1 | 80 / 23 | outlier arms k1 cm (z +4.5) |
| `lawrence_0_108_108_t37-43_shift` | B | 4_lawrence_0_108_108 36.6–43.1 s | 29.1 / 16.3 | 33 / 9 | human steps; outlier knee max (z +5.9) |
| `lawrence_0_108_108_t44-60_shift` | B | 4_lawrence_0_108_108 43.9–59.7 s | 17.9 / 10.7 | 34 / 10 | outlier knee max (z +3.8) |
| `lawrence_0_109_109_t52-57_shift` | B | 4_lawrence_0_109_109 52.0–57.2 s | 23.5 / 14.0 | 70 / 22 | outlier arms k1 cm (z +4.1) |
| `lawrence_0_10_10_t17-30_shift` | B | 4_lawrence_0_10_10 17.0–30.1 s | 23.1 / 13.2 | 28 / 11 | outlier knee max (z +6.3) |
| `lawrence_0_10_10_t31-38_shift` | B | 4_lawrence_0_10_10 31.0–38.5 s | 26.5 / 15.2 | 36 / 12 | human steps; outlier knee max (z +5.7) |
| `lawrence_0_10_10_t36-42` | A | 4_lawrence_0_10_10 36.5–42.2 s | 8.0 / 5.3 | 38 / 13 | shoulder at limit 12% |
| `lawrence_0_10_10_t40-45_shift` | B | 4_lawrence_0_10_10 40.2–44.7 s | 8.5 / 4.9 | 32 / 12 | shoulder at limit 16%; outlier knee max (z +3.6) |
| `lawrence_0_10_10_t43-51` | A | 4_lawrence_0_10_10 42.7–51.3 s | 5.4 / 3.6 | 41 / 17 | outlier trunk drop (z +3.6) |
| `lawrence_0_10_10_t49-57_shift` | B | 4_lawrence_0_10_10 49.3–56.6 s | 28.7 / 15.3 | 36 / 13 | human steps; outlier knee max (z +6.0) |
| `lawrence_0_10_10_t7-15_shift` | B | 4_lawrence_0_10_10 7.1–14.9 s | 17.1 / 10.3 | 35 / 14 | outlier knee max (z +5.8) |
| `lawrence_0_110_110_t19-23_shift` | B | 4_lawrence_0_110_110 18.8–23.3 s | 11.4 / 6.6 | 26 / 7 | outlier knee max (z +4.5) |
| `lawrence_0_110_110_t21-26` | A | 4_lawrence_0_110_110 21.3–26.2 s | 1.8 / 1.1 | 22 / 7 | outlier knee max (z +4.1) |
| `lawrence_0_110_110_t24-38_shift` | B | 4_lawrence_0_110_110 24.2–37.8 s | 13.0 / 7.1 | 35 / 11 | outlier knee max (z +4.2) |
| `lawrence_0_110_110_t6-18_shift` | B | 4_lawrence_0_110_110 6.5–17.5 s | 21.2 / 11.7 | 28 / 9 | outlier knee max (z +5.1) |
| `lawrence_0_111_111_t0-6_shift` | B | 4_lawrence_0_111_111 0.0–5.9 s | 17.7 / 9.6 | 36 / 9 | outlier knee max (z +5.6) |
| `lawrence_0_111_111_t36-43_shift` | B | 4_lawrence_0_111_111 36.3–43.0 s | 22.4 / 15.4 | 36 / 10 | outlier knee max (z +4.3) |
| `lawrence_0_111_111_t50-56_shift` | B | 4_lawrence_0_111_111 49.6–56.2 s | 23.0 / 14.3 | 42 / 13 | outlier knee max (z +3.6) |
| `lawrence_0_111_111_t59-66_shift` | B | 4_lawrence_0_111_111 59.3–66.0 s | 20.1 / 11.1 | 54 / 17 | outlier knee max (z +3.6) |
| `lawrence_0_111_111_t8-13_shift` | B | 4_lawrence_0_111_111 7.6–13.2 s | 20.1 / 11.7 | 29 / 8 | outlier knee max (z +6.0) |
| `lawrence_0_112_112_t0-6_shift` | B | 4_lawrence_0_112_112 0.0–6.4 s | 23.1 / 12.8 | 37 / 10 | outlier knee max (z +4.7) |
| `lawrence_0_112_112_t37-41_shift` | B | 4_lawrence_0_112_112 36.6–41.2 s | 23.3 / 15.5 | 49 / 14 | outlier knee max (z +6.3) |
| `lawrence_0_112_112_t41-54_shift` | B | 4_lawrence_0_112_112 41.3–54.2 s | 23.9 / 14.2 | 49 / 13 | outlier knee max (z +4.4) |
| `lawrence_0_112_112_t62-69_shift` | B | 4_lawrence_0_112_112 61.5–68.8 s | 15.9 / 8.9 | 37 / 10 | outlier knee max (z +4.3) |
| `lawrence_0_113_113_t38-43_shift` | B | 4_lawrence_0_113_113 38.1–42.6 s | 12.0 / 6.9 | 50 / 18 | outlier knee max (z +4.2) |
| `lawrence_0_114_114_t11-18_shift` | B | 4_lawrence_0_114_114 11.0–18.1 s | 20.8 / 11.8 | 42 / 11 | outlier knee max (z +4.5) |
| `lawrence_0_114_114_t37-41_shift` | B | 4_lawrence_0_114_114 37.0–41.0 s | 25.0 / 14.5 | 39 / 10 | human steps; outlier knee max (z +3.8) |
| `lawrence_0_114_114_t50-57_shift` | B | 4_lawrence_0_114_114 50.5–56.5 s | 20.5 / 10.2 | 51 / 15 | outlier knee max (z +6.3) |
| `lawrence_0_114_114_t59-68_shift` | B | 4_lawrence_0_114_114 59.3–68.1 s | 16.0 / 8.9 | 50 / 15 | outlier knee max (z +5.4) |
| `lawrence_0_115_115_t17-21_shift` | B | 4_lawrence_0_115_115 17.0–21.0 s | 24.6 / 15.0 | 41 / 11 | outlier knee max (z +4.6) |
| `lawrence_0_115_115_t53-60_shift` | B | 4_lawrence_0_115_115 52.6–60.0 s | 13.8 / 7.1 | 47 / 12 | outlier knee max (z +3.8) |
| `lawrence_0_116_116_t24-31_shift` | B | 4_lawrence_0_116_116 24.0–31.3 s | 18.6 / 10.8 | 41 / 12 | outlier knee max (z +4.5) |
| `lawrence_0_117_117_t0-5_shift` | B | 4_lawrence_0_117_117 0.4–5.1 s | 24.6 / 13.7 | 34 / 10 | outlier knee max (z +4.0) |
| `lawrence_0_117_117_t22-28_shift` | B | 4_lawrence_0_117_117 21.6–28.1 s | 18.5 / 12.1 | 63 / 16 | outlier knee max (z +4.8) |
| `lawrence_0_117_117_t5-20_shift` | B | 4_lawrence_0_117_117 5.1–19.8 s | 22.7 / 12.5 | 46 / 13 | outlier knee max (z +5.5) |
| `lawrence_0_118_118_t14-24_shift` | B | 4_lawrence_0_118_118 13.9–23.8 s | 16.7 / 9.8 | 50 / 13 | outlier knee max (z +4.9) |
| `lawrence_0_11_11_t26-35_shift` | B | 4_lawrence_0_11_11 26.3–35.1 s | 26.9 / 14.2 | 29 / 12 | human steps; outlier knee max (z +6.4) |
| `lawrence_0_11_11_t52-59_shift` | B | 4_lawrence_0_11_11 52.3–59.3 s | 20.4 / 11.8 | 47 / 14 | outlier knee max (z +5.6) |
| `lawrence_0_11_11_t57-69` | A | 4_lawrence_0_11_11 57.3–69.1 s | 9.3 / 5.5 | 33 / 9 | outlier knee max (z +3.6) |
| `lawrence_0_11_11_t6-10_shift` | B | 4_lawrence_0_11_11 5.8–10.1 s | 18.8 / 10.0 | 32 / 14 | outlier knee max (z +4.9) |
| `lawrence_0_12_12_t23-28_shift` | B | 4_lawrence_0_12_12 22.8–28.1 s | 20.7 / 11.6 | 38 / 13 | outlier knee max (z +4.0) |
| `lawrence_0_12_12_t26-38` | A | 4_lawrence_0_12_12 26.1–37.7 s | 1.5 / 0.7 | 31 / 11 | shoulder at limit 12% |
| `lawrence_0_12_12_t39-47_shift` | B | 4_lawrence_0_12_12 38.6–47.3 s | 23.6 / 15.3 | 46 / 18 | outlier knee max (z +6.3) |
| `lawrence_0_12_12_t51-65_shift` | B | 4_lawrence_0_12_12 50.6–65.4 s | 24.9 / 12.5 | 41 / 15 | outlier trunk drop (z +4.3); outlier knee max (z +4.6) |
| `lawrence_0_12_12_t65-72_shift` | B | 4_lawrence_0_12_12 65.4–71.7 s | 24.7 / 12.7 | 44 / 18 | outlier knee max (z +5.8) |
| `lawrence_0_12_12_t70-74` | A | 4_lawrence_0_12_12 69.7–74.1 s | 5.2 / 1.3 | 45 / 15 | shoulder at limit 8%; outlier trunk drop (z +3.9); outlier knee max (z +3.7) |
| `lawrence_0_13_13_t0-4_shift` | B | 4_lawrence_0_13_13 0.0–4.2 s | 19.7 / 10.8 | 35 / 11 | outlier knee max (z +4.0) |
| `lawrence_0_13_13_t2-8` | A | 4_lawrence_0_13_13 2.2–8.5 s | 3.3 / 2.3 | 33 / 12 | outlier trunk drop (z +3.8); outlier knee max (z +4.6) |
| `lawrence_0_13_13_t30-35_shift` | B | 4_lawrence_0_13_13 30.4–35.0 s | 8.8 / 5.9 | 39 / 15 | outlier knee max (z +5.2) |
| `lawrence_0_13_13_t33-38` | A | 4_lawrence_0_13_13 33.0–38.4 s | 9.7 / 4.7 | 32 / 14 | outlier knee max (z +3.6) |
| `lawrence_0_13_13_t36-41_shift` | B | 4_lawrence_0_13_13 36.4–41.0 s | 23.0 / 14.7 | 30 / 11 | outlier knee max (z +6.2) |
| `lawrence_0_13_13_t6-17_shift` | B | 4_lawrence_0_13_13 6.5–16.9 s | 13.3 / 7.6 | 34 / 13 | outlier trunk drop (z +4.0); outlier knee max (z +4.6) |
| `lawrence_0_13_13_t61-65_shift` | B | 4_lawrence_0_13_13 60.8–65.4 s | 15.8 / 8.8 | 48 / 19 | outlier knee max (z +4.0) |
| `lawrence_0_13_13_t70-74_shift` | B | 4_lawrence_0_13_13 69.9–74.4 s | 15.4 / 9.6 | 39 / 11 | outlier knee max (z +6.0) |
| `lawrence_0_13_13_t76-81_shift` | B | 4_lawrence_0_13_13 75.9–80.8 s | 21.7 / 12.7 | 30 / 13 | outlier knee max (z +5.3) |
| `lawrence_0_14_14_t31-37_shift` | B | 4_lawrence_0_14_14 31.1–36.6 s | 14.9 / 8.7 | 32 / 10 | outlier knee max (z +4.5) |
| `lawrence_0_14_14_t35-39` | A | 4_lawrence_0_14_14 34.6–39.3 s | 3.1 / 1.2 | 34 / 10 | outlier knee max (z +4.8) |
| `lawrence_0_14_14_t76-81_shift` | B | 4_lawrence_0_14_14 76.5–80.9 s | 9.0 / 5.1 | 24 / 10 | outlier knee max (z +4.6) |
| `lawrence_0_14_14_t79-86` | A | 4_lawrence_0_14_14 78.9–86.1 s | 5.6 / 1.4 | 29 / 12 | outlier knee max (z +4.3) |
| `lawrence_0_15_15_t0-6_shift` | B | 4_lawrence_0_15_15 0.0–6.2 s | 21.9 / 12.4 | 22 / 9 | outlier knee max (z +5.6) |
| `lawrence_0_15_15_t23-28_shift` | B | 4_lawrence_0_15_15 23.3–27.8 s | 17.6 / 11.4 | 30 / 11 | outlier knee max (z +5.8) |
| `lawrence_0_15_15_t35-40_shift` | B | 4_lawrence_0_15_15 35.1–39.7 s | 14.1 / 7.4 | 26 / 10 | outlier knee max (z +6.7) |
| `lawrence_0_15_15_t43-52_shift` | B | 4_lawrence_0_15_15 43.1–52.1 s | 19.6 / 11.1 | 23 / 10 | outlier knee max (z +4.9) |
| `lawrence_0_15_15_t58-62_shift` | B | 4_lawrence_0_15_15 57.9–62.2 s | 5.5 / 3.2 | 27 / 9 | shoulder at limit 35% |
| `lawrence_0_15_15_t60-76` | A | 4_lawrence_0_15_15 60.2–75.6 s | 4.0 / 2.5 | 33 / 11 | shoulder at limit 15% |
| `lawrence_0_15_15_t74-78_shift` | B | 4_lawrence_0_15_15 73.6–78.1 s | 13.5 / 7.8 | 50 / 13 | outlier knee max (z +4.8) |
| `lawrence_0_15_15_t82-87_shift` | B | 4_lawrence_0_15_15 82.1–86.6 s | 17.0 / 10.5 | 26 / 10 | outlier knee max (z +3.5) |
| `lawrence_0_15_15_t9-20_shift` | B | 4_lawrence_0_15_15 9.2–20.2 s | 13.6 / 7.9 | 32 / 14 | outlier knee max (z +6.0) |
| `lawrence_0_16_16_t18-23_shift` | B | 4_lawrence_0_16_16 17.6–23.1 s | 17.8 / 9.5 | 36 / 12 | outlier knee max (z +3.6) |
| `lawrence_0_16_16_t44-48_shift` | B | 4_lawrence_0_16_16 43.8–48.3 s | 11.0 / 6.8 | 43 / 12 | outlier knee max (z +4.3) |
| `lawrence_0_16_16_t51-55_shift` | B | 4_lawrence_0_16_16 50.6–54.6 s | 29.0 / 16.5 | 40 / 13 | human steps; outlier knee max (z +6.3) |
| `lawrence_0_16_16_t88-96_shift` | B | 4_lawrence_0_16_16 87.8–95.8 s | 23.9 / 13.0 | 23 / 8 | outlier knee max (z +5.1) |
| `lawrence_0_17_17_t0-6_shift` | B | 4_lawrence_0_17_17 0.0–5.7 s | 24.7 / 13.6 | 42 / 14 | outlier knee max (z +7.6) |
| `lawrence_0_17_17_t13-22_shift` | B | 4_lawrence_0_17_17 12.9–21.6 s | 22.2 / 12.0 | 33 / 14 | outlier knee max (z +4.8) |
| `lawrence_0_17_17_t20-29` | A | 4_lawrence_0_17_17 19.6–29.3 s | 9.9 / 5.6 | 26 / 9 | outlier trunk drop (z +3.7); outlier knee max (z +4.2) |
| `lawrence_0_17_17_t7-11_shift` | B | 4_lawrence_0_17_17 6.7–10.7 s | 22.2 / 12.3 | 21 / 11 | outlier knee max (z +5.2) |
| `lawrence_0_18_18_t0-9_shift` | B | 4_lawrence_0_18_18 0.0–8.9 s | 19.5 / 11.2 | 37 / 13 | outlier knee max (z +6.8) |
| `lawrence_0_18_18_t24-29_shift` | B | 4_lawrence_0_18_18 24.2–28.7 s | 13.4 / 8.5 | 46 / 16 | outlier knee max (z +4.6) |
| `lawrence_0_18_18_t27-31` | A | 4_lawrence_0_18_18 26.7–31.4 s | 0.7 / 0.3 | 27 / 11 | shoulder at limit 13% |
| `lawrence_0_18_18_t29-36_shift` | B | 4_lawrence_0_18_18 29.4–35.9 s | 26.3 / 14.0 | 27 / 11 | human steps; outlier knee max (z +5.0) |
| `lawrence_0_18_18_t63-67_shift` | B | 4_lawrence_0_18_18 62.7–66.7 s | 21.9 / 12.5 | 25 / 10 | outlier knee max (z +6.0) |
| `lawrence_0_18_18_t7-18` | A | 4_lawrence_0_18_18 6.9–17.7 s | 10.0 / 6.0 | 28 / 10 | outlier knee max (z +4.4) |
| `lawrence_0_19_19_t24-28_shift` | B | 4_lawrence_0_19_19 23.9–28.3 s | 11.3 / 6.9 | 25 / 9 | outlier knee max (z +5.1) |
| `lawrence_0_19_19_t30-34_shift` | B | 4_lawrence_0_19_19 29.5–34.1 s | 17.1 / 10.7 | 32 / 11 | outlier knee max (z +5.9) |
| `lawrence_0_19_19_t36-41_shift` | B | 4_lawrence_0_19_19 36.5–41.0 s | 14.9 / 9.0 | 38 / 11 | outlier knee max (z +4.6) |
| `lawrence_0_19_19_t4-12_shift` | B | 4_lawrence_0_19_19 4.0–11.7 s | 20.7 / 12.4 | 40 / 15 | outlier knee max (z +4.3) |
| `lawrence_0_19_19_t52-57_shift` | B | 4_lawrence_0_19_19 52.1–56.6 s | 15.8 / 9.4 | 28 / 11 | outlier knee max (z +5.3) |
| `lawrence_0_1_1_t18-35_shift` | B | 4_lawrence_0_1_1 17.8–34.8 s | 20.2 / 10.1 | 26 / 10 | outlier knee max (z +7.1) |
| `lawrence_0_1_1_t43-49` | A | 4_lawrence_0_1_1 42.7–48.9 s | 4.9 / 1.9 | 26 / 11 | outlier trunk drop (z +3.7); outlier knee max (z +6.8) |
| `lawrence_0_1_1_t47-51_shift` | B | 4_lawrence_0_1_1 46.7–50.7 s | 24.2 / 13.6 | 31 / 12 | outlier trunk drop (z +3.7); outlier knee max (z +6.3) |
| `lawrence_0_1_1_t51-55_shift` | B | 4_lawrence_0_1_1 50.7–54.8 s | 24.8 / 13.9 | 26 / 13 | outlier knee max (z +5.6) |
| `lawrence_0_1_1_t55-61_shift` | B | 4_lawrence_0_1_1 54.8–60.6 s | 23.8 / 13.5 | 26 / 11 | outlier knee max (z +5.7) |
| `lawrence_0_1_1_t61-66_shift` | B | 4_lawrence_0_1_1 61.1–65.6 s | 13.7 / 8.1 | 26 / 10 | outlier knee max (z +5.7) |
| `lawrence_0_1_1_t69-73_shift` | B | 4_lawrence_0_1_1 69.2–73.4 s | 21.6 / 13.1 | 26 / 10 | outlier knee max (z +5.6) |
| `lawrence_0_20_20_t10-15_shift` | B | 4_lawrence_0_20_20 9.9–15.2 s | 23.1 / 12.3 | 30 / 10 | outlier knee max (z +4.5) |
| `lawrence_0_20_20_t28-42` | A | 4_lawrence_0_20_20 27.7–41.5 s | 7.7 / 4.3 | 26 / 10 | outlier knee max (z +4.9) |
| `lawrence_0_20_20_t40-44_shift` | B | 4_lawrence_0_20_20 39.5–44.2 s | 19.3 / 11.4 | 21 / 8 | outlier knee max (z +5.3) |
| `lawrence_0_20_20_t47-52_shift` | B | 4_lawrence_0_20_20 46.8–51.6 s | 20.6 / 13.2 | 42 / 12 | outlier knee max (z +4.6) |
| `lawrence_0_20_20_t53-57_shift` | B | 4_lawrence_0_20_20 52.6–57.0 s | 9.7 / 6.1 | 32 / 13 | outlier knee max (z +5.1) |
| `lawrence_0_20_20_t59-63_shift` | B | 4_lawrence_0_20_20 58.9–63.5 s | 12.1 / 7.7 | 34 / 14 | outlier knee max (z +4.2) |
| `lawrence_0_20_20_t64-70_shift` | B | 4_lawrence_0_20_20 63.9–70.5 s | 19.8 / 11.2 | 41 / 15 | outlier knee max (z +5.8) |
| `lawrence_0_21_21_t37-42_shift` | B | 4_lawrence_0_21_21 37.3–41.8 s | 12.9 / 7.4 | 29 / 10 | outlier knee max (z +5.4) |
| `lawrence_0_21_21_t54-63_shift` | B | 4_lawrence_0_21_21 54.2–63.3 s | 22.5 / 14.0 | 36 / 13 | outlier knee max (z +6.5) |
| `lawrence_0_21_21_t67-71_shift` | B | 4_lawrence_0_21_21 66.6–71.2 s | 19.1 / 11.5 | 41 / 13 | outlier knee max (z +6.2) |
| `lawrence_0_21_21_t7-27` | A | 4_lawrence_0_21_21 7.2–26.8 s | 9.9 / 5.8 | 29 / 12 | outlier trunk drop (z +4.1) |
| `lawrence_0_22_22_t10-16_shift` | B | 4_lawrence_0_22_22 10.1–16.1 s | 19.4 / 10.7 | 20 / 8 | outlier knee max (z +5.2) |
| `lawrence_0_22_22_t17-22_shift` | B | 4_lawrence_0_22_22 17.5–22.0 s | 11.2 / 7.7 | 25 / 10 | outlier knee max (z +3.7) |
| `lawrence_0_22_22_t24-28_shift` | B | 4_lawrence_0_22_22 23.6–28.1 s | 15.7 / 9.4 | 32 / 12 | outlier knee max (z +6.6) |
| `lawrence_0_22_22_t64-69_shift` | B | 4_lawrence_0_22_22 64.2–68.7 s | 14.4 / 8.8 | 33 / 13 | outlier knee max (z +5.9) |
| `lawrence_0_23_23_t20-24_shift` | B | 4_lawrence_0_23_23 19.8–24.3 s | 13.5 / 7.9 | 20 / 9 | outlier knee max (z +5.9) |
| `lawrence_0_23_23_t26-31_shift` | B | 4_lawrence_0_23_23 26.5–31.1 s | 13.8 / 8.3 | 23 / 9 | outlier knee max (z +6.0) |
| `lawrence_0_23_23_t5-10_shift` | B | 4_lawrence_0_23_23 5.2–9.7 s | 10.5 / 7.5 | 21 / 9 | outlier knee max (z +4.9) |
| `lawrence_0_24_24_t0-11_shift` | B | 4_lawrence_0_24_24 0.0–10.6 s | 24.8 / 14.2 | 36 / 12 | outlier knee max (z +7.0); hand presses into leg 15 mm for 0.2 s (at 5.4 s) |
| `lawrence_0_24_24_t29-37_shift` | B | 4_lawrence_0_24_24 28.8–36.6 s | 21.4 / 12.1 | 31 / 13 | outlier knee max (z +4.8) |
| `lawrence_0_24_24_t37-43_shift` | B | 4_lawrence_0_24_24 36.7–43.2 s | 17.8 / 10.5 | 21 / 10 | outlier knee max (z +6.9) |
| `lawrence_0_24_24_t60-72_shift` | B | 4_lawrence_0_24_24 59.9–72.2 s | 20.7 / 11.0 | 30 / 11 | outlier knee max (z +6.8) |
| `lawrence_0_24_24_t81-85_shift` | B | 4_lawrence_0_24_24 80.6–85.2 s | 17.1 / 10.9 | 28 / 11 | outlier knee max (z +4.9) |
| `lawrence_0_24_24_t85-90_shift` | B | 4_lawrence_0_24_24 85.3–89.8 s | 16.3 / 10.6 | 27 / 10 | outlier knee max (z +5.3) |
| `lawrence_0_24_24_t91-96_shift` | B | 4_lawrence_0_24_24 91.0–96.4 s | 22.4 / 11.9 | 27 / 10 | outlier knee max (z +5.6) |
| `lawrence_0_25_25_t0-9_shift` | B | 4_lawrence_0_25_25 0.0–9.1 s | 18.2 / 10.1 | 29 / 10 | outlier knee max (z +4.2) |
| `lawrence_0_25_25_t35-42_shift` | B | 4_lawrence_0_25_25 34.9–42.5 s | 14.6 / 8.0 | 39 / 15 | outlier knee max (z +4.0) |
| `lawrence_0_25_25_t45-49_shift` | B | 4_lawrence_0_25_25 44.9–49.5 s | 18.5 / 11.8 | 29 / 9 | outlier knee max (z +7.9) |
| `lawrence_0_25_25_t51-56_shift` | B | 4_lawrence_0_25_25 50.7–56.4 s | 22.3 / 12.1 | 22 / 9 | outlier knee max (z +6.8) |
| `lawrence_0_25_25_t67-71_shift` | B | 4_lawrence_0_25_25 66.9–71.5 s | 16.8 / 9.0 | 28 / 10 | outlier knee max (z +6.5) |
| `lawrence_0_25_25_t74-82_shift` | B | 4_lawrence_0_25_25 73.6–82.4 s | 30.0 / 16.5 | 38 / 14 | human steps; outlier knee max (z +6.9) |
| `lawrence_0_26_26_t17-26_shift` | B | 4_lawrence_0_26_26 17.2–25.7 s | 21.1 / 12.2 | 31 / 14 | outlier knee max (z +7.1) |
| `lawrence_0_26_26_t75-81_shift` | B | 4_lawrence_0_26_26 74.8–81.2 s | 20.3 / 12.2 | 38 / 11 | outlier knee max (z +4.3) |
| `lawrence_0_27_27_t16-28_shift` | B | 4_lawrence_0_27_27 15.8–28.5 s | 13.0 / 6.7 | 45 / 13 | outlier knee max (z +4.2) |
| `lawrence_0_27_27_t5-11_shift` | B | 4_lawrence_0_27_27 5.0–11.1 s | 18.0 / 10.8 | 46 / 16 | outlier knee max (z +6.4) |
| `lawrence_0_27_27_t58-62_shift` | B | 4_lawrence_0_27_27 58.2–62.2 s | 23.6 / 14.4 | 22 / 9 | outlier knee max (z +4.6) |
| `lawrence_0_28_28_t20-24_shift` | B | 4_lawrence_0_28_28 19.5–23.9 s | 9.8 / 6.5 | 24 / 9 | outlier knee max (z +4.4) |
| `lawrence_0_28_28_t31-36_shift` | B | 4_lawrence_0_28_28 31.1–35.7 s | 16.6 / 10.3 | 36 / 13 | outlier knee max (z +5.7) |
| `lawrence_0_28_28_t67-72_shift` | B | 4_lawrence_0_28_28 66.9–71.5 s | 17.4 / 12.1 | 35 / 12 | outlier knee max (z +4.4) |
| `lawrence_0_29_29_t28-40` | A | 4_lawrence_0_29_29 27.9–40.0 s | 6.6 / 3.8 | 31 / 12 | shoulder at limit 10% |
| `lawrence_0_29_29_t38-48_shift` | B | 4_lawrence_0_29_29 38.0–47.8 s | 15.3 / 9.3 | 44 / 18 | outlier knee max (z +5.0) |
| `lawrence_0_29_29_t52-58` | A | 4_lawrence_0_29_29 51.5–57.7 s | 9.0 / 1.9 | 30 / 10 | outlier knee max (z +4.2) |
| `lawrence_0_29_29_t56-60_shift` | B | 4_lawrence_0_29_29 55.7–60.1 s | 10.6 / 5.0 | 18 / 7 | outlier knee max (z +4.2) |
| `lawrence_0_29_29_t68-74_shift` | B | 4_lawrence_0_29_29 68.2–73.6 s | 23.0 / 12.3 | 21 / 7 | outlier knee max (z +4.9) |
| `lawrence_0_29_29_t77-81_shift` | B | 4_lawrence_0_29_29 76.8–80.8 s | 27.1 / 15.5 | 14 / 6 | human steps |
| `lawrence_0_2_2_t0-11_shift` | B | 4_lawrence_0_2_2 0.0–11.3 s | 18.5 / 10.8 | 26 / 10 | outlier knee max (z +7.0) |
| `lawrence_0_2_2_t12-16_shift` | B | 4_lawrence_0_2_2 11.9–16.3 s | 8.8 / 4.4 | 14 / 7 | outlier knee max (z +3.5) |
| `lawrence_0_2_2_t22-27_shift` | B | 4_lawrence_0_2_2 22.2–26.7 s | 11.5 / 6.6 | 26 / 12 | outlier knee max (z +4.0) |
| `lawrence_0_2_2_t46-53_shift` | B | 4_lawrence_0_2_2 46.4–52.9 s | 22.3 / 12.4 | 30 / 10 | outlier knee max (z +4.3) |
| `lawrence_0_2_2_t61-66_shift` | B | 4_lawrence_0_2_2 61.3–65.7 s | 14.9 / 8.7 | 35 / 12 | outlier knee max (z +5.8) |
| `lawrence_0_2_2_t67-74_shift` | B | 4_lawrence_0_2_2 67.4–74.4 s | 21.9 / 11.9 | 33 / 12 | outlier knee max (z +5.6) |
| `lawrence_0_2_2_t77-82_shift` | B | 4_lawrence_0_2_2 77.4–81.8 s | 16.8 / 11.0 | 22 / 6 | outlier knee max (z +4.9) |
| `lawrence_0_30_30_t14-21_shift` | B | 4_lawrence_0_30_30 13.7–21.1 s | 22.1 / 11.9 | 38 / 14 | outlier knee max (z +6.4) |
| `lawrence_0_30_30_t58-67_shift` | B | 4_lawrence_0_30_30 58.2–66.8 s | 23.5 / 12.6 | 25 / 8 | outlier knee max (z +6.4) |
| `lawrence_0_31_31_t35-42_shift` | B | 4_lawrence_0_31_31 35.0–42.2 s | 14.8 / 8.5 | 30 / 11 | outlier knee max (z +4.2) |
| `lawrence_0_31_31_t53-58_shift` | B | 4_lawrence_0_31_31 52.7–58.3 s | 27.1 / 15.4 | 27 / 12 | human steps; outlier knee max (z +4.0) |
| `lawrence_0_31_31_t68-75_shift` | B | 4_lawrence_0_31_31 68.0–74.6 s | 20.7 / 12.0 | 33 / 13 | outlier knee max (z +4.9) |
| `lawrence_0_31_31_t9-16_shift` | B | 4_lawrence_0_31_31 8.7–15.8 s | 23.1 / 12.4 | 26 / 12 | outlier knee max (z +4.4) |
| `lawrence_0_32_32_t34-41_shift` | B | 4_lawrence_0_32_32 34.1–41.1 s | 22.1 / 13.7 | 45 / 15 | outlier knee max (z +6.6) |
| `lawrence_0_33_33_t20-24_shift` | B | 4_lawrence_0_33_33 20.0–24.4 s | 20.3 / 12.6 | 48 / 17 | outlier knee max (z +3.6) |
| `lawrence_0_33_33_t39-44_shift` | B | 4_lawrence_0_33_33 39.0–44.3 s | 26.3 / 16.1 | 11 / 5 | human steps; outlier knee max (z +5.2) |
| `lawrence_0_33_33_t59-63_shift` | B | 4_lawrence_0_33_33 58.7–63.1 s | 13.0 / 7.6 | 20 / 9 | outlier knee max (z +4.7) |
| `lawrence_0_34_34_t54-58_shift` | B | 4_lawrence_0_34_34 53.9–58.3 s | 14.0 / 7.7 | 30 / 9 | outlier knee max (z +4.8) |
| `lawrence_0_35_35_t10-14_shift` | B | 4_lawrence_0_35_35 10.0–14.5 s | 12.0 / 7.8 | 20 / 8 | outlier knee max (z +3.7) |
| `lawrence_0_35_35_t19-24_shift` | B | 4_lawrence_0_35_35 18.6–24.2 s | 28.8 / 16.6 | 21 / 7 | human steps |
| `lawrence_0_35_35_t47-51_shift` | B | 4_lawrence_0_35_35 46.8–51.0 s | 19.0 / 10.7 | 29 / 8 | outlier knee max (z +4.2) |
| `lawrence_0_35_35_t54-67_shift` | B | 4_lawrence_0_35_35 53.5–67.1 s | 16.3 / 9.2 | 29 / 11 | knee 61 deg; outlier knee max (z +8.4) |
| `lawrence_0_36_36_t46-51_shift` | B | 4_lawrence_0_36_36 46.1–50.6 s | 14.0 / 7.7 | 24 / 9 | outlier knee max (z +5.9) |
| `lawrence_0_36_36_t5-10_shift` | B | 4_lawrence_0_36_36 5.0–9.7 s | 16.4 / 8.8 | 36 / 15 | outlier knee max (z +4.6) |
| `lawrence_0_37_37_t21-26_shift` | B | 4_lawrence_0_37_37 21.1–25.7 s | 13.9 / 7.5 | 24 / 9 | outlier knee max (z +4.4) |
| `lawrence_0_37_37_t36-45_shift` | B | 4_lawrence_0_37_37 36.5–45.5 s | 16.9 / 9.1 | 21 / 8 | outlier knee max (z +5.8) |
| `lawrence_0_37_37_t46-50_shift` | B | 4_lawrence_0_37_37 45.9–50.4 s | 16.3 / 10.9 | 25 / 7 | outlier knee max (z +5.8) |
| `lawrence_0_37_37_t52-59_shift` | B | 4_lawrence_0_37_37 51.7–58.7 s | 11.9 / 6.1 | 33 / 11 | outlier knee max (z +3.8) |
| `lawrence_0_37_37_t64-69_shift` | B | 4_lawrence_0_37_37 64.4–68.9 s | 14.4 / 8.9 | 17 / 7 | outlier knee max (z +6.3) |
| `lawrence_0_38_38_t31-36_shift` | B | 4_lawrence_0_38_38 31.0–35.6 s | 11.2 / 6.4 | 23 / 8 | outlier knee max (z +3.6) |
| `lawrence_0_38_38_t37-41_shift` | B | 4_lawrence_0_38_38 36.8–41.5 s | 16.6 / 9.6 | 28 / 11 | outlier knee max (z +5.3) |
| `lawrence_0_38_38_t47-52_shift` | B | 4_lawrence_0_38_38 47.1–51.7 s | 20.6 / 11.1 | 33 / 13 | outlier knee max (z +5.0) |
| `lawrence_0_38_38_t54-59_shift` | B | 4_lawrence_0_38_38 54.0–58.6 s | 19.2 / 12.3 | 30 / 13 | outlier knee max (z +6.1) |
| `lawrence_0_38_38_t61-66_shift` | B | 4_lawrence_0_38_38 61.2–65.8 s | 17.1 / 8.3 | 19 / 7 | outlier knee max (z +4.9) |
| `lawrence_0_39_39_t42-51_shift` | B | 4_lawrence_0_39_39 42.4–51.3 s | 18.2 / 11.1 | 28 / 9 | outlier knee max (z +4.1) |
| `lawrence_0_3_3_t18-25_shift` | B | 4_lawrence_0_3_3 18.3–24.8 s | 19.6 / 10.5 | 24 / 9 | outlier knee max (z +5.2) |
| `lawrence_0_3_3_t28-40_shift` | B | 4_lawrence_0_3_3 28.5–40.4 s | 22.5 / 12.9 | 28 / 12 | outlier knee max (z +6.9) |
| `lawrence_0_3_3_t3-11` | A | 4_lawrence_0_3_3 3.4–11.1 s | 10.0 / 5.6 | 26 / 10 | outlier knee max (z +4.3) |
| `lawrence_0_3_3_t41-50_shift` | B | 4_lawrence_0_3_3 41.4–50.0 s | 15.3 / 8.5 | 22 / 9 | outlier knee max (z +4.6) |
| `lawrence_0_3_3_t51-58_shift` | B | 4_lawrence_0_3_3 50.9–58.1 s | 20.7 / 10.1 | 24 / 10 | outlier knee max (z +6.4) |
| `lawrence_0_3_3_t60-64_shift` | B | 4_lawrence_0_3_3 59.5–64.0 s | 14.9 / 8.4 | 23 / 9 | outlier knee max (z +5.1) |
| `lawrence_0_3_3_t69-78_shift` | B | 4_lawrence_0_3_3 69.0–77.7 s | 11.4 / 6.3 | 33 / 13 | outlier knee max (z +4.0) |
| `lawrence_0_40_40_t0-5_shift` | B | 4_lawrence_0_40_40 0.4–4.9 s | 10.9 / 5.9 | 27 / 12 | shoulder at limit 13% |
| `lawrence_0_40_40_t13-18_shift` | B | 4_lawrence_0_40_40 13.4–17.9 s | 14.3 / 9.8 | 44 / 13 | shoulder at limit 76%; outlier knee max (z +5.5) |
| `lawrence_0_40_40_t3-8` | A | 4_lawrence_0_40_40 2.9–8.0 s | 1.3 / 0.5 | 39 / 15 | shoulder at limit 8% |
| `lawrence_0_40_40_t32-36` | A | 4_lawrence_0_40_40 32.0–36.4 s | 4.4 / 1.2 | 56 / 19 | outlier knee max (z +4.9) |
| `lawrence_0_40_40_t6-10_shift` | B | 4_lawrence_0_40_40 6.0–10.5 s | 11.2 / 6.5 | 42 / 16 | outlier knee max (z +4.7) |
| `lawrence_0_40_40_t60-64_shift` | B | 4_lawrence_0_40_40 59.7–64.3 s | 17.5 / 10.2 | 31 / 10 | outlier knee max (z +5.1) |
| `lawrence_0_41_41_t11-17` | A | 4_lawrence_0_41_41 11.2–17.2 s | 1.0 / 0.9 | 55 / 15 | shoulder at limit 11% |
| `lawrence_0_41_41_t15-20_shift` | B | 4_lawrence_0_41_41 15.2–19.7 s | 16.5 / 9.7 | 39 / 12 | shoulder at limit 14%; outlier knee max (z +5.8) |
| `lawrence_0_41_41_t46-50_shift` | B | 4_lawrence_0_41_41 46.5–50.5 s | 25.1 / 13.5 | 38 / 12 | human steps; outlier knee max (z +5.2) |
| `lawrence_0_41_41_t7-11_shift` | B | 4_lawrence_0_41_41 6.6–10.6 s | 11.9 / 6.3 | 32 / 10 | shoulder at limit 86% |
| `lawrence_0_42_42_t33-39_shift` | B | 4_lawrence_0_42_42 32.7–39.2 s | 26.8 / 14.1 | 40 / 12 | human steps |
| `lawrence_0_42_42_t5-11_shift` | B | 4_lawrence_0_42_42 5.3–11.1 s | 17.6 / 9.5 | 24 / 8 | outlier knee max (z +6.5); hand presses into leg 18 mm for 0.5 s (at 0.8 s) |
| `lawrence_0_43_43_t19-27_shift` | B | 4_lawrence_0_43_43 19.3–27.2 s | 22.4 / 13.9 | 19 / 7 | outlier knee max (z +6.1) |
| `lawrence_0_43_43_t5-15_shift` | B | 4_lawrence_0_43_43 5.5–15.4 s | 20.7 / 10.6 | 21 / 6 | outlier knee max (z +5.3); hand presses into leg 8 mm for 0.2 s (at 1.1 s) |
| `lawrence_0_46_46_t3-7_shift` | B | 4_lawrence_0_46_46 3.3–7.3 s | 10.0 / 2.0 | 27 / 10 | outlier knee max (z +5.2) |
| `lawrence_0_46_46_t30-47_shift` | B | 4_lawrence_0_46_46 30.4–46.9 s | 33.5 / 20.0 | 41 / 14 | human steps; K1 feet move 20 cm; outlier knee max (z +7.5) |
| `lawrence_0_46_46_t5-14` | A | 4_lawrence_0_46_46 5.1–13.7 s | 9.4 / 2.3 | 39 / 12 | outlier knee max (z +5.9) |
| `lawrence_0_46_46_t58-62_shift` | B | 4_lawrence_0_46_46 58.2–62.2 s | 13.9 / 8.0 | 28 / 11 | outlier knee max (z +3.5) |
| `lawrence_0_47_47_t35-42_shift` | B | 4_lawrence_0_47_47 35.0–41.6 s | 22.1 / 11.2 | 36 / 14 | outlier knee max (z +5.3) |
| `lawrence_0_47_47_t45-53_shift` | B | 4_lawrence_0_47_47 45.4–53.3 s | 37.5 / 22.1 | 44 / 13 | human steps; K1 feet move 22 cm; outlier knee max (z +5.7) |
| `lawrence_0_48_48_t3-8_shift` | B | 4_lawrence_0_48_48 2.7–7.6 s | 7.7 / 1.7 | 43 / 12 | outlier knee max (z +6.1) |
| `lawrence_0_48_48_t44-61_shift` | B | 4_lawrence_0_48_48 43.8–60.7 s | 14.5 / 9.5 | 29 / 10 | outlier knee max (z +4.0) |
| `lawrence_0_4_4_t30-34_shift` | B | 4_lawrence_0_4_4 29.9–34.5 s | 14.5 / 8.5 | 27 / 11 | outlier knee max (z +7.1) |
| `lawrence_0_4_4_t36-44_shift` | B | 4_lawrence_0_4_4 36.4–44.1 s | 17.7 / 9.4 | 31 / 13 | outlier knee max (z +6.3) |
| `lawrence_0_4_4_t53-61_shift` | B | 4_lawrence_0_4_4 53.1–61.3 s | 22.4 / 13.0 | 25 / 9 | outlier knee max (z +7.4) |
| `lawrence_0_4_4_t69-78_shift` | B | 4_lawrence_0_4_4 69.1–78.1 s | 15.9 / 9.2 | 23 / 8 | outlier knee max (z +6.4) |
| `lawrence_0_4_4_t81-91_shift` | B | 4_lawrence_0_4_4 80.7–90.8 s | 13.3 / 7.0 | 29 / 12 | outlier knee max (z +3.6) |
| `lawrence_0_4_4_t9-16_shift` | B | 4_lawrence_0_4_4 9.1–16.4 s | 15.0 / 8.2 | 28 / 9 | outlier knee max (z +5.2) |
| `lawrence_0_50_50_t27-33_shift` | B | 4_lawrence_0_50_50 27.1–32.5 s | 18.6 / 10.4 | 25 / 7 | outlier knee max (z +6.6) |
| `lawrence_0_51_51_t25-29_shift` | B | 4_lawrence_0_51_51 24.6–29.0 s | 10.9 / 6.6 | 38 / 10 | outlier knee max (z +5.1) |
| `lawrence_0_52_52_t35-40_shift` | B | 4_lawrence_0_52_52 34.9–39.5 s | 16.3 / 10.4 | 35 / 13 | outlier knee max (z +5.2) |
| `lawrence_0_53_53_t28-38_shift` | B | 4_lawrence_0_53_53 28.2–37.8 s | 16.7 / 9.1 | 29 / 12 | outlier knee max (z +5.2) |
| `lawrence_0_54_54_t16-20_shift` | B | 4_lawrence_0_54_54 15.7–20.1 s | 11.3 / 7.2 | 31 / 13 | outlier knee max (z +4.0) |
| `lawrence_0_54_54_t23-28_shift` | B | 4_lawrence_0_54_54 23.5–28.0 s | 15.9 / 9.9 | 46 / 16 | outlier knee max (z +5.2) |
| `lawrence_0_55_55_t20-38` | A | 4_lawrence_0_55_55 19.6–38.4 s | 5.1 / 1.8 | 36 / 11 | outlier trunk drop (z +4.2) |
| `lawrence_0_57_57_t12-25_shift` | B | 4_lawrence_0_57_57 12.4–25.2 s | 16.6 / 8.5 | 33 / 10 | outlier knee max (z +4.8) |
| `lawrence_0_57_57_t23-32` | A | 4_lawrence_0_57_57 23.2–31.8 s | 10.0 / 3.0 | 48 / 14 | shoulder at limit 16%; leg at limit 7% |
| `lawrence_0_58_58_t2-10` | A | 4_lawrence_0_58_58 1.5–10.1 s | 6.4 / 3.7 | 53 / 17 | outlier knee max (z +5.9) |
| `lawrence_0_59_59_t18-30` | A | 4_lawrence_0_59_59 17.7–30.4 s | 8.9 / 5.9 | 32 / 9 | leg at limit 8%; outlier trunk drop (z +4.4) |
| `lawrence_0_59_59_t36-41_shift` | B | 4_lawrence_0_59_59 36.4–40.9 s | 13.2 / 7.1 | 26 / 8 | outlier knee max (z +5.4) |
| `lawrence_0_59_59_t5-18` | A | 4_lawrence_0_59_59 5.0–17.7 s | 6.4 / 2.3 | 39 / 11 | outlier trunk drop (z +4.3) |
| `lawrence_0_59_59_t54-59_shift` | B | 4_lawrence_0_59_59 53.6–58.8 s | 12.1 / 7.1 | 51 / 14 | outlier knee max (z +6.1) |
| `lawrence_0_5_5_t0-7_shift` | B | 4_lawrence_0_5_5 0.2–6.9 s | 24.8 / 13.9 | 22 / 8 | outlier knee max (z +4.0) |
| `lawrence_0_5_5_t13-18_shift` | B | 4_lawrence_0_5_5 13.3–17.8 s | 14.7 / 8.9 | 24 / 10 | outlier knee max (z +5.8) |
| `lawrence_0_5_5_t20-25_shift` | B | 4_lawrence_0_5_5 20.1–24.5 s | 7.1 / 5.0 | 30 / 13 | outlier knee max (z +3.6) |
| `lawrence_0_5_5_t25-29_shift` | B | 4_lawrence_0_5_5 24.6–29.0 s | 9.9 / 7.0 | 27 / 11 | outlier knee max (z +4.7) |
| `lawrence_0_5_5_t42-48_shift` | B | 4_lawrence_0_5_5 42.1–48.0 s | 24.4 / 13.6 | 22 / 8 | outlier knee max (z +4.3) |
| `lawrence_0_5_5_t52-64_shift` | B | 4_lawrence_0_5_5 52.4–64.0 s | 17.2 / 9.1 | 27 / 10 | outlier knee max (z +7.5) |
| `lawrence_0_5_5_t68-73_shift` | B | 4_lawrence_0_5_5 68.3–72.7 s | 10.1 / 5.6 | 23 / 10 | outlier knee max (z +5.0) |
| `lawrence_0_5_5_t88-92_shift` | B | 4_lawrence_0_5_5 87.8–92.3 s | 9.8 / 6.7 | 37 / 15 | outlier knee max (z +5.2) |
| `lawrence_0_61_61_t0-16_shift` | B | 4_lawrence_0_61_61 0.0–15.9 s | 20.3 / 10.9 | 38 / 11 | outlier knee max (z +6.5) |
| `lawrence_0_61_61_t14-18` | A | 4_lawrence_0_61_61 13.9–18.1 s | 2.9 / 2.5 | 37 / 11 | upper-arm twist at limit 17% |
| `lawrence_0_61_61_t16-21_shift` | B | 4_lawrence_0_61_61 16.1–20.6 s | 16.1 / 10.0 | 29 / 10 | outlier knee max (z +5.6) |
| `lawrence_0_63_63_t30-39_shift` | B | 4_lawrence_0_63_63 30.4–39.4 s | 27.2 / 14.0 | 45 / 15 | human steps; outlier knee max (z +4.3) |
| `lawrence_0_64_64_t0-16_shift` | B | 4_lawrence_0_64_64 0.0–15.9 s | 18.8 / 11.7 | 24 / 8 | outlier knee max (z +4.3) |
| `lawrence_0_65_65_t0-4_shift` | B | 4_lawrence_0_65_65 0.0–4.1 s | 24.9 / 14.3 | 40 / 13 | outlier knee max (z +5.4) |
| `lawrence_0_65_65_t10-29_shift` | B | 4_lawrence_0_65_65 10.4–29.4 s | 25.0 / 14.5 | 47 / 16 | outlier knee max (z +7.5) |
| `lawrence_0_66_66_t12-18_shift` | B | 4_lawrence_0_66_66 11.5–17.7 s | 21.6 / 11.9 | 33 / 12 | outlier knee max (z +6.1) |
| `lawrence_0_66_66_t19-23_shift` | B | 4_lawrence_0_66_66 18.7–23.2 s | 16.4 / 10.9 | 19 / 6 | outlier knee max (z +5.3) |
| `lawrence_0_66_66_t23-27_shift` | B | 4_lawrence_0_66_66 23.4–27.4 s | 20.8 / 12.2 | 30 / 11 | outlier knee max (z +4.1) |
| `lawrence_0_66_66_t36-53_shift` | B | 4_lawrence_0_66_66 35.7–53.2 s | 20.7 / 12.9 | 51 / 17 | outlier knee max (z +6.2) |
| `lawrence_0_66_66_t56-60_shift` | B | 4_lawrence_0_66_66 56.3–60.3 s | 14.4 / 5.7 | 68 / 23 | outlier arms k1 cm (z +4.3) |
| `lawrence_0_67_67_t3-9_shift` | B | 4_lawrence_0_67_67 3.2–8.6 s | 17.4 / 9.2 | 44 / 12 | outlier knee max (z +5.3) |
| `lawrence_0_67_67_t31-36_shift` | B | 4_lawrence_0_67_67 30.5–35.5 s | 24.6 / 14.1 | 66 / 20 | outlier arms k1 cm (z +3.5); outlier knee max (z +6.1) |
| `lawrence_0_67_67_t39-43_shift` | B | 4_lawrence_0_67_67 39.2–43.4 s | 19.8 / 10.9 | 37 / 11 | outlier knee max (z +4.4) |
| `lawrence_0_68_68_t33-38_shift` | B | 4_lawrence_0_68_68 33.1–38.3 s | 20.5 / 10.9 | 34 / 12 | outlier knee max (z +4.4) |
| `lawrence_0_68_68_t40-47_shift` | B | 4_lawrence_0_68_68 40.5–47.5 s | 25.1 / 13.8 | 71 / 21 | human steps; outlier arms k1 cm (z +3.9); outlier knee max (z +5.4) |
| `lawrence_0_68_68_t45-52` | A | 4_lawrence_0_68_68 45.5–52.0 s | 6.6 / 3.2 | 69 / 21 | outlier arms k1 cm (z +3.8) |
| `lawrence_0_6_6_t27-38_shift` | B | 4_lawrence_0_6_6 27.2–38.4 s | 16.0 / 8.6 | 24 / 10 | outlier knee max (z +5.8) |
| `lawrence_0_6_6_t5-9_shift` | B | 4_lawrence_0_6_6 4.8–9.3 s | 13.2 / 9.2 | 28 / 12 | outlier knee max (z +5.5) |
| `lawrence_0_6_6_t79-93_shift` | B | 4_lawrence_0_6_6 79.0–92.8 s | 15.1 / 8.2 | 35 / 14 | outlier knee max (z +5.5) |
| `lawrence_0_6_6_t87-92` | A | 4_lawrence_0_6_6 87.4–92.2 s | 9.7 / 5.6 | 34 / 14 | outlier knee max (z +5.5) |
| `lawrence_0_70_70_t28-33_shift` | B | 4_lawrence_0_70_70 28.4–32.8 s | 12.8 / 7.9 | 32 / 13 | outlier knee max (z +5.2) |
| `lawrence_0_70_70_t35-40_shift` | B | 4_lawrence_0_70_70 35.4–40.0 s | 19.7 / 11.8 | 34 / 15 | outlier knee max (z +4.3) |
| `lawrence_0_72_72_t13-27_shift` | B | 4_lawrence_0_72_72 13.4–26.6 s | 20.4 / 11.6 | 31 / 12 | outlier knee max (z +4.3) |
| `lawrence_0_73_73_t18-31_shift` | B | 4_lawrence_0_73_73 18.2–30.7 s | 17.0 / 10.7 | 34 / 10 | outlier knee max (z +4.3) |
| `lawrence_0_73_73_t33-46_shift` | B | 4_lawrence_0_73_73 33.1–45.8 s | 24.8 / 12.5 | 44 / 12 | outlier knee max (z +5.3) |
| `lawrence_0_73_73_t4-8` | A | 4_lawrence_0_73_73 3.7–8.1 s | 0.4 / 0.7 | 12 / 4 | hand presses into leg 11 mm for 1.8 s (at 2.3 s) |
| `lawrence_0_73_73_t6-10_shift` | B | 4_lawrence_0_73_73 6.1–10.4 s | 8.2 / 4.4 | 16 / 5 | hand presses into leg 18 mm for 1.6 s (at 0.0 s) |
| `lawrence_0_74_74_t40-44_shift` | B | 4_lawrence_0_74_74 39.8–44.3 s | 13.2 / 7.4 | 35 / 10 | outlier knee max (z +4.7) |
| `lawrence_0_74_74_t47-51_shift` | B | 4_lawrence_0_74_74 46.7–50.8 s | 25.8 / 14.4 | 37 / 10 | human steps; outlier knee max (z +5.1) |
| `lawrence_0_75_75_t24-28_shift` | B | 4_lawrence_0_75_75 23.6–27.6 s | 24.7 / 13.3 | 39 / 11 | outlier knee max (z +4.0) |
| `lawrence_0_75_75_t4-8_shift` | B | 4_lawrence_0_75_75 4.2–8.2 s | 23.8 / 13.5 | 56 / 17 | outlier knee max (z +5.2) |
| `lawrence_0_76_76_t23-28_shift` | B | 4_lawrence_0_76_76 23.2–28.4 s | 26.6 / 15.6 | 49 / 14 | human steps |
| `lawrence_0_76_76_t32-45_shift` | B | 4_lawrence_0_76_76 32.0–44.8 s | 33.1 / 20.9 | 40 / 11 | human steps; K1 feet move 21 cm |
| `lawrence_0_77_77_t15-21_shift` | B | 4_lawrence_0_77_77 14.8–20.9 s | 11.7 / 6.6 | 71 / 22 | outlier arms k1 cm (z +4.2); outlier knee max (z +4.0) |
| `lawrence_0_77_77_t22-26_shift` | B | 4_lawrence_0_77_77 21.7–26.2 s | 15.4 / 10.5 | 36 / 9 | outlier knee max (z +5.8) |
| `lawrence_0_77_77_t27-32_shift` | B | 4_lawrence_0_77_77 27.4–31.8 s | 11.3 / 6.7 | 29 / 6 | outlier knee max (z +3.5) |
| `lawrence_0_77_77_t4-13_shift` | B | 4_lawrence_0_77_77 4.4–12.6 s | 11.7 / 6.9 | 19 / 5 | outlier knee max (z +3.7) |
| `lawrence_0_78_78_t12-21_shift` | B | 4_lawrence_0_78_78 11.9–20.8 s | 19.7 / 11.2 | 35 / 11 | outlier knee max (z +4.1) |
| `lawrence_0_78_78_t34-42_shift` | B | 4_lawrence_0_78_78 34.5–41.8 s | 23.3 / 13.3 | 35 / 10 | outlier knee max (z +3.8) |
| `lawrence_0_79_79_t16-24` | A | 4_lawrence_0_79_79 15.9–24.2 s | 8.1 / 4.8 | 39 / 12 | shoulder at limit 10% |
| `lawrence_0_79_79_t5-9_shift` | B | 4_lawrence_0_79_79 4.9–8.9 s | 21.2 / 12.5 | 29 / 10 | outlier knee max (z +5.3) |
| `lawrence_0_79_79_t50-54_shift` | B | 4_lawrence_0_79_79 49.8–53.8 s | 29.5 / 16.5 | 41 / 12 | human steps |
| `lawrence_0_7_7_t22-26_shift` | B | 4_lawrence_0_7_7 21.7–26.2 s | 13.0 / 8.2 | 23 / 8 | outlier knee max (z +4.9) |
| `lawrence_0_7_7_t27-32_shift` | B | 4_lawrence_0_7_7 26.8–32.2 s | 20.5 / 12.1 | 20 / 8 | outlier knee max (z +6.8) |
| `lawrence_0_7_7_t49-53_shift` | B | 4_lawrence_0_7_7 48.6–53.1 s | 14.1 / 8.4 | 27 / 11 | outlier knee max (z +6.0) |
| `lawrence_0_7_7_t62-70_shift` | B | 4_lawrence_0_7_7 62.5–70.2 s | 18.2 / 9.9 | 25 / 10 | outlier knee max (z +5.2) |
| `lawrence_0_7_7_t74-78_shift` | B | 4_lawrence_0_7_7 73.7–78.2 s | 15.6 / 9.7 | 42 / 15 | outlier knee max (z +6.1) |
| `lawrence_0_7_7_t76-83` | A | 4_lawrence_0_7_7 76.2–83.2 s | 2.2 / 1.4 | 37 / 14 | outlier knee max (z +5.4) |
| `lawrence_0_7_7_t81-86_shift` | B | 4_lawrence_0_7_7 81.2–85.8 s | 24.3 / 14.6 | 27 / 11 | knee 62 deg; outlier knee max (z +8.5) |
| `lawrence_0_80_80_t10-18_shift` | B | 4_lawrence_0_80_80 10.1–17.5 s | 22.6 / 12.4 | 39 / 12 | outlier knee max (z +4.7) |
| `lawrence_0_80_80_t50-55_shift` | B | 4_lawrence_0_80_80 50.0–55.0 s | 24.0 / 12.5 | 52 / 15 | outlier knee max (z +6.0) |
| `lawrence_0_81_81_t30-34_shift` | B | 4_lawrence_0_81_81 30.0–34.4 s | 9.9 / 5.3 | 25 / 7 | outlier knee max (z +4.3) |
| `lawrence_0_81_81_t32-48` | A | 4_lawrence_0_81_81 32.4–48.2 s | 9.3 / 4.8 | 35 / 10 | outlier knee max (z +3.7); hand presses into leg 24 mm for 0.1 s (at 6.0 s) |
| `lawrence_0_81_81_t48-64` | A | 4_lawrence_0_81_81 48.2–64.1 s | 0.4 / 0.5 | 14 / 4 | hand presses into leg 13 mm for 0.1 s (at 7.0 s) |
| `lawrence_0_82_82_t91-95_shift` | B | 4_lawrence_0_82_82 90.9–95.3 s | 11.2 / 6.2 | 52 / 14 | outlier knee max (z +5.2) |
| `lawrence_0_83_83_t71-75_shift` | B | 4_lawrence_0_83_83 70.8–74.8 s | 22.5 / 12.5 | 41 / 12 | outlier knee max (z +6.2) |
| `lawrence_0_85_85_t30-45` | A | 4_lawrence_0_85_85 30.2–45.3 s | 0.3 / 0.3 | 13 / 4 | hand presses into leg 7 mm for 0.1 s (at 9.1 s) |
| `lawrence_0_85_85_t45-60` | A | 4_lawrence_0_85_85 45.3–60.5 s | 0.8 / 0.9 | 16 / 5 | hand presses into leg 13 mm for 0.5 s (at 8.0 s) |
| `lawrence_0_85_85_t58-64_shift` | B | 4_lawrence_0_85_85 58.5–64.5 s | 15.9 / 9.0 | 22 / 6 | outlier knee max (z +4.5) |
| `lawrence_0_86_86_t16-35` | A | 4_lawrence_0_86_86 15.6–34.9 s | 4.6 / 1.0 | 30 / 9 | hand presses into leg 31 mm for 0.2 s (at 12.6 s) |
| `lawrence_0_87_87_t0-5_shift` | B | 4_lawrence_0_87_87 0.0–5.0 s | 15.0 / 8.4 | 52 / 14 | outlier knee max (z +4.1) |
| `lawrence_0_88_88_t24-31_shift` | B | 4_lawrence_0_88_88 24.5–30.8 s | 24.7 / 13.8 | 15 / 5 | outlier knee max (z +4.1) |
| `lawrence_0_8_8_t14-22_shift` | B | 4_lawrence_0_8_8 13.9–22.0 s | 19.9 / 11.2 | 32 / 13 | outlier knee max (z +6.5) |
| `lawrence_0_8_8_t32-40_shift` | B | 4_lawrence_0_8_8 32.4–40.0 s | 17.6 / 8.4 | 28 / 11 | outlier knee max (z +5.3) |
| `lawrence_0_8_8_t38-44` | A | 4_lawrence_0_8_8 38.0–43.8 s | 2.4 / 1.1 | 34 / 13 | outlier trunk drop (z +4.0); outlier knee max (z +3.6) |
| `lawrence_0_8_8_t63-68_shift` | B | 4_lawrence_0_8_8 63.1–67.5 s | 9.3 / 5.6 | 48 / 19 | outlier knee max (z +4.1) |
| `lawrence_0_8_8_t7-12_shift` | B | 4_lawrence_0_8_8 7.4–11.9 s | 14.4 / 9.1 | 30 / 13 | outlier knee max (z +5.7) |
| `lawrence_0_8_8_t71-78_shift` | B | 4_lawrence_0_8_8 71.3–78.2 s | 18.3 / 10.1 | 21 / 6 | outlier knee max (z +4.7) |
| `lawrence_0_8_8_t94-102_shift` | B | 4_lawrence_0_8_8 94.0–101.7 s | 27.1 / 15.7 | 28 / 9 | human steps; outlier knee max (z +5.9) |
| `lawrence_0_90_90_t0-8_shift` | B | 4_lawrence_0_90_90 0.0–8.5 s | 21.9 / 11.9 | 39 / 13 | outlier knee max (z +5.5) |
| `lawrence_0_90_90_t26-30_shift` | B | 4_lawrence_0_90_90 25.9–30.3 s | 10.0 / 5.6 | 37 / 11 | outlier knee max (z +5.2) |
| `lawrence_0_90_90_t74-78_shift` | B | 4_lawrence_0_90_90 74.0–78.5 s | 9.3 / 5.3 | 32 / 10 | outlier knee max (z +4.1) |
| `lawrence_0_91_91_t0-4_shift` | B | 4_lawrence_0_91_91 0.0–4.0 s | 18.2 / 9.6 | 22 / 6 | outlier knee max (z +4.0) |
| `lawrence_0_91_91_t24-28_shift` | B | 4_lawrence_0_91_91 23.9–28.3 s | 9.1 / 5.2 | 51 / 15 | outlier knee max (z +4.8) |
| `lawrence_0_91_91_t52-56_shift` | B | 4_lawrence_0_91_91 52.4–56.4 s | 24.1 / 14.0 | 38 / 15 | outlier knee max (z +4.5) |
| `lawrence_0_92_92_t31-46` | A | 4_lawrence_0_92_92 30.7–46.1 s | 12.7 / 7.0 | 58 / 16 | human steps |
| `lawrence_0_93_93_t26-30_shift` | B | 4_lawrence_0_93_93 26.1–30.1 s | 27.3 / 15.3 | 13 / 5 | human steps; outlier knee max (z +4.2) |
| `lawrence_0_94_94_t10-25` | A | 4_lawrence_0_94_94 10.3–25.0 s | 4.2 / 0.7 | 28 / 10 | shoulder at limit 6% |
| `lawrence_0_94_94_t52-58_shift` | B | 4_lawrence_0_94_94 52.4–57.5 s | 8.2 / 5.4 | 82 / 20 | outlier arms k1 cm (z +3.7) |
| `lawrence_0_95_95_t20-35_shift` | B | 4_lawrence_0_95_95 19.5–34.8 s | 24.0 / 13.6 | 58 / 18 | knee 60 deg; outlier knee max (z +8.1) |
| `lawrence_0_95_95_t45-61_shift` | B | 4_lawrence_0_95_95 44.9–60.6 s | 12.5 / 7.0 | 57 / 15 | outlier knee max (z +6.8) |
| `lawrence_0_96_96_t0-6_shift` | B | 4_lawrence_0_96_96 0.0–5.9 s | 23.6 / 13.0 | 40 / 14 | outlier knee max (z +6.7) |
| `lawrence_0_96_96_t17-29` | A | 4_lawrence_0_96_96 16.6–29.3 s | 10.9 / 5.9 | 35 / 13 | human steps |
| `lawrence_0_96_96_t27-33_shift` | B | 4_lawrence_0_96_96 27.3–33.3 s | 16.5 / 9.7 | 50 / 14 | outlier knee max (z +6.2) |
| `lawrence_0_96_96_t35-52_shift` | B | 4_lawrence_0_96_96 34.7–52.4 s | 15.9 / 9.3 | 56 / 18 | outlier knee max (z +6.1) |
| `lawrence_0_96_96_t50-56` | A | 4_lawrence_0_96_96 50.4–55.8 s | 1.4 / 0.5 | 86 / 20 | outlier arms k1 cm (z +3.5) |
| `lawrence_0_97_97_t35-39_shift` | B | 4_lawrence_0_97_97 35.0–39.4 s | 9.7 / 5.2 | 77 / 20 | outlier arms k1 cm (z +3.7) |
| `lawrence_0_97_97_t45-50_shift` | B | 4_lawrence_0_97_97 45.1–49.5 s | 10.3 / 6.1 | 26 / 9 | outlier knee max (z +3.8) |
| `lawrence_0_98_98_t0-7_shift` | B | 4_lawrence_0_98_98 0.0–7.4 s | 20.4 / 12.0 | 37 / 10 | outlier knee max (z +5.2) |
| `lawrence_0_98_98_t18-25_shift` | B | 4_lawrence_0_98_98 17.8–25.0 s | 23.4 / 13.6 | 52 / 14 | outlier knee max (z +5.6) |
| `lawrence_0_98_98_t34-40` | A | 4_lawrence_0_98_98 34.1–40.2 s | 8.4 / 5.0 | 72 / 23 | outlier arms k1 cm (z +4.4) |
| `lawrence_0_98_98_t38-43_shift` | B | 4_lawrence_0_98_98 38.2–42.9 s | 14.7 / 8.2 | 53 / 13 | outlier knee max (z +4.9) |
| `lawrence_0_99_99_t16-28_shift` | B | 4_lawrence_0_99_99 15.9–28.4 s | 13.9 / 8.1 | 30 / 10 | outlier knee max (z +3.6) |
| `lawrence_0_99_99_t50-59_shift` | B | 4_lawrence_0_99_99 49.9–59.2 s | 15.7 / 9.1 | 40 / 17 | outlier knee max (z +6.2) |
| `lawrence_0_9_9_t12-21_shift` | B | 4_lawrence_0_9_9 11.8–20.8 s | 24.5 / 12.5 | 44 / 15 | outlier knee max (z +6.7) |
| `lawrence_0_9_9_t54-62_shift` | B | 4_lawrence_0_9_9 54.4–61.9 s | 22.4 / 11.9 | 37 / 13 | outlier knee max (z +4.9) |
| `lawrence_1_10_10_t133-137_shift` | B | 4_lawrence_1_10_10 133.1–137.1 s | 1.1 / 1.9 | 54 / 15 | head at limit 9% |
| `lawrence_1_10_10_t134-140` | A | 4_lawrence_1_10_10 133.7–140.2 s | 6.1 / 1.2 | 59 / 16 | head at limit 17% |
| `lawrence_1_10_10_t146-150_shift` | B | 4_lawrence_1_10_10 146.2–150.2 s | 12.3 / 10.5 | 19 / 5 | head at limit 50% |
| `lawrence_1_10_10_t148-153` | A | 4_lawrence_1_10_10 147.8–153.3 s | 4.5 / 3.0 | 24 / 7 | head at limit 32% |
| `lawrence_1_10_10_t172-177_shift` | B | 4_lawrence_1_10_10 172.3–177.5 s | 13.8 / 7.9 | 44 / 14 | hand presses into leg 14 mm for 0.2 s (at 3.0 s) |
| `lawrence_1_10_10_t175-181` | A | 4_lawrence_1_10_10 175.5–181.4 s | 1.4 / 1.0 | 62 / 20 | outlier arms k1 cm (z +3.6) |
| `lawrence_1_10_10_t179-184_shift` | B | 4_lawrence_1_10_10 179.4–183.8 s | 9.6 / 5.3 | 105 / 32 | outlier arms k1 cm (z +7.0) |
| `lawrence_1_10_10_t19-31` | A | 4_lawrence_1_10_10 18.7–31.0 s | 6.2 / 4.0 | 36 / 13 | outlier knee max (z +3.7) |
| `lawrence_1_10_10_t205-209_shift` | B | 4_lawrence_1_10_10 205.2–209.2 s | 20.0 / 7.8 | 57 / 18 | outlier knee max (z +4.3) |
| `lawrence_1_10_10_t216-232` | A | 4_lawrence_1_10_10 216.5–232.2 s | 9.3 / 8.8 | 5 / 1 | K1 feet move 9 cm |
| `lawrence_1_10_10_t258-272_shift` | B | 4_lawrence_1_10_10 257.8–271.9 s | 27.6 / 17.8 | 34 / 10 | human steps; knee 62 deg; outlier trunk drop (z +5.1); outlier knee max (z +8.6) |
| `lawrence_1_10_10_t28-32_shift` | B | 4_lawrence_1_10_10 27.8–31.8 s | 17.4 / 7.6 | 56 / 21 | outlier arms k1 cm (z +3.9); outlier knee max (z +3.8) |
| `lawrence_1_10_10_t363-372_shift` | B | 4_lawrence_1_10_10 362.8–371.7 s | 19.7 / 11.3 | 35 / 10 | outlier knee max (z +6.0) |
| `lawrence_1_10_10_t44-49_shift` | B | 4_lawrence_1_10_10 44.0–49.0 s | 11.3 / 6.9 | 34 / 10 | outlier knee max (z +3.6) |
| `lawrence_1_10_10_t468-474_shift` | B | 4_lawrence_1_10_10 468.0–474.3 s | 12.5 / 7.2 | 24 / 7 | head at limit 6% |
| `lawrence_1_10_10_t489-496_shift` | B | 4_lawrence_1_10_10 489.2–496.0 s | 26.7 / 16.3 | 37 / 11 | human steps; outlier knee max (z +7.3) |
| `lawrence_1_10_10_t539-544_shift` | B | 4_lawrence_1_10_10 539.3–543.9 s | 10.0 / 5.2 | 56 / 16 | head at limit 17% |
| `lawrence_1_10_10_t554-573` | A | 4_lawrence_1_10_10 553.7–573.4 s | 2.6 / 0.5 | 18 / 5 | head at limit 6% |
| `lawrence_1_10_10_t642-649_shift` | B | 4_lawrence_1_10_10 642.2–649.2 s | 18.3 / 10.6 | 42 / 13 | outlier knee max (z +4.2) |
| `lawrence_1_10_10_t66-70_shift` | B | 4_lawrence_1_10_10 65.5–69.9 s | 9.6 / 4.3 | 67 / 20 | outlier arms k1 cm (z +3.7) |
| `lawrence_1_10_10_t85-91_shift` | B | 4_lawrence_1_10_10 85.3–90.9 s | 12.7 / 6.2 | 113 / 30 | outlier arms k1 cm (z +6.4) |
| `lawrence_1_10_10_t97-101_shift` | B | 4_lawrence_1_10_10 96.6–101.1 s | 12.5 / 7.8 | 23 / 4 | outlier knee max (z +4.6) |
| `lawrence_1_11_11_t124-138` | A | 4_lawrence_1_11_11 124.5–137.6 s | 8.0 / 4.4 | 66 / 20 | outlier arms k1 cm (z +3.6) |
| `lawrence_1_11_11_t15-26` | A | 4_lawrence_1_11_11 15.4–26.5 s | 4.7 / 8.3 | 2 / 1 | K1 feet move 8 cm |
| `lawrence_1_11_11_t157-168` | A | 4_lawrence_1_11_11 156.7–168.2 s | 0.7 / 0.8 | 24 / 9 | head at limit 7% |
| `lawrence_1_11_11_t166-171_shift` | B | 4_lawrence_1_11_11 166.2–171.3 s | 15.3 / 7.6 | 23 / 9 | outlier knee max (z +4.5) |
| `lawrence_1_11_11_t181-185_shift` | B | 4_lawrence_1_11_11 180.8–184.8 s | 12.7 / 7.3 | 34 / 15 | outlier knee max (z +4.7) |
| `lawrence_1_11_11_t185-189_shift` | B | 4_lawrence_1_11_11 185.2–189.5 s | 8.5 / 4.6 | 60 / 28 | outlier arms k1 cm (z +5.7) |
| `lawrence_1_11_11_t207-214_shift` | B | 4_lawrence_1_11_11 206.8–214.1 s | 22.0 / 13.0 | 39 / 12 | outlier knee max (z +5.7) |
| `lawrence_1_11_11_t307-313_shift` | B | 4_lawrence_1_11_11 307.2–312.5 s | 15.0 / 8.5 | 39 / 15 | outlier knee max (z +5.4) |
| `lawrence_1_11_11_t322-333` | A | 4_lawrence_1_11_11 322.0–333.5 s | 7.2 / 2.1 | 10 / 5 | outlier knee max (z +3.7) |
| `lawrence_1_11_11_t336-344` | A | 4_lawrence_1_11_11 335.8–343.8 s | 1.6 / 0.8 | 31 / 9 | outlier knee max (z +4.3) |
| `lawrence_1_11_11_t342-346_shift` | B | 4_lawrence_1_11_11 341.8–346.2 s | 15.7 / 8.5 | 18 / 5 | outlier knee max (z +6.5) |
| `lawrence_1_11_11_t394-398_shift` | B | 4_lawrence_1_11_11 393.7–397.7 s | 19.3 / 12.4 | 43 / 19 | outlier knee max (z +4.0) |
| `lawrence_1_11_11_t438-451` | A | 4_lawrence_1_11_11 437.9–451.1 s | 6.6 / 2.8 | 7 / 2 | outlier knee max (z +4.7) |
| `lawrence_1_11_11_t66-71_shift` | B | 4_lawrence_1_11_11 66.4–70.8 s | 7.3 / 3.3 | 9 / 6 | head at limit 8% |
| `lawrence_1_12_12_t152-160_shift` | B | 4_lawrence_1_12_12 151.8–159.8 s | 16.4 / 9.0 | 26 / 9 | outlier knee max (z +6.4) |
| `lawrence_1_12_12_t215-225` | A | 4_lawrence_1_12_12 214.7–224.7 s | 2.3 / 5.1 | 6 / 3 | head at limit 10% |
| `lawrence_1_12_12_t223-227_shift` | B | 4_lawrence_1_12_12 222.7–227.5 s | 14.8 / 9.7 | 6 / 4 | head at limit 19%; outlier knee max (z +4.3) |
| `lawrence_1_12_12_t243-256` | A | 4_lawrence_1_12_12 243.3–255.6 s | 4.5 / 1.7 | 19 / 5 | outlier knee max (z +4.4) |
| `lawrence_1_12_12_t284-292_shift` | B | 4_lawrence_1_12_12 284.3–291.5 s | 15.8 / 7.8 | 48 / 15 | outlier knee max (z +4.2) |
| `lawrence_1_12_12_t360-364_shift` | B | 4_lawrence_1_12_12 359.7–363.9 s | 14.3 / 8.2 | 45 / 11 | outlier knee max (z +4.6) |
| `lawrence_1_12_12_t586-590_shift` | B | 4_lawrence_1_12_12 586.1–590.1 s | 31.2 / 18.0 | 13 / 7 | human steps; head at limit 24% |
| `lawrence_1_12_12_t621-625_shift` | B | 4_lawrence_1_12_12 620.6–624.8 s | 16.3 / 10.6 | 1 / 1 | head at limit 14% |
| `lawrence_1_12_12_t658-662_shift` | B | 4_lawrence_1_12_12 657.7–662.0 s | 9.9 / 3.9 | 25 / 8 | outlier knee max (z +4.2) |
| `lawrence_1_12_12_t690-703` | A | 4_lawrence_1_12_12 689.6–703.3 s | 9.5 / 3.8 | 18 / 6 | shoulder at limit 21% |
| `lawrence_1_1_1_t12-16_shift` | B | 4_lawrence_1_1_1 11.5–16.0 s | 24.0 / 12.4 | 59 / 13 | outlier knee max (z +6.7) |
| `lawrence_1_1_1_t248-252_shift` | B | 4_lawrence_1_1_1 248.3–252.3 s | 24.1 / 12.8 | 70 / 18 | outlier knee max (z +4.1) |
| `lawrence_1_1_1_t298-302_shift` | B | 4_lawrence_1_1_1 297.7–301.9 s | 10.6 / 3.8 | 45 / 22 | outlier arms k1 cm (z +4.2) |
| `lawrence_1_1_1_t326-330_shift` | B | 4_lawrence_1_1_1 325.8–329.8 s | 18.2 / 7.2 | 41 / 11 | outlier knee max (z +6.7) |
| `lawrence_1_1_1_t371-378` | A | 4_lawrence_1_1_1 371.3–377.5 s | 9.5 / 8.6 | 38 / 10 | K1 feet move 9 cm |
| `lawrence_1_1_1_t374-378_shift` | B | 4_lawrence_1_1_1 374.0–378.0 s | 24.8 / 10.2 | 38 / 8 | outlier knee max (z +5.0) |
| `lawrence_1_1_1_t519-523_shift` | B | 4_lawrence_1_1_1 518.7–522.7 s | 19.3 / 10.7 | 52 / 12 | outlier knee max (z +4.6) |
| `lawrence_1_1_1_t554-559_shift` | B | 4_lawrence_1_1_1 553.6–558.7 s | 22.6 / 12.3 | 78 / 23 | outlier arms k1 cm (z +4.4) |
| `lawrence_1_2_2_t113-117_shift` | B | 4_lawrence_1_2_2 112.5–116.5 s | 31.3 / 18.7 | 39 / 13 | human steps; K1 feet move 19 cm; outlier knee max (z +3.9) |
| `lawrence_1_2_2_t199-209` | A | 4_lawrence_1_2_2 198.7–208.9 s | 8.1 / 8.0 | 21 / 5 | K1 feet move 8 cm |
| `lawrence_1_2_2_t20-24_shift` | B | 4_lawrence_1_2_2 19.7–23.7 s | 26.8 / 14.8 | 30 / 14 | human steps; knee 60 deg; outlier knee max (z +8.2) |
| `lawrence_1_2_2_t210-215_shift` | B | 4_lawrence_1_2_2 210.0–214.7 s | 9.7 / 2.7 | 20 / 5 | leg at limit 29%; outlier knee max (z +3.7) |
| `lawrence_1_2_2_t307-313_shift` | B | 4_lawrence_1_2_2 307.4–312.7 s | 21.2 / 11.9 | 91 / 26 | outlier arms k1 cm (z +5.2); outlier knee max (z +4.0) |
| `lawrence_1_2_2_t355-361_shift` | B | 4_lawrence_1_2_2 355.2–360.7 s | 14.4 / 9.6 | 22 / 7 | knee 65 deg; outlier knee max (z +9.8) |
| `lawrence_1_2_2_t393-398_shift` | B | 4_lawrence_1_2_2 393.2–398.5 s | 11.8 / 6.3 | 17 / 5 | knee 75 deg; outlier knee max (z +13.1) |
| `lawrence_1_2_2_t68-74` | A | 4_lawrence_1_2_2 68.4–73.6 s | 8.4 / 2.6 | 11 / 4 | shoulder at limit 11% |
| `lawrence_1_2_2_t76-82` | A | 4_lawrence_1_2_2 76.3–81.7 s | 2.9 / 0.9 | 41 / 12 | hand presses into leg 15 mm for 0.4 s (at 2.4 s) |
| `lawrence_1_2_2_t95-107` | A | 4_lawrence_1_2_2 94.6–106.6 s | 10.1 / 5.0 | 44 / 14 | human steps |
| `lawrence_1_3_3_t117-121_shift` | B | 4_lawrence_1_3_3 116.7–121.2 s | 10.1 / 6.1 | 46 / 11 | head at limit 40% |
| `lawrence_1_3_3_t136-140_shift` | B | 4_lawrence_1_3_3 136.0–140.1 s | 23.4 / 17.2 | 56 / 18 | outlier knee max (z +4.7) |
| `lawrence_1_3_3_t152-157_shift` | B | 4_lawrence_1_3_3 152.0–157.0 s | 17.4 / 9.1 | 17 / 9 | outlier knee max (z +4.5) |
| `lawrence_1_3_3_t183-198` | A | 4_lawrence_1_3_3 182.8–198.4 s | 8.6 / 4.8 | 22 / 6 | shoulder at limit 19% |
| `lawrence_1_3_3_t198-214` | A | 4_lawrence_1_3_3 198.4–214.0 s | 8.0 / 5.9 | 38 / 15 | shoulder at limit 7% |
| `lawrence_1_3_3_t212-216_shift` | B | 4_lawrence_1_3_3 212.0–216.4 s | 24.0 / 13.7 | 39 / 14 | outlier knee max (z +5.6) |
| `lawrence_1_3_3_t232-236` | A | 4_lawrence_1_3_3 231.7–235.7 s | 1.2 / 0.7 | 16 / 8 | shoulder at limit 8% |
| `lawrence_1_3_3_t256-262` | A | 4_lawrence_1_3_3 256.5–261.7 s | 1.8 / 0.7 | 66 / 19 | head at limit 8% |
| `lawrence_1_3_3_t260-264_shift` | B | 4_lawrence_1_3_3 259.7–264.3 s | 9.2 / 6.2 | 81 / 23 | outlier arms k1 cm (z +4.5) |
| `lawrence_1_3_3_t27-31_shift` | B | 4_lawrence_1_3_3 27.2–31.2 s | 11.5 / 2.8 | 25 / 7 | outlier knee max (z +3.6) |
| `lawrence_1_3_3_t275-280_shift` | B | 4_lawrence_1_3_3 275.5–280.2 s | 22.7 / 12.7 | 32 / 10 | outlier knee max (z +5.9) |
| `lawrence_1_3_3_t292-303_shift` | B | 4_lawrence_1_3_3 292.3–302.7 s | 19.1 / 10.8 | 39 / 11 | head at limit 7%; outlier knee max (z +3.6) |
| `lawrence_1_3_3_t328-332_shift` | B | 4_lawrence_1_3_3 328.0–332.0 s | 24.0 / 11.6 | 4 / 2 | outlier knee max (z +4.2) |
| `lawrence_1_3_3_t366-372` | A | 4_lawrence_1_3_3 366.1–371.8 s | 2.0 / 1.0 | 17 / 4 | head at limit 8% |
| `lawrence_1_3_3_t378-383` | A | 4_lawrence_1_3_3 378.0–383.3 s | 8.6 / 9.3 | 8 / 3 | K1 feet move 9 cm |
| `lawrence_1_3_3_t388-398` | A | 4_lawrence_1_3_3 388.1–397.9 s | 3.5 / 4.4 | 46 / 12 | head at limit 6% |
| `lawrence_1_3_3_t408-412_shift` | B | 4_lawrence_1_3_3 407.6–412.0 s | 9.0 / 6.7 | 35 / 12 | outlier knee max (z +3.7) |
| `lawrence_1_3_3_t470-489` | A | 4_lawrence_1_3_3 470.2–488.6 s | 7.8 / 2.9 | 19 / 6 | head at limit 6% |
| `lawrence_1_3_3_t583-588_shift` | B | 4_lawrence_1_3_3 583.1–587.6 s | 11.3 / 6.0 | 55 / 16 | outlier knee max (z +4.6) |
| `lawrence_1_3_3_t9-13_shift` | B | 4_lawrence_1_3_3 8.7–13.2 s | 20.0 / 11.4 | 47 / 12 | outlier knee max (z +5.6) |
| `lawrence_1_4_4_t102-106_shift` | B | 4_lawrence_1_4_4 101.5–106.5 s | 23.3 / 9.3 | 9 / 2 | knee 100 deg; outlier knee max (z +21.4) |
| `lawrence_1_4_4_t115-120_shift` | B | 4_lawrence_1_4_4 114.9–120.1 s | 15.9 / 8.1 | 11 / 3 | knee 63 deg; outlier knee max (z +9.0) |
| `lawrence_1_4_4_t13-17` | A | 4_lawrence_1_4_4 13.0–17.2 s | 1.2 / 1.1 | 32 / 11 | shoulder at limit 6% |
| `lawrence_1_4_4_t201-210` | A | 4_lawrence_1_4_4 200.5–210.4 s | 8.8 / 2.6 | 26 / 7 | hand presses into leg 24 mm for 0.2 s (at 0.0 s) |
| `lawrence_1_4_4_t238-243_shift` | B | 4_lawrence_1_4_4 238.2–243.5 s | 17.8 / 11.1 | 20 / 6 | outlier knee max (z +5.5) |
| `lawrence_1_4_4_t241-253` | A | 4_lawrence_1_4_4 241.5–253.3 s | 0.9 / 0.6 | 29 / 9 | hand presses into leg 13 mm for 0.5 s (at 2.7 s) |
| `lawrence_1_4_4_t250-254_shift` | B | 4_lawrence_1_4_4 250.4–254.4 s | 23.5 / 11.1 | 26 / 7 | outlier knee max (z +6.0) |
| `lawrence_1_4_4_t281-293` | A | 4_lawrence_1_4_4 280.5–293.2 s | 7.1 / 4.1 | 34 / 9 | head at limit 13% |
| `lawrence_1_4_4_t359-363_shift` | B | 4_lawrence_1_4_4 358.6–362.9 s | 22.9 / 10.4 | 50 / 19 | leg at limit 13% |
| `lawrence_1_4_4_t401-411` | A | 4_lawrence_1_4_4 400.8–411.4 s | 1.4 / 0.8 | 8 / 2 | hand presses into leg 12 mm for 1.0 s (at 6.8 s) |
| `lawrence_1_4_4_t478-495` | A | 4_lawrence_1_4_4 477.5–494.9 s | 9.2 / 4.7 | 2 / 2 | head at limit 14% |
| `lawrence_1_4_4_t6-15_shift` | B | 4_lawrence_1_4_4 6.0–15.0 s | 15.1 / 11.0 | 46 / 17 | outlier knee max (z +5.5) |
| `lawrence_1_4_4_t94-98_shift` | B | 4_lawrence_1_4_4 93.6–97.6 s | 26.6 / 12.4 | 23 / 6 | human steps; outlier knee max (z +7.2) |
| `lawrence_1_5_5_t102-108_shift` | B | 4_lawrence_1_5_5 102.1–107.7 s | 17.2 / 10.2 | 65 / 19 | outlier knee max (z +4.1) |
| `lawrence_1_5_5_t124-129_shift` | B | 4_lawrence_1_5_5 124.5–128.8 s | 13.7 / 9.4 | 3 / 3 | head at limit 11% |
| `lawrence_1_5_5_t127-137` | A | 4_lawrence_1_5_5 126.8–137.1 s | 5.9 / 1.2 | 19 / 7 | head at limit 13% |
| `lawrence_1_5_5_t138-144_shift` | B | 4_lawrence_1_5_5 137.8–143.6 s | 14.9 / 8.0 | 41 / 10 | outlier knee max (z +4.6) |
| `lawrence_1_5_5_t142-159` | A | 4_lawrence_1_5_5 141.6–158.8 s | 5.5 / 2.8 | 49 / 13 | outlier trunk drop (z +3.6); outlier knee max (z +5.4) |
| `lawrence_1_5_5_t169-173_shift` | B | 4_lawrence_1_5_5 168.8–172.8 s | 12.4 / 5.8 | 18 / 5 | outlier knee max (z +3.6) |
| `lawrence_1_5_5_t205-209_shift` | B | 4_lawrence_1_5_5 204.7–208.7 s | 13.4 / 3.6 | 2 / 1 | head at limit 74% |
| `lawrence_1_5_5_t206-224` | A | 4_lawrence_1_5_5 205.9–223.8 s | 2.3 / 1.6 | 12 / 3 | head at limit 32% |
| `lawrence_1_5_5_t239-243_shift` | B | 4_lawrence_1_5_5 239.0–243.4 s | 22.7 / 13.0 | 43 / 10 | knee 67 deg; outlier knee max (z +10.3) |
| `lawrence_1_5_5_t33-38_shift` | B | 4_lawrence_1_5_5 33.0–37.6 s | 15.5 / 9.3 | 24 / 11 | outlier knee max (z +4.5) |
| `lawrence_1_5_5_t330-334_shift` | B | 4_lawrence_1_5_5 329.8–333.8 s | 11.1 / 2.0 | 80 / 26 | outlier arms k1 cm (z +5.3) |
| `lawrence_1_5_5_t44-50_shift` | B | 4_lawrence_1_5_5 44.0–49.5 s | 19.5 / 10.7 | 34 / 12 | outlier knee max (z +4.3) |
| `lawrence_1_5_5_t490-494_shift` | B | 4_lawrence_1_5_5 489.7–493.7 s | 14.6 / 4.0 | 92 / 26 | head at limit 16%; outlier arms k1 cm (z +5.1) |
| `lawrence_1_5_5_t498-509` | A | 4_lawrence_1_5_5 498.1–508.7 s | 1.6 / 1.2 | 32 / 9 | head at limit 7% |
| `lawrence_1_5_5_t507-514_shift` | B | 4_lawrence_1_5_5 506.7–513.5 s | 15.0 / 8.6 | 10 / 3 | head at limit 23% |
| `lawrence_1_5_5_t532-536_shift` | B | 4_lawrence_1_5_5 532.0–536.5 s | 22.0 / 11.9 | 30 / 9 | head at limit 50% |
| `lawrence_1_5_5_t556-573` | A | 4_lawrence_1_5_5 555.8–573.4 s | 7.0 / 1.9 | 22 / 7 | head at limit 5% |
| `lawrence_1_5_5_t571-576_shift` | B | 4_lawrence_1_5_5 571.4–576.0 s | 15.3 / 8.9 | 31 / 11 | head at limit 27%; outlier knee max (z +7.1) |
| `lawrence_1_5_5_t574-594` | A | 4_lawrence_1_5_5 574.0–593.5 s | 3.3 / 1.8 | 45 / 12 | head at limit 10% |
| `lawrence_1_5_5_t604-608` | A | 4_lawrence_1_5_5 603.7–607.8 s | 6.7 / 2.7 | 113 / 30 | head at limit 12%; outlier arms k1 cm (z +6.4) |
| `lawrence_1_5_5_t9-13_shift` | B | 4_lawrence_1_5_5 9.2–13.2 s | 9.8 / 4.6 | 30 / 13 | head at limit 9% |
| `lawrence_1_5_5_t96-104` | A | 4_lawrence_1_5_5 96.2–104.1 s | 1.9 / 0.4 | 41 / 11 | head at limit 6% |
| `lawrence_1_6_6_t186-191_shift` | B | 4_lawrence_1_6_6 186.2–190.9 s | 22.8 / 16.3 | 34 / 12 | shoulder at limit 45%; self-collision left_hand_collision / right_hand_end_collision 0.6 s (at 0.0 s, 20 mm) |
| `lawrence_1_6_6_t209-213_shift` | B | 4_lawrence_1_6_6 208.9–213.2 s | 9.7 / 5.8 | 28 / 7 | hand presses into leg 9 mm for 0.2 s (at 3.8 s) |
| `lawrence_1_6_6_t245-255` | A | 4_lawrence_1_6_6 244.9–255.1 s | 0.6 / 0.9 | 20 / 6 | hand presses into leg 13 mm for 0.9 s (at 1.2 s) |
| `lawrence_1_6_6_t298-310` | A | 4_lawrence_1_6_6 298.1–309.5 s | 6.7 / 8.6 | 30 / 10 | K1 feet move 9 cm |
| `lawrence_1_6_6_t31-41` | A | 4_lawrence_1_6_6 30.9–41.4 s | 2.7 / 2.3 | 46 / 13 | hand presses into leg 20 mm for 0.3 s (at 2.6 s) |
| `lawrence_1_6_6_t313-318` | A | 4_lawrence_1_6_6 312.9–318.3 s | 5.6 / 5.2 | 94 / 28 | outlier arms k1 cm (z +5.7); hand presses into leg 22 mm for 0.1 s (at 1.0 s) |
| `lawrence_1_6_6_t316-325_shift` | B | 4_lawrence_1_6_6 316.3–324.7 s | 17.3 / 7.7 | 67 / 18 | head at limit 33%; outlier knee max (z +3.8) |
| `lawrence_1_6_6_t323-340` | A | 4_lawrence_1_6_6 322.7–340.1 s | 1.4 / 0.9 | 20 / 6 | head at limit 12% |
| `lawrence_1_6_6_t337-341_shift` | B | 4_lawrence_1_6_6 336.9–340.9 s | 24.8 / 11.1 | 34 / 10 | outlier knee max (z +7.0) |
| `lawrence_1_6_6_t342-347` | A | 4_lawrence_1_6_6 341.9–347.3 s | 5.2 / 3.7 | 47 / 13 | head at limit 18% |
| `lawrence_1_6_6_t345-350_shift` | B | 4_lawrence_1_6_6 345.3–350.0 s | 13.8 / 11.4 | 63 / 17 | head at limit 19% |
| `lawrence_1_6_6_t348-361` | A | 4_lawrence_1_6_6 348.0–361.0 s | 0.8 / 0.6 | 53 / 15 | head at limit 13% |
| `lawrence_1_6_6_t384-395` | A | 4_lawrence_1_6_6 384.1–395.0 s | 8.1 / 5.6 | 15 / 4 | head at limit 23% |
| `lawrence_1_6_6_t397-403` | A | 4_lawrence_1_6_6 396.8–403.3 s | 2.9 / 1.9 | 96 / 28 | head at limit 9%; outlier arms k1 cm (z +5.7) |
| `lawrence_1_6_6_t401-406_shift` | B | 4_lawrence_1_6_6 401.3–405.7 s | 10.0 / 3.6 | 109 / 34 | head at limit 9%; outlier arms k1 cm (z +7.4) |
| `lawrence_1_6_6_t404-410` | A | 4_lawrence_1_6_6 403.7–409.9 s | 6.2 / 0.8 | 68 / 21 | outlier arms k1 cm (z +3.9) |
| `lawrence_1_6_6_t415-420` | A | 4_lawrence_1_6_6 414.7–419.8 s | 3.0 / 0.9 | 79 / 20 | outlier arms k1 cm (z +3.6) |
| `lawrence_1_6_6_t418-422_shift` | B | 4_lawrence_1_6_6 417.8–422.2 s | 9.6 / 4.8 | 84 / 20 | outlier arms k1 cm (z +3.7) |
| `lawrence_1_6_6_t453-458_shift` | B | 4_lawrence_1_6_6 453.1–458.4 s | 24.8 / 14.6 | 59 / 14 | outlier knee max (z +5.2) |
| `lawrence_1_6_6_t465-470_shift` | B | 4_lawrence_1_6_6 465.0–469.5 s | 24.1 / 19.1 | 64 / 15 | K1 feet move 19 cm; head at limit 23%; leg at limit 13% |
| `lawrence_1_6_6_t474-478_shift` | B | 4_lawrence_1_6_6 473.8–477.8 s | 14.6 / 5.8 | 10 / 3 | head at limit 13% |
| `lawrence_1_6_6_t475-484` | A | 4_lawrence_1_6_6 474.9–484.2 s | 2.0 / 0.5 | 7 / 4 | head at limit 9% |
| `lawrence_1_6_6_t503-507_shift` | B | 4_lawrence_1_6_6 502.6–507.0 s | 7.0 / 5.3 | 64 / 17 | head at limit 40% |
| `lawrence_1_6_6_t517-521_shift` | B | 4_lawrence_1_6_6 516.6–520.9 s | 6.5 / 3.4 | 19 / 9 | outlier knee max (z +6.7) |
| `lawrence_1_6_6_t519-535` | A | 4_lawrence_1_6_6 518.9–534.7 s | 2.4 / 0.9 | 48 / 13 | outlier knee max (z +5.2) |
| `lawrence_1_6_6_t533-537_shift` | B | 4_lawrence_1_6_6 532.7–537.0 s | 13.0 / 6.8 | 82 / 22 | head at limit 7%; outlier arms k1 cm (z +4.3); outlier knee max (z +3.8) |
| `lawrence_1_6_6_t549-554_shift` | B | 4_lawrence_1_6_6 548.7–554.1 s | 10.6 / 9.8 | 42 / 13 | head at limit 20% |
| `lawrence_1_6_6_t88-98` | A | 4_lawrence_1_6_6 87.5–97.9 s | 7.9 / 12.7 | 59 / 18 | K1 feet move 13 cm; outlier knee max (z +3.5) |
| `lawrence_1_6_6_t95-99_shift` | B | 4_lawrence_1_6_6 95.3–99.3 s | 23.4 / 13.5 | 109 / 32 | head at limit 9%; outlier arms k1 cm (z +7.0) |
| `lawrence_1_7_7_t304-311_shift` | B | 4_lawrence_1_7_7 304.0–310.5 s | 11.4 / 3.9 | 8 / 2 | outlier knee max (z +3.6) |
| `lawrence_1_7_7_t327-334_shift` | B | 4_lawrence_1_7_7 326.8–334.2 s | 17.4 / 11.0 | 33 / 11 | head at limit 13% |
| `lawrence_1_7_7_t332-336` | A | 4_lawrence_1_7_7 332.2–336.2 s | 1.5 / 0.5 | 3 / 3 | head at limit 8% |
| `lawrence_1_7_7_t340-352` | A | 4_lawrence_1_7_7 339.8–352.0 s | 8.0 / 10.5 | 1 / 1 | K1 feet move 11 cm; head at limit 25% |
| `lawrence_1_7_7_t368-372_shift` | B | 4_lawrence_1_7_7 368.0–372.1 s | 21.9 / 14.9 | 22 / 8 | knee 62 deg; outlier knee max (z +8.7) |
| `lawrence_1_7_7_t412-417_shift` | B | 4_lawrence_1_7_7 412.2–417.2 s | 10.9 / 4.0 | 17 / 5 | outlier trunk drop (z +4.3) |
| `lawrence_1_7_7_t425-436` | A | 4_lawrence_1_7_7 424.6–435.5 s | 7.6 / 9.0 | 10 / 5 | K1 feet move 9 cm |
| `lawrence_1_7_7_t480-485` | A | 4_lawrence_1_7_7 480.1–485.5 s | 3.8 / 0.9 | 89 / 25 | head at limit 8%; outlier arms k1 cm (z +5.0); outlier trunk drop (z +3.8) |
| `lawrence_1_7_7_t520-533` | A | 4_lawrence_1_7_7 520.2–532.9 s | 1.7 / 1.3 | 1 / 1 | head at limit 27% |
| `lawrence_1_7_7_t536-543` | A | 4_lawrence_1_7_7 535.7–542.8 s | 2.5 / 2.6 | 8 / 4 | head at limit 5% |
| `lawrence_1_7_7_t540-544_shift` | B | 4_lawrence_1_7_7 540.1–544.1 s | 23.7 / 9.4 | 2 / 1 | head at limit 14% |
| `lawrence_1_7_7_t58-74` | A | 4_lawrence_1_7_7 58.0–74.1 s | 6.3 / 2.4 | 20 / 6 | head at limit 22% |
| `lawrence_1_7_7_t585-590_shift` | B | 4_lawrence_1_7_7 584.7–589.7 s | 24.7 / 18.4 | 65 / 19 | K1 feet move 18 cm; outlier knee max (z +6.8) |
| `lawrence_1_7_7_t9-15` | A | 4_lawrence_1_7_7 9.0–14.7 s | 3.6 / 1.6 | 1 / 1 | head at limit 53% |
| `lawrence_1_8_8_t12-17_shift` | B | 4_lawrence_1_8_8 12.0–16.5 s | 9.7 / 6.2 | 60 / 21 | outlier arms k1 cm (z +3.8) |
| `lawrence_1_8_8_t136-144_shift` | B | 4_lawrence_1_8_8 136.3–143.8 s | 17.6 / 10.4 | 55 / 15 | head at limit 8%; outlier knee max (z +4.9) |
| `lawrence_1_8_8_t142-156` | A | 4_lawrence_1_8_8 141.8–156.4 s | 8.4 / 3.2 | 49 / 14 | head at limit 14% |
| `lawrence_1_8_8_t185-189` | A | 4_lawrence_1_8_8 184.8–189.2 s | 3.1 / 1.9 | 7 / 2 | hand presses into leg 13 mm for 0.3 s (at 4.1 s) |
| `lawrence_1_8_8_t187-192_shift` | B | 4_lawrence_1_8_8 187.2–192.2 s | 12.3 / 4.0 | 29 / 7 | outlier knee max (z +4.8); hand presses into leg 27 mm for 0.9 s (at 1.7 s) |
| `lawrence_1_8_8_t211-215_shift` | B | 4_lawrence_1_8_8 210.7–215.1 s | 15.9 / 9.5 | 78 / 23 | head at limit 44%; outlier arms k1 cm (z +4.5) |
| `lawrence_1_8_8_t224-231` | A | 4_lawrence_1_8_8 224.3–231.0 s | 8.1 / 6.9 | 35 / 12 | head at limit 18% |
| `lawrence_1_8_8_t238-246_shift` | B | 4_lawrence_1_8_8 238.2–246.2 s | 24.9 / 10.2 | 58 / 15 | head at limit 28% |
| `lawrence_1_8_8_t239-246` | A | 4_lawrence_1_8_8 239.4–245.6 s | 1.9 / 0.4 | 49 / 13 | head at limit 37% |
| `lawrence_1_8_8_t26-35` | A | 4_lawrence_1_8_8 26.1–34.9 s | 2.6 / 0.5 | 26 / 9 | head at limit 14% |
| `lawrence_1_8_8_t273-278` | A | 4_lawrence_1_8_8 273.4–277.8 s | 2.9 / 1.4 | 25 / 8 | head at limit 5% |
| `lawrence_1_8_8_t403-408` | A | 4_lawrence_1_8_8 403.4–408.3 s | 0.6 / 0.5 | 40 / 9 | head at limit 7% |
| `lawrence_1_8_8_t406-412_shift` | B | 4_lawrence_1_8_8 406.3–412.1 s | 23.1 / 10.9 | 58 / 15 | head at limit 50%; outlier knee max (z +4.7) |
| `lawrence_1_8_8_t418-425_shift` | B | 4_lawrence_1_8_8 418.5–425.0 s | 24.5 / 18.3 | 70 / 20 | K1 feet move 18 cm; head at limit 11%; outlier arms k1 cm (z +3.7); outlier knee max (z +5.2) |
| `lawrence_1_8_8_t420-424` | A | 4_lawrence_1_8_8 419.7–424.3 s | 3.5 / 2.2 | 62 / 18 | head at limit 15% |
| `lawrence_1_8_8_t502-506_shift` | B | 4_lawrence_1_8_8 501.9–505.9 s | 18.2 / 11.9 | 1 / 1 | outlier knee max (z +4.1) |
| `lawrence_1_8_8_t55-70` | A | 4_lawrence_1_8_8 55.0–70.5 s | 3.4 / 1.9 | 9 / 3 | head at limit 7% |
| `lawrence_1_8_8_t6-14` | A | 4_lawrence_1_8_8 6.1–14.0 s | 3.7 / 1.1 | 64 / 22 | outlier arms k1 cm (z +4.3) |
| `lawrence_1_8_8_t627-632` | A | 4_lawrence_1_8_8 627.0–631.9 s | 9.9 / 5.3 | 30 / 10 | head at limit 10% |
| `lawrence_1_8_8_t95-100_shift` | B | 4_lawrence_1_8_8 94.9–99.6 s | 9.6 / 7.1 | 69 / 21 | outlier arms k1 cm (z +3.8) |
| `lawrence_1_9_9_t101-106` | A | 4_lawrence_1_9_9 100.9–105.9 s | 8.8 / 1.8 | 12 / 6 | head at limit 57% |
| `lawrence_1_9_9_t118-124_shift` | B | 4_lawrence_1_9_9 118.3–123.8 s | 18.8 / 10.9 | 23 / 10 | outlier knee max (z +4.0) |
| `lawrence_1_9_9_t124-131_shift` | B | 4_lawrence_1_9_9 124.4–131.0 s | 16.2 / 9.3 | 27 / 7 | outlier knee max (z +4.3) |
| `lawrence_1_9_9_t177-190_shift` | B | 4_lawrence_1_9_9 177.3–189.7 s | 16.5 / 11.0 | 14 / 5 | head at limit 9%; outlier knee max (z +6.1) |
| `lawrence_1_9_9_t208-213` | A | 4_lawrence_1_9_9 207.8–212.7 s | 3.0 / 4.8 | 64 / 18 | head at limit 13% |
| `lawrence_1_9_9_t213-219` | A | 4_lawrence_1_9_9 213.4–219.2 s | 7.8 / 5.0 | 45 / 12 | head at limit 5% |
| `lawrence_1_9_9_t244-256` | A | 4_lawrence_1_9_9 244.1–255.8 s | 5.3 / 1.6 | 26 / 8 | shoulder at limit 31% |
| `lawrence_1_9_9_t259-263_shift` | B | 4_lawrence_1_9_9 258.8–262.8 s | 18.3 / 12.7 | 70 / 21 | outlier arms k1 cm (z +3.9) |
| `lawrence_1_9_9_t269-281` | A | 4_lawrence_1_9_9 269.3–280.7 s | 4.4 / 3.8 | 4 / 3 | head at limit 25% |
| `lawrence_1_9_9_t290-294_shift` | B | 4_lawrence_1_9_9 290.0–294.1 s | 9.1 / 8.0 | 3 / 1 | head at limit 15% |
| `lawrence_1_9_9_t450-456_shift` | B | 4_lawrence_1_9_9 450.0–456.3 s | 13.6 / 11.9 | 59 / 18 | outlier knee max (z +4.2) |
| `lawrence_1_9_9_t467-471_shift` | B | 4_lawrence_1_9_9 466.9–470.9 s | 12.4 / 10.5 | 12 / 6 | head at limit 12% |
| `lawrence_1_9_9_t468-473` | A | 4_lawrence_1_9_9 467.8–473.3 s | 0.6 / 1.0 | 5 / 3 | head at limit 9% |
| `lawrence_1_9_9_t483-487_shift` | B | 4_lawrence_1_9_9 482.6–487.5 s | 18.3 / 14.2 | 2 / 2 | knee 69 deg; leg at limit 5%; outlier knee max (z +10.9) |
| `lawrence_1_9_9_t5-13` | A | 4_lawrence_1_9_9 5.1–12.7 s | 7.2 / 1.9 | 2 / 2 | head at limit 26% |
| `lawrence_1_9_9_t549-556_shift` | B | 4_lawrence_1_9_9 548.9–556.0 s | 21.0 / 15.0 | 37 / 11 | outlier knee max (z +3.6) |
| `lawrence_1_9_9_t558-563_shift` | B | 4_lawrence_1_9_9 558.1–563.1 s | 20.6 / 17.4 | 20 / 8 | head at limit 12%; hand presses into leg 26 mm for 1.5 s (at 3.5 s) |
| `lawrence_1_9_9_t565-578` | A | 4_lawrence_1_9_9 565.5–578.3 s | 4.0 / 8.7 | 19 / 5 | K1 feet move 9 cm; hand presses into leg 41 mm for 3.0 s (at 0.0 s) |
| `lawrence_1_9_9_t75-86` | A | 4_lawrence_1_9_9 75.1–85.7 s | 8.7 / 6.6 | 34 / 9 | outlier trunk drop (z +3.9); outlier knee max (z +5.9) |
| `li_0_103_103_t18-33` | A | 20_li_0_103_103 17.9–33.0 s | 11.6 / 7.3 | 37 / 11 | human steps |
| `li_0_103_103_t31-47_shift` | B | 20_li_0_103_103 31.0–47.3 s | 20.7 / 11.8 | 43 / 10 | outlier knee max (z +6.4) |
| `li_0_103_103_t63-69_shift` | B | 20_li_0_103_103 63.4–69.3 s | 16.5 / 9.6 | 51 / 13 | outlier knee max (z +5.1) |
| `li_0_103_103_t89-93_shift` | B | 20_li_0_103_103 88.8–92.8 s | 24.4 / 14.2 | 18 / 5 | outlier knee max (z +4.0) |
| `li_0_10_10_t58-62_shift` | B | 20_li_0_10_10 58.0–62.0 s | 24.8 / 14.3 | 25 / 7 | outlier knee max (z +3.9) |
| `li_0_1_1_t30-37_shift` | B | 20_li_0_1_1 29.8–36.5 s | 15.6 / 10.5 | 30 / 8 | outlier knee max (z +6.3) |
| `li_0_1_1_t51-68` | A | 20_li_0_1_1 51.2–67.8 s | 10.8 / 6.1 | 8 / 3 | human steps |
| `li_0_2_2_t17-30_shift` | B | 20_li_0_2_2 17.2–30.2 s | 18.0 / 10.1 | 21 / 5 | outlier knee max (z +4.6) |
| `li_0_2_2_t66-78_shift` | B | 20_li_0_2_2 65.5–78.5 s | 20.7 / 11.6 | 26 / 7 | outlier knee max (z +3.9) |
| `li_0_65_65_t11-20_shift` | B | 20_li_0_65_65 11.1–19.7 s | 22.5 / 12.4 | 32 / 9 | outlier knee max (z +7.2) |
| `li_0_65_65_t25-30_shift` | B | 20_li_0_65_65 25.1–29.7 s | 14.2 / 8.2 | 39 / 10 | outlier knee max (z +4.3) |
| `li_0_65_65_t32-45_shift` | B | 20_li_0_65_65 31.8–45.0 s | 23.8 / 12.9 | 34 / 9 | outlier knee max (z +6.0) |
| `li_0_65_65_t49-54_shift` | B | 20_li_0_65_65 48.6–54.1 s | 19.3 / 11.4 | 30 / 9 | outlier knee max (z +7.5) |
| `li_0_73_73_t26-38_shift` | B | 20_li_0_73_73 25.6–37.6 s | 18.6 / 10.5 | 27 / 7 | outlier knee max (z +4.0) |
| `li_0_81_81_t0-4_shift` | B | 20_li_0_81_81 0.0–4.0 s | 21.8 / 12.9 | 33 / 10 | outlier knee max (z +5.2) |
| `li_0_81_81_t2-7` | A | 20_li_0_81_81 1.8–6.6 s | 7.3 / 2.8 | 23 / 8 | outlier knee max (z +5.2) |
| `li_0_87_87_t0-7_shift` | B | 20_li_0_87_87 0.0–6.8 s | 23.8 / 13.6 | 28 / 9 | outlier knee max (z +5.7) |
| `li_0_87_87_t37-45_shift` | B | 20_li_0_87_87 37.4–45.0 s | 19.5 / 11.2 | 30 / 8 | outlier knee max (z +4.6) |
| `li_0_87_87_t88-92_shift` | B | 20_li_0_87_87 88.1–92.1 s | 25.1 / 14.3 | 21 / 6 | human steps; outlier knee max (z +4.7) |
| `li_0_95_95_t35-42_shift` | B | 20_li_0_95_95 34.6–42.5 s | 18.4 / 9.9 | 53 / 13 | outlier knee max (z +4.3) |
| `li_0_9_9_t0-8_shift` | B | 20_li_0_9_9 0.0–8.3 s | 20.4 / 11.6 | 19 / 5 | outlier knee max (z +7.1) |
| `li_0_9_9_t20-28_shift` | B | 20_li_0_9_9 20.0–27.7 s | 19.0 / 11.1 | 13 / 5 | outlier knee max (z +4.3) |
| `li_0_9_9_t59-67_shift` | B | 20_li_0_9_9 59.0–67.4 s | 16.3 / 9.4 | 16 / 5 | outlier knee max (z +4.4) |
| `li_1_1_1_t210-215_shift` | B | 20_li_1_1_1 209.9–214.5 s | 14.7 / 10.2 | 7 / 2 | outlier knee max (z +5.8) |
| `li_1_1_1_t216-226_shift` | B | 20_li_1_1_1 216.3–226.3 s | 13.4 / 6.8 | 18 / 5 | outlier knee max (z +6.7) |
| `li_1_1_1_t228-233_shift` | B | 20_li_1_1_1 227.8–233.1 s | 7.2 / 4.9 | 19 / 7 | outlier knee max (z +6.8) |
| `li_1_1_1_t247-251_shift` | B | 20_li_1_1_1 246.8–250.8 s | 10.4 / 5.9 | 15 / 5 | outlier knee max (z +4.3) |
| `li_1_1_1_t252-258_shift` | B | 20_li_1_1_1 251.5–257.6 s | 22.4 / 13.2 | 12 / 5 | outlier knee max (z +5.3) |
| `li_1_1_1_t261-266_shift` | B | 20_li_1_1_1 261.1–265.6 s | 11.2 / 6.2 | 22 / 7 | outlier knee max (z +4.2) |
| `li_1_1_1_t270-275_shift` | B | 20_li_1_1_1 270.4–274.9 s | 8.0 / 6.3 | 18 / 8 | outlier knee max (z +5.7) |
| `li_1_1_1_t334-338_shift` | B | 20_li_1_1_1 333.9–338.4 s | 14.1 / 8.1 | 13 / 4 | outlier knee max (z +4.4) |
| `li_1_1_1_t365-374_shift` | B | 20_li_1_1_1 365.4–373.5 s | 23.2 / 13.2 | 22 / 7 | outlier knee max (z +5.4) |
| `li_1_1_1_t431-436_shift` | B | 20_li_1_1_1 430.8–435.6 s | 14.5 / 7.3 | 48 / 13 | outlier knee max (z +3.7) |
| `li_1_1_1_t439-444_shift` | B | 20_li_1_1_1 439.5–444.5 s | 17.4 / 12.6 | 30 / 10 | knee 67 deg; outlier knee max (z +10.4); hand presses into leg 37 mm for 2.2 s (at 1.8 s) |
| `li_1_1_1_t442-456` | A | 20_li_1_1_1 442.5–456.5 s | 2.9 / 1.6 | 13 / 6 | hand presses into leg 31 mm for 0.9 s (at 0.0 s) |
| `li_1_1_1_t454-464_shift` | B | 20_li_1_1_1 454.5–464.3 s | 16.9 / 9.2 | 4 / 2 | outlier knee max (z +5.4) |
| `li_1_1_1_t486-500` | A | 20_li_1_1_1 486.2–500.3 s | 2.5 / 2.2 | 13 / 5 | hand presses into leg 56 mm for 3.8 s (at 8.0 s) |
| `li_1_1_1_t498-503_shift` | B | 20_li_1_1_1 498.3–502.9 s | 12.0 / 8.7 | 24 / 8 | hand presses into leg 34 mm for 3.4 s (at 0.7 s) |
| `li_1_1_1_t501-520` | A | 20_li_1_1_1 500.9–519.6 s | 2.3 / 0.7 | 28 / 10 | hand presses into leg 26 mm for 1.4 s (at 0.0 s) |
| `li_1_1_1_t532-537_shift` | B | 20_li_1_1_1 532.0–536.7 s | 11.9 / 5.3 | 10 / 4 | outlier knee max (z +4.9) |
| `li_1_1_1_t618-624_shift` | B | 20_li_1_1_1 618.2–623.6 s | 19.2 / 10.6 | 55 / 19 | outlier knee max (z +4.6) |
| `li_1_2_2_t107-115_shift` | B | 20_li_1_2_2 106.6–115.4 s | 15.7 / 8.0 | 7 / 3 | outlier knee max (z +7.0) |
| `li_1_2_2_t130-135_shift` | B | 20_li_1_2_2 129.7–135.4 s | 21.4 / 12.4 | 7 / 3 | outlier knee max (z +4.5) |
| `li_1_2_2_t14-21_shift` | B | 20_li_1_2_2 14.4–21.1 s | 13.2 / 8.0 | 13 / 6 | outlier knee max (z +4.2) |
| `li_1_2_2_t148-155_shift` | B | 20_li_1_2_2 148.0–155.4 s | 30.3 / 18.5 | 18 / 5 | human steps; K1 feet move 19 cm; outlier knee max (z +3.7) |
| `li_1_2_2_t211-217_shift` | B | 20_li_1_2_2 211.2–217.0 s | 23.3 / 13.4 | 13 / 5 | outlier knee max (z +3.5) |
| `li_1_2_2_t22-30_shift` | B | 20_li_1_2_2 21.9–29.5 s | 20.3 / 11.5 | 11 / 5 | outlier knee max (z +4.8) |
| `li_1_2_2_t225-230_shift` | B | 20_li_1_2_2 225.4–230.1 s | 16.3 / 12.7 | 12 / 4 | knee 61 deg; outlier knee max (z +8.3) |
| `li_1_2_2_t236-240_shift` | B | 20_li_1_2_2 235.8–240.3 s | 13.6 / 8.0 | 14 / 7 | outlier knee max (z +3.6) |
| `li_1_2_2_t271-279_shift` | B | 20_li_1_2_2 270.8–279.4 s | 17.1 / 10.4 | 10 / 4 | outlier knee max (z +4.7) |
| `li_1_2_2_t297-313_shift` | B | 20_li_1_2_2 297.1–313.2 s | 15.9 / 12.1 | 18 / 7 | outlier knee max (z +6.5) |
| `li_1_2_2_t316-330` | A | 20_li_1_2_2 316.1–329.7 s | 8.5 / 2.0 | 12 / 5 | outlier knee max (z +5.1) |
| `li_1_2_2_t33-41_shift` | B | 20_li_1_2_2 33.1–40.7 s | 27.7 / 16.1 | 8 / 3 | human steps; outlier knee max (z +6.8) |
| `li_1_2_2_t341-346_shift` | B | 20_li_1_2_2 341.3–345.9 s | 15.2 / 11.2 | 22 / 8 | outlier knee max (z +5.6) |
| `li_1_2_2_t353-360_shift` | B | 20_li_1_2_2 352.9–360.2 s | 21.0 / 11.3 | 16 / 5 | outlier knee max (z +6.4) |
| `li_1_2_2_t410-415_shift` | B | 20_li_1_2_2 410.4–415.2 s | 14.0 / 8.5 | 16 / 7 | outlier knee max (z +7.1) |
| `li_1_2_2_t416-424_shift` | B | 20_li_1_2_2 416.0–424.0 s | 24.5 / 14.3 | 14 / 6 | outlier knee max (z +5.8) |
| `li_1_2_2_t432-441_shift` | B | 20_li_1_2_2 432.5–441.1 s | 17.3 / 10.4 | 12 / 5 | outlier knee max (z +4.5) |
| `li_1_2_2_t445-454_shift` | B | 20_li_1_2_2 445.2–453.7 s | 27.3 / 15.5 | 16 / 5 | human steps; outlier knee max (z +7.6) |
| `li_1_2_2_t457-466_shift` | B | 20_li_1_2_2 457.0–465.5 s | 18.7 / 9.8 | 25 / 7 | outlier knee max (z +4.7) |
| `li_1_2_2_t472-481_shift` | B | 20_li_1_2_2 472.3–480.6 s | 29.0 / 17.0 | 8 / 3 | human steps; outlier knee max (z +7.3) |
| `li_1_2_2_t484-493_shift` | B | 20_li_1_2_2 483.6–492.7 s | 18.2 / 13.1 | 12 / 4 | outlier knee max (z +7.5) |
| `li_1_2_2_t521-526_shift` | B | 20_li_1_2_2 520.6–526.0 s | 41.2 / 24.2 | 8 / 3 | human steps; K1 feet move 24 cm |
| `li_1_2_2_t526-534_shift` | B | 20_li_1_2_2 526.0–533.7 s | 24.5 / 14.4 | 22 / 7 | outlier knee max (z +6.1) |
| `li_1_2_2_t539-543_shift` | B | 20_li_1_2_2 539.0–543.0 s | 25.2 / 14.3 | 16 / 6 | human steps |
| `li_1_2_2_t543-548_shift` | B | 20_li_1_2_2 543.0–548.0 s | 13.6 / 10.8 | 36 / 10 | outlier knee max (z +4.1) |
| `li_1_2_2_t591-595_shift` | B | 20_li_1_2_2 590.7–595.3 s | 12.0 / 7.2 | 9 / 4 | outlier knee max (z +3.8) |
| `li_1_2_2_t595-603_shift` | B | 20_li_1_2_2 595.5–602.7 s | 23.8 / 13.4 | 11 / 4 | outlier knee max (z +5.5) |
| `li_1_2_2_t611-619_shift` | B | 20_li_1_2_2 611.0–618.8 s | 21.3 / 14.0 | 12 / 5 | outlier knee max (z +6.2) |
| `li_1_2_2_t91-98_shift` | B | 20_li_1_2_2 91.3–98.3 s | 25.0 / 14.4 | 14 / 4 | outlier knee max (z +6.5) |
| `li_1_2_2_t98-104_shift` | B | 20_li_1_2_2 98.3–104.5 s | 17.4 / 9.8 | 8 / 3 | outlier knee max (z +3.6) |
| `li_1_3_3_t122-134_shift` | B | 20_li_1_3_3 122.2–134.4 s | 18.9 / 10.9 | 15 / 5 | outlier knee max (z +4.4) |
| `li_1_3_3_t148-152_shift` | B | 20_li_1_3_3 147.8–152.4 s | 13.9 / 8.7 | 25 / 9 | head at limit 9%; outlier knee max (z +5.0) |
| `li_1_3_3_t16-26_shift` | B | 20_li_1_3_3 15.6–26.3 s | 15.4 / 8.6 | 12 / 6 | outlier knee max (z +5.5) |
| `li_1_3_3_t191-196_shift` | B | 20_li_1_3_3 191.4–196.0 s | 14.3 / 9.7 | 18 / 8 | outlier knee max (z +5.3) |
| `li_1_3_3_t220-231` | A | 20_li_1_3_3 220.5–231.1 s | 10.0 / 5.1 | 27 / 9 | human steps |
| `li_1_3_3_t229-238_shift` | B | 20_li_1_3_3 229.1–238.0 s | 14.0 / 9.3 | 21 / 7 | outlier knee max (z +6.2) |
| `li_1_3_3_t268-272_shift` | B | 20_li_1_3_3 268.1–272.1 s | 24.8 / 14.7 | 20 / 7 | outlier knee max (z +5.4) |
| `li_1_3_3_t30-34_shift` | B | 20_li_1_3_3 29.8–33.8 s | 25.1 / 14.5 | 13 / 5 | human steps; outlier knee max (z +3.6) |
| `li_1_3_3_t34-40_shift` | B | 20_li_1_3_3 33.8–39.9 s | 14.5 / 10.8 | 22 / 7 | outlier knee max (z +5.1) |
| `li_1_3_3_t366-375_shift` | B | 20_li_1_3_3 366.1–374.6 s | 17.2 / 9.6 | 28 / 9 | outlier knee max (z +4.1) |
| `li_1_3_3_t392-396_shift` | B | 20_li_1_3_3 391.8–396.3 s | 8.1 / 4.6 | 20 / 10 | outlier knee max (z +5.3) |
| `li_1_3_3_t394-400` | A | 20_li_1_3_3 394.3–400.0 s | 4.1 / 0.8 | 42 / 21 | outlier arms k1 cm (z +3.9) |
| `li_1_3_3_t398-406_shift` | B | 20_li_1_3_3 398.0–405.6 s | 16.8 / 9.4 | 24 / 11 | outlier knee max (z +6.0) |
| `li_1_3_3_t41-56_shift` | B | 20_li_1_3_3 41.5–55.8 s | 20.7 / 11.5 | 20 / 6 | outlier knee max (z +7.1) |
| `li_1_3_3_t416-421_shift` | B | 20_li_1_3_3 415.9–420.6 s | 14.4 / 11.5 | 40 / 10 | outlier knee max (z +7.4) |
| `li_1_3_3_t436-441_shift` | B | 20_li_1_3_3 436.1–440.7 s | 12.0 / 9.0 | 37 / 12 | outlier knee max (z +3.8) |
| `li_1_3_3_t441-448_shift` | B | 20_li_1_3_3 440.9–448.0 s | 25.3 / 14.6 | 37 / 12 | human steps; outlier knee max (z +7.9) |
| `li_1_3_3_t454-458_shift` | B | 20_li_1_3_3 453.6–458.3 s | 16.3 / 11.9 | 10 / 3 | outlier knee max (z +4.6) |
| `li_1_3_3_t458-462_shift` | B | 20_li_1_3_3 458.4–462.4 s | 28.6 / 17.3 | 20 / 7 | human steps |
| `li_1_3_3_t495-499_shift` | B | 20_li_1_3_3 494.5–499.1 s | 17.5 / 11.0 | 26 / 9 | outlier knee max (z +3.9) |
| `li_1_3_3_t513-529` | A | 20_li_1_3_3 513.2–529.2 s | 11.5 / 4.9 | 25 / 9 | human steps |
| `li_1_3_3_t536-545_shift` | B | 20_li_1_3_3 536.4–545.2 s | 15.9 / 11.0 | 39 / 10 | outlier knee max (z +4.5) |
| `li_1_3_3_t57-71_shift` | B | 20_li_1_3_3 57.0–71.1 s | 23.3 / 13.3 | 15 / 5 | outlier knee max (z +6.8) |
| `li_1_3_3_t575-579_shift` | B | 20_li_1_3_3 575.1–579.1 s | 24.9 / 14.4 | 34 / 9 | outlier knee max (z +3.9) |
| `li_1_3_3_t579-584_shift` | B | 20_li_1_3_3 579.1–584.3 s | 19.2 / 11.8 | 19 / 5 | outlier knee max (z +5.1) |
| `li_1_3_3_t618-626_shift` | B | 20_li_1_3_3 618.4–626.4 s | 16.3 / 9.1 | 21 / 9 | outlier knee max (z +6.2) |
| `li_1_3_3_t75-94_shift` | B | 20_li_1_3_3 74.7–94.3 s | 22.2 / 12.7 | 12 / 6 | outlier knee max (z +7.0) |
| `lu_0_103_103_t0-4_shift` | B | 13_lu_0_103_103 0.0–4.0 s | 17.5 / 9.1 | 16 / 7 | outlier knee max (z +6.4) |
| `lu_0_103_103_t19-30_shift` | B | 13_lu_0_103_103 19.4–30.2 s | 15.1 / 7.5 | 36 / 17 | outlier knee max (z +4.5) |
| `lu_0_103_103_t24-28` | A | 13_lu_0_103_103 24.3–28.5 s | 8.7 / 3.5 | 33 / 17 | outlier knee max (z +4.8) |
| `lu_0_103_103_t33-38_shift` | B | 13_lu_0_103_103 32.8–38.4 s | 24.2 / 12.9 | 33 / 13 | knee 62 deg; outlier knee max (z +8.6) |
| `lu_0_103_103_t40-58_shift` | B | 13_lu_0_103_103 40.5–58.4 s | 12.9 / 7.7 | 35 / 16 | outlier knee max (z +6.7) |
| `lu_0_103_103_t60-69_shift` | B | 13_lu_0_103_103 60.1–69.2 s | 28.0 / 14.9 | 34 / 14 | human steps; outlier trunk drop (z +4.1); outlier knee max (z +4.7) |
| `lu_0_103_103_t9-19_shift` | B | 13_lu_0_103_103 8.6–19.4 s | 23.4 / 15.0 | 26 / 9 | outlier knee max (z +7.8) |
| `lu_0_104_104_t19-33_shift` | B | 13_lu_0_104_104 19.4–33.3 s | 24.9 / 14.3 | 26 / 12 | knee 71 deg; outlier knee max (z +11.6) |
| `lu_0_104_104_t35-40_shift` | B | 13_lu_0_104_104 35.1–39.8 s | 9.9 / 5.2 | 31 / 14 | outlier knee max (z +3.9) |
| `lu_0_104_104_t38-48` | A | 13_lu_0_104_104 37.8–47.8 s | 9.9 / 4.8 | 23 / 12 | outlier knee max (z +7.4) |
| `lu_0_104_104_t48-56` | A | 13_lu_0_104_104 47.8–56.2 s | 9.8 / 5.1 | 34 / 16 | outlier knee max (z +3.7) |
| `lu_0_104_104_t56-73` | A | 13_lu_0_104_104 56.2–72.8 s | 8.7 / 5.7 | 31 / 12 | outlier knee max (z +5.3) |
| `lu_0_104_104_t6-19_shift` | B | 13_lu_0_104_104 5.8–18.8 s | 18.2 / 8.4 | 26 / 11 | outlier knee max (z +6.7) |
| `lu_0_111_111_t0-5_shift` | B | 13_lu_0_111_111 0.0–4.5 s | 11.9 / 6.8 | 39 / 17 | outlier knee max (z +3.8) |
| `lu_0_111_111_t10-25` | A | 13_lu_0_111_111 9.8–25.1 s | 8.9 / 3.9 | 31 / 13 | elbow bend at limit 7% |
| `lu_0_111_111_t23-41_shift` | B | 13_lu_0_111_111 23.1–41.2 s | 22.0 / 14.8 | 28 / 10 | knee 62 deg; outlier knee max (z +8.8) |
| `lu_0_111_111_t44-51_shift` | B | 13_lu_0_111_111 43.6–51.4 s | 13.0 / 5.3 | 37 / 12 | outlier knee max (z +3.9) |
| `lu_0_111_111_t7-12_shift` | B | 13_lu_0_111_111 7.4–11.8 s | 8.9 / 4.6 | 36 / 18 | elbow bend at limit 19% |
| `lu_0_112_112_t26-40_shift` | B | 13_lu_0_112_112 26.0–40.0 s | 19.0 / 11.8 | 51 / 16 | knee 61 deg; outlier knee max (z +8.3) |
| `lu_0_112_112_t40-54_shift` | B | 13_lu_0_112_112 40.0–54.1 s | 9.8 / 4.9 | 30 / 10 | outlier knee max (z +5.7) |
| `lu_0_112_112_t8-22` | A | 13_lu_0_112_112 7.9–21.7 s | 7.9 / 5.8 | 36 / 12 | outlier knee max (z +6.8) |
| `lu_0_11_11_t44-50_shift` | B | 13_lu_0_11_11 43.7–50.4 s | 12.3 / 6.6 | 34 / 13 | outlier knee max (z +4.0) |
| `lu_0_12_12_t26-31_shift` | B | 13_lu_0_12_12 26.1–30.6 s | 8.0 / 3.3 | 38 / 12 | shoulder at limit 7% |
| `lu_0_12_12_t34-38_shift` | B | 13_lu_0_12_12 33.5–38.2 s | 13.4 / 9.8 | 49 / 17 | outlier knee max (z +5.8) |
| `lu_0_12_12_t36-46` | A | 13_lu_0_12_12 36.2–46.3 s | 0.3 / 0.4 | 34 / 15 | shoulder at limit 11% |
| `lu_0_12_12_t46-56` | A | 13_lu_0_12_12 46.3–56.4 s | 0.8 / 0.8 | 28 / 11 | shoulder at limit 13% |
| `lu_0_14_14_t40-45_shift` | B | 13_lu_0_14_14 39.5–45.4 s | 22.0 / 11.7 | 19 / 8 | outlier knee max (z +5.0) |
| `lu_0_15_15_t23-29_shift` | B | 13_lu_0_15_15 22.8–29.1 s | 20.3 / 11.2 | 43 / 17 | outlier knee max (z +3.8) |
| `lu_0_15_15_t61-66_shift` | B | 13_lu_0_15_15 61.2–65.8 s | 14.7 / 8.8 | 29 / 13 | outlier knee max (z +4.2) |
| `lu_0_15_15_t70-74_shift` | B | 13_lu_0_15_15 69.5–74.3 s | 15.1 / 7.7 | 30 / 11 | outlier knee max (z +4.4) |
| `lu_0_15_15_t72-77` | A | 13_lu_0_15_15 72.3–76.9 s | 2.1 / 0.6 | 29 / 12 | shoulder at limit 9% |
| `lu_0_16_16_t20-26` | A | 13_lu_0_16_16 20.2–25.5 s | 9.6 / 7.8 | 40 / 16 | elbow bend at limit 15% |
| `lu_0_16_16_t22-26_shift` | B | 13_lu_0_16_16 22.4–26.4 s | 11.8 / 7.9 | 39 / 15 | elbow bend at limit 20% |
| `lu_0_16_16_t27-44` | A | 13_lu_0_16_16 27.1–43.8 s | 0.6 / 0.4 | 29 / 11 | elbow bend at limit 7% |
| `lu_0_16_16_t42-48_shift` | B | 13_lu_0_16_16 41.8–47.9 s | 22.5 / 11.9 | 24 / 9 | elbow bend at limit 17% |
| `lu_0_1_1_t24-31_shift` | B | 13_lu_0_1_1 24.5–31.1 s | 19.0 / 9.8 | 33 / 11 | outlier knee max (z +4.6) |
| `lu_0_1_1_t31-35_shift` | B | 13_lu_0_1_1 31.4–35.4 s | 17.9 / 9.5 | 31 / 14 | outlier knee max (z +3.6) |
| `lu_0_1_1_t51-58_shift` | B | 13_lu_0_1_1 50.8–58.5 s | 18.4 / 10.9 | 30 / 14 | outlier knee max (z +3.7) |
| `lu_0_2_2_t36-40_shift` | B | 13_lu_0_2_2 35.6–40.1 s | 8.1 / 4.6 | 26 / 11 | shoulder at limit 8% |
| `lu_0_3_3_t31-39_shift` | B | 13_lu_0_3_3 31.4–38.8 s | 16.9 / 10.2 | 34 / 11 | outlier knee max (z +5.8) |
| `lu_0_3_3_t43-48_shift` | B | 13_lu_0_3_3 42.7–47.5 s | 16.6 / 10.7 | 31 / 12 | outlier knee max (z +4.2) |
| `lu_0_4_4_t73-80_shift` | B | 13_lu_0_4_4 73.4–79.8 s | 32.5 / 17.1 | 31 / 9 | human steps; outlier knee max (z +5.5) |
| `lu_0_5_5_t14-22_shift` | B | 13_lu_0_5_5 13.9–21.7 s | 16.6 / 8.3 | 25 / 10 | outlier knee max (z +3.6) |
| `lu_0_5_5_t43-59` | A | 13_lu_0_5_5 42.8–58.6 s | 6.8 / 4.9 | 31 / 13 | shoulder at limit 7% |
| `lu_0_65_65_t0-5_shift` | B | 13_lu_0_65_65 0.0–4.9 s | 21.8 / 11.0 | 40 / 13 | outlier knee max (z +7.4) |
| `lu_0_65_65_t23-27_shift` | B | 13_lu_0_65_65 22.8–27.3 s | 19.6 / 10.3 | 29 / 11 | outlier knee max (z +6.3) |
| `lu_0_65_65_t32-49_shift` | B | 13_lu_0_65_65 32.4–48.8 s | 19.3 / 9.3 | 44 / 15 | outlier knee max (z +7.8) |
| `lu_0_65_65_t7-13_shift` | B | 13_lu_0_65_65 7.3–13.5 s | 24.4 / 13.7 | 39 / 17 | outlier knee max (z +6.0) |
| `lu_0_66_66_t16-20_shift` | B | 13_lu_0_66_66 16.2–20.4 s | 21.8 / 11.5 | 47 / 19 | outlier knee max (z +4.1) |
| `lu_0_66_66_t22-28_shift` | B | 13_lu_0_66_66 22.4–28.0 s | 13.5 / 7.3 | 52 / 17 | outlier knee max (z +7.4) |
| `lu_0_66_66_t36-42_shift` | B | 13_lu_0_66_66 35.9–41.9 s | 10.5 / 6.8 | 41 / 16 | outlier knee max (z +4.7) |
| `lu_0_66_66_t42-47_shift` | B | 13_lu_0_66_66 41.9–46.8 s | 19.5 / 10.0 | 44 / 16 | outlier knee max (z +5.3) |
| `lu_0_66_66_t49-57_shift` | B | 13_lu_0_66_66 48.6–56.8 s | 19.2 / 10.4 | 48 / 16 | knee 60 deg; outlier knee max (z +8.1) |
| `lu_0_66_66_t6-16_shift` | B | 13_lu_0_66_66 6.2–16.2 s | 24.8 / 14.0 | 39 / 15 | outlier knee max (z +5.1) |
| `lu_0_6_6_t12-24` | A | 13_lu_0_6_6 11.9–23.7 s | 10.0 / 5.2 | 36 / 10 | human steps |
| `lu_0_6_6_t73-79_shift` | B | 13_lu_0_6_6 73.0–78.8 s | 7.3 / 3.1 | 23 / 8 | outlier knee max (z +5.5) |
| `lu_0_73_73_t14-20` | A | 13_lu_0_73_73 14.2–20.1 s | 6.5 / 2.9 | 51 / 21 | outlier arms k1 cm (z +3.9) |
| `lu_0_73_73_t18-25_shift` | B | 13_lu_0_73_73 18.1–25.5 s | 13.8 / 7.6 | 58 / 21 | outlier arms k1 cm (z +3.8) |
| `lu_0_73_73_t23-31` | A | 13_lu_0_73_73 23.5–31.0 s | 5.4 / 2.9 | 65 / 24 | outlier arms k1 cm (z +4.6) |
| `lu_0_73_73_t29-36_shift` | B | 13_lu_0_73_73 29.0–35.6 s | 16.7 / 8.6 | 50 / 15 | outlier knee max (z +4.8) |
| `lu_0_74_74_t46-51_shift` | B | 13_lu_0_74_74 46.1–51.0 s | 18.2 / 11.1 | 65 / 22 | outlier arms k1 cm (z +4.2); outlier knee max (z +8.0) |
| `lu_0_82_82_t60-80` | A | 13_lu_0_82_82 59.7–79.7 s | 10.6 / 6.2 | 20 / 5 | human steps |
| `lu_0_87_87_t14-21_shift` | B | 13_lu_0_87_87 13.8–20.5 s | 30.2 / 15.2 | 30 / 11 | human steps; outlier knee max (z +5.3) |
| `lu_0_87_87_t19-26` | A | 13_lu_0_87_87 18.5–26.2 s | 9.7 / 5.1 | 33 / 10 | outlier knee max (z +4.2) |
| `lu_0_87_87_t26-32_shift` | B | 13_lu_0_87_87 26.1–32.3 s | 23.3 / 11.7 | 31 / 10 | outlier knee max (z +3.6) |
| `lu_0_87_87_t33-38_shift` | B | 13_lu_0_87_87 33.2–37.7 s | 11.9 / 5.0 | 21 / 8 | outlier knee max (z +4.4) |
| `lu_0_87_87_t43-62_shift` | B | 13_lu_0_87_87 42.9–61.9 s | 25.2 / 12.3 | 32 / 12 | human steps; outlier knee max (z +4.5) |
| `lu_0_87_87_t6-13_shift` | B | 13_lu_0_87_87 5.6–13.2 s | 21.3 / 11.3 | 33 / 11 | outlier knee max (z +5.8) |
| `lu_0_87_87_t67-73_shift` | B | 13_lu_0_87_87 66.8–73.2 s | 28.0 / 13.3 | 25 / 12 | human steps; outlier knee max (z +6.8) |
| `lu_0_88_88_t18-29_shift` | B | 13_lu_0_88_88 18.3–28.8 s | 21.3 / 11.8 | 40 / 10 | outlier knee max (z +6.0) |
| `lu_0_88_88_t31-41_shift` | B | 13_lu_0_88_88 30.7–41.0 s | 21.8 / 12.1 | 30 / 10 | outlier knee max (z +5.2) |
| `lu_0_88_88_t41-51_shift` | B | 13_lu_0_88_88 41.0–51.4 s | 29.1 / 16.2 | 28 / 8 | human steps; outlier knee max (z +5.5) |
| `lu_0_88_88_t49-61` | A | 13_lu_0_88_88 49.4–61.0 s | 9.4 / 3.5 | 34 / 9 | outlier knee max (z +5.5) |
| `lu_0_88_88_t8-18_shift` | B | 13_lu_0_88_88 7.8–18.3 s | 21.1 / 11.6 | 44 / 13 | outlier knee max (z +8.0) |
| `lu_0_8_8_t30-35_shift` | B | 13_lu_0_8_8 30.3–34.8 s | 16.6 / 9.4 | 37 / 12 | outlier knee max (z +5.2) |
| `lu_0_8_8_t38-43_shift` | B | 13_lu_0_8_8 38.4–43.3 s | 24.3 / 15.2 | 35 / 11 | outlier knee max (z +6.0) |
| `lu_0_8_8_t58-64_shift` | B | 13_lu_0_8_8 58.0–63.6 s | 24.9 / 13.5 | 37 / 10 | outlier knee max (z +4.2) |
| `lu_0_95_95_t0-16_shift` | B | 13_lu_0_95_95 0.0–16.0 s | 20.5 / 11.6 | 33 / 12 | knee 62 deg; outlier knee max (z +8.6) |
| `lu_0_95_95_t16-32_shift` | B | 13_lu_0_95_95 16.0–31.9 s | 17.7 / 9.6 | 40 / 13 | outlier knee max (z +6.6) |
| `lu_0_95_95_t32-48_shift` | B | 13_lu_0_95_95 31.9–47.9 s | 24.0 / 11.2 | 32 / 13 | knee 62 deg; outlier knee max (z +8.5) |
| `lu_0_95_95_t46-53` | A | 13_lu_0_95_95 45.9–52.5 s | 9.2 / 5.1 | 38 / 15 | outlier knee max (z +3.9) |
| `lu_0_95_95_t51-55_shift` | B | 13_lu_0_95_95 50.5–54.8 s | 16.9 / 10.1 | 35 / 9 | outlier knee max (z +3.8) |
| `lu_0_96_96_t0-13_shift` | B | 13_lu_0_96_96 0.0–12.8 s | 17.5 / 9.8 | 23 / 7 | outlier knee max (z +5.0) |
| `lu_0_96_96_t19-31_shift` | B | 13_lu_0_96_96 19.3–31.3 s | 17.2 / 10.6 | 35 / 11 | outlier knee max (z +7.9) |
| `lu_0_96_96_t29-34` | A | 13_lu_0_96_96 29.3–33.9 s | 8.8 / 8.3 | 39 / 11 | K1 feet move 8 cm; outlier knee max (z +7.8) |
| `lu_0_96_96_t32-50_shift` | B | 13_lu_0_96_96 31.9–49.8 s | 22.0 / 14.0 | 38 / 13 | knee 68 deg; outlier knee max (z +10.7) |
| `lu_0_9_9_t43-54` | A | 13_lu_0_9_9 42.7–53.8 s | 11.3 / 6.4 | 33 / 12 | human steps |
| `lu_0_9_9_t52-56_shift` | B | 13_lu_0_9_9 51.8–56.4 s | 16.3 / 10.4 | 32 / 10 | outlier knee max (z +6.3) |
| `lu_1_1_1_t107-120` | A | 13_lu_1_1_1 106.8–120.3 s | 12.2 / 6.3 | 22 / 10 | human steps |
| `lu_1_1_1_t146-150_shift` | B | 13_lu_1_1_1 146.1–150.1 s | 23.9 / 12.4 | 20 / 10 | outlier knee max (z +4.1) |
| `lu_1_1_1_t153-157` | A | 13_lu_1_1_1 152.8–157.2 s | 8.8 / 5.0 | 75 / 24 | shoulder at limit 17%; outlier arms k1 cm (z +4.8) |
| `lu_1_1_1_t205-214_shift` | B | 13_lu_1_1_1 205.4–213.9 s | 27.4 / 13.1 | 15 / 6 | human steps; outlier knee max (z +5.3) |
| `lu_1_1_1_t215-220` | A | 13_lu_1_1_1 214.7–220.5 s | 5.4 / 3.0 | 20 / 7 | shoulder at limit 9% |
| `lu_1_1_1_t225-230_shift` | B | 13_lu_1_1_1 224.8–230.3 s | 17.4 / 11.6 | 23 / 10 | outlier knee max (z +5.0) |
| `lu_1_1_1_t381-386_shift` | B | 13_lu_1_1_1 381.3–385.5 s | 22.8 / 11.0 | 29 / 12 | shoulder at limit 12%; outlier knee max (z +5.0) |
| `lu_1_1_1_t384-390` | A | 13_lu_1_1_1 383.5–389.7 s | 3.4 / 3.5 | 32 / 13 | shoulder at limit 59% |
| `lu_1_1_1_t410-414_shift` | B | 13_lu_1_1_1 410.4–414.4 s | 10.3 / 2.5 | 22 / 7 | outlier knee max (z +3.7) |
| `lu_1_1_1_t458-471_shift` | B | 13_lu_1_1_1 458.5–471.3 s | 27.1 / 15.9 | 26 / 9 | human steps; outlier knee max (z +5.3) |
| `lu_1_1_1_t479-484_shift` | B | 13_lu_1_1_1 479.3–483.9 s | 8.9 / 6.6 | 32 / 12 | shoulder at limit 49% |
| `lu_1_1_1_t482-489` | A | 13_lu_1_1_1 481.9–489.2 s | 2.5 / 0.9 | 22 / 9 | shoulder at limit 24% |
| `lu_1_1_1_t490-503` | A | 13_lu_1_1_1 489.6–503.0 s | 6.9 / 1.4 | 12 / 5 | outlier knee max (z +4.7) |
| `lu_1_1_1_t512-517_shift` | B | 13_lu_1_1_1 512.5–516.9 s | 6.6 / 3.6 | 18 / 7 | outlier knee max (z +3.7) |
| `lu_1_1_1_t56-66_shift` | B | 13_lu_1_1_1 55.9–65.7 s | 22.3 / 12.9 | 25 / 8 | outlier knee max (z +5.2) |
| `lu_1_1_1_t566-572_shift` | B | 13_lu_1_1_1 566.3–572.0 s | 25.4 / 14.4 | 24 / 6 | human steps; outlier knee max (z +5.0) |
| `lu_1_1_1_t596-601_shift` | B | 13_lu_1_1_1 596.3–600.8 s | 13.4 / 8.8 | 28 / 7 | outlier knee max (z +3.7) |
| `lu_1_1_1_t609-613_shift` | B | 13_lu_1_1_1 608.9–612.9 s | 17.3 / 12.9 | 33 / 8 | outlier knee max (z +4.0) |
| `lu_1_1_1_t621-625_shift` | B | 13_lu_1_1_1 621.1–625.2 s | 9.6 / 7.7 | 18 / 8 | outlier knee max (z +3.7) |
| `lu_1_2_2_t141-145_shift` | B | 13_lu_1_2_2 140.9–145.0 s | 11.8 / 3.9 | 29 / 12 | outlier knee max (z +5.0) |
| `lu_1_2_2_t174-179_shift` | B | 13_lu_1_2_2 173.9–179.0 s | 18.7 / 10.0 | 19 / 9 | outlier knee max (z +4.2) |
| `lu_1_2_2_t180-186_shift` | B | 13_lu_1_2_2 180.4–186.0 s | 23.8 / 14.3 | 25 / 8 | outlier knee max (z +3.8) |
| `lu_1_2_2_t184-193` | A | 13_lu_1_2_2 184.0–193.3 s | 9.3 / 4.9 | 19 / 8 | outlier knee max (z +3.6) |
| `lu_1_2_2_t190-194_shift` | B | 13_lu_1_2_2 190.0–194.0 s | 11.2 / 6.0 | 17 / 7 | outlier knee max (z +3.6) |
| `lu_1_2_2_t220-228_shift` | B | 13_lu_1_2_2 220.4–227.7 s | 19.6 / 11.0 | 23 / 10 | outlier knee max (z +6.1) |
| `lu_1_2_2_t272-279_shift` | B | 13_lu_1_2_2 271.6–278.7 s | 22.8 / 14.9 | 23 / 7 | outlier knee max (z +3.6) |
| `lu_1_2_2_t333-338_shift` | B | 13_lu_1_2_2 333.4–337.9 s | 11.3 / 7.9 | 20 / 5 | outlier knee max (z +6.0) |
| `lu_1_2_2_t360-364_shift` | B | 13_lu_1_2_2 359.9–364.5 s | 14.3 / 7.9 | 20 / 8 | outlier knee max (z +3.6) |
| `lu_1_2_2_t380-385_shift` | B | 13_lu_1_2_2 380.2–384.7 s | 15.8 / 8.5 | 16 / 7 | outlier knee max (z +4.3) |
| `lu_1_2_2_t393-399` | A | 13_lu_1_2_2 392.9–399.5 s | 9.7 / 8.4 | 23 / 9 | K1 feet move 8 cm |
| `lu_1_2_2_t404-409_shift` | B | 13_lu_1_2_2 404.0–408.6 s | 12.7 / 8.5 | 6 / 3 | outlier knee max (z +4.0) |
| `lu_1_2_2_t45-50_shift` | B | 13_lu_1_2_2 45.0–49.5 s | 12.2 / 7.1 | 31 / 9 | outlier knee max (z +4.0) |
| `lu_1_2_2_t461-469_shift` | B | 13_lu_1_2_2 461.4–469.1 s | 25.7 / 15.5 | 20 / 8 | human steps; outlier knee max (z +4.0) |
| `lu_1_2_2_t473-479_shift` | B | 13_lu_1_2_2 473.4–479.1 s | 24.6 / 14.5 | 36 / 8 | outlier knee max (z +3.9) |
| `lu_1_2_2_t52-56_shift` | B | 13_lu_1_2_2 51.6–56.2 s | 17.0 / 8.6 | 25 / 10 | outlier knee max (z +4.9) |
| `lu_1_2_2_t624-630` | A | 13_lu_1_2_2 624.0–629.8 s | 9.8 / 2.0 | 35 / 9 | outlier knee max (z +5.0) |
| `lu_1_2_2_t78-82_shift` | B | 13_lu_1_2_2 78.2–82.2 s | 11.3 / 2.0 | 28 / 16 | outlier knee max (z +4.3) |
| `lu_1_2_2_t87-91_shift` | B | 13_lu_1_2_2 86.8–90.8 s | 16.1 / 11.5 | 15 / 6 | outlier knee max (z +4.9) |
| `lu_1_3_3_t116-124_shift` | B | 13_lu_1_3_3 116.2–124.1 s | 19.8 / 13.7 | 23 / 5 | outlier knee max (z +5.8) |
| `lu_1_3_3_t178-190_shift` | B | 13_lu_1_3_3 177.5–189.7 s | 29.5 / 16.6 | 26 / 10 | human steps |
| `lu_1_3_3_t207-218` | A | 13_lu_1_3_3 207.4–217.7 s | 5.4 / 2.6 | 30 / 13 | shoulder at limit 6% |
| `lu_1_3_3_t22-26_shift` | B | 13_lu_1_3_3 21.6–26.1 s | 14.8 / 7.1 | 21 / 10 | outlier knee max (z +4.1) |
| `lu_1_3_3_t268-272` | A | 13_lu_1_3_3 267.7–271.8 s | 9.9 / 2.7 | 19 / 7 | outlier knee max (z +4.8) |
| `lu_1_3_3_t270-276_shift` | B | 13_lu_1_3_3 269.8–275.7 s | 9.4 / 3.2 | 25 / 7 | leg at limit 5%; outlier knee max (z +6.3) |
| `lu_1_3_3_t345-354_shift` | B | 13_lu_1_3_3 344.6–353.6 s | 24.2 / 11.7 | 17 / 6 | outlier knee max (z +5.7) |
| `lu_1_3_3_t393-405` | A | 13_lu_1_3_3 393.1–405.4 s | 9.6 / 5.5 | 15 / 6 | outlier knee max (z +3.9) |
| `lu_1_3_3_t42-46_shift` | B | 13_lu_1_3_3 41.8–46.5 s | 13.0 / 6.3 | 18 / 6 | outlier knee max (z +3.9) |
| `lu_1_3_3_t497-505_shift` | B | 13_lu_1_3_3 496.7–505.5 s | 16.9 / 8.6 | 31 / 7 | outlier knee max (z +5.4) |
| `lu_1_3_3_t519-528_shift` | B | 13_lu_1_3_3 518.6–527.8 s | 17.6 / 10.8 | 24 / 7 | outlier knee max (z +4.6) |
| `lu_1_3_3_t597-603_shift` | B | 13_lu_1_3_3 597.2–602.9 s | 25.2 / 13.1 | 31 / 7 | human steps; outlier knee max (z +3.7) |
| `lu_1_3_3_t67-77_shift` | B | 13_lu_1_3_3 66.7–77.0 s | 35.0 / 20.5 | 25 / 9 | human steps; K1 feet move 21 cm; outlier knee max (z +5.5) |
| `luqi_0_103_103_t31-36` | A | 22_luqi_0_103_103 31.3–36.2 s | 1.5 / 0.3 | 23 / 7 | shoulder at limit 10%; hand presses into leg 24 mm for 2.6 s (at 1.5 s) |
| `luqi_0_103_103_t64-70` | A | 22_luqi_0_103_103 64.3–69.8 s | 1.7 / 0.3 | 18 / 7 | self-collision left_hand_collision / trunk_collision 0.9 s (at 2.4 s, 9 mm) |
| `luqi_0_104_104_t1-7` | A | 22_luqi_0_104_104 0.9–6.6 s | 2.7 / 0.9 | 18 / 5 | self-collision right_hand_collision / trunk_collision 0.2 s (at 3.5 s, 13 mm) |
| `luqi_0_104_104_t48-53` | A | 22_luqi_0_104_104 47.9–52.9 s | 1.9 / 1.8 | 13 / 4 | left arm behind body 5 cm (human's in front) |
| `luqi_0_112_112_t30-38` | A | 22_luqi_0_112_112 30.2–38.1 s | 1.6 / 0.9 | 19 / 7 | hand presses into leg 30 mm for 0.5 s (at 0.0 s) |
| `luqi_0_1_1_t5-10` | A | 22_luqi_0_1_1 5.1–9.6 s | 2.8 / 1.4 | 19 / 6 | hand presses into leg 25 mm for 0.3 s (at 4.2 s) |
| `luqi_0_1_1_t69-73` | A | 22_luqi_0_1_1 68.5–72.8 s | 3.1 / 1.7 | 45 / 13 | self-collision left_hand_collision / trunk_collision 0.2 s (at 0.5 s, 7 mm) |
| `luqi_0_2_2_t15-29_shift` | B | 22_luqi_0_2_2 15.3–28.6 s | 22.3 / 11.7 | 16 / 5 | outlier knee max (z +3.5) |
| `luqi_0_2_2_t8-13_shift` | B | 22_luqi_0_2_2 8.0–12.6 s | 16.0 / 2.2 | 15 / 6 | outlier knee max (z +5.4) |
| `luqi_0_3_3_t27-32` | A | 22_luqi_0_3_3 26.7–32.5 s | 2.2 / 0.8 | 15 / 5 | hand presses into leg 18 mm for 0.6 s (at 4.5 s) |
| `luqi_0_3_3_t42-52` | A | 22_luqi_0_3_3 41.8–52.5 s | 9.0 / 1.7 | 17 / 5 | self-collision right_hand_collision / trunk_collision 1.1 s (at 3.8 s, 14 mm) |
| `luqi_0_3_3_t59-65_shift` | B | 22_luqi_0_3_3 59.1–64.8 s | 13.9 / 5.6 | 16 / 6 | outlier knee max (z +4.8) |
| `luqi_0_3_3_t67-74_shift` | B | 22_luqi_0_3_3 67.4–73.9 s | 17.8 / 2.5 | 13 / 4 | outlier knee max (z +4.0) |
| `luqi_0_4_4_t14-18` | A | 22_luqi_0_4_4 13.9–17.9 s | 3.0 / 0.9 | 11 / 3 | self-collision right_hand_collision / trunk_collision 0.2 s (at 0.0 s, 16 mm) |
| `luqi_0_4_4_t48-56` | A | 22_luqi_0_4_4 47.8–55.6 s | 8.3 / 0.9 | 8 / 3 | self-collision left_hand_collision / trunk_collision 3.4 s (at 2.3 s, 10 mm) |
| `luqi_0_4_4_t56-65` | A | 22_luqi_0_4_4 56.1–65.3 s | 3.1 / 1.8 | 14 / 4 | self-collision right_hand_collision / trunk_collision 0.4 s (at 6.8 s, 17 mm) |
| `luqi_0_4_4_t6-16_shift` | B | 22_luqi_0_4_4 5.8–15.9 s | 15.2 / 8.2 | 14 / 5 | outlier knee max (z +7.3); self-collision right_hand_collision / trunk_collision 1.1 s (at 7.2 s, 21 mm) |
| `luqi_0_4_4_t72-78` | A | 22_luqi_0_4_4 72.0–77.7 s | 4.2 / 1.8 | 13 / 4 | hand presses into leg 16 mm for 0.1 s (at 5.4 s) |
| `luqi_0_65_65_t34-44_shift` | B | 22_luqi_0_65_65 34.2–43.7 s | 10.2 / 7.7 | 19 / 6 | shoulder at limit 13%; self-collision right_hand_collision / trunk_collision 0.5 s (at 7.5 s, 9 mm) |
| `luqi_0_65_65_t37-41` | A | 22_luqi_0_65_65 36.8–40.8 s | 1.6 / 0.2 | 18 / 5 | shoulder at limit 15% |
| `luqi_0_65_65_t42-48` | A | 22_luqi_0_65_65 41.7–48.1 s | 3.3 / 0.7 | 19 / 8 | shoulder at limit 5%; self-collision right_hand_collision / trunk_collision 0.5 s (at 0.0 s, 9 mm) |
| `luqi_0_65_65_t53-58` | A | 22_luqi_0_65_65 53.1–57.8 s | 3.5 / 0.9 | 9 / 3 | right arm behind body 5 cm (human's in front) |
| `luqi_0_6_6_t46-52_shift` | B | 22_luqi_0_6_6 46.1–51.9 s | 13.3 / 5.2 | 17 / 5 | outlier knee max (z +5.0) |
| `luqi_0_7_7_t13-24` | A | 22_luqi_0_7_7 13.3–24.4 s | 2.3 / 1.5 | 14 / 5 | hand presses into leg 27 mm for 1.9 s (at 5.7 s) |
| `luqi_0_87_87_t37-41_shift` | B | 22_luqi_0_87_87 36.7–41.1 s | 18.9 / 3.0 | 28 / 10 | outlier knee max (z +6.5) |
| `luqi_0_88_88_t74-83_shift` | B | 22_luqi_0_88_88 74.0–82.5 s | 22.2 / 7.3 | 30 / 9 | outlier knee max (z +7.4); hand presses into leg 11 mm for 0.2 s (at 7.0 s) |
| `luqi_0_88_88_t81-88` | A | 22_luqi_0_88_88 80.5–87.6 s | 2.7 / 1.0 | 24 / 7 | hand presses into leg 11 mm for 0.2 s (at 0.4 s) |
| `luqi_0_8_8_t10-14` | A | 22_luqi_0_8_8 9.9–14.3 s | 3.5 / 2.0 | 21 / 7 | self-collision right_hand_collision / trunk_collision 0.2 s (at 2.5 s, 18 mm) |
| `luqi_0_8_8_t28-33` | A | 22_luqi_0_8_8 28.3–32.8 s | 2.5 / 0.6 | 19 / 6 | self-collision left_hand_collision / trunk_collision 0.7 s (at 0.0 s, 11 mm) |
| `luqi_0_8_8_t5-12_shift` | B | 22_luqi_0_8_8 5.2–11.9 s | 16.3 / 5.5 | 12 / 4 | outlier knee max (z +4.9); hand presses into leg 10 mm for 0.1 s (at 4.1 s) |
| `luqi_1_1_1_t100-118` | A | 22_luqi_1_1_1 100.1–117.7 s | 1.7 / 0.3 | 9 / 3 | elbow bend at limit 8% |
| `luqi_1_1_1_t116-121_shift` | B | 22_luqi_1_1_1 115.7–120.6 s | 17.7 / 7.5 | 10 / 2 | outlier knee max (z +4.5) |
| `luqi_1_1_1_t134-149` | A | 22_luqi_1_1_1 133.9–149.3 s | 1.5 / 0.6 | 8 / 3 | self-collision left_hand_collision / trunk_collision 0.7 s (at 3.1 s, 7 mm) |
| `luqi_1_1_1_t147-154_shift` | B | 22_luqi_1_1_1 147.3–154.4 s | 11.0 / 8.8 | 6 / 2 | self-collision right_hand_collision / trunk_collision 2.2 s (at 1.8 s, 23 mm) |
| `luqi_1_1_1_t152-169` | A | 22_luqi_1_1_1 152.4–168.9 s | 2.0 / 0.3 | 10 / 4 | self-collision left_hand_collision / trunk_collision 0.3 s (at 2.1 s, 7 mm) |
| `luqi_1_1_1_t186-204` | A | 22_luqi_1_1_1 186.2–203.6 s | 3.8 / 0.8 | 8 / 2 | self-collision right_hand_collision / trunk_collision 0.2 s (at 6.4 s, 9 mm) |
| `luqi_1_1_1_t23-41` | A | 22_luqi_1_1_1 23.3–40.7 s | 0.3 / 0.3 | 6 / 3 | outlier knee max (z -4.3) |
| `luqi_1_1_1_t262-276` | A | 22_luqi_1_1_1 262.0–275.8 s | 2.7 / 3.8 | 9 / 5 | self-collision right_hand_collision / trunk_collision 0.3 s (at 5.0 s, 7 mm) |
| `luqi_1_1_1_t274-282_shift` | B | 22_luqi_1_1_1 273.8–282.1 s | 37.0 / 15.4 | 9 / 3 | human steps; outlier knee max (z +6.2); hand presses into leg 16 mm for 0.3 s (at 7.5 s) |
| `luqi_1_1_1_t280-288` | A | 22_luqi_1_1_1 280.1–288.1 s | 2.3 / 6.1 | 4 / 1 | hand presses into leg 5 mm for 0.1 s (at 1.2 s) |
| `luqi_1_1_1_t306-322` | A | 22_luqi_1_1_1 305.9–322.2 s | 1.8 / 0.3 | 15 / 5 | hand presses into leg 13 mm for 0.4 s (at 10.4 s) |
| `luqi_1_1_1_t322-332` | A | 22_luqi_1_1_1 322.2–331.5 s | 1.6 / 0.3 | 19 / 7 | self-collision head_2_collision / right_hand_end_collision 1.5 s (at 2.0 s, 25 mm) |
| `luqi_1_1_1_t330-340_shift` | B | 22_luqi_1_1_1 329.5–340.5 s | 20.3 / 10.9 | 5 / 2 | outlier knee max (z +5.5) |
| `luqi_1_1_1_t354-360_shift` | B | 22_luqi_1_1_1 353.5–360.5 s | 20.8 / 10.3 | 9 / 3 | outlier knee max (z +6.9) |
| `luqi_1_1_1_t382-386_shift` | B | 22_luqi_1_1_1 381.6–386.1 s | 12.2 / 7.6 | 4 / 1 | outlier knee max (z +6.0) |
| `luqi_1_1_1_t426-432_shift` | B | 22_luqi_1_1_1 426.2–432.4 s | 20.1 / 10.5 | 9 / 4 | outlier knee max (z +4.9) |
| `luqi_1_1_1_t430-449` | A | 22_luqi_1_1_1 430.4–449.4 s | 2.4 / 0.6 | 9 / 4 | self-collision right_hand_collision / trunk_collision 0.2 s (at 16.6 s, 11 mm) |
| `luqi_1_1_1_t466-471_shift` | B | 22_luqi_1_1_1 466.4–471.3 s | 14.7 / 8.7 | 12 / 3 | shoulder at limit 5%; outlier knee max (z +6.5) |
| `luqi_1_1_1_t549-561` | A | 22_luqi_1_1_1 549.1–560.8 s | 0.8 / 0.3 | 15 / 7 | self-collision right_hand_collision / trunk_collision 0.8 s (at 8.3 s, 19 mm) |
| `luqi_1_1_1_t56-61_shift` | B | 22_luqi_1_1_1 56.0–60.7 s | 7.8 / 6.6 | 25 / 10 | outlier knee max (z +4.5) |
| `luqi_1_1_1_t561-572` | A | 22_luqi_1_1_1 560.8–572.5 s | 0.9 / 0.3 | 11 / 4 | shoulder at limit 20%; outlier knee max (z -4.2); self-collision right_hand_collision / trunk_collision 0.9 s (at 1.9 s, 19 mm) |
| `luqi_1_1_1_t570-575_shift` | B | 22_luqi_1_1_1 570.5–574.9 s | 6.7 / 1.2 | 12 / 3 | shoulder at limit 32%; self-collision right_hand_collision / waist_collision 1.0 s (at 2.1 s, 14 mm) |
| `luqi_1_1_1_t573-591` | A | 22_luqi_1_1_1 572.9–590.8 s | 4.0 / 7.0 | 6 / 2 | self-collision right_hand_collision / trunk_collision 1.1 s (at 9.6 s, 11 mm); hand presses into leg 6 mm for 0.2 s (at 0.7 s) |
| `luqi_1_1_1_t59-70` | A | 22_luqi_1_1_1 58.7–70.2 s | 2.5 / 0.7 | 12 / 4 | self-collision left_hand_collision / trunk_collision 4.9 s (at 5.0 s, 23 mm) |
| `luqi_1_1_1_t597-601_shift` | B | 22_luqi_1_1_1 596.7–600.7 s | 20.7 / 15.0 | 6 / 2 | outlier knee max (z +4.1) |
| `luqi_1_1_1_t6-23` | A | 22_luqi_1_1_1 6.0–23.3 s | 8.0 / 7.4 | 9 / 4 | elbow bend at limit 6% |
| `luqi_1_1_1_t68-75_shift` | B | 22_luqi_1_1_1 68.2–75.4 s | 22.4 / 10.7 | 14 / 4 | outlier knee max (z +3.8); self-collision left_hand_collision / trunk_collision 0.3 s (at 0.0 s, 10 mm) |
| `luqi_1_1_1_t86-92_shift` | B | 22_luqi_1_1_1 85.9–91.8 s | 24.8 / 12.0 | 19 / 5 | outlier knee max (z +4.8); hand presses into leg 26 mm for 0.3 s (at 3.3 s) |
| `luqi_1_1_1_t90-100` | A | 22_luqi_1_1_1 89.8–99.6 s | 3.6 / 2.2 | 14 / 5 | hand presses into leg 33 mm for 3.5 s (at 3.5 s) |
| `luqi_1_2_2_t182-189_shift` | B | 22_luqi_1_2_2 181.8–189.3 s | 7.9 / 2.2 | 7 / 3 | self-collision right_hand_collision / trunk_collision 0.8 s (at 3.6 s, 11 mm) |
| `luqi_1_2_2_t248-267` | A | 22_luqi_1_2_2 248.4–267.4 s | 3.9 / 6.6 | 7 / 3 | shoulder at limit 15% |
| `luqi_1_2_2_t288-293_shift` | B | 22_luqi_1_2_2 287.9–293.3 s | 12.5 / 1.0 | 12 / 3 | elbow bend at limit 26% |
| `luqi_1_2_2_t291-300` | A | 22_luqi_1_2_2 291.3–300.4 s | 2.4 / 0.4 | 8 / 3 | elbow bend at limit 22% |
| `luqi_1_2_2_t315-320` | A | 22_luqi_1_2_2 315.0–319.5 s | 2.1 / 1.5 | 2 / 1 | leg at limit 90% |
| `luqi_1_2_2_t318-325_shift` | B | 22_luqi_1_2_2 317.5–325.4 s | 23.4 / 7.7 | 3 / 2 | leg at limit 27% |
| `luqi_1_2_2_t335-351` | A | 22_luqi_1_2_2 335.3–351.4 s | 7.9 / 11.7 | 4 / 2 | K1 feet move 12 cm |
| `luqi_1_2_2_t353-363` | A | 22_luqi_1_2_2 352.7–362.9 s | 1.9 / 0.8 | 27 / 9 | shoulder at limit 29%; elbow bend at limit 8%; self-collision left_hand_end_collision / trunk_collision 1.4 s (at 4.6 s, 22 mm) |
| `luqi_1_2_2_t37-42_shift` | B | 22_luqi_1_2_2 37.3–42.0 s | 9.7 / 8.1 | 13 / 4 | outlier knee max (z +4.4) |
| `luqi_1_2_2_t401-417` | A | 22_luqi_1_2_2 401.1–416.8 s | 5.4 / 1.1 | 7 / 3 | hand presses into leg 8 mm for 0.8 s (at 1.3 s) |
| `luqi_1_2_2_t5-22` | A | 22_luqi_1_2_2 5.1–22.2 s | 2.4 / 0.5 | 9 / 4 | elbow bend at limit 6% |
| `luqi_1_2_2_t541-557` | A | 22_luqi_1_2_2 540.6–557.4 s | 9.5 / 5.3 | 9 / 4 | elbow bend at limit 7% |
| `luqi_1_2_2_t608-614` | A | 22_luqi_1_2_2 607.6–613.7 s | 4.9 / 9.8 | 5 / 2 | K1 feet move 10 cm |
| `luqi_1_2_2_t614-620` | A | 22_luqi_1_2_2 614.1–619.9 s | 6.0 / 3.3 | 11 / 5 | elbow bend at limit 32% |
| `luqi_1_2_2_t87-104` | A | 22_luqi_1_2_2 87.3–104.4 s | 8.0 / 4.3 | 12 / 5 | self-collision left_hand_collision / trunk_collision 2.8 s (at 14.3 s, 23 mm) |
| `luqi_1_3_3_t179-183_shift` | B | 22_luqi_1_3_3 179.1–183.1 s | 12.8 / 14.5 | 8 / 2 | hand presses into leg 17 mm for 2.8 s (at 1.2 s) |
| `luqi_1_3_3_t180-189` | A | 22_luqi_1_3_3 179.9–189.0 s | 5.9 / 10.0 | 4 / 1 | K1 feet move 10 cm; hand presses into leg 23 mm for 8.3 s (at 0.3 s) |
| `luqi_1_3_3_t273-281_shift` | B | 22_luqi_1_3_3 273.2–280.7 s | 16.1 / 7.3 | 8 / 2 | hand presses into leg 8 mm for 0.2 s (at 2.3 s) |
| `luqi_1_3_3_t358-369_shift` | B | 22_luqi_1_3_3 357.7–368.9 s | 18.4 / 12.2 | 19 / 6 | shoulder at limit 7%; hand presses into leg 14 mm for 0.3 s (at 5.8 s) |
| `luqi_1_3_3_t380-385_shift` | B | 22_luqi_1_3_3 380.0–385.3 s | 19.8 / 2.6 | 6 / 2 | hand presses into leg 23 mm for 2.3 s (at 0.0 s) |
| `luqi_1_3_3_t428-445` | A | 22_luqi_1_3_3 428.4–444.6 s | 2.0 / 0.3 | 10 / 4 | self-collision right_hand_collision / trunk_collision 0.7 s (at 14.6 s, 13 mm) |
| `luqi_1_3_3_t445-461` | A | 22_luqi_1_3_3 444.6–460.9 s | 9.8 / 3.6 | 7 / 3 | self-collision right_hand_collision / trunk_collision 2.4 s (at 1.0 s, 11 mm) |
| `luqi_1_3_3_t563-568_shift` | B | 22_luqi_1_3_3 563.2–567.6 s | 17.3 / 6.7 | 16 / 4 | outlier knee max (z +4.9) |
| `luqi_1_3_3_t598-605` | A | 22_luqi_1_3_3 598.3–604.6 s | 10.0 / 0.7 | 8 / 3 | elbow bend at limit 11% |
| `luqi_1_3_3_t603-608_shift` | B | 22_luqi_1_3_3 602.6–608.3 s | 9.4 / 6.2 | 42 / 16 | elbow bend at limit 17% |
| `miranda_0_116_116_t53-71` | A | 9_miranda_0_116_116 53.1–70.8 s | 0.7 / 0.9 | 11 / 4 | outlier knee max (z +4.3) |
| `miranda_0_12_12_t35-52` | A | 9_miranda_0_12_12 34.9–52.3 s | 0.5 / 0.4 | 28 / 10 | elbow bend at limit 8% |
| `miranda_0_17_17_t53-58_shift` | B | 9_miranda_0_17_17 53.3–57.8 s | 9.9 / 5.5 | 16 / 6 | leg at limit 5%; outlier knee max (z +7.5) |
| `miranda_0_18_18_t1-10` | A | 9_miranda_0_18_18 1.5–9.9 s | 6.5 / 1.1 | 34 / 9 | leg at limit 5% |
| `miranda_0_19_19_t17-34` | A | 9_miranda_0_19_19 16.9–33.9 s | 7.4 / 4.2 | 20 / 6 | elbow bend at limit 6% |
| `miranda_0_20_20_t23-29` | A | 9_miranda_0_20_20 23.4–29.3 s | 2.9 / 0.8 | 29 / 8 | outlier knee max (z +4.7) |
| `miranda_0_20_20_t9-13_shift` | B | 9_miranda_0_20_20 8.8–12.8 s | 24.9 / 13.0 | 13 / 3 | outlier knee max (z +4.7) |
| `miranda_0_30_30_t50-62` | A | 9_miranda_0_30_30 50.2–61.8 s | 8.0 / 1.5 | 16 / 5 | outlier knee max (z +5.7) |
| `miranda_0_32_32_t0-4_shift` | B | 9_miranda_0_32_32 0.0–4.0 s | 23.6 / 12.0 | 17 / 6 | outlier knee max (z +4.7) |
| `miranda_0_32_32_t2-21` | A | 9_miranda_0_32_32 1.6–21.2 s | 7.9 / 4.7 | 21 / 7 | elbow bend at limit 10% |
| `miranda_0_33_33_t0-5_shift` | B | 9_miranda_0_33_33 0.0–5.0 s | 23.2 / 11.5 | 27 / 8 | outlier knee max (z +5.9) |
| `miranda_0_33_33_t51-55_shift` | B | 9_miranda_0_33_33 51.0–55.0 s | 19.6 / 9.3 | 58 / 13 | outlier knee max (z +3.8) |
| `miranda_0_37_37_t0-15` | A | 9_miranda_0_37_37 0.0–14.6 s | 4.7 / 2.4 | 38 / 12 | outlier knee max (z +3.7) |
| `miranda_0_37_37_t13-21_shift` | B | 9_miranda_0_37_37 12.6–20.8 s | 20.2 / 10.6 | 34 / 9 | head at limit 7%; outlier knee max (z +7.8) |
| `miranda_0_37_37_t28-43` | A | 9_miranda_0_37_37 28.0–42.8 s | 1.0 / 0.5 | 31 / 9 | elbow bend at limit 8% |
| `miranda_0_41_41_t0-9_shift` | B | 9_miranda_0_41_41 0.0–8.9 s | 15.3 / 7.1 | 29 / 9 | knee 62 deg; outlier knee max (z +8.6) |
| `miranda_0_44_44_t32-45` | A | 9_miranda_0_44_44 31.7–45.5 s | 10.0 / 2.2 | 15 / 4 | outlier knee max (z +5.9) |
| `miranda_0_44_44_t43-48_shift` | B | 9_miranda_0_44_44 43.5–48.1 s | 10.2 / 7.1 | 14 / 3 | outlier knee max (z +6.9) |
| `miranda_0_46_46_t48-52_shift` | B | 9_miranda_0_46_46 47.6–51.6 s | 24.6 / 13.0 | 11 / 3 | outlier knee max (z +4.5) |
| `miranda_0_46_46_t52-60` | A | 9_miranda_0_46_46 51.5–60.1 s | 9.4 / 2.7 | 62 / 16 | outlier knee max (z +3.5) |
| `miranda_0_46_46_t58-64_shift` | B | 9_miranda_0_46_46 58.1–63.8 s | 12.8 / 2.0 | 47 / 14 | knee 60 deg; outlier knee max (z +8.2) |
| `miranda_0_47_47_t0-4_shift` | B | 9_miranda_0_47_47 0.0–4.0 s | 20.0 / 11.4 | 15 / 5 | outlier knee max (z +4.1) |
| `miranda_0_67_67_t0-14` | A | 9_miranda_0_67_67 0.0–13.9 s | 1.6 / 0.4 | 39 / 12 | elbow bend at limit 9% |
| `miranda_0_68_68_t41-45_shift` | B | 9_miranda_0_68_68 40.7–44.7 s | 14.2 / 7.1 | 31 / 8 | elbow bend at limit 11% |
| `miranda_0_76_76_t39-43_shift` | B | 9_miranda_0_76_76 39.4–43.4 s | 24.7 / 13.3 | 35 / 9 | outlier knee max (z +4.3) |
| `miranda_0_80_80_t19-38` | A | 9_miranda_0_80_80 18.9–37.8 s | 1.0 / 0.6 | 30 / 9 | outlier knee max (z +4.3) |
| `miranda_0_89_89_t29-43` | A | 9_miranda_0_89_89 28.7–43.1 s | 10.1 / 4.7 | 9 / 3 | human steps |
| `miranda_0_91_91_t14-23_shift` | B | 9_miranda_0_91_91 13.7–22.6 s | 14.5 / 10.8 | 24 / 6 | knee 62 deg; outlier knee max (z +8.8) |
| `miranda_0_95_95_t15-19_shift` | B | 9_miranda_0_95_95 14.6–19.0 s | 5.9 / 2.0 | 30 / 8 | outlier knee max (z +5.2) |
| `miranda_0_95_95_t17-33` | A | 9_miranda_0_95_95 17.0–32.9 s | 5.9 / 1.8 | 17 / 5 | outlier knee max (z +5.2) |
| `miranda_0_98_98_t44-48_shift` | B | 9_miranda_0_98_98 43.8–47.8 s | 21.1 / 11.9 | 17 / 4 | outlier knee max (z +3.8) |
| `miranda_0_99_99_t0-4_shift` | B | 9_miranda_0_99_99 0.0–4.3 s | 15.9 / 7.7 | 38 / 14 | outlier knee max (z +3.7) |
| `miranda_1_10_10_t140-160` | A | 9_miranda_1_10_10 140.2–160.0 s | 3.0 / 1.5 | 10 / 5 | elbow bend at limit 12% |
| `miranda_1_10_10_t160-180` | A | 9_miranda_1_10_10 160.0–179.8 s | 0.6 / 0.8 | 8 / 5 | elbow bend at limit 7% |
| `miranda_1_10_10_t17-21_shift` | B | 9_miranda_1_10_10 16.8–21.3 s | 15.1 / 7.9 | 12 / 5 | outlier knee max (z +4.9) |
| `miranda_1_10_10_t200-219` | A | 9_miranda_1_10_10 199.5–219.3 s | 12.1 / 6.6 | 16 / 5 | human steps |
| `miranda_1_10_10_t430-449` | A | 9_miranda_1_10_10 430.2–448.8 s | 16.0 / 10.7 | 11 / 3 | human steps; K1 feet move 11 cm |
| `miranda_1_10_10_t561-578` | A | 9_miranda_1_10_10 560.9–578.5 s | 8.6 / 4.6 | 22 / 7 | outlier knee max (z +3.7) |
| `miranda_1_10_10_t595-609` | A | 9_miranda_1_10_10 594.6–609.3 s | 2.7 / 2.5 | 32 / 11 | head at limit 7%; elbow bend at limit 12%; outlier trunk drop (z +3.7) |
| `miranda_1_10_10_t75-83_shift` | B | 9_miranda_1_10_10 74.9–83.0 s | 14.8 / 7.6 | 24 / 6 | outlier trunk drop (z +3.7); outlier knee max (z +5.9) |
| `miranda_1_11_11_t166-171_shift` | B | 9_miranda_1_11_11 166.0–171.1 s | 14.7 / 7.2 | 7 / 2 | outlier knee max (z +4.7) |
| `miranda_1_11_11_t192-211` | A | 9_miranda_1_11_11 191.9–210.7 s | 5.7 / 1.2 | 14 / 6 | elbow bend at limit 13% |
| `miranda_1_11_11_t264-282` | A | 9_miranda_1_11_11 264.5–281.8 s | 1.6 / 0.4 | 13 / 4 | elbow bend at limit 7% |
| `miranda_1_11_11_t336-340_shift` | B | 9_miranda_1_11_11 335.7–339.7 s | 21.2 / 10.7 | 14 / 5 | outlier knee max (z +4.4) |
| `miranda_1_11_11_t350-368` | A | 9_miranda_1_11_11 349.7–368.1 s | 1.5 / 0.5 | 22 / 6 | outlier knee max (z +5.3) |
| `miranda_1_11_11_t39-57` | A | 9_miranda_1_11_11 39.0–56.6 s | 8.8 / 4.2 | 9 / 4 | head at limit 7% |
| `miranda_1_11_11_t424-442` | A | 9_miranda_1_11_11 423.6–442.1 s | 0.9 / 0.6 | 27 / 12 | head at limit 14%; outlier knee max (z +6.6) |
| `miranda_1_11_11_t442-461` | A | 9_miranda_1_11_11 442.1–460.6 s | 0.8 / 0.5 | 20 / 6 | elbow bend at limit 10% |
| `miranda_1_11_11_t489-504` | A | 9_miranda_1_11_11 488.8–503.7 s | 3.0 / 3.0 | 12 / 5 | elbow bend at limit 34% |
| `miranda_1_11_11_t504-519` | A | 9_miranda_1_11_11 503.7–518.6 s | 0.2 / 0.6 | 7 / 2 | elbow bend at limit 24% |
| `miranda_1_11_11_t57-74` | A | 9_miranda_1_11_11 56.6–74.1 s | 8.8 / 4.4 | 12 / 3 | outlier knee max (z +4.3) |
| `miranda_1_11_11_t83-87_shift` | B | 9_miranda_1_11_11 82.6–87.3 s | 14.2 / 8.6 | 16 / 6 | elbow bend at limit 42%; outlier knee max (z +3.8) |
| `miranda_1_11_11_t85-103` | A | 9_miranda_1_11_11 85.3–102.8 s | 6.7 / 5.6 | 7 / 3 | head at limit 8%; elbow bend at limit 16% |
| `miranda_1_12_12_t101-105_shift` | B | 9_miranda_1_12_12 100.8–105.1 s | 12.4 / 8.8 | 33 / 9 | knee 65 deg; outlier knee max (z +9.6) |
| `miranda_1_12_12_t341-345_shift` | B | 9_miranda_1_12_12 340.9–345.0 s | 11.4 / 6.7 | 29 / 9 | outlier knee max (z +6.0) |
| `miranda_1_12_12_t364-381` | A | 9_miranda_1_12_12 363.5–381.4 s | 3.2 / 2.0 | 26 / 7 | elbow bend at limit 7% |
| `miranda_1_12_12_t469-474_shift` | B | 9_miranda_1_12_12 468.8–474.1 s | 21.8 / 10.9 | 10 / 3 | outlier knee max (z +3.7) |
| `miranda_1_1_1_t214-223` | A | 9_miranda_1_1_1 214.2–222.7 s | 0.9 / 0.8 | 26 / 10 | elbow bend at limit 28% |
| `miranda_1_1_1_t249-254_shift` | B | 9_miranda_1_1_1 249.0–254.5 s | 14.1 / 7.9 | 25 / 7 | elbow bend at limit 8% |
| `miranda_1_1_1_t417-436` | A | 9_miranda_1_1_1 417.2–435.5 s | 3.2 / 1.5 | 29 / 12 | upper-arm twist at limit 16% |
| `miranda_1_1_1_t452-456_shift` | B | 9_miranda_1_1_1 451.8–456.2 s | 7.5 / 4.0 | 35 / 11 | shoulder at limit 52% |
| `miranda_1_2_2_t117-134` | A | 9_miranda_1_2_2 117.0–133.7 s | 8.7 / 5.1 | 35 / 12 | self-collision left_hand_collision / right_hand_end_collision 0.8 s (at 2.7 s, 17 mm) |
| `miranda_1_2_2_t236-253` | A | 9_miranda_1_2_2 236.2–253.3 s | 3.8 / 1.2 | 29 / 12 | outlier trunk drop (z +3.7); outlier knee max (z +6.2) |
| `miranda_1_2_2_t268-273_shift` | B | 9_miranda_1_2_2 268.4–272.7 s | 5.5 / 2.3 | 35 / 23 | outlier arms k1 cm (z +4.4) |
| `miranda_1_2_2_t308-327` | A | 9_miranda_1_2_2 307.8–326.6 s | 0.6 / 0.7 | 27 / 11 | hand presses into leg 39 mm for 0.8 s (at 4.3 s) |
| `miranda_1_2_2_t32-37_shift` | B | 9_miranda_1_2_2 32.4–36.7 s | 7.5 / 3.7 | 50 / 28 | outlier arms k1 cm (z +5.8) |
| `miranda_1_2_2_t364-383` | A | 9_miranda_1_2_2 364.4–383.3 s | 8.3 / 4.4 | 25 / 9 | head at limit 7%; elbow bend at limit 7% |
| `miranda_1_2_2_t515-534` | A | 9_miranda_1_2_2 515.1–533.6 s | 0.5 / 1.1 | 44 / 13 | head at limit 10% |
| `miranda_1_3_3_t107-124` | A | 9_miranda_1_3_3 106.8–124.0 s | 0.6 / 1.1 | 27 / 12 | elbow bend at limit 9% |
| `miranda_1_3_3_t211-228` | A | 9_miranda_1_3_3 211.4–228.1 s | 7.7 / 1.7 | 12 / 4 | outlier knee max (z +4.6) |
| `miranda_1_3_3_t228-240` | A | 9_miranda_1_3_3 228.1–239.6 s | 9.6 / 6.0 | 36 / 16 | outlier knee max (z +8.0) |
| `miranda_1_3_3_t259-279` | A | 9_miranda_1_3_3 259.3–278.9 s | 11.8 / 2.5 | 30 / 11 | human steps; outlier knee max (z +3.6) |
| `miranda_1_3_3_t277-283_shift` | B | 9_miranda_1_3_3 276.9–283.1 s | 19.0 / 11.7 | 56 / 22 | outlier arms k1 cm (z +4.0); outlier knee max (z +7.3) |
| `miranda_1_3_3_t299-316` | A | 9_miranda_1_3_3 298.6–316.2 s | 0.3 / 0.3 | 14 / 5 | outlier knee max (z -4.0) |
| `miranda_1_3_3_t31-47` | A | 9_miranda_1_3_3 31.5–47.2 s | 6.1 / 1.0 | 18 / 9 | shoulder at limit 5% |
| `miranda_1_3_3_t316-334` | A | 9_miranda_1_3_3 316.2–333.8 s | 2.8 / 2.1 | 25 / 8 | elbow bend at limit 8% |
| `miranda_1_3_3_t386-404` | A | 9_miranda_1_3_3 386.5–404.1 s | 3.8 / 2.1 | 23 / 8 | outlier trunk drop (z +4.3); outlier knee max (z +6.7) |
| `miranda_1_3_3_t515-535` | A | 9_miranda_1_3_3 514.8–534.6 s | 1.6 / 0.6 | 27 / 10 | shoulder at limit 13% |
| `miranda_1_3_3_t579-586_shift` | B | 9_miranda_1_3_3 579.4–585.9 s | 15.2 / 7.0 | 31 / 9 | outlier knee max (z +4.6) |
| `miranda_1_3_3_t61-68_shift` | B | 9_miranda_1_3_3 60.9–67.8 s | 10.9 / 5.7 | 32 / 13 | outlier knee max (z +5.3) |
| `miranda_1_3_3_t610-617_shift` | B | 9_miranda_1_3_3 610.2–617.2 s | 13.9 / 6.7 | 49 / 21 | outlier arms k1 cm (z +3.8) |
| `miranda_1_4_4_t14-19_shift` | B | 9_miranda_1_4_4 13.8–18.6 s | 10.7 / 6.9 | 26 / 8 | outlier knee max (z +4.3) |
| `miranda_1_4_4_t181-185_shift` | B | 9_miranda_1_4_4 180.9–184.9 s | 23.0 / 17.7 | 67 / 19 | knee 67 deg; outlier knee max (z +10.5) |
| `miranda_1_4_4_t236-252` | A | 9_miranda_1_4_4 235.7–251.9 s | 2.2 / 1.0 | 49 / 15 | outlier knee max (z +4.9) |
| `miranda_1_4_4_t36-55` | A | 9_miranda_1_4_4 35.9–55.2 s | 0.9 / 0.6 | 30 / 9 | elbow bend at limit 8% |
| `miranda_1_4_4_t55-74` | A | 9_miranda_1_4_4 55.2–74.5 s | 1.0 / 0.6 | 47 / 16 | elbow bend at limit 6% |
| `miranda_1_4_4_t560-579` | A | 9_miranda_1_4_4 560.5–579.0 s | 1.1 / 0.6 | 25 / 9 | outlier knee max (z +5.3) |
| `miranda_1_4_4_t579-597` | A | 9_miranda_1_4_4 579.0–597.5 s | 1.3 / 0.6 | 8 / 3 | outlier knee max (z +4.6) |
| `miranda_1_5_5_t187-192_shift` | B | 9_miranda_1_5_5 186.8–192.0 s | 7.9 / 5.3 | 16 / 5 | outlier knee max (z +6.5) |
| `miranda_1_5_5_t343-347_shift` | B | 9_miranda_1_5_5 343.0–347.3 s | 6.4 / 4.5 | 11 / 4 | head at limit 49%; outlier trunk drop (z +3.8) |
| `miranda_1_5_5_t345-365` | A | 9_miranda_1_5_5 345.3–364.6 s | 8.6 / 4.9 | 21 / 7 | head at limit 11%; outlier trunk drop (z +4.3) |
| `miranda_1_5_5_t447-466` | A | 9_miranda_1_5_5 446.6–466.1 s | 2.6 / 1.0 | 33 / 10 | head at limit 16% |
| `miranda_1_5_5_t466-486` | A | 9_miranda_1_5_5 466.1–485.7 s | 7.3 / 4.5 | 12 / 5 | head at limit 12% |
| `miranda_1_5_5_t499-515` | A | 9_miranda_1_5_5 499.4–515.0 s | 4.6 / 3.1 | 16 / 5 | outlier trunk drop (z +3.5) |
| `miranda_1_5_5_t618-626` | A | 9_miranda_1_5_5 618.2–626.1 s | 0.9 / 0.3 | 13 / 4 | head at limit 10% |
| `miranda_1_5_5_t623-627_shift` | B | 9_miranda_1_5_5 622.8–626.8 s | 18.1 / 9.0 | 8 / 2 | head at limit 23% |
| `miranda_1_6_6_t125-143` | A | 9_miranda_1_6_6 125.5–142.6 s | 0.7 / 0.6 | 21 / 9 | elbow bend at limit 7% |
| `miranda_1_6_6_t18-37` | A | 9_miranda_1_6_6 18.4–36.6 s | 0.2 / 0.1 | 2 / 1 | outlier knee max (z -4.5) |
| `miranda_1_6_6_t209-214_shift` | B | 9_miranda_1_6_6 209.0–213.7 s | 6.9 / 4.4 | 53 / 15 | outlier knee max (z +6.4) |
| `miranda_1_6_6_t212-218` | A | 9_miranda_1_6_6 211.7–217.5 s | 2.6 / 0.7 | 46 / 12 | outlier knee max (z +6.4) |
| `miranda_1_6_6_t252-257_shift` | B | 9_miranda_1_6_6 252.5–256.8 s | 9.2 / 4.1 | 8 / 2 | head at limit 24% |
| `miranda_1_6_6_t255-266` | A | 9_miranda_1_6_6 254.8–266.0 s | 8.3 / 3.5 | 10 / 3 | head at limit 9% |
| `miranda_1_6_6_t329-333_shift` | B | 9_miranda_1_6_6 329.0–333.0 s | 14.9 / 9.4 | 39 / 14 | outlier knee max (z +4.7) |
| `miranda_1_6_6_t331-344` | A | 9_miranda_1_6_6 330.8–344.4 s | 1.8 / 1.1 | 62 / 21 | outlier arms k1 cm (z +3.9) |
| `miranda_1_6_6_t89-94_shift` | B | 9_miranda_1_6_6 89.3–93.8 s | 24.5 / 14.7 | 46 / 12 | outlier knee max (z +4.6) |
| `miranda_1_6_6_t94-98_shift` | B | 9_miranda_1_6_6 93.8–97.9 s | 21.6 / 14.1 | 17 / 11 | outlier knee max (z +3.5) |
| `miranda_1_7_7_t252-272` | A | 9_miranda_1_7_7 252.4–271.9 s | 6.2 / 3.5 | 17 / 6 | elbow bend at limit 7% |
| `miranda_1_7_7_t272-291` | A | 9_miranda_1_7_7 271.9–291.4 s | 4.3 / 0.8 | 21 / 9 | elbow bend at limit 6% |
| `miranda_1_7_7_t58-77` | A | 9_miranda_1_7_7 57.9–77.2 s | 0.9 / 0.5 | 17 / 6 | elbow bend at limit 8% |
| `miranda_1_7_7_t96-116` | A | 9_miranda_1_7_7 96.5–115.8 s | 3.2 / 2.1 | 29 / 11 | outlier knee max (z +4.9) |
| `miranda_1_8_8_t268-287` | A | 9_miranda_1_8_8 268.1–286.9 s | 1.8 / 1.0 | 15 / 6 | elbow bend at limit 12% |
| `miranda_1_8_8_t287-306` | A | 9_miranda_1_8_8 286.9–305.7 s | 0.5 / 0.3 | 16 / 5 | hand presses into leg 40 mm for 1.2 s (at 12.8 s) |
| `miranda_1_8_8_t379-384_shift` | B | 9_miranda_1_8_8 379.1–384.5 s | 16.3 / 11.9 | 18 / 6 | knee 66 deg; outlier knee max (z +9.9) |
| `miranda_1_9_9_t119-138` | A | 9_miranda_1_9_9 119.3–138.2 s | 7.6 / 4.1 | 20 / 6 | elbow bend at limit 10% |
| `miranda_1_9_9_t176-195` | A | 9_miranda_1_9_9 176.1–195.0 s | 10.5 / 5.5 | 13 / 4 | human steps |
| `miranda_1_9_9_t196-203` | A | 9_miranda_1_9_9 196.2–202.8 s | 6.3 / 7.0 | 8 / 2 | outlier knee max (z +4.8) |
| `miranda_1_9_9_t201-205_shift` | B | 9_miranda_1_9_9 200.8–205.3 s | 8.5 / 6.6 | 9 / 3 | outlier knee max (z +4.2) |
| `miranda_1_9_9_t21-25_shift` | B | 9_miranda_1_9_9 20.8–25.5 s | 11.0 / 7.3 | 18 / 7 | outlier knee max (z +4.5) |
| `miranda_1_9_9_t23-29` | A | 9_miranda_1_9_9 23.5–28.7 s | 2.7 / 0.9 | 23 / 10 | upper-arm twist at limit 39%; leg at limit 14%; outlier knee max (z +4.0) |
| `miranda_1_9_9_t27-31_shift` | B | 9_miranda_1_9_9 26.7–31.2 s | 10.1 / 7.1 | 15 / 6 | knee 60 deg; outlier knee max (z +8.2) |
| `miranda_1_9_9_t303-323` | A | 9_miranda_1_9_9 302.7–322.6 s | 1.6 / 1.6 | 23 / 7 | head at limit 8% |
| `miranda_1_9_9_t323-342` | A | 9_miranda_1_9_9 322.6–342.5 s | 2.3 / 0.8 | 20 / 8 | outlier knee max (z +5.3) |
| `miranda_1_9_9_t47-51_shift` | B | 9_miranda_1_9_9 46.8–51.3 s | 7.3 / 5.2 | 57 / 16 | outlier knee max (z +6.0) |
| `miranda_1_9_9_t479-483_shift` | B | 9_miranda_1_9_9 478.7–482.7 s | 24.2 / 13.0 | 14 / 6 | outlier knee max (z +3.5) |
| `miranda_1_9_9_t49-65` | A | 9_miranda_1_9_9 49.3–65.2 s | 8.5 / 6.0 | 30 / 8 | outlier knee max (z +5.3) |
| `miranda_1_9_9_t496-510` | A | 9_miranda_1_9_9 496.3–510.4 s | 1.3 / 0.4 | 17 / 8 | head at limit 6% |
| `miranda_1_9_9_t510-525` | A | 9_miranda_1_9_9 510.4–524.6 s | 6.2 / 2.1 | 18 / 5 | head at limit 8%; outlier knee max (z +5.3); hand presses into leg 11 mm for 0.4 s (at 8.4 s) |
| `miranda_1_9_9_t523-527_shift` | B | 9_miranda_1_9_9 522.6–526.8 s | 2.6 / 0.6 | 6 / 2 | head at limit 14% |
| `miranda_1_9_9_t525-534` | A | 9_miranda_1_9_9 524.8–534.2 s | 7.7 / 1.2 | 16 / 5 | head at limit 9% |
| `miranda_1_9_9_t570-587` | A | 9_miranda_1_9_9 569.6–586.8 s | 5.5 / 3.8 | 17 / 7 | elbow bend at limit 6% |
| `miranda_1_9_9_t584-588_shift` | B | 9_miranda_1_9_9 583.8–587.8 s | 23.7 / 12.4 | 24 / 6 | outlier knee max (z +3.9) |
| `nidal_1_10_10_t155-160_shift` | B | 11_nidal_1_10_10 155.2–159.6 s | 7.8 / 4.3 | 21 / 7 | upper-arm twist at limit 25% |
| `nidal_1_10_10_t158-169` | A | 11_nidal_1_10_10 157.6–169.4 s | 6.3 / 2.1 | 30 / 8 | upper-arm twist at limit 23% |
| `nidal_1_10_10_t207-215_shift` | B | 11_nidal_1_10_10 206.6–214.5 s | 12.0 / 11.2 | 30 / 10 | outlier knee max (z +6.1) |
| `nidal_1_10_10_t230-234_shift` | B | 11_nidal_1_10_10 229.9–233.9 s | 29.0 / 16.6 | 18 / 5 | human steps; outlier knee max (z +3.9) |
| `nidal_1_10_10_t340-344_shift` | B | 11_nidal_1_10_10 339.9–343.9 s | 23.0 / 13.8 | 24 / 7 | outlier knee max (z +4.5) |
| `nidal_1_10_10_t344-354_shift` | B | 11_nidal_1_10_10 344.5–353.5 s | 16.5 / 13.6 | 36 / 9 | outlier knee max (z +4.1) |
| `nidal_1_10_10_t531-541_shift` | B | 11_nidal_1_10_10 530.8–540.6 s | 30.3 / 18.5 | 13 / 5 | human steps; K1 feet move 19 cm; outlier knee max (z +4.3) |
| `nidal_1_11_11_t153-159_shift` | B | 11_nidal_1_11_11 152.9–158.9 s | 26.9 / 15.0 | 19 / 5 | human steps; outlier knee max (z +4.0) |
| `nidal_1_11_11_t194-199_shift` | B | 11_nidal_1_11_11 193.7–199.4 s | 30.8 / 17.6 | 38 / 10 | human steps; outlier knee max (z +6.7) |
| `nidal_1_11_11_t246-251_shift` | B | 11_nidal_1_11_11 245.6–251.3 s | 22.2 / 12.5 | 22 / 7 | outlier knee max (z +4.1) |
| `nidal_1_11_11_t295-301_shift` | B | 11_nidal_1_11_11 295.3–301.3 s | 17.7 / 10.4 | 22 / 7 | outlier knee max (z +4.5) |
| `nidal_1_12_12_t138-144_shift` | B | 11_nidal_1_12_12 138.5–144.4 s | 19.8 / 12.0 | 22 / 5 | outlier knee max (z +3.6) |
| `nidal_1_12_12_t171-179_shift` | B | 11_nidal_1_12_12 170.6–178.9 s | 15.4 / 8.5 | 7 / 2 | outlier knee max (z +5.0) |
| `nidal_1_12_12_t709-726` | A | 11_nidal_1_12_12 708.6–726.3 s | 10.1 / 6.1 | 13 / 4 | human steps |
| `nidal_1_12_12_t95-101_shift` | B | 11_nidal_1_12_12 94.8–100.7 s | 18.2 / 11.6 | 29 / 6 | outlier knee max (z +3.6) |
| `nidal_1_1_1_t612-632` | A | 11_nidal_1_1_1 612.3–632.0 s | 0.3 / 0.4 | 14 / 5 | shoulder at limit 8% |
| `nidal_1_5_5_t135-142_shift` | B | 11_nidal_1_5_5 134.6–142.1 s | 18.5 / 10.8 | 25 / 6 | outlier knee max (z +5.9) |
| `nidal_1_5_5_t151-163` | A | 11_nidal_1_5_5 151.4–162.8 s | 8.0 / 1.0 | 28 / 9 | shoulder at limit 7% |
| `nidal_1_5_5_t543-562` | A | 11_nidal_1_5_5 543.2–562.3 s | 0.9 / 0.7 | 27 / 9 | shoulder at limit 8% |
| `nidal_1_5_5_t78-82_shift` | B | 11_nidal_1_5_5 77.5–81.5 s | 25.0 / 14.7 | 36 / 9 | human steps; outlier knee max (z +4.9) |
| `nidal_1_5_5_t82-86_shift` | B | 11_nidal_1_5_5 81.5–85.5 s | 22.0 / 12.6 | 18 / 6 | outlier knee max (z +5.1) |
| `nidal_1_6_6_t117-123_shift` | B | 11_nidal_1_6_6 117.4–122.7 s | 20.8 / 11.5 | 12 / 3 | outlier knee max (z +4.2) |
| `nidal_1_6_6_t238-242_shift` | B | 11_nidal_1_6_6 237.7–242.2 s | 8.7 / 6.2 | 22 / 7 | outlier knee max (z +3.9) |
| `nidal_1_6_6_t42-47_shift` | B | 11_nidal_1_6_6 41.8–46.6 s | 11.9 / 8.2 | 16 / 7 | outlier knee max (z +4.2) |
| `nidal_1_6_6_t68-74_shift` | B | 11_nidal_1_6_6 67.5–74.3 s | 20.2 / 12.5 | 25 / 9 | outlier knee max (z +4.4) |
| `nidal_1_7_7_t338-357` | A | 11_nidal_1_7_7 338.4–357.5 s | 15.5 / 9.1 | 26 / 8 | human steps; K1 feet move 9 cm |
| `nidal_1_7_7_t374-391` | A | 11_nidal_1_7_7 374.1–390.8 s | 7.0 / 2.2 | 14 / 5 | outlier knee max (z +5.6) |
| `nidal_1_7_7_t389-394_shift` | B | 11_nidal_1_7_7 388.8–393.6 s | 14.3 / 8.8 | 8 / 3 | outlier trunk drop (z +4.0); outlier knee max (z +5.5) |
| `nidal_1_7_7_t427-432_shift` | B | 11_nidal_1_7_7 427.1–431.6 s | 12.6 / 7.9 | 27 / 10 | outlier knee max (z +4.2) |
| `nidal_1_7_7_t616-632` | A | 11_nidal_1_7_7 616.5–632.1 s | 0.2 / 0.3 | 25 / 7 | outlier knee max (z -4.2) |
| `nidal_1_7_7_t86-92_shift` | B | 11_nidal_1_7_7 85.5–92.1 s | 16.5 / 9.8 | 17 / 9 | outlier knee max (z +3.5) |
| `nidal_1_8_8_t13-18_shift` | B | 11_nidal_1_8_8 13.1–17.8 s | 15.9 / 10.3 | 17 / 11 | outlier knee max (z +4.7) |
| `nidal_1_8_8_t137-141_shift` | B | 11_nidal_1_8_8 136.7–140.7 s | 17.1 / 10.1 | 16 / 7 | outlier knee max (z +3.6) |
| `nidal_1_8_8_t141-146_shift` | B | 11_nidal_1_8_8 141.3–146.3 s | 19.8 / 13.3 | 39 / 12 | outlier knee max (z +5.8) |
| `nidal_1_8_8_t251-255_shift` | B | 11_nidal_1_8_8 250.9–254.9 s | 24.0 / 12.4 | 55 / 12 | outlier knee max (z +4.3) |
| `nidal_1_8_8_t382-387_shift` | B | 11_nidal_1_8_8 382.4–386.8 s | 12.9 / 7.6 | 14 / 5 | outlier knee max (z +4.5) |
| `nidal_1_8_8_t397-410` | A | 11_nidal_1_8_8 397.5–410.1 s | 6.0 / 4.9 | 28 / 10 | shoulder at limit 8% |
| `nidal_1_8_8_t408-413_shift` | B | 11_nidal_1_8_8 408.1–412.7 s | 12.3 / 8.2 | 24 / 9 | outlier knee max (z +4.0) |
| `nidal_1_8_8_t469-481` | A | 11_nidal_1_8_8 469.4–481.5 s | 8.4 / 2.3 | 26 / 10 | outlier knee max (z +3.5) |
| `nidal_1_8_8_t492-496_shift` | B | 11_nidal_1_8_8 491.5–496.2 s | 16.7 / 10.9 | 31 / 8 | outlier knee max (z +5.6) |
| `nidal_1_9_9_t287-292_shift` | B | 11_nidal_1_9_9 287.2–291.8 s | 18.2 / 11.7 | 20 / 5 | outlier knee max (z +4.0) |
| `nidal_1_9_9_t306-322` | A | 11_nidal_1_9_9 305.7–321.6 s | 0.4 / 0.5 | 30 / 8 | shoulder at limit 5% |
| `nidal_1_9_9_t350-354_shift` | B | 11_nidal_1_9_9 349.9–353.9 s | 22.3 / 12.7 | 32 / 7 | outlier knee max (z +4.6) |
| `nidal_1_9_9_t379-384_shift` | B | 11_nidal_1_9_9 379.1–383.7 s | 11.9 / 7.9 | 12 / 4 | outlier knee max (z +4.0) |
| `nidal_1_9_9_t555-559_shift` | B | 11_nidal_1_9_9 554.9–559.3 s | 11.7 / 7.0 | 17 / 6 | outlier knee max (z +3.7) |
| `scott_0_100_100_t23-29_shift` | B | 2_scott_0_100_100 22.7–28.5 s | 15.1 / 11.9 | 33 / 12 | outlier knee max (z +4.9) |
| `scott_0_100_100_t30-34` | A | 2_scott_0_100_100 30.1–34.2 s | 9.1 / 4.9 | 77 / 26 | outlier arms k1 cm (z +5.3) |
| `scott_0_100_100_t32-38_shift` | B | 2_scott_0_100_100 32.2–37.7 s | 24.4 / 13.6 | 59 / 20 | outlier arms k1 cm (z +3.5); outlier knee max (z +4.1) |
| `scott_0_100_100_t7-13_shift` | B | 2_scott_0_100_100 7.4–13.3 s | 23.9 / 18.5 | 49 / 14 | K1 feet move 18 cm; outlier knee max (z +7.2) |
| `scott_0_101_101_t41-45_shift` | B | 2_scott_0_101_101 40.6–45.2 s | 18.2 / 14.6 | 34 / 9 | outlier knee max (z +5.1) |
| `scott_0_102_102_t22-27_shift` | B | 2_scott_0_102_102 21.7–26.6 s | 12.5 / 2.9 | 47 / 15 | outlier knee max (z +5.7) |
| `scott_0_104_104_t27-32` | A | 2_scott_0_104_104 27.1–31.5 s | 6.1 / 3.2 | 50 / 21 | outlier arms k1 cm (z +3.9) |
| `scott_0_104_104_t6-10_shift` | B | 2_scott_0_104_104 5.7–10.4 s | 24.6 / 13.8 | 23 / 9 | outlier knee max (z +3.7) |
| `scott_0_106_106_t35-46_shift` | B | 2_scott_0_106_106 34.7–46.3 s | 22.0 / 14.0 | 48 / 16 | outlier knee max (z +6.2) |
| `scott_0_107_107_t10-15` | A | 2_scott_0_107_107 10.4–14.9 s | 3.4 / 5.5 | 21 / 6 | hand presses into leg 37 mm for 3.0 s (at 1.5 s) |
| `scott_0_107_107_t27-31_shift` | B | 2_scott_0_107_107 26.7–31.4 s | 12.6 / 9.2 | 51 / 18 | outlier knee max (z +5.2) |
| `scott_0_108_108_t33-37_shift` | B | 2_scott_0_108_108 32.9–37.3 s | 21.6 / 11.4 | 53 / 15 | outlier knee max (z +5.2) |
| `scott_0_109_109_t18-22_shift` | B | 2_scott_0_109_109 17.8–21.8 s | 21.3 / 11.0 | 23 / 10 | outlier knee max (z +6.4) |
| `scott_0_109_109_t29-34_shift` | B | 2_scott_0_109_109 29.5–34.0 s | 17.3 / 10.2 | 41 / 13 | outlier knee max (z +5.4) |
| `scott_0_109_109_t32-37` | A | 2_scott_0_109_109 32.0–36.9 s | 4.8 / 4.8 | 37 / 16 | outlier knee max (z +5.1) |
| `scott_0_10_10_t31-42` | A | 2_scott_0_10_10 31.1–41.7 s | 9.7 / 6.0 | 47 / 13 | outlier knee max (z +3.5) |
| `scott_0_10_10_t40-47_shift` | B | 2_scott_0_10_10 39.7–46.9 s | 15.8 / 9.4 | 35 / 10 | outlier knee max (z +5.5) |
| `scott_0_110_110_t10-17` | A | 2_scott_0_110_110 10.1–17.0 s | 1.2 / 0.9 | 62 / 21 | outlier arms k1 cm (z +4.0) |
| `scott_0_110_110_t15-19_shift` | B | 2_scott_0_110_110 15.0–19.5 s | 19.9 / 12.4 | 46 / 19 | knee 66 deg; outlier knee max (z +10.2) |
| `scott_0_110_110_t40-46_shift` | B | 2_scott_0_110_110 40.2–46.0 s | 18.9 / 10.7 | 32 / 14 | knee 68 deg; outlier knee max (z +10.6) |
| `scott_0_110_110_t47-51_shift` | B | 2_scott_0_110_110 47.0–51.3 s | 23.7 / 12.5 | 43 / 11 | outlier knee max (z +5.4) |
| `scott_0_111_111_t12-16_shift` | B | 2_scott_0_111_111 12.1–16.2 s | 19.3 / 10.7 | 30 / 11 | outlier knee max (z +6.6) |
| `scott_0_111_111_t47-52` | A | 2_scott_0_111_111 46.6–51.7 s | 2.7 / 0.8 | 76 / 23 | outlier arms k1 cm (z +4.4) |
| `scott_0_113_113_t29-34_shift` | B | 2_scott_0_113_113 28.7–34.3 s | 24.0 / 10.6 | 64 / 18 | outlier knee max (z +6.1) |
| `scott_0_113_113_t5-13_shift` | B | 2_scott_0_113_113 5.4–12.9 s | 21.3 / 11.6 | 64 / 18 | knee 62 deg; outlier knee max (z +8.6) |
| `scott_0_113_113_t8-12` | A | 2_scott_0_113_113 7.7–11.7 s | 5.8 / 5.8 | 65 / 20 | outlier arms k1 cm (z +3.6) |
| `scott_0_114_114_t14-23_shift` | B | 2_scott_0_114_114 14.4–23.4 s | 18.6 / 12.2 | 57 / 17 | outlier knee max (z +7.7) |
| `scott_0_114_114_t24-28_shift` | B | 2_scott_0_114_114 24.0–28.0 s | 21.0 / 16.3 | 53 / 18 | outlier knee max (z +5.9) |
| `scott_0_114_114_t25-29` | A | 2_scott_0_114_114 24.6–29.0 s | 7.3 / 8.7 | 60 / 20 | K1 feet move 9 cm; outlier arms k1 cm (z +3.7); outlier trunk drop (z +3.8); outlier knee max (z +3.6) |
| `scott_0_114_114_t36-40_shift` | B | 2_scott_0_114_114 35.5–39.8 s | 21.6 / 11.8 | 74 / 22 | outlier arms k1 cm (z +4.2); outlier knee max (z +6.2) |
| `scott_0_115_115_t16-22_shift` | B | 2_scott_0_115_115 16.0–21.5 s | 22.1 / 15.7 | 45 / 11 | outlier knee max (z +5.6) |
| `scott_0_115_115_t31-36_shift` | B | 2_scott_0_115_115 31.0–36.4 s | 30.1 / 17.8 | 65 / 20 | human steps; outlier arms k1 cm (z +3.6); outlier knee max (z +5.4) |
| `scott_0_116_116_t17-21_shift` | B | 2_scott_0_116_116 16.9–21.0 s | 23.5 / 11.0 | 33 / 21 | outlier arms k1 cm (z +3.8) |
| `scott_0_116_116_t46-54_shift` | B | 2_scott_0_116_116 46.2–54.5 s | 24.8 / 20.1 | 63 / 18 | K1 feet move 20 cm; outlier knee max (z +7.1) |
| `scott_0_117_117_t30-35_shift` | B | 2_scott_0_117_117 30.5–35.4 s | 17.1 / 14.5 | 42 / 14 | outlier knee max (z +3.7) |
| `scott_0_11_11_t14-27_shift` | B | 2_scott_0_11_11 13.6–26.8 s | 24.2 / 13.5 | 45 / 13 | outlier knee max (z +4.9) |
| `scott_0_11_11_t38-48_shift` | B | 2_scott_0_11_11 37.9–47.8 s | 19.1 / 10.1 | 30 / 9 | outlier knee max (z +4.5) |
| `scott_0_12_12_t21-32_shift` | B | 2_scott_0_12_12 21.0–32.2 s | 28.4 / 15.4 | 61 / 17 | human steps; outlier knee max (z +4.7) |
| `scott_0_12_12_t40-55_shift` | B | 2_scott_0_12_12 40.2–54.8 s | 23.8 / 16.4 | 48 / 14 | outlier knee max (z +6.3) |
| `scott_0_12_12_t57-64_shift` | B | 2_scott_0_12_12 57.4–64.4 s | 15.9 / 8.8 | 40 / 13 | shoulder at limit 12% |
| `scott_0_12_12_t76-90_shift` | B | 2_scott_0_12_12 75.7–89.9 s | 20.8 / 11.6 | 51 / 14 | outlier knee max (z +4.6) |
| `scott_0_13_13_t4-17_shift` | B | 2_scott_0_13_13 4.3–16.7 s | 23.2 / 14.6 | 42 / 13 | outlier knee max (z +4.3) |
| `scott_0_14_14_t79-86` | A | 2_scott_0_14_14 79.2–85.8 s | 0.8 / 0.6 | 77 / 20 | outlier arms k1 cm (z +3.7) |
| `scott_0_14_14_t9-15_shift` | B | 2_scott_0_14_14 9.3–14.8 s | 19.0 / 11.2 | 50 / 15 | outlier knee max (z +4.1) |
| `scott_0_15_15_t16-21` | A | 2_scott_0_15_15 15.9–20.6 s | 9.8 / 6.7 | 34 / 15 | outlier trunk drop (z +3.8) |
| `scott_0_15_15_t19-35_shift` | B | 2_scott_0_15_15 18.6–35.0 s | 16.5 / 9.9 | 33 / 12 | outlier knee max (z +8.0) |
| `scott_0_15_15_t62-67_shift` | B | 2_scott_0_15_15 62.0–66.9 s | 16.9 / 15.5 | 21 / 6 | outlier knee max (z +6.8) |
| `scott_0_15_15_t88-92_shift` | B | 2_scott_0_15_15 87.5–91.8 s | 18.4 / 3.5 | 45 / 12 | outlier knee max (z +4.4) |
| `scott_0_16_16_t12-29_shift` | B | 2_scott_0_16_16 12.1–29.4 s | 20.3 / 10.7 | 58 / 18 | outlier trunk drop (z +4.3); outlier knee max (z +5.8); hand presses into leg 28 mm for 0.1 s (at 0.7 s) |
| `scott_0_16_16_t3-12_shift` | B | 2_scott_0_16_16 2.5–12.1 s | 25.0 / 16.5 | 37 / 11 | outlier knee max (z +6.2) |
| `scott_0_16_16_t43-49_shift` | B | 2_scott_0_16_16 43.1–48.6 s | 17.9 / 12.4 | 55 / 16 | outlier trunk drop (z +5.0); outlier knee max (z +5.5) |
| `scott_0_16_16_t64-71_shift` | B | 2_scott_0_16_16 63.8–70.7 s | 24.2 / 15.3 | 60 / 15 | outlier knee max (z +6.6) |
| `scott_0_17_17_t62-71_shift` | B | 2_scott_0_17_17 61.8–70.7 s | 15.7 / 11.7 | 37 / 11 | outlier knee max (z +5.2) |
| `scott_0_17_17_t7-12_shift` | B | 2_scott_0_17_17 7.4–12.1 s | 22.9 / 11.4 | 74 / 20 | outlier arms k1 cm (z +3.6); outlier knee max (z +4.2) |
| `scott_0_18_18_t2-6_shift` | B | 2_scott_0_18_18 1.6–5.8 s | 21.3 / 13.7 | 49 / 15 | outlier knee max (z +6.3) |
| `scott_0_18_18_t23-28_shift` | B | 2_scott_0_18_18 23.3–27.8 s | 22.2 / 13.2 | 35 / 9 | outlier knee max (z +4.5) |
| `scott_0_19_19_t14-20_shift` | B | 2_scott_0_19_19 14.4–20.0 s | 24.6 / 15.0 | 72 / 18 | outlier knee max (z +5.3) |
| `scott_0_1_1_t24-31_shift` | B | 2_scott_0_1_1 24.3–30.6 s | 20.1 / 12.5 | 59 / 15 | outlier knee max (z +5.3) |
| `scott_0_1_1_t54-59_shift` | B | 2_scott_0_1_1 54.4–59.1 s | 24.3 / 17.4 | 28 / 8 | outlier knee max (z +6.3) |
| `scott_0_22_22_t21-26_shift` | B | 2_scott_0_22_22 21.2–25.7 s | 22.1 / 14.8 | 56 / 15 | outlier knee max (z +3.8) |
| `scott_0_22_22_t41-55_shift` | B | 2_scott_0_22_22 41.4–54.7 s | 30.0 / 13.1 | 50 / 14 | human steps; outlier knee max (z +4.5) |
| `scott_0_22_22_t56-61_shift` | B | 2_scott_0_22_22 56.1–61.5 s | 24.7 / 13.2 | 25 / 10 | outlier knee max (z +5.8) |
| `scott_0_22_22_t9-17_shift` | B | 2_scott_0_22_22 9.1–17.4 s | 24.8 / 14.7 | 59 / 17 | outlier knee max (z +5.4) |
| `scott_0_23_23_t17-21` | A | 2_scott_0_23_23 16.6–20.8 s | 3.6 / 4.3 | 84 / 24 | outlier arms k1 cm (z +4.6) |
| `scott_0_23_23_t44-49_shift` | B | 2_scott_0_23_23 44.0–49.0 s | 20.3 / 9.5 | 37 / 9 | outlier knee max (z +5.5) |
| `scott_0_24_24_t44-51` | A | 2_scott_0_24_24 44.3–50.6 s | 1.8 / 0.5 | 27 / 8 | outlier knee max (z +4.3) |
| `scott_0_24_24_t69-78_shift` | B | 2_scott_0_24_24 69.1–77.8 s | 23.5 / 13.4 | 47 / 14 | outlier knee max (z +6.3) |
| `scott_0_26_26_t17-25_shift` | B | 2_scott_0_26_26 16.6–24.6 s | 24.8 / 14.2 | 28 / 9 | outlier knee max (z +6.1) |
| `scott_0_27_27_t56-60_shift` | B | 2_scott_0_27_27 56.1–60.3 s | 24.9 / 16.9 | 27 / 8 | outlier knee max (z +5.9) |
| `scott_0_28_28_t8-12_shift` | B | 2_scott_0_28_28 7.8–11.8 s | 20.6 / 19.3 | 38 / 12 | K1 feet move 19 cm |
| `scott_0_29_29_t12-18_shift` | B | 2_scott_0_29_29 11.7–17.8 s | 29.5 / 13.4 | 34 / 11 | human steps |
| `scott_0_29_29_t24-28_shift` | B | 2_scott_0_29_29 23.5–27.6 s | 17.5 / 9.7 | 19 / 7 | outlier knee max (z +5.1) |
| `scott_0_29_29_t8-14` | A | 2_scott_0_29_29 7.8–13.7 s | 9.6 / 9.9 | 29 / 11 | K1 feet move 10 cm |
| `scott_0_2_2_t17-22_shift` | B | 2_scott_0_2_2 16.9–21.6 s | 19.1 / 12.0 | 33 / 11 | outlier knee max (z +4.9) |
| `scott_0_2_2_t39-44_shift` | B | 2_scott_0_2_2 39.2–43.6 s | 9.6 / 5.9 | 15 / 5 | outlier knee max (z +4.4) |
| `scott_0_2_2_t47-62_shift` | B | 2_scott_0_2_2 47.0–61.8 s | 21.5 / 13.2 | 40 / 12 | outlier knee max (z +4.4) |
| `scott_0_30_30_t24-29_shift` | B | 2_scott_0_30_30 23.7–28.8 s | 16.0 / 10.4 | 27 / 9 | outlier knee max (z +6.8) |
| `scott_0_31_31_t48-53_shift` | B | 2_scott_0_31_31 47.6–52.7 s | 25.9 / 14.9 | 75 / 21 | human steps; outlier arms k1 cm (z +3.9); outlier knee max (z +5.3) |
| `scott_0_32_32_t32-36_shift` | B | 2_scott_0_32_32 32.2–36.2 s | 30.2 / 17.1 | 47 / 12 | human steps; outlier knee max (z +7.9) |
| `scott_0_33_33_t20-28_shift` | B | 2_scott_0_33_33 20.1–28.0 s | 21.6 / 16.8 | 28 / 12 | outlier knee max (z +6.8) |
| `scott_0_34_34_t47-53_shift` | B | 2_scott_0_34_34 47.0–53.2 s | 18.2 / 7.7 | 39 / 13 | outlier knee max (z +3.7) |
| `scott_0_35_35_t8-17_shift` | B | 2_scott_0_35_35 8.5–16.9 s | 20.0 / 10.9 | 29 / 11 | knee 70 deg; outlier knee max (z +11.3) |
| `scott_0_36_36_t36-42_shift` | B | 2_scott_0_36_36 36.4–42.2 s | 15.3 / 4.9 | 49 / 14 | outlier knee max (z +4.1) |
| `scott_0_36_36_t8-14_shift` | B | 2_scott_0_36_36 8.2–13.9 s | 13.1 / 7.7 | 32 / 11 | outlier knee max (z +5.3) |
| `scott_0_3_3_t23-27_shift` | B | 2_scott_0_3_3 22.6–26.6 s | 24.9 / 11.9 | 40 / 12 | outlier knee max (z +6.6) |
| `scott_0_3_3_t47-55_shift` | B | 2_scott_0_3_3 47.4–54.9 s | 13.2 / 7.8 | 32 / 11 | outlier trunk drop (z +3.8); outlier knee max (z +7.9) |
| `scott_0_3_3_t48-53` | A | 2_scott_0_3_3 48.5–52.7 s | 9.6 / 1.7 | 25 / 10 | outlier knee max (z +7.9) |
| `scott_0_40_40_t51-55_shift` | B | 2_scott_0_40_40 50.7–55.4 s | 18.1 / 12.3 | 45 / 14 | outlier knee max (z +4.7); hand presses into leg 35 mm for 0.2 s (at 3.4 s) |
| `scott_0_41_41_t7-12_shift` | B | 2_scott_0_41_41 7.0–11.5 s | 17.4 / 13.1 | 34 / 11 | outlier knee max (z +5.7) |
| `scott_0_42_42_t19-24_shift` | B | 2_scott_0_42_42 19.2–24.0 s | 14.3 / 9.9 | 37 / 12 | outlier knee max (z +4.9) |
| `scott_0_42_42_t5-9_shift` | B | 2_scott_0_42_42 4.9–9.2 s | 17.9 / 8.5 | 35 / 11 | outlier knee max (z +4.9) |
| `scott_0_43_43_t20-25_shift` | B | 2_scott_0_43_43 20.4–25.1 s | 9.9 / 2.2 | 28 / 9 | outlier knee max (z +7.2) |
| `scott_0_44_44_t7-13_shift` | B | 2_scott_0_44_44 7.5–13.4 s | 21.9 / 13.0 | 36 / 9 | outlier knee max (z +6.7) |
| `scott_0_45_45_t30-34_shift` | B | 2_scott_0_45_45 30.2–34.4 s | 12.1 / 8.8 | 28 / 9 | outlier trunk drop (z +5.0); outlier knee max (z +7.7) |
| `scott_0_46_46_t1-5_shift` | B | 2_scott_0_46_46 1.3–5.4 s | 14.9 / 8.4 | 101 / 29 | outlier arms k1 cm (z +6.0) |
| `scott_0_46_46_t42-46_shift` | B | 2_scott_0_46_46 41.5–46.4 s | 11.5 / 6.1 | 29 / 9 | outlier knee max (z +4.3) |
| `scott_0_46_46_t65-74_shift` | B | 2_scott_0_46_46 64.8–73.8 s | 21.1 / 10.3 | 43 / 13 | outlier knee max (z +4.9) |
| `scott_0_46_46_t72-76` | A | 2_scott_0_46_46 71.8–76.5 s | 4.8 / 0.5 | 19 / 7 | head at limit 39% |
| `scott_0_47_47_t4-8_shift` | B | 2_scott_0_47_47 3.8–8.4 s | 19.6 / 11.4 | 35 / 10 | outlier knee max (z +3.5) |
| `scott_0_47_47_t9-15_shift` | B | 2_scott_0_47_47 9.0–15.2 s | 18.1 / 10.4 | 28 / 9 | outlier knee max (z +4.7) |
| `scott_0_49_49_t0-6_shift` | B | 2_scott_0_49_49 0.0–5.9 s | 21.4 / 12.7 | 35 / 10 | outlier knee max (z +4.2) |
| `scott_0_49_49_t21-31_shift` | B | 2_scott_0_49_49 21.2–31.3 s | 17.9 / 4.3 | 41 / 12 | outlier knee max (z +7.5) |
| `scott_0_4_4_t18-24_shift` | B | 2_scott_0_4_4 18.0–24.4 s | 21.7 / 13.7 | 44 / 13 | outlier knee max (z +6.7) |
| `scott_0_4_4_t49-53_shift` | B | 2_scott_0_4_4 49.2–53.2 s | 21.7 / 12.8 | 26 / 10 | outlier knee max (z +4.4) |
| `scott_0_50_50_t31-38` | A | 2_scott_0_50_50 31.4–37.8 s | 1.9 / 1.4 | 25 / 9 | shoulder at limit 10% |
| `scott_0_52_52_t34-40` | A | 2_scott_0_52_52 34.0–40.2 s | 3.6 / 2.7 | 41 / 10 | hand presses into leg 13 mm for 0.1 s (at 2.4 s) |
| `scott_0_52_52_t6-13_shift` | B | 2_scott_0_52_52 5.8–13.4 s | 21.7 / 12.4 | 41 / 15 | outlier knee max (z +4.8) |
| `scott_0_52_52_t9-13` | A | 2_scott_0_52_52 9.0–13.2 s | 9.5 / 10.4 | 38 / 15 | K1 feet move 10 cm |
| `scott_0_53_53_t11-16_shift` | B | 2_scott_0_53_53 11.4–16.5 s | 20.4 / 11.0 | 42 / 12 | outlier knee max (z +6.3) |
| `scott_0_53_53_t7-11_shift` | B | 2_scott_0_53_53 6.7–10.7 s | 16.1 / 7.4 | 21 / 9 | leg at limit 6% |
| `scott_0_57_57_t54-59` | A | 2_scott_0_57_57 54.1–58.7 s | 6.0 / 1.0 | 79 / 21 | outlier arms k1 cm (z +3.8) |
| `scott_0_59_59_t20-24_shift` | B | 2_scott_0_59_59 19.7–23.7 s | 18.0 / 10.6 | 57 / 14 | outlier knee max (z +3.8) |
| `scott_0_60_60_t15-19_shift` | B | 2_scott_0_60_60 14.9–18.9 s | 24.4 / 12.8 | 37 / 10 | outlier knee max (z +4.3) |
| `scott_0_60_60_t19-24_shift` | B | 2_scott_0_60_60 19.2–23.6 s | 9.3 / 6.9 | 27 / 7 | outlier knee max (z +4.8) |
| `scott_0_62_62_t13-17_shift` | B | 2_scott_0_62_62 12.7–17.1 s | 15.3 / 8.3 | 29 / 10 | outlier knee max (z +4.2) |
| `scott_0_62_62_t21-25_shift` | B | 2_scott_0_62_62 21.1–25.1 s | 24.9 / 9.3 | 60 / 15 | outlier knee max (z +5.2) |
| `scott_0_64_64_t10-14_shift` | B | 2_scott_0_64_64 9.7–13.9 s | 17.1 / 11.1 | 32 / 10 | outlier knee max (z +3.6) |
| `scott_0_64_64_t7-12` | A | 2_scott_0_64_64 7.4–11.7 s | 4.3 / 4.7 | 27 / 9 | outlier knee max (z +5.5) |
| `scott_0_65_65_t14-18_shift` | B | 2_scott_0_65_65 13.6–17.6 s | 10.7 / 11.4 | 33 / 12 | outlier knee max (z +5.0) |
| `scott_0_65_65_t15-23` | A | 2_scott_0_65_65 15.0–23.1 s | 5.5 / 4.8 | 47 / 14 | hand presses into leg 20 mm for 0.7 s (at 6.0 s) |
| `scott_0_66_66_t10-16_shift` | B | 2_scott_0_66_66 10.3–16.0 s | 12.6 / 8.0 | 46 / 12 | outlier knee max (z +6.1) |
| `scott_0_66_66_t60-66_shift` | B | 2_scott_0_66_66 59.9–65.5 s | 25.0 / 11.3 | 30 / 9 | outlier knee max (z +6.0) |
| `scott_0_68_68_t35-42_shift` | B | 2_scott_0_68_68 34.8–41.6 s | 30.6 / 18.9 | 39 / 12 | human steps; K1 feet move 19 cm; outlier knee max (z +5.7) |
| `scott_0_6_6_t48-53_shift` | B | 2_scott_0_6_6 48.5–52.7 s | 11.7 / 2.2 | 25 / 9 | outlier knee max (z +7.8) |
| `scott_0_6_6_t9-14_shift` | B | 2_scott_0_6_6 9.5–14.0 s | 22.4 / 14.4 | 54 / 15 | outlier knee max (z +5.0) |
| `scott_0_70_70_t12-16_shift` | B | 2_scott_0_70_70 11.5–15.7 s | 10.8 / 6.0 | 23 / 6 | outlier knee max (z +3.7) |
| `scott_0_70_70_t4-11_shift` | B | 2_scott_0_70_70 4.4–11.0 s | 24.1 / 18.4 | 77 / 21 | K1 feet move 18 cm; outlier arms k1 cm (z +4.0); outlier knee max (z +4.6) |
| `scott_0_74_74_t16-21_shift` | B | 2_scott_0_74_74 16.4–21.3 s | 23.0 / 10.2 | 23 / 11 | outlier knee max (z +4.6) |
| `scott_0_78_78_t5-9_shift` | B | 2_scott_0_78_78 4.7–9.3 s | 24.5 / 14.7 | 65 / 17 | knee 62 deg; outlier knee max (z +8.6) |
| `scott_0_7_7_t27-34_shift` | B | 2_scott_0_7_7 27.2–34.2 s | 25.8 / 13.8 | 37 / 10 | human steps; outlier knee max (z +7.4) |
| `scott_0_7_7_t35-39_shift` | B | 2_scott_0_7_7 35.1–39.1 s | 24.9 / 11.3 | 22 / 9 | outlier knee max (z +5.5) |
| `scott_0_7_7_t50-55_shift` | B | 2_scott_0_7_7 50.1–54.7 s | 16.5 / 9.8 | 24 / 11 | outlier knee max (z +4.8) |
| `scott_0_7_7_t55-62_shift` | B | 2_scott_0_7_7 54.8–61.9 s | 20.8 / 9.8 | 35 / 13 | outlier knee max (z +4.7) |
| `scott_0_81_81_t40-45_shift` | B | 2_scott_0_81_81 39.7–44.8 s | 32.0 / 17.8 | 50 / 13 | human steps; outlier knee max (z +7.2) |
| `scott_0_81_81_t56-61_shift` | B | 2_scott_0_81_81 56.0–61.4 s | 36.8 / 20.5 | 45 / 13 | human steps; K1 feet move 20 cm; outlier knee max (z +6.4) |
| `scott_0_81_81_t6-14_shift` | B | 2_scott_0_81_81 6.1–13.5 s | 22.6 / 12.2 | 25 / 9 | outlier knee max (z +4.3) |
| `scott_0_81_81_t63-67_shift` | B | 2_scott_0_81_81 62.8–66.8 s | 36.7 / 20.1 | 63 / 16 | human steps; K1 feet move 20 cm; outlier knee max (z +5.3) |
| `scott_0_82_82_t0-6_shift` | B | 2_scott_0_82_82 0.0–6.1 s | 23.6 / 13.0 | 21 / 5 | outlier knee max (z +7.6) |
| `scott_0_82_82_t36-48_shift` | B | 2_scott_0_82_82 36.5–48.3 s | 18.7 / 8.9 | 45 / 13 | knee 63 deg; outlier knee max (z +9.0) |
| `scott_0_82_82_t50-54_shift` | B | 2_scott_0_82_82 49.6–53.6 s | 15.3 / 8.8 | 43 / 12 | outlier knee max (z +6.7) |
| `scott_0_82_82_t56-64_shift` | B | 2_scott_0_82_82 56.5–64.3 s | 23.3 / 14.5 | 54 / 14 | outlier knee max (z +5.6) |
| `scott_0_82_82_t8-18_shift` | B | 2_scott_0_82_82 7.6–18.3 s | 29.3 / 17.4 | 32 / 10 | human steps; outlier knee max (z +6.9) |
| `scott_0_83_83_t36-48_shift` | B | 2_scott_0_83_83 36.1–48.1 s | 20.8 / 12.9 | 39 / 12 | outlier knee max (z +7.0) |
| `scott_0_83_83_t6-10_shift` | B | 2_scott_0_83_83 6.4–10.4 s | 19.4 / 6.0 | 50 / 14 | outlier knee max (z +6.0) |
| `scott_0_84_84_t12-22_shift` | B | 2_scott_0_84_84 11.7–21.8 s | 19.0 / 10.7 | 31 / 12 | outlier knee max (z +6.9) |
| `scott_0_87_87_t16-23_shift` | B | 2_scott_0_87_87 15.9–22.9 s | 12.9 / 9.3 | 36 / 11 | outlier knee max (z +5.5); hand presses into leg 15 mm for 0.1 s (at 6.9 s) |
| `scott_0_87_87_t24-28_shift` | B | 2_scott_0_87_87 23.7–28.5 s | 23.3 / 16.2 | 44 / 12 | outlier knee max (z +5.4) |
| `scott_0_87_87_t46-50_shift` | B | 2_scott_0_87_87 46.3–50.3 s | 21.6 / 10.5 | 49 / 14 | outlier knee max (z +5.3) |
| `scott_0_87_87_t61-77_shift` | B | 2_scott_0_87_87 60.8–77.2 s | 22.0 / 17.6 | 30 / 11 | knee 60 deg; outlier knee max (z +8.1) |
| `scott_0_87_87_t8-15_shift` | B | 2_scott_0_87_87 7.7–15.4 s | 22.7 / 9.9 | 66 / 18 | outlier knee max (z +6.1) |
| `scott_0_88_88_t10-20_shift` | B | 2_scott_0_88_88 9.6–19.9 s | 18.6 / 12.2 | 35 / 17 | knee 65 deg; outlier knee max (z +9.8) |
| `scott_0_88_88_t28-33_shift` | B | 2_scott_0_88_88 28.1–33.3 s | 23.9 / 15.9 | 24 / 9 | outlier trunk drop (z +4.3); outlier knee max (z +6.4) |
| `scott_0_88_88_t36-41_shift` | B | 2_scott_0_88_88 36.4–41.1 s | 17.0 / 11.8 | 48 / 18 | outlier knee max (z +5.8) |
| `scott_0_88_88_t62-70_shift` | B | 2_scott_0_88_88 61.6–69.8 s | 30.6 / 13.6 | 55 / 18 | human steps; outlier trunk drop (z +3.8); outlier knee max (z +6.7) |
| `scott_0_89_89_t23-28_shift` | B | 2_scott_0_89_89 22.7–27.9 s | 22.0 / 13.7 | 41 / 16 | outlier knee max (z +4.1) |
| `scott_0_8_8_t15-27_shift` | B | 2_scott_0_8_8 15.2–27.2 s | 28.5 / 16.3 | 33 / 13 | human steps; outlier knee max (z +6.3) |
| `scott_0_8_8_t56-60_shift` | B | 2_scott_0_8_8 55.6–59.6 s | 16.0 / 8.9 | 30 / 9 | outlier knee max (z +3.7) |
| `scott_0_8_8_t63-73_shift` | B | 2_scott_0_8_8 62.9–72.8 s | 17.1 / 9.2 | 38 / 12 | knee 61 deg; outlier knee max (z +8.5) |
| `scott_0_90_90_t10-15_shift` | B | 2_scott_0_90_90 9.6–14.6 s | 17.9 / 11.9 | 31 / 12 | outlier knee max (z +4.9) |
| `scott_0_90_90_t53-58_shift` | B | 2_scott_0_90_90 52.8–58.3 s | 20.5 / 12.1 | 52 / 14 | outlier knee max (z +5.5) |
| `scott_0_91_91_t28-34_shift` | B | 2_scott_0_91_91 28.0–34.0 s | 20.1 / 10.9 | 66 / 20 | outlier arms k1 cm (z +3.5); outlier knee max (z +5.1) |
| `scott_0_92_92_t17-22_shift` | B | 2_scott_0_92_92 17.2–22.1 s | 11.8 / 4.8 | 51 / 14 | outlier trunk drop (z +4.4); outlier knee max (z +4.6) |
| `scott_0_93_93_t14-18_shift` | B | 2_scott_0_93_93 14.2–18.2 s | 16.9 / 5.8 | 35 / 17 | outlier knee max (z +5.6) |
| `scott_0_93_93_t2-7_shift` | B | 2_scott_0_93_93 1.8–6.7 s | 23.1 / 14.2 | 45 / 11 | outlier knee max (z +8.0) |
| `scott_0_93_93_t45-49_shift` | B | 2_scott_0_93_93 44.6–48.8 s | 16.3 / 10.9 | 31 / 11 | outlier knee max (z +7.7) |
| `scott_0_94_94_t0-10_shift` | B | 2_scott_0_94_94 0.0–9.9 s | 19.2 / 11.8 | 36 / 13 | outlier knee max (z +7.6) |
| `scott_0_94_94_t16-24_shift` | B | 2_scott_0_94_94 16.5–23.5 s | 16.5 / 13.1 | 33 / 11 | outlier trunk drop (z +3.5); outlier knee max (z +7.9) |
| `scott_0_94_94_t22-26` | A | 2_scott_0_94_94 21.5–25.8 s | 3.4 / 1.2 | 29 / 13 | outlier trunk drop (z +4.2); outlier knee max (z +6.1) |
| `scott_0_94_94_t24-29_shift` | B | 2_scott_0_94_94 23.8–28.5 s | 17.4 / 11.7 | 44 / 17 | outlier trunk drop (z +4.5); outlier knee max (z +7.9) |
| `scott_0_95_95_t24-29` | A | 2_scott_0_95_95 24.1–29.0 s | 1.7 / 1.3 | 44 / 16 | outlier knee max (z +5.2) |
| `scott_0_95_95_t43-49` | A | 2_scott_0_95_95 43.1–48.7 s | 2.7 / 0.7 | 91 / 26 | outlier arms k1 cm (z +5.3) |
| `scott_0_96_96_t13-18_shift` | B | 2_scott_0_96_96 13.0–18.5 s | 19.2 / 11.5 | 66 / 17 | outlier knee max (z +4.6) |
| `scott_0_96_96_t23-30_shift` | B | 2_scott_0_96_96 22.6–29.8 s | 16.8 / 8.5 | 69 / 20 | outlier arms k1 cm (z +3.5); outlier knee max (z +5.7) |
| `scott_0_97_97_t27-35_shift` | B | 2_scott_0_97_97 26.9–34.8 s | 24.7 / 17.2 | 46 / 17 | outlier knee max (z +7.2) |
| `scott_0_97_97_t9-16_shift` | B | 2_scott_0_97_97 9.2–15.9 s | 14.5 / 9.0 | 38 / 11 | outlier knee max (z +5.1) |
| `scott_0_99_99_t26-31_shift` | B | 2_scott_0_99_99 25.6–30.5 s | 19.7 / 9.9 | 54 / 16 | knee 61 deg; head at limit 6%; outlier knee max (z +8.3) |
| `scott_0_99_99_t3-12_shift` | B | 2_scott_0_99_99 3.4–11.6 s | 23.3 / 21.6 | 36 / 11 | K1 feet move 22 cm; outlier knee max (z +4.5) |
| `scott_0_99_99_t40-46_shift` | B | 2_scott_0_99_99 39.9–46.2 s | 14.7 / 8.7 | 59 / 17 | outlier knee max (z +5.4) |
| `scott_0_9_9_t13-20_shift` | B | 2_scott_0_9_9 12.6–20.4 s | 16.0 / 10.6 | 49 / 14 | outlier knee max (z +4.3) |
| `scott_0_9_9_t23-28_shift` | B | 2_scott_0_9_9 23.0–28.4 s | 19.6 / 10.8 | 40 / 9 | outlier knee max (z +8.0) |
| `scott_0_9_9_t35-40_shift` | B | 2_scott_0_9_9 34.6–40.2 s | 18.5 / 9.5 | 33 / 10 | outlier knee max (z +5.4) |
| `scott_0_9_9_t50-54_shift` | B | 2_scott_0_9_9 50.5–54.5 s | 14.8 / 9.3 | 44 / 13 | outlier knee max (z +5.8) |
| `scott_1_10_10_t170-176_shift` | B | 2_scott_1_10_10 170.3–176.5 s | 22.1 / 15.6 | 43 / 15 | outlier knee max (z +7.1) |
| `scott_1_10_10_t236-241_shift` | B | 2_scott_1_10_10 235.9–240.8 s | 23.4 / 14.5 | 12 / 3 | outlier knee max (z +7.0) |
| `scott_1_10_10_t369-374_shift` | B | 2_scott_1_10_10 369.2–373.6 s | 17.7 / 11.5 | 65 / 20 | outlier arms k1 cm (z +3.7); outlier knee max (z +4.1) |
| `scott_1_11_11_t199-204_shift` | B | 2_scott_1_11_11 198.6–203.9 s | 15.5 / 15.2 | 16 / 4 | outlier knee max (z +5.7) |
| `scott_1_11_11_t209-215_shift` | B | 2_scott_1_11_11 209.1–214.5 s | 15.1 / 10.2 | 25 / 7 | outlier knee max (z +4.5) |
| `scott_1_11_11_t306-310_shift` | B | 2_scott_1_11_11 305.7–310.0 s | 24.8 / 22.3 | 42 / 14 | K1 feet move 22 cm |
| `scott_1_11_11_t362-366_shift` | B | 2_scott_1_11_11 361.8–366.0 s | 15.0 / 10.6 | 20 / 6 | outlier knee max (z +5.3) |
| `scott_1_11_11_t372-376_shift` | B | 2_scott_1_11_11 371.7–376.0 s | 16.3 / 6.9 | 42 / 12 | outlier knee max (z +8.0) |
| `scott_1_11_11_t425-430_shift` | B | 2_scott_1_11_11 425.3–429.6 s | 18.8 / 18.7 | 24 / 7 | K1 feet move 19 cm |
| `scott_1_12_12_t558-564_shift` | B | 2_scott_1_12_12 558.4–563.6 s | 23.5 / 16.5 | 27 / 7 | outlier knee max (z +4.1) |
| `scott_1_1_1_t0-8_shift` | B | 2_scott_1_1_1 0.0–8.1 s | 25.0 / 15.0 | 30 / 10 | outlier knee max (z +6.1) |
| `scott_1_1_1_t117-123_shift` | B | 2_scott_1_1_1 117.3–122.9 s | 23.5 / 11.8 | 36 / 16 | knee 73 deg; outlier trunk drop (z +3.9); outlier knee max (z +12.5) |
| `scott_1_1_1_t200-204_shift` | B | 2_scott_1_1_1 200.1–204.3 s | 19.8 / 10.1 | 25 / 11 | outlier knee max (z +3.6) |
| `scott_1_1_1_t202-208` | A | 2_scott_1_1_1 202.3–207.6 s | 0.8 / 0.8 | 58 / 23 | outlier arms k1 cm (z +4.4); outlier knee max (z +6.5) |
| `scott_1_1_1_t219-224` | A | 2_scott_1_1_1 218.8–223.6 s | 8.6 / 12.5 | 56 / 16 | K1 feet move 13 cm; outlier knee max (z +3.6) |
| `scott_1_1_1_t224-232_shift` | B | 2_scott_1_1_1 224.4–231.8 s | 16.4 / 9.2 | 28 / 9 | outlier knee max (z +6.0) |
| `scott_1_1_1_t269-275_shift` | B | 2_scott_1_1_1 269.4–274.6 s | 14.8 / 11.7 | 33 / 8 | outlier knee max (z +3.9) |
| `scott_1_1_1_t286-292_shift` | B | 2_scott_1_1_1 286.4–291.5 s | 21.2 / 11.7 | 10 / 3 | outlier knee max (z +4.7) |
| `scott_1_1_1_t295-299_shift` | B | 2_scott_1_1_1 294.8–298.8 s | 12.4 / 10.4 | 74 / 21 | outlier arms k1 cm (z +3.9) |
| `scott_1_1_1_t317-321` | A | 2_scott_1_1_1 316.6–320.6 s | 7.8 / 8.7 | 34 / 10 | K1 feet move 9 cm |
| `scott_1_1_1_t319-333_shift` | B | 2_scott_1_1_1 318.6–333.0 s | 20.5 / 10.9 | 47 / 15 | outlier knee max (z +5.5) |
| `scott_1_1_1_t337-342_shift` | B | 2_scott_1_1_1 336.6–341.5 s | 23.6 / 13.3 | 30 / 11 | outlier knee max (z +7.1) |
| `scott_1_1_1_t349-359_shift` | B | 2_scott_1_1_1 348.9–359.3 s | 24.7 / 20.2 | 47 / 17 | K1 feet move 20 cm; outlier knee max (z +6.0) |
| `scott_1_1_1_t364-368_shift` | B | 2_scott_1_1_1 364.5–368.5 s | 17.6 / 11.0 | 44 / 13 | outlier knee max (z +5.8) |
| `scott_1_1_1_t373-377_shift` | B | 2_scott_1_1_1 373.1–377.3 s | 24.6 / 15.7 | 47 / 11 | outlier knee max (z +5.3) |
| `scott_1_1_1_t406-410_shift` | B | 2_scott_1_1_1 405.9–410.4 s | 23.5 / 10.6 | 46 / 22 | outlier arms k1 cm (z +4.1); outlier knee max (z +4.4) |
| `scott_1_1_1_t55-60_shift` | B | 2_scott_1_1_1 54.7–60.3 s | 18.2 / 10.9 | 37 / 14 | outlier knee max (z +4.5) |
| `scott_1_1_1_t60-69_shift` | B | 2_scott_1_1_1 60.3–69.1 s | 19.8 / 12.6 | 37 / 15 | outlier knee max (z +4.3) |
| `scott_1_2_2_t108-118` | A | 2_scott_1_2_2 107.9–117.7 s | 7.6 / 6.5 | 17 / 9 | elbow bend at limit 21% |
| `scott_1_2_2_t116-122_shift` | B | 2_scott_1_2_2 115.7–122.1 s | 10.5 / 6.2 | 11 / 6 | head at limit 17%; shoulder at limit 9%; outlier knee max (z +3.7) |
| `scott_1_2_2_t120-133` | A | 2_scott_1_2_2 120.1–133.4 s | 8.9 / 7.6 | 19 / 10 | head at limit 16%; elbow bend at limit 12%; outlier knee max (z +3.6) |
| `scott_1_2_2_t131-136_shift` | B | 2_scott_1_2_2 131.4–135.8 s | 10.1 / 6.9 | 18 / 10 | elbow bend at limit 15%; outlier knee max (z +4.0) |
| `scott_1_2_2_t157-161_shift` | B | 2_scott_1_2_2 157.0–161.0 s | 23.2 / 13.9 | 17 / 4 | outlier knee max (z +6.6) |
| `scott_1_2_2_t172-177_shift` | B | 2_scott_1_2_2 171.6–177.4 s | 21.6 / 11.6 | 25 / 9 | outlier knee max (z +7.5) |
| `scott_1_2_2_t20-27_shift` | B | 2_scott_1_2_2 19.5–26.8 s | 19.0 / 11.1 | 23 / 11 | outlier knee max (z +4.2) |
| `scott_1_2_2_t210-215_shift` | B | 2_scott_1_2_2 209.9–215.0 s | 21.2 / 13.9 | 32 / 11 | outlier knee max (z +4.4) |
| `scott_1_2_2_t223-227_shift` | B | 2_scott_1_2_2 223.4–227.4 s | 20.4 / 10.6 | 19 / 8 | outlier knee max (z +6.7) |
| `scott_1_2_2_t250-254_shift` | B | 2_scott_1_2_2 250.2–254.2 s | 19.9 / 11.7 | 22 / 8 | outlier knee max (z +4.1) |
| `scott_1_2_2_t273-280_shift` | B | 2_scott_1_2_2 273.5–279.9 s | 18.8 / 10.6 | 18 / 6 | outlier knee max (z +5.0) |
| `scott_1_2_2_t287-292_shift` | B | 2_scott_1_2_2 287.2–292.2 s | 21.4 / 11.5 | 26 / 10 | knee 60 deg; outlier knee max (z +8.2) |
| `scott_1_2_2_t295-299_shift` | B | 2_scott_1_2_2 294.9–299.1 s | 10.3 / 6.7 | 22 / 9 | outlier knee max (z +6.9) |
| `scott_1_2_2_t297-302` | A | 2_scott_1_2_2 297.1–302.3 s | 7.7 / 4.5 | 25 / 11 | outlier knee max (z +6.7) |
| `scott_1_2_2_t343-348_shift` | B | 2_scott_1_2_2 343.1–348.3 s | 25.0 / 14.1 | 62 / 19 | knee 65 deg; outlier knee max (z +9.9) |
| `scott_1_2_2_t349-354_shift` | B | 2_scott_1_2_2 348.8–354.1 s | 22.5 / 12.2 | 11 / 5 | outlier knee max (z +7.2) |
| `scott_1_2_2_t357-361_shift` | B | 2_scott_1_2_2 356.8–360.8 s | 19.5 / 10.8 | 28 / 11 | elbow bend at limit 38%; outlier knee max (z +6.6) |
| `scott_1_2_2_t358-369` | A | 2_scott_1_2_2 357.7–369.4 s | 2.8 / 3.3 | 18 / 8 | elbow bend at limit 48% |
| `scott_1_2_2_t42-48_shift` | B | 2_scott_1_2_2 42.4–47.6 s | 20.2 / 14.6 | 39 / 17 | outlier knee max (z +4.4) |
| `scott_1_2_2_t53-57_shift` | B | 2_scott_1_2_2 53.1–57.1 s | 15.1 / 8.8 | 23 / 10 | outlier knee max (z +3.7) |
| `scott_1_2_2_t80-84_shift` | B | 2_scott_1_2_2 79.5–83.5 s | 19.0 / 10.6 | 26 / 11 | outlier knee max (z +5.7) |
| `scott_1_2_2_t96-102` | A | 2_scott_1_2_2 96.5–101.9 s | 1.2 / 1.9 | 94 / 29 | outlier arms k1 cm (z +6.1) |
| `scott_1_2_2_t98-102_shift` | B | 2_scott_1_2_2 98.4–102.4 s | 10.2 / 6.7 | 69 / 22 | outlier arms k1 cm (z +4.1) |
| `scott_1_3_3_t119-123_shift` | B | 2_scott_1_3_3 118.9–123.5 s | 17.6 / 11.3 | 25 / 7 | outlier knee max (z +4.4) |
| `scott_1_3_3_t14-21_shift` | B | 2_scott_1_3_3 14.3–21.1 s | 24.2 / 14.1 | 48 / 14 | outlier knee max (z +4.6) |
| `scott_1_3_3_t165-170_shift` | B | 2_scott_1_3_3 165.0–170.0 s | 15.4 / 8.5 | 60 / 17 | outlier knee max (z +5.2) |
| `scott_1_3_3_t185-195` | A | 2_scott_1_3_3 184.9–195.0 s | 0.7 / 0.5 | 6 / 3 | shoulder at limit 76%; self-collision right_hand_end_collision / trunk_collision 0.5 s (at 9.5 s, 8 mm) |
| `scott_1_3_3_t193-197_shift` | B | 2_scott_1_3_3 193.0–197.4 s | 9.3 / 5.4 | 17 / 7 | shoulder at limit 45%; self-collision right_hand_end_collision / trunk_collision 0.5 s (at 1.4 s, 8 mm) |
| `scott_1_3_3_t199-205_shift` | B | 2_scott_1_3_3 198.9–204.8 s | 18.0 / 10.4 | 29 / 9 | hand presses into leg 8 mm for 0.1 s (at 2.2 s) |
| `scott_1_3_3_t22-28_shift` | B | 2_scott_1_3_3 22.3–27.8 s | 14.8 / 13.1 | 15 / 5 | shoulder at limit 57% |
| `scott_1_3_3_t232-241_shift` | B | 2_scott_1_3_3 232.2–241.2 s | 20.5 / 13.4 | 12 / 3 | outlier knee max (z +5.3) |
| `scott_1_3_3_t241-249_shift` | B | 2_scott_1_3_3 241.3–249.3 s | 21.8 / 11.3 | 13 / 4 | outlier knee max (z +6.8) |
| `scott_1_3_3_t257-264` | A | 2_scott_1_3_3 256.7–263.8 s | 9.6 / 7.3 | 21 / 5 | outlier knee max (z +3.7) |
| `scott_1_3_3_t270-281` | A | 2_scott_1_3_3 270.3–280.7 s | 5.8 / 1.5 | 47 / 21 | outlier arms k1 cm (z +3.9) |
| `scott_1_3_3_t286-294_shift` | B | 2_scott_1_3_3 286.1–293.7 s | 21.1 / 14.3 | 52 / 17 | outlier knee max (z +4.3) |
| `scott_1_3_3_t313-319` | A | 2_scott_1_3_3 313.0–319.0 s | 5.9 / 0.6 | 45 / 14 | outlier trunk drop (z +4.8); outlier knee max (z +7.8) |
| `scott_1_3_3_t363-367_shift` | B | 2_scott_1_3_3 363.1–367.1 s | 25.0 / 14.0 | 49 / 19 | upper-arm twist at limit 8%; outlier knee max (z +6.4) |
| `scott_1_3_3_t369-373_shift` | B | 2_scott_1_3_3 369.1–373.1 s | 20.4 / 12.0 | 33 / 8 | outlier knee max (z +4.5) |
| `scott_1_3_3_t375-382_shift` | B | 2_scott_1_3_3 375.1–382.4 s | 18.8 / 10.1 | 40 / 11 | outlier knee max (z +3.8) |
| `scott_1_3_3_t397-406` | A | 2_scott_1_3_3 396.8–406.0 s | 0.8 / 0.8 | 11 / 5 | shoulder at limit 72% |
| `scott_1_3_3_t447-452_shift` | B | 2_scott_1_3_3 447.3–452.4 s | 17.3 / 8.8 | 37 / 11 | outlier knee max (z +5.4) |
| `scott_1_3_3_t478-485` | A | 2_scott_1_3_3 477.6–484.6 s | 2.0 / 1.2 | 24 / 10 | elbow bend at limit 24% |
| `scott_1_3_3_t50-59_shift` | B | 2_scott_1_3_3 50.1–59.2 s | 21.4 / 10.7 | 46 / 14 | outlier knee max (z +5.2) |
| `scott_1_3_3_t527-537_shift` | B | 2_scott_1_3_3 527.0–536.9 s | 23.1 / 14.1 | 54 / 18 | knee 61 deg; outlier knee max (z +8.5) |
| `scott_1_3_3_t537-541_shift` | B | 2_scott_1_3_3 536.9–540.9 s | 11.8 / 5.1 | 64 / 21 | outlier arms k1 cm (z +3.8) |
| `scott_1_3_3_t538-542` | A | 2_scott_1_3_3 537.6–541.7 s | 1.6 / 1.8 | 66 / 20 | outlier arms k1 cm (z +3.7) |
| `scott_1_3_3_t558-562_shift` | B | 2_scott_1_3_3 558.2–562.3 s | 21.9 / 10.6 | 69 / 18 | outlier knee max (z +6.3) |
| `scott_1_3_3_t572-577_shift` | B | 2_scott_1_3_3 572.1–577.5 s | 22.5 / 14.5 | 19 / 6 | outlier knee max (z +5.4) |
| `scott_1_3_3_t575-582` | A | 2_scott_1_3_3 575.5–582.4 s | 6.8 / 7.7 | 25 / 9 | outlier knee max (z +4.3) |
| `scott_1_3_3_t580-585_shift` | B | 2_scott_1_3_3 580.4–584.6 s | 39.9 / 20.9 | 29 / 12 | human steps; K1 feet move 21 cm; outlier knee max (z +4.2) |
| `scott_1_3_3_t587-591_shift` | B | 2_scott_1_3_3 587.1–591.1 s | 24.2 / 12.5 | 54 / 20 | outlier arms k1 cm (z +3.5) |
| `scott_1_3_3_t607-612_shift` | B | 2_scott_1_3_3 607.0–611.6 s | 18.8 / 12.3 | 34 / 14 | outlier knee max (z +5.9) |
| `scott_1_3_3_t62-66_shift` | B | 2_scott_1_3_3 61.6–65.6 s | 13.0 / 7.7 | 24 / 13 | outlier knee max (z +4.4) |
| `scott_1_3_3_t66-73_shift` | B | 2_scott_1_3_3 65.8–72.7 s | 18.1 / 11.8 | 36 / 14 | outlier knee max (z +5.1) |
| `scott_1_3_3_t81-90_shift` | B | 2_scott_1_3_3 80.5–89.5 s | 23.3 / 13.1 | 50 / 15 | outlier knee max (z +5.0) |
| `scott_1_4_4_t107-115_shift` | B | 2_scott_1_4_4 106.7–114.5 s | 20.1 / 17.7 | 31 / 13 | outlier knee max (z +4.8) |
| `scott_1_4_4_t12-17_shift` | B | 2_scott_1_4_4 12.0–16.7 s | 16.1 / 10.4 | 22 / 11 | outlier knee max (z +4.6) |
| `scott_1_4_4_t155-160` | A | 2_scott_1_4_4 154.8–159.7 s | 1.1 / 0.5 | 73 / 20 | outlier arms k1 cm (z +3.6) |
| `scott_1_4_4_t200-207` | A | 2_scott_1_4_4 200.2–206.6 s | 7.4 / 4.4 | 17 / 7 | outlier knee max (z +4.0) |
| `scott_1_4_4_t211-216_shift` | B | 2_scott_1_4_4 210.5–215.6 s | 22.6 / 11.7 | 37 / 15 | outlier knee max (z +4.1) |
| `scott_1_4_4_t224-228_shift` | B | 2_scott_1_4_4 223.7–228.1 s | 20.6 / 14.4 | 71 / 20 | outlier arms k1 cm (z +3.7) |
| `scott_1_4_4_t232-237` | A | 2_scott_1_4_4 232.1–237.1 s | 1.4 / 0.4 | 18 / 9 | elbow bend at limit 38% |
| `scott_1_4_4_t235-240_shift` | B | 2_scott_1_4_4 235.1–239.7 s | 6.1 / 4.1 | 44 / 13 | elbow bend at limit 15% |
| `scott_1_4_4_t315-319_shift` | B | 2_scott_1_4_4 314.6–319.1 s | 11.1 / 7.0 | 22 / 8 | outlier knee max (z +3.9) |
| `scott_1_4_4_t317-322` | A | 2_scott_1_4_4 317.1–322.3 s | 0.5 / 0.3 | 7 / 4 | head at limit 27% |
| `scott_1_4_4_t358-364` | A | 2_scott_1_4_4 358.3–363.5 s | 5.5 / 5.0 | 23 / 10 | elbow bend at limit 6% |
| `scott_1_4_4_t398-404_shift` | B | 2_scott_1_4_4 398.2–404.1 s | 19.2 / 11.8 | 16 / 7 | knee 60 deg; outlier knee max (z +8.1) |
| `scott_1_4_4_t407-411_shift` | B | 2_scott_1_4_4 406.7–411.0 s | 24.3 / 10.7 | 31 / 10 | outlier knee max (z +3.7) |
| `scott_1_4_4_t418-422` | A | 2_scott_1_4_4 418.2–422.5 s | 1.4 / 3.4 | 12 / 7 | head at limit 12%; elbow bend at limit 9% |
| `scott_1_4_4_t420-429_shift` | B | 2_scott_1_4_4 420.5–428.6 s | 14.6 / 7.0 | 10 / 5 | head at limit 42% |
| `scott_1_4_4_t427-433` | A | 2_scott_1_4_4 426.6–433.2 s | 6.5 / 1.3 | 9 / 5 | head at limit 36%; shoulder at limit 26% |
| `scott_1_4_4_t431-436_shift` | B | 2_scott_1_4_4 431.2–436.0 s | 21.4 / 10.8 | 22 / 9 | head at limit 21%; shoulder at limit 34%; outlier knee max (z +5.0) |
| `scott_1_4_4_t475-482_shift` | B | 2_scott_1_4_4 474.9–482.3 s | 16.5 / 9.8 | 35 / 11 | outlier knee max (z +5.1) |
| `scott_1_4_4_t48-52_shift` | B | 2_scott_1_4_4 47.7–51.9 s | 18.1 / 13.6 | 18 / 6 | outlier knee max (z +3.7) |
| `scott_1_4_4_t523-528_shift` | B | 2_scott_1_4_4 522.9–528.4 s | 14.0 / 13.8 | 48 / 12 | outlier knee max (z +4.8) |
| `scott_1_4_4_t53-57_shift` | B | 2_scott_1_4_4 53.4–57.4 s | 12.7 / 14.3 | 28 / 8 | elbow bend at limit 29% |
| `scott_1_4_4_t54-65` | A | 2_scott_1_4_4 54.2–65.1 s | 2.7 / 0.6 | 22 / 8 | elbow bend at limit 26% |
| `scott_1_4_4_t579-586_shift` | B | 2_scott_1_4_4 579.0–586.3 s | 24.5 / 14.0 | 35 / 13 | outlier knee max (z +6.9) |
| `scott_1_4_4_t67-71_shift` | B | 2_scott_1_4_4 66.6–70.6 s | 21.5 / 9.3 | 29 / 13 | knee 71 deg; outlier knee max (z +11.8) |
| `scott_1_4_4_t94-99` | A | 2_scott_1_4_4 93.9–99.4 s | 0.8 / 0.5 | 34 / 22 | outlier arms k1 cm (z +4.1) |
| `scott_1_4_4_t96-100_shift` | B | 2_scott_1_4_4 96.2–100.2 s | 11.3 / 7.7 | 30 / 24 | outlier arms k1 cm (z +4.7) |
| `scott_1_5_5_t138-143_shift` | B | 2_scott_1_5_5 138.2–142.9 s | 20.6 / 18.8 | 38 / 12 | K1 feet move 19 cm; outlier knee max (z +4.2) |
| `scott_1_5_5_t210-215_shift` | B | 2_scott_1_5_5 209.7–215.4 s | 18.5 / 15.5 | 59 / 22 | shoulder at limit 7%; upper-arm twist at limit 30%; leg at limit 9%; outlier arms k1 cm (z +4.2) |
| `scott_1_5_5_t246-250` | A | 2_scott_1_5_5 245.7–249.9 s | 9.2 / 6.6 | 101 / 30 | outlier arms k1 cm (z +6.3) |
| `scott_1_5_5_t263-268` | A | 2_scott_1_5_5 263.2–268.1 s | 9.3 / 10.3 | 24 / 10 | K1 feet move 10 cm |
| `scott_1_5_5_t366-374_shift` | B | 2_scott_1_5_5 366.4–373.6 s | 25.0 / 17.6 | 19 / 6 | outlier knee max (z +4.1) |
| `scott_1_5_5_t38-42` | A | 2_scott_1_5_5 37.5–42.0 s | 6.3 / 10.7 | 33 / 14 | K1 feet move 11 cm |
| `scott_1_5_5_t471-475_shift` | B | 2_scott_1_5_5 470.9–475.1 s | 21.6 / 21.3 | 50 / 14 | K1 feet move 21 cm |
| `scott_1_5_5_t530-538_shift` | B | 2_scott_1_5_5 530.5–538.0 s | 22.6 / 22.6 | 30 / 8 | K1 feet move 23 cm |
| `scott_1_5_5_t550-554_shift` | B | 2_scott_1_5_5 549.6–554.5 s | 12.4 / 13.6 | 30 / 9 | outlier knee max (z +6.6) |
| `scott_1_6_6_t2-7` | A | 2_scott_1_6_6 1.6–6.6 s | 1.0 / 0.5 | 10 / 2 | shoulder at limit 60% |
| `scott_1_6_6_t27-32_shift` | B | 2_scott_1_6_6 27.3–32.4 s | 16.2 / 14.6 | 62 / 22 | outlier arms k1 cm (z +4.1) |
| `scott_1_6_6_t318-325_shift` | B | 2_scott_1_6_6 318.0–325.4 s | 23.5 / 12.9 | 30 / 9 | outlier knee max (z +7.2) |
| `scott_1_6_6_t351-359` | A | 2_scott_1_6_6 351.3–358.5 s | 9.1 / 5.2 | 19 / 6 | shoulder at limit 46%; self-collision right_hand_end_collision / trunk_collision 1.1 s (at 4.6 s, 10 mm) |
| `scott_1_6_6_t402-406_shift` | B | 2_scott_1_6_6 401.5–406.2 s | 21.7 / 15.4 | 36 / 10 | outlier knee max (z +4.8) |
| `scott_1_6_6_t419-427_shift` | B | 2_scott_1_6_6 419.5–426.6 s | 22.5 / 12.1 | 45 / 15 | outlier knee max (z +7.4) |
| `scott_1_6_6_t73-78_shift` | B | 2_scott_1_6_6 72.8–78.0 s | 21.6 / 15.3 | 77 / 22 | outlier arms k1 cm (z +4.0) |
| `scott_1_7_7_t148-152_shift` | B | 2_scott_1_7_7 147.6–151.6 s | 13.8 / 8.2 | 10 / 3 | outlier knee max (z +4.7) |
| `scott_1_7_7_t204-208_shift` | B | 2_scott_1_7_7 203.9–208.4 s | 16.8 / 16.4 | 31 / 9 | outlier knee max (z +6.0) |
| `scott_1_7_7_t25-29_shift` | B | 2_scott_1_7_7 24.6–28.9 s | 14.2 / 10.4 | 28 / 12 | outlier knee max (z +6.3) |
| `scott_1_7_7_t290-294_shift` | B | 2_scott_1_7_7 290.3–294.3 s | 22.3 / 13.6 | 28 / 7 | outlier knee max (z +5.8) |
| `scott_1_7_7_t314-318_shift` | B | 2_scott_1_7_7 314.3–318.4 s | 22.6 / 17.2 | 51 / 14 | outlier knee max (z +4.6) |
| `scott_1_7_7_t377-382_shift` | B | 2_scott_1_7_7 377.0–382.2 s | 21.9 / 13.5 | 100 / 29 | outlier arms k1 cm (z +6.1); outlier knee max (z +6.3) |
| `scott_1_7_7_t389-394_shift` | B | 2_scott_1_7_7 389.4–394.0 s | 24.6 / 14.6 | 42 / 11 | outlier knee max (z +6.9) |
| `scott_1_7_7_t449-454_shift` | B | 2_scott_1_7_7 448.7–453.6 s | 24.6 / 18.6 | 32 / 9 | K1 feet move 19 cm; outlier knee max (z +5.3) |
| `scott_1_7_7_t463-469_shift` | B | 2_scott_1_7_7 463.4–469.0 s | 21.4 / 13.8 | 29 / 13 | outlier knee max (z +5.2) |
| `scott_1_7_7_t533-537_shift` | B | 2_scott_1_7_7 532.8–537.2 s | 13.2 / 6.8 | 52 / 24 | outlier arms k1 cm (z +4.8) |
| `scott_1_7_7_t597-601_shift` | B | 2_scott_1_7_7 597.0–601.0 s | 20.4 / 8.5 | 11 / 4 | outlier knee max (z +4.9) |
| `scott_1_7_7_t6-10_shift` | B | 2_scott_1_7_7 6.5–10.5 s | 24.7 / 19.4 | 10 / 5 | K1 feet move 19 cm; outlier knee max (z +5.4) |
| `scott_1_8_8_t248-252_shift` | B | 2_scott_1_8_8 248.4–252.5 s | 24.9 / 13.9 | 27 / 11 | outlier knee max (z +5.1) |
| `scott_1_8_8_t307-313_shift` | B | 2_scott_1_8_8 306.8–313.2 s | 21.8 / 20.3 | 50 / 13 | K1 feet move 20 cm; outlier knee max (z +5.6) |
| `scott_1_8_8_t316-320_shift` | B | 2_scott_1_8_8 315.6–320.2 s | 24.9 / 15.6 | 21 / 5 | outlier knee max (z +4.9) |
| `scott_1_8_8_t399-405_shift` | B | 2_scott_1_8_8 399.3–405.1 s | 20.0 / 15.8 | 23 / 7 | outlier knee max (z +5.5) |
| `scott_1_8_8_t477-481_shift` | B | 2_scott_1_8_8 477.2–481.2 s | 18.0 / 10.1 | 20 / 5 | outlier knee max (z +6.5) |
| `scott_1_8_8_t478-482` | A | 2_scott_1_8_8 478.1–482.3 s | 6.3 / 10.7 | 20 / 5 | K1 feet move 11 cm |
| `scott_1_9_9_t113-118_shift` | B | 2_scott_1_9_9 113.2–118.0 s | 23.4 / 17.7 | 13 / 5 | outlier knee max (z +3.9) |
| `scott_1_9_9_t26-30_shift` | B | 2_scott_1_9_9 25.6–29.6 s | 23.2 / 20.5 | 5 / 2 | K1 feet move 20 cm |
| `scott_1_9_9_t392-396_shift` | B | 2_scott_1_9_9 391.8–396.2 s | 15.7 / 9.2 | 60 / 21 | outlier arms k1 cm (z +3.8) |
| `scott_1_9_9_t624-628_shift` | B | 2_scott_1_9_9 624.3–628.3 s | 19.8 / 16.8 | 32 / 11 | outlier knee max (z +7.1) |
| `solomon_0_100_100_t29-46` | A | 3_solomon_0_100_100 29.1–45.9 s | 2.3 / 0.9 | 18 / 5 | outlier knee max (z +5.9) |
| `solomon_0_101_101_t24-44` | A | 3_solomon_0_101_101 24.2–43.7 s | 3.7 / 1.3 | 19 / 6 | outlier knee max (z +4.0) |
| `solomon_0_102_102_t14-22_shift` | B | 3_solomon_0_102_102 14.5–21.8 s | 23.6 / 14.7 | 22 / 6 | outlier knee max (z +4.2) |
| `solomon_0_102_102_t27-44` | A | 3_solomon_0_102_102 27.2–43.5 s | 2.6 / 1.1 | 18 / 5 | outlier knee max (z +4.2) |
| `solomon_0_103_103_t23-31_shift` | B | 3_solomon_0_103_103 23.3–31.3 s | 23.9 / 14.5 | 22 / 6 | outlier knee max (z +3.9) |
| `solomon_0_103_103_t29-43` | A | 3_solomon_0_103_103 29.3–43.0 s | 9.0 / 5.5 | 28 / 7 | outlier trunk drop (z +5.2); outlier knee max (z +6.4) |
| `solomon_0_104_104_t27-33_shift` | B | 3_solomon_0_104_104 27.1–33.4 s | 15.6 / 9.0 | 15 / 5 | outlier knee max (z +5.6) |
| `solomon_0_104_104_t45-55_shift` | B | 3_solomon_0_104_104 44.9–54.5 s | 10.8 / 6.4 | 21 / 8 | outlier knee max (z +5.2) |
| `solomon_0_105_105_t38-42_shift` | B | 3_solomon_0_105_105 37.8–41.8 s | 11.3 / 7.8 | 53 / 14 | shoulder at limit 7%; outlier trunk drop (z +3.7); outlier knee max (z +4.9) |
| `solomon_0_108_108_t52-69` | A | 3_solomon_0_108_108 51.6–68.8 s | 6.8 / 4.0 | 34 / 7 | outlier knee max (z +3.9) |
| `solomon_0_10_10_t43-47_shift` | B | 3_solomon_0_10_10 42.8–47.0 s | 28.3 / 17.9 | 26 / 8 | human steps |
| `solomon_0_112_112_t33-47` | A | 3_solomon_0_112_112 33.3–47.4 s | 9.8 / 7.0 | 27 / 8 | outlier knee max (z +3.9) |
| `solomon_0_113_113_t30-41` | A | 3_solomon_0_113_113 30.3–40.8 s | 10.9 / 6.6 | 28 / 10 | human steps |
| `solomon_0_11_11_t17-37_shift` | B | 3_solomon_0_11_11 17.0–36.7 s | 30.4 / 17.5 | 24 / 6 | human steps; outlier knee max (z +4.5) |
| `solomon_0_12_12_t40-47` | A | 3_solomon_0_12_12 40.0–46.7 s | 5.6 / 1.0 | 67 / 23 | outlier arms k1 cm (z +4.4); outlier knee max (z +3.9) |
| `solomon_0_12_12_t43-47_shift` | B | 3_solomon_0_12_12 43.3–47.3 s | 24.5 / 14.8 | 68 / 22 | outlier arms k1 cm (z +4.1); outlier knee max (z +4.7) |
| `solomon_0_13_13_t14-20` | A | 3_solomon_0_13_13 14.5–20.0 s | 3.4 / 1.9 | 77 / 23 | outlier arms k1 cm (z +4.5) |
| `solomon_0_13_13_t29-40_shift` | B | 3_solomon_0_13_13 29.1–40.1 s | 25.6 / 16.2 | 48 / 14 | human steps; upper-arm twist at limit 8% |
| `solomon_0_14_14_t65-70` | A | 3_solomon_0_14_14 64.5–70.1 s | 8.2 / 5.1 | 37 / 13 | outlier trunk drop (z +3.6); outlier knee max (z +4.5) |
| `solomon_0_15_15_t0-6_shift` | B | 3_solomon_0_15_15 0.0–5.8 s | 18.3 / 9.5 | 27 / 8 | outlier knee max (z +3.7) |
| `solomon_0_15_15_t30-45_shift` | B | 3_solomon_0_15_15 30.2–45.1 s | 17.4 / 11.8 | 45 / 13 | outlier knee max (z +4.2) |
| `solomon_0_15_15_t6-13_shift` | B | 3_solomon_0_15_15 6.4–12.9 s | 23.5 / 14.2 | 35 / 9 | outlier knee max (z +3.5) |
| `solomon_0_16_16_t19-23_shift` | B | 3_solomon_0_16_16 19.1–23.4 s | 17.4 / 10.3 | 99 / 28 | upper-arm twist at limit 30%; outlier arms k1 cm (z +5.7) |
| `solomon_0_17_17_t41-45_shift` | B | 3_solomon_0_17_17 40.6–44.6 s | 23.1 / 14.2 | 47 / 13 | outlier knee max (z +3.9) |
| `solomon_0_17_17_t50-64_shift` | B | 3_solomon_0_17_17 49.9–64.1 s | 14.9 / 8.7 | 52 / 14 | outlier knee max (z +4.1) |
| `solomon_0_18_18_t8-12_shift` | B | 3_solomon_0_18_18 7.7–12.2 s | 9.3 / 6.8 | 28 / 7 | outlier knee max (z +4.9) |
| `solomon_0_19_19_t56-64_shift` | B | 3_solomon_0_19_19 55.6–64.3 s | 24.3 / 14.9 | 38 / 10 | outlier knee max (z +4.6) |
| `solomon_0_19_19_t9-17_shift` | B | 3_solomon_0_19_19 8.6–17.1 s | 14.1 / 7.0 | 31 / 10 | outlier knee max (z +4.1) |
| `solomon_0_1_1_t28-32_shift` | B | 3_solomon_0_1_1 27.5–31.5 s | 25.3 / 15.4 | 50 / 12 | human steps |
| `solomon_0_20_20_t0-8_shift` | B | 3_solomon_0_20_20 0.0–8.1 s | 13.3 / 8.2 | 51 / 13 | outlier knee max (z +3.8) |
| `solomon_0_20_20_t26-39_shift` | B | 3_solomon_0_20_20 25.5–38.6 s | 20.0 / 12.1 | 28 / 7 | outlier knee max (z +4.8) |
| `solomon_0_20_20_t49-62_shift` | B | 3_solomon_0_20_20 49.5–62.4 s | 18.6 / 10.8 | 50 / 14 | outlier knee max (z +3.9) |
| `solomon_0_21_21_t0-4` | A | 3_solomon_0_21_21 0.0–4.0 s | 9.9 / 5.0 | 23 / 5 | outlier knee max (z +3.6) |
| `solomon_0_21_21_t32-39_shift` | B | 3_solomon_0_21_21 31.6–38.9 s | 18.3 / 11.0 | 29 / 8 | outlier knee max (z +3.9) |
| `solomon_0_22_22_t42-53` | A | 3_solomon_0_22_22 41.5–53.5 s | 4.3 / 2.6 | 25 / 7 | outlier knee max (z +4.2) |
| `solomon_0_22_22_t62-67` | A | 3_solomon_0_22_22 62.1–67.4 s | 4.9 / 1.4 | 52 / 16 | outlier knee max (z +3.7) |
| `solomon_0_23_23_t0-4_shift` | B | 3_solomon_0_23_23 0.2–4.2 s | 21.3 / 12.7 | 5 / 2 | outlier knee max (z +4.1) |
| `solomon_0_23_23_t62-69_shift` | B | 3_solomon_0_23_23 61.9–69.2 s | 21.6 / 12.9 | 34 / 9 | outlier knee max (z +5.5) |
| `solomon_0_23_23_t9-13_shift` | B | 3_solomon_0_23_23 8.8–12.8 s | 23.7 / 15.9 | 31 / 8 | outlier knee max (z +4.9) |
| `solomon_0_24_24_t0-5_shift` | B | 3_solomon_0_24_24 0.0–4.7 s | 12.4 / 9.5 | 20 / 5 | outlier knee max (z +4.3) |
| `solomon_0_24_24_t17-25_shift` | B | 3_solomon_0_24_24 17.1–25.2 s | 12.2 / 7.1 | 34 / 11 | outlier knee max (z +4.1) |
| `solomon_0_25_25_t26-31_shift` | B | 3_solomon_0_25_25 26.4–30.9 s | 10.2 / 5.1 | 30 / 11 | outlier knee max (z +3.6) |
| `solomon_0_25_25_t43-51_shift` | B | 3_solomon_0_25_25 42.6–50.7 s | 27.1 / 16.5 | 23 / 7 | human steps; outlier knee max (z +3.9) |
| `solomon_0_25_25_t52-63_shift` | B | 3_solomon_0_25_25 51.8–62.8 s | 23.0 / 13.5 | 29 / 9 | outlier trunk drop (z +4.0); outlier knee max (z +6.6) |
| `solomon_0_25_25_t61-65` | A | 3_solomon_0_25_25 60.8–65.3 s | 7.2 / 1.9 | 31 / 7 | outlier trunk drop (z +3.7); outlier knee max (z +6.6) |
| `solomon_0_25_25_t63-72_shift` | B | 3_solomon_0_25_25 63.3–71.8 s | 18.7 / 11.0 | 32 / 8 | outlier knee max (z +5.1) |
| `solomon_0_28_28_t16-31` | A | 3_solomon_0_28_28 15.7–31.4 s | 6.4 / 2.8 | 25 / 7 | outlier knee max (z +4.3) |
| `solomon_0_29_29_t44-57` | A | 3_solomon_0_29_29 43.5–56.8 s | 8.7 / 4.7 | 35 / 10 | outlier knee max (z +3.8) |
| `solomon_0_2_2_t25-34_shift` | B | 3_solomon_0_2_2 24.7–33.8 s | 15.0 / 9.2 | 43 / 11 | outlier knee max (z +5.5) |
| `solomon_0_31_31_t57-64_shift` | B | 3_solomon_0_31_31 57.0–64.2 s | 19.7 / 11.8 | 49 / 13 | outlier knee max (z +4.0) |
| `solomon_0_32_32_t14-27` | A | 3_solomon_0_32_32 13.7–27.4 s | 10.4 / 7.7 | 39 / 10 | human steps |
| `solomon_0_35_35_t16-33` | A | 3_solomon_0_35_35 16.4–32.8 s | 10.4 / 6.0 | 24 / 6 | human steps |
| `solomon_0_37_37_t0-17` | A | 3_solomon_0_37_37 0.0–17.4 s | 6.0 / 3.2 | 29 / 6 | outlier knee max (z +5.5) |
| `solomon_0_38_38_t49-61` | A | 3_solomon_0_38_38 49.5–61.1 s | 4.4 / 1.3 | 36 / 10 | outlier trunk drop (z +4.3); outlier knee max (z +3.9) |
| `solomon_0_3_3_t37-42_shift` | B | 3_solomon_0_3_3 37.0–41.8 s | 23.5 / 14.0 | 40 / 11 | outlier knee max (z +4.9) |
| `solomon_0_42_42_t34-51` | A | 3_solomon_0_42_42 34.0–51.0 s | 11.7 / 7.2 | 49 / 13 | human steps |
| `solomon_0_42_42_t51-57_shift` | B | 3_solomon_0_42_42 51.4–56.8 s | 23.3 / 14.3 | 32 / 10 | outlier knee max (z +4.4) |
| `solomon_0_45_45_t31-45_shift` | B | 3_solomon_0_45_45 30.6–44.8 s | 14.4 / 9.3 | 15 / 4 | outlier knee max (z +3.6) |
| `solomon_0_47_47_t52-60_shift` | B | 3_solomon_0_47_47 52.2–59.8 s | 33.2 / 20.4 | 41 / 10 | human steps; K1 feet move 20 cm; outlier knee max (z +4.4) |
| `solomon_0_48_48_t10-24` | A | 3_solomon_0_48_48 9.7–23.9 s | 4.0 / 2.0 | 38 / 9 | upper-arm twist at limit 7% |
| `solomon_0_48_48_t24-38` | A | 3_solomon_0_48_48 23.9–38.1 s | 10.1 / 5.9 | 31 / 8 | human steps |
| `solomon_0_4_4_t2-6_shift` | B | 3_solomon_0_4_4 2.0–6.4 s | 19.4 / 11.3 | 42 / 12 | shoulder at limit 6% |
| `solomon_0_4_4_t24-43_shift` | B | 3_solomon_0_4_4 24.3–42.6 s | 19.4 / 11.4 | 42 / 10 | outlier knee max (z +3.5) |
| `solomon_0_4_4_t55-66_shift` | B | 3_solomon_0_4_4 54.7–66.2 s | 18.4 / 11.0 | 38 / 8 | outlier knee max (z +5.0) |
| `solomon_0_50_50_t30-45` | A | 3_solomon_0_50_50 29.9–44.8 s | 15.1 / 9.5 | 22 / 7 | human steps; K1 feet move 10 cm |
| `solomon_0_57_57_t17-30` | A | 3_solomon_0_57_57 17.3–29.9 s | 10.0 / 7.3 | 40 / 13 | human steps |
| `solomon_0_57_57_t2-7_shift` | B | 3_solomon_0_57_57 2.2–6.7 s | 8.9 / 4.8 | 27 / 9 | outlier knee max (z +4.1) |
| `solomon_0_5_5_t56-63_shift` | B | 3_solomon_0_5_5 55.5–63.3 s | 13.7 / 7.9 | 29 / 8 | outlier knee max (z +3.8) |
| `solomon_0_5_5_t79-85_shift` | B | 3_solomon_0_5_5 78.5–84.8 s | 28.8 / 17.4 | 30 / 8 | human steps |
| `solomon_0_63_63_t32-37_shift` | B | 3_solomon_0_63_63 32.5–37.1 s | 15.3 / 9.7 | 23 / 6 | outlier knee max (z +4.6) |
| `solomon_0_63_63_t51-59_shift` | B | 3_solomon_0_63_63 51.1–58.8 s | 26.2 / 16.6 | 56 / 15 | human steps |
| `solomon_0_66_66_t34-43` | A | 3_solomon_0_66_66 33.8–42.7 s | 4.9 / 1.2 | 32 / 7 | outlier knee max (z +3.9) |
| `solomon_0_66_66_t41-45_shift` | B | 3_solomon_0_66_66 40.7–45.0 s | 8.3 / 5.7 | 43 / 9 | outlier knee max (z +3.7) |
| `solomon_0_67_67_t0-19` | A | 3_solomon_0_67_67 0.0–19.3 s | 3.2 / 1.0 | 21 / 5 | outlier knee max (z +4.9) |
| `solomon_0_67_67_t19-38` | A | 3_solomon_0_67_67 19.3–38.5 s | 10.2 / 6.6 | 27 / 8 | human steps |
| `solomon_0_68_68_t16-31` | A | 3_solomon_0_68_68 15.7–31.4 s | 3.3 / 0.8 | 10 / 3 | outlier knee max (z +3.5) |
| `solomon_0_6_6_t29-36_shift` | B | 3_solomon_0_6_6 29.2–35.7 s | 18.9 / 10.7 | 49 / 12 | outlier knee max (z +3.8) |
| `solomon_0_72_72_t31-38_shift` | B | 3_solomon_0_72_72 30.5–38.4 s | 18.8 / 11.4 | 26 / 7 | outlier knee max (z +4.9) |
| `solomon_0_7_7_t22-28_shift` | B | 3_solomon_0_7_7 22.1–28.5 s | 25.6 / 15.8 | 48 / 13 | human steps |
| `solomon_0_8_8_t21-32_shift` | B | 3_solomon_0_8_8 21.3–32.0 s | 23.2 / 13.6 | 26 / 7 | outlier knee max (z +5.8) |
| `solomon_0_8_8_t78-83_shift` | B | 3_solomon_0_8_8 78.3–83.4 s | 8.7 / 2.1 | 51 / 14 | outlier knee max (z +5.0) |
| `solomon_0_93_93_t15-31` | A | 3_solomon_0_93_93 15.5–30.9 s | 1.0 / 0.6 | 33 / 9 | self-collision left_hand_end_collision / right_hand_end_collision 0.2 s (at 11.4 s, 9 mm) |
| `solomon_0_95_95_t42-49_shift` | B | 3_solomon_0_95_95 42.3–49.4 s | 18.5 / 12.8 | 38 / 11 | shoulder at limit 8% |
| `solomon_0_95_95_t57-64` | A | 3_solomon_0_95_95 57.2–64.1 s | 2.3 / 0.9 | 30 / 9 | outlier knee max (z +4.0) |
| `solomon_0_96_96_t22-27_shift` | B | 3_solomon_0_96_96 21.6–27.4 s | 21.0 / 13.0 | 31 / 10 | outlier knee max (z +3.7) |
| `solomon_0_96_96_t33-39` | A | 3_solomon_0_96_96 33.5–39.0 s | 8.5 / 5.2 | 31 / 8 | outlier knee max (z +3.5) |
| `solomon_0_96_96_t37-45_shift` | B | 3_solomon_0_96_96 37.0–44.6 s | 18.7 / 11.9 | 37 / 9 | outlier trunk drop (z +4.9); outlier knee max (z +5.4) |
| `solomon_0_97_97_t18-32_shift` | B | 3_solomon_0_97_97 18.5–31.6 s | 20.6 / 12.6 | 23 / 6 | outlier knee max (z +5.0) |
| `solomon_0_97_97_t30-39` | A | 3_solomon_0_97_97 29.6–39.5 s | 3.6 / 1.5 | 21 / 6 | outlier trunk drop (z +3.7); outlier knee max (z +6.3) |
| `solomon_0_97_97_t40-45_shift` | B | 3_solomon_0_97_97 40.0–45.1 s | 23.1 / 13.3 | 52 / 12 | outlier knee max (z +5.4) |
| `solomon_0_97_97_t43-50` | A | 3_solomon_0_97_97 43.1–49.7 s | 1.1 / 0.4 | 40 / 11 | outlier knee max (z +6.8) |
| `solomon_0_97_97_t46-50_shift` | B | 3_solomon_0_97_97 46.2–50.2 s | 17.8 / 7.2 | 22 / 7 | outlier trunk drop (z +3.8); outlier knee max (z +6.8) |
| `solomon_0_98_98_t0-19` | A | 3_solomon_0_98_98 0.0–18.8 s | 8.0 / 4.3 | 25 / 7 | outlier trunk drop (z +5.2); outlier knee max (z +6.5) |
| `solomon_0_98_98_t17-21_shift` | B | 3_solomon_0_98_98 16.8–21.4 s | 8.5 / 4.7 | 67 / 18 | outlier trunk drop (z +5.2); outlier knee max (z +6.5) |
| `solomon_0_98_98_t19-39` | A | 3_solomon_0_98_98 19.4–39.1 s | 3.9 / 2.7 | 48 / 12 | outlier trunk drop (z +4.7); outlier knee max (z +4.9) |
| `solomon_0_9_9_t20-34_shift` | B | 3_solomon_0_9_9 19.8–34.0 s | 17.9 / 12.3 | 29 / 8 | outlier knee max (z +3.8) |
| `solomon_1_10_10_t207-213_shift` | B | 3_solomon_1_10_10 207.1–212.8 s | 21.9 / 13.6 | 15 / 5 | outlier knee max (z +4.9) |
| `solomon_1_10_10_t331-340_shift` | B | 3_solomon_1_10_10 331.1–340.0 s | 25.0 / 16.3 | 16 / 5 | outlier knee max (z +4.6) |
| `solomon_1_10_10_t383-387_shift` | B | 3_solomon_1_10_10 382.9–387.0 s | 20.6 / 11.9 | 6 / 3 | outlier knee max (z +3.9) |
| `solomon_1_11_11_t20-28_shift` | B | 3_solomon_1_11_11 19.9–27.9 s | 23.7 / 14.5 | 8 / 3 | outlier knee max (z +4.6) |
| `solomon_1_4_4_t264-269_shift` | B | 3_solomon_1_4_4 264.3–269.1 s | 11.4 / 7.1 | 15 / 5 | outlier knee max (z +4.9) |
| `solomon_1_4_4_t568-586` | A | 3_solomon_1_4_4 567.9–585.5 s | 11.4 / 6.0 | 13 / 3 | human steps |
| `solomon_1_5_5_t312-329` | A | 3_solomon_1_5_5 312.5–328.8 s | 7.3 / 8.1 | 5 / 2 | K1 feet move 8 cm |
| `solomon_1_5_5_t475-490` | A | 3_solomon_1_5_5 475.0–489.9 s | 9.6 / 8.4 | 4 / 1 | K1 feet move 8 cm |
| `solomon_1_5_5_t580-595` | A | 3_solomon_1_5_5 580.2–595.0 s | 10.4 / 7.4 | 18 / 5 | human steps |
| `solomon_1_5_5_t64-80` | A | 3_solomon_1_5_5 64.0–79.5 s | 12.5 / 7.0 | 7 / 1 | human steps |
| `solomon_1_6_6_t105-123` | A | 3_solomon_1_6_6 104.9–123.3 s | 16.7 / 10.8 | 8 / 3 | human steps; K1 feet move 11 cm |
| `solomon_1_6_6_t186-201` | A | 3_solomon_1_6_6 186.4–201.4 s | 9.6 / 10.5 | 12 / 3 | K1 feet move 10 cm |
| `solomon_1_6_6_t233-237_shift` | B | 3_solomon_1_6_6 233.1–237.1 s | 32.5 / 18.4 | 38 / 6 | human steps; K1 feet move 18 cm |
| `solomon_1_6_6_t412-420_shift` | B | 3_solomon_1_6_6 412.2–419.6 s | 16.8 / 10.5 | 29 / 6 | outlier knee max (z +5.1) |
| `solomon_1_6_6_t567-587_shift` | B | 3_solomon_1_6_6 567.3–587.2 s | 25.3 / 14.3 | 14 / 4 | human steps; outlier knee max (z +4.1) |
| `solomon_1_7_7_t136-140_shift` | B | 3_solomon_1_7_7 136.4–140.4 s | 30.8 / 19.0 | 14 / 4 | human steps; K1 feet move 19 cm |
| `solomon_1_7_7_t182-196_shift` | B | 3_solomon_1_7_7 182.2–195.9 s | 26.1 / 17.4 | 12 / 3 | human steps |
| `solomon_1_7_7_t452-456_shift` | B | 3_solomon_1_7_7 451.5–456.1 s | 11.6 / 7.6 | 15 / 4 | outlier knee max (z +4.5) |
| `solomon_1_7_7_t461-465_shift` | B | 3_solomon_1_7_7 461.1–465.1 s | 33.3 / 19.1 | 13 / 3 | human steps; K1 feet move 19 cm; outlier knee max (z +5.9) |
| `solomon_1_7_7_t465-477_shift` | B | 3_solomon_1_7_7 465.1–476.8 s | 24.2 / 18.0 | 13 / 3 | K1 feet move 18 cm; outlier knee max (z +3.7) |
| `solomon_1_7_7_t488-492_shift` | B | 3_solomon_1_7_7 488.3–492.3 s | 24.6 / 16.6 | 38 / 7 | outlier knee max (z +3.8) |
| `solomon_1_7_7_t515-523_shift` | B | 3_solomon_1_7_7 515.1–522.9 s | 21.8 / 12.7 | 22 / 7 | outlier knee max (z +3.8) |
| `solomon_1_7_7_t545-560_shift` | B | 3_solomon_1_7_7 545.1–559.9 s | 24.9 / 14.9 | 20 / 6 | outlier knee max (z +3.9) |
| `solomon_1_7_7_t76-86_shift` | B | 3_solomon_1_7_7 75.7–85.9 s | 29.6 / 18.5 | 14 / 3 | human steps; K1 feet move 19 cm; outlier knee max (z +4.8) |
| `solomon_1_8_8_t12-21_shift` | B | 3_solomon_1_8_8 11.5–21.3 s | 14.3 / 8.7 | 10 / 3 | outlier knee max (z +4.2) |
| `solomon_1_8_8_t131-139_shift` | B | 3_solomon_1_8_8 130.6–139.2 s | 24.9 / 14.5 | 16 / 4 | outlier knee max (z +3.6) |
| `solomon_1_8_8_t22-28_shift` | B | 3_solomon_1_8_8 22.1–28.3 s | 24.0 / 15.2 | 22 / 7 | outlier knee max (z +3.5) |
| `solomon_1_8_8_t276-283` | A | 3_solomon_1_8_8 275.5–282.7 s | 9.2 / 13.6 | 15 / 5 | K1 feet move 14 cm |
| `solomon_1_8_8_t280-284_shift` | B | 3_solomon_1_8_8 280.3–284.3 s | 21.2 / 13.5 | 16 / 5 | outlier knee max (z +3.5) |
| `solomon_1_8_8_t29-35` | A | 3_solomon_1_8_8 29.1–35.3 s | 9.5 / 12.6 | 11 / 3 | K1 feet move 13 cm |
| `solomon_1_8_8_t351-357_shift` | B | 3_solomon_1_8_8 350.7–356.6 s | 24.3 / 16.8 | 13 / 3 | outlier knee max (z +4.2) |
| `solomon_1_8_8_t368-372_shift` | B | 3_solomon_1_8_8 368.1–372.3 s | 24.7 / 15.2 | 13 / 3 | outlier knee max (z +4.7) |
| `solomon_1_8_8_t78-90_shift` | B | 3_solomon_1_8_8 78.1–89.8 s | 15.6 / 10.3 | 21 / 5 | outlier knee max (z +3.9) |
| `solomon_1_8_8_t90-94_shift` | B | 3_solomon_1_8_8 90.2–94.2 s | 22.7 / 14.8 | 9 / 2 | outlier knee max (z +4.6) |
| `solomon_1_9_9_t123-127_shift` | B | 3_solomon_1_9_9 123.2–127.5 s | 11.9 / 18.1 | 22 / 6 | K1 feet move 18 cm |
| `solomon_1_9_9_t175-181_shift` | B | 3_solomon_1_9_9 175.0–180.9 s | 15.6 / 12.6 | 5 / 2 | outlier knee max (z +3.8) |
| `solomon_1_9_9_t195-200_shift` | B | 3_solomon_1_9_9 195.1–199.5 s | 24.7 / 15.0 | 9 / 2 | outlier knee max (z +4.3) |
| `sophie_0_103_103_t14-24` | A | 7_sophie_0_103_103 13.6–23.7 s | 1.5 / 1.8 | 25 / 9 | shoulder at limit 7% |
| `sophie_0_11_11_t46-62` | A | 7_sophie_0_11_11 46.3–61.8 s | 10.5 / 6.0 | 17 / 5 | human steps |
| `sophie_0_19_19_t56-75` | A | 7_sophie_0_19_19 56.0–74.7 s | 10.0 / 5.5 | 15 / 4 | human steps |
| `sophie_0_22_22_t22-27_shift` | B | 7_sophie_0_22_22 22.1–26.5 s | 8.9 / 5.7 | 23 / 6 | outlier knee max (z +4.0) |
| `sophie_0_2_2_t10-15_shift` | B | 7_sophie_0_2_2 10.4–14.9 s | 13.0 / 8.4 | 22 / 7 | outlier knee max (z +5.6) |
| `sophie_0_2_2_t44-61` | A | 7_sophie_0_2_2 44.3–60.6 s | 9.2 / 3.4 | 15 / 5 | outlier knee max (z +4.4) |
| `sophie_0_2_2_t59-63_shift` | B | 7_sophie_0_2_2 58.6–62.8 s | 21.9 / 11.8 | 14 / 5 | outlier knee max (z +5.0) |
| `sophie_0_3_3_t13-17_shift` | B | 7_sophie_0_3_3 12.8–17.3 s | 13.0 / 8.7 | 20 / 6 | outlier knee max (z +4.6) |
| `sophie_0_3_3_t29-37_shift` | B | 7_sophie_0_3_3 28.6–37.2 s | 17.3 / 9.7 | 20 / 6 | outlier knee max (z +4.4) |
| `sophie_0_3_3_t54-62_shift` | B | 7_sophie_0_3_3 54.3–61.8 s | 21.1 / 11.9 | 15 / 5 | outlier knee max (z +5.6) |
| `sophie_0_44_44_t38-58` | A | 7_sophie_0_44_44 38.5–57.8 s | 10.1 / 5.6 | 13 / 4 | human steps |
| `sophie_0_47_47_t15-19_shift` | B | 7_sophie_0_47_47 14.6–18.9 s | 8.6 / 5.2 | 19 / 6 | outlier knee max (z +4.2) |
| `sophie_0_4_4_t12-17_shift` | B | 7_sophie_0_4_4 12.1–17.0 s | 17.5 / 10.1 | 15 / 4 | outlier knee max (z +3.7) |
| `sophie_0_5_5_t21-29_shift` | B | 7_sophie_0_5_5 21.2–28.7 s | 21.4 / 11.9 | 17 / 5 | outlier knee max (z +4.7) |
| `sophie_0_62_62_t52-58_shift` | B | 7_sophie_0_62_62 52.2–58.3 s | 13.8 / 7.1 | 18 / 5 | outlier knee max (z +3.7) |
| `sophie_0_64_64_t10-16_shift` | B | 7_sophie_0_64_64 10.3–15.8 s | 22.7 / 12.4 | 16 / 5 | outlier knee max (z +6.7) |
| `sophie_0_65_65_t2-11_shift` | B | 7_sophie_0_65_65 2.3–11.2 s | 12.1 / 7.4 | 27 / 7 | outlier knee max (z +4.2) |
| `sophie_0_68_68_t45-49_shift` | B | 7_sophie_0_68_68 44.7–48.8 s | 13.9 / 7.4 | 16 / 5 | outlier knee max (z +4.1) |
| `sophie_0_7_7_t53-58_shift` | B | 7_sophie_0_7_7 53.1–57.8 s | 21.0 / 12.1 | 12 / 3 | outlier knee max (z +5.1) |
| `sophie_1_10_10_t104-109` | A | 7_sophie_1_10_10 104.2–108.9 s | 1.3 / 1.3 | 22 / 7 | elbow bend at limit 25%; right arm behind body 7 cm (human's in front) |
| `sophie_1_10_10_t110-121_shift` | B | 7_sophie_1_10_10 109.5–120.7 s | 10.8 / 4.4 | 17 / 5 | knee 62 deg; elbow bend at limit 10%; outlier knee max (z +8.7); right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t12-20` | A | 7_sophie_1_10_10 11.7–19.8 s | 8.8 / 1.7 | 18 / 6 | outlier knee max (z +5.9) |
| `sophie_1_10_10_t131-135` | A | 7_sophie_1_10_10 130.6–135.5 s | 1.2 / 1.3 | 11 / 3 | right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t136-144` | A | 7_sophie_1_10_10 136.0–144.2 s | 5.2 / 0.9 | 24 / 7 | elbow bend at limit 17%; right arm behind body 7 cm (human's in front) |
| `sophie_1_10_10_t142-147_shift` | B | 7_sophie_1_10_10 142.2–146.8 s | 12.3 / 7.3 | 19 / 6 | outlier knee max (z +7.6); right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t145-150` | A | 7_sophie_1_10_10 144.8–150.5 s | 9.6 / 2.2 | 17 / 5 | outlier knee max (z +5.0); right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t148-157_shift` | B | 7_sophie_1_10_10 148.5–156.7 s | 10.1 / 3.3 | 21 / 7 | knee 62 deg; outlier knee max (z +8.5); right arm behind body 7 cm (human's in front) |
| `sophie_1_10_10_t162-170` | A | 7_sophie_1_10_10 161.7–170.5 s | 1.5 / 1.1 | 25 / 9 | elbow bend at limit 17% |
| `sophie_1_10_10_t18-22_shift` | B | 7_sophie_1_10_10 17.8–22.2 s | 12.9 / 7.6 | 28 / 11 | outlier knee max (z +5.8) |
| `sophie_1_10_10_t182-193` | A | 7_sophie_1_10_10 182.1–192.9 s | 1.5 / 1.3 | 5 / 2 | elbow bend at limit 9% |
| `sophie_1_10_10_t20-25` | A | 7_sophie_1_10_10 20.2–24.7 s | 1.6 / 0.6 | 23 / 9 | elbow bend at limit 22% |
| `sophie_1_10_10_t202-220` | A | 7_sophie_1_10_10 201.6–220.3 s | 4.7 / 0.7 | 20 / 8 | elbow bend at limit 23% |
| `sophie_1_10_10_t220-239` | A | 7_sophie_1_10_10 220.3–239.0 s | 1.5 / 1.0 | 15 / 6 | elbow bend at limit 15%; right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t23-27_shift` | B | 7_sophie_1_10_10 22.7–27.3 s | 14.7 / 9.3 | 19 / 8 | elbow bend at limit 16%; outlier knee max (z +4.0) |
| `sophie_1_10_10_t239-258` | A | 7_sophie_1_10_10 239.0–257.7 s | 10.9 / 5.7 | 17 / 6 | human steps; elbow bend at limit 35%; right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t25-33` | A | 7_sophie_1_10_10 25.3–33.4 s | 1.2 / 0.6 | 17 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t256-260_shift` | B | 7_sophie_1_10_10 255.7–260.3 s | 15.0 / 9.5 | 19 / 5 | elbow bend at limit 47%; outlier knee max (z +5.7) |
| `sophie_1_10_10_t258-276` | A | 7_sophie_1_10_10 258.3–276.2 s | 1.9 / 0.9 | 18 / 5 | elbow bend at limit 17%; right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t288-294` | A | 7_sophie_1_10_10 287.6–293.8 s | 1.8 / 1.4 | 18 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t295-301` | A | 7_sophie_1_10_10 294.8–300.9 s | 1.9 / 1.4 | 20 / 6 | elbow bend at limit 12% |
| `sophie_1_10_10_t302-307_shift` | B | 7_sophie_1_10_10 301.5–307.2 s | 12.8 / 8.2 | 18 / 8 | outlier knee max (z +4.6) |
| `sophie_1_10_10_t305-316` | A | 7_sophie_1_10_10 305.2–315.5 s | 1.9 / 0.8 | 20 / 6 | right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t325-329` | A | 7_sophie_1_10_10 324.6–328.9 s | 2.2 / 2.6 | 18 / 5 | elbow bend at limit 12% |
| `sophie_1_10_10_t330-338` | A | 7_sophie_1_10_10 329.7–337.9 s | 1.1 / 0.9 | 17 / 6 | elbow bend at limit 27%; right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t339-344` | A | 7_sophie_1_10_10 338.6–344.4 s | 8.1 / 1.6 | 13 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t341-345_shift` | B | 7_sophie_1_10_10 340.9–344.9 s | 10.9 / 2.0 | 11 / 4 | outlier knee max (z +5.3); right arm behind body 7 cm (human's in front) |
| `sophie_1_10_10_t351-355_shift` | B | 7_sophie_1_10_10 350.8–355.2 s | 10.2 / 4.8 | 13 / 6 | outlier knee max (z +5.9) |
| `sophie_1_10_10_t353-364` | A | 7_sophie_1_10_10 353.2–363.7 s | 6.4 / 4.8 | 22 / 8 | elbow bend at limit 6%; outlier knee max (z +4.7); right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t364-374` | A | 7_sophie_1_10_10 363.7–374.2 s | 2.6 / 0.9 | 22 / 7 | elbow bend at limit 31%; right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t372-379_shift` | B | 7_sophie_1_10_10 372.2–378.6 s | 14.0 / 7.4 | 26 / 7 | elbow bend at limit 10%; outlier knee max (z +5.2); right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t377-383` | A | 7_sophie_1_10_10 376.6–382.7 s | 2.1 / 0.9 | 26 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t38-42_shift` | B | 7_sophie_1_10_10 38.3–42.3 s | 10.0 / 5.0 | 11 / 4 | elbow bend at limit 45% |
| `sophie_1_10_10_t381-389_shift` | B | 7_sophie_1_10_10 380.7–388.8 s | 12.2 / 7.9 | 17 / 5 | elbow bend at limit 7%; right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t387-397` | A | 7_sophie_1_10_10 386.8–396.7 s | 1.5 / 0.7 | 22 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t39-50` | A | 7_sophie_1_10_10 39.5–50.5 s | 1.3 / 0.7 | 14 / 4 | elbow bend at limit 30% |
| `sophie_1_10_10_t395-399_shift` | B | 7_sophie_1_10_10 394.7–399.1 s | 12.5 / 7.5 | 13 / 5 | outlier knee max (z +5.3) |
| `sophie_1_10_10_t417-437` | A | 7_sophie_1_10_10 416.7–436.7 s | 7.1 / 3.3 | 18 / 7 | outlier knee max (z +4.6) |
| `sophie_1_10_10_t435-439_shift` | B | 7_sophie_1_10_10 434.7–439.3 s | 9.7 / 6.6 | 15 / 5 | elbow bend at limit 15%; outlier knee max (z +5.9); right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t437-450` | A | 7_sophie_1_10_10 437.3–449.7 s | 1.2 / 0.5 | 16 / 6 | elbow bend at limit 43%; right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t460-465_shift` | B | 7_sophie_1_10_10 460.0–464.5 s | 11.6 / 8.3 | 10 / 5 | elbow bend at limit 9%; outlier knee max (z +3.8) |
| `sophie_1_10_10_t488-492_shift` | B | 7_sophie_1_10_10 487.8–492.3 s | 10.5 / 6.0 | 19 / 7 | shoulder at limit 8%; outlier knee max (z +4.1) |
| `sophie_1_10_10_t490-495` | A | 7_sophie_1_10_10 490.3–494.6 s | 2.5 / 1.0 | 18 / 7 | shoulder at limit 23%; elbow bend at limit 11% |
| `sophie_1_10_10_t493-501_shift` | B | 7_sophie_1_10_10 492.6–500.6 s | 35.7 / 19.3 | 21 / 7 | human steps; K1 feet move 19 cm; outlier knee max (z +6.2) |
| `sophie_1_10_10_t499-506` | A | 7_sophie_1_10_10 498.6–505.7 s | 1.9 / 1.5 | 29 / 10 | elbow bend at limit 6%; right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t50-61` | A | 7_sophie_1_10_10 50.5–61.4 s | 1.9 / 0.9 | 19 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t506-512` | A | 7_sophie_1_10_10 506.3–511.6 s | 2.5 / 1.1 | 28 / 11 | elbow bend at limit 44% |
| `sophie_1_10_10_t512-517` | A | 7_sophie_1_10_10 512.4–516.5 s | 1.5 / 1.1 | 12 / 4 | elbow bend at limit 6% |
| `sophie_1_10_10_t517-521` | A | 7_sophie_1_10_10 517.2–521.4 s | 1.5 / 1.1 | 11 / 4 | elbow bend at limit 23% |
| `sophie_1_10_10_t535-541_shift` | B | 7_sophie_1_10_10 535.4–541.0 s | 10.9 / 5.2 | 17 / 5 | outlier knee max (z +6.0); right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t539-544` | A | 7_sophie_1_10_10 539.0–544.4 s | 4.4 / 1.2 | 12 / 5 | right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t582-600` | A | 7_sophie_1_10_10 581.8–600.4 s | 7.3 / 3.7 | 21 / 5 | elbow bend at limit 17% |
| `sophie_1_10_10_t59-65_shift` | B | 7_sophie_1_10_10 59.4–65.3 s | 18.7 / 9.6 | 20 / 7 | elbow bend at limit 8%; outlier knee max (z +5.4); right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t598-603_shift` | B | 7_sophie_1_10_10 598.4–602.9 s | 10.2 / 6.0 | 26 / 6 | outlier knee max (z +6.8) |
| `sophie_1_10_10_t601-615` | A | 7_sophie_1_10_10 600.9–614.6 s | 8.7 / 4.8 | 21 / 7 | elbow bend at limit 11% |
| `sophie_1_10_10_t611-615_shift` | B | 7_sophie_1_10_10 611.4–615.4 s | 14.7 / 6.8 | 18 / 8 | elbow bend at limit 16% |
| `sophie_1_10_10_t616-625` | A | 7_sophie_1_10_10 616.1–624.8 s | 4.0 / 2.4 | 30 / 9 | elbow bend at limit 5%; right arm behind body 6 cm (human's in front) |
| `sophie_1_10_10_t7-11` | A | 7_sophie_1_10_10 6.7–11.0 s | 3.6 / 1.9 | 33 / 12 | head at limit 10%; elbow bend at limit 28% |
| `sophie_1_10_10_t72-76_shift` | B | 7_sophie_1_10_10 71.8–76.5 s | 15.7 / 11.1 | 17 / 6 | elbow bend at limit 5%; outlier knee max (z +4.0) |
| `sophie_1_10_10_t74-87` | A | 7_sophie_1_10_10 74.5–87.4 s | 3.3 / 3.1 | 19 / 7 | elbow bend at limit 9% |
| `sophie_1_10_10_t85-90_shift` | B | 7_sophie_1_10_10 85.4–89.9 s | 13.6 / 8.3 | 19 / 5 | outlier knee max (z +6.2); right arm behind body 5 cm (human's in front) |
| `sophie_1_10_10_t95-104` | A | 7_sophie_1_10_10 95.1–103.7 s | 6.6 / 1.6 | 18 / 7 | elbow bend at limit 14%; right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t0-5_shift` | B | 7_sophie_1_11_11 0.0–5.0 s | 11.1 / 5.7 | 28 / 8 | elbow bend at limit 10% |
| `sophie_1_11_11_t112-119` | A | 7_sophie_1_11_11 111.8–118.6 s | 1.8 / 1.3 | 19 / 5 | head at limit 14%; elbow bend at limit 5% |
| `sophie_1_11_11_t119-124_shift` | B | 7_sophie_1_11_11 119.2–124.1 s | 20.2 / 11.9 | 21 / 7 | elbow bend at limit 12%; outlier knee max (z +5.3); right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t14-24` | A | 7_sophie_1_11_11 13.5–24.1 s | 4.9 / 0.8 | 17 / 5 | elbow bend at limit 36%; right arm behind body 5 cm (human's in front) |
| `sophie_1_11_11_t144-156` | A | 7_sophie_1_11_11 143.5–156.0 s | 2.0 / 1.5 | 19 / 6 | elbow bend at limit 17% |
| `sophie_1_11_11_t156-160_shift` | B | 7_sophie_1_11_11 156.5–160.5 s | 11.7 / 5.7 | 16 / 6 | right arm behind body 5 cm (human's in front) |
| `sophie_1_11_11_t165-175` | A | 7_sophie_1_11_11 164.7–175.5 s | 2.7 / 0.8 | 27 / 9 | elbow bend at limit 5%; right arm behind body 5 cm (human's in front) |
| `sophie_1_11_11_t176-182` | A | 7_sophie_1_11_11 176.1–181.6 s | 1.2 / 0.6 | 23 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t182-186_shift` | B | 7_sophie_1_11_11 182.1–186.2 s | 16.9 / 9.2 | 14 / 5 | right arm behind body 5 cm (human's in front) |
| `sophie_1_11_11_t184-195` | A | 7_sophie_1_11_11 184.2–194.5 s | 6.8 / 0.7 | 28 / 10 | elbow bend at limit 10%; right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t193-197_shift` | B | 7_sophie_1_11_11 192.5–197.0 s | 11.0 / 5.8 | 26 / 11 | outlier knee max (z +5.5); right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t195-200` | A | 7_sophie_1_11_11 195.0–200.0 s | 3.0 / 0.7 | 33 / 11 | elbow bend at limit 21% |
| `sophie_1_11_11_t201-208` | A | 7_sophie_1_11_11 200.7–207.5 s | 2.3 / 1.0 | 27 / 8 | elbow bend at limit 10% |
| `sophie_1_11_11_t212-218` | A | 7_sophie_1_11_11 212.3–218.0 s | 1.4 / 0.5 | 31 / 10 | elbow bend at limit 8% |
| `sophie_1_11_11_t215-219_shift` | B | 7_sophie_1_11_11 214.8–218.8 s | 24.8 / 14.0 | 23 / 8 | elbow bend at limit 7%; outlier knee max (z +6.6) |
| `sophie_1_11_11_t22-27_shift` | B | 7_sophie_1_11_11 22.1–26.5 s | 12.9 / 7.0 | 17 / 7 | elbow bend at limit 39%; right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t225-236` | A | 7_sophie_1_11_11 224.7–235.8 s | 1.0 / 1.0 | 20 / 7 | elbow bend at limit 7%; right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t248-254` | A | 7_sophie_1_11_11 247.5–253.5 s | 9.7 / 1.7 | 19 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t25-30` | A | 7_sophie_1_11_11 24.5–30.0 s | 1.7 / 0.6 | 16 / 5 | elbow bend at limit 20% |
| `sophie_1_11_11_t259-263_shift` | B | 7_sophie_1_11_11 259.2–263.2 s | 15.4 / 5.5 | 12 / 4 | head at limit 35% |
| `sophie_1_11_11_t260-277` | A | 7_sophie_1_11_11 260.5–277.3 s | 5.4 / 3.3 | 14 / 5 | head at limit 6%; elbow bend at limit 8% |
| `sophie_1_11_11_t292-298_shift` | B | 7_sophie_1_11_11 292.1–298.3 s | 24.4 / 13.4 | 21 / 9 | elbow bend at limit 9%; outlier knee max (z +4.2) |
| `sophie_1_11_11_t3-14` | A | 7_sophie_1_11_11 3.0–13.5 s | 2.9 / 0.4 | 13 / 5 | elbow bend at limit 14% |
| `sophie_1_11_11_t310-316_shift` | B | 7_sophie_1_11_11 309.7–316.2 s | 15.0 / 7.3 | 12 / 4 | head at limit 14% |
| `sophie_1_11_11_t314-331` | A | 7_sophie_1_11_11 314.2–331.2 s | 4.2 / 1.1 | 20 / 5 | elbow bend at limit 28%; right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t329-337_shift` | B | 7_sophie_1_11_11 329.2–337.0 s | 12.9 / 6.7 | 15 / 6 | elbow bend at limit 55%; outlier knee max (z +5.7) |
| `sophie_1_11_11_t335-344` | A | 7_sophie_1_11_11 335.0–343.9 s | 9.9 / 2.3 | 21 / 7 | elbow bend at limit 22%; outlier knee max (z +5.2) |
| `sophie_1_11_11_t342-349_shift` | B | 7_sophie_1_11_11 341.9–348.7 s | 13.7 / 7.1 | 21 / 5 | knee 62 deg; outlier knee max (z +8.7) |
| `sophie_1_11_11_t349-354_shift` | B | 7_sophie_1_11_11 349.2–353.8 s | 16.5 / 11.8 | 12 / 3 | head at limit 41%; outlier knee max (z +4.1) |
| `sophie_1_11_11_t352-359` | A | 7_sophie_1_11_11 351.8–359.3 s | 4.1 / 0.9 | 8 / 2 | head at limit 70% |
| `sophie_1_11_11_t356-360_shift` | B | 7_sophie_1_11_11 356.2–360.2 s | 21.2 / 10.9 | 7 / 2 | head at limit 45%; outlier knee max (z +6.0) |
| `sophie_1_11_11_t360-371` | A | 7_sophie_1_11_11 359.8–371.1 s | 9.9 / 2.6 | 13 / 3 | elbow bend at limit 42%; outlier knee max (z +4.9) |
| `sophie_1_11_11_t369-375_shift` | B | 7_sophie_1_11_11 369.1–374.9 s | 11.2 / 3.1 | 15 / 4 | head at limit 8%; elbow bend at limit 16%; outlier knee max (z +8.0) |
| `sophie_1_11_11_t378-383_shift` | B | 7_sophie_1_11_11 378.3–382.9 s | 11.6 / 8.5 | 31 / 10 | elbow bend at limit 5%; outlier knee max (z +4.5); right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t381-395` | A | 7_sophie_1_11_11 380.9–394.8 s | 1.4 / 0.6 | 25 / 7 | elbow bend at limit 12%; right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t395-409` | A | 7_sophie_1_11_11 394.8–408.6 s | 2.1 / 0.8 | 15 / 6 | elbow bend at limit 21%; right arm behind body 5 cm (human's in front) |
| `sophie_1_11_11_t414-419_shift` | B | 7_sophie_1_11_11 414.0–418.7 s | 21.2 / 13.8 | 21 / 6 | outlier knee max (z +5.0) |
| `sophie_1_11_11_t426-431_shift` | B | 7_sophie_1_11_11 426.1–430.6 s | 28.7 / 17.6 | 25 / 8 | human steps; outlier knee max (z +7.0) |
| `sophie_1_11_11_t429-434` | A | 7_sophie_1_11_11 428.6–434.4 s | 8.3 / 1.2 | 9 / 4 | head at limit 13% |
| `sophie_1_11_11_t43-58` | A | 7_sophie_1_11_11 42.7–57.9 s | 1.6 / 1.2 | 12 / 4 | elbow bend at limit 11% |
| `sophie_1_11_11_t432-437_shift` | B | 7_sophie_1_11_11 432.4–436.8 s | 10.6 / 6.0 | 13 / 6 | head at limit 22% |
| `sophie_1_11_11_t440-445_shift` | B | 7_sophie_1_11_11 440.4–444.9 s | 9.3 / 4.8 | 29 / 8 | outlier knee max (z +4.2); right arm behind body 5 cm (human's in front) |
| `sophie_1_11_11_t446-451_shift` | B | 7_sophie_1_11_11 446.2–450.7 s | 10.2 / 7.2 | 25 / 9 | elbow bend at limit 7% |
| `sophie_1_11_11_t449-466` | A | 7_sophie_1_11_11 448.7–465.8 s | 1.7 / 1.1 | 21 / 7 | elbow bend at limit 36% |
| `sophie_1_11_11_t464-470_shift` | B | 7_sophie_1_11_11 463.8–470.1 s | 18.0 / 9.7 | 40 / 10 | outlier knee max (z +3.8) |
| `sophie_1_11_11_t487-505` | A | 7_sophie_1_11_11 486.6–505.0 s | 6.9 / 1.9 | 17 / 5 | elbow bend at limit 29%; outlier knee max (z +5.3) |
| `sophie_1_11_11_t505-524` | A | 7_sophie_1_11_11 505.0–523.5 s | 0.7 / 0.9 | 17 / 6 | elbow bend at limit 6% |
| `sophie_1_11_11_t58-69` | A | 7_sophie_1_11_11 58.5–69.0 s | 5.5 / 1.6 | 13 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t75-83` | A | 7_sophie_1_11_11 74.8–82.9 s | 8.6 / 1.7 | 16 / 6 | head at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t81-86_shift` | B | 7_sophie_1_11_11 80.9–85.8 s | 16.8 / 8.7 | 24 / 8 | knee 61 deg; elbow bend at limit 14%; outlier knee max (z +8.5); right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t84-91` | A | 7_sophie_1_11_11 83.8–91.1 s | 3.1 / 0.5 | 24 / 8 | elbow bend at limit 10%; right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t89-94_shift` | B | 7_sophie_1_11_11 89.1–93.8 s | 19.9 / 12.0 | 15 / 5 | elbow bend at limit 18%; outlier knee max (z +7.5); right arm behind body 6 cm (human's in front) |
| `sophie_1_11_11_t98-108` | A | 7_sophie_1_11_11 97.5–107.6 s | 1.8 / 0.9 | 31 / 10 | right arm behind body 5 cm (human's in front) |
| `sophie_1_12_12_t102-106_shift` | B | 7_sophie_1_12_12 102.2–106.2 s | 22.5 / 12.6 | 17 / 4 | elbow bend at limit 35%; outlier knee max (z +5.4) |
| `sophie_1_12_12_t107-126` | A | 7_sophie_1_12_12 106.9–125.6 s | 2.4 / 2.2 | 21 / 6 | head at limit 22%; elbow bend at limit 5% |
| `sophie_1_12_12_t145-155` | A | 7_sophie_1_12_12 144.8–155.5 s | 9.5 / 4.5 | 18 / 5 | head at limit 25% |
| `sophie_1_12_12_t155-166` | A | 7_sophie_1_12_12 155.5–166.2 s | 3.8 / 0.9 | 14 / 4 | elbow bend at limit 14% |
| `sophie_1_12_12_t164-169_shift` | B | 7_sophie_1_12_12 164.2–168.7 s | 14.3 / 8.2 | 19 / 5 | head at limit 14% |
| `sophie_1_12_12_t171-190` | A | 7_sophie_1_12_12 171.4–190.2 s | 2.0 / 1.0 | 28 / 8 | elbow bend at limit 14% |
| `sophie_1_12_12_t190-209` | A | 7_sophie_1_12_12 190.2–208.9 s | 2.9 / 1.0 | 22 / 8 | elbow bend at limit 8%; right arm behind body 5 cm (human's in front) |
| `sophie_1_12_12_t206-210_shift` | B | 7_sophie_1_12_12 205.7–209.7 s | 15.5 / 8.7 | 32 / 11 | right arm behind body 6 cm (human's in front) |
| `sophie_1_12_12_t210-221` | A | 7_sophie_1_12_12 210.5–221.1 s | 1.5 / 2.4 | 8 / 2 | head at limit 8% |
| `sophie_1_12_12_t22-32` | A | 7_sophie_1_12_12 22.4–31.8 s | 9.8 / 1.7 | 27 / 6 | outlier knee max (z +6.0) |
| `sophie_1_12_12_t232-252` | A | 7_sophie_1_12_12 232.3–251.8 s | 8.6 / 4.9 | 22 / 7 | elbow bend at limit 11% |
| `sophie_1_12_12_t252-271` | A | 7_sophie_1_12_12 251.8–271.2 s | 2.4 / 1.6 | 13 / 5 | head at limit 6%; elbow bend at limit 14% |
| `sophie_1_12_12_t271-291` | A | 7_sophie_1_12_12 271.2–290.7 s | 4.0 / 1.1 | 17 / 6 | elbow bend at limit 28% |
| `sophie_1_12_12_t306-312_shift` | B | 7_sophie_1_12_12 306.3–311.8 s | 32.3 / 17.3 | 28 / 9 | human steps; elbow bend at limit 19%; outlier knee max (z +5.4) |
| `sophie_1_12_12_t310-330` | A | 7_sophie_1_12_12 309.8–329.7 s | 2.3 / 1.7 | 16 / 6 | elbow bend at limit 20% |
| `sophie_1_12_12_t328-332_shift` | B | 7_sophie_1_12_12 327.7–332.2 s | 23.0 / 15.0 | 24 / 8 | elbow bend at limit 13%; outlier knee max (z +5.4); right arm behind body 5 cm (human's in front) |
| `sophie_1_12_12_t330-336` | A | 7_sophie_1_12_12 330.2–336.1 s | 3.0 / 3.2 | 25 / 7 | elbow bend at limit 14%; hand presses into leg 9 mm for 0.1 s (at 4.2 s) |
| `sophie_1_12_12_t34-40` | A | 7_sophie_1_12_12 34.3–40.1 s | 1.9 / 0.6 | 37 / 10 | elbow bend at limit 23% |
| `sophie_1_12_12_t353-368` | A | 7_sophie_1_12_12 352.6–368.5 s | 2.3 / 1.5 | 5 / 1 | head at limit 56% |
| `sophie_1_12_12_t368-384` | A | 7_sophie_1_12_12 368.5–384.3 s | 1.5 / 1.1 | 33 / 8 | elbow bend at limit 19% |
| `sophie_1_12_12_t384-400` | A | 7_sophie_1_12_12 384.3–400.2 s | 1.2 / 1.0 | 25 / 7 | elbow bend at limit 12% |
| `sophie_1_12_12_t41-55` | A | 7_sophie_1_12_12 40.7–54.9 s | 1.4 / 1.1 | 15 / 6 | elbow bend at limit 23% |
| `sophie_1_12_12_t415-429` | A | 7_sophie_1_12_12 415.4–428.6 s | 3.1 / 0.9 | 13 / 4 | elbow bend at limit 8% |
| `sophie_1_12_12_t427-434_shift` | B | 7_sophie_1_12_12 426.6–434.3 s | 13.4 / 8.6 | 18 / 5 | elbow bend at limit 6% |
| `sophie_1_12_12_t446-460` | A | 7_sophie_1_12_12 446.1–459.9 s | 1.1 / 1.0 | 22 / 7 | elbow bend at limit 14% |
| `sophie_1_12_12_t457-461_shift` | B | 7_sophie_1_12_12 456.7–460.7 s | 18.8 / 10.9 | 24 / 8 | elbow bend at limit 8%; outlier knee max (z +4.9) |
| `sophie_1_12_12_t461-475` | A | 7_sophie_1_12_12 461.4–475.2 s | 2.2 / 1.2 | 16 / 4 | head at limit 25%; elbow bend at limit 7% |
| `sophie_1_12_12_t490-509` | A | 7_sophie_1_12_12 489.5–508.6 s | 7.7 / 3.6 | 22 / 8 | elbow bend at limit 15%; right arm behind body 5 cm (human's in front) |
| `sophie_1_12_12_t5-10_shift` | B | 7_sophie_1_12_12 5.4–10.0 s | 18.9 / 10.9 | 12 / 4 | head at limit 9%; outlier knee max (z +7.1) |
| `sophie_1_12_12_t509-528` | A | 7_sophie_1_12_12 508.6–527.6 s | 4.0 / 2.2 | 22 / 7 | elbow bend at limit 24% |
| `sophie_1_12_12_t526-530_shift` | B | 7_sophie_1_12_12 525.6–530.0 s | 8.8 / 5.8 | 30 / 8 | outlier knee max (z +6.5) |
| `sophie_1_12_12_t548-562` | A | 7_sophie_1_12_12 548.5–561.9 s | 1.4 / 1.7 | 16 / 6 | elbow bend at limit 20% |
| `sophie_1_12_12_t55-62` | A | 7_sophie_1_12_12 55.4–61.5 s | 9.2 / 1.1 | 20 / 6 | elbow bend at limit 32% |
| `sophie_1_12_12_t566-573` | A | 7_sophie_1_12_12 565.6–573.1 s | 5.6 / 1.1 | 33 / 10 | right arm behind body 5 cm (human's in front) |
| `sophie_1_12_12_t571-576_shift` | B | 7_sophie_1_12_12 571.1–575.7 s | 13.9 / 6.6 | 22 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_12_12_t574-585` | A | 7_sophie_1_12_12 573.7–585.4 s | 6.5 / 2.1 | 23 / 7 | elbow bend at limit 13%; right arm behind body 5 cm (human's in front) |
| `sophie_1_12_12_t583-588_shift` | B | 7_sophie_1_12_12 583.4–588.2 s | 22.6 / 12.4 | 22 / 6 | head at limit 28%; outlier knee max (z +4.7) |
| `sophie_1_12_12_t586-592` | A | 7_sophie_1_12_12 586.2–591.7 s | 9.8 / 2.0 | 21 / 6 | head at limit 10% |
| `sophie_1_12_12_t592-597` | A | 7_sophie_1_12_12 591.7–597.1 s | 10.0 / 3.2 | 28 / 10 | outlier knee max (z +5.6) |
| `sophie_1_12_12_t595-600_shift` | B | 7_sophie_1_12_12 595.1–600.3 s | 3.1 / 0.9 | 42 / 11 | right arm behind body 5 cm (human's in front) |
| `sophie_1_12_12_t60-64_shift` | B | 7_sophie_1_12_12 59.5–64.0 s | 11.7 / 5.4 | 20 / 7 | outlier knee max (z +6.3); right arm behind body 5 cm (human's in front) |
| `sophie_1_12_12_t601-612` | A | 7_sophie_1_12_12 601.1–611.8 s | 2.3 / 1.4 | 15 / 4 | head at limit 51% |
| `sophie_1_12_12_t612-619_shift` | B | 7_sophie_1_12_12 612.5–618.7 s | 21.8 / 11.9 | 21 / 6 | head at limit 81%; outlier knee max (z +6.0) |
| `sophie_1_12_12_t62-81` | A | 7_sophie_1_12_12 62.0–81.3 s | 6.1 / 3.1 | 17 / 7 | elbow bend at limit 11%; right arm behind body 5 cm (human's in front) |
| `sophie_1_12_12_t79-84_shift` | B | 7_sophie_1_12_12 79.3–83.7 s | 9.6 / 5.0 | 15 / 6 | head at limit 9% |
| `sophie_1_12_12_t8-14` | A | 7_sophie_1_12_12 8.0–13.6 s | 1.6 / 1.2 | 15 / 4 | head at limit 7% |
| `sophie_1_12_12_t82-93` | A | 7_sophie_1_12_12 81.7–93.4 s | 1.5 / 1.1 | 29 / 9 | head at limit 13%; elbow bend at limit 6% |
| `sophie_1_12_12_t93-105` | A | 7_sophie_1_12_12 93.4–105.1 s | 1.5 / 0.9 | 19 / 7 | elbow bend at limit 26% |
| `sophie_1_1_1_t100-105_shift` | B | 7_sophie_1_1_1 100.2–104.6 s | 16.0 / 9.2 | 19 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t106-117` | A | 7_sophie_1_1_1 105.8–117.4 s | 1.9 / 0.9 | 18 / 7 | elbow bend at limit 5% |
| `sophie_1_1_1_t139-144` | A | 7_sophie_1_1_1 139.3–144.4 s | 5.6 / 1.7 | 24 / 8 | right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t142-147_shift` | B | 7_sophie_1_1_1 142.4–147.1 s | 17.4 / 9.5 | 24 / 8 | outlier knee max (z +6.0); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t145-151` | A | 7_sophie_1_1_1 145.1–151.2 s | 8.4 / 5.0 | 27 / 9 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t152-165` | A | 7_sophie_1_1_1 151.9–164.6 s | 4.0 / 1.4 | 19 / 8 | right arm behind body 7 cm (human's in front) |
| `sophie_1_1_1_t16-21` | A | 7_sophie_1_1_1 15.7–20.7 s | 1.8 / 1.1 | 15 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t163-167_shift` | B | 7_sophie_1_1_1 162.6–167.4 s | 20.9 / 11.2 | 21 / 7 | outlier knee max (z +3.6); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t168-173_shift` | B | 7_sophie_1_1_1 168.0–173.1 s | 11.1 / 7.8 | 18 / 5 | head at limit 8% |
| `sophie_1_1_1_t174-178` | A | 7_sophie_1_1_1 173.8–178.3 s | 5.4 / 1.5 | 19 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t176-191_shift` | B | 7_sophie_1_1_1 176.3–190.9 s | 29.6 / 14.7 | 18 / 5 | human steps; outlier knee max (z +6.6); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t191-199_shift` | B | 7_sophie_1_1_1 191.3–199.3 s | 17.3 / 8.9 | 18 / 6 | outlier knee max (z +4.6) |
| `sophie_1_1_1_t204-209_shift` | B | 7_sophie_1_1_1 203.6–209.1 s | 28.3 / 12.7 | 22 / 6 | human steps; outlier knee max (z +4.2); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t218-225` | A | 7_sophie_1_1_1 217.6–224.6 s | 2.0 / 0.7 | 24 / 9 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t22-32_shift` | B | 7_sophie_1_1_1 22.5–31.7 s | 21.5 / 12.4 | 12 / 5 | outlier knee max (z +3.7); right arm behind body 7 cm (human's in front) |
| `sophie_1_1_1_t223-227_shift` | B | 7_sophie_1_1_1 222.6–226.8 s | 18.1 / 10.5 | 28 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t229-234` | A | 7_sophie_1_1_1 228.6–233.6 s | 2.0 / 0.8 | 21 / 7 | elbow bend at limit 17%; right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t234-239_shift` | B | 7_sophie_1_1_1 234.2–239.2 s | 21.6 / 13.1 | 16 / 7 | outlier knee max (z +6.1); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t237-244` | A | 7_sophie_1_1_1 237.2–243.9 s | 1.7 / 1.3 | 19 / 9 | right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t241-245_shift` | B | 7_sophie_1_1_1 240.6–244.6 s | 25.1 / 13.8 | 21 / 8 | human steps; outlier knee max (z +8.0); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t248-253_shift` | B | 7_sophie_1_1_1 247.8–252.7 s | 24.8 / 13.3 | 18 / 7 | elbow bend at limit 12%; outlier knee max (z +6.9) |
| `sophie_1_1_1_t257-262` | A | 7_sophie_1_1_1 256.8–261.9 s | 5.3 / 1.6 | 18 / 6 | elbow bend at limit 16%; right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t26-31` | A | 7_sophie_1_1_1 25.9–30.6 s | 5.3 / 1.8 | 14 / 5 | right arm behind body 7 cm (human's in front) |
| `sophie_1_1_1_t260-265_shift` | B | 7_sophie_1_1_1 259.9–265.4 s | 23.9 / 11.5 | 22 / 7 | outlier knee max (z +4.1); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t263-268` | A | 7_sophie_1_1_1 263.4–267.9 s | 9.8 / 2.5 | 19 / 7 | outlier knee max (z +4.6); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t266-278_shift` | B | 7_sophie_1_1_1 265.9–277.6 s | 13.8 / 6.4 | 19 / 6 | outlier knee max (z +5.5); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t276-281` | A | 7_sophie_1_1_1 275.6–281.1 s | 9.9 / 5.5 | 17 / 6 | head at limit 6%; right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t281-287` | A | 7_sophie_1_1_1 281.1–287.2 s | 8.9 / 3.3 | 18 / 5 | head at limit 6%; elbow bend at limit 9% |
| `sophie_1_1_1_t285-290_shift` | B | 7_sophie_1_1_1 285.2–289.6 s | 14.9 / 5.4 | 16 / 5 | head at limit 8% |
| `sophie_1_1_1_t295-302_shift` | B | 7_sophie_1_1_1 295.2–302.2 s | 12.9 / 7.2 | 18 / 6 | outlier knee max (z +5.1); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t300-316` | A | 7_sophie_1_1_1 300.2–316.4 s | 10.0 / 5.9 | 15 / 6 | elbow bend at limit 5%; right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t32-38_shift` | B | 7_sophie_1_1_1 32.4–37.6 s | 18.5 / 12.1 | 20 / 7 | outlier knee max (z +4.5) |
| `sophie_1_1_1_t320-324_shift` | B | 7_sophie_1_1_1 319.9–324.3 s | 9.6 / 3.4 | 15 / 6 | outlier knee max (z +3.9); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t322-332` | A | 7_sophie_1_1_1 322.3–332.5 s | 5.7 / 0.9 | 18 / 7 | elbow bend at limit 5%; right arm behind body 7 cm (human's in front) |
| `sophie_1_1_1_t330-336_shift` | B | 7_sophie_1_1_1 330.5–335.8 s | 15.9 / 5.8 | 17 / 7 | outlier knee max (z +6.8); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t337-342_shift` | B | 7_sophie_1_1_1 337.0–341.6 s | 16.2 / 11.3 | 13 / 4 | outlier knee max (z +5.1); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t348-352` | A | 7_sophie_1_1_1 348.0–352.4 s | 1.0 / 1.1 | 16 / 5 | elbow bend at limit 27% |
| `sophie_1_1_1_t350-355_shift` | B | 7_sophie_1_1_1 350.4–354.9 s | 20.9 / 8.2 | 17 / 6 | elbow bend at limit 17% |
| `sophie_1_1_1_t353-367` | A | 7_sophie_1_1_1 352.9–366.9 s | 2.6 / 1.7 | 18 / 6 | right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t365-369_shift` | B | 7_sophie_1_1_1 364.9–369.4 s | 16.1 / 8.6 | 18 / 6 | outlier knee max (z +4.1); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t367-374` | A | 7_sophie_1_1_1 367.4–374.2 s | 5.2 / 2.9 | 19 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t372-377_shift` | B | 7_sophie_1_1_1 372.2–376.8 s | 12.8 / 8.8 | 15 / 6 | outlier knee max (z +5.6) |
| `sophie_1_1_1_t377-382_shift` | B | 7_sophie_1_1_1 377.2–381.8 s | 19.4 / 11.2 | 13 / 6 | outlier knee max (z +6.2) |
| `sophie_1_1_1_t380-386` | A | 7_sophie_1_1_1 379.8–386.0 s | 7.3 / 4.2 | 15 / 6 | right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t384-389_shift` | B | 7_sophie_1_1_1 384.0–388.6 s | 17.4 / 12.3 | 24 / 9 | outlier knee max (z +6.0) |
| `sophie_1_1_1_t4-18_shift` | B | 7_sophie_1_1_1 4.3–17.5 s | 26.0 / 13.8 | 13 / 5 | human steps; head at limit 6%; elbow bend at limit 5%; outlier knee max (z +8.0) |
| `sophie_1_1_1_t40-47_shift` | B | 7_sophie_1_1_1 39.8–46.7 s | 10.4 / 6.6 | 19 / 7 | head at limit 25% |
| `sophie_1_1_1_t414-419_shift` | B | 7_sophie_1_1_1 414.1–419.2 s | 23.2 / 11.5 | 17 / 8 | elbow bend at limit 5%; outlier knee max (z +6.6); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t417-424` | A | 7_sophie_1_1_1 417.2–423.5 s | 3.8 / 1.1 | 20 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t424-430` | A | 7_sophie_1_1_1 424.3–429.5 s | 1.4 / 1.0 | 21 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t437-442` | A | 7_sophie_1_1_1 436.9–441.5 s | 6.6 / 1.8 | 24 / 8 | elbow bend at limit 21%; right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t440-445_shift` | B | 7_sophie_1_1_1 439.5–445.0 s | 33.6 / 18.9 | 28 / 9 | human steps; K1 feet move 19 cm; elbow bend at limit 15%; outlier knee max (z +6.8) |
| `sophie_1_1_1_t451-468` | A | 7_sophie_1_1_1 451.0–468.0 s | 7.2 / 2.2 | 23 / 8 | outlier knee max (z +3.5) |
| `sophie_1_1_1_t466-472_shift` | B | 7_sophie_1_1_1 466.0–471.8 s | 21.9 / 9.2 | 27 / 8 | outlier knee max (z +6.3); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t47-52_shift` | B | 7_sophie_1_1_1 47.4–52.1 s | 21.2 / 10.3 | 13 / 5 | head at limit 21% |
| `sophie_1_1_1_t473-478` | A | 7_sophie_1_1_1 472.6–478.2 s | 1.1 / 1.2 | 25 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t479-483` | A | 7_sophie_1_1_1 478.7–482.8 s | 2.2 / 1.4 | 17 / 6 | right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t480-484_shift` | B | 7_sophie_1_1_1 480.1–484.1 s | 15.4 / 8.8 | 13 / 4 | right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t485-497` | A | 7_sophie_1_1_1 485.3–496.9 s | 2.8 / 1.3 | 15 / 5 | right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t495-499_shift` | B | 7_sophie_1_1_1 494.9–499.4 s | 15.0 / 8.5 | 13 / 5 | outlier knee max (z +5.8); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t497-502` | A | 7_sophie_1_1_1 497.4–502.0 s | 4.5 / 3.2 | 14 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t50-54` | A | 7_sophie_1_1_1 50.1–54.3 s | 3.1 / 0.9 | 15 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t500-508_shift` | B | 7_sophie_1_1_1 500.0–507.8 s | 16.5 / 8.1 | 20 / 7 | outlier knee max (z +6.6); right arm behind body 7 cm (human's in front) |
| `sophie_1_1_1_t506-523` | A | 7_sophie_1_1_1 505.8–523.4 s | 9.1 / 3.1 | 22 / 9 | outlier knee max (z +3.9); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t541-547` | A | 7_sophie_1_1_1 540.9–546.7 s | 2.0 / 1.3 | 19 / 8 | elbow bend at limit 8% |
| `sophie_1_1_1_t547-557` | A | 7_sophie_1_1_1 547.3–556.5 s | 9.9 / 3.9 | 19 / 6 | knee 61 deg; outlier knee max (z +8.2) |
| `sophie_1_1_1_t555-560_shift` | B | 7_sophie_1_1_1 554.5–560.0 s | 15.4 / 5.9 | 20 / 6 | knee 61 deg; outlier knee max (z +8.2); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t583-590` | A | 7_sophie_1_1_1 583.2–590.2 s | 4.8 / 1.5 | 13 / 4 | elbow bend at limit 29%; right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t588-593_shift` | B | 7_sophie_1_1_1 588.2–592.7 s | 13.9 / 8.1 | 16 / 5 | outlier knee max (z +5.2); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t591-600` | A | 7_sophie_1_1_1 590.7–599.8 s | 8.6 / 2.9 | 16 / 6 | elbow bend at limit 7%; leg at limit 7%; right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t60-66_shift` | B | 7_sophie_1_1_1 60.5–66.2 s | 16.1 / 9.4 | 24 / 9 | outlier knee max (z +5.4); right arm behind body 6 cm (human's in front) |
| `sophie_1_1_1_t68-73_shift` | B | 7_sophie_1_1_1 68.3–73.0 s | 19.9 / 11.0 | 23 / 6 | elbow bend at limit 26%; outlier knee max (z +6.4); right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t71-76` | A | 7_sophie_1_1_1 71.0–75.7 s | 4.6 / 4.0 | 22 / 7 | elbow bend at limit 27%; right arm behind body 5 cm (human's in front) |
| `sophie_1_1_1_t94-99` | A | 7_sophie_1_1_1 93.5–99.0 s | 3.4 / 1.0 | 21 / 7 | elbow bend at limit 14% |
| `sophie_1_1_1_t96-100_shift` | B | 7_sophie_1_1_1 96.2–100.2 s | 25.2 / 13.2 | 22 / 6 | human steps; elbow bend at limit 14%; outlier knee max (z +6.5) |
| `sophie_1_2_2_t0-6` | A | 7_sophie_1_2_2 0.0–5.6 s | 6.3 / 0.9 | 28 / 11 | elbow bend at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t101-108` | A | 7_sophie_1_2_2 101.1–107.7 s | 1.9 / 1.1 | 24 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t106-110_shift` | B | 7_sophie_1_2_2 105.7–110.4 s | 12.8 / 7.4 | 23 / 6 | head at limit 10%; right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t108-114` | A | 7_sophie_1_2_2 108.4–113.8 s | 6.0 / 1.5 | 21 / 8 | right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t112-116_shift` | B | 7_sophie_1_2_2 111.8–116.4 s | 12.7 / 8.9 | 28 / 10 | outlier knee max (z +5.4); right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t114-119` | A | 7_sophie_1_2_2 114.4–119.2 s | 2.0 / 1.1 | 25 / 9 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t117-122_shift` | B | 7_sophie_1_2_2 117.2–121.6 s | 11.9 / 6.1 | 21 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t120-135` | A | 7_sophie_1_2_2 119.6–134.7 s | 8.0 / 3.1 | 16 / 5 | elbow bend at limit 5%; outlier knee max (z +5.5) |
| `sophie_1_2_2_t13-17_shift` | B | 7_sophie_1_2_2 12.9–17.3 s | 7.8 / 3.3 | 15 / 5 | elbow bend at limit 15% |
| `sophie_1_2_2_t135-142` | A | 7_sophie_1_2_2 135.1–141.5 s | 2.4 / 1.1 | 19 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t140-144_shift` | B | 7_sophie_1_2_2 139.5–143.9 s | 10.2 / 6.2 | 21 / 7 | elbow bend at limit 8%; outlier knee max (z +3.9) |
| `sophie_1_2_2_t147-154_shift` | B | 7_sophie_1_2_2 146.8–154.3 s | 16.6 / 8.1 | 20 / 7 | outlier knee max (z +7.3); right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t15-27` | A | 7_sophie_1_2_2 15.3–27.0 s | 7.6 / 3.0 | 23 / 9 | elbow bend at limit 10% |
| `sophie_1_2_2_t152-158` | A | 7_sophie_1_2_2 152.3–157.6 s | 4.8 / 1.2 | 21 / 7 | right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t156-163_shift` | B | 7_sophie_1_2_2 155.6–163.1 s | 11.8 / 8.5 | 24 / 6 | outlier knee max (z +8.0); right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t161-171` | A | 7_sophie_1_2_2 161.1–171.0 s | 6.4 / 2.4 | 21 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t169-174_shift` | B | 7_sophie_1_2_2 169.0–173.5 s | 12.5 / 7.5 | 25 / 8 | head at limit 7%; outlier knee max (z +5.8) |
| `sophie_1_2_2_t172-177` | A | 7_sophie_1_2_2 171.5–177.0 s | 6.0 / 4.0 | 22 / 8 | head at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t175-183_shift` | B | 7_sophie_1_2_2 175.0–182.8 s | 17.1 / 9.3 | 26 / 9 | outlier knee max (z +5.8); right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t181-198` | A | 7_sophie_1_2_2 180.8–198.2 s | 6.2 / 1.8 | 26 / 10 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t196-201_shift` | B | 7_sophie_1_2_2 196.2–200.7 s | 18.4 / 9.9 | 13 / 7 | head at limit 10%; outlier knee max (z +4.3); right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t199-204` | A | 7_sophie_1_2_2 198.7–203.6 s | 2.8 / 1.4 | 13 / 7 | head at limit 10%; right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t221-229` | A | 7_sophie_1_2_2 221.4–229.0 s | 2.1 / 1.4 | 6 / 3 | elbow bend at limit 7% |
| `sophie_1_2_2_t227-232_shift` | B | 7_sophie_1_2_2 227.0–231.5 s | 12.4 / 8.8 | 21 / 8 | elbow bend at limit 17% |
| `sophie_1_2_2_t233-246_shift` | B | 7_sophie_1_2_2 233.2–246.3 s | 20.1 / 11.6 | 16 / 6 | elbow bend at limit 12%; outlier knee max (z +6.5); right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t244-250` | A | 7_sophie_1_2_2 244.3–249.6 s | 9.9 / 2.3 | 28 / 10 | elbow bend at limit 13%; outlier knee max (z +4.5); right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t25-30_shift` | B | 7_sophie_1_2_2 25.0–29.5 s | 15.9 / 8.8 | 29 / 8 | outlier knee max (z +5.0) |
| `sophie_1_2_2_t262-267` | A | 7_sophie_1_2_2 262.3–267.0 s | 6.3 / 4.1 | 16 / 5 | right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t271-276` | A | 7_sophie_1_2_2 270.6–276.1 s | 3.0 / 1.1 | 14 / 4 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t277-285` | A | 7_sophie_1_2_2 276.9–284.6 s | 8.7 / 3.3 | 19 / 8 | outlier knee max (z +5.0) |
| `sophie_1_2_2_t28-32` | A | 7_sophie_1_2_2 27.5–32.2 s | 2.9 / 0.7 | 21 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t283-287_shift` | B | 7_sophie_1_2_2 282.6–287.0 s | 14.2 / 8.0 | 25 / 9 | right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t285-289` | A | 7_sophie_1_2_2 285.0–289.0 s | 1.5 / 0.7 | 30 / 11 | right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t290-296` | A | 7_sophie_1_2_2 289.7–296.3 s | 9.9 / 2.2 | 18 / 6 | elbow bend at limit 5%; right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t294-302_shift` | B | 7_sophie_1_2_2 294.3–301.7 s | 10.0 / 2.8 | 23 / 8 | outlier knee max (z +4.8) |
| `sophie_1_2_2_t300-306` | A | 7_sophie_1_2_2 299.7–306.0 s | 10.0 / 2.8 | 21 / 8 | outlier knee max (z +4.8); right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t304-313_shift` | B | 7_sophie_1_2_2 304.0–312.8 s | 22.3 / 13.1 | 21 / 9 | elbow bend at limit 6%; outlier knee max (z +7.4); right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t311-324` | A | 7_sophie_1_2_2 310.8–323.7 s | 5.6 / 1.9 | 23 / 9 | elbow bend at limit 5%; right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t322-326_shift` | B | 7_sophie_1_2_2 321.7–326.2 s | 17.6 / 10.0 | 28 / 11 | outlier knee max (z +6.4) |
| `sophie_1_2_2_t347-356` | A | 7_sophie_1_2_2 346.7–355.8 s | 0.9 / 1.0 | 15 / 6 | elbow bend at limit 44% |
| `sophie_1_2_2_t356-361` | A | 7_sophie_1_2_2 356.4–361.0 s | 4.6 / 1.1 | 18 / 11 | right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t362-373` | A | 7_sophie_1_2_2 361.7–372.9 s | 1.9 / 1.3 | 24 / 9 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t374-378` | A | 7_sophie_1_2_2 373.5–377.6 s | 3.0 / 2.0 | 15 / 6 | elbow bend at limit 11%; right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t389-393_shift` | B | 7_sophie_1_2_2 389.0–393.0 s | 12.7 / 8.0 | 31 / 11 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t390-396` | A | 7_sophie_1_2_2 390.5–396.5 s | 1.9 / 0.6 | 24 / 9 | elbow bend at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t394-400_shift` | B | 7_sophie_1_2_2 394.5–399.5 s | 14.3 / 6.4 | 16 / 7 | elbow bend at limit 7%; right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t398-403` | A | 7_sophie_1_2_2 397.5–402.7 s | 4.6 / 1.9 | 23 / 10 | right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t400-404_shift` | B | 7_sophie_1_2_2 399.7–403.7 s | 25.0 / 13.7 | 26 / 10 | outlier knee max (z +7.7); right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t404-418_shift` | B | 7_sophie_1_2_2 403.7–417.7 s | 12.2 / 4.3 | 23 / 8 | leg at limit 8%; outlier knee max (z +7.4); right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t412-417` | A | 7_sophie_1_2_2 411.7–417.0 s | 6.0 / 1.5 | 24 / 9 | right arm behind body 9 cm (human's in front) |
| `sophie_1_2_2_t418-425` | A | 7_sophie_1_2_2 418.2–425.5 s | 3.1 / 1.3 | 24 / 9 | elbow bend at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t423-432_shift` | B | 7_sophie_1_2_2 423.5–431.5 s | 23.9 / 13.0 | 27 / 10 | elbow bend at limit 5%; outlier knee max (z +7.0) |
| `sophie_1_2_2_t43-48` | A | 7_sophie_1_2_2 43.3–47.7 s | 1.4 / 1.1 | 21 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t430-434` | A | 7_sophie_1_2_2 429.5–434.5 s | 2.1 / 1.0 | 32 / 11 | elbow bend at limit 5% |
| `sophie_1_2_2_t432-437_shift` | B | 7_sophie_1_2_2 432.5–437.0 s | 16.2 / 10.0 | 24 / 9 | outlier knee max (z +7.0); right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t435-442` | A | 7_sophie_1_2_2 435.0–441.8 s | 4.8 / 1.6 | 30 / 10 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t446-458` | A | 7_sophie_1_2_2 446.1–457.9 s | 10.0 / 2.8 | 22 / 9 | elbow bend at limit 11%; outlier knee max (z +6.9) |
| `sophie_1_2_2_t456-462_shift` | B | 7_sophie_1_2_2 455.9–462.2 s | 25.0 / 14.4 | 15 / 7 | outlier knee max (z +6.9) |
| `sophie_1_2_2_t463-468_shift` | B | 7_sophie_1_2_2 463.1–467.7 s | 22.2 / 12.6 | 17 / 8 | outlier knee max (z +7.6) |
| `sophie_1_2_2_t475-481` | A | 7_sophie_1_2_2 475.2–481.0 s | 7.2 / 4.4 | 19 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_2_2_t48-56` | A | 7_sophie_1_2_2 48.2–55.9 s | 5.3 / 3.4 | 17 / 5 | elbow bend at limit 37% |
| `sophie_1_2_2_t482-492` | A | 7_sophie_1_2_2 481.7–491.9 s | 2.7 / 1.9 | 22 / 8 | elbow bend at limit 11%; right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t496-500_shift` | B | 7_sophie_1_2_2 496.3–500.3 s | 24.9 / 14.5 | 31 / 11 | outlier knee max (z +6.3) |
| `sophie_1_2_2_t530-536` | A | 7_sophie_1_2_2 530.1–535.9 s | 6.3 / 3.8 | 14 / 5 | elbow bend at limit 8% |
| `sophie_1_2_2_t537-547` | A | 7_sophie_1_2_2 536.6–547.0 s | 1.5 / 1.2 | 8 / 4 | elbow bend at limit 8% |
| `sophie_1_2_2_t562-568` | A | 7_sophie_1_2_2 562.4–567.6 s | 7.7 / 3.9 | 23 / 9 | outlier knee max (z +3.9) |
| `sophie_1_2_2_t566-570_shift` | B | 7_sophie_1_2_2 565.6–570.1 s | 13.2 / 7.1 | 12 / 6 | outlier knee max (z +6.4); right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t568-573` | A | 7_sophie_1_2_2 568.1–572.8 s | 3.6 / 1.6 | 13 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t574-581` | A | 7_sophie_1_2_2 573.6–581.5 s | 1.6 / 0.9 | 14 / 5 | elbow bend at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t582-587` | A | 7_sophie_1_2_2 582.1–587.4 s | 10.0 / 2.4 | 18 / 7 | elbow bend at limit 19%; outlier knee max (z +3.8); right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t590-594_shift` | B | 7_sophie_1_2_2 589.6–594.1 s | 10.0 / 2.5 | 19 / 7 | outlier knee max (z +7.0); right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t592-596` | A | 7_sophie_1_2_2 592.1–596.4 s | 4.5 / 1.1 | 24 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t597-605` | A | 7_sophie_1_2_2 597.2–604.8 s | 1.3 / 0.9 | 13 / 7 | right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t60-66` | A | 7_sophie_1_2_2 60.4–66.1 s | 7.3 / 2.5 | 15 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_2_2_t67-73` | A | 7_sophie_1_2_2 66.8–72.6 s | 1.0 / 0.8 | 22 / 8 | right arm behind body 7 cm (human's in front) |
| `sophie_1_2_2_t81-97` | A | 7_sophie_1_2_2 81.1–96.7 s | 2.1 / 1.3 | 25 / 9 | elbow bend at limit 9%; right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t0-7_shift` | B | 7_sophie_1_3_3 0.0–6.9 s | 22.9 / 11.8 | 32 / 8 | outlier knee max (z +8.0) |
| `sophie_1_3_3_t125-129` | A | 7_sophie_1_3_3 124.7–129.1 s | 2.2 / 1.9 | 23 / 8 | elbow bend at limit 13%; right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t132-137` | A | 7_sophie_1_3_3 132.4–137.0 s | 2.2 / 0.9 | 12 / 4 | right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t138-146` | A | 7_sophie_1_3_3 137.8–146.4 s | 2.3 / 1.4 | 16 / 6 | elbow bend at limit 6%; right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t150-155` | A | 7_sophie_1_3_3 150.5–154.8 s | 6.4 / 1.1 | 16 / 6 | elbow bend at limit 52%; right arm behind body 7 cm (human's in front) |
| `sophie_1_3_3_t153-157_shift` | B | 7_sophie_1_3_3 152.8–157.2 s | 10.6 / 5.7 | 15 / 5 | elbow bend at limit 26%; right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t155-167` | A | 7_sophie_1_3_3 155.2–166.6 s | 9.5 / 2.8 | 28 / 10 | elbow bend at limit 21%; outlier knee max (z +4.4) |
| `sophie_1_3_3_t165-171_shift` | B | 7_sophie_1_3_3 164.6–171.3 s | 19.1 / 10.2 | 16 / 7 | knee 91 deg; outlier knee max (z +18.3) |
| `sophie_1_3_3_t172-183` | A | 7_sophie_1_3_3 171.9–183.0 s | 1.5 / 1.2 | 19 / 7 | elbow bend at limit 62% |
| `sophie_1_3_3_t184-188` | A | 7_sophie_1_3_3 183.7–188.4 s | 3.0 / 2.2 | 23 / 8 | elbow bend at limit 27%; right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t189-195` | A | 7_sophie_1_3_3 189.1–195.3 s | 2.9 / 0.9 | 13 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t19-26` | A | 7_sophie_1_3_3 19.1–26.1 s | 7.9 / 1.2 | 12 / 6 | elbow bend at limit 12% |
| `sophie_1_3_3_t196-200` | A | 7_sophie_1_3_3 195.9–200.1 s | 3.0 / 1.4 | 14 / 6 | elbow bend at limit 15%; right arm behind body 8 cm (human's in front) |
| `sophie_1_3_3_t201-205` | A | 7_sophie_1_3_3 200.7–204.7 s | 2.9 / 2.5 | 17 / 8 | elbow bend at limit 18%; right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t210-216` | A | 7_sophie_1_3_3 209.8–216.0 s | 2.1 / 2.2 | 20 / 7 | elbow bend at limit 9% |
| `sophie_1_3_3_t221-228_shift` | B | 7_sophie_1_3_3 221.0–228.2 s | 18.5 / 9.9 | 14 / 6 | knee 62 deg; head at limit 5%; outlier knee max (z +8.8) |
| `sophie_1_3_3_t229-233_shift` | B | 7_sophie_1_3_3 228.5–233.2 s | 18.1 / 10.8 | 29 / 9 | outlier knee max (z +7.0); right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t24-28_shift` | B | 7_sophie_1_3_3 24.1–28.3 s | 9.2 / 2.6 | 12 / 5 | elbow bend at limit 13%; outlier knee max (z +6.9); right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t241-246` | A | 7_sophie_1_3_3 240.6–245.6 s | 4.0 / 1.4 | 44 / 10 | elbow bend at limit 17% |
| `sophie_1_3_3_t242-246_shift` | B | 7_sophie_1_3_3 242.1–246.1 s | 11.8 / 2.1 | 50 / 10 | outlier knee max (z +4.3) |
| `sophie_1_3_3_t247-252` | A | 7_sophie_1_3_3 247.4–251.9 s | 1.8 / 1.4 | 27 / 8 | elbow bend at limit 9% |
| `sophie_1_3_3_t258-263` | A | 7_sophie_1_3_3 257.8–262.7 s | 9.9 / 3.0 | 9 / 3 | outlier knee max (z +5.6) |
| `sophie_1_3_3_t259-263_shift` | B | 7_sophie_1_3_3 259.3–263.3 s | 7.4 / 2.9 | 11 / 3 | outlier knee max (z +4.6) |
| `sophie_1_3_3_t26-33` | A | 7_sophie_1_3_3 26.3–32.8 s | 9.9 / 3.8 | 16 / 7 | elbow bend at limit 30%; outlier knee max (z +7.8) |
| `sophie_1_3_3_t264-274` | A | 7_sophie_1_3_3 264.4–273.9 s | 2.2 / 1.5 | 21 / 7 | elbow bend at limit 21% |
| `sophie_1_3_3_t295-300` | A | 7_sophie_1_3_3 295.0–300.1 s | 2.6 / 1.9 | 26 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t301-309` | A | 7_sophie_1_3_3 300.8–308.8 s | 2.7 / 2.0 | 19 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t309-314` | A | 7_sophie_1_3_3 309.5–313.9 s | 3.6 / 1.9 | 18 / 5 | elbow bend at limit 24%; right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t31-35_shift` | B | 7_sophie_1_3_3 30.8–34.9 s | 1.7 / 0.5 | 15 / 7 | elbow bend at limit 42% |
| `sophie_1_3_3_t321-326` | A | 7_sophie_1_3_3 321.0–326.2 s | 9.6 / 5.6 | 28 / 8 | elbow bend at limit 12% |
| `sophie_1_3_3_t336-342` | A | 7_sophie_1_3_3 335.5–341.5 s | 2.1 / 1.1 | 12 / 5 | right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t355-362` | A | 7_sophie_1_3_3 355.2–362.3 s | 7.8 / 5.8 | 15 / 5 | outlier knee max (z +4.5) |
| `sophie_1_3_3_t36-44` | A | 7_sophie_1_3_3 35.6–44.3 s | 2.9 / 2.1 | 9 / 3 | elbow bend at limit 18% |
| `sophie_1_3_3_t363-371` | A | 7_sophie_1_3_3 362.9–371.4 s | 10.0 / 5.2 | 17 / 6 | elbow bend at limit 10%; outlier knee max (z +5.7) |
| `sophie_1_3_3_t371-384` | A | 7_sophie_1_3_3 371.4–384.1 s | 4.8 / 4.0 | 20 / 7 | elbow bend at limit 13%; right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t394-401_shift` | B | 7_sophie_1_3_3 394.0–401.4 s | 13.8 / 7.8 | 15 / 5 | outlier knee max (z +5.6) |
| `sophie_1_3_3_t415-420_shift` | B | 7_sophie_1_3_3 415.1–419.6 s | 8.3 / 4.3 | 13 / 3 | outlier knee max (z +4.6) |
| `sophie_1_3_3_t418-425` | A | 7_sophie_1_3_3 417.6–424.7 s | 9.9 / 1.8 | 22 / 6 | head at limit 13%; outlier knee max (z +4.0) |
| `sophie_1_3_3_t457-461_shift` | B | 7_sophie_1_3_3 456.7–460.7 s | 15.5 / 7.0 | 28 / 10 | elbow bend at limit 8%; right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t458-465` | A | 7_sophie_1_3_3 458.2–464.8 s | 1.4 / 0.6 | 25 / 10 | elbow bend at limit 18%; right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t463-467_shift` | B | 7_sophie_1_3_3 462.6–466.6 s | 23.5 / 13.3 | 21 / 9 | outlier knee max (z +3.9); right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t471-477` | A | 7_sophie_1_3_3 471.1–476.8 s | 2.6 / 1.5 | 21 / 7 | elbow bend at limit 17% |
| `sophie_1_3_3_t51-59_shift` | B | 7_sophie_1_3_3 51.0–58.6 s | 13.9 / 5.3 | 26 / 9 | elbow bend at limit 18%; outlier knee max (z +5.4); right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t514-523` | A | 7_sophie_1_3_3 513.7–522.7 s | 4.3 / 3.9 | 15 / 6 | elbow bend at limit 7% |
| `sophie_1_3_3_t530-537_shift` | B | 7_sophie_1_3_3 529.9–537.1 s | 11.4 / 3.4 | 18 / 5 | outlier knee max (z +4.3) |
| `sophie_1_3_3_t535-541` | A | 7_sophie_1_3_3 535.1–540.7 s | 1.8 / 1.3 | 16 / 5 | elbow bend at limit 9% |
| `sophie_1_3_3_t57-70` | A | 7_sophie_1_3_3 56.6–70.0 s | 2.0 / 1.6 | 22 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t573-581` | A | 7_sophie_1_3_3 573.4–580.6 s | 3.4 / 0.6 | 38 / 9 | head at limit 6%; elbow bend at limit 7% |
| `sophie_1_3_3_t67-71_shift` | B | 7_sophie_1_3_3 66.7–70.7 s | 26.0 / 13.9 | 19 / 6 | human steps; outlier knee max (z +7.4); right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t71-76` | A | 7_sophie_1_3_3 70.6–76.0 s | 3.6 / 2.3 | 27 / 11 | elbow bend at limit 30%; right arm behind body 5 cm (human's in front) |
| `sophie_1_3_3_t74-78_shift` | B | 7_sophie_1_3_3 74.0–78.4 s | 6.4 / 2.0 | 19 / 11 | elbow bend at limit 74%; outlier knee max (z +4.0) |
| `sophie_1_3_3_t76-84` | A | 7_sophie_1_3_3 76.4–84.0 s | 9.7 / 2.7 | 9 / 4 | elbow bend at limit 26%; outlier knee max (z +4.0) |
| `sophie_1_3_3_t85-90` | A | 7_sophie_1_3_3 84.8–90.1 s | 1.2 / 0.9 | 19 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_3_3_t91-99` | A | 7_sophie_1_3_3 90.8–99.4 s | 4.6 / 3.1 | 15 / 5 | elbow bend at limit 15%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t10-14` | A | 7_sophie_1_4_4 9.7–14.3 s | 4.8 / 1.9 | 12 / 5 | head at limit 7% |
| `sophie_1_4_4_t100-117` | A | 7_sophie_1_4_4 100.0–116.7 s | 9.1 / 5.7 | 19 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t117-133` | A | 7_sophie_1_4_4 116.7–133.4 s | 1.9 / 1.7 | 17 / 7 | elbow bend at limit 26%; right arm behind body 5 cm (human's in front) |
| `sophie_1_4_4_t133-150` | A | 7_sophie_1_4_4 133.4–150.1 s | 2.2 / 1.0 | 15 / 6 | elbow bend at limit 9%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t150-167` | A | 7_sophie_1_4_4 150.1–166.8 s | 2.0 / 0.8 | 14 / 6 | elbow bend at limit 14% |
| `sophie_1_4_4_t167-184` | A | 7_sophie_1_4_4 166.8–183.5 s | 2.3 / 0.8 | 16 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t182-186_shift` | B | 7_sophie_1_4_4 181.5–186.0 s | 12.4 / 7.2 | 12 / 5 | head at limit 21%; outlier knee max (z +5.6); right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t184-200` | A | 7_sophie_1_4_4 184.0–200.2 s | 8.9 / 6.9 | 18 / 7 | knee 66 deg; head at limit 6%; outlier knee max (z +10.0); right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t198-203_shift` | B | 7_sophie_1_4_4 198.2–202.8 s | 13.1 / 9.2 | 10 / 4 | knee 66 deg; outlier knee max (z +10.0); right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t201-218` | A | 7_sophie_1_4_4 200.8–217.9 s | 1.5 / 1.3 | 19 / 7 | elbow bend at limit 10%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t218-235` | A | 7_sophie_1_4_4 217.9–235.0 s | 3.6 / 1.1 | 22 / 7 | elbow bend at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t233-237_shift` | B | 7_sophie_1_4_4 232.8–236.8 s | 26.0 / 13.7 | 33 / 11 | human steps; outlier knee max (z +6.2); right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t236-241` | A | 7_sophie_1_4_4 235.6–240.8 s | 2.8 / 1.5 | 17 / 7 | right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t255-260` | A | 7_sophie_1_4_4 254.9–259.6 s | 7.5 / 1.1 | 22 / 7 | elbow bend at limit 10%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t258-262_shift` | B | 7_sophie_1_4_4 257.6–262.2 s | 7.2 / 2.9 | 21 / 7 | outlier knee max (z +5.1); right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t260-275` | A | 7_sophie_1_4_4 260.2–275.0 s | 2.0 / 1.4 | 17 / 8 | elbow bend at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t275-290` | A | 7_sophie_1_4_4 275.0–289.8 s | 5.1 / 1.1 | 17 / 6 | elbow bend at limit 20%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t288-293_shift` | B | 7_sophie_1_4_4 287.8–292.6 s | 16.3 / 10.0 | 18 / 6 | outlier knee max (z +5.6); right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t291-300` | A | 7_sophie_1_4_4 290.6–300.0 s | 3.4 / 1.4 | 20 / 7 | elbow bend at limit 27%; right arm behind body 5 cm (human's in front) |
| `sophie_1_4_4_t305-309` | A | 7_sophie_1_4_4 304.9–309.2 s | 3.9 / 3.0 | 15 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t316-321` | A | 7_sophie_1_4_4 315.8–321.1 s | 5.8 / 3.7 | 13 / 5 | elbow bend at limit 11%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t322-327` | A | 7_sophie_1_4_4 321.9–327.1 s | 1.2 / 0.7 | 14 / 4 | elbow bend at limit 16% |
| `sophie_1_4_4_t335-346` | A | 7_sophie_1_4_4 335.1–345.7 s | 2.1 / 1.7 | 21 / 8 | right arm behind body 5 cm (human's in front) |
| `sophie_1_4_4_t346-356` | A | 7_sophie_1_4_4 345.7–356.3 s | 2.0 / 1.6 | 23 / 9 | right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t361-367_shift` | B | 7_sophie_1_4_4 360.6–366.9 s | 12.0 / 7.1 | 17 / 6 | elbow bend at limit 29% |
| `sophie_1_4_4_t365-382` | A | 7_sophie_1_4_4 364.9–381.7 s | 1.9 / 0.9 | 7 / 3 | head at limit 20% |
| `sophie_1_4_4_t382-398` | A | 7_sophie_1_4_4 381.7–398.4 s | 4.0 / 1.9 | 15 / 5 | elbow bend at limit 15% |
| `sophie_1_4_4_t398-415` | A | 7_sophie_1_4_4 398.4–415.2 s | 6.6 / 3.6 | 18 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t413-418_shift` | B | 7_sophie_1_4_4 413.2–418.4 s | 16.5 / 14.7 | 15 / 6 | knee 79 deg; outlier knee max (z +14.3); right arm behind body 5 cm (human's in front) |
| `sophie_1_4_4_t416-435` | A | 7_sophie_1_4_4 416.4–434.7 s | 2.8 / 2.9 | 21 / 7 | elbow bend at limit 7% |
| `sophie_1_4_4_t435-453` | A | 7_sophie_1_4_4 434.7–453.0 s | 2.3 / 0.8 | 22 / 8 | right arm behind body 5 cm (human's in front) |
| `sophie_1_4_4_t451-456_shift` | B | 7_sophie_1_4_4 451.0–455.6 s | 18.0 / 10.7 | 23 / 8 | outlier knee max (z +7.3); right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t454-459` | A | 7_sophie_1_4_4 453.6–458.7 s | 3.6 / 1.3 | 12 / 5 | right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t457-461_shift` | B | 7_sophie_1_4_4 456.7–461.4 s | 11.1 / 2.6 | 10 / 4 | right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t459-468` | A | 7_sophie_1_4_4 459.4–468.0 s | 8.8 / 2.8 | 11 / 4 | outlier knee max (z +5.5); right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t469-474` | A | 7_sophie_1_4_4 469.0–473.6 s | 5.9 / 1.6 | 10 / 4 | right arm behind body 8 cm (human's in front) |
| `sophie_1_4_4_t474-480` | A | 7_sophie_1_4_4 474.4–479.8 s | 9.4 / 3.7 | 13 / 4 | right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t480-490` | A | 7_sophie_1_4_4 479.8–489.8 s | 1.3 / 1.0 | 17 / 5 | elbow bend at limit 11%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t490-500` | A | 7_sophie_1_4_4 489.8–499.8 s | 4.4 / 1.3 | 16 / 5 | elbow bend at limit 22%; right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t500-507_shift` | B | 7_sophie_1_4_4 500.4–506.5 s | 23.3 / 12.8 | 15 / 4 | elbow bend at limit 12%; outlier knee max (z +6.1); right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t528-547` | A | 7_sophie_1_4_4 528.5–547.0 s | 2.6 / 1.0 | 14 / 5 | elbow bend at limit 7%; right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t56-74` | A | 7_sophie_1_4_4 56.4–74.2 s | 2.1 / 1.1 | 16 / 6 | elbow bend at limit 8%; right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t566-584` | A | 7_sophie_1_4_4 565.6–584.2 s | 4.2 / 1.3 | 18 / 6 | elbow bend at limit 6%; right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t582-587_shift` | B | 7_sophie_1_4_4 582.2–586.6 s | 9.1 / 4.8 | 18 / 5 | right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t585-603` | A | 7_sophie_1_4_4 584.6–603.2 s | 8.8 / 2.2 | 22 / 7 | outlier knee max (z +6.1); right arm behind body 6 cm (human's in front) |
| `sophie_1_4_4_t75-86` | A | 7_sophie_1_4_4 74.7–86.4 s | 1.5 / 1.6 | 14 / 5 | elbow bend at limit 9%; right arm behind body 5 cm (human's in front) |
| `sophie_1_4_4_t87-92_shift` | B | 7_sophie_1_4_4 86.9–92.3 s | 17.6 / 10.3 | 17 / 7 | right arm behind body 7 cm (human's in front) |
| `sophie_1_4_4_t90-96` | A | 7_sophie_1_4_4 90.3–95.7 s | 1.5 / 1.2 | 12 / 4 | elbow bend at limit 5%; right arm behind body 8 cm (human's in front) |
| `sophie_1_4_4_t94-102_shift` | B | 7_sophie_1_4_4 93.7–102.0 s | 16.5 / 8.5 | 18 / 6 | outlier knee max (z +6.3); right arm behind body 7 cm (human's in front) |
| `sophie_1_5_5_t0-8_shift` | B | 7_sophie_1_5_5 0.0–7.7 s | 17.0 / 9.5 | 15 / 7 | knee 67 deg; outlier knee max (z +10.4) |
| `sophie_1_5_5_t102-107` | A | 7_sophie_1_5_5 101.5–107.2 s | 1.7 / 1.1 | 15 / 5 | elbow bend at limit 31% |
| `sophie_1_5_5_t108-114` | A | 7_sophie_1_5_5 107.9–114.4 s | 1.7 / 1.1 | 15 / 5 | right arm behind body 7 cm (human's in front) |
| `sophie_1_5_5_t115-131` | A | 7_sophie_1_5_5 115.1–130.6 s | 1.5 / 0.6 | 7 / 3 | elbow bend at limit 5% |
| `sophie_1_5_5_t131-146` | A | 7_sophie_1_5_5 130.6–146.1 s | 1.2 / 1.1 | 14 / 5 | elbow bend at limit 26%; right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t144-153_shift` | B | 7_sophie_1_5_5 144.1–152.8 s | 21.3 / 14.5 | 20 / 7 | knee 65 deg; elbow bend at limit 5%; outlier knee max (z +9.5); right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t155-171` | A | 7_sophie_1_5_5 154.7–170.5 s | 2.6 / 1.4 | 19 / 7 | elbow bend at limit 11% |
| `sophie_1_5_5_t171-189` | A | 7_sophie_1_5_5 170.9–188.5 s | 1.7 / 1.6 | 20 / 8 | elbow bend at limit 12%; right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t187-191_shift` | B | 7_sophie_1_5_5 186.5–191.2 s | 19.0 / 10.2 | 25 / 10 | elbow bend at limit 6%; outlier knee max (z +5.2) |
| `sophie_1_5_5_t194-198_shift` | B | 7_sophie_1_5_5 193.5–198.0 s | 12.1 / 5.7 | 26 / 9 | outlier knee max (z +3.8); right arm behind body 5 cm (human's in front) |
| `sophie_1_5_5_t20-35` | A | 7_sophie_1_5_5 20.5–35.2 s | 10.3 / 2.9 | 13 / 5 | human steps; outlier knee max (z +4.0) |
| `sophie_1_5_5_t201-206_shift` | B | 7_sophie_1_5_5 201.1–205.6 s | 16.1 / 8.5 | 9 / 4 | outlier knee max (z +4.9) |
| `sophie_1_5_5_t206-211_shift` | B | 7_sophie_1_5_5 206.1–210.7 s | 18.6 / 10.6 | 9 / 3 | elbow bend at limit 12%; outlier knee max (z +3.7) |
| `sophie_1_5_5_t209-227` | A | 7_sophie_1_5_5 208.7–226.6 s | 6.4 / 1.6 | 13 / 5 | elbow bend at limit 10%; right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t244-262` | A | 7_sophie_1_5_5 244.4–262.3 s | 2.2 / 1.0 | 17 / 7 | elbow bend at limit 16%; right arm behind body 5 cm (human's in front) |
| `sophie_1_5_5_t259-263_shift` | B | 7_sophie_1_5_5 259.1–263.1 s | 25.3 / 13.4 | 19 / 8 | human steps; outlier knee max (z +5.3); right arm behind body 5 cm (human's in front) |
| `sophie_1_5_5_t263-269_shift` | B | 7_sophie_1_5_5 263.1–268.5 s | 19.3 / 10.9 | 13 / 7 | elbow bend at limit 13%; outlier knee max (z +3.8); right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t267-272` | A | 7_sophie_1_5_5 266.5–271.7 s | 3.4 / 1.4 | 10 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t270-274_shift` | B | 7_sophie_1_5_5 269.7–274.1 s | 9.5 / 5.5 | 10 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t272-289` | A | 7_sophie_1_5_5 272.1–288.9 s | 3.7 / 3.3 | 16 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t287-291_shift` | B | 7_sophie_1_5_5 286.9–291.5 s | 6.8 / 5.1 | 14 / 6 | elbow bend at limit 10%; right arm behind body 5 cm (human's in front) |
| `sophie_1_5_5_t289-305` | A | 7_sophie_1_5_5 289.5–305.4 s | 2.3 / 1.1 | 19 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_5_5_t305-321` | A | 7_sophie_1_5_5 305.4–321.4 s | 6.2 / 3.5 | 17 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t322-340` | A | 7_sophie_1_5_5 322.5–340.4 s | 5.1 / 3.3 | 17 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t33-38_shift` | B | 7_sophie_1_5_5 33.2–37.7 s | 14.8 / 8.0 | 21 / 7 | elbow bend at limit 17%; outlier knee max (z +4.2); right arm behind body 5 cm (human's in front) |
| `sophie_1_5_5_t338-347_shift` | B | 7_sophie_1_5_5 338.4–347.1 s | 11.1 / 8.0 | 19 / 7 | elbow bend at limit 14%; outlier knee max (z +3.6); right arm behind body 7 cm (human's in front) |
| `sophie_1_5_5_t345-351` | A | 7_sophie_1_5_5 345.1–350.6 s | 5.7 / 1.3 | 18 / 7 | right arm behind body 7 cm (human's in front) |
| `sophie_1_5_5_t349-353_shift` | B | 7_sophie_1_5_5 348.6–353.2 s | 12.5 / 6.6 | 23 / 9 | elbow bend at limit 18%; outlier knee max (z +3.7); right arm behind body 7 cm (human's in front) |
| `sophie_1_5_5_t351-357` | A | 7_sophie_1_5_5 351.2–357.4 s | 8.0 / 1.1 | 26 / 9 | elbow bend at limit 10%; right arm behind body 7 cm (human's in front) |
| `sophie_1_5_5_t36-40` | A | 7_sophie_1_5_5 35.7–39.7 s | 3.1 / 2.4 | 20 / 7 | elbow bend at limit 48% |
| `sophie_1_5_5_t362-366_shift` | B | 7_sophie_1_5_5 362.5–366.5 s | 25.8 / 13.6 | 20 / 5 | human steps; outlier knee max (z +5.8) |
| `sophie_1_5_5_t408-413_shift` | B | 7_sophie_1_5_5 408.5–412.8 s | 12.2 / 2.4 | 35 / 10 | outlier knee max (z +4.8) |
| `sophie_1_5_5_t41-45` | A | 7_sophie_1_5_5 40.5–45.3 s | 1.8 / 1.2 | 18 / 7 | elbow bend at limit 10% |
| `sophie_1_5_5_t416-421` | A | 7_sophie_1_5_5 416.0–420.7 s | 1.1 / 0.7 | 30 / 9 | right arm behind body 5 cm (human's in front) |
| `sophie_1_5_5_t446-450` | A | 7_sophie_1_5_5 445.6–450.0 s | 3.2 / 1.4 | 13 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t451-456_shift` | B | 7_sophie_1_5_5 450.9–456.0 s | 14.9 / 6.4 | 29 / 10 | right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t457-468` | A | 7_sophie_1_5_5 456.9–467.6 s | 6.1 / 1.0 | 30 / 10 | right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t46-51_shift` | B | 7_sophie_1_5_5 45.8–51.2 s | 18.0 / 9.7 | 21 / 7 | elbow bend at limit 17% |
| `sophie_1_5_5_t484-492` | A | 7_sophie_1_5_5 483.6–491.9 s | 3.9 / 1.2 | 19 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_5_5_t49-63` | A | 7_sophie_1_5_5 49.2–63.1 s | 9.0 / 4.3 | 16 / 6 | elbow bend at limit 29%; right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t570-577` | A | 7_sophie_1_5_5 569.8–577.4 s | 1.9 / 1.3 | 40 / 13 | elbow bend at limit 20%; right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t587-600` | A | 7_sophie_1_5_5 587.3–599.8 s | 3.4 / 1.7 | 25 / 7 | shoulder at limit 16%; elbow bend at limit 14% |
| `sophie_1_5_5_t6-20` | A | 7_sophie_1_5_5 5.7–20.5 s | 1.6 / 2.4 | 11 / 4 | elbow bend at limit 37% |
| `sophie_1_5_5_t63-77` | A | 7_sophie_1_5_5 63.1–77.1 s | 1.4 / 1.0 | 13 / 5 | elbow bend at limit 36%; right arm behind body 6 cm (human's in front) |
| `sophie_1_5_5_t77-91` | A | 7_sophie_1_5_5 77.1–91.0 s | 1.1 / 1.2 | 11 / 4 | elbow bend at limit 17%; right arm behind body 5 cm (human's in front) |
| `sophie_1_5_5_t89-94_shift` | B | 7_sophie_1_5_5 89.0–93.9 s | 10.7 / 6.1 | 17 / 7 | elbow bend at limit 36% |
| `sophie_1_5_5_t92-101` | A | 7_sophie_1_5_5 91.9–100.9 s | 4.7 / 1.5 | 14 / 6 | elbow bend at limit 15% |
| `sophie_1_6_6_t0-7` | A | 7_sophie_1_6_6 0.0–7.2 s | 9.4 / 1.6 | 13 / 5 | elbow bend at limit 6%; right arm behind body 7 cm (human's in front) |
| `sophie_1_6_6_t14-19` | A | 7_sophie_1_6_6 13.5–19.5 s | 3.8 / 1.2 | 21 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t144-154` | A | 7_sophie_1_6_6 143.6–154.1 s | 1.7 / 1.4 | 15 / 4 | elbow bend at limit 10% |
| `sophie_1_6_6_t155-159` | A | 7_sophie_1_6_6 154.7–158.7 s | 7.4 / 3.9 | 19 / 6 | elbow bend at limit 17%; right arm behind body 5 cm (human's in front) |
| `sophie_1_6_6_t159-168` | A | 7_sophie_1_6_6 159.4–168.2 s | 3.7 / 1.4 | 12 / 6 | elbow bend at limit 10%; right arm behind body 7 cm (human's in front) |
| `sophie_1_6_6_t169-178` | A | 7_sophie_1_6_6 168.8–178.0 s | 2.6 / 0.9 | 14 / 5 | elbow bend at limit 18% |
| `sophie_1_6_6_t20-25` | A | 7_sophie_1_6_6 20.1–25.1 s | 2.3 / 2.1 | 15 / 5 | right arm behind body 5 cm (human's in front) |
| `sophie_1_6_6_t204-213` | A | 7_sophie_1_6_6 204.2–213.3 s | 2.0 / 1.3 | 20 / 6 | elbow bend at limit 32% |
| `sophie_1_6_6_t223-232_shift` | B | 7_sophie_1_6_6 223.3–231.5 s | 11.9 / 4.0 | 22 / 6 | head at limit 9%; outlier knee max (z +7.2) |
| `sophie_1_6_6_t252-260` | A | 7_sophie_1_6_6 251.9–260.4 s | 3.6 / 1.6 | 20 / 7 | elbow bend at limit 22%; right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t261-267` | A | 7_sophie_1_6_6 261.0–266.5 s | 4.5 / 3.3 | 40 / 11 | elbow bend at limit 7%; right arm behind body 5 cm (human's in front) |
| `sophie_1_6_6_t267-279` | A | 7_sophie_1_6_6 267.3–279.2 s | 5.7 / 4.5 | 19 / 7 | head at limit 7% |
| `sophie_1_6_6_t280-285` | A | 7_sophie_1_6_6 279.9–284.6 s | 2.1 / 0.5 | 32 / 10 | head at limit 13% |
| `sophie_1_6_6_t299-312` | A | 7_sophie_1_6_6 299.4–312.0 s | 7.6 / 2.0 | 19 / 5 | elbow bend at limit 20% |
| `sophie_1_6_6_t319-324` | A | 7_sophie_1_6_6 318.9–324.0 s | 5.8 / 3.9 | 15 / 6 | head at limit 8% |
| `sophie_1_6_6_t325-332` | A | 7_sophie_1_6_6 324.8–332.0 s | 1.3 / 1.6 | 24 / 6 | right arm behind body 5 cm (human's in front) |
| `sophie_1_6_6_t333-337_shift` | B | 7_sophie_1_6_6 332.6–336.6 s | 10.8 / 6.7 | 14 / 6 | head at limit 18%; right arm behind body 5 cm (human's in front) |
| `sophie_1_6_6_t334-340` | A | 7_sophie_1_6_6 333.5–340.3 s | 0.9 / 1.4 | 15 / 5 | right arm behind body 5 cm (human's in front) |
| `sophie_1_6_6_t341-346` | A | 7_sophie_1_6_6 341.1–345.9 s | 6.3 / 1.0 | 32 / 10 | head at limit 13% |
| `sophie_1_6_6_t354-360` | A | 7_sophie_1_6_6 353.7–359.6 s | 2.1 / 2.8 | 29 / 9 | right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t371-375` | A | 7_sophie_1_6_6 371.1–375.5 s | 1.3 / 1.3 | 33 / 10 | elbow bend at limit 10% |
| `sophie_1_6_6_t380-395` | A | 7_sophie_1_6_6 379.9–395.3 s | 4.5 / 2.7 | 29 / 8 | leg at limit 13% |
| `sophie_1_6_6_t399-416` | A | 7_sophie_1_6_6 399.2–415.5 s | 3.1 / 2.4 | 21 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t420-431` | A | 7_sophie_1_6_6 420.0–430.6 s | 9.9 / 1.4 | 25 / 7 | head at limit 5%; elbow bend at limit 5%; outlier knee max (z +5.0) |
| `sophie_1_6_6_t436-448` | A | 7_sophie_1_6_6 436.0–447.9 s | 1.9 / 1.7 | 21 / 6 | right arm behind body 5 cm (human's in front) |
| `sophie_1_6_6_t464-481` | A | 7_sophie_1_6_6 463.9–480.8 s | 10.0 / 4.2 | 8 / 3 | head at limit 15% |
| `sophie_1_6_6_t483-489` | A | 7_sophie_1_6_6 482.9–489.2 s | 1.7 / 0.6 | 13 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t490-496` | A | 7_sophie_1_6_6 489.9–495.9 s | 8.2 / 1.6 | 22 / 7 | elbow bend at limit 12%; right arm behind body 5 cm (human's in front) |
| `sophie_1_6_6_t494-501_shift` | B | 7_sophie_1_6_6 493.9–500.7 s | 10.2 / 2.7 | 20 / 6 | outlier knee max (z +5.9) |
| `sophie_1_6_6_t5-9_shift` | B | 7_sophie_1_6_6 4.7–8.7 s | 25.6 / 12.9 | 20 / 5 | human steps; knee 63 deg; elbow bend at limit 7%; outlier knee max (z +8.9); right arm behind body 7 cm (human's in front) |
| `sophie_1_6_6_t504-508_shift` | B | 7_sophie_1_6_6 503.5–508.3 s | 19.0 / 9.8 | 13 / 4 | outlier knee max (z +5.6) |
| `sophie_1_6_6_t509-527` | A | 7_sophie_1_6_6 509.0–526.9 s | 2.1 / 2.7 | 13 / 7 | elbow bend at limit 17% |
| `sophie_1_6_6_t528-532` | A | 7_sophie_1_6_6 527.6–531.9 s | 3.9 / 3.0 | 16 / 8 | right arm behind body 7 cm (human's in front) |
| `sophie_1_6_6_t536-543` | A | 7_sophie_1_6_6 536.0–542.7 s | 2.2 / 1.3 | 24 / 9 | elbow bend at limit 36% |
| `sophie_1_6_6_t541-546_shift` | B | 7_sophie_1_6_6 540.7–546.4 s | 21.4 / 12.4 | 26 / 9 | elbow bend at limit 59%; outlier knee max (z +4.9); right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t547-552` | A | 7_sophie_1_6_6 546.9–552.1 s | 3.5 / 0.7 | 15 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t550-555_shift` | B | 7_sophie_1_6_6 550.1–555.3 s | 10.4 / 2.9 | 12 / 7 | outlier knee max (z +6.8); right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t556-567` | A | 7_sophie_1_6_6 555.8–567.3 s | 9.0 / 5.6 | 20 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t565-572_shift` | B | 7_sophie_1_6_6 565.3–572.5 s | 21.7 / 10.4 | 14 / 6 | elbow bend at limit 19%; outlier knee max (z +4.7) |
| `sophie_1_6_6_t570-575` | A | 7_sophie_1_6_6 570.5–575.0 s | 4.6 / 1.4 | 21 / 10 | elbow bend at limit 63% |
| `sophie_1_6_6_t580-586` | A | 7_sophie_1_6_6 580.1–586.2 s | 4.1 / 1.9 | 25 / 10 | elbow bend at limit 63% |
| `sophie_1_6_6_t584-592_shift` | B | 7_sophie_1_6_6 584.2–592.4 s | 14.4 / 7.8 | 19 / 7 | elbow bend at limit 23%; outlier knee max (z +3.7) |
| `sophie_1_6_6_t590-598` | A | 7_sophie_1_6_6 590.4–598.2 s | 6.3 / 2.3 | 23 / 10 | elbow bend at limit 53% |
| `sophie_1_6_6_t596-601_shift` | B | 7_sophie_1_6_6 596.2–600.8 s | 13.6 / 9.0 | 15 / 6 | head at limit 8%; right arm behind body 5 cm (human's in front) |
| `sophie_1_6_6_t599-604` | A | 7_sophie_1_6_6 598.8–604.0 s | 2.8 / 1.0 | 17 / 5 | head at limit 7% |
| `sophie_1_6_6_t605-609` | A | 7_sophie_1_6_6 604.7–608.8 s | 0.8 / 1.0 | 16 / 7 | elbow bend at limit 28%; right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t81-88` | A | 7_sophie_1_6_6 80.6–88.4 s | 8.0 / 2.2 | 18 / 5 | elbow bend at limit 10%; right arm behind body 6 cm (human's in front) |
| `sophie_1_6_6_t86-91_shift` | B | 7_sophie_1_6_6 86.4–90.9 s | 11.8 / 4.4 | 20 / 6 | outlier knee max (z +5.5) |
| `sophie_1_6_6_t94-102` | A | 7_sophie_1_6_6 94.5–102.0 s | 1.1 / 0.9 | 14 / 5 | right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t0-6_shift` | B | 7_sophie_1_7_7 0.0–5.6 s | 13.1 / 6.8 | 27 / 8 | elbow bend at limit 17% |
| `sophie_1_7_7_t115-123_shift` | B | 7_sophie_1_7_7 114.9–122.5 s | 19.7 / 11.8 | 16 / 5 | elbow bend at limit 6%; right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t121-140` | A | 7_sophie_1_7_7 120.5–139.5 s | 8.9 / 4.2 | 19 / 8 | elbow bend at limit 18%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t138-142_shift` | B | 7_sophie_1_7_7 137.5–142.0 s | 9.2 / 7.7 | 24 / 8 | elbow bend at limit 34% |
| `sophie_1_7_7_t140-158` | A | 7_sophie_1_7_7 140.0–157.7 s | 9.0 / 4.9 | 26 / 8 | outlier knee max (z +6.3); right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t158-175` | A | 7_sophie_1_7_7 157.7–175.3 s | 11.3 / 2.9 | 17 / 5 | human steps; head at limit 5%; elbow bend at limit 7%; outlier knee max (z +5.8); right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t17-31` | A | 7_sophie_1_7_7 17.2–30.8 s | 2.9 / 0.9 | 19 / 6 | elbow bend at limit 23%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t173-179_shift` | B | 7_sophie_1_7_7 173.3–178.8 s | 16.5 / 8.6 | 17 / 5 | elbow bend at limit 19%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t177-189` | A | 7_sophie_1_7_7 176.8–188.5 s | 6.0 / 2.1 | 17 / 6 | head at limit 6%; elbow bend at limit 13%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t187-191_shift` | B | 7_sophie_1_7_7 186.5–191.2 s | 9.2 / 4.8 | 20 / 7 | elbow bend at limit 29%; right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t189-208` | A | 7_sophie_1_7_7 189.2–208.5 s | 5.5 / 2.5 | 26 / 10 | elbow bend at limit 17% |
| `sophie_1_7_7_t208-228` | A | 7_sophie_1_7_7 208.5–227.8 s | 2.0 / 0.9 | 16 / 7 | elbow bend at limit 13%; right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t226-230_shift` | B | 7_sophie_1_7_7 225.8–230.3 s | 10.9 / 6.4 | 19 / 9 | head at limit 9%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t228-235` | A | 7_sophie_1_7_7 228.3–234.6 s | 7.5 / 4.2 | 27 / 10 | head at limit 6%; elbow bend at limit 14% |
| `sophie_1_7_7_t233-237_shift` | B | 7_sophie_1_7_7 232.6–237.1 s | 9.9 / 6.7 | 21 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t235-244` | A | 7_sophie_1_7_7 235.1–244.3 s | 6.7 / 1.9 | 20 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t242-247_shift` | B | 7_sophie_1_7_7 242.3–247.4 s | 16.0 / 13.2 | 14 / 5 | knee 68 deg; outlier knee max (z +10.6); right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t245-264` | A | 7_sophie_1_7_7 245.4–263.9 s | 1.2 / 0.6 | 20 / 8 | head at limit 6%; elbow bend at limit 14%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t264-282` | A | 7_sophie_1_7_7 263.9–282.4 s | 1.8 / 1.1 | 18 / 6 | elbow bend at limit 21% |
| `sophie_1_7_7_t282-301` | A | 7_sophie_1_7_7 282.4–300.8 s | 2.5 / 1.2 | 23 / 7 | elbow bend at limit 7%; right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t301-319` | A | 7_sophie_1_7_7 300.8–319.3 s | 2.9 / 3.5 | 23 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t31-44` | A | 7_sophie_1_7_7 30.8–44.5 s | 3.6 / 4.5 | 15 / 5 | elbow bend at limit 22%; right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t319-338` | A | 7_sophie_1_7_7 319.3–337.7 s | 3.7 / 1.1 | 18 / 6 | elbow bend at limit 5% |
| `sophie_1_7_7_t336-340_shift` | B | 7_sophie_1_7_7 335.7–340.1 s | 7.8 / 3.8 | 17 / 7 | head at limit 12%; elbow bend at limit 35%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t338-347` | A | 7_sophie_1_7_7 338.1–346.8 s | 7.3 / 10.6 | 17 / 7 | K1 feet move 11 cm; knee 75 deg; elbow bend at limit 8%; outlier knee max (z +13.2) |
| `sophie_1_7_7_t345-349_shift` | B | 7_sophie_1_7_7 344.8–349.4 s | 14.7 / 12.3 | 16 / 6 | knee 75 deg; elbow bend at limit 9%; outlier knee max (z +13.2); right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t347-365` | A | 7_sophie_1_7_7 347.4–365.3 s | 2.2 / 1.3 | 15 / 6 | elbow bend at limit 6%; right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t365-383` | A | 7_sophie_1_7_7 365.3–383.2 s | 5.5 / 1.7 | 21 / 8 | elbow bend at limit 22%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t383-401` | A | 7_sophie_1_7_7 383.2–401.1 s | 6.2 / 1.8 | 19 / 7 | right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t399-404_shift` | B | 7_sophie_1_7_7 399.1–403.6 s | 13.1 / 7.1 | 26 / 9 | outlier knee max (z +4.5) |
| `sophie_1_7_7_t4-17` | A | 7_sophie_1_7_7 3.6–17.2 s | 5.2 / 2.8 | 14 / 6 | head at limit 10%; elbow bend at limit 21%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t408-414_shift` | B | 7_sophie_1_7_7 408.5–413.5 s | 16.5 / 8.5 | 16 / 6 | head at limit 27%; outlier knee max (z +5.2); right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t42-48_shift` | B | 7_sophie_1_7_7 42.5–48.4 s | 14.8 / 8.3 | 15 / 7 | head at limit 6%; elbow bend at limit 11% |
| `sophie_1_7_7_t430-436` | A | 7_sophie_1_7_7 429.9–436.5 s | 2.5 / 2.2 | 23 / 13 | right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t439-444_shift` | B | 7_sophie_1_7_7 439.3–443.8 s | 16.3 / 8.5 | 19 / 8 | right arm behind body 7 cm (human's in front) |
| `sophie_1_7_7_t442-455` | A | 7_sophie_1_7_7 441.8–455.1 s | 6.7 / 3.7 | 15 / 6 | right arm behind body 8 cm (human's in front) |
| `sophie_1_7_7_t453-458_shift` | B | 7_sophie_1_7_7 453.1–457.5 s | 9.5 / 7.9 | 13 / 6 | right arm behind body 8 cm (human's in front) |
| `sophie_1_7_7_t456-463` | A | 7_sophie_1_7_7 455.5–463.0 s | 0.9 / 0.9 | 20 / 5 | right arm behind body 7 cm (human's in front) |
| `sophie_1_7_7_t46-58` | A | 7_sophie_1_7_7 46.4–57.9 s | 2.6 / 1.0 | 17 / 7 | elbow bend at limit 24% |
| `sophie_1_7_7_t461-467_shift` | B | 7_sophie_1_7_7 461.0–466.9 s | 19.1 / 10.9 | 20 / 6 | elbow bend at limit 14%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t465-475` | A | 7_sophie_1_7_7 464.9–475.2 s | 2.5 / 0.6 | 17 / 8 | elbow bend at limit 8%; right arm behind body 7 cm (human's in front) |
| `sophie_1_7_7_t475-486` | A | 7_sophie_1_7_7 475.2–485.5 s | 1.6 / 1.1 | 13 / 5 | right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t482-486_shift` | B | 7_sophie_1_7_7 482.5–486.5 s | 15.3 / 8.1 | 7 / 3 | elbow bend at limit 8% |
| `sophie_1_7_7_t506-510_shift` | B | 7_sophie_1_7_7 505.5–510.3 s | 11.5 / 4.6 | 17 / 6 | head at limit 6%; elbow bend at limit 29%; right arm behind body 7 cm (human's in front) |
| `sophie_1_7_7_t508-524` | A | 7_sophie_1_7_7 508.3–524.5 s | 5.5 / 2.2 | 18 / 7 | elbow bend at limit 27%; right arm behind body 7 cm (human's in front) |
| `sophie_1_7_7_t524-541` | A | 7_sophie_1_7_7 524.5–540.6 s | 1.9 / 0.8 | 15 / 5 | right arm behind body 7 cm (human's in front) |
| `sophie_1_7_7_t541-557` | A | 7_sophie_1_7_7 541.2–557.5 s | 1.3 / 1.1 | 26 / 10 | elbow bend at limit 6%; right arm behind body 7 cm (human's in front) |
| `sophie_1_7_7_t56-62_shift` | B | 7_sophie_1_7_7 55.9–61.9 s | 26.3 / 11.4 | 13 / 5 | human steps |
| `sophie_1_7_7_t561-578` | A | 7_sophie_1_7_7 561.4–578.0 s | 8.2 / 4.2 | 17 / 6 | elbow bend at limit 22% |
| `sophie_1_7_7_t578-595` | A | 7_sophie_1_7_7 578.0–594.6 s | 5.7 / 2.2 | 25 / 9 | elbow bend at limit 15%; right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t593-597_shift` | B | 7_sophie_1_7_7 592.6–597.2 s | 12.9 / 8.6 | 31 / 9 | right arm behind body 6 cm (human's in front) |
| `sophie_1_7_7_t595-600` | A | 7_sophie_1_7_7 595.2–599.8 s | 1.6 / 0.6 | 28 / 9 | right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t60-78` | A | 7_sophie_1_7_7 59.9–78.1 s | 1.7 / 0.7 | 13 / 5 | elbow bend at limit 24%; right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t78-96` | A | 7_sophie_1_7_7 78.1–96.2 s | 7.0 / 1.5 | 17 / 7 | head at limit 6%; elbow bend at limit 31% |
| `sophie_1_7_7_t94-101_shift` | B | 7_sophie_1_7_7 94.2–100.7 s | 16.4 / 9.4 | 17 / 7 | head at limit 20%; elbow bend at limit 10%; right arm behind body 5 cm (human's in front) |
| `sophie_1_7_7_t99-117` | A | 7_sophie_1_7_7 98.7–116.9 s | 9.6 / 2.9 | 23 / 7 | head at limit 6%; elbow bend at limit 13%; outlier knee max (z +4.4); right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t0-4` | A | 7_sophie_1_8_8 0.0–4.5 s | 0.7 / 0.8 | 21 / 7 | right arm behind body 7 cm (human's in front) |
| `sophie_1_8_8_t102-109` | A | 7_sophie_1_8_8 102.0–109.1 s | 9.7 / 2.6 | 25 / 7 | elbow bend at limit 42%; right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t107-112_shift` | B | 7_sophie_1_8_8 107.1–111.6 s | 6.3 / 2.8 | 16 / 5 | elbow bend at limit 32%; right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t126-132` | A | 7_sophie_1_8_8 125.8–131.9 s | 1.2 / 1.8 | 15 / 6 | elbow bend at limit 10% |
| `sophie_1_8_8_t136-149` | A | 7_sophie_1_8_8 136.4–148.5 s | 2.8 / 1.8 | 20 / 7 | elbow bend at limit 17%; right arm behind body 7 cm (human's in front) |
| `sophie_1_8_8_t153-163` | A | 7_sophie_1_8_8 152.7–162.8 s | 1.4 / 0.6 | 23 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t173-182` | A | 7_sophie_1_8_8 173.4–182.3 s | 1.3 / 1.2 | 24 / 8 | right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t18-22_shift` | B | 7_sophie_1_8_8 18.0–22.5 s | 13.5 / 8.8 | 18 / 6 | outlier knee max (z +5.0); right arm behind body 8 cm (human's in front) |
| `sophie_1_8_8_t183-187` | A | 7_sophie_1_8_8 183.0–187.4 s | 3.3 / 3.1 | 28 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t185-190_shift` | B | 7_sophie_1_8_8 185.4–190.0 s | 14.0 / 9.9 | 30 / 7 | elbow bend at limit 23%; outlier knee max (z +4.9); right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t188-193` | A | 7_sophie_1_8_8 188.0–192.7 s | 1.8 / 0.5 | 27 / 8 | elbow bend at limit 27%; right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t191-195_shift` | B | 7_sophie_1_8_8 190.7–195.3 s | 13.9 / 8.8 | 13 / 4 | outlier knee max (z +4.9) |
| `sophie_1_8_8_t193-203` | A | 7_sophie_1_8_8 193.3–202.9 s | 1.5 / 1.2 | 19 / 7 | elbow bend at limit 20% |
| `sophie_1_8_8_t20-40` | A | 7_sophie_1_8_8 20.5–40.4 s | 3.2 / 0.9 | 22 / 7 | elbow bend at limit 14%; right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t216-229` | A | 7_sophie_1_8_8 215.6–228.8 s | 2.0 / 1.7 | 18 / 5 | elbow bend at limit 27% |
| `sophie_1_8_8_t229-237` | A | 7_sophie_1_8_8 229.4–236.9 s | 3.2 / 2.0 | 27 / 7 | right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t238-252` | A | 7_sophie_1_8_8 237.6–252.4 s | 9.2 / 2.2 | 21 / 6 | outlier knee max (z +3.5) |
| `sophie_1_8_8_t257-261` | A | 7_sophie_1_8_8 257.0–261.1 s | 2.6 / 3.6 | 18 / 4 | elbow bend at limit 6% |
| `sophie_1_8_8_t262-268` | A | 7_sophie_1_8_8 261.7–267.9 s | 3.8 / 0.7 | 21 / 7 | elbow bend at limit 46%; right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t266-270_shift` | B | 7_sophie_1_8_8 265.9–270.5 s | 13.4 / 6.6 | 20 / 8 | elbow bend at limit 55%; outlier knee max (z +6.4); right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t268-288` | A | 7_sophie_1_8_8 268.5–288.4 s | 2.4 / 1.1 | 20 / 7 | elbow bend at limit 17%; right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t302-306_shift` | B | 7_sophie_1_8_8 301.9–306.4 s | 10.6 / 7.9 | 13 / 5 | right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t308-313_shift` | B | 7_sophie_1_8_8 308.4–313.0 s | 19.1 / 10.8 | 14 / 6 | knee 63 deg; outlier knee max (z +8.9) |
| `sophie_1_8_8_t311-316` | A | 7_sophie_1_8_8 311.0–315.5 s | 5.0 / 2.1 | 18 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t314-318_shift` | B | 7_sophie_1_8_8 313.5–318.3 s | 21.1 / 15.8 | 24 / 7 | knee 60 deg; outlier knee max (z +8.1); right arm behind body 7 cm (human's in front) |
| `sophie_1_8_8_t316-323` | A | 7_sophie_1_8_8 316.3–322.9 s | 1.7 / 0.3 | 35 / 10 | elbow bend at limit 20%; right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t321-326_shift` | B | 7_sophie_1_8_8 320.9–325.8 s | 19.2 / 11.1 | 27 / 7 | outlier knee max (z +4.9) |
| `sophie_1_8_8_t326-342` | A | 7_sophie_1_8_8 326.3–341.7 s | 1.1 / 0.7 | 22 / 9 | right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t342-357` | A | 7_sophie_1_8_8 341.7–357.1 s | 1.3 / 1.3 | 15 / 6 | right arm behind body 7 cm (human's in front) |
| `sophie_1_8_8_t363-380` | A | 7_sophie_1_8_8 363.4–379.9 s | 1.2 / 1.6 | 14 / 6 | elbow bend at limit 10% |
| `sophie_1_8_8_t380-385_shift` | B | 7_sophie_1_8_8 380.4–384.7 s | 21.1 / 12.1 | 17 / 8 | right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t383-395` | A | 7_sophie_1_8_8 382.7–395.1 s | 2.2 / 1.8 | 13 / 6 | elbow bend at limit 6%; right arm behind body 7 cm (human's in front) |
| `sophie_1_8_8_t41-47` | A | 7_sophie_1_8_8 41.1–47.0 s | 4.3 / 3.6 | 18 / 7 | head at limit 8%; right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t410-417` | A | 7_sophie_1_8_8 409.8–416.6 s | 1.5 / 1.3 | 15 / 6 | right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t417-429` | A | 7_sophie_1_8_8 417.2–429.1 s | 8.7 / 4.1 | 12 / 4 | elbow bend at limit 42%; right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t466-472` | A | 7_sophie_1_8_8 465.8–472.4 s | 2.1 / 0.5 | 22 / 8 | elbow bend at limit 5% |
| `sophie_1_8_8_t473-488` | A | 7_sophie_1_8_8 473.1–488.4 s | 1.5 / 1.2 | 18 / 6 | elbow bend at limit 7% |
| `sophie_1_8_8_t5-20` | A | 7_sophie_1_8_8 5.0–20.0 s | 8.7 / 3.2 | 17 / 5 | head at limit 10%; elbow bend at limit 21%; outlier knee max (z +7.0); right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t508-523` | A | 7_sophie_1_8_8 507.5–522.5 s | 2.3 / 0.9 | 25 / 8 | right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t542-546` | A | 7_sophie_1_8_8 541.5–546.4 s | 1.3 / 0.7 | 15 / 5 | elbow bend at limit 51% |
| `sophie_1_8_8_t544-549_shift` | B | 7_sophie_1_8_8 544.4–548.8 s | 7.6 / 4.3 | 12 / 4 | elbow bend at limit 68% |
| `sophie_1_8_8_t547-564` | A | 7_sophie_1_8_8 546.8–564.2 s | 3.3 / 0.6 | 12 / 5 | elbow bend at limit 14%; right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t562-567_shift` | B | 7_sophie_1_8_8 562.2–566.6 s | 7.6 / 4.6 | 11 / 4 | elbow bend at limit 12%; right arm behind body 7 cm (human's in front) |
| `sophie_1_8_8_t565-577` | A | 7_sophie_1_8_8 564.6–577.3 s | 10.0 / 5.3 | 17 / 6 | outlier knee max (z +7.9); right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t577-581` | A | 7_sophie_1_8_8 577.3–581.4 s | 2.0 / 0.8 | 8 / 3 | head at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t579-584_shift` | B | 7_sophie_1_8_8 579.4–584.4 s | 13.0 / 5.4 | 14 / 7 | elbow bend at limit 47%; outlier knee max (z +6.1) |
| `sophie_1_8_8_t582-596` | A | 7_sophie_1_8_8 582.4–596.5 s | 2.1 / 0.7 | 18 / 7 | elbow bend at limit 15%; right arm behind body 5 cm (human's in front) |
| `sophie_1_8_8_t597-601` | A | 7_sophie_1_8_8 597.0–601.1 s | 1.1 / 1.4 | 7 / 3 | elbow bend at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_8_8_t602-607_shift` | B | 7_sophie_1_8_8 601.7–607.1 s | 20.5 / 10.6 | 18 / 6 | elbow bend at limit 7%; outlier knee max (z +4.2) |
| `sophie_1_8_8_t65-82` | A | 7_sophie_1_8_8 65.0–81.8 s | 5.4 / 2.4 | 18 / 7 | right arm behind body 7 cm (human's in front) |
| `sophie_1_8_8_t80-84_shift` | B | 7_sophie_1_8_8 79.8–84.3 s | 13.0 / 6.7 | 19 / 8 | outlier knee max (z +5.2); right arm behind body 7 cm (human's in front) |
| `sophie_1_8_8_t82-90` | A | 7_sophie_1_8_8 82.3–90.3 s | 8.3 / 2.1 | 26 / 10 | elbow bend at limit 8% |
| `sophie_1_8_8_t91-102` | A | 7_sophie_1_8_8 91.1–101.5 s | 0.9 / 1.5 | 17 / 5 | elbow bend at limit 16%; right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t105-112` | A | 7_sophie_1_9_9 104.6–111.9 s | 9.3 / 1.6 | 14 / 4 | elbow bend at limit 68% |
| `sophie_1_9_9_t110-114_shift` | B | 7_sophie_1_9_9 109.9–114.4 s | 12.3 / 7.8 | 24 / 8 | elbow bend at limit 49%; outlier knee max (z +4.2) |
| `sophie_1_9_9_t112-129` | A | 7_sophie_1_9_9 112.4–129.5 s | 1.6 / 1.2 | 20 / 8 | elbow bend at limit 19% |
| `sophie_1_9_9_t129-147` | A | 7_sophie_1_9_9 129.5–146.6 s | 1.8 / 0.6 | 15 / 6 | elbow bend at limit 18% |
| `sophie_1_9_9_t145-149_shift` | B | 7_sophie_1_9_9 144.6–148.9 s | 10.3 / 6.0 | 21 / 10 | right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t147-156` | A | 7_sophie_1_9_9 146.9–156.0 s | 8.7 / 4.5 | 16 / 7 | elbow bend at limit 28%; right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t154-159_shift` | B | 7_sophie_1_9_9 154.0–159.2 s | 11.4 / 7.2 | 14 / 6 | elbow bend at limit 69%; right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t157-164` | A | 7_sophie_1_9_9 157.2–164.3 s | 2.0 / 1.6 | 19 / 9 | elbow bend at limit 34% |
| `sophie_1_9_9_t162-167_shift` | B | 7_sophie_1_9_9 162.3–166.8 s | 12.7 / 9.0 | 11 / 5 | elbow bend at limit 6%; outlier knee max (z +4.6); right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t165-177` | A | 7_sophie_1_9_9 164.8–176.7 s | 0.9 / 1.2 | 9 / 3 | elbow bend at limit 7%; right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t173-177_shift` | B | 7_sophie_1_9_9 173.4–177.4 s | 43.4 / 24.6 | 14 / 4 | human steps; K1 feet move 25 cm; outlier knee max (z +6.0); right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t180-184_shift` | B | 7_sophie_1_9_9 179.7–183.7 s | 24.9 / 13.4 | 5 / 2 | outlier knee max (z +5.1) |
| `sophie_1_9_9_t186-191_shift` | B | 7_sophie_1_9_9 186.5–191.1 s | 16.6 / 8.1 | 6 / 3 | outlier knee max (z +5.6) |
| `sophie_1_9_9_t19-35` | A | 7_sophie_1_9_9 19.0–35.0 s | 4.9 / 3.3 | 10 / 4 | elbow bend at limit 32% |
| `sophie_1_9_9_t193-198_shift` | B | 7_sophie_1_9_9 193.4–197.9 s | 10.8 / 7.1 | 16 / 6 | elbow bend at limit 39%; right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t196-212` | A | 7_sophie_1_9_9 195.9–212.4 s | 3.8 / 1.9 | 11 / 5 | elbow bend at limit 63% |
| `sophie_1_9_9_t210-215_shift` | B | 7_sophie_1_9_9 210.4–214.9 s | 13.2 / 7.5 | 20 / 7 | elbow bend at limit 19%; outlier knee max (z +4.2); right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t213-219` | A | 7_sophie_1_9_9 212.9–219.2 s | 2.2 / 0.6 | 16 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t220-226` | A | 7_sophie_1_9_9 220.0–225.5 s | 0.9 / 0.7 | 25 / 7 | elbow bend at limit 6%; right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t231-246` | A | 7_sophie_1_9_9 230.6–245.7 s | 7.4 / 4.1 | 10 / 4 | elbow bend at limit 9% |
| `sophie_1_9_9_t246-261` | A | 7_sophie_1_9_9 245.7–260.9 s | 1.8 / 1.0 | 18 / 7 | elbow bend at limit 25% |
| `sophie_1_9_9_t262-278` | A | 7_sophie_1_9_9 262.3–277.9 s | 1.4 / 1.7 | 20 / 6 | elbow bend at limit 21% |
| `sophie_1_9_9_t276-280_shift` | B | 7_sophie_1_9_9 275.9–280.5 s | 27.3 / 16.3 | 6 / 2 | human steps; outlier knee max (z +6.1) |
| `sophie_1_9_9_t290-303` | A | 7_sophie_1_9_9 289.5–303.3 s | 1.2 / 1.2 | 12 / 4 | elbow bend at limit 13%; right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t3-18` | A | 7_sophie_1_9_9 3.2–18.5 s | 6.6 / 4.5 | 13 / 5 | elbow bend at limit 9% |
| `sophie_1_9_9_t304-309` | A | 7_sophie_1_9_9 304.0–309.4 s | 1.9 / 1.5 | 16 / 7 | elbow bend at limit 30%; right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t307-312_shift` | B | 7_sophie_1_9_9 307.4–312.0 s | 15.1 / 10.5 | 15 / 6 | outlier knee max (z +3.9); right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t325-329_shift` | B | 7_sophie_1_9_9 324.7–329.2 s | 12.9 / 7.7 | 23 / 7 | outlier knee max (z +4.0); right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t327-334` | A | 7_sophie_1_9_9 327.2–333.6 s | 1.3 / 1.6 | 20 / 7 | elbow bend at limit 9%; right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t332-336_shift` | B | 7_sophie_1_9_9 331.6–336.1 s | 14.8 / 8.8 | 18 / 6 | right arm behind body 6 cm (human's in front) |
| `sophie_1_9_9_t334-344` | A | 7_sophie_1_9_9 334.1–343.5 s | 3.6 / 2.2 | 18 / 6 | right arm behind body 7 cm (human's in front) |
| `sophie_1_9_9_t344-351` | A | 7_sophie_1_9_9 344.4–351.4 s | 1.8 / 1.1 | 16 / 5 | elbow bend at limit 17% |
| `sophie_1_9_9_t35-51` | A | 7_sophie_1_9_9 35.0–50.9 s | 1.2 / 1.2 | 15 / 5 | elbow bend at limit 7% |
| `sophie_1_9_9_t356-366` | A | 7_sophie_1_9_9 356.4–365.5 s | 5.0 / 1.3 | 25 / 8 | elbow bend at limit 8% |
| `sophie_1_9_9_t386-396` | A | 7_sophie_1_9_9 385.5–395.7 s | 4.7 / 2.0 | 15 / 5 | elbow bend at limit 8% |
| `sophie_1_9_9_t406-416` | A | 7_sophie_1_9_9 406.0–416.5 s | 7.0 / 2.1 | 14 / 5 | elbow bend at limit 16% |
| `sophie_1_9_9_t417-431` | A | 7_sophie_1_9_9 417.1–430.8 s | 1.9 / 1.8 | 16 / 6 | elbow bend at limit 36% |
| `sophie_1_9_9_t436-441_shift` | B | 7_sophie_1_9_9 436.5–440.9 s | 6.3 / 2.7 | 23 / 9 | outlier knee max (z +6.3) |
| `sophie_1_9_9_t439-449` | A | 7_sophie_1_9_9 438.9–449.3 s | 6.4 / 5.7 | 23 / 9 | knee 62 deg; outlier knee max (z +8.9); right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t450-456` | A | 7_sophie_1_9_9 450.0–456.4 s | 1.4 / 1.1 | 21 / 7 | elbow bend at limit 7% |
| `sophie_1_9_9_t463-475` | A | 7_sophie_1_9_9 462.5–475.0 s | 1.9 / 1.5 | 14 / 5 | elbow bend at limit 8% |
| `sophie_1_9_9_t490-498` | A | 7_sophie_1_9_9 490.0–497.7 s | 2.5 / 1.1 | 27 / 7 | head at limit 8%; elbow bend at limit 32% |
| `sophie_1_9_9_t498-508` | A | 7_sophie_1_9_9 498.4–507.8 s | 1.8 / 0.8 | 14 / 5 | elbow bend at limit 16%; right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t508-513` | A | 7_sophie_1_9_9 508.5–512.7 s | 2.9 / 1.4 | 24 / 6 | elbow bend at limit 9%; right arm behind body 5 cm (human's in front) |
| `sophie_1_9_9_t51-67` | A | 7_sophie_1_9_9 50.9–66.9 s | 1.4 / 1.7 | 9 / 4 | elbow bend at limit 21% |
| `sophie_1_9_9_t514-523` | A | 7_sophie_1_9_9 513.6–522.6 s | 4.4 / 1.3 | 24 / 9 | elbow bend at limit 19% |
| `sophie_1_9_9_t521-525_shift` | B | 7_sophie_1_9_9 520.6–525.1 s | 14.8 / 9.2 | 21 / 7 | knee 62 deg; outlier knee max (z +8.7) |
| `sophie_1_9_9_t533-539` | A | 7_sophie_1_9_9 533.1–539.0 s | 3.5 / 0.9 | 28 / 7 | elbow bend at limit 22% |
| `sophie_1_9_9_t537-541_shift` | B | 7_sophie_1_9_9 537.0–541.4 s | 15.7 / 9.3 | 26 / 8 | elbow bend at limit 15%; outlier knee max (z +5.3) |
| `sophie_1_9_9_t539-545` | A | 7_sophie_1_9_9 539.4–545.2 s | 2.7 / 0.7 | 31 / 10 | elbow bend at limit 48% |
| `sophie_1_9_9_t546-564` | A | 7_sophie_1_9_9 546.0–564.5 s | 1.6 / 1.1 | 12 / 3 | head at limit 71% |
| `sophie_1_9_9_t572-579_shift` | B | 7_sophie_1_9_9 571.6–579.1 s | 8.6 / 6.3 | 25 / 9 | elbow bend at limit 39%; outlier knee max (z +4.3) |
| `sophie_1_9_9_t577-585` | A | 7_sophie_1_9_9 577.1–584.6 s | 1.9 / 0.6 | 14 / 5 | head at limit 47%; elbow bend at limit 28% |
| `sophie_1_9_9_t582-586_shift` | B | 7_sophie_1_9_9 581.6–585.6 s | 12.4 / 7.1 | 12 / 4 | head at limit 88%; elbow bend at limit 10% |
| `sophie_1_9_9_t586-600` | A | 7_sophie_1_9_9 586.2–599.8 s | 3.3 / 2.5 | 22 / 6 | head at limit 9% |
| `sophie_1_9_9_t67-83` | A | 7_sophie_1_9_9 66.9–82.8 s | 3.2 / 1.8 | 9 / 4 | elbow bend at limit 28% |
| `sophie_1_9_9_t81-85_shift` | B | 7_sophie_1_9_9 80.8–85.3 s | 11.8 / 6.7 | 10 / 4 | elbow bend at limit 31%; outlier knee max (z +3.7) |
| `sophie_1_9_9_t83-91` | A | 7_sophie_1_9_9 83.3–90.6 s | 2.0 / 0.4 | 19 / 5 | elbow bend at limit 48% |
| `sophie_1_9_9_t89-93_shift` | B | 7_sophie_1_9_9 88.6–93.2 s | 17.6 / 10.0 | 12 / 4 | elbow bend at limit 9%; outlier knee max (z +5.8) |
| `sophie_1_9_9_t91-104` | A | 7_sophie_1_9_9 91.2–104.1 s | 1.0 / 1.6 | 10 / 5 | elbow bend at limit 43% |
| `stewart_0_111_111_t30-34_shift` | B | 5_stewart_0_111_111 29.9–34.3 s | 12.7 / 7.1 | 7 / 3 | outlier knee max (z +4.0) |
| `stewart_0_111_111_t41-51_shift` | B | 5_stewart_0_111_111 41.2–50.9 s | 21.3 / 13.0 | 35 / 9 | outlier knee max (z +7.6) |
| `stewart_0_111_111_t55-65_shift` | B | 5_stewart_0_111_111 55.0–64.8 s | 29.5 / 17.5 | 16 / 5 | human steps; outlier knee max (z +4.2) |
| `stewart_0_15_15_t72-78_shift` | B | 5_stewart_0_15_15 71.6–77.8 s | 17.2 / 10.2 | 12 / 4 | outlier knee max (z +3.5) |
| `stewart_0_65_65_t13-17_shift` | B | 5_stewart_0_65_65 13.0–17.2 s | 14.8 / 8.2 | 34 / 9 | outlier knee max (z +4.1) |
| `stewart_0_73_73_t7-12_shift` | B | 5_stewart_0_73_73 7.2–12.2 s | 18.1 / 10.1 | 24 / 6 | outlier knee max (z +6.3) |
| `stewart_0_87_87_t34-39_shift` | B | 5_stewart_0_87_87 34.5–38.5 s | 10.8 / 7.5 | 52 / 12 | outlier trunk drop (z +4.0); outlier knee max (z +6.5) |
| `stewart_0_95_95_t9-20` | A | 5_stewart_0_95_95 8.8–19.7 s | 2.6 / 0.7 | 42 / 11 | outlier knee max (z +4.2) |
| `stewart_1_1_1_t155-159_shift` | B | 5_stewart_1_1_1 155.0–159.5 s | 13.4 / 8.0 | 9 / 3 | outlier knee max (z +3.8) |
| `stewart_1_2_2_t10-24` | A | 5_stewart_1_2_2 9.6–24.4 s | 5.1 / 2.4 | 2 / 1 | hand presses into leg 24 mm for 14.8 s (at 0.0 s) |
| `stewart_1_2_2_t22-28_shift` | B | 5_stewart_1_2_2 22.4–28.0 s | 15.8 / 9.3 | 2 / 1 | hand presses into leg 25 mm for 5.6 s (at 0.0 s) |
| `stewart_1_2_2_t26-44` | A | 5_stewart_1_2_2 26.0–43.8 s | 0.7 / 0.3 | 9 / 2 | hand presses into leg 26 mm for 9.6 s (at 0.0 s) |
| `stewart_1_2_2_t378-397` | A | 5_stewart_1_2_2 377.8–397.0 s | 0.3 / 0.3 | 12 / 4 | outlier knee max (z -3.9) |
| `stewart_1_2_2_t397-416` | A | 5_stewart_1_2_2 397.0–416.3 s | 0.2 / 0.3 | 10 / 3 | outlier knee max (z -4.0) |
| `tiffnay_0_104_104_t7-11_shift` | B | 28_tiffnay_0_104_104 7.4–11.4 s | 21.0 / 11.1 | 12 / 4 | outlier knee max (z +4.1) |
| `tiffnay_0_10_10_t9-13_shift` | B | 28_tiffnay_0_10_10 8.7–13.3 s | 13.0 / 6.7 | 7 / 4 | outlier knee max (z +4.3) |
| `tiffnay_0_11_11_t13-19_shift` | B | 28_tiffnay_0_11_11 12.8–18.6 s | 23.5 / 12.8 | 6 / 3 | outlier knee max (z +3.6) |
| `tiffnay_0_1_1_t0-18` | A | 28_tiffnay_0_1_1 0.0–18.3 s | 0.7 / 0.4 | 8 / 4 | outlier knee max (z -3.8) |
| `tiffnay_0_66_66_t0-19` | A | 28_tiffnay_0_66_66 0.0–18.9 s | 3.4 / 1.3 | 9 / 4 | head at limit 7% |
| `tiffnay_0_6_6_t72-83_shift` | B | 28_tiffnay_0_6_6 71.9–82.8 s | 24.5 / 11.9 | 13 / 5 | outlier knee max (z +5.0) |
| `tiffnay_0_82_82_t23-27_shift` | B | 28_tiffnay_0_82_82 22.6–27.1 s | 13.9 / 8.3 | 9 / 4 | outlier knee max (z +4.1) |
| `tiffnay_0_95_95_t25-29_shift` | B | 28_tiffnay_0_95_95 24.6–29.1 s | 7.6 / 4.7 | 6 / 2 | outlier knee max (z +4.6) |
| `tiffnay_0_96_96_t9-15_shift` | B | 28_tiffnay_0_96_96 9.4–14.7 s | 23.0 / 12.1 | 17 / 6 | knee 64 deg; outlier knee max (z +9.5) |
| `tiffnay_0_9_9_t50-57` | A | 28_tiffnay_0_9_9 50.0–56.7 s | 1.5 / 0.7 | 7 / 4 | outlier knee max (z +4.5) |
| `tiffnay_0_9_9_t55-59_shift` | B | 28_tiffnay_0_9_9 54.7–59.3 s | 12.9 / 6.0 | 13 / 5 | outlier knee max (z +3.5) |
| `tiffnay_1_1_1_t125-142` | A | 28_tiffnay_1_1_1 124.9–142.3 s | 0.8 / 0.4 | 7 / 5 | elbow bend at limit 64% |
| `tiffnay_1_1_1_t142-160` | A | 28_tiffnay_1_1_1 142.3–159.6 s | 1.6 / 0.4 | 5 / 3 | elbow bend at limit 9% |
| `tiffnay_1_1_1_t182-190_shift` | B | 28_tiffnay_1_1_1 182.5–190.2 s | 16.6 / 6.2 | 5 / 3 | outlier knee max (z +5.8) |
| `tiffnay_1_1_1_t332-338_shift` | B | 28_tiffnay_1_1_1 332.1–338.0 s | 15.3 / 7.5 | 12 / 5 | outlier knee max (z +7.3) |
| `tiffnay_1_1_1_t343-348_shift` | B | 28_tiffnay_1_1_1 343.4–347.9 s | 11.3 / 6.9 | 10 / 5 | outlier knee max (z +4.2) |
| `tiffnay_1_1_1_t346-361` | A | 28_tiffnay_1_1_1 345.9–360.8 s | 1.7 / 0.5 | 15 / 7 | elbow bend at limit 10% |
| `tiffnay_1_1_1_t390-395_shift` | B | 28_tiffnay_1_1_1 390.3–394.6 s | 12.8 / 6.8 | 21 / 5 | outlier knee max (z +5.1) |
| `tiffnay_1_1_1_t496-514` | A | 28_tiffnay_1_1_1 496.2–513.5 s | 1.0 / 0.5 | 13 / 4 | hand presses into leg 55 mm for 1.6 s (at 7.4 s) |
| `tiffnay_1_1_1_t87-92_shift` | B | 28_tiffnay_1_1_1 86.9–92.2 s | 18.2 / 14.4 | 5 / 2 | outlier knee max (z +5.0) |
| `tiffnay_1_2_2_t169-175_shift` | B | 28_tiffnay_1_2_2 168.9–175.1 s | 17.6 / 8.2 | 6 / 3 | outlier knee max (z +7.8) |
| `tiffnay_1_2_2_t209-216_shift` | B | 28_tiffnay_1_2_2 208.8–215.6 s | 22.2 / 11.2 | 6 / 3 | outlier knee max (z +3.6) |
| `tiffnay_1_2_2_t292-299_shift` | B | 28_tiffnay_1_2_2 292.1–299.0 s | 21.2 / 11.5 | 13 / 6 | outlier knee max (z +6.3) |
| `tiffnay_1_2_2_t336-355` | A | 28_tiffnay_1_2_2 335.8–355.2 s | 4.8 / 2.2 | 9 / 4 | elbow bend at limit 9% |
| `tiffnay_1_2_2_t567-572_shift` | B | 28_tiffnay_1_2_2 566.7–571.9 s | 24.4 / 17.3 | 5 / 3 | knee 76 deg; outlier knee max (z +13.4) |
| `tiffnay_1_3_3_t105-120` | A | 28_tiffnay_1_3_3 104.5–119.7 s | 1.8 / 0.5 | 13 / 7 | elbow bend at limit 26% |
| `tiffnay_1_3_3_t148-153_shift` | B | 28_tiffnay_1_3_3 148.1–152.6 s | 11.9 / 5.2 | 4 / 1 | outlier knee max (z +5.0) |
| `tiffnay_1_3_3_t151-159` | A | 28_tiffnay_1_3_3 150.6–159.4 s | 1.3 / 1.1 | 8 / 4 | elbow bend at limit 26% |
| `tiffnay_1_3_3_t157-162_shift` | B | 28_tiffnay_1_3_3 157.4–162.0 s | 15.9 / 6.7 | 12 / 4 | elbow bend at limit 24%; outlier knee max (z +4.7) |
| `tiffnay_1_3_3_t200-219` | A | 28_tiffnay_1_3_3 199.6–219.4 s | 2.3 / 0.5 | 7 / 4 | elbow bend at limit 60% |
| `tiffnay_1_3_3_t239-257` | A | 28_tiffnay_1_3_3 238.7–256.8 s | 3.8 / 1.8 | 3 / 1 | outlier knee max (z +4.1) |
| `tiffnay_1_3_3_t3-23` | A | 28_tiffnay_1_3_3 2.8–22.7 s | 6.6 / 3.6 | 23 / 8 | elbow bend at limit 25% |
| `tiffnay_1_3_3_t317-336` | A | 28_tiffnay_1_3_3 316.7–336.4 s | 5.5 / 1.4 | 5 / 3 | leg at limit 5% |
| `tiffnay_1_3_3_t382-387_shift` | B | 28_tiffnay_1_3_3 381.6–386.7 s | 14.7 / 7.0 | 11 / 5 | outlier knee max (z +3.5) |
| `tiffnay_1_3_3_t454-474` | A | 28_tiffnay_1_3_3 454.3–474.0 s | 2.5 / 0.7 | 11 / 5 | elbow bend at limit 11% |
| `tiffnay_1_3_3_t514-532` | A | 28_tiffnay_1_3_3 514.0–531.6 s | 4.4 / 1.9 | 16 / 7 | elbow bend at limit 17% |
| `tiffnay_1_3_3_t530-535_shift` | B | 28_tiffnay_1_3_3 529.6–535.0 s | 23.8 / 11.6 | 34 / 12 | elbow bend at limit 16%; outlier knee max (z +6.2) |
| `tiffnay_1_3_3_t580-590` | A | 28_tiffnay_1_3_3 579.6–589.8 s | 3.1 / 1.1 | 16 / 7 | elbow bend at limit 12% |
| `wayne_0_100_100_t18-23_shift` | B | 1_wayne_0_100_100 18.4–22.9 s | 13.5 / 8.6 | 57 / 22 | outlier arms k1 cm (z +4.1); outlier knee max (z +3.8) |
| `wayne_0_100_100_t25-30_shift` | B | 1_wayne_0_100_100 25.0–29.6 s | 14.2 / 9.7 | 30 / 10 | outlier knee max (z +4.1) |
| `wayne_0_101_101_t25-33_shift` | B | 1_wayne_0_101_101 25.4–32.9 s | 17.1 / 10.4 | 29 / 12 | outlier knee max (z +6.9) |
| `wayne_0_101_101_t44-49_shift` | B | 1_wayne_0_101_101 44.1–48.6 s | 10.6 / 7.9 | 84 / 28 | outlier arms k1 cm (z +5.9) |
| `wayne_0_101_101_t47-51` | A | 1_wayne_0_101_101 46.6–51.4 s | 6.8 / 1.5 | 64 / 24 | outlier arms k1 cm (z +4.6) |
| `wayne_0_101_101_t8-14_shift` | B | 1_wayne_0_101_101 8.2–14.2 s | 10.6 / 7.4 | 31 / 13 | outlier knee max (z +3.5) |
| `wayne_0_103_103_t29-36_shift` | B | 1_wayne_0_103_103 29.0–35.9 s | 19.3 / 11.6 | 31 / 11 | outlier knee max (z +5.6) |
| `wayne_0_103_103_t49-54_shift` | B | 1_wayne_0_103_103 49.1–53.7 s | 17.1 / 10.1 | 19 / 7 | outlier knee max (z +6.4) |
| `wayne_0_104_104_t26-37_shift` | B | 1_wayne_0_104_104 26.5–37.3 s | 23.6 / 14.5 | 25 / 10 | outlier knee max (z +5.4) |
| `wayne_0_104_104_t9-19_shift` | B | 1_wayne_0_104_104 9.3–19.1 s | 20.5 / 11.5 | 27 / 11 | outlier knee max (z +6.7) |
| `wayne_0_105_105_t26-30_shift` | B | 1_wayne_0_105_105 25.6–29.6 s | 24.7 / 14.7 | 11 / 4 | outlier knee max (z +5.4) |
| `wayne_0_106_106_t17-24_shift` | B | 1_wayne_0_106_106 16.7–23.7 s | 22.1 / 13.6 | 43 / 15 | outlier knee max (z +5.0) |
| `wayne_0_107_107_t22-30_shift` | B | 1_wayne_0_107_107 22.4–30.2 s | 27.6 / 15.7 | 30 / 12 | human steps; outlier knee max (z +5.6) |
| `wayne_0_107_107_t31-35_shift` | B | 1_wayne_0_107_107 30.5–35.3 s | 24.1 / 14.8 | 21 / 8 | outlier knee max (z +4.0) |
| `wayne_0_108_108_t49-54_shift` | B | 1_wayne_0_108_108 49.1–53.8 s | 17.1 / 11.8 | 44 / 11 | outlier knee max (z +5.8) |
| `wayne_0_109_109_t11-20` | A | 1_wayne_0_109_109 10.6–20.0 s | 7.1 / 1.7 | 46 / 20 | outlier arms k1 cm (z +3.7) |
| `wayne_0_109_109_t8-13_shift` | B | 1_wayne_0_109_109 8.1–12.6 s | 9.2 / 6.5 | 36 / 20 | outlier arms k1 cm (z +3.5) |
| `wayne_0_110_110_t41-45_shift` | B | 1_wayne_0_110_110 40.8–44.8 s | 22.9 / 12.8 | 42 / 11 | outlier knee max (z +3.6) |
| `wayne_0_111_111_t13-17_shift` | B | 1_wayne_0_111_111 12.6–17.0 s | 12.4 / 8.2 | 38 / 11 | outlier knee max (z +4.3) |
| `wayne_0_111_111_t27-39` | A | 1_wayne_0_111_111 26.9–38.7 s | 10.8 / 5.5 | 40 / 10 | human steps |
| `wayne_0_111_111_t45-49_shift` | B | 1_wayne_0_111_111 44.9–48.9 s | 26.1 / 18.4 | 49 / 13 | human steps; K1 feet move 18 cm; outlier knee max (z +5.2) |
| `wayne_0_111_111_t52-57_shift` | B | 1_wayne_0_111_111 52.3–56.9 s | 16.1 / 11.7 | 33 / 8 | outlier knee max (z +4.2) |
| `wayne_0_112_112_t41-46_shift` | B | 1_wayne_0_112_112 41.1–45.6 s | 15.3 / 10.3 | 32 / 10 | outlier knee max (z +5.2) |
| `wayne_0_112_112_t46-51_shift` | B | 1_wayne_0_112_112 45.9–50.6 s | 17.0 / 12.2 | 27 / 10 | outlier knee max (z +4.2) |
| `wayne_0_113_113_t26-31_shift` | B | 1_wayne_0_113_113 26.1–30.8 s | 23.1 / 16.2 | 50 / 17 | outlier knee max (z +5.6) |
| `wayne_0_113_113_t32-37_shift` | B | 1_wayne_0_113_113 32.4–37.0 s | 18.2 / 12.8 | 35 / 12 | outlier knee max (z +4.3) |
| `wayne_0_114_114_t31-44` | A | 1_wayne_0_114_114 31.1–44.5 s | 5.9 / 5.8 | 36 / 13 | hand presses into leg 22 mm for 0.3 s (at 11.9 s) |
| `wayne_0_115_115_t49-54_shift` | B | 1_wayne_0_115_115 49.3–53.8 s | 8.4 / 5.3 | 53 / 21 | shoulder at limit 7%; outlier arms k1 cm (z +3.8) |
| `wayne_0_116_116_t21-25_shift` | B | 1_wayne_0_116_116 20.7–25.3 s | 12.8 / 9.8 | 26 / 10 | outlier knee max (z +4.1) |
| `wayne_0_116_116_t27-31_shift` | B | 1_wayne_0_116_116 26.8–31.4 s | 17.9 / 14.1 | 33 / 10 | outlier knee max (z +4.0) |
| `wayne_0_116_116_t35-55` | A | 1_wayne_0_116_116 34.8–54.5 s | 2.8 / 0.9 | 54 / 16 | outlier knee max (z +3.5) |
| `wayne_0_116_116_t53-57_shift` | B | 1_wayne_0_116_116 52.5–57.0 s | 14.0 / 10.0 | 69 / 17 | outlier knee max (z +5.7) |
| `wayne_0_116_116_t62-66_shift` | B | 1_wayne_0_116_116 61.7–66.1 s | 13.5 / 9.0 | 56 / 14 | outlier knee max (z +4.5) |
| `wayne_0_116_116_t64-70` | A | 1_wayne_0_116_116 64.1–70.2 s | 0.8 / 0.5 | 64 / 20 | shoulder at limit 8%; outlier arms k1 cm (z +3.6) |
| `wayne_0_116_116_t67-71_shift` | B | 1_wayne_0_116_116 66.7–70.7 s | 28.7 / 18.8 | 68 / 23 | human steps; K1 feet move 19 cm; outlier arms k1 cm (z +4.5); outlier knee max (z +4.4) |
| `wayne_0_117_117_t22-27_shift` | B | 1_wayne_0_117_117 21.9–27.0 s | 17.5 / 11.7 | 33 / 10 | outlier knee max (z +4.2) |
| `wayne_0_118_118_t10-15_shift` | B | 1_wayne_0_118_118 10.4–14.9 s | 10.6 / 6.8 | 29 / 8 | outlier knee max (z +4.1) |
| `wayne_0_118_118_t17-22_shift` | B | 1_wayne_0_118_118 16.9–22.3 s | 31.5 / 22.3 | 38 / 13 | human steps; K1 feet move 22 cm; outlier knee max (z +5.3) |
| `wayne_0_118_118_t29-34_shift` | B | 1_wayne_0_118_118 28.7–34.5 s | 26.1 / 15.5 | 30 / 10 | human steps |
| `wayne_0_11_11_t35-44_shift` | B | 1_wayne_0_11_11 34.9–43.6 s | 21.1 / 12.2 | 13 / 5 | outlier knee max (z +3.9) |
| `wayne_0_12_12_t33-38_shift` | B | 1_wayne_0_12_12 32.7–38.3 s | 21.1 / 12.3 | 6 / 3 | outlier knee max (z +5.1) |
| `wayne_0_12_12_t60-64_shift` | B | 1_wayne_0_12_12 59.6–64.0 s | 9.4 / 7.4 | 14 / 5 | outlier knee max (z +5.6) |
| `wayne_0_13_13_t11-22` | A | 1_wayne_0_13_13 10.8–21.6 s | 0.9 / 0.3 | 8 / 3 | outlier knee max (z -4.8) |
| `wayne_0_14_14_t18-24_shift` | B | 1_wayne_0_14_14 18.1–23.6 s | 18.7 / 10.7 | 19 / 7 | outlier knee max (z +4.8) |
| `wayne_0_14_14_t38-44_shift` | B | 1_wayne_0_14_14 37.9–44.1 s | 24.4 / 15.2 | 8 / 4 | outlier knee max (z +4.7) |
| `wayne_0_14_14_t4-10_shift` | B | 1_wayne_0_14_14 3.7–9.6 s | 15.7 / 9.4 | 10 / 5 | outlier knee max (z +4.0) |
| `wayne_0_14_14_t64-73_shift` | B | 1_wayne_0_14_14 63.5–72.8 s | 21.9 / 10.0 | 13 / 5 | outlier knee max (z +5.1) |
| `wayne_0_15_15_t17-22_shift` | B | 1_wayne_0_15_15 17.4–21.9 s | 13.7 / 9.9 | 16 / 7 | outlier knee max (z +4.7) |
| `wayne_0_15_15_t23-29_shift` | B | 1_wayne_0_15_15 23.2–29.1 s | 37.6 / 21.6 | 14 / 8 | human steps; K1 feet move 22 cm; outlier knee max (z +5.8) |
| `wayne_0_15_15_t31-42_shift` | B | 1_wayne_0_15_15 31.4–41.5 s | 26.2 / 16.9 | 14 / 6 | human steps; knee 67 deg; outlier knee max (z +10.2) |
| `wayne_0_15_15_t52-58_shift` | B | 1_wayne_0_15_15 52.0–58.1 s | 13.9 / 8.4 | 15 / 7 | outlier knee max (z +4.3) |
| `wayne_0_16_16_t66-72_shift` | B | 1_wayne_0_16_16 66.3–71.8 s | 24.0 / 14.2 | 22 / 10 | outlier knee max (z +4.1) |
| `wayne_0_18_18_t38-49` | A | 1_wayne_0_18_18 37.8–49.2 s | 0.6 / 1.4 | 12 / 5 | leg at limit 6% |
| `wayne_0_1_1_t14-19_shift` | B | 1_wayne_0_1_1 14.2–18.9 s | 19.5 / 10.4 | 12 / 4 | outlier knee max (z +6.1) |
| `wayne_0_1_1_t21-27_shift` | B | 1_wayne_0_1_1 21.0–27.0 s | 24.3 / 12.9 | 14 / 6 | outlier knee max (z +6.9) |
| `wayne_0_1_1_t61-69_shift` | B | 1_wayne_0_1_1 61.2–68.8 s | 15.2 / 8.2 | 22 / 9 | outlier knee max (z +4.1) |
| `wayne_0_1_1_t8-13_shift` | B | 1_wayne_0_1_1 8.5–13.0 s | 13.0 / 9.3 | 13 / 4 | outlier knee max (z +4.6) |
| `wayne_0_2_2_t0-12_shift` | B | 1_wayne_0_2_2 0.0–12.2 s | 19.3 / 12.7 | 13 / 5 | outlier knee max (z +5.0) |
| `wayne_0_2_2_t36-40_shift` | B | 1_wayne_0_2_2 35.5–39.5 s | 31.8 / 16.0 | 5 / 2 | human steps; outlier knee max (z +5.4) |
| `wayne_0_2_2_t49-54_shift` | B | 1_wayne_0_2_2 49.0–53.5 s | 14.7 / 10.6 | 18 / 6 | outlier knee max (z +6.2) |
| `wayne_0_33_33_t61-66_shift` | B | 1_wayne_0_33_33 60.7–66.5 s | 13.0 / 9.1 | 10 / 4 | outlier knee max (z +4.3) |
| `wayne_0_34_34_t1-16` | A | 1_wayne_0_34_34 0.9–16.1 s | 10.0 / 7.5 | 23 / 10 | outlier knee max (z +5.3) |
| `wayne_0_34_34_t14-19_shift` | B | 1_wayne_0_34_34 14.1–18.6 s | 10.5 / 13.5 | 24 / 7 | outlier knee max (z +5.4) |
| `wayne_0_34_34_t37-42_shift` | B | 1_wayne_0_34_34 37.2–41.6 s | 8.9 / 10.6 | 22 / 7 | outlier knee max (z +3.7) |
| `wayne_0_35_35_t23-28_shift` | B | 1_wayne_0_35_35 23.1–27.6 s | 12.7 / 8.2 | 22 / 8 | outlier knee max (z +4.9) |
| `wayne_0_35_35_t5-14` | A | 1_wayne_0_35_35 4.8–13.9 s | 9.7 / 10.8 | 17 / 7 | K1 feet move 11 cm |
| `wayne_0_36_36_t0-12` | A | 1_wayne_0_36_36 0.0–11.8 s | 1.5 / 8.2 | 20 / 7 | K1 feet move 8 cm |
| `wayne_0_36_36_t12-24` | A | 1_wayne_0_36_36 12.2–23.8 s | 8.4 / 7.5 | 22 / 9 | outlier knee max (z +6.1) |
| `wayne_0_36_36_t22-28_shift` | B | 1_wayne_0_36_36 21.8–28.4 s | 14.1 / 8.6 | 23 / 9 | outlier knee max (z +4.2) |
| `wayne_0_37_37_t50-55` | A | 1_wayne_0_37_37 49.8–54.9 s | 3.7 / 2.4 | 34 / 14 | leg at limit 8% |
| `wayne_0_37_37_t53-57_shift` | B | 1_wayne_0_37_37 52.9–57.3 s | 11.9 / 9.9 | 46 / 17 | leg at limit 10%; outlier knee max (z +4.7) |
| `wayne_0_37_37_t61-68_shift` | B | 1_wayne_0_37_37 61.4–67.8 s | 24.1 / 14.0 | 17 / 5 | outlier knee max (z +3.7) |
| `wayne_0_38_38_t36-40_shift` | B | 1_wayne_0_38_38 35.8–40.2 s | 13.7 / 10.8 | 42 / 14 | outlier knee max (z +5.0) |
| `wayne_0_38_38_t40-45_shift` | B | 1_wayne_0_38_38 40.3–44.8 s | 15.3 / 11.1 | 29 / 9 | outlier knee max (z +6.4) |
| `wayne_0_38_38_t58-62_shift` | B | 1_wayne_0_38_38 57.8–61.8 s | 22.4 / 13.5 | 9 / 5 | outlier knee max (z +6.9) |
| `wayne_0_39_39_t26-34_shift` | B | 1_wayne_0_39_39 26.1–34.1 s | 14.1 / 8.5 | 28 / 10 | outlier knee max (z +4.1) |
| `wayne_0_39_39_t37-42_shift` | B | 1_wayne_0_39_39 37.4–42.1 s | 15.3 / 10.0 | 27 / 11 | leg at limit 11%; outlier knee max (z +5.6) |
| `wayne_0_3_3_t38-47_shift` | B | 1_wayne_0_3_3 38.3–47.4 s | 15.0 / 8.8 | 14 / 6 | outlier knee max (z +4.7) |
| `wayne_0_3_3_t49-54_shift` | B | 1_wayne_0_3_3 49.2–53.8 s | 12.3 / 8.3 | 27 / 10 | outlier knee max (z +3.5) |
| `wayne_0_40_40_t27-34_shift` | B | 1_wayne_0_40_40 26.9–33.9 s | 18.0 / 10.4 | 27 / 11 | outlier knee max (z +5.1) |
| `wayne_0_41_41_t34-51` | A | 1_wayne_0_41_41 33.8–50.8 s | 0.3 / 0.3 | 20 / 7 | outlier knee max (z -3.8) |
| `wayne_0_4_4_t67-72_shift` | B | 1_wayne_0_4_4 66.7–71.8 s | 16.5 / 9.7 | 8 / 3 | outlier knee max (z +5.2) |
| `wayne_0_56_56_t28-43` | A | 1_wayne_0_56_56 28.5–42.7 s | 11.2 / 3.3 | 32 / 11 | human steps |
| `wayne_0_58_58_t30-36_shift` | B | 1_wayne_0_58_58 30.3–35.8 s | 25.4 / 14.9 | 29 / 11 | human steps |
| `wayne_0_5_5_t24-36_shift` | B | 1_wayne_0_5_5 24.4–36.3 s | 13.5 / 9.0 | 19 / 8 | outlier knee max (z +4.0) |
| `wayne_0_5_5_t63-69_shift` | B | 1_wayne_0_5_5 62.7–68.8 s | 37.3 / 21.3 | 17 / 7 | human steps; K1 feet move 21 cm; outlier knee max (z +3.9) |
| `wayne_0_60_60_t26-30_shift` | B | 1_wayne_0_60_60 25.6–30.1 s | 13.6 / 8.5 | 35 / 12 | outlier knee max (z +4.4) |
| `wayne_0_61_61_t21-27_shift` | B | 1_wayne_0_61_61 20.7–26.5 s | 21.9 / 12.8 | 39 / 14 | outlier knee max (z +5.4) |
| `wayne_0_61_61_t36-40_shift` | B | 1_wayne_0_61_61 35.9–40.4 s | 19.6 / 14.2 | 20 / 8 | outlier knee max (z +5.7) |
| `wayne_0_61_61_t41-46_shift` | B | 1_wayne_0_61_61 41.2–45.8 s | 18.5 / 13.8 | 14 / 5 | outlier knee max (z +4.8) |
| `wayne_0_61_61_t58-63_shift` | B | 1_wayne_0_61_61 58.0–62.8 s | 11.8 / 7.4 | 33 / 12 | outlier knee max (z +4.3) |
| `wayne_0_62_62_t37-41_shift` | B | 1_wayne_0_62_62 36.9–41.4 s | 11.2 / 8.7 | 35 / 12 | outlier knee max (z +3.8) |
| `wayne_0_62_62_t44-51_shift` | B | 1_wayne_0_62_62 43.9–51.1 s | 11.2 / 7.1 | 31 / 11 | shoulder at limit 22%; outlier knee max (z +3.5) |
| `wayne_0_65_65_t34-41_shift` | B | 1_wayne_0_65_65 33.7–40.5 s | 12.3 / 7.5 | 23 / 7 | outlier knee max (z +3.6) |
| `wayne_0_66_66_t24-29_shift` | B | 1_wayne_0_66_66 24.0–28.5 s | 12.8 / 9.2 | 28 / 8 | outlier knee max (z +3.8) |
| `wayne_0_66_66_t27-36` | A | 1_wayne_0_66_66 26.5–36.2 s | 9.8 / 5.8 | 27 / 9 | outlier knee max (z +4.2) |
| `wayne_0_67_67_t37-41_shift` | B | 1_wayne_0_67_67 36.7–41.2 s | 17.5 / 12.1 | 26 / 7 | outlier knee max (z +4.4) |
| `wayne_0_67_67_t42-51_shift` | B | 1_wayne_0_67_67 42.4–50.8 s | 14.7 / 8.4 | 40 / 15 | outlier knee max (z +3.9) |
| `wayne_0_68_68_t17-34_shift` | B | 1_wayne_0_68_68 17.2–34.0 s | 25.0 / 15.0 | 47 / 22 | outlier arms k1 cm (z +4.0); outlier trunk drop (z +4.6); outlier knee max (z +6.2) |
| `wayne_0_68_68_t3-10_shift` | B | 1_wayne_0_68_68 2.8–10.4 s | 12.3 / 7.3 | 51 / 21 | outlier arms k1 cm (z +3.9) |
| `wayne_0_68_68_t39-43_shift` | B | 1_wayne_0_68_68 38.9–42.9 s | 26.3 / 14.9 | 42 / 17 | human steps; outlier knee max (z +5.1) |
| `wayne_0_69_69_t12-17_shift` | B | 1_wayne_0_69_69 12.1–16.8 s | 11.6 / 7.3 | 45 / 15 | outlier knee max (z +3.7) |
| `wayne_0_69_69_t17-29_shift` | B | 1_wayne_0_69_69 17.1–28.7 s | 38.6 / 23.2 | 30 / 10 | human steps; K1 feet move 23 cm; outlier knee max (z +7.1) |
| `wayne_0_69_69_t53-59_shift` | B | 1_wayne_0_69_69 53.3–59.0 s | 14.0 / 9.7 | 33 / 11 | outlier knee max (z +3.8) |
| `wayne_0_6_6_t0-5_shift` | B | 1_wayne_0_6_6 0.0–5.0 s | 17.6 / 12.4 | 8 / 4 | outlier knee max (z +5.5) |
| `wayne_0_6_6_t12-25_shift` | B | 1_wayne_0_6_6 12.4–25.2 s | 10.7 / 8.2 | 15 / 5 | knee 65 deg; outlier knee max (z +9.8) |
| `wayne_0_6_6_t6-10_shift` | B | 1_wayne_0_6_6 5.5–9.5 s | 24.4 / 16.0 | 14 / 7 | outlier knee max (z +5.7) |
| `wayne_0_70_70_t27-31_shift` | B | 1_wayne_0_70_70 27.3–31.4 s | 24.1 / 13.7 | 36 / 13 | shoulder at limit 16%; outlier knee max (z +5.5) |
| `wayne_0_70_70_t54-60_shift` | B | 1_wayne_0_70_70 54.0–59.8 s | 22.8 / 12.6 | 45 / 15 | outlier knee max (z +5.5) |
| `wayne_0_71_71_t17-24_shift` | B | 1_wayne_0_71_71 17.1–23.8 s | 20.9 / 12.8 | 36 / 14 | outlier knee max (z +4.7) |
| `wayne_0_71_71_t32-40_shift` | B | 1_wayne_0_71_71 32.3–39.8 s | 15.8 / 10.8 | 33 / 13 | outlier knee max (z +5.6) |
| `wayne_0_71_71_t40-47_shift` | B | 1_wayne_0_71_71 40.4–46.8 s | 23.7 / 14.4 | 68 / 22 | outlier arms k1 cm (z +4.2); outlier knee max (z +5.0) |
| `wayne_0_72_72_t13-17_shift` | B | 1_wayne_0_72_72 13.0–17.5 s | 13.0 / 9.8 | 32 / 11 | outlier knee max (z +5.2) |
| `wayne_0_72_72_t30-44_shift` | B | 1_wayne_0_72_72 29.7–44.2 s | 18.4 / 11.9 | 55 / 20 | outlier knee max (z +5.7) |
| `wayne_0_72_72_t56-60_shift` | B | 1_wayne_0_72_72 56.0–60.0 s | 19.7 / 10.5 | 27 / 10 | outlier knee max (z +5.2) |
| `wayne_0_73_73_t26-32` | A | 1_wayne_0_73_73 26.4–31.8 s | 6.7 / 4.1 | 62 / 22 | outlier arms k1 cm (z +4.2) |
| `wayne_0_73_73_t30-43_shift` | B | 1_wayne_0_73_73 29.8–42.8 s | 23.6 / 14.7 | 41 / 14 | outlier knee max (z +3.6) |
| `wayne_0_74_74_t12-22_shift` | B | 1_wayne_0_74_74 11.9–22.3 s | 23.2 / 14.3 | 39 / 12 | outlier knee max (z +3.6) |
| `wayne_0_74_74_t30-34_shift` | B | 1_wayne_0_74_74 29.7–34.3 s | 14.1 / 9.8 | 27 / 11 | outlier knee max (z +4.7) |
| `wayne_0_74_74_t49-53_shift` | B | 1_wayne_0_74_74 48.8–52.8 s | 18.7 / 12.2 | 33 / 13 | outlier knee max (z +3.9) |
| `wayne_0_75_75_t0-16` | A | 1_wayne_0_75_75 0.0–16.3 s | 9.9 / 7.5 | 37 / 12 | shoulder at limit 6% |
| `wayne_0_77_77_t14-19` | A | 1_wayne_0_77_77 13.6–19.4 s | 4.8 / 4.4 | 58 / 21 | outlier arms k1 cm (z +3.8) |
| `wayne_0_77_77_t17-25_shift` | B | 1_wayne_0_77_77 17.4–24.9 s | 24.7 / 15.4 | 58 / 21 | outlier arms k1 cm (z +3.8); outlier knee max (z +4.8) |
| `wayne_0_77_77_t28-40` | A | 1_wayne_0_77_77 27.6–40.5 s | 3.4 / 0.5 | 52 / 19 | shoulder at limit 11% |
| `wayne_0_77_77_t38-43_shift` | B | 1_wayne_0_77_77 38.5–42.6 s | 21.6 / 12.0 | 37 / 11 | outlier knee max (z +5.1) |
| `wayne_0_78_78_t11-15_shift` | B | 1_wayne_0_78_78 10.8–15.2 s | 12.1 / 9.6 | 36 / 13 | outlier knee max (z +4.6) |
| `wayne_0_78_78_t21-28_shift` | B | 1_wayne_0_78_78 20.7–27.6 s | 19.9 / 13.6 | 40 / 14 | outlier knee max (z +4.3) |
| `wayne_0_78_78_t29-33_shift` | B | 1_wayne_0_78_78 28.6–33.1 s | 16.0 / 9.4 | 64 / 23 | outlier arms k1 cm (z +4.4); outlier knee max (z +3.9) |
| `wayne_0_78_78_t42-46_shift` | B | 1_wayne_0_78_78 41.8–45.8 s | 10.7 / 8.2 | 37 / 14 | left arm behind body 5 cm (human's in front) |
| `wayne_0_79_79_t19-30` | A | 1_wayne_0_79_79 19.3–30.2 s | 8.9 / 6.4 | 80 / 24 | outlier arms k1 cm (z +4.8) |
| `wayne_0_79_79_t30-41` | A | 1_wayne_0_79_79 30.2–41.1 s | 10.6 / 6.8 | 40 / 15 | human steps |
| `wayne_0_7_7_t45-49_shift` | B | 1_wayne_0_7_7 44.5–49.1 s | 11.6 / 8.0 | 16 / 7 | outlier knee max (z +3.8) |
| `wayne_0_80_80_t0-15_shift` | B | 1_wayne_0_80_80 0.0–15.3 s | 24.1 / 15.2 | 39 / 13 | outlier knee max (z +5.4) |
| `wayne_0_80_80_t23-34` | A | 1_wayne_0_80_80 22.6–33.8 s | 1.5 / 1.6 | 71 / 22 | outlier arms k1 cm (z +4.2) |
| `wayne_0_80_80_t49-57` | A | 1_wayne_0_80_80 48.6–56.6 s | 2.2 / 1.1 | 96 / 31 | outlier arms k1 cm (z +6.7) |
| `wayne_0_80_80_t53-57_shift` | B | 1_wayne_0_80_80 53.2–57.2 s | 24.9 / 15.3 | 114 / 35 | outlier arms k1 cm (z +7.7); outlier knee max (z +4.4) |
| `wayne_0_82_82_t40-45_shift` | B | 1_wayne_0_82_82 40.2–44.6 s | 5.2 / 4.6 | 32 / 11 | shoulder at limit 13% |
| `wayne_0_83_83_t37-43_shift` | B | 1_wayne_0_83_83 37.4–42.9 s | 18.0 / 10.3 | 20 / 8 | outlier knee max (z +5.2) |
| `wayne_0_84_84_t17-35` | A | 1_wayne_0_84_84 17.4–34.6 s | 6.2 / 4.9 | 26 / 9 | shoulder at limit 10% |
| `wayne_0_85_85_t50-55_shift` | B | 1_wayne_0_85_85 50.3–54.8 s | 13.7 / 10.8 | 51 / 16 | outlier knee max (z +4.4) |
| `wayne_0_85_85_t65-74_shift` | B | 1_wayne_0_85_85 65.3–73.8 s | 28.5 / 19.7 | 5 / 2 | human steps; K1 feet move 20 cm; outlier knee max (z +5.8); hand presses into leg 11 mm for 0.1 s (at 2.1 s) |
| `wayne_0_86_86_t47-52_shift` | B | 1_wayne_0_86_86 47.3–51.9 s | 18.8 / 10.3 | 21 / 5 | outlier knee max (z +4.8) |
| `wayne_0_86_86_t53-58_shift` | B | 1_wayne_0_86_86 53.0–57.8 s | 21.8 / 16.2 | 36 / 9 | outlier knee max (z +6.0) |
| `wayne_0_87_87_t57-62_shift` | B | 1_wayne_0_87_87 57.3–61.9 s | 15.1 / 8.9 | 12 / 5 | outlier knee max (z +6.8) |
| `wayne_0_87_87_t69-73_shift` | B | 1_wayne_0_87_87 68.9–73.5 s | 13.5 / 10.7 | 10 / 4 | outlier knee max (z +4.8) |
| `wayne_0_87_87_t75-80_shift` | B | 1_wayne_0_87_87 74.9–79.8 s | 20.7 / 14.9 | 11 / 4 | outlier knee max (z +4.8) |
| `wayne_0_88_88_t26-38_shift` | B | 1_wayne_0_88_88 25.6–37.8 s | 15.6 / 10.5 | 37 / 15 | outlier knee max (z +4.5) |
| `wayne_0_88_88_t61-67` | A | 1_wayne_0_88_88 60.8–67.0 s | 9.4 / 3.1 | 42 / 14 | outlier knee max (z +4.0) |
| `wayne_0_88_88_t65-70_shift` | B | 1_wayne_0_88_88 65.0–69.5 s | 11.3 / 8.6 | 34 / 12 | outlier knee max (z +4.5) |
| `wayne_0_89_89_t66-70_shift` | B | 1_wayne_0_89_89 65.6–69.6 s | 19.3 / 11.0 | 17 / 6 | outlier knee max (z +3.8) |
| `wayne_0_8_8_t0-4_shift` | B | 1_wayne_0_8_8 0.0–4.0 s | 16.5 / 9.6 | 14 / 5 | outlier knee max (z +4.0) |
| `wayne_0_8_8_t16-20_shift` | B | 1_wayne_0_8_8 16.0–20.0 s | 24.9 / 15.7 | 17 / 5 | outlier knee max (z +6.8) |
| `wayne_0_8_8_t24-30_shift` | B | 1_wayne_0_8_8 24.3–30.3 s | 22.2 / 13.4 | 15 / 5 | outlier knee max (z +7.4) |
| `wayne_0_90_90_t0-5_shift` | B | 1_wayne_0_90_90 0.3–5.0 s | 12.6 / 10.6 | 10 / 3 | outlier knee max (z +3.6) |
| `wayne_0_90_90_t40-45_shift` | B | 1_wayne_0_90_90 40.1–44.6 s | 15.4 / 11.1 | 36 / 13 | outlier knee max (z +5.6) |
| `wayne_0_90_90_t47-51_shift` | B | 1_wayne_0_90_90 47.4–51.4 s | 26.8 / 15.7 | 34 / 13 | human steps |
| `wayne_0_91_91_t24-28_shift` | B | 1_wayne_0_91_91 24.2–28.2 s | 25.5 / 15.2 | 21 / 7 | human steps; outlier knee max (z +5.5) |
| `wayne_0_91_91_t36-40_shift` | B | 1_wayne_0_91_91 35.9–39.9 s | 24.7 / 16.1 | 18 / 7 | outlier knee max (z +6.1) |
| `wayne_0_91_91_t7-17` | A | 1_wayne_0_91_91 6.6–17.1 s | 1.5 / 0.6 | 25 / 10 | shoulder at limit 9% |
| `wayne_0_93_93_t11-23_shift` | B | 1_wayne_0_93_93 11.4–22.9 s | 34.8 / 23.0 | 35 / 14 | human steps; K1 feet move 23 cm; shoulder at limit 6%; outlier knee max (z +4.1) |
| `wayne_0_94_94_t49-53_shift` | B | 1_wayne_0_94_94 48.8–53.3 s | 15.7 / 10.3 | 20 / 8 | outlier knee max (z +6.8) |
| `wayne_0_94_94_t60-68_shift` | B | 1_wayne_0_94_94 60.1–67.8 s | 30.4 / 19.2 | 49 / 17 | human steps; K1 feet move 19 cm; outlier knee max (z +5.0) |
| `wayne_0_95_95_t0-13_shift` | B | 1_wayne_0_95_95 0.0–13.1 s | 17.8 / 12.2 | 28 / 10 | outlier knee max (z +4.7) |
| `wayne_0_95_95_t11-27` | A | 1_wayne_0_95_95 11.1–27.3 s | 8.8 / 4.6 | 51 / 18 | outlier knee max (z +4.8) |
| `wayne_0_95_95_t27-43` | A | 1_wayne_0_95_95 27.3–43.4 s | 10.5 / 5.7 | 45 / 17 | human steps |
| `wayne_0_96_96_t27-35` | A | 1_wayne_0_96_96 26.9–35.1 s | 2.0 / 0.8 | 33 / 12 | outlier knee max (z +3.6) |
| `wayne_0_98_98_t15-24_shift` | B | 1_wayne_0_98_98 15.1–24.2 s | 25.1 / 14.2 | 32 / 11 | human steps; knee 61 deg; outlier knee max (z +8.3) |
| `wayne_0_98_98_t24-34_shift` | B | 1_wayne_0_98_98 24.4–33.5 s | 26.1 / 18.6 | 43 / 15 | human steps; K1 feet move 19 cm; outlier knee max (z +7.8) |
| `wayne_0_98_98_t7-12_shift` | B | 1_wayne_0_98_98 7.2–11.8 s | 10.6 / 8.1 | 24 / 10 | outlier knee max (z +4.0) |
| `wayne_0_9_9_t26-31_shift` | B | 1_wayne_0_9_9 25.8–31.3 s | 20.6 / 12.1 | 9 / 3 | outlier knee max (z +6.3) |
| `wayne_0_9_9_t4-8_shift` | B | 1_wayne_0_9_9 4.0–8.0 s | 15.5 / 13.2 | 9 / 3 | outlier knee max (z +3.7) |
| `wayne_0_9_9_t56-62_shift` | B | 1_wayne_0_9_9 56.2–61.8 s | 15.5 / 10.2 | 10 / 3 | outlier knee max (z +4.0) |
| `wayne_1_10_10_t248-256` | A | 1_wayne_1_10_10 248.4–256.0 s | 9.6 / 8.1 | 13 / 5 | K1 feet move 8 cm |
| `wayne_1_10_10_t273-277_shift` | B | 1_wayne_1_10_10 273.0–277.0 s | 33.0 / 16.5 | 22 / 8 | human steps |
| `wayne_1_10_10_t447-455_shift` | B | 1_wayne_1_10_10 447.1–455.3 s | 30.3 / 18.9 | 27 / 10 | human steps; K1 feet move 19 cm |
| `wayne_1_10_10_t551-555_shift` | B | 1_wayne_1_10_10 550.7–555.4 s | 18.0 / 11.6 | 15 / 5 | outlier knee max (z +4.6) |
| `wayne_1_10_10_t575-584` | A | 1_wayne_1_10_10 574.8–584.0 s | 8.2 / 8.6 | 23 / 9 | K1 feet move 9 cm |
| `wayne_1_10_10_t586-591` | A | 1_wayne_1_10_10 586.5–591.1 s | 9.8 / 9.3 | 17 / 5 | K1 feet move 9 cm |
| `wayne_1_10_10_t59-69_shift` | B | 1_wayne_1_10_10 58.6–68.6 s | 22.5 / 14.4 | 25 / 7 | outlier knee max (z +4.1) |
| `wayne_1_10_10_t597-603_shift` | B | 1_wayne_1_10_10 597.1–602.8 s | 26.7 / 14.9 | 16 / 6 | human steps; outlier knee max (z +4.3) |
| `wayne_1_10_10_t621-632_shift` | B | 1_wayne_1_10_10 621.4–631.6 s | 31.2 / 20.1 | 23 / 9 | human steps; K1 feet move 20 cm; outlier knee max (z +4.0) |
| `wayne_1_10_10_t72-77_shift` | B | 1_wayne_1_10_10 71.9–76.5 s | 17.8 / 10.3 | 26 / 8 | outlier knee max (z +3.5) |
| `wayne_1_10_10_t77-82_shift` | B | 1_wayne_1_10_10 77.3–81.9 s | 16.0 / 10.9 | 24 / 7 | outlier knee max (z +4.3) |
| `wayne_1_11_11_t103-108_shift` | B | 1_wayne_1_11_11 102.9–108.3 s | 25.0 / 14.0 | 19 / 6 | human steps; outlier knee max (z +4.2) |
| `wayne_1_11_11_t15-23_shift` | B | 1_wayne_1_11_11 14.8–22.7 s | 17.1 / 10.4 | 16 / 5 | outlier knee max (z +3.6) |
| `wayne_1_11_11_t195-200_shift` | B | 1_wayne_1_11_11 195.3–200.1 s | 17.8 / 9.1 | 17 / 6 | outlier knee max (z +3.7) |
| `wayne_1_11_11_t221-228` | A | 1_wayne_1_11_11 221.1–228.0 s | 0.6 / 1.0 | 33 / 10 | shoulder at limit 29% |
| `wayne_1_11_11_t245-250_shift` | B | 1_wayne_1_11_11 244.6–250.4 s | 25.7 / 17.2 | 27 / 13 | human steps; self-collision left_hand_end_collision / right_hand_collision 0.4 s (at 5.5 s, 18 mm) |
| `wayne_1_11_11_t248-259` | A | 1_wayne_1_11_11 248.4–258.9 s | 1.1 / 0.8 | 17 / 9 | self-collision left_hand_end_collision / right_hand_collision 4.3 s (at 1.6 s, 18 mm) |
| `wayne_1_11_11_t302-315_shift` | B | 1_wayne_1_11_11 302.0–314.8 s | 26.5 / 14.6 | 29 / 9 | human steps; outlier knee max (z +5.8) |
| `wayne_1_11_11_t32-37_shift` | B | 1_wayne_1_11_11 31.6–37.0 s | 23.9 / 12.6 | 20 / 9 | outlier knee max (z +4.4) |
| `wayne_1_11_11_t565-571_shift` | B | 1_wayne_1_11_11 565.3–571.0 s | 30.2 / 15.4 | 28 / 12 | human steps; outlier knee max (z +4.4) |
| `wayne_1_11_11_t58-64_shift` | B | 1_wayne_1_11_11 57.6–63.5 s | 31.9 / 17.5 | 20 / 8 | human steps |
| `wayne_1_11_11_t70-75_shift` | B | 1_wayne_1_11_11 69.5–75.3 s | 28.9 / 15.4 | 17 / 7 | human steps |
| `wayne_1_12_12_t144-157` | A | 1_wayne_1_12_12 143.9–156.9 s | 7.6 / 8.7 | 14 / 7 | K1 feet move 9 cm |
| `wayne_1_12_12_t185-192_shift` | B | 1_wayne_1_12_12 184.7–192.4 s | 17.9 / 10.1 | 20 / 7 | outlier knee max (z +4.4) |
| `wayne_1_12_12_t259-264_shift` | B | 1_wayne_1_12_12 259.1–263.6 s | 16.8 / 10.0 | 29 / 12 | outlier knee max (z +4.9) |
| `wayne_1_12_12_t264-269_shift` | B | 1_wayne_1_12_12 264.3–268.9 s | 17.7 / 13.2 | 21 / 8 | outlier knee max (z +4.9) |
| `wayne_1_12_12_t298-302_shift` | B | 1_wayne_1_12_12 297.7–302.4 s | 22.6 / 14.9 | 33 / 14 | outlier knee max (z +4.7) |
| `wayne_1_12_12_t326-333_shift` | B | 1_wayne_1_12_12 325.6–332.6 s | 23.2 / 13.6 | 37 / 13 | outlier knee max (z +5.1) |
| `wayne_1_12_12_t404-412_shift` | B | 1_wayne_1_12_12 403.7–412.4 s | 16.4 / 9.6 | 20 / 8 | outlier knee max (z +3.8) |
| `wayne_1_12_12_t424-430_shift` | B | 1_wayne_1_12_12 423.5–429.8 s | 23.6 / 13.4 | 34 / 15 | outlier knee max (z +3.9) |
| `wayne_1_12_12_t475-481` | A | 1_wayne_1_12_12 474.7–481.5 s | 9.1 / 10.4 | 21 / 9 | K1 feet move 10 cm |
| `wayne_1_12_12_t502-511_shift` | B | 1_wayne_1_12_12 502.0–511.1 s | 21.0 / 11.3 | 27 / 12 | outlier knee max (z +5.0) |
| `wayne_1_12_12_t605-612_shift` | B | 1_wayne_1_12_12 605.4–611.5 s | 26.0 / 12.6 | 17 / 6 | human steps |
| `wayne_1_1_1_t123-131_shift` | B | 1_wayne_1_1_1 122.6–131.2 s | 22.6 / 11.2 | 21 / 7 | outlier knee max (z +5.9) |
| `wayne_1_1_1_t147-158_shift` | B | 1_wayne_1_1_1 146.6–157.6 s | 31.5 / 15.8 | 32 / 10 | human steps |
| `wayne_1_1_1_t165-176_shift` | B | 1_wayne_1_1_1 164.9–175.6 s | 27.9 / 15.1 | 33 / 13 | human steps; outlier knee max (z +3.9) |
| `wayne_1_1_1_t202-208_shift` | B | 1_wayne_1_1_1 202.3–208.0 s | 28.8 / 15.5 | 20 / 9 | human steps |
| `wayne_1_1_1_t251-255_shift` | B | 1_wayne_1_1_1 251.4–255.4 s | 24.2 / 14.4 | 22 / 8 | outlier knee max (z +6.6) |
| `wayne_1_1_1_t274-282_shift` | B | 1_wayne_1_1_1 274.1–282.0 s | 18.7 / 11.2 | 38 / 14 | outlier knee max (z +6.6) |
| `wayne_1_1_1_t305-313_shift` | B | 1_wayne_1_1_1 304.8–312.6 s | 25.3 / 13.1 | 31 / 11 | human steps; outlier knee max (z +3.7) |
| `wayne_1_1_1_t366-374_shift` | B | 1_wayne_1_1_1 365.7–374.0 s | 29.2 / 16.6 | 30 / 11 | human steps; outlier knee max (z +4.8) |
| `wayne_1_1_1_t403-408_shift` | B | 1_wayne_1_1_1 403.0–408.3 s | 21.7 / 10.3 | 33 / 11 | outlier knee max (z +4.4) |
| `wayne_1_1_1_t409-416_shift` | B | 1_wayne_1_1_1 409.4–415.5 s | 24.7 / 12.7 | 36 / 11 | outlier knee max (z +5.3) |
| `wayne_1_1_1_t543-553` | A | 1_wayne_1_1_1 543.1–553.1 s | 5.1 / 0.6 | 34 / 11 | shoulder at limit 32% |
| `wayne_1_1_1_t55-60_shift` | B | 1_wayne_1_1_1 55.3–59.9 s | 20.2 / 13.3 | 35 / 9 | outlier knee max (z +5.4) |
| `wayne_1_1_1_t554-563` | A | 1_wayne_1_1_1 554.5–563.1 s | 9.6 / 8.2 | 15 / 6 | K1 feet move 8 cm |
| `wayne_1_1_1_t578-583_shift` | B | 1_wayne_1_1_1 578.0–582.6 s | 13.6 / 10.4 | 19 / 8 | outlier knee max (z +4.2) |
| `wayne_1_1_1_t591-595_shift` | B | 1_wayne_1_1_1 591.4–595.4 s | 29.9 / 15.2 | 17 / 7 | human steps; outlier knee max (z +4.9) |
| `wayne_1_1_1_t65-70_shift` | B | 1_wayne_1_1_1 65.1–69.7 s | 19.3 / 12.3 | 31 / 9 | outlier knee max (z +5.1) |
| `wayne_1_1_1_t77-82_shift` | B | 1_wayne_1_1_1 76.8–81.5 s | 21.9 / 13.6 | 23 / 7 | outlier knee max (z +4.8) |
| `wayne_1_1_1_t82-86_shift` | B | 1_wayne_1_1_1 81.8–86.5 s | 22.8 / 14.1 | 21 / 7 | outlier knee max (z +4.8) |
| `wayne_1_1_1_t89-95_shift` | B | 1_wayne_1_1_1 89.4–95.0 s | 19.2 / 10.3 | 26 / 10 | outlier knee max (z +3.6) |
| `wayne_1_2_2_t108-113_shift` | B | 1_wayne_1_2_2 107.7–113.3 s | 30.2 / 17.1 | 21 / 8 | human steps |
| `wayne_1_2_2_t111-116` | A | 1_wayne_1_2_2 111.3–115.8 s | 0.6 / 0.4 | 31 / 11 | shoulder at limit 12% |
| `wayne_1_2_2_t126-130_shift` | B | 1_wayne_1_2_2 125.5–130.2 s | 16.9 / 11.0 | 34 / 10 | outlier knee max (z +5.2) |
| `wayne_1_2_2_t131-135_shift` | B | 1_wayne_1_2_2 130.8–135.5 s | 20.6 / 13.1 | 41 / 13 | outlier knee max (z +5.1) |
| `wayne_1_2_2_t138-146_shift` | B | 1_wayne_1_2_2 137.6–146.4 s | 21.5 / 12.0 | 42 / 18 | outlier knee max (z +4.5) |
| `wayne_1_2_2_t167-172_shift` | B | 1_wayne_1_2_2 167.2–171.8 s | 25.0 / 14.0 | 36 / 13 | outlier knee max (z +4.3) |
| `wayne_1_2_2_t186-191_shift` | B | 1_wayne_1_2_2 185.8–191.1 s | 24.4 / 10.7 | 37 / 11 | outlier knee max (z +4.2) |
| `wayne_1_2_2_t194-201_shift` | B | 1_wayne_1_2_2 193.7–200.9 s | 23.9 / 12.2 | 22 / 7 | outlier knee max (z +3.6) |
| `wayne_1_2_2_t22-27_shift` | B | 1_wayne_1_2_2 22.3–26.8 s | 16.5 / 10.7 | 17 / 7 | outlier knee max (z +4.4) |
| `wayne_1_2_2_t239-247_shift` | B | 1_wayne_1_2_2 239.2–247.3 s | 26.1 / 15.4 | 36 / 14 | human steps |
| `wayne_1_2_2_t248-253_shift` | B | 1_wayne_1_2_2 248.2–252.7 s | 19.2 / 8.6 | 18 / 7 | outlier knee max (z +4.0) |
| `wayne_1_2_2_t253-268_shift` | B | 1_wayne_1_2_2 253.1–267.7 s | 25.2 / 14.9 | 24 / 9 | human steps; outlier knee max (z +7.1) |
| `wayne_1_2_2_t272-280_shift` | B | 1_wayne_1_2_2 271.5–280.2 s | 28.4 / 16.9 | 29 / 9 | human steps; outlier knee max (z +6.6) |
| `wayne_1_2_2_t285-289_shift` | B | 1_wayne_1_2_2 285.2–289.2 s | 25.0 / 14.2 | 24 / 10 | outlier knee max (z +4.8) |
| `wayne_1_2_2_t289-307` | A | 1_wayne_1_2_2 289.2–306.7 s | 7.7 / 5.5 | 37 / 14 | shoulder at limit 13% |
| `wayne_1_2_2_t30-39` | A | 1_wayne_1_2_2 29.9–38.7 s | 7.4 / 0.6 | 38 / 13 | shoulder at limit 8% |
| `wayne_1_2_2_t305-315_shift` | B | 1_wayne_1_2_2 304.7–315.3 s | 26.0 / 14.6 | 31 / 12 | human steps; outlier knee max (z +5.4) |
| `wayne_1_2_2_t316-321_shift` | B | 1_wayne_1_2_2 316.4–321.1 s | 15.6 / 11.3 | 27 / 11 | outlier knee max (z +4.9) |
| `wayne_1_2_2_t364-368` | A | 1_wayne_1_2_2 363.6–367.7 s | 0.8 / 0.5 | 63 / 20 | outlier arms k1 cm (z +3.7) |
| `wayne_1_2_2_t366-376_shift` | B | 1_wayne_1_2_2 365.7–375.7 s | 25.3 / 21.1 | 29 / 10 | human steps; K1 feet move 21 cm; knee 65 deg; outlier knee max (z +9.7) |
| `wayne_1_2_2_t399-406_shift` | B | 1_wayne_1_2_2 399.2–405.7 s | 30.5 / 19.0 | 49 / 18 | human steps; K1 feet move 19 cm; outlier knee max (z +5.0) |
| `wayne_1_2_2_t449-456` | A | 1_wayne_1_2_2 449.2–456.2 s | 1.2 / 0.4 | 46 / 21 | outlier arms k1 cm (z +3.7) |
| `wayne_1_2_2_t5-11_shift` | B | 1_wayne_1_2_2 5.2–11.0 s | 22.5 / 16.4 | 30 / 9 | knee 64 deg; outlier knee max (z +9.5) |
| `wayne_1_2_2_t535-545_shift` | B | 1_wayne_1_2_2 534.7–544.9 s | 16.0 / 14.6 | 36 / 14 | outlier knee max (z +4.5) |
| `wayne_1_2_2_t545-561_shift` | B | 1_wayne_1_2_2 545.1–561.2 s | 23.8 / 13.9 | 34 / 14 | outlier knee max (z +5.1) |
| `wayne_1_2_2_t59-65_shift` | B | 1_wayne_1_2_2 59.3–64.9 s | 24.0 / 12.0 | 28 / 10 | outlier knee max (z +4.9) |
| `wayne_1_2_2_t599-608` | A | 1_wayne_1_2_2 598.9–607.8 s | 6.1 / 11.2 | 22 / 11 | K1 feet move 11 cm |
| `wayne_1_2_2_t63-72` | A | 1_wayne_1_2_2 62.9–71.8 s | 2.5 / 0.6 | 28 / 10 | shoulder at limit 7% |
| `wayne_1_2_2_t70-75_shift` | B | 1_wayne_1_2_2 69.8–74.7 s | 16.2 / 10.9 | 35 / 13 | shoulder at limit 25% |
| `wayne_1_3_3_t0-13` | A | 1_wayne_1_3_3 0.0–13.3 s | 9.7 / 9.5 | 23 / 8 | K1 feet move 10 cm |
| `wayne_1_3_3_t155-169` | A | 1_wayne_1_3_3 155.4–168.7 s | 9.8 / 8.1 | 22 / 7 | K1 feet move 8 cm |
| `wayne_1_3_3_t310-320_shift` | B | 1_wayne_1_3_3 310.2–319.9 s | 33.0 / 20.9 | 26 / 10 | human steps; K1 feet move 21 cm; outlier knee max (z +4.1) |
| `wayne_1_3_3_t470-477_shift` | B | 1_wayne_1_3_3 470.2–477.0 s | 14.3 / 7.6 | 22 / 9 | outlier knee max (z +4.2) |
| `wayne_1_3_3_t478-482_shift` | B | 1_wayne_1_3_3 478.1–482.1 s | 13.4 / 8.4 | 35 / 20 | outlier arms k1 cm (z +3.7) |
| `wayne_1_3_3_t479-485` | A | 1_wayne_1_3_3 479.2–484.6 s | 2.2 / 0.8 | 44 / 21 | outlier arms k1 cm (z +3.9) |
| `wayne_1_4_4_t103-110` | A | 1_wayne_1_4_4 103.3–109.6 s | 7.6 / 2.2 | 53 / 20 | outlier arms k1 cm (z +3.5) |
| `wayne_1_4_4_t120-125` | A | 1_wayne_1_4_4 119.6–124.7 s | 6.5 / 3.7 | 40 / 19 | shoulder at limit 22% |
| `wayne_1_4_4_t197-210_shift` | B | 1_wayne_1_4_4 197.1–209.9 s | 19.4 / 13.7 | 29 / 10 | outlier knee max (z +3.8) |
| `wayne_1_4_4_t246-250_shift` | B | 1_wayne_1_4_4 246.2–250.2 s | 22.3 / 11.6 | 13 / 5 | outlier knee max (z +5.4) |
| `wayne_1_4_4_t310-326_shift` | B | 1_wayne_1_4_4 310.5–326.3 s | 20.1 / 12.9 | 37 / 15 | outlier knee max (z +5.9) |
| `wayne_1_4_4_t434-439` | A | 1_wayne_1_4_4 434.2–438.6 s | 8.8 / 9.7 | 19 / 6 | K1 feet move 10 cm |
| `wayne_1_5_5_t108-115_shift` | B | 1_wayne_1_5_5 108.2–115.3 s | 20.4 / 13.1 | 42 / 14 | outlier knee max (z +5.2) |
| `wayne_1_5_5_t146-151` | A | 1_wayne_1_5_5 146.5–151.1 s | 7.3 / 2.7 | 72 / 25 | outlier arms k1 cm (z +5.0) |
| `wayne_1_5_5_t202-207_shift` | B | 1_wayne_1_5_5 202.4–207.3 s | 13.5 / 9.4 | 25 / 9 | outlier knee max (z +3.9) |
| `wayne_1_5_5_t205-213` | A | 1_wayne_1_5_5 205.3–212.9 s | 7.2 / 9.2 | 29 / 10 | K1 feet move 9 cm |
| `wayne_1_5_5_t237-243_shift` | B | 1_wayne_1_5_5 237.1–242.9 s | 19.5 / 11.7 | 23 / 7 | outlier knee max (z +4.0) |
| `wayne_1_5_5_t271-281_shift` | B | 1_wayne_1_5_5 271.1–281.3 s | 23.6 / 11.4 | 31 / 11 | outlier knee max (z +3.9) |
| `wayne_1_5_5_t293-302_shift` | B | 1_wayne_1_5_5 293.4–302.2 s | 20.1 / 19.6 | 29 / 9 | K1 feet move 20 cm; knee 78 deg; outlier knee max (z +14.2) |
| `wayne_1_5_5_t311-315_shift` | B | 1_wayne_1_5_5 310.7–315.0 s | 21.3 / 12.3 | 15 / 6 | outlier knee max (z +4.3) |
| `wayne_1_5_5_t567-578_shift` | B | 1_wayne_1_5_5 567.0–577.7 s | 24.0 / 11.7 | 19 / 7 | outlier knee max (z +5.6) |
| `wayne_1_5_5_t580-589_shift` | B | 1_wayne_1_5_5 579.7–588.7 s | 41.5 / 24.2 | 33 / 11 | human steps; K1 feet move 24 cm; outlier knee max (z +3.6) |
| `wayne_1_6_6_t121-126_shift` | B | 1_wayne_1_6_6 120.6–126.1 s | 15.5 / 8.7 | 41 / 13 | outlier knee max (z +5.4) |
| `wayne_1_6_6_t233-237_shift` | B | 1_wayne_1_6_6 233.1–237.1 s | 32.2 / 19.5 | 15 / 7 | human steps; K1 feet move 19 cm; outlier knee max (z +5.1) |
| `wayne_1_6_6_t294-303_shift` | B | 1_wayne_1_6_6 294.0–303.2 s | 16.9 / 10.9 | 21 / 7 | outlier knee max (z +4.5) |
| `wayne_1_6_6_t310-315` | A | 1_wayne_1_6_6 309.9–314.8 s | 6.8 / 9.7 | 18 / 6 | K1 feet move 10 cm |
| `wayne_1_6_6_t313-317_shift` | B | 1_wayne_1_6_6 312.8–317.4 s | 12.9 / 10.3 | 34 / 12 | outlier knee max (z +3.8) |
| `wayne_1_6_6_t400-404_shift` | B | 1_wayne_1_6_6 399.6–403.6 s | 12.5 / 7.8 | 64 / 20 | outlier arms k1 cm (z +3.7) |
| `wayne_1_6_6_t442-448_shift` | B | 1_wayne_1_6_6 442.4–448.4 s | 15.7 / 4.4 | 27 / 9 | outlier knee max (z +3.6) |
| `wayne_1_6_6_t455-460_shift` | B | 1_wayne_1_6_6 454.9–459.5 s | 12.8 / 8.7 | 24 / 10 | outlier knee max (z +7.8) |
| `wayne_1_6_6_t458-463` | A | 1_wayne_1_6_6 457.5–463.1 s | 9.2 / 8.6 | 25 / 9 | K1 feet move 9 cm |
| `wayne_1_6_6_t471-479` | A | 1_wayne_1_6_6 470.6–479.1 s | 8.2 / 9.2 | 25 / 7 | K1 feet move 9 cm |
| `wayne_1_6_6_t492-499` | A | 1_wayne_1_6_6 491.7–499.0 s | 6.1 / 3.6 | 70 / 21 | outlier arms k1 cm (z +3.9) |
| `wayne_1_6_6_t598-603_shift` | B | 1_wayne_1_6_6 598.3–602.7 s | 17.8 / 8.7 | 42 / 19 | outlier knee max (z +5.6) |
| `wayne_1_6_6_t82-86_shift` | B | 1_wayne_1_6_6 82.5–86.5 s | 13.3 / 8.2 | 24 / 10 | outlier knee max (z +4.3) |
| `wayne_1_7_7_t182-188` | A | 1_wayne_1_7_7 181.6–188.0 s | 9.8 / 8.4 | 23 / 6 | K1 feet move 8 cm |
| `wayne_1_7_7_t186-191_shift` | B | 1_wayne_1_7_7 186.0–191.1 s | 23.5 / 14.7 | 15 / 4 | outlier knee max (z +6.1) |
| `wayne_1_7_7_t198-203_shift` | B | 1_wayne_1_7_7 198.2–203.0 s | 33.2 / 19.4 | 13 / 5 | human steps; K1 feet move 19 cm; outlier knee max (z +5.4) |
| `wayne_1_7_7_t323-328` | A | 1_wayne_1_7_7 323.0–327.6 s | 6.8 / 8.5 | 19 / 7 | K1 feet move 8 cm |
| `wayne_1_7_7_t337-342_shift` | B | 1_wayne_1_7_7 336.5–342.1 s | 39.9 / 21.0 | 19 / 7 | human steps; K1 feet move 21 cm; outlier knee max (z +5.4) |
| `wayne_1_7_7_t368-373_shift` | B | 1_wayne_1_7_7 368.4–373.2 s | 26.5 / 14.1 | 8 / 3 | human steps; outlier knee max (z +3.7) |
| `wayne_1_7_7_t400-406_shift` | B | 1_wayne_1_7_7 400.4–405.7 s | 26.2 / 12.2 | 23 / 8 | human steps |
| `wayne_1_7_7_t496-502` | A | 1_wayne_1_7_7 495.9–501.7 s | 3.6 / 0.9 | 36 / 15 | shoulder at limit 13% |
| `wayne_1_7_7_t584-590` | A | 1_wayne_1_7_7 583.5–590.2 s | 2.4 / 2.2 | 21 / 8 | shoulder at limit 18% |
| `wayne_1_8_8_t199-208_shift` | B | 1_wayne_1_8_8 199.0–208.3 s | 23.3 / 14.7 | 15 / 7 | outlier knee max (z +4.1) |
| `wayne_1_8_8_t211-218_shift` | B | 1_wayne_1_8_8 211.4–217.8 s | 28.2 / 20.8 | 31 / 13 | human steps; K1 feet move 21 cm |
| `wayne_1_8_8_t278-284` | A | 1_wayne_1_8_8 277.9–284.3 s | 6.4 / 2.9 | 36 / 12 | shoulder at limit 6% |
| `wayne_1_8_8_t282-287_shift` | B | 1_wayne_1_8_8 282.3–287.1 s | 13.9 / 4.7 | 39 / 12 | shoulder at limit 8% |
| `wayne_1_8_8_t381-387_shift` | B | 1_wayne_1_8_8 381.2–386.9 s | 13.6 / 5.4 | 31 / 13 | outlier knee max (z +3.6) |
| `wayne_1_8_8_t634-638_shift` | B | 1_wayne_1_8_8 633.7–637.7 s | 29.9 / 15.4 | 29 / 9 | human steps; outlier knee max (z +4.0) |
| `wayne_1_8_8_t87-91_shift` | B | 1_wayne_1_8_8 87.3–91.3 s | 30.8 / 16.9 | 30 / 14 | human steps |
| `wayne_1_9_9_t138-146_shift` | B | 1_wayne_1_9_9 138.0–146.1 s | 22.3 / 9.5 | 28 / 10 | outlier knee max (z +4.0) |
| `wayne_1_9_9_t18-26_shift` | B | 1_wayne_1_9_9 18.2–26.2 s | 29.3 / 17.9 | 21 / 8 | human steps; outlier knee max (z +4.4) |
| `wayne_1_9_9_t229-235_shift` | B | 1_wayne_1_9_9 229.0–234.6 s | 21.0 / 11.4 | 13 / 5 | outlier knee max (z +3.7) |
| `wayne_1_9_9_t235-242_shift` | B | 1_wayne_1_9_9 235.2–242.1 s | 29.1 / 15.6 | 18 / 6 | human steps |
| `wayne_1_9_9_t246-252_shift` | B | 1_wayne_1_9_9 246.0–251.9 s | 32.1 / 17.1 | 25 / 9 | human steps |
| `wayne_1_9_9_t259-265_shift` | B | 1_wayne_1_9_9 259.0–264.8 s | 34.9 / 19.0 | 29 / 10 | human steps; K1 feet move 19 cm; outlier knee max (z +3.9) |
| `wayne_1_9_9_t289-296_shift` | B | 1_wayne_1_9_9 288.8–296.0 s | 27.3 / 18.6 | 32 / 10 | human steps; K1 feet move 19 cm; outlier knee max (z +3.6) |
| `wayne_1_9_9_t326-333_shift` | B | 1_wayne_1_9_9 326.0–333.2 s | 26.0 / 14.6 | 19 / 10 | human steps |
| `wayne_1_9_9_t365-370_shift` | B | 1_wayne_1_9_9 365.0–369.5 s | 14.3 / 8.2 | 23 / 8 | outlier knee max (z +3.6) |
| `wayne_1_9_9_t507-511_shift` | B | 1_wayne_1_9_9 506.7–510.7 s | 28.3 / 15.0 | 16 / 6 | human steps |
| `yingqing_0_103_103_t62-73` | A | 27_yingqing_0_103_103 62.4–73.2 s | 1.0 / 0.7 | 31 / 12 | elbow bend at limit 10%; outlier knee max (z +3.9); self-collision head_2_collision / right_hand_end_collision 2.4 s (at 5.0 s, 24 mm) |
| `yingqing_0_10_10_t0-6_shift` | B | 27_yingqing_0_10_10 0.0–6.3 s | 16.9 / 9.6 | 24 / 10 | outlier knee max (z +4.0) |
| `yingqing_0_10_10_t24-32_shift` | B | 27_yingqing_0_10_10 23.5–31.8 s | 21.9 / 11.8 | 26 / 8 | outlier knee max (z +7.3) |
| `yingqing_0_10_10_t47-65` | A | 27_yingqing_0_10_10 47.2–64.7 s | 1.4 / 0.6 | 32 / 12 | elbow bend at limit 6% |
| `yingqing_0_111_111_t0-6_shift` | B | 27_yingqing_0_111_111 0.0–6.0 s | 12.7 / 10.9 | 13 / 4 | outlier knee max (z +7.4) |
| `yingqing_0_111_111_t14-22_shift` | B | 27_yingqing_0_111_111 14.4–22.0 s | 16.1 / 11.1 | 11 / 4 | outlier knee max (z +6.1) |
| `yingqing_0_111_111_t33-37_shift` | B | 27_yingqing_0_111_111 32.8–37.2 s | 10.5 / 7.3 | 14 / 5 | outlier knee max (z +4.8) |
| `yingqing_0_111_111_t38-43_shift` | B | 27_yingqing_0_111_111 38.1–42.6 s | 10.8 / 7.8 | 20 / 6 | outlier knee max (z +7.1) |
| `yingqing_0_111_111_t43-48_shift` | B | 27_yingqing_0_111_111 42.8–47.6 s | 22.0 / 11.2 | 23 / 7 | outlier knee max (z +6.6) |
| `yingqing_0_111_111_t65-72_shift` | B | 27_yingqing_0_111_111 65.2–71.7 s | 33.8 / 17.1 | 30 / 8 | human steps; leg at limit 6%; outlier knee max (z +7.7) |
| `yingqing_0_1_1_t17-34` | A | 27_yingqing_0_1_1 16.8–33.6 s | 0.8 / 0.5 | 26 / 11 | elbow bend at limit 9% |
| `yingqing_0_1_1_t32-39_shift` | B | 27_yingqing_0_1_1 31.6–38.7 s | 11.9 / 6.5 | 24 / 11 | self-collision left_hand_collision / trunk_collision 0.4 s (at 6.0 s, 20 mm) |
| `yingqing_0_1_1_t54-62_shift` | B | 27_yingqing_0_1_1 54.0–62.1 s | 19.2 / 10.0 | 10 / 3 | outlier knee max (z +6.7) |
| `yingqing_0_2_2_t28-33_shift` | B | 27_yingqing_0_2_2 28.3–33.0 s | 11.5 / 6.0 | 24 / 7 | outlier knee max (z +4.0) |
| `yingqing_0_65_65_t0-8_shift` | B | 27_yingqing_0_65_65 0.0–7.6 s | 11.4 / 6.8 | 51 / 18 | knee 64 deg; elbow bend at limit 32%; outlier knee max (z +9.2) |
| `yingqing_0_65_65_t19-25_shift` | B | 27_yingqing_0_65_65 18.9–25.4 s | 14.9 / 7.4 | 39 / 11 | elbow bend at limit 11%; outlier knee max (z +3.6); hand presses into leg 29 mm for 0.2 s (at 0.0 s) |
| `yingqing_0_65_65_t23-38` | A | 27_yingqing_0_65_65 23.4–37.6 s | 2.7 / 2.6 | 48 / 16 | elbow bend at limit 7% |
| `yingqing_0_65_65_t6-15` | A | 27_yingqing_0_65_65 5.6–15.5 s | 1.7 / 0.5 | 45 / 14 | elbow bend at limit 16% |
| `yingqing_0_73_73_t13-26` | A | 27_yingqing_0_73_73 13.2–26.4 s | 1.4 / 0.3 | 21 / 8 | shoulder at limit 14% |
| `yingqing_0_73_73_t24-32_shift` | B | 27_yingqing_0_73_73 24.4–32.3 s | 21.6 / 11.4 | 41 / 8 | outlier knee max (z +6.9) |
| `yingqing_0_87_87_t42-50` | A | 27_yingqing_0_87_87 41.7–50.3 s | 5.5 / 1.2 | 20 / 7 | self-collision left_hand_end_collision / right_hand_collision 0.7 s (at 7.7 s, 16 mm) |
| `yingqing_0_87_87_t48-53_shift` | B | 27_yingqing_0_87_87 48.3–52.7 s | 11.6 / 8.4 | 16 / 11 | shoulder at limit 5%; outlier knee max (z +4.3); self-collision left_hand_end_collision / right_hand_collision 1.0 s (at 1.8 s, 16 mm) |
| `yingqing_0_87_87_t67-82` | A | 27_yingqing_0_87_87 67.0–82.4 s | 7.2 / 1.6 | 24 / 9 | hand presses into leg 30 mm for 1.6 s (at 0.0 s) |
| `yingqing_0_87_87_t80-89_shift` | B | 27_yingqing_0_87_87 80.4–88.7 s | 28.4 / 13.2 | 27 / 8 | human steps; outlier knee max (z +5.2); hand presses into leg 11 mm for 0.4 s (at 0.1 s) |
| `yingqing_0_95_95_t40-44_shift` | B | 27_yingqing_0_95_95 39.6–43.6 s | 24.2 / 12.7 | 46 / 15 | outlier knee max (z +5.7) |
| `yingqing_0_95_95_t54-68` | A | 27_yingqing_0_95_95 53.8–67.7 s | 1.0 / 0.5 | 42 / 13 | outlier trunk drop (z +3.8); outlier knee max (z +6.7) |
| `yingqing_0_9_9_t0-8_shift` | B | 27_yingqing_0_9_9 0.0–8.0 s | 23.0 / 12.7 | 27 / 9 | knee 63 deg; outlier knee max (z +8.9) |
| `yingqing_0_9_9_t33-39_shift` | B | 27_yingqing_0_9_9 33.0–39.2 s | 18.8 / 11.7 | 27 / 8 | outlier knee max (z +7.4) |
| `yingqing_0_9_9_t57-62_shift` | B | 27_yingqing_0_9_9 57.3–61.6 s | 8.7 / 5.9 | 37 / 8 | outlier knee max (z +4.6) |
| `yingqing_1_1_1_t146-150_shift` | B | 27_yingqing_1_1_1 145.5–150.1 s | 9.9 / 5.1 | 9 / 5 | outlier knee max (z +3.8); self-collision left_hand_end_collision / right_hand_end_collision 1.8 s (at 2.8 s, 17 mm) |
| `yingqing_1_1_1_t148-167` | A | 27_yingqing_1_1_1 148.1–167.5 s | 8.7 / 2.7 | 7 / 3 | self-collision left_hand_end_collision / right_hand_end_collision 11.4 s (at 0.2 s, 23 mm) |
| `yingqing_1_1_1_t221-229_shift` | B | 27_yingqing_1_1_1 221.1–228.6 s | 12.4 / 8.8 | 22 / 8 | outlier knee max (z +3.5) |
| `yingqing_1_1_1_t227-241` | A | 27_yingqing_1_1_1 226.6–240.5 s | 1.0 / 0.2 | 17 / 7 | shoulder at limit 15% |
| `yingqing_1_1_1_t24-29_shift` | B | 27_yingqing_1_1_1 24.1–28.6 s | 14.3 / 7.3 | 16 / 8 | outlier knee max (z +5.5) |
| `yingqing_1_1_1_t252-261_shift` | B | 27_yingqing_1_1_1 252.4–260.7 s | 14.0 / 11.5 | 27 / 9 | outlier knee max (z +7.7) |
| `yingqing_1_1_1_t269-273_shift` | B | 27_yingqing_1_1_1 268.7–273.2 s | 9.5 / 6.3 | 39 / 13 | elbow bend at limit 17%; outlier knee max (z +6.3); self-collision head_2_collision / right_hand_end_collision 1.4 s (at 3.0 s, 19 mm) |
| `yingqing_1_1_1_t271-286` | A | 27_yingqing_1_1_1 271.2–285.7 s | 1.0 / 0.3 | 17 / 7 | elbow bend at limit 5%; self-collision head_2_collision / right_hand_end_collision 2.3 s (at 0.6 s, 19 mm) |
| `yingqing_1_1_1_t31-35_shift` | B | 27_yingqing_1_1_1 30.7–35.0 s | 11.1 / 6.3 | 13 / 5 | outlier knee max (z +6.1) |
| `yingqing_1_1_1_t313-317_shift` | B | 27_yingqing_1_1_1 312.8–317.4 s | 15.1 / 8.8 | 24 / 9 | outlier knee max (z +5.4) |
| `yingqing_1_1_1_t348-353_shift` | B | 27_yingqing_1_1_1 348.0–353.3 s | 10.3 / 3.1 | 12 / 4 | outlier knee max (z +5.1); self-collision left_hand_end_collision / right_hand_end_collision 1.0 s (at 2.1 s, 17 mm) |
| `yingqing_1_1_1_t378-382_shift` | B | 27_yingqing_1_1_1 377.5–381.5 s | 10.2 / 1.8 | 28 / 7 | knee 64 deg; outlier knee max (z +9.3) |
| `yingqing_1_1_1_t385-389_shift` | B | 27_yingqing_1_1_1 384.9–389.4 s | 14.7 / 9.9 | 26 / 10 | outlier knee max (z +7.1) |
| `yingqing_1_1_1_t403-411_shift` | B | 27_yingqing_1_1_1 403.0–411.1 s | 14.3 / 11.2 | 13 / 4 | outlier knee max (z +7.7) |
| `yingqing_1_1_1_t417-421_shift` | B | 27_yingqing_1_1_1 416.5–421.2 s | 20.1 / 12.8 | 16 / 5 | shoulder at limit 47%; elbow bend at limit 26%; outlier knee max (z +5.8); self-collision left_hand_end_collision / trunk_collision 0.9 s (at 2.6 s, 21 mm) |
| `yingqing_1_1_1_t419-428` | A | 27_yingqing_1_1_1 419.2–428.3 s | 2.8 / 0.4 | 6 / 2 | shoulder at limit 89%; elbow bend at limit 16%; self-collision left_hand_end_collision / right_arm_3_collision 4.3 s (at 3.8 s, 8 mm) |
| `yingqing_1_1_1_t426-432_shift` | B | 27_yingqing_1_1_1 426.3–432.3 s | 16.7 / 13.4 | 17 / 5 | shoulder at limit 23%; elbow bend at limit 11%; outlier knee max (z +6.4); self-collision left_hand_end_collision / right_arm_3_collision 0.9 s (at 0.0 s, 8 mm) |
| `yingqing_1_1_1_t458-463_shift` | B | 27_yingqing_1_1_1 457.9–462.7 s | 17.5 / 8.5 | 42 / 11 | outlier knee max (z +4.6) |
| `yingqing_1_1_1_t48-62_shift` | B | 27_yingqing_1_1_1 47.9–61.5 s | 18.3 / 8.9 | 14 / 4 | outlier knee max (z +7.7) |
| `yingqing_1_1_1_t533-537_shift` | B | 27_yingqing_1_1_1 533.4–537.4 s | 21.7 / 11.2 | 10 / 4 | outlier knee max (z +5.2) |
| `yingqing_1_1_1_t547-552_shift` | B | 27_yingqing_1_1_1 547.3–552.3 s | 20.1 / 10.1 | 19 / 9 | outlier knee max (z +6.2) |
| `yingqing_1_1_1_t579-583_shift` | B | 27_yingqing_1_1_1 578.6–582.6 s | 25.0 / 13.6 | 15 / 6 | knee 62 deg; outlier knee max (z +8.7) |
| `yingqing_1_1_1_t590-595_shift` | B | 27_yingqing_1_1_1 590.3–594.8 s | 12.0 / 8.3 | 24 / 7 | outlier knee max (z +7.5) |
| `yingqing_1_1_1_t67-72` | A | 27_yingqing_1_1_1 66.8–71.9 s | 8.6 / 6.1 | 20 / 6 | outlier knee max (z +4.7) |
| `yingqing_1_1_1_t70-74_shift` | B | 27_yingqing_1_1_1 69.9–74.3 s | 15.8 / 9.0 | 16 / 7 | outlier knee max (z +5.0) |
| `yingqing_1_1_1_t85-99` | A | 27_yingqing_1_1_1 85.3–98.5 s | 9.7 / 2.1 | 15 / 5 | outlier knee max (z +5.5) |
| `yingqing_1_2_2_t0-4_shift` | B | 27_yingqing_1_2_2 0.0–4.0 s | 23.3 / 11.7 | 15 / 6 | outlier knee max (z +5.8) |
| `yingqing_1_2_2_t160-164_shift` | B | 27_yingqing_1_2_2 159.6–164.0 s | 7.5 / 4.6 | 25 / 8 | outlier knee max (z +4.7) |
| `yingqing_1_2_2_t177-182_shift` | B | 27_yingqing_1_2_2 177.0–181.7 s | 24.8 / 15.7 | 11 / 3 | outlier knee max (z +6.8) |
| `yingqing_1_2_2_t245-250_shift` | B | 27_yingqing_1_2_2 245.4–249.8 s | 12.8 / 7.1 | 21 / 8 | outlier knee max (z +6.2) |
| `yingqing_1_2_2_t262-267_shift` | B | 27_yingqing_1_2_2 262.0–266.6 s | 21.8 / 12.4 | 17 / 6 | outlier knee max (z +7.4) |
| `yingqing_1_2_2_t283-298` | A | 27_yingqing_1_2_2 282.8–297.7 s | 1.1 / 0.3 | 16 / 7 | self-collision left_hand_end_collision / right_hand_end_collision 0.9 s (at 4.6 s, 7 mm) |
| `yingqing_1_2_2_t357-368` | A | 27_yingqing_1_2_2 356.7–367.9 s | 0.6 / 0.4 | 7 / 3 | self-collision left_hand_end_collision / right_hand_end_collision 3.0 s (at 8.2 s, 17 mm) |
| `yingqing_1_2_2_t393-397_shift` | B | 27_yingqing_1_2_2 392.6–397.0 s | 9.7 / 5.9 | 14 / 5 | outlier knee max (z +7.6) |
| `yingqing_1_2_2_t458-462_shift` | B | 27_yingqing_1_2_2 458.0–462.5 s | 13.4 / 8.5 | 20 / 5 | outlier knee max (z +5.5) |
| `yingqing_1_2_2_t471-475_shift` | B | 27_yingqing_1_2_2 470.9–475.4 s | 14.6 / 9.5 | 13 / 3 | outlier knee max (z +6.7) |
| `yingqing_1_2_2_t481-485_shift` | B | 27_yingqing_1_2_2 480.8–484.8 s | 14.6 / 8.3 | 16 / 6 | outlier knee max (z +4.5); self-collision left_hand_end_collision / right_hand_end_collision 2.3 s (at 1.7 s, 12 mm) |
| `yingqing_1_2_2_t482-496` | A | 27_yingqing_1_2_2 482.1–496.2 s | 2.1 / 0.6 | 15 / 5 | self-collision left_hand_end_collision / right_hand_end_collision 4.2 s (at 0.5 s, 12 mm) |
| `yingqing_1_2_2_t561-566` | A | 27_yingqing_1_2_2 561.2–565.6 s | 1.7 / 0.7 | 30 / 9 | shoulder at limit 6%; self-collision left_hand_end_collision / waist_collision 1.4 s (at 0.0 s, 25 mm); hand presses into leg 30 mm for 1.4 s (at 0.0 s) |
| `yingqing_1_2_2_t72-76_shift` | B | 27_yingqing_1_2_2 71.7–76.1 s | 7.0 / 1.9 | 20 / 7 | leg at limit 38%; outlier knee max (z +6.3) |
| `yingqing_1_2_2_t90-101` | A | 27_yingqing_1_2_2 89.8–101.1 s | 0.6 / 0.4 | 21 / 6 | self-collision left_hand_end_collision / right_hand_end_collision 0.2 s (at 6.6 s, 8 mm) |
| `yingqing_1_3_3_t135-141_shift` | B | 27_yingqing_1_3_3 135.3–140.7 s | 15.4 / 9.9 | 30 / 10 | outlier knee max (z +6.2) |
| `yingqing_1_3_3_t147-151_shift` | B | 27_yingqing_1_3_3 146.6–151.1 s | 13.3 / 7.9 | 22 / 6 | outlier knee max (z +4.4) |
| `yingqing_1_3_3_t17-21_shift` | B | 27_yingqing_1_3_3 16.9–21.5 s | 15.4 / 11.0 | 16 / 5 | outlier knee max (z +6.9) |
| `yingqing_1_3_3_t238-244_shift` | B | 27_yingqing_1_3_3 237.5–244.1 s | 20.2 / 9.3 | 34 / 11 | outlier knee max (z +7.0) |
| `yingqing_1_3_3_t338-347_shift` | B | 27_yingqing_1_3_3 338.3–347.1 s | 18.6 / 9.8 | 18 / 7 | outlier knee max (z +6.3) |
| `yingqing_1_3_3_t356-363_shift` | B | 27_yingqing_1_3_3 356.1–363.1 s | 16.6 / 8.3 | 14 / 4 | outlier knee max (z +4.1) |
| `yingqing_1_3_3_t37-41_shift` | B | 27_yingqing_1_3_3 37.1–41.1 s | 25.4 / 13.3 | 13 / 4 | human steps; outlier knee max (z +7.3) |
| `yingqing_1_3_3_t381-386_shift` | B | 27_yingqing_1_3_3 380.9–386.0 s | 19.1 / 10.4 | 16 / 6 | outlier knee max (z +4.7) |
| `yingqing_1_3_3_t401-407_shift` | B | 27_yingqing_1_3_3 400.9–406.9 s | 24.8 / 13.2 | 49 / 12 | outlier knee max (z +5.8) |
| `yingqing_1_3_3_t497-501_shift` | B | 27_yingqing_1_3_3 497.0–501.0 s | 15.3 / 12.1 | 20 / 9 | outlier knee max (z +5.9) |
| `yingqing_1_3_3_t517-521` | A | 27_yingqing_1_3_3 516.7–520.9 s | 5.1 / 1.4 | 2 / 2 | shoulder at limit 86%; left arm behind body 10 cm (human's in front) |
| `yingqing_1_3_3_t542-548_shift` | B | 27_yingqing_1_3_3 541.9–548.2 s | 23.8 / 15.3 | 36 / 13 | knee 72 deg; shoulder at limit 31%; outlier knee max (z +12.0) |
| `yingqing_1_3_3_t570-574_shift` | B | 27_yingqing_1_3_3 570.2–574.2 s | 9.3 / 1.9 | 47 / 13 | outlier knee max (z +5.5) |
| `yingqing_1_3_3_t60-70_shift` | B | 27_yingqing_1_3_3 59.5–70.1 s | 12.9 / 3.3 | 16 / 6 | outlier knee max (z +7.0) |
| `yingqing_1_3_3_t81-100` | A | 27_yingqing_1_3_3 80.9–100.0 s | 6.8 / 1.4 | 14 / 6 | shoulder at limit 6% |
| `zhao_0_104_104_t4-10_shift` | B | 12_zhao_0_104_104 4.0–10.2 s | 22.0 / 13.8 | 55 / 14 | head at limit 8%; outlier knee max (z +6.0) |
| `zhao_0_104_104_t49-54_shift` | B | 12_zhao_0_104_104 49.4–54.1 s | 20.7 / 14.3 | 43 / 16 | outlier knee max (z +6.4) |
| `zhao_0_104_104_t64-74_shift` | B | 12_zhao_0_104_104 63.9–74.2 s | 19.9 / 11.5 | 38 / 12 | outlier knee max (z +5.0) |
| `zhao_0_10_10_t0-6` | A | 12_zhao_0_10_10 0.0–5.6 s | 9.0 / 4.9 | 43 / 10 | leg at limit 7% |
| `zhao_0_10_10_t11-15_shift` | B | 12_zhao_0_10_10 11.0–15.0 s | 14.9 / 7.5 | 41 / 10 | outlier knee max (z +4.2) |
| `zhao_0_10_10_t4-10_shift` | B | 12_zhao_0_10_10 3.6–9.8 s | 18.9 / 8.9 | 50 / 11 | leg at limit 6%; outlier knee max (z +4.5) |
| `zhao_0_10_10_t40-44_shift` | B | 12_zhao_0_10_10 40.0–44.0 s | 22.1 / 12.5 | 75 / 22 | shoulder at limit 18%; outlier arms k1 cm (z +4.1); outlier knee max (z +4.3) |
| `zhao_0_10_10_t48-53_shift` | B | 12_zhao_0_10_10 48.2–53.2 s | 17.9 / 9.8 | 68 / 14 | leg at limit 11% |
| `zhao_0_12_12_t44-58` | A | 12_zhao_0_12_12 44.2–57.8 s | 10.0 / 5.0 | 51 / 13 | shoulder at limit 7% |
| `zhao_0_12_12_t67-74_shift` | B | 12_zhao_0_12_12 66.9–74.4 s | 22.5 / 13.1 | 85 / 26 | outlier arms k1 cm (z +5.3); outlier trunk drop (z +3.8); outlier knee max (z +4.2) |
| `zhao_0_12_12_t72-77` | A | 12_zhao_0_12_12 72.4–77.3 s | 8.4 / 4.6 | 95 / 28 | outlier arms k1 cm (z +5.8); outlier knee max (z +4.2) |
| `zhao_0_12_12_t78-82_shift` | B | 12_zhao_0_12_12 78.3–82.3 s | 18.1 / 8.8 | 73 / 18 | shoulder at limit 13% |
| `zhao_0_13_13_t41-45` | A | 12_zhao_0_13_13 40.7–44.7 s | 7.3 / 3.8 | 105 / 27 | leg at limit 6%; outlier arms k1 cm (z +5.4) |
| `zhao_0_13_13_t61-65_shift` | B | 12_zhao_0_13_13 60.5–65.4 s | 14.6 / 4.2 | 80 / 22 | outlier arms k1 cm (z +4.1); outlier knee max (z +4.6) |
| `zhao_0_14_14_t18-27_shift` | B | 12_zhao_0_14_14 17.7–26.9 s | 19.1 / 13.8 | 85 / 22 | elbow bend at limit 10%; outlier arms k1 cm (z +4.0); outlier knee max (z +5.9) |
| `zhao_0_14_14_t28-38_shift` | B | 12_zhao_0_14_14 28.3–38.5 s | 23.4 / 12.9 | 70 / 19 | knee 61 deg; outlier knee max (z +8.4) |
| `zhao_0_14_14_t40-45_shift` | B | 12_zhao_0_14_14 39.8–44.7 s | 20.1 / 11.5 | 66 / 18 | outlier knee max (z +5.8) |
| `zhao_0_14_14_t46-51_shift` | B | 12_zhao_0_14_14 46.0–50.9 s | 21.3 / 11.1 | 76 / 18 | outlier knee max (z +4.8) |
| `zhao_0_14_14_t8-13` | A | 12_zhao_0_14_14 7.5–13.1 s | 1.2 / 0.5 | 48 / 12 | leg at limit 8% |
| `zhao_0_15_15_t28-33_shift` | B | 12_zhao_0_15_15 28.1–33.4 s | 18.3 / 10.0 | 85 / 21 | outlier arms k1 cm (z +3.9); outlier knee max (z +5.7) |
| `zhao_0_15_15_t50-59_shift` | B | 12_zhao_0_15_15 50.4–59.0 s | 23.6 / 13.6 | 38 / 11 | outlier knee max (z +4.2); self-collision left_hand_collision / trunk_collision 0.8 s (at 4.9 s, 10 mm) |
| `zhao_0_15_15_t86-100_shift` | B | 12_zhao_0_15_15 86.1–99.8 s | 20.7 / 11.0 | 60 / 15 | outlier knee max (z +3.8) |
| `zhao_0_16_16_t26-32` | A | 12_zhao_0_16_16 25.5–31.8 s | 8.3 / 4.1 | 83 / 23 | shoulder at limit 5%; outlier arms k1 cm (z +4.4) |
| `zhao_0_16_16_t79-83_shift` | B | 12_zhao_0_16_16 79.5–83.5 s | 16.7 / 10.9 | 67 / 12 | leg at limit 9%; hand presses into leg 14 mm for 0.2 s (at 0.5 s) |
| `zhao_0_16_16_t81-86` | A | 12_zhao_0_16_16 80.9–85.8 s | 4.4 / 1.7 | 70 / 13 | leg at limit 7% |
| `zhao_0_2_2_t4-10_shift` | B | 12_zhao_0_2_2 4.2–10.3 s | 24.9 / 14.9 | 33 / 9 | outlier knee max (z +6.4) |
| `zhao_0_2_2_t42-50_shift` | B | 12_zhao_0_2_2 42.2–49.9 s | 19.1 / 10.8 | 44 / 12 | outlier knee max (z +5.3) |
| `zhao_0_3_3_t26-32_shift` | B | 12_zhao_0_3_3 26.4–31.5 s | 21.8 / 12.3 | 35 / 9 | outlier knee max (z +4.6) |
| `zhao_0_3_3_t40-47_shift` | B | 12_zhao_0_3_3 39.9–46.6 s | 25.1 / 12.2 | 80 / 22 | human steps; outlier arms k1 cm (z +4.2); outlier knee max (z +3.6) |
| `zhao_0_3_3_t68-76_shift` | B | 12_zhao_0_3_3 67.9–75.9 s | 21.6 / 13.8 | 64 / 16 | shoulder at limit 6%; outlier knee max (z +4.2) |
| `zhao_0_4_4_t15-20_shift` | B | 12_zhao_0_4_4 15.0–19.9 s | 13.3 / 4.9 | 64 / 20 | outlier arms k1 cm (z +3.5) |
| `zhao_0_4_4_t26-37_shift` | B | 12_zhao_0_4_4 25.6–37.4 s | 24.0 / 13.4 | 33 / 9 | outlier knee max (z +5.6) |
| `zhao_0_4_4_t3-15_shift` | B | 12_zhao_0_4_4 3.1–14.9 s | 22.5 / 12.7 | 48 / 11 | outlier knee max (z +6.0) |
| `zhao_0_4_4_t56-72_shift` | B | 12_zhao_0_4_4 55.6–72.1 s | 23.1 / 13.1 | 42 / 11 | outlier knee max (z +3.6) |
| `zhao_0_5_5_t17-25_shift` | B | 12_zhao_0_5_5 16.9–24.6 s | 22.3 / 12.6 | 22 / 6 | outlier knee max (z +5.6) |
| `zhao_0_5_5_t39-44_shift` | B | 12_zhao_0_5_5 39.4–43.8 s | 21.8 / 12.6 | 63 / 17 | outlier knee max (z +4.0) |
| `zhao_0_5_5_t70-75_shift` | B | 12_zhao_0_5_5 69.8–74.9 s | 23.4 / 12.6 | 51 / 14 | outlier knee max (z +5.5) |
| `zhao_0_5_5_t83-88_shift` | B | 12_zhao_0_5_5 83.0–87.8 s | 23.2 / 12.0 | 47 / 12 | outlier knee max (z +4.3) |
| `zhao_0_65_65_t15-29_shift` | B | 12_zhao_0_65_65 15.4–29.1 s | 24.2 / 15.1 | 54 / 14 | knee 64 deg; head at limit 7%; outlier knee max (z +9.3); hand presses into leg 20 mm for 0.8 s (at 9.1 s) |
| `zhao_0_66_66_t42-46_shift` | B | 12_zhao_0_66_66 42.2–46.5 s | 18.8 / 11.3 | 61 / 13 | head at limit 22%; shoulder at limit 6% |
| `zhao_0_6_6_t55-60` | A | 12_zhao_0_6_6 55.0–60.3 s | 5.2 / 1.3 | 46 / 13 | shoulder at limit 5% |
| `zhao_0_7_7_t23-38` | A | 12_zhao_0_7_7 22.9–38.2 s | 10.9 / 4.6 | 54 / 14 | human steps |
| `zhao_0_81_81_t27-33` | A | 12_zhao_0_81_81 27.1–33.2 s | 5.9 / 1.8 | 29 / 8 | self-collision left_hand_collision / trunk_collision 0.3 s (at 0.0 s, 17 mm) |
| `zhao_0_81_81_t4-10` | A | 12_zhao_0_81_81 4.4–10.2 s | 9.3 / 5.2 | 37 / 10 | self-collision left_hand_collision / trunk_collision 1.4 s (at 0.0 s, 23 mm) |
| `zhao_0_81_81_t68-79` | A | 12_zhao_0_81_81 67.6–79.4 s | 7.3 / 1.8 | 23 / 6 | hand presses into leg 31 mm for 1.4 s (at 8.8 s) |
| `zhao_0_81_81_t77-81_shift` | B | 12_zhao_0_81_81 76.8–80.8 s | 23.0 / 13.7 | 15 / 4 | outlier knee max (z +5.1); hand presses into leg 30 mm for 1.1 s (at 0.0 s) |
| `zhao_0_82_82_t17-24` | A | 12_zhao_0_82_82 17.3–24.0 s | 6.3 / 3.9 | 30 / 8 | hand presses into leg 31 mm for 1.3 s (at 4.9 s) |
| `zhao_0_82_82_t29-37_shift` | B | 12_zhao_0_82_82 29.0–37.3 s | 16.2 / 9.2 | 39 / 10 | outlier knee max (z +3.9); hand presses into leg 17 mm for 0.6 s (at 0.9 s) |
| `zhao_0_82_82_t44-53_shift` | B | 12_zhao_0_82_82 43.9–53.4 s | 25.0 / 16.0 | 49 / 13 | shoulder at limit 8% |
| `zhao_0_82_82_t70-75` | A | 12_zhao_0_82_82 70.3–75.3 s | 0.9 / 0.7 | 51 / 15 | hand presses into leg 22 mm for 0.3 s (at 3.5 s) |
| `zhao_0_82_82_t79-84` | A | 12_zhao_0_82_82 79.2–83.9 s | 2.5 / 0.9 | 33 / 8 | self-collision left_hand_collision / trunk_collision 0.3 s (at 2.4 s, 8 mm) |
| `zhao_0_87_87_t41-45_shift` | B | 12_zhao_0_87_87 40.6–45.0 s | 21.0 / 15.0 | 31 / 9 | outlier knee max (z +4.6); self-collision left_hand_collision / trunk_collision 0.2 s (at 2.7 s, 14 mm) |
| `zhao_0_87_87_t63-73_shift` | B | 12_zhao_0_87_87 63.3–73.2 s | 25.0 / 13.4 | 88 / 24 | outlier arms k1 cm (z +4.8); outlier knee max (z +6.7) |
| `zhao_0_88_88_t24-29_shift` | B | 12_zhao_0_88_88 24.3–28.6 s | 17.9 / 11.1 | 55 / 14 | outlier knee max (z +3.8) |
| `zhao_0_88_88_t37-42_shift` | B | 12_zhao_0_88_88 36.9–42.1 s | 21.6 / 12.7 | 61 / 20 | shoulder at limit 9%; outlier trunk drop (z +4.4); outlier knee max (z +4.7) |
| `zhao_0_88_88_t49-56_shift` | B | 12_zhao_0_88_88 49.2–56.2 s | 21.5 / 12.8 | 62 / 15 | head at limit 10%; outlier knee max (z +7.1) |
| `zhao_0_88_88_t74-80_shift` | B | 12_zhao_0_88_88 74.1–79.8 s | 15.6 / 7.7 | 81 / 29 | head at limit 7%; shoulder at limit 9%; outlier arms k1 cm (z +6.0); outlier trunk drop (z +3.8); outlier knee max (z +5.8) |
| `zhao_0_8_8_t0-6_shift` | B | 12_zhao_0_8_8 0.0–5.7 s | 18.4 / 9.5 | 50 / 12 | outlier knee max (z +4.0) |
| `zhao_0_96_96_t27-32` | A | 12_zhao_0_96_96 27.2–32.3 s | 5.1 / 1.7 | 84 / 27 | head at limit 25%; outlier arms k1 cm (z +5.6) |
| `zhao_0_96_96_t35-40_shift` | B | 12_zhao_0_96_96 34.8–39.9 s | 11.7 / 6.1 | 84 / 24 | head at limit 25%; outlier arms k1 cm (z +4.5) |
| `zhao_0_96_96_t41-48` | A | 12_zhao_0_96_96 41.5–47.8 s | 4.8 / 1.5 | 74 / 23 | head at limit 26%; outlier arms k1 cm (z +4.5) |
| `zhao_0_9_9_t24-28_shift` | B | 12_zhao_0_9_9 23.6–28.3 s | 19.0 / 9.8 | 72 / 20 | shoulder at limit 9%; leg at limit 9%; outlier arms k1 cm (z +3.7); outlier knee max (z +6.3) |
| `zhao_0_9_9_t30-34` | A | 12_zhao_0_9_9 29.6–34.4 s | 8.6 / 3.8 | 58 / 15 | leg at limit 8% |
| `zhao_0_9_9_t42-46_shift` | B | 12_zhao_0_9_9 41.5–45.6 s | 18.3 / 10.9 | 56 / 13 | shoulder at limit 6%; outlier knee max (z +4.1) |
| `zhao_0_9_9_t49-61_shift` | B | 12_zhao_0_9_9 48.9–60.7 s | 21.1 / 11.1 | 61 / 17 | leg at limit 6%; outlier knee max (z +4.3) |
| `zhao_0_9_9_t59-64` | A | 12_zhao_0_9_9 58.7–64.1 s | 6.8 / 0.9 | 54 / 14 | leg at limit 6% |
| `zhao_1_1_1_t102-108_shift` | B | 12_zhao_1_1_1 101.6–107.6 s | 14.3 / 6.0 | 53 / 13 | shoulder at limit 33% |
| `zhao_1_1_1_t110-118` | A | 12_zhao_1_1_1 109.5–118.4 s | 5.6 / 4.2 | 35 / 11 | shoulder at limit 30% |
| `zhao_1_1_1_t116-126_shift` | B | 12_zhao_1_1_1 116.4–126.0 s | 19.7 / 11.9 | 48 / 12 | shoulder at limit 45% |
| `zhao_1_1_1_t151-160_shift` | B | 12_zhao_1_1_1 151.5–159.8 s | 13.5 / 8.7 | 38 / 9 | shoulder at limit 33% |
| `zhao_1_1_1_t153-157` | A | 12_zhao_1_1_1 152.8–157.5 s | 4.7 / 1.0 | 39 / 10 | shoulder at limit 9% |
| `zhao_1_1_1_t165-170_shift` | B | 12_zhao_1_1_1 164.8–169.7 s | 17.7 / 11.1 | 24 / 5 | outlier knee max (z +4.2) |
| `zhao_1_1_1_t26-30_shift` | B | 12_zhao_1_1_1 26.5–30.5 s | 1.0 / 0.5 | 30 / 7 | shoulder at limit 50% |
| `zhao_1_1_1_t272-278` | A | 12_zhao_1_1_1 272.2–278.4 s | 2.8 / 1.7 | 52 / 14 | shoulder at limit 77% |
| `zhao_1_1_1_t276-289_shift` | B | 12_zhao_1_1_1 276.4–289.1 s | 17.1 / 11.9 | 44 / 12 | shoulder at limit 61% |
| `zhao_1_1_1_t318-322_shift` | B | 12_zhao_1_1_1 318.2–322.2 s | 18.1 / 11.9 | 20 / 6 | outlier knee max (z +5.5) |
| `zhao_1_1_1_t339-351_shift` | B | 12_zhao_1_1_1 339.1–351.3 s | 18.9 / 11.6 | 25 / 8 | outlier knee max (z +4.1) |
| `zhao_1_1_1_t356-361` | A | 12_zhao_1_1_1 356.1–360.8 s | 9.7 / 5.0 | 40 / 13 | shoulder at limit 6% |
| `zhao_1_1_1_t359-369_shift` | B | 12_zhao_1_1_1 358.8–369.2 s | 26.2 / 14.1 | 38 / 13 | human steps; shoulder at limit 7%; outlier knee max (z +6.4) |
| `zhao_1_1_1_t409-415` | A | 12_zhao_1_1_1 409.1–414.9 s | 2.6 / 1.8 | 18 / 6 | shoulder at limit 38% |
| `zhao_1_1_1_t416-420` | A | 12_zhao_1_1_1 416.3–420.3 s | 1.3 / 1.0 | 29 / 11 | shoulder at limit 22% |
| `zhao_1_1_1_t423-437` | A | 12_zhao_1_1_1 423.2–437.1 s | 4.6 / 2.3 | 55 / 14 | shoulder at limit 28% |
| `zhao_1_1_1_t460-466_shift` | B | 12_zhao_1_1_1 459.7–465.9 s | 17.3 / 8.8 | 46 / 15 | shoulder at limit 42% |
| `zhao_1_1_1_t464-471` | A | 12_zhao_1_1_1 463.9–470.8 s | 2.1 / 1.2 | 35 / 11 | shoulder at limit 85% |
| `zhao_1_1_1_t469-474_shift` | B | 12_zhao_1_1_1 468.8–473.8 s | 18.6 / 10.2 | 60 / 17 | shoulder at limit 89%; outlier knee max (z +4.8) |
| `zhao_1_1_1_t476-487_shift` | B | 12_zhao_1_1_1 476.4–486.8 s | 20.0 / 12.4 | 21 / 5 | outlier knee max (z +5.9) |
| `zhao_1_1_1_t487-497_shift` | B | 12_zhao_1_1_1 486.8–497.3 s | 23.7 / 15.0 | 12 / 3 | outlier knee max (z +4.3) |
| `zhao_1_1_1_t499-503_shift` | B | 12_zhao_1_1_1 498.6–503.1 s | 13.6 / 7.3 | 8 / 2 | outlier knee max (z +3.9) |
| `zhao_1_1_1_t548-553_shift` | B | 12_zhao_1_1_1 547.7–552.8 s | 21.8 / 14.4 | 58 / 13 | shoulder at limit 20% |
| `zhao_1_1_1_t554-559_shift` | B | 12_zhao_1_1_1 554.1–558.6 s | 18.5 / 11.8 | 57 / 13 | outlier knee max (z +4.1) |
| `zhao_1_1_1_t574-582_shift` | B | 12_zhao_1_1_1 574.1–581.6 s | 20.5 / 11.5 | 39 / 10 | outlier knee max (z +6.9) |
| `zhao_1_2_2_t252-256_shift` | B | 12_zhao_1_2_2 252.4–256.4 s | 29.7 / 17.7 | 31 / 7 | human steps; outlier knee max (z +6.1) |
| `zhao_1_2_2_t392-397_shift` | B | 12_zhao_1_2_2 391.6–396.7 s | 12.8 / 6.8 | 25 / 6 | outlier knee max (z +5.7) |
| `zhao_1_2_2_t446-450_shift` | B | 12_zhao_1_2_2 445.8–450.5 s | 15.6 / 11.7 | 24 / 5 | outlier knee max (z +4.6) |
| `zhao_1_2_2_t498-503` | A | 12_zhao_1_2_2 497.9–503.2 s | 6.3 / 1.9 | 61 / 19 | shoulder at limit 7% |
| `zhao_1_2_2_t501-506_shift` | B | 12_zhao_1_2_2 501.2–505.6 s | 13.7 / 9.1 | 54 / 13 | outlier knee max (z +4.1) |
| `zhao_1_2_2_t509-518_shift` | B | 12_zhao_1_2_2 509.2–517.6 s | 23.4 / 14.9 | 36 / 10 | outlier knee max (z +5.6) |
| `zhao_1_2_2_t538-543_shift` | B | 12_zhao_1_2_2 538.3–542.9 s | 11.6 / 9.0 | 28 / 7 | outlier knee max (z +5.1) |
| `zhao_1_2_2_t556-560_shift` | B | 12_zhao_1_2_2 555.8–559.8 s | 19.6 / 12.1 | 25 / 7 | outlier knee max (z +3.6) |
| `zhao_1_3_3_t125-129_shift` | B | 12_zhao_1_3_3 124.6–128.6 s | 14.9 / 10.0 | 47 / 9 | outlier knee max (z +4.0) |
| `zhao_1_3_3_t132-141_shift` | B | 12_zhao_1_3_3 131.9–140.6 s | 22.5 / 13.2 | 46 / 10 | outlier knee max (z +6.2) |
| `zhao_1_3_3_t161-165_shift` | B | 12_zhao_1_3_3 160.6–164.6 s | 26.3 / 14.2 | 9 / 2 | human steps; outlier knee max (z +5.0) |
| `zhao_1_3_3_t199-203_shift` | B | 12_zhao_1_3_3 198.7–202.7 s | 23.7 / 12.7 | 28 / 10 | shoulder at limit 18% |
| `zhao_1_3_3_t200-211` | A | 12_zhao_1_3_3 200.1–211.3 s | 5.3 / 1.0 | 67 / 21 | outlier arms k1 cm (z +4.0) |
| `zhao_1_3_3_t209-215_shift` | B | 12_zhao_1_3_3 209.3–215.3 s | 24.5 / 15.6 | 43 / 12 | outlier knee max (z +5.2) |
| `zhao_1_3_3_t216-220_shift` | B | 12_zhao_1_3_3 216.3–220.3 s | 23.7 / 14.2 | 15 / 4 | outlier knee max (z +4.4) |
| `zhao_1_3_3_t233-240_shift` | B | 12_zhao_1_3_3 232.7–239.7 s | 22.8 / 10.9 | 27 / 7 | outlier knee max (z +5.1) |
| `zhao_1_3_3_t286-297` | A | 12_zhao_1_3_3 285.6–296.8 s | 9.8 / 6.6 | 54 / 16 | shoulder at limit 9% |
| `zhao_1_3_3_t295-310_shift` | B | 12_zhao_1_3_3 294.8–310.3 s | 26.9 / 15.3 | 28 / 8 | human steps; outlier knee max (z +5.1) |
| `zhao_1_3_3_t312-316_shift` | B | 12_zhao_1_3_3 312.0–316.0 s | 25.0 / 13.1 | 32 / 8 | human steps; outlier knee max (z +5.4) |
| `zhao_1_3_3_t320-330_shift` | B | 12_zhao_1_3_3 320.0–330.0 s | 17.1 / 9.7 | 35 / 8 | outlier knee max (z +6.1) |
| `zhao_1_3_3_t333-338_shift` | B | 12_zhao_1_3_3 333.4–338.2 s | 22.7 / 15.9 | 22 / 5 | knee 60 deg; outlier knee max (z +8.1) |
| `zhao_1_3_3_t360-367_shift` | B | 12_zhao_1_3_3 360.0–366.6 s | 25.9 / 15.2 | 27 / 6 | human steps |
| `zhao_1_3_3_t432-442_shift` | B | 12_zhao_1_3_3 432.2–441.8 s | 14.9 / 8.8 | 32 / 6 | outlier knee max (z +3.7) |
| `zhao_1_3_3_t600-604_shift` | B | 12_zhao_1_3_3 600.2–604.3 s | 20.1 / 11.6 | 45 / 11 | outlier knee max (z +3.5) |
