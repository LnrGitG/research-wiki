#!/bin/bash
# domrf_price_job.sh — cron-обёртка: индекс цен ДОМ.РФ.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
exec "$PY" scripts/domrf_fetch_monthly.py
