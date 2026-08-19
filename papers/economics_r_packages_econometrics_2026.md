# Экономика строительства в R: Стратегический выбор пакетов для оценки, наукастинга и прогнозирования

**Источник:** PDF (28 стр., 480 КБ, WeasyPrint 67.0)
**Тематика:** R-пакеты для эконометрического анализа в строительстве
**Ссылок:** 113

## Содержание

1. Фундаментальные пакеты: fixest, marginaleffects, lmtest, sandwich, zoo, xts, forecast, fable
2. Причинно-следственный анализ: DiD, BSTS, Synthetic Control, CausalImpact
3. Наукастинг: BSTS, факторные модели, ML (Random Forest, XGBoost)
4. Долгосрочное прогнозирование: ARIMA/ETS, Bayesian (bsts), ML
5. Интеграция данных и структурные сдвиги: xtbreak, strucc
6. Стратегические рекомендации (5-шаговый workflow)

---

## Ключевые R-пакеты

| Пакет | Назначение | Ключевые функции |
|-------|-----------|-----------------|
| **fixest** | Модели с фиксированными эффектами | feols(), робастные SE, события |
| **marginaleffects** | Интерпретация результатов | AME, контрасты, 100+ моделей |
| **lmtest** | Тесты диагностики | Breusch-Pagan, Durbin-Watson |
| **sandwich** | Робастные SE | HC, HAC, кластеризованные |
| **zoo/xts** | Временные ряды | Структуры данных |
| **forecast** | Классические модели | auto.arima(), ets() |
| **fable** | Современный forecast | tidyverts, множественная оценка |
| **bsts** | Bayesian Structural TS | Causal inference, nowcasting |
| **CausalImpact** | Причинный вывод | BSTS, структурные модели |
| **xtbreak** | Структурные сдвиги | Тесты на breakpoints |

---

## Список ссылок (113)

1. wcasting Transaction-Based House Price Indices Using ...
   https://www.researchgate.net/publication/395135699_Nowcasting_Transaction-Based_House_Price_Indices_Using_Web-Scraped_Listings_and_MIDAS_Regression

2. e next hour of residential load using boosting ... - Nature
   https://www.nature.com/articles/s41598-025-91767-6

3. House Price Estimations with Multi-Head Gated Attention
   https://arxiv.org/html/2405.07456v1

4. rice Index Prediction through ARMA with Inflation Effect
   https://www.mdpi.com/2075-5309/14/5/1243

5. ting and the real-time data flow - European Central Bank
   https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1564.pdf

6. d estimating structural breaks in time series and panel ...
   https://journals.sagepub.com/doi/10.1177/1536867X251365449

7. Structural Breaks in Time Series - RPubs 7.
   https://rpubs.com/Ken_Fritzell/982102

8. Estimating Structural Breaks in Time Series and Panel ...
   https://arxiv.org/html/2110.14550v3

9. ting and testing multiple structural breaks occurring at ...
   https://www.sciencedirect.com/science/article/pii/S0960077924000298

10. Structural Breaks in Interactive Effects Panel Data Models
   https://onlinelibrary.wiley.com/doi/full/10.1002/jae.3097

11. ting and Quantifying Structural Breaks in Climate - MDPI
   https://www.mdpi.com/2225-1146/10/4/33

12. act of Structural Break Location on Forecasting Accuracy
   https://www.researchgate.net/publication/366737406_Impact_of_Structural_Break_Location_on_Forecasting_Accuracy_Traditional_Methods_Versus_Artificial_Neural_Network

13. matters, when it matters: Introducing Maynard, a tool ...
   https://www.sciencedirect.com/science/article/pii/S2352711025004327

14. tion Intervals for Time Series Forecasting: A Bootstrap ...
   https://onlinelibrary.wiley.com/doi/10.1002/for.70126?af=R

15. d beyond: new data for decision making in central banks
   https://www.bis.org/ifc/publ/ifcb66.pdf

16. an methodology for adaptive sparsity and shrinkage in ...
   https://www.tandfonline.com/doi/full/10.1080/07350015.2025.2592349

17. d Topics in Time Series Forecasting: Statistical Models ...
   https://pmc.ncbi.nlm.nih.gov/articles/PMC11941414/

18. y of Data-Driven Construction Materials Price Forecasting
   https://www.researchgate.net/publication/384624528_A_Survey_of_Data-Driven_Construction_Materials_Price_Forecasting

19. inflation rate in construction projects cost: Forecasting ...
   https://www.sciencedirect.com/science/article/pii/S2405844024020681

20. OVERY-INFORMED FORECASTING STRATEGY ... - arXiv
   https://arxiv.org/html/2603.01085v1

21. Construction Material Price Forecasting | PDF - Scribd 1.
   https://www.scribd.com/document/968341521/2512-09360v1

22. g Office Construction Price Indices for Cost Planning in ...
   https://www.mdpi.com/2075-5309/16/1/103

23. Irresistible Fairy Tale: The Cultural and Social History ...
   https://www.academia.edu/102856895/The_Irresistible_Fairy_Tale_The_Cultural_and_Social_History_of_a_Genre_by_Jack_Zipes_review_

24. Thematic Apperception Test, The Children's Appee in ... .
   https://www.scribd.com/document/722921297/Thematic-Apperception-Test-The-Children-s-Appee-in-Clinical-Use-The-Bellak-Leopold-1916

25. mpirical Investigation of Temporal Association between ...
   https://www.researchgate.net/publication/319177019_Empirical_Investigation_of_Temporal_Association_between_Architecture_Billings_Index_and_Construction_Spending_Using_Time-Series_Methods

26. 1 Introduction - arXiv 26.
   https://arxiv.org/html/2603.00422v1

27. sting and Near-Term Forecasting Cambodia's Economy in
   https://www.elibrary.imf.org/view/journals/001/2024/147/article-A001-en.xml

28. arning for financial forecasting: A review of recent trends
   https://www.sciencedirect.com/science/article/pii/S1059056025008822

29. [PDF] Nowcasting Made Easier: a toolbox for economists
   https://www.ecb.europa.eu/pub/pdf/scpwps/ecb.wp3004~3ce9d0d8ca.en.pdf

30. inancial Condition Index Construction and Forecasting ...
   https://www.mdpi.com/2073-8994/17/6/904

31. olkit: Choosing the right model for the task: Migration ...
   https://www.oecd.org/en/publications/migration-anticipation-and-preparedness_4161131f-en/full-report/forecasters-toolkit-choosing-the-right-model-for-the-task_af4817f2.html

32. ying impact of uncertainty shocks on the co-movement ...
   https://www.nature.com/articles/s41599-025-04494-8

33. troduction to Double/Debiased Machine Learning - arXiv
   https://arxiv.org/pdf/2504.08324

34. cial intelligence model for payment delay optimisation ...
   https://www.sciencedirect.com/science/article/pii/S294986352500038X

35. Matrix Completion Methods for Causal Panel Data Models
   https://www.researchgate.net/publication/320707597_Matrix_Completion_Methods_for_Causal_Panel_Data_Models

36. Forecasting: theory and practice 36.
   https://arxiv.org/pdf/2012.03854

37. emand during and after supply chain disruptions using ...
   https://www.tandfonline.com/doi/full/10.1080/00207543.2025.2577158

38. ions & supply chain management: principles and practice
   https://www.tandfonline.com/doi/full/10.1080/00207543.2025.2555531

39. Nowcasting 39.
   https://ideas.repec.org/p/ecb/ecbwps/20101275.html

40. Real estate listings and their usefulness for hedonic ... 40.
   https://ideas.repec.org/a/spr/empeco/v61y2021i6d10.1007_s00181-020-01992-3.html

41. Search and Predictability of Prices in the Housing Market
   https://ideas.repec.org/a/inm/ormnsc/v70y2024i1p415-438.html

42. Forecasting and Nowcasting Macroeconomic Variables 2.
   https://ideas.repec.org/p/oxf/wpaper/674.html

43. Forecasting the US Real Private Residential Fixed ... 43.
   https://ideas.repec.org/p/pre/wpaper/201348.html

44. Now-Casting and the Real-Time Data Flow 44.
   https://ideas.repec.org/h/eee/ecofch/2-195.html

45. Forecasting Real House Price of the U.S.: An Analysis ... .
   https://ideas.repec.org/p/pre/wpaper/201362.html

46. Nowcasting GDP and Inflation: The Real Time ... 46.
   https://ideas.repec.org/p/cpr/ceprdp/5178.html

47. Now-casting and the real-time data flow 47.
   https://ideas.repec.org/p/ecb/ecbwps/20131564.html

48. ding indicators for the US housing market: New empirical
   https://ideas.repec.org/a/eee/finana/v89y2023ics1057521923002818.html

49. owth using Google Trends data: A Bayesian Structural ...
   https://www.sciencedirect.com/science/article/pii/S0169207022000620

50. ents on the Bayesian Structural Time Series Model - arXiv
   https://arxiv.org/pdf/2011.00938

51. PDF) Multivariate Bayesian Structural Time Series Model
   https://www.researchgate.net/publication/322383288_Multivariate_Bayesian_Structural_Time_Series_Model

52. [PDF] Targeted Synthetic Control Method - arXiv 52.
   https://arxiv.org/pdf/2602.04611

53. Nowcasting from cross‐sectionally dependent panels 53.
   https://onlinelibrary.wiley.com/doi/10.1002/jae.2980

54. Rising building material prices: impact on residential real
   https://ideas.repec.org/p/arz/wpaper/eres2023_104.html

55. Costs of Construction and Housing Prices: A Full-Cost ...
   https://www.researchgate.net/publication/372646742_The_Costs_of_Construction_and_Housing_Prices_A_Full-Cost_Pricing_or_Tendering_Theory

56. ystematic literature review on price forecasting models ...
   https://www.tandfonline.com/doi/full/10.1080/15623599.2023.2241761

57. Housing Boom and Headline Inflation 57.
   https://www.imf.org/-/media/files/publications/wp/2022/english/wpiea2022151-print-pdf.pdf

58. The amplifying effect of spatial planning restrictions on ...
   https://www.sciencedirect.com/science/article/pii/S1051137725000440

59. ] a conceptual synthesis of causal assumptions for - arXiv
   https://www.arxiv.org/pdf/2504.11035v1

60. rustworthy AI in FinTech: Fraud Analytics, Credit Risk ...
   https://www.researchgate.net/publication/402845787_Trustworthy_AI_in_FinTech_Fraud_Analytics_Credit_Risk_Modeling_and_Regulatory-Grade_Explainability

61. ata for Advanced Modelling of Electricity Demand and ...
   https://pastel.hal.science/tel-05086472v1/file/2025UPSLM004_archivage.pdf

62. ebiased machine learning for treatment and structural ...
   https://ideas.repec.org/r/ifs/cemmap/28-17.html

63. Nowcasting using regression on signatures 63.
   https://arxiv.org/html/2305.10256v2

64. owcasting US GDP Using Tree-Based Ensemble Models ...
   https://pmc.ncbi.nlm.nih.gov/articles/PMC7789904/

65. Identifying Optimal Indicators and Lag Terms for ... 65.
   https://www.imf.org/-/media/files/publications/wp/2023/english/wpiea2023045-print-pdf.pdf

66. ) Coupled Supply and Demand Forecasting in Platform ...
   https://www.researchgate.net/publication/401469453_Coupled_Supply_and_Demand_Forecasting_in_Platform_Accommodation_Markets

67. ols for Econometrics | PDF | Regression Analysis - Scribd
   https://www.scribd.com/document/798671480/BidData-New-Tricks-for-Econometrics-Varian-H

68. ed Supply and Demand Forecasting in Platform ... - arXiv
   https://arxiv.org/pdf/2603.00422

69. omatic Time Series Forecasting: TheforecastPackage forR
   https://www.researchgate.net/publication/222105759_Automatic_Time_Series_Forecasting_TheforecastPackage_forR

70. mise of Time-Series Foundation Models for Agricultural ...
   https://arxiv.org/html/2601.06371v2

71. e R-package to forecast time series: ARIMA models and ...
   https://www.academia.edu/29661724/Using_the_R_package_to_forecast_time_series_ARIMA_models_and_Application

72. Forecast Time Series With R Language | PDF - Scribd 72.
   https://www.scribd.com/document/353164893/Forecast-Time-Series-With-R-Language

73. omatic time series forecasting: the forecast package for R
   https://ideas.repec.org/p/msh/ebswps/2007-6.html

74. Forecasting Homework 5 - AWS 74.
   https://rstudio-pubs-static.s3.amazonaws.com/1288685_aab2cf721e034ad69abbdc4c564040f1.html

75. Journal of Forecasting - ResearchGate 75.
   https://www.researchgate.net/journal/Journal-of-Forecasting-1099-131X

76. Architectural Diversity and Open Challenges 76.
   https://arxiv.org/pdf/2411.05793

77. ARSS: Multivariate Autoregressive State-space Models ...
   https://www.researchgate.net/publication/259383212_MARSS_Multivariate_Autoregressive_State-space_Models_for_Analyzing_Time-series_Data

78. Migration Anticipation and Preparedness 78.
   https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/03/migration-anticipation-and-preparedness_c7c13bc4/4161131f-en.pdf

79. orecasting US real private residential fixed investment ...
   https://ideas.repec.org/a/spr/empeco/v51y2016i4d10.1007_s00181-015-1059-z.html

80. Appl. Sci., Volume 15, Issue 22 (November-2 2025) 80.
   https://www.mdpi.com/2076-3417/15/22

81. Guofu Zhou 81.
   https://ideas.repec.org/f/c/pzh420.html

82. United Nations Activities on Artificial Intelligence (AI) 2.
   https://www.itu.int/dms_pub/itu-s/opb/gen/S-GEN-UNACT-2021-PDF-E.pdf

83. REPORT 2023/2024 | Human Development Reports 83.
   https://hdr.undp.org/system/files/documents/global-report-document/hdr2023-24reporten.pdf

84. ausal Inference with Continuous Instruments Using the ...
   https://www.researchgate.net/publication/329037537_Robust_causal_inference_with_continuous_instruments_using_the_local_instrumental_variable_curve

85. Victor Chernozhukov - IDEAS/RePEc 85.
   https://ideas.repec.org/f/c/pch864.html

86. ne Learning For Econometrics ENSAE Paris IP Paris | PDF
   https://www.scribd.com/document/681274148/2019-Machine-Learning-for-Econometrics-ENSAE-Paris-IP-Paris

87. e Performance of Hierarchical Forecasting Methods on ...
   https://www.researchgate.net/publication/332638404_Assessing_the_Performance_of_Hierarchical_Forecasting_Methods_on_the_Retail_Sector

88. Download book PDF - Springer 88.
   https://link.springer.com/content/pdf/10.1007/978-0-585-33173-7.pdf

89. l Machine Learning: A Survey and Open Problems - arXiv
   https://arxiv.org/pdf/2206.15475

90. ausal machine learning can leverage marketing strategies
   https://pmc.ncbi.nlm.nih.gov/articles/PMC9833560/

91. Sovereign debt cost and economic complexity 91.
   https://www.sciencedirect.com/science/article/pii/S1042443125000113

92. e-Vacancy Dynamics—An Empirical Study of the Hong ...
   https://www.mdpi.com/2227-7072/12/3/74

93. d Object Detection with Transformers Lecture Notes in ...
   https://exaly.com/paper-pdf/83545276/citation-report.pdf

94. publications at Department of Economics University of ...
   https://ideas.repec.org/d/g/deuchus.html

95. onometric panel data-based approach for housing price ...
   https://www.researchgate.net/publication/233833260_An_econometric_panel_data-based_approach_for_housing_price_forecasting_in_Iran

96. ts on forecasting construction prices using vector error ...
   https://www.researchgate.net/publication/266376132_Market_effects_on_forecasting_construction_prices_using_vector_error_correction_models

97. view on the economic and inflation environment in the ...
   https://www.ecb.europa.eu/pub/pdf/scpops/ecb.op371.en.pdf

98. DF] OECD Economic Outlook, Volume 2025 Issue 2 (EN)
   https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/oecd-economic-outlook-volume-2025-issue-2_413f7d0a/9f653ca1-en.pdf

99. IMF Blogs 99.
   https://www.imf.org/en/blogs

100. g Private-Sector Construction Works: VAR Model Using ...
   https://www.researchgate.net/publication/275338730_Forecasting_Private-Sector_Construction_Works_VAR_Model_Using_Economic_Indicators

101. Inferring causal impact using Bayesian structural time- ...
   https://www.researchgate.net/publication/276126076_Inferring_causal_impact_using_Bayesian_structural_time-series_models

102. e Time-Series Properties of House Prices: A Case Study ...
   https://www.researchgate.net/publication/225617517_The_Time-Series_Properties_of_House_Prices_A_Case_Study_of_the_Southern_California_Market

103. Christian Hansen | IDEAS/RePEc 103.
   https://ideas.repec.org/f/c/pha982.html

104. ) Machine learning in agricultural and applied economics
   https://www.researchgate.net/publication/335444933_Machine_learning_in_agricultural_and_applied_economics

105. A conceptual synthesis of causal assumptions for causal ...
   https://www.researchgate.net/publication/390810618_A_conceptual_synthesis_of_causal_assumptions_for_causal_discovery_and_inference

106. Business Analytics Practical Data Science For Decision ...
   https://www.scribd.com/document/939595376/Modern-Business-Analytics-Practical-Data-Science-for-Decision-making-Matt-Taddy-Leslie-Hendrix-Matthew-C-Harding

107. Machine Learning in Econometrics Course | PDF - Scribd
   https://www.scribd.com/document/716636753/HD-Econometrics

108. rical study on the economic factors of the architectural ...
   https://link.springer.com/article/10.1186/s43238-025-00193-0

109. An empirical study of the impacts of wildfires on home ...
   https://www.sciencedirect.com/science/article/pii/S0169204624000616

110. Housing prices, costs, and policy: The housing supply ... .
   https://onlinelibrary.wiley.com/doi/10.1111/1540-6229.12491

111. The Effect of New Residential Construction on Housing ...
   https://www.researchgate.net/publication/263664371_The_Effect_of_New_Residential_Construction_on_Housing_Prices

112. Vicki L. Been - Publications | NYU School of Law 112.
   https://its.law.nyu.edu/facultyprofiles/index.cfm?fuseaction=profile.publications&personid=19774

113. pact of housing prices and land financing on economic ...
   https://pmc.ncbi.nlm.nih.gov/articles/PMC11060597/
