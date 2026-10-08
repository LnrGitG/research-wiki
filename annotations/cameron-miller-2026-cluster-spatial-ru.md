---
type: annotation
class: A
paper: "Cameron A.C., Miller D.L. (2026). Inference for Regression with Clustered or Spatially Correlated Data I: Framework and Clustering; II: Spatial Correlation. NBER Working Papers 35800 и 35801, октябрь 2026."
doi: "10.3386/w35800; 10.3386/w35801"
url: "https://www.nber.org/papers/w35800 ; https://www.nber.org/papers/w35801"
pdf: ""
tags: [econometrics, cluster-robust, spatial-hac, conley, standard-errors, DiD]
sources: [NBER Working Paper Series]
---

# Выписки: Cameron & Miller 2026 (NBER 35800 + 35801)

## Идентификация

- Авторы: A. Colin Cameron, Douglas L. Miller. Серия NBER WP, октябрь 2026.
  dois: 10.3386/w35800 (I), 10.3386/w35801 (II). Класс A (NBER, официальные
  страницы; PDF прямая загрузка блокирована 403 — тексты не извлечены,
  выписки по официальным абстрактам).
- Два companion-труда, «guide to empirical researchers»; преемники их
  классического «Practitioner's Guide to Cluster-Robust Inference» (JHR 2015).

## Что сказано (по абстрактам)

- Общая рамка (I): данные коррелированны внутри кластера и/или пространственно;
  положительная корреляция снижает информационное содержание наблюдений;
  без поправки стандартные ошибки занижены → CI уже, тесты over-reject.
- Часть I — кластерная инференция: методы с улучшенным конечным выборочным
  поведением, когда число кластеров невелико. Акцент: такие поправки
  «often necessary».
- Часть II — пространственная: когда корреляция затухает с расстоянием —
  методом по умолчанию служит spatial HAC Conley (1999); при высокой
  пространственной персистентности Conley работает плохо, нужны альтернативы.
  Важно контролировать пространственные тренды, иначе ложная корреляция.

## Оговорки

- Выписки сделаны по абстрактам официальных страниц (класс A), но числовые
  детали методов (конкретные поправки, симуляции) не извлечены — при
  использовании в дизайне эмпирики скачать PDF через доступный канал и
  дополнить выписки.