#!/usr/bin/env python3
"""Загрузка в канон длинной панели ИПЦ из хранилища db_cpi_store.

Источник — публичная папка «Статистика.ИПЦ» на Яндекс.Диске
(https://disk.yandex.ru/d/i6czrcdNO0I7BQ), архив db_cpi_store.7z, база
db_cpi_store.accdb. По содержанию это **дублёр ЕМИСС в части ИПЦ**: таблица
data_indices содержит MoM и YoY по разрезу «товар × регион × месяц», то же
самое, что отдаёт показатель ЕМИСС 31074, но без обращений к fedstat.ru,
который с датацентр-адресов закрыт.

Что делает скрипт:
  * читает панель по Российской Федерации (region_code=0), подготовленную
    scripts/extract_cpi_region.py из выгрузки mdb-export;
  * проверяет три контроля (сцепление 2026 против публикации, совпадение с
    каноном Росстата rosstat_cpi_cmp_*, сцепление 12 месяцев против YoY);
  * пишет метрики `cpistore_<item>_mom` и `cpistore_<item>_yoy`, наблюдения по
    РФ, релиз `cpi_store_2026-09`.

Запись только при --apply; по умолчанию dry-run.
"""
import argparse
import csv
import datetime as dt
import hashlib
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / 'scripts'))
import db_tunnel  # noqa: E402

SRC_DIR = Path(os.path.expanduser('~/macroeconomist/inbox/cpi-store/csv'))
PANEL = SRC_DIR / 'indices_ru.csv'
NAMES = SRC_DIR / 'items_names.csv'
SETS = SRC_DIR / 'items_set.csv'

UNIT_PCT = 12
FREQ_MONTH = 5
REGION_RU = 1
PUBLIC_URL = 'https://disk.yandex.ru/d/i6czrcdNO0I7BQ'
SOURCE_CODE = 'cpi_store'
LABEL = 'cpi_store_2026-09'
TOL_OVERLAP = 0.05
TOL_CHAIN = 0.30


def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def load_panel():
    mom, yoy = {}, {}
    with open(PANEL, encoding='utf-8') as fh:
        for r in csv.DictReader(fh):
            key = (r['item_code'], r['day'][:7])
            if r['mom']:
                mom[key] = float(r['mom'])
            if r['yoy']:
                yoy[key] = float(r['yoy'])
    return mom, yoy


def load_names():
    out = {}
    with open(NAMES, encoding='utf-8-sig', errors='replace') as fh:
        for r in csv.DictReader(fh):
            out[r['Item_code']] = (r['Item_name'] or '').strip()
    return out


def load_local():
    out = {}
    with open(SETS, encoding='utf-8-sig', errors='replace') as fh:
        for r in csv.DictReader(fh):
            if r.get('local_code'):
                out[r['Item_code']] = r['local_code']
    return out


def controls(mom, yoy, local):
    problems = []
    # 1) цепь 2026 янв-сен по агрегату
    chain = 1.0
    ok1 = True
    for m in range(1, 10):
        v = mom.get(('1', '2026-%02d' % m))
        if v is None:
            ok1 = False
            break
        chain *= v / 100.0
    if not ok1:
        problems.append('нет полного ряда агрегата за 2026')
    elif abs(chain * 100 - 105.04) > 0.02:
        problems.append('цепь 2026 = %.2f, опубликовано 105.04' % (chain * 100))
    print('контроль 1 (цепь 2026): %s' % ('%.2f' % (chain * 100) if ok1 else 'нет данных'))

    # 2) совпадение с каноном Росстата в окне 2025-01…2026-09
    rows = db_tunnel.query(
        """select m.metric_code, o.period_start, o.value
           from data.observation o join catalog.metric m using(metric_id)
           where m.metric_code like 'rosstat_cpi_cmp_%%_mom'
             and o.period_start >= date '2025-01-01'""")
    canon = {(mc, ps.strftime('%Y-%m')): float(v) for mc, ps, v in rows}
    pairs = close = 0
    worst = []
    for ic, lc in local.items():
        mc = 'rosstat_cpi_cmp_%s_mom' % lc
        for p in ['2025-%02d' % m for m in range(1, 13)] + ['2026-%02d' % m for m in range(1, 10)]:
            a, b = canon.get((mc, p)), mom.get((ic, p))
            if a is None or b is None:
                continue
            pairs += 1
            d = b - a
            if abs(d) <= TOL_OVERLAP:
                close += 1
            else:
                worst.append((mc, p, a, b, round(d, 3)))
    share = close / pairs if pairs else 0
    print('контроль 2 (сверка с Росстатом): %d пар, совпало %.1f%%'
          % (pairs, 100 * share))
    for w in sorted(worst, key=lambda x: -abs(x[4]))[:5]:
        print('   !', w)
    if pairs and share < 0.99:
        problems.append('расхождение с каноном Росстата %.1f%%' % (100 * (1 - share)))

    # 3) цепь 12 месяцев против YoY
    ok = bad = 0
    for (ic, p), v in yoy.items():
        y, m = int(p[:4]), int(p[5:])
        c = 1.0
        miss = False
        for k in range(12):
            mm = m - k
            yy = y + (mm - 1) // 12
            mm = (mm - 1) % 12 + 1
            q = mom.get((ic, '%04d-%02d' % (yy, mm)))
            if q is None:
                miss = True
                break
            c *= q / 100.0
        if miss:
            continue
        if abs(c * 100 - v) <= TOL_CHAIN:
            ok += 1
        else:
            bad += 1
    share3 = ok / (ok + bad) if ok + bad else 0
    print('контроль 3 (цепь 12 мес против г/г): совпало %d, расхождений %d'
          % (ok, bad))
    if ok + bad and share3 < 0.99:
        problems.append('г/г не сходится у %.1f%% рядов' % (100 * (1 - share3)))
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()

    if not PANEL.exists():
        sys.exit('нет панели %s — сначала scripts/extract_cpi_region.py' % PANEL)
    mom, yoy = load_panel()
    names = load_names()
    local = load_local()
    items = sorted({k[0] for k in mom} | {k[0] for k in yoy})
    print('товаров: %d, точек mom %d, yoy %d' % (len(items), len(mom), len(yoy)))

    problems = controls(mom, yoy, local)
    if problems and not a.force:
        print('ОСТАНОВ: контроль не пройден')
        for p in problems:
            print('   -', p)
        return 2
    for p in problems:
        print('   ! (force)', p)

    if not a.apply:
        print('DRY-RUN. Пример метрики: cpistore_%s_mom — %s'
              % (items[0], names.get(items[0], '?')[:60]))
        return 0

    digest = sha256(PANEL)
    rel = db_tunnel.query('select source_id from catalog.source where source_code=%s',
                          (SOURCE_CODE,))
    if rel:
        source_id = rel[0][0]
    else:
        source_id = db_tunnel.query(
            """insert into catalog.source (source_code, name_ru, url, publisher, reliability,
                                           is_active)
               values (%s,%s,%s,%s,'secondary',true) returning source_id""",
            (SOURCE_CODE,
             'Хранилище ИПЦ db_cpi_store (дублёр ЕМИСС в части ИПЦ)',
             PUBLIC_URL, 'Публичная папка «Статистика.ИПЦ» (Яндекс.Диск)'))[0][0]
    print('source_id=%s' % source_id)

    rel = db_tunnel.query('select release_id from catalog.release where label=%s', (LABEL,))
    if rel:
        release_id = rel[0][0]
        db_tunnel.execute(
            """update catalog.release set status='loaded', ingested_at=now(),
                   content_hash=%s, url=%s, source_id=%s where release_id=%s""",
            (digest, PUBLIC_URL, source_id, release_id))
    else:
        release_id = db_tunnel.query(
            """insert into catalog.release (source_id, label, published_at, content_hash,
                                            status, ingested_at, url, notes)
               values (%s,%s,%s,%s,'loaded',now(),%s,%s) returning release_id""",
            (source_id, LABEL, dt.datetime(2026, 10, 13, tzinfo=dt.timezone.utc),
             digest, PUBLIC_URL,
             'ИПЦ по товарам и услугам, РФ, 2010-01…2026-09; дублёр ЕМИСС 31074'))[0][0]
    print('release_id=%s' % release_id)

    rows = []
    for ic in items:
        nm = names.get(ic, 'товар %s' % ic)
        for suffix, what in (('mom', 'к предыдущему месяцу'), ('yoy', 'к соответствующему месяцу предыдущего года')):
            mc = 'cpistore_%s_%s' % (ic, suffix)
            desc = ('Хранилище ИПЦ db_cpi_store (дублёр ЕМИСС по ИПЦ), %s, %s, РФ, '
                    '2010-01…2026-09. Код товара %s' % (what, nm[:150], ic))
            rows.append((mc, nm[:180], desc))
    n = db_tunnel.execute_many(
        """insert into catalog.metric (metric_code, name_ru, description, unit_id, source_id,
                                       frequency_id, metric_type, is_derived, status, tags)
           values (%s,%s,%s,%s,%s,%s,'primary',false,'active',%s)
           on conflict (metric_code) do update set name_ru=excluded.name_ru,
               description=excluded.description, is_active=true""",
        [(mc, nm, ds, UNIT_PCT, source_id, FREQ_MONTH,
          ['cpi', 'duplicate_emiss', 'inflation', 'long_history'])
         for mc, nm, ds in rows])
    print('метрик записано/обновлено: %d' % n)

    obs = []
    for (ic, p), v in sorted(mom.items()):
        ps = dt.date(int(p[:4]), int(p[5:]), 1)
        pe = (ps + dt.timedelta(days=32)).replace(day=1) - dt.timedelta(days=1)
        obs.append(('cpistore_%s_mom' % ic, ps, pe, v,
                    'db_cpi_store data_indices, РФ, товар %s' % ic))
    for (ic, p), v in sorted(yoy.items()):
        ps = dt.date(int(p[:4]), int(p[5:]), 1)
        pe = (ps + dt.timedelta(days=32)).replace(day=1) - dt.timedelta(days=1)
        obs.append(('cpistore_%s_yoy' % ic, ps, pe, v,
                    'db_cpi_store data_indices, РФ, товар %s' % ic))
    print('к вставке наблюдений: %d' % len(obs))
    db_tunnel.execute(
        """delete from data.observation where metric_id in
             (select metric_id from catalog.metric where metric_code like 'cpistore_%%')
           and release_id=%s""", (release_id,))
    total = 0
    step = 5000
    for i in range(0, len(obs), step):
        chunk = obs[i:i + step]
        total += db_tunnel.execute_many(
            """insert into data.observation (metric_id, region_id, period_start, period_end,
                   value, observation_status, assessment_type, release_id, frequency_id,
                   source_id, quality_flags, notes)
               values ((select metric_id from catalog.metric where metric_code=%s),
                       %s,%s,%s,%s,'validated','final',%s,%s,%s,'{}',%s)""",
            [(mc, REGION_RU, ps, pe, v, release_id, FREQ_MONTH, source_id, note)
             for mc, ps, pe, v, note in chunk])
        print('  вставлено %d/%d' % (total, len(obs)), flush=True)
    chk = db_tunnel.query(
        """select count(distinct m.metric_id), count(*), min(o.period_start), max(o.period_start)
           from data.observation o join catalog.metric m using(metric_id)
           where m.metric_code like 'cpistore_%%'""")
    print('в каноне: %d рядов, %d наблюдений, %s … %s' % chk[0])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
