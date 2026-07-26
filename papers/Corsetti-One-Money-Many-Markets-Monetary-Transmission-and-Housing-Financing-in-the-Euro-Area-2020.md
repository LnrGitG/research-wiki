---
title: **WP/20/108**
type: paper
source_pdf: raw/papers/Corsetti_One Money, Many Markets Monetary Transmission and Housing Financing in the Euro Area_2020.pdf
converted: 2026-07-26
---

# **WP/20/108** 

One Money, Many Markets: Monetary Transmission and Housing Financing in the Euro Area 

by Giancarlo Corsetti, Joao B. Duarte, and Samuel Mann 

**_IMF Working Papers_ describe research in progress by the author(s) and are published to elicit comments and to encourage debate.** The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management. 

© 2020 International Monetary Fund 

WP/20/108 

#### **IMF Working Paper** 

Monetary and Capital Markets Department 

#### **One Money, Many Markets: Monetary Transmission and Housing Financing in the Euro Area**<sup>**1**</sup> 

#### **Prepared by Giancarlo Corsetti, Joao B. Duarte, and Samuel Mann** 

Authorized for distribution by Mahvash S. Qureshi 

June 2020 

**Disclaimer:** This document was prepared before COVID-19 became a global pandemic and resulted in unprecedented economic strains. It, therefore, does not reflect the implications of these developments and related policy priorities. We direct you to the **<u>IMF Covid-19 page</u>** that includes staff recommendations with regard to the COVID-19 global outbreak. 

**_IMF Working Papers_ describe research in progress by the author(s) and are published to elicit comments and to encourage debate.** The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, <u>or IMF management.</u> 

#### **<mark>Abstract</mark>** 

We study the transmission of monetary shocks across euro-area countries using a dynamic factor model and high-frequency identification. We develop a methodology to assess the degree of heterogeneity, which we find to be low in financial variables and output, but significant in consumption, consumer prices, and variables related to local housing and labor markets. Building a small open economy model featuring a housing sector and calibrating it to Spain, we show that varying the share of adjustable-rate mortgages and loan-to-value ratios explains up to one-third of the cross-country heterogeneity in the responses of output and private consumption. 

JEL Classification Numbers: E21, E31, E44, E52, F44, F45 

Keywords: Monetary Policy, High-Frequency Identification, Monetary Union, Housing Market, Loan-to-value Ratio, Adjustable Mortgage Rates 

Authors’ E-Mail Addresses: gc422@cam.ac.uk, <u>joao.duarte@novasbe.pt, smann2@imf.org.</u> 

> 1 The authors are grateful to Alexei Onatski, Peter Karadi, Refet Gurkaynak, Tiago Cavalcanti, Luca Dedola, Pontus Rendahl, Vasco Carvalho, Simon Lloyd, Domenico Giannone, Antonio Conti, Michele Lenza and conference participants at the Banco Central do Brasil, the Bank of Italy, the 42nd EEA annual congress, and the Macro Lunch Seminar at the University of Cambridge for comments and suggestions. 

|**CONTENTS**<br> **PAGE**|
|---|
|**Abstract ............................................................................................................. 2**|
|**I. Introduction ...................................................................................................4**|
|**II. A Dynamic Factor Model for the EA .............................................................. 8**|
|A. Motivation ............................................................................................................................ 8|
|B. EmpiricalFramework............................................................................................................ 9|
|C. Identification ....................................................................................................................... 11|
|D. Data and Estimation ........................................................................................................... 18|
|**III. Empirical Results ....................................................................................... 21**|
|A. Euro-wide Dynamic Effects of Monetary Policy ................................................................ 21|
|B. Cross-Country Dynamic Effects of Monetary Policy......................................................... 24|
|**IV. Quantifying How Mortgage Markets Shape Monetary Transmission .......... 30**|
|A. Model .................................................................................................................................. 31|
|B. Calibration .......................................................................................................................... 37|
|C. Quantitative Exercise: One Money, Many Housing Markets ................................................ 40|
|**V. Conclusion .................................................................................................. 48**|
|**References ....................................................................................................... 49**|
|**Appendix ......................................................................................................... 54**|



3 

## **1 Introduction** 

Monetary policy in the euro area (EA) has long been challenged by financial, economic, and institutional heterogeneity among member countries. Although there has been some convergence over time in financial markets, the convergence process has slowed down markedly since the financial crisis (see ECB, 2017). Other markets have remained remarkably different across member countries. Most notably, the institutional backgrounds in labour and housing are highly dissimilar across the currency block. Because of these slow developments, policy and academic researchers have long been faced with two questions. First, to which extent is the transmission of the European Central Bank’s (ECB) monetary policy heterogeneous across borders? Second, how do differences in institutional characteristics of specific markets weigh on the observed heterogeneity?<sup>1</sup> 

In this paper, we provide novel empirical and quantitative answers to these questions, developing a methodology suitable to analyze and test the degree of cross-country heterogeneity in the transmission of monetary policy. On empirical grounds, we set up a dynamic factor model (DFM) and assemble a large dataset including economic and financial time series for the EA as a block and the 11 original member countries, spanning the years from 1999 to 2016. The high dimensionality of the data allows us to carry out a formal comparison of the degree of heterogeneity among responses to monetary policy shocks across different dimensions of the economy, such as output and asset prices, as well as housing and labour markets. We identify monetary policy shocks by constructing an external instrument using high-frequency changes in asset prices around ECB policy announcements, following Gurkaynak et al. (2005) and Gertler and Karadi (2015). To bring theory to bear on our findings, we build a small open economy with housing operating in a monetary union and assess quantitatively how much of the variation in individual EA countries’ responses to a monetary policy shock can be explained by differences in housing financing. Our focus is on the share of mortgages with adjustable rates and average loan-to-value ratios. 

Our main results are as follows. First, at the aggregate EA level, we find that results from the factor model are in line with theory and, notably, that the transmission of monetary shocks does not suffer from the price puzzle. Second, we show that the estimated country-level effects are significantly heterogeneous in prices and variables related to labour and housing markets—some of the least integrated markets in the euro area. The degree of heterogeneity among responses to policy is instead low in financial variables and output. 

> 1See Angeloni et al. (2003) for a discussion of the early debate on these issues. Naturally, the ECB would benefit from knowing how monetary policy affects the individual member countries differently. At the same time, policymakers would gain from understanding the implications of their policies and reforms for the transmission of monetary policy. 

4 

Third, we find that differences in mortgage market characteristics across the EA can explain up to one-third of the cross-country heterogeneity of responses in output and private consumption. 

On methodological grounds, our main contributions are, first, how to measure and statistically test heterogeneity in the responses of economic variables to a common shock in both theoretical and empirical applications. While confidence intervals around impulse response functions and Wald tests on the differences of these functions test whether responses are statistically different, they do not provide a measure of the degree of heterogeneity. To bridge this gap, we propose the following: for each set of impulse responses (e.g., GDP across member countries), we calculate the coefficient of variation statistic, also known as relative standard deviation. The coefficient of variation (CoV) for a variable is defined as the standard deviation of responses across countries with respect to the EA response, normalised by the size of the EA response. This statistical measure of the dispersion of impulse responses allows for an intuitive and meaningful comparison of variables. As a first application using the CoV, we measure the degree of heterogeneity in the DFMs estimated monetary transmission to key macro variables across EA member countries, and carry out hypothesis testing based on a bootstrapping procedure, which yields error bands for the coefficient of variation of each variable as well as pairwise differences across variables. As a second application, we use the CoV to measure the heterogeneity in the simulated theoretical responses from varying model parameters, which can then be directly compared to its empirical counterpart. 

Our second contribution consists of a quantitative assessment of the effects of crosscountry differences in mortgage markets on monetary policy transmission in a monetary union. We calibrate our baseline economy to Spain, and, using this benchmark calibration, vary the loan-to-value ratios and shares of adjustable-rate mortgage contracts to mimic observed data for different countries. This procedure allows us to compare the dispersion of the simulated impulse response functions with the dispersion we estimated in the empirical section of the paper. As we do not recalibrate the model for each country in our sample, our quantitative responses may not account for several economic factors other than housing financing that may potentially help to match the evidence. However, holding all parameters other than the share of adjustment-rate mortgages and loan-to-value ratio constant allows us to isolate more clearly the specific role played by housing financing in monetary transmission. 

**Literature** In specifying our empirical model, we build on the factor modeling literature developed in the 1970s<sup>2</sup> and recently popularised in the context of monetary policy analy- 

> 2Stock and Watson (2016) provides a comprehensive exposition of factor models, including their early history. See also Giannone et al. (2005) and Forni and Gambetti (2010). 

5 

sis. In their seminal contribution, Bernanke et al. (2005) model macroeconomic interaction with a factor-augmented VAR (FAVAR) that combines factors and perfectly observable series, typically interest rates, in one dynamic system. The dynamic factor model that we employ in our analysis is a special case of FAVARs, in that it only contains unobservable factors. From an applied perspective, the prime advantage of a factor approach is its ability to keep track of individual country-level responses to a common monetary policy shock without heavy parameterisation. Looking at the alternatives, country-by-country VARs incur the cost of heavy parameterisation, while a large panel VAR with all countries imposes restrictions on the individual dynamics. The dynamic factor model solves both problems and provides dynamic effects on the individual countries—including net spillovers—while keeping the parameter space small. In addition, the assumptions on the information structure in the dynamic factor model naturally fit the EA setting. The ECB follows not only a large number of euro-wide series but also series in individual member countries. Hence, an empirical model with a small number of variables that does not include country-level data is unlikely to span the information set used by the ECB.<sup>3</sup> 

While closely following the methodology of Stock and Watson (2012) in constructing our DFM, we identify monetary policy shocks with an external high-frequency instrument. As is well known, estimations of monetary policy transmission suffer from an identification problem. One common way to overcome this problem and identify monetary policy shocks is to impose additional internal structure on the VAR, such as timing or sign restrictions. Alternatively, one can add information from outside of the VAR, termed an external instrument approach. We make use of the latter. As in Gurkaynak et al. (2005) and Gertler and Karadi (2015), we pursue a high-frequency approach, stipulating that asset price movements occurring within a narrow time window around policy announcements are most likely associated with monetary policy shocks.<sup>4</sup> 

We construct our external instrument series based on changes in the 1-year Euro Overnight Index Average (EONIA) swap rate (i.e., the Overnight Index Swap (OIS) rate for the euro area) around policy announcements. This instrument has been proven to be economi- 

> 3Other seminal contributions on dynamic factor modelling include Sargent and Sims (1977), Sargent (1989), Giannone et al. (2005) and Boivin and Giannoni (2007). 

> 4The two leading contributions using external instruments to identify monetary policy shocks in the US are Romer and Romer (2002), pursuing the narrative approach, and Gurkaynak et al. (2005), pursuing the high-frequency approach. The idea to use high-frequency changes in asset prices, specifically interest rate derivatives, has also been developed by Kuttner (2001), Hamilton (2008) and Campbell et al. (2012). Building on these contributions, Gertler and Karadi (2015) identify monetary policy shocks in a VAR using high frequency changes in Fed funds futures. Further applications of high-frequency identification in the context of monetary policy can be found in Hanson and Stein (2015), Nakamura and Steinsson (2018), Bagliano and Favero (1999), Cochrane and Piazzesi (2002), Faust et al. (2004) and Barakchian and Crowe (2013), among others. 

6 

cally meaningful, in that it highlights the implications of using various means of policy communication—press releases, press statements, and Q&A sessions—for the transmission of current and expected future policy (see e.g. Altavilla et al., 2019). Our instrument series is a broad measure of monetary policy surprises that incorporates all of the communication channels above. 

Relative to the literature, our contribution is to show how to overcome data availability issues by combining intraday data with end-of-day data from different timezones, creating de-facto intraday series where actual intraday data is unavailable.<sup>5</sup> We test for the relevance of the series in a small VAR, confirming its validity as an external instrument. Based on historical tick data, Jarocinski and Karadi (2018) use the high-frequency co-movement of interest rates and stock prices around a narrow window of the policy announcement to disentangle policy from information shocks. The effects of the monetary shocks we identify in this paper are close to the effects of the policy shocks (as opposed to information shocks) these authors document in their work. 

The analysis of the housing channel conducted in our paper is closely related to Calza et al. (2013), who also study how heterogeneity in the structure of housing financing across the euro area can affect the transmission of monetary policy to housing prices, consumption and output. Relative to this work, our paper differs in the empirical methodology and identification, and, most importantly, in that it provides a quantitative assessment using a fully calibrated model. More generally, our work is related to the vast body of policy and academic research that, given the importance of the topic, has been devoted to the heterogeneous transmission of monetary policy across EA member states. Among the leading examples are Ciccarelli et al. (2013), who look at heterogeneity from the perspective of financial fragility, as well as Barigozzi et al. (2014) who, similar to the methodology followed in this paper, rely on a factor model, although identifying shocks with sign restrictions and pursuing a less comprehensive study, both in the number of variable included and the methodological and empirical questions addressed. Recently, Slacalek et al. (2020) develop a back-of-the-envelope calculation, applying a HANK model to the EA to study the effects of monetary policy on household consumption. They conclude that the housing wealth effect is a relevant determinant of the aggregate consumption response to monetary policy and helps explain the cross-country heterogeneity in these responses in the EA. 

> 5Intraday data on EONIA swaps is only available for recent years. However, we were able to combine endof-day data from Tokyo and London to create a de-facto intraday series that goes back to the introduction of the euro. We then compared a narrowly constructed instrument over a sub-sample for which we had complete intraday data with our proposed de-facto intraday series. We find that the series is not significantly different for the sub-sample. See Section 2.3.1 for details. In addition, our instrument series strongly correlates (0.9) with the monetary event window surprises in the euro-area monetary policy event-study database (Altavilla et al. (2019)). The latter has the advantage of being updated regularly. 

7 

The rest of the paper is organized as follows. In the next section, we describe the methodology used in the empirical analysis and provide details on the external instrument used for the identification of monetary policy shocks. In Section 3, we present our results, tracing out the effects of monetary policy on the EA as a whole, as well as on individual member countries. Section 4 introduces our analytical model to uncover how institutional differences in housing markets affect monetary transmission across the euro area. Section 5 concludes. 

## **2 A Dynamic Factor Model for the EA** 

We begin by motivating the use of a dynamic factor model for the EA and laying out the empirical framework. Later in this section, we provide details about the external instrument we construct to identify monetary policy shocks. At the end of the section, we discuss the large data set and estimation. 

### **2.1 Motivation** 

Given the EA setting, we are fundamentally interested in studying the effects of a common monetary policy shock on the EA as a block and on its member countries.<sup>6</sup> Recovering both the effects on the block and member countries imposes some empirical challenges and tradeoffs. On the one hand, fully recovering the effects of monetary policy on each individual country comes with heavy parameterisation. On the other hand, reducing the parameter space by imposing restrictions prevents us from studying the full width of heterogeneous effects. In addition, a small data sample in the time dimension, as encountered in the context of the EA, further increases the acuteness and relevance of this trade-off. 

We propose a dynamic factor model for the EA as a parsimonious way to avoid heavy parameterisation while keeping track of individual country responses to the common monetary policy shock. The dynamic factor model allows us to capture dynamic effects on individual countries through unobservable common components. The dimensionality reduction achieved through the factor model allows us to get statistically robust dynamic effects on the individual countries while keeping the parameter space small. 

The dynamic factor model has another set of appealing features for the EA. Firstly, we can relax the informational assumption that both the ECB and the econometrician perfectly observe all relevant economic variables. Secondly, as the ECB monitors a large number of 

> 6A similar setting would appear if, e.g., one was simultaneously interested in the effects of monetary policy on the U.S. as a whole and at the individual State level. 

8 

indicators in the process of policy formulation, including on the country level, it is necessary for the econometrician to take account of the same information set. The DFM achieves this. Finally, the dynamic factor model provides a format that is consistent with economic theory. We next address each of these points. 

In using a dynamic factor model, we do not have to take a stand on specific observable measures corresponding to theoretical concepts. This point was convincingly put forward by Bernanke et al. (2005). In the EA context, this relaxation becomes more relevant as it is harder to find observable euro wide variables—often weighted averages of individual member countries—that correspond to concepts of economic theory. For example, the concept of _economic activity_ in the EA may not be perfectly measured by taking a weighted average of real GDP across countries, given compositional changes that cannot be captured by treating the EA as a single economy in a theoretical model. 

The European Central Bank follows not only a large number of euro wide series but also a large number of individual member countries’ series. Hence, an empirical model, with a small number of variables, that does not include country data is unlikely to span the information set used by the ECB. This issue naturally motivates the inclusion of country-level series in our analysis. 

The state-space representation of the dynamic factor model also provides a clear link with economic theory, which creates the opportunity to formally test different mechanisms aimed at explaining the dynamic effects found in this paper. Moreover, given the large size of the dynamic effects found in observables, it is possible to test interactions of different mechanisms using the same model and dataset. 

There are alternatives to the DFM approach chosen by us—notably Panel VAR and Global VAR models. Both of these approaches involve restricting or explicitly modelling the dynamics through which variables in different units affect each other. These restrictions come at the cost of higher parameterisation relative to the dynamic factor model. Given that we are not explicitly interested in these interactions at the cross-sectional level, but rather in the final net effect, we choose the dynamic factor model for efficiency gains. Ciccarelli et al. (2013) provide a further insightful discussion of the differences between these three approaches. 

### **2.2 Empirical Framework** 

We consequently use the DFM to model macroeconomic interaction. In doing so, we largely follow the methodology proposed by Stock and Watson (2012). 

9 

Given a vector of _n_ macroeconomic series _Xt_ = ( _X_ 1 _t, ..., Xnt_ )<sup>_′_</sup> we first model each series as a combination of factors and idiosyncratic disturbances: 



where _Ft_ is a vector of unobserved factors, Λ is an _n × r_ matrix of factor loadings and _et_ = ( _e_ 1 _t, ..., ent_ )<sup>_′_</sup> denotes a vector of _n_ disturbances. We can interpret Λ _Ft_ as the ‘common component’ of _Xt_ , whilst _et_ is the ‘idiosyncratic component’. The evolution of factors is characterised by the following VAR: 



which can be rewritten with lag-operator notation as 



where Φ( _L_ ) is a _p × r_ matrix of lag polynomials and _ηt_ a vector of _r_ innovations. This equation characterises all dynamics in the model. As it stems solely from the interaction of factors, there is no need to model the co-movement of observed variables, hence avoiding the curse of dimensionality. 

The static factors can be estimated by suitable cross-sectional averaging. Whilst a setup with multiple factors and general factor loadings does not allow for simple cross-sectional averaging to produce a consistent estimate of the factors, the idea can be generalised using principal components analysis. Given large _n_ and _T_ , the principal components approach estimates the space spanned by the factors, even though the factors themselves are not estimated consistently. Put differently, _Ft_ is estimated consistently up to premultiplication by an arbitrary nonsingular _r × r_ matrix. The resulting normalisation problem can be resolved by imposing the restriction that Λ<sup>_′_</sup> Λ = _Ir_ . Given that this restriction is chosen arbitrarily, the factors cannot be directly interpreted in an economic sense. For most parts, we will work with the reduced-form DFM, making the normalisation inconsequential. 

More generally, principal component analysis provides the factors that explain the most variation in the data, while at the same time avoiding an information overlap between the factors as they are orthogonal to each other<sup>7</sup> . 

> 7See Stock and Watson (2016) for further details on the estimation of DFMs. 

10 

### **2.3** 

This section turns to the identification of the monetary policy shocks in the DFM. As is well known, estimations of monetary policy suffer from an identification problem, as monetary policy contemporaneously reacts to other variables in the model. To find the part of the variation in monetary policy that is orthogonal to other variables, various approaches have been proposed in the literature. In traditional VAR-type models, researchers have typically imposed some internal structure on the coefficients in the VAR, such as timing restrictions or sign restrictions. More recently, Olea and Watson (2012) as well as others have proposed an additional method, where information from outside the VAR is used to identify monetary policy. In the so-called external instrument approach, an instrument is employed that is correlated with the structural shock that the researcher tries to uncover, while being uncorrelated with all other shocks in the system. This corresponds to the standard assumptions of relevance and exogeneity in the instrumental variables literature. 

The main concept behind using an external instrument is that when regressing the VAR innovations _ηt_ on the instrument _Zt_ , the fitted value of the regression identifies the structural shock—up to sign and scale. In fact, as this approach uncovers the covariance between _ηt_ and _Zt_ , a regression of the instrument on the VAR innovations would equally uncover the structural shock. 

Following the VAR literature and the notation in Stock and Watson (2012), we model a linear relationship between the VAR innovations _ηt_ and the structural shocks _ϵt_ : 



where _H_ is a matrix of coefficients and _H_ 1 is the first column of _H_ . It follows that Σ _ηη_ = _H_ Σ _ϵϵH_<sup>_′_</sup> , with Σ _ηη_ = _E_ ( _ηtηt_<sup>_′_)andΣ</sup><sup>_ϵϵ_=</sup><sup>_E_(</sup><sup>_ϵtϵ′_</sup> _t_<sup>).Ifthesystemisinvertible—astandard</sup> assumption in the VAR literature—structural shocks can be expressed as linear combinations of innovations: 



The main interest in the DFM, as in other VAR-type models, lies in uncovering impulse response functions (IRFs) to a specific shock. To find the impulse response function of _Xt_ with respect to the _i_<sup>_th_</sup> structural shock, we can use equations 3 and 5 to get 



11 

Substituting 6 into 1, we find that 



where the IRF is ΛΦ( _L_ )<sup>_−_1</sup> _H_ . Λ and Φ( _L_ ) are already identified from the reduced form, equation 2, which we can estimate via ordinary least squares. However, this leaves the identification of _Ht_ , which is dealt with in the next section. 

As mentioned above, we identify the shock of interest, say _ϵ_ 1 _t_ , using the instrumental variable _Zt_ . The necessary conditions are: 

1. Relevance: _E_ ( _ϵ_ 1 _tZt_ ) = _α_ = 0 

2. Exogeneity: _E_ ( _ϵjtZt_ ) = 0, _j_ = 2 _, ..., r_ 



where _D_ is an _r × r_ matrix. The last condition is the standard structural VAR assumption that structural shocks are uncorrelated. This assumption does not fix the variance of shocks. From equation 4 we get 



where the last identity follows from the relevance and exogeneity conditions. It follows that _H_ 1 is identified up to scale and sign by the covariance between the VAR innovations and the instrument. To identify the shocks themselves, we need the third condition on uncorrelated shocks. It implies that we can rewrite the varianance-covariance matrix of _ηt_ as 



Moreover, defining by Π the matrix of coefficients from the population regression of _Zt_ on _ηt_ , the fitted value of this regression is 



which, using equation 8 and 9, can be written as 



12 

By simplifying and using equation 5, we obtain 



Finally, we note that _H_<sup>_−_1</sup> _H_ 1 = _e_ 1, where _e_ 1 = (1 _,_ 0 _, ...,_ 0)<sup>_′_</sup> , which implies that 



This conforms with the original statement that the fitted value of a regression of the instrument on the innovations, i.e. Π _ηt_ , identifies the structural shock _ϵ_ 1 _t_ up to a constant. For additional intuition, Stock and Watson (2012) point out that if the structural shocks _ϵt_ were observable and we could hence regress the instrument on the structural shocks, the predicted value would again uncover the shock _ϵ_ 1 _t_ , up to scale, as the coefficients on all other elements of _ϵt_ would be zero. This follows from the relevance and exogeneity conditions of the instrument. Equation 13 shows that the projection of _Zt_ on _ηt_ provides the exact same result, uncovering _ϵ_ 1 _t_ . Note that to estimate the structural shock, we use the sample analogue of the above equation. 

#### **2.3.1 Instrument - “Scripta Volant, Verba Manent”**<sup>8</sup> 

To obtain an instrument that fulfills the necessary requirement of only being correlated with the monetary policy shock, we build a new series of high frequency surprises around ECB policy announcements. The key idea is that by choosing a narrow time window around policy announcements, any surprises occurring within the window are most likely only associated with monetary policy shocks. Put differently, the assumption is that no other major structural shocks occur during the chosen window around the policy announcement. Correspondingly, all endogenous monetary policy, i.e. all expected monetary policy, is assumed to already have been priced in before the window starts. Consequently, endogenous monetary policy would not cause a change in the instrument at the time of the announcement. 

For the instrument we choose changes in the 1-year Euro Overnight Index Average (EONIA) swap rate. The logic goes that while expectations about future policy rate changes are already priced in, unexpected policy shocks will cause the swap to appreciate or depreciate instantly. If market participants, for example, expect a hike in the policy rate by a certain amount, the announcement of such a hike will not cause the 1-year EONIA swap 

> 8The original quotation ( _Verba volant, scripta manent_ ), attributed to Caius Titus, roughly translates as “spoken words fly away, written words remain.” We find that, on the contrary, it is often the spoken word of the ECB President during the press conference and Q&A session, which has a larger impact on markets than the written word of the monetary policy press release. 

13 

rate to move. However, should a hike or cut be out of line with expectations, the swap rate will adjust as soon as the announcement is made. Similarly, any policy action that changes expectations about future rate movements—often termed ‘forward guidance’—will have an impact on the swap. Lloyd (2017a) and Lloyd (2017b) demonstrates that 1 to 24-month Overnight Indexed Swap (OIS) rates accurately measure interest rate expectations. As our chosen EONIA swap rate is the corresponding OIS rate for the euro area, this finding is directly applicable to our instrument, allowing us to capture not only current monetary policy, but also expectations about the future path of monetary policy. 

When deciding on the tenor of the EONIA swap, two considerations have to be taken into account. Firstly, to capture how a monetary policy shock affects interest rates across the whole yield curve, a longer dated swap is better suited compared to one with a shorter tenor. On the other hand, however, term premia play a larger role at longer horizons, potentially contaminating the information about future short rates. In dealing with this trade-off, we choose the 1-year rate, based on the observation that 1-year rates are highly sensitive to monetary policy, while still remaining relatively unaffected by term premia. That said, we also construct instruments based on 3-month, 6-month and 2-year EONIA swaps and do not find a significant difference in our results. 

For their high frequency analysis of US monetary policy, Gertler and Karadi (2015) choose a window of 30 minutes around the policy announcement (starting 10 minutes before the Federal Open Market Committee (FOMC) announcement and ending 20 minutes after). The main policy announcement of the FOMC contains a large amount of information about the decision as well as the view of the committee about the state of the economy and expectations of future policy action. This means that within the 30 minute window, the market can fully integrate recent policy changes and adjust the price of the instrument. The procedure of policy releases is somewhat different at the ECB, as also recently pointed out by contemporaneous work by Jarocinski and Karadi (2018) and Altavilla et al. (2019). The release of the monetary policy decision at 13:45 CET only contains a limited amount of information on the latest policy actions. A significant amount of information is disseminated to the market at a later stage, through the press conference and Q&A with the President, starting at 14:30 CET. For this reason, we decided to extend the window for our analysis to cover not only the prime release, but also the press conference. Specifically, we choose a 6-hour window from 13:00 to 19:00 CET.<sup>9</sup> 

> 9The press conference typically lasts for only one hour, implying that the window could be more narrowly defined, ending, e.g. at 16:00 CET. We chose not to do so due to data availability issues. Specifically, intraday data on swap prices on Bloomberg are available only from January 2008 onwards. In other words, we would have been able to create an instrument only from 2008 using intraday data. For a window from 

14 



<!-- Start of picture text -->
4 . 65<br>4 . 6<br>4 . 55 Press release →<br>4 . 5<br>4 . 45<br>4 . 4<br>4 . 35 ← Q&A session<br>4 . 3<br>9:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00 18:00 19:00<br>1Y EONIA swap rate<br><!-- End of picture text -->

**Figure 1:** 1-year EONIA swap rate on 5 June 2008. Horizontal axis shows Central European Time (CET). Source: Bloomberg, authors’ calculations. 

Figures 1 and 2 show examples of characteristic movements in the 1-year EONIA swap on ECB meeting days, highlighting the importance of including the Q&A in the high-frequency window if one wants to study the effect of all monetary actions. On 5 June 2008, the Governing Council of the ECB decided that policy rates will remain unchanged. As this was in line with market expectations, the 1-year EONIA swap rate did not move much in reaction to the press release at 13:45 CET. During the press conference however, the president expressed concern about increased risks to price stability, setting expectations of rate hikes in the near future. In reaction to this information, the swap rate immediately jumped higher and over the afternoon increased by 27 basis points. This example clearly demonstrates that information about ECB policy information can to a large degree be contained in the press conference, compared to the policy announcement. An example where both the original announcement, as well as the press conference convey substantial information to market participants is the meeting on 6 October 2011. The press release once again stated that rates would remain unchanged. However, this was not in line with market expectations for a cut and hence created a tightening surprise that led to an immediate increase in the 1- year EONIA swap rate. During the press conference, the then ECB President Jean-Claude Trichet re-emphasised that inflation rates had remained at elevated levels. This in turn pushed market expectations towards tighter monetary policy and caused a further jump in 

13:00 to 19:00 CET, however, this problem does not arise as these times correspond to the closing times of the Tokyo and London stock exchanges, respectively. Hence it is possible to obtain end-of-day data, which is available from 2001, and create a _de-facto_ intraday window from 13:00 to 19:00 CET. For the subsample of overlapping observations (2008-2016) we tested for the difference in using the window ending with the press conference vs. later the same afternoon and found it to be statistically insignificant. 

15 



<!-- Start of picture text -->
0 . 75<br>Press release →<br>0 . 7<br>0 . 65<br>← Q&A session<br>0 . 6<br>9:00 10:00 11:00 12:00 13:00 14:00 15:00 16:00 17:00 18:00 19:00<br>1Y EONIA swap rate<br><!-- End of picture text -->

**Figure 2:** 1-year EONIA swap rate on 6 October 2011. Horizontal axis shows Central European Time (CET). Source: Bloomberg, authors’ calculations. 

the swap rate. Naturally, there are also examples where the press conference does not convey a significant amount of information to the market, but the above cases highlight the need to include the press release in the high-frequency window. 

The above discussion raises the question to which degree the various forms of information dissemination could be used to develop a more differentiated understanding of the nature of policy shocks. On one hand, Jarocinski and Karadi (2018) have suggested a separation of monetary policy _instrument_ shocks from monetary policy _communication_ shocks, sometimes also termed _target_ and _path_ shocks. On the other hand, Altavilla et al. (2019) have separately constructed monetary surprises for the press release and Q&A event window. For the purpose of our paper, we want to use a broad measure of monetary policy shocks that encompasses all forms of surprises related to monetary actions. 

As we estimate a quarterly VAR, we have to turn the surprises on ECB meeting days into quarterly average surprises. In practice, we first calculate the cumulative daily surprise over the past quarter (93 days) for each day in our sample. In the next step we take the average of this daily cumulative series over each quarter. In doing so, we incorporate the information that some meetings happen early within a quarter while others happen later. Our averaging procedure makes sure that a surprise happening late in the quarter has less influence on the quarterly average than a surprise at the beginning of the quarter.<sup>10</sup> 

To get a better understanding of our instrument, we plot its time series in Figure 3. In particular, we want to point out events that led to particularly large positive or nega- 

> 10A similar approach was taking by Gertler and Karadi (2015) to create monthly FOMC surprises. 

16 

tive values in the instrument to develop an intuition regarding the behaviour of the series. Proceeding chronologically, the earliest of the four largest surprises happened in the fourth quarter of 2001, with a value of -0.15. This data point is driven by the aggressive interest rate cut on 17 September 2001, in response to the 9/11 terrorist attacks.<sup>11</sup> The ECB cut all three interest rates by 50bp leading to a drop in 1-year EONIA swaps of 20bp during our window. Another particularly large negative shock appears in the fourth quarter of 2008. The value of -0.17 is mostly driven by the monetary policy decision on 2 October 2008. Interest rates were kept unchanged on the day, in line with expectations. However, President Trichet highlighted financial market turmoil and weakness in the EA economy during his statement, leading to a large drop in the swap rate between 14:30 and 15:30 CET as markets priced in future cuts to the policy rate. In the following quarter, Q1 2009, our instrument records a particularly high reading of 0.14. This goes back in large part to a contractionary monetary policy surprise during the meeting of 4 December 2008, but also to a surprise during the meeting of 15 January 2009. Interestingly, during both meetings, which happened at the height of the financial crisis, interest rates were cut—by 75bp and 50bp, respectively. While this led to momentarily lower swap rates on both occasions, rhetoric during the press conference led to further increases in the rate. In fact, on both occasions, the President’s various dovish and hawkish comments led to the rate moving up and down, but the contractionary sentiment dominated overall. Finally, we investigate the events driving our instrument during Q3 2011. The negative value of -0.22—the largest value in absolute terms during our sample period—mainly goes back to the policy decision on 4 August 2011. After an interest rate hike at the previous meeting, policymakers left interest rates unchanged on the day. As this was in line with expectations, the swap rate did not move at 13:45 CET. During the press conference, however, the ECB announced the decision to conduct a liquidity-providing supplementary longer-term refinancing operation (LTRO), based on observed tensions in financial markets within the euro area. This policy action amounted to a large dovish surprise and 1-year EONIA swaps fell by about 18bp between 14:30 and 15:30 CET. 

Finally, we test the strength of our instrument. We do so in a small VAR containing only three variables: output, consumer prices and a policy indicator. The model is specified both at monthly and quarterly frequency and is identified using high-frequency instruments based on 3, 6 and 12-month EONIA swaps. We report further details and all results in Online Appendix B, but note here that in our baseline specification the instrument is strong, with a first-stage F-test statistic of 19.45. This confirms the relevance of our external instrument. 11Note that the surprise actually happened in the third quarter of 2001. However, because our averaging approach takes into account whether a shock appears early or late in a quarter—and consequently, whether it has a larger influence on the current or the next quarter—the policy decision from 17 September 2001 mostly affects our instrument during Q4 2001. 

17 



<!-- Start of picture text -->
0 . 15<br>0 . 1<br>0 . 05<br>0<br>− 0 . 05<br>− 0 . 1<br>− 0 . 15<br>− 0 . 2<br>− 0 . 25<br>2001 Q1 2003 Q1 2005 Q1 2007 Q1 2009 Q1 2011 Q1 2013 Q1 2015 Q1 2016 Q4<br>1Y EONIA swap rate surprises<br><!-- End of picture text -->

**Figure 3:** Instrument - Quarterly 1-year EONIA swap rate surprises from 2001Q1 to 2016Q4 

### **2.4 Data and Estimation** 

Our data set consists of quarterly observations from 1999 Q4 to 2016 Q4 on 90 area-wide measures such as prices, output, investment, employment and housing, as well as 342 individual country time series for the 11 early adopters of the Euro: Austria, Belgium, Finland, France, Germany, Ireland, Italy, Luxembourg, the Netherlands, Portugal and Spain. The vintage of the data is June 2017. Appendix A lists all data series with detailed descriptions and notes on the completeness and length of the individual series. 

All data series are transformed to induce stationarity. Depending on the nature of the data, this was done either by taking the first difference in logs or levels. Details on transformations can also be found in Appendix A. As we lose one observation by differencing, our working dataset starts in 2000 Q1. 

Principal component analysis is sensitive to double-counting<sup>12</sup> and we consequently only use a subset of our data for factor extraction. In practice, we avoid double-counting along two dimensions. Firstly, we do not include euro-area aggregates for indicators where we have included all individual country series. Secondly, we do not include category aggregates, such as GDP, when we have included its components, such as the components of GDP. Where possible, we avoid using high-level aggregate series altogether and instead include disaggregate series. In total, we use 179 series for factor extraction. 

We rely on a number of specific tests and information criteria to determine the number of common factors _r_ . Specifically, we estimate them by means of the test proposed by Onatski (2009), which suggests _r ∈_ 2 _,_ 3 (Table 1), the eigenvalue difference method proposed by 

> 12See e.g. Stock and Watson (2012). 

18 

**Table 1:** Determining the number of common factors: Onatski (2009) test. The Table shows p-values of the null of _q_ 0 common shocks against _r_ 0 _< r ≤ r_ 1 common shocks. 

|_r_0 **vs** _r_0 _< r ≤r_1|1|2|3|4|5|6|7|
|---|---|---|---|---|---|---|---|
|0|0.727|0.089|0.122|0.153|0.18|0.209|0.232|
|1|0|0.05|0.089|0.122|0.153|0.18|0.209|
|2|0|0|0.521|0.414|0.539|0.632|0.705|
|3|0|0|0|0.229|0.414|0.539|0.632|
|4|0|0|0|0|0.794|0.595|0.746|
|5|0|0|0|0|0|0.336|0.595|
|6|0|0|0|0|0|0|0.561|



Onatski (2010) suggesting _r_ = 2, the criterion by Bai and Ng (2002) suggesting _r_ = 5, and the bi-cross-validation method proposed by Owen et al. (2016)<sup>13</sup> suggesting _r_ = 8. We choose as our baseline specification _r_ = 5, that is, the average of these results. Figure **??** in Online Appendix A shows the variance of the data explained by each additional factor. Five factors account for 80 percent of the total data variance.<sup>14</sup> 

On the basis of Akaike and Bayes Information Criteria we include one lag for the baseline of the DFM. 

To get a better understanding of how well the extracted factors characterise the data, Table 2 shows the variation in the data explained by the five factors. The second column shows the fraction of explained variation for a selection of aggregate area-wide series. The third column shows the corresponding average across series from individual member countries. In particular, two observations stand out. Firstly, the variation in most aggregate series is remarkably well explained by the five factors. With a few exceptions, notably the exchange rate, the R-squared ranges between 70 percent and 99 percent. Secondly, despite the granularity of the individual country series, the factors on average still explain more than half of all variation. In some cases, such as HICP inflation, government spending and, most notably, long-term interest rates, they explain considerably more. Columns 4 and 5 show the same information as column 3, but differentiate between the size of the countries. In particular, we separate the 5 countries in our sample with the largest economies (by nominal GDP) from the 6 countries with the smallest economies. As expected, the factors pick up 

> 13see Figure **??** in Online Appendix A. 

> 14As can be seen in Figure **??** , the bulk of the variance in the data is explained by the first two factors. In line with this observation and the test results from Onatski (2009) and (2010), we re-estimate the DFM with only two factors. We find that all main results of the 5-factor model hold. While the smaller amount of factors allow for greater precision, the larger amount of factors gives us more explanatory power for the observable series. We prefer the latter effect over the former and hence select 5 factors for our baseline specification. 

19 

**Table 2:** R-squared for regression of data series on five principal components. *Germany, France, Italy, Spain, Netherlands. **Belgium, Austria, Ireland, Finland, Portugal, Luxembourg. 

||EA<br>aggregate|Average across<br>individual<br>country series|Average across<br>large* countries|Average across<br>small** countries|
|---|---|---|---|---|
|Gross Domestic Product|0.85|0.56|0.70|0.45|
|Harmonised Index of<br>Consumer Prices|0.81|0.64|0.71|0.59|
|Housing Prices|0.71|0.46|0.52|0.40|
|Exports|0.76|0.54|0.49|0.58|
|Imports|0.75|0.58|0.45|0.69|
|Government Spending|0.18|0.68|0.77|0.59|
|Gross Fixed<br>Capital Formation|0.76|0.33|0.51|0.19|
|Consumption|0.61|0.30|0.34|0.27|
|Unemployment|0.72|0.51|0.68|0.36|
|Long-term Rates|0.99|0.98|0.98|0.98|
|Rents|0.41|0.35|0.32|0.38|
|Share Prices|0.65|0.58|0.59|0.57|
|Producer Prices in Industry|0.87|-|-|-|
|Wages|0.75|-|-|-|
|Employment|0.74|-|-|-|
|GER 2Y yield|0.98|-|-|-|
|Cost of Borrowing indicator|0.91|-|-|-|
|EONIA|0.99|-|-|-|
|Nominal Efective<br>Exchange Rate|0.12|-|-|-|



20 

information from the large economies to a much greater extent than for smaller economies. With the exception of exports, imports and rents, data from larger economies is consistently explained better by the factors. This difference is particularly strong for GDP (70 percent vs. 45 percent) and unemployment (68 percent vs. 36 percent). As concrete examples of the above, Figure **??** in Online Appendix D plots fitted series on the basis of the 5 extracted factors against actual (transformed) series for GDP and HICP in the euro area, Germany and Luxembourg. 

## **3 Empirical Results** 

This section gives an overview of our empirical findings, starting at the aggregate level for the euro area and subsequently exploring results on the country level. 

### **3.1 Euro-wide Dynamic Effects of Monetary Policy** 

We start our description of the results with an overview of a selection of aggregate series across the euro area. Figure 4 shows percentage responses to a contractionary monetary policy shock of 25 basis points (bp). As discussed in Section 2.3, the external instrument approach identifies the shock only up to sign and scale. Using the response of EONIA as a policy indicator, we scale the system to a 25bp contraction in EONIA. The shaded area around the point estimates signify confidence intervals of one standard deviation, obtained from a wild bootstrapping procedure with a simple (Rademacher) distribution. Given a strong instrument, the confidence intervals obtained under this approach are valid despite the presence of heterogeneity. Because both stages of the regression are incorporated in the bootstrapping procedure, the error from the external instrument regression is accounted for. A similar approach has been followed by Mertens and Ravn (2013) and Gertler and Karadi (2015). 

Notably, our results do not suffer from the prize puzzle—the occurrence of rising prices in reaction to a contractionary monetary policy shock. In fact, while the harmonised index of consumer prices (HICP) does not have any significant reaction, our producer prices fall significantly, in line with economic theory. Given the longstanding struggle of VAR-type models to get rid of the price puzzle, we interpret these findings as an indication of the ability of the model to accurately characterise economic dynamics. In particular, we attribute the non-existence of the price puzzle to the combination of correctly capturing information about prices in the economy (via the DFM) and precisely identifying monetary policy shocks (via 

21 

the high frequency instrument).<sup>15</sup> The remainder of the series in Figure 4 also behave as suggested by theory. GDP contracts overall, as do all components with the exception of Government Spending, which moves in the opposite direction of the monetary shock. In line with theory, investment (GFCF) is a lot more volatile than consumption, as are imports and exports. The reaction of the German 2-year sovereign yield closely follows EONIA. The aggregate indicator for mortgage interest rates in the euro area as compiled by the ECB also rises in reaction to a shock, but displays imperfect pass-through as a significant number of mortgages are characterised by fixed rates that do not adapt to changes in policy. In the labour market, unemployment rises, while wages fall. Interestingly, the reaction in wages is not significant, hinting at a large degree of nominal wage stickiness. In the housing market, housing prices fall significantly after a contraction, following economic theory that higher policy rates make mortgages more expensive and consequently suppress demand for houses. Rents, on the other hand, increase in reaction to a shock. Recent research (see e.g. Dias and Duarte (2019)) suggests that a worsening of conditions in the mortgage market leads agents to substitute house purchase with renting, thus exerting pressure on rental prices. The euro exchange rate appreciate, although only with a delay. 

> 15We also applied the FAVAR approach proposed by Bernanke et al. (2005) using EONIA as the only observable factor and found that the price puzzle was still present 

22 



<!-- Start of picture text -->
20 20 20 20<br>10 10 10 10<br>Rents Wages NEER<br>Producer Prices in Industry 0 0 0 0<br>0.5 0 -0.5 -1 0.1 0.05 0 0.2 0 -0.2 -0.4 1 0.5 0 -0.5<br>20 20 20 20<br>10 10 10 10<br>HICP<br>House Prices<br>Unemployment<br>Mortgage Interest Rates<br>0 0 0 0<br>0.1 0 -0.1 -0.2 0.5 0 -0.5 -1 0.05 0 -0.05 0.2 0.1 0 -0.1<br>20 20 20 20<br>10 10 10 10<br>GFCF<br>Imports<br>Consumption GER 2Y yield<br>0 0 0 0<br>0.2 0 -0.2 -0.4 1 0 -1 -2 0 -1 -2 -3 0.4 0.2 0 -0.2<br>20 20 20 20<br>10 10 10 10<br>GDP<br>Exports EONIA<br>Government Spending<br>0 0 0 0<br>0.5 0 -0.5 -1 0.2 0.1 0 -0.1 2 0 -2 -4 0.4 0.2 0 -0.2<br><!-- End of picture text -->

23 



<!-- Start of picture text -->
0 0.2<br>0.15<br>-0.5 0.1<br>0.05<br>0<br>-1<br>-0.05<br>-0.1<br>-1.5<br>-0.15<br>0 5 10 15 20 0 5 10 15 20<br><!-- End of picture text -->

**Figure 5:** Percentage responses of real GDP and HICP to a 25bp contractionary policy shock across euro-area member countries. 

### **3.2 Cross-Country Dynamic Effects of Monetary Policy** 

Moving on to results at the country level, we start to uncover the full potential of the DFM when it comes to providing results for a large number of series. Of the 342 individual country series in our data set, we have selected a representative sub-sample for Figures 5-7. In particular, this section takes a closer look at the responses of GDP, the components of GDP, interest rates, equities, housing prices and unemployment. We point out, however, that the model produces impulse response functions for all series in our sample.<sup>16</sup> 

Figure 5 shows the responses of real GDP and HICP across the 11 euro-area countries in our sample. While we omitted error bands for ease of presentation, it is noteworthy that reactions of real GDP and HICP across countries appear to be quite heterogeneous.<sup>17</sup> In terms of HICP, the responses are positive for half of the countries while they are negative for the other half. In addition, the mean HICP response is negative and very low, which makes the relative distance of responses quite large when compared to that of real GDP. Turning to real GDP, at one end of the spectrum, the reaction of Irish GDP clearly differs from the five countries with the weakest reaction. That said, even the reactions of Finland and Luxembourg are statistically different from France and Spain, having non-overlapping 

> 16Given that the time period used for the estimation of the DFM includes both the global financial crisis and the European debt crisis, a natural concern is whether the heterogeneity in monetary transmission was largely driven by these events. In Appendix B, we provide a sub-sample robustness check where we split the sample into before and after the financial crisis and estimate the DFM separately for both sub-samples. We find that the main conclusions remain the same. The heterogeneity in monetary transmission remains large for variables related to private consumption, housing and labor in the period preceding the great recession 17Later on in the text, we propose a methodology to assess heterogeneity based on coefficients of variation. 

24 



<!-- Start of picture text -->
1<br>0<br>0<br>-0.2 -1<br>-2<br>-0.4<br>-3<br>-0.6<br>-4<br>-0.8 -5<br>0 5 10 15 20 0 5 10 15 20<br>6 2<br>4<br>1<br>2<br>0<br>0<br>-1<br>-2<br>-4 -2<br>0 5 10 15 20 0 5 10 15 20<br><!-- End of picture text -->

**Figure 6:** Percentage responses of GDP components to a 25bp contractionary policy shock across euro-area member countries. 

confidence intervals from the 10th step onward. This heterogeneity is in itself noteworthy, but also raises the question which parts of the economy are particularly prone to asymmetric reactions. 

For a first pass at this question, Figure 6 contains the reactions of the components of GDP. The IRFs highlights two main observations. Firstly, the responses of national private consumption and gross fixed capital formation, have the same sign and follow similar patterns. In contrast, the responses of national government spending and net exports do not have the same sign. In part, these differences in the general nature of responses can be explained by the determinants of the individual series. Government spending, for example, is notoriously idiosyncratic, depending on the degrees of pro- and counter-cyclicality of fiscal 

25 



<!-- Start of picture text -->
0.3 0<br>-2<br>0.2<br>-4<br>0.1<br>-6<br>0<br>-8<br>-0.1<br>-10<br>0 5 10 15 20 0 5 10 15 20<br><!-- End of picture text -->

**Figure 7:** Percentage responses of long-term interest rates and local equity indices to a 25bp contractionary policy shock across euro-area member countries. Long-term interest rates are defined in accordance with OECD methodology, conforming to government bonds of (in most cases) 10 year maturity. 

policy that tend to vary both across countries and over time. 

Secondly, whether or not the responses move in the same direction, there is a visible degree of heterogeneity. In particular, consider the disparity in the reaction of private consumption. While the drop in private consumption reaches a maximum at about 0.02 percentage points in Germany, the drop in Ireland is more than 20 times as large, at 0.4 percentage points. Aside from Ireland, which could be considered an outlier, the drop in consumption in Italy, Finland, Spain and Portugal is roughly 10 times the size of the drop in Germany. 

In some notable cases, we find that the degree of heterogeneity in the impulse responses may reflect (inversely) the state of convergence in particular markets across the euro area. In particular, financial markets have experience a relatively stronger convergence than other markets.<sup>18</sup> This can be seen in the reaction of interest rates and stock prices across countries. Figure 7 shows that, while the response of long-term interest rates to a policy shock is not uniform across countries on impact, it converges and become almost identical over time. By the same token, while the responses of national equity indices, displayed in the same figure, does not converge across equity markets, the confidence intervals around the IRF are mostly overlapping. 

Among the markets with records of little or no convergence in institutional characteristics are the labour and housing markets. In Figure 8, we show that, after one year (4 steps) the 18 see e.g. ECB (2017). 

26 



<!-- Start of picture text -->
1 0.2<br>0.5 0.1<br>0 0<br>-0.5 -0.1<br>-1 -0.2<br>-1.5 -0.3<br>0 5 10 15 20 0 5 10 15 20<br><!-- End of picture text -->

**Figure 8:** Percentage responses of housing prices and unemployment rate to a 25bp contractionary monetary policy shock across euro-area member countries. 

shocks, housing prices fall and unemployment rises at quite different rates across border.<sup>19</sup> To gain a firmer insight on the degree of heterogeneity in the impulse responses across countries, in what follows we propose and implement a more rigorous approach to testing. For each set of responses, we calculate the coefficient of variation, i.e. the standard deviation of responses (among countries) with respect to the EA response of the same variable. To make this measure comparable across different series, we normalise it by the size of the EA response. By doing so, we create a numerical measure for the dispersion of impulse responses that allows for intuitive and meaningful comparison between series. Table 3 reports the coefficients of variation for a selection of variables, evaluated on impact, as well as at the 8th and the 20th step. The table also reports a lower and a upper bound for the coefficients of variation, which we obtain from our bootstrapping procedure. The table shows that longterm interest rates and stock prices have a much smaller coefficient of variation than the other variables, in line with our discussion above suggesting a lower degree of heterogeneity for financial than for real variables. Remarkably, however, the table also shows that at the 20th step, GDP is also less heterogeneous than other real variables, namely private consumption and unemployment. 

> 19Online Appendix E proposes an alternative representation of our result, to highlight the statistical significance of differences across IRFs. Figures **??** and 14 plot the highest and the lowest national response, together with the IRFs for the whole EA, showing confidence intervals. Figure **??** plots IRFs for real variables: GDP, private consumption and unemployment. Figure 14 plots IRFs for price-related series: interest rates, HICP and stock prices. The confidence intervals for the highest and the lowest IRS do not overlap for the real variables. In contrast, they are overlapping for most parts of the price-related series, with the exception of stock prices, which are diverging around the 10th step. 

27 

**Table 3:** Coefficient of variation of the cross-country responses to a 25bp monetary policy shock. 

|Variable|Coefcient<br>of<br>Variation|Lower<br>Bound|Upper<br>Bound|
|---|---|---|---|
|**On Impact**||||
|GDP|1.45|0.70|4.00|
|Private Consumption|1.19|1.01|2.52|
|Unemployment Rates|7.16|2.83|25.02|
|Housing Prices|2.03|1.51|4.57|
|HICP|3.24|0.99|13.25|
|Long-term Interest Rates|0.21|0.14|0.53|
|Stock Prices|0.37|0.21|0.65|
|**At the 8th Step**||||
|GDP|0.74|0.56|1.10|
|Private Consumption|1.01|0.99|1.12|
|Unemployment Rates|1.57|1.08|3.00|
|Housing Prices|1.20|0.84|3.57|
|HICP|1.69|0.80|6.00|
|Long-term Interest Rates|0.96|0.28|3.36|
|Stock Prices|0.20|0.18|0.22|
|**At the 20th Step**||||
|GDP|0.64|0.47|0.95|
|Private Consumption|1.02|0.99|1.11|
|Unemployment Rates|1.24|0.94|4.22|
|Housing Prices|1.08|0.84|2.02|
|HICP|1.25|0.62|4.05|
|Long-term Interest Rates|0.46|0.17|1.87|
|Stock Prices|0.21|0.19|0.26|



As some of the intervals around coefficients of variation are overlapping, we also bootstrap pair-wise differences in the coefficient of variation. The results, presented in Table 4, mostly confirm earlier observations. Reactions of long-term interest rates (LTINT) and stock prices (SP) are significantly less dispersed than all other variables. Moreover, at the 20th step, GDP has a significantly lower coefficient of variation than private consumption (PCON), unemployment (U), and real housing prices (RHPI). 

Summing up. Our empirical evidence suggests that, in line with our conjecture, heterogeneity in the responses to monetary shocks is lower in financial variables, such as interest rates and stock prices, reflecting a relatively high degree of integration, relative to variables 

28 

related to much less integrated markets, such as the labour and housing markets. We also show that the heterogeneity in the response larger in consumption and consumer prices, than is in the response of output output. Our evidence, showing that in some cases the response can even have a different sign, has straightforward implications for policy. Further institutional convergence can be expected to enhanced cohesion in the euro area, by reducing unintended responses to common monetary stimulus or contraction across countries. That said, a much deeper understanding of the mechanisms at play is necessary to motivate and structure consistent convergence policies. 

**Table 4:** Bootstrapped pair-wise differences in the coefficient of variation of the cross-country responses to a 25bp monetary policy shock. * marks differences in variation that are significant at the 68 percent confidence level. The inference is drawn from a bootstrap procedure. 

||GDP|HICP|LTINT|SP|PCON|U|RHPI|
|---|---|---|---|---|---|---|---|
|**On Impact**||||||||
|GDP|0|-0.99|1.20*|1.06*|0.16|-5.42*|-0.84|
|HICP|1.10|0|3.02*|2.85*|1.69|-3.81|0.66|
|LTINT|-1.19*|-3.02*|0|-0.13|-0.90*|-6.66*|-1.79*|
|SP|-1.04*|-2.85*|0.13|0|-0.84*|-6.84*|-1.60*|
|PCON|-0.16|-1.69|0.90*|0.84*|0|-5.20*|-0.75|
|U|5.32*|3.81|6.66*|6.84*|5.20*|0|5.02|
|RHPI|0.87|-0.66|1.79*|1.60*|0.75|-5.02|0|
|**At the 8th Step**||||||||
|GDP|0|-0.86|-0.23|0.54*|-0.30|-0.73*|-0.44|
|HICP|0.86|0|3.02*|2.85*|1.69|-3.81|0.66|
|LTINT|0.23|-0.60|0|-0.13|-0.90*|-6.66*|-1.79*|
|SP|-0.54*|-1.45*|-0.74*|0|-0.84*|-6.84*|-1.60*|
|PCON|0.30|-0.59|0.10|0.80*|0|-5.20*|-0.75|
|U|0.73*|-0.08|0.65|1.38*|0.51*|0|5.02|
|RHPI|0.44|-0.16|0.49|1.03*|0.18|-0.19|0|
|**At the 20th Step**||||||||
|GDP|0|-0.55|0.21|0.45*|-0.39*|-0.59*|-0.43*|
|HICP|0.55|0|0.64|1.02*|0.19|-0.18|-0.16|
|LTINT|-0.21|-0.64|0|0.24|-0.60|-0.99*|-0.62|
|SP|-0.45*|-1.02*|-0.24|0|-0.80*|-1.04*|-0.85*|
|PCON|0.39*|-0.19|0.60|0.80*|0|-0.20|0.00|
|U|0.59*|0.18|0.99|1.04*|0.20|0|0.20|
|RHPI|0.43*|0.16|0.62|0.85*|0.00|-0.20|0|



29 

## **4 Quantifying How Mortgage Markets Shape Monetary Transmission** 

A growing body of literature has recently reconsidered a “housing channel” in the transmission of monetary policy (Iacoviello (2005), Calza et al. (2013), Greenwald (2018), Wong (2019), Beraja et al. (2019), Cloyne et al. (2019) and Slacalek et al. (2020)). The importance of this channel is commonly motivated by noting that, for most households, their home is the single most important item on the asset side of their balance sheet, and their mortgage is the household’s largest liability. In this section, we build an small open economy model featuring a housing sector, and use it to investigate the housing channel of monetary policy in a currency union in some detail. Specifically, we will make use of the European institutional setting to explore variation in the housing channel across EA countries, reflecting different characteristics of housing financing across member countries. 

Many institutional characteristics of national housing markets differ substantially across EA members. Mortgage markets display marked variation in the relative share of fixed versus flexible rate contracts and typical loan-to-value ratios; rental markets are subject to different regimes and controls; taxation is very heterogeneous, to name but a few aspects—see Osborne (2005), Andrews et al. (2011) and Westig and Bertalot (2016) for a comprehensive overview. The importance of these differences for monetary policy transmission in Europe has not gone unnoticed, and previous literature, most notably Calza et al. (2013), has produced empirical and qualitative assessments. However, to our knowledge, there is no quantitative assessment using a fully calibrated model. 

In what follows, we study quantitatively how much of the variation in individual EA country responses to a monetary policy shock can be explained by differences in mortgage market characteristics. First, we describe the model, focusing on a set of institutional parameters that affect housing financing, namely the loan-to-value ratio and the share of adjustable-rate mortgage contracts. Our analysis merges the main elements of Calza et al. (2013) into a small open economy modeled after De Paoli (2009). Doing so allows us to quantitatively assess the importance of differences in institutional characteristics of mortgage markets in the transmission of monetary policy. Second, we calibrate the model to the Spanish economy in order to get empirically plausible long-term moments and impulse response functions to monetary policy shocks. Finally, we feed the model with the loan-to-value ratios and shares of adjustable-rate mortgage contracts observed in the data for each country, and compare the dispersion from these simulated IRFs with the dispersion we estimated using the DFM in the previous section. 

30 

### **4.1 Model** 

The economy features three types of agents — savers, fixed-rate borrowers, and variable— rate borrowers, as proposed by Rubio (2011) and a collateral constraint in line with Campbell and Hercowitz (2005), Iacoviello (2005), Iacoviello and Neri (2010), and Liu et al. (2010). Savers are standard Ricardian agents who own all firms in the consumption and housing sectors as well as financial intermediaries, while borrowers are credit constrained in equilibrium and behave as hand-to-mouth consumers. As customary in the literature, we assume that the domestic economy is so small relative to the rest of the EA that domestic economic dynamics are irrelevant for equilibrium outcomes in the rest of the EA (see e.g. De Paoli (2009)). 

#### **4.1.1 Patient Households** 

There is a continuum of measure 1 of patient agents. Their economic size is measured by their wage share, which is assumed to be constant reflecting a Cobb-Douglas production function with unit elasticity of substitution. A representative patient household maximizes: 



where _β_ is the discount factor, _ct_ is consumption of goods other than housing, _j_ is a housing preference over consumption parameter, _ζ_ captures consumption habit formation, _θ_ indicates the elasticity of substitution between working in the consumption or housing sectors, and _ψ_ is the inverse Frisch elasticity of labor supply. _nc,t_ and _nh,t_ denote hours worked in the consumption and housing sectors, respectively, and _ht_ denotes the consumption of housing services. The consumption of goods _ct_ is a bundle of home and foreign goods with the following form: 



Here _ν ∈_ [0 _,_ 1] measures the home bias in consumption<sup>20</sup> . Here, the bundles of Home- and Foreign-produced goods are defined as follows: 



20 This specification of home bias follows Sutherland (2005) and De Paoli (2009). With _ν_ = 1, there is no home bias. If the relative price of foreign and domestic goods is unity, Home‘s consumption basket contains a share _n_ of Home-produced goods and a share (1 _− n_ ) of imported goods. A lower value of _ν_ implies that the fraction of domestically produced goods in final goods exceeds the share of domestic production in the world economy. Hence, in the other extreme case, if _ν_ = 0, there is full home bias and no trade across countries. 

31 

where _cH,t_ ( _j_ ) and _cF,t_ ( _j_ ) denote differentiated intermediate goods produced in Home and Foreign, respectively, and _ε >_ 1 measures the elasticity of substitution between intermediate goods produced within the same country. 

Patient households own all firms in this economy, accumulate houses and make loans to impatient households. Patient households maximize their utility subject to: 



where _qt_ is the house price, _Wc,t_ is the nominal wage in the consumption sector, _Wh,t_ is the nominal wage in the housing sector, _Rt_ is the gross nominal interest rate, _δh_ is the housing depreciation rate, _πt_ is the inflation rate, _Pt_ is the domestic price level index, _Tt_ is total firm profits and _Qt,t_ +1 is the stochastic discount factor for one-period ahead nominal pay-offs relevant to the domestic household. We assume that patient households have access to a complete set of contingent claims, traded internationally. 

#### **4.1.2 Impatient Households** 

There is a measure 1 of impatient households, a share _ω_ of which have mortgage contracts with variable interest rates, denoted by subscript _v_ , while the remaining 1 _− ω_ possess a fixed-rate mortgage contract, denoted by subscript _f_ . Similarly to patient households, they maximize 



where _β_<sup>_′_</sup> _< β_ , which makes these households impatient. Differently from patient households, they do not own firms nor can they trade contingent claims internationally, and are subject to the following budget and collateral constraints: 



where _m_ is the loan-to-value ratio. In the steady state without uncertainty this last constraint will bind since _β_<sup>_′_</sup> _< β_ . Impatient households with fixed-rate mortgages face _Rf,t_ = _R_<sup>¯</sup> _t_ , while those with variable-rate mortgages face _Rv,t_ = _Rt_ . 

The two key institutional characteristics relevant to housing financing are thus encapsulated in the two parameters _ω_ and _m_ . The first is the share of households that finance their housing purchase with adjustable-rate mortgages, the second is the loan-to-value ratio. 

32 

#### **4.1.3 Relationship among inflation, terms of trade and exchange rate** 

When maximizing utility, households take prices as given. Let _Pt_ ( _j_ ) denote the price that the producer of good _j_ charges in the Home country, denoted in Home currency. Let _Pt_ ( _j_ ) denote the price that the producer charges for the same good in the Foreign country, expressed in Foreign currency. The consumer price indices in Home and Foreign are given by 





where _PH,t_ ( _PH,t_<sup>_∗_)isthepricesub-indexforHome-producedgoodsexpressedindomestic</sup> (foreign) currency and _PF,t_ ( _PF,t_<sup>_∗_) is the price sub-index for Foreign-produced goods expressed</sup> in the domestic (foreign) currency. 





Moreover, we assume that the law of one price holds for intermediate goods, so that 



_ξt_ is the nominal exchange rate measured as the price of Foreign currency in terms of Home currency. A rise in _ξt_ , thus, marks a nominal depreciation from Home‘s perspective. 

Therefore, equations (21), (22) together with condition (25), imply that _PH,t_ = _ξtPH,t_<sup>_∗_</sup> and _PF,t_ = _ξtPF,t_<sup>_∗_.However, as equations (23) and (24) illustrate, the home bias specification</sup> leads to deviations from purchasing power parity, that is, _Pt_ = _ξtPt_<sup>_∗_.Forthisreason,we</sup> denote the real exchange rate by _RSt_ =<sup>_<u>ξt</u>_</sup> _P_<sup>_P_</sup> _tt_<sup>_∗_.</sup> 

Assuming that _n →_ 0, and using the preferences of consumers, we can derive total demand for a generic good _j_ , produced in country _H_ : 



33 

#### **4.1.4 Firms** 

_Consumption Sector_ . Producers of intermediate consumption goods operate under monopolistic competition and face the demand function (26). The production function is given by: 



where _nc,y_ ( _j_ ) and _nc,y_ ( _j_ )<sup>_′_</sup> denote labor services from patient and impatient households, respectively, employed by firm _j ∈_ [0 _, n_ ] in period _t_ . We assume that prices are set in the currency of the producer and that price setting is constrained exogenously a la Calvo, such that in each period only a fraction of intermediate good producers (1 _− φ_ ) may adjust their price. When firm _j_ has the opportunity, it sets _P_<sup>˜</sup> _t_ ( _j_ ) to maximize the expected discounted value of net profits: 



subject to the sequence of demand constraints 



where Λ _t,t_ + _s_ is the stochastic discount factor and _MCt_<sup>_n_</sup> + _s_<sup>denotes the nominal marginal cost.</sup> 

_Housing Sector_ . We rule out nominal rigidities in the housing market. On the one hand, housing is relatively expensive on a per-unit basis, implying large incentives to negotiate on the price. On the other hand, most homes are priced for the first time only when they are sold. 

In the housing sector there is a representative firm that produces residential investment according to the following technology: 



Hence, assuming perfect competition, this firm takes the price of housing as fixed and optimally chooses labor input in order to maximize profits. 



_Financial Intermediaries_ . There is a financial intermediary that accepts deposits from savers and extends both fixed- and variable-rate loans to borrowers. We assume a competitive framework under which the intermediary takes variable interest rates as given. The profits of the financial intermediary are defined as 



34 

In equilibrium, aggregate borrowing and saving must be equal, that is: 



Substituting (33) into (32), one obtains, 



In order for the two types of mortgages to be offered in equilibrium, the fixed interest rate has to be such that the intermediary is indifferent between lending at a variable or fixed rate. Hence, the expected discounted profits from issuing new debt in a given period at a fixed interest rate must be equal to those from issuing at a variable rate. Also, since the financial intermediaries are owned by the savers, their stochastic discount factor is applied in computing the optimal equilibrium value of the fixed rate in period _t_ , given by: 



Hence, new debt issued at date _t_ is associated with a different fixed interest rate set by equation (35). However, this implies that the aggregate return on the whole stock of debt is a function of new debt as well as rates set on past debt. Therefore the aggregate fixed interest rate that a financial intermediary charges at date _t_ is an average of what was charged last period for the previous stock of mortgages and what is charged for new debt: 



#### **4.1.5 Monetary Policy** 

Since the Home economy belongs to a currency union, its monetary policy adjusts interest rates so as to make sure that the nominal exchange rate is unchaged for all periods: 



In doing so, the Home country gives up monetary autonomy. Given a fixed nominal exchange rate and uncovered interest parity, Homes interest rate in equilibrium follows the Foreign rate one-to-one. Finally, the monetary authority for the currency union adjusts interest rates according to the following Taylor rule: 



35 

#### **4.1.6 Aggregation and Market Clearing** 

Total borrowers’ consumption, labor supply in the consumption and housing sectors, and housing are given by: 



The aggregate consumption is given by: 



and housing and goods market clear: 





Finally, we define the real GDP measure defined in terms of home consumption goods for our economy: 





#### **4.1.7 Equilibrium** 

In our model, the EA block can be treated as exogenous to the Home economy. The EA block is a standard New Keynesian economy with price stickiness. We dispense with a full description as the definition of equilibrium in this economy is standard.<sup>21</sup> Since there is no growth in this model, all variables are stationary. The model is solved with a second order perturbation method around the deterministic steady state. 

> 21The full set of equilibrium equations can be found in Appendix C. 

36 

### **4.2 Calibration** 

We calibrate the model to the Spanish economy. We pick parameters to reflect quarterly data and to match well both the relevant long-term moments of the Spanish economy as well as short-term dynamics of the transmission of monetary policy shocks to the Spanish and EA economies. We have 24 parameters in our model, out of which 18 are calibrated and the remaining 6 are estimated. Table 5 summarises our calibration. We set _β_<sup>_∗_</sup> = _β_ = 0 _._ 9925, implying a steady-state annual real interest rate of 3 percent both for Spain and the EA. The elasticity of substitution in intermediate goods consumption in both regions, _ε_<sup>_∗_</sup> and _ε_ , is set at 7.66 in order to get a steady-state markup of 15 percent, as in Iacoviello and Neri (2010). The EA Taylor rule parameters regarding inflation and the output gap, _γπ_ and _γy_ , are set according to Christoffel et al. (2008). For the lagged nominal interest rate parameter _γr_ we choose a slightly lower value — 0.6 instead of 0.8 — because we want to match the EA HICP and GDP reactions to monetary policy shocks with the ones estimated in the DFM. 

37 

**Table 5:** Calibrated parameters. 

|Parameter|Value|Target|
|---|---|---|
|**Euro Area**|||
|_β_<sup>_∗_</sup>|0.9925|EA Steady-state annual real interest rate of 3%|
|_ψ_<sup>_∗_</sup>|0.5|Smets and Wouters (2003)|
|_ε_<sup>_∗_</sup>|7.66|Steady-state markup of 15%|
|_γπ_|1.7|Christofel et al. (2008)|
|_γy_|0.125|Christofel et al. (2008)|
|_γr_|0.6|Christofel et al. (2008)|
|**Spain**|||
|_β_|0.9925|EA Steady-state annual real interest rate of 3%|
|_β_<sup>_′_</sup>|0.97|Iacoviello and Neri (2010)|
|_θ_<sup>_′_</sup>|0.97|Iacoviello and Neri (2010)|
|_ψ_|0.5|Burriel et al. (2010)|
|_ψ_<sup>_′_</sup>|0.5|Burriel et al. (2010)|
|_j_|0.2|Housing wealth to GDP ratio in the steady-state of 3.5|
|_δh_|0.005|7% steady-state residential investment share of GDP|
|_m_|0.7|Average loan-to-value ratio in Spain, Calza et al. (2013)|
|_ω_|0.9|Share of adjustable-rate mortgages, Albertazzi et al. (2018)|
|_ε_|7.66|Steady-state mark-up of 15%|
|_φ_|0.78|Spain average price duration of 4.6 quarters, Alvarez et al.<br>(2006)|
|_α_|0.68|Steady-state housing stock value share owned by wealthy|
|||hand-to-mouth household of 18%, Slacalek et al. (2020)|



Following Iacoviello (2005) we fix the discount of the impatient households _β_<sup>_′_</sup> at 0.97 to = = ensure that a steady-state with binding borrowing constraint is accurate. We fix _ψ_<sup>_∗_</sup> _ψ ψ_<sup>_′_</sup> to match a Frisch labor supply elasticity of 2 for the EA as in Smets and Wouters (2003), as well as for both savers and borrowers in Spain, in line with Burriel et al. (2010). Next, we pick the housing preference parameter _j_ , which essentially governs the steady-state housing wealth-to-GDP ratio, to be at 0.2. This value twice the size of the parameter used in Iacoviello (2005) and Iacoviello and Neri (2010), as the ratio of housing wealth to GDP is much higher in Spain than in the US. According to Mart´ınez-Toledano (2017), the housing wealth-to-GDP ratio for the time period we study was at approximately 3.5 in Spain. The 

38 

quarterly housing depreciation rate _δh_ is set at 0.005 which is consistent with an empirically reasonable 2 percent annual depreciation rate and with a steady-state residential investment share of GDP in Spain of approximately 7 percent. The institutional parameters on housing financing are taken from previous studies. The typical loan-to-value ratio in Spain reported in Calza et al. (2013) is 70 percent, while the average share of adjustable-rate mortgages is around 90 percent according to bank-level data reported in Albertazzi et al. (2018). The share of firms that do not reset prices each period _φ_ is set at 0.78 in order to match the average price duration of 4.6 quarters in Spain as reported in Alvarez et al. (2006). Finally, the share of borrowing constrained agents _α_ is set at 0.68 in order to match the share of housing stock in the hands of agents that face liquidity constraints to a level of 18 percent as reported in Slacalek et al. (2020). 

Since we only include one shock in the economy, the remaining 6 parameters are estimated using a limited information approach. First, we pick the model variables that are of interest in relation with the observed heterogeneity found in the empirical section. Second, we select the following variables for the small open economy: GDP, aggregate consumption, inflation and housing prices. For the EA we pick GDP, nominal interest rates and inflation. Third, we estimate these parameters by minimizing a measure of the distance between the DFM’s empirical impulse responses and the model responses. Let **Γ** _≡_ ( _ξ_<sup>_∗_</sup> _, φ_<sup>_∗_</sup> _, ξ, ξ_<sup>_′_</sup> _, δ, ν_ ) be a vector with the remaining 6 parameters, and let **Ψ(Γ** ) denote the mapping from the deep parameters **Γ** to the model impulse response functions. Further, let **Ψ**<sup>**ˆ**</sup> denote the corresponding empirical DFM estimates. We include the first 20 elements of each response function. Our estimator of **Γ** is the solution to 



where **_V_** is a weighting matrix. We choose **_V_** to be the inverse of the matrix with the sample variances of the DFM’s impulse responses on the main diagonal. Table 6 summarizes our point estimates and standard errors of the parameters in vector **Γ** . The point estimates we get are in line with the previous literature and are precisely estimated.<sup>22</sup> The point estimate for the habit formation parameter in the EA _ξ_<sup>_∗_</sup> is 0.78 which is reasonably close to the 0.69 estimated in Adolfson et al. (2007). The point estimate for the Calvo price parameter in the EA _φ_<sup>_∗_</sup> is 0.88, in line with both Smets and Wouters (2003) and Adolfson et al. (2007). The point estimates for the parameter on habit formation in consumption for savers and borrowers, _ξ_ and _ξ_<sup>_′_</sup> , are 0.84 and 0.8, respectively. These are consistent with the value of 0.847 reported in Burriel et al. (2010). The point estimate for the parameter on labor 

> 22 Standard errors were computed using the asymptotic delta function method applied to the first-order condition associated with the minimization problem. 

39 

mobility between sectors of savers _δ_ is 0.66, which surprisingly is identical to the estimate reported in Iacoviello and Neri (2010). Finally, we get a slightly lower home bias estimate 1 _− ν_ of 0.73 than the 0.81 reported in Burriel et al. (2010). In Figure 9 we show that the theoretical impulse response functions based on estimated parameters are reasonably close to their empirical counterparts. 

**Table 6:** Estimated parameters and their standard errors. 

|Parameter|Value|S.E.|
|---|---|---|
|**Euro Area**|||
|_ζ_<sup>_∗_</sup>|0.78|0.006|
|_φ_<sup>_∗_</sup>|0.88|0.005|
|**Spain**|||
|_ζ_|0.84|0.019|
|_ζ_<sup>_′_</sup>|0.8|0.006|
|_θ_|0.66|0.168|
|_ν_|0.27|0.015|



### **4.3 Quantitative Exercise: one money, many housing markets** 

In this section, we delve into an assessment of the extent to which differences in institutional characteristics of mortgage markets alone can account for the heterogeneity in monetary policy transmission in the EA. To this end, we take the model calibrated to the Spanish economy, and feed it with the loan-to-value (LTV) ratios and shares of adjustablerate mortgages (ARM) for Spain as well as the other EA countries. We then compare the dispersion of the simulated impulse response functions using the model, with the dispersion estimated using our DFM. In other words, we look at how different the transmission of monetary policy in Spain would be if this country had the LTV ratios and ARM shares of other EA member countries. A comment is in order concerning our methodology. One the one hand, the model’s impulse response functions are not directly comparable to those obtained from the DFM because, by construction, we do not calibrate the model to each individual country. On the other hand, keeping all other parameters constant allows us to isolate the effect of changing the housing financing parameters on monetary policy transmission, consistent with the goal of our exercise. 

In Table (7) we report loan-to-value ratios and the shares of Adjustable-rate mortgage in our EA sample countries. The discrepancy in these institutional characteristics is apparent. Notably, there are countries, such as Belgium and France, that combine a high LTV ratio 

40 



<!-- Start of picture text -->
EA Real GDP EONIA<br>0<br>− 0 . 2 0 . 2<br>0 . 1<br>− 0 . 4<br>0<br>− 0 . 6<br>− 0 . 1<br>0 5 10 15 20 0 5 10 15 20<br>EA HICP ESP Real GDP<br>0 . 1<br>0<br>0<br>− 0 . 5<br>− 0 . 1<br>− 1<br>0 5 10 15 20 0 5 10 15 20<br>ESP HICP ESP Real Housing Price<br>0 . 1 0<br>0<br>− 0 . 1 − 1<br>− 0 . 2<br>− 2<br>0 5 10 15 20 0 5 10 15 20<br>ESP Real Private Consumption<br>0<br>Empirical<br>− 0 . 2 Model<br>− 0 . 4<br>− 0 . 6<br>− 0 . 8<br>− 1<br>0 5 10 15 20<br>Figure 9: Model vs. empirical impulse response functions.<br><!-- End of picture text -->

with a low shares of ARM. For these reasons, we find it important to use both in the model, so to assess the impact of potentially counteracting forces. 

In Table 8 and Figures 10 - 12 we present the main results of the quantitative exercise.<sup>23</sup> 

> 23Here we include only results from changing the mortgage market parameters. In Online Appendix F.2, we show how differences in Calvo pricing parameters generate differences in monetary policy transmission. We find that differences in price stickiness generate more dispersion in GDP responses to monetary policy 

41 

**Table 7:** Institutional parameters of EA countries’ mortgage systems. 

|Country|LTV ratio|ARM share|
|---|---|---|
|BEL|0.83|0.20|
|DEU|0.7|0.15|
|IRL|0.74|1.00|
|ESP|0.7|0.90|
|FRA|0.75|0.15|
|ITA|0.5|0.70|
|LUX|0.8|0.60|
|NLD|0.9|0.10|
|AUT|0.6|0.50|
|PRT|0.85|0.98|
|FIN|0.75|0.98|



Source: Calza et al. (2013) and Albertazzi et al. (2018). 

Our main results are fourfold. First, differences in LTV ratios generate more dispersion in the responses of consumption, output, and housing prices to monetary shocks than differences in the shares of ARM. This result follows from comparing the different columns of Table 8, which show how much of the dispersion in the DFM responses at different horizons (steps) is explained by the model, when we feed the LTV ratios and shares of ARM of the countries in our sample. Both on impact and at the 8th and 20th step, the variation in LTV ratios generates a substantially higher level of dispersion in GDP, housing prices, CPI, and private consumption. This result stands in contrast to the numerical illustration by Calza et al. (2013), suggesting that LTV ratios and the share of ARM are roughly equivalent in explaining the impulse responses. In our calibrated model, differences in the observed shares of ARM generate relatively smaller differences in the macro and price responses to monetary shocks. Furthermore, under the reasonable assumption that the share of ARM correlates with the households’ net interest rate exposure, our results are also in line with the result shown in Figure 7 of Slacalek et al. (2020). These authors show that large differences in net interest rate exposure across Germany, France, Spain, and Italy, have a minimal effect on the response of consumption to monetary policy shocks in these countries. 

Second, in Figure 10 through 12, we plot the responses from the DFM against the responses from the model obtained from changing either LTV ratios, or the share of ARM, or both. A key result from comparing the figures is that the correlation is weak for LTV 

shocks than in housing prices and private consumption responses, which is at odds with our empirical findings. More importantly, the responses implied by the model with different Calvo parameters are not in line with the individual country responses estimated in the DFM. 

42 

ratios, strong for the share of ARM. In other words, while feeding the model with different LTV ratios generates a high level of dispersion in the IRFs, the majority of the simulated responses do not align with the DFM responses. By way of example, in Figure 10 bottom right corner, the model predicts that, at the 20th step, the most negative response of private consumption (PCON) is obtained by using the Netherlands LTV ratio, which is the highest in our countries sample. At the same time, however, in the estimated DFM, the PCON response in the Netherlands is average relative to other countries. This is in contrast with the results from feeding different shares of ARM: the model’s IRFs have a high correlation with those estimated in the DFM. In Figure 11, this high correlation is apparent for output and consumption. The R-square from a linear regression for output is 0.48 for the impact response and 0.5 at the 8th step.<sup>24</sup> For consumption, the R-square is 0.63 at impact and 0.79 at the 8th step. So, an important conclusion from our exercise is that, while varying the relative share of ARM does not generate sizeable heterogeneity in monetary policy transmission, it does help the model to generate IRFs that are more in line with the evidence from DFM’s. 

Third, when we use both LTV ratios and the shares of ARM from the data, the model can account for approximately one-third of the estimated dispersion of the IRFs to a monetary policy shock for GDP and private consumption. The simulated responses are remarkably in line with the DFM’s. In Figure 12, for GDP and consumption, the R-squared at the 8th step is 0.21 and 0.41, respectively. Using our institutional parameters jointly produces heterogeneity in monetary policy transmission that is both sizeable and in line with the evidence. Nonetheless, the correlation is much weaker for the other two variables<sup>25</sup> , which brings us to our final result. 

Fourth, we find that differences in LTV ratios, alone or when combined with differences in the shares of ARM, generate substantial variation in housing prices at the 8th and 20th step. Yet, the simulated variation is not in line with what we observe in the data. One possible reason for this puzzling<sup>26</sup> result is that the response of housing prices to monetary shocks are not precisely estimated by our DFM, while output and consumption are. Housing prices clearly deserve further investigation. 

> 24The R-square is computed here from a linear regression where the slope coefficient is constrained to be 1. We impose this restriction to grasp how much of the DFM responses gap relative to the mean can be explained by the model responses relative to their mean—allowing for differences on these means (hence, we do not restrict the intercept). When fitting a linear regression with a constrained slope, it is possible to get negative R-squares when the correlation between the model and the DFM responses is negative. 

> 25Varying the parameters related to housing financing does not generate sizable heterogeneity in HICP responses. The observed heterogeneity in HICP responses to monetary shocks may nonetheless be rooted in differences in other markets, such as the labor market (see Campolmi and Faia (2011)). 

> 26The puzzle stems from the fact that previous literature (see e.g. Mian et al. (2013) and Berger et al. (2018)) has shown a relevant direct link between housing prices and consumption responses. 

43 

Overall, in addition to providing novel and disaggregated empirical and quantitative evidence on the role of different institutional features of housing financing, our analysis lends support to the empirical findings of Calza et al. (2013), obtained using a different methodology. Also, they are in line with the back-of-the-envelope calculation using a HANK model in Slacalek et al. (2020), which shows how the monetary policy transmission in the EA is affected by differences in households’ balance sheets across countries. The link between our results and those in Slacalek et al. (2020) is best understood in light of the fact that, in equilibrium, different institutional parameters for mortgage markets imply differences in the compositions of households’ balance sheets. 

Our analysis has notable implications for macroprudential policy. While previous studies, such as Arena et al. (2020), have focused on uncovering the effect of macroprudential policies on housing prices, our work highlights the potential for such measures to shape the monetary transmission mechanism. Our results suggest that national macroprudential policies, reflected in the share of adjustable mortgage rates and the loan-to-value ratio, can either amplify or dampen the transmission of ECB policy to a particular country. They provide quantitative insight on how a high degree of harmonisation of macroprudential regulation across countries can result in a more homogeneous transmission of monetary policy across the block. 

**Table 8:** Coefficient of variation of the cross-country responses to a 25bp monetary policy shock — estimated DFM vs. model. 

|Variable|Coe<br>|fcient<br>|of Vari<br>|ation (CoV)<br>|Co<br>|VModel/C<br>|oVDFM (%)<br>|
|---|---|---|---|---|---|---|---|
||DFM|LTV|ARM|LTV + ARM|LTV|ARM|LTV + ARM|
|**On Impact**||||||||
|GDP|0.95|0.53|0.17|1.18|55.97|17.36|123.43|
|Housing Prices|2.39|0.01|0.02|0.04|0.42|0.85|1.73|
|HICP|1.39|0.28|0.00|0.27|19.89|0.07|19.55|
|PCON|1.04|0.34|0.02|0.34|32.60|2.16|33.15|
|**At the 8th Step**||||||||
|GDP|0.56|0.18|0.02|0.20|32.26|4.26|35.47|
|Housing Prices|1.39|0.30|0.02|0.24|21.52|1.26|16.98|
|HICP|1.44|0.12|0.12|0.17|8.58|8.40|11.93|
|PCON|0.76|0.30|0.08|0.26|39.33|11.15|34.44|
|**At the 20th Step**||||||||
|GDP|0.51|0.19|0.02|0.17|36.72|4.66|33.37|
|Housing Prices|1.47|0.38|0.17|0.30|25.95|11.48|20.65|
|HICP|1.16|0.09|0.05|0.08|7.57|4.73|6.90|
|PCON|0.75|0.19|0.14|0.20|24.84|18.57|27.12|



44 



<!-- Start of picture text -->
forour scatter<br>NLD -0.15 NLD -0.2 -0.07 DEU FRABELNLDITA -0.6 line,<br>depict<br>PRT NLD AUTAUT<br>BEL -0.3 LUX -0.7<br>BEL PRT -0.2 LUX -0.4 PRT -0.08 DEU ITA FIN ESPESP PRT IRL 45 degree line -0.8 degree45 figure and at the 20th step<br>FRA FINLUX IRL -0.25 DEU FRAFINFIN PRT ESPESP IRLIRL -0.5 NLD FRA BELBELLUX DEUAUT -0.09 LUXFRA FIN IRL -0.9 the ofthe<br>FRABELAUTAUTNLDESPESPPRTDEUDEUITA FINLUX IRL -0.3 AUTAUT ITALUX -0.6 FINFIN ITAITA IRLIRL PRT FRA LUX ESPESPDEUAUT -0.1 BEL PRT -1 Model IRFs: LTV ratios with Therows at the 8th step,<br>ITA -0.7 -1.1<br>together<br>GDP 20th step, RMSE = 0.39, R-squared = 0.11 BEL DEU FRAITA HICP 20th step, RMSE = 0.099, R-squared = 0.39 PCON 20th step, RMSE = 0.65, R-squared = 0.11 NLD<br>NLD -0.8<br>-0.2 NLD-0.4 -0.6 -0.8 -1 -1.2 -0.35 Housing Prices 20th step, RMSE = 0.54, R-squared = -0.3 1 0.5 0 -0.5 -1 0.1 0.05 0 -0.05 -0.1 -0.11 0 -0.5 -1 -1.2 y-axis, (PCON).<br>NLD -0.2 -0.12 ITA -0.4<br>-0.15 NLD AUTDEU FRABELNLD the<br>-0.4 ITA FRA BEL DEU -0.14 AUTDEULUX ITA FIN ESPESP PRTIRL -0.6 on<br>IRL<br>PRT AUT FRA FIN<br>-0.2 LUX AUT DFM consumption<br>PRT BEL -0.6 ITA -0.16 LUX<br>BEL LUX ESP DEU BEL -0.8 the<br>FIN IRL PRT<br>GDP 8th step, RMSE = 0.41, R-squared = 0.15 FRA BELESPESPAUTAUTNLDPRTITAITADEUDEU FINFIN LUXLUX IRLIRL -0.25-0.3 AUTAUT BEL DEUDEUFRAFRAITAITALUXFINFIN NLDPRT ESPESP IRLIRL -0.8-1 HICP 8th step, RMSE = 0.22, R-squared = -0.16 NLD FIN IRL PRT FRA BELLUX -0.18-0.2 PCON 8th step, RMSE = 0.53, R-squared = 0.089 NLD PRT -1 Model IRFs: LTV ratios fromresponses HICP,andprivate<br>-0.5 -1 -1.5 Housing Prices 8th step, RMSE = 0.71, R-squared = -0.23 1 0.5 0 -0.5 -1 -1.2 0.2 0.1 0 -0.1 -0.2 -0.22 0 -0.5 -1 -1.2<br>NLD ITA<br>0.02 -0.6 AUT -0.08 ITA -0.04 prices,<br>AUT<br>0 -0.61 NLD LUXIRLIRL FINFINBELPRT FRAFRAITA ESPESPDEUDEUAUT -0.1 AUT DEUDEUNLDFRAFRA ITAFINFINLUXBEL ESPIRLESPIRL PRT -0.06 estimated<br>BELFRA DEU NLD LUX the housing<br>NLD -0.62 LUX -0.12 BEL -0.08<br>and<br>PRT -0.02 BEL PRT<br>AUT<br>GDP,<br>BEL LUX -0.63 PRT -0.14 -0.1<br>DEUFRANLDBEL LUX -0.04 ITAITA PRT x-axis —<br>AUT AUT BEL<br>DEUESPFRAESPAUTFINFINITAITAPRT LUX IRLIRL -0.06 IRLIRL FRA FINFIN LUXDEU PRT ESP -0.64 -0.16 NLD -0.12 Model IRFs: LTV ratios theon interest<br>-0.65 -0.18 -0.14<br>GDP impact, RMSE = 0.067, R-squared = 0.12 HICP impact, RMSE = 0.19, R-squared = -0.71 PCON impact, RMSE = 0.05, R-squared = 0.2 of hits.<br>NLD<br>0 -0.08 Housing Prices impact, RMSE = 0.76, R-squared = -0.3 0 -0.66 0 -0.2 0 -0.16 Impulse response functions of analytical model featuring different LTV ratios, compared to DFM. We plot the analytical<br>-0.1 -0.2 -0.3 0.5 -0.5 0.2 0.1 -0.1 -0.2 -0.1<br>-0.05 -0.15 shock<br>10: responses<br>variables the<br>Figure model’s main plots for different variables while the columns present them by the response steps — on impact, after<br>DFM IRFs DFM IRFs DFM IRFs<br>DFM IRFs<br><!-- End of picture text -->

45 

|5<br>-0.3<br>-0.295<br>-0.29<br>-0.285<br>**GDP 20th step, RMSE = 0.37, R-squared = -0.56**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.8<br>-0.7<br>-0.6<br>-0.5<br>**ng Prices 20th step, RMSE = 0.61, R-squared = -0.45**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>5<br>-0.1<br>-0.095<br>-0.09<br>**HICP 20th step, RMSE = 0.1, R-squared = -0.14**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br><br>-0.8<br>-0.75<br>-0.7<br>-0.65<br>-0.6<br>-0.55<br>Model IRFs: ARM shares<br>**PCON 20th step, RMSE = 0.45, R-squared = 0.8**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>45 degree line<br> ARM, compared to DFM. We plot the<br>e y-axis, together with the 45 degree line,<br>n (PCON). The rows of the fgure depict<br>— on impact, at the 8th step, and at the|
|---|
|-0.065<br>-0.06<br>-0.055<br>-0.05<br>-0.045<br>-0.04<br>-0.3<br>-0.2<br>-0.1<br>0<br>DFM IRFs<br>**GDP impact, RMSE = 0.061, R-squared = 0.46**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.295<br>-0.29<br>-0.285<br>-0.28<br>-0.275<br>-0.27<br>-1.5<br>-1<br>-0.5<br>**GDP 8th step, RMSE = 0.4, R-squared = 0.5**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.30<br>-1.2<br>-1<br>-0.8<br>-0.6<br>-0.4<br> <br>-0.65<br>-0.64<br>-0.63<br>-0.62<br>-0.61<br>-0.6<br>-0.5<br>0<br>0.5<br>DFM IRFs<br>**Housing Prices impact, RMSE = 0.75, R-squared = 0.11**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.96<br>-0.95<br>-0.94<br>-0.93<br>-0.92<br>-0.91<br>-1<br>-0.5<br>0<br>0.5<br>1<br>**Housing Prices 8th step, RMSE = 0.75, R-squared = -0.49**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.9<br>-1<br>-0.5<br>0<br>0.5<br>1<br>**Housi**<br>-0.1004 -0.10035 -0.1003 -0.10025 -0.1002 -0.10015<br>-0.1<br>0<br>0.1<br>0.2<br>DFM IRFs<br>**HICP impact, RMSE = 0.16, R-squared = -0.018**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.19<br>-0.18<br>-0.17<br>-0.16<br>-0.15<br>-0.14<br>-0.13<br>-0.1<br>0<br>0.1<br>0.2<br>**HICP 8th step, RMSE = 0.19, R-squared = -0.3**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.10<br>-0.1<br>-0.05<br>0<br>0.05<br>0.1<br> <br>-0.063<br>-0.062<br>-0.061<br>-0.06<br>-0.059<br>-0.058<br>Model IRFs: ARM shares<br>-0.15<br>-0.1<br>-0.05<br>0<br>DFM IRFs<br>**PCON impact, RMSE = 0.041, R-squared = -0.63**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.6<br>-0.58<br>-0.56<br>-0.54<br>-0.52<br>-0.5<br>Model IRFs: ARM shares<br>-0.6<br>-0.4<br>-0.2<br>0<br>**PCON 8th step, RMSE = 0.34, R-squared = 0.79**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.85<br>-0.8<br>-0.6<br>-0.4<br>-0.2<br>0<br> <br>**Figure 11:** Impulse response functions of analytical model featuring diferent shares of<br>analytical model’s responses on the x-axis and the estimated responses from the DFM on th<br>for our main variables of interest — GDP, housing prices, HICP, and private consumptio<br>scatter plots for diferent variables while the columns present them by the response steps <br>20th step after the shock hits.|



46 

|-0.3<br>-0.25<br>-0.2<br>-0.15<br>**GDP 20th step, RMSE = 0.38, R-squared = 0.015**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.8<br>-0.6<br>-0.4<br>-0.2<br>**ng Prices 20th step, RMSE = 0.62, R-squared = -0.55**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>5<br>-0.1<br>-0.095<br>-0.09<br>-0.085<br>-0.08<br>**HICP 20th step, RMSE = 0.1, R-squared = 0.059**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-1.1<br>-1<br>-0.9<br>-0.8<br>-0.7<br>-0.6<br>Model IRF: LTV ratios and ARM shares<br>**CON 20th step, RMSE = 0.52, R-squared = 0.68**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>45 degree line<br> and shares of ARM, compared to DFM.<br>he DFM on the y-axis, together with the<br>te consumption (PCON). The rows of the<br>ponse steps — on impact, at the 8th step,|
|---|
|-0.1<br>-0.05<br>0<br>0.05<br>0.1<br>-0.3<br>-0.2<br>-0.1<br>0<br>0.1<br>DFM IRFs<br>**GDP impact, RMSE = 0.073, R-squared = 0.23**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.35<br>-0.3<br>-0.25<br>-0.2<br>-0.15<br>-0.1<br>-1.5<br>-1<br>-0.5<br>**GDP 8th step, RMSE = 0.41, R-squared = 0.21**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.35<br>-1.2<br>-1<br>-0.8<br>-0.6<br>-0.4<br>-0.2<br> <br>-0.65<br>-0.6<br>-0.55<br>-0.5<br>0<br>0.5<br>DFM IRFs<br>**Housing Prices impact, RMSE = 0.75, R-squared = -0.14**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-1.2<br>-1<br>-0.8<br>-0.6<br>-0.4<br>-1<br>-0.5<br>0<br>0.5<br>1<br>**Housing Prices 8th step, RMSE = 0.72, R-squared = -0.31**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-1<br>-1<br>-0.5<br>0<br>0.5<br>1<br>**Housi**<br>-0.2<br>-0.18<br>-0.16<br>-0.14<br>-0.12<br>-0.1<br>-0.08<br>-0.2<br>-0.1<br>0<br>0.1<br>0.2<br>DFM IRFs<br>**HICP impact, RMSE = 0.19, R-squared = -0.71**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.24<br>-0.22<br>-0.2<br>-0.18<br>-0.16<br>-0.14<br>-0.12<br>-0.2<br>-0.1<br>0<br>0.1<br>0.2<br>**HICP 8th step, RMSE = 0.2, R-squared = -0.23**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-0.10<br>-0.1<br>-0.05<br>0<br>0.05<br>0.1<br> <br>-0.16<br>-0.14<br>-0.12<br>-0.1<br>-0.08<br>-0.06<br>-0.04<br>Model IRF: LTV ratios and ARM shares<br>-0.15<br>-0.1<br>-0.05<br>0<br>DFM IRFs<br>**PCON impact, RMSE = 0.052, R-squared = 0.15**<br>BEL<br>DEU<br>IRLESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-1<br>-0.9<br>-0.8<br>-0.7<br>-0.6<br>-0.5<br>-0.4<br>Model IRF: LTV ratios and ARM shares<br>-1<br>-0.5<br>0<br>**PCON 8th step, RMSE = 0.44, R-squared = 0.41**<br>BEL<br>DEU<br>IRL<br>ESP<br>FRA<br>ITA<br>LUX<br>NLD<br>AUT<br>PRT<br>FIN<br>-1.2<br>-1<br>-0.5<br>0<br>**P**<br>**Figure 12:** Impulse response functions of analytical model featuring diferent LTV ratios<br>We plot the analytical model’s responses on the x-axis and the estimated responses from t<br>45 degree line, for our main variables of interest — GDP, housing prices, HICP, and priva<br>fgure depict scatter plots for diferent variables while the columns present them by the res<br>and at the 20th step after the shock hits.|



47 

## **5 Conclusion** 

Using a dynamic factor model with high-frequency identification, this paper investigates the heterogeneous effects of monetary policy across the euro area. We contribute to the literature a measure of the degree of heterogeneity in the effects of monetary policy. Focusing on housing financing as a case study, we provide quantitative evidence and insight into institutional determinants of country-specific transmission mechanisms. 

In our findings, across all variables of interest, the average dispersion of country-specific responses to a monetary shock is twice the size of the mean response. There are, however, significant differences across variables. Country-level financial variables and output react fairly similarly across borders: the dispersion in their responses is low—20 to 50 percent of the average response at EA level. On the contrary, variables naturally related to markets that have experienced little convergence, such as housing and labour markets, react in significantly asymmetric ways. This is novel evidence lending empirical support to the idea that the degree of heterogeneity is inversely related to the degree of cross-border institutional convergence. 

We elaborate on this point with a case study of European housing markets. We build a model of a small open economy featuring housing, operating in a monetary union. We use this model to quantitatively assess how much of the variation in individual countrylevel responses to a EA monetary policy shock can be explained by differences in housing financing. We find that differences in mortgage market characteristics across the EA explain one-third of the cross-country heterogeneity of responses in output and private consumption. 

Other features of the housing market can be expected to weigh on the transmission of monetary policy. By way of example, prima facie evidence points to a specific role of the share of home ownership.<sup>27</sup> In addition, our methodology could be extended to the analysis of institutional divergences in other markets, such as national labor markets. These are promising and intriguing areas that we leave to future research. 

> 27See the working paper version of this text, Corsetti et al. (2018) 

48 

## **References** 

- Adolfson, M., S. Las´een, J. Lind´e, and M. Villani (2007). Bayesian estimation of an open economy dsge model with incomplete pass-through. _Journal of International Economics 72_ (2), 481–511. 

- Albertazzi, U., S. Ongena, and F. Fringuellotti (2018). Fixed rate versus adjustable rate mortgages: evidence from euro area banks. Temi di discussione (Economic working papers) 1176, Bank of Italy, Economic Research and International Relations Area. 

- Altavilla, C., L. Brugnolini, R. S. G¨urkaynak, R. Motto, and G. Ragusa (2019). Measuring euro area monetary policy. _Journal of Monetary Economics 108_ , 162–179. 

- Alvarez, L. J., E. Dhyne, M. Hoeberichts, C. Kwapil, H. Le Bihan, P. L¨unnemann, F. Martins, R. Sabbatini, H. Stahl, P. Vermeulen, et al. (2006). Sticky prices in the euro area: a summary of new micro-evidence. _Journal of the European Economic association 4_ (2-3), 575–584. 

- Andrews, D., A. Caldera, and A. Johansson (2011). Housing markets and structural policies in OECD countries. OECD Economics Department Working Papers 836, OECD Publishing. 

- Angeloni, I., A. Kashyap, and B. Mojon (Eds.) (2003). _Monetary Policy Transmission in the Euro Area: A Study by the Eurosystem Monetary Transmission Network_ . Cambridge University Press. 

- Arena, M., T. Chen, S. M. Choi, N. Geng, C. A. Gueye, T. Lybek, E. Papageorgiou, and Y. S. Zhang (2020). Macroprudential policies and house prices in europe. Departmental Paper 20/03, International Monetary Fund. 

- Bagliano, F. C. and C. A. Favero (1999). Information from financial markets and VAR measures of monetary policy. _European Economic Review 43_ (4), 825 – 837. 

- Bai, J. and S. Ng (2002). Determining the number of factors in approximate factor models. _Econometrica 70_ (1), 191–221. 

- Barakchian, S. M. and C. Crowe (2013). Monetary policy matters: Evidence from new shocks data. _Journal of Monetary Economics 60_ (8), 950 – 966. 

- Barigozzi, M., A. M. Conti, and M. Luciani (2014). Do euro area countries respond asymmetrically to the common monetary policy? _Oxford Bulletin of Economics and Statistics 76_ (5), 693–714. 

- Beraja, M., A. Fuster, E. Hurst, and J. Vavra (2019). Regional heterogeneity and the refinancing channel of monetary policy. _The Quarterly Journal of Economics 134_ (1), 109–183. 

- Berger, D., V. Guerrieri, G. Lorenzoni, and J. Vavra (2018). House prices and consumer spending. _The Review of Economic Studies 85_ (3), 1502–1542. 

49 

- Bernanke, B. S., J. Boivin, and P. Eliasz (2005). Measuring the effects of monetary policy: A factor-augmented vector autoregressive (FAVAR) approach. _The Quarterly Journal of Economics 120_ (1), 387–422. 

- Boivin, J. and M. Giannoni (2007). DSGE Models in a Data-Rich Environment. Working Paper Series 162, Banque de France. 

- Burriel, P., J. Fernndez-Villaverde, and J. F. Rubio-Ramrez (2010, March). MEDEA: a DSGE model for the Spanish economy. _SERIEs 1_ (1-2), 175–243. 

- Calza, A., T. Monacelli, and L. Stracca (2013). Housing Finance And Monetary Policy. _Journal of the European Economic Association 11_ , 101–122. 

- Campbell, J. R., C. L. Evans, J. D. Fisher, and A. Justiniano (2012). Macroeconomic effects of federal reserve forward guidance. _Brookings Papers on Economic Activity 2012_ (1), 1–80. 

- Campbell, J. R. and Z. Hercowitz (2005). The role of collateralized household debt in macroeconomic stabilization. Technical report, National Bureau of Economic Research. 

- Campolmi, A. and E. Faia (2011). Labor market institutions and inflation volatility in the euro area. _Journal of Economic Dynamics and Control 35_ (5), 793–812. 

- Christoffel, K. P., G. Coenen, and A. Warne (2008). The new area-wide model of the euro area: a micro-founded open-economy model for forecasting and policy analysis. 

- Ciccarelli, M., A. Maddaloni, and J.-L. Peydr´o (2013). Heterogeneous transmission mechanism: monetary policy and financial fragility in the eurozone. _Economic Policy 28_ (75), 459–512. 

- Cloyne, J., C. Ferreira, and P. Surico (2019, 01). Monetary Policy when Households have Debt: New Evidence on the Transmission Mechanism. _The Review of Economic Studies 87_ (1), 102–129. 

- Cochrane, J. H. and M. Piazzesi (2002). The Fed and interest rates - a high-frequency identification. _American Economic Review 92_ (2), 90–95. 

- Corsetti, G., J. B. Duarte, and S. Mann (2018). One money, many markets: a factor model approach to monetary policy in the euro area with high-frequency identification. Discussion Paper Series CFM-DP2018-05, CFM. 

- De Paoli, B. (2009). Monetary policy and welfare in a small open economy. _Journal of international Economics 77_ (1), 11–22. 

- Dias, D. A. and J. B. Duarte (2019). Monetary policy, housing rents, and inflation dynamics. _Journal of Applied Econometrics 34_ (5), 673–687. 

- ECB (2017). Financial integration in Europe. _Annual Report_ . 

50 

- Faust, J., E. T. Swanson, and J. H. Wright (2004). Identifying vars based on high frequency futures data. _Journal of Monetary Economics 51_ (6), 1107 – 1131. 

- Forni, M. and L. Gambetti (2010). The dynamic effects of monetary policy: A structural factor model approach. _Journal of Monetary Economics 57_ (2), 203 – 216. 

- Gertler, M. and P. Karadi (2015). Monetary policy surprises, credit costs, and economic activity. _American Economic Journal: Macroeconomics 7_ (1), 44–76. 

- Giannone, D., L. Reichlin, and L. Sala (2005). Monetary policy in real time. In _NBER Macroeconomics Annual 2004_ , Volume 19, pp. 161–224. MIT Press. 

- Greenwald, D. (2018). The mortgage credit channel of macroeconomic transmission. MIT Sloan Research Paper 5184-16. 

- Gurkaynak, R. S., B. Sack, and E. T. Swanson (2005). Do actions speak louder than words? the response of asset prices to monetary policy actions and statements. _International Journal of Central Banking 1_ (1), 55–93. 

- Hamilton, J. D. (2008). Daily monetary policy shocks and new home sales. _Journal of Monetary Economics 55_ (7), 1171 – 1190. 

- Hanson, S. G. and J. C. Stein (2015). Monetary policy and long-term real rates. _Journal of Financial Economics 115_ (3), 429 – 448. 

- Iacoviello, M. (2005). House Prices, Borrowing Constraints, and Monetary Policy in the Business Cycle. _American Economic Review 95_ (3), 739–764. 

- Iacoviello, M. and S. Neri (2010). Housing market spillovers: evidence from an estimated dsge model. _American Economic Journal: Macroeconomics 2_ (2), 125–64. 

- Jarocinski, M. and P. Karadi (2018). Deconstructing monetary policy surprises: the role of information shocks. _ECB Working Paper Series_ (2133). 

- Kuttner, K. N. (2001). Monetary policy surprises and interest rates: Evidence from the Fed funds futures market. _Journal of Monetary Economics 47_ (3), 523 – 544. 

- Liu, Z., P. Wang, and T. A. Zha (2010). Do credit constraints amplify macroeconomic fluctuations? Working Paper 2010-1, FRB Atlanta. 

- Lloyd, S. (2017a). Estimating nominal interest rate expectations: Overnight indexed swaps and the term structure. Cambridge working papers in economics, University of Cambridge. 

- Lloyd, S. (2017b). Overnight indexed swap market-based measures of monetary policy expectations. Cambridge working papers in economics, University of Cambridge. 

51 

- Mart´ınez-Toledano, C. (2017). Housing bubbles, offshore assets and wealth inequality in spain. Working Papers Series 2017/19, WDI. 

- Mertens, K. and M. O. Ravn (2013). The dynamic effects of personal and corporate income tax changes in the United States. _American Economic Review 103_ (4), 1212–47. 

- Mian, A., K. Rao, and A. Sufi (2013). Household Balance Sheets, Consumption, and the Economic Slump. _Quarterly Journal of Economics 128_ (4). 

- Nakamura, E. and J. Steinsson (2018). High-frequency identification of monetary non-neutrality: the information effect. _The Quarterly Journal of Economics 133_ (3), 1283–1330. 

- Olea, Jos´e L. Montiel, S. J. and M. W. Watson (2012). Inference in Structural VARs with External Instruments. Working paper. 

- Onatski, A. (2009). Testing hypotheses about the number of factors in large factor models. _Econometrica 77_ (5), 1447–1479. 

- Onatski, A. (2010). Determining the number of factors from empirical distribution of eigenvalues. _The Review of Economics and Statistics 92_ (4), 1004–1016. 

- Osborne, J. (2005). Housing in the euro area - twelve markets one money. Quarterly Bulletin 4, Central Bank of Ireland. 

- Owen, A. B., J. Wang, et al. (2016). Bi-cross-validation for factor analysis. _Statistical Science 31_ (1), 119–139. 

- Romer, C. D. and D. H. Romer (2002). A rehabilitation of monetary policy in the 1950’s. _American Economic Review 92_ (2), 121–127. 

- Rubio, M. (2011). Fixed-and variable-rate mortgages, business cycles, and monetary policy. _Journal of Money, Credit and Banking 43_ (4), 657–688. 

- Sargent, T. and C. Sims (1977). Pretending to have too much a priori economic theory. In _New Methods in Business Cycle Research: Proceedings From a Conference_ , pp. 45–109. Federal Reserve Bank of Minneapolis. 

- Sargent, T. J. (1989). Two models of measurements and the investment accelerator. _Journal of Political Economy 97_ (2), 251–287. 

- Slacalek, J., O. Tristani, and G. L. Violante (2020). Household balance sheet channels of monetary policy: A back of the envelope calculation for the euro area. Working Paper 26630, National Bureau of Economic Research. 

52 

- Smets, F. and R. Wouters (2003). An estimated dynamic stochastic general equilibrium model of the euro area. _Journal of the European Economic Association 1_ (5), 1123–1175. 

- Stock, J. H. and M. W. Watson (2012). Disentangling the channels of the 2007-2009 recession. _Brookings Papers on Economic Activity_ (18094), 81–135. 

- Stock, J. H. and M. W. Watson (2016). Dynamic factor models, factor-augmented vector autoregressions, and structural vector autoregressions in macroeconomics. Volume 2 of _Handbook of Macroeconomics_ , pp. 415 – 525. Elsevier. 

- Sutherland, A. (2005). Incomplete pass-through and the welfare effects of exchange rate variability. _Journal of international economics 65_ (2), 375–399. 

- Westig, D. and L. Bertalot (2016). Hypostat 2016: A review of Europe’s housing and mortgage markets. Report, European Mortgage Federation. 

- Wong, A. (2019). Refinancing and the transmission of monetary policy to consumption. _American Economic Review_ . 

53 

## **Appendix** 

## **A Data Set** 

Table 9 contains a complete list of the series in our data set as well as detailed descriptions and information regarding transformations, geographical coverage and sources. Abbreviations and codes are laid out in the following: 

Transformation code (T) 

- 1 - no transformation 

- 2 - in levels 

- 4 - logs 

- 5 - difference in logs 

Geography 

EA - Euro area 

EA12 - Euro area (12 countries) EA19 - Euro area (19 countries) 

EACC - Euro area (changing composition) 

EA11 ~~i~~ - 11 individual series for sample countries 

Factor analysis (F) 

- Y - included in data set for principal component analysis 

Seasonal adjustment 

WDSA - working day and seasonally adjusted 

SA - seasonally adjusted 

NA - neither working day nor seasonally adjusted 

Note: National house price indices have different start dates across countries. They begin in 2005 Q4 for Spain, 2006 Q2 for France, 2007 Q1 for Luxembourg, 2008 Q1 for Portugal, 2010 Q1 for Italy and Austria, and 2005 Q1 for all other countries. Furthermore, unemployment data for France between 2000 Q1 and 2005 Q1, as well as Luxembourg between 2000 Q1 and 2003 Q1 is only available annually and has been linearly interpolated to create a quarterly data series. Thereafter all unemployment data is quarterly. Finally, import and export data for Germany, Spain and Italy is only available from 2012 Q1 onward. 

54 

|End<br>F<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4|
|---|
|y<br>Start<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1|
|Geograph<br>EA12<br>EA12<br>EA12<br>EA12<br>EA12<br>EA12<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA12<br>EA12<br>EA12<br>EA12<br>EA12<br>EA12<br>EA19<br>EACC<br>EACC<br>EACC<br>EACC<br>EACC<br>EACC<br>EACC<br>EACC<br>EACC<br>EACC<br>EACC<br>EACC|
|Source<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat|
|T<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5<br>5|
|Description<br>**rsonal Income**<br>Gross Domestic Product at market prices, Chain linked volumes, 2010=100, WDSA<br>Household and NPISH fnal consumption expenditure, Chain linked volumes, 2010=100, WDSA<br>Final consumption expenditure of general government, Chain linked volumes, 2010=100, WDSA<br>Gross fxed capital formation, Chain linked volumes, 2010=100, WDSA<br>Exports of goods and services, Chain linked volumes, 2010=100, WDSA<br>Imports of goods and services, Chain linked volumes, 2010=100, WDSA<br>Gross Domestic Product at market prices, Chain linked volumes, 2010=100, WDSA<br>Final consumption expenditure, Chain linked volumes, 2010=100, WDSA<br>Household and NPISH fnal consumption expenditure, Chain linked volumes, 2010=100, WDSA<br>Final consumption expenditure of general government, Chain linked volumes, 2010=100, WDSA<br>Gross fxed capital formation, Chain linked volumes (2010), million euro, WDSA<br>Exports of goods and services, Chain linked volumes, 2010=100, unadjusted data<br>Imports of goods and services, Chain linked volumes, 2010=100, unadjusted data<br>**ators**<br>Gross domestic product at market prices, Price index (implicit defator), 2010=100, euro, WDSA<br>Household and NPISH fnal consumption expenditure, Price index (implicit defator),<br>2010=100, euro, WDSA<br>Final consumption expenditure of general government, Price index (implicit defator),<br>2010=100, euro, WDSA<br>Gross fxed capital formation, Price index (implicit defator), 2010=100, euro, WDSA<br>Exports of goods and services, Price index (implicit defator), 2010=100, euro, WDSA<br>Imports of goods and services, Price index (implicit defator), 2010=100, euro, WDSA<br>Producer prices in industry, domestic market, index 2010=100, unadjusted data<br>All-items HICP, Index, 2015=100<br>HICP Food and non-alcoholic beverages, Index, 2015=100<br>HICP Alcoholic beverages, tobacco and narcotics, Index, 2015=100<br>HICP Clothing and footwear, Index, 2015=100<br>HICP Furnishings, household equipment and routine household maintenance, Index, 2015=100<br>HICP Health, Index, 2015=100<br>HICP Transport, Index, 2015=100<br>HICP Communications, Index, 2015=100<br>HICP Recreation and culture, Index, 2015=100<br>HICP Education, Index, 2015=100<br>HICP Restaurants and hotels, Index, 2015=100<br>HICP Miscellaneous goods and services, Index, 2015=100|
|**GDP & Pe**<br>GDP<br>PCON<br>G<br>GFCF<br>EX<br>IM<br>GDP<br>i<br>CON<br>i<br>PCON<br>i<br>G<br>i<br>GFCF<br>i<br>EX<br>i<br>IM<br>i<br>**Prices/Def**<br>GDPDEF<br>PCONDEF<br>GDEF<br>GFCFDEF<br>EXDEF<br>IMDEF<br>PPI<br>HICP00<br>HICP01<br>HICP02<br>HICP03<br>HICP05<br>HICP06<br>HICP07<br>HICP08<br>HICP09<br>HICP10<br>HICP11<br>HICP12|



55 

|2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4|
|---|
|2000 Q4<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1|
|EACC<br>EACC<br>EACC<br>EACC<br>EA19<br>EA19<br>EA19<br>EA19<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>World<br>EA19<br>EACC<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19|
|5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>IMF<br>5<br>ECB SDW<br>5<br>ECB SDW<br>5<br>ECB SDW<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>1<br>Eurostat<br>5<br>Eurostat|
|Overall HICP index excluding seasonal food, Index, 2015=100<br>Overall HICP index excluding housing, water, electricity, gas and other fuels, 2015=100<br>Overall HICP index excluding education, health and social protection, Index, 2015=100<br>HICP Housing, water electricity, gas and other fuels, Index, 2015=100<br>Producer Price Index, MIG - intermediate goods, unadjusted data, 2010=100<br>Producer Price Index, MIG - capital goods, unadjusted data, 2010=100<br>Producer Price Index, non-durable consumer goods, unadjusted data, 2010=100<br>Producer Price Index, Manufacturing, unadjusted data, 2010=100<br>Individual country HICP<br>HICP Housing, water electricity, gas and other fuels, Index, 2015=100<br>Producer prices in industry (except construction sewerage, waste management and<br>remediation activities), Domestic output price index in national currency, 2010=100<br>Final consumption expenditure, Price index (implicit defator), 2010=100, euro, WDSA<br>Household and NPISH fnal consumption expenditure, Price index (implicit defator),<br>2010=100, euro, WDSA<br>Gross fxed capital formation, Price index (implicit defator), 2010=100, euro, WDSA<br>IMF World Commodity Price Index, USD denominated, weights based on<br>2002-2004 average world export earnings, non-fuel primary commodities and energy, 2005=100<br>ECB Commodity Price Index, Euro denominated, use-weighted, Total non-energy commodity,<br>unadjusted data, 2010=100<br>Brent crude oil 1-month forward, fob (free on board) per barrel, Euro<br>**Production**<br>Industrial Production Index, Total Industry, WDSA, 2005=100<br>Industrial Production Index, MIG - intermediated goods, WDSA, 2010=100<br>Industrial Production Index, MIG - energy, WDSA, 2010=100<br>Industrial Production Index, MIG - capital goods, WDSA, 2010=100<br>Industrial Production Index, MIG - consumer goods, WDSA, 2010=100<br>Industrial Production Index, MIG - durable consumer goods, WDSA, 2010=100<br>Industrial Production Index, MIG - non-durable consumer goods, WDSA, 2010=100<br>Industrial Production Index, Mining and quarrying, WDSA, 2010=100<br>Industrial Production Index, Manufacturing, WDSA, 2010=100<br>Industrial Turnover Index, MIG Intermediate Goods (2010=100, WDSA)<br>Industrial Turnover Index, MIG Energy (2010=100, WDSA)<br>Industrial Turnover Index, MIG Capital Goods (2010=100, WDSA)<br>Industrial Turnover Index, MIG Consumer Goods (2010=100, WDSA)<br>Industrial Turnover Index, MIG Durable Consumer Goods (2010=100, WDSA)<br>Industrial Turnover Index, MIG Non-Durable Consumer Goods (2010=100, WDSA)<br>Current level of capacity utilization, percent<br>Industrial Turnover Index, Manufacturing, 2010=100, SWDA|
|HICPXFD<br>HICPXUTIL<br>HICPXHTH<br>HICPUTIL<br>PPIING<br>PPICAG<br>PPINDCOG<br>PPIM<br>HICP<br>i<br>UTIL<br>i<br>PPI<br>i<br>CDEF<br>i<br>PCONDEF<br>i<br>GFCFDEF<br>i<br>CPIIMF<br>CPIECB<br>OIL<br>**Industrial **<br>IPIT<br>IPIING<br>IPINRG<br>IPICAG<br>IPICOG<br>IPIDCOG<br>IPINDCOG<br>IPIMQ<br>IPIM<br>ITIING<br>ITINRG<br>ITICAG<br>ITICOG<br>ITIDCOG<br>ITINDCOG<br>CAPUTIL<br>ITIM|



56 

|2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4|
|---|
|2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br><br>2000 Q1<br>2000 Q1<br><br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br><br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2003 Q1<br>2003 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2004 Q4<br>2004 Q4<br>2004 Q4<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2004 Q4|
|EA12<br>EACC<br>EA19<br>EA11<br>i<br>EA19<br>EA19<br>EACC<br>11 ex BEL<br>EACC<br>11 ex BEL<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA11<br>i<br>11 ex BEL<br>EA<br>EACC<br>EACC<br>EACC<br>EACC<br>EA<br>EA<br>EA<br>EA<br>EA<br>EA<br>EA<br>EA<br>EA<br>EA|
|Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>Eurostat<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>Eurostat<br>Eurostat<br>Bloomberg<br>Eurostat<br>Eurostat<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW<br>ECB SDW|
|**and Unemployment**<br>Compensation of employees, Current prices, million euro, WDSA<br>5<br>Total Unemployment rate (quarterly average), WDSA<br>2<br>Total employment<br>5<br>Unemployment rate, total from age 15 to 74, percentage<br>2<br>Labour Input in Construction, Index of Hours Worked, 2010=100, WDSA<br>5<br>**rts**<br>Building Permits, Residential Buildings, Index, 2010=100, WDSA<br>5<br>Gross fxed capital formation: Total construction (gross), chain linked volumes, Index, 2010=100<br>5<br>Gross fxed capital formation: Total construction (gross), chain linked volumes, Index, 2010=100<br>5<br>Gross fxed capital formation: Dwellings (gross), chain linked volumes, Index, 2010=100<br>5<br>Gross fxed capital formation: Dwellings (gross), chain linked volumes, Index, 2010=100<br>5<br>Production in Construction, Volume Index, 2010=100, WDSA<br>5<br>**Orders and Sales**<br>Industrial New Orders, MIG Intermediate Goods, 2010=100, SA<br>5<br>Industrial New Orders, MIG Capital Goods, 2010=100, SA<br>5<br>Industrial New Orders, MIG Consumer Goods, 2010=100, SA<br>5<br>Industrial New Orders, Manufacturing, 2010=100, SA<br>5<br>**d Productivity**<br>Real labour productivity per hour worked, 2010=100, unadjusted data<br>5<br>Nominal unit labour cost based on hours worked, 2010=100, unadjusted data<br>5<br>**Credit**<br>1 year EONIA swap<br>1<br>3-month money market interest rate<br>1<br>EMU convergence criterion long-term bond yields<br>1<br>Bank interest rates - loans to households for house purchase (outstanding amount<br>business coverage), average of observations through period, percent per annum<br>1<br>Cost of borrowing for households for house purchase (new business coverage),<br>average of observations through period, percent per annum<br>1<br>3-Month Euro Interbank Ofered Rate (%, NSA)<br>1<br>6-Month Euro Interbank Ofered Rate (%, NSA)<br>1<br>1-Year Euro Interbank Ofered Rate (%, NSA)<br>1<br>3-Year Euro Area Government Benchmark Bond Yield (%, NSA)<br>1<br>5-Year Euro Area Government Benchmark Bond Yield (%, NSA)<br>1<br>10-Year Euro Area Government Benchmark Bond Yield (%, NSA)<br>1<br>Euro Overnight Index Average (%, NSA)<br>1<br>ECB Ofcial Refnancing Operation Rate (efective, %, NSA)<br>1<br>Spread EURIBOR3MD - REFI<br>1<br>Spread YLD<br>10Y - REFI<br>1|
|**Employment**<br>WIN<br>U<br>EMP<br>U<br>i<br>LABCON<br>**Housing Sta**<br>BUILD<br>GFCFC<br>GFCFC<br>i<br>GFCFD<br>GFCFD<br>i<br>PROCO<br>**Inventories, **<br>ORDING<br>ORDCAG<br>ORDCOG<br>ORDM<br>**Earnings an**<br>PRD<br>i<br>ULC<br>i<br>**Money and **<br>EUSWE1<br>STINT<br>LTINT<br>MIR<br>COB<br>EURIBOR3MD<br>EURIBOR6MD<br>EURIBOR1YD<br>YLD<br>3Y<br>YLD<br>5Y<br>YLD<br>10Y<br>EONIA<br>REFI<br>S3MDREFI<br>S10YYLDREFI|



57 

|2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>Y<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>2016 Q4<br>Y<br>2016 Q4|
|---|
|2000 Q1<br>2000 Q1<br>2003 Q1<br>2003 Q1<br>2000 Q1<br>2000 Q1<br>2003 Q1<br>2000 Q1<br>2005 Q1<br>2005 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2005 Q1<br>2005 Q1<br><br>2005 Q1<br>2005 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1<br>2000 Q1|
|EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA19<br>EA11<br>i<br>EA11<br>i<br>EACC<br>EACC<br>EACC<br>EACC<br>EA19<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>EA11<br>i<br>11 ex NLD<br>EA11<br>i<br>EA19<br>EA<br>EA<br>EA<br>EA<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19<br>EA19|
|1<br>OECD<br>1<br>OECD<br>1<br>ECB SDW<br>1<br>ECB SDW<br>5<br>OECD<br>5<br>OECD<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Author’s<br>calculation<br>5<br>Eurostat<br>5<br>Author’s<br>calculation<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>5<br>Eurostat<br>2<br>Eurostat<br>2<br>Eurostat<br>2<br>Eurostat<br>2<br>Eurostat<br>2<br>Eurostat<br>2<br>Eurostat<br>2<br>Eurostat|
|Long-term interest rates, percent per annum<br>Short-term interest rates, percent per annum<br>Bank interest rates - loans to households for house purchase (outstanding amount<br>business coverage), average of observations through period, percent per annum<br>Cost of borrowing for households for house purchase (new business coverage),<br>average of observations through period, percent per annum<br>**ces, Wealth, Household Balance Sheets**<br>Share prices, Index, 2010=100<br>Share prices, Index, 2010=100<br>Distribution of population by tenure status: ownership, percentage<br>**Prices**<br>HICP Actual rentals for housing, Index, 2015=100<br>House price index, 2010=100<br>Real housing prices (=HPI/HICP00)<br>Real rents (=RENTS/HICP00)<br>TI<br>Construction Cost Index, Residential Buildings (2010=100, WDSA)<br>HICP Actual rentals for housing, Index, 2015=100<br>Real rents (=REN/HICP00)<br>House price index, 2010=100<br>Real housing prices (=HPI/HICP00)<br>House price index, New dwellings, 2010=100<br>House price index, Existing dwellings, 2010=100<br> **Rates**<br>Euro Nominal Efective Exchange Rate - 42 trading partners, Index, 2005=100<br>Foreign Exchange Rate: United Kingdom (GBP per EUR - quarterly average)<br>Foreign Exchange Rate: Switzerland (CHF per EUR - quarterly average)<br>Foreign Exchange Rate: Japan (JPY per EUR - quarterly average)<br>Foreign Exchange Rate: United States of America (USD per EUR - quarterly average)<br>**ons**<br>EA Business Climate Indicator (SA)<br>Construction Confdence Indicator (SA)<br>Economic Sentiment Indicator (SA)<br>Industrial Confdence Indicator (SA)<br>Retail Confdence Indicator (SA)<br>Consumer Confdence Indicator (SA)<br>Services Confdence Indicator (SA)|
|LTINT<br>i<br>STINT<br>i<br>MIR<br>i<br>COB<br>i<br>**Stock Pri**<br>SP<br>SP<br>i<br>OWN<br>i<br>**Housing **<br>RENTS<br>HPI<br>RHPI<br>RRENTS<br>BUILDCOS<br>REN<br>i<br>RREN<br>i<br>HPI<br>i<br>RHPI<br>i<br>NDW<br>i<br>EDW<br>i<br>**Exchange **<br>NEER<br>EXRUK<br>EXRSW<br>EXRJP<br>EXRUS<br>**Expectati**<br>BSBCI<br>BSCCI<br>BSESI<br>BSICI<br>BSRCI<br>BSCSMCI<br>BSSCI|



58 

## **B Robustness** 

### **B.1 Sub-sample Analysis** 



<!-- Start of picture text -->
GDP HICP LINT<br>1 0.2<br>0<br>0<br>0.1<br>-0.1<br>-1 -0.2<br>0<br>0 10 20 0 10 20 0 10 20<br>SP PCON U<br>0<br>0.05<br>0<br>-5 -0.1<br>0<br>-0.2<br>-10 -0.05<br>0 10 20 0 10 20 0 10 20<br>Steps<br>RHPI RREN<br>0.5<br>0<br>0<br>-0.5<br>-1 -0.5<br>0 10 20 0 10 20<br>Steps Steps<br><!-- End of picture text -->

**Figure 13:** Cross-country impulse responses for selected variables when the model is estimated for the pre-crisis 2001Q1 to 2007Q4 period. 

59 



<!-- Start of picture text -->
GDP HICP LINT<br>1<br>0.2<br>0.2<br>0<br>0.1<br>0.1<br>-1<br>0<br>0<br>0 10 20 0 10 20 0 10 20<br>SP PCON U<br>0 0<br>-2 -0.2 0.1<br>0.05<br>-4 -0.4<br>0<br>-6 -0.6<br>0 10 20 0 10 20 0 10 20<br>Steps<br>RHPI RREN<br>0 0<br>-0.5<br>-1<br>-1<br>-2<br>0 10 20 0 10 20<br>Steps Steps<br><!-- End of picture text -->

**Figure 14:** Cross-country impulse responses for selected variables when the model is estimated for the post-crisis 2008Q1 to 2016Q4 period. 

60 

## **C Model Equations** 

### **C.1 Home Economy Block** 

Patient households: 



Impatient households: 







Terms of trade and identities: 

61 



Consumption sector firms: 



Residential investment sector firms: 







Financial intermediaries 



Aggregation and market clearing: 

62 



### **C.2 EA Economy Block** 



Monetary Policy 





63 

