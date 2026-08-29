#!/usr/bin/env python3
import os
import sys
import requests
import zipfile
import io
import csv
import re
from datetime import datetime, timezone, timedelta

# Configuration
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../data/raw/gdelt')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# GDELT base URL
BASE_URL = "http://data.gdeltproject.org/gdeltv2"

def get_latest_export_url():
    """Fetch lastupdate.txt and extract the most recent export file URL."""
    lastupdate_url = f"{BASE_URL}/lastupdate.txt"
    print(f"Fetching {lastupdate_url}")
    try:
        resp = requests.get(lastupdate_url, timeout=10)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to download {lastupdate_url}: {e}", file=sys.stderr)
        return None

    # Parse lines: each line is <size> <hash> <URL>
    # We want the line with .export.CSV.zip
    for line in resp.text.strip().split('\n'):
        if '.export.CSV.zip' in line:
            parts = line.split()
            if len(parts) >= 3:
                url = parts[2]
                print(f"Found export file: {url}")
                return url
    print("No export file found in lastupdate.txt", file=sys.stderr)
    return None

def download_and_process(url):
    """Download the zip file from URL, extract CSV, filter for RUS, and save."""
    print(f"Downloading {url}")
    try:
        resp = requests.get(url, stream=True, timeout=60)
        resp.raise_for_status()
    except Exception as e:
        print(f"Failed to download {url}: {e}", file=sys.stderr)
        return False

    # Load zip in memory
    try:
        z = zipfile.ZipFile(io.BytesIO(resp.content))
    except zipfile.BadZipFile as e:
        print(f"Downloaded content is not a valid zip file: {e}", file=sys.stderr)
        return False

    # Assume there is a single CSV file inside (the same basename as the zip but without .zip)
    zip_basename = os.path.basename(url)
    csv_name = zip_basename.replace('.zip', '')
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

    # Extract date from the filename for output naming
    # Expected format: YYYYMMDDHHMMSS.export.CSV
    match = re.search(r'(\d{8})', csv_name)
    date_str = match.group(1) if match else 'unknown'
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
        print(f"Finished. Total rows processed: {row_count}, kept: {kept_count}")

    return True

def main():
    # Try to get the latest export file from lastupdate.txt
    url = get_latest_export_url()
    if url is None:
        print("Falling back to trying daily files for the last 3 days", file=sys.stderr)
        # Fallback to original method: try yesterday, day before, today
        today = datetime.now(timezone.utc)
        for days_back in [1, 2, 0]:
            target_date = today - timedelta(days=days_back)
            date_str = target_date.strftime('%Y%m%d')
            zip_name = f"{date_str}export.csv.zip"
            url = f"{BASE_URL}/{zip_name}"
            print(f"Trying {url}")
            try:
                resp = requests.get(url, stream=True, timeout=60)
                if resp.status_code == 200:
                    break
            except Exception:
                continue
        else:
            print("Failed to download GDELT data for the last 3 days", file=sys.stderr)
            sys.exit(1)

    # Download and process the file
    if not download_and_process(url):
        sys.exit(1)

if __name__ == '__main__':
    main()
