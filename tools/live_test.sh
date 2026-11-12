#!/usr/bin/env bash
# Standard live test (notes/live_test_script.md): gesture service + speech loop + video, one command.
#
#   tools/live_test.sh            # the K1 gestures live in a MuJoCo window while you talk (step 7);
#                                 # press Ctrl-C when done; then a video of exactly what it did live
#                                 # is made (gesture live-video), with your voice and its replies
#   tools/live_test.sh --no-video # skip the video (still checks the motion)
#   tools/live_test.sh --offline  # step 6's way: no window, motion made after each reply
#   DRY_RUN=1 tools/live_test.sh --no-video   # test the script itself on the last recorded session
#
# Starts `gesture live` (or `gesture serve`) in the background, waits until it answers, runs the
# hands-free speech loop in this terminal, and when you stop it (Ctrl-C) stops the service, prints
# the live timing summary, and films the run (live) or replays the session as a video (--offline).
set -euo pipefail
cd "$(dirname "$0")/.."
REPO=$(pwd)
VIDEO_FLAG=""
MODE="live"
for arg in "$@"; do
  case "$arg" in
    --no-video) VIDEO_FLAG="--no-video" ;;
    --offline) MODE="serve" ;;
    *) echo "unknown option $arg"; exit 1 ;;
  esac
done

mkdir -p logs
LOG="logs/gesture_${MODE}_$(date +%Y-%m-%d_%H-%M-%S).txt"
echo "starting the gesture service: gesture $MODE (log: $LOG)..."
uv run gesture "$MODE" > "$LOG" 2>&1 &
SERVE_PID=$!
stop_service() { kill "$SERVE_PID" 2>/dev/null || true; wait "$SERVE_PID" 2>/dev/null || true; }
trap stop_service EXIT

for _ in $(seq 1 120); do
  curl -s -m 1 http://127.0.0.1:8765/health > /dev/null 2>&1 && break
  if ! kill -0 "$SERVE_PID" 2>/dev/null; then echo "gesture service failed to start:"; tail -20 "$LOG"; exit 1; fi
  sleep 1
done
curl -s -m 1 http://127.0.0.1:8765/health > /dev/null || { echo "gesture service not answering after 2 min"; exit 1; }
echo "gesture service ready."
[[ "$MODE" == "live" ]] && echo "The robot is in the MuJoCo window (drag with the mouse to turn the view). Leave it open."

BEFORE=$(ls -d speech/runs/20*/ 2>/dev/null | sort | tail -1 || true)
if [[ "${DRY_RUN:-0}" == "1" ]]; then   # testing this script without a microphone: reuse the last session
  BEFORE=""
else
  echo
  echo "Talk now (script: notes/live_test_script.md). Press Ctrl-C when you're done."
  echo
  # Ctrl-C reaches this script too; with a handler (not "ignore") the speech loop still gets it and
  # stops, while the script carries on to make the video.
  trap ':' INT
  (cd speech && uv run python -m speech.loop --hands-free) || true
  trap - INT
fi

SESSION=$(ls -d speech/runs/20*/ 2>/dev/null | sort | tail -1 || true)
if [[ -z "$SESSION" || "$SESSION" == "$BEFORE" ]]; then
  echo "no new session recorded."
  exit 0
fi
sleep 2   # let the last reply's motion request finish before stopping the service
stop_service
trap - EXIT
if [[ "$MODE" == "live" ]]; then
  echo
  echo "live motion (full log: $LOG):"
  grep -E "^\[live\] .*(replies|pieces after|first pieces|FELL|->)" "$LOG" || true
fi

SESSION=${SESSION%/}
if [[ "$MODE" == "live" ]]; then
  RUN=$(grep -oE "logs/gesture/live/[0-9_-]+" "$LOG" | tail -1)
  if [[ -n "$VIDEO_FLAG" || -z "$RUN" ]]; then exit 0; fi
  echo
  echo "filming what the robot did live ($RUN, ~1 min per 90 s of conversation)..."
  uv run gesture live-video --run "$RUN" 2>&1 | grep -E "^\[live-video\]|Error"
  exit 0
fi
echo
echo "making the conversation video for $SESSION..."
uv run gesture replay --session "$SESSION" $VIDEO_FLAG 2>&1 | grep -E "^\[conversation\]|^\[generate\]|^\[render\]|^conv_|WARNING|Error" \
  | sed 's/features.*foot lock/foot lock/'
OUT="$REPO/logs/gesture/conversations/conv_$(basename "$SESSION")"
[[ -z "$VIDEO_FLAG" ]] && echo && echo "video: $OUT/sim_audio.mp4" && echo "watch: ffplay -autoexit $OUT/sim_audio.mp4"
