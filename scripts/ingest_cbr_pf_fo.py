#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ставка и объёмы проектного финансирования по федеральным округам → канон.

Источник: raw/cbr/escrow/DDMMYYYY.xlsx (месячные файлы ЦБ «Информация о
проектном финансировании», страница
https://cbr.ru/statistics/bank_sector/equity_const_financing/).

Почему отдельный загрузчик. Штатный `cbr_banking_canon.py` берёт колонки по
фиксированным индексам (4 → «Задолженность», 7 → «ставка»). Это верно только
для файлов 2025 года и новее: в файлах 2022–2024 колонки «Задолженность» нет
вовсе, поэтому индекс 4 попадал в «Кол-во счетов эскроу», а 7 — в «Кол-во
раскрытых счетов». В результате ряды `cbr_pf_rate_reg_m` и `cbr_pf_debt_reg_m`
содержат не ставки и не задолженность (значения до 3·10⁶ «процентов»).
Загрузчик читает шапку и находит колонки по тексту заголовка, а не по номеру.

Что важно про гранулярность: ставка в файлах публикуется только по
федеральным округам, по субъектам колонка пуста (конфиденциальность). Поэтому
новые метрики — окружные, а агрегат по России считается как взвешенное
среднее ставок округов с весом «Сумма действующих кредитных договоров».

Метрики (unit 12 — %, unit 11 — млн руб.):
  cbr_pf_rate_fo_m   средневзвешенная ставка по кредитным договорам ПФ, округа
  cbr_pf_sum_fo_m    сумма действующих кредитных договоров ПФ, округа
  cbr_pf_debt_fo_m   задолженность по действующим кредитным договорам ПФ, округа
  cbr_pf_rate_ru_m   ставка по России (взвешенная по сумме договоров округов)

Идемпотентно: строки предыдущего прогона этого релиза удаляются перед вставкой.
"""
try:
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
ENGINE = engine_from_argv()  # --xlsx-engine openpyxl|fastexcel, резерв — XLSX_ENGINE

try:
    from xlsx_engine import open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import open_workbook  # noqa: E402

import datetime as dt
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ESCROW_DIR = os.path.join(BASE, 'raw', 'cbr', 'escrow')
RELEASE_LABEL = os.environ.get(
    'CBR_PF_RELEASE', 'cbr-pf-fo canon 2026-10-15 (ставки по округам)')

METRICS = {
    'cbr_pf_rate_fo_m': ('ЦБ: средневзвешенная ставка по кредитным договорам проектного '
                         'финансирования, федеральные округа', 12),
    'cbr_pf_sum_fo_m': ('ЦБ: сумма действующих кредитных договоров проектного '
                        'финансирования, федеральные округа', 11),
    'cbr_pf_debt_fo_m': ('ЦБ: задолженность по действующим кредитным договорам проектного '
                         'финансирования, федеральные округа', 11),
    'cbr_pf_rate_ru_m': ('ЦБ: средневзвешенная ставка по кредитным договорам проектного '
                         'финансирования, Российская Федерация', 12),
}

# признаки колонок в шапке (нормализованный текст)
COLMAP = [
    ('name', ('субъект',)),
    ('n_contracts', ('кол-во действующих кредитных',)),
    ('sum_contracts', ('сумма действующих кредитных',)),
    ('debt', ('задолженность',)),
    ('n_escrow', ('кол-во счетов эскроу',)),
    ('escrow_bal', ('остатки средств на счетах',)),
    ('rate', ('ставка по кредитным договорам',)),
]


def norm(s):
    return re.sub(r'\s+', ' ', ('' if s is None else str(s))).strip().lower().replace('ё', 'е')


def header_map(row):
    """Номер колонки → поле, по тексту шапки."""
    out = {}
    for idx, cell in enumerate(row):
        t = norm(cell)
        if not t:
            continue
        for field, keys in COLMAP:
            if field in out.values():
                continue
            if any(k in t for k in keys):
                out[idx] = field
                break
    return out


def fname_to_date(fname):
    m = re.match(r'(\d{2})(\d{2})(\d{4})\.xlsx$', fname)
    if not m:
        return None
    d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return dt.date(y, mo, 1)


def parse_file(path):
    """Возвращает {имя_округа: {поле: значение}} + номер строки шапки."""
    wb = open_workbook(path, engine=ENGINE)
    # read_only-лист отдаёт строки однократно: читаем всё одним проходом
    all_rows = list(wb.active.iter_rows(values_only=True))
    wb.close()
    if not all_rows:
        return {}, None
    hrow, hidx = None, None
    for i, r in enumerate(all_rows[:30]):
        if r and any('субъект' in norm(c) for c in r):
            hrow, hidx = r, i
            break
    if hrow is None:
        return {}, None
    cmap = header_map(hrow)
    if 'name' not in cmap.values():
        return {}, hidx
    out = {}
    total_rows = all_rows[hidx + 1:]
    for r in total_rows:
        if not r:
            continue
        # имя округа лежит не всегда в колонке «Субъект»: в строках ФО колонка
        # «Субъект» пуста, а название стоит в колонке «№ п/п» (она без номера).
        name = None
        for cell in r:
            if isinstance(cell, str) and cell.strip():
                name = cell.strip()
                break
        if not name:
            continue
        if not re.search(r'\bФО\b|федеральный округ', name, re.I):
            continue
        rec = {}
        for idx, field in cmap.items():
            if field == 'name' or idx >= len(r):
                continue
            v = r[idx]
            if isinstance(v, (int, float)):
                rec[field] = float(v)
        if rec:
            out[name] = rec
    return out, hidx


def fo_prefix(name):
    """'Центральный ФО' → 'центральный'."""
    s = norm(name)
    s = re.sub(r'\s*фо\s*$', '', s)
    s = re.sub(r'\s*федеральный округ\s*$', '', s)
    return s.strip()


def main():
    files = sorted(f for f in os.listdir(ESCROW_DIR)
                   if re.match(r'\d{8}\.xlsx$', f)) if os.path.isdir(ESCROW_DIR) else []
    if not files:
        raise SystemExit('нет файлов в %s' % ESCROW_DIR)

    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src_id = cur.execute(
                "SELECT source_id FROM catalog.source WHERE source_code='cbr'").fetchone()[0]
            freq_m = cur.execute(
                "SELECT frequency_id FROM catalog.frequency WHERE freq_code='M'").fetchone()[0]
            rf_id = cur.execute(
                "SELECT region_id FROM catalog.region WHERE name_ru='Российская Федерация'"
            ).fetchone()[0]
            fo = cur.execute(
                "SELECT region_id, name_ru FROM catalog.region WHERE level='federal_district'"
            ).fetchall()
            fo_by_prefix = {fo_prefix(nm): rid for rid, nm in fo}

            def resolve_fo(name):
                return fo_by_prefix.get(fo_prefix(name))

            rel = cur.execute('SELECT release_id FROM catalog.release WHERE label=%s',
                              (RELEASE_LABEL,)).fetchone()
            if rel:
                release_id = rel[0]
            else:
                release_id = cur.execute(
                    """INSERT INTO catalog.release (source_id,label,published_at,status,notes)
                       VALUES (%s,%s,%s,'loaded',
                               'ставки и объёмы проектного финансирования по округам, '
                               'колонки по шапке файла')
                       RETURNING release_id""",
                    (src_id, RELEASE_LABEL, dt.date(2026, 10, 15))).fetchone()[0]
                conn.commit()

            def ensure_metric(code):
                r = cur.execute('SELECT metric_id FROM catalog.metric WHERE metric_code=%s',
                                (code,)).fetchone()
                if r:
                    return r[0]
                name, unit_id = METRICS[code]
                mid = cur.execute(
                    """INSERT INTO catalog.metric
                       (metric_code,name_ru,unit_id,source_id,frequency_id,metric_type,status,is_active)
                       VALUES (%s,%s,%s,%s,%s,'primary','active',true) RETURNING metric_id""",
                    (code, name, unit_id, src_id, freq_m)).fetchone()[0]
                conn.commit()
                return mid

            metrics = {c: ensure_metric(c) for c in METRICS}

            rows, rejects, months, ru_rate, scaled = [], {}, [], [], []
            for fname in files:
                per = fname_to_date(fname)
                if per is None:
                    continue
                parsed, hidx = parse_file(os.path.join(ESCROW_DIR, fname))
                if not parsed:
                    rejects[fname] = rejects.get(fname, 0) + 1
                    continue
                months.append((per, len(parsed)))
                # в файлах 2023-02…2023-06 ставка записана долей (0,046), а не
                # процентом: масштаб выравнивается по максимуму файла
                rates = [rec['rate'] for rec in parsed.values() if 'rate' in rec]
                if rates and max(rates) < 0.5:
                    for rec in parsed.values():
                        if 'rate' in rec:
                            rec['rate'] *= 100.0
                    scaled.append(fname)
                num, den = 0.0, 0.0
                for name, rec in parsed.items():
                    rid = resolve_fo(name)
                    if rid is None:
                        rejects[name] = rejects.get(name, 0) + 1
                        continue
                    if 'rate' in rec:
                        rows.append(('cbr_pf_rate_fo_m', rid, per, rec['rate']))
                        if 'sum_contracts' in rec:
                            num += rec['rate'] * rec['sum_contracts']
                            den += rec['sum_contracts']
                    if 'sum_contracts' in rec:
                        rows.append(('cbr_pf_sum_fo_m', rid, per, rec['sum_contracts']))
                    if 'debt' in rec:
                        rows.append(('cbr_pf_debt_fo_m', rid, per, rec['debt']))
                if den > 0:
                    ru_rate.append((per, num / den, den))

            for per, rate, wsum in ru_rate:
                rows.append(('cbr_pf_rate_ru_m', rf_id, per, rate))

            payload = sorted({(metrics[c], rid, per, v) for c, rid, per, v in rows})
            cur.execute('DELETE FROM data.observation WHERE release_id=%s', (release_id,))
            conn.commit()

            inserted = 0
            B = 2000
            for i in range(0, len(payload), B):
                chunk = payload[i:i + B]
                cur.executemany(
                    """INSERT INTO data.observation
                       (metric_id,region_id,period_start,frequency_id,value,
                        assessment_type,observation_status,source_id,release_id,sub_dimension)
                       VALUES (%s,%s,%s,%s,%s,'final','validated',%s,%s,'')
                       ON CONFLICT (metric_id,region_id,period_start,frequency_id,
                                    assessment_type,sub_dimension,release_id) DO NOTHING""",
                    [(m, rid, per, freq_m, v, src_id, release_id) for m, rid, per, v in chunk])
                inserted += cur.rowcount
            conn.commit()

            print('release_id=%s | файлов=%d | месяцев=%d | кандидатов=%d | новых=%d'
                  % (release_id, len(files), len(months), len(payload), inserted))
            for code, mid in metrics.items():
                got = cur.execute(
                    'SELECT count(*), count(DISTINCT region_id), min(period_start), '
                    'max(period_start) FROM data.observation WHERE metric_id=%s',
                    (mid,)).fetchone()
                print('  %-22s canon=%4d рег.=%2d %s .. %s'
                      % (code, got[0], got[1], got[2], got[3]))
            if rejects:
                print('отклонено:', sorted(rejects.items(), key=lambda x: -x[1])[:5])
            if scaled:
                print('масштаб ставки выправлен (доля → %):', ', '.join(scaled))
            bad = cur.execute(
                """SELECT count(*) FROM data.observation WHERE release_id=%s AND metric_id=%s
                   AND (value < 0.5 OR value > 40)""",
                (release_id, metrics['cbr_pf_rate_fo_m'])).fetchone()[0]
            print('ставки вне коридора 0,5–40 %:', bad)
            # контроль: ставка по России за последние месяцы
            print('контроль ставки РФ:', cur.execute(
                """SELECT to_char(period_start,'YYYY-MM'), round(value,2)
                   FROM data.observation WHERE metric_id=%s
                   ORDER BY period_start DESC LIMIT 6""",
                (metrics['cbr_pf_rate_ru_m'],)).fetchall())


if __name__ == '__main__':
    main()
