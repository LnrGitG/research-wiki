---
title: Bayesian Vector Autoregressions
type: paper
source_pdf: raw/papers/CFMDP2018-08-Paper.pdf
converted: 2026-07-26
---

# Bayesian Vector Autoregressions 

Silvia Miranda-Agrippino<sup>_∗_</sup> Bank of England and CFM 

Giovanni Ricco<sup>_†_</sup> University of Warwick and OFCE - SciencesPo 

This version: 23 March 2018 

##### **Abstract** 

This article reviews Bayesian inference methods for Vector Autoregression models, commonly used priors for economic and financial variables, and applications to structural analysis and forecasting. 

**Keywords:** Bayesian inference, Vector Autoregression Models, BVAR, SVAR, forecasting 

**JEL Classification:** C30, C32, E00 

> _∗_ Monetary Analysis, Bank of England, Threadneedle Street, London EC2R 8AH, UK. Email: `silvia.miranda-agrippino@bankofengland.co.uk` Web: `www.silviamirandaagrippino.com` 

> _†_ Department of Economics, The University of Warwick, The Social Sciences Building, Coventry, West Midlands CV4 7AL, UK. Email: `G.Ricco@warwick.ac.uk` Web: `www.giovanni-ricco.com` 

This is a draft of an article that has been submitted for publication by Oxford University Press in the forthcoming Oxford Encyclopedia of Economics and Finance, `http://economics.oxfordre.com/` . 

**Acknowledgments.** We are grateful to Fabio Canova, Andrea Carriero, Matteo Ciccarelli, Domenico Giannone, Marek Jaroci´nski, Dimitris Korobilis, Marco del Negro, Massimiliano Marcellino, Giorgio Primiceri, Lucrezia Reichlin and Frank Shorfheide for helpful comments and discussions. The views expressed in this paper are those of the authors and do not necessarily reflect those of the Bank of England or any of its Committees. 

|**C**|**on**|**tents**|
|---|---|---|
|**1**|**Int**|**roduction**<br>**3**|
|**2**|**Inf**|**erence in BVARs**<br>**7**|
|**3**|**Inf**|**ormative Priors for Reduced-Form VARs**<br>**13**|
||3.1|Natural Conjugate Normal-Inverse Wishart Priors . . . . . . . . . . . . .<br>14|
||3.2|Minnesota Prior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>17|
||3.3|Priors for VAR with Unit Roots and Trends . . . . . . . . . . . . . . . .<br>20|
||3.4|Priors from Structural Models . . . . . . . . . . . . . . . . . . . . . . . .<br>24|
||3.5|Priors for Model Selection . . . . . . . . . . . . . . . . . . . . . . . . . .<br>25|
|**4**|**Hy**|**perpriors and Hierarchical Modelling**<br>**26**|
|**5**|**For**|**ecasting with BVARs**<br>**28**|
||5.1|Bayesian Forecasting . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>28|
||5.2|Bayesian Model Averaging and Prediction Pools . . . . . . . . . . . . . .<br>30|
|**6**|**Co**|**nditional Forecasts and Scenario Analysis**<br>**32**|
|**7**|**Str**|**uctural VARs**<br>**34**|
|**8**|**Lar**|**ge Bayesian VARs**<br>**39**|
||8.1|Bayesian VARs and Dynamic Factor Models . . . . . . . . . . . . . . . .<br>41|
||8.2|Large SVARs, non-fundamentalness . . . . . . . . . . . . . . . . . . . . .<br>43|
||8.3|Forecasting in Data-Rich Environments . . . . . . . . . . . . . . . . . . .<br>43|
|**9**|**Tim**|**e-Varying Parameter, State-Dependent, Stochastic Volatility VARs 45**|
||9.1|Time-varying parameters VAR (TVP-VAR)<br>. . . . . . . . . . . . . . . .<br>45|
||9.2|Markov Switching, Threshold, and Smooth Transition VARs . . . . . . .<br>48|



2 

## **1 Introduction** 

Vector Autoregressions (VARs) are linear multivariate time-series models able to capture the joint dynamics of multiple time series. The pioneering work of Sims (1980) proposed to replace the large-scale macroeconomic models popular in the 1960s with VARs, and suggested that Bayesian methods could have improved upon frequentist ones in estimating the model coefficients. Bayesian VARs (BVARs) with macroeconomic variables were first employed in forecasting by Litterman (1979) and Doan et al. (1984). Since then, VARs and BVARs have been a standard macroeconometric tool routinely used by scholars and policy makers for structural analysis, forecasting and scenario analysis in an ever growing number of applications. 

The aim of this article is to review key ideas and contributions in the BVAR literature, and to provide a brief introduction to estimation methods for BVARs in Economics, and review selected applications such as forecasting, structural identification and scenario analysis. An exhaustive survey of the literature is beyond the scope of this article due to space limitations. Readers are referred to a number of monographs and more detailed surveys available on different topics in the BVARs literature.<sup>1</sup> 

Differently from frequentist statistics, Bayesian inference treats the VAR parameters as random variables, and provides a framework to update probability distributions about the unobserved parameters conditional on the observed data. By providing such a framework, the Bayesian approach allows to incorporate prior information about the model parameters into post-sample probability statements. The ‘prior’ distributions 

> 1Several books provide excellent in-depth treatments of Bayesian inference. Among others, Zellner (1971), Gelman et al. (2003), Koop (2003) and Geweke (2005). Canova (2007) provides a book treatment of VARs and BVARs in the context of the methods for applied macroeconomic research. Several recent articles survey the literature on BVARs. Del Negro and Schorfheide (2011) have a deep and insightful discussion of BVAR with a broader focus on Bayesian macroeconometrics and DSGE models. Koop and Korobilis (2010) propose a discussion of Bayesian multivariate time series models with an indepth discussion of time-varying parameters and stochastic volatility models. Geweke and Whiteman (2006a) and Karlsson (2013b) provide a detailed survey with a focus on forecasting with Bayesian Vector Autoregression. Ciccarelli and Rebucci (2003) survey BVARs in forecasting analysis with Euro Area data. Canova and Ciccarelli (2013) discuss panel Bayesian VARs, a topic that is not discussed in this article. Finally, the reader is referred to Timmermann (2006) for an in-depth discussion on model averaging and forecast combination, a natural extension of the Bayesian framework. Dieppe et al. (2016) have developed the ready-to-use BEAR toolbox that implements many of the methods described in this article. 

3 

about the location of the model parameters summarise pre-sample information available from a variety of sources, such as other macro o micro datasets, theoretical models, other macroeconomic phenomena, or introspection. 

In the absence of pre-sample information, Bayesian VAR inference can be thought of as adopting ‘non-informative’ (or ‘diffuse’ or ‘flat’) priors, that express complete ignorance about the model parameters, in the light of the sample evidence summarised by the likelihood function (i.e. the probability density function of the data as a function of the parameters). Often, in such a case, Bayesian probability statements about the unknown parameters (conditional on the data) are very similar to classical confidence statements about the probability of random intervals around the true parameters value. For example, for a VAR with Gaussian errors and a flat prior on the model coefficients, the posterior distribution is centred at the maximum likelihood estimator (MLE), with variance given by the variance-covariance matrix of the residuals. Section 2 discusses inference in BVARs and ‘non-informative’ priors. 

While non-informative priors can provide a useful benchmark, in empirical work with macroeconomic and financial variables informative priors are often adopted. In scientific data analysis, priors on the model coefficients do not incorporate the investigator’s ‘subjective’ beliefs, instead, they summarise stylised representations of the data generating process. Conditional on a model, these widely held standardised priors aim at making the likelihood-based description of the data useful to investigators with potentially diverse prior beliefs (Sims, 2010b).<sup>2</sup> 

The most commonly adopted macroeconomic priors for VARs are the the so-called ‘Minnesota’ priors (Litterman, 1980). They express the belief that an independent random-walk model for each variable in the system is a reasonable ‘centre’ for the beliefs about their time series behaviour. While not motivated by economic theory, they are computationally convenient priors, meant to capture commonly held beliefs about how economic time series behave. Minnesota priors can be cast in the form of a Normal- 

> 2 Bayesian priors can often be interpreted as frequentist penalised regressions (see, for example, De Mol et al., 2008). A Gaussian prior for the regression coefficients, for example, can be thought of as a Ridge penalised regression. Having a double exponential (Laplace) prior on the coefficients is instead equivalent to a Lasso regularisation problem. 

4 

Inverse-Wishart (NIW) prior, which is the conjugate prior for the likelihood of a VAR with normally distributed disturbances (see Kadiyala and Karlsson, 1997). Conjugate priors are such that the posterior distribution belongs to the same family as the prior probability distribution. Hence, they allow for analytical tractability of the posterior, and computational speed. Because the data is incorporated into the posterior distribution only through the sufficient statistics, formulas for updating the prior into the posterior are in this case conveniently simple. It is often useful to think of the – – parameters of a prior distribution known as ‘hyperparameters’ as corresponding to having observed a certain number of ‘dummy’ or ‘pseudo-’ observations with properties specified by the prior beliefs on the VAR parameters. Minnesota priors can be formulated in terms of artificial data featuring pseudo observations for each of the regression coefficients, and that directly assert the prior on them. 

Dummy observations can also implement prior beliefs about relations among the VAR coefficients, such as e.g. co-integration among variables. In this case, commonly used priors are formulated directly as linear joint stochastic restrictions among the coefficients.<sup>3</sup> This is, for example, the case of the ‘single-unit root’ prior, that is centred on a region of the VAR parameter space where either there is no intercept and the system contains at least one unit root, or the system is stationary and close to its steady state at the beginning of the sample (Sims, 1993).<sup>4</sup> Another instance in which dummy observations are used to establish relations among several coefficients is the ‘sum-of-coefficients’ prior, that incorporates the widely shared prior beliefs that economic variables can be represented by a process with unit roots and weak cross-sectional linkages (Litterman, 1979).<sup>5</sup> Section 3 discusses some of the priors commonly adopted in the economic liter- 

> 3In principle, dummy observations can also implement prior beliefs about nonlinear functions of the parameters (a short discussion on this is in Sims, 2005b). 

> 4Such a prior is adopted to capture the belief that it is not plausible to assume that initial transients can explain a large part of observed long-run variation in economic time series. Since in a sample of given size there is no information on the behaviour of time series at frequencies longer than the sample size, the prior assumptions implicitly or explicitly elicited in the analysis will inform results. This is a clear example, in the inference in VARs, of an issue for which Bayesian inference provides a framework to make prior information explicit and available to scientific discussion on the inference in VAR models. 

> 5Several sets of pseudo-observations can be adopted at the same time. In fact, successive dummy observations modify the prior distribution as if they reflected successive observations of functions of the VAR parameters, affected by stochastic disturbances. 

5 

#### ature. 

The hyperparameters can be either fixed using prior information (and sometimes ‘unorthodoxly’ using sample information), or associated to hyperprior distributions that express beliefs about their values. A Bayesian model with more than one level of priors is called a hierarchical Bayes model. In empirical macroeconomic modelling, the hyperparameters associated with the informativeness of the prior beliefs (i.e. the tightness of the prior distribution) are usually left to the investigator’s judgement. In order to select a value for these hyperparameters, the VAR literature has adopted mostly heuristic methodologies that minimise pre-specified loss functions over a pre-sample (e.g. the out-of-sample mean squared forecast error in Litterman, 1979, or the in-sample fit in Ba´nbura et al., 2010). Conversely, Giannone et al. (2015) specify hyperprior distributions and choose the hyperparameters that maximise their posterior probability distribution conditional on the data. Section 4 discusses hierarchical modelling and common approaches to choose hyperparameters not specified by prior information. 

BVARs have been applied to an increasingly large number of empirical problems. Forecasting, however, has featured predominantly in the development of BVARs. In this context, BVARs with informative priors have often proved to be superior tools compared to standard frequentist/flat-prior VARs. VARs are highly parametrised autoregressive models, whose number of parameters grows with the square of the number of variables times the number of lags included. Given the limited length of standard macroeco– nomic datasets that usually involve monthly, quarterly, or even annual observations –, such overparametrisation makes the estimation of VARs impossible with standard (frequentist) techniques, already for relatively small sets of variables. This is known in the literature as the ‘curse of dimensionality’. BVARs efficiently deal with the problem of over-parametrisation through the use of prior information about the model coefficients. The general idea is to use informative priors that shrink the unrestricted model towards a parsimonious na¨ıve benchmark, thereby reducing parameter uncertainty, and improving forecast accuracy. Section 5 discusses forecasting with BVARs. 

Another important area of application is the study of causal relationships among economic variables with Structural (B)VARs (Sims and Zha, 1998). It is common practice 

6 

– to present results from SVARs in the form of impulse response functions i.e. causal responses over time of a given variable of interest to an ‘identified’ economic shock – together with bands that characterise the shape of the posterior distribution of the model (see Sims and Zha, 1999).<sup>6</sup> Section 7 reviews Bayesian techiniques in SVARs. 

The application of Bayesian techniques to ‘big data’ problems is one of the most active frontiers in the BVAR literature. Indeed, because they can efficiently deal with parameters proliferation, large BVARs are valuable tools to handle empirical analysis in data-rich environments (Ba´nbura et al., 2010). Important applications in this case also concern forecasting and structural analysis, where large-information BVARs can efficiently address issues related to misspecification and non-fundamentalness. De Mol et al. (2008) have discussed the connection between BVARs and factor models, another popular way to handle large datatsets. We review large BVARs in Section 8. 

Finally, in Section 9 we discuss Bayesian inference in VAR models that relax the assumption of fixed coefficients in order to capture changes in the time series dynamics of macroeconomic and financial variables, such as VARs with autoregressive coefficients, threshold and Markov switching VARs. 

## **2 Inference in BVARs** 

Vector Autoregressions (VARs) are linear stochastic models that describe the joint dynamics of multiple time series. Let _yt_ be an _n ×_ 1 random vector that takes values in – – R _n_ . The evolution of _yt_ the endogenous variables is described by a system of _p_ -th – order difference equations the VAR( _p_ ): 



> 6An extreme version of lack of sample information arises in this context. In fact Structural VARs can be parametrised in terms of reduced form VARs that capture the joint dynamics of economic variables, and an ‘impact matrix’ describing the casual connection between stochastic disturbances and economic variables. This matrix is not uniquely identified by sample information and hence the investigator has to elicit prior beliefs on it (see Sims and Zha, 1998; Baumeister and Hamilton, 2015). 

7 

In Eq. (1), _Aj, j_ = 1 _, . . . , p_ are _n × n_ matrices of autoregressive coefficients, _c_ is a vector of _n_ intercepts, and _ut_ is an _n_ -dimensional vector of one-step-ahead forecast errors, or reduced-form innovations. The vector of stochastic innovations, _ut_ , an independent and identically distributed random variable for each _t_ . The distribution from which _ut_ is drawn determines the distribution of _yt_ , conditional on its past _y_ 1 _−p_ : _t−_ 1 _≡{y_ 1 _−p, . . . , y_ 0 _, . . . , yt−_ 2 _, yt−_ 1 _}_ . The standard assumption in the macroeconometric literature is that errors are Gaussian 



This implies that also the conditional distribution of _yt_ is Normal.<sup>7</sup><sup>_,_8</sup> 

Bayesian inference on the model in Eq. (1) amounts to updating prior beliefs about the VAR parameters, that are seen as stochastic variables, after having observed a sample _y_ 1 _−p_ : _t ≡{y_ 1 _−p, . . . , y_ 0 _, . . . , yt−_ 2 _, yt}_ . Prior beliefs about the VAR coefficients are summarised by a probability density function (p.d.f.), and updated using Bayes’ Law 



where we define _A ≡_ [ _A_ 1 _, . . . , Ap, c_ ]<sup>_′_</sup> as a _k × n_ matrix, with _k_ = _np_ + 1. The joint posterior distribution of the VAR( _p_ ) coefficients _p_ ( _A,_ Σ _|y_ 1 _−p_ : _t_ ) incorporates the inform– ation contained in the prior distribution _p_ ( _A,_ Σ) summarising the initial information about the model parameters –, and the sample information summarised by _p_ ( _y_ 1 _−p_ : _t|A,_ Σ). Viewed as a function of the parameters, the sample information is the likelihood function.<sup>9</sup> The posterior distribution summarises the entire information available, and is 

> 7While the assumption of normally distributed errors makes the posterior p.d.f. tractable, modern computational methods permit straightforward characterisation of posterior distributions obtained under different assumptions. Among others, Chiu et al. (2017) and Panagiotelis and Smith (2008) depart from the normality assumption and allow for _t_ -distributed errors. 

> 8It is interesting to observe that in large samples, and under certain regularity conditions, the likelihood function converges to a Gaussian distribution, with mean at the maximum likelihood estimator (MLE) and covariance matrix given by the usual MLE estimator for the covariance matrix. This implies that conditioning on the MLE and using its asymptotic Gaussian distribution is, approximately in large samples, as good as conditioning on all the data (see discussion in Sims, 2010b). 

> 9 The marginal p.d.f. for the observations, denoted as _p_ ( _y_ 1 _−p_ : _t_ ), is a normalising constant and as such can be dropped when making inference about the model parameters. 

8 

used to conduct inference on the VAR parameters. 

Given the autoregressive structure of the model, and the i.i.d. innovations, the – (conditional) likelihood function of the sample observations _y_ 1: _T_ conditional on _A_ , Σ and on the first _p_ observations _y_ 1 _−p_ :0 –, can be written as the product of the conditional distribution of each observation 



Under the assumption of Gaussian errors, the conditional likelihood of the VAR in Eq. (1) is 



where _x_<sup>_′_</sup> _t_<sup>_≡_</sup> � _yt_<sup>_′_</sup> _−_ 1 _. . . yt_<sup>_′_</sup> _−p_ 1 �. The likelihood in Eq. (5) can be written in compact form, by using the seemingly unrelated regression (SUR) representation of the VAR 



where the _T × n_ matrices _y_ and _u_ and the _T × k_ matrix _x_ are defined as 



Using this notation and standard properties of the trace operator, the conditional likelihood function can be equivalently expressed as 



9 

where _A_<sup>�</sup> is the maximum-likelihood estimator (MLE) of _A_ , and _S_<sup>�</sup> the matrix of sums of squared residuals, i.e. 



The likelihood can also be written in terms of the vectorised representation of the VAR 



where **y** _≡ vec_ ( _y_ ) and **u** _≡ vec_ ( _u_ ) are _Tn ×_ 1 vectors, and _α ≡ vec_ ( _A_ ) is _nk ×_ 1. In this vectorised notation the likelihood function is written as 



where, consistently, _α_ ˆ _≡ vec_ ( _A_<sup>�</sup> ) is _nk ×_ 1. Detailed derivations for the multivariate Gaussian linear regression model can be found in Zellner (1971). 

Given the likelihood function, Eq. (3) is used to update the prior information regarding the VAR parameters. An interesting case arises when we assume the absence of any information on the location of the model parameters. This setting can be formalised by assuming that _α_ and Σ are independently distributed, i.e., 



with prior p.d.f. 



These priors are known as diffuse or Jeffreys’ prior (Geisser, 1965; Tiao and Zellner, 1964). Jeffreys priors are proportional to the square root of the determinant of the 

10 

Fisher information matrix, and are derived from the Jeffreys’ ‘invariance principle’, meaning that the prior is invariant to re-parameterization (see Zellner, 1971).<sup>10</sup> 

Given this set of priors, it is straightforward to derive the posterior distribution of the VAR parameters as 



where the proportionality factor has been dropped for convenience. 

From the joint posterior in Eq. (14) one can readily deduce the form of the posterior for _α_ , conditional on Σ and the observed sample. Also, the posterior can be integrated over _α_ to obtain the marginal posterior for Σ. Therefore, it is possible to conveniently write the posterior distribution of the parameters as 



where 





Hence, given the diffuse priors on _α_ and Σ, the posterior for the autoregressive coeffi- 

> 10‘Non-informative’ or ‘flat’ priors are designed to extract the maximum amount of expected information from the data. They maximise the difference (measured by Kullback-Leibler distance) between the posterior and the prior when the number of samples drawn goes to infinity. Jeffreys priors for VARs are ‘improper’, in the sense that they do not integrate to one over the parameter space. Hence, they cannot be thought of as well specified p.d.f. distributions. However, they can be obtained as degenerate limit of the Normal-Inverse-Wishart conjugate distribution, and their posterior is proper. For an in-depth discussion on non-informative priors in multi-parameter settings see Zellner (1971) and Bernardo and Smith (2009). 

11 

cients is centred at the MLE, with posterior variance Σ _⊗_ ( _x_<sup>_′_</sup> _x_ )<sup>_−_1</sup> .<sup>11</sup> Interestingly, in this standard normal multivariate linear regression model, Bayesian probability statements about the parameters (given the data) have the same form as the frequentist pre-sample probability statements about the parameters’ estimator (see also Sims, 2010b). This is a more general property, in fact, Kwan (1998) has shown that, under widely applicable regularity conditions, an estimator _α_ ˆ _T_ for which 



ˆ ˆ allows, with high accuracy, to approximate the distribution of _√T_ ( _α − αT_ ) _|α_ as _N_ (0 _,_ Σ) in large samples. Hence, it is often possible to interpret (1 _− ρ_ ) approximate confidence sets generated from the frequentist asymptotic approximate distribution as if they were sets in the parameter space with posterior probability (1 _− ρ_ ). 

In potentially misspecified models for which linear regression coefficients are the object of interest, M¨uller (2013) proposes to adopt an artificial Gaussian posterior centred at the MLE but with a sandwich estimator for the covariance matrix. In fact, in the case of a misspecified model, the shape of the likelihood (the posterior) is asymptotically Gaussian and centred at the MLE, but of a different variance than the asymptotically normal sampling distribution of the MLE. This argument can be seen as a ‘flipping’ of the frequentist asymptotic statement that supports the use of a sandwich estimator for the covariance matrix in misspecified models, in line with the results in Kwan (1998).<sup>12</sup> 

An important case in which frequentist pre-sample probability statements and Bayesian post-sample probability statements about parameters diverge, is the case of time- 

11 The marginal posterior distribution of the _k × n_ matrix _A_ is matricvariate _t_ 



> (see Kadiyala and Karlsson, 1997). 

> 12M¨uller (2013) shows that a Bayesian decision-maker can justify using OLS with a sandwich covariance matrix when the probability limit of the OLS estimator is the object of interest, despite the fact that the linear regression model is known not to be the true model (see discussion in Sims, 2010b). Miranda-Agrippino and Ricco (2017) use this intuition to construct coverage bands for impulse responses estimated with Bayesian Local Projections (BLP). This method can be thought of as a generalisation of BVARs that estimates a different model for different forecast horizons – as in direct forecasts – and hence induces autocorrelation in the reduced-form residuals that violate the the i.i.d. assumption in Eq. (2). 

12 

series regression models with unit roots. In such cases, while the frequentist distribution of the estimator is skewed asymptotically, the likelihood, and hence the posterior p.d.f., remain unaffected (see Sims and Uhlig, 1991; Kim, 1994). 

## **3 Informative Priors for Reduced-Form VARs** 

Informative prior probability distributions incorporate information about the VAR parameters that is available before some sample is observed. Such prior information can be – contained in samples of past data from the same or a related system –, or can be elicited from introspection, casual observation, and theoretical models. The first case is sometimes referred to as a ‘data-based’ prior, while the second as a ‘nondata-based’ prior. 

An important case arises when the prior probability distribution yields a posterior distribution for the parameters in the same family as the prior p.d.f. In this case the prior is called a natural conjugate prior for the likelihood function (Raiffa and Schlaifer, 1961). In general, it has been shown that exponential distributions are the only class of distributions that admit a natural conjugate prior, due to these having a fixed number of sufficient statistics that does not increase as the sample size _T_ increases (see e.g. Gelman et al., 2013). Because the data is incorporated into the posterior distribution only through the sufficient statistics, formulas for updating the prior into the posterior are in these cases conveniently simple. 

Prior distributions can be expressed in terms of coefficients, known as hyperparameters, whose functions are sufficient statistics for the model parameters. It is often useful to think of the hyperparameters of a conjugate prior distribution as corresponding to having observed a certain number of pseudo-observations with properties specified by the priors on the parameters. In general, for nearly all conjugate prior distributions, the hyperparameters can be interpreted in terms of ‘dummy’ or pseudo-observations. The basic idea is to add to the observed sample extra ‘data’ that express prior beliefs about the hyperparameters. The prior then takes the form of the likelihood function of these dummy observations. Hyperparameters can be either fixed using prior informa- 

13 

tion, or associated to hyperprior distributions that express beliefs about their values. A Bayesian model with more than one level of priors is called a hierarchical Bayes model. In this section we review some of the most commonly used priors for VARs with macroeconomic and financial variables, while we discuss the choice of the hyperpriors and hierarchical modelling in Section 4. 

### **3.1 Natural Conjugate Normal-Inverse Wishart Priors** 

The Normal-Inverse Wishart (NIW) conjugate priors, part of the exponential family, are commonly used prior distributions for ( _A,_ Σ) in VARs with Gaussian errors. These assume a multivariate normal distribution for the regression coefficients, and an Inverse Wishart specification for the covariance matrix of the error term, and can be written as 





where ( _<u>S, d, α,</u>_ <u>Ω) are the priors’ hyperparameters.</u> _<u>d</u>_ and _<u>S</u>_ denote, respectively, the degrees of freedom and the scale of the prior Inverse-Wishart distribution for the variancecovariance matrix of the residuals. _<u>α</u>_ is the prior mean of the VAR coefficients, and <u>Ω</u> acts as a prior on the variance-covariance matrix of the dummy regressors.<sup>13</sup> The posterior distribution can be analytically derived and is given by 





> 13The prior mean of the VAR coefficients is E[ _α_ ] = _<u>α,</u>_ for _<u>d</u> > n_ , while the variance is V _ar_ [ _α_ ] = <u>(</u> _<u>d</u> − n −_ 1)<sup>_−_1</sup> _<u>S</u> ⊗_ <u>Ω</u> _,_ for _<u>d</u> > n_ + 1. Setting _<u>d</u>_ = max _{n_ + 2 _, n_ + 2 _h − T }_ ensures that both the prior variances of _A_ and the posterior variances of the forecasts at _T_ + _h_ are defined. 

14 

where 



Comparing Eqs. (16) - (17) to Eqs. (19) - (20), it is evident that informative priors can be thought of as equivalent to having observed dummy observations ( _yd, xd_ ) of size _Td_ , such that 









This idea was first proposed for a classical estimator for stochastically restricted coefficients by Theil (1963). Once a set of pseudo-observations able to match the wished hyperparameters is found, the posterior can be equivalently estimated using the extended samples _y∗_ = [ _y_<sup>_′_</sup> _, yd_<sup>_′_]</sup><sup>_′_,</sup><sup>_x∗_= [</sup><sup>_x′, x′_</sup> _d_<sup>]</sup><sup>_′_ofsize</sup><sup>_T∗_=</sup><sup>_T_+</sup><sup>_Td_obtaining</sup> 





Indeed, it is easy to verify that the posterior moments obtained with the starred variables coincide with those in Eqs. (21) - (22). The posterior estimator efficiently combines sample and prior information using their precisions as weights in the spirit of the mixed estimation of Theil and Goldberger (1961). Posterior inference can be conducted via direct sampling. 

**Algorithm 1: Direct Monte Carlo Sampling from Posterior of VAR Para-** 

15 

#### **meters.** 

For _s_ = 1 _, . . . , nsim_ : 

1. Draw Σ<sup>(</sup><sup>_s_)</sup> from the Inverse-Wishart distribution Σ _|_ **y** _∼IW_ ( _S∗, T∗_ + _<u>d</u>_ <u>).</u> 

2. Draw _A_<sup>(</sup><sup>_s_)</sup> from the Normal distribution of _A_<sup>(</sup><sup>_s_)</sup> _|_ Σ<sup>(</sup><sup>_s_)</sup> _,_ **y** _∼N_ � _α∗,_ Σ<sup>(</sup><sup>_s_)</sup> _⊗_ ( _x_<sup>_′_</sup> _∗_<sup>_x∗_)</sup><sup>_−_1�</sup> . 

When it is not possible to sample directly from the posterior distribution, as in this case, Markov chain Monte Carlo (MCMC) algorithms are usually adopted (see e.g. Chib, 2001).<sup>14</sup> 

An important feature of the NIW priors in Eqs. (19) - (20) is the Kronecker factorisation that appears in the Gaussian prior for _α_ . As discussed in the previous section, because the same set of regressors appears in each equation, homoskedastic VARs can be written as SUR models. This symmetry across equations means that homoskedastic VAR models have a Kronecker factorisation in the likelihood, which in turn implies that estimation can be broken into _n_ separate least-squares calculations, each only of dimension _np_ + 1. The symmetry in the likelihood can be inherited by the posterior, if the prior adopted also features a Kronecker structure as in Eq. (20). This is a desirable property that guarantees tractability of the posterior p.d.f. and computational speed. However, such a specification can result in unappealing restrictions and may not fit the actual prior beliefs one has – see discussions in Kadiyala and Karlsson (1997), and Sims and Zha (1998). In fact, it forces symmetry across equations, because the coefficients of each equation have the same prior variance matrix (up to a scale factor given by the elements of Σ). There may be situations in which theory suggests ‘asymmetric restrictions’ may be desirable instead, e.g. money neutrality implies that the money supply 

> 14 The key idea of MCMC algorithms is to construct a Markov chain for _θ ≡_ ( _A,_ Σ) which has the posterior as its (unique) limiting stationary distribution, and such that random draws can be sampled from the transition kernel _p_ ( _θ_<sup>(</sup><sup>_s_+1)</sup> _|θ_<sup>(</sup><sup>_s_)</sup> ). Tierney (1994) and Geweke (2005) discuss the conditions for the convergence of the chain to the posterior distribution when starting from an arbitrary point in the parameter space. Typically, a large number of initial draws (known as burn-in sample) is discarded to avoid including portions of the chain which have not yet converged to the posterior. Also, even if convergent, the chain may move very slowly in the parameter space due to e.g. autocorrelation between the draws, and a very large number of draws may be needed. See also Karlsson (2013a) for a discussion on this point and on empirical diagnostic tests to assess the chain convergence. References include Geweke (1999); Chib and Greenberg (1995); Geweke and Whiteman (2006b). 

16 

does not Granger-cause real output.<sup>15</sup> Also, the Kronecker structure implies that prior beliefs must be correlated across the equations of the reduced form representation of the VAR, with a correlation structure that is proportional to that of the disturbances. 

### **3.2 Minnesota Prior** 

In macroeconomic and financial applications, the parameters of the NIW prior in Eq. Eqs. (19) - (20) are often chosen so that prior expectations and variances of _A_ coincide with the so-called ‘Minnesota’ prior, that was originally proposed in Litterman (1980, 1986).<sup>16</sup> The basic intuition behind this prior is that the behaviour of most macroeconomic variables is well approximated by a random walk with drift. Hence, it ‘centres’ the distribution of the coefficients in _A_ at a value that implies a random-walk behaviour for all the elements in _yt_ 



While not motivated by economic theory, these are computationally convenient priors, meant to capture commonly held beliefs about how economic time series behave. 

The Minnesota prior assumes the coefficients _A_ 1 _, . . . , Ap_ to be a priori independent and normally distributed, with the following moments 



In Eq. (33), ( _Aℓ_ ) _ij_ denotes the coefficient of variable _j_ in equation _i_ at lag _ℓ_ . _δi_ is 

> 15Such restrictions can be accommodated by replacing Eq. (19) with a truncated Normal distribution. In this case, however, posterior moments are not available analytically and must be evaluated numerically, with consequential complications and loss of efficiency with respect to the MCMC algorithm discussed above (see Hajivassiliou and Ruud, 1994; Kadiyala and Karlsson, 1997, for further details). 

> 16The original formulation of Litterman (1980)’s prior was of the form 



2 2 where <u>Γ</u> _≡ diag_ ([ _<u>γ</u>_ ~~1~~<sup>_, . . . , γ_</sup> _~~n~~_<sup>])isassumedtobefixed,known,anddiagonal.</sup> Highfield (1992) and Kadiyala and Karlsson (1997) observed that by modifying Litterman’s prior to make it symmetric across equations in the form of a NIW prior, the posterior p.d.f. was tractable. 

17 

usually set to 1 in accordance with Eq. (32).<sup>17</sup> The prior also assumes that lags of other variables are less informative than own lags, and that most recent lags of a variable tend to be more informative than more distant lags. This intuition is formalised with _f_ ( _ℓ_ ). A common choice for this function is a harmonic lag decay – i.e. _f_ ( _ℓ_ ) = _ℓ_<sup>_λ_2</sup> , a special case of which is _f_ ( _ℓ_ ) = _ℓ_ –, where the severity of the lag decay is regulated by the hyperparameter _λ_ 2. The factor Σ _ij/ωj_<sup>2accountsforthedifferentscalesofvariables</sup> _i_ and _j_ . The hyperparameters _ωj_<sup>2areoftenfixedusingsampleinformation,forexample</sup> from univariate regressions of each variable onto its own lags. 

Importantly, _λ_ 1 is a hyperparameter that controls the overall tightness of the random walk prior. If _λ_ 1 = 0 the prior information dominates, and the VAR reduces to a vector of univariate models. Conversely, as _λ_ 1 _→∞_ the prior becomes less informative, and the posterior mostly mirrors sample information. We discuss the choice of the free hyperparameters in Section 4. 

The Minnesota prior can be implemented using dummy observations. Priors on the _A_ coefficients are implemented via the following pseudo-observations 



where _Jp_ = _diag_ ([1<sup>_λ_2</sup> _,_ 2<sup>_λ_2</sup> _, . . . , p_<sup>_λ_2</sup> ]) with geometric lag decay.<sup>18</sup> To provide intuition on how the prior is implemented using artificial observations, we consider the simplified case of a _n_ = 2 _, p_ = 2 VAR for the pseudo-observations . The first _n_ rows of Eq. (34) impose priors on _A_ 1; that is, on the coefficients of the first lag. In the _n_ = 2 _, p_ = 2 case 

> 17The random-walk assumption is taken for convenience and can be modified to accommodate the characteristics of the series in _yt_ . For stationary series, or variables that have been transformed to achieve stationarity, Ba´nbura et al. (2010) centre the distribution around zero (i.e. _δi_ = 0). 

> 18Given the dummy observations in Eq. (34), the matrix Ωin Eq. (19) is diagonal and of the form 



18 

one obtains, 



that implies, for example, the following equations for the elements (1 _,_ 1) and (1 _,_ 2) of _A_ 1 



Similar restrictions are obtained for the elements the elements (2 _,_ 1) and (2 _,_ 2) of _A_ 1. The following ( _n −_ 1) _p_ rows in Eq. (34) implement priors on the coefficients of the other lags. In fact, we readily obtain 



which for example implies the following restriction for the element (1 _,_ 1) of _A_ 2 



Similar restrictions obtain for the other elements of _A_ 2. Priors beliefs on the residual covariance matrix Σ can instead implemented by the following block of dummies 



In the _n_ = 2 _, p_ = 2 case, they correspond to appending to the VAR equations _λ_ 3 

19 

replications of 



_λ_ 3 is the hyperparameter that determines the tightness of the prior on Σ. To understand how this works, it is sufficient to consider that with _λ_ 3 artificial observations _zi ∼ λ_ 3 _N_ (0 _, σz_<sup>2),anestimatorforthecovarianceisgivenby</sup><sup>_λ−_</sup> 3<sup>1</sup> � _i_ =1<sup>_z_</sup> _i_<sup>2.</sup> 

Finally, uninformative priors for the intercept are often implemented with the following set of pseudo-observations 



where _ϵ_ is a hyperparameter usually set to a very small number.<sup>19</sup> 

### **3.3 Priors for VAR with Unit Roots and Trends** 

Sims (1996, 2000) observed that flat-prior VARs, or more generally estimation methods that condition on initial values, tend to attribute an implausibly large share of – the variation in observed time series to deterministic and hence entirely predictable – components. The issue stems from the fact that ML and OLS estimators that condition on the initial observations and treat them as non-stochastic do not apply any penalisation to parameters values that imply that these observations are very distant from the variables’ steady state (or their trend if non-stationary). As a consequence, complex transient dynamics from the initial conditions to the steady state are treated as plausible, and can explain an ‘implausibly’ large share of the low-frequency variation of the data. This typically translates into poor out-of-sample forecasts. To understand the intuition, consider the univariate model 



> 19 **??** propose a set of artificial observations to account for seasonal patterns and potentially other peaks in the spectral densities. 

20 

Iterating Eq. (40) backward yields 



which, if _|a| <_ 1, reduces to 



The first term in square brackets in Eq. (41) is the deterministic component: the evolution of _yt_ from the initial conditions _y_ 0, absent any shocks. The second term instead captures the stochastic evolution of _yt_ due to the shocks realised between [0 _, t−_ 1]. _c/_ (1 _− a_ ) in Eq. (42) is the unconditional mean of _yt_ . If _yt_ is close to non-stationary – i.e. _a ≃_ 1 –, the MLE estimator of the unconditional mean of _yt_ may be very far from _y_ 0, and the ‘reversion to the mean’ from _y_ 0 is then used to fit the data (see Eq. 42). 

One way to deal with this issue is to use the unconditional likelihood, by explicitly incorporating the density of the initial observations in the inference. However, because most macroeconomic time series are effectively nonstationary, it is not obvious how the density of the initial observations should be specified.<sup>20</sup> Another approach, following Sims and Zha (1998); Sims (2000), is to instead specify priors that downplay the importance of the initial observations, and hence reduce the explanatory power of the deterministic component. 

These types of priors, implemented through artificial observations, aim to reduce the importance that the deterministic component has in explaining a large share of the in-sample variation of the data, eventually improving forecasting performances out-ofsample (see Sims, 1996; Sims and Zha, 1998, for a richer discussion on this point).<sup>21</sup> 

> 20This approach requires the use of iterative nonlinear optimisation methods. The main issue with this approach is that nonstationary models have no unconditional – viz. ergodic – distribution of the initial conditions. Also, while near-nonstationary models may have an ergodic distribution, the time required to arrive at the ergodic distribution from arbitrary initial conditions may be very long. For this reason, using such a method requires strong beliefs about the stationarity of the model, which is rarely the case in macroeconomics, and imposing the ergodic distribution on the first _p_ observations may be unreasonable (see Sims, 2005a). 

> 21The treatment of unit root in Bayesian and frequentist inference has been hotly debated. Among 

21 

The ‘co-persistence’ (or ‘one-unit-root’ or ‘dummy initial observation’) prior (Sims, 1993) reflects the belief that when all lagged _yt_ ’s are at some level _y_ ¯0, _yt_ tends to persist at that level. It is implemented using the following artificial observation 



where _y_ ¯0 _,i, i_ = 1 _, . . . , n_ are the average of the initial values of each variable, and usually set to be equal to the average of the first _p_ observations in the sample. Writing down the implied system of equations _yd_<sup>(4)</sup> = _Ax_<sup>(4)</sup> _d_ + _u_<sup>(4)</sup> _d_ one obtains the following stochastic restriction on the VAR coefficients 



where I _n − A_ (1) = (I _n − A_ 1 _− . . . − Ap_ ). The hyperparameter _λ_ 4 controls the tightness of this stochastic constraint. The prior is uninformative for _λ_ 4 _→∞_ . Conversely, as _λ_ 4 _→_ 0 the model tends to a form where either there is at least one explosive common unit root and the constant _c_ is equal to zero (¯ _y_ 0 is the eigenvector of the unit root), or the VAR is stationary, _c_ is different from zero, and the initial conditions are close to the implied unconditional mean (¯ _y_ 0 = [I _n − A_ (1)]<sup>_−_1</sup> _c_ ). In the stationary form, this prior does not rule out cointegrated models. This prior induces prior correlation among all the VAR coefficients in each equation, including the constant.<sup>22</sup> 

The ‘sums-of-coefficients’ (or ‘no-cointegration’) prior (Doan et al., 1984), captures the belief that when the average lagged values of a variable _yj,t_ is at some level _y_ ¯0 _,j_ , ¯ then _y_ 0 _,j_ is likely to be a good forecast of _yj,t_ . It also implies that knowing the average 

others, important contributions are Sims (1988, 1991), Sims and Uhlig (1991), Koop and Steel (1991), Phillips (1991a,b), Uhlig (1994a,b), M¨uller and Elliott (2003); Jaroci´nski and Marcet (2011, 2014). The Journal of Applied Econometrics October/December 1991 Volume 6, Issue 4 has been entirely dedicated to this debate. 

> 22To put a heavier weight on the presence of a unit root, one could add to the observation in Eq. (43) an additional artificial observation that enforces the belief that _c_ = 0. Alternatively, one could modify Eq. (43) to have a zero in place of _λ_<sup>_−_</sup> 4<sup>1</sup> as the observation corresponding to the intercept. In this case, the prior gives no plausibility to stationary models and, if used in isolation, allows for at least a single unit root without any restriction on _c_ . Hence, despite the presence of a unit root, it may not necessarily reduce the importance of the deterministic component (see Sims, 2005a). 

22 

of lagged values of variable _j_ does not help in predicting a variable _i_ = _j_ . This prior is implemented using _n_ artificial observations, one for each variable in _yt_ 



The prior implied by these dummy observations is centred at 1 for the sum of coefficients on own lags for each variable, and at 0 for the sum of coefficients on other variables’ lags. It also introduces correlation among the coefficients of each variable in each equation. In fact, it is easy to show that equation by equation this priors implies the stochastic constraint 



where ( _Aℓ_ ) _jj_ denotes the coefficient of variable _j_ in equation _j_ at lag _ℓ_ . The hyperparameter _λ_ 5 controls the variance of these prior beliefs. As _λ_ 5 _→∞_ the prior becomes uninformative, while _λ_ 5 _→_ 0 implies that each variable is an independent unit-root process, and there are no co-integration relationships.<sup>23</sup> 

The Bayesian analysis of cointegrated VARs is an active area of research, (a detailed survey is in Koop et al. 2006).<sup>24</sup> Giannone et al. (2016) elicit theory-based priors for the long run of persistent variables which shrink towards a random walk those linear combination of variables that are likely to have a unit root. Conversely, combinations which are likely to be stationary (i.e. cointegrating relationships among variables) are shrunk towards stationary processes. Operationally, this is achieved by rewriting the 

> 23The sums-of-coefficients observations of Eq. (45) do not imply any restriction on the vector of intercepts _c_ , since the artificial observations loading on the constant are set to zero. Therefore, this prior allows for a non-zero constant, and hence for a linearly trending drift. To assign smaller probability to versions of the model in which deterministic transient components are much more important than the error term in explaining the series variance, one has to add to Eq. (45) artificial observations that favour _c_ = 0 (see Sims, 2005a). 

> 24Among many others, contributions to the treatment of cointegration in Bayesian VARs are in Kleibergen and van Dijk (1994), Geweke (1996), Villani (2001), Kleibergen and Paap (2002), Strachan and Inder (2004), Koop et al. (2011), Jochmann and Koop (2015). 

23 

VAR in Eq. (1) as 



where Π = _A_ 1 + _. . ._ + _Ap −_ I _n_ , _Pj_ = _−_ ( _Aj_ +1 + _. . ._ + _Ap_ ), and _F_ is any invertible _n_ - dimensional matrix. The problem is then specified as setting a prior for Π<sup>�</sup> _≡_ Π _F_<sup>_−_1</sup> , conditional on a specific choice of _F_ . _F_ defines the relevant linear combinations of the variables in _yt_ which macroeconomic theory suggest to be a priori stationary or otherwise. 

Another alternative is in Villani (2009). Here the VAR is written as 



where _ρ_ 0 and _ρ_ 1 are _n×_ 1 vectors. The first term, _ρ_ 0 + _ρ_ 1 _t_ , captures a linear deterministic trend of _yt_ , whereas the law of motion of _y_ ˜ _t_ captures stochastic fluctuations around the deterministic trend, which can be either stationary or non-stationary. This alternative specification allows to separate beliefs about the deterministic trend component from beliefs about the persistence of fluctuations around this trend. Let _A_ = [ _A_ 1 _, . . . , Ap_ ]<sup>_′_</sup> and _ρ_ = [ _ρ_<sup>_′_</sup> 0<sup>_, ρ_</sup> 1<sup>_′_]</sup><sup>_′_.It can be shown that if the prior distribution of</sup><sup>_ρ_conditional on</sup><sup>_A_and Σ is</sup> Normal, the (conditional) posterior distribution of _ρ_ is also Normal (see also Del Negro and Schorfheide, 2011, for details). Hence, posterior inference can be implemented via Gibbs sampling. 

### **3.4 Priors from Structural Models** 

DeJong et al. (1993), Ingram and Whiteman (1994), Del Negro and Schorfheide (2004) have proposed the use of priors for VARs that are derived from Dynamic Stochastic General Equilibrium (DSGE) models. This approach bridges VARs and DSGEs by constructing families of prior distributions informed by the restrictions that a DSGEmodel implies on the VAR coefficients. This modelling approach is sometimes referred 

24 

to as DSGE-VAR. Ingram and Whiteman (1994) derive prior information from the basic stochastic growth model of King et al. (1988) and report that a BVAR based on the Real Business Cycle model prior outperforms a BVAR with a Litterman prior in forecasting real economic activity. Del Negro and Schorfheide (2004) extend and generalise this approach, and show how to conduct policy simulations within this framework. 

Schematically, the exercises can be thought of as follows. First, time-series are simulated form a DSGE model. Second, a VAR is estimated from these simulated data. Population moments of the simulated data computed from the DSGE model solution are considered in place of sample moments. Since the DSGE model depends on unknown structural parameters, hierarchical prior modelling is adopted by specifying a distribution on the DSGE model parameters. A tightness parameter controls the weight of the DSGE model prior relative to the weight of the actual sample. Finally, Markov Chain Monte Carlo methods are used to generate draws from the joint posterior distribution of the VAR and DSGE model parameters. 

### **3.5 Priors for Model Selection** 

It is standard practice in VAR models to pre-select the relevant variables to be included in the system (and with how many lags). This procedure may be thought of as having dogmatic priors about which variables have non-zero coefficients in the system. The challenge is in selecting among an expansive set of potential models. Indeed, for a VAR with _n_ endogenous variables, _q_ additional potentially exogenous variables including a constant, and _p_ lags, there are 2<sup>(</sup><sup>_q_+</sup><sup>_pn_)</sup><sup>_n_+</sup><sup>_n_(</sup><sup>_n−_1)</sup><sup>_/_2</sup> possible models. 

Jaroci´nski and Ma´ckowiak (2017) propose to select the variables to be included in the system by systematically assessing the posterior probability of ‘Granger causal priority’ (Sims, 2010a) in a BVAR with conjugate priors. Granger causal priority answers questions of the form “Is variable z relevant for variable x, after controlling for other variables in the system?” The authors provide a closed form expression for the posterior probability of Granger causal priority, and suggest that variables associated with high Granger causal priority probabilities can be omitted from a VAR with the variables of 

25 

interest. 

Alternatively, one can adopt priors that support model selection and enforce sparsity. A variety of techniques, including double exponential (Laplace) prior, spike-and-slab prior, etc., have been adopted to handle this issue. Some recent theoretical and empirical contributions on this topic are in Mitchell and Beauchamp (1988), George et al. (2008), Korobilis (2013), Bhattacharya et al. (2015a), Griffin and Brown (2010, 2017), Giannone et al. (2017), Huber and Feldkircher (2017). 

## **4 Hyperpriors and Hierarchical Modelling** 

As seen in the previous section, the informativeness of prior beliefs on the VAR parameters often depends on a set of free hyperparameters. Let _λ ≡_ [ _λ_ 1 _, λ_ 2 _, . . ._ ] denote the vector collecting all the hyperparameters not fixed using (pre)sample information, and _θ_ denote all the VAR parameters, i.e. _A_ and Σ. The prior distribution of _θ_ is thus effectively _pλ_ ( _θ_ ). Choosing a value for _λ_ alters the tightness of the prior distribution, and hence determines how strictly the prior is enforced on the data. 

In order to set the informativeness of the prior distribution of the VAR coefficients, the literature has initially used mostly heuristic methodologies. Litterman (1980) and Doan et al. (1984), for example, choose a value for the hyperparameters that maximises the out-of-sample forecasting performance over a pre-sample. Conversely, Ba´nbura et al. (2010) propose to choose the shrinkage parameters that yield a desired in-sample fit, in order to control for overfitting. Subsequent studies have then either used these as ‘default’ values, or adopted either one of these criteria. Robertson and Tallman (1999); Wright (2009); Giannone et al. (2014) opt for the first, while e.g. Giannone et al. (2008); Bloor and Matheson (2011); Carriero et al. (2009); Koop (2013) follow Ba´nbura et al. (2010). 

In VARs, Giannone et al. (2015) observe that, from a purely Bayesian perspective, choosing _λ_ is conceptually identical to conducting inference on any other unknown parameter of the model. Specifically, the model is interpreted as a hierarchical one (Berger, 

26 

1985; Koop, 2003) and _λ_ can be chosen as the maximiser of 



This method is also known in the literature as the Maximum Likelihood Type II (MLII) approach to prior selection (Berger, 1985; Canova, 2007). In Eq. (49), _p_ ( _λ|_ **y** ) is the posterior distribution of _λ_ conditional on the data, and _p_ ( _λ_ ) denotes a prior probability density specified on the hyperparameters themselves, and also known as the hyperprior distribution. In such hierarchical model, the prior distribution for the VAR coefficients is treated as a conditional prior, that is _pλ_ ( _θ_ ) is replaced by _p_ ( _θ|λ_ ). In the case of a NIW family of distributions, the prior structure becomes _p_ ( _α|_ Σ _, λ_ ) _p_ (Σ _|λ_ ) _p_ ( _λ_ ). _p_ ( **y** _|λ, y_ 1 _−p_ :0) is the marginal likelihood (ML), and is obtained as the density of the data as a function of _λ_ , after integrating out all the VAR parameters. Conveniently, with conjugate priors the ML is available in closed form. 

Conversely, the joint posterior of _α_ , Σ and _λ_ is not available in closed form. However, with NIW priors for _θ_ , Giannone et al. (2015) set up the following Metropolis-Hasting sampler for the joint distribution 

#### **Algorithm 2: MCMC Sampler for a VAR with Hierarchical Prior.** For _s_ = 1 _, . . . , nsim_ : 

1. Draw a candidate vector _λ_<sup>_∗_</sup> from the random walk distribution _λ_<sup>_∗_</sup> _∼N_ ( _λ_<sup>_s−_1</sup> _, κH_<sup>_−_1</sup> ), where _H_ is the Hessian of the negative of the log-posterior at the peak for _λ_ , and _κ_ is a tuning constant. Choose 



2. Draw Σ<sup>(</sup><sup>_s_)</sup> form the full conditional posterior Σ _|_ **y** _, λ_<sup>(</sup><sup>_s_)</sup> in Eq. (21). 

3. Draw _A_<sup>(</sup><sup>_s_)</sup> from the full conditional posterior _A_<sup>(</sup><sup>_s_)</sup> _|_ **y** _,_ Σ<sup>(</sup><sup>_s_)</sup> _, λ_<sup>(</sup><sup>_s_)</sup> in Eq. (22). 

27 

In a similar fashion, Belmonte et al. (2014) apply a hierarchical structure to timevarying parameters (TVP) models and specify priors for Bayesian Lasso shrinkage parameters to determine whether coefficients in a forecasting model for inflation are zero, constant, or time-varying in a data driven way. 

Carriero et al. (2015a) evaluate the forecasting performance of BVARs where tightness hyperparameters are chosen as the maximisers of Eq. (49) or rather set to default values and find that the former route yields modest but statistically significant gains in forecasting accuracy particularly at short horizons (see Section 5 for additional discussions). 

## **5 Forecasting with BVARs** 

Reduced form Bayesian Vector Autoregressions usually outperform VARs estimated with frequentist techniques (or flat priors). Using the frequentist terminology, reasonably specified priors reduce estimated parameters variance and hence improve forecast accuracy, at the cost of the introduction of relatively small biases. From a more Bayesian – perspective, the prior information that may not be apparent in short samples as for example the long-run properties of economic variables captured by the Minnesota priors – helps in forming sharper posterior distributions for the VAR parameters, conditional on an observed sample (see e.g. Todd, 1984, for an early treatment of forecasting with BVARs). 

### **5.1 Bayesian Forecasting** 

The fundamental object in Bayesian forecasting is the posterior predictive density.<sup>25</sup> That is, the distribution of future data points _yT_ +1: _T_ + _H_ = [ _yT_<sup>_′_</sup> +1<sup>_, . . . , y_</sup> _T_<sup>_′_</sup> + _H_<sup>]</sup><sup>_′_, conditional</sup> on past data _y_ 1 _−p_ : _T_ . Choosing a particular forecast _F_ – e.g. the mode or median of the predictive distribution, alongside appropriate probability intervals –, is essentially a decision problem, given a specified loss function _L_ ( _·_ ). The Bayesian decision corresponds 

> 25The exposition in this section follows Karlsson (2013a). See also Geweke and Whiteman (2006b). 

28 

to choosing the forecast that minimises the expected loss, conditional on past data 



For a given loss function, the solution to the minimisation problem is a function of the data, i.e. _F_ ( _y_ 1 _−p_ : _T_ ). For example, with quadratic loss function _L_ ( _F, yT_ +1: _T_ + _H|y_ 1 _−p_ : _T_ ) = ( _F − yT_ +1: _T_ + _H_ )<sup>_′_</sup> ( _F − yT_ +1: _T_ + _H_ ), the solution is the conditional expectation _F_ ( _y_ 1 _−p_ : _T_ ) = E[ _yT_ +1: _T_ + _H|y_ 1 _−p_ : _T_ ]. The predictive density is given by 



where _θ_ is the vector collecting all the VAR parameters, i.e. _A_ and Σ, _p_ ( _θ|y_ 1 _−p_ : _T_ ) is the posterior distribution of the parameters, and _p_ ( _yT_ +1: _T_ + _H|y_ 1 _−p_ : _T , θ_ ) is the likelihood of future data. Eq. (51) highlights how Bayesian forecasts account for both the uncertainty related to future events via _p_ ( _yT_ +1: _T_ + _H|y_ 1 _−p_ : _T , θ_ ), and that related to parameters values via _p_ ( _θ|y_ 1 _−p_ : _T_ ). 

The posterior predictive density for _h >_ 1 is not given by any standard density function. However, if it is possible to sample directly from the posterior probability for the parameters, Eq. (51) provides an easy way to generate draws from this predictive density. 

#### **Algorithm 3: Sampling from the Posterior Predictive Density.** For _s_ = 1 _, . . . , nsim_ : 

1. Draw _θ_<sup>(</sup><sup>_s_)</sup> from the posterior _p_ ( _θ|y_ 1 _−p_ : _T_ ). 

2. Generate _u_<sup>(</sup> _T_<sup>_s_</sup> +1<sup>)</sup><sup>_, . . . , u_</sup> _T_<sup>(</sup><sup>_s_</sup> +<sup>)</sup> _H_<sup>fromthedistributionoftheerrorsandcalculaterecurs-</sup> ively _y_ ˜ _T_<sup>(</sup><sup>_s_</sup> +1<sup>)</sup><sup>_, . . . ,_˜</sup><sup>_y_</sup> _T_<sup>(</sup><sup>_s_</sup> +<sup>)</sup> _H_<sup>fromtheVARequationswithparameters</sup><sup>_A_(</sup><sup>_s_).</sup> 

The set _y_ ˜ _T_<sup>(</sup><sup>_s_</sup> +1<sup>)</sup><sup>_, . . . ,_˜</sup><sup>_y_</sup> _T_<sup>(</sup><sup>_s_</sup> +<sup>)</sup> _H nsim_ � � _s_ =1<sup>is a sample of independent draws from the joint predictive</sup> distribution. 

Kadiyala and Karlsson (1993) analyse the forecasting performance of different priors and find that those that induce correlation among the VAR coefficients, e.g. the sums- 

29 

of-coefficient priors (Doan et al., 1984) and the co-persistence prior (Sims, 1993), tend to do better. 

Carriero et al. (2015a) conduct an extensive assessment of Bayesian VARs under different specifications. Starting from a benchmark VAR in levels and with NIW, sumsof-coefficients, and co-persistence priors, they evaluate (1) the effects of the optimal choice of the tightness hyperparameters, (2) of the lag length, (3) of the relative merits of modelling in levels or growth rates, (4) of direct, iterated and pseudo-iterated _h_ -stepahead forecasts, and (5) and the treatment of the error variance Σ and (6) of crossvariable shrinkage _f_ ( _ℓ_ ). They find that simpler specifications tend to be very effective and recommend the use of differenced data, long lag lengths, a Normal-Inverse Wishart prior, and forecasts based on the posterior means of the parameters.<sup>26</sup> 

### **5.2 Bayesian Model Averaging and Prediction Pools** 

Bayesian analysis offers a straightforward way to deal with model uncertainty. Consider for instance the two competing models _M_ 1 and _M_ 2 with likelihood _p_ ( **y** _|θ_ 1 _, M_ 1 _, y_ 1 _−p_ :0) and _p_ ( **y** _|θ_ 2 _, M_ 2 _, y_ 1 _−p_ :0) and prior probabilities _p_ ( _θ_ 1 _|M_ 1) and _p_ ( _θ_ 2 _|M_ 2) respectively. Bayesian Model Averaging (BMA) obtains the marginalised (with respect to the models) predictive distribution as 



where _p_ ( _Mj_ ) is the prior probability assigned to model _Mj_ , and _p_ ( _yT_ +1: _T_ + _H|_ **y** _, Mj_ ) is the model’s marginal likelihood. Eq. (52) can be extended to allow for _M_ different models. This can be seen as a generalisation of the predictive distribution in Eq. (51) where instead of conditioning on a single model, _M_ different models are considered. BMA was introduced in economic forecasting by the seminal work of Geweke (1999) and its applications in the context of forecast combinations and pooling have been numerous. 

Earlier reviews of BMA and forecast combinations are in Geweke and Whiteman (2006b) 

> 26Carriero et al. (2015a) find that overall the differences between the iterated and direct forecasts are small, but there are large gains from the direct forecast for some of the variables. This is presumably because the direct forecast is more robust to misspecification. 

30 

and Timmermann (2006). 

Geweke and Amisano (2011, 2012) proposed Linear Optimal Prediction Pools which dispense from the implicit assumption of one model in _M_ 1 _, . . . , MM_ being true. One important aspect of these pools is that prediction weights based on log scoring rules will not converge asymptotically to either zero or 1, as is instead the case for posterior probabilities in BMA.<sup>27</sup> Del Negro et al. (2016) design Dynamic Prediction Pools as a method to combine predictive densities to estimate time-varying model weights in linear prediction pools.<sup>28</sup> Billio et al. (2013) propose a general approach to combine predictive densities using time-varying weights that nests static linear pools, the Markovswitching weight specification of Waggoner and Zha (2012), and the dynamic linear pool in Del Negro et al. (2016). 

Amisano and Geweke (2017) suggest improvements to BMA which involve equal prior weights but condition on full Bayesian predictive densities rather than on the posterior modes for the estimated parameters. A generalisation of BMA is the Dynamic Model Averaging/Selection (DMA/DMS) developed in Raftery et al. (2010), which allows for the forecasting model to change over time, and for the coefficients in each of the models considered to also be time dependent. Hwang (2017) uses DMA to introduce forecasting using specification-switching VARs. Koop and Korobilis (2012) use the same method to forecast inflation, and show it is superior to using a fixed model with time varying coefficients. Aastveit et al. (2017) introduce combined density nowcasting with timevarying model weights assigned each period in a real-time forecasting environment. 

> 27The log score of model _Mj_ at time _t_ is 



> _LS_ ( _y_ 1 _−p_ : _T , Mj_ ) is a measure of _Mj_ ’s forecasting accuracy. If _Mj_ is subjective Bayesian (as opposed to e.g. based on personal judgement) then _LS_ ( _y_ 1 _−p_ : _T , Mj_ ) is the model’s marginal likelihood in the sample _y_ 1 _−p_ : _T_ (see e.g. Geweke and Amisano, 2012). 

> 28Other relevant contributions on density forecast combination are Waggoner and Zha (2012); Geweke and Amisano (2011); Hall and Mitchell (2007). 

31 

## **6 Conditional Forecasts and Scenario Analysis** 

Forecasts that condition on a specific path for one of the variables, such as e.g. a preferred path for the policy interest rate, are of particular interest to central banks. Early treatment of such forecasts, also referred to as scenario analysis, is in Doan et al. (1984), who note that a conditional forecast is equivalent to imposing restrictions on the disturbances _uT_ +1 _, . . . , ut_ + _H_ . Waggoner and Zha (2012) suggest a way to compute conditional forecasts which does not condition on specific parameters values (for example the posterior means) and produces minimum squared forecast errors conditional on the restrictions. Moreover, it yields posterior distributions for the parameters which are consistent with the constrained paths. Let 



denote the desired restrictions on the future path of some of the variables in _yt_ . These can be rewritten as 

where 



and _Cj_ are the coefficients of the MA representation with 



32 

Rearranging Eq. (54) as 



defining _G ≡ RC_<sup>_′_</sup> and _g ≡ r − R_ E( _yT_ +1: _T_ + _H|y_ 1 _−p_ : _T , θ_ ), and noting that _uT_ +1: _T_ + _H ∼ N_ (0 _,_ I _H ⊗_ Σ), one obtains the conditional distribution of _uT_ +1: _T_ + _H_ as 



which can be used to draw from the predictive distribution. In order to ensure consistency of the posterior distribution with the restriction in Eq. (57), Waggoner and Zha (2012) suggest treating _yT_ +1: _T_ + _H_ as latent variables and simulating the joint posterior of the parameters and the future observations using the following MCMC sampler. 

**Algorithm 4: MCMC Sampler for VAR with restrictions on** _yT_ +1: _T_ + _H_ **.** Given restrictions as in Eq. (57), select starting values for _A_<sup>(0)</sup> and Σ<sup>(0)</sup> using e.g. simulation on historical data. For _s_ = 1 _, . . . , nsim_ : 

1. Draw _uT_ +1: _T_ + _H_ from the distribution in Eq. (58) and recursively calculate 



2. Augment _y_ 1 _−p_ : _T_ with _yT_<sup>(</sup><sup>_s_</sup> +1:<sup>)</sup> _T_ + _h_<sup>anddraw</sup><sup>_A_(</sup><sup>_s_)andΣ(</sup><sup>_s_)fromthefullconditional</sup> posteriors 



using an appropriate sampling given the chosen VAR specification and priors. 



33 

Jaroci´nski (2010) suggests an efficient way to sample _uT_ +1: _T_ + _H_ that reduces the computational burden of the algorithm discussed above. An extension to this method is in Andersson et al. (2010), who restrict the forecasts _yT_ +1: _T_ + _H_ to be in a specified region S _∈_ R _nH_ . This is a case of ‘soft’ restrictions, as opposed to those in Eq. (57). Robertson et al. (2005) follow a different approach and propose exponential tilting as a way to enforce moment conditions on the path of future _yt_ . This is the approach also implemented in Cogley et al. (2005). These methods are typically used in conjunction with small VARs, and become quickly computationally cumbersome as the system’s dimension increases. 

Ba´nbura et al. (2015) propose instead a Kalman Filter-based algorithm to produce conditional forecasts in large systems which admit a state-space representation such as large Bayesian VARs and Factor Models. Intuitively, this method improves on computational efficiency due to the recursive nature of filtering techniques which allow to tackle the problem period by period. 

Antolin-Diaz et al. (2018) propose a method to conduct ‘structural scenario analysis’ that can be supported by economic interpretation by choosing which structural shock is responsible for the conditioning path. 

## **7 Structural VARs** 

Reduced form VARs can capture the autocovariance properties of multiple time-series. However, their ‘structural interpretation’ as the data generating process of the observed data, and of their one-step-ahead forecast errors in terms of economically meaningful shocks, requires additional identifying restrictions. 

A VAR in structural form (SVAR) can be written as 



where _B_ 0 is a matrix of contemporaneous (causal) relationships among the variables, and _et_ is a vector of structural shocks that are mutually uncorrelated and have an economic 

34 

interpretation. All structural shocks are generally assumed to be of unitary variance. This does not imply a loss of generality, however, since the diagonal elements of _B_ 0 are unrestricted. In the structural representation, the coefficients have a direct behavioural interpretation, and it is possible to provide a causal assessment of the effects of economic – shocks on variables e.g. the effect of a monetary policy shock onto prices and output. Premultiplying the SVAR in Eq. (59) by _B_ 0<sup>_−_1</sup> yields its reduced-form representation, i.e. the VAR in Eq. (1). Comparing the two representations one obtains that _Ai_ = _B_ 0<sup>_−_1</sup><sup>_Bi_,</sup> _i_ = 1 _, . . . , p_ , and _ut_ = _B_ 0<sup>_−_1</sup><sup>_et_.Thevarianceofthereducedformforecasterrors,</sup><sup>_ut_is</sup> 



Since Σ is symmetric, it has only _n_ ( _n_ + 1) _/_ 2 independent parameters. This implies that the data can provide information to uniquely identify only _n_ ( _n_ + 1) _/_ 2 out of the _n_<sup>2</sup> parameters in _B_ 0. In fact, given a positive definite matrix Σ, it is possible to write _B_ 0 as the product of the unique lower triangular Cholesky factor of Σ (Σ = Σ _Chol_ Σ<sup>_′_</sup> _Chol_<sup>)</sup> times an orthogonal matrix _Q_ 



From this decomposition is clear that while Σ _Chol_ is uniquely determined for a given Σ, the _n_ ( _n −_ 1) _/_ 2 unrestricted parameters span the space of the _O_ ( _n_ ) group of _n × n_ orthogonal matrices. The central question in structural identification is how to recover the elements of _B_ 0 given the variance-covariance matrix of the one-step-ahead forecast errors, Σ. That is, how to choose _Q_ out of the many possible _n_ -dimensional orthogonal matrices.<sup>29</sup> 

From a Bayesian perspective, the issue is that since _yt_ depends only on Σ and not on its specific factorisation, the conditional distribution of the parameter _Q_ does not get 

> 29It is assumed that the information in the history of _yt_ is sufficient to recover the structural shocks _et_ , i.e., that it is possible to write the structural shocks as a linear combination of the reduced form innovations _ut_ . In this case, it is said that the shocks are fundamental for _yt_ . Departures from this case are discussed in Section 8. Relevant references are provided therein. 

35 

updated by the information provided in the data, i.e. 



For some regions of the parameter space, posterior inference will be determined purely by prior beliefs even if the sample size is infinite, since the data are uninformative. This is a standard property of Bayesian inference in partially identified models, as discussed for example in Kadane (1975), Poirier (1998), and Moon and Schorfheide (2012). 

Much of ingenuity and creativity in the SVAR literature has been devoted to provide – – arguments i.e. ‘identification schemes’ about the appropriate choice of _p_ ( _Q|A,_ Σ).<sup>30</sup> These arguments translate into what can be viewed as Bayesian inference with dogmatic – – prior beliefs i.e. distributions with singularities about the conditional distribution of _Q_ , given the reduced form parameters. For example, the commonly applied recursive identification amounts, from a Bayesian perspective, to assuming with dogmatic certainty that all of the upper diagonal elements of _B_ 0 are zero, while we do not have any information on the other values of _B_ 0. Equivalently, it assumes with certainty that _Q_ = I _n_ . Similarly, other commonly used identifications – e.g. long-run, medium-run, – sign restrictions, etc. can be expressed in terms of probabilistic a priori statements about the parameters in _B_ 0. 

Once a _B_ 0 matrix is selected, dynamic causal effects of the identified structural shocks on the variables in _yt_ are usually summarised by the structural impulse response functions (IRFs). In a VAR( _p_ ), they can be recursively calculated as 



where 



Θ0 = I _n_ , and _Aτ_ are the reduced form autoregressive coefficients of Eq. (1) with 

> 30A survey of the identification schemes proposed in the literature goes beyond the scope of this article. A recent textbook treatment on the subject is in Kilian and L¨utkepohl (2017). 

36 

_Aτ_ = 0 for _τ > p_ . The ( _i, j_ ) element of _IRFh_ denotes the response of variable _i_ to shock _j_ at horizon _h_ . Uncertainty about dynamic responses to identified structural shocks is typically reported in the Bayesian literature as point-wise coverage sets around – the posterior mean or median IRFs, at each horizon i.e. as the appropriate quantiles of the IRFs posterior distribution. For example, 68% coverage intervals are shown as three lines plotting the posterior IRF mean, and two lines representing 16th and 84th percentiles. Such credible sets usually need to be interpreted as point-wise, i.e. as credible sets for the response of a specific variable, to a specific shock, at a given horizon. However, point-wise bands effectively ignore the existing correlation between responses at different horizons. To account for the time (horizon) dependence, Sims and Zha (1999) suggest to use the first principal components of the covariance matrix of the IRFs. 

Sims and Zha (1998) discuss a very general framework for Bayesian inference on the structural representation in Eq. (59). Rewrite the SVAR as 



where the _T × n_ matrices _y_ and _e_ and the _T × k_ matrix _x_ are defined as 



and _B_ = [ _B_ 1 _, . . . , Bp, Bc_ ]. The likelihood can be written as 



where _|B_ 0 _|_ is the determinant of _B_ 0 (and the Jacobian of the transformation of _e_ in _y_ ). Conditional on _B_ 0, the likelihood function is a normal distribution in _B_ . Define _β ≡ vec_ ( _B_ ) and _β_ 0 _≡ vec_ ( _B_ 0). A prior for the SVAR coefficients can be conveniently 

37 

factorised as 



where _p_ ( _β_ 0) is the marginal distribution for _β_ 0, and can include singularities generated by e.g. zero restrictions. The (conditional) prior for _β_ can be chosen to be a normal p.d.f.<sup>31</sup> 



The posterior distribution of _β_ is hence of the standard form 



where the posterior moments are updated as in the standard VAR with Normal-Inverse Wishart priors (see e.g. Kadiyala and Karlsson, 1997). The posterior for _β_ 0 will depend on the assumed prior.<sup>32</sup> 

Baumeister and Hamilton (2015) apply a streamlined version of this framework to provide analytical characterisation of the informative prior distributions for impulseresponse functions that are implicit in a commonly used algorithm for sign restrictions. Sign restrictions are a popular identification scheme, pioneered in a Bayesian framework by Canova and De Nicolo (2002) and Uhlig (2005). The scheme selects sets of models whose _B_ 0 comply with restrictions on the sign of the responses of variables of interests over a given horizon. Bayesian SVARs with sign restrictions are typically estimated using algorithms such as in Rubio-Ram´ırez et al. (2010), where a uniform (or Haar) prior is assumed for the orthogonal matrix. Operationally, a _n × n_ matrix _X_ of independent _N_ (0 _,_ 1) values is generated, and decomposed using a _QR_ decomposition where _Q_ is the orthogonal factor and _R_ is upper triangular. The orthogonal matrix is used as candidate rotation _Q_ and the signs of the responses of variables at the horizons of interest are assessed against the desired sign restrictions. Baumeister and Hamilton (2015) show that this procedure implies informative distributions on the structural objects of interest. In 

> 31As it is usually done in the literature, Sims and Zha (1998) suggest to preserve the Kronecker structure of the likelihood to avoid the inversion of _nk × nk_ matrices and gain computational speed. 

> 32Canova and P´erez Forero (2015) provide a general procedure to estimate structural VARs also in the case of overidentified systems where identification restrictions are of linear or of nonlinear form. 

38 

fact, it implies that the impact of a one standard-deviation structural shock is regarded (before seeing the data) as coming from a distribution with more mass around zero when the number of variables _n_ in the VAR is greater than 3 (and with more mass at large values when _n_ = 2). It also implies Cauchy priors for structural parameters such as elasticities. The influence of these priors does not vanish even asymptotically, since the data do not contain information about _Q_ . In fact, as the sample size goes to infinity, the height of the posterior distribution for the impact parameters is proportional to that of the prior distribution for all the points in the parameter space for which the structural coefficients satisfy the set restrictions that orthogonalise the true variance-covariance matrix. 

Giacomini and Kitagawa (2015) suggest the use of ‘ambiguous’ prior for the structural rotation matrix in order to account for the uncertainty about the structural parameters in all under-identified SVARs. The methodology consists in formally incorporating in the inference all classes of priors for the structural rotation matrix which are consistent with the a priori ‘dogmatic’ restrictions. In a similar vein, Baumeister and Hamilton (2017) discuss how to generalise priors on _B_ 0 to a less restrictive formulation that incorporates uncertainty about the identifying assumptions themselves, and use this approach to study the importance of shocks to oil supply and demand. 

## **8 Large Bayesian VARs** 

The size of the VARs typically used in empirical applications ranges from three to a dozen variables. VARs with larger sets of variables are impossible to estimate with standard techniques, due the ‘curse of dimensionality’ induced by the densely parametrised structure of the model.<sup>33</sup> However, in many applications there may be concerns about the omission of many potentially relevant economic indicators, that may affect 

> 33 The number of parameters to be estimated in an unrestricted VAR increases in the square of _n_ , the number of variables in _yt_ . Even when mechanically feasible, that is, when the number of available data points allows to produce point estimates for the parameters of interest, the tiny number of available degrees of freedom implies that parameters are estimated with substantial degrees of uncertainty, and typically yield very imprecise out-of-sample forecasts. 

39 

both structural analysis and forecasting.<sup>34</sup> Additionally, big datasets are increasingly important in economics to study phenomena in a connected and globalised world, where economic developments in one region can propagate and affect others.<sup>35</sup> 

VARs involving tens or even hundreds of variables have become increasingly popular following the work of Ba´nbura et al. (2010), that showed that standard macroeconomic – – priors Minnesota and sums-of-coefficients with a careful setting of the tightness parameters allowed to effectively incorporate very large sets of endogenous variables. Indeed, a stream of papers have found large VARs to forecast well (see, e.g. Ba´nbura et al. 2010, Carriero et al. 2015a, Carriero et al. 2009, Giannone et al. 2014 and Koop 2013). 

Early examples of higher-dimensional VARs are Panel VARs, where small countryspecific VARs are interacted to allow for international spillovers (see e.g. Canova and Ciccarelli, 2004, 2009). These models can be seen as large scale models that impose more structure on the system of equations. Koop and Korobilis (2015) study methods for high-dimensional panel VARs. In the study of international spillovers, an alternative to Panel VARs are Global VARs (Pesaran et al., 2004). A Bayesian treatment to G- VARs is in e.g. Cuaresma et al. (2016). 

A recent development in this literature has been the inclusion of stochastic volatility in Large BVAR models. Carriero et al. (2016a) assume a factor structure in the stochastic volatility of macroeconomic and financial variables in Large BVARs. In Carriero et al. (2016b), stochastic volatility and asymmetric priors for large _n_ are instead handled using a triangularisation method which allows to simulate the conditional mean coefficients of the VAR by drawing them equation by equation. Chan et al. (2017) propound composite likelihood methods for large BVARs with multivariate stochastic volat- 

> 34A standard example of this has been the debate about the so called ‘price puzzle’ – positive reaction of prices in response to a monetary tightening – that is often found in small scale VARs (see for example Christiano et al., 1999). The literature has often connected such a puzzling result as an artefact resulting from the omission of forward looking variables, like the commodity price index. In fact, one of the first instances of VARs incorporating more than a few variables was the 19-variable BVAR in Leeper et al. (1996) to study the effects of monetary policy shocks. 

> 35Large datasets of macroeconomic and financial variables are increasingly common. For example, in the US, the Federal Reserve Bank of St. Louis maintains the FRED-MD monthly database for well over 100 macroeconomic variables from 1960 to the present (see McCracken and Ng, 2015), and several other countries and economic areas have similarly sized datasets. 

40 

ility which involve estimating large numbers of parsimonious sub-models and then taking a weighted average across them. Koop et al. (2016) discuss large Bayesian VARMA. Koop (2017) reviews the applications of big data in macroeconomics. 

### **8.1 Bayesian VARs and Dynamic Factor Models** 

Research started with Ba´nbura et al. (2010) has shown that large BVARs are competitive models in leading with large- _n_ problems in empirical macroeconomics, along with factor models (see e.g. Forni et al., 2000; Stock and Watson, 2002) and Factor-Augmented VARs (FAVARs, see e.g. Bernanke et al., 2005). Indeed, Bayesian VARs are strictly connected to factor models as shown by De Mol et al. (2008) and Ba´nbura et al. (2015). 

The link can be better understood in terms of data that have been transformed to achieve stationarity, ∆ _yt_ , and that have been standardised to have zero mean and unit variance. A VAR in first differences can be written as 



Imposing the requirement that the level of each variable _yt_ must follow an independent random walk process is equivalent to requiring its first difference ∆ _yt_ to follow an independent white noise process. Hence, the prior on the autoregressive coefficients in Eq. (71) can be characterised by the following first and second moments: 



The covariance between coefficients at different lags is set to zero. Since the variables have been rescaled to have the same variance, we can set Σ = _σ_ I _n_ , where Σ = E[ _vtvt_<sup>_′_].</sup> Denote the eigenvalues of the variance-covariance matrix of the standardised data by _ζj_ , and the associated eigenvectors by _νj_ , for _j_ = 1 _, . . . , n_ , i.e. 



41 

where _νi_<sup>_′νj_= 1if</sup><sup>_i_=</sup><sup>_j_andzerootherwise.Weassumeanorderingsuchthat</sup><sup>_ζ_1</sup><sup>_≥ζ_2</sup><sup>_≥_</sup> _· · · ≥ ζn_ . The sample principal components of ∆ _yt_ are defined as 



The principal components transform correlated data, ∆ _yt_ , into linear combinations which are cross-sectionally uncorrelated and have unit variance, i.e. _T_<sup>_−_1 �</sup><sup>_T_</sup> _t_ =1<sup>_ztz_</sup> _t_<sup>_′_= I</sup><sup>_n_.</sup> The principal components can be ordered according to their ability to explain the variability in the data, as the total variance explained by each principal component is equal to _ζj_ . 

Rewrite the model in Eq. (71) in terms of the ordered principal components, as 



The priors that impose a uniform shrinkage on the parameters in Eq. (72) map into a non-uniform shrinkage on the parameters in Eq. (75): 



Importantly, the prior variance for the coefficients on the _j_ -th principal component is proportional to its share of explained variance of the data _ζj_ . 

If the data are characterised by a factor structure, then, as _n_ and _T_ increase, _ζj_ will go to infinity at a rate _n_ for _j_ = 1 _, . . . , r_ where _r_ is the number of common factors. Conversely, _ζr_ +1 _, . . . , ζn_ will grow at a slower rate, which cannot be faster than _n/√T_ . If _λ_ 1 is set such that it converges to zero a rate that is faster than that for the smaller _<u>√T</u>_ <u>1</u> eigenvalues and slower than that for the largest eigenvalues, e.g. _λ_ 1 _∝ n T_<sup>_ϱ_,with</sup> 0 _< ϱ <_ 1 _/_ 2, then _λ_ 1 _ζj_ will go to infinity for _j_ = 1 _, . . . , r_ and the prior on the coefficients associated with the first _r_ principal components will become flat (see Ba´nbura et al., 2015). Conversely, the coefficients related to the principal components associated with the bounded eigenvalues will be shrunk to zero, since _λ_ 1 _ζj_ will go to zero for _j > r_ . 

42 

De Mol et al. (2008) show that, if the data are generated by a factor model and _λ_ 1 is set according to the rate described above, the point forecasts obtained by using shrinkage estimators converge to the unfeasible optimal forecasts that would be obtained if the common factors were observed. 

### **8.2 Large SVARs, non-fundamentalness** 

One of the open problems in SVARs is the potential ‘non-fundamentalness’ of structural shocks for commonly employed VARs (a review on this issue is in Alessi et al. 2011). Non-fundamentalness implies that the true structural shocks (i.e. _et_ in Eq. 59) cannot be retrieved from current and past forecast errors of the VARs of choice (see Hansen and Sargent, 1980; Lippi and Reichlin, 1994). This situation arises when for example the econometrician does not have all the information available to economic agents, such as news about future policy actions. This is notoriously the case for fiscal shocks, as explained in Leeper et al. (2013). In this case, economic agents’ expectations may not be based only on the current and past _yt_ , implying that the residuals of the reducedform model (i.e. _ut_ in Eq. 1) are not the agents’ expectation/forecast errors. As a consequence, the shocks of interest may not be retrieved from the forecast errors, and may be non-fundamental. A possible solution is to allow for noninvertible moving average (MA) components. A different strategy is to view non-fundamentalness as an omitted variables problem. In this respect BVARs (and factor models) can offer a solution to the incorporation of larger information sets. For example, Ellahie and Ricco (2017) discuss the use of large BVARs to study the propagation of government purchases shocks, while controlling for potential non-fundamentalness of shocks in small VARs.<sup>36</sup> 

### **8.3 Forecasting in Data-Rich Environments** 

A research frontier is the application of Bayesian VARs to forecasting in data-rich environment, where the predictive content of large datasets (typically counting 100 or more 

> 36L¨utkepohl (2014) has observed that while large information techniques can be of help in dealing with the problem, they are bound to distort the parameter estimates and also the estimated impulse responses, hence results have to been taken with some caution. 

43 

variables) is exploited to forecast variables of interest. A recent survey is in Bok et al. (2017). 

Ba´nbura et al. (2010) study the forecasting performance of large Bayesian VARs. They find that while it increases with model size – provided that the shrinkage is appropriately chosen as a function of _n_ –, most of the gains are in fact achieved by a 20-variable VAR. Evaluation of the forecasting performance of medium and large Bayesian VARs is also provided in Koop (2013). Carriero et al. (2011) evaluate the forecasting accuracy of reduced-rank Bayesian VARs in large datasets. The reduced-rank model adopted has a factor model underlying structure, with factors that evolve following a VAR. Koop and Korobilis (2013) extend the framework to allow for time-varying parameters. Giannone et al. (2017) argue in favour of dense representations of predictive models for economic forecasting and use a ‘spike-and-slab’ prior that allows for both variable selection and shrinkage. 

BVARs are also a valuable tool for real-time forecasting and nowcasting with mixedfrequency datasets. In fact, they can be cast in state-space form and filtering techniques can be easily used to handle missing observations, data in real time, and data sampled at different frequencies. Recent examples of these applications include Schorfheide and Song (2015); Carriero et al. (2015b); Brave et al. (2016); Clark (2011); Giannone et al. (2014); McCracken et al. (2015). 

Koop et al. (2016) propose the use of Bayesian compressed VARs for high dimensional forecasting problems, and find that these tend to outperform both factor models and large VAR with prior shrinkage. More recently, Kastner and Huber (2017) develop BVARs that can handle vast dimensional information set and also allow for changes in the volatility of the error variance. This is done by assuming that the reduced-form residuals have a factor stochastic volatility structure (which allows for conditional equationby-equation estimation) and by applying a Dirichlet-Laplace prior (Bhattacharya et al., 2015b) to the VAR coefficients that heavily shrinks the coefficients towards zero while still allowing for some non-zero parameters. Kastner and Huber (2017) provide MCMCbased algorithms to sample from the posterior distributions and show that their proposed model typically outperforms simpler nested alternatives in forecasting output, inflation 

44 

and the interest rate. 

## **9 Time-Varying Parameter, State-Dependent, Stochastic Volatility VARs** 

Models that allow parameters to change over time are increasingly popular in empirical research, in recognition of the fact that they can capture structural changes in the economy. In fact, it seems to be a common belief that the properties of many (if not most) macroeconomic time series have changed over time, and can change across regimes or phases of the business cycle. Model parameters either change frequently and gradually over time according to a multivariate autoregressive process – as in e.g. in Time-Varying Parameters VARs (TVP-VARs) –, or they change abruptly and infrequently as in e.g. Markov-switching or structural-break models. 

### **9.1 Time-varying parameters VAR (TVP-VAR)** 

Time-varying parameters VARs differ from fixed-coefficient VARs in that they allow the parameters of the model to vary over time, according to a specified law of motion.<sup>37</sup> TVP-VARs often include also stochastic volatility (SV), which allows for time variation in the variance of the stochastic disturbances.<sup>38</sup> Doan et al. (1984) were first to show how estimation of a TVP-VAR with Litterman priors could be conducted by casting the VAR in state space form and using Kalman filtering techniques. This same specification is in Sims (1993). Bayesian time varying parameter VARs have become popular in empirical macroeconomics following the work of Cogley and Sargent (2002, 2005) and Primiceri (2005) who provided the foundations for Bayesian inference in these models, and used then innovations in MCMC algorithms to improve on their computational feasibility. 

> 37Review articles are in Del Negro and Schorfheide (2011); Koop and Korobilis (2010); Lubik and Matthes (2015). 

> 38Stochastic volatility in Bayesian VARs was initially introduced in Uhlig (1997). 

45 

The basic TVP-VAR is of the form 



where the constant coefficients of Eq. (1) are replaced by the time-varying _Aj,t_ . Eq. (77) can be rewritten in compact form as 



where _xt_ is defined as in Eq. (5), and _At_ = [ _A_ 1 _,t, . . . , Ap,t, ct_ ]<sup>_′_</sup> are. It is common to assume that the coefficients follow a random-walk process 



where _αt ≡ vec_ ( _At_ ). The covariance matrix Υ is usually restricted to be diagonal, and the innovations _ςt_ to be uncorrelated with _ut_ , with _ut_ distributed as in Eq. (2). The law of motion for _αt_ in Eq. (79) – i.e. the state equation –, implies that _αt_ +1 _|αt,_ Υ _∼N_ ( _αt,_ Υ), which can be used as a prior distribution for _αt_ +1. Hence, the prior for all the states (i.e. _αt ∀t_ ) is a product of normal distributions. For the initial vector of the VAR coefficients Cogley and Sargent (2002, 2005) use a prior of the form _α_ 1 _∼N_ <u>(</u> _<u>α</u>_ ~~1~~ _|_ 0<sup>_,_</sup><sup><u>Υ</u></sup> ~~1~~ _|_ 0<sup>),</sup> where _<u>α</u>_ ~~1~~ _|_ 0<sup>and</sup><sup><u>Υ</u></sup> ~~1~~ _|_ 0<sup>aresetbyestimatingafixed-coefficientVARwithaflatpriorona</sup> pre-sample.<sup>39</sup> If the Gaussian prior for the states is complemented with IW priors for both Σ and Υ, then sampling from the joint posterior is possible with a Gibbs sampling algorithm 

#### **Algorithm 5: Gibbs Sampling from Posterior of TVP-VAR Parameters.** Select starting values for Σ<sup>(0)</sup> and Υ<sup>(0)</sup> . For _s_ = 1 _, . . . , nsim_ : 

1. Draw _αT_<sup>(</sup><sup>_s_)</sup> from the full conditional posterior 



> 39See also the discussion in Karlsson (2013a) for additional details on the specification of the prior for _αt_ . 

46 

obtained from the Kalman filter. For _t_ = _T −_ 1 _, . . . ,_ 1 draw _αt_<sup>(</sup><sup>_s_)</sup> from the full conditional posterior 



obtained from a simulation smoother. 

2. Draw Υ<sup>(</sup><sup>_s_)</sup> from 



3. Draw Σ<sup>(</sup><sup>_s_)</sup> from 



When stochastic volatility is added to the framework, the VAR innovations are assumed to be still normally distributed, but with variance that evolves over time (see Cogley and Sargent, 2002, 2005; Primiceri, 2005) 



where _K_ is a lower-triangular matrix with ones on the main diagonal, and Ξ _t_ a diagonal matrix with elements evolving following a geometric random-walk process 



The prior distributions for Υ and _ση,j_<sup>2</sup><sup>_j_= 1</sup><sup>_, . . . , n_canbeusedtoexpressbeliefsabout</sup> the magnitude of the period-to-period drift in the VAR coefficients, and the changes in the volatility of the VAR innovations respectively. In practice, these priors are chosen to ensure that innovations to the parameters are small enough that the short- and medium-run dynamics of _yt_ are not swamped by the random-walk behaviour of _At_ and 

47 

Ξ _t_ . Primiceri (2005) extends the above TVP-VAR by also allowing the nonzero offdiagonal elements of the contemporaneous covariance matrix _K_ to evolve as randomwalk processes (i.e. _K_ is replaced by _Kt_ to allow for an arbitrary time-varying correlation structure). A Gibbs sampler to draw from the posterior distribution of the parameters is in Primiceri (2005). 

### **9.2 Markov Switching, Threshold, and Smooth Transition VARs** 

Contrary to the drifting coefficients models discussed in the previous section, Markov switching (MS) VARs are designed to capture abrupt changes in the dynamics of _yt_ .<sup>40</sup> These can be viewed as models that allow for at least one structural break to occur within the sample, with the timing of the break being unknown. They are of the form 



where _xt_ is defined as in Eq. (5). The matrix of autoregressive coefficients _A_ ( _st_ ) and the variance of the error term Σ( _st_ ) are a function of a discrete _m_ -state Markov process _st_ with fixed transition probabilities 



If _πii_ = 1 for some _i ∈_ [1 _, . . . , m_ ], then _Si_ is an absorbing state from which the system is not allowed to move away. Suppose _m_ = 2, and that both _A_ ( _st_ ) and Σ( _st_ ) change simultaneously when switching from _S_ 1 to _S_ 2 and vice versa. If a NIW prior is specified for _A_ ( _st_ ) and Σ( _st_ ), and _π_ 11 and _π_ 22 have independent Beta prior distributions, a Gibbs sampler can be used to sample from the posterior (see e.g. Del Negro and Schorfheide, 2011). 

A MS-VAR with non-recurrent states is called a ‘change-point’ model (see Chib, 

> 40The book by Kim and Nelson (1999) is the standard reference for frequentist and Bayesian estimation of Markov switching models. 

48 

1998; Bauwens and Rombouts, 2012). Generalising the specification to allow for more states, with the appropriate transition probabilities, allows to adapt the change-point model to the case of several structural breaks (see also Koop and Potter, 2007, 2009; Liu et al., 2017, for models where the number of change-points is unknown). Important extensions regard the transmission of structural shocks in the presence of structural breaks and in a time-varying coefficient environment discussed in e.g. Sims and Zha (2006) and Koop et al. (2011) who also allow for cointegration. 

In threshold VARs (TVARs), the coefficients of the model change across regimes when an observable variable exceeds a given threshold value. Bayesian inference in TVAR models is discussed in detail in Geweke and Terui (1993) and Chen and Lee (1995). A TVAR with two regimes can be written as 



where _A_ and _A_<sup>_∗_</sup> are _n × k_ matrices that collect the autoregressive coefficients of the two regimes, Θ( _·_ ) is a Heaviside step function, i.e. a discontinuous function whose value is zero for a negative argument, and one for a positive argument, _τt−d_ is threshold variable at lag _d_ , and _τ_ is a potentially unobserved threshold value. The system in Eq. (84) can be easily generalised to allow for multiple regimes. TVARs have been applied to several problems in the economic literature (see, for example Koop and Potter, 1999; Ricco et al., 2016; Alessandri and Mumtaz, 2017). 

If the coefficients gradually migrate to the new state(s), the model is called a smoothtransition VAR (STVAR). A STVAR model with two regimes can be written as 



where _A_<sup>_∗_</sup> , _A_ , and _xt_ are defined as in Eq. (84). The function _G_ ( _wt_ ; _ϑ, w_ ) governs the transition across states, and is a function of the observable variable _wt_ , and of the 

49 

parameters _ϑ_ and _w_ . In an exponential smooth-transition (EST) VAR, typically 



where _ϑ >_ 0 determines the speed of transition across regimes, _w_ can be thought of as a threshold value, and _σw_ is the sample standard deviation of _wt_ . The higher _ϑ_ the more abrupt the transition, the more the model collapses into a fixed threshold VAR. Among others, Gefang and Strachan (2009) and Gefang (2012) apply Bayesian techniques to estimate Smooth-transition VAR models. 

50 

## **References** 

- Aastveit, Knut Are, Francesco Ravazzolo, and Herman K. Van Dijk (2017) “Combined Density Nowcasting in an Uncertain Economic Environment,” _Journal of Business & Economic Statistics_ , Vol. 0, No. 0, pp. 1–15. 

- Alessandri, Piergiorgio and Haroon Mumtaz (2017) “Financial conditions and density forecasts for US output and inflation,” _Review of Economic Dynamics_ , Vol. 24, pp. 66–78, March. 

- Alessi, Lucia, Matteo Barigozzi, and Marco Capasso (2011) “Non-Fundamentalness in Structural Econometric Models: A Review,” _International Statistical Review_ , Vol. 79, No. 1, pp. 16–47, 04. 

- Amisano, Gianni and John Geweke (2017) “Prediction Using Several Macroeconomic Models,” _The Review of Economics and Statistics_ , Vol. 99, No. 5, pp. 912–925. 

- Andersson, Michael K., Stefan Palmqvist, and Daniel Waggoner (2010) “Density-Conditional Forecasts in Dynamic Multivariate Models,” Working Paper Series 247, Sveriges Riksbank (Central Bank of Sweden). 

- Antolin-Diaz, Juan, Ivan Petrella, and Juan Francisco Rubio-Ram´ırez (2018) “Structural Scenario Analysis with SVARs,” CEPR Discussion Papers 12579, C.E.P.R. Discussion Papers. 

- Ba´nbura, Marta, Domenico Giannone, and Michele Lenza (2015) “Conditional forecasts and scenario analysis with vector autoregressions for large cross-sections,” _International Journal of Forecasting_ , Vol. 31, No. 3, pp. 739 – 756. 

- Ba´nbura, Marta, Domenico Giannone, and Lucrezia Reichlin (2010) “Large Bayesian vector auto regressions,” _Journal of Applied Econometrics_ , Vol. 25, No. 1, pp. 71–92. 

- Baumeister, Christiane and James D. Hamilton (2015) “Sign Restrictions, Structural Vector Autoregressions, and Useful Prior Information,” _Econometrica_ , Vol. 83, No. 5, pp. 1963– 1999, September. 

   - (2017) “Inference in Structural Vector Autoregressions When the Identifying Assump- 

   - tions are Not Fully Believed: Re-evaluating the Role of Monetary Policy in Economic Fluctuations,” mimeo, UCSD. 

- Bauwens, Luc and Jeroen V.K. Rombouts (2012) “On marginal likelihood computation in change-point models,” _Computational Statistics & Data Analysis_ , Vol. 56, No. 11, pp. 3415– 3429. 

- Belmonte, Miguel A.G., Gary Koop, and Dimitris Korobilis (2014) “Hierarchical Shrinkage in Time-Varying Parameter Models,” _Journal of Forecasting_ , Vol. 33, No. 1, pp. 80–94, January. 

- Berger, James O. (1985) _Statistical Decision Theory and Bayesian Analysis_ : Springer. 

- Bernanke, Ben S., Jean Boivin, and Piotr Eliasz (2005) “Measuring the Effects of Monetary Policy: A Factor-Augmented Vector Autoregressive (FAVAR) Approach,” _The Quarterly Journal of Economics_ , Vol. 120, pp. 387–422. 

- Bernardo, J.M. and A.F.M. Smith (2009) _Bayesian Theory_ , Wiley Series in Probability and Statistics: Wiley. 

- Bhattacharya, Anirban, Debdeep Pati, Natesh S. Pillai, and David B. Dunson (2015a) “Dirichlet-Laplace Priors for Optimal Shrinkage,” _Journal of the American Statistical Association_ , Vol. 110, No. 512, pp. 1479–1490. PMID: 27019543. 

51 

(2015b) “Dirichlet-Laplace priors for optimal shrinkage,” _Journal of the American Statistical Association_ , Vol. 110, No. 512, pp. 1479–1490. 

- Billio, Monica, Roberto Casarin, Francesco Ravazzolo, and Herman K. van Dijk (2013) “Timevarying combinations of predictive densities using nonlinear filtering,” _Journal of Econometrics_ , Vol. 177, No. 2, pp. 213 – 232. Dynamic Econometric Modeling and Forecasting. 

- Bloor, Chris and Troy Matheson (2011) “Real-time conditional forecasts with Bayesian VARs: An application to New Zealand,” _The North American Journal of Economics and Finance_ , Vol. 22, No. 1, pp. 26 – 42. Symposium on Nowcasting and Model Combination. 

- Bok, Brandyn, Daniele Caratelli, Domenico Giannone, Argia M. Sbordone, and Andrea Tambalotti (2017) “Macroeconomic nowcasting and forecasting with big data,” Staff Reports 830, Federal Reserve Bank of New York. 

- Brave, Scott, R. Andrew Butters, and Alejandro Justiniano (2016) “Forecasting Economic Activity with Mixed Frequency Bayesian VARs,” Working Paper Series WP-2016-5, Federal Reserve Bank of Chicago. 

- Canova, Fabio (2007) _Methods for Applied Macroeconomic Research_ : Princeton University Press. 

- Canova, Fabio and Matteo Ciccarelli (2004) “Forecasting and turning point predictions in a Bayesian panel VAR model,” _Journal of Econometrics_ , Vol. 120, No. 2, pp. 327–359, June. (2009) “Estimating Multicountry VAR Models,” _International Economic Review_ , Vol. 

- 50, No. 3, pp. 929–959. 

(2013) “Panel vector autoregressive models: a survey,” Working Paper Series 1507, European Central Bank. 

- Canova, Fabio and Gianni De Nicolo (2002) “Monetary disturbances matter for business fluctuations in the G-7,” _Journal of Monetary Economics_ , Vol. 49, No. 6, pp. 1131–1159, September. 

- Canova, Fabio and Fernando J. P´erez Forero (2015) “Estimating overidentified, nonrecursive, time-varying coefficients structural vector autoregressions,” _Quantitative Economics_ , Vol. 6, No. 2, pp. 359–384. 

- Carriero, Andrea, Todd E. Clark, and Massimiliano Marcellino (2015a) “Bayesian VARs: Specification Choices and Forecast Accuracy,” _Journal of Applied Econometrics_ , Vol. 30, No. 1, pp. 46–73. 

   - (2015b) “Realtime nowcasting with a Bayesian mixed frequency model with stochastic 

   - volatility,” _Journal of the Royal Statistical Society: Series A (Statistics in Society)_ , Vol. 178, No. 4, pp. 837–862. 

   - (2016a) “Common Drifting Volatility in Large Bayesian VARs,” _Journal of Business_ 

   - _& Economic Statistics_ , Vol. 34, No. 3, pp. 375–390. 

   - (2016b) “Large Vector Autoregressions with Stochastic Volatility and Flexible Priors,” 

   - Working Paper 1617, Federal Reserve Bank of Cleveland. 

- Carriero, Andrea, George Kapetanios, and Massimiliano Marcellino (2009) “Forecasting exchange rates with a large Bayesian VAR,” _International Journal of Forecasting_ , Vol. 25, No. 2, pp. 400–417. 

   - (2011) “Forecasting large datasets with Bayesian reduced rank multivariate models,” 

   - _Journal of Applied Econometrics_ , Vol. 26, No. 5, pp. 735–761, August. 

52 

- Chan, Joshua C. C., Eric Eisenstat, Chenghan Hou, and Gary Koop (2017) “Composite Likelihood Methods for Large Bayesian VARs with Stochastic Volatility,” mimeo, University of Strathclyde. 

- Chen, Cathy W. S. and Jack C. Lee (1995) “Bayesian Inference of Threshold Autoregressive Models,” _Journal of Time Series Analysis_ , Vol. 16, No. 5, pp. 483–492. 

- Chib, Siddhartha (1998) “Estimation and comparison of multiple change-point models,” _Journal of Econometrics_ , Vol. 86, No. 2, pp. 221 – 241. 

   - (2001) “Markov Chain Monte Carlo Methods: Computation and Inference,” in 

   - James J. Heckman and Edward Leamer eds. _Handbook of Econometrics_ , Vol. 5: Elsevier, – 

   - pp. 3569 3649. 

- Chib, Siddhartha and Edward Greenberg (1995) “Understanding the Metropolis-Hastings Algorithm,” _The American Statistician_ , Vol. 49, No. 4, pp. 327–335. 

- Chiu, Ching-Wai (Jeremy), Haroon Mumtaz, and G´abor Pint´er (2017) “Forecasting with VAR models: Fat tails and stochastic volatility,” _International Journal of Forecasting_ , Vol. 33, No. 4, pp. 1124 – 1143. 

- Christiano, Lawrence J., Martin Eichenbaum, and Charles L. Evans (1999) “Monetary policy shocks: What have we learned and to what end?” in _Handbook of Macroeconomics_ , Vol. 1, Part A: Elsevier, pp. 65 – 148. 

- Ciccarelli, Matteo and Alessandro Rebucci (2003) “Bayesian Vars; A Survey of the Recent Literature with An Application to the European Monetary System,” IMF Working Papers 03/102, International Monetary Fund. 

- Clark, Todd E. (2011) “Real-Time Density Forecasts From Bayesian Vector Autoregressions With Stochastic Volatility,” _Journal of Business & Economic Statistics_ , Vol. 29, No. 3, pp. 327–341. 

- Cogley, Timothy and Thomas J. Sargent (2002) “Evolving Post-World War II U.S. Inflation Dynamics,” in _NBER Macroeconomics Annual 2001, Volume 16_ : National Bureau of Economic Research, Inc, pp. 331–388. 

   - (2005) “Drift and Volatilities: Monetary Policies and Outcomes in the Post WWII 

   - U.S,” _Review of Economic Dynamics_ , Vol. 8, No. 2, pp. 262–302, April. 

- Cogley, Timothy, Sergei Morozov, and Thomas J. Sargent (2005) “Bayesian fan charts for U.K. inflation: Forecasting and sources of uncertainty in an evolving monetary system,” _Journal of Economic Dynamics and Control_ , Vol. 29, No. 11, pp. 1893 – 1925. Expectations, learning, and monetary policy. 

- Cuaresma, Jes´us Crespo, Martin Feldkircher, and Florian Huber (2016) “Forecasting with Global Vector Autoregressive Models: a Bayesian Approach,” _Journal of Applied Econometrics_ , Vol. 31, No. 7, pp. 1371–1391. 

- De Mol, Christine, Domenico Giannone, and Lucrezia Reichlin (2008) “Forecasting using a large number of predictors: Is Bayesian shrinkage a valid alternative to principal components?” _Journal of Econometrics_ , Vol. 146, No. 2, pp. 318 – 328. Honoring the research contributions of Charles R. Nelson. 

- DeJong, David N., Beth Ingram, and Charles H. Whiteman (1993) “Analyzing VARs with monetary business cycle model priors,” _Proceedings of the American Statistical Association, Bayesian Statistics Section_ , pp. 160–169. 

- Del Negro, Marco and Frank Schorfheide (2004) “Priors from General Equilibrium Models for VARS,” _International Economic Review_ , Vol. 45, No. 2, pp. 643–673, May. 

53 

(2011) “Bayesian Macroeconometrics,” in John Geweke, Gary Koop, and Herman Van Dijk eds. _The Oxford Handbook of Bayesian Econometrics_ : Oxford University Press, pp. 293–389. 

- Del Negro, Marco, Raiden B. Hasegawa, and Frank Schorfheide (2016) “Dynamic prediction pools: An investigation of financial frictions and forecasting performance,” _Journal of Econometrics_ , Vol. 192, No. 2, pp. 391 – 405. Innovations in Multiple Time Series Analysis. 

- Dieppe, Alistair, Bj¨orn van Roye, and Romain Legrand (2016) “The BEAR toolbox,” Working Paper Series 1934, European Central Bank. 

- Doan, Thomas, Robert Litterman, and Christopher Sims (1984) “Forecasting and conditional projection using realistic prior distributions,” _Econometric Reviews_ , Vol. 3, No. 1, pp. 1–100. 

- Ellahie, Atif and Giovanni Ricco (2017) “Government purchases reloaded: Informational insufficiency and heterogeneity in fiscal VARs,” _Journal of Monetary Economics_ , Vol. 90, No. C, pp. 13–27. 

- Forni, Mario, Marc Hallin, Marco Lippi, and Lucrezia Reichlin (2000) “The Generalized Dynamic-Factor Model: Identification and Estimation,” _Review of Economics and Statistics_ , Vol. 82, No. 4, pp. 540–554. 

- Gefang, Deborah (2012) “Money?output Causality Revisited ? A Bayesian Logistic Smooth Transition VECM Perspective,” _Oxford Bulletin of Economics and Statistics_ , Vol. 74, No. 1, pp. 131–151, February. 

- Gefang, Deborah and Rodney Strachan (2009) “Nonlinear Impacts of International Business Cycles on the U.K. – A Bayesian Smooth Transition VAR Approach,” _Studies in Nonlinear Dynamics & Econometrics_ , Vol. 14, No. 1, pp. 1–33, December. 

- Geisser, Seymour (1965) “Bayesian Estimation in Multivariate Analysis,” _The Annals of Mathematical Statistics_ , Vol. 36, No. 1, pp. 150–159, 02. 

- Gelman, A., J.B. Carlin, H.S. Stern, and D.B. Rubin (2003) _Bayesian Data Analysis, Second Edition_ , Chapman & Hall/CRC Texts in Statistical Science: Taylor & Francis. 

- Gelman, A., J.B. Carlin, H.S. Stern, D.B. Dunson, A. Vehtari, and D.B. Rubin (2013) _Bayesian Data Analysis, Third Edition_ , Chapman & Hall/CRC Texts in Statistical Science: Taylor & Francis. 

- George, Edward I., Dongchu Sun, and Shawn Ni (2008) “Bayesian stochastic search for VAR model restrictions,” _Journal of Econometrics_ , Vol. 142, No. 1, pp. 553 – 580. 

- Geweke, John (1996) “Bayesian reduced rank regression in econometrics,” _Journal of Econometrics_ , Vol. 75, No. 1, pp. 121–146, November. (1999) “Using simulation methods for bayesian econometric models: inference, devel- 

- opment,and communication,” _Econometric Reviews_ , Vol. 18, No. 1, pp. 1–73. 

   - (2005) _Contemporary Bayesian Econometrics and Statistics_ , Wiley Series in Probab- 

   - ility and Statistics: Wiley. 

- Geweke, John and Gianni Amisano (2011) “Optimal prediction pools,” _Journal of Econometrics_ , Vol. 164, No. 1, pp. 130 – 141. Annals Issue on Forecasting. (2012) “Prediction with Misspecified Models,” _American Economic Review_ , Vol. 102, 

- No. 3, pp. 482–86, May. 

- Geweke, John and Nobuhiko Terui (1993) “Bayesian Threshold Autoregressive Models for Nonlinear Time Series,” _Journal of Time Series Analysis_ , Vol. 14, No. 5, pp. 441–454. 

54 

- Geweke, John and Charles Whiteman (2006a) “Bayesian Forecasting,” in G. Elliott, C. Granger, and A. Timmermann eds. _Handbook of Economic Forecasting_ , Vol. 1: Elsevier, 1st edition, Chap. 01, pp. 3–80. 

- (2006b) “Bayesian Forecasting,” in G. Elliott, C.W.J. Granger, and A. Timmermann 

- eds. _Handbook of Economic Forecasting_ , Vol. 1: Elsevier, pp. 3 – 80. 

- Giacomini, Raffaella and Toru Kitagawa (2015) “Robust inference about partially identified SVARs,” mimeo, UCL. 

- Giannone, Domenico, Michele Lenza, and Giorgio E. Primiceri (2015) “Prior Selection for Vector Autoregressions,” _The Review of Economics and Statistics_ , Vol. 2, No. 97, pp. 436– 451, May. 

   - (2016) “Priors for the Long Run,” CEPR Discussion Papers 11261, C.E.P.R. Discus- 

   - sion Papers. 

   - (2017) “Economic Predictions with Big Data: The Illusion Of Sparsity,” CEPR Dis- 

   - cussion Papers 12256, C.E.P.R. Discussion Papers. 

- Giannone, Domenico, Michele Lenza, and Lucrezia Reichlin (2008) “Explaining The Great Moderation: It Is Not The Shocks,” _Journal of the European Economic Association_ , Vol. 6, No. 2-3, pp. 621–633, 04-05. 

- Giannone, Domenico, Michele Lenza, Daphne Momferatou, and Luca Onorante (2014) “Shortterm inflation projections: A Bayesian vector autoregressive approach,” _International Journal of Forecasting_ , Vol. 30, No. 3, pp. 635–644. 

- Griffin, Jim E. and Philip J. Brown (2010) “Inference with normal-gamma prior distributions in regression problems,” _Bayesian Anal._ , Vol. 5, No. 1, pp. 171–188, 03. 

- Griffin, Jim and Phil Brown (2017) “Hierarchical Shrinkage Priors for Regression Models,” _Bayesian Analysis_ , Vol. 12, No. 1, pp. 135–159, 03. 

- Hajivassiliou, Vassilis A. and Paul A. Ruud (1994) “Classical estimation methods for LDV models using simulation,” in _Handbook of Econometrics_ , Vol. 4: Elsevier, pp. 2383 – 2441. 

- Hall, Stephen G. and James Mitchell (2007) “Combining density forecasts,” _International Journal of Forecasting_ , Vol. 23, No. 1, pp. 1 – 13. 

- Hansen, Lars Peter and Thomas J. Sargent (1980) “Formulating and estimating dynamic linear rational expectations models,” _Journal of Economic Dynamics and Control_ , Vol. 2, No. 1, pp. 7–46, May. 

- Highfield, Richard A. (1992) “Forecasting Similar Time Series with Bayesian Pooling Methods: Application to Forecasting European Output Growth,” in Prem K. Goel and N. Sreenivas Iyengar eds. _Bayesian Analysis in Statistics and Econometrics_ , pp. 303–326, New York, NY: Springer New York. 

- Huber, Florian and Martin Feldkircher (2017) “Adaptive Shrinkage in Bayesian Vector Autoregressive Models,” _Journal of Business & Economic Statistics_ , Vol. 0, No. 0, pp. 1–13. 

- Hwang, Youngjin (2017) “Forecasting with Specification-Switching VARs,” _Journal of Forecasting_ , Vol. 36, No. 5, pp. 581–596. for.2455. 

- Ingram, Beth F. and Charles H. Whiteman (1994) “Supplanting the ’Minnesota’ prior: Forecasting macroeconomic time series using real business cycle model priors,” _Journal of Monetary Economics_ , Vol. 34, No. 3, pp. 497–510, December. 

55 

- Jaroci´nski, Marek (2010) “Conditional forecasts and uncertainty about forecast revisions in vector autoregressions,” _Economics Letters_ , Vol. 108, No. 3, pp. 257–259, September. 

- Jaroci´nski, Marek and Bartosz Ma´ckowiak (2017) “Granger Causal Priority and Choice of Variables in Vector Autoregressions,” _The Review of Economics and Statistics_ , Vol. 99, No. 2, pp. 319–329, May. 

- Jaroci´nski, Marek and Albert Marcet (2011) “Autoregressions in Small Samples, Priors about Observables and Initial Conditions,” CEP Discussion Papers dp1061, Centre for Economic Performance, LSE. 

   - (2014) “Contrasting Bayesian and Frequentist Approaches to Autoregressions: the 

   - Role of the Initial Condition,” Working Papers 776, Barcelona Graduate School of Economics. 

- Jochmann, Markus and Gary Koop (2015) “Regime-switching cointegration,” _Studies in Nonlinear Dynamics & Econometrics_ , Vol. 19, No. 1, pp. 35–48, February. 

- Kadane, Joseph B. (1975) “The Role of Identification in Bayesian Theory,” in Stephen E. Fienberg and Arnold Zellner eds. _Studies in Bayesian Econometrics and Statistics_ : Amsterdam: North-Holland, Chap. 5.2, pp. 175–191. 

- Kadiyala, Rao K. and Sune Karlsson (1993) “Forecasting with generalized bayesian vector auto regressions,” _Journal of Forecasting_ , Vol. 12, No. 3-4, pp. 365–378. (1997) “Numerical Methods for Estimation and Inference in Bayesian VAR-Models,” 

- _Journal of Applied Econometrics_ , Vol. 12, No. 2, pp. 99–132, March-Apr. 

- Karlsson, Sune (2013a) “Forecasting with Bayesian Vector Autoregression,” in Graham Elliott and Allan Timmermann eds. _Handbook of Economic Forecasting_ , Vol. 2 of Handbook of Economic Forecasting: Elsevier, pp. 791 – 897. 

   - (2013b) _Forecasting with Bayesian Vector Autoregression_ , Vol. 2 of Handbook of Eco- 

   - nomic Forecasting, Chap. 0, pp. 791–897: Elsevier. 

- Kastner, G. and F. Huber (2017) “Sparse Bayesian vector autoregressions in huge dimensions,”Technical report, WU Vienna University of Economics and Business. 

- Kilian, L. and H. L¨utkepohl (2017) _Structural Vector Autoregressive Analysis_ , Themes in Modern Econometrics: Cambridge University Press. 

- Kim, Jae Young (1994) “Bayesian Asymptotic Theory in a Time Series Model with a Possible Nonstationary Process,” _Econometric Theory_ , Vol. 10, No. 3/4, pp. 764–773. 

- Kim, Chang Jin and Charles Nelson (1999) _State-Space Models with Regime Switching: Classical and Gibbs-Sampling Approaches with Applications_ , Vol. 1: The MIT Press, 1st edition. 

- King, Robert G., Charles I. Plosser, and Sergio T. Rebelo (1988) “Production, growth and business cycles: I. The basic neoclassical model,” _Journal of Monetary Economics_ , Vol. 21, No. 2, pp. 195 – 232. 

- Kleibergen, Frank and Richard Paap (2002) “Priors, posteriors and bayes factors for a Bayesian analysis of cointegration,” _Journal of Econometrics_ , Vol. 111, No. 2, pp. 223–249, December. 

- Kleibergen, Frank and Herman K. van Dijk (1994) “On the Shape of the Likelihood/Posterior in Cointegration Models,” _Econometric Theory_ , Vol. 10, No. 3-4, pp. 514–551, August. 

- Koop, Gary (2003) _Bayesian Econometrics_ : Wiley. 

56 

(2013) “Forecasting with Medium and Large Bayesian VARS,” _Journal of Applied Econometrics_ , Vol. 28, No. 2, pp. 177–203, March. 

   - (2017) “Bayesian methods for empirical macroeconomics with big data,” _Review of_ 

   - _Economic Analysis_ , Vol. 9, pp. 33–56, March. 

- Koop, Gary and Dimitris Korobilis (2010) “Bayesian Multivariate Time Series Methods for Empirical Macroeconomics,” _Foundations and Trends(R) in Econometrics_ , Vol. 3, No. 4, pp. 267–358, July. 

(2012) “Forecasting Inflation using Dynamic Model Averaging,” _International Economic Review_ , Vol. 53, No. 3, pp. 867–886. 

   - (2013) “Large time-varying parameter VARs,” _Journal of Econometrics_ , Vol. 177, No. 

   - 2, pp. 185–198. 

   - (2015) “Forecasting With High Dimensional Panel VARs,” Working Papers 25, Busi- 

   - ness School - Economics, University of Glasgow. 

- Koop, Gary and Simon M. Potter (1999) “Dynamic Asymmetries in U.S. Unemployment,” _Journal of Business & Economic Statistics_ , Vol. 17, No. 3, pp. 298–312. (2007) “Estimation and Forecasting in Models with Multiple Breaks,” _The Review of_ 

- _Economic Studies_ , Vol. 74, No. 3, pp. 763–789. 

   - (2009) “Prior Elicitation In Multiple Change-Point Models,” _International Economic_ 

   - _Review_ , Vol. 50, No. 3, pp. 751–772, August. 

- Koop, Gary and Mark F. J. Steel (1991) “A comment on: “To criticize the critics: An objective bayesian analysis of stochastic trends”, By Peter C. B. Phillips,” _Journal of Applied Econometrics_ , Vol. 6, No. 4, pp. 365–370. 

- Koop, Gary, Dimitris Korobilis, and Davide Pettenuzzo (2016) “Bayesian Compressed Vector Autoregressions,” Working Papers 103, Brandeis University, Department of Economics and International Businesss School. 

- Koop, Gary, Roberto Leon-Gonzalez, and Rodney W. Strachan (2011) “Bayesian inference in a time varying cointegration model,” _Journal of Econometrics_ , Vol. 165, No. 2, pp. 210–220. 

- Koop, G., R.W. Strachan, H.K. van Dijk, and M. Villani (2006) “Monetary policy shocks: What have we learned and to what end?” in T. C.Mills and K. P. Patterson eds. _Palgrave Handbook of Econometrics_ , Vol. 1: Basingstoke: Palgrave Macmillan, pp. 871–98. 

- Korobilis, Dimitris (2013) “VAR Forecasting Using Bayesian Variable Selection,” _Journal of Applied Econometrics_ , Vol. 28, No. 2, pp. 204–230. 

- Kwan, Yum K. (1998) “Asymptotic Bayesian analysis based on a limited information estimator,” _Journal of Econometrics_ , Vol. 88, No. 1, pp. 99–121, November. 

- Leeper, Eric M., Christopher A. Sims, and Tao Zha (1996) “What Does Monetary Policy Do?,” _Brookings Papers on Economic Activity_ , Vol. 27, No. 2, pp. 1–78. 

- Leeper, Eric M., Todd B. Walker, and Shu-Chun Susan Yang (2013) “Fiscal Foresight and Information Flows,” _Econometrica_ , Vol. 81, No. 3, pp. 1115–1145, May. 

- Lippi, Marco and Lucrezia Reichlin (1994) “VAR analysis, nonfundamental representations, blaschke matrices,” _Journal of Econometrics_ , Vol. 63, No. 1, pp. 307–325, July. 

- Litterman, Robert B. (1979) “Techniques of forecasting using vector autoregressions,” Working Papers 115, Federal Reserve Bank of Minneapolis. 

57 

(1980) “A Bayesian Procedure for Forecasting with Vector Autoregression,” working papers, MIT Department of Economics. 

   - (1986) “Forecasting with Bayesian Vector Autoregressions-Five Years of Experience,” 

   - _Journal of Business & Economic Statistics_ , Vol. 4, No. 1, pp. 25–38, January. 

- Liu, Philip, Haroon Mumtaz, Konstantinos Theodoridis, and Francesco Zanetti (2017) “Changing Macroeconomic Dynamics at the Zero Lower Bound,” _Journal of Business & Economic Statistics_ , Vol. 0, No. ja, pp. 0–0. 

- Lubik, Thomas A. and Christian Matthes (2015) “Time-Varying Parameter Vector Autoregressions: Specification, Estimation, and an Application,” _Economic Quarterly_ , Vol. 4Q, pp. 323–352. 

- L¨utkepohl, Helmut (2014) “Fundamental Problems with Nonfundamental Shocks,” in Niels Haldrup, Mika Meitz, and Pentti Saikkonen eds. _Essays in Nonlinear Time Series Econometrics_ : Oxford University Press, Chap. 8, pp. 198–214. 

- McCracken, Michael W. and Serena Ng (2015) “FRED-MD: A Monthly Database for Macroeconomic Research,” Working Papers 2015-12, Federal Reserve Bank of St. Louis. 

- McCracken, Michael W., Michael T. Owyang, and Tatevik Sekhposyan (2015) “Real-Time Forecasting with a Large, Mixed Frequency, Bayesian VAR,” Working Papers 2015-30, Federal Reserve Bank of St. Louis. 

- Miranda-Agrippino, Silvia and Giovanni Ricco (2017) “The transmission of monetary policy shocks,” Bank of England working papers 657, Bank of England. 

- Mitchell, T. J. and J. J. Beauchamp (1988) “Bayesian Variable Selection in Linear Regression,” _Journal of the American Statistical Association_ , Vol. 83, No. 404, pp. 1023–1032. 

- Moon, Hyungsik Roger and Frank Schorfheide (2012) “Bayesian and Frequentist Inference in Partially Identified Models,” _Econometrica_ , Vol. 80, No. 2, pp. 755–782, March. 

- M¨uller, Ulrich K. (2013) “Risk of Bayesian Inference in Misspecified Models, and the Sandwich Covariance Matrix,” _Econometrica_ , Vol. 81, No. 5, pp. 1805–1849. 

- M¨uller, Ulrich K. and Graham Elliott (2003) “Tests for Unit Roots and the Initial Condition,” _Econometrica_ , Vol. 71, No. 4, pp. 1269–1286. 

- Panagiotelis, Anastasios and Michael Smith (2008) “Bayesian density forecasting of intraday electricity prices using multivariate skew t distributions,” _International Journal of Forecasting_ , Vol. 24, No. 4, pp. 710–727. 

- Pesaran, M. Hashem, Til Schuermann, and Scott M Weiner (2004) “Modeling Regional Interdependencies Using a Global Error-Correcting Macroeconometric Model,” _Journal of Business & Economic Statistics_ , Vol. 22, No. 2, pp. 129–162. 

- Phillips, P. C. B. (1991a) “Bayesian routes and unit roots: De rebus prioribus semper est disputandum,” _Journal of Applied Econometrics_ , Vol. 6, No. 4, pp. 435–473. (1991b) “To criticize the critics: An objective bayesian analysis of stochastic trends,” 

- _Journal of Applied Econometrics_ , Vol. 6, No. 4, pp. 333–364. 

- Poirier, Dale J. (1998) “Revising Beliefs in Nonidentified Models,” _Econometric Theory_ , Vol. 14, No. 4, pp. 483–509. 

- Primiceri, Giorgio E. (2005) “Time Varying Structural Vector Autoregressions and Monetary Policy,” _Review of Economic Studies_ , Vol. 72, No. 3, pp. 821–852. 

58 

- Raftery, Adrian E., Miroslav K´arn´y, and Pavel Ettler (2010) “Online Prediction Under Model Uncertainty via Dynamic Model Averaging: Application to a Cold Rolling Mill,” _Technometrics_ , Vol. 52, No. 1, pp. 52–66. 

- Raiffa, H. and R. Schlaifer (1961) _Applied statistical decision theory_ , Studies in managerial economics: Division of Research, Graduate School of Business Adminitration, Harvard University. 

- Ricco, Giovanni, Giovanni Callegari, and Jacopo Cimadomo (2016) “Signals from the government: Policy disagreement and the transmission of fiscal shocks,” _Journal of Monetary Economics_ , Vol. 82, No. C, pp. 107–118. 

- Robertson, John C. and Ellis W. Tallman (1999) “Vector autoregressions: forecasting and reality,” _Economic Review_ , Vol. Issue Q1, pp. 4–18. 

- Robertson, John C., Ellis W. Tallman, and Charles H. Whiteman (2005) “Forecasting Using Relative Entropy,” _Journal of Money, Credit and Banking_ , Vol. 37, No. 3, pp. 383–401. 

- Rubio-Ram´ırez, Juan F., Daniel F. Waggoner, and Tao Zha (2010) “Structural Vector Autoregressions: Theory of Identification and Algorithms for Inference,” _The Review of Economic Studies_ , Vol. 77, No. 2, pp. 665–696. 

- Schorfheide, Frank and Dongho Song (2015) “Real-Time Forecasting With a Mixed-Frequency VAR,” _Journal of Business & Economic Statistics_ , Vol. 33, No. 3, pp. 366–380, July. 

- Sims, Christopher A. (1980) “Macroeconomics and Reality,” _Econometrica_ , Vol. 48, No. 1, pp. 1–48, January. (1988) “Bayesian skepticism on unit root econometrics,” _Journal of Economic Dy-_ 

- _namics and Control_ , Vol. 12, No. 2, pp. 463 – 474. 

   - (1991) “Comment by Christopher A. Sims on ?to criticize the critics?, by Peter C. B. 

   - Phillips,” _Journal of Applied Econometrics_ , Vol. 6, No. 4, pp. 423–434. 

   - (1993) “A Nine-Variable Probabilistic Macroeconomic Forecasting Model,” in _Busi-_ 

   - _ness Cycles, Indicators and Forecasting_ : National Bureau of Economic Research, Inc, pp. 179–212. 

   - (1996) “Inference For Multivariate Time Series Models With Trend,”Technical report, 

   - Princeton University, mimeo. 

   - (2000) “Using a likelihood perspective to sharpen econometric discourse: Three ex- 

   - amples,” _Journal of Econometrics_ , Vol. 95, No. 2, pp. 443–462. 

   - (2005a) “Conjugate Dummy Observation Priors for VARs,”Technical report, Prin- 

   - ceton University, mimeo. 

   - (2005b) “Dummy Observation Priors Revisited,”Technical report, Princeton Univer- 

   - sity, mimeo. 

   - (2010a) “Causal Ordering and Exogeneity,”Technical report, Princeton University, 

   - mimeo. 

   - (2010b) “Understanding Non-Bayesians,”Technical report, Princeton University, 

   - mimeo. 

- Sims, Christopher A and Harald Uhlig (1991) “Understanding Unit Rooters: A Helicopter Tour,” _Econometrica_ , Vol. 59, No. 6, pp. 1591–1599, November. 

- Sims, Christopher A. and Tao Zha (1998) “Bayesian Methods for Dynamic Multivariate Models,” _International Economic Review_ , Vol. 39, No. 4, pp. 949–68, November. 

59 

(1999) “Error Bands for Impulse Responses,” _Econometrica_ , Vol. 67, No. 5, pp. 1113– 1156, September. 

   - (2006) “Were There Regime Switches in U.S. Monetary Policy?” _American Economic_ 

   - _Review_ , Vol. 96, No. 1, pp. 54–81, March. 

- Stock, James H. and Mark W. Watson (2002) “Macroeconomic Forecasting Using Diffusion Indexes,” _Journal of Business & Economic Statistics_ , Vol. 20, No. 2, pp. 147–162. 

- Strachan, Rodney W. and Brett Inder (2004) “Bayesian analysis of the error correction model,” _Journal of Econometrics_ , Vol. 123, No. 2, pp. 307–325, December. 

- Theil, H. (1963) “On the Use of Incomplete Prior Information in Regression Analysis,” _Journal of the American Statistical Association_ , Vol. 58, No. 302, pp. 401–414. 

- Theil, H. and A. S. Goldberger (1961) “On Pure and Mixed Statistical Estimation in Economics,” _International Economic Review_ , Vol. 2, No. 1, pp. 65–78. 

- Tiao, George C. and Arnold Zellner (1964) “On the Bayesian Estimation of Multivariate Regression,” _Journal of the Royal Statistical Society. Series B (Methodological)_ , Vol. 26, No. 2, pp. 277–285. 

- Tierney, Luke (1994) “Markov Chains for Exploring Posterior Distributions,” _Ann. Statist._ , Vol. 22, No. 4, pp. 1701–1728, 12. 

- Timmermann, Allan (2006) “Forecast Combinations,” in G. Elliott, C. Granger, and A. Timmermann eds. _Handbook of Economic Forecasting_ , Vol. 1: Elsevier, Chap. 4, pp. 135–196. 

- Todd, Richard M. (1984) “Improving economic forecasting with Bayesian vector autoregression,” _Quarterly Review_ , Vol. 8, No. 4. 

- Uhlig, Harald (1994a) “On Jeffreys Prior when Using the Exact Likelihood Function,” _Econometric Theory_ , Vol. 10, No. 3-4, pp. 633–644. 

   - (1994b) “What Macroeconomists Should Know about Unit Roots: A Bayesian Per- 

   - spective,” _Econometric Theory_ , Vol. 10, No. 3-4, pp. 645–671. 

   - (1997) “Bayesian Vector Autoregressions with Stochastic Volatility,” _Econometrica_ , 

   - Vol. 65, No. 1, pp. 59–74, January. 

   - (2005) “What are the effects of monetary policy on output? Results from an agnostic 

   - identification procedure,” _Journal of Monetary Economics_ , Vol. 52, No. 2, pp. 381–419, March. 

- Villani, Mattias (2001) “Bayesian prediction with cointegrated vector autoregressions,” _International Journal of Forecasting_ , Vol. 17, No. 4, pp. 585 – 605. (2009) “Steady-state priors for vector autoregressions,” _Journal of Applied Economet-_ 

- _rics_ , Vol. 24, No. 4, pp. 630–650. 

- Waggoner, Daniel F. and Tao Zha (2012) “Confronting model misspecification in macroeconomics,” _Journal of Econometrics_ , Vol. 171, No. 2, pp. 167 – 184. Bayesian Models, Methods and Applications. 

- Wright, Jonathan H. (2009) “Forecasting US inflation by Bayesian model averaging,” _Journal of Forecasting_ , Vol. 28, No. 2, pp. 131–144. 

- Zellner, Arnold (1971) _An introduction to Bayesian inference in econometrics_ , Wiley Classics Library: Wiley-Interscience. 

60 

