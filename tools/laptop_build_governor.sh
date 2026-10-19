#!/bin/bash
# Keep the laptop (Dell XPS 15) cool during long CPU builds (tools/beat2_batch.py): run the
# `balanced` power profile until the chassis gets hot, `power-saver` until it cools, repeat.
#
# Why: one core at full turbo always reads 100 C on this laptop (Intel's own limit, ignored here);
# what heats the machine is total power. balanced runs GMR ~3x faster than power-saver but the
# chassis climbs ~1 C per 10 s; cycling kept it at 51-64 C at ~3x power-saver speed (2026-10-18).
#   hot  = any chassis sensor (SODIMM / Ambient / Other / HDD) >= 65 C, or mean core >= 93 C for 60 s
#   cool = chassis <= 52 C and mean core <= 70 C
# On any exit (build done, crash, kill) it sets power-saver; restore with `powerprofilesctl set balanced`.
# Also run build workers single-threaded: OMP_NUM_THREADS=1 (numpy threads x workers pinned 100 C).
#
# Usage (detached, so it survives the terminal / a Claude Code restart):
#   setsid nohup bash tools/laptop_build_governor.sh > /tmp/governor.log 2>&1 < /dev/null &
# It exits by itself when no `tools/beat2_batch.py --spec` process is left. Don't stop it with
# `pkill -f governor`: that pattern matches the shell running pkill; use its PID.
trap 'powerprofilesctl set power-saver; echo "$(date +%T) governor exiting: power-saver"' EXIT
trap 'exit 1' INT TERM HUP
mode=$(powerprofilesctl get); hot_since=0; last=$(date +%s); cycles=0
while true; do
  s=$(sensors 2>/dev/null)
  core=$(awk '/^Core [0-9]+:/ {gsub(/[+°C]/,"",$3); t+=$3; n++} END {if (n) print int(t/n)}' <<<"$s")
  chassis=$(awk '/^(SODIMM|Ambient|Other|HDD):/ {gsub(/[+°C]/,"",$2); if ($2+0>m) m=$2+0} END {print int(m)}' <<<"$s")
  now=$(date +%s)
  if [ -z "$core" ] || [ -z "$chassis" ]; then          # can't read sensors: be safe
    [ "$mode" != "power-saver" ] && powerprofilesctl set power-saver && mode=power-saver
  elif [ "$mode" = "balanced" ]; then
    if [ "$core" -ge 93 ]; then [ $hot_since -eq 0 ] && hot_since=$now; else hot_since=0; fi
    if [ "$chassis" -ge 65 ] || { [ $hot_since -ne 0 ] && [ $((now - hot_since)) -ge 60 ]; }; then
      powerprofilesctl set power-saver && mode=power-saver; hot_since=0
    fi
  elif [ "$chassis" -le 52 ] && [ "$core" -le 70 ]; then
    powerprofilesctl set balanced && mode=balanced; cycles=$((cycles + 1))
  fi
  if ! pgrep -f "[t]ools/beat2_batch.py --spec" > /dev/null; then echo "$(date +%T) build gone after $cycles cycles"; exit 0; fi
  if [ $((now - last)) -ge 1800 ]; then echo "$(date +%H:%M) $cycles cycles; $mode, core ${core}C, chassis ${chassis}C"; last=$now; fi
  sleep 5
done
