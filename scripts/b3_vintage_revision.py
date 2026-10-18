#!/usr/bin/env python3
"""B-3: переход таблицы 2.6 на свежую ревизию (издание 2024 года).

Сборники пересекаются: в приложении 2024 года есть и 2005-2021. Раньше год
закреплялся за самым РАННИМ сборником (2005-2021 — издание 2022, 2022-2023 —
2024), из-за чего на стыке 2021/2022 в ряду образовывался разрыв уровня.
Решение владельца (18.10.2026): основной ряд — свежая ревизия, прежняя остаётся
в каноне отдельной версией.

Как разделяются версии: обе строки остаются assessment_type='final' (это два
опубликованных издания, а не «предварительные» и «уточнённые» значения), а
принадлежность к изданию пишется в подразрез меткой «vintage: издание 2022»
или «vintage: издание 2024». Различить их можно и по release_id, но метка нужна
читателю, который смотрит на подразрез, а не на релиз.

Режимы: без APPLY — только сверка и статистика ревизии; APPLY=1 — запись.
Точка возврата: дамп изменяемых строк релиза 13 в attic/.

Регион определяется сопоставлением значений: старая строка файла отождествляется
с канонической по совпадению всего вектора значений 2005-2021, а не по написанию
названия (в сборниках встречаются «Архангельская область без НАО» и подобные).
"""
import csv
import gzip
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as t

NEW = '/tmp/revis/R_10_2_3_pril.xlsx'      # издание 2024
OLD = '/tmp/revis/old_2022.xlsx'           # издание 2022
METRIC = 'y477140044'
REL_OLD, REL_NEW = 13, 14
YEARS = list(range(2005, 2022))
UNIT_SUB = 'ед.: Тысяч человек'
VINT_OLD = ' | vintage: издание 2022'
VINT_NEW = ' | vintage: издание 2024'
APPLY = os.environ.get('APPLY') == '1'


def norm(v):
    return re.sub(r'\s+', ' ', str(v)).strip()


def num(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(',', '.')
    if not s or s in ('-', '–', '—'):
        return None
    return float(s) if re.match(r'^-?\d+(\.\d+)?$', s) else None


def table(path):
    """Строки таблицы 2.6: (название территории, {год: значение})."""
    import openpyxl
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = next(w for w in wb.worksheets if w.title.strip().startswith('2.6'))
    rows = list(ws.iter_rows(values_only=True))
    wb.close()
    hdr, years = None, {}
    for i, r in enumerate(rows[:8]):
        found = {c: int(str(v).strip().split('.')[0]) for c, v in enumerate(r or ())
                 if v is not None and re.fullmatch(r'(20\d{2})(\.0)?', str(v).strip())}
        if len(found) >= 3:
            hdr, years = i, found
            break
    start = next((i for i, r in enumerate(rows)
                  if r and str(r[0] or '').strip().lower().startswith('российская федерация')), None)
    out = []
    for r in rows[start:]:
        name = norm(r[0]) if r and r[0] else ''
        if not name or name.startswith('1)') or name.lower().startswith('по данным'):
            break
        if name.endswith(':') or name.lower() in ('в том числе', 'из них', 'итого'):
            continue
        out.append((name, {y: num(r[c]) if c < len(r) else None for c, y in years.items()}))
    return out


def canon():
    """Канонические строки релиза 13: {(region_id, sub): {год: значение}}."""
    rows = t.query("""SELECT o.region_id, o.sub_dimension, date_part('year', o.period_start)::int, o.value
        FROM data.observation o JOIN core.metric m ON m.metric_id=o.metric_id
        WHERE m.metric_code=%s AND o.release_id=%s AND o.assessment_type='final'""", (METRIC, REL_OLD))
    data = {}
    for rid, sub, y, v in rows:
        data.setdefault((rid, sub), {})[int(y)] = float(v)
    return data


def main():
    new_rows = table(NEW)
    old_rows = table(OLD)
    can = canon()
    print('файл 2024: строк %d | файл 2022: строк %d | канонических строк релиза 13: %d'
          % (len(new_rows), len(old_rows), len(can)))

    # сопоставление старой строки файла с канонической по вектору значений
    index = {}
    for key, series in can.items():
        fp = tuple(sorted((y, round(v, 6)) for y, v in series.items() if 2005 <= y <= 2021))
        index.setdefault(fp, []).append(key)
    match, unmatched, ambiguous = {}, [], []
    for name, series in old_rows:
        fp = tuple(sorted((y, round(v, 6)) for y, v in series.items()
                          if 2005 <= y <= 2021 and v is not None))
        cand = [k for k in index.get(fp, []) if k[1].startswith(UNIT_SUB)]
        if len(cand) == 1:
            match[name] = cand[0]
        elif not cand:
            unmatched.append(name)
        else:
            ambiguous.append(name)
    print('сопоставлено строк: %d | не сопоставлено: %d | неоднозначно: %d'
          % (len(match), len(unmatched), len(ambiguous)))
    if unmatched:
        print('   примеры не сопоставленных:', unmatched[:3])
    if ambiguous:
        print('   примеры неоднозначных:', ambiguous[:3])

    # ревизия: значение издания 2024 против канона (издание 2022)
    pairs = []
    for name, series in new_rows:
        key = match.get(name)
        if key is None:
            continue
        for y, v in series.items():
            if y in YEARS and v is not None and y in can[key]:
                pairs.append((key[0], key[1], y, can[key][y], v))
    diffs = [(a, b) for *_, a, b in pairs if abs(a - b) > 1e-9]
    rel = sorted(abs(b - a) / abs(a) for a, b in diffs if a)
    print('сверено точек: %d | расходятся: %d (%.1f %%)' % (len(pairs), len(diffs),
                                                            100.0 * len(diffs) / max(1, len(pairs))))
    if rel:
        mid = rel[len(rel) // 2]
        print('   медиана расхождения: %.1f %% | максимум: %.1f %% | больше 5 %%: %d точек'
              % (100 * mid, 100 * rel[-1], sum(1 for x in rel if x > 0.05)))

    if not APPLY:
        print('\nсухой прогон: запись не выполнялась (APPLY=1 для записи)')
        return 0

    os.makedirs('attic', exist_ok=True)
    with gzip.open('attic/b3_rel13_before.csv.gz', 'wt', newline='') as fh:
        wr = csv.writer(fh)
        wr.writerow(['region_id', 'sub_dimension', 'year', 'value'])
        for (rid, sub), series in can.items():
            for y, v in sorted(series.items()):
                wr.writerow([rid, sub, y, v])
    print('дамп релиза 13: attic/b3_rel13_before.csv.gz')

    # 1) прежнее издание помечается меткой версии
    n_old = t.execute("""UPDATE data.observation o SET sub_dimension = o.sub_dimension || %s
        FROM core.metric m WHERE m.metric_id=o.metric_id AND m.metric_code=%s
          AND o.release_id=%s AND o.sub_dimension LIKE %s AND o.sub_dimension NOT LIKE %s""",
                      (VINT_OLD, METRIC, REL_OLD, UNIT_SUB + '%', '%vintage:%'))
    print('помечено прежнее издание: строк %d' % n_old)

    # 2) строки издания 2024 за пересекающиеся годы
    mid = t.query("SELECT metric_id FROM core.metric WHERE metric_code=%s", (METRIC,))[0][0]
    ins = skipped = 0
    for rid, sub, y, _old_v, v in pairs:
        new_sub = sub + VINT_NEW
        done = t.execute("""INSERT INTO data.observation
              (metric_id, region_id, period_start, frequency_id, assessment_type, sub_dimension, release_id, value)
            SELECT %s,%s,%s,f.frequency_id,'final',%s,%s,%s FROM catalog.frequency f WHERE f.frequency_code='A'
            ON CONFLICT ON CONSTRAINT ux_observation DO NOTHING""",
                         (mid, rid, '%d-01-01' % y, new_sub, REL_NEW, v))
        ins += done
        skipped += 0 if done else 1
    print('вставлено строк издания 2024: %d | пропущено существующих: %d' % (ins, skipped))
    return 0


if __name__ == '__main__':
    sys.exit(main())
