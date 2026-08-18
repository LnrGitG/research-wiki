---
title: Das_The Blessing Of Dimensionality in Forecasting Real House Price Growth in the 9 Census Divisions of the US_2009
type: paper
source_pdf: raw/papers/Das_The Blessing Of Dimensionality in Forecasting Real House Price Growth in the 9 Census Divisions of the US_2009.pdf
converted: 2026-08-18
---



## **University of Pretoria** 

**_Department of Economics Working Paper Series_** 

# **The Blessing of Dimensionality in Forecasting Real House Price Growth in the Nine Census Divisions of the US** 

Sonali Das CSIR Rangan Gupta University of Pretoria Alain Kabundi University of Johannesburg Working Paper: 2009-02 January 2009 

__________________________________________________________ Department of Economics University of Pretoria 0002, Pretoria South Africa Tel: +27 12 420 2413 Fax: +27 12 362 5207 

## THE BLESSING OF DIMENSIONALITY IN FORECASTING REAL HOUSE PRICE GROWTH IN THE NINE CENSUS DIVISIONS OF THE US Sonali Das<sup>*</sup> , Rangan Gupta<sup>**</sup> and Alain Kabundi<sup>#</sup> 

## Abstract 

This paper analyzes whether a wealth of information contained in 126 monthly series used by large-scale Bayesian Vector Autoregressive (LBVAR) models, as well as Factor Augmented Vector Autoregressive (FAVAR) models, either Bayesian or classical, can prove to be more useful in forecasting real house price growth rate of the nine census divisions of the US, compared to the small-scale VAR models, that merely use the house prices. Using the period of 1991:02 to 2000:12 as the in-sample period and 2001:01 to 2005:06 as the out-of-sample horizon, we compare the forecast performance of the alternative models for one- to twelve–months ahead forecasts. Based on the average Root Mean Squared Error (RMSEs) for one- to twelve–months ahead forecasts, we find that the alternative FAVAR models outperform the other models in eight of the nine census divisions. 

_Journal of Economic Literature Classification:_ C11, C13, C33, C53. Keywords: Dynamic Factor Model, BVAR, Forecast Accuracy. 

## 1. Introduction 

This paper develops Factor Augmented Vector Autoregressive (FAVAR) models, based on both classical and Bayesian assumptions, and large-scale Bayesian Vector Autoregressive (LBVAR) models, using 126 monthly series, for forecasting annualized real house price growth rates for the nine census divisions of the United States (US).<sup>2</sup> Using an in-sample period of 1991:02 to 2000:12, the FAVARs and the LBVARs, are used to forecast one- to twelve-months-ahead real house price growth rates over the out-of-sample horizon of 2001:01 to 2005:06. The forecast performance of the FAVARs and the LBVARs are then compared in terms of average Root Mean Square Errors (RMSEs) with the classical and Bayesian versions of small-scale VAR models that consider only the real growth rates of homes in the nine census divisions. 

With the methodologies in place, three questions arise immediately. First, why is forecasting real house price growth rates important? Second, why use large-scale models for this purpose? And, third, why use regional data for this purpose? As far as the answer to the first question is concerned, the importance of predicting house price inflation is motivated by recent studies that conclude that asset prices help forecast both inflation and output (Forni _et al._ , 2003; Stock and Watson, 2003, Gupta and Das, 2008a,b and Das _et al._ , 2008a,b). Since a large amount of individual wealth is imbedded in houses, similar to other asset prices, house price movements are thus 

> *Senior Researcher, Logistics and Quantitative Methods, CSIR Built Environment, P.O. Box: 395, Pretoria, 0001, South Africa. Email: <u>SDas@csir.co.za, Phone: +27 12 841 3713, Fax: +27 12 841 3037.</u> 

> ** To whom correspondence should be addressed. Associate Professor, Department of Economics, University of Pretoria, Pretoria, 0002, South Africa, Email: Rangan.Gupta@up.ac.za. Phone: +27 12 420 3460, Fax: +27 12 362 5207. 

> # Senior Lecturer, University of Johannesburg, Department of Economics, Johannesburg, 2006, South Africa, Email: <u>akabundi@uj.ac.za. Phone: +27 11 559 2061, Fax: +27 11 559 3039.</u> 

> 2 The US Census bureau organises the fifty states into five census regions, and further into nine divisions, which,  in alphabetical order, are: East north Central, East South Central, Middle Atlantic, Mountain, New England, Pacific, South Atlantic, West North Central and West South Central. 

1 

important in signaling inflation. As such, models that forecast real house price inflation can give policy makers an idea about the direction of overall inflation in the future, and hence, can provide a better control for designing of appropriate policies. In addition, given that movements in the housing market are likely to play an important role in the business cycle (Iacoviello and Neri, 2008), not only because housing investment is a very volatile component of demand (Bernanke and Gertler, 1995), but also because changes in house prices tends to have important wealth effects on consumption (International Monetary Fund, 2000) and investment (Topel and Rosen, 1988), and hence, the importance of forecasting house price inflation is vital. The housing sector thus plays a significant role in acting as a leading indicator of the real sector of the economy, and as such, predicting it correctly cannot be overemphasized, especially in the light of the recent credit crunch in the U.S. that started with the burst of the housing price bubble which, in turn, transmitted to the real sector of the economy driving it towards an imminent recession. 

The rationale for using large-scale models to forecast real house price growth rates emanates from the fact that a large number of economic variables help in predicting real housing price growth (Cho, 1996; Abraham and Hendershott, 1996; Johnes and Hyclak, 1999; and Rapach and Strauss, 2007, 2008). For instance, income, interest rates, construction costs, labor market variables, stock prices, industrial production, consumer confidence index – which are amongst the 126 monthly series used by the large-scale models, which act as potential predictors.  As to why we decide to use census division data, the answer comes from past studies, namely Carlino and DeFina (1998, 1999), Burger and van Rensburg (2008), Gupta and Das (2008a) and VargasSilva (2008a,b), among others. These papers have not only documented the segmented nature of housing markets, but have also suggested of non-uniform economic conditions that might be prevailing across the regions at a specific point of time. 

To realize the contribution of this study, it is important to place this paper in the context of current research that has been done on forecasting in the housing market. In this regard, few studies that are worth mentioning: Rapach and Strauss (2007) used an autoregressive distributed lag (ARDL) model framework, containing 25 determinants, to forecast real housing price growth for the individual states of the Federal Reserve’s Eighth District. Given the difficulty in determining _apriori_ the particular variables that are most important for forecasting real housing price growth, the authors also use various methods to combine the individual ARDL model forecasts, which result in better forecast of real housing price growth. Rapach and Strauss (2008) look at doing the same for 20 largest US states based on ARDL models containing large number of potential predictors, including state, regional and national level variables. Once again, the authors reach similar conclusions as far as the importance of combining forecasts are concerned. On the other hand, Gupta and Das (2008b), look into forecasting the recent downturn in real house price growth rates for the twenty largest states of the US economy. In this paper, the authors use Spatial BVARs, based merely on real house price growth rates, to predict their downturn over the period of 2007:01 to 2008:01. They find that, though the models are quite well-equipped in predicting the recent downturn, they underestimate the decline in the real house price growth rates by quite a margin. They attribute this underprediction of the models to the lack of any information on fundamentals in the estimation process. 

2 

Given that in practice, forecasters and policymakers often extract information from many series than the ones included in smaller models, like the ones used by Rapach and Strauss (2007, 2008), who also indicate the importance of combining forecast from alternative models, the role of a large-scale models cannot be ignored. In addition, one cannot condone the fact that the main problem of small models, as seen from the studies by Rapach and Strauss (2007, 2008), is in the decision regarding the choice of the correct potential predictors to be included.  Due to this reason, VargasSilva (2008a) uses a FAVAR model containing 120 monthly series to analyze the impact of monetary policy actions on the housing sector of four different regions of the United States. To the best of our knowledge, this is the first attempt to look into the ability of FAVARs and LBVARs in forecasting regional real house price growth rates.<sup>3</sup> 

In such a backdrop, our paper can thus be viewed as an extension of the abovementioned studies, in the sense that we use large-scale models that allow for the role of a wide possible set of fundamentals to affect the housing sector. The remainder of the paper is organized as follows: Section 2 lays out the basics of the alternative small- and large-scale models. In Section 3 we discuss the data. In Section 4 we evaluate the forecasting performances of the various models, and finally Section 5 concludes. 

## 2. The Models<sup>4</sup> 

## _2.1 VARs and BVARs_ 

The Vector Autoregressive (VAR) model, though ‘atheoretical’, is particularly useful for forecasting purposes. An unrestricted VAR model, as suggested by Sims (1980), can be written as follows: 

_yt_ = _A_ 0 + _A_ ( _L_ ) _yt_ + ε _t_ (1) where _y_ is a ( _n_ × 1 ) vector of variables being forecasted; _A(L)_ is a ( _n_ × _n_ ) polynomial matrix in the backshift operator _L_ with lag length _p_ , _i.e., A(L)_ = _A L_ 1 + _A_ 2 _L_ 2 + ................ + _A pL p_ ; _A_ 0 is a ( _n_ × 1 ) vector of constant terms, and ε is a ( _n_ × 1 ) vector of error terms. In our case, we assume that ε ~ _N_ (0, σ 2 _I n_ ), where _I n_ isa _n_ × _n_ identity matrix . 

Note the VAR model, generally uses equal lag length for all the variables of the model. One drawback of VAR models is that many parameters need to be estimated, some of which may be insignificant. This problem of overparameterization, resulting in multicollinearity and a loss of degrees of freedom, leads to inefficient estimates and possibly large out-of-sample forecasting errors. One solution, often adapted, is simply to exclude the insignificant lags based on statistical tests. Another approach is to use a near VAR, which specifies an unequal number of lags for the different equations. 

However, an alternative approach to overcoming this overparameterization, as 

> 3 Note, Dua and Smyth (1995), Dua and Miller (1996) and Dua _et al._ (1999) used coincident and leading indexes in BVAR models to forecast home sales for the Connecticut and the overall US economy, respectively. 

> 4 This section relies heavily on the discussion available in Gupta and Sichei (2006), Gupta (2006) and Gupta and Kabundi (2008a). 

3 

described in Litterman (1981), Doan _et al._ (1984), Todd (1984), Litterman (1986), and Spencer (1993), is to use a BVAR model. Instead of eliminating longer lags, the Bayesian method imposes restrictions on these coefficients by assuming that they are more likely to be near zero than the coefficients on shorter lags. However, if there are strong effects from less important variables, the data can override this assumption. The restrictions are imposed by specifying normal prior distributions with zero means and small standard deviations for all coefficients with the standard deviation decreasing as the lags increase. The exception to this is that the coefficient on the first own lag of a variable has a mean of unity. Litterman (1981) used a diffuse prior for the constant. This is popularly referred to as the ‘Minnesota prior’ due to its development at the University of Minnesota and the Federal Reserve Bank at Minneapolis. 

Formally, as discussed above, the means and variances of the Minnesota prior take the following form: 



where β _i_ denotes the coefficients associated with the lagged dependent variables in each equation of the VAR, while β _j_ represents any other coefficient. In the belief that lagged dependent variables are important explanatory variables, the prior means corresponding to them are set to unity. However, for all the other coefficients, β _j_ ’s, in a particular equation of the VAR, a prior mean of zero is assigned to suggest that these variables are less important to the model. 

2 2 The prior variances σβ _i_<sup>and</sup> σβ _j_<sup>, specify uncertainty about the prior means</sup> β _i_ = 1, and β _j_ = 0, respectively. Because of the overparameterization of the VAR, Doan _et al._ (1984) suggested a formula to generate standard deviations as a function of small numbers of hyperparameters: _w, d_ , and a weighting matrix _f(i, j)_ . This approach allows the forecaster to specify individual prior variances for a large number of coefficients based on only a few hyperparameters. The specification of the standard deviation of the distribution of the prior imposed on variable _j_ in equation _i_ at lag _m_ , for all _i, j_ and _m_ , defined as σ _ijm_ , can be specified as follows: 



with _f(i, j)_ = _1_ , if _i = j_ and<sup>_k_</sup> _ij_<sup>otherwise, with (</sup> 0 ≤<sup>_k_</sup> _ij_ ≤ 1), _g(m)_ = _m_ − _d_ , _d_ > 0 . Note that σ ˆ _i_ is the estimated standard error of the univariate autoregression for variable _i_ . The ratio σ ˆ _i_ / σ ˆ _j_ scales the variables to account for differences in the units of measurement and, hence, causes specification of the prior without consideration of the magnitudes of the variables. The term _w_ indicates the overall tightness and is also the standard deviation on the first own lag, with the prior getting tighter as we reduce the value. The parameter _g(m)_ measures the tightness on lag _m_ with respect to lag 1, and is assumed to have a harmonic shape with a decay factor of _d_ , which tightens the prior on increasing lags. The parameter _f(i, j)_ represents the tightness of variable _j_ in equation _i_ relative to variable _i_ , and by increasing the interaction, i.e., the value of<sup>_k_</sup> _ij_<sup>,</sup> 

4 

we can loosen the prior.<sup>5</sup> Note, in the standard Minnesota-type prior, the overall tightness ( _w_ ) takes the values of 0.1, 0.2 and 0.3, while, the lag decay ( _d_ ) is generally chosen to be equal to 0.5, 1.0 and 2.0. The interaction parameter (<sup>_k_</sup> _ij_<sup>) is traditionally</sup> 

set at = 0.5. The small-scale BVARs would be estimated with this set of parameterization of the priors. 

Given that, we have regional (real house price growth rates of the nine census divisions) as well as national variables in the 126 data series used for the large-scale models, and realizing that regional variables would have minimal, if any, effect on the national, while the latter set of variables is sure to have an influence on the former, setting<sup>_k_</sup> _ij_<sup>= 0.5 could be a quite far fetched from reality. Hence, borrowing from the</sup> 

BVAR models used for regional forecasting, involving both regional and national variables, and following Kinal and Ratner (1986), Shoesmith (1992), Dua and Ray (1995), Das _et al._ (2008b), and Gupta and Kabundi (2008b,c), the weight of a national variable in a national equation, as well as a domestic equation, is set at 0.6. The weight of a regional variable in other regional equation is fixed at 0.1 and that in a national equation at 0.01. Finally, the weight of the regional variable in its own equation is 1.0. These weights are in line with Litterman’s circle-star structure. Star (national) variables affect both star and circle (regional) variables, while circle variables primarily influence only other circle variables.<sup>6</sup> The large-scale BVARs are, thus, estimated with asymmetric priors. 

Finally, once the priors have been specified, the alternative BVARs, whether based on nine or all of the 126 variables, are estimated using Theil's (1971) mixed estimation technique. Specifically, suppose we denote a single equation of the VAR model as: 2 _y_ 1 = _XA_ + ε 1, with _Var_ ( ε 1 ) = σ _I_ , then the stochastic prior restrictions for this single equation can be written as: 



2 Note, _Var_ ( _u_ ) = σ _I_ and the prior means _M ijm_ and σ _ijm_ take the forms shown in (2) and (3). With (4) written as: 

_r_ = _RA_ + _u_ 



and the estimates for a typical equation are derived as follows: 

_A_ ˆ = ( _X_ ' _X_ + _R_ ' _R_ ) − 1( _X_ ' _y_ 1 + _R_ ' _r_ ) (6) 

Essentially then, the method involves supplementing the data with prior information on the distribution of the coefficients. The number of observations and degrees of 

> 5 For an illustration, see Dua and Ray (1995). 

> 6 We also experimented by assigning higher and lower interaction values, in comparison to those specified above, to the star variables in both the star and circle equations, but, the rank ordering of the alternative forecasts remained the same. 

5 

freedom are increased by one in an artificial way, for each restriction imposed on the parameter estimates. The loss of degrees of freedom due to over- parameterization associated with a classical VAR model is, therefore, not a concern in the BVARs. 

## _2.2  FAVARs_ 

This study uses the Dynamic Factor Model (DFM) to extract common components between macroeconomic series, and then these common components are used to forecast real house price growth rates of the nine census divisions of the US, by adding the extracted factors to the nine variables of our concern and constructing a FAVAR in the process. Furthermore, we estimate idiosyncratic component with AR( _p_ ) processes as suggested by Boivin and Ng (2005). 

The DFM expresses individual times series as the sum of two unobserved components: a common component driven by a small number of common factors and an idiosyncratic component, which are specific to each variable. The relevance of the method is that the DFM is able to extract the few factors that explain the comovement of all US. Forni et al. (2005) demonstrated that when the number of factors is small relative to the number of variables and the panel is heterogeneous, the factors can be recovered from the present and past observations. 

Consider a _n_ × 1 covariance stationary process _Yt_ = ( _y_ 1 _t_ ,...., _ynt_ )' . Suppose that _X t_ is the standardized version of<sup>_Y_</sup> _t_<sup>, i.e.</sup> _X t_ has a mean zero and a variance equal to one. Under DFM _X t_ is described by a factor model, it can be written as the sum of two orthogonal components: _xit_ = λ _i Ft_ +ξ _it_ (7) where<sup>_F_</sup> _t_<sup>is a</sup> _r_ × 1 vector of static factors,<sup>λ</sup> _i_<sup>is an</sup> _n_ × _q_ matrix of factor loadings, and ξ _it_ is a _n_ × 1 vector of idiosyncratic components. In a DFM,<sup>_F_</sup> _t_<sup>and</sup> ξ _it_ are mutually orthogonal stationary process, while, χ _it_ = λ _i Ft_ is the common component. 

Since dynamic common factors are latent, they need to be estimated. It is important to point out that the estimation technique used matters for factor forecasts. This paper uses SW method, which employs the static principal component approach (PCA) on _X t_ . The factor estimates are therefore the first   principal components of _X t_ , i.e. ˆ _Ft_ = Λ′<sup>ˆ</sup> _X t_ , where Λ<sup>ˆ</sup> is the _n_ × _r_ matrix of the eigenvectors corresponding to the _r_ largest eigenvalues of the sample covariance matrix Σ<sup>ˆ</sup> 

> Following Boivin and Ng (2005) we represent the idiosyncratic errors as AR( _p_ ) processes. Therefore, the forecasting equation to predict<sup>_y_</sup> _t_<sup>is given by:</sup> 



> where _h_ is the forecasting horizon, α _i_ ( _L_ ) are lag polynomials, which can be estimated based on restrictions suggested by the Minnesota prior or without restrictions. We consider the following DFM specifications: 

6 

- UFAVAR: includes one of the variables of interest and the obtained number of common static factors; 

- MFAVAR: includes all the nine real house price growth rates and the common static factors; 

- UBFAVAR: uses one of the variables of interest and the common static factors, and which, in turn, are estimated based on Bayesian restrictions discussed in the previous subsection; 

- MBFAVAR: with a specification similar to the MFAVAR, except that the current model applies Bayesian restrictions on lag of the variables based on the Minnesota prior. 

## 3. Data 

While the small-scale VARs, both the classical and Bayesian variants, include data of only the nine variables of interest, namely, the annualized real house price growth rates of the nine census divisions of the US, the large-scale BVARs and the DFM are estimated based on  126 monthly series. The nominal house price figures for these nine US census divisions and for the whole of US were obtained from the Office of Federal Housing Enterprise Oversight (OFEO), and were converted to their real counterpart by dividing them with the personal consumption expenditure deflator. Figure 1 presents the nine census divisions of the US to provide a general idea about their layout. Data between 1991:02 and 2000:12 was used for the in-sample analyses, while the data between 2001:1 and 2005:6 was used for the out-of-sample forecast evaluation of the real house price growth of nine regions in the US. The out-of-sample forecast is done for one to twelve months ahead. The choice of 2001:01 as the onset of forecast horizon is motivated from Iacoviello and Neri (2008) in which they indicate that the experience of the U.S. housing market at the beginning of the 21st century has been characterized by fast growth in housing prices and residential investment initially, and a decline thereafter. Given this observed volatility in the housing market, the choice of the out-of-sample horizon emerged quite naturally. 

For the remaining 116 variables we use the macroeconomic indicators in the data set of Boivin _et al._ (2008). With this data set ending at 2005:06, the endpoint of our sample is automatically determined to be the same. The data set contains a broad range of macroeconomic variables, such as industrial production, income, employment and unemployment, housing starts, inventories and orders, stock prices, exchange rates, interest rates, money aggregates, consumer prices, producer prices, earnings, and consumption expenditure. So, in total we have a balanced panel of 126 monthly series for the period running from 1991:02 to 2005:06. All series are in logarithms, except those that have already been expressed in rates and those that contain negative observations. All data have been transformed to induce stationarity.<sup>7</sup> Following Bernanke _et al._ (2005), five static factors are extracted from the DFM estimated with 13 lags. As with these authors, we find that increasing the number of factors further does not change the results. 

> 7 It must however be pointed out that, non-stationarity is not an issue with the BVAR, since Sims _et al._ (1990) indicate that with the Bayesian approach entirely based on the likelihood function, the associated inference does not need to take special account of nonstationarity, since the likelihood function has the same Gaussian shape regardless of the presence of nonstationarity. 

7 



Figure 1: Layout of the Nine Census Divisions of the US. (Source: US Department of Commerce, Economics and Statistics Administration, US Census Bureau.)<sup>8</sup> 

## 4. Results 

Given the specifications of the models, we estimate the multivariate versions of the classical VAR, the small-scale BVARs, the large-scale BVARs and the FAVARs, univariate and multivariate, classical and Bayesian, over the period of 1991:02 to 2000:12, based on monthly data. Then we compute the out-of-sample one- through twelve-months-ahead forecasts for the period of 2001:01 to 2005:06, and compare the forecast accuracy of the alternative models. The different types of the VARs are estimated with 3 lags<sup>9</sup> of each variable. Since we use three lags, the initial three months of the sample, 1991:02 to 1991:04, are used to feed the lags. We generate dynamic forecasts, as would naturally be achieved in actual forecasting practice. The models are re-estimated each month over the out-of-sample forecast horizon in order to update the estimate of the coefficients, before producing the 12-months-ahead forecasts. This iterative estimation and 12-steps-ahead forecast procedure was carried out for 54 months, with the first forecast beginning in 2001:01. This experiment produced a total of 54 one-month-ahead forecasts, 54-two-months-ahead forecasts, 

> 8 See: http://commons.wikimedia.org/wiki/File:Census_Regions_and_Divisions.PNG. 

> 9 The choice of 3 lags is based on the unanimity of the sequential modified LR test statistic, Akaike information criterion (AIC), the final prediction error (FPE) criterion and the Schwarz information criterion (SIC) applied to a stable VARs. Note, stability, as usual, implies that no roots were found to lie outside the unit circle. 

8 

and so on, up to 54 12-step-ahead forecasts. The RMSEs<sup>10</sup> for the 54, month 1 through month 4 forecasts are then calculated for the annualized real house price growth rates of the nine census divisions. The values of the RMSE statistic for one- to four-quarters-ahead forecasts for the period 2001:01 to 2005:06 are then examined. The model that produces the lowest average value for the RMSE is selected as the ‘optimal’ model for a specific category of real house price growth rate. 

In Tables 1 through 9, we compare the RMSEs of one- to twelve-months-ahead outof-sample-forecasts for the period of 2000:01 to 2005:06, generated by the abovementioned alternative models models. At this stage, a few words need to be said regarding the choice of the evaluation criterion for the out-of-sample forecasts generated from Bayesian models. As Zellner (1986: 494) points out the ‘optimal’ Bayesian forecasts will differ depending upon the loss function employed and the form of predictive probability density function. In other words, Bayesian forecasts are sensitive to the choice of the measure used to evaluate the out-of-sample forecast errors. However, Zellner (1986) also points out that the use of the mean of the predictive probability density function for a series, is optimal relative to a squared error loss function and the Mean Squared Error (MSE), and hence, the RMSE is an appropriate measure to evaluate performance of forecasts, when the mean of the predictive probability density function is used. This is exactly what we do below in Tables 1 through 9, when we use the average RMSEs over the one- to twelve-monthsahead forecasting horizon. The conclusions, regarding each of the nine divisions of real house price growth rate, based on the average one- to twelve-months-ahead RMSEs, from these tables can be summarized as follows: 

- (i) Based on the minimum average RMSEs, there always exists a largescale model, which outperforms all other small-scale models. Specifically, the best performing large-scale models are: UVFAVAR for East South Central and West South Central, UVBFAVAR with _w_ =0.1, _d_ = 2 for East North Central and Mountain, LBVAR with _w_ =0.1, _d_ =1 for Middle Atlantic, MVBFAVAR with _w_ =0.2, _d_ =2 for New England, MVBFAVAR with _w_ =0.1, _d_ =2 for South Atlantic and West North Central, and MVFAVAR for Pacific; 

- (ii) In general, with the exceptions of Middle Atlantic under _w_ =0.3, _d_ =0.5, _w_ = 0.2, _d_ =1, _w_ =0.1, _d_ =1 and _w_ =0.1, _d_ =2, there always exists at least one small-scale model that outperforms the large-scale BVAR. The large-scale BVAR with _w_ =0.3, _d_ =0.5 and _w_ =0.1, _d_ =2 are found to better the corresponding UVBFAVARs for New England and for Middle Atlantic the same holds true for all the alternative values of _w_ and _d_ ; 

- (iii) In most cases, barring West South Central, even the second-best performing models are large-scale in nature. For this census division, the SBVAR with _w_ =0.1, _d_ =1 comes in second; 

- (iv) Overall, the FAVARs, Bayesian or classical, univariate or multivariate, are the standout performers. Even in the case of Middle Atlantic where 

> 10 Note that if _At_ + _n_ denotes the actual value of a specific variable in period _t + n_ and _t Ft_ + _n_ is the forecast made in period _t_ for _t + n_ , the RMSE statistic can be defined as: _N_ 1 ∑ ( _At_ + _n_ − _t Ft_ + _n_ )2 . For _n = 1_ , the 

> summation runs from 2001:01 to 2005:06, and for _n = 2_ , the same covers the period of 2001:02 to 2005:06, and so on. 

9 

the LBVAR is the best performing model, we are able to find a FAVAR model, namely, MVBFAVAR with _w_ =0.1, _d_ =2, as the second-best model in a different category of models. 

In summary, even though there is no unique model under a specific category of models that performs the best, the FAVARs in their various forms are the standout performers, where the FAVARs are VAR models of the real house price growth rates of the nine census divisions augmented by the 5 static factors, the latter capturing the majority of the variation in the 126 monthly series. Given the relatively poor performance of the large-scale BVAR, it would be interesting to study these five factors in greater details, and in the process, open up the black-box and unveil those macroeconomic variables that play a dominant part in comprising these factors. This would be an interesting extension of the current study, since this would allow us to concentrate on a smaller number of macroeconomic indicators that affects the housing market, rather than on a set of 116 variables. This would be extremely helpful to policy-makers trying to design policies to appropriately affect the housing market. 

## 5. Conclusion 

In this paper we analyze whether a wealth of information generally used by largescale BVARs, as well as FAVAR models, either Bayesian or classical, can prove to be more useful in forecasting real house price growth, compared to small-scale VAR models, that merely uses the house prices. As a case study, we considered house price growth of the nine census divisions of the US, using data on 126 monthly series for the period 1991:02 to 2005:06. The period 1991:02 to 2000:12 is considered as the insample data, while the period 2001:01 to 2005:06 is used for the evaluation of the forecasts from the various models considered, based on the average RMSE values. We perform one- to twelve – months ahead forecast in the forecast horizon of 2001:01 to 2005:06. 

Our results indicate that the various types of FAVAR models prove to be better suited for forecasting house price growth at the divisional scale, when compared to the alternative forms of the VAR models. This investigation overwhelmingly proves that the data rich environment of the FAVAR models that include a wide range of macroeconomic series of the US economy, besides the house price growth rates of the census divisions, is more informative when forecasting the house price growth rate of the nine census regions. Realizing that the FAVARs are VAR models of the real house price growth rates of the nine census divisions augmented by factors capturing the majority of the variation in the large dataset, the role of fundamentals in affecting the housing market cannot be underestimated. The current paper can be extended in at least two directions: First, as indicated earlier, one might want to take a detailed look at the factors to determine the dominant macroeconomic variables that comprise these factors; and second, one might want to incorporate the role of the house price growth rate of the neighbouring division(s) in the forecasting process of a particular census division, by developing spatial versions of the above models. 

10 

References 

Abraham, J.M., & Hendershott, P.H. (1996). Bubbles in Metropolitan Housing Markets. Journal of Housing Research, 7(2), 191–207. 

Bernanke, B., & Gertler, M. (1995). Inside the Black Box: the Credit Channel of Monetary Transmission. Journal of Economic Perspectives, 9(4), 27–48. Boivin, J., & Ng, S. (2005). Undertanding and comparing factor based forecasts. International Journal of Central Banking, 1(3), 117-152. 

Boivin, J., Giannoni, M., & Mihov, I. (2008). Sticky Prices and Monetary Policy: Evidence from Disaggregated U.S. Data. _Forthcoming American Economic Review_ . Burger, P., & Van Rensburg, L.J. (2008). Metropolitan house prices in South Africa: Do they converge? South African Journal of Economics, 76(2), 291-297. Carlino, G.A., & DeFina, R.H. (1998). The Differential Regional Effects of Monetary Policy. The Review of Economics and Statistics _,_ 80(4), 572–587. 

Carlino, G.A., & DeFina, R.H. (1999). Do States Respond Differently to Changes in Monetary Policy? Business Review, (July/August), 17–27. 

Cho, M. (1996). House Price Dynamics: A Survey of Theoretical and Empirical Issues _._ Journal of Housing Research, 7(2),145–172. 

Das, S., Gupta, R., & Kabundi, A. (2008a). Is a DFM Well-Suited for Forecasting Regional House Price Inflation?” Working Paper No. 85, Economic Research Southern Africa. 

Das, S., Gupta, R., & Kabundi, A. (2008b). Could We Have Forecasted the Recent Downturn in the South African Housing Market? Working Paper No. 200831, Department of Economics, University of Pretoria. 

Doan, T.A., Litterman, R.B., & Sims, C.A. (1984). Forecasting and Conditional Projections Using Realistic Prior Distributions. Econometric Reviews, 3(3),1-100. Dua, P., & Smyth, D. J. (1995). Forecasting U. S. Home Sales using BVAR Models and Survey Data on Households’ Buying Attitude for Homes. Journal of Forecasting, 14(3), 217-227. 

Dua, P., Miller, S. M., & Smyth, D. J. (1999). Using Leading Indicators to Forecast U. S. Home Sales in a Bayesian Vector Autoregressive Framework. Journal of Real Estate Finance and Economics, 18(2), 191-205. 

Dua, P., & Miller, S. M. (1996). Forecasting Connecticut Home Sales in a BVAR Framework Using Coincident and Leading Indexes. Journal of Real Estate Finance and Economics, 13(3), 219-235. 

Dua, P., & Subhash, C. R. (1995). A BVAR Model for the Connecticut Economy. Journal of Forecasting, 14(3),167-180. 

Forni, M., Hallin, M., Lippi, M., & Reichlin, L. (2005). The Generalized Dynamic Factor Model, One Sided Estimation and Forecasting. Journal of the American Statistical Association, 100(471), 830–840. 

Forni M., Hallin, M., Lippi, M., Reichlin, L. (2003). Do financial variables help forecasting inflation and real activity in the euro area _?_ Journal of Monetary Economics, 50(6), 1243-1255. 

Gupta, R., & Das, S. (2008a). Spatial Bayesian Methods for Forecasting House Prices in Six Metropolitan Areas of South Africa. South African Journal of Economics _,_ 76(2), 298-313 _._ 

Gupta, R., & Das, S. (2008b). Predicting Downturns in the US Housing Market. Forthcoming Journal of Real Estate Economics and Finance _._ 

Gupta, R., & Kabundi, A. (2008a). A Dynamic Factor Model for Forecasting Macroeconomic Variables in South Africa. Working Paper No. 200815, Department 

11 

of Economics, University of Pretoria. 

Gupta, R., & Kabundi, A. (2008b). Forecasting Macroeconomic Variables using Large Datasets: Dynamic Factor Model vs Large-Scale BVARs. Working Paper No. 200816, Department of Economics, University of Pretoria. 

Gupta, R., & Kabundi, A. (2008c). Forecasting Macroeconomic Variables in a Small Open Economy: A Comparison between Small- and Large-Scale Models. Working Paper No. 200830, Department of Economics, University of Pretoria. 

Gupta, R. (2006). Forecasting the South African Economy with VARs and VECMs. South African Journal of Economics, 74(4), 611-628 _._ 

Gupta, R., & Sichei, M. (2006).A BVAR Model for the South African Economy. South African Journal of Economics, 74(3), 391-409 _._ 

Iacoviello, M., & Neri, S. (2008). Housing Market Spillovers: Evidence from an Estimated DSGE Model. Working Paper No. 659, Boston College Department of Economics. 

International Monetary Fund. World Economic Outlook: Asset Prices and the Business Cycle, 2000. Johnes, G., &  Hyclak, T. (1999). House Prices and Regional Labor Markets. Annals of Regional Science, 33(1), 33–49. 

Kinal, T., & Ratner, J. (1986). A VAR Forecasting Model of a Regional Economy: Its Construction and Comparison. International Regional Science Review, 10(2), 113126. 

Litterman, R.B. (1981). A Bayesian Procedure for Forecasting with Vector Autoregressions. Working Paper, Federal Reserve Bank of Minneapolis. 

Litterman, R. B. (1986). Forecasting with Bayesian Vector Autoregressions – Five Years of Experience . Journal of Business and Economic Statistics, 4 (1), 25-38. Rapach, D.E., & Strauss. J. K. (2008). Differences in Housing Price Forecast ability Across U.S. States. Forthcoming International Journal of Forecasting. 

Rapach, D.E., & Strauss, J.K. (2007). Forecasting Real Housing Price Growth in the Eighth District States. Federal Reserve Bank of St. Louis _._ Regional Economic Development, 3(2), 33–42. 

Shoesmith, G. L. (1992). Co-integration, Error Correction and Medium-Term Regional VAR Forecasting. Journal of Forecasting, 11(1), 91-109. 

Sims, C. A., Stock, J. H., & Watson, M. W. (1990). Inference in Linear Time Series Models with Some Unit Roots. Econometrica, 58(1), 113-144. Sims, C.A. (1980). Macroeconomics and Reality. Econometrica, 48(1),1-48. Spencer, D.E. (1993). Developing a Bayesian Vector Autoregression Model. International Journal of Forecasting, 9(3), 407-421. 

Stock, J.H., & Watson, M.W.  (2003), Forecasting Output and Inflation: The Role of Asset Prices. Journal of Economic Literature, 41(3), 788-829. Theil, H. (1971). Principles of Econometrics. New York, John Wiley. 

Todd, R.M. (1984). Improving Economic Forecasting with Bayesian Vector Autoregression. Quarterly Review, Federal Reserve Bank of Minneapolis, Fall, 18-29. Topel, R. H., & Rosen, S. (1988). Housing Investment in the United States. Journal of Political Economy, 96(4), 718–740. 

Vargas-Silva, C. (2008a).The Effect of Monetary Policy on Housing: A Factor Augmented Approach. Applied Economics Letters, 15(10), 749-752. 

Vargas-Silva, C. (2008b). Monetary Policy and the US Housing Market: A VAR Analysis Imposing Sign Restrictions. Journal of Macroeconomics, 30(3), 977-990. Zellner, A. (1986). A Tale of Forecasting 1001 Series: The Bayesian Knight Strikes Again. International Journal of Forecasting, 2(4), 494-494. 

12 

||||**Ta**|**ble 1: On**|**e- to Tw**|**elve-Mon**|**ths-Ahea**|**d RMSEs**|**for East**|**North C**|**entral**|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Models**|**1**|**2**|**3**|**4**|**5**|**6**|<br>**7**|**8**|**9**|**10**|**11**|**12**|**Average**|
|**VAR**|0.3848|0.0449|0.3247|0.4676|0.1712|0.0971|0.1571|0.2072|0.1916|0.1233|0.3247|0.0599|0.2128|
|**UVFAVAR**|0.0631|0.0534|0.2456|0.3957|0.1798|0.1276|0.1613|0.2451|0.1842|0.0919|0.3595|0.0723|0.1816|
|**MVFAVAR**|0.3527|0.3480|0.1094|0.2044|0.2240|0.0536|0.3729|0.2014|0.1536|0.0213|0.3671|0.1094|0.2098|
|**SBVAR**|0.3780|0.0477|0.3218|0.4626|0.1695|0.0991|0.1560|0.2066|0.1911|0.1234|0.3255|0.0585|0.2116|
|**LBVAR**<br>**w=03 d=05**|0.7785|0.0465|0.8700|0.0405|0.9427|0.3827|0.0136|1.2500|0.5549|0.1922|1.5933|0.6823|0.6123|
|**UVBFAVAR**<br>**., .**|0.1447|0.0972|0.2008|0.4521|0.1364|0.0801|0.1135|0.2003|0.2306|0.1375|0.3144|0.0268|0.1779|
|**MVBFAVAR**|0.3427|0.3134|0.1372|0.2100|0.2080|0.0648|0.3572|0.1968|0.1494|0.0093|0.3659|0.1068|0.2051|
|**SBVAR**|0.3570|0.0507|0.3036|0.4466|0.1647|0.1054|0.1529|0.2050|0.1910|0.1232|0.3284|0.0537|0.2069|
|**LBVAR**<br>**w=02 d=1**|0.6093|0.0577|0.8558|0.1256|0.9344|0.4610|0.1834|1.1307|0.5718|0.0108|1.5647|0.7133|0.6015|
|**UVBFAVAR**<br>**.,**|0.1472|0.0989|0.1986|0.4541|0.1345|0.0781|0.1116|0.1983|0.2325|0.1395|0.3124|0.0248|0.1775|
|**MVBFAVAR**|0.3039|0.2205|0.1861|0.2219|0.1770|0.0920|0.3159|0.1921|0.1399|0.0232|0.3641|0.1027|0.1949|
|**SBVAR**|0.3074|0.0526|0.2745|0.4223|0.1591|0.1149|0.1446|0.2075|0.1946|0.1241|0.3308|0.0461|0.1982|
|**LBVAR**<br>**w=01 d=1**|0.6175|0.0004|0.8334|0.1998|0.8020|0.5274|0.2763|0.9848|0.5589|0.1756|1.3850|0.6955|0.5880|
|**UVBFAVAR**<br>**.,**|0.1462|0.0998|0.1968|0.4540|0.1335|0.0771|0.1110|0.1975|0.2333|0.1402|0.3116|0.0240|0.1771|
|**MVBFAVAR**|0.2262|0.1131|0.2340|0.2513|0.1636|0.1314|0.2542|0.2200|0.1428|0.0530|0.3709|0.0989|0.1883|
|**SBVAR**|0.3082|0.0331|0.2481|0.4211|0.1636|0.1173|0.1384|0.2129|0.1990|0.1248|0.3324|0.0425|0.1951|
|**LBVAR**<br>**w=02 d=2**|0.2471|0.3680|0.8433|0.0952|1.1480|0.6558|0.2907|1.1432|0.9273|0.4679|1.6355|1.0166|0.7365|
|**UVBFAVAR**<br>**.,**|0.1465|0.0987|0.1959|0.4526|0.1341|0.0773|0.1119|0.1980|0.2328|0.1395|0.3122|0.0246|0.1770|
|**MVBFAVAR**|0.2107|0.0860|0.2238|0.2595|0.1710|0.1376|0.2401|0.2340|0.1439|0.0579|0.3742|0.1003|0.1866|
|**SBVAR**|0.2499|0.0165|0.2277|0.4147|0.1591|0.1122|0.1267|0.2159|0.2132|0.1298|0.3250|0.0348|0.1855|
|**LBVAR**<br>**w=01 d=2**|0.3215|0.1779|0.7948|0.2807|0.8117|0.6113|0.4548|0.9083|0.6233|0.5933|1.2923|0.7526|0.6352|
|**UVBFAVAR**<br>**.,**|0.1435|0.0981|0.1889|0.4491|0.1330|0.0753|0.1124|0.1971|0.2336|0.1399|0.3115|0.0240|0.1755|
|**MVBFAVAR**|0.1441|0.0555|0.2429|0.3100|0.1831|0.1619|0.1985|0.2622|0.1541|0.0682|0.3800|0.0944|0.1879|



Notes: Model acronyms as defined in the text. 

13 

||||**Ta**|**ble 2: On**|**e- to Twe**|**lve-Mon**|**ths-Ahea**|**d RMSEs**|**for East**|**South C**|**entral**|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Models**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**Average**|
|**VAR**|0.0006|0.9774|0.7245|0.0096|0.3004|0.0289|0.4348|0.0485|0.1235|0.4169|0.2960|0.2041|0.2971|
|**UVFAVAR**|0.2091|0.5272|0.4818|0.0687|0.2618|0.1500|0.4385|0.0091|0.0788|0.4098|0.3121|0.2375|0.2654|
|**MVFAVAR**|0.3967|0.7135|0.7012|0.1222|0.5081|0.1056|0.4034|0.1483|0.2089|0.3625|0.2168|0.1398|0.3356|
|**SBVAR**|0.0002|0.9738|0.7241|0.0129|0.2949|0.0304|0.4334|0.0457|0.1215|0.4172|0.2965|0.2057|0.2964|
|**LBVAR**<br>**w=03 d=05**|0.8753|0.3136|0.2394|1.0097|0.4302|1.1718|1.0393|0.0895|0.7142|1.0194|0.7826|0.4349|0.6766|
|**UVBFAVAR**<br>**., .**|0.2717|0.4715|0.4970|0.1119|0.2318|0.1803|0.4692|0.0190|0.0517|0.3826|0.3378|0.2629|0.2740|
|**MVBFAVAR**|0.3486|0.7218|0.6809|0.1221|0.4630|0.0782|0.4055|0.1329|0.2001|0.3665|0.2173|0.1504|0.3240|
|**SBVAR**|0.0107|0.9631|0.7212|0.0259|0.2751|0.0403|0.4289|0.0382|0.1122|0.4172|0.2988|0.2118|0.2953|
|**LBVAR**<br>**w=02 d=1**|1.0086|0.3377|0.5086|0.6377|0.1001|1.1733|1.2560|0.2621|0.9241|0.7932|1.0945|0.6291|0.7271|
|**UVBFAVAR**<br>**.,**|0.2721|0.4708|0.4972|0.1139|0.2313|0.1811|0.4698|0.0198|0.0510|0.3819|0.3385|0.2636|0.2742|
|**MVBFAVAR**|0.2124|0.7687|0.6456|0.1194|0.3611|0.0253|0.4060|0.0953|0.1693|0.3865|0.2288|0.1793|0.2998|
|**SBVAR**|0.0280|0.9136|0.7064|0.0389|0.2455|0.0681|0.4295|0.0242|0.0941|0.4142|0.3075|0.2256|0.2913|
|**LBVAR**<br>**w=01 d=1**|0.9429|0.2965|0.5312|0.5438|0.0873|0.8526|1.2645|0.4768|0.6344|0.4221|0.9822|0.7191|0.6461|
|**UVBFAVAR**<br>**.,**|0.2663|0.4711|0.4955|0.1179|0.2322|0.1815|0.4696|0.0204|0.0508|0.3817|0.3386|0.2638|0.2741|
|**MVBFAVAR**|0.0529|0.8255|0.6340|0.1040|0.2870|0.0143|0.4091|0.0640|0.1299|0.4208|0.2687|0.2024|0.2844|
|**SBVAR**|0.0608|0.9057|0.7080|0.0540|0.2304|0.0836|0.4389|0.0245|0.0806|0.4123|0.3140|0.2325|0.2954|
|**LBVAR**<br>**w=02 d=2**|1.5804|0.2447|0.9159|0.5142|0.4014|1.3981|1.7776|0.8322|1.3935|0.3340|1.7648|1.4305|1.0489|
|**UVBFAVAR**<br>**.,**|0.2710|0.4746|0.4908|0.1206|0.2324|0.1814|0.4687|0.0204|0.0511|0.3818|0.3384|0.2636|0.2746|
|**MVBFAVAR**|0.0138|0.8678|0.6566|0.1103|0.2605|0.0203|0.4279|0.0551|0.1099|0.4237|0.2895|0.2163|0.2876|
|**SBVAR**|0.0931|0.7710|0.6445|0.0136|0.2268|0.1351|0.4499|0.0035|0.0656|0.3984|0.3256|0.2500|0.2814|
|**LBVAR**<br>**w=01 d=2**|1.3507|0.1189|0.9098|0.3717|0.2644|0.9819|1.5416|0.8519|0.8247|0.2600|1.2492|1.1812|0.8255|
|**UVBFAVAR**<br>**.,**|0.2628|0.4827|0.4789|0.1347|0.2355|0.1821|0.4670|0.0214|0.0514|0.3817|0.3382|0.2636|0.2750|
|**MVBFAVAR**|0.0811|0.8147|0.6038|0.0674|0.2555|0.0718|0.4268|0.0373|0.1005|0.4237|0.3024|0.2256|0.2842|



Notes: Model acronyms as defined in the text. 

14 

**<u>Table 3: One- to Twelve-Months-Ahead RMSEs for Middle Atlantic</u>** 

|**Models**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**Average**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**VAR**|0.0240|0.0117|1.2435|0.5537|1.1070|0.5216|<br>0.6251|1.1142|0.4837|0.3328|1.4821|0.3672|0.6556|
|**UVFAVAR**|0.2449|0.0351|1.0379|0.2018|0.8569|0.5402|<br>0.6643|0.9914|0.4676|0.2459|1.3650|0.4627|0.5928|
|**MVFAVAR**|0.6265|0.6467|0.8088|1.2422|0.8200|0.1156|<br>0.0853|0.6455|0.0811|0.1461|0.9445|0.8369|0.5833|
|**SBVAR**|0.0236|0.0158|1.2397|0.5432|1.0999|0.5297|<br>0.6319|1.1151|0.4898|0.3369|1.4860|0.3620|0.6561|
|**LBVAR**<br>**w=03 d=05**|0.1084|0.0735|0.5033|1.2123|0.4776|0.9256|<br>0.8559|0.1385|0.3434|0.3944|0.0874|0.6373|0.4798|
|**UVBFAVAR**<br>**., .**|0.1758|0.0328|1.1658|0.0350|1.0376|0.7603|<br>0.8958|1.2390|0.7297|0.5135|1.6414|0.1816|0.7007|
|**MVBFAVAR**|0.5988|0.6398|0.8132|1.1949|0.8161|0.0634|<br>0.1013|0.6683|0.0510|0.1229|0.9803|0.8184|0.5724|
|**SBVAR**|0.0159|0.0344|1.2259|0.4944|1.0753|0.5568|<br>0.6635|1.1194|0.5166|0.3540|1.5021|0.3401|0.6582|
|**LBVAR**<br>**w=02 d=1**|0.0296|0.1683|0.5794|1.1879|0.5515|0.8009|<br>0.7638|0.0377|0.4838|0.3900|0.3018|0.2446|0.4616|
|**UVBFAVAR**<br>**.,**|0.1732|0.0419|1.1717|0.0257|1.0483|0.7699|<br>0.9075|1.2504|0.7413|0.5258|1.6535|0.1692|0.7065|
|**MVBFAVAR**|0.5156|0.6148|0.8377|1.0627|0.8006|0.0565|<br>0.1703|0.7222|0.0399|0.0621|1.0740|0.7614|0.5598|
|**SBVAR**|0.0164|0.0723|1.2006|0.3641|1.0408|0.6170|<br>0.7302|1.1450|0.5791|0.4003|1.5435|0.2890|0.6665|
|**LBVAR**<br>**w=01 d=1**|0.0290|0.1904|0.5660|1.0595|0.5672|0.3973|<br>0.5732|0.2753|0.4142|0.3570|0.6671|0.1018|0.4332|
|**UVBFAVAR**<br>**.,**|0.1698|0.0689|1.1794|0.0083|1.0674|0.7810|<br>0.9239|1.2631|0.7528|0.5379|1.6636|0.1592|0.7146|
|**MVBFAVAR**|0.4659|0.4824|0.8467|0.8532|0.7600|0.1890|<br>0.2897|0.7697|0.1631|0.0070|1.1647|0.6813|0.5561|
|**SBVAR**|0.0075|0.0913|1.1850|0.2802|1.0319|0.6350|<br>0.7752|1.1571|0.6132|0.4257|1.5639|0.2614|0.6690|
|**LBVAR**<br>**w02 d2**|0.7100|0.6596|0.5570|0.7005|0.8072|0.5442|<br>1.0099|0.5176|0.8184|0.4234|0.9765|0.6972|0.7018|
|**UVBFAVAR**<br>**=., =**|0.1677|0.0989|1.1907|0.0063|1.0874|0.7895|<br>0.9363|1.2722|0.7588|0.5443|1.6674|0.1561|0.7230|
|**MVBFAVAR**|0.4075|0.4752|0.8681|0.7652|0.7399|0.2109|<br>0.3463|0.7854|0.2007|0.0326|1.1884|0.6522|0.5560|
|**SBVAR**|0.0327|0.1884|1.1644|0.0627|1.0686|0.7278|<br>0.8867|1.2332|0.7094|0.5106|1.6352|0.1852|0.7004|
|**LBVAR**<br>**w01 d2**|0.4024|0.4964|0.4665|0.6959|0.7645|0.1196|<br>0.4837|0.7843|0.6310|0.1710|1.2502|0.3459|0.5510|
|**UVBFAVAR**<br>**=., =**|0.1466|0.2297|1.2394|0.0799|1.1659|0.8340|<br>0.9919|1.3136|0.7931|0.5774|1.6935|0.1319|0.7664|
|**MVBFAVAR**|0.4711|0.2227|0.8533|0.5048|0.7279|0.3232|<br>0.4671|0.8437|0.2981|0.1079|1.2421|0.5793|0.5534|



Notes: Model acronyms as defined in the text. 

15 

|||||**Table**|**4: One- to**|**Twelve-**|**Months-**|**Ahead R**|**MSEs for**|**Mountai**|**n**|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Models**|**1**|**2**|**3**|**4**|**5**|**6**|<br>**7**|**8**|**9**|**10**|**11**|**12**|**Average**|
|**VAR**|0.7237|0.3197|0.6920|0.5368|0.9308|0.3053|<br>0.9059|0.5794|1.2154|0.4498|0.2662|0.0850|0.5842|
|**UVFAVAR**|0.3041|0.1668|0.4541|0.2948|0.5441|0.3540|<br>0.9075|0.5065|1.2426|0.4656|0.2490|0.0743|0.4636|
|**MVFAVAR**|0.9396|0.0363|0.4980|0.6929|0.8773|0.3518|<br>1.0178|0.3661|1.2129|0.2996|0.0995|0.1507|0.5452|
|**SBVAR**|0.7191|0.3118|0.6907|0.5304|0.9176|0.3083|<br>0.9052|0.5757|1.2190|0.4490|0.2626|0.0872|0.5814|
|**LBVAR**<br>**w=03 d=05**|0.1683|0.6250|0.5985|1.1054|0.6518|1.7442|<br>2.3752|0.8155|2.6273|1.0145|1.1200|1.7952|1.2201|
|**UVBFAVAR**<br>**., .**|0.2239|0.2684|0.3466|0.4001|0.4200|0.4674|<br>1.0226|0.3881|1.3550|0.3524|0.1364|0.1842|0.4637|
|**MVBFAVAR**|0.9160|0.0472|0.5208|0.6920|0.8694|0.3400|<br>1.0059|0.3847|1.2174|0.3170|0.1127|0.1442|0.5473|
|**SBVAR**|0.7130|0.2757|0.6770|0.5002|0.8670|0.3270|<br>0.9041|0.5593|1.2347|0.4440|0.2473|0.0976|0.5706|
|**LBVAR**<br>**w=02 d=1**|0.0749|0.4867|0.4662|1.1833|0.3959|1.7464|<br>2.3469|0.7547|2.6119|0.7880|1.2344|1.6471|1.1447|
|**UVBFAVAR**<br>**.,**|0.2210|0.2695|0.3436|0.4032|0.4174|0.4708|<br>1.0258|0.3849|1.3585|0.3490|0.1330|0.1876|0.4637|
|**MVBFAVAR**|0.8634|0.0588|0.5809|0.6632|0.8387|0.3230|<br>0.9704|0.4322|1.2314|0.3587|0.1540|0.1360|0.5509|
|**SBVAR**|0.6740|0.1848|0.6350|0.4451|0.7609|0.3649|<br>0.9184|0.5226|1.2714|0.4274|0.2153|0.1227|0.5452|
|**LBVAR**<br>**w=01 d=1**|0.0651|0.4834|0.3720|1.1973|0.3461|1.5945|<br>2.2352|0.7093|2.5851|0.8615|1.1772|1.4365|1.0886|
|**UVBFAVAR**<br>**.,**|0.2183|0.2654|0.3419|0.4037|0.4189|0.4721|<br>1.0260|0.3849|1.3594|0.3487|0.1325|0.1884|0.4634|
|**MVBFAVAR**|0.7596|0.0557|0.6195|0.5729|0.7720|0.3222|<br>0.9394|0.4800|1.2536|0.4013|0.1923|0.1356|0.5420|
|**SBVAR**|0.7034|0.1209|0.5784|0.4003|0.7052|0.4051|<br>0.9286|0.4938|1.2958|0.4116|0.1938|0.1402|0.5314|
|**LBVAR**<br>**w=02 d=2**|0.4309|0.7213|0.2497|1.1392|0.0315|1.6446|<br>2.3155|0.5397|2.6710|0.8235|1.2233|1.3854|1.0980|
|**UVBFAVAR**<br>**.,**|0.2151|0.2586|0.3427|0.4030|0.4234|0.4711|<br>1.0241|0.3876|1.3580|0.3505|0.1344|0.1869|0.4629|
|**MVBFAVAR**|0.7806|0.0008|0.6234|0.5118|0.7393|0.3520|<br>0.9303|0.4805|1.2666|0.4021|0.1931|0.1421|0.5352|
|**SBVAR**|0.6144|0.0312|0.4731|0.3715|0.5735|0.4511|<br>0.9739|0.4381|1.3362|0.3796|0.1596|0.1684|0.4975|
|**LBVAR**<br>**w01 d2**|0.3579|0.6238|0.0353|1.1205|0.0015|1.3573|<br>1.9711|0.4627|2.3600|0.7385|0.9424|0.9900|0.9134|
|**UVBFAVAR**<br>**=., =**|0.2022|0.2330|0.3407|0.4013|0.4354|0.4712|<br>1.0203|0.3923|1.3567|0.3534|0.1368|0.1852|0.4607|
|**MVBFAVAR**|0.6718|0.0244|0.5782|0.3726|0.6750|0.3582|<br>0.9111|0.5031|1.2640|0.4353|0.2151|0.1148|0.5103|



Notes: Model acronyms as defined in the text. 

16 

|||||**Table 5: **|**One- to T**|**welve-M**|**onths-Ah**|**ead RMS**|**Es for N**|**ew Engla**|**nd**|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Models**|**1**|**2**|**3**|**4**|**5**|**6**|<br>**7**|**8**|**9**|**10**|**11**|**12**|**Average**|
|**VAR**|1.2563|0.1011|0.2261|1.1054|0.1178|0.1881|<br>0.6685|1.2306|0.0869|0.0597|0.5914|1.0115|0.5536|
|**UVFAVAR**|0.8783|0.5972|0.2073|0.8664|0.0428|0.3802|<br>0.5477|1.1429|0.1467|0.2260|0.3961|0.7773|0.5174|
|**MVFAVAR**|0.4843|0.9700|0.0884|0.7011|0.7657|0.2313|<br>0.3749|0.5139|0.5988|0.3988|0.1307|0.4345|0.4744|
|**SBVAR**|1.2416|0.0772|0.2169|1.0862|0.1012|0.2031|<br>0.6688|1.2408|0.0787|0.0509|0.5973|1.0204|0.5486|
|**LBVAR**<br>**w=03 d=05**|0.5970|1.2337|0.1358|0.2923|1.1111|2.1098|<br>0.0799|0.8807|1.5362|2.0144|0.0090|0.2173|0.8514|
|**UVBFAVAR**<br>**., .**|1.0000|0.9254|0.5416|1.3195|0.5375|0.8942|<br>1.0972|1.7027|0.4229|0.3532|0.9802|1.3653|0.9283|
|**MVBFAVAR**|0.4848|0.9354|0.0977|0.6836|0.6988|0.1908|<br>0.3570|0.5658|0.5838|0.3957|0.0928|0.4660|0.4627|
|**SBVAR**|1.1974|0.0096|0.1477|1.0153|0.0403|0.2654|<br>0.6758|1.2806|0.0421|0.0157|0.6254|1.0537|0.5308|
|**LBVAR**<br>**w=02 d=1**|0.7140|0.9752|0.3888|0.3296|1.4249|2.1457|<br>0.1354|0.8500|2.0528|1.9652|0.2582|0.1616|0.9501|
|**UVBFAVAR**<br>**.,**|1.0062|0.9345|0.5543|1.3350|0.5551|0.9137|<br>1.1180|1.7246|0.4456|0.3765|1.0040|1.3895|0.9464|
|**MVBFAVAR**|0.4958|0.7958|0.0755|0.6001|0.5198|0.0874|<br>0.3131|0.7034|0.5153|0.3960|0.0131|0.5495|0.4221|
|**SBVAR**|1.1159|0.1774|0.0107|0.9423|0.0809|0.4134|<br>0.7183|1.3697|0.0597|0.0697|0.7077|1.1310|0.5664|
|**LBVAR**<br>**w=01 d=1**|0.6761|0.8783|0.5395|0.3977|1.3516|1.6661|<br>0.1505|0.5378|2.0172|1.8085|0.2345|0.0963|0.8628|
|**UVBFAVAR**<br>**.,**|1.0188|0.9441|0.5709|1.3481|0.5681|0.9277|<br>1.1303|1.7368|0.4576|0.3880|1.0153|1.4007|0.9589|
|**MVBFAVAR**|0.5089|0.5286|0.0538|0.5457|0.3198|0.0232|<br>0.2931|0.8519|0.4127|0.3974|0.1489|0.6179|0.3918|
|**SBVAR**|1.1006|0.2502|0.1406|0.9037|0.1320|0.4846|<br>0.7610|1.4133|0.1124|0.1129|0.7561|1.1689|0.6114|
|**LBVAR**<br>**w02 d2**|0.7069|0.8125|1.2278|0.2444|1.3670|2.0976|<br>0.2377|0.9010|3.2253|1.8619|0.3843|0.5304|1.1331|
|**UVBFAVAR**<br>**=., =**|1.0446|0.9519|0.5882|1.3588|0.5733|0.9331|<br>1.1318|1.7364|0.4562|0.3851|1.0116|1.3964|0.9640|
|**MVBFAVAR**|0.5550|0.4071|0.0562|0.4469|0.2665|0.0669|<br>0.3041|0.8770|0.3759|0.3942|0.1850|0.6347|0.3808|
|**SBVAR**|1.1108|0.4238|0.3349|1.0526|0.2822|0.7096|<br>0.9132|1.5603|0.2924|0.2521|0.8934|1.2943|0.7599|
|**LBVAR**<br>**w01 d2**|0.6578|0.8143|1.2507|0.5241|1.3876|1.3158|<br>0.2403|0.3415|2.5119|1.5753|0.2717|0.2756|0.9305|
|**UVBFAVAR**<br>**=., =**|1.1263|0.9958|0.6646|1.4084|0.6140|0.9729|<br>1.1603|1.7612|0.4781|0.4035|1.0284|1.4118|1.0021|
|**MVBFAVAR**|0.6262|0.1135|0.0570|0.5824|0.2015|0.1722|<br>0.3538|0.9644|0.3088|0.3614|0.2615|0.6659|0.3891|



Notes: Model acronyms as defined in the text. 

17 

|||||**Table**|**6: One-  **|**to Twelv**|**e-Months**|**-Ahead R**|**MSEs fo**|**r Pacific**||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Models**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**Average**|
|**VAR**|0.0650|1.0012|0.5885|0.4370|0.1540|0.0444|0.4337|0.0898|1.1303|0.8043|0.1511|1.6704|0.5475|
|**UVFAVAR**|0.6503|1.0900|0.8696|0.3697|0.1546|0.0599|0.4228|0.0090|1.0770|0.9343|0.3127|1.5105|0.6217|
|**MVFAVAR**|0.1967|0.4755|0.5027|0.7625|0.2584|0.3494|0.1042|0.1779|0.7409|1.1675|0.4888|1.2979|0.5435|
|**SBVAR**|0.0748|1.0052|0.6012|0.4360|0.1513|0.0528|0.4383|0.0964|1.1389|0.8000|0.1448|1.6782|0.5515|
|**LBVAR**<br>**w=03 d=05**|1.0621|0.0185|0.7096|0.1877|1.8358|1.4237|0.0145|2.2149|1.2277|1.6524|1.0450|0.2554|0.9706|
|**UVBFAVAR**<br>**., .**|0.7744|1.0576|0.8905|0.3239|0.0375|0.2200|0.6219|0.2502|1.3486|0.6360|0.0106|1.8528|0.6687|
|**MVBFAVAR**|0.2541|0.5112|0.5150|0.7706|0.2490|0.3410|0.1140|0.1694|0.7498|1.1624|0.4820|1.3079|0.5522|
|**SBVAR**|0.1016|1.0158|0.6611|0.4228|0.1346|0.0843|0.4632|0.1235|1.1754|0.7777|0.1186|1.7104|0.5658|
|**LBVAR**<br>**w=02 d=1**|1.0910|0.1844|0.5144|0.0943|1.8513|1.3711|0.0699|2.1676|0.7988|1.8856|1.0565|0.2167|0.9418|
|**UVBFAVAR**<br>**.,**|0.7734|1.0632|0.8953|0.3172|0.0284|0.2290|0.6329|0.2622|1.3612|0.6222|0.0249|1.8678|0.6731|
|**MVBFAVAR**|0.4038|0.6163|0.5683|0.7804|0.2509|0.2985|0.1450|0.1589|0.7872|1.1372|0.4679|1.3378|0.5794|
|**SBVAR**|0.1631|1.0458|0.7849|0.3631|0.0906|0.1625|0.5341|0.1907|1.2602|0.7128|0.0530|1.7835|0.5954|
|**LBVAR**<br>**w=01 d=1**|1.1228|0.1949|0.4805|0.3224|1.5098|1.2044|0.1398|1.7149|0.5550|2.0703|1.1004|0.7031|0.9265|
|**UVBFAVAR**<br>**.,**|0.7632|1.0857|0.9116|0.2958|0.0037|0.2496|0.6560|0.2844|1.3816|0.6014|0.0443|1.8863|0.6803|
|**MVBFAVAR**|0.4951|0.7428|0.6259|0.7081|0.2739|0.2110|0.1947|0.1519|0.8697|1.0987|0.4423|1.3849|0.5999|
|**SBVAR**|0.1522|1.0405|0.8773|0.3060|0.0554|0.2045|0.5867|0.2314|1.3077|0.6690|0.0157|1.8242|0.6059|
|**LBVAR**<br>**w=02 d=2**|1.2389|0.3835|0.0406|0.0667|1.6356|1.9928|0.7607|2.1999|0.8746|2.0738|1.0914|0.8096|1.0974|
|**UVBFAVAR**<br>**.,**|0.7485|1.1144|0.9360|0.2703|0.0266|0.2738|0.6805|0.3075|1.4009|0.5831|0.0601|1.8998|0.6918|
|**MVBFAVAR**|0.5683|0.8134|0.6642|0.6816|0.2937|0.1825|0.2181|0.1510|0.8922|1.0808|0.4349|1.3974|0.6148|
|**SBVAR**|0.1916|1.1144|1.0506|0.1445|0.0709|0.3461|0.7362|0.3530|1.4394|0.5473|0.0901|1.9266|0.6676|
|**LBVAR**<br>**w=01 d=2**|1.2777|0.3365|0.0284|0.5189|1.1467|1.5649|0.0034|1.3949|0.3914|2.2465|1.0663|0.9750|0.9126|
|**UVBFAVAR**<br>**.,**|0.6849|1.2382|1.0359|0.1607|0.1472|0.3728|0.7801|0.3988|1.4806|0.5084|0.1262|1.9591|0.7411|
|**MVBFAVAR**|0.5467|0.8899|0.7222|0.5419|0.2964|0.1058|0.2738|0.1182|0.9495|1.0426|0.4070|1.4264|0.6100|



Notes: Model acronyms as defined in the text. 

18 

|||||**Table 7:**|**One- to T**|**welve-M**|**onths-Ah**|**ead RMS**|**Es for So**|**uth Atla**|**ntic**|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Models**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**Average**|
|**VAR**|1.2906|0.1725|0.5069|0.2603|0.0348|0.2985|0.3062|0.5061|0.2381|0.8458|0.1666|0.4233|0.4208|
|**UVFAVAR**|0.7274|0.0744|0.6383|0.2386|0.0354|0.2166|0.3558|0.4476|0.2962|0.8202|0.0902|0.3458|0.3572|
|**MVFAVAR**|1.3033|0.6803|0.5486|0.1370|0.1161|0.1838|0.0638|0.4478|0.3685|0.6217|0.0425|0.2895|0.4003|
|**SBVAR**|1.2813|0.1659|0.5080|0.2589|0.0291|0.2963|0.3137|0.5055|0.2371|0.8504|0.1678|0.4259|0.4200|
|**LBVAR**<br>**w=03 d=05**|0.1565|0.6512|0.3626|1.4114|0.4322|0.6213|1.1313|0.7045|1.8073|0.0067|1.0121|1.2521|0.7958|
|**UVBFAVAR**<br>**., .**|0.7820|0.1600|0.7304|0.3884|0.1854|0.3769|0.5224|0.6168|0.1251|0.9929|0.2639|0.5204|0.4720|
|**MVBFAVAR**|1.2642|0.6515|0.5436|0.1422|0.1048|0.1824|0.0843|0.4388|0.3650|0.6334|0.0476|0.2904|0.3957|
|**SBVAR**|1.2557|0.1447|0.5250|0.2525|0.0067|0.2870|0.3431|0.5058|0.2328|0.8676|0.1738|0.4358|0.4192|
|**LBVAR**<br>**w=02 d=1**|0.1717|0.7403|0.3775|1.3285|0.5280|0.5796|1.2010|0.7624|1.6986|0.1392|1.1399|1.1473|0.8178|
|**UVBFAVAR**<br>**.,**|0.7836|0.1636|0.7349|0.3938|0.1915|0.3833|0.5292|0.6238|0.1180|1.0001|0.2712|0.5277|0.4767|
|**MVBFAVAR**|1.1684|0.5618|0.5438|0.1390|0.0753|0.1772|0.1414|0.4197|0.3600|0.6715|0.0571|0.2921|0.3839|
|**SBVAR**|1.1824|0.0951|0.5633|0.2536|0.0396|0.2775|0.3972|0.5174|0.2151|0.9030|0.1930|0.4569|0.4245|
|**LBVAR**<br>**w=01 d=1**|0.1034|0.7498|0.4267|1.2385|0.5253|0.5820|1.0458|0.8286|1.7134|0.2820|1.2538|1.0065|0.8130|
|**UVBFAVAR**<br>**.,**|0.7814|0.1685|0.7398|0.3962|0.1958|0.3867|0.5324|0.6272|0.1148|1.0033|0.2743|0.5308|0.4793|
|**MVBFAVAR**|1.0373|0.3957|0.5518|0.1239|0.0300|0.1637|0.2231|0.4000|0.3498|0.7264|0.0575|0.3000|0.3633|
|**SBVAR**|1.1840|0.0962|0.6124|0.2459|0.0652|0.2689|0.4241|0.5241|0.2055|0.9180|0.2028|0.4667|0.4345|
|**LBVAR**<br>**w=02 d=2**|0.0683|0.7624|0.4855|1.3117|0.5957|0.5323|1.2227|1.1571|1.4928|0.4285|1.4717|0.9801|0.8757|
|**UVBFAVAR**<br>**.,**|0.7857|0.1697|0.7456|0.3961|0.1965|0.3866|0.5313|0.6260|0.1164|1.0016|0.2726|0.5290|0.4797|
|**MVBFAVAR**|1.0340|0.3644|0.5732|0.1106|0.0286|0.1530|0.2461|0.3914|0.3508|0.7366|0.0551|0.2968|0.3617|
|**SBVAR**|1.0920|0.0622|0.6877|0.2865|0.1198|0.3013|0.4737|0.5664|0.1639|0.9608|0.2385|0.4991|0.4543|
|**LBVAR**<br>**w01 d2**|0.0495|0.8838|0.5221|1.0961|0.6423|0.5079|0.9615|1.0279|1.6164|0.5120|1.4056|0.8946|0.8433|
|**UVBFAVAR**<br>**=., =**|0.7874|0.1867|0.7686|0.4022|0.2076|0.3935|0.5363|0.6309|0.1125|1.0052|0.2760|0.5322|0.4866|
|**MVBFAVAR**|0.9351|0.2350|0.6220|0.1295|0.0096|0.1585|0.2930|0.3991|0.3381|0.7711|0.0561|0.3098|0.3547|



Notes: Model acronyms as defined in the text. 

19 

||||**Ta**|**ble 8: On**|**e- to Twe**|**lve-Mont**|**hs-Ahea**|**d RMSEs**|**for Wes**|**t North C**|**entral**|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Models**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**Average**|
|**VAR**|0.9929|0.3586|0.7306|0.3623|0.4283|0.2820|0.0269|0.2976|0.3556|0.0536|0.2128|0.3543|0.3713|
|**UVFAVAR**|0.6528|0.2925|0.6948|0.4185|0.3414|0.0792|0.1403|0.3989|0.2667|0.1060|0.2419|0.2888|0.3268|
|**MVFAVAR**|0.7154|0.6677|0.5492|0.2203|0.3403|0.0254|0.4037|0.3782|0.2588|0.3411|0.5455|0.2382|0.3903|
|**SBVAR**|0.9938|0.3669|0.7281|0.3725|0.4240|0.2756|0.0178|0.2988|0.3539|0.0527|0.2087|0.3539|0.3705|
|**LBVAR**<br>**w=03 d=05**|0.6619|0.3004|0.4647|1.2679|1.4178|0.3541|0.1465|0.1881|0.4687|0.3168|0.7970|0.7683|0.5960|
|**UVBFAVAR**<br>**., .**|0.8310|0.1001|0.7620|0.5213|0.4735|0.1916|0.2534|0.2838|0.3819|0.0107|0.1259|0.4054|0.3617|
|**MVBFAVAR**|0.7067|0.6529|0.5643|0.2339|0.3322|0.0213|0.3616|0.3808|0.2595|0.3254|0.5182|0.2364|0.3828|
|**SBVAR**|1.0064|0.3931|0.7112|0.4122|0.4138|0.2479|0.0170|0.3015|0.3478|0.0497|0.1954|0.3553|0.3709|
|**LBVAR**<br>**w=02 d=1**|0.7236|0.2001|0.3952|1.4574|1.4663|0.4044|0.5113|0.2703|0.6836|0.1360|0.5317|0.7152|0.6246|
|**UVBFAVAR**<br>**.,**|0.8378|0.0940|0.7660|0.5262|0.4788|0.1965|0.2583|0.2787|0.3869|0.0158|0.1209|0.4105|0.3642|
|**MVBFAVAR**|0.6944|0.6193|0.5943|0.2933|0.2941|0.0181|0.2439|0.3874|0.2445|0.2802|0.4399|0.2335|0.3619|
|**SBVAR**|1.0054|0.4226|0.6975|0.4603|0.3974|0.2011|0.0899|0.3082|0.3422|0.0432|0.1717|0.3631|0.3752|
|**LBVAR**<br>**w=01 d=1**|0.7053|0.1561|0.2669|1.1748|1.1235|0.4772|0.2984|0.4002|0.6813|0.2667|0.2932|0.8073|0.5542|
|**UVBFAVAR**<br>**.,**|0.8415|0.0924|0.7674|0.5284|0.4808|0.1983|0.2603|0.2768|0.3888|0.0177|0.1189|0.4125|0.3653|
|**MVBFAVAR**|0.6951|0.5948|0.6350|0.3370|0.2487|0.0314|0.0970|0.4278|0.2194|0.2249|0.3563|0.2234|0.3409|
|**SBVAR**|1.0386|0.4040|0.6724|0.4818|0.3997|0.1748|0.1237|0.3108|0.3396|0.0379|0.1663|0.3694|0.3766|
|**LBVAR**<br>**w=02 d=2**|0.8979|0.1228|0.5022|1.6017|1.6139|0.5350|1.2167|0.4947|0.9043|0.6688|0.0675|0.8475|0.7894|
|**UVBFAVAR**<br>**.,**|0.8406|0.0950|0.7663|0.5273|0.4791|0.1969|0.2589|0.2782|0.3874|0.0163|0.1204|0.4110|0.3648|
|**MVBFAVAR**|0.6961|0.5389|0.6095|0.3835|0.2151|0.0334|0.0395|0.4395|0.1978|0.2103|0.3338|0.2227|0.3267|
|**SBVAR**|1.0007|0.3643|0.7060|0.4727|0.4155|0.1594|0.1979|0.3092|0.3578|0.0158|0.1429|0.3892|0.3776|
|**LBVAR**<br>**01 d2**|0.8850|0.0866|0.3363|1.0116|1.0883|0.6153|0.5401|0.5919|0.8101|0.0740|0.2057|0.8796|0.5937|
|**UVBFAVAR**<br>**w=., =**|0.8491|0.0978|0.7673|0.5304|0.4802|0.1981|0.2606|0.2767|0.3889|0.0178|0.1188|0.4126|0.3665|
|**MVBFAVAR**|0.7069|0.4608|0.6557|0.3520|0.2553|0.0456|0.0548|0.4575|0.2127|0.1683|0.2964|0.2367|0.3252|



Notes: Model acronyms as defined in the text. 

20 

||||**Ta**|**ble 9: On**|**e- to Twe**|**lve-Mont**|**hs-Ahea**|**d RMSEs **|**for West**|**South C**|**entral**|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Models**|**1**|**2**|**3**|**4**|**5**|**6**|**7**|**8**|**9**|**10**|**11**|**12**|**Average**|
|**VAR**|0.0483|0.2295|0.4568|0.6241|0.9026|0.0340|0.1676|0.7120|0.3865|0.5226|0.3158|0.0078|0.3673|
|**UVFAVAR**|0.0637|0.2400|0.2866|0.3752|0.8593|0.1526|0.0849|0.7700|0.4196|0.5812|0.3600|0.0232|0.3514|
|**MVFAVAR**|0.6987|0.2308|0.6812|0.6667|1.3093|0.1503|0.1200|1.0262|0.1703|0.7091|0.5505|0.2336|0.5456|
|**SBVAR**|0.0442|0.2284|0.4542|0.6143|0.8979|0.0403|0.1641|0.7106|0.3882|0.5214|0.3144|0.0084|0.3655|
|**LBVAR**<br>**w=03 d=05**|0.2664|0.2298|1.1203|0.8231|1.0109|0.4720|0.0217|0.8920|1.1818|0.0386|0.2912|1.0229|0.6142|
|**UVBFAVAR**<br>**., .**|0.2375|0.3645|0.1434|0.4800|0.7283|0.2742|0.1901|0.6450|0.5330|0.4693|0.2407|0.0902|0.3664|
|**MVBFAVAR**|0.6567|0.2096|0.6746|0.6501|1.2719|0.1357|0.1097|1.0046|0.1791|0.6967|0.5391|0.2225|0.5292|
|**SBVAR**|0.0330|0.2301|0.4429|0.5827|0.8890|0.0695|0.1539|0.7086|0.3973|0.5171|0.3095|0.0125|0.3622|
|**LBVAR**<br>**w=02 d=1**|0.0577|0.3978|1.0771|0.5561|1.2206|0.2628|0.1720|1.1377|0.8196|0.4359|0.0961|0.5569|0.5659|
|**UVBFAVAR**<br>**.,**|0.2457|0.3684|0.1412|0.4876|0.7247|0.2784|0.1961|0.6411|0.5379|0.4641|0.2362|0.0952|0.3681|
|**MVBFAVAR**|0.5442|0.1810|0.6559|0.5961|1.1752|0.0814|0.0679|0.9438|0.2169|0.6757|0.5052|0.1859|0.4858|
|**SBVAR**|0.0021|0.2278|0.4152|0.5278|0.8693|0.1217|0.1425|0.7053|0.4243|0.5083|0.2980|0.0263|0.3557|
|**LBVAR**<br>**w=01 d=1**|0.1095|0.3773|1.0568|0.5568|1.1579|0.2441|0.1394|0.9805|0.6846|0.4904|0.0180|0.4473|0.5219|
|**UVBFAVAR**<br>**.,**|0.2595|0.3677|0.1484|0.5006|0.7282|0.2782|0.2029|0.6428|0.5403|0.4609|0.2359|0.0977|0.3719|
|**MVBFAVAR**|0.3947|0.1586|0.5879|0.4940|1.0582|0.0154|0.0198|0.8702|0.2648|0.6623|0.4617|0.1400|0.4273|
|**SBVAR**|0.0105|0.2526|0.3999|0.5129|0.8800|0.1548|0.1452|0.7116|0.4403|0.5030|0.2960|0.0365|0.3619|
|**LBVAR**<br>**w=02 d=2**|0.1115|0.7329|0.9305|0.4221|1.8311|0.3528|0.3343|1.6584|0.6799|0.7653|0.5777|0.1479|0.7120|
|**UVBFAVAR**<br>**.,**|0.2594|0.3698|0.1643|0.5085|0.7323|0.2718|0.2068|0.6471|0.5384|0.4605|0.2388|0.0967|0.3745|
|**MVBFAVAR**|0.3810|0.2223|0.6066|0.4698|1.0457|0.0111|0.0043|0.8682|0.2828|0.6630|0.4588|0.1267|0.4284|
|**SBVAR**|0.0109|0.2863|0.3704|0.4983|0.8440|0.1964|0.1719|0.7015|0.4897|0.4854|0.2752|0.0680|0.3665|
|**LBVAR**<br>**w01 d2**|0.0817|0.6844|0.9298|0.5565|1.6054|0.2466|0.0800|1.2864|0.4364|0.6697|0.2462|0.0869|0.5758|
|**UVBFAVAR**<br>**=., =**|0.2960|0.3728|0.2161|0.5552|0.7480|0.2601|0.2272|0.6572|0.5399|0.4542|0.2420|0.0995|0.3890|
|**MVBFAVAR**|0.2887|0.2586|0.5373|0.4112|0.9782|0.0485|0.0265|0.8444|0.3308|0.6395|0.4290|0.0883|0.4068|



Notes: Model acronyms as defined in the text. 

21 

