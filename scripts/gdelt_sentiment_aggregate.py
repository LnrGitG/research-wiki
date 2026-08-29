#!/usr/bin/env python3
import pandas as pd
import glob
import os
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), '../data/raw/gdelt')
OUT_DIR  = os.path.join(os.path.dirname(__file__), '../data/processed')
os.makedirs(OUT_DIR, exist_ok=True)

# List of themes we consider relevant to real estate / mortgage
RELEVANT_THEMES = {
    'ECONOMICS_REAL_ESTATE',
    'MORTGAGE',
    'PROPERTY_TAX',
    'CONSTRUCTION',
    'HOUSING'
}

def parse_themes(cell):
    """Return set of themes from a semicolon-separated string."""
    if pd.isna(cell):
        return set()
    return set(cell.split(';'))

def main():
    files = sorted(glob.glob(os.path.join(DATA_DIR, 'gdelt_gkg_rus_*.csv')))
    if not files:
        print("No GDELT GKG files found in", DATA_DIR)
        return

    dfs = []
    for f in files:
        # Read only needed columns to save memory
        df = pd.read_csv(f, dtype={'THEMES': str, 'AVG_TONE': float, 'SQLDATE': str})
        # Filter rows where any relevant theme appears in THEMES
        mask = df['THEMES'].apply(lambda t: any(theme in parse_themes(t) for theme in RELEVANT_THEMES))
        df = df.loc[mask]
        if df.empty:
            continue
        # Group by date and compute mean tone
        daily = df.groupby('SQLDATE')['AVG_TONE'].mean().reset_index()
        daily.rename(columns={'AVG_TONE': 'sentiment_avg_tone'}, inplace=True)
        dfs.append(daily)

    if not dfs:
        print("No rows matched the relevant themes.")
        return

    result = pd.concat(dfs).groupby('SQLDATE', as_index=False).mean()
    # Convert SQLDATE to proper date
    result['date'] = pd.to_datetime(result['SQLDATE'], format='%Y%m%d')
    result = result[['date', 'sentiment_avg_tone']].sort_values('date')

    out_path = os.path.join(OUT_DIR, 'gdelt_rus_real_estate_sentiment_daily.csv')
    result.to_csv(out_path, index=False)
    print(f"Saved daily sentiment series to {out_path}")
    print(f"Number of days: {len(result)}")
    if len(result) > 0:
        print("First few rows:")
        print(result.head())

if __name__ == '__main__':
    main()
