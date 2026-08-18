---
title: Bork_Housing price forecastability A factor analysis_2012
type: paper
source_pdf: raw/papers/Bork_Housing price forecastability A factor analysis_2012.pdf
converted: 2026-08-18
---





## **Housing price forecastability: A factor analysis** 

## **Lasse Bork and Stig V. Møller** 

## **CREATES Research Paper 2012-27** 

Department of Economics and Business Aarhus University Bartholins Allé 10 DK-8000 Aarhus C Denmark 

Email: oekonomi@au.dk Tel: +45 8716 5515 

# Housing price forecastability: A factor analysis<sup>∗</sup> 

Lasse Bork<sup>†</sup> Stig V. Møller<sup>‡</sup> 

May 2012 

###### Abstract 

We examine US housing price forecastability using a common factor approach based on a large panel of 122 economic time series. We find that a simple threefactor model generates an explanatory power of about 50% in one-quarter ahead in-sample forecasting regressions. The predictive power of the model stays high at longer horizons. The estimated factors are strongly statistically significant according to a bootstrap resampling method which takes into account that the factors are estimated regressors. The simple three-factor model also contains substantial out-of-sample predictive power and performs remarkably well compared to both autoregressive benchmarks and computational intensive forecast combination models. 

Keywords: House prices; Forecasting; Factor model; Principal components; Macroeconomic factors; Factor forecast combination; Bootstrap JEL codes: C53; E3; G1 

> ∗We gratefully thank Graham Elliott, Carsten Tanggaard, participants at the 2012 Arne Ryde Workshop in Financial Economics, and seminar participants at CREATES, Aalborg University, and Aarhus University for comments and suggestions. Møller acknowledges support from CREATES, which is funded by the Danish National Research Foundation. 

> †Department of Business and Management, Aalborg University, Denmark. E-mail: bork@business.aau.dk. 

> ‡Department of Economics and Business, Aarhus University and CREATES. Address: Fuglesangs Allé 4, 8210 Aarhus, Denmark. E-mail: svm@asb.dk. 

### 1 Introduction 

The recent boom and burst of the U.S. housing market strongly emphasizes that movements in housing prices play a significant role for consumer spendings, financial markets, and the macroeconomy as a whole. It follows that building an adequate forecasting model could provide useful information to central banks, financial supervision authorities as well as to other economic agents. 

The existing literature on house price forecastability is in some respects still limited. In particular, the existing evidence tends to focus on long-run trends in house prices. The focus also tends to be on only a single or a few selected house price indicators at a time such that a very narrow information set is used to generate forecasts of house prices. Valuation ratios (e.g., price-to-rent or price-to-income ratios) are among the most commonly used predictors of future house prices. These ratios work well as predictive variables at long horizons, but they are not necessarily useful at shorter horizons.<sup>1</sup> Using only a single or a few selected variables at a time to some extent appears ineffi cient when predicting future house prices because movements in house prices may reflect many different sources of information. Therefore, it may be possible to obtain more accurate house price forecasts by conditioning on a rich information set instead of only a few variables. 

Motivated by the above, this paper examines the ability to forecast real house prices at short and long horizons using a common factor approach in which we employ information from a very large number of macroeconomic and financial time series. The basic idea is to 

> 1See, for example, Campbell et al. (2009) and Gallin (2008) for in-depth analyses of the predictive power of the price-rent ratio. 

2 

summarize a large amount of information in a relatively small number of estimated factors and, as the next step, we use these estimated factors to forecast housing price fluctuations. In this way, we are able to make use of a much richer information set in comparison to previous studies on housing price forecastability. Essentially, the methodology that we apply in this paper enables us to condition the house price forecasts on a large information set involving more than 100 macroeconomic and financial variables. This is in sharp contrast to the typical predictive regression where only up to about a handful of observed variables is included in the predictor set. The key to embedding such a large information set in the regressions derives from a factor analysis of the panel where a few latent common factors are shown to describe the majority of the variation of the series in the panel. The factor analysis thus makes it possible to effectively reduce the dimension of the predictor set while still being able to summarize and use the underlying information in the panel. Furthermore, Stock and Watson (2002a, 2008) find that the common factor approach is robust to structural instability that often plagues predictive regressions because of the many different sources of information that shape each factor. 

Based on a large panel of 122 economic time series, we show that the estimated common factors contain substantial information about future movements in real house prices. In particular, a three-factor model is able to explain as much as around 50% of the variation in one-quarter ahead growth rates in real house prices. The predictive power also stays high at longer forecasting horizons. The three predictive factors can be interpreted as an economic activity, an inflation, and an interest rate factor. Following Gospodinov and Ng (2011), we conduct inference using a bootstrap procedure to address potential statistical issues originating from our use of estimated regressors and to take into 

3 

account possible time series dependencies in the predictive regressions. The bootstrap resampling method suggests that the three factors are generally strongly statistically significant. 

Our results are robust using both in-sample and out-of-sample forecasting regressions. In the out-of-sample forecasting, we compare with richly parameterized autoregressive models, and the simple three-factor model consistently beats the autoregressive benchmark across all forecasting horizons. This holds true when taking into account announcement delays of the macroeconomic series. We also conduct out-of-sample forecasting using a factor forecast combination approach in which optimal weights are recursively chosen based on criteria such as the past forecasting performance. Again, the results show that utilizing information from the large panel of economic series leads to smaller forecast errors than autoregressive benchmarks. In addition, we find that the simple three-factor model works remarkably well in comparison to the computational intensive forecast combination models. 

Focusing on the very volatile period around the recent boom and burst of the housing market, we find that the three-factor model contains useful information in the sense that it predicts with the right sign. Admittedly, the model does not fully capture the very large growth rates around the peak of the house price boom, but it does predict positive growth rates, i.e., the sign of the forecast is correct. Likewise, the model does not fully capture the sharp decline in house prices when the crash occurred, but it does predict negative growth rates. Thus, also when the crash occurred, the model gets the direction right. 

4 

Related literature. Case and Shiller (1989, 1990) were the first to document that housing prices do not follow a random walk. They show that housing returns exhibit positive autocorrelation and that various information variables predict future housing returns. Many recent studies examine predictability in the housing market using the price-rent ratio, which is analogous to the price-dividend ratio often used to forecast the stock market. Gallin (2008) examines the long run relationship between house prices and rents and finds that they are cointegrated and that the price-rent ratio contains useful information for predicting housing returns at long horizons. Favilukis et al. (2012) develop a general equilibrium model of the housing market, and their model implies that a high price-rent ratio predicts low future housing returns. They provide empirical evidence consistent with this implication. Campbell et al. (2009) and Cochrane (2011) also give empirical evidence that a high price-rent ratio is a signal of low future housing returns. Our focus is to forecast the growth in house prices conditioning on a large and more general information set. We find that using the large panel of economic time series gives much better out-of-sample predictive power relative to using the price-rent ratio. Actually, we find that the price-rent ratio performs worse than the historical mean in out-of-sample regressions, i.e., just like Goyal and Welch (2003, 2008) document that the price-dividend ratio is not able to beat the historical mean when forecasting stock returns out-of-sample. 

As an exception, Rapach and Strauss (2009) examine housing price forecastability using more than just a single or a few selected predictors. They analyze differences in housing price forecastability across the 20 largest U.S. states in terms of population. One of their findings is that the degree of predictability is lower in states with high average 

5 

house price growth (i.e., coastal states) than in states with low average price growth (i.e., interior states). As the focus of our paper is to forecast national house prices and not to examine the cross-sectional variation in forecasting power across regions, we only include national variables in our panel, and this also allows us to base our forecasts on a much larger set of economic variables. Specifically, we use 122 national economic series, while Rapach and Strauss (2009) only use 16. Exploiting a richer information set when forecasting house prices could potentially be very important as it intuitively should lead to more accurate forecasts, and it makes it possible to more fully examine the degree of predictability in housing prices. Another important difference is that our sample period includes the 2007 crash and the subsequent volatile period in the housing market. 

The empirical methodology that we apply in this paper to predict housing returns has also been used to predict stock returns (Ludvigson and Ng 2007) and to predict bond returns (Ludvigson and Ng 2009, 2011). The innovative methodological feature of our paper is that we also consider factor forecast combination and use a bootstrap resampling method to take into account that the factors are estimated regressors. 

The rest of the paper is organized as follows. Section 2 describes our empirical methodology, section 3 provides empirical results, and section 4 concludes. 

### 2 Empirical methodology 

In this section, we first describe how we estimate the factors using asymptotic principal component analysis. Then we describe how we run predictive regressions in which the predictor set includes time series of common factors from the factor analysis. 

6 

#### 2.1 Factor model and the estimation of factors 

In recent years, factor models have become a standard tool in applied macroeconomics and finance. Essentially, when the number of random sources of variation is less than the number of dependent variables, then a factor model enables the researcher to reduce the dimension of the number of explanatory variables to a few latent factors. Since the first generation of (exact) factor models by Geweke (1977) and Sargent and Sims (1977), a considerable amount of research has been devoted to the econometric theory and empirical analysis of large dimensional dynamic factor models. In particular, building on the approximate factor model of Chamberlain and Rothschild (1983), the large dimensional approximate dynamic factor model is introduced by Forni, Hallin, Lippi and Reichlin (2000, 2004, 2005) in the frequency domain and by Stock and Watson (2002a, 2002b) in the time domain.<sup>2</sup> They estimate the large dimensional dynamic factor model nonparametrically by dynamic and static principal component methods, respectively, but recently these models have also been estimated by Bayesian methods (Otrok and Whiteman 1998; Kim and Nelson 1999) as well as by maximum likelihood methods (Doz, Giannone and Reichlin 2011a, 2011b; Jungbacker and Koopman 2008). 

In our forecast analysis and similar to Ludvigson and Ng (2007, 2009, 2011), we implement the static principal component method of Stock and Watson because this method is fast, easy to implement, and given the sample size we consider, this method also performs similarly well compared to dynamic principal components (Boivin and Ng 

> 2By ’large’we mean large in the cross-section, i.e., large in the number of time series (N ), and large in the number of observations (T ) of the time series; for instance N = 100<sup>+</sup> and T = 100<sup>+</sup> depending on the frequency of the data. By ’approximate’we refer to the relaxation of the iid error term assumption in the exact factor model such that the error terms are allowed to be weakly (locally) correlated, cf. Chamberlain and Rothschild (1983). 

7 

2005) as well as maximum likelihood methods (Doz, Giannone and Reichlin 2011a). We now briefly describe the static principal component method, and for this purpose we present the dynamic factor model. 

##### 2.1.1 Dynamic factor model 

Consider a panel of observable economic variables Xi,t, where i denotes the cross-section unit, i = 1, ..., N , while t refers to the time index, t = 1, ..., T. The panel of observed economic variables is transformed into stationary variables with zero mean and unit variance and denoted by xi,t. The key implication of the dynamic approximate factor model is that the variation of each of the N observed variables can be decomposed into a common component, χt, that captures the cross-sectional comovement and an idiosyncratic component, ξt. Furthermore, the cross-sectional comovement of the variables is entirely driven by r << N common factors denoted Ft through series specific factor loadings, Λi. For the ith variable we write: 



where Ft is an r × 1 vector, Λi is an r × 1 vector of factor loadings for the ith observed variable, and where the idiosyncratic component ξi,t may have a limited amount of cross- 

sectional correlation.<sup>3</sup> The model in (1) is often labeled as the static form of the dynamic 

> 3Formally, this limited cross-sectional correlation is ensured by imposing the condition that the contribution of the covariance of the idiosyncratic terms to the total covariance of x as N gets large is bounded (by a constant M ): 



See Stock and Watson (2006) or Ludvigson and Ng (2009). 

8 

factor model because the (static) factors Ft only enter contemporaneously, but this is, however, merely a notational artifact.<sup>4</sup> 

The dynamic factor model in (1) is estimated by static principal components method which can be seen as a solution to the least squares problem: 



where k refers to number of factors involved in the minimization problem such that F<sup>(k)</sup> becomes a T × k matrix of estimated factors and Λ<sup>(k)</sup> = (Λ1, Λ2, ..., Λk)<sup>′</sup> is an N × k matrix of estimated loadings. As the model in (1) is not econometrically identified, a total of k<sup>2</sup> restrictions are imposed; in this case the standard k (k + 1) /2 normalization restrictions given by F<sup>(k)⊤</sup> F<sup>(k)</sup> = Ik, and the requirement that Λ<sup>(k)⊤</sup> Λ<sup>(k)</sup> is diagonal, which imposes an additional k (k − 1) /2 restrictions on the symmetric matrix Λ<sup>(k)⊤</sup> Λ<sup>(k)</sup> . The solution to this least squares problem is F<sup>ˆ(k)</sup> = √T P<sup>ˆ(k)</sup> and Λ<sup>ˆ(k)</sup> = x<sup>⊤</sup> F<sup>ˆ(k)</sup> /T, where ˆ P<sup>(k)</sup> is the T × k matrix of eigenvectors corresponding to the k largest eigenvalues of xx<sup>⊤</sup> /NT ; see, e.g., Stock and Watson (1998). Consistency of the principal component estimator of Ft is shown by Connor and Korajczyk (1986), Stock and Watson (2002a), and Bai and Ng (2006). In particular, Bai and Ng (2006) provide improved rates under which the estimated factors F<sup>ˆ</sup> t can be treated as observed, and hence inference about the parameters obtained in our second-stage predictions are not necessarily affected by the fact that the factors are estimated. However, as a precautionary step we base our 

> 4Notice, we could specify a model with the common component given by χi,t = λ<sup>T</sup> i<sup>(L) ft, where λi(L)</sup> is a q × 1 lag polynomial of finite order s representing the dynamic loadings, and ft is q × 1 dimensional vector of dynamic factors. Stacking the loadings and the dynamic factors into the q (s + 1) = r vectors Λi and Ft, respectively, the static representation of the dynamic approximate factor model of Stock and Watson (2002b) follows. 

9 

inference on a bootstrap resampling procedure, which we detail below in Section 2.4. 

We need to determine the number of factors k involved in the principal component analysis above. Econometric theory for the determination of the number of factors has recently been developed for both the dynamic factor framework (Hallin and Liska 2007; Stock and Watson 2005; Bai and Ng 2007) as well as for the static factor framework (Bai and Ng 2002). We apply the information criterion IC2 of Bai and Ng (2002) and as detailed in the next section, we find r = 11 factors. Accordingly, the principal component analysis in (2) proceeds by setting k = r = 11. 

#### 2.2 Predictive regressions 

Our purpose is to forecast the log real house price growth, yt+h = 100 × ln (Pt+h/Pt), where Pt denotes the real house price at time t, and h is the forecasting horizon. To do this, we use predictive regressions of the form: 



where the vector f<sup>ˆ</sup> t ⊂ F<sup>ˆ</sup> t contains estimated common factors that are relevant for forecasting h-period ahead real house price growth rates. β(L) and γ (L) are lag polynomials. 

We carry out both in-sample and out-of-sample forecasting analyses. The advantage of in-sample regressions is that all information is exploited, and therefore in-sample forecasting regressions is the most useful when it comes to examining the true relationship between the set of predictors and future house price growth rates. The disadvantage of in-sample forecasting regressions is that it does not tell us whether the forecasting model 

10 

would have been useful to an economic agent who operates in real time. 

We conduct out-of-sample forecasting based on a recursive scheme using all available data at the time of the forecast. We divide the full sample of T − h observations into an initial estimation period of T1 − h observations and an out-of-sample period of T2 observations. Thus, using a procedure where we recursively estimate the common factors as well as the parameters of the model, we generate a series of in total T2 forecasts of yt+h. If we let the out-of-sample window depend on h rather than the initial estimation period, our results do not change to any noteworthy extent. We generate the out-of-sample forecasts using the unrestricted model given in Eq. (3) and compare with an autoregressive benchmark model in which we set β(L) = 0.<sup>5</sup> Let ˆ ˆ h ε<sup>h</sup> U,t+h<sup>=yt+h−</sup> α<sup>h</sup> U,t<sup>+ ˆβ</sup> U,t<sup>(L)′ ˆft+ ˆγh</sup> U,t<sup>(L) yt</sup> denote the forecast error of the unre� � stricted forecasting model, and let ˆε<sup>h</sup> R,t+h<sup>= yt+h−</sup> �αˆ<sup>h</sup> R,t<sup>+ ˆγh</sup> R,t<sup>(L) yt</sup> � denote the forecast error of the restricted forecasting model. The out-of-sample statistic that we use is then given by: 



where a MSFE-ratio (Mean-Squared-Forecast-Error) of less than 1 implies that the unrestricted model produces a smaller mean squared forecast error than that of the restricted model. 

> 5 We use the autoregressive model as our main benchmark, but also show results using a number of alternative benchmarks, which we detail further below. 

11 

#### 2.3 Factor forecast combination 

Common factors effectively reduce the dimension of the predictor set and alleviate the instability issues arising from, e.g., structural shifts in the regressors. However, it is still a challenging task to specify a good forecasting model as a large number of candidate forecast models could arise out of the eleven factors and their potential lags combined with lagged house price growth rates. To overcome this challenge, we also consider a forecast combination approach; see Stock and Watson (2001), Timmermann (2006) and Aiolfiet al. (2010). In forecast combinations, forecasts from a large number of individual forecast models are combined to produce a weighted forecast, yˆt<sup>(</sup> +<sup>c)</sup> h|t<sup>.Thisapproachis</sup> often found to offer good empirical performance over individual model forecasts. 

In our application, we combine a large number of forecasts from different univariate and multivariate candidate forecast models involving factors and lagged house price growth rates. In particular, the forecast from the i<sup>th</sup> candidate model takes the form: 



where at most four factors of any combination of the eleven factors enters a particular specification. β<sup>ˆ</sup> i(L) is at most of order three (1 + β<sup>ˆ</sup> i1L + β<sup>ˆ</sup> i2L<sup>2</sup> + β<sup>ˆ</sup> i3L<sup>3</sup> ), and in case the lagged dependent variable enters, γˆi (L) is at most of order five (1 + ˆγi1L + ˆγi2L<sup>2</sup> + γˆi3L<sup>3</sup> +ˆγi4L<sup>4</sup> +ˆγi5L<sup>5</sup> ). For a given forecast horizon h, a total of M = 13, 488 models were estimated recursively for each of the T2 forecast dates. However, once the i<sup>th</sup> candidate forecast model has been estimated for all possible lag structures, we use the Schwartz information criterion (SIC) to choose the best lag specification. As an example, suppose 

12 

that the i<sup>th</sup> model involves four regressors: f<sup>ˆ</sup> 1,t, f<sup>ˆ</sup> 2,t, f<sup>ˆ</sup> 3,t, and yt. Given the restrictions on the lag polynomials, a total of 4 × 6 SIC values are then estimated for this particular model at time t, and for this particular model we then choose the best fitting model. This procedure effectively reduces the number of candidate models to m = 562. 

The combined forecast is then calculated as: 



where the time t weight assigned to the forecast from the i<sup>th</sup> candidate model takes a number of forms in the literature. We consider three popular weighting schemes. The first weighting scheme is based on the Schwartz information criterion (SIC) which can be viewed as Bayesian model averaging weights. The second scheme is based on the past MSFE performance, and the third is based on past discounted MSFE performance. Specifically, we apply the following three weighting schemes: 



where ∆SICi,t|t−h refers to the difference between the SIC criterion for the i<sup>th</sup> model at time t minus the time t best-fitting model. The MSFEi,t|t−h is calculated over a window of the previous v periods: 



13 

and DMSFEi,t|t−h refers to the discounted MSFE:<sup>6</sup> 



In the empirical section we provide out-of-sample results from this forecast combination approach. 

#### 2.4 Bootstrap 

We address potential small sample distortions in the inference about predictive regressions by a non-parametric moving block bootstrap that preserves time-series dependencies. On top of this, the moving block bootstrap also addresses the issue of generated regressors (the factors) in the predictive regressions, although Bai and Ng (2006) have shown that for a large cross-sectional dimension relative to the time-series dimension, we can ignore uncertainty in the factor estimates. 

The non-parametric moving block bootstrap method resamples the data in blocks of consecutive observations across all variables in order to reproduce possible time series dependencies due to, e.g., serial correlation and heteroskedasticity and to preserve any cross-sectional dependencies in the data. In our application, the resampling procedure thus needs to draw blocks simultaneously from the dependent variable y and the panel x, and from the resampled panel the factors are subsequently estimated. Then for each bootstrap sample the predictive coeffi cients in Eq. (3) are computed, and based on a large number of bootstraps the bootstrap confidence intervals can be computed; see the details below. 

> 6 We use the typical value of θ = 0.9 and set v = 12 quarters. 

14 

Consider stacking the dependent variable in Y = (yh+1, yh+2, ..., yT )<sup>′</sup> , the panel in X = (x1, x2, ..., xT −h)<sup>′</sup> , and in a similar way K lags of the dependent variable in W. We then represent the matrices Y, X , and W in a single ’parent’matrix B of dimension (T − h) × (1 + N + K): 



which is subsequently block-resampled with replacement yielding a particular bootstrap sample B<sup>∗</sup> . The factors are re-estimated using the corresponding X<sup>∗</sup> resulting in a set of factors F<sup>∗</sup> from which a subset f<sup>∗</sup> ⊂ F<sup>∗</sup> is used along with K lags of the dependent variable from W<sup>∗</sup> , as described by the predictive regression in Eq. (3) . Before detailing the resampling procedure, it can be noted that for a simple predictive regression in the form of yt+h = α + β<sup>′</sup> ft + γyt + εt+h, the B matrix is particularly simple: 



A given bootstrap sample B<sup>∗</sup> is essentially composed of a number of randomly selected blocks of size w × (1 + N + K) that are stacked upon each other so that the size of B<sup>∗</sup> is the same size as B. The number of blocks, b, is the integer of T/w, and the length w of each block can be computed using automatic block-length procedures as in, e.g., 

Patton et al. (2009)<sup>7</sup> . Specifically, a particular bootstrap sample can be generated 

> 7We are grateful to Andrew Patton for providing MATLAB code on his homepage to compute the automatic block-length. We find w = 20 and varying this number does not change our inference significantly. We are also grateful to Serena Ng for providing MATLAB code for bootstrapping factor models, which we modified slightly to fit our application. 

15 

by drawing with replacement (on a so-called circle) b iid uniform random variables, {ui}<sup>b</sup> i=1<sup>∈{1, 2, ..., (T−h)} ,where uiessentially determines at which row in Bwe select</sup> the ith block Bi<sup>∗with wrows (ui, ui+ 1, ..., ui+ w −1) and (1 + N+ K) columns.Then</sup> a particular bootstrap sample B<sup>∗</sup> can be written as: 



For each of the j = 1, ..., 5000 bootstraps, we run predictive regressions like Eq. (3) but here conditioning on the j<sup>th</sup> bootstrap data �Bj<sup>∗, F</sup> j<sup>∗</sup> �: 



We collect the estimated coeffi cients from Eq. (11) in a vector<sup>ˆ</sup> θ∗j<sup>with s.e.</sup> ˆθ∗j denoting � � the corresponding HAC standard errors.<sup>8</sup> Then we construct the following quantity for the ℓ<sup>th</sup> element of<sup>ˆ</sup> θ∗ j<sup>:</sup> 



where<sup>ˆ</sup> θℓ refers to the estimate from Eq. (3) conditioning on the observed sample. Following Gospodinov and Ng (2011), we let υ<sup>∗</sup> p<sup>and υ∗</sup> (1−p)<sup>denote the pthand (1 −p)thelement</sup> of the sorted sequence of tpℓ,j ’s, and obtain the 100 (1 − p) % percentile bootstrap confidence interval for<sup>ˆ</sup> θℓ as: 



8The lag truncation in the Newey-West HAC standard errors are set to h+3 to accommodate potential increasing residual autocorrelation problems in long-run regressions with overlapping observations. Due to the sign indeterminacy of the principal components, we ensure that the j<sup>th</sup> bootstrap factor stays positively correlated with the j<sup>th</sup> parent factor; possibly multiplying f<sup>ˆ</sup> j,t<sup>∗by(−1) .</sup> 

16 

These bootstrap confidence intervals are applied to every in-sample regression and are designed to address the issue of generated regressors as well as the issue of time series dependencies including residual autocorrelation due to long-run regressions with overlapping observations. 

### 3 Empirical results 

Our sample is quarterly and runs from 1975:1 to 2011:2. We measure nominal house prices based on the all-transactions house price index available from the Federal Housing Finance Administration (FHFA).<sup>9</sup> We obtain a real house price index by dividing the nominal house price index with the personal consumption deflator available from the Bureau of Economic Analysis. In Figure 1, we depict the time series of real house price growth over our sample period. The figure clearly illustrates the boom in the U.S. housing market from the beginning of the mid-1990s up to around 2006 as well as the crash in house prices in 2007. Furthermore, the figure illustrates an increase in volatility during the recent period of economic crisis. 

We use a panel of 122 economic series to estimate the factors. The list of series is provided in the Appendix. The series represent the following categories of macroeconomic time series: output and income; employment, hours and earnings; housing; consumption, orders and inventories; money and credit; bond and exchange rates; consumer, producer and commodity prices; and stock prices. 

When choosing how many principal components to retain, we apply the panel infor- 

> 9 Formerly Offi ce of Federal Housing Enterprise Oversight (OFHEO). 

17 

mation criteria developed by Bai and Ng (2002). In particular, when we use their IC2 criterion, we find that the appropriate number of components is eleven. As we show in Table 1, these eleven factors are able to account for a large part of the total variance in the panel: Almost 80% of the total variance is attributed to these eleven factors. The table also shows that about 50% of the total variability in the panel is accounted for by the three factors. 

In Table 1 we also report 1st order autocorrelation coeffi cients of the estimated factors. All factors (except the 9th factor) have positive persistence, and the degree of persistence varies somewhat across the factors. The second factor is the one with the highest degree of persistence with an AR(1) coeffi cient of 0.79, which is far from the unit root. 

#### 3.1 In-sample results 

We first assess the in-sample predictive power of the estimated common factors. We do so by estimating the forecasting model in Eq. (3) using the full sample. We are only interested in the factors containing useful information about future growth rates in real house prices. In general, across forecast horizons, statistical significance and information criteria suggest that it is suffi cient to include the first three factors out of the eleven estimated factors. We also adopt a parsimonious lag structure of order one as higher-order lags of f<sup>ˆ</sup> t and yt tend not to contribute with much predictive power. In the in-sample analysis, we therefore restrict the attention to the following simple three-factor 

18 

model:<sup>10</sup> 



For each forecast horizon that we consider (h = 1, 2, 4, and 8), Table 2 reports OLS estimates of the slope coeffi cients, 90% bootstrap confidence intervals of the slope coeffi - cients, the adjusted R<sup>2</sup> -statistic, and 90% bootstrap confidence intervals of the adjusted R<sup>2</sup> -statistic. 

Table 2 shows that the three estimated predictive factors are in almost all cases statistically significant according to the bootstrap resampling method. The only exception is when using h = 8, where the slope coeffi cient on the first factor is inside the bootstrap confidence interval. Likewise, the lagged house price growth rate is also in general statistically significant across horizons (only exception is when using h = 2). Looking at the adjusted R<sup>2</sup> statistic, the model is able to explain as much as 53.7% of the variation in one-quarter ahead house growth rates. The predictive power of the model stays high when increasing the forecast horizon: 53.2% at the 1-year horizon and 41.0% at the 2- year horizon. Thus, the model works well at various forecasting horizons. We also find that the bootstrap confidence interval for the adjusted R<sup>2</sup> statistic is well above 0 for all forecast horizons. 

If we drop yt from the model and only consider the information from the panel of economic series, the model continues to do well in predicting future house prices. Using the three predictive factors alone and excluding yt from the set of predictors, the adjusted R<sup>2</sup> s are given by 51.7%, 48.9%, 48.1%, and 36.8% at horizon h = 1, 2, 4, and 8.<sup>11</sup> 

> 10In the out-of-sample analysis, we experiment with forecast combination techniques where the lag length and the factor combination are recursively chosen based on Schwartz information criterion weights as well as inverse MSFE-weights (see section 3.2). 

> 11A table with results is available upon request. 

19 

Comparing with the adjusted R<sup>2</sup> s from Table 2, we thus observe a relatively small fall in predictive power when leaving out yt from the model. The high predictive power of the model is therefore not driven by the information contained in past house price growth rates. 

The three-factor model is able to forecast about 50% of the variation in the one-quarter ahead housing return. This high degree of forecastability suggests that our results are not only statistically significant, but also economically significant. Further, the strong predictive power of the factor model that utilizes information from a very large number of economic variables also suggests that it may be insuffi cient and misleading to base house price forecasts on only a single or a few selected predictors. In unreported results, we find that the price-rent ratio − the most commonly used house return predictor − does not contain much predictive power in comparison to the three-factor model and is statistically insignificant when adding it to the model. This is the case at both short and long horizons. Detailed results are available upon request. 

To illustrate how well our model works in-sample, Figure 2 plots the actual times series of real house price growth together with the forecasted values from the augmented three-factor model. The model convincingly captures large swings as well as peaks and troughs in housing returns. Even in the recent period with rapid house price fluctuations the model works reasonably well in predicting house prices. We also stress that our model does not fully capture the house price boom in the period from around 2004 to 2006 where the house price growth rates were very large. In this period the model does predict positive growth rates in real house prices, but it tends to underestimate the level of the growth rates. Similarly, the model does predict negative growth rates in 2007 when 

20 

the crash occurred, but it does not fully capture the sharp decline in house prices. Still, the sign of the forecast is correct and the model seems to contain important predictive ability even in periods with very volatile growth rates. 

##### 3.1.1 Factor interpretation 

In the following, we give an economic interpretation of our estimated common factors. We do this by looking at the R<sup>2</sup> s from regressing each of the series in the panel on each of the factors one at a time. Figure 3 illustrates that f<sup>ˆ</sup> 1,t is an economic activity factor. It loads heavily on industrial production and employment data. From Figure 4, we see that ˆ f2,t may be interpreted as an inflation factor since it loads most heavily on the various price indices that we transformed to standardized quarterly inflation rates. The factor also loads heavily on interest rates spreads, but whereas the various inflation rates are positively correlated with f<sup>ˆ</sup> 2,t, the interest rate spreads are negatively correlated with ˆ f2,t.<sup>12</sup> We find this inverse relationship between inflation and interest rate spreads quite intuitive as high inflation rates would force the Federal Reserve to increase the short-term monetary policy rate relative to the long-term interest rates in order to bring down inflation. Figure 5 indicates that f<sup>ˆ</sup> 3,t loads heavily on notably the longer-term interest rate related series (first differences) as well as housing variables. There is an inverse relationship between changes in interest rates and housing variables like housing starts, whereas the relationship is positive for houses for sale relative to houses sold. Accordingly, rising long-term interest rates makes it more diffi cult to finance houses and increases the selling period. Unreported results show that the absolute correlations between interest rates 

> 12Notice also that to enhance interpretation we can rotate the factors and loadings by multiplying by (−1). This only changes the sign of the regression coeffi cients, not the magnitude. 

21 

changes and f<sup>ˆ</sup> 3,t are more than twice as high as the absolute correlations with housing variables until summer 2009. However, for the last two years of the sample, housing starts and house selling periods begin to dominate f<sup>ˆ</sup> 3,t. On this background, we interpret the third factor as primarily an interest rate factor. Consistent with this interpretation, Thom (1985) provides evidence that housing starts are significantly influenced by interest rates and not the other way around. 

We now relate the factor interpretations to the sign of the slope coeffi cients in the predictive regressions (see Table 2). The economic activity factor (f<sup>ˆ</sup> 1,t) has a positive slope coeffi cient for every forecast horizon h in the predictive regressions. It implies that expected housing returns move procyclical, i.e., expected house price changes are high when economic conditions are good and low when economic conditions are bad. This is in contrast to return predictability evidence on the stock market (see, e.g., the survey of Cochrane 2007), the bond market (see, e.g., Ludvigson and Ng 2009), and the currency market (see, e.g., Lustig et al. 2010). In these asset markets, expected returns move countercyclical because investors require a higher expected return in times of bad economic conditions. One reason why we should not expect to see the same predictability patterns in the housing market is that housing is both a consumption good and an investment good. Further, due to various market frictions on the housing market (transaction costs, search costs, transaction time, financing constraints, short sale constraints, etc.), it is very likely that new information is only reflected fully in house prices with a time lag. This time lag also implies that when the affordability of households improves in times of good economic conditions, we should expect to see a positive impact on future house price growth rates. Our findings of procyclicality in expected house price 

22 

changes is consistent with Case and Shiller (1990) who find that employment and income variables have a positive relation with future housing returns. 

The inflation factor (f<sup>ˆ</sup> 2,t) has a negative slope coeffi cient for every forecast horizion h in the predictive regressions, so low inflation rates predict high real house price changes. Fama and Schwert (1977), Fama (1981), among others, provide evidence of a negative relation between inflation and real returns on the stock market. Moreover, Brunnermeier and Julliard (2008) document a negative relation between inflation and housing returns due to money illusion. In times when the inflation is low, investors that suffer from money illusion tend to underestimate the real interest rate and, hence, tend to underestimate real mortgage payments. In turn, this drives house prices up. 

The interest rate factor (f<sup>ˆ</sup> 3,t) has a negative slope coeffi cient for every forecasting horizon h. This is a very intuitive result: Low interest rates lead to cheaper mortgage loans, which again lead to larger mortgages and higher expected house prices. Because housing starts variables load negatively on f<sup>ˆ</sup> 3,t, increasing housing starts, due to easy house financing, coincides with higher expected house prices. 

#### 3.2 Out-of-sample results 

So far we have focused on in-sample forecasting regressions. To check the robustness of our in-sample results, we now turn to the out-of-sample evidence. In-sample forecasting makes use of full-sample estimates, while out-of-sample forecasting tests how sensitive the model is towards unstable predictive coeffi cients. Also, in the in-sample forecasting regressions, we generate the predictive factors once using the full sample of information, while in the out-of-sample regressions, we estimate the predictive factors recursively. In 

23 

the out-of-sample analysis, we thereby address the potential concern of look-ahead bias. Given the fact that many of the time series in our panel are subject to data revisions, another potential concern is that the series that are available today are different from the series available in real time. We only have access to vintage data for a limited part of our panel of time series, and we do not have vintage data for the house price index for a suffi ciently long period of time.<sup>13</sup> We therefore follow Rapach and Strauss (2009), Ludvigson and Ng (2007, 2009, 2011), among many others, and conduct out-of-sample forecasting using the today-available time series. We do, on the other hand, take into account that many of the series in our panel are announced with a delay of up to one quarter. Thus, in the out-of-sample analysis where the goal is to mimic the situation of a real-time forecaster, we lag our predictive variables an additional quarter. 

In our out-of-sample forecasting exercise, we use an initial estimation period of 20 years from 1975:1 to 1994:4, and the out-of-sample period thus runs from 1995:1 to 2011:2 (16.5 years). This period covers the recent boom and burst of the U.S. housing market. We conduct out-of-sample forecasting using two approaches. In the first approach the real time forecaster chooses the factors to be included in the model based on the initial estimation period and sticks with that model throughout the out-of-sample period. We recursively estimate the factors and the model parameters, but the choice of factors stays the same. In the second approach the real time forecaster utilizes factor forecast combination models. The out-of-sample forecasting power of the two approaches is compared with that of an autoregressive model in which the optimal number of lags is recursively chosen based on the Schwartz information criterion. We denote this model 

> 13In fact, the first vintage for the national house price index is from August 2010 in St. Louis Fed’s ALFRED real-time database. 

24 

by AR(SIC). To execute our program code within a reasonable time frame, we impose restrictions on the lag polynomials; see section 2.3. Specifically, the maximum number of lags allowed is six. However, the SIC criterion usually selects less than six lags. 

Three-factor model. The Bai and Ng (2002) panel information criterion suggests that the panel of economic series is well described by eleven factors. However, it is not necessarily the case that all eleven factors are useful in predicting house price growth rates. Statistical significance and various information criteria suggest only to include the first three out of the eleven factors. This is the case when estimating the model in Eq. (3) on the full sample, but also when estimating the model on the initial estimation period. To control for autocorrelation we augment the factor model with lagged house price growth rates. As with the autoregressive benchmark, we choose the optimal number of lags in the factor model recursively based on the SIC. 

The first row in Table 3 reports the out-of-sample results for augmented three-factor model. Across all forecasting horizons h = 1, 2, 4, 8, the three-factor model yields a lower mean-squared-forecast-error than the AR(SIC) model. By consistently beating the AR(SIC) model, the out-of-sample evidence confirms the in-sample evidence that the three-factor model contains useful information for predicting future house price growth rates. 

Forecast combination. We now consider the results from the factor forecast combination approach which combines forecasts from a large number of individual models. The individual models are based on various combinations of the eleven common factors as well as lags of the house price growth rate as detailed in section 2.3. We choose the 

25 

optimal lag structure of the individual models recursively using the SIC. We then calculate forecasts of the house price growth rates by weighting the forecasts of the individual models. We employ three different weighting schemes. The first scheme is based on the SIC criterion, the second scheme is based on the past MSFE performance, and the third scheme is based on past discounted MSFE performance. 

Table 3 reports the MSFE-ratio of the forecast combination models relative to the AR(SIC) model. It can be seen that the forecast combination models generally beat the autoregressive benchmark, especially at the long horizons. We also observe that the SIC weighting scheme tends to perform equally well as the two MSFE weighting schemes, and that the discounting procedure in DMSFE does not seem to matter for the forecast performance. 

Interestingly, the simple three-factor model performs very well compared to both the AR(SIC) model as well as to the much more computational intensive factor forecast combination models. In fact, the three-factor model performs better in MSFE ratio terms than the AR(SIC) model and the three variations of factor forecast combination methods for all forecast horizons up to one year, while for a two-year forecast horizon the forecast combination methods perform slightly better than the simple three-factor model. 

One of the explanations for the success of the forecast combination approach in empirical research is the robustness of this method towards structural shifts in one or more of the variables in the predictor set. Because the combination forecast is a weighted average of many candidate forecasting models, the fact that a few of the models become unstable does not change the forecast significantly. In this perspective, the moderate forecasting performance of the factor forecast combination in comparison to the three-factor model 

26 

is probably not surprising as the three-factor model is already robust towards structural shifts. But still, it is striking that among all these combinations, the factor combination approach could not find a particular weighting of various factor configurations that outperforms the simple three-factor model. Thus, the first three factors seem to be the relevant macroeconomic factors for forecasting the growth in real house prices. 

Alternative benchmarks. We have also made comparisons with more simple benchmarks than the AR(SIC) model, such as the sample mean growth rate in house prices and autoregressive models with a fixed lag structure through time. Given the strong focus on the price-rent ratio, see, e.g., Gallin (2008), Campbell et al. (2010), Cochrane (2011), Favilukas et al. (2012), we have also compared with the price-rent ratio. As we show in Table 4, the three-factor model strongly outperforms these alternative benchmarks. Interestingly, we find that the price-rent ratio generates worse out-of-sample forecasts than the historical mean. This finding relates to Goyal and Welch (2003, 2008) who provide evidence that the price-dividend ratio and a number of other predictors have worse out-of-sample performance on the stock market than do the historical mean stock return. Thus, the price-rent ratio shares the same lack of ability to predict returns out-of-sample as do the price-dividend ratio. 

### 4 Conclusions 

This paper examines the ability to forecast real house price changes using a common factor approach in which we exploit information from 122 economic time series. Using three common factors that together account for about 50% of the variability in the panel, 

27 

we are able to explain more than 50% of the variation in one-quarter ahead growth rates in real house prices. The forecasting power of the three-factor model also stays high at longer horizons. The estimated predictive factors are generally strongly statistically significant according to a bootstrap resampling method, which we design to address statistical issues such as time series dependencies and the use of estimated regressors in the forecasting regressions. 

The strong degree of predictability that we document using our panel approach suggests that it is insuffi cient and misleading to form house price forecasts based on a limited set of economic time series. As an illustration of this point, we find that the price-rent ratio − one of the most widely used house price indicators − performs worse than the historical mean in out-of-sample regressions. By contrast, the predictive power of the three-factor model is robust in out-of-sample regressions. The model strongly beats the historical mean, but also performs remarkably well compared to both an autoregressive benchmark with a rich lag structure as well as to much more computational intensive factor forecast combination models. 

28 

### Appendix 

This appendix presents the series in the panel. The first column of the table contains transformation codes where "lvl" indicates an untransformed series, say Xi,t. "∆lvl" " " " " means Xi,t − Xi,t−1, ln means ln Xi,t, and ∆ln means ln Xi,t − ln Xi,t−1. The second column contains longer descriptions of the variables. All series were downloaded from St. Louis Fed’s FRED database. 

###### Output and income 

- ∆ln Personal Income (Chained 2005 Dollars, SA) ∆ln Disposable Personal Income (Chained 2005 Dollars, SA) ∆ln Personal Income Excluding Current Transfer Receipts (Chained 2005 Dollars, SA) ∆ln Gross Domestic Product (Chained 2005 Dollars, SA) ∆ln Industrial Production Index - Total Index (SA) ∆ln Industrial Production - Durable Manufacturing (SA) ∆ln Industrial Production Index - Final Products (SA) ∆ln Industrial Production Index - Consumer Goods (SA) ∆ln Industrial Production Index - Durable Consumer Goods (SA) ∆ln Industrial Production Index - Nondurable Consumer Goods (SA) ∆ln Industrial Production Index - Business Equipment (SA) ∆ln Industrial Production Index - Materials (SA) ∆ln Industrial Production Index - Durable Goods Materials (SA) ∆ln Industrial Production Index - Nondurable Goods Materials (SA) ∆ln Industrial Production Index - Manufacturing (SA) lvl Napm Production Index (SA) lvl Capacity Utilization (SA) 

29 

Employment, hours and earnings 

|∆ln|Civilian Labor Force (Thous., SA)|
|---|---|
|∆ln|Civilian Employment (Thous., SA)|
|∆lvl|Unemployed (Thous., SA)|
|∆lvl|Average Duration of Unemployment (Weeks, SA)<br>|
|∆ln|Civilians Unemployed - Less Than 5 Weeks (Thous., SA)<br>|
|∆ln|Civilians Unemployed for 5-14 Weeks (Thous., SA)|
|∆ln|Civilians Unemployed - 15 Weeks & Over (Thous., SA)|
|∆ln|Civilians Unemployed for 15-26 Weeks (Thous., SA)|
|∆ln|Civilians Unemployed for 27 Weeks and Over (Thous., SA)|
|∆ln|All Employees: Total Nonfarm (Thous., SA)|
|∆ln|All Employees: Total Private Industries (Thous., SA)|
|∆ln|All Employees: Goods-Producing Industries (Thous., SA)|
|∆ln|All Employees: Mining and Logging (Thous., SA)|
|∆ln|All Employees: Construction (Thous., SA)|
|∆ln|All Employees: Manufacturing (Thous., SA)|
|∆ln|All Employees: Durable Goods (Thous., SA)|
|∆ln|All Employees: Nondurable Goods (Thous., SA)|
|∆ln|All Employees: Service-Providing Industries (Thous., SA)|
|∆ln|All Employees: Trade, Transportation & Utilities (Thous., SA)|
|∆ln|All Employees: Wholesale Trade (Thous., SA)|
|∆ln|All Employees: Retail Trade (Thous., SA)|
|∆ln|All Employees: Financial Activities (Thous., SA)|
|∆ln|All Employees: Government (Thous., SA)|
|∆ln|All Employees: Information Services (Thous., SA)|
|∆ln|All Employees: Professional & Business Services (Thous., SA)|
|lvl|Average Weekly Hours of Production and Nonsupervisory Employees: Goods|
|∆lvl|Average Weekly Hours of Production and Nonsupervisory Employees: Construction|
|lvl|Napm Employment Index|
|∆ln|Average Hourly Earnings of Production and Nonsupervisory Employees: Goods|
|∆ln|Average Hourly Earnings of Production and Nonsupervisory Employees: Construction|
|∆ln|Average Hourly Earnings of Production and Nonsupervisory Employees: Manufacturing|
|∆ln|Average Hourly Earnings of Production and Nonsupervisory Employees: Total Private|



###### Housing 

ln Housing Starts Total: New Privately Owned Housing Units Started (Thous., SA) ln Housing Starts in Midwest Census Region (Thous., SA) ln Housing Starts in Northeast Census Region (Thous., SA) ln Housing Starts in South Census Region (Thous., SA) ln Housing Starts in West Census Region (Thous., SA) ln New One Family Houses Sold: United States (Thous., SA) ln New Private Housing Units Authorized by Building Permits (Thous., SA) ln New Privately-Owned Housing Units Under Construction: Total (Thous., SA) ln New Homes Sold in the United States (Thous) lvl Median Number of Months on Sales Market lvl Ratio of Houses for Sale to Houses Sold (SA) 

###### Consumption, orders and inventories 

lvl Purchasing Managers’Index lvl Napm New Orders Index lvl Napm Supplier Deliveries Index lvl Napm Inventories Index ∆ln Personal Consumption Expenditures (Chained 2005 Dollars) 

30 

###### Money and credit 

|∆ln|Commercial and Industrial Loans at All Commercial Banks (SA)|
|---|---|
|∆ln|Consumer (Individual) Loans at All Commercial Banks (SA)|
|∆ln|Currency Component of M1 (SA)|
|∆ln|M1 Money Stock (SA)|
|∆ln|M2 Money Stock (SA)|
|∆ln|Real Estate Loans at All Commercial Banks (SA)|
|lvl|Personal Saving Rate (%)|
|∆ln|Total Consumer Credit Outstanding (SA)|
|∆ln|Home Mortgages - Liabilities - Balance Sheet of Households and Nonproft Organizations|
|∆ln|Household Sector: Liabilites: Household Credit Market Debt Outstanding|
|∆ln|Debt Outstanding Domestic Nonfnancial Sectors - Household, Consumer Credit Sector|
|∆ln|Debt Outstanding Domestic Nonfnancial Sectors - Household, Home Mortgage Sector|
|∆ln|Owners’Equity in Household Real Estate - Net Worth - Balance Sheet of Households and Nonproft Organizations|
|∆ln|Real Estate - Assets - Balance Sheet of Households and Nonproft Organizations|



###### Bond and exchange rates 

|∆lvl<br>Interest|Rate:|Federal F|unds|(Efective)|
|---|---|---|---|---|
|∆lvl<br>Interest|Rate:|U.S. Trea|sury|Bills, Sec. Mkt., 1-Mo.|
|∆lvl<br>Interest|Rate:|U.S. Trea|sury|Bills, Sec. Mkt., 3-Mo.|
|∆lvl<br>Interest|Rate:|U.S. Trea|sury|Bills, Sec. Mkt., 6-Mo.|
|∆lvl<br>Interest|Rate:|U.S. Trea|sury|Const. Maturities, 1-Yr.|
|∆lvl<br>Interest|Rate:|U.S. Trea|sury|Const. Maturities, 3-Yr.|
|∆lvl<br>Interest|Rate:|U.S. Trea|sury|Const. Maturities, 5-Yr.|
|∆lvl<br>Interest|Rate:|U.S. Trea|sury|Const. Maturities, 7-Yr.|
|∆lvl<br>Interest|Rate:|U.S. Trea|sury|Const. Maturities, 10-Yr.|
|∆lvl<br>Interest|Rate:|30-Year C|onve|ntional Mortgage Rate|
|∆lvl<br>Bond Y|ield: M|oody’s A|AA|Corporate|
|∆lvl<br>Bond Y|ield: M|oody’s B|AA C|orporate|
|lvl<br>Spread:|3m —|fed funds|||
|lvl<br>Spread:|6m —|fed funds|||
|lvl<br>Spread:|1y —f|ed funds|||
|lvl<br>Spread:|3y —f|ed funds|||
|lvl<br>Spread:|5y —f|ed funds|||
|lvl<br>Spread:|7y —f|ed funds|||
|lvl<br>Spread:|10y —|fed funds|||
|lvl<br>Spread:|AAA|—fed fund|s||
|lvl<br>Spread:|BAA|—fed fund|s||
|lvl<br>Spread:|BAA|—AAA|||
|∆ln<br>Foreign|Excha|nge Rate:|Can|adian Dollars to One U.S. Dollar|
|∆ln<br>Foreign|Excha|nge Rate:|Jap|anese Yen to One U.S. Dollar|
|∆ln<br>Foreign|Excha|nge Rate:|U.S.|Dollars to One British Pound|
|∆ln<br>Foreign|Excha|nge Rate:|Swis|s Francs to One U.S. Dollar|



31 

###### Prices 

- ∆ln Producer Price Index: Crude Materials for Further Processing (1982=100, SA) ∆ln Producer Price Index: Finished Consumer Foods (1982=100, SA) ∆ln Producer Price Index: Finished Goods (1982=100, SA) ∆ln Producer Price Index: Intermediate Materials: Supplies & Components (1982=100, SA) ∆ln Cpi-U: All Items (82-84=100, SA) ∆ln Cpi-U: Housing (82-84=100, SA) ∆ln Cpi-U: Transportation (82-84=100, SA) ∆ln Cpi-U: Commodities (82-84=100, SA) ∆ln Cpi-U: Durables (82-84=100, SA) ∆ln Cpi-U: Nondurables (82-84=100, SA) ∆ln Cpi-U: All Items Less Food (82-84=100, Sa) ∆ln Cpi-U: All Items Less Shelter (82-84=100, SA) ∆ln Spot Oil Price: West Texas Intermediate ∆ln Personal Consumption Expenditures: Chain-type Price Index (2005=100, SA) ∆ln Gross Domestic Product: Implicit Price Deflator (2005=100, SA) 

###### Stock market 

- ∆ln S&P Composite Index Level ∆ln Dow Jones Industrial Average 

32 

### References 

Aiolfi, M., Capistrán, C., & Timmermann, A. (2010). Forecast combinations. In: Clements, M. & Hendry, D., (Eds.), Forecast Handbook, Oxford. 

Bai, J., & Ng, S. (2002). Determining the number of factors in approximate factor models. Econometrica, 70, 191-221. 

Bai, J., & Ng, S. (2006). Confidence intervals for diffusion index forecasts and inference for factor-augmented regressions. Econometrica, 74, 1133-1150. 

Bai, J., & Ng, S. (2007). Determining the number of primitive shocks in factor models. Journal of Business & Economic Statistics, 25, 52-60. 

Boivin, J., & Ng, S. (2005). Understanding and comparing factor-based forecasts. International Journal of Central Banking, 1, 117-151. 

Brunnermeier, M. K., & Julliard, C. (2008). Money illusion and housing frenzies. Review of Financial Studies, 21, 135-180. 

Campbell, S. D., Davis, M. A., Gallin, J., & Martin, R. F. (2009). What moves housing markets: A variance decomposition of the rent-price ratio. Journal of Urban Economics, 66, 90-102. 

Case, K. E., & Shiller, R. J. (1989). The effi ciency of the market for single family homes. American Economic Review, 79, 125-137. 

Case, K. E., & Shiller, R. J. (1990). Forecasting prices and excess returns in the housing market. American Real Estate and Urban Economics Association Journal, 18, 253-273. 

Chamberlain, G., & Rothschild, M. (1983). Arbitrage, factor structure, and meanvariance analysis on large asset markets. Econometrica, 51, 1281-1304. 

Cochrane, J. H. (2007). Financial markets and the real economy. In: Mehra, R., The equity premium, North Holland Handbook of Finance Series, North Holland, Amsterdam. Cochrane, J. H. (2011). Discount rates. Joural of Finance, 66, 1047-1108 

Connor, G., & Korajczyk, R. A. (1986). Performance measurement with the arbitrage pricing theory: A new framework for analysis. Journal of Financial Economics, 17, 255-289. 

Doz, C., Giannone, D., & Reichlin, L. (2011a). A quasi maximum likelihood approach for large approximate dynamic factor models. Review of Economics and Statistics, forthcoming. 

Doz, C., Giannone, D., & Reichlin, L. (2011b). A two-step estimator for large approximate dynamic factor models based on Kalman filtering. Journal of Econometrics, forthcoming. 

33 

Fama, E. F., & Schwert, G. W. (1977). Asset returns and inflation. Journal of Financial Economics, 5, 115-146. 

Fama, E. F. (1981). Stock returns, real activity, inflation and money. American Economic Review, 71, 545-565. 

Favilukis, J., Van Nieuwerburgh, S., Ludvigson, S. (2012). The macroeconomic effects of housing wealth, housing finance, and limited risk-sharing in general equilibrium. Working paper. 

Forni, M., Hallin, M., Lippi, M., & Reichlin, L. (2000). The generalized dynamic factor model: Identification and estimation. Review of Economics and Statistics, 82, 540-554. 

Forni, M., Hallin, M., Lippi, M., & Reichlin, L. (2004). The generalised dynamic factor: Consistency and rates. Journal of Econometrics, 119, 231-255. 

Forni, M., Hallin, M., Lippi, M., & Reichlin, L. (2005). The generalized dynamic factor model: One sided estimation and forecasting. Journal of the American Statistical Association, 100, 830-840. 

Gallin, J. (2008). The long-run relationship between house prices and rents. Real Estate Economics, 4, 635-658. 

Geweke, J. (1977). The dynamic factor analysis of economic time series. In: Aigner & Golderger, Latent Variables in Socioeconomic Models, North Holland, Amsterdam. 

Gospodinov, N. & Ng, S. (2011). Commodity prices, convenience yields and inflation. Review of Economics and Statistics, forthcoming. 

Goyal, A., & Welch, I. (2003). Predicting the equity premium with dividend ratios. Management Science, 49, 639-654. 

Goyal, A., & Welch, I. (2008). A comprehensive look at the empirical performance of equity premium prediction. Review of Financial Studies, 21, 1455-1508. 

Hallin, M., & Liska, R. (2007). Determining the number of factors in the generalized factor model. Journal of the American Statistical Association, 102, 603-617. 

Jungbacker, B., & Koopman, S. J. (2008). Likelihood-based analysis for dynamic factor models. Working paper. 

Kim, C. J., & Nelson, C. R. (1999). State-Space Models with Regime Switching. The MIT Press. 

Ludvigson, S. C., & Ng, S. (2007). The empirical risk-return relation: A factor analysis approach. Journal of Financial Economics, 83, 171-222. 

Ludvigson, S. C., & Ng, S. (2009). Macro factors in bond risk premia. Review of Financial Studies, 22, 5027-5067. 

Ludvigson, S. C., & Ng, S. (2011). A factor analysis of bond risk premia. In: Ullah & 

34 

Giles, Handbook of Empirical Economics and Finance. 

Lustig, H., Roussanov, N., & Verdelhan, A. (2010). Countercyclical currency risk premia. Working paper. 

Otrok, C., & Whiteman, C. H. (1998). Bayesian leading indicators: Measuring and predicting economic conditions in Iowa. International Economic Review, 39, 997-1014. Patton, A., Politis, D. & White, H. (2009). Correction to “Automatic Block-Length Selection for the Dependent Bootstrap”by D. Politis and H. White, Econometric Reviews, 28, 372-375. 

Rapach, D. E., & Strauss, J. K. (2009). Differences in housing price forecastability across US states. International Journal of Forecasting, 25, 351-372. 

Sargent, T. J., & Sims, C. A. (1977). Business cycle modeling without pretending to have too much a priori economic theory. In Sims, New Methods in Business Cycle Research, Federal Reserve Bank on Minneapolis, 45-110. 

Stock, J. H., & Watson, M. W. (1998). Diffusion indexes. NBER Working paper 6702. Stock, J. H., & Watson, M. W. (2001). A comparison of linear and nonlinear univariate models for forecasting macroeconomic time series. In: Engle, R., White, H. (Eds.), Cointegration, Causality and Forecasting. A Festschrift in honour of Clive W.J. Granger, Oxford University Press, Oxford. pp. 1-44. 

Stock, J. H., & Watson, M. W. (2002a). Forecasting using principal components from a large number of predictors. Journal of the American Statistical Association, 97, 11671179. 

Stock, J. H., & Watson, M. W. (2002b). Macroeconomic forecasting using diffusion indexes. Journal of Business & Economic Statistics, 20, 147-162. 

Stock, J. H., & Watson, M. W. (2005). Implications of dynamic factor models for VAR analysis. Working paper 11467, National Bureau of Economic Statistics. 

Stock, J. H., & Watson, M. W. (2006). Forecasting with many predictors. In: Elliott, Graham, Granger, Clive, & Timmermann, Handbook of Forecasting, 20, 147-162. 

Stock, J. H., & Watson, M. W. (2008). Forecasting in dynamic factor models subject to structural instability. In: Castle & Shephard, The Methodology and Practice of Econometrics: A Festschrift in Honour of Professor David F. Hendry, Oxford University Press. 

Thom, R. (1985). The relationship between housing starts and mortgage availability. Review of Economics and Statistics, 67, 693-696. 

Timmermann, A. (2006). Forecast combinations. In: Elliott, G., Granger, C.W.J., Timmermann, A. (Eds.), Handbook of Economic Forecasting, vol. 1. Elsevier, Amsterdam. 

35 

Table 1. Summary statistics for estimated factors 

|i|AR1( <sup>ˆ</sup>fi,t)|R<sup>2</sup><br>i|~~�~~R2<br>i|
|---|---|---|---|
|1|0.74|28.0%|28.0%|
|2|0.79|12.5%|40.5%|
|3|0.47|9.3%|49.8%|
|4|0.11|5.9%|55.7%|
|5|0.69|5.4%|61.1%|
|6|0.46|4.9%|66.0%|
|7|0.41|3.8%|69.8%|
|8|0.40|2.1%|72.0%|
|9|−0.34|2.0%|74.0%|
|10|0.37|1.8%|75.8%|
|11|0.24|1.8%|77.6%|



AR1(f<sup>ˆ</sup> i,t) is the first-order autocorrelation coeffi cient of the ith estimated factor, while Ri<sup>2is the proportion of the total variance explained by the ith estimated factor as deter-</sup> mined by the i<sup>th</sup> eigenvalue divided by the sum of eigenvalues. 

36 

Table 2. In-sample results: slope coeffi cients, explanatory power, and bootstrap confidence intervals. 

||ˆf1,t|ˆf2,t|ˆf3,t|yt|¯R<sup>2</sup>|
|---|---|---|---|---|---|
||||h= 1|||
|OLS estimate|0.28|−0.30|−0.65|0.19|53.7%|
|Bootstrap C.I.|[0.01; 0.74]|[−0.79;−0.02]|[−1.66;−0.44]<br>h= 2|[0.03; 0.46]|[42.1%; 60.5%]|
|OLS estimate|0.78|−0.54|−1.08|0.20|49.3%|
|Bootstrap C.I.|[0.14; 1.76]|[−1.12;−0.10]|[−2.89;−0.78]<br>h= 4|[−0.14; 0.84]|[37.2%; 59.7%]|
|OLS estimate|1.29|−0.99|−1.23|0.90|53.2%|
|Bootstrap C.I.|[0.10; 3.27]|[−1.83;−0.24]|[−2.68;−0.94]<br>h= 8|[0.38; 2.24]|[43.2%; 65.1%]|
|OLS estimate|1.84|−2.31|−1.58|1.54|41.0%|
|Bootstrap C.I.|[−0.55; 6.28]|[−4.75;−0.66]|[−4.73;−0.85]|[0.84; 3.86]|[34.6%; 63.3%]|



This table reports results of predictive regressions for the h-quarter ahead real house price growth: yt+h = α + β1f<sup>ˆ</sup> 1,t + β2f<sup>ˆ</sup> 2,t + β3f<sup>ˆ</sup> 3,t + γyt + εt+h. For each regression, the table reports OLS estimates of the slope coeffi cients, 90% bootstrap confidence intervals, the adjusted R<sup>2</sup> -statistic, and 90% bootstrap confidence intervals for the adjusted R<sup>2</sup> - statistic. Coeffi cients in bold indicate statistical significance. 

37 

Table 3. Out-of-sample results: MSFE performance relative to the AR(SIC) benchmark. 

|Row|Model|Benchmark|h= 1|Hor<br>h= 2|izon<br>h= 4|h= 8|
|---|---|---|---|---|---|---|
|1|Three-factor model (SIC)|AR(SIC)|0.92|0.97|0.93|0.93|
|2|Fcst combi (SIC weights)|AR(SIC)|0.98|1.00|0.96|0.92|
|3|Fcst combi (MSFE weights)|AR(SIC)|0.98|1.00|0.95|0.92|
|4|Fcst combi (disc. MSFE weights)|AR(SIC)|0.98|1.00|0.94|0.91|



We use factor forecast combination using three weighting schemes. The first scheme is based on the Schwartz information criterion (SIC). The second scheme is based on the past MSFE performance. The third scheme is based on past discounted MSFE performance. We also report results for the augmented three-factor model. We compare with an autoregressive benchmark where the number of lags is recursively chosen based on the SIC criterion. The table reports the ratio of the mean-squared-forecast-error (MSFE) between the given model and the autoregressive benchmark, AR(SIC). 

38 

Table 4. Out-of-sample results: MSFE performance relative to other benchmarks. 

|||||Hor|izon||
|---|---|---|---|---|---|---|
|Row|Model|Benchmark|h= 1|h= 2|h= 4|h= 8|
|1|Three-factor model|(SIC)<br>AR(1)|0.75|0.77|0.78|0.98|
|2|Three-factor model|(SIC)<br>Mean|0.65|0.61|0.51|0.78|
|3|Three-factor model|(SIC)<br>Price-rent ratio|0.60|0.55|0.45|0.72|



The table reports the ratio of the mean-squared-forecast-error (MSFE) between the three-factor model and various benchmarks. 

39 

Figure 1: Real house price growth rate. 



<!-- Start of picture text -->
0.04<br>0.03<br>0.02<br>0.01<br>0<br>-0.01<br>-0.02<br>-0.03<br>-0.04<br>-0.05<br>Q1-80 Q1-90 Q1-00 Q1-10<br><!-- End of picture text -->

40 

Figure 2: Model fit. 



<!-- Start of picture text -->
0.04<br>y<br>Forecast of y<br>0.03<br>0.02<br>0.01<br>0<br>-0.01<br>-0.02<br>-0.03<br>-0.04<br>-0.05<br>Q1-80 Q1-90 Q1-00 Q1-10<br><!-- End of picture text -->

41 

Figure 3: R<sup>2</sup> between factor 1 and each individual series. Documents/Papers/WP/house prices/WP/graphics/RsquarePanelTr1.pdf 



<!-- Start of picture text -->
R−squared in pct.<br>IP: total<br>IP: final prod<br>IP: cons gds<br>IP: cons dble<br>IP: cons nondble<br>IP: bus eqpt<br>IP: matls<br>IP: dble matls<br>IP: nondble matls<br>IP: mfg<br>Real GDP 1 dec<br>IP: dur mfg<br>Real pers inc<br>Cap util total indus<br>Real disp pers inc<br>Pers inc excl transf<br>NAPM prod comp idx<br>Labor force > 16 yrs<br>Emp CPS total<br>Emp CPS nonag<br>Unemp > 16 yrs<br>U: mean duration<br>U < 5 wks<br>U 5-14 wks<br>U 15+ wks<br>U 15-26 wks<br>U 27+ wks<br>Emp: total<br>Emp: gds prod<br>Emp: mining<br>Emp: const<br>Emp: mfg<br>Emp: dble gds<br>Emp: nondbles<br>Emp: services<br>Emp: information<br>Emp: bus service<br>Emp: TTU<br>Emp: wholesale<br>Emp: retail<br>Emp: FIRE<br>Emp: Govt<br>Avg hrly earn<br>Avg hrs goods<br>Avg hrly earn goods<br>Avg hrs constr<br>Avg hrly earn Constr<br>Avg hrly earn mgf<br>NAPM emp<br>Starts: nonfarm<br>Starts: NE<br>Starts: MW<br>Starts: South<br>Starts: West<br>One fam houses − sold<br>New Homes sold<br>Median mth sales<br>Ratio house sale/sold<br>New housing units<br>New houses completed<br>PMI<br>NAPM new ordrs<br>NAPM vendor del<br>NAPM Invent<br>real PCE<br>M1<br>M2<br>Currency<br>C and I loans comm bank<br>Household credit debt<br>Banks consumer loans<br>Credit mkt: cons credit<br>Credit mkt: home mortg<br>US home mortgs − bal hholds<br>Owners equity hhold estate<br>Real estate bal hholds<br>Total consumer credit<br>Pers savings of disp inc<br>Real estate bal banks<br>Fed Funds (FF)<br>Cert. dep.  1m<br>Cert. dep.  3m<br>Cert. dep.  6m<br>1 yr CM T-bond<br>3 yr CM T-bond<br>5 yr CM T-bond<br>7 yr CM T-bond<br>10 yr CM T-bond<br>Aaa bond<br>Baa bond<br>Fixed mortg rate 30 yr<br>Cert. dep.  3m − FF<br>Cert. dep.  6m − FF<br>1 yr CM T-bond − FF<br>3 yr CM T-bond − FF<br>5 yr CM T-bond − FF<br>7 yr CM T-bond − FF<br>10 yr CM T-bond − FF<br>Aaa bond − FF<br>Baa bond − FF<br>Baa bond − Aaa bond<br>FX JP−US<br>FX US−UK<br>FX CAN−US<br>FX Sw−US<br>Spot oil price<br>PPI: crude matls<br>PPI: int materials<br>PPI finished cons goods<br>PPI: fin gds<br>CPI-U: all<br>CPI-U: transp<br>CPI-U: comm.<br>CPI-U: dbles<br>CPI-U: ex food<br>CPI-U: ex shelter<br>CPI−U non dur<br>CPI−U housing<br>GDP − price defl<br>PCE chain price idx<br>Dow Jones Industrial Average<br>SP 500 42<br>1<br>0 10 20 30 40 50 60 70 80 90 100<br>      Output and income<br>Labour Market<br>Housing<br>Consump./orders/inven.<br>Money/Credit p<br>Bonds/FX<br>Prices<br>Stocks<br><!-- End of picture text -->

##### Figure 4: R<sup>2</sup> between factor 2 and each individual series. Documents/Papers/WP/house prices/WP/graphics/RsquarePanelTr2.pdf 



<!-- Start of picture text -->
R−squared in pct.<br>IP: total<br>IP: final prod<br>IP: cons gds<br>IP: cons dble<br>IP: cons nondble<br>IP: bus eqpt<br>IP: matls<br>IP: dble matls<br>IP: nondble matls<br>IP: mfg<br>Real GDP 1 dec<br>IP: dur mfg<br>Real pers inc<br>Cap util total indus<br>Real disp pers inc<br>Pers inc excl transf<br>NAPM prod comp idx<br>Labor force > 16 yrs<br>Emp CPS total<br>Emp CPS nonag<br>Unemp > 16 yrs<br>U: mean duration<br>U < 5 wks<br>U 5-14 wks<br>U 15+ wks<br>U 15-26 wks<br>U 27+ wks<br>Emp: total<br>Emp: gds prod<br>Emp: mining<br>Emp: const<br>Emp: mfg<br>Emp: dble gds<br>Emp: nondbles<br>Emp: services<br>Emp: information<br>Emp: bus service<br>Emp: TTU<br>Emp: wholesale<br>Emp: retail<br>Emp: FIRE<br>Emp: Govt<br>Avg hrly earn<br>Avg hrs goods<br>Avg hrly earn goods<br>Avg hrs constr<br>Avg hrly earn Constr<br>Avg hrly earn mgf<br>NAPM emp<br>Starts: nonfarm<br>Starts: NE<br>Starts: MW<br>Starts: South<br>Starts: West<br>One fam houses − sold<br>New Homes sold<br>Median mth sales<br>Ratio house sale/sold<br>New housing units<br>New houses completed<br>PMI<br>NAPM new ordrs<br>NAPM vendor del<br>NAPM Invent<br>real PCE<br>M1<br>M2<br>Currency<br>C and I loans comm bank<br>Household credit debt<br>Banks consumer loans<br>Credit mkt: cons credit<br>Credit mkt: home mortg<br>US home mortgs − bal hholds<br>Owners equity hhold estate<br>Real estate bal hholds<br>Total consumer credit<br>Pers savings of disp inc<br>Real estate bal banks<br>Fed Funds (FF)<br>Cert. dep.  1m<br>Cert. dep.  3m<br>Cert. dep.  6m<br>1 yr CM T-bond<br>3 yr CM T-bond<br>5 yr CM T-bond<br>7 yr CM T-bond<br>10 yr CM T-bond<br>Aaa bond<br>Baa bond<br>Fixed mortg rate 30 yr<br>Cert. dep.  3m − FF<br>Cert. dep.  6m − FF<br>1 yr CM T-bond − FF<br>3 yr CM T-bond − FF<br>5 yr CM T-bond − FF<br>7 yr CM T-bond − FF<br>10 yr CM T-bond − FF<br>Aaa bond − FF<br>Baa bond − FF<br>Baa bond − Aaa bond<br>FX JP−US<br>FX US−UK<br>FX CAN−US<br>FX Sw−US<br>Spot oil price<br>PPI: crude matls<br>PPI: int materials<br>PPI finished cons goods<br>PPI: fin gds<br>CPI-U: all<br>CPI-U: transp<br>CPI-U: comm.<br>CPI-U: dbles<br>CPI-U: ex food<br>CPI-U: ex shelter<br>CPI−U non dur<br>CPI−U housing<br>GDP − price defl<br>PCE chain price idx<br>Dow Jones Industrial Average<br>SP 500 43<br>2<br>0 10 20 30 40 50 60 70 80 90 100<br>      Output and income<br>Labour Market<br>Housing<br>Consump./orders/inven.<br>Money/Credit p<br>Bonds/FX<br>Prices<br>Stocks<br><!-- End of picture text -->

Figure 5: R<sup>2</sup> between factor 3 and each individual series. Documents/Papers/WP/house prices/WP/graphics/RsquarePanelTr3.pdf 



<!-- Start of picture text -->
R−squared in pct.<br>IP: total<br>IP: final prod<br>IP: cons gds<br>IP: cons dble<br>IP: cons nondble<br>IP: bus eqpt<br>IP: matls<br>IP: dble matls<br>IP: nondble matls<br>IP: mfg<br>Real GDP 1 dec<br>IP: dur mfg<br>Real pers inc<br>Cap util total indus<br>Real disp pers inc<br>Pers inc excl transf<br>NAPM prod comp idx<br>Labor force > 16 yrs<br>Emp CPS total<br>Emp CPS nonag<br>Unemp > 16 yrs<br>U: mean duration<br>U < 5 wks<br>U 5-14 wks<br>U 15+ wks<br>U 15-26 wks<br>U 27+ wks<br>Emp: total<br>Emp: gds prod<br>Emp: mining<br>Emp: const<br>Emp: mfg<br>Emp: dble gds<br>Emp: nondbles<br>Emp: services<br>Emp: information<br>Emp: bus service<br>Emp: TTU<br>Emp: wholesale<br>Emp: retail<br>Emp: FIRE<br>Emp: Govt<br>Avg hrly earn<br>Avg hrs goods<br>Avg hrly earn goods<br>Avg hrs constr<br>Avg hrly earn Constr<br>Avg hrly earn mgf<br>NAPM emp<br>Starts: nonfarm<br>Starts: NE<br>Starts: MW<br>Starts: South<br>Starts: West<br>One fam houses − sold<br>New Homes sold<br>Median mth sales<br>Ratio house sale/sold<br>New housing units<br>New houses completed<br>PMI<br>NAPM new ordrs<br>NAPM vendor del<br>NAPM Invent<br>real PCE<br>M1<br>M2<br>Currency<br>C and I loans comm bank<br>Household credit debt<br>Banks consumer loans<br>Credit mkt: cons credit<br>Credit mkt: home mortg<br>US home mortgs − bal hholds<br>Owners equity hhold estate<br>Real estate bal hholds<br>Total consumer credit<br>Pers savings of disp inc<br>Real estate bal banks<br>Fed Funds (FF)<br>Cert. dep.  1m<br>Cert. dep.  3m<br>Cert. dep.  6m<br>1 yr CM T-bond<br>3 yr CM T-bond<br>5 yr CM T-bond<br>7 yr CM T-bond<br>10 yr CM T-bond<br>Aaa bond<br>Baa bond<br>Fixed mortg rate 30 yr<br>Cert. dep.  3m − FF<br>Cert. dep.  6m − FF<br>1 yr CM T-bond − FF<br>3 yr CM T-bond − FF<br>5 yr CM T-bond − FF<br>7 yr CM T-bond − FF<br>10 yr CM T-bond − FF<br>Aaa bond − FF<br>Baa bond − FF<br>Baa bond − Aaa bond<br>FX JP−US<br>FX US−UK<br>FX CAN−US<br>FX Sw−US<br>Spot oil price<br>PPI: crude matls<br>PPI: int materials<br>PPI finished cons goods<br>PPI: fin gds<br>CPI-U: all<br>CPI-U: transp<br>CPI-U: comm.<br>CPI-U: dbles<br>CPI-U: ex food<br>CPI-U: ex shelter<br>CPI−U non dur<br>CPI−U housing<br>GDP − price defl<br>PCE chain price idx<br>Dow Jones Industrial Average<br>SP 500 44<br>3<br>0 10 20 30 40 50 60 70 80 90 100<br>      Output and income<br>Labour Market<br>Housing<br>Consump./orders/inven.<br>Money/Credit p<br>Bonds/FX<br>Prices<br>Stocks<br><!-- End of picture text -->

**Research Papers 2012** 



- 2012-10: Peter Exterkate: Model Selection in Kernel Ridge Regression 

- 2012-11: Torben G. Andersen, Nicola Fusari and Viktor Todorov: Parametric Inference and Dynamic State Recovery from Option Panels 

- 2012-12: Mark Podolskij and Katrin Wasmuth: Goodness-of-fit testing for fractional diffusions 

- 2012-13: Almut E. D. Veraart and Luitgard A. M. Veraart: Modelling electricity day–ahead prices by multivariate Lévy 

- 2012-14: Niels Haldrup, Robinson Kruse, Timo Teräsvirta and Rasmus T. Varneskov: Unit roots, nonlinearities and structural breaks 

- 2012-15: Matt P. Dziubinski and Stefano Grassi: Heterogeneous Computing in Economics: A Simplified Approach 

- 2012-16: Anders Bredahl Kock and Laurent A.F. Callot: Oracle Inequalities for High Dimensional Vector Autoregressions 

- 2012-17: Eric Hillebrand, Huiyu Huang, Tae-Hwy Lee and Canlin Li: Using the Yield Curve in Forecasting Output Growth and Inflation 

- 2012-18: Eric Hillebrand and Tae-Hwy Lee: Stein-Rule Estimation and Generalized Shrinkage Methods for Forecasting Using Many Predictors 

- 2012-19: Bent Jesper Christensen, Morten Ørregaard Nielsen and Jie Zhu: The impact of financial crises on the risk-return tradeoff and the leverage effect 

- 2012-20: Hendrik Kaufmann, Robinson Kruse and Philipp Sibbertsen: On tests for linearity against STAR models with deterministic trends 

- 2012-21: Andrey Launov, Olaf Posch and Klaus Wälde: On the estimation of the volatility-growth link 

- 2012-22: Peter O. Christensen and Zhenjiang Qin: Information and Heterogeneous Beliefs: Cost of Capital, Trading Volume, and Investor Welfare 

- 2012-23: Zhenjiang Qin: Heterogeneous Beliefs, Public Information, and Option Markets 

- 2012-24: Zhenjiang Qin: Continuous Trading Dynamically Effectively Complete Market with Heterogeneous Beliefs 

- 2012-25: Heejoon Han and Dennis Kristensen: Asymptotic Theory for the QMLE in GARCH-X Models with Stationary and Non-Stationary Covariates 

- 2012-26: Lei Pan, Olaf Posch and Michel van der Wel: Measuring Convergence using Dynamic Equilibrium Models: Evidence from Chinese Provinces 

- 2012-27: Lasse Bork and Stig V. Møller: Housing price forecastability: A factor analysis 

