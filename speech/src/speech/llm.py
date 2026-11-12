"""Stage 3 of the speech loop: the LLM (large language model). transcript.json -> reply.json

Run it (from the speech/ folder):
    uv run python -m speech.llm                         # reply to the most recent transcript
    uv run python -m speech.llm runs/<session>/turn_02  # reply to a specific turn

The model runs on Groq's servers. We talk to it with the "OpenAI-compatible" chat API, a format
many providers accept (Groq, Gemini, a local Ollama). So switching provider = changing base_url,
api_key_env and model in config.toml [llm]; this code stays the same.

A chat request is a list of messages, each with a role:
    system    - standing instructions ("you are a robot, answer in 1-3 spoken sentences")
    user      - what the person said
    assistant - what the model answered before
The model has no memory between requests. "Conversation history" = we resend the earlier turns
of this session every time.
"""

import argparse
import json
import os
import re
import time
from pathlib import Path

from openai import OpenAI

from speech.config import latest_turn, load_config

SENTENCE_END = re.compile(r"[.!?](\s|$)")


class ThinkFilter:
    """Drop <think>...</think> blocks from streamed text. qwen3.8-27b sometimes starts its reply
    with an (empty) "thinking" block, which the voice would read out. Pieces can split a tag
    ("<thi" + "nk>"), so a possible partial tag at the end is held back until the next piece."""

    OPEN, CLOSE = "<think>", "</think>"

    def __init__(self):
        self.buffer, self.inside = "", False

    def feed(self, piece: str) -> str:
        self.buffer += piece
        out = ""
        while True:
            if self.inside:
                i = self.buffer.find(self.CLOSE)
                if i < 0:
                    self.buffer = self.buffer[-(len(self.CLOSE) - 1):]
                    return out
                self.buffer, self.inside = self.buffer[i + len(self.CLOSE):], False
                continue
            i = self.buffer.find(self.OPEN)
            if i >= 0:
                out += self.buffer[:i]
                self.buffer, self.inside = self.buffer[i + len(self.OPEN):], True
                continue
            hold = max((k for k in range(1, len(self.OPEN)) if self.buffer.endswith(self.OPEN[:k])),
                       default=0)
            out += self.buffer[:len(self.buffer) - hold]
            self.buffer = self.buffer[len(self.buffer) - hold:]
            return out

    def flush(self) -> str:
        out = "" if self.inside else self.buffer
        self.buffer = ""
        return out


class ChatModel:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.client = OpenAI(base_url=cfg["base_url"], api_key=os.environ[cfg["api_key_env"]])

    def build_messages(self, history: list[dict], user_text: str) -> list[dict]:
        return ([{"role": "system", "content": self.cfg["system_prompt"]}]
                + history + [{"role": "user", "content": user_text}])

    NUDGE = {"role": "system", "content": "Always say something short out loud in reply, "
                                          "even just a brief reaction. Never stay silent."}
    FALLBACK_TEXT = "Mm-hm."  # said if the model stays silent twice

    def reply(self, messages: list[dict], on_text=None, _start: float | None = None) -> dict:
        """Send messages, stream the answer back piece by piece, return text + timing.

        Streaming = the server sends the answer a few words at a time as it writes it, instead of
        all at once at the end. "First token" is when the first piece arrives; that number matters
        most for a talking robot, because speech can start then (step 4 of the plan).
        on_text(piece) is called for each piece (here: to print it as it arrives).
        """
        extra = {}
        if "reasoning_effort" in self.cfg:
            extra["reasoning_effort"] = self.cfg["reasoning_effort"]
        if "max_tokens" in self.cfg:  # without it Groq assumes a long reply and can refuse on the free tier
            extra["max_tokens"] = int(self.cfg["max_tokens"])

        start = _start if _start is not None else time.monotonic()  # a retry keeps the first start
        first_token_seconds = first_sentence_seconds = None
        pieces, usage = [], None
        thinking = ThinkFilter()
        stream = self.client.chat.completions.create(
            model=self.cfg["model"], messages=messages, stream=True,
            stream_options={"include_usage": True}, **extra)
        for chunk in stream:
            if chunk.usage:  # the last chunk carries the token counts
                usage = chunk.usage.model_dump()
            if chunk.choices and chunk.choices[0].delta.content:
                piece = thinking.feed(chunk.choices[0].delta.content)
                if not pieces and not piece.strip():
                    continue  # nothing speakable yet (thinking block, leading newlines)
                if first_token_seconds is None:
                    first_token_seconds = time.monotonic() - start
                pieces.append(piece)
                if first_sentence_seconds is None and SENTENCE_END.search("".join(pieces)):
                    first_sentence_seconds = time.monotonic() - start
                if on_text:
                    on_text(piece)
        tail = thinking.flush()
        if tail and (pieces or tail.strip()):
            pieces.append(tail)
            if on_text:
                on_text(tail)

        if not "".join(pieces).strip() and _start is not None:
            # Silent twice: say a short acknowledgement rather than nothing.
            if on_text:
                on_text(self.FALLBACK_TEXT)
            pieces = [self.FALLBACK_TEXT]
            first_token_seconds = first_sentence_seconds = time.monotonic() - start
        if not "".join(pieces).strip() and _start is None:
            # Seen 2026-11-11 with qwen3.8-27b: after a statement that needs no answer, it sometimes
            # ends its reply at once (1 token, no text) and the robot just stays silent. Ask once
            # more with a nudge; timings then count from the first attempt.
            retry = self.reply(messages + [self.NUDGE], on_text, _start=start)
            return {**retry, "retried_empty": True}

        return {
            "text": "".join(pieces).strip(),
            "first_token_seconds": round(first_token_seconds or 0.0, 3),
            # when the first full sentence had arrived (streamed speech could start then)
            "first_sentence_seconds": round(first_sentence_seconds or time.monotonic() - start, 3),
            "total_seconds": round(time.monotonic() - start, 3),
            "usage": usage,  # tokens = word pieces; providers limit and bill by tokens
            "provider": self.cfg["provider"],
            "model": self.cfg["model"],
        }


def session_history(turn: Path) -> list[dict]:
    """Earlier turns of the same session, as user/assistant messages."""
    history = []
    for earlier in sorted(turn.parent.glob("turn_*")):
        if earlier.name >= turn.name:
            break
        transcript, reply = earlier / "transcript.json", earlier / "reply.json"
        if transcript.exists() and reply.exists() and json.loads(reply.read_text())["text"]:
            # (empty replies are left out: they teach the model that silence is an answer)
            history.append({"role": "user", "content": json.loads(transcript.read_text())["text"]})
            history.append({"role": "assistant", "content": json.loads(reply.read_text())["text"]})
    return history


def main() -> None:
    parser = argparse.ArgumentParser(description="Reply to a turn's transcript.json; save reply.json.")
    parser.add_argument("turn", nargs="?", type=Path, help="turn folder (default: most recent)")
    args = parser.parse_args()
    turn = args.turn or latest_turn()

    transcript = turn / "transcript.json"
    if not transcript.exists():
        raise SystemExit(f"No {transcript}. Run speech-to-text first: uv run python -m speech.stt")
    user_text = json.loads(transcript.read_text())["text"]

    model = ChatModel(load_config()["llm"])
    messages = model.build_messages(session_history(turn), user_text)
    # request.json = exactly what was sent, so you can see (and later replay) the full prompt.
    (turn / "request.json").write_text(json.dumps(
        {"model": model.cfg["model"], "messages": messages}, indent=2, ensure_ascii=False))

    print(f'you: "{user_text}"')
    print("robot: ", end="", flush=True)
    result = model.reply(messages, on_text=lambda piece: print(piece, end="", flush=True))
    print()

    (turn / "reply.json").write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"first words after {result['first_token_seconds']:.2f} s, "
          f"full reply after {result['total_seconds']:.2f} s ({result['model']} on {result['provider']})")
    print(f"saved {turn / 'request.json'} and {turn / 'reply.json'}")


if __name__ == "__main__":
    main()
