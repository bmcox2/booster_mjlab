"""Audio-motion sync check for BEAT2 clips on the K1 (notes/gesture_plan.md, step 1).

Is a clip's motion aligned with its speech audio? Both are turned into one value per 20 ms (50 Hz,
the motion frame rate), then compared at every time shift (lag) from -1 s to +1 s:

- **loudness**: RMS energy of each 20 ms window of audio, in dB (louder speech -> higher);
- **hand speed**: how fast both hands move relative to the trunk, in m/s (sway of the whole body is
  removed, so this is gesturing, not leaning).

Both curves are z-scored per clip (mean 0, standard deviation 1), so their product averages to a
correlation between -1 and 1. The lag with the highest correlation is the offset between speech
and motion. **Positive lag = the hands peak after the loudness.** Gestures usually land on or a
little before the stressed syllable, so a peak within about +-0.2 s means in sync; a peak far
from 0 (or none at all) means an offset or no relation.

Short clips give noisy curves, so the pooled curve (all clips averaged) is the number to trust.
Its height is also a first answer to step 2's question: does loudness predict hand speed at all?

Usage (from ~/projects/booster-mjlab):
    # clips exported with tools/export_deploy_clip.py --audio (pairs <clip>.npz + <clip>.wav)
    uv run python tools/gesture_sync_check.py --dir logs/sync
    # library clips straight from a combined file, audio cut from the BEAT2 takes via segments.json
    uv run python tools/gesture_sync_check.py --motion-file ~/robotics/data/beat2_full_torso/combined/beat2-full-torso-train-a.npz \\
        --speakers 1_wayne 4_lawrence 9_miranda --max-clips 300
Writes a plot next to the clips (--dir) or to --plot.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import mujoco
import numpy as np
from scipy.io import wavfile

REPO = Path(__file__).resolve().parents[1]
K1_XML = REPO / "src/booster_mjlab/robots/booster_k1/xmls/k1.xml"
SEGMENTS = Path.home() / "robotics/data/beat2_full_torso/segments.json"
WAVE_DIR = Path.home() / "robotics/data/BEAT2/beat_english_v2.0.0/wave16k"
HANDS = ("left_hand_end_ball", "right_hand_end_ball")
TRUNK = "Trunk"


def to_float(audio: np.ndarray) -> np.ndarray:
    """BEAT2 mixes int16 and float32 files: bring both to float in [-1, 1], mono."""
    if audio.dtype.kind == "i":
        audio = audio.astype(np.float64) / np.iinfo(audio.dtype).max
    audio = audio.astype(np.float64)
    return audio.mean(axis=1) if audio.ndim == 2 else audio


def loudness_db(audio: np.ndarray, rate: int, fps: float, n_frames: int) -> np.ndarray:
    """RMS energy of each motion frame's slice of audio, in dB. One value per frame."""
    hop = rate / fps  # audio samples per motion frame (16000 / 50 = 320)
    out = np.full(n_frames, np.nan)
    for k in range(n_frames):
        a, b = round(k * hop), round((k + 1) * hop)
        if b > len(audio):
            break
        rms = np.sqrt(np.mean(audio[a:b] ** 2))
        out[k] = 20 * np.log10(rms + 1e-6)  # +1e-6: silence gives -120 dB instead of -inf
    return out


def hand_speed(body_pos: np.ndarray, body_names: list[str], fps: float) -> np.ndarray:
    """Summed speed of both hands relative to the trunk (m/s), one value per frame."""
    trunk = body_pos[:, body_names.index(TRUNK)]
    speed = np.zeros(len(body_pos))
    for h in HANDS:
        rel = body_pos[:, body_names.index(h)] - trunk
        v = np.linalg.norm(np.diff(rel, axis=0), axis=1) * fps
        speed += np.concatenate([v[:1], v])  # same length as the clip
    return speed


def zscore(x: np.ndarray) -> np.ndarray:
    return (x - x.mean()) / (x.std() + 1e-9)


def xcorr(loud: np.ndarray, speed: np.ndarray, max_lag: int) -> tuple[np.ndarray, np.ndarray]:
    """Correlation at each lag in [-max_lag, max_lag] frames, plus the number of overlapping
    frames per lag. Lag L pairs loudness at t with hand speed at t + L."""
    n = min(len(loud), len(speed))
    ok = ~np.isnan(loud[:n])
    a, h = zscore(loud[:n][ok]), zscore(speed[:n][ok])
    lags = np.arange(-max_lag, max_lag + 1)
    corr, count = np.full(len(lags), np.nan), np.zeros(len(lags))
    for i, L in enumerate(lags):
        x, y = (a[: len(a) - L], h[L:]) if L >= 0 else (a[-L:], h[: len(h) + L])
        if len(x) > 10:
            corr[i], count[i] = np.mean(x * y), len(x)
    return corr, count


def clips_from_dir(folder: Path):
    for npz in sorted(folder.glob("*.npz")):
        wav = npz.with_suffix(".wav")
        if not wav.exists():
            continue
        with np.load(npz) as z:
            fps = float(z["fps"][0])
            yield npz.stem, z["body_pos_w"], [str(n) for n in z["body_names"]], fps, *wavfile.read(wav)


def clips_from_library(motion_file: Path, speakers: list[str], max_clips: int, seed: int):
    takes = json.loads(SEGMENTS.read_text())["takes"]
    seg = {c["name"]: c for t in takes for c in t["clips"] if t["speaker"] in speakers}
    model = mujoco.MjModel.from_xml_path(str(K1_XML))
    body_names = [model.body(b).name for b in range(1, model.nbody)]  # motion-file order
    z = np.load(motion_file)
    names = [str(n) for n in z["clip_names"]]
    starts = np.concatenate([[0], np.cumsum(z["clip_lengths"])])
    fps = float(z["fps"][0])
    picked = [i for i, n in enumerate(names) if n in seg]
    rng = np.random.default_rng(seed)
    picked = sorted(rng.choice(picked, size=min(max_clips, len(picked)), replace=False))
    print(f"{len(picked)} clips of {sorted(speakers)} (from {sum(n in seg for n in names)} in the file)")
    body_pos = z["body_pos_w"]  # loads the whole array once (~1-2 GB for train-a)
    cache: dict[str, tuple[int, np.ndarray]] = {}
    for i in picked:
        c = seg[names[i]]
        if c["take"] not in cache:
            cache.clear()  # clips are sorted by take, so one take's audio at a time is enough
            cache[c["take"]] = wavfile.read(WAVE_DIR / f"{c['take']}.wav")
        rate, audio = cache[c["take"]]
        a, b = round(c["start"] * rate), round(c["end"] * rate)
        yield names[i], body_pos[starts[i]:starts[i + 1]], body_names, fps, rate, audio[a:b]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--dir", type=Path, help="folder of <clip>.npz + <clip>.wav (export_deploy_clip.py --audio)")
    src.add_argument("--motion-file", type=Path, help="combined motion .npz; audio from segments.json + BEAT2 takes")
    ap.add_argument("--speakers", nargs="+", default=["1_wayne", "4_lawrence", "9_miranda"])
    ap.add_argument("--max-clips", type=int, default=300)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--max-lag-s", type=float, default=1.0)
    ap.add_argument("--plot", type=Path, help="where to save the plot (default: <dir>/sync_check.png)")
    args = ap.parse_args()

    clips = (clips_from_dir(args.dir) if args.dir
             else clips_from_library(args.motion_file, args.speakers, args.max_clips, args.seed))
    total, weight, rows, examples = None, None, [], []
    for name, body_pos, body_names, fps, rate, audio in clips:
        max_lag = round(args.max_lag_s * fps)
        loud = loudness_db(to_float(audio), rate, fps, len(body_pos))
        speed = hand_speed(body_pos, body_names, fps)
        corr, count = xcorr(loud, speed, max_lag)
        lags_s = np.arange(-max_lag, max_lag + 1) / fps
        best = int(np.nanargmax(corr))
        rows.append((name, len(body_pos) / fps, lags_s[best], corr[best], corr[max_lag]))
        w = np.nan_to_num(count)
        total = np.nan_to_num(corr) * w if total is None else total + np.nan_to_num(corr) * w
        weight = w if weight is None else weight + w
        if len(examples) < 3:
            examples.append((name, loud, speed, fps))
    if not rows:
        raise SystemExit("no clips found (need <clip>.npz + <clip>.wav pairs, or matching speakers)")

    print(f"\n{'clip':34} {'len s':>6} {'best lag s':>10} {'corr there':>10} {'corr at 0':>9}")
    for name, sec, lag, c, c0 in rows:
        print(f"{name:34} {sec:6.1f} {lag:+10.2f} {c:10.2f} {c0:9.2f}")
    pooled = total / np.maximum(weight, 1)
    lags_s = np.arange(len(pooled)) / fps - args.max_lag_s
    best = int(np.argmax(pooled))
    lag_list = np.array([r[2] for r in rows])
    print(f"\npooled over {len(rows)} clips: peak at {lags_s[best]:+.2f} s (corr {pooled[best]:.2f}); "
          f"corr at 0 s {pooled[len(pooled) // 2]:.2f}")
    print(f"per-clip best lag: median {np.median(lag_list):+.2f} s, middle half "
          f"{np.percentile(lag_list, 25):+.2f} to {np.percentile(lag_list, 75):+.2f} s")
    print("positive lag = hands peak after the loudness")

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(len(examples) + 1, 1, figsize=(10, 2.6 * (len(examples) + 1)))
    ax = axes[0]
    ax.plot(lags_s, pooled, color="black")
    ax.axvline(0, color="gray", lw=0.8)
    ax.axvline(lags_s[best], color="tab:red", ls="--", lw=0.8)
    ax.set(title=f"pooled cross-correlation, {len(rows)} clips (peak {lags_s[best]:+.2f} s)",
           xlabel="lag (s): positive = hands after loudness", ylabel="correlation")
    for ax, (name, loud, speed, fps_) in zip(axes[1:], examples):
        t = np.arange(len(speed)) / fps_
        ax.plot(t, zscore(np.nan_to_num(loud, nan=np.nanmin(loud))), label="loudness (z)", lw=0.9)
        ax.plot(t, zscore(speed), label="hand speed (z)", lw=0.9)
        ax.set(title=name, xlabel="time (s)")
        ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    out = args.plot or ((args.dir or Path("logs")) / "sync_check.png")
    fig.savefig(out, dpi=110)
    print(f"plot: {out}")


if __name__ == "__main__":
    main()
