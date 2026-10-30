#!/usr/bin/env python3
"""Связность `catalog.metric_definition`: цепочка версий и пустые единицы.

Два дефекта, оба видны запросом и оба ломают «какая редакция текущая»:

1. `supersedes` пуст у всех строк, хотя у 23 кодов по 2–3 редакции. Без связи
   текущая редакция определяется догадкой (`max(version)` / статусом), а не
   историей. Формат ссылки — `<metric_code>@<version>`.
2. Три ручные редакции (`okb`, `pzk`, `zka`) заведены без единицы, хотя у самой
   метрики `unit_id` = 29 (`шт.`): определяется по `catalog.unit.name_ru`, а если
   у метрики единицы нет — пишется явное «единица не определена источником»,
   чтобы пустота не выглядела как забывчивость.

Идемпотентность: `--check` ничего не пишет; `--apply` трогает только строки, где
`supersedes IS NULL AND version > 1` и где `unit_canonical` пуст, поэтому
повторный прогон даёт 0 изменений.
"""
import argparse
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402

NO_UNIT = 'единица не определена источником'

SQL_CHAIN = """
SELECT metric_code, version, status, supersedes
FROM catalog.metric_definition
ORDER BY metric_code, version
"""

SQL_UNITS = """
SELECT d.definition_id, d.metric_code, u.name_ru, u.unit_code
FROM catalog.metric_definition d
LEFT JOIN catalog.metric m ON m.metric_id = d.metric_id
LEFT JOIN catalog.unit u ON u.unit_id = m.unit_id
WHERE d.unit_canonical IS NULL OR d.unit_canonical = ''
ORDER BY d.metric_code
"""


def plan_chain(rows):
    """[(code, version)] строк, которым нужен supersedes → ссылка на предыдущую."""
    by_code = {}
    for code, version, status, sup in rows:
        by_code.setdefault(code, []).append((version, sup))
    todo = []
    for code, vers in by_code.items():
        present = {v for v, _ in vers}
        for version, sup in sorted(vers):
            if version > 1 and not sup:
                prev = version - 1
                if prev in present:
                    todo.append((code, version, f'{code}@{prev}'))
    return todo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()

    rows = db_tunnel.query(SQL_CHAIN)
    chain_todo = plan_chain([(r[0], r[1], r[2], r[3]) for r in rows])
    codes_multi = {}
    for code, version, status, sup in rows:
        codes_multi.setdefault(code, 0)
        codes_multi[code] += 1
    n_multi = sum(1 for c, k in codes_multi.items() if k > 1)
    print(f'строк: {len(rows)}, кодов: {len(codes_multi)}, кодов с >1 редакцией: {n_multi}')
    print(f'нужно заполнить supersedes: {len(chain_todo)}')
    for t in chain_todo[:5]:
        print('  ', t)

    units = db_tunnel.query(SQL_UNITS)
    print(f'пустых единиц: {len(units)}')
    unit_todo = []
    for did, code, name_ru, ucode in units:
        unit_todo.append((did, (name_ru or '').strip() or NO_UNIT))
    for t in unit_todo[:5]:
        print('  ', t)

    if not args.apply:
        print('режим --check: записи не выполнялись')
        return 0

    conn = db_tunnel.connect()
    try:
        with conn.cursor() as cur:
            for code, version, link in chain_todo:
                cur.execute("""UPDATE catalog.metric_definition
                               SET supersedes = %s, updated_at = now()
                               WHERE metric_code = %s AND version = %s
                                 AND supersedes IS NULL""", (link, code, version))
            n_chain = 0 if cur.rowcount < 0 else cur.rowcount
            for did, unit in unit_todo:
                cur.execute("""UPDATE catalog.metric_definition
                               SET unit_canonical = %s, updated_at = now()
                               WHERE definition_id = %s
                                 AND (unit_canonical IS NULL OR unit_canonical = '')""", (unit, did))
            n_units = cur.rowcount
        conn.commit()
    finally:
        conn.close()
    print(f'обновлено supersedes: {n_chain}, единиц: {n_units}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
