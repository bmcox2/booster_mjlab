"""Combine several tracking clips into one motion.npz for MultiMotionCommand, and upload it as one artifact.

The output is upload-motion's format with every clip's frames concatenated end to end, plus a
clip table (`clip_lengths`, `clip_names`, `clip_sources`). Training still takes a single
`--registry-name`, and MultiMotionCommand keeps each robot inside its own clip.

Sources can be mixed:
- W&B motion artifacts: `<entity>/motion_upload/wave_000508-tracking:v3` (no version = :latest)
- local tracking .npz files (upload-motion's output); a combined .npz contributes all its clips
- local GMR .pkl clips, e.g. ground_clip.py's `*_grounded.pkl` (converted like upload-motion does)

Clip names default to the artifact/file name without `-tracking`, `_grounded` and the version;
pass --names to choose your own. Names show up in W&B as Metrics/motion/clip/<metric>/<name>.

Usage:
    uv run combine-motions <entity>/motion_upload/wave_000508-tracking:v3 \\
        <entity>/motion_upload/wave_001104-tracking:v2 --artifact-name waves-2clip
    uv run combine-motions ... --output logs/motions/waves_2clip.npz --no-upload   # local only
    uv run combine-motions a.pkl b.pkl ... --workers 8   # convert .pkl clips in parallel (same output)
"""

from __future__ import annotations

import multiprocessing
import os
import re
import tempfile
import zipfile
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import tyro

FRAME_KEYS = ("joint_pos", "joint_vel", "body_pos_w", "body_quat_w", "body_lin_vel_w", "body_ang_vel_w")


@dataclass(frozen=True)
class Config:
    sources: tyro.conf.Positional[tuple[str, ...]]
    """Clips to combine, in order: W&B artifact names, tracking .npz files, or GMR .pkl files."""
    artifact_name: str | None = None
    """W&B artifact name for the combined file (required unless --no-upload)."""
    names: tuple[str, ...] | None = None
    """Clip names, one per clip, overriding the defaults."""
    output: Path | None = None
    """Also save the combined file here."""
    upload: bool = True
    entity: str | None = os.environ.get("WANDB_ENTITY")
    project: str = "motion_upload"
    device: str = "cpu"
    """Device for converting .pkl clips."""
    workers: int = 1
    """Convert .pkl clips in this many processes at once. Each conversion builds its own one-robot sim and
    runs on one core, so this scales with cores; the output is identical (clips keep their order)."""


@dataclass
class Clip:
    name: str
    source: str
    fps: float
    frames: dict[str, np.ndarray]

    @property
    def num_frames(self) -> int:
        return self.frames["joint_pos"].shape[0]


def _default_name(stem: str) -> str:
    stem = stem.split(":")[0].split("/")[-1]
    stem = stem.removesuffix("-tracking").removesuffix("_grounded")
    return re.sub(r"[^A-Za-z0-9_.-]", "_", stem)


def _clips_from_npz(path: Path, name: str, source: str) -> list[Clip]:
    with np.load(path) as data:
        fps = float(np.asarray(data["fps"]).reshape(-1)[0])
        frames = {k: data[k] for k in FRAME_KEYS}
        if "clip_lengths" not in data.files:
            return [Clip(name, source, fps, frames)]
        # Already combined: split it back into its clips.
        ends = np.cumsum(data["clip_lengths"])
        starts = ends - data["clip_lengths"]
        sources = data["clip_sources"] if "clip_sources" in data.files else [source] * len(ends)
        return [
            Clip(str(n), str(src), fps, {k: v[s:e] for k, v in frames.items()})
            for n, src, s, e in zip(data["clip_names"], sources, starts, ends)
        ]


def load_source(src: str, device: str) -> list[Clip]:
    path = Path(src).expanduser()
    if path.suffix == ".pkl":
        # Same arrays as upload-motion's convert() (bit-identical), but the sim is built once per
        # process and runs 256 frames per forward call: ~25x faster per clip.
        from booster_mjlab.scripts.upload_motion import convert_batched

        data = convert_batched(path, device=device)
        frames = {k: data[k] for k in FRAME_KEYS}
        return [Clip(_default_name(path.stem), str(path.resolve()), float(data["fps"][0]), frames)]
    if path.suffix == ".npz":
        return _clips_from_npz(path, _default_name(path.stem), str(path.resolve()))

    import wandb

    name = src if ":" in src else src + ":latest"
    art = wandb.Api().artifact(name)
    return _clips_from_npz(Path(art.download()) / "motion.npz", _default_name(art.name), art.qualified_name)


def check_compatible(clips: list[Clip]) -> None:
    ref = clips[0]
    for c in clips:
        if not np.isclose(c.fps, ref.fps):
            raise SystemExit(f"{c.name}: {c.fps} fps but {ref.name} is {ref.fps} fps; all clips must match")
        if c.num_frames < 2:
            raise SystemExit(f"{c.name}: needs at least 2 frames, has {c.num_frames}")
        for k in FRAME_KEYS:
            if c.frames[k].shape[1:] != ref.frames[k].shape[1:]:
                raise SystemExit(f"{c.name}: {k} shape {c.frames[k].shape[1:]} != {ref.frames[k].shape[1:]} ({ref.name})")
            if not np.isfinite(c.frames[k]).all():
                raise SystemExit(f"{c.name}: {k} has NaN/inf")
    names = [c.name for c in clips]
    dupes = sorted({n for n in names if names.count(n) > 1})
    if dupes:
        raise SystemExit(f"Duplicate clip names {dupes}; pass --names to tell them apart")


def combine(clips: list[Clip], out: Path) -> None:
    """Write the combined .npz (np.savez's layout), one array at a time.

    np.savez needs every concatenated array in memory at once, on top of the clips: ~2x the data,
    ~13 GB for a 25 h BEAT2 file. Concatenating and writing one key at a time keeps ~1.3x.
    """

    def put(zf: zipfile.ZipFile, key: str, arr: np.ndarray) -> None:
        with zf.open(f"{key}.npy", "w", force_zip64=True) as f:
            np.lib.format.write_array(f, np.asanyarray(arr), allow_pickle=False)

    with zipfile.ZipFile(out, "w", zipfile.ZIP_STORED, allowZip64=True) as zf:
        put(zf, "fps", np.array([clips[0].fps], dtype=np.float32))
        for k in FRAME_KEYS:
            put(zf, k, np.concatenate([c.frames[k] for c in clips], axis=0))
        put(zf, "clip_lengths", np.array([c.num_frames for c in clips], dtype=np.int64))
        put(zf, "clip_names", np.array([c.name for c in clips]))
        put(zf, "clip_sources", np.array([c.source for c in clips]))


def upload(cfg: Config, clips: list[Clip], motion_path: Path) -> str:
    import wandb

    run = wandb.init(entity=cfg.entity, project=cfg.project, name=cfg.artifact_name, job_type="combine-motions")
    artifact = wandb.Artifact(
        cfg.artifact_name,
        type="motions",
        metadata={
            "clip_names": [c.name for c in clips],
            "clip_lengths": [c.num_frames for c in clips],
            "clip_sources": [c.source for c in clips],
            "fps": clips[0].fps,
        },
    )
    artifact.add_file(str(motion_path), name="motion.npz")
    for c in clips:  # lineage: the W&B graph shows which artifacts went into this one
        if ":" in c.source and not Path(c.source).exists():
            run.use_artifact(c.source)
    run.log_artifact(artifact)
    artifact.wait()
    qualified = artifact.qualified_name
    wandb.finish()
    return qualified


def main() -> None:
    cfg = tyro.cli(Config)
    if cfg.upload and not cfg.artifact_name:
        raise SystemExit("Pass --artifact-name (or --no-upload with --output to only save locally)")
    if not cfg.upload and cfg.output is None:
        raise SystemExit("--no-upload needs --output, or nothing is saved")

    if cfg.workers > 1 and len(cfg.sources) > 1:
        # spawn, not fork: each worker starts clean instead of inheriting torch / warp state.
        with ProcessPoolExecutor(cfg.workers, mp_context=multiprocessing.get_context("spawn")) as pool:
            loaded = list(pool.map(load_source, cfg.sources, [cfg.device] * len(cfg.sources)))
    else:
        loaded = [load_source(src, cfg.device) for src in cfg.sources]
    clips = [clip for src_clips in loaded for clip in src_clips]
    if cfg.names is not None:
        if len(cfg.names) != len(clips):
            raise SystemExit(f"--names has {len(cfg.names)} names for {len(clips)} clips")
        for c, n in zip(clips, cfg.names):
            c.name = n
    check_compatible(clips)

    print(f"{'#':>3}  {'clip':<28} {'frames':>7} {'seconds':>8}  source")
    for i, c in enumerate(clips):
        print(f"{i:>3}  {c.name:<28} {c.num_frames:>7} {c.num_frames / c.fps:>8.2f}  {c.source}")
    total = sum(c.num_frames for c in clips)
    print(f"     {'total':<28} {total:>7} {total / clips[0].fps:>8.2f}")

    with tempfile.TemporaryDirectory() as tmp:
        if cfg.output is not None:  # written in place: no temp copy (a 25 h file is ~7 GB)
            cfg.output.parent.mkdir(parents=True, exist_ok=True)
            motion_path = cfg.output
        else:
            motion_path = Path(tmp) / "motion.npz"
        combine(clips, motion_path)
        if cfg.output is not None:
            print(f"[out] {cfg.output}")
        if cfg.upload:
            print(f"[upload] Uploaded artifact: {upload(cfg, clips, motion_path)}")
            print("Train with: uv run train Mjlab-Tracking-Flat-Booster-K1 --registry-name <that name>")


if __name__ == "__main__":
    main()
