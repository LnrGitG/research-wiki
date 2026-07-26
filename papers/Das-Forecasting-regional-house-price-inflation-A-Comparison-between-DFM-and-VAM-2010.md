---
title: **Forecasting Regional House Price Infl ation: A Comparison between Dynamic Factor Models and Vector Autoregressive Models**
type: paper
source_pdf: raw/papers/Das_Forecasting regional house price inflation A Comparison between DFM and VAM_2010.pdf
converted: 2026-07-26
---

_Journal of Forecasting J. Forecast._ (2010) Published online in Wiley InterScience (www.interscience.wiley.com) **DOI** : 10.1002/for.1182 

# **Forecasting Regional House Price Infl ation: A Comparison between Dynamic Factor Models and Vector Autoregressive Models** 

SONALI DAS,<sup>1</sup> RANGAN GUPTA<sup>2</sup> * AND ALAIN KABUNDI<sup>3</sup> 1 _Logistics and Quantitative Methods, CSIR Built Environment, Pretoria, South Africa_ 

> 2 _Department of Economics, University of Pretoria, Pretoria, South Africa_ 

> 3 _Department of Economics, University of Johannesburg, Johannesburg, South Africa_ 

### ABSTRACT 

This paper uses the dynamic factor model framework, which accommodates a large cross-section of macroeconomic time series, for forecasting regional house price infl ation. In this study, we forecast house price infl ation for fi ve metropolitan areas of South Africa using principal components obtained from 282 quarterly macroeconomic time series in the period 1980:1 to 2006:4. The results, based on the root mean square errors of one to four quarters ahead out-of-sample forecasts over the period 2001:1 to 2006:4 indicate that, in the majority of the cases, the Dynamic Factor Model statistically outperforms the vector autoregressive models, using both the classical and the Bayesian treatments. We also consider spatial and non-spatial specifi cations. Our results indicate that macroeconomic fundamentals in forecasting house price infl ation are important. Copyright © 2010 John Wiley & Sons, Ltd. 

key words  Bayesian models; forecast accuracy; spatial and non-spatial models 

## INTRODUCTION 

This paper investigates whether the wealth of information contained in the dynamic factor model (DFM) framework, developed by Forni _et al._ (2005), can be useful in forecasting regional house price infl ation. To illustrate, we use the DFM to predict house price infl ation, defi ned as the percentage change in house prices, in fi ve metropolitan areas of South Africa, namely Cape Town, Durban, Johannesburg, Port Elizabeth and Pretoria, using quarterly data over the period 1980:1 to 2006:4. The panel data comprise 282 quarterly series for the South African economy, a set of global variables such as commodity industrial inputs price index and crude oil prices, and time series of major trading 

> * Correspondence to: Rangan Gupta, Department of Economics, University of Pretoria, Pretoria 0002, South Africa. E-mail: Rangan.Gupta@up.ac.za 

Copyright © 2010 John Wiley & Sons, Ltd. 

## _S. Das, R. Gupta and A. Kabundi_ 

partners, namely Germany, the UK, and the USA. The forecast performance of the DFM is evaluated in terms of the root mean square error (RMSE), by comparing its performance with spatial Bayesian vector autoregressive (SBVAR) models that weighs in the infl uence of neighbors on the determination of house price infl ation of a particular region, and also to the non-spatial unrestricted classical vector autoregressive (VAR) model and Bayesian vector autoregressive (BVAR) models using the Minnesota prior. All the alternative models are estimated based on only the house price infl ation series. 

The importance of predicting house price infl ation is highlighted by recent studies in which it is concluded that asset prices help to forecast both infl ation and output (Forni _et al._ , 2003; Stock and Watson, 2003). Since a large amount of individual wealth is embedded in houses, house prices are important in signaling infl ation. Gupta and Das (2008) point out that, in South Africa, housing infl a- tion and consumer price index (CPI) infl ation tend to move together. As such, models that forecast house price infl ation can give policy makers an idea about the direction of CPI infl ation in the future, and hence can provide a better control for designing appropriate policies. The reason for using regional data is to account for possible heterogeneity and segmentation that might exist in the housing market. Herein also comes the justifi cation of modeling house prices separately based on the size of the house. 

The rationale behind using a data-rich DFM to forecast house price infl ation emanates from the fact that a large number of economic variables help in predicting housing price growth (Cho, 1996; <u>Abraham and Hendershott, 1996; Johnes and Hyclak, 1999; Rapach and Strauss, 2007, 2009). For</u> instance, income, interest rates, construction costs, labor market variables, stock prices, industrial production, and consumer confi dence index—which are included in the DFM—are potential predictors. In addition, given that movements in the housing market are likely to play an important role in the business cycle, not only because housing investment is a very volatile component of demand (Bernanke and Gertler, 1995), but also because changes in house prices tend to have important wealth effects on consumption (International Monetary Fund, 2000) and investment (Topel and Rosen, <u>1988), the importance of forecasting house price infl ation is vital, since the housing sector serves as</u> a leading indicator of the real sector of the economy. 

To the best of our knowledge, this is the fi rst attempt to compare the forecasting performances of a DFM with spatial and non-spatial econometric models in terms of predicting regional house price infl ation. Rapach and Strauss (2007, 2009) used autoregressive distributed lag (ARDL) models containing, respectively, 25 and 30 variables to forecast real housing price growth for the individual states of the Federal Reserve’s Eighth District and the 20 largest US states. Given the diffi culty in determining a priori the particular variables that are most important for forecasting real housing price growth, the authors used various methods to combine the individual ARDL model forecasts, which in turn resulted in better forecasting of real housing price growth compared to the individual ARDL models. Vargas-Silva (2008) point to the importance of using as many as 120 monthly series to analyze the impact of monetary policy actions on the housing sector of four different regions of the USA based on a factor-augmented VAR (FAVAR) model. The author indicates that the housing market tends to be negatively affected by positive interest rate shocks but, more importantly, marked heterogeneity in the responses of the housing market variables for the four regions were depicted, with the Southern region driving the aggregate US housing market. The remainder of the paper is organized as follows: the second and third sections, respectively, lay out the DFM and outline the basics of the VAR, the Minnesota-type BVARs, and the SBVARs based on the fi rst-order spatial contiguity (FOSC) and the random walk averaging (RWA) priors developed by LeSage and Pan (1995) and LeSage and Krivelyova (1999), respectively. The fourth section discusses the data used 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

_Forecasting Regional House Price Infl ation_ 

to estimate the DFM, while the fi fth section reports the results from the forecasting exercise. The sixth section concludes. 

## DYNAMIC FACTOR MODEL (DFM) 

This study uses the generalized dynamic factor model (DFM) developed by Forni _et al._ (2005) to extract common components between macroeconomics series, which are then used to forecast metropolitan house price infl ation for the South African housing market. In the VAR models, since all variables are used in forecasting, the number of parameters to be estimated depends on the number of variables _n_ . With such a large information set, _n_ , the estimation of a large number of parameters leads to a curse of dimensionality problem. The generalized DFM expresses individual times series as the sum of two unobserved components: a common component driven by a small number of common factors and an idiosyncratic component, which are specifi c to each variable. Forni _et al._ (2005) demonstrated that when the number of factors is small relative to the number of variables and the panel is heterogeneous, the factors can be recovered from present and past observations. 

′ Consider an _n_ × 1 covariance stationary process _Yt_ = ( _y_ 1 _t_ , . . . , _ynt_ ) . Defi ne _Xt_ as the standardized version of _Yt_ . The generalized DFM of by Forni _et al._ (2005) is given by 



where _ft_ is a _q_ × 1 vector of dynamic factors, while _Ft_ is an _r_ × 1 vector of static factors, with _r_ = _q_ ( _s_ + 1), _B_ ( _L_ ) = _B_ 0 + _B_ 1 _L_ + . . . + _BsL_<sup>_s_</sup> is an _n_ × _q_ factor loadings matrix polynomial of order _s_ and Λ is the factor loadings matrix related to static factors, _ξt_ is the _n_ × 1 vector of idiosyncratic components. Note that _L_ denotes the lag operator. 

The generalized DFM is a weighted version of the static principal components estimator of Stock and Watson (2002), which exploits information of leads and lags of variables where time series are converted to the frequency domain. However, dynamic principal component analysis (PCA) is a two-sided fi lter. This causes a problem at the end of the sample, making it diffi cult to estimate and forecast the common component since no future observations are available. The generalized DFM solves this problem by proposing a two-step approach. In the fi rst step, it relies on the dynamic approach in the estimation of the covariance matrices of the common and idiosyncratic component (at all leads and lags) through an inverse Fourier transform of the spectral density matrices. It involves estimating the eigenvalues and eigenvectors decomposition of the spectral density matrix for _Xt_ , Σ<sup>ˆ</sup> ( _θ_ ) with rank _q_ , corresponding to the _q_ largest eigenvalues. For each frequency, − _π_ < _θ_ < _π_ , the spectral density matrix of _Xt_ can be decomposed into the spectral densities of the common and the idiosyncratic component, Σ( _θ_ ) = Σ _χ_ ( _θ_ ) + Σ _ξ_ ( _θ_ ). Hence the estimated spectral density matrix of common component Σ<sup>ˆ</sup> _χ_ ( _θ_ ) can be constructed. In the second step, this information is used to compute _r_ linear combinations of _Xt_ that maximizes the contemporaneous covariance matrices estimated explained by the common factors, estimated in the fi rst step. Further, it reduces the idiosyncratic noise in the common factor space to a minimum, by selecting the variables with the highest common/idiosyncratic variance ratio. This step is a one-sided approach and is only used to estimate and forecast the common component. 

For forecasting purposes, we adopt the method of Boivin and Ng (2005). The forecasting equation is as follows: 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

_S. Das, R. Gupta and A. Kabundi_ 



where _χˆt_ + _h_ is obtained by artifi cially projecting _χt_ + _h_ on the estimated dynamic factor, _F_<sup>_ˆ_</sup> _t_ obtained from _ˆ_ ′ (1), such that _χt_ + _h_ = Γ<sup>ˆ</sup> _χ_ ( _k_ ) _Z_ ( _Z_ ′Σ<sup>ˆ</sup> _Z_ )<sup>−1</sup> _Z Xt_ , _Z_ is the _r_ generalized eigenvectors of Γ<sup>ˆ</sup> _χ_ ( _k_ ) with respect to Γ<sup>ˆ</sup> _ξ_ ( _k_ ) under normalization _Z_ ′Γ<sup>ˆ</sup> _χ_ (0) _Z_ = 1, and Γ<sup>ˆ</sup> _χ_ ( _k_ ) and Γ<sup>ˆ</sup> _ξ_ ( _k_ ) are covariance matrices of common and ′ _ˆ_ idiosyncratic components at different leads and lags. Since _F_<sup>_ˆ_</sup> _t_ = _Z Xt_ , then _χt_ + _h_ = Γ<sup>ˆ</sup> _χ_ ( _θ_ ) _Z_ ( _Z_ ′Σ<sup>ˆ</sup> _Z_ )<sup>−1</sup> _F_<sup>_ˆ_</sup> _t_ . 

## VECTOR AUTOREGRESSIVE (VAR) MODELS 

In this study, the generalized DFM is our benchmark model. To evaluate the forecasting performance of the DFM we consider alternative models: in our case, the unrestricted classical VAR, BVARs based on the Minnesota prior, and the SBVARs based on the FOSC and RWA priors. This section outlines the basics of the above-mentioned competing models. 

## **Classical VARs** 

The VAR model, as suggested by Sims (1980), can be written as follows: 



where _y_ is an _n_ × 1 vector of variables being forecast; _A_ ( _L_ ) is an _n_ × _n_ polynomial matrix in the backshift operator _L_ with lag length _p_ , i.e., _A_ ( _L_ ) = _A_ 1 _L_ + _A_ 2 _L_<sup>2</sup> + . . . + _A_ p _L_<sup>_p_</sup> ; _A_ 0 is an _n_ × 1 vector of constant terms; and _ε_ is an _n_ × 1 vector of error terms. In our case, we assume that _εt_ ≈ _N_ (0, _σ_<sup>2</sup> _In_ ), where _In_ is an _n_ × _n_ identity matrix. The VAR model is estimated based on ordinary least squares (OLS) and forecasting is straightforward (See Hamilton, 1994, ch. 11). 

## **Non-spatial Bayesian VARs** 

The BVAR model, on the other hand, as described in Litterman (1981), Doan _<u>et al.</u>_ <u>(1984), Todd</u> (1984), Litterman (1986), and Spencer (1993), imposes priors on the coeffi cients of the VAR model. Besides a diffuse prior on the constants, the means of the prior, popularly called the Minnesota prior, take the following form: 



where _βi_ denotes the coeffi cients associated with the lagged dependent variables in each equation of the VAR, while _βj_ represents any other coeffi cient. The specifi cation of the standard deviation of the distribution of the prior imposed on variable _j_ in equation _i_ at lag _m_ , for all _i_ , _j_ and _m_ , denoted by _S_ 1( _i_ , _j_ , _m_ ), is specifi ed as follows: 



_ˆ_ with _F_ ( _i_ , _j_ ) = 1, if _i_ = _j_ and _kij_ otherwise, with (0 ≤ _kij_ ≤ 1); _g_ ( _m_ ) = _m_<sup>−</sup><sup>_d_</sup> , _d_ > 0. Note that _σi_ is the estimated standard error of the univariate autoregression for variable _i_ . The ratio _σˆi_ / _σˆj_ scales the 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

Copyright © 2010 John Wiley & Sons, Ltd. 

_Forecasting Regional House Price Infl ation_ 

variables to account for differences in the units of measurement, and hence causes specifi cation of the prior without consideration of the magnitudes of the variables. The term _w_ indicates the overall tightness and is also the standard deviation on the fi rst own lag, with the prior getting tighter as we reduce the value. The parameter _g_ ( _m_ ) measures the tightness on lag _m_ with respect to lag 1, and is assumed to have a harmonic shape with a decay factor of _d_ , which tightens the prior on increasing lags. The parameter _F_ ( _i_ , _j_ ) represents the tightness of variable _j_ in equation _i_ relative to variable _i_ , and by increasing the interaction, i.e., the value of _kij_ , we can loosen the prior. Note that the overall tightness ( _w_ ) and the lag decay ( _d_ ) hyperparameters used in the standard Minnesota prior have values of 0.1 and 1.0, respectively, while _kij_ = 0.5 implies a weighting matrix ( _F_ ) with 1.0 on the diagonals and 0.5 as the off-diagonal elements. 

## **Spatial Bayesian VARs** 

Given that the Minnesota prior treats all variables in the VAR, except for the fi rst own lag of the dependent, in an identical manner, several attempts have been made to alter this fact. Usually, this has boiled down to increasing the value of the overall tightness ( _w_ ) hyperparameter from 0.10 to 0.20, so that the larger value of _w_ can allow for more infl uence from other variables in the model. In addition, as proposed by Dua and Ray (1995), we also try out a prior that is even more loose, specifi cally with _w_ = 0.30 and _d_ = 0.50. Alternatively, LeSage and Pan (1995) have suggested the construction of the weight matrix based on the FOSC, which implies the creation of a non-symmetric _F_ matrix that emphasizes the importance of the variables from the neighboring states/provinces more than those of the non-neighboring states/provinces. Lesage and Pan (1995) suggest the use of a value of unity on the diagonal elements of the weight matrix, as in the Minnesota prior, as well as in place(s) that correspond to the variable(s) from other state(s)/province(s) with which the specifi c state in consideration has common order(s). However, for the elements in the _F_ matrix that corresponds to variable(s) from state(s)/province(s) that are not immediate neighbor(s), Lesage and an (1995) propose a value of 0.1. (See the Appendix for further details regarding the construction of the _F_ matrix based on FOSC.) 

In addition to the FOSC-based prior, LeSage and Krivelyova (1999) have also put forth another approach to remedy the equal treatment nature of the Minnesota prior by the RWA prior. This involves both the prior means and the variances based on a distinction made between important variables (like house price infl ation of neighboring metropolitan area(s)), and unimportant variables (like house price infl ation of non-neighboring metropolitan area(s)), in each equation of the VAR model. To understand the motivation behind the design of the prior means, consider the weight matrix _F_ for the VAR consisting of house price infl ation of the fi ve metropolitan areas. Retaining the ordering of the fi ve metropolitan areas as outlined in the FOSC prior, the weight matrix contains values of unity in positions associated with the house price infl ation(s) of neighboring metropolitan area(s), i.e., for important variables in each equation of the VAR model, while zero values are assigned to the unimportant variables, i.e., house price infl ation of non-neighboring metropolitan area(s), with neighbors and non-neighbors identifi ed as discussed under the FOSC prior. As with the Minnesota prior, we continue to have a value of one on the main diagonal of the _F_ matrix, which is then standardized to a matrix _C_ , so that the rows sum to unity and we can consider the random walk with drift, which averages over the important variables in each equation _i_ of the VAR. (See the Appendix for further details on the design of the _F_ and _C_ matrices under RWA prior. The prior on the standard deviations for the RWA-based model has also been outlined in the Appendix.) 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

_S. Das, R. Gupta and A. Kabundi_ 

## **Estimation of BVARs** 

Finally, the BVARs and the SBVARs, based on the FOSC and the RWA priors, are estimated using Theil’s (1971) mixed estimation technique (See Hamilton, 1994, pp. 360–362). In each equation of the different types of VARs, there are 41 parameters including the constants, given the fact that the model is estimated with eight lags of each variable, which are essentially the house price infl ation (percentage change in house prices) of the fi ve metropolitan areas. All data on house price infl ation are seasonally adjusted, before being converted to house price infl ation, in order to ( _inter alia_ ) address the fact that, as pointed out by Hamilton (1994, p. 362), the Minnesota-type priors are not well suited for seasonal data. The choice of eight lags is based on the unanimity of the sequential modifi ed LR test statistic, Akaike information criterion (AIC) and the fi nal prediction error (FPE) criterion. 

The fi ve-variable VAR, BVAR and SBVAR models for an initial prior are estimated for the period of 1980:1 to 2000:4 and then forecast from 2001:1 through to 2006:4. Since we use eight lags, the initial eight quarters of the sample 1980:1 to 1981:4 are used to feed the lags. We generate dynamic forecasts, as would naturally be achieved in actual forecasting practice. The models are re-estimated each quarter over the out-of-sample forecast horizon in order to update the estimate of the coeffi - cients, before producing the four-quarters-ahead forecasts. This iterative estimation and four-stepsahead forecast procedure was carried out for 24 quarters, with the fi rst forecast beginning in 2001:1. This experiment produced a total of 24 one-quarter-ahead forecasts, 24 two-quarters-ahead forecasts, and so on, up to 24 four-steps-ahead forecasts. The RMSEs for the 24 quarter 1 through quarter 4 forecasts, for the period 2001:1 to 2006:4, are then calculated and compared for the house price infl ation of the fi ve metropolitan areas obtained from that of the generalized DFM. Note that if _At_ + _n_ denotes the actual value of a specifi c variable in period _t_ + _n_ and _tFt_ + _n_ is the forecast made in period _t_ for _t_ + _n_ , the RMSE statistic can be defi ned as 



For _n_ = 1, the summation runs from 2001:1 to 2006:4, and for _n_ = 2 the same covers the period of 2001:2 to 2006:4, and so on. 

## DATA 

We study the South African house price data empirically. As in Burger and Van Rensburg (2008) and Gupta and Das (2008), we do not consider the residential market in general; rather, we subdivide the market in terms of size and price of the houses. Specifi cally, we use the ABSA (one of the leading South African private banks) house price index, which distinguishes between three price categories, expressed in the domestic currency rand (R), as luxury houses (R2.6 million to R9.5 million), middlesegment houses (R226,000 to R2.6 million) and affordable houses (R226,000 and below). Further, the middle-segment category has three subcategories based on size (measured by square meters of house): small (80–140 m<sup>2</sup> ), medium (141–220 m<sup>2</sup> ) and large (221–400 m<sup>2</sup> ). Given that regional house price infl ation data are only available for the middle-segment houses, we restrict our study to this category. Although ABSA reports data for both metropolitan and non-metropolitan areas, the availability is limited and lacks clarity regarding the area of coverage, especially for the rural areas. We thus limit our analysis to the fi ve major metropolitan areas of South Africa. 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

_Forecasting Regional House Price Infl ation_ 

Besides the 15 house price series (fi ve metropolitan areas for each of the three middle-segment houses), the dataset contains 267 quarterly series of South Africa, ranging from real, nominal, and fi nancial sectors; intangible variables, such as confi dence indices and survey variables, and additionally to national variables; we also use a set of global variables such as commodity industrial inputs price index and crude oil prices. The data comprise series of major trading partners such as Germany, the UK and the USA. All series are seasonally adjusted. The more powerful Dickey–Fuller generalized least squares (DF-GLS) test of Elliott _<u>et al.</u>_ <u>(1996) is used to assess the degree of integration</u> of all series. All non-stationary series are made stationary through differencing. The Schwarz information criterion is used to select the appropriate lag length so that no serial correction is left in the stochastic error term. Where there were doubts about the presence of unit root, the KPSS test (Kwiatowski _<u>et al.</u>_ <u>, 1992), with the null hypothesis of stationarity, was applied. All series are stan-</u> dardized to have a mean of zero and a constant variance. The in-sample period contains data from 1980:1 to 2000:4, while the out-of-sample set is 2001:1 to 2006:4. 

There are various statistical approaches in determining the number of factors in the DFM. The <u>Bai and Ng (2002) approach suggests fi ve static factors in our dataset, while the Bai and Ng (2007)</u> approach suggests two dynamic factors. The approach of Forni _et al._ (2000) also suggests two dynamic factors, with the fi rst two dynamic principal components explaining approximately 99% of the variation. 

## EVALUATION OF FORECAST ACCURACY 

To evaluate the accuracy of forecasts generated by the DFM, we compare its performance with the alternative models using the same statistic, namely the RMSE. Given that there are seven alternative models, we use a parsimonious approach while reporting the results in Tables I–III.<sup>1</sup> We compare each of the one- to four-quarters-ahead forecasts generated by the DFM with those from a specifi c- type of VAR model that performs the best, in terms of average RMSEs<sup>2</sup> for one- to four-quartersahead forecasts, within the category of VAR models for a specifi c region, under a particular category of housing, over the out-of-sample horizon of 2001:1 to 2006:4.<sup>3</sup> Note the values for these hyperparameters are based on the ranges suggested by LeSage (1999). The main observations can be summarized as follows: 

- _Large middle-segment houses_ . From Table I we observe that for the category of large middlesegment houses the DFM, barring the cases of third- and fourth-quarter-ahead forecasts for Port Elizabeth, and fi rst-, third- and fourth-quarter-ahead forecasts for Cape Town, outperforms the best-performing model within the VAR category. Amongst the alternative VARs, the SBVAR model based on the FOSC prior is the standout performer for all the metropolitan areas, except 

> 1 In Tables I–III, the metropolitan areas have been abbreviated to ECAP, JOBU, KWAZ, PRET, and WCAP for Eastern Cape (Port Elizabeth), Johannesburg, KwaZulu Natal (Durban Unicity), Pretoria, and Western Cape (Cape Town), respectively. 

> 2 The decision to use average RMSEs for choosing the best-performing VAR model within this category is standard practice. For two recent examples, refer to Liu _et al._ (2009a,b). However, all the other forecasting results for the alternative types of VAR models will be made available upon request. 

> 3 Note that for the SBVAR model based on the RWA prior that did best amongst other SBVAR models consistently for all house sizes and majority of the metropolitan areas had the following values of the hyperparameters: _σc_ = 0.3, η = 8, and ρ = 1 (refer to the Appendix for further details). 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

## _S. Das, R. Gupta and A. Kabundi_ 

Table I. RMSEs for large middle-segment houses (2001:1 to 2006:4) 

|Region|Model||Quarter|s ahead||
|---|---|---|---|---|---|
|||1|2|3|4|
|ECAP|DFM|5.1070|5.2891|5.4843|5.7861|
|||(−3.4843***)|(−2.8597***)|(1.4047)|(1.4125)|
||SBVAR1|11.9550|9.1444|4.1622|4.3177|
|JOBU|DFM|2.0938|2.8122|2.7223|2.5270|
|||(−1.9688**)|(−4.1425***)|(−3.3087***)|(−3.7419***)|
||SBVAR1|4.1098|9.4896|7.0795|7.3525|
|KWAZ|DFM|4.8798|5.3617|5.2879|5.0944|
|||(−3.0842***)|(−2.8666***)|(−1.0528)|(−3.4439***)|
||BVAR1|10.2062|8.4188|5.3277|9.9729|
|PRET|DFM|2.3077|3.4558|2.4556|2.5799|
|||(−1.9613**)|(−2.6433***)|(−3.1497***)|(−4.2843***)|
||SBVAR1|4.9353|7.0118|6.4439|13.3315|
|WCAP|DFM|2.3846|2.3843|2.8635|2.9397|
|||(1.2997)|(−1.1664)|(1.3863)|(1.6584*)|
||SBVAR1|2.0253|2.5750|2.4713|1.2203|



_Note_ : DFM, dynamic factor model; BVAR1, BVAR model based on the standard Minnesota prior with _w_ = 0.1, _d_ = 1.0; SBVAR1, spatial BVAR based on the fi rst-order spatial contiguity (FOSC) prior. Numbers in parentheses represent the Diebold and Mariano (1995) tests statistic, with asterisks indicating signifi cance at ***1%, **5% and *10% levels, respectively. 

Table II. RMSEs for medium middle-segment houses (2001:1 to 2006:4) 

|Region|Model||Quarter|s ahead||
|---|---|---|---|---|---|
|||1|2|3|4|
|ECAP|DFM|3.3023|4.0077|3.5462|3.5971|
|||(−2.6537***)|(−3.2237***)|(−1.9832**)|(−4.7779***)|
||BVAR1|7.7311|10.0543|5.1025|13.4312|
|JOBU|DFM|2.3033|2.4067|2.4604|2.4403|
|||(−4.7008***)|(−1.7855*)|(−2.0133**)|(−4.2055***)|
||BVAR3|10.0155|3.9097|7.3349|9.1191|
|KWAZ|DFM|3.3450|4.1419|4.0736|4.0927|
|||(1.0634)|(−1.8226*)|(−3.9921***)|(−3.2368***)|
||SBVAR1|3.1487|6.2767|8.9245|8.0334|
|PRET|DFM|1.6371|1.7522|1.7688|1.7456|
|||(−1.6876*)|(−1.9747**)|(−1.9513**)|(−1.6536*)|
||BVAR2|3.6546|4.4684|4.4186|3.3969|
|WCAP|DFM|2.0675|2.1097|2.2301|2.3201|
|||(2.4400**)|(2.4469**)|(1.9381**)|(2.4345**)|
||BVAR1|0.4921|0.3304|0.9992|0.6025|



_Note_ : See note to Table I. In addition, BVAR2 and BVAR3 are the BVAR models based on the standard Minnesota prior with _w_ = 0.2, _d_ = 1.0 and _w_ = 0.3, _d_ = 0.5, respectively. 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

_Forecasting Regional House Price Infl ation_ 

Table III. RMSEs for small middle-segment houses (2001:1 to 2006:4) 

|Region|Model||Quarter|s ahead||
|---|---|---|---|---|---|
|||1|2|3|4|
|ECAP|DFM|4.7737|5.1827|4.8109|4.7781|
|||(−2.6052***)|(−3.2060***)|(−4.6989***)|(−3.9490***)|
||SBVAR1|9.5527|15.3944|19.7870|13.2875|
|JOBU|DFM|2.8092|2.7369|3.2401|3.6976|
|||(−1.9640**)|(−2.7922***)|(−2.3022**)|(−3.1810***)|
||SBVAR1|4.5326|7.3926|6.1887|12.9415|
|KWAZ|DFM|4.1300|4.8269|4.3750|4.4162|
|||(−1.7266*)|(−3.5030***)|(−1.6997*)|(−3.0940***)|
||BVAR1|5.9458|13.0952|5.4940|9.8042|
|PRET|DFM|2.4921|2.9355|2.6855|2.5327|
|||(−1.9651**)|(−2.1687**)|(1.6355)|(−2.0016**)|
||SBVAR1|4.3445|4.7499|1.7359|4.7650|
|WCAP|DFM|2.2799|2.5541|2.7095|2.6751|
|||(−1.6604*)|(1.6566*)|(1.2202)|(−1.1130)|
||SBVAR1|3.5421|1.7169|2.0921|2.9398|



_Note_ : See note to Table 1. 

- for Durban Unicity under the KwaZulu Natal metropolitan area, which in turn is forecast with the lowest errors by the BVAR model with _w_ = 0.1, _d_ = 1.0. 

- _Medium middle-segment houses_ . From Table II we learn that the DFM outperforms the bestperforming model within the VAR category in four of the fi ve metropolitan areas, with the exception of the fi rst-quarter-ahead forecast for the Durban Unicity and all of the one- to four-quarters-ahead forecasts for Cape Town, for which the BVAR model with _w_ = 0.1, _d_ = 1.0 does the best. Unlike the case of large middle-segment housing, there does not exist a unique overwhelmingly favorite VAR model across all of the fi ve metropolitan areas. The BVAR model with _w_ = 0.1, _d_ = 1.0 performed the best for the Eastern and Western Capes, while the BVARs with _w_ = 0.2, _d_ = 1.0 and _w_ = 0.3, _d_ = 0.5 stood out for Johannesburg and Pretoria, respectively. The SBVAR model based on the FOSC prior was the best-performing model for Durban Unicity. 

- _Small middle-segment houses_ . From Table III we observe that, as with the large and medium middle-segment housing, the DFM in general stands out as the best-suited model for forecasting house price infl ation in all fi ve metropolitan areas for all of the one- to four-quarters-ahead forecasts. The minor exceptions are the third-quarter-ahead forecast for Pretoria and the second- and third-quarter-ahead forecasts for Cape Town. Amongst the VARs, the SBVAR model based on the FOSC prior produces the lowest RMSEs for four of the fi ve metropolitan areas, with the exception of KwaZulu Natal metropolitan area, for which the BVAR model with _w_ = 0.3, _d_ = 0.5 outperforms the other VAR models. Thus, as with the large middle-segment housing, the SBVAR model based on the FOSC prior is the overwhelming favorite within the category of VAR models. 

<u>Gupta and Das (2008) observed that the spatial models tended to outperform the other models for</u> large middle-segment houses, while the unrestricted VAR and the BVAR models produced lower average out-of-sample forecast errors for middle and small middle-segment houses, respectively. In 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

## _S. Das, R. Gupta and A. Kabundi_ 

our case though, in general, and especially for the large and small middle-segment houses, the SBVAR model based on the FOSC stands out once we take the DFM out of consideration. 

When we take into account the cross-model tests of forecast accuracy proposed by Diebold and <u>Mariano (1995), in the majority of cases where the DFM outperforms a specifi c type of the VAR</u> model the statistics are signifi cant at least at the 10% level. The exceptions are the third- and secondquarter-ahead forecasts for Pretoria and Western Cape, respectively, under the large middle-segment housing, and the fourth-quarter-ahead forecast for Cape Town for the small middle-segment houses. At the same time, in most cases where the alternative model tends to outperform the DFM, the Diebold–Mariano (1995)<sup>4</sup> test statistics are insignifi cant. 

## CONCLUSIONS 

This paper analyzes whether the wealth of information contained in the DFM framework can be useful in forecasting regional house price infl ation. As a case study illustration we use the DFM to predict house price infl ation in fi ve metropolitan areas of South Africa, namely Cape Town, Durban, Johannesburg, Port Elizabeth and Pretoria, using quarterly data over the period 1980:1 to 2006:4. The in-sample period contains data from 1980:1 to 2000:4, and the out-of-sample forecasts are based on one- to four-quarter-ahead forecasts over a 24-quarter forecasting horizon covering 2001:1 to 2006:4. The forecast performance of DFM is evaluated in terms of the RMSEs by comparing it with SBVAR models, based on the FOSC and the RWA priors, besides non-spatial models like the VAR and BVAR models with the Minnesota prior, estimated merely based on house price infl ation of the fi ve above-mentioned metropolitan areas of South Africa. Our results thus indicate that a data-rich DFM, in general, is best suited in forecasting regional house price infl ation when compared to the alternative VARs. 

## APPENDIX: FOSC- AND RWA-BASED MINNESOTA PRIORS 

## **FOSC prior** 

_ˆ_ Given equation (5) in the text, i.e., _S_ 1( _i_<sup>,</sup> _j_<sup>,</sup> _m_ ) = [ _w_ × _g_ ( _m_ ) × _F_ ( _i_ , _j_ )] σ<sup>σ</sup> _ˆ_ _<u>ij</u>_<sup>, and referring to the</sup> 

provincial map of South Africa given in Figure 1, the design of the _F_ matrix based on the FOSC prior, discussed in the main text, given the alphabetical ordering<sup>5</sup> of the fi ve metropolitan areas as the Eastern Cape Metropolitan area (Port Elizabeth/Uitenhage), Greater Johannesburg, the KwaZulu Natal Metropolitan area (Durban Unicity), Pretoria and the Western Cape Metropolitan area (Cape Town), can be formalized as in equation (A1). Note that each element of _F_ represents the relationship between the respective pair of location, with 1.0 representing pairs that are neighbors, while 

> 4 If { _et_ DFM} _Tt_ =1<sup>denotes the forecast errors from the DFM model and {</sup><sup>_e_</sup> ALT _t_ } _Tt_ =1<sup>denotes the forecast errors</sup> from the alternative model, the Diebold and Mariano (1995) test statistic is then defi ned as: _s_ =<sup>1</sup> , where _l_ is the sample σ _l_ 

> mean of the ‘loss differentials’, { _lt_ }<sup>_T_</sup> _t_ =1<sup>, using</sup><sup>_l_</sup> _t_<sup>= (</sup><sup>_e_</sup> _t_ DFM)2 − ( _e_ ALT _t_ )2 for all _t_ = 1, 2, 3, . . . , _T_ , and _σl_ is the standard error of _l_ . The _s_ statistic is asymptotically distributed as a standard normal random variable and can be estimated under the null hypothesis of equal forecast accuracy, i.e., _l_ = 0. Therefore, a negative value of _s_ would suggest that the DFM model outperforms the alternative model in terms of out-of-sample forecasting. 

> 5 It must, however, be pointed out that alternative ordering of the fi ve metropolitan areas do not affect our fi nal results in any way. 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

_Forecasting Regional House Price Infl ation_ 



Figure 1. Provincial Map of South Africa. Source: CSIR, Pretoria, South Africa 

0.1 represents non-neighbors. To illustrate the design of the _F_ matrix, let us, for example, consider the fi rst row of the matrix that corresponds to Port Elizabeth/Uitenhage in the Eastern Cape province. Eastern Cape has the provinces of KwaZulu Natal and Western Cape as immediate neighbors; hence the metropolitan areas of Durban Unicity and Cape Town that fall under these two provinces, respectively, have been treated as neighbors of Port Elizabeth/Uitenhage. Thus, speaking formally in terms of the entries in the different columns of the fi rst row of the _F_ matrix, we have a value of 1.0 on the third and fi fth off-diagonal elements, besides the diagonal, since these two entries correspond to Durban Unicity and Cape Town, respectively. Since Johannesburg and Pretoria belong to the Gauteng province, which is not an immediate neighbor of the Eastern Cape province, the second and fourth columns of the fi rst row of the _F_ matrix have a value of 0.1. We follow a similar reasoning for the remaining entries of the _F_ matrix, realizing that the immediate neighbor of Johannesburg is Pretoria and vice versa, while Port Elizabeth/Uitenhage is the only metropolitan area next to Durban Unicity and Cape Town. Mathematically, we have 



Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

## _S. Das, R. Gupta and A. Kabundi_ 

## **RWA prior** 

To distinguish the _F_ matrix under the RWA prior, discussed in the main text, from that in equation (A1), we denote it as _F_<sup>1</sup> as follows: 



The weight matrix given above is then standardized so that the rows sum to unity. Formally, we can write the standardized _F_<sup>1</sup> matrix, _C_ , as follows: 



Formally: 



On expanding equation (A4), we observe that multiplying _yjt_ −1 containing the house price growth rates of fi ve metropolitan areas at _t_ − 1 by the matrix _C_ would produce a set of explanatory variables for each equation of the VAR equal to the mean of observations from the important variables (neighboring house prices) in each equation _i_ at _t_ − 1. In other words, after normalization of the rows, one needs to calculate the neighborhood weighted average of the variable _yt_ from previous periods. This also suggests that the prior mean for the coeffi cients on the fi rst own-lag of the important variables is equal to 1/ _ci_ , with _ci_ being the number of important variables in a specifi c equation _i_ of the VAR model. However, as in the Minnesota prior, the RWA prior uses a prior mean of zero for the coeffi cients on all lags, except for the fi rst own lags, and _δ_ is estimated based on a diffuse prior. 

Note that the RWA approach of specifying prior means requires the variables to be scaled to have similar magnitudes, as it does not make much intuitive sense to suggest that the value of a variable at _t_ is equal to the average of values from the important variables at _t_ − 1. This transformation is not much of an issue as the data on the variables, in our case the house price infl ation, can always be expressed as percentage change, or annualized growth rates, thus meeting the similar-magnitude requirements of the RWA prior. 

As proposed by LeSage and Krivelyova (1999), a fl exible form of the RWA prior standard deviations, _S_ 2( _i_ , _j_ , _m_ ), for a variable _j_ in equation _i_ at lag length _m_ , is as follows: 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

_Forecasting Regional House Price Infl ation_ 



where 0 < _σc_ < 1; _η_ > 1 and 0 < _ρ_ ≤ 1. For the variables _j_ = 1, . . . , _n_ in equation _i_ , those variables that are important in explaining the movements in variable _i_ ( _j_ ∈ _C_ ), the prior mean for the lag length of 1 is set to the average of the number of important variables in equation _i_ , and to zero for the unimportant variables ( _j_ ∉ _C_ ). With 0 < _σc_ < 1, the prior standard deviation for the fi rst own-lag imposes a tight prior mean to refl ect averaging over important variables. For important variables at lags greater than one, the variance decreases as _m_ increases, but the restriction of η > 1 allows for the zero prior means on the coeffi cients of these variables to be imposed loosely. Finally, we use ρ _σc_ / _m_ for lags on unimportant variables, which has prior means of zero, to indicate that the variance decreases as _m_ increases. In addition, with 0 < ρ ≤ 1, we impose the zero means on the unimportant variables with more certainty. 

## ACKNOWLEDGEMENTS 

Prof. Alain Kabundi gratefully acknowledges the fi nancial support from Economic Research Southern Africa (ERSA), South Africa. 

## REFERENCES 

<u>Abraham JM, Hendershott PH. 1996. Bubbles in metropolitan housing markets.</u> _<u>Journal of Housing Research</u>_ **<u>7</u>** <u>: 191–207. Bai J, Ng S. 2002. Determining the number of factors in approximate factor models.</u> _<u>Econometrica</u>_ **<u>70</u>** <u>: 191–221. Bai J, Ng S. 2007. Determining the number of primitive shocks in factor models.</u> _<u>Journal of Business and Economic Statistics</u>_ **<u>25</u>** <u>: 52–60.</u> _-_ <u>Bernanke B, Gertler M. 1995. Inside the black box: the credit channel of monetary transmission.</u> _<u>Journal of Eco nomic Perspectives</u>_ **<u>9</u>** <u>: 27–48. Boivin J, Ng S. 2005. Understanding and comparing factor-based forecasts. International Journal of Central Banking</u> **<u>1</u>** <u>: 117–151. Burger P, Van Rensburg LJ. 2008. Metropolitan house prices in South Africa: do they converge?</u> _<u>South African Journal of Economics</u>_ **<u>76</u>** <u>: 291–297. Cho M. 1996. House price dynamics: a survey of theoretical and empirical issues.</u> _<u>Journal of Housing Research</u>_ **<u>7</u>** <u>: 145–172. Diebold FX, Mariano RS. 1995. Comparing predictive accuracy.</u> _<u>Journal of Business and Economic Statistics</u>_ **<u>13</u>** <u>: 253–263. Doan T, Litterman RB, Smis C. 1984. Forecasting and conditional projection using realistic prior distributions.</u> _<u>Econometric Reviews</u>_ **<u>3</u>** <u>: 1–144. Dua P, Ray SC. 1995. A BVAR model for the Connecticut economy.</u> _<u>Journal of Forecasting</u>_ **<u>14</u>** <u>: 167–180.</u> 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

## _S. Das, R. Gupta and A. Kabundi_ 

<u>Elliott G, Rothenberg TJ, Stock J. 1996. Eff cient tests for an autoregressive unit root.</u> _<u>Econometrica</u>_ **<u>64</u>** <u>: 813–836.</u> 

Forni M, Hallin M, Lippi M. Reichlin L. 2000. The generalized dynamic factor model: identifi cation and estimation. _Review of Economics and Statistics_ **82** : 540–554. 

Forni M, Hallin M, Lippi M, Reichlin L. 2003. Do fi nancial variables help forecasting infl ation and real activity in the euro area? _Journal of Monetary Economics_ **50** : 1243–1255. 

Forni M, Hallin M, Lippi M, Reichlin L. 2005. The generalized dynamic factor model: identifi cation and estimation. _Review of Economics and Statistics_ **82** : 540–554. <u>Gupta R, Das S. 2008. Spatial Bayesian methods of forecasting house prices in six metropolitan areas of South Africa.</u> _<u>South African Journal of Economics</u>_ **<u>76</u>** <u>: 298–313. Hamilton JD. 1994.</u> _<u>Time Series Analysis</u>_ <u>(2nd edn). Princeton University Press: Princeton, NJ. International Monetary Fund. 2000.</u> _<u>World Economic Outlook: Asset Prices and the Business Cycle</u>_ <u>. IMF: Washington, DC. Johnes G, Hyclak T. 1999. House prices and regional labor markets.</u> _<u>Annals of Regional Science</u>_ **<u>33</u>** <u>: 33–49. Kwiatowski D, Phillips PCB, Schmidt P, Shin Y. 1992. Testing the null hypothesis of stationarity against the alternative of a unit root: how sure are we that economic time series have a unit root?</u> _<u>Journal of Econometrics</u>_ **<u>54</u>** <u>: 159–178. LeSage JP. 1999. Applied econometrics using MATLAB, 1999. http://www.spatial-econometrics.com/html/ mbook.pdf LeSage JP, Krivelyova A. 1999. A spatial prior for Bayesian autoregressive models.</u> _<u>Journal of Regional Science</u>_ **<u>39</u>** <u>: 297–317. LeSage JP, Pan Z. 1995. Using spatial contiguity as Bayesian prior information in regional forecasting models.</u> _<u>International Regional Science Review</u>_ **<u>18</u>** <u>: 33–53. Litterman RB. 1981.</u> _<u>A Bayesian procedure for forecasting with vector autoregressions</u>_ <u>. Working paper, Federal Reserve Bank of Minneapolis.</u> _-_ <u>Litterman RB. 1986. Forecasting with Bayesian vector autoregressions: f ve years of experience.</u> _<u>Journal of Busi ness and Statistics</u>_ **<u>4</u>** <u>: 25–38. Liu G, Gupta R, Schaling E. 2009a. Forecasting the South African economy: a hybrid-DSGE approach.</u> _<u>Journal of Economic Studies</u>_ <u>(forthcoming). Liu G, Gupta R, Schaling E. 2009b. A New Keynesian DSGE model for forecasting the South African economy.</u> _<u>Journal of Forecasting</u>_ **<u>28</u>** <u>: 387–404.</u> Rapach DE, Strauss JK. 2007. Forecasting real housing price growth in the eighth district states. Federal Reserve Bank of St Louis. _Regional Economic Development_ **3** : 33–42. <u>Rapach DE, Strauss JK. 2009. Differences in housing price forecast ability across U.S. states.</u> _<u>International Journal of Forecasting</u>_ **<u>25</u>** <u>: 351–372.</u> Sims CA. 1980. Macroeconomics and reality. _Econometrica_ **48** : 1–48. <u>Spencer DE. 1993. Developing a Bayesian vector autoregression model.</u> _<u>International Journal of Forecasting</u>_ **<u>9</u>** <u>: 407–421. Stock JH, Watson MW. 2002. Forecasting using principal components from a large number of predictors.</u> _<u>Journal of the American Statistical Association</u>_ **<u>97</u>** <u>: 147–162.</u> Stock JH, Watson MW. 2003. Forecasting output growth and infl ation: the role of asset prices. _Journal of Economic Literature_ **41** : 788–829. <u>Theil H. 1971.</u> _<u>Principles of Econometrics</u>_ <u>. Wiley: New York. Todd RM. 1984. Improving economic forecasting with Bayesian vector autoregression.</u> _<u>Quarterly Review, Federal Reserve Bank of Minneapolis</u>_ **<u>Fall</u>** <u>: 18–29. Topel RH, Rosen S. 1988. Housing investment in the United States.</u> _<u>Journal of Political Economy</u>_ **<u>96</u>** <u>: 718–740.</u> - <u>Vargas Silva C. 2008. The effect of monetary policy on housing: a factor augmented vector autoregression (FAVAR) approach.</u> _<u>Applied Economics Letters</u>_ **<u>15</u>** <u>: 749–752.</u> 

### _Authors’ biographies_ : 

**Sonali Das** is a Senior Researcher (Statistics) at the Council of Scientifi c and Industrial Research, Pretoria. She has published referred papers in both theoretical and applied statistics in areas ranging from health, environment to housing. 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

_Forecasting Regional House Price Infl ation_ 

**Rangan Gupta** is a Professor at the Department of Economics, University of Pretoria. He has published extensively in refereed journals, and his research interests are mainly macroeconomics and time series econometrics. 

**Alain Kabundi** is an Associate Professor in the Department of Economics and Econometrics, University of Johannesburg. He has published extensively in refereed journals, and his research interests are mainly macroeconomics, fi nancial economics and time series econometrics. 

### _Authors’ addresses_ : 

**Sonali Das** , Logistics and Quantitative Methods, CSIR Built Environment, PO Box 395, Pretoria 0001, South Africa. 

**Rangan Gupta** , Department of Economics, University of Pretoria, Pretoria, 0002, South Africa. 

**Alain Kabundi** , Department of Economics, University of Johannesburg, Johannesburg 2006, South Africa. 

Copyright © 2010 John Wiley & Sons, Ltd. 

_J. Forecast_ . (2010) **DOI** : 10.1002/for 

