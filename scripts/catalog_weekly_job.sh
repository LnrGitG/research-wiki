#!/usr/bin/env bash
# catalog_weekly_job.sh — недельная пересборка каталога витрины и сторож ярлыков.
#
# Режим watchdog (no_agent): при норме в stdout не печатается ничего.
#   1) сторож: в витринном представлении не должно быть строк без кода метрики
#      (инцидент 17.10.2026: полтора месяца 1 097 972 наблюдения шли без ярлыка,
#      потому что представление читало замороженные *_legacy-копии справочников);
#   2) пересборка docs/metrics-catalog.json и docs/metrics-details.json — один
#      проход по канону, около девяти минут;
#   3) итог: число метрик в каталоге и число метрик в справочнике.
#
# Публикация витрины на GitHub Pages сюда НЕ входит: это отдельное действие
# владельца (APPLY=1 scripts/publish_wiki.py).
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
REPO=/home/lnr/research-wiki-private
cd "$REPO" || exit 1

out=""
# 1) сторож ярлыков
if ! chk=$("$PY" scripts/fix_datalens_view_live.py --check 2>&1); then
    out="ТРЕВОГА витрины: $chk"
fi

# 2) пересборка каталога
log=$(mktemp)
if ! "$PY" scripts/build_metrics_catalog.py >"$log" 2>&1; then
    out="$out
СБОЙ пересборки каталога: $(tail -3 "$log" | tr '\n' ' ')"
fi

n_cat=$("$PY" - <<'EOF' 2>/dev/null
import json
print(len(json.load(open('docs/metrics-catalog.json'))))
EOF
)
n_all=$("$PY" - <<'EOF' 2>/dev/null
import sys
sys.path.insert(0, 'scripts')
import db_tunnel as tunnel
print(tunnel.query('SELECT count(*) FROM core.metric')[0][0])
EOF
)
rm -f "$log"

if [ -n "$out" ]; then
    printf '%s\n' "$out"
fi
echo "каталог витрины: метрик $n_cat из $n_all"
