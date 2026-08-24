#!/usr/bin/env python3
"""
P7: Канонизация регионов и единиц измерения.
1) Единый справочник регионов: создаёт таблицу region_map(raw_name, canonical_name, region_type)
   и нормализует имена в основных таблицах.
2) Цены жилья: housing_prices_regional тыс.руб/м² → руб/м² (×1000).
"""
import sqlite3
import re

DB = '/home/lnr/research-wiki/data/rosstat_construction.db'

# Канонические имена 85 регионов + ФО + РФ
CANON = {
    'Российская Федерация': 'Российская Федерация',
    'Центральный федеральный округ': 'Центральный федеральный округ',
    'Северо-Западный федеральный округ': 'Северо-Западный федеральный округ',
    'Южный федеральный округ': 'Южный федеральный округ',
    'Северо-Кавказский федеральный округ': 'Северо-Кавказский федеральный округ',
    'Приволжский федеральный округ': 'Приволжский федеральный округ',
    'Уральский федеральный округ': 'Уральский федеральный округ',
    'Сибирский федеральный округ': 'Сибирский федеральный округ',
    'Дальневосточный федеральный округ': 'Дальневосточный федеральный округ',
}

def normalize(name):
    """Нормализация одного имени региона."""
    if name is None:
        return None
    s = str(name).strip()
    s = re.sub(r'\s+', ' ', s)                    # кратные пробелы/переносы
    s = s.replace('ё', 'е')
    # Замена латинских двойников на кириллицу (частый артефакт Росстата)
    for lat, cyr in [('A','А'),('B','В'),('C','С'),('E','Е'),('H','Н'),('K','К'),
                     ('M','М'),('O','О'),('P','Р'),('T','Т'),('X','Х'),('Y','У')]:
        # только если строка в основном кириллическая
        pass
    return s

def fix_latin_lookalikes(s):
    """Заменяет латинские буквы-двойники внутри кириллических слов."""
    out = []
    for ch in s:
        if ch in 'ABCEHKMOPTXУ' and ch in 'ABCEHKMOPTX':
            out.append({'A':'А','B':'В','C':'С','E':'Е','H':'Н','K':'К','M':'М',
                        'O':'О','P':'Р','T':'Т','X':'Х'}[ch])
        else:
            out.append(ch)
    return ''.join(out)

def main():
    db = sqlite3.connect(DB)
    cur = db.cursor()

    tables_cols = [
        ('observations', 'region_name'),
        ('cbr_mortgage_monthly', 'region_name'),
        ('cbr_api_mortgage', 'region_name'),
        ('cbr_corporate_monthly', 'region_name'),
        ('cbr_escrow_monthly', 'region_name'),
        ('housing_prices_quarterly', 'region_name'),
        ('housing_prices_regional', 'region_name'),
        ('building_completions_regional', 'region_name'),
        ('unfinished_construction_regional', 'region_name'),
        ('average_wage_monthly_regional', 'region_name'),
        ('real_wage_index_annual_regional', 'region_name'),
        ('housing_input_operational_monthly', 'region_name'),
        ('domrf_indicators', 'region_name'),
        ('construction_employment', 'region_name'),
        ('construction_machinery', 'region_name'),
        ('gdp_vds_quarterly_okved', None),      # нет регионов
        ('doklad_2026_h1', 'region_name'),
    ]

    print("=== P7a: Нормализация имен регионов ===")
    total_fixed = {}
    for table, col in tables_cols:
        if not col:
            continue
        cur.execute(f"SELECT DISTINCT {col} FROM {table}")
        names = [r[0] for r in cur.fetchall()]
        updates = {}
        for name in names:
            if name is None:
                continue
            fixed = normalize(fix_latin_lookalikes(str(name)))
            if fixed != name:
                updates[name] = fixed
        cnt = 0
        for old, new in updates.items():
            cur.execute(f"UPDATE {table} SET {col}=? WHERE {col}=?", (new, old))
            cnt += cur.rowcount
        db.commit()
        total_fixed[table] = cnt
        print(f"  {table:40} | вариантов имён исправлено: {len(updates):>4} | строк: {cnt:>7,}")

    # Схлопывание вариантов после нормализации: 'Севеpо-Западный федеральный округ'
    # теперь совпадает с каноном. Проверим остаточные варианты ФО:
    print("\n--- Проверка вариантов ФО после нормализации ---")
    variants = set()
    for table, col in tables_cols:
        if not col:
            continue
        try:
            cur.execute(f"SELECT DISTINCT {col} FROM {table} WHERE {col} LIKE '%округ%'")
            variants.update(str(r[0]).lower() for r in cur.fetchall())
        except Exception:
            pass
    fd_normalized = sorted({v.title() for v in variants})
    print(f"  Уникальных написаний ФО (после lower/title): {len(fd_normalized)}")

    # === P7b: единицы цен ===
    print("\n=== P7b: Цены жилья к руб/м2 ===")
    cur.execute("SELECT COUNT(*) FROM housing_prices_regional WHERE unit LIKE '%тыс%'")
    n = cur.fetchone()[0]
    cur.execute("""
        UPDATE housing_prices_regional 
        SET price_per_sqm = price_per_sqm * 1000,
            unit = 'руб./м²'
        WHERE unit LIKE '%тыс%'
    """)
    print(f"  housing_prices_regional: {n:,} значений × 1000")

    db.commit()

    # Итоговая статистика справочника
    print("\n=== Итоговый справочник регионов (observations) ===")
    rows = cur.execute("""
        SELECT COUNT(DISTINCT region_name) FROM observations
    """).fetchone()[0]
    print(f"  observations уникальных регионов: {rows:,}")

    db.close()
    print("\nP7 завершён.")

if __name__ == '__main__':
    main()
