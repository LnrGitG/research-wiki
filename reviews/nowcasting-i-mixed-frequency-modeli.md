---
title: "Nowcasting и mixed-frequency модели — обзор кластера"
type: review
created: 2026-07-27
updated: 2026-07-27
tags: [review, nowcasting, mixed-frequency, MIDAS, BVAR, entropic-tilting, DFM]
cluster_size: 8
---

# Nowcasting и mixed-frequency модели — обзор кластера

## О кластере

Кластер объединяет 6 оригинальных академических работ (2014–2021 гг.) по nowcasting и mixed-frequency моделированию в макроэкономике. Все статьи используют байесовские векторные авторегрессии (BVAR) или динамические факторные модели (DFM) для оперативного прогнозирования ключевых макропоказателей — ВВП, инфляции, безработицы — в условиях разнородной частоты данных, асинхронных выпусков и «рваных краёв» (ragged edge) информационных наборов. Методологически кластер делится на три направления.

**Первое направление** — entropic tilting (наклонение по относительной энтропии): методы комбинации BVAR-прогнозов с внешними nowcast-ами из опросов или других моделей. Три работы (Tallman & Zaman 2020; Krüger, Clark & Ravazzolo 2017/2014; Koop et al. 2019) показывают, что наклонение плотности BVAR под moment conditions внешних прогнозов систематически улучшает точность как point, так и density forecast. Tallman & Zaman расширяют KCR (2017) до long-horizon наклонения, Krüger et al. добавляют наклонение по дисперсии, а Koop et al. адаптируют tilting для агрегационного ограничения (национальный ВВП = взвешенная сумма региональных GVA).

**Второе направление** — large BVAR с mixed-frequency: Cimadomo et al. (2021) сравнивают три стратегии — L-BVAR (латентные низкочастотные процессы с фильтром Калмана), B-BVAR (blocking/stacking) и frequency mapping — и показывают, что все три конкурентоспособны с BLS Staff nowcast (DFM-based) и не уступают факторным моделям. Anttonen (2018) показывает, что seasonal BVAR с дашбидами Google Search даёт modest improvements для безработицы в ЕС (28 стран), а оптимизация гиперпараметров через mode of posterior значительно превосходит rule-of-thumb.

**Третье направление** — региональный nowcasting с агрегационными ограничениями. Koop et al. (2019) создают long historical series annual regional GVA (1966–2016) для 11 регионов Великобритании и демонстрируют, что stacked mixed-frequency VAR с entropic tilting агрегационного ограничения позволяет обновлять annual nowcasts quarterly, значительно сокращая lag официальной статистики ONS (11 месяцев → flash-оценки за 2 месяца).

Две работы из инвентаря — `combining-survey-long-run-forecasts-and-nowcasts.md` (презентация Tallman & Zaman) и `wp-1439-using-entropic-tilting-to-combine-BVAR-Forecats-with-external-nowcasts-pdf.md` (working paper версия Krüger et al.) — являются дубликатами оригинальных публикаций и не добавляют нового контента. RBNZ working paper (rbnz-2025-gdp-nowcasting-dfm) заблокирован сайтом банка, текст не извлечён; по названию — это GDP nowcasting DFM от Резервного банка Новой Зеландии. В таблице ниже эти 3 работы учтены как дубликаты/недоступные.

## Сводная таблица

| Статья | Тип | Метод | Данные/период | Ключевой результат |
|---|---|---|---|---|
| [[papers/Tallman-Zaman-IJF-2020-Combining-survey-long-run-forecasts-and-nowcasts-with-BVAR]] | Реферируемая статья (Int. J. Forecasting, 2020) | Relative entropy tilting BVAR + SPF long-run + nowcast; фикс-параметр VAR, TVP-VAR; 10 спецификаций | США; SPF; 1960–2018+ | Гибридные прогнозы статистически значимо точнее; наибольший выигрыш для инфляции и ставки; spillover-эффекты на нетилированные переменные; простые VAR с post-WII данных конкурентоспособны с TVP-VAR |
| [[papers/Using-Entropic-Tilting-to-Combine-BVAR-Forecasts-With-External-Nowcasts]] | Реферируемая статья (JBES, 2017; WP 14-39, 2014) | Entropic tilting BVAR (со сток. волатильностью) + SPF survey nowcasts и model-based nowcasts; наклонение по mean и по mean+variance | США; SPF + bridging eq.; 1970–2013 | Tilting по mean+variance точнее по density, чем mean only; выигрыши для persist variables (безработица, ставка) сохраняются до 5 кварталов; SPF лучше для ВВП/инфляции, model-based для безработицы/ставки |
| [[papers/Koop-etal-JRSSA2019-UK-regional-nowcasting-using-a-mixed-frequency-Vector-Autoregressive]] | Реферируемая статья (JRSS-A, 2019) | Stacked mixed-frequency VAR + entropic tilting агрегационного ограничения + multivariate stochastic volatility | UK 11 регионов; annual GVA (1966–2016) + quarterly UK GVA | Stacked VAR с tilting агрегационного ограничения → flash-оценки региональных GVA за ~2 мес. вместо 11 мес.; точность nowcasts значительно выше initial unconditional forecasts |
| [[papers/Paper-CGLMS-Mixed-Frequency-BVAR-Nowcasting]] | Рабочий документ (Cimadomo et al., 2021) | Сравнение трёх BVAR-стратегий: L-BVAR (latent+Kalman), B-BVAR (blocking/stacking), frequency mapping; scenario analysis | США; 18 переменных; 2005–2019 real-time | Все три BVAR-варианта точны, коррелируют с NY Fed Staff nowcast; различия только в первых неделях квартала; BVAR конкурентоспособен с DFM для big data nowcasting |
| [[papers/Nowcasting-the-Unemployment-Rate-in-the]] | Рабочий документ (Anttonen, ETLA WP 62, 2018) | Seasonal BVAR с monthly dummies + Google Search index; mode of posterior для гиперпараметров | 28 стран ЕС; Eurostat + Google Trends; 2000–2018 | Google Search даёт modest improvements; mode-of-posterior гиперпараметры → значимое улучшение out-of-sample точности vs rule-of-thumbMinnesota priors |
| [[papers/rbnz-2025-gdp-nowcasting-dfm]] | Working paper (RBNZ) | Dynamic Factor Model для GDP nowcasting (текст недоступен) | Новая Зеландия | Информация недостаточна (сайт RBNZ заблокировал доступ) |
| [[papers/combining-survey-long-run-forecasts-and-nowcasts]] | **Дубликат**: презентация Tallman & Zaman (BoE 2018) | — | — | Содержательно совпадает с [[papers/Tallman-Zaman-IJF-2020-Combining-survey-long-run-forecasts-and-nowcasts-with-BVAR]]; самостоятельной ценности не имеет |
| [[papers/wp-1439-using-entropic-tilting-to-combine-BVAR-Forecats-with-external-nowcasts-pdf]] | **Дубликат**: WP-версия Krüger et al. (FRB Cleveland WP 14-39) | — | — | Содержательно совпадает с [[papers/Using-Entropic-Tilting-to-Combine-BVAR-Forecasts-With-External-Nowcasts]]; дубликат рабочего документа перед публикацией в JBES |

## Основные выводы по темам

### Nowcasting с entropic tilting и combining forecasts

Entropic tilting — наиболее зрелый метод кластера. KCR (2017) показал базовую идею: наклонить BVAR-плотность по moment conditions survey nowcast. Krüger et al. (2017) расширили на variance tilting и model-based nowcasts, показав, что комбинация mean+variance даёт дополнительную плотность. Tallman & Zaman (2020) добавили long-horizon tilting для устранения structural break и bias в long-run прогнозах фикс-параметр VAR. Все три показывают статистически значимые улучшения point и density accuracy. Ключевой вывод: spillover-эффекты — переменные, не подвергшиеся direct tilting, тоже улучшаются через динамические связи в BVAR. Для persist-переменных (безработица, ставка) выигрыши сохраняются до 5 кварталов; для less-persistent (ВВП, инфляция) затухают быстрее.

Практическое значение: entropic tilting — non-parametric, computationally light альтернатива сложным TVP-VAR и DSGE. Простые фикс-параметр VAR + tilting конкурентоспособны с TVP-VAR (Tallman & Zaman), что критично для emerging markets с короткими рядями.

### Mixed-frequency VAR (stacked/latent)

Cimadomo et al. (2021) — систематическое сравнение трёх подходов mixed-frequency BVAR: L-BVAR (latent state + Kalman), B-BVAR (blocking/stacking) и frequency mapping. Главный вывод: все три подхода дают comparable accuracy; различия только в первых неделях квартала. Это говорит о том, что mixed-frequency данные ценны именно для timeliness, а не для структурных различий. BVAR конкурентоспособен с DFM (стандартным инструментом nowcasting) в big-data settings с 18+ переменными.

Koop et al. (2019) демонстрируют reverse frequency mismatch: many low-frequency (regional) variables to nowcast using one high-frequency (aggregate) indicator. Stacked VAR с entropic tilting агрегационного ограничения — элегантное решение, позволяющее «раскладывать» национальный рост по регионам в режиме near-real-time. Создание long historical series (1966–2016) для regional GVA — значимый data contribution.

### Использование внешних данных (Google Search, SPF)

Anttonen (2018) — единственная работа кластера, интегрирующая big data non-traditional data (Google Search index) в BVAR nowcasting. Google данные дают modest (но статистически значимые) улучшения. Подтверждается вывод из более широкой литературы: «soft» данные не заменяют «hard» макростатистику, но добавляют margin signal. Отмечено, что это первая работа, тестирующая Google data в BVAR-контексте.

Оптимизация гиперпараметров Minnesota priors через mode of posterior (а не rule-of-thumb) значимо улучшает точность — важный практический результат для репликации.

### Региональный nowcasting и агрегационные ограничения

Koop et al. (2019) — единственная работа, работающая на уровне регионов. Проблема «rear-view mirror»: региональные GVA публикуются с lag 11 месяцев, а quarterly UK GVA — с lag ~2 мес. Стек VAR + entropic tilting агрегационного ограничения позволяет «раскладывать» национальный рост на регионы в реальном времени, сокращая lag с 11 мес. до ~2 мес. Агрегационное ограничение (национальный GVA = взвешенная сумма региональных) реализовано через entropic tilting, что теоретически оптимально (минимизация KL-divergence при constraint).

### Противоречия и пробелы

**Противоречия и дебаты:**

1. **BVAR vs DFM для nowcasting.** Стандартный консенсус — DFM (factor models) are tool of choice for big data nowcasting (Aruoba et al. 2009; Banbura et al. 2011). Cimadomo et al. (2021) бросают вызов: large BVAR with Bayesian shrinkage конкурентоспособен с DFM и даёт additional benefits — dynamic heterogeneity (shocks affect variables with leads/lags, не одновременно), nonstationary data without differencing, richer structural analysis. Однако различия в точности между методами минимальны, что говорит: оба работают, выбор зависит от дополнительных задач (structural analysis vs pure nowcasting).

2. **Fixed-parameter VAR + tilting vs TVP-VAR.** Tallman & Zaman (2020) показывают, что простые VAR + entropic tilting конкурентоспособны с TVP-VAR, особенно для инфляции. Это оспаривает доминирование TVP-VAR для structural change. Контраргумент: TVP-VAR captures structural breaks endogenously, тогда как tilting — exogenous/semi-exogenous adjustment. Комбинация обоих подходов не исследована.

3. **Google data: signal или noise?** Anttonen (2018) находит modest improvements — это соответствует общей литературе (Choi & Varian 2012, Tuhkuri 2016), где «soft» данные редко превосходят «hard» макростатистику. Однако вопрос о causal link vs spurious correlation остаётся открытым: Google search отражает беспокойство по поводу безработицы, а не саму безработицу.

**Пробелы:**

1. **Жилищная экономика отсутствует.** Ни одна из работ кластера не моделирует housing market, house prices, housing investment или construction — ключевые переменные жилищной экономики. Nowcasting применяется к aggregate GDP, inflation, unemployment, regional GVA, но не к housing-specific indicators.

2. **Нет работы с ragged edge + low-frequency housing data.** Regional housing data (ввод, цены, транзакции) — низкочастотные и публикуются с лагами. Методология Koop et al. (2019) для regional GVA могла бы быть напрямую применена к regional housing, но таких исследований в кластере нет.

3. **RBNZ-статьи недоступны.** RBNZ working paper заблокирован, и его вклад (возможно, DFM for NZ GDP) не проанализирован. Это ослабляет кластер, так как NZ — частый case study для nowcasting (RBNZ — пионер DFM nowcasting с 2000-х).

4. **Не explored: combining BVAR with tilting в смешанной частоте.** Не встречалось работ, которые одновременно используют stacked mixed-frequency VAR + entropic tilting external forecasts. Koop et al. — только tilting агрегационного ограничения; Krüger et al. — только tilting external forecasts. Комбинация двух идей — перспективное направление.

5. **Нет оценки in-sample vs real-time.** Большинство работ показывают out-of-sample оценки, но few compare real-time vs latest-vintage. Koop et al. стараются использовать first-release data, что правильно, но для housing — ситуация ещё хуже с revisions.

## Что читать первым (топ-5)

1. [[papers/Using-Entropic-Tilting-to-Combine-BVAR-Forecasts-With-External-Nowcasts]] — фундаментальная статья по entropic tilting: полная методология, mean+variance, survey vs model-based nowcasts, реальные улучшения точности. Лучший вход в тему combining forecasts.

2. [[papers/Tallman-Zaman-IJF-2020-Combining-survey-long-run-forecasts-and-nowcasts-with-BVAR]] — расширение tilting до long-horizon; систематическое сравнение 10 BVAR-спецификаций; практический вывод: простые VAR + tilting > сложные TVP-VAR для многих задач.

3. [[papers/Paper-CGLMS-Mixed-Frequency-BVAR-Nowcasting]] — систематическое сравнение трёх mixed-frequency BVAR стратегий; BVAR конкурентоспособен с DFM. Лучшее введение в architecture choices large BVAR nowcasting.

4. [[papers/Koop-etal-JRSSA2019-UK-regional-nowcasting-using-a-mixed-frequency-Vector-Autoregressive]] — уникальный regional nowcasting с агрегационными ограничениями; entropic tilting для structural constraints; directly relevant для регионального анализа жилищной экономики.

5. [[papers/Nowcasting-the-Unemployment-Rate-in-the]] — применение Google data в BVAR; оптимизация гиперпараметров; seasonal BVAR для non-adjusted series. Полезно для non-traditional data integration.

## Связанные страницы

- [[concepts/econometric-models-housing-market]]
- [[concepts/regionalnaya-differenciaciya]]
- [[concepts/transmisionnyi-mehanizm-dkp-zhile]]
- [[papers/Zubarev-Otsenka-vliyaniya-globalqnykh-shokov-na-rossiyskuyu-ekonomiku-i-naukasting-VVP-v-ramkakh-fak]] — FAVAR for Russia nowcasting
- [[papers/naukasting-i-prognozirovanie-osnovnyh-rossiyskih-makroekonomicheskih-pokazateley-s-pomoschyu-mfbvar-]] — MFBVAR для России (критически релевантно для моста к жилищной экономике)