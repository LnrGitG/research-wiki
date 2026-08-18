---
title: Koop_etal_JRSSA2019_UK_regional_nowcasting_using_a_mixed_frequency_Vector_Autoregressive
type: paper
source_pdf: raw/papers/Koop_etal_JRSSA2019_UK_regional_nowcasting_using_a_mixed_frequency_Vector_Autoregressive.pdf
converted: 2026-08-18
---

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

# UK Regional Nowcasting using a Mixed Frequency Vector Autoregressive Model with Entropic Tilting<sup>_∗_</sup> 

Gary Koop,<sup>_†_</sup> Stuart McIntyre<sup>_‡_</sup> and James Mitchell<sup>_§_</sup> 

Abstract: Output growth data for the UK regions are only available at the annual frequency and are released with significant delay. Regional policymakers would benefit from more frequent and timely data. We develop a stacked, mixed frequency Vector Autoregression (VAR) to provide, each quarter, nowcasts of annual output growth for the UK regions. The information we use to update our regional nowcasts includes output growth data for the UK as a whole, as these aggregate data are released in a more timely and frequent (quarterly) fashion than the regional disaggregates which it comprises. We show how entropic tilting methods can be adapted to exploit the restriction that UK output growth is a weighted average of regional growth. In our real time nowcasting application we find that the stacked mixed frequency VAR model, with entropic tilting, provides an effective means of nowcasting the regional disaggregates exploiting known information on the aggregate. 

> _∗_ Thanks to ESCoE for financial support; and to the Editor and three anonymous referees, ESCoE colleagues and Aubrey Poon for helpful comments on earlier drafts of this paper. Thanks to Jeffrey Darko and Trevor Fenton, at the ONS, for helping us retrieve historical ONS data. 

> _†_ Rimini Centre for Economic Analysis; Fraser of Allander Institute, Department of Economics, University of Strathclyde; Economic Statistics Centre of Excellence (gary.koop@strath.ac.uk) 

> _‡_ Fraser of Allander Institute, Department of Economics, University of Strathclyde; Economic Statistics Centre of Excellence (s.mcintyre@strath.ac.uk) 

> _§_ Warwick Business School, University of Warwick; Economic Statistics Centre of Excellence 

> (James.Mitchell@wbs.ac.uk) 

1 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

## **1 Introduction** 

The fact that official data for many key macroeconomic variables are released with delay sparks interest in nowcasting. Our particular interest is nowcasting nominal output growth for the regions of the UK. This is because regional output data, as measured by Gross Value Added (GVA), are currently available from the Office for National Statistics (ONS) only on an annual basis, with the initial release for a particular year currently occurring more than eleven months after the end of the year. But, for the UK as a whole, GVA data are released quarterly (in fact, since summer 2018, they have also been made available monthly) with a first estimate historically released by the ONS roughly two months after the end of the calendar quarter. We should note that while regional output is measured by GVA rather than Gross Domestic Product (GDP), the two concepts relate closely given that GVA plus taxes (less subsidies) on products equals GDP. 

The ONS have published, with a lag of at least eleven months, these annual estimates of nominal output for the regions of the UK since the late 1960s. They only began to publish real estimates in 2013; policy and media interest has therefore resided with the nominal regional GVA data, that are our focus in this paper. But their publication lags mean that the most up-to-date official information on growth in the regions of the UK can be nearly two years old by the time economists and policymakers make decisions and set policy; they are very much looking through the “rear-view mirror” (see Bean, 2007) unable to assess in a timely fashion the regional effects, for example, of the global financial crisis (as stressed by the Chief Economist at the Bank of England, see Haldane (2016)) or indeed monitor the of Brexit. 

There is a large(r) literature concerned with how best to nowcast or forecast an aggregate using disaggregated information (e.g. see Giacomini and Granger (2004) for theoretical discussion, and for applications nowcasting UK and Euro Area output growth see Bell, Co, Stone and Wallis (2014), Lui and Mitchell (2013) and Foroni and Marcellino (2014)). In contrast, our interest is nowcasting the regional disaggregates exploiting available data on the UK aggregate (and possibly other available indicators). Accordingly, our paper’s contribution is to develop methods to produce, and then evaluate the empirical utility of, quarterly nowcasts of low frequency (regional) output growth data that are updated within the year as new information about higher frequency variables, such as quarterly UK output growth, is released. This means policy and decision makers do not have to wait nearly a year to receive updated estimates of regional output growth. 

To provide these regional nowcasts, accommodating both the frequency mismatches between the available data and the increasingly large amounts of data that are available, we draw on and extend the growing literature on mixed frequency Vector Autoregressions (VARs). Alternatives to the VAR, including mixed frequency dynamic factor models (e.g. see Marcellino and Schumacher (2010), Mariano and Murasawa (2010) and Frale, Marcellino, Mazzi and Proietti (2011), have been used in other nowcasting applications (with Foroni and Marcellino (2014) offering a comparison). But we follow studies like Carriero, Clark and Marcellino 

2 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

(2015) and use the VAR. This choice is also supported by empirical evidence (from papers cited below) that VAR models can be effective nowcasting tools in practice. 

There are two main VAR modelling approaches and, in turn, timing conventions used in this literature. The first, often called the stacked VAR approach, can be classified as an “observation-driven” modelling approach (following Cox, 1981) and writes the VAR at the low frequency with the high frequency variables appearing multiple times in each period (i.e. if there are _R_ regions, then the dependent variables in the VAR will include the _R_ regional variables plus four UK quarterly values). The stacked VAR can also be interpreted as a multivariate analogue of the univariate unrestricted MIDAS model of Foroni, Marcellino and Schumacher (2015). Pioneering stacked VAR papers include Ghysels (2016), Carriero, Clark and Marcellino (2015) and McCracken, Owyang and Sekhposyan (2018). The second, which can be called the state space VAR approach, is instead a “parameter-driven” modelling approach (see Cox, 1981). It writes the VAR at the high frequency as a state space model with filtering used to fill in the missing observations driven by latent processes (see, e.g., Mariano and Murasawa (2010); Kuzin, Marcellino and Schumacher, 2011; Eraker, Chiu, Foerster, Kim and Seoane, 2015; Schorfheide and Song, 2015 and Brave, Butters and Justiniano, 2016). 

Our paper uses a stacked VAR and therefore does not rely on latent processes; this confers some computational advantages. That is, Bayesian analysis of models involving such latent processes is typically done using Markov Chain Monte Carlo (MCMC) methods with data augmentation. The computational burden associated with such methods can be avoided by working with the stacked VAR. However, our approach also deviates from conventional stacked VAR approaches in some important ways; and this requires the extension and adaptation of existing methods. A conventional stacked VAR approach typically exploits the information in many high frequency variables to update a single low frequency variable of interest (e.g. using many monthly macroeconomic variables to nowcast quarterly GDP growth). An exception is Ghysels, Grigoris and Ozkan (2017) which forecasts annual government expenditures and revenues for 48 US states using quarterly and monthly predictors. Another exception is Mandalinci (2015) which is a regional UK GVA application with a similar frequency mis-match to ours. Both these papers use different econometric methods than those we employ and have a different empirical focus. In our regional nowcasting application, the frequency mismatch is reversed. We have many low frequency variables to nowcast (i.e. GVA growth for _R_ UK regions) and a single high frequency indicator (i.e. quarterly UK GVA growth) of particular interest. Although, as we discuss below, other indicators can always be added into the model too, we expect this particular aggregate indicator to be of particular utility when nowcasting the disaggregates - given that it is the cross-sectional aggregation of the (regional) data that we are aiming to nowcast. Larger VAR models also raise additional empirical challenges. For example, if we had used the state space VAR when our data set had so many low (and possibly many high) frequency variables, the number of missing observations would be large and estimation burdensome. To-date, mixed-frequency applications of state-space VAR models, as referenced above, have confined their attention to a relatively 

3 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

small number of variables given their increased computational burden relative to the stacked VAR. 

To overcome these challenges and add some empirically useful features, we follow Carriero, Clark and Marcellino (2015) and McCracken, Owyang and Sekhposyan (2018) and use Bayesian methods which allow for prior shrinkage (with the degree of shrinkage estimated from the data) so as to avoid over-parameterisation problems in our relatively large stacked VAR. And given strong evidence of volatility changes in many conventional VAR macroeconomic forecasting applications (e.g. Clark, 2011), we follow Carriero, Clark and Marcellino (2015), in their mixed frequency nowcasting application, and add multivariate stochastic volatility into our stacked VAR. 

We then extend stacked VAR nowcasting methods in two main ways. These extensions let us handle, using the stacked VAR, both data subject to differential publication lags (often referred to as the ragged-edge) and the aggregation constraint. First, each quarter, as new timely releases of UK GVA data (and any other indicators) are received, we entropically tilt towards these new releases so as to produce updated density nowcasts of regional GVA which reflect this information. Secondly, we extend entropic tilting methods to exploit the fact that GVA growth for the UK as a whole should be (approximately, discussed further below) equal to a weighted average of regional GVA growth rates. Our approach, relative to alternative ways these two features could be accommodated in state-space VAR models with latent variables, benefits from being computationally simple and more readily extendable to large VAR contexts. And entropic tilting has established theoretical benefits, given that it imposes the constraints in an optimal way. 

Another contribution of this paper lies in the construction of a long time series of annual regional GVA data from 1966 to 2016 for the UK. The current regional nominal GVA dataset from the ONS only begins in 1997. Details of how we combine these data with earlier sources are provided in the Data Appendix. Aware of data revisions, our ambition in putting together the database was to use, as close as possible to (over our out-of-sample window), first-release estimates of regional GVA and match these with the appropriate, similarly dated, data release for UK GVA. This means that in producing our nowcasts we are estimating our models on (as close as possible to, as explained in the Data Appendix) first-release estimates and evaluating each nowcast relative to the ONS’s first estimate of regional GVA. Clements and Galvao (2013) have advocated a similar use of ‘lightly revised’ data instead of using data from the latest-available (real-time) vintage. 

Using these data and the stacked VAR, we carry out a real-time nowcasting exercise. At the beginning of each year, we provide unconditional (with respect to current year information) density forecasts of regional GVA growth for each region for the current year. These forecasts do, however, condition on data from previous years; and to acknowledge the publication lags of the regional data they are in effect two-year ahead forecasts, rather than just one year ahead, until late in the current year when the previous year’s regional data are published. Then, as each quarter of the current year passes by, and new UK-wide GVA data 

4 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

are released, we produce nowcasts of regional GVA growth which update the unconditional forecasts using entropic tilting methods. We find that these updated nowcasts are much more accurate than the initial unconditional forecasts, in terms of anticipating the ONS’s subsequent first releases for regional GVA growth. This provides evidence that the methods developed in this paper can be used to produce quarterly ‘flash’ (i.e. pre ONS first release) estimates of regional GVA growth where currently only annual estimates are available. They let us allocate national growth among the regions of the UK as soon as the quarterly UK figures are published, enabling the production of much more timely estimates of regional GVA growth. For instance, at the end of May 2017 we could already produce a nowcast of regional GVA growth for 2017, conditioning on 2017Q1 UK GVA data. The actual initial release of 2017 regional GVA by the ONS will not be until mid December 2018. In the time between May 2017 and December 2018, our nowcasts might be found useful by a regional policymaker in giving an early and reliable signal of the state of the economy in their region. 

Methodological improvements at national statistical offices are of course an ongoing process, and their official estimates are to be preferred over model-based ones. Therefore, while it is anticipated that 2019 will see the ONS starting to produce ‘Regional Short Term Indicators’ at the quarterly frequency, the methods developed in this paper will remain relevant - given that these new regional data from the ONS will still be published with a delay of 3 to 4 months. So, in time (as these new data accumulate, and their historical coverage improves facilitating model estimation), one can imagine the methods developed in this paper being used again, perhaps at the monthly frequency exploiting the ONS’s new monthly estimates of UK output growth too. Similar issues are faced in other countries, as Stock (2005) emphasises: “an important practical challenge facing regional economists is combining...different sources of data to provide a timely and accurate measure of regional economic activity”. Therefore, we also imagine the methods developed in this paper having wider applicability. For example, currently in the US while the Bureau of Economic Aanalysis produce their ‘advance’ US-wide quarterly GDP estimate about one month after the end of the quarter, quarterly state domestic product data are published three months later. 

## **2 The Econometrics of Regional Nowcasting** 

Our goal is to build an econometric model for nowcasting regional output growth using mixed frequency data comprising annual observations for the regions and quarterly observations for the UK as a whole; although, as we discuss below and consider in the empirical application, other quarterly indicators, that empirically may help explain regional growth, can also be added into the model in a relatively straightforward manner. 

Our nowcasts will be of annual growth rates, but they will be updated quarterly using entropic tilting methods. In this section, we first describe the stacked VAR we use. Next we describe the prior used to achieve prior shrinkage and avoid over-parameterisation concerns. Subsequently, we describe predictive and posterior inference in the model. Finally, we 

5 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

describe how we implement the entropic tilting. 

### **2.1 The Stacked VAR** 

First, we define our notation: 

- _r_ = 1 _, .., R_ is an index for the UK regions. 

- _t_ = 1 _, .., T_ is an index for time at the _annual_ frequency. 









Note that we are not approximating the percentage growth rate using log differences. The use of log differences would entail slight changes in our entropic tilting formulae and, in particular, to the weights in (20) below. 

The stacked VAR is a VAR (at the annual frequency) using 



as the vector of dependent variables where _yt_<sup>_A_=</sup> _yt_<sup>1</sup><sup>_,A_</sup> _, .., yt_<sup>_R,A_</sup> stacks all the annual vari� � ables into vectors. In words, this approach stacks GVA growth for all the regions along with the four quarterly values for UK GVA growth into a vector which contains the dependent variables in a VAR. As we consider further below, in section 3.1 of the empirical application, other variables (e.g. regional labour market data and sectoral GVA growth data) can also be added to _yt_ - in the hope that these indicators help deliver improved nowcasts for regional GVA growth, _yt_<sup>_r,A_</sup> . These additional indicator variables could be quarterly or annual, and measured at the regional, sectoral and/or aggregate levels. It is ultimately, assuming data availability for these indicator variables, an empirical question whether and, if so, what additional indicator variables help explain and nowcast regional GVA growth. Our methodology is in principle applicable irrespective of this; and for ease, but without loss of generality, in setting out our methodology below we focus on the more parsimonious VAR model where _′ yt_ = � _yt,_<sup>_UK_</sup> 1<sup>_, y_</sup> _t,_<sup>_UK_</sup> 2<sup>_, y_</sup> _t,_<sup>_UK_</sup> 3<sup>_, y_</sup> _t,_<sup>_UK_</sup> 4<sup>_, y_</sup> _t_<sup>_A_</sup> � . While consideration of a larger VAR increases the computational costs of estimating our model, in principle the Bayesian methods we use, as in Banbura, Giannone and Reichlin (2010) and the subsequent ‘large Bayesian VAR’ literature, 

6 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

mean our modelling approach and use of entropic tilting is both applicable and feasible even when many additional indicators are considered. In sub-section 3.1.1, we do consider such a larger VAR with more indicators. However, our main focus is on showing how entropic tilting methods can be used to exploit the constraint that UK output growth is (approximately) a weighted average of regional growth to produce more accurate nowcasts. Thus, our main results are for a VAR involving only GVA data. 

The reduced form version of the stacked VAR with _P_ lags is written as: 



where _B_ 0 is a vector of intercepts. The stacked VAR is often written as a structural VAR which imposes a sequential ordering on the high frequency variables (see, e.g., McCracken, Owyang and Sekhposyan, 2018). To do impulse response analysis, such an ordering is required. But for unconditional forecasting, it is acceptable to use an unrestricted reduced form (see the discussion in section 2.3 of Ghysels, 2016). In this paper, we use the stacked VAR to produce unconditional forecasts which are then entropically tilted. Hence, we work with this reduced form VAR. Given that, as discussed further in section 2.3, the weighted sum of the four quarterly UK growth rates approximately equals the weighted sum of the regional growth rates, the covariance matrix of our model is close to singular; but this presents no particular difficulties in estimation itself, given our Bayesian approach and the prior/shrinkage or regularisation implied. That is, even if the error covariance matrix were singular (which it is not), the posterior and predictive densities are proper. Given that we wish to nowcast all the disaggregates using known information on the aggregate, our approach to imposing the aggregation constraint is attractive relative to the alternative of avoiding singularities by eliminating one of the disaggregates from the model. 

We consider homoskedastic and heteroskedastic versions of the model, (2). The former assumes _εt_ to be i.i.d. _N_ (0 _,_ Σ). The heteroskedastic version of this model uses the specification of Cogley and Sargent (2005) which replaces the Σ of the homoskedastic model by Σ _t_ which is written as: 



where _A_ is a lower triangular matrix with ones on the diagonal. _Dt_ is a diagonal matrix with diagonal elements _σit_<sup>2whichareassumedtofollowunivariatestochasticvolatilityprocesses.</sup> That is, 



where 



with _vit_ i.i.d. _N_ (0 _, φi_ ). The homoskedastic specification is obtained if _φi_ = 0 for all _i_ . 

Note that we are working with annual data which means the sample will be short. And, since the dimension of _yt_ is _N_ = _R_ + 4 we are working with a fairly large VAR. With large 

7 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

VARs such as this, it is common to use Bayesian methods so as to allow for prior shrinkage to overcome the problems associated with a shortage of data information. 

### **2.2 Bayesian Analysis with the Stacked VAR** 

With large VARs, Bayesian methods using the Minnesota prior are commonly used (see, among many others, Banbura, Giannone and Reichlin, 2010) and we follow this practice with our mixed frequency VAR. However, following Giannone, Lenza and Primiceri (2015), we estimate the prior shrinkage parameters from the data. In this sub-section, we provide details (see also Dieppe, Legrand and van Roye, 2016, section 3.3). 

We begin with the homoskedastic version of the model. The Minnesota prior replaces Σ by Σ<sup>�</sup> which is the OLS estimate from the stacked VAR. Thus, we need only worry about the prior for the VAR coefficients. Let _β_ be the _N ×_ ( _NP_ + 1) vector containing all the VAR coefficients. The Minnesota prior is _N_ � _<u>β, V</u>_ � with particular choices for _<u>β</u>_ and _<u>V</u>_ . These can be explained by noting that the VAR coefficients can be divided into three categories: i) own lags (i.e. lags of dependent variable _i_ in equation _i_ ), ii) other lags (i.e. lags of dependent variable _i_ in equation _j_ for _i_ = _j_ ) and iii) exogenous variables such as the intercept. The prior mean vector, _<u>β</u>_ , is set to zero except for first own lag coefficients which are set to _b_ . We consider a grid of values within the interval _b ∈_ [0 _._ 1 _,_ 1 _._ 0] with a step size of 0.05 and estimate _b_ . 

The prior covariance matrix, _<u>V</u>_ , is a diagonal matrix with diagonal elements specified as follows: 

- Prior variances for coefficients on own lags at lag _l_ are: 



- Prior variances for coefficients on the _l_<sup>_th_</sup> lag of the _j_<sup>_th_</sup> variable in the _i_<sup>_th_</sup> equation are: 



- The prior variance for the intercept is: 



In these expressions, _s_<sup>2</sup> _i_<sup>istheOLSestimateoftheerrorvariancefromaunivariateautore-</sup> gressive model for the _i_<sup>_th_</sup> variable. 

We estimate the shrinkage parameters. For _λ_ 1, which controls overall shrinkage, we use the grid of values in the interval [0 _._ 05 _,_ 0 _._ 3] with a step size of 0.01. For _λ_ 2 which controls 

8 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

other lag shrinkage, we use the grid of values in the interval [0 _._ 1 _,_ 3] with a step size of 0.05. For _λ_ 3 which controls the rate that shrinkage increases on longer lag lengths, we use a grid of values in the interval [1 _,_ 2] with step size 0.2. For _λ_ 4 we use a grid over the interval [100 _,_ 1000] with step size 100 which implies a very non-informative prior. All these intervals contain the benchmark recommendations of Dieppe, Legrand and van Roye (2016) within them; and we did not obtain estimates at any of the boundaries of our grids indicating that they are sufficiently wide. 

For the heteroskedastic version of the model we use the prior just described for the VAR coefficients, but additionally require a prior for the parameters controlling Σ _t_ . These are _A_ , _γ_ and _φi_ and _hi_ 0 for _i_ = 1 _, .., N_ . We set _γ_ = 0 _._ 85 and let each free element of the lower triangular matrix _A_ have a non-informative prior. For _φi_ we use relatively non-informative inverse Gamma priors: 



As a general comment about prior specification, we have done extensive experimentation with various choices from the range of priors available in the BEAR Toolbox of Dieppe, Legrand and van Roye (2016). We have also experimented with different lag lengths. The specification and prior choices used in this paper are those which yield the highest marginal likelihoods. This led us to work with the Minnesota prior and set the lag length, _P_ , to one. 

We remind the reader that analytical posterior results are available for the homoskedastic version of the model. But when we allow for stochastic volatility computationally demanding MCMC methods are required. Our method for the estimation of shrinkage parameters requires MCMC methods to be repeatedly used at every possible combination of values for our shrinkage parameters. By having 4 shrinkage parameters, the number of combinations considered is 2<sup>4</sup> . This is already more flexible that most of what is done in the existing literature (e.g. Banbura, Giannone and Reichlin (2010) only have one shrinkage parameter). It would be possible to have additional shrinkage parameters (e.g. to give lags of UK GVA data a different treatment than regional GVA variables) or to have more refined grids, but computation would increase commensurately. 

Posterior and predictive analysis can be done using standard Bayesian MCMC methods and we use the BEAR toolbox to do so (see Dieppe, Legrand and van Roye, 2016). The main output will be draws from the one-step (and two-step) ahead predictive densities. For future reference, we will denote the predictive density of _yτ_ +1 given all the information available at time _τ_ by _p_ ( _yτ_ +1 _|Dataτ_ ), where _Dataτ_ denotes all the data available to the forecaster at the end of period _τ_ . Given the aforementioned publication lags associated with the regional data, such that in the UK regional GVA data for year _τ_ are not currently available until near the end of year _τ_ + 1, the predictive density of interest, _p_ ( _yτ_ +1 _|Dataτ_ ), is in effect produced as a two-year ahead forecast from the stacked VAR until the regional data for year _τ_ are published in December of year ( _τ_ + 1). That is, until late in year ( _τ_ + 1), rather than contain data for year _τ_ , _Dataτ_ in fact contains regional GVA data dated year ( _τ −_ 1) and earlier. 

9 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

### **2.3 Entropic Tilting Using Quarterly Releases of UK Data** 

The previous sub-section described how to produce unconditional (with respect to current year information) forecasts using annual data. Given the (as of the time of writing this paper) nearly one year delay in releasing regional GVA data, these forecasts, _p_ ( _yτ_ +1 _|Dataτ_ ), can be used as nowcasts for the year. However, we want to update these nowcasts throughout year ( _τ_ + 1) as new information on UK GVA, and any other indicators, is released each quarter. We will do so using entropic tilting methods as described in this sub-section. 

The standard stacked VAR defined by (2) captures the general property that quarterly GVA growth data for the UK as a whole (or indeed any additional indicators) might help nowcast regional GVA growth, since lags of UK GVA growth (or any additional indicators) appear on the right hand side of the equation for each region and the VAR error covariance matrix allows for contemporaneous correlations between the equations for regional GVA growth and that of the UK as a whole. This structure means that if we update UK GVA figures as they are released after each quarter, the regional GVA growth figures will also be updated. If, for instance, an unexpectedly favourable outcome for UK GVA growth occurs in the first quarter of a year, this is a strong signal that growth in most or all UK regions has also increased. It is desirable to incorporate this information now (i.e. after the first quarter value of UK GVA has been released) and update the estimates of regional GVA throughout the year rather than waiting for the release of regional GVA data. The interlinkages built into the VAR allow us to do this. However, this assumes a balanced dataset. In practice, as the quarterly UK GVA data, and any additional indicators, arrive sequentially throughout year ( _τ_ + 1) we have a “ragged-edge” with current quarter/year values known for some indicators but not others. We will show how entropic tilting can be used to update the unconditional density forecast (produced from the balanced dataset, _Dataτ_ ) as these new data arrive through year ( _τ_ + 1). An alternative, practical way of modifying the stacked VAR model to accommodate differential publication lags of any additional indicators, is simply to include leads of them in the VAR. However, as we go onto explain, this is less attractive when handling the UK GVA data themselves - that we anticipate are an important, and stable, indicator for regional GVA - given that we also wish to modify the stacked VAR to reflect the reality that these regional data (spatially) sum, at a given point in time, to the (temporal) sum of the four quarterly UK-wide estimates. 

But there is a second way that the quarterly releases of UK GVA data can be used to shed light on what is happening in the regions. This is through what we call the cross-sectional restriction. This restriction, as just discussed, embodies the fact that GVA growth for the UK as a whole is a weighted average of regional growth rates. In this sub-section, we discuss how to incorporate these types of information in the context of the stacked VAR using entropic tilting methods. 

Increasingly, macroeconomic forecasters want to move beyond unconditional forecasts to incorporate extra information or restrictions on their forecasts (see, among many others, Alessi, Ghysels, Onorante, Peach and Potter, 2014, and Kr¨uger, Clark and Ravazzolo, 2017) 

10 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

such as our cross-sectional restriction. Conditional forecasting and entropic tilting are two ways of doing this. A previous literature in statistics dating back to Deming and Stephan (1941), with Bryon (1978) and Smith, Weale and Satchell (1998) developing the statistical theory, imposes constraints using least squares methods and focuses on the mean as opposed to the entire predictive density as here. 

The idea of (“hard”) conditional forecasting (see Waggoner and Zha, 1999) is that you impose this condition exactly on the forecasts. This is increasingly done by policymakers in, for example, central banks. For instance, the policymaker may be interested in forecasts of inflation for different interest rate paths. An unrestricted VAR for inflation, the interest rate and other variables would provide unrestricted forecasts of inflation. Conditional forecasting procedures would allow, for instance, for a forecast of inflation conditional on the interest rate remaining at 0.5%, another forecast conditional on the interest rate being raised to 0.75%, etc. And more relevantly for us, in their nowcasting application using a stacked VAR, McCracken, Owyang and Sekhposyan (2018) show how nowcasts of quarterly US GDP growth can be produced and updated within-quarter via conditional forecasting methods as highfrequency indicator data are released throughout the quarter. “Hard” conditional forecasting methods impose the restriction exactly. That is, in a predictive simulation algorithm which provides draws (call them _yτ_<sup>(</sup><sup>_s_</sup> +1<sup>)for</sup><sup>_s_= 1</sup><sup>_, .., S_)fromthepredictivedensity,everysingledraw</sup> will satisfy the restriction. This contrasts with entropic tilting (that relates to the “soft” conditioning approach of Waggoner and Zha, 1999) where only the predictive mean (or other predictive moments specified by the researcher) will satisfy the constraint. 

In this paper we use entropic tilting since we expect the cross-sectional restriction to hold only approximately and, thus, we do not wish to impose it exactly as in (“hard”) conditional forecasting (or least squares methods). In our case, this cross-sectional relationship is approximate since the GVA data for the regions that we use do not exactly add up to UK GVA because of measurement error (see the Data Appendix) and because our main results exclude GVA produced in the UK continental shelf (UKCS). UKCS data are dominated by the activities of the UK oil and gas sector. 

As Table 5 shows, the UKCS data exhibit volatile behaviour that is also inconsistent with how the other regions relate to UK GVA. As a result, for our main results, we do not include UKCS in _yt_<sup>_A_forfearofcontaminatingtherelationshipbetweentheotherUKregionsand</sup> UK GVA with potentially deleterious effects on the accuracy of the nowcasts. However, as it is ultimately an empirical matter what works best, we also present results which do include UKCS in _yt_<sup>_A_.Inbothcases,UKCSremainspartof</sup><sup>_y_</sup> _t,q_<sup>_UK_;i.e.theUKGVAfiguresthatwe</sup> condition the regional nowcasts on include the UKCS. This means that for those VARs that exclude UKCS in _yt_<sup>_A_thisisanadditionalreason,tomeasurementerror,whyweexpectthe</sup> cross-sectional relationship to hold only approximately. Note that it is not possible to remove UKCS activity from the overall estimates of UK quarterly GVA and then entropically tilt towards that estimate. While some sectoral detail for GVA is available for the UK as a whole on a more timely basis, not all Oil and Gas related activity in the UK ‘Mining & quarrying 

11 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

including oil and gas extraction’ sector is activity which takes place in the UKCS. Some of this activity relates to onshore activity in support of activity in the UKCS. Similarly, not all of the activity in this sector relates to oil and gas extraction. It would therefore not be appropriate to treat the ‘Mining & quarrying including oil and gas extraction’ sector as synonymous with the UKCS activity series. 

The idea of entropic tilting is to produce a new predictive density, 

_p_<sup>_∗_</sup> ( _yτ_ +1 _|Dataτ_ ), which has a mean which satisfies the restriction but is in all other respects as close as possible to _p_ ( _yτ_ +1 _|Dataτ_ ). “As close as possible” is defined according to the Kullback-Leibler Information Criterion (KLIC) which is a measure of the relative entropy of _p_<sup>_∗_</sup> ( _yτ_ +1 _|Dataτ_ ) to _p_ ( _yτ_ +1 _|Dataτ_ ). So, in our case, the predictive mean (i.e. the point forecast) produced by _p_<sup>_∗_</sup> ( _yτ_ +1 _|Dataτ_ ) will satisfy the restrictions but otherwise the predictive density will be as close as possible to the unrestricted predictive density produced by the stacked VAR. 

We use results based on a Normal approximation. Conditional on the parameters of the model, the predictive density from our model is Normal. The unconditional predictive density integrates out the parameters and, thus, is no longer Normal but is likely to be nearly so. Assume that the unrestricted predictive density is Normal: 



and break down the parameters into UK and regional blocks as follows: 



The estimation procedure of the preceding sub-section will provide _µ_ and _V_ . 

Now suppose that we want to tilt the multivariate predictive density so that the mean of some variable (or set of variables) is fixed (e.g. so as to set the predictive mean of _yτ_<sup>_UK_</sup> +1<sup>to</sup> _µ_<sup>_∗_</sup> _UK_<sup>where</sup><sup>_µ∗_</sup> _UK_<sup>is chosen to reflect period</sup><sup>_τ_+1 UK-wide information that has come available</sup> before the _τ_ + 1 regional data are released), but otherwise we want to leave the predictive density to be as close to _p_ ( _yτ_ +1 _|Dataτ_ ) as possible. It can be shown (see, e.g., Altavilla, Giacomini and Ragusa, 2017) that the tilted predictive density is: 



where _V_<sup>_∗_</sup> = _V_ (i.e. tilting does not change the predictive variance) and 



Note that this type of entropic tilting relates to UK variables since this is what is being released throughout the year. Thus, it may appear that it does not directly impact on the regional growth nowcasts. But this appearance is incorrect since _µR_ = _µ_<sup>_∗_</sup> _R_<sup>.Theintuitionis</sup> 

12 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

that, unless _VUK,R_ = 0 and the UK nowcasts are uncorrelated with the regional nowcasts, the updating of UK GVA nowcasts will spill over into the regional nowcasts. Note that cross-region dependencies are captured via _VR_ . 

But we also want to tilt toward the cross-sectional constraint which does directly relate to the regional growth nowcasts. To add the latter restriction, we extend the conventional result given in (12). To this end, we define a new variable _z_ = _Ayt_ +1. The properties of the multivariate Normal distribution imply 



for any _M × N_ matrix _A_ . If we set 



where _w_ = (0 _,_ 0 _,_ 0 _,_ 0 _, w_ 1 _,t−_ 1 _, .., wR,t−_ 1) and _wr,t−_ 1 for _r_ = 1 _, .., R_ are region-specific weights to be defined below, then _z_ contains the weighted average of the nowcasts of regional GVA growth as its first element, followed by the four quarterly UK GVA growth nowcasts, followed by the _R_ regional nowcasts. 

We apply the entropic tilting formula of (12) to _z_ . To this end, let _µ_<sup>_†_</sup> = _Aµ_ and _V_<sup>_†_</sup> = _AV A_<sup>_′_</sup> where 



and assume that the tilting restrictions are _µ_<sup>_†_</sup> 1<sup>=</sup><sup>_µ∗_</sup> 1<sup>.Let</sup><sup>_z†_denotethetiltedversionof</sup><sup>_z_.</sup> Then the same derivations used to find (12) can be used to show that: 



where 



Note that _V_<sup>_†_</sup> will be a singular matrix, but this causes no problem for our derivations as they only involve inverting _V_ 11<sup>_†_(whichisnon-singular)andweareonlyinterestedinthe</sup> tilted predictive densities for the regional GVA variables which have predictive covariance matrix _V_ 22<sup>_†_(whichisnon-singular).</sup> 

The preceding material described the general motivation and formulae relating to entropic tilting. To describe the precise way we implement it (i.e. the exact choice for _µ_<sup>_∗_</sup> 1<sup>),wefirst</sup> define the temporal and cross-sectional constraints we will use. These results arise from the fact that annual UK GVA, _Yt_<sup>_UK_</sup> , can be written in two different ways: 





This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

In growth rates, this implies 



where _yt,q_<sup>_UK_</sup> is UK growth relative to the previous year and the _w_ ’s are the weights. Now imagine we know _yt_<sup>_UK_</sup> +1 _,_ 1<sup>i.e.UKgrowthinthefirstquarterofyear(</sup><sup>_t_+ 1).Wewish</sup> to impose this information when nowcasting, but _yt_<sup>_UK_</sup> +1 _,_ 2<sup>_, y_</sup> _t_<sup>_UK_</sup> +1 _,_ 3<sup>_, y_</sup> _t_<sup>_UK_</sup> +1 _,_ 4<sup>arestillunknown.We</sup> therefore assume, when tilting to reflect the cross-sectional constraint, that _yt_<sup>_UK_</sup> +1 _,_ 2<sup>=</sup><sup>_y_</sup> _t_<sup>_UK_</sup> +1 _,_ 3<sup>=</sup> _yt_<sup>_UK_</sup> +1 _,_ 4<sup>=</sup><sup>_y_</sup> _t_<sup>_UK_</sup> +1 _,_ 1<sup>i.e.growthcontinuesthroughyear</sup><sup>_t_+ 1attherateseeninthefirstquarter.</sup> Given that our data are seasonally adjusted, the assumption of constant growth throughout the year is the most reasonable one and, as we shall see, it works well empirically. This implies we tilt to reflect 



Now assume we know _yt_<sup>_UK_</sup> +1 _,_ 1<sup>and</sup><sup>_y_</sup> _t_<sup>_UK_</sup> +1 _,_ 2<sup>andagainassumegrowthcontinuesatthemost</sup> recent quarterly rate through the remainder of the year. This means we now tilt to reflect: 



_R_ Noting that the first element of _µ_<sup>_∗_</sup> 1<sup>willrelatetothevariable</sup> � _wr,tyt_<sup>_r,A_</sup> +1<sup>,thefollowing</sup> _r_ =1 summarises how we proceed as we update our nowcasts using entropic tilting as new UK data (Q1 to Q4, i.e. _yτ_<sup>_UK_</sup> +1 _,_ 1<sup>to</sup><sup>_y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 4<sup>)arereleased:</sup> 





This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

2. After Q2 release (in August of each year) set: _′_ 

_µ_<sup>_∗_</sup> 1<sup>=</sup> �� _w_ 1<sup>_uk_</sup> _,τ_<sup>_y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 1<sup>+ 3</sup><sup>_w_</sup> 2<sup>_uk_</sup> _,τ_<sup>_y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 2� _, yτ_<sup>_UK_</sup> +1 _,_ 1<sup>_, y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 2� . 

3. After Q3 release (in November of each year) set: _′_ 

_µ_<sup>_∗_</sup> 1<sup>=</sup> �� _w_ 1<sup>_uk_</sup> _,τ_<sup>_y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 1<sup>+</sup><sup>_w_</sup> 2<sup>_uk_</sup> _,τ_<sup>_y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 2<sup>+ 2</sup><sup>_w_</sup> 3<sup>_uk_</sup> _,τ_<sup>_y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 3� _, yτ_<sup>_UK_</sup> +1 _,_ 1<sup>_, y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 2<sup>_, y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 3� . 

4. After Q4 release (in February of each year) set: _′_ 

_µ_<sup>_∗_</sup> 1<sup>=</sup> � _yτ_<sup>_UK_</sup> +1<sup>_, y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 1<sup>_, y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 2<sup>_, y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 3<sup>_, y_</sup> _τ_<sup>_UK_</sup> +1 _,_ 4� . 

In fact, since prior to release of the Q4 data for year _τ_ + 1 the regional GVA data for year _τ_ are not yet available (since 2005 the regional data have been published in December of each year), and so as to respect this publication lag and produce genuinely real-time nowcasts, we condition our Q1 to Q3 nowcasts on 2-year rather than 1-year ahead (unconditional) density forecasts from the VARs. While this does not affect how we condition the regional nowcasts on within-year ( _τ_ + 1) data for the UK, as detailed in 1. to 4. above, for the Q1 to Q3 nowcasts we consider an augmented _A_ matrix and an augmented _µ_<sup>_†_</sup> vector, see (23) below, that let us impose the additional cross-sectional constraint that the regional data for year _τ_ , while now forecast rather than assumed known as in Q4, are consistent with known UK data for (the previous) year _τ_ that are available from when the Q1 nowcast is made for year _τ_ +1. 



## **3 Empirical Results** 

In this section, we examine the performance of our nowcasting methods using data from 1967-2016. We continue to use quarterly UK GVA growth data and annual GVA growth data for either 9 UK regions or 10 if we include UKCS; i.e. we continue to focus in these baseline empirical results on stacked VAR models in _yt_ , as defined in equation (1), before we turn to consideration of larger VAR models, with additional indicator variables, in section 3.1 below. 

15 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Figure 1: GVA Growth for the UK Regions (in %: 100 _× yt_<sup>_r,A_</sup> ) 



<!-- Start of picture text -->
35<br>North<br>Yorkshire & Humber<br>30 East Midlands<br>London & SE<br>South West<br>West Midlands<br>25 Wales<br>Scotland<br>Northern Ireland<br>20 UK<br>15<br>10<br>5<br>0<br>-5<br>1970 1975 1980 1985 1990 1995 2000 2005 2010 2015<br>Year<br>Percentage<br><!-- End of picture text -->

Definitions of these regions and further details of the data are given in the Data Appendix. It is worth reiterating that in this empirical exercise we use, as closely as possible, first release GVA estimates in our model, and compare our nowcasts to these same data (plotted in Figure 1). In this way our empirical exercise is as near as possible real-time. The key question of interest is whether the entropic tilting using timely, quarterly, UK-wide data will improve the nowcasts of (ONS first release) regional GVA data. This is the question we will focus on in this section To evaluate the nowcasts from the VAR models, we use a variety of standard measures of forecast performance. In particular, we use root mean squared forecast errors (RMSFE) to evaluate the quality of the point nowcasts. The evaluation of the accuracy of the entire predictive density uses log predictive scores (LPS) and the continuous ranked probability score (CRPS). See Appendix A.10 of Dieppe, Legrand, and van Roye (2016) for definitions of all these nowcast (forecast) evaluation metrics. We report these results for the VAR models relative to the (2-year ahead density) forecasts from AR(1) models (with Normal errors). These models simply take the annual regional data for each region individually and use ordinary least squares (OLS) methods; but given the aforementioned publication lags we use 2-year ahead forecasts. Comparison against a univariate benchmark enables us to assess the utility in our VAR models of conditioning the regional nowcasts on within-year UK data exploiting inter-regional dynamics. While arguably the most common forecasting benchmark in applied macroeconomics, with some attractive robustness properties in the presence of structural breaks (e.g. see Clements and Hendry, 1999), we examine the sensivity of our 

16 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

results to this specific choice for the benchmark model in section 3.1 below by considering a more sophisticated mixed frequency univariate benchmark. 

To aid in interpretation, note that relative values for the CRPS and RMSFE measures less than unity indicate that there are forecast gains associated with use of our VAR models; these _relative_ values are calculated as the CRPS or RMSFE from our nowcasting model divided by the CRPS or RMSFE from the benchmark model. For the LPS we subtract the LPS for the benchmark model from those for each of our VAR models; positive values now therefore indicate improved forecast accuracy, relative to the univariate benchmark and are similar to a Bayes factor (except that the Bayes factor is an evaluation of predictive performance over the entire sample). With Bayes factors a common rule of thumb (see Kass and Raftery, 1995) is that there is strong evidence in favour of one model over another if the log Bayes factor is greater than 3. The reader is advised to keep this value in mind when comparing LPS results from different approaches. 

Our nowcast evaluation period begins in 2006. Our methods are recursive, and involve repeated re-estimation of our models. That is, we do a real-time out-of-sample nowcasting exercise using an expanding window of data beginning in 2006. 

Tables 1 and 2 present these three forecast metrics, relative to the AR model, for the 9 UK regions for the homoskedastic and heteroskedastic stacked VARs. Tables 3 and 4 repeat the analysis using 10 regions, where UKCS is included in the stacked VAR. The final row of each panel of each table presents an average (for RMSFE and CRPS) or sum (for LPS) over all regions. As one moves from left to right in the tables, the forecasting metrics reflect more and more information. The first column of numbers in each table is based on unconditional nowcasts (i.e. 2-year density forecasts from the VARs). In all these tables, it can be seen that, except on one occasion if interested in nowcasting the UKCS, incorporating new information on UK GVA (as it accumulates each quarter) via our entropic tilting methods, produces more accurate nowcasts. That is, substantial decreases in RMSFEs and CRPSs and increases in LPSs, relative to the AR benchmark, are observed as we move through the year. For instance, in Table 1 we find that the average (across regions) of the RMSFEs is almost half as small by the end of the year as it was at the beginning (i.e. it drops from 0.97 to 0.49 as we move through the year). Thus, overall, the point forecasts are improving substantially. The LPS results show that similar improvements occur for the entire predictive density. For instance, in Table 1 the sum of the LPSs over all regions increases from 0.79 to 6.54, which is _strong_ evidence in favour of conditioning on UK GVA values bearing in mind that log Bayes factors greater than 3 are generally seen as strong. The gains are also strong using the CRPSs with, in Table 1, the average over all regions dropping from 0.93 to 0.48 and the average CRPS dropping from 0.85 to 0.55 in Table 2. Interestingly most of the gains in nowcast performance are found after the first quarter of UK GVA data are released. Thus, nowcasts produced as early as May by our stacked VAR approach are appreciably better than the unconditional nowcasts that would have been produced in February. There are nevertheless modest gains seen, on average in Table 1, as quarterly information accrues through the year with the RMSE 

17 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

and CRPS ratios declining and the LPS differences increasing. Interestingly, conditioning on the Q4 release does not help much; this is despite the fact that it is only with this Q4 release of UK GVA that the regional data for the previous year become available, so that we can condition on a 1 rather than a 2-year (unconditional) density forecast from the VAR. 

The fact that our four tables are producing similar results offers reassurance that our results are robust to changes in specification and in data. We note that there is little evidence that inclusion of stochastic volatility is important in this application, perhaps related to our use of yearly rather than higher frequency forecasts. It is true that, if we use conventional model comparison measures using the unconditional forecasts, the inclusion of stochastic volatility does lead to slight improvements relative to the homoskedatic model. For instance, the sum of the log predictive scores is 1.04 in Table 2 (which includes stochastic volatility) and 0.79 in Table 1 (which does not). A similar pattern can be found if we compare Tables 3 and 4. However, when we look at the entropically tilted nowcasts, the homoskedastic version of the model tends to do better. For instance, the sum of log predictive scores using tilted nowcasts with 4 quarters of UK GVA growth is 6.54 in Table 1 but only 4.54 in Table 2. 

A comparison of Tables 3 and 4 with Tables 1 and 2 indicates that including UKCS as a region does not tend (with a few exceptions) to lead to any improvements in nowcast performance for the 9 other UK regions. For instance, the best overall summary of evidence is probably the sum of the log predictive scores for the 9 UK regions; and for this a comparison of Table 1 and Table 3 indicates that including UKCS leads to a rise of 0.12 in the unconditional forecast case, but reductions in the log predictive scores across the other four nowcasts (relative to the AR benchmark). On this basis, we conclude that omitting UKCS is not harmful and take the homoskedastic mixed frequency VAR with nine regions as being our preferred specification to look at in more detail. We are not surprised by this result, given the distinct (univariate) time series properties of UKCS relative to the other regions of the UK as summarised in Table 5. 

If we look at the individual regions, they uniformly exhibit the same patterns noted above. As new information about UK GVA is released (on a quarterly basis) it clearly is helping to improve nowcasts for every region. These (relative) nowcast improvements are particularly large for London and the South East. This is not surprising, since this region comprises a large share of UK GVA; and, as Table 5 shows, it is (in-sample) the most correlated English region with UK GVA growth. Following Pesaran (2006), UK GVA growth - as a cross-sectional average - can be interpreted as the common “factor” driving regional growth dynamics. But even for smaller regions (e.g. Scotland), we find nowcast improvements which are similarly large. This is consistent with these regions’ growth dynamics still being dominated by (common) UK dynamics, again as illustrated via the high correlations of regional GVA growth with UK GVA growth shown in Table 5. The weakest relative performance is for Northern Ireland. As seen in Table 5, GVA growth in Northern Ireland exhibits the lowest correlation with UK GVA at 0.8 compared with at least 0.9 for the other regions (with the exception of the UKCS). This suggests that GVA movements in Northern Ireland depend less on the 

18 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

common UK “factor” than in the other regions of the UK. But even for Northern Ireland, the nowcast metrics improve as new information on UK GVA growth is incorporated throughout the year; and the nowcasts are clearly more accurate than those from the AR benchmark (with gains of at least 20% across the three evaluation metrics). 

It can be seen that while there are often gains from using an unconditional multivariate forecasting method which allows information from different regions and the UK as a whole to inform the forecasts of a particular region, our unconditional forecasting metrics (i.e. without entropic tilting) do not always beat the AR(1) benchmark. London and the South East is a leading example in Table 1. It is only when entropic tilting is used that we see the more substantive gains. That is, when we use the additional quarterly UK data as it released throughout the year large gains are made relative to a simple univariate method. 

Tables 1 to 4 reflect average performance over our nowcast evaluation period. Figures 2 to 4 shed light on whether there are particular time periods when incorporating new information using our tilting methods is particularly important. These figures are based on the homoskedastic mixed frequency stacked VAR and do not include the UKCS. They plot, for each region, actual regional GVA growth (i.e. the subsequent realisation using the first estimate from the ONS) along with our five different nowcasts (conditional means of the nowcast densities). One clear pattern which emerges, to varying degrees across regions, is that 2009 is a year where updating regional nowcasts, in the light of the more timely UK data, is particularly important. As the Great Recession hit, the unconditional forecast of 2009 GVA growth turned out to be much higher than the realisation in every region. However, our tilting methodology quickly downgraded the 2009 nowcasts. 2013 is another year when the tilted nowcasts showed big improvements relative to the unconditional forecasts. In this case, realised GVA growth in all regions was higher than expected and the unconditional forecast was too low in every region. By tilting towards UK-wide releases as they came available, the nowcasts were upgraded and ended up being much closer to the actual 2013 realisation. 

### **3.1 Robustness** 

#### **3.1.1 Larger VAR models** 

In other nowcasting and forecasting applications, albeit of aggregate output growth, it has been found that consideration of a larger set of indicators can be beneficial; e.g. see Banbura, Giannone, Reichlin (2010), Foroni and Marcellino (2014) and Carriero, Clark and Marcellino (2015). Similarly, in our application, we might hope that additional indicators help explain and anticipate regional output growth. It is ultimately an empirical matter. But we should admit that we are ( _a priori_ ) somewhat cautious about the predictive content of these additional indicators, given that they do not share the characteristic of UK GVA growth, the main indicator considered above, of being the cross-sectional aggregation of the regional GVA data that we are in fact seeking to nowcast. 

Nevertheless, to explore the scope to improve further the accuracy of our regional growth 

19 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

nowcasts when additional quarterly and/or annual indicators, at the regional, sectoral and aggregate levels, are included in our VAR models, in this section we provide some evidence that evaluates how nowcast accuracy is affected empirically when we do consider some stacked VAR models augmented with additional indicators. We should emphasise that our stacked VAR models are already pretty ‘large’, given our consideration of regional data, and of a comparable size to the ‘large’ VAR models considered, for example, in Carriero, Clark and Marcellino (2015)’s nowcasting application. So consideration of appreciably larger VAR models raises computational challenges, given our model specification and strategy to estimate the shrinkage parameters preclude use of analytical methods. We therefore restrict our attention to VAR models with a dozen or so additional indicators. 

Our experiments involved adding to _yt_ candidate indicator variables that might credibly be believed to offer some additional (to quarterly UK GVA growth and lagged regional GVA growth) explanatory power for regional GVA growth. In searching for these indicator variables, inevitably we face some data constraints and limitations. In applications which nowcast country-wide output growth, timely data on industrial production are often found to improve accuracy (e.g. see Mazzi, Mitchell and Montana, 2014). However, the ONS do not publish higher-frequency and/or more timely breakdowns of regional industrial production. Drawing on Bell, Co, Stone and Wallis (2014) in their application which nowcasts (aggregate) output growth in the UK, we might also hope to use qualitative business survey data, as they find these survey data are useful and timely indicators of UK output growth. While regional breakdowns of these business survey data, for example PMI data, are available, in fact at the monthly frequency, their historical coverage is limited; regional PMI data date back to 1997 only. But the historical coverage of regional labour market data is better. So we do augment our stacked VAR model with regional data on jobseeker’s allowance (JSA), an ONS measure of unemployment. JSA data are in fact available monthly, but we choose to work with them aggregated to the quarterly frequency. But in aggregating we accommodate the fact that these JSA data are currently released just two weeks after the end of the month of interest. So, for example, in defining _yt_ we match the JSA annual growth rate ending in April (published in May) with the Q1 UK GVA growth estimates, _yt,_<sup>_UK_</sup> 1<sup>, that also become available</sup> in May. Similarly, the Q2 data, _yt,_<sup>_UK_</sup> 2<sup>,arematchedtoJSAannualgrowthratesendingin</sup> July, and so on for the other quarters. These regional JSA data, which are not typically revised so we use latest vintage data, date back to 1975; we backcast earlier estimates using the UK aggregate. We also add to our VAR model sectoral GVA growth data: for the service sector, manufacturing, construction and agriculture. These data are released at the same time as the quarterly UK GVA data; with historical data available from the Bank of England’s real-time database. As the sectoral composition of the UK regions varies, we might find that regional output growth is better explained by sectoral rather than total output growth. Consideration of these extra indicators at the quarterly frequency would increase the dimension of our stacked VAR model by (9 + 4) _×_ 4. To facilitate computation, but after experimentation that suggested results were robust to this, we elected to estimate this larger 

20 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

VAR by including only the Q4 values of these additional indicators; these are always, in any case, the latest estimates known when the unconditional predictive densities are recursively computed. However, when tilting we do so conditioning on the latest quarterly estimate of annual growth available for that indicator at each of the four points within the year at which we update the nowcasts. 

Accordingly, we repeated the real-time out-of-sample nowcasting exercise above using this larger VAR model (as discussed, having also experimented with alternatives, dropping or including subsets of these additional indicators, and finding results to be similar). Table 6 reports results, continuing to focus on the homoskedastic stacked VAR that does not include the UKCS - given this was found to be the preferred model above. Comparing Tables 1 and 6 we are therefore able to evaluate the empirical utility of using the larger set of indicators. Looking first at the accuracy of the unconditional forecasts, we see little evidence to suggest that the larger set of indicator delivers improved accuracy; this is so irrespective of which of the three measures of forecast performance we consult. In fact, it is striking how similar accuracy is across Tables 1 and 6 when confining attention to the unconditional forecasts; if anything the slight edge goes to the smaller VAR in Table 1. But when we turn to look at the conditional nowcasts, we find the larger VAR model to be outperformed by the smaller VAR model. This is especially so when measures of density accuracy are consulted. The CRPS and LPS statistics are clearly worse than for the smaller model - even when we condition on the Q4 release. Inspection of the underlying density nowcasts from the larger VAR models (not reported) indicates this may be explained by the extra uncertainty apparently associated when nowcasting with this larger set of indicators; the variances of the predictive nowcasts are often double those from the smaller VAR model, with the extra parameter estimation error associated with the larger VAR model no doubt contributing to this. An explanation for these results is that, in contrast to other relationships in the larger VAR model, there is a more stable relationship between UK output growth and regional output growth. These other indicators offer little or no, given their noise, value-added relative to conditioning the regional nowcasts on UK-wide output growth (and lagged values). 

#### **3.1.2 A mixed frequency (MIDAS) benchmark** 

To assess the incremental gains of entropic tilting and imposing the cross-sectional constraint on our cross-region stacked VAR model, we also compare our results with those from a mixed frequency univariate benchmark model that allows the regional nowcasts to be updated through the year as the quarterly UK GVA data are released. To accommodate the fact that this benchmark model now conditions on available quarterly UK GVA data, and is therefore mixed frequency, we follow Foroni, Marcellino and Schumacher (2015) and, in effect, use “Unrestricted” U-MIDAS models. These involve recursively forecasting using regressions of annual regional GVA growth on lagged (again by two years) growth, as with the AR benchmark, but then adding Q1-Q4 quarterly UK GDP as (an) additional indicator(s). So while the first (Q1) nowcast, produced before the first release of Q1 UK GVA growth, is the 

21 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

same as the nowcast produced from the AR, the second nowcast also conditions on current year Q1 UK GVA growth, the third nowcast on both Q1 and Q2 UK GVA growth, and so on. 

We construct the density nowcasts from these U-MIDAS models analytically, assuming normality for the errors, with the variance of the density nowcast computed to account for parameter estimation uncertainty as suggested by Clements and Galvao (2017); for a more general discussion see Aastveit, Foroni and Ravazzolo (2017). We should note that accommodating parameter estimation error does little to affect the AR results considered in Tables 1 to 4 above; but for these less parsimonious U-MIDAS models it does make a 

Table 7 reports the RMSE, CRPS and LPS statistics from these U-MIDAS models relative to those from the AR; with numbers less than unity, for RMSE and CRPS, again indicating that the U-MIDAS model is more accurate; and numbers for LPS greater than zero indicating that the U-MIDAS model is more accurate. Looking at RMSE first, for several regions, but a decreasing number as we move right in the tables, U-MIDAS is better. But looking at the measures of density accuracy, we see overwhelming evidence that the U-MIDAS models are less accurate than the arguably more naive AR benchmark. This result is less surprising when we note that the U-MIDAS models, as they condition on accumulating within-year (Q1-Q4) UK GVA growth data fit the regional GVA growth data increasingly well in-sample - as within-year data accumulates. The in-sample fit of these regressions is considerably higher than those of the AR benchmark. This in-sample accuracy then translates into narrower predictive nowcasts for regional GVA growth, notwithstanding some extra parameter estimation error as the U-MIDAS models are less parsimonious. And given the out-of-sample ‘shocks’ evident over our out-of-sample period, these narrow density nowcasts from the U-MIDAS models often appear to miss or attach a very low probability to the subsequent regional GVA growth outturn. 

## **4 Conclusions** 

In this paper we have highlighted the need for more timely macroeconomic data for the UK regions. Our desire is to produce regional GVA estimates which are more frequent (quarterly instead of annual) and also more timely. We have developed an econometric procedure which combines a mixed frequency stacked VAR with entropic tilting. Our key contributions lie in the incorporation of the new, more timely, information provided by the quarterly releases of UK wide data acknowledging the fact that UK growth is a weighted average of growth for the individual regions. Exploiting this cross-sectional constraint, and noting that we do not expect it to hold exactly, we are able to produce updated regional nowcasts to the same timescale as the ONS currently produce their quarterly UK estimates. That is, the latest UK data help allocate national growth among the regions of the UK. In a real-time nowcasting exercise we find our methods to work well. As new, quarterly UK wide information is released throughout 

22 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

the year our nowcasts of regional GVA growth improve. Thus, using the methods we propose, regional policymakers can have at their disposal more accurate nowcasts of current growth rates. They do not have to rely on out-of-date figures or indeed have to wait many months for new regional data releases from ONS. 

We hope that entropic tilting, with mixed frequency stacked VARs, as developed in this paper will find other applications when interested in nowcasting and forecasting with data subject to aggregation constraints and differential publication lags. 

23 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Table 1: Nowcasting Performance Using Homoskedastic Mixed Frequency VAR (Results Relative to AR Benchmark) _Note: the RMSFE and CRPS values from our VAR nowcasting model are presented relative to (divided by) those from the benchmark AR model; in the same way the LPS are presented relative to (by subtraction of) the LPS from the AR model._ 

|Tilting Using New Information:|None|Q1|Q2|Q3|Q4|
|---|---|---|---|---|---|
||**RMSFE**|||||
|North|0.96|0.61|0.58|0.56|0.59|
|York. & Humber|0.92|0.48|0.51|0.49|0.48|
|East Mids|0.90|0.56|0.44|0.42|0.45|
|West Mids|0.88|0.47|0.37|0.35|0.37|
|Lon & SE|1.09|0.37|0.35|0.39|0.38|
|South West|0.97|0.48|0.45|0.42|0.35|
|Wales|1.06|0.62|0.55|0.53|0.58|
|Scotland|0.92|0.45|0.41|0.41|0.44|
|N. Ireland|1.05|0.71|0.77|0.77|0.76|
|**Average RMSE**|0.97|0.53|0.49|0.48|0.49|
||**LPS**|||||
|North|0.23|0.57|0.60|0.61|0.71|
|York. & Humber|0.28|0.62|0.60|0.61|0.76|
|East Mids|0.08|0.54|0.63|0.65|0.76|
|West Mids|0.17|0.63|0.70|0.70|0.82|
|Lon & SE|-0.21|0.71|0.73|0.70|0.80|
|South West|0.16|0.59|0.61|0.63|0.76|
|Wales|0.08|0.57|0.63|0.64|0.73|
|Scotland|0.14|0.65|0.68|0.68|0.86|
|N. Ireland|-0.14|0.43|0.35|0.35|0.35|
|**Sum LPS**|0.79|5.32|5.53|5.58|6.54|
||**CRPS**|||||
|North|0.89|0.58|0.56|0.55|0.55|
|York. & Humber|0.85|0.52|0.53|0.52|0.47|
|East Mids|0.86|0.53|0.45|0.44|0.43|
|West Mids|0.80|0.48|0.41|0.41|0.39|
|Lon & SE|1.15|0.44|0.43|0.45|0.42|
|South West|0.90|0.51|0.49|0.47|0.40|
|Wales|1.01|0.60|0.54|0.53|0.55|
|Scotland|0.88|0.47|0.44|0.44|0.43|
|N. Ireland|1.06|0.69|0.74|0.73|0.69|
|**Average CRPS**|0.93|0.53|0.51|0.50|0.48|



24 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Table 2: Nowcasting Performance Using Mixed Frequency VAR with Stochastic Volatility (Results Relative to AR Benchmark) _Note: the RMSFE and CRPS values from our VAR nowcasting model are presented relative to (divided by) those from the benchmark AR model; in the same way the LPS are presented relative to (by subtraction of) the LPS from the AR model._ 

|Tilting Using New Information:|None|Q1|Q2|Q3|Q4|
|---|---|---|---|---|---|
||**RMSFE**|||||
|North|0.78|0.63|0.61|0.59|0.63|
|York. & Humber|0.71|0.45|0.40|0.38|0.37|
|East Mids|0.75|0.55|0.44|0.43|0.43|
|West Mids|0.82|0.51|0.40|0.39|0.39|
|Lon & SE|0.92|0.36|0.34|0.39|0.36|
|South West|0.79|0.47|0.44|0.41|0.37|
|Wales|0.86|0.58|0.52|0.50|0.56|
|Scotland|0.76|0.46|0.41|0.41|0.43|
|N. Ireland|0.88|0.69|0.75|0.74|0.75|
|**Average RMSE**|0.81|0.52|0.48|0.47|0.48|
||**LPS**|||||
|North|0.06|0.16|0.22|0.23|0.40|
|York. & Humber|0.20|0.32|0.36|0.37|0.60|
|East Mids|0.17|0.33|0.40|0.41|0.59|
|West Mids|0.02|0.31|0.38|0.38|0.51|
|Lon & SE|-0.04|0.33|0.34|0.33|0.49|
|South West|0.12|0.32|0.34|0.35|0.50|
|Wales|0.18|0.35|0.39|0.39|0.51|
|Scotland|0.23|0.42|0.42|0.42|0.59|
|N. Ireland|0.09|0.22|0.20|0.20|0.35|
|**Sum LPS**|1.04|2.76|3.04|3.09|4.54|
||**CRPS**|||||
|North|0.87|0.74|0.73|0.73|0.67|
|York. & Humber|0.81|0.66|0.63|0.62|0.51|
|East Mids|0.74|0.61|0.54|0.53|0.46|
|West Mids|0.87|0.64|0.57|0.57|0.51|
|Lon & SE|1.00|0.62|0.61|0.63|0.54|
|South West|0.83|0.63|0.61|0.60|0.51|
|Wales|0.86|0.68|0.63|0.63|0.59|
|Scotland|0.77|0.57|0.55|0.55|0.50|
|N. Ireland|0.89|0.73|0.77|0.76|0.70|
|**Average CRPS**|0.85|0.65|0.63|0.62|0.55|



25 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Table 3: Nowcasting Performance Using Homoskedastic Mixed Frequency VAR including UKCS (Results Relative to AR Benchmark) _Note: the RMSFE and CRPS values from our VAR nowcasting model are presented relative to (divided by) those from the benchmark AR model; in the same way the LPS are presented relative to (by subtraction of) the LPS from the AR model._ 

|Tilting Using New Information:|None<br>**RMSFE**|Q1|Q2|Q3|Q4|
|---|---|---|---|---|---|
|North|0.96|0.54|0.52|0.52|0.67|
|York. & Humber|0.91|0.49|0.39|0.40|0.55|
|East Mids|0.92|0.68|0.54|0.50|0.42|
|West Mids|0.89|0.51|0.34|0.33|0.37|
|Lon & SE|1.09|0.55|0.42|0.43|0.45|
|South West|0.97|0.56|0.46|0.43|0.42|
|Wales|1.03|0.67|0.56|0.54|0.52|
|Scotland|0.91|0.46|0.37|0.39|0.46|
|N. Ireland|1.05|0.76|0.71|0.72|0.76|
|UKCS|3.69|1.37|0.99|0.95|1.16|
|**Average RMSE (Inc. UKCS)**|1.24|0.66|0.53|0.52|0.58|
|**Average RMSE (Exc. UKCS)**|0.97|0.58|0.48|0.47|0.51|
||**LPS**|||||
|North|0.24|0.62|0.63|0.63|0.59|
|York. & Humber|0.29|0.60|0.64|0.64|0.69|
|East Mids|0.06|0.40|0.54|0.57|0.79|
|West Mids|0.16|0.59|0.71|0.72|0.82|
|Lon & SE|-0.19|0.56|0.66|0.66|0.73|
|South West|0.16|0.53|0.59|0.61|0.72|
|Wales|0.13|0.50|0.59|0.60|0.82|
|Scotland|0.16|0.62|0.68|0.67|0.83|
|N. Ireland|-0.12|0.36|0.43|0.41|0.35|
|UKCS|0.50|0.65|0.67|0.67|0.77|
|**Sum LPS (Inc. UKCS)**|1.41|5.44|6.14|6.17|7.10|
|**Sum LPS (Exc. UKCS)**|0.91|4.78|5.47|5.50|6.34|
||**CRPS**|||||
|North|0.89|0.53|0.52|0.53|0.61|
|York. & Humber|0.84|0.52|0.47|0.48|0.52|
|East Mids|0.88|0.63|0.52|0.49|0.40|
|West Mids|0.81|0.51|0.40|0.40|0.39|
|Lon & SE|1.14|0.58|0.48|0.49|0.48|
|South West|0.90|0.56|0.49|0.47|0.44|
|Wales|0.97|0.65|0.55|0.54|0.49|
|Scotland|0.87|0.48|0.43|0.44|0.44|
|N. Ireland|1.06|0.74|0.68|0.68|0.69|
|UKCS|1.06|0.73|0.70|0.70|0.65|
|**Average RMSE (Inc. UKCS)**|0.94|0.59|0.52|0.52|0.51|
|**Average RMSE (Exc. UKCS)**|0.93|0.58|0.50|0.50|0.50|



26 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Table 4: Nowcasting Performance Using Mixed Frequency VAR with Stochastic Volatility and including UKCS (Results Relative to AR Benchmark) _Note: the RMSFE and CRPS values from our VAR nowcasting model are presented relative to (divided by) those from the benchmark AR model; in the same way the LPS are presented relative to (by subtraction of) the LPS from the AR model._ 

|Tilting Using New Information:|None<br>**RMSFE**|Q1|Q2|Q3|Q4|
|---|---|---|---|---|---|
|North|0.79|0.59|0.59|0.58|0.65|
|York. & Humber|0.72|0.42|0.36|0.35|0.42|
|East Mids|0.76|0.60|0.50|0.49|0.44|
|West Mids|0.83|0.52|0.42|0.41|0.41|
|Lon & SE|0.92|0.42|0.34|0.35|0.36|
|South West|0.79|0.46|0.42|0.37|0.37|
|Wales|0.85|0.62|0.56|0.54|0.55|
|Scotland|0.76|0.46|0.37|0.38|0.48|
|N. Ireland|0.89|0.72|0.71|0.71|0.77|
|UKCS|1.82|0.53|0.90|0.98|0.90|
|**Average RMSE (Inc. UKCS)**|0.91|0.53|0.52|0.51|0.54|
|**Average RMSE (Exc. UKCS)**|0.81|0.53|0.47|0.46|0.49|
||**LPS**|||||
|North|0.11|0.19|0.22|0.23|0.41|
|York. & Humber|0.23|0.31|0.35|0.35|0.61|
|East Mids|0.19|0.27|0.33|0.34|0.62|
|West Mids|0.09|0.27|0.34|0.33|0.52|
|Lon & SE|0.04|0.28|0.30|0.31|0.52|
|South West|0.15|0.29|0.31|0.33|0.54|
|Wales|0.18|0.30|0.34|0.35|0.56|
|Scotland|0.22|0.39|0.42|0.42|0.57|
|N. Ireland|0.08|0.20|0.21|0.21|0.35|
|UKCS|0.44|0.46|0.46|0.46|0.63|
|**Sum LPS (Inc. UKCS)**|1.74|2.96|3.27|3.33|5.33|
|**Sum LPS (Exc. UKCS)**|1.30|2.50|2.81|2.88|4.70|
||**CRPS**|||||
|North|0.86|0.72|0.72|0.72|0.68|
|York. & Humber|0.79|0.65|0.62|0.62|0.52|
|East Mids|0.75|0.65|0.59|0.58|0.46|
|West Mids|0.86|0.67|0.60|0.59|0.51|
|Lon & SE|0.99|0.66|0.64|0.63|0.52|
|South West|0.82|0.63|0.61|0.59|0.49|
|Wales|0.86|0.71|0.67|0.66|0.57|
|Scotland|0.78|0.57|0.54|0.54|0.52|
|N. Ireland|0.90|0.76|0.74|0.73|0.70|
|UKCS|0.91|0.85|0.86|0.87|0.73|
|**Average RMSE (Inc. UKCS)**|0.85|0.69|0.66|0.65|0.57|
|**Average RMSE (Exc. UKCS)**|0.85|0.67|0.64|0.63|0.55|



27 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Table 5: Descriptive statistics for annual regional nominal GVA <u>growth</u> rates (1967-2016) 

||Mean|Standard<br>Deviation|Correlation<br>with<br>UK<br>GVA|
|---|---|---|---|
|North|0.077|0.053|0.922|
|York. & Humber|0.078|0.056|0.910|
|East Midlands|0.082|0.061|0.906|
|London & South East|0.086|0.047|0.928|
|South West|0.088|0.062|0.880|
|West Midlands|0.077|0.050|0.918|
|Wales|0.079|0.059|0.919|
|Scotland|0.082|0.054|0.940|
|N. Ireland|0.089|0.064|0.791|
|UKCS|-0.260|2.813|-0.187|



28 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Table 6: Nowcasting Performance Using Larger Homoskedastic Mixed Frequency VAR (Results Relative to AR Benchmark) _Note: the RMSFE and CRPS values from our VAR nowcasting model are presented relative to (divided by) those from the benchmark AR model; in the same way the LPS are presented relative to (by subtraction of) the LPS from the AR model._ 

|Tilting Using New Information:|None|Q1|Q2|Q3|Q4|
|---|---|---|---|---|---|
||**RMSFE**|||||
|North|0.90|0.62|0.55|0.52|0.62|
|York. & Humber|0.96|0.59|0.51|0.47|0.70|
|East Mids|0.96|0.75|0.69|0.65|0.81|
|West Mids|0.96|0.69|0.64|0.60|0.67|
|Lon & SE|1.12|0.46|0.65|0.69|0.83|
|South West|0.85|0.64|0.60|0.57|0.70|
|Wales|1.16|0.84|0.79|0.77|0.95|
|Scotland|0.94|0.59|0.53|0.50|0.66|
|N. Ireland|1.02|0.85|0.84|0.82|0.81|
|**Average RMSE**|0.98|0.67|0.64|0.62|0.75|
||**LPS**|||||
|North|0.13|0.24|0.25|0.26|0.41|
|York. & Humber|0.10|0.25|0.27|0.28|0.38|
|East Mids|0.05|0.26|0.31|0.33|0.28|
|West Mids|0.06|0.25|0.28|0.30|0.41|
|Lon & SE|0.12|0.14|0.09|0.08|0.17|
|South West|0.26|0.45|0.49|0.51|0.47|
|Wales|0.01|0.17|0.18|0.19|0.22|
|Scotland|0.10|0.30|0.32|0.34|0.41|
|N. Ireland|0.04|0.15|0.16|0.17|0.26|
|**Sum LPS**|0.86|0.24|0.26|0.27|0.33|
||**CRPS**|||||
|North|0.90|0.72|0.69|0.67|0.65|
|York. & Humber|0.94|0.71|0.67|0.66|0.70|
|East Mids|0.91|0.72|0.67|0.64|0.75|
|West Mids|0.89|0.70|0.67|0.64|0.65|
|Lon & SE|1.17|0.70|0.80|0.83|0.87|
|South West|0.79|0.62|0.59|0.57|0.64|
|Wales|1.09|0.85|0.82|0.80|0.89|
|Scotland|0.91|0.65|0.61|0.60|0.65|
|N. Ireland|0.99|0.84|0.83|0.81|0.79|
|**Average CRPS**|0.95|0.72|0.71|0.69|0.73|



29 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

|_values from the_<br> _same way the_||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|_CRPS _<br>_; in the_|||**LPS**|-23.65|-7.15|-8.65|-20.65|-22.07|-7.41|-21.84|-19.13|-9.85|0.13|
|_E and _<br> _model_||Q4|**CRPS**|1.40|1.18|0.92|1.15|1.18|1.12|1.30|1.12|1.33|1.00|
|_RMSF_<br>_ark AR_||-MIDAS-|**MSE**<br>|1.13|1.10|0.91|1.09|1.00|1.08|1.21|0.99|1.18|1.35|
|_the _<br>_hm_|_el._|U|**R**|||||||||||
|_Note: _<br>_e benc_|_R mod_||**LPS**|-22.72|-6.66|-6.50|-20.68|-22.16|-6.51|-22.20|-17.66|-10.22|0.06|
|mark. <br>_rom th_|_the A_|-Q3|**CRPS**|1.39|1.21|0.96|1.16|1.18|1.18|1.33|1.16|1.35|1.00|
|bench<br>_those f_|_S from _|U-MIDAS|**RMSE**|1.14|1.13|0.94|1.11|1.00|1.13|1.23|1.02|1.19|1.15|
|the AR<br>_ded by) _|_) the LP_||**LPS**<br>|-19.10|-5.66|-2.57|-19.88|-16.51|-5.01|-21.98|-12.78|-8.54|0.08|
|ative to<br>_o (divi_|_tion of_|Q2|**CRPS**|1.35|1.19|0.93|1.15|1.14|1.17|1.33|1.13|1.31|1.00|
|el<br>_e t_|_ac_|AS-||||||||||||
|uracy r<br> _relativ_|_y subtr_|U-MID|**RMSE**|1.11|1.11|0.92|1.10|0.98|1.12|1.23|1.01|1.17|1.17|
|st acc<br>_ented _|_e to (b_||**LPS**|-7.97|0.55|0.97|-6.32|-5.60|-0.68|-3.66|-1.00|-1.25|0.14|
|nowca<br>_e pres_|_elativ_|1|**CRPS**|1.20|0.97|0.84|1.07|1.00|1.01|1.12|0.93|1.08|0.98|
|MIDAS <br>_model ar_|_sented r_|U-MIDAS-Q|**RMSE**<br>|1.07|0.98|0.86|1.03|0.94|1.00|1.08|0.90|1.04|0.69|
|e 7: U-<br>_IDAS _|_are pre_|||h|& H|Mid|& SE|st|Mid|s|and|land|S|
|Tabl<br>_U-M_|_LPS _|||Nort|York|East|Lon|S We|West|Wale|Scotl|N.Ire|UKC|



30 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Figure 2: Plots of GVA Growth, _yt_<sup>_r,A_</sup> , and Nowcasts for the UK Regions 



<!-- Start of picture text -->
North<br>0.1<br>0.05 Actual<br>Unconditional<br>Q1<br>0 Q2<br>Q3<br>Q4<br>-0.05<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br>Yorkshire & Humber<br>0.15<br>0.1<br>0.05 ActualUnconditional<br>0 Q1Q2<br>-0.05 Q3Q4<br>-0.1<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br>East Midlands<br>0.15<br>0.1<br>Actual<br>0.05 UnconditionalQ1<br>Q2<br>0 Q3<br>Q4<br>-0.05<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br><!-- End of picture text -->

Figure 3: Plots of GVA Growth, _yt_<sup>_r,A_</sup> , and Nowcasts for the UK Regions (cont.) 



<!-- Start of picture text -->
West Midlands<br>0.15<br>0.1<br>Actual<br>0.05 UnconditionalQ1<br>Q2<br>0 Q3<br>Q4<br>-0.05<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br>London & the South East<br>0.15<br>0.1<br>Actual<br>0.05 UnconditionalQ1<br>Q2<br>0 Q3<br>Q4<br>-0.05<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br>South West<br>0.15<br>0.1<br>Actual<br>0.05 UnconditionalQ1<br>Q2<br>0 Q3<br>Q4<br>-0.05<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br><!-- End of picture text -->

31 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Figure 4: Plots of GVA Growth, _yt_<sup>_r,A_</sup> , and Nowcasts for the UK Regions (cont.) 



<!-- Start of picture text -->
Wales<br>0.1<br>0.05 Actual<br>Unconditional<br>Q1<br>0 Q2<br>Q3<br>Q4<br>-0.05<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br>Scotland<br>0.15<br>0.1<br>Actual<br>0.05 UnconditionalQ1<br>Q2<br>0 Q3<br>Q4<br>-0.05<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br>Northern Ireland<br>0.15<br>0.1<br>Actual<br>0.05 UnconditionalQ1<br>Q2<br>0 Q3<br>Q4<br>-0.05<br>2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016<br><!-- End of picture text -->

32 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

## References 

Aastveit, K.A., Foroni, C. and Ravazzolo, F. (2017). “Density forecasts from MIDAS models”. Journal of Applied Econometrics, 32, 783-801. 

Alessi, L., Ghysels, E., Onorante, L., Peach, R. and Potter, S. (2014). “Central bank macroeconomic forecasting during the global financial crisis: The European Central Bank and Federal Reserve Bank of New York experiences,” Journal of Business and Economic Statistics, 32, 483-500. 

Altavilla, C., Giacomini, R. and Ragusa, G. (2017). “Anchoring the yield curve using survey expectations,” Journal of Applied Econometrics, 32, 1055-1068. 

Banbura, M., Giannone, D. and Reichlin, L. (2010). “Large Bayesian vector autoregressions,” Journal of Applied Econometrics, 25, 71-92. 

Bean, C. (2007). “Risk, uncertainty and monetary policy”. Bank of England Quarterly Bulletin, 47(4), 600-606. 

Bell, V., Co, L.W., Stone, S. and Wallis, G. (2014). “Nowcasting UK GDP growth”. Bank of England Quarterly Bulletin, 54(1), 58-68. 

Brave, S., Butters, R. and Justiniano, A. (2016). “Forecasting economic activity with mixed frequency Bayesian VARs,” Federal Reserve Bank of Chicago Working Paper 2016-05. 

Byron, R.P. (1978). “The estimation of large social account matrices,” Journal of the Royal Statistical Society: Series A, 141, 359-367. 

Carriero, A., Clark, T.E. and Marcellino, M. (2015). “Realtime nowcasting with a Bayesian mixed frequency model with stochastic volatility,” Journal of the Royal Statistical Society: Series A, 178, 837-862. 

Carriero, A., Clark, T.E. and Marcellino, M. (2016). “Common drifting volatility in large Bayesian VARs,” Journal of Business and Economic Statistics, 34, 375-390. 

Clark, T.E. (2011). “Real-time density forecasts from BVARs with stochastic volatility,” Journal of Business and Economic Statistics, 29, 327-341. 

Clements, M.P., and Galvao, A.B. (2013). “Real-time forecasting of inflation and output growth with autoregressive models in the presence of data revisions.” Journal of Applied Econometrics, 28(3), 458-477. 

Clements, M.P., and Galvao, A.B. (2017). “Model and survey estimates of the term structure of US macroeconomic uncertainty”. International Journal of Forecasting, 33, 591604. 

Clements, M.P. and Hendry, D.F. (1999). “Forecasting Non-stationary Economic Time Series”. Cambridge, Mass.: MIT Press. 

Cox, D. R. (1981). “Statistical analysis of time series: some recent developments”. Scandinavian Journal of Statistics, 8, 93–115. 

D’Agostino, A., Gambetti, L. and Giannone, D. (2013). “Macroeconomic forecasting and structural change,” Journal of Applied Econometrics, 28, 82-101. 

Deming, W. and Stephan, F. (1941). “On a least squares adjustment of a sampled frequency table when the expected marginal totals are known,” Annals of Mathematical 

33 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Statistics, 11, 427-444. 

Dieppe, A., Legrand, R. and van Roye, B. (2016). “The BEAR toolbox,” European Central Bank working paper 1934. 

Eraker, B., Chiu, C., Foerster, A., Kim, T. and Seoane, H. (2015). “Bayesian mixed frequency VAR’s,” Journal of Financial Econometrics, 13, 698-721. 

Foroni, C. and Marcellino, M. (2014). “A comparison of mixed frequency approaches for nowcasting Euro area macroeconomic aggregates”, International Journal of Forecasting, 30, 554-568. 

Foroni, C., Marcellino, M. and Schumacher, C. (2015). “U-MIDAS: MIDAS regressions with unrestricted lag polynomial”, Journal of the Royal Statistical Society, Series A, 178, 57-82. 

Frale, C., Marcellino, M., Mazzi, G-L. and Proietti, T. (2011), “EUROMIND: A Monthly Indicator of the Euro Area Economic Conditions”, Journal of the Royal Statistical Society, Series A, 174, 439-470. 

Ghysels, E. (2016). “Macroeconomics and the reality of mixed frequency data,” Journal of Econometrics, 193, 294-314. 

Ghysels, E., Grigoris, F. and Ozkan, N. (2017). “Forecasting of state and local government budgets: Exploiting mixed frequency and cross-border data,” manuscript. 

Giacomini, R. and Granger, C.W.J. (2004). “Aggregation of space-time processes”. Journal of Econometrics, 118, 7-26. 

Giannone, D., Lenza, M. and Primiceri, G. E. (2015). “Prior selection for vector autoregressions,” Review of Economics and Statistics, 27, 436-451. 

Haldane, A. (2016). “Whose recovery? Speech given in Port Talbot on 30 June 2016.” Available at `https://www.bankofengland.co.uk/-/media/boe/files/speech/2016/whos e-recovery` 

Kass, R. and Raftery, A. (1995). “Bayes Factors,” Journal of the American Statistical Association, 90, 773-795. 

Kr¨uger, F., Clark, T.E. and Ravazzolo, F. (2017). “Using entropic tilting to combine BVAR forecasts with external nowcasts,” Journal of Business and Economic Statistics, 35, 470-485. 

Kuzin, V., Marcellino, M. and Schumacher, C, (2011). “MIDAS vs Mixed-Frequency VAR for Nowcasting GDP in the Euro Area”, International Journal of Forecasting, 27, 529-542. Lui, S. and J. Mitchell (2013). “Nowcasting quarterly euro-area GDP growth using a global VAR model”. In The GVAR Handbook: Structure and Applications of a Macro Model of the Global Economy for Policy Analysis (eds. di Mauro, F. and M.H. Pesaran), Oxford University Press. 

McCracken, M., Owyang, M. and Sekhposyan, T. (2018). “Real-time forecasting with a large, mixed frequency Bayesian VAR,” manuscript available at `http://www.tateviksekhp osyan.org/` 

Mandalinci, Z. (2015). “Effects of monetary policy shocks on UK regional activity: A 

34 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

constrained MFVAR approach,” School of Economics and Finance, Queen Mary University of London, working paper 758. 

Marcellino, M. and Schumacher, C. (2010). “Factor-MIDAS for now- and forecasting with ragged-edge data: A model comparison for German GDP”, Oxford Bulletin of Economics and Statistics, 72, 518-550. 

Mariano, R.S. and Y. Murasawa (2010). “A coincident index, common factors, and monthly real GDP”, Oxford Bulletin of Economics and Statistics, 72, 27-46. 

Mazzi, G-L., Mitchell, J. and Montana, G. (2014). “Density nowcasts and model combination: Nowcasting Euro-Area GDP growth over the 2008-09 recession”. Oxford Bulletin of Economics and Statistics, 76, 233-256. 

Mikosch, H. and Neuwirth, S. (2015). “Real-time forecasting with a MIDAS VAR,” Bank of Finland Institute for Economies in Transition Discussion Paper 13-2015. 

Pesaran, M.H. (2006), “Estimation and inference in large heterogeneous panels with a multifactor error structure”. Econometrica, 74, 967-1012. 

Primiceri. G. (2005). “Time varying structural vector autoregressions and monetary policy,” Review of Economic Studies, 72, 821-852. 

Robertson, J., Tallman, E. and Whiteman, C. (2005). “Forecasting using relative entropy,” Journal of Money, Credit and Banking, 37, 383-401. 

Schorfheide, F. and Song, D. (2015). “Real-time forecasting with a mixed-frequency VAR,” Journal of Business and Economic Statistics, 33, 366-380. 

Smith, R., Weale, M. and Satchell, S. (1998). “Measurement error with accounting constraints: Point and interval estimation for latent data with an application to U.K. Gross Domestic Product,” Review of Economic Studies, 65, 109-134. 

Stock, J.H. (2005). “Symposium on Regional Economic Indicators”. Review of Economics and Statistics, 87, 593. 

Waggoner, D. F. and Zha, T. (1999). “Conditional forecasts in dynamic multivariate models,” Review of Economics and Statistics, 81, 639–651. 

35 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

## **Regional Data Appendix (to be published Online)** 

This appendix summaries the data sources and construction of the regional GVA (income approach) database for the UK used in this paper. It describes the process of arriving at an annual dataset for nominal GVA for 9 ‘regions’ of the UK (plus the UK Continental Shelf) from 1966 to 2016 that is as consistent as possible, given changes to accounting standards over the time period. These changes mean that our regional estimates are measured at factor cost prior to 1996 and at basic prices from 1997. 

## **A1 Data sources and matching against UK data** 

Our ambition in putting together the database was to use, as near as possible (certainly over our out-of-sample window), first-release estimates of regional GVA, at basic prices, and match these with the appropriate, similarly dated, data release for UK GVA. This strategy is in part motivated by our interest in nowcasting first release regional GVA estimates. But it also reflects the reality that final vintage data, e.g. the ONS’s latest regional estimates, are not available over the whole sample period (i.e. the latest ONS data, published in December 2017, cover the period 1997-2016 only). So to get earlier data we inevitably have to look to earlier data vintages. In matching the regional data to the UK data we sought to minimise the cross-sectional aggregation error, as ideally the sum of the regional GVA data equals the annual sum of the quarterly UK data. But, we should emphasise (as is detailed below) that it was not possible to eradicate this measurement error for all years. This motivates our use of tilting methods to approximately impose the cross-sectional aggregation constraint reflecting this measurement error. 

The regional GVA data all come from the ONS (CSO) but via three sources: 

1. The historical regional GDP database, recently published by the ONS, provides estimates, at factor cost, from 1966-1996, compiled from historical editions of the ‘Regional Trends’ and ‘Economic Trends’ journals: `https://www.ons.gov.uk/economy/regiona laccounts/grossdisposablehouseholdincome/adhocs/006226historiceconomicda taforregionsoftheuk1966to1996` . The ONS Blue Book definition of factor cost states that “in the System of National Accounts 1968 this was the basis of valuation which excluded the effects of taxes on expenditure and subsidies”. By contrast, the latest ONS regional GVA estimates, considered in 2. and 3. below, are published in basic prices which exclude taxes (less subsidies) on products but do include taxes on the production process (such as business rates and any vehicle excise duty paid by businesses). 

   - The historical regional database “can be used as a proxy for the current regional GVA estimates”, as explained by the ONS in their supporting documentation. They also note that these data were “produced under the various statistical standards, regional and industry breakdowns which were current at the time they were 

36 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

first published”. The historical database does not always pick up estimates from successive yearly publications of Regional Trends. Our understanding, following email communication with ONS, is that this is because ONS chose to publish, in this historical database, the latest iteration for a given year rather than the first. As our interest is in extracting a database of first estimates, we deviate from the historical database as follows. From the (first) 1973 Regional Trends publication we extract regional data from 1966 to 1971. Thereafter, we consult successive annual Regional Trends publications so that the 1972 regional data come from the 1974 publication, the 1973 data come from the 1975 publication, and so on. 

2. Successive annual issues of Economic Trends/Regional Trends (published in 1998 to 2005) were consulted to obtain regional GVA estimates, at basic prices, from 1997 to 2004. 

   - This means the regional data are first release data. 

3. The GVA NUTS1 regional GVA revisions dataset is consulted to provide first release regional GVA estimates, at basic prices, from 2005-2016: `https://www.ons.gov.uk/eco nomy/grossvalueaddedgva/datasets/revisionstrianglesregionalgrossvalueadd edincomeapproachincurrentbasicprices` . These regional estimates are published with an eleven month lag, so that the 2005 data come from the December 2006 publication, and so on. 

From 1966 to 1996 these regional data are matched against quarterly UK GVA data (at factor cost, seasonally adjusted) extracted from successive, similarly dated, national account data releases (obtained from the Bank of England’s real-time database for nominal income; code CGCB) with the secondary aim of minimising the cross-sectional aggregation measurement error of the sum of the regional data against the quarterly UK data when aggregated to the annual frequency. From 1997 the regional data are matched against successive, similarly dated (so that again the data vintages of the regional data match that of the UK data), releases of quarterly UK GVA estimates, at basic prices, from the ONS’s “Second estimate of GDP” previously known as the “UK Output, Income and Expenditure” press release/bulletins. Figure A1 shows that since 1997 (and our use of first release data) the cross-sectional aggregation measurement error is time-varying and not zero. The average statistical discrepancy between 1966 and 1996 is -0.47%, between 1997 and 2016 it is -0.39%. It is worth noting that in the historical data that were released (data source 1 above) there was an explicit entry for ‘Statistical discrepancy’ and this accounts for the gap in Figure A.1 before 1997. In the later data no similar statistical discrepancy is formally reported, although as explained here, while small, a statistical discrepancy does emerge from a comparison of the first release of regional GVA data and the similarly dated (vintage) value of UK GVA data. 

37 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Figure A1: Discrepancy, by year, between the UK Quarterly series and Regional Annual series, as % UK GVA in each year 



<!-- Start of picture text -->
1<br>0.5<br>0<br>-0.5<br>-1<br>-1.5<br>-2<br>-2.5<br>1966 1976 1986 1996 2006 2016<br>Percentage<br><!-- End of picture text -->

## **A2 Geographic reconciliation** 

The next step was to reconcile the different geographic breakdowns implied by the three data sources above. While the original Regional Trends publications (the historical data, 1. above) use “Standard Statistical Regions”, the later data sources for 1997 onwards (2. and 3. above) use NUTS1 regions. 

This means that the historical data provide estimates for the following geographies: United Kingdom; North; Yorkshire and Humberside; East Midlands; East Anglia; South East; Greater London (1978 onwards); Rest of South East (1978 onwards); South West; West Midlands (2); North West; England; Wales; Scotland; Northern Ireland; United Kingdom Continental Shelf (UKCS). Prior to 1978 London was not separately identified in the regional data, instead it was part of the South East Standard Statistical Region. Between 1978 and the introduction of the NUTS classification system the old South East region was split into Greater London and Rest of South East. With the introduction of the NUTS classification, the Rest of South East region was split and one part merged with the old East Anglia Standard Statistical Region (which existed in the data from 1966-1994) to create a new ‘East of England’ NUTS1 region, and the other part maintained as the NUTS1 region ‘South East England’. 

NUTS1 data are therefore presented for the following areas: United Kingdom; North East; North West & Merseyside; Yorkshire and the Humber; East Midlands; West Midlands; Eastern; London; South East; South West; England; Wales; Scotland; Northern Ireland; 

38 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

United Kingdom less Continental Shelf. 

To arrive at a consistent series - for what we call our final dataset - we aggregated both geographical classifications to produce 9 (10 including the UKCS) “regional” GVA series which, we believe, are consistent in terms of geographic coverage across the two regional definitions. Table A1 details how the GVA series were aggregated across standard statistical and NUTS1 regions to arrive at our final “regions”. 

##### **Table A1: Regional definitions** 

|**Historical data**|**NUTS1**|**KMM**<br>**Region**<br>**ID**|**Final dataset name**|
|---|---|---|---|
|North|North East|1|North|
||North West & Merseyside|1|North|
|North West||1|North|
|Yorkshire and Humberside|Yorkshire and the Humber|2|Yorkshire and Humber|
|East Midlands|East Midlands|3|East Midlands|
|West Midlands|West Midlands|4|West Midlands|
|South East||5|London & South East|
|Greater London (_>_1978 )||5|London & South East|
||London|5|London & South East|
|Rest of South East (_>_1978)||5|London & South East|
||South East (GOR)|5|London & South East|
|East Anglia||5|London & South East|
||Eastern|5|London & South East|
|South West|South West|6|South West|
|Wales|Wales|7|Wales|
|Scotland|Scotland|8|Scotland|
|Northern Ireland|Northern Ireland|9|Northern Ireland|
|United Kingdom CS|United Kingdom CS|10|United Kingdom CS|



Looking at Table A1, we see the London and South East England was the most problematic region. This reflects the fact that, at the beginning of the sample, data are reported only for the South East of England (encompassing London and the rest of the South East, although not reported separately) and East Anglia (which was about 8% the size of the South East region in GVA terms). The difficulty is that we cannot disaggregate the South East, in the early part of these data, into London and the rest of the South East. In addition, were we able to do so, in practice the values for the South East Standard Statistical Region (pre-1995) do not align well with those for the NUTS1 region ‘South East’ in 1995. 

Figure A2 illustrates the correspondence between the statistical regions and the Government Office (or NUTS1) regions. This map illustrates this difficulty that we encountered in the South East of England. The East Anglia region, as reported from 1966-1994 (in the historical data, 1. above) is not coterminous with the subsequent East of England NUTS1 region. Similarly, the old Standard Statistical Region ‘South East of England’ (1966-1994, although split out into ‘Greater London’ and ‘Rest of South East’ from 1978) includes parts of what is now ‘East of England’, as well as ‘London’ and the ‘South East of England’. 

39 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

In addition, we can see that from Figure A2 that in the North of England, the ‘North’ Standard Statistical Region comprised parts of what, under the NUTS1 classification, is now ‘North East’ and ‘North West’ regions of England. 

Our strategy to derive a consistent database was therefore to aggregate both geographies to the most disaggregated common boundary. This results in the 9 “regions”, plus the UKCS, that we work with in the main paper. 

Figure A2: Government Office Region boundaries and Standard Statistical Region boundaries (http://www.celsius.lshtm.ac.uk/modules/geog/ge030301.html) 



## **A3 Data adjustments** 

Figure A3 plots annual nominal GVA growth rates (in %), for each of our 9 regions and for the UK as a whole, using these data. Inspection of this figure reveals a spike in growth between 1996 and 1997. To give an example, there is an 11% increase in UK GVA between 1996 and 1997, whereas separate ONS figures for the UK lead us to expect growth half this 

40 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Figure A3: Original regional nominal GVA growth rates (in %: 100 _× yt_<sup>_r,A_</sup> ) 



<!-- Start of picture text -->
35<br>North<br>Yorkshire & Humber<br>30 East Midlands<br>London & SE<br>South West<br>25 West Midlands<br>Wales<br>Scotland<br>Northern Ireland<br>20 UK<br>15<br>10<br>5<br>0<br>-5<br>1970 1975 1980 1985 1990 1995 2000 2005 2010 2015<br>Year<br>Percentage<br><!-- End of picture text -->

rate. Since we know this spike is, therefore, a feature of how we have merged the data from 1. (above) with that from 2. and 3. (above), and reflects in particular the move from estimates at factor cost to basic prices, we treat it as an _outlier_ ; recall that 1996 to 1997 was also when the aforementioned change in how regions were measured took place, with an apparent (upward) level shift in the series. We therefore elected to smooth out this spike in the 1996-1997 annual growth rate. As our regional econometric models are estimated in annual growth rates, rather than (log) levels, our practical solution is simply to proxy the 1997 growth rate with the average of the growth rates in 1996 and 1998. This, in fact, brings the UK growth rate for 1996-1997 into line with that for ONS figures for UK GVA as a whole. Figure A4 presents the annual growth rates (in %) for each region having made this adjustment. We note that this adjustment falls outside the out-of-sample window we use to assess the nowcasting performance of our models. 

41 

This version: March 2019 

Authors' copy: Accepted for publication at Journal of the Royal Statistical Society: Series A 

Figure A4: Smoothed regional nominal GVA growth rates (in %: 100 _× yt_<sup>_r,A_</sup> ) 



<!-- Start of picture text -->
35<br>North<br>Yorkshire & Humber<br>30 East Midlands<br>London & SE<br>South West<br>West Midlands<br>25 Wales<br>Scotland<br>Northern Ireland<br>20 UK<br>15<br>10<br>5<br>0<br>-5<br>1970 1975 1980 1985 1990 1995 2000 2005 2010 2015<br>Year<br>Percentage<br><!-- End of picture text -->

42 

This version: March 2019 

