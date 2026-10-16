#!/bin/bash
# rosstat_industrial_job.sh — cron-обёртка: промышленные индексы Росстата.
# Цепочка: prom_files_update → sezon_parse → harmonize_6
# Шаг refresh_staging убран 16.10.2026 (пункт 2 аудита): гармонайзер читает
# лендинги напрямую (staging_direct.py), схема staging больше не нужна.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
"$PY" scripts/rosstat_prom_files_update.py || exit 1
"$PY" scripts/rosstat_sezon_parse.py || exit 2
"$PY" scripts/harmonize_6_rosstat_extra.py || exit 3
echo "rosstat_industrial: цепочка завершена"
