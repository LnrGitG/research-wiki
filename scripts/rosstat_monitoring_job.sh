#!/usr/bin/env bash

# --- журнал загрузок (ops.ingest_run), см. scripts/run_logged.py ---
if [ -z "${INGEST_LOGGED:-}" ]; then
  exec env INGEST_LOGGED=1 /home/lnr/.hermes/hermes-agent/venv/bin/python3 \
       /home/lnr/research-wiki-private/scripts/run_logged.py --job "$(basename "$0")" -- bash "$0" "$@"
fi

# Региональный монитор Росстата: докачка info-stat-MM-YYYY.zip и загрузка в канон.
# Молчит, когда нового выпуска нет (тихий cron): пустой stdout = успех.
set -u
cd /home/lnr/research-wiki-private || exit 1
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3

OUT=$(APPLY=1 $PY scripts/rosstat_monitoring_files_update.py 2>&1)
RC=$?
if [ "$RC" -ne 0 ]; then
  echo "монитор Росстата: код $RC"
  echo "$OUT" | tail -20
  exit "$RC"
fi
if [ -n "$OUT" ]; then
  echo "$OUT"
fi
exit 0
