#!/bin/bash
# metric_card_rebuild.sh — обновление статистики карточек метрик (без эмбеддингов)
# Запуск: cron no_agent, ежедневно 03:00 UTC
# --skip-embed: обновляет n_obs, freshness_days, period_min/max, themes, search_text
# Полный ребилд с эмбеддингами — вручную: python3 scripts/build_metric_cards.py
set -euo pipefail
cd ~/research-wiki-private
# Без --skip-embed: карточки вставляются, а эмбеддинги запрашиваются только для
# текстов, которых нет в кэше по content_hash. Иначе новые метрики навсегда
# остаются без карточки (30.10: 246 активных рядов, включая cbr_pf_* и orvds*).
~/.hermes/hermes-agent/venv/bin/python3 scripts/build_metric_cards.py 2>&1 | tail -5