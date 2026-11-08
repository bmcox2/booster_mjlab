"""The whole v0 conversation: record -> speech-to-text -> LLM -> text-to-speech -> play, repeated.

Run it (from the speech/ folder):
    uv run python -m speech.loop

Press Enter, talk, press Enter. The robot answers out loud. Repeat. Type q + Enter to quit.
Each turn is saved in runs/<session>/turn_NN/ with the same files the single stages write, so any
turn can be re-run one stage at a time (e.g. uv run python -m speech.tts runs/<session>/turn_03).

This is step 1 of notes/speech_plan.md: one turn at a time, nothing overlaps yet. The models
are loaded once at the start, so each turn only pays for the actual work.
"""

import json
import time
from datetime import datetime

import numpy as np

from speech.audio import describe, find_device, play, record_until_enter, save_wav
from speech.config import RUNS_DIR, load_config
from speech.llm import ChatModel, session_history
from speech.stt import SpeechToText
from speech.tts import KOKORO_SAMPLE_RATE, TextToSpeech


def save_json(path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def main() -> None:
    cfg = load_config()
    in_dev = find_device(cfg["audio"]["input_device"], "input")
    out_dev = find_device(cfg["audio"]["output_device"], "output")
    sample_rate = cfg["audio"]["sample_rate"]

    print("loading models...")
    stt = SpeechToText(cfg["stt"])
    tts = TextToSpeech(cfg["tts"])
    llm = ChatModel(cfg["llm"])
    # Warm-up: the first use of a model is slower than the rest (memory setup, caches), so we
    # run each local model once on throwaway input before the conversation starts.
    stt.transcribe(np.zeros(sample_rate, dtype=np.float32))
    tts.synthesize("Ready.")
    print(f"ready (speech-to-text {cfg['stt']['model']}, LLM {cfg['llm']['model']}, "
          f"voice {cfg['tts']['voice']})\n")

    session = RUNS_DIR / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    turn_number = 0
    while True:
        audio = record_until_enter(sample_rate, in_dev,
                                   prompt="Press Enter to talk (q + Enter to quit)... ")
        if audio is None:
            break
        stopped = time.monotonic()  # you finished talking here
        turn_number += 1
        turn = session / f"turn_{turn_number:02d}"
        save_wav(turn / "input.wav", audio, sample_rate)

        transcript = stt.transcribe(audio)
        save_json(turn / "transcript.json", transcript)
        print(f'you: "{transcript["text"]}"')
        if not transcript["text"]:
            print(f"(heard nothing: {describe(audio, sample_rate)}; try again)\n")
            continue

        messages = llm.build_messages(session_history(turn), transcript["text"])
        save_json(turn / "request.json", {"model": llm.cfg["model"], "messages": messages})
        reply = llm.reply(messages)
        save_json(turn / "reply.json", reply)
        print(f'robot: "{reply["text"]}"')

        speech, tts_info = tts.synthesize(reply["text"])
        save_wav(turn / "reply.wav", speech, KOKORO_SAMPLE_RATE)
        save_json(turn / "tts.json", tts_info)

        # How long you waited between stopping talking and hearing the answer, and where it went.
        # (Step 2 of the plan replaces this rough line with proper timing files.)
        waited = time.monotonic() - stopped
        print(f"[waited {waited:.1f} s: speech-to-text {transcript['transcribe_seconds']:.1f}, "
              f"LLM {reply['total_seconds']:.1f}, text-to-speech {tts_info['synthesize_seconds']:.1f}]")
        play(speech, KOKORO_SAMPLE_RATE, out_dev)
        print()

    print(f"saved {turn_number} turns in {session}")


if __name__ == "__main__":
    main()
