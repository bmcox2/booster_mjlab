"""A fixed set of recordings, replayed through the pipeline, so setups can be compared fairly.

Record it once (from the speech/ folder):
    uv run python -m speech.testset record              # read each script aloud (Enter / Enter)
    uv run python -m speech.testset record --only pause_short   # redo one

Replay it (no microphone, no speaker; same audio every time):
    uv run python -m speech.testset run
    uv run python -m speech.testset run --set stt.provider=local     # try another setup
    uv run python -m speech.testset run --set llm.model=qwen/qwen3.8-27b --set tts.cpu_threads=14
Then compare:  uv run python -m speech.latency --mode testset

Files: testset/<id>.wav (your voice; gitignored because the repo is public) and
testset/testset.json (the scripts = correct transcripts; committed). If you said something
different from the script, fix "reference" in testset.json so the word error rate is fair.
Each replay item is its own one-turn conversation (no history), so items don't affect each other.
"""

import argparse
import json
import time
import tomllib
from datetime import datetime

import soundfile as sf

from speech.audio import describe, find_device, record_until_enter, save_wav
from speech.config import RUNS_DIR, SPEECH_DIR, load_config
from speech.timing import TurnTimer

TESTSET_DIR = SPEECH_DIR / "testset"
INDEX = TESTSET_DIR / "testset.json"

# (id, what it tests, how to say it, script). "..." in a script = pause there for the time given.
SCRIPTS = [
    ("short_name", "short question", "normal voice", "What's your name?"),
    ("short_yes", "one-word answer", "just say it", "Yeah."),
    ("short_wave", "short request", "normal voice", "Can you wave at me?"),
    ("names", "project words", "normal voice",
     "I'm in the SIGRobotics club and we work on the Booster K1 in the Booster Lab."),
    ("fillers", "filler words", "say the ums and uhs naturally",
     "Um, so, like, what do you, uh, think about people?"),
    ("pause_short", "mid-sentence pause", "pause about 1 second at the ...",
     "I want to know... how you decide what to say."),
    ("pause_long", "long mid-sentence pause", "pause about 2 seconds at the ...",
     "Okay so the plan is... we finish the speech loop first and then add the gestures."),
    ("explain", "question needing a real answer", "normal voice",
     "Explain what reinforcement learning is in one sentence."),
    ("joke", "open request", "normal voice", "Tell me a joke about robots."),
    ("point", "body request (tool calls later)", "normal voice",
     "Can you look to your left and then point at the table?"),
    ("ramble", "long ramble (~15 s)", "relaxed, like talking to a friend",
     "So today I was thinking about what we should show at the demo. Maybe the robot could "
     "introduce itself, talk a little about how it learned to move from motion capture data, "
     "and then wave at the audience before answering a few questions from the crowd."),
    ("far", "quiet / far away", "stand about 1 meter from the laptop",
     "How's the weather looking today?"),
]


def reference_text(script: str) -> str:
    return " ".join(script.replace("...", " ").split())


def load_index() -> dict:
    return json.loads(INDEX.read_text()) if INDEX.exists() else {}


def record(only: list[str] | None) -> None:
    cfg = load_config()["audio"]
    in_dev = find_device(cfg["input_device"], "input")
    index = load_index()
    items = [s for s in SCRIPTS if not only or s[0] in only]
    print(f"{len(items)} recordings. For each: read the instruction, press Enter, say the line, "
          "press Enter.\nTake a breath before talking, and stop right after the last word.\n")
    for n, (item_id, kind, how, script) in enumerate(items, 1):
        while True:
            print(f"[{n}/{len(items)}] {item_id}  ({kind}; {how})")
            print(f'    "{script}"')
            audio = record_until_enter(cfg["sample_rate"], in_dev,
                                       prompt="    Enter to start (q + Enter to quit)... ")
            if audio is None:
                return
            print(f"    {describe(audio, cfg['sample_rate'])}")
            if input("    Enter = keep, r + Enter = redo... ").strip().lower() != "r":
                break
        save_wav(TESTSET_DIR / f"{item_id}.wav", audio, cfg["sample_rate"])
        index[item_id] = {"kind": kind, "how": how, "reference": reference_text(script),
                          "seconds": round(len(audio) / cfg["sample_rate"], 2)}
        INDEX.write_text(json.dumps(index, indent=2, ensure_ascii=False))
    print(f"\nsaved in {TESTSET_DIR}. Replay with: uv run python -m speech.testset run")


def apply_overrides(cfg: dict, overrides: list[str]) -> None:
    """--set stt.provider=local  ->  cfg["stt"]["provider"] = "local" (numbers/bools parsed)."""
    for item in overrides:
        path, _, raw = item.partition("=")
        try:
            value = tomllib.loads(f"v = {raw}")["v"]
        except tomllib.TOMLDecodeError:
            value = raw
        *parents, key = path.split(".")
        node = cfg
        for p in parents:
            node = node[p]
        node[key] = value


def run(overrides: list[str], only: list[str] | None) -> None:
    from speech.loop import Pipeline  # imported here so `record` doesn't load the models

    index = load_index()
    items = [(i, v) for i, v in index.items() if (TESTSET_DIR / f"{i}.wav").exists()
             and (not only or i in only)]
    if not items:
        raise SystemExit(f"No recordings in {TESTSET_DIR}. Record first: uv run python -m speech.testset record")

    cfg = load_config()
    apply_overrides(cfg, overrides)
    print("loading models...")
    pipeline = Pipeline(cfg)
    print(f"setup: {pipeline.label}\n")

    out = RUNS_DIR / "_testset" / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    rows = []
    for item_id, item in items:
        audio, sample_rate = sf.read(TESTSET_DIR / f"{item_id}.wav", dtype="float32")
        print(f"--- {item_id}")
        timer = TurnTimer()  # the whole recording is available now = "you just stopped talking"
        record = pipeline.run_turn(audio, out / item_id, timer, output_device=None, mode="testset",
                                   history=[], reference=item["reference"])
        rows.append((item_id, record))
        time.sleep(2)  # spacing for the free tier's per-minute limits (not part of any timing)

    print(f"\n{'item':12} {'words wrong':>11} {'stt s':>6} {'llm s':>6} {'tts s':>6} {'reply ready s':>14}")
    for item_id, r in rows:
        s = r["stages"]
        print(f"{item_id:12} {r.get('wer', 0):11.0%} {s.get('stt', 0):6.2f} {s.get('llm_total', 0):6.2f} "
              f"{s.get('tts', 0):6.2f} {r['events'].get('tts_done', 0):14.2f}")
    print(f"\nfiles in {out}\nsummary across runs: uv run python -m speech.latency --mode testset")


def main() -> None:
    parser = argparse.ArgumentParser(description="Record or replay the fixed test set.")
    sub = parser.add_subparsers(dest="command", required=True)
    rec = sub.add_parser("record", help="record the scripts with your voice")
    rec.add_argument("--only", nargs="+", help="item ids to (re)record")
    rep = sub.add_parser("run", help="replay the recordings through the pipeline")
    rep.add_argument("--set", dest="overrides", action="append", default=[],
                     help="override config.toml, e.g. stt.provider=local (repeatable)")
    rep.add_argument("--only", nargs="+", help="item ids to replay")
    args = parser.parse_args()
    if args.command == "record":
        record(args.only)
    else:
        run(args.overrides, args.only)


if __name__ == "__main__":
    main()
