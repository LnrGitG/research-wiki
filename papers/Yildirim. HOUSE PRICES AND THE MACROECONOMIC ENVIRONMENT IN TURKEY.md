---
title: Yildirim. HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY
type: paper
source_pdf: raw/papers/Yildirim. HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY.pdf
converted: 2026-08-18
---

ECONOMIC ANNALS, Volume LXII, No. 215 / October – December 2017 UDC: 3.33 ISSN: 0013-3264 

**<u>https://doi.org/10.2298/EKA1715081Y</u>** 

## _Mustafa Ozan Yıldırım* Mehmet İvrendi**_ 

# **HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY: THE EXAMINATION OF A DYNAMIC RELATIONSHIP** 

**ABSTRACT:** _The aim of this paper is to examine the dynamic relationship between house prices, income, interest rates, housing permits, and share prices in Turkey, using Structural Vector Autoregressive (SVAR) models. This paper uses both monthly and quarterly data for the Turkish economy and applies four different SVAR models to reveal this dynamic relationship over the 2003–2016 period. The results show statistically significant and substantial relationships between the variables. The analysis also shows that house prices and housing_ 

_permits as housing market variables are very sensitive to monetary policy and income shocks. The key finding of the study for policymakers is that a change in mortgage rates is the factor that most changes house prices. The study also shows that the housing market plays an important role in transferring monetary policy to the real economy in Turkey._ 

**KEY WORDS:** _House Prices, Macroeconomic Shocks, Turkish Housing Market, Structural VAR_ 

### **JEL CLASSIFICATION:** R31, E44, C32 

> * Department of Economics, Pamukkale University, Turkey. moyildirim@pau.edu.tr 

> ** Department of Economics, Pamukkale University, Turkey. mivrendi@pau.edu.tr 

81 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

#### **1. INTRODUCTION** 

In recent years, due to rising house prices, and following the financial crisis in the US and its effect on the US economy and other economies worldwide, academics and policymakers began to analyze the interaction between house prices and macroeconomic policies, and the underlying factors behind this interaction. Because of the effect of the housing market on other sectors of the economy, studies of it in developed countries increased rapidly after the 2008 financial crisis. The substantial role of housing markets in the monetary policy transmission mechanism affects and shapes many macro-economic variables. For this reason, house markets attract great interest in almost all countries. 

Many economists recognize the fact that house prices in developed countries, notably the US, are experiencing a rapid and historic rise. Since the 1990s many developed countries (Japan being an exception) have witnessed a spike in house prices under favorable macroeconomic conditions. From the end of 1990 to the second quarter of 2007, real house prices rose by approximately 60% in the USA, 40% in the euro area, 55% in Canada, and 135% in the UK. Real house prices fell drastically after the financial crisis, but the upward trend had resumed by the end of 2012. Many studies have investigated the causes of housing market booms and have discussed how to use monetary policy to stabilize housing markets (see Mishkin 2007; Elbourne 2008; Bjornland and Jacobsen 2010; Jarocinski and Smets 2008). 

Since the 1990s the housing market boom in Turkey has been much bigger than in the USA, the euro area, Canada, the UK, and most other industrial countries. Therefore, this study is an example of an extreme case. House prices in Turkey increased by 160% between 2009 and 2016 and have risen by over 230% since 2003, according to the REIDIN House Price Index, as shown in Table 1; much more sharply than consumer, agricultural, and industry prices. 

82 

HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

**Table 1.** Growth Rates of Selected Sectors for Turkey and the Rate of Price Increases 

|**Period**|**Pri**|**ces gr**<br>**(**|**owth ra**<br>**%)**|**te**|**Real**|**growth**<br>**(%)**|**rate**|**Sha**|**re in G**<br>**(%)**|**DP**|**Economic**<br>**Growth**<br>**(%)**|
|---|---|---|---|---|---|---|---|---|---|---|---|
||**HPI**|**Agr.**|**Man**|**CPI**|**Cons**|**Agr**|**Man**|**Cons**|**Agr.**|**Man.**||
|**2003–**|29|69|55|70|7.9|1.2|7.0|6.0|10.1|23.3|5.9|
|**2008**||||||||||||
|**2009–**|160|77|75|79|3.6|3.4|4.2|5.7|9.3|23.9|3.8|
|**2016**||||||||||||
|**2003–**|232|199|172|203|5.6|2.3|5.5|5.8|9.7|23.7|4.7|
|**2016**||||||||||||



**Source:** Turkey Statistical Institute, Central Bank of Republic of Turkey **HPI:** House Price Index, **Agr:** Agricultural Prices, **Man** : Manufacturing Prices, **CPI** : Consumer Price Index, **Cons:** Construction Sector 

Table 1 also presents historical prices in the agricultural and industrial sectors, their real growth rates, and their share in the national income of Turkey. The periodic classification is made considering the macroeconomic effects of the financial crisis. While economic growth averaged 5.9% from 2003 until the financial crisis, it fell to 3.8% in the post-crisis period. The growth rate for the entire period examined in this paper is 4.7%. The slowdown in economic growth is also observed in the construction and industrial sectors, where it fell from 7.9% to 3.6% and from 7.2% to 4.2%, respectively. As can be seen from Table 1, prices in the housing, agricultural, and industrial sectors increased by 232%, 199%, and 172% in nominal terms for the period 2003–2016. The real increase in house prices in the subperiod 2009–2016 was more than twice compared to the agricultural and industrial sectors, reaching 80%, while between 2003 and 2016 the real increase is around 30%. The increase in house prices in Turkey seems to be largely due to significant declines in real mortgage rates in recent years, increased housing construction costs, the number of credit users, asset demand, and urban transformation. However, the share of the construction sector in the national income remained at around 5.8% throughout the period 2003–2016. This share was 4.2% in the USA and 5.4% in the EU-28 (Eurostat 2015). 

These statistics suggest that the housing market plays an important role in Turkey’s economy. The question is, what are the factors that affect housing prices and, especially, what is the role of monetary policy in this market? This 

83 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

paper aims to reveal the role of monetary policy, housing investment (permits), equity prices, income, and inflation on housing prices using the Structural Vector Autoregression (SVAR hereafter) models developed by Bernanke (1986), Sims (1986), and Blanchard and Quah (1989). 

This study differs from the existing literature in Turkey in the following ways. First, it includes both monetary policy and macroeconomic variable shocks when investigating the determinants of house prices, using different SVAR models to reveal the most effective variables. Second, it uses two different data sets, the newest and longest house price data generated by REIDIN. Third, it investigates the relationship between the variables of interest using both quarterly data (covering 2002:Q1–2015:Q3) and monthly data (from January 2003 to November 2016). This study also differs from the existing housing literature in that it is an example of an extreme case regarding the boom in the housing market. Our findings show that the housing market plays an important role in the monetary policy transfer mechanism in Turkey. Monetary shocks have a direct impact on house prices via the mortgage rate channel. Furthermore, the results reveal that housing permits respond systematically to changes in economic activity. However, the strength and timing of the response vary from one model to another. 

The remainder of this paper is organized as follows. Section 2 presents the broad literature on the relationship between housing and the macroeconomy. Section 3 gives detailed information about the estimated model and variables used in this paper. Section 4 discusses the empirical findings, and the conclusions are presented in the last section. 

#### **2. LITERATURE REVIEW** 

Although in recent years many studies have modelled the relationship between housing market and the macroeconomy, this paper relates to recent work on the interaction between housing-related variables, monetary policy, and the macroeconomy. In these studies the various time series analysed are used as econometric methods, and the use of SVAR models has become widespread. 

Recently, a large body of literature in economics has tried to reveal the different nexus between housing sector activity and the rest of economy, including monetary and fiscal policy. Vargas-Silva (2007) finds that US housing investment and prices are negatively affected by contractionary monetary policy 

84 

##### HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

shock, while Iacoviello (2000), Guilidori (2004), and Bulligan (2009) show that in most European countries, monetary policy shocks have a significant impact on house prices in the long run. Baffoe-Bonnie (1998) investigates the dynamic effects of monetary policy and macroeconomic variables on house prices and housing sales at both the regional and national level. His findings show that macroeconomic variables like mortgage rates, money supply, and employment effect house prices and housing sales. In a similar vein, Apergis (2003) also reveals that mortgage rates, inflation, and employment are the most important explanatory variables regarding the fluctuation in real house prices. Wadud et al. (2012) show that in Australia tight monetary policy significantly reduces housing activity but has no significant negative impact on house prices. They also reveal that house production and real house prices react to shocks arising from housing demand and supply. 

The nexus between house prices and monetary policy transmission has also been widely investigated. Bjornland and Jacobsen (2010) examine the role of house prices in the monetary transmission mechanism and show that unexpected changes in interest rates in Norway, Sweden, and the UK have a rapid impact on house prices. Monetary policy that increases interest rates by 1% results in house price decreases of 3%–5%, according to the time and the country. Elbourne (2008) analyses the impact of the monetary transmission mechanism on house prices for the United Kingdom. The results show that a 1% increase in interest rates reduces house prices by 0.75% and house sales by 0.4%. 

Musso et al. (2011) study the linkages between the housing market and the macroeconomy for the US and the euro area, looking at the three basic structural shocks which affect the housing market: monetary policy, credit supply, and housing demand shock. They find that in the two economies there are more housing market similarities than differences, and that monetary policy shocks in the US play a stronger and determinant role in the housing market. Another finding shows that credit supply shocks are more important in explaining house price fluctuations in the euro area. Robstad (2017) extends the Bjørnland and Jacobsen (2010) model by adding the household loan amount and analyses the impact of monetary policy shocks on house prices and credit. The results show that although monetary policy shocks significantly affect house prices they have little impact on household credit loans. 

85 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

Besides the VAR/SVAR approach, which investigates the dynamic relationship between the housing market, macroeconomic variables, and monetary policy, there are other methods that studies in the literature use. Gupta et al. (2010) examine the impact of monetary policy on house prices using the Factor Augmented Vector Autoregressive (FAVAR) method for South Africa and divide the housing market into five segments such as middle, luxury and affordable segments. They show that the increase in real house prices is a negative response to positive monetary policy shock, but these reactions change from region to region and differ by housing category. The responses in the luxury, large–medium, and middle categories are much higher than those in the small, medium, and low-budget categories. Jarocinski and Smets (2008) focus on the role of housing investment and prices in explaining business cycles for the US using the Bayesian VAR method. They show that housing demand shocks have a significant impact on housing investment and house prices, but these shocks have limited impact on the growth of the US economy. Goodhard and Hofmann (2008) analyze the relationship between money supply, private sector loan volume, house prices, and economic activity for 17 industrialized countries using Panel VAR. They find that an increase in money supply has a significant effect on house prices, which also increases the number of private loans. Kishor and Marfatia (2017) examine the dynamic relation between house prices and macroeconomic variables in 15 OECD countries. Their findings suggest that only permanent movements in house prices, income, and interest rates are interrelated. Demir and Yıldırım (2017) investigate the convergence of house prices in OECD countries over the 1996-2015 using the system-GMM method. Their findings point that there is a significant house prices convergence process and some macroeconomic variables such as income, construction permits and share prices play an important role for the house price convergences. 

There are few studies on how the housing market and prices relate to the Turkish economy, due to insufficiently regular and reliable housing market data. Coşkun (2016) analyses the impact of house price fluctuations at both micro and macro levels, based on reviewing the literature and case study analysis. His findings show that housing is a very beneficial investment opportunity for Turkish households. He also points out that real returns on housing may vary at the regional market level, depending on adjustments in nominal house price appreciation in different periods. Akkaş and Sayılgan (2015) investigate the causality between house prices and mortgage rates during 2010–2015. They find that there is one-way causality between mortgage rates 

86 

HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

and the house price index. They also show that mortgage rate shocks have a lagged and significantly negative impact on house prices. Akseki et al. (2014) examine the impact of macroeconomic variables on housing market activity in Turkey from 1992 to 2012. They conduct a two-regime MS-VAR model and find that M1 and interbank rate account for a considerable amount of the variation in housing permits. Badurlar (2008), Kargı (2013), and Sarı et al. (2007) find a significant relationship between the housing market and mortgage rates. Hepşen and Kalfa (2009), Halıcıoğlu (2007), and Öztürk and Fitöz (2009) find that housing demand and supply are influenced by variables representing economic activity. 

#### **3. DATA AND MODEL SPECIFICATIONS** 

##### **3.1 Data** 

This paper uses eleven macroeconomics variables relating to the Turkish housing market, with two different data periods. While six of them cover monthly frequency for the period 2003:1 to 2016:11, others are quarterly, from 2002: Q1 to 2015: Q3. All VARs include the following variables: industrial production index ( _ipi_ ), broad money supply<sup>1</sup> ( _ms_ ), house price index ( _hpi_ ), mortgage rates ( _int_m_ for monthly, _int_q_ for quarterly), Borsa Istanbul share price index ( _bist100_ for monthly, _Bist_100_ for quarterly), housing permit ( _permit_m_ for monthly, _permit_q_ for quarterly), gross domestic product ( _gdp_ ), and construction deflator ( _constr_def_ ).<sup>2</sup> The data is all from the Central Bank of the Republic of Turkey (CBRT), except the industrial production index, which is from the Turkish Statistical Institute (TUİK), and the house price index from the REIDIN. All SVAR model variables except quarterly mortgage rates are real values and are used in logarithm. Gross domestic product, the construction deflator, the industrial production index, and the house price index are adjusted for seasonality using the Census X-12 method. 

##### **3.2 Model Specifications** 

The SVAR methodology is used to investigate the dynamic relationship between house prices and the macroeconomy. The structural representation of a VAR model is described in Lütkepohl (2005) as follows: 

> 1 M2 broad money supply is used as a monetary policy indicator. 

> 2 Based on Kılınc and Tunc (2013) the construction deflator is formed from construction investments in GDP. 

87 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 



where<sup>_y_</sup> _t_<sup>is a</sup> _K_  1  vector of observable time series variables, the _Aj_ ' _s_  _j_  1, , _p_  are  _K_  _K_  coefficient matrices, and<sup>_u_</sup> _t_<sup>is K-dimensional white</sup> noise with _ut_  (0,Σ _u_ ). For simplicity, no constant term or seasonal or dummy variables are added to the equation. 

The VAR model in (4.2) will be transformed into the structural VAR model form under the structural constraints expressed by the zero constraints in matrix A. 







Thus, for a proper choice of A,  _t_ will have a diagonal covariance matrix. 

It may be worth reflecting a little on the restrictions required for a unique  matrix A of instantaneous effects. From the relation Σ   ΑΣ _u_ Α and the assumption of a diagonal Σ matrix, we get  _K_  _K_  1  /2 independent equations, that is, all _K_  _K_  1  /2 off-diagonal elements of ΑΣ _u_ Α  are equal to zero. To solve uniquely all _K_ 2 elements of Α we need a set of _K_ 2 equations. They may be set up in the form of restrictions for the elements of A. Clearly, we may want to choose the diagonal elements of A to be unity. This normalization enables us to write the _k_ -th equation of (4.2) with _ykt_ as the left-hand variable. In addition to this normalization, we still need another _K_  _K_  1  /2 restrictions. Such restrictions have to come from nonsample sources. For example, if a Wold causal ordering is possible, where _y_ 1 _t_ may have an instantaneous impact on all the other variables, _y_ 2 _t_ may have an instantaneous impact on all other variables except _y_ 1 _t_ , and so on, then 

88 

HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 



is a lower-triangular matrix. Thus, we have just enough restrictions so that the innovations and the associated impulse responses are just identified. The zeros can also appear in a different arrangement as off-diagonal elements of A. There can also be more than _K_  _K_  1  /2 restrictions. In SVAR modelling it is common that just-identified models are considered. In other words, as few restrictions are imposed as are necessary for obtaining unique impulse responses. 

Generally, in impulse response analysis the emphasis has shifted from specifying the relations between the observable variables directly to interpreting the unexpected part of their changes or the shocks. Therefore, it is not uncommon to identify the structural innovations  _t_ directly from the forecast errors or reduced-form residuals<sup>_u_</sup> _t_<sup>. One way to do so is to think of the forecast errors as</sup> linear functions of the structural innovations. 

In that case, we have the relationship 





Hence, Σ _u_  ΒΣ  Β .<sup></sup> Normalizing the variances of the structural innovations to one, i.e., assuming  _t_  0,<sup>_I_</sup> _K_  , gives 



Due to the symmetry of the covariance matrix, these relationships specify only _K_  _K_  1  /2 different equations and we again need _K_  _K_  1  /2 further relationships to identify all _K_ 2 elements of Β. 

It is also possible to consider both types of restriction of the previous subsections simultaneously. That is, we may consider the so-called AB model, 

89 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 



 1 In this model, from Equation (4.6) we get _ut_  Α Β  _t_ , and hence  1   1' Σ _u_  Α ΒΒ _A_ . Thus, the variance–covariance matrix has _K_  _K_  1  /2 equations, and the two matrices A and B have _K_ 2 elements to estimate. Thus, we need additionally 2 _K_ 2  1 _K_  _K_  1   _K_  3 _K_  1  /2 restrictions to identify all 2 2 _K_ 2 elements of Α and Β at least locally. 

In this paper the SVAR model has 5 x 1 dimensions and requires 10 restrictions on the structural parameters. Recursive (i.e., Cholesky) ordering gives the 10 restrictions imposed on the structural parameters in the benchmark SVAR model. 



According to Cholesky decomposition, matrix A must be identified as a lower triangular matrix and matrix B as the n-dimensional identity matrix. Therefore, it is necessary to consider the ordering of variables. In the general implementation literature the most exogenous variable is placed at the top of the order, under the assumption that it will not be affected contemporaneously by other variables that succeed it. According to this ordering scheme, each variable in the parentheses is not contemporaneously affected by shocks that follow it, but is contemporaneously affected by shocks from preceding variables (İvrendi and Pearce 2014). In all the SVAR models employed in this paper, output ( _ipi_ and _gdp_ ) is not contemporaneously affected by any other variables in the SVAR model, as it is placed at the top of the order. When used in the same method, house prices are affected by all the preceding variables but do not contemporaneously affect them, as they are placed at the bottom of the order. However, in the SVAR ordering defined above, variables are allowed to be affected both by themselves and by other lagged variables. 

90 

HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

**Table 2.** The Ordering of SVAR Models 

|**Variables**|**Model 1**|**Model 2**|**Model 3**|**Model 4**|
|---|---|---|---|---|
|**_gdp_**|X|X|X|+|
|**_ipi_**|+|+|+|X|
|**_ms_**|+|+|X|X|
|_<br>**_int_**<br>**_m_**|+|+|+|X|
|_<br>**_int_**<br>**_q_**|X|X|X|+|
|_<br>**_permit_**<br>**_m_**|+|+|+|X|
|100<br>**_bist_**|X|+|+|X|
|_100<br>**_Bist_**|X|X|X|+|
|**_hpi_**|+|+|+|X|
|_<br>**_constr_**<br>**_def_**|X|X|X|+|
|_<br>**_permit_**<br>**_q_**|X|X|X|+|



Table 2 shows the ordering of the four different SVAR models used in this paper to analyze the interaction between house prices and macroeconomic variables. The _X_ s are variables that are not included in the model, while _+s_ represents the variables that are located in the model. Unlike the first model, model (2) includes share price index in order to investigate the indirect effect of change in the wealth of economic agents on house prices.<sup>3</sup> Model (3) does not include money supply. Model (4) is estimated by using a house price indicator variable, which is different from the other models. The construction deflator calculated by Kılınç and Tunç (2013) is also used in one of the SVAR models discussed below. The first three models are estimated using monthly observations while the fourth model is quarterly. 

##### **3.3 Unit Root Test** 

In this paper, standard Augmented Dickey-Fuller (ADF), Phillips-Perron (PP), and Kwiatkowski–Phillips–Schmidt–Shin (KPSS) unit root tests are performed to determine the stationarity of the series before estimating the reduced VAR model. As can be seen from Table 3, all the series except _permit_m_ and _hpi (_ for monthly _)_ and _int_q_ (for quarterly) appear to be I (1). 

> 3 For the January–September 2015 period, foreign investors’ share of trading volume on the Istanbul Stock Exchange was 22% and the market value share was 64%. (MKK-Stock Market Trends Report 2015) 

91 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

**Table 3.** Unit Root Tests 

||**A**<br>|**DF**<br>|**P**<br>|**P**<br>|**KP**<br>|**SS**<br>|
|---|---|---|---|---|---|---|
||**Level**|**1st Dif**|**Level**|**1st Dif**|**Level**|**1st Dif.**|
|**Monthly**|||||||
|_ipi_|-2.59|-7.02**|-1.93|-29.2**|0.23|0.03**|
|_ms_|-2.98|-6.08**|-2.65|-10.35**|0.79|0.04**|
|_<br>_int_<br>_m_|-3.93**|-|-3.37|-12.39**|0.088**|-|
|_<br>_permit_<br>_m_|<sup>-3.98**</sup>|-|-10.65**|-|0.49|0.01|
|_hpi_|-3.99**|-|-3.28|-9.95**|0.35|0.05**|
|_100<br>_bist_|-2.79|-5.80|-2.55|-10.00**|0.38|0.06**|
|**Quarterly**|||||||
|_gpd_|-2.40|-4.00**|-2.71|-5.79**|0.17|0.06**|
|_<br>_int_<br>_q_|-5.36**|-|-8.47|-|0.06**|-|
|_<br>_permit_<br>_q_|-2.50|-5.86**|-1.19|-15.56|0.20|0.03**|
|_<br>_constr_<br>_def_|-3.40|-7.19**|-2.71|-5.79**|0.22|0.04**|
|_100<br>_Bist_|-2.53|-4.21**|-1.63|-5.29**|0.21|0.04**|



**Note:** ADF and PP reject the null hypothesis that the variables used have unit roots for the alternative hypothesis of stationarity, while the KPSS rejects the null hypothesis that the variables being tested are stationary. Asterisks ** denote significance at the 5% level. Test results are given with trend and intercept in the table. The critical values for ADF, PP, and KPSS are 3.44, –3.49, and 0.14 respectively. 

#### **4. EMPIRICAL RESULTS** 

The SVAR models provide three important findings to interpret the economics results: contemporaneous structural coefficient, impulse-response function, and forecast error variance decomposition. All VAR in this study is estimated using a constant and two lags. The number of lags is determined by Akaike and Schwarz criteria. The estimated coefficients in Tables 4, 5, and 6 show the contemporaneous structural coefficients obtained from the three different models. Most of the coefficients estimating the contemporaneous effect between the variables are statistically significant and consistent with our theoretical expectations explaining the contemporaneous interaction between the variables in the tables. 

92 

HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

**Table 4.** Contemporaneous Structural Coefficients of SVAR Model (1) 

|**SVAR**|**ipi_d1**|**ms_d1**|**int_m**|**permit_m**|**hpi_d1**|
|---|---|---|---|---|---|
|**ipi_d1**|1|0|0|0|0|
|**ms_d1**|-0.275(-1.24)|1|0|0|0|
|**int_m**|1.758 (0.78)|**-6.320 (-7.93)**|1|0|0|
|**permit_m**|**-0.946 (-2.97)**|0.238 (1.78)|-0.004 (-0.41)|1|0|
|**hpi_d1**|-0.136 (-1.65)|**-0.86 (-25.22)**|**-0.005 (-1.97)**|0.02 (1.01)|1|



**Note** : Bold cells show statistically significant coefficient. “d1” presents the stationary variables by taking the first difference. 

Table 4 reports the contemporaneous structural coefficient estimates obtained from estimated SVAR model (1). For example, contemporaneous effects for housing permits can be written as 

_permit_  m_  0.946 _ipi_  d_ 1  0.238 _ms_  d_ 1  0.004 _int_  m_ 

Thus, the contemporaneous effects for the remaining parameters can be stated and interpreted according to this logic. According to the findings of model (1), a 1% increase in the industrial production index ( _ipi_ ) increases housing permits ( _permit_m_ ) by 0.946%. The positive significant effect of _ipi_ reveals that an increase in industrial production will increase housing demand by increasing the income of economic agents. Thus, the number of housing permits will increase. The table 4 reveals that a 1% increase in money supply ( _ms_ ) leads to a 0.86% increase in real house prices. The explanation for this finding is that an increase in money supply lowers interest rates in the money market, which enhances a fall in mortgage rates and therefore a rise in real house prices. Bjørnland and Jacobsen (2010) also find such results when they analyse the role of house prices in the monetary policy transmission mechanism in Norway, Sweden, and the UK. 

Table 4 also shows a statistically significant relationship between mortgage rates ( _int_m_ ) and the house price index ( _hpi_ ). A 1% increase in mortgage rates increases the real house price index by 0.005%. Mortgage rates have two effects on house prices. The first is that an increase in mortgage rates reduces the demand for houses and therefore reduces house prices. The second is that it increases housing construction costs, which in turn increases house prices. The 

93 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

estimated SVAR model reveals that in Turkey the second effect is greater than the first effect. Overall, in this model there seems to be some evidence for the impact of policy variables on the housing market. 

Table 5 reports a similar ordering of the variables in the SVAR model as in Table 5, but the SVAR model in Table 5 includes an additional variable, the Borsa Istanbul share price index ( _bist100_ ), to investigate the share price or wealth effect on the housing market in Turkey. 

**Table 5.** Contemporaneous Structural Coefficients of SVAR Model (2) 

|**SVAR**|**ipi_d1**|**ms_d1**|**int_m**|**permit_m**|**bist100_d1**|**hpi_d1**|
|---|---|---|---|---|---|---|
|**ipi_d1**|1|0|0|0|0|0|
|**ms_d1**|-0.26(-1.15)|1|0|0|0|0|
|**int_m**|0.25 (0.11)|**-6.46(-8.66)**|<br>1|0|0|0|
|**permit_m**|**-1.09 (-3.37)**|0.15 (1.11)|0.007(0.61)|1|0|0|
|**bist100_d1**|0.002 (0.01)|**-0.25(-5.30)**|**0.02 (5.30)**|-0.003(-0.12)|1|0|
|**hpi_d1**|-0.08 (-1.03)|**-0.83(-22.4)**|**-0.008(-2.59)**|0.01 (0.89)|**-0.11(-2.05)**|<br>1|



**Note** : Bold cells show statistically significant coefficient. “d1” presents the variables which are stationary by taking the first difference. 

The theoretical expectation behind the relationship between share prices and housing demand is that rises in stock market returns, via wealth effect channels, increase consumption and housing demand in the economy (Ludwig and Slok 2004); Davis 2010). The results of SVAR model (2) show that the effect of share prices ( _bist100_ ) on the house price index is significant and positive. A 1% rise in the _bist100_ increases the house price index by 0.114%, which is consistent with the theoretical expectation that an increase in the wealth of economic agents affects the demand for housing. In the literature, Sellin (2001) explicitly shows that positive money supply shocks lead to an increase in stock prices. He states that an increase in money supply will increase the demand for money, thus signaling an increase in economic activity. Higher economic activity indicates an increase in stock prices due to increasing cash flows into the market. As stated in economic theory, Table 5 presents the significant relationship between money supply ( _ms_ ) and share price index ( _bist100_ ). A 1% increase in money supply increases the demand for shares, and therefore their price, by 0.256%. The reason for this finding is that interest rates and shares are two alternative instruments in the portfolios of financial market participants. 

94 

##### HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

Perhaps one of the most striking results is that the impact of mortgage rates ( _int_m_ ) on share price ( _bist100_ ) is negative. Table 5 reports that a 1% increase in mortgage rates decreases the _bist100_ by 0 _._ 022% _._ The implication of this result is that when the mortgage rate and/or market rate rises the economic agents take their savings from the stock market and put them into alternative risk-free interest rates, which is probably the relationship between mortgage rate and _bist100_ that the table reports. Table 5 also shows that the house price index is contemporaneously affected by changes in money supply and mortgage rates, as in the previous model. It is also shows that the effect of industrial production on housing permits is statistically significant and positive. The effect is that a 1% increase in the industrial production index increases housing permits by 1.09%. An increase in industrial production is an indicator of a rise in wealth and hence a rise in the demand for houses and permits. 

**Table 6.** Contemporaneous Structural Coefficients of SVAR Model (3) 

|**SVAR**|**ipi_d1**|**int_m**|**bist100_d1**|**permit_m**|**hpi_d1**|
|---|---|---|---|---|---|
|**ipi_d1**|1|0|0|0|0|
|**int_m**|0.547 (0.22)|1|0|0|0|
|**bist100_d1**|-0.062 (0.55)|**0.010 (2.83)**|1|0|0|
|**permit_m**|**-1.038 (-3.37)**|0.009 (0.94)|0.094 (0.44)|1|0|
|**hpi_d1**|**-0.414 (-2.42)**|**-0.041 (-7.88)**|**-0.529 (-4.61)**|**0.098(-2.34)**|1|



**Note** : Bold cells show statistically significant coefficient. “d1” presents the variables which are stationary by taking the first difference. 

Table 6 presents the findings of the SVAR model which excludes money supply. In the estimation of SVAR model (3) the ordering of _bist100, permit_m,_ and _hpi_ has changed, but this does not change the conclusion regarding the importance of house prices in the ordering. One of the important results of model (3) is that, unlike the two previous models, the coefficient of industrial production index on house price index is found to be statistically significant with the expected positive sign. A 1% increase in industrial production raises the real house price index by 0.41%. This result is expected, since an increase in economic activity is expected to lead to an increase in the economic agent's demand for houses. 

The other important relationship that this model captures is that housing permits have a negative effect on the house price index. Since housing permits are an indicator of future housing supply, a 1% increase in housing permits reduces house prices by 0.09%. This finding can be interpreted as market 

95 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

participants viewing a rise in housing permits as an indicator of a rise in future house supply and postponing their current demand for houses, which reduces house prices. Table 6 also reports that the effect of industrial production on housing permits is statistically significant with the expected positive sign. As in all estimated models in this study, the relationship between mortgage rate (generally all interest rates) and stock prices is, as expected, statistically negative, implying that stocks and interest are two alternative instruments in economic agents’ portfolio assets. The effect of share price index on housing prices as found in model 3 is positive and statically significant, as expected. 

In the analysis of the relationship between house prices and macroeconomic variables, the construction deflator that Kılınç and Tunç (2013) develop and use in their paper is included in the fourth SVAR model. Although the findings of the model are not presented here<sup>4</sup> , they reinforce the findings obtained from the earlier three models. 

The findings obtained from the models are similar to the results of other studies that investigate Turkey’s housing market. The effect of changes in money supply on house prices obtained in this paper is similar to that of Sarı et al. (2007) and Ergeç and Taşdemir (2008). The finding that increasing house prices change money supply shocks, which lower mortgage rates, is also consistent with the findings of Akkaş and Sayılgan (2015). This paper also reveals that economic agents’ increased housing demand leads to an increased number of housing permits, in line with the results of Öztürk and Fitöz (2009) and Badurlar (2008). Tables 4, 5, and 6 also provide strong results regarding the impact of monetary policy on housing market variables. As with other assets, house prices are affected by changes in interest rates, which are highly correlated with mortgage rates. 

##### **4.1 Impulse Response Functions** 

Figures 1, 2, and 3 plot the impulse response functions predicted by the SVAR models in this paper. In all models, the bootstrap CIs are obtained using Hall’s (1992) percentile intervals. Hall’s CIs are based on 1000 bootstrap replications. In all figures the solid line indicates the point estimate and the dashed lines represent 95% confidence intervals. Of all the impulse responses reported in Figures 1, 2, and 3, only the impulse response of housing market variables ( _hpi,_ 

> 4 The results are available upon request. 

96 

##### HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

_permit_m_ ) and mortgage rate ( _int_m,)_ to money supply and other macroeconomic shocks are interpreted below. 

First, consider the impact of a one-standard-deviation positive shock to money supply on the house price index. The shock is defined as an exogenous and unexpected rise in money supply. Other shocks are also defined in the same vein for other variables. The effect of one standard deviation of the money supply on house price index as shown in Figures 1 and 2 is positive and statistically significant (within the confidence intervals; confidence intervals do not include zero). This shock lasts approximately two months and dies out later. It is important to point out that these responses are both statistically significant and of strong magnitude, even though short-lived. An indicator of the importance of this result is that it can be said that monetary policy alone affects house prices in the short term in Turkey. As theoretically expected, industrial production ( _ipi_ ) and gross domestic product ( _gdp_ ) shocks appear to have a slight and short-lived positive significant effect on house prices. These house price index responses appear to be compatible with the theory because increased income stimulates higher house demand, leading to a higher house price index. 

Figures 2 and 3 plot the effect of a share price shock on the house price index in Turkey. The timing and strength of the response to a stock price shock vary between models. In Figure 3 the effect of a share price shock on house prices is found to be both statistically and quantitatively significant and lasts three months after the initial shock. However, in Figure 2 the effect of a share price shock on house prices is not statistically significant until it dies out. Thus, the impact of share price on house prices is inconclusive. Figures 1, 2, and 3 show that a mortgage rate shock significantly reduces the number of new houses permitted not in the short term but in the medium term. Initial effects are not statistically significant in Figures 1, 2, and 3, but are significant after 2 months in Figure 3 and marginally significant after 6 and 5 months in Figures 1 and 2 respectively. Overall, the effect is negative in the medium term. This finding is consistent with the standard theory that emphasizes the existence of a negative relationship between interest rates, housing demand, and housing supply. The effects of mortgage shock on housing prices and permits are negative and only marginally significant. 

Figures 1–3 also show that an unexpected shock to the industrial production index significantly influences housing permits for at least one month, and then quickly falls to its baseline level. Figures 1–2 indicate that mortgage rates 

97 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

( _int_m_ ) have a negative but insignificant impact on house prices. In Figure 3, mortgage rate shocks have a positive and statistically significant effect on house prices. This unexpected relationship can be explained as follows: economic agents may create an expectation that inflation will increase after interest rates rise. So, with general price increases in the economy, rising house prices may lead economic agents to have a hedging effect that protects their wealth against inflation. As a result, house prices may rise due to increase in housing demand. 

98 

HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 





































































99 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 





































































100 

HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 





































































101 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

##### **4.2 Forecast Error Variance Decomposition** 

To access the quantitative importance of a structural shock on the other variables in the SVAR models discussed so far, Tables 7–9 present the variance decomposition of forecast errors of the housing-related variables ( _house prices, housing permits_ ) and mortgage rates. The idea is to show the percentage of the fluctuation in one variable referable to other variables at selected time horizons. The selected time horizon for this study is 20 periods. The variance decompositions reveal the portion of the variance in the prediction for each variable in the system that is attributable to its own shocks, and to shocks to other variables in the system. 

Thus far, this paper has tried to expose the dynamic effect of house prices and macroeconomic variables. This part of paper aims to investigate the following question: In what proportion do the different shocks contribute to the variance in house prices and other macroeconomic variables? To answer this question, Table 7-9 report the forecast error variance decomposition. The tables show the contribution of unexpected shocks to macroeconomic variables in the variance of mortgage rates ( _int_m_ ), housing permits ( _permit_m_ ), and house price ( _hpi_ ). 

**Table 7.** Variance Decomposition of SVAR Model (1) 

|**Variable**||**_int_m_**||**_p_**|**_ermit__**|**_m_**||**_hpi_**||
|---|---|---|---|---|---|---|---|---|---|
|**Period**|**1**|**5**|**20**|**1**|**5**|**20**|**1**|**5**|**20**|
|**(Month)**||||||||||
|**_ipi_**|0.00|0.01|0.01|0.04|0.07|0.06|0.02|0.03|0.03|
|**_ms_**|0.28|0.38|0.41|0.02|0.04|0.12|0.84|0.80|0.79|
|**_int_m_**|0.72|0.62|0.58|0.00|0.01|0.06|0.00|0.02|0.02|
|**_permit_m_**|0.00|0.01|0.01|0.93|0.85|0.74|0.00|0.02|0.03|
|**_hpi_**|0.00|0.00|0.00|0.00|0.02|0.02|0.14|0.13|0.13|



**Note:** Due to rounding of numbers, values in each column sum to 100% approximately. 

Firstly, the findings imply that monetary policy shocks (i.e., _money supply_ ) do have important effects on the housing market variables in Turkey. Tables 7 and 8 show that the contribution of money supply ( _ms_ ) shocks accounts for a larger fraction of the total variance in the real house price index ( _hpi_ ) than variations produced by shocks to other macroeconomic variables. At the end of 20 

102 

##### HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

months, approximately 80% of variance in house prices comes from money supply shock. In both model (1) and model (2), 13% of the variation in real house prices can be explained by its own innovations. These results again support the finding that money supply shocks are significantly responsible for house price stability in Turkey. Compared to monetary policy shocks, industrial production ( _ipi_ ), mortgage rate ( _int_m_ ), housing permit ( _permit_m_ ), and share price ( _bist_100_ ) shocks have a rather weak effect on house prices. 

Tables 7 and 8 also present the variance decomposition of the variables in SVAR model (1) and SVAR model (2), respectively. Even though initially money supply shocks do not contribute significantly to variation in housing permits, after 20 months they account for an important portion: 12% and 14% in Tables 7 and 8, respectively. Industrial production and mortgage rate shocks account for very little of the variance (6% in each table). Likewise, real house price shocks do not seem to be important driving factors for housing permits. The mortgage rate ( _int_m_ ) is widely accounted for by own shocks. After 20 months, money supply shocks explain a large fraction (41% and 37%) of the variation in mortgage rates. Interestingly, share price shocks ( _bist100_ ) account for 10% of the variation in mortgage rates in Table 8. 

**Table 8.** Variance Decomposition of SVAR Model (2) 

|**Variable**||**_int_m_**||**_p_**|**_ermit__**|**_m_**||**_hpi_**||
|---|---|---|---|---|---|---|---|---|---|
|**Period**|**1**|**5**|**20**|**1**|**5**|**20**|**1**|**5**|**20**|
|**(Month)**||||||||||
|**_ipi_**|0.00|0.01|0.01|0.06|0.07|0.06|0.01|0.03|0.03|
|**_ms_**|0.32|0.36|0.37|0.02|0.05|0.14|0.85|0.79|0.78|
|**_int_m_**|0.68|0.53|0.50|0.00|0.02|0.07|0.00|0.02|0.02|
|**_permit_m_**|0.00|0.00|0.01|0.92|0.81|0.69|0.00|0.02|0.02|
|**_bist100_**|0.00|0.10|0.10|0.00|0.03|0.02|0.00|0.02|0.03|
|**_hpi_**|0.00|0.00|0.00|0.00|0.02|0.02|0.13|0.13|0.13|



In both models, money supply shocks do not appear to indicate that mortgage rate shock explain a significant portion of the variation in real house prices at any forecast horizon. For example, at a forecast horizon of 20 months, mortgage 

103 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

rates contribute 21% of the variance in real house prices. The second important driving factor for real house prices in Table 9 is share price shock ( _bist100_ ). This accounts for 9% of the variation in real house prices. However, industrial production and housing permits have a weak effect on real house prices. Even after 20 months they only explain between 2% and 3% of the variance in real house prices. 

**Table 9.** Variance Decomposition of SVAR Model (3) 

|**Variable**||**_int_m_**||**_p_**|**_ermit__**|**_m_**||**_hpi_**||
|---|---|---|---|---|---|---|---|---|---|
|**Period**|**1**|**5**|**20**|**1**|**5**|**20**|**1**|**5**|**20**|
|**(Month)**||||||||||
|**_ipi_**|0.00|0.00|0.00|0.06|0.06|0.05|0.02|0.02|0.02|
|**_int_m_**|1.00|0.91|0.89|0.01|0.06|0.17|0.21|0.21|0.21|
|**_bist100_**|0.00|0.06|0.07|0.00|0.02|0.02|0.09|0.09|0.09|
|**_permit_m_**|0.00|0.01|0.03|0.93|0.86|0.76|0.02|0.03|0.03|
|**_hpi_**|0.00|0.01|0.01|0.00|0.00|0.00|0.66|0.66|0.66|



These results<sup>5</sup> indicate that house price shocks play an important role in forming expectations of future house prices. As shown in Tables 7–9, monetary policy shocks ( _money supply_ , _ms_ ) have a significant share in the explanation of forecast error variance decomposition in real house prices. Besides monetary policy shocks, mortgage rate shocks appear to be an important factor that changes real house prices. Interestingly, in all tables, housing permit and economic activity (both _ipi_ and _gdp_ ) shocks do not explain much of the variation in the forecast errors of real house prices for the 2002–2016 period. Their contributions at the end of 20 months are between 2% and 7%. 

#### **5. CONCLUSION** 

This paper presents a dynamic empirical analysis of the relationship between real house prices and macroeconomics variables in Turkey, using contemporaneous structural coefficients, impulse responses, and forecast error 

> 5 The fourth model’s variance decomposition results provide the same findings as the other three models. The results are available upon request. 

104 

##### HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

variance decomposition from various Structural Vector Autoregressive (SVAR) models. The estimated models based on the relationship reveal that money supply shocks, real economic activity (industrial production and output), and housing permit shocks are the main determinants of house price fluctuations in Turkey. According to the findings obtained from all models used in this paper, there is a positive relationship between the industrial production index, which is regarded as a leading indicator of economic growth, and housing permits. This relationship can be interpreted as an increase in industrial production leading to an increase in national income, so that house prices rise due to increased wealth and housing demand. 

The effect of monetary policy shocks on the housing market is analysed using different SVAR models. The findings suggest that in Turkey the effects of monetary policy shocks on the housing market are important. The evidence of a positive relationship between money supply and house prices in Turkey is consistent with the above discussion and conventional wisdom. A theoretical explanation for this finding is that an increase in money supply is expected to reduce all interest rates, including the mortgage rate. These results are supported by the impulse response and variance decomposition analyses. 

It is important to point out that this finding presents an important policy tool for the efficient control of house prices through the effective use of monetary policy. When the share price, which is a sign of economic agents’ wealth in terms of being one of the factors behind housing demand, is included in a SVAR model, an increase in the BIST 100 index increases house prices. This implies that share price is one of the factors that affects house prices. As shown in this study, the finding that an increase in the number of housing permits reduces house prices indicates that housing market participants interpret the increase as an indicator of supply shift in the market, and therefore it leads to a fall in house prices. 

The study also reveals that an increase in the mortgage rate leads to an increase in the house prices used in the analysis, which is consistent with theoretical expectations. This implies that housing loans are an important part of housing cost. This, in turn, raises house prices. One striking finding is that an increase in house prices leads to an increase in the number of housing permits. This is inconsistent with theoretical expectations. Theoretically, an increase in house prices should reduce demand and therefore the number of housing permits. Contrary to this theoretical expectation, the positive relationship that is found 

105 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

between house prices and the number of housing permits can be interpreted as follows. Households in Turkey invest their savings in housing as a way of protecting against inflation, expecting that the increase in house prices will exceed inflation. We demonstrate this in Appendix Graph 1a. The inflation rate shown as Consumer Price Index (CPI) increases by 202% between 2003 and 2016, while the house price index rises 232% in the same period. It is widely observed for some periods in many countries, such as the US, the United Kingdom (UK), and Australia, that investing in housing provides less risk and higher returns than alternative investment instruments such as stocks and interest on savings. 

The study shows that the housing market plays an important role in transferring monetary policy to the real economy. Moreover, monetary shocks have a direct impact on house prices via the mortgage rate channel. The findings of this study are from an economy which is a relatively extreme case of housing price boom compared to the US, the euro area, Canada, the UK, and most other industrialized countries. 

##### **REFERENCES** 

Akkaş, M.E., & Sayilgan, G. (2015). Housing Prices and Mortgage Interest Rate: Toda-Yamamoto Causality Test. _Journal of Economics, Finance and Accounting_ , 2 (4), 572-583. DOI: 10.17261/ Pressacademia.2015414369 

Akseki, U., Çatık, A.N., & Gök.B. (2014). A Regime-dependent Investigation of the Impact of Macroeconomic Variables on the Housing Market Activity in Turkey. _Economics Bulletin_ , 34 (2), pp. 1081–1090. 

Apergis, N. (2003). Housing Prices and the Macroeconomic Factors: Prospects within the European Monetary Union. _International Real Estate Review_ , 6 (1), pp. 63–74. 

Badurlar, İ.Ö. (2008). An Investigation of the Relationship Between House Prices and Macroeconomic Variables in Turkey. _Anadolu University Journal of Social Science_ , 8 (1), pp. 223– 238. 

Baffoe-Bonnie, J. (1998). The Dynamic Impact of Macroeconomic Aggregates on Housing Prices and Stock of Houses: A National and Regional Analysis. _Journal of Real Estate Finance and Economics_ , 17 (2), pp. 179–197. 

106 

##### HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

Bernanke, B.S. (1986). Alternative Explanations of the Money-income Correlation. _NBER Working Paper_ , No 1842, February 1986. 

Bjørnland, C.H., & Jacobsen, D.H. (2010). The Role of House Prices in the Monetary Policy Transmission Mechanism in Small Open Economies. _Journal of Financial Stability_ , 6 (1), pp. 218– 229. Doi: 10.1016/j.jfs.2010.02.001 

Blanchard, O.J., & Quah D. (1989). The Dynamic Effects of Aggregate Demand and Supply Disturbances. _The American Economic Review_ , 79 (4), pp. 655–673. 

Bulligan, G. (2010). Housing and the Macroeconomy: The Italian Case. _In_ de Bandt, O., T. Knetsch, J. Peñalosa and F. Zollino (eds), _Housing Markets in Europe, A Macroeconomic Perspective_ , Springer. 

Coşkun, Y. (2016). Property Prices and Investment: An Analysis for Turkey. _The Journal of the Faculty of Economics and Administrative Science_ , Niğde University, 9 (2), pp. 201–217. 

Demir, C., & Yıldırım, M. O. (2017). Convergence in House Prices across OECD Countries: A Panel Data Analysis. Central European Review of Economic Issues, 20 (1), pp.5-15. doi: 10.7327/ cerei.2017.03.01 

Elbourne, A. (2008). The UK Housing Market and the Monetary Policy Transmission Mechanism: A SVAR approach. _Journal of Housing Economics,_ 17, pp. 65–87. Doi: 10.1016/j.jhe.2007.09.002 

Ergeç, E.H., & Taşdemir, M. (2008). Causality Relations Between the Construction Sector and Monetary Policies in Turkey. _Eskisehir Osmangazi University Journal of Social Science_ , 9 (1), pp. 115–132. 

Eurostat, 2015. _Statistics explained_ . (http://ec.europa.eu/eurostat/statisticsexplained/index.php/ File:Gross_value_added_at_basic_prices,_2005_and_2015_(%25_share_of_total_gross_value_ added)_YB16.png) 

Davis, P.E. (2010). New International Evidence on Asset-Price Effects on Investment, and a Survey for Consumption. _OECD Journal: Economic Studies_ , Volume 2010. 

Goodhart, C., & Hofmann, B. (2008). House Prices, Money, Credit and the Macroeconomy. _Oxford Review of Economic Policy_ , 24(1), pp. 180–205. Doi.org/10.1093/oxrep/grn009 

Guilidori, M. (2004). Monetary Policy Shocks and the Role of House Prices Across European Countries. De Nederlandsche Bank Working Paper, No 15. 

Gupta, R., Jurgilas, M., & Kabundi, A. (2010). The Effect of Monetary Policy on Real House Price Growth in South Africa: A Factor-Augmented Vector Autoregression (FAVAR) Approach. _Economic Modelling_ , 27 (1), pp. 315-323. DOI: 10.1016/j.econmod.2009.09.011 

Halıcıoğlu, F. (2007). The Demand for New Housing in Turkey: An Application of the ARDL Model. _Global Business and Economics Review_ , Volume 9, Issue 1. 

107 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

Hall, P. (1992). Bootstrap Confidence Intervals in Nonparametric Regression. _The Annals of Statistics_ , 20 (2), pp. 695–711. 

Hepşen, A., & Kalfa, N., (2009). Housing Market Activity and Macroeconomic Variables: An Analysis of the Turkish Dwelling Market Under the New Mortgage System. İstanbul University Journal of the School of Business Administration, 38 (1), pp. 38–46. 

Iacoviello, M. (2000). House Prices and The Macroeconomy in Europe: Results from a Structural VAR Analysis. ECB Working Paper 18. 

İvrendi, M., & Pierce, D. (2014). Asset Prices and Expected Monetary Policy: Evidence from Daily Data. _Applied Economics_ , 46 (9), pp. 985–995. DOI 10.1080/00036846.2013.864038. 

Jarocinski, M., & Smets, F.R., (2008). House Prices and the Stance of Monetary Policy. _Federal Reserve Bank of St. Louis Review_ , July /August 2008, 90 (4), pp. 339–65. 

Kargı, B. (2013). Housing Market and Economic Growth Relation: Time Series Analysis Over Turkey (2000-2012). _International Journal of Human Sciences_ , 10 (1), pp. 898–924. 

Kılınç, M., & Tunç, C. (2014). Identification of Monetary Policy Shocks in Turkey: A Structural VAR Approach. TCMB Working Paper, 14/23. 

Kishor, N.K., & Marfatia H.A. (2017). The Dynamic Relationship Between Housing Prices and the Macroeconomy: Evidence from OECD Countries. _The Journal of Real Estate Finance and Economics_ , 54, pp. 237–268. doi:10.1007/s11146-015-9546-8. 

Ludwig, A., & Slok, T. (2004). The Relationship between Stock Prices, House Prices, and Consumption in OECD Countries. _The B.E. Journal of Macroeconomics_ , 4 (1), pp.1–28. 

Lütkepohl, H. (2005). _New Introduction to Multiple Time Series Analysis_ . Springer. 

Mishkin, F.S. (2007). The Transmission Mechanism and the Role of Asset Prices in Monetary Policy. NBER Working Paper 8617. 

MKK, Stock Market Trends Report. (2015). Access (http://www.tuyid.org/files/BIST_Trends_ Report_XV.pdf) 

Musso, A., Neri, S., & Stracca L. (2011). Housing, Consumption and Monetary Policy: How different are the US and the Euro Area? _Journal of Banking and Finance_ , 35 (11), pp. 3019–3041. dx.doi.org/10.1016/j.jbankfin.2011.04.004 

Öztürk, N., & Fitöz, E. (2009). The Determinants of the Housing Sector in Turkey: An Empirical Analysis. _ZKU Journal of Social Sciences_ , 5 (10), pp. 21–46. 

Robstad, O. (2017). House prices, Credit, and the Effect of Monetary Policy in Norway: Evidence from Structural VAR Models. _Empirical Economics,_ January, pp. 1–23. DOI: 10.1007/s00181-0161222-1 

108 

##### HOUSE PRICES AND THE MACROECONOMIC ENVIRONMENT IN TURKEY 

Sarı, R., Ewing, T.B., & Aydın, B. (2007). Macroeconomic Variables and the Housing Market in Turkey. _Emerging Markets Finance and Trade_ , 43 (5). 

Sellin, P. (2001). Monetary Policy and the Stock Market: Theory and Empirical Evidence. _Journal of Economic Surveys_ , 15 (4), pp. 491–541. 

Sims, C. (1986). Are Forecasting Models Usable for Policy Analysis? _Quarterly Review_ , Federal Reserve Bank of Minneapolis, pp. 2–16. 

Vargas-Silva, C. (2008). Monetary Policy and the USA Housing Market: A VAR Analysis Imposing Sign Restrictions. _Journal of Macroeconomics_ , 30 (3), pp. 977–990. dx.doi.org/10.1016/j. jmacro.2007.07.004 

Wadud, M., Bashar, O., & Ahmet, H.J.A. (2012). Monetary Policy and the Housing Market in Australia. _Journal of Policy Modeling_ , 34, pp. 849–863. dx.doi.org/10.1016/j.jpolmod.2012.06.002. 

Received: September 13, 2017 Accepted: December 18, 2017 

109 

_Economic Annals_ , Volume LXII, No. 215 / October – December 2017 

#### **APPENDIX** 

### **Graph 1a.** Price Trends in Turkey 2003–2016 



<!-- Start of picture text -->
350<br>300<br>250<br>200<br>150<br>100<br>50<br>Manufacture Agriculture House Prices CPI<br>Jan‐03 Sep‐03 May‐04 Jan‐05 Sep‐05 May‐06 Jan‐07 Sep‐07 May‐08 Jan‐09 Sep‐09 May‐10 Jan‐11 Sep‐11 May‐12 Jan‐13 Sep‐13 May‐14 Jan‐15 Sep‐15 May‐16<br><!-- End of picture text -->

**Source:** Turkey Statistical Institute, Central Bank of Republic of Turkey 

110 

