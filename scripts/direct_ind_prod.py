#!/usr/bin/env python3
"""Прямой загрузчик: ИПП по субъектам РФ (ind_sub_MM-YYYY.xlsx) → канон.

Путь «сырьё → канон» вместо прежнего «парсер → SQLite-лендинг (таблица
rosstat_ind_prod_regions) → гармонайзер 6 → канон». Группа рубежа 6 —
`rosreestr_deals__rosstat_ind_prod_regions`: источник `rosstat`, разбор периода
`ym`, регион по имени строки, одна метрика — «Индекс промышленного производства,
% к соответствующему месяцу» (`ippsm`, metric_id 1141), релиз `rosstat_ind_sub_2023`.

Сырьё: raw/rosstat/data/ind_sub_2023_MM-YYYY.xlsx, лист «4». Шапка: строка 2 —
название серии, строка 3 — единица («в % к соответствующему месяцу предыдущего
года»), строка 4 — годы (объединённые блоки по 12 столбцов, у последнего года
меньше), строка 5 — месяцы, строки 6… — Российская Федерация, федеральные округа,
субъекты; в конце сноски-строки, начинающиеся с цифры («1Агрегированные…»,
«2 Без учета…»), они прерывают разбор.

ВАЖНО про выбор листа (проверено 16.10.2026). Лист 4 в файле — это «Индекс
производства по виду экономической деятельности "Добыча полезных ископаемых" по
субъектам РФ», а не «Индекс промышленного производства» (это лист 1). Прежняя
дорога брала именно лист 4, и в каноне под метрикой 1141 «Индекс промышленного
производства, % к соответствующему месяцу» лежит индекс по ДОБЫЧЕ: сверка окна
дала совпадение с листом 4 по всем регионам и нулевое с листом 1, а таблица
лендинга `rosstat_ind_prod_regions` (7 457 строк) несёт те же значения. Загрузчик
намеренно повторяет прежний выбор листа — перевод групп не должен менять смысл
ряда; вопрос о переименовании метрики и о недостающих сериях (ИПП, обрабатывающие,
энергетика, водоснабжение) вынесен владельцу отдельно.

Окно файла — последние 20 месяцев (текущий: 2025-01..2026-08), то есть файл
СКОЛЬЗЯЩИЙ, а канон держит ряд с 2020-01: старые периоды накоплены прежней
дорогой из прошлых выпусков. Отсюда два режима:

  PRUNE=period — рабочий режим (месячный прогон): снимаются ровно периоды окна и
                 пишутся заново; периоды вне окна не трогаются.
  MIGRATE_FREQ=1 — разовая миграция частоты для остатка вне окна: рубеж 6 помечал
                 весь ряд квартальной частотой `Q`, хотя периоды идут по месяцам.
                 Источник этих периодов уже не отдаёт, поэтому значения
                 переносятся в неизменном виде, меняется только частота
                 (`UPDATE` с защитой от столкновения ключей: частота входит в
                 уникальный ключ, M-близнецов у метрики нет). Карточка метрики
                 тоже переводится на M.

Запуск:
    python3 scripts/direct_ind_prod.py                       # разбор и отчёт
    APPLY=1 PRUNE=period python3 scripts/direct_ind_prod.py  # месячный прогон
    APPLY=1 MIGRATE_FREQ=1 PRUNE=period python3 scripts/direct_ind_prod.py
        # разово: миграция частоты остатка плюс перезапись окна
"""
import glob
import os
import re
import sys

import openpyxl

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer, norm  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(REPO, 'raw', 'rosstat', 'data')
ATTIC = os.path.join(REPO, 'attic')
SHEET = '4'
SOURCE = 'rosstat'
RELEASE = 'rosstat_ind_sub_2023'
FREQ = 'M'
METRICS = ['Индекс промышленного производства, % к соответствующему месяцу']
MONTHS = {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
          'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11,
          'декабрь': 12}


def latest_file():
    files = sorted(glob.glob(os.path.join(RAW_DIR, 'ind_sub_*.xlsx')))

    def key(p):
        m = re.search(r'ind_sub_\d{4}_(\d{2})-(\d{4})', os.path.basename(p))
        return (int(m.group(2)), int(m.group(1))) if m else (0, 0)
    return max(files, key=key) if files else None


def num(v):
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        try:
            return float(v.strip().replace(' ', '').replace(',', '.'))
        except ValueError:
            return None
    return None


def parse(path):
    """[(имя строки, год, месяц, значение)] с листа «1»."""
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb[SHEET]
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    if len(rows) < 6:
        return []
    years, months, cur = {}, {}, None
    for i, c in enumerate(rows[3]):          # строка 4 — годы (объединённые блоки)
        if isinstance(c, str) and re.match(r'^\d{4}', c.strip()):
            cur = int(c.strip()[:4])
        if cur is not None:
            years[i] = cur
    for i, c in enumerate(rows[4]):          # строка 5 — месяцы
        if isinstance(c, str) and norm(c) in MONTHS:
            months[i] = MONTHS[norm(c)]
    cols = [(i, years[i], months[i]) for i in sorted(months) if i in years]
    out = []
    for r in rows[5:]:
        name = r[0]
        if not isinstance(name, str) or not name.strip():
            continue
        s = name.strip()
        if s[:1].isdigit():                  # сноски в конце листа
            break
        for i, y, m in cols:
            v = num(r[i]) if len(r) > i else None
            if v is not None:
                out.append((s, y, m, v))
    return out


def migrate_freq(w, metric_names):
    """Перевод частоты ряда на M (значения не меняются), с точкой возврата."""
    os.makedirs(ATTIC, exist_ok=True)
    n = w.dump_group(metric_names, os.path.join(ATTIC, 'ippsm_before_freq.csv.gz'),
                     delete=False)
    print('точка возврата: attic/ippsm_before_freq.csv.gz — %d строк' % n)
    mid_q = 'SELECT frequency_id FROM core.frequency WHERE frequency_code = %s'
    w.cur.execute(mid_q, (FREQ,))
    m_id = w.cur.fetchone()[0]
    names = [norm(nm[:200]) for nm in metric_names]
    ids = sorted({mid for k, mid in w.by_name.items() if k in names})
    w.cur.execute("""UPDATE data.observation o SET frequency_id = %s
        WHERE o.metric_id = ANY(%s) AND o.frequency_id <> %s
          AND NOT EXISTS (SELECT 1 FROM data.observation x
              WHERE x.metric_id = o.metric_id AND x.region_id = o.region_id
                AND x.period_start = o.period_start
                AND x.assessment_type = o.assessment_type
                AND x.release_id = o.release_id AND x.frequency_id = %s
                AND coalesce(x.sub_dimension, '') = coalesce(o.sub_dimension, ''))""",
                     (m_id, ids, m_id, m_id))
    moved = w.cur.rowcount
    w.cur.execute("UPDATE core.metric SET frequency_id = %s WHERE metric_id = ANY(%s)",
                  (m_id, ids))
    w.conn.commit()
    print('частота переведена на %s: наблюдений %d, карточек %d' % (FREQ, moved, len(ids)))


def main():
    apply = os.environ.get('APPLY') == '1'
    prune = 'period' if os.environ.get('PRUNE') == 'period' else False
    migrate = os.environ.get('MIGRATE_FREQ') == '1'
    path = sys.argv[1] if len(sys.argv) > 1 else latest_file()
    if not path or not os.path.exists(path):
        sys.exit('не найдено raw/rosstat/data/ind_sub_*.xlsx')
    recs = parse(path)
    periods = sorted({(y, m) for _, y, m, _ in recs})
    names = sorted({r[0] for r in recs})
    print('файл: %s, лист %s' % (os.path.basename(path), SHEET))
    print('строк разобрано: %d, имён строк: %d, периодов: %d (%04d-%02d .. %04d-%02d)'
          % (len(recs), len(names), len(periods),
             periods[0][0], periods[0][1], periods[-1][0], periods[-1][1]))

    w = Writer(tag='direct_ind_prod')
    rows = []
    for nm, y, m, v in recs:
        rid, parts = w.resolve_region({'region': nm}, 'region', None)
        rows.append(dict(metric_name=METRICS[0], value=v, ps=(y, m), region=rid,
                         sub=' | '.join(parts) or None, freq=FREQ, source=SOURCE,
                         release=RELEASE, unit='unknown'))
    if not apply:
        print('без записи (APPLY=1 — записать): строк к канону %d' % len(rows))
        w.close()
        return

    prep, ins, conf, nm_new = w.ingest(rows, group=RELEASE, prune=prune)
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, nm_new))
    if migrate:
        migrate_freq(w, METRICS)
    w.close()


if __name__ == '__main__':
    main()
