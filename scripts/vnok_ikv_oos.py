#!/usr/bin/env python3
"""Reproducible pseudo-real-time quarterly OOS for IKV and VNOK.

Read-only exports via db_tunnel and local SQLite mode=ro. Historical-vintage
identity is a user-provided assumption, not verified. Predictor choices are
explicit: Russia aggregate construction (kep1_72), housing completions
(kep1_82), cement (ptvg). Do not interpret SA/units until source audit.
"""
from __future__ import annotations
import argparse, json, sqlite3, sys
from pathlib import Path
import numpy as np
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_tunnel import query

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'queries' / 'vnok-ikv-oos-origin-forecasts-2026-10-28.csv'

def get_canon(code, region_id=None, release_id=None, sub=None):
    sql="""SELECT o.period_start,o.value,o.region_id,o.release_id,o.sub_dimension,o.assessment_type
      FROM data.observation o JOIN catalog.metric m USING(metric_id)
      WHERE m.metric_code=%s"""
    params=[code]
    if region_id is not None: sql += " AND o.region_id=%s"; params.append(region_id)
    if release_id is not None: sql += " AND o.release_id=%s"; params.append(release_id)
    if sub is not None: sql += " AND o.sub_dimension=%s"; params.append(sub)
    sql += " ORDER BY o.period_start"
    rows=query(sql,tuple(params))
    vals={}
    for p,v,reg,rel,sub,assess in rows:
        q=pd.Period(str(p),freq='Q')
        if q in vals: raise ValueError(f'{code}: duplicate target quarter {q}')
        vals[q]=float(v)
    return pd.Series(vals,dtype=float).sort_index()

def get_monthly(code, release_id, sub, region_id=1):
    rows=query("""SELECT o.period_start,o.value,o.region_id,o.release_id,o.sub_dimension,o.assessment_type
      FROM data.observation o JOIN catalog.metric m USING(metric_id)
      WHERE m.metric_code=%s AND o.region_id=%s AND o.release_id=%s
        AND o.sub_dimension=%s AND o.assessment_type IN ('final','preliminary')
      ORDER BY o.period_start""",(code,region_id,release_id,sub))
    s={}
    for p,v,*_ in rows:
        m=pd.Period(str(p),freq='M')
        if m in s: raise ValueError(f'{code}: duplicate month {m}')
        s[m]=float(v)
    return pd.Series(s,dtype=float).sort_index()

def quarterly_yoy(s, method='sum'):
    s=s.sort_index()
    if method=='sum': q=s.groupby(s.index.asfreq('Q')).sum(min_count=3)
    elif method=='mean': q=s.groupby(s.index.asfreq('Q')).mean()
    else: raise ValueError('method must be sum or mean')
    return q.pct_change(4)*100

def score(actual,pred,base):
    e=np.asarray(pred)-np.asarray(actual)
    eb=np.asarray(base)-np.asarray(actual)
    return {'n':int(len(e)),'MAE':float(np.mean(np.abs(e))),
            'RMSE':float(np.sqrt(np.mean(e*e))),
            'Theil_U_vs_carry':float(np.sqrt(np.mean(e*e))/np.sqrt(np.mean(eb*eb))) if np.sqrt(np.mean(eb*eb)) else None}

def eval_target(name,y,xs,start='2023Q1',min_train=12):
    records=[]
    ts=[q for q in y.index if q>=pd.Period(start,'Q')]
    for t in ts:
        train=y[y.index<t].dropna()
        if len(train)<min_train: continue
        prev=t-1
        if prev not in y.index: continue
        carry=float(y.loc[prev])
        seas=float(y.loc[t-4]) if t-4 in y.index else np.nan
        # AR(1) fit only using target observations strictly before origin.
        pairs=pd.DataFrame({'y':y,'lag':y.shift(1)}).loc[:t-1].dropna()
        if len(pairs)<min_train-1: ar=np.nan
        else:
            X=np.column_stack([np.ones(len(pairs)),pairs['lag'].to_numpy()])
            b=np.linalg.lstsq(X,pairs['y'].to_numpy(),rcond=None)[0]
            ar=float(b[0]+b[1]*carry)
        base={'carry':carry,'seasonal_naive':seas,'AR1':ar}
        row={'target':name,'origin_quarter':str(prev),'target_quarter':str(t),
             'actual':float(y.loc[t]),'carry_forecast':carry,
             'seasonal_naive_forecast':seas,'AR1_forecast':ar}
        for k,x in xs.items():
            # Features are quarterly YOY; only prior-quarter observation used,
            # avoiding unknown within-quarter months at origin.
            xp=t-1
            if xp not in x.index or not np.isfinite(x.loc[xp]):
                row[k+'_forecast']=np.nan; continue
            train_df=pd.concat([y.rename('y'),x.rename('x')],axis=1)
            train_df=train_df[train_df.index<t].dropna()
            if len(train_df)<min_train:
                row[k+'_forecast']=np.nan; continue
            Z=np.column_stack([np.ones(len(train_df)),train_df.x.to_numpy()])
            b=np.linalg.lstsq(Z,train_df.y.to_numpy(),rcond=None)[0]
            row[k+'_forecast']=float(b[0]+b[1]*x.loc[xp])
        records.append(row)
    return records

def load_wordstat():
    p=ROOT / 'data/wordstat_weekly_b2b_invest.csv'
    w=pd.read_csv(p)
    w['date']=pd.to_datetime(w.date)
    w['share']=pd.to_numeric(w.share,errors='raise')
    q=[]
    for phrase,g in w.groupby('phrase'):
        s=g.set_index('date').share.sort_index()
        m=s.resample('QE').mean()
        m.index=m.index.to_period('Q')
        q.append(m.rename(phrase))
    return pd.concat(q,axis=1).sort_index().mean(axis=1,skipna=False).rename('wordstat_s6')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--write',action='store_true'); a=ap.parse_args()
    ikv=get_canon('ikv_rf_q_yoy',region_id=1,sub='')
    vnok=get_canon('vnoki',region_id=1,sub='')
    smr=quarterly_yoy(get_monthly('kep1_72',134,'ряд: КЭП | лист: 1.7 | блок: уровень'))
    housing=quarterly_yoy(get_monthly('kep1_82',134,'ряд: КЭП | лист: 1.8 | блок: уровень'))
    wordstat=load_wordstat()
    rows=query("""SELECT o.period_start,o.value,o.release_id,o.sub_dimension,o.assessment_type
      FROM data.observation o JOIN catalog.metric m USING(metric_id)
      WHERE m.metric_code='ptvg' AND o.region_id=1 ORDER BY o.period_start,o.release_id""")
    cem={}
    for p,v,rid,sub,ass in rows:
        m=pd.Period(str(p),freq='M')
        if m in cem:
            if rid>cem[m][0]: cem[m]=(rid,float(v))
        else: cem[m]=(rid,float(v))
    cement=quarterly_yoy(pd.Series({m:v for m,(rid,v) in cem.items()},dtype=float).sort_index())
    preds={'smr':smr,'housing':housing,'cement':cement,'wordstat_s6':wordstat}
    records=eval_target('ikv_rf_q_yoy',ikv,preds)+eval_target('vnoki',vnok,preds)
    if not records: raise RuntimeError('No forecast origins')
    df=pd.DataFrame(records).sort_values(['target','target_quarter'])
    for target,g in df.groupby('target'):
        valid=g.dropna(subset=['carry_forecast'])
        print(target,'origins',valid['target_quarter'].iloc[0],valid['target_quarter'].iloc[-1],len(valid))
        for model,col in [('carry','carry_forecast'),('seasonal','seasonal_naive_forecast'),('AR1','AR1_forecast'),('SMR','smr_forecast'),('housing','housing_forecast'),('cement','cement_forecast'),('wordstat_s6','wordstat_s6_forecast')]:
            z=valid.dropna(subset=[col])
            if len(z): print(model,score(z.actual,z[col],z.carry_forecast))
    print('forecast rows',len(df),'output',OUT)
    if a.write:
        df.to_csv(OUT,index=False)
        print('WROTE',OUT)
    else: print('Dry run only; pass --write to persist the keyed forecast table.')
if __name__=='__main__': main()
