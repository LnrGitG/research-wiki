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

def download_daily(date_str):
    """Try to download the daily file for the given date (YYYYMMDD)."""
    zip_name = f"{date_str}export.csv.zip"
    url = f"{BASE_URL}/{zip_name}"
    print(f"Trying daily file: {url}")
    try:
        resp = requests.get(url, stream=True, timeout=60)
        if resp.status_code == 200:
            return resp.content
        else:
            print(f"  -> HTTP {resp.status_code}")
            return None
    except Exception as e:
        print(f"  -> Error: {e}")
        return None

def download_hourly(date_str, hour, minute):
    """Try to download an hourly file for the given date and time."""
    # Format: YYYYMMDDHHMMSS.export.CSV.zip
    filename = f"{date_str}{hour:02d}{minute:02d}00.export.CSV.zip"
    url = f"{BASE_URL}/{filename}"
    # print(f"  Trying hourly: {url}")  # Too verbose
    try:
        resp = requests.get(url, stream=True, timeout=30)
        if resp.status_code == 200:
            return resp.content
        else:
            # Uncomment the next line for debugging
            # print(f"    -> HTTP {resp.status_code}")
            return None
    except Exception as e:
        # Uncomment the next line for debugging
        # print(f"    -> Error: {e}")
        return None

def process_zip_content(content, date_str, out_file):
    """Process the zip content, extract CSV, filter for RUS, and write to out_file."""
    try:
        z = zipfile.ZipFile(io.BytesIO(content))
    except zipfile.BadZipFile as e:
        print(f"  -> Bad zip file: {e}")
        return 0, 0  # rows, kept

    # Assume there is a single CSV file inside (the same basename as the zip but without .zip)
    # We don't know the exact name inside, so we take the first file.
    csv_name = z.namelist()[0]
    # print(f"    Extracting {csv_name} from zip...")

    # Indices we keep (based on GDELT 2.0 format)
    keep_indices = [0,1,5,6,7,15,16,17,25,27,28,29,30,31,32,33,34,50,51,52,53,54,55,56,57]
    header = [
        'GLOBALEVENTID','SQLDATE','Actor1Code','Actor1Name','Actor1CountryCode',
        'Actor2Code','Actor2Name','Actor2CountryCode','IsRootEvent','EventBaseCode','EventRootCode',
        'QuadClass','GoldsteinScale','NumMentions','NumSources','NumArticles','AvgTone',
        'ActionGeo_FullName','ActionGeo_CountryCode','ActionGeo_ADM1Code','ActionGeo_Lat',
        'ActionGeo_Long','ActionGeo_FeatureID','DATEADDED','SOURCEURL'
    ]

    # We'll write the header only once, so we need to know if we are at the first file.
    # We'll pass a flag to write_header, but for simplicity, we'll write the header outside.
    # Instead, we'll return the rows and let the caller write? Let's change: we'll write inside.

    # Actually, we'll let the caller handle the header. We'll just return the rows to write.
    # But we want to avoid holding all rows in memory. We'll write directly to the given out_file.

    # We'll change the function to take an already opened output file and write to it.
    # However, we are already passing the out_file (opened in the caller). Let's adjust.

    # We'll rewrite: the function will take the content and the output file handle (already opened for appending).
    # But we need to write the header only once. We'll handle that in the caller.

    # Let's change the function signature to process_zip_content(content, out_file) and assume the header is already written.
    # We'll move the header writing to the caller.

    # We'll do: the caller opens the file, writes the header, then calls this function for each piece.

    # So we remove the header writing from here.

    # Indices we keep (based on GDELT 2.0 format)
    keep_indices = [0,1,5,6,7,15,16,17,25,27,28,29,30,31,32,33,34,50,51,52,53,54,55,56,57]

    with z.open(csv_name) as csv_file, out_file:
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
    return row_count, kept_count

def main():
    # Determine date for yesterday (GDELT files for current day may be incomplete)
    today = datetime.now(timezone.utc)
    target_date = today - timedelta(days=1)
    date_str = target_date.strftime('%Y%m%d')
    print(f"Processing GDELT data for {date_str}")

    out_filename = os.path.join(OUTPUT_DIR, f"gdelt_rus_{date_str}.csv")
    print(f"Writing filtered data to {out_filename}")

    total_rows = 0
    total_kept = 0

    # First, try the daily file
    content = download_daily(date_str)
    if content is not None:
        # Process the daily file
        with open(out_filename, 'w', newline='', encoding='utf-8') as out_file:
            # Write header
            writer = csv.writer(out_file)
            writer.writerow([
                'GLOBALEVENTID','SQLDATE','Actor1Code','Actor1Name','Actor1CountryCode',
                'Actor2Code','Actor2Name','Actor2CountryCode','IsRootEvent','EventBaseCode','EventRootCode',
                'QuadClass','GoldsteinScale','NumMentions','NumSources','NumArticles','AvgTone',
                'ActionGeo_FullName','ActionGeo_CountryCode','ActionGeo_ADM1Code','ActionGeo_Lat',
                'ActionGeo_Long','ActionGeo_FeatureID','DATEADDED','SOURCEURL'
            ])
            rows, kept = process_zip_content(content, date_str, out_file)
            total_rows += rows
            total_kept += kept
        print(f"Processed daily file: {total_rows} rows, {total_kept} kept")
    else:
        print("Daily file not found, trying hourly files...")
        # If daily file fails, try to get all hourly files for the day
        with open(out_filename, 'w', newline='', encoding='utf-8') as out_file:
            # Write header
            writer = csv.writer(out_file)
            writer.writerow([
                'GLOBALEVENTID','SQLDATE','Actor1Code','Actor1Name','Actor1CountryCode',
                'Actor2Code','Actor2Name','Actor2CountryCode','IsRootEvent','EventBaseCode','EventRootCode',
                'QuadClass','GoldsteinScale','NumMentions','NumSources','NumArticles','AvgTone',
                'ActionGeo_FullName','ActionGeo_CountryCode','ActionGeo_ADM1Code','ActionGeo_Lat',
                'ActionGeo_Long','ActionGeo_FeatureID','DATEADDED','SOURCEURL'
            ])

            files_processed = 0
            # Iterate over each 15-minute interval of the day
            for hour in range(24):
                for minute in [0, 15, 30, 45]:
                    content = download_hourly(date_str, hour, minute)
                    if content is None:
                        continue
                    files_processed += 1
                    rows, kept = process_zip_content(content, date_str, out_file)
                    total_rows += rows
                    total_kept += kept
                    if files_processed % 10 == 0:
                        print(f"  Processed {files_processed} files, {total_rows} rows, {total_kept} kept")

            print(f"Finished processing {files_processed} hourly files.")

    print(f"Total rows processed: {total_rows}, kept: {total_kept}")

    if total_rows == 0:
        print("No data processed for the day.", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
