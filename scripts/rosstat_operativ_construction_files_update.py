#!/usr/bin/env python3
"""Fetch the latest monthly Rosstat operational construction workbook safely."""
import re
import sys
from pathlib import Path
import requests
from openpyxl import load_workbook

BASE='https://rosstat.gov.ru/storage/mediabank/Operativ_{month:02d}.xlsx'
DEST=Path(__file__).resolve().parent.parent/'raw/rosstat/data'
YEAR=2026

def main():
    DEST.mkdir(parents=True,exist_ok=True)
    headers={'User-Agent':'Research data ingestion bot/1.0'}
    for month in range(12,0,-1):
        url=BASE.format(month=month)
        try:
            resp=requests.get(url,headers=headers,timeout=35)
        except requests.exceptions.SSLError as exc:
            print(f'TLS verification failed for {url}; no insecure retry: {exc}',file=sys.stderr);return 2
        except requests.RequestException as exc:
            print(f'network failure for month {month:02d}: {exc}',file=sys.stderr);return 2
        if resp.status_code==404:
            continue
        if resp.status_code!=200:
            print(f'HTTP {resp.status_code} for {url}',file=sys.stderr);return 2
        tmp=DEST/f'.Operativ_{month:02d}_{YEAR}.xlsx.tmp'
        final=DEST/f'Operativ_{month:02d}_{YEAR}.xlsx'
        try:
            tmp.write_bytes(resp.content)
            wb=load_workbook(tmp,read_only=True,data_only=True)
            if 'Содержание' not in wb.sheetnames or '1' not in wb.sheetnames:
                raise ValueError(f'unexpected sheets: {wb.sheetnames}')
            updated=None
            for row in wb['Содержание'].iter_rows(values_only=True):
                for value in row:
                    if isinstance(value,str) and 'Обновлено:' in value:
                        updated=value.strip()
                        break
                if updated: break
            if not updated or not re.search(r'\b2026\b',updated):
                raise ValueError(f'missing/incorrect source update stamp: {updated!r}')
            rows=wb['1'].iter_rows(min_row=1,max_row=1,values_only=True)
            header=next(rows,None)
            if not header or not any(isinstance(v,str) and 'строительств' in v.lower() for v in header):
                raise ValueError('table 1 header does not identify construction')
            wb.close()
            tmp.replace(final)
            print(f'published={final.name}; source_update={updated}; bytes={final.stat().st_size}')
            return 0
        except Exception as exc:
            try: tmp.unlink(missing_ok=True)
            except OSError: pass
            print(f'validation failed for {url}: {exc}',file=sys.stderr);return 3
    print('No published operational construction workbook found for 2026',file=sys.stderr)
    return 4

if __name__=='__main__': raise SystemExit(main())
