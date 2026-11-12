"""The gesture generator's features on synthetic signals with known answers (no data files needed)."""

from __future__ import annotations

import numpy as np

from booster_mjlab.gesture import audio, motion

RATE, FPS = 16000, 50.0


def tone(f0: float, seconds: float, amp: float = 0.3, harmonics: int = 6) -> np.ndarray:
    """A voice-like periodic sound: f0 plus decaying harmonics."""
    t = np.arange(int(seconds * RATE)) / RATE
    return amp * sum(np.sin(2 * np.pi * f0 * h * t) / h for h in range(1, harmonics + 1))


def test_frames_are_centered_on_motion_frames():
    x = np.zeros(RATE)
    x[8000] = 1.0  # an impulse at exactly 0.5 s = motion frame 25
    loud = audio.loudness_db(audio.frames(x, RATE, FPS))
    assert int(np.argmax(loud)) == 25


def test_loudness_tracks_amplitude():
    x = np.concatenate([tone(150, 1.0, amp=0.05), tone(150, 1.0, amp=0.5)])
    loud = audio.loudness_db(audio.frames(x, RATE, FPS))
    quiet, loud_part = np.median(loud[10:40]), np.median(loud[60:90])
    assert abs((loud_part - quiet) - 20.0) < 0.5  # 10x amplitude = +20 dB


def test_pitch_finds_f0_and_rejects_noise():
    for f0 in (90.0, 140.0, 220.0, 330.0):
        est, voiced = audio.pitch(audio.frames(tone(f0, 1.0), RATE, FPS), RATE)
        mid = est[10:40]
        assert np.all(voiced[10:40] > 0.8), f0
        assert np.max(np.abs(mid - f0)) / f0 < 0.02, (f0, mid.min(), mid.max())
    rng = np.random.default_rng(0)
    est, voiced = audio.pitch(audio.frames(0.3 * rng.standard_normal(RATE), RATE, FPS), RATE)
    assert np.mean(voiced[5:-5] >= audio.VOICED_THRESHOLD) < 0.05


def test_onsets_peak_at_syllable_starts():
    # Four 150 ms "syllables" starting at 0.2, 0.6, 1.0, 1.4 s, silence between.
    x = np.zeros(2 * RATE)
    starts = [0.2, 0.6, 1.0, 1.4]
    for s in starts:
        a = int(s * RATE)
        x[a:a + int(0.15 * RATE)] = tone(180, 0.15)
    onset = audio.onset_strength(audio.frames(x, RATE, FPS), RATE)
    peaks = [i for i in range(1, len(onset) - 1) if onset[i] >= onset[i - 1] and onset[i] > onset[i + 1]
             and onset[i] > 0.3 * onset.max()]
    assert len(peaks) == len(starts)
    for p, s in zip(peaks, starts):
        assert abs(p / FPS - s) <= 0.03  # within ~1 frame of the true start


def test_speech_features_shapes_and_pauses():
    x = np.concatenate([np.zeros(RATE // 2), tone(150, 1.0), np.zeros(RATE // 2)])
    x = x + 1e-4 * np.random.default_rng(1).standard_normal(len(x))
    f = audio.speech_features(x, RATE, FPS, n_frames=100)
    assert f.shape == (100, len(audio.FEATURES))
    speech = f[:, audio.FEATURES.index("speech")]
    assert speech[:20].sum() == 0 and speech[-20:].sum() == 0 and speech[30:70].all()
    pitch_st = f[:, audio.FEATURES.index("pitch_st")]
    assert np.all(np.abs(pitch_st[30:70]) < 0.5)  # steady tone = its own median pitch
    assert np.all(np.isfinite(f))


def test_units_cut_at_hand_pauses():
    # Hand speed: 5 gestures (bumps) of 0.8 s each, separated by short pauses.
    t = np.arange(int(5 * FPS)) / FPS
    speed = np.abs(np.sin(np.pi * t / 1.0)) + 0.02
    bounds = motion.cut_units(speed, FPS, min_s=0.5, max_s=3.0)
    assert bounds[0] == 0 and bounds[-1] == len(speed)
    cuts = np.array(bounds[1:-1]) / FPS
    assert len(cuts) == 4
    assert np.max(np.abs(cuts - np.array([1.0, 2.0, 3.0, 4.0]))) <= 0.05
    lengths = np.diff(bounds) / FPS
    assert lengths.min() >= 0.5 and lengths.max() <= 3.0


def test_units_respect_min_and_max_length():
    rng = np.random.default_rng(0)
    speed = np.abs(rng.standard_normal(int(20 * FPS))) + 0.01  # jittery: many tiny minima
    bounds = motion.cut_units(speed, FPS, min_s=0.5, max_s=3.0)
    lengths = np.diff(bounds) / FPS
    assert lengths.min() >= 0.5 - 1e-9 and lengths.max() <= 3.0 + 1e-9
    flat = np.full(int(10 * FPS), 0.1)  # no pauses at all: still split under max_s
    lengths = np.diff(motion.cut_units(flat, FPS, min_s=0.5, max_s=3.0)) / FPS
    assert lengths.max() <= 3.0 + 1e-9 and lengths.min() >= 0.5 - 1e-9


def test_reply_features_match_library_normalization(tmp_path):
    """A TTS reply must be normalized exactly like a library take, or matching compares scales."""
    from booster_mjlab.gesture.analysis import Lib, recording_features

    rng = np.random.default_rng(0)
    x = np.concatenate([tone(150, 1.0), np.zeros(RATE // 3), tone(200, 0.8, amp=0.6)])
    x = x + 1e-3 * rng.standard_normal(len(x))
    raw = audio.speech_features(x, RATE, FPS)
    n = len(raw)
    path = tmp_path / "lib.npz"
    np.savez(path, fps=FPS, audio_features=np.array(audio.FEATURES), motion_features=np.array(motion.MOTION_FEATURES),
             clip_name=np.array(["c"]), clip_take=np.array(["t"]), clip_speaker=np.array(["s"]),
             clip_offset=np.array([0]), clip_length=np.array([n]), audio=raw.astype(np.float32),
             motion=np.zeros((n, len(motion.MOTION_FEATURES)), np.float32),
             unit_clip=np.array([0]), unit_start=np.array([0]), unit_end=np.array([n]))
    lib = Lib(path)
    feats, voiced, pitch = recording_features(raw.astype(np.float32))
    np.testing.assert_allclose(feats, lib.feats, atol=1e-5)
    np.testing.assert_array_equal(voiced, lib.voiced_mask)
