#!/usr/bin/env bash
# Standard live test (notes/live_test_script.md): gesture service + speech loop + video, one command.
#
#   tools/live_test.sh            # talk; press Ctrl-C when done; the video is made automatically
#   tools/live_test.sh --no-video # skip the video (still checks the motion)
#   DRY_RUN=1 tools/live_test.sh --no-video   # test the script itself on the last recorded session
#
# Starts `gesture serve` in the background, waits until it answers, runs the hands-free speech loop
# in this terminal, and when you stop it (Ctrl-C) stops the service and replays the new session.
set -euo pipefail
cd "$(dirname "$0")/.."
REPO=$(pwd)
VIDEO_FLAG=""
[[ "${1:-}" == "--no-video" ]] && VIDEO_FLAG="--no-video"

mkdir -p logs
LOG="logs/gesture_serve_$(date +%Y-%m-%d_%H-%M-%S).txt"
echo "starting the gesture service (log: $LOG)..."
uv run gesture serve > "$LOG" 2>&1 &
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

SESSION=${SESSION%/}
echo
echo "making the conversation video for $SESSION..."
uv run gesture replay --session "$SESSION" $VIDEO_FLAG 2>&1 | grep -E "^\[conversation\]|^\[generate\]|^\[render\]|^conv_|WARNING|Error" \
  | sed 's/features.*foot lock/foot lock/'
OUT="$REPO/logs/gesture/conversations/conv_$(basename "$SESSION")"
[[ -z "$VIDEO_FLAG" ]] && echo && echo "video: $OUT/sim_audio.mp4" && echo "watch: ffplay -autoexit $OUT/sim_audio.mp4"
