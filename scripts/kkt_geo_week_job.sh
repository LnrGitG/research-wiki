#!/bin/bash
# Еженедельный сбор геочек ФНС (последняя полная неделя) + инжест в БД v2.
# Запуск: cron hermes, вторник 07:00 (неделя закрывается в пн, API отдаёт её со вторника).
set -e
cd "$HOME/research-wiki-private"

# 1. Сбор на ВМ (grid json синхронизировать на случай обновлений)
scp -q -i ~/.ssh/id_yc data/geochecki_grid.json ubuntu@89.169.168.214:/tmp/geochecki_grid.json
ssh -i ~/.ssh/id_yc ubuntu@89.169.168.214 'pkill -f gc_week_collect 2>/dev/null; nohup setsid ~/.venvs/sandbox/bin/python3 /tmp/gc_week_collect.py > /tmp/gc_geo/collect.log 2>&1 < /dev/null & sleep 150; tail -2 /tmp/gc_geo/collect.log'

# 2. Проверка результата: features total в логе
if ! grep -q "features total" /tmp/gc_geo/collect.log 2>/dev/null; then
  ssh -i ~/.ssh/id_yc ubuntu@89.169.168.214 'tail -20 /tmp/gc_geo/collect.log'
  echo "ERROR: сбор не завершился" >&2
  exit 1
fi

# 3. Забрать CSV и инжест
date_tag=$(date -d "last monday - 7 days" +%GW%V)
scp -q -i ~/.ssh/id_yc ubuntu@89.169.168.214:/tmp/gc_geo/geo_week.csv "data/geochecki_week_${date_tag}.csv"
~/.hermes/hermes-agent/venv/bin/python3 scripts/ingest_geochecki_week.py "data/geochecki_week_${date_tag}.csv"
echo "geoweek done: ${date_tag}"