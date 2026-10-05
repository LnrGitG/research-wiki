#!/bin/bash
# metric_card_rebuild.sh — обновление статистики карточек метрик (без эмбеддингов)
# Запуск: cron no_agent, ежедневно 03:00 UTC
# --skip-embed: обновляет n_obs, freshness_days, period_min/max, themes, search_text
# Полный ребилд с эмбеддингами — вручную: python3 scripts/build_metric_cards.py
set -euo pipefail
cd ~/research-wiki-private
~/.hermes/hermes-agent/venv/bin/python3 scripts/build_metric_cards.py --skip-embed 2>&1 | tail -5