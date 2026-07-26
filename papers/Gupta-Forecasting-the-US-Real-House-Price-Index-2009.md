---
title: **Forecasting the US Real House Price Index: Structural and NonStructural Models with and without Fundamentals**
type: paper
source_pdf: raw/papers/Gupta_Forecasting the US Real House Price Index_2009.pdf
converted: 2026-07-26
---





_Department of Economics Working Paper Series_ 

# **Forecasting the US Real House Price Index: Structural and NonStructural Models with and without Fundamentals** 

Rangan Gupta 

University of Pretoria 

Alain Kabundi University of Johannesburgh 

# Stephen M. Miller 

University of Connecticut and University of Nevada, Las Vegas 

Working Paper 2009-42 

December 2009 



Storrs, CT 06269–1063 Phone: (860) 486–3022 Fax: (860) 486–4463 http://www.econ.uconn.edu/ 

This working paper is indexed on RePEc, http://repec.org/ 

# **Abstract** 

We employ a 10-variable dynamic structural general equilibrium model to forecast the US real house price index as well as its turning point in 2006:Q2. We also examine various Bayesian and classical time-series models in our forecasting exercise to compare to the dynamic stochastic general equilibrium model, estimated using Bayesian methods. In addition to standard vector-autoregressive and Bayesian vector autoregressive models, we also include the information content of either 10 or 120 quarterly series in some models to capture the influence of fundamentals. We consider two approaches for including information from large data sets – extracting common factors (principle components) in a FactorAugmented Vector Autoregressive or Factor-Augmented Bayesian Vector Autoregressive models or Bayesian shrinkage in a large-scale Bayesian Vector Autoregressive models. We compare the out-of-sample forecast performance of the alternative models, using the average root mean squared error for the forecasts. We find that the small-scale Bayesian-shrinkage model (10 variables) outperforms the other models, including the large-scale Bayesian-shrinkage model (120 variables). Finally, we use each model to forecast the turning point in 2006:Q2, using the estimated model through 2005:Q2. Only the dynamic stochastic general equilibrium model actually forecasts a turning point with any accuracy, suggesting that attention to developing forward-looking microfounded dynamic stochastic general equilibrium models of the housing market, over and above fundamentals, proves crucial in forecasting turning points. 

## C32, R31 

**Keywords:** US House prices, Forecasting, DSGE models, Factor Augmented Models, Large-Scale BVAR models 

We gratefully acknowledge Matteo Iacoviello and Stefano Neri for many helpful comments. All remaining errors are ours. 

## 1 **. Introduction** 

This paper considers the dynamics of the US real house price index and the ability of a dynamic stochastic general equilibrium (DSGE) model and different time-series models to forecast this price index. As a part of the analytical analysis, we consider how the researcher can incorporate large data sets into forecasting equations, using dynamic factor analysis or Bayesian-shrinkage vector autoregressive (VAR) models. The main focus, however, compares the relative effectiveness of the DSGE and various time-series models in out-of-sample forecasting and turning-point identification. 

Policy makers and academics desire accurate forecasts of economic variables. Economic theorists exploit the recent development in computation to write simple and complex models that can closely simulate reality. As such, an increasing need exists for large information sets to mimic economic relationships. Traditional econometric models, such as univariate time-series and multivariate VAR models, cannot easily accommodate large numbers of variables. Although popular when compared to traditional structural macroeconometric models for forecasting purposes, the VAR model exhibits serious limitations -- the issue of overparametrization. Thus, the main problem of small-scale models lies in choosing the correct variables to include. In practice, however, forecasters and policymakers believe that information from many series, which cannot be included simultaneously in a VAR model, can prove important in the forecasting exercise. 

Bernanke and Boivin (2003) argue that central banks monitor and analyze literally thousands of variables to inform their monetary policy decisions. Therefore, econometricians should consider the marginal benefits and marginal costs associated with increasing the amount of information brought to the forecasting exercise. The use of factor models significantly advances the accommodation of large panels of variables in forecasting exercises. Sargent and 

2 

Sims (1977) and Geweke (1977) introduce the dynamic factor approach to macroeconomics. They exploit the dynamic interrelationship of variables and then reduce the number of common factors even further. The method employed by Sargent and Sims (1977) and Geweke (1977), however, proves too restrictive, since it imposes orthogonality on the idiosyncratic components. Chamberlain (1983) and Chamberlain and Rothschild (1983) allow weak cross-sectional correlation of the idiosyncratic components. 

Recently, Stock and Watson (2002b), Kapetanios and Marcellino (2009) and Forni _et al_ . (2005) propose improved methods to account for serial correlation and weak cross-sectional correlation of the idiosyncratic components. Since this innovation can accommodate a large panel of variables in the forecasting exercise, increasing interest arises amongst universities, international organizations, central banks, and government agencies in the usage of these models. Much divergence in opinion remains as to whether factor models with large cross-section of time series will outperform traditional econometric models with a limited number of variables. Giannone and Matheson (2007), Van Nieuwenhuyze (2006), Cristadoro _et al_ . (2005), Forni _et al_ . (2005), Schneider and Spitzer (2004), Kabundi (2004), Forni _et al_ . (2001), Stock and Watson (2002a, 2002b, 1999, 1991, 1989), and Gupta _et al._ (2009) provide evidence of improvement in forecasting performance of macroeconomic variables using such factor analysis. Schumacher (2007), Schumacher and Dreger (2004), Gosselin and Tkacz (2001) and Angelini _et al_ . (2001) find no or only minor improvements in forecasting ability. 

What explains this difference in outcomes? Banerjee _et al_ . (2005), for example, find that small models forecast macroeconomic variables better than factor-augmented models. In addition, they also report that the performance of factor-augmented models differs across countries. Factor-augmented models perform better at forecasting real variables but worse at nominal variables in the US compared to the euro area. Furthermore, Boivin and Ng (2006) 

3 

claim that the composition of the dataset and the size of the cross-section dimension matter in producing better forecasts with factor-augmented models. In sum, the existing research suggests that idiosyncratic factors determine the best performing model. 

This paper uses a DSGE model developed by Iacoviello and Neri (2010) to forecast the US real house price index and its turning point in 2006:Q2 and compares the performance to that DSGE model to a series of time-series models. The Iacoviello and Neri (2010) model employs 10 variables in their DSGE specification. We also exploit the information content of 120 quarterly time-series variables, including the 10 variables in Iacoviello and Neri (2010) and the 110 macroeconomic variables in Boivin _et al._ (2009), in some of our other forecasting models.<sup>1</sup> We evaluate the forecasting performance of the DSGE model and the various time-series models relative to the Root Mean Squared Error (RMSE) of the out-of-sample forecasts of the random walk (RW) model. Moreover, with the exception of Wang (2008) and Gupta and Kabundi (2008), the comparison of a factor-augmented models and a DSGE model occurs rarely and, hence, deserves more attention. Note, allowing for a DSGE model as an alternative forecasting framework, helps us to compare between the “atheoretical” models, like the factor-augmented VAR and Bayesian VAR (BVAR) models with a microfounded theoretical model. 

We next examine the explanatory power of including information from a large set of economic variables, using dynamic factors or Bayesian shrinkage approaches. More specifically, we compare the out-of-sample forecasting performance of various time-series models – VAR, FAVAR, and various Bayesian time-series models. For the Bayesian models, we estimate BVAR, Bayesian factor augmented VAR (BFAVAR), and small- and large-scale BVAR (SBVAR and LBVAR) models. Based on the average root mean squared error for the one-, two-, 

> 1 Boivin _et al._ (2009) report 111 macroeconomic variables. One variable, the Treasury bill rate, also appears in the 10 variables in Iacoviello and Neri (2010). 

4 

three-, and four–quarters-ahead forecasts, we find that the small-scale Bayesian-shrinkage model (10 variables) outperforms the other models, even outperforming the large-scale Bayesianshrinkage model. Finally, we use ex ante forecasts of each model to identify the turning point in 2006:Q2, using the estimated model through 2005:Q2. Only the DSGE model actually forecasts a turning point with any accuracy, suggesting that attention to fundamentals and their interactions proves crucial in forecasting turning points. 

We organize the rest of the paper as follows. Section 2 outlines the DSGE model of Iacoviello and Neri (2010). Section 3 provides a brief review of the literature on using large data sets in forecasting models. Section 4 discusses the literature on forecasting house prices. Section 5 specifies the various time-series models estimated and used for forecasting. Section 6 discusses the data and the results. Section 7 concludes. 

## **2. The DSGE Model of Iacoviello and Neri (2010)** 

Iacoviello and Neri (2010) develop a DSGE model of the US economy to consider how shocks in the macreoeconomy affect events in the housing market and then how housing market adjustments spill over and affect the macroeconomy. We adopt their structural model of the macroeconomy to determine how this model performs with respect to various time-series models in forecasting real house prices as well as predicting the turning point in real house prices that occurred in 2006:Q2. 

The model differentiates between housing and non-housing goods. The household sector divides into patient (lenders) and impatient (borrowers) households. Both types of households work, consume, and accumulate housing. Impatient households face a binding collateral constraint in equilibrium, because they only accumulate the minimum down payment to obtaining the financing to buy their housing. The production process for housing combines capital, labor, and land to produce new homes. 

5 

Wholesale firms operate under competitive flexible prices and produce both housing and non-housing goods, using separable production technologies. Nominal rigidities exist in the nonhousing goods market with the assumption of monopolistic competition. The housing market, on the other hand, operates with flexible prices (Barsky _et al._ , 2007). The labor markets also adopt rigidities similar to the non-housing good market. Monetary policy uses a Taylor rule that adapts gradually to inflation and GDP growth. 

Heterogeneous trends exist in productivity across the consumption, non-residential, and housing sectors. Random shocks to productivity conform to first-order auto-correlated processes. Market equilibrium includes the consumption, housing, and loan markets, where goods market equilibrium includes consumption, business investment (accumulation of capital for consumption and housing production), and intermediate inputs. 

The final model includes 36 equations.<sup>2</sup> The data for construction of the model requires 10 variables – aggregate consumption, business fixed investment, residential investment, inflation, the nominal short-run interest rate, real house prices, hours in the consumption and housing sectors, and wage inflation in the consumption and housing sectors as well as a series of parameter choices. We adopt the same model, including the prior distributions on the parameters<sup>3</sup> , in our analysis. 

## **3. Forecasting with Large Data Sets** 

For forecasting purposes, time-series models generally perform as well as or better than dynamic structural econometric specifications. Zellner and Palm (1974) provide the theoretical rationalization.<sup>4</sup> An important issue involves determining how additional information can or 

> 2 See Appendix B of Iacoviello and Neri (2010). 

> 3 See Tables 3 and 4 in Iacoviello and Neri (2010). 

> 4 Any dynamic structural model implicitly generates a series of univariate time-series models for each endogenous variable. The dynamic structural model, however, imposes restrictions on the parameters in the reduced-form time- 

6 

cannot improve the forecasting performance over a simple univariate autoregressive or autoregressive-moving-average representation. 

One method uses “atheoretical” VAR models.<sup>5</sup> These models do not impose exogeneity assumptions on the included variables. Unlike the single-equation ARDL model, the VAR approach assumes that lagged values of each variable may provide valuable information in forecasting each endogenous variable. VAR models, however, face problems of overparameterization, since the number of parameters to estimate increases dramatically with additional variables or additional lags in the system.<sup>6</sup> Given this problem, one approach for using more data in the VAR model involves the extraction of common factors from a large data set that researchers can then add to the VAR specification (Bernanke _et al._ , 2005, Stock and Watson 2002, 2005). Adding several common factors from the large dataset to a VAR system economizes on the number of new parameters to estimate. 

BVAR models address the over-parameterization problem by specifying a small number of hyper-parameters that defines the relationships between all the parameters in the system. Since the Bayesian approach already solves the over-parameterization problem, researchers can add a large set of variables to the estimation of a BVAR system, obviating the need to extract common factors. Nothing prevents, however, the extraction of common factors from the large set of 

series specification. Dynamic structural models prove most effective in performing policy analysis, albeit subject to the Lucas critique. Time-series models prove most effective at forecasting. That is, in both cases errors creep in whenever the researcher makes a decision about the specification. Clearly, more researcher decisions relate to a dynamic structural model than a univariate time-series model, suggesting that fewer errors enter the time-series model and allowing the model to produce generally better forecasts. 

5 A simple approach, which we do not adopt in this paper, uses an autoregressive distributed lag (ARDL) model (Stock and Watson 1999, 2003, 2004). That is, the researcher runs an ARDL, or transfer function, model, where the variable to forecast enters as an autoregressive process and one driver variable enters as a distributed lag. The researcher compares the baseline model, the pure autoregressive specification forecasts with the forecasts for the ARDL specification. Extending this further, the researcher can repeat the process for a whole series of potential driver variables. In this extended case, one aggregates across all of the individual forecasts to generate the combined forecast. Combination forecasts range from simple means or medians to more complicated principal-components- or mean-square-forecast-error-weighted forecasts. 

> 6 The implementation of the ARDL approach avoids the problem by only using bivariate transfer function models and then combining the forecasts from the different bivariate analyses. 

7 

macroeconomic variables to include in a factor-augmented VAR and BVAR systems, which we also do. 

In the factor-augmented approach, the researcher potentially leaves information on the table by only extracting the common factor information and leaving the remaining information out of the analysis. On the other hand, the Bayesian approach, includes all the information from 

the large set of data, but restricts the estimation by imposing conditions on the parameters of the estimating equation. In sum, all methods introduce restrictions on the way information from the large dataset affects the estimation process. Thus, any of the individual approaches may lead to better forecasts _a priori_ . 

In this paper, we consider the factor-augmented and large-scale Bayesian methods for incorporating the information from a large dataset.<sup>7</sup> These methods provide the natural extension of the VAR and BVAR models.<sup>8</sup> 

## **4. Forecasting House Prices** 

Traditionally, the housing market and its cycle played an important role in understanding the business cycle. More recently, several authors argue that asset prices help forecast both inflation and output (Forni _et al._ , 2003; Stock and Watson, 2003, Gupta and Das, forthcoming, 2008, Das _et al._ , forthcoming a, forthcoming b, and 2009). Since homes imbed much individual wealth, house price movements may provide important signals for consumption, output, and inflation. That is, housing market adjustments play an important role in the business cycle (Iacoviello and Neri, 2010), not only because housing investment proves a volatile component of demand (Bernanke and Gertler, 1995), but also because house price changes generate important wealth 

> 7 We also include a small-scale Bayesian-shrinkage model that includes the 10 variables in the Iacoviello and Neri (2010) DSGE model. 

> 8 The ARDL model involves a single-equation, whereas the VAR and BVAR models involve multiple equations. Thus, we exclude the ARDL approach from our analysis. 

8 

effects on consumption (International Monetary Fund, 2000) and investment (Topel and Rosen, 1988). 

In sum, models that forecast real house price inflation can give policy makers an idea about the future direction of the overall macroeconomy and, hence, can provide important information for designing better and more-appropriate policies. In other words, the housing sector acts as a leading indicator for the real sector of the economy. The recent world-wide credit crunch began with the end of the run-up in the US real house price index with a dramatic fall in that index, which, in turn, led the real sector of the world’s economy toward an economic slump. 

The existing literature on forecasting house prices considers whether economic fundamentals provide sufficient information. A large number of economic variables affect house price growth (Cho, 1996; Abraham and Hendershott, 1996; Johnes and Hyclak, 1999; and Rapach and Strauss, 2007, 2009). For instance, income, interest rates, construction costs, labor market variables, stock prices, industrial production, consumer confidence index, and so on act as potential predictors. On these issues, Quigly (1999) and Wheaton and Nechayev (2008) compare the forecasting performance of models with and without fundamentals. Quigley (1999) concludes that models including only fundamentals explain less than half of the movement in house prices. Further, he argues that explaining turning points in house prices improves in models that include fundamentals, but still do not predict such turning points well. Wheaton and Nechayev (2008) also consider the role of fundamentals in explaining house price movements. They estimate autoregressive models in the house price augmented by fundamentals. They conclude that in all 59 housing markets, the models that include fundamentals underpredict the house price run up from 1998 to 2005. 

Most models that forecast US house prices focus on regional, state, or MSA levels of analysis and do not consider the national house price index. Several papers implement techniques 

9 

that relate to our paper. Rapach and Strauss (2007, 2009) consider forecasting house prices in states, using a large data set of economic variables. Rapach and Strauss (2007) use an autoregressive distributed lag (ARDL) model framework, containing 25 determinants, to forecast real house price growth for the individual states of the Federal Reserve’s Eighth District – Arkansas, Illinois, Indiana, Kentucky, Missouri, Mississippi, and Tennessee. Given the difficulty in determining _a priori_ the particular variables that prove the most important in forecasting real house price growth, the authors also use various methods to combine the individual ARDL model forecasts, which result in better forecast of real house price growth. Rapach and Strauss (2009) perform the same analysis for the 20 largest US states based on ARDL models containing large number of potential predictors, including state, regional and national level variables. Once again, the authors reach similar conclusions on the importance of combining forecasts. 

Das _et al._ , (forthcoming b) consider the forecasting performance of regional real house price growth rates in the nine US Census regions, using FAVAR and LBVAR models. They find that the FAVAR models generally outperform the LBVAR models. Gupta, Kabundi, and Miller (2009) consider the forecasting performance of time-series models with and without 308 monthly variables and spatial specifications for the 20 largest US states and corroborate the general findings of Das _et al._ (forthcoming b) in that factor augmented models generally outperform large-scale models. Finally, based on principal component analysis and Bayesian regression, Gupta and Kabundi (2009) reach similar conclusions when forecasting the aggregate US real house price using 112 monthly variables. 

Our paper extends the above mentioned studies by considering a DSGE model in addition to various time-series models with and without fundamentals to forecast the US real house price index out of sample and to forecast the turning point of the run-up of the US real house price index. 

10 

## **5. VAR, BVAR, FAVAR, FABVAR, and LBVAR Specifications and Estimation**<sup>**9**</sup> 

_5.1 VAR, BVAR, and LBVAR:_ 

Following Sims (1980), we can write an unrestricted VAR model as follows: 



where _y_ equals a ( _n_ × 1) vector of variables to forecast; _A_ 0 equals an ( _n_ × 1) vector of constant _10_ terms; _A(L)_ equals an ( _n_ × _n_ ) polynomial matrix in the backshift operator _L_ with lag length _p,_ 2 and ε equals an ( _n_ × 1) vector of error terms. In our case, we assume that ε ~ _N_ (0, σ _In_ ) , where 

_In_ equals an ( _n_ × _n_ 

) identity matrix. 

The VAR method typically use equal lag lengths for all variables, which implies that the researcher must estimate many parameters, including many that prove statistically insignificant. This over-parameterization problem can create multicollinearity and a loss of degrees of freedom, leading to inefficient estimates, and possibly large out-of-sample forecasting errors. Some researchers exclude lags with statistically insignificant coefficients. Alternatively, researchers use near VAR models, which specify unequal lag lengths for the variables and equations. 

Litterman (1981), Doan _et al.,_ (1984), Todd (1984), Litterman (1986), and Spencer (1993) use the BVAR model to overcome the over-parameterization problem. Rather than eliminating lags, the Bayesian method imposes restrictions on the coefficients across different lag lengths, assuming that the coefficients of longer lags may more closely approach zero than the coefficients on shorter lags. If, however, stronger effects come from longer lags, the data can override this initial restriction. Researchers impose the constraints by specifying normal prior 

> 9 The discussion in this section relies heavily on LeSage (1999), Gupta and Sichei (2006), Gupta (2006), Gupta and Miller (2009a, 2009b), and Das _et al_ ., (2009). 

> 10 2 _p_ That is, _A(L)_ = _A L_ 1 + _A_ 2 _L_ + ... + _Ap L_ ; 

11 

distributions with zero means and small standard deviations for most coefficients, where the standard deviation decreases as the lag length increases and implies that the zero-mean prior holds with more certainty. The first own-lag coefficient in each equation proves the exception with a unitary mean. Finally, Litterman (1981) imposes a diffuse prior for the constant. We employ this “Minnesota prior” in our analysis, where we implement Bayesian variants of the classical VAR models. 

Formally, the means of the Minnesota prior take the following form: 



where<sup>β</sup> _i_<sup>equals the coefficients associated with the lagged dependent variables in each equation</sup> of the VAR model (i.e., the first own-lag coefficient), while β _j_ equals any other coefficient. In sum, the prior specification reduces to a random-walk with drift model for each variable, if we set all variances to zero. The prior variances, σ<sup>β</sup> 2 _i_ and σβ 2 _j_ , specify uncertainty about the prior 

means,<sup>β</sup> _i_<sup>= 1, and</sup> β _j_ = 0. We also adopt the specification in Banbura _et al_ . (forthcoming) and Bloor and Matheson (2008), whereby we set a white-noise prior (i.e.,<sup>β</sup> _i_<sup>= 0) for those variables</sup> in the data sets (i.e., comprising of 10 or 120 variables) that exhibit mean-reversion. Otherwise, we impose the random walk prior, described above. 

Doan _et al.,_ (1984) propose a formula to generate standard deviations that depend on a small numbers of hyper-parameters: _w, d_ , and a weighting matrix _f_ ( _i, j_ ) to reduce the overparameterization in the VAR models. This approach specifies individual prior variances for a large number of coefficients, using only a few hyper-parameters. The specification of the standard deviation of the distribution of the prior imposed on variable _j_ in equation _i_ at lag _m_ , for all _i, j_ and _m_ , equals _S(i, j, m)_ , defined as follows: 

12 



where _f_ ( _i, j_ ) = _1_ , if _i = j_ and<sup>_k_</sup> _ij_ otherwise, with ( 0 ≤<sup>_k_</sup> _ij_ ≤ 1), and _g(m)_ = _m_<sup>−</sup> _d_ , with _d > 0_ . The σ estimated standard error of the univariate autoregression for variable _i_ equals ˆ σ _i_ . The ratio<sup>ˆ</sup><sup>_i_</sup> σ ˆ _j_ scales the variables to account for differences in the units of measurement and, hence, causes the specification of the prior without consideration of the magnitudes of the variables. The term _w_ indicates the overall tightness, with the prior getting tighter as the value falls. The parameter _g(m)_ measures the tightness on lag _m_ with respect to lag 1, and equals a harmonic shape with decay factor _d_ , which tightens the prior at longer lags. The parameter _f_ ( _i, j_ ) equals the tightness of variable _j_ in equation _i_ relative to variable _i_ , and by increasing the interaction (i.e., the value of 

> <sup>), we loosen the prior.</sup> 11 

> <sup>_k_</sup> _ij_ 

We estimate the alternative BVARs using Theil's (1971) mixed estimation technique. Essentially, the method involves supplementing the data with prior information on the distribution of the coefficients. The number of observations and degrees of freedom increase artificially by one for each restriction imposed on the parameter estimates. Thus, the loss of degrees of freedom from over-parameterization in the classical VAR models does not emerge as a concern in the alternative BVAR specifications. We consider the following VAR specifications: 

- VAR: In addition to the univariate autoregressive model (AR) with eight lags in the US real house price index, we also run a 10-variable VAR, incorporating the 10 variables in Iacoviello and Neri (2010); 

> 11 For an illustration, see Dua and Ray (1995). 

13 

- UBVAR: This benchmark univariate BVAR model uses only the US real house price index; 

- SBVAR: The small-scale BVAR model includes only the 10 variables in Iacoviello and Neri (2010); and 

- - LBVAR: The large-scale BVAR model includes the 10 variables in Iacoviello and Neri (2010) plus the 110 additional variables from Bovin _et al._ (2009). 

## _5.2 FAVAR and BFAVAR:_ 

This study also uses the Dynamic Factor Model (DFM) to extract common components between macroeconomic series and then uses these common components to forecast the US real house price index, adding the extracted factors to univariate and multivariate VAR and BVAR models to create FAVAR and BFAVAR models in the process. Furthermore, we estimate idiosyncratic component (see below) with AR( _p_ ) processes as suggested by Boivin and Ng (2005). 

The DFM expresses individual times series as the sum of two unobserved components: a common component driven by a small number of common factors and an idiosyncratic component for each variable. The DFM extracts the few factors that explain the co-movement of the US economy. Forni _et al._ (2005) demonstrate that for a small number of factors relative to the number of variables and a heterogeneous panel, we can recover the factors from present and past observations. 

Consider a _n_ × 1 covariance stationary process _Yt_ = ( _y_ 1 _t_ ,...., _ynt_ )'. Suppose that _X t_ equals the standardized version of<sup>_Y_</sup> _t_ . Under DFM, we write _X t_ as the sum of two orthogonal components as follows: 



where<sup>_F_</sup> _t_ equals a _r_ × 1 vector of static factors, λ equals an _n_ × _r_ matrix of factor loadings, and 

14 

> <sup>ξ</sup> _t_<sup>equals a</sup> _n_ × 1 vector of idiosyncratic components. In a DFM,<sup>_F_</sup> _t_ and<sup>ξ</sup> _t_<sup>are mutually</sup> 

orthogonal stationary process, while, χ _t_ = λ _Ft_ equals the common component. 

Since dynamic common factors are latent, we must estimate them. We note that the estimation technique used matters for factor forecasts. This paper adopts the Stock and Watson (2002b) method, which employs the static principal component approach (PCA) on _X t_ . The factor estimates, therefore, equal the first principal components of _X t_ , (i.e.,<sup>_F_</sup> ˆ _t_<sup>= Λ</sup> ˆ ′ _X t_ , where Λ ˆ equals the _n_ × _r_ matrix of the eigenvectors corresponding to the _r_ largest eigenvalues of the ˆ sample covariance matrix Σ ). 

For forecasting purposes, we use a univariate and a multivariate VAR augmented by extracted common factors using the Stock and Watson (2002a) approach. This approach is similar to the univariate static, unrestricted approach of Bovin and Ng (2005). Therefore, the forecasting equation to predict<sup>_Y_</sup> _t_ is given by 



where _h_ equals the forecasting horizon, Φ ˆ ( _L_ ) equal lag polynomials, which we estimate with and without restrictions. As Boivin and Ng (2005) clearly note, VAR models are special cases of equation (5). With known factors and the parameters, the FAVAR approach should produce smaller mean squared errors. In practice, however, one does not observe the factors and we must estimate them. Moreover, the forecasting equation should reflect a correct specification. We consider the following DFM specifications: 

15 

- UFAVAR: Includes the US real house price index and the common static factors;<sup>12</sup> 

- MFAVAR: Includes the 10 variables in Iacoviello and Neri (2010) and the common static factors; 

- BUFAVAR:  The Bayesian version that includes the US real house price index and the common static factors; and 

- BMFAVAR: The Bayesian version that includes the 10 variables in Iacoviello and Neri (2010) and the common static factors. 

## **6. Data Description, Model Estimation, and Results** 

- _6.1 Data_ 

While the univariate VARs, both the classical and Bayesian variants, include data of only the annualized US real house price index, the large-scale BVAR and the factor-augmented models also include the 120 quarterly series. In between, we estimate small-scale VARs and BVARs in the 10 variables employed by Iacoveillo and Neri (2010), including the US real house price index. The nominal US house price index comes from the Census Bureau House Price Index deflated by the implicit price deflator for the nonfarm business sector. In addition, we also employ the other nine variables identified in Iacoviello and Neri (2010). See Appendix A in their paper for a discussion of sources of data for these 10 variables as well as the transformations made to these variables. 

For the remaining 110 quarterly macroeconomic series of the US economy, we use the data set constructed by Boivin _et al._ (2009) that covers the period of 1976:01 to 2005:02. The data set includes measures of industrial production, several price indices, interest rates, employment as well as other key macroeconomic and financial variables. To this data set we add 

> 12 We also confirm the choice of the four factors by the cumulative variance share, under which, the fifth eigenvalue fell below the threshold of 5 percent. 

16 

10 of the variables used by Iacoviello and Neri (2010), implying a total of 120 variables. Note, we drop the Treasury bill rate from the original 111 variables in the Boivin _et al_ (2009) data set, since it appears in the Iacoviello and Neri data set. Moreover, since the Boivin _et al_ (2009) data set appears at a monthly frequency, we convert it into a quarterly frequency by taking averages for flow variables and the last month observation for the stock variables (i.e., we use temporal aggregation and systematic sampling, respectively, as suggested by the literature on frequency conversions). We seasonally adjust and transform all series to induce stationarity for the FAVAR.<sup>13</sup> Since this data set ends in 2005:Q2, our sample also ends at the same point. 

## _6.2 Estimation and Results_ 

This section reports our econometric findings. First, we select the optimal model for forecasting the US real house price index, using the minimum average root mean squared error (RMSE) across the one-, two-, three-, and four-quarter-ahead out-of-sample forecasts. Second, we consider the ability of the best models to predict the turning point in 2006:Q2, using ex ante and recursive forecasts. 

## _One- to Four-Quarter-Ahead Forecast Accuracy._ 

Following the existing literature on estimation of DSGE models and, of course, Iacoviello and 

Neri (2010), we consider the linearized DSGE model describing the equilibrium around the balanced growth path. Given the parameters, we represent the solution to the DSGE model in a state-space form that is used to compute the likelihood function. The estimation strategy follows a Bayesian approach, which involves transforming the data into a form suitable for computing the likelihood function, choosing prior distributions for the parameters of the DSGE model, and 

> 13 Using non-stationary data, however, is not required with the BVAR. Sims _et al._ (1990) indicate that with the Bayesian approach entirely based on the likelihood function, the associated inference does not require special treatment for non-stationarity, since the likelihood function exhibits the same Gaussian shape regardless of the presence of non-stationarity. 

17 

estimating their posterior distribution using the random-walk version of the Metropolis-Hastings algorithm. We estimate the DSGE model over the in-sample of 1976:Q1 to 2000:Q4 and then recursively over the out-of-sample horizon of 2001:Q1-2005:Q2, based on a sample of 500,000 draws. We use a normal jump distribution with the covariance matrix equal to the Hessian of the posterior density evaluated at the maximum. We choose the scale factor to obtain an acceptance rate of about 25 percent. We assessed convergence by comparing the moments computed by splitting the draws of the Metropolis into two halves.<sup>14</sup> 

Given the specification of priors in Section 4, we estimate the alternative univariate, small-, and large-scale models in our sample over the period 1976:Q1 to 2000:Q4 using quarterly data. We then compute out-of-sample one- to four-quarters-ahead forecasts for the period of 2001:Q1 to 2005:Q2, and compare the forecast accuracy relative to the forecasts generated by the RW model. Note that the choice of the in-sample period, especially the starting date, depends on data availability. The starting point of the out-of-sample period precedes the rapid run-up and then collapse of the house price index experienced over the last decade. As indicated above, the end-point of the horizon is 2005:Q2, since the Boivin _et al._ (2009) data on the 110 macroeconomic variables ends there. 

We estimate the univariate and multivariate versions of the classical VAR, the smallscale BVARs, the large-scale BVARs, and the classical and Bayesian FAVARs over the period 1976:Q1 to 2000:Q4, and then forecast from 2001:Q1 through 2005:Q2. Since we use eight lags<sup>15</sup> , the initial eight quarters from 1976:Q1 to 1976:Q4 feed the lags. We re-estimate the models each quarter over the out-of-sample forecast horizon in order to update the estimate of 

> 14 See Appendix C of Iacoviello and Neri (2010) for more details. 

> 15 The choice of 8 lags reflects the unanimity of the sequential modified LR test statistic, Akaike information criterion (AIC) and the final prediction error (FPE) criterion and the Hannan-Quinn (HQ) information criterion applied to the stable small-scale VAR estimated with ten variables. Note, stability, as usual, implies that no roots lie outside the unit circle. We retain the eight lags for all the “atheoretical” models. 

18 

the coefficients, before producing the four-quarters-ahead forecasts. We implemented this iterative estimation and the four-quarters-ahead forecast procedure for 15 quarters, with the first forecast beginning in 2001:Q1. This produced a total of 15 one-quarter-ahead forecasts, …, up to 15 four-quarters-ahead forecasts.<sup>16</sup> We calculate the root mean squared errors (RMSE)<sup>17</sup> for the 15 one-, two-, three-, and four-quarters-ahead forecasts for the real house price index of the models. We then examine the average of the RMSE statistic for one-, two-, three-, and fourquarters ahead forecasts over 2001:Q1 to 2005:Q2. 

> For the various Bayesian time-series models, we start with a value of _w_ = 0.1 and _d_ = 1.0, 

> and then increase the value to _w_ = 0.2 to account for more influences from variables other than the first own lags of the dependant variables of the model. In addition, as in Dua and Ray (1995), Gupta and Sichei (2006), Gupta (2006), and Gupta and Miller (2009a, 2009b), we also estimate 

> the BVARs and BFAVARs with _w_ = 0.3 and _d_ = 0.5. We also introduce _d = 2_ to increase the 

> tightness on lag _m_ . In addition, we follow Banbura _et al._ (forthcoming), Bloor and Matheson 

> (2008), and De Mol _et al._ (2008) in setting the value of the overall tightness parameter to obtain a desired average fit for the variable of interest (i.e., real US house price, in the in-sample period 

> from 1976:Q1 to 2000:Q4). We retain the optimal value of _w(Fit)_ (=0.006)<sup>18</sup> obtained in this 

> fashion for the entire evaluation period. Specifically, for a desired _Fit, w_ comes from the following optimization: 

> 16 For this, we used the Kalman filter algorithm in RATS, version 7.1. 



> of forecasts. 

> 18 Note that, in this case, _d_ =2 and<sup>_k_</sup> _ij_ =0.5. 

19 





error (MSE) evaluated using the training sample _t = 1,....._<sup>_T_</sup> 0 _-1_ , with<sup>_T_</sup> 0 being the beginning of 

the sample period and _p_ being the order of the AR model of the real US house price. _MSEi_ 0 

equals the _MSE_ of variable _i_ with the prior restriction imposed exactly ( _w_ =0). Finally, the baseline _Fit_ equals the relative MSE from the OLS-estimated AR model as follows: 



We select the model that produces the lowest average RMSE values as the ‘optimal’ specification. 

Table 1 reports the average of the one-, two-, three-, and four-quarter-ahead RMSEs across the various specifications. The benchmark for all forecast evaluations is the RW model forecast RMSEs. Thus, the 0.672 entry for the UFAVAR model for the four-quarter-ahead forecast means that the UFAVAR model experienced a forecast RMSE of only 67.2 percent of the forecast RMSE for the RW model. 

Several observations emerge. First, the Bayesian models forecast better than the benchmark RW model, whereas the non-Bayesian models generally do not. That is, the VAR, MVFAVAR, and the DSGE models perform worse than the benchmark. The AR(8) and UFAVAR models do perform better than the benchmark model, but they perform worse than every Bayesian model, save two – the LBVAR models with ( _w=0.3, d=0.5_ ) and ( _w=0.2, d=1_ ). 

Second, the SBVAR model with ( _w=0.3, d=0.5_ ) posts the best forecasting performance at all horizons, including the overall average, except for the four-quarter-ahead forecasts, where 

20 

the LBVAR model with ( _w=0.006, d=2_ ) does the best. In other words, the Bayesian models that include fundamentals utilized by Iacoviello and Neri (2010) in their DSGE model does the best job of forecasting out of sample. The average RMSE sees the SBVAR model improving over the benchmark RW model by 47 percent. 

_Forecasting the Turning Point._ Figure 1 illustrates that the US housing market experienced a marked reversal of the real house price index after the peaks in 2006:Q2. That is, the run-up in the house price index reverses itself in 2006:Q2 and then proceeds to fall. We expose our optimal forecast models to the acid test – predicting turning point. We estimate the optimal models based on the average RMSE from Table 1, using data through 2005:Q2. Next we forecast prices from 2005:Q3 through the end of the sample period in 2009:Q1, the last equal to a 15-quarter-ahead forecast. The results of this forecasting experiment appear in Tables 2. 

Examining the actual data, we see that the US real house price index peaked in 2006:Q2 at 102.41, but we also see secondary peaks in 2005:Q4 at 102.22 and 2007:Q1 at 102.08. After 2007:Q1, the index falls monotonically through the end of the sample in 2009:Q1, reaching a level of 83.72. 

The ex ante forecasting results exhibit several observations. First, most of the optimal forecasting models do not predict a turning point and rather forecast a continual rise in the index through the end of the sample in 2009:Q1. Two exceptions exist – the DSGE model and the optimal MVFAVAR model. Only the DSGE model, however, forecasts a turning point (i.e., 2006:Q3) close to the actual turning point. Moreover, the MVFAVAR model forecasts exceed the actual data by large margins (e.g., 130.73 versus 83.72 in 2009:Q1). Further, examining the correlations between that actual series and each of the forecast series, we see that only the DSGE model exhibits a positive correlation (i.e., 0.81). All other forecasts report a negative correlation with the actual series. In sum, the DSGE model performs better than the other models in 

21 

forecasting the actual series, which includes the turning point in 2006:Q2. On the other hand, while the DSGE model shows a turning point one quarter after the actual turning point, its forecasts uniformly over-predict the actual index numbers after the turning point (e.g., 100.67 versus 83.72 in 2009:Q1). 

Finally, we also report recursive forecasts from 2005:Q2 to 2009:Q1. That is, we first estimate the models through 2005:Q2 and then forecast one-quarter ahead to 2005:Q3. Then we add the observation 2005:Q3 to the sample and re-estimate the models and forecast one-quarter ahead to 2005:Q4. We continue this process until we estimate the models through 2008:Q4 and forecast 2009:Q1. Since the 110 variables reported in Boivin _et al._ (2009) only run through 2005:Q2, we only report recursive forecasts that use up to the 10 variables employed in Iacoviello and Neri (2010). We chose to report the results for the optimal SBVAR model with _w=0.3, d=0.5_ and the DSGE model. 

Table 3 reports the findings and Figure 3 illustrates the actual data as well as the DSGE and SBVAR forecasts. We see that the DSGE and SBVAR models follow the actual data more closely than for the ex ante forecasts, which is not a surprise since we update the estimation with new data in the recursive forecasts. The correlations between the actual series and the DSGE and the SBVAR models equal 0.93 and 0.87, respectively. Thus, although the margin is closer, the DSGE model still outperforms the SBVAR model in forecasting the movement in the actual data. 

Gupta and Miller (2009a, 2009b) in their analysis of Los Angeles, and Phoenix as well as 8 Southern California MSAs report that ex ante forecasts continuing increases in housing prides beyond the peaks in those series. Only for the recursive forecasts do they find estimates that follow the decline in house prices after their peak. In that regard, our DSGE ex ante forecasts provide the exception to the rule in that they follow the downward movement in the US real 

22 

house price index after its peak, albeit with an underprediction. 

## **7. Conclusion** 

We forecast the US real house price index, using various time-series models, both with and without the information content of 10 or 120 additional quarterly macroeconomic series. Two approaches exist for incorporating information from a large number of data series – extracting common factors (principle components) in a Factor-Augmented Vector Autoregressive (FAVAR) or Factor-Augmented Bayesian Vector Autoregressive (FABVAR) models or Bayesian shrinkage in a large-scale Bayesian Vector Autoregressive (LBVAR) models.<sup>19</sup> In addition, we also employ the DSGE model of Iacoviello and Neri (2010) as a dynamic structural method of forecasting the US real house price index. 

Using the period of 1976:Q1 to 2000:Q4 as the in-sample period and 2001:Q1 to 2005:Q2 as the out-of-sample horizon, we compare the forecast performance of the alternative models for one- to four-quarters ahead forecasts. Based on the average root mean squared error (RMSE) for the one-, two-, three-, and four–quarter-ahead forecasts, we find that the SBVAR model performs the best for the one-, two-, and three-quarter-ahead forecasts as well as for the average across all four horizons. The MVFAVAR model performs the best only at the fourquarter-ahead forecast horizon. The DSGE model performs poorly, never beating the benchmark RW model at any horizon. 

Finally, we also report ex ante and recursive forecasts of the actual US real house price index from 2005:Q3 to 2009:Q1. Interestingly, now the DSGE model performs better than the other forecasting models, even though the DSGE model exhibit a one- to four-quarter ahead 

> 19 Another approach also exists, the ADRL method. This approach estimates a series of bivariate transfer function models with forecasted variable as the dependent variable and then aggregates forecasts with various weighting methods. We do not pursue this single-equation method and only consider the multiple-equation FAVAR and LBVAR models. 

23 

forecasting performance that does not beat the benchmark RW model. 

In sum, the utilization of fundamental economic variables improves the forecasting performance over models that do not use such data. This conclusion, however, does not hold for the large data set of 120 macroeconomic variables, but seems to hold for the 10 fundamental economic variables in the DSGE model of Iacoveillo and Neri (2010). In other words, macroeconomic fundamentals do seem to matter when forecasting real house prices, but only certain fundamentals. Moreover, to forecast the peak of a house price run-up requires a forwardlooking microfounded dynamic stochastic (DSGE) model in the fundamental variables. 

## **References:** 

- Abraham, J. M., and Hendershott, P. H., (1996). Bubbles in Metropolitan Housing Markets. _Journal of Housing Research_ 7(2), 191–207. 

- Angelini, E., J. Henry, and Mestre, R., (2001). Diffusion Index-Based Inflation Forecasts for the Euro Area. Working Paper No. 61 ECB. 

- Banbura, M., Gianonne, D., and Reichlin, L., (forthcoming). Bayesian VARs with Large Panels. _Journal of Applied Econometrics_ . 

- Banerjee, A., Marcellino, M., and Masten, I., (2005). Leading Indicators for Euro-Area Inflation and GDP Growth. _Oxford Bulletin of Economics and Statistics_ 67(1), 785–814. 

- Barsky, R. B., House, C. L., and Kimball, M. S., (2007). Sticky-Price Models and Durable Goods. _American Economic Review_ 97(3), 984-998. 

- Bernanke, B., and Boivin, J., (2003). Monetary Policy in a Data-Rich Environment. _Journal of Monetary Economics_ 50(3), 525–546. 

- Bernanke, B. S., Boivin, J., and Eliazs, P., (2005). Measuring the Effects of Monetary Policy: A Factor-Augmented Vector autoregressive (FAVAR) Approach, _The Quarterly Journal of Economics_ 120(1), 387–422. 

- Bernanke, B., and Gertler, M., (1995). Inside the Black Box: the Credit Channel of Monetary Transmission. _Journal of Economic Perspectives_ 9(4), 27–48. 

- Bloor, C., and Matheson, T., (2008). Analysing Shock Transmission in a Data-Rich Environment: A Large BVAR for New Zealand. _Reserve Bank of New Zealand Discussion Paper Series_ DP2008/09 _._ 

24 

- Boivin, J., and Ng, S., (2005). Undertanding and Comparing Factor Based Forecasts. _International Journal of Central Banking_ 1(3), 117-152. 

- Boivin, J., and Ng, S., (2006). Are More Data Always Better for Factor Analysis? _Journal of Econometrics_ 132(1), 169–194. 

- Boivin, J., Giannoni, M. P., and Mihov, I., (2009). Sticky Prices and Monetary Policy: Evidence from Disaggregated US Data. _American Economic Review_ 99(1), 350-384. 

- Chamberlain, G., (1983). Funds, Factors, and Diversification in Arbitrage Pricing Models. _Econometrica_ 51(5), 1281–1304. 

- Chamberlain, G., and Rothschild, M., (1983). Arbitrage, Factor Structure and Mean-Variance Analysis in Large Markets. _Econometrica_ 51(5), 1305–1324. 

- Cristadoro, R., Forni, M., Reichlin, L., and Veronese, G., (2005). A Core Inflation Indicator for the Euro Area. _Journal of Money, Credit and Banking_ 37(3), 539–560. 

- Das, S., Gupta, R., and Kabundi, A., (2009). Could We Have Predicted the Recent Downturn in the South African Housing Market? _Journal of Housing Economics_ , 18(4), 325 - 335. 

- Das, S., Gupta, R., and Kabundi, A., (forthcoming a). Is a DFM Well-Suited for Forecasting Regional House Price Inflation?” _Journal of Forecasting_ . 

- Das, S., Gupta, R., and Kabundi, A., (forthcoming b). The Blessing of Dimensionality in Forecasting Real House Price Growth in the Nine Census Divisions of the US. _Journal of Housing Research_ . 

- De Mol, C., Giannone, ., and Reichlin, L., (2008). Forecasting Using a Large Number of Predictors: Is Bayesian Regression a Valid Alternative to Principal Components? _Journal of Econometrics_ 146(2), 318-328. 

- Doan, T. A., Litterman, R. B., and Sims, C. A., (1984). Forecasting and Conditional Projections Using Realistic Prior Distributions. _Econometric Reviews_ 3(1), 1-100. 

- Dua, P., and Miller, S. M., (1996). Forecasting Connecticut Home Sales in a BVAR Framework Using Coincident and Leading Indexes. _Journal of Real Estate Finance and Economics_ 13(3), 219-235. 

- Dua, P., Miller, S. M., and Smyth, D. J., (1999). Using Leading Indicators to Forecast U. S. Home Sales in a Bayesian Vector Autoregressive Framework. _Journal of Real Estate Finance and Economics_ 18(2), 191-205. 

- Dua, P., and Ray, S. C., (1995). A BVAR Model for the Connecticut Economy. _Journal of Forecasting_ 14(3), 167-180. 

25 

- Dua, P., and Smyth, D. J., (1995). Forecasting U. S. Home Sales using BVAR Models and Survey Data on Households’ Buying Attitude for Homes. _Journal of Forecasting_ 14(3), 217-227. 

- Forni, M., Hallin, M., Lippi, M., and Reichlin, L., (2001). Coincident and Leading Indicators for the EURO Area. _The Economic Journal_ 111(471), 62-85. 

- Forni, M., Hallin, M., Lippi, M., and Reichlin, L., (2005). The Generalized Dynamic Factor Model, One Sided Estimation and Forecasting. _Journal of the American Statistical Association_ 100(471), 830–840. 

- Geweke, J., (1977). The Dynamic Factor Analysis of Economic Time Series. In _Latent Variables in Socio-Economic Models,_ (Aigner, and A. Goldberger, eds.). Amsterdam: North Holland, 365–383. 

- Giannone, D., and Matheson, T. D., (2007). A New Core Inflation Indicator for New Zealand. _International Journal of Central Banking_ 3(4), 145-180. 

- Gosselin, M.-A., and Tkacz, G., (2001). Evaluating Factor Models: An Application to Forecasting Inflation in Canada. Working Paper No. 18 Bank of Canada. 

- Gupta, R., (2006). Forecasting the South African Economy with VARs and VECMs. _South African Journal of Economics_ 74(4), 611-628 _._ 

- Gupta, R., and Das, S., (forthcoming). Predicting Downturns in the US Housing Market. _Journal of Real Estate Economics and Finance,_ in press _._ 

- Gupta, R., and Das, S., (2008). Spatial Bayesian Methods for Forecasting House Prices in Six Metropolitan Areas of South Africa. _South African Journal of Economics_ 76(2), 298-313 _._ 

- Gupta, R., and Kabundi, A., (2008). A Large Factor Model for Forecasting Macroeconomic Variables in South Africa. Working Paper No. 200815, Department of Economics, University of Pretoria. <u>http://ideas.repec.org/p/pre/wpaper/200815.html.</u> 

- Gupta, R., and Kabundi, A., (2009). Forecasting Real US House Price: Principal Components Versus Bayesian Regressions. Working Paper N. 200907, Department of Economics, University of Pretoria. <u>http://ideas.repec.org/p/pre/wpaper/200907.html.</u> 

- Gupta, R., and Miller, S. M., (2009a). “Ripple Effects” and Forecasting Home Prices in Los Angeles, Las Vegas, and Phoenix. University of Nevada, Las Vegas, Working Paper No. 0902. <u>http://ideas.repec.org/p/nlv/wpaper/0902.html.</u> 

- Gupta, R., and Miller, S. M., (2009b). The Time-Series Properties on Housing Prices: A Case Study of the Southern California Market. University of Nevada, Las Vegas, Working Paper No. 0912. <u>http://ideas.repec.org/p/nlv/wpaper/0912.html.</u> 

26 

- Gupta, R., Kabundi, A., and Miller S. M., (2009). Using Large Data Sets to Forecast Housing Prices: A Case Study of Twenty US States. University of Nevada, Las Vegas, Working Paper No. 0912. <u>http://ideas.repec.org/p/nlv/wpaper/0916.html.</u> 

- Gupta, R., and Sichei, M. M., (2006). A BVAR Model for the South African Economy. _South African Journal of Economics_ 74(3), 391-409 _._ 

- Iacoviello, M., and Neri, S., (2010). Housing Market Spillovers: Evidence from an Estimated DSGE Model. _American Economic Journal: Macroeconomics,_ in press. 

- International Monetary Fund, (2000). _World Economic Outlook: Asset Prices and the Business Cycle_ . 

- Johnes, G., and Hyclak, T., (1999). House Prices and Regional Labor Markets. _Annals of Regional Science_ 33(1), 33–49. 

- Kabundi, A., (2004). Estimation of Economic Growth Using Business Survey Data. International Monetary Fund, Working Paper No. 04/69. 

- Kapetanios, G., and Marcellino, M., (2009). A Parametric Estimation Method for Dynamic Factor Models of Large Dimensions. _Journal of Time Series Analysis_ 30(2): 208-238. 

LeSage, J. P., (1999). _Applied Econometrics Using MATLAB_ , www.spatial-econometrics.com. 

- Litterman, R. B., (1981). A Bayesian Procedure for Forecasting with Vector Autoregressions. _Working Paper_ , Federal Reserve Bank of Minneapolis. 

- Litterman, R. B., (1986). Forecasting with Bayesian Vector Autoregressions – Five Years of Experience. _Journal of Business and Economic Statistics_ 4(1), 25-38. 

- Niemira, M. P., and Klein, P. A., (1994). _Forecasting Financial and Economic Cycles._ New York: John Wiley & Sons, Inc. 

- Quigley, J. M., (1999). Real Estate Prices and Economic Cycles. _International Real Estate Review_ 2(1), 1-20. 

- Rapach, D. E., and Strauss, J. K., (2007). Forecasting Real Housing Price Growth in the Eighth District States. Federal Reserve Bank of St. Louis. _Regional Economic Development_ 3(2), 33–42. 

- Rapach, D. E., and Strauss, J. K., (2009). Differences in Housing Price Forecast Ability Across U.S. States. _International Journal of Forecasting_ 25(2), 351-372. 

- Sargent, T. J., and Sims, C,. A., (1977). Business Cycle Modelling without Predenting to Have Too Much a Priori Economic Theory. In _New Methods in Business Research_ (C. Sims, eds.) Federal Reserve Bank of Minneapolis. 

27 

- Schneider, M., and Spitzer, M., (2004). Forecasting Austrian GDP Using the Generalized Dynamic Factor Model. Oesterreichische National Bank, Working Paper No. 89. 

- Schumacher, C., (2007). Forecasting German GDP Using Alternative Factor Models Based on Large Datasets. _Journal of Forecasting_ 26(4), 271–302. 

- Schumacher, C., and Dreger, C., (2004). Estimating Large-Scale Factor Models for Economic Activity in Germany: Do They Outperform Simpler Models? _Jahrbücher fùr Nationalökonomie und Statistik_ 224(6), 731–750. 

Sims, C. A., (1980). Macroeconomics and Reality. _Econometrica_ 48(1), 1-48. 

- Spencer, D. E., (1993). Developing a Bayesian Vector Autoregression Model. _International Journal of Forecasting_ 9(3), 407-421. 

- Stock, J. H., and Watson, M. W., (1989). New Indexes of Coincident and Leading Economic Indicators. _NBER Macroeconomics Annual,_ 351-393. 

- Stock, J. H., and Watson, M. W., (1991). A Probability Model of the Coincident Indicators. In _Leading Economic Indicators: New Approaches and Forecasting Record_ (K. Lahiri, and G. Moore, eds.) Cambridge: Cambridge University Press, 63–95. 

- Stock, James H., and Watson, M. W., (1999). Forecasting Inflation. _Journal of Monetary Economics 44_ (2), 293-335. 

- Stock, J. H., and Watson, M.W., (2002a). Forecasting Using Principal Components from a Large Number of Predictors. _Journal of the American Statistical Association_ 97(460), 147–162. 

- Stock, J. H., and Watson, M. W., (2002b). Macroeconomics Forecasting Using Diffusion Indexes, _Journal of Business and Economic Statistics_ 20(2), 147–162. 

- Stock, J. H., and Watson, M.W., (2003). Forecasting Output and Inflation: The Role of Asset Prices. _Journal of Economic Literature_ 41(3), 788-829. 

- Stock, J. H., and Watson, M. W., (2004). Combination Forecasts of Output Growth in a SevenCountry Data Set. _Journal of Forecasting 23_ (6), 405-430. 

- Stock, J. H., and Watson, M. W., (2005). Implications of Dynamic Factor Models for VAR Analysis. NBER Working Paper No. 11467. 

- Todd, R. M., (1984). Improving Economic Forecasting with Bayesian Vector Autoregression. _Quarterly Review_ , Federal Reserve Bank of Minneapolis, Fall, 18-29. 

- Topel, R. H., and Rosen, S., (1988). Housing Investment in the United States. _Journal of Political Economy_ 96(4), 718–740. 

28 

- United States Department of Commerce, (1977). Composite Indexes of Leading, Coincident, and Lagging Indicators: A Brief Explanation of Their Construction. In _Handbook of Cyclical Indicators, A Supplement to the Business Conditions Digest._ Washington, D.C.: Bureau of Economic Analysis, May, 73-76. 

- United States Department of Commerce, (1984). Composite Indexes of Leading, Coincident, and Lagging Indicators: A Brief Explanation of Their Construction. In _Handbook of Cyclical Indicators, A Supplement to the Business Conditions Digest._ Washington, D.C.: Bureau of Economic Analysis, May, 65-70. 

- Van Nieuwenhuyze, C., (2006). A Generalized Dynamic Factor Model for the Belgian Economy Identification of the Business Cycle and GDP Growth Forecasts. _Journal of Business Cycle Measurement and Analysis_ 2005(2), 213–248. 

- Vargas-Silva, C., (2008a). The Effect of Monetary Policy on Housing: A Factor Augmented Approach. _Applied Economics Letters_ 15(10), 749-752. 

- Wang, T., (2008). Comparing the DSGE Model with the Factor Model: An Out-of- Sample Forecasting Experiment, Deutsche Bundesbank Discussion Paper Series 1: Economic Studies 2008/04. 

- Wheaton, W. C., and Nechayev, G., (2008). The 1998-2005 Housing “Bubble” and the Current “Correction”: What’s Different This Time? _Journal of Real Estate Research_ 30(1), 1-26. 

- Zellner, A., and Palm, F., (1974). Time Series Analysis and Simultaneous Equation Econometric Models. _Journal of Econometrics_ 2(1), 17-54. 

29 

**Table 1: One to Four-Quarters-Ahead RMSEs for the Real US House** **<u>Price Index</u>** 

||||**Q**|**uarters Ah**|**ead**||
|---|---|---|---|---|---|---|
||**Models**|**1**|**2**|**3**|**4**|**Average**|
||**AR(8)**|0.8974|0.7976|0.7379|0.7784|0.8028|
||**VAR**|1.3565|1.2213|1.0199|0.8888|1.1216|
||**UFAVAR**|0.9480|0.8730|0.7210|0.6721|0.8035|
||**MFAVAR**|1.6070|1.2293|1.1515|0.9186|1.2266|
||**DSGE**|1.1666|1.1888|1.1863|1.1193|1.1653|
||**UBVAR**|0.8540|0.7372|0.6534|0.6878|0.7331|
||**BUFAVAR**|0.8017|0.6694|0.5421|0.5711|0.6461|
|**w=0.3,d=0.5**|**BMFAVAR**|0.7580|0.6337|0.4438|0.4472|0.5706|
||**SBVAR**|**0.7372***|**0.5810***|**0.3880***|0.4119|**0.5295***|
||**LBVAR**|0.8952|0.9540|0.7514|0.6776|0.8195|
||**UBVAR**|0.8631|0.7517|0.6633|0.6902|0.7421|
||**BUFAVAR**|0.8655|0.7640|0.6713|0.6988|0.7499|
|**w=0.2,d=1**|**BMFAVAR**|0.7711|0.6651|0.5056|0.5434|0.6213|
||**SBVAR**|0.7732|0.6410|0.4868|0.5239|0.6062|
||**LBVAR**|0.9064|0.9153|0.7218|0.7124|0.8140|
||**UBVAR**|0.8696|0.7567|0.6606|0.6792|0.7415|
||**BUFAVAR**|0.8808|0.7771|0.6867|0.7089|0.7634|
|**w=0.1,d=1**|**BMFAVAR**|0.8531|0.7612|0.6504|0.6762|0.7352|
||**SBVAR**|0.8453|0.7368|0.6221|0.6443|0.7121|
||**LBVAR**|0.9332|0.8892|0.6772|0.6886|0.7971|
||**UBVAR**|0.8614|0.7379|0.6303|0.6406|0.7175|
||**BUFAVAR**|0.9026|0.7972|0.7042|0.7124|0.7791|
|**w=0.2,d=0.2**|**BMFAVAR**|0.8062|0.7309|0.5896|0.6200|0.6867|
||**SBVAR**|0.8153|0.7191|0.5874|0.6136|0.6839|
||**LBVAR**|0.9095|0.8579|0.6842|0.7116|0.7908|
||**UBVAR**|0.8598|0.7349|0.6269|0.6347|0.7140|
||**BUFAVAR**|0.8809|0.7645|0.6659|0.6783|0.7474|
|**w=0.1,d=2**|**BMFAVAR**|0.8664|0.7819|0.6758|0.6935|0.7544|
||**SBVAR**|0.8611|0.7632|0.6554|0.6692|0.7372|
||**LBVAR**|0.9138|0.8251|0.6170|0.6490|0.7512|
|**w(Fit)=0.006,d=2**|**LBVAR**|0.8174|0.6249|0.4139|**0.3909***|0.5618|



30 

## **Table 1: One to Four-Quarters-Ahead RMSEs for the Real US House Price Index (continued)** 

- Note: The numbers equal the ratio of the root-mean square error (RMSE) of the Model in the row divided by the RMSE of the random walk (RW) model. The starred and bolded numbers equal the minimum values in each column. AR(8) is the autoregressive model with 8 lags. VAR is the vector autoregressive model. UFAVAR is the univariate factor-augmented VAR model. MFAVAR is the multivariate FAVAR model. DSGE is the dynamic structural general equilibrium model. UBVAR is the univariate Bayesian VAR model. BUFAVAR is the Bayesian univariate FAVAR model. BMFAVAR is the Bayesian multivariate FAVAR. SBVAR is the small Bayesian VAR model and the LBVAR is the large BVAR model. The average column computes the average RMSE of the one-, two-, three-, and four-quarter-ahead RMSE reported in columns 1, 2, 3 and 4. 

31 

## **Table 2: Ex Ante Forecasts for the Real US House Price Index** 

|**Date**|**Actual**|**RW**|**AR(8)**|**VAR**|**DSGE**|**UFAVAR**|**MFAVAR**|**UBVAR**|**BUFAVAR**|**SBVAR**|**BMFAVAR**|**LBVAR**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**2005:Q2**|99.59|99.59|99.59|99.59|99.59|99.59|99.59|99.59|99.59|99.59|99.59|99.59|
|**2005:Q3**|100.74|101.88|101.77|104.47|101.04|101.97|110.92|101.97|103.51|103.91|102.50|102.31|
|**2005:Q4**|102.22|102.71|102.42|103.16|101.36|102.53|105.38|102.47|102.88|105.12|103.18|103.48|
|**2006:Q1**|101.58|103.52|103.88|104.96|101.70|103.64|105.95|103.58|104.64|106.58|104.49|104.62|
|**2006:Q2**|**102.41***|104.34|104.97|105.67|101.92|104.81|115.66|104.86|105.21|107.45|105.27|105.73|
|**2006:Q3**|101.07|105.17|105.94|104.27|**102.01***|105.37|116.64|105.29|104.31|106.84|105.59|106.85|
|**2006:Q4**|99.75|105.98|106.84|107.62|101.95|105.98|124.36|106.02|106.92|109.10|106.99|108.01|
|**2007:Q1**|102.08|106.80|107.52|107.25|101.81|106.95|127.76|106.98|106.85|111.46|107.73|109.21|
|**2007:Q2**|100.54|107.63|108.35|105.78|101.63|107.69|123.78|107.52|106.15|111.77|108.18|110.47|
|**2007:Q3**|97.51|108.46|109.19|108.35|101.45|108.41|130.48|108.43|108.15|113.90|109.26|111.79|
|**2007:Q4**|96.22|109.29|109.89|108.13|101.26|109.48|122.66|109.55|108.23|113.65|110.14|113.15|
|**2008:Q1**|92.61|110.13|110.59|108.89|101.10|110.20|113.17|110.40|108.78|114.40|111.01|114.56|
|**2008:Q2**|95.39|110.97|111.29|109.90|100.94|111.21|**132.24***|111.59|109.70|116.77|111.91|115.99|
|**2008:Q3**|93.39|111.81|111.99|109.66|100.81|112.48|127.87|112.86|109.96|118.47|112.86|117.47|
|**2008:Q4**|88.29|112.67|112.67|111.15|100.72|113.56|123.91|114.06|111.10|120.34|113.75|118.94|
|**2009:Q1**|83.72|**113.52***|**113.35***|**111.61***|100.67|**115.13***|130.73|**115.71***|**111.69***|**121.65***|**114.74***|**120.43***|
|**Correlation**||-0.88|-0.84|-0.88|0.81|-0.90|-0.49|-0.91|-0.89|-0.89|-0.89|-0.90|



Note: The starred and bolded numbers equal the maximum values in each column. The correlation measures the correlation between the column’s forecasted values and the actual values. 

32 

**Table 3: Recursive Forecasts for the Real US House Price Index** 

||**Actual**|**DSGE**|**Optimal**<br>**SBVAR**<br>**(w=0.3,d=0.5)**|
|---|---|---|---|
|**2005:Q2**|99.59|99.59|99.59|
|**2005:Q3**|100.74|100.97|103.50|
|**2005:Q4**|102.22|100.16|101.54|
|**2006:Q1**|101.58|100.92|**104.29***|
|**2006:Q2**|**102.41***|101.38|101.80|
|**2006:Q3**|101.07|101.87|103.59|
|**2006:Q4**|99.75|101.58|100.51|
|**2007:Q1**|102.08|**103.33***|99.49|
|**2007:Q2**|100.54|102.15|99.59|
|**2007:Q3**|97.51|100.39|101.58|
|**2007:Q4**|96.22|97.30|100.07|
|**2008:Q1**|92.61|96.00|100.01|
|**2008:Q2**|95.39|92.41|93.36|
|**2008:Q3**|93.39|95.20|94.55|
|**2008:Q4**|88.29|93.27|91.17|
|**2009:Q1**|83.72|88.26|88.11|
|**Correlation**<br>Note:<br>The starr|ed and bolded nu|0.93<br>mbers equal the m|0.87<br>aximum values in|



<mark>Note: The starred and bolded numbers equal the maximum values in each column. The correlation measures the correlation between the column’s forecasted values and the actual values.</mark> 

33 

## **Figure 1: The US Real House Price Index** 



34 

## **Figure 2: Out-of-Sample Ex Ante Forecasts: US Real House price Index** 



35 

## **Figure 3: Out-of-Sample Recursive Forecasts: US Real House Price Index** 



36 

