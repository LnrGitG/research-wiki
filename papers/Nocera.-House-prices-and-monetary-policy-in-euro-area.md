---
title: **Working Paper Series**
type: paper
source_pdf: raw/papers/Nocera. House prices and monetary policy in euro area.pdf
converted: 2026-07-26
---



# **Working Paper Series** 

> Andrea Nocera, Moreno Roma House prices and monetary policy in the euro area: evidence from structural VARs 



<!-- Start of picture text -->
No 2073 / June 2017<br><!-- End of picture text -->

**Disclaimer:** This paper should not be reported as representing the views of the European Central Bank (ECB). The views expressed are those of the authors and do not necessarily reflect those of the ECB. 

#### **Abstract** 

We use a Bayesian stochastic search variable selection structural VAR model to investigate the heterogeneous impact of housing demand shocks on the macro-economy and the role of house prices in the monetary policy transmission, across euro area countries. A novel set of identification restrictions, which combines zero and sign restrictions, is proposed. By exploiting the cross-sectional dimension of our data, we explore the differences in the propagation channels of house prices and monetary policy and the challenges they pose in the process of real and nominal convergence in the Eurozone. Among the main results, we find a comparatively stronger housing wealth effect on consumption in Ireland and Spain. We provide new evidence in support of the financial accelerator hypothesis, showing that house prices play an important role in the availability of loans. A significant and highly heterogeneous effect of monetary policy on house price dynamics is also documented. 

#### **JEL Classification:** C22, E21, E31, E44, E52. 

**Keywords:** Bayesian Vector Autoregression, house prices, identified VARs, monetary policy, policy counterfactuals. 

ECB Working Paper 2073, June 2017 

1 

## **Non-technical Summary** 

We use a structural Bayesian vector autoregression model for seven euro-area countries (Belgium, France, Germany, Ireland, Italy, the Netherlands, and Spain) for the period 1980:Q12014:Q4 to provide a systematic structural analysis of the impacts of housing demand shocks on economic activity and the role of house prices in the monetary policy transmission. We focus on a country by country analysis, given the idiosyncratic characteristics of the housing market in the euro area, which suggest that pooling or aggregating may lead to biased inference (Pesaran and Smith, 1995) and misleading policy recommendations. At the same time, we exploit the cross-sectional dimension of our data, to compare and quantify the degree of heterogeneity of the effects of housing demand and monetary policy shocks across euro area members. In doing so we fill a gap in the literature, largely focused on the US, the UK and the euro area as a whole. 

Identification of housing demand and monetary policy shocks is achieved using a novel set of zero and sign restrictions. The priors are selected using a Bayesian stochastic search approach to allow for shrinkage of the VAR coefficients while selecting restrictions that are supported by the data itself. This in turn allows appropriate finite sample inference and exploits in full the intrinsic cross-country heterogeneity typical of the housing market. 

Estimation results confirm that the effects of housing demand and monetary policy shocks differ widely across countries. We highlight some of the main results. First, we find a modest housing wealth effect in the euro area, with the exception of Ireland and Spain, where a housing demand shock, in terms of a 1% increase in real house prices, is associated with a significant increase of real private consumption of 0.15%. The historical decompositions corroborate the results of the impulse response analysis. The cumulative effects of housing demand shocks on real private consumption are muted in most countries but Ireland and Spain. In both countries, housing demand shocks significantly contributed to the surge of consumption growth during the specific housing boom episode observed in the sample and to the subsequent decline during the following recession. 

Second, we document a strong response of real loans to housing demand shocks. The effects of housing shocks on loans are significant across all countries, while the degree of heterogeneity is less pronounced. Similarly, housing demand shocks play an important role in explaining loans forecast error variance (FEV) across all countries under investigation, with an average contribution of slightly less than 40%. These findings support the “financial accelerator” hypothesis, according to which increases in the value of the collateral improve households borrowing capacity. Moreover, the cumulative effects of housing demand shocks to real loans growth are sizeable across all countries under investigation. 

Finally, we corroborate the strong role of house prices in the euro area monetary policy transmission and document high heterogeneity in the impact of monetary policy shocks on 

ECB Working Paper 2073, June 2017 

2 

house price fluctuations. A 25 basis points contractionary monetary policy shock significantly reduces real house prices between 0.4% (in Germany) and 3% (in Spain), on average by 1.6%. Being aware of such heterogeneity is crucial to address possible imbalances across countries and to design policies to mitigate risks deriving from residential property markets which have assumed a key role in the macroprudential toolkit (ECB (2016)). Monetary policy shocks account on average for around 25% of the FEV of real house price growth. Historical decompositions highlight a strong contribution of monetary shocks to real house price growth. A substantial increase in house prices would have occurred in Ireland and Spain between 2001 and 2006 even if all the other structural shocks but monetary policy had been turned off. 

ECB Working Paper 2073, June 2017 

3 

## **1 Introduction** 

In the light of the recent global financial crisis, it is crucially important to understand the role that house prices played in the past and the linkages between housing, monetary policy and macroeconomic activity in general, in order to detect future housing imbalances and to improve financial stability. As a result, the literature on housing in macroeconomics has grown very rapidly in recent years.<sup>1</sup> Nevertheless, most of the current studies focus on the aggregate euro area, the UK and the US.<sup>2</sup> Yet, little is known about the effects of house prices in each euro area member states. A notable exception is Giuliodori (2005) although this work only covers the pre-EMU period.<sup>3</sup> The first contribution of this paper is to fill this gap. We use a structural Bayesian vector autoregression model for seven euro-area countries (Belgium, France, Germany, Ireland, Italy, the Netherlands, and Spain) for the period 1980:Q1-2014:Q4. We focus on a country by country analysis, given the idiosyncratic characteristics of the housing market in the euro area (ECB, 2003) which suggest that pooling or aggregating may lead to biased inference (Pesaran and Smith, 1995) and misleading policy recommendations. Adopting a novel set of identification restrictions which combines zero and sign restrictions, based on the algorithm developed by Arias et al. (2014), we provide a systematic structural analysis of the effects of housing demand shocks on economic activity and the role of house prices in the monetary transmission mechanism across euro area countries. The combination of zero and sign restrictions allows us to distinguish between a housing demand shock and an aggregate demand shock. Disentangling these two shocks would be less than obvious if we were to use only sign restrictions. The priors are selected using the Bayesian stochastic search variable selection (SSVS) approach developed by George, Sun and Ni (2008). This method allows for shrinkage of the VAR coefficients (to overcome the over-parameterization problem) while selecting restrictions that are supported by the data itself. This in turn allows appropriate finite sample inference and exploits in full the intrinsic cross-country heterogeneity typical of the housing market. 

Second, using to the extent possible a dataset composed of comparable data sources, sample periods, and by employing the same econometric methodology for each country, we exploit the cross-sectional dimension of our data to quantify the degree of heterogeneity of the impact of housing demand shocks on the macro-economy and the role of house prices in 

> 1An excellent survey is provided by Piazzesi and Schneider (2016). 

> 2Notably, Iacoviello (2005), Iacoviello and Neri (2010), Jarocinski and Smets (2008), and Mishkin (2007) for the US. Musso et al. (2011) compare the US with the (aggregated) euro area. 

> 3Using a recursively identified VAR, the author focuses on the role of house prices in the monetary transmission and provides some evidence on their effects on household consumption while leaving aside their role in driving other important variables such as GDP, inflation, lending rates and most importantly the supply of credit. 

ECB Working Paper 2073, June 2017 

4 

the transmission of monetary policy across Eurozone members.<sup>4</sup> In fact, the current literature lacks of such comparative studies, especially with respect to the role of housing wealth on economic activity. The investigation of heterogeneity in the euro area housing markets is clearly relevant from a policy perspective. Given the ongoing recovery in house prices, it is fundamental to ask what are the implications for the broader macro-economy and to investigate how the heterogenous impacts of house prices across countries can amplify the existing economic divergences across Eurozone members.<sup>5</sup> House prices in the euro area appear to be currently supported by several factors: favourable financing conditions, the enfolding recovery in growth and employment and a low yield environment which makes housing investment relative attractive compared to alternative asset classes (ECB, 2015). A protracted increase in house prices is therefore foreseeable and its macroeconomic implications need to be carefully assessed by policy makers. Moreover, considering the numerous interactions - of a real and financial nature - characterizing the housing market (Wachter, 2015), it is inevitable that the two aforementioned questions - how housing demand shocks affect the macro-economy and how monetary policy affects house prices - are intrinsically interrelated. In this context, house prices, like other asset prices, represent a potentially important component in monetary policy transmission, to the extent that changes in interest rates and other (non-standard) monetary policy measures affect house prices, thereby influencing economic activity and private consumption. 

With regard to the transmission of monetary policy, Calza et al. (2013) conduct an analysis similar to our investigation. Accounting for heterogeneity in the estimation, the authors classify 19 advanced economies into two groups according to the degree of development of mortgage markets and the type of interest rate structure, to examine whether the national mortgage markets’ institutional characteristics influence the effects of monetary shocks. Identification of the latter is achieved via Cholesky decomposition. Differently from them, we ask whether a common monetary policy could amplify divergences in house prices fluctuations among the Eurozone members when reacting to area wide aggregates such as inflation and economic activity. As noted in Bini Smaghi (2011), given its primary objective of maintaining price stability in the euro area, the ECB has “no choice but to take a euro area perspective”. Therefore, since its policy decisions aim at price stability at the area-wide level and “cannot be tailored to the specific needs of a single Member State”, it is important to quantify and compare the different effects of monetary shocks on house price dynamics across euro area countries, regardless of the degree of development of national mortgage markets, which according to Cardarelli et al. (2008) is rather low in all countries under study, 

> 4A description of the data sources is presented in Appendix B.1. 

> 5The focus is on the implications in terms of real GDP, real private consumption, inflation and credit developments. 

ECB Working Paper 2073, June 2017 

5 

with the exception of the Netherlands.<sup>6</sup> Being aware of such heterogeneity is essential when addressing real and financial imbalances at the country level by means of macroprudential policies.<sup>7</sup> 

Estimation results confirm that the effects of housing demand and monetary policy shocks differ widely across the countries under investigation. We find evidence of the existence of a housing wealth effect in the euro area, although with a certain degree of heterogeneity in the response of household consumption to house price increases. While there is a broad consensus on the housing wealth effect in the U.S. (e.g. Iacoviello and Neri, 2007), and the U.K. (e.g. Campbell and Cocco, 2007), it is argued that such an effect is relatively modest in the euro area (ECB, 2009). Although this is true for many countries under investigation, the same cannot be said for Ireland and Spain, where we show that an increase in real house prices has a positive and statistically significant impact on real private consumption. Both countries have recently experienced a boom-bust pattern in house prices. This finding supports the view (e.g. Shiller, 2005) that house price booms play an important role in boosting confidence, which in turn stimulate consumption. The historical decomposition analysis corroborates the importance of housing demand shocks in driving consumption, especially in Ireland and Spain. In both countries, in the absence of housing demand shocks, the growth rates of real private consumption would have been lower than the actual rates between 2002 and 2007, and larger between 2008 and 2013. To illustrate, in Ireland, the cumulative effect of housing demand shocks on consumption is equal to 0.79% up to 2006 and to -1.16% at the end of 2011. In Spain, it is equal to 0.5% up to 1995 and 2004, and to -0.66% in 2012. Housing demand shocks also play an important role in explaining variation in the supply of credit, confirming the “financial accelerator” hypothesis, according to which changes in the collateral affect borrowing capacity (Bernanke et al. (1996) and Almeida et al. (2006)). The impact of housing demand shocks on loans is less heterogeneous than the effect on consumption. Furthermore, we corroborate the strong role of house prices in the monetary policy transmission for the euro area while documenting high heterogeneity in the impact of monetary policy shocks on euro area countries’ house price fluctuations. Historical decompositions highlight a strong contribution of monetary shocks to real house price growth. A substantial increase in house prices would have occurred in Ireland and Spain between 2001 and 2006 even if all the other structural shocks but monetary policy had been turned off. The remainder of the paper is organised as follows. Section 2 presents the data used and 

> 6For instance, if we were to classify the countries examined according to their Loan-to-Value ratio following Calza et al. (2013), all countries would belong to the “low development” group but Belgium and the Netherlands. If we were to use mortgage equity withdrawal, only the Netherlands would belong to the “high development” group. More heterogeneity is found in terms of the type of interest rate structure, with Italy and Spain being characterized by variable rates, although this is a recent development. 

> 7On this topic, see for example Schoenmaker (2014) and Hartmann (2015). 

ECB Working Paper 2073, June 2017 

6 

some stylized facts. In Section 3 we provide a brief review of the literature on housing in macroeconomics. Section 4 describes the methodology used. Section 5 presents results of the structural VAR analysis. In particular, we highlight the strategy used to identify the structural shocks and describe the main findings from impulse response analysis, the forecast error variance decomposition, and historical decomposition. Finally, we conclude. 

## **2 Data and Stylized Facts** 

**Some Stylized Facts.** The house price cycle has turned the corner in the euro area. The annual rate of change in euro area house prices started to increase in mid-2013 and turned mildly positive since the second half of 2014, subsequently reaching a post crisis high at the beginning of 2016. This aggregate trend follows heterogeneous developments across euro area countries. Large downward adjustments in real house prices took place in Spain and Ireland since the beginning of 2008, where prices declined around 40% from the peaks reached before the financial crisis. Sizable declines in excess of 20% were also experienced in the same period in the Netherlands and Italy, while real house prices were broadly stable in Belgium and increased notably in Germany by 27%. Indeed, the building and subsequent – correction of house price imbalances typical of a boom-bust pattern characterising the housing market - renders the observed aggregate recovery relatively muted and characterised by a differentiated pace across countries. In this context, exploring how house price dynamics affect the macroeconomy and how monetary policy influence house prices appear of particular interest. To further grasp the importance of housing for the macro-economy and put things into perspective, housing wealth in the euro area represents, on average, 37% of households’ net worth. In turn, at the end of 2014, real estate-related loans to households and nonfinancial firms in the euro area accounted for nearly 57% of euro area banks’ total loans to the non-financial private sector and more than half of euro area GDP (ECB, (2015)). 

**Data.** A detailed description of the database used in the descriptive and econometric analysis is provided in Appendix B.1. In Appendix B.2, we provide charts which depict the variables of interest for the seven euro area countries examined (Belgium (BE), France (FR), Germany (DE), Ireland (IE), Italy (IT), Spain (ES), and the Netherlands (NL)) and, for illustrative purposes, the euro area. The variables are: real house prices, consumer price inflation, real GDP, real loans to households, lending rates and monetary policy rates. All variables are shown as an index level, except for the interest rates which are in percentage terms. From a first graphical inspection of the data some interesting points emerge. First, the heterogeneity in real house price dynamics across the panel of euro area countries is broadly matched by qualitatively similar dynamics in real loans to households, generally suggesting a high degree 

ECB Working Paper 2073, June 2017 

7 

of co-movement between the two variables. In particular, countries experiencing boom-bust episodes in house prices (such as Ireland and Spain) have also undergone sharp increases in credit to households before the financial crisis followed by reversals after the crisis. This also holds to some extent for Italy and the Netherlands. At the same time, sustained house price dynamics in France and Belgium, especially in the latter part of the sample period, have been accompanied by continued growth in loans to households. On the contrary, in the case of Germany, declining or subdued house price dynamics for a large part of the sample period have been matched by a modest increase in loans to households. Second, a certain degree of co-movement between real house prices and economic activity in terms of real GDP is also evident, in particular in the case of Ireland, Spain and the Netherlands. The findings described above are confirmed when looking at cross correlations. The alignment between real house prices and the business cycle (in terms of real GDP) is highest in terms of maximum correlation in Spain, Ireland and the Netherlands and it is found at broadly coincident level. The maximum correlation between annual real house prices and real loans to households is found in the case of France, Ireland, Spain (around 70%) and Belgium and the Netherlands (around 50-60%). In the case of the Netherlands, Spain and Belgium real house price growth tends to slightly lead annual growth in real loans to households. Third, consumer prices were characterised by a much lower degree of cross-country heterogeneity compared to house prices, as well by more moderate increases or less pronounced falls. Finally, the well-known downward trend in lending rates is evident, notwithstanding some volatility in the initial – – part of the sample before 1999 characterised by different monetary policy regimes. 

## **3 Literature** 

In this section, we briefly review the main theories on the role of house prices in the business cycle and in the transmission of monetary policy. A non exhaustive list of works which use multivariate structural models to quantify the impact of housing demand and monetary policy shocks is also reported. 

### **3.1 The Interaction between House Prices and the Business Cycle** 

**How do house price fluctuations affect households’ consumption decisions?** House price changes may have significant effects on aggregate consumption through different channels. First, an increase in house prices leads to a rise in homeowners’ wealth, seen as the sum of liquid financial assets and real estate’s value minus outstanding debt. However, as noted in Campbell and Cocco (2007), such an increase does not necessarily correspond to a raise in real wealth and therefore may have no effect on consumption. In fact, a house price increase does not affect the consumption behavior of a homeowner who is not planning to 

ECB Working Paper 2073, June 2017 

8 

sell his house. It is just a compensation for a higher implicit rental cost of living in the house as pointed out in Sinai and Souleles (2005). The age structure of the population may play a role. While Campbell and Cocco (2007) find that house price increases benefit mostly old owners, rather than young renters, confirming the so-called “wealth hypothesis”, Attanasio et al. (2009) findings support the so called “common factor hypothesis”: the impact of house prices on consumption is the same across different age groups. 

Second, even in the absence of wealth effect, an increase in house prices may lead to an increase in consumption, since housing can be used as collateral in a loan. It therefore allows borrowing constrained homeowners to smooth consumption over the life cycle, as shown in Ortalo-Magne and Rady (2006) and Lustig and Van Nieuwerburgh (2006). As argued in Almeida et al. (2006), if the collateral-based accelerator theory were to hold, one should expect a larger increase in consumption (following an increase in house prices) in high loanto-value (LTV) ratio countries. In fact, as stated by the authors “the procyclical increase in borrowing capacity may allow households to further increase housing spending, amplifying the collateral-based spending cycle”. Countries with a high LTV ratio are characterized by higher marginal opportunity to borrow. This argument is also made in Muellbauer (2015), where the author argues that in countries with low first-time buyer FTB-LTV ratio, higher house prices may have a negative impact on aggregate consumption if they are not accompanied by higher income or income growth expectations. The main reason is that those who want to become owner-occupiers need to save more while renters anticipate higher rents in the future which therefore negatively affects their spending decisions. 

**House prices and economic activity.** House price shocks may have a positive impact on GDP through higher consumption since, as discussed above, an increase in house prices implies a higher value of colletaral which can be used by a borrowing-constrained households to obtain more credit. Furthermore, due to the “Tobin’s q” effect, a rise in house prices encourages companies to invest more in housing construction (because their market value is higher than their construction costs) which in turn affects real growth. At the same time, housing demand shocks may exercise upward pressure on inflation directly trough higher rents (which are a component of CPI services inflation) and indirectly through consumption. The impact on inflation through higher rents should be larger in those countries where homeownership is lower. According to the “financial accelerator” theory, the (indirect) impact on CPI (through consumption) should be bigger in countries with higher LTV ratio. 

**House prices and the market for loans.** As discussed in Basten and Koch (2016), different mechanisms are at play in the relationship between house prices and mortgage volumes. First, an increase in house prices which is not accompanied by a contemporaneous increase in households wealth may induce those who are seeking to buying to resort to 

ECB Working Paper 2073, June 2017 

9 

more loans when purchasing a new housing. This increase in demand will result in higher equilibrium mortgage amounts, even in the absence of an outward shift in the mortgage supply curve. At the same time, given that the value of the collateral has increased, banks may be more willing to extend loans, especially if they expect future house prices to grow further. In such a case, an increase in house prices can also cause a shift of the credit supply curve. The subsequent consequences on lending rates depend on many factors among which, the availability of credit and regulatory capital ratio requirements, the risk perception of potential borrowers or the degree of competition in the banking sector. 

### **3.2 The Role of Monetary Policy Shock for House Price Fluctuations** 

Bernanke and Gertler (1995) argue that credit market frictions can have a relevant impact on households’ borrowing and spending decisions on durable items such as houses which in turn affect residential investment and therefore aggregate economic activity. Monetary policy can affect residential investment through the balance sheet channel. In fact, the authors note a direct link between housing demand and consumer balance sheets, due to features such as “down-payment requirements, up-front transaction costs, like closing costs and ‘points’ and minimum income-to-interest-payment ratios”. The lending channel also plays a role. According to Iacoviello and Minetti (2008), in the occurrence of a liquidity shock, banks may tend to shift from less to more liquid loans or to securities. Therefore, the relative illiquidity of mortgages becomes crucial especially in those countries where mortgage standardisation and securitisation are not common. At the same time, a fall in bank mortgages will result in a shortage of funds for house purchases, especially in those countries in which the supply of loans from specialist mortgage lenders or from the state is not enough to satisfy the demand for housing purchases. 

### **3.3 Selected Empirical Evidence** 

In this subsection, we present a non-exhaustive overview of the empirical literature on housing and the monetary policy transmission.The studies presented in Table 1 differ in terms of methodology, country coverage, and sample periods. Therefore, their comparability is inevitably limited. We focus only on the literature which derives insights on the quantitative importance of different mechanisms from multivariate structural models. Most of the works reviewed here use VAR models estimated using classical inference, with a few exceptions. Jarocinski and Smets (2008) use two Bayesian VAR specifications: a VAR in levels which uses standard Minnesota priors and one in differences with priors about the steady state, as in Villani, (2008). Goodhart and Hofmann (2008) use a Fixed-effects panel VAR. Iacoviello 

ECB Working Paper 2073, June 2017 

10 

**Table 1:** Selected Empirical Evidence 

|**Study**|**Country Coverage**|**Sample Period**|**Identifcation**|**Shocks**|**Confdence Bands**|
|---|---|---|---|---|---|
|Aoki et al. (2002)|UK|1975:Q1 - 1999:Q4|(a)|MP|2 Standard Errors|
|Bjornland and Jacobsen (2010)|NO, SE, UK|1983:Q1 - 2006:Q4|(b)|MP, HP|68%|
|Calza et al. (2013)|19 advanced countries|1980:Q1 - 2007:Q4|(a)|MP|2 Standard Errors|
|Elbourne (2008)|UK|1987:Jan - 2003:May|(d)|MP, HP|90%|
|Giuliodori (2005)|9 European countries|1979:Q3 - 1998:Q4|(a)|MP, HP|90%|
|Goodhart and Hofmann (2008)|17 industrialized countries|1973:Q1 - 2006:Q4|(e)|-|-|
|Iacoviello and Minetti (2008)|FI, UK, DE & NO|1974:Q2 -1999:Q4|(a) & (b)|MP, Mix|1 Standard Error|
|Jarocinski and Smets (2008)|US|1987:Q1 - 2007:Q2|(c)|HP, MP & TS|68%|
|Musso et al. (2011)|US & (aggregated) EA|1986:Q1 - 2009:Q2|(a)|MP, HP & CS|68%|



Identification Strategy: (a) stands for recursively identified system (Choleski decomposition); (b) for mix of short and long-run restrictions; (c) for mix of zero and sign restrictions; (d) Kim & Roubini (2000) approach; and (e) Reduced-Form analysis only. MP, HP and CS stands fo monetary policy, housing demand and credit supply shocks, respectively. TS is the term spread computed as the difference between long-term interest rates and federal funds rates. Mix denotes the external finance mix, which is the fraction of housing loans by “non-banks”. Iacoviello and Minetti (2008) use (b) to identifying MP shocks, and (a) for Mix. EA, FI, DE, NO, and SE are an abbreviation of Euro Area, Finland, Germany, Norway and Sweden, respectively. 

and Minetti (2008) estimate both VAR and VEC models. 

## **4 The Bayesian SSVS-VAR Model** 

We run a Bayesian VAR model for each country, namely Belgium, France, Germany, Ireland, Italy, the Netherlands, and Spain. VAR models have been widely used in the study of house prices and monetary policy, given that linear interdependencies may exist among the time series under study, and because of their ability to forecast and quantify impulse responses to macroeconomic shocks, among other reasons. The choice of countries is dictated by three reasons. First, we focus on a country dimension given the intrinsic idiosyncratic nature of housing markets across the euro area members. Second, the country coverage is influenced by the need of sufficiently long time series and reliable house price data. Finally, differently from the current literature, we are interested on a cross-country comparison for euro area countries rather than focusing on the euro area as a whole. 

For each country, the reduced form VAR(p) model van be written as 



for _t_ = 1 _, .., T,_ where _ut ∼ N_ (0 _,_ Σ _u_ ) and _yt_ is a _m ×_ 1 vector of endogenous variables.<sup>8</sup> 

The vector of endogenous variables in our baseline VAR model includes lending rates to households (for house purchase), national banks’ official rates (starting from 1999, we use 

> 8The subscript _i_ , denoting the particular country of interest, is omitted for clarity of exposition 

ECB Working Paper 2073, June 2017 

11 

the ECB rate on the marginal lending facility) and (annualized) growth rates of real house prices, real consumption (or alternatively real GDP), the consumer price index (CPI), and real loans to households. The choice of variables is in line with Giuliodori (2005) and Musso et al. (2011), among others. 

Equation (1) can be rewritten in compact form as 



where **Y** and _U_ are two _T × m_ matrices, _X_ is of dimension _T × K_ and _A_ = ( _µ, A_ 1 _, .., Ap_ )<sup>_′_</sup> is a _K × m_ matrix of coefficients, with _K_ = ( _mp_ +1). The estimation sample is 1980Q1:2014Q4.<sup>9</sup> The lag order of the model for each country has been chosen using the Akaike information criterion.<sup>10</sup> 

### **4.1 The Choice of the Prior** 

When the number of observations is limited, the number of parameters to be estimated may be too large relative to the available data. In the absence of restrictions in the regression coefficients and the covariance matrix, the model is over-parameterized. Consequently, the precision of inference and the reliability of prediction are negatively affected. 

To overcome this problem, the Bayesian approach has become widely used for VAR modelling, as it incorporates prior knowledge about parameter values. Various priors for unrestricted and restricted VARs which allow for shrinkage of the coefficients have been proposed. Prior elicitation is typically based on the ground of formal or informal economic theory or using information about pattern on macroeconomic data. For instance, Doan et al. (1984) suggested a Minnesota prior that shrinks the VAR parameters towards a random walk model. However, as noted by George, Sun and Ni (2008), such approaches “are based on an implicit assumption that the relevant restrictions are known” even though “at least for some economic problems, current theoretical knowledge does not warrant such confidence”. Moreover, Koop and Korobilis (2010) note that they require “substantial prior input from the researcher (although this prior input can be of an automatic form such as in the Minnesota prior)”. In view of the above reasons, following George, Sun and Ni (2008), we use a Bayesian stochastic search approach (SSVS) to selecting restrictions for VAR models that are supported by the data itself. It does so in an automatic fashion by using a hierarchical model, where the prior for a parameter is a function of a hyperparameter which in turn has its own prior. Therefore, it allows us to impose plausible restrictions on both the covariance matrix and 

> 9The sample periods vary across countries depending on data availability. 

> 10We choose to estimate the optimal lag order using Aikake rather than Schwartz criterion, as the former always yields a larger order. 

ECB Working Paper 2073, June 2017 

12 

the VAR regression coefficients while requiring “minimal prior input from researcher” (Koop and Korobilis, 2010). 

In particular, let _α_ = _vec_ ( _A_ ) be the _Km ×_ 1 vector of regression coefficients. The SSVS assumes that the prior distribution of _αj_ (the _j_ th element of _α_ ) is a mixture of two Normal distributions: 



where _γj_ is a dummy variable; _τ_ 0 _j_ is set to be small and _τ_ 1 _j_ large (for _j_ = 1 _, .., Km_ ) so that _αj_ is restricted to be very close to zero when _γj_ = 0 and unrestricted when _γj_ = 1. The dummy _γj_ is unknown and it has to be estimated in a data-based fashion. In particular, it is assumed that the _γj_ ’s are independent Bernoulli random variables so that 



As noted by George, Sun and Ni (2008), for each _j_ , _pj_ reflects the prior belief that _αj_ should be unrestricted. In the absence of such prior information, one could set _pj ≡ ._ 5 and let the data decide whether to shrink or not the coefficient to zero, as we do in this paper. A similar prior for Σ _u_ is assumed, in order to impose restriction on the covariance matrix. We refer the reader to Appendix A.1 and to George, Sun and Ni (2008) for details. 

Bayesian stochastic search approach is advantageous to select restrictions, shrinking many coefficients to zero, while providing relative probabilities of the selected models. Therefore, it helps researchers to focus on the more realistic submodels and in turn to make adequate finite sample inference. It differs from previous VAR modeling approaches as “it does not a priori rule out submodels of the VAR under consideration. Instead, it allows for the comparison of submodels based on the data”. In fact, as noted in Koop and Korobilis (2010), the result of the SSVS-MCMC algorithm will be Bayesian model averaging (BMA). At the same time, using simulated numerical examples, George, Sun and Ni (2008) find that their model performs well in selecting a satisfactory model and lead to improvements in forecasting in terms of Mean Squared Errors. 

## **5 Structural Analysis** 

### **5.1 Identification Strategy** 

To investigate the heterogeneous effects of house prices on the macro-economy, and their role in the monetary policy transmission across euro area countries, we identify both housing demand and monetary policy shocks. Intuitively, a housing demand shock is mainly attributable to households’ preferences. Such a shock would increase the relative attractiveness of housing vis-a-vis other goods/services, for example via a more favourable tax treatment or 

ECB Working Paper 2073, June 2017 

13 

**Table 2:** Short Run Responses to Housing Demand and Monetary Policy Shocks 

||**Housing Demand**|**Mon Pol**|**Loans Supply**|**Lend Rates**|**A. Supply**|**A. Demand**|
|---|---|---|---|---|---|---|
|**House Prices**|+|_−_|||||
|**Monet. Rate**|0|+|0|0|||
|**Loans**|+|_−_|+|_−_|||
|**Lending Rates**|+|+|_−_|+|||
|**Consump. (GDP)**|0|0|||+|+|
|**Infation**|0|0|||_−_|+|



The first column lists the endogenous variables of the VAR, which react to the shocks reported in the first row: housing demand shocks, monetary policy innovations, shocks to the credit supply (third and fourth column), aggregate supply and demand shocks. Our interest is in identifying housing demand and monetary policy shocks. 

deductibility of mortgage expenditures, or in terms of improved location due to enhanced services and amenities (think of a new underground project connecting the suburb of a city with its centre). Such a shock could also be interpreted as a preference shock resulting in changes in the political and social environments that encourage an increase in home-ownership as in Baldi (2014). In the case of Spain, Aspachs-Bracons and Rabanal (2011) interpret such a shock as driven by population changes: increased immigration, the baby boom generation, and social changes that reduce the number of persons per households and increase the number of household units. 

Since the works of Faust (1998), Canova and De Nicolo (2002), and Uhlig (2005), identification via sign restrictions has become increasingly popular (see Fry and Pagan (2011) for a review). We identify housing demand and monetary policy shocks by using a combination of zero and sign restrictions, using the algorithm proposed by Arias et al. (2014). The matrix of contemporaneous impacts of the shocks on the endogenous variables is defined in Table 2.<sup>11</sup> 

**Identification of housing demand shocks.** Among other reasons, combining zero with sign restrictions allows us to specify enough information to discriminate between a housing demand shock and an aggregate demand shock. This distinction would have not been possible by simply using an identification strategy which only imposes sign restrictions. 

The assumption that real consumption (or real GDP) and inflation do not react on impact to a house price shock, captures the idea of stickiness in the transmission of the shock due, 

> 11Identification of housing demand shocks does not require imposing any restrictions in rows 3 to 6 of the second column, as well as no restrictions in the (2,3) and (2,4) elements of the matrix shown in Table 2. Similarly, when identifying monetary policy shocks, we do not impose any restriction in rows 3 to 6 of the first column and in the (4,3) and (3,5) elements of the matrix. We do so to facilitate replicability of results. In fact, imposing all the restrictions is computationally costly as identification of each country’s VAR shocks would require around two days. 

ECB Working Paper 2073, June 2017 

14 

for example, to the transaction time required to buy/sell a property and/or to a lagged or muted reaction of rents affecting inflation with some delay. In fact, Muellbauer (2015) note that rents (both private and commercial) adjust relatively slowly to an increase in house prices. A sluggish response of inflation to house prices is also found in Bjornland and Jacobsen (2010). This assumption is also used in Jarocinski and Smets (2008) and it is in line with Giuliodori (2005) and Musso et al. (2011), who imposes a recursive structure in which house prices are ordered after GDP and inflation. The patterns used to distinguish aggregate demand and supply shocks are commonly used in the literature (e.g. Fry and Pagan (2011)). The zero contemporaneous impact of a house demand shock on monetary policy is consistent with a Taylor Rule. Furthermore, by imposing sign restriction rather than simply assuming a recursive causal structure of the system (e.g Sims, 1980), we are able to discriminate house prices shocks from loans supply and lending rates shocks on the ground of economic theory. Instead, it would be more difficult to find an appropriate theoretical justification in what order those variables are recursive. We assume that a house demand shock causes a contemporaneous increase in both real loans and lending rates. To understand the latter hypothesis, we look at the market for loans, and suppose demand and supply are in equilibrium. An exogenous housing demand shock may shift up the demand curve and down the supply curve (given that the value of housing collateral increases). We assume that the shift in the demand curve will be higher than the shift in supply because of regulatory requirements and balance sheets conditions that banks have to satifsy (e.g. the availability of mortgage credit is limited to a maximum LTV ratio, Almeida et al. (2006)) and given that some borrowers may be highly leveraged (e.g. their debt-to-income ratio is quite high even before applying for a new loan). As a result, the new equilibrium will be characterized by higher market lending rates and an increase in the volume of loans.<sup>12</sup> This is in line with Jarocinski and Smets (2008) and Iacoviello and Neri (2010), who assume that an increase in real house prices is not associated with a fall in nominal short-term interest rate to rule out an expansionary monetary poliy shock. This assumption allows us to distinguish between housing demand shocks and a (positive) loans supply shock. The latter may be associated to various events, such as changes in regulatory capital ratio requirements which increase the amount of banks capital available for loans.<sup>13</sup> 

**Identification of a monetary policy shock.** When recoverying the monetary policy (MP) shock, combining zero and sign restrictions allow us to be consistent with both the 

12For example, Basten and Koch (2016) studying the causal effect of house prices on the mortgage market in Switzerland, find that higher house prices lead to an increase in mortgage demand which is not accompanied by an expansion in mortgage supply. 

13See Gambetti and Musso (2016) and Eickmeier and Ng (2015) for a comprehensive list of possible events which may trigger a shock in the supply of credit. 

ECB Working Paper 2073, June 2017 

15 

literature which studies systematic changes in monetary policy rules (e.g. Christiano et al., 1999) and the one which focuses on the role of asset prices in the transmission of MP shocks (e.g. Zettelmeyer (2004), Rigobon and Sack (2004) and Kuttner (2005)). In line with the former, we assume that central banks react endogenously to conemporaneous movement in current prices and output, among other things. In other words, we assume that output and prices respond only with a lag to a policy instrument shock. The latter branch of literature argues that house prices, and asset prices in general, react almost instantaneously to news and therefore are important transmission mechasnism of monetary policy shocks. Therefore, we assume that both interest rates and house prices react simultaneously to news. To consider house prices as forward looking variables which respond immediately to monetary policy news is consistent with economic theory, see Iacoviello (2005). A similar assumption is made in Bjornland and Jacobsen (2010). Instead, using a recursive structure, Goodhart and Hofmann (2001) and Giuliodori (2005) impose that house prices do not respond immediately to monetary policy shocks. Assuming a decrease (increase) in loans after a contractionary (expansionary) monetary policy shock is in line with Gerali et al. (2010) and Gertler and Karadi (2011). We also assume that central banks do not react contemporaneously to a loans supply shock. In fact, as central banks target inflation, they intervene only if inflationary pressure from supply shocks realizes.<sup>14</sup> 

**Model Identification Problem.** Although sign restrictions provide sufficient information to identify the structural parameters, they do not lead to a unique set of impulse responses.<sup>15</sup> As noted by Fry and Pagan (2011), there is a variety of models which are consistent with the imposed sign restrictions and which provide the same fit to the data. In other words, sign restrictions do not overcome the “model identification problem”. We adopt Fry and Pagan (2007)’s “Median Target” (MT) strategy which consists in finding a single model whose impulse responses are closest to the median responses across all the qualifying models. By devising a criterion to do this, we solve the “multiple models” problem since it ensures that the impulses come from the same model and that the corresponding shocks are orthogonal. As noted in Fry and Pagan (2011), the MT criterion selects the median responses when these are uncorrelated. Finally, we note that although the choice of the MT criterion, rather than other magnitude of impulses, may be arbitrary, it is a popular choice as it captures the central tendency of all the plausible models found (Eickemeier and Ng, 2015). Another advantage of using the MT strategy is that when employing this criterion, the sum of the contributions of each error to the forecast error variance of each endogenous variable is equal to one. 

> 14As discussed in Hristov et al. (2012) and Gambetti and Musso (2016), it is not always clear that an increase in the supply of credit loans causes a contemporaneous rise in inflation. 

> 15In our setting, at each Gibbs sampling iteration, we generate at most 100 structural matrices satisfying the imposed zero and sign restrictions. 

ECB Working Paper 2073, June 2017 

16 

### **5.2 The Impact of Housing Demand Shocks** 

In this section we report the impulse responses of selected variables to a housing demand shock - in terms of a 1% increase in real house prices - for each country under investigation. Comparison across countries is facilitated by the fact that all the structural shocks have unit variances. In addition, we apply the Mean Group (MG) estimation procedure proposed by Pesaran and Smith (1995) to obtain cross-sectional average responses. In particular, let _ζkl_<sup>(</sup><sup>_i_)</sup> be a _h ×_ 1 vector containing the MT responses of variable _l_ to an impulse in variable _k_ over _h_ periods, for country _i_ . The MG responses of variable _l_ to an impulse in variable _k_ (over _h_ periods), can be computed as the cross-sectional average 



Similarly, the credible intervals for the MG responses can be computed by taking the cross-sectional average of the impulse responses associated with the percentile of interest. 

For the vast majority of countries, a positive housing demand shock has a significant positive impact on inflation, economic activity and real loans to households. Figure 1 shows the effects of housing demand shocks on house prices, real GDP, and inflation. The magnitude of the maximum impact on inflation varies between 0.02% and 0.2%, averaging around 0.05% across the countries examined. The impact on real GDP varies between 0.04% and 0.12%, averaging 0.09% and is significant for France, Ireland, Spain, and partially Italy. The maximum impact of the shock is achieved after three quarters on average for activity and inflation. Three country specific observations can be made. First, the impact of a housing demand shock on real GDP is highest for Ireland and Spain, countries having experienced a boom-bust pattern in house prices.<sup>16</sup> Second, the impact of the shock on inflation are larger and significant in the case of Germany, France, and Spain. Muellbauer (2015) argues that in Germany, having a system of comparatively flexible rent controls, an increase in house prices may be followed by a rise in rents affecting in turn inflation developments. 

> 16When using 95% confidence bands, the impact is significant in Ireland and Spain, as well as in Italy and France. For Belgium, the Netherlands and Germany significance holds only when considering 80% credible intervals. 

ECB Working Paper 2073, June 2017 

17 



**Figure 1:** Impulse response functions to a housing demand shock, for real house prices growth, real GDP growth, and inflation, across countries. The red lines delimit the 95 per cent credible interval. The grey shaded area delimits the space between 10th and 90th percentiles. The blue line is the median impulse response, while the crossed blue line is the median Mean Group (MG) response, both obtained using the MT approach. 

**House prices and the market for loans.** The impact on real loans to households, shown in Figure 2, varies between 0.10% and 0.5%, averaging 0.35%. The positive effect of house price shocks on loans is highest on impact for all countries and reflects the tight links between the credit and the housing markets. The impulse responses of real loans exhibits a fairly similar pattern across countries in terms of expected sign, size and statistical significance. 

ECB Working Paper 2073, June 2017 

18 



**Figure 2:** Impulse response of real loans to a housing demand shock. Cross-country comparisons. The red lines delimit the 95 per cent credible interval. The grey shaded area delimits the space between 10th and 90th percentiles. The blue line is the median impulse response while the crossed blue line is the median Mean Group response, both obtained using the MT approach. 

**Wealth Effects.** Results shown in Figure 3 indicate that the magnitude of the maximum impact on real private consumption varies between 0.02% and 0.16% across the countries examined, averaging 0.1%, with the maximum impact occurring after three quarters on average. They confirm the intuition that liquidity constrained households can expand their consumption capabilities using housing wealth as collateral to obtain higher borrowing (Iacoviello, 2004). Moreover, the ordering of countries is confirmed. Ireland and Spain exhibit the largest wealth effects on consumption (around 0.15%) followed by Italy. Results for the first two countries are highly significant, while those for the others exhibit a lower magnitude of the impact and lower statistical significance. Muellbauer (2015) finds a negative effect of real house prices on consumption in both France and Germany. Instead, our analysis reveals that a housing demand shock has a positive impact on consumption in both countries, even though, as noted above, this effect is rather muted. 

ECB Working Paper 2073, June 2017 

19 



**Figure 3:** Impulse response of real private consumption to a housing demand shock. Cross-country comparisons. The red lines delimit the 95 per cent credible interval. The grey shaded area delimits the space between 10th and 90th percentiles. The blue line is the median impulse response while the crossed blue line is the median Mean Group response, both obtained using the MT approach. 

#### **5.2.1 Variance Decomposition** 

Forecast error variance (FEV) decomposition is crucial to understand how important a housing shock is for consumption, credit supply and other variables of interest. In fact, this “innovation accounting” analysis allows us to answer to what extent the variability in the aforementioned variables can be explained by a housing demand shock. Figure 4 shows the proportion of 1, 3, 5 _,_ and 20 quarters ahead forecast error variance of each endogenous variable of the VAR accounted for by innovations in real house prices. 

ECB Working Paper 2073, June 2017 

20 



**Figure 4:** Variance Decomposition. Proportion of 1, 3, 5, 10, and 20 quarters ahead FEV of each variable accounted for by innovations in house prices. Cross-country comparisons. Red line indicates the average contribution across countries. 

The contribution of the housing demand shock to fluctuations of aggregate consumption, inflation, loans and lending rates is highly heterogeneous across countries. About 40% of the FEV of house prices is accounted for by own innovations in Ireland and Spain, followed by Belgium and Italy. The identified structural shock seems to play a minor role in explaining the variation of consumption across countries, with the exception of Spain and Ireland, where house prices innovations contribute slightly less than 15% to the forecast error variance of consumption. For all the other countries, the contribution is less than 5% and almost zero in Germany. In France, Ireland, and Spain, only 10% of the FEV of inflation can be explained by a housing shock. On the other hand, housing demand shocks play an important role in explaining loans FEV across all countries under investigation (the average contribution is approximately 40%), confirming the “financial accelerator” hypothesis, according to which changes in the collateral affect borrowing capacity (Bernanke et al. (1996) and Almeida et al. (2006)). 

ECB Working Paper 2073, June 2017 

21 

### **5.3 Monetary Policy Shocks and the Role of House Prices** 

Regarding the role of house prices in the transmission of monetary policy, we find that monetary policy shocks have a significant, strong and lasting impact on house prices, corroborating the existence of a credit channel in the euro area housing market. 



**Figure 5:** Impulse response of house prices to a monetary policy shock. Cross-country comparisons. The red lines delimit the 95 per cent credible interval. The grey shaded area delimits the space between 10th and 90th percentiles. The blue line is the median impulse response while the crossed blue line is the median Mean Group response, both obtained using the MT approach. 

Figure 5 depicts the impulse responses of real house price growth to a monetary policy shock in terms of 25 basis points increase in the policy rate. The responses are highly heterogeneous across the countries examined. A 25 basis points contractionary monetary policy shock significantly reduces real house prices between 0.4% (in Germany) and 3% (in Spain), on average by 1.6%, with the maximum impact generally occurring contemporaneously.<sup>17</sup> Being aware of such heterogeneity is crucial to address possible imbalances across countries and to design policies to mitigate risks deriving from residential property markets. The result 

17 Comparisons across countries is further facilitated by the fact that all the structural shocks have unit variances. 

ECB Working Paper 2073, June 2017 

22 

for Spain seems to suggest that lower interest rates may have played a role in stimulating the demand for housing by easing financing conditions. In Ireland, the response of house prices to a monetary shock are in line with the average responses. 



**Figure 6:** Impulse response of real loans to a monetary policy shock, in terms of a 25 basis points increase in the monetary policy rate. Cross-country comparisons. The grey area delimits the space between 10th and 90th percentiles. The red lines delimits the 95 per cent credible interval. The blue line is the median impulse response while the crossed blue line is the median Mean Group response, both obtained using the MT approach. 

As shown in Figure 6, a contractionary monetary policy shock also causes a significant decline of real loans to households, between 0.2% (Germany) and 0.8% (the Netherlands), on average by 0.6%, with the maximum impact occurring contemporaneously. The heterogeneity across countries of the impact of the shock on real loans does not appear to be related to the tenure of the mortgage rate structure. The magnitude of the impact is also quite dispersed – within countries characterised by prevalence of variable rates such as Italy, Spain and – – Ireland or fixed rates such as France, Belgium, Germany and the Netherlands (ESRB (2015)). 

ECB Working Paper 2073, June 2017 

23 

#### **5.3.1 Variance Decomposition** 

To quantify the importance of monetary policy shocks we compute the forecast error variance decomposition. A monetary policy shock accounts on average for around 25% of the FEV of real house price growth (Figure 7). The contribution is above the average for Spain, followed by Italy and the Netherlands and is the lowest in Germany. 



**Figure 7:** Variance Decomposition. Proportion of 1, 3, 5, 10, and 20 quarters ahead FEV of each variable accounted for by innovations in monetary rate. Cross-country comparisons. Red line indicates the average contribution across countries. 

In the latter country, only less than 10% of the FEV of house price growth is accounted for by a monetary policy innovation. These results corroborate the evidence that the housing market plays an important role in the monetary policy transmission mechanism, and provide new evidence on the heterogeneous impact of monetary policy on house prices fluctuations. Monetary policy shocks also contribute on average around 30% of the variability in real loan growth, which is less than the average contribution of housing demand shocks. 

ECB Working Paper 2073, June 2017 

24 

### **5.4 Historical Decompositions** 

So far we have studied how the structural shocks of interest affect average movements in the data, by means of forecast error variance decompositions and impulse response functions. In this section, we use historical decompositions in order to assess the cumulative effects of housing demand and monetary policy shocks on the business cycle and their relative importance in explaining the observed fluctuations in the endogenous variables of the VAR, at each point in time. 

To compute the historical decompositions, we rewrite the VAR model described in equation (1), in its moving average representation: 



where Θ _s_ = Φ _sA_<sup>˜</sup> _o_ , and _wt−s_ = _A_<sup>˜</sup><sup>_−_</sup> _o_<sup>1</sup><sup>_ut−s_are the orthogonal shocks.</sup><sup>_A_˜</sup><sup>_o_is the contemporaneous</sup> structural matrix satisfying the imposed zero and sign restrictions. As we cannot estimate all the “infinite” shocks, _wt−s_ , for _s_ = 0 _, .., ∞_ , we truncate the series. We denote such an approximation as 



ˆ ˆ where _yt_ = (ˆ _yt − µ_ ). The unknown values in the right-hand side are replaced by their estimates. Each endogenous variable, _y_ ˆ _kt_ , for _k_ = 1 _, .., m_ can be written as 



where _y_ ˆ _kt_<sup>(</sup><sup>_j_)is the cumulative effect of shock</sup><sup>_j_to the</sup><sup>_k_th variable of the VAR process and</sup><sup>_θ_ˆ</sup> _s_<sup>(</sup><sup>_k,j_)</sup> is the ( _k, j_ ) element of Θ<sup>ˆ</sup> _s_ . 

As suggested in Kilian and Lütkepohl (2017), we demean both _y_ ˆ _t_ and _yt_ to remove any discrepancy among them. We discard the initial (transients) observations (in particular, we remove the first 20 observations) so that the two observations coincide with minimal approximation errors (which could arise from the truncation of the infinite sum). Following Kilian and Lütkepohl (2017), we construct counterfactuals as an alternative way of assessing the cumulative effect of a structural shock to the observed data _ykt_ , for _k_ = 1 _, .., m_ . They are defined as 



where the counterfactual, _c_<sup>(</sup> _kt_<sup>_j_),representstheevolutionof</sup><sup>_ykt_intheabsenceofthe</sup><sup>_j_thstruc-</sup> tural shock. 

ECB Working Paper 2073, June 2017 

25 



**Figure 8:** Historical counterfactuals for real (private) consumption growth. The counterfactuals (black line) indicate the evolution of real consumption growth in the absence of housing demand shocks. The difference between actual data (blue line) and counterfactuals corresponds to the cumulative effects of housing shocks to real consumption growth over time (dotted red line). If the red line lies above zero, it means that the shocks positively contributed to the growth rates of real consumption. The left y-axis measures quarterly changes (from the sample mean) in real consumption growth with and without the cumulative effects of housing shocks. The right y-axis reports quarterly changes (from their sample mean) in the cumulative effects of housing demand shocks. 

**Housing Demand Shocks and Business Cycles.** Figure 8 illustrates the evolution of (quarterly) real private consumption growth ( _ykt_ ) in deviations from the sample mean against its counterfactual ( _c_<sup>(</sup> _kt_<sup>_j_)).Thelatterindicateshowrealconsumptiongrowthwould</sup> have evolved if all the realizations of housing demand shocks had been equal to zero, while maintaining the remaining structural shocks in the model. The difference between the two (ˆ _ykt_<sup>(</sup><sup>_j_))representsthecumulativeeffectsofhousingdemandshocksonconsumptionupto</sup> a certain point in time. It measures how growth rates of real consumption would have evolved if the economy had been hit only by housing demand shocks, in the absence of all other concurrent shocks. A line above zero reveals that the structural shock exerted upward pressure on consumption. 

The historical decompositions analysis suggests an important role of housing demand 

ECB Working Paper 2073, June 2017 

26 

shocks in driving consumption in Ireland and Spain, confirming previous findings for the impulse response analysis. It is noteworthy that in both countries, in the absence of housing demand shocks, the growth rates of real private consumption would have been lower than the actual rates between 2002 and 2007, and larger between 2008 and 2013. In particular, in Ireland, the cumulative effect of housing demand shocks on consumption is equal to 0.79% up to 2006 and equal to -1.16% at the end of 2011. Similarly, in Spain, in the absence of other shocks, if the growth rates of real consumption (in deviations from the sample mean) had been driven exclusively by housing demand shocks, they would have been largest around 1995 and 2004 (0.5%), and lowest in 2012 (-0.66%).<sup>18</sup> The cumulative effect of housing demand shocks is rather muted in the remaining countries. 



**Figure 9:** Historical counterfactuals for real loans growth. The counterfactuals (black line) indicate the evolution of real loans growth in the absence of housing demand shocks. The difference between actual data (blue line) and counterfactuals corresponds to the cumulative effects of housing shocks to real loans growth over time (dotted red line). If the red line lies above zero, it means that the shocks positively contributed to the growth rates of real loans. The left y-axis measures quarterly changes (from the sample mean) in real loans growth with and without the cumulative effects of housing demand shocks. The right y-axis reports quarterly changes (from the sample mean) in the cumulative effects of housing shocks. 

> 18Excluding monetary policy from the VAR, these differences would have been even higher. 

ECB Working Paper 2073, June 2017 

27 

As shown in Figure 9, the historical decomposition analysis corroborates the ”financial accelerator” hypothesis according to which increases in the collateral improve households borrowing capacity. The cumulative effects of housing demand shocks to real loans growth are sizeable across most of the countries under investigation. As for consumption, the contribution of housing shocks to real loans growth was larger in Spain and especially in Ireland. In both countries, exogenous housing price increases significantly contributed to the raise of real loans growth during the specific housing boom episode observed in the sample. The subsequent bursting of the housing bubble and the consequent decline in house prices drastically reduced the availability of loans, which in turn may also have had negative consequences on real consumption growth. 



**Figure 10:** Historical counterfactuals for real house prices growth. The counterfactuals (black line) indicate the evolution of real house prices growth in the absence of monetary policy shocks. The difference between actual data (blue line) and counterfactuals corresponds to the cumulative effects of monetary policy shocks to real house prices growth over time (dotted red line). If the red line lies above zero, it means that the shocks positively contributed to the growth rates of real house prices. The left y-axis measures quarterly changes (from the sample mean) in real house prices growth with and without the cumulative effects of monetary shocks. The right y-axis reports quarterly changes (from the sample mean) in the cumulative effects of monetary policy shocks. 

ECB Working Paper 2073, June 2017 

28 

**Monetary Policy Shocks and House Price Dynamics.** Figure 10 plots the historical evolution of (quarterly) real house prices growth (in terms of deviations from the sample mean), the dynamics of the counterfactual, as well as the difference between the two (i.e. the hypothetical movements of real house prices growth if all structural shocks but monetary policy shocks had been turned off). The cumulative contribution of monetary policy shocks to house price growth differ widely across countries: from a peak of 0.4% in Germany to a maximum cumulative effect of above 2% in Ireland, followed by the Netherlands and Spain. The maximum contribution is also relevant in Italy (slightly above 1%), while in Belgium and France it lies in a middle ground. It is worthy of note that a substantial increase in house prices would have occurred in Ireland and Spain between 2001 and 2006 even in the absence of all other structural shocks but monetary policy. Finally, we note that the cumulative contributions of monetary policy shocks vary not only in size but also they do not appear to be correlated over time across countries. 

## **6 Conclusions** 

In this paper, we use a structural Bayesian VAR model to provide a systematic structural analysis of the effects of housing demand shocks on the macro-economy across selected euro area countries, and the role of house prices in the monetary transmission mechanism. A novel identification strategy which combines zero and sign restrictions is proposed. Among other things, by doing so, we are able to distinguish between a house price and an aggregate demand shock, which would be difficult otherwise. To overcome the over-parameterization problem, the priors are selected using a Stochastic Search Variables Selection method, which allows for shrinkage of the VAR coefficients while selecting restrictions that are supported by the data itself. This in turn makes adequate finite sample inference and exploits in full the intrinsic cross-country heterogeneity typical of the housing market. 

Furthermore, given the lack in the literature of comparative studies that try to quantify the degree of heterogeneity of the impact of house prices and their role in the transmission of monetary policy across euro zone members, we exploit the cross-sectional dimension of our data to quantify and compare the different dynamics of house prices, their heterogeneous effect on the macro-economy and the diverse impact of monetary policy in driving house price cycles across eurozone member states. Quantifying such diverse effects is important from a policy perspective, in particular when addressing real and financial imbalances at the country level. 

The structural analysis confirms that the effects of housing demand and monetary policy shocks differ widely across the countries under investigation. We document the existence of a housing “wealth effect” in Ireland and Spain, where a one percent increase in real house prices is associated with a 0.15% rise in real private consumption. The fact that 

ECB Working Paper 2073, June 2017 

29 

both countries experienced a housing bubble corroborates the view that house price booms play an important role in boosting confidence, which in turn stimulate consumption. The historical decomposition analysis supports these findings. The cumulative effects of housing demand shocks on consumption are larger in Ireland and Spain. In both countries, housing demand shocks significantly contributed to the surge of consumption growth during the specific housing boom episode observed in the sample and to the subsequent decline during the recession started around 2007. 

The impact of housing demand shocks on real loans to household exhibits a less heterogeneous and a fairly similar pattern across countries in terms of sign, size and statistical significance. On average, a housing demand shock, in terms of a 1% increase in house prices, causes a 0.35% increase in real loans. Housing demand shocks play an important role in explaining loans forecast error variance across all countries under investigation. This clearly suggests that changes in the value of collateral affect borrowing capacity. The historical decomposition analysis provides further evidence in support of the “financial accelerator” theory. We then show that monetary policy has a strong and lasting impact on house prices, corroborating the existence of a credit channel in the euro area housing market and an important role of house prices in the monetary transmission mechanism. The impact is highly heterogeneous, varying between 0.4% (in Germany) and 3% (in Spain). A monetary policy shock accounts on average for around 25 to 30% of the forecast error variance of real house price growth. The historical decomposition analysis documents a highly heterogenous contribution of monetary policy shocks to house price dynamics. 

ECB Working Paper 2073, June 2017 

30 

## **A Technical Appendix** 

### **A.1 The VAR with SSVS Prior** 

**Prior on the VAR coefficients.** Let _α_ = _vec_ ( _A_ ) be the _Km ×_ 1 vector of regression coefficients. The SSVS assumes that the prior distribution of _αj_ (the _j_ th element of _α_ ) is a mixture of two Normal distributions: 



To select _τ_ 0<sup>2</sup> _i_<sup>and</sup><sup>_τ_2</sup> 1 _i_<sup>,wefollowGeorge,SunandNi(2008).Theyproposea“default</sup> ˆ ˆ semi-automatic approach” which involves setting _τ_ 0 _j_ = _c_ 0 _σαj_ and _τ_ 1 _j_ = _c_ 1 _σαj_ , where _c_ 0 _≪ c_ 1, ˆ i.e. _c_ 0 = 0 _._ 1 and _c_ 1 = 10; _σαj_ is the standard error associated with the unconstrained least squares estimate of _αj_ . The dummy _γj_ is unknown and it has to be estimated in a data-based fashion. In particular, it is assumed that the _γj_ ’s are independent Bernoulli random variables so that 



As noted by George, Sun and Ni (2008), for each _j_ , _pj_ reflects the prior belief that _αj_ should be unrestricted. In the absence of such prior information, one could set _pj ≡ ._ 5 and let the data decide whether to shrink or not the coefficient to zero, as we do in this paper. 

**Prior on the covariance parameters.** The covariance matrix can be decomposed as _′_ Σ<sup>_−_</sup> _u_<sup>1</sup> = , where _Ψ_ is upper triangular. Let _ψij_ be the ( _i, j_ )th entry of _Ψ_ . Each off-diagonal element has the prior distribution 



We arbitrarily set _κ_ 0 _ij_ = 0 _._ 1, and _κ_ 1 _ij_ = 6. Alternatively, _κ_ 0 _ij_ and _κ_ 1 _ij_ can be chosen using similar consideration for setting _τ_ 0 _j_ and _τ_ 1 _j_ . 

We assume that the _ωij_ are independent Bernoulli random variables such that 



for _i_ = 1 _, ..., m_ and _j_ = 2 _, ..., m −_ 1 and where _qij ∈_ (0 _,_ 1). 

Given the absence of prior information on whether _ωij_ should be unrestricted, we follow George, Sun and Ni (2008) suggestion, by setting _qij_ = 0 _._ 5. 

For the diagonal elements, it is assumed prior independence with _ωii_<sup>2</sup><sup>_∼gamma_(</sup><sup>_ai, bi_).</sup> The hyperparameters ( _ai, bi_ ) are set equal to (0 _._ 01 _,_ 0 _._ 01) to render this prior noninfluential. 

ECB Working Paper 2073, June 2017 

31 

**Posterior Distribution.** Posterior computation is carried out using the Gibbs sampling algorithm described in George, Sun and Ni (2008). 

Following the latter, we simulate a Markov chain of 20 _._ 000 cycles and discard the initial 10 _._ 000 burn-in replications. In their simulated numerical examples, the authors note that simulation results using a larger number of cycles (50 _._ 000) change little, suggesting that the Markov chains converge rather quickly. 

Estimation of the reduced form VAR requires approximately one minute (for each country). 

## **B Data** 

### **B.1 Data Sources** 

All data cover the period 1980Q1-2014Q4, unless otherwise specified. All variables were transformed in annualised quarter on quarter changes except for interest rates which are in levels. When seasonally adjusted data are not directly available, we make the necessary adjustments, using the X-12 Census method. Nominal house prices and nominal loans were deflated using CPI indices. 

– **GDP, Private Consumption and Consumer Price Indices.** Sources: OECD Main Economic indicators. Data on private consumption for Ireland starts on 1990Q1. Data on private consumption for Germany are obtained from the European Central Bank’s Multi Country Model Dataset. 

**House Prices.** For Belgium and Italy, we use “Residential property prices, New and existing dwellings; Residential property in good & poor condition; Whole country”. For France, Ireland, the Netherlands, and Spain, we use “Residential property prices, New dwellings; Residential property in good & poor condition; Whole country”. For Germany, an annual series covering new dwellings (apartments and houses) in 50 West German cities were used given its long time span (starting in 1975) and due to the absence of structural breaks related to the German reunification compared to other available series (the annual series was linearly interpolated at a quarterly frequency). House price data for Spain starts in 1987Q1. 

Sources: ECB and national sources, and BIS (Germany). 

**Loans.** We use data on “Credit to Households and NPISHs from All sectors”. Source: BIS http://www.bis.org/statistics/totcredit.htm 

ECB Working Paper 2073, June 2017 

32 

**Lending Rates.** The dataset consists of “Lending to households for house purchase excluding revolving loans and overdrafts, convenience and extended credit card debt”. Sources: ECB - MFI Interest Rate Statistics. 

**Monetary Policy Rates.** For the pre-EMU period we use national official discount rates from BISM Dataset: “BIS Macro-economic series”. From 1999, we use the ECB Marginal Lending Facility. 

ECB Working Paper 2073, June 2017 

33 

### **B.2 Supplementary Charts** 

#### **Dynamics across the Euro Area.** 



ECB Working Paper 2073, June 2017 

34 

## **References** 

- [1] Heitor Almeida, Murillo Campello, and Crocker Liu. The financial accelerator: evidence from international housing markets. _Review of Finance_ , 10(3):321–352, 2006. 

- [2] Kosuke Aoki, James Proudman, and Gertjan Vlieghe. Houses as collateral: Has the link between house prices and consumption in the UK changed? _Federal Reserve Bank of New York Economic Policy Review_ , 8(1):163–78, 2002. 

- [3] Jonas Arias, Juan Francisco Rubio-Ramirez, and Daniel F Waggoner. Inference based on SVARs identified with sign and zero restrictions: Theory and applications. _FRB Atlanta Working Paper_ , 2014. 

- [4] Oriol Aspachs-Bracons and Pau Rabanal. The effects of housing prices and monetary policy in a currency union. _IMF Working Papers_ , pages 1–52, January 2011. 

- [5] Orazio P Attanasio, Laura Blow, Robert Hamilton, and Andrew Leicester. Booms and busts: Consumption, house prices and expectations. _Economica_ , 76(301):20–50, 2009. 

- [6] Guido Baldi. The economic effects of a central bank reacting to house price inflation. _Journal of Housing Economics_ , 26:119–125, 2014. 

- [7] Christoph Basten and Catherine Koch. The causal effect of house prices on mortgage demand and mortgage supply: Evidence from Switzerland. _Journal of Housing Economics_ , 30:1–22, 2015. 

- [8] Ben Bernanke, Mark Gertler, and Simon Gilchrist. The financial accelerator and the flight to quality. _Review of Economics and Statistics_ , 78:1–15, 1996. 

- [9] Ben S Bernanke and Kenneth N Kuttner. What explains the stock market’s reaction to Federal Reserve policy? _The Journal of Finance_ , 60(3):1221–1257, 2005. 

- [10] Lorenzo Bini Smaghi. The European Central Bank in a global perspective - central banking and the challenge of rising inflation. _Speech at the 16th Annual Conference of the German-British Forum_ , May 2011. 

- [11] Hilde C Bjørnland and Dag Henning Jacobsen. The role of house prices in the monetary policy transmission mechanism in small open economies. _Journal of Financial Stability_ , 6(4):218–229, 2010. 

- [12] Alessandro Calza, Tommaso Monacelli, and Livio Stracca. Housing finance and monetary policy. _Journal of the European Economic Association_ , 11(s1):101–122, 2013. 

ECB Working Paper 2073, June 2017 

35 

- [13] John Y Campbell and Joao F Cocco. How do house prices affect consumption? evidence from micro data. _Journal of Monetary Economics_ , 54(3):591–621, 2007. 

- [14] Fabio Canova and Gianni De Nicolo. Monetary disturbances matter for business fluctuations in the G-7. _Journal of Monetary Economics_ , 49(6):1131–1159, 2002. 

- [15] Roberto Cardarelli, Deniz Igan, and Alessandro Rebucci. The changing housing cycle and the implications for monetary policy. _World Economic Outlook: Housing and the Business Cycle_ , 19:52, 2008. 

- [16] Lawrence J Christiano, Martin Eichenbaum, and Charles L Evans. Monetary policy shocks: What have we learned and to what end? _Handbook of Macroeconomics_ , 1:65– 148, 1999. 

- [17] Thomas Doan, Robert Litterman, and Christopher Sims. Forecasting and conditional projection using realistic prior distributions. _Econometric Reviews_ , 3(1):1–100, 1984. 

- [18] Sandra Eickmeier and Tim Ng. How do US credit supply shocks propagate internationally? a GVAR approach. _European Economic Review_ , 74:128–145, 2015. 

- [19] Adam Elbourne. The UK housing market and the monetary policy transmission mechanism: An SVAR approach. _Journal of Housing Economics_ , 17(1):65–87, 2008. 

- [20] European Central Bank. Structural factors in the EU housing markets. March 2003. 

- [21] European Central Bank. Housing wealth and private consumption in the euro area. _ECB Monthly Bulletin_ , pages 59–71, January 2009. 

- [22] European Central Bank. The state of the house price cycle in the euro area. _ECB Economic Bulletin_ , (6), 2015. 

- [23] European Central Bank. Financial Stability Review. November 2016. 

- [24] European Systemic Risk Board. Report on residential real estate and financial stability in the EU. December 2015. 

- [25] Jon Faust. The robustness of identified VAR conclusions about money. In _CarnegieRochester Conference Series on Public Policy_ , volume 49, pages 207–244. Elsevier, 1998. 

- [26] Andrea Ferrero. House price booms, current account deficits, and low interest rates. _Journal of Money, Credit and Banking_ , 47(S1):261–293, 2015. 

ECB Working Paper 2073, June 2017 

36 

- [27] Renée Fry and Adrian Pagan. Some issues in using sign restrictions for identifying structural vars. _National Centre for Econometric Research Working Paper_ , 14, 2007. 

- [28] Renée Fry and Adrian Pagan. Sign restrictions in structural vector autoregressions: A critical review. _Journal of Economic Literature_ , 49(4):938–960, 2011. 

- [29] Luca Gambetti and Alberto Musso. Loan supply shocks and the business cycle. _Journal of Applied Econometrics_ , 2016. 

- [30] John Geanakoplos. The leverage cycle. In _NBER Macroeconomics Annual 2009, Volume 24_ , pages 1–65. University of Chicago Press, 2010. 

- [31] Edward I. George, Dongchu Sun, and Shawn Ni. Bayesian stochastic search for VAR model restrictions. _Journal of Econometrics_ , 142(1):553–580, 2008. 

- [32] Andrea Gerali, Stefano Neri, Luca Sessa, and Federico M Signoretti. Credit and banking in a DSGE model of the euro area. _Journal of Money, Credit and Banking_ , 42(s1):107– 141, 2010. 

- [33] Mark Gertler and Peter Karadi. A model of unconventional monetary policy. _Journal of Monetary Economics_ , 58(1):17–34, 2011. 

- [34] Massimo Giuliodori. The role of house prices in the monetary transmission mechanism across european countries. _Scottish Journal of Political Economy_ , 52(4):519–543, 2005. 

- [35] Charles Goodhart and Boris Hofmann. Asset prices, financial conditions, and the transmission of monetary policy. In _Conference on Asset Prices, Exchange Rates, and Monetary Policy, Stanford University_ , pages 2–3, February 2001. 

- [36] Clive W. J. Granger and Paul Newbold. _Forecasting economic time series_ . Academic Press, 2014. 

- [37] Philipp Hartmann. Real estate markets and macroprudential policy in Europe. _Journal of Money, Credit and Banking_ , 47(S1):69–80, 2015. 

- [38] Nikolay Hristov, Oliver Hülsewig, and Timo Wollmershäuser. Loan supply shocks during the financial crisis: Evidence for the euro area. _Journal of International Money and Finance_ , 31(3):569–592, 2012. 

- [39] Matteo Iacoviello. House prices, borrowing constraints, and monetary policy in the business cycle. _The American Economic Review_ , 95(3):739–764, 2005. 

ECB Working Paper 2073, June 2017 

37 

- [40] Matteo Iacoviello and Raoul Minetti. The credit channel of monetary policy: Evidence from the housing market. _Journal of Macroeconomics_ , 30(1):69–96, 2008. 

- [41] Matteo Iacoviello and Stefano Neri. The role of housing collateral in an estimated twosector model of the US economy. _Boston College Working Papers in Economics_ , (412), 2007. 

- [42] Matteo Iacoviello and Stefano Neri. Housing market spillovers: evidence from an estimated DSGE model. _American Economic Journal: Macroeconomics_ , 2(2):125–164, 2010. 

- [43] Marek Jarocinski and Frank Smets. House prices and the stance of monetary policy. _Federal Reserve Bank of St. Louis Review_ , 90(4):339–365, 2008. 

- [44] Lutz Kilian and Helmut Lütkepohl. _Structural vector autoregressive analysis_ . Cambridge University Press, 2017. 

- [45] Gary Koop and Dimitris Korobilis. Bayesian multivariate time series methods for empirical macroeconomics. In _Foundations and Trends in Econometrics_ , volume 3, pages 267–358. Now Publishers Inc, 2010. 

- [46] John Muellbauer. Housing and the macroeconomy: Inflation and the financial accelerator. _Journal of Money, Credit and Banking_ , 47(S1):51–58, 2015. 

- [47] Alberto Musso, Stefano Neri, and Livio Stracca. Housing, consumption and monetary policy: How different are the us and the euro area? _Journal of Banking & Finance_ , 35(11):3019–3041, 2011. 

- [48] M Hashem Pesaran and Ron Smith. Estimating long-run relationships from dynamic heterogeneous panels. _Journal of Econometrics_ , 68(1):79–113, 1995. 

- [49] Monika Piazzesi and Martin Schneider. Housing and macroeconomics. In John Taylor and Harald Uhlig, editors, _Handbook of Macroeconomics_ . Elsevier, 2016. 

- [50] Roberto Rigobon and Brian Sack. The impact of monetary policy on asset prices. _Journal of Monetary Economics_ , 51(8):1553–1575, 2004. 

- [51] Dirk Schoenmaker. Macroprudentialism. _VoxEU.org eBook_ , 2014. 

- [52] Robert J Shiller. _Irrational exuberance_ . Princeton University Press, 2005. 

- [53] Christopher A Sims. Macroeconomics and reality. _Econometrica: Journal of the Econometric Society_ , pages 1–48, 1980. 

ECB Working Paper 2073, June 2017 

38 

- [54] Todd Sinai and Nicholas S Souleles. Owner-occupied housing as a hedge against rent risk. _The Quarterly Journal of Economics_ , 120(2):763–789, 2005. 

- [55] Harald Uhlig. What are the effects of monetary policy on output? Results from an agnostic identification procedure. _Journal of Monetary Economics_ , 52(2):381–419, 2005. 

- [56] Susan Wachter. The housing and credit bubbles in the United States and Europe: A comparison. _Journal of Money, Credit and Banking_ , 47(S1):37–42, 2015. 

- [57] Jeromin Zettelmeyer. The impact of monetary policy on the exchange rate: evidence from three small open economies. _Journal of Monetary Economics_ , 51(3):635–652, 2004. 

ECB Working Paper 2073, June 2017 

39 

##### **Acknowledgements** 

We would like to thank Chiara Osbat, Carlos Montes-Galdon, Michele Lenza, Thomas Westermann, and participants to the ECB-DED and Birkbeck seminar for useful comments and suggestions. Part of this project was written during Andrea’s traineeship at the European Central Bank, Prices and Costs Division. He would like to thank the staff members for their warm hospitality. The usual disclaimers apply. 

##### **Andrea Nocera** 

Birkbeck, University of London, United Kingdom; email: a.nocera@mail.bbk.ac.uk 

##### **Moreno Roma** 

European Central Bank, Frankfurt am Main, Germany; email: moreno.roma@ecb.int 

##### **© European Central Bank, 2017** 

Postal address 60640 Frankfurt am Main, Germany Telephone +49 69 1344 0 Website www.ecb.europa.eu All rights reserved. Any reproduction, publication and reprint in the form of a different publication, whether printed or produced electronically, in whole or in part, is permitted only with the explicit written authorisation of the ECB or the authors. This paper can be downloaded without charge from www.ecb.europa.eu, from the Social Science Research Network electronic library or from RePEc: Research Papers in Economics. Information on all of the papers published in the ECB Working Paper Series can be found on the ECB’s website. ISSN 1725-2806 (pdf) DOI 10.2866/894992 (pdf) ISBN 978-92-899-2795-6 (pdf) EU catalogue No QB-AR-17-085-EN-N 

