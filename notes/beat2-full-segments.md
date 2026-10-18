# BEAT2 Segments (human side)

Generated 2026-10-18 by `tools/beat2_segments.py` from `tools/datasets/beat2_full.toml`. Human motion only (before GMR).

- **Tier A:** maximal stretches with both ankles within 10 cm of their median spot, starting and ending on planted frames (ankles < 0.1 m/s), cut into 4–20 s clips.
- **Tier B:** foot shifts inside 25 cm stretches that Tier A leaves out, each with 2 s of standing on either side (so B overlaps A by its padding), same clip lengths. Names end in `_shift`.
- **Rejected:** share of the take's time in no clip (A only, or A + B), i.e. lost to stepping or walking.
- **A min / B min** add clip lengths; B's include the padding that A also covers.

## Training speakers

### `train` takes

| speaker | takes | minutes | A clips | A min | rejected (A) | B clips | B min | rejected (A+B) |
|---|---|---|---|---|---|---|---|---|
| 1_wayne | 95 | 90.0 | 444 | 77.9 | 14% | 289 | 26.1 | 4% |
| 2_scott | 95 | 87.2 | 124 | 11.6 | 87% | 195 | 18.6 | 70% |
| 3_solomon | 95 | 99.7 | 399 | 90.0 | 10% | 158 | 16.8 | 2% |
| 4_lawrence | 95 | 105.7 | 535 | 78.6 | 26% | 430 | 43.1 | 7% |
| 5_stewart | 7 | 7.2 | 25 | 5.1 | 29% | 13 | 1.3 | 19% |
| 6_carla | 63 | 49.3 | 290 | 35.9 | 27% | 162 | 13.3 | 15% |
| 7_sophie | 95 | 85.6 | 312 | 84.3 | 1% | 45 | 3.5 | 0% |
| 9_miranda | 95 | 81.2 | 304 | 79.4 | 2% | 49 | 3.9 | 1% |
| 10_kieks | 7 | 6.8 | 25 | 6.8 | 0% | 2 | 0.1 | 0% |
| 12_zhao | 19 | 25.5 | 69 | 9.8 | 61% | 85 | 10.1 | 32% |
| 13_lu | 19 | 23.5 | 107 | 18.3 | 22% | 85 | 9.0 | 3% |
| 15_carlos | 17 | 21.0 | 82 | 20.0 | 4% | 20 | 2.1 | 0% |
| 16_jorge | 19 | 17.9 | 0 | 0.0 | 100% | 19 | 2.3 | 87% |
| 17_itoi | 19 | 26.1 | 89 | 17.8 | 32% | 65 | 8.2 | 10% |
| 18_daiki | 19 | 26.9 | 98 | 25.6 | 5% | 25 | 2.5 | 1% |
| 22_luqi | 13 | 16.2 | 93 | 10.2 | 37% | 31 | 3.3 | 26% |
| 23_hailing | 18 | 24.9 | 93 | 24.1 | 3% | 21 | 1.8 | 1% |
| 24_kexin | 19 | 25.6 | 88 | 25.6 | 0% | 1 | 0.1 | 0% |
| 25_goto | 18 | 29.0 | 95 | 29.0 | 0% | 0 | 0.0 | 0% |
| 28_tiffnay | 19 | 24.7 | 88 | 23.9 | 3% | 14 | 1.3 | 1% |
| 30_katya | 19 | 24.9 | 91 | 24.5 | 1% | 15 | 1.3 | 0% |
| **total** | 865 | 899.0 | 3451 | 698.6 | 22% | 1724 | 168.8 | 13% |

### `val` takes

| speaker | takes | minutes | A clips | A min | rejected (A) | B clips | B min | rejected (A+B) |
|---|---|---|---|---|---|---|---|---|
| 1_wayne | 8 | 9.1 | 44 | 7.8 | 15% | 35 | 3.3 | 1% |
| 2_scott | 8 | 9.5 | 19 | 1.8 | 81% | 31 | 4.3 | 43% |
| 3_solomon | 8 | 10.7 | 24 | 2.8 | 74% | 44 | 6.5 | 25% |
| 4_lawrence | 8 | 11.0 | 54 | 6.7 | 39% | 52 | 5.5 | 15% |
| 5_stewart | 8 | 8.9 | 30 | 8.8 | 1% | 1 | 0.1 | 0% |
| 7_sophie | 8 | 8.6 | 29 | 8.5 | 1% | 3 | 0.2 | 0% |
| 9_miranda | 8 | 8.3 | 29 | 8.2 | 1% | 3 | 0.2 | 0% |
| 10_kieks | 8 | 8.7 | 29 | 8.6 | 2% | 2 | 0.2 | 0% |
| 12_zhao | 2 | 2.2 | 5 | 0.5 | 79% | 9 | 0.8 | 50% |
| 13_lu | 2 | 2.1 | 9 | 1.9 | 6% | 6 | 0.5 | 0% |
| 15_carlos | 2 | 2.1 | 9 | 1.9 | 9% | 4 | 0.3 | 4% |
| 16_jorge | 2 | 1.6 | 0 | 0.0 | 100% | 2 | 0.1 | 91% |
| 17_itoi | 2 | 2.4 | 8 | 2.3 | 5% | 2 | 0.2 | 2% |
| 18_daiki | 2 | 2.2 | 9 | 2.0 | 11% | 4 | 0.5 | 2% |
| 23_hailing | 2 | 2.4 | 8 | 2.4 | 0% | 0 | 0.0 | 0% |
| 24_kexin | 2 | 2.2 | 8 | 2.2 | 0% | 0 | 0.0 | 0% |
| 25_goto | 2 | 3.2 | 11 | 3.2 | 0% | 0 | 0.0 | 0% |
| 28_tiffnay | 2 | 2.2 | 10 | 2.0 | 7% | 4 | 0.4 | 0% |
| 30_katya | 2 | 2.3 | 11 | 2.2 | 5% | 4 | 0.3 | 1% |
| **total** | 86 | 99.5 | 346 | 73.6 | 26% | 206 | 23.5 | 11% |

### `test` takes

| speaker | takes | minutes | A clips | A min | rejected (A) | B clips | B min | rejected (A+B) |
|---|---|---|---|---|---|---|---|---|
| 1_wayne | 15 | 16.9 | 72 | 11.7 | 31% | 58 | 6.0 | 12% |
| 2_scott | 15 | 16.5 | 47 | 5.1 | 69% | 57 | 5.7 | 47% |
| 3_solomon | 15 | 19.2 | 64 | 11.5 | 40% | 57 | 7.8 | 13% |
| 4_lawrence | 15 | 20.3 | 101 | 14.0 | 31% | 103 | 11.6 | 3% |
| 5_stewart | 15 | 15.8 | 62 | 13.8 | 13% | 16 | 1.5 | 7% |
| 6_carla | 7 | 6.0 | 32 | 4.3 | 29% | 19 | 1.6 | 14% |
| 7_sophie | 15 | 15.1 | 71 | 14.0 | 7% | 38 | 3.3 | 0% |
| 9_miranda | 7 | 6.7 | 23 | 6.5 | 3% | 4 | 0.3 | 1% |
| 10_kieks | 15 | 15.4 | 56 | 15.4 | 0% | 4 | 0.3 | 0% |
| 12_zhao | 9 | 10.7 | 14 | 1.5 | 86% | 21 | 2.1 | 68% |
| 13_lu | 9 | 9.7 | 35 | 5.6 | 42% | 36 | 5.2 | 6% |
| 15_carlos | 9 | 11.6 | 44 | 9.9 | 15% | 21 | 2.5 | 2% |
| 16_jorge | 9 | 7.6 | 0 | 0.0 | 100% | 7 | 0.8 | 90% |
| 17_itoi | 9 | 11.8 | 39 | 6.5 | 45% | 40 | 3.9 | 25% |
| 18_daiki | 9 | 11.0 | 42 | 10.4 | 6% | 19 | 1.7 | 0% |
| 22_luqi | 9 | 10.6 | 47 | 5.2 | 51% | 25 | 2.7 | 37% |
| 23_hailing | 8 | 9.7 | 32 | 9.5 | 2% | 2 | 0.2 | 1% |
| 24_kexin | 9 | 10.8 | 39 | 10.8 | 0% | 0 | 0.0 | 0% |
| 25_goto | 8 | 11.4 | 37 | 11.4 | 0% | 0 | 0.0 | 0% |
| 28_tiffnay | 9 | 10.6 | 39 | 10.5 | 1% | 10 | 0.8 | 0% |
| 30_katya | 9 | 10.6 | 44 | 10.5 | 1% | 11 | 0.8 | 0% |
| **total** | 225 | 258.2 | 940 | 188.0 | 27% | 548 | 58.7 | 14% |

## Held-out speakers

### `val` takes

| speaker | takes | minutes | A clips | A min | rejected (A) | B clips | B min | rejected (A+B) |
|---|---|---|---|---|---|---|---|---|
| 11_nidal | 8 | 13.3 | 44 | 13.3 | 0% | 0 | 0.0 | 0% |
| 20_li | 2 | 2.6 | 15 | 1.8 | 30% | 13 | 1.4 | 5% |
| 21_ayana | 8 | 10.7 | 39 | 10.1 | 5% | 11 | 1.1 | 2% |
| 27_yingqing | 2 | 2.2 | 9 | 1.8 | 17% | 5 | 0.6 | 3% |
| **total** | 20 | 28.7 | 107 | 27.0 | 6% | 29 | 3.1 | 1% |

### `test` takes

| speaker | takes | minutes | A clips | A min | rejected (A) | B clips | B min | rejected (A+B) |
|---|---|---|---|---|---|---|---|---|
| 11_nidal | 15 | 21.9 | 74 | 21.9 | 0% | 0 | 0.0 | 0% |
| 20_li | 9 | 12.0 | 59 | 8.7 | 28% | 54 | 6.1 | 3% |
| 21_ayana | 7 | 7.6 | 32 | 6.8 | 12% | 15 | 1.3 | 4% |
| 27_yingqing | 9 | 11.5 | 49 | 9.8 | 15% | 21 | 2.0 | 8% |
| **total** | 40 | 53.0 | 214 | 47.1 | 11% | 90 | 9.3 | 3% |

## Totals

| group / type | takes | minutes | A clips | A min | rejected (A) | B clips | B min | rejected (A+B) |
|---|---|---|---|---|---|---|---|---|
| train / train | 865 | 899.0 | 3451 | 698.6 | 22% | 1724 | 168.8 | 13% |
| train / val | 86 | 99.5 | 346 | 73.6 | 26% | 206 | 23.5 | 11% |
| train / test | 225 | 258.2 | 940 | 188.0 | 27% | 548 | 58.7 | 14% |
| heldout / val | 20 | 28.7 | 107 | 27.0 | 6% | 29 | 3.1 | 1% |
| heldout / test | 40 | 53.0 | 214 | 47.1 | 11% | 90 | 9.3 | 3% |

## Training balance (Tier A, `train` takes)

| speaker | A min | share |
|---|---|---|
| 3_solomon | 90.0 | 12.9% |
| 7_sophie | 84.3 | 12.1% |
| 9_miranda | 79.4 | 11.4% |
| 4_lawrence | 78.6 | 11.3% |
| 1_wayne | 77.9 | 11.1% |
| 6_carla | 35.9 | 5.1% |
| 25_goto | 29.0 | 4.2% |
| 18_daiki | 25.6 | 3.7% |
| 24_kexin | 25.6 | 3.7% |
| 30_katya | 24.5 | 3.5% |
| 23_hailing | 24.1 | 3.4% |
| 28_tiffnay | 23.9 | 3.4% |
| 15_carlos | 20.0 | 2.9% |
| 13_lu | 18.3 | 2.6% |
| 17_itoi | 17.8 | 2.6% |
| 2_scott | 11.6 | 1.7% |
| 22_luqi | 10.2 | 1.5% |
| 12_zhao | 9.8 | 1.4% |
| 10_kieks | 6.8 | 1.0% |
| 5_stewart | 5.1 | 0.7% |
| 16_jorge | 0.0 | 0.0% |
| **total** | 698.6 (11.64 h) | |

## Clips

| tier | clips | length s (min / median / max) | feet cm (median / p95 / max) | arms cm/s (median / p10) | clips over the tier radius |
|---|---|---|---|---|---|
| A | 5058 | 4.0 / 13.4 / 20.0 | 3.0 / 9.7 / 15.1 | 21 / 10 | 37 |
| B | 2597 | 4.0 / 4.7 / 19.7 | 15.1 / 24.9 / 38.6 | 29 / 14 | 104 |
