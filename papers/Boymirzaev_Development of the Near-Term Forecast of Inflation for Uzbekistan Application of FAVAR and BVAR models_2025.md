---
title: Boymirzaev_Development of the Near-Term Forecast of Inflation for Uzbekistan Application of FAVAR and BVAR models_2025
type: paper
source_pdf: raw/papers/Boymirzaev_Development of the Near-Term Forecast of Inflation for Uzbekistan Application of FAVAR and BVAR models_2025.pdf
converted: 2026-08-18
---



**Graduate Institute of International and Development Studies International Economics Department Working Paper Series** 

Working Paper No. HEIDWP06-2025 

**Development of the Near-Term Forecast of Inflation for Uzbekistan: Application of FAVAR and BVAR models** 

# **Temurbek Boymirzaev** 

Central Bank of Uzbekistan 

Chemin Eug`ene-Rigot 2 P.O. Box 136 CH - 1211 Geneva 21 Switzerland 

- © The Authors. All rights reserved. Working Papers describe research in progress by the author(s) and are published to 

- elicit comments and to further debate. No part of this paper may be reproduced without the permission of the authors. 



## **_Development of the Near-Term Forecast of Inflation for Uzbekistan: Application of FAVAR and BVAR models_** 

**_Temurbek Boymirzaev_** _Central Bank of Uzbekistan_ 

## **Abstract** 

This study investigates the application of Factor-Augmented Vector Autoregression (FAVAR) and Bayesian Vector Autoregression (BVAR) models for inflation forecasting. FAVAR models deal with high-dimensional data by extracting latent factors from extensive macroeconomic indicators, while BVAR models incorporate prior distributions to enhance forecast stability and precision in data-limited environments. Employing a comprehensive dataset of Uzbekistan-specific inflation determinants, we conduct an empirical assessment of both models, examining their predictive accuracy. Findings from this research aim to optimize inflation forecasting methodologies, providing the Central Bank of Uzbekistan with robust, data-driven insights for improved policy formulation. 

**Keywords** : FAVAR, BVAR, inflation forecast, forecast combination **JEL:** E30, E31, E37 

_The author thanks Assistant Professor Marko Mlikota from Geneva Graduate Institute for the academic supervision of this paper. This research took place through the visiting program under the Bilateral Assistance and Capacity Building for Central Banks (BCC), financed by SECO, and the Graduate Institute in Geneva. The views expressed in this paper are solely those of the author and do not necessarily reflect those of the Central Bank of Uzbekistan._ 

## **CONTENTS** 

|**1. INTRODUCTION**..................................................................................................................... 3|
|---|
|**2. LITERATURE REVIEW**......................................................................................................... 5|
|_2.1 Empirical studies of FAVAR models_...................................................................................... 5|
|_2.2 Empirical studies of BVAR models_........................................................................................ 6|
|_2.3 Combining FAVAR and BVAR models_................................................................................... 7|
|**3. THEORETICAL FRAMEWORK OF THE FAVAR AND BVAR MODELS**..................... 7|
|_3.1 FAVAR model estimation_....................................................................................................... 7|
|_3.2 BVAR model estimation_......................................................................................................... 9|
|**4. DATA DESCRIPTION AND ESTIMATION**........................................................................11|
|_4.1 The BVAR model and data description_............................................................................... 12|
|_4.2 The FAVAR model and data description_.............................................................................. 13|
|_4.3 Forecast Procedure_............................................................................................................. 14|
|**5. EMPIRICAL RESULTS**......................................................................................................... 15|
|_5.1 Evaluating BVAR point forecast performance_.................................................................... 15|
|_5.2 Evaluating FAVAR point forecast performance_................................................................... 15|
|_5.3 Evaluating the Forecast Combination_................................................................................ 16|
|**6. CONCLUSION AND FINAL REMARKS**........................................................................... 16|
|**REFERENCES**............................................................................................................................ 18|
|**APPENDIX**.................................................................................................................................. 19|



2 

## **1. INTRODUCTION** 

Domestic and external factors shape inflation dynamics in Uzbekistan. Recent liberalization measures, price reforms and adjustments in subsidy policies have created new inflationary pressures. At the same time, a volatile global price of commodity market generated additional pressures to the domestic prices. In addition, domestic factors like structural reforms, supply chain disruptions and changes in consumer demand patterns are also exerting a strong influence on inflation dynamics. The above factors have made the generation of accurate predictions more complicated, emphasizing the necessity of sophisticated models that account for the complex joint dependencies of economic variables. 

Many of these complexities are difficult to address with traditional forecasting models, like univariate time series or vector autoregressive (VAR) approaches. In data-rich settings, they often have limited predictive power, or fail to incorporate structural breaks. To address these limitations, we firstly utilize two advanced econometric models: the Factor-Augmented Vector Autoregression (FAVAR) model and the Bayesian Vector Autoregression (BVAR) model. 

The FAVAR is used for data-rich environments. It compresses a large dataset into a small number of latent factors that comprise the essential economic information. This allows the model to incorporate a wide range of macroeconomic and sectoral drivers in conventional VAR frameworks. The BVAR model, in contrast, integrates prior information into the estimation, which alleviates the problems of over-parameterization and improves forecasting stability for small sample sizes. 

This study contributes by utilizing advantages of both models for better forecasting performance. In this context, this study seeks to produce optimal inflation forecasts combining the results of FAVAR and BVAR models that are accurate as well as robust. 

Precise inflation predictions are required for constructing sound and efficient monetary policies and for ensuring the credibility of the CBU. Transparent and reliable forecasts anchor inflation expectations and enhance overall public confidence in the central bank’s policy. Given that Uzbekistan is still in transition toward a market economy, signaling monetary policy objectives plays a vital role in achieving macroeconomic stability. 

The paper is structured as follows. Section 1 provides a short background on inflation dynamics during 2014-2023. Section 2 summarizes theoretical and empirical literature on inflation forecasting using FAVAR and BVAR models. In Section 3, the methodological framework is presented, which includes model specifications and forecasting strategy. Section 4 explains data sources and constructs the variables used for the analysis, focusing on their relevance to the Uzbek economy. Section 5 shows empirical results both for the comparison of individual model performances and for the combined forecast approach. Finally, Section 6 concludes with a summary of model performance and recommendations for future research. 

3 

## _Inflation dynamics in Uzbekistan during 2014–2023_ 

During 2014-2023, inflation in Uzbekistan had different phases that were affected by structural reforms, external shocks and development of monetary policies. Inflation behaved very differently during these periods, going from relatively stable to acceleration of inflation and then gradual stabilization as the country moved toward a market-based economic model. 

## _2014–2016: Relative stability amid structural constraints_ 

During this period, annual inflation in Uzbekistan remained moderate, averaging 8% to 9%. The state-dominated economic structure, with extensive subsidies and administrative control over major sectors, allowed to hold down inflationary pressures. But this stability was achieved at the cost of inefficiencies, such as demand suppression, currency misalignment and lack of responsiveness to the market. Other factors, including modest global commodity prices, also helped keep inflation low and stable. 

**Figure 1. Inflation dynamics in Uzbekistan during 2014–2023** 



_Source: Statistics Agency_ 

## _2017–2018: Currency liberalization and inflation surge_ 

Since 2017, inflation dynamics had changed significantly, following major economic reforms, especially after the implementation of a market-based exchange rate policy. The Uzbek soum was substantially devaluated after liberalization of the exchange rate in September 2017. This reform was needed for economic modernization and improving competitiveness. However, it caused inflation to jump from 14.8% in 2017 to 17.0% in 2018. 

4 

This period also included an adjustment of previously controlled prices for utilities, fuel, and essential products, further contributing inflationary pressure. The government tried to balance between liberalization and stability of the economy to mitigate short-term costs of reforms. 

_2019–2023: Inflation peaks and policy adjustments_ 

In 2019 inflation accelerated to 15.9% due to external shocks as global commodity price fluctuations and growing local demand aggravated domestic factors. The Central Bank of Uzbekistan (CBU) reacted by implementing tighter monetary policies, such as an increase in policy rates and liquidity controls. These policies were implemented in 2020 and enabled to reduce inflation to 11-12%. 

Inflation dynamics were also affected by economic impacts of the COVID-19 pandemic. Broad disruptions of global supply chains and temporary mitigation in domestic demand had mixed effects. On the one hand, adverse supply-side developments pulled prices higher. On the other hand, weak activity and lower than expected consumer spending acted as countervailing forces, resulting in moderate disinflation by the end of 2020. 

_2021–2023: Gradual decline and stabilization efforts_ 

In 2021 inflation began to gradually stabilize, slowing to 10% by the year end. However, inflationary pressures remained due to external shocks such as rising global oil prices, geopolitics and supply chain issues. Hence, the decreasing trend of inflation during this period likely reflect improved policy coordination. 

At the end of 2023, annual inflation rate dropped to 8.8%, the lowest level in seven years. This is a significant progress due to structural reforms and tighter monetary policy in the economy. External conditions, including relatively steady global commodity markets also helped to achieve declining trend of inflation. 

## **2. LITERATURE REVIEW** 

Structural shifts in economies in transition, such as the adjustments of regulated prices, the exchange rate liberalization and the changing external environment present challenges for modeling inflation. Such challenges have led to the growing popularity of various econometric models, such as Factor-Augmented Vector Autoregression (FAVAR) and Bayesian Vector Autoregression (BVAR). These models provide a powerful framework to incorporate increasingly rich datasets that improves the accuracy of inflation forecasts at short and medium-term horizons. This section reviews previous studies applying the FAVAR and BVAR model, gives concise information on their application in various economic contexts. 

## _2.1 Empirical studies of FAVAR models_ 

The original work of Factor-Augmented Vector Autoregression (FAVAR) model emerged as a contribution to the classic VAR model, that finds it difficult to deal with high-dimensional datasets. Specifically, standard VAR model had popularity in macroeconomic forecasting and 

5 

often suffer from omitted variable bias and compromised capacity to accommodate high-dimensional data. Bernanke (2005) introduced the FAVAR approach to address these issues by incorporating underlying factors from large datasets. These factors are derived through statistical methods (principal component analysis) that condense data for a large number of variables into a smaller, computationally tractable number of factors. This allows FAVAR model to better capture dynamics of the macroeconomics structure, making this approach particularly useful for cross-sectoral analysis of the impact of monetary shocks. 

Stock and Watson (2002) showed low-dimensional factor models outperformed other parsimonious alternatives, like univariate AR and VAR models, by better predicting inflation and output. Bernanke (2005) used the FAVAR model applying both methods, one step and two steps, showed that the FAVAR model addresses some of the important issues, so-called price puzzle. This is the converse of what happens in standard VARs, in which a monetary tightness causes an initial price rise. 

Günay (2018) used a FAVAR model to forecast core inflation and industrial production in Turkey, similarly found that less complicated models with fewer factors did at least well than more complex setups. Likewise, Reigl (2017) adopted the FAVAR framework to Estonia — employing more than 300 economic and financial variables to predict both headline and core inflation. These studies highlight the model’s ability to accommodate rich datasets, while mitigate overfitting risks associated with traditional VAR models. 

FAVAR specifications have also been successful in modelling macroeconomic dynamics in small open economies. Ajevskis and Davidsons (2008) used factor analysis techniques for Latvia and found that FAVAR models consistently outperformed AR models for GDP and inflation, although the gains are sometimes marginal in a statistical sense. 

More recent research aims to improve the factor extraction process and to develop FAVAR in the presence of structural changes in the data and time-varying dynamics. Bai and Ng (2007) introduced specific identification of the number of factors to preserve explanatory of the model. 

## _2.2 Empirical studies of BVAR models_ 

Bayesian Vector Autoregression (BVAR) models have gained valuable applications in econometric forecasts compared to the unrestricted VAR models. Traditional VAR models can lead to over-parameterization, especially in small data sets or complex economic systems. The "Minnesota prior" developed by Litterman (1986) applies Bayesian shrinkage, providing advantage of reducing the estimation of parameters and thus improve forecasting accuracy. 

Banbura, Giannone, and Reichlin (2010) presented that Bayesian shrinkage techniques allow to incorporate over 100 variables and outperforms small-scale VAR models in forecasting macroeconomic indicators. Carriero, Clark and Marcellino (2011) showed that the use of flexible priors leads to robust results across different economic environment. 

6 

Poghosyan (2013) evaluated model comparison in forecasting inflation and GDP growth of Armenia applying VAR, BVAR and FAVAR models. In this study, BVAR models provided promising forecast even under structural changes. Similarly, BVAR models were found to significantly reduce forecast errors relative to unrestricted VAR models for inflation and exchange rates in the Albanian data (Vika, 2018). These studies highlight BVAR models could adapt to the complexities of small-sample environments and volatile economic conditions. 

## _2.3 Combining FAVAR and BVAR models_ 

The forecast combination using both FAVAR and BVAR model results has the potential to capitalize on their respective advantages and increase forecasting accuracy. 

Several empirical studies have focused on the advantages of combining FAVAR and BVAR methodologies to benefit from both of them. Akdogan (2012) demonstrated the gains of such method applying this to predict a short-term inflation in Turkey. They found that vector autoregressions incorporating more economic information, such as factor-augmented vector autoregressions (FAVAR) and Bayesian vector autoregressions (BVAR), provide superior near-term forecasts compared to simple univariate models. This study summarized the scope for improving forecast accuracy by integrating information from various sources including consumer prices, industrial production and financial markets, 

Geweke and Amisano (2011) investigated Bayesian Model Averaging (BMA) framework for the combination of forecasts from a number of econometric models. In this study, BMA applies a posterior probability distribution over each model, generating a weighted BVAR that allows probabilistic integration of FAVAR and BVAR forecasts. This approach improves robustness with respect to model uncertainty. 

Waggoner and Zha (2012) present dynamic weighting schemes that adjust the contribution of each model to the joint forecast based on prevailing economic environment. During times of structural stability, the data-driven FAVAR may dominate the combination. In contrast, during times of higher volatility, the robustness of the BVAR model becomes more important. This gives the ability to do more context-sensitive forecasting and have better accuracy per time horizon. 

## **3. THEORETICAL FRAMEWORK OF THE FAVAR AND BVAR MODELS** 

## _3.1 FAVAR model estimation_ 

Factor models are designed to extract and use large volumes of information available in datasets, tackling common issues such as limited degrees of freedom, overfitting or increased parameter uncertainty during estimation. 

Models that rely on only a few variables often exclude critical information due to restrictions imposed by degrees of freedom, leading to less dependable results. FAVAR models offer a more comprehensive solution by leveraging extensive datasets and mitigating omitted variable bias. 

7 

Let 𝑌𝑡 represent an 𝑀 × 1 vector of observable variables and 𝐹𝑡 denote a 𝐾 × 1 vector of latent (unobserved) variables. The joint evolution of (𝐹𝑡, 𝑌𝑡) is assumed to follow the specified transition equation: 



The term 𝛷(𝐿) denotes a lag polynomial of finite order d, conformable to the dimensions of the system and may incorporate a priori constraints, as typically employed in structural VAR frameworks. The error term 𝑣𝑡 is assumed to be mean zero with a covariance matrix Σ. Since the factors 𝐹𝑡 are unobservable, it is not feasible to estimate equation (3.1) directly. Instead, the latent information contained in 𝐹𝑡 can be extracted from a set of economic time series represented by the 𝑁 × 1 vector 𝑋𝑡. It is assumed that the number of observed time series 𝑁 is significantly larger than the number of latent factors, providing a comprehensive dataset for analysis. 𝑋𝑡 is assumed to be connected to the unobservable 𝐹𝑡 and the observable 𝑌𝑡 through the following relationship: 



In this framework, Λ<sup>𝑓</sup> is defined as an 𝑁 × 𝐾 matrix of factor loadings, while Λ<sup>𝑌</sup> represents an 𝑁 × 𝑀 matrix. The 𝑁 × 1 vector of error terms, e𝑡, is assumed to have a mean of zero and follows a normal distribution. Depending on the estimation approach whether through likelihood methods or principal components the error terms are either uncorrelated or exhibit minimal crosscorrelation. Equation (3.2) embodies the concept that both 𝑌𝑡 and 𝐹𝑡 act as driving forces underlying the dynamics of 𝑋𝑡. The factors and variables used for forecasting in the FAVAR model can be represented in the following form: 



In this context, 𝐹𝑡 represents the estimated factor. 

A critical aspect of the FAVAR model is the method used for estimation. Two primary approaches are commonly employed. The first, known as the two-step procedure, involves estimating the unobserved factors initially and then incorporating them into standard VAR models. The second approach estimates both factors and VAR simultaneously, referred to as the one-step estimation procedure. Each method has its respective strengths and limitations. Bernanke et al. (2005) apply both methods to estimate FAVAR models and report minimal differences in the results. Consequently, given that the one-step procedure is technically complex without providing substantial improvements in model performance, we adopt the two-step procedure. In this approach, principal component (PC) analysis is used to estimate the factors. 

8 

## _3.2 BVAR model estimation_ 

A reduced form of the VAR model expressed as follows: 



where 𝑌𝑡 is an _n × 1_ vector of endogenous variables and 𝑢𝑡 represents an _n × 1_ vector of error terms, assumed to be independently and identically distributed (i.i.d.) according to a multivariate normal distribution with mean zero and variance-covariance matrix ∑. 



𝐵𝑙(for 𝑙= 1,2, … . , 𝑝) are an _n × n_ coefficient matrices representing the impact of past values of 𝑌𝑡 on the present. 



where 𝑋𝑡 = (𝐼𝑡 ⊗𝑊𝑡) is an _n × nk_ matrix, _k = np_ . 𝑊𝑡 = (𝑌𝑡−1′ , 𝑌𝑡−2,′ … . , 𝑌𝑡−𝑝′ )<sup>′</sup> is _k × 1_ vector containing all lagged endogenous variables. 𝛽= 𝑣𝑒𝑐(𝐵1, 𝐵2, … , 𝐵𝑝) is _nk × 1_ vector containing all unknown coefficients. Here, ⊗ represents the Kronecker product, and the vec ⋅ operator vec( ) transforms a matrix into a column vector by stacking its columns. The key objective is to estimate the parameters 𝛽 (lag coefficients) and ∑ (covariance matrix of residuals) using Bayesian methods. 



where 𝑓(𝑌|𝛽, ∑) is the likelihood function of the data, denoted as 𝐿(𝑌 |𝛽, ∑) and 𝑓(𝛽, ∑) represents the prior distribution of the parameters, incorporating prior knowledge. 𝑓(𝑌) is a normalizing constant that ensures the posterior integrates to one but does not depend on 𝛽 or ∑. Since 𝑓(𝑌) is independent of the parameters, the posterior distribution simplifies to: 



The posterior density 𝑓(𝛽, ∑ | 𝑌) summarizes all available information about the parameters after observing the data and can be used to derive point estimators for 𝛽 and ∑. The prior density 𝑓(𝛽, ∑) represents subjective beliefs about the parameters before observing the data. The selection of an appropriate prior distribution is a critical component in setting up of the model. Although numerous alternatives have been proposed in the academic literature, this research employs the Litterman (Minnesota) prior. 

The Minnesota prior distribution assumes that the coefficients matrix 𝐵 follows a normal distribution, with a specified prior mean assigned to the first own lag, while the remaining coefficients are set to zero. Consequently, this prior distribution assumes that the variables exhibit autoregressive behavior of order one (AR(1)), encompassing white noise and random walk components. 

9 

Litterman (1986) proposes a multivariate normal prior distribution for 𝛽, with prior mean, 𝛽<sup>∗</sup> and variance of the prior, 𝛺<sup>∗</sup> . 



The variance of the prior 𝛺<sup>∗</sup> is specified in structured manner and is determined by the following relationships for the VAR coefficients. 





In this context, 𝑖 represents the dependent variable in the 𝑖th equation, while 𝑗 denotes the independent variables within the same equation. When 𝑖= 𝑗, the coefficients correspond to the own lags of variable 𝑖. The terms 𝜎𝑖 and 𝜎𝑗 indicate the variances of the error terms derived from autoregressive (AR) regressions, estimated using ordinary least squares (OLS) based on the variables included in the VAR model. The ratio 𝜎𝑖/𝜎𝑗 in the equation’s accounts for potential differences in scale between variables 𝑖 and 𝑗. The 𝜆<sup>′</sup> 𝑠 are parameters to set that control the tightness of the prior. The following values for the hyperparameters are set: 





The values of these parameters can be determined based on the forecast performance of the model. Moreover, the values of these hyperparameters can be determined using the marginal likelihood. 

The Minnesota prior offers a computationally efficient approach to deriving the posterior distribution of VAR coefficients. However, its principal limitation is the assumption of a known residual covariance matrix. A more general and flexible alternative is to employ a normal-Wishart prior distribution, which accounts for the uncertainty in both the 𝛽 coefficient parameters and the 𝛴 covariance matrix by treating them as unknown. The prior distribution of 𝛽 is assumed to be as a multivariate normal distribution. 



10 

Similar to the Minnesota prior, 𝛽0 is defined as a _q × 1_ vector, while 𝛷0 is a _k × k_ diagonal matrix. The residual variance-covariance matrix, 𝛴 implies that the Kronecker product 𝛴⊗𝛷0 yields a covariance matrix of dimension _nk × nk_ or equivalently _q × q_ . 

The prior for 𝛴 is an inverse Wishart distribution: 



Here, 𝑆0 is defined as the _n_ -scale matrix for the prior, whereas 𝛼0 specifies the prior degrees of freedom. 

## **4. DATA DESCRIPTION AND ESTIMATION** 

The following section provides a brief description of the main explanatory variables used in both BVAR and FAVAR models. These variables are selected based on their economic relevance to improve forecasting accuracy. The selection process is guided by economic theory, empirical studies and experience, ensuring that the models effectively capture the most important dynamics and determinants of inflation. 

**Table 1. BVAR variable structure.** 

|**Economic Sectors**|**Variables**|**Observed Series**|
|---|---|---|
|Prices|Domestic prices|Consumer Price Index (CPI)<br>Producer Price Index (PPI)|
|Economic Activity|Production|Real GDP Growth|
||Broad money|Money aggregate M2|
|Monetary Indicators|Interest rate|Interbank Money Market Rate|
||Loan|Loan stock in the economy|
||Competitiveness|Exchange rate (UZS to USD)|
|Fi Idi|Financial inflow|Remittance of Households|
|oregn ncators||Energy price index|
||Foreign prices|Non-energy price index|



11 

## _4.1 The BVAR model and data description_ 

A total of 10 explanatory variables are selected to ensure a good forecasting performance of the BVAR model. Three BVAR models are constructed based on economic theory and experience in analyzing factors influencing inflation dynamics. BVAR-5 incorporates the most important explanatory variables, BVAR-7 adds additional significant variables and BVAR-10 reflects impact of external prices on inflation. The rationale for categorizing the models into three groups is to assess whether the forecasting accuracy improves as more variables are included. We provide explanation of the variables and their relevance to various economic sectors in Table 1. 

The **real sector** variables reflects both supply and demand for goods and services in the economy. In the model, real GDP growth is included as an indicator of economic activity from the production side. Moreover, positive real GDP growth is associated with rising incomes, which in turn boosts demand for goods and services, thereby influencing price levels. 

**Table 2. BVAR model`s structure.** 

|**Variable Name**|**BVAR-5**|**BVAR-7**|**BVAR-10**|
|---|---|---|---|
|Consumer Price Index (CPI)||||
|Real GDP Growth||||
|Money aggregate M2||||
|Interbank Money Market Rate||||
|Exchange rate (UZS to USD)||||
|Loan stock in the economy||||
|Producer Price Index (PPI)||||
|Remittance of Households||||
|Energy price index||||
|Non-energy price index||||



12 

As for **price changes** in the economy, the model uses CPI data for forecasting inflation for the short-term period. The Producer Price Index (PPI) is included in the model. The producer price has pass-through effect into domestic prices, hence considered as one of the main determinants of inflation behavior. When prices for intermediate goods rise, these increases often pass to the final prices of goods with some time lag. The extent and speed of this pass-through depends on factors such as the economic structure, market competition, product types, consumer behavior etc. 

The model incorporates variables such as the interbank rate **,** broad money supply (M2) and loan stock in order to capture inflation determinants from the **monetary side.** The monetary policy transmission mechanism operates through the formation of interbank rates in the money market, that influences deposit and credit market rates. These changes ultimately impact household consumption and saving behaviors, as well as investment decisions made by businesses. 

**External factors** play a significant role in shaping economic structures and their indicators. In the model, external variables include exchange rate and remittance inflows. Exchange rate depreciation directly impacts consumer prices, particularly in economies heavily relied on imported goods. Conversely, remittance inflows act as a source of income for households, influencing their consumption behavior. The model also includes energy and non-energy price indices, given the substantial increase in import volumes over the past decade. 

The dataset for the BVAR model is a quarterly time series covering the period 2014Q1–2024Q2. Given the importance of the explanatory variables for inflation, the first BVAR model includes 5 variables, the second model includes 7 variables, and the third extended model covers 10 variables. The domestic variables are sourced from the Statistics Agency and the CBU, while external variables are obtained from World Bank statistics. 

Real GDP is measured as an annual growth rate. Inflation and producer price data are transformed into yearly changes, calculated using the CPI and PPI indices. These real GDP and price data are sourced from the Statistics Agency. The monetary indicators, such as M2, loan stock, and the interbank rate, are obtained from the CBU sources. The first two variables are nominal data and calculated as annual changes, whereas the interbank rate represents the cost of money over a one-year period. 

External variables as the exchange rate and remittance inflows are nominal data, calculated as yearly changes. These data are also available on the CBU’s website. The remaining two indicators, energy and non-energy prices, are expressed as annual rates, measured by changes in the relevant indices. These indices are available from the World Bank. 

## _4.2 The FAVAR model and data description_ 

The explanatory variables for the FAVAR model follow the same structure as those in the BVAR model but they are significantly expanded in terms of the number of variables included. The economic sectors covered by the model include economic activity, prices, monetary indicators and foreign variables, with a total of 42 variables. 

13 

The explanatory variables related to economic activity include wage and sub-components of the production index. The price sector comprises sub-components of the Producer Price Index (PPI). As for monetary indicators, variables are the same as those in the BVAR model. Foreign variables include the exchange rate, the real effective exchange rate, sub-components of the FAO Index, and sub-components of the World Bank Commodity Index. A brief information on detailed list of all variables and their corresponding economic sectors is available in the Appendix. 

The dataset for the FAVAR model consists of monthly time series data spanning the period from January 2018 to June 2024. Data sources include the Statistics Agency, Central Bank, FAO, and World Bank statistics. All data are converted into monthly changes, except for the monthly index of prices, production indices, and foreign price indices, which are already provided in terms of monthly changes. 

## _4.3 Forecast Procedure_ 

The entire sample period is divided into two parts: the estimation period and the forecast period. The estimation period includes data from 2014Q1 to 2023Q2, while the forecast period extends four quarters ahead, covering 2023Q3 to 2024Q2. Forecasts are conducted for all models using lags ranging from 1 to 4. The optimal lag is determined based on the overall performance of out-of-sample forecast errors. In selecting the lags, the focus is not solely on the forecast performance for individual quarters but rather on the overall performance across all four quarters. At the second stage, weighting is applied based on the forecast performance of each quarter. 

The precision of its central predictions is assessed by calculating the root mean squared errors (RMSE) in order to evaluate the model's forecasting performance. The RMSE at forecast horizon ℎ is expressed as: 



The forecast error, as defined in Equation (4.1), represents the difference between the observed data and the mean forecast for the corresponding period. Here, T denotes the total sample size, which is divided into an estimation period of length R and out-of-sample segment of length P. The forecast horizon is represented by h. 

The benchmark model - the Bayesian AR model is used to assess the model performance comparing the forecast results of the BVAR and FAVAR models. This comparison facilitates a more robust evaluation of the forecasting performance. 

14 

## **5. EMPIRICAL RESULTS** 

## _5.1 Evaluating BVAR point forecast performance_ 

The benchmark model of the Bayesian-AR with one lag demonstrates superior forecast performance compared to other lags. This model with one lag is therefore used as a reference for evaluating the forecast performance of other models. When analyzing forecast performance by each quarter, the benchmark model with lag 1 outperformed other lags in periods one and four, while models with lags 2 and 3 showed better performance in periods two and three, respectively. 

The BVAR-5 shows that the estimation of the model with four lags achieved the lowest overall out-of-sample forecast error. The model with lag 1 performed best in period one, while lag 2 outperformed in periods two and four. 

The BVAR-7 model demonstrates that the model with two lags had the lowest overall forecast error. Lag 1 performed best in period one, lag 2 delivered better results in periods two and four, and lag 4 outperformed in period three. 

The BVAR-10 model shows that the model with two lags had the lowest overall out-ofsample forecast errors. In periods one and two, the model with lag 1 performed best, while lag 2 performed well in periods three and four. 

## _5.2 Evaluating FAVAR point forecast performance_ 

The FAVAR model was also applied to identify the lag that achieves the best forecasting performance for the entire forecast period. The model with lag 1 demonstrated the best overall forecasting power and performed well in periods one and three. However, lag 2 had the lowest forecast errors in period four, while lag 3 showed superior performance in period two. 

As discussed, we have determined the lags that show superior out-of-sample forecasting performance. In the next stage, we compare the BVAR and FAVAR models with the benchmark model. The estimation results indicate that, over the entire forecast horizon, the FAVAR model outperformed both the benchmark model and the BVAR models, achieving a root mean squared error (RMSE) of approximately 0.7 points. 

However, when considering the forecasting errors for individual forecast horizons, it can be observed that in period one, the benchmark model outperformed all other models. In periods two and three, the BVAR-7 and BVAR-10 models had the lowest forecast errors. This result may be explained by the inclusion of additional variables, such as loan stock and producer price index, as well as external factors (remittances, energy prices, and non-energy prices), which enhance the models’ ability to capture the dynamics of inflation during these forecast horizons. 

15 

## _5.3 Evaluating the Forecast Combination_ 

This section presents the empirical results of forecast combination, performed using two approaches: (i) averaging the out-of-sample forecast results and (ii) weighting based on the outof-sample forecast errors. 

Both combination methods are applied to the BVAR and FAVAR models. The results indicate that, for the BVAR models, the averaging method performs slightly less accurately compared to the weighting method. However, the individual BVAR-5 model with two lags outperforms both combination methods. 

For the FAVAR model, the forecast combination is conducted within the model using different lag structures. The results exhibit a similar pattern to the BVAR models, with the weighting method yielding lower forecast errors than the averaging method. Unlike the BVAR models, however, the weighting method for FAVAR not only outperforms all other lag specifications but also surpasses the performance of all BVAR models. This result highlights the advantage of the FAVAR model, as it captures latent factors from a large dataset, thereby improving forecasting accuracy. 

It is worth noting that when out-of-sample forecast results from both the FAVAR and BVAR models are combined, the forecast errors do not decrease. This outcome is attributed to the higher forecast errors of the BVAR models compared to the FAVAR models. Consequently, it is more effective to rely on the individual forecast results with the lowest forecast errors rather than attempting to combine forecasts from both models. 

## **6. CONCLUSION AND FINAL REMARKS** 

This study provides a comprehensive evaluation of the forecasting performance of the BVAR and the FAVAR models, focusing on point forecasting for short-term inflation. By examining these models across various lag structures, forecast horizons, and combination methods, the study identifies effective approaches improving forecast accuracy and highlighting key insights into inflation dynamics and methodological refinements. 

## _Performance of BVAR Models_ 

The forecasting accuracy of the BVAR models is influenced by lag selection and forecast horizons. Among the models analyzed, the BVAR-5 with two lags consistently delivered the lowest forecast errors in several periods, underscoring the critical role of selecting appropriate lags for effectively capturing inflation dynamics. However, the performance of BVAR models varied across forecast horizons, reflecting the importance of aligning lag selection with the specific characteristics of the data and the forecast period. For example, while the BVAR-5 performed best in period one, BVAR-7 and BVAR-10 with two lags showed better performance in later periods. 

16 

## _Performance of the FAVAR Models_ 

The FAVAR model demonstrated superior forecasting accuracy across all horizons, outperforming the BVAR models. This advantage likely stems from its ability to incorporate latent factors derived from extensive datasets, allowing it to capture a wider range of economic dynamics influencing inflation. The FAVAR model performed well in periods two and three. 

## _Forecast Combination Techniques_ 

The study also evaluated forecast combination methods, including averaging and weighting based on forecast errors. For the BVAR models, weighting generally outperformed averaging but provided only marginal improvements. For the FAVAR model, the weighted combination approach consistently outperformed averaging and achieved lower forecast errors than any BVAR models. Combining forecasts from both models did not reduce errors due to the higher forecast errors of the BVAR compared to the FAVAR models, suggesting that relying on the best-performing individual model, particularly the FAVAR model is a more effective strategy. 

## _Implications for Inflation Forecasting_ 

The findings have important implications for inflation forecasting. First, the FAVAR model's superior performance highlights the value of incorporating latent factors and additional macroeconomic variables to enhance accuracy and deepen understanding of inflation drivers. Second, BVAR models, while flexible, are highly sensitive to lag selection, making them less reliable unless carefully specified. Third, weighted forecast combinations offer potential for improved accuracy, particularly when leveraging complementary model strengths. Further research on hybrid models or advanced Bayesian averaging techniques could enhance forecast performance by combining the strengths of both approaches. 

## _Final Remarks_ 

In summary, this study underscores the superior performance of the FAVAR model in short-term inflation forecasting due to its ability to incorporate latent factors and a broader range of macroeconomic variables. At the same time, it highlights the importance of careful model specification, optimal lag selection, and effective forecast combination techniques. By addressing these factors, future research can build on the insights provided here to further refine inflation forecasting methodologies and improve predictive performance. 

17 

## **REFERENCES** 

Ajevskis, V., & Davidsons, G. (2008). Application of factor models for forecasting GDP and inflation in Latvia. Bank of Latvia Working Paper Series. 

Akdogan, K., Beser, S., Chadwick, M.G., Ertug, D., Hulagu, T., Kosem, S., Ogunc, F., Ozmen, M.U and Tekalti, N. (2012). “Short-term Inflation Forecasting Models for Turkey and a Forecast Combination Analysis”, Turkiye Cumhuriyet Merkez Bankasi Working Paper No 12/09. 

Bai, J., & Ng, S. (2007). Determining the number of primitive shocks in factor models. Journal of Econometrics, 133(1), 123–150. 

Banbura, M., Giannone, D., & Reichlin, L. (2010). Large Bayesian vector auto regressions. Journal of Applied Econometrics, 25(1), 71–92. 

Bernanke, B. S., Boivin, J., & Eliasz, P. (2005). Measuring the effects of monetary policy: A factor-augmented vector autoregressive (FAVAR) approach. Quarterly Journal of Economics, 120(1), 387–422. 

Carriero, A., Clark, T. E., & Marcellino, M. (2011). Bayesian VARs: Specification choices and forecast accuracy. Journal of Applied Econometrics, 26(2), 238–273. 

Christoffel, K., Coenen, G., & Warne, A. (2011). Forecasting with DSGE models and Bayesian VARs. International Journal of Forecasting, 27(4), 1075–1105. 

Günay, M. (2018). Using factor models to forecast industrial production and core inflation in Turkey. Central Bank of Turkey Working Papers. 

Litterman, R.B. (1985), “Forecasting with Bayesian Vector Autoregressions – Five years of experience”, Federal Reserve Bank of Minneapolis, Working Paper 274. 

Reigl, N. (2017). Forecasting the Estonian rate of inflation using factor models. Baltic Journal of Economics, Vol. 17, No. 2, pp. 152–189. 

Stock, J. H., & Watson, M. W. (2002). Macroeconomic forecasting using diffusion indexes. Journal of Business & Economic Statistics, 20(2), 147–162. 

Vika, I. (2018), “Practical issues in forecasting with vector autoregressions”, Economic Review, 2018 H2. 

Waggoner, D. F. and Zha, T. (1999). Conditional forecasts in dynamic multivariate models. The Review of Economics and Statistics, 81(4):639{651}. 

18 

## **APPENDIX** 

**Table 3. FAVAR model variables** 

|**Economic Sectors**|**Selected Variables**|
|---|---|
||Consumer Price Index|
||Producer Price Index|
||_PPI sub-components:_|
||Transport|
||Food products|
||Beverages|
||Textiles|
|**Prices**|Chemical products|
||Coke refined petroleum|
||Non-metallic mineral|
||Metallurgical industry|
||Fabricated metal|
||Electrical equipment|
||Motor vehicles|
||Supply gas vapor air conditioning|
||Water supply recycling of waste|
||Wage|
||_Production index sub-components:_|
||Foodproducts|
||Beverages|
||Tobacco|
||Textiles|
|**Ei tiit**|Wearingapparel|
|**conomc acvy**|Leather|
||Wood andproducts of wood|
||Paperproducts|
||Printingand reproduction|
||Refinedpetroleumproducts|
||Chemicalproducts|
||Pharmachemicals|



19 

||Plastics|
|---|---|
||Mineralproducts|
||Metallurgy|
||Fabricated metal|
||Computer electronic and optical|
||Electrical equipment|
||Machineryand equipment|
||Motor vehicles trailers|
||Transport equipment|
||Furniture|
||Other manufacturing|
||Repair and installation|
||Electricity gas|
||Water supply|
||Interbank MoneyMarket Rate|
|**Monetar indicators**|Moneyaggregate M2|
|**y**|Loan stock in the economy|
||New loan to the economy|
||Exchange rate (UZS to USD)|
||Real effective exchange rate|
||_Foreign prices:_|
||Meat|
||Dairy|
||Cereals|
|**Foreign indicators**|Oils|
||Sugar|
||Energy|
||Beverages|
||Raw materials|
||Fertilizer|
||Metals minerals|



20 

## **Table 4. Optimal lag selection based on the model forecast performance** 





|**BVAR-5**|**2023Q3**|**2023Q4**<br>**For**|**2024Q1 **<br>**ecast ho**|**2024Q2 **<br>**rizon**|**Overall**|
|---|---|---|---|---|---|
|Lag 1<br>Lag 2|0.27<br>0.40|0.21<br>0.13|1.21<br>1.18|1.22<br>1.14|0.88<br>0.85|
|Lag 3|0.53|0.18|0.87|1.35|0.85|
|Lag 4|0.57|0.31|0.75|1.36|0.84|



|**Bayesian-AR**|**2023Q3 **|**2023Q4 **<br>**Fore**|**2024Q1 **<br>**cast hor**|**2024Q2 **<br>**izon**|**Overall**<br>**B**|
|---|---|---|---|---|---|
|Lag 1|0.09|0.79|1.67|0.87|1.02|
|Lag 2|0.99|0.67|0.33|1.95|1.15|
|Lag 3|0.93|0.94|0.01|2.39|1.37|
|Lag 4|0.90|0.81|0.01|2.42|1.35|







|Lag 1<br>**BVAR-10**|**2023Q3**<br>0.91|**2023Q4**<br>0.77<br>**For**|**2024Q1 **<br>0.04<br>**ecast ho**|**2024Q2 **<br>2.44<br>**rizon**|**Overall**<br>1.36|
|---|---|---|---|---|---|
|Lag 2|0.99|0.91|0.03|2.30|1.33|
|Lag 3|1.14|1.25|0.32|2.59|1.56|
|Lag 4|10.20|27.51|17.74|50.78|26.56|



|**BVAR-7**|**2023Q3 **|**2023Q4 **<br>**Fore**|**2024Q1 **<br>**cast hor**|**2024Q2 **<br>**izon**|**Overall**<br>**B**|
|---|---|---|---|---|---|
|Lag 1|0.28|0.19|1.08|1.45|0.92|
|Lag 2|0.46|0.08|1.07|1.27|0.86|
|Lag 3|0.62|0.33|0.71|1.58|0.93|
|Lag 4|0.66|0.34|0.69|1.43|0.88|





|**FAVAR**|**2023Q3**|**2023Q4**<br>**For**|**2024Q1**<br>**ecast hor**|**2024Q2**<br>**izon**|**Overall**|
|---|---|---|---|---|---|
|Lag 1|0.42|0.25|0.39|1.28|0.71|
|Lag 2|0.47|0.14|0.44|1.28|0.72|
|Lag 3|0.66|0.10|0.45|1.29|0.76|
|Lag 4|0.71|0.18|0.40|1.31|0.78|



21 

**Table 5. Forecast performance compared with the benchmark model** 



|**FAVAR**|**2023Q3**|**2023Q4**<br>**For**|**2024Q1**<br>**ecast hor**|**2024Q2**<br>**izon**|**Overall**|
|---|---|---|---|---|---|
|BVAR-5<br>BVAR-7|4.65<br>5.24|0.16<br>0.10|0.70<br>0.64|1.32<br>1.47|0.83<br>0.84|
|BVAR-10|11.36|1.16|0.02|2.66|1.30|
|FAVAR|4.81|0.32|0.23|1.48|0.70|



**Table 6. Forecast combination for BVAR and FAVAR models** 





|**BVAR models**|**2023Q3 **|**2023Q4 **<br>**Fore**|**2024Q1 **<br>**cast hori**|**2024Q2 **<br>**zon**|**Overall**|Lag 1<br>**FAVAR**|**2023Q3 **<br>0.42|**2023Q4 **<br>0.25<br>**Fore**|**2024Q1 **<br>0.39<br>**cast hor**|**2024Q2 **<br>1.28<br>**izon**|**Overall**<br>0.71|
|---|---|---|---|---|---|---|---|---|---|---|---|
|BVAR-5|0.40|0.13|1.18|1.14|0.85|||||||
|||||||Lag 2|0.47|0.14|0.44|1.28|0.72|
|BVAR-7|0.46|0.08|1.07|1.27|0.86|Lag 3|0.66|0.10|0.45|1.29|0.76|
|BVAR-10|0.91|0.77|0.04|2.44|1.36|Lag 4|0.71|0.18|0.40|1.31|0.78|
|**Forecast**<br>**combination**<br>**(Averaging)**|**0.59**|**0.33**|**0.76**|**1.62**|**1.02**|**Forecast**<br>**combination**<br>**(Averaging)**|**0.56**|**0.17**|**0.42**|**1.29**|**0.74**|
|**Comparison with**<br>**Bayesian-AR**|**6.79**|**0.41**|**0.45**|**1.87**|**1.00**|**Comparison with**<br>**Bayesian-AR**|**6.50**|**0.21**|**0.25**|**1.49**|**0.73**|



22 

**Graph 1. Bayesian AR with lag 1** 







**Graph 2. Bayesian AR with lag 2** 







**Graph 3. Bayesian AR with lag 3** 







23 

**Graph 4. Bayesian AR with lag 4** 







**Graph 5. BVAR-5 with lag 1** 







**Graph 6. BVAR-5 with lag 2** 







24 

**Graph 7. BVAR-5 with lag 3** 







## **Graph 8. BVAR-5 with lag 4** 







**Graph 9. BVAR-7 with lag 1** 







25 

**Graph 10. BVAR-7 with lag 2** 







**Graph 11. BVAR-7 with lag 3** 







**Graph 12. BVAR-7 with lag 4** 







26 

**Graph 13. BVAR-10 with lag 1** 







**Graph 14. BVAR-10 with lag 2** 







**Graph 15. BVAR-10 with lag 3** 





> <sup>`</sup> 



27 

**Graph 16. FAVAR with lag 1** 





**Graph 17. FAVAR with lag 2** 





28 

**Graph 18. FAVAR with lag 3** 





**Graph 19. FAVAR with lag 4** 





29 

