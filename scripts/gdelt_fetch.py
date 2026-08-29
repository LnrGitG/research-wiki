#!/usr/bin/env python3
import os
import sys
import requests
import zipfile
import io
import csv
from datetime import datetime, timezone, timedelta

# Increase CSV field size limit to handle large fields
csv.field_size_limit(sys.maxsize)

def is_rus_present(line):
    """Return True if line contains the standalone word RUS (case-insensitive)."""
    line_upper = line.upper()
    i = 0
    while i < len(line_upper) - 2:
        if line_upper[i:i+3] == 'RUS':
            # Check before: if exists, must not be alphanumeric
            if i > 0 and line_upper[i-1].isalnum():
                i += 1
                continue
            # Check after: if exists, must not be alphanumeric
            if i+3 < len(line_upper) and line_upper[i+3].isalnum():
                i += 1
                continue
            return True
        i += 1
    return False

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../data/raw/gdelt')
os.makedirs(OUTPUT_DIR, exist_ok=True)
BASE_URL = "http://data.gdeltproject.org/gdeltv2"

def download_hourly(date_str, hour, minute):
    filename = f"{date_str}{hour:02d}{minute:02d}00.gkg.csv.zip"
    url = f"{BASE_URL}/{filename}"
    try:
        resp = requests.get(url, stream=True, timeout=30)
        if resp.status_code == 200:
            return resp.content
        else:
            return None
    except Exception:
        return None

def process_zip_content(content, out_file):
    try:
        z = zipfile.ZipFile(io.BytesIO(content))
    except zipfile.BadZipFile:
        return 0, 0
    # Assume first file in zip is the CSV
    csv_name = z.namelist()[0]
    with z.open(csv_name) as csv_file:
        # GKG files are tab-separated and have NO header
        text_wrapper = io.TextIOWrapper(csv_file, encoding='utf-8', errors='replace')
        reader = csv.reader(text_wrapper, delimiter='\t')
        writer = csv.writer(out_file)
        rows = 0
        kept = 0
        for row in reader:
            rows += 1
            # Join fields with a marker to search for RUS country code pattern
            line = "\t".join(row)
            # Check for patterns indicating Russia: look for standalone 'RUS' (case-insensitive)
            if is_rus_present(line):
                # Extract needed fields:
                # Field0: GLOBALEVENTID
                # Field1: SQLDATE (YYYYMMDD)
                # Field7: THEMES (semicolon-separated)
                # Field15: TONE_METRICS (comma-separated numbers, first is AvgTone)
                if len(row) > 15:
                    glob_event_id = row[0]
                    sql_date = row[1]  # YYYYMMDD
                    themes = row[7] if len(row) > 7 else ''
                    tone_metrics = row[15] if len(row) > 15 else ''
                    # Extract first number from tone_metrics as AvgTone
                    avg_tone = ''
                    if tone_metrics:
                        # Split by comma, take first part
                        parts = tone_metrics.split(',')
                        if parts:
                            avg_tone = parts[0].strip()
                    # Write output
                    writer.writerow([glob_event_id, sql_date, themes, avg_tone])
                    kept += 1
        return rows, kept

def main():
    today = datetime.now(timezone.utc)
    target_date = today - timedelta(days=1)
    date_str = target_date.strftime('%Y%m%d')
    print(f"Processing GDELT GKG data for {date_str}")

    out_filename = os.path.join(OUTPUT_DIR, f"gdelt_gkg_rus_{date_str}.csv")
    print(f"Writing filtered data to {out_filename}")

    total_rows = 0
    total_kept = 0
    files_processed = 0

    with open(out_filename, 'w', newline='', encoding='utf-8') as out_file:
        # Write header
        writer = csv.writer(out_file)
        writer.writerow(['GLOBALEVENTID', 'SQLDATE', 'THEMES', 'AVG_TONE'])

        # Iterate over each 15-minute interval of the day
        for hour in range(24):
            for minute in [0, 15, 30, 45]:
                content = download_hourly(date_str, hour, minute)
                if content is None:
                    continue
                files_processed += 1
                rows, kept = process_zip_content(content, out_file)
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
