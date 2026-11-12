"""Streaming gesture motion (gesture_plan.md step 7): ``gesture/stream.py`` and the replay events.

The timeline tests need the gesture library and GMR's K1 model (skipped without them)."""

from __future__ import annotations

import base64
import json
from pathlib import Path

import numpy as np
import pytest
from scipy.io import wavfile

from booster_mjlab.gesture.generate import FPS, GenCfg
from booster_mjlab.gesture.live import replay_events
from booster_mjlab.gesture.stream import LEAD, MotionStream, RunningFeatures, StreamCfg

RATE = 16000


def voice(seconds: float, amp: float, seed: int = 0) -> np.ndarray:
    """A harmonic tone that swells ~8 times per second, like syllables."""
    t = np.arange(int(seconds * RATE)) / RATE
    tone = sum(np.sin(2 * np.pi * 140 * h * t) / h for h in range(1, 6))
    env = 0.6 + 0.4 * np.sin(2 * np.pi * 4 * t + seed) ** 2  # never silent: silence inside speech counts as speech
    return amp * tone * env


def test_running_features_normalize_across_pieces():
    rf = RunningFeatures()
    f1, _, _ = rf(voice(2.0, 0.1))
    assert len(f1) == 100  # one row per 20 ms
    sp = f1[:, 4] > 0
    assert sp.mean() > 0.3
    assert abs(f1[sp, 0].mean()) < 1e-6  # first piece: z-scored on itself
    f2, _, _ = rf(voice(2.0, 0.4, seed=1))  # 12 dB louder: above the session's mean so far
    assert f2[f2[:, 4] > 0, 0].mean() > 0.3
    f3, _, _ = rf(voice(2.0, 0.1, seed=2))  # the first level again: now below the mean
    assert f3[f3[:, 4] > 0, 0].mean() < -0.3


@pytest.fixture(scope="module")
def stream():
    from booster_mjlab.gesture.generate import Units, _tool

    gc = _tool("ground_clip")
    if not GenCfg.library.exists() or not Path(gc.DEFAULT_GMR_XML).exists():
        pytest.skip("needs the gesture library and GMR's K1 model")
    import mujoco

    m = mujoco.MjModel.from_xml_path(str(gc.DEFAULT_GMR_XML))
    names = [gc.RENAME.get(n, n) for n in gc.hinge_names(m)]
    s = MotionStream(Units(GenCfg.library), names, GenCfg(reply=Path("."), speaker="9_miranda"), StreamCfg())
    while s.n < 300:
        s.extend_idle()
    return s


def test_speak_replaces_only_the_future_and_keeps_the_feet(stream):
    s = stream
    before = s.snapshot(10 ** 9)
    now, play = 100, 180
    info = s.speak(voice(3.0, 0.2), [], play, now)
    earliest = now + round(s.cfg.margin_s * FPS)
    assert info["late_frames"] == 0 and info["start_frame"] == play - LEAD
    assert info["first_frame"] >= earliest
    after = s.snapshot(10 ** 9)
    k = info["first_frame"] - 1  # the frame before the first changed one: its velocity is recomputed
    np.testing.assert_array_equal(before["joint_pos"][:k + 1], after["joint_pos"][:k + 1])
    np.testing.assert_array_equal(before["joint_vel"][:k], after["joint_vel"][:k])
    assert (after["kind"][play - LEAD:info["end_frame"]] == 1).all()
    assert info["end_frame"] == play - LEAD + 150 == len(after["joint_pos"])
    # no jump at the splice, and velocities are the positions' differences
    speed = np.abs(np.diff(after["joint_pos"], axis=0)) * FPS
    assert speed.max() < 10.0
    np.testing.assert_allclose(after["joint_vel"][1:-1], (after["joint_pos"][2:] - after["joint_pos"][:-2]) * FPS / 2, atol=1e-9)
    # feet: one place for the whole session, on the floor
    a, g = s._a, s.g
    pos = {side: [] for side in g.feet}
    low = []
    for f in range(s.n):
        g.set_pose(a["out_pos"][f], a["out_rot"][f], a["out_dof"][f])
        for side, foot in g.feet.items():
            pos[side].append(g.data.xpos[foot["body"]].copy())
        low.append(min(g.geom_lowest_z(foot["geom"]) for foot in g.feet.values()))
    for side in pos:
        assert np.ptp(np.array(pos[side]), axis=0).max() < 0.002
    assert abs(min(low)) < 0.002 and max(low) < 0.002
    assert s.lock_fails == 0


def test_late_piece_is_trimmed_or_dropped(stream):
    s = stream
    while s.n < 700:
        s.extend_idle()
    now = 600
    info = s.speak(voice(2.0, 0.2), [], now, now)  # plays right now: its first 0.44 s + margin of motion are gone
    margin = round(s.cfg.margin_s * FPS)
    assert info["late_frames"] == LEAD + margin
    assert info["start_frame"] == now + margin
    assert s.speak(voice(0.5, 0.2), [], now, now) is None  # nothing worth gesturing is left
    pre = s.pre_start(100, now + 20)
    assert pre["start_frame"] == now + 20 + margin and (s.snapshot(10 ** 9)["kind"][pre["start_frame"]:] == 2).all()


def test_replay_events_keep_the_recorded_timing(tmp_path):
    turn = tmp_path / "2026-01-01_00-00-00" / "turn_01"
    turn.mkdir(parents=True)
    rate = 24000
    wavfile.write(turn / "reply.wav", rate, (voice(3.0, 0.2)[: 3 * 16000].repeat(2)[: 3 * rate] * 32767).astype(np.int16))
    chunks = [{"index": 0, "text": "Hi there,", "start_sample": 0, "audio_seconds": 1.0, "ready_s": 1.7, "played_s": 1.72},
              {"index": 1, "text": "how are you today?", "start_sample": rate, "audio_seconds": 2.0, "ready_s": 2.3, "played_s": 2.72}]
    (turn / "tts.json").write_text(json.dumps({"chunks": chunks, "words": [{"word": "Hi", "start": 0.0, "end": 0.2},
                                                                           {"word": "how", "start": 1.1, "end": 1.3}]}))
    (turn / "timing.json").write_text(json.dumps({"events": {"llm_first_chunk": 1.0, "playback_end": 4.72}}))
    ev = replay_events(turn.parent, gap_s=1.5)
    assert [e["path"] for e in ev] == ["/begin", "/piece", "/piece", "/end"]
    base = ev[0]["at"] - 1.0
    assert [round(e["at"] - base, 2) for e in ev] == [1.0, 1.7, 2.3, 4.72]
    assert [round(e["play_at"] - base, 2) for e in ev[1:3]] == [1.72, 2.72]
    second = ev[2]["body"]
    assert len(base64.b64decode(second["audio"])) == 2 * rate * 2  # 2 s of 16-bit samples
    assert second["words"] == [{"word": "how", "start": pytest.approx(0.1), "end": pytest.approx(0.3)}]
