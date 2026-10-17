#!/usr/bin/env python3
"""Решение владельца (17.10.2026): свести региональную группу ИКВ к одному релизу
и снять дубль-карточку.

Состояние до операции — группа лежала тремя наборами:

  * `iokmrrk`  (metric_id 482, 2 400 строк) — релиз 1 «Срез Росстата на 17.09.2026
    (перенос из SQLite)»; подразрез несёт метки накопления и состава
    («накопительно: I полугодие | состав: …»);
  * `iokmrrkri` (metric_id 59561, 2 400 строк) — релиз 76 `rosstat_inv_reg_kv`,
    «Рубеж 6: первичный источник»; тот же ряд, что у 482 (мультимножество
    «регион — период — значение» совпадает 2 400 из 2 400), подразрез беднее —
    2 100 строк с пустым подразрезом, 300 строк с одними метками состава;
  * `iokspr`   (metric_id 1927, 2 400 строк) — релиз 77
    `rosstat_inv_reg_kv_2020-2026_pct`.

Операция (одна транзакция):

  1. релиз 76 переименовывается в `rosstat_inv_reg_kv_2020-2026` — целевой
     релиз группы;
  2. `iokmrrk` переводится из релиза 1 в релиз 76;
  3. `iokspr` переводится из релиза 77 в релиз 76;
  4. строки карточки-дубля `iokmrrkri` удаляются (значения полностью
     перекрыты `iokmrrk`), сама карточка гасится (status='inactive');
  5. осиротевший релиз 77 удаляется.

Точка возврата: `attic/ikv_reg_merge_before_<метка>.csv.gz` (строки трёх
метрик до операции) плюс тег `pre-ikv-merge-<метка>` в репозитории.
Дамп не перезаписывается: имя включает метку времени прогона.

Запуск: `APPLY=1 python3 scripts/merge_ikv_releases.py` (без APPLY — только
отчёт о состоянии, без записи).
"""

import csv
import gzip
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel as tunnel  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MLN_ID, PCT_ID, DUP_ID = 482, 1927, 59561
SRC_REL_MLN, SRC_REL_PCT, TARGET_REL, DROP_REL = 1, 77, 76, 77
NEW_LABEL = 'rosstat_inv_reg_kv_2020-2026'
NOTE = ('Росстат: Inv_reg_kv_2020-2026.xlsx — объединение трёх наборов '
        '(перенос из SQLite + два релиза рубежа 6), 17.10.2026')
CARD_NOTE = ('дубль iokmrrk (482), 2 400 из 2 400 значений совпадают; строки сняты '
             '17.10.2026, релиз объединён в rosstat_inv_reg_kv_2020-2026')


def stamp():
    return datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')


def dump(path):
    """Дамп строк трёх метрик (все колонки) — точка возврата."""
    cols = [c[0] for c in tunnel.query(
        "SELECT column_name FROM information_schema.columns "
        "WHERE table_schema='data' AND table_name='observation' ORDER BY ordinal_position")]
    rows = tunnel.query(
        "SELECT %s FROM data.observation WHERE metric_id IN (%%s,%%s,%%s) "
        "ORDER BY metric_id, region_id, period_start, sub_dimension" % ','.join(cols),
        (MLN_ID, PCT_ID, DUP_ID))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, 'wt', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in rows:
            w.writerow(r)
    return len(rows), cols


def state():
    out = {}
    for code, mid in (('iokmrrk', MLN_ID), ('iokmrrkri', DUP_ID), ('iokspr', PCT_ID)):
        out[code] = tunnel.query(
            "SELECT o.release_id, count(*) FROM data.observation o "
            "WHERE o.metric_id=%s GROUP BY 1 ORDER BY 1", (mid,))
    return out


def cross_dupes():
    """Строки iokmrrkri, не перекрытые iokmrrk по (регион, период, значение)."""
    return tunnel.query("""
        WITH a AS (SELECT region_id, period_start, value FROM data.observation WHERE metric_id=%s),
             b AS (SELECT region_id, period_start, value FROM data.observation WHERE metric_id=%s)
        SELECT (SELECT count(*) FROM (SELECT * FROM b EXCEPT SELECT * FROM a) x),
               (SELECT count(*) FROM (SELECT * FROM a EXCEPT SELECT * FROM b) y),
               (SELECT count(*) FROM b)""", (MLN_ID, DUP_ID))[0]


def main():
    apply = os.environ.get('APPLY') == '1'
    print('=== ДО ===')
    for code, st in state().items():
        print('  %-9s %s' % (code, st))
    only_b, only_a, n_b = cross_dupes()
    print('  перекрытие iokmrrkri → iokmrrk: строк у дубля %d, не найдено в каноне %d, '
          'только в каноне %d' % (n_b, only_b, only_a))
    if only_b:
        sys.exit('СТОП: у карточки-дубля %d строк без пары — это не полный дубль' % only_b)

    rel = tunnel.query("SELECT release_id, label, notes FROM catalog.release "
                       "WHERE release_id IN (%s,%s)", (SRC_REL_MLN, DROP_REL))
    print('  релизы под перенос: %s' % rel)
    foreign = tunnel.query("SELECT count(*) FROM data.observation WHERE release_id=%s "
                           "AND metric_id NOT IN (%s,%s)", (DROP_REL, DUP_ID, PCT_ID))[0][0]
    if foreign:
        sys.exit('СТОП: в релизе %s есть чужие метрики (%d строк)' % (DROP_REL, foreign))

    if not apply:
        print('\nСухой прогон. Запись — APPLY=1.')
        return

    tag = stamp()
    path = os.path.join(REPO, 'attic', 'ikv_reg_merge_before_%s.csv.gz' % tag)
    n, cols = dump(path)
    print('\nточка возврата: %s (%d строк, %d колонок)' % (path, n, len(cols)))

    conn = tunnel.connect()
    try:
        with conn.cursor() as cur:
            cur.execute("UPDATE catalog.release SET label=%s, notes=%s WHERE release_id=%s",
                        (NEW_LABEL, NOTE, TARGET_REL))
            print('  релиз %s → %r: %d' % (TARGET_REL, NEW_LABEL, cur.rowcount))
            cur.execute("UPDATE data.observation SET release_id=%s "
                        "WHERE metric_id=%s AND release_id=%s", (TARGET_REL, MLN_ID, SRC_REL_MLN))
            print('  iokmrrk  → релиз %s: %d строк' % (TARGET_REL, cur.rowcount))
            cur.execute("UPDATE data.observation SET release_id=%s "
                        "WHERE metric_id=%s AND release_id=%s", (TARGET_REL, PCT_ID, SRC_REL_PCT))
            print('  iokspr   → релиз %s: %d строк' % (TARGET_REL, cur.rowcount))
            cur.execute("DELETE FROM data.observation WHERE metric_id=%s", (DUP_ID,))
            print('  iokmrrkri снят: %d строк' % cur.rowcount)
            cur.execute("DELETE FROM catalog.release WHERE release_id=%s", (DROP_REL,))
            print('  релиз %s удалён: %d' % (DROP_REL, cur.rowcount))
            cur.execute("UPDATE catalog.metric SET status='inactive', "
                        "description=coalesce(description||' | ','')||%s WHERE metric_id=%s",
                        (CARD_NOTE, DUP_ID))
            print('  карточка %s погашена: %d' % (DUP_ID, cur.rowcount))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

    print('\n=== ПОСЛЕ ===')
    for code, st in state().items():
        print('  %-9s %s' % (code, st))
    print('  релизы группы: %s' % tunnel.query(
        "SELECT r.release_id, r.label, count(*) FROM data.observation o "
        "JOIN catalog.release r USING(release_id) WHERE o.metric_id IN (%s,%s) "
        "GROUP BY 1,2", (MLN_ID, PCT_ID)))
    print('  всего наблюдений: %s' % tunnel.query(
        "SELECT count(*) FROM data.observation")[0][0])
    print('\nТочка возврата: %s' % path)


if __name__ == '__main__':
    main()
