"""BEAT2 takes -> still segments, cut into 4-20 s clips, in two tiers (human side only, no GMR).

Replaces beat2_batch's old top-k window picking. Every second of a take where the speaker stands in
place becomes training data, quiet moments included (no arm-activity floor):

- Tier A: every maximal stretch where both ankles stay within `tier_a_cm` of their median spot
  (10 cm, the old window filter). Stretches start and end on planted frames (both ankles slower than
  `move_speed`), so a clip never begins or ends halfway through a step.
- Tier B: the foot shifts between Tier A stretches (ankles within `tier_b_cm`, 25 cm), each as a
  window with `shift_pad_s` of standing on either side. Tier B is built on top of Tier A, which
  doesn't change: B clips overlap A clips by their padding, so A alone or A + B are both valid sets.
- Each stretch / shift window longer than `max_s` is cut into equal pieces (a 45 s stretch -> 3 x 15 s);
  anything shorter than `min_s` is dropped (counted as rejected for foot movement).

Takes and their official split type (train / val / test / additional) come from BEAT2's
train_test_split.csv. Speakers, tiers and limits come from a dataset spec (tools/datasets/*.toml).

Usage (from ~/projects/booster-mjlab):
    uv run python tools/beat2_segments.py --spec tools/datasets/beat2_full.toml   # report -> notes/
"""
from __future__ import annotations

import argparse
import csv
import json
import multiprocessing
import os
import sys
import tomllib
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

import numpy as np
from scipy.ndimage import uniform_filter1d

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import beat2_to_gmr as b2g  # noqa: E402

SPLIT_TYPES = ("train", "val", "test", "additional")


@dataclass(frozen=True)
class SegmentCfg:
    tier_a_cm: float = 10.0
    tier_b_cm: float = 25.0
    min_s: float = 4.0
    max_s: float = 20.0
    shift_pad_s: float = 2.0     # standing kept on each side of a Tier B foot shift
    move_speed: float = 0.10     # m/s; an ankle faster than this (0.17 s average) is moving, not planted
    check_s: float = 0.1         # how often a growing stretch re-checks the radius


# ---------------------------------------------------------------------------------------- spec

def load_spec(path: Path) -> dict:
    with open(path, "rb") as f:
        spec = tomllib.load(f)
    for k in ("beat2_dir", "out_dir", "ik_config", "qc_report", "segments_report"):
        if spec.get(k):
            p = Path(os.path.expanduser(spec[k]))
            spec[k] = p if p.is_absolute() else (REPO / p)
    spec["segment_cfg"] = SegmentCfg(**spec.get("segments", {}))
    return spec


def load_split(beat2_dir: Path) -> dict[str, str]:
    """Take id (e.g. 2_scott_0_17_17) -> official type (train / val / test / additional)."""
    with open(beat2_dir / "train_test_split.csv") as f:
        rows = list(csv.reader(f))[1:]
    return {take: typ for take, typ in rows}


def speaker_of(take: str) -> str:
    return "_".join(take.split("_")[:2])  # 2_scott_0_17_17 -> 2_scott


def speaker_groups(spec: dict, split: dict[str, str]) -> dict[str, str]:
    """Speaker -> 'train' or 'heldout' (speakers in spec.speakers.skip are left out)."""
    sp = spec["speakers"]
    every = sorted({speaker_of(t) for t in split}, key=lambda s: int(s.split("_")[0]))
    held, skip = list(sp["heldout"]), set(sp.get("skip", []))
    train = [s for s in every if s not in held and s not in skip] if sp.get("train", "rest") == "rest" else list(sp["train"])
    unknown = sorted(set(held + train) - set(every))
    if unknown:
        sys.exit(f"Speakers not in train_test_split.csv: {unknown}")
    if set(held) & set(train):
        sys.exit(f"Speakers in both groups: {sorted(set(held) & set(train))}")
    return {**{s: "train" for s in train}, **{s: "heldout" for s in held}}


def selected_takes(spec: dict, split: dict[str, str]) -> list[tuple[str, str, str]]:
    """(take, speaker group, split type) for every take some set in the spec uses."""
    groups = speaker_groups(spec, split)
    wanted = {(s["speakers"], t) for s in spec["sets"].values() for t in s["takes"]}
    limit = spec["speakers"].get("max_takes")  # per speaker and type, for quick end-to-end tests
    out, count = [], defaultdict(int)
    for take, typ in sorted(split.items(), key=lambda kv: (kv[0].split("_")[:3], [int(x) for x in kv[0].split("_")[3:]])):
        g = groups.get(speaker_of(take))
        if g and (g, typ) in wanted and (limit is None or count[(speaker_of(take), typ)] < limit):
            count[(speaker_of(take), typ)] += 1
            out.append((take, g, typ))
    return out


# ---------------------------------------------------------------------------------------- segments

def take_signals(path: Path, model_dir: Path) -> dict:
    """Per-frame human signals the segmentation and clip stats use."""
    t = b2g.read_take(path, model_dir, None, verbose=False)
    pos, pelvis_rot = b2g.body_joint_positions(t, model_dir)
    fps = t["fps"]
    ankles = pos[:, [b2g.L_ANKLE, b2g.R_ANKLE], :2]
    speed = np.linalg.norm(np.diff(ankles, axis=0), axis=-1) * fps                  # (T-1, 2) m/s
    speed = uniform_filter1d(np.r_[speed[:1], speed], int(round(0.17 * fps)) | 1, axis=0).max(axis=1)
    wrists = np.stack([pelvis_rot.inv().apply(pos[:, j] - pos[:, 0]) for j in (b2g.L_WRIST, b2g.R_WRIST)], axis=1)
    wrist_speed = np.clip(np.linalg.norm(np.diff(wrists, axis=0), axis=-1) * fps, 0, b2g.MAX_WRIST_SPEED)
    return dict(fps=fps, n=len(pos), ankles=ankles, ankle_speed=speed, wrist_speed=wrist_speed, pelvis_z=pos[:, 0, 2])


def foot_move(ankles: np.ndarray) -> float:
    """Farthest either ankle strays from its median spot, m (the old window filter's measure)."""
    return float(np.linalg.norm(ankles - np.median(ankles, axis=0), axis=-1).max())


def still_stretches(ankles: np.ndarray, planted: np.ndarray, radius: float, fps: float, cfg: SegmentCfg) -> list[tuple[int, int]]:
    """Maximal [start, end) frame ranges where both ankles stay within `radius` of their median spot.

    Greedy, left to right: a stretch starts on a planted frame and grows (re-checked every check_s)
    until an ankle strays too far; its end is then pulled back to the last planted frame, so the
    step that broke it is left out. The next stretch starts at the next planted frame.
    """
    n, stride = len(ankles), max(1, int(round(cfg.check_s * fps)))
    out, s = [], 0
    while s < n:
        if not planted[s]:
            s += 1
            continue
        good, e = s + 1, min(n, s + stride)
        while True:
            if foot_move(ankles[s:e]) > radius:
                break
            good = e
            if e == n:
                break
            e = min(n, e + stride)
        end = good
        while end > s + 1 and not planted[end - 1]:
            end -= 1
        out.append((s, end))
        s = max(good, s + 1)
    return out


def cut(start: int, end: int, fps: float, cfg: SegmentCfg) -> list[tuple[int, int]]:
    """[start, end) into equal pieces no longer than max_s; nothing if shorter than min_s."""
    n = end - start
    if n < cfg.min_s * fps:
        return []
    k = int(np.ceil(n / (cfg.max_s * fps)))
    edges = np.round(np.linspace(start, end, k + 1)).astype(int)
    return list(zip(edges[:-1], edges[1:]))


def shift_windows(b_stretches, covered: np.ndarray, fps: float, cfg: SegmentCfg) -> list[tuple[int, int]]:
    """Tier B: the time inside 25 cm stretches that Tier A clips don't cover, padded with standing."""
    pad, need = int(round(cfg.shift_pad_s * fps)), int(round(cfg.min_s * fps))
    out = []
    for s, e in b_stretches:
        gap = ~covered[s:e]
        edges = np.flatnonzero(np.diff(np.r_[0, gap.astype(int), 0]))
        windows = []
        for gs, ge in zip(edges[::2] + s, edges[1::2] + s):
            a, b = max(s, gs - pad), min(e, ge + pad)
            if b - a < need:  # widen evenly within the stretch to reach min_s
                extra = need - (b - a)
                a = max(s, a - (extra + 1) // 2)
                b = min(e, a + need)
                a = max(s, b - need)
            if windows and a <= windows[-1][1]:
                windows[-1] = (windows[-1][0], max(windows[-1][1], b))
            else:
                windows.append((a, b))
        for a, b in windows:
            out += cut(a, b, fps, cfg)
    return out


def clip_name(take: str, start: float, end: float, tier: str) -> str:
    base = f"{take.split('_', 1)[1]}_t{start:.0f}-{end:.0f}"  # 2_scott_0_1_1 -> scott_0_1_1_t34-44
    return base if tier == "A" else f"{base}_shift"


def segment_take(job: tuple[Path, str, str, Path, SegmentCfg]) -> dict:
    path, group, typ, model_dir, cfg = job
    take = path.stem
    try:
        sig = take_signals(path, model_dir)
    except Exception as e:  # e.g. a take that is still downloading
        return dict(take=take, error=f"{type(e).__name__}: {e}")
    fps, n, ankles = sig["fps"], sig["n"], sig["ankles"]
    planted = sig["ankle_speed"] < cfg.move_speed
    a_clips = [c for s, e in still_stretches(ankles, planted, cfg.tier_a_cm / 100, fps, cfg) for c in cut(s, e, fps, cfg)]
    covered = np.zeros(n, bool)
    for s, e in a_clips:
        covered[s:e] = True
    b_stretches = [(s, e) for s, e in still_stretches(ankles, planted, cfg.tier_b_cm / 100, fps, cfg)
                   if e - s >= cfg.min_s * fps]
    b_clips = shift_windows(b_stretches, covered, fps, cfg)
    covered_b = covered.copy()
    for s, e in b_clips:
        covered_b[s:e] = True

    clips = []
    for tier, ranges in (("A", a_clips), ("B", b_clips)):
        for s, e in ranges:
            clips.append(dict(
                take=take, speaker=speaker_of(take), group=group, type=typ, tier=tier,
                name=clip_name(take, s / fps, e / fps, tier),
                start=s / fps, end=e / fps, start_frame=int(s), end_frame=int(e),
                feet_human_cm=foot_move(ankles[s:e]) * 100,
                arms_human_cm_s=float(sig["wrist_speed"][s:max(s + 1, e - 1)].mean() * 100),
                pelvis_drop_human_cm=float(np.ptp(sig["pelvis_z"][s:e]) * 100),
            ))
    return dict(take=take, speaker=speaker_of(take), group=group, type=typ, fps=fps, frames=n,
                a_frames=int(covered.sum()), ab_frames=int(covered_b.sum()), clips=clips)


def pool_map(fn, items: list, workers: int) -> list:
    if workers <= 1 or len(items) <= 1:
        return [fn(x) for x in items]
    ctx = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(min(workers, len(items)), mp_context=ctx) as pool:
        return list(pool.map(fn, items, chunksize=4))


def segment_all(spec: dict, workers: int) -> tuple[list[dict], list[str]]:
    """Segment every take the spec uses. Returns per-take results and the takes not on disk."""
    beat2_dir, cfg = spec["beat2_dir"], spec["segment_cfg"]
    model_dir = Path(os.path.expanduser(spec.get("model_dir", str(b2g.DEFAULT_MODEL_DIR))))
    split = load_split(beat2_dir)
    jobs, missing = [], []
    for take, group, typ in selected_takes(spec, split):
        p = beat2_dir / "smplxflame_30" / f"{take}.npz"
        if p.exists():
            jobs.append((p, group, typ, model_dir, cfg))
        else:
            missing.append(take)
    return pool_map(segment_take, jobs, workers), missing


# ---------------------------------------------------------------------------------------- report

def summarize(takes: list[dict]) -> dict:
    """(speaker, type) -> takes, minutes, clips and minutes per tier, rejected share."""
    tab = defaultdict(lambda: defaultdict(float))
    for t in takes:
        if "error" in t:
            continue
        r = tab[(t["speaker"], t["type"])]
        r["group"] = t["group"]
        r["takes"] += 1
        r["min"] += t["frames"] / t["fps"] / 60
        r["a_min_unique"] += t["a_frames"] / t["fps"] / 60
        r["ab_min_unique"] += t["ab_frames"] / t["fps"] / 60
        for c in t["clips"]:
            r[f"{c['tier']}_clips"] += 1
            r[f"{c['tier']}_min"] += (c["end"] - c["start"]) / 60
    return tab


def write_report(spec: dict, takes: list[dict], missing: list[str], path: Path) -> None:
    cfg, tab = spec["segment_cfg"], summarize(takes)
    clips = [c for t in takes if "error" not in t for c in t["clips"]]
    errors = [t for t in takes if "error" in t]

    def line(key, r):
        rej_a = 1 - r["a_min_unique"] / r["min"] if r["min"] else 0
        rej_ab = 1 - r["ab_min_unique"] / r["min"] if r["min"] else 0
        return (f"| {key} | {int(r['takes'])} | {r['min']:.1f} | {int(r['A_clips'])} | {r['A_min']:.1f} | {rej_a:.0%} | "
                f"{int(r['B_clips'])} | {r['B_min']:.1f} | {rej_ab:.0%} |")

    def total(rows):
        t = defaultdict(float)
        for r in rows:
            for k, v in r.items():
                if k != "group":
                    t[k] += v
        return t

    hdr = ("| {} | takes | minutes | A clips | A min | rejected (A) | B clips | B min | rejected (A+B) |\n"
           "|---|---|---|---|---|---|---|---|---|")
    lines = [
        "# BEAT2 Segments (human side)",
        "",
        f"Generated {date.today()} by `tools/beat2_segments.py` from `{spec['_spec_path']}`. Human motion only (before GMR).",
        "",
        f"- **Tier A:** maximal stretches with both ankles within {cfg.tier_a_cm:g} cm of their median spot, "
        f"starting and ending on planted frames (ankles < {cfg.move_speed:g} m/s), cut into {cfg.min_s:g}–{cfg.max_s:g} s clips.",
        f"- **Tier B:** foot shifts inside {cfg.tier_b_cm:g} cm stretches that Tier A leaves out, each with "
        f"{cfg.shift_pad_s:g} s of standing on either side (so B overlaps A by its padding), same clip lengths. Names end in `_shift`.",
        "- **Rejected:** share of the take's time in no clip (A only, or A + B), i.e. lost to stepping or walking.",
        "- **A min / B min** add clip lengths; B's include the padding that A also covers.",
    ]
    if missing:
        lines.append(f"- **Not on disk ({len(missing)} takes):** " + ", ".join(missing[:20]) + (" …" if len(missing) > 20 else ""))
    if errors:
        lines.append(f"- **Unreadable ({len(errors)}):** " + "; ".join(f"{t['take']} ({t['error']})" for t in errors[:10]))

    for group in ("train", "heldout"):
        types = [t for t in SPLIT_TYPES if any(k[1] == t and r["group"] == group for k, r in tab.items())]
        lines += ["", f"## {'Training' if group == 'train' else 'Held-out'} speakers"]
        for typ in types:
            rows = {k: r for k, r in tab.items() if r["group"] == group and k[1] == typ}
            spk_sorted = sorted(rows, key=lambda k: int(k[0].split("_")[0]))
            lines += ["", f"### `{typ}` takes", "", hdr.format("speaker")]
            lines += [line(k[0], rows[k]) for k in spk_sorted]
            lines.append(line("**total**", total(rows.values())))

    lines += ["", "## Totals", "", hdr.format("group / type")]
    for group in ("train", "heldout"):
        for typ in SPLIT_TYPES:
            rows = [r for k, r in tab.items() if r["group"] == group and k[1] == typ]
            if rows:
                lines.append(line(f"{group} / {typ}", total(rows)))

    # training-set balance: each speaker's share of Tier A minutes over every split type a training set uses
    train_types = sorted({t for s in spec["sets"].values() if s["speakers"] == "train"
                          and set(s["takes"]) <= {"train", "additional"} for t in s["takes"]})
    per_spk = defaultdict(lambda: defaultdict(float))
    for (spk, typ), r in tab.items():
        if r["group"] == "train" and typ in train_types:
            per_spk[spk][typ] += r["A_min"]
            per_spk[spk]["A"] += r["A_min"]
            per_spk[spk]["B"] += r["B_min"]
    a_total = sum(v["A"] for v in per_spk.values()) or 1
    b_total = sum(v["B"] for v in per_spk.values())
    lines += ["", f"## Training balance (Tier A, {' + '.join(f'`{t}`' for t in train_types)} takes)", "",
              "| speaker | " + " | ".join(f"A min ({t})" for t in train_types) + " | A min | share | B min |",
              "|---|" + "---|" * (len(train_types) + 3)]
    for spk, v in sorted(per_spk.items(), key=lambda kv: -kv[1]["A"]):
        share = v["A"] / a_total
        lines.append(f"| {spk} | " + " | ".join(f"{v[t]:.1f}" for t in train_types)
                     + f" | {v['A']:.1f} | {share:.1%}{' **> 15%**' if share > 0.15 else ''} | {v['B']:.1f} |")
    lines.append(f"| **total** | " + " | ".join(f"{sum(v[t] for v in per_spk.values()):.1f}" for t in train_types)
                 + f" | {a_total:.1f} ({a_total / 60:.2f} h) | | {b_total:.1f} ({b_total / 60:.2f} h) |")

    # clip-length and foot-movement distributions, per tier
    lines += ["", "## Clips", "", "| tier | clips | length s (min / median / max) | feet cm (median / p95 / max) | "
              "arms cm/s (median / p10) | clips over the tier radius |", "|---|---|---|---|---|---|"]
    for tier, radius in (("A", cfg.tier_a_cm), ("B", cfg.tier_b_cm)):
        cs = [c for c in clips if c["tier"] == tier]
        if not cs:
            continue
        ln = np.array([c["end"] - c["start"] for c in cs])
        ft = np.array([c["feet_human_cm"] for c in cs])
        ar = np.array([c["arms_human_cm_s"] for c in cs])
        lines.append(f"| {tier} | {len(cs)} | {ln.min():.1f} / {np.median(ln):.1f} / {ln.max():.1f} | "
                     f"{np.median(ft):.1f} / {np.percentile(ft, 95):.1f} / {ft.max():.1f} | "
                     f"{np.median(ar):.0f} / {np.percentile(ar, 10):.0f} | {(ft > radius).sum()} |")
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spec", type=Path, required=True, help="dataset spec, e.g. tools/datasets/beat2_full.toml")
    ap.add_argument("--report", type=Path, default=None, help="markdown report (default: spec's segments_report)")
    ap.add_argument("--workers", type=int, default=min(12, os.cpu_count() or 1))
    args = ap.parse_args()
    spec = load_spec(args.spec)
    spec["_spec_path"] = args.spec
    takes, missing = segment_all(spec, args.workers)
    report = args.report or spec.get("segments_report") or REPO / "notes/beat2-segments.md"
    write_report(spec, takes, missing, report)
    out = spec["out_dir"] / "segments.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"cfg": asdict(spec["segment_cfg"]), "missing": missing, "takes": takes}, indent=1))
    n = sum(len(t.get("clips", [])) for t in takes)
    print(f"[segments] {len(takes)} takes -> {n} clips; report {report}; clips {out}")


if __name__ == "__main__":
    main()
