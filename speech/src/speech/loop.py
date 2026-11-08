"""The whole v0 conversation: record -> speech-to-text -> LLM -> text-to-speech -> play, repeated.

Run it (from the speech/ folder):
    uv run python -m speech.loop

Press Enter, talk, press Enter. The robot answers out loud. Repeat. Type q + Enter to quit.
Each turn is saved in runs/<session>/turn_NN/ with the same files the single stages write, plus
timing.json (when each step finished). Every turn is also appended to runs/latency.jsonl;
summarize with: uv run python -m speech.latency

This is step 1-2 of notes/speech_plan.md: one turn at a time, nothing overlaps yet. The models
are loaded once at the start, so each turn only pays for the actual work.
"""

import json
import time
from datetime import datetime
from pathlib import Path

import numpy as np
import sounddevice as sd

from speech.audio import describe, find_device, record_until_enter, save_wav
from speech.config import RUNS_DIR, load_config
from speech.llm import ChatModel, session_history
from speech.metrics import word_error_rate
from speech.stt import SpeechToText
from speech.timing import TurnTimer, config_label
from speech.tts import KOKORO_SAMPLE_RATE, TextToSpeech


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


class Pipeline:
    """The three models, loaded once, and one function that runs a whole turn."""

    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.label = config_label(cfg)
        self.stt = SpeechToText(cfg["stt"])  # loads + warms up its providers
        self.tts = TextToSpeech(cfg["tts"])
        self.llm = ChatModel(cfg["llm"])
        # Warm-up: the first use of a model is slower than the rest (memory setup, caches).
        self.tts.synthesize("Ready.")

    def run_turn(self, audio: np.ndarray, turn: Path, timer: TurnTimer,
                 output_device: int | None, mode: str, history: list[dict] | None = None,
                 reference: str | None = None) -> dict:
        """input audio -> transcript -> reply -> speech (-> played if output_device is set).

        timer must already be started at the moment speech ended. reference = the correct text
        (test set only), to score the transcript. Returns the timing record.
        """
        sample_rate = self.cfg["audio"]["sample_rate"]
        turn.mkdir(parents=True, exist_ok=True)
        meta = {"mode": mode, "label": self.label}

        transcript = self.stt.transcribe(audio)
        timer.mark("stt_done")
        save_wav(turn / "input.wav", audio, sample_rate)  # saving happens after the timestamp
        save_json(turn / "transcript.json", transcript)
        print(f'you: "{transcript["text"]}"')
        meta.update(stt_provider=transcript["provider"], fallback_used=transcript["fallback_used"],
                    input_audio_seconds=transcript["audio_seconds"])
        if reference is not None:
            meta["wer"] = round(word_error_rate(reference, transcript["text"]), 4)
        if not transcript["text"]:
            print(f"(heard nothing: {describe(audio, sample_rate)})")
            return timer.save(turn, {**meta, "skipped": "empty transcript"})

        if history is None:
            history = session_history(turn)
        messages = self.llm.build_messages(history, transcript["text"])
        llm_start = time.monotonic()
        reply = self.llm.reply(messages)
        timer.mark("llm_first_token", llm_start + reply["first_token_seconds"])
        timer.mark("llm_first_sentence", llm_start + reply["first_sentence_seconds"])
        timer.mark("llm_done", llm_start + reply["total_seconds"])
        save_json(turn / "request.json", {"model": self.llm.cfg["model"], "messages": messages})
        save_json(turn / "reply.json", reply)
        print(f'robot: "{reply["text"]}"')

        speech, tts_info = self.tts.synthesize(reply["text"])
        timer.mark("tts_done")
        save_wav(turn / "reply.wav", speech, KOKORO_SAMPLE_RATE)
        save_json(turn / "tts.json", tts_info)
        meta["reply_audio_seconds"] = tts_info["audio_seconds"]

        if output_device is not None:
            sd.play(speech, KOKORO_SAMPLE_RATE, device=output_device)  # returns immediately
            timer.mark("playback_start")
            # Output latency: how long the sound card's buffer takes to reach the speaker.
            timer.extra["output_latency_s"] = round(sd.get_stream().latency, 4)
            record = timer.save(turn, meta)  # save before waiting, so the record is written
            print(f"[{summary_line(record)}]")
            sd.wait()
            return record

        record = timer.save(turn, meta)
        print(f"[{summary_line(record)}]")
        return record


def summary_line(record: dict) -> str:
    s = record["stages"]
    reply_ready = s.get("response", record["events"].get("tts_done", 0.0))
    return (f"answer after {reply_ready:.2f} s: speech-to-text {s.get('stt', 0):.2f}, "
            f"LLM {s.get('llm_total', 0):.2f} (first sentence {s.get('llm_first_sentence', 0):.2f}), "
            f"text-to-speech {s.get('tts', 0):.2f}")


def main() -> None:
    cfg = load_config()
    in_dev = find_device(cfg["audio"]["input_device"], "input")
    out_dev = find_device(cfg["audio"]["output_device"], "output")
    sample_rate = cfg["audio"]["sample_rate"]

    print("loading models...")
    pipeline = Pipeline(cfg)
    print(f"ready ({pipeline.label})\n")

    session = RUNS_DIR / datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    turn_number = 0
    while True:
        audio = record_until_enter(sample_rate, in_dev,
                                   prompt="Press Enter to talk (q + Enter to quit)... ")
        if audio is None:
            break
        timer = TurnTimer()  # you finished talking here: time 0 for this turn
        turn_number += 1
        pipeline.run_turn(audio, session / f"turn_{turn_number:02d}", timer, out_dev, mode="live")
        print()

    print(f"saved {turn_number} turns in {session}")
    print("timing summary: uv run python -m speech.latency")


if __name__ == "__main__":
    main()
