---
title: **Lithuanian house price index: modelling and forecasting**
type: paper
source_pdf: raw/papers/Narusevicius. Lithuanian house price index modelling and forecasting.pdf
converted: 2026-07-26
---

# **Lithuanian house price index: modelling and forecasting** 

Occasional Paper Series 

No 28 / 2019 

ISSN 2424-3213 (online) 

Occasional Paper Series No. 28 / 2019 

Laurynas Naruševičius<sup>*</sup> 

Tomas Ramanauskas 

Laura Gudauskaitė 

Tomas Reichenbachas 

## November 2019 

> * Corresponding author: Financial Stability Department, Bank of Lithuania. Email: LNarusevicius@lb.lt. 

2 

© Lietuvos bankas, 2019 

Reproduction for educational and non-commercial purposes is permitted provided that the source is acknowledged. 

Gedimino  pr. 6, LT-01103 Vilnius 

www. lb.lt 

The series is managed by Applied Macroeconomic Research Division of Economics Department and the Center for Excellence in Finance and Economic Research. 

The views expressed are those of the author(s) and do not necessarily represent those of the Bank of Lithuania. 

3 

### **CONTENTS** 

|Abstract .................................................................................................................................................. 5|
|---|
|1. Introduction ........................................................................................................................................ 6|
|2. Discussion about the fundamentals of house price development .............................................................. 6|
|3. Discussion about house price modeling and forecasting .......................................................................... 8|
|4. Dynamics of Lithuanian house price index ............................................................................................. 9|
|5. Fundamentals of the Lithuanian house price index: VECM analysis ........................................................ 10|
|6. Determinants of the house price growth and short term forecasting: ARDL model................................... 16|
|7. Short and medium term forecasting: forecast combination ................................................................... 19|
|References ............................................................................................................................................ 26|
|Appendix A ........................................................................................................................................... 29|
|Appendix B ........................................................................................................................................... 30|
|Appendix C ........................................................................................................................................... 31|



4 

### **ABSTRACT** 

Timely monitoring of the housing market developments in Lithuania is one of the key elements in the analysis framework of the macroprudential authority aiming to contribute to financial stability in Lithuania. In this paper, we addressed three important questions related to Lithuanian house prices, namely, whether house prices are under- or over valuated, which explanatory variables have the biggest impact on the growth of house prices and what the future development of the Lithuanian house price index could be. Three separate modelling and forecasting exercises were performed in order to tackle these questions. The first exercise employs the vector error correction modelling (VECM) approach to assess under- or overvaluation of the house prices. We then use an autoregressive distributed lag model (ARDL) to evaluate which explanatory variables have the biggest impact on house price growth. As the last exercise, we develop a suite of models that are used to forecast future development of the house price index. The analysis presented in this paper may be viewed as a further step towards more formalised modelling and forecasting of the Lithuanian house price index. 

**JEL:** C22, C32, C53, E37, R30 

**Keywords:** House price index, fundamental value, time series models, forecasting, forecast combination 

5 

### **1. INTRODUCTION** 

The Global Financial Crisis showcased how increase in house price volatility may affect real economic activity and induce stress in the financial system. The Lithuanian housing market was very buoyant during the boom years and then declined sharply in 2009. This had huge negative consequences for households with mortgage loans, banks that experienced deterioration of their balance sheets, the construction and real estate sector, and the overall economy. Therefore, timely monitoring of housing market developments in Lithuania is one of the key elements in the analysis framework of the macroprudential authority contributing to financial stability in Lithuania. 

From the macroprudential perspective, there are three main questions regarding house price developments that are important for warranted and timely policy actions. First, policymakers need to assess whether the house prices are in line with their fundamentals and identify periods of under- or overvaluation of house prices. The second crucial question relates to identification of those fundamentals and other major drivers of house price changes. And lastly, policymakers need to form forecasts of future developments of house prices. In this paper, we address all these questions by undertaking three separate modelling and forecasting exercises. The first exercise employs the vector error correction modelling (VECM) approach to assess underor overvaluation of house prices. We then use an autoregressive distributed lag model (ARDL) to evaluate which explanatory variables have the biggest impact on house price growth. As the last exercise, we develop a suite of models that are used to forecast the future development of the house price index. 

We develop a VECM model, which is used primarily to assess the long-term econometric equilibrium relationship between house prices and other macroeconomic variables (namely, real interest rates, construction costs, credit and investment imbalance<sup>1</sup> and household indebtedness indicator), as well as analyse the impact of shocks to fundamental and non-fundamental variables on the house price dynamics. The model could also be used for house price forecast error decomposition, historical shock decomposition, unconditional and conditional forecasting and other analytical purposes. An alternative, ARDL modelling approach allows us to examine a broader array of indicators that can be useful in explaining house price dynamics. The results reveal that interest rates on new loans to households and building permits are among the key factors for changes in house prices, whereas other variables, such as number of housing transactions, house price to income ratio, etc., have a smaller impact on the dependent variable. In the forecasting exercise, various univariate and multivariate time series models are employed to build a suite of models. For robustness checks and in order to reduce model uncertainty we consider several forecast combination approaches that improve forecasting accuracy compared to individual models. We suggest that the combination of forecasts could be used to predict future changes in the Lithuanian housing price index. 

The outline of this paper is as follows: Section 2 provides some theoretical background for housing market modelling. Section 3 contains a brief presentation of relevant empirical literature on house price modelling and forecasting. Section 4 outlines the historical developments of the Lithuanian house price index. Section 5 describes estimation of the fundamental house price. Section 6 provides ARDL modelling results. In Section 7 we describe a suite of models used to forecast the house price index. The last section concludes. 

### **2. DISCUSSION ABOUT THE FUNDAMENTALS OF HOUSE PRICE DEVELOPMENT** 

We begin our analysis by presenting a theoretical framework for housing market modelling. A commonly used theory for the drivers of house prices in the analysis of house prices has been the life-cycle model (see, e.g., Poterba, 1984; Muellbauer & Murphy, 1997; Meen, 2002; Anundsen, 2016). This approach centres on a representative agent that maximises lifetime utility with respect to consumption of housing and composite 

> 1 Ratio of new housing loans to nominal housing investment. 

6 

consumption good. The marginal rate of substitution between these two goods satisfies the following equilibrium condition: 

equilibrium condition: **(1)** 𝑯𝑯 �� 𝑼𝑼 𝒕𝒕 𝒕𝒕 𝒕𝒕 𝒕𝒕 𝑪𝑪 = 𝑷𝑷𝑯𝑯 �(𝟏𝟏−𝜽𝜽 )𝒊𝒊 −𝝅𝝅 + 𝜹𝜹−𝔼𝔼�<sup>𝚫𝚫𝑷𝑷𝑯𝑯𝒕𝒕+𝟏𝟏</sup> 𝒕𝒕 where is the marginal utility of housing goods ( 𝑼𝑼 ), is the marginal utility of composite consumption 𝑷𝑷𝑯𝑯 goods ( 𝐻𝐻 ), represents house prices. Time-varying tax rates, mortgage interest rates, and inflation rate are 𝐶𝐶 𝑈𝑈 𝐻𝐻 𝑈𝑈 denoted by , 𝑡𝑡 , and , respectively. is the housing depreciation rate and ⁄ ] is the expected 𝐶𝐶 𝑃𝑃𝐻𝐻 real capital gain. Equation (1) states that the marginal rate of substitution between housing and other goods is 𝑡𝑡 𝑡𝑡 𝑡𝑡 𝑡𝑡+1 𝑡𝑡 𝜃𝜃 𝑖𝑖 𝜋𝜋 𝛿𝛿 𝔼𝔼[Δ𝑃𝑃𝐻𝐻 𝑃𝑃𝐻𝐻 equal to what it costs to own one more unit of a property, measured in terms of forgone consumption of other goods. 



Market efficiency also requires the following arbitrage relationship to be satisfied in equilibrium: 



where Qt is the real imputed rent on housing services. This implies that price-to-rent ratio is proportional to the inverse of the user cost: 







Equations (4) and (6) are then used as a starting point from which econometric models of house prices are built. In empirical analysis many authors use the semi-logarithmic model to evaluate house price developments: 



where D is households’ debt and the expected sign of the coefficient is: βd > 0 . 

7 

Equations (7) and (8) can be estimated empirically, which would result in the so-called fundamental house price. Large positive and systematic deviations of actual house prices from the estimated fundamental value can be considered as an indication of unsustainable developments (overvaluation) in house prices. 

### **3. DISCUSSION ABOUT HOUSE PRICE MODELLING AND FORECASTING** 

The empirical literature on house price modelling and forecasting consists of two broad streams. One part of the literature tries to estimate the relationship between house price development and other macroeconomic variables or tries to estimate fundamental house prices. The other part of the literature tries to forecast house price development in the future. Even though authors may use similar models, for example, the vector autoregressive model (VAR), the difference is that they put emphasis either on in-sample fit or on out-ofsample forecasting performance. 

Studies examining the fundamental house price usually involve variables from the demand equation, because there is an assumption that the supply of housing is relatively inelastic in the short or medium term. The estimation of the fundamental house price allows one to determine periods of booms and busts in the housing development. In such studies, authors use an error correction model (ECM) or vector error correction model where the level of house prices is often linked to household income, interest rate, mortgage lending, demographic and labour market variables. For example, de Haas & de Greef (2000) use an ECM model for the Dutch housing market and find that house prices depend on bank lending, even controlling for household income, mortgage interest rate, and other important variables. The authors also find that house prices can deviate significantly from their long term fundamental value, and the adjustment process can take a few years. Oikarinen (2008) uses VECM models for Finland’s data and also finds that two-way interaction between house prices and credit is very important because this relationship can amplify the boom-bust cycle in the economy and increase instability in the financial sector. Similarly, Greiber & Setzer (2007) observe that excess liquidity can fuel house prices in the US. 

Other approaches are also used to estimate boom and bust periods or the deviation from the fundamental house prices. For example, Kajuth et al. (2013) apply panel regression for Germany’s administrative districts and take the regression residuals as a measure for deviations of actual house prices from their fundamental equilibrium level. Gerdesmeier et al. (2012) take a less common approach to detect boom and bust episodes in the euro area housing market. The authors apply quantile regression and find that beside variables such as disposable income, user cost rate and unemployment rate, it is useful to include credit variables in the specification as they help explain the boom/bust cycle of house prices. Anundsen (2016) considers four alternative econometric methods (for example, tests based on ADF-test statistic) to construct indicators of housing market imbalances for the US, Finland and Norway. He estimates that only one of the measures indicates imbalances in the Finnish housing market, whereas none of the measures suggest a bubble in Norway. 

Some authors in the literature analyse the relationship between house prices and other determinants in order to estimate the response of the house prices to changes in those variables. Katrakilidis & Trachanas (2012) study dependence of house prices on macroeconomic variables in Greece using asymmetric autoregressive distributed lag methodology. Their results reveal significant differences in the response of house prices to positive or negative changes of the explanatory variables in both the short and long term. Many authors apply some kind of VAR type model to assess the impact of monetary policy shock to house prices. Carstensen et al. (2009) analyse 12 European Union countries using a panel VAR model, Eickmeier & Hofmann (2010) and Gupta et al. (2010) employ a factor-augmented VAR (FAVAR) model to the US and South Africa data, respectively, Jarociński & Smets (2008) use Bayesian VAR models for the US data and Robstad (2014) apply such models for the Norwegian data. Most of the authors conclude that house price response to a monetary policy shock is negative and persistent. In addition, Carstensen et al. (2009) show that in countries with a 

8 

more pronounced reaction of house prices the propagation of monetary policy shocks to macroeconomic variables is amplified. Meanwhile, Gupta et al. (2010) find that responses are heterogeneous across the affordable, middle and luxury segments of the housing market. 

Another broad stream in the literature focuses on the out-of-sample forecasting performance of the models. Authors explore a wide range of models, from univariate models, like the autoregressive moving average model (ARMA) (Barari et al., 2014) or the ARDL model (Rapach & Strauss, 2007), to multivariate models like VAR, BVAR (Das et al., 2011; Gupta & Miller, 2009) or large scale models like dynamic factor models (DFM) (Emiris, 2016), FAVAR models (Gupta et al., 2009) and various other model classes. The choice of variables as predictors for house prices is similar as in the modelling literature, i.e. macroeconomic, monetary, and demographic fundamentals are used in the models. In general, several lessons can be learned from these studies. 

Firstly, taking into account additional variables improves the forecasting accuracy of an autoregressive model. For example, an de Meulen et al. (2011) show that ARDL and VAR models with additional macroeconomic variables outperform autoregressive model. Secondly, Gupta et al. (2009) find that a small scale BVAR model is more accurate than a large scale BVAR model. They conclude that only a few fundamental variables are important for house price developments. 

Furthermore, allowing estimated model parameters to vary over time gives better forecasting performance. Bork and Møller (2015) and Risse and Kern (2016) use dynamic model averaging (DMA) and dynamic model selection (DMS) and conclude that forecasting accuracy improves substantially when the entire forecasting model is allowed to change over time. Similarly, Barcilar et al. (2015), with a smooth transition autoregressive model (STAR), and Kouwenberg & Zwinkels (2014), with a smooth transition VECM model, show that smooth transition models in an out-of-sample forecasting assessment perform better than competing standard static AR or VECM models. 

Lastly, forecast combination can address the issues of unknown data generating process and model uncertainty. Forecast combination is gaining popularity in the empirical studies, where this approach has been found to frequently outperform forecasts from the best-performing model in real time. Such results were found by Drought & McDonald (2011) for New Zealand’s, an de Meulen et al. (2011) for Germany’s and Rapach & Strauss (2007) for US house prices forecasting exercises. 

To summarise, many modern time series modelling and forecasting techniques have been used in the literature to analyse house price development in the past and to predict it in the future. None of the model class appears to be clearly superior to others. In general, the choice of modelling approach and its empirical estimation depends on the research question and on the quality and availability of data. 

### **4. DYNAMICS OF LITHUANIAN HOUSE PRICE INDEX** 

The Lithuanian housing market developments and price index dynamics from the 2000s comprise several characteristic phases. A modern housing market, where banks more actively issued mortgage loans and investors began to participate beside individual buyers, emerged around 2000. The initial phase can be considered to span the period until May 2004 when Lithuania joined the European Union. Following this structural change, consumers, businesses and banks began to form very optimistic expectations with regard to economic progress, improvement in living standards and their rapid convergence to the level of incumbent EU member states. High economic growth bolstered by rising household incomes and strong consumer spending, as well as negative real lending rates and large credit flows directed towards the housing market – all of this contributed to a rapid increase in house prices, which lasted until its peak in Q2 2008 (see Fig. 1). During that period, the annual house price growth averaged 35.3%. The highest quarterly and annual growth figures (21.5% and 64.2%, respectively) were recorded in Q4 2005. The bust of the house prices coincided with the global financial crisis, which severely affected credit supply. Concurrently, general economic 

9 

conditions worsened significantly, denting affordability of housing and leading to a plummeting demand for housing. The house price trough was reached in Q1 2010, and peak-to-trough decline in house prices amounted to 38.5%. The largest negative quarterly change in house price index was recorded in Q1 2009 and equalled 20.0%. 

The post-crisis stagnation phase was between Q1 2011 and Q4 2013, when the house price index increased only by 3%. In Q3 2011, the Bank of Lithuania introduced the Responsible Lending Regulations (RLR), which limited borrowers’ loan-to-value (LTV) and debt service-to-income (DSTI) ratios, as well as the maximum loan duration. RLR restricted unsustainable borrowing which could then translate into house price growth. The most recent phase of development of the Lithuanian house price index, or a more pronounced price recovery phase, spanned the period from Q4 2013 until the end of the sample in Q2 2018. During this period, house prices continually exhibited positive annual growth rates. 

Fig. 1. Development of the Lithuanian house price index: level (left), quarterly growth (centre), annual growth (right) 



<!-- Start of picture text -->
Index, 2015 = 100  Percentages  Percentages<br>140 25 80<br>20<br>120 60<br>15<br>100 10<br>40<br>80 5<br>0 20<br>60<br>-5<br>0<br>40 -10<br>-15<br>20 -20<br>-20<br>0 -25 -40<br>Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1 Q1<br>2002 2005 2008 2011 2014 2017 2002 2005 2008 2011 2014 2017 2002 2005 2008 2011 2014 2017<br>Source: Statistics Lithuania  Source: Statistics Lithuania  Source: Statistics Lithuania<br><!-- End of picture text -->

Due to the strongly expressed boom/bust cycle of the Lithuanian house price index, quarterly and annual growth rates are very volatile which makes modelling and forecasting quite challenging. During the sample period, i.e. from Q1 2002 to Q2 2018, the average quarterly growth rate was equal to 2.2% with a standard deviation of 6.3 p.p. At the same time, the average annual growth rate was equal to 10.4% with a standard deviation of 18.9 p.p. However, after the crisis volatility in the data has considerably decreased. Calculating quarterly and annual growth rates from Q1 2011 to the end of the sample we get the average quarterly growth of 1.2% (with standard deviation of 1.7 p.p.) and the average annual growth of 4.8% (with standard deviation of 3.4 p.p.). High volatility and a change in it could have an impact on confidence intervals of the estimated model coefficients and forecasts. 

### **5. FUNDAMENTALS OF THE LITHUANIAN HOUSE PRICE INDEX: VECM ANALYSIS** 

In this section we develop a VECM model to assess the cointegrating relationship (or a long-term econometric equilibrium relationship) between house prices and other macroeconomic variables, as well as analyse the impact of shocks to fundamental and non-fundamental variables on house price dynamics. The model could also be used for house price forecast error decomposition, historical shock decomposition, unconditional and conditional forecasting and other analytical purposes. 

10 

#### **5.1. ECONOMETRIC MODEL** 

To estimate the VECM model we employ the standard Engle-Granger procedure (Engle & Granger, 1987). First, the cointegrating relationship among a number of I(1), i.e. integrated of order one, variables is estimated by ordinary least squares (OLS): **(9)** 𝟏𝟏𝒕𝒕 𝟏𝟏 𝟐𝟐 𝟐𝟐𝒕𝒕 𝒏𝒏 𝒏𝒏𝒕𝒕 𝒕𝒕 Here is the housing price variable, other 𝒚𝒚 = 𝜷𝜷 + 𝜷𝜷 denote other macroeconomic variables and 𝒚𝒚 + ⋯+ 𝜷𝜷 𝒚𝒚 + 𝜺𝜺 is a stationary error term. Using residuals 1𝑡𝑡 from the estimated cointegrating relationship in dynamic equations of individual 𝑡𝑡 𝑦𝑦 𝑦𝑦′s 𝜀𝜀 variables, one can formulate the error correction model. In matrix notation, it can be written as follows: 𝑡𝑡 𝜀𝜀̂ 𝒑𝒑−𝟏𝟏 **(10)** 𝒕𝒕 𝒕𝒕−𝟏𝟏 𝒊𝒊 𝒕𝒕−𝒊𝒊 𝒕𝒕 ∆𝒚𝒚 = 𝜶𝜶𝜺𝜺� + �𝜞𝜞 ∆𝒚𝒚 + 𝝐𝝐 where ) is a vector of endogenous variables and 𝒊𝒊=𝟏𝟏 denotes a commensurately sized vector of adjustment parameters measuring how individual variables respond to last period’s deviations from 𝑡𝑡 1,𝑡𝑡 2,𝑡𝑡 𝑛𝑛,𝑡𝑡 𝒚𝒚 = (𝑦𝑦 , 𝑦𝑦 , … , 𝑦𝑦 𝑛𝑛× 1 𝜶𝜶 the equilibrium. is an coefficient matrix associated with _i_ -th lag. Parameter _p_ denotes the number of lags in the model’s VAR form. Model variables and the number of lags are chosen so as to ensure that model 𝑖𝑖 𝜞𝜞 𝑛𝑛× 𝑛𝑛 disturbances follow a multivariate normal distribution. Finally, ∆ denotes a difference operator. 𝑡𝑡 **5.2. MODEL VARIABLES AND DATA** 𝝐𝝐 

#### **5.2. MODEL VARIABLES AND DATA** 

Taking the inverse housing demand function as a starting point for our empirical analysis of house price determination, we expect house prices to be positively linked to rent prices, inflation and expectations of future growth of house prices and negatively linked to interest rates, as well as maintenance and depreciation rates. 

Though this inverse housing demand function, or housing user cost approach, forms the basis of much of the empirical research on house price fundamentals, there are some caveats associated with this approach and with interpretation of this relationship as fundamentals. First, “explaining” high house prices by expensive rents may be misleading because rents can also be procyclical and can strongly decline during a downturn in the housing market. Notably, this has been the case in Lithuania. 

Also, the formula suggests that high house prices can be justified by expected future house price growth. Given the element of reflexivity in this formulation, one has to be careful and distinguish whether these expectations are rational and reflect underlying structural developments or they are not fully rational and reflect subjective market sentiment. In fact, one of the most popular definitions of a house price bubble, formulated by Stiglitz (1990), suggests that a bubble exists if the reason that the price is high today is only because investors believe that the selling price will be high tomorrow – when “fundamental” factors do not seem to justify such a price. In this light it is logical in the empirical analysis to replace the unobserved and somewhat vague expectations variable with structural imbalances and other factors that are likely to drive house price growth. At the same time, house price inertia, adaptive expectations and bubble formation tendencies can be modelled by including house price lags in the model. 

Finally, in its pure theoretical form, the housing demand function leaves out credit. In reality, however, house prices and credit are strongly intertwined and it can be difficult to reasonably explain house price dynamics without taking into consideration developments in the credit market. So, if the aim is to explain actual house price dynamics using an empirical model, one should try to incorporate some credit-related variables (even though they are usually regarded as non-fundamental) in the model in addition to those that can be thought of as fundamentals. 

Because of the above-mentioned caveats and data issues, in our empirical analysis we had to depart quite far from the initial theoretical formulation (equation 7). The analysis was affected by the usual problem of short data series. Quarterly data spanned the period from Q4 2004 to Q2 2018 (a total of 55 observations), which 

11 

essentially included one very significant boom-bust cycle. Against the backdrop of huge cyclical variation, there were cases of very strong covariation between house prices and some other variables (e.g. rent prices), rendering a number of other reasonable candidate variables insignificant. With this in mind and given the lack of sufficient quality data on rent prices in Lithuania, we tried to proxy the rent price variable by demographic, household income, housing stock variables and other indicators that could potentially affect conditions in the rental market. However, none of them appeared significant and were therefore left out of the analysis. We tried to proxy unobserved expectations of house price dynamics by consumer and business confidence variables, construction price index, household indebtedness, variables reflecting imbalances between financial capital (housing loans) and physical investment, etc. 

The working version of the VECM model includes five variables: 

- House price index (denoted as hpi) 

- Real (HICP inflation-adjusted) lending rate on housing loans (r) 

- Construction cost price index (ccpi) 

- New housing loans to nominal housing investment ratio (credInv) 

- Existing housing loans to nominal GDP ratio (debtRatio) 

Data series are seasonally adjusted using Census X-13 seasonal adjustment procedure. All variables, except for the real loan rate, enter the model in logs. Application of the augmented Dickey-Fuller test confirms that all variables are nonstationary and integrated of order one. 

#### **5.3. MODEL RESULTS** 

As the first stage of the Engle-Granger procedure, we estimate the cointegrating relationship among selected variables (see Fig. 2). Applying the Engle-Granger test, the null hypothesis of no cointegration can be rejected at 10% significance level. Coefficient signs are as expected: house prices are negatively linked to real lending rates and positively related to all other variables in the cointegrating relationship, indicating that higher house prices are positively associated with higher construction costs, stronger credit flows and larger household indebtedness (see Table A1, Appendix A). The long-run sensitivity of house prices to real lending rates is moderate: a 1 p. p. increase is associated with a 1.1% decline in house price over the long run. Notably, house prices are found to be very sensitive to increases in construction costs, with elasticity of 1.54. 

Fig. 2. Cointegrating relationship: house price index and the fit from the estimated long-run relation (left) residuals from cointegrating relationship (right) 



<!-- Start of picture text -->
0.15<br>4.9<br>0.10<br>4.7<br>4.5 0.05<br>4.3<br>0.00<br>4.1<br>-0.05<br>3.9<br>3.7 -0.10<br>3.5<br>-0.15<br>Q4 Q4 Q4 Q4 Q4 Q4 Q4<br>Q4 Q4 Q4 Q4 Q4 Q4 Q4<br>2004 2006 2008 2010 2012 2014 2016<br>2004 2006 2008 2010 2012 2014 2016<br>House price index Fitted value Residuals<br>Sources: Statistics Lithuania, authors' calculations  Sources: authors' calculations<br><!-- End of picture text -->

Various model selection criteria (Akaike informatation criterion, Bayesian information criterion and the likelihood ratio test) suggest that the optimal number of lags to include in the VAR form of the model is two, which is equivalent to one lag in the VECM form. However, the Ljung-Box test indicates that residuals of the 

12 

house price equation in the resulting VECM model are autocorrelated. Attempting to tackle the problem but at the same time avoiding the need to estimate too many parameters associated with inclusion of additional lags, we tried adding individual lagged (exogenous or endogenous) variables to the model. The residual autocorrelation problem was corrected when we included the fourth lag of the household debt ratio. Thus, our working model is: **(11)** 𝒕𝒕 𝒕𝒕−𝟏𝟏 𝟏𝟏 𝒕𝒕−𝟏𝟏 𝒕𝒕−𝟒𝟒 𝒕𝒕 where , 𝑐 𝑐 , 𝑐 𝑑∆𝒚𝒚 = 𝜶𝜶𝜺𝜺�, 𝑐 + 𝜞𝜞 )∆𝒚𝒚 and + 𝜸𝜸∆𝒅 is the coefficient vector associated with the fourth lag of 𝒃𝒃𝒕𝒕𝑹𝑹𝒃𝒃𝒕𝒕𝒊𝒊𝒃𝒃 + 𝝐𝝐 _debtRatio_ 𝑡𝑡 variable. Since this variable is endogenous, we actually have a restricted VECM model – term 𝑡𝑡 𝑡𝑡 𝑡𝑡 𝑡𝑡 𝑡𝑡 𝒚𝒚 = (ℎ𝑝𝑝𝑖𝑖 𝑐𝑐𝑛𝑛𝑐𝑐 𝑅𝑅𝑑 𝑖𝑖𝑑𝑑 𝑝𝑝𝑖𝑖 , 𝑐𝑐 𝜸𝜸 𝑑 can be equivalently expressed as 4 , where the third column of parameter matrix 4 equals and all other matrix elements are zero. 𝑡𝑡−4 𝑡𝑡−4 𝜸𝜸∆𝑐 𝑅𝑅𝑑 𝑖𝑖𝑑𝑑 𝜞𝜞 ∆𝒚𝒚 𝜞𝜞 Estimation results show that house prices are modestly pulled to the long-term equilibrium as they tend to 𝜸𝜸 

Estimation results show that house prices are modestly pulled to the long-term equilibrium as they tend to correct around 9% of the deviation from the long-term equilibrium in the preceding quarter. The value of the error correction parameter is in line with typical values reported in the literature on house price fundamentals (where they range from ‒0.07 to ‒0.25), though in our case the parameter is not statistically significant. In contrast, the credit-investment imbalance variable ( _credInv_ ) is strongly pushed away from the equilibrium values, suggesting that this imbalance is a significant source of instability in the system. The result is logical, because historically, as Lithuania’s house price bubble inflated, housing loans rose faster than investment and during the bubble deflation phase a drop in new housing loans was stronger than a decrease in housing investment. One more thing to note is that in the house price equation there is a strong autoregressive element – the positive coefficient associated with the lagged change in house prices, sometimes in the literature referred to as the “bubble generator” parameter, is large and significant, indicating inertia of house price movements and arguably a strong role of adaptive market expectations. 

The Granger representation theorem implies that our VECM model can be expressed as a nonstationary reduced-form VAR. This enables us to calculate impulse response functions. Generalised impulse responses of the house price variable to one standard deviation shocks to each variable are shown in Fig. 3. The house price variable is strongly positively affected by shocks to construction costs and the house price itself. The house price response to a change in credit-investment imbalance in the housing market is moderately positive. House prices negatively react to real lending rate and indebtedness shocks. The impulse responses can also be transformed into various multipliers. For example, the cumulative multiplier can be calculated as a cumulative impulse response of the response variable divided by a cumulative response of the shock variable to a shock to itself. As can be seen from Fig. 4, a 1% increase in construction costs is associated with a 1.6% increase in house prices, whereas a 1 p.p. rise in real lending rates leads to a 2% decline in house prices over the long run. 

13 

Fig. 3. Generalised impulse responses of house prices to one standard deviation shocks 



<!-- Start of picture text -->
0.10<br>0.08<br>0.06<br>0.04<br>0.02<br>0.00<br>-0.02<br>-0.04<br>-0.06<br>-0.08<br>-0.10<br>0 2 4 6 8 10 12 14 16 18<br>credInv hpi ccpi<br>debtRatio r<br>Sources: authors' calculations<br><!-- End of picture text -->

Fig. 4. Cumulative multipliers of house prices 



<!-- Start of picture text -->
Percentages<br>2.5<br>2.0<br>1.5<br>1.0<br>0.5<br>0.0<br>-0.5<br>-1.0<br>-1.5<br>-2.0<br>-2.5<br>0 2 4 6 8 10 12 14 16 18<br>credInv hpi ccpi<br>debtRatio r<br>Sources: authors' calculations<br><!-- End of picture text -->

In order to identify structural (orthogonalised) shocks, we apply Cholesky decomposition procedure, which requires ordering variables from most endogenous to most exogenous. Based on the Granger causality analysis and economic considerations, we put the system’s variables in the following order: _credInv_ , _hpi_ , _ccpi_ , _debtRatio_ , and _r_ . Structural shock identification enables us to perform shock decomposition analysis. The forecast error variance decomposition reveals the relative importance of various structural shocks in determining stochastic variation in house prices. Fig. 5 shows that in the very short term the variation in house prices is driven predominantly by structural shocks to the house price variable itself, whereas in the long run a significant fraction of house price variation is explained by structural shocks to construction costs and household indebtedness. 

14 

Fig. 5. House price forecast error variance decomposition 



<!-- Start of picture text -->
1.0<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>0.0<br>0 2 4 6 8 10 12 14 16 18<br>credInv hpi ccpi<br>debtRatio r<br>Sources: authors' calculations<br><!-- End of picture text -->

Historical shock decomposition allows us to decompose the dynamics (more specifically, the change from the values observed at the start of the sample) of a given variable into a deterministic (nonlinear trend) component and the cumulative impact of individual structural shocks. The deterministic components of each variable represent the system’s dynamics in the absence of structural shocks, so they approximate the model’s long-term econometric equilibrium path. It is not the equilibrium or sustainable growth path in a strict economic sense because the trend depends on initial conditions and also on the “nonfundamental” variables included in the system. Nevertheless, the estimates of such trends reflect the variables’ “balanced” paths with regard to the rest of the system – the variables are beaten off of these paths by structural shocks to the system. As can be seen from Fig. 6, in 2006‒2008 house prices rose above their balanced path, then in 2008 and 2009 abruptly fell well below it and starting from 2012 started gradually closing the gap from below. According to the model, house prices were still slightly below their econometric balanced path at the end of the sample, in 2018. 

Fig. 6. Deterministic component (nonlinear trend) of house price dynamics 



<!-- Start of picture text -->
5.0<br>4.9<br>4.8<br>4.7<br>4.6<br>4.5<br>4.4<br>4.3<br>4.2<br>4.1<br>Q2 Q2 Q2 Q2 Q2 Q2 Q2<br>2006 2008 2010 2012 2014 2016 2018<br>House price index<br>Nonlinear deterministic trend<br><!-- End of picture text -->

Sources: Statistics Lithuania, authors' calculations 

The model can also be directly applied for forecasting house prices (and other model variables), adding to the suite of specialised forecasting models described in the sections below. Notably, the model can be used for conditional forecasts and counterfactual analysis, which allows us to analyse the dynamics of the system subject to externally imposed restrictions on paths of selected variables. In this regard, we are specifically interested in assessing the impact of unbalanced credit and investment dynamics on house prices. If we assume a balanced credit and investment dynamics (set _creditInv_ equal to zero), we get the result that excess credit flows may have raised house prices over the analysed period by about 40% (see Fig. 7). 

15 

Fig. 7. Unconditional and counterfactual house price trends 



<!-- Start of picture text -->
5.0<br>4.9<br>4.8<br>4.7<br>4.6<br>4.5<br>4.4<br>4.3<br>Q2 Q2 Q2 Q2 Q2 Q2 Q2<br>2006 2008 2010 2012 2014 2016 2018<br>House price index<br>Unconditional forecast<br>Conditional forecast (with credInv = 0)<br>Sources: Statistics Lithuania, authors' calculations<br><!-- End of picture text -->

### **6. DETERMINANTS OF THE HOUSE PRICE GROWTH AND SHORT TERM FORECASTING: ARDL MODEL** 

In this section, we analyse the potential factors that determine the dynamics of Lithuanian house prices. We employ an ARDL model to evaluate house price changes and to make short term forecasts (up to four quarters). In this section, we follow the work of Rapach & Strauss (2007), who model and forecast the US house price dynamics. 



Furthermore, let ( ) represent potential determinants of house price growth rate. An ARDL model can be written as: 𝑖𝑖,𝑡𝑡 𝒙𝒙 𝑖𝑖= 1, … , 𝑛𝑛 𝒑𝒑 𝒒𝒒 **(13)** 𝒉𝒉 𝒉𝒉 𝒕𝒕+𝒉𝒉 𝒋𝒋 𝒕𝒕−𝒋𝒋 𝒋𝒋 𝒊𝒊,𝒕𝒕−𝒋𝒋 𝒕𝒕+𝒉𝒉 𝐲𝐲 = 𝛂𝛂+ �𝜷𝜷 𝚫𝚫𝒚𝒚 + �𝜸𝜸 𝒙𝒙 + 𝜺𝜺 where ℎ is an error term. In this exercise, the ARDL model parameters were estimated using OLS and the 𝒋𝒋=𝟎𝟎 𝒋𝒋=𝟎𝟎 model is used in two ways. First, we estimate the model with a full data sample in order to determine which 𝑡𝑡+ℎ 𝜀𝜀 variables made the biggest impact on house price growth. Second, equation 13 is used to construct a set of ℎ recursive (expanding estimation window) out-of-sample forecasts of using information available at time . 𝑡𝑡+ℎ Due to short time series, the lag length is set to 0, i.e. only Δyt is included in the equation. The lag length 𝑦𝑦 𝑑𝑑 can vary between 0 and 2. Furthermore, the number of determinants can also vary between one to four 𝑝𝑝 𝑞𝑞 predictors per model. In this way, we estimated a few thousand different ARDL models. 𝑖𝑖,𝑡𝑡 𝒙𝒙 

#### **6.2. EXPLANATORY VARIABLES** 

Data availability in this modelling exercise determined the data sample which covers the period from Q2 2006 to Q2 2018. We include 12 potential explanatory variables of house price growth rate which could be attributed to three main groups. Demand-related variables provide measures of the ability of households to purchase housing: 

16 

- Population 

- Unemployment rate 

- Wages 

- Consumer price index 

- Consumer confidence index 

- House price to income ratio 

Supply-related variables may reflect supply conditions in the housing market with a potential impact on house prices: 

- Building permits 

- Investment in real estate 

- Construction cost index 

- Number of housing transactions 

Meanwhile, bank credit related variables show households’ access to credit for housing purchases: 

- Interest rate on new loans for households 

- New loans for households 

In this modelling exercise the house price index and some of the explanatory variables were seasonally adjusted: wages, building permits, investment in real estate, construction cost index, number of housing transactions. Furthermore, all of the variables were transformed by taking first the differences of log levels to make them stationary, with the exceptions to unemployment rate, house price to income ratio and interest rate (which were taken in levels) and building permits, number of housing transactions and new loans for households (which were taken in log levels). 

In order to reduce the number of ARDL models, sign restrictions were applied on the estimated coefficients. A positive sign restriction was imposed on population, wages, consumer price index, consumer confidence index, construction cost index and new loans for households. A negative sign restriction was imposed on unemployment rate, building permits, investment in real estate and interest rate on new loans to households. The number of housing transactions and house price to income ratio were left unrestricted. 

#### **6.3. MODEL EVALUATION AND COMBINATION** 

All ARDL models were evaluated by their performance in various model accuracy testing procedures. First of all, we estimated all models using the full data sample and kept only those models that have coefficients in accordance with the sign restrictions mentioned above. Then the in-sample fit was examined by the mean absolute scaled error (MASE), sign accuracy, and p-value of the coefficients. Introduced by Hyndman & Koehler (2006), MASE is the mean absolute error of the fitted values, divided by the mean absolute error of the one-step naïve forecast: 



Another model evaluation criterion was based on model performance during a crisis period. We re-estimated models from the start of the sample until Q3 2008 and forecasted four quarters ahead. Then we examined coefficient sign accuracy and retained only those models, which predicted decline in house prices at least in one quarter. 

17 

The last model evaluation criterion was based on model performance in the out-of-sample forecasting exercise. Initially, models were estimated using the data from the training sample, i.e. from Q2 2006 until Q4 2011. Then the short-term (i.e. four quarters ahead) forecasts were calculated. All models were then reestimated on an incrementally expanding (by one quarter) data window to produce a new set of forecasts. The expanding window estimation was repeated until Q2 2017. Once again, we kept only those models that had the average forecast sign accuracy greater than 0.5, i.e. on average at least two times out of four correctly predicted the direction of the development. 

Only models that passed all accuracy testing procedures were used in the further analysis. Since it is not obvious which individual model is best suited for the analysis and short term forecasting, we applied model combination, which provided a way to incorporate information from several models. The model combination allows having more variables as explanatory variables compared to a single model and as noted by Rapach & Strauss (2007) helps improve forecasting accuracy. 



#### **6.4. MODELING RESULTS** 

Empirical estimation provided 18 individual ARDL models that passed all model evaluation criteria. The results from the estimated models were then aggregated into one weighted ARDL model. Fig. 8 shows which explanatory variables had the biggest impact on the deviation from the long term growth of house prices. Four variables were not included in any of the individual models: consumer price index, wages, population and unemployment rate. The figure shows that interest rate is one of the main drivers of house price developments. The low interest rate environment mainly caused the recent increase in house price growth. From the supply side variables, building permits had the biggest impact in the past. All other variables played a lesser role in affecting the dependent variable. The figure also reveals that quite a big part of the house price changes, especially during the crisis, is still left unexplained by the model. This may suggest that the actual decrease in growth could be attributed to changes in perception of the house value which could not be captured by any explanatory variables. Another possible explanation could be that the relationship between house price growth and other variables is more contemporaneous. However, given the forecasting purpose of the model, we could not include higher lags of the explanatory variables in the model. 

18 

Fig.8. Determinants of the house price growth in the past 



<!-- Start of picture text -->
Percentages<br>Unexplained error<br>40<br>House price to income<br>30<br>Construction cost index<br>20<br>10 Consumer confidence index<br>0 Interest rate<br>-10 New loans<br>-20 Number of housing transactions<br>-30<br>Investment in real estate<br>-40<br>Building permits<br>-50<br>Q2 Q2 Q2 Q2 Q2 Q2 Q2 Δyt<br>2006 2008 2010 2012 2014 2016 2018<br>Actual data<br><!-- End of picture text -->

Sources: Statistics Lithuania, authors' calculations 

The combined ARDL model was also used to produce short term out-of-sample forecast. Fig. B1 (in Appendix B) shows the forecasts at different forecasting horizons. The results show that the model tends to overpredict the growth of house prices at the beginning of the forecasting sample. This result may come from the fact that data showed high volatility before and during the crisis, which may affect the size of the coefficients in the individual ARDL models. Nevertheless, at the end of the sample, combined ARDL forecasts are more accurate. Moving forward, we can expect better forecasting performance as a longer data sample will give better estimates of the model coefficients. 

### **7. SHORT AND MEDIUM TERM FORECASTING: FORECAST COMBINATION** 

In this section, we present a suite of models aimed at forecasting the Lithuanian house price index in the short and medium term (up to ten quarters). We explore univariate and multivariate time series models and compare their performance by out-of-sample forecasting accuracy. Thus, this modelling exercise follows a stream of literature that focuses on the forecasting performance of the models. 

#### **7.1. ECONOMETRIC MODELS** 

The starting point of our forecasting exercise is a simple naïve forecast of the log level of the house price index. Thus, our benchmark model assumes that during the forecasting period the level of house price index will remain the same as the last observed value. All other models will be compared to this benchmark model. 

#### **ARMA** 

In a univariate case, the ARMA model is used, which is the most common empirical approach in modelling and forecasting time series data. The classical ARMA( _p, q_ ) model, where and denote the AR and MA orders, can be written as: 𝑝𝑝 𝑞𝑞 **(16)** 𝒕𝒕 𝟏𝟏 𝒕𝒕−𝟏𝟏 𝒑𝒑 𝒕𝒕−𝒑𝒑 𝒕𝒕 𝟏𝟏 𝒕𝒕−𝟏𝟏 𝒒𝒒 𝒕𝒕−𝒒𝒒 where yt is a variable of interest, c is a constant, 𝒚𝒚 = 𝐜𝐜+ 𝝓𝝓 𝒚𝒚 + ⋯+ 𝝓𝝓 is an error term, 𝒚𝒚 + 𝒅𝒅 + 𝜽𝜽 𝒅𝒅 + ⋯+ 𝜽𝜽1 , …, 𝒅𝒅 and 1 , …, are parameters of the model. The model is fitted using the maximum likelihood estimation method. 𝑡𝑡 𝑝𝑝 𝑞𝑞 𝑐𝑐 𝜙𝜙 𝜙𝜙 𝜃𝜃 𝜃𝜃 The house price index is forecasted taking the AR order from 1 to 4 ( ), and the MA order from 0 to 2 ( ). Furthermore, each ARMA model specification is estimated taking house price index in log level, 𝑝𝑝= 1, 2, 3, 4 𝑞𝑞= 0, 1, 2 

19 

quarterly growth rate, and annual growth rate. Overall, 36 different ARMA models were estimated and included in the suite of models. 

#### **VAR** 

Gupta et al. (2009) and an de Meulen et al. (2011) showed that including additional macroeconomic variables improves forecasting accuracy compared to autoregressive models. Therefore, VAR-type models are included in the suite of models for forecasting house price index. The classical VAR model with endogenous variables and lags was suggested by Sims (1980) and can be written as: 𝑛𝑛 𝑝𝑝 **(17)** 𝒕𝒕 𝟎𝟎 𝟏𝟏 𝒕𝒕−𝟏𝟏 𝟐𝟐 𝒕𝒕−𝟐𝟐 𝒑𝒑 𝒕𝒕−𝒑𝒑 𝒕𝒕 where ) is a 𝒀𝒀 vector of endogenous variables, = 𝑩𝑩 + 𝑩𝑩 𝒀𝒀 + 𝑩𝑩 𝒀𝒀 + ⋯+ 𝑩𝑩 𝒀𝒀 0 is a + 𝒖𝒖 vector of constant terms, 1 , 2 , …, 𝑡𝑡 are 1,𝑡𝑡 2,𝑡𝑡 matrices of coefficients and 𝑛𝑛,𝑡𝑡 is a vector of residuals, which follows a multivariate 𝑌𝑌 = (𝑦𝑦 , 𝑦𝑦 , … , 𝑦𝑦 𝑛𝑛× 1 𝐵𝐵 𝑛𝑛× 1 𝐵𝐵 normal distribution, i.e. 𝑝𝑝 . Estimation of the model is done by the ordinary least squares (OLS) and 𝑡𝑡 𝐵𝐵 𝐵𝐵 𝑛𝑛× 𝑛𝑛 𝑢𝑢 𝑛𝑛× 1 forecasting is straightforward (see, e.g., Lütkepohl, 2005). 𝑡𝑡 𝑢𝑢 ~ 𝒩𝒩(0, Σ) 

The house price index is forecasted using seven alternative VAR model specifications (see Table 1). Due to data limitations and following Gupta et al. (2009), who found that small scale VAR-type models are more accurate than large scale models, we explore different specifications which include from four to six variables in the model. All specifications follow the same structure: the house price index is modelled with interest rate, lending to households, macroeconomic and labour market variables. 

Table 1. Estimated VAR model specifications 

|**Specification**|||**Va**|**riables**|||
|---|---|---|---|---|---|---|
|Spec. 1|Real GDP|House price<br>index|Credit to<br>households|Interest rate<br>on loans to<br>households|||
|Spec. 2|Real GDP|House price<br>index|Credit to<br>households|Interest rate<br>on loans to<br>households|HICP||
|Spec. 3|Real GDP|House price<br>index|Credit to<br>households|Interest rate<br>on loans to<br>households|HICP|Unemployment<br>rate|
|Spec. 4|Disposable<br>income|House price<br>index|Credit to<br>households|Interest rate<br>on loans to<br>households|HICP||
|Spec. 5|Disposable<br>income|House price<br>index|Credit to<br>households|Interest rate<br>on loans to<br>households|HICP|Unemployment<br>rate|
|Spec. 6|Real private<br>consumption|House price<br>index|Credit to<br>households|Interest rate<br>on loans to<br>households|HICP||
|Spec. 7|Real private<br>consumption|House price<br>index|Credit to<br>households|Interest rate<br>on loans to<br>households|HICP|Unemployment<br>rate|



As in the case of autoregressive models, each VAR model specification is estimated taking endogenous variables in log levels (except interest rate and unemployment rate which are taken in percentages), quarterly growth rates (interest rate and unemployment rate are taken in quarterly changes) or annual growth rates (interest rate and unemployment rate are taken in annual changes). Furthermore, each specification is estimated taking the number of lags from 1 to 4, i.e. . Overall, 84 different VAR models were estimated and included in the suite of models. 𝑝𝑝= 1, … , 4 

20 

#### **BVAR** 

Even though a VAR model is one of the main tools for macroeconomic modelling and forecasting, the estimation of these models poses certain challenges. The VAR model requires many parameters to be estimated because typically equal lag lengths for all variables are used, including many that are statistically insignificant. The rich parameterisation of VAR models (over-parameterisation problem) brings a risk of overfitting the data, inefficient estimates and possibly large out-of-sample forecasting errors. Consequently, this limits the endogenous variables and the number of lags, which can be included in the simple VAR model to avoid those problems. Litterman (1986) and many other authors used the Bayesian estimation of the VAR model (BVAR) to overcome the over-parameterisation problem. See, for example, Karlsson (2013) for extensive literature on forecasting using Bayesian VAR models. The Bayesian approach suggests a solution to this curse of dimensionality by introducing prior distributions on parameters of interest. According to Karlsson (2013), BVAR models usually show better forecasting performance compared to VAR models estimated with frequentist techniques. 

In Bayesian econometrics, every parameter of interest is treated as a random variable, characterised by some underlying probability distribution. In this study, we employ widely used Minnesota prior distributions (Litterman, 1986). Instead of eliminating lags, the Bayesian estimation imposes restrictions on the coefficients across different lag lengths. Minnesota priors take the fact that more recent values of a data series usually contain more information about the current value of the series than past values. Furthermore, it also takes the fact that past values of a given variable contain more information about its current state than past values of other variables. In this framework, it is assumed that the VAR residual variance-covariance matrix Σ is known and the only object left to estimate is the vector of coefficients . It is assumed that follows a multivariate normal distribution: 𝛽𝛽 𝛽𝛽 𝒊 𝒊 ) **and** ) **(18)** 𝟐𝟐 𝟐𝟐 𝜷𝜷 𝒊𝒊𝒋𝒋 𝜷𝜷𝒊𝒊𝒋𝒋 where 𝑖 denotes the coefficients associated with the lagged dependent variable in each equation of the VAR 𝜷𝜷 ~ 𝓝𝓝(𝟏𝟏, 𝝈𝝈 𝜷𝜷 ~ 𝓝𝓝(𝟎𝟎, 𝝈𝝈 model, 𝑖 represents any other coefficient. The prior variances 2𝑖 and 2𝑖 specify uncertainty about the prior 𝛽𝛽 means. Based on Litterman (1986), for coefficients relating endogenous variables to their own lags, the 𝛽𝛽 𝛽𝛽 𝛽𝛽 𝜎𝜎 𝜎𝜎 variance is given by: **(19)** 𝒊 = �<sup>𝝀𝝀𝟏𝟏</sup> �𝟐𝟐 𝟐𝟐 𝜷𝜷 where 1 is an overall tightness parameter, is the lag considered by the coefficient, and 𝝈𝝈 𝒍𝒍<sup>𝝀𝝀𝟑𝟑</sup> 3 is a scaling parameter controlling the speed at which coefficients for lags greater than 1 converge to 0 with greater 𝜆𝜆 𝑙𝑙 𝜆𝜆 certainty. For parameters related to cross-variable lag coefficients, the variance is given by: = ~~�~~<sup>𝝈𝝈</sup> 𝟐𝟐<sup>𝒊𝒊</sup> � ~~�~~<sup>𝝀𝝀𝟏𝟏𝝀𝝀𝟐𝟐</sup> ~~�~~ 𝟐𝟐 **(20)** 𝟐𝟐 2 2 𝝈𝝈𝜷𝜷𝒊𝒊𝒋𝒋 𝟐𝟐𝒋𝒋 where and denotes the OLS residual variance of the autoregressive models estimated for variables 𝝈𝝈 𝒍𝒍<sup>𝝀𝝀𝟑𝟑</sup> and , and 2𝑖𝑖 represents a cross-variable specific variance parameter. 𝑖𝑖 𝜎𝜎 𝜎𝜎 𝑖𝑖 𝑗𝑗 For exogenous variables (including constant terms), the variance is given by: 𝜆𝜆 ) **(21)** 𝟐𝟐𝒄𝒄𝒊𝒊 𝟐𝟐𝒊𝒊 𝟏𝟏 𝟒𝟒 𝟐𝟐 where 4 is a large variance parameter. In this study, typical values found in the literature for parameters 𝝈𝝈 = 𝝈𝝈 (𝝀𝝀 𝝀𝝀 1 , 2 , 3 and 4 are used, i.e. 1 = 0.1 , 2 = 0.5 , 3 = 1 and 4 = 10<sup>2</sup> . 𝜆𝜆 𝜆𝜆 𝜆𝜆 𝜆𝜆 𝜆𝜆 𝜆𝜆 𝜆𝜆 𝜆𝜆 𝜆𝜆 

21 

Empirical BVAR model estimation follows the same strategy as VAR model estimation. Thus, we take the same seven model specifications and estimate them taking the number of lags from one to four. Overall, 84 different BVAR models were estimated and included in the suite of models. 

#### **BVAR WITH STOCHASTIC VOLATILITY** 

Several authors noted (e.g. Kouwenberg & Zwinkels, 2014) that allowing time-variation in parameters may improve house price forecasting performance. Furthermore, Chan & Eisenstat (2018) analysed US macroeconomic data and found strong support for the time-varying parameter VAR with stochastic volatility (TVP-VAR-SV) compared to a constant coefficient VAR with homoscedastic innovations. However, the authors argue that most of the gains come from allowing for stochastic volatility rather than time variation in the VAR coefficients. Following these results in our analysis, we apply the BVAR model with stochastic volatility (BVARSV) which was initially proposed by Cogley & Sargent (2005) and Primiceri (2005). Thus, we allow for stochastic volatility but BVAR coefficients are left constant. 

In a traditional VAR model it is assumed that the residuals are distributed according to multivariate normal distribution, i.e. . Meanwhile, in the BVAR-SV model, it is assumed that the residuals are independently but not identically distributed across time. Their variance-covariance matrix 𝑡𝑡 Σ is allowed to be 𝑢𝑢 ~ 𝒩𝒩(0, Σ) time varying, hence providing stochastic volatility and introducing heteroscedasticity. It is assumed that Σ can be decomposed into: 𝑡𝑡 **(22)** 𝒕𝒕 𝒕𝒕 where is a lower triangular matrix with ones on the diagonal and non-zero coefficients below the diagonal. 𝚺𝚺 = 𝑭𝑭<sup>−𝟏𝟏</sup> 𝚲𝚲 𝑭𝑭<sup>−𝟏𝟏′</sup> Meanwhile, Λ is a period-specific diagonal matrix of variances, i.e. 𝐹𝐹<sup>−1</sup> diag(Λ 1 𝑡𝑡 �, 2 �) . 1 , 2 , … , are known scaling terms and , , …, are dynamic processes generating the heteroscedasticity of the model. It is assumed that they are 𝑡𝑡 1,𝑡𝑡 2,𝑡𝑡 𝑛𝑛 𝑛𝑛,𝑡𝑡 𝑛𝑛 1,𝑡𝑡 2,𝑡𝑡 𝑛𝑛,𝑡𝑡 ) = (𝑠𝑠̅ exp�𝜆𝜆 𝑠𝑠̅ exp�𝜆𝜆 �, … , 𝑠𝑠̅ exp�𝜆𝜆 𝑠𝑠̅ 𝑠𝑠̅ 𝑠𝑠̅ 𝜆𝜆 𝜆𝜆 𝜆𝜆 characterised by the autoregressive process: **,** ) **(23)** 𝒊𝒊,𝒕𝒕 𝒊𝒊 𝒊𝒊,𝒕𝒕−𝟏𝟏 𝒊𝒊,𝒕𝒕 𝒊𝒊,𝒕𝒕 𝒊𝒊 −1 The parameters of interest to be estimated are: the VAR coefficients 𝝀𝝀 = 𝜸𝜸 𝝀𝝀 + 𝜺𝜺 𝜺𝜺 ~ 𝓝𝓝(𝟎𝟎, 𝝋𝝋 , the elements related to the matrix, the set of dynamic coefficients , the set of 𝑖𝑖 𝛽𝛽 𝑓𝑓<sup>−1</sup> = �𝑓𝑓 : 𝑖𝑖= 2, … , 𝑛𝑛� autoregressive coefficients and the heteroscedasticity parameters 𝑖𝑖,𝑡𝑡 . 𝐹𝐹<sup>−1</sup> 𝜆𝜆= �𝜆𝜆 : 𝑖𝑖= 1, … , 𝑛𝑛; 𝑑𝑑= 1, … , 𝑇𝑇� 𝑖𝑖 𝑖𝑖 Once again, the empirical BVAR-SV model estimation follows the same strategy as VAR model estimation. 𝛾𝛾= {𝛾𝛾 : 𝑖𝑖= 1, … , 𝑛𝑛} 𝜑𝜑= {𝜑𝜑 : 𝑖𝑖= 1, … , 𝑛𝑛} Thus, we take the same seven model specifications and estimate them taking the number of lags from one to four. Overall, 84 different BVAR-SV models were estimated and included in the suite of models. 

#### **7.2. ESTIMATION OF FORECAST ACCURACY** 

In the forecasting exercise, we used the house price index and other Lithuanian data spanning from Q1 2002 to Q2 2018 ( _T = 66_ ). To compute out-of-sample forecasts, the data sample was split into an in-sample period ( _I = 40_ ) and an out-of-sample period ( _O = 26_ ). With a forecast horizon of ten quarters, this allowed evaluating 17 forecasts ( _N = 17_ ). At the start, all models were estimated using data until Q4 2011 and up to ten quarters ahead forecasts of log level of the house price index were made. All models were then reestimated by expanding the training data set by one quarter to produce a new set of forecasts. The expanding window estimation was repeated until Q4 2015, which was the final estimation period. 

The forecasting performance was assessed using several standard forecast evaluation measures. The main measure of forecasting accuracy in this exercise was the root mean squared error (RMSE) of forecasts at particular period ahead, which is defined as: 





22 

where is the h-step ahead forecast, is the actual value at that step, and is the number of forecasts. The forecast accuracy was compared at one-, four-, eight- and ten-quarter-ahead RMSEs across all models. In 𝑛𝑛,ℎ 𝑛𝑛,ℎ 𝑓𝑓 𝑦𝑦 𝑁𝑁 general, the lower RMSE indicates the better forecasting accuracy of the model. 

Another measure for forecasting accuracy is the mean absolute forecast error (MAE) which is defined as: 𝑴 𝑵𝑵 | **(25)** 𝒏𝒏,𝒉𝒉 𝒏𝒏,𝒉𝒉 𝑴𝑴=<sup>𝟏𝟏</sup> �|𝒚𝒚 −𝒇𝒇 In this exercise we calculate the relative absolute error (RMAE): 𝑵𝑵 𝒏𝒏=𝟏𝟏 , where 𝑀 = 1 𝑁 ï𝑣<sup>ï𝑣ï𝑣</sup> ∑ | is the MAE of the our benchmark naïve forecast. RMAE smaller than one indicates a better 𝑁𝑁 𝑅𝑅𝑀 𝑀𝑀= 𝑀 𝑀𝑀 / 𝑀 𝑀𝑀<sup>𝑁</sup> 𝑀𝑀<sup>𝑁</sup> forecasting performance compared to a simple naïve forecast. 𝑁𝑁 𝑛𝑛=1 |𝑦𝑦𝑛𝑛,ℎ −𝑓𝑓𝑛𝑛,ℎ The forecasting accuracy was calculated for the log level of the house price index. If the model used quarterly growth rates or annual growth rates of the house price index then forecasts of those models were recalculated to the log level of the index and only then forecasting accuracy was evaluated. 

#### **7.3. FORECASTING PERFORMANCE** 

Estimated forecasting accuracy is presented in Appendix C, where tables report RMSE of the individual models at different forecasting horizons. Results in the tables also indicate which models had RMAE lower than one, i.e. which models performed better than a benchmark naïve forecast. Several observations can be made from this forecasting exercise. 

First of all, model accuracy depends on the forecasting horizon. If we consider one-quarter-ahead forecasts, only a few BVAR and BVAR-SV models estimated in log levels outperformed a simple naïve forecast. In longer forecasting horizons, many more models were able to give better accuracy. 

The results also show that univariate models, in general, give better results than VAR models. Especially models estimated in quarterly growth rates, which constitute one of the best model classes in this exercise. Only some of the BVAR and BVAR-SV models outperformed univariate models. Thus, additional variables may improve forecasting performance, but we need Bayesian estimation to exploit that gain. 

Relatively short time series may be one of the reasons why VAR models (especially with a higher number of lags) provided poorer forecasting accuracy. A large number of parameters that need to be estimated caused large out-of-sample forecasting errors. Our results are in line with Karlsson (2013), who showed that BVAR models usually show better forecasting accuracy compared to VAR models. Furthermore, the results show that allowing stochastic volatility enhances forecasting performance of the models estimated in log levels. But it seems that there are no gains if we model house price index by taking the quarterly or annual growth rate. 

If we consider different multivariate model specifications, then specifications 2 and 6 estimated in log levels provided better forecasting accuracy than other specifications. Thus, it seems that the unemployment rate did not provide additional information. The results also show that multivariate models with one lag outperform models with a higher number of lags. It seems that additional lags are associated with additional parameters to be estimated and this leads to larger out-of-sample forecasting errors. 

Fig. 9 shows forecasts of the individual models that performed best (in terms of RMSE) in different model classes. In the univariate case, the best performing model was ARMA(4,1) estimated on quarterly growth rates. The lowest RMSEs between VAR-type models were achieved by VAR(1) Spec. 2 (taking log levels), BVAR(1) Spec. 6 (taking annual growth rates) and BVAR-SV(1) Spec. 7 (taking log levels). Thus, we see that depending on the model class, different data transformation or multivariate model specification would be preferred for the purposes of forecasting the house price index. Also, moving further ahead in the forecasting horizon, the dispersion between models’ forecasts increases. One-quarter-ahead forecasts are close, but a range of forecasts at eight quarters ahead is wide. Furthermore, some models, for example, ARMA(4,1) or VAR(1) Spec. 2, showed significant adjustments in their forecasts as new data are taken into account. 

23 

Fig. 9. Forecasts of individual models at different forecasting horizons 



<!-- Start of picture text -->
Index, 2015 = 100  Index, 2015 = 100<br>One-quarter-ahead  Four-quarters-ahead<br>130 130<br>Actual<br>125 125<br>120 Naïve 120<br>115 115<br>110 ARMA(4,1) 110<br>105 105<br>VAR(1)<br>100 Spec. 2 100<br>95 BVAR(1) 95<br>90 Spec. 6 90<br>85 BVAR-SV(1) 85<br>Spec. 7<br>80 80<br>Q1 2010 Q1 2012 Q1 2014 Q1 2016 Q1 2018 Q1 2010 Q1 2012 Q1 2014 Q1 2016 Q1 2018<br>Sources: Statistics Lithuania, authors' calculations  Sources: Statistics Lithuania, authors' calculations<br><!-- End of picture text -->



<!-- Start of picture text -->
Index, 2015 = 100  Index, 2015 = 100<br>Eight-quarters-ahead  Ten-quarters-ahead<br>130 130<br>125 125<br>120 120<br>115 115<br>110 110<br>105 105<br>100 100<br>95 95<br>90 90<br>85 85<br>80 80<br>Q1 2010 Q1 2012 Q1 2014 Q1 2016 Q1 2018 Q1 2010 Q1 2012 Q1 2014 Q1 2016 Q1 2018<br>Sources: Statistics Lithuania, authors' calculations  Sources: Statistics Lithuania, authors' calculations<br><!-- End of picture text -->

To summarise, BVAR-SV(1) Spec. 7, estimated taking data in log levels, provided the best forecasting accuracy across all estimated models. However, we recognise that the results are driven by the current data sample, which is relatively short and volatile. Thus, the results may change as we will have more data in our analysis. 

#### **7.4. FORECAST COMBINATION** 

Even though BVAR-SV(1) Spec. 7 showed the best out-of-sample forecasting accuracy in our analysis, the data generating process is unknown and model uncertainty risk is still an issue. Furthermore, if we consider many forecasting models, it is unclear which forecast to focus on. Those issues can be addressed by combining the forecasts. Various forecast combination methods have gained ground in the forecasting literature because it is found that in empirical exercises these methods usually outperform forecasts from a single model. A detailed discussion on forecast combinations can be found in Timmermann (2006). The author distinguishes several reasons why forecast combination may be useful. First, forecast combination may be more robust to unknown instabilities (e.g. structural breaks) than an individual model. Second, individual models may be subject to misspecification bias and these biases may be averaged out in the combination forecast. 

In our exercise we consider four combination approaches to produce point forecasts at each horizon. The first two approaches are a simple mean and median of the individual forecasts at each forecasting horizon. Timmermann (2006) argues that simple combination methods are hard to beat. The third combination approach is based on individual eight quarters ahead forecasting accuracy (in terms of RMSE) of the model: 

24 

**(26)** 



Table 2. Forecasting accuracy of the forecast combination approaches 

|**Combination approach**|**H1**|**H4**|**H8**|**H10**|
|---|---|---|---|---|
|Mean|0.020|**0.035**|**0.045**|**0.043**|
|Median|0.019|**0.033**|**0.047**|**0.046**|
|Weighted mean (RMSE)|0.020|**0.034**|**0.044**|**0.042**|
|Weighted mean (RMSE, where RMAE < 1)|**0.019**|**0.033**|**0.042**|**0.038**|



Notes: the table provides RMSE at a different forecasting horizon. The bold numbers show models where RMAE < 1. 

Table 2 shows the forecasting accuracy of the different forecast combination approaches. The results indicate that even simple combination methods increased forecasting accuracy considerably. Applying weights based on RMSEs further enhances forecasting power. Only three BVAR-SV type models showed a bit better forecasting performance than the first three forecast combination approaches. And only one model, i.e. BVARSV(1) Spec. 7, showed better forecasting accuracy than the fourth combination approach. Nevertheless, the forecast combination helps to address model uncertainty issue and is still reasonably accurate over various forecasting horizons. 

### **CONCLUDING REMARKS** 

In this paper, we addressed three important questions related to Lithuanian house prices, namely, whether house prices are under or over valuated, which explanatory variables have the biggest impact on the growth of house prices and what the future development of the Lithuanian house price index could be. Three separate modelling and forecasting exercises were performed in order to try answering these questions. 

The results of the VECM model show that house prices are negatively associated with real lending rates and have a strong positive association with construction costs and credit flows (in excess of housing investment). House prices also exhibit very strong inertia and the pull towards the long-term equilibrium is weak and statistically insignificant. The model helps identify a pronounced boom-bust cycle of house prices and shows that house prices were still slightly below their econometric balanced path at the end of the analysed sample, in 2018. 

We employed an ARDL model to assess which explanatory variables had the biggest impact on house price growth. The results revealed that interest rates on new loans to households and building permits are among the key drivers behind house price dynamics in Lithuania. The unexplained error may show that the actual decrease in growth could be attributed to changes in perception of the house value or that the relationship between variables is more contemporaneous. In both cases, the current modelling setup does not allow us to address these issues. The short term out-of-sample forecasting showed that we need a longer time series to make more accurate predictions with this type of model. 

Furthermore, a suite of models was built to make short and medium term forecasts of the Lithuanian house price index. We employed various univariate and multivariate time series forecasting models and compared their forecasting accuracy. The results show that the multivariate models outperformed univariate models, but we need Bayesian estimation to exploit the gain of the additional variables. Relatively short time series may be one of the reasons why the traditional VAR models provided relatively poor forecasting accuracy. To 

25 

safeguard against model uncertainty we considered several forecast combination approaches that showed improved forecasting accuracy compared to individual models. Thus, the combination of forecasts will be used to predict future changes in the Lithuanian housing price index. 

Analysis presented in this paper may be viewed as a further step towards more formalised modelling and forecasting of the Lithuanian house price index at the Bank of Lithuania. Each of the empirical exercises could be improved in various directions. However, we are analysing relatively short and volatile data and, therefore, as more observations become available, a longer data sample will help to model and forecast the Lithuanian house price index more accurately. 

### **REFERENCES** 

Anundsen, A.K. (2016). _Detecting imbalances in house prices: What goes up must go down?_ Norges Bank Working Paper 11. 

Anundsen, A.K., & E.S. Jansen (2013). _Self-reinforcing effects between housing prices and credit_ . Journal of Housing Economics, Vol. 22(3), pp. 192-212. 

Barari, M., N. Sarkar, S. Kundu, & K.B. Chowdhury (2014). _Forecasting house prices in the United States with multiple structural breaks_ . International Economic Review, Vol. 6(1), pp. 1-23. 

Barcilar, M., R. Gupta, & S.M. Miller (2015). _The out-of-sample forecasting performance of non-linear models of regional housing prices in the US_ . Applied Economics, Vol. 47(22), pp. 2259-2277. 

Bork, L., and S.V. Møller (2015). _Forecasting house prices in the 50 states using dynamic model averaging and dynamic model selection_ . International Journal of Forecasting, Vol. 31(1), pp. 63-78. 

Carstensen, K., O. Hülsewig, & T. Wollmershäuser (2009). _Monetary policy transmission and house prices: European cross-country evidence_ . CESifo, Working Paper, No 2750. 

Chan, J.C.C., & E. Eisenstat (2018). _Bayesian model comparison for time-varying parameter VARs with stochastic volatility_ . Journal of Applied Econometrics, Vol. 33(4), pp. 509-532. 

Cogley, T., & T.J. Sargent (2005). _Drifts and volatilities: monetary policies and outcomes in the post WWII US_ . Review of Economic Dynamics, Vol. 8(2), pp. 262-302. 

Das, S., R. Gupta, & A. Kabundi (2011). _Forecasting regional house price inflation: a comparison between dynamic factor models and vector autoregressive models._ Journal of Forecasting, Vol. 30(2), pp. 288-302. 

Drought, S., & Ch. McDonald (2011). _Forecasting house price inflation: a model combination approach._ Reserve Bank of New Zealand, Discussion Paper series, 2011/07. 

Eickmeier, S., & B. Hofmann (2010). _Monetary policy, housing booms and financial (im)balances_ . Deutsche Bundesbank, Discussion Paper Series 1: Economic Studies, No 07/2010. 

Emiris, M. (2016). _A dynamic factor model for forecasting house price in Belgium_ . National Bank of Belgium Working Paper research, No 313. 

Jarociński, M., & F. Smets (2008). _House prices and the stance of monetary policy_ . European Central Bank, Working Paper No 891. 

de Haas, R. & I. de Greef (2000). _Housing prices, bank lending, and monetary policy_ . De Nederlandsche Bank Research Series Supervision Paper, No 31. 

Gerdesmeier, D., A. Lenarčič, & B. Roffia (2012). _An alternative method for identifying booms and busts in the euro area housing market_ . European Central Bank, Working Paper Series, No 1493. 

Greiber, C., & R. Setzer (2007). _Money and housing ‒ evidence for the euro area and the US_ . Deutsche Bundesbank, Discussion Paper Series: Economic Studies, No 12/2007. 

26 

Gupta, R., A. Kabundi, & S.M. Miller (2009). _Forecasting the US real house price index: structural and nonstructural models with and without fundamentals._ University of Connecticut, Department of Economics Working Paper series, 2009-42. 

Gupta, R., M. Jurgilas, & A. Kabundi (2010). _The effect of monetary policy on real house price growth in South Africa: a factor-augmented vector autoregression (FAVAR) approach._ Econometric Modelling, Vol. 27(1), pp. 315-323. 

Gupta, R., & S.M. Miller (2009). _The time-series properties on housing prices: A case study of the Southern California Market._ University of Connecticut, Department of Economics, Working Paper series, 2009-10. 

Hyndman, R.J., & A.B. Koehler (2006). _Another look at measures of forecast accuracy_ . International Journal of Forecasting, Vol. 22(4), pp. 679-688. 

Kajuth, F., Th. Knetsch, & N. Pinkwart (2013). _Assessing house prices in Germany: evidence from an estimated stock-flow model using regional data._ Deutsche Bundesbank Discussion Paper No. 46/2013. 

Karlsson, S. (2013). _Forecasting with Bayesian vector autoregressions_ . Handbook of Economic Forecasting, Vol. 2 (Part B), pp. 791-897. 

Katrakilidis, C., & E. Trachanas (2012). _What drive housing price dynamics in Greece: new evidence from asymmetric ARDL cointegration._ Economic Modelling, Vol. 29(4), pp. 1064-1069. 

Kouwenberg, R., & R. Zwinkels (2014). _Forecasting the US housing market_ . International Journal of Forecasting. Vol. 30, pp. 415-425. 

Litterman, R. (1986). _Forecasting with Bayesian vector autoregressions – five years of experience_ . Journal of Business and Economic Statistics, Vol. 4(1), pp. 25-38. 

Lütkepohl, H. (2005). _New introduction to multiple time series analysis_ . Springer. 

Meen, G. (2002). _The time-series behavior of house prices: a transatlantic divide?_ Journal of Housing Economics, Vol. 11, pp. 1-23. 

an de Meulen, Ph., M. Micheli, & T. Schmidt (2011). _Forecasting house prices in Germany_ . Ruhr Economic Papers, No. 294. 

Muellbauer, J., & A. Murphy (1997). _Booms and busts in the UK housing market._ The Economic Journal, Vol. 107(445), pp. 1701-1727. 

Oikarinen, E. (2008). _Interaction between housing prices and household borrowing in Finland_ . ETLA Discussion Papers, No. 1145. 

Poterba, J.M. (1984). _Tax subsidies to owner-occupied housing: an asset-market approach_ . The Quarterly Journal of Economics, Vol. 99(4), pp. 729-752. 

Primiceri, G.E. (2005). Time varying structural vector autoregressions and monetary policy. The Review of Economic Studies, Vol. 72(3), pp. 821-852. 

Rapach, D.E., & J.K. Strauss (2007). _Forecasting real housing price growth in eight district states_ . Federal Reserve Bank of St. Louis, Regional Economic Development, Vol. 3(2), pp. 33-42. 

Risse, M., & M. Kern (2016). _Forecasting house price growth in the Euro area with dynamic model averaging._ North American Journal of Economics and Finance, Vol. 38, pp. 70-85. 

Robstad, Ø (2014). _House prices, credit and the effect of monetary policy in Norway: evidence from structural VAR models._ Norges Bank, Working Paper 05. 

Sims, C.A. (1980). _Macroeconomics and reality_ . Econometrica Vol. 48, pp. 1-48. 

Stiglitz, J.E. (1990). _Symposium on Bubbles._ Journal of Economic Perspectives, Vol. 4(2), pp. 13-18. 

27 

Timmermann, A (2006). _Forecast Combinations_ . Handbook of Economic Forecasting, Vol. 1 (chapter 4), pp. 135-196, Elsevier. 

28 

### **APPENDIX A** 

Table A1. Cointegrating relationship estimation results 

||**Dependent variable:**|**_hpi_**||
|---|---|---|---|
||**Variable**|**Coefficients**|**Standard errors**|
|_Intercept_||‒2.054*|0.399|
|_r_||‒1.084*|0.376|
|_ccpi_||1.543*|0.083|
|_credInv_||0.205*|0.020|
|_debtRatio_||0.231*|0.029|



Notes: * significant at the 0.05 level. 

29 

### **APPENDIX B** 

Fig. B1. Out-of-sample forecasts of weighted ARDL model at different forecasting horizons 



<!-- Start of picture text -->
Percentages  Percentages<br>One quarter ahead  Four quarter ahead<br>50 50<br>40 40<br>30 30<br>20 20<br>10 10<br>0 0<br>-10 -10<br>-20 -20<br>-30 -30<br>-40 -40<br>-50 -50<br>Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2 Q2<br>2006 2008 2010 2012 2014 2016 2018 2006 2008 2010 2012 2014 2016 2018<br>Actual Forecasts Actual Forecasts<br>Sources: Statistics Lithuania, authors' calculations  Sources: Statistics Lithuania, authors' calculations<br><!-- End of picture text -->

30 

### **APPENDIX C** 

Table C1. Forecasting accuracy of the naïve forecasts and univariate ARMA models 

|**Model**||**log l**|**evel**|||**q-o-q g**|**rowth**|||**y-o-y **|**growth**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**h1**|**h4**|**h8**|**h10**|**h1**|**h4**|**h8**|**h10**|**h1**|**h4**|**h8**|**h10**|
|Naïve|0.018|0.047|0.101|0.132|0.025|0.080|0.156|0.191|0.024|**0.042**|**0.077**|**0.090**|
|AR(1)|0.020|0.054|0.130|0.173|**0.020**|**0.042**|**0.065**|**0.071**|0.041|0.053|0.113|0.153|
|AR(2)|0.022|0.070|0.174|0.232|**0.020**|**0.041**|**0.062**|**0.067**|0.040|**0.046**|**0.092**|**0.125**|
|AR(3)|0.022|0.075|0.195|0.261|**0.020**|**0.039**|**0.061**|**0.065**|0.038|**0.042**|**0.082**|**0.113**|
|AR(4)|0.022|0.075|0.194|0.261|**0.020**|**0.039**|**0.061**|**0.064**|0.032|**0.043**|**0.085**|**0.117**|
|ARMA(1,1)|0.021|0.060|0.146|0.195|**0.020**|**0.039**|**0.059**|**0.061**|0.040|**0.049**|**0.100**|**0.134**|
|ARMA(2,1)|0.022|0.074|0.192|0.259|**0.020**|**0.040**|**0.061**|**0.065**|0.037|**0.044**|**0.092**|**0.129**|
|ARMA(3,1)|0.023|0.074|0.189|0.254|**0.020**|**0.040**|**0.062**|**0.066**|0.036|**0.042**|**0.085**|**0.119**|
|ARMA(4,1)|0.022|0.075|0.191|0.255|**0.020**|**0.039**|**0.057**|**0.060**|0.031|**0.041**|**0.078**|**0.109**|
|ARMA(1,2)|0.022|0.064|0.157|0.209|**0.020**|**0.040**|**0.062**|**0.067**|0.033|**0.048**|**0.099**|**0.129**|
|ARMA(2,2)|0.023|0.071|0.177|0.236|**0.020**|**0.040**|**0.063**|**0.067**|0.029|**0.044**|**0.081**|**0.096**|
|ARMA(3,2)*|-|-|-|-|**0.020**|**0.040**|**0.060**|**0.063**|0.031|**0.046**|**0.089**|**0.104**|
|ARMA(4,2)|0.022|0.077|0.202|0.269|0.028|**0.043**|**0.064**|**0.065**|0.049|**0.047**|**0.089**|**0.140**|



Notes: the table provides RMSE at different forecasting horizon. The bolded numbers show models where RMAE < 1. * Stationary model was not found for ARMA(3,2) specification. 

31 

Table C2. Forecasting accuracy of the VAR models 

|||**log  **|**level**|||**q-o-q **|**growth**|||**y-o-y **|**growth**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Model**|**h1**|**h4**|**h8**|**h10**|**h1**|**h4**|**h8**|**h10**|**h1**|**h4**|**h8**|**h10**|
|**Specificati**|**on 1**||||||||||||
|VAR(1)|0.038|0.104|0.119|**0.105**|0.021|0.051|**0.080**|**0.093**|0.026|0.057|0.117|0.155|
|VAR(2)|0.031|0.115|0.168|0.163|0.021|0.062|0.117|0.144|0.033|0.077|0.190|0.264|
|VAR(3)|0.021|0.071|0.156|0.176|0.022|0.065|0.147|0.190|0.037|0.094|0.211|0.278|
|VAR(4)|0.022|0.049|**0.085**|**0.100**|0.027|0.062|0.138|0.185|0.039|0.106|0.232|0.300|
|**Specificati**|**on 2**||||||||||||
|VAR(1)|0.020|**0.041**|**0.049**|**0.049**|0.029|0.065|**0.093**|**0.104**|0.027|0.055|**0.099**|**0.122**|
|VAR(2)|0.028|0.058|**0.071**|**0.072**|0.025|0.055|**0.090**|**0.103**|0.046|0.093|0.164|0.223|
|VAR(3)|0.028|**0.046**|**0.059**|**0.060**|0.042|0.079|0.148|0.189|0.044|0.098|0.133|**0.152**|
|VAR(4)|0.039|0.062|**0.085**|**0.077**|0.043|0.080|0.143|0.168|0.062|0.131|0.190|0.241|
|**Specificati**|**on 3**||||||||||||
|VAR(1)|0.021|**0.042**|**0.050**|**0.057**|0.024|0.068|**0.117**|**0.131**|0.050|0.103|0.188|0.246|
|VAR(2)|0.031|0.057|**0.099**|**0.121**|0.031|0.074|**0.129**|**0.142**|0.057|0.095|0.160|0.205|
|VAR(3)|0.035|0.059|**0.083**|**0.079**|0.037|0.098|0.172|0.191|0.062|0.136|0.197|0.223|
|VAR(4)|0.044|0.104|0.163|**0.173**|0.043|0.119|0.286|0.391|0.068|0.136|0.290|0.298|
|**Specificati**|**on 4**||||||||||||
|VAR(1)|0.038|0.119|0.179|0.184|0.021|0.052|**0.084**|**0.094**|0.031|0.054|**0.080**|**0.094**|
|VAR(2)|0.031|0.102|0.177|0.192|0.020|**0.047**|**0.078**|**0.084**|0.039|0.060|**0.109**|**0.132**|
|VAR(3)|0.025|0.066|0.162|0.191|0.026|0.055|**0.090**|**0.090**|0.048|0.088|0.156|0.199|
|VAR(4)|0.043|0.089|0.184|0.190|0.028|0.059|**0.113**|**0.132**|0.061|0.119|0.208|0.250|
|**Specificati**|**on 5**||||||||||||
|VAR(1)|0.036|0.117|0.182|0.189|0.024|0.071|**0.128**|**0.143**|0.037|0.072|0.118|**0.145**|
|VAR(2)|0.030|0.094|0.142|**0.133**|0.024|0.071|**0.120**|**0.129**|0.047|0.082|0.147|0.181|
|VAR(3)|0.029|0.063|**0.114**|**0.139**|0.029|0.074|0.138|**0.170**|0.060|0.099|0.170|0.206|
|VAR(4)|0.052|0.125|0.234|0.261|0.031|0.074|0.161|0.219|0.060|0.237|0.506|0.577|
|**Specificati**|**on 6**||||||||||||
|VAR(1)|0.021|**0.043**|**0.049**|**0.047**|0.024|0.052|**0.079**|**0.090**|0.030|0.055|**0.087**|**0.100**|
|VAR(2)|0.027|0.059|**0.069**|**0.066**|0.023|**0.045**|**0.066**|**0.066**|0.035|0.078|0.154|0.216|
|VAR(3)|0.029|**0.050**|**0.068**|**0.065**|0.032|0.060|0.119|**0.153**|0.056|0.125|0.240|0.307|
|VAR(4)|0.038|0.060|**0.085**|**0.074**|0.033|0.072|0.127|**0.136**|0.060|0.147|0.301|0.390|
|<br>**Specificati**|**on 7**||||||||||||
|VAR(1)|0.021|**0.042**|**0.061**|**0.074**|0.023|**0.060**|**0.104**|**0.119**|0.039|0.078|0.130|**0.159**|
|VAR(2)|0.026|0.067|0.192|0.245|0.029|0.070|**0.116**|**0.126**|0.052|0.089|0.169|0.240|
|VAR(3)|0.032|0.070|0.165|**0.188**|0.036|0.088|0.155|0.175|0.072|0.119|0.192|0.233|
|VAR(4)|0.045|0.181|0.406|0.481|0.046|0.151|0.386|0.525|0.088|0.134|0.252|0.236|



Notes: the table provides RMSE at different forecasting horizon. The bolded numbers show models where RMAE < 1. 

32 

Table C3. Forecasting accuracy of the BVAR models 

|||**log  **|**level**|||**q-o-q **|**growth**|||**y-o-y **|**growth**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Model**|**h1**|**h4**|**h8**|**h10**|**h1**|**h4**|**h8**|**h10**|**h1**|**h4**|**h8**|**h10**|
|**Specificati**|**on 1**||||||||||||
|BVAR(1)|0.024|0.052|**0.051**|**0.045**|0.021|**0.046**|**0.074**|**0.090**|0.023|**0.045**|**0.091**|**0.114**|
|BVAR(2)|0.025|0.057|**0.058**|**0.050**|0.021|**0.043**|**0.056**|**0.059**|0.025|0.053|0.118|0.153|
|BVAR(3)|0.025|0.062|**0.077**|**0.070**|0.021|**0.047**|**0.081**|**0.101**|0.024|0.055|0.120|0.161|
|BVAR(4)|0.021|**0.041**|**0.054**|**0.055**|0.021|**0.048**|**0.087**|**0.111**|0.024|**0.050**|**0.106**|0.142|
|**Specificati**|**on 2**||||||||||||
|BVAR(1)|**0.018**|**0.041**|**0.085**|**0.111**|0.021|**0.044**|**0.067**|**0.079**|0.022|**0.037**|**0.057**|**0.063**|
|BVAR(2)|**0.018**|**0.040**|**0.082**|**0.107**|0.021|**0.043**|**0.057**|**0.060**|0.022|**0.039**|**0.069**|**0.081**|
|BVAR(3)|**0.018**|**0.039**|**0.079**|**0.103**|0.021|**0.051**|**0.101**|**0.129**|0.022|**0.039**|**0.065**|**0.077**|
|BVAR(4)|**0.019**|**0.038**|**0.074**|**0.096**|0.021|**0.046**|**0.085**|**0.109**|0.023|**0.040**|**0.061**|**0.072**|
|**Specificati**|**on 3**||||||||||||
|BVAR(1)|**0.017**|**0.039**|**0.081**|**0.108**|0.021|0.052|**0.087**|**0.103**|0.023|**0.038**|**0.053**|**0.063**|
|BVAR(2)|**0.018**|**0.042**|**0.092**|**0.125**|0.021|**0.044**|**0.062**|**0.066**|0.023|**0.040**|**0.064**|**0.075**|
|BVAR(3)|**0.018**|**0.039**|**0.090**|**0.118**|0.021|**0.050**|**0.099**|**0.126**|0.027|0.051|**0.084**|**0.098**|
|BVAR(4)|0.019|**0.046**|0.104|0.136|0.021|**0.047**|**0.078**|**0.096**|0.028|0.071|0.139|0.164|
|**Specificati**|**on 4**||||||||||||
|BVAR(1)|**0.019**|**0.034**|**0.063**|**0.088**|0.021|**0.046**|**0.072**|**0.081**|0.022|**0.038**|**0.057**|**0.064**|
|BVAR(2)|**0.019**|**0.036**|**0.060**|**0.081**|0.021|**0.043**|**0.057**|**0.059**|0.023|**0.043**|**0.077**|**0.093**|
|BVAR(3)|**0.020**|**0.042**|**0.082**|**0.109**|0.021|**0.052**|0.108|0.142|0.023|**0.044**|**0.075**|**0.091**|
|BVAR(4)|**0.019**|**0.037**|**0.076**|**0.103**|0.021|**0.050**|**0.101**|**0.136**|0.023|**0.040**|**0.065**|**0.078**|
|**Specificati**|**on 5**||||||||||||
|BVAR(1)|**0.018**|**0.028**|**0.056**|**0.080**|0.021|0.051|**0.087**|**0.102**|0.024|**0.040**|**0.064**|**0.081**|
|BVAR(2)|**0.018**|**0.032**|**0.061**|**0.086**|0.021|**0.044**|**0.062**|**0.065**|0.024|**0.044**|**0.076**|**0.091**|
|BVAR(3)|**0.019**|**0.035**|**0.075**|**0.102**|0.021|**0.048**|**0.097**|**0.125**|0.027|0.052|**0.088**|**0.103**|
|BVAR(4)|0.020|**0.046**|0.111|0.150|0.021|**0.048**|**0.081**|**0.100**|0.027|0.058|**0.106**|**0.126**|
|**Specificati**|**on 6**||||||||||||
|BVAR(1)|**0.019**|0.048|**0.098**|**0.127**|0.021|**0.045**|**0.070**|**0.083**|0.023|**0.036**|**0.054**|**0.057**|
|BVAR(2)|0.019|0.047|**0.096**|**0.124**|0.021|**0.042**|**0.056**|**0.058**|0.022|**0.039**|**0.066**|**0.077**|
|BVAR(3)|0.019|**0.045**|**0.093**|**0.118**|0.021|**0.047**|**0.088**|**0.111**|0.022|**0.038**|**0.065**|**0.075**|
|BVAR(4)|**0.019**|**0.041**|**0.080**|**0.102**|0.021|**0.044**|**0.076**|**0.096**|0.023|**0.038**|**0.057**|**0.067**|
|**Specificati**|**on 7**||||||||||||
|BVAR(1)|**0.019**|0.047|**0.098**|**0.127**|0.021|0.051|**0.086**|**0.101**|0.023|**0.038**|**0.054**|**0.061**|
|BVAR(2)|0.019|0.048|0.105|0.139|0.021|**0.044**|**0.060**|**0.064**|0.023|**0.041**|**0.066**|**0.076**|
|BVAR(3)|**0.018**|**0.046**|0.109|0.142|0.021|**0.049**|**0.094**|**0.117**|0.026|**0.047**|**0.074**|**0.083**|
|BVAR(4)|**0.019**|**0.047**|0.111|0.145|0.021|**0.047**|**0.079**|**0.098**|0.026|**0.047**|**0.078**|**0.089**|



Notes: the table provides RMSE at different forecasting horizon. The bolded numbers show models where RMAE < 1. 

33 

Table C4. Forecasting accuracy of the BVAR-SV models 

|||**log l**|**evel**|||**q-o-q **|**growth**|||**y-o-y **|**growth**||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Model**|**h1**|**h4**|**h8**|**h10**|**h1**|**h4**|**h8**|**h10**|**h1**|**h4**|**h8**|**h10**|
|**Specification**|**1**||||||||||||
|BVAR-SV(1)|0.030|0.083|**0.120**|**0.129**|0.020|0.051|**0.101**|**0.131**|0.022|**0.036**|**0.062**|**0.069**|
|BVAR-SV(2)|0.027|0.079|**0.116**|**0.125**|0.021|**0.044**|**0.086**|**0.112**|0.021|**0.040**|**0.084**|**0.107**|
|BVAR-SV(3)|0.025|0.068|**0.107**|**0.117**|0.020|**0.033**|**0.054**|**0.061**|0.023|**0.037**|**0.073**|**0.093**|
|BVAR-SV(4)|0.021|**0.046**|**0.074**|**0.086**|0.021|**0.034**|**0.051**|**0.056**|0.023|**0.036**|**0.067**|**0.085**|
|**Specification**|**2**||||||||||||
|BVAR-SV(1)|**0.017**|**0.033**|**0.065**|**0.080**|0.019|**0.039**|**0.081**|**0.108**|0.023|**0.042**|**0.071**|**0.084**|
|BVAR-SV(2)|**0.018**|**0.035**|**0.067**|**0.084**|0.019|**0.036**|**0.064**|**0.081**|0.025|0.053|**0.104**|**0.133**|
|BVAR-SV(3)|**0.019**|**0.036**|**0.073**|**0.093**|0.019|**0.035**|**0.054**|**0.063**|0.026|0.056|0.114|0.151|
|BVAR-SV(4)|**0.019**|**0.034**|**0.066**|**0.084**|0.020|**0.037**|**0.050**|**0.054**|0.026|0.054|**0.098**|**0.123**|
|**Specification**|**3**||||||||||||
|BVAR-SV(1)|**0.019**|**0.034**|**0.041**|**0.041**|0.020|0.055|**0.112**|**0.141**|0.027|**0.046**|**0.072**|**0.088**|
|BVAR-SV(2)|0.021|**0.044**|**0.054**|**0.051**|0.020|0.054|**0.105**|**0.132**|0.028|**0.048**|**0.082**|**0.107**|
|BVAR-SV(3)|0.021|**0.044**|**0.055**|**0.051**|0.020|**0.039**|**0.061**|**0.066**|0.030|0.055|**0.097**|**0.123**|
|BVAR-SV(4)|0.021|**0.044**|**0.056**|**0.054**|0.021|**0.042**|**0.063**|**0.069**|0.036|0.069|**0.117**|**0.152**|
|**Specification**|**4**||||||||||||
|BVAR-SV(1)|**0.021**|**0.044**|**0.060**|**0.066**|0.021|**0.042**|**0.069**|**0.086**|0.023|**0.041**|**0.073**|**0.089**|
|BVAR-SV(2)|**0.020**|**0.047**|**0.058**|**0.063**|0.020|**0.039**|**0.056**|**0.057**|0.023|**0.046**|**0.094**|**0.120**|
|BVAR-SV(3)|**0.021**|**0.047**|**0.059**|**0.065**|0.021|**0.049**|**0.100**|**0.126**|0.023|**0.048**|**0.096**|**0.121**|
|BVAR-SV(4)|0.021|**0.041**|**0.048**|**0.054**|0.021|**0.046**|**0.087**|**0.110**|0.025|**0.048**|**0.087**|**0.108**|
|**Specification**|**5**||||||||||||
|BVAR-SV(1)|**0.020**|**0.037**|**0.048**|**0.056**|0.022|0.053|**0.091**|**0.107**|0.028|0.051|**0.093**|**0.118**|
|BVAR-SV(2)|**0.019**|**0.039**|**0.045**|**0.048**|0.021|**0.044**|**0.067**|**0.069**|0.026|**0.048**|**0.091**|**0.116**|
|BVAR-SV(3)|0.021|**0.040**|**0.043**|**0.044**|0.021|**0.043**|**0.083**|**0.099**|0.028|0.051|**0.094**|**0.114**|
|BVAR-SV(4)|0.021|**0.039**|**0.039**|**0.041**|0.021|**0.047**|**0.079**|**0.092**|0.033|0.055|**0.090**|**0.108**|
|**Specification**|**6**||||||||||||
|BVAR-SV(1)|**0.018**|**0.030**|**0.056**|**0.068**|0.022|0.066|0.148|0.196|0.025|**0.039**|**0.060**|**0.068**|
|BVAR-SV(2)|**0.018**|**0.031**|**0.050**|**0.059**|0.021|0.061|0.146|0.196|0.027|0.053|**0.092**|**0.112**|
|BVAR-SV(3)|0.021|**0.032**|**0.056**|**0.068**|0.019|**0.031**|**0.049**|**0.056**|0.027|0.052|**0.092**|**0.112**|
|BVAR-SV(4)|0.021|**0.032**|**0.050**|**0.060**|0.021|**0.036**|**0.049**|**0.052**|0.035|0.068|**0.113**|**0.144**|
|**Specification**|**7**||||||||||||
|BVAR-SV(1)|**0.018**|**0.029**|**0.030**|**0.030**|0.023|0.079|0.172|0.222|0.031|0.055|**0.100**|**0.134**|
|BVAR-SV(2)|0.022|**0.045**|**0.045**|**0.037**|0.023|0.072|0.155|0.201|0.033|0.060|**0.106**|**0.132**|
|BVAR-SV(3)|0.027|0.061|**0.063**|**0.053**|0.020|**0.036**|**0.061**|**0.070**|0.036|0.067|**0.117**|**0.146**|
|BVAR-SV(4)|0.028|0.065|**0.071**|**0.065**|0.023|**0.049**|**0.074**|**0.079**|0.044|0.075|**0.119**|**0.144**|



Notes: the table provides RMSE at different forecasting horizon. The bolded numbers show models where RMAE < 1. 

34 

Figure C1. Forecasts of forecast combinations at different forecasting horizons 



<!-- Start of picture text -->
Index, 2015 = 100  Index, 2015 = 100<br>One-quarter-ahead  Four-quarter-ahead<br>130 130<br>Actual<br>125 125<br>120 Naïve 120<br>115 115<br>110 Mean 110<br>105 105<br>Median<br>100 100<br>95 RMSE 95<br>90 90<br>85 RMSE, where 85<br>RMAE < 1<br>80 80<br>Q1 2010 Q1 2012 Q1 2014 Q1 2016 Q1 2018 Q1 2010 Q1 2012 Q1 2014 Q1 2016 Q1 2018<br>Sources: Statistics Lithuania, authors' calculations  Sources: Statistics Lithuania, authors' calculations<br><!-- End of picture text -->



<!-- Start of picture text -->
Index, 2015 = 100  Index, 2015 = 100<br>Eight-quarter-ahead  Ten-quarter-ahead<br>130 130<br>125 125<br>120 120<br>115 115<br>110 110<br>105 105<br>100 100<br>95 95<br>90 90<br>85 85<br>80 80<br>Q1 2010 Q1 2012 Q1 2014 Q1 2016 Q1 2018 Q1 2010 Q1 2012 Q1 2014 Q1 2016 Q1 2018<br>Sources: Statistics Lithuania, authors' calculations  Sources: Statistics Lithuania, authors' calculations<br><!-- End of picture text -->

35 

