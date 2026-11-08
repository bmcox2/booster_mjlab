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
import time
from pathlib import Path

from openai import OpenAI

from speech.config import latest_turn, load_config


class ChatModel:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.client = OpenAI(base_url=cfg["base_url"], api_key=os.environ[cfg["api_key_env"]])

    def build_messages(self, history: list[dict], user_text: str) -> list[dict]:
        return ([{"role": "system", "content": self.cfg["system_prompt"]}]
                + history + [{"role": "user", "content": user_text}])

    def reply(self, messages: list[dict], on_text=None) -> dict:
        """Send messages, stream the answer back piece by piece, return text + timing.

        Streaming = the server sends the answer a few words at a time as it writes it, instead of
        all at once at the end. "First token" is when the first piece arrives; that number matters
        most for a talking robot, because speech can start then (step 4 of the plan).
        on_text(piece) is called for each piece (here: to print it as it arrives).
        """
        extra = {}
        if "reasoning_effort" in self.cfg:
            extra["reasoning_effort"] = self.cfg["reasoning_effort"]

        start = time.monotonic()
        first_token_seconds = None
        pieces, usage = [], None
        stream = self.client.chat.completions.create(
            model=self.cfg["model"], messages=messages, stream=True,
            stream_options={"include_usage": True}, **extra)
        for chunk in stream:
            if chunk.usage:  # the last chunk carries the token counts
                usage = chunk.usage.model_dump()
            if chunk.choices and chunk.choices[0].delta.content:
                piece = chunk.choices[0].delta.content
                if first_token_seconds is None:
                    first_token_seconds = time.monotonic() - start
                pieces.append(piece)
                if on_text:
                    on_text(piece)

        return {
            "text": "".join(pieces).strip(),
            "first_token_seconds": round(first_token_seconds or 0.0, 3),
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
        if transcript.exists() and reply.exists():
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
