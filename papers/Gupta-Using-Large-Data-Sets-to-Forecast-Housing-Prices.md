---
title: **Using Large Data Sets to Forecast Housing Prices: A Case Study of Twenty US States***
type: paper
source_pdf: raw/papers/Gupta_Using Large Data Sets to Forecast Housing Prices.pdf
converted: 2026-07-26
---

# **Using Large Data Sets to Forecast Housing Prices: A Case Study of Twenty US States*** 

Rangan Gupta Department of Economics University of Pretoria Pretoria, 0002, SOUTH AFRICA 

Alain Kabundi Department of Economics and Econometrics University of Johannesburg Johannesburg, 2006, SOUTH AFRICA 

Stephen M. Miller** Department of Economics College of Business University of Nevada, Las Vegas Las Vegas, Nevada, USA 89154-6005 _stephen.miller@unlv.edu_ 

## **Abstract** 

We implement several Bayesian and classical models to forecast housing prices in 20 US states. In addition to standard vector-autoregressive (VAR) and Bayesian vector autoregressive (BVAR) models, we also include the information content of 308 additional quarterly series in some models. Several approaches exist for incorporating information from a large number of series. We consider two approaches – extracting common factors (principle components) in a FactorAugmented Vector Autoregressive (FAVAR) or Factor-Augmented Bayesian Vector Autoregressive (FABVAR) models or Bayesian shrinkage in a large-scale Bayesian Vector Autoregressive (LBVAR) models. In addition, we also introduce spatial or causality priors to augment the forecasting models. Using the period of 1976:Q1 to 1994:Q4 as the in-sample period and 1995:Q1 to 2003:Q4 as the out-of-sample horizon, we compare the forecast performance of the alternative models. Based on the average root mean squared error (RMSE) for the one-, two-, three-, and four–quarters-ahead forecasts, we find that one of the factoraugmented models generally outperform the large-scale models in the 20 US states examined in this paper. 

**Keywords:** 

Housing prices, Forecasting, Factor Augmented Models, LargeScale BVAR models 

## **_JEL classification:_** C32, R31 

* We acknowledge the assistance of D. Liu and D. W. Jansen, who provided the data on the 308 macroeconomic indicators, as well as for clarifying all the data related issues. 

** _Corresponding author_ 

**Electronic copy available at: http://ssrn.com/abstract=1406698** 

## 1 **. Introduction** 

This paper considers the dynamics of housing prices and the ability of different pure time-series models to forecast housing prices. The main focus considers how the researcher can incorporate large data sets into forecasting equations, using dynamic factor analysis or shrinking large-scale BVAR models. We illustrate the process using housing prices from the most-populous 20 US states – Arizona, California, Florida, Georgia, Illinois, Indiana, Massachusetts, Maryland, Michigan, Missouri, North Carolina, New Jersey, New York, Ohio, Pennsylvania, Tennessee, Texas, Virginia, Washington, and Wisconsin. 

We begin by searching for evidence of Granger temporal causality between housing prices in the 20 US states. UK housing experts found a “ripple” effect of housing prices that begins in the Southeast UK and proceeds toward the Northwest. Meen (1999) outlines four different theories to justify the ripple effect – migration, equity conversion, spatial arbitrage, and exogenous shocks with different timing of spatial effects.<sup>1</sup> The ripple effect receives little support in the US. For example, most analyses relate to a given geographic housing market, such as a metropolitan area (Tirtirglou 1992; Clapp and Tirtirglou 1994; and Gupta and Miller 2009b). More recent evidence across census regions also exists, which may reflect the fourth of Meen’s explanations (Pollakowski and Ray, 1997; Meen 2002). Gupta and Miller (2009a) find evidence of a ripple effect from Los Angeles to Las Vegas and from Las Vegas to Phoenix, which they attribute to the first three of Meen’s (1999) rationalizations. Our study adds to the evidence of ripple effects in the US. 

> 1 The migration explanation requires that households move from one metropolitan area to another to take advantage of regional housing price differences. The equity conversion explanation requires that residents of one region sell their home and move to a lower cost region where they can buy a similar quality home for a lower price and pocket the residual equity. The spatial arbitrage explanation means that investors acquire properties in lower priced regions, where higher anticipated return on housing investment exist. The exogenous shocks explanation implies that if the determinants of housing prices in different regions experience a correlated movement, then housing prices will also exhibit the same correlated movement. 

2 

**Electronic copy available at: http://ssrn.com/abstract=1406698** 

We next examine the explanatory power of including information from a large set of economic variables, using dynamic factors or Bayesian shrinkage approaches. More specifically, we compare the out-of-sample forecasting performance of various time-series models – vector autoregressive (VAR), factor augmented VAR (FAVAR), and various Bayesian time-series models. For the Bayesian models, we estimate Bayesian VAR (BVAR), factor augmented BVAR (FABVAR), and large-scale BVAR (LBVAR) models that include spatial and causality priors (LeSage 2004, Gupta and Miller 2009a, 2009b). The factor-augmented models, frequently with spatial priors, generally perform the best across the 20 states, using the average root-meansquared-error (RMSE) criteria. Large-scale models usually come in a close second to the factoraugmented models, and actually outperform the factor-augmented models in two states. Finally, the models that exclude the information from the large set of data come in a distant third in forecast performance, implying that the macroeconomic fundamentals partly drive housing prices. 

We organize the rest of the paper as follows. Section 2 provides a brief review of the literature on using large data sets in forecasting models. Section 3 discusses the literature on forecasting housing prices. Section 4 specifies the various time-series models estimated and used for forecasting. Section 5 discusses the data and the results. Section 6 concludes. 

## **2. Forecasting with Large Data Sets** 

For forecasting purposes, time-series models generally perform as well as or better than dynamic structural econometric specifications. Zellner and Palm (1974) provide the theoretical rationalization.<sup>2</sup> An important issue involves determining how additional information can or 

> 2 Any dynamic structural model implicitly generates a series of univariate time-series models for each endogenous variable. The dynamic structural model, however, imposes restrictions on the parameters in the reduced-form timeseries specification. Dynamic structural models prove most effective in performing policy analysis, albeit subject to the Lucas critique. Time-series models prove most effective at forecasting. That is, in both cases errors creep in 

3 

cannot improve the forecasting performance over a simple univariate autoregressive or autoregressive-moving-average representation. 

A simple approach uses an autoregressive distributed lag (ARDL) model (Stock and Watson 1999, 2003, 2004). That is, the researcher runs an ARDL, or transfer function, model, where the variable to forecast enters as an autoregressive process and one driver variable enters as a distributed lag. The researcher compares the baseline model, the pure autoregressive specification forecasts with the forecasts for the ARDL specification. Extending this further, the researcher can repeat the process for a whole series of potential driver variables. In this extended case, one aggregates across all of the individual forecasts to generate the combined forecast. Combination forecasts range from simple means or medians to more complicated principalcomponents- or mean-square-forecast-error-weighted forecasts. 

Another method uses “atheoretical” VAR models. These models do not impose exogeneity assumptions on the included variables. Unlike the single-equation ARDL model, the VAR approach assumes that lagged values of each variable may provide valuable information in forecasting each endogenous variable. VAR models, however, face problems of overparameterization, since the number of parameters to estimate increases dramatically with additional variables or additional lags in the system. Given this problem, one approach for using more data in the VAR model involves the extraction of common factors from a large data set that researchers can then add to the VAR specification (Bernanke, Boivin, and Eliazs 2005, Stock and Watson 2002, 2005). Adding a couple of common factors from the large dataset to a VAR system economizes on the number of new parameters to estimate. 

> whenever the researcher makes a decision about the specification. Clearly, more researcher decisions relate to a dynamic structural model than a univariate time-series model, suggesting that fewer errors enter the time-series model and allowing the model to produce better forecasts. 

4 

Bayesian VAR (BVAR) models address the over-parameterization problem by estimating a small number of hyper-parameters in the specification that define all the parameters in the system. Since the Bayesian approach already solves the over-parameterization problem, researchers can add a large set of variables to the estimation of a BVAR system, obviating the need to extract common factors. Nothing prevents, however, the extraction of common factors from the large set of macroeconomic variables to include in a factor-augmented VAR system, which we also do. 

The ADRL method uses information in the large dataset one variable at a time and then aggregates across all forecasts. As a result, this approach does not differentiate between common factors and non-common factors in the large dataset. Each exhibits the same effect on the forecast, over and above the autoregressive part of the model. In the factor-augmented approach, the researcher potentially leaves information on the table by only extracting the common factor information and leaving the remaining information out of the analysis. On the other hand, the Bayesian approach, includes all the information from the large set of data, but restricts the estimation by imposing conditions on the parameters of the estimating equation. In sum, all methods introduce restrictions on the way information from the large dataset affects the estimation process. Thus, any of the individual approaches may lead to better forecasts _a priori_ . 

In this paper, we consider the factor-augmented and large-scale Bayesian methods for incorporating the information from a large dataset. These methods provide the natural extension of the VAR and BVAR models. The ARDL model involves a single-equation, whereas the VAR and BVAR models involve multiple equations. Thus, we exclude the ARDL approach from our analysis. 

5 

## **3. Forecasting Housing Prices** 

Traditionally, the housing market and its cycle played an important role in understanding the business cycle. More recently, several authors argue that asset prices help forecast both inflation and output (Forni _et al._ , 2003; Stock and Watson, 2003, Gupta and Das, 2008a, 2008b and Das _et al._ , 2008a, 2008b). Since homes imbed much individual wealth, housing price movements may provide important signals for consumption, output, and inflation. That is, housing market adjustments play an important role in the business cycle (Iacoviello and Neri, 2008), not only because housing investment proves a volatile component of demand (Bernanke and Gertler, 1995), but also because housing price changes generate important wealth effects on consumption (International Monetary Fund, 2000; ) and investment (Topel and Rosen, 1988). 

In sum, models that forecast real housing price inflation can give policy makers an idea about the future direction of the overall macroeconomy, and hence, can provide important information for designing better and more-appropriate policies. In other words, the housing sector acts as a leading indicator for the real sector of the economy. The recent world-wide credit crunch began with the burst of the housing price bubble, which, in turn, led the real sector of the world’s economy toward an economic slump. 

A large number of economic variables affect housing price growth (Cho, 1996; Abraham and Hendershott, 1996; Johnes and Hyclak, 1999; and Rapach and Strauss, 2007, 2008). For instance, income, interest rates, construction costs, labor market variables, stock prices, industrial production, consumer confidence index, and so on act as potential predictors. 

Rapach and Strauss (2007, 2008) consider forecasting housing prices in states, using a large data set of economic variables. Rapach and Strauss (2007) use an autoregressive distributed lag (ARDL) model framework, containing 25 determinants, to forecast real housing price growth 

6 

for the individual states of the Federal Reserve’s Eighth District – Arkansas, Illinois, Indiana, Kentucky, Missouri, Mississippi, and Tennessee. Given the difficulty in determining _a priori_ the particular variables that prove the most important in forecasting real housing price growth, the authors also use various methods to combine the individual ARDL model forecasts, which result in better forecast of real housing price growth. Rapach and Strauss (2008) perform the same analysis for 20 largest US states based on ARDL models containing large number of potential predictors, including state, regional and national level variables. Once again, the authors reach similar conclusions on the importance of combining forecasts. 

Vargas-Silva (2008a) uses a factor-augmented VAR (FAVAR) model, containing 120 monthly series, to analyze the effect of monetary policy actions on the housing sector of four different regions of the United States. To our knowledge, this is the first attempt to look into the ability of FAVARs in forecasting regional real housing price growth rates.<sup>3</sup> Das _et al._ , (2009) consider the forecasting performance of regional real housing price growth rates in the nine US Census regions, using FAVAR and LBVAR models. They find that the FAVAR models generally outperform the LBVAR models. 

Our paper extends the above mentioned studies, in the sense that we use large-scale models that allow for not only the role of a wide possible set of fundamentals to affect the housing sector, but also spatial and causal influences amongst the prices of the 20 largest US states. 

> 3 Note that Dua and Smyth (1995), Dua and Miller (1996) and Dua _et al._ (1999) used coincident and leading indexes in BVAR models to forecast home sales for the Connecticut and the overall US economy, respectively. Coincident and leading indexes incorporate information from component series, using the procedures established by the Department of Commerce and described in U.S. Department of Commerce (1977, 1984) and in Niemira and Klein (1994). 

7 

## **4. VAR, BVAR, FAVAR, FABVAR, and LBVAR Specifications and Estimation**<sup>**4**</sup> 

_4.1 VAR, BVAR, and LBVAR:_ 

Following Sims (1980), we can write an unrestricted VAR model as follows: 



where _y_ equals a ( _n_ × 1) vector of variables to forecast; _A_ 0 equals an ( _n_ × 1) vector of constant _5_ terms; _A(L)_ equals an ( _n_ × _n_ ) polynomial matrix in the backshift operator _L_ with lag length _p,_ 2 and ε equals an ( _n_ × 1) vector of error terms. In our case, we assume that ε ~ _N_ (0, σ _In_ ) , where _In_ equals an ( _n_ × _n_ ) identity matrix. 

The VAR method typically use equal lag lengths for all variables, which implies that the researcher must estimate many parameters, including many that prove statistically insignificant. This over-parameterization problem can create multicollinearity and a loss of degrees of freedom, leading to inefficient estimates, and possibly large out-of-sample forecasting errors. Some researchers exclude lags with statistically insignificant coefficients. Alternatively, researchers use near VAR models, which specify unequal lag lengths for the variables and equations. 

Litterman (1981), Doan _et al.,_ (1984), Todd (1984), Litterman (1986), and Spencer (1993) use the BVAR model to overcome the over-parameterization problem. Rather than eliminating lags, the Bayesian method imposes restrictions on the coefficients across different lag lengths, assuming that the coefficients of longer lags may more closely approach zero than the coefficients on shorter lags. If, however, stronger effects come from longer lags, the data can 

override this initial restriction. Researchers impose the constraints by specifying normal prior 

> 4 The discussion in this section relies heavily on LeSage (1999), Gupta and Sichei (2006), Gupta (2006), Gupta and Miller (2009a, 2009b), and Das _et al_ ., (2009). 

> 5 2 _p_ That is, _A(L)_ = _A L_ 1 + _A_ 2 _L_ + ... + _Ap L_ ; 

8 

distributions with zero means and small standard deviations for most coefficients, where the standard deviation decreases as the lag length increases and implies that the zero-mean prior holds with more certainty. The first own-lag coefficient in each equation proves the exception with a unitary mean. Finally, Litterman (1981) imposes a diffuse prior for the constant. We employ this “Minnesota prior” in our analysis, where we implement Bayesian variants of the classical VAR models. 

Formally, the means of the Minnesota prior take the following form: 



where<sup>β</sup> _i_<sup>equals the coefficients associated with the lagged dependent variables in each equation</sup> of the VAR model (i.e., the first own-lag coefficient), while β _j_ equals any other coefficient. In sum, the prior specification reduces to a random-walk with drift model for each variable, if we set all variances to zero. The prior variances, σ<sup>β</sup> 2 _i_ and σβ 2 _j_ , specify uncertainty about the prior means,<sup>β</sup> _i_<sup>= 1, and</sup> β _j_ = 0. 

Doan _et al.,_ (1984) propose a formula to generate standard deviations that depend on a small numbers of hyper-parameters: _w, d_ , and a weighting matrix _f_ ( _i, j_ ) to reduce the overparameterization in the VAR models. This approach specifies individual prior variances for a large number of coefficients, using only a few hyper-parameters. The specification of the standard deviation of the distribution of the prior imposed on variable _j_ in equation _i_ at lag _m_ , for all _i, j_ and _m_ , equals _S1(i, j, m)_ , defined as follows: 



where _f_ ( _i, j_ ) = _1_ , if _i = j_ and<sup>_k_</sup> _ij_ otherwise, with ( 0 ≤<sup>_k_</sup> _ij_ ≤ 1), and _g(m)_ = _m_<sup>−</sup> _d_ , with _d > 0_ . The 

9 

σ estimated standard error of the univariate autoregression for variable _i_ equals ˆ σ _i_ . The ratio<sup>ˆ</sup><sup>_i_</sup> σ ˆ _j_ scales the variables to account for differences in the units of measurement and, hence, causes the specification of the prior without consideration of the magnitudes of the variables. The term _w_ indicates the overall tightness, with the prior getting tighter as the value falls. The parameter _g(m)_ measures the tightness on lag _m_ with respect to lag 1, and equals a harmonic shape with decay factor _d_ , which tightens the prior at longer lags. The parameter _f_ ( _i, j_ ) equals the tightness of variable _j_ in equation _i_ relative to variable _i_ , and by increasing the interaction (i.e., the value of<sup>), we loosen the prior.</sup> 6<sup>_k_</sup> _ij_ 

> The overall tightness ( _w_ ) and the lag decay ( _d_ ) hyper-parameters equal 0.1 and 1.0, respectively, in the standard Minnesota prior, while<sup>_k_</sup> _ij_<sup>= 0.5, implying a 20x20 weighting matrix</sup> 

> ( _F_ ) for our 20 states as follows: 



Since researchers believe that the lagged dependant variable in each equation proves most 

> important, _F_ imposes<sup>β</sup> _i_<sup>=1 loosely. The</sup> β _j_ coefficients, however, that associate with less- 

> important variables receive a coefficient in the weighting matrix ( _F_ ) that imposes the prior means of zero more tightly. Since the Minnesota prior treats all variables in the VAR, except for the first own-lag of the dependent variable, in an identical manner, several researchers attempt to alter this fact. Usually, this means increasing the value for the overall tightness ( _w_ ) hyper- 

> 6 For an illustration, see Dua and Ray (1995). 

10 

parameter from 0.10 to 0.20, so that more influence comes from other variables in the model. In addition, Dua and Ray (1995) introduce a prior that imposes fewer restrictions on the other variables in the VAR model (i.e., _w_ = 0.30 and _d_ = 0.50). 

Alternatively, LeSage and Pan (1995) propose spatial BVAR (SBVAR) models. They adopt a weight matrix that uses the first-order spatial contiguity (FOSC) prior, implying a nonsymmetric _F_ matrix with more importance given to variables from neighboring states than those from non-neighboring states. Figure 1 maps the locations of the 20 states. They impose a value of one for both the diagonal elements of the weight matrix, as in the Minnesota prior, as well as for place(s) that correspond to variable(s) from states with which the specific state shares a common border(s). For the elements in the _F_ matrix that correspond to variable(s) from states that do not share common borders, Lesage and Pan (1995) impose a weight of 0.1. In sum, the 0.5 weights in the specification shown in equation (5) become 1.0 for neighbors and 0.1 for nonneighbors. 

Gupta and Miller (2009a, 2009b) propose new specifications, causality BVAR (CBVAR) models, where the weight matrix depends on tests for Granger temporal causality –- the temporal causality (TC) prior. They modify the LeSage and Pan (1995) first-order spatial-contiguity (FOSC) prior in that they consider some neighbors as more important than other neighbors. In fact, non-neighbors may exert more influence than neighbors. If one state’s housing prices temporally cause another state’s housing prices, then they code the weight matrix for that offdiagonal entry at 1.0. If no temporal causality exists, then they code the off-diagonal entry as 0.1. 

In the current application, we use 328 quarterly series, housing price growth rates of the 20 largest states as well as 308 national macroeconomic variables. Logic and prior research argues that state-level variables should exert minimal, if any, effect on national indicators, while 

11 

the latter set of variables surely influences the former. Thus, setting<sup>_k_</sup> _ij_ = 0.5 seems unrealistic. 

Hence, borrowing from the BVAR models used for regional forecasting, involving both regional and national variables, such as Kinal and Ratner (1986), Shoesmith (1992), Dua and Ray (1995), Das _et al._ (2008a, 2009), and Gupta and Kabundi (2008a, b), we set the weight of a national variable in a national equation, as well as a state equation, at 0.6. We set the weight of a state variable in other state equation at 0.1 and in a national equation at 0.01. Finally, we set the weight of the state variable in its own equation at 1.0. These weights implement Litterman’s circle-star structure. Star (national) variables affect both star and circle (state) variables, while circle variables primarily influence only other circle variables.7 Thus, we estimate the large-scale BVARs with asymmetric priors, incorporating spatial and causal influences as well as unequal influences amongst the state- and national-level variables. 

We estimate the alternative BVARs, whether based on 20 or 328 variables, using Theil's (1971) mixed estimation technique. Specifically, we denote a single equation of the VAR model 

2 as: _y_ 1 = _X_ β+ ε 1 , with _Var_ ( ε 1) = σ _I_ . Then, we can write the stochastic prior restrictions for this 

single equation as follows: 



> 7 We also experimented by assigning higher and lower interaction values, in comparison to those specified above, to the star variables in both the star and circle equations. The rank ordering of the alternative forecasts remained the same. 

12 

2 8 Note that _Var_ ( _u_ ) = σ _I_ , and the prior means _rijm_ and the prior variance σ _ijm_ take the 

forms shown in equations (2) and (3) for the Minnesota prior. With equation (5) written as follows: 



we derive the estimates for a typical equation as follows: 



Essentially then, the method involves supplementing the data with prior information on the distribution of the coefficients. The number of observations and degrees of freedom increase artificially by one for each restriction imposed on the parameter estimates. Thus, the loss of degrees of freedom from over-parameterization in the classical VAR models does not emerge as a concern in the alternative BVAR specifications. 

### _4.2 FAVAR and FABVAR:_ 

This study uses the Dynamic Factor Model (DFM) to extract common components between macroeconomic series and then uses these common components to forecast real housing price growth rates of the 20 largest US states, adding the extracted factors to the 20-variable VAR model to create a FAVAR in the process. Furthermore, we estimate idiosyncratic component (see below) with AR( _p_ ) processes as suggested by Boivin and Ng (2005). 

The DFM expresses individual times series as the sum of two unobserved components: a common component driven by a small number of common factors and an idiosyncratic component for each variable. The DFM extracts the few factors that explain the co-movement of the US economy. Forni _et al._ (2005) demonstrate that for a small number of factors relative to 

> 8 Note σ _ijm_ in equation (12) is a generic term used to describe _Sk(i, j, m), k=1, 2, 3._ 

13 

the number of variables and a heterogeneous panel, we can recover the factors from present and past observations. 

Consider a _n_ × 1 covariance stationary process _Yt_ = ( _y_ 1 _t_ ,...., _ynt_ )'. Suppose that _X t_ equals the standardized version of<sup>_Y_</sup> _t_ (i.e., _X t_ possesses a mean zero and a variance equal to one). Under DFM, we write _X t_ as the sum of two orthogonal components as follows: 



> where<sup>_F_</sup> _t_ equals a _r_ × 1 vector of static factors, λ equals an _n_ × _r_ matrix of factor loadings, and 

> <sup>ξ</sup> _t_<sup>equals a</sup> _n_ × 1 vector of idiosyncratic components. In a DFM,<sup>_F_</sup> _t_ and<sup>ξ</sup> _t_<sup>are mutually</sup> 

orthogonal stationary process, while, χ _t_ = λ _Ft_ equals the common component. 

Since dynamic common factors are latent, we must estimate them. We note that the estimation technique used matters for factor forecasts. This paper adopts the Stock and Watson (2002b) method, which employs the static principal component approach (PCA) on _X t_ . The factor estimates, therefore, equal the first principal components of _X t_ , (i.e.,<sup>_F_</sup> ˆ _t_ = Λ ˆ ′ _X t_ , where Λ ˆ equals the _n_ × _r_ matrix of the eigenvectors corresponding to the _r_ largest eigenvalues of the ˆ sample covariance matrix Σ ). 

For forecasting purposes, we use a 20-variable VAR augmented by extracted common factors using the Stock and Watson (2002a) approach. This approach is similar to the univariate Static and Unrestricted (SU) approach of Bovin and Ng (2005). Therefore, the forecasting equation to predict<sup>_Y_</sup> _t_ is given by 



14 

> where _h_ equals the forecasting horizon, Φ ˆ ( _L_ ) equal lag polynomials, which we estimate with and without restrictions. As Boivin and Ng (2005) clearly note, VAR models are special cases of equation (9). With known factors and the parameters, the FAVAR approach should produce smaller mean squared errors. In practice, however, one does not observe the factors and we must estimate them. Moreover, the forecasting equation should reflect a correct specification. We consider the following DFM specifications: 

- FAVAR: includes the real housing price growth rates of the 20 states and the common static factors; and 

- BFAVAR: the FAVAR specification with Bayesian restrictions on lags of the real housing price growth rates based on the alternative types of priors outlined above. 

## **5. Data Description, Model Estimation, and Results** 

- _5.1 Data_ 

While the small-scale VARs, both the classical and Bayesian variants, include data of only the annualized real housing price growth rates of the 20 largest US states, the large-scale BVARs and the DFM also include the 308 quarterly national series. Nominal housing prices come from the Freddie Mac database, the Conventional Mortgage Home Price Index (CMHPI). The CMHPI uses matched transactions on the same property over time to account for quality changes and consists of both purchase and refinance-appraisal transactions on over 33 million homes. We deflate the state-level nominal CMHPI housing price by the personal consumption expenditure (PCE) deflator from the Bureau of Economic Analysis (BEA) to generate our real housing price series. We then compute annualized growth rates as 400 times the differences in the natural logs of real housing prices. 

15 

For the remaining 308 national variables, we use the macroeconomic indicators in the data set of Liu and Jansen (2007). All data were transformed to induce stationarity.<sup>9</sup> Since this data set ends in 2003, our sample also ends at the same point.<sup>10</sup> Amongst the 308 macroeconomic indicators, 172 variables relate to real activity, 80 relate to prices or inflation, and 56 relate to the monetary sector. Appendix A in Liu (2004) details the variables and their transformations. The real activity group consists of variables such as industrial production, capacity utilization, manufacturers’ inventories, retail inventories, retail sales, real personal consumption, real personal income, new housing starts, employment, average working hours, and so on. The price and inflation group consists of variables such as the consumer price index, the producer price index, the personal consumption expenditure deflator, average hourly earnings, and so on. The monetary sector group consists of variables such as monetary aggregates, various interest rates, credit outstanding, and so on. Following Liu and Jansen (2007), we extract four static factors from the DFM estimated with one lag.<sup>11</sup> 

## _5.2 Estimation and Results_ 

This section reports our econometric findings. First, we determine whether temporal (Granger) causality exists between the variables in our model. Second, we select the optimal model for forecasting each market’s housing price, using the minimum average root mean squared error (RMSE) across the one-, two-, three-, and four-quarter-ahead out-of-sample forecasts. 

The data sample for all 20 states runs from 1976:Q1 through 2003:Q4. First, the temporal 

> 9 Using non-stationary data, however, is not required with the BVAR. Sims _et al._ (1990) indicate that with the Bayesian approach entirely based on the likelihood function, the associated inference does not require special treatment for non-stationarity, since the likelihood function exhibits the same Gaussian shape regardless of the presence of non-stationarity. 

> 10 Since the state-level housing prices exist only at a quarterly frequency, we transform the monthly data set of  Liu and Jansen (2007) into quarterly values by taking the averages over three months. 

> 11 We also confirm the choice of the four factors by the cumulative variance share, under which, the fifth eigenvalue fell below the threshold of 5 percent. 

16 

(Granger) causality tests use data from 1976:Q1 through 1994:Q4. Second the out-of-sample forecasting experiment covers 1995:Q1 through 2003:Q4. 

## _5.3 Evidence on Temporal Causality_ 

We first test for Granger temporal causality between the 20 state housing price series. Temporal causality tests emerge from the VAR model. We consider various lag-length selection criteria for 

the VAR specification, including the sequential modified likelihood ratio (LR) test statistic (each test at the 5-percent level), the final prediction error (FPE), the Akaike information criterion (AIC), the Schwarz information criterion (SIC), and the Hannan-Quinn information criterion (HQIC). All criteria except the SIC choose two lags. Table 1 reports the results. 

Running the VAR specification and using the block exogeneity test, we discover that 96 pairs of states do not exhibit any temporal (Granger) causality between each other. With 20 states, we need to consider a total of 190 bivariate pairs of states.<sup>12</sup> Of the remaining pairs, 74 exhibit one-way temporal causality while 20 pairs exhibit two-way causality. 

The most influential, and least influenced, states include California, Massachusetts, New Jersey, and Pennsylvania. Housing prices in Pennsylvania temporally lead housing prices in nine other states; California, in eight; and Massachusetts and New Jersey, in six. In addition, only one state’s housing prices each, North Carolina, Pennsylvania, Massachusetts, and Georgia, temporally lead the housing prices in California Massachusetts, New Jersey, and Pennsylvania, respectively. North Carolina temporally causes only two states, Arizona and Wisconsin, whereas Georgia only temporally causes three, Illinois, Indiana, and Pennsylvania. 

Switching to examine the most linkages, Indiana and Michigan housing prices respond to the most other states housing prices – 11 states each. Further, Michigan, along with Ohio and 



17 

Virginia, housing prices also temporally lead the housing prices in eight other states. Thus, Michigan exhibits two-way temporal causality with five other states -- Florida, Illinois, Maryland, Virginia, and Wisconsin. Two-way temporal causality also exists between Florida, Illinois, and Indiana and four other states. The most influential states, California, Massachusetts, New Jersey, and Pennsylvania, and Washington do not exhibit two-way temporal causality with any other state. Washington, even though geographically isolated, temporally causes five states and is temporally caused by five other states. 

While the reader may expect to see housing prices in one state influencing the housing prices in its geographic neighbors, we find little evidence of that. For the 20 instances of bivariate temporal causality, only Michigan and Wisconsin share a common border, and that only along the upper peninsula. Figure 1 reveals that 20 pairs of states share a contiguous border. One-way causality between contiguous states only occurs seven times out of the remaining 19 cases, excluding the two-way causality between Michigan and Wisconsin. 

Typically, the geographic reach of the housing market reflects the commuting shed for the metropolitan area. That is, homes compete with each other within the same metropolitan area. Tirtirglou (1992) and Clapp and Tirtirglou (1994) provided some of the earliest tests of whether the housing market exhibited efficiency in a spatial market in Hartford, Connecticut. Gupta and Miller (2009b) provide a more recent examination for 8 MSAs in the Southern California housing market. 

Since we cannot transport homes from one geographic region to another, does this necessarily imply that the housing markets in the states do not exhibit linkages? Trade theory shows that although labor and capital frequently do not move between countries, factor prices equalize (Samuelson 1948). The flows of goods and services between countries act as surrogates 

18 

for labor and capital flows and cause the prices of labor and capital to equalize even though capital and labor do not move between countries. Since housing cannot flow between markets, do other flows exist that can cause housing price convergence? Yes. First, the migration of home buyers between metropolitan areas can link the housing markets. Second, home builders can also move their operations between metropolitan areas in response to differential returns on home building activity. In sum, the movement of home buyers and home builders between regions in response to price differences can arbitrage the prices of homes, even though the homes themselves cannot move between regions. 

We argue that housing prices between geographic regions affect each other if either home buyers or home builders move between the markets in response to price incentives. On the home buyer side, different types of buyers or motivations may assist in the arbitrage process. One, migration between states for jobs or retirement may link geographically separated states. Two, equity conversion may allow some longtime residents of one state that experienced significant appreciation to cash in their accumulated equity and buy a “better” home in another state with lower housing prices, possibly linked to retirement decisions. Three, investors may use spatial arbitrage to allocate their housing investment funds.<sup>13</sup> In sum, we find more evidence of temporal causality occurring between non-adjacent states and not occurring between adjacent states than we initially hypothesized. 

## _5.4 One- to Four-Quarter-Ahead Forecast Accuracy_ 

Given the specification of priors in Section 4, we estimate the alternative small- and large-scale models for the 20 states in our sample over the period 1976:Q1 to 1994:Q4 using quarterly data. 

We then compute out-of-sample one- to four-quarters-ahead forecasts for the period of 1995:Q1 

> 13 Meen (1999) offers a similar discussion of UK for housing price arbitrage between the Southeast to the Northwest, which he calls the “ripple effect.” He defines four explanations -- migration, equity conversion, spatial arbitrage, and exogenous shocks with different timing of spatial effects. 

19 

to 2003:Q4, and compare the forecast accuracy relative to the forecasts generated by an unrestricted VAR. Note that the choice of the in-sample period, especially the starting date, depends on data availability. The starting point of the out-of-sample period follows Rapach and Strauss (2007, 2008), who observe marked differences in housing price growth across U.S. regions since the mid-1990s. As indicated above, the end-point of the horizon is 2003:Q4, since the Liu and Jansen (2007) data on the national 308 variables ends there. 

We estimate the multivariate versions of the classical VAR, the small-scale BVARs, the large-scale BVARs, and the classical and Bayesian FAVARs over the period 1976:Q1 to 1994:Q4, and then forecast from 1995:Q1 through 2003:Q4. Since we use two lags, the initial two quarters from 1976:Q1 to 1976:Q2 feed the lags. We re-estimate the models each quarter over the out-of-sample forecast horizon in order to update the estimate of the coefficients, before producing the four-quarters-ahead forecasts. We implemented this iterative estimation and the four-quarters-ahead forecast procedure for 36 quarters, with the first forecast beginning in 1995:Q1. This produced a total of 36 one-quarter-ahead forecasts, …, up to 36 four-quartersahead forecasts.<sup>14</sup> We calculate the root mean squared errors (RMSE)<sup>15</sup> for the 36 one-, two-, three-, and four-quarters-ahead forecasts for the 20 annualized real housing price growth rates of the models. We then examine the average of the RMSE statistic for one-, two-, three-, and fourquarters ahead forecasts over 1995:Q1 to 2003:Q4. 

> For the BVAR and FABVAR models, we start with a value of _w_ = 0.1 and _d_ = 1.0, and 

> then increase the value to _w_ = 0.2 to account for more influences from variables other than the 

> 14 For this, we used the algorithm in the Econometric Toolbox of MATLAB, version R2007a. 



of forecasts. 

20 

first own lags of the dependant variables of the model. In addition, as in Dua and Ray (1995), Gupta and Sichei (2006), Gupta (2006), and Gupta and Miller (2009a, 2009b), we also estimate the BVARs and FABVARs with _w_ = 0.3 and _d_ = 0.5. We also introduce _d = 2_ to increase the tightness on lag _m_ . We select the model that produces the lowest average RMSE values as the ‘optimal’ specification for a specific state. 

Table 3 reports the average of the one-, two-, three-, and four-quarter-ahead RMSEs across all 20 states. The benchmark for all forecast evaluations is the VAR model forecast RMSEs. Thus, the 0.141 entry for the FAVAR model means that the FAVAR model experienced a forecast RMSE of only 14.1 percent of the forecast RMSE for the VAR model. The results fall into three different categories. The spatial and causality Bayesian VAR models (SBVAR and CBVAR, respectively) do not perform much better than the VAR model with improvements in RMSE in the neighborhood of 11 to 16 percent. Next, the large-scale spatial and causality Bayesian VAR models (LSBVAR and LCBVAR, respectively) show more improvement in RMSE over the VAR model, gaining between 73 to 75 percent. Finally, the factor augmented models – VAR, spatial BVAR, and causality BVAR – experienced the most improvement over the simple VAR RMSE forecast errors, improving by 81 to 86 percent. As such, the SBVAR and CBVAR models forecast performance do not improve much over the benchmark VAR model forecasts and the factor-augmented and large-scale Bayesian models exhibit improved performance over the VAR (SBVAR and CBVAR) model, but do not differ too much for each other in forecasting performance. 

> The factor augmented spatial Bayesian VAR model with _w=0.1_ and _d=2._ 0 provides the lowest average RMSE at 13.7-percent of the RMSE of the benchmark VAR model, which we identify as the optimal specification. This specification deviates from the Minnesota prior in that 

21 

the decay factor reduces the influence of lagged values more quickly. The SFABVAR model with _w=0.1_ and _d=1._ 0, the Minnesota prior, emerged as the second best performing model with a RMSE of 14.1 percent of the VAR model, barely edging out the FAVAR model. 

Table 4 reports the average one-, two-, three-, and four-quarter-ahead RMSE forecast errors for each of the 20 states. First, the factor-augmented models generally performed better than the large-scale models. A large-scale model emerged as the best performing model in terms of minimum RMSE in only two states – Massachusetts and Virginia. In both states, the largescale causality BVAR achieved the best forecast performance, albeit with different priors _w=0.2_ and _d=2._ 0 and _w=0.3_ and _d=0.5_ , respectively. In the remaining 18 states, factor-augmented models performed the best. In seven states the FAVAR model without spatial or causality priors achieved the lowest RMSEs – California, Florida, Georgia, Maryland, New Jersey, Texas, and Washington. For 10 states, the spatial factor-augmented model achieved the best performance – six states with _w=0.1_ and _d=2._ 0 – Arizona, Michigan, New York, Ohio, Pennsylvania, and Wisconsin; three states with _w=0.3_ and _d=0.5_ – Indiana, Missouri, and Tennessee; and one state with _w=0.2_ and _d=1._ 0 -- Illinois. North Carolina achieved the best forecast performance for the Causality factor-augmented BVAR model with the Minnesota prior. 

In sum, different specifications yield the lowest RMSE in different states. No common pattern emerges. Comparing the forecasting performance across states, however, we see that the five best performing forecast models in order from best to worst include Michigan (2.6 percent of the VAR RMSE), Virginia (5.7 percent), Florida (8.4 percent), Washington (8.5 percent), and Illinois (9.2 percent). The five worst performing forecast models, although the best in each state, in order from worst to best include Pennsylvania (16.8 percent of the VAR RMSE), Ohio (15.9 percent), Texas (14.9 percent), Georgia (14.5 percent), and New York (13.5 percent). 

22 

## **6. Conclusion** 

We forecast housing prices in 20 US states, using the VAR and BVAR models, both with and without the information content of 308 additional quarterly economic series. Two approaches exist for incorporating information from a large number of data series – extracting common factors (principle components) in a Factor-Augmented Vector Autoregressive (FAVAR) or Factor-Augmented Bayesian Vector Autoregressive (FABVAR) models or Bayesian shrinkage in a large-scale Bayesian Vector Autoregressive (LBVAR) models.<sup>16</sup> In addition, we also introduce spatial or causality priors to augment the forecasting models. 

Using the period of 1976:Q1 to 1994:Q4 as the in-sample period and 1995:Q1 to 2003:Q4 as the out-of-sample horizon, we compare the forecast performance of the alternative models for one- to four-quarters ahead forecasts. Based on the average root mean squared error (RMSE) for the one-, two-, three-, and four–quarter-ahead forecasts, we find that the factoraugmented models, sometimes with spatial or causality priors, generally outperform the largescale models in the 20 US states examined. In two states, the large-scale BVAR models provide the best forecasts. But, the differences between the factor-augmented and large scale Bayesian models average RMSEs generally prove small in size. Both the factor-augmented and large-scale Bayesian models produce much lower average RMSEs than the spatial or causality VAR or BVAR models. 

In sum, the utilization of a large dataset of economic variables improves the forecasting performance over models that do not use this data. In other words, macroeconomic fundamentals do matter when forecasting real housing prices. 

> 16 Another approach also exists, the ADRL method. This approach estimates a series of bivariate transfer function models with forecasted variable as the dependent variable and then aggregates forecasts with various weighting methods. We do not pursue this single-equation method and only consider the multiple-equation FAVAR and LBVAR models. 

23 

## **References:** 

Abraham, J. M., and Hendershott, P. H. (1996). Bubbles in Metropolitan Housing Markets. _Journal of Housing Research_ , 7(2), 191–207. 

- Bernanke, B. S., Boivin, J., and Eliazs, P. (2005) Measuring the Effects of Monetary Policy: A Factor-Augmented Vector autoregressive (FAVAR) Approach, _The Quarterly Journal of Economics_ , 120, 387–422. 

- Bernanke, B., and Gertler, M. (1995). Inside the Black Box: the Credit Channel of Monetary Transmission. _Journal of Economic Perspectives_ , 9(4), 27–48. 

- Boivin, J., and Ng, S. (2005). Undertanding and comparing factor based forecasts. _International Journal of Central Banking_ , 1(3), 117-152. 

- Cho, M. (1996). House Price Dynamics: A Survey of Theoretical and Empirical Issues _. Journal of Housing Research_ , 7(2), 145–172. 

- Clapp, J. M., and Tirtirglou, D. (1994) .Positive Feedback Trading and Diffusion of Asset Price Changes: Evidence from Housing Transactions. _Journal of Economic Behavior and Organization_ , 24(3), 337-355. 

- Das, S., Gupta, R., and Kabundi, A. (2008a). Could We Have Forecasted the Recent Downturn in the South African Housing Market? Working Paper No. 200831, University of Pretoria. <u>http://ideas.repec.org/p/pre/wpaper/200831.html.</u> 

- Das, S., Gupta, R., and Kabundi, A. (2008b). Is a DFM Well-Suited for Forecasting Regional House Price Inflation?” Working Paper No. 85, Economic Research Southern Africa. http://www.econrsa.org/wp85.html. 

- Das, S., Gupta, R., and Kabundi, A. (2009). The Blessing of Dimensionality in Forecasting Real House Price Growth in the Nine Census Divisions of the US. Working Paper No. 200902, University of Pretoria. <u>http://ideas.repec.org/p/pre/wpaper/200902.html.</u> 

- Doan, T. A., Litterman, R. B., and Sims, C. A. (1984). Forecasting and Conditional Projections Using Realistic Prior Distributions. _Econometric Reviews_ , 3(1), 1-100. 

- Dua, P., and Miller, S. M. (1996). Forecasting Connecticut Home Sales in a BVAR Framework Using Coincident and Leading Indexes. _Journal of Real Estate Finance and Economics_ , 13(3), 219-235. 

- Dua, P., Miller, S. M., and Smyth, D. J. (1999). Using Leading Indicators to Forecast U. S. Home Sales in a Bayesian Vector Autoregressive Framework. _Journal of Real Estate Finance and Economics_ , 18(2), 191-205. 

24 

- Dua, P., and Ray, S. C. (1995). A BVAR Model for the Connecticut Economy. _Journal of Forecasting_ , 14(3), 167-180. 

- Dua, P., and Smyth, D. J. (1995). Forecasting U. S. Home Sales using BVAR Models and Survey Data on Households’ Buying Attitude for Homes. _Journal of Forecasting_ , 14(3), 217-227. 

- Forni, M., Hallin, M., Lippi, M., and Reichlin, L. (2005). The Generalized Dynamic Factor Model, One Sided Estimation and Forecasting. _Journal of the American Statistical Association_ , 100(471), 830–840. 

- Gupta, R. (2006). Forecasting the South African Economy with VARs and VECMs. _South African Journal of Economics,_ 74(4), 611-628 _._ 

- Gupta, R., and Das, S. (2008a). Predicting Downturns in the US Housing Market. Forthcoming _Journal of Real Estate Economics and Finance._ 

- Gupta, R., and Das, S. (2008b). Spatial Bayesian Methods for Forecasting House Prices in Six Metropolitan Areas of South Africa. _South African Journal of Economics,_ 76(2), 298313 _._ 

- Gupta, R., and Kabundi, A. (2008a). Forecasting Macroeconomic Variables using Large Datasets: Dynamic Factor Model vs Large-Scale BVARs. Working Paper No. 200816, Department of Economics, University of Pretoria. 

- Gupta, R., and Kabundi, A. (2008b). Forecasting Macroeconomic Variables in a Small Open Economy: A Comparison between Small- and Large-Scale Models. Working Paper No. 200830, Department of Economics, University of Pretoria. 

- Gupta, R., and Miller S. M. (2009a) “‘Ripple Effects” and Forecasting Home Prices in Los Angeles, Las Vegas, and Phoenix.” University of Nevada, Las Vegas ,Working Paper No. 0902. <u>http://ideas.repec.org/p/nlv/wpaper/0902.html.</u> 

- Gupta, R., and Miller S. M. (2009b) “The Time-Series Properties on Housing Prices: A Case Study of the Southern California Market.” University of Nevada, Las Vegas ,Working Paper No. 0912. <u>http://ideas.repec.org/p/nlv/wpaper/0912.html.</u> 

- Gupta, R., and Sichei, M. M. (2006). A BVAR Model for the South African Economy. _South African Journal of Economics,_ 74(3), 391-409 _._ 

- Iacoviello, M., and Neri, S. (2008). Housing Market Spillovers: Evidence from an Estimated DSGE Model. Working Paper No. 659, Boston College Department of Economics. http://fmwww.bc.edu/ec-p/wp659.pdf. 

- International Monetary Fund. _World Economic Outlook: Asset Prices and the Business Cycle_ , 2000. 

25 

- Liu, D., and Jansen, D. W. (2007). "Macroeconomic forecasting using structural factor " 

- <u>analysis,</u> _<u>International Journal of Forecasting</u>_ <u>, 23(4), pages 655-677.</u> 

- Johnes, G., and Hyclak, T. (1999). House Prices and Regional Labor Markets. _Annals of Regional Science_ , 33(1), 33–49. 

LeSage, J. P. (1999). _Applied Econometrics Using MATLAB_ , www.spatial-econometrics.com. 

- LeSage, J. P., (2004) Spatial Regression Models. In _Numerical Issues in Statistical Computing for the Social Scientist_ , John Wiley & Sons, Inc., Micah Altman, Je Gill and Michael McDonald (eds.), 199-218. 

- LeSage, J. P., and Pan, Z. (1995). Using Spatial Contiguity as Bayesian Prior Information in Regional Forecasting Models, _International Regional Science Review_ , 18(1), 33-53. 

- Litterman, R. B. (1981). A Bayesian Procedure for Forecasting with Vector Autoregressions. _Working Paper_ , Federal Reserve Bank of Minneapolis. 

- Litterman, R. B. (1986). Forecasting with Bayesian Vector Autoregressions – Five Years of Experience. _Journal of Business and Economic Statistics_ , 4(1), 25-38. 

- Liu, D. (2004). The Effects of Monetary Policy and Macroeconomic Forecasting Using Structural Factor Analysis, Mimeo, Department of Economics, Texas A&M University. 

- Meen, G. P. (1999). Regional House Prices and the Ripple Effect: A New Interpretation. _Housing Studies_ , 14(6), 733-753. 

- Meen, G. P. (2002). The Time-Series Behavior of House Prices: A Transatlantic Divide? _Journal of Housing Economics_ , 11(1), 1-23. 

- Niemira, M. P., and Klein, P. A. (1994). _Forecasting Financial and Economic Cycles._ New York: John Wiley & Sons, Inc. 

- Pollakowski, H.O., and Ray T. S. (1997) Housing price diffusion patterns at different aggregation levels: an examination of housing market efficiency. _Journal of Housing Research_ , 8(1), 107-124. 

- Rapach, D. E., and Strauss, J. K. (2007). Forecasting Real Housing Price Growth in the Eighth District States. Federal Reserve Bank of St. Louis. _Regional Economic Development_ , 3(2), 33–42. 

Rapach, D. E., and Strauss, J. K. (2008). Differences in Housing Price Forecast ability Across U.S. States. _International Journal of Forecasting_ , 25(2), 351-372. 

26 

- Samuelson, P. A. 1948. International Trade and Equalisation of Factor Prices. _Economic Journal_ , 58(230), 163–184. 

Sims, C. A. (1980). Macroeconomics and Reality. _Econometrica_ , 48(1), 1-48. 

- Spencer, D. E. (1993). Developing a Bayesian Vector Autoregression Model. _International Journal of Forecasting_ , 9(3), 407-421. 

- Stock, James H., and Watson, M. W., (1999). Forecasting Inflation. _Journal of Monetary Economics_ , _44_ (2), 293-335. 

- Stock, J. H., and Watson, M.W. (2002a) Forecasting Using Principal Components from a Large Number of Predictors. _Journal of the American Statistical Association,_ 97(460), 147–162. 

- Stock, J. H., and Watson, M. W., (2002b) Macroeconomics forecasting using diffusion indexes, _Journal of Business and Economic Statistics_ , 20(2), 147–162. 

- Stock, J. H., and Watson, M.W., (2003). Forecasting Output and Inflation: The Role of Asset Prices. _Journal of Economic Literature_ , 41(3), 788-829. 

- Stock, J. H., and Watson, M. W., (2004). Combination Forecasts of Output Growth in a SevenCountry Data Set. _Journal of Forecasting_ , _23_ (6), 405-430. 

- Stock, J. H., and Watson, M. W., (2005). Implications of dynamic factor models for VAR analysis. NBER Working Paper No. 11467. 

Theil, H. (1971). _Principles of Econometrics_ . New York: John Wiley. 

- Tirtirglou, D. (1992). Efficiency in Housing Markets: Temporal and Spatial Dimensions. _Journal of Housing Economics_ ,  2(3), 276-292. 

- Todd, R. M. (1984). Improving Economic Forecasting with Bayesian Vector Autoregression. _Quarterly Review_ , Federal Reserve Bank of Minneapolis, Fall, 18-29. 

- Topel, R. H., and Rosen, S. (1988). Housing Investment in the United States. _Journal of Political Economy_ , 96(4), 718–740. 

- United States Department of Commerce. (1977). "Composite Indexes of Leading, Coincident, and Lagging Indicators: A Brief Explanation of Their Construction." In _Handbook of Cyclical Indicators, A Supplement to the Business Conditions Digest._ Washington, D.C.: Bureau of Economic Analysis, May, pp. 73-76. 

- United States Department of Commerce. (1984)."Composite Indexes of Leading, Coincident, and Lagging Indicators: A Brief Explanation of Their Construction." In _Handbook of Cyclical Indicators, A Supplement to the Business Conditions Digest._ Washington, D.C.: Bureau of Economic Analysis, May, pp. 65-70. 

27 

- Vargas-Silva, C. (2008a).The Effect of Monetary Policy on Housing: A Factor Augmented Approach. _Applied Economics Letters_ , 15(10), 749-752. 

- Zellner, A., and Palm, F. (1974). Time Series Analysis and Simultaneous Equation Econometric Models. _Journal of Econometrics_ , 2(1), 17-54. 

28 

## **Table 1: Lag-Length Selection Tests** 

|Lag|LogL|LR|FPE|AIC|SC|HQ|
|---|---|---|---|---|---|---|
|0|-4801.889|NA|8.88e+31|130.3213|130.9440*|130.5697|
|1|-3966.763|1196.261|9.55e+26|118.5612|131.6383|123.7778|
|2|-3097.724|775.0886*|3.58e+22*|105.8844*|131.4160|116.0693*|



**Note:** The star indicates lag order selected by the criterion. The criterion include the sequential modified likelihood ratio (LR) test statistic (each test at 5% level), the final prediction error (FPE), the Akaike information criterion (AIC), the Schwarz information criterion (SIC), and the Hannan-Quinn information criterion (HQIC). 

29 

## **Table 2: Granger Temporal Causality Tests** 

|**States**|**AZ**|**CA**|**FL**|**GA**|**IL**|**IN**|**MA**|**MD**|**MI**|**MO**|**NC**|**NJ**|**NY**|**OH**|**PA**|**TN**|**TX**|**VA**|**WA**|**WI**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**AZ**||2.850|3.432|0.160|1.265|3.164|0.190|0.439|4.196|0.873|4.744‡|3.501|1.058|3.428|10.516*|1.548|2.208|1.456|7.125†|0.220|
|**CA**|0.749||4.010|1.003|2.081|1.547|0.492|2.198|1.677|6.742†|2.514|0.855|0.741|2.158|1.728|2.456|1.275|0.346|2.490|0.896|
|**FL**|0.812|9.435*||4.434|0.714|6.253†|4.769‡|8.201†|10.162*|2.659|3.319|1.864|8.099†|0.761|6.757†|1.992|5.426‡|3.785|5.610‡|1.870|
|**GA**|4.250|0.175|2.954||8.031†|12.644*|4.215|0.165|6.752†|2.546|3.411|0.740|3.041|0.779|4.056|4.329|1.834|0.209|7.864†|0.011|
|**IL**|0.898|6.865†|23.347*|4.698‡||1.072|0.501|0.726|18.365*|13.470*|2.907|1.718|0.006|1.123|1.493|6.706†|22.187*|34.438*|4.544|1.530|
|**IN**|3.207|12.407*|8.765†|8.232†|2.788||5.527‡|6.175†|1.282|12.780*|0.278|2.559|5.296‡|15.491*|12.503*|1.738|4.633‡|10.058*|4.437|1.097|
|**MA**|1.723|1.711|1.574|0.754|0.670|0.064||0.761|0.783|2.181|3.044|0.174|1.370|0.641|4.909‡|4.190|1.265|3.864|0.151|0.266|
|**MD**|2.501|13.451*|5.198‡|0.949|5.045‡|1.506|0.728||6.393†|2.649|2.029|3.386|1.414|4.338|0.336|2.730|6.269†|5.657‡|3.399|4.141|
|**MI**|23.111*|2.803|12.694*|0.587|9.447*|2.009|6.663†|10.343*||13.879*|0.867|0.320|3.309|7.207†|23.995*|2.620|10.684*|7.369†|3.918|10.676*|
|**MO**|6.334†|1.892|2.839|0.079|2.520|5.594‡|1.167|2.240|1.334||2.337|1.060|16.220*|10.040*|21.569*|6.258†|1.268|5.079‡|0.042|9.123†|
|**NC**|8.644†|0.766|2.835|0.032|1.933|5.220‡|1.318|1.301|5.875‡|2.499||1.017|5.503‡|3.105|4.113|11.981*|1.824|1.780|6.228†|2.570|
|**NJ**|2.280|0.369|2.109|1.766|0.028|0.867|6.227†|0.674|1.879|0.930|0.792||0.122|0.450|0.377|3.522|1.837|0.884|0.884|2.184|
|**NY**|19.033*|1.215|9.521*|0.998|8.517†|4.438|4.203|4.324|7.340†|7.049†|2.469|35.284*||6.169†|20.294*|2.735|0.727|7.898†|0.117|2.631|
|**OH**|0.324|2.271|5.992†|0.351|2.018|4.018|1.553|0.927|1.185|0.283|1.593|6.191†|20.447*||5.884‡|0.693|1.448|2.395|1.330|1.943|
|**PA**|0.932|1.467|4.274|5.264‡|0.250|2.005|3.787|2.745|0.012|3.777|2.158|1.072|2.038|1.177||0.392|1.220|0.184|2.392|2.188|
|**TN**|4.369|0.553|6.529|4.010|0.282|0.473|13.220*|1.474|0.083|2.940|0.564|4.983‡|3.525|3.086|0.099||0.114|3.427|7.867†|18.831*|
|**TX**|0.655|5.485‡|0.738†|0.056|5.298‡|5.309‡|4.106|7.614†|2.858|1.722|0.546|5.251‡|1.404|6.031†|0.170|1.132||0.724|1.978|13.070*|
|**VA**|1.521|9.088†|0.624|3.345|6.057†|3.473|7.436†|3.203|6.062†|0.285|0.257|9.355*|2.199|21.673*|3.398|2.677|0.030||2.370|13.518*|
|**WA**|1.647|16.669*|1.295|0.440|3.249|4.863‡|4.118|0.457|0.023|3.210|1.384|5.775‡|1.371|5.496‡|2.453|0.027|1.392|10.230*||1.085|
|**WI**|0.174|0.051|0.899|4.376|1.279|7.534†|4.582|0.361|8.180†|3.782|5.586‡|1.462|29.678*|5.127‡|20.469*|10.545*|1.219|5.179‡|1.292||



**Note:** Numbers are χ 2 tests with 2 degrees of freedom. The test determines whether the column state temporally (Granger) causes the row state. 

* Means significant at the 1-percent level. † Means significant at the 5-percent level. ‡ Means significant at the 10-percent level. 

**Table 3: Forecast Results for the Real Housing Price Index: All 20 States** 

|**Model**|**Parameters**|**All**<br>**States**|**Model**|**Parameters**|**All**<br>**States**|**Model**|**Parameters**|**All**<br>**States**|
|---|---|---|---|---|---|---|---|---|
|**FAVAR**||0.141|||||||
||**w=0.3,d=0.5**|0.877||**w=0.3,d=0.5**|0.155||**w=0.3,d=0.5**|0.256|
||**w=0.2,d=1**|0.871||**w=0.2,d=1**|0.147||**w=0.2,d=1**|0.257|
|**SBVAR**|**w=0.1,d=1**|0.846|**SFABVAR**|**w=0.1,d=1**|0.141|**LSBVAR**|**w=0.1,d=1**|0.257|
||**w=0.2,d=2**|0.871||**w=0.2,d=2**|0.145||**w=0.2,d=2**|0.253|
||**w=0.1,d=2 **|0.846||**w=0.1,d=2 **|0.137*||**w=0.1,d=2 **|0.252|
||**w=0.3,d=0.5**|0.884||**w=0.3,d=0.5**|0.184||**w=0.3,d=0.5**|0.267|
||**w=0.2,d=1**|0.869||**w=0.2,d=1**|0.181||**w=0.2,d=1**|0.270|
|**CBVAR**|**w=0.1,d=1**|0.843|**CFABVAR**|**w=0.1,d=1**|0.177|**LCBVAR**|**w=0.1,d=1**|0.270|
||**w=0.2,d=2**|0.869||**w=0.2,d=2**|0.178||**w=0.2,d=2**|0.268|
||**w=0.1,d=2 **|0.843||**w=0.1,d=2 **|0.168||**w=0.1,d=2 **|0.267|



**Note:** Numbers all relative to the RMSE forecast error of the simple VAR model as the benchmark. Thus, values less than one mean that the model exhibits a lower RMSE than the VAR model. The star (*) indicates the forecasting model in all states with the minimum RMSE. 

## **Table 4: Forecast Results for the Real Housing Price Index: 20 States** 

|**MODEL**|**Parameters**|**AZ**|**CA**|**FL**|**GA**|**IL**|**IN**|**MA**|**MD**|**MI**|**MO**|**NC**|**NJ**|**NY**|**OH**|**PA**|**TN**|**TX***|**VA**|**WA**|**WI**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**FAVAR**||0.187|0.101*|0.084*|0.145*|0.100|0.242|0.143|0.092*|0.171|0.120|0.162|0.110*|0.137|0.185|0.229|0.155|0.149|0.096|0.085*|<br>0.133|
||**w=0.3,d=0.5**|1.026|0.939|1.035|1.122|0.776|0.843|0.924|1.041|0.802|0.792|0.859|0.958|0.733|0.828|0.883|0.660|1.007|0.954|0.599|0.753|
||**w=0.2,d=1**|1.025|0.942|1.019|1.093|0.770|0.852|0.922|1.028|0.765|0.827|0.839|0.972|0.730|0.821|0.896|0.645|0.981|0.958|0.603|0.740|
|**SBVAR**|**w=0.1,d=1**|0.975|0.937|0.928|0.953|0.751|0.857|0.926|0.995|0.695|0.870|0.799|0.979|0.727|0.799|0.932|0.616|0.909|0.920|0.625|0.721|
||**w=0.2,d=2**|1.025|0.942|1.019|1.093|0.770|0.852|0.922|1.028|0.765|0.827|0.839|0.972|0.730|0.821|0.896|0.645|0.981|0.958|0.603|0.740|
||**w=0.1,d=2**|0.975|0.937|0.928|0.953|0.751|0.857|0.926|0.995|0.695|0.870|0.799|0.979|0.727|0.799|0.932|0.616|0.909|0.920|0.625|0.721|
||**w=0.3,d=0.5**|0.999|0.913|0.880|1.021|0.839|0.811|0.929|1.015|0.849|0.738|0.845|0.914|0.821|0.890|0.904|0.870|1.042|0.910|0.733|0.755|
||**w=0.2,d=1**|1.010|0.914|0.851|0.999|0.842|0.794|0.927|1.022|0.803|0.696|0.799|0.915|0.815|0.896|0.920|0.820|1.026|0.892|0.703|0.737|
|**CBVAR**|**w=0.1,d=1**|0.940|0.917|0.799|0.894|0.852|0.808|0.927|1.027|0.720|0.733|0.766|0.927|0.838|0.868|0.920|0.688|0.952|0.840|0.687|0.749|
||**w=0.2,d=2**|1.010|0.914|0.851|0.999|0.842|0.794|0.927|1.022|0.803|0.696|0.799|0.915|0.815|0.896|0.920|0.820|1.026|0.892|0.703|0.737|
||**w=0.1,d=2**|0.940|0.917|0.799|0.894|0.852|0.808|0.927|1.027|0.720|0.733|0.766|0.927|0.838|0.868|0.920|0.688|0.952|0.840|0.687|0.749|
||**w=0.3,d=0.5**|0.167|0.204|0.100|0.167|0.142|0.109*|0.181|0.113|0.061|0.100*|0.152|0.110|0.197|0.195|0.222|0.108*|0.210|0.142|0.233|0.192|
||**w=0.2,d=1**|0.140|0.178|0.093|0.172|0.0928|0.113|0.197|0.116|0.055|0.108|0.147|0.116|0.183|0.184|0.189|0.125|0.205|0.140|0.217|0.165|
|**SFABVAR**|**w=0.1,d=1**|0.139|0.146|0.095|0.171|0.099|0.129|0.208|0.111|0.040|0.132|0.148|0.118|0.152|0.168|0.169|0.137|0.198|0.128|0.202|0.134|
||**w=0.2,d=2**|0.139|0.156|0.091|0.169|0.103|0.120|0.213|0.120|0.045|0.124|0.147|0.116|0.173|0.175|0.173|0.139|0.200|0.141|0.207|0.141|
||**w=0.1,d=2**|0.126*|0.130|0.092|0.162|0.106|0.144|0.216|0.109|0.026*|0.149|0.138|0.116|0.135*|0.159*|0.168*|0.145|0.190|0.115|0.196|0.1208|
||**w=0.3,d=0.5**|0.196|0.210|0.152|0.201|0.175|0.137|0.199|0.143|0.101|0.151|0.182|0.132|0.210|0.227|0.316|0.125|0.264|0.152|0.231|0.175|
||**w=0.2,d=1**|0.162|0.163|0.155|0.218|0.136|0.159|0.216|0.141|0.160|0.185|0.149|0.133|0.207|0.222|0.301|0.161|0.267|0.132|0.197|0.163|
|**CFABVAR**|**w=0.1,d=1**|0.185|0.123|0.156|0.211|0.115|0.181|0.220|0.140|0.182|0.206|0.124*|0.135|0.197|0.198|0.282|0.177|0.263|0.124|0.168|0.148|
||**w=0.2,d=2**|0.168|0.133|0.147|0.208|0.109|0.183|0.239|0.142|0.143|0.208|0.129|0.136|0.191|0.217|0.293|0.173|0.261|0.130|0.177|0.166|
||**w=0.1,d=2**|0.173|0.113|0.132|0.182|0.128|0.208|0.228|0.138|0.125|0.205|0.132|0.135|0.167|0.190|0.258|0.169|0.238|0.129|0.155|0.146|
||**w=0.3,d=0.5**|0.267|0.214|0.100|0.405|0.166|0.446|0.161|0.222|0.254|0.263|0.333|0.350|0.296|0.373|0.308|0.214|0.169|0.074|0.196|0.311|
||**w=0.2,d=1**|0.222|0.193|0.097|0.405|0.191|0.414|0.147|0.230|0.221|0.256|0.295|0.410|0.286|0.388|0.332|0.238|0.221|0.082|0.243|0.272|
|**LSBVAR**|**w=0.1,d=1**|0.218|0.192|0.098|0.397|0.190|0.414|0.150|0.228|0.218|0.258|0.294|0.413|0.287|0.387|0.330|0.234|0.224|0.082|0.244|0.275|
||**w=0.2,d=2**|0.152|0.157|0.125|0.432|0.184|0.382|0.136|0.217|0.215|0.207|0.244|0.457|0.251|0.388|0.349|0.252|0.302|0.080|0.315|0.210|
||**w=0.1,d=2**|0.141|0.157|0.119|0.419|0.186|0.382|0.141|0.215|0.225|0.217|0.242|0.457|0.256|0.385|0.344|0.248|0.304|0.077|0.315|0.217|
||**w=0.3,d=0.5**|0.366|0.199|0.116|0.368|0.175|0.455|0.154|0.143|0.289|0.239|0.351|0.347|0.363|0.307|0.474|0.164|0.314|0.057*|0.203|0.256|
||**w=0.2,d=1**|0.299|0.193|0.117|0.392|0.189|0.426|0.142|0.158|0.253|0.272|0.321|0.395|0.374|0.321|0.450|0.221|0.375|0.071|0.231|0.206|
|**LCBVAR**|**w=0.1,d=1**|0.294|0.192|0.117|0.384|0.188|0.426|0.146|0.158|0.258|0.269|0.319|0.397|0.376|0.321|0.448|0.218|0.374|0.071|0.232|0.205|
||**w=0.2,d=2**|0.192|0.179|0.140|0.446|0.190|0.404|0.131*|0.154|0.253|0.265|0.278|0.430|0.374|0.308|0.388|0.259|0.470|0.087|0.265|0.147|
||**w=0.1,d=2**|0.191|0.178|0.133|0.433|0.190|0.404|0.136|0.152|0.259|0.269|0.276|0.430|0.379|0.304|0.387|0.255|0.466|0.085|0.266|0.147|



**Note:** Numbers all relative to the RMSE forecast error of the simple VAR model as the benchmark. Thus, values less than one mean that the model exhibits a lower RMSE than the VAR model. The star (*) indicates the forecasting model in each state with the minimum RMSE. 



33 

