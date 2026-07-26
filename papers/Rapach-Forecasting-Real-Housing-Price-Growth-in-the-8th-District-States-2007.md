---
title: Forecasting Real Housing Price Growth in the Eighth District States
type: paper
source_pdf: raw/papers/Rapach_Forecasting Real Housing Price Growth in the 8th District States_2007.pdf
converted: 2026-07-26
---



# Forecasting Real Housing Price Growth in the Eighth District States 

### **David E. Rapach and Jack K. Strauss** 

The authors consider forecasting real housing price growth for the individual states of the Federal Reserve’s Eighth District. They first analyze the forecasting ability of a large number of potential predictors of state real housing price growth using an autoregressive distributed lag (ARDL) model framework. A number of variables, including the state housing price-to-income ratio, state unemployment rate, and national inflation rate, appear to provide information that is useful for forecasting real housing price growth in many Eighth District states. Given that it is typically difficult to determine a priori the particular variable or small set of variables that are the most relevant for forecasting real housing price growth for a given state and time period, the authors also consider various methods for combining the individual ARDL model forecasts. They find that combination forecasts are quite helpful in generating accurate forecasts of real housing price growth in the individual Eighth District states. (JEL C22, C53, E37) 

Federal Reserve Bank of St. Louis _Regional Economic Development_ , 2007, _3_ (2), pp. 33-42. 

he rollercoaster ride of the housing market continues to receive considerable attention in the popular and financial T press. There is currently speculation of a precipitous drop in housing prices in certain regions of the country after the sharp rise in housing prices (“bubble”?) over the past decade. Policymakers are keenly interested in housing price fluctuations and their potential impact on household consumption spending, as evinced by numerous comments by former Federal Reserve Chairman Alan Greenspan and current Chairman Ben Bernanke. This interest appears warranted: The median household now holds more of its wealth in housing than in stocks and has greater access to cash through refinancing backed by housing wealth (Greenspan and Kennedy, 2005). 

Given the substantial interest in housing price fluctuations, the present paper investigates fore- 

casts of real housing price growth in the individual states of the Federal Reserve’s Eight District (Arkansas, Illinois, Indiana, Kentucky, Missouri, Mississippi, and Tennessee). We focus on forecast horizons of four and eight quarters because these horizons are relevant to forecasting over the business cycle, and most recent discussions of housing price fluctuations focus on possible swings in housing prices over business-cycle horizons.<sup>1</sup> We consider a large number of potential predictors (25) of real housing price growth for each state. This is motivated by a sizable literature that examines the determinants of housing prices using in-sample 

> 1 The literature on forecasting housing prices in the United States at the aggregate or state level is relatively sparse, especially compared with the massive literature on forecasting economic variables such as U.S. gross domestic product (GDP) and inflation. The extant literature on forecasting housing prices in the United States tends to focus on long-run trends (Hendershott and Weicher, 2002). 

David E. Rapach is an associate professor of economics and Jack K. Strauss is the Simon Professor of Economics at Saint Louis University. The authors acknowledge financial support from the Simon Center for Regional Forecasting at Saint Louis University. The authors thank participants at the 2007 Eighth District Business and Economics Research Group (BERG) conference and a referee for very helpful comments. The results reported in this paper were generated using GAUSS 6.0; the GAUSS programs are available at http://pages.slu.edu/faculty/rapachde/Research.htm. 

> ©<sup>2007, The Federal Reserve Bank of St. Louis. Articles may be reprinted, reproduced, published, distributed, displayed, and transmitted in</sup> their entirety if copyright notice, author name(s), and full citation are included. Abstracts, synopses, and other derivative works may be made only with prior written permission of the Federal Reserve Bank of St. Louis. 

VOLUME 3, NUMBER 2 2007 33 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

##### Rapach and Strauss 

tests; see, for example, Cho (1996), Abraham and Hendershott (1996), and Johnes and Hyclak (1999). Potential determinants of housing prices in this literature include income, interest rates, construction costs, and labor market variables such as the unemployment rate and size of the labor force.<sup>2</sup> 

Following Stock and Watson (1999, 2003, and 2004), we generate simulated out-of-sample forecasts of real housing price growth using an autoregressive distributed lag (ARDL) model framework. More specifically, when forecasting real housing price growth for a given Eighth District state, we estimate 25 individual ARDL forecasting models of real housing price growth, where each ARDL model includes one of the potential predictors. This provides a convenient framework for analyzing the forecasting ability of each of the individual potential predictors of real housing price growth. 

The plethora of potential predictors of real housing price growth also leads us to consider combination forecasts. Typically, it is difficult to identify a priori the particular variable (or small set of variables) that is most relevant for forecasting a variable such as real housing price growth, especially because the predictive ability of individual variables can vary markedly over time.<sup>3</sup> Combination forecasts provide a way of incorporating information that may be useful for forecasting in environments with a large number of potential predictors, and they have been shown to work well in a number of recent forecasting applications involving GDP growth, inflation, and employment growth; see, for example, Stock and Watson (1999, 2003, and 2004) and Rapach and Strauss (2005 and 2007). We consider a number of different methods for combining the individual ARDL model forecasts from the extant literature and investigate their ability to help generate reliable forecasts of 

> 2 We focus on real housing price growth at the state level in this paper primarily because it allows us to examine regional differences in housing price fluctuations while still having a fairly large number of potential predictors available at the state level. Although statelevel housing prices are able to capture some important geographic differences in housing price fluctuations, as we mention in the conclusion, we are also planning to investigate forecasts of real housing price growth for individual metropolitan areas in the Eighth District in future research. 

> 3 See Stock and Watson (2003) for evidence of this in the context of forecasting U.S. GDP growth and inflation. 

real housing price growth in the Eighth District states.<sup>4</sup> 

Previewing our results, we find that a number of the individual predictors are able to improve on forecasts of real housing price growth relative to an autoregressive (AR) benchmark model, sometimes substantially. These variables include the housing price-to-income ratio, state unemployment rate, and national inflation rate. However, there is no single variable that is able to improve on the AR model forecasts across all of the Eighth District states at all of the forecast horizons considered, and there are instances where a variable that performs very well for one particular state performs poorly for another. Fortunately, we also find that some of the forecast combining methods perform quite well and almost always provide sizable improvements in forecast accuracy relative to the AR benchmark model. 

The rest of the paper is organized as follows: The next section outlines the econometric methodology, and the third section presents the empirical results. 

## ECONOMETRIC METHODOLOGY 

Let ∆ _yt_ = _yt_ – _yt_ –1, where _yt_ is the log level of real housing prices at time _t_ . Furthermore, let 



so that _yt_<sup>_h_</sup> + _h_<sup>is the (approximate) growth rate of real</sup> housing prices from time _t_ to _t_ + _h_ ; _h_ is the forecast horizon. Let _xi_ , _t_ ( _i_ = 1,…, _n_ ) represent one of _n_ potential predictors of real housing price growth. An individual ARDL model based on the predictor _xi_ , _t_ is given by 



where ε _t_<sup>_h_</sup> + _h_<sup>is an error term. Equation (1) can be</sup> used to construct a set of recursive (expanding estimation window) simulated out-of-sample forecasts of _yt_<sup>_h_</sup> + _h_<sup>using information available at time</sup><sup>_t_,</sup> 

> 4 See Timmermann (2006) for a recent survey of forecast combining methods. 

34 VOLUME 3, NUMBER 2 2007 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

Rapach and Strauss 

and we denote the forecast of _yt_<sup>_h_</sup> + _h_<sup>formed at time</sup><sup>_t_</sup> ˆ<sup>_h_</sup> for a given predictorˆ<sup>_h_</sup> _xi_ , _t_ by _yi_ , _t_ + _h|t_<sup>. More specifically,</sup> _yi_ , _t_ + _h|t_<sup>is calculated by plugging ∆</sup><sup>_y_</sup> _t_ – _j_<sup>�</sup><sup>_j_= 0,…,</sup><sup>_q_</sup> 1<sup>–1�</sup> and _xi_ , _t–j_ � _j_ = 0,…, _q_ 2–1� into (1), with the α, β _j_ , and γ _j_ parameters set equal to their ordinary least squares (OLS) estimates based on data available from the start of the sample through period _t_ and ε _t_<sup>_h_</sup> + _h_<sup>set to its expected value of zero. We select the</sup> lag lengths ( _q_ 1 and _q_ 2) in (1) using the Schwarz information criterion (SIC) and a minimum value of zero for _q_ 1 and one for _q_ 2 (to ensure that the potential predictor _xi_ , _t_ appears in (2)) and a maximum value of four for _q_ 1 and _q_ 2.<sup>5</sup> Dividing the total sample into in-sample and out-of-sample portions of size _R_ and _P_ , respectively, we use this procedure to generate a series of _P_ – � _h_ – 1� recursive simulated out-of-sample forecasts for the ARDL model that includes _xi_ , _t_ , which we denote as 



Note that the lag lengths _q_ 1 and _q_ 2 are selected anew when forming each out-of-sample forecast, so that the lag lengths for the ARDL forecasting model are allowed to vary through time. In our applications in the next section, we consider 25 potential predictors, and so we will have 25 series of _h_ -step-ahead individual ARDL model forecasts of real housing price growth for each of the seven states in the Eighth District. 

We also compute recursive simulated out-ofsample forecasts for an AR model, which is given by (1) with the restriction γ _j_ = 0 � _j_ = 0,…, _q_ 2–1� imposed. The series of out-of-sample forecasts are generated using a procedure analogous to that for the ARDL forecasting model described above.<sup>7</sup> Following much of the forecasting literature, the 

> 5 The SIC and the Akaike information criterion (AIC) are two popular model selection procedures. Note that we obtain similar results when we select the lag lengths in (1) using the AIC. 

> 6 Note that the first forecast uses all data available at time _R_ to form a forecast of _y R_<sup>_h_</sup> + _h_<sup>; this forecast is denoted by</sup><sup>_y_ˆ</sup><sup>_h_</sup> _i_ , _R_ + _h_ | _R_<sup>. The information</sup> set is then updated by one period, and we use all data available at time _R_ + 1 to form a forecast of _y_ �<sup>_h_</sup> R+1�+ _h_<sup>; this second forecast is denoted</sup> by _y_<sup>ˆ</sup><sup>_h_</sup> _i_ ,� _R_ +1�+ _h_ | _R_ +1<sup>. We continue in this manner through the end of the</sup> out-of-sample period, leaving us with _P_ – � _h_ – 1� recursive simulated out-of-sample forecasts, { _y_<sup>ˆ</sup><sup>_h_</sup> _i_ , _t_ + _h_ | _t_<sup>}</sup><sup>_T_</sup> _t_ =<sup>–</sup> _R_<sup>_h_.</sup> 

> 7 We select the lag length ( _q_ 1) for the AR model using the SIC and a minimum (maximum) value of zero (four) for _q_ 1. 

AR model serves as a benchmark forecasting model. 

We consider three types of methods for combining the individual ARDL model forecasts. Some of the combining methods require a holdout period to calculate the weights ({ _wi_ , _t_ } _i_<sup>_n_</sup> = 1<sup>) used to</sup> combine the individual ARDL model forecasts, and we use the first _P_ 0 observations from the outof-sample period as the initial holdout period. This leaves us with a total of _P_ – � _h_ – 1� – _P_ 0 outof-sample forecasts available for evaluation.<sup>8</sup> In our applications in the next section, we evaluate the benchmark AR model, individual ARDL model, and combination forecasts over the 1995:Q1– 2006:Q4 out-of-sample period. Importantly, this period includes the bull housing market that has prevailed in many parts of the country over the past decade. 

The first type of combining method uses simple schemes: mean, median, and trimmed mean. The mean (median) combination forecast is simply the average (median) of the individual ARDL model forecasts, while the trimmed mean combination forecast takes the average of the individual ARDL model forecasts after dropping the highest and lowest individual ARDL model forecasts. Stock and Watson (1999 and 2003) find that simple combinations of individual ARDL model forecasts consistently outperform an AR benchmark model (although by a fairly limited margin) with respect to forecasting U.S. real GDP growth and inflation.<sup>9</sup> 

The second type of combining procedure we employ uses a discount mean square forecast error (DMSFE) criterion over the holdout out-of-sample period to determine the weights used to combine the individual ARDL model forecasts formed at time _t_ ; see Stock and Watson (2004). More specifically, the DMSFE combining method uses the weights 

> 8 Note that we use the first _P_ 0 observations from the out-of-sample period to estimate the combining weights used to generate the first combination forecast available for evaluation. We then use the first _P_ 0 + 1 observations from the out-of-sample period to estimate the combining weights used to generate the second combination forecast available for evaluation. We continue in this manner through the end of the available out-of-sample period, leaving us with a series of _P_ – � _h_ – 1� – _P_ 0 out-of-sample combination forecasts available for evaluation. 

- 9 The simple combining methods obviously do not require a holdout period, as the combining weights are not estimated. 

VOLUME 3, NUMBER 2 2007 35 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

##### Rapach and Strauss 



where 



and the parameter θ is a discount factor. When θ = 1, there is no discounting, whereas θ < 1 means that greater importance is attached to the recent forecasting performance of the individual ARDL models in determining the combining weights. In the next section, we consider θ values of 1.0 and 0.9 in our applications. 

The final type of combining method we use is the “cluster” approach recently developed by Aiolfi and Timmermann (2006) based on their _C_ � _K_ , _PB_ � algorithm. The initial cluster combination forecast is generated by first grouping the individual ARDL model forecasts over the holdout out-of-sample period, 



into _K_ equal-sized clusters based on the MSFE, with the first cluster containing the individual ARDL model forecasts with the lowest MSFE values, the second cluster containing the individual ARDL model forecasts with the next lowest MSFE values, and so on. The initial combination forecast is the average of the individual ARDL model forecasts contained in the first cluster. To form the second combination forecast, the MSFE is computed for the individual ARDL model forecasts, 



and the individual ARDL model forecasts are again grouped into _K_ clusters based on the MSFE. The second combination forecast is again the average of the individual forecasts in the first cluster. We can proceed in this manner through the end of the available out-of-sample period to construct the complete set of combination forecasts. Following Aiolfi and Timmermann (2006), we consider _K_ values of two and three in our applications in the next section. 

## EMPIRICAL RESULTS 

### _Data_ 

Nominal housing price indices for individual U.S. states starting in 1975:Q1 are available from Freddie Mac. The Conventional Mortgage Home Price Index provides a means for measuring the typical price inflation for houses within the United States using matched transactions on the same property over time to account for quality changes. Freddie Mac uses data from both purchase and refinance-appraisal transactions, and its database consists of over 33 million homes. The available sample for the housing price indices ends in 2006:Q4. We convert the nominal housing price index into real terms using the personal consumption expenditure (PCE) deflator from the Bureau of Economic Analysis (BEA). We then compute annualized growth rates as 400 times the differences in the log levels of real housing prices. The annualized real housing price growth rates are plotted in Figure 1. Note that real housing price growth is predominantly positive over much of our 1995:Q1–2006:Q4 out-of-sample forecast evaluation period, indicating that the individual states of the Eighth District typically experienced fairly strong housing markets over the past decade.<sup>10</sup> 

As discussed above, we consider 25 potential predictors of real housing price growth for each state. Six of these are state-level variables: 

- Ratio of housing price to per capita personal income 

- Real per capita personal income 

- Population 

- Employment 

- Labor force 

- Unemployment rate 

Nominal personal income data are from the BEA and are converted into per capita terms using 

> 10 The housing price indices exhibit exaggerated saw-tooth patterns in the first part of the sample for a number of the states. This appears to be an artifact of the development and construction of the housing price indices. To minimize the influence of these patterns when estimating the forecasting models, we smooth the real housing price growth observations up to 1984:Q4 by taking a moving average of the current and three previous real housing price observations. Smoothing of the early observations has been applied to the real housing price growth rate series depicted in Figure 1. 

36 VOLUME 3, NUMBER 2 2007 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

Rapach and Strauss 

### Figure 1 

#### Annualized Real Housing Price Growth, 1976:Q1–2006:Q4 



<!-- Start of picture text -->
20 Arkansas 20 Illinois 20 Indiana<br>10 10 10<br>0 0 0<br>−10 −10 −10<br>−20 −20 −20<br>1980 1985 1990 1995 2000 2005 1980 1985 1990 1995 2000 2005 1980 1985 1990 1995 2000 2005<br>20 Kentucky 20 Missouri 20 Mississippi<br>10 10 10<br>0 0 0<br>−10 −10 −10<br>−20 −20 −20<br>1980 1985 1990 1995 2000 2005 1980 1985 1990 1995 2000 2005 1980 1985 1990 1995 2000 2005<br>20 Tennessee<br>10<br>0<br>−10<br>−20<br>1980 1985 1990 1995 2000 2005<br><!-- End of picture text -->

population data from the U.S. Census Bureau and then into real terms using the PCE deflator. The labor market variables are from the Bureau of Labor Statistics (BLS). The housing price-to-income ratio is a popular “valuation ratio” for housing prices that may help to signal whether housing is overor under-valued. The income and employment variables provide measures of the ability of households to purchase housing and are thus potentially important determinants of housing demand. Significant changes in population can also lead to sizable shifts in housing demand. 

We also consider five regional variables as predictors: 

- Housing starts 

- Building permits 

- Homes for sale 

- Homes sold 

- Housing vacancy rate 

These variables, all from the U.S. Census Bureau, are available for each of the four U.S. Census regions.<sup>11</sup> These housing market variables may provide signals of trends and supply conditions in housing markets that affect housing prices. 

Finally, 14 national variables also serve as predictors: 

- Average weekly hours in manufacturing 

> 11 Reflecting their U.S. Census Bureau classification, we use variables from the South region for Arkansas, Kentucky, Mississippi, and Tennessee and variables from the Midwest region for Illinois, Indiana, and Missouri. Note that these variables are not available at the state level for the entire sample period we consider. 

VOLUME 3, NUMBER 2 2007 37 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

##### Rapach and Strauss 

- Average weekly initial claims for unemployment insurance 

- Manufacturers’ new orders for consumer goods and materials (in chained 1982 dollars) 

- Vendor performance 

- Manufacturers’ new orders of nondefense capital goods (in chained 1982 dollars) 

- S&P 500 stock price index 

- Real M2 money supply (in chained 2000 dollars) 

- Term spread (10-year Treasury bond yield minus the federal funds rate) 

- Consumer confidence index 

- PCE deflator 

- Industrial production 

- Commercial and industrial loans outstanding (in chained 2000 dollars) 

- Consumer installment credit outstanding 

- Real effective mortgage rate 

The first nine national predictors comprise nine of the ten leading economic indicators from the Conference Board<sup>12</sup> : These indicators potentially measure broad economic trends that can affect the demand for housing. Data on industrial production, commercial and industrial loans outstanding, and consumer installment credit outstanding are all from the Conference Board. These variables include credit measures that also may significantly influence housing prices. The nominal effective mortgage rate is from Freddie Mac, and we subtract the inflation rate based on the PCE deflator to approximate a real effective mortgage rate. The mortgage rate is an important component of the “user cost” of housing and thus a potentially important determinant of housing demand. 

All of the predictors are transformed in an effort to render them stationary. This involves taking the first differences of log levels, with the following exceptions: We use levels for the unemployment rate, housing vacancy rate, unemployment claims, vendor performance, term spread, and consumer confidence; we use log levels for 

> 12 The leading indicator we omit is national building permits, as this is included as a regional predictor. 

the housing price-to-income ratio; and we use first differences for average weekly hours. 

### _AR Benchmark and Individual ARDL Model Forecasting Results_ 

Table 1 reports forecasting results for the AR benchmark and individual ARDL forecasting models for each state. The table reports the MSFE for the AR benchmark model and the ratio of the individual ARDL model MSFE to the AR benchmark model MSFE. A ratio below unity thus indicates that the individual ARDL model has a lower MSFE than the AR benchmark. Results are reported for forecast horizons of four ( _h_ = 4) and eight ( _h_ = 8) quarters. 

An important result in Table 1 is that no single predictor has an MSFE ratio that is below unity in all states for both forecast horizons; that is, there is no single predictor that delivers consistently more accurate forecasts than the benchmark AR model across all of the Eighth District states and both forecast horizons. The PCE deflator (inflation rate) produces an MSFE ratio below unity for all seven states at both horizons, with one exception (Indiana at _h_ = 4), and many of the MSFE ratios for the inflation rate are well below unity (for example, 0.26 for Kentucky at _h_ = 8), indicating substantial reductions in forecast accuracy relative to the AR model. The state housing price-to-income ratio— as mentioned above, a popular valuation ratio for housing—also performs quite well for Arkansas, Indiana, Kentucky, Mississippi, and Tennessee, with MSFE ratios all below unity (often substantially so) at both forecast horizons. However, the MSFE ratios for the state housing price-to-income ratio are well above unity for both horizons for Illinois and above unity for Missouri at the eightquarter horizon. Other predictors that perform well for a number of Eighth District states are the state unemployment rate and consumer confidence, but there again are situations where the MSFE ratios for these variables are considerably above unity. 

Looking at the results in Table 1 on a state-bystate basis, the state housing price-to-income ratio and state unemployment rate stand out for Arkansas. These predictors generate reductions in MSFE relative to the AR benchmark model of up to 31 percent and 54 percent at the four- and eight- 

38 VOLUME 3, NUMBER 2 2007 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

Rapach and Strauss 

||**essee**<br>**_h_ = 8**|4.56<br>0.52<br>1.06<br>1.04<br>1.16<br>1.16<br>1.34<br>0.95<br>1.01<br>1.08<br>0.86<br>0.83<br>1.11<br>0.97<br>1.06<br>0.97<br>1.00<br>1.02<br>0.94<br>1.29<br>0.72<br>0.62<br>1.00<br>1.02<br>1.12<br>1.19|**model**|
|---|---|---|---|
||**Tenn**<br>**_h_ = 4**|3.43<br>0.76<br>1.05<br>1.02<br>1.33<br>1.29<br>1.15<br>1.11<br>1.04<br>1.22<br>1.08<br>0.95<br>1.17<br>0.96<br>1.08<br>1.05<br>1.01<br>1.01<br>1.02<br>1.23<br>0.94<br>0.89<br>1.08<br>1.16<br>1.30<br>1.12|**ual ARDL**|
|od|**issippi**<br>**_h_ = 8**|9.44<br>0.35<br>1.01<br>0.75<br>1.18<br>1.01<br>0.89<br>0.94<br>0.95<br>1.01<br>1.02<br>1.10<br>1.08<br>0.96<br>1.05<br>0.91<br>1.00<br>1.04<br>0.90<br>1.01<br>0.56<br>0.43<br>0.98<br>1.01<br>1.22<br>1.13|**the individ**|
|on Peri|**Miss**<br>**_h_ = 4**|9.70<br>0.58<br>1.02<br>1.02<br>1.23<br>1.08<br>0.99<br>0.99<br>1.03<br>1.18<br>1.15<br>1.08<br>1.16<br>0.98<br>1.14<br>1.11<br>1.03<br>1.06<br>0.92<br>1.30<br>0.88<br>0.63<br>1.03<br>1.04<br>1.37<br>1.11|**MSFE for**|
|aluati|**ouri**<br>**_h_ = 8**|4.69<br>1.13<br>1.43<br>0.96<br>1.60<br>1.17<br>2.05<br>1.22<br>1.14<br>1.05<br>1.00<br>0.83<br>1.16<br>1.04<br>1.12<br>1.09<br>1.02<br>1.03<br>0.80<br>1.65<br>0.44<br>0.32<br>1.13<br>0.99<br>1.38<br>1.29|**io of the**|
|ecast Ev|**Miss**<br>**_h_ = 4**|2.93<br>0.92<br>1.14<br>0.90<br>1.38<br>1.17<br>1.21<br>1.24<br>1.12<br>1.05<br>1.00<br>1.11<br>1.08<br>0.97<br>1.03<br>1.03<br>1.01<br>1.03<br>0.77<br>1.16<br>0.67<br>0.53<br>1.07<br>1.02<br>1.33<br>0.97|**ort the rat**|
|ple For|**ucky**<br>**_h_ = 8**|2.25<br>0.38<br>1.01<br>0.70<br>1.47<br>0.98<br>0.69<br>1.01<br>0.99<br>1.17<br>0.65<br>0.62<br>1.20<br>0.91<br>1.29<br>1.07<br>1.01<br>1.03<br>0.89<br>1.96<br>0.54<br>0.26<br>1.08<br>1.02<br>1.12<br>1.05|**r rows rep**|
|of-Sam|**Kent**<br>**_h_ = 4**|1.18<br>0.67<br>0.99<br>0.78<br>1.98<br>1.07<br>0.67<br>1.15<br>1.10<br>1.33<br>1.97<br>0.85<br>1.40<br>0.97<br>1.17<br>1.16<br>1.01<br>1.05<br>0.95<br>2.00<br>0.75<br>0.68<br>1.05<br>1.08<br>1.17<br>1.03|**n the othe**<br>**model.**|
|Q4 Out-|**iana**<br>**_h_ = 8**|1.93<br>0.69<br>1.13<br>0.50<br>1.31<br>1.28<br>0.47<br>1.13<br>1.01<br>1.09<br>1.00<br>1.23<br>1.18<br>0.67<br>1.10<br>0.94<br>1.02<br>1.02<br>1.04<br>1.76<br>1.20<br>0.96<br>0.93<br>1.26<br>0.99<br>1.07|**l. Entries i**<br>**benchmark**|
|–2006:|**Ind**<br>**_h_ = 4**|2.15<br>0.84<br>0.95<br>0.81<br>1.17<br>1.13<br>0.69<br>1.29<br>1.11<br>1.29<br>1.06<br>1.17<br>1.20<br>0.90<br>1.06<br>0.96<br>1.13<br>1.01<br>1.12<br>1.25<br>1.03<br>1.08<br>0.99<br>1.21<br>0.93<br>1.03|**ark mode**<br>**or the AR**|
|95:Q1|**ois**<br>**_h_ = 8**|5.66<br>2.74<br>1.03<br>0.84<br>1.09<br>0.71<br>1.89<br>1.06<br>1.02<br>0.97<br>1.00<br>0.57<br>1.23<br>1.02<br>1.13<br>1.01<br>1.00<br>1.10<br>0.75<br>1.10<br>1.16<br>0.58<br>1.11<br>0.92<br>1.01<br>1.37|**R benchm**<br>**e MSFE f**|
|9|**n**||**A**<br>**h**|
|sults: 1|**Illi**<br>**_h_ = 4**|4.66<br>1.89<br>1.02<br>0.88<br>1.07<br>1.05<br>1.39<br>1.18<br>1.07<br>1.00<br>1.00<br>0.82<br>1.58<br>1.03<br>1.31<br>0.93<br>1.01<br>1.08<br>0.98<br>1.05<br>1.09<br>0.83<br>1.21<br>1.07<br>1.06<br>1.15|**FE for the**<br>**olumn to t**|
|cast Re|**nsas**<br>**_h_ = 8**|5.49<br>0.46<br>1.02<br>1.45<br>1.36<br>1.08<br>0.49<br>0.97<br>0.99<br>1.21<br>1.02<br>1.18<br>1.10<br>1.02<br>1.04<br>0.93<br>1.00<br>1.04<br>0.95<br>0.82<br>0.82<br>0.64<br>1.04<br>0.98<br>1.08<br>1.01|**t the MS**<br>**he first c**|
|l Fore|**Arka**<br>**_h_ = 4**|4.90<br>0.70<br>1.01<br>1.82<br>1.41<br>1.14<br>0.69<br>1.08<br>1.06<br>1.36<br>1.02<br>1.12<br>1.33<br>0.95<br>1.14<br>0.90<br>1.00<br>1.05<br>0.94<br>0.81<br>0.87<br> 0.81<br>1.05<br>1.28<br>1.23<br> 0.95|**w repor**<br>**ated in t**|
|l ARDL Mode||ng<br>ncome ratio<br>ersonal income<br>ation<br>yment<br>orce<br>ployment rate<br>using starts<br>ilding permits<br>mes for sale<br>mes sold<br>cancy rate<br>ekly hours<br>ent claims<br>–consumer<br>ormance<br>–capital goods<br>ex<br> <br>onfidence<br>r (inflation rate) <br>roduction<br>/industry loans<br>redit<br>ng<br>e mortgage rate|**in the AR MSFE ro**<br>**the predictor indic**|
|a||i<br>i<br>p<br>l<br>lo<br>r f<br>m<br>o<br>u<br>o<br>o<br>a<br>e<br>m<br>rs<br>rf<br>rs<br>d<br>ad<br>c<br>o<br>p<br>al<br>c<br>i<br>iv|**es**<br>**s**|
|1<br>u||<br>us<br>o-<br>l<br>pu<br>p<br>o<br>e<br>h<br>b<br>h<br>h<br>v<br>w<br>y<br>e<br>e<br>e<br>n<br>e<br>er<br>at<br>l<br>ci<br>er<br>d<br>ct|**ri**<br>**e**|
|e <br>id|**ctor**|SFE<br>ho<br>e-t<br>rea<br>po<br>em<br>lab<br>un<br>nal<br>nal<br>nal<br>nal<br>nal<br>ge<br>plo<br>ord<br>ds<br>or p<br>ord<br>00 i<br>M2<br>spr<br>um<br>efl<br>tria<br>er<br>um<br>tan<br>ffe|**Ent**<br>**clud**|
|Tabl<br>Indiv|**Predi**|AR M<br>State<br>pric<br>State<br>State<br>State<br>State<br>State<br>Regio<br>Regio<br>Regio<br>Regio<br>Regio<br>Avera<br>Unem<br>New<br>goo<br>Vend<br>New<br>S&P 5<br>Real<br>Term<br>Cons<br>PCE d<br>Indus<br>Comm<br>Cons<br>outs<br>Real e|**NOTE:**<br>**that in**|



VOLUME 3, NUMBER 2 2007 39 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

##### Rapach and Strauss 

||**essee**|**_h_ = 8**|0.92|0.99|0.99|0.95|0.93|0.86|0.79||
|---|---|---|---|---|---|---|---|---|---|---|
||**Tenn**|**_h_ = 4**|0.98|1.00|1.18|0.99|0.99|0.98|1.00||
||**sippi**|**_h_ = 8**|0.88|0.97|0.89|0.84|0.80|0.81|0.74||
||**Missis**|**_h_ = 4**|0.97|1.00|1.01|0.93|0.89|0.92|0.86|**odel.**|
|eriod|**ouri**|**_h_ = 8**|0.95|1.03|1.02|0.88|0.76|0.84|0.70|**nchmark m**|
|P|**ss**|||||||||**be**|
|ation|**Mi**|**_h_ = 4**|0.89|0.97|0.97|0.90|0.86|0.86|0.80|**the AR**|
|Evalu|**cky**|**_h_ = 8**|0.76|0.91|0.84|0.71|0.69|0.61|0.52|**MSFE for**|
|st|**u**|||||||||**e**|
|Foreca|**Kent**|**_h_ = 4**|0.86|0.90|0.98|0.85|0.84|0.81|0.76|**lumn to th**|
|ample|**na**|**_h_ = 8**|0.75|0.89|0.78|0.69|0.68|0.69|0.63|**e first co**|
|S|**ia**|||||||||**th**|
|ut-of-|**Ind**|**_h_ = 4**|0.87|0.93|0.89|0.86|0.88|0.88|0.84|**cated in**|
|6:Q4 O|**ois**|**_h_ = 8**|0.82|0.97|0.94|0.83|0.76|0.81|0.72|**ethod indi**|
|0|**n**|||||||||**m**|
|Q1–20|**Illi**|**_h_ = 4**|0.93|0.97|1.02|0.93|0.91|0.92|0.85|**mbining**|
|s: 1995:|**nsas**|**_h_ = 8**|0.91|0.99|0.98|0.88|0.82|0.85|0.76|**for the co**|
|lt|**a**|||||||||**FE**|
|Resu|**Ark**|**_h_ = 4**|0.96|0.99|1.03|0.92|0.90|0.90|0.87|**f the MS**|
|bination Forecast|**ining**|**od**||an|ed mean|E,θ= 1.0|E,θ= 0.9|_B_�|_B_�|**Entries report the ratio o**|
|m|**mb**|**th**|an|di|mm|SF|SF|2,_P_|3,_P_|**TE:**|
|Co|**Co**|**me**|Me|Me|Tri|DM|DM|_C_�|_C_�|**NO**|



40 VOLUME 3, NUMBER 2 2007 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

##### Rapach and Strauss 

quarter horizons, respectively. For Illinois, the state population, regional vacancy rate, and inflation rate display the best performance, with reductions in MSFE relative to the AR benchmark of up to 18 percent and 43 percent at the reported horizons. The state housing price-to-income ratio, state population, state unemployment rate, and unemployment claims produce large reductions in MSFE for Indiana, with reductions up to 31 percent and 53 percent at the two horizons. For Kentucky, six predictors are able to generate sizable reductions in MSFE relative to the AR benchmark at both horizons: the state housing price-to-income ratio, state population, state unemployment rate, regional vacancy rate, inflation rate, and consumer confidence. The largest reductions in MSFE are 33 percent and 74 percent at the four- and eight-quarter horizons, respectively. Real M2, consumer confidence, and the inflation rate lead to sizable reductions in MSFE relative to the AR benchmark for Missouri, with reductions of up to 47 percent and 68 percent at the two horizons. Three variables stand out for Mississippi: the state housing priceto-income ratio, consumer confidence, and inflation rate. The state housing price-to-income ratio leads to the largest reductions in MSFE (42 percent and 65 percent) at the two reported horizons. For Tennessee, the state housing price-to-income ratio and inflation rate lead to the largest reductions in MSFE relative to the AR benchmark at both of the reported horizons (up to 24 percent and 48 percent). 

### _Combining Method Forecasting Results_ 

Table 2 reports the combination forecast results in the form of the ratio of the combining method MSFE to the AR benchmark MSFE, so that (as in Table 1) a ratio below unity indicates that the combining method forecast is more accurate than the AR benchmark forecast in terms of MSFE. The results in Table 2 show that the simple combining methods often produce reductions in MSFE relative to the AR benchmark of around 10 percent, and this is in line with the findings of Stock and Watson (1999 and 2003) in the context of U.S. GDP growth and inflation forecasts. The DMSFE combining method forecasts appear to perform somewhat better than the simple combining method forecasts in most cases, with the DMSFE combining method 

based on θ = 0.9 leading to reductions in MSFE relative to the AR benchmark of approximately 10 to 15 percent at the four-quarter horizon and approximately 20 to 30 percent at the eight-quarter horizon in most cases. The cluster combining methods exhibit the best overall performance, especially the _C_ �3, _PB_ � method. With one exception (Tennessee at _h_ = 4), the MSFE ratios are all well below unity for the _C_ �3, _PB_ � method, with reductions in MSFE of up to 24 percent and 48 percent relative to the benchmark AR model at horizons of four and eight quarters, respectively (both for Kentucky). The _C_ �3, _PB_ � cluster combining method leads to average reductions in MSFE relative to the AR benchmark model across the seven states of approximately 15 percent and 30 percent at horizons of four and eight quarters, respectively. Given that it will be difficult to identify a priori the particular predictors that are most relevant for a given out-of-sample period, the performance of the combining methods—especially the _C_ �3, _PB_ � method—indicates that they provide a useful way of producing relatively accurate forecasts of real housing price growth in the Eighth District states in the presence of many potentially relevant predictors. 

## CONCLUSION 

We examine the ability of a host of economic variables to forecast real housing price growth for the seven individual states in the Federal Reserve’s Eighth District. A number of variables, such as the state housing price-to-income ratio, state unemployment rate, consumer confidence, and inflation rate, produce forecasts that often substantially outperform a benchmark AR model in terms of MSFE in individual Eighth District states, but no single variable is able to improve on the AR benchmark for all states at all reported horizons. Given that it will be difficult to identify a priori the particular variable or small set of variables that are best suited for forecasting real housing price growth for a given state and time period, we also analyze the performance of forecast combining methods. We find that combining methods generally offer useful means of incorporating and culling information from a large number of potential predictors 

VOLUME 3, NUMBER 2 2007 41 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

##### Rapach and Strauss 

when forecasting real housing price growth in the Eighth District states. 

Finally, we briefly discuss two ways that we are extending the research presented in this paper. First, we are currently applying the approaches employed in the present paper to a greater number of individual U.S. states, including larger U.S. states (in terms of population) that have experienced substantial increases in real housing prices over the past decade—states for which there are serious concerns of a housing price “bubble.” We are also preparing to apply the approach used in the present paper to forecasting real housing price growth for individual metropolitan areas in the Eighth District, as households are often interested in forecasts of housing price growth in their more immediate vicinity. 

## REFERENCES 

- Aiolfi, Marco and Timmermann, Allan. “Persistence in Forecasting Performance and Conditional Combination Strategies.” _Journal of Econometrics_ , November-December 2006, _135_ (1-2), pp. 31-53. 

- Abraham, Jesse M. and Hendershott, Patric H. “Bubbles in Metropolitan Housing Markets.” _Journal of Housing Research_ , 1996, _7_ (2), pp. 191-207. 

- Cho, Man. “House Price Dynamics: A Survey of Theoretical and Empirical Issues.” _Journal of Housing Research_ , 1996, _7_ (2), pp. 145-72. 

- Greenspan, Alan and Kennedy, James. “Estimates of Home Mortgage Originations, Repayments, and Debt on One-to-Four Family Residences.” Finance and Economic Discussion Series Paper 2005-41, Federal Reserve Board, September 2005. 

- Hendershott, Patric H. and Weicher, John C. “Forecasting Housing Markets: Lessons Learned.” _Real Estate Economics_ , Spring 2002, _30_ (1), pp. 1-11. 

- Johnes, Geraint and Hyclak, Thomas. “House Prices and Regional Labor Markets.” _Annals of Regional Science_ , February 1999, _33_ (1), pp. 33-49. 

- Rapach, David E. and Strauss, Jack K. “Forecasting Employment Growth in Missouri with Many Potentially Relevant Predictors: An Analysis of Forecast Combining Methods.” Federal Reserve Bank of St. Louis _Regional Economic Development_ , 2005, _1_ (1), pp. 97-112. 

- Rapach, David E. and Strauss, Jack K. “Forecasting U.S. Employment Growth Using Forecast Combining Methods.” _Journal of Forecasting_ , 2007 (forthcoming). 

- Stock, James H. and Watson, Mark W. “Forecasting Inflation.” _Journal of Monetary Economics_ , October 1999, _44_ (2), pp. 293-335. 

- Stock, James. H. and Watson, Mark W. “Forecasting Output Growth and Inflation: The Role of Asset Prices.” _Journal of Economic Literature_ , September 2003, _41_ (3), pp. 788-829. 

- Stock, James H. and Watson, Mark W. “Combination Forecasts of Output Growth in a Seven-Country Data Set.” _Journal of Forecasting_ , September 2004, _23_ (6), pp. 405-30. 

- Timmermann, Allan. “Forecast Combinations,” in Graham Elliott, Clive W.J. Granger, and Allan Timmermann, eds., _Handbook of Economic Forecasting_ . Amsterdam: Elsevier, 2006, pp. 135-96. 

42 VOLUME 3, NUMBER 2 2007 

FEDERAL RESERVE BANK OF ST. LOUIS _REGIONAL ECONOMIC DEVELOPMENT_ 

