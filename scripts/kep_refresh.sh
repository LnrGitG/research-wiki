#!/usr/bin/env bash
# Обновление «Краткосрочных экономических показателей РФ» (КЭП, рубеж 7).
#
# Один вызов проходит весь цикл: скачать свежий выпуск → разобрать в staging →
# гармонизировать в core.observation_v2. Оба python-скрипта идемпотентны:
#   * kep_collect.py     — сверяет хеш файла, при совпадении не перезаписывает;
#   * harmonize_7_kep.py — если выпуск уже загружен, печатает «пропуск» и выходит.
#
# РЕЖИМ ВЫВОДА (под cron с --no-agent, чтобы не будить LLM на рутинной загрузке):
#   * ничего нового нет  → пустой stdout (тишина, в Telegram ничего не уходит);
#   * загружен новый выпуск → короткий отчёт;
#   * сбой → сообщение + ненулевой код возврата (срабатывает failure-доставка).
#
# Расписание: КЭП публикуется 1–4 числа месяца (график оперативных публикаций
# Росстата, см. queries/kep-source.md). Cron ставится на 5-е число с повтором
# 7-го — второй прогон страхует от задержек и праздников.
set -uo pipefail

PY="$HOME/.hermes/hermes-agent/venv/bin/python3"
WIKI="$HOME/research-wiki"
cd "$WIKI" || { echo "СБОЙ: нет каталога $WIKI"; exit 1; }

# --- 1. сбор свежего выпуска ---
COLLECT_OUT=$("$PY" scripts/kep_collect.py 2>&1)
COLLECT_RC=$?
if [ $COLLECT_RC -ne 0 ]; then
    echo "СБОЙ: kep_collect.py, код $COLLECT_RC"
    echo "$COLLECT_OUT" | tail -15
    exit 1
fi

# --- 2. гармонизация ---
HARM_OUT=$("$PY" scripts/harmonize_7_kep.py 2>&1)
HARM_RC=$?
if [ $HARM_RC -ne 0 ]; then
    echo "СБОЙ: harmonize_7_kep.py, код $HARM_RC"
    echo "$HARM_OUT" | tail -15
    exit 1
fi

# --- 3. вывод только при изменениях ---
if echo "$HARM_OUT" | grep -q "уже загружен"; then
    exit 0            # пустой stdout = тишина
fi

LABEL=$(echo "$COLLECT_OUT" | grep -oP 'release_label: \K.*' | tail -1)
N_OBS=$(echo "$HARM_OUT" | grep -oP 'наблюдений: \K[0-9]+' | tail -1)
N_MET=$(echo "$HARM_OUT" | grep -oP 'метрик: \K[0-9]+' | tail -1)

echo "КЭП обновлён: ${LABEL:-выпуск не определён}"
echo "Наблюдений: ${N_OBS:-?}, метрик: ${N_MET:-?}"

# --- 4. запись в журнал репозитория ---
{
    echo ""
    echo "## $(date '+%Y-%m-%d') — КЭП: автоматическое обновление по расписанию"
    echo ""
    echo "- Выпуск: ${LABEL:-не определён}"
    echo "- Загружено наблюдений: ${N_OBS:-?}, метрик: ${N_MET:-?}"
    echo "- Источник: rosstat.gov.ru/compendium/document/50802"
} >> log-tech.md
git add log-tech.md 2>/dev/null
git commit -q -m "data(kep): автоматическое обновление — ${LABEL:-выпуск}" 2>/dev/null
