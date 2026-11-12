"""Per-take check that a BEAT2 recording's audio lines up with its motion capture.

The jaw moves with every syllable, at almost no delay, so in a synced take the jaw's *opening speed*
peaks with the loudness. The jaw comes from the same motion capture file as the body, so a take
whose jaw is in sync has its gestures in sync too.

Use jaw **speed**, not jaw **angle**: the angle is slow and also opens to breathe in before a
phrase, which made Miranda's takes look 0.5-0.9 s off when they weren't (2026-11-11, log.md).
Syllable-rate jaw speed can't be fooled that way.

Measured 2026-11-11 (jaw speed vs loudness, 30 fps): Wayne 114/130 takes within 67 ms, the rest
-100..-200 ms (the jaw moves slightly before the sound; corr at 0 almost as high) + one take at
+2 s; Lawrence similar; Miranda 104/122 + ~12 takes at -0.23..-0.77 s. Hence ``MAX_LAG_S`` 0.2.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

from booster_mjlab.gesture.audio import frames, load_audio, loudness_db

MAX_LAG_S = 0.2  # |jaw-vs-loudness lag| above this fails the take
SEARCH_S = 2.0  # lags searched: +-2 s
JAW = slice(66, 69)  # SMPL-X joint 22 (jaw) in BEAT2's `poses`


@dataclass
class JawSync:
    take: str
    lag_s: float  # positive = jaw after loudness
    corr: float  # correlation at that lag
    corr_at_0: float
    passed: bool


def lagged_corr(a: np.ndarray, b: np.ndarray, max_lag: int) -> np.ndarray:
    """Correlation of z-scored a[t] with b[t + L] for L in [-max_lag, max_lag]."""
    n = min(len(a), len(b))
    a = (a[:n] - a[:n].mean()) / (a[:n].std() + 1e-9)
    b = (b[:n] - b[:n].mean()) / (b[:n].std() + 1e-9)
    out = np.full(2 * max_lag + 1, np.nan)
    for i, L in enumerate(range(-max_lag, max_lag + 1)):
        x, y = (a[: n - L], b[L:]) if L >= 0 else (a[-L:], b[: n + L])
        if len(x) > 10:
            out[i] = np.mean(x * y)
    return out


def jaw_sync(smplx_npz: Path, wav: Path) -> JawSync:
    """Jaw opening speed vs loudness for one take, at the motion capture's frame rate."""
    with np.load(smplx_npz) as z:
        fps = float(z["mocap_frame_rate"])
        jaw_open = z["poses"][:, JAW][:, 0]  # rotation about x: opening and closing
    jaw_speed = np.abs(np.gradient(jaw_open))
    x, rate = load_audio(wav)
    loud = loudness_db(frames(x, rate, fps, len(jaw_speed)))
    max_lag = round(SEARCH_S * fps)
    c = lagged_corr(loud, jaw_speed, max_lag)
    i = int(np.nanargmax(c))
    lag = (i - max_lag) / fps
    return JawSync(smplx_npz.stem, lag, float(c[i]), float(c[max_lag]), abs(lag) <= MAX_LAG_S)
