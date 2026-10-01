#!/usr/bin/env python3
"""Загрузка демографического слоя ВПН-2020 по всем субъектам РФ и пересборка
витрины экспозиции реформы «Семейной ипотеки» 01.10.2026.

Источники (класс A, Росстат):
  * Tom8_tab4_VPN-2020.xlsx — ВПН-2020, том 8, таблица 4: частные домохозяйства
    по числу детей моложе 18 лет, по субъектам (строки РФ в файле нет —
    агрегируем по субъектам).
  * Chisl_polvozr_01-01-2022_VPN-2020.xlsx, лист «М+Ж_Г+С» — численность
    населения по полу и возрасту на 1.01.2022 (с учётом итогов ВПН-2020);
    дети 0–6 — колонки «до 1»..«6» (5–11), дети 0–17 — колонки 5–22.

Таблицы (public):
  vpn_households_children(region, with1, with2, with3p, share_3p, share_12)
  rosstat_children_06(region, kids_06, kids_017, population, share_kids06)
  did_exposure_reform2026(...) — витрина экспозиции, три маржи M1/M2/M4.

Экспозиция (design: queries/dizayn-prognoz-spros-pervichka-reforma-2026.md, §5).
Допущение: возрасты детей в домохозяйстве независимы; тогда для домохозяйства
с n детьми P(есть ребёнок младше 7) = 1 − (1 − p)^n, где
p = доля детей 0–6 среди детей 0–17.

  s1 = with1 · p / T                        — 1 ребёнок и есть ребёнок <7  → M1
  s2 = with2 · (1 − (1−p)^2) / T            — 2 детей и есть ребёнок <7   → M2
  s3 = with3p · (1 − (1−p)^3) / T           — 3+ детей и есть ребёнок <7  → M3 (растёт)
  s4 = (with2·(1−p)^2 + with3p·(1−p)^3) / T — 2+ детей, ребёнка <7 нет    → M4 (теряет право)

Веса — рост субсидируемой ставки, п.п.: M1: +4 (регионы) / +6 (столичные),
M2: +2 / +4; M4 — полная потеря субсидии, эталон 6 п.п. (дореформенная ставка).
  exposure_pp     = w1·s1 + w2·s2 + w4·s4            (п.п. роста ставки)
  exposure_gross  = exposure_pp / 6                  (нормированный индекс 0–1)
  exposure_share  = s1 + s2 + s4                     (доля семей, чьё положение хуже)

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 load_vpn_demography.py [--write]
Без --write — только печать разбора и сверки (dry run).
"""
import os
import sys

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from db_tunnel import query, execute  # noqa: E402

RAW = os.path.expanduser('~/research-wiki-private/raw/rosstat/vpn2020')
TAB4 = os.path.join(RAW, 'Tom8_tab4_VPN-2020.xlsx')
AGE = os.path.join(RAW, 'Chisl_polvozr_01-01-2022_VPN-2020.xlsx')

URL_TAB4 = 'https://rosstat.gov.ru/storage/mediabank/Tom8_tab4_VPN-2020.xlsx'
URL_AGE = 'https://rosstat.gov.ru/storage/mediabank/Chisl_polvozr_01-01-2022_VPN-2020.xlsx'


def ensure_sources():
    """Скачать исходные xlsx Росстата, если их нет (raw/ вне репозитория)."""
    os.makedirs(RAW, exist_ok=True)
    for path, url in ((TAB4, URL_TAB4), (AGE, URL_AGE)):
        if os.path.exists(path) and os.path.getsize(path) > 100_000:
            continue
        import requests
        import urllib3
        urllib3.disable_warnings()
        ua = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=ua, verify=False, timeout=120)
        if r.status_code != 200 or r.content[:2] != b'PK':
            raise SystemExit(f'не скачался {url}: HTTP {r.status_code}')
        with open(path, 'wb') as fh:
            fh.write(r.content)
        print('скачан', os.path.basename(path))

CAPITALS = {27, 19, 38, 34}          # Москва, МО, СПб, ЛО (отдельная шкала)
W1_REG, W1_CAP = 4.0, 6.0            # M1: рост ставки, п.п.
W2_REG, W2_CAP = 2.0, 4.0            # M2: рост ставки, п.п.
W4 = 6.0                             # M4: полная потеря субсидии, эталон 6 п.п.
WNORM = 6.0                          # нормировка индекса (максимальный вес)


def norm(s):
    s = ' '.join(str(s).replace('\n', ' ').split())
    s = (s.replace('\u2013', '-').replace('\u2014', '-').replace('−', '-')
         .replace('H', 'Н').replace('O', 'О').replace('P', 'Р').replace('A', 'А')
         .replace('C', 'С').replace('B', 'В').replace('E', 'Е'))
    return s.lower()


def to_num(v):
    try:
        return float(str(v).replace(',', '.').replace(' ', ''))
    except (TypeError, ValueError):
        return None


def parse_tab4():
    d = pd.read_excel(TAB4, sheet_name='Табл.4', header=None)
    n = len(d)
    SUB = ('в том числе', 'домохозяйства', 'прочие', 'из них', 'с ', 'в них', 'все домохозяйства')
    headers = []
    for i in range(n):
        c0 = d.iloc[i, 0]
        if isinstance(c0, str) and c0.strip() and pd.isna(d.iloc[i, 1]):
            s = ' '.join(c0.replace('\n', ' ').split()).strip()
            low = s.lower()
            if s.startswith('4.') or any(low.startswith(x) for x in SUB):
                continue
            headers.append((i, s))
    out = {}
    for k, (i, name) in enumerate(headers):
        end = headers[k + 1][0] if k + 1 < len(headers) else n
        got = {}
        for j in range(i + 1, end):
            c0 = d.iloc[j, 0]
            if not isinstance(c0, str):
                continue
            low = ' '.join(c0.replace('\n', ' ').split()).strip().lower()
            if low.startswith('из них домохозяйства') and 'детей моложе 18' in low and 'total' not in got:
                got['total'] = to_num(d.iloc[j, 1])
            elif low.startswith('с 1 ребенком') and 'c1' not in got:
                got['c1'] = to_num(d.iloc[j, 1])
            elif low.startswith('с 2 детьми') and 'c2' not in got:
                got['c2'] = to_num(d.iloc[j, 1])
            elif low.startswith('с 3 и более детьми') and 'c3' not in got:
                got['c3'] = to_num(d.iloc[j, 1])
        out[name] = got
    return out


def parse_age():
    d = pd.read_excel(AGE, sheet_name='М+Ж_Г+С', header=None)
    out = {}
    for i in range(len(d)):
        c0 = d.iloc[i, 0]
        if not (isinstance(c0, str) and c0.strip() and not pd.isna(d.iloc[i, 1])):
            continue
        name = ' '.join(c0.replace('\n', ' ').split()).strip()
        if name.lower().startswith('всё население'):
            continue
        out[name] = {
            'pop': to_num(d.iloc[i, 1]),
            'k06': sum(to_num(d.iloc[i, j]) or 0 for j in range(5, 12)),
            'k017': sum(to_num(d.iloc[i, j]) or 0 for j in range(5, 23)),
        }
    return out


def canonical_regions():
    rows = query("""SELECT region_id, name_ru FROM core.region
                    WHERE level='region' AND region_id BETWEEN 10 AND 94
                    ORDER BY region_id""")
    return [(r[0], r[1]) for r in rows]


# источники пишут имена иначе — точечные переопределения (по norm())
OVERRIDE = {
    'г. москва': 27,
    'г. санкт-петербург': 38,
    'г. севастополь': 46,
    'архангельская область без автономного округа': 30,
    'архангельская область без автономии': 30,
    'тюменская область без автономных округов': 70,
    'тюменская область без автономий': 70,
    'ханты-мансийский автономный округ - югра': 71,
    'ханты-мансийский авт. округ - югра': 71,
    'кемеровская область - кузбасс': 80,
    'республика северная осетия - алания': 51,
}
SKIP = {
    'архангельская область',            # полная (с НАО) — агрегат, не субъект
    'тюменская область',                # полная (с ХМАО и ЯНАО) — агрегат
    'российская федерация',
    'центральный федеральный округ', 'северо-западный федеральный округ',
    'южный федеральный округ', 'северо-кавказский федеральный округ',
    'приволжский федеральный округ', 'уральский федеральный округ',
    'сибирский федеральный округ', 'дальневосточный федеральный округ',
}


def match(name, by_norm):
    ns = norm(name)
    if ns in SKIP:
        return None
    if ns in OVERRIDE:
        return OVERRIDE[ns]
    return by_norm.get(ns)


def main():
    write = '--write' in sys.argv
    ensure_sources()
    can = canonical_regions()
    by_norm = {norm(nm): rid for rid, nm in can}
    assert len(can) == 85, f'ожидалось 85 субъектов, получено {len(can)}'

    hh = parse_tab4()
    age = parse_age()

    rec = {}
    unmatched_hh, unmatched_age = [], []
    for nm, v in hh.items():
        rid = match(nm, by_norm)
        if rid is None:
            if norm(nm) not in SKIP:
                unmatched_hh.append(nm)
            continue
        rec.setdefault(rid, {})['hh'] = v
    for nm, v in age.items():
        rid = match(nm, by_norm)
        if rid is None:
            if norm(nm) not in SKIP:
                unmatched_age.append(nm)
            continue
        rec.setdefault(rid, {})['age'] = v

    print(f'сопоставлено субъектов: {len(rec)} из 85')
    if unmatched_hh:
        print('НЕ сопоставлены (домохозяйства):', unmatched_hh)
    if unmatched_age:
        print('НЕ сопоставлены (возраст):', unmatched_age)
    missing = [rid for rid, _ in can if rid not in rec or 'hh' not in rec[rid] or 'age' not in rec[rid]]
    if missing:
        print('НЕТ данных по субъектам:', [(rid, dict(can)[rid]) for rid in missing])

    rows = []
    for rid, nm in can:
        v = rec.get(rid, {})
        h = v.get('hh', {})
        a = v.get('age', {})
        w1, w2 = (W1_CAP, W2_CAP) if rid in CAPITALS else (W1_REG, W2_REG)
        rows.append({'region_id': rid, 'region': nm,
                     'with1': h.get('c1'), 'with2': h.get('c2'), 'with3p': h.get('c3'),
                     'kids_06': a.get('k06'), 'kids_017': a.get('k017'), 'population': a.get('pop'),
                     'w1': w1, 'w2': w2})
    df = pd.DataFrame(rows)

    # --- РФ-агрегат (сумма 85 субъектов; строка РФ в файлах отсутствует) ---
    agg = {'region_id': 1, 'region': 'Российская Федерация',
           'with1': df.with1.sum(), 'with2': df.with2.sum(), 'with3p': df.with3p.sum(),
           'kids_06': df.kids_06.sum(), 'kids_017': df.kids_017.sum(),
           'population': df.population.sum(), 'w1': W1_REG, 'w2': W2_REG}
    df = pd.concat([df, pd.DataFrame([agg])], ignore_index=True)

    # --- производные ---
    T = df.with1 + df.with2 + df.with3p
    p = df.kids_06 / df.kids_017
    df['share_12'] = (df.with1 + df.with2) / T
    df['share_3p'] = df.with3p / T
    df['share_kids06'] = p
    df['s1'] = df.with1 * p / T
    df['s2'] = df.with2 * (1 - (1 - p) ** 2) / T
    df['s3'] = df.with3p * (1 - (1 - p) ** 3) / T
    df['s4'] = (df.with2 * (1 - p) ** 2 + df.with3p * (1 - p) ** 3) / T
    df['exposure_pp'] = df.w1 * df.s1 + df.w2 * df.s2 + W4 * df.s4
    df['exposure_gross'] = df.exposure_pp / WNORM
    df['exposure_share'] = df.s1 + df.s2 + df.s4
    df['exposure_old'] = df.share_12 * (1 - df.share_kids06)

    # --- контроль: агрегат РФ против строки РФ в файле возрастной структуры ---
    rf_file = age.get('Российская Федерация', {})
    rf_sum = df[df.region_id == 1].iloc[0]
    print('\n== контроль агрегата РФ (сумма 85 субъектов против строки файла) ==')
    for label, got, ref in (('kids_06', rf_sum.kids_06, rf_file.get('k06')),
                            ('kids_017', rf_sum.kids_017, rf_file.get('k017')),
                            ('population', rf_sum.population, rf_file.get('pop'))):
        d = (got - ref) if ref else None
        print(f'  {label:10s} сумма={got:.0f} файл={ref} расхождение={d}')

    print('\n== 9 уральских регионов: старое и новое определение ==')
    ural = [54, 60, 63, 68, 69, 70, 71, 72, 73]   # Башк, Пермь, Оренб, Курган, Свердл, Тюмень(б/АО), ХМАО, ЯНАО, Челяб
    for rid in ural:
        r = df[df.region_id == rid].iloc[0]
        print(f'  {r.region[:42]:42s} old={r.exposure_old:.4f}  share={r.exposure_share:.4f}  gross={r.exposure_gross:.4f}')

    print('\n== экспозиция (пересборка) ==')
    cols = ['region', 'share_12', 'share_3p', 'share_kids06', 's1', 's2', 's4',
            'exposure_share', 'exposure_pp', 'exposure_gross', 'exposure_old']
    print(df[cols].round(4).to_string(index=False))

    if not write:
        print('\n[dry run] запись не выполнялась; добавьте --write')
        return

    # --- бэкап текущих таблиц ---
    bdir = os.path.expanduser('~/research-wiki-private/backups/vpn20261001')
    os.makedirs(bdir, exist_ok=True)
    for t in ('vpn_households_children', 'rosstat_children_06', 'did_exposure_reform2026'):
        try:
            cur = pd.DataFrame(query(f'SELECT * FROM {t}'))
            cur.to_csv(os.path.join(bdir, t + '.csv'), index=False)
            print('бэкап:', os.path.join(bdir, t + '.csv'))
        except Exception as e:
            print('бэкап', t, 'не сделан:', str(e)[:80])

    ddl = """
    DROP TABLE IF EXISTS vpn_households_children CASCADE;
    CREATE TABLE vpn_households_children (
        region TEXT PRIMARY KEY, with1 NUMERIC, with2 NUMERIC, with3p NUMERIC,
        share_3p NUMERIC, share_12 NUMERIC);
    DROP TABLE IF EXISTS rosstat_children_06 CASCADE;
    CREATE TABLE rosstat_children_06 (
        region TEXT PRIMARY KEY, kids_06 NUMERIC, kids_017 NUMERIC,
        population NUMERIC, share_kids06 NUMERIC);
    DROP TABLE IF EXISTS did_exposure_reform2026 CASCADE;
    CREATE TABLE did_exposure_reform2026 (
        region TEXT PRIMARY KEY, region_id BIGINT,
        n_hh_children NUMERIC, share_12 NUMERIC, share_3p NUMERIC, share_kids06 NUMERIC,
        s1 NUMERIC, s2 NUMERIC, s3 NUMERIC, s4 NUMERIC,
        w1 NUMERIC, w2 NUMERIC, w4 NUMERIC, is_capital BOOLEAN,
        exposure_pp NUMERIC, exposure_gross NUMERIC, exposure_share NUMERIC,
        exposure_old NUMERIC);
    """
    for stmt in [s for s in ddl.split(';') if s.strip()]:
        execute(stmt)

    hh_ins = df[['region', 'with1', 'with2', 'with3p', 'share_3p', 'share_12']].values.tolist()
    age_ins = df[['region', 'kids_06', 'kids_017', 'population', 'share_kids06']].values.tolist()
    exp_ins = df[['region', 'region_id', 'with1', 'with2', 'with3p', 'share_12', 'share_3p',
                  'share_kids06', 's1', 's2', 's3', 's4', 'w1', 'w2']].copy()
    exp_ins['w4'] = W4
    exp_ins['is_capital'] = exp_ins.region_id.isin(CAPITALS)
    exp_ins['exposure_pp'] = df.exposure_pp
    exp_ins['exposure_gross'] = df.exposure_gross
    exp_ins['exposure_share'] = df.exposure_share
    exp_ins['exposure_old'] = df.exposure_old
    exp_ins = exp_ins[['region', 'region_id', 'with1', 'with2', 'with3p', 'share_12', 'share_3p',
                       'share_kids06', 's1', 's2', 's3', 's4', 'w1', 'w2', 'w4', 'is_capital',
                       'exposure_pp', 'exposure_gross', 'exposure_share', 'exposure_old']]
    # with1..with3p = n_hh_children components; в витрине храним как n_hh_children
    exp_vals = exp_ins.values.tolist()

    from db_tunnel import execute_many
    execute_many("""INSERT INTO vpn_households_children
        (region, with1, with2, with3p, share_3p, share_12) VALUES (%s,%s,%s,%s,%s,%s)""", hh_ins)
    execute_many("""INSERT INTO rosstat_children_06
        (region, kids_06, kids_017, population, share_kids06) VALUES (%s,%s,%s,%s,%s)""", age_ins)
    execute_many("""INSERT INTO did_exposure_reform2026
        (region, region_id, n_hh_children, share_12, share_3p, share_kids06, s1, s2, s3, s4,
         w1, w2, w4, is_capital, exposure_pp, exposure_gross, exposure_share, exposure_old)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                 [[v[0], v[1], (v[2] or 0) + (v[3] or 0) + (v[4] or 0)] + v[5:] for v in exp_vals])
    execute("GRANT SELECT ON vpn_households_children TO viewer")
    execute("GRANT SELECT ON rosstat_children_06 TO viewer")
    execute("GRANT SELECT ON did_exposure_reform2026 TO viewer")

    for t in ('vpn_households_children', 'rosstat_children_06', 'did_exposure_reform2026'):
        n = query(f'SELECT count(*) FROM {t}')[0][0]
        print(f'записано {t}: {n} строк')


if __name__ == '__main__':
    main()