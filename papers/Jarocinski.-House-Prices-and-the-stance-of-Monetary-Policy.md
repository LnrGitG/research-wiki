---
title: **Working Paper**
type: paper
source_pdf: raw/papers/Jarocinski. House Prices and the stance of Monetary Policy.pdf
converted: 2026-07-26
---





Jarociński, Marek; Smets, Frank 

###### **Working Paper** 

House Prices and the stance of Monetary Policy. 

ECB Working Paper, No. 891 

**Provided in Cooperation with:** European Central Bank (ECB) 

_Suggested Citation:_ Jarociński, Marek; Smets, Frank (2008) : House Prices and the stance of Monetary Policy., ECB Working Paper, No. 891, European Central Bank (ECB), Frankfurt a. M. 

This Version is available at: 

https://hdl.handle.net/10419/153325 

###### **Standard-Nutzungsbedingungen:** 

Die Dokumente auf EconStor dürfen zu eigenen wissenschaftlichen Zwecken und zum Privatgebrauch gespeichert und kopiert werden. 

Sie dürfen die Dokumente nicht für öffentliche oder kommerzielle Zwecke vervielfältigen, öffentlich ausstellen, öffentlich zugänglich machen, vertreiben oder anderweitig nutzen. 

Sofern die Verfasser die Dokumente unter Open-Content-Lizenzen (insbesondere CC-Lizenzen) zur Verfügung gestellt haben sollten, gelten abweichend von diesen Nutzungsbedingungen die in der dort genannten Lizenz gewährten Nutzungsrechte. 

###### **Terms of use:** 

_Documents in EconStor may be saved and copied for your personal and scholarly purposes._ 

_You are not to copy documents for public or commercial purposes, to exhibit the documents publicly, to make them publicly available on the internet, or to distribute or otherwise use the documents in public._ 

_If the documents have been made available under an Open Content Licence (especially Creative Commons Licences), you may exercise further usage rights as specified in the indicated licence._ 





**Working PaPer SerieS no 891 / aPril 2008** 



**HouSe PriceS and tHe Stance of monetary Policy** 

by Marek Jarociński and Frank Smets 









**WORKING PAPER SERIES NO 891 / APRIL 2008** 

# **HOUSE PRICES AND THE STANCE OF MONETARY POLICY**<sup>**1**</sup> 

by Marek Jarociński and Frank Smets<sup>2</sup> 





In 2008 all ECB publications feature a motif taken from the 10 banknote. 

This paper can be downloaded without charge from http://www.ecb.europa.eu or from the Social Science Research Network electronic library at http://ssrn.com/abstract_id=1120167. 



1 This paper has been prepared for the 32nd Annual Economic Policy Conference of the Federal Reserve Bank of St. Louis on “Monetary Policy under Uncertainty”. We thank our discussants, Bob King and Steve Cecchetti, for their insightful comments. The views expressed are solely our own and not necessarily those of the European Central Bank. 

2   Both authors: European Central Bank, Kaiserstrasse 29, 60311 Frankfurt am Main, Germany; 

e-mail: marek.jarocinski@ecb.int and frank.smets@ecb.int. 

###### **© European Central Bank, 2008** 

###### **Address** 

Kaiserstrasse 29 60311 Frankfurt am Main, Germany 

###### **Postal address** 

Postfach 16 03 19 60066 Frankfurt am Main, Germany 

###### **Telephone** 

+49 69 1344 0 

###### **Website** 

http://www.ecb.europa.eu 

###### **Fax** 

+49 69 1344 6000 

_All rights reserved._ 

_Any reproduction, publication and reprint in the form of a different publication, whether printed or produced electronically, in whole or in part, is permitted only with the explicit written authorisation of the ECB or the author(s)._ 

_The views expressed in this paper do not necessarily refl ect those of the European Central Bank._ 

_The statement of purpose for the ECB Working Paper Series is available from the ECB website, http://www.ecb. europa.eu/pub/scientifi c/wps/date/html/ index.en.html_ 

ISSN 1561-0810 (print) ISSN 1725-2806 (online) 

## **CONTENTS** 

|Abstract|**4**|
|---|---|
|Non-technical summary|**5**|
|1 Introduction|**7**|
|2 A Bayesian VAR with housing||
|for the US economy|**9**|
|3 Identifying housing demand, monetary policy<br>and term spread shocks|**13**|
|4 House prices and the monetary policy stance<br>in the US|**17**|
|4.1  MCI in a VAR: methodology and intuition|**18**|
|4.2  An application to house prices and the<br>policy stance in the US|**22**|
|5 Conclusions|**25**|
|Tables and f gures|**27**|
|References|**43**|
|Appendix|**45**|
|European Central Bank Working Paper Series|**46**|



ECB Working Paper Series No 891April 2008 3 

### Abstract 

This paper estimates a Bayesian VAR for the US economy which includes a housing sector and addresses the following questions. Can developments in the housing sector be explained on the basis of developments in real and nominal GDP and interest rates? What are the effects of housing demand shocks on the economy? How does monetary policy affect the housing market? What are the implications of house price developments for the stance of monetary policy? Regarding the latter question, we implement a version of a Monetary Conditions Index (MCI) due to Céspedes et al. (2006). 

Keywords: House prices, monetary conditions index, Bayesian VAR, monetary policy shock, conditional forecast. 

JEL Classification: E3-E4 

ECB 4 Working Paper Series No 891April 2008 

#### **Non-technical summary** 

The current financial turmoil, triggered by increasing defaults in the sub-prime mortgage market in the United States, has re-ignited the debate about the impact of the housing market on the economy at large and about how monetary policy should respond to booming house prices. Reviewing the role of housing investment in postWWII business cycles in the United States, Leamer (2007) concludes that “problems in residential investment have contributed 26% of the weakness in the economy in the year before the eight recessions” and suggests that in the most recent boom and bust period highly stimulative monetary policy by the Fed first contributed to a booming housing market and subsequently led to an abrupt contraction as the yield curve inverted. Similarly, using counterfactual simulations Taylor (2007) shows that the period of exceptionally low short-term interest rates in 2003 and 2004 (compared to a Taylor rule) may have substantially contributed to the boom in housing starts and may have led to an upward spiral of higher house prices, falling delinquency and foreclosure rates, more favourable credit ratings and financing conditions and higher demand for housing. As the short-term interest rates returned to normal levels, housing demand rapidly fell bringing down both construction and house price inflation. In contrast, Mishkin (2007) illustrates the limited ability of standard models to explain the most recent housing developments and emphasises the uncertainty associated with housing-related monetary transmission channels. He also warns against leaning against rapidly increasing house prices over and above their effects on the outlook for economic activity and inflation and suggests instead a pre-emptive easing of policy when a house price bubble bursts to avoid a large loss in economic activity. Even more recently, Kohn (2007) says “I suspect that, when studies are done with cooler reflection, the causes of the swing in house prices will be seen as less a consequence of monetary policy and more a result of the emotions of excessive optimism followed by fear experienced every so often in the marketplace through the ages. Low policy interest rates early in this decade helped feed the initial rise in house prices. However, the worst excesses in the market probably occurred when short-term interest rates were already well on their way to more normal levels, but longer-term rates were held down by a variety of forces.” 

In this paper we review the role of the housing market and monetary policy in US business cycles over the period 1987:1 to 2007:2 using an identified Bayesian Vector Autoregressive (BVAR) model. We use the BVAR to perform three exercises. First, we analyse the housing boom and bust in the new millennium using conditional forecasts by asking the question: Conditional on the estimated model, can we forecast the housing boom and bust based on observed real GDP, prices and short and longterm interest rate developments. This is a first attempt at understanding the sources of the swing in residential construction and house prices in the new millennium. In the benchmark VAR, our finding is that housing market developments can only partially be explained by nominal and real GDP developments. In particular, the strong rise in house prices in 2000 and the peak of house price increases in 2006 cannot be explained. Adding developments in the federal funds rate and the long-term interest rate to the information set helps forecasting the housing boom somewhat better. 

Second, we identify the effects of housing demand, monetary policy and term spread shocks on the economy. We find that the effects of housing demand and monetary policy shocks are broadly in line with the existing empirical literature. Housing demand shocks have significant effects on residential investment and house prices, 

ECB Working Paper Series No 891April 2008 5 

but overall these shocks appear to have had only a limited impact on the performance of the US economy in terms of aggregate growth and inflation. There is also evidence that monetary policy has significant effects on residential investment and house prices and that easy monetary policy designed to stave off perceived risks of deflation in 2002 to 2004 has contributed to the boom in the housing market in 2004 and 2005. However, again the impact on the overall economy was limited. A counterfactual simulation suggests that without those policy shocks inflation would have been about 25 basis points lower at the end of 2006. 

Finally, in the light of the above findings and following a methodology proposed by Céspedes et al. (2006), we explore the use of a Monetary Conditions Index (MCI), which includes the federal funds rate, the long-term interest rate spread and real house prices, to measure the stance of monetary policy. The idea of measuring monetary conditions by taking an appropriate weight of financial asset prices was pioneered by the Bank of Canada and the Reserve Bank of New Zealand in the 1990s. As both countries are small open economies, these central banks worried about how changes in the value of the exchange rate may affect the monetary policy stance. The idea was to construct a weighted index of the short-term interest rate and the exchange rate, where the weights reflected the relative impact of those monetary conditions on an intermediate or final target variable, such as the output gap, output growth or inflation. A number of authors have extended the idea of the MCI to other asset prices arguing that those asset prices may be equally or more important than the exchange rate. A prominent example is Goodhart and Hofmann (2007), who argue that real house prices should receive a significant weight because of its large impact on the economy and inflation in particular. In contrast to this literature, the crucial feature of the MCI methodology proposed by Céspedes et al. (2006) is that it takes into account that interest rates and house prices are endogenous variables that systematically respond to the state of the economy. As a result, their MCI can more naturally be interpreted as a measure of the monetary policy stance. Using the identified Bayesian VAR, we apply the methodology to the question whether the rise in house prices and the fall in long-term interest rates led to an implicit easing of monetary policy in the United States. We show that, in spite of the endogeneity of house prices to both the state of the economy and the level of interest rates, taking house prices into account may sharpen the inference on whether the stance of monetary policy has changed over time. Given the uncertainty about the sources of business cycle fluctuations and the impact of the various shocks (including housing demand shocks) on the economy, uncertainty regarding the stance of monetary policy remains high. Nevertheless, taking the development of house prices into account, there is some indication that monetary conditions may have been too loose in 2004 and were relatively tight in the summer of 2007. 

Various caveats of the methodology we use in this paper are worth mentioning. First, all the analysis presented in this paper is in-sample and ex-post. While this is helpful in trying to understand past developments, it clearly is not sufficient to prove its realtime usefulness. For that, we need to extend the analysis to a real-time context. Second, the statistical model we use to interpret the US housing market and business cycle is basically a linear one. It has been argued that costly asset price booms and busts are fundamentally of an asymmetric nature. Our linear methodology is not able to handle such non-linearities. Third, the robustness of the analysis to different identification schemes for the structural shocks needs to be further examined. We hope to shed some light on some of these issues in further analysis. 

ECB <mark>6</mark> Working Paper Series No 891April 2008 

##### **1. Introduction** 

The current financial turmoil, triggered by increasing defaults in the sub-prime mortgage market in the United States, has re-ignited the debate about the impact of the housing market on the economy at large and about how monetary policy should respond to booming house prices.<sup>1</sup> Reviewing the role of housing investment in post-WWII business cycles in the United States, Leamer (2007) concludes that “problems in residential investment have contributed 26% of the weakness in the economy in the year before the eight recessions” and suggests that in the most recent boom and bust period highly stimulative monetary policy by the Fed first contributed to a booming housing market and subsequently led to an abrupt contraction as the yield curve inverted. Similarly, using counterfactual simulations Taylor (2007) shows that the period of exceptionally low short-term interest rates in 2003 and 2004 (compared to a Taylor rule) may have substantially contributed to the boom in housing starts and may have led to an upward spiral of higher house prices, falling delinquency and foreclosure rates, more favourable credit ratings and financing conditions and higher demand for housing. As the short-term interest rates returned to normal levels, housing demand rapidly fell bringing down both construction and house price inflation. In contrast, Mishkin (2007) illustrates the limited ability of standard models to explain the most recent housing developments and emphasises the uncertainty associated with housing-related monetary transmission channels. He also warns against leaning against rapidly increasing house prices over and above their effects on the outlook for economic activity and inflation and suggests instead a pre-emptive easing of policy when a house price bubble bursts to avoid a large loss in economic activity. Even more recently, Kohn (2007) says “I suspect that, when studies are done with cooler reflection, the causes of the swing in house prices will be seen as less a consequence of monetary policy and more a result of the emotions of excessive optimism followed by fear experienced every so often in the marketplace through the ages. Low policy interest rates early in this decade helped feed the initial rise in house prices. However, the worst excesses in the market probably occurred when short-term interest rates were already well on their way to more normal levels, but longer-term rates were held down by a variety of forces.” 

In this paper we review the role of the housing market and monetary policy in US business cycles since the second half of the 1980s using an identified Bayesian Vector Autoregressive (BVAR) model. We focus on the last two decades for a number of reasons. First, following the “Great Inflation” of the 1970s, inflation measured by the GDP deflator has been relatively stable between 0 and 4% since the mid-1980s. As discussed by Clarida, Galí and Gertler (1999) and many others, this is likely to be partly due to a more systematic monetary policy 

> 1  See the annual economic symposium organised by the Kansas City Fed in Jackson Hole on 30 August 2007 on “Housing, housing finance and monetary policy”. A literature survey is presented in Mishkin (2007). 

ECB Working Paper Series No 891April 2008 <mark>7</mark> 

approach geared at maintaining price stability. Second, there is significant evidence that the volatility of real GDP growth has fallen since 1984 (e.g. Pérez-Quirós and McConnell, 2000). An important component of this fall in volatility has been a fall in the volatility of residential investment. Moreover, Mojon (2007) has shown that a major contribution to the “Great Moderation” has been a fall in the correlation between interest-rate sensitive consumer investment such as housing investment and the other components of GDP. This suggests that the role of housing investment in the business cycle may have changed since the deregulation of the mortgage market in the early 1980s. Indeed, Dynan et al. (2005) find that the interest rate sensitivity of residential investment has fallen over this period. 

We use the BVAR to perform three exercises. First, we analyse the housing boom and bust in the new millennium using conditional forecasts by asking the question: Conditional on the estimated model, can we forecast the housing boom and bust based on observed real GDP, prices and short and long-term interest rate developments. This is a first attempt at understanding the sources of the swing in residential construction and house prices in the new millennium. In the benchmark VAR, our finding is that housing market developments can only partially be explained by nominal and real GDP developments. In particular, the strong rise in house prices in 2000 and the peak of house price increases in 2006 cannot be explained. Adding the federal funds rate to the information set helps forecasting the housing boom. Interestingly, most of the variations in the term spread can also be explained on the basis of the short-term interest rate, but there is some evidence of a long-term interest rate conundrum in 2005 and 2006. As a result, observing the long-term interest rate also provides some additional information to explain the boom in house prices. 

Second, using a mixture of zero and sign restrictions, we identify the effects of a housing demand, monetary policy and term spread shock on the economy. We find that the effects of housing demand and monetary policy shocks are broadly in line with the existing empirical literature. We also analyse the role of those shocks in explaining the housing boom and its impact on the wider economy. We find that both housing market and monetary policy shocks explain a significant fraction of the construction and house price boom, but their effects on overall GDP growth and inflation are relatively contained. 

Finally, in the light of the above findings and following a methodology proposed by Céspedes et al. (2006), we explore the use of a Monetary Conditions Index (MCI), which includes the federal funds rate, the long-term interest rate spread and real house prices, to measure the stance of monetary policy. The idea of measuring monetary conditions by taking an appropriate weight of financial asset prices was pioneered by the Bank of Canada and the Reserve Bank of New Zealand in the 1990s. As both countries are small open economies, these central banks worried about how changes in the value of the exchange rate may affect 

ECB 8 Working Paper Series No 891April 2008 

the monetary policy stance.<sup>2</sup> The idea was to construct a weighted index of the short-term interest rate and the exchange rate, where the weights reflected the relative impact of those monetary conditions on an intermediate or final target variable, such as the output gap, output growth or inflation. A number of authors have extended the idea of the MCI to other asset prices arguing that those asset prices may be equally or more important than the exchange rate. A prominent example is Goodhart and Hofmann (2007), who argue that real house prices should receive a significant weight because of its large impact on the economy and inflation in particular. In contrast to this literature, the crucial feature of the MCI methodology proposed by Céspedes et al. (2006) is that it takes into account that interest rates and house prices are endogenous variables that systematically respond to the state of the economy. As a result, their MCI can more naturally be interpreted as a measure of the monetary policy stance. Using the identified Bayesian VAR, we apply the methodology to the question whether the rise in house prices and the fall in long-term interest rates led to an implicit easing of monetary policy in the United States. 

In the rest of this paper, we first present two specifications of the estimated BVAR. We then use both BVARs to calculate conditional forecasts of the housing market boom and bust in the new millennium. In Section 3, we identify housing demand, monetary policy and term spread shocks, and investigate their effect on the US economy. Finally, in Section 4 we develop the MCI and show using a simple analytical example how the methodology works and why it is important to take into account the endogeneity of short and long-term interest rates and house prices with respect to the state of the economy. We then use the estimated BVARs to address the question whether long-term interest rates and house prices play a significant role in measuring the stance of monetary policy. Finally, Section 5 contains some conclusions and discusses some of the shortcomings and areas for future research. 

#### **2. A Bayesian VAR with housing for the US economy** 

In this section, we present the results from estimating a 9-variable BVAR of order five for the US economy. In addition to standard variables such as real GDP, the GDP deflator, commodity prices, the federal funds rate and M2, we include real consumption, real residential investment, real house prices and the long-term interest rate spread. To measure house price inflation, we use the nation-wide Case-Shiller house price index, which limits our sample to start from 1987Q1 and it ends in 2007Q2. We estimate two specifications of the VAR. One is a traditional VAR in levels and uses a standard Minnesota prior. The other VAR is specified in growth rates and uses priors about the steady state (see Villani, 2008). 

> 2  See, for example, Freedman (1994, 1995ab) and Duguay (1994). 

ECB Working Paper Series No 891 April 2008 

9 

More specifically, in the level-VAR (L-VAR) the vector of endogenous variables is given by: 



In the differences-VAR (D-VAR) the vector of endogenous variables is instead given by: 



The main difference between the two specifications is related to the assumptions one makes about the steady state of the endogenous variables. The advantage of the D-VAR with a prior on the joint steady state, is that it guarantees that the growth rates are reasonable and mutually consistent in the long run, in spite of the short sample used in the estimation. The cost is that it discards important sample information contained in the level variables. As we discuss below, this may be the main reason behind the larger error bands around its impulse responses and conditional projections. Although the forecasts of the L-VAR match the data better at shorter horizons, the longer-run unconditional forecasts it produces make less sense from an economic point of view. As these considerations may matter for assessing the monetary policy stance, we report the findings using both specifications. 

In both cases the estimation is Bayesian. In the case of the D-VAR, it involves specifying a prior on the steady state of the VAR and a Minnesota prior on dynamic coefficients, as has been introduced in Villani (2008). The Minnesota prior uses standard settings and is the same as the one for the levels specification. The informative prior on the steady state of the VAR serves two roles: first, it regularizes inference on the steady states of variables. Without it, the posterior distribution of the steady states is ill specified, because of the singularity at the unit root. Second, and this is our innovation with respect to the approach of Villani (2008), we use economic theory to specify prior correlations between steady states. The steady state nominal interest rate is, by the Fisher equation, required to be the sum of the steady state inflation rate and the equilibrium real interest rate. The steady state real interest rate is, in turn, required to 

> 3  See the data appendix for the sources of the time series. 

ECB 10 Working Paper Series No 891April 2008 

be equal to the steady state output growth rate, plus a small error reflecting time preference and a risk premium. The steady state output and consumption growth rates are also correlated a priori, as we think of them as having a common steady state. 

The prior and posterior means and standard deviations of the steady states in the D-VAR are given in Table 1. 

##### {Insert Table 1} 

Figure 1 plots the data we use, as well as the estimated steady state values from the D-VAR. The steady state growth rate of real GDP is estimated to be close to 3 percent over the estimation period. Average GDP deflator inflation is somewhat above 2%. The steady state residential investment to GDP ratio is about 4.5%. During the new millennium construction boom the ratio rose by 1 percentage point peaking at 5.5% in 2005 before dropping below its long-term average in the 2<sup>nd</sup> quarter of 2007. Real house price developments mirror the developments in the construction sector. The estimated steady state real growth rate of house prices is 1.5 percent over the sample period. However, real house price changes were negative during the early 1990s recession. House price growth rates rose above average in the late 1990s and accelerated significantly above its estimated steady state reaching a maximum annual growth rate of more than 10 percent in 2005, before falling abruptly to negative growth rates in 2006 and 2007. Turning to interest rate developments, the estimated steady state nominal interest rate is around 5 percent. The estimated steady state term spread, i.e. the difference between the 10-year bond yield rate and the federal funds rate, is 1.4 percent. In the analysis below, we will mostly focus on the boom and bust period in the housing market starting in 2000. 

##### {Insert Figure 1} 

Using both BVAR specifications we then ask the following question: Can we explain developments in the housing market based on observed developments in real and nominal GDP and the short and long-term interest rates? To answer this question we make use of the conditional forecasting methodology developed by Doan, Litterman and Sims (1984) and Waggoner and Zha (1999). 

Figures 2a and 2b report the results for the D-VAR and the L-VAR respectively, focusing on the post-2000 period. Each figure shows the actual developments of the housing investment/GDP ratio (first column) and the annual real growth rate of house prices (second column), as well as the unconditional forecast and a forecast conditional on observed real and nominal GDP (first row), observed real and nominal GDP and the federal funds rate (second 

ECB Working Paper Series No 891April 2008 11 

row) and observed real and nominal GDP, the federal funds rate and the term spread (third row). Note that this is an in-sample analysis in the sense that the respective VARs are estimated over the full sample period. The idea behind increasing the information set is to see to what extent short and long-term interest rates provide information about developments in the housing market, in addition to the information already contained in real and nominal GDP. 

##### {Insert Figure 2a} 

A number of interesting observations can be made. First, as discussed above, the unconditional forecasts of residential investment and real house price growth are quite different in both VARs. The D-VAR projects the housing investment-GDP ratio to fluctuate mildly around its steady state, while the growth rate of house prices is projected to return quite quickly to its steady state of 1.5 percent from the relatively high level of growth of more than 5 percent at the end of 1999. The L-VAR instead captures some of the persistent in-sample fluctuations and projects a further rise in housing investment and house price growth before it returns to close to the sample mean in 2007. 

Second, based on the D-VAR in Figure 2a, neither GDP developments nor short or long-term interest rates can explain why real house prices continued to grow at rates above 5 percent following the slowdown of the economy in 2000 and 2001. Real and nominal GDP developments can explain an important fraction of the housing boom in 2002 and 2003, but they cannot account for the acceleration of house price growth to 10 percent in 2004 and 2005. The low level of short and long-term interest rates helps explaining the 2004 and 2005 boom. In particular towards the end of 2004 and in 2005, the unusually low level of long-term interest rates helps accounting for the acceleration in house prices. According to this model, there is some evidence of a “conundrum” in the sense that in this period long-term interest rates are lower than would be expected on the basis of observed short-term interest rates. The ability to better forecast the boom period comes, however, at the expense of larger unexplained undershooting of house prices and housing investment towards the end of the sample. Overall, these results suggest that the unusually low level of short and long-term interest rates may have contributed to the boom in US housing markets in the new millennium. 

##### {Insert Figure 2b} 

Third, the results based on the L-VAR in Figure 2b are, however, less clear. The part of the housing boom that cannot be explained by developments in real and nominal GDP is smaller. Moreover, adding short and long-term interest rates to the data set does not change the picture 

ECB 12 Working Paper Series No 891April 2008 

very significantly. These findings suggest that the results of the analysis partly depend on the assumed steady state behaviour of the housing market and interest rates. 

#### **3. Identifying housing demand, monetary policy and term spread shocks** 

In order to put a bit more structure on the analysis, in this section we identify housing demand, monetary policy and term spread shocks in order to analyse their effect on the economy. We use a mixture of a recursive identification scheme and sign restrictions. As usual, monetary policy shocks are identified by zero restrictions. They are assumed to affect economic activity and prices with a one quarter lag, but they may have an immediate impact on the term spread and the money stock. The housing demand shock is a shock that affects residential investment and house prices contemporaneously and in the same direction. Moreover, its immediate impact on output is roughly equal to the increase in residential investment (i.e. this shock has no contemporaneous effect on the other components of output taken together). We use sign restrictions to impose this identification scheme<sup>4</sup> . For simplicity we also assume that this shock only affects the GDP deflator with a lag. The shock that affects residential investment and house prices in opposite directions can be interpreted as a housing supply shock. However, it turns out that this shock explains only a small fraction of developments in the housing market, so that we will not explicitly discuss this shock. Figure 3 shows the estimated impulse responses together with a 68% posterior probability region for both VAR specifications. 

##### {Insert Figure 3} 

A number of observations are worth making. Overall, both VAR specifications give similar estimated impulse response functions. One difference worth noting is that relative to the L- VAR specification, the D-VAR (shaded impulse response functions) incorporates larger and more persistent effects on house prices and the GDP deflator. In what follows, we focus on the more precisely estimated L-VAR specification. According to Figure 3, a one standard deviation housing demand shock leads to a persistent rise in real house prices of about 0.75 percent and an increase in the residential investment share of about 0.05 percentage points. The impact on the overall economy is for real GDP to rise by about 0.10 percent after 4 quarters, while the effect on the GDP deflator takes longer (about 3 years) to peak at 0.08 percent above baseline. Note that the peak impact on prices in the D-VAR specification is quite a bit larger. The monetary policy response as captured by the federal funds rate is initially limited, but eventually the federal funds rate increases by about 20 basis points after 

> 4 For a discussion of VAR identification with sign restrictions see e.g. Uhlig (2005). 

ECB Working Paper Series No 891April 2008 13 

two years. The initial effect on the term spread is positive, reflecting a rise in long-term interest rates that anticipates the rise in inflation and short-term rates. 

In order to assess how reasonable these quantitative effects are, it is useful to compare them with other empirical results. One relevant literature is the empirical literature on the size of wealth/collateral effects of housing on consumption. As discussed in Muellbauer (2007) and Mishkin (2007), the empirical results are somewhat diverse, but some of the more robust findings suggest that the wealth effects from housing are approximately twice as large as those from stock prices. For example, Carroll, Otsuka and Slacalek (2006) estimate that the long-run marginal propensity to consume out of a dollar increase in housing is 9 cents, compared with 4 cents for non-housing wealth. Similarly, using cross-country time series, Slacalek (2007) finds that it is 7 cents out of a dollar. Overall, the long-run marginal propensities to consume out of housing wealth range from 5 to 17 percent, but a reasonable median estimate is probably around 7-8 percent compared to a 5 percent elasticity out of stock market wealth. How does this compare with the elasticities embedded in our estimated impulse response to a housing price shock? A one percent persistent increase in real house prices, leads to a 0.075 percent increase in real consumption after four quarters. Taking into account that the housing wealth-consumption ratio is around three in the United States, this suggest a marginal propensity to consumer of about one third of the long-run median estimate reported above. This lower effect on consumption may partly be explained by the fact that the increase in house prices is temporary. The mean elasticities embedded in the D-VAR are somewhat lower. 

We can also compare our estimated impulse response with the simulations using the FRB-US model reported in Mishkin (2007). Figure 5 of Mishkin (2007) reports that a 20 percent decline in real house prices under the estimated Taylor rule leads to a 1.5 percent deviation of real GDP from baseline in a version of the FRB/US with magnified channels, and to only a bit more than 0.5 percent in the benchmark version (which excludes an effect on real residential investment). Translating our results to a 20 percent real house price shock, suggests a multiplier of 2.5 percent. This is quite a bit higher than suggested by the FRB/US simulations, but this may be partly due to the strong immediate response of residential investment in our case. 

Finally, we can also compare the estimated impulse response functions of Figure 3 with the impulse responses to a positive housing preference shock in the estimated structural DSGE model of the US economy in Iacoviello and Neri (2007). They find that a one percent persistent increase in real house prices is associated with a 0.07 percent increase in consumption and a 3.6 percent increase in real residential investment. Whereas our estimated elasticity of real consumption is very similar, the elasticity of real residential investment is 

ECB 14 Working Paper Series No 891April 2008 

quite a bit lower at approximately 1.5 percent. It falls at the lower bound of the findings of Topel and Rosen (1988) who estimate that for every 1 percent increase in house prices lasting for two years, new construction increases on impact between 1.5 and 3.15 percent depending on the specifications. 

##### {Insert Figure 4 } 

Turning to the monetary policy shock, Figure 4 shows that a persistent 25 basis point tightening of the federal funds rate has the usual delayed negative effects on real GDP and the GDP deflator. The size of the real GDP response is quite small with a maximum mean negative effect of about 0.1 percent deviation from baseline after three years. This effect is even smaller and less significant in the D-VAR specification. The effect on residential investment is larger and quicker with a maximum negative effect of 0.03 percentage points of GDP (which would correspond to approximately 0.75 percent change) after about two years. Real house prices also immediately start falling and bottom out at 0.5 percent below baseline after two and half years. The housing market effects are somewhat stronger in the D-VAR specification. The higher sensitivity of residential investment to a monetary policy shock is consistent with the findings in the literature. For example, using identified VARs Erceg and Levin (2002) find that residential investment is about 10 times as responsive as consumption to a monetary policy shock. Our results are also comparable with those reported in Mishkin (2007) using the FRB/US model. In those simulations, a 100 basis point increase in the federal funds rate leads to a fall in real GDP of about 0.3 to 0.4 percent, although the lags (6 to 8 quarters) are somewhat smaller than those in our estimated BVAR. Also in these simulations, the effect on real residential investment is faster (within a year) and larger, but the estimated magnitude of those effects (between 1 and 1.25 percent) is quite a bit larger in our case (around 2.5 percent). Dynan et al. (2005) argue that the interest rate sensitivity of real residential investment has fallen since the second half of the 1980s (partly due to the deregulation of the mortgage market in the early 1980s). Our results suggest elasticities that are more in line with Erceg and Levin (2002) than with the FRB/US simulations. 

Our results can also be compared with the impulse responses to an adverse interest rate shock in Iacoviello and Neri (2007). They find that a 50 basis point temporary increase in the federal funds rate leads to a fall in real house prices of about 0.75 percent from baseline, compared to a delayed 1 percent fall in real house prices in our case (the delay is partly due to our recursive identification assumption). According to the estimates of Iacoviello and Neri (2007), real investment responds six times more strongly than real consumption and two times as strongly as real fixed investment. Overall, this is consistent with our results. However, the effects in Iacoviello and Neri (2007) are immediate, whereas they are delayed in our case. (See also Del Negro and Otrok, 2007) 

ECB Working Paper Series No 891April 2008 15 

In conclusion, the overall quantitative estimates of the effects of a monetary policy shock are in line with those found in the empirical literature. Similarly to our results, Goodhart and Hofmann (2007) find that a standard deviation shock to the real short-term interest rate has about the same quantitative effect on the output gap as a one-standard-deviation shock to the real house price gap. 

##### {Insert Figure 5} 

Finally, in the light of the discussion on the role of developments in long-term interest rates for the house price boom and bust in the United States and many other countries, it is also interesting to have a look at the effects of a term spread shock on the housing market. Figure 5 shows that a 20 basis point increase in the spread of long-term interest rates over the federal funds rate has a quite significant impact on residential investment, which drops by more than 0.014 percentage points of GDP (which corresponds to a 0.3 percent change) after about a year. Also real GDP falls with a bit more of a delay by about 0.075 percent after six quarters. Both the GDP deflator and real house prices fall, but only gradually. Overall, the size of the impulse responses is, however, small. 

##### {Insert Table 2a,b} 

Table 2a,b reports the contribution of the three shocks to the forecast error variance at different horizons in both specifications. Overall, the housing demand, monetary policy and term spread shocks account for only a small fraction of the total variance in real GDP and the GDP deflator. Monetary policy and housing demand shocks do, however, account for a significant fraction of the variance in the housing market. 

##### {Insert Figure 6a} 

This can be verified by looking at the contribution of the three shocks to the historical boom and bust episode since 2000, as depicted in Figure 6a-b. Each of the two columns reports respectively actual developments of the real residential investment/GDP ratio and the annual change in real house prices as well as the unconditional forecast as of 2000 and the counterfactual evolution if either of the three identified shocks are put to zero. The term spread shock does not have a visible impact on the housing market or the economy as a whole. The housing demand shock has a large positive impact on the housing market in 2001 and 2002 and again in 2004 and 2005. A negative demand shock also explains a large fraction of the fall in construction and house price growth from 2006 onward. These shocks have only negligible effects on overall GDP growth, but do seem to have pushed up inflation by 10 to 20 basis points over most of the post 2000 period. Loose monetary policy also seems to have 

ECB 16 Working Paper Series No 891April 2008 

contributed to the housing boom in 2004 and 2005. Without the relatively easy policy of late 2003 and early 2004 the boom in house price growth would have stayed well below the 10 percent growth rate in 2005. Easy monetary policy also has a noticeable, though small effect on GDP growth and inflation. 

The L-VAR results depicted in Figure 6b give similar indications, although they generally attribute an even larger role to the housing demand shocks. 

{Insert Figure 6b} 

##### **4. House prices and the monetary policy stance in the US** 

The idea of measuring monetary conditions by taking an appropriate weight of interest rates and asset prices was pioneered by the Bank of Canada and the Reserve Bank of New Zealand in the 1990s. As both countries are small open economies, these central banks worried about how changes in the value of the exchange rate may affect the monetary policy stance.<sup>5</sup> The idea was to construct a weighted index of the short-term interest rate and the exchange rate, where the weights reflected the relative impact of the exchange rate on an intermediate or final target variable, such as the output gap, output growth or inflation. A number of authors have extended the idea of the MCI to other asset prices arguing that those asset prices may be equally or more important than the exchange rate. One prominent example is Goodhart and Hofmann (2007), who argue that real house prices should receive a significant weight in a monetary conditions index because of its significant impact on the economy. For the US they argue that the relative weight of the short-term interest rate versus house prices should be of the order of 0.6 to 1.8. 

In the small literature that developed following the introduction of the MCI concept, a number of shortcomings have been highlighted.<sup>6</sup> One difficulty is that the lag structure of the impact of changes in the interest rate and the real house price on the economy may be different. As noted above, according to our estimates the effect of an interest rate shock on economic activity appears to take somewhat longer than the effect of a house price shock. In response, Batini and Turnbull (2002) (BT from now on) proposed a dynamic MCI that takes into account the different lag structure by weighting all current and past interest rates and asset prices with their estimated impulse responses. Another shortcoming of the standard MCI is that it is very difficult to interpret the MCI as an indicator of the monetary policy stance, because it does not take into account that changes in monetary conditions will typically be 

> 5  See, for example, Freedman (1994, 1995ab) and Duguay (1994). 

> 6  See, for example, Gerlach and Smets (2000). 

ECB Working Paper Series No 891April 2008 17 

endogenous to the state of the economy. The implicit assumption of the traditional MCI is that the monetary conditions are driven by exogenous shocks. This is clearly at odds with the identified VAR literature that suggests that most of the movements in monetary conditions are responses to the state of the economy. For example, changes in the federal funds rate will typically be a response to changing economic conditions and a changing outlook for price stability. An alternative way of expressing this drawback is that the implicit benchmark against which the MCI is measured does not depend on the likely source of the shocks in the economy. As a result, the benchmark in the standard MCI does not depend on the state of the economy, although clearly for given objectives the optimal MCI will vary with the shocks to the economy. Third, often the construction of the MCI does not take into account that the estimated weight of its various components is subject to uncertainty and estimation error. This uncertainty needs to be taken into account when interpreting the significance of apparent changes in monetary conditions. The methodology developed by Céspedes et al. (2006) (CLMM from now on) addresses each of those shortcomings. 

In this section, we apply a version of the monetary conditions index proposed by CLMM to derive a measure of the monetary policy stance that takes into account movements in the short and long-term interest rate and in real house prices. Using this index we try to answer the question whether the rise in house prices and the fall in long-term interest rates since 2000 led to an implicit easing of monetary policy in the United States. We use the Bayesian VARs estimated in the previous section to implement the methodology. In the next subsection, we define the MCI and use a simple analytical example to illustrate its logic. Next, we apply it to the US economy using the estimated BVAR. 

##### **4.1. MCI in a VAR: methodology and intuition** 

For the sake of example, let the economy be described by a stationary VAR of order one: 



> where _X t_ is the vector of non-policy variables, such as output and inflation, and<sup>_P_</sup> _t_<sup>is the</sup> vector of monetary policy and financial variables, such as in our case the short-term interest rate, the long-term interest rate spread and the real house price index. As in BT, a standard dynamic MCI with respect to a target variable j can then be defined as: _H_ (4) _MCI BTj_ , _t_ � _S j_ � _A_ 11 _s_ � 1 _A_ 12 ( _Pt_ � _s_ � _Pt_ * � _s_ ) _s_ � 1 

ECB <mark>18</mark> Working Paper Series No 891April 2008 

where _S j_ is a selection vector which selects the target variable j from the list of non-policy variables. Typically, the target variable in the construction of an MCI is either output growth or the output gap. This is based on the notion that financial and monetary conditions affect inflation primarily through their impact on spending and output. However, also inflation can be used as a target variable. In this paper, we will present results for both output growth and inflation as a target variable. The parameter H is the window over which lags of the monetary * conditions are considered.<sup>_P_</sup> _t_ � _s_<sup>is typically given by the steady state of the monetary</sup> conditions. In our case this would be the equilibrium nominal interest rate, the steady state term spread and steady state real house price growth rate. Alternatively, it could also be given by the monetary conditions that would have been expected as of period _t-H_ , if there had been no shocks from period _t-H_ to _t_ . Equation (2) illustrates that the standard MCI is a weighted average of the deviations of current and past policy variables from their steady state values, where the weights are determined by the partial elasticity of output with respect to a change in the policy variable. 

As discussed above, a problem with this notion of the MCI is that the policy variables are treated as exogenous and independent from the underlying economic conditions, or alternatively they are assumed to be driven by exogenous shocks. As a result, it is very problematic to interpret this index as a measure of the monetary policy stance. For example, it may easily be the case that the policy rate rises above its steady state value because of positive demand shocks. In that case monetary policy may either be too loose, neutral or too tight depending on whether the higher interest rate is able to offset the effect of the demand shocks only partially, fully or more than fully. Instead, the standard MCI will always indicate that monetary conditions have tightened. 

In contrast to the standard MCI, the alternative MCI proposed by CLMM does take into account the endogeneity of the policy instruments. In this case the MCI is defined as: 



The first part is the same as in the standard case (equation (4)), but in this case the effects on the target variable of the shocks that are most consistent with the observed path of monetary conditions are added. More specifically, the shocks are drawn from their distribution subject to the restriction that they generate the observed path of monetary conditions. Doan et al. (1984) and Waggoner and Zha (1999) show that the mean of this constrained distribution is given by: 

ECB Working Paper Series No 891April 2008 <mark>19</mark> 



_P_ where � _stacked_ is a vector of stacked shocks over the window of H periods, R is a stacked matrix of impulse response coefficients of the monetary conditions with respect to the shocks and _P_ � _E_ [ _P_ ] is the vector of correspondingly stacked forecast errors associated with the observed or assumed monetary conditions over the same window. 

In order to give the intuition for why the MCI by CLMM is a potentially much better indicator of the stance of monetary policy, it is useful to go through a simple static analytical example. 

Assume the economy is given by the following set of equations: 



where<sup>_y_</sup> _t_<sup>is the target variable, say output growth,</sup><sup>_s_</sup> _t_<sup>is the short-term policy rate,</sup><sup>_h_</sup> _t_<sup>is real</sup> house prices and there are three shocks: an output shock, a policy shock and a housing shock. Equation (7) reflects the dependence of output on the monetary conditions and an output shock. For convenience we have in this case assumed that there are no lags in the transmission process. Equation (8) is a monetary policy reaction function and equation (9) shows how the house price depends on the short rate and a shock. 

In this case the standard MCI (as in BT) is given by: 



and is independent of the monetary policy reaction function. If � 1 is negative and � 2 is positive, a rise in house prices will lead to an easing of monetary conditions unless the shortterm interest rate rises to exactly offset the effect of house prices on the target variable. 

Instead, the MCI of CLMM is given by: 



where we have assumed that all variables are measured as deviations from steady state. As in equation (6), the mean output shock needs to be consistent with the observed short-term interest rate and the real house price. 

ECB <mark>20</mark> Working Paper Series No 891April 2008 

Next we derive the expression of the last term in equation (11) as a function of the interest rate and house prices. From equation (6) and (7), it is clear that the relation between the interest rate conditions and the shocks is given by: 



As discussed above, given a joint standard normal distribution of the shocks, the mean of the shocks conditional on the observed interest rates is given by: 



where R is given in equation (12). 

> To simplify even further, assume that � 3<sup>�</sup> 0 , i.e. there is no policy shock. In that case, there is a one-to-one relationship between the shocks and the observed interest rate and house price, given by: 



As a result, in this case the MCI of CLMM is given by: 



Comparing expressions (15) and (10), it is obvious that the MCI’s of BT and CLMM have different weights on the short-term interest rate and the house price. The weights in the MCI of CLMM depend not only on the partial elasticities of output with respect to the short-term interest rate and the house price, but also on the coefficients in the policy reaction function and the elasticity of the house price with respect to the short-term interest rate. 

To see why the MCI of CLMM is a better indicator of the monetary policy stance, it is useful to investigate how the weights in (15) will depend on systematic policy behaviour. From equations (7) and (9), one can easily show that if the central bank targets output growth, the optimal interest rate reaction function is given by: 

ECB Working Paper Series No 891April 2008 <mark>21</mark> 



> If the interest rate elasticity of output is negative ( � 1<sup>�</sup> 0 ) and elasticity with respect to the house price positive ( � 2<sup>�</sup> 0 ), then a central bank trying to stabilise output will lean against positive output and house price shocks, where the size of the reaction coefficient will depend on the strength and the channels of the transmission mechanism. 

> Substituting the coefficients � 1 and � 2 in (15) by the coefficients in expression (16), it can be verified that in this case the MCI will be equal to zero. In other words, a policy that stabilises output will be seen as a neutral policy according to this index. In contrast, it is obvious that such a change in the policy reaction function will not affect the standard MCI. Instead assume that the central bank reacts optimally to the output shock as in equation (13), 

> but does not respond to the shock to the house price ( � 2<sup>�</sup> 0 ). In that case, it can be shown that the MCI of CLMM is given by: 



Also this result is very intuitive, when the central bank does not respond to house price shocks and a rise in house prices has a stimulative impact on output, then the MCI will indicate easy monetary conditions whenever there is a positive shock to the house price. 

This simple example makes it clear that in order to have a meaningful indicator of the monetary policy stance, it is important to realise that the monetary conditions are conditional on the shocks hitting the economy. 

##### **4.2. An application to house prices and the policy stance in the US** 

Obviously, the static example is too simple to bring to the data. In reality, monetary conditions will have lagged effects on output and inflation and the lag patterns may differ across the various components as shown in Section 3. In this section, we use the two specifications of the estimated BVAR to calculate an MCI for the US economy. Consistent with the MCI literature, we use respectively real GDP growth and inflation as the target variables. Moreover, in order to take the lags in the transmission process of monetary policy that we documented in Section 3 into account, we assume that in the case of real GDP growth the target variable is expected annual GDP growth one year ahead, whereas in the case of inflation it is expected annual inflation two years ahead. Figures 7a-b show the results of this exercise. In order to illustrate the impact of the conditionality of the MCI, we also compare 

ECB <mark>22</mark> Working Paper Series No 891April 2008 

the CLMM measure (which conditions on the full set of shocks) with the BT measure. In the latter case, we assume that the observed interest rates and house prices are only driven by the exogenous shocks identified in Section 3. 

##### {Insert Figure 7a} 

Figures 7a-b show the estimated MCIs together with their 68 percent probability regions for one-year ahead annual output growth (left column) and two-years ahead annual inflation (right column) as target variables, using the federal funds rate (first row), the federal funds rate and the term spread (second row) and the federal funds rate, the term spread and the real house price (third row) as indicators of monetary conditions. Figure 7a use the D-VAR, whereas Figure 7b uses the L-VAR. The shaded area refers to the BT measure. The MCIs shown are basically the difference between the conditional forecast of the target variable based on the actual path of the monetary conditions and the one based on an equilibrium path of the monetary conditions given by the unconditional forecast. 

##### {Insert Figure 7b} 

A few observations are worth making on the basis of Figure 7a. First, overall the indications that come from the MCI based on expected output growth and expected inflation are similar. Financial conditions were relatively tight in 2000-2001, gradually became relatively loose in the period 2002-2005, before turning tight again during 2006. Second, the uncertainty surrounding the MCI is very high. Based on standard significance levels, the monetary conditions were not significantly different from neutral during the whole period. Third, taking house prices into account (third row of Figure 7a) does seem to matter for measuring the monetary policy stance. More specifically buoyant growth in house prices in 2004 and 2005 suggests that monetary policy was relatively loose in this period, whereas it turned tight in 2007. During the housing boom, easy monetary conditions implied two-year ahead annual inflation that was more than 0.5 percentage points above its steady state. Most recently, tight conditions imply expected inflation almost 0.5 percentage points below the target. These results differ marginally when the L-VAR specification is used (compare Figure 7b with 7a). 

A comparison of the shaded areas (showing the 68 posterior probability region for the BT MCI) with the areas enclosed by dotted lines (showing the 68 percent posterior probability region for the CLMM MCI) reveals that, although the broad messages of the estimated MCIs are similar, conditioning on exogenous shocks only, gives less precise estimates. This is partly the result of the fact that the exogenous shocks contribute only to a limited degree to the forecast variance of output and inflation. As a result, the effects are also less precisely estimated.  The point estimates are similar, which suggests that the developments in 2002- 

ECB Working Paper Series No 891April 2008 <mark>23</mark> 

2005 were strongly influenced by the policy and housing demand shocks, and not so much by responses to other shocks. 

As is clear from the discussion in section 4.1, the MCIs are a weighted average of current and past levels of the short-term interest rate, the term spread (or the long-term interest rate) and real house price growth. In order to get an idea of the relative importance of the three components, Table 3 gives the sum of the weights on current and up to 8 quarter lagged values of each of three components in the MCI. As in Figure 7a, this is done for an MCI calculated on the basis of the short-term interest rate, the short and long-term interest rate and the short and long-term interest rate and real house price growth respectively and taking both annual GDP growth and inflation as target variables. A few observations are worth making. First, taking only the short-term interest rate as an indicator of the policy stance, it is clear that on average an observed increase of the interest rate above its steady state value indicates a restrictive policy stance both with respect to GDP growth and inflation. This is, in particular, the case when the short-term interest rate is assumed to be driven by the three identified exogenous shocks. However, if the full conditional nature of the nominal interest rate is taken into account (as in CLMM), this is less the case and more so for inflation than for growth. The reason is that due to the central bank’s reaction function the short-term interest rate is likely to increase in response to shocks that drive up future output growth and inflation. In that case a rise in interest rates may even suggest an easing of the policy stance if interest rates do not rise enough to offset the pick-up in growth and inflation. To the extent that changes in the nominal interest rate reflect higher inflation and inflation expectations, this argument will be particularly strong when expected inflation is the target. 

Taking the long-term interest rate into account slightly changes the picture. Keeping the longterm interest rate constant, observing a 1 percentage point increase in the short-term interest rate for 8 quarters signals a fall in GDP growth of about 20 basis points over the next year and a fall in inflation of somewhat less over the next two years. In contrast, keeping the short-term rate constant, a rise in the long-term interest rate by 1 percentage point signals lax monetary policy, as it predicts a rise in both GDP growth (9 basis points) and inflation (16 basis points) above steady state. Finally, the right-hand panel of Table 3 shows the weights when also real house prices are included in the MCI. Including house prices does not very much affect the weights on the interest rates. The upper rows show that the weight on real house price growth is close to zero when the target variable is GDP growth. This is indeed also reflected in the fact that the actual MCI does not change very much in Figure 7a. However, when annual inflation in two years time is the target variable, there is a significant weight on house prices. A 5 percentage point rise in the growth rate of real house prices for two years signals a rise in annual inflation of 30 to 40 basis points in two years time. According to the weights such a 

ECB <mark>24</mark> Working Paper Series No 891April 2008 

rise in house prices would call for a substantially higher short-term rate (of about 2 percentage points) in order to have neutral monetary conditions. 

##### **5. Conclusions** 

In this paper, we have examined the role of housing investment and house prices in US business cycles since the second half of the 1980s using an identified Bayesian VAR. We found that housing demand shocks have significant effects on residential investment and house prices, but overall these shocks have had only a limited impact on the performance of the US economy in terms of aggregate growth and inflation in line with the empirical literature. There is also evidence that monetary policy has significant effects on residential investment and house prices and that easy monetary policy designed to stave off perceived risks of deflation in 2002 to 2004 has contributed to the boom in the housing market in 2004 and 2005. However, again the impact on the overall economy was limited. A counterfactual simulation suggests that without those policy shocks inflation would have been about 25 basis points lower at the end of 2006. 

In order to examine the impact of house prices on monetary conditions, we implement a methodology proposed by Céspedes et al. (2006). This methodology consists of calculating the forecast of a target variable (expected GDP growth or expected inflation) conditional on the observed path of monetary conditions including the short-term interest rates, the term spread and house prices. We show that, in spite of the endogeneity of house prices to both the state of the economy and the level of interest rates, taking house prices into account may sharpen the inference on whether the stance of monetary policy has changed over time. Given the uncertainty about the sources of business cycle fluctuations and the impact of the various shocks (including housing demand shocks) on the economy, uncertainty regarding the stance of monetary policy remains high. Nevertheless, taking the development of house prices into account, there is some indication that monetary conditions may have been too loose in 2004 and were relatively tight in the summer of 2007. 

Various caveats of the methodology we use in this paper are worth mentioning. First, all the analysis presented in this paper is in-sample and ex-post. While this is helpful in trying to understand past developments, it clearly is not sufficient to prove its real-time usefulness. For that, we need to extend the analysis to a real-time context. Second, the statistical model we use to interpret the US housing market and business cycle is basically a linear one. It has been argued that costly asset price booms and busts are fundamentally of an asymmetric nature. Our linear methodology is not able to handle such non-linearities. Third, the robustness of the 

ECB Working Paper Series No 891April 2008 <mark>25</mark> 

analysis to different identification schemes for the structural shocks needs to be further examined. We hope to shed some light on some of these issues in further analysis. 

ECB <mark>26</mark> Working Paper Series No 891April 2008 

**Table 1** 

Prior and posterior means and standard deviations of the steady states in the D-VAR 

|Variable|Real<br>GDP<br>growth|Real<br>Consumption<br>growth|GDP<br>deflator<br>inflation|Housing<br>investment<br>/GDP|House<br>price<br>growth|Commodity<br>price<br>growth|Federal<br>funds<br>rate|Term<br>spread|Money<br>growth|
|---|---|---|---|---|---|---|---|---|---|
|Prior||||||||||
|Mean|2.50|2.50|2.00|4.50|0.00|2.00|4.50|1.00|4.50|
|Std|0.50|0.71|0.20|1.00|2.00|2.00|0.62|1.00|1.00|
|Posterior||||||||||
|Mean|2.96|3.23|2.21|4.51|1.52|2.00|5.05|1.42|4.35|
|Std|0.22|0.22|0.15|0.07|1.08|1.54|0.34|0.24|0.51|



ECB Working Paper Series No 891April 2008 <mark>27</mark> 

##### **Table 2a** 

Shares of housing demand, monetary policy and term spread shocks in variance 

decomposition, D-VAR 

||Horizon:|<br>0|3|11|23|
|---|---|---|---|---|---|
|Variable|Shock|||||
|Output|Housing|0.016|0.034|0.052|0.062|
||Monetary Policy|0.000|0.004|0.021|0.039|
||Termpremium|0.000|0.003|0.015|0.028|
|Consumption|Housing|0.005|0.018|0.033|0.055|
||Monetary Policy|0.000|0.003|0.015|0.029|
||Termpremium|0.000|0.005|0.034|0.063|
|Prices|Housing|0.002|0.013|0.120|0.166|
||Monetary Policy|0.000|0.003|0.014|0.037|
||Termpremium|0.000|0.006|0.034|0.046|
|House inv.|Housing|0.521|0.579|0.382|0.291|
||Monetary Policy|0.000|0.015|0.175|0.136|
||Termpremium|0.000|0.005|0.023|0.062|
|House pr.|Housing|0.535|0.554|0.410|0.242|
||Monetary Policy|0.000|0.010|0.068|0.083|
||Termpremium|0.000|0.002|0.021|0.060|
|Commodity pr.|Housing|0.027|0.028|0.041|0.085|
||Monetary Policy|0.000|0.012|0.167|0.222|
||Termpremium|0.000|0.004|0.018|0.055|
|Short intr.|Housing|0.037|0.061|0.165|0.178|
||Monetary Policy|0.752|0.496|0.192|0.166|
||Termpremium|0.000|0.023|0.076|0.088|
|Spread|Housing|0.090|0.050|0.177|0.186|
||Monetary Policy|0.223|0.303|0.214|0.206|
||Termpremium|0.336|0.245|0.146|0.134|
|Money|Housing|0.060|0.044|0.062|0.099|
||Monetary Policy|0.204|0.141|0.044|0.045|
||Termpremium|0.013|0.042|0.129|0.135|



Note: The reported shares are averages over the posterior distribution, and relate to the (log) level variables. 

ECB <mark>28</mark> Working Paper Series No 891April 2008 

##### **Table 2b** 

Shares of housing demand, monetary policy and term spread shocks in variance decomposition, L-VAR 

|Variable|Horizon:<br>Shock|<br>0|3|11|23|
|---|---|---|---|---|---|
|Output|Housing|0.019|0.049|0.073|0.106|
||Monetary Policy|0.000|0.005|0.036|0.052|
||Termpremium|0.000|0.005|0.026|0.026|
|Consumption|Housing|0.005|0.021|0.051|0.093|
||Monetary Policy|0.000|0.008|0.040|0.051|
||Termpremium|0.000|0.005|0.021|0.024|
|Prices|Housing|0.002|0.017|0.127|0.153|
||Monetary Policy|0.000|0.005|0.038|0.114|
||Termpremium|0.000|0.005|0.012|0.016|
|House inv.|Housing|0.582|0.554|0.357|0.351|
||Monetary Policy|0.000|0.027|0.124|0.125|
||Termpremium|0.000|0.015|0.021|0.019|
|House pr.|Housing|0.586|0.610|0.360|0.229|
||Monetary Policy|0.000|0.011|0.087|0.066|
||Termpremium|0.000|0.003|0.010|0.014|
|Commodity pr.|Housing|0.030|0.044|0.154|0.149|
||Monetary Policy|0.000|0.008|0.072|0.100|
||Termpremium|0.000|0.005|0.012|0.015|
|Short intr.|Housing|0.032|0.055|0.217|0.211|
||Monetary Policy|0.709|0.453|0.206|0.177|
||Termpremium|0.000|0.007|0.018|0.018|
|Spread|Housing|0.072|0.048|0.129|0.150|
||Monetary Policy|0.230|0.281|0.163|0.152|
||Termpremium|0.355|0.215|0.114|0.085|
|Money|Housing|0.040|0.036|0.053|0.066|
||Monetary Policy|0.257|0.237|0.089|0.060|
||Termpremium|0.015|0.020|0.021|0.025|



Note: The reported shares are averages over the posterior distribution. 

ECB Working Paper Series No 891April 2008 <mark>29</mark> 

**Table 3** 

8-quarter sum of MCI weights (D-VAR) 

||MCIi|MCIi,s||MCIi,s,hp|||
|---|---|---|---|---|---|---|
||Short<br>rate|Short<br>rate|Long<br>rate|Short<br>rate|Long<br>rate|House<br>prices|
|CLMM-GDP|-0.162|-0.201|0.090|-0.198|0.102|0.000|
|BT-GDP|-0.198|-0.190|0.074|-0.194|0.102|0.003|
|CLMM-DP|-0.046|-0.142|0.162|-0.148|0.250|0.056|
|BT-DP|-0.154|-0.182|0.168|-0.087|0.180|0.083|



ECB <mark>30</mark> Working Paper Series No 891April 2008 

##### **Figure 1** 

Data used (as in the D-VAR) and their estimated steady state value 



<!-- Start of picture text -->
output consumption prices<br> 8  7  5<br> 6  4.5<br> 6<br> 5  4<br> 4<br> 4  3.5<br> 3<br> 3<br> 2  2<br> 2.5<br> 1<br> 0  2<br>data  0<br>mean -1  1.5<br>-2 16 pctile84 pctile -2  1<br>-4 -3  0.5<br>1990 1995 2000 2005 1990 1995 2000 2005 1990 1995 2000 2005<br>housing investment housing prices commodity prices<br> 5.6  15  50<br> 5.4  40<br> 10<br> 5.2  30<br> 5<br> 5  20<br> 4.8<br> 10<br> 4.6  0<br> 0<br> 4.4<br>-5 -10<br> 4.2<br> 4 -20<br>-10<br> 3.8 -30<br> 3.6 -15 -40<br>1990 1995 2000 2005 1990 1995 2000 2005 1990 1995 2000 2005<br>interest rate spread money<br> 10  4  12<br> 9  3.5  10<br> 8  3<br> 8<br> 7  2.5<br> 6  2  6<br> 5  1.5  4<br> 4  1  2<br> 3  0.5<br> 0<br> 2  0<br> 1 -0.5 -2<br> 0 -1 -4<br>1990 1995 2000 2005 1990 1995 2000 2005 1990 1995 2000 2005<br><!-- End of picture text -->

ECB Working Paper Series No 891April 2008 <mark>31</mark> 

##### **Figure 2a** 

Housing investment to GDP ratio and annual house price growth rate (1995-2007) Actual data and unconditional and conditional forecasts from the D-VAR. 



<!-- Start of picture text -->
(hi/y)*100 conditional on y,p log(hp/hp(-4)) conditional on y,p<br> 5.6<br>cond.fcast mean<br> 5.4 16 pctile<br> 5.2 84 pctile  10<br>uncond.fcast mean<br> 5 actual<br> 5<br> 4.8<br> 4.6<br> 0<br> 4.4<br> 4.2<br>-5<br> 4<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br>(hi/y)*100 conditional on y,p,int log(hp/hp(-4)) conditional on y,p,int<br> 5.6<br> 5.4<br> 10<br> 5.2<br> 5<br> 5<br> 4.8<br> 4.6<br> 0<br> 4.4<br> 4.2<br>-5<br> 4<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br>(hi/y)*100 conditional on y,p,int,spread log(hp/hp(-4)) conditional on y,p,int,spread<br> 5.6<br> 5.4<br> 10<br> 5.2<br> 5<br> 5<br> 4.8<br> 4.6<br> 0<br> 4.4<br> 4.2<br>-5<br> 4<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br><!-- End of picture text -->

ECB <mark>32</mark> Working Paper Series No 891April 2008 

##### **Figure 2b** 

Housing investment to GDP ratio and annual house price growth rate (1995-2007) Actual data and unconditional and conditional forecasts from the L-VAR. 



<!-- Start of picture text -->
(hi/y)*100 conditional on y,p log(hp/hp(-4)) conditional on y,p<br> 5.6<br>cond.fcast mean<br> 5.4 16 pctile<br> 5.2 84 pctile  10<br>uncond.fcast mean<br> 5 actual<br> 5<br> 4.8<br> 4.6<br> 0<br> 4.4<br> 4.2<br>-5<br> 4<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br>(hi/y)*100 conditional on y,p,int log(hp/hp(-4)) conditional on y,p,int<br> 5.6<br> 5.4<br> 10<br> 5.2<br> 5<br> 5<br> 4.8<br> 4.6<br> 0<br> 4.4<br> 4.2<br>-5<br> 4<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br>(hi/y)*100 conditional on y,p,int,spread log(hp/hp(-4)) conditional on y,p,int,spread<br> 5.6<br> 5.4<br> 10<br> 5.2<br> 5<br> 5<br> 4.8<br> 4.6<br> 0<br> 4.4<br> 4.2<br>-5<br> 4<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br><!-- End of picture text -->

ECB Working Paper Series No 891April 2008 <mark>33</mark> 

##### **Figure 3** 

Impulse responses to a housing demand shock (D-VAR and L-VAR) 



<!-- Start of picture text -->
output consumption prices<br>0.40<br>0.30 DVAR 68pct 0.30<br>LVAR mean 0.30<br>0.20 LVAR 68pct 0.20<br>0.20<br>0.10 0.10<br>0.10<br>0.00 0.00<br>0.00<br>-0.10 -0.10<br>-0.10<br>-0.20 -0.20<br>-0.20<br>-0.30 -0.30<br>-0.30<br> 0  5  10  15  20  0  5  10  15  20  0  5  10  15  20<br>housing investment housing prices commodity prices<br>0.10 3.00<br>2.00 2.00<br>0.05 1.00<br>1.00<br>0.00<br>-1.00<br>0.00 0.00<br>-2.00<br>-3.00<br>-1.00<br>-0.05 -4.00<br>-2.00 -5.00<br>-0.10 -6.00<br> 0  5  10  15  20  0  5  10  15  20  0  5  10  15  20<br>interest rate spread money<br>0.50 1.00<br>0.30<br>0.40<br>0.20<br>0.30 0.50<br>0.20 0.10<br>0.10 0.00 0.00<br>0.00 -0.10<br>-0.10 -0.50<br>-0.20<br>-0.20<br>-0.30<br>-0.30 -1.00<br> 0  5  10  15  20  0  5  10  15  20  0  5  10  15  20<br><!-- End of picture text -->

ECB <mark>34</mark> Working Paper Series No 891April 2008 

##### **Figure 4** 

Impulse responses to a monetary policy shock 



<!-- Start of picture text -->
output consumption prices<br>0.40<br>0.30 DVAR 68pct 0.30<br>LVAR mean 0.30<br>0.20 LVAR 68pct 0.20<br>0.20<br>0.10 0.10<br>0.10<br>0.00 0.00<br>0.00<br>-0.10 -0.10<br>-0.10<br>-0.20 -0.20<br>-0.20<br>-0.30 -0.30<br>-0.30<br> 0  5  10  15  20  0  5  10  15  20  0  5  10  15  20<br>housing investment housing prices commodity prices<br>0.10 3.00<br>2.00 2.00<br>0.05 1.00<br>1.00<br>0.00<br>-1.00<br>0.00 0.00<br>-2.00<br>-3.00<br>-1.00<br>-0.05 -4.00<br>-2.00 -5.00<br>-0.10 -6.00<br> 0  5  10  15  20  0  5  10  15  20  0  5  10  15  20<br>interest rate spread money<br>0.50 1.00<br>0.30<br>0.40<br>0.20<br>0.30 0.50<br>0.20 0.10<br>0.10 0.00 0.00<br>0.00 -0.10<br>-0.10 -0.50<br>-0.20<br>-0.20<br>-0.30<br>-0.30 -1.00<br> 0  5  10  15  20  0  5  10  15  20  0  5  10  15  20<br><!-- End of picture text -->

ECB Working Paper Series No 891April 2008 <mark>35</mark> 

##### **Figure 5** 

Impulse response to a term-premium shock 



<!-- Start of picture text -->
output consumption prices<br>0.40<br>0.30 DVAR 68pct 0.30<br>LVAR mean 0.30<br>0.20 LVAR 68pct 0.20<br>0.20<br>0.10 0.10<br>0.10<br>0.00 0.00<br>0.00<br>-0.10 -0.10<br>-0.10<br>-0.20 -0.20<br>-0.20<br>-0.30 -0.30<br>-0.30<br> 0  5  10  15  20  0  5  10  15  20  0  5  10  15  20<br>housing investment housing prices commodity prices<br>0.10 3.00<br>2.00 2.00<br>0.05 1.00<br>1.00<br>0.00<br>-1.00<br>0.00 0.00<br>-2.00<br>-3.00<br>-1.00<br>-0.05 -4.00<br>-2.00 -5.00<br>-0.10 -6.00<br> 0  5  10  15  20  0  5  10  15  20  0  5  10  15  20<br>interest rate spread money<br>0.50 1.00<br>0.30<br>0.40<br>0.20<br>0.30 0.50<br>0.20 0.10<br>0.10 0.00 0.00<br>0.00 -0.10<br>-0.10 -0.50<br>-0.20<br>-0.20<br>-0.30<br>-0.30 -1.00<br> 0  5  10  15  20  0  5  10  15  20  0  5  10  15  20<br><!-- End of picture text -->

ECB <mark>36</mark> Working Paper Series No 891April 2008 

##### **Figure 6a** 

Counterfactuals when shutting down each of the identified shocks – D-VAR 

##### **Panel 1** 



<!-- Start of picture text -->
(hi/y)*100 with all shocks except housing shock log(hp/hp(-4)) with all shocks except housing shock<br> 5.6<br>counterfactual<br> 5.4 unconditional fcast<br>actual  10<br> 5.2<br> 5  5<br> 4.8<br> 4.6  0<br> 4.4<br>-5<br> 4.2<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br>(hi/y)*100 feeding all shocks except monetary policy log(hp/hp(-4)) feeding all shocks except monetary policy<br> 5.6<br> 5.4<br> 10<br> 5.2<br> 5  5<br> 4.8<br> 4.6  0<br> 4.4<br>-5<br> 4.2<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br>(hi/y)*100 feeding all shocks except spread log(hp/hp(-4)) feeding all shocks except spread<br> 5.6<br> 5.4<br> 10<br> 5.2<br> 5  5<br> 4.8<br> 4.6  0<br> 4.4<br>-5<br> 4.2<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br><!-- End of picture text -->

ECB Working Paper Series No 891April 2008 <mark>37</mark> 

##### **Panel 2** 



<!-- Start of picture text -->
gdp with shocks except housing shock p with shocks except housing shock int feeding shocks except housing shock<br> 5  3.5  7<br> 4.5 counterfactual<br>unconditional fcast  6<br> 4 actual  3<br> 3.5  5<br> 3<br> 2.5  2.5  4<br> 2  2  3<br> 1.5<br> 1  2<br> 0.5  1.5<br> 1<br> 0<br>-0.5  1  0<br>97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01<br>gdp feeding shocks except monetary policy p feeding shocks except monetary policyint feeding shocks except monetary policy<br> 5  3.5  7<br> 4.5<br> 6<br> 4  3<br> 3.5  5<br> 3  2.5  4<br> 2.5<br> 2  2  3<br> 1.5  2<br> 1  1.5<br> 1<br> 0.5<br> 0  1  0<br>97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01<br>gdp feeding shocks except spread p feeding shocks except spread int feeding shocks except spread<br> 5  3.5  7<br> 4.5<br> 6<br> 4  3<br> 3.5  5<br> 3  2.5  4<br> 2.5<br> 2  2  3<br> 1.5  2<br> 1  1.5<br> 1<br> 0.5<br> 0  1  0<br>97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01<br><!-- End of picture text -->

ECB <mark>38</mark> Working Paper Series No 891April 2008 

##### **Figure 6b** 

Counterfactuals when shutting down each of the identified shocks – L-VAR 

##### **Panel 1** 



<!-- Start of picture text -->
(hi/y)*100 with all shocks except housing shock log(hp/hp(-4)) with all shocks except housing shock<br> 5.6<br>counterfactual<br> 5.4 unconditional fcast<br>actual  10<br> 5.2<br> 5  5<br> 4.8<br> 4.6  0<br> 4.4<br>-5<br> 4.2<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br>(hi/y)*100 feeding all shocks except monetary policy log(hp/hp(-4)) feeding all shocks except monetary policy<br> 5.6<br> 5.4<br> 10<br> 5.2<br> 5  5<br> 4.8<br> 4.6  0<br> 4.4<br>-5<br> 4.2<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br>(hi/y)*100 feeding all shocks except spread log(hp/hp(-4)) feeding all shocks except spread<br> 5.6<br> 5.4<br> 10<br> 5.2<br> 5  5<br> 4.8<br> 4.6  0<br> 4.4<br>-5<br> 4.2<br>96-01 98-01 00-01 02-01 04-01 06-01 96-01 98-01 00-01 02-01 04-01 06-01<br><!-- End of picture text -->

ECB Working Paper Series No 891April 2008 <mark>39</mark> 

##### **Panel 2** 



<!-- Start of picture text -->
gdp with shocks except housing shock p with shocks except housing shock int feeding shocks except housing shock<br> 5  3.5  7<br>counterfactual<br> 4.5<br>unconditional fcast  6<br> 4 actual  3<br> 3.5  5<br> 3  2.5  4<br> 2.5<br> 2  2  3<br> 1.5  2<br> 1  1.5<br> 1<br> 0.5<br> 0  1  0<br>97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01<br>gdp feeding shocks except monetary policy p feeding shocks except monetary policyint feeding shocks except monetary policy<br> 5  3.5  7<br> 4.5<br> 6<br> 4  3<br> 3.5  5<br> 3  2.5  4<br> 2.5<br> 2  2  3<br> 1.5  2<br> 1  1.5<br> 1<br> 0.5<br> 0  1  0<br>97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01<br>gdp feeding shocks except spread p feeding shocks except spread int feeding shocks except spread<br> 5  3.5  7<br> 4.5<br> 6<br> 4  3<br> 3.5  5<br> 3  2.5  4<br> 2.5<br> 2  2  3<br> 1.5  2<br> 1  1.5<br> 1<br> 0.5<br> 0  1  0<br>97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01 97-01 00-01 03-01 06-01<br><!-- End of picture text -->

ECB <mark>40</mark> Working Paper Series No 891April 2008 

##### **Figure 7a** 

##### MCI’s of CLMM and BT – D-VAR 



<!-- Start of picture text -->
output conditional on short term interest rate prices conditional on short term interest rate<br> 3  3<br>BT 68pct<br> 2 CLMM mean  2<br>CLMM 68pct<br> 1  1<br> 0  0<br>-1 -1<br>-2 -2<br>-3 -3<br>00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01 00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01<br>output conditional on short term interest, spread prices conditional on short term interest, spread<br> 3  3<br> 2  2<br> 1  1<br> 0  0<br>-1 -1<br>-2 -2<br>-3 -3<br>00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01 00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01<br>output conditional on interest, spread, housing prices prices conditional on interest, spread, housing prices<br> 3  3<br> 2  2<br> 1  1<br> 0  0<br>-1 -1<br>-2 -2<br>-3 -3<br>00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01 00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01<br><!-- End of picture text -->

ECB Working Paper Series No 891April 2008 <mark>41</mark> 



<!-- Start of picture text -->
Figure 7b<br><!-- End of picture text -->



<!-- Start of picture text -->
MCI’s of CLMM and BT – L-VAR<br>output conditional on short term interest rate prices conditional on short term interest rate<br> 3  3<br>BT 68pct<br> 2 CLMM mean  2<br>CLMM 68pct<br> 1  1<br> 0  0<br>-1 -1<br>-2 -2<br>-3 -3<br>00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01 00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01<br>output conditional on short term interest, spread prices conditional on short term interest, spread<br> 3  3<br> 2  2<br> 1  1<br> 0  0<br>-1 -1<br>-2 -2<br>-3 -3<br>00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01 00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01<br>output conditional on interest, spread, housing prices prices conditional on interest, spread, housing prices<br> 3  3<br> 2  2<br> 1  1<br> 0  0<br>-1 -1<br>-2 -2<br>-3 -3<br>00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01 00-01 01-01 02-01 03-01 04-01 05-01 06-01 07-01<br><!-- End of picture text -->

ECB <mark>42</mark> Working Paper Series No 891April 2008 

##### **References** 

Batini, N. and Turnbull, K. (2002). A dynamic monetary conditions index for the UK. _Journal of Policy Modeling_ , 24:257–281. 

Carroll, C. D., Otsuka, M., and Slacalek, J. (2006). How large is the housing wealth effect? a new approach. NBER Working Papers 12746, National Bureau of Economic Research, Inc. 

- Céspedes, B., E. Lima, A. Maka and M. Mendonça (2006), “Conditional forecasts and the measurement of monetary policy stance in Brazil”, mimeo. 

- Clarida, R., Galí, J., and Gertler, M. (1999). The science of monetary policy: A new Keynesian perspective. _Journal of Economic Literature_ , 37(4):1661–1707. 

- Del Negro, M. and Otrok, C. (2007). 99 Luftballons: Monetary policy and the house price boom across U.S. states. _Journal of Monetary Economics_ , 54(7):1962– 1985. 

- Doan, T., Litterman, R., and Sims, C. (1984). Forecasting and conditional projection using realistic prior distributions. _Econometric Reviews_ , 3(1):1–100. 

Duguay, P. (1994), "Empirical Evidence on the Strength of the Monetary Transmission Mechanism in Canada - an Aggregate Approach", _Journal of Monetary Economics_ , 33, pp. 39-61. 

- Dynan, K., D. Elmendorf and D. Sichel (2006), “Can financial innovation help to explain the reduced volatility of economic activity?”, _Journal of Monetary Economics_ 53(2006), 123-150. 

- Erceg, C. and Levin, A. (2002). Optimal monetary policy with durable and non-durable goods. FRB International Finance Discussion Paper No. 748. 

- Freedman, C. (1994), "The Use of Indicators and the Monetary Conditions Index in Canada", in T.J.T. Balino and C. Cottarelli (eds.), _Frameworks for Monetary Stability - Policy Issues and Country Experiences_ , IMF, Washington, pp. 458476. 

- Freedman, C. (1995a). The Canadian experience with targets for reducing and controlling inflation. In Leiderman, L. and Svensson, L., editors, _Inflation Targets_ . CEPR, London. 

- Freedman, C. (1995b), "The Role of Monetary Conditions and the Monetary Conditions Index in the Conduct of Policy," _Bank of Canada Review_ , Autumn, pp. 53-59. 

- Gerlach, S. and F. Smets (2000), “MCIs and monetary policy”, _European Economic Review_ , 44:9, 1677-1700, October 2000. 

Goodhart, C. and B. Hofmann (2007), “Financial Conditions Indices”, Chapter 3 in House prices and the macro economy: Implications for banking and price stability, Oxford University Press. 

ECB Working Paper Series No 891April 2008 <mark>43</mark> 

Iacoviello, M. and Neri, S. (2007). The role of housing collateral in an estimated twosector model of the U.S. economy. Boston College Working Papers in Economics 659, Boston College Department of Economics. 

- Kohn, D. (2007), “Success and failure of monetary policy since the 1950s”, Speech at “Monetary policy over fifty years”, a conference to mark the fiftieth anniversary of the Deutsche Bundesbank, Frankfurt, Germany. 

- Leamer, E. E. (2007). Housing and the business cycle. paper presented at the Annual Economic Symposium organized by the Kansas City Fed in Jackson Hole. 

- McConnell, M. M. and Pérez-Quirós, G. (2000). Output fluctuations in the United States: What has changed since the early 1980’s? _American Economic Review_ , 90(5):1464–1476. 

- Mishkin, F. (2007), “Housing and the monetary transmission mechanism”, paper presented at the Annual Economic Symposium organised by the Kansas City Fed in Jackson Hole. 

- Mojon, B. (2007), “Monetary policy, output composition and the Great Moderation”, Federal Reserve Bank of Chicago WP 2007-07. 

- Muellbauer, J. (2007), “Housing and consumer behaviour”, paper presented at the Annual Economic Symposium organised by the Kansas City Fed in Jackson Hole. 

- Slacalek, J. (2006), “What drives personal consumption? The role of housing and financial wealth”, mimeo, November 2006. 

- Topel, R. H. and Rosen, S. (1988). Housing investment in the United States. _Journal of Political Economy_ , 96(4):718–40. 

- Taylor, J. B. (2007). Housing and monetary policy. panel intervention in the Annual Economic Symposium organized by the Kansas City Fed in Jackson Hole. 

- Uhlig, H. (2005). What are the effects of monetary policy on output? results from an agnostic identification procedure. _Journal of Monetary Economics_ , 52(2):381– 419. 

- Villani, Mattias (2008). Steady State Priors for Vector Autoregressions, Journal of Applied Econometrics, forthcoming 

- Waggoner, D. F. and Zha, T. (1999). Conditional forecasts in dynamic multivariate models. _The Review of Economics and Statistics_ , 81(4):639–651. 

ECB <mark>44</mark> Working Paper Series No 891April 2008 

##### Appendix A: Data and sources 

**Real GDP** : Real Gross Domestic Product, 3 Decimal (GDPC96), Seasonally Adjusted Annual Rate, Quarterly, Billions of Chained 2000 Dollars, source: FRED, after BEA. 

**Real Consumption** : Real Personal Consumption Expenditures (PCECC96), Seasonally Adjusted Annual Rate, Quarterly, Billions of Chained 2000 Dollars, source: FRED, after BEA. 

**GDP deflator** : Gross Domestic Product: Implicit Price Deflator (GDPDEF), Seasonally Adjusted, Quarterly, Index 2000=100, source: FRED, after BEA 

**Fed Funds Rate** : Effective Federal Funds Rate (FEDFUNDS), Monthly, 

Percent, Averages of Daily Figures, source: FRED, after Board of Governors of the Federal Reserve System; averaged over 3 months of the quarter 

**Long-term interest rate** : 10-Year Treasury Constant Maturity Rate (GS10), Monthly, Percent, Averages of business days, source: FRED after Board of Governors of the Federal Reserve System; averaged over 3 months of the quarter 

**S&P/Case-Shiller U.S. National Home Price Index** , quarterly, based on repeated sales, <u>http://www.standardandpoors.com; available since 1987</u> 

**M2** : M2 Money Stock (M2NS), Not Seasonally Adjusted, Monthly, Billions of Dollars, source: FRED, after Board of Governors of the Federal Reserve System, averaged over 3 months of the quarter 

**Real Private Residential Fixed Investment** , 3 Decimal, (PRFIC96), U.S. Department of Commerce: Bureau of Economic Analysis, Seasonally Adjusted Annual Rate, Quarterly, Billions of Chained 2000 Dollars, source: FRED 

**Commodity price index: Dow Jones Spot Average** , quarter average, source: Global Financial Data (www.globalfinancialdata.com) acronym _DJSD. 

In the VAR we use the interest rate spread, computed as the difference between the long interest rate and the federal funds rate, house prices deflated relative to the GDP deflator, and the ratio of the real private residential fixed investment to real GDP. All the variables, except for the short term interest rate, spread and housing investment, enter either in log levels, or log differences (annualized), depending on the VAR specification indicated. 

ECB Working Paper Series No 891April 2008 <mark>45</mark> 

###### **European Central Bank Working Paper Series** 

For a complete list of Working Papers published by the ECB, please visit the ECB’s website (http://www.ecb.europa.eu). 

- 848 “Economic growth and budgetary components: a panel assessment for the EU” by A. Afonso and J. González Alegre, January 2008. 

- 849 “Government size, composition, volatility and economic growth” by A. Afonso and D. Furceri, January 2008. 

- 850  “Statistical tests and estimators of the rank of a matrix and their applications in econometric modelling” by G. Camba-Méndez and G. Kapetanios, January 2008. 

- 851 “Investigating inflation persistence across monetary regimes” by L. Benati, January 2008. 

- 852 “Determinants of economic growth: will data tell?” by A. Ciccone and M. Jarociński, January 2008. 

- 853 “The cyclical behavior of equilibrium unemployment and vacancies revisited” by M. Hagedorn and I. Manovskii, January 2008. 

- 854 “How do firms adjust their wage bill in Belgium? A decomposition along the intensive and extensive margins” by C. Fuss, January 2008. 

- 855 “Assessing the factors behind oil price changes” by S. Dées, A. Gasteuil, R. K. Kaufmann and M. Mann, January 2008. 

- 856 “Markups in the euro area and the US over the period 1981-2004: a comparison of 50 sectors” by R. Christopoulou and P. Vermeulen, January 2008. 

- 857 “Housing and equity wealth effects of Italian households” by C. Grant and T. Peltonen, January 2008. 

- 858 “International transmission and monetary policy cooperation” by G. Coenen, G. Lombardo, F. Smets and R. Straub, January 2008. 

- 859 “Assessing the compensation for volatility risk implicit in interest rate derivatives” by F. Fornari, January 2008. 

- 860 “Oil shocks and endogenous markups: results from an estimated euro area DSGE model” by M. Sánchez, January 2008. 

- 861 “Income distribution determinants and public spending efficiency” by A. Afonso, L. Schuknecht and V. Tanzi, January 2008. 

- 862 “Stock market volatility and learning” by K. Adam, A. Marcet and J. P. Nicolini, February 2008. 

- 863 “Population ageing and public pension reforms in a small open economy” by C. Nickel, P. Rother and A. Theophilopoulou, February 2008. 

- 864 “Macroeconomic rates of return of public and private investment: crowding-in and crowdingout effects” by A. Afonso and M. St. Aubyn, February 2008. 

- 865 “Explaining the Great Moderation: it is not the shocks” by D. Giannone, M. Lenza and L. Reichlin, February 2008. 

- 866 “VAR analysis and the Great Moderation” by L. Benati and P. Surico, February 2008. 

- 867 “Do monetary indicators lead euro area inflation?” by B. Hofmann, February 2008. 

ECB <mark>46</mark> Working Paper Series No 891April 2008 

- 868 “Purdah: on the rationale for central bank silence around policy meetings” by M. Ehrmann and M. Fratzscher, February 2008. 

- 869 “The reserve fulfilment path of euro area commercial banks: empirical testing using panel data” by N. Cassola, February 2008. 

- 870 “Risk management in action: robust monetary policy rules under structured uncertainty” by P. Levine, P. McAdam, J. Pearlman and R. Pierse, February 2008. 

- 871 “The impact of capital flows on domestic investment in transition economies” by E. Mileva, February 2008. 

- 872 “Why do Europeans work part-time? A cross-country panel analysis” by H. Buddelmeyer, G. Mourre and M. Ward, February 2008. 

- 873 “The Feldstein-Horioka fact” by D. Giannone and M. Lenza, February 2008. 

- 874 “How arbitrage-free is the Nelson-Siegel model?” by L. Coroneo, K. Nyholm and R. Vidova-Koleva, February 2008. 

- 875 “Global macro-financial shocks and expected default frequencies in the euro area” by O. Castrén, S. Dées and F. Zaher, February 2008. 

- 876 “Are sectoral stock prices useful for predicting euro area GDP?” by M. Andersson and A. D’Agostino, February 2008. 

- 877 “What are the effects of fiscal policy shocks? A VAR-based comparative analysis” by D. Caldara and C. Kamps, March 2008. 

- 878 “Nominal and real interest rates during an optimal disinflation in New Keynesian models” by M. Hagedorn, March 2008. 

- 879 “Government risk premiums in the bond market: EMU and Canada” by L. Schuknecht, J. von Hagen and G. Wolswijk, March 2008. 

- 880 “On policy interactions among nations: when do cooperation and commitment matter?” by H. Kempf and L. von Thadden, March 2008. 

- 881 “Imperfect predictability and mutual fund dynamics: how managers use predictors in changing systematic risk” by G. Amisano and R. Savona, March 2008. 

- 882 “Forecasting world trade: direct versus “bottom-up” approaches” by M. Burgert and S. Dées, March 2008. 

- 883 “Assessing the benefits of international portfolio diversification in bonds and stocks” by R. A. De Santis and L. Sarno, March 2008. 

- 884 “A quantitative perspective on optimal monetary policy cooperation between the US and the euro area” by S. Adjemian, M. Darracq Pariès and F. Smets, March 2008. 

- 885 “Impact of bank competition on the interest rate pass-through in the euro area” by M. van Leuvensteijn, C. Kok Sørensen, J. A. Bikker and A. A. R. J. M. van Rixtel, March 2008. 

- 886 “International evidence on sticky consumption growth” by C. D. Carroll, J. Slacalek and M. Sommer, March 2008. 

ECB Working Paper Series No 891April 2008 <mark>47</mark> 

- 887 “Labor supply after transition: evidence from the Czech Republic” by A. Bičáková, J. Slacalek and M. Slavík, March 2008. 

- 888 “House prices, money, credit and the macroeconomy” by C. Goodhart and B. Hofmann, April 2008. 

- 889 “Credit and the natural rate of interest” by F. De Fiore and O. Tristani, April 2008. 

- 890 “Globalisation, domestic inflation and global output gaps: evidence from the euro area” by A. Calza, April 2008. 

- 891 “House prices and the stance of monetary policy” by M. Jarociński and F. Smets, April 2008. 

ECB <mark>48</mark> Working Paper Series No 891April 2008 

