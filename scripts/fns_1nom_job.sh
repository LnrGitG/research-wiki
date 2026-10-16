#!/bin/bash
# fns_1nom_job.sh — cron-обёртка: обновление ФНС.
# 1) update_fns_1nom.py — докачка новых версий 1-НОМ в raw/fns и инжест по кодам ОКВЭД;
# 2) direct_fns.py — прямые загрузчики «сырьё → канон»: выручка по ОКВЭД F (G53),
#    РФ-итоги по формам ФНС, 5-П по регионам. Заменили группу рубежа 6 после снятия
#    SQLite-лендинга; запускаются после докачки, чтобы новые срезы попадали в канон.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
REPO=/home/lnr/research-wiki-private

"$PY" "$REPO/scripts/update_fns_1nom.py" \
  || echo "предупреждение: update_fns_1nom.py завершился с ошибкой"

APPLY=1 "$PY" "$REPO/scripts/direct_fns.py" 1nom_okved_f rf_annual profitorg
