"""Does speech audio predict hand motion, and by how much? (notes/gesture_plan.md step 2)

Retrieval picks motion whose *own* audio resembles the new speech. That only works if similar
audio goes with similar motion. Three levels, each against a baseline that ignores the audio:

1. **Frames:** lagged correlation of each audio feature with hand speed (which features move
   with the hands, and how far ahead the hands are).
2. **Windows** (1 s and 2 s): summarize a window's audio (loudness, onsets, pitch movement, pauses)
   and predict how much the hands move in it.
   - ridge regression, tested on takes it never saw (same speakers) and on a speaker it never saw
     (a new voice, like the robot's TTS);
   - nearest neighbours: the hand motion of the most similar-sounding windows of *other* speakers.
   Baseline: the same model trained on shuffled labels (what chance looks like with this much data).
3. **Units:** the same nearest-neighbour test on gesture units, the pieces retrieval will use.

"How much the hands move" is mean hand speed, z-scored per take: how animated someone is *for
them* right now, so a calm speaker's big gesture counts as much as an animated speaker's. Audio
is normalized per take the same way, which is also how the robot's TTS will be normalized.

A correlation r explains r^2 of the variation: r = 0.3 is a real but partial relation (9%).
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.ndimage import uniform_filter1d

from booster_mjlab.gesture.sync import lagged_corr

FRAME_FEATURES = ("loudness", "onset", "voicing", "pitch", "speech")
WINDOW_FEATURES = ("loud_mean", "loud_std", "loud_max", "onset_mean", "onset_rate", "speech_frac",
                   "voiced_frac", "pitch_mean", "pitch_std", "pitch_range")


@dataclass
class AnalysisCfg:
    library: Path = Path.home() / "robotics/data/gesture/library_v0.npz"
    out_dir: Path = Path("logs/gesture")
    max_lag_s: float = 1.0
    window_s: tuple[float, ...] = (1.0, 2.0)
    hop_s: float = 0.5
    k: int = 20
    ridge: float = 10.0
    permutations: int = 20
    seed: int = 0


# ---------------------------------------------------------------------------------------- data


class Lib:
    """The library npz plus per-take-normalized frame features for analysis."""

    def __init__(self, path: Path):
        L = np.load(path)
        self.fps = float(L["fps"])
        self.names = L["clip_name"]
        self.take = L["clip_take"]
        self.speaker = L["clip_speaker"]
        self.offset, self.length = L["clip_offset"].astype(int), L["clip_length"].astype(int)
        self.speed = L["motion"][:, list(L["motion_features"]).index("speed")].astype(np.float64)
        self.units = np.stack([L["unit_clip"], L["unit_start"], L["unit_end"]], 1).astype(int)
        raw = L["audio"].astype(np.float64)
        af = list(L["audio_features"])
        loud, onset, voiced, pitch, speech = (raw[:, af.index(n)] for n in
                                              ("loud_db", "onset", "voiced", "pitch_st", "speech"))
        onset = np.log1p(onset)  # spectral flux is very skewed; log keeps spikes from dominating
        feats = np.zeros((len(raw), len(FRAME_FEATURES)))
        for t in np.unique(self.take):
            rows = np.concatenate([np.arange(o, o + n) for o, n in zip(self.offset[self.take == t],
                                                                       self.length[self.take == t])])
            sp = rows[speech[rows] > 0] if np.any(speech[rows] > 0) else rows
            for j, x in enumerate((loud, onset)):  # z-score on this take's speech frames
                feats[rows, j] = (x[rows] - x[sp].mean()) / (x[sp].std() + 1e-9)
        feats[:, 2] = voiced
        feats[:, 4] = speech
        # Pitch contour: semitones where voiced, bridged across short unvoiced gaps, 0 in pauses.
        for o, n in zip(self.offset, self.length):
            p = np.where(pitch[o:o + n] != 0, pitch[o:o + n], np.nan)
            ok = ~np.isnan(p)
            if ok.sum() >= 2:
                p = np.interp(np.arange(n), np.flatnonzero(ok), p[ok])
            feats[o:o + n, 3] = np.where(speech[o:o + n] > 0, np.nan_to_num(p), 0.0)
        self.feats = feats
        self.voiced_mask = (pitch != 0) & (voiced > 0)
        self.raw_pitch = pitch

    def clip(self, i: int) -> slice:
        return slice(self.offset[i], self.offset[i] + self.length[i])


def recording_features(raw: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """``Lib``'s normalization for one continuous recording (e.g. a TTS reply): raw
    ``audio.speech_features`` -> (FRAME_FEATURES, voiced mask, raw pitch). Must stay identical to
    ``Lib.__init__`` for a take with one clip (``tests/test_gesture.py`` checks it), or replies and
    library units would be compared on different scales."""
    loud, onset, voiced, pitch, speech = (raw[:, j].astype(np.float64) for j in range(5))
    onset = np.log1p(onset)
    sp = speech > 0 if np.any(speech > 0) else np.ones(len(raw), bool)
    feats = np.zeros((len(raw), len(FRAME_FEATURES)))
    for j, x in enumerate((loud, onset)):
        feats[:, j] = (x - x[sp].mean()) / (x[sp].std() + 1e-9)
    feats[:, 2] = voiced
    feats[:, 4] = speech
    p = np.where(pitch != 0, pitch, np.nan)
    ok = ~np.isnan(p)
    if ok.sum() >= 2:
        p = np.interp(np.arange(len(p)), np.flatnonzero(ok), p[ok])
    feats[:, 3] = np.where(speech > 0, np.nan_to_num(p), 0.0)
    return feats, (pitch != 0) & (voiced > 0), pitch


# ---------------------------------------------------------------------------------------- 1. frames


def frame_level(lib: Lib, max_lag: int) -> dict:
    """Pooled lagged correlation of each frame feature with hand speed (positive lag = hands after)."""
    out = {}
    spk_all = np.unique(lib.speaker)
    for j, name in enumerate(FRAME_FEATURES):
        tot, wt, per_spk = 0.0, 0.0, {}
        for s in spk_all:
            st, sw = 0.0, 0.0
            for i in np.flatnonzero(lib.speaker == s):
                sl = lib.clip(i)
                f, v = lib.feats[sl, j], lib.speed[sl]
                if f.std() < 1e-9:
                    continue
                c = lagged_corr(f, v, max_lag)
                n = np.array([len(f) - abs(L) for L in range(-max_lag, max_lag + 1)], float)
                st = st + np.nan_to_num(c) * n
                sw = sw + n
            per_spk[s] = st / np.maximum(sw, 1)
            tot, wt = tot + st, wt + sw
        pooled = tot / np.maximum(wt, 1)
        b = int(np.argmax(np.abs(pooled)))
        out[name] = {"curve": pooled, "best_lag_s": (b - max_lag) / lib.fps, "best_r": float(pooled[b]),
                     "r_at_0": float(pooled[max_lag]),
                     "per_speaker_best": {s: ((int(np.argmax(np.abs(c))) - max_lag) / lib.fps,
                                              float(c[int(np.argmax(np.abs(c)))])) for s, c in per_spk.items()}}
    return out


# ---------------------------------------------------------------------------------------- 2. windows


def summarize(f: np.ndarray, voiced: np.ndarray, pitch: np.ndarray, fps: float) -> np.ndarray:
    """WINDOW_FEATURES of one stretch of frame features."""
    loud, onset, _, _, speech = f.T
    o = onset
    peaks = np.sum((o[1:-1] > 1.0) & (o[1:-1] >= o[:-2]) & (o[1:-1] > o[2:]))
    pv = pitch[voiced]
    has = len(pv) >= 5
    return np.array([
        loud.mean(), loud.std(), loud.max(), onset.mean(), peaks / (len(f) / fps), speech.mean(), voiced.mean(),
        pv.mean() if has else 0.0, pv.std() if has else 0.0,
        (np.percentile(pv, 90) - np.percentile(pv, 10)) if has else 0.0,
    ])


def windows(lib: Lib, win: int, hop: int, lead: int):
    """Audio summaries X, target y (mean hand speed, z-scored per take), take and speaker per window.
    The motion window is shifted by ``lead`` frames (negative = earlier) relative to the audio window."""
    X, y, take, spk = [], [], [], []
    for i in range(len(lib.names)):
        sl = lib.clip(i)
        f, v = lib.feats[sl], lib.speed[sl]
        vm, pr = lib.voiced_mask[sl], lib.raw_pitch[sl]
        n = len(v)
        for s in range(max(0, -lead), n - win - max(0, lead) + 1, hop):
            X.append(summarize(f[s:s + win], vm[s:s + win], pr[s:s + win], lib.fps))
            y.append(v[s + lead:s + lead + win].mean())
            take.append(lib.take[i])
            spk.append(lib.speaker[i])
    X, y, take, spk = np.array(X), np.array(y), np.array(take), np.array(spk)
    for t in np.unique(take):  # target: z-score per take
        m = take == t
        y[m] = (y[m] - y[m].mean()) / (y[m].std() + 1e-9)
    return X, y, take, spk


def spearman(a: np.ndarray, b: np.ndarray) -> float:
    ra, rb = np.argsort(np.argsort(a)), np.argsort(np.argsort(b))
    return float(np.corrcoef(ra, rb)[0, 1])


def ridge_fit_predict(Xtr, ytr, Xte, lam: float) -> np.ndarray:
    mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-9
    A = (Xtr - mu) / sd
    w = np.linalg.solve(A.T @ A + lam * np.eye(A.shape[1]), A.T @ (ytr - ytr.mean()))
    return ((Xte - mu) / sd) @ w + ytr.mean()


def knn_predict(Xtr, ytr, Xte, k: int, chunk: int = 2048) -> np.ndarray:
    mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-9
    A, Q = (Xtr - mu) / sd, (Xte - mu) / sd
    a2 = (A**2).sum(1)
    out = np.empty(len(Q))
    for s in range(0, len(Q), chunk):
        q = Q[s:s + chunk]
        d = a2[None, :] - 2 * q @ A.T
        idx = np.argpartition(d, k, axis=1)[:, :k]
        out[s:s + chunk] = ytr[idx].mean(1)
    return out


def cv_eval(X, y, groups, predict, rng, n_perm: int, folds: int | None = None) -> dict:
    """Held-out correlation, grouping by ``groups`` (takes in k folds, or one fold per group)."""
    uniq = np.unique(groups)
    if folds:
        perm = rng.permutation(uniq)
        fold_of = {g: i % folds for i, g in enumerate(perm)}
        fid = np.array([fold_of[g] for g in groups])
    else:
        fid = np.searchsorted(uniq, groups)
    pred, pred_null = np.empty(len(y)), np.empty((n_perm, len(y)))
    for f in np.unique(fid):
        te, tr = fid == f, fid != f
        pred[te] = predict(X[tr], y[tr], X[te])
        for p in range(n_perm):
            pred_null[p, te] = predict(X[tr], rng.permutation(y[tr]), X[te])
    r = float(np.corrcoef(pred, y)[0, 1])
    per = {str(g): float(np.corrcoef(pred[groups == g], y[groups == g])[0, 1]) for g in uniq} if not folds else {}
    null = np.array([np.corrcoef(pn, y)[0, 1] for pn in pred_null])
    return {"r": r, "null_mean": float(null.mean()), "null_sd": float(null.std()), "per_group": per}


# ---------------------------------------------------------------------------------------- 3. units


def unit_table(lib: Lib, lead: int):
    X, y, take, spk = [], [], [], []
    for ci, a, b in lib.units:
        sl = lib.clip(ci)
        n = lib.length[ci]
        a_aud, b_aud = a - lead, b - lead  # audio that goes with this motion (lead < 0: audio later)
        if a_aud < 0 or b_aud > n:
            a_aud, b_aud = max(0, a_aud), min(n, b_aud)
        if b_aud - a_aud < 10:
            continue
        f = lib.feats[sl][a_aud:b_aud]
        X.append(summarize(f, lib.voiced_mask[sl][a_aud:b_aud], lib.raw_pitch[sl][a_aud:b_aud], lib.fps))
        y.append(lib.speed[sl][a:b].mean())
        take.append(lib.take[ci])
        spk.append(lib.speaker[ci])
    X, y, take, spk = np.array(X), np.array(y), np.array(take), np.array(spk)
    for t in np.unique(take):
        m = take == t
        y[m] = (y[m] - y[m].mean()) / (y[m].std() + 1e-9)
    return X, y, take, spk


# ---------------------------------------------------------------------------------------- 4. timing


def strokes_and_accents(lib: Lib, i: int, accent_prominence: float = 2.0) -> tuple[np.ndarray, np.ndarray]:
    """Frame indices of stroke **ends** and strong accents in clip i.

    Stroke: a hand-speed peak that stands out like a unit boundary does; its end is the first frame
    after the peak where the speed has halved (the hand arriving). Accent: a loudness peak during
    speech at least ``accent_prominence`` sd above its surroundings, >= 0.2 s apart.
    Chosen 2026-11-11 from a sweep (log.md): stroke ends and strong accents (2 sd) align best."""
    sl = lib.clip(i)
    return stroke_ends(lib.speed[sl], lib.fps), strong_accents(lib.feats[sl], lib.fps, accent_prominence)


def stroke_ends(speed: np.ndarray, fps: float) -> np.ndarray:
    """Frames where strokes end: after each hand-speed peak that stands out like a unit boundary
    does, the first frame where the (0.2 s smoothed) speed has halved."""
    from scipy.signal import find_peaks

    s = uniform_filter1d(np.asarray(speed, float), max(1, round(0.2 * fps)), mode="nearest")
    peaks, p = find_peaks(s, distance=round(0.25 * fps), prominence=0.1)
    peaks = peaks[p["prominences"] >= 0.5 * s[peaks]]
    ends = []
    for k in peaks:
        after = np.flatnonzero(s[k:] < 0.5 * s[k])
        ends.append(k + (after[0] if len(after) else 0))
    return np.array(ends, dtype=int)


def strong_accents(feats: np.ndarray, fps: float, prominence: float = 2.0) -> np.ndarray:
    """Frames of loudness peaks during speech, >= ``prominence`` sd above their surroundings
    (``FRAME_FEATURES`` input, loudness z-scored per recording), >= 0.2 s apart."""
    from scipy.signal import find_peaks

    loud = uniform_filter1d(feats[:, 0], max(1, round(0.1 * fps)), mode="nearest")
    acc, _ = find_peaks(loud, distance=round(0.2 * fps), prominence=prominence)
    return acc[feats[acc, 4] > 0]


def timing(lib: Lib, rng, max_s: float = 1.0, n_null: int = 20) -> dict:
    """Signed distance from each stroke to its nearest accent (accent - stroke, s), real vs strokes
    moved to random times in the same clip (same count; the null keeps rates, breaks alignment)."""
    win = round(max_s * lib.fps)
    edges = np.arange(-win, win + 2) - 0.5
    real, null = np.zeros(len(edges) - 1), np.zeros(len(edges) - 1)
    n_strokes = 0
    for i in range(len(lib.names)):
        st, ac = strokes_and_accents(lib, i)
        if len(st) == 0 or len(ac) == 0:
            continue
        n = lib.length[i]
        n_strokes += len(st)
        d = ac[None, :] - st[:, None]
        real += np.histogram(d[np.abs(d) <= win], edges)[0]
        for _ in range(n_null):
            fake = rng.integers(0, n, len(st))
            d = ac[None, :] - fake[:, None]
            null += np.histogram(d[np.abs(d) <= win], edges)[0] / n_null
    ratio = uniform_filter1d(real, 5) / np.maximum(uniform_filter1d(null, 5), 1e-9)
    lags = (np.arange(len(real)) - win) / lib.fps
    b = int(np.argmax(ratio))
    return {"lags": lags, "real": real, "null": null, "ratio": ratio, "n_strokes": n_strokes,
            "peak_lag_s": float(lags[b]), "peak_ratio": float(ratio[b])}


# ---------------------------------------------------------------------------------------- run


def run(cfg: AnalysisCfg) -> dict:
    rng = np.random.default_rng(cfg.seed)
    lib = Lib(cfg.library)
    cfg.out_dir.mkdir(parents=True, exist_ok=True)
    print(f"[analysis] {len(lib.names)} clips, {lib.length.sum() / lib.fps / 3600:.2f} h, "
          f"{len(lib.units)} units, speakers {sorted(str(s) for s in set(lib.speaker))}")
    report: dict = {"library": str(cfg.library)}

    # 1. frames
    max_lag = round(cfg.max_lag_s * lib.fps)
    fl = frame_level(lib, max_lag)
    print("\n1. Frames: correlation of each audio feature with hand speed (positive lag = hands after audio)")
    print(f"   {'feature':10} {'best r':>7} {'at lag':>7} {'r at 0':>7}   per speaker (lag s, r)")
    for name, d in fl.items():
        ps = ", ".join(f"{s.split('_')[1]} {l:+.2f}/{r:+.2f}" for s, (l, r) in d["per_speaker_best"].items())
        print(f"   {name:10} {d['best_r']:+7.3f} {d['best_lag_s']:+7.2f} {d['r_at_0']:+7.3f}   {ps}")
    lead_s = fl["loudness"]["best_lag_s"]
    lead = round(lead_s * lib.fps)
    print(f"   -> motion windows are shifted by {lead_s:+.2f} s (loudness' best lag)")
    report["frames"] = {k: {kk: vv for kk, vv in v.items() if kk != "curve"} for k, v in fl.items()}
    report["lead_s"] = lead_s

    # 2. windows
    report["windows"] = {}
    ridge = lambda Xtr, ytr, Xte: ridge_fit_predict(Xtr, ytr, Xte, cfg.ridge)  # noqa: E731
    knn = lambda Xtr, ytr, Xte: knn_predict(Xtr, ytr, Xte, cfg.k)  # noqa: E731
    scatter = None
    for ws in cfg.window_s:
        win, hop = round(ws * lib.fps), round(cfg.hop_s * lib.fps)
        X, y, take, spk = windows(lib, win, hop, lead)
        print(f"\n2. Windows of {ws:.0f} s (hop {cfg.hop_s} s): {len(y)} windows. Target = mean hand speed (z per take)")
        print("   single features (Spearman rank correlation, all windows):")
        rs = {n: spearman(X[:, j], y) for j, n in enumerate(WINDOW_FEATURES)}
        print("   " + ", ".join(f"{n} {r:+.2f}" for n, r in sorted(rs.items(), key=lambda kv: -abs(kv[1]))))
        res = {"n": int(len(y)), "single": rs}
        print(f"   {'model':38} {'r held-out':>10} {'shuffled-label baseline':>24}")
        for label, pred, groups, folds in (("ridge, unseen takes (5-fold by take)", ridge, take, 5),
                                           ("ridge, unseen speaker (leave one out)", ridge, spk, None),
                                           (f"kNN k={cfg.k}, unseen speaker (retrieval)", knn, spk, None)):
            nperm = cfg.permutations if "ridge" in label else max(3, cfg.permutations // 4)
            e = cv_eval(X, y, groups, pred, rng, nperm, folds)
            per = (" | " + ", ".join(f"{g.split('_')[1]} {v:+.2f}" for g, v in e["per_group"].items())) if e["per_group"] else ""
            print(f"   {label:38} {e['r']:+10.3f} {e['null_mean']:+12.3f} +- {e['null_sd']:.3f}{per}")
            res[label] = e
        report["windows"][f"{ws:.0f}s"] = res
        if scatter is None:
            p = np.empty(len(y))
            for s in np.unique(spk):
                p[spk == s] = ridge(X[spk != s], y[spk != s], X[spk == s])
            scatter = (p, y)

    # 3. units
    X, y, take, spk = unit_table(lib, lead)
    print(f"\n3. Units ({len(y)}): retrieval test, audio of each unit vs the units of other speakers")
    e = cv_eval(X, y, spk, knn, rng, max(3, cfg.permutations // 4))
    er = cv_eval(X, y, spk, ridge, rng, cfg.permutations)
    print(f"   kNN k={cfg.k}: r {e['r']:+.3f} (shuffled {e['null_mean']:+.3f} +- {e['null_sd']:.3f}) | "
          + ", ".join(f"{g.split('_')[1]} {v:+.2f}" for g, v in e["per_group"].items()))
    print(f"   ridge:  r {er['r']:+.3f} (shuffled {er['null_mean']:+.3f} +- {er['null_sd']:.3f})")
    report["units"] = {"n": int(len(y)), "knn": e, "ridge": er}

    # 4. timing
    t = timing(lib, rng)
    w = round(1.0 * lib.fps)
    print(f"\n4. Timing: {t['n_strokes']} strokes. Strong accents near a stroke's end, vs strokes at random times:")
    print("   " + ", ".join(f"{L:+.1f} s {t['ratio'][w + round(L * lib.fps)]:.2f}x" for L in (-0.6, -0.4, -0.2, 0, 0.2, 0.4, 0.6))
          + f" | peak {t['peak_ratio']:.2f}x at {t['peak_lag_s']:+.2f} s (accent - stroke end)")
    report["timing"] = {k: (v.tolist() if isinstance(v, np.ndarray) else v) for k, v in t.items()}

    out = cfg.out_dir / "analysis_v0.json"
    out.write_text(json.dumps(report, indent=1, default=float))
    _plot(cfg.out_dir / "analysis_v0.png", fl, lib.fps, max_lag, scatter)
    print(f"\n[analysis] {out}, {cfg.out_dir / 'analysis_v0.png'}")
    return report


def _plot(path: Path, fl: dict, fps: float, max_lag: int, scatter) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 2, figsize=(12, 4))
    lags = (np.arange(2 * max_lag + 1) - max_lag) / fps
    for name, d in fl.items():
        ax[0].plot(lags, d["curve"], label=name)
    ax[0].axvline(0, color="gray", lw=0.8)
    ax[0].set(title="audio feature vs hand speed, all clips", xlabel="lag (s): positive = hands after audio",
              ylabel="correlation")
    ax[0].legend(fontsize=8)
    p, y = scatter
    ax[1].hexbin(p, y, gridsize=40, bins="log", cmap="Greys")
    ax[1].set(title=f"1 s windows, unseen speaker: predicted vs actual (r {np.corrcoef(p, y)[0, 1]:.2f})",
              xlabel="predicted hand activity (ridge)", ylabel="actual hand activity (z per take)")
    fig.tight_layout()
    fig.savefig(path, dpi=110)
