"""Summarize runs/latency.jsonl: typical (median) and bad-case (p90) time per stage, per setup.

Run it (from the speech/ folder):
    uv run python -m speech.latency                 # every turn ever logged
    uv run python -m speech.latency --mode testset  # only test-set replays (comparable runs)
    uv run python -m speech.latency --last 20       # only the 20 most recent turns

median = the middle value: half the turns were faster, half slower ("typical").
p90    = 90% of turns were at least this fast ("a bad but normal turn").
Turns are grouped by setup (which speech-to-text, LLM, voice), so different setups don't mix.
"""

import argparse
import json
import statistics
from collections import defaultdict

from speech.timing import LATENCY_LOG, STAGES


def p90(values: list[float]) -> float:
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, round(0.9 * (len(ordered) - 1)))]


def main() -> None:
    parser = argparse.ArgumentParser(description="Median / p90 per stage from runs/latency.jsonl.")
    parser.add_argument("--mode", choices=["live", "testset"], help="only this kind of turn")
    parser.add_argument("--last", type=int, help="only the N most recent turns")
    args = parser.parse_args()

    if not LATENCY_LOG.exists():
        raise SystemExit(f"No {LATENCY_LOG} yet. Run the loop or the test set first.")
    records = [json.loads(line) for line in LATENCY_LOG.read_text().splitlines() if line.strip()]
    records = [r for r in records if "skipped" not in r and (not args.mode or r["mode"] == args.mode)]
    if args.last:
        records = records[-args.last:]
    if not records:
        raise SystemExit("No matching turns.")

    groups = defaultdict(list)
    for r in records:
        groups[(r["mode"], r["label"])].append(r)

    stage_names = list(STAGES)
    for (mode, label), rs in groups.items():
        print(f"\n{mode}: {label}   ({len(rs)} turns)")
        print(f"  {'stage':20} {'median s':>9} {'p90 s':>8} {'max s':>8}")
        for name in stage_names:
            values = [r["stages"][name] for r in rs if name in r["stages"]]
            if values:
                print(f"  {name:20} {statistics.median(values):9.2f} {p90(values):8.2f} {max(values):8.2f}")
        fallbacks = sum(r.get("fallback_used", False) for r in rs)
        if fallbacks:
            print(f"  ({fallbacks} turns used the speech-to-text fallback)")
        wers = [r["wer"] for r in rs if r.get("wer") is not None]
        if wers:
            print(f"  word error rate: mean {statistics.mean(wers):.1%}, worst {max(wers):.1%}")
    print("\nresponse = you stop talking -> audio starts (target: median < 1.0 s, p90 < 1.5 s)")


if __name__ == "__main__":
    main()
