"""Retrieval gesture generator v0: a spoken reply in, a K1 reference out (notes/gesture_plan.md step 3).

1. **Reply features:** ``audio.speech_features`` at 50 fps, normalized like a library take
   (``analysis.recording_features``); strong accents (``analysis.strong_accents``).
2. **Segments:** the reply is split at word starts (``tts.json``) and pauses into ~1.3 s pieces.
3. **Candidates per segment** (all 20k units, then the best ``k``), cost = weighted sum of
   - audio: distance between the segment's audio summary and the unit's own audio summary
     (onset mean, peak / mean loudness, speech fraction; step 2: pitch adds nothing);
   - length: how much the unit must be stretched (at most +-15%);
   - pause: in pauses, prefer calm units (step 2's clearest signal);
   - timing: distance from the reply's strong accents to the unit's stroke ends once placed.
4. **Search:** the cheapest sequence of units, adding a transition cost between consecutive units
   (end pose vs next start pose: joints, legs weighted most because they move the feet, and hand
   positions). Dynamic programming (Viterbi) over the segments. A unit that continues the previous
   one in its original clip costs nothing to join.
5. **Stitch** in the units' source GMR ``.pkl`` (30 fps): each unit is time-stretched to its
   segment, turned and moved so its trunk heading and position continue from the previous unit, and
   crossfaded over ``crossfade_s`` using the frames just past each cut in the source clips.
6. **Clean up** like training data: ``tools/ground_clip.py`` (feet onto the floor), ``tools/clip_qc.py``
   (Gate 1), ``upload_motion.convert_batched`` (50 fps ``.npz`` by forward kinematics).

Timing: in the library, hands lead the audio by ``LEAD_S`` (0.44 s). A unit is matched against the
audio that came 0.44 s after its motion, and in the output the reply's audio starts 0.44 s after the
motion does (``plan.json`` ``audio_offset_s``).

``random_baseline``: same units, segments, stitching and transition cost, but the audio, pause and
timing terms off: what step 5 compares against.
"""

from __future__ import annotations

import json
import pickle
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import mujoco
import numpy as np
from scipy.ndimage import uniform_filter1d
from scipy.signal import resample_poly

from booster_mjlab.gesture import audio as A
from booster_mjlab.gesture.analysis import (
    WINDOW_FEATURES,
    Lib,
    recording_features,
    stroke_ends,
    strong_accents,
    summarize,
)

REPO = Path(__file__).resolve().parents[3]
FPS = 50.0  # library / analysis frame rate
PKL_FPS = 30  # source clips and the stitched output before conversion
LEAD_S = 0.44  # hands lead the audio (step 2, loudness' best lag)
MATCH = ("onset_mean", "loud_max", "loud_mean", "speech_frac")
# Joint weights for the transition cost, K1 order: head 2, left arm 4, right arm 4, left leg 6, right leg 6.
JOINT_W = np.array([0.5] * 2 + [1.0] * 8 + [2.0] * 12)


@dataclass
class GenCfg:
    reply: Path
    """A speech-loop turn folder (reply.wav + tts.json) or a .wav file."""
    library: Path = Path.home() / "robotics/data/gesture/library_v0.npz"
    out_dir: Path = Path("logs/gesture/replies")
    name: str | None = None
    """Output folder name (default: <session>_<turn>, plus _random for the baseline)."""
    random_baseline: bool = False
    seed: int = 0
    w_audio: float = 1.0
    w_length: float = 0.5
    w_pause: float = 0.5
    w_activity: float = 0.5
    """Pull toward the activity of the units whose audio sounds most similar (step 2's kNN)."""
    k_activity: int = 50
    w_timing: float = 0.5
    w_transition: float = 1.0
    max_stretch: float = 0.15
    seg_target_s: float = 1.3
    seg_min_s: float = 0.8
    seg_max_s: float = 2.2
    k_prefilter: int = 300
    k: int = 30
    crossfade_s: float = 0.3
    """Shortest crossfade at a seam; longer when the joints differ more (max_seam_speed)."""
    max_crossfade_s: float = 1.0
    max_seam_speed: float = 2.0
    """rad/s: the fastest any joint may move because of a crossfade."""
    timing_cap_s: float = 0.3
    w_speaker: float = 0.5
    """Cost of switching speaker between consecutive units (styles differ between people)."""
    speaker: str | None = None
    """Only use this speaker's units (e.g. 9_miranda): one consistent style."""
    foot_lock: bool = True
    idle_mean_speed: float = 0.10
    """Idle (listening) units: mean hand speed below this (m/s) ..."""
    idle_peak_speed: float = 0.25
    """... and never faster than this. 1,806 units, 53 min in library v0."""
    idle_seg_s: float = 2.0
    idle_noise: float = 1.0
    """Random cost added to idle candidates (calmness spans ~0-1), so each idle segment gets a different
    short list and the calmest few units don't dominate."""
    max_side_shift: float = 0.08
    """With foot lock: skip units whose trunk goes further than this (m) sideways from between the feet
    (over one leg); a locked stance can't reach it (miranda_1_5_5_t515-530, 12 cm, held 65 frames)."""
    reuse_gap_s: float = 60.0
    """A unit may come back only after this long (a viewer notices repeats close together)."""
    """Keep the feet on one stance (leg IK); off = blended legs, feet slide between units."""


# ---------------------------------------------------------------------------------------- library side


class Units:
    """Per-unit data the search needs, from the library (built once, ~10 s)."""

    def __init__(self, path: Path):
        self.lib = lib = Lib(path)
        L = np.load(path)
        self.source = L["clip_source"]
        joint_pos = L["joint_pos"].astype(np.float64)
        tw = L["twist"].astype(np.float64)
        hands = L["motion"][:, 3:9].astype(np.float64)  # lx ly lz rx ry rz, trunk frame
        lead = round(LEAD_S * FPS)
        cols = [WINDOW_FEATURES.index(f) for f in MATCH]
        n = len(lib.units)
        self.clip, self.a, self.b = lib.units.T
        self.length = self.b - self.a
        self.audio = np.zeros((n, len(MATCH)))
        self.activity = np.zeros(n)
        self.start_pose, self.end_pose = np.zeros((n, 22)), np.zeros((n, 22))
        self.start_hand, self.end_hand = np.zeros((n, 6)), np.zeros((n, 6))
        self.start_twist, self.end_twist = np.zeros(n), np.zeros(n)
        self.strokes = np.full((n, 12), np.nan)  # stroke ends, frames from the unit start
        self.next = np.full(n, -1)  # the unit that continues this one in its clip
        self.speaker = lib.speaker[self.clip]
        self.speed_mean = np.zeros(n)
        self.speed_peak = np.zeros(n)
        side = np.abs(L["trunk_over_feet"][:, 1]).astype(np.float64)
        self.side_shift = np.array([side[lib.offset[c] + a:lib.offset[c] + b].max() for c, a, b in lib.units])
        ends_by_clip = {}
        for u, (ci, a, b) in enumerate(lib.units):
            o, cl = lib.offset[ci], lib.length[ci]
            a2, b2 = min(a + lead, cl - 1), min(b + lead, cl)
            if b2 - a2 < 5:
                a2, b2 = a, b
            sl = slice(o + a2, o + b2)
            self.audio[u] = summarize(lib.feats[sl], lib.voiced_mask[sl], lib.raw_pitch[sl], FPS)[cols]
            self.activity[u] = lib.speed[o + a:o + b].mean()
            self.speed_mean[u], self.speed_peak[u] = self.activity[u], lib.speed[o + a:o + b].max()
            self.start_pose[u], self.end_pose[u] = joint_pos[o + a], joint_pos[o + b - 1]
            self.start_hand[u], self.end_hand[u] = hands[o + a], hands[o + b - 1]
            self.start_twist[u], self.end_twist[u] = tw[o + a], tw[o + b - 1]
            if ci not in ends_by_clip:
                ends_by_clip[ci] = stroke_ends(lib.speed[o:o + cl], FPS)
            e = ends_by_clip[ci]
            e = e[(e >= a) & (e < b)] - a
            self.strokes[u, :min(len(e), 12)] = e[:12]
        for u in range(n - 1):
            if self.clip[u + 1] == self.clip[u] and self.a[u + 1] == self.b[u]:
                self.next[u] = u + 1
        for t in np.unique(lib.take[self.clip]):  # activity: z-scored per take, like step 2's target
            m = lib.take[self.clip] == t
            self.activity[m] = (self.activity[m] - self.activity[m].mean()) / (self.activity[m].std() + 1e-9)
        self.audio_mu, self.audio_sd = self.audio.mean(0), self.audio.std(0) + 1e-9
        self.audio_z = (self.audio - self.audio_mu) / self.audio_sd
        rng = np.random.default_rng(0)
        i, j = rng.integers(0, n, 5000), rng.integers(0, n, 5000)
        self.audio_scale = float(np.median(np.linalg.norm(self.audio_z[i] - self.audio_z[j], axis=1)))
        self.trans_scale = float(np.median(self.transition(i, j)))

    def transition(self, u: np.ndarray, v: np.ndarray) -> np.ndarray:
        """Distance from the end of unit(s) u to the start of unit(s) v: joints (rad, weighted),
        hands (2 x m), and trunk twist relative to the feet (rad x 3: with locked feet a twist change
        turns the whole trunk during the seam)."""
        dq = np.sqrt((JOINT_W * (self.end_pose[u] - self.start_pose[v]) ** 2).sum(-1))
        dh = np.linalg.norm(self.end_hand[u] - self.start_hand[v], axis=-1)
        dt = np.abs((self.end_twist[u] - self.start_twist[v] + np.pi) % (2 * np.pi) - np.pi)
        cost = dq + 2.0 * dh + 3.0 * dt
        return np.where(self.next[u] == v, 0.0, cost)


# ---------------------------------------------------------------------------------------- reply side


@dataclass
class Reply:
    wav: Path
    feats: np.ndarray  # FRAME_FEATURES, 50 fps
    voiced: np.ndarray
    pitch: np.ndarray
    accents: np.ndarray  # frames (reply audio clock)
    words: list[tuple[str, float, float]]
    seconds: float
    kind: np.ndarray | None = None  # per frame, conversations only: 1 = robot speaking, 0 = idle
    audio: np.ndarray | None = None  # 16 kHz, what plays with the motion (audio clock)


def load_reply(path: Path) -> Reply:
    wav = path / "reply.wav" if path.is_dir() else path
    x, rate = A.load_audio(wav)
    if rate != 16000:  # the library's features were computed at 16 kHz
        g = np.gcd(rate, 16000)
        x, rate = resample_poly(x, 16000 // g, rate // g), 16000
    raw = A.speech_features(x, rate, FPS)
    feats, voiced, pitch = recording_features(raw)
    words = []
    tts = wav.parent / "tts.json"
    if tts.exists():
        words = [(w["word"], float(w["start"]), float(w["end"])) for w in json.loads(tts.read_text()).get("words", [])]
    return Reply(wav, feats, voiced, pitch, strong_accents(feats, FPS), words, len(x) / rate, audio=x)


def load_conversation(sessions: list[Path], max_s: float | None = None, start_idle_s: float = 2.0,
                      end_idle_s: float = 3.0) -> tuple[Reply, list[dict]]:
    """Speech-loop sessions replayed on their real timeline, as one query: per turn the robot listens
    while the user speaks (``input.wav``, ``input_audio_seconds``), waits until its reply starts
    (``playback_start`` - ``endpoint`` in ``timing.json``), then speaks (``reply.wav``). Listening and
    waiting are idle; the audio track carries the user's voice there and the reply where it speaks."""
    blocks: list[tuple[str, float, Path | None, Reply | None]] = [("idle", start_idle_s, None, None)]
    total = start_idle_s
    for session in sessions:
        for turn in sorted(Path(session).glob("turn_*"), key=lambda t: int(t.name.split("_")[1])):
            tj = turn / "timing.json"
            if not tj.exists() or not (turn / "reply.wav").exists():
                continue
            t = json.loads(tj.read_text())
            if t.get("reply_audio_seconds", 0) < 0.5:  # no reply (e.g. a glitch): the robot only listens
                listen = float(t.get("input_audio_seconds", 0.0))
                blocks.append(("idle", listen + 1.0, turn / "input.wav", None))
                total += listen + 1.0
                continue
            ev = t.get("events", {})
            wait = max(0.2, ev.get("playback_start", 1.0) - ev.get("endpoint", 0.0))
            listen = float(t.get("input_audio_seconds", 0.0))
            reply = load_reply(turn)
            blocks += [("idle", listen + wait, turn / "input.wav", None), ("reply", reply.seconds, turn, reply)]
            total += listen + wait + reply.seconds
            if max_s and total >= max_s:
                break
        if max_s and total >= max_s:
            break
    blocks.append(("idle", end_idle_s, None, None))

    hop = 16000 // round(FPS)
    feats, voiced, pitch, kind, audio, accents, words, timeline = [], [], [], [], [], [], [], []
    f0 = 0
    for kind_name, seconds, src, reply in blocks:
        if kind_name == "reply":
            n = len(reply.feats)
            feats.append(reply.feats)
            voiced.append(reply.voiced)
            pitch.append(reply.pitch)
            a = reply.audio
            accents.append(reply.accents + f0)
            words += [(w, s0 + f0 / FPS, s1 + f0 / FPS) for w, s0, s1 in reply.words]
        else:
            n = round(seconds * FPS)
            feats.append(np.zeros((n, 5)))
            voiced.append(np.zeros(n, bool))
            pitch.append(np.zeros(n))
            a = np.zeros(0)
            if src is not None and src.exists():  # the user's voice while the robot listens
                a, rate = A.load_audio(src)
                if rate != 16000:
                    g = np.gcd(rate, 16000)
                    a = resample_poly(a, 16000 // g, rate // g)
        seg_audio = np.zeros(n * hop)
        a = A.match_level(a) if len(a) else a  # user and robot voices at the same level
        seg_audio[:min(len(a), n * hop)] = a[:n * hop]
        audio.append(seg_audio)
        kind.append(np.full(n, 1 if kind_name == "reply" else 0, np.int8))
        timeline.append({"kind": kind_name, "start_s": f0 / FPS, "seconds": n / FPS, "source": str(src) if src else None})
        f0 += n
    q = Reply(Path("conversation"), np.concatenate(feats), np.concatenate(voiced), np.concatenate(pitch),
              np.concatenate(accents) if accents else np.zeros(0, int), words, f0 / FPS,
              kind=np.concatenate(kind), audio=np.concatenate(audio))
    return q, timeline


def segment(reply: Reply, cfg: GenCfg) -> list[tuple[int, int]]:
    """Frame ranges ~seg_target_s long, cut at word starts or in pauses (pause middles preferred)."""
    n = len(reply.feats)
    speech = reply.feats[:, 4] > 0
    cuts = {int(round(s * FPS)) for w, s, _ in reply.words if w.strip() and w[0].isalnum()}
    pause_mid = set()
    k = 0
    while k < n:  # middles of pauses >= 0.15 s
        if not speech[k]:
            j = k
            while j < n and not speech[j]:
                j += 1
            if j - k >= round(0.15 * FPS):
                pause_mid.add((k + j) // 2)
            k = j
        else:
            k += 1
    cands = np.array(sorted((cuts | pause_mid) - {0}))
    lo, hi, tgt = (round(s * FPS) for s in (cfg.seg_min_s, cfg.seg_max_s, cfg.seg_target_s))
    out, pos = [], 0
    while n - pos > hi:
        ok = cands[(cands >= pos + lo) & (cands <= pos + hi)] if len(cands) else np.array([], int)
        if len(ok):
            score = np.abs(ok - (pos + tgt)) - np.isin(ok, list(pause_mid)) * round(0.3 * FPS)
            c = int(ok[np.argmin(score)])
        else:
            c = pos + tgt
        out.append((pos, c))
        pos = c
    if out and n - pos < lo:  # fold a short tail into the previous segment
        out[-1] = (out[-1][0], n)
    else:
        out.append((pos, n))
    return out


# ---------------------------------------------------------------------------------------- search


def segment_query(q: Reply, cfg: GenCfg) -> list[tuple[int, int]]:
    """``segment`` for a reply; for a conversation, speaking blocks are segmented the same way and
    idle blocks are split evenly into ~``idle_seg_s`` pieces."""
    if q.kind is None:
        return segment(q, cfg)
    out = []
    edges = np.flatnonzero(np.diff(q.kind)) + 1
    for a, b in zip(np.concatenate([[0], edges]), np.concatenate([edges, [len(q.kind)]])):
        a, b = int(a), int(b)
        if q.kind[a] == 1:
            acc = q.accents[(q.accents >= a) & (q.accents < b)] - a
            words = [(w, s0 - a / FPS, s1 - a / FPS) for w, s0, s1 in q.words if a / FPS <= s0 < b / FPS]
            sub = Reply(q.wav, q.feats[a:b], q.voiced[a:b], q.pitch[a:b], acc, words, (b - a) / FPS)
            out += [(a + s0, a + s1) for s0, s1 in segment(sub, cfg)]
        else:
            k = max(1, round((b - a) / (cfg.idle_seg_s * FPS)))
            cuts = np.linspace(a, b, k + 1).round().astype(int)
            out += list(zip(cuts[:-1].tolist(), cuts[1:].tolist()))
    return out


def candidates(units: Units, reply: Reply, seg: tuple[int, int], cfg: GenCfg, rng,
               idle: bool = False) -> tuple[np.ndarray, np.ndarray, dict]:
    """Best ``k`` units for one segment and their costs (without transitions). ``idle``: a listening
    stretch: calm units only, calmer preferred, with a little randomness for variety."""
    qa, qb = seg
    stretch = (qb - qa) / units.length
    ok = np.abs(np.log(stretch)) <= np.log1p(cfg.max_stretch)
    allowed = units.speaker == cfg.speaker if cfg.speaker else np.ones(len(ok), bool)
    if cfg.foot_lock:
        allowed &= units.side_shift <= cfg.max_side_shift
    if idle:
        allowed &= (units.speed_mean < cfg.idle_mean_speed) & (units.speed_peak < cfg.idle_peak_speed)
        idx = np.flatnonzero(ok & allowed)
        if len(idx) < cfg.k:
            idx = np.flatnonzero(allowed)[np.argsort(np.abs(np.log(stretch[allowed])))[: cfg.k * 4]]
        cost = (units.speed_mean[idx] / cfg.idle_mean_speed
                + cfg.w_length * np.abs(np.log(stretch[idx])) / np.log1p(cfg.max_stretch)
                + rng.uniform(0, cfg.idle_noise, len(idx)))
        order = np.argsort(cost)[: cfg.k]
        return idx[order], cost[order], {"speech_frac": 0.0, "accents": [], "idle": True}
    idx = np.flatnonzero(ok & allowed)
    if len(idx) < cfg.k:  # nothing fits closely: take the closest lengths
        idx = np.flatnonzero(allowed)[np.argsort(np.abs(np.log(stretch[allowed])))[: cfg.k * 4]]
    if cfg.random_baseline:
        pick = rng.choice(idx, size=min(cfg.k, len(idx)), replace=False)
        return pick, np.zeros(len(pick)), {}
    cols = [WINDOW_FEATURES.index(f) for f in MATCH]
    q = summarize(reply.feats[qa:qb], reply.voiced[qa:qb], reply.pitch[qa:qb], FPS)[cols]
    qz = (q - units.audio_mu) / units.audio_sd
    d_audio = np.linalg.norm(units.audio_z[idx] - qz, axis=1) / units.audio_scale
    d_len = np.abs(np.log(stretch[idx])) / np.log1p(cfg.max_stretch)
    speech_frac = float(reply.feats[qa:qb, 4].mean())
    # Pauses: calm hands, only in segments that are mostly pause (a 20% pause share must not calm
    # speech; that made every reply subdued, 2026-11-11).
    pause = max(0.0, 0.5 - speech_frac) / 0.5 * units.activity[idx]
    # Intensity: the activity of the units whose own audio is most like this segment (any length).
    # Units that fit a segment's length are calmer than average (long units are calm, short ones are
    # quick beats), so without this the search drifts calm.
    near = np.argpartition(np.linalg.norm(units.audio_z - qz, axis=1), cfg.k_activity)[: cfg.k_activity]
    target = float(units.activity[near].mean())
    d_act = np.abs(units.activity[idx] - target)
    cost = cfg.w_audio * d_audio + cfg.w_length * d_len + cfg.w_pause * pause + cfg.w_activity * d_act
    keep = np.argsort(cost)[: cfg.k_prefilter]
    idx, cost = idx[keep], cost[keep]
    # Timing: reply accents (moved to the output clock, where audio starts LEAD_S late) vs stroke
    # ends of the placed, stretched unit.
    lead = round(LEAD_S * FPS)
    acc = reply.accents + lead
    acc = acc[(acc >= qa) & (acc < qb)]
    if len(acc):
        placed = qa + units.strokes[idx] * stretch[idx][:, None]  # (K, 12), NaN = no stroke
        d = np.abs(acc[None, :, None] - placed[:, None, :])  # (K, accents, strokes)
        d = np.nanmin(np.where(np.isnan(d), np.inf, d), axis=2)
        timing = np.minimum(d, cfg.timing_cap_s * FPS).mean(1) / (cfg.timing_cap_s * FPS)
        cost = cost + cfg.w_timing * timing
    order = np.argsort(cost)[: cfg.k]
    return idx[order], cost[order], {"speech_frac": speech_frac, "accents": acc.tolist(), "activity_target": target}


def search(units: Units, cands: list[np.ndarray], costs: list[np.ndarray], cfg: GenCfg,
           seg_start_s: list[float] | None = None) -> list[int]:
    """Viterbi over segments: node costs + transition costs; a unit may not come back within
    ``reuse_gap_s`` (``seg_start_s``: each segment's start; without it, never).

    Every too-early repeat is forbidden and the search runs again, until none are left. (One repeat
    per pass, 10 passes, was enough for a reply but left a 10-minute conversation reusing 38 idle
    units for 173 segments: a visible listening loop, 2026-11-11.)"""
    costs = [c.copy() for c in costs]
    trans = [None] + [
        cfg.w_transition * units.transition(cands[s - 1][:, None], cands[s][None, :]) / units.trans_scale
        + cfg.w_speaker * (units.speaker[cands[s - 1]][:, None] != units.speaker[cands[s]][None, :])
        for s in range(1, len(cands))
    ]
    for _ in range(200):
        best = costs[0].copy()
        back = []
        for s in range(1, len(cands)):
            tot = best[:, None] + trans[s]
            back.append(np.argmin(tot, axis=0))
            best = tot.min(axis=0) + costs[s]
        path = [int(np.argmin(best))]
        for bk in reversed(back):
            path.append(int(bk[path[-1]]))
        path = path[::-1]
        chosen = [int(cands[s][i]) for s, i in enumerate(path)]
        last, repeats = {}, []
        for s, u in enumerate(chosen):
            t = seg_start_s[s] if seg_start_s else 0.0
            if u in last and (seg_start_s is None or t - last[u] < cfg.reuse_gap_s):
                repeats.append((s, path[s]))
            last[u] = t
        if not repeats:
            return chosen
        for s, i in repeats:  # used earlier in this timeline: forbid here, search again
            costs[s][i] += 1e6
    print(f"[search] warning: {len(repeats)} units still repeat after 200 passes")
    return chosen


# ---------------------------------------------------------------------------------------- stitch


def _load_pkl(path: str, cache: dict) -> dict:
    if path not in cache:
        with open(path, "rb") as f:
            d = pickle.load(f)
        if int(d["fps"]) != PKL_FPS:
            raise ValueError(f"{path}: {d['fps']} fps, expected {PKL_FPS}")
        cache[path] = {k: np.asarray(d[k], float) for k in ("root_pos", "root_rot", "dof_pos")}
    return cache[path]


def _slerp(q0: np.ndarray, q1: np.ndarray, t: np.ndarray) -> np.ndarray:
    """Row-wise slerp of xyzw quaternions."""
    dot = (q0 * q1).sum(-1, keepdims=True)
    q1 = np.where(dot < 0, -q1, q1)
    dot = np.abs(dot)
    t = np.asarray(t, float).reshape(-1, 1)
    theta = np.arccos(np.clip(dot, -1, 1))
    small = theta < 1e-6
    s = np.sin(theta)
    w0 = np.where(small, 1 - t, np.sin((1 - t) * theta) / np.where(small, 1, s))
    w1 = np.where(small, t, np.sin(t * theta) / np.where(small, 1, s))
    q = w0 * q0 + w1 * q1
    return q / np.linalg.norm(q, axis=-1, keepdims=True)


def _sample(clip: dict, src_t: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Root position, rotation (xyzw) and joints of a 30 fps clip at times src_t (s), clamped."""
    n = len(clip["dof_pos"])
    f = np.clip(np.asarray(src_t) * PKL_FPS, 0, n - 1)
    i0 = np.floor(f).astype(int)
    i1 = np.minimum(i0 + 1, n - 1)
    w = (f - i0)[:, None]
    pos = (1 - w) * clip["root_pos"][i0] + w * clip["root_pos"][i1]
    dof = (1 - w) * clip["dof_pos"][i0] + w * clip["dof_pos"][i1]
    rot = _slerp(clip["root_rot"][i0], clip["root_rot"][i1], w[:, 0])
    return pos, rot, dof


def _yaw(q_xyzw: np.ndarray) -> float:
    """Heading of a trunk orientation: direction of its x axis projected on the floor."""
    x, y, z, w = q_xyzw
    fx = 1 - 2 * (y * y + z * z)
    fy = 2 * (x * y + w * z)
    return float(np.arctan2(fy, fx))


def _yaw_quat(yaw: float) -> np.ndarray:
    return np.array([0.0, 0.0, np.sin(yaw / 2), np.cos(yaw / 2)])


def _quat_mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """xyzw quaternion product a * b (rows)."""
    ax, ay, az, aw = np.moveaxis(np.atleast_2d(a), -1, 0)
    bx, by, bz, bw = np.moveaxis(np.atleast_2d(b), -1, 0)
    return np.stack([aw * bx + ax * bw + ay * bz - az * by, aw * by - ax * bz + ay * bw + az * bx,
                     aw * bz + ax * by - ay * bx + az * bw, aw * bw - ax * bx - ay * by - az * bz], -1)


def stitch(units: Units, segs: list[tuple[int, int]], chosen: list[int], cfg: GenCfg) -> dict:
    """The output motion at 30 fps (GMR .pkl layout)."""
    cache: dict = {}
    n_out = int(np.ceil(segs[-1][1] / FPS * PKL_FPS))
    t_out = np.arange(n_out) / PKL_FPS
    pieces = []  # per segment: (clip arrays, segment start/end s, unit start s, stretch, yaw, R, offset)
    prev_end = None
    for (qa, qb), u in zip(segs, chosen):
        clip = _load_pkl(str(units.source[units.clip[u]]), cache)
        s0, s1 = qa / FPS, qb / FPS
        ua = units.a[u] / FPS
        stretch = (qb - qa) / units.length[u]
        p0, r0, _ = _sample(clip, np.array([ua]))
        if prev_end is None:
            dyaw, shift = -_yaw(r0[0]), -p0[0, :2]
            target_xy = np.zeros(2)
        else:
            dyaw = _yaw(prev_end[1]) - _yaw(r0[0])
            target_xy = prev_end[0][:2]
        c, s = np.cos(dyaw), np.sin(dyaw)
        Rz = np.array([[c, -s], [s, c]])
        offset = target_xy - Rz @ p0[0, :2] if prev_end is not None else Rz @ shift
        pieces.append((clip, s0, s1, ua, stretch, dyaw, Rz, offset))
        end_src = ua + (s1 - s0) / stretch
        pe, re, _ = _sample(clip, np.array([end_src]))
        prev_end = (np.concatenate([Rz @ pe[0, :2] + offset, pe[0, 2:]]), _quat_mul(_yaw_quat(dyaw), re)[0])

    def piece_at(p, t):
        clip, s0, _, ua, stretch, dyaw, Rz, offset = p
        pos, rot, dof = _sample(clip, ua + (t - s0) / stretch)
        pos = np.column_stack([pos[:, :2] @ Rz.T + offset, pos[:, 2]])
        rot = _quat_mul(np.repeat(_yaw_quat(dyaw)[None], len(t), 0), rot)
        return pos, rot, dof

    root_pos, root_rot, dof = np.zeros((n_out, 3)), np.zeros((n_out, 4)), np.zeros((n_out, 22))
    seg_of = np.searchsorted([p[2] for p in pieces], t_out, side="right").clip(0, len(pieces) - 1)
    for s, p in enumerate(pieces):
        m = seg_of == s
        root_pos[m], root_rot[m], dof[m] = piece_at(p, t_out[m])
    seam_s = []
    for s in range(1, len(pieces)):  # crossfade around each cut, using frames past the cut in the sources
        tb = pieces[s][1]
        # Long enough that no joint crossfades faster than max_seam_speed (a smoothstep over T moving
        # by d peaks at 1.5 d / T): two units can hold their hands alike with very different forearm
        # twist, and 0.8 rad in 0.3 s spun an elbow at 5.5 rad/s (2026-11-11).
        d = np.abs(piece_at(pieces[s - 1], np.array([tb]))[2] - piece_at(pieces[s], np.array([tb]))[2]).max()
        room = min(pieces[s - 1][2] - pieces[s - 1][1], pieces[s][2] - pieces[s][1])  # shorter segment
        T = float(np.clip(1.5 * d / cfg.max_seam_speed, cfg.crossfade_s, min(cfg.max_crossfade_s, room)))
        seam_s.append(T)
        half = T / 2
        m = np.abs(t_out - tb) < half
        if not m.any():
            continue
        t = t_out[m]
        a = (t - (tb - half)) / (2 * half)
        a = (a * a * (3 - 2 * a))[:, None]  # smoothstep
        lp, lr, ld = piece_at(pieces[s - 1], t)
        rp, rr, rd = piece_at(pieces[s], t)
        root_pos[m] = (1 - a) * lp + a * rp
        dof[m] = (1 - a) * ld + a * rd
        root_rot[m] = _slerp(lr, rr, a[:, 0])
    return {"fps": PKL_FPS, "root_pos": root_pos, "root_rot": root_rot, "dof_pos": dof,
            "local_body_pos": None, "link_body_list": None, "_crossfade_s": seam_s}


# ---------------------------------------------------------------------------------------- foot lock


def _heading(R: np.ndarray) -> float:
    return float(np.arctan2(R[1, 0], R[0, 0]))


def _wrap(a):
    return (np.asarray(a) + np.pi) % (2 * np.pi) - np.pi


def _solve_leg_soft(g, foot: dict, target: np.ndarray, yaw_target: float, q0: np.ndarray,
                    w_tilt: float = 0.5, w_yaw: float = 0.05) -> tuple[np.ndarray, float]:
    """Leg joints putting the foot at ``target`` (exact), sole level (weighted), and its heading
    near ``yaw_target`` (soft: gives way at joint limits). Damped Gauss-Newton from ``q0`` (the
    previous frame's answer, to stay on one solution). Returns (q, position error in m).

    ``ground_clip.Grounder.solve_leg`` demands position *and* full orientation equally; when the
    trunk twists against locked feet that can't be met within the hip's range, and it diverged
    (2026-11-11, a 2.5 m miss)."""
    rob, data = g.rob, g.data
    adr = foot["leg_adr"]
    q = q0.copy()

    def residual(x):
        data.qpos[adr] = x
        mujoco.mj_kinematics(rob, data)
        R = data.xmat[foot["body"]].reshape(3, 3)
        up = R @ foot["up_local"]
        return np.concatenate([target - data.xpos[foot["body"]], w_tilt * up[:2],
                               [w_yaw * _wrap(yaw_target - _heading(R))]])

    for _ in range(30):
        f = residual(q)
        if np.abs(f).max() < 1e-6:
            break
        eps = 1e-6
        J = np.column_stack([(residual(q + eps * e) - f) / eps for e in np.eye(len(q))])
        step = np.linalg.solve(J.T @ J + 1e-4 * np.eye(len(q)), J.T @ f)
        q = np.clip(q - np.clip(step, -0.1, 0.1), foot["leg_lo"], foot["leg_hi"])
    return q, float(np.linalg.norm(residual(q)[:3]))


def foot_lock(motion: dict, grounder, max_residual_m: float = 0.005, smooth_s: float = 0.8) -> dict:
    """Keep both feet on one stance for the whole reply.

    Every unit brings its own stance (feet width, angle), so blending their legs slides the feet. Per
    frame: the **stance frame** sits between the feet, x pointing forward (perpendicular to the line
    from the right foot to the left). The trunk's pose relative to that frame is kept (its sway and
    lean), but placed on one fixed stance: the first frame's stance frame, with each foot at its median
    position in stance coordinates. Leg IK (``_solve_leg_soft``) then reaches those feet.

    The stance frame is smoothed over ``smooth_s``: within a unit the feet are planted (no change), and
    at a seam between units with different trunk twist the trunk turns over ~0.8 s instead of during
    the 0.3 s crossfade (which flicked a knee at 3.2 rad/s, 2026-11-11)."""
    g = grounder
    n = len(motion["dof_pos"])
    root_pos, root_rot, dof = (np.array(motion[k], float) for k in ("root_pos", "root_rot", "dof_pos"))
    sides = list(g.feet)  # "left", "right"
    foot_p = {s: np.zeros((n, 3)) for s in sides}
    foot_R = {s: np.zeros((n, 3, 3)) for s in sides}
    for t in range(n):
        g.set_pose(root_pos[t], root_rot[t], dof[t])
        for s in sides:
            foot_p[s][t] = g.data.xpos[g.feet[s]["body"]]
            foot_R[s][t] = g.data.xmat[g.feet[s]["body"]].reshape(3, 3)
    mid = (foot_p["left"][:, :2] + foot_p["right"][:, :2]) / 2
    across = foot_p["left"][:, :2] - foot_p["right"][:, :2]
    yaw = np.arctan2(across[:, 1], across[:, 0]) - np.pi / 2  # stance x = forward
    w = max(1, round(smooth_s * PKL_FPS))
    yaw = uniform_filter1d(np.unwrap(yaw), w, mode="nearest")
    mid = uniform_filter1d(mid, w, axis=0, mode="nearest")

    def to_stance(t, xy):  # world xy -> stance coordinates of frame t
        c, s_ = np.cos(-yaw[t]), np.sin(-yaw[t])
        d = xy - mid[t]
        return np.array([c * d[0] - s_ * d[1], s_ * d[0] + c * d[1]])

    def from_stance(xy):  # stance coordinates -> world xy of the fixed stance
        c, s_ = np.cos(yaw[0]), np.sin(yaw[0])
        return mid[0] + np.array([c * xy[0] - s_ * xy[1], s_ * xy[0] + c * xy[1]])

    canon = {s: np.median([to_stance(t, foot_p[s][t, :2]) for t in range(n)], axis=0) for s in sides}
    # Circular mean: foot angles near +-180 deg must not average to 0.
    canon_yaw = {s: float(np.angle(np.mean(np.exp(1j * _wrap([_heading(foot_R[s][t]) - yaw[t] for t in range(n)])))))
                 for s in sides}
    out_pos, out_rot, out_dof = root_pos.copy(), root_rot.copy(), dof.copy()
    q_prev = {s: dof[0, g.feet[s]["leg_cols"]].copy() for s in sides}
    q_good = dict(q_prev)  # the last pose that reached its target
    worst, fails, fail_frames = 0.0, 0, []
    for t in range(n):
        dyaw = yaw[0] - yaw[t]
        out_pos[t, :2] = from_stance(to_stance(t, root_pos[t, :2]))
        out_rot[t] = _quat_mul(_yaw_quat(dyaw), root_rot[t])[0]
        g.set_pose(out_pos[t], out_rot[t], dof[t])
        for s in sides:
            target = np.concatenate([from_stance(canon[s]), foot_p[s][t, 2:]])
            q, res = _solve_leg_soft(g, g.feet[s], target, yaw[0] + canon_yaw[s], q_prev[s])
            if res > max_residual_m:
                # Retry from fresh starts: this frame's own (unlocked) legs and the last good pose.
                # Without this one bad frame cascaded: every later frame started from the stuck pose
                # and a leg stayed unsolved for 106 s of a 10-min conversation (2026-11-11).
                for seed in (dof[t, g.feet[s]["leg_cols"]], q_good[s]):
                    q2, r2 = _solve_leg_soft(g, g.feet[s], target, yaw[0] + canon_yaw[s], seed)
                    if r2 < res:
                        q, res = q2, r2
            if res > max_residual_m:  # still unreachable: hold the last good legs rather than jump
                fails += 1
                fail_frames.append(t)
                q = q_good[s]
            else:
                q_good[s] = q
                worst = max(worst, res)
            g.data.qpos[g.feet[s]["leg_adr"]] = q
            out_dof[t, g.feet[s]["leg_cols"]] = q
            q_prev[s] = q
    motion = {**motion, "root_pos": out_pos, "root_rot": out_rot, "dof_pos": out_dof}
    motion["_foot_lock"] = {"worst_residual_m": float(worst), "frames_over": int(fails),
                            "stance_width_cm": float(np.linalg.norm(canon["left"] - canon["right"]) * 100),
                            "held_s": [round(f / PKL_FPS, 2) for f in sorted(set(fail_frames))][:200]}
    return motion


# ---------------------------------------------------------------------------------------- run


def _tool(name: str):
    sys.path.insert(0, str(REPO / "tools"))
    try:
        return __import__(name)
    finally:
        sys.path.pop(0)


def generate(cfg: GenCfg, units: Units | None = None, query: Reply | None = None, name: str | None = None,
             timeline: list[dict] | None = None) -> Path:
    """One reply (``cfg.reply``) or a prepared query (``load_conversation``) -> reference folder."""
    rng = np.random.default_rng(cfg.seed)
    units = units or Units(cfg.library)
    t0 = time.perf_counter()
    reply = query if query is not None else load_reply(cfg.reply)
    t_feat = time.perf_counter() - t0
    segs = segment_query(reply, cfg)
    cands, costs, info = [], [], []
    for seg in segs:
        idle = reply.kind is not None and reply.kind[seg[0]] == 0
        c, k, i = candidates(units, reply, seg, cfg, rng, idle=idle)
        cands.append(c)
        costs.append(k)
        info.append(i)
    chosen = search(units, cands, costs, cfg, [a / FPS for a, _ in segs])
    t_search = time.perf_counter() - t0 - t_feat
    motion = stitch(units, segs, chosen, cfg)
    crossfades = motion.pop("_crossfade_s")
    t_stitch = time.perf_counter() - t0 - t_feat - t_search

    turn = cfg.reply if cfg.reply.is_dir() else cfg.reply.parent
    name = name or cfg.name or f"{turn.parent.name}_{turn.name}" + ("_random" if cfg.random_baseline else "")
    out = cfg.out_dir / name
    out.mkdir(parents=True, exist_ok=True)
    raw_pkl, grounded = out / "motion.pkl", out / "motion_grounded.pkl"
    with open(raw_pkl, "wb") as f:
        pickle.dump(motion, f)
    gc, qc = _tool("ground_clip"), _tool("clip_qc")
    grounder = gc.Grounder(gc.DEFAULT_GMR_XML, gc.DEFAULT_ROBOT_XML)
    lock = {}
    if cfg.foot_lock:
        t1 = time.perf_counter()
        motion = foot_lock(motion, grounder)
        lock = {**motion.pop("_foot_lock"), "seconds": time.perf_counter() - t1}
        if lock["frames_over"]:
            print(f"[generate] WARNING: foot lock couldn't reach the stance on {lock['frames_over']} frames "
                  f"(worst {lock['worst_residual_m'] * 100:.1f} cm): legs held, feet will jump. Try --speaker.")
        with open(raw_pkl, "wb") as f:
            pickle.dump(motion, f)
    t1 = time.perf_counter()
    grounder.ground(raw_pkl, grounded)
    t_ground = time.perf_counter() - t1
    t1 = time.perf_counter()
    row = qc.K1Checker().check(grounded)
    qc.flag([row])
    t_qc = time.perf_counter() - t1
    from booster_mjlab.scripts.upload_motion import convert_batched

    t1 = time.perf_counter()
    arrays = convert_batched(grounded)
    t_convert = time.perf_counter() - t1
    n = len(arrays["joint_pos"])
    np.savez(out / "reference.npz", **arrays, clip_names=np.array([name]), clip_lengths=np.array([n]))
    from scipy.io import wavfile

    track = reply.audio if reply.kind is not None else A.match_level(reply.audio)  # conversations: per voice
    wavfile.write(out / "reply.wav", 16000, (np.clip(track, -1, 1) * 32767).astype(np.int16))
    np.savez(out / "query.npz", feats=reply.feats, voiced=reply.voiced, pitch=reply.pitch, accents=reply.accents,
             kind=reply.kind if reply.kind is not None else np.ones(len(reply.feats), np.int8))

    lib = units.lib
    plan = {
        "reply": str(cfg.reply) if query is None else None, "timeline": timeline,
        "cfg": {k: str(v) for k, v in asdict(cfg).items()},
        "audio_offset_s": LEAD_S, "reply_s": reply.seconds, "frames_50fps": n,
        # features..ground = what a robot needs at runtime; qc + convert (forward kinematics for body
        # positions, used only by checks and videos) are offline extras.
        "time_s": {"features": t_feat, "search": t_search, "stitch": t_stitch, "foot_lock": lock.get("seconds", 0.0),
                   "ground": t_ground, "qc": t_qc, "convert": t_convert},
        "qc": {"flags": row.get("flags", []), "severe": row.get("severe", [])}, "foot_lock": lock,
        "crossfade_s": crossfades,
        "segments": [{"start_s": a / FPS, "end_s": b / FPS, "unit": int(u), "clip": str(lib.names[units.clip[u]]),
                      "speaker": str(lib.speaker[units.clip[u]]), "unit_frames": [int(units.a[u]), int(units.b[u])],
                      "stretch": float((b - a) / units.length[u]), "cost": float(costs[s][list(cands[s]).index(u)]),
                      "continues_previous": bool(s and units.next[chosen[s - 1]] == u),
                      "speech_frac": info[s].get("speech_frac"), "accents_out_frames": info[s].get("accents"),
                      "idle": bool(info[s].get("idle", False))}
                     for s, ((a, b), u) in enumerate(zip(segs, chosen))],
    }
    (out / "plan.json").write_text(json.dumps(plan, indent=1))
    print(f"[generate] {name}: {reply.seconds:.1f} s, {len(segs)} segments, "
          f"features {t_feat * 1000:.0f} ms, search {t_search * 1000:.0f} ms, stitch {t_stitch * 1000:.0f} ms; "
          f"foot lock {lock.get('seconds', 0):.1f} s (worst IK residual {lock.get('worst_residual_m', 0) * 1000:.1f} mm); "
          f"QC flags: {row.get('flags') or 'none'}, severe: {row.get('severe') or 'none'} -> {out}")
    return out


@dataclass
class RenderCfg:
    dir: Path
    """A folder written by ``gesture generate``."""
    wandb_run_path: str = "bmcox2-university-of-illinois-urbana-champaign/mjlab/y1r48dhc"
    blend_s: float = 2.0
    hold_start_s: float = 1.0
    push: bool = False
    obs_delay_steps: int = 0
    runs: int = 1
    video: bool = True


def render(cfg: RenderCfg) -> str:
    """sim2sim from standing on the reference (lead-in blend + hold, as on the robot), then the reply's
    audio dubbed on, delayed by the lead-in plus ``audio_offset_s``. Returns sim2sim's summary line."""
    import os
    import subprocess

    plan = json.loads((cfg.dir / "plan.json").read_text())
    name = str(np.load(cfg.dir / "reference.npz")["clip_names"][0])
    video = cfg.dir / "sim.mp4"
    cmd = [sys.executable, "-m", "booster_mjlab.scripts.sim2sim", "--wandb-run-path", cfg.wandb_run_path,
           "--motion-file", str(cfg.dir / "reference.npz"), "--clip", name, "--start", "stand",
           "--blend-s", str(cfg.blend_s), "--hold-start-s", str(cfg.hold_start_s), "--runs", str(cfg.runs),
           "--obs-delay-steps", str(cfg.obs_delay_steps)]
    if cfg.push:
        cmd.append("--push")
    if cfg.video:
        cmd += ["--video", str(video)]
    res = subprocess.run(cmd, capture_output=True, text=True, env={**os.environ, "MUJOCO_GL": "egl"})
    lines = [ln for ln in res.stdout.splitlines() if ln.startswith(("[sim2sim]", "  run"))]
    if res.returncode != 0:
        raise RuntimeError(res.stderr[-2000:])
    summary = lines[-1] if lines else "?"
    if cfg.video:
        delay_ms = round((cfg.blend_s + cfg.hold_start_s + plan["audio_offset_s"]) * 1000)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video), "-i", str(cfg.dir / "reply.wav"),
                        "-af", f"adelay=delays={delay_ms}:all=1", "-c:v", "copy", "-c:a", "aac",
                        str(cfg.dir / "sim_audio.mp4")], check=True)
    print(f"[render] {cfg.dir.name}: {summary}" + (f" -> {cfg.dir / 'sim_audio.mp4'}" if cfg.video else ""))
    return summary


@dataclass
class CheckCfg:
    dirs: tuple[Path, ...]
    """Folders written by ``gesture generate`` (e.g. logs/gesture/replies/*)."""


def check_reference(d: Path) -> dict:
    """Numbers for one generated reference (step 3 exit criteria; step 5 reuses them):
    seams (fastest joint near a seam vs elsewhere), feet travel, Gate 1 flags, how animated it is,
    strong accents with a stroke end within 0.14 s, hand speed in pauses vs while talking."""
    from booster_mjlab.gesture.analysis import stroke_ends
    from booster_mjlab.gesture.motion import hand_features
    from booster_mjlab.gesture.library import body_names

    plan = json.loads((d / "plan.json").read_text())
    z = np.load(d / "reference.npz")
    bn = body_names()
    q = z["joint_pos"]
    v = np.abs(np.diff(q, axis=0)) * FPS
    near = np.zeros(len(v), bool)
    for seg, cf in zip(plan["segments"][1:], plan.get("crossfade_s", [])):
        k, h = round(seg["start_s"] * FPS), round(max(cf, 0.3) * FPS / 2) + 2
        near[max(0, k - h):k + h] = True
    feet = [bn.index(f) for f in ("left_foot_link", "right_foot_link")]
    travel = max(np.linalg.norm(np.diff(z["body_pos_w"][:, f, :2], axis=0), axis=1).sum() for f in feet)
    speed = hand_features(z["body_pos_w"], z["body_quat_w"], bn, FPS)[:, 2]
    qz = np.load(d / "query.npz") if (d / "query.npz").exists() else None
    reply = load_reply(Path(plan["reply"])) if qz is None else None
    feats = qz["feats"] if qz is not None else reply.feats
    kind = qz["kind"] if qz is not None else np.ones(len(feats), np.int8)
    acc0 = qz["accents"] if qz is not None else reply.accents
    lead = round(plan["audio_offset_s"] * FPS)
    acc = acc0 + lead
    acc = acc[acc < len(speed)]
    ends = stroke_ends(speed, FPS)
    hits = [bool(len(ends) and np.min(np.abs(ends - a)) <= 7) for a in acc]
    # Chance: the same strokes against accents moved to random times (livelier motion has more
    # strokes, so it hits more accents by luck alone).
    rng = np.random.default_rng(0)
    fake = rng.integers(lead, len(speed), size=(500, max(len(acc), 1)))
    chance = float(np.mean(np.min(np.abs(ends[None, None, :] - fake[..., None]), axis=-1) <= 7)) if len(ends) else 0.0
    sp = feats[:, 4] > 0
    n = min(len(sp), len(speed) - lead)
    s_al, k_al = speed[lead:lead + n], kind[:n]
    talk, pause = s_al[sp[:n] & (k_al == 1)], s_al[~sp[:n] & (k_al == 1)]
    idle = s_al[k_al == 0]
    return {
        "name": d.name, "seconds": len(q) / FPS, "segments": len(plan["segments"]),
        "seam_max_speed": float(v[near].max()) if near.any() else 0.0,
        "other_max_speed": float(v[~near].max()), "feet_travel_cm": float(travel * 100),
        "qc_flags": plan["qc"]["flags"], "qc_severe": plan["qc"]["severe"],
        "hand_speed": float(speed.mean()), "accents": int(len(acc)), "accent_hits": int(sum(hits)), "accent_chance": chance,
        "hand_speed_pause": float(pause.mean()) if len(pause) else float("nan"),
        "hand_speed_talk": float(talk.mean()), "pause_s": float(len(pause) / FPS),
        "hand_speed_idle": float(idle.mean()) if len(idle) else float("nan"), "idle_s": float(len(idle) / FPS),
        "speakers": sorted({x["speaker"] for x in plan["segments"]}),
    }


def check(cfg: CheckCfg) -> list[dict]:
    rows = [check_reference(Path(d)) for d in sorted(cfg.dirs) if (Path(d) / "plan.json").exists()]
    print(f"{'reference':38} {'segs':>4} {'seam/other max rad/s':>20} {'feet cm':>7} {'hands m/s':>9} "
          f"{'accent hits (chance)':>20} {'pause/talk m/s':>15} {'idle m/s':>8}  QC")
    for r in rows:
        print(f"{r['name']:38} {r['segments']:4} {r['seam_max_speed']:9.1f} / {r['other_max_speed']:<8.1f} "
              f"{r['feet_travel_cm']:7.1f} {r['hand_speed']:9.2f} {r['accent_hits']:5}/{r['accents']:<3} ({100 * r['accent_chance']:3.0f}%)    "
              f"{r['hand_speed_pause']:7.2f}/{r['hand_speed_talk']:.2f} {r['hand_speed_idle']:8.2f}  {r['qc_severe'] or r['qc_flags'] or 'ok'}")
    for kind in ("matched", "random"):
        R = [r for r in rows if r["name"].endswith("_random") == (kind == "random")]
        if not R:
            continue
        acc = sum(r["accents"] for r in R)
        print(f"{kind:8}: {len(R)} refs, accents hit {sum(r['accent_hits'] for r in R)}/{acc} "
              f"({100 * sum(r['accent_hits'] for r in R) / max(acc, 1):.0f}%; chance {100 * sum(r['accent_chance'] * r['accents'] for r in R) / max(acc, 1):.0f}%), mean hand speed "
              f"{np.mean([r['hand_speed'] for r in R]):.2f} m/s, worst seam {max(r['seam_max_speed'] for r in R):.1f} rad/s, "
              f"max feet travel {max(r['feet_travel_cm'] for r in R):.1f} cm, severe QC {sum(bool(r['qc_severe']) for r in R)}")
    return rows


@dataclass
class ConversationCfg:
    sessions: tuple[Path, ...]
    """Speech-loop session folders (speech/runs/<session>), replayed in order."""
    max_minutes: float | None = None
    name: str | None = None
    library: Path = GenCfg.library
    out_dir: Path = Path("logs/gesture/conversations")
    seed: int = 0
    speaker: str | None = "9_miranda"
    """The persona: every unit from one speaker. Mixing speakers mixes stances (feet width, trunk twist:
    Lawrence twists ~2x Miranda), and one locked stance couldn't reach all of them (foot-lock IK
    failed on 299 frames of a 10-min mixed run, 2026-11-11). Miranda: least twist, most calm units."""


def conversation(cfg: ConversationCfg) -> Path:
    """A whole conversation (idle while listening, gestures while speaking) as one reference."""
    q, timeline = load_conversation(list(cfg.sessions), cfg.max_minutes * 60 if cfg.max_minutes else None)
    name = cfg.name or "conv_" + "+".join(Path(s).name for s in cfg.sessions) + (f"_{cfg.max_minutes:g}min" if cfg.max_minutes else "")
    gcfg = GenCfg(reply=Path(cfg.sessions[0]), library=cfg.library, out_dir=cfg.out_dir, seed=cfg.seed, speaker=cfg.speaker)
    n_turns = sum(t["kind"] == "reply" for t in timeline)
    speaking = sum(t["seconds"] for t in timeline if t["kind"] == "reply")
    print(f"[conversation] {q.seconds / 60:.1f} min, {n_turns} replies, robot speaking {speaking / q.seconds:.0%}")
    return generate(gcfg, query=q, name=name, timeline=timeline)


@dataclass
class ReplayCfg:
    session: Path
    """A speech-loop session folder (speech/runs/<session>)."""
    speaker: str | None = "9_miranda"
    video: bool = True
    out_dir: Path = Path("logs/gesture/conversations")


def replay(cfg: ReplayCfg) -> Path:
    """A recorded conversation as one dubbed sim video: ``conversation`` + ``render`` + ``check``."""
    out = conversation(ConversationCfg(sessions=(cfg.session,), name=f"conv_{cfg.session.name}",
                                       out_dir=cfg.out_dir, speaker=cfg.speaker))
    render(RenderCfg(dir=out, video=cfg.video))
    check(CheckCfg(dirs=(out,)))
    return out
