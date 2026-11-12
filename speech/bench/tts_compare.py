"""Compare text-to-speech engines by speed (time to voice the first piece) and by ear.

Run (from speech/):
    uv run python bench/tts_compare.py                       # every engine that has a key
    uv run python bench/tts_compare.py kokoro orpheus        # just these
    uv run python bench/tts_compare.py --listen-only         # blind listening test on the saved samples

Uses the pieces of recent live replies (runs/2026-11-11_*/turn_*/tts.json):
  1. speed: each engine voices the first piece of 12 replies (the piece the listener waits for)
  2. by ear: each engine voices 3 whole replies piece by piece, put together exactly as the
     stream plays them (padding trimmed, pause after each piece) -> runs/_voices/compare/<engine>_N.wav
Orpheus (Groq free tier: 100 requests/day, 10/min) uses ~21 requests per run: add --gap-s 6.5.
Results: runs/_bench/tts_compare.json
"""
import argparse, json, os, statistics, time, warnings
from pathlib import Path

import numpy as np

warnings.simplefilter("ignore")
from speech.audio import find_device, play, save_wav  # noqa: E402
from speech.config import load_config  # noqa: E402
from speech.streaming import pause_after, trim_silence  # noqa: E402
from speech.tts import ENGINES, SAMPLE_RATE, CloudError  # noqa: E402

SPEECH = Path(__file__).resolve().parents[1]
OUT = SPEECH / "runs/_bench/tts_compare.json"
WAVS = SPEECH / "runs/_voices/compare"


def level(audio: np.ndarray, target_rms: float = 0.08) -> np.ndarray:
    """Same loudness for every engine (louder samples tend to sound "better" in a comparison)."""
    voiced = audio[np.abs(audio) > 0.01]
    return audio * (target_rms / max(float(np.sqrt(np.mean(voiced ** 2))), 1e-6)) if len(voiced) else audio


def replies() -> list[list[str]]:
    out = []
    for p in sorted(SPEECH.glob("runs/2026-11-11_*/turn_*/tts.json")):
        chunks = json.loads(p.read_text()).get("chunks", [])
        if chunks:
            out.append([c["text"] for c in chunks])
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("engines", nargs="*", default=list(ENGINES))
    parser.add_argument("--listen", action="store_true", help="play the samples afterwards")
    parser.add_argument("--n-first", type=int, default=12)
    parser.add_argument("--n-whole", type=int, default=3)
    parser.add_argument("--gap-s", type=float, default=0.0,
                        help="wait between cloud requests (Orpheus free tier: 10 requests/min -> 6.5)")
    parser.add_argument("--listen-only", action="store_true", help="skip voicing; blind test on saved samples")
    args = parser.parse_args()

    cfg = load_config()
    if args.listen_only:
        blind_listen(cfg, args.engines, args.n_whole)
        return
    all_replies = replies()
    first_pieces = [r[0] for r in all_replies[-args.n_first:]]
    whole = [r for r in all_replies if len(r) >= 3][-args.n_whole:]
    results = json.loads(OUT.read_text()) if OUT.exists() else {}
    WAVS.mkdir(parents=True, exist_ok=True)

    for name in args.engines:
        ecfg = cfg["tts"] if name == "kokoro" else cfg["tts"][name]
        if name != "kokoro" and not os.environ.get(ecfg["api_key_env"]):
            print(f"{name}: skipped (no {ecfg['api_key_env']} in speech/.env)")
            continue
        engine = ENGINES[name](ecfg)
        engine.synthesize("Ready.")  # warm up (opens the connection)
        times, firsts, fails = [], [], 0
        for text in first_pieces:
            if name != "kokoro":
                time.sleep(args.gap_s)
            t0 = time.monotonic()
            try:
                audio, info = engine.synthesize(text)
            except CloudError as e:
                print(f"  {name} failed: {e}")
                fails += 1
                continue
            times.append(time.monotonic() - t0)
            firsts.append(info.get("first_bytes_seconds", times[-1]))
        for i, pieces in enumerate(whole):
            parts = []
            for text in pieces:
                if name != "kokoro":
                    time.sleep(args.gap_s)
                try:
                    audio, _ = engine.synthesize(text)
                except CloudError as e:
                    print(f"  {name} failed: {e}")
                    fails += 1
                    continue
                audio, _ = trim_silence(audio, SAMPLE_RATE)
                parts += [audio, np.zeros(int(pause_after(text, cfg["stream"]) * SAMPLE_RATE), np.float32)]
            if parts:
                save_wav(WAVS / f"{name}_{i + 1}.wav", level(np.concatenate(parts)), SAMPLE_RATE)
        if not times:
            continue
        row = {"voice": ecfg["voice"], "n": len(times), "fails": fails,
               "first_piece_median_s": round(statistics.median(times), 3),
               "first_piece_p90_s": round(float(np.percentile(times, 90)), 3),
               "first_piece_max_s": round(max(times), 3),
               "first_bytes_median_s": round(statistics.median(firsts), 3),
               "date": time.strftime("%Y-%m-%d %H:%M")}
        results[name] = row
        OUT.parent.mkdir(parents=True, exist_ok=True)
        OUT.write_text(json.dumps(results, indent=1))
        print(f"{name:11s} first piece median {row['first_piece_median_s']:.2f} s, p90 "
              f"{row['first_piece_p90_s']:.2f}, max {row['first_piece_max_s']:.2f}; "
              f"first bytes {row['first_bytes_median_s']:.2f} s; fails {fails}", flush=True)

    print(f"\nsamples in {WAVS}")
    for i, pieces in enumerate(whole):
        print(f"  _{i + 1}: " + " ".join(pieces))
    if args.listen:
        blind_listen(cfg, args.engines, len(whole))


def blind_listen(cfg: dict, engines: list[str], n: int) -> None:
    """Play each reply once per engine in a shuffled order labeled A, B, C...; you score each 1-5;
    the engine names are shown only at the end (so you judge the voice, not the name)."""
    import random
    import soundfile as sf
    dev = find_device(cfg["audio"]["output_device"], "output")
    scores = {e: [] for e in engines}
    print("\nBlind test: score each version 1 (robotic) to 5 (natural). r = replay.")
    for i in range(n):
        files = [(e, WAVS / f"{e}_{i + 1}.wav") for e in engines if (WAVS / f"{e}_{i + 1}.wav").exists()]
        random.shuffle(files)
        print(f"\nreply {i + 1}")
        for label, (engine, f) in zip("ABCDEF", files):
            audio, rate = sf.read(f, dtype="float32")
            while True:
                print(f"  {label}: playing...")
                play(audio, rate, dev)
                ans = input(f"  {label} score 1-5 (r = replay): ").strip().lower()
                if ans in {"1", "2", "3", "4", "5"}:
                    scores[engine].append(int(ans))
                    break
    print("\nresults (mean score, higher = more natural):")
    for e, v in sorted(scores.items(), key=lambda kv: -statistics.mean(kv[1]) if kv[1] else 0):
        if v:
            print(f"  {e:11s} {statistics.mean(v):.2f}  {v}")
    out = SPEECH / "runs/_bench/tts_listen.json"
    log = json.loads(out.read_text()) if out.exists() else []
    log.append({"date": time.strftime("%Y-%m-%d %H:%M"), "scores": scores})
    out.write_text(json.dumps(log, indent=1))


if __name__ == "__main__":
    main()
