"""Dataset spec -> BEAT2 segments -> grounded K1 clips -> Gate 1 QC -> combined artifacts, in one command.

The spec (tools/datasets/*.toml) says which speakers are held out, which official split types
(train / val / test / additional) and tiers go into which set, the segment limits, the GMR IK config,
and the QC limits. Stages, in order:

1. segment: every still stretch of every take a set uses, cut into 4-20 s Tier A / Tier B clips
   (tools/beat2_segments.py; human motion only, so it can run before the GMR config is final)
2. convert: each clip to GMR's input (beat2_to_gmr: Y-up -> Z-up, 16 betas, trimmed audio if on disk)
3. retarget with GMR, headless (tools/gmr_retarget.py, run with GMR's venv; --workers processes)
4. ground_clip (flatten stance feet, plant them, put the lowest point on the floor)
5. qc: Gate 1 checks on booster-mjlab's K1 model (tools/clip_qc.py) -> <qc_report>, flags severe clips
6. combine: one file per set; training sets are checked for leakage (held-out speakers, other split
   types, takes shared with an eval set) on the written file before anything is uploaded

Every stage skips clips that are already done. The out-dir remembers the segment limits and IK config
it was built with and refuses to mix in clips built differently (use a new out_dir, or --force).
Each worker needs up to ~1.5 GB of RAM.

Usage (from ~/projects/booster-mjlab):
    uv run python tools/beat2_batch.py --spec tools/datasets/beat2_full.toml --stages segment   # human side only
    uv run python tools/beat2_batch.py --spec tools/datasets/beat2_full.toml                    # all, then upload
    ... --no-upload        # write <out_dir>/combined/<name>-<set>.npz only
    ... --sets train val   # combine only these sets
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import multiprocessing
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict
from datetime import date
from pathlib import Path

import numpy as np

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import beat2_segments as bs  # noqa: E402
import beat2_to_gmr as b2g  # noqa: E402
import clip_qc  # noqa: E402
from ground_clip import DEFAULT_GMR_XML, DEFAULT_ROBOT_XML, Grounder  # noqa: E402

GMR_PYTHON = Path.home() / "projects/GMR/.venv/bin/python"
STAGES = ("segment", "convert", "retarget", "ground", "qc", "combine")
TRAINING_TYPES = {"train", "additional"}  # split types a training set may use


def newer(dst: Path, src: Path) -> bool:
    return dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime


def check_stamp(spec: dict, force: bool) -> None:
    """Refuse to reuse an out-dir built with other segment limits or another IK config."""
    ik = spec.get("ik_config")
    stamp = {"segments": asdict(spec["segment_cfg"]),
             "ik_config": str(ik) if ik else "",
             "ik_config_sha1": hashlib.sha1(Path(ik).read_bytes()).hexdigest() if ik else ""}
    path = spec["out_dir"] / "build.json"
    if path.exists() and not force:
        old = json.loads(path.read_text())
        if old != stamp:
            diff = [k for k in stamp if old.get(k) != stamp[k]]
            sys.exit(f"{spec['out_dir']} was built with different {', '.join(diff)}; its cached clips would be "
                     "mixed in. Use a new out_dir in the spec, or --force to rebuild everything.")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(stamp, indent=1))


# ---------------------------------------------------------------------------------------- stages 1-4

def clips_from_segments(spec: dict, takes: list[dict]) -> list[dict]:
    """Every segment some set uses, with its file paths and the sets it belongs to."""
    out_dir, clips = spec["out_dir"], []
    for t in takes:
        for c in t.get("clips", []):
            sets = [name for name, s in spec["sets"].items()
                    if c["group"] == s["speakers"] and c["type"] in s["takes"] and c["tier"] in s["tiers"]]
            if not sets:
                continue
            clips.append({**c, "sets": sets,
                          "smplx": out_dir / "smplx" / f"{c['name']}.npz",
                          "k1": out_dir / "k1" / f"{c['name']}.pkl",
                          "grounded": out_dir / "k1" / f"{c['name']}_grounded.pkl"})
    names = [c["name"] for c in clips]
    dupes = sorted({n for n in names if names.count(n) > 1})
    if dupes:
        sys.exit(f"Duplicate clip names (two segments round to the same seconds?): {dupes[:5]}")
    return clips


def convert_one(job: tuple[dict, Path, Path]) -> None:
    c, beat2_dir, model_dir = job
    wav = beat2_dir / "wave16k" / f"{c['take']}.wav"
    ns = argparse.Namespace(start=c["start"], end=c["end"], up=None, wav=wav if wav.exists() else None,
                            model_dir=model_dir)
    with contextlib.redirect_stdout(io.StringIO()):  # converter is chatty; errors still raise
        b2g.convert(beat2_dir / "smplxflame_30" / f"{c['take']}.npz", c["smplx"], ns)


def convert(clips: list[dict], spec: dict, args) -> None:
    src = lambda c: spec["beat2_dir"] / "smplxflame_30" / f"{c['take']}.npz"  # noqa: E731
    todo = [c for c in clips if args.force or not newer(c["smplx"], src(c))]
    bs.pool_map(convert_one, [(c, spec["beat2_dir"], spec["model_dir"]) for c in todo], args.workers)
    print(f"[convert] {len(todo)} converted, {len(clips) - len(todo)} cached")


def retarget(clips: list[dict], spec: dict, args) -> None:
    todo = [c for c in clips if args.force or not newer(c["k1"], c["smplx"])]
    if not todo:
        return
    if not GMR_PYTHON.exists():
        sys.exit(f"GMR's venv python not found: {GMR_PYTHON}")
    n = max(1, min(args.workers, len(todo)))
    print(f"[gmr] retargeting {len(todo)} clip(s) headless with {GMR_PYTHON}, {n} process(es)")
    base = [str(GMR_PYTHON), str(TOOLS / "gmr_retarget.py")]
    if spec.get("ik_config"):
        base += ["--ik-config", str(spec["ik_config"])]
    env = {k: v for k, v in os.environ.items() if k not in ("DISPLAY", "WAYLAND_DISPLAY")}  # prove it's headless
    # Each clip gets its own GMR solver (gmr_retarget.py builds one per clip), so splitting the list
    # across processes gives the same clips as one process.
    procs = [subprocess.Popen(base + [str(p) for c in todo[i::n] for p in (c["smplx"], c["k1"])], env=env)
             for i in range(n)]
    failed = [p.args for p in procs if p.wait() != 0]
    if failed:
        sys.exit(f"[gmr] {len(failed)} of {n} retarget process(es) failed")


_GROUNDER: Grounder | None = None  # one per worker process


def _init_grounder() -> None:
    global _GROUNDER
    _GROUNDER = Grounder(DEFAULT_GMR_XML, DEFAULT_ROBOT_XML)


def ground_one(c: dict) -> str:
    out = io.StringIO()
    tmp = c["grounded"].with_name(c["grounded"].stem + ".tmp.pkl")  # rename when complete (safe to interrupt)
    with contextlib.redirect_stdout(out):
        _GROUNDER.ground(c["k1"], tmp)
    os.replace(tmp, c["grounded"])
    c["grounded"].with_suffix(".txt").write_text(out.getvalue())
    return c["name"]


def ground(clips: list[dict], args) -> None:
    todo = [c for c in clips if args.force or not (newer(c["grounded"], c["k1"]) and c["grounded"].with_suffix(".txt").exists())]
    if not todo:
        return
    ctx = multiprocessing.get_context("spawn")
    with ProcessPoolExecutor(max(1, min(args.workers, len(todo))), mp_context=ctx, initializer=_init_grounder) as pool:
        for i, _ in enumerate(pool.map(ground_one, todo, chunksize=4), 1):
            if i % 200 == 0 or i == len(todo):
                print(f"[ground] {i}/{len(todo)}")


# ---------------------------------------------------------------------------------------- stage 5: QC

def human_wrist_forward(job: tuple[Path, Path]) -> list[float]:
    """Mean (left, right) wrist position along the human's forward axis, relative to the pelvis, m."""
    smplx_npz, model_dir = job
    take = b2g.read_take(smplx_npz, model_dir, "+z", verbose=False)
    pos, pelvis_rot = b2g.body_joint_positions(take, model_dir)
    return [float(pelvis_rot.inv().apply(pos[:, j] - pos[:, 0])[:, 2].mean())  # SMPL-X body +z = forward
            for j in (b2g.L_WRIST, b2g.R_WRIST)]


def ik_failures(log: Path) -> int:
    m = re.search(r"IK failed on (\d+) frames", log.read_text()) if log.exists() else None
    return int(m.group(1)) if m else 0


def qc(clips: list[dict], spec: dict, args) -> list[dict]:
    limits = {k: v for k, v in spec.get("qc", {}).items() if k in clip_qc.LIMITS}
    cfg = spec["segment_cfg"]
    exclude = args.exclude or spec.get("qc", {}).get("exclude", "severe")
    cached = spec["out_dir"] / "qc.json"
    # Reuse the last QC if it covers exactly these clips with these limits and no clip changed since.
    if not args.force and cached.exists() and all(newer(cached, c["grounded"]) for c in clips):
        old = json.loads(cached.read_text())
        if old.get("limits", {}) == limits and [r["name"] for r in old["clips"]] == [c["name"] for c in clips]:
            rows = old["clips"]
            clip_qc.flag(rows, limits)  # flags depend only on the stored numbers: re-flag with the current rules
            for r in rows:
                r["excluded"] = bool((exclude == "severe" and r["severe"]) or (exclude == "flagged" and r["flags"]))
            print(f"[qc] {len(rows)} clips, cached {cached}")
            return rows
    k1 = clip_qc.check_all([c["grounded"] for c in clips], args.workers, limits)
    wrists = bs.pool_map(human_wrist_forward, [(c["smplx"], spec["model_dir"]) for c in clips], args.workers)
    rows = []
    for c, r, w in zip(clips, k1, wrists):
        r.update({k: v for k, v in c.items() if k not in ("smplx", "k1", "grounded")},
                 hand_fwd_human_m=w, ik_fail_frames=ik_failures(c["grounded"].with_suffix(".txt")),
                 max_foot_move_cm=cfg.tier_a_cm if c["tier"] == "A" else cfg.tier_b_cm)
        rows.append(r)
    clip_qc.flag(rows, limits)
    for r in rows:
        r["excluded"] = bool((exclude == "severe" and r["severe"]) or (exclude == "flagged" and r["flags"]))
    return rows


def write_qc(rows: list[dict], spec: dict, artifacts: dict, path: Path) -> None:
    """Per speaker / tier summary, how often each check fires, and every flagged clip."""
    exclude = spec.get("qc", {}).get("exclude", "severe")
    kinds = {}
    for r in rows:
        for f in r["flags"]:
            k = re.sub(r"[\d.]+", "#", f.split(" (")[0])
            kinds.setdefault(k, [0, 0])
            kinds[k][0] += 1
            kinds[k][1] += f in r["severe"]
    lines = [
        "# BEAT2 Clip QC (Gate 1)",
        "",
        f"Generated {date.today()} by `tools/beat2_batch.py --spec {spec['_spec_path']}`. "
        "Checks and limits: `tools/clip_qc.py` (calibration: `notes/gate1-calibration.md`). All numbers per clip: "
        f"`{spec['out_dir'] / 'qc.json'}`.",
        "",
        f"- **Clips:** {len(rows)}, **{sum(bool(r['flags']) for r in rows)} flagged**, "
        f"{sum(bool(r['severe']) for r in rows)} severe; {sum(r['excluded'] for r in rows)} left out (`exclude = {exclude}`)",
        f"- **IK config:** `{spec.get('ik_config') or 'GMR default'}`",
    ]
    for name, art in artifacts.items():
        lines.append(f"- **{name}:** `{art}`")
    lines += ["", "## Per speaker", "", "| group | speaker | tier | clips | minutes | flagged | severe | kept min |",
              "|---|---|---|---|---|---|---|---|"]
    keys = sorted({(r["group"], r["speaker"], r["tier"]) for r in rows}, key=lambda k: (k[0] != "train", int(k[1].split("_")[0]), k[2]))
    for g, s, t in keys:
        rs = [r for r in rows if (r["group"], r["speaker"], r["tier"]) == (g, s, t)]
        mins = sum(r["end"] - r["start"] for r in rs) / 60
        kept = sum(r["end"] - r["start"] for r in rs if not r["excluded"]) / 60
        lines.append(f"| {g} | {s} | {t} | {len(rs)} | {mins:.1f} | {sum(bool(r['flags']) for r in rs)} | "
                     f"{sum(bool(r['severe']) for r in rs)} | {kept:.1f} |")
    lines += ["", "## Checks that fired", "", "| flag | clips | severe |", "|---|---|---|"]
    lines += [f"| {k} | {n} | {sv} |" for k, (n, sv) in sorted(kinds.items(), key=lambda kv: -kv[1][0])]
    lines += ["", "## Flagged clips", "", "Severe in **bold**.", "",
              "| clip | tier | source | feet human / K1 (cm) | arms human / K1 (cm/s) | flags |", "|---|---|---|---|---|---|"]
    for r in sorted((r for r in rows if r["flags"]), key=lambda r: (not r["severe"], r["name"])):
        fl = "; ".join(f"**{x}**" if x in r["severe"] else x for x in r["flags"]) + (" *(excluded)*" if r["excluded"] else "")
        lines.append(f"| `{r['name']}` | {r['tier']} | {r['take']} {r['start']:.1f}–{r['end']:.1f} s | "
                     f"{r['feet_human_cm']:.1f} / {r['feet_k1_cm']:.1f} | {r['arms_human_cm_s']:.0f} / {r['arms_k1_cm_s']:.0f} | {fl} |")
    path.write_text("\n".join(lines) + "\n")


# ---------------------------------------------------------------------------------------- stage 6: combine

def is_training(s: dict) -> bool:
    return s["speakers"] == "train" and set(s["takes"]) <= TRAINING_TYPES


def check_sets(clips: list[dict], spec: dict) -> None:
    """Training sets: no take may also be in an eval set (they never share a speaker group + type, but check)."""
    train_takes = {c["take"] for c in clips for s in c["sets"] if is_training(spec["sets"][s])}
    eval_takes = {c["take"] for c in clips for s in c["sets"] if not is_training(spec["sets"][s])}
    shared = sorted(train_takes & eval_takes)
    if shared:
        sys.exit(f"[leakage] {len(shared)} takes are in both a training and an eval set, e.g. {shared[:5]}")


def combine(name: str, clips: list[dict], spec: dict, args) -> str | None:
    if not clips:
        print(f"[combine] {name}: no clips; skipping")
        return None
    art = f"{spec['name']}-{name}"
    out = spec["out_dir"] / "combined" / f"{art}.npz"
    hours = sum(c["end"] - c["start"] for c in clips) / 3600
    # Reuse the file if it holds exactly these clips and is newer than all of them (converting
    # thousands of .pkl clips again takes about an hour; uploading afterwards shouldn't).
    if (not args.force and out.exists() and all(newer(out, c["grounded"]) for c in clips)
            and clip_qc.combined_clip_names(out) == [c["name"] for c in clips]):
        print(f"[combine] {name}: {len(clips)} clips, {hours:.2f} h, cached {out}")
    else:
        cmd = ["uv", "run", "combine-motions", *[str(c["grounded"]) for c in clips], "--workers", str(args.workers),
               "--no-upload", "--output", str(out)]
        print(f"[combine] {name}: {len(clips)} clips, {hours:.2f} h -> {out}")
        subprocess.run(cmd, check=True, cwd=REPO, capture_output=True, text=True)

    s = spec["sets"][name]
    if is_training(s):  # check the file that was actually written, not the list we meant to write
        split = bs.load_split(spec["beat2_dir"])
        heldout = {k for k, g in bs.speaker_groups(spec, split).items() if g == "heldout"}
        problems = clip_qc.leakage(clip_qc.combined_clip_names(out), split, heldout, set(s["takes"]))
        if problems:
            sys.exit(f"[leakage] {art}: {len(problems)} problems, e.g. {problems[:5]}; not uploading")
        print(f"[leakage] {art}: clean (no held-out speakers, only {'/'.join(s['takes'])} takes)")
    if not args.upload:
        return str(out)
    cmd = ["uv", "run", "combine-motions", str(out), "--artifact-name", art] + (["--entity", args.entity] if args.entity else [])
    res = subprocess.run(cmd, check=True, cwd=REPO, capture_output=True, text=True)
    m = re.search(r"Uploaded artifact: (\S+)", res.stdout)
    print(f"[upload] {m.group(1) if m else art}")
    return m.group(1) if m else art


# ---------------------------------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spec", type=Path, required=True, help="dataset spec, e.g. tools/datasets/beat2_full.toml")
    ap.add_argument("--stages", nargs="+", choices=STAGES, default=list(STAGES),
                    help="run up to and including the last stage listed (earlier stages reuse their cache)")
    ap.add_argument("--sets", nargs="+", default=None, help="only build these sets (default: all in the spec)")
    ap.add_argument("--entity", default=os.environ.get("WANDB_ENTITY"))
    ap.add_argument("--no-upload", dest="upload", action="store_false", help="write <out_dir>/combined/*.npz only")
    ap.add_argument("--exclude", choices=("none", "severe", "flagged"), default=None, help="override the spec's qc.exclude")
    ap.add_argument("--workers", type=int, default=min(12, os.cpu_count() or 1),
                    help="clips processed at once in each stage (same output as 1; ~1.5 GB RAM each)")
    ap.add_argument("--force", action="store_true", help="redo every stage")
    args = ap.parse_args()

    spec = bs.load_spec(args.spec)
    spec["_spec_path"] = args.spec
    spec["model_dir"] = Path(os.path.expanduser(spec.get("model_dir", str(b2g.DEFAULT_MODEL_DIR))))
    if args.sets:
        unknown = set(args.sets) - set(spec["sets"])
        if unknown:
            sys.exit(f"Sets not in the spec: {sorted(unknown)}")
        spec["sets"] = {k: v for k, v in spec["sets"].items() if k in args.sets}
    last = max(STAGES.index(s) for s in args.stages)
    run = lambda stage: STAGES.index(stage) <= last  # noqa: E731
    t0 = time.time()

    # 1. segments (human side)
    takes, missing = bs.segment_all(spec, args.workers)
    bs.write_report(spec, takes, missing, spec.get("segments_report") or REPO / "notes/beat2-segments.md")
    spec["out_dir"].mkdir(parents=True, exist_ok=True)
    (spec["out_dir"] / "segments.json").write_text(json.dumps({"cfg": asdict(spec["segment_cfg"]), "missing": missing, "takes": takes}, indent=1))
    clips = clips_from_segments(spec, takes)
    print(f"[segment] {len(takes)} takes -> {len(clips)} clips, {sum(c['end'] - c['start'] for c in clips) / 3600:.1f} h "
          f"({len(missing)} takes not on disk) -> {spec.get('segments_report')}")
    if missing:
        print(f"[warn] {len(missing)} takes the spec uses are not downloaded, e.g. {missing[:3]}")
    if not run("convert"):
        return
    check_stamp(spec, args.force)
    check_sets(clips, spec)

    # 2-4. convert, retarget, ground
    convert(clips, spec, args)
    if run("retarget"):
        retarget(clips, spec, args)
    if run("ground"):
        ground(clips, args)
    if not run("qc"):
        return

    # 5. QC
    rows = qc(clips, spec, args)
    limits = {k: v for k, v in spec.get("qc", {}).items() if k in clip_qc.LIMITS}
    (spec["out_dir"] / "qc.json").write_text(json.dumps({"limits": limits, "clips": rows}, indent=1, default=str))

    # 6. combine
    artifacts = {}
    if run("combine"):
        keep = [c for c, r in zip(clips, rows) if not r["excluded"]]
        for name in spec["sets"]:
            art = combine(name, [c for c in keep if name in c["sets"]], spec, args)
            if art:
                artifacts[name] = art
    write_qc(rows, spec, artifacts, spec.get("qc_report") or REPO / "notes/beat2-qc.md")
    print(f"[qc] {len(rows)} clips, {sum(bool(r['flags']) for r in rows)} flagged, "
          f"{sum(r['excluded'] for r in rows)} excluded -> {spec.get('qc_report')}")
    print(f"[done] {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
