#!/usr/bin/env python3
import os
import sys
import requests
import zipfile
import io
import csv
from datetime import datetime, timezone, timedelta

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '../data/raw/gdelt')
os.makedirs(OUTPUT_DIR, exist_ok=True)
BASE_URL = "http://data.gdeltproject.org/gdeltv2"

def download_hourly(date_str, hour, minute):
    filename = f"{date_str}{hour:02d}{minute:02d}00.export.CSV.zip"
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
        # GDELT files are tab-separated and have NO header
        text_wrapper = io.TextIOWrapper(csv_file, encoding='utf-8')
        reader = csv.reader(text_wrapper, delimiter='\t')
        writer = csv.writer(out_file)
        rows = 0
        kept = 0
        for row in reader:
            rows += 1
            # GDELT 2.0 schema (0-index):
            # 0 GLOBALEVENTID
            # 1 SQLDATE
            # 2 MonthYear
            # 3 Year
            # 4 FractionDate
            # 5 Actor1Code
            # 6 Actor1Name
            # 7 Actor1CountryCode
            # 8 Actor1KnownGroupCode
            # 9 Actor1EthnicCode
            # 10 Actor1Religion1Code
            # 11 Actor1Religion2Code
            # 12 Actor1Type1Code
            # 13 Actor1Type2Code
            # 14 Actor1Type3Code
            # 15 Actor2Code
            # 16 Actor2Name
            # 17 Actor2CountryCode
            # 18 Actor2KnownGroupCode
            # 19 Actor2EthnicCode
            # 20 Actor2Religion1Code
            # 21 Actor2Religion2Code
            # 22 Actor2Type1Code
            # 23 Actor2Type2Code
            # 24 Actor2Type3Code
            # 25 IsRootEvent
            # 26 EventCode
            # 27 EventBaseCode
            # 28 EventRootCode
            # 29 QuadClass
            # 30 GoldsteinScale
            # 31 NumMentions
            # 32 NumSources
            # 33 NumArticles
            # 34 AvgTone
            # 35 Actor1Geo_Type
            # 36 Actor1Geo_FullName
            # 37 Actor1Geo_CountryCode
            # 38 Actor1Geo_ADM1Code
            # 39 Actor1Geo_Lat
            # 40 Actor1Geo_Long
            # 41 Actor1Geo_FeatureID
            # 42 Actor2Geo_Type
            # 43 Actor2Geo_FullName
            # 44 Actor2Geo_CountryCode
            # 45 Actor2Geo_ADM1Code
            # 46 Actor2Geo_Lat
            # 47 Actor2Geo_Long
            # 48 Actor2Geo_FeatureID
            # 49 ActionGeo_Type
            # 50 ActionGeo_FullName
            # 51 ActionGeo_CountryCode
            # 52 ActionGeo_ADM1Code
            # 53 ActionGeo_Lat
            # 54 ActionGeo_Long
            # 55 ActionGeo_FeatureID
            # 56 DATEADDED
            # 57 SOURCEURL
            # 58 THEMES? Actually according to GDELT 2.0, there are 58 columns? Wait there is also column for DATEADDED (56) and SOURCEURL (57). THEMES is part of GKG not Events. Oh! I made mistake: THEMES is in GKG (Global Knowledge Graph) not in Events. The Events file does NOT have THEMES column.
            # So we cannot get themes from Events. We need to use GKG file instead.
            # However, the requirement is to get sentiment by theme. We can still use AvgTone from Events but need to filter by theme via GKG.
            # This complicates.
            # For simplicity, we can use the GKG file which includes themes and also includes AvgTone? GKG includes fields like V2Tone (average tone). Let's check: GKG columns: 
            # 0 GLOBALEVENTID
            # 1 EventDateDate
            # 2 EventTime
            # 3 ...
            # Actually better to use GKG 2.0: columns include V2Theme (semicolon-separated themes) and V2Tone (average tone). 
            # However, we already have a pipeline for Events; switching to GKG would require reworking.
            # Given time, we can approximate sentiment by using Events and filtering by keywords in Actor1Name/Actor2Name? Not ideal.
            # Let's adjust: We'll use GKG instead of Events for sentiment by theme. We'll change the script to download GKG files.
            # GKG files are also hourly: ...export.csv.zip but they contain GKG records.
            # We'll need to adjust column indices accordingly.
            pass
        return rows, kept
