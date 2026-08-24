#!/usr/bin/env python3
"""
P6: Пересоздание индексов + VACUUM rosstat_construction.db.
Старые idx_domrf_* (region/file/indicator/date) заменяются на composite-индексы
под типовые запросы моделирования.
"""
import sqlite3
import os
import time

DB = '/home/lnr/research-wiki/data/rosstat_construction.db'

def main():
    size_before = os.path.getsize(DB)
    db = sqlite3.connect(DB)
    cur = db.cursor()

    print("=== Удаление старых индексов ===")
    for idx in ['idx_domrf_region', 'idx_domrf_file', 'idx_domrf_indicator', 'idx_domrf_date']:
        try:
            cur.execute(f"DROP INDEX IF EXISTS {idx}")
            print(f"  {idx} — удалён")
        except Exception as e:
            print(f"  {idx}: {e}")

    # Удаляем осиротевшие индексы observations (таблица поредела)
    for idx in ['idx_obs_region']:
        try:
            cur.execute(f"DROP INDEX IF EXISTS {idx}")
            print(f"  {idx} — удалён")
        except Exception as e:
            print(f"  {idx}: {e}")

    db.commit()

    print("\n=== Создание composite-индексов ===")
    indexes = [
        # ДОМ.РФ: выборка ряда по региону+типу+дате; по коду показателя; сканирование по файлу
        ("idx_domrf_query", "domrf_indicators(region_name, data_type, date)"),
        ("idx_domrf_code",  "domrf_indicators(indicator_code, region_name, date)"),
        ("idx_domrf_file",  "domrf_indicators(file_name)"),
        # ЦБ ипотека: ряд по индикатору/региону/дате
        ("idx_cbr_mort_query", "cbr_mortgage_monthly(indicator, region_name, report_date)"),
        # API таблица
        ("idx_cbr_api_query", "cbr_api_mortgage(indicator_id, region_name, date)"),
        # observations: ряд по индикатору/региону/периоду
        ("idx_obs_query", "observations(indicator_id, region_name, period)"),
    ]
    for name, defn in indexes:
        t0 = time.time()
        cur.execute(f"CREATE INDEX IF NOT EXISTS {name} ON {defn}")
        print(f"  {name} — создан ({time.time()-t0:.1f}s)")

    db.commit()
    db.close()

    print("\n=== VACUUM (может занять несколько минут) ===")
    t0 = time.time()
    db = sqlite3.connect(DB)
    db.execute("PRAGMA journal_mode=DELETE")   # WAL не нужен, файл один
    db.execute("VACUUM")
    db.execute("ANALYZE")
    db.close()
    print(f"  VACUUM+ANALYZE завершён за {time.time()-t0:.1f}s")

    size_after = os.path.getsize(DB)
    print(f"\nРазмер: {size_before/1024/1024:.0f} МБ → {size_after/1024/1024:.0f} МБ "
          f"(-{(size_before-size_after)/1024/1024:.0f} МБ, -{100*(1-size_after/size_before):.0f}%)")

if __name__ == '__main__':
    main()
