#!/bin/bash
# fns_1nom_job.sh — cron-обёртка: обновление ФНС 1-НОМ.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
exec "$PY" /home/lnr/research-wiki-private/scripts/update_fns_1nom.py
