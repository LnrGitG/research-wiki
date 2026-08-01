#!/usr/bin/env python3
"""
CBR Data Ingester
Downloads and normalizes CBR statistical data to Parquet.
Supports: XLSX (mortgage stats), JSON API (key rate)
"""
import yaml
import pandas as pd
import requests
import duckdb
from pathlib import Path
from datetime import datetime
import sys
import json
import io
import xml.etree.ElementTree as ET

ROOT = Path(__file__).parent.parent
CATALOG = ROOT / "data/catalog.yaml"
RAW_DIR = ROOT / "data/raw"
PROCESSED_DIR = ROOT / "data/processed"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def load_catalog():
    with open(CATALOG, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_metadata(table_name: str, meta: dict):
    """Save ingestion metadata"""
    meta_path = PROCESSED_DIR / f"{table_name}.meta.json"
    meta['ingested_at'] = datetime.now().isoformat()
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')

def ingest_xlsx_source(source: dict) -> pd.DataFrame:
    """Download and parse XLSX from CBR - handles multi-sheet files"""
    url = source['url']
    sheet = source.get('sheet', None)  # None = all sheets
    header_row = source.get('header_row', None)  # No header, we handle structure manually
    
    print(f"  Downloading {url}...")
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    
    # Save raw copy
    raw_path = RAW_DIR / f"{source['id']}.xlsx"
    raw_path.write_bytes(r.content)
    print(f"  Saved raw: {raw_path}")
    
    # Parse Excel - get all sheets if sheet is None
    if sheet is None:
        # Read all sheets
        xls = pd.read_excel(io.BytesIO(r.content), sheet_name=None, header=None)
        print(f"  Sheets found: {list(xls.keys())}")
        
        # Normalize each sheet and combine
        all_dfs = []
        for sheet_name, df_sheet in xls.items():
            print(f"  Processing sheet: {sheet_name} (shape: {df_sheet.shape})")
            df_norm = normalize_mortgage_new_loans(df_sheet, sheet_name)
            if len(df_norm) > 0:
                all_dfs.append(df_norm)
        
        if all_dfs:
            df = pd.concat(all_dfs, ignore_index=True)
            print(f"  Combined shape: {df.shape}")
        else:
            df = pd.DataFrame(columns=['region', 'period', 'metric', 'currency', 'value'])
    else:
        # Single sheet
        df = pd.read_excel(io.BytesIO(r.content), sheet_name=sheet, header=header_row)
        print(f"  Sheet '{sheet}' shape: {df.shape}")
        df = normalize_mortgage_new_loans(df, sheet)
    
    print(f"  Columns: {list(df.columns)}")
    return df

def ingest_json_source(source: dict) -> pd.DataFrame:
    """Download and parse JSON from CBR API"""
    url = source['url']
    
    print(f"  Downloading {url}...")
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    
    data = r.json()
    
    # Save raw copy
    raw_path = RAW_DIR / f"{source['id']}.json"
    raw_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"  Saved raw: {raw_path}")
    
    # CBR keyrate API returns list of dicts
    df = pd.DataFrame(data)
    print(f"  Raw shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    
    return df

def ingest_csv_source(source: dict) -> pd.DataFrame:
    """Download and parse CSV from URL (Rosstat, etc.)"""
    url = source['url']
    
    print(f"  Downloading {url}...")
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    
    # Save raw copy
    raw_path = RAW_DIR / f"{source['id']}.csv"
    raw_path.write_bytes(r.content)
    print(f"  Saved raw: {raw_path}")
    
    # Detect encoding
    import chardet
    enc = chardet.detect(r.content[:10000])['encoding'] or 'utf-8'
    
    # Parse CSV with various separators
    for sep in [',', ';', '\t']:
        try:
            df = pd.read_csv(io.BytesIO(r.content), encoding=enc, sep=sep)
            if len(df.columns) > 1:
                break
        except:
            continue
    else:
        df = pd.read_csv(io.BytesIO(r.content), encoding=enc, sep=None, engine='python')
    
    print(f"  Raw shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    
    return df

def ingest_xml_source(source: dict) -> pd.DataFrame:
    """Download and parse XML from CBR API (e.g., exchange rates)"""
    url = source['url']
    
    print(f"  Downloading {url}...")
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    
    # Save raw copy
    raw_path = RAW_DIR / f"{source['id']}.xml"
    raw_path.write_bytes(r.content)
    print(f"  Saved raw: {raw_path}")
    
    # Parse XML
    root = ET.fromstring(r.content)
    
    # CBR XML structure: <ValCurs><Record Date="..." Id="..."><Nominal>1</Nominal><Value>...</Value><VunitRate>...</VunitRate></Record></ValCurs>
    records = []
    for record in root.findall('.//Record'):
        date_str = record.get('Date')
        nominal = record.find('Nominal')
        value = record.find('Value')
        vunit_rate = record.find('VunitRate')
        
        records.append({
            'date': date_str,
            'nominal': int(nominal.text) if nominal is not None else 1,
            'value': value.text if value is not None else None,
            'vunit_rate': vunit_rate.text if vunit_rate is not None else None,
        })
    
    df = pd.DataFrame(records)
    print(f"  Raw shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    
    return df

def normalize_mortgage_new_loans(df_raw: pd.DataFrame, sheet_name: str) -> pd.DataFrame:
    """Normalize a single sheet from 02_04_New_loans_ind.xlsx"""
    # Actual sheet structure (0-indexed):
    # Row 0: metric description in A1 (merged cell, reads as NaN in pandas)
    # Row 1: all NaN
    # Row 2: period headers starting from column B (index 1)
    # Row 3+: region data
    
    if len(df_raw) < 4:
        return pd.DataFrame(columns=['region', 'period', 'metric', 'currency', 'value'])
    
    # Determine metric type from sheet name
    if 'рублях' in sheet_name:
        metric = 'volume_mln_rub'
        currency = 'RUB'
    elif 'валюте' in sheet_name:
        metric = 'volume_mln_rub'
        currency = 'FX'
    elif 'итого' in sheet_name:
        metric = 'volume_mln_rub'
        currency = 'TOTAL'
    else:
        metric = 'volume_mln_rub'
        currency = 'UNKNOWN'
    
    # Row 2 has period headers (index 2)
    period_row = df_raw.iloc[2]
    
    # Data starts from row 3 (index 3)
    data_rows = df_raw.iloc[3:].copy()
    
    # First column is region
    region_col = data_rows.columns[0]
    data_rows = data_rows.rename(columns={region_col: 'region'})
    
    # Period columns are all except region
    period_cols = [c for c in data_rows.columns if c != 'region']
    
    df_long = data_rows.melt(id_vars=['region'], value_vars=period_cols,
                              var_name='period_raw', value_name='value')
    
    # Map period_raw to actual period from header row (row 2)
    period_map = {}
    for col in period_cols:
        if col in period_row.index:
            period_map[col] = period_row[col]
        else:
            period_map[col] = col
    
    df_long['period_str'] = df_long['period_raw'].map(period_map)
    
    # Parse Russian month names to datetime
    def parse_russian_period(p):
        if pd.isna(p):
            return pd.NaT
        p = str(p).strip()
        # Format: "Январь 2019", "Февраль 2020", etc.
        ru_months = {
            'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4,
            'май': 5, 'июнь': 6, 'июль': 7, 'август': 8,
            'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12
        }
        parts = p.lower().split()
        if len(parts) == 2:
            month_name, year_str = parts
            if month_name in ru_months:
                try:
                    year = int(year_str)
                    month = ru_months[month_name]
                    return pd.Timestamp(year=year, month=month, day=1)
                except:
                    pass
        # Fallback
        try:
            return pd.to_datetime(p)
        except:
            return pd.NaT
    
    df_long['period'] = df_long['period_str'].apply(parse_russian_period)
    df_long = df_long.dropna(subset=['period'])
    
    # Clean region names
    df_long['region'] = df_long['region'].astype(str).str.strip()
    df_long = df_long[df_long['region'] != 'nan']
    df_long = df_long[df_long['region'] != '']
    
    # Convert values to numeric
    df_long['value'] = pd.to_numeric(df_long['value'], errors='coerce')
    df_long = df_long.dropna(subset=['value'])
    
    # Add metric info
    df_long['metric'] = metric
    df_long['currency'] = currency
    
    # Sort
    df_long = df_long.sort_values(['region', 'period']).reset_index(drop=True)
    
    return df_long[['region', 'period', 'metric', 'currency', 'value']]

def normalize_exchange_rate(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize exchange rate XML data"""
    df = df.copy()
    df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')
    df['nominal'] = pd.to_numeric(df['nominal'], errors='coerce')
    df['value'] = pd.to_numeric(df['value'].str.replace(',', '.'), errors='coerce')
    df['vunit_rate'] = pd.to_numeric(df['vunit_rate'].str.replace(',', '.'), errors='coerce')
    df = df.dropna(subset=['date', 'vunit_rate'])
    df = df.sort_values('date').drop_duplicates(subset='date', keep='last')
    return df.reset_index(drop=True)

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
        # Download and parse
        if source['format'] == 'xlsx':
            df = ingest_xlsx_source(source)
        elif source['format'] == 'json':
            df_raw = ingest_json_source(source)
            df = normalize_exchange_rate(df_raw)
        elif source['format'] == 'xml':
            df_raw = ingest_xml_source(source)
            df = normalize_exchange_rate(df_raw)
        elif source['format'] == 'csv':
            df_raw = ingest_csv_source(source)
            # For Rosstat CSVs, we'll need custom normalizers
            df = df_raw  # placeholder
        else:
            print(f"❌ Unsupported format: {source['format']}")
            return False
        
        # Save processed Parquet
        out_path = PROCESSED_DIR / f"{source['table']}.parquet"
        df.to_parquet(out_path, index=False)
        print(f"✅ Saved: {out_path} ({len(df)} rows)")
        
        # Metadata
        meta = {
            'source': source['id'],
            'name': source['name'],
            'url': source['url'],
            'rows': len(df),
            'columns': list(df.columns),
            'dtypes': {c: str(df[c].dtype) for c in df.columns},
        }
        if 'period' in df.columns:
            meta['period_range'] = f"{df['period'].min()} → {df['period'].max()}"
        if 'date' in df.columns:
            meta['date_range'] = f"{df['date'].min()} → {df['date'].max()}"
        if 'region' in df.columns:
            meta['regions_count'] = df['region'].nunique()
            meta['regions_sample'] = df['region'].unique()[:10].tolist()
        
        save_metadata(source['table'], meta)
        print(f"✅ Metadata saved")
        
        # Also register in DuckDB for immediate querying
        con = duckdb.connect()
        con.execute(f"CREATE OR REPLACE VIEW {source['table']} AS SELECT * FROM read_parquet('{out_path}')")
        print(f"✅ DuckDB view created: {source['table']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python ingest_cbr.py <source_id>")
        print("Available sources:")
        for s in load_catalog()['sources']:
            print(f"  - {s['id']}: {s['name']}")
        sys.exit(1)
    
    source_id = sys.argv[1]
    success = ingest_source(source_id)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()