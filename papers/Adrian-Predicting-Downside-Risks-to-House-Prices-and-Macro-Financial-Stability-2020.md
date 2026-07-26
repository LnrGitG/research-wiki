---
title: **WP/��/��**
type: paper
source_pdf: raw/papers/Adrian_Predicting Downside Risks to House Prices and Macro-Financial Stability_2020.pdf
converted: 2026-07-26
---

# **WP/��/��** 

Predicting Downside Risks to House Prices and Macro-Financial Stability 

by Tobias Adrian, Andrea Deghi, Mitsuru Katagiri, Sohaib Shahid, and Nico Valckx 

**_IMF Working Papers_ describe research in progress by the author(s) and are published to elicit comments and to encourage debate.** The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management. 

© 20��International Monetary Fund 

�������� 

#### **IMF Working Paper** 

Monetary and Capital Markets Department 

#### **Predicting Downside Risks to House Prices and Macro-Financial Stability** 

**<mark>Prepared by ���������������Andrea Deghi, Mitsuru Katagiri, Sohaib Shahid, and Nico Valckx</mark>**<sup>**1**</sup> 

Authorized for distribution by Jérôme Vandenbussche 

������������ 

**IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate.** The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management. 

#### **Abstract** 

This paper predicts downside risks to future real house price growth in 32 advanced and emerging market economies. Using a macro-model and predictive quantile regressions, we show that current house price overvaluation, excessive credit growth, and tighter financial conditions jointly forecast higher house-prices-at-risk up to three years ahead. House-prices-at-risk in turn predict future downside risks to economic growth and financial crises. We further investigate and propose policy solutions for preventing the identified risks. We find that tightening macroprudential policy is the most effective across both short and longer horizons, whereas a loosening of conventional monetary policy reduces short term downside risks only in advanced economies. 

JEL Classification Numbers: C12, E17, E37, R31 

Keywords: House Prices; Growth at Risk; Panel Quantile Regression; Early Warning Models; Macroprudential Policy; Monetary Policy 

> 1 ����������������������������������������������������������������������������������������������������� ������������������������������������������������������������������������������������������������������������� ������������������������������������������������������������������������������������������������������������������ ����������������������������������������������������������������������������������������������������������� ����������������������������������������������������������������������������������������������������������������� ��������������������� 

## **Contents** 

|**1**|**Intr**|**oduction**|**4**|
|---|---|---|---|
|**2**|**The**|**oretical Framework**|**9**|
|**3**|**Dat**|**a and Methodology**|**16**|
||3.1|Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>16|
||3.2|Modeling House-Prices-at-Risk<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>20|
|**4**|**Em**|**pirical Results**|**22**|
||4.1|Baseline Estimations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>22|
|||4.1.1<br>Out-of-Sample Evidence . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>26|
|||4.1.2<br>Additional Robustness tests . . . . . . . . . . . . . . . . . . . . . .|. . .<br>29|
||4.2|Contribution of House-Prices-at-Risk to Macro-Financial Stability . . . . .|. . .<br>31|
||4.3|Policies to Mitigate Downside Risks to House Prices<br>. . . . . . . . . . . .|. . .<br>34|
|||4.3.1<br>Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>39|
|**5**|**Con**|**clusion**|**43**|
|**A **|**App**|**endices**|**48**|
||A.1|Tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>48|
||A.2|Data Sources and Defnitions<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>68|
||A.3|Additional Decomposition of HaR at Selected Horizons . . . . . . . . . . .|. . .<br>70|
||A.4|Additional Robustness Tests . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>73|
||A.5|Out-of-Sample Analysis: Probability Integral Transform . . . . . . . . . .|. . .<br>87|



3 

## **1 Introduction** 

Developments in the housing market are important for various economic agents—banks, households and firms. Housing serves both as a long-term investment and as a consumption good that generates considerable utility for households. Housing consumption and investment accounted for about one sixth of the GDP in the US and euro area economies in 2017, representing one of the largest components of GDP in both cases. Since housing makes up a large share of households’ wealth in many countries, drops in house prices decrease households’ net worth and can thus reduce consumption. At the same time, mortgages and other housing-related lending make up a large fraction of banks’ assets. Sudden and sharp house price declines can decrease the value of collateral pledged by borrowers and negatively impact banks’ portfolio quality, profitability, and stability.<sup>1</sup> 

During the COVID-19 pandemic crisis, the housing market has been exceptionally resilient, sustained by continued accommodative monetary policy and strong demand for new homes. However, sustained periods of rapid growth in house prices can create the expectation that such prices will continue to rise in the future, potentially leading to excessive risk-taking and rising vulnerabilities in the housing market. As central banks around the world need to tighten monetary policy in response to the global surge in inflation in the aftermath of the pandemic, it is crucial to identify how large future downside risks to house prices are, and what they imply for financial stability. 

In view of these questions, this paper is the first to propose a novel non-parametric approach to predict downside risks to house prices (i.e., house-prices-at-risk) and their impact on the risk of future macroeconomic downturns. We first develop a macroeconomic model to motivate our empirical specification and then apply quantile regressions to show how current house price 

> 1Claessens et al. (2012) show that recessions are deeper and last longer when house prices fall more and more quickly, and more than two-thirds of the nearly 50 systemic banking crises in recent decades were preceded by boom-bust patterns in house prices. Moreover, certain housing market characteristics, such as higher loan-to-value ratios and greater reliance on wholesale markets, are associated with even higher risks of crises. The interactions between house prices and credit volumes may also result in selfreinforcing feedback loops where an increase in house prices facilitates an expansion in credit (through collateral effects) that puts further upward pressure on house prices. When that process is reversed, large house price declines may be followed by a collapse in credit and GDP growth. 

4 

overvaluation, excessive credit growth, and tighter financial conditions can jointly forecast higher house-prices-at-risk up to three years ahead. Our measure of risk in the housing market, in turn, predicts future financial crises and economic downturns. Finally, our model puts forward several policy measures that could mitigate future sudden downturns, which we analyze in our prediction framework. We find that macroprudential policies are the most effective while conventional monetary policy only relieves pressure in advanced economies and in the very short term. 

The house-prices-at-risk (HaR) measure we develop uses the 5th percentile of the conditional house price growth distribution, which reflects the nonlinear nature of house prices Duca et al. (2021) and that large and sudden downturns in house prices bear the highest risk for financial stability. Our model and quantile regressions show that the left tail of the house prices growth distribution is mainly driven by fundamental factors, including financial conditions, GDP growth, credit growth, and house price overvaluation. For instance, a one-standarddeviation tightening of financial conditions is associated with an up to 0.7 percentage point higher downside risk to house prices in the short term. Credit booms further exacerbate the incidence of large negative house price corrections at short- and medium-term horizons by up to 0.5 percentage points, which is in line with historical evidence Schularick and Taylor (2012). Importantly, we evaluate the out-of-sample performance of the model by only using information available at and before the time of prediction. The stability of the recursive out-of-sample estimates shows that our framework can effectively predict future downside risk to house prices in real-time. 

Large declines in house prices in turn forecast future risks to economic growth and serve as a leading indicator for financial stability risks captured by the growth-at-risk (GaR) model of Adrian et al. (2019). In general, the GaR framework links current macrofinancial conditions to the distribution of future growth.We find that a negative 12 percent on our gauge—corresponding to a 5 percent probability of at least a 12 percent drop in house prices—indicates a 31 percent probability of a financial crisis two years later in advanced economies and a 10 percent probability in emerging markets. Overall, the highest impact of HaR on financial stability is four 

5 

to eight quarters into the future, with a 1 percentage point decline in the house-prices-at-risk measure preceding on average a 0.3 percentage point decline in growth at risk. This association is robust to using alternative credit quantity measures and other indirect measures of house price imbalances in the GaR specification. 

To understand how house price downturns arise and how policy can mitigate the associated financial stability risks, we develop a comprehensive macroeconomic framework. In our model, housing crises are a vicious cycle of real GDP and house price declines. When household debt levels are high, further borrowing by households in response to income declines makes the collateral constraint bind. Fire sales of homes follow, leading to a decline in house prices and further tightening of the collateral constraint. As a result, aggregate demand and household incomes drop and another round of deteriorating conditions ensues. Macroprudential measures, such as a Pigouvian tax on household debt, can alleviate the negative effects of housing crises on the real economy by preventing the tightening of collateral constraints from a decline in house prices. Monetary policy, however, does not have any direct effect on house price growth in times of distress other than through general financial conditions. 

The predictions of the model are confirmed by our empirical analysis. First, we combine information on the tightening and loosening of interventions to create a proxy for the intensity of the macroprudential policy stance. The measure is “purged” of the variation due to credit-to-GDP to mitigate potential endogeneity concerns. Second, we create monetary policy shocks as residuals from a Taylor rule specification. We then re-estimate the baseline house prices-at-risk specification with our constructed policy measures. We find that a tightening of macroprudential policies is associated with a reduction of downside risks to house prices. This is especially the case for policies aimed at strengthening the resilience of borrowers, such as limits on loan-to-value and debt-service-to-income ratios. The ability of monetary policy to mitigate downside risks to housing prices, beyond its relationship with financial conditions, seems more limited. Financial conditions, which are partly driven by monetary policy actions, have a clear relationship with downside risks to house prices. Beyond this indirect effect, the influence of conventional monetary policy is limited to the short-term and to advanced economies. 

6 

Taken together, our results establish the house-prices-at-risk measure as a novel and important indicator of risks in the housing sector. The quantitative framework that we develop can successfully predict house-prices-at-risk out of sample, which allows for real-time monitoring and forecasting. Finally, our macroeconomic model sheds light on the effectiveness of policy interventions aimed at restoring the efficient functioning of the housing market. 

**Related Literature.** One of our main contributions is in analyzing the predictors of downside risks to housing markets. The literature has mostly focused on the determinants of average house prices. Recent studies find that house prices are tied to household income, macrofinancial conditions, and structural factors such as population growth and urbanization (Duca et al., 2021). Other studies point to the role of leverage, credit constraints, and bank regulation (Duca et al., 2010; Favara and Imbs, 2015), global financial integration (Cesa-Bianchi et al., 2018), and the presence of speculative bubbles in housing markets (Schularick and Taylor, 2012; Kuttner and Shim, 2016; Glaeser and Nathanson, 2017). Another set of papers has looked at booms and busts in house prices. For example, Cerutti et al. (2017) also examine the potential role of housing finance characteristics on the likelihood of house price booms and busts. 

This paper is the first to study the relationship between fundamental factors and house price tail risks and quantify their implications for financial stability. Our approach is novel as it focuses on the 5th percentile of the house price distribution as a risk measure. One key benefit of our measure is that it does not rely on any ex-post classification of boom-and-bust periods. It can be measured in real-time and flexibly applied to both in- and out-of-sample tests. In addition, using local projections allows us to explore the evolution of risk over the forecast horizon. 

We also contribute to the literature studying the effect of house prices on aggregate measures of economic activity (Mian et al., 2013; Jordà et al., 2015). For instance, Mian et al. (2017) show that rising household debt-to-GDP ratios predict slower GDP growth in the medium run. There is also evidence that elevated house prices growth can improve the forecast of financial crisis based on overall credit growth (Richter et al., 2021). We extend these previous stud- 

7 

ies by identifying the existence of a strong nonlinear relationship between the left tail of the conditional house price growth distribution and downside risks to future economic activity. 

Our methodological approach involves estimating and evaluating conditional distributions. Previous research by Adrian et al. (2019) proposed a two-step procedure for estimating the conditional probability distribution function, while Giglio et al. (2016) utilized a quantile regression approach to assess the ability of various systemic risk measures to predict the distribution of shocks to real economic activity. In our study, we build on these works by utilizing panel quantile regression methods to examine the primary drivers of downside risks in house prices. Furthermore, our study is the first to quantify the impact of tail risks in house prices on future downside risks to GDP. The association between the historical average of downside risk for house prices (HaR) and the conditional growth at the lower 5th percentile of the GDP growth distribution (defined as growth-at-risk or GaR) is illustrated in Figure 1. 



**Figure 1: Relationship between Growth-at-Risk (GaR) and House-Prices-at-Risk (HaR).** This figure shows the unconditional relationship between GaR (y-axis) and HaR forecasts lagged by four quarters (x-axis). GaR is the conditional growth at the (lower) 5th percentile of the GDP growth distribution, and thus captures expected growth at a low realization of the GDP growth distribution. Forecasts are estimated separately at a one year predictive horizon for a panel of 22 major advanced economies and a panel of 10 emerging market economies. 

8 

Finally, we contribute to the discussion on the effectiveness of different policy measures in curbing housing bubbles and financial stability risks. Borio and Shim (2007) support augmenting macroprudential tools with “a lean against the wind” monetary policy to prevent house price inflationary pressures. In contrast, others argue that the welfare losses of using monetary policies outweigh their benefits (Svensson, 2017) and that macroprudential tools can be more effective in limiting household debt (Richter et al., 2019; Alam et al., 2019).<sup>2</sup> We inform this debate by showing how macroprudential policies can specifically target the downside risk in the house price growth distribution, which foreshadows future financial crises. To identify the effect of policies on the trade-off we examine policy surprises, constructed as deviations from estimated policy rules. Our findings provide support for the effectiveness of macroprudential policies versus monetary policy and are rationalized in a macroeconomic framework. 

The remainder of the paper is organized as follows. First, in Section 2, we develop a theoretical foundation for the determinants of house price risks and the effects of macroprudential and monetary policies. In Section 3, we detail the panel quantile methodology and data. Section 4 presents the main findings on house prices-at-risk, the contribution of HaR to macro-financial stability, and the effects of monetary and macroprudential policies on HaR. Section 5 concludes. 

## **2 Theoretical Framework** 

This paper applies a nonlinear dynamic stochastic general equilibrium (DSGE) model with occasionally binding housing collateral constraints. The approach generally follows Guerrieri and Iacoviello (2017) ignores interactions with the corporate sector and focuses on the household sector by distinguishing between two types of households with different discount factors: borrowers and lenders. Households maximize their utility by choosing consumption, leisure, and housing, subject to budget and collateral constraints. Housing is the only collateral for borrowing, and house prices are determined by a standard forward-looking asset pricing formula. 

> 2In this context, Miao et al. (2019) also show how macroprudential tools can help reduce bubble volatility and are optimal in a rational bubble model with serially correlated bubble shocks and adaptive learning. 

9 

The collateral constraint is not always but occasionally binding, depending on house prices, income, and debt level. Other parts of the model align with a standard DSGE model with Euler equations for each type of household, a new Keynesian Phillips curve, and a monetary policy rule. 

More specifically, the economy consists of borrowers and lenders. In this economy, the borrower maximizes: 



where _ct_ denotes consumption of goods and services, _ht_ housing consumption, _Lt_ labor (the complement of leisure), _β_<sup>_t_</sup> is a discount factor, _σ_ and _ω_ are elasticities of substitution, Ψ and _χ_ are preference parameters. _E_ 0 is the conditional expectations operator and _t_ is a time subscript. Borrowers are subject to the budget constraint: 



where _bt−_ 1 denotes real savings (or borrowing) in the previous period, _wt_ real wages, _qt_ is the house price, as in Guerrieri and Iacoviello (2017), and _R_ is the gross interest rate. 

The borrower’s collateral constraint is: 



where _κ_ and _γ_ determine the tightness of the collateral constraint (both are positive factors). By assuming that the housing supply is fixed and _ht_ = 1 for all _t_ , the equilibrium is characterized by the Euler equation for the borrower: 



10 

and the asset pricing formula for the house price 



where _λt_ = _c_<sup>_−_</sup> _t_<sup>_σ_</sup> and _µt_ is a Lagrange multiplier for the collateral constraint, satisfying the complementary slackness. The latter condition implies that at least one of the following constraints must hold with equality in each period: 



The lender’s problem is analogous to the borrower’s problem, but the lender does not consume housing and does not face the borrowing constraint. The nominal interest rate _Rt_ is set by the central bank following a Taylor rule, based on deviations of (year-on-year) inflation from its target and the output gap, 



where _R_ the steady-state interest rate, _π_ the inflation rate and _π_<sup>_∗_</sup> the inflation target, _y_ / _y_<sup>_∗_</sup> the output gap and _ϕπ_ and _ϕ_ y central bank preference parameters. The corporate sector follows a standard new Keynesian model, and the price and output dynamics are characterized by the new Keynesian Phillips curve. The model is numerically solved by the iteration method with discretized grid points for productivity and the borrower’s debt. 

The model successfully replicates housing crises.<sup>3</sup> The blue line in Figure 2a shows the 

> 3Since the purpose of this quantitative exercise is to give a suggestive prediction, the parameter values are just set to standard ones in the literature. The discount factor, _β_ , the CRRA coefficient, _σ_ , and the inverse of Frisch elasticity, _ω_ , are calibrated to 0.96, 2.0, and 0.5, respectively. The value of _χ_ and Ψ are arbitrarily set to 0.2 and 0.6 because they only influence the steady state values and have little effect on simulation results. On the parameter values for the collateral constraint, the value of maximum LTV ratios, _κ_ , varies across previous studies, from 0.35 in Bianchi (2011) to 0.90 in Guerrieri and Iacoviello (2017). Hence, _κ_ = 0 _._ 65 in this study. Also, since the inertia of borrowing constraint, _γ_ , 

11 

ergodic distribution of output gaps (that is, the gap from the steady-state level) in the baseline simulation, indicating that the model can replicate massive declines in output during a housing crisis. In the model, housing crises are described as a vicious cycle of output and house price declines due to the binding collateral constraint: when the level of household debt is high, further borrowing by households in response to an income decline makes the collateral constraint bind. Then, households start "fire sales" of their houses (an alternative interpretation may be as foreclosures) because they cannot borrow, leading to a decline in house prices and further tightening of the collateral constraint. Since the binding collateral constraint prevents households from borrowing, it forces them to reduce their consumption, decreasing aggregate demand, output, wages, and household income, thus leading to another round of deteriorating conditions within the vicious cycle. 

The model also predicts a positive association between the initial level of household debt and the incidence of housing crises. Figure 2b presents scatter plots of house price growth in period _t_ (the vertical axis) against the debt-to-GDP ratios in period _t_ -1 (the horizontal axis). The three lines are the estimated fifth, fiftieth, and ninety-fifth percentile. The figure indicates that while higher debt-to-GDP ratios have no effects (or slightly positive effects) on median growth of house prices, they significantly increase the probability of housing crises, which is consistent with this paper’s empirical analysis using a quantile regression. The model, therefore, offers a theoretical foundation as to why debt-to-GDP ratios can be used as an early warning indicator. 

Three policy measures to mitigate the adverse effects of housing crises are examined. First are macroprudential measures (MPMs). MPMs are modeled as a Pigouvian tax on debt following the literature, e.g. in Bianchi and Mendoza (2018). While the MPM rule to internalize the pecuniary externality is a complicated and nonlinear function of state variables, it can be well approximated by a linear function of household debt (that is, high taxes on debt when the debt level is high).<sup>4</sup> The second policy measure is monetary policy augmented by a response to 

> varies from zero in Bianchi (2011) and Bianchi and Mendoza (2018) to 0.64 in Guerrieri and Iacoviello (2017), _γ_ is set to 0.35. Finally, the monetary policy is assumed to follow the standard Taylor rule with _ϕπ_ = 1 _._ 5 and _ϕy_ = 0 _._ 5. 

> 4Note that other MPMs including caps on loan-to-value ratios and surcharges on lending rates for 

12 

household debt. Under this monetary policy rule, nominal interest rates are positively linked to household debt levels, implying that the central bank increases interest rates in a run-up period while it lowers interest rates in response to deleveraging. The third policy measure is monetary policy augmented by a response to credit spreads, as argued by Curdia and Woodford (2011). The credit spread in the model is defined by the interest rate gap between secured and unsecured lending (i.e., without housing collateral). Since the spread is negligible in normal times, the central bank behaves differently from the baseline case only in a crisis by lowering interest rates in response to higher credit spreads. 

More specifically, to discuss the effect of MPMs, the Euler equation for the social planner (i.e., the authority) is defined by: 



and the house price _qt′_ +1<sup>is compared with the competitive equilibrium.The only difference</sup> from the borrower’s first order condition is the term associated with the first derivative of the next period’s house price with respect to the current level of household debt, _qt′_ +1<sup>(</sup><sup>_bt_).To</sup> replicate the social planner’s Euler equation in a decentralized economy, the macroprudential tax, _ωt_ , is imposed on household debt. With the macroprudential tax, the borrower’s budget constraint is 



In this case, the borrower should pay a macroprudential tax in addition to interest rate payments. The macroprudential tax rate is state contingent and chosen by the authority so that the Euler equation for the borrower matches the one for the social planner. 

Macroprudential measures lower the probability of housing crises and mitigate their negative effects. The green line in Figure 2a shows the ergodic distribution of the output gap household debt are mathematically equivalent to MPMs using taxes on debt in the model. 

13 

with MPMs. The figure shows that compared with the baseline case without MPMs (the blue line), MPMs significantly decrease the variance of the output gap, particularly by shrinking the left tail of the distribution. This result suggests that MPMs are effective in preventing and mitigating the impacts of housing crises. 



<!-- Start of picture text -->
2a. Ergodic Distribution of the Output Gap 2b. Credit-to-GDP and Real House Price Growth<br>0.18 6<br>Baseline<br>0.16 with MPMs 4<br>0.14 2<br>0.12 0<br>0.10 -2<br>0.08 -4<br>0.06 -6<br>0.04 -8<br>0.02<br>-10<br>0.00 -3 -2 -1 0 1<br>-1.0 -0.8 -0.6 -0.4 -0.2 0.0 0.2 0.4 Credit-to-GDP ratio (t)<br>2c. Variables’ Response under Different Policy Regimes<br>House price growth (t+4)<br><!-- End of picture text -->



<!-- Start of picture text -->
Base MP1 MP2 MPM MP1 MP2 MPM Base MP1 MP2 MPM Base MP1 MP2MPM<br>0 0 -4 -2.8<br>-1<br>-5<br>-1 -3.0<br>-2<br>-6<br>-3 -2 -3.2<br>-7<br>-4<br>-3 -3.4<br>-8<br>-5<br>-6 -4 -9 -3.6<br>(i) Output Growth (ii) House Price Growth (iii) Interest Rate Change (iv) Change in<br>(percent) (percent) (percentage points) Credit-to-GDP<br>(percent, wrt baseline)<br><!-- End of picture text -->

**Figure 2: Impact of Monetary and Macroprudential Policies in the Theoretical Model.** This figure shows results from the theoretical framework described in Section 2. The blue line depicts the ergodic distribution of output gaps (that is, the gap from the steady-state level) in the baseline simulation. The green line depicts the ergodic distribution of output gaps after the introduction of macroprudential measures (MPM). Panel 2 shows different associations between debt-to-GDP and house price growth for the lower 5th percentile (red line), 50<sup>th</sup> percentile (median, orange line) and 95th percentile (green line). In panel 3, output growth less than _−_ 3 percent in the baseline model (Base) is defined as crisis period. MP1 = monetary policy rule augmented by the response to household debt-to-GDP; MP2 = monetary policy rule augmented by the response to credit spreads. MPM = macroprudential tax on credit-to-GDP ratio. 

14 

To see the policy effects during crisis periods more precisely, the first three panels in Figure 2c show output growth, house price growth, and nominal interest rates during crisis periods. In the figure, the crisis periods are defined as those with declines in output of more than 3 percent. The first and second panels in Figure 2c show that MPMs mitigate the decline in both output growth and house price growth during a crisis. This result suggests that MPMs mitigate the negative effects of housing crisis on the real economy by limiting the tightening of collateral constraints from declining house prices. Panel iv in Figure 2c shows that the average level of household debt is significantly lower than in the baseline case, not only during run-up periods but also in normal times. 

Monetary policy responding to household debt mitigates the adverse effects of housing crises, but its policy effect is insignificant relative to MPMs. In this exercise, the monetary policy rule is augmented by a response to household debt, and the parameters are calibrated so that the steady state debt level is at the same level as in the economy with MPMs (the fourth panel in Figure 2c). The results show that while monetary policy responding to household debt slightly mitigates the adverse effects on output growth in a crisis (panel i), it does not have any effects on house price growth in crisis periods, in contrast to MPMs (panel ii). The decline in nominal interest rates in times of crisis is larger than in the baseline case (panel iii) because the central bank now lowers rates in response to deleveraging. Hence, the augmented monetary policy rule does not improve house prices and only slightly mitigates the adverse effects on output growth by: (i) subduing debt accumulation before a crisis, and (ii) lowering nominal interest rates in response to deleveraging. The results suggest that monetary policy may be too blunt as a tool for crisis management (Bernanke, 2012; Svensson, 2017).<sup>5</sup> 

There are, however, several caveats. First, the exercise shows a very specific form of the monetary policy rule, namely the conventional Taylor rule augmented by a linear response to household debt. This does not mean that all monetary policy rules in a more general form may not work for crisis management. Second, in the midst of a crisis, monetary policy can respond 

> 5Surcharges on lending rates for household debt are equivalent to MPMs using taxes on debt in the model. Hence, the augmented monetary policy performs worse than MPMs only because the monetary policy influences not only lending rates but also other relevant interest rates including deposit rates. 

15 

more promptly than MPMs, and may be more practically useful for policymakers. 

Monetary policy responding to credit spreads also mitigates the negative effects of housing crises, but its policy effect is also limited and assumes considerable room for policy reactions. As in the previous case, Figure 2c shows that monetary policy responding to credit spreads slightly mitigates the adverse effects on output growth in a crisis (left panel) but does not bear any effects on house price growth in a crisis (middle panel). Hence, monetary policy under this rule does not prevent crises per se but mitigates their adverse effects on output growth by lowering nominal interest rates and thus boosting aggregate demand. Furthermore, the decline in nominal interest rates in a crisis are very pronounced (right panel), reflecting the central bank’s response to increases in credit spreads. Such a large decline in nominal interest rates, however, may not be possible in some countries in a low-interest rate environment, rendering the feasibility of this monetary policy rule somewhat doubtful. 

## **3 Data and Methodology** 

### **3.1 Data** 

House price data are collected for 22 major advanced economies and 10 emerging market economies. An effort was made to maintain regional balance by collecting quarterly data from North America (Canada, Mexico and U.S.), South America (Brazil, Chile, and Colombia), Europe (16 countries including Austria, Belgium, France, Germany, Ireland, Italy, Netherlands, four Nordic countries, Spain, Switzerland, U.K. plus Russia and Turkey), Asia-Pacific (Australia, China, Hong Kong SAR, Japan, Malaysia, New Zealand and Singapore), and Africa (South Africa is the only African country in the sample). Data typically go back to 1990:Q1 in advanced economies. In emerging market economies, data series generally start later, but efforts were made to combine different sources to expand the house price series towards the early 1990s. Various data sources were consulted, including the Bank for International Settlements, national statistical offices, the Organization for Economic Co-operation and Development, and the IMF. House price data were deflated using the overall CPI index when nominal house prices 

16 

were retrieved (see Appendix A.2) for details on data coverage, transformations and summary statistics). 

**3a. AEs: Annual Change in Real House Prices** (Percent) 



<!-- Start of picture text -->
50<br>10th -90th percentile 25th -75th percentile Median<br>40<br>30<br>20<br>10<br>0<br>-10<br>-20<br>-30<br>1971 1974 1977 1980 1983 1986 1989 1992 1995 1998 2001 2004 2007 2010 2013 2016<br><!-- End of picture text -->



<!-- Start of picture text -->
3b. EMs: Annual Change in Real House Prices<br>(Percent)<br>50<br>10th -90th percentile 25th -75th percentile Median<br>40<br>30<br>20<br>10<br>0<br>-10<br>-20<br>-30<br>1995 1997 1999 2001 2003 2005 2007 2009 2011 2013 2015 2017<br><!-- End of picture text -->

###### **3c. AEs: Frequency Distribution of Real House Price Growth** (Relative frequency of annualilzed real house price growth) 



<!-- Start of picture text -->
0.30 One-year change<br>Three-year change<br>0.25<br>0.20<br>0.15<br>0.10<br>0.05<br>0.00<br>-20 -18 -15 -13 -10 -8 -5 -3 0 3 5 8 10 13 15 18 20<br><!-- End of picture text -->

###### **3d. EMs: Frequency Distribution of Real House Price Growth** (Relative frequency of annualilzed real house price growth) 



<!-- Start of picture text -->
0.30<br>One-year change<br>Three-year change<br>0.25<br>0.20<br>0.15<br>0.10<br>0.05<br>0.00<br>-20 -18 -15 -13 -10 -8 -5 -3 0 3 5 8 10 13 15 18 20 23<br><!-- End of picture text -->

**Figure 3: Historical Developments in Real House Prices.** This figure show developments in house prices in house prices across 22 major advanced economies and 10 emerging market economies. Panels 1 and 2 show the distribution of four-quarter real house price changes (median, interquartile and 10th–90th percentile range) for advanced and emerging market economies. Nominal house prices are adjusted for inflation using the consumer price index. AEs = advanced economies; EMs = emerging market economies. 

House prices tend to co-move during crises, with some countries appearing more cyclical than others (Figure 3a and Figure 3b). For example, during the early 1990s, some advanced economy countries suffered steep declines in real house prices of up to 20 percent, while others maintained a stable growth rate. During the European sovereign debt crisis in 2011-2012, similar differences were apparent; although during the global financial crisis of 2008-2009, most advanced economies saw a fall in house prices. 

In emerging market economies, three episodes of large declines stand out: the Asian crisis 

17 

in the late 1990s, the global financial crisis of 2008-2009, and the turmoil in Russia and Brazil in 2015-2016. Historically, the average (annualized) one-year and three-year growth rates of real house prices stood at about 2 percent a year in advanced economies and 2.6 percent a year in emerging market economies (Figure 3c and Figure 3d). Negative real growth in house prices occurs in about half of the observations in advanced economies and in a third of the observations in emerging market economies over a one-year horizon. 

Variables related to fundamental house price valuations and vulnerabilities are also informative about downside risks to housing. As described in the previous section, the theoretical framework can relate house price risks to household leverage, financial conditions, price-toGDP, and real GDP growth. Financial conditions are proxied by a composite index based on a principal component analysis of 11 macrofinancial variables.<sup>6</sup> 

The financial conditions index (FCI) captures the price of risk, and a larger value of the index indicates tighter financial conditions. A simple look at the univariate relationship between these fundamental house price valuation variables and the house price distribution quantiles confirms the prediction. The association between these variables and house price growth further varies with different parts of the house price distribution (Figure 4). 

Tighter financial conditions are associated with lower house prices in the future, where the effect is most pronounced when house price growth is most negative, that is, in the left tail (5th percentile) of the distribution (Figure 4a). Real GDP growth, used as a proxy for changes in households’ real income, is generally associated with lower house price growth (Figure 4b). The credit-to-GDP ratio, capturing movements in leverage of economic agents, also displays a negative relationship with house price growth when the ratio is above its long-term mean (Figure 4c). Finally, the price-to-GDP per capita ratio is a valuation metric for housing, capturing the 

> 6The indicator is constructed by the IMF as described in Internet Appendix 1.1 of GFSR 2018. The variables used to construct the index include real short-term rate, interbank spread, term spread, sovereign local debt spread, sovereign dollar debt spread, corporate local currency spread, corporate dollar debt spread, equity prices, equity price volatility, exchange rate and real house prices. An increase in the FCI represents a tightening of the pricing of risk in the economy. To mitigate endogeneity concerns, the financial conditions index (FCI) is statistically purged from variation due to house prices growth by regressing the index on quarterly changes in real house prices while controlling for countryfixed effects. We refer to the residuals from the regression as “FCI purged” and use it in the empirical analysis. 

18 

degree of deviation from fundamental valuation levels. 

###### **4b. Real GDP Growth** 







###### **4d. Price-to-GDP per Capita Ratio** 



**Figure 4: Determinants of Real House Prices.** This figure shows the univariate relationship between these fundamental house price valuation variables and quantiles of the house prices distribution confirms the prediction Panels 1–4, respectively, depict the association between one-year-ahead real house price growth and current financial conditions, real GDP growth, the detrended credit-to-GDP ratio, and the detrended price-to-GDP ratio. For detrending, a linear method was used, but robustness checks with different detrending methods produced very similar results. Lines show the estimated relationship between these variables and real house prices at the 5th(red line), 50th (yellow line), and 95th (green line) quantiles. _t_ = currrent quarter; _t_ + 4 = one year (four quarters) ahead. FCI purged corresponds to a financial conditions index statistically purged from variation due to house price growth. 

Overall, the differences in slopes indicate a markedly stronger relationship for the left tail of the future house prices growth distribution relative to the median and the 95th percentile of the distribution (Figure 4d). 

19 

### **3.2 Modeling House-Prices-at-Risk** 

HaR is defined as a measure of downside risk for the growth of real house prices over a given horizon at a 5 percent probability, corresponding to the fifth percentile of the distribution. Although our approach can be applied to any distribution percentile, we limit our attention to the fifth percentile in the baseline model. This captures the most negative real house price growth realizations in line with the paper’s focus on downside risks and financial stability. 

Importantly, by focusing on different horizons, the estimated coefficients for a given factor in the HaR model establish a term structure of house price risks, reflecting short-term versus long-term responses of HaR to that factor. While the estimation uses panel data to increase statistical power, separate panels are run for advanced and emerging market economies to maintain some homogeneity in the structure of the financial system and real economy. Panel quantile regressions allow us to formally characterize the conditional relationship between future house price growth and a set of key determinants across countries. The estimation is done using a two-step procedure for panel quantile regressions, following Canay (2011). 

_First step._ The first step estimates unobserved fixed effects using within-estimators. We denote ∆ _hYi,t_ + _h_ the average log change in real house prices, h periods ahead, for country _i_ and _Xi,t_ a vector of key determinants, including past log changes in real house prices: 



where ∆ _hYi,t_ + _h,τ_ is the conditional distribution for adjusted log annualized changes in real house prices (for simplicity referred to as house prices changes henceforth), _h_ periods ahead, for country _i_ , at a specific quantile _τ_ , estimated to depend on a vector of key determinants ( _X_ ). The vector _X_ includes past changes in real house prices, GDP growth, a credit boom indicator, FCI, and an overvaluation variable (“house price misalignment”). Credit booms are defined as periods during which the credit-to-GDP ratio is above a long-term trend.<sup>7</sup> To ensure greater 

> 7Specifically, we first estimate the deviation of credit-to-GDP from an HP trend with a smoothing parameter of 1600. The credit boom indicator is equal to one when the cyclical component is greater than zero. 

20 

coverage, the overvaluation variable used in our baseline model is an easily constructed valuation metric capturing the degree of deviation from fundamental valuation levels. The indicator corresponds to the deviation of price-to-GDP per capita ratios from an estimated linear trend.<sup>8</sup> The parameter _βh,τ_ is the (vector of) estimated coefficient(s), and _e_ denotes the quantile regression error term. The estimated fixed effects from Equation (10) can then be simply eliminated as follows 



_Second step._ We estimate a quantile regression for each quantile _τ_ and time horizon h. Formally, in a quantile regression of ∆ _hY_<sup>ˆ</sup> _i,t_ + _h,τ_ on _Xi,t_ , the regression slope _βh,τ_ is chosen to minimize the quantile weighted absolute value of errors: 



where _ρ_ (<sup>.</sup> ) denotes the indicator function, _n_ the number of cross-sections and _T_ the number _n_ of observations. The notation E _nT_ is used as short for E _nT ≡_ ( _nT_ )<sup>_−_1 �</sup><sup>_T_</sup> _t_ =1 � _i_ =1<sup>(■).The</sup> predicted value from the previous regression is the quantile of ∆ _hY_<sup>ˆ</sup> _i,t_ + _h,τ_ conditional on _Xt_ : 



Canay (2011) shows that _Qi,t_ +ˆ _h|xi,t_ is a consistent linear estimator of the quantile function _Yi,t_ + _h_ , under independence restrictions. Standard errors for this estimator can also easily be computed from the asymptotically normal representation.<sup>9</sup> 

> 8As discussed in the following sections, we test the sensitivity of the HaR model against a specific definition of credit boom and house price misalignment adopted in the baseline specifications. Overall, the findings from these robustness tests are quantitatively similar and qualitatively unchanged from our baseline specification (See Appendix A). 

> 9To account for remaining heteroskedasticity, we adopted in our analysis pairs-bootstrap when computing the standard errors of the quantile regression estimates. Alternatively, bootstrap cross- sectional or cross-sectional & temporal resampling can be used. Results from these estimations provide however very similar results and are available upon request to the authors. 

21 

HaR can be defined as the value at risk of future house prices growth as: 



where _HaRit,,h_ ( _τ |Xt_ ) is the house price at risk for country _i_ in _h_ quarters in the future at a probability _τ_ . By varying _h_ , we estimate the term structure and intertemporal properties of HaR. For a given house price determinant, _X_ , and a given quantile of the future house price distribution, _τ_ , the sequence of _βτ_ coefficients estimated at different horizons, _h_ , shows how an increase in _X_ changes the _τ_<sup>_th_</sup> quantile of future house price growth at those forecasting horizons, thus providing a “term structure” of HaR. 

## **4 Empirical Results** 

### **4.1 Baseline Estimations** 

HaR appear to broadly respond to past price dynamics and fundamental factors. The estimation includes past growth in house prices, which captures momentum effects, and the four factors described in Section 3. Lagged house prices are especially relevant because they may reflect the persistence in house price cycles as well as the role of persistent variables, such as supply restrictions. Other, more structural variables that are considered in the literature, such as population growth and urbanization, cannot be included because of limited data availability. However, their effect can be partially absorbed using fixed effects, especially if they are slowmoving in nature. The results are as follows (see Figure 5 and Table A.1): 

- _Financial conditions:_ A one-standard-deviation tightening of financial conditions, reflecting a higher underlying price of risk for the economy, is associated with 0.3 to 0.7 percentage point higher downside risk to house prices in the short term (with a stronger impact in emerging market economies).<sup>10</sup> Over longer horizons, the impact diminishes to 0.1 

> 10In comparison, the global financial crisis entailed a 2.3 standard deviation shock to financial conditions in advanced economies (1.4 standard deviations in emerging market economies). The GDP growth 

22 

percentage point in advanced economies and becomes insignificant for emerging market economies. Hence, the relationship between financial conditions and HaR is strongest in the short term and diminishes over time. However, if measures of house price overvaluation are excluded, the medium-term association between financial conditions and HaR becomes positive, which suggests that the channel through which easy financial conditions today impact downside risks to house prices in the future is through an overvaluation in current prices. 

- _Real GDP growth:_ A one-standard-deviation higher real GDP growth does not significantly reduce downside risks to house prices one to three quarters ahead in advanced economies but appears to have the opposite and significant relationship over longer horizons. In emerging market economies, the association between GDP growth and downside risks to house prices is positive but not statistically significant. 

- _Overvaluation (house price misalignment)_ : An increase in the ratio of house pricestoGDP-per capita above its historical trend —also a proxy for affordability—appears consistently and significantly related to higher downside risks to house prices over time. A one-standard deviation higher price misalignment ratio is linked to a 0.5 to 1.0 percentage point increase in downside risks to house prices in advanced economies and a 0.7 to 1.1 percentage point increase in emerging market economies. 

- _Credit booms:_ Our results show that credit booms tend to be related to a worsening of the house-prices-at-risk measure by up to 0.5 percentage points at short horizons in advanced economies (three quarters ahead) and up to 1.1 percentage point at mediumterm horizons (up to eight quarters ahead) in emerging market economies. The fact that credit booms have an immediate effect on house price risk is likely due to the definition of the boom variable, which signals overstretched household balance sheets instantaneously, rather than gradually building up. 

shock was 2.2 standard deviations in advanced economies and 1.7 standard deviations in emerging market economies, and the overvaluation shock was about 0.2 standard deviation across both groups. 

23 

The impact of fundamental factors is generally more pronounced in the left tail than at the median of the house price distribution (see Table A.2). For example, the strongest effect of tightening financial conditions is on the tail risk of house prices in both advanced and emerging market economies. In advanced economies, higher real GDP growth is more strongly correlated with downside risks to house prices than median house prices. In emerging market economies, on the other hand, higher GDP growth is correlated with lower downside risks to house prices, albeit not significantly. 





**Figure 5: Fundamental Factors on House Price Growth.** The figure shows the estimated panel quantile coefficients for four standardized variables in panel quantile regressions with real house price growth, estimated at the 5th percentile, over different horizons (1 to 16 quarters ahead). The regressions are performed separately for the sample of advanced economies (panel a) and emerging market economies (panel b). Black markers indicate insignificant coefficients, while colored circles denote significant coefficients at the 10 percent level or lower. All coefficients (except the credit boom dummy) are standardized. The full estimation results are reported in Table A.1. AEs = advanced economies; FCI = financial conditions index; EMs = emerging market economies 

Finally, shocks to the ratio of house prices-to-per capita GDP and credit booms are more strongly related to downside house prices than to median house prices in both advanced and emerging market economies. 

The model also captures the relative contribution of the different factors to HaR. This can best be illustrated through concrete examples, such as the one-year-ahead HaR fluctuations for 

24 

the United States and China, which are the largest advanced and emerging market economies, respectively (Figure 6). 

**6a. United States: One-Year HaR Decomposition** (Percentage points, 5th percentile) 



**6b. China: One-Year HaR Decomposition** (Percentage points, 5th percentile) 



**Figure 6: Factors Affecting House-Prices-at-Risk in the United States and China** . The Figure shows the decomposition of the estimated one-year-ahead annualized HaR at the 5th percentile into contributions of past house prices, financial conditions, real GDP growth, house price misalignment, and credit boom. The (negative) constant term is not shown. Panel a shows the decomposition for the United States and panel b the decomposition for China. 

25 

In the United States, HaR gradually deteriorated beginning in the early 2000s, leading up to the global financial crisis (Figure 6a). This pattern was initially related to house price overvaluation. Over time, past house price movements and credit also started to have a negative effect, partially offset by relatively loose financial conditions. Once the global financial crisis set in, the tightening of financial conditions weighed negatively on HaR. Since late 2016, HaR appear to have deteriorated gradually due to overvaluation concerns and high credit growth, but they have been partly offset by still-easy financial conditions and past house price momentum. 

In China, HaR seem more volatile, partly following the volatility in overall house price growth (Figure 6b). Easy financial conditions kept house price risks contained until 2010. After 2010, high credit-to-GDP gaps and tightening of financial conditions contributed to increased downside risks. Since 2016, house price overvaluation has also contributed to the deterioration of house-prices-at-risk. 

#### **4.1.1 Out-of-Sample Evidence** 

The HaR model can be extended to analyze real-time data for forecasting and surveillance. A model that only forecasts well within the data sample used to estimate it may not be able to predict future realizations in an out-of-sample manner. However, the latter is crucial for generating forecasts and warnings ahead of time, allowing policymakers and market participants to prepare a timely response. To this end, we perform out-of-sample tests. 

Using the United States as a case study, we first compare the predicted HaR using the entire sample period with estimates computed recursively. A recursive estimation of HaR implies that the forecast of the 5th percentile of the house price growth distribution at time _t+h_ is constructed using only information from the estimation sample observable up to time _t_ . In particular, all parameters and fitted values are estimated using data ending no later than time _t_ . The earliest out-of-sample start dates are 2006 to allow for enough observations in a given sample. 

26 



**Figure 7: Comparison of In-Sample and Out-of-Sample Predictions** . The figure shows the comparison of in-sample (blue line) and and out-of-sample (red line) predictions for the United States based on the baseline HaR model for selected forecasting horizons (h=1,4,8,12). Out-of sample estimation starts at are 2006 to allow for enough observations in the sample. IS=In-Sample; OS=Out-of-Sample. 

Figure 7 shows the results estimated at specific forecasting horizons, i.e., h=1,4,8,12. We find that out-of-sample projections of the left tail of future house price growth (red line) track well the in-sample predictions using the full sample period (blue line). In fact, the difference between the predictions calculated in “real-time” and computed from the full data sample is in general very small. This suggests that the model can forecast house price vulnerabilities in real-time, despite well-documented structural changes in financing structures over time. 

Second, we evaluate more formally out-of-sample accuracy. Quantitatively, the out-ofsample forecast accuracy of HaR can be evaluated using a quantile _R_<sup>2</sup> based on the quantile loss function _ρτ_ : 

27 



The quantile _Ri_<sup>2capturesthelossusingtheconditionaldistributionrelativetotheloss</sup> using the historical unconditional quantile estimates. The higher the value, the larger the improvement of the prediction by the model over a simple summary of historical data for a given country _i_ . In principle, the quantile _R_<sup>2</sup> could also be negative if the unconditional quantile offers a better forecast than the conditioning set of variables in the proposed baseline model. In addition, we evaluate the statistical significance of the quantile _R_<sup>2</sup> by comparing the sequences of quantile forecasts losses based on the forecasting model (the numerator) to the quantile loss based on the historical unconditional quantile (the denominator), following Diebold and Mariano (2002).<sup>11</sup> 

Table A.3 reports the quantile _R_<sup>2</sup> and the corresponding t-statistic for the United States using panel quantile forecasts of the 5th percentile at selected horizons, i.e., h=1,4,8,12. To provide additional insights on the robustness of the estimation, the table also reports the accuracy measure using a country-level model for the United States. Note that country-level quantile regressions simply correspond to the second step of the estimator described in Section 3, without the adjustment for fixed effects. Hence, equation (15 is recalculated using _αt,usa_ ˆ and _βt,usa_ ˆ specific for the United States. Overall, we find that HaR have significant out-ofsample predictive power for the 5th percentile of future house price growth using both panel and country-level quantile regression.<sup>12</sup> 

> 11An alternative method to evaluate the forecasting accuracy in a quantile setting is computing the empirical cumulative distribution of the probability transform (PIT) of the data with respect to the density forecast model. Results from this analysis are reported in the Appendix A.5. 

> 12It is worth noting that some differences in the level of quantile between panel- and country-level estimations are present for the United States case study. While the accuracy of panel-based estimates is (relatively) more precise within the first four quarters of the forecasting horizon, long-term projections based on a country-level model outperform short-term forecasts. Note also that, as expected, differences in the level of the accuracy metric of the panel quantile model are generally lower in cross-sectional data than in time series data due to the heterogeneity of cross-sections. 

28 

#### **4.1.2 Additional Robustness tests** 

In addition to the out-of-sample analysis, we run a series of additional robustness tests. First, we compare our baseline results with those from alternative panel quantile models. We test in particular the robustness of the results using the panel quantile estimation approach based on Powell (2022) as well as the methodology based on Machado and Silva (2019). Powell (2022) proposes a method consistent for small _T_ which permits nonadditive fixed effects while maintaining the nonseparable disturbance term commonly associated with quantile estimation. This avoids the need to estimate fixed effects, which could lead to biased projections in small samples. Similarly, Machado and Silva (2019) allow the individual fixed effects to affect the entire distribution and, in addition, with the inclusion of jackknife bias correction, it allows reasonably reliable inference to be performed for moderate values of _T_ . Tables A.15 and A.16 in the Appendix A.4 show the coefficients from the alternative panel quantile estimators. 

Second, we test our baseline model against the inclusion of episodes characterized by simultaneous declines in house prices across countries. In principle, sharp declines in house prices for many economies during a single event such as the financial crisis in 2008 could affect house prices-at-risk estimations due to the risk of overfitting. We test this possibility by dropping from the sample the years of the peaks of the financial crisis (2008 to 2009). Results from these regressions are reported in Table A.17. 

Third, we compare the estimations using the panel quantile estimator described in Section 3 with those from a country-level estimated model for the United States. Figure 8 report the results using from the full data sample. Country-level estimation have in general the benefit of allowing for a closer fitting the parameter estimates of the house price at risk estimator to country specific data sample. Despite this greater flexibility, predictions based on our panel quantile estimator remain very close to the country-level estimates, especially in the medium term. Note also that downside risks projected through our baseline (panel-based) model tend to anticipate episodes of large house price declines (e.g., during the GFC) at shorter prediction time horizons, which could be particular helpful from a prudential perspective. 

29 



**Figure 8: United States: Comparison of Panel- and Country-Level House-Prices-at-Risk** . The Figure shows the comparison of HaR predictions based on the baseline panel model (blue line) and the estimates from a model using only country-level data for the United States (red line) at selected = time horizons (h 1,4,8,12). Dashed lines refer to the realized house price growth h-quarters ahead from time observation. 

Finally, alternative definitions of the key determinants of HaR are tested. Specifically, we test the results from the baseline model using i) an alternative definition of credit boom based on Mendoza and Terrones (2014); ii) using a financial condition index based on a time-varying parameter vector autoregression model as in Koop and Korobilis (2014)<sup>13</sup> ; iii) using HodrickPrescott (HP) filters for the construction of the house price misalignment; iv) using alternative definitions of the house prices misalignment based on price-to-rent ratios. Results from these 

13The methodology allows for dynamic interactions between the FCIs and macroeconomic conditions that can evolve over time. It also allows for differences in starting dates for some financial indicators with a flexible estimation procedure. 

30 

tests are reported in the Appendix A.4 (Tables A.18-A.21 ). 

Overall, the findings from these robustness tests are quantitatively similar and qualitatively unchanged from our baseline model.<sup>14</sup> 

### **4.2 Contribution of House-Prices-at-Risk to Macro-Financial Stability** 

Sharp declines in house prices help forecast risks to real GDP growth. Growth-at-risk measures the degree to which future GDP growth faces downside risks and its relationship with measures of financial vulnerabilities, including in the housing sector (Adrian et al., 2019). Given that large declines in house prices are associated with contractions in GDP growth and financial stability risks (see Section 2), a deterioration in HaR should help forecast downside risks to GDP growth, over and above other measures of house price imbalances that are only indirectly related to future risks. To this aim, we run the following model: 



where ∆ _hyi,t_ + _h,τ_ refers to average GDP growth and _HaRi,t,τ_<sup>_t_+</sup><sup>_h_, to the estimated house-prices-</sup> at-risk measure h quarters ahead at time t. The empirical findings confirm this hypothesis (Figure 9a and Figure 9b, and Table A.4). An increase in downside risks to house prices (a lower, more negative HaR) is associated with an increase in future downside risk to GDP growth, i.e growth-at-risk (GaR). Furthermore, the association with downside risks is stronger than with median growth (Table A.5), consistent with studies on booms and busts in house prices and recessions (Claessens et al., 2012). 

The largest impact of HaR is four quarters ahead, with a 1 percent deterioration (i.e. more negative) in the house-prices-at-risk measure preceding, on average, a 0.4 percentage point 

> 14In unreported results, we also estimate HaR projections extending data up to the end of 2019. One year-ahead HaR projections at the onset of the COVID-19 pandemic are much lower relative to previous crisis periods, which is in line with the resilience manifested by housing markets during the pandemic. Results from this analysis are available upon request. 

31 

decline in growth at risk for advanced economies and 0.5 percentage points in emerging market economies. This association is robust to adding various credit quantity measures to the GaR model, indicating that the overall effect of HaR is not simply capturing the correlation of growth at risk with credit. The results are also robust when adding other measures of house price imbalances, such as the growth in house prices or overvaluation metrics. Thus, the houseprices-at-risk measure serves as a leading indicator for financial stability risks as captured by the GaR model. 

HaR also help predict episodes of financial crisis. Another way of evaluating the usefulness of the measure for financial stability surveillance is to study whether a more adverse level of HaR helps predict the occurrence of financial crises.<sup>15</sup> We test this by estimating the probability of financial crises with a fixed effects logit model. Formally, the crisis’s probability can be expressed as a non-linear function of a given set of explanatory variables: 



where _Yi,t_ + _h_ is a forward-looking crisis variable equal to 1 if economy _i_ is experiencing a financial crisis _h_ quarters ahead; Λ _X ′β_ denotes the CDF of the logistic distribution. � � Condition (17) defines the conditional probability that the economy _i_ experiences a systemic banking crisis at time _t_ as a function of selected indicators denoted _Xt_ . 

The analysis shows that adding HaR to standard statistical models for crisis prediction that relate the probability of a crisis to GDP growth, financial conditions, and the credit-toGDP gap helps improve the accuracy of the models. This occurs across all horizons (one, two, and three years) and for both advanced and emerging market economies. According to the estimates, an annual HaR of _−_ 16 percent—that is, an estimated 5 percent probability of a 12 percent decline in real house prices one year ahead—implies a 34 percent probability of a financial crisis one year ahead in advanced economies and a 25 percent probability in emerging 

> 15Financial crises correspond to systemic banking crises, as identified by Laeven and Valencia (2018) Crises are rare and need to be identified carefully through qualitative and quantitative criteria. The growth-at-risk framework, as used in Adrian et al. (2019), provides an alternative approach. 

32 

market economies (Figure 9c and Figure 9d, and Table A.6).<sup>16</sup> 

**9a. AEs: Regression Coefficient of HaR in GaR Model** (Percentage points, one to sixteen quarters ahead) 

**9b. EMs: Regression Coefficient of HaR in GaR Model** 

(Percentage points, one to sixteen quarters ahead) 





**9c. AEs: Marginal Probability of HaR in Financial Crisis Model** (Estimates for given house price at risk, one-year-ahead annualized growth rate) 

**9d. EMs: Marginal Probability of HaR in Financial Crisis Model** (Estimates for given house price at risk, one-year-ahead annualized growth rate) 





**Figure 9: House-Prices-at-Risk and Financial Stability.** Panels a and b depict a positive and significant association between GaR and HaR, at the 5th quantile and at the median over different projection horizons. Panels c and d show marginal probabilities of real house price declines (HaR) at given values on the occurrence of a financial (banking) crisis from a model with country fixed-effects, output growth, the financial conditions index, credit-to-GDP gap, and HaR. The panels show estimated coefficients with their 90 (68) confidence interval. AEs = advanced economies; EMs = emerging market economies; GaR = growth-at-risk. 

16An alternative test to check the relationship between HaR and systemic banking crises is to compare crisis predictability power using the Area Under Curve (AUC) metric. The results from this analysis are available upon request to the authors. 

33 

The results are in line with Claessens et al. (2012) showing that recessions are deeper and last longer when house prices fall more and more quickly, and more than two-thirds of the nearly 50 systemic banking crises in recent decades were preceded by boom-bust patterns in house prices. Moreover, certain housing market characteristics, such as higher loan-to-value ratios and greater reliance on wholesale markets, are associated with even higher risks of crises. These findings align with our theoretical framework, which suggests that interactions between house prices and credit volumes may result in self-reinforcing feedback loops where an increase in house prices facilitates an expansion in credit (through collateral effects) places further upward pressure on house prices. When that process is reversed, large house price declines may be followed by a collapse in credit and GDP growth, leading to a larger probability of financial crisis. 

### **4.3 Policies to Mitigate Downside Risks to House Prices** 

Finally, we explore the relationship between policies and HaR. We examine whether tighter macroprudential or monetary policy shifts the whole term structure of HaR. To this aim, we expand our baseline model, equation (10, as follows: 



where _Mi,t_ is the proxy for policy measures and _Xi,t_ denotes all other variables. In the specification, we also control for the interaction of _Mi,t_ with FCI. Two coefficients are especially relevant in this forecasting equation: _βh,τ_ and _λh,τ_ . The first one represents the marginal effects of policy tightening, itself while the second one represents the policy effects conditional on other variables _Xi,t_ , that is, how much the policy measure mitigates the marginal effects of _Xi,t_ on HaR over a specific horizon, as well as over time. This study can also usefully illustrate the different effects of, macroprudential and monetary policies at various points in the future while being mindful of the risks of overfitting. Below we provide details on the construction of the policy measures used in the analysis. 

34 

**Macroprudential Policy Measures.** We construct our measure of macroprudential policy using the IMF’s Integrated Macroprudential Policy (iMaPP) database. The database contains comprehensive information on the dates of tightening and loosening for a range of macroprudential policy measures across countries (Alam et al., 2019). We consider two main policy interventions targeted at the housing market. The first, are caps on loan-to-value (LTV) ratio for mortgage loans, which restricts the amount of the loan to a certain fraction of the total value of the property. More than half of the countries in our sample have used LTV caps to limit mortgage lending since 2000, making LTVs the most commonly used macroprudential tool in our sample. The second set of policy interventions correspond to debt-to-income ratio (DTI), that is limits to the value of the borrower’s debt relative to monthly income often employed together with LTVs (Kuttner and Shim, 2016). 

While we typically know the month of implementation for each macroprudential action taken, we aggregate the tools to a quarterly frequency to match the frequency of house price growth in our sample. If no action was announced in a given quarter, the value of the variable is set to zero. If multiple policy measures were used in the same quarter, we sum all changes over the same period. Each policy tightening (equal to +1) increases the measures’ unit scores and policy loosening (equal to -1) lowers the score. Hence, the policy indicator (PM) can take value in the range _{_ -2,-1,0,1,2,3 _}_ in a given quarter if all in net terms, there were more than one loosening actions, one loosening action, no change, one tightening action, two tightening actions or more in the same quarter, respectively. 

It is important to note that in certain countries such as Korea and Hong Kong SAR, LTV caps have been implemented in a targeted manner, with varying caps imposed on different borrowers based on factors such as the location of the property, whether it is their first or second home and the property’s price. Consequently, it can be challenging to ascertain the overall LTV cap for a country and comparing caps across countries can be even more difficult. Although macroprudential regulations establish binding constraints on both borrowers and lenders, the effect of such measures may take some time before becoming apparent. 

For this reason, to assess the relationship between macroprudential policy measures and 

35 

house-prices-at-risk, we first focus on the intensity of macroprudential policies instead of the quarterly changes of the policy variables. The intensity policy measure is constructed as a rolling sum of the policy indicator described above within a four-year time window from time _t_ . This allows us to capture the combined effect of multiple macroprudential measures that could bind only several quarters after being imposed. Formally: 



where _PMi,t_ corresponds to the quarterly policy indicator composed of LTV and DSTI quarterly changes. 

A common concern in the evaluation of the impact of macroprudential policies is the potential for endogeneity, whereby countries with high levels of risk due to rapid increases in housing prices and credit growth are more likely to implement such policies. This endogeneity may increase the correlation between the use of macroprudential measures and HaR, ultimately biasing the coefficient estimates. 

In order to mitigate the issue of confounding effects on macroprudential measures, we employ three approaches. Firstly, we include among the control variables ( _Xi,t_ ) of the baseline model described in equation (18) an interaction term between the financial condition index and the macroprudential policy measure. Secondly, we re-examine the analysis using macroprudential policy shocks that take into account ex-ante credit conditions, house price trends, and lag values of the policy measure, as opposed to relying solely on _MPMi,t_ . To derive such shocks, we estimate an ordered Probit regression model as follows: 



where credit gap is the credit-to-GDP gap, and _λ_ 0 _,i_ are country fixed effects. For both credit and house prices, the gap measure is the deviation from the trend, using Hodrick and Prescott 

36 

filter.<sup>17</sup> The term<sup>�4</sup> _j_ =1<sup>_I_</sup> _i,t_<sup>_MPM_</sup> _−M −j_<sup>,controlsforfourlagsofthemacroprudentialpolicymeasure</sup> = before the time window in which policy measures are cumulated (i.e., M 16). The policy shock, _LMPMi,t,_ is then recovered as the difference between the actual value of the macroprudential indicator and its estimated conditional expectation: 



ˆ where _Et−_ 1 [ _MPMi,t_ ] is the sample analogue of the expected policy indicator, condition on the ˆ quarter t-1 information, and _pk_ ( _xi,t−_ 1) _k_ is the estimated probability of _MPMi,t_ = k, with _k ∈_ [ _−_ 4 _,_ 8], conditional on the right-hand side variables ( _xi,t−_ 1) of equation (20). 

Finally, we construct an alternative version of the macroprudential policy shocks based on instantaneous policy changes ( _PMi,t_ ), i.e. using only policy changes occurred in quarter _t_ , as dependent variable in equation (20).<sup>18</sup> This last approach, allows us in turn also to compare the effect of the orthogonalized instantaneous policy changes ( _LPMi,t_ ) to the effect estimated with the orthogonalized intensity policy measure ( _LMPMi,t_ ) which captures the effect of policy measures introduced over multiple quarters before time _t_ . 

**Monetary Policy** . As a second policy measure we use an indicator of monetary policy. Distinguishing the role of monetary policy and financial conditions on house prices is intricate since the latter serves as a crucial conduit for implementing monetary policy. Thus, we center our investigation on unexpected fluctuations in conventional monetary policy, which we define as unanticipated deviations of the short-term rate from an augmented Taylor rule. To account for multiple countries in our analysis, we employ a straightforward methodology to compute 

> 17Results of the analysis do not change using alternative detrending methods such as the approach proposed in Hamilton (2018). 

> 18In this case, lags of the policy measure used in equation (20), correspond to four lags of the measure from the time of implementation of the policy measure t, i.e.,<sup>�1</sup> _j_ =4<sup>_PMi,t−j_.</sup> 

37 

monetary policy shocks. Specifically, we employ a regression model that controls for a set of variables and utilize the residual values as the identified monetary policy shocks. 



The set of controls, _Zi,t_ , includes contemporaneous and lagged values of inflation, log GDP, corporate spreads, log foreign GDP,<sup>19</sup> as well as lagged values of short-term rate and quadratic time trend. The formulation is similar to a Cholesky identification in a vector autoregression (VAR) studies that order the short-term rate last, such as Bernanke et al. (2005). 

An important advantage of this identification strategy is its ability to generate monetary policy shocks for a sizable cohort of countries while imposing less stringent data constraints. However, concerns regarding endogeneity bias may persist even with the inclusion of control variables. We validate therefore the findings of our analysis using monetary policy shocks constructed with two alternative empirical methodologies that incorporate high-frequency identification techniques to address residual endogeneity concerns. 

The first alternative approach is based on Nakamura and Steinsson (2018). The authors propose a model in which monetary policy announcements convey information about both future monetary policy and economic fundamentals; this information, in turn, affects investors’ beliefs about the natural real rate. Policy shocks are constructed based on movements in bond prices in a narrow window around scheduled Federal Open Market Committee (FOMC) meetings. The key intuition is to exploit the fact that a disproportionate amount of monetary news is revealed at the time of the FOMC meetings. The uneven way monetary news is revealed allows, in turn, for a discontinuity-based identification scheme. As the authors’ analysis focuses on the United States, we use policy shocks constructed with their proposed method for a country level test. 

Another alternative approach for addressing residual endogeneity concerns is proposed by Cieslak and Pang (2021), which involves constructing monetary policy shocks based on the 

> 19The index of foreign GDP is constructed by cumulating the average of quarter-on-quarter GDP growth for the countries in the sample. 

38 

joint dynamics of government bond yields and equity returns around central bank releases. Like Nakamura and Steinsson (2018), this approach disentangles the effect of news content of central bank communication on stock prices within a narrow time window. In addition, this alternative identification scheme exploits both the direction of the comovement between stocks and yields and the effect of news across the entire maturity dimension of the yield curve. Shocks are available from the authors for four leading central banks (the Federal Reserve Bank, the European Central Bank, the Bank of England, and the Bank of Japan) spanning the period from the late 1990s through the end of 2017. Hence, we use shocks derived from this approach in a panel setting for the jurisdictions covered by these authorities. 

#### **4.3.1 Discussion** 

We start by examining the estimated effects of macroprudential policy on HaR. Figures 1011 depict the estimated changes in the 5th percentile of the house price growth after a one standard deviation tightening of each policy measure, i.e. _βh,τ_ in equation (18), together with the respective confidence intervals. 

The empirical results show that macroprudential policy measures have a direct effect where tightening these measures reduces HaR—consistent with macroprudential policy measures leading to the accumulation of buffers, so that HaR is lower for any combination of factors. Especially a tightening of borrower-based macroprudential policy measures, caps on loan-to-value and debt-service-to-income ratios, affects HaR and shift the entire term structure of HaR upward (Figure 10, panels a and b, and Table A.7). 

In advanced economies, one standard deviation increase in the macroprundetial policy intensity measure (corresponding to 1.2 units) has a maximum impact 7 quarters ahead equal to 0.3 percentage points. In emerging market economies, the impact is the highest in the longer term, and remains steady after 12 quarters.<sup>20</sup> Specifically, a one-unit tightening of macroprudential measures could lower the three-years-ahead annualized average HaR by 0.2 in 

> 20According to Choi et al. (2018), tightening nine macroprudential policies on annual house prices from a broad set of countries appeared to take two years to have the intended effect, and in the first year after implementation real housing prices rose instead of falling. 

39 

emerging market economies (about 50 percent of the median HaR value). 

**10a. AEs: Effect of Macroprudential Policy on HaR Using Intensity Measure** (Percentage Points) 

**10b. EMs: Effect of Macroprudential Policy on HaR Using Intensity Measure** (Percentage Points) 



**10c. AEs: Effect of Macroprudential Policy on HaR Using Orthogonalized Intensity Measure** (Percentage Points) 



**10e. AEs: Effect of Macroprudential Policy on HaR Using Orthogonalized Instantaneous Measure** (Percentage Points) 



**10d. EMs: Effect of Macroprudential Policy on HaR Using Orthogonalized Intensity Measure** (Percentage Points) 



**10f. AEs: Effect of Macroprudential Policy on HaR Using Orthogonalized Instantaneous Measure** (Percentage Points) 





**Figure 10: Effects of Macroprudential Policy on House-Prices-at-Risk.** Panels show the coefficients of different macroprudential policies on HaR. In Panels a and b, the macroprudential policy variable is based on a three-year rolling window of debt-service-to-income and loan-to-value measures (MPM). In Panels c and d, macroprudential policy shocks are constructed by orthogonalizing MPM from ex-ante credit conditions, house price developments, and lag values of the policy measure. Panels e and f, results from the same approach as in the previous panels, but using instantaneous changes of the policy measures (PM). The panels show estimated coefficients with their 90 (68) confidence interval. 

The findings demonstrate the robustness of the results obtained from employing alternative 

40 

measures of macroprudential shocks, as illustrated in Figures 10c-10f. By orthogonalizing the macroprudential intensity measure with respect to credit conditions, house price developments, and lag values of the policy measure, the estimates’ significance remains generally consistent with the baseline results (see Table A.8). Moreover, the magnitude of the coefficients remains consistent, not only when using orthogonalized intensity measures, but also when using instantaneous changes of macroprudential measures, as shown in Figures 10e-10f (Table A.9). 

Turning to monetary policy, a one standard deviation increase in monetary policy shocks contributes to a deterioration of HaR over a short horizon in advanced economies. The analysis shows that these shocks have a short-lived, negative relationship with HaR only in advanced economies (Figure 11, panels c and d, and Table A.10. The latter result might be explained by the fact that housing markets in advanced economies are more developed and integrated with capital markets than those in emerging market economies, such that changes in the short-term policy rate would directly pass through to house prices. 

Moreover, the inclusion of these monetary policy shocks weakens the short-term relationship between financial conditions and HaR, indicating that part of this relationship was associated with changes in the short-term policy rate. Thus, in general, monetary policy would influence downside risks to house prices mainly through its impact on financial conditions and have a more limited direct effect on HaR relative to targeted macroprudential policies.<sup>21</sup> 

The results are broadly consistent across alternative monetary policy shock measures. Figure 11c shows the shocks’ coefficients based on Cieslak and Pang (2021). The findings point to a similar effect of monetary policy shocks in the short term as in the baseline regression, with significance spanning up to 5 quarters ahead. However, the magnitude of the shock is more limited in the reduced sub-panel of advanced economies. 

In contrast, the estimates based on the shocks sourced from Nakamura and Steinsson (2018) for the United States showed the strength of the relationship between unexpected monetary 

> 21Note that there is anecdotal evidence that capital inflows are associated with higher house prices in the short term and hence may result in more downside risks to house prices in the medium term, which might justify capital flow management measures under some conditions. Similarly, real estate taxation may affect house prices and incentives for households to increase their leverage. The exploration of the role of these measures on HaR is a topic for future research. 

41 

policy tightening and house-prices-at-risk peaks 8 quarters ahead of the shock but has, in general, lower statistical significance (Figure 11, panel d). Full estimation results are reported in Table A.11. 

**11a. AEs: Effect of Monetary Policy Shocks on HaR 11b. EMs: Effect of Monetary Policy Shocks on HaR** (Percentage Points) (Percentage Points) 





**11c. AEs (Sub-Sample): Effect of Monetary Policy 11d. United States: Effect of Monetary Policy Shocks Shocks on HaR Using Alternative Shock Definition on HaR Using Alternative Shock Definition Based on Based on Cieslak and Pang (2021)** (Percentage Points) **Nakamura and Steinsson (2018)** (Percentage Points) 





**Figure 11: Effects of Monetary Policy on House-Prices-at-Risk.** Panels show the coefficients of monetary policy measures on HaR using alternative approaches. In Panels a and b, monetary policy is captured by predicted residuals of a feedback rule. In panel c, results are based on monetary policy shocks as defined in Cieslak and Pang (2021) based on a subsample of advanced economies with available data. Panel d shows the results for the United States using shocks defined as in Nakamura and Steinsson (2018). Panels show estimated coefficients with their 90 (68) confidence interval. 

Taken together, these empirical findings confirm the prediction of the model described in Section 1, and are consistent with previous literature arguments that leaning against the wind using monetary policy can be counterproductive, while macroprudential policy should be 

42 

preferred for this purpose (Brandao-Marques et al., 2020; Svensson, 2017; Schularick and Taylor, 2012). Intuitively, tighter borrower-based macroprudential measures can make the economy less volatile, by reducing financial accelerator effects through tighter borrowing constraints, whereas the active use of monetary policy to reduce downside risks to house prices can increase the volatility of house prices and thereby result in welfare losses. The ineffectiveness of tighter monetary policy to reduce downside risks to house prices can also be understood in the context of rational bubbles. In this setting, although an interest hike could depress the fundamental component of asset prices, it would also relax the requirement that the bubble component grows at most at the real interest rate, and the effect of monetary policy on financial stability would depend on which component dominates. However, small changes in assumptions can overturn this result (Miao et al., 2019). 

## **5 Conclusion** 

This paper lays out a new methodology to predict downside risk to house prices and finds it to be a useful early-warning indicator for financial stability surveillance. Using a panel quantile regressions framework, we find that HaR—the 5 percent probability of large house price declines over a given time horizon—is determined by fundamental factors such as financial condition, price overvaluation, the presence of credit booms and past price dynamics. HaR, in turn, have a significant impact on downside risks to economic growth. 

We also shed light on the policy solutions for preventing and mitigating future shocks to house prices and financial stability. Targeted macroprudential policies appear to be the most effective in reducing HaR, consistently with a theoretical model with occasionally binding collateral constraints. In our analysis, the relationship between policy measures and HaR is especially significant for borrower-based macroprudential measures, i.e., caps on loan-to-value and debt-service-to-income ratios. Our findings imply that these measures should be added to countries’ macroprudential policy toolkits and monitored over time. 

43 

## **References** 

- Adrian, T., N. Boyarchenko, and D. Giannone (2019): “Vulnerable growth,” _American Economic Review_ , 109, 1263–89. 

- Alam, Z., M. A. Alter, J. Eiseman, M. R. Gelos, M. H. Kang, M. M. Narita, E. Nier, and N. Wang (2019): _Digging deeper–Evidence on the effects of macroprudential policies from a new database_ , International Monetary Fund. 

- Bernanke, B. S. (2012): “The effects of the great recession on central bank doctrine and practice,” _The BE Journal of Macroeconomics_ , 12. 

- Bernanke, B. S., J. Boivin, and P. Eliasz (2005): “Measuring the effects of monetary policy: a factor-augmented vector autoregressive (FAVAR) approach,” _The Quarterly journal of economics_ , 120, 387–422. 

- Bianchi, J. (2011): “Overborrowing and systemic externalities in the business cycle,” _American Economic Review_ , 101, 3400–3426. 

- Bianchi, J. and E. G. Mendoza (2018): “Optimal time-consistent macroprudential policy,” _Journal of Political Economy_ , 126, 588–634. 

- Borio, C. E. and I. Shim (2007): “What can (macro-) prudential policy do to support monetary policy?” . 

- Brandao-Marques, M. L., M. R. Gelos, M. M. Narita, and E. Nier (2020): _Leaning against the wind: A cost-benefit analysis for an integrated policy framework_ , International Monetary Fund, Working Paper No. 2020/123. 

- Canay, I. A. (2011): “A simple approach to quantile regression for panel data,” _The econometrics journal_ , 14, 368–386. 

- Cerutti, E., J. Dagher, and G. Dell’Ariccia (2017): “Housing finance and real-estate booms: A cross-country perspective,” _Journal of Housing Economics_ , 38, 1–13. 

44 

- Cesa-Bianchi, A., A. Ferrero, and A. Rebucci (2018): “International credit supply shocks,” _Journal of International Economics_ , 112, 219–237. 

- Choi, S. M., L. E. Kodres, and J. Lu (2018): _Friend or Foe? Cross-Border Linkages, Contagious Banking Crises, and “Coordinated” Macroprudential Policies_ , International Monetary Fund. 

- Cieslak, A. and H. Pang (2021): “Common shocks in stocks and bonds,” _Journal of Financial Economics_ , 142, 880–904. 

- Claessens, S., M. A. Kose, and M. E. Terrones (2012): “How do business and financial cycles interact?” _Journal of International economics_ , 87, 178–190. 

- Curdia, V. and M. Woodford (2011): “The central-bank balance sheet as an instrument of monetarypolicy,” _Journal of Monetary Economics_ , 58, 54–79. 

- Diebold, F. X. and R. S. Mariano (2002): “Comparing predictive accuracy,” _Journal of Business & economic statistics_ , 20, 134–144. 

- Duca, J. V., J. Muellbauer, and A. Murphy (2010): “Housing markets and the financial crisis of 2007–2009: lessons for the future,” _Journal of financial stability_ , 6, 203–217. 

- ——— (2021): “What drives house price cycles? International experience and policy issues,” _Journal of Economic Literature_ , 59, 773–864. 

- Favara, G. and J. Imbs (2015): “Credit supply and the price of housing,” _American Economic Review_ , 105, 958–992. 

- Giglio, S., B. Kelly, and S. Pruitt (2016): “Systemic risk and the macroeconomy: An empirical evaluation,” _Journal of Financial Economics_ , 119, 457–471. 

- Glaeser, E. L. and C. G. Nathanson (2017): “An extrapolative model of house price dynamics,” _Journal of Financial Economics_ , 126, 147–170. 

45 

- Guerrieri, L. and M. Iacoviello (2017): “Collateral constraints and macroeconomic asymmetries,” _Journal of Monetary Economics_ , 90, 28–49. 

- Hamilton, J. D. (2018): “Why You Should Never Use the Hodrick-Prescott Filter,” _The Review of Economics and Statistics_ , 100, 831–843. 

- Jordà, Ò., M. Schularick, and A. M. Taylor (2015): “Leveraged bubbles,” _Journal of Monetary Economics_ , 76, S1–S20. 

- Koop, G. and D. Korobilis (2014): “A new index of financial conditions,” _European Economic Review_ , 71, 101–116. 

- Kuttner, K. N. and I. Shim (2016): “Can non-interest rate policies stabilize housing markets? Evidence from a panel of 57 economies,” _Journal of Financial Stability_ , 26, 31–44. 

- Laeven, L. and F. Valencia (2018): _Systemic banking crises revisited_ , International Monetary Fund. 

- Machado, J. A. and J. S. Silva (2019): “Quantiles via moments,” _Journal of Econometrics_ , 213, 145–173. 

- Mendoza, E. G. and M. E. Terrones (2014): “An anatomy of credit booms and their demise,” _Series on Central Banking Analysis and Economic Policies no. 18_ . 

- Mian, A., K. Rao, and A. Sufi (2013): “Household balance sheets, consumption, and the economic slump,” _The Quarterly Journal of Economics_ , 128, 1687–1726. 

- Mian, A., A. Sufi, and E. Verner (2017): “Household debt and business cycles worldwide,” _The Quarterly Journal of Economics_ , 132, 1755–1817. 

- Miao, J., Z. Shen, and P. Wang (2019): “Monetary policy and rational asset price bubbles: Comment,” _American Economic Review_ , 109, 1969–90. 

- Nakamura, E. and J. Steinsson (2018): “High-frequency identification of monetary nonneutrality: the information effect,” _The Quarterly Journal of Economics_ , 133, 1283–1330. 

46 

- Powell, D. (2022): “Quantile regression with nonadditive fixed effects,” _Empirical Economics_ , 63, 2675–2691. 

- Richter, B., M. Schularick, and I. Shim (2019): “The costs of macroprudential policy,” _Journal of International Economics_ , 118, 263–282. 

- Richter, B., M. Schularick, and P. Wachtel (2021): “When to lean against the wind,” _Journal of Money, Credit and Banking_ , 53, 5–39. 

- Rossi, B. and T. Sekhposyan (2017): “Macroeconomic uncertainty indices for the euro area and its individual member countries,” _Empirical Economics_ , 53, 41–62. 

- Schularick, M. and A. M. Taylor (2012): “Credit booms gone bust: monetary policy, leverage cycles, and financial crises, 1870–2008,” _American Economic Review_ , 102, 1029– 1061. 

- Svensson, L. E. (2017): “Cost-benefit analysis of leaning against the wind,” _Journal of Monetary Economics_ , 90, 193–213. 

47 

## **A Appendices** 

### **A.1 Tables** 

**Table A.1: Baseline Estimations of HaR.** The tables report the estimated coefficients of the key determinants of downside risk from the baseline house price-at-risk model. The model is estimated at the 5th percentile of 1 quarter ahead average house price growth up to 16 quarters ahead. Panel quantile regressions are performed following the approach described in Section 3. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. _∗∗∗_ p<0.01, _∗∗_ p<0.05, _∗_ p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.289***|1.151***|0.908***|0.820***|0.775***|0.562***|0.414***|0.344***|0.361***|0.381***|0.391***|0.392***|0.372***|0.357***|0.324***|0.300***|
||(0.189)|(0.141)|(0.115)|(0.078)|(0.088)|(0.082)|(0.104)|(0.093)|(0.096)|(0.088)|(0.074)|(0.067)|(0.062)|(0.073)|(0.069)|(0.058)|
|GDP growth (t)|0.197*|0.069|0.052|-0.095|-0.204**|-0.227***|-0.215**|-0.156*|-0.196**|-0.141*|-0.138**|-0.140**|-0.128***|-0.145**|-0.138***|-0.114|
||(0.106)|(0.126)|(0.108)|(0.120)|(0.083)|(0.085)|(0.090)|(0.095)|(0.083)|(0.083)|(0.057)|(0.055)|(0.049)|(0.061)|(0.053)|(0.072)|
|House price misalignment (t)|-0.473**|-0.779***|-0.788***|-0.874***|-0.931***|-0.976***|-1.033***|-1.015***|-0.972***|-0.956***|-0.920***|-0.928***|-0.945***|-0.985***|-0.982***|-0.987***|
||(0.196)|(0.137)|(0.151)|(0.090)|(0.088)|(0.078)|(0.085)|(0.060)|(0.052)|(0.043)|(0.047)|(0.047)|(0.050)|(0.037)|(0.053)|(0.038)|
|Financial condition index (t)|-0.339*|-0.283**|-0.114|-0.205*|-0.220**|-0.218***|-0.233**|-0.238***|-0.196***|-0.150***|-0.164***|-0.161***|-0.119***|-0.102**|-0.135***|-0.121***|
||(0.174)|(0.126)|(0.122)|(0.115)|(0.094)|(0.061)|(0.091)|(0.060)|(0.063)|(0.050)|(0.054)|(0.050)|(0.039)|(0.040)|(0.035)|(0.043)|
|Credit boom (t)|-0.275|-0.483*|-0.543**|-0.481***|-0.321**|-0.385**|-0.409**|-0.358**|-0.344**|-0.304*|-0.241*|-0.293**|-0.260*|-0.207**|-0.216**|-0.227**|
||(0.304)|(0.250)|(0.227)|(0.171)|(0.154)|(0.176)|(0.204)|(0.151)|(0.147)|(0.184)|(0.129)|(0.140)|(0.142)|(0.094)|(0.097)|(0.092)|
|Observations|2,389|2,367|2,345|2,323|2,301|2,279|2,257|2,235|2,213|2,191|2,169|2,147|2,125|2,103|2,081|2,059|



48 

##### **Table A.1: Baseline Estimations of HaR (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.494|1.025***|0.665***|0.529**|0.478**|0.528**|0.521***|0.469**|0.474**|0.371**|0.428**|0.261*|0.200*|0.211**|0.203***|0.183**|
||(0.310)|(0.195)|(0.205)|(0.232)|(0.203)|(0.227)|(0.185)|(0.227)|(0.214)|(0.175)|(0.197)|(0.150)|(0.110)|(0.095)|(0.076)|(0.085)|
|GDP growth (t)|0.182|0.120|0.204|0.133|0.260*|0.083|0.163|0.149|0.096|0.141|0.098|0.009|-0.002|-0.004|0.028|0.022|
||(0.246)|(0.151)|(0.187)|(0.225)|(0.145)|(0.183)|(0.158)|(0.154)|(0.169)|(0.106)|(0.105)|(0.114)|(0.057)|(0.066)|(0.069)|(0.110)|
|House price misalignment (t)|-0.748***|-0.812***|-0.837***|-0.846***|-0.962***|-0.965***|-0.976***|-1.015***|-1.085***|-1.076***|-1.015***|-1.051***|-1.047***|-1.037***|-0.978***|-1.023***|
||(0.240)|(0.198)|(0.138)|(0.117)|(0.088)|(0.144)|(0.099)|(0.084)|(0.078)|(0.087)|(0.073)|(0.076)|(0.075)|(0.084)|(0.090)|(0.095)|
|Financial condition index (t)|-0.619***|-0.525**|-0.660***|-0.674***|-0.539***|-0.453***|-0.225|-0.157|-0.094|-0.029|-0.020|-0.042|-0.086|-0.088|-0.048|-0.105|
||(0.194)|(0.241)|(0.152)|(0.180)|(0.151)|(0.167)|(0.149)|(0.177)|(0.111)|(0.069)|(0.086)|(0.068)|(0.057)|(0.070)|(0.082)|(0.085)|
|Credit boom (t)|-0.526|-0.685*|-0.934***|-1.039***|-0.959***|-1.106***|-1.065***|-0.784***|-0.561*|-0.282*|-0.125|-0.134|-0.084|-0.013|0.017|0.164|
||(0.589)|(0.378)|(0.283)|(0.341)|(0.261)|(0.386)|(0.290)|(0.240)|(0.314)|(0.157)|(0.209)|(0.214)|(0.123)|(0.262)|(0.242)|(0.246)|
|Observations|948|938|928|918|908|898|888|878|868|858|848|838|828|818|808|798|



49 

**Table A.2: Baseline Estimations of Median House Prices Growth.** The tables report the estimated coefficients from median regressions using the baseline specification of the house price-at-risk model. The model is estimated at the 50th percentile of 1 quarter ahead average house price growth up to 16 quarters ahead. Panel quantile regressions are performed following the approach described in Section 3. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.446***|1.235***|1.088***|0.933***|0.839***|0.749***|0.699***|0.633***|0.595***|0.543***|0.506***|0.461***|0.445***|0.414***|0.391***|0.366***|
||(0.083)|(0.051)|(0.035)|(0.037)|(0.034)|(0.054)|(0.036)|(0.055)|(0.045)|(0.031)|(0.034)|(0.025)|(0.027)|(0.024)|(0.017)|(0.021)|
|GDP growth (t)|0.084***|0.010|-0.009|-0.037|-0.052*|-0.042**|-0.058***|-0.051***|-0.052***|-0.044***|-0.037|-0.047***|-0.037|-0.028|-0.031*|-0.032**|
||(0.030)|(0.029)|(0.030)|(0.032)|(0.027)|(0.016)|(0.020)|(0.017)|(0.016)|(0.016)|(0.023)|(0.009)|(0.027)|(0.029)|(0.017)|(0.016)|
|House price misalignment (t)|-0.257***|-0.291***|-0.353***|-0.434***|-0.495***|-0.537***|-0.566***|-0.603***|-0.626***|-0.683***|-0.699***|-0.729***|-0.755***|-0.772***|-0.789***|-0.808***|
||(0.047)|(0.036)|(0.024)|(0.029)|(0.031)|(0.034)|(0.024)|(0.029)|(0.026)|(0.019)|(0.027)|(0.021)|(0.024)|(0.024)|(0.020)|(0.023)|
|Financial condition index (t)|-0.158***|-0.173***|-0.164***|-0.163***|-0.134***|-0.130***|-0.121***|-0.109***|-0.099***|-0.093***|-0.076***|-0.074***|-0.062***|-0.051***|-0.037***|-0.026|
||(0.034)|(0.029)|(0.024)|(0.029)|(0.032)|(0.026)|(0.028)|(0.028)|(0.026)|(0.023)|(0.021)|(0.018)|(0.021)|(0.016)|(0.011)|(0.016)|
|Credit boom (t)|-0.060|-0.077|-0.070**|-0.086|-0.114**|-0.122|-0.088***|-0.071|-0.072**|-0.047|-0.030|-0.043|-0.020|0.000|0.018|0.039|
||(0.067)|(0.063)|(0.035)|(0.054)|(0.053)|(0.075)|(0.031)|(0.044)|(0.031)|(0.052)|(0.032)|(0.044)|(0.056)|(0.041)|(0.031)|(0.042)|
|Observations|2,389|2,367|2,345|2,323|2,301|2,279|2,257|2,235|2,213|2,191|2,169|2,147|2,125|2,103|2,081|2,059|



50 

**Table A.2: Baseline Estimations of Median House Prices Growth (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.141***|0.946***|0.778***|0.781***|0.671***|0.600***|0.491***|0.494***|0.482***|0.428***|0.370***|0.357***|0.332***|0.329***|0.299***|0.283***|
||(0.100)|(0.151)|(0.120)|(0.067)|(0.082)|(0.071)|(0.092)|(0.063)|(0.074)|(0.078)|(0.074)|(0.052)|(0.054)|(0.063)|(0.042)|(0.059)|
|GDP growth (t)|0.201**|0.031|0.106|0.076|0.043|0.037|0.093|0.060|0.017|0.012|0.010|0.023|0.026|0.006|-0.008|-0.029|
||(0.098)|(0.098)|(0.084)|(0.061)|(0.069)|(0.069)|(0.062)|(0.063)|(0.033)|(0.051)|(0.041)|(0.045)|(0.039)|(0.044)|(0.038)|(0.044)|
|House price misalignment (t)|-0.311***|-0.388***|-0.399***|-0.395***|-0.482***|-0.541***|-0.554***|-0.631***|-0.673***|-0.744***|-0.782***|-0.824***|-0.822***|-0.829***|-0.825***|-0.829***|
||(0.102)|(0.074)|(0.084)|(0.082)|(0.081)|(0.059)|(0.080)|(0.051)|(0.059)|(0.080)|(0.083)|(0.076)|(0.076)|(0.054)|(0.039)|(0.030)|
|Financial condition index (t)|-0.427***|-0.318***|-0.184***|-0.165***|-0.157**|-0.126|-0.138**|-0.094*|-0.092|-0.097*|-0.104*|-0.098*|-0.073*|-0.066|-0.059*|-0.038|
||(0.098)|(0.067)|(0.063)|(0.044)|(0.074)|(0.107)|(0.057)|(0.053)|(0.057)|(0.052)|(0.058)|(0.051)|(0.038)|(0.041)|(0.036)|(0.030)|
|Credit boom (t)|0.029|0.034|-0.146|-0.076|-0.094|-0.094|-0.089|-0.078|-0.048|-0.014|0.050|0.074|0.071|0.056|0.068|0.062|
||(0.143)|(0.199)|(0.118)|(0.099)|(0.081)|(0.090)|(0.074)|(0.087)|(0.078)|(0.087)|(0.083)|(0.064)|(0.064)|(0.071)|(0.064)|(0.063)|
|Observations|948|938|928|918|908|898|888|878|868|858|848|838|828|818|808|798|



51 

**Table A.3: Quantile R**<sup>**2**</sup> **Accuracy Measure.** The table reports out-of-sample quantile R<sup>2</sup> (in percentage) relative to the historical quantile model and the corresponding t-statistic. The accuracy measure is computed for both the panel-based HaR model (baseline) and a country-level HaR model. Country-level quantile regressions correspond to the second step of the estimator described in Section 3 without the adjustment for fixed effects. Results are presented for the 5th percentile of future house price growth for the United States at selected forecasting horizons, i.e. h=1,4,8,12. 

||United Sta|tes|||
|---|---|---|---|---|
|**Panel-Based Estimates**|**H=1**|**H=4**|**H=8**|**H=12**|
|Pseudo-R2|59.96|48.09|38.18|47.77|
|T-Statistics|0.01|0.01|0.01|0.00|
|**Country-Level Estimates**|**H=1**|**H=4**|**H=8**|**H=12**|
|Pseudo-R2|80.07|72.66|86.41|83.78|
|T-Statistics|0.00|0.00|0.00|0.00|



52 

**Table A.4: Effects of HaR on GDP Downside Risks.** The tables report the estimated coefficients of a Growth-at-Risk (GaR) specification augmented with house price-at-risk. GaR refers to the set of outcomes that fall into the 5th percentile of (conditional) forecast densities of GDP growth as a function of a financial condition index (Adrian et al., 2019). The model is estimated at the 5th percentile of 1 quarter ahead average real GDP growth up to 16 quarters ahead. Panel quantile regressions are performed following the approach described in Section 3. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. Regression coefficients are standardized. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|GDP growth (t)|0.009|0.057|0.050|0.039|0.037|0.016|0.031|0.039**|0.022|0.040|0.058|0.036|0.051**|0.062**|0.054***|0.074***|
||(0.082)|(0.050)|(0.042)|(0.037)|(0.043)|(0.049)|(0.048)|(0.017)|(0.041)|(0.033)|(0.036)|(0.033)|(0.026)|(0.031)|(0.018)|(0.025)|
|Financial condition index (t)|-0.279***|-0.113**|-0.113***|-0.049|-0.043|0.009|0.044*|0.079***|0.100***|0.116***|0.123***|0.111***|0.113***|0.113***|0.113***|0.104***|
||(0.082)|(0.048)|(0.040)|(0.045)|(0.035)|(0.027)|(0.026)|(0.028)|(0.023)|(0.017)|(0.015)|(0.019)|(0.016)|(0.020)|(0.013)|(0.013)|
|HaR 1-year ahead (t)|0.342***|0.445***|0.364***|0.377***|0.350***|0.344***|0.298***|0.285***|0.245***|0.236***|0.227***|0.218***|0.207***|0.204***|0.204***|0.195***|
||(0.126)|(0.051)|(0.053)|(0.050)|(0.036)|(0.047)|(0.029)|(0.037)|(0.031)|(0.032)|(0.020)|(0.024)|(0.021)|(0.019)|(0.016)|(0.014)|
|Observations|2,394|2,372|2,350|2,328|2,306|2,284|2,262|2,240|2,218|2,196|2,174|2,152|2,130|2,108|2,086|2,064|



53 

##### **Table A.4: Effects of HaR on GDP Downside Risks (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|GDP growth (t)|0.544***|0.496***|0.185|-0.035|-0.054|-0.128**|0.047|0.070|0.091|0.103|0.112***|0.100|0.048|0.046|0.004|0.004|
||(0.207)|(0.152)|(0.122)|(0.079)|(0.120)|(0.058)|(0.062)|(0.076)|(0.073)|(0.072)|(0.036)|(0.068)|(0.063)|(0.082)|(0.077)|(0.064)|
|Financial condition index (t)|0.083|0.344**|0.442***|0.607***|0.582***|0.493***|0.461***|0.405***|0.398***|0.348***|0.287***|0.259***|0.247***|0.244***|0.237***|0.233***|
||(0.232)|(0.145)|(0.123)|(0.147)|(0.072)|(0.037)|(0.037)|(0.038)|(0.051)|(0.039)|(0.037)|(0.044)|(0.032)|(0.037)|(0.036)|(0.040)|
|HaR 1-year ahead (t)|0.354|0.301|0.462**|0.521***|0.517***|0.490***|0.405***|0.325***|0.336***|0.309***|0.292***|0.294***|0.309***|0.291***|0.271***|0.270***|
||(0.267)|(0.188)|(0.182)|(0.139)|(0.112)|(0.049)|(0.039)|(0.058)|(0.084)|(0.063)|(0.064)|(0.051)|(0.050)|(0.039)|(0.038)|(0.038)|
|Observations|953|944|935|926|917|907|897|887|877|867|857|847|837|827|817|807|



54 

**Table A.5: Effect of HaR on Future Median GDP Growth.** The tables report the estimated coefficients from median regressions using a Growthat-Risk (GaR) model augmented with HaR. The model is estimated at the 50th percentile of 1 quarter ahead average GDP growth up to 16 quarters ahead. Panel quantile regressions are performed following the approach described in Section 3. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|GDP growth (t)|0.162***|0.136***|0.111***|0.083***|0.078***|0.056***|0.039*|0.031|0.017|0.005|0.004|-0.003|0.005|-0.001|0.000|0.007|
||(0.034)|(0.029)|(0.023)|(0.028)|(0.022)|(0.016)|(0.020)|(0.022)|(0.013)|(0.014)|(0.010)|(0.011)|(0.010)|(0.015)|(0.010)|(0.010)|
|Financial condition index (t)|-0.099***|-0.063***|-0.042***|-0.032*|-0.019**|0.002|-0.002|0.008|0.009|0.022|0.031**|0.031**|0.045***|0.047***|0.060***|0.062***|
||(0.015)|(0.015)|(0.015)|(0.018)|(0.009)|(0.019)|(0.014)|(0.014)|(0.018)|(0.015)|(0.015)|(0.013)|(0.011)|(0.009)|(0.011)|(0.009)|
|HaR 1-year ahead (t)|0.198***|0.186***|0.201***|0.191***|0.194***|0.190***|0.175***|0.178***|0.169***|0.176***|0.167***|0.163***|0.156***|0.149***|0.138***|0.129***|
||(0.023)|(0.022)|(0.020)|(0.018)|(0.017)|(0.015)|(0.015)|(0.013)|(0.014)|(0.015)|(0.016)|(0.010)|(0.014)|(0.014)|(0.014)|(0.012)|
|Observations|2,394|2,372|2,350|2,328|2,306|2,284|2,262|2,240|2,218|2,196|2,174|2,152|2,130|2,108|2,086|2,064|



55 

**Table A.5: Effect of HaR on Future Median GDP Growth (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|GDP growth (t)|0.322***|0.168***|0.104**|0.110***|0.089***|0.055|0.047|0.010|0.028|0.006|0.002|-0.001|0.001|0.004|-0.001|-0.009|
||(0.072)|(0.063)|(0.052)|(0.042)|(0.027)|(0.035)|(0.039)|(0.049)|(0.031)|(0.016)|(0.022)|(0.031)|(0.036)|(0.030)|(0.026)|(0.020)|
|Financial condition index (t)|-0.159***|-0.091*|-0.078**|-0.029|-0.005|0.036|0.073**|0.095***|0.104***|0.119***|0.097***|0.095***|0.097***|0.105***|0.106***|0.104***|
||(0.046)|(0.049)|(0.035)|(0.029)|(0.029)|(0.028)|(0.033)|(0.026)|(0.040)|(0.032)|(0.030)|(0.027)|(0.019)|(0.028)|(0.021)|(0.018)|
|HaR 1-year ahead (t)|0.090*|0.139***|0.155***|0.128**|0.145***|0.156***|0.169***|0.191***|0.175***|0.171***|0.155***|0.126***|0.109***|0.079***|0.079***|0.062***|
||(0.053)|(0.046)|(0.041)|(0.050)|(0.041)|(0.029)|(0.036)|(0.036)|(0.049)|(0.028)|(0.034)|(0.027)|(0.027)|(0.028)|(0.016)|(0.019)|
|Observations|953|944|935|926|917|907|897|887|877|867|857|847|837|827|817|807|



56 

**Table A.6:** The tables show the marginal probabilities of one-year ahead HaR at given values on the occurrence of a financial crisis, as identified by Laeven and Valencia (2018), from a model with fixed effects, output growth, the financial conditions index, credit-to-GDP gap, and HaR. 

Advanced Economies 

|**HaR (H=4)**|**Predictive Margin**|**Std. Err.**|**z**|**P>z**|**[95% conf.**|**interval]**|
|---|---|---|---|---|---|---|
|-16|0.34|0.08|4.06|0.00|0.18|0.51|
|-14|0.26|0.05|5.11|0.00|0.16|0.36|
|-12|0.19|0.02|8.43|0.00|0.15|0.24|
|-10|0.14|0.00|40.71|0.00|0.13|0.14|
|-8|0.09|0.01|9.37|0.00|0.07|0.11|
|-6|0.06|0.02|4.16|0.00|0.03|0.09|
|-4|0.04|0.02|2.61|0.01|0.01|0.07|
|-2|0.03|0.01|1.89|0.06|0.00|0.06|
|0|0.02|0.01|1.47|0.14|-0.01|0.04|



Emerging Market Economies 

|**HaR (H=4)**|**Predictive Margin**|**Std. Err.**|**z**|**P>z**|**[95% conf.**|**interval]**|
|---|---|---|---|---|---|---|
|-16|0.25|0.03|7.90|0.00|0.19|0.31|
|-14|0.17|0.02|10.63|0.00|0.14|0.20|
|-12|0.11|0.01|8.00|0.00|0.08|0.14|
|-10|0.07|0.02|4.54|0.00|0.04|0.10|
|-8|0.04|0.01|2.89|0.00|0.01|0.07|
|-6|0.02|0.01|2.05|0.04|0.00|0.05|
|-4|0.01|0.01|1.55|0.12|0.00|0.03|
|-2|0.01|0.01|1.24|0.21|0.00|0.02|
|0|0.00|0.00|1.03|0.30|0.00|0.01|



57 

**Table A.7: Effect of Macroprudential Policy Intensity Measure on HaR.** The tables show the effect of the macroprudential policy intensity measure (MPM) once added to the baseline model estimation. The model is estimated at the 5th percentile of 1 quarter ahead average real house price growth up to 16 quarters ahead. The regressions control for the interaction of the policy measure with the financial conditions index (FCI). The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.246***|1.111***|0.855***|0.789***|0.734***|0.525***|0.374***|0.349***|0.329***|0.381***|0.371***|0.396***|0.369***|0.343***|0.333***|0.299***|
||(0.150)|(0.139)|(0.106)|(0.126)|(0.123)|(0.122)|(0.087)|(0.077)|(0.069)|(0.064)|(0.023)|(0.053)|(0.055)|(0.063)|(0.064)|(0.059)|
|GDP growth (t)|0.198**|0.074|0.055|-0.207*|-0.239**|-0.241**|-0.186***|-0.173***|-0.179***|-0.146**|-0.144***|-0.132**|-0.139**|-0.105*|-0.100|-0.110**|
||(0.097)|(0.130)|(0.094)|(0.116)|(0.098)|(0.099)|(0.062)|(0.063)|(0.060)|(0.071)|(0.033)|(0.061)|(0.066)|(0.056)|(0.069)|(0.050)|
|House price misalignment (t)|-0.508***|-0.753***|-0.839***|-0.937***|-1.001***|-0.980***|-1.035***|-1.035***|-0.993***|-0.956***|-0.927***|-0.966***|-0.975***|-0.975***|-1.011***|-0.996***|
||(0.120)|(0.130)|(0.124)|(0.101)|(0.098)|(0.078)|(0.063)|(0.065)|(0.055)|(0.029)|(0.038)|(0.059)|(0.046)|(0.043)|(0.035)|(0.037)|
|Financial condition index (t)|-0.287***|-0.309**|-0.120|-0.204*|-0.195|-0.214***|-0.198*|-0.191***|-0.200***|-0.160***|-0.152***|-0.115***|-0.119***|-0.107***|-0.116***|-0.121**|
||(0.088)|(0.150)|(0.097)|(0.113)|(0.121)|(0.082)|(0.103)|(0.061)|(0.071)|(0.046)|(0.052)|(0.039)|(0.045)|(0.039)|(0.039)|(0.049)|
|Credit boom (t)|-0.270|-0.503***|-0.538**|-0.455***|-0.299*|-0.263|-0.404***|-0.340***|-0.363***|-0.371***|-0.293***|-0.317**|-0.263**|-0.239***|-0.200***|-0.191***|
||(0.248)|(0.178)|(0.233)|(0.175)|(0.177)|(0.165)|(0.147)|(0.127)|(0.133)|(0.140)|(0.089)|(0.159)|(0.125)|(0.080)|(0.069)|(0.073)|
|MPM x Financial Condition Index (t|)<br>0.355***|0.332**|0.290***|0.070|0.071|0.099|0.097|0.005|-0.029|-0.044|-0.048|-0.127|-0.139*|-0.121*|-0.131**|-0.122**|
||(0.086)|(0.167)|(0.090)|(0.137)|(0.093)|(0.095)|(0.077)|(0.070)|(0.096)|(0.069)|(0.079)|(0.079)|(0.082)|(0.072)|(0.061)|(0.062)|
|MPM (t)|0.230**|0.197*|0.237***|0.235***|0.282***|0.284***|0.288***|0.204***|0.165***|0.153***|0.120**|0.065|0.042|0.059|0.046|0.043|
||(0.090)|(0.101)|(0.056)|(0.057)|(0.061)|(0.072)|(0.059)|(0.054)|(0.063)|(0.048)|(0.060)|(0.068)|(0.068)|(0.053)|(0.043)|(0.056)|
|Observations|2,389|2,367|2,345|2,323|2,301|2,279|2,257|2,235|2,213|2,191|2,169|2,147|2,125|2,103|2,081|2,059|



58 

**Table A.7: Effect of Macroprudential Policy Intensity Measure on HaR (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.557|1.039***|0.661***|0.454*|0.468***|0.494**|0.531***|0.428**|0.428**|0.331**|0.463***|0.341**|0.238**|0.171**|0.198**|0.174***|
||(0.396)|(0.191)|(0.200)|(0.238)|(0.158)|(0.247)|(0.167)|(0.215)|(0.182)|(0.147)|(0.104)|(0.143)|(0.111)|(0.074)|(0.089)|(0.062)|
|GDP growth (t)|-0.003|0.115|0.105|0.134|0.242|0.082|0.159|0.126|0.031|0.122|0.090|-0.025|-0.020|-0.009|0.048|-0.028|
||(0.325)|(0.181)|(0.221)|(0.287)|(0.165)|(0.229)|(0.141)|(0.150)|(0.116)|(0.128)|(0.123)|(0.102)|(0.061)|(0.045)|(0.076)|(0.084)|
|House price misalignment (t)|-0.936***|-0.808***|-0.860***|-0.863***|-0.958***|-1.019***|-0.981***|-1.033***|-1.053***|-1.089***|-1.106***|-1.060***|-1.049***|-1.014***|-1.033***|-0.963***|
||(0.270)|(0.255)|(0.101)|(0.185)|(0.181)|(0.114)|(0.102)|(0.103)|s|(0.088)|(0.083)|(0.085)|(0.077)|(0.094)|(0.077)|(0.088)|
|Financial condition index (t)|-0.715***|-0.503***|-0.671***|-0.691***|-0.534***|-0.485***|-0.196|-0.114|-0.114|-0.011|-0.033|-0.045|-0.078|-0.134|-0.087|-0.093|
||(0.223)|(0.194)|(0.202)|(0.223)|(0.186)|(0.176)|(0.189)|(0.209)|(0.125)|(0.115)|(0.111)|(0.088)|(0.073)|(0.088)|(0.089)|(0.081)|
|Credit boom (t)|-0.507|-0.640|-0.941***|-0.975***|-0.920***|-1.011**|-0.954***|-0.825***|-0.671***|-0.305|-0.316**|0.015|-0.033|0.093|0.124|0.105|
||(0.575)|(0.398)|(0.254)|(0.309)|(0.217)|(0.419)|(0.321)|(0.278)|(0.247)|(0.262)|(0.133)|(0.147)|(0.162)|(0.174)|(0.208)|(0.156)|
|MPM x Financial Condition Index (t)|-0.157|0.036|0.122*|0.110|0.101|0.002|-0.074|-0.040|-0.052|-0.150|-0.130|-0.103**|-0.120***|-0.053|-0.045|-0.047|
||(0.386)|(0.180)|(0.069)|(0.174)|(0.112)|(0.112)|(0.126)|(0.122)|(0.115)|(0.127)|(0.110)|(0.047)|(0.042)|(0.057)|(0.054)|(0.066)|
|MPM (t)|0.089|0.133|0.150*|0.151|0.063|0.061|0.084|0.186|0.224**|0.139|0.137|0.214***|0.145***|0.209***|0.171***|0.146***|
||(0.335)|(0.161)|(0.083)|(0.168)|(0.091)|(0.069)|(0.077)|(0.114)|(0.107)|(0.138)|(0.092)|(0.059)|(0.055)|(0.058)|(0.047)|(0.043)|
|Observations|948|938|928|918|908|898|888|878|868|858|848|838|828|818|808|798|



59 

**Table A.8: Effect of Orthogonalized Macroprudential Policy Intensity Measure on HaR.** The tables show the effect of macroprudential policy shocks on HaR once added to the baseline model estimation. The model is estimated at the 5th percentile of 1 quarter ahead average real house price growth up to 16 quarters ahead. Macroprudential policy shocks are used in the regression by orthogonalizing the macroprudential intensity measure (MPM) from ex-ante credit conditions, house price developments, and lag values of the policy measure. The regressions control for the interaction of the policy measure with the financial conditions index (FCI). The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.357***|1.130***|0.915***|0.773***|0.713***|0.572***|0.465***|0.451***|0.463***|0.450***|0.465***|0.452***|0.459***|0.418***|0.374***|0.326***|
||(0.139)|(0.124)|(0.100)|(0.133)|(0.111)|(0.112)|(0.124)|(0.089)|(0.108)|(0.112)|(0.091)|(0.081)|(0.078)|(0.062)|(0.056)|(0.067)|
|GDP growth (t)|0.185*|0.079|0.042|-0.171|-0.287***|-0.206*|-0.179|-0.198**|-0.238**|-0.235**|-0.186***|-0.193**|-0.195***|-0.174***|-0.144**|-0.122*|
||(0.100)|(0.081)|(0.071)|(0.119)|(0.076)|(0.120)|(0.113)|(0.091)|(0.101)|(0.094)|(0.064)|(0.077)|(0.062)|(0.056)|(0.071)|(0.074)|
|House price misalignment (t)|-0.348**|-0.654***|-0.800***|-0.852***|-0.828***|-0.875***|-0.967***|-0.969***|-0.952***|-0.985***|-1.018***|-1.027***|-1.057***|-1.079***|-1.086***|-1.071***|
||(0.143)|(0.136)|(0.134)|(0.100)|(0.110)|(0.082)|(0.093)|(0.070)|(0.057)|(0.068)|(0.055)|(0.063)|(0.043)|(0.047)|(0.035)|(0.038)|
|Financial condition index (t)|-0.451**|-0.283*|-0.115|-0.190|-0.191*|-0.251**|-0.183|-0.128*|-0.154**|-0.125*|-0.157**|-0.181**|-0.169***|-0.183***|-0.183***|-0.175***|
||(0.205)|(0.163)|(0.178)|(0.159)|(0.115)|(0.113)|(0.122)|(0.077)|(0.071)|(0.066)|(0.062)|(0.079)|(0.063)|(0.050)|(0.064)|(0.035)|
|Credit boom (t)|-0.126|-0.756***|-0.806***|-0.828***|-0.666***|-0.660***|-0.739***|-0.658***|-0.589***|-0.698***|-0.442*|-0.324|-0.277*|-0.202*|-0.219*|-0.188*|
||(0.325)|(0.220)|(0.228)|(0.246)|(0.250)|(0.149)|(0.195)|(0.107)|(0.193)|(0.174)|(0.238)|(0.211)|(0.162)|(0.122)|(0.121)|(0.098)|
|LMPM x Financial Condition Index (t)|0.290*|0.192**|0.160|-0.036|-0.030|-0.047|-0.055|-0.044|-0.097|-0.052|-0.063|-0.075|-0.072|-0.082|-0.082*|-0.074***|
||(0.152)|(0.082)|(0.114)|(0.080)|(0.057)|(0.081)|(0.081)|(0.099)|(0.074)|(0.065)|(0.066)|(0.048)|(0.053)|(0.053)|(0.043)|(0.024)|
|LMPM (t)|0.211***|0.311***|0.283***|0.367***|0.348***|0.336***|0.285***|0.279***|0.201***|0.223***|0.160*|0.088|0.068|0.075|0.055|0.053|
||(0.071)|(0.068)|(0.091)|(0.067)|(0.060)|(0.056)|(0.054)|(0.052)|(0.059)|(0.067)|(0.085)|(0.066)|(0.100)|(0.065)|(0.053)|(0.045)|
|Observations|2,002|1,980|1,958|1,936|1,914|1,892|1,870|1,848|1,826|1,804|1,782|1,760|1,738|1,716|1,694|1,672|



60 

##### **Table A.8: Effect of Orthogonalized Macroprudential Policy Intensity Measure on HaR (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.845**|1.373***|0.741***|0.709**|0.688***|0.683***|0.577**|0.583*|0.584*|0.613***|0.576***|0.385**|0.290**|0.266**|0.281**|0.257**|
||(0.334)|(0.256)|(0.227)|(0.293)|(0.231)|(0.227)|(0.292)|(0.325)|(0.301)|(0.234)|(0.171)|(0.181)|(0.127)|(0.115)|(0.112)|(0.118)|
|GDP growth (t)|0.023|-0.152|0.221|0.250|0.119|0.406*|0.268|0.226|0.036|0.111|0.052|-0.042|-0.013|0.007|0.014|-0.038|
||(0.348)|(0.450)|(0.321)|(0.247)|(0.208)|(0.236)|(0.243)|(0.234)|(0.179)|(0.109)|(0.120)|(0.097)|(0.104)|(0.081)|(0.071)|(0.075)|
|House price misalignment (t)|-1.014***|-1.019***|-0.988***|-1.010***|-1.160***|-1.047***|-1.004***|-1.066***|-1.172***|-1.145***|-1.144***|-1.169***|-1.130***|-1.136***|-1.082***|-1.077***|
||(0.326)|(0.156)|(0.161)|(0.136)|(0.150)|(0.120)|(0.177)|(0.106)|(0.129)|(0.086)|(0.056)|(0.082)|(0.087)|(0.094)|(0.073)|(0.102)|
|Financial condition index (t)|-0.898**|-0.728**|-0.798***|-0.739***|-0.688***|-0.422|-0.136|-0.188|-0.208|-0.149|-0.167**|-0.200*|-0.162**|-0.175***|-0.159**|-0.180***|
||(0.400)|(0.366)|(0.210)|(0.232)|(0.209)|(0.295)|(0.238)|(0.188)|(0.164)|(0.107)|(0.082)|(0.105)|(0.068)|(0.063)|(0.065)|(0.062)|
|Credit boom (t)|0.409|-0.445|-0.633*|-0.735**|-0.793**|-0.732**|-0.909**|-0.630*|-0.445|-0.206|-0.102|0.125|0.104|0.097|0.236|0.125|
||(0.786)|(0.364)|(0.375)|(0.367)|(0.348)|(0.326)|(0.399)|(0.327)|(0.330)|(0.192)|(0.166)|(0.144)|(0.119)|(0.172)|(0.146)|(0.145)|
|LMPM x Financial Condition Index (t)|-0.423|-0.207|0.275|0.083|0.162|0.126|-0.134|-0.010|0.020|0.007|0.002|-0.065|-0.121***|-0.135***|-0.131***|-0.121***|
||(0.308)|(0.174)|(0.289)|(0.213)|(0.143)|(0.178)|(0.165)|(0.172)|(0.131)|(0.107)|(0.050)|(0.076)|(0.039)|(0.044)|(0.032)|(0.039)|
|LMPM (t)|-0.147|-0.055|0.123|0.011|0.031|0.065|-0.007|-0.013|0.282|0.226*|0.222***|0.267***|0.209***|0.178***|0.168***|0.143***|
||(0.360)|(0.155)|(0.254)|(0.223)|(0.170)|(0.173)|(0.204)|(0.205)|(0.256)|(0.132)|(0.067)|(0.065)|(0.052)|(0.044)|(0.048)|(0.049)|
|Observations|847|837|827|817|807|797|787|777|767|757|747|737|727|717|707|697|



61 

**Table A.9: Effect of Orthogonalized Macroprudential Policy Instantaneous Measure on HaR.** The tables show the effect of macroprudential policy shocks on HaR once added to the baseline model estimation. The model is estimated at the 5th percentile of 1 quarter ahead average real house price growth up to 16 quarters ahead. Macroprudential policy shocks are used in the regression by orthogonalizing the instantaneous changes in the macroprudential policy measures (PM) from ex-ante credit conditions, house price developments, and lag values of the policy measure. The regressions control for the interaction of the policy measure with the financial conditions index (FCI). The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.230***|1.041***|0.921***|0.814***|0.722***|0.550***|0.397***|0.374***|0.393***|0.423***|0.398***|0.404***|0.371***|0.343***|0.319***|0.289***|
||(0.124)|(0.092)|(0.071)|(0.111)|(0.108)|(0.131)|(0.134)|(0.102)|(0.096)|(0.088)|(0.055)|(0.049)|(0.055)|(0.047)|(0.066)|(0.054)|
|GDP growth (t)|0.165**|0.049|0.028|-0.146**|-0.249**|-0.209*|-0.187**|-0.148|-0.191**|-0.146*|-0.144***|-0.141**|-0.144**|-0.121*|-0.095|-0.104*|
||(0.081)|(0.065)|(0.066)|(0.070)|(0.108)|(0.119)|(0.076)|(0.099)|(0.097)|(0.083)|(0.046)|(0.064)|(0.057)|(0.064)|(0.067)|(0.061)|
|House price misalignment (t)|-0.513***|-0.814***|-0.868***|-0.933***|-0.946***|-0.938***|-0.996***|-0.963***|-0.937***|-0.933***|-0.926***|-0.978***|-0.994***|-1.007***|-1.024***|-1.017***|
||(0.144)|(0.096)|(0.110)|(0.106)|(0.068)|(0.108)|(0.086)|(0.080)|(0.056)|(0.068)|(0.062)|(0.068)|(0.063)|(0.047)|(0.037)|(0.050)|
|Financial condition index (t)|-0.297*|-0.246***|-0.095|-0.195**|-0.245**|-0.256***|-0.184***|-0.133|-0.104|-0.111|-0.104*|-0.120**|-0.111*|-0.103|-0.134***|-0.116**|
||(0.179)|(0.089)|(0.116)|(0.088)|(0.101)|(0.060)|(0.069)|(0.101)|(0.071)|(0.074)|(0.053)|(0.051)|(0.067)|(0.063)|(0.045)|(0.056)|
|Credit boom (t)|-0.114|-0.465**|-0.580**|-0.509***|-0.429***|-0.315*|-0.518***|-0.434***|-0.433***|-0.480***|-0.392***|-0.327**|-0.290*|-0.278***|-0.222***|-0.196**|
||(0.220)|(0.215)|(0.239)|(0.166)|(0.165)|(0.172)|(0.177)|(0.150)|(0.108)|(0.162)|(0.129)|(0.154)|(0.170)|(0.100)|(0.080)|(0.100)|
|LPM x Financial Condition Index (t)|0.269***|0.256**|0.127|-0.044|-0.078|-0.039|-0.038|0.006|-0.002|-0.040|-0.035|-0.087|-0.089**|-0.095***|-0.087***|-0.078***|
||(0.095)|(0.104)|(0.111)|(0.085)|(0.096)|(0.090)|(0.076)|(0.099)|(0.095)|(0.096)|(0.078)|(0.103)|(0.041)|(0.020)|(0.019)|(0.015)|
|LPM (t)|0.310***|0.313***|0.257***|0.251***|0.296***|0.273***|0.272***|0.240***|0.210***|0.194***|0.157***|0.127*|0.094|0.063|0.065*|0.067|
||(0.079)|(0.053)|(0.033)|(0.067)|(0.046)|(0.040)|(0.043)|(0.036)|(0.045)|(0.056)|(0.053)|(0.069)|(0.068)|(0.064)|(0.035)|(0.046)|
|Observations|2,301|2,279|2,257|2,235|2,213|2,191|2,169|2,147|2,125|2,103|2,081|2,059|2,037|2,015|1,993|1,971|



62 

**Table A.9: Effect of Orthogonalized Macroprudential Policy Instantaneous Measure on HaR (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.510|1.182***|0.671**|0.557**|0.601***|0.698***|0.557***|0.605**|0.557**|0.478***|0.546***|0.430***|0.375***|0.297***|0.304***|0.276***|
||(0.364)|(0.326)|(0.269)|(0.230)|(0.134)|(0.235)|(0.178)|(0.249)|(0.226)|(0.159)|(0.143)|(0.135)|(0.126)|(0.103)|(0.073)|(0.078)|
|GDP growth (t)|0.252|0.062|0.223|0.354|0.072|0.172|0.165|0.241|0.034|0.156|0.037|-0.031|0.001|0.009|-0.013|-0.038|
||(0.288)|(0.352)|(0.300)|(0.329)|(0.141)|(0.281)|(0.150)|(0.154)|(0.189)|(0.172)|(0.096)|(0.085)|(0.101)|(0.060)|(0.074)|(0.044)|
|House price misalignment (t)|-0.821***|-0.922***|-0.873***|-0.997***|-1.054***|-1.013***|-1.050***|-1.089***|-1.173***|-1.137***|-1.180***|-1.185***|-1.161***|-1.151***|-1.118***|-1.069***|
||(0.287)|(0.181)|(0.146)|(0.100)|(0.130)|(0.108)|(0.142)|(0.116)|(0.131)|(0.082)|(0.075)|(0.073)|(0.085)|(0.081)|(0.084)|(0.058)|
|Financial condition index (t)|-0.573|-0.571***|-0.739***|-0.722***|-0.641***|-0.549***|-0.332**|-0.343**|-0.221|-0.130|-0.219*|-0.240***|-0.184***|-0.213**|-0.197***|-0.169***|
||(0.359)|(0.184)|(0.139)|(0.164)|(0.137)|(0.193)|(0.162)|(0.139)|(0.142)|(0.124)|(0.130)|(0.064)|(0.068)|(0.096)|(0.066)|(0.061)|
|Credit boom (t)|-0.280|-0.685*|-0.745*|-0.813**|-0.997***|-0.748**|-0.857***|-0.661**|-0.469**|-0.109|-0.078|0.118|0.137|0.190|0.199|0.213|
||(0.636)|(0.356)|(0.391)|(0.412)|(0.279)|(0.317)|(0.326)|(0.291)|(0.195)|(0.201)|(0.162)|(0.198)|(0.148)|(0.212)|(0.182)|(0.159)|
|LPM x Financial Condition Index (t)|-0.304|-0.221|0.051|0.038|0.078|0.037|-0.003|0.180|-0.035|0.008|0.016|-0.006|-0.072|-0.077|-0.104**|-0.110**|
||(0.229)|(0.196)|(0.222)|(0.209)|(0.139)|(0.124)|(0.136)|(0.180)|(0.114)|(0.110)|(0.074)|(0.055)|(0.055)|(0.061)|(0.052)|(0.052)|
|LPM (t)|-0.122|-0.014|-0.087|-0.015|0.076|0.061|0.081|0.035|0.167|0.171|0.219**|0.193***|0.125*|0.143**|0.166***|0.170***|
||(0.318)|(0.180)|(0.141)|(0.171)|(0.170)|(0.126)|(0.116)|(0.133)|(0.130)|(0.106)|(0.094)|(0.065)|(0.076)|(0.066)|(0.060)|(0.044)|
|Observations|912|902|892|882|872|862|852|842|832|822|812|802|792|782|772|762|



63 

**Table A.10: Effect of Monetary Policy Shocks on HaR.** The tables show the effect of monetary policy shocks on HaR once added to the baseline model estimation. The model is estimated at the 5th percentile of 1 quarter ahead average real GDP growth up to 16 quarters ahead. Monetary policy shocks are constructed as residual from a Taylor rule. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

|||||||Adva|nced Ec|onomies|||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.354***|1.153***|0.942***|0.839***|0.759***|0.591***|0.391***|0.325***|0.402***|0.329***|0.381***|0.401***|0.390***|0.356***|0.355***|0.289***|
||(0.150)|(0.108)|(0.112)|(0.101)|(0.082)|(0.090)|(0.100)|(0.080)|(0.065)|(0.079)|(0.084)|(0.089)|(0.068)|(0.083)|(0.095)|(0.046)|
|GDP growth (t)|0.189***|0.094|0.018|-0.136|-0.247**|-0.299***|-0.224**|-0.171***|-0.223**|-0.126|-0.124*|-0.124*|-0.156***|-0.151**|-0.146***|-0.134*|
||(0.061)|(0.116)|(0.118)|(0.090)|(0.106)|(0.091)|(0.093)|(0.057)|(0.087)|(0.080)|(0.070)|(0.064)|(0.055)|(0.065)|(0.046)|(0.071)|
|House price misalignment (t)|-0.373**|-0.606***|-0.839***|-0.897***|-0.924***|-0.975***|-0.991***|-0.981***|-0.970***|-0.980***|-0.982***|-1.005***|-1.036***|-1.052***|-1.045***|-1.051***|
||(0.148)|(0.155)|(0.131)|(0.088)|(0.118)|(0.090)|(0.073)|(0.064)|(0.063)|(0.075)|(0.061)|(0.072)|(0.050)|(0.052)|(0.040)|(0.043)|
|Financial condition index (t)|-0.203|0.008|-0.013|-0.008|-0.066|-0.133|-0.170**|-0.126*|-0.101*|-0.103**|-0.120*|-0.085|-0.076**|-0.088|-0.078*|-0.097*|
||(0.190)|(0.105)|(0.150)|(0.148)|(0.105)|(0.098)|(0.072)|(0.069)|(0.060)|(0.052)|(0.064)|(0.059)|(0.036)|(0.057)|(0.045)|(0.050)|
|Credit boom (t)|-0.079|-0.647***|-0.555**|-0.729**|-0.529***|-0.482***|-0.570***|-0.452***|-0.418***|-0.334*|-0.336***|-0.305***|-0.278***|-0.234***|-0.193|-0.127|
||(0.296)|(0.203)|(0.225)|(0.308)|(0.176)|(0.156)|(0.200)|(0.159)|(0.119)|(0.183)|(0.112)|(0.118)|(0.080)|(0.077)|(0.120)|(0.097)|
|Monetary policy shock (t)|-0.406***|-0.223***|-0.039|-0.016|0.088|-0.046|-0.042|-0.064|-0.030|-0.019|0.013|0.017|-0.020|-0.007|0.018|0.002|
||(0.096)|(0.072)|(0.093)|(0.103)|(0.115)|(0.079)|(0.069)|(0.075)|(0.051)|(0.048)|(0.051)|(0.074)|(0.046)|(0.062)|(0.042)|(0.058)|
|Constant|-2.662***|-2.033***|-2.048***|-1.925***|-1.897***|-1.835***|-1.639***|-1.508***|-1.444***|-1.349***|-1.263***|-1.182***|-1.148***|-1.126***|-1.089***|-1.089***|
||(0.182)|(0.149)|(0.117)|(0.144)|(0.098)|(0.093)|(0.105)|(0.081)|(0.104)|(0.075)|(0.080)|(0.086)|(0.068)|(0.094)|(0.076)|(0.064)|
|Observations|2,149|2,127|2,105|2,083|2,061|2,039|2,017|1,995|1,974|1,953|1,932|1,911|1,890|1,868|1,846|1,824|



64 

**Table A.10: Effect of Monetary Policy Shocks on HaR (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.636*|1.268***|0.914***|0.796***|0.850***|0.706***|0.616***|0.569***|0.614***|0.633***|0.570***|0.439***|0.386***|0.322***|0.278***|0.296***|
||(0.383)|(0.289)|(0.291)|(0.233)|(0.217)|(0.270)|(0.205)|(0.126)|(0.182)|(0.240)|(0.195)|(0.166)|(0.123)|(0.087)|(0.090)|(0.097)|
|GDP growth (t)|0.188|-0.143|0.133|0.369|0.189|0.301|0.294*|0.116|0.067|0.123|0.128*|0.038|0.071|0.120|0.001|0.066|
||(0.335)|(0.385)|(0.352)|(0.429)|(0.211)|(0.221)|(0.156)|(0.185)|(0.204)|(0.120)|(0.076)|(0.111)|(0.066)|(0.099)|(0.075)|(0.065)|
|House price misalignment (t)|-0.730***|-1.011***|-1.058***|-0.950***|-1.090***|-1.102***|-1.070***|-1.162***|-1.197***|-1.189***|-1.186***|-1.228***|-1.224***|-1.270***|-1.167***|-1.190***|
||(0.218)|(0.170)|(0.123)|(0.124)|(0.153)|(0.123)|(0.137)|(0.137)|(0.140)|(0.095)|(0.080)|(0.103)|(0.097)|(0.111)|(0.130)|(0.089)|
|Financial condition index (t)|-0.945***|-0.847***|-0.863***|-0.695***|-0.683***|-0.481**|-0.306*|-0.369**|-0.402**|-0.331*|-0.228|-0.261**|-0.249***|-0.314***|-0.306***|-0.278***|
||(0.224)|(0.215)|(0.217)|(0.196)|(0.258)|(0.197)|(0.179)|(0.165)|(0.203)|(0.196)|(0.160)|(0.133)|(0.095)|(0.074)|(0.098)|(0.070)|
|Credit boom (t)|0.273|-0.551*|-0.665|-0.819**|-0.899***|-0.759***|-1.077***|-0.879***|-0.514|-0.308|-0.159|-0.027|-0.003|0.111|0.220|0.188|
||(0.731)|(0.290)|(0.426)|(0.381)|(0.193)|(0.283)|(0.305)|(0.290)|(0.320)|(0.224)|(0.189)|(0.205)|(0.112)|(0.131)|(0.217)|(0.181)|
|Monetary policy shock (t)|-0.284|-0.044|-0.056|-0.161|-0.006|0.179*|0.051|0.090|0.113|0.148|0.113|0.152|0.154*|0.206***|0.109|0.132*|
||(0.221)|(0.188)|(0.169)|(0.119)|(0.072)|(0.107)|(0.080)|(0.085)|(0.127)|(0.114)|(0.077)|(0.106)|(0.089)|(0.076)|(0.093)|(0.079)|
|Constant|-4.157***|-2.942***|-2.779***|-2.454***|-2.315***|-2.200***|-2.001***|-2.095***|-2.011***|-1.859***|-1.811***|-1.789***|-1.629***|-1.619***|-1.550***|-1.465***|
||(0.344)|(0.218)|(0.281)|(0.241)|(0.174)|(0.157)|(0.137)|(0.127)|(0.169)|(0.133)|(0.136)|(0.147)|(0.093)|(0.128)|(0.162)|(0.202)|
|Observations|847|838|829|820|811|801|791|781|771|761|751|741|731|721|711|701|



65 

**Table A.11: Effect of Monetary Policy Shocks on HaR using with Alternative Monetary Policy Shocks.** The tables show the effect of monetary policy shocks on HaR once added to the baseline model estimation. The model is estimated at the 5th percentile of 1 quarter ahead average real GDP growth up to 16 quarters ahead. In the first table, monetary policy shocks are constructed as in Cieslack and Pang (2021) for a subsample of advanced economies. Shocks are available from the authors for four leading central banks—the Federal Reserve Bank, the European Central Bank, the Bank of England, and the Bank of Japan. In the second table, monetary policy shocks are constructed following the approach described in Nakamura and Steinsson (2018) for the United States. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

AEs Sub-Sample: Monetary policy shocks based on Cieslak and Pang (2021) 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.250***|1.077***|0.941***|0.962***|0.788***|0.688***|0.690***|0.672***|0.603***|0.515***|0.444***|0.321***|0.310***|0.273**|0.225*|0.139|
||(0.275)|(0.119)|(0.170)|(0.117)|(0.145)|(0.120)|(0.134)|(0.111)|(0.115)|(0.089)|(0.134)|(0.100)|(0.082)|(0.112)|(0.127)|(0.091)|
|GDP growth (t)|0.190|0.086|-0.018|-0.073|-0.012|0.002|0.040|-0.022|0.008|0.046|0.050|0.070|0.086|0.112|0.074|0.111|
||(0.181)|(0.225)|(0.203)|(0.249)|(0.244)|(0.176)|(0.136)|(0.127)|(0.115)|(0.105)|(0.093)|(0.129)|(0.133)|(0.146)|(0.179)|(0.167)|
|House price misalignment (t)|-0.271|-0.517***|-0.667***|-0.720***|-0.864***|-0.926***|-0.933***|-0.941***|-0.868***|-0.863***|-0.897***|-0.892***|-0.918***|-0.873***|-0.901***|-0.878***|
||(0.177)|(0.175)|(0.175)|(0.213)|(0.151)|(0.140)|(0.163)|(0.119)|(0.090)|(0.100)|(0.072)|(0.100)|(0.087)|(0.072)|(0.088)|(0.076)|
|Financial condition index (t)|-0.723***|-0.308*|-0.268|-0.178|-0.045|-0.054|-0.055|0.060|0.060|0.088|0.098|0.118|0.136**|0.146**|0.142***|0.155***|
||(0.252)|(0.175)|(0.195)|(0.204)|(0.127)|(0.081)|(0.068)|(0.112)|(0.075)|(0.101)|(0.064)|(0.104)|(0.058)|(0.069)|(0.046)|(0.053)|
|Credit boom (t)|0.235|-0.242|-0.444|-0.219|-0.266|-0.217|-0.293|-0.468*|-0.447***|-0.516**|-0.375*|-0.338|-0.290**|-0.223*|-0.111|-0.087|
||(0.399)|(0.357)|(0.449)|(0.430)|(0.415)|(0.267)|(0.288)|(0.266)|(0.156)|(0.212)|(0.200)|(0.207)|(0.131)|(0.132)|(0.160)|(0.143)|
|Alternative monetary policy shocks (t)|-0.036|-0.158|-0.171***|-0.166***|-0.164***|-0.137|-0.141|-0.022|-0.125|-0.010|0.003|-0.001|-0.019|-0.020|-0.020|-0.036|
||(0.273)|(0.130)|(0.057)|(0.056)|(0.063)|(0.166)|(0.106)|(0.115)|(0.091)|(0.106)|(0.101)|(0.103)|(0.073)|(0.076)|(0.049)|(0.080)|
|Observations|767|766|755|744|733|722|711|700|689|678|667|656|645|634|623|612|



66 

**Table A.11: Effect of Monetary Policy Shocks on HaR using with Alternative Monetary Policy Shocks (Cont’d).** 

United States: Monetary policy news shocks based on Nakamura and Steinsson (2018) 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|2.205***|1.999***|1.462***|1.357**|1.191**|0.913***|0.732*|0.647|0.647|0.412|0.370|0.345|0.350|0.356*|0.353*|0.370|
||(0.255)|(0.402)|(0.422)|(0.540)|(0.466)|(0.311)|(0.410)|(0.426)|(0.557)|(0.428)|(0.308)|(0.279)|(0.257)|(0.212)|(0.209)|(0.292)|
|GDP growth (t)|-0.440|-0.595|0.210|-0.198|0.198|0.505|0.464|0.383|0.056|-0.089|-0.040|0.010|-0.085|-0.056|-0.069|0.014|
||(0.343)|(0.597)|(0.575)|(0.716)|(0.645)|(0.478)|(0.319)|(0.551)|(0.359)|(0.389)|(0.181)|(0.186)|(0.134)|(0.216)|(0.153)|(0.218)|
|House price misalignment (t)|0.306|-0.013|-0.384|-0.116|-0.232|-0.342*|-0.748***|-1.082***|-1.200***|-1.343***|-1.320***|-1.253***|-1.235***|-1.272***|-1.242***|-1.186***|
||(0.264)|(0.279)|(0.286)|(0.350)|(0.231)|(0.203)|(0.277)|(0.319)|(0.375)|(0.238)|(0.076)|(0.062)|(0.132)|(0.103)|(0.079)|(0.146)|
|Financial condition index (t)|0.278|0.236|-0.528|0.462|0.673*|0.742|0.483|0.072|-0.194|-0.342|-0.265|-0.154|-0.109|-0.131|-0.186|0.020|
||(0.519)|(0.392)|(0.345)|(0.641)|(0.394)|(0.642)|(0.548)|(0.443)|(0.575)|(0.446)|(0.173)|(0.141)|(0.219)|(0.148)|(0.192)|(0.323)|
|Credit boom (t)|-0.259|-0.338|-0.834|-1.707**|-1.698**|-1.746***|-1.457*|-1.034*|-0.578|-0.382|-0.381|-0.360|-0.330|-0.135|-0.259|-0.261|
||(0.244)|(0.495)|(0.695)|(0.727)|(0.681)|(0.569)|(0.784)|(0.550)|(0.544)|(0.423)|(0.311)|(0.329)|(0.300)|(0.260)|(0.298)|(0.302)|
|Policy news shock (t)|-0.058|0.019|-0.074|0.062|0.004|-0.104|-0.166|-0.248**|-0.192|-0.056|-0.096|-0.079|-0.052|0.006|-0.026|-0.016|
||(0.150)|(0.151)|(0.174)|(0.189)|(0.155)|(0.176)|(0.175)|(0.119)|(0.163)|(0.131)|(0.100)|(0.060)|(0.036)|(0.041)|(0.049)|(0.108)|
|Observations|67|67|66|65|64|63|62|61|60|59|58|57|56|55|54|53|



67 

### **A.2 Data Sources and Definitions** 

**Table A.12:** Country Coverage 

|**Advanc**|**ed Economi**|**es**|**Emerging **|**Market Eco**|**nomies**|
|---|---|---|---|---|---|
|Country|Start Date|End Date|Country|Start Date|End Date|
|Australia|1990q2|2017q4|Brazil|1994q4|2017q4|
|Austria|1990q3|2017q4|Chile|1992q4|2017q4|
|Belgium|1990q2|2017q4|China|1996q2|2017q4|
|Canada|1990q2|2017q4|Colombia|1994q1|2017q4|
|Denmark|1993q2|2017q4|India|2001q1|2017q4|
|Finland|1990q3|2017q4|Malaysia|1991q1|2016q4|
|France|1990q2|2017q4|Mexico|1990q2|2017q4|
|Germany|1990q2|2017q4|Russia|1996q1|2017q4|
|Hong Kong SAR|1990q2|2017q4|South Africa|1990q2|2017q4|
|Ireland|1990q2|2017q4|Turkey|1990q2|2017q4|
|Italy|1990q3|2017q4||||
|Japan|1990q2|2017q4||||
|Korea|1990q2|2017q4||||
|Netherlands|1990q2|2017q4||||
|New Zealand|1990q2|2017q4||||
|Norway|1990q3|2017q4||||
|Singapore|1998q2|2017q4||||
|Spain|1990q2|2017q4||||
|Sweden|1990q2|2017q4||||
|Switzerland|1990q2|2017q4||||
|United Kingdom|1990q2|2017q4||||
|United States|1990q2|2017q4||||



Note: Data coverage is limited by the joint availability of all variables in the baseline model. 

68 

**Table A.13:** Data Sources 

|**Variable**|**Description**|Source|
|---|---|---|
|Capital Flow Measures|Real estate infow restrictions and overall infow restric-<br>tions|Fernández and others (2016); IMF<br>staf calculations|
|Capital Flows|Foreign direct investment, portfolio, and other capital<br>fows at quarterly frequency|IMF, Balance of Payments Statis-<br>tics database; IMF staf calcula-<br>tions|
|Credit Growth|Percent change in the depository corporations’ claims on<br>the private sector|Bank<br>for<br>International<br>Settle-<br>ments;<br>Haver Analytics;<br>IMF,<br>International Financial Statistics<br>database|
|Credit-to-GDP Booms|Dummy for credit-to-GDP boom, as defned in Jordà and<br>Taylor (2016)|Jordà and Taylor (2016)|
|Credit-to-GDP Ratio|Total credit provided to the private nonfnancial sector<br>by domestic money banks as a share of GDP|Bank<br>for<br>International<br>Settle-<br>ments; Haver Analytics|
|Financial Conditions In-<br>dex|For methodology and variables included in the FCI, refer<br>to Appendix 3.2 of the October 2017 Global Financial<br>Stability Report (GFSR). Positive values of the FCI in-<br>dicate tighter-than-average fnancial conditions.|IMF staf estimates|
|Global Financial Condi-<br>tions Index|Based on a PCA of all FCIs estimated; Positive values<br>of the FCI indicate tighter-than-average fnancial condi-<br>tions.<br>For methodology and variables included in the<br>FCI, refer to Appendix 3.2 of the October 2017 GFSR.|IMF, chapter 3 of the October<br>2017 GFSR.|
|Global Oil Prices|Petroleum prices, US dollar per barrel|Bloomberg Finance L.P.;<br>IMF,<br>Global Data Source database|
|Household<br>Debt-to-<br>GDP Ratio|Total credit to households and NPISH as a share of an-<br>nual GDP; frst diference|Bank<br>for<br>International<br>Settle-<br>ments; Haver Analytics|
|Macroprudential<br>Poli-<br>cies|Macroprudential policy tools at quarterly frequency|IMF Integrated Macroprudential<br>Policy Database database|
|Misalignment Measure|Standardized price to per capita GDP, price to Income,<br>price to rent, and misalignment based on fundamentals;<br>detrended using a Hodrick-Prescott flter, linear detrend-<br>ing, exponential, and recursive smoothing|Organisation for Economic Co-<br>operation<br>and<br>Development;<br>Global Property Guide; IMF staf<br>calculations|
|Monetary Policy Shocks|Identifed by regressing a country’s short-term rate on<br>a set of controls and using the residuals as the identi-<br>fed shocks. The set of controls includes contemporane-<br>ous and lagged values of infation, log GDP, log foreign<br>GDP, as well as lagged values of the short-term rate and<br>a quadratic time trend|IMF staf calculations|
|Nominal GDP|Nominal gross domestic product in purchasing-power-<br>parity dollars|IMF, World Economic Outlook<br>database|
|Real GDP|GDP at constant prices, seasonally adjusted|Haver Analytics; Organisation for<br>Economic Co-operation and De-<br>velopment;<br>IMF,<br>Global<br>Data<br>Source<br>database;<br>IMF,<br>World<br>Economic Outlook database|
|Real House Price Indices|Residential property prices (seasonally adjusted) at coun-<br>try and city levels|Bank<br>for<br>International<br>Settle-<br>ments;<br>CEIC Data Co.<br>Ltd;<br>Haver Analytics; IMF, Research<br>Department house price dataset;<br>Organisation for Economic Co-<br>operation<br>and<br>Development;<br>Thomson<br>Reuters<br>Datastream;<br>IMF staf calculations|
|Real<br>House<br>Price-to-<br>Income Ratio|Real house prices as a share of disposable income|Haver Analytics; IMF staf esti-<br>mates|
|Real<br>House<br>Price-to-<br>GDP per Capita Ratio|Real house prices as a share of GDP per capita|Haver Analytics; Organisation for<br>Economic Co-operation and De-<br>velopment;<br>IMF,<br>Global<br>Data<br>Source<br>database;<br>IMF,<br>World<br>Economic Outlook database|
|Residential Investment|City-specifc residential investment; scaled by regional<br>GDP, seasonally adjusted|Haver Analytics|
|Short-Term Nominal In-<br>terest Rate|Three-month treasury bill or interbank rate|Bloomberg Finance L.P.; Haver<br>Analytics;<br>Thomson<br>Reuters<br>Datastream;<br>IMF staf calcula-<br>tions|
|Systemic Banking Crisis|Dummy for systemic banking crisis, as defned in Laeven<br>and Valencia (2018)|Laeven and Valencia (2018)|



69 

**Table A.14:** Summary Statistics 

||**Mean**|**St.dev.**|**p25**|**p50**|**p75**|**Min**|**Max**|
|---|---|---|---|---|---|---|---|
||||**Advance**|**d Econ**|**omies**|||
|Real House Prices (YoY)|2.23|7.42|-1.95|1.95|6.13|-40.55|46.53|
|Real House Prices (QoQ)|0.48|2.36|-0.66|0.51|1.64|-18.32|16.5|
|Real GDP Growth (YoY)|2.53|3|1.09|2.47|3.79|-9.55|29.07|
|Real GDP Growth (QoQ)|0.61|1.13|0.13|0.6|1.04|-7.28|20.41|
|Total Credit to GDP|160.2|47.5|125.6|154.2|187.5|62|398.5|
|Misalignment|0|0.14|-0.09|0|0.08|-0.55|0.5|
|FCI|0.15|0.89|-0.44|0.01|0.53|-3.33|4.15|
|FCI ex house prices|0|0.81|-0.53|-0.11|0.33|-2.24|4.02|
|Credit boom|0.49|0.5|0|0|1|0|1|
|||**Eme**|**rging M**|**arket E**|**conom**|**ies**||
|Real House Prices (YoY)|2.78|8.6|-1.38|2.32|6.39|-25.87|67.48|
|Real House Prices (QoQ)|0.63|3.02|-0.86|0.54|2.11|-26.04|20.6|
|Real GDP Growth (YoY)|4.57|4.2|2.28|4.73|7.37|-12.53|16.76|
|Real GDP Growth (QoQ)|1.09|1.59|0.4|1.15|1.94|-10.58|7.52|
|Total Credit to GDP|69.5|40.2|39.8|58.5|95.9|14.1|213.4|
|Misalignment|0|0.14|-0.08|-0.01|0.07|-0.4|0.47|
|FCI|-0.14|0.79|-0.65|-0.16|0.32|-5.14|3.13|
|FCI ex house prices|-0.01|0.76|-0.45|-0.01|0.43|-3.82|3.15|
|Credit boom|0.5|0.5|0|0|1|0|1|



Note: The table shows the summary statistics of main variables across panel of advanced economies (AE) and emerging market economies (EM). AE sample size = 2384 quarterly observations. EM sample size = 960 quarterly observations. St.dev. = standard deviation; p25, p50 and p75 are the 25th, 50th (median) and 75th percentile of the distribution; Min = minimum and Max = maximum. 

### **A.3 Additional Decomposition of HaR at Selected Horizons** 

The figures below show the decomposition of estimated HaR at selected forecasting horizons into contributions of past house prices, financial conditions, real GDP growth, house price misalignment, and credit boom. Plots show one-quarter ahead, two-years ahead and three-years ahead HaR, respectively. The (negative) constant term is not shown. 

70 

**United States: One-Quarter HaR Decomposition** (Percentage points, 5th percentile) 



**United States: Two-Years HaR Decomposition** (Percentage points, 5th percentile) 



**Figure A.12: Factors Affecting House-Prices-at-Risk in the United States at selected forecasting horizons** . The Figure shows the decomposition of the estimated annualized HaR at the 5th percentile into contributions of past house prices, financial conditions, real GDP growth, house price misalignment, and credit boom. The top panel shows the decomposition for the United States’ one-quarter-ahead HaR and bottom panel the decomposition of two-years-ahead HaR. The (negative) constant term is not shown. 

71 

**United States: Three-Years HaR Decomposition** (Percentage points, 5th percentile) 



**Figure A.13: Factors Affecting House-Prices-at-Risk in the United States at selected forecasting horizons** . The Figure shows the decomposition of the estimated three-years-ahead annualized HaR at the 5th percentile into contributions of past house prices, financial conditions, real GDP growth, house price misalignment, and credit boom. The (negative) constant term is not shown. 

72 

### **A.4 Additional Robustness Tests** 

**Table A.15: Alternative Panel Quantile Estimator Based on Powell (2022).** The tables report the estimated coefficients from the baseline HaR model using an alternative estimation strategy based on Powell (2022) to test the robustness of our baseline estimator. The model is estimated at the 5th percentile of 1 quarter ahead average house price growth up to 16 quarters ahead. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

##### Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.354***|1.275***|0.969***|0.900***|0.762***|0.635***|0.474***|0.555***|0.398***|0.514***|0.412***|0.392***|0.356***|0.279***|0.198**|0.249***|
||(0.139)|(0.151)|(0.133)|(0.181)|(0.190)|(0.141)|(0.161)|(0.169)|(0.152)|(0.083)|(0.082)|(0.098)|(0.093)|(0.075)|(0.087)|(0.073)|
|GDP growth (t)|0.255***|0.149*|0.052|-0.046|-0.086|-0.071|-0.057|-0.101|-0.079|-0.062|-0.011|-0.026|-0.035|-0.022|-0.042|-0.034|
||(0.025)|(0.090)|(0.072)|(0.158)|(0.087)|(0.091)|(0.065)|(0.063)|(0.123)|(0.059)|(0.056)|(0.049)|(0.051)|(0.055)|(0.042)|(0.055)|
|House price misalignment (t)|-0.459***|-0.568***|-0.670**|-0.856***|-0.931***|-1.059***|-1.157***|-1.060***|-0.996***|-0.908***|-0.853***|-0.785***|-0.830***|-0.926***|-0.757***|-0.781***|
||(0.104)|(0.220)|(0.268)|(0.208)|(0.226)|(0.176)|(0.221)|(0.155)|(0.166)|(0.129)|(0.103)|(0.119)|(0.106)|(0.113)|(0.140)|(0.144)|
|Financial condition index (t)|-0.470***|-0.365**|-0.254|-0.210|-0.133|-0.107|-0.098|-0.116|-0.110|-0.060|-0.029|-0.056|-0.016|-0.008|0.028|0.036|
||(0.112)|(0.154)|(0.182)|(0.143)|(0.133)|(0.078)|(0.101)|(0.086)|(0.107)|(0.058)|(0.051)|(0.059)|(0.048)|(0.049)|(0.057)|(0.057)|
|Credit boom (t)|-0.092|-0.220|-0.249|-0.351|-0.151|-0.070|-0.009|-0.061|-0.028|-0.111|-0.092|-0.111|-0.088|-0.044|-0.100|-0.134*|
||(0.142)|(0.237)|(0.221)|(0.280)|(0.173)|(0.178)|(0.137)|(0.171)|(0.117)|(0.097)|(0.080)|(0.070)|(0.079)|(0.056)|(0.067)|(0.071)|
|Observations|2,389|2,367|2,345|2,323|2,301|2,279|2,257|2,235|2,213|2,191|2,169|2,147|2,125|2,103|2,081|2,059|



73 

##### **Table A.15: Alternative Panel Quantile Estimator Based on Powell (2022) (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.172|1.116***|0.786***|0.512***|0.398***|0.531***|0.551***|0.565***|0.401*|0.543**|0.568***|0.384|0.426*|0.385|0.388|0.366*|
||(0.979)|(0.253)|(0.159)|(0.129)|(0.121)|(0.151)|(0.142)|(0.173)|(0.222)|(0.232)|(0.202)|(0.234)|(0.255)|(0.289)|(0.276)|(0.218)|
|GDP growth (t)|0.144|-0.015|0.003|0.301|0.066|-0.087*|0.007|0.085|-0.007|0.013|0.099|-0.004|0.113|0.119|0.073|0.026|
||(0.119)|(0.150)|(0.148)|(0.444)|(0.066)|(0.048)|(0.047)|(0.130)|(0.093)|(0.047)|(0.074)|(0.065)|(0.308)|(0.271)|(0.214)|(0.122)|
|House price misalignment (t)|-0.731***|-0.763***|-0.928***|-0.892***|-1.188***|-1.143***|-1.065***|-1.067***|-1.030***|-0.858***|-0.974***|-0.996***|-1.010***|-0.987***|-0.933***|-0.902***|
||(0.109)|(0.209)|(0.116)|(0.148)|(0.190)|(0.160)|(0.144)|(0.132)|(0.151)|(0.087)|(0.109)|(0.118)|(0.159)|(0.191)|(0.099)|(0.073)|
|Financial condition index (t)|-0.333*|-0.216|-0.407|-0.641|-0.263|-0.242|-0.072|-0.161*|-0.089|-0.006|-0.058|-0.055|-0.126|-0.208|-0.178|-0.186|
||(0.185)|(0.190)|(0.312)|(0.428)|(0.182)|(0.208)|(0.116)|(0.086)|(0.110)|(0.095)|(0.106)|(0.084)|(0.100)|(0.221)|(0.296)|(0.241)|
|Credit boom (t)|-0.370*|-0.612**|-0.603*|-0.860|-0.484|-0.579*|-0.289|-0.253|-0.196|-0.221|-0.211|-0.083|-0.010|0.200|0.150|0.209|
||(0.211)|(0.264)|(0.353)|(0.532)|(0.350)|(0.314)|(0.249)|(0.226)|(0.183)|(0.141)|(0.132)|(0.141)|(0.150)|(0.211)|(0.114)|(0.179)|
|Observations|948|938|928|918|908|898|888|878|868|858|848|838|828|818|808|798|



74 

**Table A.16: Alternative Panel Quantile Estimator Based on Machado and Silva (2019).** The tables report the estimated coefficients from the baseline HaR model using an alternative estimation strategy based on Machado and Silva (2019) to test the robustness of our baseline estimator. The model is estimated at the 5th percentile of 1 quarter ahead average house price growth up to 16 quarters ahead. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.600***|1.428***|1.132***|0.917***|0.768***|0.641***|0.574***|0.522***|0.493***|0.447***|0.408***|0.378***|0.349***|0.323***|0.288***|0.263***|
||(0.168)|(0.167)|(0.151)|(0.133)|(0.117)|(0.104)|(0.091)|(0.084)|(0.075)|(0.066)|(0.061)|(0.056)|(0.054)|(0.050)|(0.048)|(0.044)|
|GDP growth (t)|0.226*|0.152|0.082|0.007|-0.026|-0.029|-0.037|-0.016|-0.020|-0.004|0.007|0.011|-0.006|-0.013|-0.019|-0.017|
||(0.126)|(0.118)|(0.106)|(0.096)|(0.089)|(0.082)|(0.074)|(0.068)|(0.061)|(0.054)|(0.050)|(0.047)|(0.052)|(0.048)|(0.046)|(0.043)|
|House price misalignment (t)|-0.449***|-0.612***|-0.749***|-0.836***|-0.882***|-0.890***|-0.880***|-0.892***|-0.894***|-0.896***|-0.908***|-0.916***|-0.937***|-0.949***|-0.958***|-0.963***|
||(0.128)|(0.126)|(0.116)|(0.105)|(0.094)|(0.086)|(0.077)|(0.073)|(0.066)|(0.059)|(0.055)|(0.052)|(0.051)|(0.047)|(0.045)|(0.043)|
|Financial condition index (t)|-0.332***|-0.211**|-0.197**|-0.206**|-0.186**|-0.173***|-0.153***|-0.135**|-0.115**|-0.102**|-0.085**|-0.071*|-0.065*|-0.058*|-0.058*|-0.049|
||(0.105)|(0.097)|(0.089)|(0.081)|(0.072)|(0.065)|(0.058)|(0.055)|(0.049)|(0.044)|(0.041)|(0.039)|(0.038)|(0.035)|(0.034)|(0.031)|
|Credit boom (t)|-0.198|-0.393**|-0.403**|-0.293*|-0.215|-0.159|-0.141|-0.138|-0.139|-0.137|-0.145*|-0.147*|-0.146*|-0.127*|-0.121*|-0.116*|
||(0.188)|(0.178)|(0.164)|(0.150)|(0.136)|(0.125)|(0.113)|(0.108)|(0.098)|(0.088)|(0.083)|(0.079)|(0.077)|(0.072)|(0.069)|(0.064)|
|Observations|2,389|2,367|2,345|2,323|2,301|2,279|2,257|2,235|2,213|2,191|2,169|2,147|2,125|2,103|2,081|2,059|



75 

**Table A.16: Alternative Panel Quantile Estimator Based on Machado and Silva (2019) (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.825***|1.079***|0.856***|0.666***|0.599***|0.472***|0.464***|0.464***|0.471***|0.458***|0.399***|0.378***|0.360***|0.343***|0.324***|0.296***|
||(0.280)|(0.230)|(0.218)|(0.191)|(0.177)|(0.160)|(0.146)|(0.131)|(0.118)|(0.114)|(0.110)|(0.107)|(0.099)|(0.092)|(0.082)|(0.079)|
|GDP growth (t)|-0.147|-0.016|0.043|0.197|0.195|0.161|0.170|0.152|0.095|0.072|0.079|0.039|0.039|0.026|0.014|0.006|
||(0.268)|(0.215)|(0.206)|(0.196)|(0.182)|(0.164)|(0.148)|(0.132)|(0.116)|(0.112)|(0.108)|(0.103)|(0.095)|(0.088)|(0.080)|(0.077)|
|House price misalignment (t)|-0.756***|-0.807***|-0.864***|-0.898***|-0.918***|-0.959***|-0.974***|-0.958***|-0.979***|-1.006***|-1.021***|-1.024***|-0.998***|-0.988***|-0.980***|-0.971***|
||(0.246)|(0.192)|(0.192)|(0.179)|(0.168)|(0.157)|(0.144)|(0.131)|(0.119)|(0.115)|(0.112)|(0.109)|(0.100)|(0.093)|(0.085)|(0.082)|
|Financial condition index (t)|-0.955***|-0.608***|-0.568***|-0.398**|-0.310**|-0.271**|-0.213*|-0.143|-0.108|-0.083|-0.070|-0.037|-0.018|-0.027|-0.038|-0.031|
||(0.242)|(0.182)|(0.173)|(0.157)|(0.145)|(0.132)|(0.120)|(0.107)|(0.096)|(0.093)|(0.089)|(0.086)|(0.080)|(0.074)|(0.067)|(0.065)|
|Credit boom (t)|-0.294|-0.671**|-0.856***|-0.837***|-0.671**|-0.548**|-0.409*|-0.317|-0.162|-0.083|0.004|0.045|0.088|0.158|0.180|0.179|
||(0.447)|(0.335)|(0.319)|(0.293)|(0.272)|(0.250)|(0.230)|(0.208)|(0.187)|(0.181)|(0.176)|(0.171)|(0.158)|(0.148)|(0.134)|(0.131)|
|Observations|948|938|928|918|908|898|888|878|868|858|848|838|828|818|808|798|



76 

**Table A.17: Baseline Estimations Excluding the Global Financial Crisis.** The tables report the estimated coefficients from the baseline house price-at-risk model, excluding the years 2008 to 2009 to test the sensitivity of the model against the Global Financial Crisis. The model is estimated at the 5th percentile of 1 quarter ahead average house price growth up to 16 quarters ahead. Panel quantile regressions are performed following the approach described in Section 3. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.232***|1.152***|0.921***|0.842***|0.801***|0.582***|0.420***|0.363***|0.356***|0.373***|0.393***|0.391***|0.379***|0.362***|0.322***|0.308***|
||(0.192)|(0.125)|(0.103)|(0.088)|(0.101)|(0.099)|(0.145)|(0.060)|(0.074)|(0.095)|(0.065)|(0.070)|(0.059)|(0.064)|(0.057)|(0.066)|
|GDP growth (t)|0.205*|0.071|0.053|-0.075|-0.167|-0.202**|-0.192***|-0.161**|-0.175*|-0.101|-0.142**|-0.136**|-0.134**|-0.156**|-0.146**|-0.160***|
||(0.108)|(0.098)|(0.068)|(0.105)|(0.106)|(0.098)|(0.066)|(0.078)|(0.094)|(0.078)|(0.063)|(0.066)|(0.053)|(0.069)|(0.073)|(0.049)|
|House price misalignment (t)|-0.405**|-0.743***|-0.773***|-0.843***|-0.900***|-0.953***|-1.032***|-0.995***|-0.961***|-0.948***|-0.915***|-0.913***|-0.939***|-0.962***|-0.966***|-0.976***|
||(0.164)|(0.124)|(0.137)|(0.085)|(0.106)|(0.096)|(0.083)|(0.064)|(0.048)|(0.035)|(0.035)|(0.050)|(0.042)|(0.051)|(0.052)|(0.034)|
|Financial condition index (t)|-0.400***|-0.334**|-0.158|-0.216**|-0.238**|-0.229**|-0.248***|-0.254***|-0.204***|-0.148***|-0.166***|-0.165***|-0.119***|-0.114**|-0.134***|-0.102*|
||(0.143)|(0.148)|(0.110)|(0.098)|(0.096)|(0.094)|(0.075)|(0.059)|(0.055)|(0.043)|(0.048)|(0.048)|(0.045)|(0.049)|(0.046)|(0.053)|
|Credit boom (t)|-0.226|-0.460**|-0.502*|-0.476**|-0.308|-0.396**|-0.433***|-0.352*|-0.344***|-0.262|-0.237**|-0.284***|-0.267**|-0.201**|-0.232***|-0.214*|
||(0.308)|(0.228)|(0.263)|(0.205)|(0.200)|(0.202)|(0.164)|(0.198)|(0.105)|(0.171)|(0.111)|(0.106)|(0.107)|(0.093)|(0.087)|(0.111)|
|Observations|2,345|2,323|2,301|2,279|2,257|2,235|2,213|2,191|2,169|2,147|2,125|2,103|2,081|2,059|2,037|2,015|



77 

##### **Table A.17: Baseline Estimations Excluding the Global Financial Crisis (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.478**|1.022***|0.633***|0.403*|0.546**|0.559***|0.522***|0.491*|0.532**|0.460***|0.461***|0.368**|0.199*|0.186**|0.207***|0.207**|
||(0.209)|(0.241)|(0.190)|(0.215)|(0.221)|(0.202)|(0.199)|(0.264)|(0.220)|(0.165)|(0.175)|(0.182)|(0.110)|(0.089)|(0.079)|(0.098)|
|GDP growth (t)|0.217|0.113|0.237|0.197|0.260***|0.125|0.181|0.157|0.131|0.155|0.210*|0.040|0.029|0.031|0.048|0.029|
||(0.388)|(0.324)|(0.243)|(0.211)|(0.098)|(0.218)|(0.145)|(0.153)|(0.134)|(0.195)|(0.117)|(0.108)|(0.081)|(0.070)|(0.097)|(0.097)|
|House price misalignment (t)|-0.588***|-0.796***|-0.788***|-0.767***|-0.845***|-0.988***|-1.003***|-1.008***|-1.037***|-1.062***|-1.054***|-1.087***|-1.048***|-1.013***|-0.990***|-1.073***|
||(0.215)|(0.209)|(0.118)|(0.131)|(0.117)|(0.081)|(0.100)|(0.105)|(0.092)|(0.086)|(0.070)|(0.093)|(0.090)|(0.102)|(0.116)|(0.101)|
|Financial condition index (t)|-0.494|-0.520***|-0.618***|-0.613***|-0.363**|-0.460**|-0.254|-0.162|-0.120|-0.033|-0.024|-0.075|-0.076|-0.081|-0.047|-0.147*|
||(0.330)|(0.198)|(0.189)|(0.233)|(0.167)|(0.183)|(0.170)|(0.168)|(0.075)|(0.083)|(0.091)|(0.080)|(0.088)|(0.062)|(0.082)|(0.083)|
|Credit boom (t)|-0.579|-0.691**|-0.937***|-1.094***|-1.057***|-1.077***|-1.028***|-0.820***|-0.529**|-0.300|-0.157|-0.006|-0.116|-0.064|-0.012|0.313|
||(0.752)|(0.325)|(0.288)|(0.252)|(0.236)|(0.390)|(0.262)|(0.313)|(0.205)|(0.255)|(0.181)|(0.165)|(0.178)|(0.225)|(0.278)|(0.231)|
|Observations|928|918|908|898|888|878|868|858|848|838|828|818|808|798|788|778|



78 

**Table A.18: Baseline model with alternative credit boom dummy.** The tables report the estimated coefficients from the baseline house priceat-risk model of the key determinants of downside risk using an alternative definition of the credit boom based on Mendoza and Terrones (2014) to test the robustness of the model. A credit boom is defined in general as an episode in which credit to the private sector grows by more than during a typical business cycle expansion. The model is estimated at the 5th percentile of 1 quarter ahead average house price growth up to 16 quarters ahead. Panel quantile regressions are performed following the approach described in Section 3. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.265***|1.117***|0.891***|0.826***|0.719***|0.516***|0.417***|0.319***|0.314***|0.351***|0.363***|0.333***|0.330***|0.299***|0.282***|0.242***|
||(0.126)|(0.097)|(0.127)|(0.102)|(0.119)|(0.103)|(0.067)|(0.112)|(0.098)|(0.089)|(0.062)|(0.072)|(0.071)|(0.063)|(0.056)|(0.037)|
|GDP growth (t)|0.193|0.077|0.058|-0.210**|-0.241***|-0.222***|-0.229***|-0.196**|-0.149|-0.123*|-0.117*|-0.092*|-0.120*|-0.121***|-0.116**|-0.102**|
||(0.158)|(0.121)|(0.071)|(0.098)|(0.072)|(0.078)|(0.059)|(0.078)|(0.098)|(0.065)|(0.061)|(0.048)|(0.065)|(0.036)|(0.050)|(0.050)|
|House price misalignment (t)|-0.528***|-0.769***|-0.781***|-0.891***|-0.981***|-0.986***|-1.012***|-1.010***|-0.963***|-0.941***|-0.943***|-0.917***|-0.916***|-0.940***|-0.952***|-0.950***|
||(0.160)|(0.180)|(0.137)|(0.102)|(0.097)|(0.112)|(0.050)|(0.047)|(0.063)|(0.041)|(0.044)|(0.047)|(0.044)|(0.041)|(0.028)|(0.031)|
|Financial condition index (t)|-0.401***|-0.229|-0.207*|-0.271***|-0.264***|-0.242***|-0.284***|-0.278***|-0.225***|-0.181***|-0.184***|-0.165***|-0.152***|-0.134***|-0.111***|-0.093**|
||(0.114)|(0.157)|(0.120)|(0.091)|(0.078)|(0.079)|(0.050)|(0.057)|(0.074)|(0.058)|(0.043)|(0.035)|(0.046)|(0.049)|(0.029)|(0.037)|
|Alternative credit boom (t)|0.385|-0.098|-0.237|-0.607***|-0.755***|-0.855***|-0.948***|-0.912***|-0.862***|-0.765***|-0.690***|-0.580***|-0.490***|-0.528***|-0.538***|-0.510***|
||(0.643)|(0.347)|(0.366)|(0.212)|(0.157)|(0.133)|(0.121)|(0.109)|(0.134)|(0.129)|(0.115)|(0.066)|(0.084)|(0.097)|(0.091)|(0.124)|
|Observations|2,389|2,367|2,345|2,323|2,301|2,279|2,257|2,235|2,213|2,191|2,169|2,147|2,125|2,103|2,081|2,059|



79 

**Table A.18: Baseline model with alternative credit boom dummy (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.550|1.199***|0.810***|0.767***|0.667***|0.772***|0.720***|0.566***|0.528***|0.505***|0.440***|0.323**|0.282***|0.284**|0.213**|0.160*|
||(0.357)|(0.199)|(0.148)|(0.212)|(0.142)|(0.264)|(0.237)|(0.187)|(0.194)|(0.173)|(0.127)|(0.131)|(0.102)|(0.118)|(0.089)|(0.095)|
|GDP growth (t)|0.170|-0.043|0.067|0.227|0.099|0.200|0.225|0.202|0.059|0.090|0.094|0.055|0.090|0.065|0.155|0.072|
||(0.290)|(0.274)|(0.220)|(0.245)|(0.183)|(0.195)|(0.214)|(0.173)|(0.107)|(0.093)|(0.099)|(0.087)|(0.062)|(0.115)|(0.111)|(0.093)|
|House price misalignment (t)|-0.864***|-0.964***|-1.056***|-1.101***|-1.181***|-1.110***|-1.117***|-1.135***|-1.101***|-1.087***|-1.033***|-1.035***|-1.010***|-0.988***|-1.027***|-0.967***|
||(0.279)|(0.178)|(0.141)|(0.095)|(0.154)|(0.102)|(0.161)|(0.119)|(0.110)|(0.094)|(0.055)|(0.067)|(0.064)|(0.060)|(0.055)|(0.056)|
|Financial condition index (t)|-0.674***|-0.686***|-0.820***|-0.748***|-0.694***|-0.547***|-0.421**|-0.260*|-0.249*|-0.097|-0.058|-0.046|-0.073|-0.063*|-0.027|-0.049|
||(0.204)|(0.179)|(0.126)|(0.184)|(0.194)|(0.187)|(0.199)|(0.153)|(0.136)|(0.075)|(0.072)|(0.074)|(0.061)|(0.037)|(0.051)|(0.055)|
|Alternative credit boom (t)|-1.318|-0.691|-1.285*|-1.236|-1.476**|-1.103|-0.795|-0.716|-0.340|-0.441|-0.176|-0.245|-0.291|-0.343*|-0.383|-0.372|
||(1.965)|(0.984)|(0.678)|(0.758)|(0.732)|(0.837)|(0.767)|(1.054)|(0.853)|(0.887)|(0.368)|(0.307)|(0.210)|(0.179)|(0.235)|(0.251)|
|Observations|963|953|943|933|923|913|903|893|883|873|863|853|843|833|823|813|



80 

**Table A.19: Baseline model with alternative financial condition index.** The tables report the estimated coefficients from the baseline house priceat-risk model of the key determinants of downside risk using an alternative construction of the financial condition index bases on a time-varying parameter vector autoregression model as in Koop and Korobilis (2014). The methodology allows for dynamic interactions between the FCIs and macroeconomic conditions that can evolve over time, and it allows for differences in starting dates for some financial indicators with a flexible estimation procedure. The model is estimated at the 5th percentile of 1 quarter ahead average house price growth up to 16 quarters ahead. Panel quantile regressions are performed following the approach described in Section 3. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.304***|1.255***|1.104***|0.964***|0.937***|0.781***|0.656***|0.570***|0.510***|0.491***|0.433***|0.459***|0.418***|0.379***|0.416***|0.426***|
||(0.115)|(0.146)|(0.172)|(0.086)|(0.142)|(0.105)|(0.091)|(0.067)|(0.074)|(0.082)|(0.056)|(0.063)|(0.098)|(0.080)|(0.086)|(0.074)|
|GDP growth (t)|0.230*|-0.043|-0.128|-0.177|-0.247*|-0.224***|-0.176|-0.131|-0.145***|-0.105|-0.085|-0.096|-0.110|-0.107|-0.178*|-0.182**|
||(0.121)|(0.097)|(0.105)|(0.119)|(0.130)|(0.070)|(0.124)|(0.092)|(0.055)|(0.093)|(0.086)|(0.060)|(0.081)|(0.085)|(0.105)|(0.085)|
|House price misalignment (t)|-0.492***|-0.555***|-0.772***|-0.858***|-0.882***|-0.893***|-0.897***|-0.866***|-0.866***|-0.898***|-0.895***|-0.857***|-0.859***|-0.873***|-0.879***|-0.895***|
||(0.120)|(0.122)|(0.122)|(0.121)|(0.171)|(0.066)|(0.124)|(0.079)|(0.039)|(0.049)|(0.044)|(0.037)|(0.042)|(0.031)|(0.048)|(0.024)|
|Alternative fnancial condition index (t)|-0.065|-0.281*|-0.265|-0.166|-0.111|-0.161**|-0.108|-0.099|-0.135|-0.138**|-0.102**|-0.129***|-0.122*|-0.114**|-0.140**|-0.152***|
||(0.109)|(0.153)|(0.164)|(0.153)|(0.131)|(0.078)|(0.104)|(0.089)|(0.083)|(0.068)|(0.041)|(0.044)|(0.063)|(0.047)|(0.063)|(0.039)|
|Credit boom (t)|-0.230|-0.152|-0.223|-0.144|-0.181|-0.195*|-0.257|-0.246*|-0.193**|-0.246**|-0.207***|-0.177*|-0.180|-0.147**|-0.102|-0.049|
||(0.237)|(0.164)|(0.144)|(0.118)|(0.194)|(0.117)|(0.193)|(0.147)|(0.081)|(0.117)|(0.048)|(0.092)|(0.111)|(0.061)|(0.081)|(0.061)|
|Observations|1,295|1,283|1,271|1,259|1,247|1,235|1,223|1,211|1,199|1,187|1,175|1,163|1,151|1,139|1,127|1,115|



81 

##### **Table A.19: Baseline model with alternative financial condition index (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.513|0.834***|0.682***|0.761***|0.813***|0.790***|0.572***|0.644***|0.536**|0.508***|0.538***|0.395***|0.275**|0.311**|0.285***|0.190**|
||(0.368)|(0.158)|(0.177)|(0.201)|(0.143)|(0.188)|(0.212)|(0.244)|(0.222)|(0.163)|(0.188)|(0.131)|(0.140)|(0.142)|(0.099)|(0.086)|
|GDP growth (t)|0.420|0.266|0.472**|0.524***|0.478***|0.431***|0.323**|0.414**|0.172|0.255**|0.221|0.097|0.250|0.184|0.125|0.207|
||(0.274)|(0.246)|(0.237)|(0.180)|(0.165)|(0.117)|(0.132)|(0.195)|(0.186)|(0.103)|(0.144)|(0.126)|(0.171)|(0.151)|(0.116)|(0.142)|
|House price misalignment (t)|-0.609**|-0.537***|-0.584***|-0.712***|-0.815***|-0.906***|-1.039***|-1.051***|-1.016***|-1.007***|-1.024***|-0.977***|-0.999***|-0.945***|-0.934***|-0.925***|
||(0.267)|(0.094)|(0.135)|(0.072)|(0.081)|(0.086)|(0.139)|(0.124)|(0.104)|(0.069)|(0.066)|(0.054)|(0.080)|(0.068)|(0.087)|(0.072)|
|Alternative fnancial condition index (t)|-0.743**|-0.605***|-0.526**|-0.451***|-0.400***|-0.162|0.066|0.083|0.129|0.227**|0.149|0.221|0.285**|0.289*|0.108|0.088|
||(0.290)|(0.166)|(0.232)|(0.095)|(0.139)|(0.107)|(0.127)|(0.207)|(0.140)|(0.103)|(0.114)|(0.146)|(0.134)|(0.154)|(0.133)|(0.137)|
|Credit boom (t)|-0.232|-0.769***|-0.944***|-1.091***|-0.863**|-0.775**|-1.047***|-0.899**|-0.679***|-0.475*|-0.406**|-0.176|-0.006|-0.152|0.129|0.071|
||(0.415)|(0.281)|(0.226)|(0.349)|(0.372)|(0.354)|(0.333)|(0.419)|(0.243)|(0.289)|(0.194)|(0.225)|(0.261)|(0.183)|(0.175)|(0.220)|
|Observations|779|771|763|755|747|739|731|723|715|707|699|691|683|675|667|659|



82 

**Table A.20: Baseline model with alternative derivation of price misalignment measure.** The tables report the estimated coefficients from the baseline house price-at-risk model of the key determinants of downside risk using Hodrick–Prescott filter on price-to-GDP per capita to construct the house price misalignment measure. The model is estimated at the 5th percentile of 1 quarter ahead average house price growth up to 16 quarters ahead. Panel quantile regressions are performed following the approach described in Section 3. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.426***|1.260***|0.951***|0.858***|0.794***|0.697***|0.674***|0.604***|0.551***|0.582***|0.539***|0.510***|0.442***|0.353***|0.301***|0.325***|
||(0.148)|(0.135)|(0.105)|(0.076)|(0.097)|(0.090)|(0.082)|(0.097)|(0.082)|(0.093)|(0.091)|(0.074)|(0.077)|(0.075)|(0.069)|(0.071)|
|GDP growth (t)|0.227***|0.123|0.096|0.026|-0.041|-0.027|-0.005|0.044|0.028|0.038|-0.018|0.012|0.047|0.101|0.121|0.109|
||(0.072)|(0.138)|(0.156)|(0.077)|(0.141)|(0.114)|(0.089)|(0.122)|(0.106)|(0.099)|(0.099)|(0.086)|(0.140)|(0.098)|(0.113)|(0.109)|
|House price misalignment - HP flter (t)|-0.345***|-0.344***|-0.323***|-0.352***|-0.359***|-0.354***|-0.340***|-0.329***|-0.307***|-0.291***|-0.281***|-0.281***|-0.254***|-0.181***|-0.201***|-0.218***|
||(0.038)|(0.048)|(0.083)|(0.040)|(0.059)|(0.030)|(0.030)|(0.039)|(0.038)|(0.036)|(0.047)|(0.056)|(0.053)|(0.043)|(0.047)|(0.028)|
|Financial condition index (t)|-0.390**|-0.403***|-0.300**|-0.354***|-0.309*|-0.206**|-0.169|-0.071|-0.072|-0.041|-0.059|-0.050|-0.023|-0.031|-0.028|-0.013|
||(0.166)|(0.120)|(0.117)|(0.105)|(0.163)|(0.103)|(0.114)|(0.137)|(0.130)|(0.060)|(0.086)|(0.084)|(0.133)|(0.093)|(0.086)|(0.069)|
|Credit boom (t)|-0.225|-0.546|-0.626***|-0.346|-0.519**|-0.431**|-0.402***|-0.471**|-0.649***|-0.622***|-0.636***|-0.499***|-0.517**|-0.482***|-0.558***|-0.403**|
||(0.427)|(0.335)|(0.183)|(0.213)|(0.256)|(0.182)|(0.119)|(0.207)|(0.177)|(0.172)|(0.202)|(0.161)|(0.229)|(0.185)|(0.142)|(0.167)|
|Observations|2,389|2,367|2,345|2,323|2,301|2,279|2,257|2,235|2,213|2,191|2,169|2,147|2,125|2,103|2,081|2,059|



83 

**Table A.20: Baseline model with alternative derivation of price misalignment measure (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.699***|1.012***|0.832***|0.619***|0.543***|0.422***|0.394**|0.313***|0.326**|0.433***|0.429***|0.439***|0.446***|0.422***|0.428***|0.464***|
||(0.253)|(0.155)|(0.180)|(0.199)|(0.171)|(0.142)|(0.159)|(0.114)|(0.127)|(0.112)|(0.078)|(0.131)|(0.117)|(0.158)|(0.113)|(0.123)|
|GDP growth (t)|0.270|0.090|0.075|0.138|0.412**|0.314*|0.269***|0.276|0.202|0.082|0.120|0.142|0.182|0.194*|0.152***|0.083|
||(0.302)|(0.241)|(0.246)|(0.221)|(0.166)|(0.173)|(0.094)|(0.221)|(0.154)|(0.135)|(0.166)|(0.198)|(0.114)|(0.113)|(0.059)|(0.105)|
|House price misalignment - HP flter (t)|-0.354|-0.267|-0.420|-0.428***|-0.397***|-0.514***|-0.525***|-0.469***|-0.496***|-0.452***|-0.412***|-0.427***|-0.383***|-0.427***|-0.419***|-0.401***|
||(0.364)|(0.258)|(0.277)|(0.129)|(0.088)|(0.092)|(0.107)|(0.116)|(0.084)|(0.095)|(0.095)|(0.086)|(0.125)|(0.089)|(0.073)|(0.065)|
|Financial condition index (t)|-0.492*|-0.451*|-0.311|-0.286|-0.196|-0.086|0.015|0.097|0.080|-0.011|0.037|0.023|0.099|-0.087|-0.150|-0.127|
||(0.274)|(0.233)|(0.241)|(0.219)|(0.195)|(0.152)|(0.163)|(0.162)|(0.166)|(0.111)|(0.110)|(0.119)|(0.105)|(0.157)|(0.170)|(0.123)|
|Credit boom (t)|-0.784|-1.185***|-1.396***|-1.686***|-1.423***|-1.470***|-1.240***|-1.150***|-0.759**|-0.705*|-0.437|-0.202|-0.347|0.090|0.125|0.132|
||(0.606)|(0.285)|(0.395)|(0.408)|(0.370)|(0.418)|(0.374)|(0.391)|(0.345)|(0.368)|(0.401)|(0.227)|(0.422)|(0.400)|(0.350)|(0.309)|
|Observations|948|938|928|918|908|898|888|878|868|858|848|838|828|818|808|798|



84 

**Table A.21: Baseline model with alternative price misalignment measure based on price-to-rent ratio.** The tables report the estimated coefficients from the baseline house price-at-risk model of the key determinants of downside risk using an alternative definition of the house prices misalignment using the price-to-rent ratio. The model is estimated at the 5th percentile of 1 quarter ahead average house price growth up to 16 quarters ahead. Panel quantile regressions are performed following the approach described in Section 3. The results from the panel quantile estimation are reported separately for the sample of advanced and emerging market economies. The variables are standardized and defined in Appendix A.2. Standard errors are bootstrapped and shown in parentheses. *** p<0.01, ** p<0.05, * p<0.1. 

Advanced Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|1.405***|1.294***|1.031***|0.948***|0.833***|0.728***|0.618***|0.635***|0.617***|0.569***|0.538***|0.525***|0.469***|0.442***|0.436***|0.387***|
||(0.129)|(0.122)|(0.083)|(0.110)|(0.129)|(0.136)|(0.134)|(0.130)|(0.111)|(0.144)|(0.110)|(0.058)|(0.061)|(0.070)|(0.058)|(0.050)|
|GDP growth (t)|0.225**|0.103|0.042|-0.082|-0.122|-0.218**|-0.132|-0.089|-0.105|-0.136|-0.104|-0.092|-0.142**|-0.152***|-0.152***|-0.114*|
||(0.112)|(0.115)|(0.121)|(0.128)|(0.104)|(0.093)|(0.101)|(0.147)|(0.137)|(0.101)|(0.116)|(0.094)|(0.070)|(0.052)|(0.045)|(0.069)|
|House price misalignment - price-to-rent (t)|-0.290*|-0.613***|-0.651***|-0.785***|-0.786***|-0.805***|-0.889***|-0.834***|-0.865***|-0.808***|-0.792***|-0.759***|-0.768***|-0.780***|-0.779***|-0.794***|
||(0.159)|(0.110)|(0.093)|(0.117)|(0.126)|(0.082)|(0.064)|(0.077)|(0.051)|(0.051)|(0.051)|(0.051)|(0.042)|(0.036)|(0.035)|(0.036)|
|Financial condition index (t)|-0.359*|-0.313*|-0.306***|-0.361***|-0.402***|-0.323***|-0.388***|-0.369***|-0.343***|-0.287***|-0.257***|-0.266***|-0.254***|-0.231***|-0.255***|-0.235***|
||(0.206)|(0.161)|(0.093)|(0.094)|(0.093)|(0.087)|(0.060)|(0.100)|(0.052)|(0.097)|(0.046)|(0.063)|(0.054)|(0.056)|(0.050)|(0.059)|
|Credit boom (t)|-0.267|-0.563**|-0.705***|-0.533***|-0.358**|-0.350**|-0.376***|-0.427***|-0.421***|-0.456**|-0.538***|-0.534***|-0.551***|-0.532***|-0.585***|-0.444***|
||(0.303)|(0.222)|(0.240)|(0.189)|(0.150)|(0.162)|(0.145)|(0.142)|(0.162)|(0.183)|(0.133)|(0.166)|(0.138)|(0.140)|(0.114)|(0.147)|
|Observations|2,340|2,318|2,296|2,274|2,252|2,230|2,208|2,186|2,164|2,142|2,120|2,098|2,076|2,054|2,032|2,010|



85 

**Table A.21: Baseline model with alternative price misalignment measure based on price-to-rent ratio (Cont’d).** 

Emerging Market Economies 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|(10)|(11)|(12)|(13)|(14)|(15)|(16)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VARIABLES|t+1|t+2|t+3|t+4|t+5|t+6|t+7|t+8|t+9|t+10|t+11|t+12|t+13|t+14|t+15|t+16|
|House price growth (t)|0.800**|1.288***|1.066***|1.202***|0.930***|0.807*|0.876**|0.901*|0.714**|0.584*|0.473|0.359|0.286|0.070|0.137|0.121|
||(0.369)|(0.312)|(0.227)|(0.305)|(0.312)|(0.440)|(0.393)|(0.491)|(0.345)|(0.309)|(0.318)|(0.261)|(0.236)|(0.315)|(0.265)|(0.232)|
|GDP growth (t)|0.037|-0.051|-0.087|-0.152|-0.030|0.046|0.227|0.181|0.226|0.192|0.089|0.162|0.327|-0.014|-0.137|-0.120|
||(0.625)|(0.506)|(0.491)|(0.286)|(0.207)|(0.303)|(0.367)|(0.340)|(0.271)|(0.479)|(0.490)|(0.456)|(0.642)|(0.388)|(0.199)|(0.348)|
|House price misalignment - price-to-rent (t)|-0.572*|-0.731***|-0.842***|-1.027***|-0.985***|-1.089***|-0.959***|-0.853***|-0.882***|-0.942***|-0.979***|-1.044***|-0.827***|-0.893***|-0.875***|-0.847***|
||(0.328)|(0.141)|(0.102)|(0.212)|(0.199)|(0.196)|(0.214)|(0.231)|(0.175)|(0.251)|(0.184)|(0.137)|(0.251)|(0.187)|(0.187)|(0.112)|
|Financial condition index (t)|-1.583**|-1.313***|-1.340***|-1.473***|-1.313***|-1.173***|-1.013**|-0.943**|-0.912***|-0.890*|-1.123**|-1.017**|-0.913*|-0.173|-0.329|-0.223|
||(0.643)|(0.372)|(0.264)|(0.340)|(0.192)|(0.355)|(0.426)|(0.408)|(0.246)|(0.459)|(0.556)|(0.423)|(0.473)|(0.372)|(0.385)|(0.163)|
|Credit boom (t)|-0.111|-0.017|-0.247|-0.225|-0.423|-0.545|-0.430|-0.284|0.016|-0.112|0.269|0.322|0.444|1.300**|1.423*|1.790*|
||(0.483)|(0.688)|(0.434)|(0.430)|(0.448)|(0.832)|(0.719)|(0.665)|(0.634)|(0.664)|(0.833)|(0.516)|(0.694)|(0.638)|(0.735)|(0.959)|
|Observations|462|455|448|441|433|424|415|406|397|388|379|370|361|352|343|334|



86 

### **A.5 Out-of-Sample Analysis: Probability Integral Transform** 

We compute the empirical cumulative distribution of the Probability Integral Transform (PIT) of the data with respect to the density forecast model to assess the optimality of density forecasts. Specifically, the PIT measures the percentage of observations that are below any given quantile for each h-step ahead forecast. If the conditional density model is correctly specified, then the probability integral transformed series should be i.i.d. U[0,1]. To test this, we divide the sample in I in-sample portions and O out-ofsample portions, such that I + O – 1 + h = T+h. 

Let the estimated conditional predictive densities _ϕt_ + _h_ be denoted as ˆ _T ϕt_ + _h_ ( _Yt_ + _h|_ Θ)<sup>Parameters of the function</sup> � � _I_ = _I_<sup>where Θ is the information set at time t.</sup> _ϕt_ + _h_ are re-estimated at each t = I, _. . ._ , T using expanding windows of I observations.<sup>22</sup> 

The PIT for a given probability density function _ϕ_<sup>ˆ</sup> _t_ + _h_ corresponds to the cumulative density distribution (CDF) of the function evaluated at _Yt_ + _h_ : 



We also compute confidence bands around the 45-degree line to account for sample uncertainty. PITs of the one-year-ahead predictive distributions, bands are computed by bootstrapping under the assumption of uniformity of the PIT. Intuitively, the closer the empirical cumulative distribution function, _zt_ + _h,_ is to the 45-degree line (i.e., the cumulative distribution of a uniform distribution), the more accurate is the model prediction. Overall, results shown in Figure A.14 confirm that the quantile regression approach generates robust predictive distributions for future house price growth, and in particular it is able to capture well downside vulnerabilities. 

> 22As described in Rossi and Sekhposyan (2017), the rolling window estimation procedure is more robust to breaks in the conditional moments of the predictive densities and allows for a better calibration of the density distribution. 

87 



<!-- Start of picture text -->
1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>HaR Model-H4<br>0.1 House Prices only<br>Theoretical and 5% Critical Values<br>0<br>0 0.2 0.4 0.6 0.8 1<br>Empirical CDF<br><!-- End of picture text -->

**Figure A.14: United States: PIT for One-Year-Ahead Real House Price Growth Predictions.** The figure shows that the PITs for the full conditional predictive distribution lie well within the confidence bands of the lower quantiles for both countries analyzed, just like the benchmark distribution conditioning only on past house prices. These results lend support to the robustness of the predictive distributions against possible misspecification. 

88 

