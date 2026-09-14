# Rosstat оперативные публикации 2026: выпуск 02.09/04.09.2026 (январь-июль)

Дата проверки: 2026-09-14 (cron). График: https://rosstat.gov.ru/storage/mediabank/Grafic_oper_public_2026.doc

## Скачано
- **Краткосрочные экономические показатели РФ (январь-июль 2026)** — выпущен 04.09.2026.
  - Файл: `raw/rosstat/operational/ind_07-2026.xlsx` (1.67 Мб, 43 листа, ряды с 1999 г.)
  - Источник: https://rosstat.gov.ru/compendium/document/50802 (страница `/statistics/kratkosrochnye-pokazateli` → 404; актуальный вход — compendium 50802)
  - Ключевые листы: 1.6 (ИКВ, кв.+мес.), 1.7 (СМР), 1.8 (ввод жилья), 2.2 (финрезультат по ВЭД), 3.3 (сводный индекс цен инвестназначения)
- **График оперативных публикаций 2026** — `raw/rosstat/operational/Grafic_oper_public_2026.doc`
- **Мониторинг регионов, info-stat-07-2026.zip** (8.5 Мб, 70 файлов; выпущен в пакете 02.09) — `raw/rosstat/socioeconomic_regions/`
  - Извлечены: 03-01 (СМР по регионам, млн руб + 3 листа %), 03-02 (жилье .xls), 07-01 (ИКВ по регионам), 02-01
- **Доклад Doklad_07-2026 / Pril_Dok_07-2026**: уже был скачан ранее (md5-совпадение STROIT-1-1.doc с локальным `doklad_2026/doklad_07-2026/`); Pril_Dok_08-2026 ещё 404 (выпуск 30.09).

## Парсинг → SQLite (`data/rosstat_construction.db`)
- `construction_volume_monthly_rf`: +Июль 2026 (1790.5 млрд руб, yoy 100.8%, mom 101.1%), +Январь-июль 9290.3 млрд руб (yoy 96.7%) — источник `rosstat_kep_ind_07-2026` (лист 1.7; cumsum мес. = 9290.3).
- `housing_input_operational_monthly` (источник `rosstat_kep_ind_07-2026`): 14 строк РФ, мес. янв-июль 2026 — construction_volume и housing_input_rf (значения+yoy). Июль ввод жилья 7.87 млн кв.м (+105.7% yoy).
- `investment_fixed_capital_quarterly` (новая таблица): ИКВ РФ Q1 6634.6 млрд руб (85.7% yoy), Q2 9586.0 млрд руб (93.4% yoy) — лист 1.6.
- `doklad_2026_monitoring_jul` (новая таблица, 862 строки, 105 регионов):
  - construction_volume_cumulative (млн руб, янв-июль; РФ 3 324 731.4)
  - construction_volume_pct_to_july / _to_period / _to_prev_month
  - housing_built_area_cumulative (тыс. кв. м; РФ 37.2 млн кв.м — ввод жилья «с учетом ИЖС на садовых участках»)
  - investment_fixed_capital_cumulative (Q1 и H1 2026; РФ H1 16 220 618 млн руб) + pct

## Ключевые значения для nowcasting (РФ)
- СМР июль 2026: 1790.5 млрд руб, yoy +0.8%; янв-июль 9290.3 млрд руб, yoy −3.3%
- Ввод жилья июль: 7.87 млн кв.м, yoy +5.7%; H1: 37.2 млн кв.м (monitoring, с ИЖС-садовыми)
- ИКВ: Q1 6634.6 (−14.3% yoy), Q2 9586.0 (−6.6% yoy) — по полному кругу

## Следующие выпуски
- 30.09: Doklad/Monitoring янв-авг; 02.10: Краткосрочные