#!/usr/bin/env python3
"""Прямой загрузчик ЕМИСС 62024 → канон: индекс выпуска по базовым видам
экономической деятельности (ВБВЭД) по субъектам РФ, месячный ряд.

Источник и маршрут. Первоисточник — fedstat.ru (ЕМИСС), показатель 62024;
с датацентр-адресов он отдаёт 403, поэтому сырьё берётся из зеркала ЕМИСС в
репозитории nsEDC (CKAN, repository.nsedc.ru): package_show('emiss_62024') →
ресурс csv.gz на S3. Данные — те же (выгрузка ЕМИСС), снимок сохраняется в
raw/rosstat/emiss/, разбор — рядом в JSON (приёмка по сохранённому сырью).

Что пишется:
  metric  vbved_reg_m  — «Индекс выпуска товаров и услуг по базовым видам
                          экономической деятельности, % к соответствующему
                          периоду предыдущего года (регионы)», pct, M;
  период  — первый день месяца; накопительные строки источника
            («январь-август») идут отдельным подразрезом «накопительно: …»,
            чтобы их не читать как месяц;
  регион  — субъекты РФ и федеральные округа по catalog.region.

Запуск:
  python3 vbved_reg_canon.py --check    # разбор и сверка, без записи
  python3 vbved_reg_canon.py --apply    # запись в канон (с дампом)
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
import urllib.request
import ssl

import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direct_core import Writer, norm  # noqa: E402

CKAN = 'https://repository.nsedc.ru/api/3/action/package_show?id=emiss_62024'
RAW_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'raw', 'rosstat', 'emiss'))
CSV_PATH = os.path.join(RAW_DIR, '62024.csv.gz')
META_PATH = os.path.join(RAW_DIR, '62024_meta.json')
PARSED_PATH = os.path.join(RAW_DIR, '62024_parsed.json')
ATTIC = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'attic'))

SOURCE = 'fedstat_emiss'
METRIC_CODE = 'vbved_reg_m'
METRIC_NAME = ('Индекс выпуска товаров и услуг по базовым видам экономической '
               'деятельности, % к соответствующему периоду предыдущего года (регионы)')
RELEASE = 'ЕМИСС 62024, зеркало nsEDC, снимок 2026-10-20'
UNIT = 'pct'
FREQ = 'M'

MONTHS = {'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4, 'май': 5, 'июнь': 6,
          'июль': 7, 'август': 8, 'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11,
          'декабрь': 12}
# алиасы, которых нет в meta.region_alias, но которые встречаются в источнике
EXTRA_ALIAS = {'город федерального значения севастополь': 'Севастополь'}
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126'}


def fetch_raw() -> None:
    os.makedirs(RAW_DIR, exist_ok=True)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    meta = json.loads(urllib.request.urlopen(
        urllib.request.Request(CKAN, headers=UA), timeout=60, context=ctx).read())
    pkg = meta['result']
    res = [r for r in pkg['resources'] if r['format'] in ('csv.gz', 'csv')]
    if not res:
        raise RuntimeError('в пакете emiss_62024 нет ресурса csv — останов')
    url = res[0]['url']
    blob = urllib.request.urlopen(urllib.request.Request(url, headers=UA),
                                  timeout=180, context=ctx).read()
    with open(CSV_PATH, 'wb') as f:
        f.write(blob)
    with open(META_PATH, 'w', encoding='utf-8') as f:
        json.dump({'title': pkg.get('title'), 'resource_url': url,
                   'resource_format': res[0]['format'],
                   'downloaded_bytes': len(blob)}, f, ensure_ascii=False, indent=1)
    print('сырьё: %s (%d байт)' % (CSV_PATH, len(blob)))


def clean_region(s: str) -> str:
    s = re.sub(r'^\s*\d{3,11}\s+', '', str(s))
    return re.sub(r'\s+', ' ', s).strip()


def parse() -> tuple[list[dict], dict]:
    if not os.path.exists(CSV_PATH):
        fetch_raw()
    df = pd.read_csv(CSV_PATH, encoding='utf-8-sig', dtype=str)
    c_kind, c_reg, c_unit, c_per = df.columns[:4]
    years = [c for c in df.columns[4:] if re.fullmatch(r'\d{4}', str(c))]
    kinds = set(df[c_kind].dropna().astype(str))
    if len(kinds) != 1:
        raise RuntimeError('ожидался один вид показателя, в файле: %s' % kinds)

    rows, stats = [], {'строк в файле': len(df), 'месячных': 0, 'накопительных': 0,
                       'значений': 0, 'пустых': 0, 'регион не распознан': []}
    for _, r in df.iterrows():
        m = re.match(r'^[A-Za-z0-9_]+\s+(.+)$', str(r[c_per]).strip())
        label = (m.group(1) if m else str(r[c_per])).strip()
        if label in MONTHS:
            sub = None
            stats['месячных'] += 1
        elif re.match(r'^январь-', label):
            sub = 'накопительно: %s' % label
            stats['накопительных'] += 1
        else:
            continue
        reg = clean_region(r[c_reg])
        for y in years:
            v = r[y]
            if pd.isna(v) or str(v).strip() in ('', '-'):
                stats['пустых'] += 1
                continue
            rows.append({'регион': reg, 'год': int(y),
                         'месяц': MONTHS.get(label, 1) if sub is None else None,
                         'метка': label, 'sub': sub,
                         'значение': float(str(v).replace(',', '.')),
                         'единица': str(r[c_unit])})
            stats['значений'] += 1
    with open(PARSED_PATH, 'w', encoding='utf-8') as f:
        json.dump({'stats': {k: v for k, v in stats.items() if k != 'регион не распознан'},
                   'rows': [{'регион': x['регион'], 'год': x['год'], 'метка': x['метка'],
                             'sub': x['sub'], 'значение': x['значение']} for x in rows]},
                  f, ensure_ascii=False)
    return rows, stats


def build(rows, w: Writer) -> tuple[list[dict], dict]:
    """Строки под Writer.ingest + счётчики распознавания регионов."""
    names = {}
    # варианты состава различаем подразрезом ТОЛЬКО когда на один регион в источнике
    # приходятся две разные строки («Тюменская область» и «… без автономных округов»);
    # удлинённая официальная форма названия («Город Москва …» ) подразреза не требует
    seen = collections.Counter()
    for nm in {r['регион'] for r in rows}:
        key = norm(nm)
        rid = w.reg.get(norm(EXTRA_ALIAS.get(key, nm)))
        seen[rid] += 1
    for nm in {r['регион'] for r in rows}:
        key = norm(nm)
        rid = w.reg.get(norm(EXTRA_ALIAS.get(key, nm)))
        mark = None
        if rid is not None and seen[rid] > 1:
            mark = 'состав: %s' % nm
        names[key] = (rid, mark)
    out, lost = [], []
    for r in rows:
        rid, mark = names.get(norm(r['регион']), (None, None))
        if rid is None:
            lost.append(r['регион'])
            continue
        sub = r['sub']
        if mark:
            sub = '%s; %s' % (sub, mark) if sub else mark
        out.append({'metric_name': METRIC_NAME, 'value': r['значение'],
                    'ps': (r['год'], r['месяц'] if r['месяц'] else 1),
                    'region': rid, 'sub': sub, 'freq': FREQ,
                    'source': SOURCE, 'release': RELEASE, 'unit': UNIT,
                    '_label': r['метка']})
    # накопительные периоды ставим началом периода: (год, 1), месяц 1
    return out, {'не распознано': sorted(set(lost))}


def ensure_metric(w: Writer) -> tuple[int, bool]:
    if norm(METRIC_NAME) in w.by_name:
        return w.by_name[norm(METRIC_NAME)], False
    w.cur.execute("""INSERT INTO core.metric
        (metric_code, name_ru, unit_id, frequency_id, metric_type, status, tags)
        VALUES (%s, %s, %s, %s, 'primary', 'active', %s)
        ON CONFLICT (metric_code) DO UPDATE SET name_ru = EXCLUDED.name_ru
        RETURNING metric_id""",
                  (METRIC_CODE, METRIC_NAME, w.units.get(UNIT), w.freq.get(FREQ),
                   ['прямой загрузчик', 'vbved', 'emiss']))
    mid = w.cur.fetchone()[0]
    w.conn.commit()
    w.by_name[norm(METRIC_NAME)] = mid
    return mid, True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--refresh', action='store_true', help='перекачать сырьё из зеркала')
    a = ap.parse_args()
    if not (a.check or a.apply):
        ap.error('нужен --check или --apply')
    if a.refresh:
        fetch_raw()
    rows, stats = parse()
    print('разбор: строк %d, месячных %d, накопительных %d, значений %d, пусто %d'
          % (stats['строк в файле'], stats['месячных'], stats['накопительных'],
             stats['значений'], stats['пустых']))
    print('единицы в источнике: %s' % sorted({r['единица'] for r in rows}))

    w = Writer(tag='vbved', simulate=a.check)
    prep, info = build(rows, w)
    print('подготовлено наблюдений: %d | регион не распознан: %s'
          % (len(prep), info['не распознано'] or 'нет'))
    if info['не распознано']:
        print('ОСТАНОВ: есть нераспознанные регионы')
        w.close()
        return 2
    if a.check:
        w.close()
        print('--check: запись не выполнялась')
        return 0

    mid, created = ensure_metric(w)
    os.makedirs(ATTIC, exist_ok=True)
    dump = os.path.join(ATTIC, 'vbved_reg_m_before_%s.csv.gz' % '20261020')
    n_old = w.dump_group([METRIC_NAME], dump, delete=False) if not created else 0
    print('метрика %s (новая: %s), прежних строк в дампе: %d' % (METRIC_CODE, created, n_old))

    prep_clean = [{k: v for k, v in r.items() if not k.startswith('_')} for r in prep]
    n_prep, n_ins, n_conf, n_new = w.ingest(prep_clean, group='emiss_vbved')
    print('итог: подготовлено %d, вставлено %d, конфликтов %d, новых метрик %d'
          % (n_prep, n_ins, n_conf, n_new))
    w.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
