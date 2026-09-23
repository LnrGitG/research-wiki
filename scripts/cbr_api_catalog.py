#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Каталог универсального API Банка России (https://www.cbr.ru/dataservice/).

Обходит дерево публикаций, datasets, measures; пробует данные и печатает
сводку: что живо, диапазоны годов, свежесть. Без записи в БД.
"""
import urllib.request, ssl, json, collections

BASE = 'https://www.cbr.ru/dataservice'


def get_json(url):
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return json.loads(urllib.request.urlopen(req, timeout=60, context=ctx).read().decode('utf-8', 'ignore'))


def probe_dataset(pub_id, ds):
    ds_id = ds['id']
    out = {'publication': pub_id, 'dataset': ds_id, 'name': ds.get('dataset_name') or ds.get('name')}
    try:
        y = get_json(f'{BASE}/years?datasetId={ds_id}')
        rng = y[0] if isinstance(y, list) and y else {}
        out['years'] = f"{rng.get('FromYear')}-{rng.get('ToYear')}"
    except Exception:
        out['years'] = '?'
    try:
        ms = get_json(f'{BASE}/measures?datasetId={ds_id}')
        out['n_measures'] = len(ms.get('measure', []))
    except Exception:
        out['n_measures'] = 0
    # проба данных: без measureId и с 118
    n, last, per = 0, '-', '-'
    for mid in [None, 118]:
        try:
            url = f'{BASE}/data?y1=2016&y2=2026&datasetId={ds_id}&publicationId={pub_id}'
            if mid:
                url += f'&measureId={mid}'
            d = get_json(url)
            rows = d.get('RawData', [])
            if rows:
                n = len(rows)
                last = max(r['date'][:10] for r in rows)
                per = rows[0].get('periodicity', '-')
                break
        except Exception:
            continue
    out['rows_2016_2026'] = n
    out['last'] = last
    out['periodicity'] = per
    return out


def main():
    pubs = get_json(f'{BASE}/publications')
    by_parent = collections.defaultdict(list)
    for c in pubs:
        by_parent[c['parent_id']].append(c)

    def leaves(pid):
        kids = by_parent.get(pid, [])
        if not kids:
            return [pid]
        out = []
        for k in kids:
            out += leaves(k['id'])
        return out

    root_ids = sorted(c['id'] for c in pubs if c['parent_id'] == -1)
    for rid in root_ids:
        print(f'=== Корень {rid}: {by_parent[rid][0]["category_name"]}')
        for lid in leaves(rid):
            try:
                ds_list = get_json(f'{BASE}/datasets?publicationId={lid}')
                items = ds_list if isinstance(ds_list, list) else ds_list.get('dataset', [])
            except Exception:
                items = []
            for ds in items:
                p = probe_dataset(lid, ds)
                print(f'  pub{lid} ds{p["dataset"]:>3} | {p["name"][:55]:<55} | {p["years"]:>9} | '
                      f'm={p["n_measures"]:>3} | rows={p["rows_2016_2026"]:>6} | last={p["last"]} | {p["periodicity"]}')


if __name__ == '__main__':
    main()