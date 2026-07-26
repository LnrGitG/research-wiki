---
title: **WORKING PAPER SERIES NO 1249 / OCTOBER 2010**
type: paper
source_pdf: raw/papers/Gattini_Forecasting and assessing euro area house prices through the lens of key fundamentals_2010.pdf
converted: 2026-07-26
---



**Working PaPer SerieS no 1249 / october 2010** 

**ForecaSting and aSSeSSing euro area houSe PriceS through the lenS oF key FundamentalS** 

by Luca Gattini and Paul Hiebert 









# **WORKING PAPER SERIES NO 1249 / OCTOBER 2010** 

**FORECASTING AND ASSESSING EURO AREA HOUSE PRICES THROUGH THE LENS OF KEY FUNDAMENTALS**<sup>**1**</sup> 

by Luca Gattini<sup>2</sup> and Paul Hiebert<sup>3</sup> 



NOTE: This Working Paper should not be reported as representing the views of the European Central Bank (ECB). The views expressed are those of the authors and do not necessarily reflect those of the ECB. 



In 2010 all ECB publications feature a motif taken from the €500 banknote. 



This paper can be downloaded without charge from http://www.ecb.europa.eu or from the Social Science Research Network electronic library at http://ssrn.com/abstract_id=1679733. 

1   We would like to give a special thanks to Anders Warne for providing several MATLAB programs (i.e. SVAR suite) as well as insightful discussions. We are also indebted to Michele Lenza for extensive comments. Lastly, we thank an anonymous referee for helpful comments. 2   Economic Policy Institute, Catholic University of Milan, Via Necchi, 5; 20123 Milan, Italy; email: luca.gattini@unicatt.it and European Central Bank, Kaiserstrasse 29, 60311 Frankfurt am Main, Germany; luca.gattini@ecb.europa.eu 

3   European Central Bank, Kaiserstrasse 29, 60311 Frankfurt am Main, Germany; e-mail: paul.hiebert@ecb.europa.eu 

###### **© European Central Bank, 2010** 

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

_Any reproduction, publication and reprint in the form of a different publication, whether printed or produced electronically, in whole or in part, is permitted only with the explicit written authorisation of the ECB or the author(s)._ 

_Information on all of the papers published in the ECB Working Paper Series can be found on the ECB’s website, http://www. ecb.europa.eu/pub/scientific/wps/date/ html/index.en.html_ 

ISSN 1725-2806 (online) 

## **CONTENTS** 

|Abstract|**4**|
|---|---|
|Non-technical summary|**5**|
|1 Introduction|**7**|
|2 Data and stylised facts|**9**|
|3 The model|**11**|
|3.1 Reduced form model|**11**|
|3.2 Structural model|**13**|
|4 Results|**17**|
|4.1 Forecasting euro area house prices|**17**|
|4.2 Structural decomposition|**19**|
|5 Robustness checks|**25**|
|5.1 Fundamentalness of the system|**25**|
|5.2 Long-run restrictions|**26**|
|6 Conclusions|**26**|
|References|**28**|
|Appendices|**31**|
|Tables|**34**|
|Figures|**39**|



ECB Working Paper Series No 1249 October 2010 

3 

#### Abstract 

This paper presents a parsimonious model for forecasting and analysing euro area house prices and their interrelations with the macroeconomy. A quarterly vector error correction model is estimated over 1970-2009 using supply and demand forces central to the determination of euro area house prices in equilibrium and their dynamics: housing investment, real disposable income per capita and a mixed maturity measure of the real interest rate. In addition to house price forecasts using the resulting reduced form equation, a structural decomposition of the system is obtained employing a common trends framework of King, Plosser, Stock, and Watson (1991), which allows for the identification and economic interpretation of permanent and transitory shocks. The main results are twofold. First, the reduced form model tracks closely turning points in house prices when examining out-ofsample one- and two- step ahead forecasts. Moreover, the model suggests that euro area housing was overvalued in recent years, implying a period of stagnation to bring housing valuation back in line with its modelled fundamentals. Second, housing demand and financing cost shocks appear to have contributed strongly to the dynamism in euro area house prices over the sample period. While much of the increase appears to reflect a permanent component, a transitory component has also contributed from 2005 onwards. Specification tests suggest a robustness of the small model to alternative specifications, along with validity of the long-run restrictions. 

JEL Classification: R21, R31, C32. 

Keywords: House price, Forecasting, Vector autoregression. 

ECB 4 Working Paper Series No 1249October 2010 

### Non-technical summary 

Euro area house price growth has displayed considerable volatility in recent years, rising steadily through the middle of this decade, only to fall precipitously in recent years. Combined with a lower volatility of demand determinants, such as income, and sluggishness in the supply response, many metrics commonly used to gauge the equilibrium valuation of house prices signalled a varying degree of over- or under- valuation of house prices vis`a-vis such fundamentals. More generally, these recent developments appear to be consistent with house prices modelled as deviating on occasion from their broad long-term evolution with standard housing demand and supply fundamentals, but only temporarily. 

One econometric methodology well equipped to deal with a process characterised by dynamic fluctuations around a shared common long-term trend is a vector error- correction model (VECM). This paper presents estimation of such a model for the analysis of euro area house prices, modelling them in a system along with housing demand and supply variables key to their evolution; namely housing investment, income per capita, and a mixed maturity measure of the interest rate – yielding a parsimonious reduced-form equilibrium housing demand-supply relationship. In this setting, housing demand can be thought of as a function of its standard determinants of income and the interest rate, with the latter taking into account the role of financing in the acquisition of housing. Housing supply can also be thought of as depending to a large degree on the same two variables, with internal funds proxied by per capita income and the costs of external finance by the interest rate. The model is estimated at a quarterly frequency for an aggregation of data available for euro area countries, representing 94% of 2007 euro area GDP, from 1970-2009. 

The resulting model is used for two purposes. First, it is used to generate forecasts for house prices based on the reduced form model. Second, we provide a structural decomposition, using a so-called “common trends” identification scheme, which allows for the identification and economic interpretation of permanent and transitory shocks. In particular, this method is used to obtain impulse response functions to selected shocks –a transitory housing demand shock, along with permanent financing cost, economy-wide 

ECB Working Paper Series No 1249 October 2010 5 

technology and housing technology shocks– as well as a variance decomposition and permanent-transitory contribution based on this shock characterisation. 

The results suggest not only that the model has a superior forecasting performance to naive time series models, but also that the cointegrating relationship (embedding some mean revision of real house prices to their modelled demand and supply determinants) has helped to predict recent house price developments with a greater degree of accuracy than models without such a long-term equilibrium condition. Moreover, the model suggests that euro area housing has been overvalued in recent years, implying a period of stagnation to bring housing valuation back in line with its modelled fundamentals. The results from the structural decomposition of shocks yields the additional finding that housing demand and financing cost shocks have contributed strongly to the dynamism in euro area house prices over the sample period. While much of the increase appears to reflect a permanent component, a transitory component has also contributed from 2005 onwards. In particular, housing preference and income shocks were a key driver in explaining house price dynamics over this period. In general, specification tests suggest a robustness of the small model to alternative specifications, along with validity of the long-run restrictions. 

While the results from this rather streamlined model for the euro area are only indicative of larger-scale trends in the euro area housing market resulting from the interaction of several processes, they nonetheless appear to fit well to many facts regarding the euro area housing market witnessed over the last years. 

ECB Working Paper Series No 1249 6 October 2010 

### 1 Introduction 

The dynamics of residential house prices in the euro area have displayed considerable volatility in recent years. Through the middle of this decade, the growth rate of house prices in the euro area rose steadily, only to fall precipitously in recent years. Following the steady appreciation in house prices in the years leading up to 2005, many metrics commonly used to gauge the equilibrium valuation of house prices signalled overvaluation.<sup>1</sup> This rise and subsequent fall in house price inflation suggests a time-varying gap between real house prices and their fundamental supply and demand determinants. These recent developments appear to be consistent with a longer-term phenomenon characterised by temporary deviations of house prices from a broad long-term evolution with standard housing demand and supply fundamentals. 

This paper empirically analyses aggregate euro area housing market developments –with a focus on house price developments– using a vector errorcorrection model (VECM) framework, a methodology well suited to the analysis of a system characterised by stable low-frequency comovement among variables combined with shorter-term heterogeneous dynamics across variables. While it is possible to envisage a wide range of demand and supply fundamentals which would underlie the evolution of house prices, we adopt a relatively parsimonious system specification using four interrelated variables key for the evolution of house prices (see Figure 1): Real house prices, real housing investment, income (in the form of quarterly real disposable income per capita), and a measure of the real interest rate. The model can be thought of as an essentially reduced-form equilibrium housing demandsupply relationship, with income and interest rates determining housing demand and supply (with the latter loosely based on a financial accelerator mechanism, with internal funds proxied by income and costs of external finance by the interest rate). The system also is well equipped to capture likely multifaceted interactions amongst the variables analysed. 

The resulting VECM is used for two purposes. First, it is used to generate forecasts for house prices based on the reduced form model. The results suggest not only that the model has a superior forecasting performance to a 



> 1See, for instance, metrics such as house price-income and house price-rent ratios as presented in Girouard, Kennedy, van den Noord, and Andr´e (2006). 

ECB Working Paper Series No 1249 October 2010 <mark>7</mark> 

naive VAR model, but also that the cointegrating relationship –embedding some mean revision of real house prices to their modelled demand and supply determinants– has helped to predict recent house price developments with a greater degree of accuracy. The model suggests that euro area housing has been overvalued in recent years, implying a period of stagnation to bring housing valuation back in line with its modelled fundamentals. Second, we employ a structural decomposition, using a “common trends” identification scheme, which allows for the identification and economic interpretation of permanent and transitory shocks. Four shocks are identified: a transitory housing demand shock, along with permanent financing cost, economy-wide technology and housing technology shocks. This structural decomposition allows for policy analysis in the form of impulse responses, a variance decomposition, and a decomposition of shock-based movements of the modelled variables into permanent and transitory components. The results from this analysis indicate that housing demand and financing cost shocks have contributed to the dynamism in euro area house prices over the sample period. While much of the increase appears to reflect a permanent component, a transitory component has also contributed from 2005 onwards. In general, specification tests suggest a robustness of the small model to alternative specifications, along with validity of the long-run restrictions. 

The remainder of the paper is structured as follows. Section 2 outlines the data and their properties, along with a brief review of selected literature related to the modelling of euro area house prices. Section 3 outlines the model, first in a reduced form, then the structural decomposition used to generate impulse responses and variance decompositions. Section 4 then presents the main results, first regarding the forecasting performance, then of the properties of the structural model (including impulse responses and variance decomposition, along with a decomposition of variables into permanent and transitory components). Section 5 contains two key robustness checks, related to the “fundamentalness” of the system and the long-run restrictions imposed on the model. Section 6 is dedicated to the concluding remarks. 

ECB Working Paper Series No 1249 8 October 2010 

### 2 Data and Stylised Facts 

House price movements in the euro area since 1970 appear to have exhibited low-frequency fluctuations around an upward sloping trend, a trend which had become increasingly positively sloping in recent years. As shown in Figures 2 and 3, real house prices and their growth rate for the euro area have displayed a high degree of persistence, with a strong increase in valuation in the early years of this millennium – not unlike the evolution of real house prices witnessed in other developed economies around the globe (e.g. US in Figure 2) over the period. The high degree of persistence, combined with a high amplitude of resulting cycles, can also imply some propensity for boom and bust behaviour, similar to that documented in Agnello and Schuknecht (2009), along with house/ asset price overshooting, as documented for instance in Hiebert and Sydow (2009). Interestingly, from trough to peak, the real increase in house prices has tended to be almost the same in both the euro area and the US. Moreover, in both economic areas the duration of upward trends has tended to be shorter than downward trends. 

The recent sharp increase in house prices has at least been partly related to housing demand and supply fundamentals. On the demand side, income and interest rates have been closely associated with house price movements (see Figure 3). In particular, the long-term increase of GDP in real terms over the period of around 2 per cent per year has generated some trend increase in the purchasing power of households. At the same time, as housing is predominantly financed with borrowing, the fairly steady decrease in the real long-term government bond interest rate over the period 1995-2008 has reduced the cost of financing, thereby coinciding with much of the acceleration in euro area house prices. Indeed, this general decline in interest rates over the sample period has softened the burden associated with housing debt, thereby facilitating the financing of house purchases via external credit. A lower interest rate may have also contributed to increase the desirability of housing relative to other assets perceived as lower risk on account of its impact on the risk free return on financial assets. On the supply side, the growth of real housing investment has been closely associated with house price inflation. The fairly cyclical pattern exhibited by housing investment has also tended to lag house price increases somewhat, consistent with the notion that housing supply only sluggishly reacts to demand given consid- 

ECB Working Paper Series No 1249 October 2010 

9 

erable constraints (see, for instance, ECB (2003)). 

As the primary interest of the model is to study the dynamics of house prices, the VECM is designed to parsimoniously capture supply and demand forces central to the determination of house prices in equilibrium and their dynamics. Apart from the above close link to housing investment, house prices have a strong link with both income and interest rates – both via a standard housing demand function and a housing supply function. On the demand side, McQuinn and OReilly (2007) propose a theoretical model of house price determination that is driven by changes in income and interest rates. Likewise, Girouard, Kennedy, van den Noord, and Andr´e (2006) indicate that in advanced economies real house prices have fluctuated around an upward trend at least since 1970, generally attributed in the literature to rising demand for housing space – linked to increasing per capita income as well as a growing population on the demand side. With a generally low rate of population growth on average in the euro area, per capita income developments have likely played a dominant role. 

On the supply side, housing investment can be thought of as a function of households’ internal funds (using current income as a proxy for permanent income) and a measure of the cost of external finance (the interest rate) with housing acquisition being mainly debt-financed –in addition to house prices as a measure of the value of collateral– in the spirit of a modified financial accelerator framework.<sup>2</sup> Indeed, Iacoviello (2006) presents a standard financial accelerator model augmented by collateral constraints tied to real estate values and, for a subset of the households, nominal debt.<sup>3</sup> 

Ultimately, a four-variable system is adopted in the estimated VECM. The time series involve quarterly data from 1970 to 2009, for real house prices 



> 2Given that housing also has an important land component, the housing supply elasticity is also likely to play a strong role in house price developments. Glaeser, Gyourko, and Saiz (2008) find that US locations with more elastic housing supply have fewer and shorter bubbles, with smaller price increases. That said, housing supply is likely to be uniformly less elastic in the euro area compared with the US. 

> 3We do not include any explicit measure of credit constraints aside from any correlated of such constraints with the interest rate, given both the continued predominance of traditional bank lending in the euro area for house purchase along with the desire to adopt a parsimonious specification with an emphasis on generating house price forecasts in an internally consistent and tractable system. Moreover, credit variables such as stock and flow of credit for housing purchase in the euro area are only available at the earliest in 1980, while a estimation of a cointegrated system should be based on a set of fundamental variables as long as possible. 

ECB Working Paper Series No 1249 10 October 2010 

(hpt), real housing investment (hit), real disposable income per capita (yt), and a mixed real interest rate (rt). While a richer set of variables can be thought of as exerting an influence on housing market variables, a parsimonious specification is adopted given the focus on house prices forecasts from a small contained system. Moreover, a similar small system has already been employed in other studies such as Iacoviello and Minetti (2007) and Iacoviello (2002). Additionally, a DSGE model studying the spillovers from the housing market (Iacoviello and Neri (2010)) does not include credit on the basis that “most of the effects of credit shocks are redistributive, and their estimated effect on aggregate prices and quantities appears limited”<sup>4</sup> . A relatively lengthy time series is collected for a euro area aggregate house prices based on available country data, which amounts to a coverage of 94% of 2007 euro area GDP.<sup>5</sup> The mixed interest rate is constructed by a linear weighting of short- and long-term 10 year government interest rates (see Appendix for details on data). 

### 3 The Model 

This section presents the model used in the subsequent analysis in two steps. First, it presents the reduced form model used to generate forecasts. Second, it outlines the approach used to obtain a structural decomposition (a common trends approach). 

#### 3.1 Reduced form model 

Using the notation of King, Plosser, Stock, and Watson (1991), a reducedform error-correction representation of a standard VAR can be written in moving average form using the Wold representation and assuming that the variables are I(1) processes: 



where ϵt are the one-step ahead i.i.d. linear forecast errors in Xt – the 



- 4A robustness check of our small model is reported in section 5 

> 5The nine countries included are Austria, Belgium, Finland, France, Germany, Ireland, Italy, Netherlands and Spain. For details see Appendix A. 

ECB Working Paper Series No 1249October 2010 11 

vector of endogenous variables– given information on lagged values of Xt. This reduced-form representation can be useful for producing forecasts of variables of interest, notably house prices. 

The assumption that all variables included in the VAR are I(1) processes appears to be validated by the sample data. Table 1 reports a number of tests for detecting a unit root in our variables. The null hypothesis on existence of a unit root cannot be rejected for all four variables under all testing specifications over the full sample period (1970-2009). 

Tests for cointegration of the four variables in the system indicate a single common trend across variables, consistent with the notion of house prices underpinned by an equilibrium of housing demand and supply in the long run. Cointegration tests based on the Johansen methodology (see, for instance, Johansen (1991)) reported in Table 3 do not reject the hypothesis of one cointegrating relation across variables. Specifically, the cointegrating vector representation is: 



where bhi, by and br represent the estimated parameters for housing investment, income, and financing cost variables, respectively (the real house prices coefficient on the left hand side of the long run relation has been normalized to one). 

Table 4 reports the log-run relation for the baseline model estimated between 1970 and 2009. In the estimation, all variables are in logarithms.<sup>6</sup> The estimated coefficients in the long run relation are significant and the signs are as expected. The Akaike, Schwarz and final predictor error criteria (see Table 2) suggest the choice<sup>7</sup> of a five lag VAR. The model performs well under several stability tests and it rejects the hypothesis of autocorrelation in the residuals up to twelve lags (LM Test and Portmanteau Test). 



> 6The real interest rate in specified as log(1 + it), where it is the nominal interest rate in basis points. 

> 7The choice of a relatively long lag length is also justified by the persistency properties of the house prices. 

ECB 12 Working Paper Series No 1249October 2010 

This reduced-form model is used to obtain forecasts of house prices, results of which are reported in Section 4.1. 

#### 3.2 Structural model 

In order to render the VECM system more suitable for policy analysis, a structural decomposition is useful to analyse the responsiveness of the system to structural shocks. Equation (1) can be rewritten in a reduced form including a structure Γ0: 



where ηt is a vector of i.i.d. structural disturbances, ω = Γ<sup>−</sup> 0<sup>1μandD(L) =</sup> Γ<sup>−</sup> 0<sup>1C(L).</sup> 

Let Xt be a k-element vector of the endogenous variables and let Σ be the residual covariance matrix. The class of structural VECM (SVECM) models of interest can then be written as: 



where ϵt and ηt are vectors of length k = 4. ϵt is the observed (or reduced form) residuals, while ηt is the unobserved structural innovation. Γ0 is a matrix to be estimated. The structural innovations are assumed to be orthonormal, i.e. its covariance matrix is an identity matrix. The assumption of orthonormal innovations imposes the following identifying restrictions on Γ: 



where Σe is the variance-covariance matrix of the observed residuals. The orthonormal assumption on the structural innovations imposes that they are uncorrelated. 

Using the common trends approach developed by King, Plosser, Stock, and Watson (1991) –applied to housing market analysis by Iacoviello (2002)– short- and long-run restrictions used in identiying the cointegration proper- 

ECB Working Paper Series No 1249 October 2010 13 

ties of the data. In so doing, we distinguish between structural shocks with permanent and transitory effects on the levels of the variables. The permanent shocks are the source of common stochastic trends among the series. In our application, the number of permanent shocks (n = 3) equals the number of endogenous variables (k = 4) minus the number of cointegrating relations (r = 1), which equal the number of transitory shocks. This latter feature follows from the fact that shocks to a stationary system should not alter the steady state, identified by a stationary linear combination of the variables such as the one identified by a cointegrating vector. 

In order to generate impulse responses and forecast variance decompositions, it is necessary to first calculate the sequence of matrices {Dj}<sup>∞</sup> j=1<sup>from(5),</sup> then identify the innovations in the system and, lastly, compute standard errors for the estimated impulse responses. 

The identification of permanent shocks can be achieved by imposing enough restrictions so that the shocks and their long-run effects may be given an economic interpretation. In order to obtain permanent shocks, D(1) must be different from zero. It follows that {Xt} is nonstationary; indeed, it is I(1) in our case. D(1) has rank n, where n equals to 3 in our model. Moreover, the matrix of long-run multipliers D(1) must be orthogonal to the cointegrating vector: β′D(1) = 0. The first column in matrix D(1) has zero elements, meaning that the first shock has no long-run effects on the system. Furthermore, the time series {ΔXt} has to be jointly stationary. In addition to the above requirement, k(k − 1)/2 restrictions must be imposed. The 4 × 4 nonsingular matrix Γ0 is chosen so that permanent and transitory innovations are independent and the transitory innovations are mutually independent. 

The component D (L) ηt in equation (3) is the impulse response function of ΔXt. The responses in the levels of a shock to ΔXt∗ at t = t<sup>∗</sup> by a one standard deviation change in ηt∗ are given by: 



−1 where the matrix Dj is replaced with the estimated matrix D<sup>ˆ</sup> j = C<sup>ˆ</sup> jΓ<sup>ˆ</sup> 0 and the resp(xinf )=lims→∞resp(Xt∗+s)=R(1). 

ECB 14 Working Paper Series No 1249October 2010 

##### 3.2.1 Permanent Shocks 

The identification of permanent shocks can be achieved by imposing just enough restrictions so that shocks and their effects may interpreted from an economic standpoint. The baseline identification imposes zero restrictions on the first and second columns of the D(1) elements. We do not consider the first column since we have already shown that there are three common trends implying three permanent shocks. Hence the D(1) can be partitioned into D(1) = [0|Ψ] 



where ψij are coefficients to be estimated. The three shocks are analysed below. 

Housing market technology shock : The first column of (7) affects real house prices, real housing investment and real disposable income. As technological shocks to the construction industry – particularly in housing construction – might only be rarely observed, the shock could also be motivated by changes to the regulatory framework. Specifically, changes in building regulations and/or the modification of various zoning laws could cause changes in housing production virtually indistinguishable from changes in housing building technology (Matsuyama (1999)). For example, a decrease (increase) in the time to obtain a building permit, along with changes in regulations governing supply elasticity, could cause an increase (decrease) in investment options available at time t, or in other words generate an increase of the production possibilities given the same amount of land. In terms of impacts, this shock can be thought of as leading to a rise in housing investment on account of a fall in construction costs as well as a related drop in house prices. The impact on the real interest rate would be less clear ex-ante, depending on the time horizon. First, a permanent reduction in the value of houses stemming from a positive housing market related technology shock induces a negative valuation effect on the existing stock of collateral increasing the costs of the debt and a dampening wealth effect (see, for 

ECB Working Paper Series No 1249 October 2010 15 

instance, Darracq and Notarpietro (2008)). Second, strong co-movement between disaggregated investment can be rationalized in a small open economy, where a fixed foreign interest rate could mitigate the competition for limited resources between housing investment and business investment. In contrast, the euro area can be regarded as a relatively closed economy. Excluding positive productivity shocks common to all sectors, which increase returns from investing in housing and business capital, even small differences in the rate of return from different investment tends to generate negative co-movement. In principle, a substitution effect between categories of investment should nullify possible discrepancies in terms of returns between different categories of investment in the long-run. In other words, sectorspecific technology shocks can have an impact in the short-run on interest rates. However, the impact is zero in the long-run assuming counterbalancing movements in the other sectors of the economy. 

Economy wide technological shock : The second column of (7) can be motivated as a standard economy-wide technological shock. It would be expected to exert an impact on all the variables in the system in the long run, with weights dictated by the estimated cointegration vector. 

Financing cost shock : The third column of (7) can be thought of as the outcome of features that permanently alter interest rate risk premia, such as financial innovation or –specific to the case of euro area countries– convergence in the run up to European Monetary Union. Equally, it could capture a permanent change of collateral required to obtain new loans (i.e. a permanent rise of the loan to value ratio). A negative financing cost shock (e.g. permanent fall in the interest rates) would be expected to boost house prices and housing investment, with the impact dependent on the estimated elasticity of housing expenditure to changing interest rates. The impact on overall activity would also be expected to be positive. 

##### 3.2.2 Transitory Shock 

The single transitory shock in the system is a housing demand shock, with a short-run impact (and a zero long-run impact) on all the variables in the system. The temporary shift in preferences toward housing assets can be rationalized in the context of literature on a time-varying housing risk premia obtained, for example, in models analyzing house prices in a dividend- 

ECB Working Paper Series No 1249 16 October 2010 

discount framework (see, for instance, Hiebert and Sydow (2009) or Weeken (2004)). The transitory positive impact on house prices follows from a temporary increase in the attractiveness of housing as a result of a positive housing demand shock. An alternative interpretation is a temporary shift from non-residential demand to residential demand. In addition to housing consumption, this shock also boosts housing investment given factors such as its impact on expectations of appreciation in house prices. The housing investment impact, in turn, has a mechanical positive impact on income via the standard national income accounting framework, and a positive impact on interest rates through this latter economic impact. A two way short-run interaction between real interest rate and real income has been excluded via imposing two zero restrictions, a restriction which could be motivated by standard lags in the monetary policy transmission mechanism. 

### 4 Results 

The reduced form VECM is consistently estimated in differenced form over the sample period 1970Q1 to 2009Q4. The resulting time series has a fairly large time dimension, thereby providing enough information in principle for the estimation of the coefficients without any further a priori assumption on the coefficient matrix. Below we report the results of the VECM in two subsections. First, we look at the model in reduced form and we study its out-of-sample forecasting accuracy for house prices. Second, we identify the structural shocks as outlined in the previous section in order to provide a more structural interpretation for house price dynamics. 

#### 4.1 Forecasting euro area house prices 

In this subsection, we present the forecasting performance for house prices on the basis of the reduced-form model. In particular, we construct rolling window forecasts using a 20 years window to obtain historical out-of-sample forecast performance statistics based on 1-, 2- and 4-step ahead forecast errors. Then we present out of sample forecasts up to 2012 for the current cycle. 

The forecast evaluation statistics considered in the coverage of economic 

ECB Working Paper Series No 1249 October 2010 17 

forecasting are: the mean error (ME), the root mean squared error (RMSE), and the mean squared error (MSE). Denoting a series of interest as yt and a forecast of it as ft, the resulting forecast error is given as ϵt = yt − ft, for t = 1, ..., T . Using this notation, this fairly standard set of forecast evaluation statistics considered can be presented as below: 



Table 5 reports one, two and four step ahead forecast errors for the unrestricted VECM specified in section 3.1 and a corresponding VAR specified in levels (Sims, Stock, and Watson (1990)). The errors are based on the out-of-sample rolling forecasts. This exercise should not be interpreted as a ”horse race” across model specifications. Rather, it can be seen as a way to check the reliability of the cointegrating relationships. Indeed, the VAR in levels is the unrestricted counterpart of the VECM since a VECM can be always specified as a VAR in levels with restrictions in the VAR dynamics implied by the error correction mechanism. If the restrictions to the VAR dynamics implied by the VECM are not prominent features of the data, the unrestricted VAR in levels is more likely to outperform the VECM specification in terms of forecast accuracy. Table 5 summarizes the above statistics both for the full sample and for selected subsamples. The results indicate that the VECM model generally outperforms a VAR with same variables and lag structure, on the basis of the ME and RMSE, across the full sample and sub-samples. Indeed, the VECM performed better over all subperiods with the exception of the period 2001-2006 – not surprising given the house price boom over the period, possibly reflecting an unsustainable departure from fundamental determinants contained in the long-run cointegrating relation. This result, together with the overall performance of the VECM, suggests that the imposed cointegration restrictions are not at odds with the data. 

ECB Working Paper Series No 1249 18 October 2010 

The model predicts that, conditional on internally-generated forecasts for other variables, euro area real house prices should decrease until the end of 2010, with a turning point in the course of 2011 (see Figure 4) - based on point estimates. To put the magnitudes into perspective, the model predicts a cumulative depreciation of 8% in real terms in three years. This compares with an increase in real house prices of some 45% from the trough in 1997 through the peak in 2007. Looking at the previous house price cycle, real prices grew by about 25% between 1986 and 1991, then declined following the peak by 8%, with the period of contraction lasting for six years. In this way, the model-based forecast suggests that the recovery would be quicker, the downturn would be faster compared to the previous cycle and shorter (i.e. at most four years of downturn). As mentioned above, the two cycles seem to differ in terms of speed of adjustment. The results suggest that the 8% decrease in real terms in the current cycle will materialise in half of the time required during the cycle of the 1990s. The percentage of devaluation in real terms, instead, would be lower. While housing assets in the previous cycle lost 30% of the value gained in the upward trend, in the current cycle the decline in the value of housing assets would be closer to 18%. 

#### 4.2 Structural decomposition 

In this subsection, we present the results for the conditional model – that is, the structural model placing long- and short-run restrictions using the common trends approach outlined in Section 3.2. The estimated coefficients of the short- and long-run matrices have the predicted signs for all variables. The coefficients on the main diagonal of the long-run matrix are significant and positive, as expected, while the off diagonal coefficients also have the expected sign. 

##### 4.2.1 Impulse Response Functions 

Below, we report the dynamics of the model in response to structural shocks in Figures 5 to 8, for four unit structural innovations: (i) housing demand shock; (ii) housing market technology shock; (iii) economy wide technological shock; (iv) financing cost shock. All shocks are calibrated to be one standard deviation of the log level of the respective series. 

ECB Working Paper Series No 1249October 2010 <mark>19</mark> 

##### Housing Demand Shock 

Figure 5 reports the effects of a housing demand shock. Unsurprisingly, a positive housing demand shock leads to a significant rise in the real house price, with the positive impetus lasting almost five years. The effect on real housing investment is also positive and significant, though somewhat less persistent and with a wider confidence band, and it seems to exercise its effect with some lags with respect to real house prices. This effect is consistent with the finding that the flow into housing supply tends to positively react to house price changes (see, for instance, Topel and Rosen (1988) or Malpezzi (1999)). Real disposable income per capita, in contrast, does not seem to react significantly to the housing demand shock. In this way, the evidence does not support of a financial accelerator mechanism applied to housing assets at the economy-wide level. The real interest rate reacts positively to a housing demand shock, though only initially. This could suggest that frictions in credit supply imply a rise in the price of credit with a booming demand for loans to finance an increasing demand for housing. 

##### Housing Market Technology Shock 

The impact of a positive housing technology shock has long-run dampening effect on house prices, steadily growing in absolute terms and peaking in its impact after around 4-5 years. It decreases real house prices in the long run by around 2% while providing a steady long-run boost to real housing investment. In terms of quantities, the shock generates approximately a 1% permanent increase in real housing investment. The effect on real disposable income per capita is positive once it stabilizes, roughly after 3-4 years. This may reflect a counterbalancing effect of two countervailing forces. On the one hand, a permanent increase in productivity of the housing sector should crowd out productive investment in others sectors. On the other hand, the associated decline in house prices may boost the other sectors of the economy through its direct impact via the aggregate investment component. The impact on the interest rate is short-lived, with a significant increase of the real interest rate in the short-run (i.e. one year) which is subsequently absorbed. This combination of strong short-term and muted long-term impacts may be viewed in the context of learning, where the effects on the lending price are neutral once it is clear that house price impacts reflect supply (and not demand) factors. 

ECB Working Paper Series No 1249 20 October 2010 

##### Economy Wide Technological Shock 

This shock, which alters productivity at aggregate level, is associated with a steady increase in real house prices. Naturally, the shock also generates a positive impact on economic growth – with the long-run increase in real house prices (of around 1 %) roughly double the magnitude of the increase in real income per capita. As expected the impact on housing investment is significant whereas the impact on the interest rate is limited and of the opposite sign compared to housing market technology shock. 

##### Financing Cost Shock 

This shock, analogous to a shock that permanently increases the borrowing costs for firms and for households, produces a fall in house prices of around 1% and a fall in housing investment of a similar amount. The impact on per capita income is negative, even in the long run, though confidence bands suggest that a zero impact cannot be excluded. The impact on the real interest rate is both positive and significant. 

##### 4.2.2 Variance decomposition 

In this subsection, we present a variance decomposition derived from the structural model – mapping the identified structural shocks to the fluctuations in both housing and non-housing variables. Not surprisingly, housing demand shocks play a strong role in explaining house prices, while the housing technology shock plays a strong role in explaining housing investment – with each initially explaining around 60% of initial variance in the series. The housing demand shock, however, subsides steadily in its explanatory power whilst others rise in importance through time, notably the economy wide technology shock. Indeed, the decomposition suggests that the financing cost shock plays a prominent role in explaining the variance of housing market variables. For both the real house price and housing investment, there is a growing relevance 2-4 years after the shock in explaining forecast error variance. Economy-wide technology shocks, in contrast, play a limited role in explaining the variance of housing investment after 8-9 quarters. As expected, the economy-wide technology shock does, however, play a strong role in explaining movements in real income per capita. With time, financing cost shocks appear to also contribute to explain variance in the evolution of 

ECB Working Paper Series No 1249October 2010 <mark>21</mark> 

per capita income. Housing market-related shocks, in contrast, play almost no role in explaining the variance of aggregate per capita income. Again there is no clear evidence in favor of a direct link between housing value increases and economic expansion via a direct wealth effect on consumption (Iacoviello (2009)), for instance. The variance of real interest rates is dominated by financing cost shocks, but also housing demand shocks play a minor role. 

##### 4.2.3 Historical decomposition 

While the variance decomposition in the previous subsection assumes that structural shocks are independent and uncorrelated across time, this section presents a historical variance decomposition of the structural model based on less restrictive assumptions. Specifically, the historical decomposition is an accounting exercise that decomposes historical values into a baseline forecast as well as the accumulated effects of the current and past shocks. When interpreting the shocks, it should be considered that the impact of a shock on a variable corresponds to the cumulated effects of current and past shocks (so that values at a specific point in time may correspond to an accumulated effect due to past shocks). Figure 10 reports the historical decomposition for the key variables of the model since 1999 (more or less the beginning of the latest house price cycle). The black line in the figure is the log-level deviation from the baseline projection and the colored bars are the contributions of shocks under analysis. 

An examination of all the sub-figures clearly highlights a relevant role of financing cost shocks on all variables. Financing cost shocks, via a real interest rate channel, has pushed up real housing investment, real house prices and, importantly, real income per capita via investment and a reduction of the costs of financing private consumption. In this way, an easing of the burden of debt has boosted all real variables in our stylised model. 

Results for real house prices suggest that temporary housing demand shock combined with a relevant effect of the economy wide shock can explain large part of the increase in house prices in the period leading up to mid 2007. The combined effect of the above structural shocks and interest rate shock has, in contrast, lasted until the end of 2009. Once the financing cost shock effect elapsed, a housing supply shock seems to play major role in reducing 

ECB 22 Working Paper Series No 1249October 2010 

the turned negative deviation from the baseline projection. 

Real housing investment has been sustained mainly by financing cost shocks and a marginal economy wide shock. This has the implication that construction firms were reacting to a temporary shift in housing preferences in the short- to medium-run. 

Finally, the historical decomposition for real income per capita suggests that a credit effect has sustained output whereas economy-wide technological shocks exerted a negative impact from 2006 onward. For real interest rates, the impact of the shocks other than financing cost shock itself is limited, meaning that an easing of credit conditions is manly explained by a structural change in the credit market and an associated shift in the pricing of risk. 

##### 4.2.4 Permanent and transitory decomposition 

Our model allows for a decomposition between fundamental and non-fundamental movements of the variables – since once the structural model has been estimated, it is possible to calculate the contributions to the Beveridge-Nelson (B-N) type permanent and transitory components decomposition (Beveridge and Nelson (1981)) attributed to the various structural shocks. For cointegrated multivariate processes, several permanent-transitory decompositions have been extensively used in empirical analysis<sup>8</sup> including the multivariate decomposition proposed by Stock and Watson (1988). The permanent component contains the estimated long-run trend of each variable and it shows how single forces additively generate its trend. The transitory component represents the cycle around the identified long-term trend. Figures 11 and 12 contain the results of this decomposition. 

##### Real House Prices 

Regarding the transitory component of real house prices, the overall picture (figure 11) signals four upward cycles, namely: (i) the beginning of the 1970s; (ii) the beginning of the 1980s; (iii) the beginning of the 1990s; and (iv) the middle of the current decade. Two features are particularly noteworthy. First, the current upward cycle, which is in a downward trend since the end 



> 8For an all inclusive theoretical investigation of the permanent-transitory decomposition in VAR models with cointegration see Hecq, Palm, and Urbain (2000) 

ECB Working Paper Series No 1249 October 2010 <mark>23</mark> 

of 2007, is very similar in magnitude to the cycle of the 1980s. Second, the driving shocks are different. The 1970s cycle was driven by housing market shocks whilst the current transitory component have a relevant contribution from housing investment shocks, financing cost shocks, economy wide shocks and marginally by preference shocks. In this way, transitory financing cost shocks have helped to boost the transitory component of house prices. 

The permanent component of real house prices has three major contributions, from real interest rates, real income per capita and housing market technology shocks. Interestingly, real interest rates have played a fairly constant role over our sample period whilst real income per capita has increased its contribution and investment has contemporaneously decreased its support. Moreover, the model predicts that real house prices in the most recent cycle have been overvalued from 2006 onward. The maximum measured gap between the actual value and the fundamental value is roughly in a band of 10-15% (i.e. the distance between the dotted line and the solid line in figure 12). 

##### Real housing investment 

The permanent component of real housing investment seems to capture most of the increase over the last years. The transitory component signals two upward cycles, namely: the beginning of the 1980s and the middle of the 1990s. The main driver of these cycles has been a combination of housing preference shocks, housing market technology shocks and financing cost shocks. From 2000 onward the transitory component has been driven by negative temporary technology shocks. One interpretation is that either the productivity in this sector has decreased or temporary restrictive regulations on building space have been implemented. 

##### Real income per Capita and Real Interest Rate 

Concerning real long term interest rate and real income per capita the model would not be expected to give a full explanation, given its focus on the housing market and stylised interaction with the economy. Nevertheless, some elucidation of housing and business cycle properties may shed some light on recent cyclical dynamics. In the model decomposition, real housing investment substantially explains half of the temporary cycle of real income. The model suggests that housing investment has, accordingly, made an unusually strong contribution to GDP growth before these episodes in the same spirit 

ECB 24 Working Paper Series No 1249October 2010 

of Leamer (2007). Indeed, concentrating on business cycle turning points, the euro area in this way has not seen an analogue to the consistently strong abnormal contributions of housing investment to virtually all US recessions since 1970. 

### 5 Robustness Checks 

#### 5.1 Fundamentalness of the system 

We have opted for a small scale model to explain real house price levels and movements as a function of a small, but fundamental, set of macroeconomic variables. However, there may be other variables which potentially enter the cointegrating relation and, consequently, influence the fundamental shocks. In particular, we have included a measure of the interest rate as a central explanatory variable, though loans to households for house purchase may influence the fundamental behavior of house prices and affect the reliability of the structural shocks analyzed in the small system. To check the fundamentalness of other auxiliary variables, we follow Giannone and Reichlin (2006). Let us consider the system in equation 3 where the fundamental set of variables, Xt<sup>∗isaugmentedwithblocksofauxiliaryvariables,Xt.The</sup> new compact form system can be written as: 



where vt are additional structural shocks, orthogonal to the structural shocks of interest, ηt<sup>∗.ΔXt=(ΔX</sup> 1′ t<sup>, ..., ΔX</sup> kt′<sup>)′isavectorofadditionalvariables,</sup> D(L) = (D1(L), ..., Dk(L))<sup>′</sup> and φ(L)=(φ1(L), ..., φk(L))<sup>′</sup> . The zero restriction comes from model 3. It implies that the additional shocks are specific to the added variables. If ηt<sup>∗isfundamentalwithrespecttoΔX</sup> t<sup>∗,thenthe</sup> structural shocks can be recovered from past observables. The additional variable i is a function of its own shocks and the past observations of the Xt<sup>∗variablessincevtisorthogonaltoX</sup> t<sup>∗.Thatis:</sup> 



ECB Working Paper Series No 1249 October 2010 <mark>25</mark> 

As a consequence non-fundamentalness can be checked empirically using a Granger causality test. Specifically, it should be tested whether the block Xt<sup>∗isweaklyexogenouswithrespecttotheadditionalblocksofvariables</sup> Xt that are likely to a have a common driving factor. Table 6 reports the Granger causality tests for the block of the core model with respect to two additional variables, namely the flow of credit for housing purchase and the stock of credit for housing purchase. These series start from 1980 whereas the core system is estimated from 1970. Henceforth, the block exogeneity test is conducted only for the shorter sample. The results of the test do not reject the null hypothesis that the additional variables do not Granger-cause Xt<sup>∗.Thehypothesisofweakexogeneityisnotrejectedand,consequently,</sup> non-fundamentalness of the system in equation 3 is not detected. 

#### 5.2 Long-run restrictions 

A second robustness check concerns the long-run restriction imposed on matrix 7: the zero restriction imposed on its first column limiting the impact of housing investment on the real interest rate in the long-run. As a counterfactual, figure 13 reports the impulse response computed imposing no restrictions on matrix 7. Specifically, the restriction on the impact of investment on the real interest has been added to the short run matrix which continues to include the restrictions summarized in section 3.2.2. The differences are marginal in both qualitative and quantitative terms. The main discrepancy is related to the response of the real income to a housing technology shock. The impulse response function becomes insignificant. Henceforth, it can be inferred that the zero long-run restriction, despite having an economic reason as explained in section 3.2.1, does not have a relevant impact on the structural system. 

### 6 Conclusions 

This paper presented an empirical framework for the forecasting and analysis of house prices in the euro area using a vector error-correction model (VECM). In this framework, real house prices are related to selected housing demand and supply fundamentals, including real housing investment, real income per capita, and the real interest rates. This long-term cointegration rela- 

ECB Working Paper Series No 1249 26 October 2010 

tionship and heterogeneous dynamics of this framework fits well with the observed behaviour of euro area house prices over the last decades, characterised by a stable long-term relationship with respect to demand and supply fundamentals accompanied by intermittent episodes of overshooting. The main results are twofold. First, the reduced form model tracks closely turning points in house prices when examining out-of-sample one- and twostep ahead forecasts and the unrestricted VECM suggests a correction in the current cycle of roughly 8% in real terms. Second, once a set of identifying restrictions is imposed, we obtain a high sensitivity of real house prices to the forces driving economic fluctuations similar to Iacoviello (2002). The model suggests that euro area housing has been overvalued in recent years, implying a period of stagnation, which is already started in 2009, to bring housing valuation back in line with its modelled fundamentals. Housing and financing cost shocks appear to have contributed strongly to the dynamism in euro area house prices over the last years. During the last house price boom much of the increase appears to reflect a permanent component with an increasing importance of real disposable income per capita. The income component, more generally, becomes increasingly important in explaining the long-run trend of real house prices. Two-thirds of the increase is judged to be based on fundamentals with income playing an increasing role until 2006. A transitory component has, nonetheless, also contributed – particularly since 2006. In particular, housing preference and income shocks were a key driver in explaining house price dynamics over this period. This result is in line with the finding in the literature that housing preference shocks tend to play a leading role in explaining cyclical fluctuations in the residential property market (see Barot (2001)). Additionally, the findings in the structural model suggest that supply significantly reacts to price movements both in the long and in the short run with differing elasticities as also suggested by Jud and Winkler (2003). While the results from this rather streamlined model for the euro area are only indicative of larger-scale trends in the euro area housing market resulting from the interaction of several processes, they nonetheless appear to fit well to many facts regarding the euro area housing market witnessed over the last years. Moreover, specification tests suggest a robustness of the small model to alternative specifications, along with validity of the long-run restrictions. 

ECB Working Paper Series No 1249 October 2010 <mark>27</mark> 

### References 

- Agnello, L., and L. Schuknecht (2009): “Booms and busts in housing markets: determinants and implications,” ECB Working Paper No. 1071 (July). 

- Barot, B. (2001): “An Econometric Demand-Supply Model for Swedish Private Housing,” European Journal of Housing Policy, 1. 

- Beveridge, S., and C. R. Nelson (1981): “A New Approach to Decomposition of Economic Time Series into Permanent and Transitory Components with Particular Attention to Measurement of the ’Business Cycle’,” Journal of Monetary Economics, 7. 

- Darracq, M., and A. Notarpietro (2008): “Monetary Policy and Housing Prices in an Estimated DSGE Model for the US and The Euro Area,” ECB Working Paper No. 972 (November). 

- ECB (2003): “Structural factors in the EU housing markets,” European Central Bank Structural Issues Report (March). 

   - (2009): “Housing Finance in the Euro Area - Structural Issue 

   - Report, March 2009,” European Central Bank, Structural Issues Report, March 2009. 



- Fagan, G., J. Henry, and R. Mestre (2005): “An area-wide model (AWM) for the euro area,” Economic Modelling, 22(1). 

- Giannone, D., and L. Reichlin (2006): “Does information help recovering structural shocks from past observations?,” Journal of the European Economic Association, 4. 

- Girouard, N., M. Kennedy, P. van den Noord, and C. Andr´e (2006): “Recent house price decelopments: The role of fundamentals,” OECD Economics Department Working Paper No. 475. 

- Glaeser, E. L., J. Gyourko, and A. Saiz (2008): “Housing supply and housing bubbles,” Journal of Urban Economics, 64. 

- Hecq, A., F. C. Palm, and J.-P. Urbain (2000): “Permanent-transitory Decomposition in VAR Models with Cointegration and Common Cycles,” Oxford Bulletin of Economics and Statistics, 62. 

ECB Working Paper Series No 1249 28 October 2010 

- Hiebert, P., and M. Sydow (2009): “What drives returns to euro area housing? Evidence from a dynamic dividend-discount model,” ECB Working Paper No. 1019 (March). 

- Iacoviello, M. (2002): “House Prices and Business Cycles in Europe: a VAR Analysis,” Boston College Working Paper in Economics No. 540. 

   - (2006): “House Prices, Borrowing Constraints, and Monetary Pol- 

   - icy in the Business Cycle,” American Economic Review, 95. 



- (2009): “Housing Wealth and Consumption,” draft entry prepared 

- for the International Encyclopedia of Housing and Home, Elsevier, forthcoming, 2011. 



- Iacoviello, M., and R. Minetti (2007): “The credit Channel of Monetary Policy: Evidence from the Housing Market,” Journal of Macroeconomics, 30. 

- Iacoviello, M., and S. Neri (2010): “Housing Market Spillovers: Evidence from an Estimated DSGE Model,” American Economic Journal: Macroeconomics, 2. 

- Johansen, S. (1991): “Estimation and Hypothesis Testing of Cointegration Vectors in Gaussian Vector Autoregressive Models,” Econometrica, 59. 

- Jud, D., and D. Winkler (2003): “The Q Theory of Housing Investment,” Journal of Real Estate Finance and Economics, 27. 

- King, R., C. Plosser, J. Stock, and M. Watson (1991): “Stochastic Trends and Economic Fluctuations,” American Economic Review, 81. 

- Leamer, E. E. (2007): “Housing IS the Business Cycle,” Proceedings, Federal Reserve Bank of Kansas City, pages 149-233. 

- Malpezzi, S. (1999): “A Simple Error Correction Model of House Prices,” Journal of Housing Economics, 8. 

- Matsuyama, K. (1999): “Residential Investment and the Current Account,” Journal of International Economics, 28. 

- McQuinn, K., and G. OReilly (2007): “A Model of Cross-Country House Prices,” Central Bank and Financial Services Authority of Ireland Research Technical Paper 5 (July). 

ECB Working Paper Series No 1249October 2010 <mark>29</mark> 

- Sims, C. A., J. H. Stock, and M. W. Watson (1990): “Inference in Linear Time Series Models with Some Unit Roots,” Econometrica, 58. 

- Stock, J. H., and M. W. Watson (1988): “Testing for Common Trends,” Journal of the American Statistical Association, 83. 

- Topel, R., and S. Rosen (1988): “Housing Investment in the United States,” Journal of Political Economy, 96. 

- Weeken, O. (2004): “Asset Pricing and the Housing Market,” Bank of England Quarterly Bulletin, Spring 2004. 

ECB Working Paper Series No 1249 30 October 2010 

### Appendices 

### A Data 

##### HOUSE PRICES 

Definition: Real GDP-weighted aggregation of national indices of residential property prices. The included euro area countries are: Austria, Belgium, Finland, France, Germany, Ireland, Italy, Netherlands and Spain, together representing 94% of the euro area GDP in 2007. It is computed aggregating variables with a fixed weight procedure, where weights reflect 2007 relative GDP composition. Deflated using the private consumption deflator. Data for some countries (e.g. Germany and Italy) has been interpolated by the OECD (for reference see Girouard, Kennedy, van den Noord, and Andr´e (2006)). From 1996 biannual data interpolated with a quadratic-match approach. 

Units: Index, 2000=100. 

Source: OECD for country data and authors’ calculations based on national data; ECB from 1996 onward. 

##### HOUSING INVESTMENT 

Definition: Gross fixed capital formation: housing - at current prices in ECU/euro, seasonally and/or or working day adjusted, deflated using the private consumption deflator. 

Units: Euro in 2000 terms. 

Source: OECD and Eurostat. 

##### DISPOSABLE INCOME PER CAPITA 

Definition: Disposable income divided by population backdated (between 1970 and 1980) with GDP per capita - at current prices in ECU/euro, deflated using the private consumption deflator. 

ECB Working Paper Series No 1249 October 2010 <mark>31</mark> 

##### Units: Euro in 2000 terms. 

Source: Population - UN and OECD; Disposable income - Eurostat. GDP - ECB’s area-wide model database (for reference see Fagan, Henry, and Mestre (2005)). 

##### MIXED INTEREST RATE 

Definition: The nominal interest rate is a weighted average of the rate of interest on government bond with long-dated maturity (e.g. 10-years) and a short-term interest rate based on a Euribor 3-month and backdated with ECB calculations based on Eurostat data and the ECB’s area-wide model database (see source ). The weights are based on the structural evidence on the share of variable rate loans in total new house price loans for 2007 reported in Table 2 of ECB (2009). The aggregate is deflated using the private consumption deflator. 

##### Units: Percentage. 

Source: long-term interest rate - OECD; short-term interest rate - ECB. The latter is the Euro area (changing composition) - Money Market - Euribor 3- month - last trade price or value - Euro from 1994 onward and it is backdated with ECB calculations based on Eurostat data and the ECB’s area-wide model database (for reference see Fagan, Henry, and Mestre (2005)). 

##### PRIVATE CONSUMPTION DEFLATOR 

Definition: Deflator for private consumption applied to nominal variables. 

Units: Index, 2000=100. 

Source: Eurostat and ECB calculations. 

ECB Working Paper Series No 1249 32 October 2010 

### List of Tables 

|1|Augmented Dickey-Fuller test statistic - ADF Test .|.<br>34|
|---|---|---|
|2|VAR Lag Order Selection Criteria<br>. . . . . . . . . . .|.<br>34|
|3|Unrestricted Cointegration Test - Johansen Method . .|.<br>35|
|4|Long-Run Cointegrating Relation . . . . . . . . . . . .|.<br>36|
|5|Error Forecast: Summary . . . . . . . . . . . . . . . . .|.<br>37|
|6|Granger Causality Test. . . . . . . . . . . . . . . . . . .|.<br>37|



ECB Working Paper Series No 1249 October 2010 <mark>33</mark> 

Table 1: Augmented Dickey-Fuller test statistic - ADF Test 

||Level<br>t-Statistic|First Diference<br>t-Statistic|
|---|---|---|
|Real Private Residential Investment|0.271659|-6.857562|
|Real Mixed Int. Rate|-1.763088|-7.875|
|Real House Prices|-0.635945|-3.904523|
|Real Disp. Income|-0.269331|-8.870832|





<!-- Start of picture text -->
Real Disp. Income -0.269331 -8.870832<br>Note: Null Hypothesis - Variable has a unit root; t-Stat. critical values:<br>1 per cent: -3.473967; 5 per cent: -2.880591; 10 per cent: -2.577008<br><!-- End of picture text -->

Note: Null Hypothesis - Variable has a unit root; t-Stat. critical values: 1 per cent: -3.473967; 5 per cent: -2.880591; 10 per cent: -2.577008 Tests include intercept and not trend 



<!-- Start of picture text -->
Tests include intercept and not trend<br><!-- End of picture text -->

Table 2: VAR Lag Order Selection Criteria 

|Lag|LogL|LR|FPE|AIC|SC|HQ|
|---|---|---|---|---|---|---|
|1|1969.02|2145.362|2.06E-17|-27.06973|-26.65725|-26.90212|
|2|2068.409|186.3529|6.47E-18|-28.2279|-27.48544*|-27.92621*|
|3|2077.376|16.31615|7.15E-18|-28.13023|-27.05779|-27.69445|
|4|2091.561|25.02049|7.35E-18|-28.10502|-26.7026|-27.53515|
|5|2133.438|71.53979|5.15e-18*|-28.46442*|-26.73203|-27.76047|
|6|2144.715|18.63873|5.53E-18|-28.39882|-26.33645|-27.56079|
|7|2155.214|16.76915|6.02E-18|-28.32242|-25.93007|-27.3503|
|8|2166.503|17.40328|6.50E-18|-28.25698|-25.53466|-27.15078|
|9|2181.24|21.90082|6.70E-18|-28.23944|-25.18713|-26.99916|
|10|2195.745|20.75041|6.97E-18|-28.21868|-24.83639|-26.84431|
|11|2220.309|33.77556*|6.32E-18|-28.33763|-24.62536|-26.82917|
|12|2231.167|14.32674|6.97E-18|-28.26621|-24.22397|-26.62367|





<!-- Start of picture text -->
12 2231.167 14.32674 6.97E-18 -28.26621 -24.22397 -26.62367<br>* indicates lag order selected by the criterion<br>LR: sequential modified LR test statistic (each test at 5 per cent level)<br>FPE: Final prediction error<br>AIC: Akaike information criterion<br>SC: Schwarz information criterion<br><!-- End of picture text -->



<!-- Start of picture text -->
HQ: Hannan-Quinn information criterion<br><!-- End of picture text -->

ECB Working Paper Series No 1249 34 October 2010 

Table 3: Unrestricted Cointegration Test - Johansen Method 

||Tr|ace Test||Maximum|Eigenvalu|e Test|
|---|---|---|---|---|---|---|
|Hypothesized||Trace|||Max-Eigen||
|No. of CE(s)|Eigenvalue|Statistic|Prob.*|Eigenvalue|Statistic|Prob.*|
|||Model|with Mi|xed Interest|rate||
|None **|0.188417|54.01489|0.0118|0.188417|31.73278|0.0138|
|At most 1|0.084503|22.28211|0.2831|0.084503|13.41976|0.4144|
|At most 2|0.044458|8.86235|0.3783|0.044458|6.912371|0.4996|
|At most 3|0.012747|1.949978|0.1626|0.012747|1.949978|0.1626|
|||Model|with Long|-Term Interes|t rate||
|None **|0.211859|58.30865|0.0039|0.211859|35.4737|0.004|
|At most 1|0.096716|22.83495|0.2543|0.096716|15.15601|0.2781|
|At most 2|0.029478|7.678941|0.5003|0.029478|4.458204|0.8081|
|At most 3|0.021384|3.220738|0.0727|0.021384|3.220738|0.0727|
|||Model w|ith Short|-Term Interes|t rate||
|None **|0.183216|53.35787|0.0139|0.183216|30.76183|0.0189|
|At most 1|0.098109|22.59604|0.2665|0.098109|15.69582|0.2431|
|At most 2|0.037292|6.900229|0.5893|0.037292|5.776762|0.642|
|At most 3|0.007364|1.123467|0.2892|0.007364|1.123467|0.2892|





<!-- Start of picture text -->
At most 3 0.007364 1.123467 0.2892 0.007364 1.123467 0.2892<br>Max-eigenvalue test indicates 1 cointegrating eqn(s) at the 0.05 level<br>* MacKinnon-Haug-Michelis (1999) p-values<br>** denotes rejection of the hypothesis at the 0.05 level<br><!-- End of picture text -->



<!-- Start of picture text -->
Note: Tests are computed with Eviews 6.0<br><!-- End of picture text -->

ECB Working Paper Series No 1249 October 2010 <mark>35</mark> 

###### Table 4: Long-Run Cointegrating Relation 

|Real Private Residential<br>Investment|2.21<br>(0.6952)|
|---|---|
|Real Disposable Income|-3.07<br>(0.6562)|
|Real Mixed Int. Rate|6.87<br>(1.4354)|
|Speed of Adjustment|-0.013<br>(0.00315)|
|Note: Standard errors in paretheses and Re|al House Prices normilized to one|
|Long-run equations are reported in the form|: et−1 = pt−1 −f(Xt−1)|
|where pt−1 is the real house price and Xt1|is the vector of explanatory variables|





<!-- Start of picture text -->
Note: Standard errors in paretheses and Real House Prices normilized to one<br>Long-run equations are reported in the form: et−1 = pt−1 − f (Xt−1)<br><!-- End of picture text -->



<!-- Start of picture text -->
where pt−1 is the real house price and Xt1 is the vector of explanatory variables<br><!-- End of picture text -->

ECB Working Paper Series No 1249 36 October 2010 

Table 5: Error Forecast: Summary 

||VAR|VECM|VAR|VECM|VAR|VECM|
|---|---|---|---|---|---|---|
||One-St|ep Ahead|Two-St|ep Ahead|Four-St|ep Ahead|
|ME|-0.022|0.012|-0.018|0.127|0.664|0.003|
|MSE|0.271|0.247|1.169|1.082|5.001|4.072|
|RMSE|0.521|0.497|1.081|1.040|2.236|2.018|
||||1991-19|95|||
|ME|-0.282|-0.113|-0.569|-0.021|-1.346|0.465|
|MSE|0.191|0.168|0.878|0.858|4.066|3.722|
|RMSE|0.437|0.410|0.937|0.926|2.016|1.929|
||||1996-20|00|||
|ME|0.099|0.016|0.263|0.051|0.819|0.474|
|MSE|0.310|0.273|1.087|1.081|4.066|3.722|
|RMSE|0.557|0.522|1.043|1.040|2.016|1.929|
||||2001-20|06|||
|ME|0.202|0.208|0.555|0.555|1.738|1.629|
|MSE|0.204|0.206|0.921|0.943|4.913|5.041|
|RMSE|0.451|0.453|0.960|0.971|2.217|2.245|
||||2007-20|09|||
|ME|-0.273|-0.179|-0.760|-0.366|-2.587|-0.923|
|MSE|0.464|0.418|2.218|1.757|8.925|4.929|
|RMSE|0.681|0.647|1.489|1.326|2.987|2.220|





<!-- Start of picture text -->
RMSE 0.681 0.647 1.489 1.326 2.987 2.220<br><!-- End of picture text -->

Table 6: Granger Causality Test 



<!-- Start of picture text -->
F-test p-value<br>Real flow of loans for housing Purchase 2.13003 0.1236<br><!-- End of picture text -->

||F-test|p-value|
|---|---|---|
|Real fow of loans for housing Purchase|2.13003|0.1236|
|Real stock of loans for housing Purchase|2.27594|0.1074|





<!-- Start of picture text -->
Real stock of loans for housing Purchase 2.27594 0.1074<br><!-- End of picture text -->

The test is for the null hypothesis: Xit does not Granger-cause Xit<sup>∗fori=1, 2</sup> 

ECB Working Paper Series No 1249 October 2010 <mark>37</mark> 

### List of Figures 

|1|Evolution of housing market and related variables in the euro area 39|
|---|---|
|2|Real House Prices - index 2000=100<br>. . . . . . . . . . . . . .<br>40|
|3|Main Variables (annual growth rate, unless otherwise denoted) 40|
|4|Out of sample dynamic forecast for real house prices - 2010-2012 41|
|5|Impulse Response Function: Housing Demand Shock - 68 % confdence bands<br>42|
|6|Impulse Response Function: Housing Market Technology Shock - 68 % confdence bands<br>42|
|7|Impulse Response Function: Economy Wide Technological Shock - 68 % confdence bands<br>43|
|8|Impulse Response Function: Financing Cost Shock - 68 % confdence bands<br>43|
|9|Variance Decomposition . . . . . . . . . . . . . . . . . . . . .<br>44|
|10|Historical Decomposition (percentages)<br>. . . . . . . . . . . . . .<br>45|
|11|Transitory component - (B-N type) . . . . . . . . . . . . . . .<br>46|
|12|Permanent component - (B-N type)<br>. . . . . . . . . . . . . .<br>47|
|13|Impulse Response Function: Robustness Check - 68 % confdence bands 4<br>8|



ECB Working Paper Series No 1249 38 October 2010 

Figure 1: Evolution of housing market and related variables in the euro area 



<!-- Start of picture text -->
�����������������<br>�����������������������<br>���������������������� ��<br>��������������������������������������������������<br>���<br>��<br>�� �<br>�<br>��<br>�<br>��<br>�<br>��<br>�<br>�� ��<br>���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ����<br>�<br>�����������������<br><!-- End of picture text -->

ECB Working Paper Series No 1249 October 2010 <mark>39</mark> 

Figure 2: Real House Prices - index 2000=100 



<!-- Start of picture text -->
150<br>140<br>130<br>120<br>110<br>100<br>90<br>80<br>70<br>60<br>1970 1975 1980 1985 1990 1995 2000 2005<br>EA real house prices<br>US real house prices<br><!-- End of picture text -->

Figure 3: Main Variables (annual growth rate, unless otherwise denoted) 



<!-- Start of picture text -->
����������������� ����������������������<br>�� ����������������������� � ����������������������������<br>�<br>�<br>�<br>�<br>�<br>��<br>�<br>��<br>��<br>��� ��<br>���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ���� ����<br><!-- End of picture text -->

ECB Working Paper Series No 1249 40 October 2010 

Figure 4: Out of sample dynamic forecast for real house prices - 2010-2012 











<!-- Start of picture text -->
Peak real prices 1991<br><!-- End of picture text -->























































































ECB Working Paper Series No 1249October 2010 <mark>41</mark> 

Figure 5: Impulse Response Function: Housing Demand Shock - 68 % confidence bands 



<!-- Start of picture text -->
���������������� �����������������������<br>����� �����<br>�����<br>�����<br>�����<br>�����<br>�����<br>����� �����<br>����� �����<br>�����<br>�����<br>������<br>����� ������<br>������ ������<br>� � � �� �� �� �� �� � � � �� �� �� �� ��<br>���������������������� ������������������<br>����� �����<br>�����<br>�����<br>����� �����<br>�����<br>������<br>������<br>�����<br>������<br>������<br>������<br>������ ������<br>� � � �� �� �� �� �� � � � �� �� �� �� ��<br><!-- End of picture text -->

Figure 6: Impulse Response Function: Housing Market Technology Shock - 68 % 

confidence bands 



<!-- Start of picture text -->
����� ���������������� ����� �����������������������<br>����� �����<br>������<br>�����<br>������<br>�����<br>������<br>�����<br>������<br>�����<br>������<br>� � � �� �� �� �� ��<br>� � � �� �� �� �� ��<br>����� ���������������������� ����� ������������������<br>�����<br>�����<br>�����<br>����� �����<br>�����<br>�����<br>�����<br>����� �����<br>����� �����<br>�����<br>�����<br>������<br>����� ������<br>� � � �� �� �� �� �� � � � �� �� �� �� ��<br><!-- End of picture text -->

ECB 42 Working Paper Series No 1249October 2010 

Figure 7: Impulse Response Function: Economy Wide Technological Shock - 68 % confidence bands 



<!-- Start of picture text -->
���������������� �����������������������<br>����� �����<br>�����<br>�����<br>�����<br>�����<br>�����<br>����� �����<br>�����<br>�����<br>�����<br>����� �����<br>� � � �� �� �� �� �� � � � �� �� �� �� ��<br>���������������������� ������������������<br>����� �����<br>�����<br>�����<br>�����<br>������<br>�����<br>������<br>�����<br>����� ������<br>����� ������<br>����� ������<br>�����<br>������<br>� � � �� �� �� �� ��<br>� � � �� �� �� �� ��<br><!-- End of picture text -->

Figure 8: Impulse Response Function: Financing Cost Shock - 68 % confidence bands 



<!-- Start of picture text -->
���������������� �����������������������<br>����� �����<br>����� �����<br>����� �����<br>������ ������<br>������<br>������<br>������<br>������<br>������<br>������<br>������<br>������<br>������<br>������ ������<br>������ ������<br>� � � �� �� �� �� �� � � � �� �� �� �� ��<br>���������������������� ������������������<br>����� �����<br>����� �����<br>����� �����<br>������ �����<br>������ �����<br>������ �����<br>������ �����<br>������ �����<br>� � � �� �� �� �� �� � � � �� �� �� �� ��<br><!-- End of picture text -->

ECB Working Paper Series No 1249 October 2010 <mark>43</mark> 

Figure 9: Variance Decomposition 



<!-- Start of picture text -->
���������������� �����������������������<br>�������������������� ��������������������<br>������������������������������� �������������������������������<br>�������������������������������� ��������������������������������<br>��������������� ���������������<br>��� ���<br>��� ���<br>��� ���<br>��� ���<br>��� ���<br>��� ���<br>��� ���<br>� �<br>� � � � � � � � � ���������������������� � � � � � � � � � ����������������������<br>����������� ������������������������<br>�������������������� ��������������������<br>������������������������������� �������������������������������<br>�������������������������������� ��������������������������������<br>��������������� ���������������<br>��� ���<br>��� ���<br>���<br>���<br>���<br>���<br>���<br>���<br>���<br>���<br>���<br>���<br>���<br>��� ���<br>� �<br>� � � � � � � � � ���������������������� � � � � � � � � � ����������������������<br><!-- End of picture text -->

ECB 44 Working Paper Series No 1249October 2010 

Figure 10: Historical Decomposition (percentages) 



<!-- Start of picture text -->
��������������� ���������������� �����������������������<br>�������������������������������� ���������������<br>������������������������������� ��������������������������������<br>�������������������� �������������������������������<br>���� ���������������� ���� ��������������������<br>�����������������������<br>����<br>����<br>����<br>����<br>���� ����<br>���� ����<br>����� �����<br>����� �����<br>����� �����<br>����������� ������������������<br>���������������<br>���������������<br>�������������������������������� ��������������������������������<br>���� ��������������������������������������������������� ���� ���������������������������������������������������<br>����������� ������������������<br>���� ����<br>����<br>����<br>�<br>�<br>�����<br>�����<br>�����<br>����� �����<br>����� �����<br>������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������<br>������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������<br><!-- End of picture text -->

ECB Working Paper Series No 1249 October 2010 <mark>45</mark> 

Figure 11: Transitory component - (B-N type) 



<!-- Start of picture text -->
���������������� �����������������������<br>��� ������������<br>������������<br>��� ������������ ����<br>��������<br>���<br>��������������������<br>����<br>���<br>� ����<br>����<br>�����<br>����<br>���� �����<br>����������� ������������������������<br>���<br>����<br>����<br>����<br>����<br>���� ����<br>����<br>����<br>�<br>�<br>�����<br>�����<br>�����<br>����� �����<br>�����<br>�����<br>������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������<br>������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������<br>������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������<br><!-- End of picture text -->

ECB Working Paper Series No 1249 46 October 2010 

Figure 12: Permanent component - (B-N type) 



<!-- Start of picture text -->
���������������� �����������������������<br>�������������������<br>���������������� �������������������<br>���������������� ����������������<br>������������ ����������������<br>�������������������������� ������������<br>����������������������������������������� ���������������������������������<br>��� ��� ������������������������������������������������<br>����<br>��� ���<br>�� ����<br>���<br>���<br>����<br>��� �<br>���<br>����<br>��� �<br>���<br>��� ����<br>��� �<br>��� ����<br>��� ��� � ����<br>��� ���<br>� ����<br>���� ���<br>������������������� ����������� ������������������<br>���������������� �������������������<br>���������������� ����������������<br>������������ ����������������<br>��������������������� ������������<br>������������������������������������ ���� ���������������������������� ����<br>���� �������������������������������������������<br>���� ���<br>����<br>��<br>����<br>����<br>���� ���� ����<br>��� ����<br>���� ����<br>����<br>���<br>���� � ����<br>��� ���� ����� �����<br>�����<br>��� ���� �����<br>�����<br>��� ���� ����� �����<br>���� �� ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ���� �� ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������<br>������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������ ������<br><!-- End of picture text -->

ECB Working Paper Series No 1249 October 2010 <mark>47</mark> 

Figure 13: Impulse Response Function: Robustness Check - 68 % confidence bands 

|����������������<br>�����������<br>����������������<br>�<br>�<br>����������<br>����������������<br>�<br>�<br>����������<br>����������������<br>�<br>�<br>����������|
|---|
|�<br>�<br>�<br>�|
|�<br><br><br><br><br><br><br>�<br>�<br>�<br>�<br>�<br>�<br>�<br>�|
|�����<br>�����<br>�����<br>�����<br>������<br>�����<br>�����<br>�����<br>�����<br><br>�����<br>�����<br>�����<br>����<br>����<br>����<br>����<br>����<br>�|
|�����<br>�<br>����<br>������<br>�������<br>������<br>���������<br>�����|
|��<br>�<br>���<br>��<br>����<br>��<br>���<br>��|
|����������<br>�<br>����<br>���������<br>�<br>��<br>��������<br>�<br>��<br>��������<br><br>�<br>��|
|���<br><br><br>���<br>�<br>�<br>�<br>�|
|�<br>�<br>�<br><br>�|
|��<br>�<br>�<br>|
|**k**<br>��<br>�����<br>�����<br>�����<br>�����<br>�<br>������<br>������<br>�����<br>�����<br><br>�����<br>�����<br>�����<br><br>������<br>������<br>�����<br>�����<br>�����|
|<br>**oc**<br>�<br>�<br><br><br>�<br>�<br>��|
|**Housing Preference Shock**<br>**Housing Technology Shock**<br>**Economy Wide Technology Sh**<br>**Financing Cost Shock**<br>��������������������<br>�<br>�<br>��<br>��<br>��<br>��<br>��<br>���������������������<br>�<br>�<br>�<br>��<br>��<br>��<br>��<br>�<br>���������������������<br>�<br>�<br>��<br>��<br>��<br>��<br>�<br>���������������������<br>�<br>�<br>�<br>��<br>��<br>��<br>��<br>|
|�<br>�<br><br><br>�<br><br><br><br><br>|
|������<br>������<br>�����<br>�����<br>�����<br>�����<br><br>������<br>�����<br>�����<br>�����<br>�����<br>�����<br>�����<br>�����<br>�����<br>�����<br><br>������<br>������<br>������<br>�����<br>�����|
|��<br>��<br>��<br>��<br>��<br>��<br>��<br>��|
|��<br>��<br>��<br>��|
|���<br>��<br>���<br>��<br>���<br>��<br>���<br>��|
|����<br>��<br><br>�����<br>��<br>�����<br>��<br><br>�����<br>��|
|���<br>�<br>��<br>�<br>��<br>�<br>��<br>�<br>4~~5~~|
|����<br>�<br><br>����<br>�<br>����<br>�<br><br>����<br>�<br><br>|
|�|
|�<br><br>�<br>�|
|������<br>�����<br>�����<br>�����<br>�����<br>������<br>������<br>������<br>�����<br>�����<br>�����<br>�����<br>�����<br>�����<br>�����<br>������<br>������<br>������<br>�����|



ECB Working Paper Series No 1249 48 October 2010 



