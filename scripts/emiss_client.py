#!/usr/bin/env python3
"""Python port of fedstatAPIr (R, DenchPokepon) — EMISS/fedstat.ru data download.

Завершено 29.08.2026. Итог теста с VPS: ENDPOINT ПОЛНОСТЬЮ ЗАБЛОКИРОВАН по IP
(403 и на GET страницы индикатора, и на POST data.do — с браузерными заголовками,
multipart-телом и Referer как в R-пакете). Порт готов и заработает с резидентного IP
(домашняя машина / Mac Studio после покупки).

Использование (с машины, где fedstat доступен):
    python3 emiss_client.py 57605 out.xlsx --select "Период=Январь,Февраль..." --filter "ОКАТО=Российская Федерация"
или программно:
    from emiss_client import load_with_filters
    df_bytes = load_with_filters('57605', filters={...})
"""
import re, json, time, sys, urllib.request, urllib.error

BASE = 'https://www.fedstat.ru'
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')
HDR = {'User-Agent': UA, 'Accept-Language': 'ru-RU,ru;q=0.9,en;q=0.8',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}


def _req(url, data=None, headers=None, timeout=90, method=None):
    h = dict(HDR)
    if data is not None:
        h['Content-Type'] = 'application/x-www-form-urlencoded'
        data = urllib.parse.urlencode(data, doseq=True).encode()
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=data, headers=h, method=method or ('POST' if data else 'GET'))
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _js_json(chunk):
    """R parse_js trick → JSON: unquoted barewords to quoted, ' -> ", wrap {}."""
    s = re.sub(r"\b(?=([^']*'[^']*')*[^']*$)", '"', chunk)
    s = s.replace("'", '"')
    # strip trailing commas (JS objects allow them, JSON no)
    s = re.sub(r',(\s*[}\]])', r'\1', s)
    return json.loads('{' + s + '}')


def get_data_ids(indicator_id, retries=3, timeout=60):
    """GET indicator page, parse filter definitions from JS (filters: {..} до left_columns: [)."""
    url = f'{BASE}/indicator/{indicator_id}'
    html = None
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers=HDR)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                html = r.read().decode('utf-8', 'replace')
            break
        except urllib.error.HTTPError as e:
            if e.code == 403:
                raise RuntimeError('403 — IP заблокирован ЕМИСС (нужен резидентный IP)')
            time.sleep(5 * attempt)
        except Exception as e:
            time.sleep(5 * attempt)
    else:
        raise RuntimeError('GET страницы индикатора не удался')

    scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.S)
    js = next((s for s in scripts if 'filters:' in s and 'left_columns' in s), None)
    if js is None:
        raise RuntimeError('JS с фильтрами не найден — возможно, поменялась разметка ЕМИСС')
    lines = js.split('\n')
    i1 = next(i for i, l in enumerate(lines) if re.search(r'filters:\s*\{', l))
    i2 = next(i for i, l in enumerate(lines) if re.search(r'left_columns:\s*\[', l))
    filters = _js_json('\n'.join(lines[i1 + 1:i2 - 2]))

    # object ids (lineObjectIds/columnObjectIds/filterObjectIds)
    j3 = next(i for i, l in enumerate(lines) if re.search(r'left_columns:\s*\[', l))
    j4 = next((i for i, l in enumerate(lines) if 'grid.init()' in l), len(lines))
    objs = _js_json('\n'.join(lines[j3:j4 - 2 if j4 > j3 else j3]))

    fields = []
    for idx, (fid, f) in enumerate(filters.items()):
        values = f.get('values') or {}
        fields.append({
            'filter_field_id': str(idx),           # R: idcol = filter_field_id (порядковый)
            'field_title': f.get('title', ''),
            'object_ids': objs_map.get(str(idx), 'lineObjectIds'),
            'values': {vid: (v.get('title') if isinstance(v, dict) else str(v)) for vid, v in values.items()},
        })
    return fields, objs


def build_post_body(fields, indicator_id, selected):
    """selected: dict field_title -> value_title | '*' (все значения)."""
    parts = [('format', 'excel')]
    ind = [f for f in fields if f['field_title'] == '' or f['filter_field_id'] == '0'] if False else None
    # R: id = filter_value_id of field with filter_field_id == '0' (это сам показатель)
    # В нашей структуре: object_ids='0' соответствие — field with filterObjectIds
    indicator_field = next((f for f in fields if 'filterObjectIds' not in f and f.get('is_indicator')), None)
    body = [('format', 'excel'), ('id', indicator_id), ('indicator_title', '')]
    selected = []
    for f in fields:
        oid = f['object_ids']
        body.append((oid, f['filter_field_id']))
        want = (f.get('_want') or '*')
        for vid, vtitle in f['values'].items():
            if want == '*' or vtitle in want:
                selected.append(f"{f['filter_field_id']}_{vid}")
    for sv in selected:
        body.append(('selectedFilterIds', sv))
    return body


def post_data(body, data_format='excel', retries=4, timeout=120):
    url = f'{BASE}/indicator/data.do?format={data_format}'
    hdrs = {'User-Agent': UA, 'Referer': f'{BASE}/indicator/', 'Origin': BASE}
    data = urllib.parse.urlencode(body, doseq=True).encode()
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, data=data, headers=hdrs)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                ct = r.headers.get('Content-Type', '')
                blob = r.read()
            if ct in ('text/xml', 'application/vnd.ms-excel') and blob:
                return blob
            raise RuntimeError(f'unexpected content-type {ct}')
        except urllib.error.HTTPError as e:
            print('POST', attempt, e.code, str(e)[:60])
            time.sleep(10 * attempt)
    raise RuntimeError('POST data.do не удался')


def load_with_filters(indicator_id, filters, data_format='excel'):
    """filters: dict field_title -> value_title | '*'. Возвращает бинарный xlsx/sdmx."""
    fields = get_data_ids(indicator_id)
    # выбрать по названиям
    for f in fields:
        key = next((k for k in filters if k.lower() == f['field_title'].lower()), None)
        f['_want'] = filters.get(key, '*') if key else '*'
    body = build_post_body(fields, indicator_id)
    return post_data(body, data_format)


if __name__ == '__main__':
    print('см. load_with_filters(); тест с VPS невозможен — 403 IP-блок')