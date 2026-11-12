"""Listen to voices side by side to pick one for the robot.

Run it (from the speech/ folder):
    uv run python -m speech.voices                          # Kokoro's English male voices
    uv run python -m speech.voices --engine orpheus         # Groq Orpheus: all 6 voices
    uv run python -m speech.voices --engine cartesia        # Cartesia: a shortlist of conversational voices
    uv run python -m speech.voices --engine cartesia Toby Archie   # just these (name or voice ID)
    uv run python -m speech.voices --engine cartesia --list # every English Cartesia voice (name, ID, description)
    uv run python -m speech.voices --text "Your own sentence here."

Each voice says the same sentence; press Enter to go to the next one (r + Enter to repeat).
Samples are saved in runs/_voices/<engine>_<voice>.wav and reused when the sentence is the same,
so listening again costs no cloud requests.
To use a voice: set  engine = "<engine>"  under [tts] in config.toml, and the voice under
[tts] (Kokoro) or [tts.<engine>] (cloud; for Cartesia paste the voice ID that is printed).
"""

import argparse
import os
import time

import soundfile as sf

from speech.audio import find_device, play, save_wav
from speech.config import RUNS_DIR, load_config
from speech.tts import ENGINES, SAMPLE_RATE, CloudError

KOKORO_MALE = ["am_adam", "am_echo", "am_eric", "am_fenrir", "am_liam", "am_michael",
               "am_onyx", "am_puck", "am_santa", "bm_daniel", "bm_fable", "bm_george", "bm_lewis"]
ORPHEUS = ["austin", "daniel", "troy", "autumn", "diana", "hannah"]  # 3 male, 3 female
# Cartesia shortlist (2026-11-11, from its voice list: male, English, "conversational"/"warm").
CARTESIA = {
    "Archie": "ef191366-f52f-447a-a398-ed8c0f2943a1",    # warm, conversational British
    "Toby": "3d5ce2fb-e56c-42f0-9ed9-4662484063b4",      # warm, conversational British, polished
    "George": "4bc3cb8c-adb9-4bb8-b5d5-cbbef950b991",    # steady British, assistant
    "Alistair": "c8f7835e-28a3-4f0c-80d7-c1302ac62aae",  # sophisticated, steady British
    "Parker": "30894953-bcce-41fe-892c-15ce19c843ff",    # casual, supportive warmth (US)
    "Corey": "630ed21c-2c5c-41cf-9d82-10a7fd668370",     # cheerful young adult (US)
    "Daniel": "47c38ca4-5f35-497b-b1a3-415245fb35e1",    # clear, crisp assistant (US)
    "Gareth": "3a01612e-07da-4a85-bba8-ce10481df477",    # warm, approachable
}
DEFAULTS = {"kokoro": KOKORO_MALE, "orpheus": ORPHEUS, "cartesia": list(CARTESIA)}
DEFAULT_TEXT = ("Hi, I'm the Booster K1. I can wave, point, and talk with you. "
                "So, what are we working on today?")


def list_cartesia(cfg: dict) -> None:
    import httpx
    headers = {"Authorization": f"Bearer {os.environ[cfg['api_key_env']]}",
               "Cartesia-Version": cfg["api_version"]}
    params, n = {"limit": 100}, 0
    while True:
        r = httpx.get("https://api.cartesia.ai/voices", headers=headers, params=params, timeout=10)
        r.raise_for_status()
        d = r.json()
        for v in d["data"]:
            if v.get("language") == "en":
                n += 1
                print(f"{v['name']:12s} {v.get('gender', ''):10s} {v['id']}  {(v.get('description') or '')[:70]}")
        if not d.get("has_more"):
            break
        params["starting_after"] = d["data"][-1]["id"]
    print(f"{n} English voices. Try some: uv run python -m speech.voices --engine cartesia <name or ID> ...")


def main() -> None:
    parser = argparse.ArgumentParser(description="Play voices one after another.")
    parser.add_argument("voices", nargs="*", help="voice names (default: a list per engine)")
    parser.add_argument("--engine", choices=sorted(ENGINES), default="kokoro")
    parser.add_argument("--text", default=DEFAULT_TEXT, help="sentence every voice says")
    parser.add_argument("--list", action="store_true", help="Cartesia: list its English voices")
    parser.add_argument("--no-play", action="store_true", help="only make the samples")
    args = parser.parse_args()

    cfg = load_config()
    ecfg = cfg["tts"] if args.engine == "kokoro" else cfg["tts"][args.engine]
    if args.list:
        if args.engine != "cartesia":
            raise SystemExit(f"--list is for cartesia; {args.engine} voices: {' '.join(DEFAULTS[args.engine])}")
        return list_cartesia(ecfg)
    names = args.voices or DEFAULTS[args.engine]
    out_dev = None if args.no_play else find_device(cfg["audio"]["output_device"], "output")
    engine = None  # loaded only if a sample has to be made

    for i, name in enumerate(names, 1):
        voice = CARTESIA.get(name, name) if args.engine == "cartesia" else name
        wav = RUNS_DIR / "_voices" / f"{args.engine}_{name}.wav"
        txt = wav.with_suffix(".txt")
        if wav.exists() and txt.exists() and txt.read_text() == args.text:
            audio, _ = sf.read(wav, dtype="float32")  # same sentence as last time: no new request
        else:
            if engine is None:
                print(f"loading {args.engine}...")
                engine = ENGINES[args.engine](ecfg)
            for attempt in range(2):
                try:
                    audio, _ = engine.synthesize(args.text, voice=voice)
                    break
                except CloudError as e:  # e.g. Orpheus' 10 requests/minute: wait once and retry
                    print(f"  {name}: {e}; waiting 10 s")
                    time.sleep(10)
                    engine.blocked_until = 0.0
            else:
                continue
            save_wav(wav, audio, SAMPLE_RATE)
            txt.write_text(args.text)
        label = f"{name} ({voice})" if voice != name else name
        if args.no_play:
            print(f"[{i}/{len(names)}] {label}: saved {wav}")
            continue
        while True:
            print(f"[{i}/{len(names)}] {label}")
            play(audio, SAMPLE_RATE, out_dev)
            if input("  Enter = next, r + Enter = repeat... ").strip().lower() != "r":
                break

    print(f"\nsamples saved in {RUNS_DIR / '_voices'}")
    where = "[tts] voice" if args.engine == "kokoro" else f"[tts.{args.engine}] voice"
    print(f'to use one: set  engine = "{args.engine}"  under [tts] and  {where}  in config.toml')


if __name__ == "__main__":
    main()
