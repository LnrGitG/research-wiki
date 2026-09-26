# Anomaly Screen Audit Report

## 1. Growth calculation verification
Total rows compared (excluding emiss_31074_cpi_prevm_m and virtr): 3680
Rows with growth_pct mismatch > 0.01 p.p.: 0
First 10 mismatching rows:
|block_metric|region|period|growth_pct_A|growth_pct_computed|diff|
|---|---|---|---|---|---|

## 2. Value and value_prev consistency
Random sample (seed 42) of 200 rows: value mismatches = 0, value_prev mismatches = 0
All rows for metric vmd: mismatches = 0
All rows for metric zyli: mismatches = 0

## 3. Identical metric series across regions
|Metric 1|Metric 2|Regions with complete match|
|---|---|---|
|rosstat_housing_pop_m|rosstat_housing_total_m|1|

## 4. Regions with all-zero values per metric
|Metric|Zero regions count|Regions (if ≤5)|
|---|---|---|
|zyli|23||