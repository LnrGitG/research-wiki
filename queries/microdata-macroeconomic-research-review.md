# Макроэкономические исследования с использованием микроданных компаний

**Дата:** 04.09.2026
**Цель:** обзор международных и отечественных исследований, использующих финансовые показатели компаний (микроданные) для макроэкономического прогнозирования / nowcasting / оценки трансмиссии монетарной политики

---

## I. Международные исследования: nowcasting ВВП через микроданные

### 1. Cui, Hong, Huang, Wang (2026) — Management Science
**«Forecasting GDP Growth Rates Using Accounting Earnings: A Large Panel Microdata Approach»**
- **Данные:** 21 061 публичная компания США, квартальная бухгалтерская отчётность (Compustat), ~40 лет
- **Метод:** microforecasting — панель бухгалтерской прибыли фирм → GDP. Модель ML на кросс-секции фирм
- **Результат:** RMSE снижен на **70%** vs random walk; на **17%** лучше моделей на агрегированных макроданных
- **Ключевой вывод:** гетерогенность фирм (размер, leverage, book-to-market) несёт макро-сигнал, теряемый при агрегации. Крупные фирмы, industrials, utilities, consumer discretionary — наиболее важны для nowcasting GDP
- **Релевантность:** прямой аналог нашего пайплайна — панель РСБУ девелоперов → nowcasting СМР/ВДС строительства
- **DOI:** 10.1287/mnsc.2025.01549

### 2. Hong, Huang, Zhu (2026) — SSRN
**«From Micro to Macro: Learning Real-Time Economic Signals from Firm-Level Accounting Data»**
- **Данные:** 21 061 публичная компания США, полный cross-section бухгалтерских данных
- **Метод:** ML (machine learning) напрямую на firm-level данных, без агрегации. Сохраняет heterogeneity и cross-firm interactions
- **Результат:** **17,35%** улучшение vs модели на агрегированных макро+финансовых предикторах. Признаки: крупные активы, низкий book-to-market, низкий leverage → большая важность для nowcasting GDP
- **Ключевой вывод:** «directly exploiting the full cross-section of accounting information» превосходит агрегацию. Состав отчётников меняется во времени, но nowcast стабилен
- **Релевантность:** методология — ML на panel firm-level данных, не агрегировать заранее
- **SSRN:** 6457199

### 3. Abdalla, Carabias, Patatoukas (2021) — Journal of Monetary Economics
**«The real-time macro content of corporate financial reports: A dynamic factor model approach»**
- **Данные:** поток квартальных отчётов публичных компаний США (real-time, weekly updates)
- **Метод:** dynamic factor model (Giannone et al., 2008) + accounting factors из отчётности (income statement, balance sheet, cash flows)
- **Результат:** еженедельно обновляемые accounting factors **incrementally relevant** для nowcasting компонентов ВВП (NIPA) — и продукт-, и доход-сторона
- **Ключевой вывод:** accrual basis accounting → forward-looking content. Гетерогенность timing публикаций → богатый поток данных в течение квартала
- **Релевантность:** модель DFM с accounting factors — прямо применима к нашему набору (РСБУ через bo.nalog + МСФО через Smart-Lab)
- **DOI:** 10.1016/j.jmoneco.2021.01.006

### 4. Babii, Ghysels, Striaukas (2024) — arXiv
**«Panel Data Nowcasting: The Case of Price-Earnings Ratios»**
- **Данные:** панель фирм с разными частотами данных (микс месячные/квартальные)
- **Метод:** structured ML regressions для nowcasting с mixed-frequency panel data
- **Результат:** nowcasting квартального GDP штатов США через employment data
- **Релевантность:** mixed-frequency — наш случай (квартальная МСФО, годовая РСБУ, месячные СМР/ИФО)
- **arXiv:** 2307.02673

### 5. Asriyan, Kohlhas (2024) — BSE
**«The Macroeconomics of Firm Forecasts»**
- **Данные:** I/B/E/S-Compustat panel — managerial forecasts (микроданные прогнозов менеджеров)
- **Метод:** extraction of macro signals from firm-level managerial expectations
- **Релевантность:** аналог — использование ИФО (индексов финансовой отчётности) и опросов Росстата

---

## II. Трансмиссия монетарной политики через микроданные

### 6. ECB Working Papers — Monetary Policy Transmission with Firm-Level Data
- **Bundesbank DP 20/2001:** «Firm Investment and Monetary Policy Transmission in the Euro Area» — micro data позволяют измерять user cost, sales, cash flow на уровне фирмы
- **Banque de France WP 933:** «Corporate debt structure and heterogeneous monetary policy» — firm-level data, bond market liquidity, credit risk
- **ECB WP (Jeantteau, Kohlhas):** «Heterogeneity in corporate debt structures and the transmission of monetary policy» — финансовые микроданные → трансмиссия через структуру долга фирм
- **Bank of Canada WP 2022-49:** «Monetary Policy, Credit Constraints and SME Employment» — firm-level financial statements → IRFs монетарной политики
- **Ключевой вывод:** микроданные выявляют гетерогенность трансмиссии — малые фирмы / высокие финансовые ограничения → сильнее реагируют на шоки ставки
- **Релевантность:** прямая аналогия — Эталон/Талан (высокий долг, EBITDA/проценты ≤1×) реагируют на рост ставки сильнее, чем ПИК/А101 (низкий долг, высокая маржа)

### 7. IMF WP 24/43 — «Is Inflation Good for Business? The Firm-Level Impact of Inflation Shocks in the Baltics»
- **Данные:** large panel of firm-level data, 1997–2021, страны Балтии
- **Метод:** identification of inflation shocks → firm-level responses (продажи, прибыль, занятость)
- **Релевантность:** аналог — оценка воздействия строительной инфляции (7,6% в 2025) на девелоперов через панель

### 8. O'Neill, Velasco (2026) — BDE WP 2627 (уже в wiki)
**FABART** — непараметрический FAVAR с BART. 109 переменных, региональная гетерогенность. Непараметрическая трансмиссия — нелинейность emerge из данных.
- **Релевантность:** метод для nowcasting СМР с нелинейной трансмиссией ключевой ставки (порог ~10% по Сергиенко)

---

## III. Теоретическая база: «granular origins»

### 9. Gabaix (2011) — Econometrica
**«The Granular Origins of Aggregate Fluctuations»**
- **Теория:** в экономике с fat-tailed distribution фирм (закон Ципфа) индивидуальные шоки крупных фирм не диверсифицируются и объясняют значительную часть агрегированных флуктуаций
- **Результат:** ~1/3 вариации роста ВВП США объясняется шоками топ-100 фирм
- **Релевантность:** топ-10 девелоперов РФ (ПИК, Самолёт, ЛСР, Эталон, А101) могут объяснять значительную часть вариации СМР в строительстве. Наша панель из 14 компаний — «granular» подход

### 10. Carvalho, Gabaix (2013) — NBER
**«The Great Diversifications and Their Undoing»**
- **Теория:** диверсификация шоков снижается при концентрации отраслей → крупные фирмы/сектора → больше агрегированные флуктуации
- **Релевантность:** концентрация в строительстве РФ растёт (топ-10 девелоперов → 45% объёма) → granular effects усиливаются

---

## IV. Отечественные исследования и данные

### 11. ЦБ РФ — Мониторинг предприятий
- **Данные:** ежегодная **финансовая анкета** — бухгалтерский баланс + ОПУ предприятий нефинансового сектора. Опережающая официальная статистику
- **Метод:** агрегация микроданных → индикаторы бизнес-климата (ИБК), отраслевые сопоставления
- **Релевантность:** ЦБ использует микроданные для nowcasting ВВП, но **не публикует** firm-level данные. Наш пайплайн (bo.nalog → РСБУ → панель) — внешняя альтернатива
- **URL:** cbr.ru/dkp/mp/

### 12. ФНС — bo.nalog.gov.ru (наш скрипт collect_rsbu.py)
- **Данные:** БФО всех юрлиц РФ (баланс, ОФР) через API `/nbo/organizations/{id}/bfo/`
- **Охват:** 10 девелоперов, 2021–2025, JSON-данные баланса и ОФР
- **Релевантность:** единственный бесплатный публичный источник firm-level финансовых данных в РФ. Наш скрипт уже работает

### 13. tochno.st — Российская база бухгалтерской отчётности
- **Данные:** финансовые отчёты **всех** действующих компаний РФ за 2011–2025
- **Формат:** структурированный датасет, готовый для анализа
- **Релевантность:** потенциальный источник для расширения панели за пределы 10–14 девелоперов → все строительные компании (ОКВЭД F)
- **URL:** tochno.st/datasets/rfsd

### 14. Росстат — Наукастинг ВВП
- **Метод:** первая оценка ВВП на основе «оперативной статистической отчётности предприятий» — по сути, агрегированные микроданные
- **Q1 2026:** ВВП −0,2%, строительство — главный драйвер снижения
- **Релевантность:** Росстат уже использует микроданные для nowcasting, но на агрегированном уровне. Наш подход — firm-level granular

### 15. HSE / ЦЭМИ — Наукастинг ВВП России
- **Диссертация HSE:** «Наукастинг и краткосрочное прогнозирование развивающейся экономики» — методы nowcasting для РФ
- **ЦЭМИ:** «Наукастинг и прогнозирование ВВП России и его компонентов» (PE 2025) — вероятностный nowcasting российского ВВП
- **Релевантность:** отечественные методологии nowcasting, но без firm-level данных — наш вклад

### 16. Петрова, Трунин — RANEPA
- **Данные:** интернет-данные (поисковые запросы) для прогнозирования макропоказателей
- **Релевантность:** не firm-level, но дополнительный источник nowcasting (Wordstat → СМР, наш композит S2+S3+S4+S5)

---

## V. Сводная таблица: методы и данные

| # | Исследование | Данные | Метод | Macro-результат | Firm-level? |
|---|---|---|---|---|---|
| 1 | Cui et al. (2026) | 21K фирм США, accounting | ML panel | GDP nowcast, RMSE −70% | ✅ |
| 2 | Hong et al. (2026) | 21K фирм США, accounting | ML cross-section | GDP nowcast, +17% vs macro | ✅ |
| 3 | Abdalla et al. (2021) | Поток отчётов США | DFM + accounting factors | NIPA nowcast, incremental | ✅ |
| 4 | Babii et al. (2024) | Panel mixed-frequency | Structured ML | State GDP nowcast | ✅ |
| 5 | ECB/Bundesbank | Firm-level euro area | VAR/IRF | Monetary transmission | ✅ |
| 6 | IMF WP 24/43 | Firm-level Baltics | Panel IRF | Inflation shock effects | ✅ |
| 7 | O'Neill, Velasco (2026) | 109 vars, regional | FABART (BART+FAVAR) | Nonlinear oil transmission | Partial |
| 8 | Gabaix (2011) | Top-100 firms USA | Granular theory | 1/3 GDP variance | ✅ |
| 9 | ЦБ РФ мониторинг | Финансовая анкета | Aggregation | Business climate | ✅ (closed) |
| 10 | bo.nalog (наш скрипт) | 10 девелоперов РСБУ | API + JSON panel | Строительная панель | ✅ |
| 11 | tochno.st | Все компании РФ 2011–2025 | Dataset | Потенциал nowcasting | ✅ |
| 12 | Росстат | Оперативная отчётность | Aggregation | ВВП nowcast | ❌ (агрегат) |

---

## VI. Применимость к нашему пайплайну

| Принцип из литературы | Применение в research-wiki |
|---|---|
| **Micro-to-macro** (Cui, Hong): firm-level → GDP | Панель 14 девелоперов → nowcasting СМР/ВДС строительства |
| **Не агрегировать заранее** (Hong): сохранять heterogeneity | Записи панели: company × period × metric, не средние по отрасли |
| **Accounting factors** (Abdalla): DFM с factors из отчётности | Факторы из РСБУ (выручка, долг, прибыль) + МСФО (EBITDA, D/E) |
| **Mixed-frequency** (Babii): квартальная МСФО + годовая РСБУ + месячные СМР | Наша панель: смешанные частоты → structured ML |
| **Granular origins** (Gabaix): крупные фирмы → агрегат | Топ-10 девелоперов = 45% объёма строительства → granular effect |
| **Monetary transmission** (ECB): firm-level → heterogeneity ответа на ставку | Эталон/Талан (D/E 6,8–12,6×) vs ПИК/А101 (D/E 0,8–1,5×) |
| **Nonlinear transmission** (FABART): ставка ~10% — порог | Непараметрическая оценка порога стабилизации (Сергиенко) |
| **Russian data** (bo.nalog, tochno.st) | Расширение панели: 14 → все строительные компании ОКВЭД F |

### Предлагаемая архитектура nowcasting СМР

```
Layer 1: Firm-level data (bo.nalog API + Smart-Lab + tochno.st)
  → 14+ девелоперов, РСБУ + МСФО, 2021–2026Q2

Layer 2: Sectoral data (Росстат: ИФО, занятость, цены материалов)
  → месячные/квартальные, 2017–2026

Layer 3: Macro/financial (ключевая ставка, ипотека, эскроу)
  → месячные, 2017–2026

Layer 4: Model (DFM with accounting factors / FABART / ML panel)
  → Nowcasting СМР (месячный) / ВДС строительства (квартальный)
```