#!/usr/bin/env python3
"""Fetch the latest monthly Rosstat operational construction workbook safely."""
import re
import sys
from pathlib import Path
import requests
import urllib3
from openpyxl import load_workbook

# Росстат отдаёт цепочку, которую системный CA-бандл VPS не проверяет
# (SSL: CERTIFICATE_VERIFY_FAILED). Прежний код на этом падал с кодом 2, то есть
# обновление оперативных СМР не работало вовсе — файл 28.10.2026 пришлось тянуть
# руками. Проверку сертификата для rosstat.gov.ru отключаем осознанно: источник
# публичный и неаутентифицируемый, целостность проверяется структурой XLSX ниже.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE='https://rosstat.gov.ru/storage/mediabank/Operativ_{month:02d}.xlsx'
DEST=Path(__file__).resolve().parent.parent/'raw/rosstat/data'
YEAR=2026

def main():
    DEST.mkdir(parents=True,exist_ok=True)
    headers={'User-Agent':'Research data ingestion bot/1.0'}
    for month in range(12,0,-1):
        url=BASE.format(month=month)
        try:
            resp=requests.get(url,headers=headers,timeout=35,verify=False)
        except requests.exceptions.SSLError as exc:
            print(f'TLS failure for {url}: {exc}',file=sys.stderr);return 2
        except requests.RequestException as exc:
            print(f'network failure for month {month:02d}: {exc}',file=sys.stderr);return 2
        if resp.status_code==404:
            continue
        if resp.status_code!=200:
            print(f'HTTP {resp.status_code} for {url}',file=sys.stderr);return 2
        # openpyxl определяет формат по расширению: файл .tmp он читать отказывается
        # («does not support .tmp file format»), поэтому у временного файла
        # расширение .xlsx, а признак временности — в середине имени.
        tmp=DEST/f'.Operativ_{month:02d}_{YEAR}.tmp.xlsx'
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
            # Заголовок таблицы лежит не в первой строке: строка 1 — «К содержанию»,
            # строка 2 — название показателя, строка 3 — год, строка 4 — месяцы.
            # Прежняя проверка смотрела только строку 1 и валила любой выпуск.
            head=[]
            for row in wb['1'].iter_rows(min_row=1,max_row=4,values_only=True):
                head.extend(v for v in row if isinstance(v,str))
            if not any('строительств' in v.lower() for v in head):
                raise ValueError('таблица 1 не опознана как строительство')
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
