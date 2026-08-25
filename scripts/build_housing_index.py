#!/usr/bin/env python3
"""Validate housing dictionary and build PCA index (QUIET recipe)."""
import pandas as pd
import numpy as np

df = pd.read_csv('/home/lnr/research-wiki/data/search_trends_housing_raw.csv',
                 index_col=0, parse_dates=True)
# unify the two spellings of вторичное
if 'вторичное жилье' in df.columns:
    df['вторичное жильё'] = df['вторичное жильё'].fillna(df['вторичное жилье'])
df = df.drop(columns=['вторичное жилье'])
df = df.loc['2018-01-01':'2026-08-01']

print("=== 1. Volume filter (mean level, proxy for absolute volume) ===")
keep, drop_reason = [], {}
for c in df.columns:
    s = df[c].dropna()
    # Google Trends 0-100 within window; mean<1.5 & p75<3 => noisy/ultra-low-volume
    q75 = s.quantile(0.75)
    ok = (s.mean() >= 1.0) or (q75 >= 2.5)
    print(f"{c:18s} mean={s.mean():6.2f} q75={q75:5.1f} zeros={(s==0).sum():3d}/104 -> {'KEEP' if ok else 'DROP'}")
    if ok:
        keep.append(c)
    else:
        drop_reason[c] = 'low volume'

print("\n=== 2. Duplicate check (corr of levels > 0.8) ===")
lv = np.log(df[keep].clip(lower=0.5))
C = lv.corr()
to_drop_dup = set()
cols = list(keep)
for i in range(len(cols)):
    for j in range(i+1, len(cols)):
        r = C.iloc[i, j]
        if abs(r) > 0.8 and cols[j] not in to_drop_dup:
            to_drop_dup.add(cols[j])
            print(f"DUP {cols[i]} ~ {cols[j]}: rho={r:.3f} -> drop '{cols[j]}'")
final = [c for c in keep if c not in to_drop_dup]
print("final dictionary:", final)

print("\n=== 3. Outlier scan (log-level jumps |d.log|>1) ===")
dl = lv[final].diff()
outliers = (dl.abs() > 1.0).sum()
print(outliers.to_string())

print("\n=== 4. KMO ===")
from factor_analyzer.factor_analyzer import calculate_kmo
X = dl.dropna()
kmo_all, kmo_model = calculate_kmo(X)
print("KMO overall:", round(float(np.asarray(kmo_all).flatten()[0]), 3))
for c, k in zip(final, np.atleast_1d(kmo_model)):
    print(f"  {c:18s} {float(k):.3f}")

print("\n=== 5. PCA (correlation matrix of log-diffs) ===")
from sklearn.decomposition import PCA
Z = (X - X.mean()) / X.std()
pca = PCA(n_components=len(final)).fit(Z)
evr = pca.explained_variance_ratio_
print("explained variance:", [f"{v:.1%}" for v in evr[:4]])
pc1 = pd.Series(pca.transform(Z)[:, 0], index=X.index, name='housing_sentiment_pc1')
# sign convention: more positive = more search interest growth; orient so corr with ипотека diff is +
if pc1.corr(dl['ипотека'].dropna()) < 0:
    pc1 = -pc1
    print("(sign flipped for positive loading on ипотека)")
loadings = pd.Series(pca.components_[0], index=final).sort_values(key=abs, ascending=False)
print("\nPC1 loadings:")
print((loadings / abs(loadings).max()).round(3).to_string())

idx = pd.DataFrame({'pc1': pc1})
idx['std'] = (pc1 - pc1.mean()) / pc1.std()
idx.to_csv('/home/lnr/research-wiki/data/housing_sentiment_index.csv', float_format='%.4f')
print("\nsaved data/housing_sentiment_index.csv", idx.shape)

print("\n=== yearly means (std units) ===")
print(idx['std'].resample('YE').mean().round(2).to_string())
