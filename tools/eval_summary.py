"""Group eval-tracking results by tier and speaker, and compare runs side by side.

eval-tracking writes one row per clip (logs/eval/<run>_<checkpoint>_<motion>.json). For the full BEAT2
sets the question is per group: Tier A (still) vs Tier B (foot shifts, clip names ending in _shift),
and per speaker (held-out speakers differ a lot: read them separately). Each column is one JSON.

Per group: clips, clips with every rollout finishing (all 50/50), rollout success rate, and mean hand
error (cm, over the clips' mean errors, weighted by clip length).

Usage (from the repo):
    uv run python tools/eval_summary.py logs/eval/<runA>_model_5999_beat2-full-torso-val_v0.json \\
        logs/eval/<runAB>_model_5999_beat2-full-torso-val_v0.json
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

import numpy as np


def groups(name: str) -> list[str]:
    tier = "B (_shift)" if name.endswith("_shift") else "A"
    return ["all", f"tier {tier}", f"speaker {name.split('_')[0]}"]


def summarize(path: Path) -> dict[str, dict]:
    clips = json.loads(path.read_text())["clips"]
    acc: dict[str, list[dict]] = defaultdict(list)
    for name, c in clips.items():
        for g in groups(name):
            acc[g].append(c)
    out = {}
    for g, cs in acc.items():
        w = np.array([c["clip_seconds"] for c in cs])
        hand = np.array([c["hand_err_cm_mean"] for c in cs], dtype=float)
        ok = np.isfinite(hand)
        out[g] = {
            "clips": len(cs),
            "all_pass": sum(c["passed"] for c in cs),
            "success": sum(c["successes"] for c in cs) / max(1, sum(c["rollouts"] for c in cs)),
            "hand_cm": float(np.average(hand[ok], weights=w[ok])) if ok.any() else float("nan"),
        }
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("evals", type=Path, nargs="+", help="eval-tracking JSON files (one column each)")
    args = ap.parse_args()
    cols = [(p.stem, summarize(p)) for p in args.evals]
    keys = sorted({g for _, s in cols for g in s}, key=lambda g: (not g.startswith("all"), not g.startswith("tier"), g))
    print("| group | " + " | ".join(name for name, _ in cols) + " |")
    print("|---|" + "---|" * len(cols))
    for g in keys:
        cells = []
        for _, s in cols:
            r = s.get(g)
            cells.append("—" if r is None else
                         f"{r['all_pass']}/{r['clips']} clips all-pass, {r['success']:.1%} rollouts, hands {r['hand_cm']:.2f} cm")
        print(f"| {g} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    main()
