#!/usr/bin/env python3
"""Прямой загрузчик: индексы производства по субъектам РФ (ind_sub_MM-YYYY.xlsx) → канон.

Путь «сырьё → канон» вместо прежнего «парсер → SQLite-лендинг (таблица
rosstat_ind_prod_regions) → гармонайзер 6». Прежний путь брал из файла ОДИН лист,
поэтому в канон попало 7 552 наблюдения одной серии; здесь разбираются все 15
серийных листов (5 видов деятельности × 3 единицы измерения).

Разбор: строка 2 — название серии, строка 3 — единица, строка 4 — годы
(объединённые блоки по 12 столбцов, у последнего года меньше), строка 5 — месяцы,
строки 6… — Российская Федерация, федеральные округа, субъекты; в конце
сноски-строки, начинающиеся с цифры («1Агрегированные…», «2 Без учета…») —
они прерывают разбор. Имена строк берутся как есть: в листе 4 встречаются
подгонка пробелами («Ямало-Ненецкий             авт. округ») и сносочные цифры
(«г. Севастополь3») — именно так они лежат в каноне с прежней дороги.

ВАЖНО про смысл метрики 1141 (вскрыто и исправлено 16.10.2026). Прежняя дорога
читала лист 4 — «Индекс производства по виду экономической деятельности „Добыча
полезных ископаемых“ по субъектам РФ», — а карточка называлась «Индекс
промышленного производства, % к соответствующему месяцу». Сверка окна дала
1 805 совпадений из 1 805 с листом 4 и ноль с листом 1, то есть подмена
произошла в парсере, до гармонайзера. По решению владельца карточка 1141
переименована под добычу (`RENAME=1`), а недостающие серии заведены отдельными
метриками: освободившееся имя и код `ippsm` достались настоящему ИПП (лист 1).

Окно файла — последние 20 месяцев (текущее: 2025-01..2026-08), то есть файл
СКОЛЬЗЯЩИЙ, а канон держит ряд по добыче с 2020-01: старые периоды накоплены
прежней дорогой и источник их уже не отдаёт. Отсюда два режима:
  * PRUNE=period (обычный месячный прогон) — снимаются ровно периоды из разбора,
    затем запись заново: правка исторических значений подхватывается, а периоды
    вне окна не теряются;
  * MIGRATE_FREQ=1 — разовая правка частоты исторической части на месте
    (Q → M): перезалив невозможен, а частота входит в уникальный ключ, поэтому
    UPDATE идёт с защитой NOT EXISTS по M-близнецу.

Запуск: APPLY=1 [PRUNE=period] [MIGRATE_FREQ=1] [RENAME=1] scripts/direct_ind_prod.py
"""
try:
    from xlsx_engine import open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import open_workbook  # noqa: E402

import gzip
import os
import re
import sys
import csv

try:
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
ENGINE = engine_from_argv()  # --xlsx-engine openpyxl|fastexcel, резерв — XLSX_ENGINE


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer, norm  # noqa: E402
import db_tunnel as t  # noqa: E402

MONTHS = {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
          'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11,
          'декабрь': 12}


def num(v):
    """Число из ячейки; пустое, прочерк и текст → None."""
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace('\xa0', '').replace(' ', '').replace(',', '.')
    return float(s) if re.match(r'^[-+]?\d*\.?\d+$', s) else None

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(REPO, 'raw', 'rosstat', 'data')
ATTIC = os.path.join(REPO, 'attic')
SOURCE = 'rosstat'
RELEASE = 'rosstat_ind_sub_2023'
FREQ = 'M'
UNIT = 'pct'

# 15 серийных листов файла: (вид деятельности, [лист «к соответств. месяцу»,
# лист «к соответств. периоду», лист «к предыдущему месяцу»]).
SECTIONS = [
    ('Индекс промышленного производства', '1', '2', '3'),
    ('Индекс производства по добыче полезных ископаемых', '4', '5', '6'),
    ('Индекс производства по обрабатывающим производствам', '7', '8', '9'),
    ('Индекс производства по обеспечению электрической энергией, газом и паром',
     '10', '11', '12'),
    ('Индекс производства по водоснабжению и водоотведению', '13', '14', '15'),
]
SUFFIX = (', % к соответствующему месяцу', ', % к соответствующему периоду',
          ', % к предыдущему месяцу')

# метрика прежней дороги и её новое имя
OLD_NAME = 'Индекс промышленного производства, % к соответствующему месяцу'
MINING_NAME = SECTIONS[1][0] + SUFFIX[0]


def latest_file():
    if not os.path.isdir(RAW_DIR):
        return None
    files = [f for f in os.listdir(RAW_DIR)
             if re.match(r'^ind_sub_\d{4}_\d{2}-\d{4}\.xlsx$', f)]
    return os.path.join(RAW_DIR, sorted(files)[-1]) if files else None


def parse(path, sheet):
    """[(имя строки, год, месяц, значение), …] с одного листа."""
    wb = open_workbook(path, engine=ENGINE)
    if sheet not in wb.sheetnames:
        wb.close()
        sys.exit('нет листа %s в %s' % (sheet, path))
    ws = wb[sheet]
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    if len(rows) < 6:
        return []
    years, months, cur = {}, {}, None
    for i, c in enumerate(rows[3]):
        if isinstance(c, str) and c.strip()[:4].isdigit() and len(c.strip()) >= 4:
            cur = int(c.strip()[:4])
        if cur is not None:
            years[i] = cur
    # Месяц берём по ПОЗИЦИИ внутри годового блока (блок начинается с января и
    # идёт по месяцам), а подпись используем как перекрёстную проверку: у серий
    # «к соответствующему периоду» подписи кумулятивные («январь-август», конец
    # диапазона = месяц периода), и в листе 5 последний столбец подписан
    # «январь-июль» вместо «январь-август» — по подписи этот месяц потерялся бы.
    pos, blk = 0, None
    for i, c in enumerate(rows[4]):
        if i not in years:
            continue
        if years[i] != blk:          # новый годовой блок — счёт позиции с начала
            blk, pos = years[i], 0
        pos += 1
        if pos > 12:
            continue
        label = ''
        if isinstance(c, str) and c.strip():
            label = norm(re.split(r'\s*-\s*', c.strip())[-1])
        if label in MONTHS and MONTHS[label] != pos:
            print('  предупреждение: лист %s, столбец %d: подпись «%s» против позиции %d '
                  'в блоке %d — берём позицию' % (sheet, i, c, pos, years[i]))
        months[i] = pos
    cols = [(i, years[i], months[i]) for i in sorted(months) if i in years]
    out = []
    for r in rows[5:]:
        name = r[0]
        if not isinstance(name, str) or not name.strip():
            continue
        name = name.strip()                # хвостовой пробел прежняя дорога снимала
        if name[:1].isdigit():             # сноски «1Агрегированные…»
            break
        for i, y, m in cols:
            v = num(r[i]) if len(r) > i else None
            if v is not None:
                out.append((name, y, m, v))
    return out


def rename_mining(w_dry=False):
    """Разовая правка карточки 1141: имя и код под добычу, единица «%».

    Освобождает имя и код `ippsm` для настоящего ИПП (лист 1), который
    заводится в том же прогоне. Идемпотентно: при повторе имя уже новое.
    """
    from metric_codes import code_from_name
    rows = t.query("""SELECT metric_id, metric_code, name_ru FROM core.metric
                      WHERE name_ru = %s OR metric_code = 'ippsm'""", (OLD_NAME,))
    if not rows:
        print('переименование: карточка уже под добычей')
        return
    for mid, code, name in rows:
        if name == MINING_NAME and code != 'ippsm':
            print('переименование: карточка %d уже под добычей (%s)' % (mid, code))
            continue
        new_code = code_from_name(MINING_NAME)
        if w_dry:
            print('переименование (без записи): %d %s «%s» -> %s «%s»'
                  % (mid, code, name, new_code, MINING_NAME))
            continue
        t.execute("""UPDATE core.metric SET name_ru = %s, metric_code = %s,
                        unit_id = (SELECT unit_id FROM core.unit WHERE unit_code = %s),
                        tags = (SELECT array(SELECT DISTINCT unnest(tags || %s)) FROM core.metric WHERE metric_id = %s)
                     WHERE metric_id = %s""",
                  (MINING_NAME, new_code, UNIT, ['direct_ind_prod'], mid, mid))
        t.execute("""UPDATE derived.metric_card SET metric_code = %s, name_ru = %s,
                        unit_code = %s, unit_ru = '%%',
                        search_text = replace(search_text, %s, %s)
                     WHERE metric_id = %s""",
                  (new_code, MINING_NAME, UNIT, name, MINING_NAME, mid))
        print('переименование: %d %s «%s» -> %s «%s»' % (mid, code, name, new_code, MINING_NAME))


def dump_group(w, metric_names, path):
    """Дамп наблюдений перечисленных метрик (csv.gz) — точка возврата."""
    if os.path.exists(path):
        # суффикс времени: '.csv.gz' — ДВА расширения, os.path.splitext разберёт
        # только второе и оставит имя вида «…before.csv_1792174599.gz»
        base = path[:-len('.csv.gz')] if path.endswith('.csv.gz') else os.path.splitext(path)[0]
        path = '%s_%d.csv.gz' % (base, os.path.getmtime(path))
    names = [norm(n[:200]) for n in metric_names]
    ids = sorted({mid for k, mid in w.by_name.items() if k in names})
    if not ids:
        return 0
    w.cur.execute("""SELECT metric_id, region_id, period_start, period_end, value,
                            frequency_id, assessment_type, observation_status,
                            source_id, release_id, sub_dimension
                     FROM data.observation WHERE metric_id = ANY(%s)""", (ids,))
    cols = ['metric_id', 'region_id', 'period_start', 'period_end', 'value',
            'frequency_id', 'assessment_type', 'observation_status', 'source_id',
            'release_id', 'sub_dimension']
    data = w.cur.fetchall()
    with gzip.open(path, 'wt', newline='') as fh:
        wr = csv.writer(fh)
        wr.writerow(cols)
        wr.writerows(data)
    return len(data)


def migrate_freq(w, metric_names):
    """Разовая правка частоты исторической части на месте (Q → M).

    Перезалив невозможен: этих периодов источник уже не отдаёт. Частота входит
    в уникальный ключ, поэтому UPDATE идёт с защитой — строки, у которых уже есть
    M-близнец по остальным полям ключа, не трогаются.
    """
    m = w.freq[FREQ]
    names = [norm(nm[:200]) for nm in metric_names]
    ids = sorted({mid for k, mid in w.by_name.items() if k in names})
    w.cur.execute("""
        UPDATE data.observation o SET frequency_id = %s
        WHERE o.metric_id = ANY(%s) AND o.frequency_id <> %s
          AND NOT EXISTS (SELECT 1 FROM data.observation x
              WHERE x.metric_id = o.metric_id AND x.region_id = o.region_id
                AND x.period_start = o.period_start AND x.frequency_id = %s
                AND x.assessment_type = o.assessment_type
                AND x.release_id = o.release_id
                AND coalesce(x.sub_dimension, '') = coalesce(o.sub_dimension, ''))""",
        (m, ids, m, m))
    moved = w.cur.rowcount
    w.cur.execute("""UPDATE core.metric SET frequency_id = %s WHERE metric_id = ANY(%s)""",
                  (m, ids))
    w.conn.commit()
    print('частота переведена на %s: наблюдений %d, карточек %d' % (FREQ, moved, len(ids)))


def main():
    apply = os.environ.get('APPLY') == '1'
    prune = 'period' if os.environ.get('PRUNE') == 'period' else False
    migrate = os.environ.get('MIGRATE_FREQ') == '1'
    rename = os.environ.get('RENAME') == '1'
    path = sys.argv[1] if len(sys.argv) > 1 else latest_file()
    if not path or not os.path.exists(path):
        sys.exit('не найдено raw/rosstat/data/ind_sub_*.xlsx')

    if rename:
        rename_mining(w_dry=not apply)

    series = []
    for section, *sheets in SECTIONS:
        for sheet, suffix in zip(sheets, SUFFIX):
            recs = parse(path, sheet)
            periods = sorted({(y, m) for _, y, m, _ in recs})
            print('лист %-3s %-58s строк %5d, имён %3d, периодов %d (%04d-%02d .. %04d-%02d)'
                  % (sheet, (section + suffix)[:58], len(recs),
                     len({r[0] for r in recs}), len(periods),
                     periods[0][0], periods[0][1], periods[-1][0], periods[-1][1]))
            series.append((section + suffix, recs))
    print('файл: %s | серий: %d | строк всего: %d'
          % (os.path.basename(path), len(series), sum(len(r) for _, r in series)))

    w = Writer(tag='direct_ind_prod')
    rows = []
    for name, recs in series:
        for nm, y, m, v in recs:
            rid, parts = w.resolve_region({'region': nm}, 'region', None)
            rows.append(dict(metric_name=name, value=v, ps=(y, m), region=rid,
                             sub=' | '.join(parts) or None, freq=FREQ,
                             source=SOURCE, release=RELEASE, unit=UNIT))
    mining = [MINING_NAME] if apply else [OLD_NAME, MINING_NAME]
    if not apply:
        print('без записи (APPLY=1 — записать): строк к канону %d' % len(rows))
        w.close()
        return

    # Дамп точки возврата — только для разовых режимов (правка частоты, правка
    # подрезов, переименование): месячный прогон иначе копил бы по файлу в attic.
    if migrate or rename or os.environ.get('DUMP') == '1':
        n = dump_group(w, mining, os.path.join(ATTIC, 'ind_prod_mining_before.csv.gz'))
        print('точка возврата: attic/ind_prod_mining_before.csv.gz — %d строк' % n)
    prep, ins, conf, nm_new = w.ingest(rows, group=RELEASE, prune=prune)
    print('подготовлено %d | вставлено %d | конфликтов %d | новых метрик %d'
          % (prep, ins, conf, nm_new))
    if migrate:
        migrate_freq(w, [MINING_NAME])
    w.close()


if __name__ == '__main__':
    main()
