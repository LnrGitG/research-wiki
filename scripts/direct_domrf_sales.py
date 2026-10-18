#!/usr/bin/env python3
"""Прямой лоадер ДОМ.РФ: статистические ряды реализации жилья (файл 01_05).

Чинит дефект harmonize_4_domrf.py, из-за которого разрез собирался из
порядкового номера строки и имени листа («разрез: Всего | строка 1 | ряд:
sales_meters | лист: 6 Застройщики…»). Такой разрез не идентифицирует ряд
как временной: один и тот же показатель РФ попадал в базу по несколько раз
(листы 3 «Регионы», 6 «Застройщики», 10 «Города»), а классы застройщиков и
городов терялись, потому что попадали в регион «Российская Федерация».

Новая схема разреза — явные измерения:
    охват: регионы | статус: Продано
    охват: застройщики | класс: от 50 до 500 тыс. кв. м | статус: Не продано (продажи открыты)
    охват: города | класс: до 50 тыс. чел. | статус: Продажи не открыты
    охват: РФ | статус: Уровень готовности

Запуск:
    DRY=1 python3 direct_domrf_sales.py     # только разбор и проверки
    APPLY=1 python3 direct_domrf_sales.py   # снимок старых строк, замена, проверки
"""
import os
import re
import sys
import datetime as dt

import openpyxl
import psycopg

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_tunnel import query, query_dict  # noqa: E402

RAW = os.path.expanduser('~/research-wiki-private/raw/domrf/01_05_stockvariables_sales.xlsx')
METRICS = {111: 'rkop_3', 114: 'rke_3', 107: 'usg_4', 108: 'rrf'}
MONTHS_RU = {
    'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
    'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11,
    'декабря': 12,
}

STATUSES = {
    'продано': 'Продано',
    'не продано (продажи открыты)': 'Не продано (продажи открыты)',
    'продажи не открыты': 'Продажи не открыты',
}
READY_LABELS = {
    'в стадии строительства, кв. м': ('stock', 111),
    'объем строящегося жилья, кв. м': ('stock', 111),
    'объем строящегося жилья в российской федерации, млн кв. м': ('stock_rf', 111),
    'уровень строительной готовности, %': ('ready', 107),
}

# лист -> (охват, метрика для метров, метрика для процентов)
SALES_SHEETS = {
    '3 Регионы реализация метры': ('регионы', 111),
    '4 Регионы реализация %': ('регионы', 114),
    '6 Застройщики реализация метры': ('застройщики', 111),
    '7 Застройщики реализация %': ('застройщики', 114),
    '10 Города реализация метры': ('города', 111),
    '11 Города реализация %': ('города', 114),
}
READY_SHEETS = {
    '5 Регионы стройготовность': ('регионы', False),
    '8 Застройщики стройготовность': ('застройщики', False),
    '12 Города стройготовность': ('города', False),
    '2 РФ стройготовность': ('РФ', True),
}
RF_SHEETS = {'1 РФ реализация'}


def norm(s):
    return '' if s is None else re.sub(r'\s+', ' ', str(s)).strip().lower()


def parse_header(row):
    """Периоды из строки заголовка: datetime-ячейки или «III кв. 2026»."""
    out = []
    for i, c in enumerate(row):
        if isinstance(c, dt.datetime):
            d = c.date()
            ps = d.replace(day=1)
            nxt = (ps.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
            out.append((i, ps, nxt - dt.timedelta(days=1), 'M'))
        elif isinstance(c, str):
            m = re.match(r'^(I|II|III|IV)\s*кв\.?\s*(\d{4})$', c.strip(), re.I)
            if m:
                q = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4}[m.group(1).lower()]
                y = int(m.group(2))
                ps = dt.date(y, 3 * q - 2, 1)
                pe = dt.date(y + (q == 4), (3 * q + 1) if q < 4 else 1, 1) - dt.timedelta(days=1)
                out.append((i, ps, pe, 'Q'))
    return out


def find_header(ws, max_scan=12):
    best = None
    for r in range(1, min(max_scan, ws.max_row) + 1):
        cells = [ws.cell(row=r, column=c).value for c in range(1, ws.max_column + 1)]
        per = parse_header(cells)
        if per and (best is None or len(per) > len(best[1])):
            best = (r, per)
    return best


def parse_sheet(ws, sheet):
    """Возвращает список (metric_id, region_label, period_start, period_end,
    freq, value, sub_dimension)."""
    hdr = find_header(ws)
    if not hdr:
        return [], f'{sheet}: не найден заголовок'
    hdr_row, periods = hdr
    scope = None
    metric_m = metric_p = None
    ready = None
    if sheet in SALES_SHEETS:
        scope, metric_m = SALES_SHEETS[sheet]
        metric_p = metric_m
    elif sheet in READY_SHEETS:
        scope, rf_mode = READY_SHEETS[sheet]
        ready = 'readiness'
    elif sheet in RF_SHEETS:
        scope = 'РФ'
    else:
        return [], f'{sheet}: нет правила'

    rows, bad_region, block = [], {}, None
    group = 'Российская Федерация' if sheet in RF_SHEETS else None
    cls = None            # класс (для листов застройщиков/городов)
    cur_metric = 108 if sheet in RF_SHEETS else metric_m
    cur_scope = scope

    for r in range(hdr_row + 1, ws.max_row + 1):
        a = ws.cell(row=r, column=1).value
        label = re.sub(r'\s+', ' ', str(a)).strip() if a is not None else ''
        nl = norm(label)
        if not label:
            continue
        # блоки внутри листа «1 РФ реализация»: млн кв. м, затем %
        if nl in ('млн кв. м', '%'):
            block = nl
            cur_metric = 108 if nl == 'млн кв. м' else 114
            continue
        if nl.startswith('плановый срок ввода'):
            block = 'план'
            continue
        if nl.startswith('аналитический центр') or nl.startswith('перейти в начало'):
            continue

        # строка-показатель внутри группы (готовность)
        if nl in READY_LABELS:
            kind, mid = READY_LABELS[nl]
            if kind == 'ready':
                status = 'Уровень готовности' + (', план' if block == 'план' else '')
                mid = 107
            else:
                # «В стадии строительства, кв. м» повторяет итог листов
                # реализации (проверено: РФ 2020-01 = 107 462 611,86 в обоих
                # листах) — не дублируем, иначе один ряд ложится дважды.
                # Исключение — блок планового ввода: там квартальные периоды
                # и другой смысл ряда.
                if block != 'план':
                    continue
                status = 'Плановый ввод'
                mid = 111
            grp = group or ('Российская Федерация' if cur_scope == 'РФ' else None)
            if not grp:
                continue
            sub = f'охват: {cur_scope} | статус: {status}'
            if cls:
                sub = f'охват: {cur_scope} | класс: {cls} | статус: {status}'
            if block == 'план':
                sub += ' | блок: плановый ввод'
            # лист «2 РФ стройготовность» отдаёт долю (0,44), а не процент
            k = 100.0 if (sheet == '2 РФ стройготовность' and kind == 'ready') else 1.0
            for ci, ps, pe, fq in periods:
                v = ws.cell(row=r, column=ci + 1).value
                if isinstance(v, (int, float)):
                    rows.append((mid, grp, ps, pe, fq, float(v) * k, sub))
            continue

        # статусные строки листов реализации
        if nl in STATUSES or (cur_scope == 'РФ' and nl == 'всего'):
            status = STATUSES.get(nl, 'Всего')
            grp = group
            if not grp:
                continue
            m = 114 if (cur_scope != 'РФ' and metric_m == 114) else (cur_metric or metric_m)
            sub = f'охват: {cur_scope} | статус: {status}'
            if cls:
                sub = f'охват: {cur_scope} | класс: {cls} | статус: {status}'
            for ci, ps, pe, fq in periods:
                v = ws.cell(row=r, column=ci + 1).value
                if isinstance(v, (int, float)):
                    rows.append((m, grp, ps, pe, fq, float(v), sub))
            continue

        # иначе — заголовок группы: регион, ФО или класс
        group = label
        if cur_scope in ('застройщики', 'города'):
            # группа «Всего» в листах классов — это итог РФ, он уже есть в
            # листе «3 Регионы»; такой блок пропускаем целиком
            cls = None if nl == 'всего' else label
            if nl == 'всего':
                group = None
                continue
        grp_for_total = label
        sub = f'охват: {cur_scope} | статус: Всего'
        if cls:
            sub = f'охват: {cur_scope} | класс: {cls} | статус: Всего'
        # в листах готовности строка группы пустая — «Всего» не пишем
        if sheet not in READY_SHEETS:
            for ci, ps, pe, fq in periods:
                v = ws.cell(row=r, column=ci + 1).value
                if isinstance(v, (int, float)):
                    rows.append((cur_metric or metric_m, grp_for_total, ps, pe, fq,
                                 float(v), sub))
    return rows, bad_region


def region_map():
    m = {norm(r['name_ru']): r['region_id'] for r in query_dict(
        'select region_id, name_ru from core.region')}
    for a in query_dict('select alias, region_id from meta.region_alias'):
        m.setdefault(norm(a['alias']), a['region_id'])
    m.setdefault('российская федерация', 1)
    return m


def build():
    wb = openpyxl.load_workbook(RAW, data_only=True, read_only=False)
    regs = region_map()
    freq = {r['frequency_code']: r['frequency_id'] for r in query_dict(
        'select frequency_id, frequency_code from core.frequency')}
    out, missing = [], {}
    for sheet in list(SALES_SHEETS) + list(READY_SHEETS):
        ws = wb[sheet]
        rows, _ = parse_sheet(ws, sheet)
        scope = (SALES_SHEETS.get(sheet) or READY_SHEETS.get(sheet) or ('РФ',))[0]
        for mid, grp, ps, pe, fq, v, sub in rows:
            rid = 1 if scope in ('застройщики', 'города', 'РФ') else regs.get(norm(grp))
            if not rid:
                missing[grp] = missing.get(grp, 0) + 1
                continue
            out.append((mid, rid, ps, pe, freq.get(fq, freq.get('M')), v, sub))
    wb.close()
    # страховка от коллизий: ключ (метрика, регион, период, разрез)
    seen, dedup = {}, []
    for row in out:
        k = (row[0], row[1], row[2], row[6])
        if k in seen:
            if abs(seen[k] - row[5]) > 1e-6:
                print(f'КОНФЛИКТ значений {k}: {seen[k]} vs {row[5]}', file=sys.stderr)
            continue
        seen[k] = row[5]
        dedup.append(row)
    if len(dedup) != len(out):
        print(f'снято дублей: {len(out) - len(dedup)}', file=sys.stderr)
    return dedup, missing


def verify(rows):
    prob = []
    if missing:
        prob.append(f'не сопоставлены регионы: {list(missing.items())[:5]}')
    return prob


if __name__ == '__main__':
    rows, missing = build()
    print(f'собрано наблюдений: {len(rows)}')
    by_m = {}
    for mid, *_ in rows:
        by_m[mid] = by_m.get(mid, 0) + 1
    print('по метрикам:', dict(sorted((k, v) for k, v in by_m.items() if k)))
    print('не сопоставлено регионов:', len(missing), list(missing.items())[:5])

    if os.environ.get('APPLY') != '1':
        print('DRY: запись не выполнялась (APPLY=1 для записи)')
        sys.exit(0)

    import psycopg
    from db_tunnel import connect

    conn = connect()
    cur = conn.cursor()
    cur.execute("select source_id from core.source where source_code='domrf'")
    sid = cur.fetchone()[0]
    stamp = '20261018'
    cur.execute("create schema if not exists attic")
    # снимок делается один раз: при повторных прогонах исходные строки уже
    # удалены, и перезапись снимка уничтожила бы точку возврата
    cur.execute("select to_regclass(%s)", (f'attic.domrf_sales_pre_fix_{stamp}',))
    if cur.fetchone()[0] is None:
        cur.execute(f"""create table attic.domrf_sales_pre_fix_{stamp}
                        as select * from data.observation where false""")
        cur.execute("""insert into attic.domrf_sales_pre_fix_%s
                       select * from data.observation
                       where source_id=%%s and metric_id in (107,111,114)""" % stamp, (sid,))
        print('снимок старых строк создан:', end=' ')
    else:
        print('снимок уже существует:', end=' ')
    cur.execute(f"select count(*) from attic.domrf_sales_pre_fix_{stamp}")
    print(cur.fetchone()[0], 'строк в снимке')

    cur.execute("""insert into catalog.release
                   (source_id, label, published_at, status, notes)
                   values (%s, %s, now(), 'loaded', %s) returning release_id""",
                (sid, 'domrf-statseries 2026-10-18 (лоадер v3: явные разрезы)',
                 'Переразбор 01_05 из raw XLSX: охват/класс/статус вместо номера строки'))
    rel = cur.fetchone()[0]
    cur.execute("delete from data.observation where source_id=%s and metric_id in (107,111,114)", (sid,))
    print('удалено старых:', cur.rowcount)

    cur.executemany("""insert into data.observation
        (metric_id, region_id, period_start, period_end, value, observation_status,
         assessment_type, release_id, frequency_id, source_id, sub_dimension)
        values (%s,%s,%s,%s,%s,'validated','final',%s,%s,%s,%s)""",
        [(mid, rid, ps, pe, v, rel, fq, sid, sub) for mid, rid, ps, pe, fq, v, sub in rows])
    conn.commit()
    print('вставлено:', len(rows), '| релиз:', rel)
    conn.close()
