#!/bin/bash
# rosstat_industrial_job.sh — cron-обёртка: промышленные индексы Росстата.
# Цепочка: prom_files_update → sezon_parse → refresh_staging → harmonize_6
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
"$PY" scripts/rosstat_prom_files_update.py || exit 1
"$PY" scripts/rosstat_sezon_parse.py || exit 2
"$PY" scripts/refresh_staging_tables.py || exit 3
"$PY" scripts/harmonize_6_rosstat_extra.py || exit 4
echo "rosstat_industrial: цепочка завершена"
