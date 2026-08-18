---
title: wp 1439 using entropic tilting to combine BVAR Forecats with external nowcasts pdf
type: paper
source_pdf: raw/papers/wp 1439 using entropic tilting to combine BVAR Forecats with external nowcasts pdf.pdf
converted: 2026-08-18
---



<!-- Start of picture text -->
w o r k i n g<br>14  39<br>p a p e r<br>Using Entropic Tilting to Combine BVAR<br>Forecasts with External Nowcasts<br>Fabian Krueger, Todd E. Clark, and<br>Francesco Ravazzolo<br><!-- End of picture text -->

**F E D E R A L R E S E R V E B A N K O F C L E V E L A N D** 

**Working papers** of the Federal Reserve Bank of Cleveland are preliminary materials circulated to stimulate discussion and critical comment on research in progress. They may not have been subject to the formal editorial review accorded offi cial Federal Reserve Bank of Cleveland publications. The views stated herein are those of the authors and are not necessarily those of the Federal Reserve Bank of Cleveland, the Board of Governors of the Federal Reserve System, or the Norges Bank. 

**Working Paper 14-39** 

December 2014 

**Using Entropic Tilting to Combine BVAR Forecasts with External Nowcasts** Fabian Krueger, Todd E. Clark, and  Francesco Ravazzolo 

This paper shows entropic tilting to be a fl exible and powerful tool for combining medium-term forecasts from BVARs with short-term forecasts from other sources (nowcasts from either surveys or other models). Tilting systematically improves the accuracy of both point and density forecasts, and tilting the BVAR forecasts based on nowcast means and variances yields slightly greater gains in density accuracy than does just tilting based on the nowcast means. Hence entropic tilting can offer—more so for persistent variables than not-persistent variables—some benefi ts for accurately estimating the uncertainty of multi-step forecasts that incorporate nowcast information. 

Keywords: Forecasting, Prediction, Bayesian Analysis. JEL classifi cation code: E17, C11, C53 

Suggested citation: Krueger, Fabian, Todd E. Clark, and  Francesco Ravazzolo, 2014. “Using Entropic Tilting to Combine BVAR Forecasts with External Nowcasts,” Federal Reserve Bank of Cleveland, working paper no. 14-39. 

Fabian Krueger is at Heidelberg Institute for Theoretical Studies (fabian. krueger@h-its.org); Todd E. Clark is at the Federal Reserve Bank of Cleveland (todd.clark@clev.frb.org); and  Francesco Ravazzolo is at the Norges Bank and the BI Norwegian Business School (francesco.ravazzolo@norges-bank.no.) The authors thank Frank Schorfheide, Ellis Tallman, and the participants of the workshop on “Uncertainty and Economic Forecasting” (London, April 2014), the conference on “Uncertainty and Probabilistic Forecasting during the Financial and Economic Crisis” (Heidelberg, June 2014), the conference on “Advances in Applied Macro Finance and Forecasting” (Istanbul, September 2014), the 8th CFE conference (Pisa, December 2014), and the 25th EC2 conference on “Advances in Forecasting” (Barcelona, December 2014) for helpful comments. 

# **1 Introduction** 

It is commonly known that models such as vector autoregressions (VARs) or dynamic stochastic general equilibrium (DSGE) models that are effective in medium-term macroeconomic forecasting are not as effective at short-horizon forecasting. As a result, VARs and DSGE models are often combined with current-quarter forecasts, or nowcasts, from another source. One such source is a judgmental forecast from a central bank or a survey of professional forecasters, motivated by evidence that such forecasts often provide useful information beyond that contained in econometric models (e.g. Ang, Bekaert, and Wei, 2007; Faust and Wright, 2013). Alternatively, relatively accurate short-horizon forecasts can be obtained from bridging equations or factor models, surveyed in Banbura, Giannone, and Reichlin (2013) and Banbura, Giannone, Modugno, and Reichlin (2013). Compared to medium-term forecasting models, these nowcasting approaches improve near-term forecast accuracy by better adding up information in data releases for the current quarter and require dealing with differences in data release dates within the quarter (what is known as the “ragged edge” of data).<sup>1</sup> 

A number of methods for combining (VAR or DSGE) medium-term forecasts with nowcasts from another source have been used in the recent literature. Faust and Wright (2009) use shorthorizon forecasts from the Federal Reserve Board’s Greenbook as jumping-off points (treating them as data, appended to the actual data) for forecasts obtained from autoregressive and factoraugmented autoregressive models of GDP growth and inflation. Similarly, Faust and Wright (2013) use current-quarter forecasts from the Survey of Professional Forecasters as jumping-off points for inflation forecasts from a range of autoregressive, Phillips curve, and DSGE models. Schorfheide and Song (2013) and Wolters (2014) treat nowcasts from the Greenbook as data in forming forecasts at subsequent horizons from, respectively, a Bayesian VAR and DSGE models. Del Negro and Schorfheide (2013) combine current quarter Blue Chip Consensus forecasts of GDP growth, inflation, and interest rates with DSGE model forecasts by treating the Blue Chip forecasts as noisy data for the quarter.<sup>2</sup> Frey and Mokinski (2014) use survey nowcasts in estimating the parameters 

> 1While this discussion and our analysis focuses on combining forecasts from different sources, an alternative approach is to specify a single model in mixed frequency data (e.g., quarterly and monthly). For example, Schorfheide and Song (2013) and Giannone, Monti, and Reichlin (2014) develop mixed frequency BVAR and DSGE models, respectively. 

> 2 See section 5.3 of their paper for an explanation of the methodology, which relies on the Kalman filter, and some alternatives. Smets, Warne, and Wouters (2014) use similar methodology to combine medium-term survey forecasts, treated as noise in one case and news in another, with DSGE model forecasts. Monti (2010) develops a method for combining survey-based forecasts at a range of horizons with DSGE model forecasts. 

2 

of a VAR. Finally, while we are not aware of published examples, in practice it seems to be common to use conditional forecast methods (see e.g. Doan, Litterman, and Sims, 1984) to incorporate nowcast information into medium-term forecasts from BVARs.<sup>3</sup> 

As this review suggests, there is no single, standard approach for combining forecasts from medium-term projection models with short-term forecasts from other sources, either surveys or nowcasting models. In this paper, we examine the effects of using entropic tilting to combine such forecasts. Robertson, Tallman, and Whiteman (2005) introduced entropic tilting into macroeconomic forecasting, using it to impose conditions on policy rates in a small BVAR forecasting model.<sup>4</sup> Cogley and Sargent (2005) used tilting to produce BVAR forecasts that conditioned on information in the Bank of England’s forecast. More recently, Altavilla, Giacomini, and Ragusa (2013) use entropic tilting to combine survey-based forecasts of short-term interest rates with yield curve forecasts from econometric models. These studies primarily focused on point forecasts — not only tilting based on point forecasts but also measuring performance in terms of point forecast accuracy. 

Compared to some other existing approaches for combining forecasts from multiple sources, tilting has some advantages. First, it is non-parametric and highly flexible. This flexibility is needed here; in particular, merging a full multi-step BVAR forecast density with an external nowcast is not a conventional density combination problem in the spirit of Hall and Mitchell (2007), Geweke and Amisano (2011) and others.<sup>5</sup> Second, unlike simpler approaches such as treating the nowcast as additional data, entropic tilting permits the forecaster to properly capture uncertainty around the combined forecast. 

Building on the aforementioned prior research, we use tilting to improve macroeconomic forecasts from BVARs by combining them with short-term forecasts (nowcasts) from surveys and specialized models that may be more effective in short-term forecasting. Extending past research, we 

> 3As typically implemented assuming no variance around the nowcast condition, the Gaussian conditional forecasting approach yields forecasts that are the same as those obtained by treating the nowcasts as additional data. We return to this point in Section 4.4. 

> 4For the purposes of forecasting tax revenues in Iowa, Lewis and Whiteman (2014) develop an entropically tilted prior that minimizes out-of-sample mean squared error subject to a Kullback-Leibler divergence constraint that the new prior not differ too much from the original. 

> 5 The density combination literature is concerned with merging a set of densities _f_ 1 _, . . . , fn_ , all of which refer to the same (univariate or multivariate) random variable. Our setting differs in two respects. First, the nowcast refers to a univariate random variable whereas the BVAR density is jointly for five horizons. Second, the nowcast information does not come as a full density but only as a set of moment conditions. 

3 

consider tilting the BVAR forecast distributions toward not just the means but also the variances of the nowcasts, and we consider the effects of tilting on the accuracy of not only point forecasts but also density forecasts. We also compare how proper combination of forecasts via tilting affects estimates of forecast uncertainty compared to cruder approaches that do not account for nowcast uncertainty. 

In our implementation, we focus on forecasts of (U.S.) GDP growth, the unemployment rate, inflation in GDP price index, and the 3-month Treasury bill rate, all produced and evaluated with real-time data. A range of studies have considered similar variable sets (e.g. Clark, 2011; D’Agostino, Gambetti, and Giannone, 2013). We use forecasts from a BVAR with stochastic volatility as in Clark and Ravazzolo (2014).<sup>6</sup> The survey-based forecasts we consider are taken from the Survey of Professional Forecasters (SPF). We also consider model-based nowcasts (current-quarter forecasts); for GDP and inflation, the model uses the Bayesian mixed frequency formulation of Carriero, Clark, and Marcellino (2014), while for the unemployment and T-bill rates, we use small VARs in monthly data (to construct quarterly nowcasts), detailed below. 

Broadly, our results show entropic tilting to be a flexible, powerful, and effective tool for combining forecasts from BVARs with nowcasts from other sources, either a survey-based forecast or a model-based nowcast. We show that tilting, like other approaches to combining BVAR forecasts with nowcasts (e.g., Faust and Wright, 2013), systematically improves the accuracy of point forecasts of standard macroeconomic variables. Extending previous work, we also find that tilting based on nowcast means systematically improves the accuracy of density forecasts from our BVAR. We go on to show that tilting the BVAR forecasts based on not only nowcast means but also nowcast variances yields slightly greater gains in density accuracy than does just tilting based on the nowcast means. For less persistent variables such as GDP growth, the accuracy gains tend to die out as at the forecast horizon increases, but for unemployment and interest rates, the gains carry over to horizons as long as five quarters. Our results also show that tilting towards the nowcast mean and variance produces sharper forecast distributions than tilting towards the nowcast mean only. This is because the former approach incorporates the reduced variance of the nowcast – which uses intra-quarter information – whereas the latter approach implicitly conditions on the BVAR variance. Again, these effects are much more pronounced for the more persistent variables. 

> 6We obtained very similar results with a BVAR including both stochastic volatility and a steady state prior used in such studies as Clark (2011) and Wright (2013). 

4 

As to the merits of the survey-based (SPF) nowcasts compared to the model-based nowcasts, for GDP and inflation, survey forecasts from the SPF are hard to beat, so the BVAR is improved more by tilting toward the SPF nowcast than the model-based nowcasts. But for the unemployment and T-bill rates, our model-based nowcasts are more accurate than their SPF counterparts, with corresponding effects on the tilted BVAR forecasts. In a comparison of tilting on a variableby-variable basis to tilting jointly toward the nowcasts for all four variables of the BVAR, we find that the overall differences in forecast performance for the joint treatment of variables versus the individual treatment of variables are small. 

The paper proceeds as follows. Sections 2 and 3 detail the data and models, respectively. Section 4 explains the implementation of tilting and provides simple examples. Section 5 provides our results. Section 6 concludes. 

# **2 Data** 

## **2.1 Data for models** 

We use quarterly data to estimate BVAR models (detailed below) for growth of real GDP, inflation in the GDP price index or deflator (henceforth, GDP inflation), unemployment rate, and the 3-month Treasury bill rate. We compute GDP growth as 400 times the log difference of real GDP and inflation as 400 times the log difference of the GDP price index, to put them in units of annualized percentage point changes. The unemployment rate and interest rate are also defined in units of percentage points (annualized in the case of the interest rate), with quarterly rates formed as within-quarter averages of monthly rates. 

In constructing model-based nowcasts of growth, inflation, unemployment, and the T-bill rate using models detailed in the next section, we rely on a small set of other indicators, for reasons we detail in the model section. For nowcasting GDP growth, we use two monthly coincident indicators taken from Carriero, Clark, and Marcellino (2014): employment growth and the Institute of Supply Management’s production index for manufacturing. For nowcasting GDP inflation, we use monthly inflation rates of the CPI ex food and energy, the CPI for food, the CPI for energy, the PPI for capital goods, and the price deflator for new one-family houses under construction. We form nowcasts of unemployment using monthly data on not only unemployment but also growth in payroll employment and new claims for unemployment insurance. Finally, we construct 

5 

nowcasts of the T-bill rate using monthly data on the average (for the month) T-bill rate and the 3-month and 6-month T-bill rates on the 15th of the month. 

In forming all of our model-based forecasts and nowcasts, for those indicators subject to significant revisions and for which we can easily obtain the needed data, we use real-time data from the Federal Reserve Bank of Philadelphia’s Real Time Dataset for Macroeconomists (RTDSM). The variables for which we use real time data are the following: GDP, GDP price index, unemployment, and employment. Note that, for simplicity, we use “GDP” and “GDP price index” to refer to the output and price series to be forecast, even though the measures are based on GNP and a fixed weight deflator for some of the sample. As described in Croushore and Stark (2001), the quarterly vintages of the RTDSM are dated to reflect the information available around the middle of each quarter. In vintage _t_ , the available GDP and GDP price index data run through period _t −_ 1. For all remaining variables, we use currently available data obtained from the FAME database of the Federal Reserve Board of Governors: the Institute of Supply Management’s production index for manufacturing, new claims for unemployment insurance, the CPI ex food and energy, the CPI for food, the CPI for energy, the PPI for capital goods, and the price index for new home construction. 

## **2.2 SPF forecast data** 

We obtain quarterly SPF forecasts of growth, unemployment, inflation, and the T-bill rate from the website of the Federal Reserve of Philadelphia. At each forecast origin, the available forecasts span five quarterly horizons, from the current quarter through the next four quarters. We take the point forecast to be the median of the SPF responses. In some entropic tilting results, we also use a measure of forecast uncertainty. In the presented results, we consider what Clements (2014) refers to as an _ex post_ measure: the variance of recent (real-time) forecast errors, which we compute over the previous 20 forecasts. Specifically, with _Y_<sup>ˆ</sup> _t,h_ denoting the (median) SPF forecast of _Yt_ at forecast horizon _h_ (i.e., the forecast for _t_ based on data up to _t − h_ ), our first _h_ -period error measure is computed (for origin _t_ ) as 



where _R_ = 20. The end point of the window reflects our definition of forecast actuals, which we explain below.<sup>7</sup> 

> 7 We also considered a variance measure based on the cross sectional dispersion of point forecasts (see, e.g., Bomberger, 1996). The results with respect to entropic tilting were qualitatively very similar to the ones reported here. 

6 

## **2.3 Forecast evaluation sample** 

We evaluate forecasts from 1988:Q3 through 2013:Q2 (and over a pre-crisis sample of 1988:Q32007:Q4), which requires real-time data vintages from 1988 through 2013. The start date of 1988:Q3 marks the earliest possible for a common sample size across variables; SPF forecasts of the T-bill rate do not begin until 1981:Q3, and we require additional observations for computing the forecast error variance at all horizons. For each forecast origin _t_ starting with 1988:Q3, we use the realtime data vintage _t_ to estimate the forecast models and construct forecasts of quarterly values of all variables for periods _t_ and beyond. Consistent with the availability of SPF forecasts, we report results for forecast horizons of 1-5 quarters ahead. In light of the time _t −_ 1 information actually incorporated in the quarterly BVAR models used for forecasting at _t_ , the 1-quarter ahead forecast is a current quarter ( _t_ ) forecast, while the 2-quarter ahead forecast is a next quarter ( _t_ + 1) forecast, etc. For the BVAR used to forecast the four variables of interest, the starting point of the model estimation sample is 1955:Q1; we use data for the 1948-54 period to set the priors on some parameters, as detailed in the appendix. For the GDP and inflation nowcasting models, the starting point of model estimation is always 1970:Q2 and 1965:Q1, respectively.<sup>8</sup> For the unemployment rate and T-bill nowcasting models, the estimation samples begin with January 1955 and January 1965, respectively, reflecting data availability. 

As discussed in such sources as Romer and Romer (2000), Sims (2002), and Croushore (2006), evaluating the accuracy of real-time forecasts requires a difficult decision on what to take as the actual data in calculating forecast errors.<sup>9</sup> We follow studies such as Romer and Romer (2000) and Faust and Wright (2009) and use the second available estimates of GDP/GNP and the GDP/GNP deflator as actuals in evaluating forecast accuracy. In the case of _h_ -quarter ahead forecasts made for period _t_ + _h_ with vintage _t_ data ending in period _t −_ 1, the second available estimate is taken from the vintage _t_ + _h_ + 2 data set. In light of our abstraction from real-time revisions in unemployment and interest rates, we use final vintage data for evaluating forecasts of these series. 

> In the case of the model-based nowcasts, we instead define the variance as the variance of the posterior distribution of forecasts for the period in question (see Section 5). 

> 8The 1970 start date corresponds to the sample start used in Carriero, Clark, and Marcellino (2014), which was the earliest possible in the larger set of indicators they considered. For the inflation model, the 1965 start data is the earliest possible given the availability of the predictors we consider. 

> 9The GDP data available today for, say, 1985, represent the best available estimates of output in 1985. However, output as defined and measured today is quite different from output as defined and measured in 1970. For example, today we have available chain-weighted GDP; in the 1980s, output in the U.S. was measured with fixed-weight GNP. 

7 

# **3 Models** 

This section provides the specifications of our models and an overview of the estimation methods. The priors and estimation algorithms are detailed in the appendix. 

## **3.1 BVAR specification** 

We focus on forecasts from a BVAR with random walk stochastic volatility, the specification that Clark and Ravazzolo (2014) found to perform relatively well in a comparison of the forecasting performance (both point and density — stochastic volatility is particularly important for density accuracy) of a range of autoregressive models with and without time-varying volatility. 

Let _yt_ denote the _k ×_ 1 vector of model variables, _B_ 0 = a _k ×_ 1 vector of intercepts, and _Bi, i_ = 1 _, . . . , p_ , denote a _k × k_ matrix of coefficients on lag _i_ . For our set of _k_ = 4 variables, we consider a VAR( _p_ ) model with stochastic volatility, with a lag length of _p_ = 4: 



where _A_ = a lower triangular matrix with ones on the diagonal and non-zero coefficients below the diagonal, and the diagonal matrix Λ _t_ contains the time-varying variances of underlying structural shocks. This model implies that the reduced form variance-covariance matrix of innovations to the VAR is var( _vt_ ) _≡_ Σ _t_ = _A_<sup>_−_1</sup> Λ _tA_<sup>_−_1</sup><sup>_′_</sup> . Note that, as in Primiceri’s (2005) implementation, innovations to log volatility are allowed to be correlated across variables; Φ is not restricted to be diagonal. 

To estimate this BVAR, we use a Gibbs sampler, detailed in the appendix. Stochastic volatility is estimated with the algorithm of Kim, Shephard, and Chib (1998), as detailed in Primiceri (2005).<sup>10</sup> The VAR coefficients are drawn from a conditional posterior distribution that is multivariate normal, with a GLS-based mean and variance given in Clark (2011). All of our reported results are based on samples of 5000 posterior draws, obtained by retaining every 8th draw of a total sample 

> 10However, we modify the algorithm of Primiceri (2005) to reflect the correction to the ordering of steps detailed in Del Negro and Primiceri (2014). 

8 

of 40,000 post-burn draws, with a burn period of 5000 draws. 

The posterior distributions of forecasts reflect the uncertainty due to all parameters of the model and shocks occurring over the forecast horizon. To simulate the predictive density of the BVAR, from a forecast origin of period _T_ , for each retained draw of the model parameters or latent states ( _B_ , _A_ , Λ _t_ up through _T_ , and Φ), we: (1) draw innovations to log volatilities for periods _T_ + 1 through _T_ + _H_ from a multivariate normal distribution with variance-covariance matrix Φ and use the random walk model of log _λt_ + _h_ to compute _λT_ +1 _, . . . , λT_ + _H_ ; (2) draw innovations to _yT_ + _h_ , _h_ = 1 _, . . . , H_ , from a normal distribution with variance Σ _T_ + _h_ = _A_<sup>_−_1</sup> Λ _T_ + _hA_<sup>_−_1</sup><sup>_′_</sup> , and use the vector autoregressive structure of the model along with the coefficients _B_ to obtain draws of _yT_ + _h_ , _h_ = 1 _, . . . , H_ . The draws of _yT_ + _h_ are used to compute the forecast statistics of interest. 

## **3.2 Nowcast model: GDP growth** 

To align with the typical timing of the Survey of Professional Forecasters, we use the Bayesian mixed frequency modeling approach of Carriero, Clark, and Marcellino (2014) to produce a currentquarter forecast of GDP growth with data available around the end of the first week of the second month of the quarter. More specifically, we forecast the quarterly growth rate of GDP in month two of the current quarter based on the regression: 



where _t_ is measured in quarters and the vector _Xt_ contains predictors available at the time the forecast is formed. 

The specification of the regressor vector _Xt_ is a function of the way the monthly variables are sampled. For the timing we follow in this analysis, the vector _Xt_ contains variables available at about the end of the first week of month 2 of quarter _t_ . Specifically, in our implementation, it contains a constant, GDP growth in quarter _t −_ 1, employment growth in month 1 of quarter _t_ , and the ISM index in month 1 of quarter _t_ . We use employment and the ISM because, for our information timing, these are the two major coincident indicators that are available for forecasting GDP growth in the quarter. Our model with this small set of indicators performs comparably to models with the larger sets of indicators considered in Carriero, Clark, and Marcellino (2014). 

9 

## **3.3 Nowcast model: inflation in GDP price index** 

Our nowcasting model for inflation takes the same form as that described above for GDP growth, but with a different set of indicators included in _Xt_ . While the information set of the typical SPF response has included just week 1 of month 2 of the quarter since the Philadelphia Fed took over the survey, prior to that time the information set (and survey response date) changed over time, and it was often later in the month. Accordingly, for simplicity, we construct nowcasts of GDP inflation using (inflation rates of) monthly price indexes released in the second half of month 2 of the quarter, for the CPI ex food and energy, the CPI for food, the CPI for energy, the PPI for capital goods, and the price index for new home construction. This set of indicators reflects major measures of consumption and investment prices, as typically available in the middle of the quarter 

## **3.4 Nowcast model: unemployment rate** 

To align with current SPF timing, we obtain a nowcast of the quarterly average rate of unemployment by averaging the observed rate for month 1 of the quarter with forecasts for months 2 and 3. As noted above, the typical SPF response is based on an information set that includes labor market indicators for the first month of the quarter. We produce the forecasts of months 2 and 3 of the quarter using a BVAR(3) with stochastic volatility in monthly data, for the unemployment rate, growth in payroll employment, and new claims for unemployment insurance. We include unemployment claims in the model because they are commonly thought to be a leading indicator with some predictive content for the unemployment rate (e.g. Montgomery, Zarnowitz, Tsay, and Tiao, 1998), while employment is a major coincident indicator of the business cycle that might have predictive content for the unemployment rate, which has sometimes been considered to be a lagging indicator of the business cycle. This model takes the same basic form as the one detailed above, except in monthly rather than quarterly data. 

## **3.5 Nowcast model: T-bill rate** 

To align with SPF timing, we obtain a nowcast of the quarterly average 3-month T-bill rate by averaging the observed rate for month 1 of the quarter with forecasts for months 2 and 3. As SPF timing has shifted over time and respondents have access to a wide range of financial indicators, we incorporate in our interest rate nowcasting model information through the 15th of month 2 

10 

of the quarter (in the event the 15th is not a business day, we use the preceding business day). Specifically, to forecast the monthly T-bill rate for months 2 and 3 of the quarter, we use a BVAR(3) with stochastic volatility in which the variable vector _yt_ is monthly and contains the average 3- month T-bill rate in _t_ and the 3-month and 6-month T-bill rates on the 15th of month _t_ + 1. We include the daily rates in the model as a way of capturing current information that would be available to a forecaster under our timing assumption. We include the 6-month rate because, under the expectations hypothesis, it should contain information about the expected future path of the 3-month rate. This BVAR takes the same form as the one detailed above, except in monthly rather than quarterly data. 

# **4 Entropic tilting: methodology and examples** 

This section first details the general implementation of entropic tilting and then provides examples of our use. 

## **4.1 General methodology** 

In using tilting to incorporate information from survey forecasts or model-based nowcasts into medium-term forecasts from a BVAR with stochastic volatility, our starting point is a “raw” sample of _I_ (possibly vector-valued) MCMC forecast draws, 



where **y** _i ∈_ R<sup>_p_</sup> _, p ≥_ 1. In the following we interpret _f_ as a discrete distribution with _I_ possible outcomes, each of which has probability 1 _/I_ .<sup>11</sup> For simplicity, at this stage we suppress dependence on a certain variable, forecast origin date and forecast horizon. We consider modifying the distribution _f_ by imposing the moment condition 



where _g_ : R<sup>_p_</sup> _→_ R<sup>_m_</sup> and _g_ ¯ _∈_ R<sup>_m_</sup> _, m ≥_ 1. The following functional optimization problem is often called “entropic tilting”: 



> 11We’re assuming that there are no ties, which is innocuous for our continuous setting. 

11 

Here F denotes the class of all discrete distributions that can be constructed by re-weighting the draws from _f_ in an admissible way (such that the weights are positive and sum to one). Furthermore, 



is the Kullback-Leibler divergence between the candidate distribution _f_<sup>˜</sup> (which places weight _π_ ˜ _i_ on the _i_ th MCMC draw) and _f_ (which uses flat weights 1 _/I_ ). Finally, 



is the expectation of **y** under _f_<sup>˜</sup> . As discussed by Robertson, Tallman, and Whiteman (2005) and others, the tilting solution is given by setting 



The resulting (tilted) forecast distribution takes the form of an empirical distribution function (EDF). 

We should note the following broad implications. First, the solution of the tilting problem comes in the form of a set of weights for the existing sample _f_ . These can be used to either directly compute quantities of interest or simulate from the tilting distribution. Second, in practice tilting requires solving the minimization problem in (6), whose dimension equals the number of moment conditions (below we consider dimensions of one, two, four, and eight). This is often easy to do, given that the objective function is usually globally convex, and computing the gradient with respect to _γ_ (and passing it to a numerical optimizer) is straightforward.<sup>12</sup> Third, equation (5) implies that the functional form of the tilting weights is determined by the choice of _g_ ( _·_ ); we explore this point in our first example below. Finally, it is possible to ensure some smoothness on 

> 12In our implementation, we use the optim function of the R programming language (R Core Team, 2014), together with the Broyden-Fletcher-Goldfarb-Shanno (BFGS) algorithm. In case the algorithm fails to converge, we impose a very small penalty on the L2 norm of the candidate parameter _γ_ in order to regularize the problem. The corresponding R 

12 

the tilted forecast distribution by targeting a higher dimensional vector _g_ ¯ of moment conditions. We explore this below by experimenting with different sets of moment conditions. 

## **4.2 Tilting variants considered in this paper** 

In the results to be presented below, we will consider the following variants of entropic tilting. First, for a given variable – indicated by the index ( _k_ ) – we tilt the BVAR forecast distribution of the vector � _yt_<sup>(</sup> +1<sup>_k_)</sup> _. . . yt_<sup>(</sup> +5<sup>_k_)</sup> � to match a certain nowcast mean of variable _k_ (dubbed “small m” below). Second, we tilt the same distribution to match a certain nowcast mean and variance for variable _k_ (“small m/v”). Third, we consider the joint forecast distribution for the 20-dimensional vector � _yt_<sup>(1)</sup> +1 _. . . yt_<sup>(4)</sup> +5� comprising four variables and five forecast horizons. We tilt this distribution to simultaneously match the nowcast means of all four variables (“big m”). Finally, we again consider the full 20-dimensional distribution and tilt it to simultaneously match the nowcast means and variances for all four variables (“big m/v”). To avoid clutter, we henceforth suppress the superindex ( _k_ ) whenever we refer to a “representative” variable. **4.3 Example: Tilting the mean vs. mean and variance** In this section we illustrate how the forms of entropic tilting we will examine below are implemented and affect forecast distributions. In these examples, the model-based forecast comes from the BVAR-SV specification, and the forecast origin date is 2008:Q4. This origin date is interesting because it coincides with the recent recession becoming much more severe, which the SPF nowcasts pick up in real time but the BVAR in quarterly data by itself is slower to detect. The _p_ = 5 _′_ variate vector of interest, **y** _t_ : _t_ +4 = � _yt, yt_ +1 _, yt_ +2 _, yt_ +3 _, yt_ +4� , contains the GDP growth rates from 2008:Q4 to 2009:Q4 (i.e., forecasts for GDP growth zero to four quarters ahead). The two panels of Figure 1 illustrate the following implementations of tilting: 

- Targeting the SPF nowcast mean for GDP growth in 2008:Q4 (“small m”). This corresponds to setting 



As expected, the figure shows that the tilted distribution is located left of the raw one; this is 

13 

necessary to implement the SPF nowcast mean which is much smaller than the original one. In this case, the tilted density has a somewhat unconventional shape, featuring substantial probability mass at the lower end of its support. 

- Targeting the SPF nowcast mean and variance (“small m/v”) corresponds to<sup>13</sup> 



In this case, the tilted density again reaches the SPF nowcast mean, but the distribution is now bell-shaped. This is the result of targeting the nowcast variance in addition to the mean. 

In these example, _πt,i_<sup>_∗_— the tilting weight on the</sup><sup>_i_th MCMC draw — is a function of</sup><sup>_yt,i_(the first</sup> element of the vector **y** _t_ : _t_ +4 _,i_ ) alone; this follows from the specific choices of _g_ ( _·_ ) made here. For each example, the solutions to the tilting weights are given by the following. 





- Small m/v: 



Figure 2 plots the relationship for the two tilting variants. As the solutions and charts make clear, the choice of _g_ ( _·_ ) significantly affects the re-weighting of the draws in the tilted distribution. While the weight is a monotonic function of _yt,i_ in the first variant, the relationship is bell-shaped in the second variant. 

## **4.4 Example: Spillover effects on longer horizon forecasts** 

The results just presented demonstrate how tilting towards an external nowcast mean and variance yields a combined nowcast density. However, imposing moment conditions on the nowcast _yt_ also _′_ affects other elements of the vector of forecasts, **y** _t_ : _t_ +4 = � _yt, yt_ +1 _, yt_ +2 _, yt_ +3 _, yt_ +4� . While effects on other forecast horizons are difficult to see in the non-parametric solutions provided above 

> 13As detailed above, the variance, intended to measure SPF forecast uncertainty, is computed as the variance of SPF forecast errors over the past 20 quarters 

14 



<!-- Start of picture text -->
Raw MCMC SPF m SPF m/v<br>600 0.075 0.20<br>0.15<br>400 0.050<br>0.10<br>200 0.025<br>0.05<br>0 0.000 0.00<br>−10 −5 value0 5 10 −10 −5 value0 5 10 −10 −5 value0 5 10<br>count count count<br><!-- End of picture text -->

Figure 1: Histograms for raw and tilted samples. In each panel, the black vertical line shows the ex-post outcome of _−_ 6 _._ 55. 



<!-- Start of picture text -->
0.020<br>0.015<br>0.010<br>0.005<br>0.000<br>−10 −5 0 5 10<br>x<br>w<br><!-- End of picture text -->

Figure 2: Tilting weight _πt,i_<sup>_∗_,asafunctionofthefirstelement</sup><sup>_yt_ofthevector</sup><sup>**y**</sup><sup>_t_:</sup><sup>_t_+4.Thesolid</sup> line corresponds to tilting towards the nowcast mean only; the dashed line corresponds to tilting towards the nowcast mean and variance. 

15 

in equations (5) and (6), we can use a Gaussian benchmark case (extending the example in Robertson, Tallman, and Whiteman, 2005) to provide some intuition. 

Consider a five-variate vector **y** _t_ : _t_ +4, and suppose a forecaster uses a multivariate normal dis- _′_ tribution _f_ = _N_ ( _θ,_ Σ), where _θ_ = � _θ_ 1 _. . . θ_ 5� and Σ is a positive definite matrix with elements Σ _i,j_ .<sup>14</sup> Consider the tilted density _f_<sup>_∗_</sup> which imposes that the first system variable have mean _µ_ 1 and variance Ω1 _,_ 1. Then, _f_<sup>_∗_</sup> is multivariate normal _N_ ( _µ,_ Ω), with parameters 





where _Ai_ : _j, k_ : _l_ denotes the matrix consisting of rows _i_ : _j_ , columns _k_ : _l_ of any matrix _A_ . We write _Ai_ : _j, k_ if the “matrix” is a column vector, and _Ai, k_ : _l_ if it is a row vector. This Gaussian example yields the following implications. 

- In the special case that _yt_ is fixed, such that Ω1 _,_ 1 = 0, we end up at the textbook formulas for conditioning in the multivariate normal distribution. That is, entropic tilting is exactly the same as conditional forecasting. It is also exactly the same as treating the nowcast as data or jumping-off points for forecasts at subsequent horizons (Faust and Wright, 2009, 2013). Appendix A presents a simple example which demonstrates this equivalence. 

- The special case that Ω1 _,_ 1 = Σ1 _,_ 1 corresponds to a scenario in which the tilted variance for _yt_ +1 is the same as the un-tilted variance. Interestingly, the same solution obtains when targeting a mean of _θ_ 1 only, without making a tilting assumption about Ω1 _,_ 1 – see e.g. Altavilla, Giacomini, and Ragusa (2013, Section 3.1). This implies that, at least in the Gaussian case, targeting the mean only is equivalent to targeting the mean _and_ the original variance. 

- If Ω1 _,_ 1 _<_ Σ1 _,_ 1 and Σ2:5 _,_ 1 = 0 in (8), tilting “reduces” (in a matrix sense) the variance of the forecasts at other horizons. 

- The magnitude of the impact on _θ_ 2:5 and Ω2:5 _,_ 2:5 mainly depends on Σ2:5 _,_ 1, the correlation of the nowcast with the other horizons. This correlation matrix reflects the persistence of the time series, as predicted by the BVAR. 

> 14In practice, the parameters in _θ_ and Σ will depend on past realizations of _y_ . We suppress this here for simplicity. 

16 



<!-- Start of picture text -->
GDP Unemployment<br>G G 10 G G<br>20 G G G G<br>100 GGGGGG G G G G G GGGGG GG GG G GG G G GG G GGG G GGGGGG G G G G G GGG GG GGGG G GG G G GG G GGGGG G G GGGGG G GGGGGGGGGGGGGGG G G GGGGGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGG G G GG GGGGGG GGGGG GGGGGGGGGGGGGGG G GGGGGGGGGGGGGGGGGGGGGGG G GG G GG GGGGGG GG GG G G G G G GGGGGGG G G GG G GGGGG GGGGGG GG GG G G G G G GGGGGGG G G G RawTilted 86 GGGGG G GG G GG G G G G G G G GGGGG G G GGG G GG G G G GGG G GGGGG G GG G GG G G G G G GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG G GGGGGGGGG G G GGGGGG G G G GGG G GGGG GG G G GG GGG G GGGGGG G GG GGG GGGG GG RawTilted<br>G G G G<br>−10 GG G GG G GG G G G GGG GGGG GG G G GGG G GG G GGGGGG G G GG G GGGGGG G G GGG GGG G G GG GG G G GGG G GGGGGGG G GGG G G GG GG G GGG G GGGGGGG 42 GGG G GG GG GGG G GG GGG G GGGG G GGGG GGG G GGGGG G GGGGGGG GG G GG G G GG G GGG G GGG G GGG G GG GGG G GGGG G GGGG<br>1 5 1 5<br>Horizon Horizon<br>Boxplot of Values Boxplot of Values<br><!-- End of picture text -->

Figure 3: Vertical axis: Box plots of raw and tilted forecast distributions at origin date 2008:Q4. Horizontal axis: Forecast horizon _h_ . Boxes range from the 25 % to the 75 % quantile of a forecast distribution; the end of the upper vertical line is the 75% quantile plus 1 _._ 5 times the interquartile range. Forecast draws exceeding that value are plotted as points. 

The results we obtain for our examples using the non-parametric entropic solution are broadly consistent with the implications of the Gaussian specification. In the interest of brevity, we suppress the details and provide a simple example here. As the forecast horizon increases from the current quarter through the following four quarters, tilting has more persistent effects on the forecasts of the unemployment and T-bill rates (the most persistent variables) than the forecasts of GDP growth and inflation. That is, tilting based on the forecast for 2008:Q4 has larger effects on the 2009:Q4 forecasts for the unemployment and T-bill rates than on the 2009:Q4 forecasts for growth and inflation. Figure 3 illustrates these points for GDP and unemployment forecasts. The figure uses box plots to visualize the raw and tilted distributions, for the nowcast (2008:Q4) and the one-year-ahead forecast (2009:Q4). For GDP (left panel), tilting leads to a strong downward revision of the nowcast. At the same time, the mean and variance of the one-year-ahead forecast are not strongly revised. For unemployment (right panel), the mean of the one-year-ahead forecast is revised almost as strongly as that of the nowcast itself, with the revision pointing to higher unemployment rates in both cases. The stronger spillover effects for unemployment (compared to GDP) are due to larger entries in Σ2:5 _,_ 1, which represents the persistence of the series (as predicted by the BVAR). For example, the predicted first-order autocorrelation is only 0 _._ 20 in the case of GDP, but 0 _._ 76 in the case of unemployment. 

17 

## **4.5 Example: Joint tilting across variables and forecast horizons** 

In the examples above, we performed tilting on a variable-by-variable basis. However, the methodology allows us to directly consider the full multivariate forecast distribution comprising all variables and forecast horizons. Forecasts tilted based on the joint set of nowcasts should be conceptually preferable. In practice one is likely to have available and be interested in using nowcasts for all model variables. Tilting based on the set of nowcasts together yields a single set of forecasts of all variables that reflects the BVAR-captured historical relationships among the variables. To see the logic of it, consider the very simple (and parametric) approach of incorporating nowcasts through Gaussian conditional forecasting. One could first condition on the nowcast for variable 1 and produce BVAR forecasts for all variables, then condition on the nowcast for variable 2 and produce BVAR forecasts for all variables, etc. This would of course produce an entire set of alternative forecasts for each variable, reflecting conditions imposed one at a time. In practice, it is more likely the case that the entire set of nowcast conditions would be imposed at once, to obtain a single set of forecasts that reflects the joint set of conditions. The reasoning is the same for a joint approach to entropic tilting. 

Interestingly, “big” tilting turns out to be a more stringent version of the four “small” problems (one variable at a time). To see this, denote by _f_ the full (20 dimensional) empirical MCMC distribution for all variables and horizons, by _f_<sup>(</sup><sup>_k_)</sup> the distribution for variable _k_ (five dimensions = forecast horizons), and by _C_<sup>(</sup><sup>_k_)</sup> the set of moment conditions imposed on variable _k_ . Then, big tilting solves 



Small tilting for variable _k_ solves 



Notice that the candidate distributions _f_<sup>˜</sup> from (10) and _f_<sup>˜(</sup><sup>_k_)</sup> from (11) are both characterized by a weight vector of dimension 5000 (the number of MCMC draws), and the raw distributions _f_ and _f_<sup>(</sup><sup>_k_)</sup> both feature flat weights. Hence, for a given weight vector, we have that KLIC( _f, f_<sup>˜</sup> ) = KLIC( _f_<sup>˜(</sup><sup>_k_)</sup> _, f_<sup>(</sup><sup>_k_)</sup> ) _,_ and thus (11) is equivalent to solving 



18 

Hence the minimization problem (12) for small tilting is a variant of the problem (10) for big tilting, featuring a less stringent set of constraints. This implies that big tilting will typically entail a more drastic move away from the baseline distribution compared to small tilting. In order to illustrate this point, we again consider the 2008:Q4 example, and tilting based on the SPF nowcast means _and_ variances (big m/v, small m/v). Table 1 illustrates the logical necessity that the four small tilting approaches are KLIC-closer to raw MCMC than the big tilting approach (although, in this steep recession example, all approaches are fairly far away from the equal weights of raw MCMC, because the nowcast of growth is so different from the BVAR forecast). Similarly, Figure 4 presents “Lorenz curves” for the observation weights resulting from big versus small tilting. The figure shows that the weights for big tilting are highly unequal, with a small number of dominant MCMC draws (for example, the ten largest weights sum up to 0 _._ 5548). The weights for the small tilting problems are much more equal, i.e. the Lorenz curves in Figure 4 are left of the one for big tilting. Note that the small tilting method for inflation generates by far the most uniform weights (leftmost Lorenz curve), which is in line with the fact that in 2008:Q4 the current quarter MCMC forecast (2 _._ 74) is already close to the SPF mean nowcast (2 _._ 6). 

In this example, the reliance of the “big” tilting distribution on a few Monte Carlo draws is striking. However, in our sample, it does not seem harmful in terms of forecasting performance. In particular, we experimented with importance sampling approaches which deliberately oversample the tails of the BVAR distribution. While producing much more balanced tilting weights, these approaches did not result in more accurate distribution forecasts in terms of the Cumulative Ranked Probability Score (see Section 5 below). In the interest of simplicity, we hence focus on standard sampling approaches in the following. 

|Method|Variable|KLIC divergence<br>from equal weights|
|---|---|---|
|big m/v|(all)|4995.603|
||GDP|4994.113|
|small m/v|UNE<br>INF|4993.483<br>4991.631|
||TBI|4992.903|



Table 1: KLIC divergences for big versus small tilting in the 2008Q4 example. See equation (4) for the underlying formula. 

19 



<!-- Start of picture text -->
1.00<br>0.75<br>Method<br>big<br>small − GDP<br>0.50<br>small − INF<br>small − TBI<br>small − UNE<br>0.25<br>0.00<br>0.00 0.25 0.50 0.75 1.00<br>Share of observations<br>Sum of weights<br><!-- End of picture text -->

Figure 4: Lorenz curve of weights in the 2008Q4 example. _Reading example:_ The topmost line indicates that for inflation, the 25 % smallest weights (horizontal axis) add up to roughly 0 _._ 07 (vertical axis). 

# **5 Forecast results** 

We first consider the accuracy of point forecasts (defined as posterior means), using root mean square errors (RMSEs). We then consider density forecasts, using the average continuous ranked probability score (CRPS). Studies such as Gneiting and Raftery (2007) and Gneiting and Ranjan (2011) discuss the advantages of the CRPS over other measures. The CRPS, defined such that a lower number is a better score, is given by 



where _yt_<sup>_o_</sup> + _h_<sup>denotestheobservedoutcome,</sup><sup>_F_denotesthecumulativedistributionfunctionasso-</sup> ciated with the (posterior) predictive density _f_ , and 1 _{yt_<sup>_o_</sup> + _h_<sup>_≤z}_denotesanindicatorfunction</sup> taking value 1 if _yt_<sup>_o_</sup> + _h_<sup>_≤z_and 0 otherwise.In our analysis,</sup><sup>_F_takes the form of an empirical dis-</sup> tribution function, whereby the observation weights are equal in the case of raw MCMC but not in the case of tilted distributions. We employ the algorithm by Hersbach (2000, Section 4) – which allows for non-equal weights – to compute the CRPS in both cases. 

In order to test the statistical significance of differences in predictive performance, we consider 

20 

pairwise tests of equal predictive accuracy (henceforth, EPA; Diebold and Mariano, 1995; West, 1996) in terms of either RMSE or CRPS. All EPA tests we conduct compare the raw BVAR forecasts against a given variant of entropic tilting, using two sided tests and standard normal critical values. Based on simulation evidence in Clark and McCracken (2013), in computing the variance estimator which enters the test statistic, we employ a rectangular kernel truncated at lag _h−_ 1 and incorporate the finite sample correction due to Harvey, Leybourne, and Newbold (1997).<sup>15</sup> 

Our use of EPA tests based on normal critical values may be viewed as an approximation that simplifies an inference problem that, in our context, features many complexities — possible nesting of forecasts and tilting that bears similarities to conditional forecasting — not necessarily easily dealt with in the forecast evaluation literature (see e.g. Clark and McCracken, 2013, 2014).<sup>16</sup> Under the asymptotics of Giacomini and White (2006), a test of a null of equal forecast accuracy in the finite sample (at estimated model parameters) is generally normally distributed, subject to a requirement that the model parameters be estimated with a rolling sample of data. While we have not estimated the BVAR with a rolling sample of data, Monte Carlo evidence in Clark and McCracken (2013) indicates that, with nested models estimated with an expanding data sample (the approach we have used with our BVAR), EPA tests compared against normal critical values can be viewed as a somewhat conservative (modestly under-rejecting compared to nominal size) test for equal accuracy in the finite sample. 

As noted in Section (4), we consider the following variants of entropic tilting: small m, in which we tilt the BVAR forecast distribution of the vector � _yt_<sup>(</sup> +1<sup>_k_)</sup> _. . . yt_<sup>(</sup> +5<sup>_k_)</sup> � to match a certain nowcast mean of variable _k_ ; small m/v, in which we tilt the forecast distribution of variable _k_ to match the nowcast mean and variance; big m, in which we tilt the entire 20 element vector of variables and horizons to simultaneously match the nowcast means of all four variables; and big m/v, in which we tilt the entire 20 element vector of variables and horizons to simultaneously match the nowcast means and variances of all four variables. We separately apply each of the tilting variants to nowcasts from the SPF and from the nowcasting models described in Section 3. In the case of 

> 15In the rare cases in which the rectangular kernel yields a negative variance estimate, we resort to Bartlett kernel weights (Newey and West, 1987) in order to ensure positivity. In these cases, we use the automatic bandwidth selection procedure of Newey and West (1994) as implemented in R’s sandwich package (Zeileis, 2004). 

> 16At the one-step horizon, the tilted forecasts are, by construction, essentially the nowcasts, so the benchmark BVAR forecast and each tilted forecast are not nested, in which case the application of the EPA test is valid. At longer horizons, the picture is less clear; the tilted forecasts are functions of the nowcasts and the underlying BVAR forecasts. Under some conditions, at horizons of 2 or more periods, the tilted and BVAR forecasts could be seen as nested under a null of equal accuracy. Regardless, the multi-step tilted forecasts bear similarities to conditional forecasts; Clark and McCracken (2014) propose a modified test of EPA necessary for application to conditional forecasts. 

21 

the SPF-based results, the variances used in tilting are computed (using real time data available at each forecast origin) as described in section 2.2; for model-based nowcasts, the variances used in tilting are defined as the variance of the posterior distribution of BVAR forecasts for the period in question. 

In light of the potentially large effects of the Great Recession of 2007-2009 and ensuing slow recovery, we provide results for a sample that ends in 2007:Q4, the business cycle peak as dated by the National Bureau of Economic Research, and a full sample that ends in 2013:Q2. 

## **5.1 Comparison of current-quarter forecasts** 

Before examining the effects of entropic tilting of BVAR forecasts toward different nowcasts, it is useful to compare the accuracy of current quarter forecasts from the BVAR, the SPF, and the nowcasting models. Table 1 provides the RMSEs and CRPS scores of each current quarter forecast (except that we don’t provide CRPS scores for the SPF forecasts because the SPF does not include the forecast density information needed to compute the CRPS over our sample). These results yield the following findings. 

- Consistent with previous studies, current-quarter forecasts from the SPF and the models designed for nowcasting are generally more accurate than the current quarter forecasts from the BVAR. For example, in the case of GDP growth over the pre-crisis sample, the SPF and mixed frequency nowcasting models have RMSEs of 1.580 and 1.682, respectively, compared to the BVAR’s RMSE of 1.974. The differences (for GDP growth and unemployment) are even larger in the full sample than in the pre-crisis sample. 

- Compared to SPF, some of the nowcasting models yield better accuracy, while others yield less accuracy. For GDP growth, the mixed frequency nowcasting model is almost as accurate as SPF in the pre-crisis sample and modestly less accurate in the full sample, reflecting the better job the SPF did in picking up the sharp downturn of the Great Recession (see the discussion in Carriero, Clark, and Marcellino (2014)). For unemployment and the T-bill rate, the model-based nowcasts are at least somewhat more accurate than the SPF forecasts.<sup>17</sup> For instance, in the pre-crisis sample, the model-based nowcast of the T-bill rate has an RMSE of 

> 17Montgomery, Zarnowitz, Tsay, and Tiao (1998) also find that quarterly forecasts of the unemployment rate are greatly improved when the forecasting model takes account of the unemployment rate in the first month of the quarter. 

22 

0.066, compared to the SPF RMSE of 0.133. 

- The CRPS scores move closely in line with the RMSEs, both qualitatively and in terms of the magnitude of improvements of nowcasts over current-quarter forecasts from the BVAR. 

|||_Pre_|_Crisis (8_|_8Q3 – 0_|_7Q4)_|_Com_|_plete (8_|_8Q3 – 1_|_3Q2)_|
|---|---|---|---|---|---|---|---|---|---|
|||GDP|UNE|INF|TBI|GDP|UNE|INF|TBI|
||_SPF_|1.580|0.125|0.767|0.133|1.591|0.151|0.809|0.133|
|_RMSE_|_BMF_|1.682|0.095|0.861|0.066|1.899|0.095|0.985|0.072|
||_BVAR_|1.973|0.157|0.877|0.406|2.396|0.235|0.939|0.406|
|_CRPS_|_BMF_|0.960|0.053|0.495|0.037|1.048|0.053|0.554|0.035|
||_BVAR_|1.123|0.089|0.506|0.214|1.277|0.117|0.541|0.214|



Table 2: Root Mean Squared Errors and correlations for different nowcasts (SPF = Survey of Professional Forecasters, BMF = Bayesian Mixed Frequency, BVAR = Bayesian VAR with stochastic volatility). SPF and BMF use data up to daily frequency; BVAR is based on quarterly data. 

## **5.2 Main results** 

We now consider tilting longer-horizon forecasts based on just current-quarter forecasts. As noted above, while it is common to condition longer-horizon model-based forecasts on nowcasts from other sources (judgment, models, etc.), tilting may be seen as a more flexible generalization. Importantly, it permits the forecaster to estimate the uncertainty around longer-horizon forecasts to properly reflect uncertainty surrounding the nowcast. The results are presented in Table 3. In light of the common central bank practice of reporting growth and inflation rates that are averages over four quarters, the table provides results for (annualized) quarterly forecasts four and five quarters ahead and for four-quarter averages four and five quarters ahead (in the columns “4*” and “5*”, respectively). These results yield the following key take-aways. 

- In all cases, tilting forecasts based on just the nowcast (point or point and variance) from either the SPF or the nowcasting models improves the accuracy of point and density forecasts at horizons of two and three quarters.<sup>18</sup> For example, in the full sample results for GDP growth at the three quarters-ahead horizon, under the small m approach, tilting toward the nowcast from the mixed frequency model lowers the RMSE of the BVAR forecast from 2.663 

> 18In addition, tilting the nowcast (= one quarter ahead forecast) improves the forecast at that horizon itself. This result is to be expected from the preliminary findings in Table 2. 

23 

to 2.575; the difference is significant at the 1% level (two-sided test). For the same sample and horizon, tilting the T-bill forecasts toward the model-based nowcasts (small m approach) lowers the RMSE of the BVAR from 1.060 to 0.820 (difference significant at 1% level). Tilting has quantitatively similar effects on density forecast accuracy as measured by the CRPS. 

- At forecast horizons of four and five quarters, the performance of forecasts tilted toward nowcasts is more mixed. At these horizons, tilting has relatively little benefit for forecasts of GDP growth and inflation. But it has some benefit for forecasts of the more persistent variables, the unemployment and T-bill rates. As an example, at the five step horizon, tilting the T-bill forecasts toward the model-based nowcasts lowers the full-sample RMSE of the BVAR from 1.594 to 1.428 (difference significant at 1% level). Again, tilting has quantitatively similar effects on density forecast accuracy as measured by the CRPS. These patterns align with the observations drawn in the illustration of Section 4.4. 

- Tilting the BVAR forecasts toward both the mean and variance of nowcasts (“m/v”) — rather than just the mean or point nowcast (“m”)— yields small additional gains in density forecast accuracy. This pattern is very robust: In all scenarios (variables, subsamples and forecast horizons) covered by Table 3, the CRPS score of the best “m/v” specification is smaller than that of the best “m” specification. For example, in the case of the unemployment rate, _h_ = 2 and the full sample, the best specification based on the mean only (“BMF big m”) attains a CRPS of 0 _._ 145, whereas the best mean/variance specification (“BMF small m/v”) attains a CRPS of 0 _._ 137. By comparison, the CRPS of the raw BVAR distribution is 0 _._ 217. 

- Jointly considering the nowcasts of all four variables (“big m/v”) versus considering all variables separately (“small m/v”) tends to perform similarly well, with each approach outperforming the other in a number of scenarios. While one interpretation might be that joint treatment offers little overall advantage, an alternative interpretation might be that it is conceptually preferable for imposing tilting at a system level and does so at little (if any) cost, in terms of forecast accuracy. 

- For GDP and inflation, both ‘tilting targets’ (survey and model nowcasts) perform comparably before the crisis, whereas survey nowcasts yield better results in the full sample. This likely reflects the superiority (noted above) of the survey in picking up the Great Recession on a timely basis. By contrast, this effect cannot be observed for unemployment and T-bill, where tilting toward model nowcasts performs better in both periods. 

24 

|||||_Pre Crisis (8_|_8Q3 – 07Q_|_4)_|||_Com_|_plete (88Q_|_3 – 13Q2)_|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||_Horizon_|1|2|3|4|5|4*|5*|1|2|3|4|5|4*|5*|
||||||||||**GDP**|||||||
||raw|1.973|2.040|2.015|**1.992**|**1.969**|1.441|1.452|2.396|2.593|2.663|2.636|**2.612**|2.086|2.140|
||SPF small m|1.580<sup>_∗_</sup>|1.986|1.960<sup>_∗_</sup>|2.059|2.012|1.239<sup>_∗_</sup>|1.457|**1.591**<sup>_∗∗_</sup>|2.454<sup>_∗∗_</sup>|2.534<sup>_∗∗_</sup>|2.672|2.633|1.712<sup>_∗_</sup>|2.080|
||SPF small m/v|1.580<sup>_∗_</sup>|1.963|**1.959**<sup>_∗_</sup>|2.031<sup>_∗_</sup>|2.006|1.229<sup>_∗_</sup>|1.440|1.591<sup>_∗∗_</sup>|**2.385**<sup>_∗_</sup>|2.526<sup>_∗∗_</sup>|2.642|2.622|1.692<sup>_∗_</sup>|2.054|
|RMSE|SPF big m|1.580<sup>_∗_</sup>|**1.963**|1.979|2.042|2.051|1.234|1.441|1.591<sup>_∗∗_</sup>|2.403<sup>_∗_</sup>|2.563<sup>_∗_</sup>|2.661|2.685|1.710<sup>_∗_</sup>|2.083|
||SPF big m/v|**1.578**<sup>_∗_</sup>|1.990|1.992|2.007|1.975|**1.216**|**1.417**|1.591<sup>_∗∗_</sup>|2.388<sup>_∗_</sup>|**2.525**|**2.619**|2.712|**1.671**<sup>_∗_</sup>|**2.039**|
||BMF small m|1.682|1.991|1.969<sup>_∗_</sup>|2.048|2.010|1.258|1.454|1.899<sup>_∗∗_</sup>|2.492<sup>_∗_</sup>|2.575<sup>_∗∗_</sup>|2.666|2.631|1.841<sup>_∗_</sup>|2.101|
||BMF small m/v|1.682|1.963|1.968|2.024|2.002|1.250|1.441|1.899<sup>_∗∗_</sup>|2.469<sup>_∗∗_</sup>|2.572<sup>_∗_</sup>|2.643|2.620|1.832<sup>_∗_</sup>|2.086|
||BMF big m|1.681|1.991|2.015|2.124<sup>_∗_</sup>|2.068|1.295|1.507|1.903<sup>_∗∗_</sup>|2.505|2.764|2.767<sup>_∗_</sup>|2.709|1.944|2.194|
||<br>BMF big m/v|1.686|2.007|2.098|2.094|1.990|1.290|1.491|1.895<sup>_∗∗_</sup>|2.537|2.716|2.704|2.684|1.884<sup>_∗_</sup>|2.154|
||raw|1.123|1.158|1.147|**1.136**|**1.128**|0.826|0.832|1.277|1.382|1.420|**1.408**|**1.399**|1.123|1.158|
||SPF small m|0.924<sup>_∗∗_</sup>|1.131|1.122<sup>_∗_</sup>|1.162<sup>_∗_</sup>|1.143|0.722|0.831|0.966<sup>_∗∗_</sup>|1.315<sup>_∗∗_</sup>|1.358<sup>_∗∗_</sup>|1.423|1.409|0.928<sup>_∗∗_</sup>|1.124|
||SPF small m/v|0.901<sup>_∗∗_</sup>|**1.119**|**1.115**<sup>_∗_</sup>|1.156<sup>_∗_</sup>|1.145|0.711|0.825|0.907<sup>_∗∗_</sup>|**1.282**<sup>_∗∗_</sup>|1.344<sup>_∗∗_</sup>|1.414|1.408|0.915<sup>_∗∗_</sup>|1.114|
|CRPS|SPF big m|0.959<sup>_∗_</sup>|1.141|1.125|1.160|1.139|0.730|0.824|0.995<sup>_∗∗_</sup>|1.308<sup>_∗_</sup>|1.364<sup>_∗_</sup>|1.426|1.421|0.937<sup>_∗∗_</sup>|1.124|
||<br>SPF big m/v|**0.899**<sup>_∗∗_</sup>|1.146|1.127|1.154|1.133|**0.707**|**0.815**|**0.907**<sup>_∗∗_</sup>|1.304<sup>_∗_</sup>|**1.344**<sup>_∗_</sup>|1.409|1.453|**0.907**<sup>_∗∗_</sup>|**1.112**|
||<br>BMF small m|0.972<sup>_∗∗_</sup>|1.132|1.128<sup>_∗_</sup>|1.154|1.143|0.733|0.829|1.064<sup>_∗∗_</sup>|1.335<sup>_∗∗_</sup>|1.379<sup>_∗∗_</sup>|1.419|1.408|0.989<sup>_∗∗_</sup>|1.136|
||BMF small m/v|0.958<sup>_∗_</sup>|1.120|1.123<sup>_∗_</sup>|1.150|1.143|0.723|0.824|1.044<sup>_∗∗_</sup>|1.321<sup>_∗∗_</sup>|1.372<sup>_∗∗_</sup>|1.413|1.406|0.979<sup>_∗∗_</sup>|1.130|
||BMF big m|1.020|1.150|1.149|1.203<sup>_∗∗_</sup>|1.176|0.758|0.856|1.109<sup>_∗∗_</sup>|1.349|1.452|1.502<sup>_∗_</sup>|1.469|1.030|1.182|
||<br>BMF big m/v|0.961<sup>_∗_</sup>|1.159|1.192|1.195|1.155|0.748|0.853|1.040<sup>_∗∗_</sup>|1.353|1.465|1.466<sup>_∗_</sup>|1.448|1.013<sup>_∗_</sup>|1.170|
||||||||||**UNE**|||||||
||raw|0.157|0.274|0.397|0.511|0.605|||0.235|0.463|0.706|0.940|1.147|||
||SPF small m|0.125<sup>_∗_</sup>|0.238|0.350|0.466|0.566|||0.151<sup>_∗_</sup>|0.352|0.577|0.817|1.038|||
||SPF small m/v|0.125<sup>_∗_</sup>|0.239|0.352|0.468|0.567|||0.151<sup>_∗_</sup>|0.350|0.573|0.810|1.028|||
|RMSE|SPF big m|0.125<sup>_∗_</sup>|0.227<sup>_∗_</sup>|0.329<sup>_∗_</sup>|0.443|0.550|||0.151<sup>_∗_</sup>|0.329|0.550|0.780|1.003|||
||<br>SPF big m/v|0.122<sup>_∗_</sup>|0.226<sup>_∗_</sup>|0.330<sup>_∗_</sup>|0.441|0.543|||0.148<sup>_∗_</sup>|0.328|0.535|0.760|0.987|||
||BMF small m|0.095<sup>_∗∗_</sup>|0.192<sup>_∗_</sup>|0.296<sup>_∗_</sup>|0.407<sup>_∗_</sup>|0.511<sup>_∗_</sup>|||0.095<sup>_∗∗_</sup>|0.255|**0.468**|**0.720**|**0.969**|||
||BMF small m/v|0.096<sup>_∗∗_</sup>|0.191<sup>_∗_</sup>|0.295<sup>_∗_</sup>|0.406<sup>_∗_</sup>|0.512<sup>_∗_</sup>|||0.097<sup>_∗∗_</sup>|0.264|0.499|0.754|1.007|||
||BMF big m|**0.095**<sup>_∗∗_</sup>|**0.177**<sup>_∗_</sup>|**0.269**<sup>_∗∗_</sup>|**0.385**<sup>_∗_</sup>|0.503<sup>_∗_</sup>|||0.094<sup>_∗∗_</sup>|**0.252**|0.497|0.760|1.009|||
||BMF big m/v|0.095<sup>_∗∗_</sup>|0.179<sup>_∗_</sup>|0.277<sup>_∗_</sup>|0.390<sup>_∗_</sup>|**0.498**<sup>_∗_</sup>|||**0.093**<sup>_∗∗_</sup>|0.272|0.507|0.757|0.994|||
||raw|0.089|0.152|0.222|0.290|0.351|||0.117|0.217|0.333|0.453|0.569|||
||SPF small m|0.074<sup>_∗∗_</sup>|0.137<sup>_∗_</sup>|0.200|0.268|0.328|||0.087<sup>_∗∗_</sup>|0.178|0.280<sup>_∗_</sup>|0.396|0.512|||
||SPF small m/v|0.070<sup>_∗∗_</sup>|0.133<sup>_∗_</sup>|0.197|0.267|0.329|||0.083<sup>_∗∗_</sup>|0.176<sup>_∗_</sup>|0.276<sup>_∗_</sup>|0.392|0.507|||
|CRPS|<br>SPF big m|0.075<sup>_∗∗_</sup>|0.134<sup>_∗_</sup>|0.192<sup>_∗_</sup>|0.259|0.322|||0.088<sup>_∗∗_</sup>|0.171<sup>_∗_</sup>|0.268<sup>_∗_</sup>|0.378<sup>_∗_</sup>|0.494|||
||<br>SPF big m/v|0.069<sup>_∗∗_</sup>|0.126<sup>_∗∗_</sup>|0.183<sup>_∗_</sup>|0.250<sup>_∗_</sup>|0.314|||0.081<sup>_∗∗_</sup>|0.166<sup>_∗_</sup>|0.256<sup>_∗_</sup>|0.367<sup>_∗_</sup>|0.486<sup>_∗_</sup>|||
||<br>BMF small m|0.064<sup>_∗∗_</sup>|0.122<sup>_∗_</sup>|0.179<sup>_∗_</sup>|0.241<sup>_∗_</sup>|0.298<sup>_∗_</sup>|||0.072<sup>_∗∗_</sup>|0.147<sup>_∗_</sup>|0.241|0.359<sup>_∗_</sup>|0.479<sup>_∗_</sup>|||
||BMF small m/v|**0.054**<sup>_∗∗_</sup>|0.110<sup>_∗_</sup>|0.170<sup>_∗_</sup>|0.233<sup>_∗_</sup>|0.294<sup>_∗_</sup>|||**0.054**<sup>_∗∗_</sup>|**0.137**<sup>_∗_</sup>|0.241<sup>_∗_</sup>|0.358<sup>_∗_</sup>|0.482<sup>_∗_</sup>|||
||BMF big m|0.066<sup>_∗∗_</sup>|0.117<sup>_∗_</sup>|0.169<sup>_∗∗_</sup>|0.232<sup>_∗_</sup>|0.299<sup>_∗_</sup>|||0.073<sup>_∗∗_</sup>|0.145<sup>_∗_</sup>|0.247<sup>_∗_</sup>|0.364<sup>_∗_</sup>|0.489<sup>_∗_</sup>|||
||<br>BMF big m/v|0.055<sup>_∗∗_</sup>|**0.106**<sup>_∗∗_</sup>|**0.160**<sup>_∗∗_</sup>|**0.224**<sup>_∗∗_</sup>|**0.288**<sup>_∗_</sup>|||0.054<sup>_∗∗_</sup>|0.140<sup>_∗∗_</sup>|**0.237**<sup>_∗∗_</sup>|**0.354**<sup>_∗∗_</sup>|**0.477**<sup>_∗_</sup>|||



Table 3: **Empirical results for entropic tilting.** “RMSE” rows contain root mean squared errors. “CRPS” rows contain mean cumulative ranked probability scores. <u>raw</u> – MCMC output of BVAR-SV model. Alternative tilting targets: SPF small m – SPF mean nowcast for the same variable. SPF small m/v – SPF nowcast mean and variance for the same variable. SPF big m – SPF nowcast means for all four variables. SPF big m/v – SPF nowcast means and variances for all four variables. <u>BMF small m, BMF small m/v,</u> BMF big m and BMF big m/v are defined analogously. One and two stars indicate rejections of equal predictive ability at the five and one percent level (two sided tests; implementation details described in the beginning of Section 5). 

||||_P_|_re Crisis (8_|_8Q3 – 07Q_|_4)_|||_Com_|_plete (88Q_|_3 – 13Q2)_|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||_Horizon_|1|2|3|4|5|4*|5*|1|2|3|4|5|4*|5*|
||||||||||**INF**|||||||
||raw|0.877|0.997|0.972|1.008|1.139|0.698|0.785|0.939|0.997|1.016|1.053|1.176|0.721|0.800|
||SPF small m|0.767<sup>_∗_</sup>|0.920<sup>_∗∗_</sup>|0.943|0.997|1.115|0.634|0.746|0.809<sup>_∗∗_</sup>|0.915<sup>_∗∗_</sup>|0.977|1.031|1.146|0.636<sup>_∗_</sup>|0.747|
||SPF small m/v|0.767<sup>_∗_</sup>|0.920<sup>_∗∗_</sup>|0.944|0.997|1.117|0.634|0.748|0.809<sup>_∗∗_</sup>|0.917<sup>_∗∗_</sup>|0.977|1.031|1.149|0.637<sup>_∗_</sup>|0.750|
|RMSE|SPF big m|**0.767**<sup>_∗_</sup>|0.914<sup>_∗∗_</sup>|**0.929**|**0.986**|**1.111**|**0.617**|**0.735**|0.809<sup>_∗∗_</sup>|0.908<sup>_∗∗_</sup>|**0.949**<sup>_∗_</sup>|**1.009**|**1.143**|**0.614**<sup>_∗∗_</sup>|**0.730**|
||<br>SPF big m/v|0.771<sup>_∗_</sup>|**0.911**<sup>_∗_</sup>|0.935|1.009|1.114|0.633|0.746|**0.807**<sup>_∗∗_</sup>|**0.903**<sup>_∗∗_</sup>|0.966|1.035|1.150|0.634<sup>_∗_</sup>|0.746|
||<br>BMF small m|0.861|1.023|1.004|1.021|1.148|0.728|0.809|0.985|1.024|1.053|1.075|1.198|0.766|0.831|
||BMF small m/v|0.861|1.029|1.004|1.021|1.149|0.729|0.810|0.985|1.030|1.055|1.076|1.200|0.769|0.833|
||BMF big m|0.861|0.994|0.998|1.052|1.137|0.722|0.809|0.982|1.004|1.058|1.096|1.196|0.762|0.834|
||BMF big m/v|0.869|1.020|1.028<sup>_∗_</sup>|1.050|1.124|0.736|0.815|0.989|1.017|1.078<sup>_∗_</sup>|1.094<sup>_∗_</sup>|1.192|0.766|0.833|
||raw|0.506|0.571|0.548|0.585|0.663|0.401|0.454|0.541|0.579|0.577|0.610|0.688|0.415|0.465|
||SPF small m|0.443<sup>_∗_</sup>|0.534<sup>_∗∗_</sup>|0.541|0.579|0.653|0.374|0.440|0.470<sup>_∗∗_</sup>|0.541<sup>_∗∗_</sup>|0.565|0.602|0.676|0.379<sup>_∗_</sup>|0.445|
||SPF small m/v|**0.436**<sup>_∗_</sup>|**0.529**<sup>_∗∗_</sup>|0.538|**0.576**|**0.651**|0.367|0.436|**0.464**<sup>_∗∗_</sup>|**0.535**<sup>_∗∗_</sup>|0.560|**0.597**|**0.673**|0.370<sup>_∗_</sup>|0.439|
|CRPS|SPF big m|0.451<sup>_∗_</sup>|0.536<sup>_∗_</sup>|0.539|0.577|0.654|0.371|0.436|0.480<sup>_∗∗_</sup>|0.543<sup>_∗∗_</sup>|0.559|0.598|0.677|0.378<sup>_∗_</sup>|0.442|
||SPF big m/v|0.441<sup>_∗_</sup>|0.531<sup>_∗_</sup>|**0.536**|0.581|0.656|**0.366**|**0.434**|0.465<sup>_∗∗_</sup>|0.538<sup>_∗∗_</sup>|**0.554**|0.597|0.681|**0.368**<sup>_∗_</sup>|**0.436**|
||BMF small m|0.491|0.581|0.560|0.589|0.667|0.411|0.465|0.546|0.591|0.591|0.619|0.698|0.430|0.478|
||BMF small m/v|0.495|0.584|0.561|0.588|0.667|0.413|0.465|0.553|0.593|0.592|0.618|0.698|0.431|0.477|
||BMF big m|0.496|0.567|0.565|0.603|0.665|0.414|0.466|0.549|0.583|0.597<sup>_∗_</sup>|0.638|0.705|0.438|0.483|
||<br>BMF big m/v|0.499|0.590|0.580<sup>_∗_</sup>|0.602|0.669|0.417|0.468|0.555|0.596|0.607<sup>_∗_</sup>|0.631|0.702|0.432|0.480|
||||||||||**TBI**|||||||
||raw|0.406|0.751|1.029|1.271|1.482|||0.406|0.757|1.060|1.339|1.594|||
||SPF small m|0.133<sup>_∗∗_</sup>|0.534<sup>_∗∗_</sup>|0.848<sup>_∗∗_</sup>|1.114<sup>_∗∗_</sup>|1.362<sup>_∗∗_</sup>|||0.133<sup>_∗∗_</sup>|0.536<sup>_∗∗_</sup>|0.875<sup>_∗∗_</sup>|1.181<sup>_∗∗_</sup>|1.474<sup>_∗∗_</sup>|||
||SPF small m/v|0.132<sup>_∗∗_</sup>|0.503<sup>_∗∗_</sup>|0.823<sup>_∗∗_</sup>|1.099<sup>_∗∗_</sup>|1.345<sup>_∗∗_</sup>|||0.132<sup>_∗∗_</sup>|0.512<sup>_∗∗_</sup>|0.855<sup>_∗∗_</sup>|1.164<sup>_∗∗_</sup>|1.455<sup>_∗∗_</sup>|||
|RMSE|SPF big m|0.133<sup>_∗∗_</sup>|0.503<sup>_∗∗_</sup>|0.819<sup>_∗_</sup>|1.102<sup>_∗_</sup>|1.345<sup>_∗_</sup>|||0.133<sup>_∗∗_</sup>|0.521<sup>_∗∗_</sup>|0.851<sup>_∗∗_</sup>|1.156<sup>_∗∗_</sup>|1.433<sup>_∗∗_</sup>|||
||<br>SPF big m/v|0.134<sup>_∗∗_</sup>|0.507<sup>_∗∗_</sup>|0.826<sup>_∗∗_</sup>|1.098<sup>_∗∗_</sup>|1.338<sup>_∗_</sup>|||0.134<sup>_∗∗_</sup>|0.516<sup>_∗∗_</sup>|0.848<sup>_∗∗_</sup>|1.148<sup>_∗∗_</sup>|1.419<sup>_∗∗_</sup>|||
||<br>BMF small m|0.066<sup>_∗∗_</sup>|0.490<sup>_∗∗_</sup>|0.822<sup>_∗∗_</sup>|1.094<sup>_∗∗_</sup>|1.346<sup>_∗∗_</sup>|||**0.072**<sup>_∗∗_</sup>|0.480<sup>_∗∗_</sup>|0.820<sup>_∗∗_</sup>|1.132<sup>_∗∗_</sup>|1.428<sup>_∗∗_</sup>|||
||BMF small m/v|0.067<sup>_∗∗_</sup>|**0.453**<sup>_∗∗_</sup>|0.794<sup>_∗∗_</sup>|1.079<sup>_∗∗_</sup>|1.327<sup>_∗∗_</sup>|||0.073<sup>_∗∗_</sup>|**0.453**<sup>_∗∗_</sup>|**0.802**<sup>_∗∗_</sup>|**1.113**<sup>_∗∗_</sup>|1.406<sup>_∗∗_</sup>|||
||BMF big m|**0.066**<sup>_∗∗_</sup>|0.455<sup>_∗∗_</sup>|**0.772**<sup>_∗∗_</sup>|**1.052**<sup>_∗∗_</sup>|1.307<sup>_∗∗_</sup>|||0.073<sup>_∗∗_</sup>|0.485<sup>_∗∗_</sup>|0.803<sup>_∗∗_</sup>|1.122<sup>_∗∗_</sup>|1.420<sup>_∗∗_</sup>|||
||BMF big m/v|0.069<sup>_∗∗_</sup>|0.466<sup>_∗∗_</sup>|0.802<sup>_∗∗_</sup>|1.072<sup>_∗∗_</sup>|**1.300**<sup>_∗∗_</sup>|||0.080<sup>_∗∗_</sup>|0.472<sup>_∗∗_</sup>|0.818<sup>_∗∗_</sup>|1.124<sup>_∗∗_</sup>|**1.395**<sup>_∗∗_</sup>|||
||raw|0.214|0.414|0.586|0.743|0.887|||0.214|0.420|0.612|0.796|0.973|||
||SPF small m|0.149<sup>_∗∗_</sup>|0.326<sup>_∗∗_</sup>|0.498<sup>_∗∗_</sup>|0.658<sup>_∗∗_</sup>|0.813<sup>_∗∗_</sup>|||0.154<sup>_∗∗_</sup>|0.337<sup>_∗∗_</sup>|0.526<sup>_∗∗_</sup>|0.712<sup>_∗∗_</sup>|0.898<sup>_∗∗_</sup>|||
||SPF small m/v|0.068<sup>_∗∗_</sup>|0.267<sup>_∗∗_</sup>|0.459<sup>_∗∗_</sup>|0.636<sup>_∗∗_</sup>|0.797<sup>_∗∗_</sup>|||0.070<sup>_∗∗_</sup>|0.271<sup>_∗∗_</sup>|0.478<sup>_∗∗_</sup>|0.681<sup>_∗∗_</sup>|0.875<sup>_∗∗_</sup>|||
|CRPS|SPF big m|0.154<sup>_∗∗_</sup>|0.324<sup>_∗∗_</sup>|0.495<sup>_∗∗_</sup>|0.655<sup>_∗∗_</sup>|0.802<sup>_∗∗_</sup>|||0.158<sup>_∗∗_</sup>|0.336<sup>_∗∗_</sup>|0.519<sup>_∗∗_</sup>|0.697<sup>_∗∗_</sup>|0.871<sup>_∗∗_</sup>|||
||<br>SPF big m/v|0.071<sup>_∗∗_</sup>|0.270<sup>_∗∗_</sup>|0.464<sup>_∗∗_</sup>|0.635<sup>_∗∗_</sup>|0.790<sup>_∗∗_</sup>|||0.072<sup>_∗∗_</sup>|0.273<sup>_∗∗_</sup>|0.478<sup>_∗∗_</sup>|0.670<sup>_∗∗_</sup>|0.851<sup>_∗∗_</sup>|||
||<br>BMF small m|0.141<sup>_∗∗_</sup>|0.311<sup>_∗∗_</sup>|0.486<sup>_∗∗_</sup>|0.648<sup>_∗∗_</sup>|0.805<sup>_∗∗_</sup>|||0.148<sup>_∗∗_</sup>|0.321<sup>_∗∗_</sup>|0.506<sup>_∗∗_</sup>|0.690<sup>_∗∗_</sup>|0.875<sup>_∗∗_</sup>|||
||BMF small m/v|**0.040**<sup>_∗∗_</sup>|**0.238**<sup>_∗∗_</sup>|**0.436**<sup>_∗∗_</sup>|0.617<sup>_∗∗_</sup>|0.779<sup>_∗∗_</sup>|||**0.041**<sup>_∗∗_</sup>|**0.238**<sup>_∗∗_</sup>|**0.444**<sup>_∗∗_</sup>|**0.645**<sup>_∗∗_</sup>|0.840<sup>_∗∗_</sup>|||
||BMF big m|0.146<sup>_∗∗_</sup>|0.309<sup>_∗∗_</sup>|0.473<sup>_∗∗_</sup>|0.628<sup>_∗∗_</sup>|0.784<sup>_∗∗_</sup>|||0.158<sup>_∗∗_</sup>|0.327<sup>_∗∗_</sup>|0.502<sup>_∗∗_</sup>|0.678<sup>_∗∗_</sup>|0.864<sup>_∗∗_</sup>|||
||BMF big m/v|0.047<sup>_∗∗_</sup>|0.247<sup>_∗∗_</sup>|0.446<sup>_∗∗_</sup>|**0.616**<sup>_∗∗_</sup>|**0.767**<sup>_∗∗_</sup>|||0.048<sup>_∗∗_</sup>|0.246<sup>_∗∗_</sup>|0.460<sup>_∗∗_</sup>|0.652<sup>_∗∗_</sup>|**0.832**<sup>_∗∗_</sup>|||



Table 3: continued. 

## **5.3 Entropic tilting and nowcast uncertainty** 

Table 3 implies that tilting towards the nowcast mean _and variance_ consistently yields better CRPS scores than tilting towards the mean only. For _h_ = 1, this effect is simply a consequence of the nowcast distributions being more accurate than the BVAR ones, which is well known in the literature. Much more interestingly, the result also holds for _h ≥_ 2, which suggests that the “m/v” specification produces more favorable spillover effects on the horizons that are not directly affected by tilting. Table 4 investigates this result in more detail, by reporting the length and coverage of central prediction intervals obtained from both approaches (nominal level of 70%). In particular, we define length as the spread between the 15th and 85th percentiles of the forecast distribution and report the average length over time, and we measure coverage as the percent of actual outcomes of each variable falling within the 70% confidence band. 

For all variables and forecast horizons, we observe that the “m/v” specifications produce shorter prediction intervals than the “m” specifications, which implies sharper (i.e., more concentrated) forecast distributions. This result is natural: The SPF and model nowcasts generally have lower variance than the current quarter forecasts produced by the BVAR (see Section 5.1). While the “m/v” tilting variant imposes this information, the “m” variant fails to do so. Instead, it penalizes the (KLIC) distance from the BVAR distribution, and thus implicitly targets the BVAR variance.<sup>19</sup> These effects are clearest for the T-Bill and unemployment rates, where the “m/v” approaches produce prediction intervals whose average lengths (over time) are roughly 20-40 percent shorter than those of the “m” approaches. The differences are much smaller for GDP growth and inflation, where the average lengths of the prediction intervals typically differ by less than five percent. 

Naturally, the reduced length of the “m/v” prediction intervals comes along with reduced coverage rates compared to the “m” variants. For GDP, unemployment and inflation, the coverage rates of “m/v” are mostly still above 60 percent (recall that the nominal level is 70 percent). A similar statement holds for the T-Bill rate and _h ∈{_ 2 _,_ 3 _}_ . For the T-Bill rate and _h ∈{_ 4 _,_ 5 _}_ , the coverage rates of the “m” approaches are already well below 70 percent, with the rates of “m/v” being even lower. 

On balance, the increased sharpness of “m/v” appears to come at a small cost, in that the coverage rates are similarly close to (or far from) their nominal level as under the “m” approach. This assessment is consistent with the fact that the CRPS – which can be seen as a trade-off between sharpness and correct coverage, see e.g. Gneiting, Balabdaoui, and Raftery (2007) – consistently favors the “m/v” over the “m” approach. 

> 19This effect can be seen most clearly in the Gaussian example of Section 4.4, where the “m” approach corresponds to targeting the original (BVAR) variance. 

27 

||||_Pre_|_Crisis (8_|_8Q3 – 07_|_Q4)_|||_Comp_|_lete (88Q_|_3 – 13Q_|_2)_||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|_Horizon_||1|2|3|4|5|4*|5*|1<br>GDP|2|3|4|5|4*|5*|
||SPF m|0.846|0.705|0.718|0.718|0.718|0.667|0.641|0.870|0.700|0.700|0.700|0.660|0.640|0.560|
|Coverage|SPF m/v|0.731|0.679|0.692|0.718|0.718|0.628|0.641|0.710|0.680|0.680|0.700|0.660|0.590|0.560|
||BMF m|0.795|0.692|0.718|0.718|0.718|0.692|0.641|0.790|0.680|0.700|0.700|0.660|0.640|0.560|
||BMF m/v|0.705|0.692|0.692|0.705|0.705|0.667|0.641|0.710|0.680|0.680|0.690|0.650|0.610|0.560|
||SPF m|4.756|4.460|4.495|4.561|4.563|2.671|2.652|5.242|4.877|4.914|4.971|4.969|2.978|2.952|
|Length|SPF m/v|3.377|4.304|4.385|4.442|4.486|2.432|2.601|3.332|4.643|4.732|4.785|4.813|2.640|2.857|
||BMF m|4.577|4.437|4.458|4.528|4.538|2.630|2.634|4.927|4.812|4.844|4.899|4.907|2.913|2.919|
||BMF m/v|3.798|4.323|4.377|4.450|4.485|2.488|2.600|3.979|4.667|4.736|4.798|4.815|2.726|2.864|
||SPF m|0.924|1.131|1.122|1.162|1.143|0.722|0.831|0.966|1.315|1.358|1.423|1.409|0.928|1.124|
|CRPS|SPF m/v|**0.901**|**1.119**|**1.115**|1.156|1.145|**0.711**|0.825|**0.907**|**1.282**|**1.344**|1.414|1.408|**0.915**|**1.114**|
||BMF m<br>|0.972<br>|1.132<br>|1.128<br>|1.154<br>|**1.143**<br>|0.733<br>|0.829<br>|1.064<br>|1.335<br>|1.379<br>|1.419<br>|1.408<br>|0.989<br>|1.136<br>|
||BMF m/v|0.958|1.120|1.123|**1.150**|1.143|0.723|**0.824**|1.044|1.321|1.372|**1.413**|**1.406**|0.979|1.130|
||||||||||UNE|||||||
||SPF m|0.859|0.833|0.756|0.731|0.667|||0.860|0.820|0.750|0.710|0.650|||
|Coverage|SPF m/v|0.833|0.744|0.744|0.667|0.615|||0.750|0.710|0.730|0.660|0.600|||
||BMF m|0.987|0.923|0.872|0.808|0.744|||0.990|0.900|0.830|0.760|0.670|||
||BMF m/v|0.833|0.808|0.731|0.705|0.641|||0.830|0.750|0.720|0.680|0.590|||
||SPF m|0.389|0.623|0.818|0.977|1.090|||0.451|0.715|0.932|1.114|1.238|||
|Length|SPF m/v|0.260|0.499|0.708|0.881|1.016|||0.273|0.545|0.783|0.987|1.142|||
||BMF m|0.441|0.692|0.887|1.039|1.148|||0.505|0.786|1.004|1.179|1.312|||
||BMF m/v|0.237|0.488|0.703|0.885|1.023|||0.242|0.540|0.796|1.020|1.190|||
||SPF m|0.074|0.137|0.200|0.268|0.328|||0.087|0.178|0.280|0.396|0.512|||
|CRPS|SPF m/v|0.070|0.133|0.197|0.267|0.329|||0.083|0.176|0.276|0.392|0.507|||
||BMF m<br>|0.064<br>|0.122<br>|0.179<br>|0.241<br>|0.298<br>|||0.072<br>|0.147<br>|**0.241**<br>|0.359<br>|**0.479**<br>|||
||BMF m/v|**0.054**|**0.110**|**0.170**|**0.233**|**0.294**|||**0.054**|**0.137**|0.241|**0.358**|0.482|||
||||||||||INF|||||||
||SPF m<br>|0.769<br>|0.718<br>|0.744<br>|0.705<br>|0.718<br>|0.782<br>|0.756<br>|0.780<br>|0.740<br>|0.760<br>|0.720<br>|0.710<br>|0.820<br>|0.790<br>|
|Coverage|SPF m/v|0.718|0.679|0.731|0.692|0.705|0.795|0.744|0.700|0.710|0.750|0.710|0.690|0.830|0.780|
||BMF m|0679|0744|0718|0731|0731|0731|0756|0660|0730|0710|0740|0730|0760|0770|
||<br>BMF m/v|.<br>0.628|.<br>0.705|.<br>0.705|.<br>0.718|.<br>0.692|.<br>0.756|.<br>0.744|.<br>0.620|.<br>0.700|.<br>0.710|.<br>0.730|.<br>0.700|.<br>0.770|.<br>0.760|
||SPF m|1.885|2.078|2.242|2.403|2.581|1.681|1.899|2.029|2.239|2.421|2.594|2.782|1.822|2.054|
|Length|SPF m/v|1.603|1.993|2.170|2.340|2.510|1.566|1.824|1.670|2.126|2.322|2.502|2.682|1.664|1.951|
||BMF m|1.870|2.065|2.239|2.400|2.579|1.680|1.895|2.006|2.223|2.407|2.582|2.772|1.813|2.041|
||BMF m/v|1.742|2.030|2.208|2.376|2.555|1.635|1.869|1.830|2.168|2.358|2.539|2.729|1.739|1.993|
||SPF m<br>|0.443|0.534|0.541|0.579|0.653|0.374|0.440|0.470|0.541|0.565|0.602|0.676|0.379|0.445|
|CRPS|SPF m/v|**0.436**|**0.529**|**0.538**|**0.576**|**0.651**|**0.367**|**0.436**|**0.464**|**0.535**|**0.560**|**0.597**|**0.673**|**0.370**|**0.439**|
||BMF m|0.491|0.581|0.560|0.589|0.667|0.411|0.465|0.546|0.591|0.591|0.619|0.698|0.430|0.478|
||BMF m/v|0.495|0.584|0.561|0.588|0.667|0.413|0.465|0.553|0.593|0.592|0.618|0.698|0.431|0.477|
||||||||||TBI|||||||
||SPF m|0.962|0.795|0.628|0.564|0.474|||0.960|0.810|0.670|0.600|0.490|||
|Coverage|SPF m/v|0.795|0.692|0.551|0.449|0.423|||0.810|0.730|0.610|0.490|0.440|||
||BMF m|1000|0833|0667|0590|0526|||1000|0850|0700|0620|0540|||
||<br>BMF m/v|.<br>0.949|.<br>0.718|.<br>0.603|.<br>0.462|.<br>0.462|||.<br>0.940|.<br>0.760|.<br>0.640|.<br>0.500|.<br>0.460|||
||SPF m|0.956|1.300|1.555|1.797|1.994|||0.996|1.411|1.721|2.010|2.250|||
|Length|<br>SPF m/v|0.263|0.810|1.175|1.457|1.692|||0.299|0.887|1.298|1.627|1.897|||
||<br>BMF m|1003|1323|1562|1808|2007|||1037|1441|1742|2033|2272|||
||<br>BMF m/v|.<br>0.238|.<br>0.806|.<br>1.171|.<br>1.462|.<br>1.693|||.<br>0.241|.<br>0.859|.<br>1.280|.<br>1.617|.<br>1.889|||
||SPF m<br>|0.149|0.326|0.498|0.658|0.813|||0.154|0.337|0.526|0.712|0.898|||
|CRPS|SPF m/v<br>BMF|0.068<br>0141|0.267<br>0311|0.459<br>0486|0.636<br>0648|0.797<br>0805|||0.070<br>0148|0.271<br>0321|0.478<br>0506|0.681<br>0690|0.875<br>0875|||
||m<br>BMF m/v|.<br>**0.040**|.<br>**0.238**|.<br>**0.436**|.<br>**0.617**|.<br>**0.779**|||.<br>**0.041**|.<br>**0.238**|.<br>**0.444**|.<br>**0.645**|.<br>**0.840**|||



Table 4: **Impact of accounting for nowcast uncertainty.** “Coverage” and “Length” refer to central prediction intervals with a nominal level of 70 % (reported length is on average over time). “CRPS” reports the continuous ranked probability score (best = lowest number printed in bold). Note that the CRPS scores are identical to those in Table 3, and are reprinted here for ease of reference. 

# **6 Conclusion** 

This paper is concerned with the problem of combining forecasts from a BVAR with nowcasts from other sources. This combination problem is non-standard, in that the BVAR implies a joint forecast distribution for several forecast horizons, whereas the nowcast information is restricted to mean and variance predictions for the current quarter. We argue that entropic tilting is a powerful tool to tackle these challenges; unlike other methods proposed in the literature, it does not require restrictive assumptions such as joint normality of the VAR system or zero variance of the nowcast. 

In our empirical analysis, tilting systematically improves the accuracy of both point and density forecasts, and tilting the BVAR forecasts based on nowcast means and variances yields slightly greater gains in density accuracy than does just tilting based on the nowcast means. In a comparison of tilting on a variable-by-variable basis to tilting jointly toward the nowcasts for all four variables of the BVAR, we find that the overall differences in forecast performance for the joint treatment of variables versus the individual treatment of variables are small. 

29 

# **References** 

- ALTAVILLA, C., R. GIACOMINI, AND G. RAGUSA (2013): “Anchoring the Yield Curve Using Survey Expectations,” Working Paper, UC London. 

- ANG, A., G. BEKAERT, AND M. WEI (2007): “Do Macro Variables, Asset Markets, or Surveys Forecast Inflation Better?,” _Journal of Monetary Economics_ , 54, 1163 – 1212. 

- BANBURA, M., D. GIANNONE, M. MODUGNO, AND L. REICHLIN (2013): “Now-Casting and the Real-Time Data Flow,” in _Handbook of Economic Forecasting_ , ed. by G. Elliott, and A. Timmermann, vol. 2, pp. 195 – 237. Elsevier. 

- BANBURA, M., D. GIANNONE, AND L. REICHLIN (2013): “Nowcasting,” in _Oxford Handbook of Economic Forecasting_ , ed. by M. P. Clements, and D. F. Hendry, pp. 193 – 224. Oxford University Press. 

- BOMBERGER, W. A. (1996): “Disagreement as a Measure of Uncertainty,” _Journal of Money, Credit and Banking_ , 28, 381–392. 

- CARRIERO, A., T. E. CLARK, AND M. MARCELLINO (2014): “Real-Time Nowcasting with a Bayesian Mixed Frequency Model with Stochastic Volatility,” _Journal of the Royal Statistical Society: Series A_ , forthcoming. 

- CARTER, C. K., AND R. KOHN (1994): “On Gibbs Sampling for State Space Models,” _Biometrika_ , 81, 541–553. 

- CLARK, T. E. (2011): “Real-Time Density Forecasts From Bayesian Vector Autoregressions With Stochastic Volatility,” _Journal of Business & Economic Statistics_ , 29, 327–341. 

- CLARK, T. E., AND M. W. MCCRACKEN (2013): “Advances in Forecast Evaluation,” in _Handbook of Economic Forecasting_ , ed. by G. Elliott, and A. Timmermann, vol. 2, pp. 1107–1201. Elsevier. (2014): “Evaluating Conditional Forecasts from Vector Auturegressions,” Federal Reserve 

- Bank of Cleveland Working Paper 14-13. 

- CLARK, T. E., AND F. RAVAZZOLO (2014): “The Macroeconomic Forecasting Performance of Autoregressive Models with Alternative Specifications of Time-Varying Volatility,” _Journal of Applied Econometrics_ , forthcoming. 

- COGLEY, T., AND T. J. SARGENT (2005): “Drifts and Volatilities: Monetary Policies and Outcomes in the Post WWII US,” _Review of Economic Dynamics_ , 8, 262–302. 

- CROUSHORE, D. (2006): “Forecasting with Real-Time Macroeconomic Data,” _Handbook of Economic Forecasting_ , 1, 961–982. 

- D’AGOSTINO, A., L. GAMBETTI, AND D. GIANNONE (2013): “Macroeconomic Forecasting and Structural Change,” _Journal of Applied Econometrics_ , 28, 82–101. 

- DEL NEGRO, M., AND G. E. PRIMICERI (2014): “Time-Varying Structural Vector Autoregressions and Monetary Policy: A Corrigendum,” http://faculty.wcas.northwestern.edu/ ˜<sup>gep575/ErrataFinal2.pdf, Working Paper, Northwestern University, Accessed:2014-02-</sup> 13. 

30 

- DEL NEGRO, M., AND F. SCHORFHEIDE (2013): “DSGE Model-Based Forecasting,” in _Handbook of Economic Forecasting_ , ed. by G. Elliott, and A. Timmermann, vol. 2, pp. 57–140. Elsevier. 

- DIEBOLD, F. X., AND R. S. MARIANO (1995): “Comparing Predictive Accuracy,” _Journal of Business & Economic Statistics_ , 13, 253–263. 

- DOAN, T., R. LITTERMAN, AND C. SIMS (1984): “Forecasting and Conditional Projection using Realistic Prior Distributions,” _Econometric Reviews_ , 3, 1–100. 

- DURBIN, J., AND S. J. KOOPMAN (2002): “A Simple and Efficient Simulation Smoother for State Space Time Series Analysis,” _Biometrika_ , 89, 603–616. 

- FAUST, J., AND J. H. WRIGHT (2009): “Comparing Greenbook and Reduced Form Forecasts Using a Large Realtime Dataset,” _Journal of Business & Economic Statistics_ , 27, 468–479. (2013): “Forecasting Inflation,” in _Handbook of Economic Forecasting_ , ed. by G. Elliott, and 

- A. Timmermann, vol. 2, pp. 2–56. Elsevier. 

- FREY, C., AND F. MOKINSKI (2014): “Forecasting with Bayesian Vector Autoregressions Estimated Using Professional Forecasts,” Working Paper, University of Konstanz. 

- GEWEKE, J., AND G. AMISANO (2011): “Optimal Prediction Pools,” _Journal of Econometrics_ , 164, 130–141. 

- GIACOMINI, R., AND H. WHITE (2006): “Tests of Conditional Predictive Ability,” _Econometrica_ , 74, 1545–1578. 

- GIANNONE, D., F. MONTI, AND L. REICHLIN (2014): “Exploiting the Monthly Data-flow in Structural Forecasting,” Centre for Macroeconomics (CFM) Working Paper 1416. 

- GNEITING, T., F. BALABDAOUI, AND A. E. RAFTERY (2007): “Probabilistic Forecasts, Calibration and Sharpness,” _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , 69, 243– 268. 

- GNEITING, T., AND A. E. RAFTERY (2007): “Strictly Proper Scoring Rules, Prediction, and Estimation,” _Journal of the American Statistical Association_ , 102, 359–378. 

- GNEITING, T., AND R. RANJAN (2011): “Comparing Density Forecasts using Threshold-and Quantile-weighted Scoring Rules,” _Journal of Business & Economic Statistics_ , 29. 

- HALL, S. G., AND J. MITCHELL (2007): “Combining Density Forecasts,” _International Journal of Forecasting_ , 23, 1–13. 

- HARVEY, D., S. LEYBOURNE, AND P. NEWBOLD (1997): “Testing the Equality of Prediction Mean Squared Errors,” _International Journal of Forecasting_ , 13, 281–291. 

- HERSBACH, H. (2000): “Decomposition of the Continuous Ranked Probability Score for Ensemble Prediction Systems,” _Weather and Forecasting_ , 15, 559–570. 

- KIM, S., N. SHEPHARD, AND S. CHIB (1998): “Stochastic Volatility: Likelihood Inference and Comparison with ARCH Models,” _The Review of Economic Studies_ , 65, 361–393. 

- LEWIS, K. F., AND C. H. WHITEMAN (2014): “Empirical Bayesian Density Forecasting in Iowa and Shrinkage for the Monte Carlo Era,” _Journal of Forecasting_ , forthcoming. 

31 

- LITTERMAN, R. B. (1986): “Forecasting with Bayesian Vector Autoregressions – Five Years of Experience,” _Journal of Business & Economic Statistics_ , 4, 25–38. 

- MONTGOMERY, A. L., V. ZARNOWITZ, R. S. TSAY, AND G. C. TIAO (1998): “Forecasting the US Unemployment Rate,” _Journal of the American Statistical Association_ , 93, 478–493. 

- MONTI, F. (2010): “Combining Judgment and Models,” _Journal of Money, Credit and Banking_ , 42, 1641–1662. 

- NEWEY, W. K., AND K. D. WEST (1987): “A Simple, Positive Semi-Definite, Heteroscedasticity and Autocorrelation Consistent Covariance Matrix,” _Econometrica_ , 55, 703–708. 

- NEWEY, W. K., AND K. D. WEST (1994): “Automatic Lag Selection in Covariance Matrix Estimation,” _The Review of Economic Studies_ , 61, 631–653. 

- OMORI, Y., S. CHIB, N. SHEPHARD, AND J. NAKAJIMA (2007): “Stochastic Volatility with Leverage: Fast and Efficient Likelihood Inference,” _Journal of Econometrics_ , 140, 425–449. 

- PRIMICERI, G. E. (2005): “Time Varying Structural Vector Autoregressions and Monetary Policy,” _The Review of Economic Studies_ , 72, 821–852. 

- R CORE TEAM (2014): _R: A Language and Environment for Statistical Computing,_ R Foundation for Statistical Computing, Vienna, Austria. 

- ROBERTSON, J. C., E. W. TALLMAN, AND C. H. WHITEMAN (2005): “Forecasting Using Relative Entropy,” _Journal of Money, Credit and Banking_ , 37, 383–401. 

- ROMER, C. D., AND D. H. ROMER (2000): “Federal Reserve Information and the Behavior of Interest Rates,” _American Economic Review_ , 90, 429–457. 

- SCHORFHEIDE, F., AND D. SONG (2013): “Real-Time Forecasting with a Mixed-Frequency VAR,” _Journal of Business & Economic Statistics_ , forthcoming. 

- SIMS, C. A. (2002): “The Role of Models and Probabilities in the Monetary Policy Process,” _Brookings Papers on Economic Activity_ , 2002, 1–40. 

- SMETS, F., A. WARNE, AND R. WOUTERS (2014): “Professional Forecasters and Real-Time Forecasting with a DSGE Model,” _International Journal of Forecasting_ , 30, 981–995. 

- WEST, K. D. (1996): “Asymptotic Inference about Predictive Ability,” _Econometrica_ , 64, 1067–1084. 

- WOLTERS, M. H. (2014): “Evaluating Point and Density Forecasts of DSGE Models,” _Journal of Applied Econometrics_ , forthcoming. 

- WRIGHT, J. H. (2013): “Evaluating Real-Time Forecasts with an Informative Democratic Prior,” _Journal of Applied Econometrics_ , 28, 762–776. 

- ZEILEIS, A. (2004): “Econometric Computing with HC and HAC Covariance Matrix Estimators,” _Journal of Statistical Software_ , 11, 1–17. 

32 

# **Appendix** 

This appendix presents a simple demonstration of the equivalence between (1) Gaussian conditional forecasting with no uncertainty around the nowcast and (2) the Faust and Wright (2009) approach, and details the priors and algorithms used in estimation of the BVAR models and other nowcasting models. 

# **A Example to establish equivalence of data augmentation to conditional forecasting** 

As mentioned in the text, the data augmentation technique of Faust and Wright (2009) simply appends the nowcast to the data. Here we provide an example to demonstrate that this method is equivalent to Gaussian conditional forecasting with no uncertainty around the nowcast (so Ω11 = 0; see Section 4.4). To this end, suppose _yt_ follows an AR(1) process, and we use it to forecast _h ≥_ 2 steps ahead, with a one-step nowcast of value _µ_ 1. The model is 



## **A.1 Unconditional forecast without nowcast information** 

The usual _h_ step ahead forecast for _yt_ + _h_ is 



where the superscript _u_ stands for “unconditional” (i.e., no nowcast information). The corresponding forecast error is 



and has variance 



Furthermore, the predicted covariance between the 1-step and _h_ -step ahead forecast errors is given by 



33 

## **A.2 Data augmentation approach to incorporating nowcast** 

Under the data augmentation approach, the nowcast of _µ_ 1 is treated as data for period _t_ + 1, and we form the forecast for period _t_ + _h_ as an ( _h −_ 1)-step ahead forecast using the pseudo-data for _t_ + 1. In this case, using a superscript _a_ to denote the data augmentation approach, we obtain a forecast for _yt_ + _h_ of: 



With the nowcast treated as data for period _t_ + 1, the forecast error variance for period _t_ + _h_ is defined as just the ( _h −_ 1)-step ahead error variance, which is given by 



## **A.3 Conditional forecast approach to incorporating nowcast** 

Under the Gaussian conditional forecasting approach, the forecast for period _t_ + _h_ is formed under the condition that _yt_ +1 take the nowcast value of _µ_ 1. Using the more general conditional forecast solution given in Section 4.4, as well as the unconditional forecast quantities derived above, the point forecast is given by 



Given the nowcast condition on _yt_ +1 (without uncertainty around it, so Ω11 = 0), the general solution in Section 4.4 yields a conditional forecast error variance as follows: 



Accordingly, in this simple example, it follows that the data augmentation and conditional forecast approaches to combining a nowcast with another forecast yield the same forecasts, as long as the conditional forecast is implemented assuming a zero variance around the nowcast. 

34 

# **B Prior for BVARs with stochastic volatility** 

We describe in this section the priors used with the BVAR-SV models to produce quarterly forecasts of the variables of interest and nowcasts of unemployment and the T-bill rate. 

For the VAR coefficients, we use a conventional Minnesota prior, without cross-variable shrinkage (note that _i_ and _j_ refer to the row and column of _Bl_ ): 





Following common settings, we set _θ_ = 0.2, _ε_ = 1000, and the scale parameters _σi_<sup>2atestimatesof</sup> residual variances from AR( _p_ ) models from the estimation sample. With all of the variables of our VAR models defined so that they should be stationary, we set the prior mean of all the VAR 

In the prior for the volatility-related components of the model, we use an approach to setting them similar to that of such studies as Cogley and Sargent (2005), Primiceri (2005) and Clark (2011). The prior for _A_ is uninformative, with a mean and variance for each row vector of _<u>µ</u>_ _~~a~~ ,i_<sup>=</sup> 0 _,_ <u>Ω</u> _~~a~~ ,i_<sup>= 10002</sup><sup>_· Ii−_1,</sup><sup>_i_= 2</sup><sup>_, . . . , k_.We make the priors on the volatility-related parameters loosely</sup> informative. The prior for Φ is inverted Wishart, with mean of 0 _._ 01 _× Ik_ and _k_ + 1 degrees of freedom. For the initial value of the log volatility of each equation _i_ , we use a mean of log _λ_<sup>ˆ</sup> _i,_ 0 _,OLS_ and variance of 4. To obtain log _λ_<sup>ˆ</sup> _i,_ 0 _,OLS_ , we use the residuals from AR( _p_ ) models estimated over a training sample preceding the estimation sample. For each _j_ = 2 _, . . . , k_ , we regress the residual from the AR model for _j_ on the residuals associated with variables 1 through _j −_ 1 and compute the error variance _σ_ ˆ _i,_<sup>2</sup> 0<sup>.We set the prior mean of log volatility in period 0 at log ˆ</sup><sup>_λi,_0</sup><sup>_,OLS_=log ˆ</sup><sup>_σ_</sup> _i,_<sup>2</sup> 0<sup>.</sup> For the quarterly model and the unemployment nowcasting model, the training sample is 1949-54; for the T-bill nowcasting model, the training sample is 1959-63. For the quarterly model and the unemployment nowcasting model, because a handful of the data vintages do not start until later than most others, we use the same prior mean on initial volatility for all vintages (forecast origins), computed using the last available vintage of data. 

35 

# **C Prior for Bayesian mixed frequency models** 

We describe in this section the priors used for mixed frequency nowcasting models for GDP growth and inflation. Since the form of the prior is not dependent on the month timing _m_ , in spelling out the prior we drop the index _m_ from the model parameters for notational simplicity. 

In all cases, for the coefficient vector _β_ , we use a prior distribution that is normal, with mean 0 (for all coefficients) and variance that takes a diagonal, Minnesota-style form. The prior variance is Minnesota style in the sense that shrinkage increases with the lag (with the quarter, not with the month within the quarter), and in the sense that we impose more shrinkage on the monthly predictors than on lags of GDP growth or inflation. The shrinkage is controlled by three hyperparameters (in all cases, a smaller number means more shrinkage): _λ_ 1, which controls the overall rate of shrinkage; _λ_ 2, which controls the rate of shrinkage on variables relative to GDP or GDP inflation; and _λ_ 3, which determines the rate of shrinkage associated with longer lags. 

At each forecast origin, the prior standard deviation associated with the coefficient on variable _xi,j,t−l_ of _Xt_ , where _i_ denotes the indicator (employment, etc.), _j_ denotes the month within which the quarter at which the indicator has been sampled, and _l_ denotes the lag in quarters (while we only consider a lag of 1 in this paper, Carriero, Clark, and Marcellino (2014) include results for models with a lag of 2), is specified as follows: 



For coefficients on lag _l_ of y, the prior standard deviation is 



Finally, for the intercept, the prior is uninformative: 



In setting these components of the prior, for _σy_ and _σi,j_ we use standard deviations from AR(4) models for GDP growth or inflation and _xi,j,t_ estimated with the available sample of data. 

In all of our results, the hyperparameters are set at values that may be considered very common in Minnesota-type priors (e.g. Litterman, 1986): _λ_ 1 = 0 _._ 2, _λ_ 2 = 0 _._ 2, and _λ_ 3 = 1. 

Finally, in the prior for the volatility-related components of the model, our approach is similar to that used in such studies as Cogley and Sargent (2005), Primiceri (2005) and Clark (2011). For 

36 

the prior on _φ_ , we use a mean of 0.035 and 5 degrees of freedom. For the period 0 value of volatility of each equation _i_ , we use a prior of 



To obtain log _λ_<sup>ˆ</sup> 0 _,OLS_ , we use a training sample of 40 observations preceding the estimation sample to fit an AR(4) model to GDP growth or inflation. 

# **D Algorithm for BVAR with stochastic volatility** 

We estimate the BVAR-SV model with a five-step Gibbs sampling algorithm. Let _Xt_ denote the collection of right-hand side variables of each equation of the VAR and _B_ denote the vector of the system of VAR coefficients contained in _Bi, i_ = 0 _, . . . , p_ , as defined in the paper’s equation (1). go here 

Step 1: Draw the VAR coefficients _B_ conditional on the history of Λ _t_ , _A_ , and Φ. 

The vector of coefficients is sampled from a conditional posterior distribution that is multivariate normal with mean _µ_ ¯ _B_ and variance Ω<sup>¯</sup> _B_ , based on prior mean _<u>µ</u>_ _~~B~~_<sup>andvariance</sup><sup><u>Ω</u></sup> _~~B~~_<sup>.Letting</sup> Σ _t_ = _A_<sup>_−_1</sup> Λ _tA_<sup>_−_1</sup><sup>_′_</sup> , the posterior mean and variance are: 



Step 2: Draw the elements of _A_ conditional on _B_ , the history of Λ _t_ , and Φ. 

Following Cogley and Sargent (2005), rewrite the VAR as 



ˆ where, conditional on _B_ , _yt_ is observable. This system simplifies to a set of _i_ = 2 _, . . . , k_ equaˆ tions, with equation _i_ having as dependent variable _yi,t_ and as independent variables _−_ 1 _·_ ˆ _yj,t, j_ = 1 _, . . . . , i −_ 1, with coefficients _aij_ . Multiplying equation _i_ by _λ_<sup>_−_</sup> _i,t_<sup>0</sup><sup>_._5</sup> eliminates the heteroskedasticity associated with stochastic volatility. Then, proceeding separately for each transformed equation _i_ , draw the _i_ ’th equation’s vector of coefficients _ai_ (a vector containing _aij_ for _j_ = 1 _, . . . , i −_ 1) from 

37 

a normal posterior distribution with the mean and variance implied by the posterior mean and variance computed in the usual way. See Cogley and Sargent (2005) for details. 

Step 3: Draw the elements of the states for the mixture distribution used to approximate the _χ_<sup>2</sup> distribution under the Kim, Shephard, and Chib (1998) algorithm, conditional on _B_ , _A_ , the history of Λ _t_ , and Φ. 

See Primiceri (2005) for details. However, we depart from Primiceri by using a 10 state approximation of the _χ_<sup>2</sup> distribution from Omori, Chib, Shephard, and Nakajima (2007) instead of the 7-state approximation from Kim, Shephard, and Chib (1998). 

Step 4: Draw the elements of the variance matrix Λ _t_ conditional on _B_ , _A_ , Φ, and the mixture states. 

Following Primiceri (2005), the VAR can be rewritten as 



where _ϵt ∼ N_ (0 _, Ik_ ). Taking logs of the squares yields 



The conditional volatility process is 



The estimation of the time series of _λ_<sup>2</sup> _i,t_<sup>uses the vector of the measured log ˜</sup><sup>_y_</sup> _i,t_<sup>2and Primiceri’s ver-</sup> sion of the Kim, Shephard, and Chib (1998) algorithm; see Primiceri for further detail (we depart from his implementation by using the Durbin and Koopman (2002) simulation smoother instead of the one proposed by Carter and Kohn (1994)). 

Step 5: Draw the variance matrix Φ, conditional on _B_ , the history of Λ _t_ , and _A_ . 

Following Primiceri (2005), the sampling of Φ, the variance of innovations to the log variances, is based on inverse Wishart priors and posteriors. The scale matrix of the posterior distribution is the sum of the prior mean _×_ the prior degrees of freedom and<sup>�</sup><sup>_T_</sup> _t_ =1<sup>_ν_ˆ</sup><sup>_tν_ˆ</sup> _t_<sup>_′_,where</sup><sup>_ν_ˆ</sup><sup>_t_denotes the</sup> vector of innovations to the posterior draw of the volatilities for the set of variables. 

38 

# **E Algorithm for Bayesian mixed frequency model** 

The mixed frequency nowcasting model with stochastic volatility is estimated with a Metropoliswithin-Gibbs algorithm, used in such studies as Clark (2011) and Carriero, Clark, and Marcellino (2014). The posterior mean and variance of the coefficient vector are given by 



where we again omit the _m_ index from the parameters for notational simplicity. 

39 

