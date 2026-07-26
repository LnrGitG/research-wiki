---
title: **Working Paper Series**
type: paper
source_pdf: raw/papers/Velasco_Asymmetries in the transmission of monetary policy shocks over the business cycle a Bayesian quantile factor augmented VAR_2026.pdf
converted: 2026-07-26
---



# **Working Paper Series** 

> Sofia Velasco Asymmetries in the transmission of monetary policy shocks over the business cycle: a Bayesian quantile factor augmented VAR 

Revised March 2026 



<!-- Start of picture text -->
No 2983<br><!-- End of picture text -->

**Disclaimer:** This paper should not be reported as representing the views of the European Central Bank (ECB). The views expressed are those of the authors and do not necessarily reflect those of the ECB. 

##### **Abstract** 

This paper introduces a Bayesian Quantile Factor Augmented VAR (BQFAVAR) to examine the asymmetric effects of monetary policy throughout the business cycle. Monte Carlo experiments demonstrate that the model effectively captures non-linearities in impulse responses. Analysis of aggregate responses to a contractionary monetary policy shock reveals that financial variables and industrial production exhibit more pronounced impacts during recessions compared to expansions, aligning with predictions from the ’financial accelerator’ propagation mechanism literature. Additionally, inflation displays a higher level of symmetry across economic conditions, consistent with households’ loss aversion in the context of reference-dependent preferences and central banks’ commitment to maintaining price stability. The examination of price rigidities at a granular level, employing sectoral prices and quantities, demonstrates that during recessions, the contractionary policy shock results in a more pronounced negative impact on quantities compared to expansions. This finding provides support for the notion of stronger downward than upward price rigidity, as suggested by ’menu-costs models’. 

**Keywords:** Bayesian Quantile VAR, FAVAR, Asymmetric effects of monetary policy, Disaggregate prices, Non-linear models 

**JEL Codes:** C11 C32 E32 E37 E52 

ECB Working Paper Series No 2983 

1 

## **Non-technical summary** 

In this study, I analyze the impact of monetary policy changes in the United States on various economic indicators, including output, inflation, the Excess Bond Premium, and a detailed dataset of sectoral prices and quantities spanning from 1976 to 2005. The results indicate that when the interest rate is tightened, financial variables and industrial production exhibit notably stronger responses during economic downturns compared to periods of economic expansion. However, the response of inflation appears to be more symmetric across different economic conditions. 

The increased influence of monetary policy tightening on the Excess Bond Premium and industrial production during recessions suggests that interest rate changes affect borrowing costs and investment decisions more strongly in economic downturns. This phenomenon can be attributed to the weakened state of firms’ balance sheets during periods of economic downturn, leading to an increase in the premium as borrowers become more reliant on external finance. While the less pronounced differences in how inflation responds to monetary policy shocks across economic conditions may be due to households’ tendency to be more sensitive to consumption losses and central banks measures to maintain price stability. In addition, inflation responses are weaker during recessions due to increased inflexibility in the labor market. 

Cross-sectoral analysis of prices and quantities reveals that during recessions, price reactions vary more compared to periods of economic growth. However, on average, the results of this analysis suggest that prices don’t change significantly in response to monetary policy shifts. While, when the economy is contracting, monetary policy tightening has a larger negative impact on output compared to expansions. This asymmetry can be attributed to stronger downward than upward price rigidity, meaning that the effects of monetary policy changes are primarily reflected in output. 

ECB Working Paper Series No 2983 

2 

## **1 Introduction** 

Is the efficacy of monetary policy contingent on the economic state? This question, influenced by seminal works such as those by Graham (1930), Keynes (1937), and Friedman and Schwartz (1963), has been explored extensively in the literature. Empirical evidence suggests that monetary policy exerts asymmetric effects on output and prices depending on prevailing conditions. However, there is still no consensus on whether monetary policy is more powerful during recessions or expansions. The direction and magnitude of these asymmetries remain unclear, with some studies indicating stronger effects during downturns, while others point to amplified transmission in booms. Understanding these nonlinearities is essential for designing effective and well-timed policy interventions. 

This paper contributes to this discussion by proposing a flexible empirical framework to analyze how the transmission of structural shocks varies across the distribution of macroeconomic conditions. I develop a Bayesian Quantile Factor-Augmented VAR (BQFAVAR), a nonlinear extension of the FAVAR model introduced by Bernanke et al. (2005), and apply it to study the Propagation of monetary policy shocks account for the state of the economy. The key innovation lies in allowing the dynamics of latent factors to depend on the conditional quantile of the economic state, thereby capturing how the effectiveness of monetary policy may differ between recessions and expansions. 

The model introduces a quantile-dependent structure at the transition equation, allowing the latent forces that drive macroeconomic fluctuations to evolve differently across quantiles. This specification makes it possible to assess asymmetries in the propagation of structural shocks across different states of the economy. Expansions and recessions are modeled through the upper and lower quantiles of a real activity factor, providing a structured way to capture nonlinear transmission dynamics. 

The proposed framework builds on the strengths of vector autoregressions (VARs) for structural inference, combined with the flexibility of quantile regression techniques to model the conditional distribution of macroeconomic variables beyond the mean. Recent advances have extended quantile regression to multivariate time series contexts. Frequentist approaches include the quantile VAR introduced by White et al. (2015), and more recent contributions by Forni et al. (2023) and Chavleishvili and Manganelli (2024). Bayesian formulations have been proposed by Sch¨uler (2020) and Iacopini et al. (2022). 

A related strand of the literature introduces quantile dependence at the compression stage of factor models. This approach allows the factor structure to adjust across the distribution of observed variables, enabling distribution-sensitive signal extraction from high-dimensional data while preserving a low-dimensional representation. Notable contributions include Ando and Bai (2020), Ma et al. (2021), Chen et al. (2021), Ando et al. (2023), Korobilis and Schr¨oder (2024a),Korobilis and Schr¨oder (2024b) and Clark et al. (2024). In particular, Korobilis and Schr¨oder (2024a) combine quantile-dependent factor estimation with VAR methodology to capture distributional heterogeneity and potential asymmetries in macroeconomic dynamics. Their Quantile FAVAR model introduces quantile dependence in the observation equation, allowing the relationship between latent factors and observables to vary across the distribution. While this structure effectively captures distributional asymmetries in the measurement block, it re- 

ECB Working Paper Series No 2983 

3 

tains linear and quantile-invariant dynamics for the latent factors. Therefore, the model does not explicitly account for asymmetries in the propagation of structural shocks. My approach addresses this limitation by introducing quantile dependence in the transition equation, allowing the latent factors to evolve differently across quantiles. This enables the identification of state-contingent transmission dynamics. In addition, the model remains parsimonious, as nonlinearities are embedded in a low-dimensional latent space rather than requiring quantile-specific equations for each observable variable—an important advantage, as it allows the inclusion of a larger dataset and helps mitigate information scarcity and omitted variable bias. 

This advantage builds on the original motivation behind the FAVAR framework by Bernanke et al. (2005), who show that using a broader set of economic indicators improves the identification of monetary policy shocks. Traditional VAR models typically consider a narrower set of variables than those monitored by financial market participants and the Federal Reserve, making them prone to omitted variable bias. The results representing the ’neutral’ economic scenario align closely with the average responses reported in Bernanke et al. (2005)’s seminal paper—most notably, the absence of a price puzzle and a plausible negative response of industrial production to a contractionary monetary policy shock. However, when conditioning on the tails of the real economic activity factor, proxying economic expansions and recessions, the impact of contractionary monetary policy innovations provides further evidence of the asymmetric impact of monetary policy with respect to the economic state. Specifically, financial variables and industrial production demonstrate heightened responsiveness during economic contractions compared to expansions, while the response of inflation displays a higher degree of symmetry. Studies by Weise (1999), Dolado and Dolores (2001) or Lo and Piger (2005), among others, corroborate these findings, highlighting a stronger impact of monetary policy innovations on real activity during recessions alongside a more homogenous impact on the price level across the different business cycle phases. However, it is noteworthy that these results diverge from previous research, such as that of Tenreyro and Thwaites (2016), which suggests a more pronounced impact of monetary policy shocks during economic expansions. This discrepancy may be attributed, among other reasons, to the counteracting (or reinforcing) impact of fiscal policy during recessions (booms). 

Furthermore, my findings align with expectations from the literature on the ’financial accelerator’ propagation mechanism. This theory suggests that information asymmetry between borrowers and lenders results in an external finance premium, which typically relies on the borrower’s net worth. Borrowers with higher net worth can offer more collateral, reducing their cost of external financing. Bernanke and Gertler (1995) explore the ’balance-sheet’ channel of the credit channel theory, where changes in short-term interest rates impact capital costs and the external finance premium.<sup>1</sup> This dependence on borrower net worth creates a ’financial accelerator’ propagation mechanism. Consequently, policy tightening increases capital costs through the interest rate channel and lowers collateral values and cash flow, positively affecting the external finance premium. 

As a result, monetary policy’s impact is most significant during periods when firms heavily 

> 1See also Blinder (1987), Gertler and Hubbard (1988), Bernanke and Gertler (1989) or Kiyotaki and Moore (1997). 

ECB Working Paper Series No 2983 

4 

rely on external financing. During recessions, firms’ balance sheets are typically weaker, causing the premium to rise alongside borrowers’ reliance on external finance. Therefore, monetary policy tends to have stronger effects during recessions than in booms. Consistent with the predictions of the ’financial accelerator’ propagation mechanism, my findings, along with those of Peersman and Smets (2005), indicate a stronger impact on output and financial variables during recessions. 

The diminished evidence of state-dependent asymmetries in inflation’s response to a monetary policy shock can be attributed to multiple factors. One potential explanation is households’ aversion to losses within the framework of reference-dependent preferences and downward stickiness of real wages during recessions. Santoro et al. (2014) suggest that the relatively symmetric response of inflation compared to output during recessions could be explained by the aversion of households to losses, as described in the prospect theory by Kahneman and Tversky (1979). According to their modeling strategy, households’ utility is influenced by the deviation of their consumption from a habit-based reference level, below which loss aversion is evident. Consistent with prospect theory, losses in consumption utility are more impactful than gains. Concurrently, inflation responses are attenuated by an increased degree of real rigidity in the labor market. 

Additionally, the impact of central banks’ commitment to maintaining price stability through monetary policy, irrespective of the state of the economy, must be considered when analyzing the response of inflation. The significant influence of central banks on economic activity and inflation is supported by various research, including Cogley and Sargent (2005), Bernanke et al. (2011), and Agrippino and Ricco (2021). Moreover, Forni et al. (2020) provide evidence that monetary policy shocks have asymmetric effects on prices and output, but the systematic response of central banks helps to maintain inflation stability. This aligns with the Eurosystem monetary transmission network study Angeloni et al. (2003), which discusses the stabilizing effects of monetary policy on inflation across the business cycle. 

Furthermore, this study delves into the presence of price rigidities at a granular level by incorporating Boivin et al. (2009)’s extensive dataset of sectoral prices and quantities. The findings are consistent with those of the reference paper, indicating that the volatility in the granular price series does not translate into price flexibility in response to monetary policy shocks. Additionally, in the short run, prices exhibit more heterogeneous responses during a recession compared to an expansion. Specifically, the contractionary policy shock during recessions has a larger negative impact on quantities than during expansions. This asymmetry in response to monetary policy shocks is in line with the mechanisms elucidated by ’menu-costs models’, which attribute it to stronger downward than upward price rigidity, implying that negative fluctuations are primarily reflected in output (e.g., Ball and Mankiw (1994) and Senda (2001)). 

This paper contributes to the empirical literature in three main ways. First, it revisits the state-dependence of monetary policy by characterizing the business cycle through a multivariate lens. The use of latent factors is particularly valuable in settings where individual data series are sparse but complementary, as it enables the aggregation of diverse signals—such as output, employment, credit, and survey expectations—into a coherent representation of underlying economic conditions. This synthesis provides a more nuanced understanding of the prevailing 

ECB Working Paper Series No 2983 

5 

state of the economy, which is essential for assessing how the transmission of monetary policy varies across different phases of the business cycle. Moreover, beyond the real activity factor, the proposed methodology employs rank-reduction techniques to extract additional latent factors from a broad set of macroeconomic indicators, which are also incorporated in the estimation. This helps overcome information scarcity and addresses the omitted variable problem that often undermines structural identification in small-scale VARs. As emphasized by Sims (1992), limited information sets can distort the estimated effects of policy shocks—sometimes even generating price puzzles or muted responses in key macroeconomic variables. 

Second, this paper contributes to a growing strand of the literature that combines latent factor models with quantile-dependent dynamics. While conventional impulse response analysis focuses on average effects, this approach explores the full conditional distribution of responses, offering richer insights into how the transmission of monetary policy varies across different states of the economy. Recent work in this area introduces quantile-dependent factor structures in the observation equation, allowing the mapping from latent factors to observables to vary across quantiles (e.g., Chen et al. (2021); Korobilis and Schr¨oder (2024a)). In contrast, my approach introduces quantile dependence directly in the transition equation, allowing the latent factors themselves to evolve differently across quantiles. This shift in focus makes it possible to assess asymmetries in the propagation of structural shocks, rather than only heterogeneity in their measurement. By modeling how latent dynamics respond to different economic states, the framework provides a more direct lens on state-contingent transmission mechanisms—particularly important for understanding nonlinearities in monetary policy effectiveness. 

Third, this paper contributes to the literature on the role of sectoral heterogeneity in the transmission of monetary policy. Sector-level analysis allows for an assessment of whether aggregate results mask off-setting dynamics at the disaggregated level. As emphasized by Boivin et al. (2009) and Baumeister et al. (2013), aggregate price indices can obscure substantial crosssectional variation, and disaggregate analysis can reveal meaningful differences in how firms adjust prices and quantities in response to monetary disturbances. This study extends previous work by providing state-dependent cross-sectoral impulse responses, allowing the transmission of monetary policy shocks to be examined across industries conditional on the prevailing economic state. The results suggest that aggregate responses do not mask offsetting dynamics at the sectoral level, as price responses are relatively symmetric across states of the economy, while quantities display a stronger state dependence, with more pronounced effects during recessions. 

The remainder of the paper is laid out as follows: Section 2 introduces the empirical model and the identification strategy. Section 3 contains the results of a small Monte Carlo experiment to assess the performance of the model picking up on asymmetries in the data. Section 4 discusses the aggregate and cross-sectoral results and their implications for the asymmetry in the monetary policy actions. Section 5 concludes. 

## **2 Empirical methodology** 

This section sets out the specification of the econometric model used in this study and illustrates my approach to statistical inference. In a similar fashion as Koop and Korobilis (2014) and 

ECB Working Paper Series No 2983 

6 

Dolado et al. (2020) I perform a two step analysis. First I extract a set of common factors that I then include into a quantile Bayesian autoregression, QBVAR henceforth, and uncover the response of the main macroeconomic variables to a monetary policy shock in the US. Hereby I try to understand whether studying the quantiles of the distribution adds to the results of the canonical paper Bernanke et al. (2005). 

### **2.1 Monetary policy transmission and proxies for the business cycle** 

Bernanke et al. (2005) shows that the FAVAR framework allows for a better identification of the monetary policy shock than conventional VAR models: The fact that the set of variables considered by the researcher in a small scale VAR is likely to be less comprehensive than that taken into account by financial market participants and the Federal Reserve, can give rise to an omitted variable problem. Therefore, by applying rank reduction techniques I aim to base my analysis on an information set that resembles the central bank’s monitoring of inflation.<sup>2</sup> 

My data set for the US has a monthly frequency and runs from February 1976 to June 2005. Building on Bernanke et al. (2005), the data include a balanced panel of 118 monthly macroeconomic time series from which I extract 5 unobserved factors. For comparability to other empirical studies on the state dependency of monetary policy, I extend this dataset by the Excess Bond Premium (EBP) (Gilchrist and Zakrajˇsek (2012)) and in an additional exercise by cross-sectoral series for prices and quantities (see section 4.2). The series are standardized and transformed so as to induce stationary. Table 2 in Section B of the Appendix lists the macroeconomic and financial series considered in this study as well as its transformations and sources. The inclusion of unobserved factors carries the additional advantage that the responses of all the variables contained in the panel to a monetary policy shock can be mapped. 

The business cycle is traditionally defined as a cycle of expansions and contractions in economic activity. Commonly accepted definitions, such as that from the National Bureau of Economic Research (NBER), characterize a recession as two consecutive quarters of negative growth in key indicators such as GDP. An alternative measure is the output gap, which considers periods when the actual output is below potential. 

Econometric approaches, such as Markov switching models, smooth transition models, and Dynamic Stochastic General Equilibrium (DSGE) models, provide a nuanced view of business cycles by capturing regime changes and shifts in statistical properties over time. These models link economic theory with empirical data, offering insights into the propagation of policy shocks. They also enhance understanding of the nonlinear and stochastic characteristics of business cycles, surpassing simpler definitions based on consecutive quarters of negative growth. The Markov switching model, introduced by Hamilton (1989), identifies regimes in economic data, thus capturing the dynamic transitions between different phases of the cycle. This model helps identify periods of expansion and contraction by examining shifts in statistical properties over time. Additionally, smooth transition models, such as those developed by Terasvirta and Anderson (1992), enhance this analysis by allowing for gradual rather than abrupt changes between regimes, which better reflect real economic conditions. DSGE models for business cycle estimation (e.g., Smets and Wouters (2007)), incorporate microeconomic foundations and 

> 2For an articulation of this argument refer to Sims (1992) or Boivin et al. (2009). 

ECB Working Paper Series No 2983 

7 

frictions, providing a robust framework for analyzing policy impacts on business cycles. 

Moreover, latent variable models, such as Dynamic Factor models, have been instrumental in distinguishing and analyzing business cycle fluctuations by estimating and interpreting common dynamic factors from economic data, as discussed by Stock and Watson (1989), Diebold and Rudebusch (1996), or Kim and Nelson (1998). This study exploits the information content of large datasets not only to better identify and disentangle structural shocks but also to extract a real economic activity factor. The real economic activity factor captures the intricate dynamics of the economy by synthesizing common fluctuations across various sectors and variables. This factor leverages information embedded in real activity data and exhibits a strong correlation with established business cycle indicators, such as the Chicago National Activity Index.<sup>3</sup> 

The performance of the real economic activity factor in proxying the business cycle is further evaluated through a recursive forecasting exercise. This exercise tests Hamilton (2018)’s assertion that negative prediction errors are associated with recessions. Using a bivariate QBVAR model for the US, which includes the level of industrial production and either the median (50<sup>_th_</sup> quantile) or the lower decile (10<sup>_th_</sup> quantile) of the real economic activity factor, I assess the effectiveness of the factor and its quantiles in capturing business cycle dynamics and overall economic conditions. The results of this exercise, detailed in Section A of the Appendix, align with Hamilton’s findings for US employment: the median specification results in negative forecast errors one year ahead of financial crises, while the 10<sup>_th_</sup> quantile specification yields positive or near-zero forecast errors. This evidence supports the claim that the median real economic activity factor serves as a reliable proxy for cyclical real economic developments, and that the 10<sup>_th_</sup> quantile effectively captures recessions by driving forecast errors to zero and above. 

In the following, to gauge the state of the economy, the conditional tails of the real economic activity factor are analyzed to represent expansions (right-hand tail) or recessions (left-hand tail). Carrying out the analysis separately for expansions and recessions I inspect if there are differences across the quantiles of the response variable’s distribution. 

The large set of _N_ -observable ”informational” series _Xt_ , is related to the unobserved common factors according to the observation equation 



where Λ is a matrix of factor loadings and _ϵt_ contains series specific components that are uncorrelated with _Ft_ .<sup>4</sup> _Ft_<sup>_E_</sup> represents the real economic activity factor (extracted from subset _X_<sup>_E_</sup> ) and _Ft_<sup>_X_</sup> is the set of _k_ common factors extracted from _Xt_ after removing influence of _Ft_<sup>_E_.</sup><sup>_Ct_isavectorthatcombinestheunobservedfactorsandthefederalfundsrate</sup><sup>_Rt_,which</sup> 

> 3Similar to Mumtaz (2010), the real economic activity subsample consists of variables related to real output and income, consumption, housing starts, and inventories. Refer to Section B of the Appendix for a more precise description of the series classification. To remove the influence of real activity from the other variables, I regress the remaining series on the real activity factor and store the residuals. These residuals represent the rest of the panel, cleaned of the impact of real economic activity. 

> 4Only fast moving variables in _Xt_ are allowed to have a contemporaneous relationship with _Rt_ . An extensive explanation is available in section 2.3. 

ECB Working Paper Series No 2983 

8 

measures of the stance of monetary policy. 

### **2.2 A Bayesian quantile FAVAR model** 

Quantile regressions complement least squares regression. Two differences arise between the two methods: First, the quantile regression minimizes the sum of absolute errors, instead of the sum of squared errors. Second, the quantile regression places different varying weights on the error terms depending on whether these are below or above the quantile (e.g. Adrian et al. (2019)). Moreover, in frequentist settings the location of the random variable is defined through the minimization of the quantile regression criterion function also known as the ”checkloss function” (Koenker and Bassett (1978)). Yu and Moyeed (2001) show that the ”check-loss function” is related to the likelihood function for the asymmetric Laplace distribution. By forming the likelihood function based on the asymmetric Laplace distribution, they introduced Bayesian inference in the context of quantile regression. 

Since the seminal work of Koenker and Bassett (1978) the literature has seen a large number of applications of quantile regression approaches in the field of risk management to calculate risk measures (e.g. Engle and Manganelli (2004), Chen et al. (2012) and White et al. (2015)) and, more recently, in the field of macroeconomics to measure tail risks to output growth (e.g. Adrian et al. (2019), Figueres and Jaroci´nski (2020) or Chavleishvili and Manganelli (2024)). 

Two relevant multivariate extensions of regression quantile models are the vector autoregressive (VAR) quantile model proposed in White et al. (2015) and Bayesian quantile VAR suggested in Sch¨uler (2020). My approach consists in an extension of Sch¨uler (2020)’s VAR framework to consider a large amount of information about the economy incorporating common factors extracted from a large cross section of indicators. 

For given _Ct_ and for fixed quantile values _τ_ = ( _τ_ 1 _, τ_ 2 _, ..., τd_ )<sup>_′_</sup> the transition equation (2) describes the joint dynamics of _Ft_ and _Rt_ as a reduced form QBVAR. 



_Ai|τ Ct−i_ denotes the _dxd_ matrix of lagged coefficients, with _t_ = 1 _, ..., T_ and _d_ = _k_ +1<sup>_obs_</sup> +1<sup>_E_</sup> . _ντ_ contains the intercepts and _vt|τ_ = ( _v_ 1 _t|τ_ 1 _, ..., vdt|τd_ )<sup>_′_</sup> is a vector of error terms which is distributed following a multivariate Laplace distribution.<sup>5</sup> 

### **2.3 Identification** 

My baseline specification sets the Fed’s policy instrument, the federal funds rate ( _Rt_ ), as the observable variable. The monetary policy shock is identified recursively by ordering _Rt_ last and considering its innovations as policy shocks. The recursive ordering implies that the factors will not react to a shock to monetary policy shock contemporaneously but within a month. Given that this assumption might not be valid for some of the variables in the panel I perform a categorization into two subsets based on the dynamics of their response to monetary policy shocks. Fast-moving variables are allowed to respond contemporaneously to unanticipated changes in 

> 5Refer to Sch¨uler (2020) for the detailed proof. 

ECB Working Paper Series No 2983 

9 

the fed funds rate. While slow-moving variables are assumed to respond within a period to the monetary policy shock. The classification of these variables follow Bernanke et al. (2005).<sup>6</sup> 

Following Sch¨uler (2020) I perform pseudo-structural analysis. The focus of this approach is to summarize the common fluctuations of the disturbances at their selected quantiles and not at their first moment. Therefore, instead of the covariance matrix I study the co-exceedance measure introduced by Blomqvist (1950) and Koenker and Portnoy (1990), which captures the common fluctuation of the error terms around quantiles. Sch¨uler (2020) proposes to identify the pseudo-structural shocks _ηt|τ_ = ( _η_ 1 _t|τ , .., ηdt|τ_ )<sup>_′_</sup> through the Cholesky decomposition Γ _τ_ = _Hτ Hτ_<sup>_′_.</sup> The pseudo-structural shocks conditional on a vector of quantiles are defined as 



˜ ˜ where˜ _ϕ_<sup>˜</sup> _τ_ ( _vt|τ_ ) = ( _ϕfτv_ 11( _tv|τ_ 11 _t|_ (0) _τ_ 1)<sup>_, ...,_</sup> _ϕfτvdt_ 1( _v|τddt|_ (0) _τd_ <u>)</u><sup>)</sup><sup>_′_with mean zero and unit variance, indicator function</sup> _ϕτj_ ( _vjt|τj_ ) = _τj −_ 1 (( _vjt|τj_ ) _<_ 0) _,_ 1 and _j ∈{_ 1 _, . . . , d}_ . _fvjt|τj_ (0) is the probability density function of _v_ evaluated at 0. _jt|τj_ 

Combining the previous blocks, the response to the monetary policy shock is retrieved through the pseudo quantile impulse response function.<sup>7</sup> The pseudo quantile impulse function captures marginal impact of marginal shock j on the system. _Qτ_ ( _Ct_ + _h|_ 𭟋 _t−_ 1) defines the baseline scenario and _Q_<sup>ˇ</sup> _τ_ ( _Ct_ + _h|ηjt|τ ,_ 𭟋 _t−_ 1) the shock scenario. 



### **2.4 Overview of the empirical approach** 

The empirical method can be summarized by the following steps: 

1. Extract the economic activity factor as outlined in subsection 2.1. 

2. Remove the potential implicit dependence of _C_<sup>˜</sup> ( _Ft, Yt_ ) on _Rt_ : 

   - (i) Compute the components that are not _Rt_ ( _C_<sup>˜</sup><sup>_∗_</sup> ( _Ft_ )) by performing principal component analysis on the subset of slow-moving variables. 

   - (ii) Run the multiple regression of the form 







3. Estimate a Quantile FAVAR in _Ct_ . 

4. Identify the Monetary Policy shock applying a recursive identification scheme. 

> 6The sections B and C of the Appendix identify the variables in the dataset that are classified as slow-moving. 

> 7The quantile pseudo-impulse response functions conceptually build the generalized impulse response functions presented in Koop et al. (1996). 

ECB Working Paper Series No 2983 

10 

Carry out 3 and 4 separately for different states of the business cycle by conditioning on the 10<sup>_th_</sup> quantile of the real economic activity factor for recessions and on the 90<sup>_th_</sup> quantile for expansions. 

## **3 Monte Carlo simulations** 

I employ Monte Carlo simulations to evaluate the effectiveness of the BQVAR model in capturing asymmetries and accurately identifying underlying nonlinear patterns in the data.<sup>8</sup> These patterns are generated by a state-dependent Threshold VAR (TVAR) model, which features regime-switching dynamics and state-contingent impulse responses. 

Following the methodology and calibration in Mumtaz and Piffer (2022), the model takes the form of a recursive TVAR that switches between two regimes based on the lagged value of the third endogenous variable, in line with the TVAR models outlined in Tsay (1998) and Castelnuovo and Pellegrino (2018). The system is defined as: 







The dynamics of the data-generating process (DGP) are determined by the following parameterization: 



I start by computing the true generalized impulse response to a one-standard-deviation shock to _y_ 3 _t_ in regime 1, with the initial condition set to _y_ 0 = 0. I then assess the extent to which the linear BVAR and the QBVAR—conditioned at the 10<sup>th</sup> percentile of the distribution—are able to replicate the true impulse responses. To this end, I simulate a dataset with 300 observations, discard the initial 100, and estimate impulse responses using the remaining 200. 

For the linear BVAR, I compute conventional impulse responses. For the QBVAR, I extract 

> 8The Monte Carlo simulations build on a BQVAR rather than a BQFAVAR to assess whether the quantilebased setup is well suited to capturing state-dependent asymmetries. Since a BQFAVAR would merely scale the impulse responses by factor loadings, a BQVAR is sufficient to evaluate the model’s ability to recover asymmetric effects across quantiles. 

ECB Working Paper Series No 2983 

11 

the median of the pseudo quantile impulse responses from 2,000 posterior draws. This exercise is repeated across 100 Monte Carlo replications. Each model is estimated with a single lag. 



Estimated impulse responses from the Threshold VAR model in response to a one-standard-deviation shock to _y_ 3, starting in regime 1. The pink solid line shows the regime-1 linear response, the black squares trace the true generalized impulse response accounting for endogenous regime switching, and the dashed line displays the linear BVAR estimate. The shaded bands represent the dispersion across the 100 median estimated pseudo quantile responses obtained from the QBVAR. 

Figure 1: Monte Carlo simulation Threshold VAR 

The shock is initiated when the system is in regime 1. In a linear framework, the response would remain confined to regime 1, with dynamics fully characterized by (Π1 _, B_ 1). However, due to the model’s nonlinear structure, regime switching occurs endogenously as a function of the response of _y_ 3 _t_ . Figure 1 illustrates the results. The pink solid line depicts the regime1-specific impulse response under linearity, while the black squares trace the true generalized impulse response that incorporates transitions across regimes. The two diverge notably. The dashed line reflects the estimate from the linear BVAR, which predictably falls between the purely linear and the fully nonlinear responses. In contrast, the QBVAR provides a much closer approximation to the true generalized response. It accurately captures the trajectories of all three variables, identifying that the transition dynamics amplify the responses of the first two variables relative to a linear model constrained to a single regime. 



Estimated impulse responses from a linear VAR model in response to a one-standard-deviation shock to _y_ 3. The pink solid line shows the regime-1 linear response, the black squares trace the true generalized impulse response accounting for endogenous regime switching, and the dashed line displays the linear BVAR estimate. The shaded bands represent the dispersion across the 100 median estimated pseudo quantile responses obtained from the QBVAR. 

Figure 2: Monte Carlo simulation linear VAR. 

In a second exercise, I generate data from a DGP in which the economy remains in regime 1 

ECB Working Paper Series No 2983 

12 

throughout, thereby eliminating any endogenous regime switching. In this linear setting, shown in Figure 2, the impulse responses produced by the QBVAR and the linear BVAR estimators are nearly identical. This result highlights that the QBVAR does not impose nonlinearities when none are present in the underlying DGP. 

Overall, this exercise confirms that the proposed methodology is well-suited to capture asymmetric dynamics when they are present, while not imposing any asymmetries when the true data-generating process is linear. This finding reinforces the validity of the approach for studying nonlinear responses across different states of the economy. The empirical application of the methodology is presented in the following section. 

## **4 Empirical analysis** 

This section presents the empirical results from the BQFAVAR model. The analysis proceeds in two steps. First, I examine the aggregate responses of key macroeconomic indicators to a contractionary monetary policy shock, assessing not only their average dynamics but also how these responses vary across different states of the economy. The results are benchmarked against those from earlier studies to validate the performance of the model. Second, I turn to the sectoral dimension of the transmission mechanism, focusing on the state-dependent behavior of disaggregate prices and quantities. 

### **4.1 Aggregate responses to a contractionary monetary policy shock** 

#### **4.1.1 Key macroeconomic aggregates** 

In this section, I discuss the response of my data series to an unexpected increase of 25 basis points in the federal funds rate both, on an aggregate and sectoral level. Prior to studying the asymmetries in the impact of monetary policy across the business cycle, I relate my results for key macroeconomic aggregates to those reported by previous studies in the first column of Panel A: The black lines display the results as in Boivin et al. (2009) and the blue line corresponds to the BQFAVAR model. 

The dotted lines show the results from a small-scale VAR under two different specifications and the solid black line displays the FAVAR results.<sup>9</sup> The solid blue line shows the median quantile pseudo impulse responses of my baseline specification to a contractionary monetary policy shock.<sup>10</sup> The baseline specification considers the conditional median of 5 factors and of the federal funds rate. The graphic assessment shows that the BQFAVAR baseline results resemble those of the canonical paper for all three variables. Unlike the small-sized VARs, FAVAR approaches exploit the relevant information contained in the large dataset. Therefore, the FAVAR response of the price level does not display a price puzzle and the response of 

> 9The first VAR specification includes industrial production, the CPI and the federal funds rate and the second augments specification one with the first principal component of the large dataset. The FAVAR specification is based on 5 factors and the federal funds rate. 

> 10The choice of the 50 _th_ quantile, representing periods that are neither distinctly expansions nor contractions, enhances comparability with the findings of the canonical paper, where no distinction is made across economic states. 

ECB Working Paper Series No 2983 

13 

industrial production is more conventional than that of the VARs.<sup>11</sup> 

Figure 3 depicts that after a year an increase of the policy rate by 25 basis points reduces the level of industrial production by 0.14 per cent during an expansion (green) and by twice this magnitude during a recession (red). These results resemble those of Peersman and Smets (2002) and Bruns and Piffer (2021) for real GDP growth.<sup>12</sup> On the contrary, Tenreyro and Thwaites (2016) find stronger effects of monetary policy shocks on GDP during expansions than during recessions. The authors attribute this discrepancy, among other reasons, to the counteracting (or reinforcing) impact of fiscal policy during recessions (booms). 

Table 1: Share of posterior draws for which recession responses exceed expansion responses 

||**Hor**|**izon**|
|---|---|---|
||1 year|4 years|
|Industrial Production (IP)|97%|35%|
|CPI Infation (CPI)|76%|61%|
|Excess Bond Premium (EBP)|97%|33%|



**Notes:** The table reports the proportion of posterior draws for which the cumulative response to a contractionary monetary policy shock is larger during recessions than during expansions, at one-year and four-year horizons. Higher values indicate greater asymmetry in the response across business cycle phases. 

The third and fourth columns of Figure 3 show the joint distribution for the cumulated pseudo impulse response over a year and after 4 years of the expansion and recessions. Values of the expansion periods are plotted on the x-axis, and the associated value of a recession period is shown on the y-axis. Those combinations clustered near the 45<sup>_◦_</sup> line represent pairs for which there was little or no change between the business cycle phases and the draws that are located above the 45<sup>_◦_</sup> line represent a higher effect of monetary policy in recessions. At the 1-year horizon the stronger reaction of the observable variables during an expansion is non-negligible with at least 97% of the joint distribution being above the 45<sup>_◦_</sup> line for industrial production and 76% for inflation (Table 1). The evidence for differences across the business cycle phase is less clear at the longer horizon of 4 years. 

Overall, the findings presented in Figure 3 and Table 1 suggest weaker evidence of statedependent asymmetries in the response of inflation to a monetary policy shock compared to output. This phenomenon may be attributed, as suggested by Santoro et al. (2014), to households’ aversion to losses within the framework of reference-dependent preferences, as introduced by Kahneman and Tversky (1979) and commonly known as ’prospect theory’. Consistent with the central principle of prospect theory, losses in consumption utility have a greater impact than gains. Additionally, inflation responses are further dampened due to heightened real rigidity in the labor market 

> 11For an articulation of this argument refer to Bernanke et al. (2005). 

> 12In Peersman and Smets (2002) a one standard deviation shock is imposed. While in Bruns and Piffer (2021) the size of the shock is equivalent to that imposed in this study (25 basis points), the sign of the shock changes depending on the business cycle phase. 

ECB Working Paper Series No 2983 

14 



<!-- Start of picture text -->
PANEL A<br>0.3 0.3<br>10<br>0.2<br>0.2<br>2 5<br>0.1<br>0.1<br>0 0<br>-0.1 0 1<br>1 2 0 5 10<br>Expansion Expansion<br>0 0 0 0.2<br>0<br>-0.1 -0.2<br>-0.2<br>-0.2 -0.2<br>-0.4<br>-0.4<br>-0.3<br>-0.2-0.1 0 -0.4-0.2 0<br>Expansion Expansion<br>0 0 0.1 0.2<br>0<br>-0.1 -0.05 0<br>-0.2<br>-0.1<br>-0.2 -0.1 -0.4<br>0 0.1 -0.4 0<br>horizon horizon Expansion Expansion<br>BGM FAVAR QBFAVAR0.9 horizon = 1 year horizon = 4 years<br>VAR QBFAVAR<br>0.1<br>VAR & 1 factor<br>QBFAVAR<br>0.5<br>0 12 24 36 48 0 12 24 36 48<br>0 12 24 36 48 0 12 24 36 48<br>0 12 24 36 48 0 12 24 36 48<br>Recession Recession<br>Federal Funds Rate<br>Recession Recession<br>Industrial Production<br>Recession Recession<br>Price Level (log): CPI<br><!-- End of picture text -->

Figure 3: Response to an increase of 25 basis points in the federal funds rate. First two columns display response functions. Black lines display impulse response functions as in Boivin et al. (2009). For QBFAVAR the pseudo-impulse responses are reported. Green lines characterize expansions and red lines recessions. Scatter plots display the relation between expansion periods (x-axis) and recessions ( y-Axis) at horizon of 1 year (cyan) and horizon of 4 years (grey). 

ECB Working Paper Series No 2983 

15 

#### **4.1.2 Financial variables** 

Figure 4 illustrates the state-dependent impact of a contractionary monetary policy shock on the EBP. Increases in the EBP serve as proxies for heightened external finance premiums. In accordance with the ’balance-sheet’ strain theory of the credit channel, the EBP exhibits a stronger response during recessions, with 97% of the draws lying above the 45-degree line at the 1-year horizon (see Table 1) . 



<!-- Start of picture text -->
0.03<br>0.35<br>0.5<br>0.3<br>0.02<br>0.4<br>0.25<br>0.01 0.3<br>0.2<br>0.2<br>0 0.15<br>0.1<br>0.1<br>-0.01<br>0 12 24 36 48 0.1 0.15 0.2 0.1 0.2 0.3 0.4 0.5<br>Expansion Expansion<br>QBFAVAR<br>0.9<br>QBFAVAR0.1 horizon = 1 year horizon = 4 years<br>Recession Recession<br>Excess Bond Premium<br><!-- End of picture text -->

Figure 4: Pseudo-impulse responses to an increase of 25 basis points in the federal funds rate. Green lines characterize expansions and red lines recessions. Scatter plots display the relation between expansion periods (x-axis) and recessions (y-Axis) at the horizon of 1 year (cyan) and the horizon of 4 years (grey). 

The ’financial accelerator’ propagation mechanism posits that asymmetrical information between borrowers and lenders results in an external finance premium, which is typically contingent upon the borrower’s net worth. Borrowers with higher net worth can provide more collateral, thereby reducing their external financing costs. 

Bernanke and Gertler (1995) explore the ’balance-sheet’ channel of the credit channel theory, where changes in short-term interest rates influence capital costs and the external finance premium. This dependency on borrower net worth gives rise to a ’financial accelerator’ propagation mechanism. Consequently, policy tightening raises capital costs through the interest rate channel and reduces collateral values and cash flow, which in turn positively impacts the external finance premium. Thus, monetary policy’s effect is most pronounced during periods of heavy reliance on external financing.<sup>13</sup> 

According to this theory, such asymmetries stem from deteriorating balance sheet quality, typically observed during economic downturns, leading to increased reliance on external financing and a corresponding rise in the external finance premium. This higher premium amplifies the impact of monetary policy shocks by strengthening the traditional interest rate channel. 

> 13See for example Blinder (1987), Gertler and Hubbard (1988), or Kiyotaki and Moore (1997). 

ECB Working Paper Series No 2983 

16 

My findings for the financial variables align with those reported by other empirical studies on the state dependency of the impact of monetary policy shocks, such as Tenreyro and Thwaites (2016), who also document a higher response of financial variables during recessions.<sup>14</sup> Other studies, such as Bruns and Piffer (2021), report results of similar magnitude to mine. 

### **4.2 Exploration of price rigidities** 

This section examines the dynamics of disaggregate quantity and price responses to a contractionary monetary policy shock throughout the business cycle. The analysis of relative prices elucidates the extent to which monetary policy shocks induce real effects. Transitory fluctuations in real economic activity would result from a rapid and uniform adjustment of individual prices (see Baumeister et al. (2013)). Additionally, as emphasized by Aoki (2001) and Balke and Wynne (2007), focusing solely on the responses of aggregate price measures may not always offer a comprehensive understanding of the monetary transmission mechanism. 

Overall, my findings align with the predictions of ’Menu-costs models’, which elucidate the asymmetric responses to monetary policy shocks characterized by stronger downward than upward price rigidity. This suggests that negative fluctuations are primarily reflected in output. 

#### **4.2.1 Sectoral responses** 

Disaggregated responses offer valuable insights for the formulation of monetary policy. Therefore, I replicate the analysis outlined in Section 4.1 using the extensive dataset from Boivin et al. (2009). This dataset augments that of Bernanke et al. (2005) by including granular consumption and price series. Details on the sources and transformations of the sectoral producer price and personal consumption series are included in Section C of the Appendix.<sup>15</sup> 

Figure 5 depicts the median quasi-impulse response functions of the sectoral components of the personal consumption expenditure deflator and its corresponding real quantities following a contractionary policy shock of 25 basis points during two distinct phases of the business cycle. Recessions are displayed in the first column, and expansions are depicted in the second column. The solid lines represent the median responses of the aggregate price deflation and real consumption, while the dashed black lines represent the unweighted average of the granular responses. 

The dynamics of the mean of the granular price and quantity responses resemble those of the aggregate indices. In line with Bernanke et al. (2005), Boivin et al. (2009) or Baumeister et al. (2013) I find no evidence of a price puzzle for the aggregate price level measure. However, at the granular level, some sectors exhibit a temporary price puzzle. While there is notable heterogeneity across sectoral responses in terms of magnitude and direction, the asymmetry with respect to the business cycle phase is less pronounced compared to key macroeconomic aggregates and financial variables studied earlier. Nonetheless, granular price responses exhibit 

> 14Tenreyro and Thwaites (2016) find that the external finance premium amplifies the monetary policy shock in a recession and counteracts it during an expansion. 

> 15The dataset from Bernanke et al. (2005) spans from 1951:M01 to 2000:M07, but since the granular consumption and price series are available starting in 1976 in Boivin et al. (2009), the sample size is limited to 1976:M01-2000:M07. 

ECB Working Paper Series No 2983 

17 

discernible asymmetries relative to the state of the economy, with a larger proportion trending towards the negative territory in the medium term during recessions compared to expansions. 



<!-- Start of picture text -->
PANEL B<br>PCE Prices - Recession PCE Prices - Expansion<br>1 1<br>0 0<br>-1 -1<br>-2 -2<br>0 12 24 36 48 0 12 24 36 48<br>PCE Quantities - Recession PCE Quantities - Expansion<br>1 1<br>0 0<br>-1 -1<br>-2 -2<br>0 12 24 36 48 0 12 24 36 48<br>horizon horizon<br>percent percent<br>percent percent<br><!-- End of picture text -->

Figure 5: Estimated quasi-impulse responses: Top row displays the response of disaggregate prices during an recession (red) or expansion (green), bottom row that of disaggregate quantities. The monetary shock is a surprise increase of 25 basis points in the federal funds rate. Solid red and green lines represent the aggregate PCE deflator (top row) and real consumption (bottom row). Dashed black lines depicts the unweighted average of individual responses. 

#### **4.2.2 Cross-sectoral distribution of prices and quantities** 

I offer an alternative depiction of the effects of monetary shocks on disaggregated responses by presenting their entire distribution. Figure 6 displays the cross-sectoral smoothed densities of prices at selected horizons in the top row and of quantities in the bottom row. 

For both prices and quantities, the distribution widens around 0 at longer horizons. A progression from primarily positive to negative price responses is observable. As posited in Baumeister et al. (2013), the progressive increase in dispersion over time accentuates the differences in speed and size of the adjustments. 

During expansions, the response of disaggregate prices in the short term appears to be symmetrically bounded around zero, with a higher density at the origin compared to recessions. Moreover, the distribution of cross-sectoral price responses is slightly left-skewed during reces- 

ECB Working Paper Series No 2983 

18 



<!-- Start of picture text -->
PANEL C<br>hor = 1 year hor = 4 years<br>10 4<br>8<br>3<br>6<br>2<br>4<br>1<br>2<br>0 0<br>-0.6 -0.4 -0.2 0 0.2 0.4 -2 -1 0 1 2<br>4 2<br>3 1.5<br>2 1<br>1 0.5<br>0 0<br>-1.5 -1 -0.5 0 0.5 -2 -1 0 1 2 3<br>PCE Prices<br>PCE Quantities<br><!-- End of picture text -->

Figure 6: Smoothed densities of disaggregate responses to a 25 basis points increase in the federal funds rate at selected horizons and different states of the business cycle. Red lines represent the responses during a recession and green lines represent the response during an expansion. 

sions. This implies that the shock leads to price increases in a larger share of sectors during downturns, but also that in some areas, the price adjustment involves more extreme reductions in the near term. 

The cross-sectoral distribution of quantities shifts to the right of the origin during recessions. These results support the predictions of ’Menu-costs models’, which explain this asymmetry in response to monetary policy shocks through stronger downward than upward price rigidity.<sup>16</sup> This implies that negative fluctuations are primarily mirrored in output. 

## **5 Conclusion** 

Understanding whether the effectiveness of monetary policy varies across different phases of the business cycle remains a central issue in the empirical literature. The question remains open to debate: while early studies often found stronger effects during recessions, more recent contributions, including Tenreyro and Thwaites (2016) have suggested the opposite. As highlighted by Piger and Stockwell (2025), these findings are sensitive to key empirical choices, suggesting a persistent lack of consensus in the literature on the direction of the asymmetry. 

This paper contributes to the debate by proposing a flexible empirical framework to evaluate state-dependent monetary policy transmission, both at the aggregate and sectoral levels. I develop a Bayesian Quantile Factor-Augmented VAR (BQFAVAR), a nonlinear extension of 

> 16See, for instance, Ball and Mankiw (1994) and Senda (2001). 

ECB Working Paper Series No 2983 

19 

the FAVAR model introduced by Bernanke et al. (2005), which introduces quantile dependence directly in the transition equation. This structure allows the dynamics of latent macroeconomic forces to vary across the conditional distribution of a real activity indicator, thereby enabling the assessment of asymmetries in the propagation of structural shocks across economic states. Moreover, by extracting latent factors from a large set of macroeconomic indicators, the model revisits the state-dependence of monetary policy while accounting for multivariate drivers of the business cycle, and improves identification by mitigating omitted variable bias. 

Monte Carlo simulations confirm the model’s ability to recover nonlinear impulse responses driven by state dependence. When applied to a rich U.S. macroeconomic dataset covering the period from February 1976 to June 2005—and comprising approximately 600 variables, including sector-level price and quantity indicators—the BQFAVAR framework produces results that are consistent with established benchmarks. Under median economic conditions, the model replicates the average responses reported in Bernanke et al. (2005), Boivin et al. (2009), and Baumeister et al. (2013), notably avoiding the price puzzle and yielding plausible dynamics for industrial production and inflation. 

Importantly, when conditioning on the tails of the real activity factor—used to proxy for recessions and expansions—the model uncovers clear evidence of state-contingent transmission. Consistent with the financial accelerator mechanism Bernanke and Gertler (1995), the responses of output and financial variables to contractionary monetary policy shocks are markedly stronger during recessions, when firms’ balance sheets are weaker and reliance on external finance increases. In contrast, inflation dynamics remain relatively stable across states, an asymmetry that may reflect a combination of downward nominal rigidity, central bank credibility, and reference-dependent preferences, as discussed by Santoro et al. (2014) and Forni et al. (2020). 

In addition, the analysis highlights the importance of sectoral heterogeneity in the transmission of monetary policy. While aggregate responses provide a useful benchmark, they may obscure important variation at the disaggregated level. Consistent with the findings of Boivin et al. (2009) and Baumeister et al. (2013), the results reveal that sector-level quantities exhibit stronger state dependence than prices, with more pronounced declines during recessions. In contrast, price responses remain relatively symmetric across the cycle, suggesting that monetary policy shocks are primarily reflected in real activity at the sectoral level. This paper contributes to a growing literature on latent factors and quantile-dependent dynamics in macroeconomic models. It emphasizes the importance of modeling the full conditional distribution of macroeconomic responses to monetary policy, particularly in light of sectoral and state-dependent heterogeneity. The findings support the inclusion of nonlinearity directly in the transmission equation for latent factors as a means to capture asymmetries in transmission across the business cycle and across sectors of the economy. 

ECB Working Paper Series No 2983 

20 

## **References** 

- Adrian, T., Boyarchenko, N., and Giannone, D. (2019). Vulnerable growth. _American Economic Review_ , 109(4):1263–89. 

- Agrippino, S. and Ricco, G. (2021). The transmission of monetary policy shocks. _Bank of England Staff Working Paper_ . 

- Ando, T. and Bai, J. (2020). Quantile co-movement in financial markets: A panel quantile model with unobserved heterogeneity. _Journal of the American Statistical Association_ , 115(529):266– 279. 

- Ando, T., Li, K., and Lu, L. (2023). A spatial panel quantile model with unobserved heterogeneity. _Journal of econometrics_ , 232(1):191–213. 

- Angeloni, I., Kashyap, A., and Mojon, B. (2003). _Monetary policy transmission in the euro area_ . Cambridge University Press. 

- Aoki, K. (2001). Optimal monetary policy responses to relative-price changes. _Journal of Monetary Economics_ , 48(1):55–80. 

- Balke, N. S. and Wynne, M. A. (2007). The relative price effects of monetary shocks. _Journal of Macroeconomics_ , 29(1):19–36. 

- Ball, L. and Mankiw, N. G. (1994). Asymmetric price adjustment and economic fluctuations. _The Economic Journal_ , 104(423):247–261. 

- Baumeister, C., Liu, P., and Mumtaz, H. (2013). Changes in the effects of monetary policy on disaggregate price dynamics. _Journal of Economic Dynamics and Control_ , 37(3):543–560. 

- Bernanke, Boivin, J., and Eliasz, P. (2005). Measuring the effects of monetary policy: a factoraugmented vector autoregressive (favar) approach. _The Quarterly Journal of Economics_ , 120(1):387–422. 

- Bernanke and Gertler, M. (1989). Agency costs, net worth, and business fluctuations. _The American Economic Review_ , 79(1):14–31. 

- Bernanke, B. S. et al. (2011). Opening remarks: The near-and longer-term prospects for the us economy. In _Proceedings-Economic Policy Symposium-Jackson Hole_ , number y: 2011: p: 1-12, pages 1–12. Federal Reserve Bank of Kansas City. 

- Bernanke, B. S. and Gertler, M. (1995). Inside the black box: the credit channel of monetary policy transmission. _Journal of Economic Perspectives_ , 9(4):27–48. 

- Blinder, A. S. (1987). Keynes, lucas, and scientific progress. _The American Economic Review_ , 77(2):130–136. 

- Blomqvist, N. (1950). On a measure of dependence between two random variables. _The Annals of Mathematical Statistics_ , pages 593–600. 

ECB Working Paper Series No 2983 

21 

- Boivin, J., Giannoni, M. P., and Mihov, I. (2009). Sticky prices and monetary policy: Evidence from disaggregated us data. _American economic review_ , 99(1):350–84. 

- Bruns, M. and Piffer, M. (2021). Monetary policy shocks over the business cycle: Extending the Smooth Transition framework. _School of Economics, University of East Anglia, Norwich, UK._ , (2021-07). 

- Castelnuovo, E. and Pellegrino, G. (2018). Uncertainty-dependent effects of monetary policy shocks: A new-keynesian interpretation. _Journal of Economic Dynamics and Control_ , 93:277– 296. 

- Chavleishvili, S. and Manganelli, S. (2024). Forecasting and stress testing with quantile vector autoregression. _Journal of Applied Econometrics_ , 39(1):66–85. 

- Chen, C. W., Gerlach, R., Hwang, B. B., and McAleer, M. (2012). Forecasting value-atrisk using nonlinear regression quantiles and the intra-day range. _International Journal of Forecasting_ , 28(3):557–574. 

- Chen, L., Dolado, J. J., and Gonzalo, J. (2021). Quantile factor models. _Econometrica_ , 89(2):875–910. 

- Clark, T. E., Huber, F., Koop, G., Marcellino, M., and Pfarrhofer, M. (2024). Investigating growth-at-risk using a multicountry nonparametric quantile factor model. _Journal of Business & Economic Statistics_ , pages 1–16. 

- Cogley, T. and Sargent, T. J. (2005). Drifts and volatilities: monetary policies and outcomes in the post wwii us. _Review of Economic Dynamics_ , 8(2):262–302. 

- Diebold, F. X. and Rudebusch, G. D. (1996). _Measuring Business Cycles: A Modern Perspective_ . Review of Economics and Statistics. 

- Dolado, J. J., Chen, L., and Gonzalo, J. (2020). Quantile factor models. 

- Dolado, J. J. and Dolores, R. M. (2001). An empirical study of the cyclical effects of monetary policy in spain (1977-1997). _Investigaciones Econ´omicas_ , 25(1):3–30. 

- Engle, R. F. and Manganelli, S. (2004). Caviar: Conditional autoregressive value at risk by regression quantiles. _Journal of Business & Economic Statistics_ , 22(4):367–381. 

- Figueres, J. M. and Jaroci´nski, M. (2020). Vulnerable growth in the euro area: Measuring the financial conditions. _Economics Letters_ , 191:109126. 

- Forni, M., Debortoli, D., Gambetti, L., and Sala, L. (2020). Asymmetric effects of monetary policy easing and tightening. Technical report, CEPR Discussion Paper No. 15005. 

- Forni, M., Gambetti, L., Maffei-Faccioli, N., and Sala, L. (2023). The impact of financial shocks on the forecast distribution of output and inflation. Working Paper 2023/3, Norges Bank. 

- Friedman, M. and Schwartz, A. J. (1963). _A Monetary History of the United States, 1867-1960_ . Princeton University Press. 

ECB Working Paper Series No 2983 

22 

- Gertler, M. and Hubbard, R. G. (1988). Financial factors in business fluctuations. _NBER working paper 2758_ . 

- Gilchrist, S. and Zakrajˇsek, E. (2012). Credit spreads and business cycle fluctuations. _American Economic Review_ , 102(4):1692–1720. 

- Graham, F. D. (1930). _Exchange, prices, and production in hyper-inflation: Germany, 19201923_ , volume 1. Ludwig von Mises Institute. 

- Hamilton, J. D. (1989). A new approach to the economic analysis of nonstationary time series and the business cycle. _Econometrica_ , 57(2):357–384. 

- Hamilton, J. D. (2018). Why you should never use the hodrick-prescott filter. _Review of Economics and Statistics_ , 100(5):831–843. 

- Iacopini, M., Ravazzolo, F., and Rossini, L. (2022). Bayesian multivariate quantile regression with alternative time-varying volatility specifications. 

- Kahneman, D. and Tversky, A. (1979). Prospect theory: An analysis of decision under risk. _Econometrica_ , 47(2):263–291. 

- Keynes, J. M. (1937). The general theory of employment. _The quarterly journal of economics_ , 51(2):209–223. 

- Kim, C.-J. and Nelson, C. R. (1998). Business cycle turning points, a new coincident index, and tests of duration dependence based on a dynamic factor model with regime switching. _Review of Economics and Statistics_ , 80(2):188–201. 

- Kiyotaki, N. and Moore, J. (1997). Credit cycles. _Journal of political economy_ , 105(2):211–248. 

- Koenker, R. and Bassett, G. (1978). Regression quantiles. _Econometrica: journal of the Econometric Society_ , pages 33–50. 

- Koenker, R. and Portnoy, S. (1990). M estimation of multivariate regressions. _Journal of the American Statistical Association_ , 85(412):1060–1068. 

- Koop, G. and Korobilis, D. (2014). A new index of financial conditions. _European Economic Review_ , 71:101–116. 

- Koop, G., Pesaran, M. H., and Potter, S. M. (1996). Impulse response analysis in nonlinear multivariate models. _Journal of Econometrics_ , 74(1):119–147. 

- Korobilis, D. and Schr¨oder, M. (2024a). Monitoring multi-country macroeconomic risk: A quantile factor-augmented vector autoregressive (qfavar) approach. _Journal of Econometrics_ , page 105730. 

- Korobilis, D. and Schr¨oder, M. (2024b). Probabilistic quantile factor analysis. _Journal of Business & Economic Statistics_ , pages 1–14. 

ECB Working Paper Series No 2983 

23 

- Lo, M. C. and Piger, J. (2005). Is the response of output to monetary policy asymmetric? evidence from a regime-switching coefficients model. _Journal of Money, credit and Banking_ , pages 865–886. 

- Ma, S., Linton, O., and Gao, J. (2021). Estimation and inference in semiparametric quantile factor models. _Journal of Econometrics_ , 222(1):295–323. 

- Mumtaz, H. (2010). Evolving uk macroeconomic dynamics: a time-varying factor augmented var. _Bank of England Working Paper_ . 

- Mumtaz, H. and Piffer, M. (2022). Impulse response estimation via flexible local projections. _arXiv preprint arXiv:2204.13150_ . 

- Peersman, G. and Smets, F. (2002). Are the effects of monetary policy in the euro area greater in recessions than in booms. _Monetary Transmission in Diverse Economies_ , pages 28–48. 

- Peersman, G. and Smets, F. (2005). The industry effects of monetary policy in the euro area. _The Economic Journal_ , 115(503):319–342. 

- Piger, J. and Stockwell, T. (2025). Are the effects of monetary policy larger in recessions? a reconciliation of the evidence. _The Journal of Economic Asymmetries_ , 31:e00394. 

- Santoro, E., Petrella, I., Pfajfar, D., and Gaffeo, E. (2014). Loss aversion and the asymmetric transmission of monetary policy. _Journal of Monetary Economics_ , 68:19–36. 

- Sch¨uler, Y. S. (2020). The impact of uncertainty and certainty shocks. _Deutsche Bundesbank Discussion Paper_ . 

- Senda, T. (2001). Asymmetric effects of money supply shocks and trend inflation. _Journal of Money, Credit and Banking_ , pages 65–89. 

- Sims, C. A. (1992). Interpreting the macroeconomic time series facts: The effects of monetary policy. _European economic review_ , 36(5):975–1000. 

- Smets, F. and Wouters, R. (2007). Shocks and frictions in us business cycles: A bayesian dsge approach. _American Economic Review_ , 97(3):586–606. 

- Stock, J. H. and Watson, M. W. (1989). New indexes of coincident and leading economic indicators. _NBER Macroeconomics Annual_ , 4:351–394. 

- Stock, J. H. and Watson, M. W. (2002). Forecasting using principal components from a large number of predictors. _Journal of the American statistical association_ , 97(460):1167–1179. 

- Tenreyro, S. and Thwaites, G. (2016). Pushing on a string: Us monetary policy is less powerful in recessions. _American Economic Journal: Macroeconomics_ , 8(4):43–74. 

- Terasvirta, T. and Anderson, H. M. (1992). Characterizing nonlinearities in business cycles using smooth transition autoregressive models. _Journal of Economic Dynamics and Control_ , 16:501–534. 

ECB Working Paper Series No 2983 

24 

- Tsay, R. S. (1998). Testing and modeling multivariate threshold models. _journal of the american statistical association_ , 93(443):1188–1202. 

- Weise, C. (1999). The asymmetric effects of monetary policy: A nonlinear vector autoregression approach. _Journal of Money, Credit and Banking_ , 31(1):85–108. 

- White, H., Kim, T.-H., and Manganelli, S. (2015). Var for var: Measuring tail dependence using multivariate regression quantiles. _Journal of Econometrics_ , 187(1):169–188. 

- Yu, K. and Moyeed, R. A. (2001). Bayesian quantile regression. _Statistics and Probability Letters_ , 54(4):437–447. 

ECB Working Paper Series No 2983 

25 

## **Appendix** 

### **A Properties of the real economic factor** 

Hamilton (2018) asserts that negative prediction errors are associated with recessions, highlighting that cyclical factors are the primary reasons for prediction errors in macro and financial variables. To evaluate the effectiveness of the real economic activity factor in capturing the business cycle and its conditional tails in representing expansions (right tail) or recessions (left tail), I conduct a one-year-ahead forecast of industrial production levels using a bivariate QBVAR model for the US. This model comprises industrial production and either the median (50<sup>_th_</sup> quantile) or the lower decile (10<sup>_th_</sup> quantile) of the real economic activity factor.<sup>17</sup> The estimation employs monthly data for the US from January 1976 to June 2005 and considers two lags. Both models are estimated recursively over an expanding data window, starting with the first 10 years of data, providing approximately 220 out-of-sample forecasts from 1986 onward. 





Figure 7: One year ahead forecast error of industrial production. The blue line represents the forecast errors of the specification that considers the median (50<sup>_th_</sup> quantile) of the real economic factor, while the red line represents the forecast errors of the specification that considers the left tail (10<sup>_th_</sup> quantile) of the real economic factor. Grey vertical areas display the NBER economic recessions. 

From these projections, I compute the one-year-ahead forecast errors and present them in Figure 7, alongside the NBER classification of economic recessions (grey shaded areas), facilitating a visual representation of the forecast error dynamics around financial crises. In line 

> 17Refer to Section B of the Appendix for details on the data sources. Please note that the levels of industrial production are considered (i.e. transformation code = 1). 

ECB Working Paper Series No 2983 

26 

with Hamilton (2018)’s findings for US employment, the median specification results in negative forecast errors one year ahead of financial crises, whereas the 10<sup>_th_</sup> quantile specification yields positive or near-zero forecast errors. This evidence supports the assertion that the median real economic activity factor serves as a reliable proxy for the business cycle, while the 10<sup>_th_</sup> quantile effectively captures recessions by driving forecast errors to zero and beyond. 

ECB Working Paper Series No 2983 

27 

## **Data Descriptions** 

### **B Main Data Set** 

The main dataset adheres to the format outlined in Stock and Watson (2002) concerning the series number, series mnemonic, data span, and transformation. Transformation codes utilized are as follows: 1 – no transformation; 2 – first difference; 4 – logarithm; 5 – first difference of logarithm. Second differencing of logarithms was not utilized. These series were directly obtained from the DRI/McGraw Hill Basic Economics Database. An asterisk (*) next to the mnemonic indicates a variable presumed to exhibit slow movement in estimation. Variables included in the real economic activity subsample are highlighted in **bold** . All variables cover the sample span of 1976 : 01 _−_ 2005 : 06. 

ECB Working Paper Series No 2983 

28 

#### Table 2: Main Data Set 

OUT ————– Real Output and Income 

|1|**IPS11***|5|Industrial Production Index - Products, Total|
|---|---|---|---|
|2|**IPS299***|5|Industrial Production Index - Final Products|
|3|**IPS12***|5|Industrial Production Index - Consumer Goods|
|4|**IPS13***|5|Industrial Production Index - Durable Consumer Goods|
|5|**IPS18***|5|Industrial Production Index - Nondurable Consumer Goods|
|6|**IPS25***|5|Industrial Production Index - Business Equipment|
|7|**IPS32***|5|Industrial Production Index - Materials|
|8|**IPS34***|5|Industrial Production Index - Durable Goods Materials|
|9|**IPS38***|5|Industrial Production Index - Nondurable Goods Materials|
|10|**IPS43***|5|Industrial Production Index - Manufacturing (SIC)|
|11|**IPS67e***|5|Industrial Production Index - Mining NAICS = 21|
|12|**IPS68e***|5|Industrial Production Index - Electric and Gas Utilities|
|13|**IPS10***|5|Industrial Production Index - Total Index|
|14|**PMI***|5|Purchasing Managers’ Index (SA)|
|15|**PMP***|5|NAPM Production Index (Percent)|
|16|**PYQ***|5|Personal Income (Chained) (Bil 2000$, SAAR)|
|17|**MYXPQ***|5|Personal Income Less Transfer Payments (Chained) (Bil 2000$,SAAR)|
|18|**IPS307***|5|Industrial Production Index - Residential Utilities|
|19|**IPS316***|5|Industrial Production Index - Basic Metals|
|E|MP ————– Em|plo|yment and Hours|
|20|LHEL*|5|Index of Help-Wanted Advertising In Newspapers (1967 = 100;_SA_)|
|21|LHELX*|4|Employment: Ratio; Help-Wanted Ads: No. Unemployed Clf|
|22|LHEM*|5|Civilian Labor Force: Employed, Total (Thous., SA)|
|23|LHNAG*|5|Civilian Labor Force: Employed, Nonagric. Industries (Thous., SA)|
|24|LHUR*|1|Unemployment Rate: All Workers, 16 Years & Over (%, SA)|
|25|LHU680*|1|Unemploy. by Duration: Average(Mean) Duration in Weeks (SA)|
|26|LHU5*|1|Unemploy. by Duration: Persons Unempl.Less Than 5 Wks (Thous., SA)|
|27|LHU14*|1|Unemploy. by Duration: Persons Unempl. 5 To 14 Wks (Thous., SA)|
|28|LHU15*|1|Unemploy. by Duration: Persons Unempl. 15 Wks + (Thous., SA)|
|29|LHU26*|1|Unemploy. by Duration: Persons Unempl. 15 To 26 Wks (Thous., SA)|
|30|BLS<br>LPNAG*|5|Total Nonfarm Employment (SA) - CES0000000001|
|31|BLS<br>~~L~~P*|5|Total Private Employment (SA) - CES0500000001|
|32|BLS<br>LPGD*|5|Goods-Producing Employment (SA) - CES0600000001|
|33|BLS<br>LPMI*|5|Natural Resources and Mining Employment (SA) - CES1000000001|
|34|BLS<br>LPCC*|5|Construction Employment (SA) - CES2000000001|



ECB Working Paper Series No 2983 

29 

- 35 BLS ~~L~~ PEM* 5 Manufacturing Employment (SA) - CES3000000001 36 BLS ~~L~~ PED* 5 Durable Goods Manufacturing Employment (SA) - CES3100000001 37 BLS ~~L~~ PEN* 5 Nondurable Goods Manufacturing Employment (SA) - CES3200000001 38 BLS ~~S~~ er.-EMP* 5 Service-Providing Employment (SA) - CES0700000001 39 BLS ~~T~~ ra.EMP* 5 Trade, Transportation, and Utilities Employment (SA) - CES4000000001 40 BLS ~~R~~ et.- EMP* 5 Retail Trade Employment (SA) - CES4200000001 41 BLS ~~W~~ hol. EMP* 5 Wholesale Trade Employment (SA) - CES4142000001 42 BLS ~~F~~ in.-EMP* 5 Financial Activities Employment (SA) - CES5500000001 43 BLS ~~P~~ -Ser.EMP* 5 Private Service-Providing Employment (SA) - CES0800000001 44 BLS ~~L~~ PGOV* 5 Government Employment (SA) - CES9000000001 45 BLS ~~L~~ PHRM* 1 Manufacturing A wkly H Prod. Workers(SA) - CES3000000005 46 BLS ~~L~~ PMOSA* 1 Manufacturing A wkly Overtime Prod. Workers (SA) - CES3000000007 47 PMEMP NAPM Employment Index (Percent) HSS ———— Housing Starts and Sales 

- 48 **HSFR*** 4 Housing Starts (Thous. U., SA) 49 **HSNE*** 4 Housing Starts: Northeast (Thous. U., SA) 50 **HSMW*** 4 Housing Starts: Midwest (Thous. U., SA) 51 **HSSOU*** 4 Housing Starts: South (Thous. U., SA) 52 **HSWST*** 4 Housing Starts: West (Thous. U., SA) 53 **HSBR*** 4 Housing Authorized: Total New Private Housing Units (Thous., SAAR) 54 **HMOB*** 4 Mobile Homes: Manufacturers’ Shipments (Thous. U., SAAR) INV ————– Real Inventories and Inventory-Sales Ratios 

- 55 PMNV 1 NAPM Inventories Index (Percent) ORD————– Orders and Unfilled Orders 

- 56 PMNO 1 NAPM New Orders Index (Percent) 57 PMDEL 1 NAPM Vendor Deliveries Index (Percent) 58 MOCMQ 5 New Orders (Net) - Consumer Goods & Materials, 1996 Dollars (BCI) 59 MSONDQ 5 New Orders, Nondefense Capital Goods, In 1996 Dollars (BCI) 

ECB Working Paper Series No 2983 

30 

SPR ————– Stock Prices 

|60|FSPCOM|5|S&P’s Common Stock Price Index: Composite (1941-43=10)|
|---|---|---|---|
|61|FSPIN|5|S&P’s Common Stock Price Index: Industrials (1941-43=10)|
|62|FSDXP|1|S&P’s Composite Common Stock: Dividend Yield (% Per Annum)|
|63|FSPXE|1|S&P’s Composite Common Stock: Price-Earnings Ratio (%, NSA)|
|64|FSDJ||Common Stock Prices: Dow Jones Industrial Average|
|EX|R ————–|Exc|hange Rates|
|65|EXRSW|5|Foreign Exchange Rate: Switzerland (Swiss Franc Per U.S.$)|
|66|EXRJAN|5|Foreign Exchange Rate: Japan (Yen Per U.S.$)|
|67|EXRUK|5|Foreign Exchange Rate: United Kingdom (Cents Per Pound)|
|68|EXRCAN|5|Foreign Exchange Rate: Canada (Canadian $ Per U.S.$)|
|IN|T ————–|Inte|rest Rates|
|69|FYFF|1|Interest Rate: Federal Funds (Efective) (% Per Annum, NSA)|
|70|FYGM3|1|Interest Rate: U.S.Treasury Bills,Sec Mkt,3-Mo.(% Per Ann, NSA)|
|71|FYGM6|1|Interest Rate: U.S.Treasury Bills,Sec Mkt,6-Mo.(% Per Ann, NSA)|
|72|FYGT1|1|Interest Rate: U.S.Treasury Const Maturities, 1_−_Yr. (% Per Ann, NSA)|
|73|FYGT5|1|Interest Rate: U.S.Treasury Const Maturities, 5_−_Yr. (% Per Ann, NSA)|
|74|FYGT10|1|Interest Rate: U.S.Treasury Const Maturities, 10_−_Yr. (% Per Ann, NSA)|
|75|FYAAAC|1|Bond Yield: Moody’s AAA Corporate (% Per Annum)|
|76|FYBAAC|1|Bond Yield: Moody’s BAA Corporate (% Per Annum)|
|77|SFYGM3|1|Spread FYGM3 - FYFF|
|78|SFYGM6|1|Spread FYGM6 - FYFF|
|79|SFYGT1|1|Spread FYGT1 - FYFF|
|80|SFYGT5|1|Spread FYGT5 - FYFF|
|81|SFYGT10|1|Spread FYGT10 - FYFF|
|82|SFYAAAC|1|Spread FYAAAC - FYFF|
|83|SFYBAAC|1|Spread FYBAAC - FYFF|
|84|EBP|1|Excess Bond Premium (FRED Database)|



ECB Working Paper Series No 2983 

31 

|MO|N ————– Money|and Credit Quantity Aggregates|
|---|---|---|
|85|FM1<br>5|Money Stock: M1 (Bil$, SA)|
|86|FM2<br>5|Money Stock:M2 (Bil$, SA)|
|87|FM3<br>5|Money Stock: M3 (Bil$, SA)|
|88|FM2DQ<br>5|Money Supply - M2 In 1996 Dollars (BCI)|
|89|FMFBA<br>5|Monetary Base, Adj for Reserve Requirement Changes (Mil$, SA)|
|90|FMRRA<br>5|Depository Inst Reserves: Total,Adj For Reserve Req Chgs (Mil$, SA)|
|91|FMRNBA<br>5|Depository Inst Reserves: Nonborrowed,Adj Res Req Chgs (Mil$, SA)|
|92|FCLBMC<br>1|Wkly Rp Lg Com’l Banks: Net Change Com’l & Indus Loans (Bil$, SAAR)|
|93|CCINRV<br>5|Consumer Credit Outstanding - Nonrevolving(G19)|
|94|IMFCLNQ|Commercial & Industrial Loans Oustanding In 1996 Dollars|
|PRI|————– Price Ind|exes|
|95|PMCP<br>1|NAPM Commodity Prices Index (Percent)|
|96|PWFSA*<br>5|Producer Price Index: Finished Goods (82=100, S A)|
|97|PWFCSA*<br>5|Producer Price Index: Finished Consumer Goods (82=100, SA)|
|98|PWIMSA*<br>5|Producer Price Index: Intermed Mat.Supplies & Components (82=100, SA)|
|99|PWCMSA*<br>5|Producer Price Index: Crude Materials (82=100, SA)|
|100|PUNEW*<br>5|CPI-U: All Items (82-84=100, S A)|
|101|PU83*<br>5|CPI-U: Apparel & Upkeep (82-84=100, SA)|
|102|PU84*<br>5|CPI-U: Transportation (82-84=100, SA)|
|103|PU85*<br>5|CPI-U: Medical Care (82-84=100, SA)|
|104|PUC*<br>5|CPI-U: Commodities (82-84=100, SA)|
|105|PUCD*<br>5|CPI-U: Durables (82-84=100, SA)|
|106|PUXF*<br>5|CPI-U: All Items Less Food (82-84=100, SA)|
|107|PUXHS*<br>5|CPI-U: All Items Less Shelter (82-84=100, SA)|
|108|PUXM*<br>5|CPI-U: All Items Less Medical Care (82-84=100, SA)|
|109|PSCCOM<br>5|Spot Market Price Index: BLS & CRB: All Commodities (1967=100)|
|AH|E ————– Average|Hourly Earnings|
|110|BLS<br>~~L~~EHCC*<br>5|Construction Av H Earnings of Production Workers (SA) - CES2000000006|
|111|BLS<br>~~L~~EHM*<br>5|Manufacturing Av H Earnings of Production Workers (SA) - CES3000000006|
|OT|H ————– Miscella|neous|
|112|HHSNTN<br>1|U. of Michigan Index of Consumer Expectations (Bcd-83)|



ECB Working Paper Series No 2983 

32 

### **C Sectoral Data Set** 

This section contains the details of the granular dataset of Boivin et al. (2009). The format is equivalent to that for the main data set in terms of series number, series, data span, transformation code, and series description as they appear in the database. The transformation for all data was the first difference of logarithms, coded as 5. This dataset comprises 194 monthly price series on Personal Consumption Expenditures with no missing observations, and 194 monthly real consumption series on Personal Consumption Expenditures. The table4 describes the 194 price series. The corresponding 194 real consumption series were ordered and transformed in a similar fashion and are listed in table 3. All price and quantity series are treated as slow moving variables. 

#### **C.1 Personal Consumption Expenditures (price indexes and nominal expenditures)** 

Series were downloaded from the underlying tables of the Bureau of Economic Analysis. 

Table 3: Personal Consumption Expenditure Data Set 

|1|P1NDCG3*|5|New domestic autos|
|---|---|---|---|
|2|P1NFCG3*|5|New foreign autos|
|3|P1NETG3*|5|Net transactions in used autos|
|4|P1MARG3*|5|Net purchases of used autos: Used auto margin|
|5|P1REEG3*|5|Net purchases of used autos: Employee reimbursement|
|6|P1TRUG3*|5|Trucks, new and net used|
|7|P1REVG3*|5|Recreational vehicles|
|8|P1TATG3*|5|Tires and tubes|
|9|P1PAAG3*|5|Accessories and parts|
|10|P1FNRG3*|5|Furniture, including mattresses and bedsprings|
|11|P1MHAG3*|5|Major household appliances|
|12|P1SEAG3*|5|Small electric appliances|
|13|P1CHNG3*|5|China, glassware, tableware, and utensils|
|14|P1RADG3*|5|Video and audio goods, including musical instruments, and<br>computer goods|
|15|P1FLRG3*|5|Floor coverings|
|16|P1CLFG3*|5|Clocks, lamps, and furnishings|
|17|P1TEXG3*|5|Blinds, rods, and other|



ECB Working Paper Series No 2983 

33 

|18|P1WTRG3*|5|Writing equipment|
|---|---|---|---|
|19|P1HDWG3*|5|Tools, hardware, and supplies|
|20|P1LWNG3*|5|Outdoor equipment and supplies|
|21|P1OPTG3*|5|Ophthalmic products and orthopedic appliances|
|22|P1GUNG3*|5|Guns|
|23|P1SPTG3*|5|Sporting equipment|
|24|P1CAMG3*|5|Photographic equipment|
|25|P1BCYG3*|5|Bicycles|
|26|P1MCYG3*|5|Motorcycles|
|27|P1BOAG3*|5|Pleasure boats|
|28|P1AIRG3*|5|Pleasure aircraft|
|29|P1JRYG3*|5|Jewelry and watches|
|30|P1BKSG3*|5|Books and maps|
|31|P1GRAG3*|5|Cereals|
|32|P1BAKG3*|5|Bakery products|
|33|P1BEEG3*|5|Beef and veal|
|34|P1PORG3*|5|Pork|
|35|P1MEAG3*|5|Other meats|
|36|P1POUG3*|5|Poultry|
|37|P1FISG3*|5|Fish and seafood|
|38|P1GGSG3*|5|Eggs|
|39|P1MILG3*|5|Fresh milk and cream|
|40|P1DAIG3*|5|Processed dairy products|
|41|P1FRUG3*|5|Fresh fruits|
|42|P1VEGG3*|5|Fresh vegetables|
|43|P1PFVG3*|5|Processed fruits and vegetables|
|44|P1JNBG3*|5|Juices and nonalcoholic drinks|
|45|P1CTMG3*|5|Cofee, tea and beverage materials|
|46|P1FATG3*|5|Fats and oils|
|47|P1SWEG3*|5|Sugar and sweets|
|48|P1OFDG3*|5|Other foods|
|49|P1PEFG3*|5|Pet food|
|50|P1MLTG3*|5|Beer and ale, at home|
|51|P1WING3*|5|Wine and brandy, at home|
|52|P1LIQG3*|5|Distilled spirits, at home|



ECB Working Paper Series No 2983 

34 

|53|P1ESLG3*|5|Elementary and secondary school lunch|
|---|---|---|---|
|54|P1HSLG3*|5|Higher education school lunch|
|55|P1OPMG3*|5|Other purchased meals|
|56|P1APMG3*|5|Alcohol in purchased meals|
|57|P1CFDG3*|5|Food supplied to employees: civilians|
|58|P1MFDG3*|5|Food supplied to employees: military|
|59|P1FFDG3*|5|Food produced and consumed on farms|
|60|P1SHUG3*|5|Shoes|
|61|P1WGCG3*|5|Clothing for females|
|62|P1WICG3*|5|Clothing for infants|
|63|P1WSGG3*|5|Sewing goods for females|
|64|P1WUGG3*|5|Luggage for females|
|65|P1MBCG3*|5|Clothing for males|
|66|P1MSGG3*|5|Sewing goods for males|
|67|P1MUGG3*|5|Luggage for males|
|68|P1MICG3*|5|Standard clothing issued to military personnel (n.d.)|
|69|P1GASG3*|5|Gasoline and other motor fuel|
|70|P1LUBG3*|5|Lubricants|
|71|P1OILG3*|5|Fuel oil|
|72|P1LPGG3*|5|Liquefed petroleum gas and other fuel|
|73|P1TOBG3*|5|Tobacco products|
|74|P1SOAG3*|5|Soap|
|75|P1CSMG3*|5|Cosmetics and perfumes|
|76|P1OPHG3*|5|Other personal hygiene goods|
|77|P1SDHG3*|5|Semidurable house furnishings|
|78|P1CLEG3*|5|Cleaning preparations|
|79|P1LIGG3*|5|Lighting supplies|
|80|P1PAPG3*|5|Paper products|
|81|P1RXDG3*|5|Prescription drugs|
|82|P1NRXG3*|5|Nonprescription drugs|
|83|P1MDSG3*|5|Medical supplies|
|84|P1GYNG3*|5|Gynecological goods|
|85|P1DOLG3*|5|Toys, dolls, and games|
|86|P1AMMG3*|5|Sport supplies, including ammunition|
|87|P1FLMG3*|5|Film and photo supplies|
|88|P1STSG3*|5|Stationery and school supplies|
|89|P1GREG3*|5|Greeting cards|
|90|P1ARTG3*|5|Expenditures abroad by U.S. residents:|
||||Government expenditures abroad|



ECB Working Paper Series No 2983 

35 

|91|P1ARSG3*|5|Expenditures abroad by U.S. residents:<br>Other private services|
|---|---|---|---|
|92|P1REMG3*|5|Less: Personal remittances in kind to nonresidents|
|93|P1MGZG3*|5|Magazines and sheet music|
|94|P1NWPG3*|5|Newspapers|
|95|P1FLOG3*|5|Flowers, seeds, and potted plants|
|96|P1OMHG3*|5|Owner occupied mobile homes|
|97|P1OSTG3*|5|Owner occupied stationary homes|
|98|P1TMHG3*|5|Tenant occupied mobile homes|
|99|P1TSPG3*|5|Tenant occupied stationary homes|
|100|P1TLDG3*|5|Tenant landlord durables|
|101|P1FARG3*|5|Rental value of farm dwellings|
|102|P1HOTG3*|5|Hotels and motels|
|103|P1HFRG3*|5|Clubs and fraternity housing|
|104|P1HHEG3*|5|Higher education housing|
|105|P1HESG3*|5|Elem and second education housing|
|106|P1TGRG3*|5|Tenant group room and board|
|107|P1TGLG3*|5|Tenant group employee lodging|
|108|P1ELCG3*|5|Electricity|
|109|P1NGSG3*|5|Gas|
|110|P1WSMG3*|5|Water and sewerage maintenance|
|111|P1REFG3*|5|Refuse collection|
|112|P1LOCG3*|5|Local and cellular telephone|
|113|P1INCG3*|5|Intrastate toll calls|
|114|P1ITCG3*|5|Interstate toll calls|
|115|P1DMCG3*|5|Domestic service, cash|
|116|P1DMIG3*|5|Domestic service, in kind|
|117|P1MSEG3*|5|Moving and storage|
|118|P1FIPG3*|5|Household insurance premiums|
|119|P1FIBG3*|5|Less: Household insurance benefts paid|
|120|P1RCLG3*|5|Rug and furniture cleaning|
|121|P1EREG3*|5|Electrical repair|
|122|P1FREG3*|5|Reupholstery and furniture repair|
|123|P1PSTG3*|5|Postage|
|124|P1MHOG3*|5|Household operation services, n.e.c.|
|125|P1ARPG3*|5|Motor vehicle repair|
|126|P1RLOG3*|5|Motor vehicle rental, leasing, and other|
|127|P1TOLG3*|5|Bridge, tunnel, ferry, and road tolls|



ECB Working Paper Series No 2983 

36 

- Insurance premiums for 

- 128 P1AING3* 5 user-operated transportation 

- 129 P1IMTG3* 5 Local transportation: Mass transit systems 130 P1TAXG3* 5 Taxicab 131 P1IRRG3* 5 Railway 132 P1IBUG3* 5 Bus 133 P1IAIG3* 5 Airline 134 P1TROG3* 5 Other 135 P1PHYG3* 5 Physicians 136 P1DENG3* 5 Dentists 137 P1OPSG3* 5 Other professional services 138 P1NPHG3* 5 Hospitals: Nonprofit 

ECB Working Paper Series No 2983 

37 

#### **C.2 Producer Price Indices** 

Series were downloaded from the website of BLS. 

Table 4: Producer Price Indices Data Set 

|1|311119*|5|Other animal food manufacturing|
|---|---|---|---|
|2|311119_p∗_|5|Other animal food manufacturing (primary products)|
|3|311211*|5|Flour Milling|
|4|311212*|5|Rice milling|
|5|311213*|5|Malt mfg|
|6|311223_a∗_|5|Other oilseed processing (cottonseed cake and meal<br>and other byproducts)|
|7|311223_p∗_|5|Fats and oils refning and blending (primary<br>products)|
|8|311311*|5|Sugarcane mills|
|9|311313*|5|Beet sugar manufacturing|
|10|311412*|5|Frozen specialty food manufacturing|
|11|311520*|5|Ice cream and frozen dessert mfg|
|12|311920*|5|Cofee and tea manufacturing|
|13|312140*|5|Distilleries|
|14|32211_−_*|5|Pulp mills|
|15|2213*|5|Paperboard mills|
|16|325620_p∗_|5|Toilet preparation mfg (primary products)|
|17|325920*|5|Explosives manufacturing|
|18|32731_−_*|5|Cement mfg|
|19|327320*|5|Ready mixed concrete mfg and dist|
|20|327410*|5|Lime|
|21|327420*|5|Gypsum building products manufacturing|
|22|327910*|5|Abrasive product manufacturing|
|23|331210*|5|Iron steel pipe & tube mfg from purch steel|
|24|333210*|5|Sawmill & woodworking machinery mfg|
|25|334310*|5|Audio & video equipment mfg|
|26|335110*|5|Electric lamp bulb & part mfg|
|27|336370*|5|Motor vehicle metal stamping|
|28|337910*|5|Mattress mfg|
|29|311421*|5|Fruit and vegetable canning|



ECB Working Paper Series No 2983 

38 

- 30 311423* 5 Dried and dehydrated food manufacturing 31 311513* 5 Cheese manufacturing 32 311611* 5 Animal except poultry slaughtering 33 311612* 5 Meat processed from carcasses 34 311613* 5 Rendering and meat byproduct processing 35 311711* 5 Seafood canning 36 311712* 5 Fresh & frozen seafood processing Frozen cakes pies & other pastries mfg (Primary 

- 37 311813 _p∗_ 5 products) Dry pasta manufacturing (macaroni spaghetti 

- 38 3118233* 5 vermicelli and noodles) 

- 39 312111 _p∗_ 5 Soft drinks manufacturing (primary products) 40 312221* 5 Cigarettes 41 3122291* 5 Other tobacco product mfg (cigars) 42 313111* 5 Yarn spinning mills Broadwoven fabric finishing mills (finished cotton 

- 43 3133111* 5 broadwoven fabrics not finished in weaving mills) 

- 44 315111* 5 Sheer hosiery mills 45 315191* 5 Outerwear knitting mills 46 315223* 5 Men’s boy’s cut & sew shirt excl work mfg 47 315224* 5 Men’s boy’s cut & sew trouser slack jean mfg 48 315993* 5 Men’s and boys’ neckwear mfg 49 316211* 5 Rubber and plastic footwear manufacturing 50 316213* 5 Men’s footwear excl athletic mfg 51 316214* 5 Women’s footwear excl athletic mfg 52 316992* 5 Women’s handbag & purse mfg 53 321212* 5 Softwood veneer or plywood mfg Reconstituted wood product mfg (particleboard 

- 54 3212191* 5 produced at this location) 

- 55 3219181* 5 Other millwork including flooring 56 321991* 5 Manufactured homes mobile homes mfg Paper except newsprint mills (clay coated printing 

- 57 3221211* 5 and converting paper) 

- 58 322214* 5 Fiber can tube drum & other products mfg 59 324121* 5 Asphalt paving mixture & block mfg 60 324122* 5 Asphalt shingle & coating materials mfg Petroleum lubricating oils and greases (primary 

- 61 324191 _p∗_ 5 products) 

- 62 325181* 5 Alkalies and chlorine 

ECB Working Paper Series No 2983 

39 

|63|3251881*|5|All other basic inorganic chemical manufacturing<br>(sulfuric acid gross new and fortifed)|
|---|---|---|---|
|64|3251921*|5|Cyclic crude and intermediate manufacturing (cyclic<br>coal tar intermediates)|
|65|325212*|5|Synthetic rubber manufacturing|
|66|325222*|5|Manufactured noncellulosic fbers|
|67|325314*|5|Fertilizer mixing only manufacturing|
|68|3254111*|5|Medicinal & botanical mfg (synthetic organic|
||||medicinal chemicals in bulk)|
|69|3261131*|5|Unsupported plastics flm sheet excluding packaging<br>manufacturin|
|70|326192*|5|Resilient foor covering manufacturing|
|71|326211*|5|Tire manufacturing except retreading|
|72|327111*|5|Vitreous plumbing fxtures access ftg mfg|
|73|327121*|5|Brick and structural clay tile|
|74|327122*|5|Ceramic wall and foor tile|
|75|327124*|5|Clay refractories|
|76|327125*|5|Nonclay refractory manufacturing|
|77|327211*|5|Flat glass manufacturing|
|78|327213*|5|Glass container manufacturing|
|79|327331*|5|Concrete block and brick manufacturing|
|80|3279931*|5|Mineral wool manufacturing|
|81|331111*|5|Iron and steel mills|
|82|331112*|5|Electrometallurgical ferroalloy product mfg|
|83|331221*|5|Rolled steel shape manufacturing|
|84|331312*|5|Primary aluminum production|
|85|331315*|5|Aluminum sheet plate & foil mfg|
|86|331316*|5|Aluminum extruded products|
|87|331421*|5|Copper rolling drawing & extruding|
|88|3314913*|5|Other nonferrous metal roll draw extruding|
|89|3314923*|5|Other nonferrous secondary smelt refne alloying<br>(secondary lead)|
|90|331511*|5|Iron foundries|
||*||Hand and edge tools except machine tools and|
|91|3322121|5|handsaws (mechanics’ hand service tools)|
|92|332213*|5|Saw blade & handsaw mfg|
|93|3323111*|5|Prefabricated metal building and component<br>manufacturing|
|94|332321*|5|Metal window and door manufacturing|



ECB Working Paper Series No 2983 

40 

|95|332431*|5|Metal can mfg|
|---|---|---|---|
|96|324393*|5|Other metal container manufacturing|
|97|332611*|5|Spring heavy gauge mfg|
|98|3326122*|5|Spring light gauge mfg (precision mechanical springs)|
|99|3327224*|5|Bolt nut screw rivet & washer mfg (externally<br>threaded metal fasteners except aircraft)|
|100|332913*|5|Plumbing fxture ftting & trim mfg|
|101|332991*|5|Ball and roller bearings|
|102|332992*|5|Small arms ammunition mfg|
|103|332996*|5|Fabricated pipe & pipe ftting mfg|
|104|332998*|5|Enameled iron & metal sanitary ware mfg|
|105|333111*|5|Farm machinery & equipment mfg|
|106|333131*|5|Mining machinery & equipment mfg|
|107|333132*|5|Oil and gas feld machinery and equipment mfg|
|108|333292*|5|Textile machinery|
|109|333293*|5|Printing machinery & equipment mfg|
|110|3332941*|5|Food products machinery mfg (dairy and milk<br>products plant machinery)|
|111|333992*|5|All other industrial machinery mfg (chemical<br>manufacturing machinery equip. and parts)|
|112|333997*|5|Automatic vending machine mfg|
|113|334411*|5|Machine tool metal cutting types mfg|
|114|334414*|5|Machine tool metal forming types mfg|
|115|334415*|5|Cutting tool & machine tool accessory mfg|
|116|334417*|5|Speed changer industrial high speed drive & gear mfg|
|117|3339233*|5|Other engine equipment mfg|
|118|3332981*|5|Pump & pumping equipment mfg (indus. pumps<br>except hydraulic fuid power pumps)|
|119|3333111*|5|Conveyor & conveying equipment mfg|
|120|333512*|5|Overhead crane hoist & monorail system mfg|
|121|333513*|5|Industrial truck tractor trailer stacker machinery mfg|
|122|3335151*|5|Welding & soldering equipment mfg (welding &<br>soldering equipment mfg)|
|123|333612*|5|Scale & balance except laboratory mfg|
|124|333618*|5|Electron tube mfg|
|125|3339111*|5|Electronic capacitor mfg|
|126|333922*|5|Electronic resistor mfg|
|127|3339233*|5|Electronic connector mfg|
|128|3345153*|5|Electricity measuring testing instrument mfg|



ECB Working Paper Series No 2983 

41 

|129|334517_p∗_|5|Irradiation apparatus manufacturing (primary<br>products)|
|---|---|---|---|
|130|3351211*|5|Residential electric lighting fxture mfg|
|131|335122*|5|Commercial electric lighting fxture mfg|
|132|335129*|5|Other lighting equipment mfg|
|133|335212*|5|Household vacuum cleaner mfg|
|134|335221*|5|Household cooking appliance mfg|
|135|335311*|5|Power distribution specialty transformer mfg|
|136|335312*|5|Motor & generator|
|137|33531p_∗_|5|Relay & industrial control mfg (primary products)|
|138|335911*|5|Storage battery mfg|
|139|3359291*|5|Other communication and energy wire|
|140|335932*|5|Non-current carrying wiring device mfg|
|141|335991_p∗_|5|Carbon & graphite product mfg (primary products)|
|142|336321_p∗_|5|Vehicular lighting equipment mfg (primary products)|
|143|337121*|5|Upholstered household furniture|
|144|337122*|5|Wood household furniture except upholstered|
|145|337124*|5|Metal household furniture|
|146|337211*|5|Wood ofce furniture|
|147|3372141*|5|Nonwood ofce furniture (ofce seating including<br>upholstered nonwood)|
|148|3399111*|5|Jewelry except costume mfg|
|149|3399123*|5|Silverware & hollowware mfg ( Flatware and carving<br>sets made wholly of metal)|
|150|339931*|5|Doll & stufed toy mfg|
|151|339932*|5|Game toy & children’s vehicle mfg|
|152|339944*|5|Carbon paper & inked ribbon|
|153|3399931*|5|Fastener button needle & pin|
|154|3399945*|5|Broom brush & mop mfg (other brushes)|



ECB Working Paper Series No 2983 

42 

###### **Acknowledgements** 

I am grateful to Haroon Mumtaz for valuable advice and guidance. Also, I would like to thank Yves Schüler for his generosity in making his codes available as well as the Editorial Board of the ECB Working Paper Series, the anonymous reviewer, Christian Brownlees, Ivan Petrella, Morten O. Ravn, Silvana Tenreyro and conference participants at the 11th RCEA Money Macro Finance Conference for helpful suggestions and comments. 

The views expressed in this paper are those of the author only and not necessarily reflect those of the European Central Bank or the European System of Central Banks (ESCB). 

###### **Sofia Velasco** 

European Central Bank, Frankfurt am Main, Germany; Queen Mary University of London, London, United Kingdom; email: sofia.velasco@bde.es 

###### **© European Central Bank, 2026** 

Postal address 60640 Frankfurt am Main, Germany Telephone +49 69 1344 0 Website www.ecb.europa.eu 

All rights reserved. Any reproduction, publication and reprint in the form of a different publication, whether printed or produced electronically, in whole or in part, is permitted only with the explicit written authorisation of the ECB or the authors. 

This paper can be downloaded without charge from www.ecb.europa.eu, from the Social Science Research Network electronic library or from RePEc: Research Papers in Economics. Information on all of the papers published in the ECB Working Paper Series can be found on the ECB’s website. 

PDF ISBN 978-92-899-6833-1 ISSN 1725-2806 doi:10.2866/839279 QB-AR-24-100-EN-N 

