"""Step 4: streaming. Start speaking the first words while the rest of the reply is still being
written (LLM) and voiced (TTS).

Three parts run at the same time:
    LLM stream  (main thread)   reply text arrives a few words at a time -> Chunker
    Chunker                     cuts the text into speakable pieces ("chunks") at commas and
                                sentence ends, once a piece has enough words
    TTS worker  (second thread) voices chunk 1, then chunk 2, ... and hands each to the Player
    Player      (audio thread)  one speaker stream that plays chunks back to back

The catch: chunk 2 must be voiced before chunk 1 finishes playing, or there is a silent gap
(an "underrun": the speaker ran out of audio). Kokoro on this CPU needs ~0.3 s + ~0.4 s per second
of speech, so very short first chunks ("Sure!") cause gaps; hence the minimum word counts.

Every chunk's text, position in the reply audio, and the moment it actually started playing are
saved in tts.json. Gestures will later be scheduled on those same times (speech_plan step 7).
"""

import collections
import queue
import re
import threading
import time

import numpy as np
import sounddevice as sd

# A place where speech can pause: sentence end or comma/semicolon/colon, followed by a space.
# (Requiring the space means "3.5" or "e.g.x" never split, and we wait for the next token.)
BOUNDARY = re.compile(r"[.!?,;:](?=\s)")


class Chunker:
    """Feed it text as it arrives; it returns pieces that are ready to be voiced."""

    def __init__(self, first_min_words: int, min_words: int, max_words: int):
        self.first_min_words, self.min_words, self.max_words = first_min_words, min_words, max_words
        self.buffer = ""
        self.count = 0  # chunks emitted so far

    def _min(self) -> int:
        return self.first_min_words if self.count == 0 else self.min_words

    def feed(self, piece: str) -> list[str]:
        self.buffer += piece
        out = []
        while True:
            cut = None
            for m in BOUNDARY.finditer(self.buffer):
                if len(self.buffer[:m.end()].split()) >= self._min():
                    cut = m.end()
                    break
            if cut is None and len(self.buffer.split()) > self.max_words:
                # No pause point in a long stretch: cut before the last (maybe unfinished) word.
                cut = self.buffer.rstrip().rfind(" ")
            if not cut or cut <= 0:
                return out
            chunk, self.buffer = self.buffer[:cut].strip(), self.buffer[cut:]
            if chunk:
                out.append(chunk)
                self.count += 1

    def flush(self) -> list[str]:
        """The reply is complete: whatever is left is the last chunk."""
        rest, self.buffer = self.buffer.strip(), ""
        if rest:
            self.count += 1
            return [rest]
        return []


class Player:
    """One output stream for the whole session. Chunks added with add() play back to back.

    The audio callback runs on the sound card's thread every few ms: it copies samples, notes
    when each chunk started, and counts silence while waiting for a chunk that isn't ready.
    """

    def __init__(self, device: int, sample_rate: int, block: int = 480):  # 480 = 20 ms at 24 kHz
        self.sample_rate = sample_rate
        self.chunks: collections.deque = collections.deque()
        self.done = threading.Event()
        self.begin()
        self.stream = sd.OutputStream(samplerate=sample_rate, channels=1, dtype="float32",
                                      blocksize=block, device=device, callback=self._callback)
        self.stream.start()
        self.latency = float(self.stream.latency)  # buffer -> speaker, seconds

    def begin(self) -> None:
        """Reset for a new reply."""
        self.chunks.clear()
        self.current, self.pos, self.index = None, 0, -1
        self.started_at = {}     # chunk index -> monotonic time its first sample was handed out
        self.ended_at = None
        self.underrun_s = 0.0    # silence in the middle of the reply (chunk not ready in time)
        self.finished = False    # no more chunks will come
        self.done.clear()

    def add(self, audio: np.ndarray, index: int) -> None:
        self.chunks.append((index, audio))

    def finish(self) -> None:
        self.finished = True
        if not self.started_at and not self.chunks:  # nothing was ever added
            self.done.set()

    def wait(self) -> None:
        self.done.wait()

    def _callback(self, outdata, frames, time_info, status):
        out = outdata[:, 0]
        filled = 0
        now = time.monotonic()
        while filled < frames:
            if self.current is None:
                if not self.chunks:
                    break
                self.index, self.current = self.chunks.popleft()
                self.pos = 0
                self.started_at[self.index] = now + filled / self.sample_rate
            n = min(frames - filled, len(self.current) - self.pos)
            out[filled:filled + n] = self.current[self.pos:self.pos + n]
            filled += n
            self.pos += n
            if self.pos >= len(self.current):
                self.current = None
        out[filled:] = 0.0
        if filled < frames and self.started_at and not self.done.is_set():
            if self.finished and not self.chunks and self.current is None:
                self.ended_at = now + filled / self.sample_rate
                self.done.set()
            else:
                self.underrun_s += (frames - filled) / self.sample_rate

    def close(self) -> None:
        self.stream.stop()
        self.stream.close()


def trim_silence(audio: np.ndarray, sample_rate: int, threshold: float = 0.01,
                 keep_before: float = 0.02, keep_after: float = 0.04) -> tuple[np.ndarray, float]:
    """Kokoro pads every piece with ~0.25 s of silence before and ~0.45 s after the voice, so two
    pieces back to back had a 0.7 s pause. Cut that padding (we add natural pauses ourselves).
    Returns (trimmed audio, seconds removed from the start)."""
    frame = int(0.01 * sample_rate)  # 10 ms
    n = len(audio) // frame
    if n == 0:
        return audio, 0.0
    loudness = np.sqrt(np.mean(audio[:n * frame].reshape(n, frame) ** 2, axis=1))
    voiced = np.nonzero(loudness > threshold)[0]
    if len(voiced) == 0:
        return audio, 0.0
    start = max(0, voiced[0] * frame - int(keep_before * sample_rate))
    end = min(len(audio), (voiced[-1] + 1) * frame + int(keep_after * sample_rate))
    return audio[start:end], start / sample_rate


def pause_after(text: str, cfg: dict) -> float:
    """How long to pause after a piece, from how it ends (like a person breathing)."""
    end = text.rstrip()[-1:]
    if end in ".!?":
        return cfg.get("sentence_pause_ms", 300) / 1000
    if end in ",;:":
        return cfg.get("clause_pause_ms", 150) / 1000
    return 0.05


def simulate_playback(ready: list[float], durations: list[float]) -> tuple[list[float], float]:
    """Without a speaker (test-set replay): when would each chunk start, and how much silence
    would there be between chunks? ready = time each chunk's audio was ready."""
    starts, end, gaps = [], None, 0.0
    for r, d in zip(ready, durations):
        start = r if end is None else max(end, r)
        if end is not None:
            gaps += start - end
        starts.append(start)
        end = start + d
    return starts, gaps


def stream_reply(llm, tts, messages: list[dict], timer, chunk_cfg: dict, player: Player | None,
                 sample_rate: int, print_text: bool = True, on_event=None) -> tuple[dict, np.ndarray, dict]:
    """Stream one reply: LLM -> chunks -> TTS worker -> player. Returns (reply, audio, tts_info).

    Marks on `timer`: llm_first_chunk, tts_first_audio, tts_done, and (with a player)
    playback_start, playback_end.

    on_event(kind, data): told as things happen, for live gestures (speech/gesture.py). Times are
    time.monotonic() at the speaker (buffer time + output latency).
        "begin": the first piece's text exists (not voiced yet)
        "piece": a piece was voiced and queued; "play_time" = when it will start playing
        "end":   the reply finished; "played" = when each piece really started
    """
    chunk_queue: queue.Queue = queue.Queue()
    chunks: list[dict] = []
    errors: list[BaseException] = []
    latency = player.latency if player is not None else 0.0

    def emit(kind: str, data: dict) -> None:
        if on_event is not None and player is not None:  # live gestures need real playback times
            try:
                on_event(kind, data)
            except Exception:  # gestures must never break the conversation
                pass

    def tts_worker():
        try:
            position = 0  # samples into the whole reply
            free_at = 0.0  # when the speaker finishes the pieces queued so far
            while (item := chunk_queue.get()) is not None:
                index, text = item
                audio, info = tts.synthesize(text)
                audio, trimmed = trim_silence(audio, sample_rate)
                # The natural pause goes at the END of this piece: it plays while the next piece
                # is still being voiced, which hides that wait (at the start of the next piece it
                # would only play after the wait, making the pause longer).
                pause = pause_after(text, chunk_cfg)
                audio = np.concatenate([audio, np.zeros(int(pause * sample_rate), np.float32)])
                info = {**info, "words": [{**w, "start": round(max(0.0, w["start"] - trimmed), 3),
                                           "end": round(max(0.0, w["end"] - trimmed), 3)}
                                          for w in info["words"]],
                        "trimmed_s": round(trimmed, 3), "pause_s": pause}
                ready = time.monotonic()
                if index == 0:
                    timer.mark("tts_first_audio", ready)
                chunks.append({"index": index, "text": text, "audio": audio, "info": info,
                               "ready": ready, "start_sample": position})
                position += len(audio)
                if player is not None:
                    player.add(audio, index)
                    # Pieces play back to back, so this one starts when the previous ends (or now).
                    play_time = max(ready, free_at)
                    free_at = play_time + len(audio) / sample_rate
                    emit("piece", {"index": index, "text": text, "audio": audio, "sample_rate": sample_rate,
                                   "words": info["words"], "play_time": play_time + latency})
            timer.mark("tts_done")
        except BaseException as e:  # surface errors from the thread instead of hanging
            errors.append(e)

    worker = threading.Thread(target=tts_worker, daemon=True)
    worker.start()
    if player is not None:
        player.begin()

    chunker = Chunker(chunk_cfg["first_min_words"], chunk_cfg["min_words"], chunk_cfg["max_words"])
    sent = 0

    def send(text_chunks):
        nonlocal sent
        for text in text_chunks:
            if sent == 0:
                timer.mark("llm_first_chunk")
                emit("begin", {"text": text, "t": time.monotonic()})
            chunk_queue.put((sent, text))
            sent += 1

    # With a speaker, each piece is printed when it starts playing (like live captions);
    # without one (test-set replay), the text is printed as the LLM writes it.
    captions = print_text and player is not None
    if print_text:
        print("robot: ", end="", flush=True)

    def on_text(piece):
        if print_text and not captions:
            print(piece, end="", flush=True)
        send(chunker.feed(piece))

    llm_start = time.monotonic()
    reply = llm.reply(messages, on_text=on_text)
    if print_text and not captions:
        print()
    send(chunker.flush())
    chunk_queue.put(None)
    timer.mark("llm_first_token", llm_start + reply["first_token_seconds"])
    timer.mark("llm_first_sentence", llm_start + reply["first_sentence_seconds"])
    timer.mark("llm_done", llm_start + reply["total_seconds"])

    if captions:  # print pieces as they start playing
        printed, deadline = 0, None
        while not errors:
            if printed < len(chunks) and printed in player.started_at:
                print(next(c["text"] for c in chunks if c["index"] == printed), end=" ", flush=True)
                printed += 1
                continue
            if not worker.is_alive():
                if printed >= len(chunks):
                    break
                if deadline is None:  # all voiced; give playback its length + 2 s, never hang
                    deadline = time.monotonic() + sum(len(c["audio"]) for c in chunks) / sample_rate + 2
                elif time.monotonic() > deadline:
                    break
            time.sleep(0.01)
    worker.join()
    if errors:
        raise errors[0]
    if player is not None:
        player.finish()
        player.wait()
    if captions:
        print()

    # Put it together: the whole reply audio, plus where each chunk sits and when it played.
    audio = (np.concatenate([c["audio"] for c in chunks]) if chunks
             else np.zeros(0, dtype=np.float32))
    durations = [len(c["audio"]) / sample_rate for c in chunks]
    if player is not None and player.started_at:
        starts = [player.started_at.get(c["index"]) for c in chunks]
        gaps, measured = player.underrun_s, True
        emit("end", {"played": [None if s is None else s + latency for s in starts]})
        timer.mark("playback_start", starts[0])
        timer.mark("playback_end", player.ended_at or time.monotonic())
        timer.extra["output_latency_s"] = round(player.latency, 4)
    else:
        starts, gaps = simulate_playback([c["ready"] for c in chunks], durations)
        measured = False
    timer.extra.update(chunks=len(chunks), gaps_s=round(gaps, 3), gaps_measured=measured)

    words = []
    for c in chunks:
        offset = c["start_sample"] / sample_rate
        words += [{**w, "start": round(w["start"] + offset, 3), "end": round(w["end"] + offset, 3)}
                  for w in c["info"]["words"]]
    tts_info = {
        "text": reply["text"], "voice": chunks[0]["info"]["voice"] if chunks else None,
        "sample_rate": sample_rate, "audio_seconds": round(len(audio) / sample_rate, 3),
        "streamed": True, "gaps_s": round(gaps, 3), "gaps_measured": measured,
        "chunks": [{"index": c["index"], "text": c["text"], "start_sample": c["start_sample"],
                    "audio_seconds": round(d, 3),
                    "synthesize_seconds": c["info"]["synthesize_seconds"],
                    "ready_s": round(c["ready"] - timer.t0, 3),
                    "played_s": round(s - timer.t0, 3) if s is not None else None}
                   for c, d, s in zip(chunks, durations, starts)],
        "words": words,
    }
    return reply, audio, tts_info
