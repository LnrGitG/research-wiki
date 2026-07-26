---
title: **Forecasting the U.S. House Prices Bottom: A Bayesian FA-VAR Approach**
type: paper
source_pdf: raw/papers/Vitner. Forecasting_the_U_S_House_Prices_Bottom.pdf
converted: 2026-07-26
---

# **Forecasting the U.S. House Prices Bottom: A Bayesian FA-VAR Approach** 

#### **Mark Vitner and Azhar Iqbal**<sup>**1**</sup> 

#### **Abstract** 

We project the peak-to-trough decline in home prices utilizing the three most popular measures of house prices, which are: (1) the FHFA (formally OFHEO) Index of house values; (2) the FHFA Purchase Only Index; (3)the S&P/Case-Shiller Index of house prices. We utilize six different models to project changes in home prices, including AR, ARIMA, BVAR-level, BVARdifference, BVECM, and Bayesian FA-VAR. The Bayesian FA-VAR outperforms other models in term of simulated out-of-sample root mean square error (RMSE) criteria. 

The most important and useful findings of the study, especially for policy makers and investors, are the following; (1) we are projecting for house prices to bottom out in 2010:2Q when using the FHFA Index and forecast a 8.70% drop from its 2007:2Q peak to is 2010:2Q trough; (2) the FHFA Purchase Only Index bottoms out in 2010:2Q following a 12.24% peak-to-trough decline, with the peak again in 2007:2Q; (3) the S&P/Case-Shiller Index is expected to drop 32.85% from its 2006:2Q peak to its 2010:1Q trough. 

These three indexes measure house prices quite differently. For instance, the S&P/Case-Shiller house price index includes foreclosed houses and shows a much larger decline in national house prices, while the FHFA indexes exclude foreclosed houses and shows somewhat smaller declines. As a result, we produce two different dates for house prices to bottom out. However, all three indexes produce similar results, suggesting we will see house prices bottom next year (2010) and a very slow U-shaped recovery. Both 2009 and early 2010 will be a very difficult time for the housing industry and homeowners in general. Another important concluding remark from our empirical analysis is that while the housing sector was the root cause of the financial crisis and subsequent recession, we do not expect housing to lead the economy out of recession or to restore financial stability.  The combination of a sharp drop in home prices, dramatic loss of wealth, tightening credit conditions, and projected slow recovery in house prices, will likely mean the subsequent recovery in home sales and home construction will be too modest to drive the overall economy.  While a bottoming out in home prices may be the key to ending the financial crisis, it will not likely spark a strong and sustainable recovery. 

**Keywords** : House Prices Bottom; Dynamic Factor Model; Bayesian FA-VAR. 

#### **JEL Classification** : C32; C53; E37. 

> 1 Mark Vitner; Senior Economist and Managing Director, Wells Fargo Securities, LLC. Email: <u>mark.vitner@wachovia.com. Azhar Iqbal; Econometrician, Wells Fargo Securities, LLC. Email: azhar.iqbal@wachovia.com. The views expressed in this study are those of the authors. Neither Wells</u> Fargo Corporation nor its subsidiaries is responsible for the contents of this article. 

# **Forecasting the U.S. House Prices Bottom: A Bayesian FA-VAR Approach** 

#### **Version of November 25, 2009** 

## **_Introduction_** 

The housing boom and subsequent bust is the underlying root cause of both the financial crisis and recession. While significant contractions in the home prices and residential construction have occurred in several previous recessions during the past 60 years, the current recession is the only one where home prices and construction peaked so many quarters before the overall economy.  Most previous cycles saw housing fall at or around the same time as the rest of the economy. 

The plunge in home prices led to turmoil in the financial markets.  The 1998-2005 boom in home prices accelerated the development of a multitude of financial products to leverage the $13 trillion home mortgage market.  Once prices began falling, a negative feedback loop took hold, with home falling prices triggering delinquencies and defaults on home mortgages, which in turn have produced massive losses in the residential mortgage market and the chain of securities, derivative products and off-balance sheet investment vehicles tied to these products.  The resulting opacity in losses and potential losses resulted in a drying up of capital for a whole host of financial institutions. 

Mortgage-related loses were clearly at the center of the financial storm and played a critical role in the both the collapse of Bear Sterns and Lehman Brothers. Other investment houses and banking companies also suffered losses and many were unable to raise new equity or debt capital, which required several unprecedented moves by the Treasury and Federal Reserve to directly bolster capital and improve these firms’ access to the private-sector debt and equity markets. 

Investors’ reluctance to pour more money into these firms is understandable given the lack of transparency on the core issue behind most of these losses, which is what will happen to home prices and the value of assets tied to them? A reliable forecast of housing prices would provide some needed benchmarks to gauge the potential depth of mortgage related losses and provide some idea of when a recovery will begin. 

In addition to the impact on the credit markets, the housing bust also directly impacted overall economic conditions.  Sales of new homes plummeted 73 percent between their peak in July 2005 and the end of 2008. Sale of existing homes also declined sharply, falling 34 percent over this time period.  Residential construction also tumbled, falling by $350 billion from the beginning of 2006 to the fall 2008. Declines in home sales and residential construction also impacted everything remotely tied to housing, including 

2 

producers and distributors of building materials and anything else that ultimately went into house. In addition, the loss of wealth both directly to falling home prices and indirectly through the resulting stock market losses have severely cut into consumer spending. Output and employment plunged during the later part of 2008 and heavy job losses carried over into the early part of 2009. Fortunately, the federal government has stepped in, offering institutions about $1.1 trillion in liquidity and hundreds of billions of dollar in new capital. Given these remarkable steps, credit markets are beginning to thaw. 

Hall and Woodward (2009) suggested that financial crises unleashed by falling home prices could only be ultimately relieved by aggressive monetary and fiscal policy actions. The Obama administration signed a $787 billion stimulus package in early February 2009 that includes some provisions to promote home ownership. 

Given the central role home prices have played in the financial crisis and recession, the most critical question today is how far house prices will fall and when will house prices bottom out? The answer to this trillion dollar question is a difficult task because the current housing slump is without precedent, both in terms of breadth and magnitude. Many economists have been debating when the bottom in house prices will occur; some have suggested we might already be at the bottom of house prices at the time of this writing. Given the plethora of forecasts today, it is often unclear how many of these forecasts are being made. 

After the seminal work of Sims (1980), Vector Autoregressions (VAR) became a major tool for macroeconomic forecasting. Despite its success, however, there is a technical problem with VAR. Vector Autoregressions can only utilize a small subset of available information due to degree of freedom problem, also known as the ‘curse of dimensionality’. However, Litterman (1980) presented the Bayesian Vector Autoregression (BVAR) approach to address this problem (see Doan et al. (1984), Todd (1984), and Litterman (1986) for more detail). 

The BVAR approach is more flexible than the VAR approach and also far more information to be included. Litterman (1986) showed that his approach is as accurate, on average, as those used by the best known commercial forecasting services (DRI, Chase, and Wharton Econometrics at that time). Theoretically, recent literature shows significant development with BVAR (examples include Sims and Zha (1998), Waggoner and Zha (1999)). Empirically, however, improvement on Litterman’s original methodology does not seem particularly significant (see Robertson and Tallman (1999)). 

The performance of Litterman’s method is at least partially determined by the choice of several parameters, it is popularly referred to as the ‘Minnesota Prior’. Litterman was only able to implement a small number of the multitude of possible parameter combinations due to limited and expensive computer power at that time. With the programming flexibility and speed available with SAS, we can run Litterman’s regression using many parameter combinations and find the best possible combination; see the next section for more detail. This is one of the major advantages of our implementation. 

3 

There are few potential issues with BVAR and those are non-stationary and potential cointegration relationship, see section 2.1 for more detail. We kept all these possibilities in mind and followed three different BVAR approaches: (1) Estimate the BVAR using the level form of the series and generate forecasts that are labeled BVAR-level; (2) we use the first difference form of the series and apply BVAR and call it BVAR-difference; (3) we apply the co-integration approach on the model and then apply Bayesian vector error correction model (BVECM) and generate the forecasts. 

It always has been a difficult task for a researcher to filter through masses of data and find the most useful and best predictors. A small number of variables is essential, however, as including too many variables in a traditional econometric modeling framework creates over-fitting and/or degree of freedom issues— the so-called ‘curse of dimensionality’ problem. However, due to advancement in computer and database capabilities combined with econometric/statistical software, like SAS, we can analyze each variable from a large data set of more than 300 data series and select a reasonable amount of variables based on some statistical criterion. We follow a step-wise procedure and select a handful of predictors, seven variables, from a data set of more than 300 variables, see section 3 for more detail. 

Despite the success of VAR/BVAR methodology, the process generally limits the analysis to eight variables or fewer.<sup>2</sup> Of course, it is almost always better to have more information and today such information is available at little to no cost. In addition, the increased power of personal computers has facilitated in creating econometric models with huge amounts of information. Indeed, recent econometric analyses have confirmed the longstanding view of professional forecasters, that the use of large number of data series may significantly improve forecasts of key macroeconomic variables (Stock and Watson, 1999, 2002, 2005; Watson 2000; Bernanke and Boivin, 2003, and Bernanke et al. 2005). Dynamic factor models (DFM) can handle a large amount of information, without facing the degrees of freedom problem, leading to a more accurate forecast result. Stock and Watson (2005) said that the DFM transforms the ‘curse of dimensionality’ into the ‘blessing of dimensionality’. 

The original DFM models of Sargent and Sims (1977), Geweke (1977), Chamberlain (1983) and Chamberlain and Rothschild (1983) have improved recently through advances in estimation techniques proposed by Stock and Watson (1999, 2002, 2005), Bernanke and Boivin (2003), Bernanke et al. (2005), Bai and Ng (2002), Forni et al. (2005), and Kapetanios and Marcellino (2003)<sup>3</sup> . Several empirical researchers provide evidence of improvement in forecasting performance of macroeconomic variables using factor analysis (Giannone and Matheson 2007; Cristadore et al. 2005; Forni et al. 2005; 

> 2 See Christiano et al. (2000) for a survey of VAR literature. Leeper et al. (1996) are able to increase the number of variables analyzed through the use of Bayesian priors, but their VAR systems still typically contain fewer than 20 variables. 

> 3 Recently, another approach to resolving the curse of dimensionality has been explored in the context of Bayesian regression by De Mol et al (2008). Which method is more powerful? We leave this question for future research and used Stock and Watson (2002) approach for our study. 

4 

Schneider and Spitzer 2004; Forni et al. 2001; Stock and Watson 1999, 2002; Bernanke and Boivin 2003; Bernanke et al. 2005; Boivin and Giannoni 2008). 

The fundamental assumption of the DFM approach is that each economic variable can be decomposed into a common factor component plus an idiosyncratic component. The common component is driven by a few dynamic factors (far less than the number of available economic variables) underlying the whole economy. Stock and Watson (2002) showed that, with reasonable assumptions, principal component analysis (PCA) can be used to estimate these components consistently. Factors estimated by PCA have been proved successful in forecasting individual economic series such as Industrial Production, Retail Sales, Employment, and Inflation (Stock and Watson 1999, 2002, and Bernanke and Boivin 2003). Given that the DFM has an excellent track record of forecasting, it should help us forecast where house prices will bottom out in this cycle. We first follow the Stock and Watson (2002) and Bai and Ng (2002) approach and use PCA to estimate several common components from a large data set of 141 economic variables. We then put these common components into BVAR framework, and call it Bayesian FA-VAR, to find the best specification.<sup>4</sup> 

We used three most popular measures of house prices which are: (1) FHFA (formally OFHEO) Index of house values; (2) FHFA Purchase Only Index; (3) S&P/Case-Shiller 10-City Index of house prices.<sup>5</sup> We used six different models including AR, ARIMA, BVAR-level, BVAR-difference, BVECM, and Bayesian FA-VAR. The Bayesian FAVAR outperforms other models in term of simulated real time out-of-sample root mean square error (RMSE) criteria. Our forecasting methodology is as follow; we assume we are standing at 2001:4Q; we have quarterly data set for 1987:1Q to 2001:4Q, and ran all six models and generated forecasts for next 12 quarters.  We then advance one quarter ahead (now we have a data set for 1987:1Q to 2002:1Q) and reran the models and generate forecasts for next 12 quarters.  We repeat this process until we reach the latest available data point, which currently is 2008:3Q. Then we calculate RMSE for all models and found that the Bayesian FA-VAR has the smallest forecast error/RMSE.<sup>6</sup> 

The superior performance of the Bayesian FA-VAR is a reconfirmation of the superiority of the DFM approach and is consistent with the findings of Stock and Watson (1999, 2002) and Bernanke and Boivin (2003) and many others. The other most important and useful findings of the study, especially for policy makers and investors, are the following; (1) we are projecting house prices bottom as measured by the FHFA Index in 2010:2Q and are forecasting 8.7% peak (2007: 2Q) to trough (2010:2Q) decline; (2) house prices as measured by the FHFA Purchase Only Index will bottom out in 2010:2Q, with a 12.24% peak (2007:2Q) to trough (2010:2Q) decline; (3) and home prices as measured by the S&P/Case-Shiller Index are expected to drop by 32.85% from peak (2006:2Q) to trough (2010:1Q). 

> 4 Bernanke and Boivin (2003) used factors in a VAR framework but they suggested that forecasting performance may improved by using Bayesian priors. See next section for more detail. 

> 5 There is another index too; NAR Index of Median Prices, but we didn’t include it into our analysis. See the data and implementing strategy for more detail. 

> 6 See forecast evaluation and results section for further explanation of this methodology. 

5 

Since these three indexes are different measures of house prices, for instance, the S&P/Case-Shiller 10-city house price index includes foreclosed houses and shows a tremendous decline in national house prices, while FHFA index of house prices excludes foreclosed houses and shows a much smaller decline, we have three different dates for house prices bottom.<sup>7</sup> All three home price indexes share essentially the same conclusion. On average, we will see home prices bottom out next year (2010) and the recovery will likely be very slow, following a ‘U’ shape pattern. Overall 2009 and early 2010 will be a very challenging time for the housing industry and homeowners in general. 

Another important concluding remark from our empirical analysis is that while the housing sector was the root cause of the financial turmoil and ultimately the recession, we do not expect housing will lead the overall economy or financial markets into recovery. The sheer magnitude of the rise and fall in housing prices has caused extensive damage to the homebuilding industry and the financial infrastructure that supports it. Given the magnitude and depth of the decline in housing prices, a recovery will likely take several years to take hold, even with assistance from numerous federal programs. One important issue we would like to share here that is the effect of current stimulus package and Fed as well as U.S. Treasury effort to jump-start the economy and restore the financial sector confidence. These efforts may help during the recovery period but we do not expect a significant change in our conclusion. 

The rest of the paper is organized as follows. Section 2 sets up the econometrics of the BVAR and the Bayesian FA-VAR. The data and implementation of the BVAR and Bayesian FA-VAR is outlined in section 3. Empirical results and caveats are discussed in section 4 and section 5, respectively. Concluding remarks are provided in section 6. 

## **_2. The Econometric Methodology_** 

In this section we discuss our econometric methodology. We utilize both univariate and multivariate approaches of forecasting.  In the case of the univariate approach we follow an Autoregressive model (AR). The simplest form of the model can be a AR(1) model and in this case the current value of a dependent variable , Yt, is depend on it previous value, lag of Yt (Yt-1), and a error term. In addition, we assume that the error term is white noise. The next step in the univariate case is called an Autoregressive Integrated Moving Averages (ARIMA). We used ARIMA (1, 1, 1), where our dependent variable, Yt, has integrated of order 1(containing unit root) and error term has a moving average representation of order 1, MA (1).<sup>8</sup> We used AR (1) as well as ARIMA (1, 1, 1) models and generated out-of-sample forecasts up to 12 quarters ahead followed by the recursive method described in section 2.4. We then calculated the out-of-sample root mean square error (RMSE) for each period. Now we step ahead and discuss our next method of forecasting that is Bayesian VAR. 

> 7 We discussed these issues in more detail in the data section. 

> 8  For further detail about AR (p) as well as ARIMA (p, d, q) please see any standard Time Series econometrics or _Elements of Forecasting_ by Francis X. Diebold, 4<sup>th</sup> Edition, 2007. 

6 

### **2.1 The Bayesian Vector Autoregression Model** 

The Bayesian Vector Autoregression (BVAR) model is the extension of the Vector Autoregression (VAR) model therefore we start our discussion with the VAR approach. In addition, we highlight issues related with the Sims (1980) VAR approach and benefits of the Litterman (1980, 1986) BVAR model. 

Let Yt= (Y1t, Y2t, Y3t,……, Ynt) is a set of time series and the VAR (P) representation of these time series can be; 



Where   α= ( α1, α2,….. ,αn) is an n-dimensional vector of constants and β1, β2,……., βp are _n × n_ autoregressive matrices and  εt is an n-dimensional white noise process with ′ covariance matrix _E_ (ε _t_ ε _t_ ) = Ψ . 

The traditional VAR model has some limitations. First of all we face the issue of overparameterization.  We have to estimate too many parameters and some of them may be statistically insignificant. For example, a VAR model with five variables and four lags, and a constant in each equation will contain a total of 105 ((1+5×4) × 5=105) coefficients. The second problem is that over-parameterization will cause Multicollinearity as well as a reduction in degrees of freedom that may result as a very good in-sample fit but a possibility of a large out-of-sample forecast error, some times referred to as over-fitting problem. 

Litterman (1980) described an approach to overcome these problems. Litterman (1980, 1986) introduced Bayesian VAR approach and used a prior, popularly referred to as “Minnesota Prior”, and solved the issue of over-parameterization (see Litterman 1980, 1986; Doan et al. 1984; Todd 1984, for more detail).  Litterman’s prior is based on three assumptions.  First, all equations contain a random walk with drift model. This essentially shrinks the diagonal elements β1 towards one, and the other coefficients (β2, β3,…., βp) towards zero. Second, more recent lags provide more useful information (have more predictive power) than more distant ones. Third, own lags explain more (have more predictive power) of a given variable than the lags of the other variables in the model. The Litterman (1986) prior is imposed by the following (Mean and variance) moments for the following prior distribution of the coefficients. 



7 

The coefficients β1, β2,…., βp are assumed to be independent and normally distributed. The covariance matrix of the residuals is assumed to be diagonal, fixed and known i.e., 2 2 Ψ = ∑, where ∑ = diag (σ1 ,.........,σ _n_ ) , and the prior on the intercept is diffuse. The random walk prior (δi) has some intuitive implication such as δi=1 for all i, indicating that all variables are highly persistent. However, the researcher may believe that some of the variables in the model are following a mean reversion or at least not characterized by a random walk then this does not pose a problem for this framework, because a white-noise prior can be set for some or all of the variables in the VAR model by imposing δi=0 where appropriate. The hyper-parameter λ controls for the overall tightness of the prior distribution around δi. This hyper-parameter governs the importance of prior beliefs relative to the information contained in the data; λ=0 imposes the prior exactly so that the data do not inform the parameter estimate, and λ=∞ removes the influence of the prior altogether so that the parameter estimates are equivalent to OLS estimates. The factor 1/k<sup>2</sup> is the rate at which the prior variance decreases with the lag length of the VAR, and 2 2 σ _i_ /σ _j_ accounts for the different scale and variability of the data. The coefficient ϑε()1,0 governs the extent to which the lags of other variables are less important than own lags.<sup>9</sup> 

Litterman’s method is a good solution to many of the problems associated with the traditional VAR model. Another issue, however, is the presence of the unit root in the series of the model. What happened to the VAR’s estimate and to the forecasting in a non-stationary framework and possible cointegration relationships between the components of the VAR model? There are two popular answers to this question. One group of economists, especially, Lütkepohl(1991), Clements and Mizon (1991), and Phillips (1991) have found that when the BVAR analysis unfolds in context of a nonstationary process and there is potential for cointegration relationships, the estimate would be biased. They suggested that, on the basis of prior information which takes the entire coefficient to be inter-dependent (both in the same equation as well as between equations) and which assigns a mean equal to one, or close to one, to the first own lag coefficient and of zero to the rest, the Bayesian estimation of the VAR models tends to be biased towards system made up of univariate AR models, being incapable of capturing the possible common stochastic trends that characterize cointegration process. 

On the other hand, a group of economists are in favor of using BVAR model at the level form of the series. For example, Sims, Stock, and Watson (1990) showed that if the potential cointegration restrictions existing are not taken into account and the model is estimated in levels, this estimation is consistent. Sims (1991) said that these critiques were poorly grounded; arguing that, owing to the super-convergence property of the estimators in the presence of cointegration relationship, these aspects tend to manifest themselves with clarity, irrespective of the type of the prior information used. Alvarez and Ballabriga (1994) furnished evidence on this matter and performed a Monte-Carlo simulation with a cointegrated process that allows the power of different estimation methods for capturing the long-run relationship to be considered. The results obtained 

> 9 Kadiyala and Karlsson (1997) as well as Sims and Zha (1998) have modified original Litterman’s prior by imposing a normal prior distribution for coefficient and an inverse Wishart  prior distribution for the covariance matrix of the residuals Ψ. 

8 

sustain Sims’ proposition as opposed to that of the critics, provided that the prior distribution has been selected in keeping with a goodness-of-fit criterion. 

Instead of follow one group on other, we follow a comprehensive modeling approach. First we run a BVAR model with a level form of all series and called it BVARlevel then we run a another BVAR model with first difference form of all series and save results as BVAR-difference and the third model is a Bayesian vector error correction model (BVECM).<sup>10</sup> The Bayesian inference on a cointegrated system begins by using the prior of β obtained from the vector error correction model (VECM) form. The VECM (p) form with the cointegration rank _r_ (≤ k) is written as; 



′ Where Δ is the differencing operator, such that, ΔYt=Yt – Yt-1; Π = αβ , where α and β * are _k_ × _r_ matrices; Φ _i_ is a _k_ × _k_ matrix. 

In total, we run three different BVAR models, (1) we follow Litterman’s prior and run a BVAR model using the level form of the series of interest, calling it BVAR-level. (2) We run the same model with first difference of the data series, calling it BVARdifference, and (3) we apply a unit root test and find the order of integration and then apply cointegration and get the co-integrated rank (r) and then follow BVECM procedure, calling the result BVECM.<sup>11</sup> 

### **2.2 The Bayesian Factor Augmented Vector Autoregression (Bayesian FA-VAR) Model** 

Macroeconomic variables are often inter-related and contain useful information in forecasting each other. It is always good to have more information, as more information corresponds with better forecasting. There is a substantial interest in forecasting using many predictors or variables in recent years. Specifically, the idea that variations in a large number of economic variables can be modeled by a small number of reference variables is appealing and is used in many economic analyses. In a series of papers, Stock and Watson (1989, 1991, 2002a, 2002b, 2004, and 2005) showed that the forecast error of a large number of macroeconomic variables can be reduced by including diffusion indexes, or factors, in structural as well as non-structural forecasting model. We follow the Stock and Watson (2002) method. We extract common factors through the principal component (PC) and then used these factors in our forecasting process. The PC is 

> 10 See section 4, empirical results, for more detail. For BVAR-level and BVAR-difference we will use above mention procedure. 

> 11 We use ADF test for unit root testing and Johansen’s Cointegration test to identify the cointegration rank 

> ( _r_ ). We are not discussing these tests and detail of these tests can be found in Hamilton (1994). 

9 

arguably the best known statistical method used to reduce the dimension in a linear framework. It is one of the effective methods for handling Multicollinearity in regression analysis. The method is concerned with the variance-covariance structure of the predictor with the goal of using a few linear combinations of the predictors to explain the covariance structure.<sup>12</sup> 

The central idea of the dynamic factor model is that information in a large data set can be parsimoniously summarized by a small number of common factors i.e., q < N where N is total number of variables and q is common factors. In addition, the dynamic factor model is based on the idea that macroeconomic variables are characterized by the sum of two mutually orthogonal unobservable components; the common component driven by a small number of factors and the idiosyncratic component driven by variable-specific shocks. Let Xt be the n-dimensional vector of time series predictors and it is observed for t=1,2,……,T. Additionally, Xt is transformed to be stationary, if not stationary at level, and for notational simplicity we assume also that each series has a mean of zero. The dynamic factor model representation of the Xt with _<u>r</u>_ common dynamic factors _f_ t, 



For i=1,2,…..,N, where εit = (ε1t, ε2t,………., εNt) is a _N_ ×1 idiosyncratic disturbance. ρi(L) is a lag polynomial in non-negative powers of L, it is modeled as having finite orders of at _s j_ most _s_ , so ρi (L) = ∑ρ _ij_<sup>_L_</sup> . _j_ =1 

The finite lag assumption permits rewriting (4) as 



′ ′ ′ Where Ft = ( ( _f t_ ,........, _f t_ − _s_ ) is an _r_ × 1, where _r_ ≤ (s + 1) _<u>r</u>_ . The i-th row of the Λ is (ρ10, ρi1, …., ρis) is a matrix of factor loadings. The key advantage of this static form is that the unobserved factors can be estimated consistently as N,T → ∞ jointly by taking principal components of the covariance matrix of Xt , provided mild regularity conditions are satisfied (Stock and Watson, 2002). Indeed, recent forecasting literature contains strong evidence that models which include these estimated factors as predictors have performed very well.<sup>13</sup> 

### **2.3 Determination of the Number of Factors** 

After the estimation of these factors, questions arise about how many factors would be included in final model? There are some choices available, such as Bernanke and Boivin (2003) fixed the number of factors equal to three in their VAR model. On the other hand, 

> 12 See Johnson and Wichern (2002), chapter 8, for more detail 

> 13 See for detail, Stock and Watson (1999, 2002, and 2005), Bernanke and Boivin (2003), Boivin et al (2005), Forni et at (2005), and many others. 

10 

Bai and Ng (2002) proposed information criterion,( e.g. Bayesian information criteria (BIC)), to select number of factors and Ludvigson and Ng(2007) used that criteria and determined the number of factors equal to eight. We follow a different method. We put several estimated factors into BVAR framework and select a best combination, based on out-of-sample RMSE. We found that first five factors have a minimum out-of-sample RMSE, see next section for more detail. 

### **2.4 Forecast Evaluation** 

The objective of the study is to forecast bottom in the U.S. house prices and that implies we are interested in out-of-sample forecasts. We set out-of-sample RMSE as forecast evaluation criteria for our factor-based model and other competing models. We generate forecasts from each model and then calculate out-of-sample RMSE for each model. The framework we used for calculation of the out-of-sample RMSE is that we assume that data is available between t=1 and t=T for modeling purpose, where T represents the most recent data point that is 2008:Q3. In addition, we are interested in h-step ahead forecasts, where h= 1,2,….,12, up to twelve quarters ahead. Assume an integer variable q that varies from 1 to q using one quarter as a unit. For each q, we choose data between t=1 and t=T-q to build a model and apply it to generate h-step ahead forecasts. Thereafter, the sample is augmented by one quarter and the parameters of each model are re-estimated and the corresponding h-step forecasts computed by moving the forecast window forward. This recursive procedure is continued until we reach the end point of the sample, 2008:Q3. We then calculate the out-of-sample RMSE for each step (from one quarter ahead to twelve quarters ahead) using the following equation; 



ˆ Where<sup>_Y_</sup> _t_ + _h_ / _t_ is the h-step ahead forecast of Yt at given time t. The magnitude of this statistic is used to compare the out-of-sample performance of each model and the model with the smallest RMSE is the best model among its competitors. 

11 

## **_3. The Data and the Implementation Strategy_** 

### **3.1 The Data** 

There are a few key points that we must stress about our dependent variable (s), which is home prices. There is no single widely standard upon measure for the U.S. house prices, and there are several different theoretically sound measures of house prices. Fortunately all of the home price measures are positively correlated over time, so in terms of direction, they all tell the same story. Their growth rates diverge quite significantly, however, and the conclusions drawn are often incongruent. This difference among various price measures is partly because houses are a heterogeneous asset class. They are unique because of location and physical attributes, and sales, or turnover, is typically infrequent. Therefore, each house price measure has its own advantages and shortcomings. 

Our first measure of house prices is the Federal Housing Finance Agency (FHFA), formerly known as OFHEO, U.S. house price index (HPI). This measure of national house prices is comprehensive and is available for nearly every metropolitan area in the United States, as well as for major Census regions and the nation as a whole. The FHFA index is a weighted, repeat-sales index, which measures average price changes from repeat sales and refinancing of the same properties. One benefit of using the FHFA HPI is that it covers a large geographical area, including nine Census Bureau divisions, 50 states, the District of Columbia, and nearly every metropolitan statistical area (MSA). FHFA also produces a purchase only home price index, FHFA Purchase only, which excludes refinancing. 

Another measure of house prices is the S&P/Case-Shiller index of house prices. The FHFA and S&P/Case-Shiller national house price index follow the same fundamental repeat-valuation approach and cover about the same geographical area. One key difference is the S&P/Case-Shiller house price index includes foreclosed homes and shows a much larger decline in national home prices. The FHFA house price index excludes foreclosed homes, and therefore shows a smaller decline in national house prices. Another key difference between the S&P/Case-Shiller and the FHFA Purchase only house price indices is the FHFA Purchase only includes transactions on all houses with values under the conforming loan limit (except for foreclosure transactions), while Case-Shiller tracks prices on all houses (those with higher and more volatile average prices). Both indices are correct but the inclusion of higher priced and more volatile homes makes the S&P/Case-Shiller series much more volatile. 

12 

Despite the problem in measuring house prices, the basic picture is clear. House prices rose slowly from 1990-2003, then rapidly until about 2006 or 2007, and then dropped off a cliff.<sup>14</sup> 

We used the following indices as a measure of house prices and as dependent variables: FHFA, FHFA Purchase only, and the S&P/Case-Shiller house price indices. The FHFAHPI goes back to the first quarter of 1975, S&P/Case-Shiller index only goes back to the first quarter of 1987, and the FHFA Purchase only goes back to the first quarter of 1991. We used quarterly data for 1987:Q1 to 2008:Q3 for the FHFA and Case-Shiller based models, and data from 1991:Q1 to 2008:Q3 for the FHFA Purchase only based model. As for predictors, or independent variables, we used two approaches. (i) In the BVAR model, we used seven predictors selected from a large data set of over 300 variables, and (ii) In the Bayesian FA-VAR model, we used factors extracted from a data set of 141 variables. 

First we discuss variable selection method for independent variables for our BVAR model. The data source for all variables (dependent and independent) is the IHS Global Insight database. 

We follow a step-wise (three-step) procedure to select our independent variables. We, at Wells Fargo, maintain a large data set of over 600 variables. We keep all those variables with no missing values in the whole sample range, 1987:Q1 to 2008:Q3 for the FHFA and S&P/Case-Shiller home price indices based models, and 1991:Q1-2008:Q3 for the FHFA Purchase only-based model. Most of these variables are of monthly frequency, while others are of weekly or quarterly frequencies. We transformed the monthly and weekly data series into quarterly data series for consistency.<sup>15</sup> 

We then used four transformations: (i) the level form of the variable (ii) the lag of the variable (iii) the first difference form (iv) and the lag of the first difference form. In total, we created over 1,000 variables as potential predictors for U.S. house prices.<sup>16</sup> 

> 14 There are other measures of house prices, such as the median existing home price by the National Association of Realtors (NAR) and an index computed by Fannie Mae, etc. We focus on these measures: FHFA home price index, FHFA Purchase only and the S&P/Case-Shiller home price index. 

> 15 We used SAS to convert monthly and weekly data series into quarterly data series, using the “average“option which takes the average of the quarter’s three months as value of that particular quarter. 16 We tried to choose as many predictors as possible. In contrast to typical econometric modeling where a modeler already has a model specification guided by an economic theory, here we assume that we do not know much about the model specification. We rely on data variation and statistical principals (basically, the data mining technique) which will indicate the choice of model specifications a prior. The key advantage, among others, is that it would allow each variable at least a chance to enter the final model and allow us to explore the forecastability of all predictors to a great extent. 

13 

### **3.2 Implementation Strategy: Selection of the Best Model Specification: The BVAR Model** 

We use a step-wise procedure, consisting of three steps, to choose the best model specifications. In the first step, we start by taking the regression of the dependent variable against each of these 1,000 variables, and retain those with significant predictive power. With a much smaller data set, we then find the best model specifications with one predictor, two predictors, or up to six predictors. We used R<sup>2</sup> as the selection criterion in choosing these specifications. We selected ten variables from this step. 

In the second step, we ran a one-by-one Granger-causality test between the dependent variable against each of these 1,000 variables to come up with the top ten variables based on the Chi-squared test.  We have now narrowed down our choice-list to 20 variables, ten from regression and ten from the Granger-causality test.<sup>17</sup> These 20 variables, however, came from an in-sample statistical procedure. 

For the third step, we used an out-of-sample RMSE as a statistical measure to find the final model specification. We set an eight variable BVAR framework which provides an opportunity for each of these 20 variables to audition as a predictor. We assume that data is available until 2001:Q4 and we forecast for one-quarter ahead. We then move onequarter ahead, using data till 2002:Q1, and again forecast for one-quarter ahead. This process is repeated till our data set reaches 2008:Q3. In the end, we have 27 out-ofsample one-quarter ahead forecasted data points, which we used to calculate the RMSE. We then selected eight variables with the lowest RMSE value. 

With the help of SAS, we increased the predictive power of our final model specification. As mentioned earlier, the BVAR method used a prior, referred to as “Minnesota Prior”, and the efficacy of the BVAR model depends, to some extent, on the prior and selection of lag orders. We applied a more flexible procedure to select the prior and the lag orders, which involves the above-mentioned recursive method to calculate the out-of-sample RMSE, but this time we did not fix the lag orders as well as the value of Litterman’s prior. We fixed a maximum lag order of nine since the data series is of quarterly frequency and does not have a long history. As the Litterman’s prior ranges between zero and one, with the flexibility and speed of the SAS system, we can get a better combination of the lags and the prior. For an eight-variable model, for example, we choose a lag parameter, P, which ranges from one to nine, and the Litterman’s prior,ϑ , which ranges from 0.1 to 0.9 with 0.1 increments, and same procedure followed for λ. Altogether, there will be 729 (9×9×9 = 729) models, consisting of a unique combination of P,ϑ , and λ, and 729 sets of RMSE. We then select the combination that has the minimum RMSE. This is our final model specification. 

This model has the best overall out-of-sample forecast performance based on RMSE, across multiple equations. Our predictors are (i) real disposable personal income, (ii) 

> 17 In the second step, we included all variables and selected the top ten variables other than those already selected in the first step. That way, we increased our choose-list to 20 variables. 

14 

mortgage delinquencies on all loans, (iii) the first-time homebuyer affordability index, (iv) the ratio of financial obligation to disposable personal income, (v) the homeownership rate, (vi) the effective rate of interest on mortgage debt outstanding for owners of residential housing, and (vii) Owner’s equivalent rent of primary residence.<sup>18</sup> 

### **3.3 Implementation Strategy: The Bayesian FA-VAR** 

The Bayesian FA-VAR is a two-step methodology. In the first step we extract factors through principal component and then we used these factors as predictors in the Bayesian-VAR framework. 

The variables making up Xt in equation (5) for factor extractions are monthly macroeconomic time series, as employed by Stock and Watson (2002b).<sup>19</sup> These series include 14 main categories: real output and income; employment and hours; real retail, manufacturing, and trade sales; personal consumption; housing starts and sales; real inventories and inventory-to-sales ratio; manufacturers orders and unfilled orders; stock prices; exchange rates; interest rates; money and credit quality aggregates; price indices; average hourly earnings; and miscellaneous. We chose those variables with non-missing values between January 1987 and September 2008. In total, we created 141 variables as potential predictors. The list of these variables is given in Appendix B. 

In the first step, we extract the factors. Our starting point is to make Xt as a stationary process, I(0). All 141 variables were subjected to three possible transformations: taking the natural logarithm, first differencing, and screening for possible outliers. After these transformations, all series are standardized to have a sample mean and variance of 0 and 1, respectively. We used the PC methodology (Stock and Watson, 2002a) to estimate the factors. We first use monthly time series to extract the eight monthly factors. Then, we transform these factors into a quarterly data series. 

In the first phase of the second step, we determined a number of factors. We used an outof-sample RMSE, repeated the third step from the previous discussion, and put the factors into the BVAR framework. First, we ran a four variable BVAR model, with the house price index and three factors. Then, we ran a five variable BVAR model, with the house price index and four factors. We keep increasing the number of factors until we reach a nine-variable BVAR model, with the house price index and eight factors. In total, we ran six different models, and for each model, at first we assume that we have data through 2001:Q4 and generate a forecast for one-quarter ahead. We then move one quarter ahead, with a data series that ends in 2002:Q1, and again generate another forecast. We repeat this process until we end up with a data series that ends in 2008:Q3. We then calculate an out-of-sample RMSE for each model and we found that the model with five factors has the minimum out-of-sample RMSE. This is our final model. Then, 

> 18 See Appendix A for more details, definitions, and sources of the data. 

> 19 From IHS Global Insight, we found most variables with exact definitions appeared in Stock and Watson (2002b). For a few variables with exact definitions not available in IHS Global Insight, we obtained closely related variables. 

15 

we need to find the best combination of lags and the Litterman’s prior (P,ϑ , and λ). We again set the maximum lag to nine and the prior from 0.1 to 0.9, with increments of 0.1. In total, we again ran 729 different models (9×9×9 = 729) and selected the model with the minimum out-of-sample RMSE.<sup>20</sup> 

## **_4. Empirical Results_** 

In this section, we will discuss the empirical results. We used three different measures of house prices; FHFA, S&P/Case-Shiller, and the FHFA Purchase only house price indices. Table 1-3 presents the results of the six models, and the out-of-sample RMSE for 1 to 12 quarters ahead. We also provide the average out-of-sample RMSE for each model. In Table 4-6 provides actual data, in-sample fitted value and out-of-sample forecasts for all three indices. These forecasts are based on the six different models, including our best model, the Bayesian FA-VAR model. We also plotted these out-of-sample forecasts, actual data points, and the in-sample fit in Figure 1-3. 

### **4.1 Univariate Models: AR and ARIMA Models** 

Our first model for forecasting the bottom of the U.S. house prices is the Autoregressive model of order one, AR (1), also called the random walk model. This model is a simple forecast model for house prices. We used data for 1987:Q1- 2001:Q4 period and generated forecasts up to 12 quarters ahead. Then, we move one quarter ahead, using data from 1987:Q1 to 2002:Q1 and again generated forecasts for next 12 quarters. We employed this recursive method until we reached the final data point that is 1987:Q12008:Q3.<sup>21</sup> We then calculated the out-of-sample RMSE for each quarter. In total, we have 27 forecast errors for 1 quarter ahead, 26 for 2 quarters ahead, 25 for 3 quarters ahead… and 16 forecast errors for 12 quarters ahead. Table 1 shows the out-of-sample RMSE for each quarter ahead, up to 12 quarters, as well as average RMSE for FHFA. Table 2 shows the FHFA Purchase Only RMSE and Table 3 shows the S &P/Case-Shiller RMSE. 

As expected, the RMSE increases as the forecast horizon increases, which indicate that when forecast horizon increases, uncertainty also increases, thereby the RMSE increases as we increases the forecast horizon. This pattern applies to all three indices, three measures of the U.S. house prices. 

Our next method of forecasting is the Autoregressive Integrated Moving Average (ARIMA) and we used ARIMA (1, 1, 1). Since we are using time series data and we may face non-stationary issue and the error term may have some moving average 

> 20 See the next section for more details. 

> 21 It is worth to mentioning that FHFA Purchase Only index is available from 1991:Q1. Therefore the starting dates for model using this data series is 1991:Q1-2001:Q4. 

16 

representations, not white noise. Therefore, we employed the ARIMA (1,1,1) process, which takes care of both non-stationary and autocorrelation issues. We followed the same recursive procedure as we described for AR model and generated the out-of-sample RMSE for each quarters up to 12 quarters ahead. The RMSE can be seen in Table 1, Table 2, and Table 3 for FHFA, FHFA Purchase Only, and S&P/Case-Shiller, respectively. The RMSE based on the ARIMA models are smaller than those based on AR models. However, RMSE based on ARIMA has an increasing trend with the forecast horizon. The vital issue related with both the AR(1) and the ARIMA(1,1,1) models is they have limited capability to capture long-run dynamics in the house prices thereby unable to forecast bottom in the house prices. In addition, out-of-sample forecasts generated by both models for the FHFA and the FHFA Purchase Only house prices indices have a decreasing trend even till the end of 2011. 

As expected, the AR and ARIMA models are too simple to forecast the house prices bottom, thereby calling for more complex econometric models that are able to include more variables. 

### **4.2 Multivariate Models: The Bayesian Vector Autoregression Models** 

Our next model is the Bayesian Vector Autoregression (BVAR) method. Based on the out-of-sample RMSE, we select lag orders, P = 4, prior, ϑ =0.9, λ = 0.1 for three different house prices indices. First, we employed level form of all three house prices indices and called the model BVAR-level. The average out-of-sample RMSE was reduced for all three indices, as can be seen in Table 1-3. An interesting observation is that the ARIMA (1,1,1) model has smallest RMSE for short-run forecasting, especially for 1 quarter ahead, for all three indices. 

As we can see from Table 1-3, average RMSE are smaller for BVAR-level approach than AR and ARIMA models but issue related with BVAR-level model is that it is based on non-stationary data series. To deal with this problem, we used the first difference form of all series as it is assumed that the difference form will be stationary. We called this model the BVAR-difference. We still employed the same lag orders and prior, P = 4,ϑ = 0.9 and λ = 0.1, for all three indices. The average out-of-sample RMSE based on BVARdifference is smaller than BVAR-level, ARIMA, and AR models for all three house price indices. 

However, when using the difference form of the variables, we may not be able to retain short-term information and therefore need to develop a procedure that retains short-term information. It is always better to identify the order of integration as well as cointegration relationship properly rather than to make assumption about these relationships. Therefore, we employed the ADF test to identify the order of integration for each series in our models, and then we performed Johansen’s cointegration test to find the cointegrated 

17 

relationship.<sup>22</sup> We concluded that all series are stationary at their first difference, and the order of integration is I(1) for all series. In addition, the Johansen test results provided an evidence of cointegration for all three indices. We performed BVECM with the same lag order and prior (p =4, ϑ = 0.9 and λ = 0.1) and found the average out-of-sample RMSE are smaller for the FHFA and the S&P/Case-Shiller indices compared to other approaches. But for the FHFA Purchase Only index, the average out-of-sample RMSE based on BVECM is equal to the BVAR-difference’s out-of-sample RMSE, as shown in Table 2. On average, the BVECM approach has the smallest out-of-sample RMSE for the FHFA and the S&P/case-Shiller models. For the FHFA Purchase Only index, BVECM and the BVAR-difference approaches have the same average out-of-sample RMSE, but smaller than other approaches. 

### **4.3 The Bayesian FA-VAR** 

In the forecasting process, it is always preferable to include as much information as possible along with a better econometric method to lead to better forecast. In the Bayesian FA-VAR framework, we can incorporate more information than a traditional econometric framework. 

We included the first five factors, extracted from a large data set of 141 variables, in a BVAR framework. We selected the best combination based on an out-of-sample RMSE, using lag order, p = 5, and prior as ϑ = 0.9, and λ = 0.9. The average out-of-sample RMSE is smallest for FHFA model (Table 1), the FHFA Purchase Only (Table 2), and the S&P/Case-Shiller models (Table 3).<sup>23</sup> Since factors are extracted from a large data set which contains variables from all major sectors of the economy thus includes more information and therefore produces better forecasts. 

The forecasting performance of the Bayesian FA-VAR approach is the best out of all six models as it produces the smallest average out-of-sample RMSE, or the smallest average forecasting error.  Therefore, we used the Bayesian FA-VAR approach to forecast the bottom in U.S. house prices. We consider forecasts based on the Bayesian FA-VAR approach as key findings of the study. Using data up to 2009:Q2, we provide up-to-date out-of-sample forecasts from all six models for all three indices in Table 4, 5 and 6. In addition, in Figure 1-3, we plotted out-of-sample forecast with actual data and in-sample fitted values from all six approaches for FHFA, FHFA Purchase Only and S&P/CaseShiller indices. 

Based on our empirical study, we would like to make a few suggestions for model selection criterion. Assuming that we set one quarter ahead out-of-sample RMSE as model selection criterion, we will end up with different approaches and conclusions for 

> 22 We are not reporting unit root and cointegration results. But results are available upon request from authors. 

> 23 Due to non-stationarity issue we used the first difference form of the FHFA, FHFA Purchase Only, and S&P/Case-Shiller indices.  Since factors came from a data set of stationary series thereby we used level form of the factors. 

18 

the house prices bottom. The ARIMA (1,1,1) and BVAR-difference models have the same but smallest one quarter ahead out-of-sample RMSE for FHFA, as shown in Table 1. From Table 2, ARIMA (1,1,1) came in as the best approach because it produced the smallest one quarter ahead out-of-sample RMSE for FHFA Purchase Only.  The BVAR FA-VAR approach has the smallest one quarter ahead out-of-sample RMSE for S&P/Case-Shiller, as in Table 3. If we choose the ARIMA (1,1,1) approach for the FHFA Purchase Only index to forecast the house prices bottom. We end up with an un-realistic answer. We will not hit the bottom even at the end of 2011, showing that the FHFA Purchase Only index will fall continuously, which is not a realistic portrait. Therefore, the lesson we learn from this empirical study is that model selection criterion should be consistent with the objective of the forecast. For instance, the objective of our study is to forecast bottom in the U.S. house prices and we are expecting that house prices may be bottom out by end of this year or may by end of 2010; simply we do not know yet. In addition, we would like to see the recovery pattern, either a V-shaped—fast recovery, or a U-shaped—slow recovery. In general, we would like to see what pattern house prices will follow over the course of the next three years, or 12 quarters ahead forecasts. We desire an accurate approach for the 12 quarters ahead forecasts and therefore set the smallest out-of-sample RMSE as a selection criteria. The Bayesian FA-VAR approach fulfills that requirement and has the smallest out-of-sample RMSE, on average. Therefore, our preferred approach for forecasting the house prices bottom is the Bayesian FA-VAR. We are also forecasting a U-shaped recovery pattern for house prices. 

## **_5. Caveat_** 

In this section we discuss the limitations of our empirical methodology. There are a few issues related to both data and econometric methodology that we want to discuss here and we are leaving them for future research. 

The problems with data that we face are data revisions and different time lag in releases. Some revisions are huge, such as for the variables change in non-farm payrolls and industrial production. Therefore, there is a debate on what the appropriate data series should be – real time vs. revised<sup>24</sup> . Variables are also released with different time lags. Non-farm payrolls are release on the first Friday after the month has ended, as in the data for March comes out the first Friday of April. On the other hand, personal income and spending data are released at the end of the following month, so March data will only come out at the end of April and sometimes even in the first week of May. Often, in modeling, we assume that we are in real time and all data are available for that period of time. In reality, however, we will only obtain data after that certain time period has passed, and sometimes after quite a significant amount of time. This issue should be considered in the modeling process. However, one may argue that the consequences are not severe for long-term forecasting. 

> 24 Bernanke and Boivin (2003) found that the impact of data revision is insignificant in their forecasting. 

19 

The issue related with factor methodology is that we may lose short-run information. We used extracted factors in the Bayesian FA-VAR framework and these factors extracted from a large data set. We convert all series into stationary process, if they are not stationary originally. Most macroeconomic series are not stationary at their level thereby we need to convert them into stationary. We then standardized all series in the way they have mean and standard deviation equal to zero and one, respectively. It is good that we obtained factors from a stationary data set and thereby stationary estimated factors. By converting the data series into stationary forms, we tend to lose short-run information. We should have a way to include short-term information with these factors in modeling, but for now, we leave that for future discoveries. 

## **_6. Conclusion_** 

In this study, we utilized three different measures of house prices and six different models to forecast the bottom in house prices. We used the simulated out-of-sample root mean square error (RMSE) criteria to determine the best model to use out of the six we employed. We found the best model to be the Bayesian FA-VAR model. 

Using the Bayesian FA-VAR model, we obtained two different dates for the bottom in house prices for the three different indices. We project house prices to bottom in 2010:2Q using the FHFA index with an 8.70% drop from its 2007:2Q peak. The FHFA Purchase Only index will bottom out in 2010:2Q with a 12.24% decline from its 2007:2Q peak. The S&P/Case-Shiller index will bottom out in 2010:1Q with a 32.85% drop from its 2006:2Q peak. All three indices produced similar results, suggesting we will see house prices bottom next year (2010) and a very slow U-shaped recovery. Both 2009 and early 2010 will be a very difficult time for the housing industry and homeowners. 

Another important concluding remark from our empirical analysis is that while the housing sector was the root cause of the financial crisis and subsequent recession, we do not expect housing to lead the economy out of recession or to restore financial stability. The combination of a sharp drop in home prices, dramatic loss of wealth, tightening credit conditions, and projected slow recovery in house prices, will likely mean the subsequent recovery in home sales and home construction will be too modest to drive the overall economy.  While a bottoming out in home prices may be the key to ending the financial crisis, it will not likely spark a strong and sustainable recovery. 

One important issue we would like to share here that is the effect of current stimulus package and Fed as well as U.S. Treasury effort to jump-start the economy and restore the financial sector confidence. These efforts may help during the recovery period but we do not expect a significant change in our conclusion. 

20 

## **_Reference_** 

Álvarez, L. J. and Ballabriga, F. C. (1994). “BVAR Models in the Context of Cointegration _:_ A Monte Carlo Experimen _”._ Documento de Trabajo nº 9405, Banco de España, Servicio de Estudios. 

Bai J. and Ng S. (2002). “Determining the number of factors in approximate factor models”. _Journal of Business and Economic Statistics_ 25: 147–162. 

Bai J. and Ng S. (2007). “Determining the number of primitive shocks in factor models”. _Econometrica_ 70: 191–221. 

Bernanke B., Boivin J, and Eliasz P. (2005). “Measuring the effects of monetary policy: a factor-augmented vector autoregressive (FAVAR) approach”. _The Quarterly Journal of Economics_ 120: 387–422 

Bernanke, B. and Boivin J. (2003). “Monetary Policy in a Data-Rich Environment”. _Journal of Monetary Economics_ 50: 525-546. 

Boivin, J. and Ng S. (2005). “Understanding and comparing factor-based forecasts”. _International Journal of Central Banking_ **1** : 117–151. 

Boivin, J. and Giannoni, M., (2008). "Global Forces and Monetary Policy Effectiveness," _NBER Working Papers_ 13736,. 

Chamberlain, Gary (1983). “Funds, Factors, and Diversification in Arbitrage Pricing Models”. _Econometrica_ 51: 1281-1304. 

Chamberlain, Gary, and M. Rothschild (1983). “Arbitrage, Factor Structure and MeanVariance Analysis in Large Markets”. _Econometrica_ 51: 1305-1324. 

Christiano, L., Eichenbaum, M., and Evans, C (2000). “Monetary Policy Shocks: What have we learned and to what end?” In Taylor, J., Woodford, M. (Eds), _Handbook of Macroeconomics_ . North-Holland, Amsterdam. 

Clements, M. P. and Mizon, G. E. (1991). “Empirical Analysis of Macroeconomic Time Series: VAR and Structural Models”, _European Economic Review,_ 3 5 , 887-917. 

Cristadoro, R., Mario, F.,  Lucrezia, R., and Giovanni, V. (2005). “A Core Inflation Indicator for the Euro Are” . _Journal of Money, Credit and Banking_ 37: 539-560. 

De Mol, C, D Gianonne, and L Reichlin (2008). “Forecasting using a large number of predictors: Is Bayesian regression a valid alternative to Principal Components?” _Journal of Econometrics_ , forthcoming. 

21 

Doan, T., Litterman, R. and Sims, C. (1984). “Forecasting and Conditional Projections Using Realistic Prior Distributions”. _Econometric Reviews,_ vol.1,1-100. 

Forni M, Hallin M, Lippi M, and Reichlin L. (2000). “The generalized dynamic factor model: identification and estimation”. _The Review of Economics and Statistics_ 82: 540– 554. 

Forni M, Hallin M, Lippi M,  and Reichlin L. (2003). “Do financial variables help forecasting inflation and real activity in the Euro area?”. _Journal of Monetary Economics_ 50: 1243–1255. 

Forni, M,MHallin,MLippi, and L Reichlin (2005). “The generalized factor model: onesided estimation and forecasting”. _Journal of the American Statistical Association_ , 100(471), 830–840. 

Geweke, John (1997). “The dynamic factor analysis of economic time series _”. In Latent Variables in Socio-Economic Models_ (Aigner, and A. Goldberger, Eds.) Amsterdam: North Holland, 365-383. 

Ginnone, D. and Matheson, T., (2007). “A New Core Inflation Indicator for New Zealand “, _International Journal of Central Banking_ 3: 145-180. 

Hamilton, J. D. (1994). _Time Series Analysis_ , Princeton: Princeton University Press 

Johnson, R. A. and Wichern, D. W. (2002). _Applied Multivariate Statistical Analysis_ , 5th Edition, Prentice-Hall: Upper Saddle River, New Jersey. 

Kadiyala, K R and S Karlsson (1997). “Numerical methods for estimation and inference in Bayesian VAR-models”. _Journal of Applied Econometrics_ , John Wiley & Sons, Ltd., vol. 12(2), pages 99-132. 

Kapetanios, G., and Marcellino, M.(2003). "A Comparison of Estimation Methods for Dynamic Factor Models of Large Dimensions”. _Working Papers 489_ , Queen Mary, University of London, Department of Economics. 

Leeper, E.m., Sims, C., and Zha, T. (1996). “What does monetary policy do?”, _Brooking Papers on Economic Activity_ 2, 1-63. 

Litterman, R. (1980). “Techniques for Forecasting with Vector Autoregressions”, _University of Minnesota,_ Ph. D. Thesis. 

— (1986). “Forecasting with Bayesian vector Autoregressions - 5 years of experience”, _Journal of Business and Economic Statistics_ , 1986, 4, 25.38. 

22 

Ludvigson, S., and Ng S. (2007). “Macro Factors in Bond Risk Premia”. _NBER Working Papers_ 11703. 

LÜtkepohl, H. (1991). _Introduction to Multiple Time Series Analysis,_ Springer Verlag, New York. 

Martin Schneider and Martin Spitzer, (2004). "Forecasting Austrian GDP using the generalized dynamic factor model," _Working Papers_ 89, Austrian Central Bank. 

Phillips, P. C. B. (1991). “Bayesian Routes and Units Roots: de Rebus Prioribus Semper Est Disputandum”, _Journal of Applied Econometrics,_ 6, 435-473. 

Richard M. Todd, (1984). "Improving economic forecasting with Bayesian vector autoregression," _Quarterly Review_ , Federal Reserve Bank of Minneapolis. 

Robert E. Hall and Susan E. Woodward (2009). “The Financial Crisis and the Recession: What is Happening and What the Government Should Do” Working paper www.scribd.com/doc/8687358/The-Financial-Crisis-and-the-Recession 

Robertson, J., C., and Ellis W. Tallman (1999). “Vector Autoregressions: Forecasting and Reality” , _Federal Reserve Bank of Atlanta Economic Review_ , 1999, 84 (1), 4.18. 

Sargent TJ, and Sims CA. (977). “Business cycle modeling without pretending to have too much _a priori_ economic theory”, In _New Methods in Business Cycle Research_ , Sims CA (ed.). Federal Reserve Bank of Minneapolis: Minneapolis. 

Sims, C. A. (1980).  “Macroeconomics and Reality”. _Econometrica,_ vol. 48, nº 1, 1-48. 

— (1986a). “Are Forecasting Models Usable for Policy Analysis?”, _Quarterly Review,_ Winter, 2-16, Federal Reserve Bank of Minneapolis. Minneapolis. 

— (1986b). Bayesmth: a program for multivariate Bayesian interpolation _, Discussion Paper 234_ , University of Minnesota, Center for Economic Research. 

— (1989). A Nine Variable Probabilistic Model of the US Economy _, Discussion Paper 14_ , Federal Reserve of Minneapolis, Institute for Empirical Macroeconomics. 

— (1991a). “Comment on Empirical Analysis of Macroeconomic Time Series: VAR and Structural Models”, by Clements and Mizon, _European Economic Review,_ 35, 922-932. 

— (1991b). “Comment on To criticize the critics”, by Peter C. B. Phillips, _Journal of Applied Econometrics,_ 6, 423-34. 

Sims, C. A. and Zha, T (1998). “Bayesian Methods for Dynamic Multivariate Models”. _International Economic Review_ , 1998, 39 (4), 949.968. 

23 

Sims, C .A., Stock, J., and Watson, M. (1990). “Inference in Linear Time Series Models with Some Unit Roots”, _Econometrica,_ 58, 113-144. 

Stock J, and Watson M. (1989). “New Indexes of Coincident and Leading Economic Indicators”. In _NBER Macroeconomics Annual_ , Blanchard J, Fischer S (eds). 

Stock J, and Watson M. (1999). “Forecasting Inflation”. _Journal of Monetary Economics_ 44: 293-335. 

Stock J, and Watson M. (2002a). “Forecasting Using Principal Components from a Large Number of Predictors”, _Journal of the American Statistical Association_ 97: 1167-1179. 

Stock J, and Watson M. (2002b). “Macroeconomic Forecasting Using Diffusion Indexes”, _Journal of Business & Economic Statistics_ 20: 147-162. 

Stock J, and Watson M. (2003). “How did Leading Indicator Forecasts Do during the 2001 Recession?”, _Federal Reserve Bank of Richmond Economic Quarterly_ 89: 71-90. 

Stock J, and Watson, M (2005), “Implications of Dynamic Factor Models for VAR Analysis,” _National Bureau of Economic Research, Working Paper_ , 11467. 

Waggoner, D. F., and  Tao Zha (1999). “Conditional Forecasts In Dynamic Multivariate Models” ,. _The Review of Economics and Statistics_ , 1999, 81 (4), 639.651. 

Watson, M. W., (2000). “Macroeconomic Forecasting using Many Predictors”. Princeton 

University, Unpublished. 

24 

#### **Table 1. FHFA as Dependent Variable: Out-of-Sample RMSE** 

|||||||**Forec**<br>|**ast Horizo**<br>|**n, Quarte**<br>|**rs Ahead**<br>|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Model**|1|2|3|4|5|6|7|8|9|10|11|12|Average|
|**AR**|5.39|15.77|27.15|38.87|51.46|64.40|76.93|88.66|99.57|109.78|119.38|128.70|68.8|
|**ARIMA**|2.02|7.19|14.04|21.59|30.19|37.75|45.55|56.36|66.84|76.23|84.06|92.62|44.5|
|**BVAR-Level**|2.07|7.73|14.58|21.75|29.57|35.85|43.17|52.21|60.73|70.21|76.94|83.85|41.6|
|**BVAR-Difference**|2.02|6.80|12.58|18.39|24.58|30.94|37.44|44.44|52.50|60.34|67.58|73.65|35.9|
|**BVECM**|2.09|5.85|11.22|17.03|23.02|29.16|35.62|42.78|50.54|58.55|65.76|71.82|34.5|
|**Bayesian-FAVAR**|2.52|5.49|10.59|16.41|21.97|27.58|33.57|40.29|47.41|54.83|61.38|66.75|32.4|



#### **Table 2. FHFA Purchase Only as Dependent Variable: Out-of-Sample RMSE** 

|||||||**Foreca**<br>|**st Horizon,**<br>|**Quarters**<br>|**Ahead**<br>|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Model**|1|2|3|4|5|6|7|8|9|10|11|12|Average|
|**AR**|3.15|9.22|14.93|20.94|27.29|34.03|40.84|47.29|53.42|59.23|64.74|70.03|37.1|
|**ARIMA**|0.64|4.23|7.52|11.20|15.63|19.05|22.48|26.22|30.39|35.21|39.64|44.40|21.4|
|**BVAR-Level**|1.02|4.60|7.94|11.17|14.40|16.88|19.34|21.59|24.30|26.68|28.78|30.56|17.3|
|**BVAR-Difference**|0.75|3.66|6.34|9.34|12.62|15.67|18.75|21.77|24.32|26.81|28.38|29.51|16.5|
|**BVECM**|0.78|3.70|6.32|9.34|12.66|15.69|18.77|21.81|24.34|26.87|28.41|29.56|16.5|
|**Bayesian-FAVAR**|0.78|3.53|6.01|9.03|12.17|15.14|18.17|20.80|22.97|24.34|24.56|25.11|15.2|



25 

#### **Table 3. S&P/Case-Shiller as Dependent Variable: Out-of-Sample RMSE** 

|||||||**Forecast**<br>|**Horizon,**<br>|**Quarters A**<br>|**head**<br>|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Model**|1|2|3|4|5|6|7|8|9|10|11|12|Average|
|**AR**|4.19|12.07|18.83|25.35|31.59|37.07|42.29|47.98|54.30|60.17|65.51|70.44|39.1|
|**ARIMA**|1.68|8.40|14.84|21.35|27.48|32.65|36.25|40.51|44.25|49.17|54.22|58.73|32.5|
|**BVAR-Level**|2.29|8.30|13.92|19.38|24.39|27.70|30.26|32.84|35.06|38.01|40.52|43.67|26.4|
|**BVAR-Difference**|1.77|6.51|10.99|15.01|19.01|22.81|26.06|29.25|32.29|34.76|35.91|35.62|22.5|
|**BVECM**|1.37|5.77|10.40|14.44|18.54|22.22|25.53|28.65|31.64|34.24|35.46|35.05|21.9|
|**Bayesian-FAVAR**|1.34|5.44|9.79|13.67|17.76|21.15|24.34|27.37|30.15|32.36|34.19|33.38|20.9|



26 

**Table 4. FHFA – Home Price Index: Actual, In-Sample Fitted, and Out-of-Sample Forecast** 

||||**In-Sampl**|**e Fitted and Out-o**|**f-Sample For**|**ecast**|
|---|---|---|---|---|---|---|
|Date|Actual|AR  ARIMA B|VAR-Level B|VAR-Difference|BVECM|Bayesian FA-VAR|
|1/1/2005|333.85|326.09 333.48|333.40|331.49|332.31|333.67|
|4/1/2005|344.12|333.79 340.99|340.99|340.88|342.37|339.89|
|7/1/2005|354.57|344.05 352.35|351.03|352.29|354.34|351.18|
|10/1/2005|362.75|354.50 363.40|361.12|362.12|364.12|359.71|
|1/1/2006|369.03|362.67 370.81|368.65|368.85|370.43|370.64|
|4/1/2006|372.35|368.95 375.85|373.95|374.44|375.16|375.23|
|7/1/2006|375.68|372.26 377.21|376.92|376.82|375.59|377.35|
|10/1/2006|380.86|375.59 379.62|379.51|379.63|378.84|380.61|
|1/1/2007|383.16|380.77 385.22|383.22|384.22|384.63|383.31|
|4/1/2007|383.23|383.07 386.39|383.98|384.54|383.82|385.79|
|7/1/2007|380.39|383.14 384.89|384.16|384.14|384.11|385.65|
|10/1/2007|381.42|380.30 379.96|381.22|378.88|378.37|381.47|
|1/1/2008|381.23|381.33 381.79|380.22|380.12|381.53|382.04|
|4/1/2008|374.53|381.14 381.42|377.72|377.79|378.06|380.72|
|7/1/2008|365.98|374.44 371.62|371.52|368.81|368.10|372.20|
|10/1/2008|366.31|365.90 360.75|364.78|361.93|361.61|364.48|
|1/1/2009|368.43|366.23 364.09|362.99|363.79|364.77|364.01|
|4/1/2009|359.57|368.35 368.46|360.43|363.07|363.57|362.99|
|7/1/2009||359.49 355.59|351.97|351.60|351.75|354.74|
|10/1/2009||359.42 351.96|344.94|354.15|355.65|352.59|
|1/1/2010||359.34 348.67|337.23|354.03|355.01|351.03|
|4/1/2010||359.26 345.69|328.36|352.65|352.17|349.89|
|7/1/2010||359.19 343.00|318.73|352.73|352.48|349.91|
|10/1/2010||359.11 340.58|308.54|353.44|354.20|351.15|
|1/1/2011||359.04 338.42|297.69|353.58|353.95|353.34|
|4/1/2011||358.96 336.50|286.12|353.45|352.67|355.45|
|7/1/2011||358.88 334.80|273.85|353.62|352.78|358.41|
|10/1/2011||358.81 333.32|260.92|353.96|353.65|361.10|



27 

**Table 5. FHFA – Purchase Only: Actual, In-Sample Fitted, and Out-of-Sample Forecast** 

|||||**In-Sample Fitted and Out-**|**of-Sample**|**Forecast**|
|---|---|---|---|---|---|---|
|Date|Actual|AR|ARIMA|BVAR-Level BVAR-Differenc|eBVECM|Bayesian FA-VAR|
|1/1/2005|198.39|194.24|198.56|198.73<br>198.41|199.15|198.02|
|4/1/2005|202.91|198.30|202.23|202.45<br>201.96|202.38|202.02|
|7/1/2005|207.80|202.82|207.07|206.49<br>206.64|207.29|206.56|
|10/1/2005|212.51|207.70|212.30|211.28<br>211.86|212.54|211.63|
|1/1/2006|215.63|212.41|216.90|215.52<br>216.24|216.56|216.44|
|4/1/2006|217.12|215.52|218.70|218.16<br>218.63|219.21|218.99|
|7/1/2006|218.39|217.01|218.72|218.73<br>218.86|218.19|219.40|
|10/1/2006|220.28|218.28|219.66|219.25<br>219.80|219.17|219.89|
|1/1/2007|221.79|220.17|222.02|220.91<br>221.94|222.14|221.72|
|4/1/2007|222.13|221.68|223.27|221.76<br>222.94|222.79|223.22|
|7/1/2007|220.89|222.02|222.63|221.23<br>222.20|222.17|223.12|
|10/1/2007|218.14|220.78|219.99|219.23<br>219.69|219.62|220.93|
|1/1/2008|214.27|218.03|215.86|215.88<br>215.79|215.43|217.01|
|4/1/2008|210.61|214.17|210.93|211.46<br>210.84|210.45|212.07|
|7/1/2008|206.64|210.51|207.33|207.34<br>206.80|206.11|207.98|
|10/1/2008|200.16|206.54|203.12|202.92<br>202.37|201.09|203.79|
|1/1/2009|199.09|200.07|194.55|196.85<br>195.72|195.68|196.39|
|4/1/2009|197.71|199.00|197.70|196.23<br>196.94|197.67|196.52|
|7/1/2009||197.62|196.50|195.04<br>194.96|196.44|196.34|
|10/1/2009||197.54|195.45|192.86<br>194.63|196.15|195.64|
|1/1/2010||197.45|194.55|191.39<br>195.06|196.77|195.16|
|4/1/2010||197.36|193.79|190.58<br>195.22|197.12|194.94|
|7/1/2010||197.28|193.15|190.37<br>195.08|196.91|194.96|
|10/1/2010||197.19|192.62|190.86<br>195.09|196.74|195.16|
|1/1/2011||197.11|192.20|192.16<br>195.27|196.92|195.52|
|4/1/2011||197.02|191.88|194.28<br>195.40|197.05|196.01|
|7/1/2011||196.93|191.65|197.18<br>195.45|196.93|196.61|
|10/1/2011||196.85|191.50|200.83<br>195.53|196.82|197.30|



28 

#### **Table 6. S&P/Case-Shiller Home Price Index: Actual, In-Sample Fitted, and Out-of-Sample Forecast** 

||||**In-Sample**|**Fitted and Out-o**|**f-Sample Fo**|**recast**|
|---|---|---|---|---|---|---|
|Date|Actual|AR  ARIMA B|VAR-Level B|VAR-Difference|BVECM|Bayesian FA-VAR|
|1/1/2005|169.19|162.78 166.76|167.80|167.36|168.93|167.03|
|4/1/2005|176.7|168.89 174.49|173.61|174.39|176.58|173.36|
|7/1/2005|183.08|176.36 182.66|180.02|181.36|181.57|180.98|
|10/1/2005|186.97|182.72 187.39|185.72|187.32|187.87|187.71|
|1/1/2006|188.66|186.59 189.39|188.61|190.04|190.79|190.75|
|4/1/2006|189.93|188.27 189.65|189.74|191.13|191.01|191.58|
|7/1/2006|188.11|189.54 191.25|189.53|190.96|190.75|191.61|
|10/1/2006|186.44|187.72 185.75|186.27|186.43|185.38|188.15|
|1/1/2007|184.83|186.06 186.31|184.57|185.93|186.42|185.88|
|4/1/2007|183.17|184.46 183.52|182.81|184.80|185.86|183.51|
|7/1/2007|180.07|182.81 182.46|179.82|181.05|179.62|181.52|
|10/1/2007|170.61|179.72 177.39|175.33|176.28|174.13|178.19|
|1/1/2008|159.4|170.30 161.84|165.42|164.20|161.07|166.82|
|4/1/2008|155.9|159.14 152.07|154.31|152.69|151.15|153.73|
|7/1/2008|150.42|155.65 156.49|150.37|151.89|152.06|150.65|
|10/1/2008|139.27|150.20 144.33|143.45|142.85|140.44|145.03|
|1/1/2009|128.94|139.10 130.51|133.53|131.39|128.93|133.59|
|4/1/2009|132.64|128.81 122.60|124.78|124.82|126.97|133.39|
|7/1/2009||132.49 140.81|128.49|133.58|137.24|129.90|
|10/1/2009||132.35 145.91|124.02|129.09|130.62|127.93|
|1/1/2010||132.20 149.26|121.28|129.11|129.93|127.55|
|4/1/2010||132.06 151.60|120.00|131.87|135.07|128.05|
|7/1/2010||131.92 153.37|119.71|132.11|135.83|128.53|
|10/1/2010||131.78 154.82|120.40|130.84|131.95|129.52|
|1/1/2011||131.63 156.08|122.31|130.86|131.23|130.89|
|4/1/2011||131.49 157.23|125.47|131.81|134.16|132.48|
|7/1/2011||131.35 158.33|129.73|132.05|134.85|134.24|
|10/1/2011||131.21 159.39|135.01|131.72|132.63|136.13|



29 

#### **Figures 1a – 1f: FHFA Home Price Index: Actual, In-sample Fitted, and Out-of-Sample Forecast** 



<!-- Start of picture text -->
Forecast Based on AR Model  Forecast Based on ARIMA Model Forecast Based on BVAR-Level Model<br>FHFA Home Price Index FHFA Home Price Index FHFA Home Price Index<br>400 400 400 400 400 400<br>380 Forecast 380 380 Forecast 380 380 380<br>360 360 360 360 360 360<br>Forecast<br>340 340 340 340 340 340<br>320 320 320 320 320 320<br>300 300 300 300 300 300<br>280 280 280 280 280 280<br>260 FHFA Home Price Index: Q2 @ 359.6 260 260 FHFA Home Price Index: Q2 @ 359.6 260 260 FHFA Home Price Index: Q2 @ 359.6 260<br>Fitted AR: Q2 @ 368.3 Fitted ARIMA: Q2 @ 368.5 Fitted BVAR-Level: Q2 @ 360.4<br>240 240 240 240 240 240<br>2002 2004 2006 2008 2010 2002 2004 2006 2008 2010 2002 2004 2006 2008 2010<br><!-- End of picture text -->

##### **Figure 1a:  Based on AR model** 

##### **Figure 1b. Based on ARIMA model** 

**Figure 1c. Based on BVAR-Level Model** 



<!-- Start of picture text -->
Forecast Based on BVAR-Difference Model Forecast Based on BVECM Model Forecast Based on Bayesian FA-VAR Model<br>FHFA Home Price Index FHFA Home Price Index FHFA Home Price Index<br>400 400 400 400 400 400<br>380 Forecast 380 380 Forecast 380 380 Forecast 380<br>360 360 360 360 360 360<br>340 340 340 340 340 340<br>320 320 320 320 320 320<br>300 300 300 300 300 300<br>280 280 280 280 280 280<br>260 FHFA Home Price Index: Q2 @ 359.6 260 260 FHFA Home Price Index: Q2 @ 359.6 260 260 FHFA Home Price Index: Q2 @ 359.6 260<br>Fitted BVAR-Difference: Q2 @ 363.1 Fitted BVECM: Q2 @ 363.6 Fitted Bayesian FA-VAR: Q2 @ 363.0<br>240 240 240 240 240 240<br>2002 2004 2006 2008 2010 2002 2004 2006 2008 2010 2002 2004 2006 2008 2010<br><!-- End of picture text -->

**Figure 1d:  Based on BVAR-Difference model** 

**Figure 1e:  Based on BVECM model** 

**Figure 1f:  Based on Bayesian FA-VAR model** 

30 

#### **Figures 2a – 2f: FHFA Purchase-Only Index: Actual, In-sample Fitted, and Out-of-Sample Forecast** 



<!-- Start of picture text -->
Forecast Based on AR Model  Forecast Based on ARIMA Model Forecast Based on BVAR-Level Model<br>FHFA Purchase-Only Index FHFA Purchase-Only Index FHFA Purchase-Only Index<br>230 230 240 240 230 230<br>220 220 220 220 210 210<br>190 190<br>210 Forecast 210 200 200 Forecast<br>170 170<br>200 200<br>180 Forecast 180 150 150<br>190 190<br>160 160 130 130<br>180 180<br>110 110<br>140 140<br>170 170 90 90<br>160 FHFA Purchase-Only Index: Q2 @ 197.7 160 120 FHFA Purchase-Only Index: Q2 @ 197.7 120 70 FHFA Purchase-Only Index: Q2 @ 197.7 70<br>Fitted AR: Q2 @ 199.0 Fitted ARIMA: Q2 @ 197.7 Fitted BVAR-Level: Q2 @ 196.2<br>150 150 100 100 50 50<br>2002 2004 2006 2008 2010 2002 2004 2006 2008 2010 2002 2004 2006 2008 2010<br><!-- End of picture text -->

##### **Figure 2a:  Based on AR model** 

##### **Figure 2b. Based on ARIMA model** 

**Figure 2c. Based on BVAR-Level Model** 



<!-- Start of picture text -->
Forecast Based on BVAR-Difference Model Forecast Based on BVECM Model Forecast Based on Bayesian FA-VAR Model<br>FHFA Purchase-Only Index FHFA Purchase-Only Index FHFA Purchase-Only Index<br>230 230 230 230 230 230<br>220 220 220 220 220 220<br>210 Forecast 210 210 Forecast 210 210 210<br>200 200 200 200 200 Forecast 200<br>190 190 190 190 190 190<br>180 180 180 180 180 180<br>170 170 170 170 170 170<br>160 FHFA Purchase-Only Index: Q2 @ 197.7 160 160 FHFA Purchase-Only Index: Q2 @ 197.7 160 160 FHFA Purchase-Only Index: Q2 @ 197.7 160<br>Fitted BVAR-Difference: Q2 @ 196.9 Fitted BVECM: Q2 @ 197.7 Fitted Bayesian FA-VAR: Q2 @ 196.5<br>150 150 150 150 150 150<br>2002 2004 2006 2008 2010 2002 2004 2006 2008 2010 2002 2004 2006 2008 2010<br><!-- End of picture text -->

**Figure 2d:  Based on BVAR-Difference model** 

**Figure 2e:  Based on BVECM model** 

**Figure 2f:  Based on Bayesian FA-VAR model** 

31 

#### **Figures 3a – 3f: S&P/Case-Shiller Home Price Index: Actual, In-sample Fitted, and Out-of-Sample Forecast** 



<!-- Start of picture text -->
Forecast Based on AR Model  Forecast Based on ARIMA Model Forecast Based on BVAR-Level Model<br>S&P/Case-Shiller Home Price Index S&P/Case-Shiller Home Price Index S&P/Case-Shiller Home Price Index<br>200 200 200 200 200 200<br>190 190 190 190<br>180 180<br>180 180 180 180<br>170 170 170 170 160 160<br>160 160 160 160<br>140 140<br>150 Forecast 150 150 150<br>120 120<br>140 140 140 140 Forecast<br>130 130 130 Forecast 130 100 100<br>120 120 120 120<br>110 S&P/Case-Shiller Home Price Index: Q2 @ 132.6 110 110 S&P/Case-Shiller Home Price Index: Q2 @ 132.6 110 80 S&P/Case-Shiller Home Price Index: Q2 @ 132.6 80<br>Fitted AR: Q2 @ 128.8 Fitted ARIMA: Q2 @ 122.6 Fitted BVAR-Level: Q2 @ 124.8<br>100 100 100 100 60 60<br>2002 2004 2006 2008 2010 2002 2004 2006 2008 2010 2002 2004 2006 2008 2010<br><!-- End of picture text -->

**Figure 3a:  Based on AR model** 

**Figure 3b. Based on ARIMA model** 

**Figure 3c. Based on BVAR-Level Model** 



<!-- Start of picture text -->
Forecast Based on BVAR-Difference Model Forecast Based on BVECM Model Forecast Based on Bayesian FA-VAR Model<br>S&P/Case-Shiller Home Price Index S&P/Case-Shiller Home Price Index S&P/Case-Shiller Home Price Index<br>200 200 200 200 200 200<br>190 190 190 190 190 190<br>Forecast<br>180 180 180 180 180 180<br>170 170 170 170 170 170<br>160 160 160 160 160 160<br>Forecast<br>150 150 150 150 150 150<br>140 140 140 140 140 Forecast 140<br>130 130 130 130 130 130<br>120 120 120 120 120 120<br>110 S&P/Case-Shiller Home Price Index: Q2 @ 132.6 110 110 S&P/Case-Shiller Home Price Index: Q2 @ 132.6 110 110 S&P/Case-Shiller Home Price Index: Q2 @ 132.6 110<br>Fitted BVAR-Difference: Q2 @ 124.8 Fitted BVECM: Q2 @ 127.0 Fitted Bayesian FA-VAR: Q2 @ 133.4<br>100 100 100 100 100 100<br>2002 2004 2006 2008 2010 2002 2004 2006 2008 2010 2002 2004 2006 2008 2010<br><!-- End of picture text -->

**Figure 3d:  Based on BVAR-Difference model** 

**Figure 3e:  Based on BVECM model** 

**Figure 3f:  Based on Bayesian FA-VAR model** 

32 

#### **Appendix A** 

#### **Data Series used in the Bayesian Vector Autoregression (BVAR) Models** 

|**Series Name**|**Brief Description**|
|---|---|
|HPI.Q*|FHFA, House Price Index, 1980 Q1=100,|
|<br>XPOIUS.Q*|<br>FHFA, Purchase Only Index, 1991 Q1 = 100|
|<br>HPICSCUS.Q*|<br>S&P/Case-Shiller Home Price Index - National Index, Index Jan 2000=100|
|<br>YPDR.Q|Real Disposable Personal Income, Billions of Chained (2000) Dollars,|
|<br>NFCITUS.Q<br>JFTBAFI.Q|<br>Mortgage Delinquencies, All Loans, Loans in Foreclosure, Ttal<br>First time homebuyer affordability index, Base=100|
|<br>DSFORT%YD.Q<br>RHOMEOWNNS.Q|<br>Ratio of Financial Obligations to Disposable Personal Income, Total,<br>Homeownership rate,|
|<br>RDBTMRESHNS.Q|<br>Effective Rate Of Interest On Mortgage Debt Outstand Owner Residential<br>Housing,|
|<br>CUSTSEHC.M.PREUPD**|<br>All Urban,Owners' equivalent rent ofprimaryresidence,Dec 1982=100,|
|*_Dependent variable_|**_Monthly series_|



33 

#### **Appendix B** 

The time series used to extract factors discussed in section 3 are presented here. The format is as follow: series number, transformation code, variable mnemonics, and brief series description. The transformation codes are: 1 = no transformation, 2 = first difference, 4 = logarithm and 5 = first difference of logarithm. The logarithms were taken for all nonnegative series that were not already in rates or percentage units. First differences were taken based on ADF test results. The series were taken directly from IHS Global-Insights and the original mnemonics are used, or they were produced by authors' calculations based on data from that database, in which case the authors’ calculation and original IHS Global-Insights series mnemonics are summarized in the data description filed.  The following abbreviations appear in the data definitions: SA = seasonally adjusted; NSA = not seasonally adjusted; Saar = seasonally adjusted at an annual rate; FRB = Federal Reserve board; AC = authors’ calculation; 

##### **_Real Output and Income_** 

- 1 5 IPSB50001 industrial production: total index(2002=100,sa) 2 5 IPSB50030 industrial production:products,total (2002=100,sa) 3 5 IPSB50002 industrial production: final products (2002=100,sa) 4 5 IPSB51000 industrial production:consumer goods (2002=100,sa) 5 5 IPSB51100 industrial production: durable consumer goods (2002=100,sa) 6 4 IPSB51200 industrial production: nondurable consumer goods (2002=100,sa) 7 5 IPSB52100 industrial production: business equipment (2002=100,sa) 8 5 IPSB53000 industrial production: materials (2002=100,sa) 9 5 IPSB53100 industrial production: durable goods materials (2002=100,sa) 

- 10 4 IPSB53200 industrial production: nondurable goods materials (2002=100,sa) 11 5 IPSB00004 industrial production: manufacturing (2002=100,sa) 12 1 UTLB00004 capacity util rate: manufacturing (sic),total (% of capacity,sa) (frb) 13 1 JCOMDIF (ISM) purchasing managers index(sa) 14 1 JPRODIF ISM production index (sa) 15 5 A0M052 personal income(chained)(series#52) (bil 2000$,saar) 16 5 A0M051 personal income less transfer payments (chained)(series#51) (bil 2000$,saar) 

- **_Employment and Hours_** 17 5 A0M046 index of help-wanted advertising in news papers (1987=100;sa) 18 4 A0M860 Ratio, help wanted advertising to persons unemployed 19 5 A0M842 civilian labor force: civilian employment(thous.,sa) 20 5 EMCTTNAG civilian employment level nonagric.industries(thous.,sa) 21 1 RUCTT unemployment rate: civilian, all 16 & over (%,sa) 

- 22 2 NWUTTTODA unemployment duration:average (mean) duration in weeks (sa) 

- 23 2 NUCTTTOD1 unemployed. by duration: persons unempl. Less than 5 wks (thous.,sa) 24 2 NUCTTTOD2 unemployed. by duration: persons unempl. 5 to 14 wks (thous.,sa) 25 1 NUCTTTOD5 unemployed. by duration: persons unempl. 15 wks+ (thous.,sa) 26 1 NUCTTTOD6 unemployed. by duration: persons unempl. 15 to 26 wks (thous.,sa) 

- 27 5 CES0000000001 employees on nonag. Payrolls: total (thous.,sa) 28 5 CES0500000001 employees on nonag. Payrolls: total, private (thous.,sa) 

- 29 4 CES0600000001 employees on nonag. Payrolls: goods-producing (thous.,sa) 

- 30 5 CES1021000001 employees on nonag. Payrolls: natural resources & mining, mining (thous.,sa) 31 5 CES2000000001 employees on nonag. Payrolls: construction (thous.,sa) 

34 

- 32 4 CES3000000001 employees on nonag. Payrolls: manufacturing (thous.,sa) 33 4 CES3100000001 employees on nonag. Payrolls: durable goods (thous.,sa) 34 5 CES3200000001 employees on nonag. Payrolls: nondurable goods (thous.,sa) 35 5 CES0700000001 employees on nonag. Payrolls: service-providing (thous.,sa) 36 5 CES4000000001 employees on nonag. Payrolls: trade,trans. & utilities (thous.,sa) 37 5 CES4142000001 employees on nonag. Payrolls: wholesale trade (thous.,sa) 38 5 CES4200000001 employees on nonag. Payrolls: retail trade (thous.,sa) 39 5 CES5500000001 employees on nonag. Payrolls: financial activities (thous.,sa) 40 5 ESVP employees on nonag. Payrolls: service-Providing (thous.,sa) 41 4 CES9000000001 employees on nonag. Payrolls: government (thous.,sa) 42 2 HPEAP avg. weekly hrs. of prod. Wkrs. : total private (sa) 43 1 HPMF avg. weekly hrs. of prod. Wkrs. : manufacturing (sa) 44 2 HOPMF avg. weekly hrs. of prod. Wkrs. : overtime hrs. (sa) 45 1 JEMPDIF ISM employment index (percent,sa) 

##### **_Real Retail, Manufacturing, and Trade Sales_** 

- 46 5 X56D manufacturing & trade: total (mil of chained 1996 dollars)(sa) 

##### **_Consumption_** 

- 47 5 CR personal consumption expend.(chained)- total(bil 2000$,saar) 48 5 CDR personal consumption expend.(chained)-durables goods(bil 2000$,saar) 49 5 CNR personal consumption expend.(chained)- nondurable goods(bil 2000$,saar) 50 4 CSVR personal consumption expend.(chained)- services(bil 2000$,saar) 

##### **_Housing Starts and Sales_** 

- 51 4 UHS new privately owned housing units started, total,(thous.,saar) 52 4 UHSNE new privately owned housing units started, northeast,(thous.,saar) 53 4 UHSNC new privately owned housing units started, Midwest,(thous.,saar) 54 4 UHSSO new privately owned housing units started, south,(thous.,saar) 55 4 UHSWE new privately owned housing units started, west,(thous.,saar) 56 4 UHBPC new private housing units authorized by building permits(composite), total,(thous.,saar) 57 5 UHBPCNE new private hou. units authorized by building permits(composite) northeast,(thous.,saar) 58 4 UHBPCNC new private hou. units authorized by building permits(composite), Midwest,(thous.,saar) 59 4 UHBPCSO new private hou. units authorized by building permits(composite), south,(thous.,saar) 60 4 UHBPCWE new private housing units authorized by building permits(composite), west,(thous.,saar) 61 5 UHNSLD new single family homes sold during month, total(thous.,saar) 62 4 RHFSHS new single family houses, month’s supply @ current sales rate(ratio) sa 63 5 UHNSAL new single family houses for sale at end of the month(thous, sa) 64 5 UMOB mobile homes: manufacturers’ shipments(mil.of units,saar) 

##### **_Real Inventories and Inventory-Sales Ratios_** 

- 65 2 A0M077 ratio for mfg & trade: inventory/sales (chained 2000$,sa) 66 1 JINVDIF ISM's inventories index (percent,sa) 

##### **_Orders and Unfilled Orders_** 

- 67 1 JORNDIF ISM's new orders index (percent,sa) 68 1 JDEVDIF ISM's supplier deliveries index (percent,sa) 69 5 X213 manufacturs' new orders,consumer goods & material,1982$ sa 70 5 A0M007 value of manufacturs'new orders, durable goods industries. Mil. of 2000$ 71 5 A0M027 value of manufacturs'new orders, capital goods indus. Nondefense, 82$ sa 

##### **_Stock Prices_** 

- 72 5 MF743 S&P's common stock price index: combined(1941-43=10) 73 5 MF744 S&P's common stock price index:400 industrial(1941-43=10) 74 2 MF1431 S&P's common stock yield (% per annum) 

35 

75 2 MF2523 

S&P's combined price-earnings ratio (% per annum) 

##### **_Exchange Rates_** 

- 76 5 M111L00NEU United States nominal effective exchange rate (neer)(index no.) 77 5 M134REX foreign exchange rate: Germany(deutsche mark per U.S.$) 78 5 M146REX foreign exchange rate: Switzerland(Swiss franc per U.S.$) 79 5 M158REXUSDD foreign exchange rate: Japan(yes per U.S.$) 80 5 MF8134 foreign exchange rate:United Kingdom(cents per pound) 81 5 M156REX foreign exchange rate: Canada (canadian $ per U.S.$) 

##### **_Interest Rates_** 

- 82 2 RMFEDFUNDNS interest rate: federal funds(effective)(% per annum,nsa) 83 2 MF1405 interest rate: U.S. treasury bills, sec mkt, 3-mo.(% per ann,nsa) 84 2 MF1407 interest rate: U.S. treasury bills, sec mkt, 6-mo.(% per ann,nsa) 85 2 MF1411 interest rate: U.S. treasury const maturities,1-yr.(% per ann,nsa) 86 2 MF1413 interest rate: U.S. treasury const maturities,5-yr.(% per ann,nsa) 87 2 MF1414 interest rate: U.S. treasury const maturities,10-yr.(% per ann,nsa) 88 2 MF1425 bond yield: Moody’s aaa corporate(% per annum) 89 2 MF1426 bond yield: Moody’s baa corporate(% per annum) 90 1 Spread_2 MF1405 - RMFEDFUNDNS (AC) 

- 90 1 Spread_2 

- 91 1 Spread_3 

   - MF1407 - RMFEDFUNDNS (AC) 

- 92 1 Spread_4 MF1411 - RMFEDFUNDNS (AC) 

- 93 1 Spread_5 MF1413 - RMFEDFUNDNS (AC) 94 1 Spread_6 MF1414 - RMFEDFUNDNS (AC) 95 1 Spread_7 MF1425 - RMFEDFUNDNS (AC) 96 1 Spread_8 MF1426 - RMFEDFUNDNS (AC) 

36 

##### **_Money and Credit Quantity Aggregates_** 

|97|5|M1C|money stock: m1 (curr, trav.cks, dem dep, other ck'able dep) (bil$,sa)|
|---|---|---|---|
|98|5|M2C|money stock: m2 (m1+o' nite rps, euro$, g/p&b/d mmms&sav&sm time dep) (bil$,sa)|
|99|4|MF8285|money stock: m3 component( Institutional Money Funds)(bil$,sa)|
|100|5|A0M106|money supply-m2 in billions/chained 2000$(sa)|
|101|5|MF2705|monetary base, adj for reserve requirement changes(bil$,sa)|
|102|5|MF2700|depository inst reserves: total, adj for reserve req chgs(mil$,sa)|
|103|5|MF2701|depository inst reserves:nonborrowed adj res req cgs(mil$,sa)|
|104|5|MF9115|loans & sec @ all coml banks: assets, total(bil$,sa)<br>|
|105|5|MF9102|loans & sec @ all coml banks: U.S. govt securities(bil$,sa)|
|106|5|MF9106|loans & sec @ all coml banks:real estate loans and leases(bil$,sa)|
|107|4|MF9109|loans & sec @ all coml banks: consumer, loans and leases(bil$,sa)|
|108|5|A0M101|commercial & industrial loans outstanding in millions/chained 2000$ (sa)|
|109|5|A0M072|wkly rp lg com'l banks: outstanding debtff com'l & indus loans(mil$,sa)|
|110|1|A0M113|net change in consumer instal credit(bil$,saar)|
|**_Pric_**|**_es I_**|**_ndexes_**||
|111|1|JPRIDIF|ISM's prices index (percent,sa)|
|112|5|S30S|producer price index: finished goods(82=100,sa)|
|113|5|S31S|producer price index: finished  consumer goods(82=100,sa)|
|114|5|S20S|producer price index: intermed mat. Supplies & components (82=100,sa)|
|115|5|S10S|producer price index: crude materials (82=100,sa)|
|116|5|PCIU|cpi-u:all items(82/84=100,sa)|
|117|5|PCIUAPP|cpi-u: apparel & upkeep  (82-84=100,sa)|
|118|5|PCIUTRN|cpi-u: transportation  (82-84=100,sa)|
|119|5|PCIUMED|cpi-u: medical care  (82-84=100,sa)|
|120|5|PCIUCOM|cpi-u: commodities  (82-84=100,sa)|
|121|5|PCIUDUR|cpi-u: durables  (82-84=100,sa)|
|122|5|PCIUSER|cpi-u: services  (82-84=100,sa)|
|123|5|PCIUXFOO|cpi-u: all items less food  (82-84=100,sa)|
|124|5|PCIUXSHL|cpi-u: all items less shelter  (82-84=100,sa)|
|125|5|PCIUXMED|cpi-u: all items less medical care  (82-84=100,sa)|
|126|5|JPC|pce, impl pr defl: pce (2000=100,sa)|
|127|5|JPCD|pce, impl pr defl: durables (2000=100,sa)|
|128|5|JPCN|pce, impl pr defl: nondurable (2000=100,sa)|
|129|5|JPCSV|pce impl pr defl: services (2000=100sa)|
|<br>**_Aver_**|<br>**_ag_**|<br>**_e Hourly Earnings_**|,     ,<br>|
|130|4|AHPEAP|avg hr earnings of prod wkrs: total private nonagric($,sa)|
|131|4|AHPCON|avg hr earnings of prod wkrs: construction($,sa)|
|132|4|AHPMF|avg hr earnings of prod wkrs: manufacturing($,sa)|
|133|4|AHPFIN|avg hr earnings of nonsupv wkrs: financial activities ($,sa)|
|**_Misc_**|**_ella_**|**_neous_**||
|134|5|M111L70|U.S. mdse trade: total exports(f.a.s. value)(mil$)|
|135|5|M111L71|<br>U.S. mdse trade: imports(c.i.f. value (mil$)|
|136|5|M111L71_V|U.S. mdse import: general imports(customs value)(mil$)|
|137|2|trade_balance1|U.S. mdse trade balance: exports less imports(fas/cif)(mil$,sa) (AC)|
|138|2|trade_balance2|U.S. mdse trade balance: exports less imports(fas/custom)(mil$,sa) (AC)|
|139|1|U0M083|f ihid f  ibd 83|
||||u. o mc.nex o consumer expectatons(c )|
|140|1|JEMPDIFC|Chicago PMI employment index|
|141|5|G0M910|Leading Economic Indicators|



37 

38 

