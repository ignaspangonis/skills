#!/usr/bin/env bash
set -euo pipefail

dir="${TMPDIR:-/tmp}/claude-listen"
mkdir -p "$dir"
pidfile="$dir/player.pid"
last="$dir/last.aiff"

stop_playback() {
  if [[ -f "$pidfile" ]]; then
    kill "$(cat "$pidfile")" 2>/dev/null || true
    rm -f "$pidfile"
  fi
}

play() {
  stop_playback
  nohup afplay "$1" >/dev/null 2>&1 &
  echo $! >"$pidfile"
  disown
}

case "${1:-}" in
  --stop)
    stop_playback
    exit 0
    ;;
  --again)
    [[ -f "$last" ]] || { echo "Nothing to replay yet." >&2; exit 1; }
    play "$last"
    echo "$last"
    exit 0
    ;;
esac

input="${1:-}"
[[ -f "$input" ]] || { echo "Usage: speak.sh <script file> | --again | --stop" >&2; exit 1; }
text="$(cat "$input")"
rm -f "$input"
[[ -n "${text//[[:space:]]/}" ]] || { echo "The script file is empty." >&2; exit 1; }

stamp="$(date +%Y%m%d-%H%M%S)"
printf '%s\n' "$text" >"$dir/$stamp.txt"

voice_args=()
[[ -n "${LISTEN_VOICE:-}" ]] && voice_args=(-v "$LISTEN_VOICE")

say "${voice_args[@]+"${voice_args[@]}"}" -r "${LISTEN_RATE:-170}" -o "$dir/$stamp.aiff" -f "$dir/$stamp.txt"
cp "$dir/$stamp.aiff" "$last"
play "$last"
echo "$dir/$stamp.aiff"
