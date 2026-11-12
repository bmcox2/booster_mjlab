"""Speech features at the motion frame rate (one value per 20 ms at 50 fps).

Frame k describes the audio *around* time k / fps (a window centered there), the same instant as
motion frame k, so audio and motion arrays index the same moments.

Features (``FEATURES``, columns of ``speech_features``):
- ``loud_db``: loudness, RMS energy of a 40 ms window in dB. High on stressed, loud syllables.
- ``onset``: onset strength (spectral flux): how much the spectrum *grows* from the previous frame,
  summed over frequency bands. Spikes at the start of syllables and consonant bursts, so it marks
  rhythm, the "beats" of speech.
- ``voiced``: voicing strength 0..1 (the autocorrelation peak used for pitch). Near 1 on vowels.
- ``pitch_st``: pitch in semitones relative to the recording's median pitch, 0 where unvoiced.
  Pitch rises on emphasized words (pitch accents), which is when people tend to gesture.
- ``speech``: 1 while speaking, 0 in pauses (loudness above the recording's noise floor, small gaps
  filled).

Pitch uses the autocorrelation method with window correction (Boersma 1993, the method in Praat):
a voiced sound repeats every pitch period, so the window correlates with itself shifted by one
period. ``tests/test_gesture.py`` checks every feature on synthetic signals with known answers.
"""

from __future__ import annotations

import numpy as np
from scipy.io import wavfile
from scipy.ndimage import binary_closing, binary_opening, median_filter

FEATURES = ("loud_db", "onset", "voiced", "pitch_st", "speech")
WINDOW_S = 0.040  # analysis window (2 motion frames)
F0_MIN, F0_MAX = 70.0, 450.0  # speech pitch range searched (Hz)
VOICED_THRESHOLD = 0.45  # autocorrelation peak above which a frame counts as voiced
OCTAVE_RATIO = 0.9  # prefer the shortest period whose peak is within this fraction of the best
SPEECH_DB_ABOVE_FLOOR = 15.0  # speech = louder than the noise floor by this much


def load_audio(path) -> tuple[np.ndarray, int]:
    """Mono float audio in [-1, 1] and its sample rate. BEAT2 mixes int16 and float32 files."""
    rate, audio = wavfile.read(path)
    if audio.dtype.kind in "iu":
        audio = audio.astype(np.float64) / float(np.iinfo(audio.dtype).max)
    audio = np.asarray(audio, dtype=np.float64)
    if audio.ndim == 2:
        audio = audio.mean(axis=1)
    return audio, int(rate)


def frames(audio: np.ndarray, rate: int, fps: float, n_frames: int | None = None,
           window_s: float = WINDOW_S) -> np.ndarray:
    """(n_frames, window) matrix: row k is the window centered at time k / fps (zero-padded at ends)."""
    win = int(round(window_s * rate))
    hop = rate / fps
    if n_frames is None:
        n_frames = int(np.floor(len(audio) / hop)) + 1
    padded = np.concatenate([np.zeros(win), audio, np.zeros(win)])
    starts = (np.round(np.arange(n_frames) * hop).astype(int) - win // 2) + win  # shifted by the pad
    starts = np.clip(starts, 0, len(padded) - win)
    return padded[starts[:, None] + np.arange(win)[None, :]]


def loudness_db(fr: np.ndarray) -> np.ndarray:
    rms = np.sqrt(np.mean(fr**2, axis=1))
    return 20.0 * np.log10(rms + 1e-6)  # silence -> -120 dB instead of -inf


def _band_matrix(n_bins: int, rate: int, n_fft: int, n_bands: int = 40) -> np.ndarray:
    """Triangular bands spaced evenly on a log-frequency scale (60 Hz - 7.5 kHz): (n_bands, n_bins)."""
    freqs = np.arange(n_bins) * rate / n_fft
    edges = np.geomspace(60.0, min(7500.0, rate / 2 - 1), n_bands + 2)
    m = np.zeros((n_bands, n_bins))
    for b in range(n_bands):
        lo, mid, hi = edges[b], edges[b + 1], edges[b + 2]
        up = (freqs - lo) / (mid - lo)
        down = (hi - freqs) / (hi - mid)
        m[b] = np.clip(np.minimum(up, down), 0.0, None)
    return m / np.maximum(m.sum(axis=1, keepdims=True), 1e-9)


def onset_strength(fr: np.ndarray, rate: int) -> np.ndarray:
    """Spectral flux on log band energies, half-wave rectified (only increases count)."""
    n_fft = 1 << int(np.ceil(np.log2(fr.shape[1])))
    spec = np.abs(np.fft.rfft(fr * np.hanning(fr.shape[1]), n=n_fft, axis=1))
    bands = np.log1p(100.0 * (spec**2) @ _band_matrix(spec.shape[1], rate, n_fft).T)
    flux = np.maximum(np.diff(bands, axis=0, prepend=bands[:1]), 0.0).sum(axis=1)
    return flux


def pitch(fr: np.ndarray, rate: int, chunk: int = 4000) -> tuple[np.ndarray, np.ndarray]:
    """(f0 in Hz, 0 where unvoiced; voicing strength 0..1) per frame."""
    win = fr.shape[1]
    w = np.hanning(win)
    n_fft = 1 << int(np.ceil(np.log2(2 * win)))
    # Autocorrelation of the window itself: dividing by it undoes the taper's bias (Boersma 1993).
    rw = np.fft.irfft(np.abs(np.fft.rfft(w, n_fft)) ** 2)[:win]
    rw /= rw[0]
    # Lags past half the window rest on few samples (and a tiny window autocorrelation), so stop there.
    lag_lo, lag_hi = int(rate / F0_MAX), min(int(rate / F0_MIN), win // 2)
    f0 = np.zeros(len(fr))
    strength = np.zeros(len(fr))
    for a in range(0, len(fr), chunk):
        x = fr[a:a + chunk]
        x = (x - x.mean(axis=1, keepdims=True)) * w
        r = np.fft.irfft(np.abs(np.fft.rfft(x, n_fft, axis=1)) ** 2, axis=1)[:, :win]
        energy = r[:, :1]
        r = r / np.maximum(energy, 1e-12) / np.maximum(rw, 1e-3)
        seg = r[:, lag_lo:lag_hi + 1]
        # A sound with period T also repeats at 2T, 3T..., so the highest peak is sometimes a
        # multiple (an octave error: half the true pitch). Take the shortest-lag local peak within
        # 90% of the best one instead.
        is_peak = np.zeros_like(seg, dtype=bool)
        is_peak[:, 1:-1] = (seg[:, 1:-1] >= seg[:, :-2]) & (seg[:, 1:-1] > seg[:, 2:])
        best = seg.max(axis=1, keepdims=True)
        good = is_peak & (seg >= OCTAVE_RATIO * best)
        i = np.where(good.any(axis=1), np.argmax(good, axis=1), np.argmax(seg, axis=1))
        peak = seg[np.arange(len(seg)), i]
        # Parabolic interpolation around the peak for sub-sample lag precision.
        left = seg[np.arange(len(seg)), np.clip(i - 1, 0, seg.shape[1] - 1)]
        right = seg[np.arange(len(seg)), np.clip(i + 1, 0, seg.shape[1] - 1)]
        denom = left - 2 * peak + right
        with np.errstate(divide="ignore", invalid="ignore"):
            shift = np.where(np.abs(denom) > 1e-9, 0.5 * (left - right) / denom, 0.0)
        lag = lag_lo + i + np.clip(shift, -0.5, 0.5)
        silent = energy[:, 0] < 1e-10
        strength[a:a + chunk] = np.where(silent, 0.0, np.clip(peak, 0.0, 1.0))
        f0[a:a + chunk] = np.where(strength[a:a + chunk] >= VOICED_THRESHOLD, rate / lag, 0.0)
    return f0, strength


def speech_mask(loud: np.ndarray, fps: float) -> np.ndarray:
    """1 while speaking: loudness above the recording's noise floor (5th percentile) by
    ``SPEECH_DB_ABOVE_FLOOR``, gaps under 200 ms filled, blips under 100 ms removed."""
    floor = np.percentile(loud, 5)
    m = loud > floor + SPEECH_DB_ABOVE_FLOOR
    m = binary_closing(m, structure=np.ones(max(1, round(0.2 * fps)), bool))
    m = binary_opening(m, structure=np.ones(max(1, round(0.1 * fps)), bool))
    return m.astype(np.float64)


def speech_features(audio: np.ndarray, rate: int, fps: float, n_frames: int | None = None) -> np.ndarray:
    """(n_frames, len(FEATURES)) feature matrix, columns in ``FEATURES`` order."""
    fr = frames(audio, rate, fps, n_frames)
    loud = loudness_db(fr)
    onset = onset_strength(fr, rate)
    f0, voiced = pitch(fr, rate)
    # Remove single-frame octave jumps; next to silence the median can be 0, so keep the raw value there.
    smooth = median_filter(f0, size=5)
    f0 = np.where(f0 > 0, np.where(smooth > 0, smooth, f0), 0.0)
    med = np.median(f0[f0 > 0]) if np.any(f0 > 0) else 1.0
    pitch_st = np.where(f0 > 0, 12.0 * np.log2(np.maximum(f0, 1e-6) / med), 0.0)
    speech = speech_mask(loud, fps)
    return np.stack([loud, onset, voiced, pitch_st, speech], axis=1)


def match_level(x: np.ndarray, target_db: float = -20.0, rate: int = 16000, peak: float = 0.95) -> np.ndarray:
    """Scale speech to ``target_db`` dBFS, measured over its active part (20 ms frames within 20 dB
    of the loudest 10%), so pauses don't count; then scale down if a peak would pass ``peak``.
    For soundtracks that mix voices: the laptop mic recorded the user ~13 dB louder than Kokoro."""
    hop = max(1, rate // 50)
    if len(x) < hop:
        return x
    fr = x[: len(x) // hop * hop].reshape(-1, hop)
    rms = np.sqrt((fr ** 2).mean(axis=1)) + 1e-12
    active = rms[rms > np.percentile(rms, 90) * 0.1]
    level = np.sqrt((active ** 2).mean()) if len(active) else rms.max()
    gain = 10 ** (target_db / 20) / max(level, 1e-9)
    gain = min(gain, peak / max(np.abs(x).max(), 1e-9))
    return x * gain
