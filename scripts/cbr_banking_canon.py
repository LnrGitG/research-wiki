#!/usr/bin/env python3
"""Загрузчик банковской статистики ЦБ: сырые xlsx → канон catalog/data.

Прямая запись в канон, БЕЗ промежуточного SQLite-лендинга (cbr_lending.db).
Заменяет связку update_cbr_lending.py (landing) + transfer_cbr_lending.py (мост).

Что загружается (только ряды, которых нет в каноне под другими путями):
  raw/cbr/bulletin/mortgage_lending_market_*.xlsx, лист Т_34 (квартальные цены)
      → cbr_housing_price_primary_reg_m, cbr_housing_price_secondary_reg_m
  raw/cbr/escrow/DDMMYYYY.xlsx, колонки «Задолженность» и «Средневзвешенная ставка»
      → cbr_pf_debt_reg_m, cbr_pf_rate_reg_m

Остальные ряды банковского бюллетеня (ИЖК по регионам, корпоративные кредиты,
эскроу-счета) в канон попадают из VFS-файлов ЦБ через transfer_cbr_vfs.py —
здесь повторно не грузятся, чтобы не заводить второго писателя тех же рядов.

Разрешение регионов: catalog.region.name_ru, затем meta.region_alias.
Идемпотентно: ON CONFLICT DO NOTHING по бизнес-ключу наблюдения.
Точка возврата: DELETE FROM data.observation WHERE release_id=<новый>.
"""
import datetime as dt
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402

try:
    import openpyxl
except ImportError:  # pragma: no cover
    raise SystemExit('нужен openpyxl: %s -m pip install openpyxl'
                     % sys.executable)

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BULLETIN_DIR = os.path.join(BASE, 'raw', 'cbr', 'bulletin')
ESCROW_DIR = os.path.join(BASE, 'raw', 'cbr', 'escrow')
RELEASE_LABEL = os.environ.get('CBR_BANKING_RELEASE',
                               'cbr-banking canon 2026-10-16 (прямая загрузка)')

MONTH_MAP = {'Январь': 1, 'Февраль': 2, 'Март': 3, 'Апрель': 4, 'Май': 5, 'Июнь': 6,
             'Июль': 7, 'Август': 8, 'Сентябрь': 9, 'Октябрь': 10, 'Ноябрь': 11, 'Декабрь': 12}
QMAP = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}

# код канона → (имя, unit_id)
METRICS = {
    'cbr_housing_price_primary_reg_m': ('ЦБ: средняя цена 1 кв.м жилья, первичный рынок (рег.)', 14),
    'cbr_housing_price_secondary_reg_m': ('ЦБ: средняя цена 1 кв.м жилья, вторичный рынок (рег.)', 14),
    'cbr_pf_debt_reg_m': ('ЦБ: задолженность по действующим кредитным договорам проектного '
                          'финансирования (рег.)', 11),
    'cbr_pf_rate_reg_m': ('ЦБ: средневзвешенная ставка по кредитным договорам проектного '
                          'финансирования (рег.)', 12),
}
# escrow: индекс колонки в файле (0-based; заголовок строки 4: 0=№,1=Субъект,
# 2=Кол-во действ. кред. договоров, 3=Сумма … договоров, 4=Задолженность,
# 5=Кол-во счетов эскроу, 6=Остатки …, 7=Средневзвешенная ставка, 8/9=раскрытые)
ESCROW_COLS = {4: 'cbr_pf_debt_reg_m', 7: 'cbr_pf_rate_reg_m'}


def norm(s):
    return (s or '').strip().lower().replace('ё', 'е')


def is_fo(name):
    s = (name or '').upper().strip()
    return 'ФЕДЕРАЛЬНЫЙ ОКРУГ' in s or s.endswith('ФО') or ' ФО ' in s


def parse_month_header(val):
    if isinstance(val, dt.datetime):
        return (val.year, val.month)
    m = re.match(r'(\S+)\s+(\d{4})', str(val).strip())
    if m and m.group(1) in MONTH_MAP:
        return (int(m.group(2)), MONTH_MAP[m.group(1)])
    return None


def rdate_str(y, m):
    return '%04d-%02d-01' % (y, m)


def parse_bulletin_prices(path):
    """Т_34: квартальные средние цены 1 кв.м (первичный/вторичный) по регионам."""
    out = []
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    if 'Т_34' not in wb.sheetnames:
        wb.close()
        return out
    rows = list(wb['Т_34'].iter_rows(min_row=1, values_only=True))
    wb.close()
    if len(rows) < 7:
        return out
    col_map, year, quarter = {}, None, None
    for col in range(1, 20):
        if col < len(rows[3]) and rows[3][col] is not None:
            m = re.search(r'(\d{4})', str(rows[3][col]))
            if m:
                year = int(m.group(1))
        if col < len(rows[4]) and rows[4][col] is not None:
            qm = re.match(r'^(I{1,3}V?|IV)\b', str(rows[4][col]).strip())
            if qm:
                quarter = QMAP.get(qm.group(1), quarter)
        if col < len(rows[5]) and rows[5][col] is not None and year and quarter:
            market = 'primary' if 'Первич' in str(rows[5][col]) else 'secondary'
            col_map[col] = (year, quarter, market)
    for row in rows[6:]:
        if row[0] is None:
            continue
        name = str(row[0]).strip()
        if is_fo(name) and 'РОССИЙСКАЯ' not in name.upper():
            continue
        for col, (y, q, market) in col_map.items():
            if col >= len(row):
                continue
            val = row[col]
            if val is not None and isinstance(val, (int, float)):
                code = ('cbr_housing_price_primary_reg_m' if market == 'primary'
                        else 'cbr_housing_price_secondary_reg_m')
                out.append((code, name, rdate_str(y, {1: 3, 2: 6, 3: 9, 4: 12}[q]), float(val)))
    return out


def parse_escrow_file(path):
    """Один файл = один месяц; берём «Задолженность» (кол.2) и «ставку» (кол.6)."""
    m = re.match(r'(\d{2})(\d{2})(\d{4})\.xlsx$', os.path.basename(path))
    if not m:
        return []
    _, month, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
    rdate = rdate_str(year, month)
    out = []
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    rows = list(wb.active.iter_rows(min_row=1, values_only=True))
    wb.close()
    for row in rows[4:]:                       # данные с 5-й строки (1-based)
        if len(row) < 3:
            continue
        name = row[1] if row[1] is not None else row[0]
        if name is None:
            continue
        name = str(name).strip()
        if is_fo(name) and 'РОССИЙСКАЯ' not in name.upper():
            continue
        for col, code in ESCROW_COLS.items():
            if col >= len(row):
                continue
            val = row[col]
            if val is not None and isinstance(val, (int, float)):
                out.append((code, name, rdate, float(val)))
    return out


def main():
    with db_tunnel.connect() as conn:
        with conn.cursor() as cur:
            src_id = cur.execute("SELECT source_id FROM catalog.source WHERE source_code='cbr'").fetchone()[0]
            freq_m = cur.execute("SELECT frequency_id FROM catalog.frequency WHERE freq_code='M'").fetchone()[0]

            rmap, amap = {}, {}
            for rid, nm, lvl in cur.execute('SELECT region_id, name_ru, level FROM catalog.region').fetchall():
                rmap[norm(nm)] = (rid, lvl)
            for al, rid, conf in cur.execute('SELECT alias, region_id, confidence FROM meta.region_alias').fetchall():
                k = norm(al)
                if k not in amap or conf == 'exact':
                    amap[k] = rid
            rf = cur.execute("SELECT region_id FROM catalog.region WHERE name_ru='Российская Федерация'").fetchone()
            rf_id = rf[0] if rf else None
            fo_ids = {r[0] for r in cur.execute("SELECT region_id FROM catalog.region WHERE level <> 'region'")}

            def resolve(name):
                n = norm(name)
                if not n or 'итого' in n or 'федерация' in n:
                    return None
                n = re.sub(r'^в том числе[:\s]*', '', n).strip()
                n = re.sub(r'^в т\.\s?ч\.\s*', '', n).strip()
                if n in rmap:
                    rid, lvl = rmap[n]
                    return rid if lvl == 'region' else None
                if n in amap:
                    rid = amap[n]
                    return None if rid == rf_id or rid in fo_ids else rid
                s = ''.join(ch for ch in n if not ch.isdigit()).strip()
                if s != n and s in rmap:
                    rid, lvl = rmap[s]
                    return rid if lvl == 'region' else None
                return None

            rel = cur.execute('SELECT release_id FROM catalog.release WHERE label=%s', (RELEASE_LABEL,)).fetchone()
            if rel:
                release_id = rel[0]
            else:
                release_id = cur.execute(
                    """INSERT INTO catalog.release (source_id,label,published_at,status,notes)
                       VALUES (%s,%s,%s,'loaded','прямая загрузка банковской статистики ЦБ в канон, без SQLite')
                       RETURNING release_id""",
                    (src_id, RELEASE_LABEL, dt.date(2026, 10, 16))).fetchone()[0]
                conn.commit()

            def ensure_metric(code):
                r = cur.execute('SELECT metric_id FROM catalog.metric WHERE metric_code=%s', (code,)).fetchone()
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
            conn.commit()

            raw_rows, rejects = [], {}
            for fname in sorted(os.listdir(BULLETIN_DIR)) if os.path.isdir(BULLETIN_DIR) else []:
                if fname.startswith('mortgage_lending_market_') and fname.endswith('.xlsx'):
                    raw_rows += parse_bulletin_prices(os.path.join(BULLETIN_DIR, fname))
            for fname in sorted(os.listdir(ESCROW_DIR)) if os.path.isdir(ESCROW_DIR) else []:
                if re.match(r'\d{8}\.xlsx$', fname):
                    raw_rows += parse_escrow_file(os.path.join(ESCROW_DIR, fname))

            rows = []
            for code, region, per, val in raw_rows:
                rid = resolve(region)
                if rid is None:
                    rejects[region] = rejects.get(region, 0) + 1
                    continue
                rows.append((metrics[code], rid, per, val))

            inserted = 0
            B = 2000
            for i in range(0, len(rows), B):
                chunk = rows[i:i + B]
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

            print('release_id=%s | всего кандидатов=%d, новых=%d' % (release_id, len(rows), inserted))
            for code, mid in metrics.items():
                got = cur.execute('SELECT count(*), count(DISTINCT region_id), max(period_start) '
                                  'FROM data.observation WHERE metric_id=%s', (mid,)).fetchone()
                print('  %-34s canon=%d рег.=%d до %s' % (code, got[0], got[1], got[2]))
            if rejects:
                print('отклонено (агрегаты/неопознанные):', sorted(rejects.items(), key=lambda x: -x[1])[:8])


if __name__ == '__main__':
    main()
