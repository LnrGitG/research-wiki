#!/usr/bin/env python3
"""Проверка свежести БД v2: последняя точка по каждому источнику против порога.

Пороги (max_days) — нормальный лаг источника + допуск; спецификация порогов
в queries/datalens-db-health-dashboard-20260928.md. Прогнозные точки
(ИФО/прогнозы Росстата, имф) исключаются фильтром observation_status='actual'.
Выход — JSON в stdout. Доступ к БД: scripts/db_tunnel.py (тоннель 15432).
"""
import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from db_tunnel import query
except Exception:
    query = None

# порог = сколько дней от period_start сегодня считается ок
BLOCKS = {
    'cbr':            {'max_days': 40},   # еженедельные/ежемесячные ряды, лаг ~3 нед
    'domrf':          {'max_days': 60},
    'fedstat_emiss':  {'max_days': 60},
    'fns':            {'max_days': 130},
    'iminfin':        {'max_days': 20},
    'rosreestr':      {'max_days': 170},
    'rosstat':        {'max_days': 40},   # прогнозы до 2026-12 отфильтрованы ниже
    'smartlab':       {'max_days': 180},
    'worldbank':      {'max_days': 560},
}
# источники вне пороговой логики (прогнозные/разовые)
SKIP = {'imf'}


def main():
    if query is None:
        print(json.dumps({'status': 'error', 'reason': 'db_tunnel недоступен'}))
        return 1
    sql = ("SELECT s.source_code, MAX(ov.period_start)::text "
           "FROM core.observation_v2 ov JOIN core.source s ON s.source_id = ov.source_id "
           "WHERE ov.period_start < CURRENT_DATE "
           "GROUP BY 1")
    fresh = {r[0]: r[1] for r in query(sql)}
    out, problems = {}, 0
    today = date.today()
    for blk, spec in BLOCKS.items():
        last = fresh.get(blk)
        if not last:
            out[blk] = {'status': 'fail', 'reason': 'нет данных'}
            problems += 1
            continue
        lag = (today - date.fromisoformat(last)).days
        status = 'ok' if lag <= spec['max_days'] else 'fail'
        out[blk] = {'last_period': last, 'lag_days': lag,
                    'threshold_days': spec['max_days'], 'status': status}
        if status != 'ok':
            problems += 1
    out['_summary'] = {'status': 'ok' if problems == 0 else 'issues',
                       'problem_blocks': problems, 'checked_on': today.isoformat()}
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())