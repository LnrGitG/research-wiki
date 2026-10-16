#!/bin/bash
# domrf_price_job.sh — cron-обёртка: индекс цен ДОМ.РФ.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
cd /home/lnr/research-wiki-private
"$PY" scripts/domrf_fetch_monthly.py || exit 1
"$PY" scripts/transfer_domrf_price.py || exit 2
echo "domrf_price: обновление + перенос в канон завершены"
