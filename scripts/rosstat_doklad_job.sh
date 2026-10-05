#!/bin/bash
# rosstat_doklad_job.sh — cron-обёртка: доклады Росстата (Соц-эк положение).
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
exec "$PY" scripts/transfer_doklad_08.py
