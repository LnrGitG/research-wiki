#!/bin/bash
# cbr_api_monthly_job.sh — cron-обёртка: обновление API Банка России.
# Цепочка: monitoring_all → monitoring_facts → api_v2_ingest
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
"$PY" scripts/cbr_monitoring_all_collect.py || exit 1
"$PY" scripts/cbr_monitoring_facts_collect.py || exit 2
"$PY" scripts/cbr_api_v2_ingest.py || exit 3
echo "cbr_api: цепочка завершена"
