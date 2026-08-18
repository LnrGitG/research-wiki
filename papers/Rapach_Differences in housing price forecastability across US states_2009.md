---
title: Rapach_Differences in housing price forecastability across US states_2009
type: paper
source_pdf: raw/papers/Rapach_Differences in housing price forecastability across US states_2009.pdf
converted: 2026-08-18
---





International Journal of Forecasting 25 (2009) 351–372 



www.elsevier.com/locate/ijforecast 

# Differences in housing price forecastability across US states 

David E. Rapach<sup>∗</sup> , Jack K. Strauss<sup>1</sup> 

_Department of Economics, Saint Louis University, 3674 Lindell Boulevard, St. Louis, MO 63108–3397, United States_ 

### **Abstract** 

Given the marked differences in housing price growth across US regions since the mid-1990s, we investigate forecasts of state-level real housing price growth for 1995–2006. We evaluate forecasts from an autoregressive benchmark model as well as models based on a host of state, regional, and national economic variables. Overall, our results highlight important differences in the forecastability of real housing price growth across US states, especially between interior and coastal states. More specifically, we find that autoregressive models, and especially models that incorporate information from numerous economic variables, often provide relatively accurate housing price forecasts for a number of interior states during the period 1995–2006; all forecasting models, however, tend to perform relatively poorly for a group of primarily coastal states that experienced especially strong housing price growth during this period, pointing to a “disconnect” between housing prices and economic fundamentals for these states. 

⃝c 2009 International Institute of Forecasters. Published by Elsevier B.V. All rights reserved. 

_Keywords:_ Real housing price growth; Autoregressive distributed lag model; Combination forecasts; Mean square forecast error; Coastal/interior US states 

## **1. Introduction** 

Housing price fluctuations are receiving increasing attention in both academic and popular circles, due in large part to their apparent growing impact on consumption spending and financial markets. The median US household now holds more of its wealth in housing than in stocks, and the long 

> ∗ Corresponding author. Tel.: +1 314 977 3601; fax: +1 314 977 1478. 

_E-mail addresses:_ rapachde@slu.edu (D.E. Rapach), strausjk@slu.edu (J.K. Strauss). 

1 Tel.: +1 314 977 3813; fax: +1 314 977 1478. 

bull housing market beginning in the mid-1990s apparently helped to fuel increases in household consumption spending (Greenspan & Kennedy, 2005). Housing price declines have potentially significant implications for financial markets, as witnessed by the sub-prime mortgage market crisis that began in August 2007 in the US and spread to financial markets worldwide. Given the capacity of housing price fluctuations to affect consumption spending and financial market conditions, policymakers naturally play close attention to developments in the housing market, as evinced by numerous comments by former Fed chair Alan Greenspan and current chair Ben 

0169-2070/$ - see front matter ⃝c 2009 International Institute of Forecasters. Published by Elsevier B.V. All rights reserved. doi:10.1016/j.ijforecast.2009.01.009 

352 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Bernanke. Policymakers are chiefly concerned with the business-cycle implications of housing price fluctuations: Significant increases in housing prices can play a role in “over-heating” the economy,<sup>2</sup> while housing price declines could portend a general economic slowdown; see, for example, Leamer (2007). In general, economic agents throughout the economy are likely to be keenly interested in forecasts of real housing price growth, the approximate return to the most important asset held by the household sector. In the present paper, we consider out-of-sample forecasts of quarterly state-level real housing price growth for the 20 most populous US states. Somewhat surprisingly, the extant literature on forecasting housing prices is relatively sparse, and tends to focus on long-run trends in national housing prices (Hendershott & Weicher, 2002).<sup>3</sup> We focus on forecasting real housing prices over more immediate horizons of four and eight quarters, consistent with current concerns over shorter-term (business-cycle frequency) fluctuations in real housing prices. Due to significant differences in housing price growth in different parts of the country, especially during the recent bull market, we concentrate on forecasting at the state level instead of the US as a whole. Indeed, a primary objective of this paper is to compare the forecastability of real housing price growth across individual US states, and we are especially interested in possible differences in housing price forecastability between coastal states like California, which experienced very strong real housing price growth during the boom, and interior states like Missouri, which saw substantially more moderate growth. 

The academic literature based on in-sample analysis considers a host of potential determinants of fluctuations in real housing prices at monthly or quarterly frequencies, including various income measures, interest rates, construction costs, and labor market variables; see, for example, Abraham and 2 Relatedly, strong housing price growth can also help to offset other factors pulling the economy into a recession. For example, strong housing price growth during the 2001 recession most likely helped to stimulate consumption spending and keep the 2001 recession mild by historical standards. 

3 For example, Mankiw and Weil (1989) and Poterba (1991) emphasize the importance of demography and tax policy in longrun US housing price trends. 

Hendershott (1996), Cho (1996), Glaeser, Gyourko, and Sakes (2005), and Johnes and Hyclak (1999). In addition, professional forecasters predict housing prices for individual cities using variables such as employment growth, the unemployment rate, recent appreciations, and various measures of “affordability;” see, for example, Millner (2007). Given that numerous economic variables could plausibly affect state-level real housing price growth, we consider a large number of potential predictors in our analysis, including statelevel, regional, and national variables.<sup>4</sup> In addition to computing simulated out-of-sample forecasts of statelevel real housing price growth using an autoregressive (AR) benchmark model, we generate forecasts using a large number of individual autoregressive distributed lag (ARDL) models, where each ARDL model contains one of the potential predictors. This allows us to examine how a variety of individual state-level, regional, and national predictors perform relative to an AR benchmark model across a number of US states. 

The plethora of potential predictors of real housing price growth also leads us to consider combination forecasts. It is typically difficult to identify a priori the particular economic variable or small set of variables that are the most relevant for forecasting a variable such as real housing price growth, especially since the forecasting ability of individual predictors can vary over time.<sup>5</sup> Combination forecasts provide a way of incorporating information that can be useful for forecasting in environments with a large number of potential predictors, and they can also help to improve forecast reliability in the presence of structural breaks (Clements & Hendry, 2006; Hendry & Clements, 2004; Timmermann, 2006). Recently, combining methods have been shown to work well in forecast applications involving GDP growth, inflation, and employment growth; see, for example, Rapach 

4 Note that the consideration of a large number of potential predictors is warranted by theoretical models of housing price determination, such as the “user cost” model (see, for example, Himmelberg, Mayer, & Sinai, 2005), that include the expected housing price appreciation as a determinant of the housing price. Many economic variables could plausibly affect expectations of housing price appreciation. 

5 Stock and Watson (2003) provide evidence of changes in the predictive ability of individual economic variables over time in the context of forecasting US GDP growth and inflation. 

353 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

and Strauss (2008) and Stock and Watson (1999, 2003, 2004). We consider a variety of different methods from the literature for combining the individual ARDL model forecasts – including simple averaging, discounting (Stock & Watson, 2004), and clusters (Aiolfi & Timmermann, 2006) – and investigate their ability to generate reliable forecasts of real housing price growth for individual US states. 

Using the mean square forecast error (MSFE) metric and considering a 1995:1–2006:4 forecast evaluation period that covers the recent US housing market boom and includes a substantial portion of the 1990s expansion and 2001 recession, we find that it is difficult to identify particular individual economic variables that provide consistent forecast gains across individual US states relative to the AR benchmark model. Nevertheless, combinations of forecasts generated by individual ARDL models based on economic variables are often able to outperform the AR benchmark model for a number of states. Overall, an interesting pattern emerges in our results between groups of states. There is a collection of primarily coastal states with relatively high real housing price growth over the out-of-sample period and relatively high MSFEs for the AR benchmark model, and where combination forecasts typically offer only modest or no gains in forecast accuracy relative to the AR benchmark model. The degree of housing price forecastability thus appears to be relatively weak for these states, and there is evidence of a “disconnect” between real housing prices and a broad set of economic variables over the out-of-sample period. In contrast, there is another group of primarily interior states that typically have relatively low real housing price growth over the out-of-sample period and relatively low MSFEs for the AR benchmark model; combination forecasts typically offer sizable gains relative to the AR benchmark model for these states. The degree of housing price forecastability thus appears to be relatively strong for these interior states, and movements in economic variables are apparently more closely connected to future housing price fluctuations. 

The rest of the paper is organized as follows. Section 2 outlines the different forecasting models considered, including forecast combining methods. Section 3 describes the data and presents the empirical results, and Section 4 concludes. 

## **2. Forecasting models** 

## _2.1. ARDL and AR forecasting models_ 

We use the basic framework of Stock and Watson (1999, 2003) to generate a large number of individual ARDL model forecasts of real housing price growth, where each ARDL model includes one of _N_ potential predictors. Define _∆yt_ = _yt_ − _yt_ −1, where _yt_ is the log-level of the real price of housing in a particular US state at time _t_ . In addition, define _yt_<sup>_h_</sup> + _h_ = _(_ 1 _/ h)_<sup>�</sup><sup>_h_</sup> _j_ =1<sup>_∆yt_+</sup><sup>_j_, so that</sup><sup>_y_</sup> _t_<sup>_h_</sup> + _h_<sup>is the (approximate)</sup> growth rate of real housing prices from time _t_ to _t_ + _h_ , where _h_ is the forecast horizon. Let _xi,t_ denote one of the _N_ potential predictors of state-level real housing price growth ( _i_ = 1 _, . . . , N_ ). 

Each ARDL model takes the form: 



where _ϵt_<sup>_h_</sup> + _h_<sup>isanerrorterm.Weconstructrecursive</sup> simulated out-of-sample forecasts for _yt_<sup>_h_</sup> + _h_<sup>attime</sup><sup>_t_</sup> for a given predictor _xi,t_ (denoted by _y_ ˆ _i_<sup>_h_</sup> _,t_ + _h_ | _t_<sup>)using</sup> Eq. (1). More specifically, _y_ ˆ _i_<sup>_h_</sup> _,t_ + _h_ | _t_<sup>iscomputedby</sup> plugging _∆yt_ − _j ( j_ = 0 _, . . . , q_ 1 − 1 _)_ and _xi,t_ − _j ( j_ = 0 _, . . . , q_ 2 − 1 _)_ into Eq. (1), with the parameters set equal to their OLS estimates based on data available from the start of the sample through period _t_ , and _ϵ_<sup>_h_equaltoitsexpectedvalueofzero.Thelag</sup> _t_ + _h_<sup>set</sup> lengths in Eq. (1) are selected using the SIC, data through period _t_ , a minimum lag length of zero for _q_ 1 and one for _q_ 2 (to ensure that _xi,t_ appears in Eq. (1)), and a maximum lag length of four for _q_ 1 and _q_ 2.<sup>6</sup> Dividing the total sample into in-sample and out-ofsample portions of size _R_ and _P_ , respectively, we use this procedure to generate a series of _P_ − _(h_ − 1 _)_ recursive simulated out-of-sample forecasts for the ARDL model that includes _xi,t (_ { ˆ _yi_<sup>_h_</sup> _,t_ + _h_ | _t_<sup>}</sup> _t_<sup>_T_</sup> =<sup>−</sup> _R_<sup>_h)_.Note</sup> that the lag lengths _q_ 1 and _q_ 2 are selected anew when forming each out-of-sample forecast, so that the lag lengths for the ARDL forecasting model are allowed to vary through time. In our applications in Section 3 below, we consider 29–35 potential 

6 The results reported in Section 3 are qualitatively similar for other maximum lag lengths such as six or eight. 

354 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

predictors (depending on the number of contiguous states) for each of the 20 largest US states. We will thus have 29–35 series of _h_ -step-ahead individual ARDL model forecasts of real housing price growth for each state.<sup>7</sup> 

We also compute recursive simulated out-ofsample forecasts for an AR model, which is given by Eq. (1) with the restriction _γ j_ = 0 _( j_ = 0 _, . . . , q_ 2 − 1 _)_ imposed. The series of out-of-sample forecasts are generated using a procedure analogous to that for the ARDL forecasting model described above.<sup>8</sup> The AR model is a popular benchmark model in much of the time series forecasting literature. 

## _2.2. Combination forecasts_ 

The combination forecasts of _yt_<sup>_h_</sup> + _h_<sup>madeattime</sup> _t_ are all linear combinations of the _N_ individual forecasts based on Eq. (1): 



where { _ωi,t_ } _i_<sup>_N_</sup> =1<sup>aretheexantecombiningweights</sup> formed at time _t_ . Some of the combining methods require a holdout period to estimate the combining weights, and we use the first _P_ 0 observations from the out-of-sample period as the initial holdout period. For each of the combining methods, we compute combination forecasts over the post-holdout out-ofsample period, leaving us with a total of _P_ − _(h_ − 1 _)_ − _P_ 0 combination forecasts available for evaluation. Observe that all of the combination forecasts allow the combining weights to change at each point in time _t_ (with one exception, the mean combination forecast described below). 

The first class of combining methods we consider employs simple averaging schemes: the mean, median, and trimmed mean. The mean combination forecast sets _ωi,t_ = 1 _/N_ for _i_ = 1 _, . . . , N_ in Eq. (2), the median combination forecast is the median of { ˆ _yi_<sup>_h_</sup> _,t_ + _h_ | _t_<sup>}</sup> _i_<sup>_N_</sup> =1<sup>,andthetrimmedmeancombination</sup> 

7 Apart from data revisions, the recursive forecasting procedure mimics the situation of a forecaster in real time. Because some of the potential predictors we consider are subject to revision, we are computing “simulated” recursive out-of-sample forecasts. 

8 We select the lag length ( _q_ 1) for the AR model using the SIC and a minimum (maximum) value of zero (four) for _q_ 1. 

forecast sets _ωi,t_ = 0 for the individual forecasts with the smallest and largest values, and _ωi,t_ = 1 _/(N_ − 2 _)_ for the remaining individual forecasts in Eq. (2). Simple averaging schemes obviously do not require a holdout out-of-sample period. 

For the other class of combining methods we consider, the combining weights are based on the historical forecasting performance of the individual models over the holdout out-of-sample period. The Stock and Watson (2004) discount mean square forecast error (DMSFE) combining method uses the following weights: 



where 



and _θ_ is a discount factor. The DMSFE method thus assigns greater weights to individual ARDL model forecasts that have lower MSFE values (that is, better forecasting performance) over the holdout out-ofsample period. When _θ_ = 1, there is no discounting, and Eq. (3) produces the optimal combination forecast derived by Bates and Granger (1969) for the case where the individual forecasts are uncorrelated. When _θ <_ 1, greater weight is attached to the recent forecast accuracy of the individual models. We consider values of 1.0 and 0.9 for _θ_ in our applications in Section 3. 

Similar to Stock and Watson (2004), Aiolfi and Timmermann (2006) develop conditional combining methods based on recent forecasting performance. We use a version of their _C(K , P B)_ algorithm. The initial combination forecast is computed by grouping the individual forecasts over the initial holdout outof-sample period, { ˆ _yi_<sup>_h_</sup> _,s_ + _h_ | _s_<sup>}</sup> _s_<sup>_R_</sup> =<sup>+</sup> _R_<sup>_P_0−</sup><sup>_h_</sup> _(i_ = 1 _, . . . , N )_ into _K_ equal-sized clusters based on MSFE, with the first cluster containing the individual models with the lowest MSFE values, the second cluster containing the models with the next lowest MSFE values, and so on. The first combination forecast is the average of the individual forecasts of _y(_<sup>_h_</sup> _R_ + _P_ 0 _)_ + _h_<sup>forthemodelsin</sup> the first cluster. In forming the second combination forecast, we compute the MSFE for the individual forecasts, { ˆ _yi_<sup>_h_</sup> _,s_ + _h_ | _s_<sup>}</sup> _s_<sup>_R_</sup> =<sup>+</sup> _R_<sup>_P_</sup> +<sup>0−</sup> 1<sup>_h_+1</sup> _(i_ = 1 _, . . . , N )_ , and 

355 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

again group the individual forecasts into _K_ clusters. The second combination forecast is the average of the individual forecasts of _y(_<sup>_h_</sup> _R_ + _P_ 0+1 _)_ + _h_<sup>for the models</sup> included in the first cluster. We proceed in this manner through to the end of the available out-of-sample period. We consider _K_ = 2 and _K_ = 3 in our applications. 

## **3. Empirical results** 

## _3.1. Data_ 

The US state-level nominal housing price data consist of quarterly observations for 1975:1–2006:4 reported by Freddie Mac. Its Conventional Mortgage Home Price Index (CMHPI) provides a means of measuring the typical price inflation for houses within the US, using matched transactions on the same property over time to account for quality changes. Freddie Mac uses data from both purchase and refinance-appraisal transactions, and its database consists of over 33 million homes. To create a real housing price series, we divide the state-level CMHPI by the personal consumption expenditure (PCE) deflator from the Bureau of Economic Analysis (BEA). We compute annualized growth rates as 400 times the differences in the natural logs of real housing prices. The annualized real housing price growth rates for the 20 largest US states in terms of population (as of the latest census in 2000) are plotted in Fig. 1.<sup>9</sup> 

We consider 29–35 potential predictors of real housing price growth for each state. Many of the variables are transformed in an effort to render them stationary. Where appropriate, the transformation used is indicated in parentheses below. 

The first six predictors are **state-level** economic variables: 

- _Ratio of housing price to per capita personal income_ (housing-income ratio; logs) 

9 The CMHPI series exhibit exaggerated saw-tooth patterns in the first part of the sample for a number of states. This appears to be an artifact of the development and construction of the housing price indices. To minimize the influence of these patterns when estimating the forecasting models, we smooth real housing price growth observations up to 1984:4 by taking a moving average of the current and three previous real housing price growth observations. Smoothing of the early observations has been applied to the real housing price growth series depicted in Fig. 1. 

- _Real per capita personal income_ (real personal income; differences, logs) 

- _Population_ (differences, logs) 

- _Employment_ (differences, logs) 

- _Labor force_ (differences, logs) 

- _Unemployment rate_ . 

Nominal personal income data are from the BEA, and are converted into per capita terms using population data from the US Census Bureau, and then into real terms using the PCE deflator. The labor market variables are from the Bureau of Labor Statistics (BLS). The housing-income ratio is a wellknown valuation ratio for housing prices that could help to signal whether housing is “over-valued” or “under-valued.” As discussed by Holly, Pesaran, and Yamagata (in press), for example, a stable long-run housing-income ratio can be derived in a theoretical framework that treats housing as a durable asset and recognizes a market for housing services. This type of model implies an error-correction specification for the relationship between housing price growth and the housing-income ratio, consistent with Eq. (1).<sup>10</sup> The income and employment variables provide measures of the ability of households to purchase housing, and are thus potentially important determinants of housing demand. Significant changes in population can also lead to sizable shifts in housing demand. 

The next five predictors are **regional** variables from the US Census Bureau, and are available for each of the four US Census regions: 

- _Housing starts_ (differences, logs) 

- _Building permits_ (differences, logs) 

- _Homes for sale_ (differences, logs) 

- _Homes sold_ (differences, logs) 

- _Housing vacancy rate_ . 

For each state, we use the regional variable from the US Census Bureau region to which the state belongs. These housing market variables provide potential 

10 The evidence on the stability of the long-run housing-income ratio (that is, whether the logs of housing price and income are cointegrated) is mixed. For example, Gallin (2006) fails to find evidence of cointegration using a panel of US city-level data and bootstrapped versions of the Maddala and Wu (1999) and Pedroni (1999, 2004) panel cointegration tests, while Holly et al. (in press) find evidence of a stable relationship using US state-level data, the common correlated effects estimator of Pesaran (2006), and the panel unit root test of Pesaran (2007). 

356 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 



Fig. 1. Annualized real housing price growth, 1976:1–2006:4. 

signals of trends in demand and supply conditions in housing markets that affect housing prices. 

We also consider 16 **national** variables as predictors: 

- _Average weekly hours in manufacturing_ (average weekly hours; differences) 

- _Average weekly initial claims for unemployment insurance_ (unemployment claims) 

- _Manufacturers’ new orders for consumer goods and materials in chained 1982 dollars_ (new orders—con. goods; differences, logs) 

- _Vendor performance_ 

357 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

- _Manufacturers’ new orders of nondefense capital goods in chained 1982 dollars_ (new orders— cap. goods; differences, logs) 

- _S&P 500 stock price index_ (S&P 500 index; differences, logs) 

- _Real M2 money supply in chained 2000 dollars_ (real M2; differences, logs) 

- _10-year Treasury bond yield minus the federal funds rate_ (term spread) 

- _Consumer confidence index_ (consumer confidence) 

- _PCE deflator_ (differences, logs) 

- _Industrial production_ (differences, logs) 

- _Commercial and industrial loans outstanding in chained 2000 dollars_ (comm./ind. loans; differences, logs) 

- _Consumer installment credit outstanding_ (con. credit outstanding; differences, logs) 

- _Real effective mortgage rate_ 

- _US real housing price growth, Freddie Mac_ (RHP growth—FM) 

- _US real housing price growth, National Association of Realtors_ (RHP growth—NAR). 

The first nine national predictors comprise nine of the ten leading economic indicators from the Conference Board.<sup>11</sup> These indicators potentially detect broad economic trends that can affect the demand for housing, and thus housing prices. Data on industrial production, commercial and industrial loans outstanding, and consumer installment credit outstanding are from the Conference Board. These credit measures are additional variables that can influence housing prices. The nominal effective mortgage rate is from Freddie Mac, and we subtract the inflation rate based on the PCE deflator to approximate a real effective mortgage rate. The mortgage rate is an important component of the “user cost” of housing, and is thus a potentially important determinant of housing demand. The two US real housing price growth variables capture nationwide housing price trends that could affect state-level housing price trends. The two measures are based on the US housing price indices produced by Freddie Mac and the National Association of Realtors (NAR). As discussed above, the index produced by Freddie Mac 

11 The leading indicator we omit is national building permits, as we already include building permits as a regional predictor. 

is designed to account for quality changes. The NAR index measures the median price of existing homes sold, and thus does not control for quality changes. However, it may be able to detect trends in national housing prices more quickly than the Freddie Mac index.<sup>12</sup> 

Finally, we also use real housing price growth in neighboring (contiguous) states as predictors. Neighboring housing price growth potentially incorporates regional “momentum” in housing price fluctuations that may have predictive content; see, for example, Wood (2003). There are 2–8 neighboring states for each of the 20 states for which we generate forecasts. 

Table 1 reports summary statistics for annualized real housing price growth for each state over the 1976:1–2006:4 full-sample and 1995:1–2006:4 outof-sample periods. Comparing columns (2) and (6) of Table 1, we see that the mean annualized real housing price growth is higher in all states during the 1995:1–2006:4 out-of-sample period, relative to the full-sample period. The mean growth rate across the twenty states over the recent out-of-sample period is 4.6%, approximately double the corresponding figure for the full-sample period. Comparing columns (5) and (9), we also see that the maximum growth rate for the full 1976:1–2006:4 period occurs during the recent 1995:1–2006:4 period for most states. Overall, the statistics in Table 1 show that the 1995:1–2006:4 out-of-sample period is characterized by a general bull market in US housing. It is important to note that a number of primarily coastal states in the Northeast and West experienced especially strong housing price growth during 1995:1–2006:4. Among the states considered in our sample, Arizona, California, Florida, Massachusetts, Maryland, New Jersey, New York, Virginia, and Washington experienced average real housing price growth of 6.4% for 1995:1–2006:4, more than double the 3.1% average for the other eleven states in our sample. Furthermore, the maximum annualized real housing price growth rates over the 1995:1–2006:4 period for a number of these states are approximately 20% or more, while the interior states have maximum values that are typically substantially lower. 

> 12 See McCarthy and Peach (2004) for a discussion of different housing price indices. 

358 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 1 

Descriptive statistics: annualized real housing price growth. 

|(1)|(2)<br>1976:1–20|(3)<br>06:4|(4)|(5)|(6)<br>1995:1–2|(7)<br>006:4|(8)|(9)|
|---|---|---|---|---|---|---|---|---|
|State|Mean|Std. dev.|Minimum|Maximum|Mean|Std. dev.|Minimum|Maximum|
|AZ|2.67|7.19|−12.16|37.72|6.73|7.77|−1.67|37.72|
|CA|5.14|8.03|−11.16|37.31|8.04|7.75|−6.75|37.31|
|FL|2.74|6.50|−15.74|27.02|7.45|6.91|−3.57|27.02|
|GA|1.26|3.48|−8.17|8.17|3.54|1.95|−0.57|8.17|
|IL|2.42|4.41|−13.23|13.21|4.05|2.58|−0.93|13.21|
|IN|0.85|3.20|−8.27|8.36|1.90|1.93|−2.87|5.84|
|MA|3.84|7.59|−15.15|26.83|6.12|4.93|−5.93|18.12|
|MD|3.21|5.86|−7.62|29.06|6.13|6.82|−5.93|29.06|
|MI|1.63|5.13|−24.41|11.81|3.09|3.00|−6.83|8.39|
|MO|1.38|4.05|−15.76|9.37|3.43|1.78|−0.93|9.37|
|NC|1.49|2.96|−5.07|10.80|3.04|2.18|−1.29|10.80|
|NJ|3.59|7.36|−12.48|26.20|6.27|5.73|−4.72|26.20|
|NY|3.54|7.25|−10.94|20.05|6.12|5.25|−4.32|20.05|
|OH|1.05|3.39|−10.44|6.43|2.11|1.95|−3.76|5.81|
|PA|2.30|4.93|−8.93|16.65|4.10|4.07|−6.19|16.65|
|TN|1.26|3.52|−12.14|8.04|3.11|2.29|−1.65|8.04|
|TX|0.75|5.08|−23.57|9.86|2.65|2.30|−2.44|7.69|
|VA|2.77|5.27|−9.47|24.94|5.67|5.55|−3.07|24.94|
|WA|4.05|6.26|−10.58|22.92|5.41|4.57|−1.14|19.43|
|WI|1.86|4.71|−15.64|14.28|3.51|2.90|−1.83|14.28|



## _3.2. AR and ARDL forecasting model results_ 

Tables 2 and 3 report AR and ARDL model forecasting results for the 1995:1–2006:4 out-ofsample period, for forecast horizons of four and eight quarters, respectively. As mentioned in the introduction, we choose forecast horizons of four and eight quarters because of our interest in forecasting real housing price growth over horizons broadly corresponding to the business cycle. The first row in each table, labeled “AR RMSFE,” reports the root mean square forecast error (RMSFE) for the benchmark AR model, while the other rows report the ratio of the MSFE for the individual ARDL model indicated in the first column to the MSFE for the AR benchmark model. A ratio below unity thus indicates that the individual ARDL model outperforms the AR benchmark according to the MSFE metric. 

Focusing on the results for the four-quarter horizon in Table 2, we see that Arizona, California, Florida, Massachusetts, Maryland, New Jersey, New York, Virginia, and Washington have RMSFE values for the AR benchmark model that are all above 3%, and are typically substantially higher than the RMSFE 

values for the remaining states. Note that this is the same group of primarily coastal states that experienced relatively high average real housing price growth over the 1995:1–2006:4 out-of-sample period in Table 1. The AR benchmark model thus appears relatively less useful for forecasting real housing price growth over the 1995:1–2006:4 period in states that experienced relatively high average growth during this period. 

With respect to the individual ARDL models at the four-quarter horizon in Table 2, it is generally difficult to identify particular state-level, regional, or national variables that consistently improve on the forecast accuracy of the AR benchmark model across states. With the exception of commercial and industry loans outstanding, all of the state-level, regional, and national predictors outperform the AR benchmark model for some states, but not for a number of others. Take, for example, the housing-income ratio. It outperforms the AR benchmark model for Georgia, Indiana, Massachusetts, Missouri, North Carolina, Ohio, Tennessee, and Texas, in some cases reducing the MSFE by approximately 25%–35%. The MSFE ratios for the housing-income ratio, however, are at or above unity for all of the remaining states, and 

359 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 2 

AR model RMSFE and individual ARDL model MSFE ratios, _h_ = 4. 

|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|
|---|---|---|---|---|---|---|---|
|Predictor|AZ|CA|FL|GA|IL|IN|MA|
|AR RMSFE|6.52|5.55|5.55|2.34|2.16|1.46|3.62|
|_State-level variables_||||||||
|Housing-income ratio|1.02|1.49|1.14|0.82|1.89|0.84|0.85|
|Real personal income|1.02|1.00|1.01|1.10|1.02|0.95|1.05|
|Population|1.19|1.09|1.12|0.77|0.88|0.81|0.88|
|Employment|1.11|1.13|1.05|1.18|1.07|1.17|1.01|
|Labor force|1.01|1.04|1.04|1.09|1.05|1.13|1.06|
|Unemployment rate|0.99|0.96|1.12|0.90|1.39|0.69|1.22|
|_Regional variables_||||||||
|Housing starts|0.99|1.01|1.02|1.00|1.18|1.29|1.11|
|<br>Building permits|0.99|1.00|1.02|1.00|1.07|1.11|0.98|
|Homes for sale|1.00|1.01|1.01|1.33|1.00|1.06|0.95|
|Homes sold|0.99|0.95|1.04|1.00|1.00|1.01|1.01|
|Housing vacancy rate|1.16|1.02|0.99|1.10|0.82|1.17|1.08|
|_National variables_||||||||
|Average weekly hours|1.02|1.01|1.04|1.00|1.58|1.20|1.15|
|<br>Unemployment claims|0.98|0.95|1.09|0.94|1.03|0.90|1.12|
|New orders—con. goods|1.00|1.01|1.04|0.98|1.31|1.06|1.04|
|Vendor performance|0.90|0.90|1.00|0.96|0.93|0.96|1.01|
|New orders—cap. goods|1.01|1.01|1.00|1.00|1.01|1.13|0.98|
|S&P 500 index|1.01|1.01|1.07|1.08|1.08|1.01|1.05|
|Real M2|1.01|0.99|1.04|0.95|0.98|1.12|0.92|
|Term spread|0.87|0.97|1.06|1.12|1.05|1.25|0.99|
|Consumer confdence|0.98|0.85|1.12|0.86|1.09|1.03|0.83|
|PCE defator|1.02|1.03|1.07|0.83|0.83|1.08|1.02|
|<br>Industrial production|1.00|1.03|1.03|1.03|1.21|0.99|1.00|
|Comm./ind. loans|1.02|1.07|1.06|1.01|1.07|1.21|1.01|
|Con. credit outstanding|1.13|1.04|1.08|1.17|1.06|0.93|0.99|
|Real eff. mort. rate|0.95|1.01|0.98|1.15|1.15|1.03|0.98|
|RHP growth—FM|0.94|1.03|0.99|1.02|0.98|1.08|0.89|
|RHP growth—NAR|0.97|0.78|1.03|1.02|0.95|1.11|0.96|
|_Neighbor real housing price_|_growth_|||||||
||0.98 (CA)|0.96 (AZ)|1.03 (AL)|1.05 (AL)|1.04 (IA)|1.29 (IL)|0.87 (CT)|
||1.02 (NM)|1.09 (NV)|1.03 (GA)|1.00 (FL)|1.01 (IN)|0.90 (KY)|1.02 (NH)|
||0.58 (NV)|0.97 (OR)||0.88 (NC)|0.97 (KY)|1.18 (MI)|1.01 (NY)|
||1.22 (UT)|||1.04 (SC)|0.93 (MO)|0.89 (OH)|0.81 (RI)|
|||||1.08 (TN)|1.05 (WI)||0.96 (VT)|
|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|
|Predictor|MD|MI|MO|NC|NJ|NY|OH|
|AR RMSFE|4.35|1.79|1.71|1.57|4.08|3.62|1.54|
|_State-level variables_||||||||
|Housing-income ratio|1.07|1.39|0.92|0.96|1.30|1.65|0.76|
|Real personal income|0.98|1.29|1.14|1.04|1.01|1.02|1.01|
|Population|1.06|0.61|0.90|0.86|0.87|0.92|0.84|
|Employment|1.09|1.55|1.38|1.28|1.03|1.18|0.97|
|Labor force|1.02|1.43|1.17|1.03|1.10|0.99|1.01|
|||||||(_continued_|_on next page_)|



360 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 2 ( _continued_ ) 

|Unemployment rate|1.03|1.30|1.21|1.14|1.16|1.13|1.20|
|---|---|---|---|---|---|---|---|
|_Regional variables_||||||||
|<br>Housing starts|1.01|1.25|1.24|0.99|0.97|1.00|1.17|
|Building permits|1.02|0.90|1.12|1.01|0.89|1.06|1.07|
|Homes for sale|0.99|1.63|1.05|1.18|1.14|1.54|1.02|
|Homes sold|1.01|1.02|1.00|1.02|1.02|1.12|1.02|
|Housing vacancy rate|0.70|1.29|1.11|1.01|1.11|1.63|1.23|
|_National variables_<br>||||||||
|Average weekly hours|1.05|2.01|1.08|1.19|1.05|1.01|1.26|
|Unemployment claims|1.04|1.68|0.97|0.90|1.01|1.36|0.90|
|New orders—con. goods|0.97|1.24|1.03|1.10|1.01|1.08|1.12|
|Vendor performance|0.85|1.65|1.03|0.95|0.98|1.16|0.98|
|New orders—cap. goods|1.00|1.86|1.01|1.02|1.01|1.00|1.01|
|S&P 500 index|1.03|0.96|1.03|1.01|1.02|1.03|1.05|
|Real M2|0.92|1.02|0.77|1.02|0.93|1.07|1.07|
|Term spread|0.93|2.14|1.16|1.02|0.95|1.01|1.45|
|Consumer confdence|0.86|1.18|0.67|0.94|0.88|0.90|0.87|
|PCE defator|0.88|1.03|0.53|0.94|0.93|0.98|1.05|
|Industrial production|1.00|1.34|1.07|0.99|1.04|0.99|1.00|
|Comm./ind. loans|1.03|1.08|1.02|1.01|1.01|1.04|1.08|
|Con. credit outstanding|0.98|0.96|1.33|1.42|1.10|1.07|0.96|
|Real eff. mort. rate|1.01|1.13|0.97|1.07|1.11|1.62|1.03|
|RHP growth—FM|0.98|2.65|1.05|0.86|1.01|1.16|1.04|
|RHP growth—NAR|0.96|1.39|0.97|1.07|0.94|1.03|1.05|
|_Neighbor real housing price_|_growth_|||||||
||1.12 (DC)|1.74 (IN)|0.92 (AR)|1.03 (GA)|1.03 (DE)|1.14 (CT)|1.03 (IN)|
||1.00 (DE)|1.60 (OH)|0.93 (IA)|1.12 (SC)|0.80 (PA)|1.05 (MA)|1.01 (KY)|
||1.27 (PA)|2.40 (WI)|1.06 (IL)|0.89 (TN)|0.99 (NY)|1.13 (NJ)|1.21 (MI)|
||0.99 (VA)||0.87 (KS)|1.12 (VA)||1.03 (PA)|1.27 (PA)|
||1.00 (WV)||0.92 (KY)|||0.91 (VT)|0.92 (WV)|
||||1.05 (NE)<br>0.83 (OK)<br>1.11 (TN)|||||
|(1)|(2)|(3)|(4)|(5)|(6)|(7)||
|Predictor|PA|TN|TX|VA|WA|WI||
|AR RMSFE|2.79|1.85|2.26|3.75|3.02|2.30||
|_State-level variables_||||||||
|Housing-income ratio|1.28|0.76|0.66|1.00|2.24|1.00||
|Real personal income|1.01|1.05|0.94|1.08|1.06|1.02||
|Population|1.20|1.02|1.57|1.07|0.90|0.99||
|Employment|1.04|1.33|1.30|1.23|1.48|1.05||
|Labor force|1.01|1.29|1.81|1.02|1.08|1.16||
|Unemployment rate|1.37|1.15|0.35|1.10|1.12|1.18||
|_Regional variables_||||||||
|Housing starts|0.96|1.11|1.00|1.01|1.01|0.99||
|Building permits|1.04|1.04|1.00|1.00|1.00|1.01||
|Homes for sale|1.59|1.22|1.09|1.03|1.09|0.95||
|Homes sold|1.00|1.08|1.05|1.01|0.95|1.00||
|Housing vacancy rate|1.21|0.95|3.54|0.79|0.86|0.91||



361 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 2 ( _continued_ ) 

|_National variables_|||||||
|---|---|---|---|---|---|---|
|Average weekly hours|1.02|1.17|0.92|1.02|1.02|1.19|
|Unemployment claims|1.14|0.96|0.91|1.05|0.96|0.90|
|New orders—con. goods|1.03|1.08|0.97|1.01|1.00|1.09|
|Vendor performance|1.02|1.05|0.95|0.96|0.83|1.05|
|New orders—cap. goods|1.02|1.01|1.06|1.00|1.01|1.02|
|S&P 500 index|1.10|1.01|1.56|1.07|1.00|1.12|
|Real M2|1.14|1.02|1.31|1.05|1.01|0.97|
|Term spread|0.96|1.23|1.00|0.85|0.78|1.08|
|Consumer confdence|0.96|0.94|1.80|0.90|1.02|0.78|
|PCE defator|0.87|0.89|1.86|0.92|0.94|0.70|
|Industrial production|1.01|1.08|1.03|1.03|1.00|1.02|
|Comm./ind. loans|1.00|1.16|0.89|1.02|1.01|1.00|
|Con. credit outstanding|1.03|1.30|1.08|1.06|1.18|1.02|
|Real eff. mort. rate|1.28|1.12|1.09|1.05|0.84|1.08|
|RHP growth—FM|0.99|1.27|1.13|0.97|0.89|0.99|
|RHP growth—NAR|1.00|1.08|1.01|1.04|0.94|1.04|
|_Neighbor real housing price_|_growth_<br>||||||
||1.07 (DE)|1.03 (AL)|0.99 (AZ)|1.01 (KY)|0.99 (ID)|0.66 (IA)|
||1.18 (MD)|0.95 (AR)|0.98 (LA)|1.02 (MD)|0.95 (OR)|0.77 (IL)|
||1.02 (NJ)|1.08 (GA)|1.09 (NM)|1.10 (NC)||1.04 (MI)|
||0.89 (NY)|1.06 (KY)|1.04 (OK)|1.01 (TN)||0.92 (MN)|
||1.03 (OH)|1.07 (MO)||1.04 (NC)|||
||1.05 (WV)|0.96 (MS)<br>0.99 (NC)|||||



Notes: The first row in each section reports the root mean square forecast errors from the autoregressive forecasting model. The other rows report the ratios of the mean square forecast errors from the autoregressive distributed lag forecasting model that includes the variable indicated in the first column to the mean square forecast errors from the autoregressive forecasting model. A ratio below unity indicates that the autoregressive distributed lag forecasting model has a lower mean square forecast error than the autoregressive forecasting model. 

the MSFE increases relative to the AR benchmark by up to 124% (for Washington). Some of the labor market variables perform very well for some states; for example, the unemployment rate reduces the MSFE by 31% and 65% for Indiana and Texas, respectively, relative to the AR benchmark. For 15 of the 20 states, however, the unemployment rate has an MSFE ratio above unity. Other labor market variables, such as employment, population, and the labor force, which are popular with private forecasters, also perform inconsistently across states, and typically have MSFE ratios above unity. The MSFE ratios for commercial and industry loans outstanding are actually all at or above unity, so that this predictor does not outperform the AR benchmark for any state. There are some situations in which real housing price growth rates in neighboring states improve upon the AR benchmark, but there are also many cases where the MSFE ratios are greater than unity, sometimes by a sizable margin. 

The results in Table 3 for the eight-quarter horizon are similar to those reported in Table 2 for the fourquarter horizon: there are again variables that perform substantially better than the AR benchmark for a few states, but substantially worse for others. For example, the PCE deflator reduces the MSFE by 68% relative to the AR benchmark model for Missouri, but it increases the MSFE by 130% for Texas. From a practical standpoint, the results in Tables 2 and 3 show that it is difficult to identify a priori the particular variable or small set of variables that will prove most useful in forecasting real housing price growth for a particular state. 

## _3.3. Combination forecast results_ 

We next analyze combination forecasts of real housing price growth for individual states, and the results are reported in Tables 4 and 5 for the fourand eight-quarter horizons, respectively. Similarly to 

362 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 3 

AR model RMSFE and individual ARDL model MSFE ratios, _h_ = 8. 

|(1)<br>Predictor|(2)<br>AZ|(3)<br>CA|(4)<br>FL|(5)<br>GA|(6)<br>IL|(7)<br>IN|(8)<br>MA|
|---|---|---|---|---|---|---|---|
|AR RMSFE|6.80|5.99|6.57|2.35|2.38|1.39|3.53|
|_State-level variables_<br>||||||||
|Housing-income ratio|1.04|2.46|1.13|0.91|2.74|0.69|1.31|
|Real personal income|1.06|1.41|1.02|1.14|1.03|1.13|1.13|
|Population|1.08|1.03|0.89|0.85|0.84|0.50|0.93|
|Employment|1.21|1.50|1.08|1.31|1.09|1.31|1.04|
|Labor force|1.02|1.06|1.00|1.17|0.71|1.28|1.06|
|Unemployment rate|1.01|1.04|1.11|1.16|1.89|0.47|2.17|
|_Regional variables_||||||||
|Housing starts|1.00|1.00|1.00|1.01|1.06|1.13|1.04|
|Building permits|0.99|1.00|1.00|1.01|1.02|1.01|0.94|
|Homes for sale|0.96|1.02|0.98|1.04|0.97|1.09|0.92|
|Homes sold|1.00|1.01|1.04|1.01|1.00|1.00|1.00|
|Housing vacancy rate|1.24|0.98|1.01|1.40|0.57|1.23|1.38|
|_National variables_||||||||
|Average weekly hours|1.01|1.00|1.01|1.02|1.23|1.18|1.05|
|Unemployment claims|0.98|0.98|1.02|1.05|1.02|0.67|1.87|
|New orders—con. goods|1.01|1.01|0.99|1.01|1.13|1.10|1.04|
|Vendor performance|0.91|0.89|0.91|0.95|1.01|0.94|1.02|
|New orders—cap. goods|1.01|1.00|1.00|1.00|1.00|1.02|0.99|
|S&P 500 index|1.02|1.01|1.01|1.01|1.10|1.02|1.02|
|Real M2|1.00|0.75|1.02|0.92|0.75|1.04|0.77|
|Term spread|0.86|0.92|1.03|1.13|1.10|1.76|1.13|
|Consumer confdence|0.96|0.76|1.03|0.80|1.16|1.20|0.81|
|PCE defator|1.00|0.78|1.04|0.81|0.58|0.96|1.07|
|Industrial production|1.05|1.09|1.00|1.00|1.11|0.93|1.01|
|Comm./ind. loans|1.02|1.21|1.06|1.01|0.92|1.26|1.02|
|Con. credit outstanding|1.18|1.11|1.03|1.09|1.01|0.99|1.11|
|Real eff. mort. rate|0.91|1.02|0.96|1.20|1.37|1.07|1.05|
|RHP growth—FM|0.93|0.70|0.88|1.00|1.05|1.04|1.09|
|RHP growth—NAR|0.98|0.81|0.98|1.00|1.00|1.01|1.00|
|_Neighbor real housing price_|_growth_|||||||
||0.98 (CA)|1.02 (AZ)|1.03 (AL)|1.12 (AL)|1.03 (IA)|1.55 (IL)|0.87 (CT)|
||1.02 (NM)|1.13 (NV)|1.09 (GA)|1.13 (FL)|1.02 (IN)|0.89 (KY)|1.08 (NH)|
||0.80 (NV)|1.00 (OR)||1.14 (NC)|1.06 (KY)|1.28 (MI)|1.01 (NY)|
||1.48 (UT)|||1.07 (SC)|0.91 (MO)|0.82 (OH)|0.88 (RI)|
|||||1.21 (TN)|0.99 (WI)||1.04 (VT)|
|(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|
|Predictor|MD|MI|MO|NC|NJ|NY|OH|
|AR RMSFE|5.06|1.95|2.16|1.74|4.06|3.82|1.41|
|_State-level variables_||||||||
|Housing-income ratio|1.17|2.17|1.13|0.74|2.02|2.36|0.73|
|<br>Real personal income|1.31|1.31|1.43|1.00|1.03|1.01|1.04|
|Population|1.05|0.76|0.96|0.83|0.79|0.80|0.85|
|Employment|1.18|2.20|1.60|1.30|1.15|1.14|1.06|
|Labor force|1.05|1.70|1.17|0.93|1.20|1.02|1.02|



363 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 3 ( _continued_ ) 

|Unemployment rate|1.11|0.60|2.05|1.29|1.62|1.29|1.29|
|---|---|---|---|---|---|---|---|
|_Regional variables_||||||||
|Housing starts|1.02|1.16|1.22|0.92|1.02|1.02|1.13|
|Building permits|1.00|0.92|1.14|0.95|0.99|1.05|1.11|
|Homes for sale<br>|1.00<br>|2.10<br>|1.05<br>|1.22<br>|1.20<br>|1.35<br>|1.09<br>|
|Homes sold|0.95|1.01|1.00|1.15|1.02|0.99|1.00|
|Housing vacancy rate|0.60|1.58|0.83|1.00|1.39|1.93|1.92|
|_National variables_||||||||
|Average weekly hours|0.97|1.53|1.16|1.20|1.05|1.01|1.14|
|Unemployment claims|1.09|1.12|1.04|0.84|1.13|1.24|0.83|
|New orders—con. goods|0.98|1.11|1.12|1.16|1.05|0.99|1.11|
|Vendor performance|0.92|1.61|1.09|0.87|0.97|1.02|0.99|
|New orders—cap. goods|1.00|1.41|1.02|1.00|0.99|0.98|1.01|
|S&P 500 index|1.01|0.92|1.03|1.01|1.06|1.07|1.01|
|Real M2|0.85|1.34|0.80|1.12|0.76|0.70|1.01|
|Term spread|0.85|2.94|1.65|1.08|0.94|0.98|2.34|
|Consumer confdence|0.85|2.20|0.44|0.66|0.77|0.76|1.39|
|PCE defator|0.83|1.52|0.32|0.66|0.83|0.92|1.17|
|Industrial production|1.02|0.99|1.13|0.94|1.05|1.00|0.98|
|Comm./ind. loans|1.00|1.13|0.99|1.01|0.97|0.98|1.08|
|Con. credit outstanding|1.06|1.02|1.38|1.35|1.32|1.10|1.02|
|Real eff. mort. rate|1.02|1.11|1.29|1.24|1.40|1.85|1.16|
|RHP growth—FM|0.94|2.72|0.91|0.94|1.05|1.60|1.04|
|RHP growth—NAR|1.01|1.17|0.99|0.99|0.98|1.00|1.01|
|_Neighbor real housing pric_|_e growth_|||||||
||1.04 (DC)|1.13 (IN)|0.95 (AR)|1.00 (GA)|1.09 (DE)|0.99 (CT)|1.01 (IN)|
||0.97 (DE)|1.13 (OH)|0.91 (IA)|1.10 (SC)|0.97 (PA)|0.87 (MA)|2.12 (KY)|
||1.27 (PA)|2.04 (WI)|1.02 (IL)|0.81 (TN)|1.03 (NY)|1.01 (NJ)|1.33 (MI)|
||0.91 (VA)||0.83 (KS)|1.34 (VA)||0.94 (PA)|1.38 (PA)|
||1.00 (WV)||1.26 (KY)|||0.87 (VT)|1.00 (WV)|
||||<br>0.99 (NE)<br>0.95 (OK)<br>1.06 (TN)|||||
|(1)|(2)|(3)|(4)|(5)|(6)|(7)||
|Predictor|PA|TN|TX|VA|WA|WI||
|AR RMSFE|3.14|2.14|2.52|4.52|3.66|2.34||
|_State-level variables_||||||||
|Housing-income ratio|1.15|0.52|0.35|1.20|2.79|0.89||
|Real personal income|1.02|1.06|0.67|1.15|0.96|1.03||
|Population|1.15|1.04|1.44|1.07|0.84|1.00||
|Employment|1.02|1.16|1.22|1.27|1.56|1.17||
|Labor force|1.01|1.16|2.50|1.01|1.03|1.02||
|Unemployment rate|1.49|1.34|0.37|1.27|1.16|1.26||
|_Regional variables_||||||||
|Housing starts|0.95|0.95|1.02|1.00|1.00|0.98||
|Building permits|0.99|1.01|1.03|1.00|0.98|1.00||
|Homes for sale|1.69|1.08|1.07|0.99|1.01|0.97||
|Homes sold|1.01|0.86|1.04|0.99|0.95|1.00||
|Housing vacancy rate|1.41|0.83|3.92|0.76|0.68|0.83||
|||||||(_continued_|_on next page_)|



364 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 3 ( _continued_ ) 

|_National variables_|||||||
|---|---|---|---|---|---|---|
|Average weekly hours|1.03|1.11|0.97|1.02|1.03|1.07|
|Unemployment claims|1.10|0.97|0.74|1.06|1.02|0.94|
|New orders—con. goods|1.04|1.06|1.00|1.01|1.03|1.06|
|Vendor performance|1.00|0.97|0.93|0.99|0.74|0.99|
|New orders—cap. goods|0.99|1.00|1.02|0.99|1.08|1.00|
|S&P 500 index|1.15|1.02|1.59|1.02|1.00|1.02|
|Real M2|1.00|0.94|1.54|0.90|0.99|0.87|
|Term spread|0.84|1.29|1.02|0.86|0.64|1.14|
|Consumer confdence|0.92|0.72|2.05|0.92|1.00|0.62|
|PCE defator|0.83|0.62|2.30|0.84|0.84|0.36|
|Industrial production|1.01|1.00|0.93|1.05|1.01|1.03|
|Comm./ind. loans|0.96|1.02|0.86|1.02|1.06|0.97|
|Con. credit outstanding|1.08|1.12|1.02|1.13|1.11|0.99|
|Real eff. mort. rate|1.54|1.19|1.08|1.14|0.88|1.14|
|RHP growth—FM|1.02|1.71|1.16|0.93|0.75|0.98|
|RHP growth—NAR|0.97|1.00|1.02|1.00|0.95|1.05|
|_Neighbor real housing price_|_growth_<br>||||||
||0.85 (DE)|1.04 (AL)|0.99 (AZ)|1.02 (KY)|1.00 (ID)|0.72 (IA)|
||1.29 (MD)|0.98 (AR)|0.78 (LA)|1.02 (MD)|0.94 (OR)|0.93 (IL)|
||0.85 (NJ)|1.04 (GA)|1.11 (NM)|1.09 (NC)||1.06 (MI)|
||0.57 (NY)|0.98 (KY)|0.92 (OK)|1.02 (TN)||2.35 (MN)|
||1.02 (OH)|0.92 (MO)||0.99 (WV)|||
||1.01 (WV)|0.90 (MS)<br>0.98 (NC)|||||



Notes: The first row in each section reports the root mean square forecast errors from the autoregressive forecasting model. The other rows report the ratios of the mean square forecast errors from the autoregressive distributed lag forecasting model that includes the variable indicated in the first column to the mean square forecast errors from the autoregressive forecasting model. A ratio below unity indicates that the autoregressive distributed lag forecasting model has a lower mean square forecast error than the autoregressive forecasting model. 

Tables 2 and 3, Tables 4 and 5 report the ratio of the MSFE for a given combining method to the MSFE for the AR benchmark model. Overall, the results in Tables 4 and 5 indicate that combination forecasts are able to produce fairly consistent improvements in forecast accuracy relative to the AR benchmark model across states. The mean combination forecast has an MSFE ratio below unity for 18 (14) of the individual states at a horizon of four (eight) quarters, and the reductions in MSFE range from approximately 1%–10% (1%–20%). Among the simple averaging combining methods, the mean appears to perform better overall than the median and the trimmed mean (especially the latter). Compared to the mean combination forecasts, the DMSFE and cluster combination forecasts also typically have MSFE ratios below unity, and often offer additional increases in forecast accuracy. For example, the _C(_ 3 _, P B)_ combining method has an MSFE ratio below unity for 

17 (19) of the states at the four-quarter (eight-quarter) horizon, and it leads to reductions in MSFE of up to 22% (31%) relative to the AR benchmark model. Our results provide additional evidence that combination forecasts perform relatively well in the presence of many potential predictors. 

While combination forecasts are typically able to generate more accurate forecasts than the AR benchmark model across individual US states over the out-of-sample period, there are some interesting differences in the magnitudes of forecasting gains across states. The general pattern in Tables 4 and 5 is that states with a relatively high AR RMSFE in column (2) tend to be states where the combination forecasts offer fairly limited or no gains in forecast accuracy relative to the AR model. Take Florida, for instance. All of the combining method MSFE ratios for Florida in Tables 4 and 5 are close to unity, with the trimmed mean providing the smallest 

365 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 4 

AR model RMSFE and combining method MSFE ratios, _h_ = 4. 

|(1)<br>State|(2)<br>AR<br>RMSFE|(3)<br>Mean|(4)<br>Median|(5)<br>Trimmed<br>mean|(6)<br>DMSFE<br>(_θ_ =1)|(7)<br>DMSFE<br>(_θ_ =0_._9)|(8)<br>_C(_2_, P B)_|(9)<br>_C(_3_, P B)_|
|---|---|---|---|---|---|---|---|---|
|AZ|6.52|0.99|1.00|0.90|0.98|0.97|0.94|0.93|
|CA|5.55|0.99|0.99|0.91|0.99|0.98|0.96|0.95|
|FL|5.55|1.04|1.01|0.95|1.04|1.03|1.03|1.03|
|GA|2.34|0.97|0.98|1.02|0.98|0.97|0.97|0.96|
|IL|2.16|0.94|0.98|1.03|0.94|0.92|0.92|0.87|
|IN|1.46|0.89|0.94|0.91|0.88|0.90|0.90|0.87|
|MA|3.62|0.93|0.98|0.92|0.93|0.93|0.94|0.93|
|MD|4.35|0.96|0.98|0.92|0.96|0.96|0.96|0.95|
|MI|1.79|0.89|0.93|0.88|0.90|0.85|0.85|0.76|
|MO|1.71|0.89|0.96|0.96|0.90|0.87|0.85|0.80|
|NC|1.57|0.96|1.00|1.28|0.96|0.96|0.92|0.89|
|NJ|4.08|0.96|1.00|0.95|0.97|0.97|0.96|0.95|
|NY|3.62|1.01|1.03|1.01|1.01|1.00|1.00|0.99|
|OH|1.54|0.94|0.97|0.95|0.93|0.94|0.92|0.92|
|PA|2.79|0.99|1.00|1.03|0.98|0.99|0.99|1.00|
|TN|1.85|0.99|1.00|1.19|0.99|1.00|0.98|1.00|
|TX|2.26|0.97|1.01|1.05|0.96|0.87|0.84|0.78|
|VA|3.75|0.99|1.00|0.94|0.99|0.99|0.99|0.98|
|WA|3.02|0.94|0.96|1.26|0.93|0.92|0.91|0.90|
|WI|2.30|0.91|0.99|0.94|0.89|0.88|0.85|0.79|



Notes: The second column reports the root mean square forecast errors from the autoregressive forecasting model. The other columns report the ratios of the mean square forecast errors from the combining method indicated in the row heading to the mean square forecast errors from the autoregressive forecasting model. A ratio below unity indicates that the combining method has a lower mean square forecast error than the autoregressive forecasting model. 

MSFE ratio of 0.95 at the four-quarter horizon. Other states where the combining methods offer relatively modest gains relative to the AR benchmark model in Tables 4 and 5 include primarily coastal states such as Arizona, California, Massachusetts, Maryland, New Jersey, New York, and Virginia. As discussed above, coastal states tended to experience stronger average real housing price growth over the out-of-sample period. In contrast, there are a number of interior states in Table 4 and/or 5, such as Illinois, Indiana, Michigan, Missouri, Ohio, Texas, and Wisconsin, where the combining methods offer more sizable gains relative to the AR benchmark model. These are states that generally experienced more modest average real housing price growth over the out-of-sample period. 

## _3.4. Cross-section analysis_ 

The results in Sections 3.2 and 3.3 above point to interesting differences in real housing price forecastability across states relating to differences 

in average housing price growth during the period 1995:1–2006:4. In this section, we examine these relationships in more detail. 

Fig. 2 depicts scatterplots relating measures of forecast accuracy at the four-quarter horizon to average real housing price growth over the 1995:1–2006:4 out-of-sample period. The figure also presents fitted regression lines and estimates of the slope coefficient and its corresponding _t_ -statistic for a cross-section regression with forecast accuracy (average real housing price growth for 1995:1–2006:4) serving as the regressand (regressor).<sup>13</sup> The first panel in Fig. 2 relates the RMSFE for the AR benchmark model to real housing price growth. There is clearly a positive correlation between the RMSFE for the AR model and average real housing price growth over the period 1995:1-2006:4, and the positive relationship is significant at the 1% level. Note that states lying 

13 An intercept term is included in the cross-section regressions. 

366 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 5 

AR model RMSFE and combining method MSFE ratios, _h_ = 8. 

|(1)<br>State|(2)<br>AR<br>RMSFE|(3)<br>Mean|(4)<br>Median|(5)<br>Trimmed<br>mean|(6)<br>DMSFE<br>(_θ_ =1)|(7)<br>DMSFE<br>(_θ_ =0_._9)|(8)<br>_C(_2_, P B)_|(9)<br>_C(_3_, P B)_|
|---|---|---|---|---|---|---|---|---|
|AZ|6.80|1.01|1.00|1.09|1.00|1.00|0.99|0.99|
|CA|5.99|0.99|0.98|1.04|1.02|0.96|0.97|0.93|
|FL|6.57|1.01|1.00|1.13|1.01|1.00|1.00|1.00|
|GA|2.35|1.02|1.01|1.07|1.02|1.01|1.00|0.99|
|IL|2.38|0.85|0.98|0.97|0.87|0.81|0.84|0.78|
|IN|1.39|0.79|0.90|0.82|0.73|0.72|0.73|0.69|
|MA|3.53|0.96|0.99|0.96|0.93|0.93|0.94|0.93|
|MD|5.06|0.96|0.97|1.10|0.98|0.97|0.97|0.95|
|MI|1.95|0.79|0.89|0.76|0.77|0.69|0.66|0.63|
|MO|2.16|0.95|0.99|1.01|0.90|0.81|0.84|0.76|
|NC|1.74|0.92|0.97|1.08|0.93|0.92|0.87|0.81|
|NJ|4.06|0.99|1.01|1.08|1.00|1.01|0.99|0.99|
|NY|3.82|1.00|0.99|1.08|0.96|0.96|0.95|0.95|
|OH|1.41|0.89|0.99|0.89|0.81|0.78|0.77|0.70|
|PA|3.14|0.95|1.01|1.06|0.95|0.92|0.95|0.93|
|TN|2.14|0.95|0.99|1.01|0.97|0.94|0.88|0.82|
|TX|2.52|1.03|1.02|1.05|1.02|0.94|0.90|0.88|
|VA|4.52|1.00|1.00|1.13|1.01|1.00|0.99|0.98|
|WA|3.66|0.93|0.96|1.10|0.92|0.91|0.92|0.90|
|WI|2.34|0.86|0.99|0.93|0.79|0.79|0.80|0.69|



Notes: The second column reports the root mean square forecast errors from the autoregressive forecasting model. The other columns report the ratio of the mean square forecast errors from the combining method indicated in the row heading to the mean square forecast errors from the autoregressive forecasting model. A ratio below unity indicates that the combining method has a lower mean square forecast error than the autoregressive forecasting model. 

toward the northeast area of the graph are primarily coastal states, while those lying toward the southwest area are interior states. With the exception of the trimmed mean, similar results hold for the other panels in Fig. 2, which relate the combining method MSFE ratios to average real housing price growth. That is, in states that experienced lower average real housing price growth over the out-of sample period, combination forecasts that incorporate information from a host of economic variables tend to offer greater gains in forecasting accuracy relative to the AR benchmark model. 

Overall, Fig. 2 shows that real housing price growth forecastability generally deteriorates with average real housing price growth during 1995:1–2006:4. As average housing price growth increases, the benchmark AR model provides less accurate forecasts, and including information from multiple economic variables via combination forecasts does relatively little to improve forecast accuracy as average housing price growth increases. Conversely, the forecast 

accuracy of the AR benchmark model improves as average housing price growth decreases, and incorporating information from economic variables using combination forecasts provides further gains in forecast accuracy as average housing price growth decreases. Fig. 3 shows that this pattern is even more pronounced at the eight-quarter horizon. 

To gain further insight into the relationship between real housing price forecastability for the period 1995:1–2006:4 and average housing price growth over this period, Tables 6 and 7 report the mean forecast errors (MFE) for the AR benchmark model and each of the combining methods at horizons of four and eight quarters, respectively. The MFE measures the average bias in the forecasts and indicates whether the forecasts systematically under- or over-predict. Of course, MFE is an important component of MSFE, as the MSFE metric incorporates both the variance of the forecasts and the square of the average bias. The tables show that the MFE is positive in every case (with the exception of the _C(_ 3 _, P B)_ combining method for 

367 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

Table 6 

AR model and combining method MFEs, _h_ = 4. 

|(1)<br>State|(2)<br>AR|(3)<br>Mean|(4)<br>Median|(5)<br>Trimmed<br>mean|(6)<br>DMSFE<br>(_θ_ =1)|(7)<br>DMSFE<br>(_θ_ =0_._9)|(8)<br>_C(_2_, P B)_|(9)<br>_C(_3_, P B)_|
|---|---|---|---|---|---|---|---|---|
|AZ|2.72|2.81|2.73|3.31|2.79|2.78|2.74|2.75|
|CA|1.86|1.87|1.84|2.15|1.87|1.83|1.76|1.73|
|FL|3.39|3.49|3.44|3.94|3.48|3.48|3.47|3.47|
|GA|1.81|0.97|0.98|1.02|0.98|0.97|0.97|0.96|
|IL|1.20|1.14|1.18|1.27|1.12|1.09|1.08|1.01|
|IN|0.37|0.26|0.32|0.29|0.24|0.24|0.23|0.15|
|MA|0.50|0.64|0.54|0.68|0.63|0.61|0.52|0.54|
|MD|1.80|1.70|1.73|2.05|1.69|1.68|1.64|1.60|
|MI|0.28|0.10|0.16|0.10|0.09|0.07|0.05|−0.01|
|MO|1.05|1.00|1.04|1.09|1.01|0.97|0.93|0.88|
|NC|0.89|0.90|0.91|1.00|0.89|0.89|0.87|0.84|
|NJ|1.45|1.48|1.45|1.68|1.47|1.45|1.40|1.41|
|NY|1.85|1.99|1.91|2.16|1.97|1.93|1.87|1.86|
|OH|0.34|0.24|0.30|0.25|0.24|0.24|0.23|0.20|
|PA|1.41|1.36|1.41|1.55|1.35|1.34|1.30|1.26|
|TN|1.11|1.12|1.12|1.20|1.13|1.11|1.07|1.06|
|TX|1.60|1.73|1.69|1.78|1.71|1.62|1.60|1.59|
|VA|1.62|1.60|1.58|1.89|1.61|1.59|1.59|1.56|
|WA|1.42|1.31|1.33|1.54|1.32|1.29|1.32|1.37|
|WI|1.17|1.04|1.14|1.13|1.02|0.99|0.92|0.79|



Note: The entries are the mean forecast errors (average forecast biases) for the forecasting model indicated in the column heading. 

Table 7 

AR model and combining method MFEs, _h_ = 8. 

|(1)<br>State|(2)<br>AR|(3)<br>Mean|(4)<br>Median|(5)<br>Trimmed<br>mean|(6)<br>DMSFE<br>(_θ_ =1)|(7)<br>DMSFE<br>(_θ_ =0_._9)|(8)<br>_C(_2_, P B)_|(9)<br>_C(_3_, P B)_|
|---|---|---|---|---|---|---|---|---|
|AZ|4.64|4.75|4.68|4.86|4.71|4.71|4.69|4.71|
|CA|4.14|4.12|4.09|4.30|4.16|3.97|3.96|3.81|
|FL|5.45|5.52|5.46|5.80|5.51|5.50|5.48|5.49|
|GA|1.90|1.98|1.95|2.03|1.98|1.98|1.96|1.97|
|IL|1.95|1.75|1.92|1.85|1.76|1.70|1.75|1.66|
|IN|0.73|0.53|0.65|0.58|0.45|0.43|0.44|0.30|
|MA|1.37|1.61|1.42|1.66|1.59|1.53|1.47|1.50|
|MD|3.31|3.18|3.24|3.49|3.21|3.22|3.24|3.21|
|MI|0.73|0.47|0.57|0.53|0.33|0.21|0.35|0.22|
|MO|1.94|1.90|1.95|1.96|1.84|1.72|1.76|1.65|
|NC|1.27|1.23|1.26|1.28|1.23|1.22|1.18|1.11|
|NJ|2.66|2.67|2.67|2.79|2.72|2.74|2.75|2.78|
|NY|2.71|2.88|2.72|3.01|2.77|2.77|2.73|2.74|
|OH|0.72|0.57|0.71|0.63|0.49|0.48|0.53|0.44|
|PA|2.10|2.04|2.13|2.15|2.01|1.97|2.02|1.95|
|TN|1.61|1.54|1.59|1.57|1.55|1.52|1.45|1.37|
|TX|2.00|2.16|2.05|2.17|2.13|2.05|2.03|2.05|
|VA|3.22|3.18|3.21|3.43|3.23|3.20|3.25|3.24|
|WA|2.25|2.05|2.15|2.14|2.07|2.03|2.06|2.02|
|WI|1.83|1.68|1.82|1.75|1.59|1.58|1.56|1.39|



Note: The entries are the mean forecast errors (average forecast biases) for the forecasting model indicated in the column heading. 

368 _D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 



Fig. 2. Scatterplots and fitted regression lines relating forecast accuracy measures for the AR benchmark model and combining methods to average real housing price growth, _h_ = 4. 

Michigan at the four-quarter horizon), indicating that the forecasting models systematically under-predict real housing price over the period 1995:1–2006:4. Tables 6 and 7 further show that in states where the MFE for the AR model is relatively high, the combining methods that incorporate information from numerous economic variables often offer no reduction in forecast bias relative to the AR benchmark model. For example, the AR MFE for Arizona is 2.72 at the four-quarter horizon in Table 6, and this is one of the highest MFE values in column (2) of Table 6. For Arizona, none of the combining methods considered in Table 6 is able to reduce the MFE relative to the AR model. A similar situation holds for Arizona at the eight-quarter horizon in Table 7, where the AR MFE is 4.64, and none of the combining methods has a lower MFE. Contrast this to a state such as Indiana, which has a relatively small AR MFE value of 0.37 (0.73) in Table 6 (7). For Indiana, all of the combining methods reduce the MFE relative to the AR model, and the _C(_ 3 _, P B)_ combining method lowers the bias by over 50% at both horizons. This is reminiscent of the pattern in Tables 4 and 5, and suggests that differences 

in forecast biases across states contribute significantly to the differences in MSFE. 

Similarly to Figs. 2 and 3, Figs. 4 and 5 present scatterplots relating the MFE at horizons of four and eight quarters, respectively, to average real housing price growth for 1995:1–2006:4. The figures also show fitted regression lines and estimates of the slope coefficient and its corresponding _t_ -statistic for a cross-section regression, with MFE (average housing price growth) serving as the regressand (regressor).<sup>14</sup> The figures show that there is clearly a significant positive relationship between the bias of the different forecasting models and average housing price growth. This indicates that differences in forecast biases across states relating to average housing price growth are an important reason for the differences in MSFE across states relating to average housing price growth shown in Figs. 2 and 3. 

14 An intercept term is again included in the cross-section regressions. 

369 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 



Fig. 3. Scatterplots and fitted regression lines relating forecast accuracy measures for the AR benchmark model and combining methods to average real housing price growth, _h_ = 8. 

## **4. Conclusion** 

stronger forecastability are typically interior states, such as Indiana and Missouri. 

We investigate differences in real housing price forecastability across US states during the period 1995:1–2006:4, which covers the long bear housing market. Our results reveal important differences in housing price forecastability across states relating to differences in average housing price growth. More specifically, it is generally more difficult to forecast real housing price growth over the period 1995:1–2006:4 for states that experienced relatively high average housing price growth over this period. Forecast biases and MSFE values for AR benchmark models are typically higher in states with relatively high average housing price growth, and models that incorporate information from a host of economic variables offer only limited or no improvements in forecast accuracy relative to the AR benchmark model. States with relatively high housing price growth and weak forecastability are primarily coastal states, such as California and Florida. States with relatively lower real housing price growth for 1995:1–2006:4 and 

Our results _could_ be interpreted as out-of-sample evidence of “bubble”-type behavior in housing prices in a number of primarily coastal US states during the period 1995:1–2006:4, given that forecasting models chronically and substantially underpredict housing price growth in these states during this time. This view is perhaps best supported by the inability of combination forecasts based on a host of economic variables to outperform forecasts generated by an AR benchmark model, indicating that real housing price growth became “disconnected” from economic fundamentals during much of the out-of-sample period. While housing price growth was more modest in many interior states for 1995:1–2006:4, it was still historically high. In these interior states, combination forecasts based on a large set of economic variables are typically more accurate than forecasts generated by an AR benchmark model, so the historically high real housing price growth appears to be supported 

370 _D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 



Fig. 4. Scatterplots and fitted regression lines relating mean forecast errors for the AR benchmark model and combining methods to average real housing price growth, _h_ = 4. 

to a greater extent by the underlying economic fundamentals during the out-of-sample period.<sup>15</sup> 

It is also interesting to note that our out-of-sample results dovetail with the in-sample results recently reported by Holly et al. (in press), who use the Pesaran (2006) common correlated effects estimator to measure the long-run relationship between US statelevel real housing prices and real income. The spatial 

15 Of course, we realize that formally testing for bubbles in asset prices is quite challenging and involves numerous subtle econometric issues; see, for example, G¨urkaynak (2008). We emphasize that our results are thus are only suggestive in this regard. There is a growing body of literature examining the effects of landuse regulations on housing prices; see, for example, Glaeser et al. (2005) and Quigley and Raphael (2005). Differences in land-use regulation across states can help to explain why housing prices are more volatile in certain states due to a more inelastic supply of housing. It is not obvious, however, that differences in land-use regulations can account for the differences we detect across states in the ability of economic variables to improve housing price forecasts. We expect that changes in economic variables that, say, increase demand, will increase housing prices relatively more (less) in states with a relatively low (high) supply elasticity; in either case, however, economic variables should be relevant for predicting housing price 

aspect of their analysis reveals that a group of states, including states such as California, Massachusetts, New Jersey, New York, and Washington, have loadings on a factor capturing common shocks to state-level housing prices that differ markedly from the loadings in other states. This suggests that, after controlling for state-level income, this group of states experienced housing price fluctuations which were substantially different from those in most other states. The group of states identified by Holly et al. (in press) overlaps with many of the coastal states we identify as exhibiting out-of-sample forecastability that differs markedly from most other states. 

Finally, from a practical forecasting standpoint, our results indicate that reasonably accurate forecasting models of housing price growth based on combining methods can be constructed for a number of interior US states. In contrast, the greater potential for a disconnect between housing prices and economic variables makes accurately forecasting real housing price growth in coastal states substantially more 

371 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 



Fig. 5. Scatterplots and fitted regression lines relating mean forecast errors for the AR benchmark model and combining methods to average real housing price growth, _h_ = 8. 

## **Acknowledgements** 

The authors thank session participants at the 2007 International Symposium on Forecasting and 2007 Midwest Econometrics Group Meetings, as well as Mike McCracken and an anonymous referee, for helpful comments. The usual disclaimer applies. All of the results reported in this paper were generated using GAUSS 6.1. Rapach acknowledges support from a Summer Research Grant from the John Cook School of Business at Saint Louis University. 

- Clements, M. P., & Hendry, D. F. (2006). Forecasting with breaks. In G. Elliott, et al., (Eds.), _Handbook of economic forecasting_ (pp. 605–657). Amsterdam: Elsevier. 

- Gallin, J. (2006). The long-run relationship between house prices and income: Evidence from local housing markets. _Real Estate Economics_ , _34_ , 417–438. 

- Glaeser, E. L., Gyourko, J., & Sakes, R. E. (2005). Why is Manhattan so expensive? Regulation and the rise in housing prices. _Journal of Law and Economics_ , _48_ , 331–370. 

- Greenspan, A., & Kennedy, J. (2005). _Estimates of home mortgage originations, repayments, and debt on one-to-four family residences_ . Federal Reserve Board Finance and Economic Discussion Series Paper 2005-41. 

- G¨urkaynak, R. S. (2008). Econometric tests of asset price bubbles: Taking stock. _Journal of Economic Survey_ , _22_ , 166–186. 

## **References** 

- Abraham, J. M., & Hendershott, P. H. (1996). Bubbles in metropolitan housing markets. _Journal of Housing Research_ , _7_ , 191–207. 

- Aiolfi, M., & Timmermann, A. (2006). Persistence in forecasting performance and conditional combination strategies. _Journal of Econometrics_ , _135_ , 31–53. 

- Bates, J. M., & Granger, C. W. J. (1969). The combination of forecasts. _Operational Research Quarterly_ , _20_ , 451–468. 

- Cho, M. (1996). House price dynamics: A survey of theoretical and empirical issues. _Journal of Housing Research_ , _7_ , 145–172. 

- Hendershott, P. H., & Weicher, J. C. (2002). Forecasting housing markets: Lessons learned. _Real Estate Economics_ , _30_ , 1–11. 

- Hendry, D. F., & Clements, M. P. (2004). Pooling of forecasts. _Econometrics Journal_ , _7_ , 1–31. 

- Himmelberg, C., Mayer, C., & Sinai, T. (2005). Assessing high house prices: Bubbles, fundamentals and misperceptions. _Journal of Economic Perspectives_ , _19_ , 67–92. 

- Holly, S., Pesaran, M. H., & Yamagata, T. (2008). A spatio-temporal model of house prices in the US. _Journal of Econometrics_ (in press). 

- Johnes, G., & Hyclak, T. (1999). House prices and regional labor markets. _Annals of Regional Science_ , _33_ , 33–49. 

_D.E. Rapach, J.K. Strauss / International Journal of Forecasting 25 (2009) 351–372_ 

372 

- Leamer, E. E. (2007). _Housing IS the business cycle_ . National Bureau of Economic Research Working Paper No. 13428. 

- Maddala, G. S., & Wu, S. (1999). A comparative study of unit root tests with panel data and a new simple test. _Oxford Bulletin of Economics and Statistics_ , _61_ , 631–652. 

- Mankiw, N. G., & Weil, D. N. (1989). The baby boom, the baby bust, and the housing market. _Regional Science and Urban Economics_ , _19_ , 235–258. 

- McCarthy, J., & Peach, R. W. (2004). Are home prices the next ‘bubble’? _Federal Reserve Bank of New York Economic Policy Review_ , _10_ , 1–17. 

- Millner, M. F. (2007). _Economic real estate trends: Welcome to 2007_ . PMI Mortgage Insurance Co., Winter. 

- Pedroni, P. (1999). Critical values for cointegration tests in heterogeneous panels with multiple regressors. _Oxford Bulletin of Economics and Statistics_ , _61_ , 653–670. 

- Pedroni, P. (2004). Panel cointegration: Asymptotic and finite sample properties of pooled time series tests with an application to the purchasing power parity hypothesis. _Econometric Theory_ , _20_ , 597–625. 

- Pesaran, M. H. (2006). Estimation and inference in large heterogeneous panels with a multifactor error structure. _Econometrica_ , _74_ , 967–1012. 

- Pesaran, M. H. (2007). A simple panel unit root test in the presence of cross section dependence. _Journal of Applied Econometrics_ , _22_ , 265–312. 

- Poterba, J. M. (1991). House price dynamics: The role of taxes and demography. _Brooking Papers on Economic Activity_ , _1991_ , 143–203. 

- Quigley, J. M., & Raphael, S. (2005). Regulation and the high cost of housing in California. _American Economic Review_ , _95_ , 323–328. 

- Rapach, D. E., & Strauss, J. K. (2008). Forecasting US employment growth using forecast combining methods. _Journal of Forecasting_ , _27_ , 75–93. 

- Stock, J. H., & Watson, M. W. (1999). Forecasting inflation. _Journal of Monetary Economics_ , _44_ , 293–335. 

- Stock, J. H., & Watson, M. W. (2003). Forecasting output growth and inflation: The role of asset prices. _Journal of Economic Literature_ , _41_ , 788–829. 

- Stock, J. H., & Watson, M. W. (2004). Combination forecasts of output growth in a seven-country data set. _Journal of Forecasting_ , _23_ , 405–430. 

- Timmermann, A. (2006). Forecast combinations. In G. Elliott, et al., (Eds.), _Handbook of economic forecasting_ (pp. 135–196). Amsterdam: Elsevier. 

- Wood, R. (2003). The information content of regional house prices: Can they be used to improve national house price forecasts? _Bank of England Quarterly Bulletin_ , Autumn, 304–314. 

**David E. Rapach** is an Associate Professor of Economics and Research Economist at the Simon Center for Regional Forecasting at Saint Louis University. His research interests include time series econometrics, macroeconomics, international finance, and financial economics. He has published in numerous journals, including _Econometric Reviews_ , _Economic Inquiry_ , _International Journal of Forecasting_ , _Journal of Applied Econometrics_ , _Journal of Forecasting_ , _Journal of International Economics_ , _Journal of International Money and Finance_ , _Journal of Macroeconomics_ , and _Journal of Money, Credit, and Banking_ . 

**Jack K. Strauss** is a Professor of Economics and the Director of the Simon Center for Regional Forecasting at Saint Louis University. His research interests include time series econometrics, macroeconomics, international finance, and financial economics. He has published numerous articles in journals including _Econometric Reviews_ , _Journal of Applied Econometrics_ , _Journal of Financial Research_ , _Journal of International Money and Finance_ , and _Journal of Macroeconomics_ . 

