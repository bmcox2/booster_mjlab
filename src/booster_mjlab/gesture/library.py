"""Build the gesture library once: every usable clip's speech features, hand features and units.

Inputs (from the full BEAT2 build):
- a combined K1 motion file (``train-a``: Tier A clips of training speakers, 50 fps);
- ``segments.json``: each clip's take and time span in that take;
- BEAT2 ``wave16k/<take>.wav`` (audio) and ``smplxflame_30/<take>.npz`` (for the jaw check).

Per take: the jaw check (``sync.jaw_sync``) and speech features of the whole take at 50 fps, cached in
``<out_dir>/features/``. Per clip of a passing take: its slice of those features, hand features from
its K1 body positions, and its units (``motion.cut_units``). Everything goes into one ``.npz``:

- ``clip_*``: name, take, speaker, start (s in the take), offset/length (rows in the frame arrays),
  source (the grounded GMR ``.pkl`` it was converted from, 30 fps: what the generator stitches)
- ``audio`` (N, 5) ``audio.FEATURES``; ``motion`` (N, 9) ``motion.MOTION_FEATURES``; ``joint_pos`` (N, 22);
  ``twist`` (N,) trunk heading relative to the feet (``motion.twist``); ``trunk_over_feet`` (N, 2)
- ``unit_clip``, ``unit_start``, ``unit_end``: units as frame ranges inside their clip
- ``jaw_*``: the jaw check of every take considered (passed or not)
"""

from __future__ import annotations

import json
import time
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass, field
from pathlib import Path

import mujoco
import numpy as np

import booster_mjlab
from booster_mjlab.gesture import audio as A
from booster_mjlab.gesture import motion as M
from booster_mjlab.gesture.sync import jaw_sync

DATA = Path.home() / "robotics/data"
BEAT2 = DATA / "BEAT2/beat_english_v2.0.0"
K1_XML = Path(booster_mjlab.__file__).parent / "robots/booster_k1/xmls/k1.xml"
FEATURE_VERSION = "v1"  # bump when audio.speech_features changes, to invalidate the per-take cache


@dataclass
class LibraryCfg:
    motion_file: Path = DATA / "beat2_full_torso/combined/beat2-full-torso-train-a.npz"
    segments: Path = DATA / "beat2_full_torso/segments.json"
    speakers: tuple[str, ...] = ("1_wayne", "4_lawrence", "9_miranda")
    out: Path = DATA / "gesture/library_v0.npz"
    fps: float = 50.0
    min_unit_s: float = 0.5
    max_unit_s: float = 3.0
    workers: int = 12
    exclude_takes: tuple[str, ...] = field(default_factory=tuple)


def body_names() -> list[str]:
    """Body order of the motion files: the K1 model's bodies without the world."""
    m = mujoco.MjModel.from_xml_path(str(K1_XML))
    return [m.body(b).name for b in range(1, m.nbody)]


def _take_job(args: tuple[str, Path, float, Path]) -> tuple[str, dict, str]:
    """Jaw check + speech features of one take (runs in a worker process)."""
    take, cache_dir, fps, beat2 = args
    wav, smplx = beat2 / "wave16k" / f"{take}.wav", beat2 / "smplxflame_30" / f"{take}.npz"
    if not wav.exists() or not smplx.exists():
        return take, {}, f"missing {'audio' if not wav.exists() else 'smplx'}"
    js = jaw_sync(smplx, wav)
    cache = cache_dir / f"{take}.npz"
    if not cache.exists():
        x, rate = A.load_audio(wav)
        feats = A.speech_features(x, rate, fps).astype(np.float32)
        np.savez(cache, audio=feats, fps=fps, version=FEATURE_VERSION, seconds=len(x) / rate)
    return take, asdict(js), ""


def build(cfg: LibraryCfg) -> Path:
    t0 = time.time()
    segs = json.loads(cfg.segments.read_text())["takes"]
    clip_info = {c["name"]: c for t in segs if t["speaker"] in cfg.speakers for c in t["clips"]}
    print(f"[library] reading {cfg.motion_file.name}")
    z = np.load(cfg.motion_file)
    names = [str(n) for n in z["clip_names"]]
    sources = [str(s) for s in z["clip_sources"]]
    starts = np.concatenate([[0], np.cumsum(z["clip_lengths"])]).astype(int)
    if abs(float(z["fps"][0]) - cfg.fps) > 1e-6:
        raise SystemExit(f"motion file is {float(z['fps'][0])} fps, library expects {cfg.fps}")
    picked = [i for i, n in enumerate(names) if n in clip_info and clip_info[n]["take"] not in cfg.exclude_takes]
    takes = sorted({clip_info[names[i]]["take"] for i in picked})
    print(f"[library] {len(picked)} clips of {list(cfg.speakers)} in {len(takes)} takes")

    cache_dir = cfg.out.parent / "features" / FEATURE_VERSION
    cache_dir.mkdir(parents=True, exist_ok=True)
    jaw, problems = {}, {}
    with ProcessPoolExecutor(cfg.workers) as pool:
        for take, js, err in pool.map(_take_job, [(t, cache_dir, cfg.fps, BEAT2) for t in takes]):
            if err:
                problems[take] = err
            else:
                jaw[take] = js
    print(f"[library] takes: {sum(j['passed'] for j in jaw.values())} pass the jaw check, "
          f"{sum(not j['passed'] for j in jaw.values())} fail, {len(problems)} missing files ({time.time() - t0:.0f} s)")

    bnames = body_names()
    jp, bp, bq = z["joint_pos"], z["body_pos_w"], z["body_quat_w"]
    clip_rows, audio_parts, motion_parts, joint_parts, twist_parts, over_parts, units = [], [], [], [], [], [], []
    offset, short_audio = 0, 0
    feats_cache: dict[str, np.ndarray] = {}
    for i in picked:
        c = clip_info[names[i]]
        if c["take"] not in jaw or not jaw[c["take"]]["passed"]:
            continue
        if c["take"] not in feats_cache:
            feats_cache.clear()  # picked is in file order, mostly grouped by take
            feats_cache[c["take"]] = np.load(cache_dir / f"{c['take']}.npz")["audio"]
        take_audio = feats_cache[c["take"]]
        a, b = starts[i], starts[i + 1]
        k0 = int(round(c["start"] * cfg.fps))
        n = min(b - a, len(take_audio) - k0)
        if n < b - a:
            short_audio += 1
        if n < round(cfg.min_unit_s * cfg.fps):
            continue
        mot = M.hand_features(bp[a:a + n], bq[a:a + n], bnames, cfg.fps)
        bounds = M.cut_units(mot[:, M.MOTION_FEATURES.index("speed")], cfg.fps, cfg.min_unit_s, cfg.max_unit_s)
        ci = len(clip_rows)
        units += [(ci, u0, u1) for u0, u1 in zip(bounds[:-1], bounds[1:])]
        clip_rows.append((names[i], c["take"], c["speaker"], c["start"], offset, n, sources[i]))
        audio_parts.append(take_audio[k0:k0 + n])
        motion_parts.append(mot.astype(np.float32))
        joint_parts.append(jp[a:a + n])
        twist_parts.append(M.twist(bp[a:a + n], bq[a:a + n], bnames).astype(np.float32))
        over_parts.append(M.trunk_over_feet(bp[a:a + n], bq[a:a + n], bnames).astype(np.float32))
        offset += n

    cn, ct, cs, cst, co, cl, csrc = zip(*clip_rows)
    uc, us, ue = (np.array(x) for x in zip(*units))
    jt = sorted(jaw)
    cfg.out.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        cfg.out,
        fps=cfg.fps, audio_features=np.array(A.FEATURES), motion_features=np.array(M.MOTION_FEATURES),
        clip_name=np.array(cn), clip_take=np.array(ct), clip_speaker=np.array(cs), clip_start_s=np.array(cst),
        clip_offset=np.array(co), clip_length=np.array(cl), clip_source=np.array(csrc),
        audio=np.concatenate(audio_parts), motion=np.concatenate(motion_parts), joint_pos=np.concatenate(joint_parts),
        twist=np.concatenate(twist_parts), trunk_over_feet=np.concatenate(over_parts),
        unit_clip=uc, unit_start=us, unit_end=ue,
        jaw_take=np.array(jt), jaw_lag_s=np.array([jaw[t]["lag_s"] for t in jt]),
        jaw_corr=np.array([jaw[t]["corr"] for t in jt]), jaw_passed=np.array([jaw[t]["passed"] for t in jt]),
        cfg=json.dumps({k: str(v) for k, v in asdict(cfg).items()}), feature_version=FEATURE_VERSION,
    )
    report(cfg.out)
    if short_audio:
        print(f"[library] {short_audio} clips ran past their take's audio and were trimmed")
    if problems:
        print(f"[library] missing files: {dict(Counter(problems.values()))}, e.g. {list(problems)[:3]}")
    print(f"[library] wrote {cfg.out} ({time.time() - t0:.0f} s)")
    return cfg.out


def report(path: Path) -> None:
    """Library statistics: per speaker clips / hours / units, unit lengths, failed jaw checks."""
    L = np.load(path)
    fps = float(L["fps"])
    spk = L["clip_speaker"]
    ulen = (L["unit_end"] - L["unit_start"]) / fps
    uspk = spk[L["unit_clip"]]
    print(f"\n{'speaker':12} {'clips':>6} {'hours':>6} {'units':>6} {'unit s (median)':>16} {'takes failing jaw':>18}")
    jaw_spk = np.array(["_".join(t.split("_")[:2]) for t in L["jaw_take"]])
    for s in sorted(set(spk)):
        m = spk == s
        print(f"{s:12} {m.sum():6} {L['clip_length'][m].sum() / fps / 3600:6.2f} {(uspk == s).sum():6} "
              f"{np.median(ulen[uspk == s]):16.2f} {(~L['jaw_passed'][jaw_spk == s]).sum():8}/{(jaw_spk == s).sum()}")
    print(f"{'all':12} {len(spk):6} {L['clip_length'].sum() / fps / 3600:6.2f} {len(ulen):6} {np.median(ulen):16.2f}")
    h = np.histogram(ulen, bins=[0.5, 0.75, 1.0, 1.5, 2.0, 2.5, 3.01])[0]
    print("unit lengths (s): " + ", ".join(f"{a}-{b}: {n}" for a, b, n in
                                          zip([0.5, 0.75, 1.0, 1.5, 2.0, 2.5], [0.75, 1.0, 1.5, 2.0, 2.5, 3.0], h)))
    fails = [(t, float(l)) for t, l, p in zip(L["jaw_take"], L["jaw_lag_s"], L["jaw_passed"]) if not p]
    if fails:
        by = defaultdict(list)
        for t, l in fails:
            by["_".join(t.split("_")[:2])].append(f"{t.split('_', 2)[2]} {l:+.2f}")
        for s, v in by.items():
            print(f"jaw check failed, {s}: {', '.join(v)}")
