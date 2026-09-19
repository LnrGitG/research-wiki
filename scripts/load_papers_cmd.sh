#!/bin/bash
# Команда для ВМ YC: применить схему карточек и загрузить данные.
# Исполняется systemd-агентом, который опрашивает _cmd/command.sh.
set -e
export PGPASSFILE=/home/ubuntu/.pgpass
PSQL="psql -h localhost -U wiki -d research_wiki -v ON_ERROR_STOP=1"

echo "=== 1. схема core.paper_card ==="
if [ -f /home/ubuntu/_cmd/paper_card.sql ]; then
  $PSQL -f /home/ubuntu/_cmd/paper_card.sql
else
  echo "  ВНИМАНИЕ: paper_card.sql не найден в _cmd/"
fi

echo "=== 2. загрузка данных ==="
if [ -f /home/ubuntu/_cmd/load_paper_card.sql ]; then
  $PSQL -f /home/ubuntu/_cmd/load_paper_card.sql
else
  echo "  ВНИМАНИЕ: load_paper_card.sql не найден в _cmd/"
fi

echo "=== 3. контроль ==="
$PSQL -tAc "SELECT count(*) FROM core.paper_card"
$PSQL -tAc "SELECT count(*) FROM core.paper_card WHERE authors IS NOT NULL"
$PSQL -tAc "SELECT count(*) FROM core.paper_card WHERE file_available"
$PSQL -tAc "SELECT count(*) FROM core.paper_card WHERE findings IS NOT NULL"
$PSQL -tAc "SELECT count(*) FROM core.paper_card WHERE jsonb_array_length(coalesce(references_json,'[]'::jsonb)) > 0"
echo "--- пример записи ---"
$PSQL -tAc "SELECT paper_code, year, left(authors,40), n_references FROM core.paper_card WHERE n_references > 20 LIMIT 3"
echo "--- витрина ---"
$PSQL -tAc "SELECT count(*) FROM core.v_paper_card"
echo "=== ГОТОВО ==="
