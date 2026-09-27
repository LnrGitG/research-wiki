#!/usr/bin/env python3
"""Семантический поиск по метрикам v2 (карточки derived.metric_card).

Примеры:
  python3 scripts/metric_search.py "ипотечная задолженность по регионам"
  python3 scripts/metric_search.py "ввод жилья" --theme "жильё и строительство" --level региональный
  python3 scripts/metric_search.py "страховые взносы по отраслям" --limit 10 --with-values
"""
import argparse
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402

FOLDER = 'b1gpe14c599s44v5dacm'
API = 'https://llm.api.cloud.yandex.net/foundationModels/v1/textEmbedding'


def api_key():
    for line in open(os.path.expanduser('~/.hermes/.env'), encoding='utf-8'):
        if line.startswith('YANDEX_CLOUD_API_KEY='):
            return line.split('=', 1)[1].strip().strip('"').strip("'")
    raise SystemExit('YANDEX_CLOUD_API_KEY не найден в ~/.hermes/.env')


def embed_query(text):
    """Запрос вкладывается моделью text-search-query (отдельная от doc-модели)."""
    body = json.dumps({'modelUri': 'emb://%s/text-search-query/latest' % FOLDER,
                       'text': text[:4000]}, ensure_ascii=False)
    r = subprocess.run(['curl', '-s', '-m', '40', '-X', 'POST', API,
                        '-H', f'Authorization: Api-Key {api_key()}',
                        '-H', 'Content-Type: application/json',
                        '--data-binary', '@-'], input=body, capture_output=True, text=True)
    try:
        v = json.loads(r.stdout).get('embedding')
    except json.JSONDecodeError:
        v = None
    if not v:
        raise SystemExit('вложение запроса не получено: ' + r.stdout[:200])
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('query')
    ap.add_argument('--limit', type=int, default=8)
    ap.add_argument('--theme', default=None)
    ap.add_argument('--level', default=None)
    ap.add_argument('--source', default=None)
    ap.add_argument('--with-values', action='store_true', help='показать последние значения')
    ap.add_argument('--sql-only', action='store_true', help='без вектора: только триграммный поиск')
    args = ap.parse_args()

    db_tunnel.connect()
    where, params = ["c.status = 'active'"], []
    if args.theme:
        where.append('%s = ANY(c.themes)')
        params.append(args.theme)
    if args.level:
        where.append('c.level = %s')
        params.append(args.level)
    if args.source:
        where.append('%s = ANY(c.sources)')
        params.append(args.source)

    sql = f"""
        SELECT c.metric_code, c.name_ru, c.unit_ru, c.frequency_ru, c.level, c.sources, c.themes,
               c.n_obs, c.n_regions, c.period_min, c.period_max, c.description
        FROM derived.metric_card c
        WHERE {' AND '.join(where)}
    """
    if args.sql_only:
        sql += " AND c.search_text ILIKE %s ORDER BY c.n_obs DESC LIMIT %s"
        params += ['%' + args.query + '%', args.limit]
        rows = db_tunnel.query(sql, tuple(params))
    else:
        qv = '[' + ','.join(str(x) for x in embed_query(args.query)) + ']'
        sql += " AND c.embedding IS NOT NULL ORDER BY c.embedding <=> %s::vector LIMIT %s"
        params += [qv, args.limit]
        rows = db_tunnel.query(sql, tuple(params))

    print(f'запрос: {args.query}' + (f' | фильтры: тема={args.theme}, уровень={args.level}, источник={args.source}'
                                     if any([args.theme, args.level, args.source]) else ''))
    for i, r in enumerate(rows, 1):
        code, name, unit, freq, level, srcs, themes, n_obs, n_reg, pmin, pmax, descr = r
        print(f'\n{i}. {name}  [{code}]')
        print(f'   единица: {unit or "—"} | частота: {freq or "—"} | уровень: {level} | '
              f'охват: {n_obs} точек, {n_reg} регионов | последние: {pmax}')
        print(f'   источники: {", ".join(srcs or []) or "—"} | темы: {", ".join(themes or []) or "—"}')
        if descr:
            print(f'   описание: {descr[:160]}')
        if args.with_values:
            vals = db_tunnel.query("""
                SELECT coalesce(r.short_name, r.name_ru, 'РФ'), o.period_start::text, o.value
                FROM core.observation_v2 o
                LEFT JOIN core.region r ON r.region_id = o.region_id
                WHERE o.metric_id = (SELECT metric_id FROM derived.metric_card WHERE metric_code = %s)
                  AND o.observation_status <> 'rejected'
                ORDER BY o.period_start DESC, r.name_ru LIMIT 4""", (code,))
            print('   значения: ' + ', '.join(f'{n} {p}={v}' for n, p, v in vals if v is not None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())