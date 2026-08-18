---
title: Nsafoah_Effect of conventional and unconventional monetary policy shocks on housingprices in Canada_2024
type: paper
source_pdf: raw/papers/Nsafoah_Effect of conventional and unconventional monetary policy shocks on housingprices in Canada_2024.pdf
converted: 2026-08-18
---

Journal of Housing Economics 64 (2024) 101993 



Contents lists available at ScienceDirect 

# Journal of Housing Economics 

journal homepage: www.elsevier.com/locate/jhec 



## Effect of conventional and unconventional monetary policy shocks on housing prices in Canada<sup>✩</sup> 



### Dennis Nsafoah<sup>a</sup> , Cosmas Dery<sup>b,∗</sup> 

a _Department of Economics and Finance, Niagara University, Lewiston, NY, 14109, USA_ 

b _Department of Economics and International Business, Sam Houston State University, Huntsville, TX, 77341, USA_ 

|A R T I C L E<br>I N F O|A B S T R A C T|
|---|---|
|_JEL classification:_<br>E31<br>E43<br>E52<br>E58<br>|This paper investigates the relative importance and effect of conventional and unconventional Canadian<br>monetary policy surprises on housing prices. Using a credible approach to identify structural monetary<br>policy shocks in Canada and a comprehensive Bayesian VAR model to analyze their effects on financial and<br>macroeconomic variables, we find that both conventional monetary policy and quantitative easing shocks have<br>a significant and persistent effect on housing prices in Canada. However, the inflationary effect of a quantitative|
|_Keywords:_<br>Conventional monetary policy shocks<br>Forward guidance shocks<br>Quantitative easing shocks<br>Prices<br>Output<br>Interest rates|easing shock is more pronounced than that of an easing target monetary policy surprise. Specifically, the peak<br>effect of a 25-basis point expansionary conventional monetary policy shock is a 2.30% increase in real housing<br>prices while a comparable quantitative easing surprise leads to a peak of 4.56% increase in real housing prices.<br>We conclude that expansionary monetary policy in various forms has had significant inflationary effects on<br>Canadian housing prices. But quantitative easing surprises stand out as the most prominent contributory factor<br>to the escalating Canadian real estate price. Quantitative easing impact consistently outweighs the effects of|
|Housing prices|forward guidance and conventional monetary policy shocks.|



#### **1. Introduction** 

In recent years, the relationship between monetary policy and housing prices has gained substantial attention from both academics and the general public worldwide. This significant interest can be attributed, in part, to the growing issue of housing affordability, especially in major cities of advanced economies, where prices have skyrocketed beyond the reach of average households (Ahir and Loungani, 2019). Additionally, central banks have expanded their monetary policy toolkit to include unconventional tools to stimulate the economy (Hashmi and Nsafoah, 2021), further increasing the importance of understanding the connection between monetary policy and housing prices. 

Economic theory posits that an expansionary monetary policy, often characterized by a decrease in interest rates, tends to result in increased house prices due to lower borrowing costs and heightened demand for housing. However, the actual quantitative impact of monetary policy on housing prices is not always straightforward. Existing research has produced mixed findings, with some studies showing significant effects of monetary policy on house prices, while others indicate minimal or even negligible impacts (Kuttner, 2014). These disparities could be 

attributed to various factors, such as the specific monetary policy tools employed, the methodology used to identify monetary policy shocks, the time period studied, and the countries analyzed. To contribute to the ongoing efforts at understanding how the policy actions of a central bank impact housing prices, we adopt a state-of-the-art approach to identify structural monetary policy shocks (both conventional and unconventional monetary policy surprises) and employ a Bayesian VAR model to assess the effects of monetary policy on financial and macroeconomic variables, with a specific focus on housing prices in Canada. 

The Bank of Canada (BOC) primarily adjusts the stance of monetary policy by changing its target overnight interest rate, also known as the policy rate. This rate adjustment allows the Bank to influence economic activity and inflation, although there is typically a lag in its effects. In order to stimulate the economy, the Bank will often lower the target overnight interest rate, promoting borrowing and spending. However, if the policy rate is already very low or at its lower bound, the Bank may need to employ other unconventional policy tools to achieve a more expansionary policy. 

> ✩ We would like to thank the Editor (Henry Pollakowski), Co-Editor (Daniel Hartley), and two anonymous referees for comments that greatly improved the paper. Cosmas Dery thanks the College of Business Administration of Sam Houston State University for a Summer Research Grant that provided support for this research. 

- ∗ Corresponding author. 

- _E-mail address:_ cdery@shsu.edu (C. Dery). 

https://doi.org/10.1016/j.jhe.2024.101993 

Received 28 August 2023; Received in revised form 19 March 2024; Accepted 29 March 2024 Available online 3 April 2024 1051-1377/© 2024 Elsevier Inc. All rights reserved. 

_Journal of Housing Economics 64 (2024) 101993_ 

##### _D. Nsafoah and C. Dery_ 

During the COVID-19 pandemic, major central banks around the world, including the Federal Reserve System of the United States, the European Central Bank, and the Bank of England, relied on unconventional monetary policy tools such as forward guidance and quantitative easing after hitting their effective lower bound. Similarly, the BOC deployed unconventional tools in the form of large-scale asset purchases, also known as quantitative easing, during the pandemic, marking the first time in its modern history. The program began as the ‘‘Government of Canada Bond Purchase Program’’ in March 2020 and was later expanded to include purchase of other bonds such as corporate bonds on the secondary market. At the same time, the Bank of Canada also provided periodic updates and announcements on its policy rate and future intentions, which served as forward guidance to shape the expectations of economic agents. Forward guidance was heavily used during the global financial crisis of 2007/2008 but not quantitative easing. The BOC employed both conventional and unconventional monetary tools to aid the economic recovery from the COVID-19 recession. However, the pandemic aftermath has seen a surge in inflation and a sizzling hot housing market. Inflation spiked from 2% pre-pandemic to a new record of 8.1% in June 2022, the highest rate since the Bank began targeting inflation. Additionally, the housing price index has risen by more than 20% since the pandemic’s onset, raising questions about the role and effect of these policy tools on housing prices and the macroeconomy as a whole. 

In this paper, we assess the relative importance and effectiveness of conventional and unconventional Canadian monetary policy surprises. We disentangle the effects of conventional and unconventional monetary policy shocks using external instrument identification techniques made possible through high-frequency intra-daily changes in the Overnight Index Swap (OIS) and other financial variables within a short window on BOC monetary policy related announcements dates. We then analyze their impact on macroeconomic variables and asset prices through a Bayesian structural vector autoregressive (VAR) model. Specifically, we assess the effects of conventional policy shocks, forward guidance shocks, and quantitative easing shocks on macroeconomic variables (price, output, and exchange rate). We also examine the effects of these shocks on Canadian asset prices, focusing on both financial assets (bond yields) and real assets (housing prices). 

Our paper contributes to the literature on the identification of monetary policy shocks, especially unconventional policy shocks. As noted by Barbara (2021), unconventional monetary policy tools have played and will continue to play a critical role even during normal times. There is evidence that the reaction to monetary policy during unconventional times may occur at the announcement rather than the implementation phase of the policy thus making traditional identification approaches invalid or unable to fully capture the effect of monetary policy on the economy during unconventional times (Barbara, 2021). To avert the challenges of identifying monetary policy shocks at the effective lower bound, VAR based models have relied on alternative identification approaches such as using the shadow interest rate to capture the stance of monetary policy (Krippner, 2013; Wu and Xia, 2016, 2020; MacDonald and Popiel, 2020). Others have achieved identification through heteroskedasticity (Rigobon, 2003; Wright, 2012) and highfrequency and external instruments as in Kuttner (2001), Bernanke and Kuttner (2005), Gürkaynak et al. (2005), Gertler and Karadi (2015), Rogers et al. (2018), and Stock and Watson (2018).<sup>1</sup> The other strand of the literature estimates the effect of unconventional monetary policy shocks through DSGE models as in Kulish et al. (2017), Campbell et al. (2017), Hashmi and Nsafoah (2021) and Cai et al. (2019). On DSGE models, Barbara (2021) noted that VAR-based methods are more robust to model misspecification than DSGE models but the DSGE approach gives the researcher more flexibility regarding the role of external information and the narratives on the nature of the structural changes. 

Our study employs the instrumental variable approach to identify monetary policy shocks. Specifically, we leverage on intra-daily changes in the OIS and other high frequency financial data to identify Canadian monetary surprises. An OIS is a derivative contract that allows for the swapping of fixed for flexible interest rate for a predetermined time. OIS can be used to speculate on the future path of the overnight rate, making changes in the OIS contract (within an appropriately defined window) on the day of announcement direct and surprise responses to the BOC monetary policy announcement. This approach is widely used in modern macroeconomic literature and recognized as more credible for identifying structural monetary policy shocks (Rogers et al., 2018). However, to the best of our knowledge, this is the first paper to estimate monetary policy surprises in Canada using this approach. 

In addition, this paper makes significant contribution to the limited literature on monetary policy effects on macroeconomic variables, particularly housing prices in the context of Canada. Gambacorta et al. (2014) studied the effectiveness of unconventional monetary policy using a panel of eight countries, including Canada. They relied on exogenous innovations to the central banks’ balance sheet to identify unconventional monetary policy shocks. Similarly, Rahal (2016) using sign and zero restrictions to identify unconventional monetary policy based on innovations to total asset and monetary base, found easing monetary policy increase housing prices in a panel of countries including Canada. We complement these literature by disentangling unconventional monetary policy shocks into forward guidance and quantitative easing shocks. In the Canadian context, the implementation of quantitative easing by the Bank of Canada occurred officially only during the period of the COVID-19 pandemic. Chen and Lin (2021) studied the relationship between house prices and conventional monetary policy shock for a group of countries including Canada. Their findings indicated that an expansionary monetary policy leads to heightened house prices. Our paper differs from Chen and Lin (2021) by introducing a clear differentiation between the impacts of conventional and unconventional monetary policies on housing prices. Given unconventional monetary policy tools have become an integral part of central banks’ toolkit, it becomes imperative to distinguish between their effect on macroeconomic variables. The recent utilization of both conventional and unconventional instruments by the BOC during the COVID-19 pandemic, coupled with the subsequent surge in inflation and the raising housing prices, accentuates the necessity for a comprehensive assessment of the role and consequences of these tools on housing prices and the broader macroeconomy. 

Our study is also closely related to Rosenberg (2019), who investigated the impact of conventional and unconventional monetary policy on house prices in Scandinavian countries (Sweden, Norway, and Denmark). Rosenberg (2019) relied on sign and zero restrictions on policy rates and balance sheets to identify various shocks. The study revealed that unconventional policy shocks had significant and persistent effect impacts on housing prices across these Scandinavian countries. However, our study is significantly distinct from that of Rosenberg (2019). We make a differentiation between various forms of unconventional monetary policy surprises. This distinction is facilitated by our utilization of high-frequency data related to macroeconomic and financial variables. Through an instrumental variables approach, we are able to credibly identify and analyze the effects of conventional, forward guidance, and quantitative easing shocks on Canadian housing prices, thus contributing a novel perspective to the existing body of research, particularly in the case of Canada. 

We find that conventional policy shocks have long and variable effect on prices (with peak effect occurring around 30 months after the shock) and output(with peak effect occurring about 15 months after the shock). Forward guidance shocks have minimal effects on the dynamics of output and inflation in medium to long term. While asset purchase shocks (quantitative easing), do not generate the traditional price puzzle, their effects on output and prices are generally shortlived. Conventional policy shocks impact short-term bond yields but 

> 1 See Barbara (2021) for details on these methods. 

2 

_Journal of Housing Economics 64 (2024) 101993_ 

##### _D. Nsafoah and C. Dery_ 

have no significant effect on medium to long-term bonds. On the other hand, forward guidance shocks have a significant and persistent effect on financial asset prices, affecting every segment of the yield curve. Lastly, quantitative easing (QE) shocks affect the yield curve as usually intended. 

In terms of housing price inflation, both conventional monetary policy and QE surprises have a significant and persistent effect on housing price inflation. However, we find that the housing price inflationary effect of QE at its peak (4.56%) is almost double that of conventional monetary policy easing (2.30%). The results also show that conventional and quantitative tightening will have a symmetric effect of cooling the Canadian housing market. Between March 2022 and to January 2023, the BOC implemented eight consecutive conventional policy rate increases, along with an aggressive quantitative tightening program. Over the same period, there was a notable decline in housing prices, with a deflation of eight percentage points. Our results also show that these conventional and unconventional monetary surprises are a significant driver of the variation in housing prices across Canadian provinces. 

The remainder of the paper is organized as follows. In Section 2, we discuss the data, particularly the opportunity the high frequency financial data provided for our identification of the Canadian conventional and unconventional surprises. After a description of the VAR model in Section 3, Section 4 presents the results and in Section 5, we provide an analysis of provincial housing price response to Canadian conventional and unconventional surprises. We provide a brief conclusion in Section 6. 

#### **2. The data** 

We use high frequency intra-daily data on financial variables to disentangle Canadian monetary surprises into conventional monetary policy surprises (Target surprises) and unconventional monetary policy surprises in the form of Forward Guidance (FG) and Asset Purchase surprises (Quantitative Easing (QE)). We follow the literature on instrumental variable identification of monetary surprises along the lines of Rogers et al. (2018), Gürkaynak et al. (2005), and Gertler and Karadi (2015) to identify three monetary surprises in Canada. Subsequently, we investigate the impact of these Canadian monetary surprises on macroeconomic variables and asset prices, with a particular focus on the dynamics of housing prices in Canada. In this section we provide a brief description of the variables and the sources of these data. We start with a description of the construction of the three monetary surprises: 

1. _Target Surprises (MP1)_ : Target surprises are calculated based on changes in the 1-day Overnight Index Swap (OIS) contract within a 15-minute window before the Bank of Canada’s (BOC) monetary policy announcement and up to 1 h and 45 min after the announcement.<sup>2</sup> An OIS is an over-the-counter derivative contract in which two parties agree to swap fixed and flexible interest rates for a predetermined time (Reid, 2007). The OIS market and contract can be used to speculate on the future path of the BOC overnight rate, and changes in the OIS contract (within an appropriately defined window) on the day of the announcement are directly linked to surprise responses to the BOC monetary policy announcement. For months with more than one policy announcement, we aggregate the changes within the month. The top panel of Fig. 1 shows a plot of our Target surprises series. 

> 2 In cases where data is not available within the 2-hour window of the announcement, we used the difference between the closing and opening yields on the day of the announcement. We found that when data was available for the 2-hour window, there was no significant difference between changes in the yield within the 2-hour window and the changes in closing and opening yields. 

2. _Forward Guidance surprises (FG)_ . We obtained the intra-daily changes in the 3-month OIS contract on BOC monetary policy announcement days and defined FG as the residuals of a regression of these changes on the Target surprises.<sup>3</sup> The middle plot of Fig. 1 presents the resulting forward guidance surprises, which demonstrate that the BOC heavily relied on forward guidance during the 2007/2008 global financial crisis and again during the COVID-19 pandemic. During the 2007/2008 global financial crisis, the BOC reduced their target for the overnight interest rate to its effective lower bound and relied extensively on forward guidance regarding the future path of the overnight rate. Our constructed forward guidance surprises capture this fact quite well. 

3. _Asset Purchase surprises (QE):_ We obtained the intra-daily changes in the 10-year Government of Canada Bond Futures on BOC monetary policy announcement days. We then regressed this series on the Target and Forward Guidance surprises to obtain our Asset Purchase surprises, which are shown in the last panel of Fig. 1.<sup>4</sup> Consistent with available evidence, the BOC implemented QE policy for the first time during the COVID-19 pandemic, and our recovered Asset Purchase surprises accurately depict this well-known fact with reasonable accuracy. 

We provide a summary of the sources of data used in our analysis, which can be found in Table A1 of the Appendix, along with the time period considered.<sup>5</sup> The Bank of Canada established fixed monetary policy announcement dates in December 2000 (Reid, 2007). This schedule consists of eight pre-specified dates on which policy rate decisions are announced each year. Before this change, the Bank of Canada would adjust interest rates as necessary, often with little warning or explanation.<sup>6</sup> The Bank also committed to issuing a press release on each pre-specified date, regardless of whether or not there is a policy rate change. This change in policy led to improvements in the efficiency of the Canadian money market, including the development of new financial instruments like the OIS. Since OIS data was not available until May 2002, we limit our analysis of monetary policy surprises to this period. We analyzed a total of 166 monetary policy press statements, of which 164 were on pre-specified dates and 2 were exceptions in March 2020 in response to the COVID-19 pandemic. 

> 3 Based on existing literature (for example, Rogers et al. (2018) and Swanson (2021)), one might anticipate utilizing intra-daily changes in at least the 2-year OIS contract. However, we opt for the 3-month maturity OIS contract primarily due to constraints related to data availability. Despite this limitation, we contend that in assessing the near term impact of central bank communication, the 3-month OIS contract effectively captures the market’s expectation shifts following central bank announcements. Therefore, in light of the limited data availability for longer-term contracts, the 3-month OIS offers a practical and insightful alternative for analyzing the direct effects of policy communications. 

> 4 We restrict QE surprises to periods starting from March 2020 to the end of our sample period. There were jumps in the Government of Canada Bond Futures yield before that period but they were smaller in magnitude and do not have an interpretation as representing the effects of asset purchases. The Bank of Canada announced for the first time on March 27th, 2020 that they would begin acquiring Government of Canada securities in the secondary market with a minimum of $ 5 billion per week. These purchases were going to be financed by creating reserves, which would expand the Bank’s balance sheet. We associate QE surprises with jumps associated with long-term asset purchases financed by reserve creation. 

> 5 Our data and code are available upon request. 

> 6 Each year, in October, the Bank of Canada announces the specific dates for the following year’s announcements, which typically fall in the third or fourth week of January, the first week of March, the third or fourth week of April, the last week of May, the third or fourth week of July, the last week of August, the third or fourth week of October, and the last week of November. 

3 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 



**Fig. 1.** Canadian monetary policy shocks. 



**Fig. 2.** Frequency of Monetary Policy Decisions. 

4 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 

Fig. 2 displays the frequency of various monetary policy decisions within the period of our analysis. Of the 166 statements, 120 indicated an unchanged policy rate, 28 increased the policy rate, and 18 decreased the policy rate. Additionally, 28 statements indicated the use of multiple monetary policy tools, which involve a combination of conventional changes in the policy rate and one or both unconventional monetary tools. The first instance of such a combination was in response to the global financial crisis in 2008, in a monetary policy statement released on April 21, 2009, titled ‘‘Bank of Canada lowers overnight rate target by 1/4 percentage point to 1/4 per cent and, conditional on the inflation outlook, commits to hold current policy rate until the end of the second quarter of 2010’’. Between July 2020 and October 2021, the Bank of Canada used all three major monetary policy tools in 11 policy statements.<sup>7</sup> 

In our VAR analysis, we include the 3-month, 5-year, and 10-year Canada zero-coupon bond yields, as well as the 3-month and 10-year US zero-coupon bond yields, real effective exchange rate, log consumer price index (CPI), real GDP growth rate, and real new housing price index. The Canadian zero-coupon bond yields are obtained from the Bank of Canada, while both US zero-coupon bond yields are sourced from the Federal Reserve. We obtain the effective exchange rate series, which reflects the price of a Canadian dollar relative to a weighted basket of 27 other trading partner currencies, from the Bank for International Settlements (BIS). The weights in the basket are based on trade shares. To account for inflation, we adjust the BIS nominal effective exchange rate to obtain the real effective exchange rate. CPI and GDP data are sourced from the Bank of Canada and Statistics Canada, respectively. 

We use the monthly New Housing Price Index (NHPI) for Canada, which measures changes over time in the builders’ selling prices of new residential houses, sourced from Statistics Canada.<sup>8</sup> Three variants of the index are used: one for the house price only, another for the land price only, and a third encompassing the combined value of both the land and the house. Our choice of NHPI as the indicative measure of Canadian housing market conditions is predicated by its comprehensive coverage, spanning 27 cities representing all provinces in Canada. The index’s extensive geographical and temporal span renders it invaluable for monitoring housing market trends. Importantly, the NHPI has gained adoption among economists, academics, and the general public as the de facto indicator to monitor trends in the housing market. (See Stewart (2022) for a recent use of NHPI). Alternatively, we could have used the Multiple Listing Service (MLS) Home Price Index (HPI) from the Canadian Real Estate Association (CREA). This index gauges the resale price of exiting homes in 11 major Canadian cities. However, due to its geographical constraints and limited availability only from 2005 onward, we relegate its use to supplementary robustness analysis. The VAR is run at the monthly frequency, but daily data on the zerocoupon yields and exchange rate are used to identify the structural VAR. The sample period covers January 2000 to October 2022. 

#### **3. The structural VAR model and estimation** 

#### _3.1. Structural VAR model_ 

In this subsection, we provide a brief exposition of the econometric model used, following closely the works of Stock and Watson (2012), Mertens and Ravn (2013), Gertler and Karadi (2015), and Rogers et al. (2018). The framework is a structural vector autoregressive (VAR) model that incorporates both macroeconomic and 

> 7 The first of these instances was in a statement titled ‘‘Bank of Canada will maintain current level of policy rate until inflation objective is achieved, continues program of quantitative easing’’, released on July 15, 2020, and the last was in a statement titled ‘‘Bank of Canada maintains policy rate and forward guidance, ends quantitative easing’’, released on October 27, 2021. 

> 8 See Statistics Canada Table 18-10-0205-01-0205-01 New housing price index, monthly DOI: https://doi.org/10.25318/1810020501-eng. 

high-frequency financial data. The model is identified using external instruments. 

We begin with a typical structural VAR model of the form: 



where **_𝒀 𝒕_** is an _𝑛_ ×1 vector of the macroeconomic and financial variables and **_𝑨_** is an **_𝒏_** × **_𝒏_** matrix of contemporaneous structural coefficients. **_𝑿𝒕_** − **𝟏** is an **_𝒎_** × **𝟏** vector (where **_𝒎_** = **_𝒌𝒏_** + **𝟏** ) containing a constant and **_𝒌_** lags of **_𝒀 𝒕_** and **_𝑩_** is conformable coefficient matrices. **_𝒖𝒕_** is a vector of structural shocks. Then the reduced form representation of Eq. (1) is 

**_𝒀 𝒕_** = **_𝜱𝑿𝒕_** − **𝟏** + **_𝜺𝒕_** (2) 

where **_𝜱_** = **_𝑹𝑩_** and **_𝜺𝒕_** = **_𝑹𝒖𝒕_** and **_𝑹_** = **_𝑨_**<sup>−</sup><sup>**𝟏**</sup> . We group the structural shocks in **_𝒖𝒕_** into monetary policy shock ( **_𝒖_ 𝟏** **_𝒕_** ) and the remaining shocks ( **_𝒖_**<sup>′</sup> **𝟐** **_𝒕_**<sup>).Thatis</sup><sup>**_𝒖𝒕_**ispartitionedas(</sup><sup>**_𝒖_𝟏**</sup><sup>**_𝒕_**,</sup><sup>**_𝒖_**′</sup> **𝟐** **_𝒕_**<sup>)′.Fromourhighfrequency</sup> data (described above), we derived the Target, Forward Guidance (FG), and Asset Purchases (QE) surprises which we use as instruments. In particular, let **_𝒁𝒕_** denote either the Target, FG, or QE surprises in month **_𝒕_** . Then for **_𝒁𝒕_** to be a valid instrument of the monetary policy shock, **_𝒁𝒕_** must be correlated with **_𝒖_ 𝟏** **_𝒕_** and uncorrelated with **_𝒖_**<sup>′</sup> **𝟐** **_𝒕_**<sup>.Thatis</sup><sup>**_𝒁𝒕_**must</sup> meet the canonical instrument relevance and exogeneity conditions of valid instrumental variables as follows: 



#### and 



We also follow the literature particularly (Rogers et al., 2018) in assuming that shocks to any variable of interest in **_𝒀 𝒕_** away from the Bank of Canada’s monetary policy announcement do not contribute to the jump that is attributable to the monetary news. Specifically, suppose **_𝒀 𝒕_** is an **_𝒏_** × **𝟏** subvector of **_𝒀 𝒕_** containing only the high frequency financial data and **_𝑺_** is a **_𝒏_** × **_𝒏_** selection matrix so that 

#### **_𝒀 𝒕_** = **_𝑺𝒀 𝒕_** 

If **_𝑾 𝒕_** is an **_𝒏_** × **𝟏** vector of changes in the **_𝒀 𝒕_** within the specified window of Canadian monetary policy announcement in month **_𝒕_** , then 

_𝐸_ [ **_𝒁𝒕_** ( **_𝑺𝜺𝒕_** − **_𝑾 𝒕_** )] = 0 (5) 

Together with the instrument relevance and exogeneity conditions, this assumption then implies that _𝐸_ [ **_𝒁𝒕𝜺𝒕_** ] = **_𝜶𝑹_ 𝟏** and _𝐸_ [ **_𝒁𝒕𝑾 𝒕_** ] = **_𝜶𝑺𝑹_ 𝟏** , where **_𝑹_ 𝟏** is first column of **_𝑹_** . The assumption as stated in Eq. (5) is inspired and implied by the Efficient Market Hypothesis according to which assets price already reflect all publicly available information so that the information content of **_𝒁𝒕_** cannot predict future asset price changes or could be predicted by previous asset price changes. As noted by Rogers et al. (2018), an event-study regression of **_𝑾 𝒕_** on **_𝒁𝒕_** given that Eq. (5) holds allows us to ascertain the effect of monetary policy shocks (conventional and unconventional) on asset prices and generally on other macroeconomic variables. 

As in Rogers et al. (2018), our Target surprises for Canada is a monetary policy shock scaled to reduce the 3-month Canadian government zero-coupon bond yield by 25 basis points, while Forward Guidance and Asset Purchases surprises are shocks that are generate from lowering the 5-year zero-coupon bond yield by 25 basis points. Along the lines proposed by Caldara and Herbst (2019) and Rogers et al. (2018) we estimate the VAR by Bayesian methods. Specifically, from Eq. (2) and the ensuing discussion and assumptions above, giving Gaussian assumptions, we can write : 



where **_𝜸_** = **_𝜶𝑹_ 𝟏** . With multivariate conditional normal, **_𝒁𝒕_** | **_𝜺𝒕_** _,_ **_𝑾 𝒕_** ∼ <sup>(</sup> **_𝝁𝒁_** | **_𝜺_** _,_ **_𝑾_** _,_ **_𝑽 𝒁_** | **_𝜺_** _,_ **_𝑾_** ) (6) 

5 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 

where 



and 



Following Rogers et al. (2018), we rely on uninformative priors for the parameters<sup>{</sup> **_𝜱_** _,_ **_𝜴_** _,_ **_𝑹_ 𝟏** _,̃_ **_𝝍_**<sup>}</sup> which are proportional to | **_𝜴_** |<sup>−(</sup><sup>**_𝒍_**+</sup><sup>**𝟏**)∕</sup><sup>**𝟐**</sup> and **_𝒍_** = **_𝒌_** + **_𝒏_** . Then the posterior distribution of the parameters from which draws are taken for the simulation is 







where **_𝒁_** and **_𝑾_** are the available data on **_𝒁𝒕_** and **_𝑾 𝒕_** , while **_𝝃_** ( **_𝜱_** ) = [ **_𝒀_** − **_𝑿𝜱𝑾_** ]. 

#### _3.2. Estimation_ 

This subsection provides a brief layout of the estimation procedure. In doing so, we follow closely the procedure outlined in Rogers et al. (2018). Essentially, draws from the posterior in Eq. (7) are obtained from the following simulation procedure: 

1. Draw a candidate for **_𝜴_** from an inverse - Wishart distribution and a candidate for **_𝒗𝒆𝒄_** ( **_𝑩_** ) from  ( **_𝒗𝒆𝒄_** ( **_𝑩_** ), **_𝜮_**<sup>⨂</sup> ( **_𝑿_**<sup>′</sup> **_𝑿_** )<sup>−</sup><sup>**𝟏**</sup> ) distribution. Where the **_𝑩_** is from an OLS estimator of B and ( **_𝝃_** ( **_𝑩_** )<sup>′</sup> **_𝝃_** ( **_𝑩_** ), **_𝑻_** − **_𝒍_** − **𝟏** ) are the parameters of the inverse-Wishart distribution. Define **_𝒒_** ( **_𝑩_** , **_𝜴_** ) as the proposal density with realizations of **_𝑩_**<sup>∗</sup> and **_𝜴_**<sup>∗</sup> respectively. With probability 



a proposal is accepted, otherwise keep the existing draws of **_𝑩_** and **_𝜴_** . 

2. From a random walk Metropolis-Hasting step, draw ( **_𝜸_**<sup>∗</sup> , **_𝝍_**<sup>∗</sup> ) for ( **_𝜸_** , **_𝝍_** ), that is let the proposed value for each of these parameters be the existing values plus a Gaussian shock. Using the posterior in Eq. (6), accept the proposal with probability **_<u>𝒑</u>_** ( **_𝒁_** <u>|</u> **_𝒀_** _,_ **_𝑾_** _,_ **_𝜴_** _,_ **_<u>𝜸</u>_** ∗ _,̃_ **_<u>𝝍</u>_** ∗) 

( **_𝒑_** ( **_𝒁_** | **_𝒀_** _,_ **_𝑾_** _,_ **_𝜴_** _,_ **_𝜸_** _,̃_ **_𝝍_** )<sup>_,_</sup><sup>**𝟏**</sup> ) 

3. For target surprises, let **_𝑹_ 𝟏** be **_𝜸_** , normalized to lower the 3- month yields by 25-basis points. Similarly for forward guidance and asset purchases surprises except that they are generated from lowering of the 5-year zero coupon bond yield by 25 basis points. Positive realizations of the instruments correspond to surprise contractionary policy while negative values indicate easing surprises (expansionary shocks). In the empirical section, we present results for expansionary shocks.<sup>9</sup> Given the three instruments, we identify each shock separately. 

4. Then use **_𝑹_ 𝟏** and **_𝑩_** to compute a draw for the impulse response. 

5. By repeating steps 1 to 4, we are able to trace out the posterior distribution. Similar to Rogers et al. (2018), we use 5000 draws with 1000 initial burn in. 

> 9 For brevity, we do not present results for contractionary shocks since they are symmetric. 

We define **_𝒀 𝒕_** as a vector of nine variables: 3-month, 5-year, and 10year Canada zero-coupon bond yields, the 3-month and 10-year US zero-coupon bond yields, the real effective exchange rate, log consumer price index (CPI), real GDP growth rate, and real new housing price index. The vector **_𝑾 𝒕_** comprises observed daily data on the zerocoupon yields and real exchange rates. These variables are constructed as daily changes summed over all announcement days in a month. It is important to note that when we aggregate daily data to a monthly frequency, we assume that shocks occurring early or later in the month are equivalent. The sample period for **_𝒀 𝒕_** is from January 2000 to October 2022. On the other hand, we use data from May 2002 to October 2022 for both **_𝑾 𝒕_** and **_𝒁𝒕_** , except for QE surprises, for which we have a sample period from March 2020 to October 2022. 

#### **4. Empirical results** 

In this paper, our goal is to assess the impact of different types of monetary policy surprises on financial and macroeconomic variables in Canada. We utilize high-frequency data and state-of-the-art empirical methods to distinguish between conventional monetary policy shocks (target surprises (MP1)) and unconventional monetary policy shocks, and analyze their effects on Canadian asset prices and macroeconomic variables. Specifically, we differentiate between forward guidance shocks (FG) and asset purchases (quantitative easing shocks (QE)). We present our results in the form of impulse responses that trace out the dynamic response of the variables of interest over a 60-month period. We display the Bayesian posterior median (solid line) and their corresponding 68% credibility region (blue broken lines) in the impulse responses. As noted by Rogers et al. (2018), identifying the dynamic impact of monetary policy shocks in structural VAR models is both fascinating and crucial, yet still challenging. In many situations, 95% intervals may be too wide to be useful, so it is conventional in this literature to employ 68% intervals, as demonstrated by Eichenbaum and Evans (1995), Kim and Roubini (2000), Kim (2001), Faust and Rogers (2003), and Sims and Zha (1999). 

Fig. 3 shows the response of financial asset prices to an expansionary conventional and unconventional monetary policy shocks in Canada. The first column shows the effect of target surprises which are carefully calibrated to reduce the 3-month zero coupon yield by 25 basis points. The second and third columns show the effects of forward guidance and quantitative easing surprises respectively. Both unconventional monetary policy shocks are calibrated to reduce the 5-year zero-coupon yield by 25 basis points. Conventional monetary policy shocks have no statistically significant effect on the 5-year and 10year bond yields. In contrast, forward guidance shocks have significant reductions on yields across the short, medium, and long term. Forward guidance shocks tend to be statistically significant, pronounced, and persistent, lasting for almost three years. These results suggest that forward guidance, as a monetary policy tool, has a powerful impact on financial markets, affecting every segment of the yield curve. In line with the traditional objective of QE, which is to drive down all rates at the long end of the yield curve, our QE shock significantly reduces the long-term rate for at least 30 months. The 3-month bond yield remains unaffected by the QE shock. Thus, quantitative easing flattens the yield curve by lowering long-term interest rates, as intended.<sup>10</sup> The 

> 10 Although the most common mortgage rate, the 5-year fixed-term mortgage rate, was not directly included in our baseline analysis, it is significantly connected to the 5-year government bond yield, exhibiting a correlation of approximately 0.96. Therefore, including the 5-year mortgage rate into our model would essentially replicate the effects already demonstrated by the 5- year government bond yield. In Appendix Figure A1, we illustrate how the response pattern of the 5-year mortgage rate closely mirrors that of the 5-year government bond yield, indicating parallel effects on these closely interlinked financial indicators. Our focus in this analysis, however, remains directed towards assessing the direct impact of various Canadian monetary surprises on housing prices. 

6 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 



**Fig. 3.** Response of financial assets prices to expansionary conventional and unconventional Canadian monetary policy shocks. The solid black lines are the posterior median effects of conventional monetary policy (MP1), forward guidance (FG), and asset purchases (QE) shocks while the blue dashed lines are the corresponding Bayesian 68% confidence intervals. MP1 are normalized to lower 3-month yields by 25 basis points; FG and QE surprises are normalized to lower 5-year yields by 25 basis points. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.) 

phenomenon where QE seemingly exerts a lesser effect on long-term interest rates compared to forward guidance can initially appear puzzling. Notably, the BOC has never implemented QE without accompanying it with forward guidance in any policy rate announcement.<sup>11</sup> This consistent pairing of QE with forward guidance likely leads markets to anticipate low long-term interest rates whenever forward guidance and QE are announced. Consequently, this anticipation may limit the additional impact that QE alone would have on long-term interest rates. 

Fig. 4 displays the impact of the three expansionary monetary policy surprises on selected macroeconomic variables. The first column illustrates the effect of target surprises (conventional surprises), calibrated to reduce the 3-month zero coupon yield by 25 basis points. The second and third columns show the effects of forward guidance and quantitative easing surprises, respectively, which are both calibrated to reduce the 5-year zero-coupon yield by 25 basis points. An expansionary conventional monetary policy shock generates a significant but transient price puzzle, whereas conventional monetary policy easing eventually produces a significant inflationary effect, peaking at about 30 months, with an almost 0.7 percentage point increase in prices. The inflationary tendency of conventional monetary policy easing dissipates in the long run. The results confirm the typical price puzzle that characterizes empirical results in this literature, as noted in prior studies such as Sims et al. (1986), Sims (1992), and Christiano et al. (1999). The conventional monetary policy easing generates a contemporaneous 

> 11 This is a plausible reason for the seemingly larger confidence interval for both QE and FG shocks compared to MP1. 

reduction in output growth, but over time, output growth gradually increases to about 0.78% after 18 months. Both the response of output growth and prices highlight the long lag of monetary policy effects on the economy. 

An easing forward guidance shock reduces prices and produces a similar price puzzle as in the conventional easing scenario. In the medium to long term, forward guidance shocks do not appear to have significant lasting effects on output growth, indicating that much of the impact of Canadian forward guidance is on financial markets with little persistent effect on the real economy. Our findings do not support the ‘‘forward guidance puzzle’’ commonly observed in medium-scale DSGE models, which tend to overestimate the impact of forward guidance in the macroeconomy. We find that although forward guidance lowers long-term yields, the decline is not significant enough to boost real GDP. Quantitative easing shocks do not generate a price puzzle, as they contemporaneously increase prices, but such effects are short-lived and largely non-existent in the long run. 

The third row in Fig. 4 displays the impact of monetary policy surprises on effective real exchange rates. Our findings reveal that both expansionary conventional monetary policy and quantitative easing resulted in a significant and persistent increase in the Canadian effective exchange rate. Although it may seem unusual for an expansionary monetary policy shock to result in currency appreciation, we believe that in the case of Canada, it is possible that low-interest rates increased demand for housing by both domestic and foreign residents, leading to an appreciation in the Canadian effective exchange rate. Typically, an expansionary monetary policy would lead to a depreciation in the Canadian dollar due to lower relative returns on Canadian denominated assets. However, Fig. 4 demonstrates that this is not always the case. 

7 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 







**Fig. 4.** Response of macroeconomic variables and real assets prices to expansionary conventional and unconventional Canadian monetary policy shocks. The solid black lines are the posterior median effects of conventional monetary policy (MP1), forward guidance (FG), and asset purchases (QE) shocks while the blue dashed lines are the corresponding Bayesian 68% confidence intervals. MP1 are normalized to lower 3-month yields by 25 basis points; FG and QE surprises are normalized to lower 5-year yields by 25 basis points. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.) 

One plausible explanation for the appreciation of the real exchange rate in response to expansionary monetary policy shocks is the global inflow of capital, particularly in the Canadian housing market during periods of lower interest rates. This is further supported by the ban on foreign resident ownership of Canadian residential property on January 1, 2023, which was implemented in response to the influx of foreign capital into the Canadian housing market during the COVID-19 pandemic era of low interest rates and quantitative easing. 

Additionally, conventional monetary policy easing has been found to have an impact on housing prices, as indicated in the last row of Fig. 4.<sup>12</sup> This effect is notable and long-lasting, lasting for more than three years. Similarly, quantitative easing also leads to an increase in housing prices. By lowering long-term rates, unexpected quantitative easing generates a more severe, significant, and enduring housing price 

> 12 While the primary objective of this paper is to explore the effects of both conventional and unconventional monetary policies on housing prices, it is important to note that related studies focusing on the impact of monetary policy shocks–without differentiating between conventional and unconventional types–have also underscored the significance of these shocks in housing price dynamics. Key examples include Goodhart and Hofmann (2008) and Musso et al. (2011), who highlight the pivotal role of monetary policy shocks in determining housing prices. 

inflation. Our findings indicate that a 25-basis point reduction in the 3- month zero coupon yield resulting from a conventional monetary policy shock leads to a 2.30% increase in real housing prices by the 24th month, while a 25-basis point reduction in the 5-year zero coupon yield resulting from a quantitative easing surprise leads to an 4.56% increase in real housing prices by the 36th month. At its peak, quantitative easing raises housing prices by about twice as much as the amount that target monetary policy easing does. Furthermore, our research suggests that the effect of quantitative easing on housing prices is more persistent than that of target monetary policy easing. While the effect of target monetary policy returns to zero by the 50th month, we observe that the effect of quantitative easing on housing prices remains elevated above 3% in the 60th month. This finding aligns with the results of Rosenberg (2019), which demonstrated that unconventional monetary policies exhibit more pronounced and persistent effects compared to traditional interest rate policies. 

It is worth noting that whereas FG lower the long-term interest rates relatively more when compared to QE effect on the long-term interest rates, QE demonstrates a more significant influence on house prices than FG. This difference is attributable to various mechanisms through which QE can affect the housing market, such as wealth effects and portfolio re-balancing. The implementation of QE typically boosts the prices of financial assets, which can make households feel wealthier and potentially increase their consumption, including consumption of housing. Furthermore, in response to the lower yields on securities 

8 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 







**Fig. 5.** Response of alternative housing price index to expansionary conventional and unconventional Canadian monetary policy shocks. The solid black lines are the posterior median effects of conventional monetary policy (MP1), forward guidance (FG), and asset purchases (QE) shocks while the blue dashed lines are the corresponding Bayesian 68% confidence intervals. MP1 are normalized to lower 3-month yields by 25 basis points; FG and QE surprises are normalized to lower 5-year yields by 25 basis points. 

due to QE, investors often reallocate their portfolios towards higheryielding assets like property, contributing to an increase in house prices. Therefore, while the influence of QE on long-term interest rates is somewhat moderated by the expectations set through FG, its effect on the housing market is augmented by these other factors. 

The housing price index used in Fig. 4 encompasses both house and land prices. To provide a comprehensive analysis, we investigate the impact of various monetary policy shocks on two other housing price indices: one that assesses the price of the house only and another that evaluates the price of the land only. Fig. 4 summarizes our findings on the effects of conventional and unconventional monetary policy shocks on different Canadian housing price indices. The first row of Fig. 5 mirrors the last row of Fig. 4. Although conventional expansionary monetary policy shock results in higher prices for the land, house, and the total value of the land and the house, the land price inflation is relatively less pronounced and persistent. Conventional monetary policy easing has a significant and long-lasting inflationary impact on both the house-only and the total value of the house and land indices, usually persisting for more than three years after the initial shock. On the other hand, as illustrated in Fig. 5, quantitative easing shock has the most substantial impact on housing prices in Canada, producing statistically significant and enduring housing price inflation for up to five years after the shock. At its peak effect, QE generates an increase of 4.56%, 4.82%, and 3.57% on the total real house price, real house-only price, and real land-only price, respectively. 

Our findings on the effects of monetary policy shocks on housing prices are consistent with studies conducted in other countries. 

While Del Negro and Otrok (2007) found that monetary policy shocks have a moderate effect on housing prices in the US, Bjørnland and Jacobsen (2010) concluded that housing prices in Norway, Sweden, and the UK respond immediately and significantly to monetary policy shocks. As noted by Jordà et al. (2016), asset price booms often result from expansionary monetary policy. Our results, as shown in Fig. 5, generally support this conclusion. In particular, the heated housing market in Canada could be attributed to expansionary monetary policy, either conventional or unconventional in the form of quantitative easing. We recognize the potential influence of the shift towards remote work on housing prices during the COVID-19 pandemic. However, our construction of QE shocks, derived from intra-daily fluctuations in 10-year Government of Canada Bond Futures on BOC policy announcement days and purged of other monetary policy effects, ensures that our findings on QE impacts are robust. The specificity of our data minimizes the likelihood that the broader trend towards remote work significantly affects our QE shock measures, allowing us to attribute observed housing price variations confidently to QE activities. 

In Fig. 6, we compare the responses of housing prices to three types of easing monetary policy shocks. The scale is the same in each subplot to allow for easier comparison. The top panel of Fig. 6 shows the response of various housing price indicators to conventional monetary policy shock (MP1), forward guidance shock (FG), and quantitative easing shock (QE). Both MP1 and QE cause more inflation in the houseonly index, while the next most responsive is the combined value of the house and land (total index). The least responsive is the index for the value of the land. FG tends to have a short-lived negative effect 

9 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 



**Fig. 6.** Comparative responses of housing price index to expansionary conventional and unconventional Canadian monetary policy shocks. 

**Table 1** 

Test of significant differences between impulse responses of the various shocks. This is a t-test testing the null hypothesis of the difference between the impulse response of any two shocks is on average indistinguishable. 

|Null: Mean responses are equal|p-value|
|---|---|
|A. Real house price index - Total||
|MP1 and QE|0.000|
|MP1 and FG|0.061|
|QE and FG|0.000|
|B. Real house price index - House||
|MP1 and QE|0.000|
|MP1 and FG|0.075|
|QE and FG|0.000|
|C. Real house price index - Land||
|MP1 and QE|0.000|
|MP1 and FG|0.008|
|QE and FG|0.000|



on all measures of residential property inflation. In the bottom panel of Fig. 6, we show that QE has the largest effect on housing price inflation in Canada, regardless of the housing price indicator used. Table 1 provides a test of statistically significant differences, which is a t-test that examines the null hypothesis that the impulse response of any two shocks is, on average, indistinguishable. We reject the null hypothesis in all cases at conventional 10% significance level for all indicators of housing prices. 

As mentioned earlier in the data section, the new house price index (NHPI) developed by Statistics Canada measures fluctuations in the selling prices of newly built residential houses over time. In supplementary robustness analyses, we utilize the Multiple Listing Service (MLS) Home 

Price Index (HPI) provided by the Canadian Real Estate Association (CREA). As previously outlined, we show a preference for the NHPI due to its comprehensive coverage, spanning 27 cities representing all provinces in Canada, while the MLS HPI only covers 11 major Canadian cities. Additionally, the MLS HPI data is accessible only from January 2005, whereas the NHPI allows us to extend our sample period back to January 2000. 

The results of the MLS HPI are presented in Appendix Figures A2 and A3. Figure A2 shows the impulse responses of the MLS HPI to expansionary conventional monetary policy, forward guidance, and quantitative easing shocks. On the other hand, Figure A3 provides a direct comparative view of these responses. By employing this alternative measure, which encompasses both newly constructed and existing home sales (albeit within a shorter time-frame and limited geographical coverage), we show that our main conclusion that quantitative easing shocks have the most pronounced and persistent effect on Canadian housing prices is preserved and invariant. 

Drawing upon the previously discussed impulse responses and the results of the statistical significance test, we conclude that expansionary monetary policy in various forms have had significant inflationary effect on the Canadian housing prices. Further, quantitative easing surprise stands out as the most prominent contributory factor to escalating Canadian real estate price. This impact consistently outweighs the effects of forward guidance and conventional monetary policy shocks. 

#### **5. Provincial heterogeneity** 

As shown in Fig. 7, real total housing price index in Canada has increased by 31% from 2002 to 2023. Newfoundland and Labrador also witnessed a similar real increase of 31% over the same period. 

10 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 



**Fig. 7.** Total real housing price index. All values are relative to 2002 January. 

However, other provinces experienced a range of above the national average increases, with Manitoba, Saskatchewan, Quebec, Alberta, and Ontario experiencing real housing price increases of 89%, 53%, 50%, 46%, and 32%, respectively. British Columbia and Nova Scotia had moderate real price increases of 11% and 9%, respectively, while Prince Edward Island and New Brunswick witnessed reductions of 14% and 5%, respectively. These figures suggest that there is significant variation in real housing prices across Canadian provinces. To understand how conventional and unconventional monetary policy shock has contributed the provincial variation in housing price inflation, we reestimate the model using provincial housing price indices and assessing the impact of both conventional and unconventional monetary policy shocks on province-level housing price inflation. 

For brevity, we focus solely on the total housing price index reporting the median impulse response for each province. Real provincial housing price index are obtained by adjusting each provincial total housing price index using the provincial consumer price index. The responses are presented in Fig. 8, which depicts the results for Atlantic Canada (New Brunswick, Newfoundland and Labrador, Nova Scotia, and Prince Edward Island), Central Canada (Ontario and Quebec), and Western Canada (Manitoba, Saskatchewan, Alberta, and British 

Columbia). Overall, Fig. 8 depicts Conventional and unconventional monetary policy shocks as contributing factor to the variation in provincial housing prices. With the exception of Prince Edward Island, most provinces experience higher housing price inflation as a result of conventional expansionary monetary policy shocks. Conversely, a national easing forward guidance shock leads to housing price deflation in British Columbia and Alberta, whereas Ontario and Manitoba experience housing price inflation as a result of this forward guidance shock. Additionally, quantitative easing shocks generate housing price inflation in all provinces in Central and Western Canada while the responses in Atlantic Canada to quantitative easing shocks is mostly mixed. We observe a zero effect of QE in Newfoundland and Labrador whereas New Brunswick and Nova Scotia experience a positive but short-lived effect that quickly decay to zero statistically. Prince Edward Island on the hand had a negative effect for less than a year. 

The variation in how monetary policy surprises impact housing prices across different provinces is primarily attributed to distinct economic and housing market characteristics within each province. For instance, in our observations, Ontario, with its highly diversified economy, experienced a relatively modest increase in housing prices following an expansionary monetary policy shock. Diverse economies 

11 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 



**Fig. 8.** Provincial real total housing price index response to expansionary conventional and unconventional Canadian monetary policy shocks. 

tend to exhibit less sensitivity to such shocks. When monetary policy eases and interest rates decline, interest-sensitive sectors like construction may experience growth. Conversely, sectors less influenced by interest rates, such as technology or services, might not undergo significant changes, thereby mitigating the broader economic impact of the policy shift. 

In general, these findings emphasize the varying effects of conventional and unconventional monetary policy shocks at the provincial level, offering some explanation as to why certain provinces have experienced significantly higher housing price inflation following the pandemic. Similar results are presented for the house-only and landonly indices in Appendix Figure A4 and Figure A5, respectively. In addition, individual provincial median impulse responses with their corresponding 68% credibility region are provided in Appendix Figure A6 to A15. Overall, this section primarily outlines the differential impacts of monetary policy shocks on housing prices across Canadian provinces, suggesting that future research could delve into the specific attributes driving these diverse responses. 

#### **6. Conclusion** 

We investigate the relationship between monetary policy surprises and housing price in Canada by using changes in yields within short intervals around Bank of Canada’s monetary policy announcements as 

an external instrument. Using a Bayesian structural vector autoregression (VAR) model, we analyze the impact of conventional and unconventional monetary policy shocks on financial and macroeconomic variables. In particular, we disentangle the effects of conventional monetary policy surprises, forward guidance surprises, and quantitative easing shocks using external (instrumental variables) identification techniques made possible through high-frequency intra-daily changes in overnight index swap (OIS) and other financial variables. Our approach is widely used and recognized as more credible for identifying structural monetary policy shocks. 

Our analysis shows that conventional monetary policy shocks impact short-term bond yields, but have no significant effect on medium to long-term bonds. In contrast, forward guidance shocks have a significant and lasting impact on financial asset prices, affecting every segment of the yield curve. Quantitative easing shocks significantly reduce long-term bond yields, flattening the yield curve as intended. On CPI and output, we find that conventional policy shocks have long and variable effect on CPI (with peak effect occurring around 30 months after the shock) and output(with peak effect occurring about 15 months after the shock). Forward guidance surprises do not produce a significant dynamic effect on output and inflation over the medium to long term. While asset purchase surprises (quantitative easing) do not generate the typical price puzzle, their effects on output and prices are generally short-lived. Additionally, both expansionary conventional 

12 

_Journal of Housing Economics 64 (2024) 101993_ 

##### _D. Nsafoah and C. Dery_ 

monetary policy and quantitative easing shocks lead to a significant and persistent increase in the Canadian effective exchange rate. 

One of the most important findings of our study is that both conventional monetary policy and asset purchase shocks have a significant and persistent effect on housing price inflation. However, the inflationary effect of an asset purchase shock is more pronounced than that of a target monetary policy surprise. In fact, at its peak, quantitative easing raises housing prices by 4.56%, almost double the amount that target monetary policy easing does (2.30%). We conclude that expansionary monetary policy in various forms have had significant inflationary effect on the Canadian housing prices. Further, quantitative easing surprise stands out as the most prominent contributory factor to escalating Canadian real estate price. This impact consistently outweighs the effects of forward guidance and conventional monetary policy shocks. Our results also highlight conventional and unconventional monetary policy shocks as a contributing factor of the differences in housing price inflation among Canadian provinces. 

The implications of our findings for the Bank of Canada are significant, especially in light of the challenges faced by many central banks in returning inflation to target while avoiding a significant decline in housing prices and the wealth of citizens. Our study suggests that the Bank of Canada can navigate this challenge by increasing the policy rate without a significant shrinkage of its balance sheet to preserve the value of housing prices in Canada. 

While Our primary focus in this study was on the demand-side impacts of monetary policy, supply-related elements in the housing market, such as construction costs and land availability, could exert considerable influence on housing prices. Our paper’s analysis implicitly assumes the influence of underlying supply conditions on how monetary policy affects housing prices. Future research endeavors could aim to integrate supply-side considerations for a more complete understanding of how housing markets respond to monetary policy measures in the present of supply-sided constraints. 

#### **Funding information** 

Cosmas Dery acknowledges and thanks the College of Business Administration (COBA) of Sam Houston State University for a Summer Research Grant that provided support for this research. COBA had no involvement in the research design, collection and analysis of data, methodology and interpretation of results/conclusions of the paper and the decision to submit the paper for publication. 

#### **CRediT authorship contribution statement** 

**Dennis Nsafoah:** Writing – review & editing, Methodology, Formal analysis, Data curation, Conceptualization. **Cosmas Dery:** Writing – review & editing, Writing – original draft, Methodology, Formal analysis, Data curation. 

#### **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### **Data availability** 

Data will be made available on request. 

#### **Appendix A. Supplementary data** 

Supplementary material related to this article can be found online at https://doi.org/10.1016/j.jhe.2024.101993. 

#### **References** 

Ahir, H., Loungani, P., 2019. Managing house price booms: Evolution of IMF surveillance and policy advice. In: Hot Property: The Housing Market in Major Cities. Springer International Publishing, pp. 83–95. 

Barbara, R., 2021. Identifying and estimating the effects of unconventional monetary policy: How to do it and what have we learned? Econom. J. 24 (1), C1–C32. 

Bernanke, B.S., Kuttner, K.N., 2005. What explains the stock market’s reaction to Federal Reserve policy? J. Finance 60 (3), 1221–1257. Bjørnland, H.C., Jacobsen, D.H., 2010. The role of house prices in the monetary policy transmission mechanism in small open economies. J. Financ. Stab. 6 (4), 218–229. Cai, M., Del Negro, M., Giannoni, M.P., Gupta, A., Li, P., Moszkowski, E., 2019. DSGE forecasts of the lost recovery. Int. J. Forecast. 35 (4), 1770–1789. 

Caldara, D., Herbst, E., 2019. Monetary policy, real activity, and credit spreads: Evidence from Bayesian proxy SVARs. Am. Econ. J.: Macroecon. 11 (1), 157–192. Campbell, J.R., Fisher, J.D., Justiniano, A., Melosi, L., 2017. Forward guidance and macroeconomic outcomes since the financial crisis. NBER Macroecon. Annu. 31 (1), 283–357. 

Chen, S.-S., Lin, T.-Y., 2021. Revisiting the link between house prices and monetary policy. BE J. Macroecon. 22 (2), 481–515. 

Christiano, L.J., Eichenbaum, M., Evans, C.L., 1999. Monetary policy shocks: What have we learned and to what end? In: Handbook of Macroeconomics, vol. 1, Elsevier, pp. 65–148. Del Negro, M., Otrok, C., 2007. 99 Luftballons: Monetary policy and the house price boom across US states. J. Monetary Econ. 54 (7), 1962–1985. Eichenbaum, M., Evans, C.L., 1995. Some empirical evidence on the effects of shocks to monetary policy on exchange rates. Q. J. Econ. 110 (4), 975–1009. 

Faust, J., Rogers, J.H., 2003. Monetary policy’s role in exchange rate behavior. J. Monetary Econ. 50 (7), 1403–1424. 

Gambacorta, L., Hofmann, B., Peersman, G., 2014. The effectiveness of unconventional monetary policy at the zero lower bound: A cross-country analysis. J. Money Credit Bank. 46 (4), 615–642. 

Gertler, M., Karadi, P., 2015. Monetary policy surprises, credit costs, and economic activity. Am. Econ. J.: Macroecon. 7 (1), 44–76. Goodhart, C., Hofmann, B., 2008. House prices, money, credit, and the macroeconomy. Oxf. Rev. Econ. Policy 24 (1), 180–205. Gürkaynak, R.S., Sack, B., Swanson, E.T., 2005. Do actions speak louder than words? The response of asset prices to monetary policy actions and statements. Int. J. Central Bank. 1, 55–93. 

Hashmi, A.R., Nsafoah, D., 2021. International Spillovers of Conventional versus New Monetary Policy. University of Calgary, Department of Economics. Jordà, Ò., Schularick, M., Taylor, A.M., 2016. Sovereigns versus banks: Credit, crises, and consequences. J. Eur. Econom. Assoc. 14 (1), 45–79. Kim, S., 2001. International transmission of US monetary policy shocks: Evidence from VAR’s. J. Monet. Econ. 48 (2), 339–372. 

Kim, S., Roubini, N., 2000. Exchange rate anomalies in the industrial countries: A solution with a structural VAR approach. J. Monet. Econ. 45 (3), 561–586. Krippner, L., 2013. Measuring the stance of monetary policy in zero lower bound environments. Econom. Lett. 118 (1), 135–138. Kulish, M., Morley, J., Robinson, T., 2017. Estimating DSGE models with zero interest rate policy. J. Monetary Econ. 88, 35–49. 

Kuttner, K.N., 2001. Monetary policy surprises and interest rates: Evidence from the fed funds futures market. J. Monet. Econ. 47 (3), 523–544. 

Kuttner, K.N., 2014. Low interest rates and housing bubbles: still no smoking gun. In: The Role of Central Banks in Financial Stability: How Has It Changed, vol. 30, pp. 159–185. 

MacDonald, M., Popiel, M.K., 2020. Unconventional monetary policy in a small open economy. Open Econ. Rev. 31 (5), 1061–1115. 

Mertens, K., Ravn, M.O., 2013. The dynamic effects of personal and corporate income tax changes in the United States. Am. Econ. Rev. 103 (4), 1212–1247. 

Musso, A., Neri, S., Stracca, L., 2011. Housing, consumption and monetary policy: How different are the US and the Euro area? J. Bank. Financ. 35 (11), 3019–3041. Rahal, C., 2016. Housing markets and unconventional monetary policy. J. Hous. Econ. 32, 67–80. 

Reid, C., 2007. The Canadian overnight market: Recent evolution and structural changes. Bank Canada Rev. 2007 (Spring), 15–29. 

Rigobon, R., 2003. Identification through heteroskedasticity. Rev. Econ. Stat. 85 (4), 777–792. 

Rogers, J.H., Scotti, C., Wright, J.H., 2018. Unconventional monetary policy and international risk premia. J. Money Credit Bank. 50 (8), 1827–1850. Rosenberg, S., 2019. The effects of conventional and unconventional monetary policy on house prices in the Scandinavian countries. J. Hous. Econ. 46, 101659. Sims, C.A., 1992. Interpreting the macroeconomic time series facts: The effects of monetary policy. Eur. Econ. Rev. 36 (5), 975–1000. 

Sims, C.A., Zha, T., 1999. Error bands for impulse responses. Econometrica 67 (5), 1113–1155. 

- Sims, C.A., et al., 1986. Are forecasting models usable for policy analysis? Q. Rev. 10 (Win), 2–16. 

Stewart, K.G., 2022. How important are land values in house price growth? Evidence from Canadian cities. Can. J. Econ./Revue canadienne d’économique 55 (1), 249–271. 

13 

_D. Nsafoah and C. Dery_ 

_Journal of Housing Economics 64 (2024) 101993_ 

Stock, J.H., Watson, M.W., 2012. Disentangling the channels of the 2007-09 recession. Brook. Pap. Econ. Act. 120–157. 

Stock, J.H., Watson, M.W., 2018. Identification and estimation of dynamic causal effects in macroeconomics using external instruments. Econ. J. 128 (610), 917–948. 

Swanson, E.T., 2021. Measuring the effects of Federal Reserve forward guidance and asset purchases on financial markets. J. Monetary Econ. 118, 32–53. 

Wright, J.H., 2012. What does monetary policy do to long-term interest rates at the zero lower bound? Econ. J. 122 (564), F447–F466. 

Wu, J.C., Xia, F.D., 2016. Measuring the macroeconomic impact of monetary policy at the zero lower bound. J. Money Credit Bank. 48 (2–3), 253–291. 

- Wu, J.C., Xia, F.D., 2020. Negative interest rate policy and the yield curve. J. Appl. Econometrics 35 (6), 653–672. 

14 

