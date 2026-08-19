# Эконометрический workflow на R для research-wiki

## Архитектура системы

```
research-wiki/
├── data/
│   └── rosstat_construction.db      (SQLite, 757 МБ, 1.2M записей)
├── scripts/
│   ├── db_connect.R                 (подключение к БД, helpers)
│   ├── 01_eda.R                     (разведочный анализ)
│   ├── 02_panel_models.R            (панельные модели)
│   ├── 03_nowcasting.R              (наукастинг)
│   ├── 04_forecasting.R             (прогнозирование)
│   ├── 05_structural_breaks.R       (структурные сдвиги)
│   └── functions/
│       ├── load_data.R              (загрузка из SQLite)
│       ├── ts_utils.R               (утилиты временных рядов)
│       └── plot_utils.R             (визуализация)
└── output/
    ├── plots/
    ├── tables/
    └── models/
```

## Доступные данные для моделей

### Временные ряды (РФ, помесячно)

| Ряд | Период | N obs | Источник |
|-----|--------|-------|---------|
| Разрешения на строительство (поток) | 2024-01 → 2026-07 | 31 | DOM.RF permits_flow |
| ДДУ действующие (214-ФЗ) | 2021-01 → 2026-08 | 68 | DOM.RF ddu |
| ДДУ площадь (214-ФЗ) | 2021-01 → 2026-08 | 68 | DOM.RF ddu |
| ДДУ цена (214-ФЗ) | 2021-01 → 2026-08 | 68 | DOM.RF ddu |
| Ввод МКД (поток) | 2020-01 → 2026-07 | 79 | DOM.RF flow |
| Строящееся жильё (сток) | 2020-01 → 2026-08 | 80 | DOM.RF stock |
| Продажи квартир (м²) | 2020-01 → 2026-08 | 80 | DOM.RF sales_meters |
| ИЖК траншей (мес.) | 2024-01 → 2026-06 | 32 | DOM.RF mortgage |
| Цены первичный рынок (кв.) | 2016-Q1 → 2026-Q3 | ~43 | Росстат 10-05 |
| Цены вторичный рынок (кв.) | 2016-Q1 → 2026-Q3 | ~43 | Росстат 10-05 |
| Цены годовые (первичн.+вторичн.) | 2000 → 2023 | 24 | Росстат 3.2 |

### Панельные данные (по регионам, помесячно)

| Ряд | Период | Регионов | Записей |
|-----|--------|---------|---------|
| Разрешения на строительство | 2020-01 → 2026-07 | 91 | 28 756 |
| ДДУ | 2021-01 → 2026-08 | 90 | 36 720 |
| Ввод МКД (поток) | 2020-01 → 2026-07 | 90 | 284 400 |
| Строящееся жильё (сток) | 2020-01 → 2026-08 | 90 | 324 000 |
| Продажи квартир (м²) | 2020-01 → 2026-08 | 99 | 8 000 |

### Годовые данные (по регионам)

| Ряд | Период | Регионов | Записей |
|-----|--------|---------|---------|
| Ввод зданий | 2000 → 2024 | 96 | 2 367 |
| Незавершённое строительство | 2000 → 2024 | 97 | 6 970 |
| Занятость в строительстве | 2010 → 2024 | 85 | 358 |
| Цены на жильё (годовые) | 2000 → 2023 | 96 | 2 919 |
| Парк техники | ~2021, ~2023 | 85 | 696 |
| Производство материалов (ФО) | 2016 → 2023 | 8 | 748 |

---

## Шаг 1: Подключение и загрузка данных

### `scripts/db_connect.R`

```r
library(DBI)
library(RSQLite)
library(dplyr)
library(zoo)
library(xts)

# === Подключение к SQLite ===
db_path <- "data/rosstat_construction.db"
con <- dbConnect(RSQLite::SQLite(), db_path)

# === Helpers ===

#' Загрузка временного ряда (РФ)
load_ts_rf <- function(table, indicator_pattern, data_type = NULL,
                       freq = "monthly") {
  sql <- glue::glue(
    "SELECT date, value FROM {table}
     WHERE region_name = 'Российская Федерация'
     AND indicator_name LIKE '%{indicator_pattern}%'"
  )
  if (!is.null(data_type)) {
    sql <- paste0(sql, glue::glue(" AND data_type = '{data_type}'"))
  }
  sql <- paste0(sql, " ORDER BY date")

  df <- dbGetQuery(con, sql)
  df$date <- as.yearmon(df$date, "%Y-%m-%d")
  ts <- xts(df$value, order.by = df$date)
  return(ts)
}

#' Загрузка панельных данных
load_panel <- function(data_type, indicator_pattern = "%") {
  sql <- glue::glue(
    "SELECT region_name, date, indicator_name, value
     FROM domrf_indicators
     WHERE data_type = '{data_type}'
     AND indicator_name LIKE '%{indicator_pattern}%'
     AND region_name NOT LIKE '%ФО%'
     AND region_name NOT LIKE '%округ%'
     AND region_name NOT LIKE '%Федерация%'
     AND region_name NOT LIKE '%Не продано%'
     AND region_name NOT LIKE '%Продажи не%'
     AND region_name NOT LIKE '%Продано%'
     ORDER BY region_name, date"
  )
  df <- dbGetQuery(con, sql)
  df$date <- as.Date(df$date)
  return(df)
}

#' Загрузка цен на жильё (кв.)
load_prices <- function(market = "primary") {
  df <- dbGetQuery(con, glue::glue(
    "SELECT region_name, year, quarter, price_per_sqm
     FROM housing_prices_quarterly
     WHERE market = '{market}'
     ORDER BY region_name, year, quarter"
  ))
  df$date <- as.yearqtr(paste(df$year, df$quarter, sep = "-"))
  return(df)
}
```

---

## Шаг 2: Разведочный анализ (EDA)

### `scripts/01_eda.R`

```r
source("scripts/db_connect.R")

library(ggplot2)
library(tidyverse)
library(patchwork)  # многослойные графики

# === 2.1 Загрузка ключевых рядов ===

# Разрешения на строительство (поток, МКД шт.)
ts_permits <- load_ts_rf("domrf_indicators",
  indicator_pattern = "Количество многоквартирных домов, в отношении которых выданы",
  data_type = "permits_flow")

# ДДУ (кол-во действующих, 214-ФЗ)
ts_ddu <- load_ts_rf("domrf_indicators",
  indicator_pattern = "Количество действующих договоров участия в долевом строительстве в отн",
  data_type = "ddu")

# Ввод МКД (поток, шт.)
ts_flow <- load_ts_rf("domrf_indicators",
  indicator_pattern = "Количество многоквартирных домов в составе проектов",
  data_type = "flow")

# Продажи (м²)
ts_sales <- load_ts_rf("domrf_indicators",
  indicator_pattern = "Реализация квартир",
  data_type = "sales_meters")

# Строящееся жильё (сток, м²)
ts_stock <- load_ts_rf("domrf_indicators",
  indicator_pattern = "Общая площадь многоквартирных домов, строящихся в соотв",
  data_type = "stock")

# === 2.2 Визуализация ===

# Функция для построения графиков
plot_ts <- function(ts, title, ylab) {
  df <- data.frame(date = index(ts), value = coredata(ts))
  ggplot(df, aes(x = date, y = value)) +
    geom_line(color = "#2E86AB", linewidth = 0.8) +
    labs(title = title, y = ylab, x = "") +
    theme_minimal() +
    scale_x_yearmon(format = "%Y-%m") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}

# Сводный график: 4 ключевых индикатора
p1 <- plot_ts(ts_permits, "Разрешения на строительство (МКД, шт./мес.)", "шт.")
p2 <- plot_ts(ts_ddu, "ДДУ действующие (214-ФЗ, шт.)", "шт.")
p3 <- plot_ts(ts_sales / 1e6, "Продажи квартир (млн м²)", "млн м²")
p4 <- plot_ts(ts_stock / 1e6, "Строящееся жильё (млн м²)", "млн м²")

# Сохранить
ggsave("output/plots/eda_overview.png",
  p1 / p2 / p3 / p4, width = 10, height = 12, dpi = 150)

# === 2.3 Описательные статистики ===

library(psych)  # describe()

desc_stats <- function(ts, name) {
  data.frame(
    indicator = name,
    n = length(ts),
    mean = mean(ts, na.rm = TRUE),
    sd = sd(ts, na.rm = TRUE),
    min = min(ts, na.rm = TRUE),
    max = max(ts, na.rm = TRUE),
    cv = sd(ts, na.rm = TRUE) / mean(ts, na.rm = TRUE)
  )
}

stats <- rbind(
  desc_stats(ts_permits, "permits_flow"),
  desc_stats(ts_ddu, "ddu_active"),
  desc_stats(ts_sales, "sales_m2"),
  desc_stats(ts_stock, "stock_m2")
)

write.csv(stats, "output/tables/descriptive_stats.csv", row.names = FALSE)

# === 2.4 Корреляции между рядами ===

# Выровнять ряды по датам
all_dates <- intersect(
  intersect(index(ts_permits), index(ts_ddu)),
  intersect(index(ts_sales), index(ts_stock))
)

cor_matrix <- cbind(
  permits = as.numeric(ts_permits[all_dates]),
  ddu = as.numeric(ts_ddu[all_dates]),
  sales = as.numeric(ts_sales[all_dates]),
  stock = as.numeric(ts_stock[all_dates])
)

cor_df <- cor(cor_matrix, use = "complete.obs")
print(cor_df)
write.csv(cor_df, "output/tables/correlation_matrix.csv")

# === 2.5 Сезонность ===

library(forecast)

ts_permits_ts <- ts(as.numeric(ts_permits), frequency = 12)
decomp <- decompose(ts_permits_ts, type = "multiplicative")
plot(decomp)
ggsave("output/plots/seasonal_decomposition.png",
  autoplot(decomp), width = 10, height = 8, dpi = 150)

# Сезонные индексы
seasonal_indices <- decomp$figure
print(round(seasonal_indices, 3))

# === 2.6 Региональная гетерогенность ===

# Загрузить панельные данные по ДДУ
panel_ddu <- load_panel("ddu", "Количество действующих договоров участия в долевом строительстве в отн")

# Топ-10 регионов по последнему значению
latest_ddu <- panel_ddu %>%
  group_by(region_name) %>%
  filter(date == max(date)) %>%
  arrange(desc(value)) %>%
  slice_head(n = 10)

ggplot(latest_ddu, aes(x = reorder(region_name, value), y = value / 1000)) +
  geom_col(fill = "#2E86AB") +
  coord_flip() +
  labs(title = "Топ-10 регионов: ДДУ (тыс. шт.)",
       x = "", y = "тыс. ДДУ") +
  theme_minimal()

ggsave("output/plots/ddu_top_regions.png", width = 8, height = 6, dpi = 150)
```

---

## Шаг 3: Панельные модели (causal inference)

### `scripts/02_panel_models.R`

```r
source("scripts/db_connect.R")

library(fixest)       # быстрый FE
library(marginaleffects) # интерпретация
library(sandwich)     # робастные SE
library(lmtest)       # тесты

# === 3.1 Панель: ДДУ × цены × регион × время ===

panel_ddu <- load_panel("ddu", "Количество действующих договоров")
panel_prices <- load_prices("primary")

# Агрегировать цены до годовых по регионам
prices_annual <- panel_prices %>%
  group_by(region_name, year = floor_date(date, "year")) %>%
  summarise(price = mean(price_per_sqm, na.rm = TRUE), .groups = "drop")

# Объединить
panel_ddu$year <- floor_date(panel_ddu$date, "year")
panel_merged <- panel_ddu %>%
  left_join(prices_annual, by = c("region_name", "year"))

# === 3.2 Модель с двумя фиксированными эффектами (TWFE) ===

# log(ДДУ) ~ log(цена) | регион + год
model_twfe <- feols(
  log(value) ~ log(price) | region_name + year,
  data = panel_merged,
  cluster = ~region_name
)

summary(model_twfe)

# === 3.3 Интерпретация через marginaleffects ===

# Средний маргинальный эффект цены на ДДУ
ame <- marginaleffects(model_twfe, variables = "price")
summary(ame)

# === 3.4 Диагностика ===

# Тест на гетероскедастичность
bptest(log(value) ~ log(price), data = panel_merged)

# Кластеризованные SE (уже включены через cluster = ~region_name)
# Дополнительно: HAC-ошибки
coeftest(model_twfe, vcov = vcovHC(model_twfe, type = "HC1"))
```

---

## Шаг 4: Наукастинг

### `scripts/03_nowcasting.R`

```r
source("scripts/db_connect.R")

library(bsts)        # Bayesian Structural Time Series
library(forecast)   # ARIMA baseline
library(fable)      # современный forecast
library(MARSS)      # factor models

# === 4.1 Подготовка: помесячный ряд ДДУ (РФ) ===

ts_ddu <- load_ts_rf("domrf_indicators",
  indicator_pattern = "Количество действующих договоров участия в долевом строительстве в отн",
  data_type = "ddu")

# Преобразовать в ts
ddu_ts <- ts(as.numeric(ts_ddu), frequency = 12,
             start = c(2021, 1))

# === 4.2 Baseline: ARIMA ===

fit_arima <- auto.arima(ddu_ts, seasonal = TRUE)
fc_arima <- forecast(fit_arima, h = 3)  # 3 месяца вперёд
print(fc_arima)
autoplot(fc_arima)
ggsave("output/plots/nowcast_arima.png", width = 10, height = 6, dpi = 150)

# === 4.3 BSTS: Bayesian Structural Time Series ===

# Локальный линейный тренд + сезонность + регрессоры
ss <- AddLocalLinearTrend(list(), ddu_ts)
ss <- AddSeasonal(ss, ddu_ts, nseasons = 12)

# Добавить регрессор: разрешения на строительство (lag 1-2 мес.)
ts_permits <- load_ts_rf("domrf_indicators",
  indicator_pattern = "Количество многоквартирных домов, в отношении которых выданы",
  data_type = "permits_flow")

# Выровнять по датам
common_dates <- intersect(index(ts_ddu), index(ts_permits))
regressors <- matrix(as.numeric(ts_permits[common_dates]),
                     ncol = 1, dimnames = list(NULL, "permits"))

fit_bsts <- bsts(ddu_ts, state.specification = ss,
                 regressors = regressors,
                 niter = 1000, seed = 42)

# Прогноз на 3 месяца
pred_bsts <- predict(fit_bsts, horizon = 3)
plot(pred_bsts)
ggsave("output/plots/nowcast_bsts.png", width = 10, height = 6, dpi = 150)

# === 4.4 Сравнение моделей ===

# Точность на тестовом окне (last 3 months)
h <- 3
train <- window(ddu_ts, end = end(ddu_ts) - h/12)
test <- window(ddu_ts, start = end(ddu_ts) - (h-1)/12)

# ARIMA
fit_arima_cv <- auto.arima(train)
fc_arima_cv <- forecast(fit_arima_cv, h = h)

# BSTS
ss_cv <- AddLocalLinearTrend(list(), train)
ss_cv <- AddSeasonal(ss_cv, train, nseasons = 12)
fit_bsts_cv <- bsts(train, state.specification = ss_cv, niter = 1000, seed = 42)
pred_bsts_cv <- predict(fit_bsts_cv, horizon = h)

# RMSE
rmse_arima <- sqrt(mean((test - fc_arima_cv$mean)^2, na.rm = TRUE))
rmse_bsts <- sqrt(mean((test - as.numeric(pred_bsts_cv$mean))^2, na.rm = TRUE))

cat("Nowcasting comparison (h=3):\n")
cat(sprintf("  ARIMA RMSE: %.0f\n", rmse_arima))
cat(sprintf("  BSTS  RMSE: %.0f\n", rmse_bsts))
```

---

## Шаг 5: Прогнозирование

### `scripts/04_forecasting.R`

```r
source("scripts/db_connect.R")

library(forecast)
library(fable)
library(bsts)
library(tidyr)

# === 5.1 Загрузка длинных рядов ===

# Цены на жильё (кв., РФ, первичный рынок)
prices_df <- load_prices("primary")
prices_rf <- prices_df %>%
  filter(region_name == "Российская Федерация") %>%
  arrange(date)

price_ts <- ts(prices_rf$price_per_sqm, frequency = 4,
               start = c(2016, 1))

# === 5.2 Классический подход: ARIMA + ETS ===

# ARIMA
fit_arima_price <- auto.arima(price_ts)
fc_arima_price <- forecast(fit_arima_price, h = 8)  # 8 кварталов

# ETS
fit_ets_price <- ets(price_ts)
fc_ets_price <- forecast(fit_ets_price, h = 8)

# Сравнение
cat("Forecast comparison (8 quarters):\n")
cat(sprintf("  ARIMA AIC: %.1f\n", fit_arima_price$aic))
cat(sprintf("  ETS  AIC: %.1f\n", fit_ets_price$aic))

# === 5.3 Bayesian: BSTS ===

ss_price <- AddLocalLinearTrend(list(), price_ts)
ss_price <- AddSeasonal(ss_price, price_ts, nseasons = 4)
fit_bsts_price <- bsts(price_ts, state.specification = ss_price,
                       niter = 2000, seed = 42)
pred_bsts_price <- predict(fit_bsts_price, horizon = 8)

# === 5.4 fable: множественная оценка ===

library(tsibble)
library(fable)

prices_tsbl <- prices_df %>%
  mutate(date = yearquarter(date)) %>%
  as_tsibble(key = region_name, index = date)

# Оценить ARIMA + ETS для всех регионов
models_fit <- prices_tsbl %>%
  model(
    arima = ARIMA(price_per_sqm),
    ets = ETS(price_per_sqm)
  )

# Прогноз для всех регионов
fc_all <- forecast(models_fit, h = 8)

# Точность
accuracy(models_fit, prices_tsbl)

# === 5.5 Визуализация ===

# Сравнение прогнозов
plot_data <- data.frame(
  date = time(fc_arima_price$mean),
  arima = as.numeric(fc_arima_price$mean),
  ets = as.numeric(fc_ets_price$mean),
  bsts = as.numeric(pred_bsts_price$mean)
)

# График: исторические + прогнозы
plot(price_ts, xlim = c(2016, 2028),
     main = "Прогноз цен на жильё (первичный рынок, РФ)",
     xlab = "", ylab = "руб./м²")
lines(fc_arima_price$mean, col = "blue", lwd = 2)
lines(fc_ets_price$mean, col = "red", lwd = 2)
lines(time(pred_bsts_price$mean), pred_bsts_price$mean, col = "green", lwd = 2)
legend("topleft", c("ARIMA", "ETS", "BSTS"),
       col = c("blue", "red", "green"), lwd = 2)
dev.copy(png, "output/plots/forecast_prices.png", width = 1000, height = 600)
dev.off()
```

---

## Шаг 6: Структурные сдвиги

### `scripts/05_structural_breaks.R`

```r
source("scripts/db_connect.R")

library(strucchange)  # тесты на структурные сдвиги
library(xts)

# === 6.1 Загрузка рядов ===

ts_ddu <- load_ts_rf("domrf_indicators",
  indicator_pattern = "Количество действующих договоров участия в долевом строительстве в отн",
  data_type = "ddu")
ddu_ts <- ts(as.numeric(ts_ddu), frequency = 12, start = c(2021, 1))

# === 6.2 Тест CUSUM ===

ocus <- efp(log(ddu_ts) ~ 1, type = "OLS-CUSUM")
plot(ocus)
s <- sctest(ocus)
cat(sprintf("CUSUM test: p-value = %.4f\n", s$p.value))

# === 6.3 Тест на структурный сдвиг (Bai-Perron) ===

bp <- breakpoints(log(ddu_ts) ~ 1)
print(bp$breakpoints)
plot(bp)

# === 6.4 Учёт сдвига в модели ===

# Создать фиктивную переменную после сдвига
break_date <- time(ddu_ts)[bp$breakpoints[1]]
dummy_break <- ifelse(time(ddu_ts) >= break_date, 1, 0)

# ARIMA с учетом сдвига
fit_arima_break <- auto.arima(ddu_ts, xreg = dummy_break)
summary(fit_arima_break)
```

---

## Установка пакетов

```r
# Core
install.packages(c("DBI", "RSQLite", "dplyr", "tidyr", "glue"))

# Time series
install.packages(c("zoo", "xts", "forecast", "fable", "tsibble",
                   "bsts", "MARSS"))

# Econometrics
install.packages(c("fixest", "marginaleffects", "sandwich", "lmtest",
                   "strucchange", "plm"))

# Visualization
install.packages(c("ggplot2", "patchwork", "psych"))
```

---

## Ключевые исследовательские вопросы

### А. Оценка (causal inference)

1. **Эффект льготной ипотеки (2020)** на цены жилья: DiD с контрольной группой (регионы без льготной ипотеки)
2. **Эффект повышения ключевой ставки (2023–2024)** на ДДУ: event study
3. **Влияние разрешений на строительство на цены**: IV с лагированными РНС как инструмент
4. **Эффект КРТ (комплексное развитие)** на ввод жилья: Synthetic Control

### Б. Наукастинг

1. **Текущий объём ДДУ**: ARIMA + BSTS с регрессором (разрешения с лагом 1–2 мес.)
2. **Текущие цены на жильё**: факторная модель (несколько индикаторов DOM.RF)
3. **Текущий объём продаж**: BSTS с сезонностью

### В. Прогнозирование

1. **Цены на жильё (1–2 года)**: ARIMA/ETS/BSTS, сравнение на CV
2. **Объём ввода жилья (годовые)**: fable для всех 85 регионов одновременно
3. **Незавершённое строительство**: ARIMA с структурным сдвигом

### Г. Структурные сдвиги

1. **Сдвиг в ДДУ (COVID 2020, льготная ипотека 2020–2021, ставка 2023)**: Bai-Perron
2. **Сдвиг в ценах (кризис 2014, COVID 2020, санкции 2022)**: CUSUM на квартальных данных
3. **Сдвиг в разрешениях на строительство**: QLR test

---

## Пайплайн запуска

```bash
# Из корня research-wiki/

# 1. Установка пакетов (один раз)
Rscript -e 'source("scripts/install_packages.R")'

# 2. EDA
Rscript scripts/01_eda.R

# 3. Панельные модели
Rscript scripts/02_panel_models.R

# 4. Наукастинг
Rscript scripts/03_nowcasting.R

# 5. Прогнозирование
Rscript scripts/04_forecasting.R

# 6. Структурные сдвиги
Rscript scripts/05_structural_breaks.R
```

---

## Преимущества подхода

| Элемент | Обоснование |
|---------|------------|
| **SQLite** | Прямой доступ к 1.2M записей из R без Excel |
| **fixest** | Быстрый TWFE для 90 регионов × 68 мес. = 6 120 obs |
| **bsts** | Причинный вывод + наукастинг + учёт структурных сдвигов |
| **fable** | Множожественная оценка ARIMA/ETS для 85 регионов одновременно |
| **marginaleffects** | Корректная интерпретация в моделях с FE и логарифмами |
| **strucchange** | Выявление сдвигов: COVID, льготная ипотека, ставка |

## Ограничения данных

| Проблема | Влияние | Решение |
|----------|---------|---------|
| permits_flow только с 2024-01 | Короткий ряд (31 obs) | Добавить косвенный proxy из stock |
| mortgage: 32 obs | Недостаточно для ARIMA | Использовать как регрессор в BSTS |
| Цены квартальные, ДДУ месячные | Разные частоты | MIDAS-регрессии или агрегация |
| Нет данных до 2020 (DOM.RF) | Длинные ряды только цены | Совместить с Росстат 2000–2023 |
| stock_krt имеет прогнозы до 2033 | Нереальные нули | Фильтровать date <= 2026-08 |