#!/usr/bin/env python3
"""Загрузка компонентных рядов ИПЦ (группы и товары-представители) в канон.

Источник: Росстат, справочные таблицы «Индексы потребительских цен на товары и
услуги по Российской Федерации» — файл https://rosstat.gov.ru/storage/mediabank/
ipc_spr_MM-YYYY.xlsx. Файл накопительный: по листу на каждый месяц, в листе
наименование, локальный код группы/товара, вес в структуре потребительских
расходов и три индекса (к предыдущему месяцу, к декабрю предыдущего года,
к соответствующему месяцу предыдущего года).

Что делает скрипт:
  * качает файл (или берёт локальный через --file), разбирает все листы-месяцы;
  * собирает плоскую панель и проверяет её двумя контролями:
      1) цепной индекс «Все товары и услуги» за январь-сентябрь 2026 совпадает
         с опубликованным «к декабрю предыдущего года»;
      2) взвешенная по весам сумма приростов трёх верхних групп сходится
         с приростом агрегата (допуск 0.05 п.п.), сверка минимум в 95% месяцев;
  * пишет метрики `rosstat_cpi_cmp_<код>_mom` и наблюдения по РФ в
    catalog.metric / data.observation, релиз в catalog.release.

Запись только при --apply. По умолчанию dry-run.
"""
import argparse
import datetime as dt
import hashlib
import io
import os
import re
import ssl
import sys
import time
import urllib.request
from pathlib import Path

import openpyxl

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / 'scripts'))
import db_tunnel  # noqa: E402

URL_TPL = 'https://rosstat.gov.ru/storage/mediabank/ipc_spr_{mm}-{yyyy}.xlsx'
SOURCE_ROSSTAT = 11
UNIT_PCT = 12
FREQ_MONTH = 5
REGION_RU = 1
TOL_AGG = 0.05
MIN_SHARE_OK = 0.95
DATA_DIR = REPO / 'data' / 'cpi-components'

# верхние группы: (код, вес) — проверяются на полноту весов
TOP_GROUPS = ('6', '7', '9000')


def norm_name(s: str) -> str:
    s = str(s).replace('\u00ad', '')
    s = re.sub(r'[\r\n\t]+', ' ', s)
    s = re.sub(r'\s{2,}', ' ', s)
    return s.strip()


def slug(code: str) -> str:
    s = str(code).strip().lower()
    s = s.replace('аг', 'ag')
    s = re.sub(r'[^0-9a-z]+', '', s)
    return s


def download(year: int, month: int) -> Path:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    dest = DATA_DIR / f'ipc_spr_{month:02d}-{year}.xlsx'
    if dest.exists() and dest.stat().st_size > 10_000:
        return dest
    url = URL_TPL.format(mm=f'{month:02d}', yyyy=year)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=120, context=ctx) as r:
                blob = r.read()
            if len(blob) < 10_000:
                raise RuntimeError(f'подозрительно малый файл: {len(blob)} байт')
            dest.write_bytes(blob)
            return dest
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(3 * (attempt + 1))
    raise RuntimeError(f'не удалось скачать {url}: {last}')


def parse(path: Path) -> dict[str, dict[str, tuple[str, float, float, float, float]]]:
    """{sheet: {code: (name, weight, mom, ytd, yoy)}}"""
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    sheets = [s for s in wb.sheetnames if s != 'Содержание']
    out = {}
    for sh in sheets:
        ws = wb[sh]
        rows = ws.iter_rows(values_only=True)
        d = {}
        for r in rows:
            if not r or len(r) < 6 or not r[0] or r[1] is None:
                continue
            code = str(r[1]).strip()
            if not re.match(r'^\d{1,5}(\.\D+)?$', code):
                continue           # строки шапки: «Локальный код группы / товара»
            d[code] = (norm_name(r[0]), r[2], r[3], r[4], r[5])
        out[sh] = d
    wb.close()
    return out


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def sheet_period(sh: str) -> dt.date:
    if len(sh) == 7 and sh[:2] == '09':   # опечатка Росстата: лист 0922025 вместо 092025
        sh = sh[:2] + sh[3:]
    m = re.match(r'^(\d{1,2})(\d{4})$', sh)
    if not m:
        raise ValueError(f'непонятный лист: {sh}')
    month = int(m.group(1))
    if not 1 <= month <= 12:
        raise ValueError(f'непонятный лист: {sh}')
    return dt.date(int(m.group(2)), month, 1)


def validate(table, sheets):
    """Контроль 1: цепь; контроль 2: взвешенная сумма верхних групп."""
    sheets = sorted(sheets, key=sheet_period)
    problems = []

    # 1) цепь «Все товары и услуги» от января 2026 к сентябрю 2026
    y2026 = [s for s in sheets if s.endswith('2026')]
    if y2026:
        chain = 1.0
        for s in y2026:
            chain *= table[s]['1'][2] / 100.0
        published = table[y2026[-1]]['1'][3] / 100.0
        diff = (chain - published) * 100
        print(f'контроль 1 (цепь vs к декабрю): {chain*100-100:.2f}% против {published*100-100:.2f}%, '
              f'расхождение {diff:+.3f} п.п.')
        if abs(diff) > 0.05:
            problems.append(f'цепь не сходится с публикацией: {diff:+.3f} п.п.')

    # 2) взвешенная сумма трёх верхних групп против агрегата
    ok = total = 0
    worst = []
    for s in sheets:
        d = table[s]
        if any(g not in d for g in TOP_GROUPS):
            continue
        wsum = sum(d[g][1] for g in TOP_GROUPS)
        if abs(wsum - 100) > 0.5:
            problems.append(f'{s}: сумма весов верхних групп {wsum:.2f} != 100')
            continue
        agg = d['1'][2]
        mix = sum(d[g][1] * d[g][2] for g in TOP_GROUPS) / wsum
        total += 1
        if abs(mix - agg) <= TOL_AGG:
            ok += 1
        else:
            worst.append((s, mix, agg))
    share = ok / total if total else 0
    print(f'контроль 2 (взвешенная сумма групп): {ok}/{total} месяцев в допуске '
          f'{TOL_AGG} п.п. ({share:.1%})')
    for s, mix, agg in worst[:5]:
        print(f'   ! {s}: смесь {mix:.2f} vs агрегат {agg:.2f}')
    if share < MIN_SHARE_OK:
        problems.append(f'сборка не сходится: {share:.1%} месяцев, требуется >= {MIN_SHARE_OK:.0%}')

    # 3) сверка цепи за 12 месяцев с опубликованным г/г на последнем листе
    last = sheets[-1]
    lp = sheet_period(last)
    window = []
    for k in range(12):
        m = lp.month - k
        y = lp.year + (m - 1) // 12
        m = (m - 1) % 12 + 1
        p = dt.date(y, m, 1)
        sh = next((x for x in sheets if sheet_period(x) == p), None)
        if sh is None:
            window = []
            break
        window.append(sh)
    checked = bad = 0
    worst = []
    if window:
        window.reverse()
        for code, row in table[last].items():
            if row[4] is None:
                continue
            chain = 1.0
            okc = True
            for sh in window:
                val = table[sh].get(code, (None, None, None, None, None))[2]
                if val is None:
                    okc = False
                    break
                chain *= val / 100.0
            if not okc:
                continue
            checked += 1
            diff = chain * 100 - row[4]   # обе величины — уровни индекса, не темпы
            if abs(diff) > 0.25:
                bad += 1
                worst.append((code, round(diff, 2)))
        print(f'контроль 3 (цепь 12 месяцев vs г/г): сверено {checked}, '
              f'расхождений {bad} ({bad/checked:.2%})')
        for code, diff in sorted(worst, key=lambda x: -abs(x[1]))[:5]:
            print(f'   ! код {code}: разница {diff:+.2f} п.п.')
        if checked and bad / checked > 0.05:
            problems.append(f'г/г не сходится у {bad/checked:.0%} рядов')
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--year', type=int, default=None)
    ap.add_argument('--month', type=int, default=None)
    ap.add_argument('--file', type=Path, default=None)
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args()

    today = dt.date.today()
    year = args.year or today.year
    month = args.month or today.month
    path = args.file or download(year, month)
    print(f'файл: {path}  sha256={sha256(path)[:16]}…')

    table = parse(path)
    sheets = list(table.keys())
    ordered0 = sorted(sheets, key=sheet_period)
    print(f'листов-месяцев: {len(sheets)} ({ordered0[0]} … {ordered0[-1]}), '
          f'рядов в последнем: {len(table[ordered0[-1]])}')

    problems = validate(table, sheets)
    if problems and not args.force:
        print('ОСТАНОВ: контроль не пройден')
        for p in problems:
            print('   -', p)
        return 2
    for p in problems:
        print('   ! (force)', p)

    # все коды, встречающиеся хотя бы в одном месяце
    codes = {}
    for s in sheets:
        for code, row in table[s].items():
            codes.setdefault(code, row[0])
    print(f'уникальных компонентов: {len(codes)}')

    # панель в файл (для воспроизводимости и для H-13)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ordered = sorted(sheets, key=sheet_period)
    first_sh, last_sh = ordered[0], ordered[-1]
    panel = DATA_DIR / f'cpi_components_panel_{sheet_period(first_sh):%Y-%m}-{sheet_period(last_sh):%Y-%m}.csv'
    weights = DATA_DIR / f'cpi_weights_{sheet_period(last_sh):%Y-%m}.csv'
    with panel.open('w', encoding='utf-8') as fh:
        fh.write('metric_code;period;name_ru;weight_pct;mom;ytd;yoy\n')
        for s in sorted(sheets, key=sheet_period):
            p = sheet_period(s).isoformat()
            for code, (name, w, mom, ytd, yoy) in sorted(table[s].items()):
                fh.write(f'rosstat_cpi_cmp_{slug(code)}_mom;{p};{name};{w};{mom};{ytd};{yoy}\n')
    last = max(sheets, key=sheet_period)
    with weights.open('w', encoding='utf-8') as fh:
        fh.write('local_code;metric_code;name_ru;weight_pct\n')
        for code, (name, w, *_rest) in sorted(table[last].items()):
            fh.write(f'{code};rosstat_cpi_cmp_{slug(code)}_mom;{name};{w}\n')
    print(f'панель: {panel} ({panel.stat().st_size} байт)')
    print(f'веса: {weights}')

    if not args.apply:
        sample = [(c, codes[c]) for c in list(codes)[:3]]
        print('DRY-RUN. Примеры:', sample)
        return 0

    # --- запись ---
    label = f'rosstat_ipc_spr_{year}-{month:02d}'
    url = URL_TPL.format(mm=f'{month:02d}', yyyy=year)
    digest = sha256(path)
    rel = db_tunnel.query('select release_id from catalog.release where label=%s', (label,))
    if rel:
        release_id = rel[0][0]
        db_tunnel.execute("""update catalog.release set status='loaded', ingested_at=now(),
                             content_hash=%s, url=%s where release_id=%s""",
                          (digest, url, release_id))
    else:
        release_id = db_tunnel.query(
            """insert into catalog.release (source_id, label, published_at, content_hash,
                                            status, ingested_at, url, notes)
               values (%s,%s,%s,%s,'loaded',now(),%s,%s) returning release_id""",
            (SOURCE_ROSSTAT, label, dt.datetime(year, month, 10, tzinfo=dt.timezone.utc),
             digest, url,
             'ИПЦ по группам и товарам-представителям (справочные таблицы ipc_spr), РФ'))
        release_id = release_id[0][0]
    print(f'release_id={release_id}')

    # метрики
    rows = []
    for code, name in codes.items():
        mc = f'rosstat_cpi_cmp_{slug(code)}_mom'
        w = table[last].get(code, (None, None))[1] if code in table[last] else None
        desc = (f'Росстат, ИПЦ на «{name}», % к предыдущему месяцу, РФ. Локальный код '
                f'группы/товара {code}' + (f', вес {w:.3f}% в структуре расходов 2026' if w else ''))
        rows.append((mc, name[:180], desc))
    n = db_tunnel.execute_many(
        """insert into catalog.metric (metric_code, name_ru, description, unit_id, source_id,
                                       frequency_id, metric_type, is_derived, status, tags)
           values (%s,%s,%s,%s,%s,%s,'primary',false,'active',%s)
           on conflict (metric_code) do update set name_ru=excluded.name_ru,
               description=excluded.description, is_active=true""",
        [(mc, nm, ds, UNIT_PCT, SOURCE_ROSSTAT, FREQ_MONTH, ['cpi', 'component', 'rosstat', 'inflation'])
         for mc, nm, ds in rows])
    print(f'метрик записано/обновлено: {n}')

    # наблюдения
    obs = []
    for s in sorted(sheets, key=sheet_period):
        ps = sheet_period(s)
        pe = (ps + dt.timedelta(days=32)).replace(day=1) - dt.timedelta(days=1)
        for code, (name, w, mom, ytd, yoy) in table[s].items():
            mc = f'rosstat_cpi_cmp_{slug(code)}_mom'
            obs.append((mc, REGION_RU, ps, pe, mom, release_id,
                        f'Росстат ipc_spr_{month:02d}-{year}, лист {s}, код {code}'))
    db_tunnel.execute(
        """delete from data.observation where metric_id in
             (select metric_id from catalog.metric where metric_code like 'rosstat_cpi_cmp_%%')
           and release_id=%s""", (release_id,))
    n_obs = db_tunnel.execute_many(
        """insert into data.observation (metric_id, region_id, period_start, period_end, value,
               observation_status, assessment_type, release_id, frequency_id, source_id,
               quality_flags, notes)
           values ((select metric_id from catalog.metric where metric_code=%s),
                   %s,%s,%s,%s,'validated','final',%s,5,%s,'{}',%s)""",
        [(mc, rid, ps, pe, val, rel, SOURCE_ROSSTAT, note)
         for mc, rid, ps, pe, val, rel, note in obs])
    print(f'наблюдений вставлено: {n_obs}')

    chk = db_tunnel.query(
        """select count(distinct m.metric_id), count(*), min(o.period_start), max(o.period_start)
           from data.observation o join catalog.metric m using(metric_id)
           where m.metric_code like 'rosstat_cpi_cmp_%%'""")
    print(f'в каноне: {chk[0][0]} рядов, {chk[0][1]} наблюдений, {chk[0][2]} … {chk[0][3]}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
