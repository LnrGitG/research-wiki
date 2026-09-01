#!/usr/bin/env python3
"""Regional inflation-expectations Wordstat collection (Lyziak et al. 2022 replication).

Phrases: 6 inflation/price-attention phrases + 3 housing-expectation phrases,
collected PER_SUBJECT (Wordstat region ids, ~85 RU subjects).
Monthly 2018-01..2026-08. Output: data/wordstat_infl_exp_regions.csv
(date, subject_id, subject_name, phrase, group, count, share).
"""
import sys, os, csv, time
sys.path.insert(0, '/home/lnr/research-wiki/scripts')
os.chdir('/home/lnr/research-wiki')
from wordstat_api import dynamics

PHRASES = [
    ("инфляция", "G_infl"),
    ("подорожание", "G_infl"),
    ("рост цен", "G_infl"),
    ("цены выросли", "G_infl"),
    ("продукты подорожали", "G_food"),
    ("стоимость продуктов", "G_food"),
    ("цены на квартиры", "G_housing"),
    ("квартиры подорожают", "G_housing"),
    ("стоит ли покупать квартиру", "G_housing"),
]

# Wordstat region ids: 11053 = Federal districts, 11054 = states (subjects), 11124 = cities
# Fetch subject list from API? API has no list endpoint; use standard Wordstat geo-table (subjects).
# Subject ids 11124+ are cities; states (regions/subjects) ids come from Yandex geo reference.
# We discover them dynamically: try ids and check non-empty results is wasteful (85*9 calls).
# Instead: fetch federal district data is coarse; use the known Yandex Wordstat subject table.
SUBJECTS_FILE = 'data/wordstat_subject_ids.csv'

def load_subjects():
    if not os.path.exists(SUBJECTS_FILE):
        raise SystemExit(f"{SUBJECTS_FILE} not found — create subject id mapping first")
    subs = []
    for row in csv.DictReader(open(SUBJECTS_FILE, encoding='utf-8')):
        subs.append((int(row['id']), row['name']))
    return subs

def main():
    subs = load_subjects()
    print(f"subjects: {len(subs)}, phrases: {len(PHRASES)}, calls: {len(subs)*len(PHRASES)}")
    rows = []
    t0 = time.time()
    n_done = 0
    for sid, sname in subs:
        for ph, grp in PHRASES:
            for attempt in range(3):
                try:
                    res = dynamics(ph, 'PERIOD_MONTHLY', '2018-01-01', '2026-08-31', regions=[sid])
                    n_done += 1
                    for r in res:
                        rows.append({'date': r['date'], 'subject_id': sid, 'subject_name': sname,
                                     'phrase': ph, 'group': grp,
                                     'count': int(r['count']), 'share': float(r['share'])})
                    break
                except Exception as e:
                    print(f"retry {attempt+1} {sid} {ph}: {str(e)[:60]}", flush=True)
                    time.sleep(5 * (attempt + 1))
            else:
                print(f"FAILED {sid} {ph}")
            if n_done % 25 == 0:
                rate = n_done / (time.time() - t0)
                print(f"[{n_done}/{len(subs)*len(PHRASES)}] {rate:.1f} calls/s, elapsed {time.time()-t0:.0f}s", flush=True)
            time.sleep(0.40)  # rate limit: 100 calls/hour → spaced burst budget
    os.makedirs('data', exist_ok=True)
    with open('data/wordstat_infl_exp_regions.csv', 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=['date', 'subject_id', 'subject_name', 'phrase', 'group', 'count', 'share'])
        w.writeheader()
        w.writerows(rows)
    print(f"DONE {len(rows)} rows in {time.time()-t0:.0f}s -> data/wordstat_infl_exp_regions.csv")

if __name__ == '__main__':
    main()