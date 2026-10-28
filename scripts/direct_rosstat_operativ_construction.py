#!/usr/bin/env python3
"""Load Rosstat operational construction work (YTD cumulative snapshots) to canonical DB.
Source: raw/rosstat/data/Operativ_09_2026.xlsx, sheet 1.
Dry-run by default; set APPLY=1 to write. Rows retain YTD semantics in sub_dimension.
"""
import os, re, sys
from pathlib import Path
import openpyxl
sys.path.insert(0, str(Path(__file__).resolve().parent))
from direct_core import Writer
from db_tunnel import query

REPO = Path(__file__).resolve().parent.parent
FILE = REPO / 'raw/rosstat/data/Operativ_09_2026.xlsx'
METRIC = 'Объем работ по виду деятельности «Строительство», накопительным итогом с начала года, млн руб.'
RELEASE = 'Росстат Operativ_09.xlsx, обновлено 2026-10-28'

ALIASES = {
    'Российская Федерация': 'Российская Федерация',
    'г. Москва': 'Москва', 'г. Санкт-Петербург': 'Санкт-Петербург', 'г. Севастополь': 'Севастополь',
    'Республика Северная Осетия - Алания': 'Республика Северная Осетия — Алания',
    'Еврейская авт. область': 'Еврейская автономная область',
    'Чукотский авт. округ': 'Чукотский автономный округ',
    'Кемеровская область': 'Кемеровская область — Кузбасс',
    'Краснодарский край (с учетом ФТ "Сириус")': 'Краснодарский край',
    'Архангельская область': 'Архангельская область (с НАО)',
    'Архангельская область без авт. округа': 'Архангельская область (без НАО)',
    'Ненецкий авт. округ': 'Ненецкий автономный округ',
    'Тюменская область': 'Тюменская область (с ХМАО и ЯНАО)',
    'Тюменская область без авт. округов': 'Тюменская область (без ХМАО и ЯНАО)',
    'Ханты-Мансийский авт. округ': 'Ханты-Мансийский автономный округ — Югра',
    'Ямало-Ненецкий авт. округ': 'Ямало-Ненецкий автономный округ',
}
# Rows with explicit "with AO included" territorial scope are published alongside
# their component regions. The source file's notation encodes scope, so keep it.
ALIAS_REGION_IDS = {
    'Архангельская область': 199,
    'Архангельская область без авт. округа': 30,
    'Тюменская область': 200,
    'Тюменская область без авт. округов': 70,
}
SKIP = {'А','Центральный федеральный округ','Северо-Западный федеральный округ','Южный федеральный округ',
        'Северо-Кавказский федеральный округ','Приволжский федеральный округ','Уральский федеральный округ',
        'Сибирский федеральный округ','Дальневосточный федеральный округ'}

def norm(s): return re.sub(r'\s+', ' ', str(s or '')).strip()

def build():
    if not FILE.exists(): raise FileNotFoundError(FILE)
    wb=openpyxl.load_workbook(FILE,read_only=True,data_only=True); ws=wb['1']
    regions={r[0]:int(r[1]) for r in query('SELECT name_ru,region_id FROM catalog.region WHERE is_active')}
    if not regions: raise RuntimeError('catalog.region returned no active regions')
    rows=[]; unmatched=[]; skipped=[]; row_names=set()
    for row in ws.iter_rows(values_only=True):
        if not row or not isinstance(row[0],str): continue
        raw=norm(row[0]); raw=re.sub(r'\d+\)$','',raw).strip()
        if raw.startswith('в том числе: '): raw=norm(raw.replace('в том числе: ', '', 1))
        if raw in SKIP or raw.endswith(':'): continue
        row_names.add(raw)
        for month in range(1,10):
            if month >= len(row) or not isinstance(row[month],(int,float)): continue
            name=ALIASES.get(raw,raw)
            if raw in ALIAS_REGION_IDS: rid=ALIAS_REGION_IDS[raw]
            else:
                if name not in regions:
                    unmatched.append(raw); continue
                rid=regions[name]
            if rid == regions.get('Российская Федерация'):
                skipped.append(raw); continue
            rows.append(dict(metric_name=METRIC,value=float(row[month]),ps=(2026,month),region=rid,
                sub='накопительно: январь–%s' % ('январь февраль март апрель май июнь июль август сентябрь'.split()[month-1]),
                freq='M',source='rosstat',release=RELEASE,unit='mln_rub'))
    wb.close()
    if unmatched: raise RuntimeError('Unmapped source rows: '+repr(sorted(set(unmatched))))
    keys=[(r['region'],r['ps']) for r in rows]
    if len(keys)!=len(set(keys)): raise RuntimeError('Duplicate region-month keys; refusing to ingest')
    if not rows: raise RuntimeError('No observations parsed')
    expected={'Архангельская область','Ненецкий авт. округ','Архангельская область без авт. округа',
              'Тюменская область','Ханты-Мансийский авт. округ','Ямало-Ненецкий авт. округ',
              'Тюменская область без авт. округов'}
    if not expected.issubset(row_names): raise RuntimeError('Expected territorial breakdown rows missing')
    months=sorted({r['ps'][1] for r in rows})
    print('source=',FILE.name,'rows=',len(rows),'regions=',len({r['region'] for r in rows}),'months=',months)
    print('unmapped=0; federal_districts_skipped=8; national_total_skipped=1; territorial variants retained')
    print('sample=',[(r['region'],r['ps'],r['value']) for r in rows if r['region']==regions.get('Республика Башкортостан')][-2:])
    return rows

if __name__=='__main__':
    w=Writer(tag='rosstat_operativ_construction',simulate=os.environ.get('APPLY')!='1')
    try:
        recs=build()
        out=w.ingest(recs,group='rosstat_operativ_construction',prune=False)
        print('prepared=%d inserted=%d conflicts=%d new_metrics=%d' % out)
        if os.environ.get('APPLY')!='1': print('DRY RUN; set APPLY=1 to write')
    finally: w.close()
