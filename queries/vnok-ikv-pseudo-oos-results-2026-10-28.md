# Pseudo-OOS results: IKV and VNOK benchmarks

Date: 2026-10-28. These are exploratory expanding-window forecasts under the owner's working assumption `vintage=current`, not verified real-time forecasts. Canonical target/predictor reads were via read-only `db_tunnel`; forecasts preserve explicit origin and target quarter keys.

Reproducible code: `scripts/vnok_ikv_oos.py`. Forecast-level export: `queries/vnok-ikv-oos-origin-forecasts-2026-10-28.csv`. Target: `ikv_rf_q_yoy` (14 targets, 2023Q1–2026Q2) and canonical `vnoki` (13 targets, 2023Q1–2026Q1). The earlier planned SQLite `gdp_use_ifo_quarterly` is not a catalog metric and is not the target tested here; `vnoki` remains an unverified semantic match.

Predictors: national construction `kep1_72` and housing completion `kep1_82` at region 1/release 134/exact CЭП subdimension; cement `ptvg`, one record per month, selecting the larger release_id when months overlap. Monthly values were summed to quarter then transformed to year-over-year percent change. Each forecast used only the completed predictor quarter t−1. This is a conservative mechanical lag, not an empirically established historical publication lag. Housing has 13 valid IKV origins due to predictor coverage.

| Target | Model | n | MAE | RMSE | Theil U vs carry |
|---|---|---:|---:|---:|---:|
| IKV `ikv_rf_q_yoy` | Carry | 14 | 4.036 | 4.998 | 1.000 |
| IKV | Seasonal naive | 14 | 7.886 | 9.716 | 1.944 |
| IKV | AR(1) | 14 | 4.189 | 5.411 | 1.083 |
| IKV | Construction `kep1_72` | 14 | 5.472 | 7.181 | 1.437 |
| IKV | Housing `kep1_82` | 13 | 5.909 | 7.885 | 1.580 |
| IKV | Cement `ptvg` | 14 | 3.673 | 5.216 | 1.043 |
| `vnoki` | Carry | 13 | 4.277 | 5.108 | 1.000 |
| `vnoki` | Seasonal naive | 13 | 7.031 | 8.595 | 1.683 |
| `vnoki` | AR(1) | 13 | 4.512 | 5.332 | 1.044 |
| `vnoki` | Construction `kep1_72` | 13 | 5.870 | 6.886 | 1.348 |
| `vnoki` | Housing `kep1_82` | 13 | 7.422 | 8.500 | 1.664 |
| `vnoki` | Cement `ptvg` | 13 | 6.195 | 7.781 | 1.523 |

Interpretation: among single-predictor models, cement has lower RMSE than carry for IKV but higher MAE; no construction predictor beats carry on both metrics. All three lose to carry for `vnoki`. The test windows are short; metrics disagree for cement/IKV; target semantics and release timing remain uncertain. Thus added predictive value is not established. Do not claim statistical significance or genuine real-time performance.

This corrected origin-keyed run replaces earlier benchmark figures that lacked a validated origin/target export; do not cite those earlier MAE/RMSE numbers. The retained test uses canonical `vnoki`, not the separate local SQLite series; their equivalence is not established. `scripts/ikv_benchmarks.py` remains unsuitable because it averages across unresolved release/subdimension/region rows and includes current-quarter months.

## Wordstat extension

The six-phrase B2B investment Wordstat dataset was successfully re-fetched from Yandex Wordstat for 2018-01-01 through 2026-10-25. The API returned 457 observations for every phrase; the newest returned week is 2026-09-28, so no October 2026 weeks were available. The public-mirror CSV was refreshed at `~/research-wiki/data/wordstat_weekly_b2b_invest.csv`; a private working copy is `data/wordstat_weekly_b2b_invest.csv`.

For a preliminary comparison, weekly `share` was averaged by quarter within phrase, and the six phrase series were averaged equally into a single S6 composite. The same expanding-window origin-keyed code used only the last completed quarter's composite as predictor. For IKV, the composite has MAE 6.121 and RMSE 7.654 (`n=14`), versus carry MAE 4.036 and RMSE 4.998; it therefore does not improve the benchmark. The Wordstat composite is not yet a preregistered measure, and the data refresh is not evidence that publication dates historically preceded each forecast origin. Do not treat this as a verified real-time signal.

## Sign and temporal-split diagnostics

As an additional descriptive diagnostic, direction accuracy is defined as matching the sign of the forecasted change from the previous quarter's observed target to the sign of the realized change. This is not evidence of statistical significance. The first/second halves below are fixed chronological splits of the same OOS forecasts (7/7 quarters for ИКВ; 6/7 for `vnoki`); they are stability checks, not separately tuned model windows. Direction accuracy for carry is zero by construction under this definition because its forecast is exactly the previous value; it is shown as a reference, not a useful directional strategy.

| Target | Model | Direction correct | First-half MAE / RMSE | Second-half MAE / RMSE |
|---|---|---:|---:|---:|
| ИКВ | Carry | 0/14 (0.000) | 3.529 / 3.995 | 4.543 / 5.832 |
| ИКВ | Seasonal naive | 5/14 (0.357) | 5.800 / 7.835 | 9.971 / 11.287 |
| ИКВ | AR(1) | 8/14 (0.571) | 3.112 / 3.782 | 5.265 / 6.652 |
| ИКВ | СМР | 8/14 (0.571) | 4.820 / 5.680 | 6.124 / 8.419 |
| ИКВ | Housing | 7/13 (0.538) | 4.116 / 4.357 | 7.446 / 9.959 |
| ИКВ | Cement | 9/14 (0.643) | 3.320 / 3.795 | 4.027 / 6.325 |
| `vnoki` | Carry | 1/13 (0.077) | 5.433 / 5.892 | 3.286 / 4.324 |
| `vnoki` | Seasonal naive | 4/13 (0.308) | 5.750 / 6.682 | 8.129 / 9.946 |
| `vnoki` | AR(1) | 4/13 (0.308) | 5.546 / 5.942 | 3.627 / 4.748 |
| `vnoki` | СМР | 5/13 (0.385) | 5.922 / 6.661 | 5.827 / 7.073 |
| `vnoki` | Housing | 4/13 (0.308) | 8.929 / 9.491 | 6.130 / 7.548 |
| `vnoki` | Cement | 6/13 (0.462) | 8.559 / 9.964 | 4.167 / 5.228 |

These splits do not change the conclusion: no construction predictor robustly improves both error metrics against carry across the two targets and temporal halves. In particular, cement's ИКВ MAE improvement over carry is accompanied by worse full-window RMSE and weaker second-half RMSE; for `vnoki`, cement remains worse than carry on both full-window metrics. Directional results vary by target/model and remain descriptive in these very short windows. The forecast table includes actual target values, and the direction calculations use its `carry_forecast` as the preceding-quarter target value.
