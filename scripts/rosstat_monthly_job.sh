#!/bin/bash
# rosstat_monthly_job.sh — cron-обёртка: парсинг оперативных рядов Росстата.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
exec "$PY" scripts/rosstat_prom_monthly_parse.py
