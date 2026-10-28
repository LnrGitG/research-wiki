#!/usr/bin/env python3
"""H-007: OOS stability detail — per-quarter errors, sub-window RMSE, lag2 vs lag3 bridge."""
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, "/home/lnr/research-wiki-private/scripts")
from db_tunnel import query  # noqa: E402

CSV = os.environ.get("H007_INPUTS", "/home/lnr/.hermes/kanban/boards/research/attachments/t_e9cfa6d6/h007_inputs_quarterly.csv")
df = pd.read_csv(CSV)
df["quarter"] = pd.PeriodIndex(df["quarter"], freq="Q")
df = df.set_index("quarter").sort_index()

rows = query("""SELECT o.period_start, o.value FROM data.observation o
JOIN catalog.metric m USING(metric_id) WHERE m.metric_code='ikv_rf_q_yoy' ORDER BY 1""")
ik = pd.DataFrame(rows, columns=["d", "v"])
ik["d"] = pd.to_datetime(ik["d"])
ik["q"] = ik.d.dt.to_period("Q")
ikv = ik.groupby("q").v.mean().sort_index().astype(float)

full = pd.DataFrame({"y": ikv})
full["x2"] = df["esc_lag2"].reindex(full.index)
full["x3"] = df["esc_almon_q_pct_change"].shift(3).reindex(full.index)
full["y_l1"] = full.y.shift(1)

def run(col):
    recs = []
    for t in full.index:
        if t < pd.Period("2024Q1", "Q"):
            continue
        if pd.isna(full.loc[t, col]) or pd.isna(full.loc[t, "y"]):
            continue
        tr = full.loc[full.index < t]
        trb = tr.dropna(subset=[col, "y"])
        tra = tr.dropna(subset=["y_l1", "y"])
        if len(trb) < 4:
            continue
        A = np.column_stack([np.ones(len(tra)), tra.y_l1.values])
        ba = np.linalg.lstsq(A, tra.y.values, rcond=None)[0]
        ar = float(ba[0] + ba[1] * full.loc[t, "y_l1"])
        B = np.column_stack([np.ones(len(trb)), trb[col].values])
        bb = np.linalg.lstsq(B, trb.y.values, rcond=None)[0]
        br = float(bb[0] + bb[1] * full.loc[t, col])
        recs.append({"q": str(t), "fact": float(full.loc[t, "y"]), "ar": ar, "br": br,
                     "e_ar": ar - float(full.loc[t, "y"]), "e_br": br - float(full.loc[t, "y"])})
    return pd.DataFrame(recs)

o2, o3 = run("x2"), run("x3")
print("=== bridge lag2 (clean almon) ===")
print(o2.to_string(index=False))
print("\n=== bridge lag3 (clean almon) ===")
print(o3.to_string(index=False))

def rmse(v):
    return float(np.sqrt(np.mean(v ** 2)))

print("\n=== RMSE по окнам ===")
for nm, o in (("lag2", o2), ("lag3", o3)):
    a = o[o.q <= "2025Q3"]
    b = o[o.q >= "2025Q4"]
    print("%s: все %d кв.  AR %.2f | bridge %.2f   || 24Q3-25Q3 (%d кв.) AR %.2f | bridge %.2f   || 25Q4-26Q2 (%d кв.) AR %.2f | bridge %.2f" % (
        nm, len(o), rmse(o.e_ar), rmse(o.e_br), len(a), rmse(a.e_ar), rmse(a.e_br),
        len(b), rmse(b.e_ar), rmse(b.e_br)))
    print("   доля кварталов, где bridge ближе к факту: %d/%d" % (
        int((o.e_br.abs() < o.e_ar.abs()).sum()), len(o)))
