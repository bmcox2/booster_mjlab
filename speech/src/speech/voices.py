"""Listen to Kokoro voices side by side to pick one for the robot.

Run it (from the speech/ folder):
    uv run python -m speech.voices                          # all English male voices
    uv run python -m speech.voices am_michael bm_george     # just these
    uv run python -m speech.voices --text "Your own sentence here."

Each voice says the same sentence; you press Enter to go to the next one (r + Enter to repeat).
The samples are also saved in runs/_voices/ so you can replay them later.
To use a voice, set   voice = "<name>"   under [tts] in config.toml.

Voice names: first letter = accent (a = American, b = British), second = f/m (female/male).
"""

import argparse

from speech.audio import find_device, play, save_wav
from speech.config import RUNS_DIR, load_config
from speech.tts import KOKORO_SAMPLE_RATE, TextToSpeech

ENGLISH_MALE = ["am_adam", "am_echo", "am_eric", "am_fenrir", "am_liam", "am_michael",
                "am_onyx", "am_puck", "am_santa", "bm_daniel", "bm_fable", "bm_george", "bm_lewis"]
DEFAULT_TEXT = ("Hi, I'm the Booster K1. I can wave, point, and talk with you. "
                "So, what are we working on today?")


def main() -> None:
    parser = argparse.ArgumentParser(description="Play Kokoro voices one after another.")
    parser.add_argument("voices", nargs="*", default=ENGLISH_MALE, help="voice names (default: English male)")
    parser.add_argument("--text", default=DEFAULT_TEXT, help="sentence every voice says")
    args = parser.parse_args()

    cfg = load_config()
    out_dev = find_device(cfg["audio"]["output_device"], "output")
    print("loading the voice model...")
    tts = TextToSpeech(cfg["tts"])

    for i, voice in enumerate(args.voices, 1):
        audio, _ = tts.synthesize(args.text, voice=voice)
        save_wav(RUNS_DIR / "_voices" / f"{voice}.wav", audio, KOKORO_SAMPLE_RATE)
        while True:
            print(f"[{i}/{len(args.voices)}] {voice}")
            play(audio, KOKORO_SAMPLE_RATE, out_dev)
            if input("  Enter = next, r + Enter = repeat... ").strip().lower() != "r":
                break

    print(f"\nsamples saved in {RUNS_DIR / '_voices'}")
    print('to use one: set  voice = "<name>"  under [tts] in config.toml')


if __name__ == "__main__":
    main()
