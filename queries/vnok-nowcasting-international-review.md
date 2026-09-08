---
title: "Международный опыт nowcasting инвестиций в основной капитал (GFCF): обзор литературы"
created: 2026-09-08
updated: 2026-09-08
type: query
tags: [nowcasting, GFCF, investment, MIDAS, DFM, MF-VAR, machine-learning, literature-review]
sources: [deleg_64c9f9c5, queries/vnok-nowcasting-design]
confidence: high
---

# Международный опыт nowcasting GFCF/инвестиций

Собрано делегатом (OpenAlex + web, 2026-09-08) для [[queries/vnok-nowcasting-design|дизайна ВНОК/ИКВ]].

## Классы методов и ключевые работы

| Класс | Работы | Ключевой результат | Применимость к РФ |
|---|---|---|---|
| **Bridge** | Baffigi-Golinelli-Parigi 2004 (IJF, 537 цит.); Angelini et al. 2011 (J Forecasting, 247); ECB EB 2020 | факторный мост точнее традиционного; survey/soft-данные ценны | бенчмарк 1; hard/soft-разделение ЕЦБ → цемент (hard) + Wordstat (soft) |
| **MIDAS** | Ghysels et al. 2004/2006; Foroni-Marcellino-Schumacher 2015 (U-MIDAS); Kuzin et al. 2011 (IJF 27(2), 209 цит.) | **MIDAS лучше на 4–5 мес., MF-VAR — на 5–9** (Kuzin); R-пакет midasr | основной метод; U-MIDAS робаст при n=56 |
| **DFM** | Giannone-Reichlin-Small 2008 (REStat); Bańbura et al. 2013 (ECB WP 1564); Mariano-Murasawa 2003; Doz et al. 2011 | news-декомпозиция, ragged edge | бенчмарк на большом блоке; для 56 кв. — консервативно |
| **FAVAR** | Bernanke-Boivin-Eliasz 2005 (QJE); **Zubarev-Rybak 2022 (ЖНЭА)** — глобальные шоки ~80% динамики РФ | — | российский аналог есть; для ДКП-интерпретации, не для nowcast |
| **MF-VAR/BVAR** | Schorfheide-Song 2015 (JBES, +60% nowcast кв. частоты); Koop et al. 2019; Cimadomo et al. 2021 | Minnesota prior + MF | горизонт 5–9 мес. |
| **ML mixed-freq** | Sheng et al. 2026 (FRL, GFCF США); Dauphin et al. 2022 (IMF); Degiannakis 2021 (J Forecasting, фондовый индекс → квартальный GFCF) | DFM лучше в спокойные периоды, ML — на поворотных точках | обвал 2026Q1 = кейс для ML |
| **Firm-level** | Hong-Huang-Zhu 2026 (SSRN 6457199); Management Science 2025 (RMSE −70% vs RW) | cross-section без агрегации +17% | РСБУ/IFRS-блок (H-008) |
| **Российские** | **Макеева-Станкевич 2022 (ЭЖ ВШЭ)** — MIDAS/MIDAS+L1/MFBVAR по элементам использования ВВП вкл. валовое накопление; Станкевич 2020 (MFBVAR точнее MIDAS); Фокин 2023 (ЭЖ ВШЭ 27(3), MFBVAR > ARIMA); **Gareev 2020 (RJMF 79(1))** — ML для инвестиций РФ до 8 кв., boosting/RF > AR/RW и прогнозов МЭР; Поршаков et al. 2025 (SSRN, DFM ЦБ) | MFBVAR-лидер по Станкевичу/Фокину | **прямой прототип**: Макеева-Станкевич уже делает валовое накопление; Gareev — уже GFCF РФ |
| **Развивающиеся рынки** | Tarsidin et al. 2018 (Индонезия, DFM для потребления и инвестиций: **продажи цемента**, авто, электропотребление, кредиты, M1); Driver-Meade 2018 (survey-инвестиционные прогнозы) | цемент как предиктор инвестиций валиден кросс-страново | валидация цемент-прокси |

## Синтез для публикации (позиционирование)

1. **Каркас:** AR(1) бенчмарк (φ≈0.72 для ВНОК в пилоте) → bridge → MIDAS → DFM → MF-VAR → ML → ансамбль.
2. **Распределение по горизонтам (Kuzin et al. 2011):** MIDAS — nowcast текущего квартала (наш кейс), MF-VAR/DFM — 5–9 мес., ML — поворотные точки (2026Q1).
3. **Прямые аналоги регрессоров:** цемент = Tarsidin 2018; survey = Angelini 2011; эскроу-финансирование = финансовый канал Bańbura 2018 — **но эскроу как опережающий (lag2 +0.75) нигде не описан: это новизна** (подтверждает H-007 формулировку).
4. **Против кого пишем:** Gareev 2020 (ML уже для GFCF РФ, но без HF-эскроу и без фирменного блока), Макеева-Станкевич (MIDAS для ВН, но до эскроу-эпохи и без escrow-канала). Наш вклад: escrow-канал + firm-level блок + стресс-тест 2026Q1.

## Дополнения к стеку дизайна (принято в [[queries/vnok-nowcasting-design]])

- Добавить **MFBVAR** в бенчмарки (лидер российской литературы по Станкевичу 2020 / Фокину 2023)
- Добавить **Gareev 2020** как прямого предшественника для позиционирования новизны
- Уточнить горизонты: MIDAS для nowcast (0–1 кв.), MF-VAR для 5–9 мес., ML для поворотных точек

^[deleg_64c9f9c5 (deepseek-v4-pro:0813, 251s, OpenAlex+web); Kuzin et al. 2011 IJF; Gareev 2020 RJMF; Макеева-Станкевич 2022 ЭЖ ВШЭ; Tarsidin et al. 2018]