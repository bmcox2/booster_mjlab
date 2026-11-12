"""Stage 4 of the speech loop: text-to-speech (TTS). reply.json -> reply.wav + tts.json

Run it (from the speech/ folder):
    uv run python -m speech.tts                         # speak the most recent reply
    uv run python -m speech.tts runs/<session>/turn_01  # a specific turn
    uv run python -m speech.tts --no-play               # only write reply.wav
    uv run python -m speech.tts --engine orpheus        # try another engine (config.toml [tts] engine)

Engines (all give 24 kHz mono audio + when each word starts and ends):
    kokoro      Kokoro-82M, a small open model on this laptop's CPU. Free, ~0.65 s for a short piece.
                Text -> phonemes (word sounds; unknown words via espeak-ng) -> audio. Gives word times.
    orpheus     Groq's hosted Orpheus (canopylabs), same key as the LLM. ~0.3 s. Free tier: 100
                requests/day, 1,200 characters/min. No word times: estimated from the audio.
    elevenlabs  ElevenLabs Flash (cloud). Needs ELEVENLABS_API_KEY in speech/.env. Gives letter times.
    cartesia    Cartesia Sonic (cloud). Needs CARTESIA_API_KEY in speech/.env. Gives word times.

Word times are what line gestures up with speech: the gesture generator cuts motion at word starts.

A cloud engine can fail (no internet, rate limit, slow). Then that piece is voiced by Kokoro
instead (`fallback = "kokoro"`), so the robot never goes silent; tts.json records which engine
spoke (`"engine"`). The voice changes for that piece, which is better than silence.
"""

import argparse
import base64
import io
import json
import os
import re
import time
import warnings
from pathlib import Path

import numpy as np

from speech.audio import describe, find_device, play, save_wav
from speech.config import latest_turn, load_config

SAMPLE_RATE = 24000  # every engine is asked for 24 kHz, so the speaker stream never changes rate
KOKORO_SAMPLE_RATE = SAMPLE_RATE  # old name, still imported in places


class KokoroEngine:
    name = "kokoro"

    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.pipelines = {}  # one per accent, all sharing the same loaded model
        self._pipeline(cfg["voice"])

    def _pipeline(self, voice: str):
        """Kokoro voice names start with an accent letter: am_michael = American male,
        bm_george = British male. The accent decides how words are pronounced, so each accent
        gets its own pipeline (cheap: they share the one 82M-number model)."""
        lang = voice[0]
        if lang not in self.pipelines:
            with warnings.catch_warnings():  # Kokoro's libraries print harmless warnings on import
                warnings.simplefilter("ignore")
                from kokoro import KPipeline
                shared = next(iter(self.pipelines.values())).model if self.pipelines else True
                self.pipelines[lang] = KPipeline(lang_code=lang, repo_id="hexgrad/Kokoro-82M",
                                                 model=shared, device=self.cfg.get("device", "cpu"))
        return self.pipelines[lang]

    def synthesize(self, text: str, voice: str | None = None) -> tuple[np.ndarray, dict]:
        voice = voice or self.cfg["voice"]
        if "cpu_threads" in self.cfg:
            import torch
            # How many CPU threads the model math uses. Set right before every use, because other
            # libraries change it when they load (Kokoro's resets it to 14, Silero VAD's sets 1).
            # More is not faster on this laptop: its CPU mixes fast and slow cores; 4 was best.
            torch.set_num_threads(self.cfg["cpu_threads"])
        # Kokoro splits long text into chunks and yields one result per chunk. Word times inside a
        # result count from that chunk's start, so we add the length of the audio before it.
        chunks, words, offset = [], [], 0.0
        for result in self._pipeline(voice)(text, voice=voice):
            audio = result.audio.numpy()
            for token in result.tokens or []:
                if token.start_ts is not None and token.end_ts is not None:
                    words.append({"word": token.text, "start": round(offset + token.start_ts, 3),
                                  "end": round(offset + token.end_ts, 3)})
            chunks.append(audio)
            offset += len(audio) / SAMPLE_RATE
        audio = np.concatenate(chunks) if chunks else np.zeros(0, dtype=np.float32)
        return audio, {"voice": voice, "words": words, "word_times": "kokoro"}


class CloudError(Exception):
    """A cloud TTS call failed; the caller falls back to Kokoro."""


class CloudEngine:
    """Shared parts of the cloud engines: the API key, one reused HTTP connection (saves the
    ~0.1 s connection setup on every piece), timeouts, and pausing after a rate limit."""

    def __init__(self, cfg: dict):
        import httpx
        self.cfg = cfg
        key = os.environ.get(cfg["api_key_env"])
        if not key:
            raise SystemExit(f"{self.name}: no {cfg['api_key_env']} in speech/.env (see notes/speech_bench.md)")
        self.key = key
        # connect / read timeouts: a stuck request falls back to Kokoro instead of leaving silence
        self.http = httpx.Client(timeout=httpx.Timeout(cfg.get("timeout_s", 3.0)), http2=False)
        self.blocked_until = 0.0  # after a 429 (rate limit), skip the cloud until this time

    def check(self, r) -> None:
        if r.status_code == 429:
            wait = _seconds(r.headers.get("retry-after") or r.headers.get("x-ratelimit-reset-tokens") or "10")
            self.blocked_until = time.monotonic() + wait
            r.read()
            raise CloudError(f"rate limited for {wait:.0f} s: {r.text[:300]}")
        if r.status_code >= 400:
            r.read()
            raise CloudError(f"HTTP {r.status_code}: {r.text[:200]}")

    def synthesize(self, text: str, voice: str | None = None) -> tuple[np.ndarray, dict]:
        if time.monotonic() < self.blocked_until:
            raise CloudError("still rate limited")
        import httpx
        try:
            return self._synthesize(text, voice or self.cfg["voice"])
        except httpx.HTTPError as e:
            raise CloudError(f"{type(e).__name__}: {e}") from e


def _seconds(value: str) -> float:
    """'7.66s', '14m24s', '550ms' or '12' -> seconds."""
    total = 0.0
    for num, unit in re.findall(r"([\d.]+)(ms|m|s|h)?", value):
        total += float(num) * {"ms": 0.001, "m": 60, "h": 3600}.get(unit, 1)
    return total


class OrpheusEngine(CloudEngine):
    """Groq-hosted Orpheus. Returns a WAV; no word times, so they are estimated."""
    name = "orpheus"

    def _synthesize(self, text, voice):
        t0 = time.monotonic()
        with self.http.stream("POST", "https://api.groq.com/openai/v1/audio/speech",
                              headers={"Authorization": f"Bearer {self.key}"},
                              json={"model": self.cfg["model"], "voice": voice, "input": text,
                                    "response_format": "wav"}) as r:
            self.check(r)
            body, first = b"", None
            for b in r.iter_bytes():
                first = first or time.monotonic() - t0
                body += b
        import soundfile as sf
        audio, rate = sf.read(io.BytesIO(body), dtype="float32")
        if rate != SAMPLE_RATE:
            raise CloudError(f"orpheus sent {rate} Hz")
        return audio, {"voice": voice, "first_bytes_seconds": round(first or 0, 3),
                       "words": estimate_word_times(audio, SAMPLE_RATE, text), "word_times": "estimated"}


class ElevenLabsEngine(CloudEngine):
    """ElevenLabs text-to-speech with timestamps: raw 16-bit PCM + the start/end of every letter."""
    name = "elevenlabs"

    def _synthesize(self, text, voice):
        t0 = time.monotonic()
        r = self.http.post(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps",
                           params={"output_format": "pcm_24000"},
                           headers={"xi-api-key": self.key},
                           json={"text": text, "model_id": self.cfg["model"],
                                 **({"voice_settings": self.cfg["voice_settings"]}
                                    if "voice_settings" in self.cfg else {})})
        self.check(r)
        data = r.json()
        audio = np.frombuffer(base64.b64decode(data["audio_base64"]), "<i2").astype(np.float32) / 32768
        a = data.get("alignment") or {}
        words = letters_to_words(a.get("characters", []), a.get("character_start_times_seconds", []),
                                 a.get("character_end_times_seconds", []))
        return audio, {"voice": voice, "first_bytes_seconds": round(time.monotonic() - t0, 3),
                       "words": words, "word_times": "elevenlabs"}


class CartesiaEngine(CloudEngine):
    """Cartesia Sonic over server-sent events: audio in pieces, then word times."""
    name = "cartesia"

    def _synthesize(self, text, voice):
        t0 = time.monotonic()
        body = {"model_id": self.cfg["model"], "transcript": text,
                "voice": {"mode": "id", "id": voice}, "language": "en", "add_timestamps": True,
                "output_format": {"container": "raw", "encoding": "pcm_s16le", "sample_rate": SAMPLE_RATE}}
        pcm, words, first = [], [], None
        with self.http.stream("POST", "https://api.cartesia.ai/tts/sse", json=body,
                              headers={"Authorization": f"Bearer {self.key}",
                                       "Cartesia-Version": self.cfg["api_version"]}) as r:
            self.check(r)
            for line in r.iter_lines():
                if not line.startswith("data:"):
                    continue
                event = json.loads(line[5:])
                kind = event.get("type")
                if kind == "chunk" and event.get("data"):
                    first = first or time.monotonic() - t0
                    pcm.append(base64.b64decode(event["data"]))
                elif kind == "timestamps":
                    w = event["word_timestamps"]
                    words += [{"word": t, "start": round(s, 3), "end": round(e, 3)}
                              for t, s, e in zip(w["words"], w["start"], w["end"])]
                elif kind == "error":
                    raise CloudError(f"{event.get('title')}: {event.get('message')}")
                elif kind == "done":
                    break
        audio = np.frombuffer(b"".join(pcm), "<i2").astype(np.float32) / 32768
        return audio, {"voice": voice, "first_bytes_seconds": round(first or 0, 3),
                       "words": words, "word_times": "cartesia"}


def letters_to_words(chars: list[str], starts: list[float], ends: list[float]) -> list[dict]:
    """ElevenLabs times every letter; a word runs from its first letter's start to its last's end."""
    words, cur = [], None
    for c, s, e in zip(chars, starts, ends):
        if c.isspace():
            cur = None
            continue
        if cur is None:
            cur = {"word": "", "start": round(s, 3), "end": round(e, 3)}
            words.append(cur)
        cur["word"] += c
        cur["end"] = round(e, 3)
    return words


def estimate_word_times(audio: np.ndarray, rate: int, text: str) -> list[dict]:
    """Guess when each word is spoken, for engines that don't say (Orpheus).

    Spread the words over the *voiced* part of the audio (pauses skipped), each word getting time
    in proportion to its syllable count, +1 if it ends in punctuation (speakers slow down there).
    Checked against Kokoro's real word times (bench/word_times.py, 60 live pieces): word starts
    off by 55 ms median, 160 ms p90 (spreading words evenly: 159 / 350 ms). Good enough for the
    gesture generator, which only uses word starts as places where a motion unit may begin.
    """
    words = text.split()
    frame = int(0.01 * rate)  # 10 ms
    n = len(audio) // frame
    if not words or n == 0:
        return []
    loud = np.sqrt(np.mean(audio[:n * frame].reshape(n, frame) ** 2, axis=1))
    voiced = loud > max(0.01, 0.06 * loud.max())
    # Short dips (stop consonants like the p in "stop") are still speech: fill dips < 80 ms.
    idx = np.nonzero(voiced)[0]
    if len(idx) == 0:
        return []
    for a, b in zip(idx[:-1], idx[1:]):
        if 1 < b - a <= 8:
            voiced[a:b] = True
    frames = np.nonzero(voiced)[0]  # voiced frame k -> real time frames[k] * 10 ms
    weight = np.array([max(1, len(re.findall(r"[aeiouy]+", w.lower()))) + (w[-1] in ",.;:!?")
                       for w in words], dtype=float)
    edges = np.concatenate([[0], np.cumsum(weight)]) / weight.sum() * len(frames)
    out = []
    for i, w in enumerate(words):
        a = frames[min(int(edges[i]), len(frames) - 1)]
        b = frames[max(min(int(np.ceil(edges[i + 1])) - 1, len(frames) - 1), 0)] + 1
        out.append({"word": w, "start": round(a * 0.01, 3), "end": round(max(b, a + 1) * 0.01, 3)})
    return out


ENGINES = {"kokoro": KokoroEngine, "orpheus": OrpheusEngine, "elevenlabs": ElevenLabsEngine,
           "cartesia": CartesiaEngine}


class TextToSpeech:
    """The engine chosen in config.toml ([tts] engine), with Kokoro as the fallback."""

    def __init__(self, cfg: dict, engine: str | None = None):
        start = time.monotonic()
        self.cfg = cfg
        self.engine_name = engine or cfg.get("engine", "kokoro")
        if self.engine_name == "kokoro":
            self.engine = KokoroEngine(cfg)
            self.fallback = None
        else:
            self.engine = ENGINES[self.engine_name]({**cfg.get(self.engine_name, {})})
            self.fallback = KokoroEngine(cfg) if cfg.get("fallback") == "kokoro" else None
        self.fallbacks = 0  # pieces voiced by the fallback this program run
        self.load_seconds = time.monotonic() - start

    def warm_up(self) -> None:
        """The first use of a model is slower (memory setup, caches; for the cloud: opening the
        connection). Uses one cloud request."""
        for e in (self.engine, self.fallback):
            if e is not None:
                try:
                    e.synthesize("Ready.")
                except CloudError as err:
                    print(f"[tts] {e.name} warm-up failed ({err}); pieces will use the fallback until it works")

    def synthesize(self, text: str, voice: str | None = None) -> tuple[np.ndarray, dict]:
        """Text -> (float32 samples at 24 kHz, info with word timings and timing).

        voice: override the engine's configured voice (used by the voice sampler)."""
        start = time.monotonic()
        try:
            audio, info = self.engine.synthesize(text, voice)
            engine, error = self.engine.name, None
        except CloudError as e:
            if self.fallback is None:
                raise
            self.fallbacks += 1
            print(f"\n[tts] {self.engine.name} failed ({e}); this piece uses {self.fallback.name}")
            audio, info = self.fallback.synthesize(text)
            engine, error = self.fallback.name, str(e)
        audio = np.ascontiguousarray(audio, dtype=np.float32)
        info = {"text": text, **info, "engine": engine,
                "sample_rate": SAMPLE_RATE, "audio_seconds": round(len(audio) / SAMPLE_RATE, 3),
                "synthesize_seconds": round(time.monotonic() - start, 3)}
        if error:
            info["fallback_reason"] = error
        return audio, info


def main() -> None:
    parser = argparse.ArgumentParser(description="Speak a turn's reply.json; save reply.wav + tts.json.")
    parser.add_argument("turn", nargs="?", type=Path, help="turn folder (default: most recent)")
    parser.add_argument("--no-play", action="store_true", help="only write the files")
    parser.add_argument("--engine", choices=sorted(ENGINES), help="override config.toml's [tts] engine")
    args = parser.parse_args()
    turn = args.turn or latest_turn()

    reply = turn / "reply.json"
    if not reply.exists():
        raise SystemExit(f"No {reply}. Run the LLM first: uv run python -m speech.llm")
    text = json.loads(reply.read_text())["text"]

    cfg = load_config()
    tts = TextToSpeech(cfg["tts"], args.engine)
    print(f"{tts.engine_name} loaded in {tts.load_seconds:.1f} s (only happens once per program start)")
    audio, info = tts.synthesize(text)

    save_wav(turn / "reply.wav", audio, SAMPLE_RATE)
    (turn / "tts.json").write_text(json.dumps(info, indent=2, ensure_ascii=False))
    print(f'robot says: "{text}"')
    print(f"made {info['audio_seconds']:.1f} s of speech in {info['synthesize_seconds']:.2f} s "
          f"({describe(audio, SAMPLE_RATE)})")
    print(f"saved {turn / 'reply.wav'} and {turn / 'tts.json'}")

    if not args.no_play:
        play(audio, SAMPLE_RATE, find_device(cfg["audio"]["output_device"], "output"))


if __name__ == "__main__":
    main()
