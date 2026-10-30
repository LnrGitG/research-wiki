#!/usr/bin/env python3
"""Загрузчик ЕМИСС 34118 (ввод жилья) из выгрузки fedstat — прямо в канон.

Две правки по итогам сверки 30.10.2026 (`queries/emiss-34118-verification-20261030.md`):

1. **Регион по ОКАТО, а не по названию.** Прежний загрузчик сопоставлял регионы
   по короткому названию и терял официальные длинные формы — в срезе не было
   Москвы (`45000000000 Город Москва столица Российской Федерации город
   федерального значения`), Санкт-Петербурга, Татарстана, Чувашии, Севастополя и
   новых субъектов: 80 из 89. Здесь первые две цифры ОКАТО сравниваются с
   `catalog.region.okato`, поэтому подпись строки в файле не важна.
2. **Квартальные и накопительные строки — в свои метрики.** В файле рядом с
   месячными лежат `I квартал`, `январь-февраль`, `январь-август`. В месячной
   метрике они ложились на первый месяц периода и завышали его втрое (апрель
   2026: 20 783,1 против 6 144,9 тыс. м²). Теперь `m` идёт в
   `emiss_34118_vvod`, `q` — в `emiss_34118_vvod_q`, накопительные — в
   `emiss_34118_vvod_cum`.

Старые строки месячной метрики не удаляются: они помечаются `superseded`
(точка возврата — дамп в `attic/`), новая выгрузка пишется отдельным релизом.

    scripts/emiss_34118_canon.py --check        # разбор и отчёт, без записи
    scripts/emiss_34118_canon.py --apply        # запись в канон

Источник файла — `scripts/fedstat_indicator_fetch.sh 34118 /tmp/34118.xls`.
"""
import argparse
import collections
import csv
import gzip
import json
import os
import re
import sys
from datetime import date

import xlrd

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402

XLS = os.environ.get('XLS', '/tmp/34118.xls')
MON = {'январ': 1, 'феврал': 2, 'март': 3, 'апрел': 4, 'ма': 5, 'июн': 6,
       'июл': 7, 'август': 8, 'сентябр': 9, 'октябр': 10, 'ноябр': 11, 'декабр': 12}
QMAP = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4}
CODE_M = 'emiss_34118_vvod'
CODE_Q = 'emiss_34118_vvod_q'
CODE_CUM = 'emiss_34118_vvod_cum'


def parse_period(label):
    """('m'|'q'|'cum', start_ym, end_ym) из подписи периода."""
    s = str(label).strip().lower().replace('\u2013', '-').replace('\u2014', '-')
    s = re.sub(r'^[a-z]?\d+(?:_\d+)?\s*', '', s)       # ведущий код периода (115, M01_02)
    q = re.match(r'^(i{1,3}|iv)\s*квартал$', s)
    if q:
        n = QMAP[q.group(1)]
        return 'q', (n * 3 - 2, n * 3)
    if '-' in s:
        parts = [p.strip() for p in s.split('-')]

        def month_of(word):
            for key, m in MON.items():
                if word.startswith(key):
                    return m
            return None

        if len(parts) == 2:
            a, b = month_of(parts[0]), month_of(parts[1])
            if a and b:
                return 'cum', (a, b)
    for key, m in MON.items():
        if s.startswith(key):
            return 'm', (m, m)
    return None, None


def to_num(v):
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace('\xa0', '').replace(' ', '').replace(',', '.')
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def read_xls():
    book = xlrd.open_workbook(XLS, on_demand=True)
    sh = book.sheet_by_index(0)
    years = [int(str(sh.cell_value(2, c))[:4]) for c in range(4, sh.ncols)]
    out = []
    for r in range(3, sh.nrows):
        okato = str(sh.cell_value(r, 0)).strip()
        nomen = str(sh.cell_value(r, 1)).strip()
        unit = str(sh.cell_value(r, 2)).strip()
        label = sh.cell_value(r, 3)
        if not okato or not nomen:
            continue
        kind, span = parse_period(label)
        if not kind:
            continue
        for y, v in zip(years, [sh.cell_value(r, c) for c in range(4, sh.ncols)]):
            num = to_num(v)
            if num is not None:
                out.append({'okato': okato, 'nomen': nomen, 'unit': unit,
                            'kind': kind, 'span': span, 'year': y, 'value': num})
    return out


def build_region_map(cur):
    cur.execute("""select region_id, region_code, okato, level
                   from catalog.region where okato is not null and okato <> ''""")
    by_okato, names = {}, {}
    for rid, code, okato, level in cur.fetchall():
        key = re.sub(r'\D', '', okato)
        if key:
            by_okato.setdefault(key.zfill(2), rid)
        names[code] = rid
    return by_okato, names


def region_for(row, by_okato, ru_id):
    """Регион по ОКАТО: только субъекты (11 цифр, девять нулей после первых двух).

    В файле рядом лежат федеральные округа (030), муниципальные агрегаты
    (03020000000.АГ) и вложенные субъекты (11001000000 — Архангельская область
    без НАО, 71140000000 — ХМАО внутри Тюменской). Если брать первые две цифры у
    любой строки, они складываются в один регион и сумма удваивается.
    """
    raw = row['okato']
    digits = re.sub(r'\D', '', raw)
    if digits.startswith('643'):
        return ru_id, 'Российская Федерация'
    if '.АГ' in raw or '.аг' in raw:
        return None, None
    if len(digits) == 11 and digits[2:] == '0' * 9:
        return by_okato.get(digits[:2].zfill(2)), None
    return None, None


def target_metric(cur, code):
    cur.execute("select metric_id from catalog.metric where metric_code = %s", (code,))
    r = cur.fetchone()
    return r[0] if r else None


def ensure_metric(cur, code, name, freq_id, unit_id):
    mid = target_metric(cur, code)
    if mid:
        return mid, False
    cur.execute("""insert into catalog.metric (metric_code, name_ru, frequency_id, unit_id,
                      metric_type, status, is_active, tags)
                   values (%s, %s, %s, %s, 'primary', 'active', true, %s)
                   returning metric_id""",
                (code, name, freq_id, unit_id, ['emiss', 'emiss_34118']))
    return cur.fetchone()[0], True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--release', default=None, help='метка релиза')
    args = ap.parse_args()

    if not os.path.exists(XLS):
        print(f'нет файла {XLS} — сначала scripts/fedstat_indicator_fetch.sh 34118 {XLS}')
        return 2

    rows = read_xls()
    conn = db_tunnel.connect(options='-c work_mem=512MB')
    cur = conn.cursor()
    by_okato, names = build_region_map(cur)
    cur.execute("select region_id from catalog.region where region_code = 'ru'")
    ru_id = cur.fetchone()[0]

    kits = collections.Counter(r['kind'] for r in rows)
    print('строк в файле:', len(rows), dict(kits))

    unmapped = collections.Counter()
    prepared = []
    for r in rows:
        rid, _ = region_for(r, by_okato, ru_id)
        if rid is None:
            unmapped[r['okato'][:6]] += 1
            continue
        prepared.append((rid, r))
    print('сопоставлено регионов:', len({p[0] for p in prepared}),
          'строк:', len(prepared), 'не сопоставлено:', len(rows) - len(prepared))
    for code, n in unmapped.most_common(5):
        print('   без региона:', code, n)
    subj = collections.Counter(r['okato'][:2] for r in rows
                               if len(re.sub(r'\D', '', r['okato'])) == 11
                               and re.sub(r'\D', '', r['okato'])[2:] == '0' * 9
                               and region_for(r, by_okato, ru_id)[0] is None)
    if subj:
        print('   субъекты без карточки региона:', dict(subj))

    # контроль: сумма месячных по РФ против национальной строки
    nat, agg = {}, collections.defaultdict(float)
    for rid, r in prepared:
        if r['kind'] != 'm':
            continue
        key = (r['nomen'], r['year'], r['span'][0])
        if rid == ru_id:
            nat[key] = r['value']
        else:
            agg[key] += r['value']
    total_n = 'жилые помещения в нежилых зданиях'
    checks = sorted([k for k in nat if k in agg and total_n in k[0].lower()], key=lambda k: (k[1], k[2]))[-3:]
    for k in checks:
        d = (agg[k] - nat[k]) / nat[k] * 100
        print(f'  сверка {k[1]}-{k[2]:02d} [{k[0][:46]}]: сумма регионов {agg[k]:.1f} | '
              f'нац. строка {nat[k]:.1f} | {d:+.2f} %')

    if not args.apply:
        print('режим --check: записи не выполнялись')
        return 0

    if not checks:
        print('нет периодов для сверки — запись отменена')
        return 3

    cur.execute("select unit_id from catalog.metric where metric_code = %s", (CODE_M,))
    unit_id = cur.fetchone()[0]
    cur.execute("select frequency_id from catalog.frequency where freq_code = 'M'")
    f_m = cur.fetchone()[0]
    cur.execute("select frequency_id from catalog.frequency where freq_code = 'Q'")
    f_q = cur.fetchone()[0]
    cur.execute("select frequency_id from catalog.frequency where freq_code = 'A'")
    f_a = cur.fetchone()[0]

    m_ids = {CODE_M: unit_id}
    id_m = target_metric(cur, CODE_M)
    id_q, created_q = ensure_metric(cur, CODE_Q,
                                    'Ввод жилья, квартальный срез ЕМИСС 34118, тыс. м²',
                                    f_q, unit_id)
    id_cum, created_cum = ensure_metric(cur, CODE_CUM,
                                        'Ввод жилья, накопительный с начала года, ЕМИСС 34118, тыс. м²',
                                        f_a, unit_id)

    cur.execute("select source_id, source_code from catalog.source where source_id = 11")
    source_id, source_code = cur.fetchone()
    label = args.release or f'fedstat_34118_{date.today():%Y-%m-%d}'
    cur.execute("select release_id from catalog.release where source_id = %s and label = %s",
                (source_id, label))
    got = cur.fetchone()
    if got:
        release_id = got[0]
    else:
        cur.execute("""insert into catalog.release (source_id, label, published_at, status, url, notes)
                       values (%s, %s, now(), 'loaded', %s, %s) returning release_id""",
                    (source_id, label, 'https://www.fedstat.ru/indicator/34118',
                     'Выгрузка xls через резидентное окно (tailscale exit node ноутбука)'))
        release_id = cur.fetchone()[0]

    # точка возврата по месячной метрике
    attic = os.path.join(REPO, 'attic')
    os.makedirs(attic, exist_ok=True)
    dump = os.path.join(attic, f'emiss34118_monthly_before_{date.today():%Y%m%d}')
    cur.execute("""select metric_id, region_id, frequency_id, period_start, period_end, value,
                          assessment_type, observation_status, source_id, release_id, sub_dimension
                   from data.observation where metric_id = %s and release_id is distinct from %s""",
                (id_m, release_id))
    old = cur.fetchall()
    if old:
        path = f'{dump}.csv.gz'
        with gzip.open(path, 'wt', encoding='utf-8', newline='') as f:
            w = csv.writer(f)
            for r in old:
                w.writerow(r)
        print(f'дамп прежних строк: {path} ({len(old)})')
        cur.execute("""update data.observation set observation_status = 'superseded'
                       where metric_id = %s and observation_status <> 'superseded'
                         and release_id is distinct from %s""", (id_m, release_id))
        print('помечено superseded:', cur.rowcount)

    def ps_end(year, month, kind):
        if kind == 'q':
            return date(year, month, 1), date(year, month, 28)
        return date(year, month, 1), date(year, month, 28)

    payload = []
    for rid, r in prepared:
        y = r['year']
        if r['kind'] == 'm':
            mid, freq = id_m, f_m
            ps = date(y, r['span'][0], 1)
            sub = {'nomen': r['nomen'], 'kind': 'm', 'period_name': f'{y}-{r["span"][0]:02d}'}
        elif r['kind'] == 'q':
            mid, freq = id_q, f_q
            ps = date(y, r['span'][0], 1)
            sub = {'nomen': r['nomen'], 'kind': 'q', 'period_name': f'{y} Q{(r["span"][0] + 2) // 3}'}
        else:
            mid, freq = id_cum, f_a
            ps = date(y, r['span'][0], 1)
            sub = {'nomen': r['nomen'], 'kind': 'cum',
                   'period_name': f'{y}-{r["span"][0]:02d}..{r["span"][1]:02d}'}
        payload.append((mid, rid, freq, ps, date(y, r['span'][1], 28), r['value'],
                        'final' if y < date.today().year else 'preliminary',
                        'validated', source_id, release_id,
                        json.dumps(sub, ensure_ascii=False)))

    sql = """insert into data.observation
             (metric_id, region_id, frequency_id, period_start, period_end, value,
              assessment_type, observation_status, source_id, release_id, sub_dimension)
             values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
             on conflict (metric_id, region_id, period_start, frequency_id,
                          assessment_type, sub_dimension, release_id) do nothing"""
    for i in range(0, len(payload), 2000):
        cur.executemany(sql, payload[i:i + 2000])
    conn.commit()
    print(f'записано строк: {len(payload)} (релиз {release_id}, метка {label})')

    cur.execute("""select m.metric_code, count(*), count(distinct o.region_id)
                   from data.observation o join catalog.metric m on m.metric_id = o.metric_id
                   where o.release_id = %s group by 1 order by 1""", (release_id,))
    for code, n, nreg in cur.fetchall():
        print(f'  {code}: {n} строк, регионов {nreg}')
    conn.close()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
