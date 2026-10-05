#!/bin/bash
# wordstat_weekly_job.sh — cron-обёртка: Wordstat строительной активности.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
exec "$PY" scripts/wordstat_construction_collect.py
