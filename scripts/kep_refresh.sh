#!/usr/bin/env bash
# Обновление «Краткосрочных экономических показателей РФ» (КЭП, рубеж 7).
#
# Один вызов проходит весь цикл: скачать свежий выпуск → разобрать в staging →
# гармонизировать в core.observation_v2. Оба python-скрипта идемпотентны:
#   * kep_collect.py     — сверяет хеш файла, при совпадении не перезаписывает;
#   * harmonize_7_kep.py — если выпуск уже загружен, печатает «пропуск» и выходит.
# Поэтому повторный запуск в тот же месяц безопасен и не создаёт дублей.
#
# Расписание: КЭП публикуется 1–4 числа месяца (график оперативных публикаций
# Росстата, см. queries/kep-source.md). Cron ставится на 5-е число с повтором
# 7-го — второй прогон страхует от задержек и праздников.
#
# Вывод: короткий отчёт в stdout, он же уходит в Telegram. Ненулевой код
# возврата = сбой, о нём сообщит failure-доставка cron.
set -uo pipefail

PY="$HOME/.hermes/hermes-agent/venv/bin/python3"
WIKI="$HOME/research-wiki"
cd "$WIKI" || { echo "ОШИБКА: нет каталога $WIKI"; exit 1; }

echo "=== КЭП: обновление $(date '+%Y-%m-%d %H:%M') ==="

# --- 1. сбор свежего выпуска ---
echo "--- шаг 1: сбор ---"
COLLECT_OUT=$("$PY" scripts/kep_collect.py 2>&1)
COLLECT_RC=$?
echo "$COLLECT_OUT" | tail -8
if [ $COLLECT_RC -ne 0 ]; then
    echo "СБОЙ: kep_collect.py завершился с кодом $COLLECT_RC"
    exit 1
fi

# --- 2. гармонизация ---
echo "--- шаг 2: гармонизация ---"
HARM_OUT=$("$PY" scripts/harmonize_7_kep.py 2>&1)
HARM_RC=$?
echo "$HARM_OUT" | tail -6
if [ $HARM_RC -ne 0 ]; then
    echo "СБОЙ: harmonize_7_kep.py завершился с кодом $HARM_RC"
    exit 1
fi

# --- 3. отчёт ---
if echo "$HARM_OUT" | grep -q "уже загружен"; then
    echo "ИТОГ: выпуск уже был загружен, изменений нет."
else
    N_OBS=$(echo "$HARM_OUT" | grep -oP 'наблюдений: \K[0-9]+' | tail -1)
    N_MET=$(echo "$HARM_OUT" | grep -oP 'метрик: \K[0-9]+' | tail -1)
    echo "ИТОГ: загружено наблюдений ${N_OBS:-?}, метрик ${N_MET:-?}."
fi
