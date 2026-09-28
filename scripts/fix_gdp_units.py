#!/usr/bin/env python3
"""Проставить единицы и описания метрикам ВВП (vvp, vvpi) и выровнять названия.

Состояние до правки: у vvp и vvpi unit_id = unknown, описание пустое. Фактический смысл:
  * vvp     — ВВП в постоянных ценах (файл Росстата GDP-quarters-of-use, элементы использования),
              значения ~36,5 трлн за квартал; ряд почти плоский год к году;
  * kep1_12 — ВВП номинальный (КЭП Росстата, лист 1.1), 47 950 → 62 354 млрд руб. за 2025 год;
  * vvpi    — ИФО ВВП, % к соответствующему кварталу предыдущего года (99,8 в I кв 2026).

Отношение kep1_12/vvp растёт с 1,24 (2024-Q1) до 1,70 (2025-Q4) — это накопленный дефлятор,
что подтверждает: vvp в постоянных ценах базового года, а не номинал.

Запуск: python3 scripts/fix_gdp_units.py [--apply]
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import db_tunnel  # noqa: E402

UPDATES = [
    # (metric_code, new_name_ru, unit_code, description)
    ('vvp', 'ВВП в постоянных ценах (элементы использования), млрд руб.', 'bln_rub',
     'Валовой внутренний продукт в постоянных ценах базового года, квартальная оценка '
     'по элементам использования. Источник: Росстат, GDP-quarters-of-use-1995_1kv-2026.xls. '
     'ВНИМАНИЕ: не номинальный объём; номинальные квартальные уровни — в ряду kep1_12 (КЭП). '
     'Отношение kep1_12/vvp = накопленный дефлятор (1,24 в 2024-Q1 → 1,70 в 2025-Q4).'),
    ('vvpi', 'ИФО ВВП, % к соответствующему кварталу предыдущего года', 'pct',
     'Индекс физического объёма ВВП по элементам использования. Источник: Росстат, '
     'GDP-quarters-of-use-1995_1kv-2026.xls. Сверено с релизом: I кв 2026 = 99,8 '
     '(первое отрицательное значение в ряду); ВНОК 87,5; потребление 103,0.'),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='реально применить (по умолчанию dry-run)')
    args = ap.parse_args()

    db_tunnel.connect()
    for code, name, ucode, descr in UPDATES:
        row = db_tunnel.query('SELECT unit_id FROM core.unit WHERE unit_code=%s', (ucode,))
        if not row:
            print(f'нет unit_code={ucode} — пропуск')
            continue
        uid = row[0][0]
        if args.apply:
            db_tunnel.execute("""UPDATE core.metric SET name_ru=%s, unit_id=%s, description=%s
                WHERE metric_code=%s""", (name, uid, descr, code))
            print(f'{code}: unit → {ucode}, имя обновлено')
        else:
            cur = db_tunnel.query("""SELECT left(m.name_ru,50), u.unit_code FROM core.metric m
                LEFT JOIN core.unit u ON u.unit_id=m.unit_id WHERE m.metric_code=%s""", (code,))
            print(f'[dry-run] {code}: сейчас {cur[0] if cur else "?"} → станет unit={ucode}')
    print()
    print('итог по карточкам:')
    for r in db_tunnel.query("""SELECT metric_code, left(name_ru,50), u.unit_code FROM core.metric m
        LEFT JOIN core.unit u ON u.unit_id=m.unit_id WHERE metric_code IN ('vvp','vvpi')"""):
        print('  ', r)


if __name__ == '__main__':
    main()