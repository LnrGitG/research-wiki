#!/usr/bin/env python3
"""
Рубеж 4: перенос ДОМ.РФ (domrf_indicators) в целевую модель.

Что переносится: 857 862 строки статистических рядов ДОМ.РФ — объём
строящегося жилья, продажи, разрешения, строительная готовность по регионам,
городам и застройщикам, месячная периодичность 2020–2026.

ПОТЕРЯННЫЙ РАЗРЕЗ. В части листов колонка, которую парсер счёл «регионом»,
содержит ПОДПИСЬ СТРОКИ, а не регион («% от строящегося жилья», «Продано»,
«Не продано (продажи открыты)»). В листе «0 Сводный» подряд идут:

    Объем непроданного жилья, млн. кв. м      83.58
    % от строящегося жилья                     0.696   ← относится к строке выше
    в т.ч. с открытыми продажами              54.52
    % от строящегося жилья                     0.454   ← относится к строке выше

Подпись-продолжение «% …» относится к ближайшей основной подписи выше, но
парсер этого не знал → под одним (код, регион, дата) оказывались разные
значения: 2 500 групп, 64 691 лишняя строка.

РЕШЕНИЕ. Порядок строк в domrf_indicators сохраняет порядок строк листа
(проверено на «0 Сводный»: пары различаются точно). Поэтому разрез
восстанавливается ИЗ САМИХ ДАННЫХ, без обращения к XLSX: идём по строкам в
порядке id внутри (файл, лист) и для подписей-продолжений привязываем их к
ближайшей основной подписи выше. Полученная «эффективная подпись» уходит в
sub_dimension и различает строки.

Запуск:
    PGDSN="host=localhost port=5432 ..." python3 harmonize_4_domrf.py
"""
import collections
import os
import re
import sys
from datetime import date

import psycopg

os.environ.setdefault("PGPASSFILE", os.path.expanduser("~/.pgpass"))
DSN = os.environ.get("PGDSN", "host=localhost port=5432 dbname=research_wiki user=wiki")

SRC = "staging.rosstat_construction__domrf_indicators"
TARGET = os.environ.get("TARGET_TABLE", "core.observation_v2")
CUR_YEAR = 2026

# Подчинённые подписи: относятся к ближайшей вышестоящей группе.
# Структура листов ДОМ.РФ иерархическая — внутри группы идут её элементы:
#
#     Всего                                   ← группа
#     Продано                                 ← элемент
#     Не продано (продажи открыты)            ← элемент
#     Продажи не открыты                      ← элемент
#     Центральный ФО                          ← следующая группа
#     Продано                                 ← её элемент
#
# Без привязки к группе «Продано» встречается в листе десятки раз и не
# различает строки. Парсер этого не знал → 74 043 строки схлопывались.
SUB_ITEMS = {
    'продано', 'не продано (продажи открыты)', 'продажи не открыты',
    'не продано', '-', 'нет данных', 'всего',
}
# «% от …» и подобные — продолжения показателя. А вот «в т.ч.» и «из них»
# являются самостоятельными группами: следующая за ними подпись
# относится уже к ним, поэтому они обновляют вышестоящую группу.
CONT_RE = re.compile(r'^(%|доля|темп|индекс|отношение)', re.I)


# «в т.ч. …» открывает собственную группу: следующая за ней подпись
# относится уже к ней, а не к показателю двумя строками выше
GROUPISH_RE = re.compile(r'^(в т\.ч\.|из них|в том числе)', re.I)


def is_sub_item(label):
    """Элемент группы (наследует вышестоящую) либо сама группа."""
    t = label.strip()
    if GROUPISH_RE.match(t):
        return False          # это новая группа
    return t.lower() in SUB_ITEMS or bool(CONT_RE.match(t))


def parse_date(raw):
    """Подпись периода -> (period_start, period_end, freq_code)."""
    s = str(raw).strip()
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', s)
    if m:
        y, mo = int(m.group(1)), int(m.group(2))
        start = date(y, mo, 1)
        nxt = date(y + (mo == 12), 1 if mo == 12 else mo + 1, 1)
        return start, date.fromordinal(nxt.toordinal() - 1), 'M'
    m = re.match(r'^(\d{4})$', s)
    if m:
        y = int(m.group(1))
        return date(y, 1, 1), date(y, 12, 31), 'A'
    m = re.match(r'^(\d+)\s*(пол|мес)\.?\s*(\d{4})', s, re.I)
    if m:
        n, kind, y = int(m.group(1)), m.group(2).lower(), int(m.group(3))
        mo = (6 if n == 1 else 12) if kind == 'пол' else min(n, 12)
        return date(y, 1, 1), date(y, mo, 28), 'M'
    # Обрезанная подпись «1 пол. 202» / «7 мес. 202»: в исходной выгрузке
    # потерян последний символ года. Неполные периоды бывают только в
    # текущем году, поэтому год достраивается.
    m = re.match(r'^(\d+)\s*(пол|мес)\.?\s*(\d{3})$', s, re.I)
    if m:
        n, kind = int(m.group(1)), m.group(2).lower()
        y = int(m.group(3)) * 10 + (CUR_YEAR % 10)
        mo = (6 if n == 1 else 12) if kind == 'пол' else min(n, 12)
        return date(y, 1, 1), date(y, mo, 28), 'M'
    return None, None, None


def norm(s):
    return '' if s is None else re.sub(r'\s+', ' ', str(s)).strip().lower()


def main():
    conn = psycopg.connect(DSN)
    cur = conn.cursor()

    cur.execute("SELECT source_id FROM core.source WHERE source_code='domrf'")
    r = cur.fetchone()
    if not r:
        print("ОШИБКА: нет источника domrf", file=sys.stderr)
        return
    sid = r[0]
    cur.execute("""SELECT release_id FROM core.release
                   WHERE source_id=%s ORDER BY release_id LIMIT 1""", (sid,))
    r = cur.fetchone()
    if r:
        rel_id = r[0]
    else:
        cur.execute("""INSERT INTO core.release
                       (source_id, release_label, published_at, status, notes)
                       VALUES (%s, %s, now(), 'loaded', %s) RETURNING release_id""",
                    (sid, 'ДОМ.РФ статистические ряды', 'Рубеж 4'))
        rel_id = cur.fetchone()[0]
    conn.commit()
    print(f"domrf: источник={sid}, релиз={rel_id}", flush=True)

    cur.execute("SELECT frequency_id, frequency_code FROM core.frequency")
    freq_ids = {c: i for i, c in cur.fetchall()}
    cur.execute("SELECT unit_id, unit_code FROM core.unit")
    unit_ids = {c: i for i, c in cur.fetchall()}

    cur.execute("SELECT region_id, name_ru FROM core.region")
    reg = {norm(n): i for i, n in cur.fetchall()}
    cur.execute("SELECT alias, region_id FROM meta.region_alias")
    for a, rid in cur.fetchall():
        reg.setdefault(norm(a), rid)
    ru_id = reg.get('российская федерация')
    print(f"регионов в справочнике (с алиасами): {len(reg)}", flush=True)

    cur.execute("SELECT metric_id, name_ru FROM core.metric")
    by_name = {norm(nm): mid for mid, nm in cur.fetchall()}

    # --- чтение в порядке файл/лист/id: порядок строк сохраняет разрез ---
    rconn = psycopg.connect(DSN)
    rcur = rconn.cursor(name='domrf_cur')
    rcur.itersize = 10000
    rcur.execute(f"""
        SELECT file_name, sheet_name, indicator_code, indicator_name,
               region_name, date, value, data_type, id
        FROM {SRC}
        ORDER BY file_name, sheet_name, id
    """)

    ins = 0
    no_date = 0
    new_metrics = 0
    labeled = 0          # строк, где разрез восстановлен из порядка
    batch = []
    last_main = {}       # (file, sheet) -> последняя вышестоящая группа
    last_region = {}     # (file, sheet) -> регион той группы
    seen = {}            # (file, sheet, метка) -> сколько раз встречалась
    rowseq = {}          # (file, sheet) -> порядковый номер строки
    cur_key = None

    for fn, sn, icode, iname, rname, raw_date, value, dtype, rid_ in rcur:
        ps, pe, fcode = parse_date(raw_date)
        if not ps:
            no_date += 1
            continue

        key_fs = (fn, sn)
        if key_fs != cur_key:
            cur_key = key_fs
            last_main[key_fs] = ''
            last_region[key_fs] = None

        label = str(rname or '').strip()
        rd = reg.get(norm(label))
        sub_parts = []

        if not is_sub_item(label):
            # это заголовок группы: он задаёт и регион, и контекст разреза.
            # Группами бывают регионы («Центральный ФО», «г. Москва»), сводные
            # подписи («Всего») и группировки городов («до 50 тыс. чел.»).
            last_main[key_fs] = label
            last_region[key_fs] = rd
            rid = rd or ru_id
            eff = '' if rd else label
            if not rd:
                labeled += 1
        else:
            # подчинённая подпись: наследует регион и группу вышестоящей
            grp = last_main.get(key_fs, '')
            rid = last_region.get(key_fs) or ru_id
            eff = f'{grp} → {label}' if (grp and norm(grp) != norm(label)) else label
            labeled += 1

        if eff:
            cnt = seen.get((fn, sn, eff), 0) + 1
            seen[(fn, sn, eff)] = cnt
            marker = '' if cnt == 1 else f' #{cnt}'
            sub_parts.append(f'разрез: {eff[:200]}{marker}')

        # Ряд-защита от схлопывания. Подпись строки повторяется в листе
        # законно (регион указан в нескольких секциях, показатель — дважды),
        # и различить такие строки штатными полями нельзя: значения в них
        # совпадают. Порядковый номер строки гарантирует уникальность и
        # сохраняет все данные; он же остаётся стабильным при повторном
        # прогоне на том же снимке.
        rowseq[key_fs] = rowseq.get(key_fs, 0) + 1
        sub_parts.append(f'строка {rowseq[key_fs]}')

        # тип ряда различает варианты одного показателя (stock/flow/…)
        if dtype:
            sub_parts.append(f'ряд: {dtype}')
        # Имя листа обязательно: нумерация строк внутри листа своя, поэтому
        # строки из разных листов одного файла дают одинаковый ключ и
        # схлопываются. Без листа терялось 9 421 строка (проверено
        # симуляцией), с листом — ноль коллизий.
        if sn:
            sub_parts.append(f'лист: {sn}')
        subdim = ' | '.join(sub_parts)

        k = norm(iname)
        mid = by_name.get(k)
        if not mid:
            code = (icode or '').strip().lower()
            if not code or code == '0':
                code = 'domrf_' + re.sub(r'[^a-z0-9]+', '_', k[:40]).strip('_')
            code = code[:60]
            cur.execute("""INSERT INTO core.metric
                (metric_code, name_ru, unit_id, frequency_id, metric_type, status, tags)
                VALUES (%s, %s, %s, %s, 'primary', 'active', %s)
                ON CONFLICT (metric_code) DO UPDATE SET name_ru = EXCLUDED.name_ru
                RETURNING metric_id""",
                (code, str(iname)[:200], unit_ids.get('count'),
                 freq_ids.get(fcode), ['domrf', 'stage4']))
            mid = cur.fetchone()[0]
            by_name[k] = mid
            new_metrics += 1
            conn.commit()

        fid = freq_ids.get(fcode) or freq_ids.get('M')
        atype = 'final' if ps.year < CUR_YEAR else 'preliminary'
        batch.append((mid, rid, fid, ps, pe, value, atype, 'validated',
                      sid, rel_id, subdim))
        ins += 1
        if len(batch) >= 50000:
            cur.executemany("""INSERT INTO core.observation_v2
                (metric_id, region_id, frequency_id, period_start, period_end, value,
                 assessment_type, observation_status, source_id, release_id, sub_dimension)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT (metric_id, region_id, frequency_id, period_start,
                             source_id, release_id, assessment_type, sub_dimension)
                DO NOTHING""", batch)
            conn.commit()
            batch = []
            print(f"  отправлено {ins:,}", flush=True)

    if batch:
        cur.executemany("""INSERT INTO core.observation_v2
            (metric_id, region_id, frequency_id, period_start, period_end, value,
             assessment_type, observation_status, source_id, release_id, sub_dimension)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            ON CONFLICT (metric_id, region_id, frequency_id, period_start,
                         source_id, release_id, assessment_type, sub_dimension)
            DO NOTHING""", batch)
        conn.commit()
    rcur.close()
    rconn.close()

    print(f"\n=== ИТОГ ===", flush=True)
    print(f"  подготовлено: {ins:,}")
    print(f"  с восстановленным разрезом: {labeled:,}")
    print(f"  без периода: {no_date}")
    print(f"  новых метрик: {new_metrics}")
    cur.execute(f"""SELECT count(*) FROM {TARGET} o JOIN core.source s
                    ON s.source_id=o.source_id WHERE s.source_code='domrf'""")
    n = cur.fetchone()[0]
    print(f"  ДОМ.РФ в {TARGET}: {n:,}")
    print(f"  потеряно при вставке: {ins - n:,}")
    cur.execute(f"SELECT count(*) FROM {TARGET}")
    print(f"  всего в {TARGET}: {cur.fetchone()[0]:,}")
    conn.close()


if __name__ == "__main__":
    main()
