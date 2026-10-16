#!/bin/bash
# smartlab_ifrs_job.sh — cron-обёртка: панель МСФО девелоперов со smart-lab.ru.
#
# direct_smartlab.py — прямой загрузчик «сырьё → канон»: ходит за страницами
# /q/<TICKER>/f/{y,q}/ по шести публичным девелоперам (ПИК, Самолет, ЛСР, Эталон,
# GloraX, ДОМ.РФ), кладёт снимок разбора (JSON + исходный HTML) в
# raw/smartlab/ifrs/ и пишет в канон метрики «МСФО девелоперов: X»
# (release smart-lab). Заменил сборщик developers_ifrs_collect.py и SQLite-лендинг
# data/developers_ifrs.db — сняты из контура 16.10.2026.
#
# Идемпотентен: строки окна источника (годы 2021–2025 и пять последних кварталов)
# снимаются и переписываются заново; периоды ВНЕ окна не трогаются, снос не грозит.
# Если не удалось получить ни одну страницу — скрипт падает до записи в БД.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
REPO=/home/lnr/research-wiki-private
cd "$REPO" || exit 1

APPLY=1 "$PY" scripts/direct_smartlab.py || exit 2
echo "smartlab_ifrs: панель МСФО девелоперов загружена в канон"
