#!/usr/bin/env python3
"""Wordstat: ряд строительной активности — недельная база плюс дневное продление.

Две гранулярности, потому что у них разный лаг:
  * недельная — весь ряд с 2018 года, но доступна с отставанием около двух недель;
  * дневная — только последние ~60 дней, зато отставание около четырёх дней.

Дневные значения суммируются в недели (понедельник…воскресенье) и добавляются к недельному ряду
только для тех недель, которых в нём ещё нет. Совпадение проверяется на перекрытии: сумма дневных
за неделю, которая уже есть в недельном ряду, должна давать то же число (расхождение < 0,5 %).

Выходы:
  data/wordstat_weekly_construction.csv      — основной ряд (date, phrase, group, count, share)
  data/wordstat_daily_construction.csv       — дневные точки последнего окна
  data/wordstat_weekly_provenance.json       — происхождение недель: api | daily_sum, число дней

Диапазон запроса всегда вычисляется от текущей даты. У недельной гранулярности toDate обязан быть
воскресеньем, у месячной — последним днём месяца; захардкоженные даты здесь запрещены (один раз
такая константа уже стоила трёх недель данных).
"""
import csv
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from repo_paths import require_repo  # noqa: E402
os.chdir(require_repo())
from wordstat_api import dynamics  # noqa: E402

PHRASES = [
    # S1. Индивидуальное жилищное строительство
    ("строительство домов под ключ", "S1_ihb"),
    ("проектирование дома", "S1_ihb"),
    ("смета на строительство", "S1_ihb"),
    # S2. Спрос на материалы
    ("доставка бетона", "S2_mat"),
    ("бетон с доставкой цена", "S2_mat"),
    ("блоки бетонные купить", "S2_mat"),
    ("аренда бетононасоса", "S2_mat"),
    # S3. Аренда техники (B2B, активные площадки)
    ("аренда спецтехники", "S3_mach"),
    ("экскаватор аренда", "S3_mach"),
    ("аренда крана", "S3_mach"),
    ("аренда гусеничного экскаватора", "S3_mach"),
    ("аренда экскаватора погрузчика", "S3_mach"),
    # S4. Подряд и закупки
    ("строительная компания", "S4_b2b"),
    ("строительная фирма", "S4_b2b"),
    ("строительный подрядчик", "S4_b2b"),
    ("подряд на строительство", "S4_procure"),
    ("тендер на строительство", "S4_procure"),
    # S5. Регулирование
    ("разрешение на строительство", "S5_permits"),
    # D. Широкие фразы-знаменатели
    ("стройка", "D_broad"),
    ("строительство", "D_broad"),
]

WEEKLY = 'data/wordstat_weekly_construction.csv'
DAILY = 'data/wordstat_daily_construction.csv'
PROV = 'data/wordstat_weekly_provenance.json'
DAILY_WINDOW = 58          # дней назад: предел дневной гранулярности у Wordstat около 60 дней
SLEEP = 8                  # пауза между вызовами: у API есть и часовой, и минутный лимит
RETRY_WAIT = 75            # при HTTP 429 ждём окно лимита
WEEKLY_FROM = '2018-01-01'  # понедельник: у недельной гранулярности начало диапазона тоже выравнивается


def call(phrase, granularity, date_from, date_to, retries=3):
    """Вызов с ожиданием при исчерпании лимита: 429 означает «повтори позже», а не ошибку данных."""
    for attempt in range(retries):
        try:
            return dynamics(phrase, granularity, date_from, date_to)
        except Exception as e:
            if '429' in str(e) and attempt < retries - 1:
                print(f'    лимит API (429), пауза {RETRY_WAIT} с', flush=True)
                time.sleep(RETRY_WAIT)
                continue
            raise


def collect(granularity, date_to, phrases, date_from):
    out, ok_phrases = [], set()
    for i, (ph, grp) in enumerate(phrases, 1):
        try:
            res = call(ph, granularity, date_from, date_to)
            print(f'  [{i}/{len(phrases)}] {ph!r}: {len(res)} точек', flush=True)
            for r in res:
                out.append({"date": r["date"], "phrase": ph, "group": grp,
                            "count": int(r["count"]), "share": float(r["share"])})
            ok_phrases.add(ph)
        except Exception as e:
            print(f'  [{i}] {ph!r}: ОШИБКА {str(e)[:70]}', flush=True)
        time.sleep(SLEEP)
    return out, ok_phrases


def week_start(d):
    """Понедельник недели, к которой относится дата."""
    x = dt.date.fromisoformat(d)
    return (x - dt.timedelta(days=x.weekday())).isoformat()


def main():
    today = dt.date.today()
    last_sunday = today - dt.timedelta(days=(today.weekday() + 1) % 7)
    print(f'сегодня {today}; недельный диапазон: {WEEKLY_FROM} .. {last_sunday}', flush=True)

    weekly, ok_w = collect('PERIOD_WEEKLY', last_sunday.isoformat(), PHRASES, WEEKLY_FROM)
    print(f'недельных точек получено: {len(weekly)} (фраз без ошибок: {len(ok_w)}/{len(PHRASES)})', flush=True)

    # Дневное окно: пробуем от последней даты назад, при отказе сдвигаем начало вперёд.
    daily, ok_d, window_from = [], set(), None
    for back in (DAILY_WINDOW, DAILY_WINDOW - 10, DAILY_WINDOW - 20, DAILY_WINDOW - 30, DAILY_WINDOW - 40):
        window_from = (today - dt.timedelta(days=back))
        try:
            probe = call(PHRASES[-1][0], 'PERIOD_DAILY', window_from.isoformat(), today.isoformat(), retries=2)
            if probe:
                print(f'дневное окно принято: {window_from} .. {today} ({len(probe)} точек у фразы-пробника)', flush=True)
                daily, ok_d = collect('PERIOD_DAILY', today.isoformat(), PHRASES, window_from.isoformat())
                break
        except Exception as e:
            print(f'дневное окно от {window_from} отклонено ({str(e)[:40]}), сдвигаем', flush=True)
        time.sleep(SLEEP)
    print(f'дневных точек получено: {len(daily)} (фраз без ошибок: {len(ok_d)}/{len(PHRASES)})', flush=True)

    # Дневной файл пишем сразу: он не зависит от недельного слияния и не должен теряться при сбое ниже.
    if daily:
        with open(DAILY, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=["date", "phrase", "group", "count", "share"])
            w.writeheader()
            w.writerows(sorted(daily, key=lambda r: (r['date'], r['phrase'])))
        print(f'сохранён {DAILY}', flush=True)

    # Слияние с прежним файлом: строки фраз, которые в этом прогоне не собрались, сохраняем как были.
    old_rows = []
    if os.path.exists(WEEKLY):
        with open(WEEKLY, encoding='utf-8') as f:
            old_rows = [r for r in csv.DictReader(f)]
    kept = [dict(r, count=int(r['count']), share=float(r['share']))
            for r in old_rows if r['phrase'] not in ok_w]
    merged = kept + [{k: (int(v) if k == 'count' else float(v) if k == 'share' else v)
                      for k, v in r.items()} for r in weekly]
    print(f'слияние: сохранено прежних строк {len(kept)}, обновлено {len(weekly)}', flush=True)

    # Недельные агрегаты из дневных (только по фразам, которые собрались в обоих разрезах)
    agg = {}
    for r in daily:
        if r['phrase'] not in ok_d:
            continue
        key = (week_start(r['date']), r['phrase'])
        a = agg.setdefault(key, {'group': r['group'], 'count': 0, 'days': 0, 'share_sum': 0.0})
        a['count'] += r['count']
        a['days'] += 1
        a['share_sum'] += r['share']

    have = {(r['date'], r['phrase']) for r in merged}
    prov = {f"{r['date']}|{r['phrase']}": {'source': 'api', 'days': 7} for r in merged}

    # Калибровка сшивки: дневные суммы систематически выше недельных значений, причём тем сильнее,
    # чем меньше объём фразы (проверено на перекрытии: 24.08-14.09). Считаем медианный множитель
    # недельное/дневное по полным неделям перекрытия и применяем его к неделям из дневного слоя,
    # чтобы уровень ряда не дёргался на стыке.
    import statistics
    ratios = {}
    for ph in {p for _, p in agg}:
        rr = []
        for (wk, ph2), a in agg.items():
            if ph2 != ph or a['days'] != 7:
                continue
            api = next((r['count'] for r in merged if r['date'] == wk and r['phrase'] == ph), None)
            if api and a['count']:
                rr.append(api / a['count'])
        if rr:
            ratios[ph] = statistics.median(rr)
    if ratios:
        small = sorted(ratios.items(), key=lambda kv: kv[1])[:3]
        print('калибровка сшивки (медиана недельное/дневное): '
              + ', '.join(f'{p} {v:.4f}' for p, v in small), flush=True)

    diffs = []
    for (wk, ph), a in agg.items():
        if a['days'] == 7 and (wk, ph) in have:
            api = next((r['count'] for r in merged if r['date'] == wk and r['phrase'] == ph), None)
            if api:
                diffs.append(abs(a['count'] - api) / api)
    if diffs:
        print('сверка перекрытия: недель %d, среднее расхождение %.3f%%, максимум %.3f%%'
              % (len(diffs), 100 * sum(diffs) / len(diffs), 100 * max(diffs)), flush=True)

    added = 0
    for (wk, ph), a in sorted(agg.items()):
        if (wk, ph) in have:
            continue
        k = ratios.get(ph, 1.0)
        merged.append({'date': wk, 'phrase': ph, 'group': a['group'],
                       'count': int(round(a['count'] * k)),
                       'share': round(a['share_sum'] / max(a['days'], 1), 12)})
        prov[f'{wk}|{ph}'] = {'source': 'daily_sum', 'days': a['days'],
                              'calibration': round(k, 4), 'partial': a['days'] < 7}
        added += 1
    print(f'добавлено недель из дневных: {added}', flush=True)

    if not ok_w and not ok_d:
        print('ни одна фраза не собралась — файлы не перезаписываем')
        return 1

    merged.sort(key=lambda r: (r['date'], r['phrase']))
    with open(WEEKLY, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=["date", "phrase", "group", "count", "share"])
        w.writeheader()
        w.writerows(merged)
    if daily:
        with open(DAILY, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=["date", "phrase", "group", "count", "share"])
            w.writeheader()
            w.writerows(sorted(daily, key=lambda r: (r['date'], r['phrase'])))
    json.dump(prov, open(PROV, 'w', encoding='utf-8'), ensure_ascii=False)

    ph_ref = 'строительство'
    last_week = max(r['date'] for r in merged if r['phrase'] == ph_ref)
    last_day = max((r['date'] for r in daily), default='—')
    partial = [k for k, v in prov.items() if v['source'] == 'daily_sum' and v['days'] < 7]
    print(f'итог: строк {len(merged)}, последняя неделя {last_week}, последний день {last_day}, '
          f'неполных недель из дневных: {len(partial)}')
    print(f'сохранено: {WEEKLY}, {DAILY}, {PROV}')


if __name__ == '__main__':
    WINDOW_FROM = '2026-08-01'
    main()