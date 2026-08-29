#!/usr/bin/env python3
import os
import sys
import requests
import zipfile
import io
import csv
from datetime import datetime, timezone, timedelta

# Configuration
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../data/raw/gdelt')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# GDELT base URL
BASE_URL = "http://data.gdeltproject.org/gdeltv2"

def fetch_for_date(date_str):
    zip_name = f"{date_str}export.csv.zip"
    url = f"{BASE_URL}/{zip_name}"
    print(f"Fetching GDELT data for {date_str} from {url}")
    try:
        resp = requests.get(url, stream=True, timeout=60)
        resp.raise_for_status()
        return resp.content
    except Exception as e:
        print(f"Failed to download {url}: {e}", file=sys.stderr)
        return None

def main():
    # Determine date for yesterday (GDELT files for current day may be incomplete)
    today = datetime.now(timezone.utc)
    # Try yesterday, then the day before, then today (up to 3 days)
    for days_back in [1, 2, 0]:
        target_date = today - timedelta(days=days_back)
        date_str = target_date.strftime('%Y%m%d')
        content = fetch_for_date(date_str)
        if content is not None:
            break
    else:
        print("Failed to download GDELT data for the last 3 days", file=sys.stderr)
        sys.exit(1)

    # Load zip in memory
    try:
        z = zipfile.ZipFile(io.BytesIO(content))
    except zipfile.BadZipFile as e:
        print(f"Downloaded content is not a valid zip file: {e}", file=sys.stderr)
        sys.exit(1)

    # Assume there is a single CSV file inside named {date_str}export.csv
    csv_name = f"{date_str}export.csv"
    if csv_name not in z.namelist():
        # fallback: first file
        csv_name = z.namelist()[0]
    print(f"Extracting {csv_name} from zip...")

    # Indices we keep (based on GDELT 2.0 format)
    keep_indices = [0,1,5,6,7,15,16,17,25,27,28,29,30,31,32,33,34,50,51,52,53,54,55,56,57]
    header = [
        'GLOBALEVENTID','SQLDATE','Actor1Code','Actor1Name','Actor1CountryCode',
        'Actor2Code','Actor2Name','Actor2CountryCode','IsRootEvent','EventBaseCode','EventRootCode',
        'QuadClass','GoldsteinScale','NumMentions','NumSources','NumArticles','AvgTone',
        'ActionGeo_FullName','ActionGeo_CountryCode','ActionGeo_ADM1Code','ActionGeo_Lat',
        'ActionGeo_Long','ActionGeo_FeatureID','DATEADDED','SOURCEURL'
    ]

    out_filename = os.path.join(OUTPUT_DIR, f"gdelt_rus_{date_str}.csv")
    print(f"Writing filtered data to {out_filename}")
    with z.open(csv_name) as csv_file, open(out_filename, 'w', newline='', encoding='utf-8') as out_file:
        text_wrapper = io.TextIOWrapper(csv_file, encoding='utf-8')
        reader = csv.reader(text_wrapper)
        writer = csv.writer(out_file)
        writer.writerow(header)
        row_count = 0
        kept_count = 0
        for row in reader:
            row_count += 1
            # Ensure row has enough columns
            if len(row) > max(7,17,51):
                if row[7] == 'RUS' or row[17] == 'RUS' or row[51] == 'RUS':
                    kept_row = [row[i] for i in keep_indices]
                    writer.writerow(kept_row)
                    kept_count += 1
            if row_count % 200000 == 0:
                print(f"Processed {row_count} rows, kept {kept_count}")
        print(f"Finished. Total rows processed: {row_count}, kept: {kept_count}")

if __name__ == '__main__':
    main()
