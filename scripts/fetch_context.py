#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fetch_context.py — быстрый контекст из БД по текстовому запросу.

Вызывает ops.fetch_context() в PostgreSQL, которая:
  1. Распознаёт регион через meta.region_alias (Башкортостан, Москва, etc.)
  2. Извлекает ключевые слова, применяет stem-обрезку (left-5) для падежей
  3. Ищет active-метрики через ILIKE + pg_trgm
  4. Ранжирует по числу совпавших слов и релевантности
  5. Возвращает наблюдения (метрика, регион, период, значение)

Использование:
  python3 scripts/fetch_context.py "приросты по вкладам по Башкортостану за 3 месяца"
  python3 scripts/fetch_context.py "ключевая ставка" --limit 3 --n-values 4

Вывод: компактный текст для вставки в диалог агента.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'scripts'))
from db_tunnel import query


def main():
    ap = argparse.ArgumentParser(description="Контекст из БД по текстовому запросу")
    ap.add_argument('query', help='Текстовый запрос на русском')
    ap.add_argument('--limit', type=int, default=5, help='Макс. метрик (по умолч. 5)')
    ap.add_argument('--n-values', type=int, default=6, help='Значений на метрику (по умолч. 6)')
    ap.add_argument('--json', action='store_true', help='Вывод в JSON')
    a = ap.parse_args()

    rows = query("SELECT * FROM ops.fetch_context(%s, %s, %s)", (a.query, a.limit, a.n_values))

    if not rows:
        print(f"Ничего не найдено по запросу: {a.query}")
        return 1

    if a.json:
        import json
        results = []
        seen = set()
        for r in rows:
            mid = r[0]
            if mid not in seen:
                seen.add(mid)
                results.append({
                    'metric_id': r[0], 'metric_code': r[1], 'metric_name': r[2],
                    'source': r[3], 'frequency': r[4], 'unit': r[5],
                    'n_obs': r[11], 'last_obs': str(r[12]) if r[12] else None,
                    'relevance': r[13], 'matched_words': r[14],
                    'values': []
                })
            idx = list(seen).index(mid)
            if r[10] is not None:
                results[idx]['values'].append({
                    'region': r[7], 'period_start': str(r[8]), 'period_end': str(r[9]),
                    'value': float(r[10])
                })
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    # Текстовый вывод
    seen_metrics = {}
    for r in rows:
        mid = r[0]
        if mid not in seen_metrics:
            seen_metrics[mid] = {
                'code': r[1], 'name': r[2], 'source': r[3], 'freq': r[4],
                'unit': r[5], 'n_obs': r[11], 'relevance': r[13], 'mw': r[14],
                'values': []
            }
        if r[10] is not None:
            seen_metrics[mid]['values'].append((r[7], r[8], r[10]))

    print(f"Запрос: {a.query}")
    print(f"Найдено метрик: {len(seen_metrics)}\n")
    for i, (mid, m) in enumerate(seen_metrics.items(), 1):
        print(f"{i}. {m['name'][:70]}  [{m['code']}]")
        print(f"   src={m['source']} freq={m['freq']} unit={m['unit']} "
              f"n_obs={m['n_obs']} rel={m['relevance']:.1f} mw={m['mw']}")
        for region, period, val in m['values']:
            print(f"   {region}: {period} = {val}")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())