---
title: Martinez_Forecasting housing investment_2023
type: paper
source_pdf: raw/papers/Martinez_Forecasting housing investment_2023.pdf
converted: 2026-08-18
---



# **Working Paper Series** 

> Carlos Cañizares Martínez, Gabe J. de Bondt, Forecasting housing investment Arne Gieseck 



<!-- Start of picture text -->
No 2807<br><!-- End of picture text -->

**Disclaimer:** This paper should not be reported as representing the views of the European Central Bank (ECB). The views expressed are those of the authors and do not necessarily reflect those of the ECB. 

### **Abstract** 

This study applies a model averaging approach to conditionally forecast housing investment in the largest euro area countries and the euro area. To account for substantial modelling uncertainty, it estimates many vector error correction models (VECMs) using a wide set of short and long-run determinants and selects the most promising specifications based on in-sample and out-of-sample criteria. Our results highlight marked cross-country heterogeneity in the key drivers of housing investment which calls for country-specific housing market policies. A pseudo out-of-sample forecast exercise shows that our model averaging approach beats a battery of ambitious benchmark models, including BVARs, FAVARs, LASSO and Ridge regressions. This suggests that there is ample scope for model averaging tools in forecast exercises, notably as they also help to reduce model uncertainty and can be used to assess forecast uncertainty. 

**_Keywords_ :** Housing investment, model and forecast averaging, Tobin’s Q, VECM 

**_JEL Codes_ :** C32, C51, C52, C53, E22 

ECB Working Paper Series No 2807 

1 

## **Non-technical summary** 

Housing investment is widely monitored by forecasters, analysts, and policymakers across the globe due to its central importance for the economy. Yet, despite its importance for the economy and economic policy, the literature neither provides a clear-cut commonly agreed theoretical framework to model and forecast housing investment nor is there an agreement on its empirical determinants. Indeed, housing investment seem to be subject to relevant modelling challenges. Against this background, the aim of this study is to provide a uniform model averaging tool for conditionally forecasting housing investment for the euro area and its five largest countries. 

To account for model uncertainty, we propose a model averaging approach in which we estimate a large and diverse number of vector error correction models (VECMs) using a wide set of short and long-run determinants and apply subset selection based on in-sample and pseudo out-of-sample criteria. Finally, we average housing investment using the most accurate 50 models using a simple average. In this way, we exploit the forecasting performance of VECMs, enjoy the economic intuitions provided by error correction models and mitigate model uncertainty by averaging among forecasts obtained after estimating a diverse set of specifications. 

Two alternative specifications are explored. Our first specification is without any theoretical restrictions, i.e., we let a broad dataset speak. It considers equations where three long-run and up to four short-run determinants are freely estimated. The former includes various measures of Tobin’s Q (house price relative to another price index), income and credit measures. An innovation to the literature is that we consider also a housing affordability index as income measure. The short-run model set includes mortgage interest rates, a group of macroeconomic variables, uncertainty measures and unemployment rate, demographics and wealth. The starting point of our second specification is to assume a unit coefficient in the long run for Tobin’s Q measures and income variables. For both approaches, the same in- and out-of-sample selection criteria are applied. Our focus is on the average over the top 50 models rather than selecting the single “best” model, because the literature shows that averaging provides better predictive performance in practice. To the best of our knowledge, it is for the first time that such a flexible and encompassing model averaging tool is applied to forecasting housing investment in the euro area countries. 

Our study provides forecasters guidance about modelling housing investment in four ways. Firstly, a pseudo-out-of-sample forecast exercise shows that – across euro area countries and for the euro area - our model averaging approach significantly beats a battery of distinguished benchmark models, including BVARs using a small dataset, and FAVARs as well as machine learning techniques such as LASSO and Ridge regressions, exploiting our full dataset of 27 variables. Secondly, our model averaging tool provides robust guidance on the most promising long- and short-run determinants of housing investment. Loans to house purchase feature prominently as key long-run determinant for housing investment in the euro area and across most countries. It might also pay off for forecasters to include a housing affordability index into their models. Our results could be used to improve other forecasting models by comparing our selected equations with the equations used in these other models. Thirdly, there is substantial cross-country diversity 

ECB Working Paper Series No 2807 

2 

as concerns the significance of mortgage interest rates as a short-run determinant, which is found to be significantly negative in France and Italy, and insignificant in the other countries, where they could still play a role via the housing affordability index. Fourthly, our results suggest that the restriction of Tobin´s Q and income to one can substantially help in housing investment equations; a substantially larger number of restricted equations passed the in-sample and out-of-sample selection criteria, they beat the benchmark models much more often than the unrestricted specifications, and the top 50 restricted models consistently showed the best overall forecasting performance. This should please forecasters as restricted models also improve the narrative of the housing investment projections. 

Moreover, our tool can be used to assess the plausibility of and the risks to other projections of housing investment.  Overall, this paper might contribute to the improvement of both time series models used by forecasters and the housing blocks of semi-structural macro models of euro area central banks and other (policy) institutions. 

ECB Working Paper Series No 2807 

3 

## **1. Introduction** 

Housing investment is widely monitored by forecasters, analysts, and policymakers across the globe due to its central importance for the economy. For private households, housing investment often constitutes their largest lifetime investment and accounts for most of their wealth. For forecasters and analysts, housing investment is a significant and volatile component of aggregate demand (Nguyen, 2013), and an important driver of the business cycle (Huang et al., 2020; Leamer, 2015; Piazzesi and Schneider, 2016), including for the prediction of recessions (Aastveit et al., 2019; Kohlscheen et al., 2018). Changes to housing wealth have significant implications for private consumption spending (de Bondt et al., 2020 and 2021) and, as the Great Recession of 2008-09 has shown once again, housing booms usually develop into a recession, and when combined with a credit boom they predict a harder landing (Cerutti et al., 2017). For monetary policymakers, the transmission of policy changes into lending rates and, via housing investment and house prices, into economic activity is as much of importance as the interaction between housing markets and the credit cycle for macroprudential policies (European Systemic Risk Board, 2022). For fiscal policymakers, succeeding in smoothing housing investment cycles might significantly ease the path in the context of a green transition. 

Yet, despite its importance for the economy and economic policy, the literature neither provides a clearcut commonly agreed theoretical framework to model and forecast housing investment nor is there an agreement on its empirical determinants. The range of possible determinants of housing investment is wide and the estimated parameters differ significantly in terms of value and significance, within countries and across countries. In a similar vein, housing investment and the whole housing blocks of central bank macro models seem to be subject to relevant modelling challenges (Muellbauer, 2022). 

Against this background, the aim of this study is to provide a uniform model averaging tool for conditionally forecasting housing investment for the euro area and its five largest countries. The interest of professional forecasters – as exhibited by the large number of projections available for the largest euro area countries – as well as euro area policy makers is also typically focused on its largest member states. Germany, France, Italy, Spain, and the Netherlands account for a representative 87% of euro area housing investment. These five countries provide a reasonably general test to our tool given the structural differences they exhibit. 

To account for model uncertainty, we propose a model averaging approach in which we estimate a large and diverse number of vector error correction models (VECMs) using a wide set of short and long-run determinants and apply subset selection based on in-sample and pseudo out-of-sample criteria. Finally, we average housing investment using the most accurate 50 models using a simple average. In this way, we exploit the forecasting performance of VECMs, enjoy the economic intuitions provided by error correction models and mitigate model uncertainty by averaging among forecasts obtained after estimating a diverse set of specifications. To the best of our knowledge, it is for the first time that such a flexible and encompassing model averaging tool is applied to forecasting housing investment in the euro area countries. 

The main result of this study is that our model averaging forecasts of housing investment beat a battery of ambitious distinguished benchmark models. These benchmarks include Bayesian Vector Autoregressive 

ECB Working Paper Series No 2807 

4 

models (BVARs), Factor-Augmented VARs (FAVARs), Least Absolute Shrinkage and Selection Operator (LASSO) and Ridge regressions. The latter three benchmark models exploit our full list of 27 housing investment determinants. This outcome is along the lines of previous studies reporting robust forecasting gains obtained by using forecast combinations both in academia and in international forecasting competitions (see, e.g., Moral-Benito, 2015; Aye et al., 2016; Steel, 2019; Makridakis et al., 2020; Wang et al., 2022). 

Another promising result for forecasters is that our model averaging tool provides robust guidance on the most promising long- and short-run determinants of housing investment. Our results could be used to improve other forecasting models by comparing our selected equations with the equations used in these other models.  Moreover, our tool can be used to assess the plausibility of and the risks to other projections of housing investment.  Overall, this paper might contribute to the improvement of both time series models used by forecasters and the housing blocks of semi-structural macro models of euro area central banks and other (policy) institutions. 

This paper is structured as follows. Section 2 reviews the literature, focusing on the determinants of housing investment. Section 3 describes the empirical methodology and Section 4 the data. Section 5 reports the results in terms of numbers of selected equations, estimates, and out-of-sample forecast performance, including for the COVID-19 pandemic. Section 6 concludes. 

## **2. Literature** 

This section reviews the literature on forecasting housing investment in euro area countries and the euro area. Empirical modelling studies in this field are relatively limited; while many studies analyse house prices, studies modelling housing investment are comparatively rare. Table 1 provides a summary of housing investment studies results for the five largest euro area countries and the euro area, focusing on the empirical estimates of long-run housing investment determinants. Five remarks emerge. 

Firstly, while almost all studies explore an error correction type of model, there is no clear-cut agreement on the long-run drivers of housing investment. There is thus common agreement among modellers to distinguish between short and long-run effects, but no consensus on the long-run driving factors of housing investment. A practical challenge in this setup arises in countries where a cointegration relationship is not found, as shown by Kajuth (2020) and Vermeulen and Rouwendal (2007) for Germany and the Netherlands, respectively. 

Secondly, the most common long-run determinant is house prices, either considered alone or as part of a Tobin’s Q measure, i.e., the house price relative to another price capturing the construction cost of housing. Housing researchers use Tobin’s Q, with variety on how Q is empirically measured: ratio between house prices and prices of alternative construction projects (Poterba, 1983); ratio between existing to newhome prices (Jud and Winkler, 2003); and ratio between house prices and a measure of construction costs (Antipa, Lecat 2009; Bulligan et al. 2017; Kajuth, 2020). 

ECB Working Paper Series No 2807 

5 

Thirdly, the availability and/or the cost of credit is part of most studies, however the fact that credit is not so often considered seems to be an important omission (Muellbauer, 2022). Indeed, households often decide on their housing purchase once they have access to sufficient credit. Interestingly, estimates report positive as well as negative long-run credit effects. Negative long-term credit effects, albeit _prima facie_ counterintuitive, are in line with historical evidence (Kohl, 2021; Bezemer et al., 2016), and are related to a narrative of indebted demand (Mian et al., 2021), over indebtedness or cyclical exuberance in credit markets.<sup>1</sup> 

Fourthly, household income and/or housing affordability measures are not among the long-run determinants of housing investment in most studies, which seems counterintuitive as household income is most often the ultimate source of funds for households to repay mortgages. Instead, some studies consider macroeconomic proxies such as real GDP or private consumption despite that GDP includes housing investment and private consumption is only a rough proxy for household income. 

Finally, several studies in our overview refer to estimates of a residential investment equation as used in semi-structural models for policy and forecasting. Some of these models might provide an incomplete coverage of housing channels via credit and housing affordability, as stressed by Muellbauer (2022). In our empirical framework as described in the next section we therefore consider a large set of variables including such channels and apply a model averaging approach to deal with the model uncertainty that emerges from our literature overview. 

Insert Table 1 (landscape) here 

## **3. Empirical methodology** 

### _3.1 Model averaging_ 

Three challenges in this study shape our empirical methodology. Firstly, the literature overview shows the lack of a common agreed theoretical framework. It implies that we are unsure about the “best model”. Secondly, there is an unusually wide variety in housing investment determinants considered in empirical studies. This finding implies that we are unsure about the “true determinants”. Thirdly, given the country heterogeneity we are unsure about the “right” country treatment. All three challenges add to model uncertainty and support the usage of model averaging, with a uniform general-to-specific approach for all the countries. 

Indeed, model averaging emerges as a natural candidate to be exploited in our conditional forecasting exercise, given the robust performance of this technique versus a single “best” model approach as reported in the literature (Moral-Benito, 2015; Steel, 2019; Makridakis et al., 2020; Wang et al., 2022). Essentially, forecast combinations involve two steps. First, the estimation of a possibly large set of models potentially 

> 1 Expansionary policies generate a debt-financed short-run boom at the expense of indebted demand in the future (Panagopoulos and Vlamis, 2009). Other evidence in support of a strong link between credit and residential investment or credit and the housing market in general is for example reported for Greece (Karousos and Vlamis, 2008; Vlamis, 2014). 

ECB Working Paper Series No 2807 

6 

able to produce some accurate but diverse forecasts (see subsection 3.2). Second, the application of a subset selection procedure to filter the number of forecasts used in the forecast averaging, given that there are decreasing returns to adding additional forecasts (see subsection 3.3). 

The most common technique of subset selection is to include only the most accurate methods in the combination, discarding the worst-performing individual forecasts (Wang et al., 2022). Empirical evidence and extensive simulations repeatedly show that the simple average with equal weights often outperforms more complicated weighting schemes. Over fifty years after Bates and Granger’s (1969) pioneering work on forecast combinations, empirical studies consistently show that simple averaging repeatedly dominates more sophisticated weighted combinations which are theoretically preferred (Makridakis et al., 2020), posing a tough benchmark to beat. The literature is unconclusive about how many forecasts should be sufficient. As explained more in depth in the following subsections, after applying some selection criteria regarding cointegration, autocorrelation and economic plausibility, our focus is on the top 50 equations in terms of a pseudo out-of-sample forecast performance exercise. Therefore, we finally average over a subset of 50 model forecasts, which is in our view sufficiently large in practice. For example, model averaging using the Occam’s window reduces in many practical cases the number of models to fewer than 25 (Clyde, 1999). 

### _3.2 Specification_ 

The starting point for our model specifications is an investment adjustment process with all variables in log real terms, i.e., deflated by the private consumption deflator. Denoting _it_ as housing investment in period t, we follow the common assumption that housing investment is non-stationary in levels but stationary in growth terms. The optimal or target investment level, _i*,_ is unobserved and must be inferred from the data. The desired investment is written as a linear function of its determinants: ∗ ) (1) As reported in the forecast combinations literature, using different sources of information to generate 𝑖𝑖𝑡𝑡 = 𝑓𝑓(𝑥𝑥𝑡𝑡 forecasts, for example by employing different variables to produce them, is one way to generate diversity that in turn proves to be key for exploiting the potential model averaging forecast gains (Atiya, 2020). Along these lines, and regarding the long-run determinants of housing investment, we include the widely applied determinants of Tobin’s Q, _q_ , (house price relative to another price index), income, _y_ , and credit, _c_ . We thus extend the Q theory by including income and credit as well. The addition of income and credit addresses the main critique of Muellbauer (2022) of the omission of variables, features and interrelations related to the housing sector, including mortgage debt and affordability measures. Various measures for each determinant are considered to acknowledge uncertainty about its measurement: four measures of Tobin’s Q, always the residential property price but relative to different other price indices; and five measures of income: real disposable income per household, labour income, total compensation, compensation per employee and a housing affordability index. The latter is to the best of our knowledge for the first time considered as a potential determinant of housing investment in euro area countries and the euro area. It is 

ECB Working Paper Series No 2807 

7 

calculated in line with an index published by the National Association of Realtors and combines the joint impact of income, house prices and mortgage rates in one variable.<sup>2</sup> The credit group contains three measures: mortgages, mortgage credit to disposable income ratio and loan to value ratio. The latter is calculated as the ratio between mortgages and housing wealth. The long-run specification for housing investment is then formulated as follows: 

1 2 3 4 𝑡𝑡 𝑡𝑡 𝑡𝑡 𝑡𝑡 𝑡𝑡 𝑖𝑖 = 𝛾𝛾 + 𝛾𝛾 𝑞𝑞 + 𝛾𝛾 𝑦𝑦 + 𝛾𝛾 𝑐𝑐 + 𝜖𝜖 



A priori expectations for the coefficient signs are: γ1, γ4 can be any sign; and γ2, γ3 > 0 The long-run model residual ϵ measures the deviation from the long-run relationship and tracks the level of over or under investment compared to target and is a mean zero stochastic innovation. In Eq. (2) the housing investment level is optimally adjusted without any time lag, but lags in this adjustment process are expected. The model incorporates an error correction process to take account of a slow adjustment of housing investment this adjustment process. Therefore short-run determinants, _x_ , are additionally considered, resulting in the following specification: 1 2 3 4 5 + ⅟0 (3) 𝑡𝑡 𝑡𝑡 𝑡𝑡 𝑡𝑡 𝑡𝑡−1 𝑡𝑡−1 𝑖𝑖 𝑖𝑖,𝑡𝑡−𝑗𝑗 𝑡𝑡 𝛥𝛥𝑖𝑖 A wide range of potential short-run determinants is considered, divided into four categories: (i) mortgage = 𝛽𝛽 + 𝛽𝛽 𝛥𝛥𝑞𝑞 + 𝛽𝛽 𝛥𝛥𝑦𝑦 + 𝛽𝛽 𝛥𝛥𝑐𝑐 + 𝛽𝛽 𝛥𝛥𝑖𝑖 𝜖𝜖 + 𝛿𝛿 𝛥𝛥𝑥𝑥 + 𝜇𝜇 

A wide range of potential short-run determinants is considered, divided into four categories: (i) mortgage interest rates, _mr_ ; (ii) macroeconomic indicators, _ma_ ; (iii) demographics and wealth, _w_ ; and (iv) unemployment rate and uncertainty measures, _un_ . Mortgage rates are always included, whereas this is not necessarily the case for the other categories. Within each category between 3 to 4 series are considered. Table A1 in the Appendix provides the details about these short-run model variables. Three uncertainty measures are, to the best of our knowledge for the first time included for euro area countries. They are calculated as the volatility of the stock market, unemployment, respectively, disposable income. Theoretically, increased uncertainty should lower housing investment. Empirically, finding a proxy for uncertainty has proven problematic, but results for the US indicate that uncertainty indeed has a negative impact on housing starts (Miles, 2009). The unemployment rate is not only a labour market indicator, but it also has a close link with consumer confidence. 

Eq. (3) is an ECM type of specification. The term error-correction relates to the fact that the previous period deviation from the long-run equilibrium, the error, influences its short-run dynamics. ECMs directly estimate the speed at which housing investment returns to equilibrium after a change in other variables. This framework is useful for estimating both short-run and long-run effects of one time series on housing investment. We prefer to estimate Eq. (3) in a vector-based Johansen system, implying a 4-variable VECM, where our focus is on the housing investment equation. Besides common practice, multivariate models seem better equipped to deal with large variations in some variables, for example due to COVID-19 (Bobeica and Hartwig, 2021). They also combine the forecasting power and flexibility of VARs, with the additional economic intuitions that ECMs provide in terms of long-run and short-run narrative speed of 

> 2 It is calculated as follows: Housing affordability index (HAFI) = 100 * monthly household income (PYNH) / monthly qualifying income (PYNQ), with PYNH calculated using Eurostat data on the number of households, and PYNQ calculated as 4 * monthly down-payment (derived assuming an initial down-payment of 20% and applying the composite mortgage rate). See Frayne et al. (2022) for an in-depth analysis of housing affordability in the euro area. 

ECB Working Paper Series No 2807 

8 

adjustment. We uniformly apply 2 lags, as more lags are too demanding for the comparatively short sample. The estimated unrestricted (UN) specification reads then as follows: 0 1𝛥 2𝛥 3 4 21<sup>𝛥𝛥𝑞𝑞+ 𝛽𝛽</sup> 22<sup>𝛥𝛥𝑞𝑞+ 𝛽𝛽</sup> 31<sup>𝛥𝛥𝑦𝑦+ 𝛽𝛽</sup> 32<sup>𝛥𝛥𝑦𝑦+</sup> 41 𝑡𝑡 42 𝑡𝑡 0 2 𝑡𝑡 0 3 𝑡𝑡 0 4 𝑡𝑡<sup>+ 𝛽𝛽</sup> 0 𝑡𝑡−1 1 𝑡𝑡−2 2 𝑡𝑡−1 𝑡𝑡−2 (4) 𝛥𝛥𝑖𝑖 = 𝛼𝛼 + 𝛼𝛼 𝛥𝛥 + 𝛼𝛼 𝛥𝛥 + 𝛼𝛼 𝛥𝛥𝑤𝑤 + 𝛼𝛼 𝛥𝛥𝑢 𝛽𝛽 In addition to the fully unrestricted approach defined by Eq. (4), we also explore another avenue that 𝛥𝛥𝑐𝑐𝑡𝑡−1 + 𝛽𝛽 𝛥𝛥𝑐𝑐𝑡𝑡−2 −𝛾𝛾 𝛾𝛾 𝑞𝑞𝑡𝑡−1 −𝛾𝛾 𝛾𝛾 𝑦𝑦𝑡𝑡−1 −𝛾𝛾 𝛾𝛾 𝑐𝑐𝑡𝑡−1 + 𝛾𝛾 𝑖𝑖𝑡𝑡−1 + 𝛿𝛿 𝛥𝛥𝑖𝑖𝑖𝑖,𝑡𝑡−1 + 𝛿𝛿 𝛥𝛥𝑖𝑖𝑖𝑖,𝑡𝑡−2 + 𝜇𝜇𝑡𝑡 

In addition to the fully unrestricted approach defined by Eq. (4), we also explore another avenue that puts structure on the long-run co-integration relation by restricting the long-term coefficients of Tobin’s Q and income to one. This might help in finding plausible long-run relationships, particularly if the sample contains episodes of housing bubbles. Moreover, both restrictions notably help building a narrative of the projections. The restricted version assumes in line with Tobin’s Q theory a one-to-one relation between investment and Q as well as a constant investment-to-income ratio in the long run.  A long-run Tobin’s Q coefficient of one assures a theoretically plausible long-run supply adjustment. Similarly, a long-run income elasticity is restricted to one for a plausible long-term demand adjustment, which is in line with the evidence provided by the free estimation results of Dohring (2018) for Italy, Spain and the euro area. Moreover, it is like studies that analyses the housing investment ratio to real GDP as is the case in the euro area country panel study of Rodriguez Palenzuela and Dees, 2016) and in the ECB-BASE model (Angelini et al., 2019) or to wealth (Bulligan et al., 2017). The long-run coefficient of credit remains freely estimated, because credit can be viewed as a positive funding source for investment as well as a negative constraint or housing market risk measure. The restricted (RE) model specification reads as follows. 0 1𝛥 2𝛥 3 4 21<sup>𝛥𝛥𝑞𝑞+ 𝛽𝛽</sup> 22<sup>𝛥𝛥𝑞𝑞+ 𝛽𝛽</sup> 31<sup>𝛥𝛥𝑦𝑦+ 𝛽𝛽</sup> 32<sup>𝛥𝛥𝑦𝑦+</sup> 41 𝑡𝑡 42 𝑡𝑡 0 𝑡𝑡 0 𝑡𝑡 𝑡𝑡0<sup>+ 𝛽𝛽</sup> 4 𝑡𝑡−10 1𝑡𝑡−2 2 𝑡𝑡−1 𝑡𝑡−2 (5) 𝛥𝛥𝑖𝑖 = 𝛼𝛼 + 𝛼𝛼 𝛥𝛥 + 𝛼𝛼 𝛥𝛥 + 𝛼𝛼 𝛥𝛥𝑤𝑤 + 𝛼𝛼 𝛥𝛥𝑢 𝑡𝑡−1 𝑡𝑡−2 𝑡𝑡−1 𝑡𝑡−1 𝑡𝑡−1 𝑡𝑡−1 𝑖𝑖,𝑡𝑡−1 𝑖𝑖,𝑡𝑡−2 𝑡𝑡 𝛽𝛽 𝛥𝛥𝑐𝑐 + 𝛽𝛽 𝛥𝛥𝑐𝑐 −𝛾𝛾 ∙1 ∙𝑞𝑞 −𝛾𝛾 ∙1 ∙𝑦𝑦 −𝛾𝛾 𝛾𝛾 𝑐𝑐 + 𝛾𝛾 𝑖𝑖 + 𝛿𝛿 𝛥𝛥𝑖𝑖 + 𝛿𝛿 𝛥𝛥𝑖𝑖 + 𝜇𝜇 

### _3.3 Selection of equations_ 

As reported in section 5, the practical implementation of the specifications defined in the last subsection implies estimating literally thousands of VECMs for each country. Therefore, to exploit the potential of model averaging we also need to design a subset selection procedure, so getting rid of most of these specifications and focusing on only a subset of them to produce an average forecast of housing investment (see e.g., Lichtendahl and Winkler, 2020). However, while there is no commonly agreed set of criteria identified in the literature, the most common technique of subset selection is to focus on the most accurate models in terms of forecasting performance (Wang et al., 2022). In this study we apply a four-step selection process in which we first evaluate whether our candidate equations satisfy several in-sample statistical properties to discard potentially misspecified equations. Finally, we assess the pseudo out-of-sample forecast performance of the remaining equations to focus only on the most accurate set of specifications.<sup>3</sup> A more detailed explanation of our four-step (S1-S4) selection process follows: 

**S1.** The first selection criterion is a co-integration test. The starting point is a search among all possible combinations of long-run relationships with up to three long-run determinants, which in total deliver 119 

> 3 The selection criteria employed in this paper is along the lines of the subset selection procedure used by de Bondt et al. (2020 and 2021) for private consumption. 

ECB Working Paper Series No 2807 

9 

combinations without any short-run determinant. The error correction coefficient (γ0) should be statistically significant with a t-statistic of at least 3 (5% augmented Dickey-Fuller critical value) to ensure that housing investment is co-integrated with its long-run determinants. 

**S2.** The second selection criterion focuses on residual autocorrelation as a sign of model misspecification using the P-values of the Ljung-Box Q-statistics. The probabilities should be larger than 0.05 for lags one to four. This criterion thus tests for significant departures over the first four lags. Given the short sample, testing for more lags appears problematic as the test loses its predictive power against low degrees of freedom. 

**S3.** The third selection tests for positive and significant long-run coefficients with respect to Tobin’s Q as well as income. It hence aims at avoiding economically implausible negative long-run effects. The 5% significance level using the F-statistic is applied. This criterion is only relevant for the unrestricted specifications. We do not impose any restrictions on the estimated coefficients for credit variables. 

**S4.** The fourth and final selection criterion examines recursively the pseudo out-of-sample forecast performance. The root mean squared out-of-sample forecast error (RMSE) on average over one, two, up to eight quarters ahead should be at least 10% lower as those from a naïve AR(1) benchmark model. Each quarter of the forecast horizon of up to two years ahead is thus viewed as equally important. Then, the VECM equations are sorted according to their average RMSE from the lowest to the highest. Finally, among the specifications that remain available, we focus only on the top 50 ones with the lowest relative RMSE. We average the 50 forecasts they produce, thus obtaining our housing investment forecast. 

### _3.4 Benchmarks_ 

The forecasting ability of our approach is assessed by comparing the pseudo out-of-sample outcomes we produce to the results of a naïve benchmark and six ambitious benchmark models. This comparison should be sufficient to demonstrate the forecasting power of our model averaging tool. 

First, the naïve benchmark model we use is an autoregressive (AR) model with one lag. An economic explanation for this AR benchmark is that investment growth might depend on investment growth of the previous period. As explained in the last subsection, we use this as a benchmark to measure relative forecasting performance in our subset selection procedure. 

The second benchmark model uses building permits. Building permits are expected to be closely related to national accounts data on housing investment, particularly to the housing construction component (the other main component is housing renovation) as new construction can only start after a building permit has been granted. For Canada Demers (2005) finds that the best out-of-sample model is a leading indicator model using building permits and housing starts. Building permits (BP) are the first clear signal regarding future housing investment, so that after being issued it usually takes a couple of quarters for building permits to translate into housing starts followed by housing investment. The BP benchmark model reads as follows. = µ0 + µ1 𝛥 4) (6) where bp(ma4) denotes the four-quarter moving average of building permits excluding residences. 𝛥𝛥𝑖𝑖𝑡𝑡 𝛥𝛥(𝛥 𝑡𝑡−1 + 𝜀𝜀𝑡𝑡 

ECB Working Paper Series No 2807 

10 

The next two benchmark models are Bayesian Vector Autoregressive models with four (BVAR4) or seven variables (BVAR7). The BVAR4 consists of Tobin’s Q (measured as house price relative to the housing investment deflator), labour income, loans for house purchase (the three key drivers of housing investment), and the composite mortgage rate. All variables are in first differences and two lags are considered. The BVAR7 consists of the same four variables as the BVAR4 plus three additional variables from the short-term group: employment (macroeconomic category), number of private households (demographics) and stock market volatility (uncertainty). 

To further challenge our model averaging tool, we borrow from the big data literature dimensionality reduction and regularization techniques and allow them to exploit the full set of variables we use in our specifications. To that purpose, we first employ principal component analysis to extract an optimal number of factors from our full dataset (27 variables) and estimate a Bayesian FAVAR model. The number of factors is determined using the test of Bai and Ng (2002) and indicates for all countries and the euro area seven factors<sup>4</sup> . Both the BVARs and the BFAVARs are estimated using standard Minnesota priors. 

Finally, we use two regularization techniques based on statistical machine learning: the Least Absolute Shrinkage and Selection Operator (LASSO) and Ridge regressions. LASSO and Ridge regressions are penalized regression methods that work by shrinking the magnitudes of the coefficients in the model. In both cases, we include all 27 model variables in first differences<sup>5</sup> . 

## **4. Data** 

The sample period starts in the first quarter of 1999, which has the advantage that true euro area data as well as sector account data are used. The latter provide consistent harmonised quarterly data on household balance sheet stock and flows, such as income and wealth components. The sample period ends in 2020Q3. All variables, unless stated otherwise, are retrieved from the European Central Bank’s projection database, which, in turn, extract the data from the ECB Statistical Data Warehouse with Eurostat as main underlying data source. Included are also the number of households from the Eurostat database and housing stock data, which evolve closely in line with quarterly seasonally adjusted data for housing wealth. All explanatory variables (except ratios) have been deflated using the private consumption deflator and if needed seasonally adjusted using X12-Arima and transformed into log levels and differences according to unit root tests. Table A1 in the Appendix provides an overview of all the variables considered. 

For the reported in-sample estimates the sample period ends in 2019Q4 to ensure that the results are not affected by the COVID-19 pandemic. The first three quarters of 2020 are used to evaluate the out-of- 

> 4 Initial visual inspection of the scree plot of the ordered eigenvalues suggests choosing between 3 to 7 factors depending on the country. Therefore, we perform the Bai, Ng (2002) test setting the maximum number of factors equal to 7 for all countries. As a robustness check, we perform the same pseudo out-of-sample forecasting exercises reported in section 5 using from three to seven factors in our Bayesian FAVAR benchmark model for all countries, not finding significant performance difference. Notably, our model averaging forecasts of housing investment consistently beat all FAVARs, independently on the number of factors included. 

> 5 Both the LASSO and Ridge regressions are estimated using a time series cross-validation with an expanding window. 

ECB Working Paper Series No 2807 

11 

sample performance of our selected top 50 equations during the COVID-19 pandemic. Regarding the outof-sample period as used for the fourth selection criterion, equations are estimated recursively with enddates ranging from 2012Q4 to 2017Q4 to generate conditional forecasts for quarterly consumption growth for up to 8 quarters ahead, i.e., over the pseudo out-of-sample period spanning 2013Q1 to 2019Q4. 

Fig. 1 plots housing investment together with building permits in log level real terms. The former is the relevant series for the cointegration relation. Building permits are also plotted because they are used for a fundamental based benchmark model. The figure shows country heterogeneity in housing investment. During the 2002-2003 recession in Germany and France, housing investment declined in Germany, whereas it increased in France. Before the outbreak of the global financial crisis housing investment clearly peaked in all euro area countries, except in Germany. During the corona recession housing investment in Germany and the Netherlands was hardly affected, whereas it plummeted in the other euro area countries. 



**Fig. 1.** Housing investment and building permits in the five largest euro area countries and the euro area, in log real terms. Shaded areas are recessions as dated by the Economic Cycle Research Institute (ECRI) for Germany, France, Italy, and Spain and by the Centre for Economic Policy Research (CEPR) for the euro area. For the Netherlands, recessions correspond to technical recessions, i.e., periods with at least two consecutive quarters of quarterly contractions in real GDP. 

ECB Working Paper Series No 2807 

12 

It is important to note that nonnormality and nonlinearity in the data generating process of housing investment should in the ideal case be accounted for by the housing investment determinants considered. Jarque-Bera test statistics which measures the difference of the skewness and kurtosis of the series with those from the normal distribution show that real housing investment is over our sample period normally distributed in Germany, France, Italy, and the euro area, but not in Spain at the 10% significance level and the Netherlands at the 1% significance level.<sup>6</sup> In both countries the difference between the peak in housing investment before the global financial crisis and the bottom at the end of the euro government debt crisis is large (about 0.7) compared to the other countries (see Fig. 1), reflecting a boom and bust in housing investment. This boom-and-bust cycle can to a large extent be explained by the long-run investment determinants considered. The left panel of Fig. 2 plots for the Netherlands housing investment and the three long-run model determinants. It shows that the boom in the Dutch housing investment has gone hand in hand with a rising Tobin’s Q due to the higher house prices relative to the building costs, while it has been also supported by increasing mortgage lending relative to disposable income until de Great Recession. Mirroring this, the housing affordability index has gradually declined during the boom and improved thereafter. The right panel of Fig. 2 illustrates the potential value added of restricting the long-run coefficient of Tobin’s Q and income to one as in our restricted model version. For housing boom-and-bust cases putting some economically plausible structure to the model could be of particular use. The restricted series for Tobin’s Q and housing affordability behave much more in tandem compared to the unrestricted plot in the left panel. 



**Fig. 2.** Housing investment, Tobin’s Q, housing affordability index and loans for house purchase to disposable income in the Netherlands (left-hand panel). Housing investment minus 1.0*Tobin’s Q and housing investment minus 1.0*housing affordability index in the Netherlands (right-hand panel). Housing investment and loans in log real terms. Tobin’s Q is measured by the house price relative to the residential investment deflator. Housing affordability index is calculated as outlined in footnote 2. Sample period is 1999Q1-2020Q3. Normalised scale. 

6 The significance levels of the Jarque-Bera statistics are as follows: DE 16%; FR 39%; IT 24%; Spain 6%; Netherlands 0%; EA 17%. We thank an anonymous referee for raising this issue. It illustrates the challenge for modellers and forecasters of housing investment. This modelling challenge relates to an extensive literature on identifying booms and busts, typically applied to house prices. For a euro area application, see Gerdesmeier et al. (2015) and for a euro area country evidence, see Chatzitsolis and Vlamis (2014). Nonlinearity can also be an issue and is to a large extent captured by our second selection criterion on the Q-statistic as a general model misspecification test. For example, McLeod and Li (1983) propose to use the Q-statistic from the squared residuals of an ARMA model fit as nonlinearity test. 

ECB Working Paper Series No 2807 

13 

Besides the wide range of model variables considered for which projections are available for conditional forecasting other factors might also help in explaining country heterogeneity. For example, structural variables are not part of the model but could help in explaining differences in the empirical results across countries. Country differences in the field of housing tenure and public policy, housing finance systems and business environment as reported in Table 2 can be marked. The owner-occupied share of houses is comparatively low in Germany and high in Italy and Spain. The rent subsidized with a share of almost 20% is high in France. Rent subsidies, beyond equality considerations, might contribute to give incentives to renting, and thus creates a disincentive for buying. The latter could result in smoothing the housing investment cycle and helps explain the comparatively low standard deviation of housing investment in France. Property taxes are low in Germany and the Netherlands and high in France. The vacancy rate has been low in the Netherlands and high in Italy and Spain. Almost half of the owner in the Netherlands has a mortgage, a high share compared to the other countries where it varied between 11% and 26%. The share of adjustable-rate mortgages is with comparatively high in Spain and low in France. Turning to the business environment, the days for obtaining a building permit and the costs involved as well as enforcing contracts is comparatively favourable in Germany, whereas Italy is at the other end of the spectrum. The duration to obtain a building permit varied between about four months in Germany and seven months in Italy and to enforce a contract around one year in Germany and more than three years in Italy. 

### **Table 2** <u>Structural differences across countries.</u> 

||**DE**|**FR**|**IT**|**ES**|**NL**|
|---|---|---|---|---|---|
|**Housing tenure and public policy**||||||
|Owner-occupied accommodation (%), 1999-2019|44.0|57.0|72.7|79.8|55.3|
|Rented accommodation (%), 1999-2019|56.0|43.0|18.1|13.9|43.5|
|Rent subsidized (%), 2020|6.6|18.5|1.9|3.3|-|
|Tax on immovable property (% of total tax revenues), 2020|1.1|5.2|3.0|3.1|2.5|
|Vacancy rate (%), 1999-2019|8.0|6.9|19.3|15.2|3.6|
|**Housing finance systems**||||||
|Owner with mortgage (%), 2020|18.2|23.1|10.8|26.4|48.8|
|Share of adjustable-rate mortgages (%), 2019-2020|11.0|2.0|24.0|35.5|17.0|
|**Business environment**||||||
|Building Permits, 2006 - 2020||||||
|Days|128|189|213|172|198|
|Cost (% of building)|1.3|3.4|3.7|5.0|3.9|
|Enforcing contracts, 2004 - 2020||||||
|Days|429|447|1211|513|514|
|Cost (% of claim)|14.4|17.4|28.5|17.5|24.1|



_Note_ : Source is ECB Statistical Data Warehouse, World Bank (2021), Muellbauer (2022) and OECD (2022). 

ECB Working Paper Series No 2807 

14 

## **5. Empirical results** 

This section describes the empirical results from the applied model averaging approach. It reports the number of selected equations following the selection criteria. Focusing on the top 50 selected equations, it provides details about the in-sample estimates and fit as well as the out-of-sample performance, including during the COVID-19 pandemic. 

### _5.1 Selected equations_ 

The four selection criteria result in a varying number of selected equations across countries and the restrictiveness of the criteria differs also across countries and between unrestricted and restricted specifications. Table 3 summarises the number of selected equations after each selection criterion for the unrestricted (upper panel) and restricted specifications (lower panel). 

After the first selection criterion on cointegration, the number of selected cointegration relations vary between 1 selected cointegration relation (1% of the total considered) for the Netherlands based on the unrestricted model specifications and 53 selected long-run relations for the euro area using the restricted model specifications (45% of the total). Consequently, the number of estimated equations including the short-run variables vary between 376 for the former and almost 62 thousand for the latter. Only a minority of the equations, often around 10% to 20%, fulfil the cointegration criterion, suggesting that the comparatively strong short-term swings in housing investment prevent finding stable long-run relations. Another explanation is the nonnormal and boom-bust behaviour of housing investment in the Netherlands, resulting in a low number of equations that fulfil the first cointegration selection criterion. Often the number of selected equations after the cointegration selection criterion is higher for the restricted model version than for the unrestricted specifications. All selected equations in this step are jointly significant at the 5% level. These results support our choice of also pursuing an analysis based on restricted coefficients. 

The selection criterion on autocorrelation test is not binding at all for Germany and Italy, slightly for Spain and to some extent for France. Autocorrelation is particularly an issue for the euro area, with 60% to 74% of the equations remaining, and the Netherlands, where only 18% to 14% of the equations remain. The individual significance test for Tobin’s Q and income for the unrestricted model specifications is restrictive in all cases and most markedly in Spain where 23% of the equations are still selected. The out-of-sample selection criterion is not restrictive for the Netherlands, whereas at the other end of the spectrum is Italy where the number of selected equations declines by 55 percentage points for the unrestricted model and by 75 percentage points for the restricted model. 

Insert Table 3 (landscape) here 

ECB Working Paper Series No 2807 

15 

### _5.2 Estimated coefficients_ 

A closer look at the average estimates as well as the 15th and 85th percentiles of the top 50 selected equations reveals one main conclusion of striking country differences in the determinants of housing investment across euro area countries (see Table 4, for more details see Table A3). 

The three long-run determinants considered are not always selected for the unrestricted model specifications. Tobin’s Q is not selected in the long run for Germany, France and Italy, income not for France and Spain, and credit not for the Netherlands and the euro area. The average coefficients for Tobin’s Q and income are estimated to be larger than one in all cases except for income in the Netherlands. In the latter case the income measure selected is the housing affordability index which depends not only on income but also on house prices and the mortgage rate. Credit is estimated to be (slightly) positive in France and Italy, and negative in Germany and Spain. Looking at the estimates for the restricted specification, the country heterogeneity in the estimates remains. Tobin’s Q still doesn’t play a role in France and Italy and the credit sign variation is divided. For Spain in all cases the income measure selected is the housing affordability index (for the detailed estimation results, see in the Appendix Table A3). The cost of credit thus matters in Spain in the long run via the housing affordability index. Noteworthy is that the sum of unrestricted and restricted coefficients with respect to Tobin’s Q and income is similar for Germany, Spain, and the Netherlands and that the credit coefficient is hardly affected for France but strongly for Spain. 

The short-run estimates show also striking cross-country differences. Again, no role for Tobin’s Q in France and Italy, whereas it is an important short-run driver in Spain and the Netherlands. Short-run income elasticities are small and only positive in the euro area for the unrestricted model. Short-run credit effects are positive in all countries except for the Netherlands. The range of the estimated coefficients of Tobin’s Q, income, and credit, as reported by the 15%-85% percentiles, are generally sufficiently wide apart from France. In France the coefficient ranges are narrow and the differences between the unrestricted and restricted versions are often identical at the second decimal and only different at the third decimal. However, in practice (see Section 5.4 for a pre-COVID application over the period 2018Q4-2019Q4) the forecast range is even for France meaningfully wide, keeping in mind the low volatility of French housing investment. This is due to the impact of the other short-run coefficients. For the four short-term groups there is for all countries and the euro area quite some variation which variables are included (see Table A.4), whereas the variation within the three long- and short-term groups is rather low in France and high in the euro area. 

The finding of marked cross-country differences in long-run housing investment drivers is robust not only for the top50 equations, but also when considering the selected equations after the first selection criterion on cointegration (see Table A2). An interesting finding is that the housing affordability index is the most selected income measure in all countries and the euro area for the restricted specification. It contrasts with other studies that have not considered an affordability index. 

ECB Working Paper Series No 2807 

16 

**Table 4** 

Estimated Tobin’s Q, income, and credit coefficients. 

||||||**Long-ru**<br>|**n coeff**<br>|**icients**<br>|<br>||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||**Germ**|**any**|**Fra**|**nce**|**Ita**|**ly**|**Spa**|**in**|**Nethe**|**rlands**|**Euro**|**area**|
|||**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|
||**15%**|||||||1,74||1,35||1,10||
|**Tobin's Q**|**Average**|-|1|-|-|-|-|1,94|1|1,43|1|2,11|1|
||**85%**|||||||2,04||1,45||2,19||
||**15%**|1,65||||3,92||||0,42||1,90||
|**Income**|**Average**|2,35|1|-|1|4,04|1|-|1|0,47|1|1,93|1|
||**85%**|2,41||||4,16||||0,55||2,02||
||**15%**|-0,65|-0,99|0,20|0,20|-0,07|0,31|-1,07|||0,13|-0,34|-0,14|
|**Credit**|**Average**|-0,64|-0,96|0,20|0,20|0,43|0,43|-1,01|-|-|0,27|0,25|-0,10|
||**85%**|-0,63|-0,23|0,21|0,21|1,00|1,00|-0,89|||0,36|0,27|-0,09|
|||||**S**|**hort-r**|**un coef**|**ficients**|<br>||||||
||**15%**||0,00|||||0,22|0,16|1,06|0,93|-0,14|0,34|
|**Tobin's Q**|**Average**|-|0,05|-|-|-|-|0,27|0,21|1,10|1,06|-0,10|0,36|
||**85%**||0,18|||||0,31|0,24|1,23|1,21|0,72|0,37|
||**15%**|-0,13|-0,29||-0,10|-0,19|-0,14||-0,06|-0,02|-0,27|0,11|-0,06|
|**Income**|**Average**|-0,09|-0,26|-|-0,10|-0,18|-0,12|-|-0,05|-0,01|-0,25|0,12|-0,04|
||**85%**|0,39|-0,16||-0,10|-0,16|-0,10||-0,03|0,02|0,01|0,19|-0,02|
||**15%**|0,66|0,50|0,24|0,24|0,25|0,33|0,10|||-0,41|0,22|-0,05|
|**Credit**|**Average**|0,70|0,66|0,26|0,26|0,39|0,40|0,15|-|-|-0,12|0,35|0,01|
||**85%**|0,76|0,76|0,28|0,28|0,45|0,44|0,20|||-0,01|0,42|0,12|



_Note_ : average of the top 50 selected equations estimated up to 2019Q4 and the average coefficient of all series within a group. UN refers to unrestricted model specification and RE to restricted specification. 

The average estimated error correction coefficients vary between close to -0.05 in Italy, Spain, and France and around -0.20 in Germany and the Netherlands (both cases unrestricted model), suggesting marked difference in the speed of adjustment to the cointegration relation (see Table 5). Consequently, the half-life of disequilibrium is estimated to vary on average between three quarters (within one year) and 14 quarters (three and a half years). Country differences in the speed of adjustment broadly matches country differences in homeownership shares as well as property taxes, which are comparatively low in Germany and the Netherlands. Again, the range is small in France, indicating hardly any variation across the 50 selected equations in the estimated adjustment speed. The estimated adjustment speed is faster for the unrestricted model specifications than for the restricted ones for Germany, Spain, the Netherlands, and the euro area. The adjustment speed is broadly unchanged between the two model specifications for France and Italy. The estimated error correction coefficients are for all countries apart from Italy broadly in with the range of error-correction coefficients reported in Table 1. 

Changes in the adjustment speed are investigated further by splitting the sample into two. The first subsample starts in 1999Q1 and ends in 2009Q4. The second sub-sample starts in 2010Q1 and ends in 2019Q4. Despite the low number of observations for the two sub-samples and thus imprecise estimates the range of the estimated error correction coefficients often partially overlaps the full-sample range. 

ECB Working Paper Series No 2807 

17 

Considering the large estimated sub-sample standard errors, the adjustment speed is overwhelmingly not statistically different from the full-sample estimate. Most marked difference is a much faster estimated adjustment speed of the unrestricted model for the second half of the sample in Germany, Spain, and the euro area. Noteworthy is also the comparatively stable estimated adjustment speed of the restricted model for the housing boom-bust countries Spain and the Netherlands.  More in general, the restricted model estimates of the error correction coefficient are found to be more stable than those for the unrestricted model, illustrating the value added of imposing long-run restrictions to the model. The exceptions are France and Italy, because the unrestricted and unrestricted models hardly differ. 

**Table 5** 

<u>Estimated error correction coefficient.</u> 

|**Country**|||**Unrestrict**|**ed**||**Restricted**||
|---|---|---|---|---|---|---|---|
|||**1999-**<br>**2019**|**1999-**<br>**2009**|**2010-**<br>**2019**|**1999-**<br>**2019**|**1999-**<br>**2009**|**2010-**<br>**2019**|
||15%|-0.21|-0.15|-0.65|-0.17|-0.13|-0.16|
|**Germany**|**Average**|**-0.19**|**-0.14**|**-0.60**|**-0.15**|**-0.11**|**-0.10**|
||85%|-0.15|-0.12|-0.56|-0.11|-0.07|-0.05|
||15%|-0.08|-0.14|-0.07|-0.08|-0.15|-0.07|
|**France**|**Average**|**-0.07**|**-0.12**|**-0.06**|**-0.07**|**-0.12**|**-0.06**|
||85%|-0.07|-0.09|-0.05|-0.07|-0.09|-0.05|
||15%|-0.07|-0.03|-0.16|-0.06|-0.02|-0.13|
|**Italy**|**Average**|**-0.04**|**-0.01**|**-0.11**|**-0.04**|**0.01**|**-0.10**|
||85%|-0.02|0.02|-0.07|-0.02|0.03|-0.07|
||15%|-0.07|-0.09|-0.28|-0.05|-0.07|-0.10|
|**Spain**|**Average**|**-0.06**|**-0.06**|**-0.23**|**-0.05**|**-0.07**|**-0.07**|
||85%|-0.05|-0.04|-0.20|-0.04|-0.06|-0.03|
||15%|-0.23|-0.18|-0.12|-0.18|-0.21|-0.21|
|**Netherlands**|**Average**|**-0.20**|**-0.10**|**-0.06**|**-0.16**|**-0.16**|**-0.18**|
||85%|-0.17|-0.15|-0.08|-0.15|-0.13|-0.14|
||15%|-0.29|-0.34|-0.77|-0.13|-0.16|-0.21|
|**Euro area**|**Average**|**-0.14**|**-0.19**|**-0.41**|**-0.07**|**-0.08**|**-0.18**|
||85%|-0.05|-0.07|-0.03|-0.05|-0.04|-0.13|



_Note_ : average and 15%, respectively, 85% percentiles of the top 50 selected equations for full sample and two sub-samples. 

A couple of observations emerge from the estimates of the short-run variables, which are all included in terms of quarterly changes (see Table A4 in the Appendix for the detailed results). Mortgages interest rates significantly negatively affect housing investment growth in France and Italy, the two countries where credit plays a key role in the long run. In the other large euro area countries and the euro area the estimated coefficients for mortgages interest rates are not statistically different from zero. An explanation is that the mortgage rate plays an important role in the calculation of the housing affordability index and that its additional role is in those cases where the affordability index is included (Spain, Netherlands, euro area) rather limited. The macroeconomic group plays a statistically significant role. Real GDP growth is found to be a significant short-run determinant for all countries and real private consumption growth for Germany 

ECB Working Paper Series No 2807 

18 

and the Netherlands. In almost all cases the estimated coefficients are larger than 1. This proportionately larger rise in investment is evidence in support of an accelerator effect. Foreign demand is significant for the euro area. Total employment is found to be a significant determinant in Germany, Spain, and the euro area. The unemployment rate is also found to be a significant driver of housing investment, as its coefficient is significant in Germany, France, and Spain. In contrast, demographics and wealth hardly play a significant role. The number of households only significantly matters in Germany and population is never found to be significant. The housing stock is only found to be significant in Italy and financial assets in the Netherlands. Turning to uncertainty, a similar picture emerges. The only significant case is found for stock market volatility in France. This finding suggests that the lack of uncertainty measure in other studies is no reason for being concerned. In sum, the macro environment, including the unemployment rate does particularly play a role for housing investment in the short run. The macro environment is found to capture especially accelerator effects which are often important in explaining investment. The unemployment rate not only captures the labour market situation but also proxies consumer confidence. 

Turning to the overall in-sample fit, it becomes clear that the selected top 50 equations capture well underlying housing investment growth but not necessarily its short-run volatility. Fig. 3 shows for the period 2013-2019 that actual housing investment fluctuates far more than the growth derived from the selected equations, irrespective whether it is the unrestricted or restricted specification. Actual spikes in housing investment growth are substantial and driven by factors, such as weather conditions, strikes, tax or regulatory changes, which are not part of our set of model variables. Consequently, our model averaging tools does not capture well short-run swings in the quarterly change in housing investment. Often a high or low change in one quarter rebounds in the next quarter. The figure also reveals growth volatility differences across countries, as captured by different y-scales. The standard deviation of the quarterly change in housing investment times 100 is over 1999 to 2019 comparatively low in France (1.3) and the euro area 1.5, high in Spain (3.3) and the Netherlands (4.2) and in between in Germany and Italy (2.3). The low volatility in France can be explained by the high share of subsidised rents, implying comparatively low incentive for buying a home and thus for housing investment expenditure. The high volatility in Spain and the Netherlands reflects the housing boom and bust over the sample. 

ECB Working Paper Series No 2807 

19 



**Fig. 3.** In-sample fit. Actual quarterly changes in housing investment and median, 15% and 85% percentiles of the top 50 selected equations for unrestricted as well as restricted model specifications. 

### _5.3 Out-of-sample forecast performance_ 

Table 6 reports the RMSE of the top 50 selected equations of the restricted model specification relative to those from the unrestricted model version, all seven benchmarks as well as the top1 selected equations from the unrestricted (UN1) and restricted version (RE1). The pseudo out-of-sample forecast performance of our model averaging tool is promising, most striking is that in all cases the selected top 50 restricted equations outperform all benchmark models, with a forecast gain varying slightly below 10% for Ridge regression for Spain and building permit benchmark for Italy and about 50% for BVAR4 and BVAR7 for the euro area, BVAR7 for France, and Lasso for Spain. This is a remarkable outcome, given the battery of potential powerful benchmarks we evaluate. The building permit-based model overwhelmingly performed 

ECB Working Paper Series No 2807 

20 

best among the benchmark models. Only in the two boom-bust countries Spain and the Netherlands Ridge and LASSO regressions performed slightly better, respectively. 

Notably, the selected restricted model specifications on average consistently have performed as well (Italy and the euro area) or outperformed (Germany, France, Spain and the Netherlands) the unrestricted model specification (UN50). The forecast gain between the restricted and unrestricted model version are most markedly visible for the two boom-bust countries Spain and the Netherlands, stressing the value added of imposing long-run restrictions. In addition, forecast averaging proves also in our application a powerful forecasting tool. Averaging the forecasts from the top 50 selected equations outperforms the best performing equation from our selected top 50 equations for Germany, Netherlands and the euro area and performs similarly for France, Italy, and Spain. 

**Table 6** 

Out-of-sample performance over all eight forecast horizons. RMSE of the averaged forecasts across the top 50 restricted equations relative to RMSE of benchmarks, top 1 selected equations and top 50 <u>unrestricted equations.</u> 

||**AR**|**BP**|**BVAR4**|**BVAR7**|**BFAVAR**|**LASSO**|**Ridge**|**UN1**|**RE1**|**UN50**|
|---|---|---|---|---|---|---|---|---|---|---|
|Germany|0.70|0.72|0.62|0.63|0.64|0.59|0.72|0.93|0.98|0.92|
|France|0.67|0.80|0.63|0.49|0.60|0.62|0.63|1.02|1.02|0.98|
|Italy|0.77|0.91|0.65|0.65|0.63|0.60|0.56|1.01|1.00|1.01|
|Spain|0.71|0.85|0.64|0.70|0.70|0.51|0.93|0.88|1.00|0.85|
|Netherlands|0.73|0.80|0.74|0.73|0.76|0.83|0.79|0.90|0.97|0.88|
|Euro area|0.54|0.86|0.48|0.51|0.57|0.57|0.68|0.91|0.98|1.00|



Looking at the pseudo out-of-sample forecast performance across forecast horizon, the value added of the applied forecast averaging approach is confirmed, especially for the restricted model and for forecast horizons longer ahead. Given the superior performance among benchmark models of the building permit benchmark, Table 7 compares the performance of our forecast averaging tool relative to the building permit benchmark. For at least five out of the eight forecast horizons the forecast averaging tool outperforms the building permit benchmark (see Table 7).  This outperformance is most marked significant across horizons, especially significant at longer forecast horizons for France, the Netherlands, and the euro area (RRMSE column). The outperformance of our forecast averaging is only once significant for Spain and not at all for Italy. This notwithstanding, the forecast gain amounts in these two countries up to a sizeable 19%, respectively, 26%. In the other countries the forecast gain is up to 39%. The only cases where the building permit benchmark outperforms our unrestricted and unrestricted models are for seven and eight quarters ahead for Italy. 

The restricted model outperforms the unrestricted model for Germany and the Netherlands consistently across all forecast horizons and for Spain and the euro area for the longer ahead horizons.  The out-ofsample forecast performance hardly differ between the restricted and unrestricted models for France and Italy. Another interesting finding is that the RMSE declines over the forecast horizon in all countries, apart from Italy and the Netherlands. This finding suggests an important steering role of the cointegration relation, 

ECB Working Paper Series No 2807 

21 

irrespective whether it is the unrestricted or restricted long-run relation. It can also be viewed that the selected determinants have more difficulties capturing short-run swings, which might be more determined by unpredictable surprises such as weather conditions. 

The RMSE in absolute terms vary a lot across countries. They are below 1 for France and the euro area, around 1 for Germany and Italy and much higher in Spain (between 1.5 and 3.5) and the Netherlands (close to 5).  The latter two countries faced a housing boom-bust cycle around the global financial crisis. The absolute RMSE are also scaled by the standard deviation of household investment changes over the outof-sample period to improve the country comparison. The RMSE standard deviation ratio (RSR) show comparatively outstanding performance of a RSR of about 0.5 for seven and eight quarters ahead for Germany, France, Spain (restricted specification) and the euro area, whereas the performance is poor with a RSR of about 1.0 across the board for the Netherlands (the country with nonnormal housing investment) and at short forecast horizons for Germany, France, Spain, and the euro area. 

### Insert Table 7 (landscape) here 

### _5.4 COVID-19 pandemic_ 

The out-of-sample forecast performance of the model averaging tool is further evaluated by applying it to the final eight quarters of our sample, which includes the first three quarters of 2020 which had been affected by the COVID-19 pandemic. Fig. 4 is split into two parts due to the large size of the pandemic shock. It plots the outcomes for the restricted specification as the previous section shows that it performs at least as well as the unrestricted specification. Looking at the first five quarters up to 2019Q4, the modelbased forecasts from the top 50 selected equations are broadly in line with actual housing investment in Germany, France till 2019Q1, Netherlands (note that in 2019Q4 many building projects were put on hold due to CO-2 regulation discussion), and the euro area (with some deviation in 2019Q1). They were consistently too high in Spain and too low in Italy. The top 50 selected equations often outperform the benchmark models. The exceptions are both benchmark models for Italy, the AR benchmark for France and Spain and the building permits benchmark for the euro area. 

Turning to the first three quarters of 2020, the most striking observation is that actual housing investment in 2020Q3 is close to the model averaging outcome in 2020Q3 in all countries except Spain. It is within the model range in Germany, Italy, and the euro area. For the latter even for all three quarters. In France and the Netherlands, actual housing investment is in 2020Q3 close to the model range. The unrestricted model specification appears to deal even better with large shocks (see Fig. A1 in the Appendix). In 2020Q3 housing investment is within the model range in Germany, Italy, Netherlands and the euro area and close to the lower range for France and Spain. These findings illustrate the benefits of the model averaging tool also in case of sizeable, unexpected developments and particularly for the longer term. However, in the near term large forecast errors can occur. The COVID-19 pandemic also illustrates country heterogeneity. Housing investment has been comparatively resilient to the major shocks originating from COVID-19 in Germany and the Netherlands with initially comparatively relaxed pandemic measures (e.g. no “stay home 

ECB Working Paper Series No 2807 

22 

order” during 2020Q1-Q3, source: <u>https://www.ecdc.europa.eu/en/publications-data/download-dataresponse-measures-covid-19), whereas France, Italy, and Spain had a “stay home order” and faced</u> double-digit declines in housing investment due to COVID-19. Historical evidence suggests that strong movements following a pandemic can be expected to be transitory (Francke and Korevaar, 2021). 



**Fig. 4.** Out-of-sample forecasts for 2018Q4 – 2020Q3 based on top 50 selected restricted model equations estimated over 1999Q1 – 2018Q3. Housing investment level in 2018Q3 = 100. 

## **6. Conclusions** 

Housing investment is widely monitored by forecasters, analysts, policymakers, construction builders, and investors due to its central importance for the economy. Yet, despite its importance for the economy and economic policy, the literature neither provides a clear-cut commonly agreed theoretical framework to model and forecast housing investment nor is there an agreement on its empirical determinants. In a similar vein, housing investment and the whole housing blocks of central bank macro models seem to be subject to relevant modelling challenges (Muellbauer, 2022). Against this background, the aim of this study is to provide forecasters and modellers with a tool to assess the risks to their forecasts of housing investment 

ECB Working Paper Series No 2807 

23 

and to improve their econometric models. To account for substantial modelling uncertainty, we propose a model averaging approach to forecast housing investment. To that extent, we estimate many VECMs using a wide set of short and long-run determinants and select the most promising specifications based on a set of in-sample and pseudo out-of-sample criteria. 

Our study provides forecasters guidance about modelling housing investment in four ways. Firstly, a pseudo-out-of-sample forecast exercise shows that – across euro area countries and for the euro area - our model averaging approach significantly beats a battery of distinguished benchmark models, including BVARs using a small dataset, and FAVARs as well as machine learning techniques such as LASSO and Ridge regressions, exploiting our full dataset of 27 variables. Secondly, we have established the most promising long-run determinants of housing investment. Loans to house purchase feature prominently as key long-run determinant for housing investment in the euro area and across most countries. This variable is omitted in most housing investment equations of semi-structural macro models at euro area central banks. There is more cross-country heterogeneity in terms of income and Tobin´s Q specifications as longrun determinants. Yet, it might pay off for forecasters to include a housing affordability index into their models. Thirdly, there is substantial cross-country diversity as concerns the significance of mortgage interest rates as a short-run determinant, which is found to be significantly negative in France and Italy, and insignificant in the other countries, where they could still play role via the housing affordability index. Marcoeconomic variables such as real GDP and private consumption help explain housing investment across countries, while measures of demographic and uncertainty variables are hardly found to be significant shortrun determinants. Fourthly, our results suggest that the restriction of Tobin´s Q and income to one can substantially help in housing investment equations; a substantially larger number of restricted equations passed the in-sample and out-of-sample selection criteria, they beat the benchmark models much more often than the unrestricted specifications, and the top 50 restricted models consistently showed the best overall forecasting performance. This should please forecasters as restricted models also improve the narrative of the housing investment projections. 

The practical policy implications of our findings are several. Firstly, country heterogeneity in the drivers of housing investment makes a strong call for country specific policy measures. The most efficient policy measures to influence housing investment are found to differ across countries. For example, our results underline that Tobin’s Q and income are not necessarily factors influencing housing investment. During a crisis period like the COVID-19 pandemic the type of policy support package across countries can thus make a key difference. Moreover, common policy measures at the European level should be expected to result in different country impacts. It is particularly important to bear these differences in mind as we have seen long-lasting boom and bust cycles in housing markets, which have often ended up in causing economy-wide recessions. Secondly, we find that credit and housing affordability matter for housing investment in the long run. Housing affordability is to the best of our knowledge for the first time considered as a driver of housing investment in euro area countries. For the restricted model – our preferred specification due to its outstanding out-of-sample performance – it is the most selected income measure in all countries and the euro area. Policy measures that support housing affordability are thus expected to encourage housing investment. For investors, affordable housing can deliver attractive returns. For 

ECB Working Paper Series No 2807 

24 

modellers, a housing modelling channel via affordability is often missing (Muellbauer, 2022). Similarly, the reported differences in the vulnerability of housing investment to mortgage interest rates across countries is of interest to monetary policymakers. Thirdly, improvements in forecasting and modelling housing investment might be helpful in mitigating booms and busts in housing investment. Indeed, they could be insightful for regulators and macro prudential policymakers as they could provide guidance for setting the countercyclical capital buffer in banking regulation. European policymakers should consider adding housing investment for their assessment of housing vulnerability, as it is not part of their risk scoreboard (see Table 1 in ESRB, 2022). Fiscal policymakers should also consider contributing to smoothing the housing investment cycle by using housing taxes and subsidies in a countercyclical manner. Similarly, better modelling housing investment might also be useful for investors and construction builders as it might avoid unnecessary losses and bankruptcies. The fourth and final policy implication is that better forecasting and modelling housing investment might be helpful for avoiding possible crowding-out effects with other business investment and between private and public investment, especially in the current global context characterized by a green transition and monetary policy tightening. 

As a final point, the forecast averaging results are presented in the spirit of a promising starting point for future studies and improvements to other models in place for forecasting and modelling housing investment. Despite the proved value added of imposing long-run economic plausible restrictions to deal with boombust cycles in housing investment, possible next steps might be to introduce features dealing with nonnormality and nonlinearity for forecasting housing investment during (long-lasting) episodes of housing bubbles. Another possible avenue is to allow for nonlinear (threshold) effects of credit along the lines of Kohl (2021). 

ECB Working Paper Series No 2807 

25 

## **References** 

- Aastveit, K.A., Anundsen, A.K., Herstad, E.I., 2019. Residential Investment and Recession Predictability. International Journal of Forecasting 35, 1790–1799. 

- Angelini, E., Bokan, N., Christoffel, K., Ciccarelli, M., Zimic, S., 2019. Introducing ECB-BASE: The Blueprint of the New ECB Semi-structural Model for the Euro Area. European Central Bank Working Paper Series No. 2315. 

- Antipa, P., Lecat, R., 2010. The ’Housing Bubble’ and Financial Factors: Insights from a Structural Model of the French and Spanish Residential Markets”. In: de Bandt O., Knetsch T., Peñalosa J., Zollino F. (eds), Housing Markets in Europe. Springer, Berlin, Heidelberg, 161–186. 

- Antipa, P., Schalck, C., 2010. Impact of Fiscal Policy on Residential Investment in France. Banque de France Working Paper No. 270. 

- Arencibia, A.P., Hurtado, S., De Luis, M., Ortega, L.E. 2017. New Version of the Quarterly Model of Banco de España (MTBE). Banco de España Occasional Paper No. 1709. 

Atiya, A.F., 2020. Why Does Forecast Combination Work So Well? International Journal of Forecasting 36 (1), 197–200. 

- Aye, G.C., Miller, S.M., Gupta, R., Balcilar, M., Miller, S.M. 2016. Forecasting US Real Private Residential Fixed Investment Using a Large Number of Predictors. Empirical Economics 51, 1557–1580. 

Bai, J., Ng, S., 2002. Determining the Number of Factors in Approximate Factor Models. Econometrica, 70 (1), 191–221. 

Bates, J. M., Granger, C. W. J., 1969. The Combination of Forecasts. Operational Research Society, 20 (4), 451–468. 

- Berben, R., Kearney, I., Vermeulen, R., 2018. DELFI 2.0, DNB's Macroeconomic Policy Model of the Netherlands. Netherlands Central Bank (DNB) Occasional Studies No. 1605. 

- Bezemer, D., Grydaki, M., Zhang, L., 2016. More mortgages, lower growth? Economic Inquiry, 54 (1), 652– 674. 

Bobeica, E., Hartwig, B., 2021. The COVID-19 Shock and Challenges for Time Series Models. ECB Working Paper Series, May 2021, no 2558. 

Bulligan, G., F. Busetti, F., Caivano, M., Cova, P., Fantino, D., Locarno, A., Rodano, L. 2017. The Bank of Italy Econometric Model: An Update of the Main Equations and Model Elasticities. Banca d’Italia Working Papers No. 1130. 

- Caldera, A., Johanssen, A., 2013. The Price Responsiveness of Housing Supply in OECD Countries. Journal of Housing Economics 22 (3), 231–249. 

- Cavalleri, M. C., Cournède, B., Özsöğüt, E., 2019. How Responsive are Housing Markets in the OECD? National Level Estimates, OECD Economics Department Working Paper 1590, OECD. 

Cerutti, E, Dagher, J., Dell’Ariccia, G., 2017. Housing finance and real-estate booms: A cross-country perspective. Journal of Housing Economics, Volume 38, December 2017, 1-13. 

- Chatzitsolis, N., Vlamis, P., 2014. The Boom and Bust of the Greek Housing Market. Real Estate Issues 39 (1), 9–17. 

- Clyde, M. A., 1999. Bayesian Model Averaging and Model Search Strategies. Bayesian Statistics, 6, 157– 185. 

Demers, F., 2005. Modelling and Forecasting Housing Investment: The case of Canada”. Bank of Canada Working Paper No. 2005-41. 

de Bondt, G., Gieseck, A., Herrero, P., Zekaite, Z., 2021. Euro Area Income and Wealth Effects: Aggregation Issues. Oxford Bulletin of Economics and Statistics 83 (6), 1454–1474. 

- de Bondt, G., Gieseck, A., Zekaite, Z., 2020. Thick Modelling Income and Wealth Effects: A Forecast Application to Euro Area Private Consumption. Empirical Economics 58 (1), 257–286. 

- Diebold, F.X., Mariano, R.S., 1995. Comparing Predictive Accuracy. Journal of Business and Economic Statistics 13 (3), 253–263. 

- Dohring, B., 2018. Cyclical Patterns of Residential Construction, Quarterly Report on the Euro Area, 17 (3), 59–67. 

Dümmler, T., Kienle, S., 2010. User Costs of Housing when Households Face a Credit Constraint: Evidence for Germany. Deutsche Bundesbank Discussion Paper, Series 1: Economic Studies No. 12/2010. 

European Systemic Risk Board, 2022, Vulnerabilities in the Residential Real Estate Sectors of the EEA Countries, February. 

- Francke, M., Korevaar, M., 2021. Housing Markets in a Pandemic: Evidence from Historical Outbreaks. Journal of Urban Economics, 123, 103333. 

ECB Working Paper Series No 2807 

26 

Frayne, C., Szczypińska, A., Vašíček, B., Zeugner, S., 2022. Housing Market Developments in the Euro Area Focus on Housing Affordability. European Commission, Directorate-General for Economic and Financial Affairs, Discussion Paper 171. 

Gattini, L., Ganoulis, I., 2012. House Price Responsiveness of Housing Investments across Major European Economies. European Central Bank Working Paper Series No. 1461. 

- Gerdesmeier, D., Lenarčič, A., Roffia, B., 2015. An Alternative Method for Identifying Booms and Busts in the Euro area Housing Market, Applied economics, 47 (5), 499–518. 

- Harvey, D., Leybourne, S., Newbold, P., (1997). Testing the Equality of Prediction Mean Squared Errors. International Journal of Forecasting 13 (2), 281–291. 

Huang, Y. Lia, Q., Liow, K.H. and Zhou, X., 2020. Is Housing the Business Cycle? A Multiresolution Analysis for OECD countries. Journal of Housing Economics 49 (C), 101692. 

Jud, G.D., Winkler, D.T., 2003. The Q Theory of Housing Investment. Journal of Real Estate Finance and Economics 27 (3), 379–392. 

Kajuth, F., 2020. The German Housing Market Cycle: Answers to FAQs. Deutsche Bundesbank Discussion Paper No. 20/2020. 

Karousos, E., Vlamis, P., 2008. The Greek Construction Sector: An Overview of Recent Developments. Journal of European Real Estate Research 1 (3), 254–266. 

Knetsch, T.A., 2010. Trend and Cycle Features in German Residential Investment before and after Reunification. Deutsche Bundesbank Discussion Paper Series 1, Economic Studies No. 10/2010. 

Kohl, S., 2021. Too Much Mortgage Debt? The Effect of Housing Financialization on Housing Supply and Residential Capital Formation. Socio-Economic Review, 19 (2), 413–440. 

Kohlscheen, E., Mehrotra, A., Mihaljek, D., 2018. Residential Investment and Economic Activity: Evidence from the Past Five Decades. BIS Working Papers No. 726. 

Leamer, E.E., 2015. Housing Really is the Business Cycle: What Survives the Lessons of 2006-09. Journal of Money, Credit and Banking 47, 43–50. 

Lichtendahl, K. C., Winkler, R. L., 2020. Why Do Some Combinations Perform Better Than Others? International Journal of Forecasting, 36 (1), 142–149. Makridakis, S., Spiliotis, E., Assimakopoulos, V., 2020. The M4 Competition. 100,000 Time Series and 61 Forecasting Methods. International Journal of Forecasting, 36 (1), 54–74. 

McLeod, A., Li, W., 1983. Diagnostic Checking ARMA Time Series Models Using Squared-Residual Autocorrelations. Journal of Time Series Analysis 4, 269–273. 

Mian, A., Straub, L., Sufi, A., 2021. Indebted Demand. Quarterly Journal of Economics 136 (4), 2243–2307. Miles, W. 2009. Irreversibility, Uncertainty and Housing Investment, Journal of Real Estate Finance and Economics 38,173–182. 

Moral-Benito, E., 2015. Model Averaging in Economics: An Overview. Journal of Economic Surveys 29 (1), 46–75. 

Muellbauer, J., 2022. Real Estate Booms and Busts: Implications for Monetary and Macroprudential Policy in Europe. Presented at the ECB Forum on Central Banking 2022, 29 June, Session 3. 

Nguyen, Q.H., 2013. Housing Investment: What Makes it so Volatile? Theory and Evidence from OECD Countries. Journal of Housing Economics 22 (3), 163–178. 

OECD (2022), Housing taxation in OECD countries. 

Panagopoulos, Y., Vlamis, P., 2009. Bank Lending, Real Estate Bubbles and Basel II. Journal of Real Estate Literature, 17 (2), 295–310. 

Piazzesi, M., Schneider, M., 2016. Housing and Macroeconomics. Chapter 19 in Handbook of Macroeconomics, 2, 1547–1640. Poterba, J. M., 1983. Tax Subsidies to Owner-Occupied Housing. An Asset-Market Approach. Quarterly Journal of Economics 99 (4), 729–752. 

Rodriguez Palenzuela, D., Dees, S. (eds) and the Saving and Investment Task Force, 2016. Savings and Investment Behaviour in the Euro Area, ECB Occasional Paper Series No. 167. 

Steel, M. F. J., 2019. Model Averaging and its Use in Economics. Journal of Economic Literature 58 (3), 644–719. 

Vermeulen, W., Rouwendal, J. 2007. Housing supply in the Netherlands. CPB Discussion Paper, No. 87. Vlamis, P., 2014. Greek Fiscal Crisis and Repercussions for the Property Market. Journal of Property Investment and Finance 32 (1), 21–34. 

Wang, X., Hyndman, R. J., Li, F., Kang, Y., 2022, Forecast Combinations: An Over 50-Year Review. Cornell University. 

World Bank (2021), Doing Business 2021, DB21 data. 

ECB Working Paper Series No 2807 

27 

## **Appendix** 

### **Table A1** <u>Overview of model variables.</u> 

|**Block**|**Category**|**Variable**|**Definition**|
|---|---|---|---|
|||tq1|House price index / residential investment deflator|
||Tobin’s Q|tq2|House price index / total investment deflator|
|||tq3|House price index / private consumption deflator|
|||tq4|Houseprice index / non-housinginvestment deflator|
|||pynhr|Real disposable income per household|
|Long and short-<br>term||laby|Real labour income|
|(3 groups)|Income|winr|Real total compensation|
|||cexr|Real compensation per employee|
|||hafi|Housingaffordabilityindex|
|||lhpr|Loans for house purchase, real|
||Credit|lhpi|Loans for house purchase in % of disposable income|
|||ltv|Loans for housepurchase in % of net non-financial assets|
|||sthour|Real short-term interest rate for house purchase|
||Mortgage<br>interest rates|lthour|Real long-term interest rate for house purchase|
|||tthour|Real composite interest rate for housepurchase|
|||yer|Real GDP|
||Macroeconomic|pcr|Real private consumption|
|||lnn|Total employment|
|Shtt||fod|Real foreign demand|
|or-erm<br>(4 rous)||pop|Total population|
|gp|Demographics|prhh|Number of private households|
||and wealth|hghs|Gross housing stock|
|||hnfa|Net household financial assets|
||Unemployment<br>rate and|urx<br>stovol|Unemployment rate<br>Stock market volatility|
||<br>uncertainty|urxvol|Unemployment volatility|
|||pyrvol|Income volatility|



_Note:_ All variables in log real terms, except Tobin's Q, the loan-to-value ratio, mortgage rates and uncertainty measures. 

### **Table A2** 

Long-run variables included after the cointegration test (S1) 



ECB Working Paper Series No 2807 

28 

### **Table A3** <u>Estimates of long and short-run coefficients of Tobin’s Q, income and credit.</u> 

||**Num**|**ber of**||**Lon**|**g run**|||**Shor**|**t run**||
|---|---|---|---|---|---|---|---|---|---|---|
||**equa**|**tions**|**Coeffi**|**cients**|**t-stat**|**istics**|**Coeffi**|**cients**|**t-sta**|**tistics**|
||**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|
|**Germany**|||||||||||
|Tobin's Q measures|0|22||1||||0.05||0.2|
|Tobin's Q 1|0|0|||||||||
|Tobin's Q 2|0|3||1||||-0.06||-0.2|
|Tobin's Q 3|0|0|||||||||
|Tobin's Q 4|0|19||1||||0.07||0.2|
|Income measures|50|31|2.35|1|3.5***||-0.09|-0.26|-0.2|-0.6|
|Labour income|0|26||1||||-0.32||-0.8|
|Real disposable income per household|50|3|2.35|1|3.5***||-0.09|0.11|-0.2|0.2|
|Real total compensation|0|2||1||||0.06||0.1|
|Real compensation per employee|0|0|||||||||
|Housing affordability index|0|0|||||||||
|Credit measures|50|36|-0.64|-0.96|-1.5|-1.8*|0.70|0.62|1.1|1.0|
|Loans for house purchase (LHPR)|38|36|-0.63|-0.96|-1.5|-1.8*|0.77|0.62|1.1|1.0|
|LHPR to disposable income|12|0|-0.66||-1.2||0.49||0.8||
|LHPR to net non-financial assets|0|0|||||||||
|**France**|||||||||||
|Tobin's Q measures|0|0|||||||||
|Tobin's Q 1|0|0|||||||||
|Tobin's Q 2|0|0|||||||||
|Tobin's Q 3|0|0|||||||||
|Tobin's Q 4|0|0|||||||||
|Income measures|0|3||1||||-0.10||-0.8|
|Labour income|0|3||1||||-0.10||-0.8|
|Real disposable income per household|0|0|||||||||
|Real total compensation|0|0|||||||||
|Real compensation per employee|0|0|||||||||
|Housing affordability index|0|0|||||||||
|Credit measures|50|50|0.20|0.20|3.4***|3.4***|0.26|0.26|1.9*|1.9*|
|Loans for house purchase (LHPR)|50|50|0.20|0.20|3.4***|3.4***|0.26|0.26|1.9*|1.9*|
|LHPR to disposable income|0|0|||||||||
|LHPR to net non-financial assets|0|0|||||||||
|**Italy**|||||||||||
|Tobin's Q measures|0|0|||||||||
|Tobin's Q 1|0|0|||||||||
|Tobin's Q 2|0|0|||||||||
|Tobin's Q 3|0|0|||||||||
|Tobin's Q 4|0|0|||||||||
|Income measures|12|13|4.04|1|2.1**||-0.18|-0.12|-1.0|-0.7|
|Labour income|12|9|4.04|1|2.1**||-0.18|-0.13|-1.0|-0.9|
|Real disposable income per household|0|0|||||||||
|Real total compensation|0|0|||||||||
|<br>Real compensation per employee|0|4||1||||-0.07||-0.3|
|Housing affordability index|0|0|||||||||
|Credit measures|50|50|0.43|0.43|1.5|1.6|0.33|0.38|1.3|1.6|
|Loans for house purchase (LHPR)|50|50|0.43|0.43|1.5|1.6|0.33|0.38|1.3|1.6|
|LHPR to disposable income|0|0|||||||||
|LHPR to net non-financial assets|0|0|||||||||



_Note:_ Coefficients and t-statistics refer to median results for the top 50 selected equations estimated up to 2019Q4. ***, ** and * denote 1%, 5%, respectively, 10% significance. 

ECB Working Paper Series No 2807 

29 

### **Table A3 (cont.)** <u>Estimates of long and short-run coefficients of Tobin’s Q, income and credit.</u> 

||**Num**|**ber of**||**Lon**|**g run**|||**Sho**|**rt run**||
|---|---|---|---|---|---|---|---|---|---|---|
||**equa**|**tions**|**Coeffi**|**cients**|**t-stati**|**stics**|**Coeff**|**icients**|**t-sta**|**tistics**|
||**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|**UN**|**RE**|
|**Spain**|||||||||||
|Tobin's Q measures|50|50|1.94|1|2.1**||0.27|0.21|1.7*|1.1|
|Tobin's Q 1|50|0|1.94||2.1**||0.27||1.7*||
|Tobin's Q 2|0|0|||||||||
|Tobin's Q 3|0|48||1||||0.21||1.1|
|Tobin's Q 4|0|2||1||||0.24||1.8*|
|Income measures|0|50||1||||-0.05||-0.6|
|Labour income|0|0|||||||||
|Real disposable income per household|0|0|||||||||
|Real total compensation|0|0|||||||||
|Real compensation per employee|0|0|||||||||
|Housing affordability index|0|50||1||||-0.05||-0.6|
|Credit measures|50|0|-1.01||-2.5**||0.15||0.8||
|Loans for house purchase (LHPR)|8|0|-1.00||-2.7***||0.14||0.4||
|LHPR to disposable income|42|0|-1.01||-2.5**||0.15||0.9||
|LHPR to net non-financial assets|0|0|||||||||
|**Netherlands**|||||||||||
|Tobin's Q measures|30|50|1.43|1|3.0***||1.10|0.98|2.2**|2.1**|
|Tobin's Q 1|0|0|||||||||
|Tobin's Q 2|0|0|||||||||
|Tobin's Q 3|30|50|1.43|1|3.0***||1.10|0.98|2.2**|2.1**|
|Tobin's Q 4|0|0|||||||||
|Income measures|30|33|0.47|1|2.3**||-0.01|-0.25|0.0|-0.5|
|Labour income|0|0|||||||||
|Real disposable income per household|0|29||1||||-0.30||-0.6|
|Real total compensation|0|0|||||||||
|Real compensation per employee<br>Housing affordability index|0<br>30|0<br>4|0.47|1|2.3**||-0.01|0.12|0.0|0.7|
|Credit measures|0|50||0.13||0.5||-0.12||-0.1|
|Loans for house purchase (LHPR)|0|0|||||||||
|LHPR to disposable income|0|50||0.13||0.5||-0.12||-0.1|
|LHPR to net non-financial assets|0|0|||||||||
|**Euro area**|||||||||||
|Tobin's Q measures|24|25|2.11|1|4.9***||-0.12|0.36|-0.4|1.2|
|Tobin's Q 1|24|25|2.11||4.9***||-0.12|0.36|-0.4|1.2|
|Tobin's Q 2|0|0|||||||||
|Tobin's Q 3|0|0|||||||||
|<br>Tobin's Q 4|0|0|||||||||
|Income measures|5|50|1.93|1|2.2**||0.12|0.04|0.4|0.1|
|Labour income|0|0|||||||||
|Real disposable income per household|5|8|1.93|1|2.2**||0.12|0.04|0.4|0.1|
|Real total compensation|0|0|||||||||
|Real compensation per employee|0|0|||||||||
|<br>Housing affordability index|0|42||1||||-0.04||-0.6|
|Credit measures|42|50|0.03|-10.93|0.3|-0.8|0.34|0.01|0.9|0.3|
|Loans for house purchase (LHPR)|37|25|0.00|0.02|0.0|0.1|0.30|0.25|0.8|0.7|
|LHPR to disposable income|5|0|0.28||2.3**||0.62||1.6||
|LHPR to net non-financial assets|0|25||-21.87||-1.8*||-0.22||-0.2|



_Note:_ Coefficients and t-statistics refer to median results for the top 50 selected equations estimated up to 2019Q4. ***, ** and * denote 1%, 5%, respectively, 10% significance. 

ECB Working Paper Series No 2807 

30 

### **Table A4** 

### <u>Estimates of short-run coefficients.</u> 

||**German**|**y**|**Franc**|**e**|**Italy**||**Spai**|**n**|**Netherla**|**nds**|**Euro a**|**rea**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||**N**<br>**coeff. **|**t-stat**|**N**<br>**coeff. **|**t-stat**|**N**<br>**coeff. **|**t-stat**|**N**<br>**coeff. **|**t-stat**|**N**<br>**coeff.**|**t-stat**|**N**<br>**coeff.**|**t-stat**|
|**Unrestricted model**|||||||||||||
|Mortgage interest rates|50<br>0.42|0.8|50<br>-0.46|-3.0 **|* 50<br>-1.17|-2.5 **|* 50<br>-0.21|-0.5|30<br>0.03|0.1|50<br>-0.26|-0.6|
|Composite interest rate for house purchase|11<br>0.30|0.6|21<br>-0.50|-3.3 **|* 20<br>-1.20|-2.5 **|* 15<br>-0.20|-0.4|10<br>0.00|0.0|18<br>-0.30|-0.7|
|Short-term interest rate for house purchase|29<br>0.50|1.0|9<br>-0.50|-3.1 **|* 25<br>-1.20|-2.6 **|* 15<br>-0.10|-0.3|10<br>0.10|0.2|10<br>-0.10|-0.2|
|Long-term interest rate for house purchase|10<br>0.30|0.5|20<br>-0.40|-2.6 **|5<br>-0.90|-1.9 *|20<br>-0.30|-0.7|10<br>0.00|-0.1|22<br>-0.30|-0.7|
|Macroeconomic indicators|4<br>1.39|2.4 **|36<br>-0.17|0.2|50<br>1.64|4.4 **|* 49<br>1.44|2.7 **|* 30<br>2.52|3.3 **|* 42<br>1.98|3.2 ***|
|Real GDP|0<br>-|-|10<br>0.35|1.9 *|50<br>1.64|4.4 **|* 30<br>1.55|2.9 **|*<br>0<br>-|-|0<br>-|-|
|Real private consumption|3<br>1.04|2.5 **|6<br>0.14|0.8|0<br>-|-|5<br>0.68|1.5|30<br>2.52|3.3 **|*<br>0<br>-|-|
|Total employment|1<br>2.46|2.2 **|20<br>-0.53|-0.9|0<br>-|-|14<br>1.47|2.7 **|*<br>0<br>-|-|21<br>3.73|4.7 **|
|Foreign demand|0<br>-|-|0<br>-|-|0<br>-|-|0<br>-|-|0<br>-|-|21<br>0.23|1.8 *|
|Population and wealth measures|27<br>-2.15|-2.0 **|5<br>0.00|-0.1|19<br>-0.27|-0.4|2<br>0.44|0.9|18<br>-9.58|-1.6|19<br>-0.98|-0.8|
|Number of private households|27<br>-2.15|-2.0 **|0<br>-|-|3<br>-1.52|-1.4|1<br>0.79|0.8|3<br>-7.21|-1.1|16<br>-1.21|-0.9|
|Total population|0<br>-|-|0<br>-|-|16<br>-0.03|-0.3|0<br>-|-|12<br>-12.50|-1.4|1<br>0.71|0.2|
|Gross housing stock (-1)|0<br>-|-|0<br>-|-|0<br>-|-|0<br>-|-|0<br>-|-|0<br>-|-|
|Net financial assets (-1)|0<br>-|-|5<br>0.00|-0.1|0<br>-|-|1<br>0.08|1.0|3<br>-0.29|-3.0 **|*<br>2<br>-0.01|-0.2|
|Unemployment rate and uncertainty|27<br>0.01|0.0|38<br>-0.20|-1.1|38<br>0.90|1.5|44<br>0.90|1.6|24<br>0.84|0.6|35<br>-0.33|-1.4|
|Unemployment rate|0<br>-|-|23<br>-0.60|-1.7 *|0<br>-|-|0<br>-|-|0<br>-|-|0<br>-|-|
|Stock market volatility|8<br>-0.20|-0.4|2<br>-0.30|-2.0 **|0<br>-|-|44<br>0.90|1.6|9<br>0.40|0.4|29<br>-0.50|-1.7 *|
|Unemployment volatility|0<br>-|-|10<br>0.10|0.5|38<br>0.90|1.5|0<br>-|-|9<br>1.90|1.3|1<br>0.00|0.2|
|Income volatility|19<br>0.10|0.1|3<br>0.10|0.7|0<br>-|-|0<br>-|-|6<br>-0.10|-0.1|5<br>0.60|0.4|
|Lagged housing investment growth|50<br>-0.01|-0.5|50<br>2.27|0.5|50<br>-1.26|-0.3|50<br>0.07|0.8|30<br>-0.08|0.2|50<br>0.17|0.4|
|Housing investment (-1)|50<br>0.00|-0.1|50<br>0.49|0.1|50<br>-0.22|-0.1|50<br>0.01|0.1|30<br>-0.02|0.0|50<br>0.03|0.1|
|Housinginvestment(-2)|50<br>-0.02|-0.9|50<br>4.05|0.8|50<br>-2.31|-0.6|50<br>0.12|1.4|30<br>-0.15|0.4|50<br>0.30|0.8|
|**Restricted model**|||||||||||||
|Mortgage interest rates|50<br>0.35|0.6|50<br>-0.47|-3.0 **|* 50<br>-1.26|-2.6 **|* 50<br>-0.07|-0.2|50<br>0.03|0.1|50<br>-0.06|-0.1|
|Composite interest rate for house purchase|12<br>0.30|0.5|24<br>-0.50|-3.2 **|* 20<br>-1.20|-2.6 **|* 16<br>-0.10|-0.1|19<br>0.10|0.2|17<br>0.00|-0.1|
|Short-term interest rate for house purchase|26<br>0.40|0.7|9<br>-0.50|-3.1 **|* 29<br>-1.30|-2.7 **|* 15<br>0.00|-0.1|14<br>0.20|0.3|15<br>-0.20|-0.4|
|Long-term interest rate for house purchase|12<br>0.30|0.5|17<br>-0.40|-2.6 **|*<br>1<br>-0.01|-2.9 **|* 18<br>-0.10|-0.3|17<br>-0.20|-0.3|18<br>0.00|0.1|
|Macroeconomic|48<br>1.09|2.3 **|34<br>-0.23|0.0|50<br>1.70|4.5 **|* 29<br>0.28|0.4|50<br>2.91|4.2 **|* 50<br>0.39|2.6 **|
|Real GDP|0<br>-|-|8<br>0.32|1.7 *|50<br>1.70|4.5 **|*<br>3<br>0.78|1.1|30<br>3.12|4.9 **|*<br>8<br>1.04|3.9 ***|
|Real private consumption|45<br>0.99|2.3 **|5<br>0.14|0.8|0<br>-|-|16<br>0.47|0.9|20<br>2.60|3.3 **|*<br>0<br>-|-|
|Total employment|3<br>2.67|2.3 **|21<br>-0.53|-0.9|0<br>-|-|0<br>-|-|0<br>-|-|0<br>-|-|
|Foreign demand|0<br>-|-|0<br>-|-|0<br>-|-|10<br>-0.18|-0.6|0<br>-|-|42<br>0.27|2.3 **|
|Demographics and wealth|23<br>-2.12|-2.1 **|6<br>0.17|0.5|19<br>0.31|0.3|39<br>-0.05|0.3|16<br>-0.17|-0.3|14<br>-0.08|-0.1|
|Number of private households|23<br>-2.12|-2.1 **|0<br>-|-|0<br>-|-|0<br>-|-|0<br>-|-|7<br>-0.14|-0.1|
|Total population|0<br>-|-|0<br>-|-|16<br>-0.03|-0.3|0<br>-|-|0<br>-|-|0<br>-|-|
|Gross housing stock (-1)|0<br>-|-|1<br>1.05|3.3 **|*<br>3<br>2.12|3.2 **|* 18<br>-0.20|-0.4|16<br>-0.17|-0.3|0<br>-|-|
|Net financial assets (-1)|0<br>-|-|5<br>0.00|-0.1|0<br>-|-|21<br>0.08|0.9|0<br>-|-|7<br>-0.01|-0.2|
|Unemployment rate and uncertainty|29<br>-0.54|-0.4|40<br>-0.34|-0.9|50<br>0.80|1.5|19<br>0.14|0.3|38<br>0.42|0.3|23<br>0.02|0.1|
|Unemployment rate|5<br>-3.10|-2.0 **|2<br>-0.30|-2.0 **|0<br>-|-|10<br>0.90|1.4|2<br>-1.50|-0.5|2<br>-0.80|-0.6|
|Stock market volatility|3<br>-0.10|-0.2|11<br>0.10|0.5|0<br>-|-|0<br>-|-|8<br>0.60|0.6|21<br>0.10|0.1|
|<br>Unemployment volatility|3<br>0.60|0.7|3<br>0.10|0.7|50<br>0.80|1.5|0<br>-|-|16<br>1.40|1.0|0<br>-|-|
|<br>Income volatility|18<br>-0.10|-0.1|24<br>-0.60|-1.7 **|0<br>-|-|9<br>-0.70|-0.9|12<br>-0.70|-0.6|0<br>-|-|
|Lagged housing investment growth|50<br>0.33|-0.6|50<br>2.27|0.5|50<br>-1.19|-0.3|50<br>0.90|1.3|50<br>0.23|0.4|50<br>0.06|0.0|
|Housing investment (-1)|50<br>0.07|-0.1|50<br>0.49|0.1|50<br>-0.21|0.0|50<br>0.19|0.2|50<br>0.04|0.1|50<br>0.01|0.0|
|Housinginvestment(-2)|50<br>0.59|-1.0|50<br>4.05|0.8|50<br>-2.17|-0.5|50<br>1.62|2.4 **|50<br>0.42|0.8|50<br>0.10|0.1|



_Note:_ Coefficients and t-statistics refer to median results for the top 50 selected equations estimated up to 2019Q4. ***, ** and * denote 1%, 5%, respectively, 10% significance. 

ECB Working Paper Series No 2807 

31 



**Fig. A1.** Out-of-sample forecasts for 2018Q4 – 2020Q3 based on top 50 selected unrestricted model equations estimated over 1999Q1 – 2018Q3. Housing investment level in 2018Q3 = 100. 

ECB Working Paper Series No 2807 

32 



ECB Working Paper Series No 2807 

33 



ECB Working Paper Series No 2807 

34 



ECB Working Paper Series No 2807 

35 



ECB Working Paper Series No 2807 

36 



ECB Working Paper Series No 2807 

37 



ECB Working Paper Series No 2807 

38 

#### **Acknowledgements** 

The authors would like to thank three anonymous referees for their comments, which greatly helped to strengthen the paper. We also acknowledge comments received at an internal ECB meeting, a meeting of the Eurosystem Working Group on Forecasting, at the ICMAIF 2022 conference as well as from Christian Brownlees (Universitat Pompeu Fabra), Michal Marenčák (National Bank of Slovakia), and the Editorial Board of the ECB Working Paper Series. 

This paper was first published 17 January 2023 in the Journal of Forecasting, Volume 42, Issue 3, Special Issue: Advances in Forecasting in Macroeconomics and Financial Markets, 2023, pp. 543-565, https://doi.org/10.1002/for.2946. Reproduced by permission of Wiley. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use. © 2023 John Wiley & Sons, Ltd. 

All views expressed in this paper are those of the authors and do not necessarily reflect the position of their institutions. 

#### **Carlos Cañizares Martínez** 

National Bank of Slovakia, Bratislava, Slovakia; email: carlos.canizares.martinez@nbs.sk 

**Gabe J. de Bondt** (Corresponding author) 

European Central Bank, Frankfurt am Main, Germany; email: gabe.de_bondt@ecb.europa.eu 

#### **Arne Gieseck** 

European Central Bank, Frankfurt am Main, Germany; email: arne.gieseck@icloud.com 

#### **© European Central Bank, 2023** 

Postal address 60640 Frankfurt am Main, Germany Telephone +49 69 1344 0 Website www.ecb.europa.eu 

All rights reserved. Any reproduction, publication and reprint in the form of a different publication, whether printed or produced electronically, in whole or in part, is permitted only with the explicit written authorisation of the ECB or the authors. 

This paper can be downloaded without charge from www.ecb.europa.eu, from the Social Science Research Network electronic library or from RePEc: Research Papers in Economics. Information on all of the papers published in the ECB Working Paper Series can be found on the ECB’s website. 

PDF ISBN 978-92-899-6070-0 ISSN 1725-2806 doi:10.2866/531765 QB-AR-23-044-EN-N 

