#!/bin/bash
# Публичный монитор жилья: снапшот из PostgreSQL -> GitHub Pages.
# Запускается cron-джобом (05:00 МСК = 02:00 UTC); ручной запуск безопасен:
# без изменений в данных джоб ничего не коммитит.
set -euo pipefail

REPO="/home/lnr/research-wiki-private"
PY="/home/lnr/.hermes/hermes-agent/venv/bin/python3"
cd "$REPO"

echo "[1/4] сборка среза"
"$PY" scripts/build_public_monitor.py

echo "[2/4] проверка, что срез живой"
"$PY" - <<'PY'
import json
J = json.load(open('/home/lnr/research-wiki-private/docs/public-monitor.json', encoding='utf-8'))
empty = [m['code'] for m in J['metrics'] if not J['series'][m['code']]['rf']]
assert len(J['regions']) > 80, f"регионов мало: {len(J['regions'])}"
assert len(empty) <= 2, f"пустые метрики: {empty}"
print(f"  метрик {len(J['metrics'])}, регионов {len(J['regions'])}, срез {J['generated_at']}, пустых {len(empty)}")
PY

echo "[3/4] коммит в приватный репозиторий"
git add docs/public-monitor.json docs/public-monitor.html scripts/build_public_monitor.py
if git diff --cached --quiet; then
  echo "  изменений нет — публикация не нужна"
  exit 0
fi
git commit -q -m "Публичный монитор: автообновление среза $(date -u +%Y-%m-%d)" || true
git push private main 2>/dev/null || echo "  push private: не удалось (проверить руками)"

echo "[4/4] публикация в зеркало"
APPLY=1 "$PY" scripts/publish_wiki.py | tail -6
echo "готово: docs/public-monitor.html опубликован"
