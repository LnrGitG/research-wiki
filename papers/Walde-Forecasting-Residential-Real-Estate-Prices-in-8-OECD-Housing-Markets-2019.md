---
title: **Forecasting Residential Real Estate Prices in Eight OECD Housing Markets**
type: paper
source_pdf: raw/papers/Walde_Forecasting Residential Real Estate Prices in 8 OECD Housing Markets_2019.pdf
converted: 2026-07-26
---

# **Forecasting Residential Real Estate Prices in Eight OECD Housing Markets** 

By Claudio Walde 

Examiner: Prof. Didier Sornette 

Supervisor: Dr. Diego Ardila Alvarez 

Master thesis submitted to the Chair of Entrepreneurial Risks in partial fulfillment of graduation requirements for the degree of 

#### **Master of Science** 

In Management, Technology and Economics 





Master Thesis MSc MTEC May 2019 

Claudio Walde cwalde@student.ethz.ch 







## **Abstract** 

This master thesis analyzes the forecasting performance of three different models for residential real estate prices in eight OECD countries. An ordinary least squares (OLS) regression model, a threshold autoregressive (TAR) model, and a weighted combination of the two, a so-called ensemble model, were implemented using quarterly time series from 1970 Q1 to 2017 Q4. 

The threshold variable for the TAR model, indicating the different regimes, was hereby determined by the log periodic power law singularity (LPPLS) model. 

The results show significant improvements of the forecasting accuracy for the ensemble model compared to the stand-alone OLS model across all countries. Furthermore, the forecasting accuracy is also improved compared to the TAR model on average, but much less pronounced. 

#### **Keywords** 

Housing, Ensemble model, TAR, LPPLS 

2 

## **Table of contents** 

|**1.**<br>**INTRODUCTION ......................................................................................................................... 4**|
|---|
|**2.**<br>**DATA DESCRIPTION AND TEMPORAL PROPERTIES ..................................................... 6**|
|2.1.<br>VARIABLE DESCRIPTION.......................................................................................................... 6|
|2.2.<br>SUMMARIZINGDATADESCRIPTION........................................................................................ 9|
|_2.2.1._<br>_United States ................................................................................................................ 10_|
|_2.2.2._<br>_Switzerland ................................................................................................................... 12_|
|_2.2.3._<br>_Belgium ......................................................................................................................... 14_|
|_2.2.4._<br>_Canada ......................................................................................................................... 16_|
|_2.2.5._<br>_France .......................................................................................................................... 18_|
|_2.2.6._<br>_Germany ....................................................................................................................... 20_|
|_2.2.7._<br>_Netherlands .................................................................................................................. 22_|
|_2.2.8._<br>_United Kingdom ........................................................................................................... 24_|
|**3.**<br>**METHODOLOGY ...................................................................................................................... 26**|
|3.1.<br>CALIBRATION ANDEVALUATIONSTRATEGY....................................................................... 26|
|3.2.<br>OLS ....................................................................................................................................... 29|
|_3.2.1._<br>_Regression Models ....................................................................................................... 30_|
|3.3.<br>TAR ....................................................................................................................................... 32|
|_3.3.1._<br>_TAR Model .................................................................................................................... 33_|
|3.4.<br>LOGPERIODICPOWERLAWSINGULARITYMODEL............................................................. 33|
|3.5.<br>MODELCOMBINATION ANDWEIGHTING.............................................................................. 35|
|**4.**<br>**RESULTS ..................................................................................................................................... 37**|
|4.1.<br>OLS – RESULTS..................................................................................................................... 37|
|4.2.<br>TAR - RESULTS..................................................................................................................... 42|
|4.3.<br>ENSEMBLEMODELRESULTS................................................................................................ 45|
|**5.**<br>**DISCUSSION ............................................................................................................................... 56**|
|5.1.<br>MAINFINDINGS..................................................................................................................... 56|
|5.2.<br>LIMITATIONS......................................................................................................................... 57|
|**6.**<br>**CONCLUSION ............................................................................................................................ 59**|
|**7.**<br>**ACKNOWLEDGMENTS ........................................................................................................... 60**|
|**8.**<br>**LIST OF REFERENCES ............................................................................................................ 61**|
|**9.**<br>**APPENDIX ................................................................................................................................... 64**|
|A.<br>TIMESERIESPLOTS................................................................................................................... 64|
|B.<br>DETAILEDOLS RESULTS.......................................................................................................... 73|
|_B 1.1._<br>_OLS – Results – United States ...................................................................................... 73_|
|_B 1.2._<br>_OLS – Results – Switzerland ........................................................................................ 75_|
|_B 1.3._<br>_OLS – Results – Belgium .............................................................................................. 77_|
|_B 1.4._<br>_OLS – Results – Canada ............................................................................................... 79_|
|_B 1.5._<br>_OLS – Results – France ................................................................................................ 81_|
|_B 1.6._<br>_OLS – Results – Germany ............................................................................................ 83_|
|_B 1.7._<br>_OLS – Results – Netherlands ........................................................................................ 85_|
|_B 1.8._<br>_OLS – Results – United Kingdom ................................................................................. 87_|
|<br>C.<br>DIEBOLD-MARIANOTESTRESULTS.......................................................................................... 89|



3 

## **1. Introduction** 

Non-financial wealth, which is principally housing wealth, currently accounts for almost 50 percent of total private wealth globally, according to Credit Suisse’s Global Wealth Report (CS, 2018). In hindsight, it is therefore not surprising that the burst of the US housing bubble in 2007/2008 affected the whole world economy. 

The significance of real estate markets for individuals and institutions is also reflected in the high interest in forecasting methods that have been developed in the past. 

Typical approaches have been made with linear regression models, using macroeconomic variables to describe the price developments. Case and Shiller (Case & Shiller, 1990) have pioneered this methodology for the housing market in the early 1990s, by using an ordinary least squares regression model, including twelve descriptive variables, to forecast housing prices in four U.S. cities. Many others have followed this approach. (Leblanc & Bokreta, 2009) for example have developed the methodology by the application of dynamic parameter estimations. Whereas (Ghysels, Plazzi, Valkanov, & Torous, 2013) compare the predictability of housing prices for different model setups. The general consensus of the literature is that macroeconomic variables do show explanatory properties of housing prices. 

However, macroeconomic time series occasionally show dramatic changes in their behavior, which are not properly reflected by classic linear regression models. Regime switching models have therefore been applied to capture such dramatic breaks (Durlauf & Blume, 2010). The threshold autoregressive (TAR) model is one of these regime switching models and was first proposed by Tong in 1978. The general setup of a TAR model consists of two purely autoregressive (AR) models and a threshold variable. Whereby, the threshold variable defines the regime, high or low, of the time series at every time t. This distinction of regimes is used to fit two AR models to the time series. However, the applicability of the TAR model is generally limited because the threshold variable must be known (Tsay, 1989). 

In this work we combine the properties of a linear regression model with the ones of a threshold autoregressive (TAR) model to forecast real estate prices in the housing markets of Belgium, Canada, France, Germany, the Netherlands, Switzerland, the United Kingdom, and the United States. Multiple linear regression models are evaluated, and the best performing specification is consequently combined with a TAR model. The expectation is that the combination of the two completely different approaches would be complementary and therefore improve the forecasting accuracy. 

4 

To circumvent the problem of the missing threshold variable of the TAR model, the log periodic power law singularity (LPPLS) model (Johansen, Ledoit, Sornette, & Finance, 2000) is applied to detect regime changes in the property price indices. “The LPPL model […] is a nonlinear model that embodies the effect of positive feedback loops among economic agent, which may lead to unsustainable price developments with predictable critical times” (D. Ardila, Sanadgol, Cauwels, & Sornette, 2017). 

Furthermore, a simple autoregressive (AR) model is fitted and its forecasting accuracy is compared to the one of the TAR model to test whether the inclusion of the threshold variable adds value to the forecasting performance. 

The combination of the two models is achieved by an ensemble modelling approach, where the two forecasts from the best performing OLS model and the TAR model are weighted, and a combined forecast is calculated (Samuels & Sekkel, 2017). Whereby two different weighting methods are applied and evaluated. 

All the models were implemented and evaluated using an expanding window approach to ensure that the forecasts are not influenced by in-sample look-ahead bias. Although the results differ quite substantially across the different housing markets, a general improvement of the forecasting properties by both ensemble models compared to the OLS models is observable. On average the root mean squared prediction error (RMSE) is reduced by 24 percent in comparison to the linear regression model. Furthermore, the occurrence of the correct prediction sign is compared. The ensemble models, including the TAR model, forecast the correct prediction sign of the actual values with approximately 30 percent higher accuracy than the OLS models. 

The rest of this thesis is organized as follows. The second chapter explains the data and points out the differences in data availability across countries. In chapter three the different models and the calibration and evaluation strategy are explained. The results are presented in chapter four. Followed by the discussion and the concluding remarks in chapters five and six respectively. 

5 

## **2. Data Description and Temporal Properties** 

One of the goals of this study is to work with a long timescale, to integrate as much different regimes as possible. The data availability differs quite substantially for the different variables and countries. Whenever available, the same data source was used across different economies for reasons of comparability. 

The variables were chosen by assessments of prior literature and data availability. The eight countries were selected due to different reasons: First the US was chosen due to data availability and the importance and influential power of its economy. The European countries were chosen to point out differences and similarities in the European real estate market. And last, Canada was chosen because the assessment of its real estate market has seldomly been included in prior literature. 

The timespan of the investigation sample size reached from 1970 Q1 to 2017Q4 using quarterly time series, for a maximum of 192 observations per time series. Since some data is not available for the complete time span, the analysis of the corresponding countries was reduced. 

### 2.1. Variable description 

One dependent and up to twelve independent variables were collected for each of the seven countries. The explained variable is the property price index (PPI). There is a variety of such indices available. The Bank of International Settlement (BIS)<sup>1</sup> collects data from different sources and publishes most of the available indices. Similar indices were chosen for each country for reasons of comparability. 

The independent variables are the consumer price index (CPI), long-term interest rate (LIR), different exchange rates (XR), the population (POP), the gross national disposable income per head of population (Y), the gross domestic product (GDP), the industrial production index (IPI), the unemployment rate (UR), the consumer confidence index (CCI), the imports (IMP) and exports (EXP). 

Figure 1 on page 8 presents the normalized plots of the eight main variables<sup>2</sup> . 

> 1 “BIS Residential Property Price database, <u>http://www.bis.org/statistics/pp.htm”</u> 

> 2 They are called main variables because UR, Exp, Imp and the exchange rates were not available for all housing markets for the whole observation period. 

6 

For reasons of comparison of the development of the different time series in figure 1, the data was normalized by dividing it by its value in 2010. 

The eight housing markets which were included in the analysis have developed very differently. The first plot in the left column of figure 1 shows that especially Germany’s real housing price development seems to differ from the other countries. Switzerland’s real index also exhibits a different behavior from the other markets. Whilst the remaining six housing markets all show significantly higher price levels in 2005 than in 1970, the real housing prices in Germany and Switzerland do not differ essentially at these two observations. Moreover, the graph illustrates the varying intensities and recovery times after the financial crisis, around 2008.  It is visible, that the impact on Switzerland’s housing market was rather insignificant, whereas the US index experienced a strong decrease. Furthermore, the French, the British and especially the Dutch housing markets are also strongly affected by the financial crisis and show relatively long recovery times.  Whereas on the other hand the price decrease for the Belgian and Canadian housing markets, similar to the Swiss and German markets, is not significant during this period. 

The remaining seven plots in figure 1 show that the other variables developed similarly across all eight analyzed economies. 

Nevertheless, it is worth mentioning that the consumer price index in Switzerland has stayed more or less constant since 2010. Furthermore, the increase in population for Germany around the “Wiedervereinigung” is observable in the plots. This jump obviously has a direct impact on the per capita gross domestic product and national disposable income, which both show a strong decrease in 1990. Due to the spurious behavior of the German data around this period, it was decided to exclude the observations from 1989 to 1991 from the analysis of the German housing market. 

Figure 1 clearly evidences that most of the variables show a trend. Following this visual inspection and the influential work of (Nelson & Plosser, 1982) on stationarity in 

macroeconomic time series, it was decided to work with logarithmic growth rates for most of the variables. Tables 1 to 8 in chapters _2.2.1. to 2.2.8_ . indicate whether the variables entered the models in levels or in logarithmic growth rates. 

Detailed plots of all the time series and the corresponding log growth rates can be found in _Appendix A Time Series Plots._ 

7 

_Figure 1 Normalized time series plots of different variables_ 















_The graphs in figure 1 display the normalized time series plots, with the base year being 2010, for eight of the variables used in this work. The time series show similar developments across countries except for the real property price index, in which clear differences in the dynamics of the indices are visible._ 

8 

### 2.2. Summarizing Data Description 

Studies which are based on cross-border data collection and comparison in general harbour substantial risks. Although, a great effort was made in terms of data comparability for this thesis, the time series exhibit structural differences across the different countries. First, the content of the real estate indices differs because they do not all include the same types of dwellings. For some countries, as for the US S&P Case Shiller National Home Price Index, only single-family homes are included in the calculation of the index, whereas for other countries, like Switzerland, both, owner occupied flats and single-family homes are included in the index. 

Furthermore, the observation frequencies differ between the different time series. Whilst for the USA all the variables were available at a quarterly frequency, this was not always the case for the other countries. For all other housing markets, the annual values had to be averaged or linearly interpolated for further analysis. Of the totally 98 time series used six had to be interpolated and 18 were averaged. It was decided to calculate the year on year logarithmic growth rates of these processed time series. 

Admittedly, these transformations might influence the cross-country comparability, as year on year growth rates have different dynamics than quarterly growth rates. However, they only impact mildly the scope of this thesis, since its primary goal is to compare country-level forecasting models. 

Lastly, some of the time series have limited availability over the observation period. The Belgian unemployment rate for example is only available after 1983. And of course, all exchange rates including the euro are only available after its introduction in 1999. 

For simplicity, most of these time series with limited availability were excluded from the OLS regression models.  The exact model structures for each country are presented in _Appendix B Detailed OLS Results._ 

9 

#### _2.2.1. United States_ 

A variety of real estate indices are available for the U.S. market. The nominal S&P CoreLogic Case-Shiller U.S. National Home Price NSA Index (S&P, 2019) was chosen. It is based on a repeated sales method and includes single-family homes. The index is calculated on a 

monthly basis and is generally considered the leading measure of U.S. residential real estate prices. The nominal monthly index was used because the available real Case-Shiller indices only cover shorter time periods. 

To obtain real, quarterly data, the time series was averaged over a period of three months and deflated by the consumer price index (CPI). 

The consumer price index (CPI), measured for all items, was gathered from OECD statistics webpage and originates from the Bureau of Labor Statistics (BLS). 

The data on Long-Term Interest Rates (LIR) refer to yields on government securities with outstanding maturities of ten years. 

The real disposable income (rY) was divided by population (POP) to obtain real per Capita data, measured in U.S. Dollars (USD). 

Furthermore, all monthly data was averaged over a three months period to reduce monthly fluctuations. 

The Consumer Confidence Index (CCI) is a qualitative measure published by OECD. It provides indication on household’s future consumption and saving behavior, based upon answers regarding their expectations on the economy and their personal financial situation (OECD, 2019).  This time series was available from the same data source for every country except Canada. 

Table 1 shows a summary for the U.S. time series. 

10 

_Table 1 Data summary for the United States_ 

|**Variable**|**Description**|**Level**<br>**or**∆|**Dimension**|**Max**|**Min**|**Mean**|**Source**|**Frequency**|**Start**|**End**|
|---|---|---|---|---|---|---|---|---|---|---|
||||||||S&P/Core<br>||||
|PPI|Property Price<br>Index|∆|Index<br>(2000 =100)|205.81|18.93|93.71|Logic/<br>Case-<br>Shiller|Monthly|1970<br>Jan|2018<br>Aug|
|CPI|Consumer Price<br>Index|∆|Index<br>(2015=100)|105|16|60.6|OECD /<br>BLS|Quarterly|1970<br>Q1|2018<br>Q1|
|LIR|Long-Term<br>Interest Rates|Level|Percent, per<br>annum|14.85|1.56|6.46|Federal<br>Reserve<br>Board, US|Quarterly|1970<br>Q1|2018<br>Q1|
|XRUSDCAD|Exchange Rate 1<br>USD to<br>Canadian Dollar|∆|Absolute<br>value|1.60|0.96|1.22|Federal<br>Reserve<br>Bank of<br>St. Louis|Monthly|1971<br>Jan|2017<br>Dec|
|XRUSDEUR|Exchange Rate 1<br>USD to EUR|∆|Absolute<br>value|1.17|0.63|0.85|Federal<br>Reserve<br>Bank of<br>St. Louis|Monthly|1999<br>Jan|2017<br>Dec|
|POP|Population|∆|Total<br>Residents<br>(1000’s)|326’907|204’086|263’864|Federal<br>Reserve<br>Bank of<br>St. Louis|Quarterly|1970<br>Q1|2017<br>Q4|
|rY|Real Disposable<br>Income|∆|Bn. Chained<br>2012 USD,<br>Annual Rate|14’066|3’577|8’060|Federal<br>Reserve<br>Bank of<br>St. Louis|Quarterly|1970<br>Q1|2017<br>Q4|
|rGDPpC|Real Gross<br>Domestic<br>Product per<br>Capita|∆|Chained<br>2012 USD|56’446|23’945|39’974|Federal<br>Reserve<br>Bank of<br>St. Louis|Quarterly|1970<br>Q1|2018<br>Q2|
|IPI|Industrial<br>Production<br>Index|∆|Index<br>(2015=100)|107.30|37.85|73.97|Federal<br>Reserve<br>Bank of<br>St. Louis|Quarterly|1970<br>Q1|2018<br>Q2|
|UR|Unemployment<br>Rate|∆|Harmonized<br>UR, Percent|10.67|3.90|6.29|OECD|Quarterly|1970<br>Q1|2018<br>Q1|
|CCI|Consumer<br>Confidence<br>Index|∆|102.7|86.2|99.8|OECD|Monthly|Monthly|1970<br>Jan|2018<br>Jan|
|rExp|Real Exports|∆|Bn. Chained<br>2012 USD|2’495.87|194.34|1’050.63|Federal<br>Reserve<br>Bank of<br>St. Louis|Quarterly|1970<br>Q1|2017<br>Q4|
|rImp|Real Imports|∆|Bn. Chained<br>2012 USD|3’395.12|274.62|1’384.81|Federal<br>Reserve<br>Bank of<br>St. Louis|Quarterly|1970<br>Q1|2017<br>Q4|



_The table provides basic description of the variables used for this work. It is shown whether the variables enter the models as level or as logarithmic growth rate,_ ∆ _, indexing, summary statistics, data source, frequency and sample window. The subscript pC behind the variables represents per capita metrics and the lowercase r in front of some variables represents real values. For the corresponding time series graphs please refer to figure A1._ 

11 

#### _2.2.2. Switzerland_ 

The Swiss real estate company “Wüestpartner” publishes two real estate indices. One for owner occupied flats and one for single family houses, both based on asking prices. The Bank of International Settlement (BIS) publishes one combined real index which is computed, using an unweighted average, based on the two indices from “Wüestpartner”. Because of its broader coverage of the Swiss housing market, the combined index published by BIS was used for the analysis. 

The quarterly Consumer Price Index (CPI) is published by OECD based on data provided by the Swiss Federal Statistical Office. 

The Long -Term Interest Rate (LIR) refers to the average rates on Swiss Confederation bonds of ten years maturity. OECD publishes the metric in their Monthly Monetary and Financial Statistics (MEI), based on data provided by the Swiss National Bank (SNB). 

Population data, provided by the Swiss Federal Statistical Office, is only available on an annual basis. Therefore, it was interpolated to obtain quarterly values. 

The Disposable Income per Head of Population for Switzerland (YpC) needed to be averaged and then deflated by CPI to obtain a real quarterly time series. The same applies to Imports (Imp) and Exports (Exp), which were gathered from the Swiss Feder Statistical Office. Real Gross Domestic Product (rGDP) was deflated by population to obtain per Capita data. 

Table 2 summarizes the time series for Switzerland. 

12 

_Table 2 Data summary for Switzerland_ 

|**Variable**|**Description**|**Level**<br>**or**∆|**Dimension**|**Max**|**Min**|**Mean**|**Source**|**Frequency**|**Start**|**End**|
|---|---|---|---|---|---|---|---|---|---|---|
|rPPI|Property Price<br>Index|∆|Index<br>(2010=100)|123.08|71.61|92.51|BIS –Wüest<br>& Partner|Quarterly|1970<br>Q1|2018<br>Q2|
|CPI|Consumer Price<br>Index|∆|Index<br>(2015=100)|102.8|33.4|78.5|OECD /<br>Federal<br>Statistical<br>Office -<br>Switzerland|Quarterly|1970<br>Q1|2018<br>Q1|
|LIR|Long-Term<br>Interest Rates|Level|Percent, per<br>annum|7.33|-0.51|3.66|Swiss<br>National<br>Bank|Quarterly|1970<br>Q1|2018<br>Q1|
|XRCHFUSD|Exchange Rate<br>1 CHF to USD|∆|Absolute<br>value|1.28|0.23|0.69|Swiss<br>National<br>Bank|Monthly|1970<br>Jan|2018<br>Oct|
|XRCHFEUR|Exchange Rate<br>1 CHF to EUR|∆|Absolute<br>value|0.96|0.60|0.74|Swiss<br>National<br>Bank|Monthly|1999<br>Jan|2018<br>Oct|
|POP|Population|∆|Total<br>Residents|8’419’550|6’168’700|6’989’914|Federal<br>Statistical<br>Office -<br>Switzerland|Annual|1970|2017|
|YpC|Gross National<br>Disposable<br>Income per<br>Head of POP|∆|1000 CHF|80.08|16.89|53.52|AMECO|Annual|1970|2018|
|rGDP|Gross Domestic<br>Product|∆|Mio CHF|175’638|89’780|126’337|State<br>Secretariat<br>for<br>Economic<br>Affairs<br>SECO|Quarterly|1980<br>Q1|2018<br>Q2|
|IPI|Industrial<br>Production<br>Index|∆|Index<br>(2015=100)|107.90|42.42|67.88|Federal<br>Reserve<br>Bank of St.<br>Louis|Quarterly|1970<br>Q1|2017<br>Q3|
|UR|Unemployment<br>Rate|∆|SA UR,<br>percent|5.373|0.002|2.040|State<br>Secretariat<br>for<br>Economic<br>Affairs<br>SECO|Monthly|1970<br>Jan|2017<br>Dec|
|CCI|Consumer<br>Confidence<br>Index|∆|Index<br>(Long-term<br>average<br>=100)|103.2|95.9|100.00|OECD|Monthly|1972<br>Aug|2018<br>Jan|
||||||||Federal<br>Statistical||||
|Imp|Imports|∆|Mio CHF|298’394.0|27’873.4|117’713.3|<br>Office –<br>Switzerland<br>& HSSO|Annual|1970|2017|
|Exp|Exports|∆|Mio CHF|332’137.0|22’140.2|121’347.8|Federal<br>Statistical<br>Office –<br>Switzerland<br>& HSSO|Annual|1970|2017|



_The table provides basic description of the variables used for this work. It is shown whether the variables enter the models as level or as logarithmic growth rate,_ ∆ _, indexing, summary statistics, data source, frequency and sample window. The subscript pC behind the variables represents per capita metrics and the lowercase r in front of some variables represents real values. For the corresponding time series graphs please refer to figure A2._ 

13 

#### _2.2.3. Belgium_ 

The Bank of International Settlement (BIS) publishes a nominal quarterly real estate index (PPI) based on data provided by the Statistical Office of Belgium (STATBEL). The nominal series was chosen because the real quarterly time series is only available from 2005 onwards. Up to 2004 the index only includes existing dwellings. Thereafter, all residential properties are included in the index. To obtain a real data, the time series was deflated by CPI. 

The Long-Term Interest rate is published in OECD’s Monthly Monetary and Financial Statistics (MEI), based on data provided by the National Bank of Belgium (BNB). Up to May 1989, the metric refers to “the average yield off all the securities under the supervision of the Securities Regulation Fund for a residual term of six years and more.” Thereafter, “data refers to the yield on a government security selected by the monetary authorities as the reference for a residual term of 10 years.” 

Population was interpolated to obtain quarterly values. 

The annual time series Gross National Disposable Income per Head of Population (YpC) and the Gross Domestic Product (GDP) were averaged and deflated by CPI. Same applies to the two time series Exports (Exp) and Imports (Imp). Furthermore, GDP was deflated by population to obtain real per Capita data. 

Monthly Unemployment Rate (UR) numbers come from the National Bank of Belgium. They are only available from 1983 onwards. 

Table 3 summarizes the original data for Belgium. 

14 

_Table 3 Data summary for Belgium_ 

|**Variable**|**Description**|**Level**<br>**or**∆|**Dimension**|**Max**|**Min**|**Mean**|**Source**|**Frequency**|**Start**|**End**|
|---|---|---|---|---|---|---|---|---|---|---|
|PPI|Property Price<br>Index|∆|Index<br>(1995=100)|273.93|18.91|117.66|BIS –<br>STATBEL|Quarterly|1970<br>Q1|2018<br>Q1|
|CPI|Consumer Price<br>Index|∆|Index<br>(2015=100)|105.3|19.1|64.4|OECD|Quarterly|1970<br>Q1|2018<br>Q1|
|LIR|Long-Term<br>Interest Rates|Level|Percent, per<br>annum|13.81|0.18|6.71|National<br>Bank of<br>Belgium|Quarterly|1970<br>Q1|2018<br>Q1|
|XREURUSD|Exchange Rate<br>1 EUR to USD|∆|Absolute<br>value|1.58|0.05|1.21|Federal<br>Reserve<br>Bank of St.<br>Louis|Monthly|1999<br>Jan|2017<br>Dec|
|POP|Population|∆|Total<br>Residents|11’372’068|9’655’549|10’245’735|World<br>Bank|Annual|1970|2017|
|YpC|Gross National<br>Disposable<br>Income per<br>Head of POP|∆|1000 EUR –<br>BEF|39.73|3.55|20.56|AMECO|Annual|1970|2018|
|GDP|Gross Domestic<br>Product|∆|Mio. EUR|439’051.9|33’279.5|211’405.6|OECD|Annual|1970|2017|
|IPI|Industrial<br>Production<br>Index|∆|Index<br>(2015=100)|109.7|41.8|69.6|OECD|Quarterly|1970<br>Q1|2018<br>Q1|
|UR|Unemployment<br>Rate|∆|SA UR,<br>Percent|11|6|8.35|National<br>Bank of<br>Belgium|Monthly|1983<br>Jan|2018<br>Jan|
|CCI|Consumer<br>Confidence<br>Index|∆|Index<br>(Long-term<br>average<br>=100)|102.7|97.8|100.0|OECD|Monthly|1973<br>Jan|2018<br>Jan|
|Imp|Imports|∆|Mio. USD|436’412.0|60’351.9|197’440.8|OECD|Annual|1970|2017|
|Exp|Exports|∆|Mio. USD|443’782.1|59’236.6|199’937.6|OECD|Annual|1970|2017|



_The table provides basic description of the variables used for this work. It is shown whether the variables enter the models as level or as logarithmic growth rate,_ ∆ _, indexing, summary statistics, data source, frequency and sample window. The subscript pC behind the variables represents per capita metrics and the lowercase r in front of some variables represents real values. For the corresponding time series graphs please refer to figure A3._ 

15 

#### _2.2.4. Canada_ 

A real, quarterly index, including all type of dwellings, is computed and published by the Bank of International Settlement (BIS). The data originates from the Statistical Office of Canada (Statistics Canada). 

The Long-Term Interest rates time series originates from OECD’s Monthly Monetary and Financial Statistics (MEI) and is based on data from the Bank of Canada. The metric refers to federal government bonds with maturities of more than ten years unit 1982, and thereafter, it refers to the yield of selected Government of Canada 10-year benchmark bonds. The monthly exchange rate for one Canadian Dollar (CAD) to U.S. Dollars (USD) is only available after January 1971 and was averaged. The annual Population time series, gathered from Statistics Canada, was interpolated to obtain quarterly values. Gross National Disposable Income (Y) was available on a quarterly frequency. The time series was deflated by CPI and Population to obtain real per Capita data. The same two operation were applied to GDP. 

Nominal data on Imports and Exports is only available after 1988 by Statistics Canada. The two time series were deflated by CPI. 

Table 4 shows the summarizing statistics for the original data for Canada. 

16 

_Table 4 Data summary for Canada_ 

|**Variable**|**Description**|**Level**<br>**or**∆|**Dimension**|**Max**|**Min**|**Mean**|**Source**|**Frequency**|**Start**|**End**|
|---|---|---|---|---|---|---|---|---|---|---|
|rPPI|Property Price<br>Index|∆|Index<br>(2010 =100)|142.94|36.43|67.30|BIS-<br>Canada<br>Statistics|Quarterly|1970<br>Q1|2017<br>Q4|
|CPI|Consumer Price<br>Index|∆|Index<br>(2015=100)|104.60|16.00|62.90|OECD|Quarterly|1970<br>Q1|2018<br>Q1|
|LIR|Long-Term<br>Interest Rates|Level|Percent, per<br>annum|16.45|1.06|7.03|Bank of<br>Canada|Quarterly|1970<br>Q1|2018<br>Q1|
|XRCADUSD|Exchange Rate 1<br>CAD to USD|∆|Absolute<br>value|1.05|0.63|0.84|Federal<br>Reserve<br>Bank of<br>St. Louis|Monthly|1971<br>Jan|2017<br>Dec|
|POP|Population|∆|Total<br>Residents|36’708’083|21’962’032|28’953’589|Statistics<br>Canada|Annual|1971|2017|
|Y|Gross National<br>Disposable<br>Income|∆|Mio Current<br>CAD|1’207’192|50’388|500’561.35|Statistics<br>Canada|Quarterly|1970<br>Q1|2017<br>Q4|
|GDP|Gross Domestic<br>Prodcut|∆|Mio Current<br>CAD|2’190’328|91’012|918’443|Statistics<br>Canada|Quarterly|1970<br>Q1|2018<br>Q1|
|IPI|Industrial<br>Production<br>Index|∆|Index<br>(2015=100)|106.48|40.19|76.53|Federal<br>Reserve<br>Bank of<br>St. Louis|Quarterly|1970<br>Q1|2018<br>Q1|
|UR|Unemployment<br>Rate|∆|Harmonized<br>UR, Percent|12.93|4.87|7.98|OECD|Quarterly|1970<br>Q1|2018<br>Q1|
|Imp|Imports|∆|Mio. CAD|144’051.2|31’872.5|83’878.6|Statistics<br>Canada|Quarterly|1988<br>Q1|2017<br>Q4|
|Exp|Exports|∆|Mio. CAD|142’272.5|33’975.2|89’356.0|Statistics<br>Canada|Quarterly|1988<br>Q1|2017<br>Q4|



_The table provides basic description of the variables used for this work. It is shown whether the variables enter the models as level or as logarithmic growth rate,_ ∆ _, indexing, summary statistics, data source, frequency and sample window. The subscript pC behind the variables represents per capita metrics and the lowercase r in front of some variables represents real values. For the corresponding time series graphs please refer to figure A4._ 

17 

#### _2.2.5. France_ 

The nominal real estate index, published by BIS, which is based on data provided by the National Institute of Statistics and Economic Studies (INSEE), was used and has been deflated by CPI. 

From 2000 onwards the index includes all types of dwellings. Before this, only existing dwellings have been considered for the index. 

Data on Long-Term Interest Rates refer to the yield of long-term government bonds, traded on the secondary market. The monthly population numbers, collected from _INSEE,_ were aggregated to obtain quarterly data. YpC, Imports and Exports needed to be averaged and deflated by CPI to obtain real quarterly time series. Furthermore, the real GDP, gathered from the online database of the Federal Reserve Bank of St. Louis, was divided by Population, resulting in a per Capita time series. 

Table 5 shows a summary for the original time series for France. 

18 

_Table 5 Data summary for France_ 

|**Variable**|**Description**|**Level**<br>**or**∆|**Dimension**|**Max**|**Min**|**Mean**|**Source**|**Frequency**|**Start**|**End**|
|---|---|---|---|---|---|---|---|---|---|---|
|PPI|Property Price<br>Index|∆|Index<br>(1995=100)|258.09|14.66|120.36|BIS|Quarterly|1970<br>Q1|2017<br>Q4|
|CPI|Consumer Price<br>Index|∆|Index<br>(2015=100)|101.60|14.36|65.79|OECD|Quarterly|1970<br>Q1|2017<br>Q4|
|LIR|Long-Term<br>Interest Rates|Level|Percent, per<br>annum|17.07|0.17|7.26|Bank of<br>France|Quarterly|1970<br>Q1|2017<br>Q4|
|XREURUSD|Exchange Rate 1<br>EUR to USD|∆|Absolute<br>value|1.58|0.05|1.21|Federal<br>Reserve<br>Bank of<br>St. Louis|Monthly|1999<br>Jan|2017<br>Dec|
|POP|Population|∆|1000s of<br>Residents|64’725|52’600|58480.49|INSEE|Monthly|1975<br>Jan|2018<br>Jan|
|YpC|Gross National<br>Disposable<br>Income per Head<br>of POP|∆|1000 EUR –<br>FRF|34.32|2.40|18.95|AMECO|Annual|1970|2017|
|rGDP|Real Gross<br>Domestic<br>Product|∆|Mio. 2010<br>Chained<br>EUR|548’330.1|237’076|396’631.2|Federal<br>Reserve<br>Bank of<br>St. Louis|Quarterly|1975<br>Q1|2017<br>Q4|
|IPI|Industrial<br>Production Index|∆|Index<br>(2015=100)|113.52|60.03|90.97|Federal<br>Reserve<br>Bank of<br>St. Louis|Quarterly|1970<br>Q1|2017<br>Q4|
|UR|Unemployment<br>Rate|∆|SA, percent|10.4|2.9|8.0|INSEE|Quarterly|1975<br>Q1|2017<br>Q4|
|CCI|Consumer<br>Confidence<br>Index|∆|Index<br>(Long-term<br>average<br>=100)|102.77|96.81|100|OECD|Monthly|1973<br>Jan|2018<br>Mar|
|Imp|Imports|∆|Mio. USD|847’313.6|91’346.2|380’519.9|OECD|Annual|1970|2017|
|Exp|Exports|∆|Mio. USD|800’576.0|84’520.9|377’978.9|OECD|Annual|1970|2017|



_The table provides basic description of the variables used for this work. It is shown whether the variables enter the models as level or as logarithmic growth rate,_ ∆ _, indexing, summary statistics, data source, frequency and sample window. The subscript pC behind the variables represents per capita metrics and the lowercase r in front of some variables represents real values. For the corresponding time series graphs please refer to figure A5._ 

19 

#### _2.2.6. Germany_ 

Data which is gathered for Germany needs to be analyzed with great care. Some of the time series show a major bias due to the reunification (“Wiedervereinigung”) of East- and West Germany in 1989. Data prior to this event refers to western Germany due to reasons of data availability. The nominal long-term real estate index, provided by BIS and calculated based on data from the Federal Bank of Germany, was used because the real indices covered only a shorter period of time. Until 1994 it included only properties from cities in western Germany. The index was deflated by CPI. 

Long-Term Interest Rates refer to the yield on outstanding listed federal securities with residual maturities of over nine to ten years, which are traded on the secondary market. Figure A6 in _Appendix A Time Series Plots_ demonstrates the impact of the reunification. There is a clear jump in the population numbers visible in 1990. The annual Population time series was interpolated to obtain quarterly data. Furthermore, Gross National Disposable Income was deflated by CPI and divided by Population to obtain real per Capita data.  The nominal GDP data, collected from the German Federal Statistics Office, _destatis_ , was also deflated by CPI and Population. The annual Import and Export data, which was gathered from the OECD database, was deflated by CPI and averaged to obtain real quarterly time series. 

Table 6 summarizes the time series for Germany. 

20 

_Table 6 Data summary for Germany_ 

|**Variable**|**Description**|**Level**<br>**or**∆|**Dimension**|**Max**|**Min**|**Mean**|**Source**|**Frequency**|**Start**|**End**|
|---|---|---|---|---|---|---|---|---|---|---|
|PPI|Property Price<br>Index|∆|Index<br>(1995<br>=100)|128.82|35.87|83.76|BIS – Federal<br>Bank of<br>Germany|Quarterly|1970<br>Q1|2018<br>Q1|
|CPI|Consumer<br>Price Index|∆|Index<br>(2015=100)|103.2|29.5|69.6|OECD|Quarterly|1970<br>Q1|2018<br>Q1|
|LIR|Long-Term<br>Interest Rates|Level|Percent,<br>per annum|10.80|-0.12|5.71|Federal Bank<br>of Germany|Quarterly|1970<br>Q1|2018<br>Q1|
|XREURUSD|Exchange Rate<br>1 EUR to USD|∆|Absolute<br>value|1.58|0.05|1.21|Federal<br>Reserve Bank<br>of St. Louis|Monthly|1999<br>Jan|2017<br>Dec|
|POP|Population|∆|Total<br>Residents|82’792’351|61’001’164|73’327’939|Federal<br>Statistics<br>Office –<br>Destatis|Annual|1970|2017|
|Y|Gross National<br>Disposable<br>Income|∆|Bn. Current<br>EUR|484.47|52.51|258.11|Federal Bank<br>of Germany|Quarterly|1970<br>Q1|2017<br>Q4|
|GDP|Gross<br>Domestic<br>Product|∆|Bn. EUR|833.24|80.20|416.99|Federal<br>Statistics<br>Office –<br>Destatis|Quarterly|1970<br>Q1|2018<br>Q1|
|IPI|Industrial<br>Production<br>Index|∆|Index<br>(2015=100)|106.76|49.39|73.43|Federal<br>Reserve Bank<br>of St. Louis|Quarterly|1970<br>Q1|2018<br>Q1|
|UR|Unemployment<br>Rate|∆|NOT SA<br>UR,<br>Percent|10.60|0.40|6.22|Bundesagentur<br>für Arbeit|Monthly|1970<br>Jan|2018<br>Jan|
|CCI|Consumer<br>Confidence<br>Index|∆|Index<br>(Long-term<br>average<br>=100)|102.6|96.2|100.0|OECD|Monthly|1973<br>Jan|2018<br>Jan|
|Imp|Imports|∆|Mio. USD|1’562’738.4|176’036.0|655’000.1|OECD|Annual|1970|2017|
|Exp|Exports|∆|Mio. USD|1’810’524.6|163.335.1|718’360.5|OECD|Annual|1970|2017|



_The table provides basic description of the variables used for this work. It is shown whether the variables enter the models as level or as logarithmic growth rate,_ ∆ _, indexing, summary statistics, data source, frequency and sample window. The subscript pC behind the variables represents per capita metrics and the lowercase r in front of some variables represents real values. For the corresponding time series graphs please refer to figure A6._ 

21 

#### _2.2.7. Netherlands_ 

The nominal property price index, published by BIS and based on data provided by Statistics Netherlands, includes all types of dwellings after 1975. Before this, the index only includes sales of houses and apartments brokered by real estate agents. It was deflated by CPI. The Long-Term Interest Rate refers to latest 10-year central government bonds from 1986 onwards. Prior to this date, the data refers to long-term government bonds. The time series is published in the Monthly Monetary and Financial Statistics (MEI), by OECD, based on data from the Central Bank of Netherlands. The population numbers, which were collected from the World Bank, were interpolated from an annual to a quarterly series. Gross National Disposable Income per Head of Population (YpC) and the real Gross Domestic Product (rGDP), collected from the European Commission (AMECO) and OECD respectively, were averaged and made quarterly. The same applies to the Import and Export time series. The latter two and YpC were deflated by CPI. Furthermore, rGDP was deflated by Population to create a per Capita time series. 

Table 7 shows a summary of the time series for the Netherlands. 

22 

_Table 7 Data summary for the Netherlands_ 

|**Variable**|**Description**|**Level**<br>**or**∆|**Dimension**|**Max**|**Min**|**Mean**|**Source**|**Frequency**|**Start**|**End**|
|---|---|---|---|---|---|---|---|---|---|---|
||P Pi||Id||||BIS –||190|2018|
|PPI|roperty rce<br>Index|∆|nex<br>(1995 =100)|283.68|19.80|136.78|Statistics<br>Netherlands|Quarterly|7<br>Q1|<br>Q1|
|CPI|Consumer<br>Price Index|∆|Index<br>(2015=100)|102.2|22.5|66.0|OECD|Quarterly|1970<br>Q1|2018<br>Q1|
|LIR|Long-Term<br>Interest Rates|Level|Percent, per<br>annum|12.00|0.05|5.97|Central<br>Bank of<br>Netherlands|Quarterly|1970<br>Q1|2018<br>Q1|
|XREURUSD|Exchange Rate<br>1 EUR to USD|∆|Absolute<br>value|1.58|0.05|1.21|Federal<br>Reserve<br>Bank of St.<br>Louis|Monthly|1999<br>Jan|2017<br>Dec|
|POP|Population|∆|Total<br>Residents|17’132’854|13’038’526|15’253’060|World Bank|Annual|1970|2017|
|YpC|Gross National<br>Disposable<br>Income per<br>Head of POP|∆|1000 EUR –<br>NLG|44.68|4.86|23.09|AMECO|Annual|1970|2018|
|rGDP|Gross<br>Domestic<br>Product|∆|Constant<br>prices Mio.<br>EUR|2’932’496|1’158’279|2’034’164|OECD|Annual|1970|2017|
|IPI|Industrial<br>Production<br>Index|∆|Index<br>(2015=100)|110.36|50.15|83.12|Federal<br>Reserve<br>Bank of St.<br>Louis|Quarterly|1970<br>Q1|2018<br>Q1|
|UR|Unemployment<br>Rate|∆|Harmonized<br>SA UR,<br>Percent|9.50|3.10|6.02|Federal<br>Reserve<br>Bank of St.<br>Louis|Quarterly|1983<br>Q1|2018<br>Q2|
|CCI|Consumer<br>Confidence<br>Index|∆|Index<br>(Long-term<br>average<br>=100)|102.0|97.1|100.0|OECD|Monthly|1973<br>Jan|2018<br>Jan|
|Imp|Imports|∆|Mio. USD|615’033.8|74’199.6|259’032.9|OECD|Annual|1970|2017|
|Exp|Exports|∆|Mio. USD|712’060.4|71’601.1|293’809.4|OECD|Annual|1970|2017|



_The table provides basic description of the variables used for this work. It is shown whether the variables enter the models as level or as logarithmic growth rate,_ ∆ _, indexing, summary statistics, data source, frequency and sample window. The subscript pC behind the variables represents per capita metrics and the lowercase r in front of some variables represents real values. For the corresponding time series graphs please refer to figure A7._ 

23 

#### _2.2.8. United Kingdom_ 

The CPI deflated Property Price Index (rPPI), from the BIS data base was used for the UK. The index includes all types of dwellings in the whole country and is available on a quarterly basis. Therefore, no further data preparation was needed for the rPPI. 

The Long-Term Interest Rate refers to the par yield or par rate for bonds with a maturity of ten years. The par yield or rate is defined as the yield for which the price of a bond equals its face value. This metric is published in the Monthly Monetary and Financial Statistics (MEI), by OECD. The data used as for the publication is provided by the Bank of England. The population numbers, gathered from the World Bank database, were interpolated from annual to quarterly data. The nominal time series for the Gross National Disposable Income per Head of Population (YpC), was collected from the Office for National Statistics and deflated by the CPI. The same data source was used for the Gross Domestic Product per Capita and also deflated by the CPI. The annual Export and Import time series were averaged to obtain a quarterly series and deflated by the CPI. 

Summary statistics for the UK are shown in table 8. 

24 

_Table 8 Data summary for the United Kingdom_ 

|**Variable**|**Description**|**Level**<br>**or**∆|**Dimension**|**Max**|**Min**|**Mean**|**Source**|**Frequency**|**Start**|**End**|
|---|---|---|---|---|---|---|---|---|---|---|
|rPPI|Property Price<br>Index|∆|Index<br>(2010<br>=100)|121.73|21.87|61.14|BIS –<br>Residential<br>Property<br>Prices|Quarterly|1970<br>Q1|2018<br>Q1|
|CPI|Consumer Price<br>Index|∆|Index<br>(2015=100)|104.8|8.6|59.4|OECD|Quarterly|1970<br>Q1|2018<br>Q1|
|LIR|Long-Term<br>Interest Rates|Level|Percent, per<br>annum|16.02|0.84|7.75|Bank of<br>England|Quarterly|1970<br>Q1|2018<br>Q1|
|XRGBPUSD|Exchange Rate<br>1 GBP to USD|∆|Absolute<br>value|2.62|1.10|1.74|Federal<br>Reserve<br>Bank of St.<br>Louis|Monthly|1971<br>Jan|2017<br>Dec|
|XRGBPEUR|Exchange Rate<br>1 GBP to EUR|∆|Absolute<br>value|1.67|1.10|1.36|Bank of<br>England|Quarterly|1999<br>Q1|2017<br>Q4|
|POP|Population|∆|Total<br>Residents|66’022’273|55’663’250|58’860’322|World<br>Bank|Annual|1970|2018|
|Y|Gross National<br>Disposable<br>Income per<br>Head of POP|∆|Current<br>GBP|4’966|144|2’294.6|Office for<br>National<br>Statistics -<br>UK|Quarterly|1970<br>Q1|2017<br>Q4|
|GDPpC|Gross Domestic<br>Product per<br>Capita|∆|Current<br>Market<br>Prices|7’895|238|3’611.71|Office for<br>National<br>Statistics -<br>UK|Quarterly|1970<br>Q1|2018<br>Q2|
|IPI|Industrial<br>Production<br>Index|∆|Index<br>(2012=100)|117.20|67.10|98.14|Federal<br>Reserve<br>Bank of St.<br>Louis|Monthly|1969<br>Dec|2016<br>Dec|
|UR|Unemployment<br>Rate|∆|ILO UR,<br>Percent|11.9|3.4|7.03|Office for<br>National<br>Statistics -<br>UK|Monthly|1971<br>Feb|2018<br>Jan|
|CCI|Consumer<br>Confidence<br>Index|∆|Index<br>(Long-term<br>average<br>=100)|103.2|96.5|100|OECD|Monthly|1974<br>Jan|2018<br>Jan|
|Imp|Imports|∆|Mio. USD|859’906.9|113’635.8|398’909.5|OECD|Annual|1970|2017|
|Exp|Exports|∆|Mio. USD|794’925.9|123’592.8|389’021.9|OECD|Annual|1970|2017|



_The table provides basic description of the variables used for this work. It is shown whether the variables enter the models as level or as logarithmic growth rate,_ ∆ _, indexing, summary statistics, data source, frequency and sample window. The subscript pC behind the variables represents per capita metrics and the lowercase r in front of some variables represents real values. For the corresponding time series graphs please refer to figure A8._ 

25 

## **3. Methodology** 

The following chapter describes the different methodologies which were applied in this work. First, the evaluation and calibration strategy for the models which were implemented is presented. Furthermore, the ordinary least squares (OLS) regression model is briefly described in general, followed by a justification of the variable selection and a detailed introduction of the different model specifications. Thereafter, the concept of the threshold autoregressive (TAR) model is presented and the exact model setup for this work is 

established, along with the introduction of the autoregressive (AR) model. In addition, the log periodic power law singularity (LPPLS) model, which is used for the definition of the threshold variable, is described. 

And last, the weighting procedures for the ensemble models are defined. 

### 3.1. Calibration and Evaluation Strategy 

To avoid a look-ahead bias in the forecasting results the different models were calibrated using an expanding window (Pesaran & Timmermann, 2002). The general idea behind an expanding window regression is to calibrate a model on an initial observation window of size N. The observation window is then gradually increased by one observation until N+p observations are included. These steps result in p+1 models, which were calibrated on N, N+1, N+2,.., N+p observations. 

Each of these models is used to calculate a one observation ahead forecast, resulting in p+1 forecasts. 

Hence, the regression model used for forecasting the variable of interest 𝑦#$% is calibrated on the data 



Where ℎ∈{1,2, … ,12} represents the different descriptive variables. This method allows us to compute numerous forecasts, without including a look-ahead bias in our models, because the forecast is repeatedly conducted out-of-sample. 

26 

To assess the forecasting performance of the different models, two different metrics were calculated. 

First, the Root Mean Squared Errors (RMSE) were calculated for every model and multiplied by 100 to express the results as a percentage: 



Where 𝑦% and 𝑦E% are the actual and fitted values respectively. Furthermore, suffix  𝑗 ∈ {𝐵𝑒𝑙𝑔𝑖𝑢𝑚, 𝐶𝑎𝑛𝑎𝑑𝑎, 𝐹𝑟𝑎𝑛𝑐𝑒, 𝐺𝑒𝑟𝑚𝑎𝑛𝑦, 𝑁𝑒𝑡ℎ𝑒𝑟𝑙𝑎𝑛𝑑𝑠, 

𝑆𝑤𝑖𝑡𝑧𝑒𝑟𝑙𝑎𝑛𝑑, 𝑈𝑛𝑖𝑡𝑒𝑑 𝐾𝑖𝑛𝑔𝑑𝑜𝑚, 𝑈𝑛𝑖𝑡𝑒𝑑 𝑆𝑡𝑎𝑡𝑒𝑠} corresponds to the different housing markets and _k_ to the different models which are explained in detail in the following sections. Moreover, the occurrence of the correct prediction sign was determined. For each model the following metric was calculated: 



Despite its simplicity, this metric gives interesting insights on whether a model is able to predict periods of price increases and decreases correctly. Although, not the exact deviation of the actual values is measured, the metric gives an indication whether general changing trends are captured correctly by a model. 

Although these two metrics give a good general indication of a models forecasting performance they do not allow for any statement about the statistical significance of the differences of the predictive accuracy. To test whether there are any statistically significant differences between models, an adjusted Diebold-Mariano (DIEBOLD & MARIANO, 1995), (Harvey, Leybourne, & Newbold, 1997) was used. 

The purpose is to test the null hypothesis of equal predictive accuracy. The quality of the forecasts is judged on some specified loss function _g(ei,t),_ where _(e1,t, e2,t); t =1,…,n_ are two sets of errors produced by _s-_ steps ahead forecasts. For this work the mean squared error was set as the standard of prediction quality, meaning _g(e) = e_<sup>_2_</sup> _._ 

27 

Defining the loss differential 



one can write the null hypothesis as 

and the alternative hypothesis as 



The test is based on the observed sample mean: 



The modified Diebold-Mariano test statistic is then: 



Where, 𝑉0𝑑̅1 is the variance of the observed sample mean, which is defined by a bootstrap estimate in this work because the asymptotic estimates used in the original test generated invalid negative variance estimates. The statistic is then compared with the critical values from a Student’s t distribution with (n-1) degrees of freedom. 

The tests were carried out pairwise for the seven OLS models, which will be introduced in section _3.2.1. Regression Models_ , resulting in 42 test statistics for each country and the significance level was set at a _= 0.05_ . 

For a detailed derivation of the test statistic please refer to (Harvey et al., 1997). 

28 

### 3.2. OLS 

Changes in real estate prices have often been explained by external macroeconomic variables. The most commonly used approach to take these variables into account is the Ordinary Least Squares (OLS) regression model. Despite the simplicity, such models often show acceptable descriptive and forecasting results (Ghysels et al., 2013) (Song, Witt, & Jensen, 2003). However, the selection of the correct explanatory variables is crucial for the performance of such a model. Therefore, data preparation and selection have been a principal task in this work. 

The general model setup of a multiple linear regression model has the following form: 



Where the coefficients 𝛽p, 𝛽(, … 𝛽j are estimated by ordinary least squares (OLS), meaning that the sum of squared residuals is minimized. 

Seven different specifications were calculated for each economy using the expanding window approach, introduced in chapter _3.1. Calibration and Evaluation Strategy_ . 

To use balanced proportions of the data for the calibration and for the forecast assessment it was decided to work with an initial window size N of 80 observations and p was set at 92 for the OLS regression models. 

The following section describes the different regression models and justifies the selection of the variables included. 

29 

#### _3.2.1. Regression Models_ 

Seven different linear regression models including up to twelve explanatory variables are implemented for each real estate market. The variables have been chosen due to different reasons: 

First, the consumer price index (CPI) generally gives a good indication of the national price level. It is therefore assumed that its development has explanatory properties for real estate prices as well. Furthermore, the long-term interest rate variable (LIR) is chosen because of its direct relation on people’s saving behavior and to mortgage conditions. The assumption is therefore that a lower interest rate would increase real estate prices. The different exchange rates (XR) are included as a relative measure of comparison to other economies. Whereby an increasing exchange rate can have both negative and positive implications on a nation. The change of population (POP) is taken into account because it represents migration effects. The changes of gross national disposable income (Y) and gross domestic product (GDP), both standardized in terms of per capita, are commonly used productivity measures connected to price levels and are therefore included. The changes in industrial production index (IPI) can be interpreted as a measure of the national industry’s development. Its importance on the entire economy can therefore not be disputed. The effect of a change of the unemployment rate (UR) on a nation’s economy have been widely discussed in literature. It is therefore expected that also real estate prices are affected by changing unemployment rates. (Cox & Ludvigson, 2018) find that beliefs bear some relation to changes of house prices. The consumer confidence index (CCI) is integrated as a measure to represent the population’s beliefs. Last, the changes of imports (IMO) and exports (EXP) are included due to the implications these two variables have on the economy. 

Due to data unavailability the models had to be reduced for certain countries. The detailed models implemented, for every housing market are described in _Appendix B Detailed OLS Results_ . 

The general model setup is as follows: 

𝑀(𝐿rst = 𝐿): 

- ∆rPPIx,y$z = ∆CPIx,yi| + LIRx,yi| + ∆XR. . .x,yi|+ ∆POPx,yi| + ∆rYx,yi| + ∆rGDPpCx,yi| + ∆IPIx,yi| + ∆URx,yi| + ∆CCIx,yi| + ∆rIMPx,yi| + ∆rEXPx,yi| 

30 

Where _Lmax_ represents the maximal lag of the variables included and _j_ again the different countries. Furthermore, the prefix ∆, where ∆𝑥d = log ~~(~~ t‹ ), represents the log growth rate of t‹Œ• the corresponding time series, which was used to induce stationarity, as described in chapter _2.1. Variable Description_ . 

The integer 𝑠∈{0,1,3} determines, whether the model is used for one, two or four quarter forecasts. However, the focus of this work is clearly set one four-quarter forecasts due to the relatively slow development of real estate prices. Nevertheless, one and two quarter forecasts were calculated for personal reference but since these results do not contribute to the fundamental research question they are not presented in this thesis. 

The procedures explained in sections _3.1. and 3.2._ are applied to seven model variations of the model above which are all based on the same time series. However, different lags of the time series are included for the calibration of the seven models. 

The first three models are of the form 𝑀(𝐿rst = 1), 𝑀(𝐿rst = 2) and 𝑀(𝐿rst = 3) respectively. Meaning that they include lags up to one, two and three of all variables respectively. 

The remaining four model variations are all based on the first model and include additional ••‘ ’“’ = lags of different variables. Model four is of the form 𝑀(𝐿rst = 1, 𝐿rst = 2, 𝐿rst 2, 𝐿””•rst = 2, 𝐿••’rst = 2, 𝐿–—’rst = 2), meaning the model includes lag one of all variables and additionally lag two of the long-term interest rates, population, consumer confidence index, imports and exports. Model five is a reduced form of the previous model, without the second order lag of population, consumer confidence index and imports: 𝑀(𝐿rst = 1, 𝐿••‘rst = 2, 𝐿–—’rst = 2). The last two models take into account the importance of interest rates on housing prices which has been discussed in different publications (Reichert, 1990) (Harris, 1989). Therefore, models six, 𝑀(𝐿rst = 1, 𝐿••‘rst = 3), and seven, 𝑀(𝐿rst = 1, 𝐿••‘rst = 4), include lags one of all variables and additionally lags two and three and two, three and four of interest rates respectively. 

31 

### 3.3. TAR 

Many macroeconomic time series contain nonlinear characteristics and therefore, the description of such time series with linear Autoregressive (AR) models is not sufficient (Gibson & Nur, 2011). 

In 1978, Tong introduced the family of Threshold Autoregressive (TAR) models (Tong & Yeung, 1991),  (Tong, 2012). Using these models, one is able to constitute regime-switching properties of macroeconomic time series. 

The general model setup of a TAR model looks as follows: 



Where Zt is a threshold variable, L is the order of the model and s equals the forecasting steps. The regime-switching in the model is induced when the threshold variable Zt exceeds a certain value th. 

The definition of this threshold value has been heavily debated since the model was first introduced. Usually, a lagged value of the time series, 𝑦di , is used as threshold variable for the calibration of the model. However, there is no consensus on the definition of d and Zt so far (Tsay, 1989). 

For this work it was assumed that the current state of the dependent variable, and therefore the threshold variable, is defined at every time t by the Log Periodic Power Law Singularity (LPPLS) model (Johansen & Sornette, 1999) (Johansen et al., 2000). The LPPLS model determines whether a time series is in a normal or in a bubble state at time t and allows therefore to distinguish between regimes. 

Please refer to chapter _3.4. Log Periodic Power Law Singularity Model_ for a short description of the LPPLS model. 

Like fore the regression models, also for the TAR model an expanding window was applied for the calibration. Furthermore, the forecasting performance of the TAR models was assessed by the same two metrics, 𝑅𝑀𝑆𝐸>,? and  𝜃>,?, as introduced in chapter _3.1 Calibration and Evaluation Strategy_ . 

32 

#### _3.3.1. TAR and AR Model_ 

As mentioned before in section _3.2.1. Regression Models,_ the focus is set on four quarter forecasts. Therefore, the TAR model was implemented with s = 4. Furthermore, the order of the TAR models was set at four to capture seasonality adequately. 

The models which were implemented for the different countries had the following structure: 

∆𝑟𝑃𝑃𝐼d$£ = š<sup>𝛽</sup> 𝛾<sup>p</sup> p<sup>+ 𝛽</sup> + 𝛾<sup>(</sup> (<sup>∗∆𝑟𝑃𝑃𝐼</sup> ∗∆𝑟𝑃𝑃𝐼<sup>d</sup> d<sup>+ 𝛽</sup> + 𝛾*<sup>*</sup> ∗∆𝑟𝑃𝑃𝐼<sup>∗∆𝑟𝑃𝑃𝐼</sup> di(<sup>di(</sup> + 𝛾<sup>+ 𝛽</sup> ¤<sup>¤</sup> ∗∆𝑟𝑃𝑃𝐼<sup>∗∆𝑟𝑃𝑃𝐼</sup> di*<sup>di*</sup> + 𝛾<sup>+ 𝛽</sup> £<sup>£</sup> ∗∆𝑟𝑃𝑃𝐼<sup>∗∆𝑟𝑃𝑃𝐼</sup> di¤<sup>di¤</sup> , 𝑓𝑜𝑟 𝑡ℎ𝑉𝐴𝑅> 0<sup>, 𝑓𝑜𝑟 𝑡ℎ𝑉𝐴𝑅≤0</sup> 

The external threshold variable _thVar_ was determined by the LPPLS model. _thVar_ is a binary variable containing only zeros and ones, whereby the ones represent bubble and the zeros normal regimes. 

Furthermore, the initial fitting window for the TAR modelling needed to be increased to 140 observations because of missing variability of the threshold variable for some countries. However, the final window size was kept constant at observation 172, resulting in 33 forecasted values. 

To determine whether the threshold variable adds value to the forecasting performance of the TAR model, a simple autoregressive (AR) model was implemented and the forecasting accuracy was compared using the two metrics and the Diebold Mariano test introduced in chapter _3.1 Calibration and Evaluation Strategy._ 

The models implemented for the different countries had the following structure: 

∆𝑟𝑃𝑃𝐼d$£ = 𝛽p + 𝛽( ∗∆𝑟𝑃𝑃𝐼d + 𝛽* ∗∆𝑟𝑃𝑃𝐼di( + 𝛽¤ ∗∆𝑟𝑃𝑃𝐼di* + 𝛽£ ∗∆𝑟𝑃𝑃𝐼di¤ 

For reasons of comparability the same fitting window was used as for the implementation of the TAR model. 

### 3.4. Log Periodic Power Law Singularity Model 

The log periodic power law singularity (LPPLS) model (Johansen et al., 2000; Johansen & Sornette, 1999) has been  applied to detect periods of housing bubbles in the different real estate markets. The model identifies bubbles based on two “signatures”. “First, a transient, faster than exponential growth processes ending in a finite time singularity, resulting from 

33 

amplification mechanisms that take the form of price-to-return positive feedback (Corsi & Sornette, 2014; Lin & Sornette, 2013; Sornette, Takayasu, & Zhou, 2003). […] Second, accelerating oscillations stemming from the existence of a discrete hierarchy in the organization of agents (Sornette, 1998; Zhou, Sornette, Hill, & Dunbar, 2005) […], or from the interplay between the inertia of transforming information into decision together with nonlinear momentum and price-reversal trading styles (Ide & Sornette, 2002) […].“ (Diego Ardila, 2016) These two elements establish a signature of a bubble regime in the analyzed time series, where a correction can be triggered by any small disturbance. 

Whilst the definition of bubbles above is rather mathematical, a more intuitive one is given by Didier Sornette and Ryan Woodward (Sornette & Woodard, 2010): 

“During a housing price bubble, homebuyers think that a home that they would normally consider too expensive for them is now an acceptable purchase because they will be compensated by significant further price increases. They will not need to save as much as they otherwise might, because they expect the increased value of their home to do the saving for them. First-time homebuyers may also worry during a housing bubble that if they do not buy now, they will not be able to afford a home later.” (Sornette & Woodard, 2010) 

The general LPPLS model for a time series p(t) is defined as follows (Jiang et al., 2010): 



Where the time to the critical time _tc_ is measured by _x = tc-t._ Furthermore, the faster than exponential growth dynamics, due to positive feedback mechanisms, are described by the term _x_<sup>_m_</sup> _,_ where _m_ represents the acceleration of the bubble. The increasing oscillations in turn, are specified by the log periodic term _cos(_ w _ln(x) +_ F _)._ 

The qualified filter conditions were specified as follows: 





34 

The fitting was done with different time windows _dt_ . Since some variation of the threshold variable was desirable for the implementation of the TAR model, _dt_ was set at 2700 days, which equals approximately seven years and five months. 

It should be mentioned, that for the German housing market no “positive” bubble was detected using the said specifications over the whole observation period. However, the model detected a period where the prices decrease faster than exponentially, a so called “negative” bubble. This period was used for the differentiation of regimes for the TAR model implementation. 

Since the fitting of the LPPLS model is not the main topic of this thesis several simplifications were made for the definition of the threshold variable _thVar_ , and no detailed explanation of the theory will be provided. Please refer to (Jiang et al., 2010) for a summary of the theory and the presentation of several applications. Furthermore, a detailed description of the calibration of the LPPLS model can be found in (Filimonov & Sornette, 2013) 

### 3.5. Model Combination and Weighting 

To combine the best performing OLS, which is determined by the metrics and the test introduced in chapter _3.1. Evaluation and Calibration Strategy,_ model with the TAR model, a weighting method was applied. The final fitted values are calculated as a weighted combination of the fitted values of the OLS and the TAR model: 



Where 𝑤“•²,%,> and 𝑤³´‘,%,> are the non-constant weights for the OLS and TAR models, respectively, whereby _i_ indicates time and _j_ the different housing markets. 

Two different approaches for the calculation of the weights were implemented: (I) The weights were calculated on a rolling forecasting window of fixed size of 15 observations and (II) the forecasting window was expanded from initially 15 observations to totally 48 observations which were used for the calculation of the weights. 

35 

For both approaches 𝑀𝑆𝐸%,>,? and  𝜃%,>,? were compared to calculate the weights: 



Where 𝑀𝑆𝐸%,>,? equals the Mean Squared Prediction Error at every time _i_ : 



For both approaches the initial calibration window was set from observation 141 to 154. With each forecasting step the weights were recalculated. This step was repeated 33 times, always using the latest 15 observations for the calculation of the weights for the first approach. Whereas, for the second approach the number of observations used for the computation of the weights, was increased gradually from 15 to 48. 

Therefore, both implementations resulted in 33 combined forecasts. 

36 

## **4. Results** 

In the following chapter the results from the different models are presented. First, the forecasting performance of the different OLS models is displayed and the selection of the best performing model is justified. The detailed results and the exact model structure for each housing market are presented in _Appendix B Detailed OLS Results._ Secondly, the TAR and AR modelling results for the different housing markets are shown. And finally, the performance of the combined weighted models is presented and compared to the standalone OLS and TAR models. 

### 4.1. OLS – Results 

For the expanding OLS models an initial window size of 80 and a final window size of 172 observations were chosen, resulting in 93 forecasts for each model. These forecasts were used to calculate the two metrics: (I) the root mean squared error (RMSE) and (II) the percentage amount of times the forecast had the correct prediction sign 𝜃. 

As mentioned before, this work focuses on four quarter forecasts. Tables 9 and 10 show summarizing statistics of the four-quarter forecasting performance for the seven models across all eight housing markets. 

_Table 9 RMSE Ratios for OLS Models_ 

|**Mo**<br>**Country**|**del**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Belgium**|1.00|1.05|1.16|1.01|1.00|0.99|1.03|
|**Canada**|1.00|1.01|0.99|0.95|0.98|0.93|0.95|
|**France**|1.00|0.88|0.81|0.87|1.01|1.01|1.03|
|**Germany**|1.00|1.05|1.14|1.01|1.03|1.05|1.11|
|**Netherlands**|1|1.17|1.23|1.12|0.97|0.93|0.91|
|**Switzerland**|1.00|1.16|1.60|1.04|1.02|0.99|0.98|
|**United Kingdom**|1|1.07|1.22|1.04|1.03|1.00|0.98|
|**United States**|1|0.96|0.99|0.95|1.00|1.00|0.96|



_The table shows the ratios of the RMSEs of the seven different models compared to the RMSE of model one for the eight housing markets. They are computed based on 93 out-of-sample forecasts. The models with the smallest RMSE of each country are highlighted in green._ 

37 

_Table 10 Percentage of Correct Prediction Sign for OLS Models_ 

|**Mo**<br>**Country**|**del**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Belgium**|70%|71%|73%|71%|73%|73%|72¨%|
|**Canada**|66%|66%|64%|64%|63%|64%|65%|
|**France**|65%|70%|74%|71%|64%|62%|61%|
|**Germany**|61%|64%|61%|68%|55%|55%|59%|
|**Netherlands**|68%|71%|57%|72%|72%|74%|71%|
|**Switzerland**|58%|51%|45%|49%|53%|53%|57%|
|**United Kingdom**|65%|61%|55%|64%|60%|65%|68%|
|**United States**|54%|66%|65%|66%|53%|53%|53%|



_The table shows the percentage of correct prediction signs,_ 𝜃 _, of the 93 four-quarter forecasts for models one to seven for the eight housing markets. The models with the highest percentage value_ 𝜃 _of each country are highlighted in green._ 

Based on tables 9 and 10, there is no single OLS model with superior performance across all countries. Furthermore, the tables show that the performance of the models differs quite substantially between the different housing markets. 

= The smallest overall root mean squared error was achieved with model six, 𝑀(𝐿rst 

••‘ 1, 𝐿rst = 3). 

The differences in forecasting accuracy were investigated with the modified Diebold-Mariano test, as introduced in Chapter _3.1. Evaluation and Calibration Strategy_ . It was used to test the null hypothesis of same level of predictive accuracy for models _i_ and _j_ against the alternative hypothesis that model _i_ is less accurate than model _j_ , where 𝑖, 𝑗∈{1, … ,7}. Table 11 summarizes the results of the 336 test statistics, 42 per country, which were analyzed at a significance level of a _= 0.05_ . The percentage numbers in each cell of the table were calculated by dividing the number of rejections of _H0_ for all countries per pair by the total number of countries. 

If one looks at the rows of the table, the models with the largest percentage numbers represent models _j_ which have a higher forecasting accuracy than the others _i_ . On the other hand, when the columns are considered, large percentage numbers represent models _i_ which are outperformed in terms of prediction accuracy by models _j_ . 

The table shows that the models with highest overall forecasting accuracy are model four, 

𝑀(𝐿rst = 1, 𝐿••‘rst = 2, 𝐿’“’rst = 2, 𝐿””•rst = 2, 𝐿••’rst = 2, 𝐿–—’rst = 2), and model six, 𝑀(𝐿rst = 1, 𝐿••‘rst = 3), with average rejections rates of _H0_ of 29 and 27 percent 

38 

respectively. Furthermore, these two models also have the lowest average percentage numbers per column, 8.3 and 6.3 percent for models four and six respectively, meaning that they are the least outperformed models. 

It has to be mentioned that these results do not suggest any evidence of statistical dominance of one model over the others. This behavior might reflect the fact that all the models are based on the same variables and therefore only differ in terms of lag variations. 

The detailed results of all the test statistics for every housing market are presented in _Appendix C Diebold-Mariano results._ 

_Table 11 Diebold-Mariano test: Summarized Results: % Rejection rate of H0: Same level of accuracy, in favor of HA: Model i less accurate than model j_ 

|**Mo**<br>**Model j**|**del i**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**1**||25%|50%|12.5%|0%|0%|12.5%|
|**2**|0%||50%|0%|0%|0%|0%|
|**3**|12.5%|12.5%||12.5%|12.5%|12.5%|12.5%|
|**4**|12.5%|50%|62.5%||12.5%|25%|12.5%|
|**5**|12.5%|37.5%|50%|12.5%||0%|0%|
|**6**|25%|37.5%|50%|12.5%|25%||12.5%|
|**7**|12.5%|37.5%|50%|0%|0%|0%||



_The table shows the summarized results from Diebold-Mariano tests. The percentage of rejections across all countries of H0:Models i and j have same level of accuracy, in favor of HA: Model i is less accurate than model j, is displayed._ 

Nevertheless, these results and the consideration of the RMSEs led to the selection of model six, 𝑀(𝐿rst = 1, 𝐿••‘rst = 3), for the ensemble modelling.  Figure two shows the plots of the fitted vs. the actual values of the selected OLS model for the eight different housing markets. 

As it can be observed, there are important differences among countries. 

In Switzerland, the model strongly overestimates the real values in the 90s. After this period, the plot shows, that the model does not accurately reproduce the increase of real estate prices in the early 2000s. For the US, the model represents the steady increase of real estate prices up to approximately 2005 reasonably. On the contrary, the decrease in prices in the following years is not reproduced at all by model 6. The Belgian housing market is modeled reasonably over the whole observation period. This is also visible from the relatively high  𝜃 value in table 10. In Canada and France, the model does a reasonable job capturing the trend, but fails 

39 

to reflect the rather volatile development of the returns in these indices. The decrease of the German real estate prices in the late 90s is not modeled correctly by model 6. Furthermore, the fitted values differ quite substantially from the actual ones after this period, resulting in a relatively poor forecasting performance. On the contrary, the development of the Dutch housing prices is modeled with a relatively high accuracy which is also represented by the high 𝜃 value in table 10. The last plot on the right side in figure 2, shows that the development of the UK housing market is modeled reasonably. However, the extreme values of the price development are not represented accurately. 

40 

_Figure 2 Fitted vs. Real values OLS model 6_ 



<!-- Start of picture text -->
Switzerland Fitted vs. Real values Model 6 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.03<br>0.01<br>−0.01<br>−0.03<br><!-- End of picture text -->



<!-- Start of picture text -->
US Fitted vs. Real values Model 6 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.04<br>0.02<br>0.00<br>−0.04<br><!-- End of picture text -->



<!-- Start of picture text -->
Belgium Fitted vs. Real values Model 6 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>France Fitted vs. Real values Model 6 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>Netherlands Fitted vs. Real values Model 6 Q4<br>0.04<br>0.02<br>0.00<br>−0.04<br>0.04<br>0.02<br>0.00<br>−0.04<br><!-- End of picture text -->



<!-- Start of picture text -->
Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.04<br>0.02<br>0.00<br>−0.04<br><!-- End of picture text -->



<!-- Start of picture text -->
Canada Fitted vs. Real values Model 6 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.04<br>0.02<br>0.00<br>−0.04<br><!-- End of picture text -->



<!-- Start of picture text -->
Germany Fitted vs. Real values Model 6 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.02<br>0.01<br>0.00<br>−0.01<br><!-- End of picture text -->

**United Kindgom  Fitted vs. Real values Model 6 Q4** 



<!-- Start of picture text -->
Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.06<br>0.02<br>−0.02<br>−0.06<br><!-- End of picture text -->

_Figure 2 shows the plots of the fitted (red) vs. the real (blue) values of the property price index resulting from OLS model six,_ 𝑀(𝐿rst = 1, 𝐿••‘rst = 3) _, for the eight different housing markets._ 

41 

### 4.2. TAR and AR - Results 

As explained in section _3.3.1. TAR Model,_ the initial window size had to be increased due to limited variability of the threshold variable for some housing markets. This led to a reduced forecasting window of 33 observations for the calculation of the two metrics. Therefore, the resulting metrics of the TAR and AR models are not directly comparable with the ones of the OLS models. 

The forecasting window was set between observations 142 and 174, meaning between the first quarter of 2005 and the first quarter of 2013. 

The values of the two metrics for the TAR and AR models are presented in table 12, as well as the p-values of the Diebold Mariano test, where the null hypothesis of same level of accuracy was tested against the alternative hypothesis that the TAR model is more accurate than the AR model. 

The plots of the fitted values of the TAR model versus the real values are shown in figure 3. 

_Table 12 RMSEs and_ 𝜃 _for TAR and AR Model and Diebold Mariano test results_ 

|**Model**|**TAR Root mean**<br>**squared error %**<br>**RMSE**|**TAR Correct**<br>**prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|**AR Root mean**<br>**squared error %**<br>**RMSE**|**AR Correct**<br>**prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|**Diebold Mariano test**<br>**p-value**|
|---|---|---|---|---|---|
|**Belgium**|0.82%|79%|0.88%|55%|0.007642|
|**Canada**|1.94%|64%|1.94%|58%|0.4997|
|**France**|1.29%|73%|1.30%|73%|0.4745|
|**Germany**|0.85%|58%|0.91%|48%|0.08066|
|**Netherlands**|1.46%|79%|1.54%|76%|0.09754|
|**Switzerland**|0.98%|76%|1.07%|76%|0.04087|
|**United**<br>**Kingdom**|2.67%|70%|2.75%|67%|0.2303|
|**United**<br>**States**|1.78%|73%|1.85%|73%|0.1597|



_The table above shows the RMSEs for four quarters ahead forecasts for the TAR and the AR model for the eight different housing markets. They are computed on 33 forecasts. Furthermore, the percentage of correct prediction signs_ 𝜃 _is shown. The last column displays the p-value of the Diebold Mariano test, where H0: Same levely of predictive accuracy, was tested against HA: The TAR model is more accurate than the AR model. The tests where H0 was rejected in favor of HA  at the_ a _= 0.05 level are highlited in green._ 

Thes results presented in table 12 suggest that the TAR model generally outperforms a simple AR model, although the difference in forecasting accuracy is only statistically significant in two countries at the a _= 0.05_ significance level. 

42 

On average the inclusion of the threshold variable reduces the RMSE from 1.53 % to 1.47% and increases the occurrence of the correct prediction sign from 65.75 % to 71.5%.  The focus is therefore set on the TAR model in the following sections. 

Table 12 above also demonstrates that the forecasting performance of the implemented TAR model differs substantially for the different housing markets. The 𝜃 value for Belgium, France, the Netherlands, Switzerland and the United states lies above 70 percent, whereas the correct prediction sign for Germany is only forecasted in approximately 58 percent of the cases. It has to be pointed out again, as mentioned in section _3.4. Log Periodic Power Law Singularity Model,_ that for the German housing market no “positive bubble” was determined by the LPPLS model. However, the model detected several periods of a strong price decrease, so called “negative bubbles”, which were used to define two different regimes for the implementation of the TAR model. The resulting bubble signals of the LPPL analysis are presented in figures 4 to 11 in section _4.3. Ensemble Model Results._ 

Figure 3 illustrates these results. The fitted values of the Swiss housing market follow the actual values quite precisely, whilst the model continually underestimates the real values for the German market. 

Furthermore, it is interesting to see that the model captures the strong price decrease after 2008 in the US market with much higher accuracy than the selected OLS model does (see figure 2). For the Belgian market it is observable that the general trend is modeled with acceptable precision. However, the strong decreases in prices in 2008 are not represented accurately. The plot for Canada shows a similar behavior. Also, the general trend of the French housing market is reproduced quite precisely. Nonetheless, the strong decrease in prices in 2009 is not reproduced accurately by the model. 

The model has the highest 𝜃 value for the Dutch housing market, this high accuracy of the prediction sign is also visible in figure 3. 

From the last plot in the right column it is visible that that changes from price increases to decreases are modeled with acceptable precision for the United Kingdom with the TAR model. 

43 

_Figure 3 Fitted vs. Real values TAR model_ 

**Switzerland Fitted vs. Real values TAR Model Q4** 



<!-- Start of picture text -->
Real values<br>Fitted values<br>2006 2008 2010 2012<br>0.04<br>0.02<br>0.00<br>−0.02<br>−0.04<br><!-- End of picture text -->

**United States Fitted vs. Real values TAR Model Q4** 



<!-- Start of picture text -->
Real values<br>Fitted values<br>2006 2008 2010 2012<br>0.04<br>0.02<br>0.00<br>−0.04<br><!-- End of picture text -->

**Belgium Fitted vs. Real values TAR Model Q4** 



<!-- Start of picture text -->
Real values<br>Fitted values<br>2006 2008 2010 2012<br>0.02<br>0.01<br>0.00<br>−0.01<br><!-- End of picture text -->

**Canada Fitted vs. Real values TAR Model Q4** 



<!-- Start of picture text -->
Real values<br>Fitted values<br>2006 2008 2010 2012<br>0.04<br>0.02<br>0.00<br>−0.02<br><!-- End of picture text -->

**France Fitted vs. Real values TAR Model Q4** 



<!-- Start of picture text -->
Real values<br>Fitted values<br>2006 2008 2010 2012<br>0.04<br>0.02<br>0.00<br>−0.02<br><!-- End of picture text -->

**Germany Fitted vs. Real values TAR Model Q4** 



<!-- Start of picture text -->
Real values<br>Fitted values<br>2010 2012 2014 2016<br>0.02<br>0.01<br>0.00<br>−0.01<br><!-- End of picture text -->

**Netherlands Fitted vs. Real values TAR Model Q4** 

**United Kingdom Fitted vs. Real values TAR Model Q4** 



<!-- Start of picture text -->
Real values Real values<br>Fitted values Fitted values<br>2006 2008 2010 2012 2006 2008 2010 2012<br>0.06<br>0.02<br>0.00 0.02<br>−0.02 −0.02<br>−0.04<br>−0.06<br><!-- End of picture text -->

_Figure 3 shows the plots of the fitted (red) vs. the real (blue) values of the property price index resulting from the TAR model for the eight different housing markets._ 

44 

### 4.3. Ensemble Model Results 

The final step was to combine the two models by a weighting approach. The two different methods explained in section _3.5. Model Combination and Weighting_ were applied to the eight housing markets, using OLS model six, 𝑀(𝐿rst = 1, 𝐿••‘rst = 3), and the TAR model since it slightly outperformed the more simple AR model. 

Tables 12 and 13 show the resulting metrics from 33 forecasts, using a fixed rolling window and an expanding window for the computation of the weights respectively. As a reference, the two metrics resulting from OLS model 𝑀(𝐿rst = 1, 𝐿••‘rst = 3) and the TAR model for the 

same forecasting period are also presented in the two tables. 

The forecasting window was set between observations 157 and 189, representing the fourth quarter of 2008 and the fourth quarter of 2016. 

It needs to be pointed out that the results of the two evaluation metrics for OLS model 

𝑀(𝐿rst = 1, 𝐿••‘rst = 3) and the TAR model in tables 12 and 13 are not the same as in sections _4.1. OLS -Results_ and _4.2. TAR-Results_ because, as mentioned above, different forecasting windows are used for the calculations. 

_Table 13 RMSEs and_ 𝜃 _for combined model with fixed rolling window for weighting_ 

|**Metric**<br>**Country**|**%**<br>**RMSEOLS**|**% correct**<br>**pred.**<br>**signOLS**|**%**<br>**RMSETAR**|**% correct**<br>**pred.**<br>**signTAR**|**%**<br>**RMSECOMBINED**|**Ratio to**<br>**RMSEOLS**|**Ratio to**<br>**RMSETAR**|**% correct**<br>**pred.**<br>**signCOMBINED**|
|---|---|---|---|---|---|---|---|---|
|**Belgium**|2.00%|39%|1.00%|64%|1.02%|0.51|1.03|61 %|
|**Canada**|1.67%|85%|1.65%|79%|1.63%|0.98|0.99|85%|
|**France**|1.63%|55%|1.08%|76%|1.10%|0.67|1.02|76%|
|**Germany**|1.02%|52%|0.85%|55%|0.90%|0.88|1.05|61%|
|**Netherlands**|2.17%|45%|1.50%|85%|1.53%|0.71|1.02|76%|
|**Switzerland**|1.25%|88%|0.97%|78%|0.94%|0.76|0.97|85%|
|**United**<br>**Kingdom**|2.02%|48%|2.00%|67%|1.78%|0.88|0.89|67%|
|**United**<br>**States**|2.24%|55%|1.52%|73%|1.50%|0.67|0.98|73%|



_The table above shows the % RMSEs and the percentage of correct prediction signs_ 𝜃 _for the OLS model, the TAR model and the combined model. Columns six and seven display the ratios of the RMSEs of the combined model to the RMSEs of the OLS and TAR model respectively. All the metrics are computed on 33 forecasts using a rolling window of 15 observations for the calculation of the weights._ 

45 

_Table 14 RMSEs and_ 𝜃 _for combined model with expanding window for weighting_ 

|**Metric**<br>**Country**|**%**<br>**RMSEOLS**|**% correct**<br>**pred.**<br>**signOLS**|**%**<br>**RMSETAR**|**% correct**<br>**pred.**<br>**signTAR**|**%**<br>**RMSECOMBINED**|**Ratio to**<br>**RMSEOLS**|**Ratio to**<br>**RMSETAR**|**% correct**<br>**pred.**<br>**signCOMBINED**|
|---|---|---|---|---|---|---|---|---|
|**Belgium**|2.00%|39%|1.00%|64%|1.02%|0.51|1.03|61%|
|**Canada**|1.67%|85%|1.65%|79%|1.62%|0.97|0.98|85%|
|**France**|1.63%|55%|1.08%|76%|1.07%|0.66|1.00|73%|
|**Germany**|1.02%|52%|0.85%|55%|0.91%|0.90|1.07|58%|
|**Netherlands**|2.17%|45%|1.50%|85%|1.52%|0.70|1.02|76%|
|**Switzerland**|1.25%|88%|0.97%|78%|0.94%|0.76|0.97|82%|
|**United**<br>**Kingdom**|2.02%|48%|2.00%|67%|1.81%|0.90|0.91|67%|
|**United**<br>**States**|2.24%|55%|1.52%|73%|1.52%|0.68|1.00|73%|



_The table above shows the % RMSEs and the percentage of correct prediction signs_ 𝜃 _for the OLS model, the TAR model and the combined model. Columns six and seven display the ratios of the RMSEs of the combined model to the RMSEs of the OLS and TAR model, respectively. All the metrics are computed on 33 forecasts using an expanding window ranging from 15 to 48 observations for the calculation of the weights._ 

The first rows in tables 12 and 13 show that the ensemble model has a superior forecasting performance than OLS model 𝑀(𝐿rst = 1, 𝐿••‘rst = 3) for the Belgian housing market. However, the TAR model outperforms the combined model, in terms of correct prediction sign and root mean squared error for the given forecasting period. This applies to both weighting methods. 

Figure 4 underlines that both combined models perform very similar and that both weighting approaches lead to similar weights. It is also visible that, due to significantly larger weights of the TAR model, the fitted values of the ensemble models are very close to the ones from the TAR model. 

46 

_Figure 4 Results Belgium_ 



<!-- Start of picture text -->
a)<br><!-- End of picture text -->



<!-- Start of picture text -->
b)<br><!-- End of picture text -->



<!-- Start of picture text -->
c)<br><!-- End of picture text -->



<!-- Start of picture text -->
d)<br><!-- End of picture text -->



<!-- Start of picture text -->
e)<br><!-- End of picture text -->

_Figure 4 shows the results from the selected OLS model, the TAR model, and the ensemble models for the Belgian housing market. a) and b) show the fitted values for the ensemble models, calibrated using a rolling window and an expanding window respectively. The rolling window has a fixed size 15, whereas the expanding window ranges from 15 to 48 observations. c) and d) show the calibrated weights for the corresponding weighting approach. e) shows the development of the real property price index for this housing market. The grey shaded area represents periods where the LPPLS model has identified bubbles. The rolling and expanding window approaches have similar forecasting performance, as the weights are not strongly affected by the chosen weighting methods._ 

The combined models for the Canadian market perform better than the selected OLS model 

regarding the RMSE, and better than the TAR model, regarding both, the RMSE and the 𝜃 value. Nevertheless, also the two combined models fail to reproduce the price decreases in the given forecasting period and only take positive values. 

The plots of the development of the weights in figure 5 show that the distribution of the weights is much more balanced than for example the Belgian Market. This fact leads to ensemble models which include similar proportions of forecasts of both, the selected OLS and the TAR model. Interestingly the use of the expanding window for the calculation of the 

47 

weights smoothened the development of them. Furthermore, with the inclusion of more observations for the weighting process, the weights converge towards parity. 

_Figure 5 Results Canada_ 



<!-- Start of picture text -->
a)<br><!-- End of picture text -->



<!-- Start of picture text -->
b)<br><!-- End of picture text -->



<!-- Start of picture text -->
c)<br><!-- End of picture text -->



<!-- Start of picture text -->
d)<br><!-- End of picture text -->



<!-- Start of picture text -->
e)<br><!-- End of picture text -->

_Figure 5 shows the results from the selected OLS model, the TAR model and the ensemble models for the Canadian housing market. a) and b) show the fitted values for the ensemble models, calibrated using a rolling window and an expanding window respectively. The rolling window has a fixed size of 15, whereas the expanding window ranges from 15 to 48 observations. c) and d) show the calibrated weights for the corresponding weighting approach. e) shows the development of the real property price index for this housing market. The grey shaded area represents periods, where the LPPLS model has identified bubbles. The figures show that both combined models are influenced relatively evenly by the TAR and the OLS model over the majority of the forecasting period._ 

48 

For the French housing market, the two combined models show a slight difference in forecasting performance. Approach one outperforms approach two regarding the 𝜃 value, whereas the second approach results in a smaller RMSE. 

In comparison to the selected OLS model, both combined models clearly have superior forecasting properties, respecting both metrics. Compared to the TAR model, the forecasts from the first method result in a slightly higher RMSE and the same 𝜃 value. Whereas the forecasting performance of the second approach is worse in terms of 𝜃 values but has a lower RMSE. Figure 6 shows that the TAR model seems to dominate the OLS model in general. However, it is also observable that the OLS model is weighted stronger, when the rolling window is used for the calculation. 

49 

_Figure 6 Results France_ 



<!-- Start of picture text -->
a)<br><!-- End of picture text -->



<!-- Start of picture text -->
b)<br><!-- End of picture text -->



<!-- Start of picture text -->
c)<br><!-- End of picture text -->



<!-- Start of picture text -->
d)<br><!-- End of picture text -->



<!-- Start of picture text -->
e)<br><!-- End of picture text -->

_Figure 6 shows the results from the selected OLS model, the TAR model, and the ensemble models for the French housing market. a) and b) show the fitted values for the ensemble models, calibrated using a rolling window and an expanding window respectively. The rolling window has a fixed size 15, whereas the expanding window ranges from 15 to 48 observations. c) and d) show the calibrated weights for the corresponding weighting approach. e) shows the development of the real property price index for this housing market. The grey shaded area represents periods where the LPPLS model has identified bubbles. The plots showing the development of the weights demonstrate that the fitted values of the combined model are mainly dominated by the TAR model for both combined model approaches._ 

_This can also be seen in the fitted vs. real value plots where the fitted values of the combined models follow the fitted values of the TAR model very closely._ 

Tables 12 and 13 show that both combined modelling approaches for the German housing market outperform the OLS and the TAR model in terms of 𝜃 values. Furthermore, the 

RMSEs of the combined model are about 20 percent smaller than the ones resulting from the OLS model. However, both combined models are outperformed by the TAR models in terms of RMSE. As stated earlier, in section _4.2. TAR – Results,_ no “positive bubble” was detected by the LPPL model for the German market. Therefore, the period undergoing a “negative 

50 

bubble” was used for the differentiation between the different regimes. Furthermore, the plots showing the development of the weights in figure 7 demonstrate that for both combined models there is a transition from heavy weights for the OLS model to a dominating TAR model. It is also observable that after this transition, the TAR model is weighted much stronger for the combined model, which is calibrated on a rolling window than for the one which uses an expanding window. 

_Figure 7 Results Germany_ 



<!-- Start of picture text -->
a)<br><!-- End of picture text -->



<!-- Start of picture text -->
b)<br><!-- End of picture text -->



<!-- Start of picture text -->
c)<br><!-- End of picture text -->



<!-- Start of picture text -->
d)<br><!-- End of picture text -->



<!-- Start of picture text -->
e)<br><!-- End of picture text -->

_Figure 7 shows the results from the selected OLS model, the TAR model, and the ensemble models for the German housing market. a) and b) show the fitted values for the ensemble models, calibrated using a rolling window and an expanding window respectively. The rolling window has a fixed size 15, whereas the expanding window ranges from 15 to 48 observations. c) and d) show the calibrated weights for the corresponding weighting approach. e) shows the development of the real property price index for this housing market. The red shaded area represents a period, where the LPPL model has detected a negative bubble, i.e. a strong downwards trend in prices._ 

_The plots show how the combined models are first dominated by the OLS model and that this changes around the year 2010. After that transition point, the TAR model outweighs the OLS model until around 2016, where the combined models are influenced by both models relatively equally._ 

51 

_Figure 8 Results Netherlands_ 



<!-- Start of picture text -->
a)<br><!-- End of picture text -->



<!-- Start of picture text -->
b)<br><!-- End of picture text -->



<!-- Start of picture text -->
c)<br><!-- End of picture text -->



<!-- Start of picture text -->
d)<br><!-- End of picture text -->



<!-- Start of picture text -->
e)<br><!-- End of picture text -->

_Figure 8 shows the results from the selected OLS model, the TAR model, and the ensemble models for the Dutch housing market. a) and b) show the fitted values for the ensemble models, calibrated using a rolling window and an expanding window respectively. The rolling window has a fixed size 15, whereas the expanding window ranges from 15 to 48 observations. c) and d) show the calibrated weights for the corresponding weighting approach. e) shows the development of the real property price index for this housing market. The grey shaded area represents periods where the LPPLS model has identified bubbles. The figure sows, how for increasing observation numbers, the weights for the TAR model increase too. Furthermore, it is observable that both combined models behave very similarly._ 

For the given forecasting period the Dutch housing market is best modeled by the TAR model, as it can be seen from tables 12 and 13.  However the two combined models only slightly underperform the TAR model in terms of RMSE. The superiority of the threshold model might be explained by the strong price decreases in the period after 2010 which are not accurately represented by the OLS model. Figure 8 and tables 12 and 13 show that both combined models have very similar forecasting properties and weights. 

52 

_Figure 9 Results Switzerland_ 



<!-- Start of picture text -->
a)<br><!-- End of picture text -->



<!-- Start of picture text -->
b)<br><!-- End of picture text -->



<!-- Start of picture text -->
c)<br><!-- End of picture text -->



<!-- Start of picture text -->
d)<br><!-- End of picture text -->



<!-- Start of picture text -->
e)<br><!-- End of picture text -->

_Figure 9 shows the results from the selected OLS model, the TAR model, and the ensemble models for the Swiss housing market. a) and b) show the fitted values for the ensemble models, calibrated using a rolling window and an expanding window respectively. The rolling window has a fixed size 15, whereas the expanding window ranges from 15 to 48 observations. c) and d) show the calibrated weights for the corresponding weighting approach. e) shows the development of the real property price index for this housing market. The grey shaded area represents periods where the LPPLS model has identified bubbles. The plots show how the weights, resulting from the first approach for the combined model, undergo a transition in 2013, whereas for the second approach, only a slight decrease (TAR weights) or increase (OLS weights) of the weights is observable_ 

For the Swiss housing market, the two ensemble models dominate the OLS and the TAR model regarding the RMSE. However, the ensemble models underperform compared to the OLS model in terms of the 𝜃 value. 

Tables 12 and 13 and figure 9 also demonstrate that the rolling window model combination slightly outperforms the second combined model. Interestingly, this superiority is caused by a stronger weighting of the OLS model in the second half of the forecasting period as shown in the weight plots in figure 9. 

53 

_Figure 10 Results United Kingdom_ 



<!-- Start of picture text -->
a)<br><!-- End of picture text -->



<!-- Start of picture text -->
b)<br><!-- End of picture text -->



<!-- Start of picture text -->
c)<br><!-- End of picture text -->



<!-- Start of picture text -->
d)<br><!-- End of picture text -->



<!-- Start of picture text -->
e)<br><!-- End of picture text -->

_Figure 10 shows the results from the selected OLS model, the TAR model, and the ensemble models for the housing market of the United Kingdom. a) and b) show the fitted values for the ensemble models, calibrated using a rolling window and an expanding window respectively. The rolling window has a fixed size 15, whereas the expanding window ranges from 15 to 48 observations. c) and d) show the calibrated weights for the corresponding weighting approach. e) shows the development of the real property price index for this housing market. The grey shaded area represents periods where the LPPLS model has identified bubbles._ 

_The development of weights plots show how the expanding window method smoothens the weights during the whole forecasting period. Whilst the variation of the weights for the first approach is impossible to ignore, the weights, resulting from the second approach, stay more or less constant over the whole forecasting period._ 

Tables 12 and 13 suggest that the ensemble models show a superior forecasting performance than the OLS and the TAR model for the defined forecasting period in the UK housing market. The RMSEs of the ensemble models are approximately 20 percent lower than for the two other models. Furthermore, the 𝜃 value is almost 20 percent higher for the ensemble models than for the OLS model. Although the weights differ quite substantially for the two model combinations, as figure 10 shows, the forecasting performance of the two is very similar. 

54 

_Figure 11 Results United States_ 



<!-- Start of picture text -->
a)<br><!-- End of picture text -->



<!-- Start of picture text -->
b)<br><!-- End of picture text -->



<!-- Start of picture text -->
c)<br><!-- End of picture text -->



<!-- Start of picture text -->
d)<br><!-- End of picture text -->



<!-- Start of picture text -->
e)<br><!-- End of picture text -->

_Figure 11 shows the results from the selected OLS model, the TAR model, and the ensemble models for the housing market of the United States. a) and b) show the fitted values for the ensemble models, calibrated using a rolling window and an expanding window respectively. The rolling window has a fixed size 15, whereas the expanding window ranges from 15 to 48 observations. c) and d) show the calibrated weights for the corresponding weighting approach. e) shows the development of the real property price index for this housing market. The grey shaded area represents periods where the LPPLS model has identified bubbles._ 

_The figure shows that both approaches for the combined model have a very similar forecasting performance and that the weights are not strongly affected by the different weighting methods. Furthermore, it is observable that both combined models are strongly influenced by the TAR model._ 

Figure 11 and the last rows of tables 12 and 13 demonstrate that also the US housing market is best represented by the ensemble models. Furthermore, the forecasting properties between the OLS and the TAR model differ substantially. The inferiority of the OLS model compared to the TAR model is also represented in the weight plots, which are shown in figure 11. For both combined modelling approaches, the TAR model is weighted much heavily over the whole forecasting period. 

55 

## **5. Discussion** 

In the following, the main findings from section _4. Results_ are summarized and discussed. Special attention is thereby given to section _4.3. Combined Model Results._ Therefore, when not stated otherwise, the results refer to the forecasting window used in the said chapter, meaning observations 157 to 189. 

Furthermore, limitations of the methodology applied are listed and explained accordingly. 

### 5.1. Main Findings 

As stated earlier, the main goal of this thesis was to analyze the potential domestic forecasting performance improvements, achieved by the weighted combination of a linear regression model and a threshold autoregressive model compared to a stand-alone regression model. The analysis of the forecasting accuracy of the seven OLS regression models showed substantial differences across the eight housing markets. The application of the DieboldMariano test and the comparison of the root mean squared prediction error and the occurrence of the correct prediction sign however led to the selection of an OLS model with acceptable forecasting properties for all the economies. 

The weighted combination of the selected OLS model with the threshold autoregressive model led to an increased forecasting performance compared to the forecasting properties of the stand-alone OLS model, regarding the root mean squared prediction error, for all eight countries analyzed. On average the RMSE was reduced by approximately 24 percent by both combined weighting models compared to the OLS model. 

Furthermore, except for the Swiss residential real estate market, also the 𝜃 value, the percentage of correct forecasting signs, of the ensemble models was at least as good as the one resulting from the OLS models. On average it was increased by 31 and 29 percent for ensemble model approach one and two respectively. 

However, the combined models do not result in superior forecasting properties compared to the TAR model for all countries which were analyzed. 

The first approach of the ensemble model, using a rolling window of 15 observations for the weighting, created larger RMSEs compared to the TAR model in four countries. The second methodology, where the weights were calculated by an expanding window, resulted in larger RMSEs in three of the eight economies. On average though, both approaches reduced the RMSE across all countries by approximately 0.5 percent. A similar pattern was observed for the 𝜃 value. 

56 

The forecasting performance of the TAR model can be partly explained by the autoregressive components of the real estate prices. Different publications (Ghysels et al., 2013) (Crawford & Fratantoni, 2003) (Nagaraja, Brown, & Zhao, 2011) provide evidence that real estate prices can be modeled with acceptable accuracy by autoregressive models. Secondly, the comparison to the simple AR model in chapter _4.2. TAR and AR - Results_ also suggests that the inclusion of the threshold variable, and therefore allowing for different regimes, contributes to the forecasting performance of the TAR model. Although, the differences in forecasting accuracy are only statistically relevant in two countries, the overall forecasting performance is increased by the inclusion of the threshold variable. 

The results show that a simple average of the two forecasts outperforms the stand-alone OLS model in general significantly. Furthermore, also the stand-alone TAR model is outperformed by the ensemble models on average, although less prominently. 

The initial hypothesis that the two completely different approaches, one only including macroeconomic variables and the other being solely based on past real estate returns and a threshold variable, would be complementary, and that the combination of the two would improve the model performance, can therefore be confirmed. 

This follows the research of (Clemen, 1989) who finds that simple combinations of forecasts often improve the predictions based on a single model. 

It is observable that for most economies the TAR model is responsible for the improvement of forecasting properties. This is unsurprising since real estate prices, like many other macroeconomic variables, are known to undergo sudden regime changes (Crawford & Fratantoni, 2003). Thanks to the bubble indicators, which were derived by the LLPLS model (Johansen et al., 2000; Johansen & Sornette, 1999), the regime changes were represented accurately. 

Interestingly, for the Swiss housing market, the ensemble model with larger weights for the OLS model outperforms the second ensemble model, in which more weight is put one the TAR model. 

### 5.2. Limitations 

It is certainly the case that the differences amongst the models which were implemented for the eight housing markets, due to the limited data availability, reduce the comparability of the 

57 

results across countries. However, country internal, the OLS model were consistent in their variables. 

Moreover, the multiple testing problem, which is induced by the separate hypothesis tests for the OLS model pairs, needs to be addressed. For each model pair test the chance of a false rejection of the null hypothesis is a, whereas the chance of at least one false rejection across all eight countries is much higher (Wasserman, 2004). To avoid this issue, one could apply the very conservative Bonferroni Method (Wasserman, 2004) to the different pairwise tests. Furthermore, the simplifications which were made regarding the definition of the threshold variable have to be mentioned. The LPPLS model allows for a variety of specifications and bubble criteria definitions. The implementation of the LPPLS model is therefore a topic for a master thesis by itself, like it has been done by (Kuert, 2016). 

Moreover, it has to be pointed out that the results are analyzed on a specific forecasting window, ranging from 2008 to 2016. Whether these results extend to other periods is debatable and subject to further research. 

58 

## **6. Conclusion** 

In this thesis, the goal was to develop a short-term (four quarters ahead) forecasting model for eight OECD housing markets. The basic idea was to combine an ordinary least squares regression model with a threshold autoregressive model by using a weighted combination of the two forecasts, a so-called ensemble modelling approach. 

All of the models were calibrated using an expanding window, allowing for multiple out of sample forecasts and therefore avoiding an in-sample look-ahead bias. 

Seven different OLS models were calibrated and the one with the overall highest forecasting performance was selected for the ensemble model. The forecasting performance was thereby assessed by the Diebold-Mariano test, the root mean squared prediction error and the occurrence of the correct forecasting sign. 

The second model included in the ensemble model was a threshold autoregressive model of order four, TAR(4). Where the threshold variable for the TAR(4) model was determined by the log periodic power law singularity (LPPLS) model. 

In general, the forecasting performance of the ensemble model increased, compared to the linear regression models. The root mean squared prediction error (RMSE) was reduced by approximately 24 percent, whereas the occurrence of the correct prediction sign was increased by 30 percent on average. The two different weighting methods did not substantially affect the forecasting properties. 

For most economies the ensemble forecasts are dominated by the TAR model. However, the best forecasting results for the Swiss housing market, during the specified forecasting period, were achieved with higher weights for the OLS forecasts 

Following this work, it is suggested to apply the ensemble modelling approach with different models for the housing market. Moreover, the option of combining more than two models could also be considered. 

Furthermore, the effect of varying forecasting periods needs to be analyzed since in this thesis the model performance was evaluated on a single observation window. 

And finally, the effect of different bubble criteria and LPPLS specifications on the forecasting properties requires further research. 

59 

## **7. Acknowledgments** 

I would like to thank all the people who supported me during this thesis, in particular my supervisor Dr. Diego Ardila Alvarez. His profound knowledge in different areas and his openness for questions and discussions were a great help throughout this thesis. Furthermore, my thanks go to Professor Didier Sornette for the possibility to write my thesis at his chair. The weekly breakfast meetings introduced me to interesting new research areas and have always been a very pleasant event. 

Also, I would like to thank Jan-Christian Gerlach for the fitting of the LPPLS model. 

60 

## **8. List of references** 

Ardila, D. (2016). _DYNAMIC APPROACHES TO REAL ESTATE BUBBLES: METHODS AND EMPIRICAL STUDIES._ (Doctor of Sciences), ETH Zurich, Zurich. 

- Ardila, D., Sanadgol, D., Cauwels, P., & Sornette, D. (2017). Identification and critical time forecasting of real estate bubbles in the USA. _Quantitative Finance, 17_ (4), 613-631. Retrieved from <Go to ISI>://WOS:000395715500009. doi:10.1080/14697688.2016.1207796 

- Case, K. E., & Shiller, R. J. (1990). Forecasting Prices and Excess Returns in the HousingMarket. _Areuea Journal-Journal of the American Real Estate & Urban Economics Association, 18_ (3), 253-273. Retrieved from <Go to ISI>://WOS:A1990ET20100002. 

- Clemen, R. T. (1989). Combining forecasts: A review and annotated bibliography. _International Journal of Forecasting, 5_ (4), 559-583. 

- Corsi, F., & Sornette, D. (2014). Follow the money: The monetary roots of bubbles and crashes. _International Review of Financial Analysis, 32_ , 47-59. 

- Cox, J., & Ludvigson, S. C. (2018). _Drivers of the Great Housing Boom-Bust: Credit Conditions, Beliefs, or Both?_ Retrieved from 

- Crawford, G. W., & Fratantoni, M. C. (2003). Assessing the forecasting performance of regime-switching, ARIMA and GARCH models of house prices. _Real Estate Economics, 31_ (2), 223-243. 

CS. (2018). _Global Wealth Report 2018_ . Retrieved from 

DIEBOLD, F., & MARIANO, R. (1995). Comparing predictive accuracy. journal of business and Economics Statistics, v. 13. 

- Durlauf, S. N., & Blume, L. (2010). _Macroeconometrics and time series analysis_ . Basingstoke: Palgrave Macmillan. 

- Filimonov, V., & Sornette, D. (2013). A stable and robust calibration scheme of the logperiodic power law model. _Physica A: Statistical Mechanics and its Applications, 392_ (17), 3698-3707. 

- Ghysels, E., Plazzi, A., Valkanov, R., & Torous, W. (2013). Forecasting real estate prices. In _Handbook of economic forecasting_ (Vol. 2, pp. 509-580): Elsevier. 

- Gibson, D., & Nur, D. (2011). Threshold autoregressive models in finance: a comparative approach. 

- Harris, J. C. (1989). The effect of real rates of interest on housing prices. _The Journal of Real Estate Finance and Economics, 2_ (1), 47-60. Retrieved from 

   - <u>https://doi.org/10.1007/BF00161716. doi:10.1007/bf00161716</u> 

- Harvey, D., Leybourne, S., & Newbold, P. (1997). Testing the equality of prediction mean squared errors. _International Journal of Forecasting, 13_ (2), 281-291. Retrieved from <u>https://EconPapers.repec.org/RePEc:eee:intfor:v:13:y:1997:i:2:p:281-291.</u> 

- Ide, K., & Sornette, D. (2002). Oscillatory finite-time singularities in finance, population and rupture. _Physica A: Statistical Mechanics and its Applications, 307_ (1-2), 63-106. 

- Jiang, Z.-Q., Zhou, W.-X., Sornette, D., Woodard, R., Bastiaensen, K., & Cauwels, P. (2010). Bubble diagnosis and prediction of the 2005–2007 and 2008–2009 Chinese stock market bubbles. _Journal of economic behavior & organization, 74_ (3), 149-162. 

- Johansen, A., Ledoit, O., Sornette, D. J. I. J. o. T., & Finance, A. (2000). Crashes as critical points. _3_ (02), 219-255. 

- Johansen, A., & Sornette, D. (1999). Critical crashes. _arXiv preprint cond-mat/9901035_ . 

61 

- Kuert, R. (2016). _Analysis of real estate bubbles in eight residential markets._ (MSc), ETH Zurich, Zurich. 

- Leblanc, M., & Bokreta, R. J. A. a. S. (2009). Analysis of the US real estate market: timevarying estimation and forecast of the S&P Case-Shiller composite 20 cities. 

- Lin, L., & Sornette, D. (2013). Diagnostics of rational expectation financial bubbles with stochastic mean-reverting termination times. _The European Journal of Finance, 19_ (5), 344-365. 

- Nagaraja, C. H., Brown, L. D., & Zhao, L. H. (2011). An autoregressive approach to house price modeling. _The Annals of Applied Statistics, 5_ (1), 124-149. 

- Nelson, C. R., & Plosser, C. R. (1982). Trends and random walks in macroeconmic time series: some evidence and implications. _Journal of monetary economics, 10_ (2), 139-162. 

- OECD. (2019). OECD (2019), Consumer confidence index (CCI) (indicator). doi: 10.1787/46434d78-en (Accessed on 18 March 2019). Retrieved from <u>https://data.oecd.org/leadind/consumer-confidence-index-cci.htm</u> 

- Pesaran, M. H., & Timmermann, A. (2002). Market timing and return prediction under model instability. _Journal of Empirical Finance, 9_ (5), 495-510. Retrieved from <u>http://www.sciencedirect.com/science/article/pii/S0927539802000075.</u> doi:https://doi.org/10.1016/S0927-5398(02)00007-5 

- Reichert, A. K. (1990). The impact of interest rates, income, and employment upon regional housing prices. _The Journal of Real Estate Finance and Economics, 3_ (4), 373-391. Retrieved from https://doi.org/10.1007/BF00178859. doi:10.1007/bf00178859 

S&P. (2019). S&P CoreLogic Case - Shiller U.S. National Home Pirce NSA Index. Retrieved from <u>https://us.spindices.com/indices/real-estate/sp-corelogic-case-shiller-usnational-home-price-nsa-index</u> 

- Samuels, J. D., & Sekkel, R. M. (2017). Model Confidence Sets and forecast combination. _International Journal of Forecasting, 33_ (1), 48-60. Retrieved from <u>http://www.sciencedirect.com/science/article/pii/S0169207016300747.</u> doi:https://doi.org/10.1016/j.ijforecast.2016.07.004 

- Song, H., Witt, S. F., & Jensen, T. C. (2003). Tourism forecasting: accuracy of alternative econometric models. _International Journal of Forecasting, 19_ (1), 123-141. Retrieved from <u>http://www.sciencedirect.com/science/article/pii/S0169207001001340.</u> doi:https://doi.org/10.1016/S0169-2070(01)00134-0 

- Sornette, D. (1998). Discrete-scale invariance and complex dimensions. _Physics reports, 297_ (5), 239-270. 

- Sornette, D., Takayasu, H., & Zhou, W.-X. (2003). Finite-time singularity signature of hyperinflation. _Physica A: Statistical Mechanics and its Applications, 325_ (3-4), 492506. 

- Sornette, D., & Woodard, R. (2010). _Financial Bubbles, Real Estate Bubbles, Derivative Bubbles, and the Financial and Economic Crisis_ , Tokyo. 

- Tong, H. (2012). _Threshold models in non-linear time series analysis_ (Vol. 21): Springer Science & Business Media. 

- Tong, H., & Yeung, I. (1991). THRESHOLD AUTOREGRESSIVE MODELLING IN CONTINUOUS TIME. _Statistica Sinica, 1_ (2), 411-430. Retrieved from <u>http://www.jstor.org/stable/24304018.</u> 

- Tsay, R. S. (1989). Testing and Modeling Threshold Autoregressive Processes. _Journal of the American Statistical Association, 84_ (405), 231-240. Retrieved from <Go to ISI>://WOS:A1989U244700028. doi:Doi 10.2307/2289868 

- Wasserman, L. (2004). All of Statistics. In (pp. 165-168). 

62 

Zhou, W.-X., Sornette, D., Hill, R. A., & Dunbar, R. I. (2005). Discrete hierarchical organization of social group sizes. _Proceedings of the Royal Society B: Biological Sciences, 272_ (1561), 439-444. 

63 

## **9. Appendix** 

- A. Time Series Plots 

64 

_Figure A1 Time series for the United States_ 

Levels 



Log growth rate (D) 



_Figure A1 shows the real measures which were collected for the US, where rPPI is the real property price index, CPI the consumer price index, LIR the long-term interest rates, XRUSDCAD the exchange rate between one USD and Canadian Dollars, XRUSDEUR the exchange rate between one USD and Euros, POP the population in thousands, rYpC the real gross disposable income per capita, rGDPpC the real gross domestic product per capita, IPI the industrial production index, UR the unemployment rate in percent, CCI the consumer confidence index, rEXP the real value of exports and rImp the real value of imports._ 

_The lower part of the figure shows the log growth rate of the corresponding measures._ 

65 

_Figure A2 Time series for Switzerland_ 

Levels 



<!-- Start of picture text -->
Log growth rate (D) D) )<br><!-- End of picture text -->



<!-- Start of picture text -->
Log growth rate (D) D) )<br><!-- End of picture text -->

_Figure A2 shows the real measures which were collected for Switzerland, where rPPI is the real property price index, CPI the consumer price index, LIR the long-term interest rates, XRCHFUSD the exchange rate between one CHF and USD, XRCHFEUR the exchange rate between one CHF and Euros, POP the population, rYpC the real gross disposable income per capita, rGDPpC the real gross domestic product per capita, IPI the industrial production index, UR the unemployment rate in percent, CCI the consumer confidence index, rEXP the real value of exports and rImp the real value of imports. The lower part of the figure shows the log growth rate of the corresponding measures._ 

66 

_Figure A3 Time series for Belgium_ 

Levels 





<!-- Start of picture text -->
Log growth rate (D)<br><!-- End of picture text -->





_Figure A3 shows the real measures which were collected for Belgium, where rPPI is the real property price index, CPI the consumer price index, LIR the long-term interest rates, XREURUSD the exchange rate between one euro and USD, POP the population in hundred thousands, rYpC the real gross disposable income per capita, rGDPpC the real gross domestic product per capita, IPI the industrial production index, UR the unemployment rate in percent, CCI the consumer confidence index, rEXP the real value of exports and rImp the real value of imports._ 

_The lower part of the figure shows the log growth rate of the corresponding measures._ 

67 

_Figure A4 Time series for Canada_ 

Levels 





#### Log growth rate (D) 



_Figure A4 shows the real measures which were collected for Canada, where rPPI is the real property price index, CPI the consumer price index, LIR the long-term interest rates, XRCADUSD the exchange rate between one Canadian Dollar and USD, POP the population, rYpC the real gross disposable income per capita, rGDPpC the real gross domestic product per capita, IPI the industrial production index, UR the unemployment rate in percent, CCI the consumer confidence index, rEXP the real value of exports and rImp the real value of imports._ 

_The lower part of the figure shows the log growth rate of the corresponding measures._ 

68 

_Figure A5 Time series for France_ 

Levels 





<!-- Start of picture text -->
Log growth rate (D)<br><!-- End of picture text -->





_Figure A5 shows the real measures which were collected for France, where rPPI is the real property price index, CPI the consumer price index, LIR the long-term interest rates, XREURUSD the exchange rate between one euro and USD, POP the population in millions, rYpC the real gross disposable income per capita, rGDPpC the real gross domestic product per capita, IPI the industrial production index, UR the unemployment rate in percent, CCI the consumer confidence index, rEXP the real value of exports and rImp the real value of imports._ 

_The lower part of the figure shows the log growth rate of the corresponding measures._ 

69 

_Figure A6 Time series for Germany_ 

Levels 



Log growth rate (D) 



_Figure A6 shows the real measures which were collected for Germany, where rPPI is the real property price index, CPI the consumer price index, LIR the long-term interest rates, XREURUSD the exchange rate between one euro and USD, POP the population in millions, rYpC the real gross disposable income per capita, rGDPpC the real gross domestic product per capita, IPI the industrial production index, UR the unemployment rate in percent, CCI the consumer confidence index, rEXP the real value of exports and rImp the real value of imports._ 

_The lower part of the figure shows the log growth rate of the corresponding measures._ 

70 

_Figure A7 Time series for the Netherlands_ 



<!-- Start of picture text -->
Levels<br><!-- End of picture text -->







<!-- Start of picture text -->
Log growth rate (D)<br><!-- End of picture text -->





_Figure A7 shows the real measures which were collected for the Netherlands, where rPPI is the real property price index, CPI the consumer price index, LIR the long-term interest rates, XREURUSD the exchange rate between one euro and USD, POP the population in millions, rYpC the real gross disposable income per capita, rGDPpC the real gross domestic product per capita, IPI the industrial production index, UR the unemployment rate in percent, CCI the consumer confidence index, rEXP the real value of exports and rImp the real value of imports._ 

_The lower part of the figure shows the log growth rate of the corresponding measures._ 

71 

_Figure A8 Time series for the United Kingdom_ 

#### Levels 



#### Log growth rate (D) 



_Figure A8 shows the real measures which were collected for the UK, where rPPI is the real property price index, CPI the consumer price index, LIR the long-term interest rates, XRGBPUSD the exchange rate between one GBP and USD, XRGBPEUR the exchange rate between one GBP and Euros, POP the population in millions, rYpC the real gross disposable income per capita, rGDPpC the real gross domestic product per capita, IPI the industrial production index, UR the unemployment rate in percent, CCI the consumer confidence index, rEXP the real value of exports and rImp the real value of imports. The lower part of the figure shows the log growth rate of the corresponding measures._ 

72 

### B. Detailed OLS Results 

#### _B 1.1. OLS – Results – United States_ 

For the US, all time series were available for the whole observation period. Therefore, the models could be implemented with all variables as introduced in chapter _3.2.1. Regression models_ . Table 14 provides the metrics for all of the seven models. Detailed plots of the fitted values versus the actual values of the different models are presented in figure B1. 

_Table 15 Summary Statistics OLS Model US_ 

|**Model**<br>**Metric**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Root mean squared error**<br>**% RMSE**|1.91%|1.84%|1.90%|1.81%|1.90%|1.92%|1.84%|
|**Ratio of RMSEs to**<br>**RMSE of model 1**|1|0.96|0.99|0.95|1.00|1.00|0.96|
|**Correct prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|54%|66%|65%|66%|53%|53%|53%|



_The table above shows the root mean squared error resulting from four-quarter forecasts for the models for the United States. The second line shows the ratio of the RMSEs to the RMSE of model one for better comparison._ 

_The third line of the table shows the percentage of correct prediction signs over the 93 forecasts._ 

73 

_Figure B1 OLS models Fitted vs. Rea values United States_ 



<!-- Start of picture text -->
US Fitted vs. Real values Model 1 Q4 US Fitted vs. Real values Model 2 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 1995 2000 2005 2010 2015<br>US Fitted vs. Real values Model 3 Q4 US Fitted vs. Real values Model 4 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>US Fitted vs. Real values Model 5 Q4 US Fitted vs. Real values Model 6 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>US Fitted vs. Real values Model 7 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04<br>0.02<br>0.00<br>−0.02<br>−0.04<br><!-- End of picture text -->

_The plots above show the fitted (red) vs. the real (blue) values of the property price index resulting from the seven different OLS models for the US housing market._ 

74 

#### _B 1.2. OLS – Results – Switzerland_ 

The log growth rate of population, disposable Income, as wells as for imports and exports was calculated on a year on year basis because the original time series for Switzerland were only available annually. 

The summarizing metrics for the seven models are shown in the table 15. 

The fitted versus actual values plots are presented in figure B2. 

_Table 16 Summary Statistics OLS Model Switzerland_ 

|**Model**<br>**Metric**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Root mean squared error**<br>**% RMSE**|1.63%|1.88%|2.60%|1.70%|1.66%|1.61%|1.60%|
|**Ratio of MSEs to MSE of**<br>**model 1**|1.00|1.16|1.60|1.04|1.02|0.99|0.98|
|**Correct prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|58%|51%|45%|49%|53%|53%|57%|



_The table above shows the root mean squared error resulting from four-quarter forecasts for the models for Switzerland. The second line shows the ratio of the RMSEs to the RMSE of model one for better comparison._ 

_The third line of the table shows the percentage of correct prediction signs over the 93 forecasts._ 

75 

_Figure B2 OLS models Fitted vs. Real values Switzerland_ 



<!-- Start of picture text -->
Switzerland Fitted vs. Real values Model 1 Q4 Switzerland Fitted vs. Real values Model 2 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 1995 2000 2005 2010 2015<br>Switzerland Fitted vs. Real values Model 3 Q4 Switzerland Fitted vs. Real values Model 4 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Switzerland Fitted vs. Real values Model 5 Q4 Switzerland Fitted vs. Real values Model 6 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Switzerland Fitted vs. Real values Model 7 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.03 0.03<br>0.02 0.02<br>0.01 0.01<br>−0.01 −0.01<br>−0.03 −0.03<br>0.03 0.03<br>0.02 0.02<br>0.01 0.01<br>−0.01 −0.01<br>−0.03 −0.03<br>0.03 0.03<br>0.02 0.02<br>0.01 0.01<br>−0.01 −0.01<br>−0.03 −0.03<br>0.03<br>0.02<br>0.01<br>−0.01<br>−0.03<br><!-- End of picture text -->

_The plots above show the fitted (red) vs. the real (blue) values of the property price index resulting from the seven different OLS models for the Swiss housing market_ 

76 

#### _B 1.3. OLS – Results – Belgium_ 

For Belgium, additionally to the exchange rate, the unemployment rate had to be removed from the analysis due to limited data availability. Furthermore, the population, disposable income, GDP, import and export time series were only available annually. Therefore, the corresponding log growth rates were calculated on a year on year basis. Table 16 summarizes the two metrics. 

Detailed plots of the fitted vs. the real values can be found in figure B3. 

_Table 17 Summary Statistics OLS Models Belgium_ 

|**Model**<br>**Metric**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Root mean squared error**<br>**% RMSE**|1.94%|2.04%|2.25%|1.97%|1.95%|1.92%|1.99%|
|**Ratio of RMSEs to**<br>**RMSE of model 1**|1.00|1.05|1.16|1.01|1.00|0.99|1.03|
|**Correct prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|70%|71%|73%|71%|73%|73%|72%|



_The table above shows the root mean squared error resulting from four-quarter forecasts for the models for Belgium. The second line shows the ratio of the RMSEs to the RMSE of model one for better comparison. The third line of the table shows the percentage of correct prediction signs over the 93 forecasts._ 

77 

_Figure B3 OLS models Fitted vs. Real values Belgium_ 



<!-- Start of picture text -->
Belgium Fitted vs. Real values Model 1 Q4 Belgium Fitted vs. Real values Model 2 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 1995 2000 2005 2010 2015<br>Belgium Fitted vs. Real values Model 3 Q4 Belgium Fitted vs. Real values Model 4 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Belgium Fitted vs. Real values Model 5 Q4 Belgium Fitted vs. Real values Model 6 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Belgium Fitted vs. Real values Model 7 Q1<br>Real values<br>Fitted values<br>1995 2000 2005 2010<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04<br>0.02<br>0.00<br>−0.02<br>−0.04<br><!-- End of picture text -->

_The plots above show the fitted (red) vs. the real (blue) values of the property price index resulting from the seven different OLS models for the Belgian housing market._ 

78 

#### _B 1.4. OLS – Results – Canada_ 

For Canada, the exports and imports were removed from the analysis because the original time series was only available after 1988. Furthermore, the log growth rate of the annual population data was calculated on year on year basis. 

The plots of the different models for the Canadian housing market are presented in figure B4. The table below shows the summarizing statistics for the seven different models. 

_Table 18 Summary Statistics OLS Models Canada_ 

|**Model**<br>**Metric**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Root mean squared error**<br>**% RMSE**|2.44%|2.46%|2.42%|2.32%|2.39%|2.26%|2.32%|
|**Ratio of RMSEs to**<br>**RMSE of model 1**|1.00|1.01|0.99|0.95|0.98|0.93|0.95|
|**Correct prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|66%|66%|64%|64%|63%|64%|65%|



_The table above shows the root mean squared error resulting from four-quarter forecasts for the models for Canada. The second line shows the ratio of the RMSEs to the RMSE of model one for better comparison. The third line of the table shows the percentage of correct prediction signs over the 93 forecasts._ 

79 

_Figure B4 OLS models Fitted vs. Real values Canada_ 



<!-- Start of picture text -->
Canada Fitted vs. Real values Model 1 Q4 Canada Fitted vs. Real values Model 2 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 1995 2000 2005 2010 2015<br>Canada Fitted vs. Real values Model 3 Q4 Canada Fitted vs. Real values Model 4 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Canada Fitted vs. Real values Model 5 Q4 Canada Fitted vs. Real values Model 6 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Canada Fitted vs. Real values Model 7 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>−0.06 −0.06<br>0.04<br>0.04<br>0.02<br>0.02<br>0.00<br>0.00<br>−0.02<br>−0.02 −0.04<br>−0.06<br>−0.04<br>0.04<br>0.04<br>0.02<br>0.02<br>0.00<br>0.00<br>−0.02<br>−0.04 −0.02<br>−0.06<br>−0.04<br>0.04<br>0.02<br>0.00<br>−0.02<br>−0.04<br><!-- End of picture text -->

_The plots above show the fitted (red) vs. the real (blue) values of the property price index resulting from the seven different OLS models for the Canadian housing market._ 

80 

#### _B 1.5. OLS – Results – France_ 

The models for France included year on year log growth rates of disposable income, imports and exports because these time series were only available at an annual frequency. Besides the exchange rate, no additional variable needed to be removed from the analysis. 

The plots of the fitted versus the real values are shown in figure B5. 

The two metrics for the seven models are presented in table 18. 

_Table 19 Summary Statistics OLS Models France_ 

|**Model**<br>**Metric**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Root mean squared error**<br>**% RMSE**|1.88%|1.66%|1.52%|1.64%|1.90%|1.89%|1.94%|
|**Ratio of RMSEs to**<br>**RMSE of model 1**|1.00|0.88|0.81|0.87|1.01|1.01|1.03|
|**Correct prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|65%|70%|74%|71%|64%|62%|61%|



_The table above shows the root mean squared error resulting from four-quarter forecasts for the models for France. The second line shows the ratio of the RMSEs to the RMSE of model one for better comparison. The third line of the table shows the percentage of correct prediction signs over the 93 forecasts._ 

81 

_Figure B5 OLS models Fitted vs. Real values France_ 



<!-- Start of picture text -->
France Fitted vs. Real values Model 1 Q4 France Fitted vs. Real values Model 2 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 1995 2000 2005 2010 2015<br>France Fitted vs. Real values Model 3 Q4 France Fitted vs. Real values Model 4 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>France Fitted vs. Real values Model 5 Q4 France Fitted vs. Real values Model 6 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>France Fitted vs. Real values Model 7 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04<br>0.02<br>0.00<br>−0.02<br>−0.04<br><!-- End of picture text -->

_The plots above show the fitted (red) vs. the real (blue) values of the property price index resulting from the seven different OLS models for the French housing market._ 

82 

#### _B 1.6. OLS – Results – Germany_ 

As already discussed briefly in section _3.1.6.,_ the analysis and the data preparation for the German time series need to be conducted with great care. It was decided to do the analysis with a reduced data set, excluding the observations of the years 1989 to 1991. 

Furthermore, the log growth of the population data was calculated on a year on year basis. The plots of the different models are shown in Figure B6. 

Table 19 shows the summarizing metrics for the seven models which were gathered using the reduced German time series. 

_Table 20 Summary Statistics OLS Models Germany_ 

|**Model**<br>**Metric**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Root mean squared error**<br>**% RMSE**|0.85%|0.89%|0.97%|0.86%|0.87%|0.89%|0.94%|
|**Ratio of RMSEs to**<br>**RMSE of model 1**|1.00|1.05|1.14|1.01|1.03|1.05|1.11|
|**Correct prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|61%|64%|61%|68%|55%|55%|59%|



_The table above shows the root mean squared error resulting from four-quarter forecasts for the models for Germany. The second line shows the ratio of the RMSEs to the RMSE of model one for better comparison. The third line of the table shows the percentage of correct prediction signs over the 93 forecasts._ 

83 

_Figure B6 OLS models Fitted vs. Real values Germany_ 



<!-- Start of picture text -->
Germany Fitted vs. Real values Model 1 Q4 Germany Fitted vs. Real values Model 2 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Germany Fitted vs. Real values Model 3 Q4 Germany Fitted vs. Real values Model 4 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Germany Fitted vs. Real values Model 5 Q4 Germany Fitted vs. Real values Model 6 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Germany Fitted vs. Real values Model 7 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.02 0.02<br>0.01 0.01<br>0.00 0.00<br>−0.01 −0.01<br>0.02 0.02<br>0.01 0.01<br>0.00 0.00<br>−0.01 −0.01<br>0.02 0.02<br>0.01 0.01<br>0.00 0.00<br>−0.01 −0.01<br>0.02<br>0.01<br>0.00<br>−0.01<br><!-- End of picture text -->

_The plots above show the fitted (red) vs. the real (blue) values of the property price index resulting from the seven different OLS models for the German housing market._ 

84 

#### _B 1.7. OLS – Results – Netherlands_ 

Additionally to the exchange rate, also the unemployment rate had to be removed from the analysis due to limited data availability. Furthermore, the time series for population, disposable income, GDP, imports and exports were only available at an annual frequency. Therefore, the log returns of these time series were calculated on a year on year basis. Detailed plots of the different models are presented in the B7. 

Summarizing statistics for the seven OLS models are shown in the table below. 

_Table 21 Summary Statistics OLS Models Netherlands_ 

|**Model**<br>**Metric**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Root mean squared error**<br>**% RMSE**|2.35%|2.76%|2.90%|2.63%|2.28%|2.19%|2.14%|
|**Ratio of RMSEs to**<br>**RMSE of model 1**|1|1.17|1.23|1.12|0.97|0.93|0.91|
|**Correct prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|68%|71%|57%|72%|72%|74%|71%|



_The table above shows the root mean squared error resulting from four-quarter forecasts for the models for the Netherlands. The second line shows the ratio of the RMSEs to the RMSE of model one for better comparison._ 

_The third line of the table shows the percentage of correct prediction signs over the 93 forecasts._ 

85 

_Figure B7 OLS models Fitted vs. Real values Netherlands_ 



<!-- Start of picture text -->
Netherlands Fitted vs. Real values Model 1 Q4 Netherlands Fitted vs. Real values Model 2 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 1995 2000 2005 2010 2015<br>Netherlands Fitted vs. Real values Model 3 Q4 Netherlands Fitted vs. Real values Model 4 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Netherlands Fitted vs. Real values Model 5 Q4 Netherlands Fitted vs. Real values Model 6 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>Netherlands Fitted vs. Real values Model 7 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04 0.04<br>0.02 0.02<br>0.00 0.00<br>−0.02 −0.02<br>−0.04 −0.04<br>0.04<br>0.02<br>0.00<br>−0.02<br>−0.04<br><!-- End of picture text -->

_The plots above show the fitted (red) vs. the real (blue) values of the property price index resulting from the seven different OLS models for the Dutch housing market._ 

86 

#### _B 1.8. OLS – Results – United Kingdom_ 

The analysis of for the UK was conducted, despite the exclusion of the Euro exchange rate, with the complete data set. Since the population, import and export time series were only available at an annual frequency, their log growth rate was computed on a year on year basis. Figure B8 shows the plots of the fitted versus the real values. 

Table 21 shows the summary of the two metrics for the UK. 

_Table 22 Summary Statistics OLS Models United Kingdom_ 

|**Model**<br>**Metric**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**Root mean squared error**<br>**% RMSE**|2.49%|2.67%|3.05%|2.59%|2.58%|2.48%|2.45%|
|**Ratio of RMSEs to**<br>**RMSE of model 1**|1|1.07|1.22|1.04|1.03|1.00|0.98|
|**Correct prediction sign**<br>∆𝒑𝒕∗∆𝒑¸𝒕> 𝟎|65%|61%|55%|64%|60%|65%|68%|



_The table above shows the root mean squared error resulting from four-quarter forecasts for the models for the United Kingdom. The second line shows the ratio of the RMSEs to the RMSE of model one for better comparison. The third line of the table shows the percentage of correct prediction signs over the 93 forecasts._ 

87 

_Figure B8 OLS models Fitted vs. Real values United Kingdom_ 



<!-- Start of picture text -->
United Kindgom  Fitted vs. Real values Model 1 Q4 United Kindgom  Fitted vs. Real values Model 2 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 1995 2000 2005 2010 2015<br>United Kindgom  Fitted vs. Real values Model 3 Q4 United Kindgom  Fitted vs. Real values Model 4 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>United Kindgom  Fitted vs. Real values Model 5 Q4 United Kindgom  Fitted vs. Real values Model 6 Q4<br>Real values Real values<br>Fitted values Fitted values<br>1995 2000 2005 2010 2015 1995 2000 2005 2010 2015<br>United Kindgom  Fitted vs. Real values Model 7 Q4<br>Real values<br>Fitted values<br>1995 2000 2005 2010 2015<br>0.06 0.06<br>0.02 0.02<br>−0.02 −0.02<br>−0.06 −0.06<br>0.06 0.06<br>0.02 0.02<br>−0.02 −0.02<br>−0.06 −0.06<br>0.06 0.06<br>0.02 0.02<br>−0.02 −0.02<br>−0.06 −0.06<br>0.06<br>0.02<br>−0.02<br>−0.06<br><!-- End of picture text -->

_The plots above show the fitted (red) vs. the real (blue) values of the property price index resulting from the seven different OLS models for the UK housing market._ 

88 

### C. Diebold-Mariano Test Results 

_Table 23 Diebold-Mariano Test United States H0: Same level of accuracy, HA: Model i is less accurate than model j_ 

|**i**<br>**j**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|
|**1**|0.773|0.5572|0.8643|0.6275|0.493|0.4992|
|**2**<br>0.227||0.3108|0.7455|0.211|0.1162|0.2345|
|**3**<br>0.4428|0.6892||0.7215|0.4786|0.3902|0.3859|
|**4**<br>0.1357|0.2545|0.2785||0.08108|0.02852|0.1667|
|**5**<br>0.3725|0.789|0.5214|0.9189||0.3474|0.4243|
|**6**<br>0.507|0.8838|0.6098|0.9715|0.6526||0.5115|
|**7**<br>0.5007|0.7655|0.6141|0.8333|0.5757|0.4885||



_The table presents the p-values resulting from pair wise Diebold-Mariano tests. The null hypothesis, that model i and j have the same level of accuracy, was tested against the alternative hypothesis, that model i is less accurate than model j. The tests, where H0 was rejected at the_ a _= 0.05 level, are highlighted in green._ 

_Table 24 Diebold-Mariano Test Switzerland H0: Same level of accuracy, HA: Model i is less accurate than model j_ 

|**i**<br>**j**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|
|**1**|0.03368|0.01137|0.206|0.2391|0.6419|0.6858|
|**2**<br>0.9663||0.009897|0.9973|0.9572|0.9784|0.9807|
|**3**<br>0.9886|0.9901||0.9927|0.9883|0.9907|0.9911|
|**4**<br>0.794|0.002721|0.00732||0.7161|0.8551|0.8688|
|**5**<br>0.7609|0.04276|0.01175|0.2839||0.9653|0.9001|
|**6**<br>0.3581|0.02156|0.009261|0.1449|0.0347||0.682|
|**7**<br>0.3142|0.01929|0.008864|0.1312|0.09992|0.318||



_The table presents the p-values resulting from pair wise Diebold-Mariano tests. The null hypothesis, that model i and j have the same level of accuracy, was tested against the alternative hypothesis, that model i is less accurate than model j. The tests, where H0 was rejected at the_ a _= 0.05 level, are highlighted in green._ 

89 

_Table 25 Diebold-Mariano Test Belgium H0: Same level of accuracy, HA: Model i is less accurate than model j_ 

|**Model**<br>**Country**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|
|**1**|0.08881|0.00572|0.3275|0.4359|0.5871|0.3114|
|**2**<br>0.9112||0.0008342|0.9832|0.9782|0.9879|0.7062|
|**3**<br>0.9943|0.9992||0.9989|0.9995|1|0.9988|
|**4**<br>0.6725|0.01676|0.001143||0.6784|0.7986|0.3903|
|**5**<br>0.5642|0.02178|0.0004594|0.3216||0.7295|0.2772|
|**6**<br>0.4129|0.01205|3.869e-5|0.2014|0.2705||0.08079|
|**7**<br>0.6886|0.2937|0.001233|0.6097|0.7228|0.9192||



_The table presents the p-values resulting from pair wise Diebold-Mariano tests. The null hypothesis, that model i and j have the same level of accuracy, was tested against the alternative hypothesis, that model i is less accurate than model j. The tests, where H0 was rejected at the_ a _= 0.05 level, are highlighted in green._ 

_Table 26 Diebold-Mariano Test Canada H0: Same level of accuracy, HA: Model i is less accurate than model j_ 

|**j**|**i**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|---|
|**1**||0.7572|0.5451|0.8782|0.7646|0.9643|0.8706|
|**2**|0.2428||0.2021|0.86|0.3226|0.9251|0.6541|
|**3**|0.4549|0.7979||0.8749|0.6095|0.9216|0.7986|
|**4**|0.1218|0.14|0.1251||0.06286|0.9013|0.4537|
|**5**|0.2354|0.6774|0.3905|0.9371||0.9999|0.8344|
|**6**|0.03572|0.07486|0.0784|0.09872|9.939e-5||0.07662|
|**7**|0.1294|0.3459|0.2014|0.5463|0.1656|0.9234||



_The table presents the p-values resulting from pair wise Diebold-Mariano tests. The null hypothesis, that model i and j have the same level of accuracy, was tested against the alternative hypothesis, that model i is less accurate than model j. The tests, where H0 was rejected at the_ a _= 0.05 level, are highlighted in green._ 

90 

_Table 27 Diebold-Mariano Test France H0: Same level of accuracy, HA: Model i is less accurate than model j_ 

|**i**<br>**j**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|
|**1**|0.9468|0.9968|0.9561|0.243|0.3727|0.3284|
|**2**<br>0.05325||0.9918|0.9881|0.04527|0.04584|0.03954|
|**3**<br>0.003238|0.008201||0.01819|0.002661|0.002266|0.001272|
|**4**<br>0.04388|0.01191|0.9818||0.0372|0.03735|0.03228|
|**5**<br>0.757|0.9547|0.9973|0.9628||0.5488|0.3857|
|**6**<br>0.6273|0.9542|0.9977|0.9626|0.4512||0.3321|
|**7**<br>0.6716|0.9605|0.9987|0.9677|0.6143|0.6679||



_The table presents the p-values resulting from pair wise Diebold-Mariano tests. The null hypothesis, that model i and j have the same level of accuracy, was tested against the alternative hypothesis, that model i is less accurate than model j. The tests, where H0 was rejected at the_ a _= 0.05 level, are highlighted in green._ 

_Table 28 Diebold-Mariano Test Germany H0: Same level of accuracy, HA: Model i is less accurate than model j_ 

|**i**<br>**j**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|
|**1**|0.3056|0.09611|0.465|0.23|0.1589|0.03824|
|**2**<br>0.6944||0.02323|0.9077|0.6065|0.4536|0.1732|
|**3**<br>0.9039|0.9768||0.9986|0.8914|0.8659|0.6171|
|**4**<br>0.535|0.09228|0.001385||0.4362|0.285|0.08842|
|**5**<br>0.77|0.3935|0.1086|0.5638||0.1403|0.02078|
|**6**<br>0.8411|0.5464|0.1341|0.715|0.8597||0.006254|
|**7**<br>0.9618|0.8268|0.3829|0.9116|0.9792|0.9937||



_The table presents the p-values resulting from pair wise Diebold-Mariano tests. The null hypothesis, that model i and j have the same level of accuracy, was tested against the alternative hypothesis, that model i is less accurate than model j. The tests, where H0 was rejected at the_ a _= 0.05 level, are highlighted in green._ 

91 

_Table 29 Diebold-Mariano Test Netherlands H0: Same level of accuracy, HA: Model i is less accurate than model j_ 

|**i**<br>**j**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|
|**1**|0.02924|0.03119|0.08577|0.976|0.9742|0.0599|
|**2**<br>0.9708||0.1307|1|0.9897|0.9926|0.998|
|**3**<br>0.9688|0.8693||0.9828|0.985|0.9913|0.9973|
|**4**<br>0.9142|1.252e-5|0.01723||0.9652|0.978|0.9934|
|**5**<br>0.02396|0.01026|0.01496|0.03484||0.9311|0.9257|
|**6**<br>0.02583|0.007447|0.098744|0.02198|0.0689||0.7879|
|**7**<br>0.04014|0.002007|0.002749|0.006637|0.07431|0.2121||



_The table presents the p-values resulting from pair wise Diebold-Mariano tests. The null hypothesis, that model i and j have the same level of accuracy, was tested against the alternative hypothesis, that model i is less accurate than model j. The tests, where H0 was rejected at the_ a _= 0.05 level, are highlighted in green._ 

_Table 30 Diebold-Mariano Test United Kingdom H0: Same level of accuracy, HA: Model i is less accurate than model j_ 

|**i**<br>**j**<br>**1**|**2**|**3**|**4**|**5**|**6**|**7**|
|---|---|---|---|---|---|---|
|**1**|0.07896|0.002274|0.1534|0.1395|0.5395|0.6358|
|**2**<br>0.921||0.0009345|0.8892|0.8317|0.9274|0.938|
|**3**<br>0.9977|0.9991||0.9997|0.9986|0.9999|1|
|**4**<br>0.8466|0.1108|0.0002608||0.5431|0.8593|0.8775|
|**5**<br>0.8605|0.1683|0.001409|0.4569||0.9292|0.8921|
|**6**<br>0.4505|0.07258|0.001304|0.1407|0.07079||0.7493|
|**7**<br>0.3642|0.06203|4.343e-5|0.1225|0.1079|0.2507||



_The table presents the p-values resulting from pair wise Diebold-Mariano tests. The null hypothesis, that model i and j have the same level of accuracy, was tested against the alternative hypothesis, that model i is less accurate than model j. The tests, where H0 was rejected at the_ a _= 0.05 level, are highlighted in green._ 

92 

