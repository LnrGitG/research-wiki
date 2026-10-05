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
    """Запрос вкладывается той же моделью text-search-doc, что и карточки метрик.

    Яндекс предлагает отдельные модели text-search-query и text-search-doc,
    но pgvector cosine distance работает только в одном пространстве.
    Карточки метрик уже вложены моделью text-search-doc, поэтому запрос
    тоже эмбеддим doc-моделью для корректного сравнения.
    """
    body = json.dumps({'modelUri': 'emb://%s/text-search-doc/latest' % FOLDER,
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
    ap.add_argument('--max-age-days', type=int, default=None,
                    help='не показывать ряды, у которых последняя точка старше N дней')
    ap.add_argument('--prefer-fresh', action='store_true',
                    help='штрафовать устаревшие ряды в ранжировании (свежесть как часть сходства)')
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
    if args.max_age_days is not None:
        where.append('c.freshness_days IS NOT NULL AND c.freshness_days <= %s')
        params.append(args.max_age_days)

    sql = f"""
        SELECT c.metric_code, c.name_ru, c.unit_ru, c.frequency_ru, c.level, c.sources, c.themes,
               c.n_obs, c.n_regions, c.period_min, c.period_max, c.description
        FROM derived.metric_card c
        WHERE {' AND '.join(where)}
    """
    if args.sql_only:
        # По словам: каждое слово отдельно через ILIKE
        words = [w for w in args.query.split() if len(w) >= 3]
        if words:
            like_clauses = ' AND '.join(['c.search_text ILIKE %s'] * len(words))
            sql += f" AND {like_clauses} ORDER BY c.n_obs DESC LIMIT %s"
            params += ['%' + w + '%' for w in words] + [args.limit]
        else:
            sql += " AND c.search_text ILIKE %s ORDER BY c.n_obs DESC LIMIT %s"
            params += ['%' + args.query + '%', args.limit]
        rows = db_tunnel.query(sql, tuple(params))
    else:
        qv = '[' + ','.join(str(x) for x in embed_query(args.query)) + ']'
        sql = f"""
            WITH q AS (SELECT '{qv}'::vector AS qv)
            SELECT c.metric_code, c.name_ru, c.unit_ru, c.frequency_ru, c.level, c.sources, c.themes,
                   c.n_obs, c.n_regions, c.period_min, c.period_max, c.description
            FROM derived.metric_card c, q
            WHERE c.status = 'active' AND c.embedding IS NOT NULL
        """
        # применить фильтры
        w = ['c.status = \'active\'', 'c.embedding IS NOT NULL']
        p = []
        if args.theme:
            w.append('%s = ANY(c.themes)'); p.append(args.theme)
        if args.level:
            w.append('c.level = %s'); p.append(args.level)
        if args.source:
            w.append('%s = ANY(c.sources)'); p.append(args.source)
        if args.max_age_days is not None:
            w.append('c.freshness_days IS NOT NULL AND c.freshness_days <= %s'); p.append(args.max_age_days)
        # Перестроим WHERE
        where_clause = ' AND '.join(w)
        if args.prefer_fresh:
            sql = f"""
                WITH q AS (SELECT '{qv}'::vector AS qv)
                SELECT c.metric_code, c.name_ru, c.unit_ru, c.frequency_ru, c.level, c.sources, c.themes,
                       c.n_obs, c.n_regions, c.period_min, c.period_max, c.description
                FROM derived.metric_card c, q
                WHERE {where_clause}
                ORDER BY (c.embedding <=> q.qv)
                         + 0.06 * LEAST(COALESCE(c.freshness_days, 3650), 3650) / 3650.0
                LIMIT %s
            """
            p += [args.limit]
        else:
            sql = f"""
                WITH q AS (SELECT '{qv}'::vector AS qv)
                SELECT c.metric_code, c.name_ru, c.unit_ru, c.frequency_ru, c.level, c.sources, c.themes,
                       c.n_obs, c.n_regions, c.period_min, c.period_max, c.description
                FROM derived.metric_card c, q
                WHERE {where_clause}
                ORDER BY c.embedding <=> q.qv
                LIMIT %s
            """
            p += [args.limit]
        rows = db_tunnel.query(sql, tuple(p))

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
                FROM data.observation o
                LEFT JOIN catalog.region r ON r.region_id = o.region_id
                WHERE o.metric_id = (SELECT metric_id FROM derived.metric_card WHERE metric_code = %s)
                  AND o.observation_status IS DISTINCT FROM 'rejected'
                ORDER BY o.period_start DESC, r.name_ru LIMIT 4""", (code,))
            print('   значения: ' + ', '.join(f'{n} {p}={v}' for n, p, v in vals if v is not None))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())