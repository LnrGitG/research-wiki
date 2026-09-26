#!/usr/bin/env python3
"""Проверка дублей рядов в БД v2: ищем пары метрик, значения которых совпадают
на общих периодах (в первую очередь национальный уровень, region_id=1).

Мотив: инцидент 26.09.2026 — vmd (vfs_mortgage_debt) нёс ряд zkf (кредиты
физлицам) из-за коллизии меток в scripts/parse_cbr_lending.py. Такой дубль
не виден ни в отчётах, ни в валидации типов, только сравнением рядов.

Запуск: python3 scripts/check_metric_duplicates.py [--region 1] [--min-share 0.95] [--min-points 6]
"""
import argparse
import collections
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_tunnel  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--region', type=int, default=1, help='region_id (1 = РФ)')
    ap.add_argument('--min-share', type=float, default=0.95, help='минимальная доля совпадающих точек')
    ap.add_argument('--min-points', type=int, default=6, help='минимум общих периодов для вывода')
    ap.add_argument('--freq', type=int, default=None, help='ограничить частоту (5 = месяц)')
    args = ap.parse_args()

    db_tunnel.connect()
    sql = """SELECT m.metric_code, o.period_start::date, o.value::numeric(24,6)
             FROM core.observation_v2 o JOIN core.metric m USING (metric_id)
             WHERE o.region_id = %s AND o.sub_dimension = ''
               AND m.status <> 'deprecated'"""
    params = [args.region]
    if args.freq is not None:
        sql += " AND o.frequency_id = %s"
        params.append(args.freq)
    rows = db_tunnel.query(sql + " ORDER BY m.metric_code, o.period_start", tuple(params))

    series = collections.defaultdict(dict)
    for code, period, value in rows:
        series[code][period] = value

    codes = sorted(series)
    flagged = []
    for i, a in enumerate(codes):
        for b in codes[i + 1:]:
            common = set(series[a]) & set(series[b])
            if len(common) < args.min_points:
                continue
            eq = sum(1 for p in common if series[a][p] == series[b][p])
            share = eq / len(common)
            if share >= args.min_share:
                flagged.append((share, len(common), a, b))

    print(f'регион {args.region}: метрик {len(codes)}, пар с совпадением >= {args.min_share:.0%} '
          f'на >= {args.min_points} общих точках: {len(flagged)}')
    for share, n, a, b in sorted(flagged, reverse=True):
        vals = sorted(set(series[a].values()))
        sample = f'{vals[0]} … {vals[-1]}' if len(vals) > 1 else str(vals[0])
        print(f'  {share*100:5.1f}% ({n:>3} точек)  {a:22} == {b:22} значения: {sample}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())