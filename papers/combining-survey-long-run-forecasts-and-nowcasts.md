---
title: Ellis W. Tallman
type: paper
source_pdf: raw/papers/combining-survey-long-run-forecasts-and-nowcasts.pdf
converted: 2026-07-26
---

Combining Survey Long-Run Forecasts and Nowcasts with BVAR Forecasts using Relative Entropy<sup>1</sup> 

## Ellis W. Tallman 

Federal Reserve Bank of Cleveland 

## Saeed Zaman 

Federal Reserve Bank of Cleveland University of Strathclyde 

## 2nd Conference on Forecasting at Central Banks 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 1 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

Disclaimer: The views expressed herein are those of the authors and do not necessarily reflect those of the Federal Reserve Bank of Cleveland or of the Federal Reserve System. 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 2 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Introduction 



VARs are popular tools for forecasting; produce accurate forecasts 



Banbura, Giannone, and Reichlin (2010) showed large VARs work ok Resurgence in use of VARs for forecasting and policy analysis 



Fancier VARs: time-varying parameters, regime switching Good forecasting properties but not necessarily better 





Competitive to fixed-parameter VARs est.1985+ sample 

e.g. Aastveit, Carriero, Clark, and Marcellino, 2017 Outperforms simple VARs est. 1960+ for inflation and interest rates; mixed-evidence for real variables 

- e.g. D’Agostino, Gambetti, and Giannone, 2013; Barnett, Mumtaz, and Theodoridis, 2014; Aastveit et al, 2014 



Additional computational demands and complexity 



Constant parameter VARs remain popular for forecasting 

<mark>Tallman and Zaman ()</mark> 

<mark>3 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

<mark>BoE Forecasting 2018</mark> 

# Introduction 



Unrestricted long-run forecasts converge to ergodic mean of sample 





- Problematic as at times ergodic mean overlooks external forces (e.g. inflation target; demographic factors) that informs economists’ view Poses communication challenge for Monetary Policy, e.g. inflation 3-year out 3.5% from a model estimated with 1960+ data 



- Beyond 4 quarters, forecasts increasingly influenced by model’s implied steady-state (Clements and Hendry, 1999; Clark and McCracken, 2008) 





- Inflation forecasts 1 to 3 years out likely biased upwards Why not then estimate using a shorter sample that provides more reasonable trend forecast? One possible route 



- Some may prefer longer-sample when interest in **forecasts of multiple variables** using a **single multivariate model** 



- Recent popular papers on VAR (e.g. Banbura et al, 2010; Koop, 2013; Carriero et al, 2015) all focused on longer sample 

<mark>Tallman and Zaman ()</mark> 

<mark>4 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

<mark>BoE Forecasting 2018</mark> 

# Introduction 



Survey Long-horizon projections reasonable proxy for underlying trends, such as potential growth, natural rate of unemployment, r-star (e.g. Faust and Wright, 2013) 



adjust more rapidly in response to changes in underlying fundamentals such as demographic factors not featured in VARs 



knowledge of inflation target, central bank communications 

<mark>Tallman and Zaman ()</mark> 

<mark>5 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

<mark>BoE Forecasting 2018</mark> 

# In this paper 



Propose a systematic approach to influence forecasts of implied trends from VAR models to values informed from external surveys 



## Utilize the technique of relative entropy 







- To tilt the long-horizon VAR forecast of **select** variables towards the long-horizon survey expectations 

- fixed-parameter VARs (short and long sample) and time-Varying VAR Survey of Professional Forecasters (SPF) as it is publicly available 



Implications on forecast accuracy of **all** VAR variables over forecast horizon of interest to monetary policy makers (i.e. 1 to 12 quarters) 



- Previous research highlights role of nowcasts to improve multi-horizon forecast accuracy (Kruger et al. 2017; Knotek and Zaman, 2017) 



- also tilt VAR one-quarter ahead forecasts to survey nowcasts 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 6 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Preview of results 



Improvements in forecast accuracy of VAR forecasts tilted to survey long-run forecasts **and** nowcasts ( **hybrid forecast** ) 



- All models benefit; gains largest for fixed-parameter VAR est. with longer sample and smallest for time-varying VAR 



Time-Varying VAR: significant gains for inflation but small for others 



## Constant parameter VAR with longer sample 







- Notable improvements for many variables with biggest gains for price inflation, wage inflation, and interest rates 

- Forecast accuracy for inflation competitive to univariate benchmarks And rivals forecast accuracy from time-varying VAR 



These gains are made possible because our proposal mitigate misspecification issues arising from structural breaks 

<mark>Tallman and Zaman ()</mark> 

<mark>7 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

<mark>BoE Forecasting 2018</mark> 

# Related Research 



Incorporating Survey Long-Run Projections into VAR models 



Wright (2013) uses steady-state VAR of Villani (2009) and sets prior values for steady states informed from Blue Chip survey; stationary VAR and MCMC 



- Modeling in Gaps, i.e. deviation from time-varying trends informed from survey (e.g. Clark and McCracken, 2010; Clark, 2011, Zaman, 2013) 



- Requires the history of survey as long as the estimation sample 



Relative Entropy (RE) to Combine Survey information 







Applied to forecasting by Robertson, Tallman and Whiteman (2005) Altavilla, Giacomini and Ragusa (2017) tilt segments of term-structure forecasts to survey expectations 

- Kruger, Clark, and Ravazzolo (2017) tilt one-step ahead forecasts from TVP-VAR toward survey nowcasts 



This paper: uses RE to tilt VAR forecasts toward survey Long-Run projections in addition to survey nowcasts 

<mark>Tallman and Zaman ()</mark> 

<mark>8 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

<mark>BoE Forecasting 2018</mark> 

# Empirical Model and Data 

In our examination, we consider following quarterly VAR models: 



Small VAR consisting of five variables (i.e. _n_ =5 ) 







- Core variables of interest to monetary policy makers: Real GDP growth, CPI Inflation, unemployment rate, federal funds rate 

- Add a financial variable: credit spread (BAA rate - 10yr Treasury rate) Several papers on VAR forecasting employ it as a benchmark VAR 



Medium VAR consisting of ten variables (builds on Small VAR by five additional variables; _n_ =10) 







- Productivity growth, wage inflation, nonfarm payroll employment growth, real consumption growth, core CPI inflation 

- Shown to be useful in improving forecasts of core variables 

- Forecasts of these additional variables maybe of their own interest 



Time-Varying VAR (real GDP growth, CPI inflation, unemployment rate); along the lines of Primiceri (2005) 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 9 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Empirical Model and Data 

The usefulness of Stochastic Volatility 



We also evaluate results of allowing for stochastic volatility (SV) in our Small and Medium VARs 



past research provides strong evidence of the importance of SV (e.g. Clark, 2011; D’Agostino, Giannone, and Gambetti, 2013) 



implements the computationally convenient approach of Carriero, Clark, and Marcellino (2016); a phenomenal contribution 



SV helps significantly improve the calibration of the density forecasts 



But gains in relative accuracy are marginal because density forecasts from hybrid approach are centered around a more accurate mean 



Presentation focus on results from Small VAR without stochastic volatility 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 10 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Empirical Model and Data 



High-dimensional VARs susceptible to overfitting, estimate using Bayesian methods 



Employ conjugate Normal-Inverse Wishart prior 



Prior has computational advantage and competitive forecasting properties (Koop, 2013; Carriero et al, 2015) 



Allows us to conveniently generate multi-step predictive densities 



- Hyper parameters that govern the tightness of Minnesota and Sum of Coefficients prior are set based on optimizing the marginal likelihood over the pre-forecast evaluation sample 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 11 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Empirical Model and Data 

## Forecast details 





Forecasts generated recursively with real-time data and evaluated with real-time data (third release); robust to using revised data Estimation start 1959.Q4; and 1985.Q1 



Real-time vintages as of SPF date 



Forecasts 1 to 40 quarters ahead but focus on 1 to 12 quarters ahead 





Forecast evaluation samples: 1994.Q1 to 2016.Q4 (and 1994 - 2006) MSE for point forecasts and CRPS metric for density forecasts 



- Following Kruger, Clark, and Ravazzolo (2017) statistical significance using Diebold, Mariano and West test using two-sided tests of standard normal 



- HAC variance estimator with lag h-1 truncation parameter; finite sample correction proposed by Harvey et al (1997) 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 12 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Methodology: Relative Entropy 



Start with a predictive density **p(Y)** corresponding to an n-dimensional random variable Y generated by our VAR model 



Modify it to obtain a new predictive density **g(Y)** such that it satisfies a given set of moment conditions (e.g. survey forecasts) 



But in doing so minimizes the relative entropy (i.e. Kullback-Liebler Information Criterion) between the two predictive densities; that is _g_ ( _Y_ ) is as close as possible to the original density _p_ ( _Y_ ) in the information-criterion sense 



Density _g_ ( _Y_ ) is essentially a re-weighted original density _p_ ( _Y_ ) to work there needs to be support in _p_ ( _Y_ ) for the moment conditions 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 13 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Methodology: Relative Entropy 



An effective and flexible conditional forecasting method (KCR, 2017) 





- allows to combine both mean condition and the confidence in it an important advantage if the interest is in density forecasts 



- In a VAR, conditioning or tilting on some future horizon will influence the forecast starting from the jumping-off point all the way to the tilted horizon 





- e.g. tilt real GDP growth at h=6 then tilting it will impact the forecast trajectory from h=1 to h=5 for all the variables 

- simultaneously tilting on multiple variables result in forecast trajectories that cumulative of those conditions 



Easily adapted to any VAR that is able to generate predictive densities 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 14 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Determining the forecast horizon for tilting 





Natural inclination to combine at some very distant future horizon Some macroeconomic variables more persistent than others 





Unemployment rate very persistent while GDP growth on other extreme is in between 



Accounting for this is important when combining the forecasts 



## **Proposed approach: Informed from the BVAR model estimates** 

At each forecast origin _t_ , retrieve the persistence estimates (i.e. slope parameters), corresponding to variable _i_ from equation _i_ of the VAR. 



where _A_<sup>¯</sup> _i_<sup>(</sup> _,_<sup>_i_</sup> _l_<sup>_,i_)</sup> is posterior estimate of the slope coefficient of variable _i_ in equation _i_ of the VAR system. 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 15 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Determining the forecast horizon for tilting 



The corresponding metric that roughly determines the number of quarters it takes to revert back to BVAR’s implied steady state 



The horizon, _hi_<sup>_∗_</sup> _,t_<sup>atwhichthesurveylong-runforecastiscombinedwiththe</sup> BVAR forecast for variable _i_ is set as 











<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 16 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Hybrid Forecast: Components 



<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 17 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

## **Forecast Accuracy Comparison** 

## **Hybrid VAR Forecasts** 

## **versus** 

## **Baseline VAR Forecasts** 

**Baseline forecast** tilts Raw BVAR on survey nowcasts only **Hybrid forecast** tilts Raw BVAR on both survey nowcasts and long-run forecasts 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 18 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Results I: Point Forecast Accuracy 

## **Full Sample (1994.Q1 - 2016.Q4) Small BVAR** (est. 1960+) 

||h=1Q|h=4Q|h=6Q|h=8Q|h=10Q|h=12Q|
|---|---|---|---|---|---|---|
|**Relative MSE: Hybrid **|**/ Base**|**line**|||||
|Real GDP|1.00|1.01|0.77*|0.80*|0.88|0.93|
|CPI Infation|1.00|0.83*|0.78***|0.70**|0.60***|0.62***|
|Unemployment rate|1.00|1.16|1.07|0.98|0.94|0.92|
|Federal funds rate|1.00|0.92|0.90|0.84*|0.75**|0.69***|
|Credit Spread|1.00|0.94|0.90***|0.84***|0.81***|0.79***|



**Baseline forecast** tilts Raw BVAR on survey nowcasts only **Hybrid forecast** tilts Raw BVAR on both survey nowcasts and long-run forecasts 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 19 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Results II: Density Forecast Accuracy 

## **Full Sample (1994.Q1 - 2016.Q4) Small BVAR** (est. 1960+) 

||h=1Q|h=4Q|h=6Q|h=8Q|h=10Q|h=12Q|
|---|---|---|---|---|---|---|
|**Relative CRPS: Hybr**|**id - Bas**|**eline**|||||
|Real GDP|0.00|0.02|-0.17*|-0.11*|-0.08|-0.05|
|CPI Infation|0.00|-0.10*|-0.12***|-0.19**|-0.28***|-0.24***|
|Unemployment rate|0.00|0.02|0.02|-0.01|-0.03|-0.04|
|Federal funds rate|0.00|-0.01|-0.03|-0.07|-0.16**|-0.27***|
|Credit Spread|0.00|-0.01|-0.04***|-0.07***|-0.09***|-0.10***|



**Baseline forecast** tilts Raw BVAR on survey nowcasts only **Hybrid forecast** tilts Raw BVAR on both survey nowcasts and long-run forecasts 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 20 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Results III: Point Forecast Accuracy 

## **Full Sample (1994.Q1 - 2016.Q4) Small BVAR** (est. 1985+) 

||h=1Q|h=4Q|h=6Q|h=8Q|h=10Q|h=12Q|
|---|---|---|---|---|---|---|
|**Relative MSE: Hybrid **|**/ Base**|**line**|||||
|Real GDP|1.00|1.04|0.95|0.86*|0.87|0.90|
|CPI Infation|1.00|0.98|0.92*|0.91***|0.87**|0.85**|
|Unemployment rate|1.00|1.16|1.22|1.21|1.15|1.08|
|Federal funds rate|1.00|0.88***|0.85|0.83|0.79|0.73|
|Credit Spread|0.98|1.00|0.93|0.87|0.83*|0.80*|



**Baseline forecast** tilts Raw BVAR on survey nowcasts only **Hybrid forecast** tilts Raw BVAR on both survey nowcasts and long-run forecasts 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 21 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Results IV: Density Forecast Accuracy 

## **Full Sample (1994.Q1 - 2016.Q4) Small BVAR** (est. 1985+) 

||h=1Q|h=4Q|h=6Q|h=8Q|h=10Q|h=12Q|
|---|---|---|---|---|---|---|
|**Relative CRPS: Hybr**|**id - Bas**|**eline**|||||
|Real GDP|0.00|0.01|-0.05|-0.12**|-0.11*|-0.09**|
|CPI Infation|0.00|-0.02|-0.06*|-0.06***|-0.10**|-0.12**|
|Unemployment rate|0.00|0.02|0.04|0.05|0.04|0.03|
|Federal funds rate|0.00|-0.03**|-0.06|-0.11|-0.17|-0.24*|
|Credit Spread|0.00|0.00|-0.02|-0.04*|-0.06*|-0.08*|



**Baseline forecast** tilts Raw BVAR on survey nowcasts only **Hybrid forecast** tilts Raw BVAR on both survey nowcasts and long-run forecasts 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 22 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Results V: Time-Varying VAR 

## **Full Sample (1994.Q1 - 2016.Q4) TVP-VAR SV** 

|**elative MSE: MSE **|h=1Q<br> **Hybrid T**|h=4Q<br>**VP-VAR**|h=6Q<br> **SV / M**|h=8Q<br>**SE Baselin**|h=10Q<br>**e TVP-V**|h=12Q<br>**AR SV**|
|---|---|---|---|---|---|---|
|Real GDP|1.00|0.93|0.88|0.86|0.90|1.00|
|CPI Infation|1.00|1.00|0.87***|0.81***|0.78***|0.81***|
|Unemployment rate|1.00|1.02|1.04|1.05|1.06|1.08|



#### **Relative MSE: MSE Hybrid TVP-VAR SV / MSE Baseline TVP-VAR SV** 

h=1Q h=4Q h=6Q h=8Q h=10Q h=12Q 

#### **Relative CRPS: CRPS Hybrid TVP-VAR SV - CRPS Baseline TVP-VAR SV** 

|Real GDP|0.00|-0.05|-0.06|-0.07|-0.04|0.02|
|---|---|---|---|---|---|---|
|CPI Infation|0.00|-0.01|-0.03|-0.05|-0.06|-0.04|
|Unemployment rate|0.00|-0.01|-0.01|-0.01|-0.01|-0.01|



**Baseline forecast** tilts TVP-VAR SV on **survey nowcasts only Hybrid forecast** tilts TVP-VAR SV on both survey nowcasts and long-run 

<mark>Tallman and Zaman () Tilting BVAR Forecasts using survey</mark> 

<mark>BoE Forecasting 2018 23 / 28</mark> 

## **Forecast Accuracy Comparison** 

## **Hybrid VAR Forecasts** 

## **versus** 

## **Univariate Benchmarks** 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 24 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Results VI: Horse race 1 

CPI Inflation Forecast Accuracy: Hybrid 1960+ vs. Univariate Benchmarks 

### **Point Accuracy (1994.Q1 - 2016.Q4)** 

||h=2Q|h=4Q|h=6Q|h=8Q|h=10Q|h=12Q|
|---|---|---|---|---|---|---|
|**elative MSE: MSE Hybrid f**<br>RW (Atkeson and Ohanian)|**rom Med**<br>0.82**|**ium BVA**<br>0.87**|**R / MS**<br>0.86**|**E Univar**<br>0.77|**iate**<br>0.82*|0.90***|
|UCSV (Stock and Watson)|0.96|0.99|0.97|0.94|0.91|1.00|
|AR Gap (Faust and Wright)|1.02|0.98|0.98|0.94**|0.94**|0.94**|
|SPF|1.00|1.03|||||



#### **Relative MSE: MSE Hybrid from Medium BVAR / MSE Univariate** 

### **- Density Accuracy (1994.Q1 2016.Q4)** 

|**elative CRPS: C**|h=2Q<br>**RPS Me**|h=4Q<br>**dium BV**|h=6Q<br>**AR - CRP**|h=8Q<br>**S UCSV**|h=10Q|h=12Q|
|---|---|---|---|---|---|---|
|Baseline - UCSV|0.05|0.15**|0.15***|0.19***|0.24***|0.24**|
|Hybrid - UCSV|0.00|0.03|0.03|0.01|0.04|0.10**|



#### **Relative CRPS: CRPS Medium BVAR - CRPS UCSV** 

<mark>Tallman and Zaman () Tilting BVAR Forecasts using survey</mark> 

<mark>BoE Forecasting 2018 25 / 28</mark> 

# Results VII: Horse race 2 

## Forecast Accuracy: Hybrid 1960+ vs. TVP-VAR SV 

### **Point Accuracy (1994.Q1 - 2016.Q4)** 

|**elative MSE: MSE **|h=1Q<br> **Hybrid S**|h=4Q<br>**mall BV**|h=6Q<br>**AR / MS**|h=8Q<br>**E Baseline **|h=10Q<br> **TVP-VA**|h=12Q<br>**R SV**|
|---|---|---|---|---|---|---|
|Real GDP|1.00|1.03|0.93|0.93*|0.95|1.03|
|CPI Infation|1.00|0.99|0.94***|0.87***|0.83**|0.82**|
|Unemployment rate|1.00|1.06|1.05|1.02|1.02|1.02|



**Relative MSE: MSE Hybrid Small BVAR / MSE Baseline TVP-VAR SV** 

### **- Density Accuracy (1994.Q1 2016.Q4)** 

||h=1Q|h=4Q|h=6Q|h=8Q|h=10Q|h=12Q|
|---|---|---|---|---|---|---|
|**Relative CRPS: CRP**|**S Hybrid S**|**mall BV**|**AR - CR**|**PS Bas**|**eline TVP**|**-VAR SV**|
|Real GDP|0.11***|0.08*|0.02|0.02|0.04|0.07**|
|CPI Infation|-0.05***|0.01|0.03|-0.01|-0.03|-0.03|
|Unemployment rate|0.01***|-0.01|-0.04|-0.06|-0.08|-0.08|



<mark>Tallman and Zaman () Tilting BVAR Forecasts using survey</mark> 

<mark>BoE Forecasting 2018 26 / 28</mark> 

# Additional 



Compare and assess implications on forecast of a range of values Across surveys including with shorter history e.g. Summary of Economic Projections (SEP); median and range as mean and variance restrictions These days policy makers communicate their view of the underlying trend rates Compare how model’s forecast of core variables change, Policymaker A vs. B 



Does not require survey history to match estimation sample Could be beneficial for developing and emerging countries 



Interpolate survey forecasts for missing quarters 







Well-established survey forecasts hard to outperform (e.g. Croushore,2010) But they cover smaller number of variables and forecast horizons; infrequent SPF and Blue Chip report forecast values for five quarters and 10-year out 



Taylor-rule restriction over the forecast horizon (e.g. Robertson et al, 2005) 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 27 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Conclusion 



Approach to construct Hybrid forecast consisting of survey nowcast, VAR forecast, and long-run survey forecast 



Use Relative Entropy; easily adapt to existing VARs 



Meaningful gains in forecast accuracy in all VAR models 





Gains largest for fixed parameter VARs estimated with longer sample An important practical result; lends credibility to the use of simple VARs for production of forecasts under strict time constraints 



Inflation hybrid forecasts rival univariate benchmark models 



A useful practical contribution for monetary policy makers 



Hybrid forecasts’ accuracy from simple VARs rivals TVP-VARs 



Extent of improvements suggest a post-estimation method to accommodating structural change and moving end points 

<mark>Tallman and Zaman ()</mark> 

<mark>28 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

<mark>BoE Forecasting 2018</mark> 

## **Extra Slides** 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 29 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

Figure: Real-Time Long Run Forecasts: GDP and Unemployment Rate 



<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 30 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

Figure: Real-Time Long Run Forecasts: CPI and Short-Term Interest Rate 



<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 31 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

Figure: Cumulative Squared Error 





<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 32 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

Figure: Cumulative CRPS 





<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 33 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Appendix Result: Point Forecast Accuracy 

## **Full Sample (1994.Q1 - 2006.Q4) Small BVAR** (est. 1960+) 

||h=1Q|h=4Q|h=6Q|h=8Q|h=10Q|h=12Q|
|---|---|---|---|---|---|---|
|**Relative MSE: Hybrid **|**/ Base**|**line**|||||
|Real GDP|1.00|0.96|0.91|1.02|1.05|1.07|
|CPI Infation|1.00|0.86**|0.68***|0.63***|0.46***|0.49***|
|Unemployment rate|1.00|1.01|0.94|0.87|0.90|0.95|
|Federal funds rate|1.00|1.11*|1.07|0.92|0.79|0.73|
|Credit Spread|1.02|1.10|0.93*|0.82*|0.78*|0.79*|



**Baseline forecast** tilts Raw BVAR on survey nowcasts only **Hybrid forecast** tilts Raw BVAR on both survey nowcasts and long-run forecasts 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 34 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Appendix Result: Point Forecast Accuracy 

## **Full Sample (1994.Q1 - 2006.Q4) Small BVAR** (est. 1985+) 

||h=1Q|h=4Q|h=6Q|h=8Q|h=10Q|h=12Q|
|---|---|---|---|---|---|---|
|**Relative MSE: Hybrid **|**/ Base**|**line**|||||
|Real GDP|1.00|0.98|1.00|0.86**|0.88**|0.92|
|CPI Infation|1.00|0.89**|0.79**|0.85***|0.80*|0.92|
|Unemployment rate|1.00|0.91|1.00|1.03|0.98|0.92|
|Federal funds rate|1.00|0.88***|0.83|0.81*|0.79*|0.78**|
|Credit Spread|1.00|1.03|0.94|0.89*|0.86*|0.89*|



**Baseline forecast** tilts Raw BVAR on survey nowcasts only **Hybrid forecast** tilts Raw BVAR on both survey nowcasts and long-run forecasts 

<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 35 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

### Figure: More on Shock Uncertainty 

Knotek and Zaman (2017, IJF forthcoming) 





<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 36 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Methodology: Relative Entropy 



Start with a predictive density **p(Y)** 



_D_ draws each with a weight _wi_ = 1 _/D_ , where _i_ = 1 _, ...D_ 



Modify it to obtain a new predictive density **g(Y)** 



such that it satisfies a given set of moment conditions _g_ ¯ (e.g. survey forecasts) E _g_ ( _Y_ ) =<sup>�</sup><sup>_D_</sup> _i_ =1<sup>_w ∗_</sup> _i_<sup>_p_(</sup><sup>_Yi_) =</sup><sup>_g_¯</sup> Minimizes the relative entropy (i.e. Kullback-Liebler Information Criterion) _g_ ( _Y_ ) as close as possible to _p_ ( _Y_ ) in the information-criterion sense equivalent to solving for new weights 





satisfies the following constraints 



<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 37 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

# Methodology: Relative Entropy 



Density _g_ ( _Y_ ) is essentially a re-weighted original density _p_ ( _Y_ ) to work there needs to be support in _p_ ( _Y_ ) for the moment conditions 



The solution to the minimization problem using method of Lagrange 



where _γ_ is the vector of Lagrange multipliers associated with the constraints 



_γ_ can be obtained as a solution to the following minimization problem 



<mark>Tallman and Zaman ()</mark> 

<mark>BoE Forecasting 2018 38 / 28</mark> 

<mark>Tilting BVAR Forecasts using survey</mark> 

