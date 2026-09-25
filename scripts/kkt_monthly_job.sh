#!/bin/bash
# Ежемесячное обновление ККТ ФНС (geochecki): сбор на ВМ и инжест в БД v2.
set -e
cd /home/lnr/research-wiki-private

# 1. Сбор на ВМ (monitor-машина): коллектор идемпотентен, перезаписывает CSV целиком
ssh -i ~/.ssh/id_yc -o ConnectTimeout=20 ubuntu@89.169.168.214 '~/.venvs/sandbox/bin/python3 /tmp/gc_kkt_collect2.py > /tmp/gc_kkt/collect_$(date +%Y%m).log 2>&1'

# 2. Забрать CSV и региональные JSON на VPS
scp -i ~/.ssh/id_yc ubuntu@89.169.168.214:/tmp/gc_kkt/kkt_summary.csv data/kkt_summary.csv
scp -i ~/.ssh/id_yc "ubuntu@89.169.168.214:/tmp/gc_kkt/kkt_regions_*.json" data/kkt_regions/ 2>/dev/null || true

# 3. Инжест (идемпотентен, ON CONFLICT DO NOTHING)
python3 scripts/ingest_kkt.py