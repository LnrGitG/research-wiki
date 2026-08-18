---
title: Claessens. What drives housing prices
type: paper
source_pdf: raw/papers/Claessens. What drives housing prices.pdf
converted: 2026-08-18
---

## Erasmus University Rotterdam 

Erasmus School of Economics 

Master Thesis Econometrics & Management Science Quantitative Finance FEM61008 

# **What drives housing prices? A PVAR approach** 

_Author:_ 

Remco Claessens 475839 

_Supervisor:_ 

dr. Annika Camehl - Erasmus University Rotterdam _Second assessor:_ 

dr. Andrea Naghi - Erasmus University Rotterdam 

April 29, 2023 

This paper models the housing prices of an extensive set of countries to see if the forecasting accuracy of the housing prices can be improved and if foreign variables matter for the housing prices. This research uses a PVAR framework with a GVAR, Bayesian and LASSO approach to see which model and corresponding assumptions fits the data the best. Furthermore, we look at the effect of monetary policy shocks by the federal reserve on the housing prices. This research finds that the forecast of the housing prices can be improved for most of the countries with the different frameworks. However, there is not one universal model that performs the best for all of the countries. Moreover, the results suggest that spillovers exist between countries and therefore influencing the housing prices of different countries. Lastly, we see that the housing prices in most of the countries decrease in a period after a surprise tightening shock. 

The content of this thesis is the sole responsibility of the author and does not reflect the view of the supervisor, second assessor, Erasmus School of Economics or Erasmus University. 

## **Acknowledgements** 

I would like to thank my supervisor dr. Annika Camehl of the Erasmus University Rotterdam, who gave me insightful comments during my research and earlier versions of this paper. I would also like to thank her for sharing her code, which is used for this research, as is the case for the code of Dimitris Korobilis. 

Furthermore, I would like to thank my family and girlfriend, Willemijn, who supported me throughout my research and writing process. 

## **Contents** 

|**1**|**Intr**|**oduction**|**1**|
|---|---|---|---|
|**2**|**Dat**|**a**|**4**|
|**3**|**Me**|**thodology**|**9**|
||3.1|General PVAR model . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>9|
||3.2|GVAR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>9|
||3.3|Bayesian methods . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>12|
|||3.3.1<br>SSVS . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>12|
|||3.3.2<br>SSSS . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>12|
|||3.3.3<br>BFCS and BMixS . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>13|
||3.4|PVAR LASSO . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>15|
||3.5|Forecast implementation . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>16|
|||3.5.1<br>Hyperparameter selection<br>. . . . . . . . . . . . . . .|. . . . . . . .<br>16|
|||3.5.2<br>Lag length selection . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>17|
|||3.5.3<br>Tested models . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>18|
||3.6|Evaluation of the forecast<br>. . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>18|
||3.7|Monetary Shock Series . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>20|
||3.8|Local Projections . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>21|
|**4**|**Res**|**ults**|**22**|
||4.1|Forecasting results<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>22|
|||4.1.1<br>Models with macroeconomic variables . . . . . . . . .|. . . . . . . .<br>22|
|||4.1.2<br>Models with multiple lags<br>. . . . . . . . . . . . . . .|. . . . . . . .<br>27|
||4.2|Variable importance<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>32|
||4.3|Monetary policy shocks . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>35|
|**5**|**Con**|**clusion**|**38**|
|**6**|**App**|**endix**|**43**|
||6.1|Data explanation . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>43|
|||6.1.1<br>Nominal housing prices . . . . . . . . . . . . . . . . .|. . . . . . . .<br>43|
|||6.1.2<br>Infation . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>43|
|||6.1.3<br>GDP . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>44|
|||6.1.4<br>Share price<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>44|
||6.2|Short explanation of the code<br>. . . . . . . . . . . . . . . . .|. . . . . . . .<br>44|



## **1 Introduction** 

The housing prices play an essential role in the economy. For example, the IMF Deputy Managing Director Min Zhu stated in a speech that the housing sector satisfies an essential need (shelter) and that housing is an important component of investment. He summarizes: ”in short, a well-functioning housing sector is critical to the overall health of the economy” (Zhu, 2014). Recent literature also states the importance of housing prices on the economy and especially the business cycle (see Case et al. (2005), Leamer (2007), Aye et al. (2014), Nyakabawo et al. (2015)). Balcilar et al. (2014) demonstrate the significant impact that declining housing prices had on the ”Great Depression”. This means that studying housing prices, due to their big influence on the overall economy, is of great importance. 

When analyzing housing prices, we need to determine what their drivers are so we can explain or forecast this big factor in the overall economy. First, we see in the literature that macroeconomic variables are important to housing prices (Apergis et al. (2003), Jacobsen and Naug (2005), Taylor (2007) and San Ong (2013)). Second, literature shows signs of spillovers of housing prices or the volatility of housing prices from countries to other countries (Vansteenkiste and Hiebert (2011), Cesa-Bianchi (2013), Hirata et al. (2013) and H. S. Lee and Lee (2018)). Third, we need to consider the influence of monetary policy on housing prices. On one hand, literature shows that housing prices and housing starts respond negatively to monetary policy shocks (see Iacoviello (2005), Jarocinski and Smets (2008), Vargas-Silva (2008a), Vargas-Silva (2008b) and Choudhry (2020)), while others find negligible effects of monetary policy shocks on housing prices (for example Fratantoni and Schuh (2003) and Del Negro and Otrok (2007)). 

The mentioned drivers lead to modelling challenges as we want to jointly model the housing prices of countries with macroeconomic variables, while also allowing linkages between countries. This means for example that a regular VAR model is not suitable, because a regular VAR cannot model the cross country dependencies. Therefore, this research makes use of Panel VAR (PVAR) models. PVAR models contain multiple countries with multiple variables in one single model, meaning that lags of foreign variables can influence the housing prices of countries. This means that PVARs can capture dynamic interdependencies. Furthermore, PVARs capture static interdependencies in the covariance matrix. Moreover, PVARs account for cross sectional dynamic heterogeneities as the coefficients can be different for every country. Lastly, literature also states that PVAR models are a good option to model multiple countries in one model (see for example Dees et al. (2007) and Canova and Ciccarelli (2009)). 

However, when jointly modelling countries with different variables in a PVAR setting, one must estimate a lot of parameters. This means more flexibility in the model, but the downside is that the parameter uncertainty in the model becomes high. This makes it less 

1 

clear what the driving factors of housing prices are. Also, the forecasting accuracy drops with parameter uncertainty. Sometimes, the model cannot be estimated altogether due to the high amount of estimated parameters compared to the amount of observations. This problem of high dimensionality in the PVAR model is not a new topic in the literature and numerous methods have been developed to tackle this problem. However, it is not immediately clear what model we should use to model the housing prices. Every model uses different assumptions when estimating the variables which may or may not be better suited to this multi-country setup with multiple variables/predictors from each country. This means that we want to implement different estimation set-ups when modelling the housing prices. 

Therefore, in this research we will use an extensive set of multi-country models which jointly model housing prices of various economies to forecast housing prices and we investigate whether housing prices and macroeconomic variables of different countries are important predictors for housing prices of a specific country. In a second step, we focus on the role of monetary policy shocks. 

First, we use a Global VAR model (GVAR), because GVAR models have already been used in forecasting exercises and it shows promising results compared to the regular VAR models (Han and Hee Ng (2011) and Greenwood-Nimmo et al. (2012)). In a GVAR model, one assigns weights to the variables from the foreign countries in country-specific VARs to create fewer variables in the model. This leads to a sparser and thus better to estimate model (see Pesaran et al. (2004), Dees et al. (2007), Pesaran et al. (2009), Cuaresma et al. (2016) for more). Also, due to the weights, we know for each country which variables, originating from which specific country, are important to estimate the housing prices of a specific country. 

Another kind of model that we use for this research is the Bayesian Stochastic Search Specification Selection (SSSS) (Koop & Korobilis, 2016). This method imposes prior restrictions in the PVAR framework. Using the SSSS method, it is possible to explicitly model the dynamic and static interdependencies and the cross-section heterogeneities. Also, we can analyse the influence of each country on other countries. 

Korobilis (2016) extends on the SSSS framework and creates two new priors: the Bayesian Factor Clustering and Selection (BFCS) prior and the Bayesian Mixture Shrinkage (BMixS) prior. This research also incorporates these priors. 

Literature also shows promising results for SSSS, BFCS and BMixS when forecasting macroeconomic variables. For example, Christou et al. (2017) already use SSSS, BFCS and BMixS to forecast the real housing returns in ten countries with the help of newsbased measure of economic policy uncertainty. In their results, these methods outperform the AR and VAR benchmark for most countries. Furthermore, SSSS, BFCS and BMixS also outperforms the benchmark in Koop and Korobilis (2019). Next to Bayesian methods, one can look at machine learning methods. One of the more 

2 

well known methods is the Least Absolute Shrinkage and Selection Operator (LASSO), which is introduced by Tibshirani (1996). Numerous papers use the LASSO penalty in VAR settings (see for example Ren and Zhang (2010), W. Lee and Liu (2012), Basu and Michailidis (2015) andMelnyk and Banerjee (2016)). However, we cannot implement these methods into our PVAR setting, as they are built for the VAR setting and do not take PVAR characteristics into account. For example, the LASSO penalty is fixed for the whole system, but countries can be different such that different penalties are required for each country. Camehl (2022) develops a panel Lasso approach for the PVAR setting, which we will use. This Lasso approach keeps the nature of the PVAR model while creating a reduced form model. Camehl (2022) also show some promising results when forecasting inflation and industrial production growth of several countries. 

In this research, we model and forecast the housing prices with the GVAR, SSSS, BFCS, BMixS and Lasso PVAR. All of these models use different assumptions and estimation methods. We compare the forecast accuracy and the output of the different models to see if foreign housing prices matter, if macroeconomic variables influence the housing prices and to determine which model and therefore assumptions and restrictions fit the data the best. 

Furthermore, next to analysing the influence of foreign housing prices and macroeconomic variables, we want to explicitly model the effect of monetary policy shocks in housing prices. A lot of research has been done by identifying monetary policy shocks out of a structural reduced form VAR model. For example, Lanne and L¨utkepohl (2008) used the changes in the volatility of the shocks for identification. Others used a high frequency identification (HFI) (Cook and Hahn (1989), Kuttner (2001), Cochrane and Piazzesi (2002)). This type of identification uses the fact that a disproportionate amount of monetary news is revealed at the time of the eight regularly scheduled FOMC meetings each year (see also Nakamura and Steinsson (2018)). 

The monetary policy shock series that this research uses is developed by Bu et al. (2021). With their approach, they identify monetary policy shocks in such a way that it captures conventional policy changes (for example interest rate changes) as well as unconventional policy changes (for example Quantitative Easing). This shock series is based on the US monetary policy. With the identification of the monetary policy shocks, the last step is to look at the effect of these shocks on the housing prices. A method that proves to perform really well is the local projections method (Jord`a, 2005), where we retrieve an impulse response function that reveals the effect of the US monetary policy changes on each of the countries. 

For this research we use data from the OECD (OECD, 2022). We retrieve data for housing prices, inflation, gross domestic product and share prices of 16 different countries from 1970Q1 until 2021Q4. Also, we use an existing monetary policy shocks series from Bu et al. (2021). 

3 

Research on housing prices has already been done. However, most of the research has been done on investigating the housing prices of a single country. This research combines the housing prices of different countries into a single model with multiple variables into a panel VAR model, which has not been done with housing prices so extensively. The research that comes closest to this is done by Christou et al. (2017) where they forecast the housing prices of 10 countries with Bayesian methods. However, the current research incorporates more countries and more variables per country. Moreover, this research does not only use Bayesian methods, but also a PVAR LASSO approach to see which kind of model suits the data better. Also, next to forecasting, this research analyzes which countries influence the housing prices of other countries. Also, with the results of this research, policymakers are able to see what effect the US monetary policy will have on the housing prices of their country, so they can anticipate the US monetary policy. This research finds that the forecasts of the housing prices are more accurate with the tested PVAR models, indicating that housing prices of other countries do matter when forecasting housing prices. We find that especially the point forecasts improve with the tested models, whereas the improvement on the density forecasts is less significant. On average, we conclude that the LASSO models score better than their counterparts for both the point and density forecasts. However, there is not a single model that consistently outperforms for every single country, meaning that for each country a different model is preferred. 

Moreover, if we analyze the estimated parameters of the models, we see that there exist some dependencies between countries, indicating that it is appropriate to jointly model the housing prices of different countries, as the housing prices of countries can spillover. Furthermore, the impulse response functions from the local projections method show that the housing prices do react mostly negatively to a positive monetary policy shock, where a positive monetary policy shock means tightening the monetary policy. 

This paper is structured as follows. Section 2 covers the data and some characteristics of the data. Section 3 contains the methodology, consisting of the models used and the methods for comparing them. Section 4 presents the results. Lastly, section 5 concludes the research and provides directions for further research. 

## **2 Data** 

This research uses data from the OECD (OECD, 2022). The data we use is the nominal housing prices of 16 countries, being: Australia, the Netherlands, Canada, Switzerland, Germany, Denmark, Spain, Finland, France, United Kingdom, Ireland, Italy, Japan, Sweden, United States and South Africa<sup>1</sup> . Furthermore, we use inflation, Gross Domestic 

> 1The country codes are respectively: AUS, NLD, CAN, CHE, DEU, DNK, ESP, FIN, FRA, GBR, IRL, ITA, JPN, SWE, USA and ZAF 

4 

Product and a share price indicator, all reported by the OECD for the mentioned countries. See section 6.1 in the appendix for a more in detail explanation of the variables. The data is quarterly reported from 1985Q2 until 2021Q4, which makes it 147 datapoints per country in total. 



Figure 1: The nominal housing prices of 5 countries (2015 = 100) 

Figure 1 shows the values of the housing prices for five different countries. We can see that the housing prices are generally going up throughout the years. Also, we see that the housing prices in the Netherlands, USA and Great Britain are going down when the financial recession started in 2008. However, the housing prices in Australia and Germany do not show that pattern. 

5 



Figure 2: Cross correlations of the housing prices 

Figure 2 shows a heatmap of the cross correlations between the countries. We see that almost all the variables are highly positive correlated. This is in line with what we expect due to how the data is structured, because for every country the variable is set to 100 in 2015 and the other values are based on 2015. However, it does imply that the housing prices of the countries are comoving. The only outlier in this case is Japan, which has negative correlations with all the other countries. This is due to the fact the housing price of Japan drops in a large amount of the sample, while the housing prices of the other countries are rising. Also, when looking at this graphs, we suspect non-stationarity for the variables. As we implement VAR type models in this research, we need to check the variables for every country for stationarity. We do this by the means of an augmented Dickey–Fuller (ADF) test. 

6 

Table 1: P values of the ADF test 

||AUS|NLD|CAN|CHE|DEU|DNK|ESP|FIN|
|---|---|---|---|---|---|---|---|---|
|House|1.00|1.00|1.00|1.00|1.00|1.00|1.00|1.00|
|Inf|0.17|0.40|0.18|0_._04<sup>_∗_</sup>|0.30|0_._05<sup>_∗_</sup>|0_._05<sup>_∗_</sup>|0_._04<sup>_∗_</sup>|
|GDP|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|
|Share|0.98|0.96|0.99|1|0.95|1.00|0.66|0.80|
||FRA|GBR|IRL|ITA|JPN|SWE|USA|ZAF|
|House|1.00|1.00|1.00|1.00|0.66|1.00|1.00|1.00|
|Inf|0_._01<sup>_∗_</sup>|0_._20|0.08|0_._01<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._03<sup>_∗_</sup>|0.31|0.11|
|GDP|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|0_._00<sup>_∗_</sup>|
|Share|0.97|0.94|0.91|0.77|0.73|1.00|1.00|1.00|



Note: This table shows the p values of the ADF test for every variable of every country. A * means that the null hypothesis of a non-stationary time series is rejected at a 5% significance level 

Table 1 shows the results of the ADF test for the variables. We see that only the GDP time series is consistently stationary across the countries. This is due to the fact that the GDP series already contain the log difference of the GDP. To ensure the other variables are also stationary, we take the log difference of the housing prices, the log difference of the share prices and the first difference of the inflation. The reason we take the regular first difference for the inflation is that the inflation contains negative values, meaning that we can not take a log. We perform the ADF test again on the adjusted time series and find that every time series is stationary. Therefore, we continue to work with the adjusted time series. For convenience, we refer to the normal variable names in the text. 

7 



Figure 3: Cross correlations of the first difference of the log housing prices 

Figure 3 shows the correlations of the log first differences of the housing prices. This heatmap shows a different insight than the heatmap with the regular housing prices values. For example, Germany has a negative correlation with almost all the countries, meaning that the housing prices of Germany go down compared to the previous period when the other housing prices are going up. Furthermore, the values of the cross correlation are closer to zero compared to the original cross correlations. The difference between 2 and 3 show that the high correlation from the raw values comes from the positive trend in almost all series. 

Some country pairs are still closely related in figure 3, for example Australia-United Kingdom, France-Spain and Finland-United Kingdom. This makes us believe that countries’ housing prices can contain information for other countries. However, we need to take into account that some countries are not likely to be connected. This means that the reduced form PVAR models used in this research are well suited for this data. 

8 

## **3 Methodology** 

### **3.1 General PVAR model** 

A panel vector autoregressive model is a variant of the regular vector autogregressive model. A PVAR model includes multiple countries with multiple variables. With this setup, it accounts for interdependencies between countries and heterogeneities across variables. First, we denote a general unrestricted PVAR model. This model can be written for country _i_ , with _i_ = 1 _, . . . , N_ : 



where _yi,t_ is a vector of dependent variables with a length of _G_ for country _i_ . _t_ is the moment of time. _Yt−p_ is a vector where the different _yi,t−p_ are stacked and is an _NG ×_ 1 vector. _p_ is the order of the PVAR model and coefficient matrix _Ai,p_ is a _G × NG_ matrix. Lastly, _ϵi,t_ are the error terms with _E_ ( _ϵi,t, ϵj,t_ ) = Σ _ij_ . One can see the problem with an unrestricted PVAR model, as the estimated parameters can become larger than the amount of data in time _T_ , which means the model cannot be identified. Also, in the unrestricted form, the dependencies are unrestricted, which means that one variable of a country can have different relations with the variables of other countries. To counter above mentioned problems, one can look at shrinkage methods. However, we have to treat the PVAR model differently to a ”normal” large VAR model, as we need to take the panel structure of the data into account. 

For convenience later on, we rewrite the Matrix _A_ from equation 1 to: 



where every _Ap,jk_ is a _G × G_ matrix. 

### **3.2 GVAR** 

The first reduced form model that we use is the so called Global VAR model Cuaresma et al. (2016). We rewrite the model in equation 1 to a general VARX model: 



9 

where _yi,t_ is a vector of dependent variables with a length of _G_ for country _i_ . We define _yi,t_<sup>_∗_</sup> _−_ 1<sup>as:</sup> 



where we define _mi,j_ as the non-negative weight of country _j_ on country _i_ , with _mi,i_ = 0 and<sup>�</sup><sup>_N_</sup> _j_ =1<sup>_mi,j_=1.Also,notethat</sup><sup>_mi,j_and</sup><sup>_mj,i_arenotnecessarilyequal.Inother</sup> words, the value of a variable of country _i_ at time _t_ is dependent on the previous values of variables of country _i_ and weighted averages of the variables of the other countries. This means that, based on the weights _mi,j_ , the influence of some variables will shrink to zero when _mi,j_ is close to zero. 

When choosing the weights for the GVAR model, one can consider a lot of theoretically possible options. However, we are subject to data availability. For this research, we make a weight matrix with the help of trade weights. This is also a well known and widely used method for GVAR models (see for example Dees et al. (2007)), because trade is a major indicator of the business-cycle co-movement (Baxter & Kouparitsas, 2005). We create the trade weights by summing the import and export between the countries over 2015. We retrieve the data about export and import from the WITS (World Integrated Trade Solution) database from the World Bank<sup>2</sup> . After that, we rescale the matrix so that the weights sum to 1 for every equation. 

> 2For example, see https://wits.worldbank.org/CountryProfile/en/Country/NLD/Year/2015/TradeFlow/EXPIMP for the import and export numbers in 2015 for the Netherlands 

10 



Figure 4: Heatmap of the weights used in GVAR 

For clarity, we show a heatmap of the weights used for the GVAR model<sup>3</sup> . Figure 4 shows that heatmap. Two countries stick out with relatively high weights to almost every country, Germany and the United States. 

The main advantage of the GVAR model is that it explicitly reduces the high dimensionality of the general PVAR model, while still allowing for interdependencies between the countries through the weighted variables. This also means that the user can define the interdependencies themselves and take into consideration what is important for the model and variables. However, this explicit modelling comes at a cost. If the user misspecifies the weights in the model then the entire model is misspecified and with that any insights and results. 

> 3For the raw weight values, see table 21 in the appendix 

11 

### **3.3 Bayesian methods** 

Another model that we use is the Stochastic Search Specification Selection (SSSS) proposed by Koop and Korobilis (2016). They took the framework of the Stochastic Search Variable Selection (SSVS) and transformed it in a way so that the model takes the panel structure of the data into account. For more on SSVS, see George and McCulloch (1993) and George et al. (2008). In their original paper, they distinguish three different restrictions that can be imposed on the unrestricted PVAR model: dynamic interdependencies (DI), static interdependencies (SI) and cross-section heterogeneities (CSH). However, in later forecasting applications using this model, the SI restriction search is dropped (see for example Korobilis (2016)). This research therefore drops the SI restriction search. 

#### **3.3.1 SSVS** 

SSVS is a method that shrinks the parameters to zero. It uses a prior to determine an estimated value for the parameters. It can be expressed as: 



with _αj_ being the parameter that is estimated, which in our case would be an element in _Ap_ in equation 1. _γj ∈_ 0 _,_ 1 an unknown parameter, _c >_ 0 a small scalar, and _τj_<sup>2achosen</sup> variance. With this mixture, we can see that the first part has a variance near 0 and the second has a large variance. So based on the value of _γj_ , _αj_ is estimated near zero ( _γj_ = 0) or is unrestricted ( _γj_ = 1). Koop and Korobilis (2016) used this Bayesian SSVS framework for their SSSS method. 

#### **3.3.2 SSSS** 

In the SSSS we search for DI and CSH. A DI between country _j_ and _k_ means that the variables of country _k_ affect the variables of country _j_ . With this matrix, we can impose that there are no DIs from country _k_ to country _j_ by setting _Ap,jk_ to zero for every _p_ . However, this restriction does not mean that there are no DIs from country _j_ to country _k_ , so _Ap,kj_ is not set to zero (unless we impose a restriction on that of course). We implement this restriction in the framework of equation 5 as follows: 





where _Ap,jk_ is the _G × G_ matrix from equation 2. If _γjk_<sup>_DI_is0,</sup><sup>_Ap,jk_isshrunktozero.So</sup> instead of shrinking one variable to zero as in the SSVS framework, entire blocks of the matrices are reduced to zero. 

12 

CHS between country _j_ and _k_ means that the VAR coefficients of the own variables differ between the countries, while an absence of CHS means that they are exactly the same. Imposing this restriction in the framework of equation 5 can be done as follows: 





so if _γw_<sup>_CSH_</sup> is equal to 0, the value of _Ajj_ will shrink towards _Aii_ . With the SSSS priors, we cannot get a closed form posterior distribution of the variables. To get the posterior distributions, we use the Gibbs sampler (see Koop and Korobilis (2016) for more details). 

The main advantage of SSSS is that it clearly takes the PVAR structure into account with the restriction searches. It shrinks entire blocks of the parameter matrix to zero corresponding to the country dependencies and it shrinks the countries own VAR coefficients to have similar values to those of other countries. This reduces the high-dimensionality of the general PVAR model. Also, with this Bayesian framework, we can analyze the dependencies between the countries easily by taking a look at the posterior distributions of _γp,jk_<sup>_DI_and</sup><sup>_γ_</sup> _w_<sup>_CSH_</sup> . This can be done by looking at the draws from the Gibbs sampler and averaging them. Also, we do not need to make explicit assumptions about cross-country dependencies as with the GVAR model. Instead, the model itself determines the relationships, meaning that the SSSS is less prone to misspecification. 

The main advantage of the SSSS model is also tied to its main disadvantage. By searching with entire matrices, we can only draw conclusions with respect to cross-country interdependencies and heterogeneities. We do not know which specific variable is important for the interdependencies and heterogeneities. On the other hand, this model can set the effect of an important variable to zero, because the other variables in that specific country are not important for that equation. Also, the structure of the SSSS prior means that the restrictions only hold approximately. 

Furthermore, this model and algorithm requires a lot of computational power, because the MCMC Gibbs sampler needs a lot of draws for accurate results. This means that searching for other hyperparameters in the SSSS model is not feasible time wise. 

#### **3.3.3 BFCS and BMixS** 

Korobilis (2016) suggests two new priors that counter the shortcomings of the SSSS prior. The first prior is the Bayesian Factor Clustering and Selection (BFCS) prior. This prior is inspired by Canova and Ciccarelli (2009). They extract latent factors from the VAR coefficients. These factors serve two purposes: they provide a lower dimensional representation of the coefficients and group relevant coefficients together. To write down this 

13 

prior, we first rewrite the PVAR model to: 



where _Zt_ = _ING ⊗ Yt−_ 1, _α_ = _vec_ ( _A_<sup>_′_</sup> ) is the vector of all the PVAR coefficients with the length of _K_ = _NG_<sup>2</sup> . A structure like Canova and Ciccarelli (2009) can be written as: 



where Ξ is a _K × s_ matrix of factor loadings, _θ_ is an _s ×_ 1 vector with the factors, with _s ≪ K_ and _υ_ The downside with the prior of Canova and Ciccarelli (2009) is that they do not consider that a coefficient might be zero, as every coefficient _αk_ is clustered with a non-zero coefficient _αl_ (Korobilis, 2016). To deal with that problem, Korobilis (2016) proposed the following prior, which he calls the BFCS: 









where ∆ _k_ is the _k_ th row matrix ∆and _δ_ 0 is the Dirac delta. This means that _αk_ has prior a point mass at zero with probability (1- _π_ ) (Korobilis, 2016). 

The second prior is called the Bayesian Mixture Shrinkage (BMixS) prior. This prior is inspired by Dunson et al. (2008), by using infinite mixtures, by means of Dirichlet process priors, in order to generalize spike and slab priors and at the same time allow for soft clustering of similar coefficients (Korobilis, 2016). Korobilis (2016) adjusts the prior of Dunson et al. (2008), as the latter one is not flexible. This prior can be written as: 











with _DP_ ( _θF_ 0) is a Dirichlet process with base measure _F_ 0. We see that _αk_ has a Normal prior, but due to the distribution of _µk_ and _τk_<sup>2)itcanhavemultiplelocations.</sup> The main advantage of these two priors compared to the SSSS prior is that the BFCS en 

14 

BMixS search for each element in the matrices instead of the whole matrix. This means that some of the elements in a matrix can be zero and others nonzero. However, this means that the BFCS and BMixS lose the clear interpretation of interdepencies. Furthermore, these priors also requires a lot of computational power as with the SSSS, because the same algorithm is used. This means that we cannot search for hyperparameters for these priors. 

### **3.4 PVAR LASSO** 

The third type of model that this research uses is a model proposed by Camehl (2022). They used a penalized LASSO approach to be able to get a reduced model for the large PVAR model. First, we rewrite to general PVAR model from equation 1 to a more compact form: 



with _Y_ = ( _Y_ 1 _, . . . , YT_ ), _Yt_ = ( _y_ 1 _′ t_<sup>_, . . . , y_</sup> _Nt′_<sup>)</sup> _′_ and B = ( _B_ 1 _, . . . , BP_ ) with _Bp_ = ( _A_ 1 _p, . . . , ANp_ ) _′_ . Error term _U_ has a mean of zero and covariance Matrix Σ. We can write the optimization problem of the PVAR LASSO as: 



where _Bklp_<sup>_ij_isanelementinB,referringtolag</sup><sup>_ρ_ofvariable</sup><sup>_l_ofunit</sup><sup>_j_intheequationof</sup> variable _k_ of unit _i_ . We distinguish four penalty terms in the equation, namely _α_ , _λ_ , _γ_ and _c_ . 

The penalty _α_ (with _α >_ 0) in _ρ_<sup>_α_</sup> is an autoregressive penalty term. If _ρ_ increases, the penalty term increases. This comes from the idea that recent lags have more information than less recent lags. 

The penalty _λk_ is a VAR penalty that can have different values for each equation _k_ . This penalty term comes from the idea that equations itself have different characteristics and thus needs a seperate penalty term. 

The penalty _γ_ is a PVAR penalty that shrinks the value of the parameter variables to the average of that parameter variable for each equation. This comes from the idea that 

15 

homogeneity between equations exists. 

The penalty _c_ is a PVAR penalty that penalizes variables that are from a different country than the dependent variable in that specific equation. 

As mentioned by Camehl (2022) is the loss function of the optimization problem the weighted sum of the squared residuals with weights from the covariance matrix. 

As in Camehl (2022), we estimate the covariance matrix with the help of Graphical LASSO (GLASSO) (Friedman et al., 2008). We maximize: 



which is a Gaussian penalized log-likelihood. _S_ is the emperical covariance, _tr_ is the trace and _∥_ Ω _∥_ is the sum of absolute values of each element of Ω. 

As with the SSSS method we cannot solve the optimization problem in a closed form. So analog to Camehl (2022) we solve the optimization problem with the coordinate descent algorithm (Friedman et al. (2007) and Friedman et al. (2010)). For the full derivation, see Camehl (2022). 

Analog to the SSSS approach, the PVAR LASSO takes the PVAR structure into account. As mentioned in Camehl (2022) are the PVAR penalties _γ_ and _c_ designed to shrink to the cross-sectional homogeneity and no dynamic interdependencies (similar to the DI and CSH restrictions in SSSS). Furthermore, it comes with additional shrinkage to the AR and VAR coefficients. 

Also, compared to the SSSS, this method searches for the relevance of individual variables instead of looking at an entire block of variables. This means that an important crosscountry variable will not be set to zero, regardless if the other variables in that country are important or not. 

However, we lose the clear interpretation that the SSSS method gives us. This method does not model the cross-sectional homogeneity and dynamic interdependencies as explicitly as the SSSS methods. 

Furthermore, this method requires a lot of computational power. This means that we cannot search extensively for hyperparameters as we want to, because it simply will take too much time. 

### **3.5 Forecast implementation** 

#### **3.5.1 Hyperparameter selection** 

For the LASSO approach, we follow Camehl (2022) to estimate the optimal hyperparameters, which uses a rolling cross-validation approach (Song and Bickel (2011), Stock and Watson (2012)). We split the total of 146 datapoints per variable into three samples, the train, validation and test sets. The first sample is from period 1 until period 118. 

16 

The test sample is used to train the model. After that, we evaluate the one step ahead forecasts for the validation set, which is period 119 until 130. We perform a grid search where _γ_ , _α_ and _c_ are fixed and the optimal _λk_ is found for every combination of _γ_ , _α_ and _c_ . Then we select the group of hyperparameters that minimizes the one step ahead mean squared forecast error of the validation set. The grid of hyperparameters we test follows Camehl (2022) and is as follows: _γgrid_ = [0 _._ 2 _,_ 0 _._ 4 _,_ 0 _._ 6 _,_ 0 _._ 8], _αgrid_ = [0 _._ 2 _,_ 0 _._ 4 _,_ 0 _._ 6 _,_ 0 _._ 8], _cgrid_ = [1 _._ 2 _,_ 1 _._ 4 _,_ 1 _._ 6 _,_ 1 _._ 8] and the grid for _λK_ consists of twelve values between 0 _._ 01 and _max_ ( _max_ ( _XY ′_ )). 

For the Bayesian methods, we do not do a grid search due to the high amount of computional time it requires to estimate a model. Instead, we follow the hyperparameters chosen in Korobilis (2016), which is the following: _c × τj_ = 0 _._ 01, _τj_ = 4, _c × ξj_ = 0 _._ 01, _ξ_ = 4, _π_ = 0 _._ 5 for every Bernoulli distributed variable, _θ_ = 1 and _λ_ = 4. 

#### **3.5.2 Lag length selection** 

Choosing the optimal lag length is important in a PVAR framework. However, we have to take the amount of observations that we have in our dataset into account. For the large PVAR model where we have 16 countries with 4 variables for each country a maximum lag length of 1 can be chosen. Otherwise we cannot estimate the SSSS models due to the lack of observations compared to the amount of variables. 

A lag length of 1 is not an unreasonable assumption for financial variables. Nevertheless, we also want to test the models with a larger lag length. To achieve that, we fit restrictionless PVAR models estimated with OLS with only the housing prices with lag lengths 1, 2, 3 and 4. We only fit housing prices, because we cannot fit multiple variables per country with multiple lags and we want to compare the additional information that more lags give. We fit the model with the observations in the train and validation set and check the Akaike Information Criterion (AIC) and the Schwarz Information Criterion (BIC). 

Table 2: AIC and BIC values of the unrestricted PVAR models 

|Lag length|1|2|3|4|
|---|---|---|---|---|
|AIC|-12524.6|-12543.6|-12573.6|-12481.2|
|BIC|-11744.6|-11033.6|-10337.6|-9523.3|



Table 2 shows the values of the AIC and BIC. We see that the lowest value for the AIC is at lag length 3 and the lowest value for BIC is at lag length 1. This difference can be explained by the fact that the BIC is less tolerant for a higher number of parameters than the AIC. We already implement a model with lag length 1, meaning that we can also fit a model with lag length 3. We can only incorporate the housing prices variables into this model, because adding more variables would mean that we cannot estimate the model. 

17 

#### **3.5.3 Tested models** 

We forecast the housing prices with the following models for both of the applications: 

- GVAR: the GVAR model as described 

- SSSS1: the SSSS model with DI and CSH restriction search 

- SSSS2: the SSSS model with only DI restriction search 

- BFCS: the Bayesian model with the BFCS prior 

- BMixS: the Bayesian model with the BMixS prior 

- LASSO1: the PVAR LASSO model with penalties _λk_ , _c_ and _α_ 

- LASSO2: the PVAR LASSO model with penalties _λk_ , _c_ , _α_ and we set the covariance matrix to the identity matrix 

- LASSO3: the PVAR LASSO model with penalties _λk_ , _c_ , _α_ and _γ_ 

- OLS: the unrestricted PVAR model estimated with OLS 

- RW: the random walk model 

We use two benchmark models in this research. The first benchmark model is the unrestricted PVAR model. This model can be estimated with OLS. In line with the models we estimate, we estimate a PVAR model with 4 variables per country and 1 lag and a PVAR model with only the housing prices per country and 3 lags and compare those to their respective counterparts. Furthermore, we compare the models to a random walk model where the prediction of future observations is simply the last known observation of that specific variable. 

### **3.6 Evaluation of the forecast** 

To evaluate the models, we forecast the variables with a rolling window over the period 2018Q4-2021Q4 which is in total 16 observations to forecast per country. However, we have a maximum forecast horizon of 4, meaning that we forecast a total of 12 observation per forecast horizon. For more than one step ahead forecasts we use iterated forecasts (Marcellino et al., 2006). 

In this research we use the Mean Squared Forecast Error (MFSE) to compare the point forecasts of the PVAR models to the benchmark model. We calculate the MSFE as follows: 



18 

with Z being the amount of forecasts, _yi,k,z_ the actual value of the variable _k_ from country _i_ at time _z_ . To compare the MSFE of the PVAR models to the benchmark model, we use the modified Diebold Mariano test proposed by Harvey et al. (1997). This test is based on the regular Diebold Mariano test (Diebold & Mariano, 1995), which uses the Diebold Mariano statistic. This statistic is calculated as follows: 



where _d_ is a vector where we subtract the errors of the PVAR models from the errors of the benchmark model. _d_<sup>¯</sup> is the mean of _d_ and _σ_ ˇ _d_ is calculated as follows: 



ˆ with _σdt_ being the standard deviation of _d_ . 

The modified Diebold Mariano statistic as calculated as follows: 



with h as the forecast horizon, Z the amount of forecasts, DM as calculated in equation 25 and _H_ 0 being that the forecast errors are equal to each other or that the forecast of the benchmark model is better. This means we are doing a one sided test, as we are only interested whether the PVAR models are performing better than the benchmark model. 

The reason why we use the modified DM test compared to the regular one has to do with our amount of forecasts. The amount of forecasts in this research is quite low and the regular DM test tends to over-reject the null hypothesis for a small sample size. The modified DM test takes a small sample size into account, which is suitable in our case. Next to the point forecast, we also evaluate the density forecasts, because the density forecasts are able to capture the uncertainty of the estimates. We compare the density forecasts of the models with the average logarithmic scores (ALS) (Amisano & Giacomini, 2007). We calculate the ALS as follows: 



where _f_<sup>ˆ</sup> _j,t_ is the estimated predictive density. 

For estimating the predictive density for the Bayesian models we follow Korobilis (2016). For the LASSO methods and the GVAR method we follow Garcia et al. (2017) and Camehl (2022) to calculate the predictive density, where they bootstrap the in-sample residuals. For every rolling window we randomly draw an in sample-residual of the equation and that value is added to the forecast. We repeat that 10,000 times to construct the predictive 

19 

density. 

To compare the ALS of the PVAR models to the benchmark model, we follow Amisano and Giacomini (2007). We construct an likelihood ratio statistic as follows: 



with Z the amount of forecasts, _o_ the model we want to test and _m_ the benchmark model. The test statistic is as follows: 



with ˆ _σAG_ being the standard deviation of _AG_<sup>_o,m_</sup> . This statistic follows an standard normal distribution under the null hypothesis (see for example Giannone et al. (2015) and Berg and Henzel (2015)). 

### **3.7 Monetary Shock Series** 

We retrieve an already existing US federal reserve monetary shock series from Bu et al. (2021). The series is created by using a two-step approach with partial-least squares estimation, which involves the utilization of daily interest rate data across various maturities. The underlying concept of constructing this measure is to estimate the monetary policy shock, which is an unobservable phenomenon, by employing the Fama and MacBeth two-step regressions (Fama & MacBeth, 1973). The process starts with gauging the response of outcome variables to FOMC announcements. Firstly, time-series regressions are conducted to evaluate the sensitivity of interest rates at different maturities to FOMC announcements, which is similar to the asset beta in the original Fama-MacBeth method. This regression can be written as: 



where ∆ _Ri,t_ is equal to the change in the zero-coupon yield with maturity _i_ in years. Also they define: _ξi,t_ = _−βiϵ_ 2 _,t_ + _ϵi,t_ , with _ϵi,t_ being the monetary policy shock unrelated to monetary policy news and thus the shock we want to get. We see that the full spectrum of maturity yields are regressed to the 2 year rate. Bu et al. (2021) give three reasons for the 2 year rate. First, it is used by many others in the literature (see for example Gilchrist et al. (2015)). Second, it is not constrained by the Zero Lower Bound while capturing crucial aspects of Fed monetary policy (Swanson & Williams, 2014). Third, they state that normalizing to a relatively short-term rate helps reduce the information effect from the estimates. 

After the initial regression we get estimates of the monetary policy shock with the follow- 

20 

ing regressions: 



where _β_<sup>ˆ</sup> _i_ is estimated from equation 31 and _ϵ_<sup>_aligned_</sup> _t_ is the monetary policy shock we want to estimate<sup>4</sup> . They do these regressions for 1-day window periods around FOMC announcements. Subsequently, all outcome variables are regressed against the corresponding estimated sensitivity index from step one for each time t in the second step. This results in the monetary policy shock series as the set of estimated coefficients obtained from the Fama-MacBeth style second step regressions. 

The reason why we take this shock series instead of others (see for example Nakamura and Steinsson (2018)), is threefold. First, the shock series is almost unpredictable from the information available. Second, the shock contains no siginifcant central-bank information effect and third, this series stably bridges periods of conventional and unconventional policy making by taking the full maturity spectrum of interest rates. 

Lastly, we note that the original series is a monthly time series. As we do not have monthly housing price data, we transform the monetary policy shock series into quarterly data by summing the values of the shock series in each quarter. 

### **3.8 Local Projections** 

To get impulse response functions, we use local projections (Jord`a, 2005). We use the following local projection model: 



where _yi,t_ is the value of the housing price variable of country _i_ at time _t_ and _brwt_ the value of the monetary policy shock of Bu et al. (2021) at time _t_ . We do this regression for each country with the US monetary policy shocks. This is because the monetary policy shock series is only available for the US monetary policy and literature also shows that the US monetary policy shocks transmits to other countries. For example Kim (2001) shows that US monetary expansions lead to a higher output of the other G6 countries (see also Bluedorn and Bowdler (2011) and others). Ehrmann and Fratzscher (2009) show evidence of spillovers to the global financial markets (see also Wongswan (2009), Fratzscher et al. (2018) and Georgiadis (2016)). 

We can use the estimated _βi,h_ to get an impulse response function of country _i_ to get the effect of monetary policy shocks for that country. We do this for every country in the dataset. 

> 4We retrieve this series from https://www.federalreserve.gov/econres/feds/a-unified-measure-of-fedmonetary-policy-shocks.htm, it is reported from 1994M1 until 2020M12 

21 

## **4 Results** 

### **4.1 Forecasting results** 

#### **4.1.1 Models with macroeconomic variables** 

Table 3: One step ahead relative MSFE of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|1.121|1.335|1.317|2.098|1.407|1.001|1.084|**0.929**|1.091|
|NLD|0_._061<sup>_∗∗∗_</sup>|0_._252<sup>_∗∗_</sup>|0_._251<sup>_∗∗_</sup>|0_._078<sup>_∗∗∗_</sup>|0_._253<sup>_∗∗_</sup>|**0**_._**047**<sup>_∗∗∗_</sup>|0_._050<sup>_∗∗∗_</sup>|0_._060<sup>_∗∗∗_</sup>|0_._053<sup>_∗∗∗_</sup>|
|CAN|0_._427<sup>_∗∗_</sup>|0_._451<sup>_∗∗_</sup>|0_._302<sup>_∗∗_</sup>|**0**_._**192**<sup>_∗∗_</sup>|0_._395<sup>_∗∗_</sup>|0_._284<sup>_∗∗_</sup>|0_._250<sup>_∗∗_</sup>|0_._325<sup>_∗∗_</sup>|0_._225<sup>_∗∗_</sup>|
|CHE|0_._327<sup>_∗∗_</sup>|0_._398<sup>_∗∗_</sup>|**0**_._**198**<sup>_∗∗_</sup>|0_._261<sup>_∗∗_</sup>|0_._587<sup>_∗_</sup>|0_._210<sup>_∗∗_</sup>|0_._212<sup>_∗∗_</sup>|0_._243<sup>_∗∗_</sup>|0_._338<sup>_∗∗_</sup>|
|DEU|0_._723<sup>_∗_</sup>|0.923|1.066|0_._781<sup>_∗_</sup>|0.884|0.842|0_._596<sup>_∗_</sup>|0_._403<sup>_∗∗_</sup>|**0**_._**352**<sup>_∗∗_</sup>|
|DNK|0_._177<sup>_∗∗_</sup>|0_._270<sup>_∗∗_</sup>|0.883|0_._200<sup>_∗∗_</sup>|0_._268<sup>_∗∗_</sup>|0_._147<sup>_∗∗_</sup>|0_._213<sup>_∗∗_</sup>|**0**_._**146**<sup>_∗∗_</sup>|0_._156<sup>_∗∗_</sup>|
|ESP|0_._120<sup>_∗∗_</sup>|0.834|0.839|0_._148<sup>_∗∗_</sup>|0_._187<sup>_∗∗_</sup>|0_._177<sup>_∗∗_</sup>|0_._112<sup>_∗∗_</sup>|0_._213<sup>_∗∗_</sup>|**0**_._**075**<sup>_∗∗∗_</sup>|
|FIN|0_._185<sup>_∗∗_</sup>|0_._575<sup>_∗_</sup>|1.091|0_._131<sup>_∗∗_</sup>|0.950|**0**_._**105**<sup>_∗∗∗_</sup>|0_._112<sup>_∗∗_</sup>|0_._143<sup>_∗∗_</sup>|0_._125<sup>_∗∗_</sup>|
|FRA|0.940|11.528|8.740|**0**_._**640**<sup>_∗∗_</sup>|0_._748<sup>_∗∗_</sup>|1.029|1.018|0.845|1.222|
|GBR|0_._433<sup>_∗∗_</sup>|3.107|2.177|0_._557<sup>_∗∗_</sup>|0_._477<sup>_∗∗_</sup>|0_._386<sup>_∗∗_</sup>|**0**_._**376**<sup>_∗∗_</sup>|0_._599<sup>_∗_</sup>|0_._483<sup>_∗∗_</sup>|
|IRL|**0**_._**040**<sup>_∗∗∗_</sup>|0_._098<sup>_∗∗∗_</sup>|0_._084<sup>_∗∗∗_</sup>|0_._098<sup>_∗∗∗_</sup>|0_._456<sup>_∗∗_</sup>|0_._057<sup>_∗∗∗_</sup>|0_._089<sup>_∗∗∗_</sup>|0_._275<sup>_∗∗_</sup>|0_._069<sup>_∗∗∗_</sup>|
|ITA|0_._269<sup>_∗∗_</sup>|0_._464<sup>_∗∗_</sup>|0_._165<sup>_∗∗_</sup>|**0**_._**158**<sup>_∗∗_</sup>|0_._593<sup>_∗_</sup>|0_._243<sup>_∗∗_</sup>|0_._254<sup>_∗∗_</sup>|0_._227<sup>_∗∗_</sup>|0_._368<sup>_∗∗_</sup>|
|JPN|0_._255<sup>_∗∗_</sup>|0.989|0.913|0_._236<sup>_∗∗_</sup>|0.702|0_._230<sup>_∗∗_</sup>|**0**_._**228**<sup>_∗∗_</sup>|0_._347<sup>_∗∗_</sup>|0_._347<sup>_∗∗_</sup>|
|SWE|0_._402<sup>_∗∗_</sup>|0_._758<sup>_∗_</sup>|0_._466<sup>_∗∗_</sup>|0_._542<sup>_∗_</sup>|0_._716<sup>_∗_</sup>|**0**_._**271**<sup>_∗∗_</sup>|0_._431<sup>_∗∗_</sup>|0_._350<sup>_∗∗_</sup>|0_._459<sup>_∗∗_</sup>|
|USA|0.935|1.389|0_._633<sup>_∗_</sup>|1.016|0_._712<sup>_∗_</sup>|0_._645<sup>_∗_</sup>|0_._695<sup>_∗_</sup>|0.745|**0**_._**577**<sup>_∗_</sup>|
|ZAF|**0**_._**248**<sup>_∗∗_</sup>|1.387|1.066|1.104|1.624|0_._330<sup>_∗∗_</sup>|0_._334<sup>_∗∗_</sup>|0_._291<sup>_∗∗_</sup>|0_._334<sup>_∗∗_</sup>|
|Avg|0.416|1.547|1.262|0.515|0.685|**0.375**|0.378|0.384|0.391|



Note: This table shows the relative MSFE of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the lowest relative MSFE for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 4: Two step ahead relative MSFE of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|1.055|1.132|1.144|0.907|1.131|0.897|**0.894**|0.977|1.255|
|NLD|0_._248<sup>_∗∗_</sup>|0_._267<sup>_∗∗_</sup>|0_._197<sup>_∗∗_</sup>|0_._089<sup>_∗∗∗_</sup>|0_._285<sup>_∗∗_</sup>|0_._087<sup>_∗∗∗_</sup>|0_._085<sup>_∗∗∗_</sup>|0_._088<sup>_∗∗∗_</sup>|**0**_._**050**<sup>_∗∗∗_</sup>|
|CAN|**0**_._**597**<sup>_∗_</sup>|2.625|1.153|0.990|0.932|0.949|0.955|0_._769<sup>_∗_</sup>|1.263|
|CHE|**0**_._**141**<sup>_∗∗_</sup>|0_._301<sup>_∗_</sup>|0_._295<sup>_∗_</sup>|0_._180<sup>_∗∗_</sup>|0.875|0_._183<sup>_∗∗_</sup>|0_._186<sup>_∗∗_</sup>|0_._143<sup>_∗∗_</sup>|0_._153<sup>_∗∗_</sup>|
|DEU|2.963|2.766|2.700|3.214|3.728|2.056|2.110|2.205|**0.887**|
|DNK|**0**_._**237**<sup>_∗_</sup>|0_._503<sup>_∗_</sup>|0_._340<sup>_∗_</sup>|0_._326<sup>_∗_</sup>|0_._575<sup>_∗_</sup>|0_._309<sup>_∗_</sup>|0_._317<sup>_∗_</sup>|0_._299<sup>_∗_</sup>|0_._417<sup>_∗_</sup>|
|ESP|0.890|0_._574<sup>_∗_</sup>|0_._642<sup>_∗_</sup>|0_._107<sup>_∗∗_</sup>|0_._615<sup>_∗_</sup>|0_._152<sup>_∗∗_</sup>|0_._094<sup>_∗∗∗_</sup>|0_._177<sup>_∗∗_</sup>|**0**_._**028**<sup>_∗∗∗_</sup>|
|FIN|**0**_._**130**<sup>_∗∗_</sup>|1.748|0_._467<sup>_∗_</sup>|0_._200<sup>_∗_</sup>|0_._514<sup>_∗_</sup>|0_._138<sup>_∗∗_</sup>|0_._163<sup>_∗∗_</sup>|0_._262<sup>_∗∗_</sup>|0_._152<sup>_∗∗_</sup>|
|FRA|0_._606<sup>_∗_</sup>|9.590|1.840|0_._748<sup>_∗_</sup>|1.263|**0**_._**429**<sup>_∗∗_</sup>|**0**_._**429**<sup>_∗∗_</sup>|0_._601<sup>_∗_</sup>|0_._500<sup>_∗_</sup>|
|GBR|1.874|6.453|1.512|0.923|1.132|0.830|**0**_._**811**<sup>_∗_</sup>|1.010|0.895|
|IRL|0_._069<sup>_∗∗∗_</sup>|0_._067<sup>_∗∗∗_</sup>|0_._060<sup>_∗∗∗_</sup>|**0**_._**042**<sup>_∗∗∗_</sup>|0_._101<sup>_∗∗_</sup>|0_._052<sup>_∗∗∗_</sup>|0_._080<sup>_∗∗∗_</sup>|0_._293<sup>_∗∗_</sup>|0_._066<sup>_∗∗∗_</sup>|
|ITA|0_._252<sup>_∗∗_</sup>|0_._665<sup>_∗_</sup>|0_._560<sup>_∗_</sup>|0_._301<sup>_∗∗_</sup>|0_._730<sup>_∗_</sup>|0_._265<sup>_∗∗_</sup>|0_._262<sup>_∗∗_</sup>|**0**_._**144**<sup>_∗∗_</sup>|0_._416<sup>_∗_</sup>|
|JPN|2.532|1.794|1.865|1.999|1.995|1.767|**1.584**|3.875|1.929|
|SWE|0_._247<sup>_∗∗_</sup>|0_._617<sup>_∗_</sup>|0_._334<sup>_∗∗_</sup>|0_._317<sup>_∗∗_</sup>|0_._478<sup>_∗_</sup>|**0**_._**196**<sup>_∗∗_</sup>|0_._250<sup>_∗∗_</sup>|0_._226<sup>_∗∗_</sup>|0_._483<sup>_∗_</sup>|
|USA|1.339|2.318|**0**_._**625**<sup>_∗_</sup>|1.758|1.238|1.288|1.237|1.075|1.217|
|ZAF|0.930|1.286|1.184|1.376|1.559|0.869|0.870|**0**_._**765**<sup>_∗_</sup>|0.926|
|Avg|0.882|2.044|0.932|0.837|1.072|0.654|**0.645**|0.826|0.665|



Note: This table shows the relative MSFE of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the lowest relative MSFE for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

22 

Table 5: Three step ahead relative MSFE of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|1.156|1.249|1.082|**0.929**|1.119|0.993|0.957|1.093|1.691|
|NLD|0_._164<sup>_∗∗_</sup>|0_._156<sup>_∗∗_</sup>|0_._172<sup>_∗∗_</sup>|0_._107<sup>_∗∗∗∗_</sup>|0_._553<sup>_∗_</sup>|0_._100<sup>_∗∗∗_</sup>|**0**_._**096**<sup>_∗∗∗_</sup>|0_._105<sup>_∗∗_</sup>|0_._054<sup>_∗∗∗_</sup>|
|CAN|0_._690<sup>_∗_</sup>|1.531|0.911|0_._782<sup>_∗_</sup>|1.142|0_._797<sup>_∗_</sup>|0_._802<sup>_∗_</sup>|**0**_._**685**<sup>_∗_</sup>|0_._744<sup>_∗_</sup>|
|CHE|0_._173<sup>_∗∗_</sup>|0_._232<sup>_∗∗_</sup>|0_._219<sup>_∗∗_</sup>|0_._178<sup>_∗∗∗_</sup>|0_._289<sup>_∗∗_</sup>|0_._157<sup>_∗∗_</sup>|0_._158<sup>_∗∗_</sup>|**0**_._**147**<sup>_∗∗_</sup>|0_._174<sup>_∗∗_</sup>|
|DEU|0.804|0_._644<sup>_∗_</sup>|0_._747<sup>_∗_</sup>|0.865|1.279|0.860|0_._682<sup>_∗_</sup>|0_._696<sup>_∗_</sup>|**0**_._**132**<sup>_∗∗_</sup>|
|DNK|**0**_._**242**<sup>_∗∗_</sup>|0_._331<sup>_∗∗_</sup>|0_._351<sup>_∗∗_</sup>|0_._264<sup>_∗∗_</sup>|0_._278<sup>_∗∗_</sup>|0_._271<sup>_∗∗_</sup>|0_._258<sup>_∗∗_</sup>|0_._285<sup>_∗∗_</sup>|0_._445<sup>_∗∗_</sup>|
|ESP|1.717|0_._253<sup>_∗∗_</sup>|0_._211<sup>_∗∗_</sup>|**0**_._**099**<sup>_∗∗∗_</sup>|0_._309<sup>_∗_</sup>|0_._264<sup>_∗_</sup>|0_._171<sup>_∗∗_</sup>|0_._257<sup>_∗_</sup>|0_._112<sup>_∗∗_</sup>|
|FIN|**0**_._**033**<sup>_∗∗∗_</sup>|0_._560<sup>_∗_</sup>|0_._174<sup>_∗∗_</sup>|0_._064<sup>_∗∗∗_</sup>|0_._182<sup>_∗∗_</sup>|0_._052<sup>_∗∗∗_</sup>|0_._059<sup>_∗∗∗_</sup>|0_._098<sup>_∗∗∗_</sup>|0_._063<sup>_∗∗∗_</sup>|
|FRA|0_._734<sup>_∗_</sup>|6.347|1.176|0_._685<sup>_∗_</sup>|0_._754<sup>_∗_</sup>|**0**_._**420**<sup>_∗∗_</sup>|0_._425<sup>_∗∗_</sup>|0_._470<sup>_∗∗_</sup>|0_._444<sup>_∗∗_</sup>|
|GBR|2.561|3.122|1.794|1.179|1.281|1.078|1.087|**0.963**|1.393|
|IRL|0_._053<sup>_∗∗∗_</sup>|0_._070<sup>_∗∗∗_</sup>|0_._040<sup>_∗∗∗_</sup>|**0**_._**034**<sup>_∗∗∗_</sup>|0_._153<sup>_∗∗_</sup>|0_._050<sup>_∗∗∗_</sup>|0_._075<sup>_∗∗∗_</sup>|0_._273<sup>_∗∗_</sup>|0_._087<sup>_∗∗∗_</sup>|
|ITA|0_._126<sup>_∗∗_</sup>|0_._359<sup>_∗_</sup>|0_._335<sup>_∗_</sup>|0_._164<sup>_∗∗_</sup>|0_._345<sup>_∗_</sup>|**0**_._**110**<sup>_∗∗_</sup>|0_._111<sup>_∗∗_</sup>|0_._115<sup>_∗∗_</sup>|0_._167<sup>_∗∗_</sup>|
|JPN|0_._720<sup>_∗_</sup>|0.828|0_._698<sup>_∗_</sup>|0.760|0.848|0_._652<sup>_∗_</sup>|**0**_._**641**<sup>_∗_</sup>|1.401|0.750|
|SWE|**0**_._**513**<sup>_∗_</sup>|1.460|1.161|0.750|0.947|0_._657<sup>_∗_</sup>|0_._716<sup>_∗_</sup>|0_._707<sup>_∗_</sup>|1.360|
|USA|2.172|3.039|1.884|3.172|2.924|2.377|2.148|1.846|**1.578**|
|ZAF|1.087|1.250|0.889|0.963|0.972|0.865|0.865|0_._768<sup>_∗_</sup>|**0**_._**662**<sup>_∗_</sup>|
|Avg|0.809|1.339|0.740|0.687|0.836|0.635|**0.578**|0.619|0.616|



Note: This table shows the relative MSFE of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the lowest relative MSFE for a country. The last row shows the average per model of all the countries. 

Table 6: Four step ahead relative MSFE of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|1.575|1.761|1.604|**1.539**|1.417|1.557|1.542|1.583|2.623|
|NLD|0_._130<sup>_∗∗_</sup>|0_._191<sup>_∗∗_</sup>|0_._144<sup>_∗∗_</sup>|0_._126<sup>_∗∗_</sup>|0_._487<sup>_∗_</sup>|0_._128<sup>_∗∗_</sup>|0_._124<sup>_∗∗_</sup>|0_._134<sup>_∗∗_</sup>|**0**_._**093**<sup>_∗_</sup>|
|CAN|0.975|1.933|1.127|1.207|1.239|1.139|1.156|**0.953**|1.043|
|CHE|0_._175<sup>_∗∗_</sup>|0_._190<sup>_∗∗_</sup>|0_._219<sup>_∗∗_</sup>|0_._205<sup>_∗∗_</sup>|0_._279<sup>_∗∗_</sup>|0_._185<sup>_∗∗_</sup>|0_._185<sup>_∗∗_</sup>|0_._171<sup>_∗∗_</sup>|**0**_._**116**<sup>_∗∗_</sup>|
|DEU|1.273|1.266|1.241|1.356|1.653|0.924|1.187|1.121|**0**_._**440**<sup>_∗_</sup>|
|DNK|**0**_._**365**<sup>_∗∗_</sup>|0_._398<sup>_∗∗_</sup>|0_._371<sup>_∗∗_</sup>|0_._378<sup>_∗∗_</sup>|0_._512<sup>_∗_</sup>|0_._379<sup>_∗∗_</sup>|0_._371<sup>_∗∗_</sup>|0_._404<sup>_∗_</sup>|0_._679<sup>_∗_</sup>|
|ESP|0.775|0_._218<sup>_∗∗_</sup>|0_._171<sup>_∗∗_</sup>|0_._137<sup>_∗∗_</sup>|0_._388<sup>_∗_</sup>|0_._413<sup>_∗_</sup>|**0**_._**123**<sup>_∗∗_</sup>|0_._361<sup>_∗_</sup>|0_._143<sup>_∗∗_</sup>|
|FIN|**0**_._**058**<sup>_∗∗∗_</sup>|0_._698<sup>_∗_</sup>|0_._142<sup>_∗∗_</sup>|0_._113<sup>_∗∗∗_</sup>|0_._275<sup>_∗∗_</sup>|0_._078<sup>_∗∗∗_</sup>|0_._084<sup>_∗∗∗_</sup>|0_._142<sup>_∗∗_</sup>|0_._129<sup>_∗∗_</sup>|
|FRA|0_._414<sup>_∗_</sup>|2.267|0_._337<sup>_∗_</sup>|0_._437<sup>_∗_</sup>|0.820|**0**_._**225**<sup>_∗∗_</sup>|0_._226<sup>_∗∗_</sup>|0_._275<sup>_∗∗_</sup>|0_._257<sup>_∗∗_</sup>|
|GBR|1.108|0_._624<sup>_∗_</sup>|0_._670<sup>_∗_</sup>|0_._555<sup>_∗_</sup>|0.772|0_._484<sup>_∗_</sup>|0_._517<sup>_∗_</sup>|**0**_._**458**<sup>_∗_</sup>|0_._646<sup>_∗_</sup>|
|IRL|0_._068<sup>_∗∗∗_</sup>|0_._083<sup>_∗∗∗_</sup>|0_._062<sup>_∗∗∗_</sup>|0_._048<sup>_∗∗∗_</sup>|0_._074<sup>_∗∗∗_</sup>|**0**_._**061**<sup>_∗∗∗_</sup>|0_._071<sup>_∗∗∗_</sup>|0_._247<sup>_∗∗_</sup>|0_._140<sup>_∗∗_</sup>|
|ITA|0_._110<sup>_∗∗∗_</sup>|0_._297<sup>_∗∗_</sup>|0_._236<sup>_∗∗_</sup>|0_._108<sup>_∗∗∗_</sup>|0_._480<sup>_∗_</sup>|**0**_._**103**<sup>_∗∗∗_</sup>|**0**_._**103**<sup>_∗∗∗_</sup>|0_._114<sup>_∗∗∗_</sup>|0_._215<sup>_∗∗_</sup>|
|JPN|0.866|1.037|0.880|0.818|0.943|0.838|0.832|1.343|**0**_._**764**<sup>_∗_</sup>|
|SWE|1.219|1.696|**1.550**|1.551|1.519|1.198|1.320|1.324|2.656|
|USA|1.098|1.372|1.058|1.464|1.690|1.225|1.134|0.931|**0.857**|
|ZAF|1.006|1.333|1.016|0.893|1.136|0.875|0.878|0.727|**0**_._**302**<sup>_∗∗_</sup>|
|Avg|0.701|0.960|0.677|0.683|0.855|**0.613**|0.616|0.643|0.694|



Note: This table shows the relative MSFE of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the lowest relative MSFE for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 3 to 6 show the Mean squared forecast errors of the models with lag length 1 and including the macroeconomic variables relative to an unrestricted PVAR model. An asterisk (*) means that the model scores significantly better than the benchmark model. A few things stand out. 

23 

First, we see that most models score significantly better than the benchmark unrestricted PVAR model for most countries. However, the relative MFSE has to be quite a bit lower than we are used to, to get a significant effect. This is due to the fact that the amount of forecasts is really small, meaning that the variance of the difference between the forecast errors can become high. This means that the forecasts have to be better by a large margin to account for the variance. 

For the one step ahead forecast, we can see that the BFCS scores the best from all the Bayesian models. This is also due to large forecast errors for France and the United Kingdom for the SSSS models. This means that for those countries the SSSS models are largely misspecified, which probably is due to the fact that the SSSS cannot set coefficients to zero, but only close to zero. 

Furthermore, we see that the MSFE are more similar to each other for the LASSO models. For some countries, for example the Netherlands and Switzerland, the LASSO1 (where we set penalties for _γk_ , _c_ and _α_ ) comes out on top, where for Canada and Japan the LASSO2 (where we set penalties for _γk_ , _c_ , _α_ and we set the Covariance matrix Σ to the identity matrix) gets a better score. The LASSO3, where we also search for homogeneity is the only model with a relative MSFE smaller than 1 for Australia. 

Also, we see that the GVAR model scores pretty competitively compared to the Bayesian and LASSO models. Sometimes the GVAR model even has the best relative MSFE (for example for Ireland and South Africa). This result is not in line with the literature, which report that the Bayesian VAR models score better than the GVAR model (Koop and Korobilis (2019), Feldkircher et al. (2020)) and the results in Camehl (2022), which reports that the LASSO PVAR scores better than the GVAR models. Also, Camehl (2022) reports that the LASSO PVAR scores better than the Bayesian methods in that paper, which is on average in line with our results. For some of the countries, the Bayesian methods perform better. However, we have to note that we are testing different Bayesian methods than the methods in that research. 

Lastly, if we compare the PVAR methods to the random walk model, we conclude that for some countries the additional information of other countries variables yields better forecasts than only the information of the country itself (which is the RW model). However, this also means that some countries do not gain accuracy by adding information of other countries. This is true for Germany, Spain and the United States. For Germany and the United States we can explain this due to the fact that these two countries are the most important economies in their region and also the world. So it is likely that information from those countries spill over to the smaller economies in the dataset and not vice versa. The multi step ahead forecasts show pretty similar results to the one step ahead forecasts, with a few exceptions. For example, not a single model outperforms the unrestricted PVAR model for the 2 step ahead forecast for Japan and Germany. This also holds for the 3 step ahead forecast of the United States and the 4 step ahead forecasts of Australia 

24 

and Sweden. Furthermore, it turns out that the benchmark model is harder to beat for multi step ahead forecasts. Nevertheless, the models keep outperforming the benchmark model for most of the countries, meaning the reducing the amount of parameters results in a forecast gain. 

Table 7: One step ahead average difference of Log-Scores of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|-1.74|-0.91|-0.01|-1.20|-0.68|-0.42|-0.44|-0.06|**0.03**|
|NLD|4_._71<sup>_∗∗∗_</sup>|1_._84<sup>_∗_</sup>|2_._58<sup>_∗∗_</sup>|3_._00<sup>_∗∗_</sup>|1_._92<sup>_∗_</sup>|4_._88<sup>_∗∗_</sup>|**4**_._**89**<sup>_∗∗∗_</sup>|4_._83<sup>_∗∗∗_</sup>|4_._27<sup>_∗∗∗_</sup>|
|CAN|0.47|0.23|1_._05<sup>_∗∗_</sup>|**1**_._**15**<sup>_∗∗_</sup>|0.24|0_._85<sup>_∗∗∗_</sup>|0_._94<sup>_∗∗∗_</sup>|0_._85<sup>_∗∗∗_</sup>|0_._84<sup>_∗∗_</sup>|
|CHE|0.66|-0.65|0_._53<sup>_∗_</sup>|0_._53<sup>_∗∗_</sup>|-0.67|0_._71<sup>_∗∗∗_</sup>|0_._70<sup>_∗∗∗_</sup>|**0**_._**76**<sup>_∗∗∗_</sup>|0_._45<sup>_∗_</sup>|
|DEU|0.33|-0.57|-0.28|-0.01|-0.21|0.33|0.21|**0.54**|0.49|
|DNK|8_._88<sup>_∗_</sup>|8_._01<sup>_∗_</sup>|0.71|**9**_._**58**<sup>_∗_</sup>|9_._07<sup>_∗_</sup>|8_._91<sup>_∗_</sup>|8_._72<sup>_∗_</sup>|8_._75<sup>_∗_</sup>|4_._85<sup>_∗_</sup>|
|ESP|1_._08<sup>_∗_</sup>|-0.33|1_._01<sup>_∗_</sup>|-1.22|0.15|2_._93<sup>_∗_</sup>|2_._67<sup>_∗_</sup>|**2**_._**97**<sup>_∗_</sup>|2_._57<sup>_∗_</sup>|
|FIN|2_._04<sup>_∗_</sup>|-0.66|0_._80<sup>_∗_</sup>|1_._31<sup>_∗_</sup>|-0.28|**2**_._**15**<sup>_∗_</sup>|2_._09<sup>_∗_</sup>|2_._08<sup>_∗_</sup>|1_._91<sup>_∗_</sup>|
|FRA|**0**_._**37**<sup>_∗_</sup>|-1.75|-0.94|0.08|-1.32|0_._32<sup>_∗_</sup>|0_._28<sup>_∗_</sup>|0_._24<sup>_∗_</sup>|0.01|
|GBR|0.06|-1.28|-0.28|0_._48<sup>_∗_</sup>|-0.63|**0**_._**40**<sup>_∗_</sup>|0_._38<sup>_∗_</sup>|0.04|0.22|
|IRL|1_._92<sup>_∗_</sup>|-0.12|1_._18<sup>_∗_</sup>|1_._12<sup>_∗_</sup>|0.11|1_._83<sup>_∗_</sup>|1_._88<sup>_∗_</sup>|1_._78<sup>_∗_</sup>|**2**_._**78**<sup>_∗∗_</sup>|
|ITA|-2.57|5_._05<sup>_∗_</sup>|6_._21<sup>_∗_</sup>|**6**_._**40**<sup>_∗_</sup>|5_._14<sup>_∗_</sup>|0.39|-0.09|4_._22<sup>_∗_</sup>|-1.28|
|JPN|3_._92<sup>_∗_</sup>|2_._68<sup>_∗_</sup>|3_._30<sup>_∗_</sup>|5_._02<sup>_∗_</sup>|4_._04<sup>_∗_</sup>|3_._87<sup>_∗_</sup>|3_._97<sup>_∗_</sup>|3_._75<sup>_∗_</sup>|**12**_._**46**<sup>_∗∗_</sup>|
|SWE|-1.54|-1.25|-0.33|0.11|-1.09|0_._52<sup>_∗_</sup>|0.10|**0**_._**59**<sup>_∗_</sup>|0.37|
|USA|-0.32|0.07|**2**_._**31**<sup>_∗_</sup>|-2.17|0.51|-0.60|-0.83|-0.17|1_._24<sup>_∗_</sup>|
|ZAF|0_._66<sup>_∗_</sup>|-0.69|0.15|0.22|-0.75|0.49|0_._49<sup>_∗_</sup>|**0**_._**67**<sup>_∗_</sup>|0.53|
|Avg|1.18|0.60|1.12|1.53|0.97|1.72|1.62|**1.99**|1.98|



Note: This table shows the average difference of Log-Scores of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the highest average difference for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 8: Two step ahead average difference of Log-Scores of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|-5.53|0.65|0.45|0.64|**0.83**|-2.13|0.01|0.43|-2.37|
|NLD|7_._20<sup>_∗∗_</sup>|3_._72<sup>_∗_</sup>|4_._64<sup>_∗_</sup>|4_._78<sup>_∗_</sup>|3_._22<sup>_∗_</sup>|7_._50<sup>_∗∗_</sup>|7_._52<sup>_∗∗_</sup>|7_._36<sup>_∗∗_</sup>|**9**_._**89**<sup>_∗_</sup>|
|CAN|**0.11**|-1.01|0.08|**0.11**|-0.89|-0.01|0.00|0.10|-0.03|
|CHE|1_._07<sup>_∗_</sup>|0.61|**1**_._**80**<sup>_∗_</sup>|1_._76<sup>_∗_</sup>|0.22|0_._96<sup>_∗_</sup>|0_._96<sup>_∗_</sup>|1_._10<sup>_∗_</sup>|1_._30<sup>_∗_</sup>|
|DEU|-0.54|-0.78|-0.47|-0.47|-1.22|-1.01|-0.38|-0.62|**0.09**|
|DNK|4_._89<sup>_∗_</sup>|5_._95<sup>_∗_</sup>|7_._04<sup>_∗_</sup>|6_._61<sup>_∗_</sup>|6_._14<sup>_∗_</sup>|4_._77<sup>_∗_</sup>|5_._27<sup>_∗_</sup>|5_._46<sup>_∗_</sup>|**6**_._**06**<sup>_∗_</sup>|
|ESP|-0.21|4_._04<sup>_∗_</sup>|5_._49<sup>_∗_</sup>|3_._15<sup>_∗_</sup>|4_._11<sup>_∗_</sup>|2_._09<sup>_∗_</sup>|1_._88<sup>_∗_</sup>|2_._07<sup>_∗_</sup>|**6**_._**24**<sup>_∗_</sup>|
|FIN|0_._61<sup>_∗_</sup>|-0.44|1_._30<sup>_∗_</sup>|**1**_._**53**<sup>_∗_</sup>|-0.49|0_._64<sup>_∗∗_</sup>|0_._60<sup>_∗∗_</sup>|0_._61<sup>_∗∗_</sup>|0_._94<sup>_∗_</sup>|
|FRA|0.38|-1.67|-0.14|0.26|-1.67|0_._42<sup>_∗_</sup>|**0**_._**43**<sup>_∗_</sup>|0.35|0.16|
|GBR|0.00|-1.57|0.10|0.10|-1.48|-0.07|0.10|-0.32|**0.26**|
|IRL|6_._06<sup>_∗_</sup>|4_._94<sup>_∗_</sup>|6_._53<sup>_∗_</sup>|**6**_._**56**<sup>_∗_</sup>|5_._26<sup>_∗_</sup>|6_._11<sup>_∗_</sup>|6_._17<sup>_∗_</sup>|0.76|5_._99<sup>_∗_</sup>|
|ITA|3_._58<sup>_∗_</sup>|-0.02|0.00|1_._68<sup>_∗_</sup>|-0.09|3_._52<sup>_∗_</sup>|3_._38<sup>_∗_</sup>|**4**_._**85**<sup>_∗_</sup>|2_._74<sup>_∗_</sup>|
|JPN|**0.19**|-1.42|-0.35|-0.37|-1.68|-0.21|-0.21|-1.08|-10.70|
|SWE|1.02|-0.66|0.94|0.93|-0.90|1_._10<sup>_∗_</sup>|1_._12<sup>_∗_</sup>|**1**_._**15**<sup>_∗_</sup>|0.56|
|USA|-5.67|-0.40|-0.81|-9.45|-0.79|-2.86|-2.93|-1.74|-1.76|
|ZAF|**0.20**|-1.19|0.02|-0.03|-1.29|0.15|0.13|0.12|0.09|
|Avg|0.84|0.67|**1.66**|1.11|0.58|1.31|1.50|1.29|1.22|



Note: This table shows the average difference of Log-Scores of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the highest average difference for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

25 

Table 9: Three step ahead average difference of Log-Scores of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|-9.46|0.45|-1.01|0.44|**0.82**|-2.49|-1.16|0.05|-4.26|
|NLD|8_._65<sup>_∗_</sup>|10_._19<sup>_∗_</sup>|11_._27<sup>_∗_</sup>|11_._23<sup>_∗_</sup>|9_._81<sup>_∗_</sup>|**12**_._**58**<sup>_∗∗_</sup>|12_._33<sup>_∗∗_</sup>|12_._37<sup>_∗∗_</sup>|12_._42<sup>_∗∗_</sup>|
|CAN|**0.23**|-0.71|-0.11|-0.09|-0.87|0.05|0.02|0.18|-0.11|
|CHE|1.42|0.79|**1**_._**99**<sup>_∗∗_</sup>|1_._96<sup>_∗∗_</sup>|0.36|1_._36<sup>_∗_</sup>|1_._38<sup>_∗_</sup>|1_._51<sup>_∗_</sup>|1.11|
|DEU|0.13|0.35|0.69|0.62|0.02|-3.90|0.25|0.08|**1**_._**63**<sup>_∗_</sup>|
|DNK|7_._19<sup>_∗_</sup>|7_._16<sup>_∗_</sup>|7_._82<sup>_∗_</sup>|**7**_._**86**<sup>_∗_</sup>|7_._20<sup>_∗_</sup>|6_._24<sup>_∗_</sup>|6_._91<sup>_∗_</sup>|6_._92<sup>_∗_</sup>|**6**_._**23**<sup>_∗_</sup>|
|ESP|-5.18|0.24|2_._11<sup>_∗_</sup>|1_._42<sup>_∗_</sup>|0.32|2_._25<sup>_∗_</sup>|1_._95<sup>_∗_</sup>|2_._24<sup>_∗_</sup>|**6**_._**32**<sup>_∗_</sup>|
|FIN|**4**_._**10**<sup>_∗_</sup>|1.25|3_._09<sup>_∗_</sup>|3_._12<sup>_∗_</sup>|1.07|4_._16<sup>_∗∗_</sup>|**4**_._**17**<sup>_∗∗_</sup>|4.05|3.60|
|FRA|0.28|-1.73|0.10|0.24|-1.83|0_._35<sup>_∗_</sup>|0_._35<sup>_∗_</sup>|0_._33<sup>_∗_</sup>|**0**_._**42**<sup>_∗_</sup>|
|GBR|-3.01|-1.52|-0.07|-0.04|-1.56|0.09|-0.03|**0.13**|-0.01|
|IRL|14_._13<sup>_∗_</sup>|9_._16<sup>_∗_</sup>|10_._80<sup>_∗_</sup>|10_._75<sup>_∗_</sup>|9_._43<sup>_∗_</sup>|**14**_._**21**<sup>_∗_</sup>|14_._15<sup>_∗_</sup>|4_._18<sup>_∗_</sup>|7_._74<sup>_∗_</sup>|
|ITA|5_._52<sup>_∗_</sup>|7_._55<sup>_∗_</sup>|8_._52<sup>_∗_</sup>|**9**_._**18**<sup>_∗_</sup>|7_._39<sup>_∗_</sup>|5_._64<sup>_∗_</sup>|5_._42<sup>_∗_</sup>|3_._99<sup>_∗_</sup>|8_._94<sup>_∗_</sup>|
|JPN|-2.08|0.29|**1.29**|1.08|-0.18|0.36|0.41|-3.82|-1.80|
|SWE|-0.07|-0.85|0.31|0.49|-1.41|0.00|0.03|0.08|0.12|
|USA|-50.16|**-0.13**|-1.07|-10.78|-0.63|-59.36|-45.11|-43.9|-1.12|
|ZAF|0.22|-1.29|0.08|-0.35|-1.41|-0.02|-0.03|0.13|**0.23**|
|Avg|-1.76|1.95|**2.86**|2.32|1.78|-1.16|0.07|-0.72|2.59|



Note: This table shows the average difference of Log-Scores of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the highest average difference for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 10: Four step ahead average difference of Log-Scores of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|-7.23|-0.15|-1.00|-1.26|**-0.27**|-5.30|-3.87|-0.70|-27.86|
|NLD|10_._23<sup>_∗_</sup>|19_._02<sup>_∗_</sup>|**19**_._**74**<sup>_∗_</sup>|19_._64<sup>_∗_</sup>|18_._62<sup>_∗_</sup>|14_._30<sup>_∗_</sup>|12_._66<sup>_∗_</sup>|14_._87<sup>_∗_</sup>|17_._94<sup>_∗_</sup>|
|CAN|**0.04**|-0.81|-0.12|-0.20|-0.89|-0.02|-0.03|**0.04**|-0.41|
|CHE|2.40|1.86|**2**_._**98**<sup>_∗_</sup>|2_._93<sup>_∗_</sup>|1.57|2_._36<sup>_∗_</sup>|2_._39<sup>_∗_</sup>|2_._50<sup>_∗_</sup>|2_._15<sup>_∗_</sup>|
|DEU|-0.52|-0.44|-0.28|-0.47|-0.80|-0.41|-1.28|-0.66|**0.16**|
|DNK|1.53|1.44|**2**_._**76**<sup>_∗_</sup>|2_._43<sup>_∗_</sup>|1.54|1_._34<sup>_∗_</sup>|1_._84<sup>_∗_</sup>|1_._56<sup>_∗_</sup>|0.46|
|ESP|-2.59|0.89|2_._76<sup>_∗_</sup>|2_._56<sup>_∗_</sup>|1.03|2.21|**5**_._**90**<sup>_∗_</sup>|2.90|4.03|
|FIN|2_._41<sup>_∗_</sup>|0.42|2_._41<sup>_∗_</sup>|2_._38<sup>_∗_</sup>|0.35|2_._52<sup>_∗_</sup>|**2**_._**59**<sup>_∗_</sup>|2_._41<sup>_∗_</sup>|2.07|
|FRA|-0.78|-0.89|0_._83<sup>_∗∗_</sup>|0_._87<sup>_∗∗_</sup>|-1.22|0_._87<sup>_∗∗_</sup>|0_._85<sup>_∗∗_</sup>|0_._64<sup>_∗_</sup>|**0**_._**99**<sup>_∗∗_</sup>|
|GBR|-0.26|-1.24|0.28|0.36|-1.29|0_._40<sup>_∗_</sup>|0_._26<sup>_∗_</sup>|**0**_._**48**<sup>_∗_</sup>|0.22|
|IRL|10.96|11.30|**12**_._**80**<sup>_∗_</sup>|12_._75<sup>_∗_</sup>|11.53|11.03|11.07|3.46|9.09|
|ITA|10.60|50_._22<sup>_∗_</sup>|51_._39<sup>_∗_</sup>|**51**_._**81**<sup>_∗_</sup>|49_._95<sup>_∗_</sup>|10.32|10.07|8.32|11.49|
|JPN|-2.64|-0.17|-0.16|-0.59|-0.46|-0.34|**0.19**|-2.03|-3.91|
|SWE|-0.09|-1.60|-0.07|-0.17|-1.98|**-0.05**|-0.23|-0.31|-0.42|
|USA|-1.02|0.06|0.16|-1.03|0.51|-1.27|-5.31|-1.12|**0.49**|
|ZAF|0.21|-1.26|0.00|-0.17|-1.33|0.07|0.05|0.29|**0.87**|
|Avg|1.45|4.92|**5.91**|5.74|4.80|2.38|2.32|2.04|1.09|



Note: This table shows the average difference of Log-Scores of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the highest average difference for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 7 to 10 show the average difference of Log-Scores of the models with lag length 1 and including the macroeconomic variables relative to an unrestricted PVAR model. An asterisk (*) means that the model scores significantly better than the benchmark model. 

26 

As with the MSFE metric and test, we see that the difference has to be quite high in some cases to get a significant improvement. This is again due to the low amount of forecasts. When we compare the density forecasts to the point forecasts, we see that the significance levels of the density forecasts are on average lower than the point forecasts. The models mostly still outperform the benchmark model. Furthermore, we see many similarities with the point forecasts. For example, we see that the BFCS model scores the best out of the Bayesian models and that the LASSO models are competitive to one another. Also, the GVAR models scores better than what can be expected according to the literature. 

One thing that also stands out, is that the LASSO models sometimes have a higher significance level, while the Bayesian methods have a better Log-Score. See for example Canada in the one step ahead density forecast (table 7). This means that the LASSO methods have a lower variance in the test statistic and therefore score more consistently. 

#### **4.1.2 Models with multiple lags** 

Table 11: One step ahead relative MSFE of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|0.900|0.913|0.810|1.492|1.157|0_._917<sup>_∗_</sup>|0.911|**0**_._**777**<sup>_∗_</sup>|0.870|
|NLD|0.915|0_._542<sup>_∗_</sup>|0.812|1.049|0_._534<sup>_∗∗_</sup>|0_._464<sup>_∗∗_</sup>|0_._489<sup>_∗∗_</sup>|**0**_._**404**<sup>_∗∗_</sup>|0.706|
|CAN|1.095|0.944|1.286|1.106|1.017|0_._669<sup>_∗_</sup>|**0**_._**647**<sup>_∗_</sup>|0.959|0.913|
|CHE|0_._751<sup>_∗∗_</sup>|0.865|0.904|1.553|0.787|1.017|0.928|**0.717**|1.174|
|DEU|1.206|**0.860**|2.391|14.073|3.576|1.499|1.472|1.377|1.383|
|DNK|0.903|0.961|1.036|1.057|1.23|1.230|1.083|**0.745**|0.801|
|ESP|1.120|1.152|1.469|**0**_._**354**<sup>_∗∗_</sup>|1.385|0_._478<sup>_∗∗_</sup>|0.565|0.539|0.671|
|FIN|1.092|0_._367<sup>_∗∗_</sup>|0_._285<sup>_∗∗_</sup>|0_._590<sup>_∗_</sup>|**0**_._**280**<sup>_∗∗_</sup>|0_._613<sup>_∗_</sup>|0_._408<sup>_∗∗_</sup>|0_._288<sup>_∗∗_</sup>|0_._352<sup>_∗∗_</sup>|
|FRA|0.795|1.204|1.129|1.086|2.916|0.809|**0**_._**663**<sup>_∗_</sup>|0.933|1.223|
|GBR|0.880|0_._418<sup>_∗_</sup>|0_._468<sup>_∗_</sup>|0_._528<sup>_∗_</sup>|0_._411<sup>_∗_</sup>|0.755|0_._497<sup>_∗_</sup>|**0**_._**359**<sup>_∗∗_</sup>|0_._384<sup>_∗∗_</sup>|
|IRL|0_._574<sup>_∗∗_</sup>|1.380|2.844|1.820|2.493|**0**_._**475**<sup>_∗_</sup>|0.808|1.048|1.302|
|ITA|1.030|0.707|0.779|**0**_._**472**<sup>_∗∗_</sup>|1.232|0_._626<sup>_∗_</sup>|0_._599<sup>_∗_</sup>|0.840|0.971|
|JPN|1.301|0_._588<sup>_∗_</sup>|0_._589<sup>_∗_</sup>|0.804|**0**_._**491**<sup>_∗∗_</sup>|0_._610<sup>_∗_</sup>|0_._579<sup>_∗_</sup>|0_._651<sup>_∗_</sup>|0.731|
|SWE|**0**_._**713**<sup>_∗_</sup>|2.003|3.417|3.009|2.866|2.411|2.379|1.831|3.264|
|USA|**0.980**|1.118|1.300|1.036|2.603|1.009|1.058|1.056|0.988|
|ZAF|1.120|**0**_._**682**<sup>_∗_</sup>|0_._708<sup>_∗_</sup>|2.931|1.409|1.108|1.173|0.876|0.953|
|Avg|0.961|0.919|1.264|2.060|1.524|0.918|0.891|**0.838**|1.043|



Note: This table shows the relative MSFE of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The last row shows the average per model over all the countries. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

27 

Table 12: Two step ahead relative MSFE of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|1.045|0.797|**0**_._**782**<sup>_∗_</sup>|0.808|0_._795<sup>_∗_</sup>|0.876|0.836|0.829|1.088|
|NLD|**0.843**|1.470|2.232|2.429|2.004|0.927|0.889|1.137|1.117|
|CAN|0.959|0.804|0.816|0.849|0_._792<sup>_∗_</sup>|0.970|0.888|**0.786**|1.090|
|CHE|**0.627**|1.612|1.822|2.943|2.146|1.512|1.594|1.472|1.436|
|DEU|1.369|**1.055**|2.176|6.974|4.126|1.369|1.438|1.513|1.260|
|DNK|0.888|0.809|**0**_._**776**<sup>_∗_</sup>|0.861|0.809|1.132|1.018|0.795|1.014|
|ESP|1.021|1.205|1.063|0.193|1.162|**0**_._**436**<sup>_∗∗_</sup>|0_._507<sup>_∗∗_</sup>|0_._483<sup>_∗∗_</sup>|0_._441<sup>_∗_</sup>|
|FIN|0.852|0_._222<sup>_∗_</sup>|0_._139<sup>_∗∗_</sup>|0_._222<sup>_∗∗_</sup>|**0**_._**130**<sup>_∗∗_</sup>|0_._615<sup>_∗_</sup>|0_._327<sup>_∗∗_</sup>|0_._141<sup>_∗∗_</sup>|0_._165<sup>_∗∗_</sup>|
|FRA|**0**_._**628**<sup>_∗_</sup>|0.934|0.757|1.183|1.155|1.136|1.030|0.752|0.747|
|GBR|0.742|0_._542<sup>_∗_</sup>|0_._531<sup>_∗_</sup>|0_._549<sup>_∗_</sup>|**0**_._**451**<sup>_∗∗_</sup>|0.891|0.781|0_._497<sup>_∗_</sup>|0_._569<sup>_∗_</sup>|
|IRL|**0**_._**371**<sup>_∗_</sup>|1.393|1.120|0.979|1.323|1.314|1.453|1.454|1.771|
|ITA|1.003|1.061|1.113|**0**_._**672**<sup>_∗_</sup>|1.503|0_._718<sup>_∗_</sup>|0_._714<sup>_∗_</sup>|0.891|1.153|
|JPN|1.222|0.920|0.961|1.366|**0.825**|1.073|1.071|1.077|1.383|
|SWE|0.800|0_._629<sup>_∗_</sup>|0_._530<sup>_∗_</sup>|0.745|**0**_._**505**<sup>_∗∗_</sup>|0.954|0.730|0.551|1.343|
|USA|**0.949**|1.090|1.171|1.179|2.315|1.043|1.121|1.194|1.218|
|ZAF|1.141|**0**_._**565**<sup>_∗_</sup>|0_._596<sup>_∗_</sup>|2.457|0.735|1.075|1.238|0.949|1.088|
|Avg|**0.904**|0.944|1.037|1.526|1.299|1.003|0.977|0.908|1.055|



Note: This table shows the relative MSFE of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The last row shows the average per model over all the countries. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 13: Three step ahead relative MSFE of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|1.052|0_._690<sup>_∗_</sup>|0_._701<sup>_∗_</sup>|0_._689<sup>_∗_</sup>|**0**_._**677**<sup>_∗_</sup>|0.877|0.847|0.876|1.244|
|NLD|1.117|0_._567<sup>_∗∗_</sup>|0_._632<sup>_∗∗_</sup>|0.842|0.812|0_._518<sup>_∗∗_</sup>|0_._495<sup>_∗∗_</sup>|0_._490<sup>_∗∗_</sup>|**0**_._**381**<sup>_∗∗_</sup>|
|CAN|1.178|1.246|1.294|1.343|1.179|1.122|**1.103**|1.177|1.18|
|CHE|**0**_._**669**<sup>_∗∗_</sup>|1.334|1.322|1.844|1.276|1.282|1.318|1.343|1.495|
|DEU|1.221|1.013|1.904|3.313|3.618|1.823|1.851|1.736|**0**_._**586**<sup>_∗_</sup>|
|DNK|0.863|0_._729<sup>_∗_</sup>|**0**_._**676**<sup>_∗_</sup>|0.820|0_._692<sup>_∗_</sup>|1.023|0.887|0_._744<sup>_∗_</sup>|1.109|
|ESP|0.834|0_._711<sup>_∗_</sup>|0_._542<sup>_∗∗_</sup>|**0**_._**149**<sup>_∗∗∗_</sup>|0_._392<sup>_∗∗_</sup>|0_._482<sup>_∗∗_</sup>|0_._416<sup>_∗∗_</sup>|0_._403<sup>_∗∗_</sup>|0_._376<sup>_∗∗_</sup>|
|FIN|0.541***|0_._366<sup>_∗∗_</sup>|0_._203<sup>_∗∗_</sup>|0_._244<sup>_∗∗_</sup>|**0**_._**200**<sup>_∗∗_</sup>|0.921|0_._551<sup>_∗_</sup>|0_._222<sup>_∗∗_</sup>|0_._247<sup>_∗∗_</sup>|
|FRA|**0**_._**654**<sup>_∗∗_</sup>|0.947|0.934|1.110|0.981|1.062|0.964|0_._744<sup>_∗_</sup>|0_._670<sup>_∗_</sup>|
|GBR|0_._626<sup>_∗_</sup>|0_._440<sup>_∗∗_</sup>|0_._426<sup>_∗∗_</sup>|0_._446<sup>_∗∗_</sup>|**0**_._**392**<sup>_∗∗_</sup>|0.828|0_._683<sup>_∗_</sup>|0_._457<sup>_∗∗_</sup>|0_._560<sup>_∗_</sup>|
|IRL|**0**_._**404**<sup>_∗∗∗_</sup>|0.936|0_._715<sup>_∗_</sup>|0_._46<sup>_∗∗_</sup>|0_._489<sup>_∗∗_</sup>|0.994|1.079|1.073|1.507|
|ITA|0.871|1.308|1.292|**0**_._**856**|1.560|0.870|0.819|0.809|1.144|
|JPN|1.291|1.009|1.021|1.368|1.004|0.924|0.943|**0.901**|1.388|
|SWE|0.857|0_._511<sup>_∗_</sup>|0_._461<sup>_∗_</sup>|0_._664<sup>_∗_</sup>|**0**_._**433**<sup>_∗_</sup>|0.955|0.752|0_._528<sup>_∗_</sup>|1.126|
|USA|**0.911**|1.127|1.402|1.352|2.560|1.108|1.180|1.215|0.979|
|ZAF|1.059|**0**_._**433**<sup>_∗∗_</sup>|**0.443**|2.573|0_._697<sup>_∗_</sup>|0_._734<sup>_∗_</sup>|0.809|0_._607<sup>_∗_</sup>|0_._591<sup>_∗_</sup>|
|Avg|0.884|**0.835**|0.873|1.130|1.060|0.970|0.919|0.833|0.911|



Note: This table shows the relative MSFE of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The last row shows the average per model of all the countries. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

28 

Table 14: Four step ahead relative MSFE of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|1.044|**0**_._**724**<sup>_∗_</sup>|0_._726<sup>_∗_</sup>|0_._779<sup>_∗_</sup>|0_._734<sup>_∗_</sup>|0.871|0.841|0.873|1.264|
|NLD|1.192|0.923|1.025|1.297|1.112|0.888|0.849|0.888|**0.788**|
|CAN|1.016|0_._763<sup>_∗_</sup>|0_._779<sup>_∗_</sup>|0.959|0.807|0.779|0_._767<sup>_∗_</sup>|0.760|**0**_._**716**<sup>_∗_</sup>|
|CHE|0.897|1.192|1.339|1.391|1.355|1.037|1.075|1.251|**0**_._**785**<sup>_∗_</sup>|
|DEU|1.148|1.269|2.671|2.112|3.154|1.796|1.907|1.956|**1.050**|
|DNK|0.900|0.795|**0**_._**729**<sup>_∗_</sup>|1.067|0.749|1.012|0.898|0.828|1.346|
|ESP|0_._528<sup>_∗∗_</sup>|0_._553<sup>_∗∗_</sup>|0_._414<sup>_∗∗_</sup>|0_._331<sup>_∗∗_</sup>|**0**_._**272**<sup>_∗∗_</sup>|0_._630<sup>_∗_</sup>|0_._545<sup>_∗_</sup>|0_._478<sup>_∗∗_</sup>|0_._486<sup>_∗∗_</sup>|
|FIN|0_._761<sup>_∗_</sup>|0_._475<sup>_∗∗_</sup>|0_._222<sup>_∗∗_</sup>|0_._298<sup>_∗∗_</sup>|**0**_._**203**<sup>_∗∗_</sup>|0.980|0_._581<sup>_∗_</sup>|0_._281<sup>_∗∗_</sup>|0_._370<sup>_∗∗_</sup>|
|FRA|**0**_._**603**<sup>_∗_</sup>|1.017|0_._741<sup>_∗_</sup>|0.983|0.826|1.081|0.995|0_._769<sup>_∗_</sup>|0_._709<sup>_∗_</sup>|
|GBR|0.765|0_._455<sup>_∗_</sup>|0_._435<sup>_∗_</sup>|0_._462<sup>_∗_</sup>|**0**_._**398**<sup>_∗∗_</sup>|0.729|0_._531<sup>_∗_</sup>|0_._406<sup>_∗_</sup>|0_._540<sup>_∗_</sup>|
|IRL|0_._685<sup>_∗_</sup>|0_._542<sup>_∗∗_</sup>|0_._420<sup>_∗∗_</sup>|**0**_._**338**<sup>_∗∗_</sup>|0_._347<sup>_∗∗_</sup>|0_._633<sup>_∗_</sup>|0_._524<sup>_∗∗_</sup>|0_._534<sup>_∗∗_</sup>|0.975|
|ITA|0.872|0.976|0.897|**0**_._**598**<sup>_∗_</sup>|0.848|0.918|0.908|0.983|1.617|
|JPN|1.240|1.234|1.301|1.572|1.401|0.986|1.030|**0.975**|1.183|
|SWE|0.780|**0**_._**487**<sup>_∗∗_</sup>|0_._491<sup>_∗∗_</sup>|0.882|0_._528<sup>_∗∗_</sup>|0.874|0_._740<sup>_∗_</sup>|0_._511<sup>_∗∗_</sup>|1.178|
|USA|**0.910**|1.108|1.305|1.554|1.827|1.116|1.210|1.235|1.018|
|ZAF|0.876|0_._338<sup>_∗∗_</sup>|0_._355<sup>_∗∗_</sup>|4.351|0_._625<sup>_∗_</sup>|0_._587<sup>_∗_</sup>|0_._616<sup>_∗_</sup>|0_._388<sup>_∗∗_</sup>|**0**_._**202**<sup>_∗∗_</sup>|
|Avg|0.889|**0.803**|0.866|1.186|0.949|0.932|0.876|0.820|0.889|



Note: This table shows the relative MSFE of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The last row shows the average per model over all the countries. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 11 to 14 show the mean squared forecast error of the models with lag length 3 and only including housing prices as variables, compared to an unrestricted PVAR model. The results show that the LASSO models score well on the one step ahead forecasts. Especially the LASSO3, which comes on top in five countries. However, for the multi step ahead forecasts we see that the LASSO models score worse than the Bayesian models and the GVAR model. Also, we can see that the GVAR model scores relatively well again compared to the reported literature. 

If we compare these results to the results of the models including macroeconomic variables we see some interesting things. First, we see that the unrestricted model scores better against the tested models than is the case for the models including macroeconomic variables, as the relative MSFE is more often greater than 1. Second, we see that the Random Walk model never has the lowest relative MSFE for the one and two step ahead forecasts, meaning that lags of housing prices of other countries have an influence on the housing prices in a specific country. Also, the SSSS models do not have countries where the model is laregly misspecified, as was the case in the models with macroeconomic variables. The rest of the results are mostly in line with the results reported in the models with macroeconomic variables 

29 

Table 15: One step ahead average difference of Log-Scores of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|0.85|1.13|1.23|-0.73|**1**_._**61**<sup>_∗_</sup>|-5.03|-4.79|-0.55|0.78|
|NLD|0.03|-1.36|0.01|-0.13|-0.40|**0**_._**42**<sup>_∗_</sup>|**0**_._**42**<sup>_∗_</sup>|0_._32<sup>_∗_</sup>|0.26|
|CAN|-0.45|-0.83|-0.03|-1.04|-0.19|0_._30<sup>_∗_</sup>|**0**_._**35**<sup>_∗_</sup>|0.04|0.05|
|CHE|0.11|-1.54|-0.06|-0.53|-0.59|-0.19|-0.10|**0.13**|-0.45|
|DEU|-1.35|-1.36|-0.32|-0.59|-0.67|-0.16|-0.15|**-0.01**|-0.87|
|DNK|-0.41|-0.92|-0.49|-0.11|-0.12|-2.28|0.09|**0**_._**43**<sup>_∗_</sup>|0.35|
|ESP|-0.12|-2.23|-0.20|-1.51|-0.70|**0**_._**28**<sup>_∗_</sup>|0.19|0.16|0.15|
|FIN|-0.87|-2.29|0.24|-0.27|-0.74|0.22|**0**_._**56**<sup>_∗_</sup>|0_._53<sup>_∗_</sup>|0_._55<sup>_∗_</sup>|
|FRA|0.40|-1.30|0.06|-0.33|-0.41|0_._37<sup>_∗_</sup>|**0**_._**41**<sup>_∗_</sup>|0.29|-1.01|
|GBR|0.15|-0.91|0.15|-0.41|-0.27|-0.27|0_._35<sup>_∗_</sup>|**0**_._**42**<sup>_∗_</sup>|0.40|
|IRL|**0.88**|-1.42|-0.13|-1.34|-0.62|0.29|0.16|0.02|-1.15|
|ITA|-0.15|-0.10|0_._94<sup>_∗_</sup>|-1.04|**1**_._**17**<sup>_∗∗_</sup>|-5.31|0_._67<sup>_∗_</sup>|-1.06|0.05|
|JPN|-1.82|2_._71<sup>_∗_</sup>|**3**_._**99**<sup>_∗_</sup>|3_._46<sup>_∗_</sup>|3_._70<sup>_∗_</sup>|0.31|0.40|-0.67|1_._00<sup>_∗_</sup>|
|SWE|**0.65**|-1.60|-0.19|-0.51|-0.64|0.05|0.09|0.11|-2.01|
|USA|0.01|**0.85**|0.33|-6.00|1.70|-4.17|-1.32|-2.91|0.08|
|ZAF|-0.47|-2.78|0.10|-1.48|-1.41|-0.19|-0.09|**0.11**|**0.11**|
|Avg|-0.16|-0.87|**0.35**|-0.79|0.09|-0.96|-0.17|-0.17|-0.11|



Note: This table shows the average difference of Log-Scores of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the highest average difference for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 16: Two step ahead average difference of Log-Scores of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|-0.54|3_._42<sup>_∗_</sup>|3_._23<sup>_∗∗_</sup>|1_._67<sup>_∗_</sup>|**4**_._**03**<sup>_∗∗_</sup>|-33.48|-28.46|-6.55|-0.12|
|NLD|**0**_._**67**<sup>_∗_</sup>|-1.42|-0.28|-0.21|-0.46|0.08|0.19|-0.01|-0.65|
|CAN|0.12|-0.71|**0.31**|-1.00|0.17|-0.16|-1.36|0.20|-0.21|
|CHE|**0**_._**89**<sup>_∗_</sup>|-1.71|-0.02|-0.15|-0.52|0.01|0.00|0.00|-1.48|
|DEU|-1.87|-1.22|-0.26|-0.40|-0.66|-0.21|-0.23|-0_._05<sup>_∗_</sup>|-1.01|
|DNK|-0.11|-0.78|-0.04|-0.63|0.02|-0.49|**1**_._**09**<sup>_∗_</sup>|0.97|-0.65|
|ESP|-0.74|-1.86|-0.08|-0.44|-0.49|0.27|0.20|0.22|0_._48<sup>_∗_</sup>|
|FIN|0_._54<sup>_∗_</sup>|-2.15|0_._71<sup>_∗_</sup>|-0.01|-0.36|0.04|0_._54<sup>_∗_</sup>|**0**_._**92**<sup>_∗_</sup>|0_._91<sup>_∗_</sup>|
|FRA|**0**_._**78**<sup>_∗_</sup>|-1.68|0.05|0.03|-0.22|-0.53|-0.07|0.21|0.74|
|GBR|0.25|-0.78|0_._44<sup>_∗_</sup>|0.37|0.06|**0**_._**80**<sup>_∗_</sup>|0_._47<sup>_∗_</sup>|0_._70<sup>_∗_</sup>|0.31|
|IRL|**0**_._**85**<sup>_∗_</sup>|-1.64|-0.03|-0.26|-0.47|0.08|0.11|0.12|-0.33|
|ITA|-0.98|-0.90|0.15|-0.52|0.18|-0.92|**0.55**|-1.49|-1.45|
|JPN|-1.45|-1.06|-**0.06**|0.07|-0.12|-1.71|-1.46|-3.78|-2.65|
|SWE|0.35|-1.38|0.18|-0.04|-0.23|0.01|**0.37**|0.31|-0.21|
|USA|-1.85|-0.60|-0.13|-0.57|-4.84|-Inf|-Inf|-41.48|**0**_._**86**<sup>_∗_</sup>|
|ZAF|-0.99|**0**_._**94**<sup>_∗_</sup>|0.35|-2.23|-0.89|-0.48|-0.56|0.02|0.45|
|Avg|-0.26|-0.85|**0.28**|-0.27|-0.30|-Inf|-Inf|-3.11|-0.31|



Note: This table shows the average difference of Log-Scores of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the highest average difference for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

30 

Table 17: Three step ahead average difference of Log-Scores of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|-0.56|5_._99<sup>_∗_</sup>|4_._65<sup>_∗_</sup>|3_._58<sup>_∗_</sup>|**6**_._**15**<sup>_∗_</sup>|-6.47|-0.27|-1.14|-1.87|
|NLD|-0.87|-0.07|0_._79<sup>_∗_</sup>|0_._77<sup>_∗_</sup>|0_._79<sup>_∗_</sup>|0_._61<sup>_∗_</sup>|0.33|**0**_._**94**<sup>_∗_</sup>|0_._88<sup>_∗_</sup>|
|CAN|-0.99|-0.84|-0.06|-0.50|-0.10|-0.15|-0.18|**0.00**|-0.65|
|CHE|**0**_._**88**<sup>_∗_</sup>|-1.61|0.06|-0.27|-0.40|-0.09|-0.21|-0.13|-1.54|
|DEU|-0.54|-1.20|-0.29|-1.25|-0.63|-0.81|-0.71|-0.21|**1**_._**21**<sup>_∗_</sup>|
|DNK|0.13|-0.33|0.10|0.10|0.48|0_._69<sup>_∗_</sup>|0_._82<sup>_∗_</sup>|**1**_._**67**<sup>_∗∗_</sup>|-0.57|
|ESP|0.22|-1.98|0.06|-0.21|-0.35|0.29|**0.30**|0.27|0.28|
|FIN|**1.01**|-2.48|0.37|-0.08|-0.51|-0.36|-0.39|0.65|0.13|
|FRA|**0.51**|-1.20|0.13|-0.01|-0.04|-1.20|-0.48|0.13|0.12|
|GBR|0.43|-0.77|**0**_._**59**<sup>_∗_</sup>|0.47|0.37|-1.42|0.35|0.35|0.44|
|IRL|**0.32**|-1.61|0.00|-0.43|-0.39|0.03|0.02|0.03|0.23|
|ITA|-0.48|-1.10|-0.02|-0.90|**0.05**|-5.83|-0.16|-3.01|-0.54|
|JPN|-2.32|-0.86|0.14|-0.20|-0.00|**0.14**|0.01|-0.92|-0.67|
|SWE|-0.13|-1.13|0.17|-0.05|-0.09|-0.34|0.10|**0.32**|-1.02|
|USA|-0.24|**3**_._**55**<sup>_∗_</sup>|2.55|-2.04|3.53|-67.96|-24.75|-19.14|1.21|
|ZAF|-0.89|-1.18|**0**_._**92**<sup>_∗_</sup>|-0.83|0.07|-0.01|-0.06|0.40|0.77|
|Avg|-0.22|-0.43|**0.64**|-0.12|0.56|-5.18|-1.58|-1.24|-0.12|



Note: This table shows the average difference of Log-Scores of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the highest average difference for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 18: Four step ahead average difference of Log-Scores of the housing prices 

||GVAR|SSSS1|SSSS2|BFCS|BMS|LASSO1|LASSO2|LASSO3|RW|
|---|---|---|---|---|---|---|---|---|---|
|AUS|-0.07|**8**_._**58**<sup>_∗_</sup>|7_._16<sup>_∗_</sup>|3_._97<sup>_∗_</sup>|8_._10<sup>_∗_</sup>|-0.39|-0.18|-0.11|-0.56|
|NLD|-0.18|-0.09|-0.38|-0.05|**0.81**|-0.69|-0.83|-3.58|0.56|
|CAN|-0.47|-0.61|0.21|-0.26|0.10|-1.17|-1.26|-0.05|**0**_._**55**<sup>_∗_</sup>|
|CHE|0.12|-1.57|-0.42|-0.32|-0.24|0.03|-0.06|0.02|**0**_._**29**|
|DEU|-0.52|-1.16|-0.67|-0.72|-0.56|-0.88|-0.82|-0.88|**-0.20**|
|DNK|0.23|-0.26|**0.55**|0.25|0.54|-0.04|-0.91|0.43|-0.87|
|ESP|0.44|-1.58|0.39|-0.63|0.08|0.33|0.42|**0.49**|0.47|
|FIN|0.38|-2.30|0.41|-0.31|-0.23|-0.18|-0.17|**0.50**|0.48|
|FRA|**0.41**|-1.18|0.24|-0.99|0.12|-0.69|-0.10|0.23|0.19|
|GBR|0.22|-0.97|0_._51<sup>_∗_</sup>|0.09|0.31|0.01|0_._53<sup>_∗_</sup>|**0**_._**62**<sup>_∗_</sup>|0_._57<sup>_∗_</sup>|
|IRL|-0.35|-1.26|**0**_._**35**<sup>_∗_</sup>|-0.26|0.01|0_._29<sup>_∗_</sup>|0_._30<sup>_∗_</sup>|0_._34<sup>_∗_</sup>|-0.21|
|ITA|-0.11|-1.11|**0.18**|0.10|0.09|-5.54|0.05|-4.31|-0.87|
|JPN|-0.25|-0.67|-0.23|-0.45|0.06|**0**_._**50**<sup>_∗_</sup>|0.13|-0.62|-0.25|
|SWE|0.16|-1.07|0.27|-0.25|0.15|-0.43|-0.11|**0**_._**57**<sup>_∗_</sup>|-0.14|
|USA|0.11|**1.08**|0.01|-2.43|-2.91|-1.57|-8.93|-1.52|-0.03|
|ZAF|0.09|-0.95|1.17|-0.74|0.35|-0.05|0.07|0_._72<sup>_∗_</sup>|**1**_._**56**<sup>_∗_</sup>|
|Avg|0.01|-0.32|**0.61**|-0.19|0.42|-0.65|-0.74|-0.45|-0.01|



Note: This table shows the average difference of Log-Scores of the housing prices with respect to an unrestricted PVAR model estimated with OLS. A * means that the model has a better forecast compared to the benchmark with a 10% significance. A ** stands for a 5% significance and a *** for a 1% significance. The values in bold show the highest average difference for a country. The last row shows the average per model of all the countries. Significance levels are not reported for the average. 

Table 15 to 18 show the average difference of the Log-Scores of the models with lag length 3 and only including housing prices as variables compared to an unrestricted PVAR model. We see that the significance levels of the density forecasts are lower than the significance 

31 

levels of the point forecasts, which is a similar result to that of the models including macroeconomic variables. 

Furthermore, we see that the LASSO models have the highest Log-Score on average for the density forecast, but most of the scores are not significantly different from the benchmark model. This means that the density forecast for this set of variables performs worse than the other forecasts. 

#### **Concluding remarks** 

This forecasting exercise shows that additional information about housing prices of other countries and macroeconomic variables does lead to an increase in the forecast accuracy. On average, the LASSO models perform the best. However, there is not a single model that consistently and significantly outperforms the other models for all countries. 

### **4.2 Variable importance** 

#### **Bayesian** 

If we take a look at the _γ_ draws from the SSSS algorithm, we see something remarkable for both of the SSSS models we test in this research. The _γk_ draws are almost exclusively zero for the whole sample, implying there is no DI between almost any of the countries. However, if we take a look at the coefficient matrix, we see directly what the forementioned shortcoming is of the SSSS algorithm, as all of the entries in the coefficient matrix are nonzero. So although almost all of the _γ_ draws are equal to zero, implying that the matrix entry would be zero, there are still no nonzero matrix entries. This is because the restriction that elements are zero can only hold approximately. 

32 

#### **LASSO methods** 

|Table 19|: Amount o<br>Incoming|f cross-cou<br> dependenc|ntry depend<br>ies|encies of the<br>Outgoing|macroecon<br> dependenc|omic model<br>ies|
|---|---|---|---|---|---|---|
||LASSO1|LASSO2|LASSO3|LASSO1|LASSO2|LASSO3|
|AUS|0|0|1|2|1|4|
|NLD|0|1|0|1|1|3|
|CAN|0|1|0|1|0|1|
|CHE|0|0|0|1|1|4|
|DEU|15|4|5|0|0|2|
|DNK|0|0|0|1|1|3|
|ESP|0|0|14|2|4|5|
|FIN|0|3|1|3|2|5|
|FRA|0|0|2|1|0|2|
|GBR|4|0|0|2|2|3|
|IRL|1|5|9|1|1|3|
|ITA|1|0|0|1|0|2|
|JPN|0|0|13|1|1|2|
|SWE|1|4|1|1|0|3|
|USA|0|0|0|3|2|2|
|ZAF|0|0|1|1|2|3|



Note: This table shows the incoming and outgoing dependencies of countries for the LASSO models including the macroeconomic variables. We count a dependency, if at least one coefficient of a country was nonzero for another country’s equation. 

Table 20: Amount of cross-country dependencies of the model with multiple lags 

||Incoming|dependenci|es|Outgoing|dependenci|es|
|---|---|---|---|---|---|---|
||LASSO1|LASSO2|LASSO3|LASSO1|LASSO2|LASSO3|
|AUS|15|15|15|11|9|4|
|NLD|11|14|0|14|12|2|
|CAN|15|14|0|15|11|5|
|CHE|12|10|0|15|13|5|
|DEU|11|9|0|15|11|5|
|DNK|12|12|0|14|11|3|
|ESP|12|11|2|13|12|3|
|FIN|15|12|4|14|12|3|
|FRA|15|11|6|11|10|2|
|GBR|14|11|6|10|11|3|
|IRL|14|11|4|13|10|2|
|ITA|13|7|0|13|11|2|
|JPN|14|12|13|14|13|2|
|SWE|13|8|0|14|12|2|
|USA|11|7|1|14|13|6|
|ZAF|15|15|0|12|8|2|



Note: This table shows the incoming and outgoing dependencies of countries for the LASSO models with multiple lags. We count a dependency, if at least one coefficient of a country was nonzero for another country’s equation. 

33 

Tables 19 and 20 show the amount of incoming and outgoing nonzero coefficients from and to countries. A few things stand out. First, we can see that the amount of interdependencies between countries are a lot higher for the model with multiple lags. Especially the LASSO1 model and LASSO2 models have a lot of interdependencies. If we look closer why this difference is there, we find that the setting of the penalty parameter _λk_ differs a lot between the two models. In the model with macroeconomic variables, we search for higher values of _λk_ and those higher values also get chosen by the model in the cross validation. This means that more parameters will be set to zero and therefore leading to less interdependencies. This also explains the underperformance of the LASSO models in the forecasting exercise for the model with multiple lags, as there are not many nonzero coefficients which leads to an increased forecasting variance. 

Furthermore, we see in table 19 that Germany has high values for incoming dependencies. This is not what we expect, as Germany is one of the bigger economies, meaning that we expect Germany will have more outgoing dependencies than incoming. However, this result is in line with the forecasting results, as we see that the Random Walk model outperforms the LASSO models for Germany. This leads to the conclusion that the LASSO models are likely misspecified for Germany for the model including macroeconomic variables. Also, there are two countries that do not have any incoming dependencies, being Switzerland and the United States. From the latter this is in line with what we expect as the United States is one of the leading economies in the world, which means it is more likely that they influence other countries than vice versa. The result for Switzerland can be explained by their history of neutrality and thus not leaning on other countries. For example, they only joined the United Nations recently on September 10, 2002. However, this fact does not explain that Switzerland does have some outgoing dependencies, as we would expect this relationship also holds the other way around. 

34 

### **4.3 Monetary policy shocks** 













Figure 5: Impulse response functions due to monetary policy shocks with one standard deviation 

35 













Figure 6: Impulse response functions due to monetary policy shocks with one standard deviation 

36 









Figure 7: Impulse response functions due to monetary policy shocks with one standard deviation 

Figures 5, 6 and 7 show the impulse response functions to monetary policy shocks by the federal reserve for all the different countries. We modelled the impulse response function up to 20 quarters. We can see that almost all the countries have an initial negative response to a monetary policy shock. The only exceptions are Switzerland (5c), Germany (5d) and Ireland (6d). 

The initial negative shock means that a surprise tightening of monetary policy (which is a positive shock), leads to a decline in the housing prices. This is in line with what we expect, as a tightening of monetary policy occurs for example when the fed increases the interest rates. This increase of interest rates means that the mortgage rate is likely to go up which means that households cannot borrow as much as before. Therefore, households cannot pay as high of a price as before. 

The shape of the impulse response function differs between countries. For example, there are countries with a relative steady upward sloping impulse response function (see for example Spain (5f), Finland (6a), Italy (6e) and South Africa (7d)), meaning that the initial negative effect will become less over time and sometimes even becomes a positive effect. Furthermore, there are countries without a clear visible trend (for example Australia (5a), Switzerland 5c, Ireland (6d) 

37 

and more). One of the more peculiar shaped impulse response function belongs to Germany (5d) where the effect of the monetary policy keeps alternating between a positive effect and a negative effect. 

The graphs do suggest that monetary policy shocks by the federal reserve affect the housing prices of the observed countries. 

## **5 Conclusion** 

This research investigates the effect of foreign variables and monetary policy shocks by the federal reserve on housing prices in specific countries. Furthermore, we investigate which type of model will forecast the housing prices most accurately. This research finds that the reduced form PVAR models do increase the forecast accuracy with respect to the benchmark unrestricted model. This indicates that allowing for unrestricted interdependencies while modelling the housing prices leads to misspeficiation of the model. However, we do not find a single model that clearly performs the best out of the models for all countries. 

When looking into the dependencies on variables of other countries, we find that other countries do have some influence on the housing prices of specific countries, as the coefficients of the LASSO PVAR models do have some nonzero entries. Lastly, we construct the impulse response functions of the housing prices with federal reserve monetary policy shocks. The local projections show that the housing prices do react mostly negatively to a positive monetary policy shock, which stands for tightening the monetary policy. 

We also have some recommendations for future research. To start, we would like to assess the hyperparameter search. We have not done any hyperparameter searches for the Bayesian methods due to the high amount of computational time. We highly recommend to test some hyperparameters for the Bayesian methods if the computational time is there. Furthermore, we do a grid search for the penalty parameters of the LASSO PVAR method. While this can give a good indication which penalty parameter is suited best, it comes with a few downsides. For example, we do not consider every possible value the penalty parameter can have. For example, Bergstra and Bengio (2012) show that a random search outperforms a grid search when searching hyperparameters. Another method is the Bayesian optimization, pioneered by Snoek et al. (2012). We would suggest to follow that method for better hyperparameter optimization. Also, this research had to take some shortcuts because of the data constraint. Simply put, we do not have enough data to implement every model we wanted into the research (for example a model with a large amount of lags and variables). We would suggest to do this research again in a few years again to see if there is more data available and therefore being able to test more models. 

Lastly, we suggest future research to do more robustness checks. This research had some robustness checks in place, because we test different kind of models with more lags or more macroeconomic variables, but more can be done to elevate this research. 

38 

## **References** 

- Amisano, G., & Giacomini, R. (2007). Comparing density forecasts via weighted likelihood ratio tests. _Journal of Business & Economic Statistics_ , _25_ (2), 177–190. 

- Apergis, N., et al. (2003). Housing prices and macroeconomic factors: Prospects within the european monetary union. _International real estate review_ , _6_ (1), 63–74. 

- Aye, G. C., Balcilar, M., Bosch, A., & Gupta, R. (2014). Housing and the business cycle in south africa. _Journal of Policy Modeling_ , _36_ (3), 471–491. 

- Balcilar, M., Gupta, R., & Miller, S. M. (2014). Housing and the great depression. _Applied Economics_ , _46_ (24), 2966–2981. 

- Basu, S., & Michailidis, G. (2015). Regularized estimation in sparse high-dimensional time series models. 

- Baxter, M., & Kouparitsas, M. A. (2005). Determinants of business cycle comovement: A robust analysis. _Journal of Monetary Economics_ , _52_ (1), 113–157. 

- Berg, T. O., & Henzel, S. R. (2015). Point and density forecasts for the euro area using bayesian vars. _International Journal of Forecasting_ , _31_ (4), 1067–1095. 

- Bergstra, J., & Bengio, Y. (2012). Random search for hyper-parameter optimization. _Journal of machine learning research_ , _13_ (2). 

- Bluedorn, J. C., & Bowdler, C. (2011). The open economy consequences of us monetary policy. _Journal of International Money and Finance_ , _30_ (2), 309–336. 

- Bu, C., Rogers, J., & Wu, W. (2021). A unified measure of fed monetary policy shocks. _Journal of Monetary Economics_ , _118_ , 331–349. 

- Camehl, A. (2022). Penalized estimation of panel vector autoregressive models: A panel lasso approach. _International Journal of Forecasting_ . https://doi.org/10.1016/j. ijforecast.2022.05.007 

- Canova, F., & Ciccarelli, M. (2009). Estimating multicountry var models. _International economic review_ , _50_ (3), 929–959. 

- Case, K. E., Quigley, J. M., & Shiller, R. J. (2005). Comparing wealth effects: The stock market versus the housing market. _Advances in macroeconomics_ , _5_ (1). 

- Cesa-Bianchi, A. (2013). Housing cycles and macroeconomic fluctuations: A global perspective. _Journal of International Money and Finance_ , _37_ , 215–238. 

- Choudhry, T. (2020). Economic policy uncertainty and house prices: Evidence from geographical regions of england and wales. _Real Estate Economics_ , _48_ (2), 504–529. 

- Christou, C., Gupta, R., & Hassapis, C. (2017). Does economic policy uncertainty forecast real housing returns in a panel of oecd countries? a bayesian approach. _The Quarterly Review of Economics and Finance_ , _65_ , 50–60. 

- Cochrane, J. H., & Piazzesi, M. (2002). The fed and interest rates-a high-frequency identification. _American economic review_ , _92_ (2), 90–95. 

39 

- Cook, T., & Hahn, T. (1989). The effect of changes in the federal funds rate target on market interest rates in the 1970s. _Journal of monetary economics_ , _24_ (3), 331–351. 

- Cuaresma, J. C., Feldkircher, M., & Huber, F. (2016). Forecasting with global vector autoregressive models: A bayesian approach. _Journal of Applied Econometrics_ , _31_ (7), 1371–1391. 

- Dees, S., Mauro, F. d., Pesaran, M. H., & Smith, L. V. (2007). Exploring the international linkages of the euro area: A global var analysis. _Journal of applied econometrics_ , _22_ (1), 1–38. 

- Del Negro, M., & Otrok, C. (2007). 99 luftballons: Monetary policy and the house price boom across us states. _Journal of Monetary Economics_ , _54_ (7), 1962–1985. 

- Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. _Journal of Business & Economic Statistics_ , _13_ (3), 253–263. 

- Dunson, D. B., Herring, A. H., & Engel, S. M. (2008). Bayesian selection and clustering of polymorphisms in functionally related genes. _Journal of the American Statistical Association_ , _103_ (482), 534–546. 

- Ehrmann, M., & Fratzscher, M. (2009). Global financial transmission of monetary policy shocks. _Oxford Bulletin of Economics and Statistics_ , _71_ (6), 739–759. 

- Fama, E. F., & MacBeth, J. D. (1973). Risk, return, and equilibrium: Empirical tests. _Journal of political economy_ , _81_ (3), 607–636. 

- Feldkircher, M., Huber, F., & Pfarrhofer, M. (2020). Factor augmented vector autoregressions, panel vars, and global vars. _Macroeconomic Forecasting in the Era of Big Data: Theory and Practice_ , 65–93. 

- Fratantoni, M., & Schuh, S. (2003). Monetary policy, housing, and heterogeneous regional markets. _Journal of Money, Credit and Banking_ , 557–589. 

- Fratzscher, M., Lo Duca, M., & Straub, R. (2018). On the international spillovers of us quantitative easing. _The Economic Journal_ , _128_ (608), 330–377. 

- Friedman, J., Hastie, T., H¨ofling, H., & Tibshirani, R. (2007). Pathwise coordinate optimization. 

- Friedman, J., Hastie, T., & Tibshirani, R. (2010). Regularization paths for generalized linear models via coordinate descent. _Journal of statistical software_ , _33_ (1), 1. 

- Friedman, J., Hastie, T., & Tibshirani, R. (2008). Sparse inverse covariance estimation with the graphical lasso. _Biostatistics_ , _9_ (3), 432–441. 

- Garcia, M. G., Medeiros, M. C., & Vasconcelos, G. F. (2017). Real-time inflation forecasting with high-dimensional models: The case of brazil. _International Journal of Forecasting_ , _33_ (3), 679–693. 

- George, E. I., & McCulloch, R. E. (1993). Variable selection via gibbs sampling. _Journal of the American Statistical Association_ , _88_ (423), 881–889. 

- George, E. I., Sun, D., & Ni, S. (2008). Bayesian stochastic search for var model restrictions. _Journal of Econometrics_ , _142_ (1), 553–580. 

40 

- Georgiadis, G. (2016). Determinants of global spillovers from us monetary policy. _Journal of international Money and Finance_ , _67_ , 41–61. 

- Giannone, D., Lenza, M., & Primiceri, G. E. (2015). Prior selection for vector autoregressions. _Review of Economics and Statistics_ , _97_ (2), 436–451. 

- Gilchrist, S., L´opez-Salido, D., & Zakrajˇsek, E. (2015). Monetary policy and real borrowing costs at the zero lower bound. _American Economic Journal: Macroeconomics_ , _7_ (1), 77–109. 

- Greenwood-Nimmo, M., Nguyen, V. H., & Shin, Y. (2012). Probabilistic forecasting of output growth, inflation and the balance of trade in a gvar framework. _Journal of Applied Econometrics_ , _27_ (4), 554–573. 

- Han, F., & Hee Ng, T. (2011). _Asean-5 macroeconomic forecasting using a gvar model_ (tech. rep.). ADB Working Paper Series on Regional Economic Integration. 

- Harvey, D., Leybourne, S., & Newbold, P. (1997). Testing the equality of prediction mean squared errors. _International Journal of forecasting_ , _13_ (2), 281–291. 

- Hirata, H., Kose, M. A., Otrok, C., & Terrones, M. E. (2013). Global house price fluctuations: Synchronization and determinants. _NBER International Seminar on Macroeconomics_ , _9_ (1), 119–166. 

- Iacoviello, M. (2005). House prices, borrowing constraints, and monetary policy in the business cycle. _American economic review_ , _95_ (3), 739–764. 

- Jacobsen, D. H., & Naug, B. E. (2005). What drives house prices? _Norges Bank. Economic Bulletin_ , _76_ (1), 29. 

- Jarocinski, M., & Smets, F. (2008). House prices and the stance of monetary policy. 

- Jord`a, O.<sup>`</sup> (2005). Estimation and inference of impulse responses by local projections. _American economic review_ , _95_ (1), 161–182. 

- Kim, S. (2001). International transmission of us monetary policy shocks: Evidence from var’s. _Journal of monetary Economics_ , _48_ (2), 339–372. 

- Koop, G., & Korobilis, D. (2016). Model uncertainty in panel vector autoregressive models. _European Economic Review_ , _81_ , 115–131. 

- Koop, G., & Korobilis, D. (2019). Forecasting with high-dimensional panel vars. _Oxford Bulletin of Economics and Statistics_ , _81_ (5), 937–959. 

- Korobilis, D. (2016). Prior selection for panel vector autoregressions. _Computational Statistics & Data Analysis_ , _101_ , 110–120. 

- Kuttner, K. N. (2001). Monetary policy surprises and interest rates: Evidence from the fed funds futures market. _Journal of monetary economics_ , _47_ (3), 523–544. 

- Lanne, M., & L¨utkepohl, H. (2008). Identifying monetary policy shocks via changes in volatility. _Journal of Money, Credit and Banking_ , _40_ (6), 1131–1149. 

- Leamer, E. E. (2007). Housing is the business cycle. 

- Lee, H. S., & Lee, W. S. (2018). Housing market volatility connectedness among g7 countries. _Applied Economics Letters_ , _25_ (3), 146–151. 

41 

- Lee, W., & Liu, Y. (2012). Simultaneous multiple response regression and inverse covariance matrix estimation via penalized gaussian maximum likelihood. _Journal of multivariate analysis_ , _111_ , 241–255. 

- Marcellino, M., Stock, J. H., & Watson, M. W. (2006). A comparison of direct and iterated multistep ar methods for forecasting macroeconomic time series. _Journal of econometrics_ , _135_ (1-2), 499–526. 

- Melnyk, I., & Banerjee, A. (2016). Estimating structured vector autoregressive models. _International Conference on Machine Learning_ , 830–839. 

- Nakamura, E., & Steinsson, J. (2018). High-frequency identification of monetary nonneutrality: The information effect. _The Quarterly Journal of Economics_ , _133_ (3), 1283–1330. 

- Nyakabawo, W., Miller, S. M., Balcilar, M., Das, S., & Gupta, R. (2015). Temporal causality between house prices and output in the us: A bootstrap rolling-window approach. _The North American Journal of Economics and Finance_ , _33_ , 55–73. 

- OECD. (2022). Housing prices (indicator) [doi: 10.1787/63008438-en (Accessed on 27 November 2022)]. 

- Pesaran, M. H., Schuermann, T., & Smith, L. V. (2009). Forecasting economic and financial variables with global vars. _International journal of forecasting_ , _25_ (4), 642– 675. 

- Pesaran, M. H., Schuermann, T., & Weiner, S. M. (2004). Modeling regional interdependencies using a global error-correcting macroeconometric model. _Journal of Business & Economic Statistics_ , _22_ (2), 129–162. 

- Ren, Y., & Zhang, X. (2010). Subset selection for vector autoregressive processes via adaptive lasso. _Statistics & probability letters_ , _80_ (23-24), 1705–1712. 

- San Ong, T. (2013). Factors affecting the price of housing in malaysia. _J. Emerg. Issues Econ. Financ. Bank_ , _1_ , 414–429. 

- Snoek, J., Larochelle, H., & Adams, R. P. (2012). Practical bayesian optimization of machine learning algorithms. _Advances in neural information processing systems_ , _25_ . 

- Song, S., & Bickel, P. J. (2011). Large vector auto regressions. _arXiv preprint arXiv:1106.3915_ . 

- Stock, J. H., & Watson, M. W. (2012). Generalized shrinkage methods for forecasting using many predictors. _Journal of Business & Economic Statistics_ , _30_ (4), 481– 493. 

- Swanson, E. T., & Williams, J. C. (2014). Measuring the effect of the zero lower bound on medium-and longer-term interest rates. _American economic review_ , _104_ (10), 3154–3185. 

- Taylor, J. B. (2007). _Housing and monetary policy_ (tech. rep.). National Bureau of Economic Research. 

42 

- Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. _Journal of the Royal Statistical Society: Series B (Methodological)_ , _58_ (1), 267–288. 

- Vansteenkiste, I., & Hiebert, P. (2011). Do house price developments spillover across euro area countries? evidence from a global var. _Journal of Housing Economics_ , _20_ (4), 299–314. 

- Vargas-Silva, C. (2008a). The effect of monetary policy on housing: A factor-augmented vector autoregression (favar) approach. _Applied Economics Letters_ , _15_ (10), 749– 752. 

- Vargas-Silva, C. (2008b). Monetary policy and the us housing market: A var analysis imposing sign restrictions. _Journal of Macroeconomics_ , _30_ (3), 977–990. 

- Wongswan, J. (2009). The response of global equity indexes to us monetary policy announcements. _Journal of International Money and Finance_ , _28_ (2), 344–365. 

- Zhu, M. (2014). Housing markets, financial stability and the economy [Opening Remarks at the Bundesbank/German Research Foundation/IMF Conference by Deputy Managing Director of the IMF Min Zhu [Accessed: 2023-04-01]]. https://www. imf.org/en/News/Articles/2015/09/28/04/53/sp060514 

## **6 Appendix** 

### **6.1 Data explanation** 

The data in this research is retrieved from the OECD. Here we explain the data labels more in detail. 

#### **6.1.1 Nominal housing prices** 

The nominal housing prices are calculated as follows: The nominal house price index encompasses the sale of newly-constructed and pre-existing residential properties, in accordance with the guidelines outlined in the Residential Property Prices Indices (RPPI) manual OECD (2022). The values of the housing prices are standardized such that each country’s nominal house price value is 100 in 2015. The other years are based around that value. The data can be accessed at: https://data.oecd.org/price/housing-prices.htm. 

#### **6.1.2 Inflation** 

The inflation is measured by the consumer price index (CPI) as the annual growth rate in percent. A consumer price index is computed as a sequence of concise measurements of the proportional change in prices of a fixed collection of consumer goods and services that remain constant in quantity and characteristics, which are bought, utilized, or paid for by the reference population. Each brief measurement is created as a weighted average of many elementary aggregate indices. The elementary aggregate indices are assessed using a sample of prices for a specific set of goods and services that are obtained from a given set of outlets or other sources of consumption goods 

43 

and services in a specific region, or by its residents (OECD, 2022). The data can be accessed at: https://data.oecd.org/price/inflation-cpi.htmindicator-chart 

#### **6.1.3 GDP** 

The GDP data is reported quarterly. ”This indicator is based on real GDP (also called GDP at constant prices or GDP in volume), i.e. the developments over time are adjusted for price changes. The numbers are also adjusted for seasonal influences.” (OECD, 2022). We retrieve this series as percentage change, previous period. The data can be accessed at: gdp.htm 

#### **6.1.4 Share price** 

Share price indices are determined by calculating the value of common shares of companies traded on national or foreign stock exchanges. The stock exchange usually uses the closing daily values for monthly data and expresses the indices as simple arithmetic averages of the daily data. These indices measure the fluctuations in the value of stocks included in the index (OECD, 2022). The data can be accessed at: https://data.oecd.org/price/share-prices.htmindicator-chart 

### **6.2 Short explanation of the code** 

This research uses the code from the paper of Camehl (2022) for the LASSO methods and the code from Korobilis (2016) for the Bayesian methods. There are some small tweaks to the code, but the foundation of the original code still stands. For the GVAR method, we wrote the code ourselves, but that code is pretty straightforward in itself. 

44 

|15|07|02|1|14|04|08|07|05|15|03|09|19|06|09||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0|
|0.266|0.111|0.853|0.168|0.165|0.074|0.087|0.085|0.121|0.205|0.268|0.126|0.496|0.088|0|0.191|
|0.013|0.032|0.003|0.011|0.035|0.202|0.016|0.179|0.019|0.026|0.01|0.019|0.008|0|0.01|0.015|
|0.366|0.024|0.031|0.034|0.036|0.017|0.02|0.024|0.026|0.027|0.04|0.022|0|0.02|0.136|0.112|
|0.04|0.062|0.014|0.115|0.1|0.049|0.128|0.042|0.124|0.061|0.027|0|0.024|0.054|0.039|0.059|
|0.013|0.02|0.003|0.027|0.016|0.015|0.016|0.015|0.016|0.072|0|0.01|0.016|0.01|0.029|0.006|
|0.066|0.131|0.031|0.118|0.119|0.09|0.111|0.067|0.088|0|0.286|0.086|0.043|0.103|0.089|0.138|
|0.033|0.114|0.012|0.113|0.159|0.051|0.246|0.055|0|0.088|0.063|0.175|0.042|0.075|0.052|0.043|
|0.004|0.018|0.002|0.005|0.017|0.033|0.007|0|0.006|0.008|0.007|0.007|0.004|0.081|0.004|0.007|
|0.016|0.044|0.004|0.034|0.061|0.03|0|0.031|0.123|0.055|0.033|0.09|0.016|0.032|0.019|0.036|
|0.007|0.022|0.002|0.005|0.026|0|0.01|0.048|0.009|0.015|0.01|0.012|0.005|0.132|0.005|0.006|
|0.085|0.379|0.024|0.307|0|0.298|0.234|0.276|0.302|0.225|0.118|0.268|0.108|0.259|0.137|0.249|
|0.024|0.018|0.007|0|0.078|0.015|0.033|0.022|0.055|0.058|0.053|0.079|0.026|0.02|0.035|0.043|
|0.023|0.01|0|0.015|0.013|0.011|0.009|0.018|0.012|0.032|0.012|0.019|0.049|0.011|0.375|0.018|
|0.029|0|0.008|0.028|0.154|0.102|0.068|0.123|0.088|0.101|0.06|0.068|0.03|0.098|0.037|0.052|
||.007|.004|.01|.009|.009|.006|.007|.006|.013|.01|.011|.114|.01|.023|.027|
|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0|



45 

