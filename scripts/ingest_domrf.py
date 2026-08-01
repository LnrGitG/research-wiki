#!/usr/bin/env python3
"""
DOM.RF Data Ingester
Processes manually exported CSV/XLSX files from DOM.RF statistical series.
User downloads files in browser -> places in data/raw/domrf/ -> this script normalizes to Parquet.
"""
import pandas as pd
import yaml
from pathlib import Path
from datetime import datetime
import sys
import json
import io

ROOT = Path(__file__).parent.parent
CATALOG = ROOT / "data/catalog.yaml"
RAW_DIR = ROOT / "data/raw/domrf"
PROCESSED_DIR = ROOT / "data/processed"

RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def load_catalog():
    with open(CATALOG, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def save_metadata(table_name: str, meta: dict):
    meta_path = PROCESSED_DIR / f"{table_name}.meta.json"
    meta['ingested_at'] = datetime.now().isoformat()
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')

def detect_encoding(file_path: Path) -> str:
    """Detect file encoding"""
    import chardet
    with open(file_path, 'rb') as f:
        raw = f.read(10000)
    result = chardet.detect(raw)
    return result['encoding'] or 'utf-8'

def read_any(file_path: Path) -> pd.DataFrame:
    """Read CSV, XLSX, or XLS with encoding detection"""
    suffix = file_path.suffix.lower()
    
    if suffix in ('.xlsx', '.xls'):
        # Try to read all sheets
        xls = pd.read_excel(file_path, sheet_name=None, header=None)
        if len(xls) == 1:
            return list(xls.values())[0]
        else:
            # Combine all sheets
            dfs = []
            for name, df in xls.items():
                df = df.copy()
                df['_sheet'] = name
                dfs.append(df)
            return pd.concat(dfs, ignore_index=True)
    
    elif suffix == '.csv':
        enc = detect_encoding(file_path)
        try:
            return pd.read_csv(file_path, encoding=enc, sep=None, engine='python')
        except:
            # Try common Russian encodings
            for enc in ['cp1251', 'utf-8-sig', 'utf-8']:
                try:
                    return pd.read_csv(file_path, encoding=enc, sep=None, engine='python')
                except:
                    continue
            raise
    
    else:
        raise ValueError(f"Unsupported format: {suffix}")

def normalize_domrf_housing_starts(df_raw: pd.DataFrame, source_file: str) -> pd.DataFrame:
    """Normalize DOM.RF housing starts data (ввод жилья)"""
    # Expected structure varies, try to auto-detect
    df = df_raw.copy()
    
    # If first row looks like header, use it
    if len(df) > 0:
        first_row = df.iloc[0].astype(str).str.lower()
        if any('регион' in str(v) or 'region' in str(v) for v in first_row):
            df.columns = df.iloc[0]
            df = df.iloc[1:].reset_index(drop=True)
    
    # Clean column names
    df.columns = [str(c).strip().lower().replace('\n', ' ') for c in df.columns]
    
    # Try to find key columns
    region_col = None
    period_col = None
    value_cols = []
    
    for c in df.columns:
        c_low = c.lower()
        if any(k in c_low for k in ['регион', 'region', 'субъект', 'область', 'край', 'город']):
            region_col = c
        elif any(k in c_low for k in ['период', 'period', 'дата', 'date', 'год', 'year', 'месяц', 'month', 'квартал', 'quarter']):
            period_col = c
        elif any(k in c_low for k in ['ввод', 'площад', 'м2', 'м.кв', 'тыс', 'млн', 'кв.м', 'квадрат']):
            value_cols.append(c)
        elif df[c].dtype in ('float64', 'int64', 'float32', 'int32'):
            # Numeric column - potential value
            value_cols.append(c)
    
    if not region_col and len(df.columns) > 0:
        region_col = df.columns[0]  # First column usually region
    
    if not period_col:
        # Try to find period in column names (e.g., "2024", "Январь 2024")
        period_cols = [c for c in df.columns if any(str(y) in str(c) for y in range(2010, 2030))]
        if period_cols:
            # Wide format - melt
            id_vars = [region_col] if region_col else []
            df = df.melt(id_vars=id_vars, value_vars=period_cols, var_name='period', value_name='value')
            period_col = 'period'
            value_cols = ['value']
    
    if not value_cols and len(df.columns) > 1:
        value_cols = [c for c in df.columns if c != region_col and c != period_col]
    
    # Build normalized dataframe
    result_rows = []
    
    if period_col and value_cols:
        # Long format or melted
        for _, row in df.iterrows():
            region = str(row[region_col]).strip() if region_col else 'Россия'
            period_raw = row[period_col] if period_col else None
            
            for val_col in value_cols:
                value = row[val_col]
                if pd.notna(value) and str(value).strip():
                    try:
                        val_num = float(str(value).replace(',', '.').replace(' ', ''))
                        result_rows.append({
                            'region': region,
                            'period_raw': str(period_raw),
                            'metric': val_col,
                            'value': val_num,
                            'source_file': source_file
                        })
                    except:
                        pass
    else:
        # Fallback: try to extract any numeric data
        for _, row in df.iterrows():
            region = str(row.iloc[0]).strip() if len(row) > 0 else 'Россия'
            for i, val in enumerate(row.iloc[1:], 1):
                if pd.notna(val) and str(val).strip():
                    try:
                        val_num = float(str(val).replace(',', '.').replace(' ', ''))
                        col_name = df.columns[i] if i < len(df.columns) else f'col_{i}'
                        result_rows.append({
                            'region': region,
                            'period_raw': col_name,
                            'metric': col_name,
                            'value': val_num,
                            'source_file': source_file
                        })
                    except:
                        pass
    
    if not result_rows:
        return pd.DataFrame(columns=['region', 'period', 'metric', 'value', 'source_file'])
    
    df_norm = pd.DataFrame(result_rows)
    
    # Parse period
    def parse_period(p):
        if pd.isna(p):
            return pd.NaT
        p = str(p).strip()
        # Try various formats
        for fmt in ['%Y-%m-%d', '%d.%m.%Y', '%Y-%m', '%m.%Y', '%Y', '%B %Y', '%b %Y']:
            try:
                return pd.to_datetime(p, format=fmt)
            except:
                pass
        # Russian month names
        ru_months = {
            'январь': 1, 'февраль': 2, 'март': 3, 'апрель': 4,
            'май': 5, 'июнь': 6, 'июль': 7, 'август': 8,
            'сентябрь': 9, 'октябрь': 10, 'ноябрь': 11, 'декабрь': 12,
            'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4,
            'май': 5, 'июн': 6, 'июл': 7, 'авг': 8,
            'сен': 9, 'окт': 10, 'ноя': 11, 'дек': 12
        }
        parts = p.lower().split()
        if len(parts) == 2:
            month_name, year_str = parts
            for k, v in ru_months.items():
                if month_name.startswith(k):
                    try:
                        year = int(year_str)
                        return pd.Timestamp(year=year, month=v, day=1)
                    except:
                        pass
        try:
            return pd.to_datetime(p)
        except:
            return pd.NaT
    
    df_norm['period'] = df_norm['period_raw'].apply(parse_period)
    df_norm = df_norm.dropna(subset=['period', 'value'])
    
    # Clean region
    df_norm['region'] = df_norm['region'].str.strip()
    df_norm = df_norm[df_norm['region'] != '']
    df_norm = df_norm[df_norm['region'].str.lower() != 'nan']
    
    # Aggregate duplicates
    df_norm = df_norm.groupby(['region', 'period', 'metric'], as_index=False)['value'].sum()
    df_norm = df_norm.sort_values(['region', 'period', 'metric']).reset_index(drop=True)
    
    # Add source_file
    df_norm['source_file'] = source_file
    
    return df_norm[['region', 'period', 'metric', 'value', 'source_file']]

def normalize_domrf_sales(df_raw: pd.DataFrame, source_file: str) -> pd.DataFrame:
    """Normalize DOM.RF sales data (реализация квартир)"""
    # Same logic as housing starts
    return normalize_domrf_housing_starts(df_raw, source_file)

def normalize_domrf_generic(df_raw: pd.DataFrame, source_file: str, metric_prefix: str = 'domrf') -> pd.DataFrame:
    """Generic normalizer for any DOM.RF table"""
    return normalize_domrf_housing_starts(df_raw, source_file)

NORMALIZERS = {
    'housing_starts': normalize_domrf_housing_starts,
    'sales': normalize_domrf_sales,
    'construction': normalize_domrf_housing_starts,
    'prices': normalize_domrf_housing_starts,
    'mortgage': normalize_domrf_housing_starts,
    'generic': normalize_domrf_generic,
}

def ingest_domrf_file(file_path: Path, data_type: str = 'generic') -> pd.DataFrame:
    """Ingest a single DOM.RF export file"""
    print(f"  Reading {file_path.name}...")
    df_raw = read_any(file_path)
    print(f"  Raw shape: {df_raw.shape}, columns: {list(df_raw.columns)[:10]}")
    
    normalizer = NORMALIZERS.get(data_type, normalize_domrf_generic)
    df = normalizer(df_raw, file_path.name)
    print(f"  Normalized: {len(df)} rows")
    
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
        data_type = source.get('data_type', 'generic')
        pattern = source.get('file_pattern', '*')
        
        files = list(RAW_DIR.glob(pattern))
        if not files:
            print(f"⚠️ No files found in {RAW_DIR} matching '{pattern}'")
            print(f"   Please download exports from DOM.RF and place them in {RAW_DIR}")
            return False
        
        all_dfs = []
        for f in files:
            df = ingest_domrf_file(f, data_type)
            if len(df) > 0:
                all_dfs.append(df)
        
        if not all_dfs:
            print("❌ No valid data extracted")
            return False
        
        df = pd.concat(all_dfs, ignore_index=True)
        # Deduplicate
        df = df.drop_duplicates(subset=['region', 'period', 'metric', 'value', 'source_file'])
        df = df.sort_values(['region', 'period', 'metric']).reset_index(drop=True)
        
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
        print("Usage: python ingest_domrf.py <source_id>")
        print("Available sources:")
        for s in load_catalog()['sources']:
            if s['id'].startswith('domrf'):
                print(f"  - {s['id']}: {s['name']}")
        sys.exit(1)
    
    source_id = sys.argv[1]
    success = ingest_source(source_id)
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()