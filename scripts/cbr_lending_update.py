#!/usr/bin/env python3
"""
Parse and import CBR banking sector lending statistics into SQLite.

Sources:
  1. VFS cumulative files (corporate + mortgage new loans/debt by region)
  2. Mortgage lending market bulletin (Section II, regional sheets Т_16–Т_34)
  3. Escrow/project financing monthly snapshots (by region)

Target DB: data/cbr_lending.db
Tables: mortgage_monthly, escrow_monthly, corporate_monthly
"""

import openpyxl
import sqlite3
import os
import re
from datetime import datetime, date

# ─── Paths ───────────────────────────────────────────────────────────────
BASE = "/home/lnr/research-wiki-private"
VFS_DIR = os.path.join(BASE, "raw/cbr/vfs")
BULLETIN_DIR = os.path.join(BASE, "raw/cbr/bulletin")
ESCROW_DIR = os.path.join(BASE, "raw/cbr/escrow")
DB_PATH = os.path.join(BASE, "data/cbr_lending.db")

# ─── Month name mapping ─────────────────────────────────────────────────
MONTHS_RU = {
    "Январь": 1, "Февраль": 2, "Март": 3, "Апрель": 4, "Май": 5, "Июнь": 6,
    "Июль": 7, "Август": 8, "Сентябрь": 9, "Октябрь": 10, "Ноябрь": 11, "Декабрь": 12,
}
MONTHS_RU_LOWER = {k.lower(): v for k, v in MONTHS_RU.items()}


def parse_month_header(val):
    """Parse a month header cell — could be 'Январь 2019' or datetime(2019,1,1)."""
    if val is None:
        return None
    if isinstance(val, (datetime, date)):
        return val.strftime("%Y-%m-01")
    s = str(val).strip()
    # Try "Месяц YYYY" format
    for mname, mnum in MONTHS_RU_LOWER.items():
        m = re.match(rf"{mname}\s+(\d{{4}})", s, re.IGNORECASE)
        if m:
            return f"{m.group(1)}-{mnum:02d}-01"
    # Try YYYY-MM or YYYY-MM-DD
    m = re.match(r"(\d{4})-(\d{2})(?:-\d{2})?", s)
    if m:
        return f"{m.group(1)}-{m.group(2)}-01"
    return None


def is_fo_row(name):
    """Check if row is a federal district (ФО) — skip these."""
    if name is None:
        return False
    s = str(name).strip().upper()
    return "ФЕДЕРАЛЬНЫЙ ОКРУГ" in s or s.endswith(" ФО")


def is_rf_row(name):
    """Check if row is Russian Federation aggregate."""
    if name is None:
        return False
    s = str(name).strip().upper()
    return s == "РОССИЙСКАЯ ФЕДЕРАЦИЯ" or s == "РФ"


def is_data_region(name):
    """Check if row is a region (not FO, not РФ, not footnote, not empty)."""
    if name is None:
        return False
    s = str(name).strip()
    if not s:
        return False
    if is_fo_row(s) or is_rf_row(s):
        return False
    # Skip footnotes — they start with digit+space or * or are clearly notes
    if re.match(r"^\d+\s+", s) or s.startswith("*") or s.startswith("ИТОГО"):
        return False
    # Skip rows that are clearly not region names (long text, contain "учитываются" etc.)
    if len(s) > 60 and not any(kw in s for kw in ["область", "край", "Республика", "г.", "автоном", "АО"]):
        return False
    return True


# ═════════════════════════════════════════════════════════════════════════
# VFS FILES PARSER
# ═════════════════════════════════════════════════════════════════════════

def find_header_row(ws, max_check=5):
    """Find the row with month headers by scanning first few rows."""
    for r in range(1, max_check + 1):
        row = list(ws.iter_rows(min_row=r, max_row=r, values_only=True))[0]
        for cell in row[1:]:
            parsed = parse_month_header(cell)
            if parsed:
                return r
    return None


def parse_vfs_file(fpath, file_type):
    """
    Parse a VFS XLSX file.
    
    file_type: 'corporate_new', 'corporate_debt', 'mortgage_new', 'mortgage_debt'
    
    Returns list of (region_name, report_date, indicator, value, unit)
    """
    wb = openpyxl.load_workbook(fpath, read_only=True, data_only=True)
    records = []
    
    # Determine indicator prefixes based on file_type
    if file_type == "corporate_new":
        base_indicator = "Корпоративные кредиты — новые выдачи"
        unit = "млн руб"
        target_sheets = ["итого", "в рублях", "в инвалюте"]
    elif file_type == "corporate_debt":
        base_indicator = "Корпоративные кредиты — задолженность"
        unit = "млн руб"
        target_sheets = ["итого", "в рублях", "в инвалюте",
                         "в т.ч. просроч. итого", "в т.ч. просроч. в рублях", "в т.ч. просроч. в инвалюте"]
    elif file_type == "mortgage_new":
        base_indicator = "Ипотека физлицам — новые выдачи"
        unit = "млн руб"
        target_sheets = ["итого", "в рублях", "в инвалюте"]
    elif file_type == "mortgage_debt":
        base_indicator = "Ипотека физлицам — задолженность"
        unit = "млн руб"
        target_sheets = ["итого", "в рублях", "в инвалюте",
                         "в т.ч. просроч.", "в т.ч. просроч. в рублях", "в т.ч. просроч. в инвалюте"]
    else:
        wb.close()
        return records
    
    for sn in wb.sheetnames:
        if sn not in target_sheets:
            continue
        
        # Build indicator name from sheet
        is_overdue = "просроч" in sn.lower()
        if "в рублях" in sn.lower():
            currency = "в рублях"
        elif "в инвалюте" in sn.lower():
            currency = "в инвалюте"
        else:
            currency = "итого"
        
        if is_overdue:
            indicator = f"{base_indicator} (просроченная, {currency})"
        else:
            indicator = f"{base_indicator} ({currency})"
        
        ws = wb[sn]
        header_row = find_header_row(ws)
        if header_row is None:
            print(f"  WARNING: no header row found in {sn}")
            continue
        
        # Parse month headers
        header = list(ws.iter_rows(min_row=header_row, max_row=header_row, values_only=True))[0]
        months = []
        for cell in header[1:]:
            parsed = parse_month_header(cell)
            if parsed:
                months.append(parsed)
            else:
                months.append(None)
        
        # Data starts from header_row + 1
        for row in ws.iter_rows(min_row=header_row + 1, values_only=True):
            name = row[0]
            if name is None:
                continue
            name = str(name).strip()
            if not name:
                continue
            
            # Keep РФ, skip ФО, skip footnotes
            if not (is_rf_row(name) or is_data_region(name)):
                continue
            
            for i, val in enumerate(row[1:]):
                if i >= len(months) or months[i] is None:
                    continue
                if val is None:
                    continue
                try:
                    num_val = float(val)
                except (ValueError, TypeError):
                    continue
                records.append((name, months[i], indicator, num_val, unit))
    
    wb.close()
    return records


# ═════════════════════════════════════════════════════════════════════════
# BULLETIN PARSER (Section II: Т_16 through Т_34)
# ═════════════════════════════════════════════════════════════════════════

# Sheet metadata: (sheet_name, indicator_name, unit)
BULLETIN_SHEETS = {
    "Т_16": ("Количество ИЖК по регионам", "шт"),
    "Т_17": ("Количество ИЖК по ДДУ по регионам", "шт"),
    "Т_18": ("Количество ИЖК на цели ИЖС по регионам", "шт"),
    "T_19": ("Объём ИЖК по регионам", "млн руб"),
    "T_20": ("Объём ИЖК по ДДУ по регионам", "млн руб"),
    "T_21": ("Объём ИЖК на цели ИЖС по регионам", "млн руб"),
    "T_22": ("Задолженность по ИЖК по регионам", "млн руб"),
    "T_23": ("Задолженность по ИЖК по ДДУ по регионам", "млн руб"),
    "T_24": ("Просроченная задолженность по ИЖК по регионам", "млн руб"),
    "T_25": ("Просроченная задолженность по ИЖК по ДДУ", "млн руб"),
    "T_26": ("Ставка по ИЖК по регионам", "%"),
    "T_27": ("Ставка по ИЖК по ДДУ по регионам", "%"),
    "T_28": ("Ставка по ИЖК без учёта ДДУ", "%"),
    "T_29": ("Ставка по ИЖК на цели ИЖС", "%"),
    "T_30": ("Доля ИЖК в общем объёме кредитов", "%"),
    "T_31": ("Доля задолженности по ИЖК", "%"),
    "T_32": ("Средний размер ИЖК", "млн руб"),
    "T_33": ("Средний размер ИЖК по ДДУ", "млн руб"),
    "Т_34": ("Средняя цена 1 кв.м по регионам", "руб"),
}


def parse_bulletin(fpath):
    """Parse mortgage lending market bulletin Section II sheets."""
    wb = openpyxl.load_workbook(fpath, read_only=True, data_only=True)
    records = []
    
    for sheet_name, (indicator, unit) in BULLETIN_SHEETS.items():
        # Try both cyrillic and latin T variants
        sn = None
        for variant in [sheet_name, sheet_name.replace("T_", "Т_"), sheet_name.replace("Т_", "T_")]:
            if variant in wb.sheetnames:
                sn = variant
                break
        if sn is None:
            print(f"  WARNING: sheet {sheet_name} not found")
            continue
        
        ws = wb[sn]
        
        if sheet_name == "Т_34":
            # Quarterly price table — special structure
            # Row 4: year, Row 5: quarters, Row 6: primary/secondary, Row 7+: data
            records.extend(parse_bulletin_quarterly(ws, indicator, unit))
            continue
        
        # Standard monthly sheets: find header row with month labels
        header_row = find_header_row(ws, max_check=6)
        if header_row is None:
            print(f"  WARNING: no header row in {sn}")
            continue
        
        header = list(ws.iter_rows(min_row=header_row, max_row=header_row, values_only=True))[0]
        months = []
        for cell in header[1:]:
            parsed = parse_month_header(cell)
            months.append(parsed)
        
        for row in ws.iter_rows(min_row=header_row + 1, values_only=True):
            name = row[0]
            if name is None:
                continue
            name = str(name).strip()
            if not (is_rf_row(name) or is_data_region(name)):
                continue
            
            for i, val in enumerate(row[1:]):
                if i >= len(months) or months[i] is None:
                    continue
                if val is None:
                    continue
                try:
                    num_val = float(val)
                except (ValueError, TypeError):
                    continue
                records.append((name, months[i], indicator, num_val, unit))
    
    wb.close()
    return records


def parse_bulletin_quarterly(ws, indicator, unit):
    """Parse T_34 quarterly price table with multi-level headers."""
    records = []
    
    # Row 4: year, Row 5: quarters, Row 6: primary/secondary market
    row4 = list(ws.iter_rows(min_row=4, max_row=4, values_only=True))[0]
    row5 = list(ws.iter_rows(min_row=5, max_row=5, values_only=True))[0]
    row6 = list(ws.iter_rows(min_row=6, max_row=6, values_only=True))[0]
    
    # Build column → (year, quarter, market) mapping
    col_meta = {}
    current_year = None
    current_quarter = None
    for i in range(1, len(row4)):
        if row4[i]:
            m = re.search(r"(\d{4})", str(row4[i]))
            if m:
                current_year = m.group(1)
        if row5[i]:
            qs = str(row5[i]).strip()
            qm = re.search(r"([IV]+)\s*квартал", qs, re.IGNORECASE)
            if qm:
                current_quarter = qm.group(1).upper()
        market = None
        if row6[i]:
            ms = str(row6[i]).strip().lower()
            if "первич" in ms:
                market = "первичный"
            elif "вторич" in ms:
                market = "вторичный"
        if current_year and current_quarter and market:
            # Convert quarter to month
            q_month = {"I": "01", "II": "04", "III": "07", "IV": "10"}
            report_date = f"{current_year}-{q_month.get(current_quarter, '01')}-01"
            col_meta[i] = (report_date, market)
    
    # Data from row 7
    for row in ws.iter_rows(min_row=7, values_only=True):
        name = row[0]
        if name is None:
            continue
        name = str(name).strip()
        if not (is_rf_row(name) or is_data_region(name)):
            continue
        
        for i, val in enumerate(row):
            if i == 0 or i not in col_meta:
                continue
            if val is None:
                continue
            try:
                num_val = float(val)
            except (ValueError, TypeError):
                continue
            report_date, market = col_meta[i]
            records.append((name, report_date, f"{indicator} ({market})", num_val, unit))
    
    return records


# ═════════════════════════════════════════════════════════════════════════
# ESCROW PARSER
# ═════════════════════════════════════════════════════════════════════════

ESCROW_COLUMNS = [
    "active_contracts_count",      # col 2
    "active_contracts_sum",         # col 3 — млн руб
    "debt",                         # col 4 — млн руб
    "escrow_accounts",              # col 5 — кол-во счетов с остатком
    "escrow_balance",               # col 6 — млн руб
    "credit_rate",                  # col 7 — %
    "escrow_disclosed_count",       # col 8 — кол-во раскрытых за месяц
    "escrow_disclosed_sum",         # col 9 — млн руб
]

ESCROW_UNITS = {
    "active_contracts_count": "шт",
    "active_contracts_sum": "млн руб",
    "debt": "млн руб",
    "escrow_accounts": "шт",
    "escrow_balance": "млн руб",
    "credit_rate": "%",
    "escrow_disclosed_count": "шт",
    "escrow_disclosed_sum": "млн руб",
}


def parse_escrow_file(fpath, report_date):
    """Parse a single escrow XLSX snapshot."""
    wb = openpyxl.load_workbook(fpath, read_only=True, data_only=True)
    ws = wb["по регионам"]
    records = []
    
    # Find header row (usually row 4, but scan)
    header_row_idx = None
    for r in range(1, 8):
        row = list(ws.iter_rows(min_row=r, max_row=r, values_only=True))[0]
        if row[0] and "№" in str(row[0]):
            header_row_idx = r
            break
    if header_row_idx is None:
        print(f"  WARNING: no header row in {fpath}")
        wb.close()
        return records
    
    # Data starts from header_row_idx + 1
    for row in ws.iter_rows(min_row=header_row_idx + 1, values_only=True):
        # Column 0: number or None (for FO rows)
        # Column 1: region name
        name = row[1] if len(row) > 1 else None
        if name is None:
            continue
        name = str(name).strip()
        if not name:
            continue
        
        # Keep both FO and region rows for escrow (FO has rate data)
        # But skip footnotes
        if re.match(r"^\d+\s+", name) or name.startswith("*") or name.startswith("ИТОГО"):
            continue
        # Skip footnote-like long text
        if len(name) > 60 and not any(kw in name for kw in ["область", "край", "Республика", "г.", "автоном", "ФО", "АО"]):
            continue
        
        # Parse data columns (indices 2-9)
        for col_idx, ind_name in enumerate(ESCROW_COLUMNS):
            cell_idx = col_idx + 2
            if cell_idx >= len(row):
                continue
            val = row[cell_idx]
            if val is None:
                continue
            try:
                num_val = float(val)
            except (ValueError, TypeError):
                continue
            records.append((name, report_date, ind_name, num_val, ESCROW_UNITS[ind_name]))
    
    wb.close()
    return records


def parse_escrow_date(filename):
    """Extract date from filename like 01082026.xlsx → 2026-08-01."""
    m = re.match(r"(\d{2})(\d{2})(\d{4})\.xlsx", filename)
    if m:
        dd, mm, yyyy = m.groups()
        return f"{yyyy}-{mm}-{dd}"
    return None


# ═════════════════════════════════════════════════════════════════════════
# MAIN IMPORT
# ═════════════════════════════════════════════════════════════════════════

def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    
    total_new = 0
    
    # ─── 1. VFS files ───────────────────────────────────────────────────
    print("=" * 70)
    print("1. Parsing VFS files...")
    print("=" * 70)
    
    vfs_files = [
        ("01_04_D_New_loans_subj.xlsx", "corporate_new"),
        ("01_05_D_Debt_subj.xlsx", "corporate_debt"),
        ("02_04_New_loans_ind.xlsx", "mortgage_new"),
        ("02_05_Debt_ind.xlsx", "mortgage_debt"),
    ]
    
    for fname, ftype in vfs_files:
        fpath = os.path.join(VFS_DIR, fname)
        if not os.path.exists(fpath):
            print(f"  MISSING: {fpath}")
            continue
        print(f"  Parsing {fname} ({ftype})...")
        records = parse_vfs_file(fpath, ftype)
        
        # Determine target table
        if ftype.startswith("corporate"):
            table = "corporate_monthly"
        else:
            table = "mortgage_monthly"
        
        inserted = 0
        for rec in records:
            cur.execute(
                f"INSERT OR REPLACE INTO {table} (region_name, report_date, indicator, value, unit) VALUES (?, ?, ?, ?, ?)",
                rec
            )
            inserted += 1
        conn.commit()
        print(f"    → {table}: {inserted} records")
        total_new += inserted
    
    # ─── 2. Mortgage bulletin ───────────────────────────────────────────
    print("\n" + "=" * 70)
    print("2. Parsing mortgage bulletin...")
    print("=" * 70)
    
    # Find latest bulletin
    bulletins = sorted([f for f in os.listdir(BULLETIN_DIR) if f.startswith("mortgage_lending_market") and f.endswith(".xlsx")])
    for bname in bulletins:
        fpath = os.path.join(BULLETIN_DIR, bname)
        print(f"  Parsing {bname}...")
        records = parse_bulletin(fpath)
        inserted = 0
        for rec in records:
            cur.execute(
                "INSERT OR REPLACE INTO mortgage_monthly (region_name, report_date, indicator, value, unit) VALUES (?, ?, ?, ?, ?)",
                rec
            )
            inserted += 1
        conn.commit()
        print(f"    → mortgage_monthly: {inserted} records")
        total_new += inserted
    
    # ─── 3. Escrow files ───────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("3. Parsing escrow files...")
    print("=" * 70)
    
    escrow_files = sorted([f for f in os.listdir(ESCROW_DIR) if f.endswith(".xlsx") and re.match(r"\d{8}\.xlsx", f)])
    print(f"  Found {len(escrow_files)} escrow files")
    
    for ename in escrow_files:
        fpath = os.path.join(ESCROW_DIR, ename)
        report_date = parse_escrow_date(ename)
        if report_date is None:
            print(f"  SKIP: cannot parse date from {ename}")
            continue
        records = parse_escrow_file(fpath, report_date)
        inserted = 0
        for rec in records:
            cur.execute(
                "INSERT OR REPLACE INTO escrow_monthly (region_name, report_date, indicator, value, unit) VALUES (?, ?, ?, ?, ?)",
                rec
            )
            inserted += 1
        conn.commit()
        total_new += inserted
    print(f"  → escrow_monthly: {total_new} total processed (INSERT OR REPLACE)")
    
    # ─── Summary ────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    for table in ["mortgage_monthly", "escrow_monthly", "corporate_monthly"]:
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        total = cur.fetchone()[0]
        cur.execute(f"SELECT MAX(report_date) FROM {table}")
        latest = cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(DISTINCT report_date) FROM {table}")
        n_dates = cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(DISTINCT region_name) FROM {table}")
        n_regions = cur.fetchone()[0]
        cur.execute(f"SELECT COUNT(DISTINCT indicator) FROM {table}")
        n_inds = cur.fetchone()[0]
        print(f"\n  {table}:")
        print(f"    Total records: {total:,}")
        print(f"    Latest date: {latest}")
        print(f"    Distinct dates: {n_dates}")
        print(f"    Distinct regions: {n_regions}")
        print(f"    Distinct indicators: {n_inds}")
    
    # Top 5 regions by mortgage volume (latest month, ИЖК volume indicator)
    print("\n  Top 5 regions by ИЖК volume (latest month):")
    cur.execute("""
        SELECT region_name, value 
        FROM mortgage_monthly 
        WHERE indicator = 'Объём ИЖК по регионам' 
          AND report_date = (SELECT MAX(report_date) FROM mortgage_monthly WHERE indicator = 'Объём ИЖК по регионам')
          AND region_name != 'РОССИЙСКАЯ ФЕДЕРАЦИЯ'
        ORDER BY value DESC 
        LIMIT 5
    """)
    for r, v in cur.fetchall():
        print(f"    {r}: {v:,.1f} млн руб")
    
    # Top 5 regions by mortgage new loans (VFS, latest month)
    print("\n  Top 5 regions by mortgage new loans (VFS, latest month):")
    cur.execute("""
        SELECT region_name, value 
        FROM mortgage_monthly 
        WHERE indicator = 'Ипотека физлицам — новые выдачи (итого)' 
          AND report_date = (SELECT MAX(report_date) FROM mortgage_monthly WHERE indicator = 'Ипотека физлицам — новые выдачи (итого)')
          AND region_name != 'РОССИЙСКАЯ ФЕДЕРАЦИЯ'
        ORDER BY value DESC 
        LIMIT 5
    """)
    for r, v in cur.fetchall():
        print(f"    {r}: {v:,.1f} млн руб")
    
    # Top 5 regions by escrow balance (latest)
    print("\n  Top 5 regions by escrow balance (latest snapshot):")
    cur.execute("""
        SELECT region_name, value 
        FROM escrow_monthly 
        WHERE indicator = 'escrow_balance' 
          AND report_date = (SELECT MAX(report_date) FROM escrow_monthly WHERE indicator = 'escrow_balance')
          AND region_name NOT LIKE '%ФО%'
        ORDER BY value DESC 
        LIMIT 5
    """)
    for r, v in cur.fetchall():
        print(f"    {r}: {v:,.1f} млн руб")
    
    conn.close()
    print("\n✓ Done.")


if __name__ == "__main__":
    main()