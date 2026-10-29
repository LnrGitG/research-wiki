#!/bin/bash

# --- журнал загрузок (ops.ingest_run), см. scripts/run_logged.py ---
if [ -z "${INGEST_LOGGED:-}" ]; then
  exec env INGEST_LOGGED=1 /home/lnr/.hermes/hermes-agent/venv/bin/python3 \
       /home/lnr/research-wiki-private/scripts/run_logged.py --job "$(basename "$0")" -- bash "$0" "$@"
fi

# domrf_price_job.sh — cron-обёртка: индекс цен ДОМ.РФ.
# 1) domrf_fetch_monthly.py — скачивание API priceindex/living в raw CSV (без записи в БД);
# 2) direct_domrf.py — прямой загрузчик «сырьё → канон» (domrf_price_index_m,
#    domrf_price_index_mom, ddu_count_m). Заменил разовый перенос
#    transfer_domrf_price.py и инжест рубежа 6 из SQLite-лендинга (снят 16.10.2026).
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
REPO=/home/lnr/research-wiki-private
cd "$REPO" || exit 1

"$PY" scripts/domrf_fetch_monthly.py || exit 1
APPLY=1 "$PY" scripts/direct_domrf.py || exit 2
echo "domrf_price: скачивание и прямая загрузка в канон завершены"
