#!/usr/bin/env python3
"""Проверка загрузки прогнозов роста ВВП РФ (МВФ WEO + Всемирный банк WDI).

Sanity-проверки: регистрация источника/метрики/релиза, контрольные значения,
покрытие лет, природа значений (final/forecast), идемпотентность.

Запуск: ~/.hermes/hermes-agent/venv/bin/python3 scripts/verify_gdp_forecasts.py
Возврат: 0 — все проверки пройдены, 1 — есть расхождения.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_tunnel import query, available

IMF = 'gdp_growth_fc_imf'
WB = 'gdp_growth_fc_wb_wdi'

# Контрольные значения из первоисточников (см. queries/gdp-forecasts-ingest.md)
CONTROLS = [
    (IMF, 2024, 4.9, 'final'),
    (IMF, 2025, 1.0, 'final'),
    (IMF, 2031, 1.0, 'forecast'),
    (WB, 2020, -2.65365449695453, 'final'),
    (WB, 2023, 4.06661395813023, 'final'),
    (WB, 2024, 4.92167966203073, 'final'),
]

problems = []


def check(cond, msg):
    if cond:
        print(f'OK   {msg}')
    else:
        print(f'FAIL {msg}')
        problems.append(msg)


def main():
    if not available(verbose=True):
        print('Нет доступа к БД (тоннель не поднят)')
        return 1

    for code, expected_n in ((IMF, 39), (WB, 36)):
        n = query("SELECT count(*) FROM core.observation_v2 o JOIN core.metric m USING(metric_id) "
                  "WHERE m.metric_code=%s", (code,))[0][0]
        check(n == expected_n, f'{code}: ожидалось {expected_n} наблюдений, в БД {n}')

    # Регистрация источников
    srcs = dict(query("SELECT source_code, source_id FROM core.source WHERE source_code IN ('imf','worldbank')"))
    check(set(srcs) == {'imf', 'worldbank'}, f'источники зарегистрированы: {sorted(srcs)}')

    # Метрики: единица измерения «процент», годовая частота, тип primary
    for code in (IMF, WB):
        row = query("""SELECT u.unit_code, f.frequency_code, m.metric_type, m.status
                       FROM core.metric m JOIN core.unit u USING(unit_id)
                       JOIN core.frequency f USING(frequency_id)
                       WHERE m.metric_code=%s""", (code,))
        check(bool(row) and row[0][0] == 'pct' and row[0][1] == 'A'
              and row[0][2] == 'primary' and row[0][3] == 'active',
              f'{code}: метрика привязана к pct/A, тип primary, активна (факт: {row})')

    # Винтажи: ровно один релиз на источник, сырые значения не задвоены
    for code, src in ((IMF, 'imf'), (WB, 'worldbank')):
        row = query("""SELECT count(DISTINCT o.release_id), count(o.obs_id)
                       FROM core.observation_v2 o JOIN core.metric m USING(metric_id)
                       WHERE m.metric_code=%s""", (code,))
        check(row[0][0] == 1, f'{code}: все наблюдения в одном винтаже (факт: {row[0][0]})')
        rel = query("""SELECT r.release_label, r.status, r.published_at
                       FROM core.release r JOIN core.source s USING(source_id)
                       WHERE s.source_code=%s""", (src,))
        check(bool(rel) and rel[0][1] in ('loaded', 'validated', 'parsed'),
              f'{code}: релиз винтажа существует и не failed ({rel})')

    # Контрольные значения
    for code, year, exp_val, exp_type in CONTROLS:
        row = query("""SELECT o.value, o.assessment_type, o.observation_status
                       FROM core.observation_v2 o JOIN core.metric m USING(metric_id)
                       WHERE m.metric_code=%s AND o.period_start=%s""", (code, f'{year}-01-01'))
        got = row[0][0] if row else None
        ok = row and abs(float(got) - exp_val) < 1e-6 and row[0][1] == exp_type
        check(ok, f'{code} {year}: ожидалось {exp_val} ({exp_type}), в БД {got if row else "нет"} ({row[0][1] if row else "—"})')

    # Периоды: годовые интервалы, конец >= начала
    bad = query("""SELECT count(*) FROM core.observation_v2 o JOIN core.metric m USING(metric_id)
                   WHERE m.metric_code IN (%s,%s) AND (o.period_end < o.period_start
                   OR extract(month from o.period_start) <> 1 OR extract(day from o.period_end) <> 31)""",
                (IMF, WB))[0][0]
    check(bad == 0, f'периоды корректны (годовые, end>=start); нарушений {bad}')

    # Свежая точка Росстата: ИФО ВВП за II квартал 2026, первая оценка 11.09.2026
    ros = query("""SELECT o.value, o.assessment_type, o.observation_status, r.release_label,
                          r.published_at, s.source_code
                   FROM core.observation_v2 o
                   JOIN core.metric m USING(metric_id)
                   JOIN core.source s USING(source_id)
                   JOIN core.release r USING(release_id)
                   WHERE m.metric_code='vvpi' AND o.period_start='2026-04-01'
                     AND r.release_label='rosstat_gdp_2026q2_first_estimate'""")
    check(bool(ros) and abs(float(ros[0][0]) - 101.3) < 1e-6
          and ros[0][1] == 'preliminary' and ros[0][5] == 'rosstat',
          f'Росстат ИФО ВВП 2026Q2 = 101,3 (preliminary): {ros[0] if ros else "нет"}')

    print()
    if problems:
        print(f'ИТОГ: {len(problems)} расхождений')
        return 1
    print('ИТОГ: все проверки пройдены')
    return 0


if __name__ == '__main__':
    sys.exit(main())