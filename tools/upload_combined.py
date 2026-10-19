"""Upload an already-combined motion .npz to W&B as-is (no re-combining), as artifact `motion.npz`.

`combine-motions <file.npz> --artifact-name X` also uploads a combined file, but re-reads and rewrites
it first; for a 6 GB BEAT2 training file that is minutes of extra work and a second copy on disk.
`train` downloads the artifact and reads `motion.npz`, the same as for combine-motions' uploads. The
clip table (names, lengths, sources) stays inside the .npz; the artifact metadata gets the counts.

Usage (from ~/projects/booster-mjlab):
    uv run python tools/upload_combined.py ~/robotics/data/beat2_full_torso/combined/beat2-full-torso-train-a.npz \\
        --description "BEAT2 Tier A, ..."   # artifact name = file stem
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path

import numpy as np


def summary(npz: Path) -> dict:
    with np.load(npz, allow_pickle=False) as d:
        lengths = d["clip_lengths"]
        fps = float(np.asarray(d["fps"]).reshape(-1)[0])
        names = [str(n) for n in d["clip_names"]]
    speakers = sorted({n.split("_")[0] for n in names})
    return {"num_clips": len(names), "num_frames": int(lengths.sum()), "fps": fps,
            "hours": round(float(lengths.sum()) / fps / 3600, 3), "speakers": speakers,
            "shift_clips": sum(n.endswith("_shift") for n in names)}


def upload(npz: Path, name: str, description: str, entity: str | None, project: str = "motion_upload") -> str:
    import wandb

    meta = summary(npz)
    run = wandb.init(entity=entity, project=project, name=name, job_type="upload-combined")
    art = wandb.Artifact(name, type="motions", description=description, metadata=meta)
    art.add_file(str(npz), name="motion.npz")
    run.log_artifact(art)
    art.wait()
    qualified = art.qualified_name
    wandb.finish()
    return qualified


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("npz", type=Path, nargs="+", help="combined .npz file(s); artifact name = file stem")
    ap.add_argument("--description", default="", help="artifact description (same for every file)")
    ap.add_argument("--entity", default=os.environ.get("WANDB_ENTITY"))
    args = ap.parse_args()
    for npz in args.npz:
        print(f"[upload] {npz.name}: {summary(npz)}", flush=True)
        print(f"[upload] Uploaded artifact: {upload(npz, npz.stem, args.description, args.entity)}", flush=True)


if __name__ == "__main__":
    main()
