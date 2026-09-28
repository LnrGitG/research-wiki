#!/usr/bin/env python3
"""Проставить единицы измерения продуктовым рядам Росстата (Промпродукция).

Проблема: в staging у продуктовых строк есть текстовая колонка `unit` («Тысяча тонн»,
«Тысяча кубических метров»), но рубеж 6 не переносит её в core.metric — у метрик стоит
заглушка `unknown`, и по коду не понять, тонны это или кубометры.

Скрипт читает единицы из локальной SQLite (prom_products_monthly.unit), сопоставляет их
с core.unit (создавая отсутствующие коды) и обновляет core.metric.unit_id у метрик,
чьё название содержит продукт.

Запуск: python3 scripts/fix_prom_product_units.py [--dry-run]
"""
import argparse
import os
import re
import sqlite3
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, 'scripts'))
import db_tunnel  # noqa: E402
from yc_sync import ensure_db  # noqa: E402

# Текст Росстата -> (код единицы, русское название)
UNIT_MAP = {
    'тысяча тонн': ('ths_tonnes', 'тыс. тонн'),
    'тонн': ('tonnes', 'тонн'),
    'тысяча кубических метров': ('ths_m3', 'тыс. м³'),
    'кубических метров': ('m3', 'м³'),
    'тысяча квадратных метров общей площади': ('ths_sqm', 'тыс. м²'),
    'квадратных метров': ('sqm', 'м²'),
    'тысяча квадратных метров': ('ths_sqm', 'тыс. м²'),
    'миллион условных кирпичей': ('mln_conv_bricks', 'млн усл. кирпичей'),
    'штука': ('units', 'ед.'),
    'тысяча штук': ('ths_units', 'тыс. ед.'),
    'тысяч штук': ('ths_units', 'тыс. ед.'),
    'тысяча рублей': ('ths_rub', 'тыс. руб.'),
    'миллион рублей': ('mln_rub', 'млн руб.'),
    'тысяча гектаров': ('ths_hectares', 'тыс. га'),
    'тысяча метров': ('ths_m', 'тыс. м'),
    'гектолитр': ('hectolitres', 'гл'),
    'миллион кубических метров': ('mln_m3', 'млн м³'),
    'тысяча пар': ('ths_pairs', 'тыс. пар'),
    'тысяча литров': ('ths_litres', 'тыс. л'),
}


TRANS = str.maketrans({
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's',
    'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '',
    'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya', ' ': '_', '-': '_', ';': '_', '(': '',
    ')': '', ',': '', '.': '', '^': '', '/': '_',
})


def slug_unit(text):
    """Код единицы для редких единиц Росстата: транслит + обрезка."""
    s = text.lower().translate(TRANS)
    s = ''.join(ch for ch in s if ch.isalnum() or ch == '_')
    s = re.sub(r'_+', '_', s).strip('_')[:40]
    return 'rosstat_' + s


def resolve_unit(text, existing):
    """Текст единицы -> (unit_code, name_ru). Приоритет — ручная таблица, иначе транслит."""
    key = UNIT_MAP.get(text.lower())
    if key:
        return key
    if not text or text == '—':
        return None
    return (slug_unit(text), text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    con = sqlite3.connect(str(ensure_db('rosstat_construction.db')))
    prod_unit = {}
    for product, unit in con.execute("SELECT DISTINCT product, unit FROM prom_products_monthly WHERE unit IS NOT NULL"):
        prod_unit[product] = (unit or '').strip()
    con.close()
    print('продуктов с известной единицей:', len(prod_unit))

    db_tunnel.connect()
    existing = {r[0]: (r[1], r[2]) for r in db_tunnel.query("SELECT unit_code, unit_id, name_ru FROM core.unit")}

    # все единицы из файла -> коды (создаём отсутствующие)
    text2code = {}
    for text in set(prod_unit.values()):
        res = resolve_unit(text, existing)
        if not res:
            continue
        ucode, uru = res
        text2code[text] = ucode
        if ucode not in existing:
            if args.dry_run:
                print(f'  создать единицу {ucode} ({uru})')
            else:
                db_tunnel.execute("INSERT INTO core.unit (unit_code, name_ru, description) VALUES (%s,%s,%s)",
                                  (ucode, uru, f'Росстат, бюллетень продукции: «{text}»'))
            existing[ucode] = (None, uru)

    conn = db_tunnel.connect()
    n_upd, n_skip = 0, 0
    with conn.cursor() as cur:
        cur.execute("SELECT unit_code, unit_id FROM core.unit")
        unit_ids = dict(cur.fetchall())
        cur.execute("""SELECT metric_id, metric_code, name_ru FROM core.metric
                       WHERE name_ru LIKE 'Промпродукция%'""")
        metrics = cur.fetchall()
        pairs, skipped = [], []
        for mid, mcode, name in metrics:
            prod = name.split(':', 1)[1].strip() if ':' in name else ''
            text = prod_unit.get(prod)
            ucode = text2code.get(text) if text else None
            if not ucode or ucode not in unit_ids:
                skipped.append(name)
                continue
            pairs.append((name, unit_ids[ucode]))
        n_upd, n_skip = len(pairs), len(skipped)
        if not args.dry_run and pairs:
            # один батч вместо 12 тысяч отдельных UPDATE: VALUES-список и соединение по имени
            values = ', '.join('(%s,%s)' for _ in pairs)
            params = [x for p in pairs for x in p]
            cur.execute(f"""UPDATE core.metric m SET unit_id = v.uid
                            FROM (VALUES {values}) AS v(nm, uid)
                            WHERE m.name_ru = v.nm""", params)
            conn.commit()
    print(f'метрик с проставленной единицей: {n_upd}, без сопоставления: {n_skip}')
    print('единиц в справочнике:', db_tunnel.query('SELECT count(*) FROM core.unit'))
    if not args.dry_run:
        print('примеры:')
        for r in db_tunnel.query("""
            SELECT left(m.name_ru,58), u.name_ru FROM core.metric m JOIN core.unit u USING (unit_id)
            WHERE m.name_ru LIKE 'Промпродукция%' ORDER BY m.metric_code LIMIT 8"""):
            print('  ', r)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())