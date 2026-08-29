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

def fetch_hourly_file(date_str, hour, minute):
    # Format: YYYYMMDDHHMMSS.export.CSV.zip
    # Seconds are always 00 in the filenames we see
    filename = f"{date_str}{hour:02d}{minute:02d}00.export.CSV.zip"
    url = f"{BASE_URL}/{filename}"
    print(f"Fetching {url}")
    try:
        resp = requests.get(url, stream=True, timeout=30)
        if resp.status_code == 200:
            return resp.content
        else:
            print(f"  -> HTTP {resp.status_code}")
            return None
    except Exception as e:
        print(f"  -> Error: {e}")
        return None

def main():
    # Determine date for yesterday (GDELT files for current day may be incomplete)
    today = datetime.now(timezone.utc)
    target_date = today - timedelta(days=1)
    date_str = target_date.strftime('%Y%m%d')
    print(f"Processing GDELT data for {date_str}")

    out_filename = os.path.join(OUTPUT_DIR, f"gdelt_rus_{date_str}.csv")
    print(f"Writing filtered data to {out_filename}")

    # Indices we keep (based on GDELT 2.0 format)
    keep_indices = [0,1,5,6,7,15,16,17,25,27,28,29,30,31,32,33,34,50,51,52,53,54,55,56,57]
    header = [
        'GLOBALEVENTID','SQLDATE','Actor1Code','Actor1Name','Actor1CountryCode',
        'Actor2Code','Actor2Name','Actor2CountryCode','IsRootEvent','EventBaseCode','EventRootCode',
        'QuadClass','GoldsteinScale','NumMentions','NumSources','NumArticles','AvgTone',
        'ActionGeo_FullName','ActionGeo_CountryCode','ActionGeo_ADM1Code','ActionGeo_Lat',
        'ActionGeo_Long','ActionGeo_FeatureID','DATEADDED','SOURCEURL'
    ]

    total_rows = 0
    total_kept = 0
    files_processed = 0

    # Write header
    with open(out_filename, 'w', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(header)

        # Iterate over each 15-minute interval of the day
        for hour in range(24):
            for minute in [0, 15, 30, 45]:
                content = fetch_hourly_file(date_str, hour, minute)
                if content is None:
                    continue

                files_processed += 1
                try:
                    z = zipfile.ZipFile(io.BytesIO(content))
                except zipfile.BadZipFile as e:
                    print(f"  -> Bad zip file: {e}")
                    continue

                # Assume there is a single CSV file inside named {date_str}{HHMM}00.export.CSV
                csv_name = f"{date_str}{hour:02d}{minute:02d}00.export.CSV"
                if csv_name not in z.namelist():
                    # fallback: first file
                    csv_name = z.namelist()[0]
                print(f"  -> Extracting {csv_name} from zip...")

                with z.open(csv_name) as csv_file, open(out_filename, 'a', newline='', encoding='utf-8') as out_file:
                    text_wrapper = io.TextIOWrapper(csv_file, encoding='utf-8')
                    reader = csv.reader(text_wrapper)
                    writer = csv.writer(out_file)
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
                    total_rows += row_count
                    total_kept += kept_count
                    print(f"     Processed {row_count} rows, kept {kept_count}")

    print(f"Finished. Files processed: {files_processed}")
    print(f"Total rows processed: {total_rows}, kept: {total_kept}")

    if files_processed == 0:
        print("No files processed for the day.", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
