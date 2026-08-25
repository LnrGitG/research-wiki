# Официальное использование данных поисковых запросов (Google Trends / Яндекс Вордстат) статистическими ведомствами и центробанками

Сводка для исследования по наукастингу стройки/ввода жилья на основе индекса поисковых запросов (Яндекс Вордстат, 12 тем).
Дата сбора: 25.08.2026. Все ссылки проверены на доступность.

---

## 1. Банк Испании (Banco de España) — пионер официального использования поисковых данных
- **Организация:** Banco de España
- **Год начала:** 2012
- **Целевой показатель:** безработица (заявки на пособия), туризм, продажи автомобилей — опережающие индикаторы
- **Метод:** Google Trends (поисковые запросы) → опережающие индикаторы; сравнение с официальными рядами
- **Документ:** Artola C., Galán E. "Tracking the future on the web: construction of leading indicators using internet searches", Documentos Ocasionales No. 1203, 2012
- **Ссылка:** https://www.bde.es/webbde/SES/Secciones/Publicaciones/PublicacionesSeriadas/DocumentosOcasionales/12/Fich/do1203e.pdf
- **Статус:** исследование/эксперимент (рабочий документ, 74+ цитирований)

## 2. Банк Англии (Bank of England) — первый официальный обзор поисковых данных
- **Организация:** Bank of England
- **Год начала:** 2011
- **Целевой показатель:** рынок труда (безработица) и рынок жилья Великобритании
- **Метод:** Google Insights/Google Trends как дополнительные индикаторы к опросам; оценка прироста информации
- **Документ:** McLaren N., Shanbhogue R. "Using internet search data as economic indicators", Quarterly Bulletin 2011 Q2, pp. 134–140
- **Ссылка:** https://www.bankofengland.co.uk/quarterly-bulletin/2011/q2/using-internet-search-data-as-economic-indicators
- **Статус:** исследование (Quarterly Bulletin — официальное издание; ~395 цитирований)

## 3. Банк Италии (Banca d'Italia) — наукастинг безработицы
- **Организация:** Banca d'Italia
- **Год начала:** 2012
- **Целевой показатель:** уровень безработицы США (модель-прототип для Италии)
- **Метод:** Google job-search index (запросы о поиске работы) в моделях наукастинга
- **Документ:** D'Amuri F., Marcucci J. "The predictive power of Google searches in forecasting unemployment", Temi di discussione No. 891, 2012 (позже — International Journal of Forecasting, 2017)
- **Ссылка:** https://www.bancaditalia.it/pubblicazioni/temi-discussione/2012/2012-0891/index.html
- **Статус:** исследование (рабочая серия)

## 4. ФРС Чикаго (Federal Reserve Bank of Chicago) — Google Trends для заявок на пособия
- **Организация:** Federal Reserve Bank of Chicago
- **Год начала:** 2022 (публикация; работа велась с ~2019)
- **Целевой показатель:** первичные заявки на пособие по безработице (initial UI claims) в реальном времени
- **Метод:** Google Trends (тема "unemployment") + эластичность по ураганам; прогноз в реальном времени
- **Документ:** Aaronson D., Brave S., Butters R.A., Fogarty M., Sacks D.W. "Forecasting unemployment insurance claims in realtime with Google Trends", International Journal of Forecasting 38(2), 2022
- **Ссылка:** https://www.sciencedirect.com/science/article/abs/pii/S0169207021000649
- **Статус:** исследование (отмечено в обзоре МВФ 2026 как эксперимент ФРС Чикаго)

## 5. Бундесбанк (Deutsche Bundesbank) — Google Trends в еженедельном индексе активности
- **Организация:** Deutsche Bundesbank
- **Год начала:** 2020
- **Целевой показатель:** еженедельная экономическая активность Германии (Weekly Activity Index, WAI)
- **Метод:** 3 из 9 высокочастотных индикаторов WAI — Google Trends: "unemployment", "short-time work", "state support"; PCA (EM-алгоритм) на смешанных частотах
- **Документ:** Eraslan S., Götz T. "An unconventional weekly economic activity index for Germany", Bundesbank Technical Paper, 2020; методология на сайте
- **Ссылка:** https://www.bundesbank.de/en/statistics/economic-activity-and-prices/weekly-activity-index/methodology-833982
- **Статус:** ПРОДАКШН (публикуется еженедельно на сайте Бундесбанка; помечен как experimental measure)

## 6. ОЭСР (OECD) — Weekly Tracker на Google Trends
- **Организация:** OECD (Economics Department)
- **Год начала:** 2020
- **Целевой показатель:** еженедельный трекер роста ВВП для 46 стран ОЭСР и G20
- **Метод:** Google Trends (категории + темы, с коррекцией долгосрочного смещения), нейросеть, Shapley-интерпретация; значимые темы: "bankruptcies", "economic crisis", "investment", "luggage", "mortgage"
- **Документ:** Woloszko N. "Tracking activity in real time with Google Trends", OECD Economics Department Working Papers No. 1631, 2020
- **Ссылка:** https://www.oecd.org/en/publications/tracking-activity-in-real-time-with-google-trends_6b9c7518-en.html
- **Статус:** ПРОДАКШН (Weekly Tracker публикуется еженедельно)

## 7. Резервный банк Индии (RBI) — наукастинг недвижимости (ближайший аналог кейса исследователя)
- **Организация:** Reserve Bank of India
- **Год начала:** 2017 (публикация 2018)
- **Целевой показатель:** квартальный рост продаж компаний сектора недвижимости (real estate sales growth)
- **Метод:** Google Trends (отбор ключевых слов LARS-EN, бутстрап для шума выборки) + динамическая факторная модель (DFM, Giannone et al. 2008) с jagged edge; сравнение с моделью без Google-индекса
- **Документ:** Mitra P., Sanyal A., Choudhuri S. "Nowcasting Real Estate Activity in India using Google Trend Data", RBI Occasional Papers Vol. 38, No. 1&2, 2017
- **Ссылка:** https://rbi.org.in/Scripts/bs_viewcontent.aspx?Id=3516
- **Статус:** исследование (официальная серия RBI; вывод: поисковые данные улучшают точность наукаста продаж недвижимости)

## 8. Банк России (ЦБ РФ) — QUIET: индикатор инфляционных ожиданий на Яндекс Вордстат
- **Организация:** Банк России
- **Год начала:** 2026 (публикация; данные с 2018)
- **Целевой показатель:** инфляционные ожидания домохозяйств (РФ и регионы), прогноз ИПЦ
- **Метод:** Яндекс Вордстат (основной источник) + сравнение с Google Trends; отбор тем, PCA, MIDAS/ARDL, панели по регионам; сравнение с инФОМ и Мониторингом предприятий
- **Документ:** Карпеко Ф. "QUIET: индикатор инфляционных ожиданий домохозяйств России и ее регионов на основе данных поисковых систем", Серия докладов об экономических исследованиях Банка России № 174, 2026
- **Ссылка:** https://www.cbr.ru/statichtml/file/194046/wp_174.pdf
- **Статус:** исследование (официальная серия ЦБ; вывод: снижает ошибку прогноза ИПЦ на коротких горизонтах, пригоден для наукастинга)

## 9. Банк России (ЦБ РФ) — ранняя работа по поисковым запросам (Яндекс)
- **Организация:** Банк России
- **Год начала:** 2017
- **Целевой показатель:** инфляционные ожидания населения России
- **Метод:** машинное обучение на данных поисковых запросов Яндекса (частотность запросов по темам)
- **Документ:** Голощапова И.О., Андреев М.Л. "Оценка инфляционных ожиданий российского населения методами машинного обучения", Вопросы экономики, 2017, № 6 (53+ цитирований)
- **Ссылка:** https://www.vopreco.ru/jour/article/view/313
- **Статус:** исследование (журнальная публикация сотрудников ЦБ)

## 10. Статистическое управление Финляндии (Statistics Finland) — Google Trends в наукастинге безработицы
- **Организация:** Statistics Finland
- **Год начала:** ~2018–2020
- **Целевой показатель:** безработица Финляндии (наукастинг), краткосрочная статистика отраслей
- **Метод:** Google Trends как вспомогательные данные в наукастинг-моделях; регулярная публикация ошибок прогноза для доверия
- **Документ:** Koskimäki T., Luomaranta H. "Experiences in the use of forecasting and nowcasting methods for official statistics", презентация на 51-й сессии UNSC, 02.03.2020
- **Ссылка:** https://unstats.un.org/unsd/statcom/51st-session/side-events/documents/20200302-2L-Finland.pdf
- **Статус:** эксперимент/пилот (внедрение в краткосрочную статистику)

## 11. Центральный банк Ирландии (Central Bank of Ireland) — Google Probabilities
- **Организация:** Central Bank of Ireland
- **Год начала:** 2016 (конференция), публикация 2019
- **Целевой показатель:** наукастинг макроэкономики (ВВП) еврозоны/Ирландии
- **Метод:** Dynamic Model Selection (DMS) с "Google probabilities" — вероятности переключения моделей управляются Google-переменными
- **Документ:** Koop G., Onorante L. "Macroeconomic Nowcasting Using Google Probabilities", Advances in Econometrics, 2019 (Onorante — Central Bank of Ireland)
- **Ссылка:** https://www.emerald.com/books/edited-volume/14909/chapter/86018820/Macroeconomic-Nowcasting-Using-Google
- **Статус:** исследование

## 12. Департамент предпринимательства, туризма и занятости Ирландии (IGEES) — Google Trends для туризма/ритейла/гостеприимства
- **Организация:** Department of Enterprise, Tourism and Employment (IGEES), Ирландия
- **Год начала:** 2025
- **Целевой показатель:** раннее предупреждение стресса в потребительских секторах (hospitality, retail, tourism) — спрос и предложение
- **Метод:** PCA-композиты из высокочастотных индикаторов, включая Google Trends (поисковые запросы по секторам, данные с 2017); fixed vs rolling window PCA; пороги "alarm"
- **Документ:** Fitzgerald K., Coates D. "Patterns of activity in Ireland's consumer-facing service sectors: An experimental application of the Principal Component Approach", IGEES Working Paper, December 2025
- **Ссылка:** https://enterprise.gov.ie/en/publications/publication-files/patterns-of-activity-in-irelands-consumer-facing-service-sectors-an-experimental-application-of-the-principal-component-approach.pdf
- **Статус:** эксперимент (заявлено как основа для постоянного мониторинга департамента)

---

## Дополнительно: Евростат и Росстат (big data, но НЕ поисковые запросы)

### Евростат — web-scraped данные по рынку жилья
- **Год:** 2026 (рабочий документ); пилоты ESS с ~2019
- **Целевой показатель:** ежемесячные индексы цен на жильё (HPI) и индикаторы уровня цен из объявлений о продаже/аренде
- **Метод:** web scraping порталов недвижимости (не поисковые запросы)
- **Документ:** "Feasibility of monthly house price indices and price-level indicators from web-scraped data", Eurostat Statistical Working Paper KS-01-26-025, 2026
- **Ссылка:** https://ec.europa.eu/eurostat/web/products-statistical-working-papers/w/ks-01-26-025
- **Статус:** эксперимент (ESS pilots)

### Росстат — большие данные (без поисковых запросов)
- **Год:** Концепция использования больших данных — с 2022; пилоты с 2020–2021
- **Направления:** (а) данные ККТ/ФНС для ИПЦ (Приказ Росстата от 15.12.2021 № 915 допускает комбинирование с большими данными); (б) данные сотовых операторов для туристского потока (соглашение с Аналитическим центром при Правительстве РФ, декабрь 2021; оценка туристского потока публикуется с 2022)
- **Ссылки:** https://rosstat.gov.ru/folder/313/document/146791 ; https://rosstat.gov.ru/storage/mediabank/gaWoEUaA/Doklad_28042021.pdf
- **Статус:** пилот/эксперимент. **Официальных кейсов использования поисковых запросов (Яндекс Вордстат) в статистике строительства/ввода жилья Росстатом НЕ найдено.**

---

## Важные уточнения к исходным гипотезам заказчика

1. **GDPNow (ФРБ Атланты) НЕ использует Google Trends.** GDPNow — bridge equations на официальных данных (Census, BLS, ISM и т.д.), без поисковых данных. См. https://www.atlantafed.org/cqer/research/gdpnow
2. **ФРБ Филадельфии:** официального продукта с Google Trends не найдено (GDPplus — на официальных данных). Ближайший кейс ФРС — ФРБ Чикаго (кейс 4).
3. **CSO Ирландии:** прямого кейса CSO с Google Trends не найдено. CSO использует web scraping в Frontier Series (например, RIP.ie для смертности), а Google Trends официально применяет Департамент предпринимательства (кейс 12) и Центральный банк Ирландии (кейс 11).
4. **РБНЗ (RBNZ):** официальных кейсов с поисковыми данными не найдено. RBNZ использует ML-наукастинг ВВП на ~600 предикторах (DP2019/03) и MIDAS для рынка труда (AN2019/04, включая dwelling consents), но без Google Trends.
5. **Гонконг (HKMA):** официальных кейсов HKMA с Google Trends не найдено; есть академическая работа (Wong, 2023, Pacific Economic Review) по индексу покупательских стимулов на Google Trends для рынка недвижимости Гонконга.
6. **ЦБ РФ:** поисковые данные используются в исследовательском контуре (Серия докладов об экономических исследованиях, № 174/2026 и более ранние работы), прямых упоминаний Вордстата в Докладе о ДКП не найдено — канал внедрения идёт через рабочие статьи и внутренний мониторинг.

## Вывод для исследователя
Мировая практика подтверждает легитимность подхода: поисковые данные официально используются центробанками (BoE 2011, BdE 2012, Banca d'Italia 2012, Bundesbank 2020 — продакшн, OECD 2020 — продакшн, ЦБ РФ 2017/2026) и статведомствами (Statistics Finland). Прямой аналог кейса исследователя (поисковые запросы → наукастинг недвижимости/строительства) — RBI (Индия, 2017): Google Trends + DFM для продаж девелоперов. В строительной статистике официальные ведомства чаще используют web scraping (Евростат) и административные данные, а не поисковые запросы — это ниша, где индекс на Вордстате может быть оригинальным вкладом.
