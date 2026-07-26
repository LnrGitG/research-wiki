---
title: **Acknowledgements**
type: paper
source_pdf: raw/papers/Bańbura_Conditional Forecasts and Scenario analysis with VAR for Large Cross-Sections_2014.pdf
converted: 2026-07-26
---









**WORKING PAPER SERIES NO 1733 / SEPTEMBER 2014** 

**CONDITIONAL FORECASTS AND SCENARIO ANALYSIS WITH VECTOR AUTOREGRESSIONS FOR LARGE CROSS-SECTIONS** 

Marta Bańbura, Domenico Giannone and Michele Lenza 





In 2014 all ECB publications feature a motif taken from the €20 banknote. 



**NOTE:** This Working Paper should not be reported as representing the views of the European Central Bank (ECB). The views expressed are those of the authors and do not necessarily refl ect those of the ECB. 

##### **Acknowledgements** 

We would like to thank Todd Clark, Marek Jarociński and Lutz Kilian for their comments. Domenico Giannone was supported by the Action de recherche concertée contract ARC-AUWB/2010-15/ULB-11 and by the IAP research network grant nr. P7/06 of the Belgian government (Belgian Science Policy). 

##### **Marta Bańbura** 

European Central Bank; e-mail: marta.banbura@ecb.europa.eu 

##### **Domenico Giannone** 

LUISS, ULB-ECARES and CEPR; e-mail: dgiannon@ulb.ac.be 

##### **Michele Lenza** 

European Central Bank and ULB-ECARES; e-mail: michele.lenza@ecb.europa.eu 

##### **© European Central Bank, 2014** 

**Address** Kaiserstrasse 29, 60311 Frankfurt am Main, Germany **Postal address** Postfach 16 03 19, 60066 Frankfurt am Main, Germany **Telephone** +49 69 1344 0 **Internet** http://www.ecb.europa.eu 

All rights reserved. Any reproduction, publication and reprint in the form of a different publication, whether printed or produced electronically, in whole or in part, is permitted only with the explicit written authorisation of the ECB or the authors. This paper can be downloaded without charge from http://www.ecb.europa.eu or from the Social Science Research Network electronic library at http://ssrn.com/abstract_id=2491561. Information on all of the papers published in the ECB Working Paper Series can be found on the ECB’s website, http://www.ecb.europa.eu/pub/scientifi c/wps/date/html/index.en.html 

**ISSN** 1725-2806 (online) **ISBN** 978-92-899-1141-2 **EU Catalogue No** QB-AR-14-107-EN-N (online) 

#### **Abstract** 

This paper describes an algorithm to compute the distribution of conditional forecasts, i.e. projections of a set of variables of interest on future paths of some other variables, in dynamic systems. The algorithm is based on Kalman filtering methods and is computationally viable for large models that can be cast in a linear state space representation. We build large vector autoregressions (VARs) and a large dynamic factor model (DFM) for a quarterly data set of 26 euro area macroeconomic and financial indicators. Both approaches deliver similar forecasts and scenario assessments. In addition, conditional forecasts shed light on the stability of the dynamic relationships in the euro area during the recent episodes of financial turmoil and indicate that only a small number of sources drive the bulk of the fluctuations in the euro area economy. 

#### **JEL Classification** : C11, C13, C33, C53 

**Keywords** : Vector Autoregression, Bayesian Shrinkage, Dynamic Factor Model, Conditional Forecast, Large Cross-Sections. 

ECB Working Paper 1733, September 2014 

1 

# **Non-technical summary** 

Vector autoregressions (VARs) are very flexible and general models and provide a reliable empirical benchmark for alternative econometric representations such as dynamic stochastic general equilibrium (DSGE) models, which are more grounded in theory but, at the same time, impose more structure on the data. 

Recent literature has shown that VARs are viable tools also for large sets of data. In this paper we construct a large VAR for the euro area and we apply it to unconditional forecasting as well as for conditional forecasts and scenarios. These, along with structural analysis (assessing the effects of structural shocks), have been the main applications of VARs. Whereas large VARs have been used for unconditional forecasting and structural analysis, limited attention has been devoted as yet to conditional forecasting. This is because popular algorithms for deriving conditional forecasts have been computationally challenging for large data sets. We overcome this problem by computing the conditional forecasts recursively using Kalman filtering techniques. 

Conditional forecasts and, in particular, scenarios are projections of a set of variables of interest on future paths of some other variables. This is in contrast to unconditional forecasts, where no knowledge of the future path of any variables is assumed. The prior knowledge, albeit imperfect, of the future evolution of some economic variables may carry information for the outlook of other variables. For example, future fiscal packages would affect the future evolution of economic activity and, thus, might provide important off-model information. Moreover, it may be of interest to assess the impact of specific future events on a set of variables, i.e. to conduct scenario analysis. Notable examples of the latter are the stress tests recently conducted in the US and the euro area in order to assess the vulnerability of their banking systems. 

For VAR models, the conditional forecasts are typically computed by using the algorithm developed by Waggoner and Zha (1999). Due to computational burden, the latter approach can easily become impractical or unfeasible for high dimensional data and long forecast horizons. However, many problems in macroeconomics and finance can only be addressed by looking at the joint dynamic behavior of a large number of time series. More in general, contemporary science relies more and more on the availability and exploitation of large data sets. 

In this paper, we propose an algorithm based on Kalman filtering techniques to compute the conditional forecasts. Since the Kalman filter works recursively, i.e. period by period, this algorithm reduces significantly the computational burden and is particularly well suited for empirical approaches handling large data sets. Using a simulation smoother allows for the computation of the full distribution of conditional forecasts. The algorithm applies to any model which can be cast in a linear state space representation. For the VAR framework, we compare the computational efficiency of different algorithms and find sizeable differences in computational performance of various approaches. Kalman filter based methods can offer substantial computational gains when the number of conditioning variables and the forecast horizon are large. 

The interest in issues which are best addressed by considering large information sets raises 

ECB Working Paper 1733, September 2014 

2 

a trade-off between excessive simplicity of the models – misspecification due to omitted vari– – ables and their excessive complexity many free parameters leading to large estimation uncertainty. Recent developments in macroeconometrics have suggested two approaches to deal with the complexity of large sets of data, without losing their salient features: Bayesian VARs (BVARs) and dynamic factor models (DFMs). Both model classes can be cast in a linear state space representation. 

A solution to the curse of dimensionality in the VAR framework consists in adopting Bayesian shrinkage. The idea of this method is to combine the likelihood coming from the complex and highly parameterised VAR model with a prior distribution for the parameters that is na¨ıve but enforces parsimony. As a consequence, the estimates are “shrunk” toward the prior expectations, which are typically equal to 0. This approach can also be interpreted as a penalised maximum likelihood method. 

Factor models exploit the fact that macroeconomic and financial time series are characterised by strong cross-sectional correlation. Under the assumption that most of the fluctuations are driven by a relatively limited set of common sources, factor models offer a parsimonious representation by summarizing the information from a large number of data series in few common factors. DFMs further parameterize the dynamics of the factors, typically assuming a VAR process. 

In our empirical application, we carry out a comprehensive comparison of the two modelling approaches, the VARs and the DFMs, on a large data set of quarterly euro area macroeconomic and financial variables. We consider two versions of the BVAR – with data in (log-)levels and – in (log-)differences and a dynamic factor model. First, we show that the three models produce quite accurate unconditional forecasts, compared to univariate benchmarks, and that the forecasts from the three approaches are very correlated. The latter lends empirical support to the theoretical argument that the approaches are tightly linked, complementing similar evidence already available for the US. 

Then, we compare the two approaches also for what concerns scenarios and conditional forecasts. In particular, we study the economic developments associated to a scenario of an increase in world GDP as well as conditional forecasts based on the realised path of real GDP, consumer prices and the policy rate. We show that also the scenario analysis and the conditional forecasts computed for the three models provide similar insights. The fact that the results are not model specific is reassuring, since it indicates that the predictions of the models are reflecting genuine data features. 

The results from the conditional forecasts yield support to two further conclusions. First, the fact that the conditional forecasts based on the three variables track, in general, quite closely the actual developments in most of the variables considered suggests that there are only a few “sources” that drive the bulk of the fluctuations in the euro area economy. Second, there appears to be some degree of stability in the economic relationships following the financial crisis as the the conditional forecasts for this period based on the parameters estimated with data until end of 2007 are relatively accurate, with the possible exception of some categories of loans and broad monetary aggregates. 

ECB Working Paper 1733, September 2014 

3 

# **1 Introduction** 

Vector autoregressions (VARs) are very flexible and general models and provide a reliable empirical benchmark for alternative econometric representations such as dynamic stochastic general equilibrium (DSGE) models, which are more grounded in theory but, at the same time, impose more structure on the data (see, for example, Christiano, Eichenbaum, and Evans, 1999). 

Recent literature has shown that VARs are viable tools also for large sets of data (see Ba´nbura, Giannone, and Reichlin, 2010). In this paper, we construct a large VAR for the euro area and we apply it to unconditional forecasting as well as for conditional forecasts and scenarios. These, along with structural analysis (assessing the effects of structural shocks), have been the main applications of VARs. Whereas large VARs have been used for unconditional forecasting and structural analysis,<sup>1</sup> limited attention has been devoted as yet to conditional forecasting. This is because popular algorithms for deriving conditional forecasts have been computationally challenging for large data sets. We overcome this problem by computing the conditional forecasts recursively using Kalman filtering techniques. 

Conditional forecasts and, in particular, scenarios are projections of a set of variables of interest on future paths of some other variables. This is in contrast to unconditional forecasts, where no knowledge of the future path of any variables is assumed. The prior knowledge, albeit imperfect, of the future evolution of some economic variables may carry information for the outlook of other variables. For example, future fiscal packages would affect the future evolution of economic activity and, thus, might provide important off-model information. Moreover, it may be of interest to assess the impact of specific future events on a set of variables, i.e. to conduct scenario analysis. Notable examples of the latter are the stress tests recently conducted in the US and the euro area in order to assess the vulnerability of their banking systems. For recent examples of conditional forecasts, see Lenza, Pill, and Reichlin (2010); Giannone, Lenza, and Reichlin (2010); Jaroci´nski and Smets (2008); Bloor and Matheson (2011); Giannone, Lenza, Pill, and Reichlin (2012); Stock and Watson (2012a); Giannone, Lenza, Momferatou, and Onorante (2014). Recently, Clark and McCracken (2014) propose 

> 1See e.g. Koop (2013), Giannone, Lenza, Momferatou, and Onorante (2014), Giannone, Lenza, and Reichlin (2012), Paciello (2011),Giannone, Lenza, and Primiceri (2014). 

ECB Working Paper 1733, September 2014 

4 

and evaluate a range of tests of predictive ability for conditional forecasts from estimated models. 

The scenario analysis described above and studied in this paper can be considered as “reduced form”, in the sense that the forecasts are conditional on observables and the identification of structural shocks is not required.<sup>2</sup> Notice that, if needed, the structural shocks that are “compatible” with the scenario can be retrieved from the reduced form innovations with some identifying assumptions. An alternative approach consists in constructing scenarios by manipulating specific structural shocks so that the resulting paths of the observed variables are consistent with the conditioning information (see also Leeper and Zha, 2003; Adolfson, Las´een, Lind´e, and Villani, 2005; Christoffel, Coenen, and Warne, 2007; Luciani, 2013). Along similar lines, Baumeister and Kilian (2013) construct scenarios for real price of oil from a VAR by conditioning on a sequence of appropriately derived structural shocks rather than on a prespecified path for observables. 

For VAR models, the conditional forecasts are typically computed by using the algorithm developed by Waggoner and Zha (1999). Roughly speaking, the methodology involves drawing (the entire) paths of reduced form shocks which are compatible with the conditioning path on the observables. Due to computational burden, this approach can easily become impractical or unfeasible for high dimensional data and long forecast horizons, even if the computationally more efficient version of Jaroci´nski (2010) is employed. However, many problems in macroeconomics and finance can only be addressed by looking at the joint dynamic behavior of a large number of time series. For example, business cycle research, as in the NBER tradition, typically involves the analysis of many macroeconomic variables. Professional forecasters and policymakers look at a variety of different indicators to predict key variables of interest and to make their decisions. Investors analyze the joint behavior of many asset returns in order to choose their optimal portfolios. More in general, contemporary science relies more and more on the availability and exploitation of large data sets. 

In this paper, building on an old insight by Clarida and Coyle (1984), we propose an algorithm based on Kalman filtering techniques to compute the conditional forecasts. Since the Kalman filter works recursively, i.e. period by period, this algorithm reduces significantly the 

2For a discussion on the invariance of conditional forecast distribution to alternative identification assumptions for structural shocks see Waggoner and Zha (1999). 

ECB Working Paper 1733, September 2014 

5 

computational burden for longer forecast horizons and is particularly well suited for empirical approaches handling large data sets. Using a simulation smoother (see Carter and Kohn, 1994; de Jong and Shephard, 1995; Durbin and Koopman, 2002, for examples of simulation smoothers) allows for the computation of the full distribution of conditional forecasts. The algorithm applies to any model which can be cast in a linear state space representation. For the VAR framework, we compare the computational efficiency of different simulation smoothers and find that for large systems the simulation smoother of Durbin and Koopman (2002) can offer substantial computational gains with respect to the more popular algorithm of Carter and Kohn (1994).<sup>3</sup> 

The interest in issues which are best addressed by considering large information sets raises a trade-off between excessive simplicity of the models – misspecification due to omitted vari– – ables and their excessive complexity many free parameters leading to large estimation uncertainty. Recent developments in macroeconometrics have suggested two approaches to deal with the complexity of large sets of data, without losing their salient features: Bayesian VARs (BVARs) and dynamic factor models (DFMs). 

The aforementioned flexibility of VARs comes at the cost of a high number of free parameters to be estimated. Specifically, for a generic VAR(p) model for a vector of _n_ variables _yt_ = ( _y_ 1 _,t, . . . , yn,t_ )<sup>_′_</sup> : 



where _WN_ (0 _,_ Σ) refers to a white noise process with mean 0 and covariance matrix Σ, we count: i) _pn_<sup>2</sup> parameters in autoregressive matrices, _A_ 1 _, . . . , Ap_ , that are of dimension _n × n_ each; ii) _n_ ( _n_ + 1) _/_ 2 free parameters in the _n × n_ covariance matrix of residuals Σ; iii) _n_ parameters in the constant term _c_ . The number of parameters proliferates as the number of variables in the model increases, making estimation unreliable or unfeasible. For example, when the number of variables in a VAR with 4 lags increases from 6, as in the original VAR model proposed by Sims (1980), to 20, 50 or 100, the total number of parameters to be estimated goes from 171 to, respectively, numbers in the order of 2, 10 and 50 thousands. 

> 3This result is also relevant for other applications in which the size of the state vector is larger than the size of the vector of observables, such as e.g. time-varying parameter VARs (e.g. Primiceri, 2005) or mixedfrequency VARs (e.g. Schorfheide and Song, 2013). Estimations of such models have typically relied on Carter and Kohn (1994) algorithm. 

ECB Working Paper 1733, September 2014 

6 

Such a high number of parameters cannot be well estimated by ordinary least squares, for example, since the typical macroeconomic sample involves a limited number of data points (in the best case, 50 _−_ 60 years of data, i.e. 200 _−_ 250 data points with quarterly data). The problem of parameter proliferation that prevents econometricians from conducting reliable inference with large dimensional systems is also known as the “curse of dimensionality”. 

A solution to the curse of dimensionality in the VAR framework consists in adopting Bayesian shrinkage. The idea of this method is to combine the likelihood coming from the complex and highly parameterised VAR model with a prior distribution for the parameters that is na¨ıve but enforces parsimony. As a consequence, the estimates of the coefficients are “shrunk” toward the prior expectations, which are typically equal to 0.<sup>4</sup> This approach can also be interpreted as a penalised maximum likelihood method. 

The shrinkage methods have been advocated by early proponents of VARs as a macroeconometric tool (Litterman, 1979; Sims, 1980; Doan, Litterman, and Sims, 1984) but they were typically used for low dimensional systems. Recently, it has been shown that the idea of shrinkage works also for high dimensional systems and provides results that are very similar to those obtained by using the DFMs (see De Mol, Giannone, and Reichlin, 2008; Ba´nbura, Giannone, and Reichlin, 2010; Giannone, Lenza, and Primiceri, 2014). This is not surprising since, as shown by De Mol, Giannone, and Reichlin (2008), when applied to collinear variables, as are typically macroeconomic variables, the forecasts produced by factor models and Bayesian shrinkage tend to get closer, as the size of the sample and of the cross-section get larger. 

Factor models exploit the fact that macroeconomic and financial time series are characterised by strong cross-sectional correlation. Under the assumption that most of the fluctuations are driven by a relatively limited set of common sources, factor models offer a parsimonious representation by summarizing the information from a large number of data series in few common factors. DFMs further parameterize the dynamics of the factors, typically assuming a VAR process. The estimation of factor models generally requires that the data are stationary. Assuming that stationarity is achieved via taking first differences<sup>5</sup> , the DFM is defined as 

> 4For an extensive discussion of shrinkage in various contexts see e.g. Stock and Watson (2012b) and Ng (2013). 

> 5Trending series are typically “logged” beforehand. 

ECB Working Paper 1733, September 2014 

7 

follows: 



where _Ft_ = ( _F_ 1 _,t, . . . , Fr,t_ )<sup>_′_</sup> is an _r_ -dimensional vector of common factors, with _r_ typically much smaller than _n_ and Λ is an _n×r_ matrix of factor loadings. Since the number of common factors _r_ is typically small, the estimation of the VAR describing the dynamics of the common factors does not pose any problem. The residual _et_ = ( _e_ 1 _,t, . . . , en,t_ )<sup>_′_</sup> is the idiosyncratic component. The most common approach is to assume that the idiosyncratic component is cross-sectionally uncorrelated. This assumption gives rise to the “exact” factor model, which highlights the fact that the cross-correlation between the variables is fully accounted for by the common factors. Interestingly, recent literature has shown that factor models can be estimated with large data sets, i.e. even in situations in which the cross-sectional dimension _n_ is much larger than the sample size _T_ . In addition, the estimates are asymptotically valid also when the data generating process is not the “exact” but rather an “approximate” factor model, in the sense that the idiosyncratic components are weakly cross-correlated (see Forni, Hallin, Lippi, and Reichlin, 2000; Stock and Watson, 2002b; Bai and Ng, 2002; Bai, 2003; Forni, Hallin, Lippi, and Reichlin, 2004; Doz, Giannone, and Reichlin, 2012). Stock and Watson (2011) provide an exhaustive survey of the literature. 

Factor models are appealing also because many popular economic models can be cast in their format. The typical theoretical macro model, indeed, includes only a handful of shocks driving the key aggregate variables in the economy. The arbitrage pricing theory (APT) is built upon the existence of a set of common factors underlying all returns. Moreover, the distinction between common and idiosyncratic sources of fluctuations is often employed in international, regional and sectorial studies and represents a useful device to study macroeconomic implications of microeconomic behavior (see e.g. Kose, Otrok, and Whiteman, 2003; Foerster, Sarte, and Watson, 2011). 

In our empirical application, we carry out a comprehensive comparison of the two modelling approaches, the VARs and the DFMs, on a large data set of quarterly euro area macroeconomic and financial variables. We consider two versions of the BVAR – with data in (log-)levels and – in (log-)differences and a dynamic factor model. First, we show that the three models 

ECB Working Paper 1733, September 2014 

8 

produce quite accurate unconditional forecasts, compared to univariate benchmarks, and that the forecasts from the three approaches are very correlated. The latter finding lends empirical support to the theoretical argument that the approaches are tightly linked, complementing similar evidence already available for the US (see, for example De Mol, Giannone, and Reichlin, 2008; Giannone, Lenza, and Primiceri, 2014). 

Then, we compare the two approaches also for what concerns scenarios and conditional forecasts. In particular, we study the economic developments associated to a scenario of an increase in world GDP as well as conditional forecasts based on the realised path of real GDP, consumer prices and the policy rate. We show that also the scenario analysis and the conditional forecasts computed for the three models provide similar insights. The fact that the results are not model specific is reassuring, since it indicates that the predictions of the models are reflecting genuine data features. 

The results from the conditional forecasts yield support to two further conclusions. First, the fact that the conditional forecasts based on the three variables track, in general, quite closely the actual developments in most of the variables under analysis suggests that there are only a few “sources” that drive the bulk of the fluctuations in the euro area economy. Second, there appears to be some degree of stability in the economic relationships following the financial crisis as the the conditional forecasts for this period based on the parameters estimated with data until end of 2007 are relatively accurate, with the possible exception of some categories of loans and broad monetary aggregates (see Giannone, Lenza, and Reichlin, 2012, for an extensive discussion and interpretation of these results). 

The structure of the paper is as follows. In section 2, we review the state-of-the-art techniques for the estimation and inference for DFMs and BVARs and we expound the close relationship linking the two approaches. In section 3, we describe a Kalman filter based methodology to compute conditional forecasts. In section 4, we present and discuss the empirical results. Section 5 concludes. The appendix contains some implementation details, comparison of computational performance of different algorithms and data descriptions. 

ECB Working Paper 1733, September 2014 

9 

# **2 Models for large data sets** 

## **2.1 Dynamic factor models** 

The general representation of the dynamic factor model described in the introduction is: 



Following Doz, Giannone, and Reichlin (2012) the model can be estimated by means of quasimaximum likelihood methods. In this context, the estimation of the model is performed by maximising a likelihood function, under the assumption that data are Gaussian and that the factor structure is exact, i.e. the idiosyncratic errors are cross-sectionally orthogonal: _ut ∼_ i _._ i _._ d _.N_ (0 _, Q_ ) and _et ∼_ i _._ i _._ d _.N_ (0 _,_ Γ _d_ ), where Γ _d_ is a diagonal matrix. 

Doz, Giannone, and Reichlin (2012) have shown that this estimation procedure provides consistent estimates for approximate dynamic factor models under general regularity conditions (convergence in probability of the covariance matrix of the data and data stationarity). Remarkably, consistency is achieved without any constraint on the number of variables, _n_ , relative to the sample size, _T_ , under the assumption of weak cross-sectional dependence of the idiosyncratic term, _et_ , and of sufficient pervasiveness of the common factors. 

As the factors are unobserved, the maximum likelihood estimators of the parameters Λ _,_ Γ _d_ , Φ1 _, . . . ,_ Φ _s, Q_ , which we collect in _θ_ , are, in general, not available in closed form. They can be obtained either via a direct numerical maximisation of the likelihood, which can be computationally demanding,<sup>6</sup> or, as in Doz, Giannone, and Reichlin (2012), via the ExpectationMaximisation (EM) algorithm. The EM algorithm was proposed by Dempster, Laird, and Rubin (1977) as a general solution to problems with incomplete or latent data. In the case of the DFM, the algorithm alternates between the use of the Kalman smoother to estimate the common factors given a set of parameters (E-step), and multivariate regressions (corrected for the uncertainty in the estimation of the common factors) to estimate the parameters given the factors (M-step), see e.g. Watson and Engle (1983) or Shumway and Stoffer (1982). 

> 6Jungbacker and Koopman (2008) show how to reduce the computational burden in case the number of observables is much larger than the number of factors. 

ECB Working Paper 1733, September 2014 

10 

The algorithm can be initialised using the sample principal components. In what follows, we assume that data are standardised to have sample mean equal to zero and variance equal to one.<sup>7</sup> Denote by _dj_ , _j_ = 1 _, . . . n_ , the eigenvalues of _T_<sup><u>1</u></sup> ∑ _Tt_ =1<sup>∆</sup><sup>_yt_∆</sup><sup>_y_</sup> _t_<sup>_′_andby</sup><sup>_vj_,</sup><sup>_j_= 1</sup><sup>_, . . . n_,the</sup> associated eigenvectors, i.e. 



with _vj_<sup>_′vj_=1,</sup><sup>_v_</sup> _j_<sup>_′vk_=0for</sup><sup>_j_=</sup><sup>_k_and</sup><sup>_d_1</sup><sup>_≥d_2</sup><sup>_≥. . .≥dn_.</sup> The sample principal <u>1</u> components of ∆ _yt_ are defined as _zjt_ = _~~√~~ dj_<sup>_v_</sup> _j_<sup>_′_∆</sup><sup>_yt_.Theprincipalcomponentsareordered</sup> accordingly to their ability to explain the variability in the data as the total variance explained by each principal component is equal to _dj_ . The principal components transform cross-sectionally correlated data, ∆ _yt_ , into linear combinations _zt_ = ( _z_ 1 _,t, . . . , zn,t_ )<sup>_′_</sup> = _H_ ∆ _yt ′_ <u>1 1</u> where _H_ = ( _~~√~~ d_ 1<sup>_v_1</sup><sup>_, . . . ,_</sup> _~~√~~ dn_<sup>_vn_</sup> ) . These linear combinations are cross-sectionally uncorrelated, with unit variance, _T_<sup><u>1</u></sup> ∑ _Tt_ =1<sup>_ztz_</sup> _t_<sup>_′_=</sup><sup>_In_.</sup> 

The approximate factor structure is defined in terms of behavior of the eigenvalues of the population covariance matrix when the number of variables increases. Specifically, the first _r_ eigenvalues of the population covariance matrix of ∆ _yt_ are assumed to grow with the dimension of the system, at a rate _n_ . All the remaining eigenvalues remain, instead, bounded. It can be proved that these assumptions imply that the eigenvalues _dj_ of the sample covariance matrix will go to infinity at a rate _n_ for _j_ = 1 _, . . . , r_ , where _r_ is the number of common factors. On the other hand, _dr_ +1 _, . . . , dn_ will grow at a rate given by _n/√T_ (see De Mol, Giannone, and Reichlin, 2008; Doz, Giannone, and Reichlin, 2011, 2012). Forni, Hallin, Lippi, and Reichlin (2000) and Stock and Watson (2002a,b) have shown that if data have an approximate factor structure<sup>8</sup> , then the first _r_ principal components can approximate well the space spanned by the unobserved common factors, when the sample size and the cross-sectional dimension are large. 

> 7 The zero mean assumption is without loss of generality, since it is equivalent to concentrating out the mean. Since maximum likelihood estimates are scale invariant, rescaling the data does not affect the estimates. On the other hand, homogeneity of the scale across variables is convenient, since the algorithm for maximizing the likelihood is more efficient from a computational standpoint. In addition, working with standardised data is useful since the initialisation of the algorithm is based on principal components, which are not scale invariant. Once the estimates are obtained, the factor loadings, Λ,<sup>ˆ</sup> and the covariance matrix of the idiosyncratic components, Γ<sup>ˆ</sup> _d_ , can be obtained by simple rescaling. 

> 8As stressed above, this amounts to assuming that the idiosyncratic components are weakly cross-correlated. 

ECB Working Paper 1733, September 2014 

11 

The sample principal components offer thus good starting values for the common factors: ˆ _Ft_<sup>(0)</sup> = _zt_ .<sup>9</sup> The starting values for the parameters of the model, _θ_<sup>(0)</sup> , can then be estimated by means of OLS techniques, by treating the principal components as if they were the true factors. Once the parameters have been estimated, we can estimate a new set of factors ˆ by using the Kalman smoother: _Ft_<sup>(1)</sup> = E _θ_ (0) [ _Ft|_ ∆ _y_ 1 _, . . . ,_ ∆ _yT_ ]. At this stage, we have the two-step procedure of Doz, Giannone, and Reichlin (2011). The quasi-maximum likelihood estimation via the EM algorithm consists essentially in iterating these steps until convergence. Details are reported in the appendix. 

## **2.2 Bayesian vector autoregressions** 

For Gaussian data, the VAR model described in the introduction is: 



We consider conjugate priors belonging to the normal-inverse-Wishart family, where the prior for the covariance matrix of the residuals is inverse-Wishart and the prior for the autoregressive coefficients is normal. The priors are a version of the so-called Minnesota prior, originally due to Litterman (1979), which is centered on the assumption that each variable follows an independent random walk process, possibly with drift: 



which is a parsimonious yet “reasonable approximation of the behavior of an economic variable”. 

For the prior on the covariance matrix of the errors, Σ, we set the degrees of freedom equal to _n_ + 2, which is the minimum value that guarantees the existence of the prior mean, which we set as E[Σ] = Ψ, where Ψ is diagonal. 

> 9In fact, under the assumption that Φ1 = _. . ._ = Φ _s_ = 0 and Γ _d_ = _γI_ ¯ _n_ (i.e. homoscedastic idiosyncratic components) the quasi-maximum likelihood solution is analytical, with the expected value for the factors proportional to the principal components of the data. 

ECB Working Paper 1733, September 2014 

12 

The prior moments for the VAR coefficients are as follows: 



Notice that the variance of this prior is lower for the coefficients associated with more distant lags, and that coefficients associated with the same variable and lag in different equations can be correlated. Finally, the key hyperparameter _λ_ controls the scale of all the variances and covariances, and effectively determines the overall tightness of this prior. The terms Σ _ij/_ Ψ _jj_ account for the relative scale of the variables. The prior for the intercept, _c_ , is diffuse.<sup>10</sup> 

We include an additional prior, which implements a so-called “inexact differencing” of the data. More precisely, rewrite the VAR equation in an error correction form: 



˜ where _p_ = _p −_ 1, _Bs_ = _−As_ +1 _− . . . − Ap, s_ = 1 _, . . . ,_ ˜ _p_ and Π = _A_ 1 + _. . ._ + _Ap − In_ . 

A VAR in first differences implies the restriction Π = 0 (or _A_ 1 + _. . ._ + _Ap_ = _In_ ). We follow Doan, Litterman, and Sims (1984) and set a prior that shrinks Π to zero. Precisely, we set a prior centered at 1 for the sum of coefficients on own lags for each variable, and at 0 for the sum of coefficients on other variables’ lags. This prior introduces correlation among the coefficients on each variable in each equation. The tightness of this prior on the “sum of coefficients” is controlled by the hyperparameter _µ_ . As _µ_ goes to infinity the prior becomes diffuse while, as it goes to 0, we approach the case of exact differencing, which implies the presence of a unit root in each equation. 

Following Sims (1993) and Sims and Zha (1998), we complement such “inexact differencing” with an additional prior, known as “dummy-initial-observation” prior, that shrinks the forecast 

> 10Koop (2013) considers non-conjugate priors which allow for exclusion of certain variables from some equations, however, he finds that these do not outperform simpler Minnesota priors in terms of forecast accuracy. Carriero, Clark, and Marcellino (2012) find that allowing for stochastic volatility helps to improve forecast accuracy. See Karlsson (2013) for a comprehensive overview of Bayesian methods for inference and forecasting with VAR models. 

ECB Working Paper 1733, September 2014 

13 

of each variable at the beginning of the sample toward a no-change forecast. The tightness of the prior is controlled by an additional hyperparameter _δ_ . 

The setting of the priors importantly depends on the hyperparameters _λ_ , _µ_ , _δ_ and Ψ, which reflect the informativeness of the prior distributions for the model coefficients. These hyperparameters have been usually set on the basis of subjective considerations or rules-of-thumb. Instead, we closely follow the theoretically grounded approach proposed by Giannone, Lenza, and Primiceri (2014). This involves treating the hyperparameters as additional parameters, in the spirit of hierarchical modelling. As hyperpriors (i.e. prior distributions for the hyperparameters), we use proper but quite disperse distributions. The implementation details are reported in the appendix. 

## **2.3 Bayesian vector autoregression and dynamic factor model** 

The connection between Bayesian shrinkage and dynamic factor models is better understood by focusing on the data that have been transformed to achieve stationarity, ∆ _yt_ , and that have been standardised to have mean zero and unit variance. 

The VAR in differences can be represented by: 



Imposing that the level of each variable _yt_ follows an independent random walk process, is equivalent to imposing that its difference, ∆ _yt_ , follows an independent white noise process. 

Consequently, the prior on the autoregressive coefficients can be characterised by the following and second moments: 



Since the variables are rescaled to have the same variance, the hyperparameter related to the scale can be set to be the same for all variables, i.e. Ψ = _ψI_<sup>¯</sup> _n_ . 

ECB Working Paper 1733, September 2014 

14 

The model can be rewritten in terms of the principal components described in section 2.1: 



where _zt_ = _H_ ∆ _yt_ are the ordered principal components. 

Interestingly, the prior set-up that imposes a uniform shrinkage on the parameters is equivalent to imposing a non-uniform degree of shrinkage on principal components: 



In fact, the prior variance for the coefficients on the _j_<sup>t</sup><sup>_h_</sup> principal component turns out to be proportional to the variance explained by the latter ( _dj_ ). 

As discussed in section 2.1, if the data are characterised by a factor structure then, as the number of variables and the sample size increase, _dj_ will go to infinity at a rate _n_ for _j_ = 1 _, . . . , r_ , where _r_ is the number of common factors. On the other hand, _dr_ +1 _, . . . , dn_ will grow at a slower rate which cannot be faster than _n/√T_ . As a consequence, if _λ_ goes to zero at a rate that is faster than that for the smaller eigenvalues and slower than for the largest eigenvalues, i.e. _λ_<sup>2</sup> = _κ_ _<u>√nT</u> T_ <u>1</u><sup>_δ_with0</sup><sup>_<δ<_1</sup><sup>_/_2and</sup><sup>_κ_anarbitraryconstant,then</sup><sup>_λ_2</sup><sup>_dj_will</sup> go to infinity for _j_ = 1 _, . . . , r_ . Hence the prior on the coefficients associated with the first _r_ principal components will become flat. Instead, for _j > r_ , _λ_<sup>2</sup> _dj_ will go to zero, i.e. the coefficients related to the principal components associated with the bounded eigenvalues will be shrunk to zero. 

De Mol, Giannone, and Reichlin (2008) have shown that, if the data are generated accordingly to a factor model and the hyperparameter _λ_ is set according to the rate described above, the point forecasts obtained by using shrinkage estimators converge to the unfeasible optimal forecasts that would be obtained if the common factors were observed. 

ECB Working Paper 1733, September 2014 

15 

# **3 Conditional forecasts for linear state space representations** 

## **3.1 Linear state space representation** 

Several univariate and multivariate time-series models may be cast in a linear state space representation. For the sake of notation, the generic linear state space representation is as<sup>11</sup> : 

_Measurement equation_ 



_Transition equation_ 



where _Zt_ = ( _Z_ 1 _,t, Z_ 2 _,t, . . . , Zk,t_ )<sup>_′_</sup> is a _k_ -dimensional vector of observables, _St_ an _m_ -dimensional vector of potentially unobserved states, _vt_ and _ut_ two vectors of errors with: _vt ∼_ i _._ d _._ N(0 _,_ Rt), _wt ∼_ i _._ d _._ N(0 _,_ Ht) and E [ _vtws_<sup>_′_] = 0</sup><sup>_∀t, s_.Finally,</sup><sup>_Ct_and</sup><sup>_Gt_aretwo,respectively,</sup><sup>_k × m_and</sup> _m × m_ matrices of potentially time-varying coefficients. 

The dynamic factor model in (2) can be cast in the representation (3)-(4) with _Zt_ := ∆ _yt_ , _Ct_ := (Λ _,_ 0 _n×r_ ( _s−_ 1) _, In_ ), _Rt_ := Γ _d_ and 



> 11See Harvey (1989) for a thorough treatment of state space techniques. To simplify notation we abstract from exogenous variables as they are not included in our empirical models. 

ECB Working Paper 1733, September 2014 

16 

For the VAR in (1), we have _Zt_ := _Yt_ , _Ct_ := ( _In,_ 0 _n×np_ ), _Rt_ := 0 _n_ and 



For the implementation in differences the modifications are straightforward. 

## **3.2 Conditional forecasts** 

Simulation smoothers (see Carter and Kohn, 1994; de Jong and Shephard, 1995; Durbin and Koopman, 2002, for example) can be used to generate a draw of the state vector _St , t_ = 1 _, . . . , T_ conditional on the observations _{Zt, t_ = 1 _, . . . , T }_ and on (a draw of) the parameters, _Ct_ , _Gt_ , _Rt_ , _Ht_ , _t_ = 1 _, . . . , T_ : 



Let us now assume that for a subset of variables, _I_ , we are interested in obtaining conditional forecasts for _t > t_ 0, conditional on their own past and on the past and future observations of the remaining variables, i.e. conditional on the information set Ω= _{Zl,t, l ∈I, t ≤ t_ 0 _, Zl,t, l̸ ∈ I, t_ = 1 _, . . . , T }_ : 



In order to obtain such conditional forecasts, we adopt the solution proposed for forecasting with ragged edge data sets using a Kalman filter methodology, see e.g. Giannone, Reichlin, and Small (2005). In fact, the variables for which we do not assume the knowledge of a future path can be considered as time series with missing data. The Kalman filter allows to easily deal with such time series. Going more in details, we follow a standard approach (see e.g. Durbin and Koopman, 2001, pp. 92-93) and apply the Kalman filter to a modified state space representation with _Zt_ , _Ct_ and _Rt_ replaced by _Z_<sup>¯</sup> _t_ , _C_<sup>¯</sup> _t_ and _R_<sup>¯</sup> _t_ respectively. The latter are 

ECB Working Paper 1733, September 2014 

17 

derived from the former by removing the rows (and, for _Rt_ , also columns) that correspond to the missing observations in _Zt_ .<sup>12</sup> 

This insight is already sufficient in order to compute point conditional forecasts, as the Kalman smoother gives the expectation of the distribution in (5), conditional on the parameters. In addition, assuming that the posterior distribution of the model parameters conditional on the data is available, the following algorithm (described for the generic iteration _j_ ) may be used in order to draw from the distribution of the conditional forecasts:<sup>13</sup> 

- (i) Draw the parameters _C_<sup>˜</sup> _t_<sup>(</sup><sup>_j_),</sup><sup>_G_˜(</sup> _t_<sup>_j_),</sup><sup>_R_˜</sup> _t_<sup>(</sup><sup>_j_)</sup> and _H_<sup>˜</sup> _t_<sup>(</sup><sup>_j_)</sup> from their posterior distribution.<sup>14</sup> 

- (ii) Draw the states _S_<sup>˜</sup> _t_<sup>(</sup> _|_<sup>_j_</sup> Ω<sup>)usingasimulationsmoother(CarterandKohn,1994;deJongand</sup> Shephard, 1995; Durbin and Koopman, 2002) for the modified (for the missing data) state space representation with the parameters _C_<sup>¯˜</sup> ( _tj_ )<sup>,</sup><sup>_G_˜(</sup> _t_<sup>_j_),</sup><sup>_R_¯˜</sup> _t_<sup>(</sup><sup>_j_)</sup> and _H_<sup>˜</sup> _t_<sup>(</sup><sup>_j_).</sup> 

- (iii) Draw the disturbances for the measurement equation, _v_ ˜ _i,t_<sup>(</sup><sup>_j_)</sup> _|_ Ω<sup>,fromaconditionalmulti-</sup> variate distribution _p_ ( _vi,t|v_ ˜ _l,t_<sup>(</sup><sup>_j_)</sup> _|_ Ω<sup>_, l̸ ∈I_)</sup><sup>_,i ∈I, t > t_0.15Infact,foraVAR</sup><sup>_v_˜</sup> _i,t_<sup>(</sup><sup>_j_)</sup> _|_ Ω<sup>_≡_0.</sup> 

- (iv) Compute _Z_<sup>˜</sup> _i,t_<sup>(</sup><sup>_j_)</sup> _|_ Ω<sup>= ( ˜</sup><sup>_C_</sup> _t_<sup>(</sup><sup>_j_))</sup><sup>_i·S_˜</sup> _t_<sup>(</sup> _|_<sup>_j_</sup> Ω<sup>)+ ˜</sup><sup>_v_</sup> _i,t_<sup>(</sup><sup>_j_)</sup> _|_ Ω<sup>_,i ∈I, t > t_0.</sup> 

The algorithm can be modified in a straightforward manner for any pattern of “missing” observations in _Zt_ . Note that we can also easily condition on a linear combination of the observations. Suppose, in fact, that the aim is to condition on _j_ linear combinations _WtZt_ 

> 12Giannone, Reichlin, and Small (2005) propose an equivalent solution. Instead of removing rows (and columns) of _Ct_ and _Rt_ that correspond to missing observations, they replace _Rt_ with _R_<sup>¯</sup> _t_ defined as follows: 



where, in practice, _∞_ is a large number. 

> 13We will denote a draw of a random variable from a distribution by˜. 

14In order to take the available future paths of selected variables into account when drawing the parameters, the initial values can be obtained from the “balanced” data set (up to _t_ 0) and then steps 1-4 can be iterated, with the latest conditional forecasts treated as data when drawing the parameters in step (i). 

> 15See e.g. Greene (2002) pp. 872 for conditional normal distributions. _v_ ˜ _l,t_<sup>(</sup><sup>_j_)</sup> _|_ Ω<sup>_, l∈I_canbeobtainedfrom</sup> 

_Zl,t −_ ( _C_<sup>˜</sup> _t_<sup>(</sup><sup>_j_)</sup> ) _l·S_<sup>˜</sup> _t_<sup>(</sup> _|_<sup>_j_</sup> Ω<sup>)or,alternatively,adisturbancesmoother(seedeJongandShephard,1995;Durbinand</sup> Koopman, 2002) can be used and the states can be derived indirectly from the disturbances. 

ECB Working Paper 1733, September 2014 

18 

where _Wt_ is a sequence of matrices of dimension _j × k_ . Then we set 



Note that for a large VAR model with several lags, the size of the state vector, _St_ , is much larger than the size of the vector of observables, _Zt_ . It turns out that in this case the simulation smoother of Durbin and Koopman (2002) along with the Kalman smoother implementation of de Jong (1988) offers large computational gains compared to the algorithm of Carter and Kohn (1994), see the appendix. This is the implementation we adopt in the empirical exercises.<sup>16</sup> 

## **3.3 Comparison with the approach of Waggoner and Zha (1999)** 

The algorithm of Waggoner and Zha (1999) is a popular method to obtain conditional forecasts for VAR models. Roughly speaking, the methodology involves drawing directly vectors of _εt_ , _t_ = _t_ 0 + 1 _, . . . , T_ , in (1) which satisfy the required conditions. 

For the VAR described above and the pattern of variable availability discussed in section 3.2: 



this would involve an inversion of a _q × q_ matrix, where _q_ = ( _n −_ #( _I_ ))( _T − t_ 0) denotes the number of restrictions, and, more importantly, a spectral decomposition of a _n_ ( _T −t_ 0) _×n_ ( _T − t_ 0) matrix (see e.g. Jaroci´nski, 2010, for a detailed discussion).<sup>17</sup> Jaroci´nski (2010) proposes a way to decrease the computational complexity which involves a singular value decomposition of a _q ×n_ ( _T −t_ 0) matrix and avoids the matrix inversion. However, the complexity still heavily depends on the number of restrictions, which can be prohibitively large in case of a large data set and a long forecast horizon. In contrast, the application of the Kalman filter makes the problem “recursive”, and the size of the largest matrix to be inverted is independent of the forecast horizon. 

The appendix provides an assessment of computational performance of different algorithms for obtaining conditional forecast distributions for VARs and indeed shows major computational 

> 16 To further improve the computational performance for the VARs we include the intercept, _c_ , as a constant in the transition equation (4) and remove it from the state vector, _St_ , see the appendix. 

> 17#( _I_ ) denotes the number of elements in _I_ . 

ECB Working Paper 1733, September 2014 

19 

gains of the Kalman filter based algorithm over the one of Waggoner and Zha (1999) and Jaroci´nski (2010) when the number of restrictions increases. 

## **3.4 Conditional forecasts and structural scenarios** 

The scenario analysis described above and considered in this paper is reduced form, in the sense that the scenarios are based on all the innovations that are compatible with the conditioning information. An alternative approach consists in constructing structural scenarios based only on certain structural shocks. This amounts to considering only some specific linear combination of the reduced form innovations. These scenarios can be implemented by modifying the covariance matrix of the innovations in the state space representation. 

Let us consider the case of the VAR first. Let us denote by _ηt_ = ( _η_ 1 _,t, . . . , ηn,t_ )<sup>_′_</sup> the structural shocks, assumed to be orthonormal, E( _ηtηt_<sup>_′_) =</sup><sup>_In_.We have that</sup><sup>_εt_= Γ</sup><sup>_ηt_=</sup><sup>_γ_1</sup><sup>_η_1</sup><sup>_,t_+</sup><sup>_· · ·_+</sup><sup>_γnηn,t_,</sup> where Γ contains the contemporaneous responses to the shocks and ΓΓ<sup>_′_</sup> = Σ. If one is interested in obtaining the scenario based only on the last _n − s_ shocks (i.e. _η_ 1 _,t, . . . , ηs,t_ are assumed to be 0), it is sufficient to replace Σ with Σ =<sup>¯</sup> _γs_ +1 _γs_<sup>_′_</sup> +1<sup>+</sup><sup>_. . ._+</sup><sup>_γnγ_</sup> _n_<sup>_′_.18</sup> 

In the case of the factor model, structural shocks, _ηt_ = ( _η_ 1 _,t, . . . , ηr,t_ )<sup>_′_</sup> , E( _ηtηt_<sup>_′_) =</sup><sup>_Ir_,arelinear</sup> combinations of the shocks to the factors. We have that _ut_ = Γ _ηt_ = _γ_ 1 _η_ 1 _,t_ + _· · ·_ + _γrηr,t_ , where Γ contains the contemporaneous responses to the shocks and ΓΓ<sup>_′_</sup> = _Q_ . If one is interested in obtaining the scenario based only on the last _r − s_ shocks, that it is sufficient to replace _Q_ with _Q_<sup>¯</sup> = _γs_ +1 _γs_<sup>_′_</sup> +1<sup>+</sup><sup>_. . ._+</sup><sup>_γrγ_</sup> _r_<sup>_′_.</sup> 

Another observation is that the conditional forecast framework can be used to obtain impulse response functions for VARs with recursive identification schemes. In this case Γ is lower triangular and the impulse response function to a shock _ηit_ can be obtained as: 

IRF<sup>i</sup> j<sup>= E (Yt+j</sup><sup>_|ϵ_1</sup><sup>_,_t= 0</sup><sup>_, . . . , ϵ_i</sup><sup>_−_1</sup><sup>_,_t= 0</sup><sup>_, ϵ_i</sup><sup>_,_t=</sup><sup>_γ_ii; Yt</sup><sup>_−_1</sup><sup>_, . . . ,_Yt</sup><sup>_−_p)</sup><sup>_−_E (Yt+j</sup><sup>_|_Yt</sup><sup>_−_1</sup><sup>_, . . . ,_Yt</sup><sup>_−_p)</sup><sup>_,_</sup> 



_j_ = 0 _, . . ._ . The second term on the right-hand side of equation (6) is the unconditional forecast. The conditions _ϵi,t_ = 0 ( _ϵi,t_ = _γii_ ) are implemented by setting _Yi,t_ equal to its unconditional 

> 18One has to further insure that the reduced form innovations implied by the scenario are not “incompatible” with the assumptions on Σ.<sup>¯</sup> For example, in a recursive identification scheme with Γ lower triangular, one cannot impose that _η_ 1 _,t_ = 0 and _ϵ_ 1 _,t_ = 0. 

ECB Working Paper 1733, September 2014 

20 

forecast (plus _γii_ ).<sup>19</sup> For _i_ = 1, this is akin to estimating a generalised impulse response function (on this point, see Koop, Pesaran, and Potter, 1996; Pesaran and Shin, 1998). 

# **4 Empirical Results** 

## **4.1 Data** 

Our data set includes 26 quarterly variables. Roughly, we include the most relevant real and nominal euro area aggregates and a set of international macroeconomic variables that proxies for global macroeconomic conditions (GDP and expenditure components, consumer and producer prices, labour market data, surveys, effective exchange rate, world economic activity, commodity prices), financial variables (short and long-term interest rates, stock prices), credit (both to households and firms) and monetary aggregates (M1 and M3). 

The sample covers the period from 1995Q1 to 2012Q4. Most of the data come from the Area Wide Model data base (Fagan, Henry, and Mestre, 2005). The share price index is downloaded from Datastream and the US short-term interest rate from the IMF data base. Remaining variables can be downloaded from the ECB Statistical Data Warehouse. The data appendix at the end of the paper provides the details, including the data transformations applied prior to parameter estimation. For most of the variables that are not already expressed in rates we take the natural logarithm multiplied by 4. For the models specified in differences we further take first differences for all the variables. For the logged variables this corresponds to annualised one-period percentage changes (in decimal).<sup>20</sup> 

## **4.2 Model specifications** 

We include 3 common factors in the DFM, which are meant to roughly capture the information on real developments, prices and interest rates. Further, we include 4 lags in the VAR of the common factors. The model is estimated by maximum likelihood using the EM algorithm. We also include 4 lags in the BVAR in differences and in order to be consistent with the 

> 19On the connection between scenario analysis and impulse response functions to identified shocks see also Jardet, Monfort, and Pegoraro (2012). 

> 20This reflects the setting of the prior for Ψ, see the appendix. 

ECB Working Paper 1733, September 2014 

21 

dynamics captured in the two approaches specified on variables in differences, in the BVAR in levels we include 5 lags. In the BVAR approaches, we have to choose the tightness of the prior distributions. As suggested in Giannone, Lenza, and Primiceri (2014), we follow a hierarchical approach and we treat the hyperparameters governing such tightness as random variables with relatively diffuse prior distributions. 

## **4.3 Model validation: out-of-sample forecasting evaluation of unconditional forecasts** 

As a preliminary step, we gauge the accuracy of our empirical models in terms of out-ofsample unconditional forecasts. This preliminary step is particularly important because our models are specified on a large set of variables (26). This feature leads to a proliferation of parameters and, hence, potential instabilities due to estimation uncertainty might completely offset the gains obtained by limiting model misspecification due to variable omission. Assessing out-of-sample forecast accuracy, which reflects both estimation uncertainty and model misspecification, allows us to understand whether the benefits due to the generality of our models outweigh the costs. 

We focus on point forecasts. For the DFM the forecasts are easily obtained with the Kalman filter. For the BVARs we use the modes of the posterior distribution of the parameters and the forecasts are obtained using the chain rule. 

For each of the three models, we produce the forecasts recursively for three horizons (1, 2 and 4 quarters ahead). The evaluation period is 2004-2012. For each of the evaluation periods, _t_ = 2004 _Q_ 1 _, . . . ,_ 2012 _Q_ 4, and forecast horizons, _h_ = 1 _,_ 2 _,_ 4, the forecasts are produced using the data from 1995Q1 to _t − h_ . At each step, the parameters (including the mode of the posterior distribution of the hyperparameters) are re-estimated. 

For each variable, the target of our evaluation is defined as _m_<sup>_h_</sup> _i,t_ + _h_<sup>=</sup><sup><u>100</u></sup> _h_<sup>[</sup><sup>_yi,t_+</sup><sup>_h−yi,t_].For</sup> variables specified in logs, this is approximately the average annualised growth rate over the next _h_ quarters (in percent), while for variables not transformed in logs, this is the average annualised quarterly change over the next _h_ quarters . 

We compare our model with a simple benchmark model, namely a random walk with drift for 

ECB Working Paper 1733, September 2014 

22 

the (log-)levels of the variables. This model is a particularly challenging benchmark over the monetary union sample and, in addition, it has also the appeal of being the “prior model” for the BVAR approaches. Hence, in case the BVAR models out-perform the benchmark model, this would suggest that they are able to extract valuable information from the sample.<sup>21</sup> 

Table 1 reports the results of our analysis, for all models and variables. Results are cast in terms of ratios of the Mean Squared Forecast Errors (MSFE) of our three models with respect to the corresponding MSFE of the random walk benchmark model. Hence, values smaller than one indicate that our model outperforms the benchmark model. 

The outcomes of the evaluation show that, in general, the BVARs and the DFM are able to outperform the benchmark model, particularly for the short horizons. For the one- and two-quarter horizons, the models are more accurate than the random walk for most of the variables. Some failures to outperform the benchmark model are not particularly surprising, since it is well known that it is very hard to beat the random walk model for financial and commodity prices, in general. Also for consumer prices (HICP) and the GDP deflator there is a relatively ample documentation of the difficulties to beat the random walk due to the steady anchoring of inflation expectations in the monetary union sample.<sup>22</sup> 

As argued in section 2.3 and in De Mol, Giannone, and Reichlin (2008), there is a tight connection between the BVAR and the DFM approaches. Indeed, the out-of-sample performance of the three different approaches is quite similar. This reflects the fact that the forecasts from the three approaches are very correlated. Figure 1 (panels a-c) reports the bivariate correlation with the BVAR in levels of the DFM (black bar with stripes) and the BVAR in differences (red solid bar) for all the variables and forecast horizons. 

The figure reveals the strong collinearity of the forecasts across approaches, providing empirical support for their theoretical connection highlighted in section 2.3 and in De Mol, Giannone, and Reichlin (2008). 

> 21We also compared our models to a battery of univariate autoregressive models, another class of popular benchmark models, with very similar outcomes. 

> 22See, for example, Diron and Mojon (2005) and Giannone, Lenza, Momferatou, and Onorante (2014). 

ECB Working Paper 1733, September 2014 

23 

Table 1: Ratio of MSFE relative to random walk benchmark 

|Variables|BV|AR in le|vels|BVA|R in dife|rences|Dyna|mic Facto|r model|
|---|---|---|---|---|---|---|---|---|---|
||H=1|H=2|H=4|H=1|H=2|H=4|H=1|H=2|H=4|
|Global GDP|**0.61**|**0.67**|**0.76**|**0.65**|**0.69**|**0.69**|**0.60**|**0.62**|**0.63**|
|Real GDP|**0.59**|**0.78**|**1.00**|**0.53**|**0.73**|**0.88**|**0.56**|**0.71**|**0.84**|
|Real consumption|**0.39**|**0.21**|**0.27**|**0.41**|**0.28**|**0.36**|**0.55**|**0.41**|**0.64**|
|Government consumption|**0.54**|**0.43**|**0.31**|**0.59**|**0.44**|**0.37**|**0.85**|**0.85**|**0.91**|
|Real investment|**0.51**|**0.55**|**0.60**|**0.46**|**0.51**|**0.56**|**0.43**|**0.46**|**0.51**|
|Real exports|**0.71**|**0.98**|1.28|**0.66**|**0.91**|1.04|**0.72**|**0.99**|1.03|
|Real imports|**0.51**|**0.63**|**0.73**|**0.46**|**0.59**|**0.67**|**0.54**|**0.65**|**0.73**|
|Employment|**0.16**|**0.21**|**0.35**|**0.16**|**0.20**|**0.33**|**0.17**|**0.19**|**0.33**|
|Unemployment rate|**0.39**|**0.50**|**0.72**|**0.35**|**0.46**|**0.66**|**0.30**|**0.40**|**0.61**|
|Economic sentiment|**0.48**|**0.67**|**0.73**|**0.58**|**0.88**|**0.96**|**0.73**|**0.97**|1.17|
|Oil price|1.08|1.34|1.52|1.28|1.65|1.79|1.93|2.89|3.44|
|N.-o. comm. prices|1.08|1.33|1.40|1.16|1.48|1.61|1.23|1.55|1.63|
|HICP|1.00|1.42|2.54|**0.96**|1.28|1.79|1.55|2.28|3.25|
|PPI ex. const.|**0.72**|1.04|1.56|**0.69**|1.07|1.67|**0.97**|1.58|2.26|
|GDP defator|**0.79**|**0.98**|1.71|1.06|1.17|1.33|1.25|1.38|1.81|
|Imports defator|**0.75**|1.09|1.58|**0.74**|1.18|1.84|**0.91**|1.53|2.08|
|Nominal wages|1.17|1.39|2.24|1.02|**0.98**|1.18|**0.87**|**0.96**|1.44|
|US short-term i. r.|**0.90**|1.05|1.14|**0.80**|**0.88**|**0.82**|**0.87**|**0.88**|**0.81**|
|Short-term i. r.|**0.67**|**0.94**|1.46|**0.57**|**0.92**|1.64|**0.72**|1.18|1.75|
|Long-term i. r.|**0.90**|1.01|1.58|1.05|1.30|1.64|1.08|1.26|1.62|
|M1|**0.57**|**0.60**|**0.90**|**0.60**|**0.69**|1.23|**0.89**|1.22|1.74|
|M3|**0.46**|**0.47**|**0.66**|**0.53**|**0.54**|**0.65**|**0.54**|**0.49**|**0.55**|
|Loans to households|**0.09**|**0.11**|**0.18**|**0.12**|**0.18**|**0.30**|**0.25**|**0.31**|**0.50**|
|Loans to frms|**0.06**|**0.09**|**0.26**|**0.07**|**0.10**|**0.25**|**0.15**|**0.20**|**0.41**|
|Efective exchange rate|1.33|1.50|2.13|1.38|1.39|1.59|1.29|1.43|1.76|
|Stock prices|**0.83**|**0.93**|1.21|**0.88**|1.02|1.05|**0.90**|1.12|1.50|



Note: The table reports the ratio of Mean Squared Forecast Errors (MSFE) of the BVAR in levels, BVAR in differences and the DFM over the MSFE of the random walk with drift for the (log-)levels (the model that would prevail if we assumed a dogmatic prior). The ratios are reported for the horizons of one, two and four quarters ahead. Values smaller than one (in bold) indicate that the MSFE of a specific model is lower than the corresponding MSFE of the random walk model. 

ECB Working Paper 1733, September 2014 

24 

### Figure 1: Correlation of DFM and BVAR in differences forecasts with BVAR in levels forecasts (a) One quarter ahead 



<!-- Start of picture text -->
DFM Diff.�BVAR<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>�0.2<br>(b) Two quarters ahead<br>DFM Diff.�BVAR<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>�0.2<br>(c) Four quarters ahead<br>DFM Diff.�BVAR<br>1<br>0.8<br>0.6<br>0.4<br>0.2<br>0<br>�0.2<br>Global�GDP Real�GDP Real�consumption Government�consumption Real�investment Real�exports Real�imports Employment Unemployment�rate Economic�sentiment Oil�price N.�o.�comm.�prices HICP PPI�ex.�const. GDP�deflator Imports�deflator Nominal�wages US�short�term�i.�r. Short�term�i.�r. Long�term�i.�r. M1 M3 Loans�to�households Loans�to�firms Effective�exchange�rate Stock�prices<br>Global�GDP Real�GDP Real�consumption Government�consumption Real�investment Real�exports Real�imports Employment Unemployment�rate Economic�sentiment Oil�price N.�o.�comm.�prices HICP PPI�ex.�const. GDP�deflator Imports�deflator Nominal�wages US�short�term�i.�r. Short�term�i.�r. Long�term�i.�r. M1 M3 Loans�to�households Loans�to�firms Effective�exchange�rate Stock�prices<br>Global�GDP Real�GDP Real�consumption Government�consumption Real�investment Real�exports Real�imports Employment Unemployment�rate Economic�sentiment Oil�price N.�o.�comm.�prices HICP PPI�ex.�const. GDP�deflator Imports�deflator Nominal�wages US�short�term�i.�r. Short�term�i.�r. Long�term�i.�r. M1 M3 Loans�to�households Loans�to�firms Effective�exchange�rate Stock�prices<br><!-- End of picture text -->







Note: For each variable on the horizontal axis, we report the correlation between the forecasts from the DFM and BVAR in levels (bars with white stripes) and between the forecasts from the BVAR in differences and BVAR in levels (bars with red solid fill). 

ECB Working Paper 1733, September 2014 

25 

## **4.4 Scenario analysis: an increase in world GDP** 

In this exercise we perform a scenario analysis to assess the effects associated with positive developments in the global economy, represented by a 0.1 percentage point stronger growth (on impact) in global GDP. 

We compute the effects of the scenario by using our framework to produce conditional forecasts, as discussed in section 3.4. Precisely, we estimate our models on the whole sample and generate two forecasts: an unconditional forecast for _T_ + 1 _, . . . , T_ + _h_ given the sample 1 _,_ 2 _, . . . , T_ (which provides a “baseline” scenario) and a conditional forecast in which the world GDP growth in _T_ + 1 is set to the value of its own unconditional forecast plus 0.1 percentage points and all the remaining variables are left unconstrained (which we will refer to as the “shocked scenario”). The scenario results for all variables are computed by taking the difference between the conditional and the unconditional forecasts described above. This is equivalent to computing a generalised impulse response function to an increase in world GDP, see section 3.4. We explore the horizon of eight quarters. 

Figure 2 shows the responses of some selected variables for the three models.<sup>23</sup> In particular, we report the distribution of the scenario effects computed in the context of the BVAR model in levels (shades of orange) and the point estimates of the effects in the other two modelling approaches (DFM: dashed blue line; BVAR in differences: black solid line). For the BVARs we use the algorithm described in section 3.2 and the point estimates of the effects for the BVAR in differences are defined as the medians of the distribution.<sup>24</sup> For the DFM we simply use the Kalman smoother to obtain the (conditional) forecasts given the maximum likelihood estimates of the parameters. All results are reported in terms of deviations of (log-)levels of the variables in the shocked scenario compared to the baseline.<sup>25</sup> 

The three approaches provide similar scenario assessments for all variables, at least qualitatively but, generally, also quantitatively. This result confirms the view that, for the variables commonly used in macroeconometric studies, dynamic factor models and Bayesian shrinkage 

> 23The total set of responses is available upon request. 

> 24We generate 25000 draws from the posterior distribution of the parameters and discard the first 5000. For each of the remaining draws we compute a point (conditional) forecast using the Kalman smoother. 

> 25For the variables that are modelled in logs, this approximately corresponds to percentage deviation from the baseline for the levels. 

ECB Working Paper 1733, September 2014 

26 

Figure 2: Scenario analysis: an increase in world GDP 



<!-- Start of picture text -->
Global GDP Real GDP Real exports Real imports<br>0.2 0.15 0.3 0.3<br>0.2<br>0.15 0.1 0.2<br>0.1<br>0.1 0.05 0.1<br>0<br>0.05 0 0<br>−0.1<br>0 −0.05 −0.1 −0.2<br>0 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8<br>Unemployment rate HICP Short−term i. r. Long−term i. r.<br>0.02 0.06 0.08 0.02<br>0.05 0.01<br>0.01<br>0.06<br>0.04 0<br>0<br>0.03 0.04 −0.01<br>−0.01<br>0.02 −0.02<br>0.02<br>−0.02<br>0.01 −0.03<br>−0.03 0 0 −0.04<br>0 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8<br>M1 M3 Loans to households Loans to firms<br>0.05 0.15 0.1 0.2<br>0 0.15<br>0.1 0.05<br>−0.05 0.1<br>0.05 0<br>−0.1 0.05<br>0 −0.05<br>−0.15 0<br>−0.2 −0.05 −0.1 −0.05<br>0 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8 0 1 2 3 4 5 6 7 8<br><!-- End of picture text -->

Note: Shades of orange: distribution of the scenario responses in the BVAR in levels, excluding the lower and higher 5% quantiles. Dashed blue line: point estimate of the scenario responses in the DFM model. Solid black line: point estimate of the scenario responses in the BVAR in differences, which is computed as the median of the distribution of the scenario responses in this model. The scenario responses are shown in terms of percentage deviation (of the levels of the variables) in the shocked scenario relative to the baseline scenario (except for the unemployment rate and the interest rates, for which we show deviations). 

ECB Working Paper 1733, September 2014 

27 

(irrespective of data transformation) are both valid alternative methods to deal with the curse of dimensionality. 

Going more in details of the scenario analysis, the top left panel reports the developments in global real GDP, which is 0.1 percent higher on impact (as assumed in the scenario assumption), keeps on increasing for the first year and then tends to drop back to the level prevailing before the initial increase. 

The euro area real economy (GDP, exports, imports and unemployment) closely mirrors the developments in global GDP. Consumer prices are also higher, reaching a peak after about one year. 

The short-term interest rate, which reflects systematic monetary policy, reacts positively to stabilize the economy and then drops back toward the initial level. According to the BVAR results, long-term interest rates are not particularly affected. This implies that the term-spread (defined as long-term interest rates minus short-term interest rates) decreases on impact, to finally revert to initial values. In this case, the DFM results are different from those of the BVARs. 

Credit aggregates, which are traditionally very cyclical, follow the same path as GDP. Moreover, loans to households are coincident with GDP, while loans to firms lag behind. The narrow monetary aggregate M1 decreases on impact, reaching a trough after about 1-1.5 year. To understand this pattern, notice that M1 is negatively related to the short-term interest rate, indicating that its response to world demand is mainly driven by the liquidity effect. The effect on M3 is instead mostly driven by the increases in the short-term monetary assets included in the M3-M1 component, which completely offset the decrease in M1 (see Giannone, Lenza, and Reichlin, 2012, for an extensive discussion on the cyclical properties of credit and monetary aggregates in the euro area and their relationships with short and long-term interest rates). 

An implicitly maintained assumption in this exercise is that the forecast paths we examine involve shocks small enough so as not to be subject to the Lucas critique.<sup>26</sup> Indeed, the reliability of the results rests on the fact that the perturbations we induce in the system 

> 26See, Kilian and Lewis (2011) and references therein for a discussion of this issue. 

ECB Working Paper 1733, September 2014 

28 

by means of the scenario assumptions are not as big as to induce a substantial shift in the behavior of economic agents which could, in turn, change the economic structure and, hence, the estimated reduced form parameters. 

## **4.5 Conditional forecasts** 

In this exercise we generate forecasts from the three models conditional on the realised paths for the following three variables: real GDP, HICP and the short-term interest rate. 

The conditional forecasts are generated over the period 1997-2012. The first two years in the sample are used as initial conditions. The parameters are estimated over the sample 1995-2007. Thus the conditional forecasts for 1997-2007 can be considered as “in-sample” while those over 2008-2012 as “out-of-sample”. The aim of this exercise (see Giannone, Lenza, and Reichlin, 2012; Stock and Watson, 2012a, for similar exercises) is twofold. First, the “in-sample” part (1997-2007) of the conditional forecasts can be compared with the observed developments in order to gauge whether knowing only the time series of real GDP, HICP and the short-term interest rate is sufficient in order to capture the salient features of the variables in our model. Second, by comparing the “out-of-sample” part (i.e. from 2008 onward) of the conditional forecasts with the observed developments, we can also assess whether the turmoil associated to the financial and the sovereign debt crises was reflected in a change in the structural economic relationships in the euro area. In fact, a change in the economic relationships would likely lead to relevant inaccuracies of the conditional forecasts based on parameters representing the pre-2007 economic relationships. 

Figure 3 shows the conditional forecasts from the three models for the same selected variables shown in Figure 2.<sup>27</sup> As in the previous exercise, the distribution is generated using the BVAR in levels, using the algorithm described in section 3.2.<sup>28</sup> Blue dashed and black solid lines correspond, respectively, to the conditional point forecasts of the DFM, obtained via the Kalman smoother, and the BVAR in differences, obtained as the median of the distribution. In addition, the green line indicates the actual outcomes. For the interest rates and the 

> 27Three additional variables replace the three variables shown in Figure 2 which in this exercise were used as conditions. A complete set of results is available upon request. 

> 28We generate 25000 draws from the posterior distribution of the parameters and discard the first 5000. For each of the remaining draws we compute a draw of the conditional forecast. 

ECB Working Paper 1733, September 2014 

29 

Figure 3: Conditional Forecasts 



<!-- Start of picture text -->
Global GDP Real investment Real exports Real imports<br>10 20 20 20<br>10 10<br>5 10<br>0 0<br>0 0<br>−10 −10<br>−5 −10<br>−20 −20<br>−10 −20 −30 −30<br>2000 2005 2010 2000 2005 2010 2000 2005 2010 2000 2005 2010<br>Unemployment rate PPI ex. const. Oil price Long−term i. r.<br>20 10 200 15<br>5 10<br>15 100<br>0 5<br>10 0<br>−5 0<br>5 −100<br>−10 −5<br>0 −15 −200 −10<br>2000 2005 2010 2000 2005 2010 2000 2005 2010 2000 2005 2010<br>M1 M3 Loans to households Loans to firms<br>20 20 15 15<br>15 10<br>10<br>10<br>10 5<br>5<br>5 0<br>0<br>0<br>0 −5<br>−10 −5 −5 −10<br>2000 2005 2010 2000 2005 2010 2000 2005 2010 2000 2005 2010<br><!-- End of picture text -->

Note: Shades of orange: distribution of the conditional forecasts in the BVAR in levels, excluding the lower and higher 5% quantiles. Dashed blue line: point estimate of the conditional forecasts in the DFM model. Solid black line: point estimate of the conditional forecasts in the BVAR in differences, which is computed as the median of the distribution of the conditional forecasts in this model. Green line with crosses: actual values. The variables are all reported in terms of annual percentage changes, except for the unemployment rate and the long-term interest rate, which are in levels. Compared to Figure 2, we report total investment, producer price index and the oil price in place of real GDP, HICP and the short-term interest rate, which are our conditioning assumptions. 

ECB Working Paper 1733, September 2014 

30 

unemployment rate we report the conditional forecasts for the levels. For the remaining variables the results are expressed in terms of annual rates of change. 

Analogously to the previous exercise, the forecasts from the three models are similar for most of the variables, indicating that different methodologies capture similar cross-sectional and dynamic information. In addition, the conditional forecasts are close to the actual outcomes, in particular in the “in-sample” period. This fact suggests that 3 “dimensions” are sufficient to capture the developments in most of the economy<sup>29</sup> (Giannone, Reichlin, and Sala, 2004, reach a similar conclusion for the US economy). 

Turning to the “out-of-sample” evidence, there is still a general similarity of the conditional forecasts across approaches. However, some differences appear between forecasts and observed developments for a few variables, indicating an instability in the relationships of these variables with the conditioning set. For example, notable differences appear in the developments in money and credit variables, whose actual developments were much more subdued than what would have been predicted based on the conditioning information.<sup>30</sup> For the variables where we have evidence of instability, we also notice some discrepancies in the forecasts across methods. 

# **5 Conclusions** 

We have modelled the dynamic interactions among a large set of macroeconomic and financial indicators in the euro area by means of large dynamic factor models and large Bayesian vector autoregressions. 

We find that both classes of models are reliable tools for analyzing large data sets, since they produce accurate unconditional forecasts and meaningful scenarios. 

Interestingly, the predictions of the two model classes are not only equally reliable, but are also very similar, in general. The fact that the results are not model specific is reassuring since it indicates that the predictions of the models are reflecting genuine data features. 

29 Notable exceptions are wages, GDP deflator, government consumption and the effective exchange rate (not shown). For these variables, the conditional forecast distributions cover a relatively wide range of values and the central forecasts are often quite far from the outcomes. 

30Giannone, Lenza, and Reichlin (2012) extensively discuss and interpret the anomalies in the developments in credit and money markets during the crisis. 

ECB Working Paper 1733, September 2014 

31 

The robustness and reliability of dynamic factor models and Bayesian vector autoregressions for analyzing large macroeconomic data sets has been already established for the United States in relation to forecasting and impulse response function analysis (see e.g. Ba´nbura, Giannone, and Reichlin, 2010; Giannone, Lenza, and Primiceri, 2014). We document that the same holds true for the euro area and for conditional forecasts. 

In addition, we have shown how to implement scenario analysis and, in general, to compute conditional forecasts in the context of large data sets. The procedure is computationally feasible, produces meaningful results and interesting insights. The methodology has been already used in a number of papers including Giannone, Lenza, Momferatou, and Onorante (2014), Giannone, Lenza, and Reichlin (2010, 2012), Giannone, Lenza, Pill, and Reichlin (2012), Lenza, Pill, and Reichlin (2010) and Luciani (2013). 

ECB Working Paper 1733, September 2014 

32 

# **A Simulation smoothers** 

## **A.1 Implementation** 

As mentioned above, for the VARs, we consider a version of the transition equation (4), in which the intercept is included as a constant: 



where _c_ ¯ _t_ = ( _c_<sup>_′_</sup> 01 _×n_ ( _p−_ 1))<sup>_′_</sup> whereas _St_ , _wt_ , _Gt_ and _Ht_ are obtained from the corresponding terms in equation (4) by removing the last _n_ rows (and columns). 

Given the parameter set _Ct_ , _Gt_ , _Rt_ , _Ht_ and _c_ ¯ _t_ , the algorithm of Carter and Kohn (1994) derives draws from the conditional distribution of the state vector, _S_<sup>˜</sup> _t|T , t_ = 1 _,_ 2 _, . . . , T_ , from the following recursions: 



with _S_<sup>˜</sup> _T |T_ = _ST |T_ + _ξ_<sup>˜</sup> _T , ξT ∼ N_ (0 _, PT |T_ ). _St|t_ = E [St _|_ Z1 _, . . . ,_ Zt] and _Pt|t_ = Var [St _|_ Z1 _, . . . ,_ Zt] are obtained from the Kalman filter (see below). In the case of a VAR, the algorithm involves a (pseudo) inversion of matrices of size _np × np_ as well as a singular value decomposition of matrices of the same size. 

The simulation smoother of Durbin and Koopman (2002) can be implemented via the following steps: 

- ˜ ˜ 

- (i) Draw the disturbances _vt_ and _wt_ , _t_ = 1 _,_ 2 _, . . . , T_ , from the unconditional distribution of _vt_ and _wt_ , i.e. _N_ (0 _, Rt_ ) and _N_ (0 _, Ht_ ), respectively. 

- (ii) Generate _Z_<sup>˜</sup> _t_ and _S_<sup>˜</sup> _t_ , _t_ = 1 _,_ 2 _, . . . , T_ , using the state space representation given by (3) and (7) and _v_ ˜ _t_ and _w_ ˜ _t_ from the previous step. 

- (iii) A draw from the conditional distribution of the state vector can be obtained as _S_<sup>˜</sup> _t|T_ = E St _|_ Z<sup>˜</sup><sup>_∗_</sup> 1<sup>_, . . . ,_˜Z</sup><sup>_∗_</sup> T + _S_<sup>˜</sup> _t_ , where _Z_<sup>˜</sup> _t_<sup>_∗_=</sup><sup>_Zt−Z_˜</sup><sup>_t_,</sup><sup>_t_= 1</sup><sup>_,_2</sup><sup>_, . . . , T_.</sup> [ ] 

ECB Working Paper 1733, September 2014 

33 

Let _St_<sup>_∗_</sup> _|s_<sup>=E</sup> [St _|_ Z<sup>˜</sup><sup>_∗_</sup> 1<sup>_, . . . ,_˜Z</sup><sup>_∗_</sup> s ] and _Pt_<sup>_∗_</sup> _|s_<sup>=Var</sup> [St _|_ Z<sup>˜</sup><sup>_∗_</sup> 1<sup>_, . . . ,_˜Z</sup><sup>_∗_</sup> s ]. We obtain _St_<sup>_∗_</sup> _|T_<sup>,</sup><sup>_t_=1</sup><sup>_,_2</sup><sup>_, . . . , T_,</sup> using the following implementation of the Kalman filter: 



and smoother: 



with _rT_ = 0. This approach involves the inversion of matrix _Ft_ , which has the (row and column) size of _n −_ #( _I_ ) _≤ n_ . It is anyway needed for the run of the Kalman filter and can be stored. By contrast, the implementation of the Kalman smoother as in e.g. Hamilton (1994) for a VAR requires the inversion of _np × np_ matrices _Pt_ +1 _|t_ . Thus, the approach of Durbin and Koopman (2002) can offer sizable computational gains for large _p_ . 

In the empirical exercises we run the simulation smoother only for the part of the sample with missing data, that is we truncate the data keeping only _Zt_ , _t > t_ 0 and we use _Zt_ 0 _, Zt_ 0 _−_ 1 _, . . ._ to derive the initial conditions, _S_ 0 (e.g. in case of the VAR in levels _S_ 0 = ( _Yt_<sup>_′_</sup> 0<sup>_. . .Y_</sup> _t_<sup>_′_</sup> 0 _−p_ +1<sup>)</sup><sup>_′_).</sup> Then we set _S_ 1 _|_ 0 = _G_ 0 _S_ 0 + ¯ _c_ 0 and _P_ 1 _|_ 0 = _H_ 0. For the simulation smoother of Durbin and Koopman (2002) we set _S_ 0<sup>_∗_= 0and</sup><sup>_c_¯</sup><sup>_t_= 0</sup><sup>_np×_1.</sup> 

## **A.2 Computational time** 

Table A compares the average computational time of a draw of conditional forecast for the 26 variable VAR considered in section 4 for the following algorithms: the simulation smoother of Carter and Kohn (1994) ( _CK_ ); the simulation smoother of Durbin and Koopman (2002) with a “traditional” Kalman smoother implementation (see e.g. Hamilton, 1994, pp. 394-396) ( _DK,H_ ); the simulation smoother of Durbin and Koopman (2002) with the Kalman smoother implementation of de Jong (1988) ( _DK,dJ_ ); the algorithm of Waggoner and Zha (1999) with the implementation of Jaroci´nski (2010) ( _WZ,J_ )<sup>31</sup> . We consider the cases of different number of 

> 31We would like to thank Marek Jaroci´nski for sharing his Matlab code for this procedure. 

ECB Working Paper 1733, September 2014 

34 

lags ( _p_ = 2, _p_ = 3 or _p_ = 5), different number of variables in the conditioning set ( _n−_ #( _I_ ) = 5, _n −_ #( _I_ ) = 15 or _n −_ #( _I_ ) = 25) and different number of conditioning periods ( _T − t_ 0 = 5, _T − t_ 0 = 20 or _T − t_ 0 = 60). In each case the time for the fastest algorithm is marked in boldface, whereas the time for the slowest is put in italics. Average time in seconds over 1000 repetitions is reported.<sup>32</sup> 

Table A: Average time of a draw of conditional forecast 

||CK|DK,H|DK,dJ|WZ,J|CK|DK,H|DK,dJ|WZ,J|CK|DK,H|DK,dJ|WZ,J|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||_n −_#|(_I_) = 5|||_n −_#<br>_p_|(_I_) = 15<br>= 2|||_n −_#|(_I_) = 25||
|_T −t_0 = 5|_0.04_|0.02|**0.01**|0.01|_0.04_|0.02|**0.01**|0.02|0.03|0.02|0.01|_0.05_|
|_T −t_0 = 20|_0.16_|0.09|**0.04**|0.13|0.16|0.09|**0.04**|_0.51_|0.13|0.08|**0.03**|_1.51_|
|_T −t_0 = 60|0.42|0.28|**0.06**|_2.20_|0.38|0.26|**0.07**|_10.61_|0.40|0.26|**0.08**|_39.25_|
|||||||_p_|= 3||||||
|_T −t_0 = 5|_0.08_|0.05|0.01|**0.01**|_0.08_|0.05|**0.01**|0.02|_0.08_|0.05|**0.01**|0.05|
|_T −t_0 = 20|_0.34_|0.23|**0.04**|0.15|0.32|0.20|**0.04**|_0.52_|0.35|0.20|**0.05**|_1.59_|
|_T −t_0 = 60|1.03|0.69|**0.10**|_2.25_|0.96|0.62|**0.13**|_10.82_|1.11|0.64|**0.14**|_39.75_|
|||||||_p_|= 5||||||
|_T −t_0 = 5|_0.26_|0.16|0.03|**0.02**|_0.25_|0.15|0.03|**0.03**|_0.27_|0.16|**0.03**|0.06|
|_T −t_0 = 20|_1.14_|0.73|**0.11**|0.21|_1.05_|0.65|**0.12**|0.60|1.19|0.70|**0.12**|_1.62_|
|_T −t_0 = 60|_3.46_|2.20|**0.33**|2.40|2.49|1.56|**0.34**|_10.34_|3.69|2.15|**0.39**|_39.67_|



Note: Table provides average time in seconds over 1000 repetitions of a draw of conditional forecast for the 26 variable VAR considered in section 4. The following algorithms are considered: CK - the simulation smoother of Carter and Kohn (1994); DK,H - the simulation smoother of Durbin and Koopman (2002) with a “traditional” Kalman smoother implementation (see e.g. Hamilton, 1994, pp. 394-396); DK,dJ - the simulation smoother of Durbin and Koopman (2002) with the Kalman smoother implementation of de Jong (1988); WZ,J - the algorithm of Waggoner and Zha (1999) with the implementation of Jaroci´nski (2010). _n −_ #( _I_ ) refers to the number of variables in the conditioning set, _T − t_ 0 to the number of conditioning periods and _p_ is the number of lags in the VAR. The time of fastest algorithm in each case is marked in boldface, whereas the time for the slowest is put in italics. 

The results indeed show large computational gains of the algorithms based on the Kalman filter over the approach of Waggoner and Zha (1999) and Jaroci´nski (2010) when the number of restrictions (a combination of the number of conditioning variables and conditioning periods) increases. In the extreme case of 60 conditioning periods and 25 conditioning variables the latter algorithm needs 11 hours for 1000 draws compared to 1-7 minutes in case of the simulation smoother of Durbin and Koopman (2002) with the Kalman smoother implementation of de Jong (1988). This algorithm fares by far the best among the approaches based on the Kalman filter, with larger improvements relative to the algorithm of Carter and Kohn (1994) 

32The computations were performed with Matlab R2008a on a computer with Intel CORE Duo ˜ 2925 Mhz processor and 4.1 GB physical memory. 

ECB Working Paper 1733, September 2014 

35 

as the number of lags included in the VAR increases. As expected, the computational time of the Waggoner and Zha (1999) and Jaroci´nski (2010) algorithm is unaffected by the number of lags in the VAR while the performance of the algorithms based on the Kalman filter is not much affected by the number of conditioning variables. 

# **B Estimation** 

## **B.1 Dynamic factor model** 

If the factors were observed the joint likelihood of the data and the factors would be easily maximised and the estimates of the parameters would correspond to ordinary least squares outcomes. Specifically Λ and Γ _d_ would be obtained by regressing ∆ _yt_ on _Ft_ while the autoregressive parameters Φ1 _, . . . ,_ Φ _s_ and the covariance matrix _Q_ would be obtained by regressing _Ft_ on its lags, _Ft−_ 1 _, . . . , Ft−s_ . 

As the factors are unobserved the likelihood of the data cannot be maximised explicitly. As an alternative to numerical optimisation methods, the EM algorithm alternates between computing the expectation of the joint likelihood of the data and the factors given the parameter estimates from the previous step (E-step) and deriving new estimates by maximising the expected likelihood (M-step). An interesting property is that at each step the likelihood of the data increases, insuring that a convergence to a local maximum is reached. 

Maximising the expected likelihood given the parameters at the _j_<sup>t</sup><sup>_h_</sup> iteration is achieved through substituting the sufficient statistics with their expectation. This amounts to replacing the unobserved factors with their expected value _F_<sup>ˆ</sup> _t_<sup>(</sup><sup>_j_)</sup> = E _θ_ ( _j−_ 1) [ _Ft|y_ 1 _, . . . , yT_ ], and correcting for estimation uncertainty which is measured as 



Those quantities can be computed recursively using the Kalman smoother. 

It is easily seen that the expected sufficient statistics are as follows: 



ECB Working Paper 1733, September 2014 

36 

and 



As a consequence the M-step consists of the following equations, where for simplicity we consider the case _s_ = 1<sup>33</sup> : 

and 



Principal components represent a good starting point for the EM algorithm. The initial estimates of the factor loadings are obtained by regressing ∆ _yt_ on the principal components: 



The variance of the idiosyncratic residuals is hence given by: 



The total variance of the residual is given by: trace(Γ<sup>ˆ(0)</sup> _d_<sup>) =</sup><sup>_dr_+1 +</sup><sup>_. . ._+</sup><sup>_dn_.</sup> 

Turning to the estimation of the VAR model for the common factors, the OLS estimates, treating the factors as known, can be obtained as follows: 



> 33Extending it for more general situations is straightforward. Ba´nbura and Modugno (2014) show how to modify the following formulas in case some of the observations in ∆ _yt_ are missing. 

ECB Working Paper 1733, September 2014 

37 

and 



It is important to stress that this algorithm is more efficient when the scale of all the variables is similar. Hence, although the QML estimates are scale invariant, it is useful to standardise variables beforehand. The scale can be re-attributed accordingly once the likelihood is maximised. Standardisation is also useful for assuring a good initialisation since principal components are not scale invariant. 

## **B.2 Bayesian vector autoregression** 

In this section we summarise the procedures derived by Giannone, Lenza, and Primiceri (2014). Consider the VAR model of section 2.2: 



and rewrite it as 



_′ ′_ where _y ≡_ ( _yp_ +1 _, . . . , yT_ )<sup>_′_</sup> , _Y ≡ vec_ ( _y_ ), _xt ≡_ (1 _, yt_<sup>_′_</sup> _−_ 1<sup>_, . . . , y_</sup> _t_<sup>_′_</sup> _−p_ ) , _x ≡_ ( _xp_ +1 _, . . . , xT_ ) , _X ≡ In ⊗ x_ , _ε ≡_ ( _εp_ +1 _, . . . , εT_ )<sup>_′_</sup> , _ϵ ≡ vec_ ( _ε_ ), _B ≡_ ( _c, A_ 1 _, . . . , Ap_ )<sup>_′_</sup> and _β ≡ vec_ ( _B_ ). Finally, denote the number of regressors for each equation by _k ≡ np_ + 1. 

For expositional convenience we will focus first on the implementation of the Minnesota prior. Later in the section, we will describe how to implement the sum-of-coefficient and the dummyinitial-observation prior. 

The Minnesota prior on ( _β,_ Σ) is given by the following normal-inverse-Wishart distribution: 



ECB Working Paper 1733, September 2014 

38 

The posterior is given by: 



where _B_<sup>ˆ</sup> _≡_ ( _x_<sup>_′_</sup> _x_ + Ω<sup>_−_</sup> Ψ<sup>1</sup> _,λ_ ) _−_ 1<sup>(</sup> _x_<sup>_′_</sup> _y_ + Ω<sup>_−_</sup> Ψ<sup>1</sup> _,λ_<sup>ˆ</sup><sup>_b_</sup> ), _β_<sup>ˆ</sup> _≡ vec_ ( _B_ ˆ), _ε_ ˆ _≡ y − xB_<sup>ˆ</sup> , _ϵ_ ˆ _≡ vec_ (ˆ _ε_ ), and<sup>ˆ</sup> _b_ is a _k × n_ matrix obtained by reshaping the vector _b_ in such a way that each column corresponds to the prior mean of the coefficients of each equation (i.e. _b ≡ vec_ (<sup>ˆ</sup> _b_ )). 

We follow Giannone, Lenza, and Primiceri (2014) and set an almost flat, but proper, hyperprior. For _λ_ we choose Gamma distribution with mode equal to 0.2 and standard deviation equal to 0.4. Our prior on Ψ is an inverse-Gamma with scale and shape equal to (0 _._ 02)<sup>2</sup> . 

The posterior for the hyperparameters is _p_ (Ψ _, λ|Y_ ) _∝ p_ ( _Y |_ Ψ _, λ_ ) _p_ (Ψ _, λ_ ), where _p_ ( _Y |_ Ψ _, λ_ ) is the marginal likelihood, which takes the following form (see Giannone, Lenza, and Primiceri, 2014): 



Draws from the joint posterior of the parameters and hyperparameters can be easily derived by using the following algorithm. Since the marginal likelihood conditional on the hyperparameters is available in closed form, the hyperparameters can be drawn using the MetropolisHastings algorithm. For any draw of the hyperparameters Ψ and _λ_ , the covariance matrix of the residuals Σ and the autoregressive parameters _β_ can be drawn from their distributions conditional on Ψ and _λ_ . 

### **B.2.1 Implementing the “sum-of-coefficients” and the “dummy-initial-observation” priors** 

The sum-of-coefficient prior is implemented by using the following dummy observations: 



ECB Working Paper 1733, September 2014 

39 

where _y_ ¯0 is the average of the first _p_ initial observations, **1** _p_ is a _p ×_ 1 vector of ones and **0** _n_ is a _n ×_ 1 vector of zeros. 

Similarly, the dummy-initial-observation prior is implemented by using the following dummy observations: 



These dummy observations are added to the data and the procedure described above is per- _′ ∗ ′_ formed on the augmented data set _Yµ,δ_<sup>_∗_=</sup> ( _Y_<sup>_′_</sup> _Yµ_<sup>_′Y_</sup> _δ_<sup>_′_</sup> ) and _Xµ_<sup>=</sup> ( _X_<sup>_′_</sup> _Xµ_<sup>_′X_</sup> _δ_<sup>_′_</sup> ) . The only correction that has to taken into account concerns the marginal likelihood which should be computed on the original data only. As derived in Giannone, Lenza, and Primiceri (2014), this is equivalent to taking the ratio between the marginal likelihood of the augmented data set relative to the marginal likelihood of the dummy observations: 



The prior distributions for _µ_ and _δ_ are Gamma distributions with mode and standard deviation equal to 1. 

ECB Working Paper 1733, September 2014 

40 

# **C Description of the data set** 

|No|Short name|Description|Source|Transformation<br>(BVAR in levels)|
|---|---|---|---|---|
|1|Global GDP|World gross domestic product|AWM|4_×_log-levels|
|2|Real GDP|Real gross domestic product, euro area|AWM|4_×_log-levels|
|3|Real consumption|Real private consumption, euro area|AWM|4_×_log-levels|
|4|Government consumption|Real government consumption, euro area|AWM|4_×_log-levels|
|5|Real investment|Real gross investment, euro area|AWM|4_×_log-levels|
|6|Real exports|Real exports of goods and services, intra and extra<br>euro area|AWM|4_×_log-levels|
|7|Real imports|Real imports of goods and services, intra and extra<br>euro area|AWM|4_×_log-levels|
|8|Employment|Total employment (persons), euro area|AWM|4_×_log-levels|
|9|Unemployment rate|Unemployment rate (as a ratio to the civilian<br>workforce), euro area|AWM|Raw|
|10|Economic sentiment|Economic sentiment indicator, survey of the Euro-<br>pean Commission, euro area|Eurostat|Raw/100|
|11|Oil price|Price of oil in US dollars|AWM|4_×_log-levels|
|12|N.-o. comm. prices|Non-oil commodity prices in US dollars|AWM|4_×_log-levels|
|13|HICP|Harmonised index of consumer prices, euro area|AWM|4_×_log-levels|
|14|PPI ex. const.|Producer price index, domestic sales, total indus-<br>try excluding construction, euro area|ECB|4_×_log-levels|
|15|GDP defator|GDP defator, euro area|AWM|4_×_log-levels|
|16|Imports defator|Imports of goods and services defator, intra and<br>extra euro area|AWM|4_×_log-levels|
|17|Nominal wages|Compensation per employee, euro area|AWM|4_×_log-levels|
|18|US short-term i. r.|US short-term interest rate, 3-month dep. LIBOR|IMF (IFS)|Raw/100|
|19|Short-term i. r.|Short-term interest rate, 3-month EURIBOR|AWM|Raw/100|
|20|Long-term i. r.|Long-term interest rate, euro area 10-year govern-<br>ment benchmark bond yield|AWM|Raw/100|
|21|M1|Monetary aggregate M1, index of notional stocks,<br>euro area|ECB|4_×_log-levels|
|22|M3|Monetary aggregate M3, index of notional stocks,<br>euro area|ECB|4_×_log-levels|
|23|Loans to households|Loans to households, sum of consumer loans, loans<br>for house purchases and other loans, index of no-<br>tional stocks, euro area|ECB|4_×_log-levels|
|24|Loans to frms|Loans to non-fnancial corporations, index of no-<br>tional stocks, euro area|ECB|4_×_log-levels|
|25|Efective exchange rate|Nominal<br>efective<br>exchange<br>rate<br>of<br>the<br>euro<br>(against main 20 trading partners)|AWM|4_×_log-levels|
|26|Stock prices|Dow Jones Euro Stoxx price index|DataStream|4_×_log-levels|



Note: In the BVAR in differences and in the DFM specification we take the first difference of the variables transformed as in the BVAR in levels. AWM refers to the 13<sup>th</sup> update of the Area Wide Model data base (Fagan, Henry, and Mestre, 2005). 

ECB Working Paper 1733, September 2014 

41 

# **References** 

- Adolfson, M., S. Las´een, J. Lind´e, and M. Villani (2005): “Are constant interest rate forecasts modest interventions? Evidence from an estimated open economy DSGE model of the euro area,” _International Finance_ , 8, 509–544. 

- Bai, J. (2003): “Inferential theory for factor models of large dimensions,” _Econometrica_ , 71(1), 135–171. 

- Bai, J., and S. Ng (2002): “Determining the number of factors in approximate factor models,” _Econometrica_ , 70(1), 191–221. 

- Ba´nbura, M., D. Giannone, and L. Reichlin (2010): “Large Bayesian vector auto regressions,” _Journal of Applied Econometrics_ , 25(1), 71–92. 

- Ba´nbura, M., and M. Modugno (2014): “Maximum likelihood estimation of factor models on datasets with arbitrary pattern of missing data,” _Journal of Applied Econometrics_ , 29(1), 133–160. 

- Baumeister, C., and L. Kilian (2013): “Real-time analysis of oil price risks using forecast scenarios,” _IMF Economic Review_ , 62(1), 119–145. 

- Bloor, C., and T. Matheson (2011): “Real-time conditional forecasts with Bayesian VARs: An application to New Zealand,” _The North American Journal of Economics and Finance_ , 22(1), 26–42. 

- Carriero, A., T. E. Clark, and M. Marcellino (2012): “Common drifting volatility in large Bayesian VARs,” Working Paper 1206, Federal Reserve Bank of Cleveland. 

- Carter, C., and P. Kohn (1994): “On Gibbs sampling for state space models,” _Biometrica_ , 81, 541–553. 

- Christiano, L. J., M. Eichenbaum, and C. L. Evans (1999): “Monetary policy shocks: What have we learned and to what end?,” in _Handbook of Macroeconomics_ , ed. by J. B. Taylor, and M. Woodford, vol. 1, chap. 2, pp. 65–148. Elsevier. 

- Christoffel, K., G. Coenen, and A. Warne (2007): “Conditional versus unconditional forecasting with the new area-wide model of the euro area,” Mimeo, European Central Bank. 

- Clarida, R. H., and D. Coyle (1984): “Conditional projection by means of Kalman filtering,” NBER Technical Working Papers 0036, National Bureau of Economic Research, Inc. 

- Clark, T. E., and M. W. McCracken (2014): “Evaluating conditional forecasts from vector autoregressions,” Mimeo, Federal Reserve Bank of St. Louis. 

ECB Working Paper 1733, September 2014 

42 

- de Jong, P. (1988): “A cross-validation filter for time series models,” _Biometrika_ , 75(3), 594–600. 

- de Jong, P., and N. Shephard (1995): “The simulation smoother for time series models,” _Biometrika_ , 2, 339–350. 

- De Mol, C., D. Giannone, and L. Reichlin (2008): “Forecasting using a large number of predictors: Is Bayesian shrinkage a valid alternative to principal components?,” _Journal of Econometrics_ , 146(2), 318–328. 

- Dempster, A., N. Laird, and D. Rubin (1977): “Maximum likelihood estimation from incomplete data,” _Journal of the Royal Statistical Society_ , 14, 1–38. 

- Diron, M., and B. Mojon (2005): “Forecasting the central banks inflation objective is a good rule of thumb,” Working Paper Series 0564, European Central Bank. 

- Doan, T., R. Litterman, and C. A. Sims (1984): “Forecasting and conditional projection using realistic prior distributions,” _Econometric Reviews_ , 3, 1–100. 

- Doz, C., D. Giannone, and L. Reichlin (2011): “A two-step estimator for large approximate dynamic factor models based on Kalman filtering,” _Journal of Econometrics_ , 164(1), 188–205. 

   - (2012): “A quasi-maximum likelihood approach for large, approximate dynamic 

   - factor models,” _The Review of Economics and Statistics_ , 94(4), 1014–1024. 

- Durbin, J., and S. Koopman (2002): “A simple and efficient simulation smoother for state space time series analysis,” _Biometrika_ , 89(3), 603–615. 

- Durbin, J., and S. J. Koopman (2001): _Time Series Analysis by State Space Methods_ . Oxford University Press. 

- Fagan, G., J. Henry, and R. Mestre (2005): “An area-wide model for the euro area,” _Economic Modelling_ , 22(1), 39–59. 

- Foerster, A. T., P.-D. G. Sarte, and M. W. Watson (2011): “Sectoral versus aggregate shocks: a structural factor analysis of industrial production,” _Journal of Political_ – 

- _Economy_ , 119(1), 1 38. 

- Forni, M., M. Hallin, M. Lippi, and L. Reichlin (2000): “The generalized dynamic factor model: identification and estimation,” _Review of Economics and Statistics_ , 82, 540– 554. 

   - (2004): “The generalized dynamic factor model: consistency and rates,” _Journal of_ 

   - _Econometrics_ , 119, 231–245. 

- Giannone, D., M. Lenza, D. Momferatou, and L. Onorante (2014): “Short-term inflation projections: a Bayesian vector autoregressive approach,” _International Journal of Forecasting_ , 30(3), 635–644. 

ECB Working Paper 1733, September 2014 

43 

- Giannone, D., M. Lenza, H. Pill, and L. Reichlin (2012): “The ECB and the interbank market,” _Economic Journal_ , 122(564), F467–F486. 

- Giannone, D., M. Lenza, and G. E. Primiceri (2014): “Prior selection for vector autoregressions,” _Review of Economics and Statistics_ , forthcoming. 

- Giannone, D., M. Lenza, and L. Reichlin (2010): “Business cycles in the euro area,” in _Europe and the Euro_ , NBER Chapters, pp. 141–167. National Bureau of Economic Research, Inc. 

   - (2012): “Money, credit, monetary policy and the business cycle in the euro area,” 

   - CEPR Discussion Papers 8944, C.E.P.R. Discussion Papers. 

- Giannone, D., L. Reichlin, and L. Sala (2004): “Monetary policy in real time,” in _NBER Macroeconomics Annual_ , ed. by M. Gertler, and K. Rogoff, pp. 161–200. MIT Press. 

- Giannone, D., L. Reichlin, and D. Small (2005): “Nowcasting GDP and inflation: the real-time informational content of macroeconomic data releases,” Finance and Economics Discussion Series 2005-42, Board of Governors of the Federal Reserve System (U.S.). 

- Greene, W. H. (2002): _Econometric Analysis_ . Prentice Hall. 

- Hamilton, J. D. (1994): _Time Series Analysis_ . Princeton University Press. 

- Harvey, A. (1989): _Forecasting, Structural Time Series Models and the Kalman Filter_ . Cambridge University Press. 

- Jardet, C., A. Monfort, and F. Pegoraro (2012): “New information response functions and applications to monetary policy,” Mimeo, Banque de France. 

- Jaroci´nski, M. (2010): “Conditional forecasts and uncertainty about forecast revisions in vector autoregressions,” _Economics Letters_ , 108(3), 257–259. 

- Jaroci´nski, M., and F. R. Smets (2008): “House prices and the stance of monetary policy,” _Review_ , (Jul), 339–366. 

- Jungbacker, B., and S. J. Koopman (2008): “Likelihood-based analysis for dynamic factor models,” Tinbergen Institute Discussion Papers 08-007/4, Tinbergen Institute. 

- Karlsson, S. (2013): “Forecasting with Bayesian vector autoregressions,” in _Handbook of Economic Forecasting, Volume 2B_ , ed. by G. Elliott, and T. Timmermann. North Holland, Elsevier. 

- Kilian, L., and L. T. Lewis (2011): “Does the Fed respond to oil price shocks?,” _Economic Journal_ , 121(555), 1047–1072. 

- Koop, G., M. H. Pesaran, and S. M. Potter (1996): “Impulse response analysis in nonlinear multivariate models,” _Journal of Econometrics_ , 74(1), 119–147. 

ECB Working Paper 1733, September 2014 

44 

- Koop, G. M. (2013): “Forecasting with medium and large Bayesian VARs,” _Journal of Applied Econometrics_ , 28(2), 177–203. 

- Kose, M. A., C. Otrok, and C. H. Whiteman (2003): “International business cycles: world, region, and country-specific factors,” _American Economic Review_ , 93, 1216–1239. 

- Leeper, E. M., and T. Zha (2003): “Modest policy interventions,” _Journal of Monetary Economics_ , 50(8), 1673–1700. 

- Lenza, M., H. Pill, and L. Reichlin (2010): “Monetary policy in exceptional times,” _Economic Policy_ , 25, 295–339. 

- Litterman, R. B. (1979): “Techniques of forecasting using vector autoregressions,” Discussion paper. 

- Luciani, M. (2013): “Monetary policy and the housing market: a structural factor analysis,” _Journal of Applied Econometrics_ , forthcoming. 

- Ng, S. (2013): “Variable selection in predictive regressions,” in _Handbook of Economic Forecasting, Volume 2B_ , ed. by G. Elliott, and T. Timmermann. North Holland, Elsevier. 

- Paciello, L. (2011): “Does inflation adjust faster to aggregate technology shocks than to monetary policy shocks?,” _Journal of Money, Credit and Banking_ , 43(8), 1663–1684. 

- Pesaran, H., and Y. Shin (1998): “Generalized impulse response analysis in linear multi– 

- variate models,” _Economics Letters_ , 58(1), 17 29. 

- Primiceri, G. E. (2005): “Time Varying Structural Vector Autoregressions and Monetary Policy,” _Review of Economic Studies_ , 72(3), 821–852. 

- Schorfheide, F., and D. Song (2013): “Real-Time Forecasting with a Mixed-Frequency VAR,” NBER Working Papers 19712, National Bureau of Economic Research, Inc. 

- Shumway, R., and D. Stoffer (1982): “An approach to time series smoothing and forecasting using the EM algorithm,” _Journal of Time Series Analysis_ , 3, 253–264. 

- Sims, C. A. (1980): “Macroeconomics and reality,” _Econometrica_ , 48(1), pp. 1–48. 

   - (1993): “A nine-variable probabilistic macroeconomic forecasting model,” in _Busi-_ 

   - _ness Cycles, Indicators and Forecasting_ , NBER Chapters, pp. 179–212. National Bureau of Economic Research, Inc. 

- Sims, C. A., and T. Zha (1998): “Bayesian methods for dynamic multivariate models,” _International Economic Review_ , 39(4), 949–68. 

- Stock, J. H., and M. W. Watson (2002a): “Forecasting using principal components from a large number of predictors,” _Journal of the American Statistical Association_ , 97, 147–162. 

ECB Working Paper 1733, September 2014 

45 

   - (2002b): “Macroeconomic forecasting using diffusion indexes.,” _Journal of Business_ 

   - _and Economics Statistics_ , 20, 147–162. 

   - (2011): “Dynamic factor models,” in _The Oxford Handbook of Economic Forecasting_ , 

   - ed. by M. P. Clements, and D. F. Hendry. Oxford University Press. 

   - (2012a): “Disentangling the channels of the 2007-2009 recession,” NBER Working 

   - Papers 18094, National Bureau of Economic Research, Inc. 

   - (2012b): “Generalized shrinkage methods for forecasting using many predictors,” 

   - _Journal of Business & Economic Statistics_ , 30(4), 481–493. 

- Waggoner, D. F., and T. Zha (1999): “Conditional forecasts in dynamic multivariate models,” _The Review of Economics and Statistics_ , 81(4), 639–651. 

- Watson, M. W., and R. F. Engle (1983): “Alternative algorithms for the estimation of dynamic factor, mimic and varying coefficient regression models,” _Journal of Econometrics_ , 23, 385–400. 

ECB Working Paper 1733, September 2014 

46 

