#!/usr/bin/env python3
"""Полная загрузка: все снимки 7 форм ФНС (по ~187 CSV) + structure-справочники. Возобновляемый."""
import re, ssl, urllib.request, json, csv, io, os, time

ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0'}
def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=120, context=ctx) as r:
                return r.read()
        except Exception as e:
            if i == tries - 1: raise
            time.sleep(3 * (i + 1))

BASE = '/home/lnr/research-wiki/raw/fns'
os.makedirs(BASE, exist_ok=True)
scan = {x['code']: x for x in json.load(open('/tmp/fns_scan.json'))}
WANT = ['profitorg', 'taxagent', 'usn', 'assetorg', '1nds', 'ttorg', '1nom', 'poved']
done = fail = 0
for code in WANT:
    d_hits = re.search(r'data-(\d{8})', code)  # placeholder
    idx = scan[code]['idx']
    n = scan[code]['n_snapshots']
    # карточка уже просканирована — нужен полный список ссылок; перечитываем её
    page = get(f'https://www.nalog.gov.ru/opendata/7707329152-{code}/').decode('utf-8', 'replace')
    links = sorted(set(re.findall(r'href="(https://data\.nalog\.ru/opendata/7707329152-' + code + r'/data-[^"]+\.csv)"', page)))
    ok = 0
    for u in links:
        m = re.search(r'data-(\d{8})', u)
        if not m: continue
        local = f'{BASE}/{code}_{m.group(1)}.csv'
        if os.path.exists(local) and os.path.getsize(local) > 100:
            ok += 1; continue
        try:
            raw = get(u)
            open(local, 'wb').write(raw)
            ok += 1
        except Exception as e:
            fail += 1
            print('FAIL', u[-40:], e)
        time.sleep(0.4)
    # structure последней версии
    s_links = sorted(set(re.findall(r'href="(https://data\.nalog\.ru/opendata/7707329152-' + code + r'/structure-[^"]+\.csv)"', page)))
    if s_links:
        u = s_links[-1]
        local = f'{BASE}/{code}_structure.csv'
        if not os.path.exists(local):
            try:
                open(local, 'wb').write(get(u))
            except Exception as e:
                print('STRUCTURE FAIL', code, e)
    print(f"{idx:9s} {code:12s} {ok}/{len(links)} файлов")
    done += ok
print(f'\nитого: {done} файлов, ошибок {fail}')