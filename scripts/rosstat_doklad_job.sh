#!/bin/bash

# --- журнал загрузок (ops.ingest_run), см. scripts/run_logged.py ---
if [ -z "${INGEST_LOGGED:-}" ]; then
  exec env INGEST_LOGGED=1 /home/lnr/.hermes/hermes-agent/venv/bin/python3 \
       /home/lnr/research-wiki-private/scripts/run_logged.py --job "$(basename "$0")" -- bash "$0" "$@"
fi

# rosstat_doklad_job.sh — cron-обёртка: доклады Росстата (Соц-эк положение).
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
exec "$PY" scripts/transfer_doklad_08.py
