"""[ОТКЛЮЧЁН 16.10.2026] Лендинг cbr_lending.db снят из контура (пункт 1 аудита):
данные ЦБ пишутся в канон напрямую — cbr_banking_canon.py / cbr_monitoring_canon.py.
Скрипт оставлен как справочная реализация парсера сырья raw/cbr/ (восстановление
лендинга из сырья при необходимости: raw/cbr/{bulletin,escrow,deposits,api})."""
#!/usr/bin/env python3
"""
Update CBR banking sector statistics: mortgage lending, project financing
with escrow, and corporate lending by region.
Optimized version using iter_rows for fast bulk reads.
"""

try:
    from xlsx_engine import open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import open_workbook  # noqa: E402

import os
import re
import sqlite3
import datetime

try:
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
except ImportError:  # запуск из другого каталога
    import os as _os
    import sys as _sys
    _sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
    from xlsx_engine import engine_from_argv, open_workbook  # noqa: E402
ENGINE = engine_from_argv()  # --xlsx-engine openpyxl|fastexcel, резерв — XLSX_ENGINE


BASE = "/home/lnr/research-wiki-private"
VFS_DIR = os.path.join(BASE, "raw/cbr/vfs")
BULLETIN_DIR = os.path.join(BASE, "raw/cbr/bulletin")
ESCROW_DIR = os.path.join(BASE, "raw/cbr/escrow")
DB_PATH = os.path.join(BASE, "data/cbr_lending.db")

MONTH_MAP = {
    "Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6,
    "Июль": 7, "Август": 8, "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12,
}

def parse_month_header(val):
    if val is None:
        return None
    if isinstance(val, datetime.datetime):
        return (val.year, val.month)
    s = str(val).strip()
    m = re.match(r"(\S+)\s+(\d{4})", s)
    if m and m.group(1) in MONTH_MAP:
        return (int(m.group(2)), MONTH_MAP[m.group(1)])
    return None

def rdate_str(year, month):
    return f"{year}-{month:02d}-01"

def is_fo(name):
    if name is None:
        return True
    s = str(name).upper().strip()
    return "ФЕДЕРАЛЬНЫЙ ОКРУГ" in s or s.endswith("ФО") or " ФО " in s

def init_db(db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    for table in ["mortgage_monthly", "escrow_monthly", "corporate_monthly"]:
        c.execute(f"""CREATE TABLE IF NOT EXISTS {table} (
            region_name TEXT NOT NULL, report_date TEXT NOT NULL,
            indicator TEXT NOT NULL, value REAL, unit TEXT, source TEXT,
            PRIMARY KEY (region_name, report_date, indicator, source))""")
        # Add source column if missing (migration for existing tables)
        cols = [col[1] for col in c.execute(f"PRAGMA table_info({table})").fetchall()]
        if "source" not in cols:
            c.execute(f"ALTER TABLE {table} ADD COLUMN source TEXT")
            # Recreate PK with source — need to recreate table
            c.execute(f"CREATE TABLE IF NOT EXISTS {table}_new AS SELECT region_name, report_date, indicator, value, unit, source FROM {table}")
            c.execute(f"DROP TABLE {table}")
            c.execute(f"""CREATE TABLE {table} (
                region_name TEXT NOT NULL, report_date TEXT NOT NULL,
                indicator TEXT NOT NULL, value REAL, unit TEXT, source TEXT,
                PRIMARY KEY (region_name, report_date, indicator, source))""")
            c.execute(f"INSERT OR REPLACE INTO {table} SELECT region_name, report_date, indicator, value, unit, source FROM {table}_new")
            c.execute(f"DROP TABLE {table}_new")
    conn.commit()
    return conn

# ─── VFS files ──────────────────────────────────────────────────────────
VFS_FILES = {
    "01_04_D_New_loans_subj.xlsx": {
        "table": "corporate_monthly",
        "indicators": {
            "итого": "Корпоративные кредиты — новые выдачи (итого)",
            "в рублях": "Корпоративные кредиты — новые выдачи (в рублях)",
            "в инвалюте": "Корпоративные кредиты — новые выдачи (в инвалюте)",
        },
        "unit": "млн руб", "source": "VFS 01_04_D_New_loans_subj",
    },
    "01_05_D_Debt_subj.xlsx": {
        "table": "corporate_monthly",
        "indicators": {
            "итого": "Корпоративные кредиты — задолженность (итого)",
            "в т.ч. просроч. итого": "Корпоративные кредиты — задолженность (просроченная, итого)",
            "в рублях": "Корпоративные кредиты — задолженность (в рублях)",
            "в т.ч. просроч. в рублях": "Корпоративные кредиты — задолженность (просроченная, в рублях)",
            "в инвалюте": "Корпоративные кредиты — задолженность (в инвалюте)",
            "в т.ч. просроч. в инвалюте": "Корпоративные кредиты — задолженность (просроченная, в инвалюте)",
        },
        "unit": "млн руб", "source": "VFS 01_05_D_Debt_subj",
    },
    "02_04_New_loans_ind.xlsx": {
        "table": "mortgage_monthly",
        "indicators": {
            "итого": "Ипотека физлицам — новые выдачи (итого)",
            "в рублях": "Ипотека физлицам — новые выдачи (в рублях)",
            "в инвалюте": "Ипотека физлицам — новые выдачи (в инвалюте)",
        },
        "unit": "млн руб", "source": "VFS 02_04_New_loans_ind",
    },
    "02_05_Debt_ind.xlsx": {
        "table": "mortgage_monthly",
        "indicators": {
            "итого": "Ипотека физлицам — задолженность (итого)",
            "в т.ч. просроч.": "Ипотека физлицам — задолженность (просроченная, итого)",
            "в рублях": "Ипотека физлицам — задолженность (в рублях)",
            "в т.ч. просроч. в рублях": "Ипотека физлицам — задолженность (просроченная, в рублях)",
            "в инвалюте": "Ипотека физлицам — задолженность (в инвалюте)",
            "в т.ч. просроч. в инвалюте": "Ипотека физлицам — задолженность (просроченная, в инвалюте)",
        },
        "unit": "млн руб", "source": "VFS 02_05_Debt_ind",
    },
}

def parse_vfs_file(conn, path, config):
    table = config["table"]
    source = config["source"]
    unit = config["unit"]
    indicators = config["indicators"]
    
    wb = open_workbook(path, engine=ENGINE)
    inserted = 0
    
    for sheet_name in wb.sheetnames:
        if sheet_name not in indicators:
            continue
        indicator_name = indicators[sheet_name]
        ws = wb[sheet_name]
        
        # Read all rows at once using iter_rows
        all_rows = list(ws.iter_rows(min_row=1, values_only=True))
        
        # Find header row: first row where col0=None, col1 not None
        header_row_idx = None
        for i, row in enumerate(all_rows[:10]):
            if row[0] is None and len(row) > 1 and row[1] is not None:
                header_row_idx = i
                break
        
        if header_row_idx is None:
            continue
        
        # Parse months from header row
        header = all_rows[header_row_idx]
        months = []
        for ci in range(1, len(header)):
            parsed = parse_month_header(header[ci])
            months.append(parsed)
        
        # Data rows after header
        rows = []
        for row in all_rows[header_row_idx + 1:]:
            if row[0] is None:
                break
            name = str(row[0]).strip()
            if is_fo(name) and "РОССИЙСКАЯ" not in name.upper():
                continue
            for ci, parsed in enumerate(months):
                if parsed is None:
                    continue
                if ci + 1 >= len(row):
                    break
                val = row[ci + 1]
                if val is not None and isinstance(val, (int, float)):
                    rows.append((name, rdate_str(*parsed), indicator_name, float(val), unit, source))
        
        c = conn.cursor()
        c.executemany(
            f"INSERT OR REPLACE INTO {table} (region_name, report_date, indicator, value, unit, source) VALUES (?,?,?,?,?,?)",
            rows)
        conn.commit()
        inserted += len(rows)
        fm = months[0] if months and months[0] else "?"
        lm = months[-1] if months and months[-1] else "?"
        print(f"  {sheet_name}: {len(rows)} rows, {fm}–{lm}", flush=True)
    
    wb.close()
    return inserted

# ─── Bulletin ───────────────────────────────────────────────────────────
BULLETIN_SHEETS = {
    "Т_16": ("izhk_count", "шт"),
    "Т_17": ("izhk_ddu_count", "шт"),
    "Т_18": ("izhk_ijs_count", "шт"),
    "T_19": ("izhk_volume", "млн руб"),
    "T_20": ("izhk_ddu_volume", "млн руб"),
    "T_21": ("izhk_ijs_volume", "млн руб"),
    "T_22": ("izhk_debt", "млн руб"),
    "T_23": ("izhk_ddu_debt", "млн руб"),
    "T_24": ("izhk_overdue", "млн руб"),
    "T_25": ("izhk_ddu_overdue", "млн руб"),
    "T_26": ("izhk_rate", "%"),
    "T_27": ("izhk_ddu_rate", "%"),
    "T_28": ("izhk_nonddu_rate", "%"),
    "T_29": ("izhk_ijs_rate", "%"),
    "T_30": ("izhk_share_loans", "%"),
    "T_31": ("izhk_share_debt", "%"),
    "T_32": ("izhk_avg_size", "млн руб"),
    "T_33": ("izhk_ddu_avg_size", "млн руб"),
}

def parse_bulletin(conn, path):
    wb = open_workbook(path, engine=ENGINE)
    source = f"Bulletin {os.path.basename(path)}"
    inserted = 0
    
    for sheet_name, (indicator, unit) in BULLETIN_SHEETS.items():
        if sheet_name not in wb.sheetnames:
            continue
        ws = wb[sheet_name]
        all_rows = list(ws.iter_rows(min_row=1, values_only=True))
        
        # Row 4 (index 3) = month headers, row 5+ = data
        if len(all_rows) < 5:
            continue
        header = all_rows[3]  # row 4
        months = []
        for ci in range(1, len(header)):
            parsed = parse_month_header(header[ci])
            months.append(parsed)
        
        if not months or all(m is None for m in months):
            continue
        
        rows = []
        for row in all_rows[4:]:  # row 5+
            if row[0] is None:
                continue
            name = str(row[0]).strip()
            if is_fo(name) and "РОССИЙСКАЯ" not in name.upper():
                continue
            for ci, parsed in enumerate(months):
                if parsed is None:
                    continue
                if ci + 1 >= len(row):
                    break
                val = row[ci + 1]
                if val is not None and isinstance(val, (int, float)):
                    rows.append((name, rdate_str(*parsed), indicator, float(val), unit, source))
        
        c = conn.cursor()
        c.executemany(
            "INSERT OR REPLACE INTO mortgage_monthly (region_name, report_date, indicator, value, unit, source) VALUES (?,?,?,?,?,?)",
            rows)
        conn.commit()
        inserted += len(rows)
        fm = months[0] if months and months[0] else "?"
        lm = months[-1] if months and months[-1] else "?"
        print(f"  {sheet_name}: {len(rows)} rows, {fm}–{lm}", flush=True)
    
    # Т_34: quarterly prices
    if "Т_34" in wb.sheetnames:
        ws = wb["Т_34"]
        all_rows = list(ws.iter_rows(min_row=1, values_only=True))
        
        # Row 4 (idx 3): years, Row 5 (idx 4): quarters, Row 6 (idx 5): market type
        col_map = {}
        current_year = None
        current_quarter = None
        qmap = {"I": 1, "II": 2, "III": 3, "IV": 4}
        
        for col in range(1, 20):
            if col < len(all_rows[3]) and all_rows[3][col] is not None:
                m = re.search(r"(\d{4})", str(all_rows[3][col]))
                if m:
                    current_year = int(m.group(1))
            if col < len(all_rows[4]) and all_rows[4][col] is not None:
                qs = str(all_rows[4][col]).strip()
                # Extract Roman numeral: "I квартал" → "I", "II квартал" → "II"
                qm = re.match(r"^(I{1,3}V?|IV)\b", qs)
                if qm:
                    current_quarter = qmap.get(qm.group(1), current_quarter)
            if col < len(all_rows[5]) and all_rows[5][col] is not None and current_year and current_quarter:
                market = "первичный" if "Первич" in str(all_rows[5][col]) else "вторичный"
                col_map[col] = (current_year, current_quarter, market)
        
        rows = []
        for row in all_rows[6:]:
            if row[0] is None:
                continue
            name = str(row[0]).strip()
            if is_fo(name) and "РОССИЙСКАЯ" not in name.upper():
                continue
            for col, (year, quarter, market) in col_map.items():
                if col >= len(row):
                    continue
                val = row[col]
                if val is not None and isinstance(val, (int, float)):
                    qmonth = {1: 3, 2: 6, 3: 9, 4: 12}[quarter]
                    rows.append((name, rdate_str(year, qmonth), f"avg_price_sqm_{market}_рынок", float(val), "руб/кв.м", source))
        
        c = conn.cursor()
        c.executemany(
            "INSERT OR REPLACE INTO mortgage_monthly (region_name, report_date, indicator, value, unit, source) VALUES (?,?,?,?,?,?)",
            rows)
        conn.commit()
        inserted += len(rows)
        print(f"  Т_34: {len(rows)} rows, {len(col_map)} quarter-columns", flush=True)
    
    wb.close()
    return inserted

# ─── Escrow ─────────────────────────────────────────────────────────────
ESCROW_INDICATORS = [
    ("active_contracts_count", "шт"),
    ("active_contracts_sum", "млн руб"),
    ("debt", "млн руб"),
    ("escrow_accounts_with_balance", "шт"),
    ("escrow_balance", "млн руб"),
    ("credit_rate", "%"),
    ("disclosed_escrow_accounts", "шт"),
    ("disclosed_funds", "млн руб"),
]

def parse_escrow_file(conn, path):
    fname = os.path.basename(path)
    m = re.match(r"(\d{2})(\d{2})(\d{4})\.xlsx", fname)
    if not m:
        return 0
    _, month, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
    rdate = rdate_str(year, month)
    source = f"Escrow {fname}"
    
    wb = open_workbook(path, engine=ENGINE)
    ws = wb.active
    all_rows = list(ws.iter_rows(min_row=1, values_only=True))
    wb.close()
    
    # Structure: row 4 (1-based) = headers, row 5+ = data
    # Col 0 = № (or ФО name for ФО rows), col 1 = region name (None for ФО rows)
    # Cols 2-9 = 8 data columns (not 9 — the spec's col 6 "Кол-во счетов эскроу" is
    # actually "Кол-во счетов эскроу, имеющих остатки" in the file)
    rows = []
    for row in all_rows[4:]:  # index 4 = row 5 (1-based)
        if len(row) < 3:
            continue
        # Region name is in col 1 for regular rows, or col 0 for ФО rows
        name = row[1] if row[1] is not None else row[0]
        if name is None:
            continue
        name = str(name).strip()
        if is_fo(name) and "РОССИЙСКАЯ" not in name.upper():
            continue
        # Also skip "Итого по РФ" — will normalize later
        if "Итого по РФ" in name:
            name = "РОССИЙСКАЯ ФЕДЕРАЦИЯ"
        
        for ci, (indicator, unit) in enumerate(ESCROW_INDICATORS):
            col_idx = ci + 2  # data starts at col 2 (0-based)
            if col_idx >= len(row):
                break
            val = row[col_idx]
            if val is not None and isinstance(val, (int, float)):
                rows.append((name, rdate, indicator, float(val), unit, source))
    
    c = conn.cursor()
    c.executemany(
        "INSERT OR REPLACE INTO escrow_monthly (region_name, report_date, indicator, value, unit, source) VALUES (?,?,?,?,?,?)",
        rows)
    conn.commit()
    return len(rows)

# ─── Main ───────────────────────────────────────────────────────────────
def main():
    print("=" * 60, flush=True)
    print("CBR Lending Statistics Update", flush=True)
    print("=" * 60, flush=True)
    
    conn = init_db(DB_PATH)
    
    # 1. VFS
    print("\n-- 1. VFS files --", flush=True)
    total = 0
    for fname, config in VFS_FILES.items():
        path = os.path.join(VFS_DIR, fname)
        if not os.path.exists(path):
            print(f"  MISSING: {fname}", flush=True)
            continue
        print(f"  {fname}:", flush=True)
        n = parse_vfs_file(conn, path, config)
        total += n
    print(f"  VFS total: {total:,} records", flush=True)
    
    # 2. Bulletin
    print("\n-- 2. Mortgage bulletin --", flush=True)
    bulletins = sorted(f for f in os.listdir(BULLETIN_DIR) if f.startswith("mortgage_lending_market_") and f.endswith(".xlsx"))
    total = 0
    for bname in bulletins:
        path = os.path.join(BULLETIN_DIR, bname)
        print(f"  {bname}:", flush=True)
        n = parse_bulletin(conn, path)
        total += n
    # Deduplicate: for overlapping months between bulletins, keep the latest bulletin's data
    c = conn.cursor()
    for i in range(len(bulletins) - 1):
        old_src = f"Bulletin {bulletins[i]}"
        for j in range(i + 1, len(bulletins)):
            new_src = f"Bulletin {bulletins[j]}"
            n = c.execute("""DELETE FROM mortgage_monthly
                WHERE source = ? AND EXISTS (
                    SELECT 1 FROM mortgage_monthly m2
                    WHERE m2.region_name = mortgage_monthly.region_name
                    AND m2.report_date = mortgage_monthly.report_date
                    AND m2.indicator = mortgage_monthly.indicator
                    AND m2.source = ?)""", (old_src, new_src)).rowcount
            if n > 0:
                print(f"  Dedup: removed {n} overlapping records from {bulletins[i]} (kept {bulletins[j]})", flush=True)
    conn.commit()
    print(f"  Bulletin total: {total:,} records (before dedup)", flush=True)
    
    # 3. Escrow
    print("\n-- 3. Escrow files --", flush=True)
    escrow_files = sorted(f for f in os.listdir(ESCROW_DIR) if re.match(r"\d{8}\.xlsx", f))
    total = 0
    for ename in escrow_files:
        path = os.path.join(ESCROW_DIR, ename)
        n = parse_escrow_file(conn, path)
        total += n
    print(f"  Escrow: {len(escrow_files)} files, {total:,} records", flush=True)
    
    # Summary
    print("\n" + "=" * 60, flush=True)
    print("SUMMARY", flush=True)
    print("=" * 60, flush=True)
    c = conn.cursor()
    for table in ["mortgage_monthly", "escrow_monthly", "corporate_monthly"]:
        cnt = c.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        latest = c.execute(f"SELECT MAX(report_date) FROM {table}").fetchone()[0]
        regions = c.execute(f"SELECT COUNT(DISTINCT region_name) FROM {table}").fetchone()[0]
        indicators = c.execute(f"SELECT COUNT(DISTINCT indicator) FROM {table}").fetchone()[0]
        print(f"  {table}: {cnt:,} records, {regions} regions, {indicators} indicators, latest={latest}", flush=True)
    
    print("\n  Top 5 regions by ИЖК volume (latest):", flush=True)
    latest_m = c.execute("SELECT MAX(report_date) FROM mortgage_monthly WHERE indicator='izhk_volume'").fetchone()[0]
    if latest_m:
        top5 = c.execute("""SELECT region_name, value FROM mortgage_monthly
            WHERE indicator='izhk_volume' AND report_date=? AND region_name != 'РОССИЙСКАЯ ФЕДЕРАЦИЯ'
            ORDER BY value DESC LIMIT 5""", (latest_m,)).fetchall()
        for i, (region, vol) in enumerate(top5):
            print(f"    {i+1}. {region}: {vol:,.0f} млн руб", flush=True)
    
    conn.close()
    print("\nDone.", flush=True)

if __name__ == "__main__":
    main()