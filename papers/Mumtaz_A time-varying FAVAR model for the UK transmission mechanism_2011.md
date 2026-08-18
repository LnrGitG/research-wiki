---
title: Mumtaz_A time-varying FAVAR model for the UK transmission mechanism_2011
type: paper
source_pdf: raw/papers/Mumtaz_A time-varying FAVAR model for the UK transmission mechanism_2011.pdf
converted: 2026-08-18
---



<!-- Start of picture text -->
WORKING PAPER SERIES<br>NO 1320 / APRIL 2011<br>WHAT LIES BENEATH?<br>A TIME-VARYING<br>FAVAR MODEL<br>FOR THE UK<br>TRANSMISSION<br>MECHANISM<br>by Haroon Mumtaz,<br>Pawel Zabczyk<br>and Colin Ellis<br><!-- End of picture text -->









# **WORKING PAPER SERIES NO 1320 / APRIL 2011** 

**WHAT LIES BENEATH? A TIME-VARYING FAVAR MODEL FOR THE UK TRANSMISSION MECHANISM**<sup>**1**</sup> 

by Haroon Mumtaz<sup>2</sup> , Pawel Zabczyk<sup>3</sup> and Colin Ellis<sup>4</sup> 



NOTE: This Working Paper should not be reported as representing the views of the European Central Bank (ECB). The views expressed are those of the authors and do not necessarily reflect those of the ECB. 



In 2011 all ECB publications feature a motif taken from the €100 banknote. 

This paper can be downloaded without charge from http://www.ecb.europa.eu or from the Social Science Research Network electronic library at http://ssrn.com/abstract_id=1789603. 



1   The views expressed here are those of the authors and do not necessarily reflect those of the Bank of England or the Monetary Policy Committee. Note, that an earlier version of this paper appeared as a Bank of England Working Paper 364. For helpful comments and suggestions, we’d like to thank Jean Boivin, Alex Bowen, Bianca De Paoli, Stephen Millard, Miles Parker, Simon Price, Lucrezia Reichlin, Ricardo Reis, Garry Young, two anonymous referees and seminar participants at the 2008 MMF conference and the 2009 RES conference. All remaining errors are ours. 

2   Centre for Central Banking Studies, Bank of England. 3   Corresponding author: Bank of England and European Central Bank, Kaiserstrasse 29, D-60311 Frankfurt am Main, Germany; phone number: +49 69 1344 6819; e-mail: pawel.zabczyk@ecb.europa.eu 

4 University of Birmingham and BVCA. 

###### **© European Central Bank, 2011** 

###### **Address** 

Kaiserstrasse 29 60311 Frankfurt am Main, Germany 

###### **Postal address** 

Postfach 16 03 19 60066 Frankfurt am Main, Germany 

###### **Telephone** 

+49 69 1344 0 

###### **Internet** 

http://www.ecb.europa.eu 

###### **Fax** 

+49 69 1344 6000 

_All rights reserved._ 

_Any reproduction, publication and reprint in the form of a different publication, whether printed or produced electronically, in whole or in part, is permitted only with the explicit written authorisation of the ECB or the authors._ 

_Information on all of the papers published in the ECB Working Paper Series can be found on the ECB’s website, http://www. ecb.europa.eu/pub/scientific/wps/date/ html/index.en.html_ 

ISSN 1725-2806 (online) 

## **CONTENTS** 

|Abstrac|t|**4**|
|---|---|---|
|Non tec|hnical summary|**5**|
|1 Intr|oduction|**7**|
|2 The|empirical model|**9**|
|2.1|Identif cation of structural shocks|**11**|
|2.2|Estimation|**13**|
|2.3|Data|**14**|
|3 Res|ults|**15**|
|3.1|Model comparison|**15**|
|3.2|The Estimated factors and||
||stochastic volatility|**16**|
|3.3|Impulse response to a||
||monetary policy shock|**17**|
|4 For|ecast error variance decomposition|**26**|
|5 Con|clusions|**32**|
|Append|ices|**33**|
|Referen|ces|**47**|



ECB Working Paper Series No 1320April 2011 3 

###### Abstract 

This paper uses a time-varying Factor Augmented VAR to investigate the evolving transmission of monetary policy and demand shocks in the UK. Simultaneous estimation of time-varying impulse responses of a large set of macroeconomic variables and disaggregated prices suggest that the response of inflation, money supply and asset prices to monetary policy and demand shocks has changed over the sample period. In particular, during the post-1992 inflation targeting period, monetary policy shocks started having a bigger impact on prices, a smaller impact on activity and began contributing more to overall volatility. In contrast, demand shocks had the largest impact on these variables before the 1990s. We also document changes in the response of disaggregated prices, with the median reaction to contractionary policy shocks becoming more negative and the distribution more dispersed post-1992. 

Keywords: Transmission mechanism, monetary policy, Factor Augmented VAR, timevarying coefficients, sign restrictions. 

JEL classification: C38, E44, E52 

ECB 4 Working Paper Series No 1320April 2011 

### Non-technical Summary 

How does an economy respond when shocks hit it, or when policymakers change interest rates? And can those responses change over time, if the underlying structure of the economy changes? These questions are of critical importance to macroeconomists and monetary policy makers around the world, as they go to the heart of how interest rates can be used to underpin growth and enshrine price stability. Unfortunately, standard empirical models that are used to examine how economies behave, and how they respond to shocks, are often too small to accommodate the rich underlying tapestry of the economy, or too inflexible to allow for the fact that the economy may today respond very differently to an unexpected change in interest rates, compared with twenty or thirty years ago. 

In the past, economists have sometimes struggled to meet these challenges sufficiently well, for instance because they use small scale models — typically including three or four data series such as GDP, an inflation measure, and policy rates – that are easy to estimate but run the risk of misrepresenting the economy. In particular, these types of models often ignore asset prices or monetary aggregates, or only include them in a very limited fashion. This includes work that has tried to allow for the changing structure of the economy, as much of this literature only examines whether the dynamics of output or inflation have changed. 

This paper seeks to address these challenges using a relatively new type of statistical model, which encompasses lots of different information and data, but remains relatively straightforward to use. In addition, our modelling approach allows for changes in the underlying structure of the economy, rather than imposing one configuration over the whole of our sample. This flexible approach is important, as we address these challenges from a UK perspective, examining the behavior and response of the economy from 1975 to 2005. During this period the UK economy changed in many significant ways, not least in the shift to inflation targeting in 1992 following sterling’s exit from the European exchange rate mechanism (ERM), and the Bank of England’s subsequent independence in 1997. In light of this, the flexibility of our approach is a key strength, as is our ability to capture the rich variety of UK macroeconomic data that are available, which reduces the chance that our model is misspecified. 

Using quarterly UK data, we apply our modelling approach and uncover several important findings about the nature and structure of the UK economy. Using sign restrictions to identify two types of shocks — that is, constraining the initial response of variables to aggregate demand and monetary policy surprises — our results indicate that the structure of the UK economy has changed significantly, and suggest that models which do not allow for timevariation will be misleading. In addition, there is significant evidence that the shift to inflation targeting in 1992 had a material impact on the effectiveness of monetary policy: prior to that time, monetary policy appears to have had almost no impact on inflation, but after the change in regime inflation falls following an unexpected increase in interest rates. Furthermore, we observe that relative prices – the prices of individual goods and services, 

ECB Working Paper Series No 1320April 2011 5 

relative to the aggregate – are also more dispersed than prior to 1992. At the same time, unexpected movements in demand now appear to have far less impact on UK inflation than they did before 1992, suggesting that the move to inflation targeting affected the way that households and businesses have responded to shocks. And, in aggregate, monetary policy appears to have been much more important since 1992 in driving movements in output, inflation, monetary aggregates and asset prices than it was before the introduction of inflation targeting. 

Overall, our results suggest that the move to inflation targeting has had a clear and lasting impact on the structure of the UK economy, and possibly the behavior of firms and households. Unexpected movements in demand now have much less impact on the economy as a whole, consistent with the credibility of monetary policy. In addition, our model offers a new approach for policymakers who want to take time-variation seriously, while also allowing them to examine the impact of policy on a wide range of factors including equity prices, unemployment and money growth. 

ECB <mark>6</mark> Working Paper Series No 1320April 2011 

### 1 Introduction 

Over the last three decades, the United Kingdom has undergone major structural changes. These changes could have occurred at the same time as shifts in the properties of structural shocks and, arguably, both would have affected the transmission mechanism of policy.<sup>1</sup> Quantifying the impact of such changes and identifying the key factors driving them are of first-order importance for economists and policy-makers alike. To this end, this paper proposes an empirical model which allows for the simultaneous estimation of time-varying impulse responses of a large set of variables to structural shocks. 

The possibility of a changing transmission mechanism has been investigated for the UK largely via small scale vector autoregressions (VARs) that typically include three or four endogenous variables. For example, Benati (2008) uses a time-varying VAR in UK output, inflation, short-term interest rate and broad money and shows that there is little significant change (across time) in the response of these variables to a monetary policy shock. Similarly, Castelnuovo and Surico (2006) use a small scale VAR estimated on the pre and post-inflation targeting period to gauge the changing response of inflation to monetary policy shocks. 

Note that while these papers provide results for the changing dynamics of variables such as output and inflation, there is little existing evidence on the changing transmission of shocks to asset prices, measures of real activity other than GDP, measures of inflation other than CPI and RPI, different monetary aggregates and sectoral prices and quantities. In addition, Benati and Surico (2009) suggest that small-scale VARs may suffer from model misspecification — with omitted variables potentially distorting estimates of reduced form VAR coefficients or hindering the correct identification of structural shocks. 

The purpose of this paper is to re-examine the evolution of the UK monetary transmission mechanism using an empirical framework that incorporates substantially more information than the standard three or four variable-variable model used in most previous studies. In particular, we employ an extended version of the factor-augmented VAR (FAVAR) introduced in Bernanke et al. (2005). This model includes information from a large number of macroeconomic indicators representing various dimensions of the economy. Our extensions include allowing for time variation in the coefficients and stochastic volatility in the variances of the shocks. Our formulation has two clear advantages over previous studies: (i) we identify structural shocks using a model that incorporates around 350 macroeconomic and financial variables, hence making it less likely that our setup suffers from the shortcomings discussed above, (ii) our model allows us to estimate time-varying impulse responses for each of the variables contained in our panel. Therefore, we are able to derive results for the variation in responses of a wide variety of variables to the identified shocks. In particular, this paper 

> 1 A number of papers including Benati (2004), Mumtaz and Surico (2008) and Benati (2008) have shown that the 1970s and the 1980s were characterized by volatile inflation and output growth. In addition, the persistence of inflation was estimated to be high during this period. In contrast the period after the introduction of inflation targeting in 1992 was associated with low inflation and output volatility and low inflation persistence. 

ECB Working Paper Series No 1320April 2011 <mark>7</mark> 

not only provides evidence on the possible change in responses of the main macroeconomic variables, but also on the time-varying responses of components of the consumption deflator. 

The proposed time-varying FAVAR model is estimated on quarterly UK data spanning the period 1975-2005. We use sign restrictions to identify a monetary policy shock and an aggregate demand shock. Our main results are as follows: 

- Based on model selection criteria, a fixed coefficient FAVAR model is rejected in favor of the proposed model with time-varying parameters. 

- The response of inflation measures to a monetary policy shock is estimated to have changed substantially over the sample period. The pre-1992 response to a contractionary policy shock is estimated to be close to zero while the response over the inflation targeting period is negative and statistically significant. The response of money supply and the long-term government bond yield to this shock displays a similar pattern, with the post-1992 response larger in magnitude. 

- There is a substantial change in the response of inflation to an aggregate demand shock. While the response in the pre-1992 period to a positive demand shock was large and persistent, the inflation targeting regime is associated with a response which is smaller in magnitude. 

- There is evidence that moments of cross-sectional distribution of the response of disaggregated prices to a monetary policy shock have shifted over time. The median of the price distribution is more negative now than in the late 1970s. Similarly, the distribution is more dispersed than in the past. 

- Counterfactual experiments suggest that changes in the impulse response functions are linked to changes in the parameters of the FAVAR interest rate equation pointing to the role played by monetary policy. 

- A forecast error variance decomposition exercise indicates that the monetary policy shock became important for measures of real activity, inflation, money and asset prices after 1992, while the demand shock made an important contribution in the pre-1992 period. 

The paper is organized as follows: the next section presents the empirical model, section 3 discusses the estimated time-varying impulse responses to a monetary policy and demand shock, a time-varying forecast error variance decomposition is shown in section 4 and section 5 concludes. 

ECB 8 Working Paper Series No 1320April 2011 

### 2 The Empirical Model 

Consider any model based on the standard, three-equation New Keynesian core. Bernanke et al. (2005) argue that assumptions made about the information structure are crucial when deciding whether the dynamics of such a model can be described by a vector autoregression. In particular, if it is assumed that the specific data series included in the VAR correspond exactly to the model variables and are observed by the central bank and the econometrician, then the VAR model provides an adequate description of the theoretical model. However, both these assumptions are difficult to justify. First, measurement error implies that measures of inflation and output are less than perfect proxies for model variables. Of course, this problem is much more acute for unobserved variables such as potential output. Furthermore, for broad concepts like economic activity and inflation there exists a multitude of observable indicators none of which will be able to match the theoretical construct precisely. Second, it is highly likely that the researcher only observes a subset of the variables examined by the monetary authority. 

Note that measurement error and omitted variables can potentially affect small-scale VAR analyses of changes in the transmission of structural shocks quite acutely. When examining time variation in impulse responses, the assumptions about the measurement of model variables and the information set used by model agents apply at each point in time and are more likely to be violated. If important information is excluded from the VAR, this can affect inference on the temporal evolution of impulse responses and lead to misleading conclusions about changes in the transmission mechanism. 

The obvious solution to this problem is to try and include more variables in the VAR. However, the degrees of freedom constraint becomes binding quite quickly in standard datasets.<sup>2</sup> Bernanke et al. (2005) suggest a more practical solution. They propose a ‘Factor-Augmented’ VAR (FAVAR) model, where factors from a large cross section of economic indicators are included as extra endogenous variables in a VAR.<sup>3</sup> These factors proxy the information set of the central bank (part of) which may have been inadvertently excluded from the small scale VAR model. We extend the FAVAR model along two dimensions. 

- First, we allow the dynamics of the system to be time-varying to capture changes in the propagation of structural shocks as a result of shifts in private sector behavior and/or monetary policy preferences. 

- Second, our specification incorporates heteroscedastic shocks which account for variations in the volatility of the underlying series. 

This extended FAVAR model provides a flexible framework to examine changes in the transmission of structural shocks. Moreover, our time-varying FAVAR model is less susceptible to 

> 2 This problem is even more acute in time-varying VARs as they usually impose a stability constraint (at each point in time) and this is less likely to be satisfied as the number of variables in the VAR increases. 

> 3 See also Forni and Gambetti (2010) for a recent application to US data based on sign-restrictions. 

ECB Working Paper Series No 1320 April 2011 

9 

problems created by omitted variables and therefore provides a robust framework to examine changes in the transmission mechanism. As we discuss below, the results obtained from our model differ substantially from those obtained using a standard small-scale time-varying VAR. 

More formally, our FAVAR model for the UK economy can be written in state space form. Consider first the observation equation 



where Xt is a panel of variables that contain information about real activity, inflation, money and asset prices in the UK (see data subsection below) while Ft<sup>1toF K</sup> t denote the K latent factors. We assume that these factors capture the dynamics of the UK economy and the Λ’s denote the factor loadings. Along similar lines as in Bernanke et al. (2005) the bank rate Rt is the ‘observed factor’. We stress that the structure of the loading matrix implies that some of the variables are allowed to have a contemporaneous relationship with the short term interest rate — i.e. Ψ = 0 for data series that are expected to react promptly to monetary policy actions. 

As we describe below, time variation is introduced into the model by allowing for drift in the coefficients and the error covariance matrix of the transition equation. Note that an alternative way of modelling time variation is to allow the factor loadings (Λ and Ψ) to drift over time.<sup>4</sup> There are, however, several reasons why we do not adopt this alternative specification. First, such a setup implies that any time variation in the dynamics of each factor and the volatility of shocks to each factor is driven entirely by the drift in the associated factor loading. This assumption is quite restrictive, especially as it only allows changes in the mean and persistence of each factor to occur simultaneously with changes in the volatility of the shocks. Second, this model implies a much larger computational burden as the Kalman filter and a backward recursion have to be employed for each underlying series. Finally, apart from the computational costs, this specification implies that the dynamics of observed factors are time invariant and, in particular, that the central bank always reacts in the same way to the "state of the economy" (captured by the latent factors). Such an assumption is hard to justify given our sample period (1975Q1 to 2005Q1) and would be rather restrictive in a model designed to investigate the changing impact of monetary policy. 

Equally, allowing for time variation in both, the factor loadings and the coefficients of the transition equation would entail serious identification problems since there would be three time-varying unobserved components, i.e. Γt = [Λt, Ψt], φt and Ft. However, substituting 

> 4 See Del Negro and Otrok (2008) for this kind of approach in a different context. 

ECB 10 Working Paper Series No 1320April 2011 

the transition equation (2) into the observation equation (1) imparts a restricted form of time variation also in the factor loadings. This interaction between the loadings and the time-varying coefficients of the factors has the potential to generate rich dynamics for the impulse response functions of the underlying series. 

As described below, time-variation is introduced into the model by allowing for drift in the coefficients and the error covariance matrix of the transition equation. More specifically, the transition equation of the system is a time-varying VAR model of the following form 



where Zt = {Ft<sup>1, F</sup> t<sup>2, ..F</sup> t<sup>K, Rt}andLisfixedat2.Wefurtherpostulatethefollowinglawof</sup> motion for the coefficients φ 



and the innovation (vt) covariance matrix is factored as 



where the time-varying matrices Ht and At evolve as random walks. 

The model described by equations 1 and 2 can incorporate a large amount of information about the UK economy. In particular, if the factors in equation 1 contain relevant information not captured by the three variables used in ‘standard’ VAR studies (eg Primiceri (2005)) then one might expect structural shocks identified within the current framework to be more robust. Our flexible specification for the transition equation also implies that the model accounts for the possibility of structural breaks in the dynamics that characterize the economy. 

#### 2.1 of Structural Shocks 

We identify two shocks: a monetary policy shock, and an aggregate demand shock. Following Canova and Nicolo (2002) and Uhlig (2005), the shocks are identified by placing contemporaneous sign restrictions on the response of some of the variables in Xt to an innovation to Rt. Our procedure works as follows: let Ωt =PtPt<sup>�betheCholeskydecompositionoftheVAR</sup> covariance matrix Ωt, and let A<sup>˜</sup> 0,t ≡ Pt. We draw an N × N matrix, J, from the N (0, 1) distribution. We take the QR decomposition of J, which gives us a candidate structural impact matrix as A0,t = A<sup>˜</sup> 0,tQ. Next we compute the contemporaneous impulse response of 

ECB Working Paper Series No 1320April 2011 11 



Figure 1: Impulse response to a monetary policy shock (top panel) and demand shock (bottom panel) using the model in Lubik and Schorfheide (2006). 

X1,t, ...XN,t as 



where ΔXi,t denotes the response of the i-th variable. We check if these satisfy our sign restrictions. If this is the case we store A0,t and repeat the procedure until we have 100 A0,t matrices that satisfy the sign restrictions. Out of these 100 stored A0,t matrices we retain the matrix with elements closest to the median across these 100 estimates. If the contemporaneous sign restrictions are not satisfied, we draw another J and repeat the above. 

We motivate our sign restrictions using a structural, two-country model described in Lubik and Schorfheide (2006) — an estimated, open-economy extension of the standard, threeequation New Keynesian workhorse. The model-implied impulse responses to monetary policy and demand shocks are given in figures 1. In light of these impulse responses we impose the following: (1) contractionary monetary policy shocks are assumed to increase R, reduce GDP growth, reduce inflation and lead to a nominal effective exchange rate appreciation on impact; (2) positive demand shocks have a positive contemporaneous impact on GDP growth, inflation and the nominal rate. With this minimal set of restrictions, we are able to disentangle the two structural shocks. 

Our identification method has a number of advantages over Bernanke et al.’s (2005) recursive scheme. First, contemporaneous sign restrictions allow us to be relatively ‘agnostic’ about the impact of structural shocks (beyond the contemporaneous effects) while simultaneously 

ECB 12 Working Paper Series No 1320April 2011 

imposing more structure than a Cholesky decomposition. Second, by using our identification scheme we are able to easily identify structural shocks other than those to monetary policy. 

#### 2.2 Estimation 

We estimate the model using Bayesian methods. A detailed description of the prior and posterior distributions is provided in the appendix. Here we summarize the estimation algorithm. The Gibbs sampler cycles through the following steps: 

1. Given initial values for the factors, simulate the VAR parameters and hyperparameters 

   - The VAR coefficients φt and the off-diagonal elements of the covariance matrix αt are simulated by using the methods described in Carter and Kohn (1994) 

   - The volatilities of the reduced form shocks Ht are drawn using the date by date blocking scheme introduced in Jacquier et al. (2002). 

   - The hyperparameters are drawn from their respective distributions. 

2. Given initial values for the factors draw the factor loadings (Λ and Ψ) and the variance of the idiosyncratic components. 

   - Given data on Rt and Xi,t standard results for regression models can be used and the coefficients and the variances are simulated from a normal and inverse gamma distribution. 

3. Simulate the factors conditional on all the other parameters 

   - This is done in a straightforward way by employing the methods described in Bernanke et al. (2005) and Kim and Nelson (1999). 

4. Go to step 1. 

We use 55,000 iterations in this MCMC algorithm discarding the first 45,000 as burn-in. The cumulated means of the retained draws (see appendix) show little variation which provides some evidence of algorithm convergence. 

##### 2.2.1 Computation of Impulse Response Functions 

We calculate the impulse responses Δt of Ft<sup>1, F</sup> t<sup>2, ...F</sup> t<sup>K</sup> and Rt to the monetary policy shock and the demand shock for each quarter. With these in hand, the time-varying impulse 

ECB Working Paper Series No 1320April 2011 13 

responses of each underlying variable can be easily obtained using the observation equation (1) of the model. That is, the impulse responses of X1,t, ...XN,t are computed as: 



Given the presence of time-varying parameters in the transition equation, computation of impulse response functions has to take into account the possibility of parameter drift over the impulse response horizon. Therefore, following Koop et al. (1996), we define the impulse response functions at each date as Δt 



where Ξ denotes all the parameters and hyperparameters of the VAR and k is the horizon under consideration. Equation (5) states that the impulse response functions are calculated as the difference between two conditional expectations. The first term in equation (5) denotes a forecast of the endogenous variables conditioned on a monetary policy shock μMP . The second term is the baseline forecast, i.e. conditioned on the scenario where the monetary policy shock equals zero. Therefore, in effect, equation (5) integrates out future uncertainty in the VAR parameters. The conditional expectations in (5) are computed via Monte Carlo integration for 1000 replications of the Gibbs sampler. Details on the Monte Carlo integration procedure can be found in Koop et al. (1996). 

#### 2.3 Data 

Our dataset is quarterly running from 1964 Q1 to 2005 Q1. As described in the appendix, we use the first 40 observations as a training sample with the estimation carried out starting 1975Q1. The dataset comprises around 60 macroeconomic UK data series. It includes activity measures such as GDP, consumption and industrial production, various price measures including RPI, CPI and the GDP deflator, as well as money and asset price data. In addition to these macro variables, we included a large number of disaggregated deflator and volume series for consumers’ expenditure. The Office for National Statistics (ONS) publishes around 140 subcategories of consumer expenditure data both in volume and deflator terms, going back to the 1960s. This gives us a ready-made collection of consistent disaggregated price (and volume) data over a long time period. Further details on the dataset are provided in the appendix to the paper. 

ECB 14 Working Paper Series No 1320April 2011 

||DIC|¯D|pD|
|---|---|---|---|
|Time-varying parameter FAVAR with 1 factor|20199|19481|718|
|Fixed coefcients FAVAR with 1 factor|42107|41757|350|
|Time-varying parameter FAVAR with 2 factors|15715|14654|1061|
|Fixed coefcients FAVAR with 2 factors|35905|35225|680|
|Time-varying parameter FAVAR with 3 factors|22956|18330|4626|
|Fixed coefcients FAVAR with 3 factors|33214|32271|943|



Table 1: Model Comparison via DIC. Best fit indicated by lowest DIC. 

### 3 Results 

#### 3.1 Model Comparison 

In order to select the number of latent factors and to assess the importance of time-variation that we introduce in the parameters of the FAVAR model, we compare our benchmark model (see equation 1) with a version of the model that assumes fixed parameters via the deviance information criterion (DIC). The DIC is a generalization of the Akaike information criterion — it penalizes model complexity while rewarding fit to the data. The DIC is defined as 

##### DIC = D<sup>¯</sup> + pD. 

The first term D<sup>¯</sup> = E (−2 ln L (Ξi)) = M1 �i<sup>(−2 ln L (Ξi))whereL (Ξi)isthelikelihood</sup> evaluated at the draws of all of the parameters Ξi in the MCMC chain. This term measures goodness of fit. The second term pD is defined as a measure of the number of effective parameters in the model (or model complexity). This is defined as pD = E (−2 ln L (Ξi)) − (−2 ln L (E(Ξi))) and can be approximated as pD = M1 �i<sup>(−2 ln L (Ξi))−</sup> −2 ln L M1 � Ξi .<sup>5</sup> � � i �� Note that the model with the lowest estimated DIC is preferred. 

Estimation of the DIC requires evaluating the likelihood function for each MCMC iteration.<sup>6</sup> Calculation of the likelihood function for the time-varying FAVAR with stochastic volatility is complicated due to the non-linear interaction of the volatility with levels in equation 2. We use a particle filter to evaluate the likelihood for each Gibbs draw. The Appendix presents a brief description of the particle filtering procedure. 

Table 1 presents the estimated DIC for the time-varying parameter and fixed coefficient FAVAR.<sup>7</sup> In general model complexity (pD) is lower for the fixed coefficient FAVAR models. 

> 5 The first term in this expression is an average of −2 times the likelihood function evaluated at each MCMC iteration. The second term is (−2 times) the likelihood function evaluated at the posterior mean. 

> 6 The main advantage of DIC over Bayes factors is the difficulty in the accurate computation of the marginal likelihood in complex models. Although Monte Carlo-based methods such as the harmonic mean estimator can be used, the estimates tend to be influenced by outlying values of MCMC draws and can be inaccurate. The method described in Chib (1995) requires an additional Gibbs simulation for each parameter making its implementation difficult for the time-varying parameter model. 

> 7 Note that we limit the maximum number of factors to 3 for computational reasons. As common in the 

ECB Working Paper Series No 1320April 2011 15 



Figure 2: The estimated factors, the bank rate and the stochastic volatility of shocks to each transition equation. 

However, this comes at the cost of model fit with D<sup>¯</sup> estimated to be substantially larger for the fixed coefficient models. The DIC is minimized for the time-varying FAVAR with two factors and this model is used in the analysis below. 

#### 3.2 The Estimated Factors and Stochastic Volatility 

The top left panels of figure 2 plot the estimated factors and the associated 68% error bands. Factor 2 is highly correlated with inflation measures in our dataset with a correlation of over -0.9 with CPI inflation and other inflation measures such as the change in the consumption deflator and the GDP deflator. Factor 2 also displays a reasonable correlation with GDP growth of around 0.4. This suggests that this factor captures the evolution of inflation and real activity in our dataset. On the other hand Factor 1 is highly correlated with financial variables included in our dataset, with the highest correlation ( of 0.97) with the five year government bond yield. 

The factors are quite precisely estimated with the volatility of the shocks to their transition equations estimated to be high during the 1970s and the 1980s. However this volatility 

literature we require the time-varying transition equation of the FAVAR to be stable at each point in time. This constraint becomes very difficult to impose when the number of endogenous variables in equation 2 exceeds 4. Note that this computational constraint also prevents us from considering lag lengths longer than 2. 

ECB 16 Working Paper Series No 1320April 2011 



Figure 3: Volatility of the identified structural shocks. 

declines substantially in the post-1985 period confirming the phenomenon referred to as the great moderation. The shock to the Bank rate equation was at its most volatile during the late 1970s. This volatility declined during the Thatcher dis-inflation of the early 1980s. The independence of the Bank of England saw a further decline in this volatility, with the variance close to zero over the period 1992-2005. 

Figure 3 plots the estimated standard deviation of the structural shocks. This is calculated ¯ 1/2 at each point in time as �A<sup>−</sup> 0,t<sup>1�ΩtA¯−</sup> 0,t<sup>1</sup> � where A<sup>¯</sup> 0,t is the A0,t matrix with the elements divided by the diagonal of this matrix. The estimates of the shock volatilities show a similar pattern — the volatility is high before the early 1990s with the inflation targeting period associated with the lowest variance. 

#### 3.3 Impulse Response to a Monetary Policy Shock 

##### 3.3.1 Aggregate Series 

Figure 4 plots the cumulated response of (the quarterly growth rate of) real activity indicators to a monetary policy shock normalized to increase the Bank rate by 100 basis points in the contemporaneous period (the time-varying response of the Bank rate to this shock is shown in figure 5). The left panel of the figure plots the median response in each quarter. The middle two panels display the median response and the 68% confidence interval over the pre and post-1992 period. Note that the post-1992 period coincides with the adoption of inflation targeting in the United Kingdom and this is generally regarded as the most significant change (since the 1970s) to the monetary framework. Therefore, we present the average impulse response in these two periods as a way to assess if this change in the monetary framework was associated with a change in the transmission of structural shocks. To gauge the significance 

ECB Working Paper Series No 1320April 2011 17 



Figure 4: Impulse response of real activity to a monetary policy shock. The left panels present the time-varying median cumulated impulse response. The middle three panels show the average impulse response functions in the pre and post-1992 period and their difference, while the last panel shows the joint distribution of the cumulated response at the one year horizon in the pre and post-1992 period. 

ECB 18 Working Paper Series No 1320April 2011 



Figure 5: Time-Varying impulse response of the bank rate to the monetary policy shock. 

of any difference across these sub-periods, we present two additional pieces of information. The fourth panel of the figure plots the difference in the impulse response across the two sub-periods. The final panel plots the estimated joint distribution of the cumulated impulse response (at the 4 quarter horizon) pre and post-1992. Note that systematic differences result in the points not being distributed symmetrically around the 45 degree line.<sup>8</sup> 

The contractionary policy shock reduces GDP by around 0.2% after one year in the pre-1992 period. The post-1992 response is very similar with the joint distribution concentrated on the 45-degree line The median response of industrial production and consumption is around 0.5% at the one year horizon in the pre-1992 period with some evidence that the magnitude of the response is somewhat larger in the post-1992 period. The response of consumption shows a similar pattern, although the change in the magnitude of the response in the post-1992 period is not statistically significant. The response of investment is imprecisely estimated. The cumulated response of aggregate quarterly inflation measures to the monetary contrac- 

> 8 A similar method has been used, for example, in Cogley et al. (2010). 

ECB Working Paper Series No 1320April 2011 <mark>19</mark> 



Figure 6: Impulse response of inflation to a monetary policy shock. The left panels present the time-varying median cumulated impulse response. The middle three panels show the average impulse response functions in the pre and post-1992 period and their difference, while the last panel shows the joint distribution of the cumulated response at the one year horizon in the pre and post-1992 period. 

tion is presented in figure 6. In contrast to the response of real activity, the impulse response of inflation measures shows significant time-variation. The response of inflation measures is small and statistically insignificant in the pre-1992 period and large, negative and persistent during the inflation targeting period. The shift appears to be systematic, with the difference in the pre and post-1992 response significantly different from zero (and the joint distribution largely concentrated to the right of the 45 degree line). 

Note that one aspect of these results is in contrast to those presented in Castelnuovo and Surico (2006) and Benati (2008) — i.e. our estimates are not characterized by a (statistically significant) price-puzzle during the 1970s as reported in these papers. This possibly reflects the fact that the identification of the monetary policy shock is more robust in our FAVAR model on account of it containing more information than the small scale models used in 

ECB 20 Working Paper Series No 1320April 2011 



Figure 7: Impulse response of money to a monetary policy shock. The left panels present the time-varying median cumulated impulse response. The middle three panels show the average impulse response functions in the pre and post-1992 period and their difference, while the last panel shows the joint distribution of the cumulated response at the one year horizon in the pre and post-1992 period. 

Castelnuovo and Surico (2006). However, as in Castelnuovo and Surico (2006) and Benati (2008) the price response is more negative over a policy regime associated with a higher degree of activism in response to inflation. Castelnuovo and Surico (2006) argue that this change in the response of inflation, reflects an underlying change in the monetary authorities’ response to inflation, with higher activism consistent with a stronger negative response and an absence of the price puzzle. The increase in the magnitude of the response during the inflation targeting period is consistent with those arguments. 

Figure 7 presents the response of broad money (M4 aggregate) and credit (M4 lending) growth to a monetary contraction. The estimates display a very similar pattern to those presented for inflation above. Generally, the (negative) response of M4 and M4 lending growth is stronger and more persistent in the post-1992 period, which is in line with the results reported in Benati (2008). A potential rationale for the ‘liquidity puzzle’ of the 70s and apparent instability of short-run money demand documented in figure 7 is developed in the theoretical paper of Alvarez and Lippi (2009). 

The cumulated response of some key asset prices is shown in figure 8. The response of house prices shows little change over time with a decline of around 2% over the sample period. The FTSE reaction is somewhat stronger in the post-1992 period. Similarly, the NEER responds more to the policy shock in the post-1992 period. The response of the 10 year government bond yield shows the largest variation. In the pre-1992 period the cumulated fall in the yield is less than 1000 basis points in response to the policy shock (this corresponds to a 10 percentage point change). In the post-1992 period the magnitude almost doubles at the two year horizon with the joint distribution in the final column of the figure concentrated 

ECB Working Paper Series No 1320April 2011 <mark>21</mark> 



Figure 8: Impulse response of asset prices to a monetary policy shock. The left panels present the time-varying median cumulated impulse response. The middle three panels show the average impulse response functions in the pre and post-1992 period and the difference, while the last panel shows the joint distribution of the cumulated response at the one year horizon in the pre and post-1992 period. 

to the right of the 45-degree line. This may reflect the fact that monetary policy was more credible during the inflation targeting period resulting in a larger response of inflation expectations implicitly reflected in the long term government bond yield. Note that a similar result is reported by Bianchi et al. (2009) who use a VAR model with yield curve factors to characterize yield curve dynamics. 

##### 3.3.2 Response of the Components of the Consumption Deflator 

Our panel dataset comprises around 140 components of the consumption deflator. As in Boivin et al. (2009) our methodology allows us to derive the response of each of these series to a monetary policy shock. Moreover, we are also able to examine how the distribution of consumption deflator responses (across expenditure categories) has evolved over time. 

ECB 22 Working Paper Series No 1320April 2011 



Figure 9: Changes in the distribution of the consumption deflator across time. 

Figure 9 tracks the evolution of cross-sectional characteristics of the price level. The top left panel shows the evolution of the median response of the consumption deflator, which has clearly undergone a marked change. More specifically, in the pre-1992 period, although the price level initially falls in reaction to the monetary contraction, the fall is short-lived with the response becoming positive at longer horizons. This is in contrast to the post-1992 estimates where the median price level declines significantly. These results again point to the possible role of the changing monetary regime (see Castelnuovo and Surico (2006)). 

Notably, the change in the median of the distribution is also associated with an increase in dispersion with the standard deviation (at longer horizons) higher during the 1990s. This means that although the median response is strongly negative in the current period, prices are more dispersed 20 quarters after the shock than during the 1980s. There is little systematic change in the skewness of the estimated distribution (not reported). 

##### 3.3.3 Impulse Response to Demand Shocks 

Figure 10 shows the cumulated response of selected variables to the identified demand shock. The shock is normalized to increase GDP growth by 1% (in the initial period) at all dates in the sample. The cumulated response of industrial production shows little change across the sample period. On the other hand, the cumulated response of CPI inflation to the demand shock does change significantly. In particular, the median response of inflation in the post 1992 period is about half the magnitude of the pre-1992 response. Again, this could be related to changes in the monetary regime with inflation expectations possibly more firmly anchored under inflation targeting. Note that similar results for the US are reported in Leduc et al. (2007). 

The pattern of the median response for money growth is similar to the results obtained for inflation. Finally, the post-1992 response of the long term government bond yield is smaller 

ECB Working Paper Series No 1320April 2011 <mark>23</mark> 



Figure 10: Impulse response to a demand shock. The left panels present the time-varying median cumulated impulse response. The middle three panels show the average impulse response functions in the pre and post-1992 period and their difference, while the last panel shows the joint distribution of the cumulated response at the one year horizon in the pre and post-1992 period. 

ECB 24 Working Paper Series No 1320April 2011 



Figure 11: Impulse response to a monetary policy shock: actual and counterfactual. 

than during the earlier period, again possibly reflecting the impact of the new monetary regime in anchoring inflation expectations. 

##### 3.3.4 A Counterfactual Experiment to Assess the Role of Monetary Policy 

The estimated impulse response function reported above show significant time-variation in the responses of several key variables. The timing of these changes coincides with the onset of inflation targeting in the early 1990s and provides some prima facie evidence for the role played by policy. However, in order to explore this issue further, we use the estimated TVP-FAVAR to carry out a simple counterfactual experiment which aims to highlight the role of changes in the policy equation in driving the observed IRF shifts. The experiment involves the following steps: (a) denote the pre-1992 period sample1 and the post-1992 period sample2. For each Gibbs sampling replication we draw randomly from the lagged and contemporaneous coefficients and volatility associated with the transition equation of the model (equation 2) in sample 1. (b) we then consider two counterfactual paths for the 

ECB Working Paper Series No 1320April 2011 <mark>25</mark> 

parameters of equation 2. In the first case the elements of the interest rate equation are fixed at all time periods at the value of the corresponding parameters drawn in step (a). In the second case, the elements of the non-interest rate equations are fixed at those drawn from sample 1. (c) using these counterfactual parameters we estimate the impulse response of key variables at each point in time. The aim is to compare these counterfactual impulse response functions with the actual estimates. If changes in the parameters of the FAVAR policy rule are important then the impulse response functions estimated under case 1 in step b should not be characterized by the shifts across time evident in the actual estimated responses. Similarly, if the change in the parameters of the non-policy block of the FAVAR is important, then the counter factual impulse responses under case 2 should have have a different time-path than the actual estimates.<sup>9</sup> 

Figure 11 shows the main results. The left column of the figure shows the actual estimated (cumulated) response of inflation, GDP growth, M4 and the 10 year government bond yield. The middle panel shows the estimated response under the assumption that the parameters of the FAVAR policy rule are fixed at values prevailing in the pre-1992 period. The final column shows the estimated response under the scenario that the parameters of the nonpolicy equations are fixed at values prevailing in the pre-1992 period. It is immediately clear from the second column of the figure that once the policy rule is constrained at pre-1992 values, the changes seen in the magnitude of actual impulse responses post-1992 disappear. In particular, the counterfactual response of inflation, money and the bond yield does not increase in magnitude over the inflation targeting period which is in sharp contrast to the actual estimates. Note from the third column that this is not the case when the non-policy block of the FAVAR is constrained with the estimated responses showing a pattern very similar to the actual estimates. These results support the conclusion that the reported changes in impulse response functions are largely driven by changes in the parameters of the FAVAR policy rule. 

Figure 12 provides further evidence along these lines. The figure shows the moments of the distribution of the impulse response of the consumption deflator (to a monetary policy shock) estimated under the counterfactual scenario that the parameters of the FAVAR policy rule are fixed at values prevailing in the pre-1992 period. In contrast to the estimates shown in figure 9, there is no shift in the median or the standard deviation of the distribution in the post-1992 period. 

### 4 Forecast Error Variance Decomposition 

In order to assess the relative importance of identified structural shocks, we calculate the time-varying forecast error variance decomposition. Figure 13 shows the median decompo- 

> 9 Notably, this experiment is not immune to the Lucas critique as we are unable to take into account the expectation effects of the assumed parameter changes. 

ECB <mark>26</mark> Working Paper Series No 1320April 2011 



Figure 12: Changes in the distribution of the consumption deflator across time (counterfactual estimates). 

sition for real activity indicators. Note that the X-axis of each panel represents the timeperiods, the Y-axis is the horizon in quarters while the Z-axis is the contribution to the forecast error variance. The monetary policy shock makes an important contribution to real activity indicators during the 1980s and the 1990s. The demand shock is less important on average but contributes around 20% during the mid 1980s and the end of the sample period. 

For inflation indicators (see figure 14) the demand shock contributes the most in the preinflation targeting period, (especially the 1980s) explaining about 30% to 40% of the forecast error variance of inflation indicators. Over the inflation targeting period, the contribution of this shock is less than 10%. In contrast, the monetary policy shock appears to contribute more to inflation measures during the mid-1980s and the early 1990s. 

Figure 15 plots the time-varying variance decomposition for money and credit growth. It is interesting to note that the contribution of monetary policy shocks increases substantially after 1990 rising to around 60%. In contrast, demand shocks are more important during the 1970s and 1980s. 

The monetary policy shock appears to be more important in terms of explaining the forecast error variance of the nominal exchange rate and the 10 year government bond yield after the 1990s (see figure 16). This shock explains about 60% of the forecast error variance of house prices and the FTSE during the 1980s and the 1990s. In contrast, the contribution of the demand shock to these asset prices is higher in the pre-1992 period, especially for house prices and the government bond yield. 

ECB Working Paper Series No 1320April 2011 <mark>27</mark> 



Figure 13: Forecast error variance decomposition of real activity indicators. 

ECB 28 Working Paper Series No 1320April 2011 



Figure 14: Forecast error variance decomposition of inflation measures. 

ECB Working Paper Series No 1320April 2011 <mark>29</mark> 



Figure 15: Forecast error variance decomposition of money supply measures. 

ECB 30 Working Paper Series No 1320April 2011 



Figure 16: Forecast error variance decomposition of asset prices. 

ECB Working Paper Series No 1320April 2011 <mark>31</mark> 

### 5 Conclusions 

Our aim in this paper was to empirically study the evolving transmission of monetary policy and demand shocks in the UK. To this end, we estimated a novel, factor-augmented VAR with time-varying coefficients and shock volatility which made possible the simultaneous analysis of changing impulse responses of a large set of aggregate macroeconomic variables, disaggregated prices and quantities. 

We documented that the impulse responses to UK monetary policy, and demand shocks have changed visibly over the last thirty years. Both the impulse responses and variance decompositions show that around the beginning of the nineties monetary policy shocks started having a bigger impact on prices and began contributing more to overall volatility. We also present evidence of changes in the response of asset prices and components of the consumption deflator — with the median reaction of the latter to contractionary policy shocks becoming more negative. Counterfactual experiments show that these changes are linked to changes in the parameters of the policy rule in our empirical model. 

Our results suggest that time-variation should be taken seriously, which has clear implications for structural economic models. They also highlight a number of interesting links between the evolution of real and nominal variables and asset prices. While attempting to account for these links and for the way they change over time in a stochastic, dynamic, generalequilibrium framework is beyond the scope of this paper, we believe that it would be a worthwhile extension. 

ECB <mark>32</mark> Working Paper Series No 1320April 2011 

### APPENDIX 

### A Priors and Estimation 

Our time-varying FAVAR model consists of the following equations 



with Zt = {Ft<sup>1, F</sup> t<sup>2, Rt},Lfixedat2andthecoefficientsφassumedtoevolveaccordingto</sup> 



The covariance matrix of the innovations vt is factored as 



where the time-varying matrices Ht and At are given by 



with the hi,t evolving as geometric random walks 



Following Primiceri (2005) we postulate that the non-zero and non-one elements of the matrix At evolve as driftless random walks 



and we also assume that [e<sup>�</sup> t<sup>,v</sup> t<sup>�,η�</sup> t<sup>,τ �</sup> t<sup>,ν�</sup> t<sup>]�∼N (0, V )with</sup> 



Bernanke et al. (2005) show that identification of the FAVAR model given by equations 6 and 7 requires putting some (in our case contemporaneous) restrictions on the matrix of factor loadings. Following their example we assume that the top J × J block of Λ is an identity matrix and the top J × M block of Ψ equals zero. The model is then estimated using a Gibbs sampling algorithm with the conditional prior and posterior distributions described below. 

ECB Working Paper Series No 1320April 2011 <mark>33</mark> 

#### A.1 Prior Distributions and Starting Values 

##### A.1.1 Factors and Factor Loadings 

Following Bernanke et al. (2005) we center our prior on the factors (and obtain starting values) by using a principal components (PC) estimator applied to each Xi, t. In order to reflect the uncertainty surrounding the choice of starting values, a large prior covariance of the states (P0/0) is assumed. 

Starting values for the factor loadings are also obtained from the PC estimator after imposing the above restrictions. The priors on the diagonal elements of R are assumed to be inverse gamma 



where R0 = 0.01 and V0 = 1 denote the prior scale parameter and the prior degrees of freedom respectively. 

##### A.1.2 VAR 

The prior for the VAR coefficients is obtained via a fixed coefficients VAR model estimated over the first 10 years of the sample using the principal component estimates of the factors. Accordingly, φ0 is equal to 



OLS where V equals 0.0001 times OLS estimates of the main diagonal of var(φ<sup>ˆ</sup> ). 

##### A.1.3 Elements of Ht 

Let vˆ<sup>ols</sup> denote the OLS estimate of the VAR covariance matrix estimated on the pre-sample data described above. The prior for the diagonal elements of the VAR covariance matrix (see equation 9) is as follows 



ˆ where μ0 are the diagonal elements of the Cholesky decomposition of v<sup>ols</sup> . 

##### A.1.4 Elements of At 

The prior for the off-diagonal elements of At is 



where aˆ<sup>ols</sup> are the off-diagonal elements of vˆ<sup>ols</sup> , with each row scaled by the corresponding element on the diagonal. The matrix V �aˆ<sup>ols�</sup> is assumed to be diagonal with the diagonal ˆ elements set equal to 10 times the absolute value of the corresponding element of a<sup>ols</sup> . 

##### A.1.5 Hyperparameters 

The prior on Q is assumed to be inverse Wishart 



ECB <mark>34</mark> Working Paper Series No 1320April 2011 

where Q<sup>¯</sup> 0 is assumed to be var(φ<sup>ˆ</sup> OLS) × 10−4 × 3.5 and T0 is the length of the sample used for calibration. The prior distribution for the blocks of S is also inverse Wishart 



ˆ where i indexes the blocks of S and S<sup>¯</sup> i is calibrated using a<sup>ols</sup> . Specifically, S<sup>¯</sup> i is a diagonal ˆ matrix with the relevant elements of a<sup>ols</sup> multiplied by 10<sup>−3</sup> . Finally, following Cogley and Sargent (2005), we postulate an inverse-gamma distribution for the elements of G 



#### A.2 Simulating the Posterior Distributions 

##### A.2.1 Factors and Factor Loadings 

This closely follows Bernanke et al. (2005). Details can also be found in Kim and Nelson (1999). 

Factors The distribution of the factors Ft is linear and Gaussian 



where t = T − 1, .., 1, the vector Ξ holds all other FAVAR parameters and 



In line with Carter and Kohn (1994) the simulation consists of several steps. First we use the Kalman filter to draw FT \T and PT \T and then proceed backwards in time using 



If more than one lag of the factors appears in the VAR model, this procedure has to be modified to take account of the fact that the covariance matrix of the shocks to the transition equation (used in the filtering procedure described above) is singular. For details see Kim and Nelson (1999). 

Elements of R Following Bernanke et al. (2005) R is a diagonal matrix. The diagonal elements Rii are drawn from the following inverse gamma distribution 



ECB Working Paper Series No 1320April 2011 <mark>35</mark> 

where 



ˆ with ei denoting the residual Xit − ΓiFjt where Γi = Λi or Γi = [Λi, Ψ] for the appropriate equation. 

Elements of Λ and Ψ Letting Γi = Λi or Γi = [Λi, Ψ] for the appropriate equation, the factor loadings are sampled from 

¯ Γi ∼ N �¯Γi, RiiMi<sup>−1</sup> � ¯ where¯ Γ<sup>¯</sup> i = M<sup>¯</sup> i<sup>−1</sup> �Fi,t<sup>�Fi,t</sup> � ˆΓi, Mi = M<sup>¯</sup> 0 + �Fi,t<sup>�Fi,t</sup> � and Γ<sup>ˆ</sup> i represents an OLS estimate and M0 = I. 

##### A.2.2 Time-Varying VAR 

Given an estimate of the factors, the model becomes a VAR with drifting coefficients and covariances. This type of specification has become fairly standard in the literature and details on the posterior distributions can be found in a number of papers including Cogley and Sargent (2005), Cogley et al. (2005) and Primiceri (2005). Accordingly, we only provide a summary of the estimation algorithm — referring to the references above for further details. 

The Gibbs sampler cycles through the following steps: 

1. Given initial values for the factors, the VAR parameters and hyperparameters are simulated. 

   - As in the case of the unobserved factors the VAR coefficients φt and the offdiagonal elements of the covariance matrix αt are simulated using the methods described in Carter and Kohn (1994). In particular, given a draw for φt the VAR model can be written as 





   - Following Cogley and Sargent (2005), the volatilities of the reduced form shocks Ht are drawn using the date by date blocking scheme introduced in Jacquier et al. (2002). 

   - The hyperparameters are drawn from their respective distributions. Conditional on Zt, φl,t, Ht, and At, the innovations to φl,t, Ht, and At are observable, which allows us to draw the hyperparameters–the elements of Q, S, and the σ<sup>2</sup> i<sup>–from</sup> their respective distributions. 

2. Given initial values for the factors, the factor loadings Λ and Ψ and the variances of the idiosyncratic components are drawn. 

ECB <mark>36</mark> Working Paper Series No 1320April 2011 

   - Given data on Rt and Xi,t standard results for regression models can be used and the coefficients and the variances are simulated from a normal and inverse gamma distribution. 

3. Finally, the factors are simulated given all the other parameters. 

   - This is done in a straightforward way by employing the methods described in Bernanke et al. (2005) and Kim and Nelson (1999). 

4. Go to step 1. 

#### A.3 Convergence 

We use 55,000 iterations in this MCMC algorithm discarding the first 45,000 as burn-in. The figure below shows the recursive means of the retained draws. These show limited fluctuations providing some evidence of convergence. 



#### A.4 Particle Filter to Evaluate the Likelihood for the TVP-FAVAR 

An excellent detailed description of particle filtering and its application to macroeconomic models can be found in Fernandez-Villaverde and Rubio-Ramirez (2008) and the references 

ECB Working Paper Series No 1320April 2011 <mark>37</mark> 

cited therein. Below we provide a brief description of the filter as applied to our FAVAR model. 

Consider the distribution of the state variables (i.e. the time-varying coefficients, stochastic volatilities and the factors) in the Time-Varying FAVAR model denoted Φt conditional on information up to time t (denoted by zt) 



Equation 12 says that this density can be written as the ratio of the joint density of the data and the states f (Xt, Φt\zt−1) = f (Xt\Φt, zt−1) × f (Φt\zt−1) and the likelihood function f (Xt\zt−1) where the latter is defined as 



Note also that the conditional density f (Φt\zt−1) can be written as 



These equations suggest the following filtering algorithm to compute the likelihood function: 

1. Given a starting value f (Φ0\z0) calculate the predicted value of the state 



2. Update the value of the state variables based on information contained in the data 



where f (X1\z0) = � f (X1\Φ1, z0) × f (Φ1\z0) dΦ1 is the likelihood for observation 1. By repeating these two steps for observations t = 1...T the likelihood function of the model can be calculated as ln lik = ln f (X1\z0) + ln f (X2\z1) + ... ln f (XT \zt−1) . 

In general, this algorithm is inoperable because the integrals in the equations above are difficult to evaluate. The particle filter makes the algorithm feasible by using a MonteCarlo method to evaluate these integrals. In particular, the particle filter approximates the conditional distribution f (Φ1\z0) via M draws or particles using the transition equation of the FAVAR model. For each draw of the state variables the conditional likelihood W<sup>m</sup> = f (X1\z0) is evaluated. Conditional on the draw for the state variables, the predicted value for the variables X<sup>ˆ</sup> i<sup>M</sup> 1<sup>canbecomputedusingtheobservationequationandtheprediction</sup> error decomposition is used to evaluate the likelihood W<sup>m</sup> . The update step involves a draw from the density f (Φ1\z1). This is done by sampling with replacement from the sequence of particles with the re-sampling probability given by ~~�~~ MmW=1<sup>mW m.This re-sampling step updates</sup> the draws for Φ based on information contained in the data for that time period. By the law of large numbers the likelihood function for the observation can be approximated as ln likt = ln <u>�Mm=1M</u><sup>W m</sup> . 

ECB <mark>38</mark> Working Paper Series No 1320April 2011 

### B Dataset 

The full list of the 350 data series, along with their FAME codes, is presented below. This appendix provides an overview of the dataset. The dataset contains data on real activity and inflation. We also include some indicators of money and key asset prices. As shown in the table below we take the first log difference of non-stationary series. 

Real activity data includes real GDP, industrial production (with a broad sectoral break down), imports and exports, investment and real household consumption expenditure. The dataset includes a very detailed sectoral breakdown of consumption quantities. The data is obtained from the Office of National Statistics (ONS). 

Inflation data includes the main price indices (GDP deflator, CPI, RPI and RPIX) and components of the consumption deflator. ONS and the Bank of England are the main sources for the data. 

Money data for the U.K. includes M0 and M4, with a sectoral breakdown of the latter. This data is obtained from the Bank of England. 

The asset price data includes house prices, stock prices, exchange rates (pounds in terms of US dollars, Euros, Yen, Canadian and Australian Dollars) and the term structure of interest rates. The data are obtained from the Global Financial Database and the Bank of England. 

|NR|FAME CODE<br>log-dif. unless<br>otherwise stated|SERIES NAME|
|---|---|---|
|1|NMRY|General Government: Final consumption expenditure|
|2|GDQB|ESA95 Output Index: F: Construction:|
|3|IKBK|Balance of Payments: Trade in Goods & Services: Total exports|
|4|IKBL|Balance of Payments: Imports: Total Trade in Goods & Services|
|5|NPQT|Total Gross Fixed Capital Formation|
|6|ABMI|Gross Domestic Product: chained volume measures|
|7|CKYY|IOP: Industry D: Manufacturing: CVMSA NAYear|
|8|GDQH|SA95 Output Ind.: I : Transport storage & communication|
|9|GDQS|SA95 Output Ind.: G-Q: Total|
|10|GDQE|ESA95 Output Ind.: G & H: Distrib., hotels & catering; repairs|
|11|CKYW|IOP: Industry C,D,E: All production industries|
|12|CKYZ|IOP: Industry E: Electricity, gas and water supply:|
|13|CKZA|IOP: Industry DA: Manuf of food, drink & tobacco|
|14|CKZF|IOP: Industry DF: Manuf coke/petroleum prod/nuclear fuels|
|15|CKZG|IOP: Industry DG: Manuf of chemicals & man-made fbres|
|16|ABJR|Household fnal consumption expenditure|
|17|NPEL|Business investment|
||Household fnal|consumption expenditure:durable goods (volumes)|
|18|UTID|Total|
|19|LLKX|All furnishing & household|
|20|ATQX|Furniture and households|
|21|ATRD|Carpets and other foor coverings|
|22|XYJP|Major household appliances|
|23|XYJR|Major tools and equipment|
|24|LLKY|All Health|
|25|UWIC|Therapeutic appliances and equipment|



ECB Working Paper Series No 1320April 2011 <mark>39</mark> 

|26|LLKZ|All Transport|
|---|---|---|
|27|TMMI|All Purchase of vehicles|
|28|TMML|Motor Cars|
|29|TMMZ|Motor cycles|
|30|TMNO|Bicycles|
|31|LLLA|All Communication|
|32|ATRR|Telephone and telefax equipment|
|33|LLLB|All recreation and culture|
|34|ATRV|Audio visual equipment|
|35|ATRZ|Photo and cinema equip and optical instruments|
|36|ATSD|Information processing equipment|
|37|TMNB|Major durables for outdoor recreation|
|38|XYJT|Musical instruments and major durables for indoor recreation|
|39|LLLC|All miscellaneous|
|40|ZAYM|Jewelery, clocks and watches|
||Household|fnal consumption expenditure: semi-durable goods (volumes)|
|41|UTIT|Total|
|42|LLLZ|All clothing and footwear|
|43|XYJN|Clothing materials|
|44|ZAVK|Garments|
|45|XYJO<br>|Other articles of clothing and clothing accessories|
|46|ATQV|Shoes and other footwear|
|47|LLMA|All furnishings and household goods|
|48|ATRF|Household textiles|
|49|XYJQ|Small electric household appliances|
|50|ATRJ|Glassware, tableware and household utensils|
|51|XYJS|Small tools and miscellaneous accessories|
|52|LLMB|All transport|
|53|AWUW|Motor vehicle spares|
|54|LLMC|All recreation and culture|
|55|ATSH|Recording media|
|56|ATSL|Games, toys and hobbies|
|57|XYJU|Equipment for sport, camping etc|
|58|CDZQ|Books|
|59|LLMD|All miscellaneous|
|60|XYJX|Electrical appliances for personal care|
|61|ATSX|Other personal efects|
||Household fn|al consumption expenditure: non-durable goods (volumes)|
|62|UTIL|Total|
|63|ZWUN|All food and non-alcoholic beverages|
|64|UWBK|All food|
|65|UWBL|Bread and cereals|
|66|CCTK|Meat|
|67|CCTL|Fish|
|68|CCTM|Milk, cheese and eggs|
|69|CCTN|Oils and fats|
|70|CCTO|Fruit|
|71|UWFD|Vegetables|
|72|UWFX|Sugar and sweet products|



ECB <mark>40</mark> Working Paper Series No 1320April 2011 

|73|UWGH|Food products n.e.c.|
|---|---|---|
|74|UWGI|All non-alcoholic beverages|
|75|CCTT|Cofee, tea and cocoa|
|76|CCTU|Mineral, water and soft drinks|
|77|ZAKY|All alcoholic beverages and tobacco|
|78|UUIS|Spirits|
|79|UTHW|Wine, cider and sherry|
|80|UUVG|Beer|
|81|ZWUP|Tobacco|
|82|LLLL|All Housing, water, electricity, gas and other fuels|
|83|ATUA|Materials for the maintenance and repair of the dwelling|
|84|UTZN|Water supply|
|85|ZWUR|All electricity, gas and other fuels|
|86|CCUA|Electricity|
|87|LTZA|Gas|
|88|LTZC|Liquid fuels|
|89|TTAB|Solid fuels|
|90|LLLM|All furnishing and household goods|
|91|UWHO|Non-durable household goods|
|92|LLLN|All health|
|93|UTXP|Pharmaceutical products|
|94|UWIB|Other medical products|
|95|LLLO|All transport|
|96|CCTY|Vehicle fuels and lubricants|
|97|LLLP|All recreation and culture|
|98|AWUX|Gardens, plants and fowers|
|99|UWKQ|Pets and related products|
|100|CDZY|Newspapers and periodicals|
|101|XYJV|Miscellaneous printed matter|
|102|XYJW|Stationery and drawing materials|
|103|LLLQ|All miscellaneous|
|104|ATSP|Other products for personal care|
||Househo|ld fnal consumption expenditure: services (volumes)|
|105|UTIP|Total|
|106|LLLR|All clothing and footwear|
|107|UWHI|Clothing, repair and hire of clothing|
|108|AWUY|Repair and hire of footwear|
|109|LLLS|All housing, water, electricity, gas and other fuels|
|110|ZAVQ|All actual rentals for housing|
|111|GBFG|Actual rentals paid by tenants|
|112|GBFK|All imputed rentals for housing|
|113|CCUO|Imputed rentals of owner-occupiers|
|114|GBFN|Other imputed rentals|
|115|AWUZ|Services for the maintenance and repair of the dwelling|
|116|UWHK|Refuse collection|
|117|UTZX|Sewerage collection|
|118|LLLT|All furnishings and household services|
|119|UWHM|Repair of furniture, furnishings and foor coverings|
|120|UWHN|Repair of household appliances|



ECB Working Paper Series No 1320April 2011 <mark>41</mark> 

|121|UWIA|Domestic and household services|
|---|---|---|
|122|LLLU|All health|
|123|ZAWG|All out-patient services|
|124|ZAWI|Medical services|
|125|ZAWK|Dental services|
|126|UTMH|Paramedical services|
|127|UTYF|Hospital services|
|128|LLLV|Total transport|
|129|AWVA|Vehicle maintenance and repair|
|130|ZAWQ|Other vehicle services|
|131|ZAWS|All transport services|
|132|AWVB|Railways|
|133|ZAWU|Road|
|134|AWVC|Air|
|135|AWVD|Sea and inland waterway|
|136|AWVE|Other|
|137|LLLW|All communication|
|138|CCVM|Postal services|
|139|ZAWY|Telephone and telefax services|
|140|LLLX|All recreation and culture|
|141|UWKO|Repair of audio-visual, photo and information processing equip.|
|142|UWKP|Maintenance of other major durables for recreation and culture|
|143|UWLD|Veterinary and other services for pets|
|144|ZAXI|All recreational and cultural services|
|145|ZAXK|Recreational and sporting services|
|146|ZAXM|Cultural services|
|147|CCVA|Games of chance|
|148|ZWUT|Education|
|149|ZAXS|All restaurants and hotels|
|150|ZAXU|All catering services|
|151|ZAXW|Restaurants, cafes etc.|
|152|ZAYC|Canteens|
|153|ZAYE|Accommodation services|
|154|LLLY|All miscellaneous|
|155|CCVZ|Hairdressing salons and personal grooming establishments|
|156|ZAYO|Social protection|
|157|ZAYQ|All insurance|
|158|UTYH|Life insurance|
|159|ZAYS|Insurance connected with the dwelling|
|160|ZAYU|Insurance connected with health|
|161|ZAYW|Insurance connected with transport|
|162|ZAZA|All fnancial services n.e.c.|
|163|ZAZC|All fnancial services other than FISIM|
|164|ZAZE|Other services n.e.c.|
|||DEFLATORS|
|165|FRAH|RPI Total Food|
|166|FRAI|RPI Total Non-Food|
|167|FRAK|RPI Total All items other than seasonal Food|
|168|ROYJ|Wages|



ECB <mark>42</mark> Working Paper Series No 1320April 2011 

|169|YBGB|GDP defator|
|---|---|---|
|170||CPI|
|171|ABJS|CONSUMPTION|
|172|IMF data|Import prices|
|173|IMF data|Export prices|
||Household f|nal consumption expenditure: durable goods (defators)|
|174|UTKT|Total|
|175|LLOS|All furnishing & household|
|176|AWQK|Furniture and households|
|177|AWQL|Carpets and other foor coverings|
|178|AWQN|Major household appliances|
|179|AWQQ|Major tools and equipment|
|180|LLOT|All Health|
|181|AWQW|Therapeutic appliances and equipment|
|182|LLOU|All Transport|
|183|UTPP|All Purchase of vehicles|
|184|AWRA|Motor Cars|
|185|AWRB|Motor cycles|
|186|AWRC|Bicycles|
|187|LLOV|All Communication|
|188|UTPT|Telephone and telefax equipment|
|189|LLOW|All recreation and culture|
|190|AWRM|Audio visual equipment|
|191|AWRN|Photo and cinema equip and optical instruments|
|192|AWRO|Information processing equipment|
|193|AWRR|Major durables for outdoor recreation|
|194|AWRS|Musical instruments and major durables for indoor recreation|
|195|LLOX|All miscellaneous|
|196|AWSL|Jewelery, clocks and watches|
|H|ousehold fna|l consumption expenditure: semi-durable goods (defators)|
|197|UTLB|Total|
|198|LLPU|All clothing and footwear|
|199|AWPP|Clothing materials|
|200|AWPQ|Garments|
|201|AWPR|Other articles of clothing and clothing accessories|
|202|AWPT|Shoes and other footwear|
|203|LLPV|All furnishings and household goods|
|204|UTPH|Household textiles|
|205|AWQO|Small electric household appliances|
|206|UTPJ|Glassware, tableware and household utensils|
|207|AWQR|Small tools and miscellaneous accessories|
|208|LLPW|All transport|
|209|AWRD|Motor vehicle spares|
|210|LLPX|All recreation and culture|
|211|AWRP|Recording media|
|212|AWRU|Games, toys and hobbies|
|213|AWRV<br>|Equipment for sport, camping etc|
|214|AWSC|Books|
|215|LLPY|All miscellaneous|



ECB Working Paper Series No 1320April 2011 <mark>43</mark> 

|216|AWSJ|Electrical appliances for personal care|
|---|---|---|
|217|AWSM|Other personal efects|
|H|ousehold fna|l consumption expenditure: non-durable goods (defators)|
|218|UTKX|Total|
|219|UTJO|All food and non-alcoholic beverages|
|220|UTOV|All food|
|221|AWPB|Bread and cereals|
|222|AWPC|Meat|
|223|AWPD|Fish|
|224|AWPE|Milk, cheese and eggs|
|225|AWPF|Oils and fats|
|226|AWPG|Fruit|
|227|AWPH|Vegetables|
|228|AWPI|Sugar and sweet products|
|229|AWPJ|Food products n.e.c.|
|230|UTOW|All non-alcoholic beverages|
|231|AWPK|Cofee, tea and cocoa|
|232|AWPL|Mineral, water and soft drinks|
|233|UTJP|All alcoholic beverages and tobacco|
|234|AWPM|Spirits|
|235|AWPN|Wine, cider and sherry|
|236|AWPO|Beer|
|237<br>|UTOY<br>|Tobacco<br>|
|238|LLPG|All Housing, water, electricity, gas and other fuels|
|239|AWPZ|Materials for the maintenance and repair of the dwelling|
|240|AWQB|Water supply|
|241|UTPF|All electricity, gas and other fuels|
|242|AWQF|Electricity|
|243|AWQG|Gas|
|244|AWQH|Liquid fuels|
|245|AWQI|Solid fuels|
|246|LLPH|All furnishing and household goods|
|247|AWQS|Non-durable household goods|
|248|LLPI|All health|
|249|AWQU|Pharmaceutical products|
|250|AWQV|Other medical products|
|251|LLPJ|All transport|
|252|AWRE|Vehicle fuels and lubricants|
|253|LLPK|All recreation and culture|
|254|AWRW|Gardens, plants and fowers|
|255|AWRX|Pets and related products|
|256|AWSD|Newspapers and periodicals|
|257|AWSJ|Stationery and drawing materials|
|258|LLPL|All miscellaneous|
|259|AWSK|Other products for personal care|
||Househol|d fnal consumption expenditure: services (defators)|
|260|UTKZ|Total|
|261|LLPM|All clothing and footwear|
|262|AWPS|Clothing, repair and hire of clothing|



ECB <mark>44</mark> Working Paper Series No 1320April 2011 

|263|AWPU|Repair and hire of footwear|
|---|---|---|
|264|LLPN|All housing, water, electricity, gas and other fuels|
|265|AWPV|All actual rentals for housing|
|266|AWPV|Actual rentals paid by tenants<br>|
|267|UTPC|All imputed rentals for housing|
|268|AWPX|Imputed rentals of owner-occupiers|
|269|AWPY|Other imputed rentals|
|270|AWQA<br>|Services for the maintenance and repair of the dwelling<br>|
|271|AWQD|Sewerage collection|
|272|LLPO|All furnishings and household services|
|273|AWQM|Repair of furniture, furnishings and foor coverings|
|274|AWQP|Repair of household appliances|
|275|AWQT|Domestic and household services|
|276|LLPP|All health|
|277|UTPN|All out-patient services|
|278|AWQX|Medical services|
|279|AWQY|Dental services|
|280|AWQZ|Paramedical services|
|281|UTPO|Hospital services|
|282|LLPQ|Total transport|
|283|AWRF|Vehicle maintenance and repair|
|284|AWRG|Other vehicle services|
|285|UTPR|All transport services|
|286|AWRH|Railways|
|287|AWRI|Road|
|288|AWRJ|Air|
|289|AWRK|Sea and inland waterway|
|290|AWRL|Other|
|291|LLPR|All communication|
|292|UTPS|Postal services|
|293|UTPU|Telephone and telefax services|
|294|LLPS|All recreation and culture|
|295|AWRQ|Repair of audio-visual, photo and information processing equip.|
|296|AWRY|Veterinary and other services for pets|
|297|UTPY|All recreational and cultural services|
|298|AWRZ|Recreational and sporting services|
|299|AWSA|Cultural services|
|300|AWSB|Games of chance|
|301|UTJX|Education|
|302|UTJY|All restaurants and hotels|
|303|UTQG|All catering services|
|304|AWSG|Restaurants, cafes etc.|
|305|AWSH|Canteens|
|306|UTQH|Accommodation services|
|307|LLPT|All miscellaneous|
|308|AWSI|Hairdressing salons and personal grooming establishments|
|309|UTQK|Social protection|
|310|UTQL|All insurance|
|311|AWSN|Life insurance|



ECB Working Paper Series No 1320April 2011 <mark>45</mark> 

|312|AWSO|Insurance connected with the dwelling|
|---|---|---|
|313|AWSP|Insurance connected with health|
|314|AWSQ|Insurance connected with transport|
|315|UTQM|All fnancial services n.e.c.|
|316|AWSS|All fnancial services other than FISIM|
|317|UTQN|Other services n.e.c.|
|||MONEY SERIES|
|318|M4SA|M4 deposits Total|
|319|M4ISA|M4 deposits PNFCs|
|320|M4OSA|M4 deposits OFCs|
|321|M4PSA|M4 deposits Households|
|322|M4LISA|M4 lending Total|
|323|M4LOSA|M4 lending PNFCs|
|324|M4LPSA|M4 lending Households|
|||ASSET PRICES|
|325||Real Nationwide house prices|
|326||UK FT-Actuaries Dividend Yield (w/GFD extension)|
|327||UK FT-Actuaries PE Ratio (w/GFD extension)|
|328|GFD data|FTSE ALL Share Index|
|329|IMF data|NEER|
|330|GFD data|pounds/dollar|
|331|GFD data|pounds/euro|
|332|GFD data|pounds/yen|
|333|Global fn. data|pounds/canadian dollar|
|334|Global fn. data|pounds/australian dollar|
|335|non-transformed|Bond Yield 6 Months|
|336|non-transformed|Bond Yield 9 Months|
|337|non-transformed|Bond Yield 12 Months|
|338|non-transformed|Bond Yield 15 Months|
|339|non-transformed|Bond Yield 18 Months|
|340|non-transformed|Bond Yield 21 Months|
|341|non-transformed|Bond Yield 24 Months|
|342|non-transformed|Bond Yield 30 Months|
|343|non-transformed|Bond Yield 36 Months|
|344|non-transformed|Bond Yield 48 Months|
|345|non-transformed|Bond Yield 60 Months|
|346|non-transformed|Bond Yield 72 Months|
|347|non-transformed|Bond Yield 84 Months|
|348|non-transformed|Bond Yield 96 Months|
|349|non-transformed|Bond Yield 108 Months|
|350|non-transformed|Bond Yield 120 Months|



ECB <mark>46</mark> Working Paper Series No 1320April 2011 

### References 

- Alvarez, Fernando and Francesco Lippi, 2009, Persistent Liquidity Effect and Long Run Money Demand, University of Chicago, mimeo. 

- Baumeister, Christiane, Philip Liu and Haroon Mumtaz, 2010, Changes in the Transmission of Monetary Policy: Evidence from a Time-Varying Factor-Augmented VAR, Bank of England working papers 401, Bank of England. 

- Benati, Luca, 2004, Evolving Post-World War II U.K. Economic Performance, Journal of Money Credit and Banking 36(4), 691—717. 

- Benati, Luca, 2008, The "Great Moderation" in the United Kingdom, Journal of Money, Credit and Banking 40(1), 121—147. 

- Benati, Luca and Paolo Surico, 2009, VAR Analysis and the Great Moderation, American Economic Review 99(4), 1636—52. 

- Bernanke, Ben, Jean Boivin and Piotr S. Eliasz, 2005, Measuring the Effects of Monetary Policy: A Factor-augmented Vector Autoregressive (FAVAR) Approach, The Quarterly Journal of Economics 120(1), 387—422. 

- Bianchi, Francesco, Haroon Mumtaz and Paolo Surico, 2009, Dynamics of the Term Structure of UK Interest Rates, Bank of England working papers 363, Bank of England. 

- Boivin, Jean, Marc P. Giannoni and Ilian Mihov, 2009, Sticky Prices and Monetary Policy: Evidence from Disaggregated US Data, American Economic Review 99(1), 350—84. 

- Canova, Fabio and Gianni De Nicolo, 2002, Monetary Disturbances Matter for Business Fluctuations in the G-7, Journal of Monetary Economics 49(6), 1131—1159. 

- Carter, Chris and Robert Kohn, 1994, On Gibbs Sampling for State Space Models, Biometrika 81(3), pp. 541—553. 

- Castelnuovo, Efrem and Paulo Surico, 2006, The Price Puzzle: Fact or Artefact?, Bank of England Working Paper no. 288. 

- Chib, Siddhartha, 1995, Marginal Likelihood from the Gibbs Output, Journal of the American Statistical Association 90(432), pp. 1313—1321. 

- Cogley, Timothy, Giorgio E. Primiceri and Thomas J. Sargent, 2010, Inflation-Gap Persistence in the US, American Economic Journal: Macroeconomics 2(1), 43—69. 

- Cogley, Timothy, Sergei Morozov and Thomas J. Sargent, 2005, Bayesian Fan Charts for U.K. Inflation: Forecasting and Sources of Uncertainty in an Evolving Monetary System, Journal of Economic Dynamics and Control 29(11), 1893—1925. 

- Cogley, Timothy and Thomas J. Sargent, 2005, Drift and Volatilities: Monetary Policies and Outcomes in the Post WWII U.S, Review of Economic Dynamics 8(2), 262—302. 

- Del Negro, Marco and Christopher Otrok, 2008, Dynamic factor models with time-varying parameters: measuring changes in international business cycles, Staff Reports 326, Federal Reserve Bank of New York. 

ECB Working Paper Series No 1320April 2011 <mark>47</mark> 

- Fernandez-Villaverde, Jesus and Juan Rubio-Ramirez, 2008, How Structural Are Structural Parameters?, NBER Macroeconomics Annual 2007, Volume 22, NBER Chapters, National Bureau of Economic Research, Inc, pp. 83—137. 

- Forni, Mario and Luca Gambetti, 2010, Macroeconomic Shocks and the Business Cycle: Evidence from a Structural Factor Model, Center for Economic Research (RECent) 040, University of Modena and Reggio E., Dept. of Economics. 

- Jacquier, Eric, Nicholas G Polson and Peter E Rossi, 2002, Bayesian Analysis of Stochastic Volatility Models, Journal of Business & Economic Statistics 20(1), 69—87. 

- Kim, Chang-Jin and Charles R. Nelson, 1999, State-Space Models with Regime Switching, MIT Press, Cambridge, Massachusetts. 

- Koop, G., M. H. Pesaran and S. M. Potter, 1996, Impulse Response Analysis in Nonlinear Multivariate Models, Journal of Econometrics 74, 119—47. 

- Leduc, Sylvain, Keith Sill and Tom Stark, 2007, Self-fulfilling Expectations and the Inflation of the 1970s: Evidence from the Livingston Survey, Journal of Monetary Economics 54(2), 433—459. 

- Lubik, Thomas and Frank Schorfheide, 2006, A Bayesian Look at the New Open Economy Macroeconomics, NBER Macroeconomics Annual 2005, Volume 20, NBER Chapters, National Bureau of Economic Research, Inc, pp. 313—382. 

- Mumtaz, Haroon and Paolo Surico, 2008, Evolving International Inflation Dynamics: Evidence from a Time-Varying Dynamic Factor Model, Bank of England working papers 341, Bank of England. 

- Primiceri, Giorgio E., 2005, Time Varying Structural Vector Autoregressions and Monetary Policy, Review of Economic Studies 72(3), 821—52. 

- Uhlig, Harald, 2005, What are the Effects of Monetary Policy on Output? Results From an Agnostic Identification Procedure, Journal of Monetary Economics 52(2), 381—419. 

ECB 48 Working Paper Series No 1320April 2011 



