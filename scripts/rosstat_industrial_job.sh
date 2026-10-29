#!/bin/bash
# rosstat_industrial_job.sh — cron-обёртка: оперативная статистика Росстата, прямой контур.
#
# Что грузится (порядок важен):
# 1) rosstat_prom_files_update.py — докачка месячных файлов с портала: Prom_MM_YYYY.xlsx
#    (бюллетень «Производство важнейших видов продукции»), ind_baza/ind_sub/sezon.
#    Prom сохраняется в raw/prom (его читает только direct_rosstat_prom.py), индексы —
#    в raw/rosstat/data. До 29.10.2026 скачивание всегда шло в raw/rosstat/data, и
#    загрузчик промпродукции нового выпуска не видел.
# 2) APPLY=1 direct_rosstat_prom.py — промпродукция в канон (месяц и накопленный итог).
# 3) APPLY=1 PRUNE=period direct_sezon.py — СС-индексы (SAAR): файл кумулятивный и
#    ревизуемый, поэтому периоды из разбора снимаются и пишутся заново.
# 4) APPLY=1 PRUNE=period direct_ind_prod.py — индексы производства по субъектам
#    (15 серийных листов). Файл скользящий (окно 20 месяцев), PRUNE=period снимает
#    только периоды окна, остальная история канона не трогается.
# 5) rosstat_operativ_construction_files_update.py + APPLY=1
#    direct_rosstat_operativ_construction.py — оперативные СМР по регионам
#    (Operativ_MM.xlsx, публикуется в конце месяца): уровень накопительно, индекс
#    накопительно г/г, индекс месяц г/г, индекс м/м — четыре отдельные метрики.
#
# Расписание в cron: 0 10 26-31,1-3 * * — окно публикаций Росстата (27–28 число:
# Prom и индексы 27.10, Operativ 28.10). Прежнее расписание «13-е число» данные не
# ловило: джоб отрабатывал через две недели после публикации, а сентябрьский выпуск
# 27–28.10.2026 не забрал вовсе.
#
# Тишина при отсутствии нового: обёртка снимает хеш-снимок сырья до и после докачки
# и, если ничего не изменилось, выходит молча (no_agent-джоб доставляет stdout как
# есть, поэтому ежедневный прогон в окне не должен давать ежедневный отчёт).
#
# История: 16.10.2026 при снятии гармонайзера 6 обёртка была обращена в заглушку,
# в тот же день восстановлена на прямых загрузчиках. 29.10.2026 добавлены индексы
# оперативных СМР и тихий режим, расписание переведено с 13-го числа на окно
# публикаций.
set -u
PY=/home/lnr/.hermes/hermes-agent/venv/bin/python3
REPO=/home/lnr/research-wiki-private
cd "$REPO" || exit 1

snapshot() {
  { ls -1 raw/prom/Prom_*.xlsx 2>/dev/null
    ls -1 raw/rosstat/data/ind_baza_2023_*.xlsx raw/rosstat/data/ind_sub_2023_*.xlsx \
          raw/rosstat/data/sezon_2023_*.xlsx raw/rosstat/data/Operativ_*.xlsx 2>/dev/null
  } | sort | xargs -r sha256sum 2>/dev/null | sha256sum | cut -c1-32
}

before=$(snapshot)

if ! prom_out=$("$PY" scripts/rosstat_prom_files_update.py 2>&1); then
  echo "rosstat_industrial: докачка файлов промышленной статистики не удалась"
  echo "$prom_out"
  exit 2
fi

if ! oper_out=$("$PY" scripts/rosstat_operativ_construction_files_update.py 2>&1); then
  echo "rosstat_industrial: докачка оперативных СМР не удалась"
  echo "$oper_out"
  exit 5
fi

after=$(snapshot)
if [ "$before" = "$after" ]; then
  exit 0            # нового выпуска нет — молчим
fi

new_files=$({ echo "$prom_out"; echo "$oper_out"; } | grep -E 'скачано|published=' || true)
echo "$new_files"

APPLY=1 "$PY" scripts/direct_rosstat_prom.py || exit 3

APPLY=1 PRUNE=period "$PY" scripts/direct_sezon.py || exit 4

APPLY=1 PRUNE=period "$PY" scripts/direct_ind_prod.py || exit 6

APPLY=1 "$PY" scripts/direct_rosstat_operativ_construction.py || exit 7

echo "rosstat_industrial: промпродукция, СС-индексы, индексы субъектов и оперативные СМР загружены в канон"
