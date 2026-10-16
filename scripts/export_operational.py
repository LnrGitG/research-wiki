#!/usr/bin/env python3
"""Экспорт оперативных рядов в docs/data/operational_dashboard.json
для GitHub Pages (docs/operational.html).

Источники — канон PostgreSQL (`data.observation` + `catalog.metric`), плюс
SQLite-файл только для мониторинга ЦБ: прежние таблицы
`housing_input_operational_monthly`, `construction_volume_monthly_rf`,
`construction_contracts_monthly_rf`, `cbr_escrow_monthly`,
`average_wage_monthly_regional` в `data/rosstat_construction.db` исчезли при
замене схемы файла 05.10.2026 (осталась лишь `cbr_monitoring_construction`),
из-за чего дашборд застыл на снимке 19.09.

Соответствие рядов (канон):
  rosstat_housing_total_m / rosstat_housing_pop_m → housing_input (всего / ИЖС)
  kep1_72                                         → construction_works (СМР, млрд ₽)
  kep1_73                                         → construction_works_agg (кварталы)
  zdspmr + odpm                                   → contracts
  kvse + osse                                     → escrow (счета / остаток)
  snz                                             → wage (РФ, руб/мес)

Запуск: python3 scripts/export_operational.py
"""
import json
import os
import sys
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from db_tunnel import query
except Exception as exc:  # noqa: BLE001
    print('db_tunnel недоступен: %s' % exc)
    raise SystemExit(1)

try:
    from yc_sync import ensure_db
except Exception:  # noqa: BLE001
    ensure_db = None

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT = REPO_ROOT / 'docs' / 'data'
os.makedirs(OUT, exist_ok=True)
RF = 'Российская Федерация%'


def _num(v):
    return float(v) if isinstance(v, Decimal) else v


def monthly_rf(code):
    """Ряд по РФ помесячно: {date(period_start): value}."""
    rows = query(
        """
        SELECT o.period_start, o.value
        FROM data.observation o
        JOIN catalog.metric m ON m.metric_id = o.metric_id
        LEFT JOIN catalog.region r ON r.region_id = o.region_id
        WHERE m.metric_code = %s AND r.name_ru ILIKE %s
        ORDER BY o.period_start
        """,
        (code, RF),
    )
    out = {}
    for d, v in rows:
        out[(d.year, d.month)] = _num(v)
    return out


def with_yoy(series):
    """Добавить индекс г/г (значение / тот же месяц год назад * 100)."""
    out = {}
    for (y, m), v in series.items():
        prev = series.get((y - 1, m))
        out[(y, m)] = {'value': v, 'yoy': round(v / prev * 100, 1) if prev else None}
    return out


def cumulative_with_yoy(series):
    """Накопительный итог с начала года + индекс г/г по тому же периоду."""
    cum = {}
    for (y, m), v in series.items():
        cum[(y, m)] = cum.get((y, m - 1), 0.0) + v if m > 1 else v
    out = {}
    for (y, m), v in cum.items():
        prev = cum.get((y - 1, m))
        out[(y, m)] = {'value': v, 'yoy': round(v / prev * 100, 1) if prev else None}
    return out


def key(ym):
    return '%04d-%02d' % ym


D = {}

# ---------- 1. Ввод жилья (всего и ИЖС), помесячно + накопленным итогом ----------
tot = monthly_rf('rosstat_housing_total_m')
ind = monthly_rf('rosstat_housing_pop_m')
tot_m, tot_c = with_yoy(tot), cumulative_with_yoy(tot)
ind_m, ind_c = with_yoy(ind), cumulative_with_yoy(ind)
series = {}
for ym in sorted(set(list(tot_m) + list(ind_m))):
    rec = {}
    if ym in tot_m:
        rec['housing_input_total_monthly'] = tot_m[ym]
        rec['housing_input_total_cumulative'] = tot_c[ym]
    if ym in ind_m:
        rec['housing_input_individual_monthly'] = ind_m[ym]
        rec['housing_input_individual_cumulative'] = ind_c[ym]
    series[key(ym)] = rec
D['housing_input'] = {
    'name': 'Ввод жилья (оперативно)', 'unit': 'тыс. м²',
    'source': 'Росстат jil_dom-oper (канон: rosstat_housing_total_m/pop_m)',
    'monthly': series,
}

# ---------- 2. СМР (объём работ по виду деятельности «Строительство») ----------
works = monthly_rf('kep1_72')
works_my = with_yoy(works)
D['construction_works'] = {
    'name': 'СМР', 'unit': 'млрд руб.',
    'source': 'Росстат КЭП 1.7 (канон: kep1_72)',
    'monthly': {key(ym): works_my[ym] for ym in sorted(works_my)},
}
# квартальные агрегаты
q_rows = query(
    """
    SELECT o.period_start, o.value FROM data.observation o
    JOIN catalog.metric m ON m.metric_id = o.metric_id
    WHERE m.metric_code = 'kep1_73'
    ORDER BY o.period_start
    """
)
agg = {}
for d, v in q_rows:
    agg[(d.year, (d.month - 1) // 3 + 1)] = _num(v)
QLAB = {1: 'I квартал', 2: 'II квартал', 3: 'III квартал', 4: 'IV квартал'}
D['construction_works_agg'] = [
    {'label': QLAB[q], 'year': y, 'value': v,
     'yoy': round(v / agg[(y - 1, q)], 1) if agg.get((y - 1, q)) else None}
    for (y, q), v in sorted(agg.items())
]

# ---------- 3. Договоры строительного подряда (квартальные) ----------
con = monthly_rf('zdspmr')
back = monthly_rf('odpm')
D['contracts'] = {
    'name': 'Договоры строительного подряда', 'unit': 'млрд руб.',
    'source': 'Росстат (канон: zdspmr + odpm)',
    'monthly': {key(ym): {'value': con[ym], 'backlog': back.get(ym)} for ym in sorted(con)},
}

# ---------- 4. Мониторинг ЦБ (SQLite: таблица cbr_monitoring_construction) ----------
if ensure_db is not None:
    import sqlite3
    cur = sqlite3.connect(str(ensure_db('rosstat_construction.db'))).cursor()
    QMAP = {}
    for (q,) in cur.execute("SELECT DISTINCT question FROM cbr_monitoring_construction"):
        if '(ожид.)' in q:
            QMAP[q] = 'ibk_expected'
        elif '(факт.)' in q:
            QMAP[q] = 'ibk_actual'
        elif q.startswith('Индикатор'):
            QMAP[q] = 'ibk'
        elif 'объем производства' in q and 'ближайшие' not in q:
            QMAP[q] = 'production'
        elif 'спрос на' in q and 'ближайшие' not in q:
            QMAP[q] = 'demand'
        elif 'цены на готовую' in q:
            QMAP[q] = 'prices'
        elif 'Ценовые ожидания' in q:
            QMAP[q] = 'price_expectations'
        elif 'издержки' in q:
            QMAP[q] = 'costs'
        elif 'условия кредитования' in q:
            QMAP[q] = 'credit_conditions'
    mon = {}
    for d, q, adj, v in cur.execute(
            "SELECT date, question, adjustment, value FROM cbr_monitoring_construction"):
        k = QMAP.get(q)
        if not k or v is None:
            continue
        adj_key = 'raw' if adj == 'Исходные данные' else 'sa'
        mon.setdefault('%s|%s' % (k, adj_key), {})[d[:7]] = round(v, 2)
    # отдельный вопрос «средний ожидаемый темп прироста цен», %
    exp = {}
    for d, v in cur.execute(
            "SELECT date, value FROM cbr_monitoring_construction "
            "WHERE adjustment='Исходные данные' AND question LIKE '%Средний ожидаемый%'"):
        if v is not None:
            exp[d[:7]] = round(v, 2)
    if exp:
        mon['price_inflation_exp|raw'] = exp
    D['monitoring_legend'] = {
        'ibk': 'ИБК сводный', 'ibk_actual': 'ИБК фактический', 'ibk_expected': 'ИБК ожидания',
        'production': 'Производство (факт)', 'demand': 'Спрос (факт)',
        'prices': 'Цены на продукцию', 'price_expectations': 'Ценовые ожидания 3м',
        'costs': 'Издержки', 'credit_conditions': 'Условия кредитования',
    }
    D['cbr_monitoring'] = mon

# ---------- 5. Эскроу (канон: kvse счетов + osse остаток, сумма по регионам) ----------
esc = defaultdict(dict)
for code, field in (('kvse', 'escrow_accounts_count'), ('osse', 'escrow_balance')):
    for d, v in query(
            """
            SELECT o.period_start, sum(o.value) FROM data.observation o
            JOIN catalog.metric m ON m.metric_id = o.metric_id
            WHERE m.metric_code = %s GROUP BY 1 ORDER BY 1
            """, (code,)):
        esc[d.strftime('%Y-%m')][field] = _num(v)
D['escrow'] = {
    'name': 'Эскроу-счета', 'unit': 'млн руб / шт',
    'source': 'ЦБ РФ (канон: kvse + osse)',
    'monthly': {k: v for k, v in sorted(esc.items())},
}

# ---------- 6. Зарплата (канон: snz, РФ) ----------
wage = monthly_rf('snz')
D['wage'] = {
    'name': 'Номинальная зарплата (все отрасли)', 'unit': 'руб/мес',
    'source': 'Росстат (канон: snz)',
    'monthly': {key(ym): round(wage[ym], 0) for ym in sorted(wage)},
}

out_path = OUT / 'operational_dashboard.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(D, f, ensure_ascii=False)

print('Экспортировано %d КБ' % (out_path.stat().st_size // 1024))
for k, v in D.items():
    if isinstance(v, dict) and 'monthly' in v:
        months = sorted(v['monthly'].keys())
        if months:
            print('  %s: %d мес (%s → %s)' % (k, len(months), months[0], months[-1]))
