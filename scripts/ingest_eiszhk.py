#!/usr/bin/env python3
"""
ЕИСЖС / ДОМ.РФ Data Ingester for Yandex Disk exports
Processes the specific multi-sheet XLSX format from ЕИСЖС statistical series.
"""
import pandas as pd
import yaml
import json
from pathlib import Path
from datetime import datetime
import datetime as dt
import sys
import io

ROOT = Path(__file__).parent.parent
CATALOG = ROOT / "data/catalog.yaml"
RAW_DIR = ROOT / "data/raw/domrf/yandex_disk_import"
PROCESSED_DIR = ROOT / "data/processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def load_catalog():
    with open(CATALOG, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_metadata(table_name: str, meta: dict):
    meta_path = PROCESSED_DIR / f"{table_name}.meta.json"
    meta['ingested_at'] = datetime.now().isoformat()
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')

def parse_eiszhk_date(col_name) -> pd.Timestamp:
    """Parse date from ЕИСЖС column headers"""
    if pd.isna(col_name):
        return pd.NaT
    s = str(col_name).strip()
    # Try various formats
    for fmt in ['%d.%m.%Y', '%m.%Y', '%Y-%m-%d', '%Y-%m', '%Y']:
        try:
            return pd.to_datetime(s, format=fmt)
        except:
            pass
    # Russian month names
    ru_months = {
        'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4,
        'май': 5, 'июнь': 6, 'июль': 7, 'август': 8,
        'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12,
    }
    parts = s.lower().split()
    if len(parts) == 2:
        month_name, year_str = parts
        for k, v in ru_months.items():
            if month_name.startswith(k):
                try:
                    return pd.Timestamp(year=int(year_str), month=v, day=1)
                except:
                    pass
    try:
        return pd.to_datetime(s)
    except:
        return pd.NaT

def normalize_eiszhk_sheet(df_raw: pd.DataFrame, sheet_name: str, file_name: str) -> pd.DataFrame:
    """
    Normalize a single ЕИСЖС sheet.
    Handles two formats:
    1. Region x Date (standard)
    2. Metric x Year (like ИЖК file)
    """
    df = df_raw.copy()
    
    # Extract metric name from row 1 (index 1) for standard format
    metric_name = ""
    if len(df) > 1:
        metric_name = str(df.iloc[1, 0]).strip()
    
    # Find the header row (contains 'Регион', 'Показатель', or has year values in columns 1+)
    header_row_idx = None
    for i in range(min(5, len(df))):
        val = str(df.iloc[i, 0]).lower()
        if 'регион' in val or 'показатель' in val:
            header_row_idx = i
            break
        # Also check if this row has year-like values in columns 1+
        if i < len(df):
            row_vals = df.iloc[i, 1:].values
            year_count = sum(1 for v in row_vals if isinstance(v, (int, float)) and 2000 <= v <= 2030)
            if year_count >= 3:  # At least 3 year columns
                header_row_idx = i
                break
    
    if header_row_idx is not None:
        # Check if this is format 2 (Metric x Year) - no region column
        first_row_after_header = df.iloc[header_row_idx]
        year_cols = []
        for j, val in enumerate(first_row_after_header):
            if isinstance(val, (int, float)) and 2000 <= val <= 2030:
                year_cols.append(j)
        
        # If first column is NOT 'Регион' and we have year columns, it's format 2
        first_col_name = str(first_row_after_header.iloc[0]).lower() if len(first_row_after_header) > 0 else ''
        is_format_2 = ('регион' not in first_col_name and 'показатель' not in first_col_name and len(year_cols) >= 3)
        
        if is_format_2:
            # Format 2: Metric x Year (like ИЖК)
            # First column has metric names, year columns have years
            metrics_col = df.iloc[:, 0]
            year_values = df.iloc[header_row_idx, year_cols].values
            
            result_rows = []
            for idx in range(header_row_idx + 1, len(df)):
                metric = str(metrics_col.iloc[idx]).strip()
                if not metric or metric.lower() in ('nan', ''):
                    continue
                
                for j, year_col in enumerate(year_cols):
                    year = year_values[j]
                    if pd.isna(year):
                        continue
                    value = df.iloc[idx, year_col]
                    if pd.notna(value):
                        try:
                            val_num = float(str(value).replace(',', '.').replace(' ', ''))
                            result_rows.append({
                                'region': 'Российская Федерация',
                                'period': pd.Timestamp(year=int(year), month=1, day=1),
                                'metric': metric,
                                'value': val_num,
                                'source_file': file_name,
                                'sheet': sheet_name
                            })
                        except:
                            pass
            
            if not result_rows:
                return pd.DataFrame()
            
            df_long = pd.DataFrame(result_rows)
            return df_long[['region', 'period', 'metric', 'value', 'source_file', 'sheet']]
        
        else:
            # Format 1: Region x Date (standard)
            # Extract metric name from row before header (usually header_row_idx - 1 or header_row_idx - 2 if empty row)
            if header_row_idx > 0:
                potential_metric = str(df.iloc[header_row_idx - 1, 0]).strip()
                if potential_metric and potential_metric.lower() not in ('nan', ''):
                    metric_name = potential_metric
                elif header_row_idx > 1:
                    potential_metric2 = str(df.iloc[header_row_idx - 2, 0]).strip()
                    if potential_metric2 and potential_metric2.lower() not in ('nan', ''):
                        metric_name = potential_metric2
            
            df.columns = df.iloc[header_row_idx]
            df = df.iloc[header_row_idx + 1:].reset_index(drop=True)
            
            region_col = df.columns[0]
            df = df.rename(columns={region_col: 'region'})
            
            # Remove empty/non-region rows
            df = df[df['region'].notna() & (df['region'].astype(str).str.strip() != '')]
            df = df[~df['region'].astype(str).str.contains('Архангельская и Тюменская|Перейти|Данные в разрезе', na=False)]
            
            # Identify date columns (already datetime objects from Excel)
            date_cols = []
            for col in df.columns[1:]:
                if isinstance(col, (pd.Timestamp, dt.datetime)):
                    date_cols.append(col)
                else:
                    parsed = parse_eiszhk_date(col)
                    if not pd.isna(parsed):
                        date_cols.append(col)
            
            if not date_cols:
                return pd.DataFrame()
            
            # Melt wide to long
            df_long = df.melt(id_vars=['region'], value_vars=date_cols, var_name='period_raw', value_name='value')
            
            # Clean region
            df_long['region'] = df_long['region'].astype(str).str.strip()
            df_long = df_long[df_long['region'] != '']
            df_long = df_long[df_long['region'].str.lower() != 'nan']
            
            # Parse period (already datetime)
            df_long['period'] = pd.to_datetime(df_long['period_raw'])
            df_long = df_long.dropna(subset=['period'])
            
            # Parse value
            def parse_val(v):
                if pd.isna(v):
                    return None
                s = str(v).strip().replace(' ', '').replace(',', '.')
                if s in ('', '-', 'nan', 'NaN'):
                    return None
                try:
                    return float(s)
                except:
                    return None
            
            df_long['value'] = df_long['value'].apply(parse_val)
            df_long = df_long.dropna(subset=['value'])
            
            # Add metric
            df_long['metric'] = metric_name
            df_long['source_file'] = file_name
            df_long['sheet'] = sheet_name
            
            return df_long[['region', 'period', 'metric', 'value', 'source_file', 'sheet']]
    
    return pd.DataFrame()

def ingest_eiszhk_file(file_path: Path) -> pd.DataFrame:
    """Ingest a single ЕИСЖС XLSX file - optimized"""
    print(f"  Reading {file_path.name}...")
    
    # Read sheet names only first
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    print(f"  Sheets: {len(sheet_names)}")
    
    all_dfs = []
    for sheet_name in sheet_names:
        # Skip TOC sheets (usually 00)
        if sheet_name.endswith('_00') or sheet_name == '0 Сводный':
            continue
        try:
            # Read single sheet
            df_raw = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
            df_norm = normalize_eiszhk_sheet(df_raw, sheet_name, file_path.name)
            if len(df_norm) > 0:
                all_dfs.append(df_norm)
                print(f"    {sheet_name}: {len(df_norm)} rows")
        except Exception as e:
            print(f"    {sheet_name}: ERROR - {e}")
    
    if not all_dfs:
        return pd.DataFrame()
    
    df = pd.concat(all_dfs, ignore_index=True)
    # Deduplicate
    df = df.drop_duplicates(subset=['region', 'period', 'metric', 'value', 'source_file', 'sheet'])
    df = df.sort_values(['region', 'period', 'metric', 'sheet']).reset_index(drop=True)
    
    return df

def ingest_source(source_id: str):
    catalog = load_catalog()
    source = next((s for s in catalog['sources'] if s['id'] == source_id), None)
    
    if not source:
        print(f"❌ Source '{source_id}' not found in catalog")
        return False
    
    print(f"\n{'='*60}")
    print(f"INGESTING: {source['name']} ({source['id']})")
    print(f"{'='*60}")
    
    try:
        pattern = source.get('file_pattern', '*')
        files = list(RAW_DIR.glob(pattern))
        if not files:
            print(f"⚠️ No files found matching '{pattern}' in {RAW_DIR}")
            return False
        
        all_dfs = []
        for f in files:
            if f.suffix.lower() in ('.xlsx', '.xls'):
                df = ingest_eiszhk_file(f)
                if len(df) > 0:
                    all_dfs.append(df)
        
        if not all_dfs:
            print("❌ No valid data extracted")
            return False
        
        df = pd.concat(all_dfs, ignore_index=True)
        df = df.drop_duplicates(subset=['region', 'period', 'metric', 'value', 'source_file', 'sheet'])
        df = df.sort_values(['region', 'period', 'metric', 'sheet']).reset_index(drop=True)
        
        # Save
        out_path = PROCESSED_DIR / f"{source['table']}.parquet"
        df.to_parquet(out_path, index=False)
        print(f"✅ Saved: {out_path} ({len(df)} rows)")
        
        # Metadata
        meta = {
            'source': source['id'],
            'name': source['name'],
            'files': [f.name for f in files],
            'rows': len(df),
            'columns': list(df.columns),
            'dtypes': {c: str(df[c].dtype) for c in df.columns},
        }
        if 'period' in df.columns:
            meta['period_range'] = f"{df['period'].min()} → {df['period'].max()}"
        if 'region' in df.columns:
            meta['regions_count'] = df['region'].nunique()
            meta['regions_sample'] = df['region'].unique()[:10].tolist()
        if 'metric' in df.columns:
            meta['metrics'] = df['metric'].unique().tolist()
        if 'sheet' in df.columns:
            meta['sheets'] = df['sheet'].unique().tolist()
        
        save_metadata(source['table'], meta)
        print(f"✅ Metadata saved")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python ingest_eiszhk.py <source_id>")
        print("Available sources:")
        for s in load_catalog()['sources']:
            if s['id'].startswith('eiszhk') or s['id'].startswith('domrf_'):
                print(f"  - {s['id']}: {s['name']}")
        sys.exit(1)
    
    source_id = sys.argv[1]
    success = ingest_source(source_id)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()