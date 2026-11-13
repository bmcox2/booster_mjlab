# Onboard Conversation: Plan

Written 2026-11-13. Target: **a full spoken conversation on the real K1, Thursday 2026-11-19**, with
the robot's own mics and speaker and live gestures. Roadmap step 6 (`roadmap.md`), pulled forward.

**Decision (Boston, 2026-11-13): everything runs on the robot.** The laptop is only for SSH,
testing and rehearsal. No laptop-to-robot frame streaming, no laptop speaker. Hiccups get fixed on
the robot. This is also the simplest clock story: the laptop design already assumes one machine
(speech loop and `gesture live` share `time.monotonic()`), and the robot is that machine.

## Architecture on the K1

```
K1 mic array ─► speech loop (P3) ─► Groq Whisper ─► gpt-oss-120b ─► cloud TTS ─► K1 speaker (USB card 0)
                     │  /begin /piece /end  (localhost HTTP, play times in time.monotonic)
                     ▼
              gesture live --robot (P2): library + MotionStream ─► 50 Hz reference frames in /dev/shm
                                                                          ▼
              deploy.py --task k1_gesture_live (P1, ROS 2, system Python): policy y1r48dhc ─► /joint_ctrl
```

Three processes, not one:
- **GIL:** P2 plans in ~100 ms bursts of Python. In the control process that would stall the 50 Hz loop.
- **Python versions:** P1 is the robot's system Python with ROS 2 (`rclpy`, `booster_interface`); P2 and P3 are
  our uv venvs (3.12). Shared memory of plain numpy arrays works across both.
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
  `aplay`'s default is the Jetson's silent internal audio. The speech loop finds devices by name (`find_device`), so a
  name like "USB Audio" in the config should be enough.
- **Mics:** datasheet: circular 6-mic array in the head. **Seen 2026-11-12: iFlytek XFM-DP-V0.0.18 USB board, ALSA
  card 1** (`arecord -D plughw:1,0 -r 16000 -c 1` works; PulseAudio shows it as a mono 16 kHz source). It dropped off
  USB while the robot was moved and needed a reboot: check `cat /proc/asound/cards` before each test.
- **Booster SDK audio service** (`booster_robotics_sdk_python` 1.6.3 on PyPI, cp310–cp314 aarch64 wheels; example
  `python_example/sdk_pybind_audio_example.py`; headers say K1 | T1 | T2):
  - `AudioManager`: `GetDevices`, system volume / mute, Bluetooth.
  - `AudioCaptureStream`: mic PCM frames by callback, **`raw`** (default 16 kHz, 3 channels, 16-bit, "BoosterAEC")
    and **`naec`** (echo-cancelled; "hardware/backend dependent, may return kAudioErrNotSupported").
  - `AudioPlayer`: files or a PCM stream (`PushPcmStream`), `SetPreferredDevice`.
  - `AudioLocalizer.GetDoaAngle()`: direction the voice comes from (later: turn the head toward the speaker).
  - `AiClient.StartAiChat` / `StopAiChat` (Booster's own voice assistant: needs their cloud), `LuiClient` (their
    ASR/TTS). Nothing documents how to keep their assistant from holding the mic.
  - Needs `ChannelFactory.Instance().Init(0, <net if>)` (DDS). Unknown whether the robot's firmware matches SDK 1.6.3.
    Robot interfaces (2026-11-12): `enP9p1s0` 192.168.10.102, `enP8p1s0` 192.168.13.101, `usb_eth0` 192.168.127.101.
  - Booster's `ensure-booster-alsa-config` manages `/etc/asound.conf`: choose devices by name, don't edit it. Their
    `booster-audio` already publishes mic audio (`/booster/audio/capture/slot_1..8`) and has a wake-word/DOA library.

## Unknowns: probe first (10 min of robot time, read-only)

1. **Internet from the robot** (Groq, TTS): **yes, IllinoisNet** (2026-11-12, `10.193.195.162`; JoinNow renewal due
   2026-12-18). Left: `curl` timing to `api.groq.com`.
2. **Mic access:** does the array show in `arecord -l` / PipeWire-PulseAudio (`pactl list short sources`), or only
   through Booster's audio service? Is their assistant or audio service holding it (`fuser -v /dev/snd/*`,
   `systemctl list-units | grep -i -E 'audio|ai|rtc|lui'`)?
3. **Python:** `uv` present? (else install it; needs internet). Disk space for venvs + library (220 MB).
4. **CPU / memory headroom** with `deploy.py` running (`top`, `free -h`).
5. **Noise:** 5 s recordings, quiet and with the motors running (fans, motors into VAD).
6. **Echo:** play a test sentence on card 0 while recording: how loud is the robot's own voice in its mics?

Script: `tools/robot_probe.sh` (to write; prints everything, records the WAVs, copies them back).

## Work before Thursday

**A. Robot runtime** (laptop first, rehearsed with the robot's exact process layout):
1. `gesture live --robot`: same planner and HTTP events, but instead of running the policy in MuJoCo it writes
   timestamped 50 Hz frames (joint positions, velocities, trunk orientation) a few seconds ahead into shared
   memory. Keep the window mode for testing.
2. `booster_deploy` task **`k1_gesture_live`** (copy of `k1_gesture_tracking`): reads the frame for "now" from shared
   memory instead of a clip file; stale-frame safety (table above); same X / A / Ctrl-C, same run logs and
   `check_run.py`.
3. **Rehearsal on the laptop:** speech loop + `gesture live --robot` + `fake_robot.py` running
   `deploy.py --task k1_gesture_live`. The standard live test (`tools/live_test.sh` script), then 10 min, and kill
   each process once to check the failure table.
4. **Speech robot profile:** a config for the robot (devices by name, cloud TTS) and a slim install: Silero VAD
   through onnxruntime without torch, no faster-whisper, no Kokoro. **No Kokoro fallback onboard**, so the cloud TTS
   must not run out: Groq Dev tier for Orpheus (~$0.02 per 10-turn conversation) or Cartesia. Kokoro on the Jetson
   GPU is a later option.
5. **K1 audio adapter, only if the mics aren't plain ALSA:** `speech/src/speech/k1_audio.py` with the SDK's
   `AudioCaptureStream` (use `naec` if supported) and `AudioPlayer` PCM stream, behind the same interface the loop
   uses for sounddevice.
6. **Install + start scripts:** copy the gesture runtime, speech, library and keys to the robot
   (`sync_to_robot.sh`-style); `tools/robot_conversation.sh` starts P1–P3 in `tmux` panes. API keys on a shared
   robot: use separate keys and revoke them afterwards.

**B. Context gestures** (in sim, in parallel once A1–A3 work; design in `gesture_plan.md` step 8). Ships to the
robot as library units and LLM prompt changes, with no robot-side code:
1. Emphasis tags (`[emph]...[/emph]`): the generator raises that segment's intensity.
2. A small vocabulary: `wave` (greeting / goodbye; `wave_000508`, `wave_001104` already track 50/50), `point_you`,
   `point_self`. Inline tags, stripped before TTS, tied to word times; the generator enforces the rate (≤ 1 per
   sentence + cooldown). Units: search BEAT2 first, phone video → GVHMR → GMR if missing. `sim2sim` every new unit.

**C. Robot time** (any session before Thursday if possible, then Thursday). Each step only if the previous was clean:
1. Probe (above).
2. Audio alone: record + play with the robot standing in Booster's controller; then the speech loop alone on the
   robot (no gestures): a few turns.
3. One canned clip (`k1_gesture_tracking`) to confirm nothing changed.
4. Live conversation on the gantry, then the floor with a slack harness. Someone else on the e-stop.
5. 5 minutes, then 10.

**Done when:** a 5-minute conversation on the floor with the robot's own mics and speaker, gestures in sync, no
fall, no manual restarts (roadmap step 6).

## Fallbacks (only if a step fails on the robot)

- Mics unusable (noise, locked by Booster's service): a USB conference mic plugged into the robot.
- No internet on the robot: phone hotspot.
- Robot hears itself: half-duplex is already the rule (`speech/src/speech/vad.py` pauses the mic during
  playback and skips `echo_tail_ms` after it); raise `echo_tail_ms` if needed, then the `naec` stream.
- Orin CPU too busy: the planner's chunk sizes and the onnxruntime threads are the knobs; measure first.
