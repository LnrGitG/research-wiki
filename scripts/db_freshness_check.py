#!/usr/bin/env python3
"""Ежедневный сторож свежести на единой схеме (catalog + data + ops).

Два слоя:

1. **Движок** — `ops.check_freshness()` (PL/pgSQL). Снимает снимок свежести
   по всем активным метрикам `catalog.metric` через `derived.v_metric_context`,
   где пороги привязаны к частоте ряда (D=10, W=25, M=75, Q=160, A=550 дней).
   Пишет в `ops.freshness_snapshot`, поднимает алерты в `ops.alert` при
   переходе из «свежие» в «отстают»/«устарели» (подавление повторов — 3 дня).

2. **Отчёт** — этот скрипт. Читает свежий снимок, сводит по источнику
   (`catalog.source`) и формирует JSON в stdout: для каждого источника —
   доля свежих/отстающих/устаревших метрик, худший лаг, статус.
   Источники вне пороговой логики (imf — прогнозные ряды) пропускаются.

Пороги по частоте заданы в `derived.v_metric_context` (CASE по freq_code).
Перенастройка порогов — правкой представления, а не этого скрипта.

Доступ к БД: scripts/db_tunnel.py (тоннель 15432).

История: до переезда на схему data скрипт опрашивал `core.observation_v2`
с порогами по источнику, зашитыми в BLOCKS. После переезда `core.*` стали
представлениями над `catalog.*` + `data.observation`, а в БД появилась
готовая инфраструктура `ops.check_freshness()` с покруговой гранулярностью.
Ревизия 3 (05.10.2026): переход на ops-движок, no_agent-режим cron.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from db_tunnel import query, execute
except Exception:
    query = execute = None

SKIP_SOURCES = {'imf'}  # прогнозные ряды — вне пороговой логики


def main():
    if query is None:
        print(json.dumps({'status': 'error',
                          'reason': 'db_tunnel недоступен'}))
        return 1

    # 1. снять свежий снимок через ops-движок
    try:
        n = query("SELECT ops.check_freshness()")[0][0]
    except Exception as e:
        print(json.dumps({'status': 'error',
                          'reason': 'ops.check_freshness: %s' % str(e)[:200]}))
        return 1

    # 2. сводка по источнику из свежего снимка
    rows = query("""
        SELECT s.source_code,
               count(*)                                         AS metrics,
               count(*) FILTER (WHERE f.freshness = 'свежие')    AS fresh,
               count(*) FILTER (WHERE f.freshness = 'отстают')   AS lagging,
               count(*) FILTER (WHERE f.freshness = 'устарели')  AS stale,
               count(*) FILTER (WHERE f.freshness = 'нет данных') AS nodata,
               max(f.last_observation)                           AS last_period,
               max(f.days_stale)                                 AS worst_lag
        FROM ops.freshness_snapshot f
        JOIN catalog.metric  m ON m.metric_id = f.metric_id
        JOIN catalog.source  s ON s.source_id = m.source_id
        WHERE f.snapshot_at = (SELECT max(snapshot_at) FROM ops.freshness_snapshot)
        GROUP BY 1
        ORDER BY 2 DESC
    """)

    out, problems = {}, 0
    for (src, total, fresh, lagging, stale, nodata,
         last_period, worst_lag) in rows:
        if src in SKIP_SOURCES:
            continue
        bad = (lagging or 0) + (stale or 0) + (nodata or 0)
        status = 'ok' if bad == 0 else 'issues'
        out[src] = {
            'metrics': total,
            'fresh': fresh or 0,
            'lagging': lagging or 0,
            'stale': stale or 0,
            'nodata': nodata or 0,
            'last_period': str(last_period) if last_period else None,
            'worst_lag_days': worst_lag,
            'status': status,
        }
        if status != 'ok':
            problems += 1

    # 3. недоставленные алерты
    alerts = query("""
        SELECT count(*) FROM ops.alert
        WHERE kind = 'freshness' AND delivered_at IS NULL
    """)[0][0]

    out['_summary'] = {
        'status': 'ok' if problems == 0 else 'issues',
        'problem_sources': problems,
        'snapshot_rows': n,
        'pending_alerts': alerts,
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())