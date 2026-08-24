#!/usr/bin/env python3
"""
Очистка rosstat_construction.db от дубликатов и маргинальных данных.
План: queries/db-cleanup-plan.md
Фазы P1-P5 выполняются этим скриптом, VACUUM (P6) — отдельно.
"""
import sqlite3
import os
import sys
import json
from datetime import datetime

DB = '/home/lnr/research-wiki/data/rosstat_construction.db'
ARCHIVE_DIR = '/home/lnr/research-wiki/data/archive'

def get_count(cur, sql, params=()):
    return cur.execute(sql, params).fetchone()[0]

def main():
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    db = sqlite3.connect(DB)
    cur = db.cursor()
    report = {'started': datetime.now().isoformat(), 'phases': {}}

    before_total = get_count(cur, "SELECT COUNT(*) FROM domrf_indicators")
    print(f"domrf_indicators до очистки: {before_total:,}")

    # ============ P1: маргинальные блоки ДОМ.РФ → архив + удаление ============
    print("\n=== P1: Маргинальные блоки ДОМ.РФ ===")
    marginal_types = ['ddu_nonres', 'ddu_nonres_area', 'ddu_nonres_price',
                      'ddu_parking', 'ddu_parking_area', 'ddu_parking_price',
                      'stock_krt']
    p1_deleted = 0
    for dt in marginal_types:
        cnt = get_count(cur, "SELECT COUNT(*) FROM domrf_indicators WHERE data_type=?", (dt,))
        if cnt:
            # Архивируем в JSONL по data_type
            arch_path = os.path.join(ARCHIVE_DIR, f'domrf_{dt}_archived.jsonl')
            with open(arch_path, 'w', encoding='utf-8') as f:
                for row in cur.execute(
                    "SELECT id, file_name, sheet_name, indicator_code, indicator_name, "
                    "region_name, date, value, unit, data_type FROM domrf_indicators WHERE data_type=?",
                    (dt,)
                ):
                # write compact json per line
                    rec = dict(zip(['id','file','sheet','code','name','region','date','value','unit','type'], row))
                    f.write(json.dumps(rec, ensure_ascii=False) + '\n')
            cur.execute("DELETE FROM domrf_indicators WHERE data_type=?", (dt,))
            p1_deleted += cnt
            print(f"  {dt:22} | {cnt:>8,} строк → архив")
    report['phases']['P1'] = {'deleted': p1_deleted}
    db.commit()

    # ============ P2: точные дубликаты ДОМ.РФ ============
    print("\n=== P2: Точные дубликаты ДОМ.РФ ===")
    # Дубликат: одинаковый (file,sheet,code,region,date,type,value), оставляем min(id)
    dup_groups = cur.execute("""
        SELECT COUNT(*) FROM (
          SELECT 1 FROM domrf_indicators
          GROUP BY file_name, sheet_name, indicator_code, region_name, date, data_type, value
          HAVING COUNT(*) > 1
        )
    """).fetchone()[0]
    cur.execute("""
        DELETE FROM domrf_indicators WHERE id NOT IN (
          SELECT MIN(id) FROM domrf_indicators
          GROUP BY file_name, sheet_name, indicator_code, region_name, date, data_type, value
        )
    """)
    p2_deleted = cur.rowcount if cur.rowcount and cur.rowcount > 0 else 0
    print(f"  Групп-дубликатов: {dup_groups:,}, удалено строк: {p2_deleted:,}")
    report['phases']['P2'] = {'dup_groups': dup_groups, 'deleted': p2_deleted}
    db.commit()

    # ============ P3: мусорные «регионы» ДОМ.РФ ============
    print("\n=== P3: Мусорные регионы ДОМ.РФ ===")
    p3_deleted = cur.execute("""
        DELETE FROM domrf_indicators 
        WHERE region_name GLOB '[0-9]*' AND length(region_name) <= 4
    """).rowcount
    print(f"  Удалено: {p3_deleted:,}")
    report['phases']['P3'] = {'deleted': p3_deleted or 0}
    db.commit()

    # ============ P4: cumulative-снимки observations ============
    print("\n=== P4: Cumulative-снимки observations ===")
    p4_deleted = cur.execute(
        "DELETE FROM observations WHERE period_type='cumulative'"
    ).rowcount
    print(f"  Удалено: {p4_deleted:,}")
    report['phases']['P4'] = {'deleted': p4_deleted or 0}

    # Чистим осиротевшие индикаторы (без наблюдений)
    orphaned = cur.execute("""
        SELECT id, indicator_name FROM indicators 
        WHERE id NOT IN (SELECT DISTINCT indicator_id FROM observations)
    """).fetchall()
    for iid, name in orphaned:
        print(f"    Осиротевший индикатор [{iid}]: {str(name)[:60]}")
    cur.execute("DELETE FROM indicators WHERE id NOT IN (SELECT DISTINCT indicator_id FROM observations)")
    report['phases']['P4']['orphaned_indicators_removed'] = len(orphaned)
    db.commit()

    # ============ P5: нулевые fx-строки ЦБ ============
    print("\n=== P5: Нулевые fx-строки ЦБ ===")
    p5_mortgage = cur.execute(
        "DELETE FROM cbr_mortgage_monthly WHERE indicator LIKE '%_fx' AND value = 0"
    ).rowcount
    p5_corporate = cur.execute(
        "DELETE FROM cbr_corporate_monthly WHERE currency='FX' AND value = 0"
    ).rowcount
    print(f"  mortgage: {p5_mortgage:,}, corporate: {p5_corporate:,}")
    report['phases']['P5'] = {'mortgage_fx_zero': p5_mortgage or 0, 'corporate_fx_zero': p5_corporate or 0}
    db.commit()

    after_total = get_count(cur, "SELECT COUNT(*) FROM domrf_indicators")
    print(f"\ndomrf_indicators после очистки: {after_total:,}")
    total_deleted = sum(p.get('deleted', 0) for k, p in report['phases'].items() if isinstance(p.get('deleted'), int))
    print(f"Всего удалено строк: ~{total_deleted:,}")

    report['finished'] = datetime.now().isoformat()
    report['total_deleted'] = total_deleted
    with open(os.path.join(ARCHIVE_DIR, 'cleanup_report.json'), 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    db.close()
    print(f"\nОтчёт: {ARCHIVE_DIR}/cleanup_report.json")

if __name__ == '__main__':
    main()
