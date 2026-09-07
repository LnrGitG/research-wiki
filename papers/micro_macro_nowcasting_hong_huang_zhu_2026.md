---
title: "From Micro to Macro: Learning Real-Time Economic Signals from Firm-Level Accounting Data"
authors: [Yongmiao Hong, Naijing Huang, Shijie Zhu]
year: 2026
type: working_paper
venue: SSRN (working paper, May 13, 2026)
url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6457199
source_pdf: raw/papers/micro_macro_nowcasting_hong_huang_zhu_2026.pdf
extracted_md: raw text in raw/papers/micro_macro_nowcasting_hong_huang_zhu_2026.txt
tags: [nowcasting, micro-to-macro, machine-learning, random-forest, firm-level-accounting, MIDAS, real-time-data, russia-adaptation]
date_added: '2026-09-07'
---

# From Micro to Macro: Learning Real-Time Economic Signals from Firm-Level Accounting Data

Hong, Y., Huang, N., Zhu, S. (2026). SSRN 6457199, 13.05.2026, 22 с.

## Аннотация (сжатая)

Предложен подход *micro-to-macro*: machine learning работает напрямую с полной кросс-секцией квартальных бухгалтерских данных 21 061 публичной компании США (без агрегирования в рыночные/отраслевые индикаторы или факторы DFM) для nowcast реального роста ВВП США. Выборка OOS: 2000:Q3–2024:Q2. Три фирменные переменные: RNOA (доходность чистых операционных активов), Growth (рост выручки), Earnings (прибыль). Алгоритмы: RF (лучший), и др. ML.

## Ключевые результаты (точные значения)

| Сравнение | Снижение RMSE |
|---|---|
| micro-to-macro vs random walk (RW) | **>70%** (avg RMSE ratio 0,287–0,311) |
| Лучший спек: RNOA–Earnings vs RW | 0,287 (−71%) |
| vs агрегированные market-level | −25,13% |
| vs sector-level агрегаты | −15,21% |
| vs DFM-факторы | −46,52% |
| vs mixed-frequency макро+фин. предикторы | −15,99% (комбинация: −16,18%, прирост ≈0) |

- RF — лучший алгоритм во всех спеках (dense non-linear: взаимодействие фирм).
- Раннее в квартале (t=−8, >40% фирм ещё не отчитались) точность ≈ t=0 — сигнал уже содержится в ранних репортёрах (bellwether-фирмы; granular view: Carvalho–Gabaix 2013; network view: Acemoglu et al. 2012).
- Высокая волатильность (GFC, COVID): средняя абсолютная ошибка micro-to-macro на **65,21%** ниже RW; в эпизодах отрицательного роста ошибка переоценки 7,39% против 16,53% у RW.
- Робастность: номинальный ВВП (−~70% RMSE) и реальный GDI (Nalewaik 2010) — результаты сохраняются.

## Feature importance

- Гетерогенность по фирмам и датам отсечения; overlap топ-200 при t=−8 и t=0 — только 99 фирм.
- По характеристикам: **крупные активы, низкий book-to-market, низкий leverage** → выше вклад (growth-профиль, меньшая чувствительность к финансированию).
- По отраслям (GICS): industrials, utilities, consumer discretionary; динамика: industrials доминируют в начале выборки, utilities растут после GFC и к ~2013 становятся лидером.

## Механизмы

- RNOA — микро-прокси совокупной производительности (операционная эффективность на вложенный капитал); Earnings — широкая итоговая прибыль (выручка, издержки, фин. условия). Каналы прогнозной силы прибыли: совокупная корпоративная прибыль, инфляция (Shivakumar–Urcan 2017), ДКП, рынок труда.
- Early reporters = bellwether; информация частично замещает поздние отчёты (Foster 1981).

## Релевантность для research-wiki (адаптация к РФ)

1. **Конкуренция с Midas-nowcasting контуром**: фирменные квартальные данные могут доминировать над mixed-frequency макронабором (−15,99% RMSE у micro-to-macro vs макро+фин. предикторов; комбинация даёт ≈0 прироста). Стоит протестировать как конкурентный baseline к композиту Wordstat (0,63 lead-1m vs YoY СМР).
2. **РФ-ограничения репликации** (оценка 2026-09-07): ГИР БО (bo.nalog.gov.ru) — годовая БФО для большинства (квартальная только для КФО-эмитентов); лаг до 3 мес. + аудит до конца след. года → точная репликация real-time невозможна. Реалистичная адаптация: годовая фирменная панель (ОКВЭД 41/68) → прогноз годовой ВДС строительства, честный real-time vintage-дизайн по полю actualBfoDate. Публичный JSON-поиск работает без ключа; булк — платная подписка REST API ФНС.
3. **Структурный инсайт**: низкий leverage → выше прогнозная важность — консистентно с контуром финансового здоровья девелоперов (Эксперт РА 08.2026: EBITDA/%% ≤1,5х у большинства; чистый долг/EBITDA >4,0x в среднесрочной перспективе).
4. Для РФ: RNOA мапится на операционную рентабельность из БФО (стр. 2200/активы), Earnings — на чистую прибыль (стр. 2400); book-to-market недоступен без котировок (прокси — капитализация MOEX для листингованных девелоперов).

## Кросс-ссылки

- `baum-snow-han-2024-microgeography-housing-supply` — микроданные → агрегатный контур (симметричная логика micro-to-macro в пространстве, а не во времени).
- Эксперт РА «Жилищное строительство: под давлением» (13.08.2026) — фирменные метрики leverage/покрытия процентов как кандидатные фичи.
- Контур collect_panel.py (11 девелоперов) — панель-кандидат для пилота.
- Midas-nowcasting skill (класс-level playbook) — методологическая связка.