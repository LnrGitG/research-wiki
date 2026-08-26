#!/usr/bin/env python3
"""MVP step 2: build demand indices from Wordstat core + validate vs Rosreestr.
- Weekly group sums + RII (share of group in broad denominator)
- Quarterly aggregation -> lead/lag correlations vs rosreestr_deals.db
NOTE: only 10 quarterly obs of deals (2024q1-2026q2) => correlations are
exploratory, NOT inference. Full 2018-2026 index saved for future targets.
"""
import csv, sqlite3, math
from collections import defaultdict

def qof(date):  # 'YYYY-MM-DD' -> 'YYYYQn'
    y, m = int(date[:4]), int(date[5:7])
    return f"{y}Q{(m-1)//3+1}"

rows = list(csv.DictReader(open('/home/lnr/research-wiki/data/wordstat_weekly_core.csv', encoding='utf-8')))

# ---- weekly aggregation: count by phrase-date
cnt = defaultdict(int)          # (date, phrase) -> count
phr_group = {}
for r in rows:
    cnt[(r['date'], r['phrase'])] = int(r['count'])
    phr_group[r['phrase']] = r['group']

dates = sorted({d for d, _ in cnt})
groups = defaultdict(lambda: defaultdict(int))   # date -> group -> sum
for (d, ph), c in cnt.items():
    groups[d][phr_group[ph]] += c

# RII: group share among "real estate universe" = D_broad + all housing groups?
# Per concept formula: numerator group phrases, denominator ALL queries in category.
# We use D_broad (недвижимость, ипотека, купить квартиру, вторичное жильё) as proxy
# of category volume. Report both raw sums and shares.
out_w = []
for d in dates:
    g = groups[d]
    D = max(g.get('D_broad', 0), 1)
    out_w.append({
        'date': d,
        'A_invest': g.get('A_invest', 0),
        'B_rent': g.get('B_rent', 0),
        'C_panic': g.get('C_panic', 0),
        'D_broad': g.get('D_broad', 0),
        'rii_A': round(g.get('A_invest', 0) / D, 5),
        'rii_B': round(g.get('B_rent', 0) / D, 5),
        'rii_C': round(g.get('C_panic', 0) / D, 5),
    })

with open('/home/lnr/research-wiki/data/wordstat_demand_indices_weekly.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out_w[0].keys()))
    w.writeheader(); w.writerows(out_w)

# ---- quarterly
qg = defaultdict(lambda: defaultdict(int))
for d in dates:
    qq = qof(d)
    for k, v in groups[d].items():
        qg[qq][k] += v
quarters = sorted(qg)
out_q = []
for qq in quarters:
    g = qg[qq]
    D = max(g.get('D_broad', 0), 1)
    out_q.append({'quarter': qq,
                  'A_invest': g.get('A_invest', 0), 'B_rent': g.get('B_rent', 0),
                  'C_panic': g.get('C_panic', 0), 'D_broad': g.get('D_broad', 0),
                  'rii_A': round(g.get('A_invest', 0)/D, 5),
                  'rii_B': round(g.get('B_rent', 0)/D, 5),
                  'rii_C': round(g.get('C_panic', 0)/D, 5)})
with open('/home/lnr/research-wiki/data/wordstat_demand_indices_quarterly.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=list(out_q[0].keys()))
    w.writeheader(); w.writerows(out_q)

# ---- validation vs Rosreestr deals
con = sqlite3.connect('/home/lnr/research-wiki/data/rosreestr_deals.db')
deals = {f"{y}Q{q}": (n, nd) for y, q, n, nd in
         con.execute("SELECT year,q,n,ndkp FROM deals_rf_quarterly")}

def spearman(x, y):
    def rank(v):
        s = sorted(range(len(v)), key=lambda i: v[i])
        rk = [0]*len(v)
        for r, i in enumerate(s): rk[i] = r
        return rk
    rx, ry = rank(x), rank(y)
    mx, my = sum(rx)/len(rx), sum(ry)/len(ry)
    num = sum((a-mx)*(b-my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a-mx)**2 for a in rx)*sum((b-my)**2 for b in ry))
    return num/den if den else float('nan')

def pearson(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((a-mx)*(b-my) for a, b in zip(x, y))
    den = math.sqrt(sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))
    return num/den if den else float('nan')

common = [qq for qq in quarters if qq in deals]
print(f"\nOverlap quarters ({len(common)}): {common[0]}..{common[-1]}")
series = {'A_invest': [], 'B_rent': [], 'C_panic': [], 'rii_A': [], 'rii_B': []}
for lag in range(-2, 3):  # index leads by `lag` quarters relative to deals
    xs, yn, yd = {k: [] for k in series}, [], []
    for i, qq in enumerate(quarters):
        tq = i + lag
        if not (0 <= tq < len(quarters)): continue
        key = quarters[tq]
        if key not in deals: continue
        for k in series: xs[k].append(out_q[i][k])
        yn.append(deals[key][0]); yd.append(deals[key][1])
    if len(yn) < 6: continue
    print(f"\n-- index leads deals by {-lag}q (n={len(yn)} obs) --")
    for k in series:
        print(f"  {k:9s} pearson={pearson(xs[k], yn):+.2f} spearman={spearman(xs[k], yn):+.2f} | ndkp: {pearson(xs[k], yd):+.2f}/{spearman(xs[k], yd):+.2f}")

# sanity: weekly corr between B and C (rent vs panic)
b = [groups[d].get('B_rent', 0) for d in dates]
c = [groups[d].get('C_panic', 0) for d in dates]
a = [groups[d].get('A_invest', 0) for d in dates]
print(f"\nweekly pearson A~B={pearson(a,b):+.2f} A~C={pearson(a,c):+.2f} B~C={pearson(b,c):+.2f}")
print("\nSaved: data/wordstat_demand_indices_{weekly,quarterly}.csv")
