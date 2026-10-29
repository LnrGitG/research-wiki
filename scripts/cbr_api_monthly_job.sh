#!/bin/bash

# --- журнал загрузок (ops.ingest_run), см. scripts/run_logged.py ---
if [ -z "${INGEST_LOGGED:-}" ]; then
  exec env INGEST_LOGGED=1 /home/lnr/.hermes/hermes-agent/venv/bin/python3 \
       /home/lnr/research-wiki-private/scripts/run_logged.py --job "$(basename "$0")" -- bash "$0" "$@"
fi

# cbr_api_monthly_job.sh — cron-обёртка: обновление API Банка России.
# Цепочка: monitoring_canon (API/XLSX → канон напрямую) → api_v2_ingest
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
"$PY" scripts/cbr_monitoring_canon.py || exit 1
"$PY" scripts/cbr_api_v2_ingest.py || exit 3
echo "cbr_api: цепочка завершена"
