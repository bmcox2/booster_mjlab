# Onboard Conversation: Plan

Written 2026-11-13, made step-by-step the same day. Target: **a full spoken conversation on the real K1, Thursday
2026-11-19**, with the robot's own mics and speaker and live gestures. Roadmap step 6 (`roadmap.md`), pulled forward.

**Decision (Boston, 2026-11-13): everything runs on the robot.** The laptop is only for SSH, testing and rehearsal.
No laptop-to-robot frame streaming, no laptop speaker. Hiccups get fixed on the robot. This is also the simplest clock
story: the laptop design already assumes one machine (speech loop and `gesture live` share `time.monotonic()`), and
the robot is that machine.

**Done when:** a 5-minute conversation on the floor with the robot's own mics and speaker, gestures in sync, no fall,
no manual restarts.

## Architecture on the K1

```
K1 mic array ─► speech loop (P3) ─► Groq Whisper ─► LLM (step 0) ─► cloud TTS ─► K1 speaker (USB card 0)
(iFlytek, card 1)    │  /begin /piece /end  (localhost HTTP, play times in time.monotonic)
                     ▼
              gesture live --robot (P2): library + MotionStream ─► 50 Hz reference frames in /dev/shm
                                                                          ▼
              deploy.py --task k1_gesture_live (P1, ROS 2, system Python): policy y1r48dhc ─► /joint_ctrl
```

Three processes, not one:
- **GIL** (Python runs one thread at a time): P2 plans in ~100 ms bursts. In the control process that would stall
  the 50 Hz loop.
- **Python versions:** P1 is the robot's system Python with ROS 2 (`rclpy`, `booster_interface`); P2 and P3 are our
  uv venvs (3.12). Shared memory of plain numpy arrays works across both.
- **Failure isolation:** a crash in speech must not stop the body.

| Failure | Behaviour |
|---|---|
| Speech loop dies or the network drops | P2 keeps streaming idle; the robot stands and idles |
| P2 dies / frames older than ~0.2 s | P1 holds the last frame, then eases to the standing pose |
| Ctrl-C on P1 | Hands over to Walking (Booster's balance controller), as on 2026-11-12 |
| Trunk > 60° from reference | Safety stop, damping (limp): gantry or harness first |

## What we know (2026-11-13)

- **Tracker on hardware:** 4 floor runs on 2026-11-12, no falls, handover to Walking each time (`booster_deploy`
  commit `2ed4b62`).
- **Robot software:** `booster_deploy` talks ROS 2 (`/low_state`, `/joint_ctrl`) from the system Python (has torch +
  onnxruntime). Compute: Jetson Orin NX (8 or 16 GB: datasheets disagree, check `free -h`).
- **Speaker:** C-Media USB adapter, ALSA card 0 (`aplay -D plughw:0,0`), loud at 100% (`amixer -c 0 set PCM 60%`).
  `aplay`'s default is the Jetson's silent internal audio. The speech loop finds devices by name (`find_device`).
- **Mics:** **iFlytek XFM-DP-V0.0.18 USB board, ALSA card 1** (`arecord -D plughw:1,0 -r 16000 -c 1` works; PulseAudio
  shows a mono 16 kHz source). It dropped off USB while the robot was moved and needed a reboot: check
  `cat /proc/asound/cards` before each test.
- **Internet:** yes, IllinoisNet (2026-11-12, `10.193.195.162`; JoinNow renewal due 2026-12-18).
- **Robot interfaces** (2026-11-12): `enP9p1s0` 192.168.10.102, `enP8p1s0` 192.168.13.101, `usb_eth0` 192.168.127.101.
- **Booster audio:** `ensure-booster-alsa-config` manages `/etc/asound.conf` (choose devices by name, don't edit it).
  Their `booster-audio` already publishes mic audio (`/booster/audio/capture/slot_1..8`) and has a wake-word / DOA
  library.
- **Booster SDK audio API** (`booster_robotics_sdk_python` 1.6.3 on PyPI, aarch64 wheels; example
  `python_example/sdk_pybind_audio_example.py`): `AudioCaptureStream` (`raw` 16 kHz 3-channel, and an echo-cancelled
  `naec` stream, "may return kAudioErrNotSupported"), `AudioPlayer` (PCM stream), `AudioLocalizer.GetDoaAngle()`,
  `AiClient.StartAiChat` / `StopAiChat` (Booster's own assistant). Needs `ChannelFactory.Instance().Init(0, <if>)`.
  **Only needed if plain ALSA fails or for echo cancellation later.**
- **Mic echo:** the loop is half-duplex already (`speech/src/speech/vad.py` pauses the mic during playback and skips
  `echo_tail_ms` after it).

## Steps

Who: **[me]** = Claude builds it, **[you]** = needs you (accounts, robot, judging), **[robot]** = needs robot time.
Each step has a check; don't start the next step of the same track until the check passes.

### Step 0. Choose the LLM (Sat 11-14)

Goal: the smartest model whose replies still start fast enough to talk. Today: `gpt-oss-120b` on Groq, first token
0.35 s median, response 1.47–1.59 s.

Shortlist (all streamed, short spoken replies; details in "LLM choice" below):

| Candidate | How it's run | Est. cost per 10-turn chat |
|---|---|---|
| `openai/gpt-oss-120b` (Groq, today) | reasoning low | ~free (free tier) |
| Claude Haiku 5.5 `claude-haiku-5-5` | thinking off, effort low | < $0.01 |
| Claude Sonnet 5.5 `claude-sonnet-5-5` | thinking off (`between_tools`), effort low | ~$0.04 |
| Claude Opus 5.5 `claude-opus-5-5` | thinking can't be turned off; effort low | ~$0.08 |
| Claude Fable 5.2 `claude-fable-5-2` (ceiling check only) | thinking always on; effort low | ~$0.15 |

Costs: ~1.5k input tokens per turn (system prompt + history) and ~50–150 output tokens, at list prices; estimates,
the bench measures them.

1. **[you]** Make an Anthropic API key: console.anthropic.com → sign in → **Settings → API Keys → Create Key**. Under
   **Settings → Limits**, set a monthly spend limit (e.g. $10). Add `ANTHROPIC_API_KEY=...` to `speech/.env`.
2. **[me]** `ClaudeModel` in `speech/src/speech/llm.py` (official `anthropic` SDK, streaming), chosen with
   `[llm] provider = "anthropic"`. Same `reply()` output as `ChatModel`, so streaming, gestures and logs don't change.
3. **[me]** `speech/bench/llm_compare.py`: replays the 90 recorded turns (6 sessions, 2026-11-11/12) plus ~15 harder
   prompts (explain something, follow-up that needs earlier turns, opinion, a fact) through each candidate. Measures
   first token, **first speakable piece** (what the chunker can send to TTS), total time, words, cut-offs, cost.
4. **[you]** Blind test, like the voice test: pairs of replies to the same turn, models hidden, pick the better one
   (~20 pairs).
5. **[me + you]** Pick: the model you prefer whose first speakable piece is ≤ ~0.6 s median (≤ ~1.0 s p90). Log it.
   - **Check:** `[llm]` in `speech/config.toml` set; one live test (`tools/live_test.sh`) with response time noted.
6. **[you]** TTS: no Kokoro onboard, so the cloud voice must not run out. Upgrade Groq to the Dev tier (Orpheus
   ~$0.02 per conversation) or pick Cartesia. Decide by Sunday.

### Step 1. Robot runtime, built on the laptop (Sat 11-14 – Mon 11-16)

1. **[me]** `src/booster_mjlab/gesture/shm.py`: the shared-memory reference. A ring of ~5 s of 50 Hz frames (22 joint
   positions, 22 velocities, trunk quaternion, the frame's `time.monotonic()`), a write counter, and a reader that
   returns the frame for "now". numpy only, so the robot's system Python can import it.
   - **Check:** unit test: writer in one process, reader in another, frames match, stale detection works.
2. **[me]** `gesture live --robot`: same planner and `/begin /piece /end` events, no MuJoCo policy and no window;
   writes the timeline into shared memory. Window mode stays for sim tests.
   - **Check:** `--replay-session` of a recorded session writes frames with no gaps for its whole length.
3. **[me]** `booster_deploy` task **`k1_gesture_live`** (copy of `k1_gesture_tracking`): reads the frame for "now";
   lead-in from home as today; stale-frame rule (hold, then ease to standing); same X / A / Ctrl-C, run logs and
   `check_run.py`.
   - **Check:** `fake_robot.py` + `gesture live --robot --replay-session`: 0 falls, `check_run.py` clean, killing P2
     mid-run makes the robot hold and settle.
4. **[me]** Speech robot profile: `speech/config.robot.toml` (input device "XFM", output "USB Audio" or whatever the
   names turn out to be), and a slim install: Silero VAD through onnxruntime (no torch), faster-whisper and Kokoro
   moved to an optional group.
   - **Check:** a fresh `uv sync` without the optional group runs the loop on the laptop.
5. **[me]** Full rehearsal on the laptop with the robot's exact layout: mic → speech → `gesture live --robot` →
   `fake_robot.py` running `deploy.py --task k1_gesture_live`. Standard live test, then 10 minutes; kill each process
   once.
   - **Check:** all pieces on time, 0 falls, the failure table holds.
6. **[me]** `tools/robot_install.sh` (copies the gesture runtime, `speech/`, the library (220 MB) and the policy to
   `~/gesture_conv/` on the robot, runs `uv sync`; API keys copied separately) and `tools/robot_conversation.sh`
   (starts P1–P3 in `tmux` panes, prints which pane is which).
   - **Check:** both run against the laptop itself as a dry target.

### Step 2. Context gestures in sim (Mon 11-16 – Wed 11-18, after step 1.5)

Design: `gesture_plan.md` step 8. Ships to the robot as library units and prompt changes; nothing robot-side.

1. **[me]** Tag format: the LLM may add `[emph]...[/emph]`, `[wave]`, `[point_you]`, `[point_self]` inline. The speech
   loop strips tags before TTS, maps each to its word's time, and sends them with the `/piece` event.
   - **Check:** 20 replayed turns: tags never spoken, every tag lands on a word time.
2. **[me]** Emphasis: the generator raises the intensity target on the tagged words and prefers a stroke on their
   strongest accent.
3. **[me]** Units: `wave_000508` / `wave_001104` as named units; search the library for pointing at the listener
   (arm reaching forward) and at self (hand to chest). If none are good: **[you]** film 3–4 takes on a phone →
   GVHMR → GMR.
   - **Check:** every named unit 0 falls in `sim2sim` with pushes + 40 ms delay.
4. **[me]** Rate rules in the generator: ≤ 1 named gesture per sentence, cooldown ~10 s per gesture, emphasis ≤ 1 per
   reply. A tag that breaks a rule is dropped (beats continue).
5. **[you]** Watch 3 dubbed videos of the same session: no tags / sparse / dense. Pick the rate.
   - **Check:** live test in the sim window with tags on; nothing spoken wrong, no falls.

### Step 3. First robot access (any time before Thursday, ~1 h) [you] [robot]

1. `cat /proc/asound/cards`: the iFlytek mic (card 1) and C-Media speaker (card 0) are both there.
2. **[me writes, you run]** `tools/robot_probe.sh`: `curl` timing from the robot to Groq / Anthropic / the TTS API,
   `uv` present, disk, `free -h`, `nproc`, who holds the sound cards (`fuser -v /dev/snd/*`), the device names Python
   sees, 5 s recordings (quiet; while the speaker plays a sentence = echo level). Copies the WAVs back.
3. `tools/robot_install.sh` to the robot.
4. Speech loop alone, the robot standing in Booster's controller (no gestures): 5 turns.
   - **Check:** it hears you from ~1 m, never answers itself, replies come out of the K1.
5. If there's time: P1 + P2 with a replayed session (no mic) on the gantry.

### Step 4. Wednesday 11-18: final rehearsal at home

1. **[me]** Laptop rehearsal (step 1.5) with everything in: chosen LLM, voice, context gestures.
2. **[me]** Session card `notes/robot_session_2026-11-19.md`: every command in order, stop rules.
3. **[you]** Charge the robot; check the IllinoisNet login still works; someone booked for the e-stop.

### Step 5. Thursday 11-19 at the robot

1. `cat /proc/asound/cards`, then `tools/robot_probe.sh` (2 min).
2. `tools/robot_install.sh` if anything changed since Wednesday.
3. One canned clip (`k1_gesture_tracking`): confirms nothing else changed.
4. Speech loop alone, standing in Booster's controller: 3 turns.
5. Full conversation (`tools/robot_conversation.sh`) **on the gantry**, 2 minutes.
6. **Floor**, slack harness, someone on the e-stop: 5 minutes, then 10.
7. Record: phone video, `logs/run_*.npz`, `speech/runs/<session>/`, P2's frame log. Copy back, `/log-session`.

## Day by day

| Day | Track A: runtime (step 1) | Track B: conversation quality |
|---|---|---|
| Sat 11-14 | 1.1–1.3 shared memory, `--robot`, `k1_gesture_live` | Step 0: key, Claude backend, bench, blind test |
| Sun 11-15 | 1.4–1.6 slim speech, laptop rehearsal, install scripts | Step 0 decision; TTS decision |
| Mon 11-16 | Step 3 if the robot is free | 2.1–2.2 tags, emphasis |
| Tue 11-17 | fixes from step 3 | 2.3–2.4 units, rate rules |
| Wed 11-18 | Step 4 rehearsal + session card | 2.5 rate pick |
| Thu 11-19 | **Step 5 at the robot** | |

If something slips, cut from track B first (the vocabulary, then emphasis); the runtime is what makes Thursday work.

## LLM choice (notes for step 0)

- **What matters for talking:** time to the first *speakable piece*, not total time; the chunker sends the first
  ≥ 2 words up to a comma or period to TTS. Voice-agent guides put the LLM's first token at ~0.5 s or less (Pipecat:
  much above 0.7 s feels slow). Our whole response is 1.5 s median now; the LLM is ~0.35 s of it.
- **Thinking costs time.** The smart models think before answering. Haiku 5.5 and Sonnet 5.5 can turn thinking off;
  Opus 5.5 and Fable 5.2 can't (only lower effort), so they will start later. The bench measures by how much.
- **Later steps want tool calls** (look_at, wave, point; roadmap step 7): Claude models are strong at them, gpt-oss is
  usable. That's a second reason to compare now.
- **Code:** the loop's `ChatModel` speaks the OpenAI-compatible format (Groq). Claude gets its own `ClaudeModel` with
  Anthropic's SDK; `provider` in `[llm]` picks one. Groq stays as the fallback if the Anthropic call fails.
- **Keys on the robot:** a separate key per service with a spend limit, revoked after the semester or if the robot
  changes hands.

## Fallbacks (only if a step fails on the robot)

- Mic drops off USB: reboot (seen 2026-11-12); if it keeps happening, a USB conference mic.
- Mic held by `booster-audio`: read their topic `/booster/audio/capture/slot_N`, or the SDK's `AudioCaptureStream`.
- Robot hears itself: raise `echo_tail_ms`; then the SDK's echo-cancelled `naec` stream.
- IllinoisNet fails: phone hotspot.
- Orin CPU too busy: the planner's chunk sizes and onnxruntime threads are the knobs; measure first.
- Chosen LLM slow on the robot's network: switch `[llm]` back to Groq (one line).
