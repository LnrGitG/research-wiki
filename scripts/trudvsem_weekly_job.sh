#!/bin/bash
# trudvsem_weekly_job.sh — cron-обёртка: сбор вакансий Работа России.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
exec "$PY" scripts/trudvsem_weekly.py
