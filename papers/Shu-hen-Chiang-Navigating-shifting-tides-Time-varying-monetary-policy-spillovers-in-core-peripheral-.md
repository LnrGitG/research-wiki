---
title: Navigating shifting tides: Time-varying monetary policy spillovers in core-peripheral housing markets in the Euro area
type: paper
source_pdf: raw/papers/Shu-hen Chiang_Navigating shifting tides Time-varying monetary policy spillovers in core-peripheral housing markets in the Euro area_2025.pdf
converted: 2026-07-26
---

Journal of Housing Economics 69 (2025) 102090 



Contents lists available at ScienceDirect Journal of Housing Economics journal homepage: www.elsevier.com/locate/jhec 



# Navigating shifting tides: Time-varying monetary policy spillovers in core-peripheral housing markets in the Euro area 



## Shu-hen Chiang<sup>a</sup> , Sandy Suardi<sup>b</sup> , Chien-Fu Chen<sup>c,*</sup> 



a _Chung-Yuan Christian University, Taiwan_ b _School of Business, University of Wollongong, Australia_ c _National Dong Hwa University, Taiwan_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|_Keywords:_|This study examines the spillover effects of a unifed monetary policy on core and peripheral housing markets in|
|Monetary policy<br>Shadow short rate<br>Spillovers<br>VAR<br>Euro area|<br>the Euro Area, utilizing augmented spillover accounting techniques developed by Diebold and Yilmaz (2009).<br>Our estimation results reveal signifcant core-peripheral differences: core countries experience stronger and more<br>immediate spillovers from monetary policy, especially during the unconventional period following the 2008<br>global fnancial crisis and events such as the Russian invasion of Ukraine. In contrast, peripheral countries exhibit<br>a slower, more moderate response, thereby remaining relatively insulated from policy-driven systemic risks. This<br>underscores the varying impacts of monetary policy on housing stability across the Euro Area, highlighting the<br>need for tailored policy responses.|



### **1. Introduction** 

The global financial crisis (GFC) starkly highlighted the risks of debtfueled housing surges followed by crashes (Brunnermeier et al., 2000). As real estate finance continues to grow, it poses a threat to financial stability (Jorda et al., 2016` ). According to economic theory, monetary policy influences house prices by adjusting interest rates, which in turn affect homeownership costs and asset values (Kuttner, 2012). Investigating how monetary policy can mitigate housing booms is crucial for maintaining financial stability. This paper examines the influence of monetary policy on housing prices across the euro area (EA), with a focus on its role in managing housing market fluctuations. 

Established in 1999, the European Central Bank (ECB) plays a crucial role in issuing the Euro and setting unified monetary policies for the EA countries. Rodriguez-Fuentes and Dow (2003) suggest that European monetary policy impacts broader regional stability, potentially exacerbating credit instability in peripheral regions and influencing housing demand. Following the GFC, economic disparities within the EA have increased, particularly affecting GIIPS countries (Greece, Ireland, Italy, Portugal, and Spain). The ECB’s unconventional policies, including the 

zero lower bound (ZLB) and large-scale asset purchases, have provoked much controversy. Ouerk et al. (2020) find these effects to be less robust than those of conventional policies, while Hulsewig and Rottmann (2021) observe that accommodative monetary policies, including innovations in central bank assets, have driven up house prices across the EA. More recently, the COVID-19 pandemic and the Russian invasion of Ukraine have underscored the importance of examining how these monetary policies affect housing markets over time. Based on the above, tracing out the time-varying effects of a common monetary policy in core-peripheral countries is essential. 

Unlike previous studies that focus on the effects of a common monetary policy on output growth in EA member countries,<sup>1</sup> our research specifically examines its impact on housing markets within the EA. This focus is crucial for two reasons. First, the housing market presents unique challenges, including asset indivisibility, high capital requirements, low liquidity, and the lack of short sales (Wachter, 2015; Duca et al., 2019). These characteristics can significantly threaten banks’ balance sheets and exacerbate systemic risk, as seen during the GFC.<sup>2</sup> Second, while housing markets are often analyzed locally, there has been limited investigation into how ECB monetary policy affects 

* Corresponding author. 

_E-mail address:_ cfc@mail.ndhu.edu.tw (C.-F. Chen). 

> 1 A non-exhaustive list of studies includes Peersman and Smets (2005), Rafiq and Mallick (2008), Georgiadis (2015), Hulsewig and Rottmann (2021) and Mandler et al. (2022). 

- 2 The pivotal role of the housing sector in terms of financial stability has garnered substantial global attention post-GFC, as highlighted by Reinhart and Rogoff 

- (2008), Blanchard et al. (2010), Geanakoplos et al. (2012), and Eickmeier and Hofmann (2013). 

https://doi.org/10.1016/j.jhe.2025.102090 

Received 28 December 2024; Received in revised form 12 August 2025; Accepted 17 August 2025 Available online 18 August 2025 

1051-1377/© 2025 Elsevier Inc. All rights are reserved, including those for text and data mining, AI training, and similar technologies. 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 

housing markets across core and peripheral countries, hence the spillover effects. This research fills these gaps by exploring these cross-country dynamics.<sup>3</sup> 

Through several approaches, our study investigates the relationship between a common monetary policy and housing markets in EA member countries. First, we use the Diebold-Yilmaz spillover method to assess time-varying spillovers, quantifying their magnitude and trends. Second, we apply Cholesky decomposition to identify monetary policy shocks, incorporating the lagged effects of housing prices on the shadow short rate (SSR). Third, we consider all possible core and peripheral housing market re-ordering to enhance contagion analysis. Finally, we distinguish spillovers between EA-wide monetary policy and individual member housing markets using an innovative spillover accounting approach to reveal the complex dynamics and drivers of monetary policy spillovers to housing markets in both core and peripheral economies. 

Using quarterly data from 1995 to 2023, our analysis examines spillovers between the shadow short rate, serving as the policy rate, and real housing prices in four core EA countries (Germany, France, the Netherlands, and Belgium) and four peripheral countries (Ireland, Italy, Portugal, and Spain). Key findings include: (1) the immediate impact of monetary policy is very significant compared to its longer-term effects; (2) spillovers exhibit high volatility and time-varying patterns, highlighting the need for a dynamic analytical approach; (3) unconventional monetary policies<sup>4</sup> have a notable effect on housing markets; (4) peripheral countries had lower monetary policy spillovers than local – housing markets except the period (2009 2013) of the European sovereign debt crisis (ESDC); and (5) during the period of the Russian invasion of Ukraine, core countries experienced a sharp rise in monetary policy spillovers, increasing systemic risks, while peripheral countries even saw decreasing spillovers, with local housing dynamics playing a larger role. These insights reveal how monetary policy and housing markets interact differently across core and peripheral economies, especially during economic crises. 

This paper makes several important contributions to the literature on monetary policy and housing market dynamics in the Euro Area (EA). It shifts the focus from conventional macroeconomic outcomes, such as output growth, to the underexplored area of how a common monetary policy, particularly unconventional monetary policy tools like the zero lower bound (ZLB) and large-scale asset purchases, affects real housing prices across both core and peripheral EA countries. To our knowledge, this is among the first studies to systematically examine the time-varying spillover effects of these non-traditional monetary interventions on national housing markets. Using a comprehensive empirical strategy that includes Diebold-Yilmaz spillover indices, Cholesky decomposition, and novel spillover accounting methods, the study uncovers the dynamic and asymmetric nature of monetary policy spillovers. Core countries are found to experience stronger and more immediate effects, especially during episodes of unconventional policy and geopolitical shocks such as the Russian invasion of Ukraine, whereas peripheral countries exhibit more gradual and delayed responses, with notable exceptions during the European sovereign debt crisis. These findings not only highlight a critical gap in the existing literature, largely focused on output or financial markets, but also question the efficacy of unconventional 

> 3 Fratantoni and Schuh (2003), Del Negro and Otrok (2007), Fischer et al. (2019), and Beraja et al. (2019) have explored the regional impacts of monetary policy on local housing markets using U.S. regional data. 

> 4 Unconventional monetary policy measures began in response to the Global Financial Crisis in 2008-2009 and have continued through various phases, including the Eurozone sovereign debt crisis in 2010-2013, the low inflation environment of 2014–2019, and the COVID-19 pandemic of 2020-2022. Each phase introduced different instruments, such as longer-term refinancing operations, the Securities Markets Program, quantitative easing, and the Pandemic Emergency Purchase Program (PEPP). 

monetary policies in stabilizing housing markets and managing systemic risks. In so doing, this paper provides valuable insights for designing more effective and context-sensitive policy responses within a diverse monetary union. 

The paper is structured as follows: Section 2 introduces our VAR model, which underpins the augmented spillover accounting within a rolling-window framework. Section 3 outlines the data utilized in our analysis. Section 4 details static and dynamic estimation results and their policy implications. The final section concludes the paper. 

### **2. The VAR model and spillover accounting** 

### _2.1. The DY spillover method for the EA housing markets_ 



ʹ where Δ _lnHPt_ = ( Δ _lnHP_ 1 _,t,_ Δ _lnHP_ 2 _,t,_ ⋯ _,_ Δ _lnHPN,t_ ) , _c_ is the _N_ -element vector of constant terms, each Φ _l_ is an _N_ × _N_ matrix of coefficients, and _εt_ is the _N_ -element vector of random error terms. 

first difference ensures the stationarity requirement of the VAR model. In Eq. (1), Δ _lnHPi,t_ is the housing return of a member country. The Here, _ε_ is a random error distributed with a zero mean and a covariance matrix, Σ. A moving average representation can represent the VAR model: ΔlnHP _t_ =<sup>∑∞</sup> _l_ =0<sup>_Alεt_−</sup><sup>_l_where A is an adjustment coefficient</sup> matrix. 

Based on (1), Diebold and Yilmaz (2009) proposed a novel spillover measure by means of Forecast Error Variance Decomposition (FEVD) over H forecast horizons, where the sum of the own variance share ( _φ_ ii(H)) in (3) and the cross-variance shares (<sup>∑N</sup> _j_ =1 _φ_ ij(H)) in (4) is equal _j_ ∕= _i_ 

to unity as depicted in (2): 



Diebold and Yilmaz (2009) argued that cross-variance shares provide a suitable proxy indicator for spillovers, as these shares are grounded in the ability of other regions to explain variations in this specific region. This makes larger (smaller) cross-variance shares directly correspond to higher (lower) levels of spillovers. Consequently, the DY spillover method is suitable for quantifying the extent of spillovers, which goes beyond the confines of a "pairwise" relationship between two markets, as seen in methods like the causality test proposed by Billio et al. (2012). 

Diebold and Yilmaz (2009, 2012) developed the total spillover index (TSP), defined in (5): 



The total spillover index represents the mean of all cross-variance shares, collectively representing the extent of spillovers across N 

2 

_Journal of Housing Economics 69 (2025) 102090_ 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics_ 

markets. A greater total spillover index indicates a higher level of interconnectedness, and consequently, a heightened level of systemic risk. 

Next, the directional spillovers capture possible causal relations between nation i and other EA member countries in two directions: “from” and “to” other markets using (6) with _DSPi._ and using (7) with _DSP.i_ , respectively. 



Finally, the net spillover index, denoted as _NSPi_ is computed following (8). This involves subtracting the directional spillovers "from" other markets (as given in (6)) from the directional spillovers "to" other markets (as given in (7)). Depending on the sign of the net spillover, a positive (negative) value signifies that the nation is a provider (receiver) of spillovers. 



In the rolling window calculation, we start with a fixed sample size, such as 40 quarters, to establish the initial parameters for the spillover indices based on the first 40 observations. Then, we progress with a fixed-size estimation window, updating parameters one period at a time until the last observation. This iterative approach enables the computation of time-varying spillover indices, providing insights into their evolving dynamics over time. 

### _2.2. The augmented DY spillover method incorporating monetary policy_ 

Unlike in past studies, we consider monetary policy to revisit housing spillovers. Thus, consider a VAR with endogenous variables that can be partitioned as follows: _Zt_ = [ _ZZ_ 12 _,,tt_ ], where _Z_ 1 _,t_ contains the monetary 

policy variable (SSR), and _Z_ 2 _,t_ comprises housing prices for the _N_ EA member countries. We therefore construct a stationary matrix Z as in (9) with ( _N_ + 1) variables: 



Since the Cholesky decomposition of the reduced-form VAR is sensitive to variable ordering, we are concerned about establishing a reasonable identification based on economic rationale. As far as the role of monetary policy ( _Z_ 1 _,t_ ) is concerned, the goal of a common monetary policy by the ECB must first focus on the “EU-wide” economy, rather than a specific member country or housing sector. To reply to this consideration, taking _Z_ 1 _,t_ as the first variable over _Z_ 2 _,t_ ensures that housing prices have no immediate effect on SSR (“contemporaneous” effect) via the assumption of weak exogeneity, but rather an indirect impact from lagged housing prices influencing current SSR values; at the same time, monetary policy can contemporaneously influence local housing markets (Fratantoni and Schuh, 2003; Giuliodori, 2005; Abdallah and Lastrapes, 2013; Bahadir and Lastrapes, 2015). 

On the other hand, for local housing markets ( _Z_ 2 _,t_ ), there is no information on their ordering, just as Diebold and Yilmaz (2014) mentioned that spillovers among different geographic units are pure empirical work. However, given SSR as the first variable, the generalized VAR is never again our solution. Following Klobner and Wagner (2013), we can resolve the selection of the ordering for _Z_ 2 _,t_ through all permutations for local housing markets. To sum up, we can establish our ordering strategy for the Cholesky decomposition: _Z_ 1 _,t_ is designed for the first ordering, while _Z_ 2 _,t_ is appointed to the ordering, except the first, using all possible combinations of N housing markets. 

For instance, with four housing markets in this paper, there are 24 permutations for the ordering from 2 to 5, given that SSR is the first variable. We estimate the VAR for each combination, continuing the iteration until the 24th. Finally, averaging the cross-variance shares from these permutations yields robust spillover estimates, comprehensively addressing variable orderings and potential contemporaneous effects among housing markets. 

The FEVD of our augmented VAR model captures average crossvariance shares denoted as _~~φ~~_ 1 _j_ and _~~φ~~ j_ 1, representing robust (average) spillovers of monetary policy "from" or "to" all local housing markets. Additionally, _~~φ~~ ij_ and _~~φ~~ ji_ depict average spillovers of country i "from" or "to" other member housing markets. These values allow computation of DY spillover indices, including the augmented total spillovers (ATSP) in Eq. (10), reflecting interactions between monetary policy and local housing markets. Note that (10) differs from (5) as it incorporates the interaction between monetary policy and local housing markets. 



The next step is to separate spillovers from the two components: monetary policy (m) and the local housing system (RE), respectively, by excluding own variance shares from the diagonal elements. Eqs. (11) and (12) define the total spillovers for monetary policy and local housing systems separately.<sup>5</sup> This approach disentangles and analyzes the unique spillover dynamics of each component, enhancing understanding of their impacts. 



For directional spillovers, we examine the causal relationships between monetary policy and all local housing markets in two directions: "from" (←) and "to" (→), as depicted in (13) and (14), respectively. These equations enable us to evaluate the impact of monetary policy on local housing markets and vice versa. Likewise, we can calculate directional spillovers for each country _i_ "from" and "to" other member housing markets using Eqs. (15) and (16), respectively. This enables us to understand the directional influence of each country on the housing markets of other member countries within the analysis. 





There are two types of net spillovers we can analyze. Firstly, net spillovers determine the overall impact of monetary policy on the local housing system (in (17)). This is calculated by subtracting "from" directional spillovers (in (13)) from "to" directional spillovers (in (14)). 

> 5 To ensure the validity of our spillover account, the sum of equations (11) and (12) is exactly equal to equation (10). 

3 

_Journal of Housing Economics 69 (2025) 102090_ 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics_ 

#### **Table 1** 

Home ownership and tenancy rates. 

||Owner<br>||||||Tenant<br>||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Core|2021|2022|2023|2024|mean|sd|2021|2022|2023|2024|mean|sd|
|**Germany**|49.1|46.5|47.6|47.2|47.60|1.10|50.9|53.5|52.4|52.8|52.40|1.10|
|**Belgium**|71.3|72.5|71.9|70.2|71.48|0.98|28.7|27.5|28.1|29.8|28.53|0.98|
|**France**|64.7|63.4|63.1|61.2|63.10|1.44|35.3|36.6|36.9|38.8|36.90|1.44|
|**Netherlands**|70.1|70.6|69.3|68.8|69.70|0.80|29.9|29.4|30.7|31.2|30.30|0.80|
|**Peripheral**|**2021**|**2022**|**2023**|**2024**|**mean**|**sd**|**2021**|**2022**|**2023**|**2024**|**mean**|**sd**|
|**Spain**|75.8|76|75.3|73.7|75.20|1.04|24.2|24|24.7|26.3|24.80|1.04|
|**Italy**|73.7|74.3|75.2|75.9|74.78|0.97|26.3|25.7|24.8|24.1|25.23|0.97|
|**Portugal**|78.3|77.8|76|73.4|76.38|2.22|21.7|22.2|24|26.6|23.63|2.22|
|**Ireland**|69.8|70.5|69.4|69.3|69.75|0.54|30.2|29.5|30.6|30.7|30.25|0.54|



Source: Eurostat data. 

A positive value suggests that monetary policy contributes to the local housing system, while a negative value indicates that local housing markets influence monetary policy. Secondly, net spillovers assess interactions between a specific country and other member housing markets (in (18)). It is derived by subtracting "from" directional spillovers (in (15)) from "to" directional spillovers (in (16)). Negative implies the country receives influence from others, positive suggests exerting influence on others. These analyses help identify the roles of entities in monetary policy-housing market interactions. 





Our approach integrates a novel spillover accounting to comprehensively evaluate all spillovers from monetary policy to local housing markets. This holistic understanding can inform ECB decisions, fostering stability and informed economic policy within the EA. 

### **3. Data** 

### _3.1. Selection of core and periphery member countries and their real housing prices_ 

The core-periphery divide within the European Monetary Union (EMU) has been a focal point for economists since its inception (Bayoumi and Eichengreen, 1993). To assess the core value of a unified Eurozone monetary policy, we first focus on core-member housing markets, where the ECB’s impact is most pronounced, given their historically close economic coordination, from the European Exchange Rate Mechanism (ERM) to the Euro adoption (Peersman and Smets, 2005). Definitions of core members vary across the literature (Bayoumi and Eichengreen, 1993; Campos and Macchiarelli, 2016, 2021; Ahlborn and Wortmann, 2018; Hulsewig and Rottmann, 2021). Considering these variations, data availability, and challenges related to the European System of Accounts (ESA-2010) classification, we identify Belgium, France, Germany, and the Netherlands as core countries, consistent with previous studies, while addressing practical and data constraints. Moreover, GIIPS countries, typically viewed as peripheries, have faced severe debt crises, except for Greece, which underwent IMF and EU bailouts, debt defaults, and austerity from 2010 to 2011, until the EU’s monitoring eased in 2022. Our core and periphery economies classification is consistent with past studies (see De Santis and Cesaroni, 2016; Hoynck et al., 2025). Analyzing the ECB’s monetary policy effects on housing markets in both core and peripheral nations offers crucial insights into the core-peripheral debate. 

The analysis of homeownership and tenancy rates across these categories further supports our classification of countries into core and peripheral groups. The Eurostat database offers comparable 

homeownership and tenancy rates for Euro Area member countries, though the data only covers the period from 2021 to 2024. As a result, we present a comparison of homeownership structures among these economies in Table 1. In Section 4.4.2, under robustness checks, we include homeownership as a control variable in our model, using a longer dataset spanning from 2008 to 2023 to account for demand factors. Germany stands out among the core countries due to notably higher tenancy rates, likely contributing to its lower homeownership rate compared to other core members. Conversely, the other three core countries exhibit relatively similar housing tenure profiles. Peripheral countries consistently demonstrate higher homeownership rates and lower tenancy rates compared to core economies. These differences in homeownership structure between core and peripheral countries suggest potential variations in the spillover effects of monetary policy across these groups. 

We analyzed housing prices in four core and four peripheral countries using the OECD real housing price index, with 2015 as the base year to adjust for inflation. Fig. 1 reveals key trends: all four core countries showed a general upward trend in housing prices. Before the 2008–2009 global financial crisis (GFC), Germany’s housing market experienced a slight decline, whereas Belgium, France, and the Netherlands saw notable increases. Following the GFC, the ECB’s unconventional monetary policies led to consistently growing housing prices in all four countries, suggesting that these policies stimulated price appreciation. Notably, since the COVID-19 pandemic began, there has been an unprecedented surge in housing prices across all four core countries. 

We further categorized the four core countries into high-growth (Germany and the Netherlands) and low-growth (Belgium and France) groups based on recent housing price inflation since 2014. This classification highlights differences in housing price growth among these countries. 

Fig. 2 shows that among the four peripheral members, Spain and Italy have experienced low housing price growth, while Portugal and Ireland have exhibited high growth since 2014. Notably, Spain and Italy experienced a significant boom and bust cycle around the 2008 global financial crisis, with peak real house prices reaching 160 before the crash. 

### _3.2. Shadow short rate (SSR)_ 

Unconventional monetary policy differs significantly from conventional monetary policy, necessitating the consideration of a suitable policy rate that takes into account these new measures. Wu and Xia (2016) were among the first to address the challenges posed by the zero lower bound (ZLB) and yield curves in developing a new policy rate, known as the shadow short rate (SSR). Subsequently, Wu and Xia (2020) adjusted their SSR estimates in response to the ECB’s introduction of negative nominal interest rates. 

4 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 



**Fig. 1.** Real housing prices for four core members. 



**Fig. 2.** Real housing prices for four peripheral members. 

Our analysis uses SSR data from Krippner (2020), which incorporates time-varying ZLB, longer-maturity yield curves, and an extended time series dating back to 1995.<sup>6</sup> This dataset is crucial for examining the evolving relationship between the SSR and housing markets. Notably, the SSR is approximately equal to the official ECB interest rate under the conventional monetary policy; however, after 2009, the SSR significantly diverged from the official ECB interest rate, a shift from its prior alignment. This deviation highlights the SSR’s sensitivity to unconventional monetary policy measures, emphasizing its role in reflecting the impacts of such policies. 

> 6 We utilise the extended shadow short rate (SSR) series developed by Krippner (2015) as a consistent proxy for monetary policy across the Euro Area, commencing in 1995. For the period before January 1, 1999, Krippner employs the midpoint of the Deutsche Bundesbank’s discount rate as a proxy, reflecting Germany’s central role in shaping monetary conditions before the establishment of the European Central Bank (ECB). From 1999 onward, the SSR is derived from ECB policy rates. 

Fig. 3 reveals a key development: the ECB’s introduction of monetary policy with negative SSR values in response to the European Sovereign Debt Crisis (ESDC). This shift signifies the adoption of unconventional measures to address economic challenges. However, persistent negative SSR values may lead to a potential liquidity trap, which could limit the ECB’s ability to stimulate the economy through interest rate adjustments. In 2022, the ECB raised short-term interest rates sharply in response to high inflation caused by the Russian invasion of Ukraine; however, it remains uncertain whether this increase will effectively break through the barriers of the liquidity trap, given the rising trend in housing prices. 

While the SSR, especially as estimated by Krippner (2020), captures a broad range of monetary policy actions, including forward guidance and quantitative easing, its ability to reflect the market effects of specific 

5 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 



**Fig. 3.** Shadow short rate. 

announcements or credit-focused programs, such as TLTROs, may be limited.<sup>7</sup> However, one advantage of Krippner’s SSR is that it incorporates information from the entire yield curve, including long-term government bond yields, which were particularly elevated during the sovereign debt crisis in countries such as Ireland and Portugal. This allows the SSR to partially reflect market conditions that led to, or resulted from, such nonstandard ECB interventions. 

We conduct the Augmented Dickey-Fuller test on the growth rates of house prices and the SSR and find that the unit root null hypothesis is rejected at conventional significance levels. The results are presented in Appendix Table A1. As a result, we use the first differences of house prices and the SSR in our model estimation. 

Our dataset for SSR and core and peripheral housing returns spans from Q2 1995 to Q2 2023, covering over 25 years and totaling 113 observations. We use a rolling window approach with a 40-quarter (10year) window to estimate our VAR model, allowing us to compute various spillovers.<sup>8</sup> This approach yields 73 estimated parameters from 2005 onwards. The extensive dataset facilitates a comparison of the time-varying evolution of spillovers between monetary policy and local housing markets, encompassing both conventional and unconventional monetary policies, which will be detailed in the following section. 

### **4. Empirical results** 

### _4.1. Static spillovers: core vs. peripheral member countries_ 

We begin by applying Diebold and Yilmaz’s (2012) static spillover approach to estimate our VAR model for the period from 1995 to 2023, using a lag order of one as determined by the Bayesian Information Criterion (BIC). The model is estimated 24 times for different permutations of variable orderings among the four core and peripheral member countries, respectively. The results, detailing average cross-variance shares and two types of spillovers, are presented in Tables 2 (core) and 3 (periphery). 

Several key observations emerge from the analysis. Firstly, the total spillover effect, combining both local housing systems and monetary policy, is 16.49 %. Of this, monetary policy-driven spillovers average 3.72 % (calculated as (15.91 % + 2.67 %) ÷ 5), while spillovers among the four housing markets account for 12.77 % (calculated as 16.49 % - 3.72 %). In this static analysis, monetary policy-driven spillovers account for approximately 23 % of the total. The net spillovers from monetary policy to the housing markets average 2.65 % (calculated as (15.91 % - 2.67 %) ÷ 5), showing a minimal impact. Among the local housing systems, France is the only source of positive spillovers at 0.85 % (calculated as (23.11 % - 18.87 %) ÷ 5), while the other three countries receive spillovers. 

In peripheral countries, the total spillover effect from both the local housing system and monetary policy is 15.66 %. Of this, monetary policy spillovers contribute only 1.73 % (calculated as [(5.89 % + 2.74 %) ÷ 5]), while spillovers among the housing markets account for 13.93 % (calculated as 15.66 % - 1.73 %). This indicates that monetary policy spillovers make up about 11 % of the total, roughly half of what is observed in core countries. The net spillovers from monetary policy to the housing markets are modestly positive, averaging 0.63 % (calculated as [(5.89 % - 2.74 %) ÷ 5]). Compared to core countries, monetary policy has a smaller impact on the housing markets in peripheral EA countries. Among the four peripheral nations, only Italy shows a net negative spillover of 2.17 % (calculated as [(11.07 % - 21.94 %) ÷ 5]), while the other three are net providers. 

Comparing spillover effects, core EA countries experience higher monetary policy-driven spillovers than peripheral countries, at 3.72 % versus 1.73 %, respectively. Housing market spillovers are similar, accounting for 12.77 % in core and 13.93 % in peripheral countries. Monetary policy’s net spillover effects on housing markets are generally positive in core countries, while peripheral countries show mixed results, with Italy as a net recipient and other peripheral nations as net providers. 

### _4.2. Dynamic spillovers: the effects of monetary policy on core vs peripheral countries_ 

> 7 The ECB’s unconventional monetary policies, particularly the 2012 “whatever it takes” announcement by President Mario Draghi, went beyond the shadow short rate (SSR). This intervention, along with targeted longer-term refinancing operations (TLTROs), likely impacted housing markets in peripheral euro area countries by easing sovereign debt concerns and supporting credit supply. Notably, only Ireland and Portugal entered formal bailout programs, while Italy and Spain, despite high yields, did not request direct assistance, leading to varied impacts across these economies. 

> 8 To ensure the robustness of the VAR models, we selected the optimal lag length based on the Bayesian Information Criterion (BIC), choosing the specification with the lowest BIC value. Additionally, we tested for autocorrelation and found no evidence of it. The results are presented in Appendix Table A2. 

Figs. 1 and 2 both illustrate the inherent volatility in housing markets for core and peripheral countries, with Spain and Ireland experiencing significant boom-bust cycles. To capture this dynamic, we use a 40quarter rolling window in our analysis, running VAR models 1752 times (73 for each of the 24 permutations). This approach yields an average of 73 cross-variance shares, which are used to compute total, directional, and net spillovers, as detailed in Figs. 4 and 5 for core and peripheral countries, respectively. 

6 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 

#### **Table 2** 

Static version of spillovers in core countries. 

||SSR|Belgium|France|Germany|Netherlands|Unit: %<br>Contribution**from**others|
|---|---|---|---|---|---|---|
|SSR|97.33|1.07|1.04|0.14|0.42|2.67|
|Belgium|6.20|73.05|19.39|0.22|1.13|26.94|
|France|0.23|12.77|81.14|1.72|4.15|18.87|
|Germany|9.16|1.18|0.72|81.97|6.98|18.04|
|Netherlands|0.32|8.78|1.96|4.89|84.04|15.95|
|Contribution**to**others|15.91|23.80|23.11|6.97|12.68|82.47|
|Contribution including own|113.24|96.85|104.25|88.94|96.72|16.49|



#### **Table 3** 

Static version of spillovers in peripheral countries. 

||SSR|Spain|Italy|Portugal|Ireland|Unit: %<br>Contribution**from**others|
|---|---|---|---|---|---|---|
|SSR|97.27|0.58|0.03|1.85|0.28|2.74|
|Spain|0.17|73.63|8.25|4.48|13.47|26.37|
|Italy|3.73|14.91|78.06|1.88|1.42|21.94|
|Portugal|1.84|3.22|1.63|89.61|3.70|10.39|
|Ireland|0.15|9.09|1.16|6.46|83.14|16.86|
|Contribution**to**others|5.89|27.80|11.07|14.67|18.87|78.30|
|Contribution including own|103.16|101.43|89.13|104.28|102.01|15.66|





**Fig. 4.** Augmented total spillovers for SSR and core housing markets. 

### _4.2.1. Total spillovers_ 

Fig. 4 presents the augmented total spillovers for the SSR and core member housing markets, using a rolling window approach, which contrasts with the static estimates in Table 2. The dynamic analysis reveals that spillovers fluctuate between 12 % and 30 % before peaking over 60 % in 2023, significantly higher than the static estimate of 16.49 %. This variation highlights the importance of dynamic estimation in 

understanding the spillover patterns between monetary policy and housing markets. Key events are highlighted, including the Global Financial Crisis (GFC), the European Sovereign Debt Crisis (ESDC), the US-China trade war, the COVID-2019 pandemic, and the Russian invasion of Ukraine, each marked by notable peaks. The Russian invasion of Ukraine in February 2022 and the subsequent sharp rise in SSR led to an exceptional peak of 65 % in 2023. This dynamic perspective offers a 



**Fig. 5.** Augmented total spillovers for SSR and peripheral housing markets. 7 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 

more nuanced understanding of how significant geopolitical and economic events influence the relationship between monetary policy and housing markets. 

Fig. 5 shows that peripheral countries exhibit a similar trend in augmented total spillovers as core countries, with notable peaks during the GFC, ESDC, and US-China trade war, although these peaks are more pronounced. However, unlike core countries, peripheral nations did not experience a sharp rise in spillovers after 2022. During the COVID-19 pandemic, spillovers in peripheral countries initially increased but began to decline around mid-2021, a pattern that contrasts with the one observed in core countries. 

We further analyze the sources of augmented total spillovers in core and peripheral countries to determine whether these changes are driven by monetary policy or local housing markets. Figs. 6 and 7 illustrate how temporal variations in spillovers reveal the evolving relationship between monetary policy and housing markets. 

Fig. 6 illustrates the time-varying total spillovers from monetary policy and local housing markets in core countries. Notably, short-term spillovers from monetary policy are more pronounced, ranging from 2 % to 32 %, compared to the static long-term estimates. A comparison between traditional monetary policies (2005 to mid-2008) and unconventional policies (from Q3 2008 onward) shows that unconventional measures generate more spillovers, consistent with previous research (Boeckx et al., 2017; Dell’Ariccia et al., 2018). Besides, local housing markets mainly contributed more to total spillovers than monetary policy before 2019. However, with the onset of unconventional monetary policy around 2009, this gap narrowed. From 2008 to 2020, the disparity between the contributions of the housing market and monetary policy to spillovers was smaller than during the conventional policy period. 

During the COVID-19 period, a notable increase in spillover occurred among local housing markets, peaking at over 20 %, as shown in Fig. 6. Comparisons between Figs. 4 and 6 indicate that the total augmented spillovers surged past 25 %, driven primarily by strong ripple effects within local housing markets rather than monetary policy. This substantial rise highlights increasing systemic risk, with local housing market dynamics exerting a greater influence on spillovers than monetary policy shocks. Our findings align with Battistini et al. (2021), who highlight the resilience of the EA housing market during the COVID-19 pandemic’s second and third waves, despite stricter restrictions in late 2020. House prices surged by approximately 6 % in both Q4 2020 and Q1 2021, a pace not seen since mid-2007, and housing investment approached pre-crisis levels. This resilience is attributed to supply-side factors such as increased construction and real estate activity, and demand-side factors including a return to pre-crisis transaction levels and heightened mortgage demand. Contributing factors include less severe restrictions, significant fiscal and monetary policy support, 

favorable financing conditions, and increased housing attractiveness due to forced savings. Similarly, Gamber et al. (2023) attribute the rise in housing demand and prices to "stay-at-home" consumption behaviors during the pandemic. 

However, a shift from the local housing system to monetary policy began in 2022, coinciding with the Russian invasion of Ukraine. This result indicates that an abrupt increase in SSR eventually breaks through the liquidity trap to effectively impact core housing markets. 

Fig. 7 provides a detailed view of the evolving total spillovers from monetary policy and local housing markets in peripheral countries. Short-term monetary policy spillovers range from 2 % to 15 %, compared to a long-term static estimate of 5.89 %. Local housing markets consistently contribute more to total spillovers than monetary policy, with this gap widening post-2013. In contrast, core countries saw housing market contributions surpassing monetary policy spillovers until 2015, after which monetary policy contributions prevailed until 2019. During the unconventional monetary policy period (2009–2013) due to the ESDC event, peripheral countries had high monetary policy spillovers, averaging 15 %, which then declined to 5 % from 2019 to 2023. In core countries, monetary policy contributions averaged around 10 % from 2009 to 2019. 

Since 2015, contributions from local housing markets to total spillovers have steadily risen, peaking by _>_ 30 % during the COVID-19 period, although this increase is less pronounced than in core countries. In core countries, housing market contributions to total spillovers reached nearly 20 % during the COVID-19 period, representing a substantial increase compared to the 5 % rise in peripheral countries. This difference explains the moderate uptick in augmented total spillovers in peripheral countries since the pandemic’s onset, as shown in Fig. 5. The decline in augmented total spillovers around mid-2021 is due to decreased housing market contributions and lower monetary policy spillovers in peripheral countries. This contrasts with core countries, where a significant increase in augmented total spillovers highlights heightened systemic risk. In peripheral countries, while local housing spillovers remain more influential than monetary policy shocks, systemic risk is less severe compared to core countries. 

### _4.2.2. Directional and net spillovers_ 

In this subsection, we discuss the role of monetary policy in directional and net spillovers. Fig. 8 illustrates the spillovers between monetary policy and local housing markets in core countries. Fig. 8(b) shows that directional spillovers from monetary policy to local housing markets are significantly higher than those from housing markets to monetary policy, as seen in Fig. 8(a). Consequently, positive net spillovers from monetary policy to housing markets are evident over time, as shown in Fig. 8(c). A notable spike in net spillovers occurred after the SSR surged, coinciding with the Russian invasion of Ukraine. These 



**Fig. 6.** Total spillovers from monetary policy and the core housing markets. 

8 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 



**Fig. 7.** Total spillovers from monetary policy and the peripheral housing markets. 



**Fig. 8.** Directional and net spillovers of monetary policy on core housing markets. 

results indicate that while monetary policy does impact core economies, the effects on local housing markets in the EA have been relatively subdued since 2022. 

Fig. 9 illustrates the transmission of spillovers between monetary policy and local housing markets in peripheral countries. As in core countries, the directional spillovers of monetary policy "to" the local housing markets are notably higher than those "from" the local housing markets, as shown in Fig. 9(b). However, peripheral countries experienced a significant increase in monetary policy spillovers to local 

housing markets starting in 2009, following the ESDC event, which was marked by the introduction of unconventional monetary policies. Despite this, the net spillovers of monetary policy to housing markets, particularly after the SSR increase in 2022, are less pronounced compared to core countries. During the COVID-19 pandemic and the Russian invasion of Ukraine, peripheral countries exhibit smaller and more positive net spillovers, indicating a less significant impact of monetary policy on local housing markets compared to core countries. 





**Fig. 9.** Directional and net spillovers of monetary policy on peripheral housing markets. 

9 

_Journal of Housing Economics 69 (2025) 102090_ 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics_ 

_4.3. Housing market spillovers during unconventional monetary policy and the COVID-19 pandemic_ 

Figs. 6 and 7 indicate that interregional housing spillovers primarily drive the increase in total spillovers during the COVID-19 pandemic. We 

further analyze the interactive relationships among local housing markets by examining directional and net spillovers for individual EA member countries. 

During the early period of unconventional monetary policy, Fig. 10 (c) shows that France is the only country with positive net directional 









**Fig. 10.** Directional spillovers: Core housing markets. 

10 

_Journal of Housing Economics 69 (2025) 102090_ 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics_ 

spillovers, meaning it transmitted housing market shocks to other core countries. However, during the COVID-19 pandemic, France became a net recipient of shocks, a trend that continues after the significant SSR increase in the Russian invasion of Ukraine since 2022. The Netherlands also exhibits negative net spillovers post-2022. Conversely, Belgium and Germany are net providers of shocks to the housing markets of other 

core countries. After the pandemic, France and Germany shift to being net recipients of housing market shocks. 

During the early period of unconventional monetary policy, Fig. 11 (c) shows that Spain and Portugal were net providers of housing market shocks to other peripheral countries. Italy, conversely, has been a net recipient of shocks from other peripheral countries since 2009, a trend 







**Fig. 11.** Directional spillovers: Peripheral housing markets. 

11 

_Journal of Housing Economics 69 (2025) 102090_ 

that continues through the pandemic and the 2022 SSR increase. Ireland, on the other hand, shifts from being a net recipient to a net provider of housing market shocks starting in 2008, maintaining this role throughout the pandemic. Overall, core countries exhibit more dynamic shifts in spillover roles, while peripheral countries show greater stability in their roles as transmitters or receivers of shocks. 

### _4.4. Robustness checks_ 

### _4.4.1. Controlling for working age (25_ – _45) population growth rates, a demand-side factor_ 

One proxy for the demand factor is homeownership. However, due to data limitations, we are unable to include this factor directly in our estimation model, as Eurostat only provides annual data on homeownership and rental ratios from 2021 to 2024. Instead, we incorporated the working-age population growth rates (ages 25–45), which are known to Mankiw and have a significant impact on housing demand and prices ( Weil, 1989; Monnet and Wolf, 2017), as an exogenous variable in the VAR model, resulting in the VARX model. Annual data on the working-age population (ages 25–45) are available from the Eurostat database, covering the period from 1998 to 2003. Quarterly data for this variable were interpolated from the annual data using the Chow and Lin (1971) method. The rolling spillovers were estimated from the first quarter of 2008 to the second quarter of 2023. Figs. 12(a) and (b) present the augmented total spillovers for SSR on core and peripheral housing markets, respectively. 

The inclusion of the demand factor, proxied by the growth rate of the working-age population, results in spikes in the total spillover of SSR for the core housing market during key event dates, similar to the pattern shown in Fig. 4. However, the peak spillover during the Russian invasion of Ukraine in 2023 is 45 %, lower than the 60 % observed in Fig. 4. Additionally, spillovers before 2022 fluctuate between 15 % and 32 %, compared to the 12 % to 30 % range in Fig. 4. Fig. 12(b) displays a similar pattern of increased total spillovers for SSR, similar to Fig. 5, where peripheral countries exhibit spillovers comparable to those in core countries. Notable peaks occur during the GFC, the European Sovereign Debt Crisis (ESDC), and the US-China trade war, although these peaks are more pronounced in peripheral countries. However, unlike core countries, peripheral nations did not experience a sharp rise in spillovers after 2022. During the COVID-19 pandemic, spillovers in peripheral countries initially increased but began to decline around mid2021, contrasting with the persistent rise observed in core countries. These findings suggest that our baseline regression results are robust to the exclusion of the demand factor. 

Figs. 12(c) and 12(d) display the sources of the augmented total spillovers for core and peripheral countries, respectively, to assess whether these changes are driven by monetary policy or local housing markets. The total spillovers attributed to monetary policy and the core 

housing markets are consistent with those shown in Fig. 6. Notably, before 2019, local housing markets contributed more to total spillovers than monetary policy. During the COVID-19 period, a significant increase in spillovers from local housing markets is observed, peaking at over 30 %, which is notably higher than the 20 % peak observed in Fig. 6. 

Fig. 12(d) provides a detailed view of the evolving total spillovers from monetary policy and local housing markets in peripheral countries. Short-term monetary policy spillovers range from 3 % to 20 %. Local housing markets consistently contribute more to total spillovers than monetary policy, with this gap widening after 2013. Since 2015, the contribution of local housing markets to total spillovers has steadily increased, peaking at over 30 % during the COVID-19 period, a trend similar to that shown in Fig. 7. In peripheral countries, local housing market spillovers continue to have a more substantive influence than monetary policy shocks. 

### _4.4.2. Controlling for homeownership rates, an alternative demand-side factor_ 

Another proxy for the demand factor is homeownership. However, the Statista database only provides annual data on homeownership from 2008 to 2023. Instead of using the working-age population variable as in Section 4.4.1 , we incorporated homeownership rates, which can influence housing demand and prices, as an exogenous variable in the VAR model. Quarterly data for this variable were interpolated from the annual data using the Chow and Lin (1971) method. The rolling spillovers were estimated from Q4 2017 to Q2 2023. Figs. 13(a) and 13(b) present the augmented total spillovers for SSR on core and peripheral housing markets, respectively. 

Controlling for this demand factor, we observe a similar sharp spike in the total spillover of SSR for the core housing market during the Russian invasion of Ukraine, and a more moderate spike during the COVID-19 pandemic, reflecting a pattern similar to that shown in Fig. 4 The peak spillover during the Russian invasion of Ukraine in 2023 is of comparable magnitude (around 40 %) to that in Fig. 12(a). Fig. 13(b) shows a similar pattern to Fig. 12(b), particularly noting a decline in spillovers from SSR for peripheral countries during the Russian invasion period. However, the decrease from the peak of the COVID-19 pandemic is about 20 % (13 %) when controlling for the working-age population (homeownership). Furthermore, unlike core countries, peripheral nations did not experience a sharp rise in spillovers after 2022. These findings further suggest that our baseline regression results remain robust even when the demand factor is excluded. 

Figs. 13(c) and (d) illustrate the sources of the augmented total spillovers for core and peripheral countries, respectively, to determine whether these changes are driven by monetary policy or local housing markets. The total spillovers attributed to monetary policy and core housing markets align with those shown in Fig. 12(c) and Fig. 6 



**Fig. 12(a).** Augmented total spillovers for SSR and core housing markets. 

12 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 



**Fig. 12(b).** Augmented total spillovers for SSR and peripheral housing markets. 



**Fig. 12(c).** Total spillovers from monetary policy and the core housing markets. 



**Fig. 12(d).** Total spillovers from monetary policy and the peripheral housing markets. 

Notably, prior to 2019, monetary policy contributed more to total spillovers than local housing markets, with this trend reversing post2019. The housing market spillover effect is less pronounced when including the homeownership rate during the COVID-19 period compared to using the working-age population, but it peaked at 30 % during the Russian invasion, similar to the pattern observed in Fig. 12 (c). 

Lastly, Fig. 13(d) shows the evolving total spillovers from monetary policy and local housing markets in peripheral countries for the period 2018 to 2023. Short-term monetary policy spillovers range from 

approximately 3 % to 12 %, with a similar magnitude to those in Fig. 12 (d). Local housing markets consistently contribute more to total spillovers than monetary policy, with this gap widening after 2018 and narrowing after 2021. The contribution of local housing markets to total spillovers has steadily increased, peaking at around 30 % during the COVID-19 period, a trend consistent with that shown in Fig. 12(d) and Fig. 7. In peripheral countries, local housing market spillovers continue to exert a more substantial influence than monetary policy shocks. 

13 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 



**Fig. 13(a).** Augmented total spillovers for SSR and core housing markets. 



**Fig. 13(b).** Augmented total spillovers for SSR and peripheral housing markets. 



**Fig. 13(c).** Total spillovers from monetary policy and the core housing markets. 

### _4.4.3. Controlling for building permits growth rates, a supply-side factor_ 

As a proxy for housing supply elasticity, we use building permits. We estimated a VARX model that included the growth rate of building permits. Data on building permits are sourced from the Eurostat database and have been available since the first quarter of 2000. The rolling spillovers were estimated from the first quarter of 2010 to the second quarter of 2023. Fig. 14(a) shows the augmented total spillovers for SSR on the core housing markets. By and large, the trend of total spillovers is similar to that shown in Fig. 12(a), except during the COVID-19 pandemic, when we observe a rise in spillovers, which continued into 2022–2023, reaching a peak of 50 %. Fig. 14(b) displays a similar 

pattern in the augmented total spillovers for SSR on the peripheral housing markets, albeit with a peak of 35 % in 2021, which is slightly lower than the 40 % observed in Fig. 12(b). 

Fig. 14(b) shows the augmented total spillovers for SSR and peripheral housing markets. The trends for the contributions of spillovers attributed to monetary policy and housing markets remain consistent with those observed in core housing markets in Fig. 14(c). However, the gap between the contribution of housing markets and monetary policy is – noticeably larger during the period 2010 2014 when controlling for building permits, compared to the one observed using the VARX model that incorporates working-age population growth rates. Finally, Fig. 14 

14 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 



**Fig. 13(d).** Total spillovers from monetary policy and the peripheral housing markets. 



**Fig. 14(a).** Augmented total spillovers for SSR and core housing markets. 



**Fig. 14(b).** Augmented total spillovers for SSR and peripheral housing markets. 

(d) illustrates that the contributions of monetary policy and housing markets to total spillovers in peripheral economies follow a similar pattern to those shown in Fig. 12(d). Overall, these results suggest that our baseline findings remain robust even with the inclusion of a housing supply elasticity proxy, such as housing permit growth rates. 

### _4.4.4. Excluding 1995_ – _1998 data_ 

Given that the Euro area was established in 1999, we tested the robustness of our baseline results by excluding pre-EA data (i.e., 1995–1998). The baseline VAR model was estimated using data from 1999 onwards, with the rolling estimation period starting from the first 

quarter of 2009 to the second quarter of 2023. Overall, the patterns of augmented total spillovers for SSR in both core and peripheral housing markets remain consistent when excluding the 1995–1998 data. Fig. 15 (a) for the core housing market mirrors Fig. 4 from the baseline model, while Fig. 15(b) for the peripheral housing market replicates the pattern observed in Fig. 5. 

Similarly, the contributions of spillovers attributed to monetary policy and housing markets for core economies (Fig. 15(c)) and peripheral economies (Fig. 15(d)) closely resemble those in Figs. 6 and 7, respectively. These findings indicate that the inclusion of pre-EA data does not significantly affect the estimation results. 

15 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 



**Fig. 14(c).** Total spillovers from monetary policy and the core housing markets. 



**Fig. 14(d).** Total spillovers from monetary policy and the peripheral housing markets. 



**Fig. 15(a).** Augmented total spillovers for SSR and core housing markets. 

### _4.5. Some policy implications_ 

To better understand the policy implications for core and peripheral economies, we first summarize the key differences in the effects of monetary policy between core and peripheral countries, which center on the magnitude and timing of spillovers. In core countries, monetary policy spillovers tend to be stronger in the short run, particularly during periods of unconventional monetary policy, such as after the 2008 global financial crisis. These spillovers also exhibit a substantial increase following major events like the Russian invasion of Ukraine, with 

positive net spillovers from monetary policy to local housing markets remaining significant. In contrast, peripheral countries experienced a slower and more moderate response to monetary policy. The spillovers of monetary policy to local housing markets became more substantive after 2009, with lower positive net spillovers compared to core countries, especially during recent crises. 

Additionally, while core countries saw a sharp rise in augmented total spillovers driven by monetary policy until 2022, peripheral countries experienced a steep decline in total spillovers after 2022. In other words, the housing markets of peripheral countries are more insulated 

16 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 



**Fig. 15(b).** Augmented total spillovers for SSR and peripheral housing markets. 



**Fig. 15(c).** Total spillovers from monetary policy and the core housing markets. 



**Fig. 15(d).** Total spillovers from monetary policy and the peripheral housing markets. 

from monetary policy spillovers, with local housing market dynamics contributing significantly to systemic risks. For core countries, monetary policy is more dominant in driving systemic risks, particularly during major economic crises like the COVID-19 pandemic and the Russian invasion of Ukraine. Peripheral economies exhibit less pronounced systemic risk from both monetary policy and housing market spillovers, despite some increased positive net effects of monetary policy during the pandemic. 

Judging from the above, the heterogeneous effects of monetary policy spillovers on core and peripheral economies are evident, where 

monetary policy spillovers are effective in core countries but ineffective in peripheral economies. Consequently, the fact that stronger core nations are associated with lower housing risks, while weaker peripheral countries may suffer from higher housing risks, leads to a widening divide between core and peripheral countries. 

For core member countries, policy efforts to curb rising house prices should focus on enhancing the coordination between monetary and macroprudential policies. Given the stronger and more immediate spillovers from monetary policy to housing markets, particularly during periods of unconventional monetary policy, there is a need for more 

17 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 

targeted macroprudential tools. These could include stricter loan-tovalue ratios, higher capital buffers for banks with significant exposure to housing, and tighter regulations on speculative real estate investments. Additionally, core countries should monitor cross-border capital flows into housing markets, especially in the wake of economic shocks, such as the Russian invasion of Ukraine, where capital inflows can exacerbate housing price inflation. Coordinating housing policies across the EA can also help mitigate spillover effects that lead to housing market overheating, ensuring that measures taken in one country are supported by broader EA-wide efforts (Agenor et al., 2021; Chiang and Chen, 2023). 

For peripheral countries, policies should be tailored to address the slower and more moderate response of housing markets to monetary policy spillovers. With local housing market dynamics playing a larger role in systemic risks, macroprudential regulations should focus on managing local factors such as speculative lending and regional housing supply constraints. While monetary policy spillovers are less pronounced, the recent positive net effects during the COVID-19 pandemic highlight the need for proactive measures, such as tighter regulation on mortgage lending and speculative real estate activity. Furthermore, peripheral countries would benefit from enhanced collaboration with core economies and the ECB to implement localized policies that account for regional differences while avoiding the amplification of housing market shocks across the EA. 

Finally, given the challenges the ECB’s monetary policy faces in managing peripheral housing markets, it is important to emphasize how core and peripheral members can be better integrated. We suggest that the most effective buffer mechanism would be to enhance communication and cooperation across all member policies, including housing financing, financial market regulation, and fiscal recommendations (Aizenman et a., 2016; Cesaroni et al., 2019; Hallett and Mavrodimitrakis, 2019; Casagrande and Dallago, 2023). 

### **5. Conclusion** 

This paper presents contrasting spillover dynamics between monetary policy and local housing markets in both core and peripheral euro area countries. Core countries exhibit stronger short-term spillovers from monetary policy, particularly during unconventional policy phases, with significant increases following major events, such as the Russian invasion of Ukraine. In contrast, peripheral countries experience more gradual and moderate spillovers, with substantial impacts emerging only after 2009. During the COVID-19 pandemic, core countries saw a notable rise in housing market spillovers, while peripheral countries showed less pronounced increases. In core countries, monetary policy spillovers to housing markets are consistently positive, though smaller during the pandemic. 

The insights gained from our analysis underscore the intricate interplay between monetary policy and housing markets within the euro area, particularly in the aftermath of significant economic disruptions, such as the COVID-19 pandemic. Our findings underscore the critical role that time-varying spillovers play in understanding how monetary policy impacts housing markets. The substantial rise in spillovers among core EA countries, in contrast to more moderate spillovers in peripheral countries, reveals a differentiated response to monetary policy that has evolved. This dynamic interaction, marked by volatile and evolving spillover effects, challenges the efficacy of traditional and unconventional monetary policy measures in stabilizing housing markets. 

Our results illuminate the limitations of relying heavily on unconventional monetary policy tools, such as the zero lower bound (ZLB) and large-scale asset purchases, in managing housing market exuberance. While these measures have historically influenced housing markets, n 

their ability to prevent or mitigate housing booms is increasingly questioned. The observed rise in spillovers suggests that the interconnected nature of core EA housing markets amplifies the effects of monetary policy, potentially leading to widespread housing price increases and heightened systemic risks across the euro area. 

We advocate for a multifaceted strategy to manage housing market stability across the euro area. Future research should explore innovative regulatory frameworks and collaborative policy measures that address the divergent needs of core and peripheral countries. By doing so, the EA can better safeguard against housing market volatility and systemic risks, fostering a more resilient financial system in the face of future economic shocks. 

This study is not without limitations. First, while the Maastricht Treaty sets convergence criteria to promote fiscal alignment, fiscal policy in the Euro Area remains largely decentralized. As Alter and Beyer (2014) note, “In the European Monetary Union context, monetary policy is centralized, whereas fiscal policy remains the responsibility of national governments.” This institutional asymmetry may influence housing market dynamics and interact with monetary policy in ways not captured by our current model. Future research could benefit from incorporating fiscal variables to better assess their joint effects on housing markets alongside monetary policy. 

Second, we acknowledge the potential loss of long-run equilibrium information resulting from our use of house price growth rates in the VAR framework. Lagged adjustment and long-term correction mechanisms are crucial features of housing markets, and cointegration-based approaches, such as the Engle-Granger methodology or the vector error correction model (VECM) framework proposed by Pesaran et al. (2001), are well-suited to capturing such dynamics. However, to our knowledge, no extension of the Diebold-Yilmaz spillover framework currently exists that accommodates cointegrated systems or explicitly models long-run relationships. As such, we recognize this as a methodological limitation and suggest it as a promising avenue for future research. 

Finally, due to the challenges in obtaining consistent time-series data on mortgage regulations and housing supply elasticity across Eurozone countries, we are unable to integrate these factors into our model. We acknowledge this as a limitation of our work and emphasize the importance of considering alternative groupings based on mortgage market liberalization or labor supply elasticity as robustness checks against the core/periphery categorization. Additionally, we recognize the potential role of Basel II in shaping mortgage market dynamics, particularly in periphery countries, where regulatory shifts likely contributed to housing bubbles. While our current analysis did not explicitly address these regulatory changes, we plan to incorporate these insights into future iterations of the study to better capture the effects of regulatory flexibility on housing price movements. 

### **CRediT authorship contribution statement** 

**Shu-hen Chiang:** Writing – original draft, Project administration, Investigation, Funding acquisition, Formal analysis, Conceptualization. **Sandy Suardi:** Writing – review & editing, Writing – original draft, Validation, Investigation, Formal analysis. **Chien-Fu Chen:** Writing – review & editing, Validation, Software, Methodology, Funding acquisition, Data curation. 

### **Declaration of competing interest** 

The authors declare that they have no conflicts of interest to influence the work reported in this paper. 

18 

> _S.-h. Chiang et al.                                                                                                                                                                                                                               Journal of Housing Economics 69 (2025) 102090_ 

### **Appendix** 

#### **Table A1** 

ADF unit root tests for the growth rates of housing prices and SSR. 

||No constant and trend|Constant|Constant and time trend|
|---|---|---|---|
|SSR|−6.360(0)***|−6.328(0)***|−6.461(0)***|
|Belgium|−2.633(2)***|−3.893(1)***|−4.888(1)***|
|France|−2.079(0)**|−2.290(0)|−3.223(0)*|
|Germany|−3.188(1)***|−1.589(2)|−1.082(2)|
|Netherlands|−2.273(1)**|−2.203(1)|−2.303(1)|
|Spain|−2.062(1)**|−2.051(1)|−2.023(1)|
|Italy|−1.861(2)*|−1.841(2)|−2.581(2)|
|Portugal|−2.957(1)***|−4.523(0)***|−4.919(0)***|
|Ireland|−2.757(1)***|−2.706(1)*|−2.650(1)|



Note: The numbers in the parentheses are the lag length included in the ADF regression. The symbols *, **, and *** denote significance at the 10 %, 5 %, and 1 % level. 

#### **Table A2** 

Multivariate Q statistic for autocorrelation of the residuals from VAR models. 

||Statistic|p-value|
|---|---|---|
|VAR model for core countries|_χ_<sup>2</sup>(4) =94_._864|0.626|
||_χ_<sup>2</sup>(8) =206_._873|0.355|
|VAR model for peripheral countries|_χ_<sup>2</sup>(4) =95_._741|0.602|
||_χ_<sup>2</sup>(8) =189_._629|0.689|



### **Data availability** 

Data will be made available on request. 

### **References** 

- Abdallah, C., Lastrapes, W.D., 2013. Evidence on the relationship between housing and consumption in the US: a state-level analysis. J. Money Credit Bank 45, 559–589. 

Agenor, P., Jackson, T., Kharroubi, E., Gambacorta, L., Lombardo, G., Pereira da Silva, L. A., 2021. Assessing the gains from international macroprudential policy cooperation. J. Money Credit Bank 53, 1819–1866. 

Ahlborn, M., Wortmann, M., 2018. The core-periphery pattern of European business cycles: a fuzzy clustering approach. J. Macroecon. 55, 12–27. 

Aizenman, J., Chinn, M.D., Ito, H., 2016. Monetary policy spillovers and the trilemma in the new normal: periphery country sensitivity to core country conditions. J. Int. Money. Finance 68, 298–330. 

Alter, A., Beyer, A., 2014. The dynamics of spillover effects during the European sovereign debt turmoil. J. Bank. & Finan. 42, 134–153. 

Bahadir, B., Lastrapes, W.D., 2015. Emerging market economies and the world interest rate. J. Int. Money. Finance 58, 1–28. 

Battistini, N., Falagiarda, M., Gareis, J., Hackmann, A., Roma, M., 2021. The Euro Area Housing Market During the COVID-19 Pandemic. ECB Economic Bulletin. Issue 7/ 2021. URL: https://www.ecb.europa.eu/pub/economic-bulletin/articles/2021/h tml/ecb.ebart202107_03~36493e7b67.en.html#toc5. 

Bayoumi, T., Eichengreen, B., 1993. Shocking aspects of European monetary integration. In: Torres, F., Giavazzi, F. (Eds.), Adjustment and Growth in the European Monetary Union. Cambridge University Press, Cambridge, pp. 193–240. 

Beraja, M., Fuster, A., Hurst, E., Vavra, J., 2019. Regional heterogeneity and the refinancing channel of monetary policy. Q. J. Econ. 134, 109–183. 

Billio, M., Getmansky, M., Lo, A.W., Pelizzon, L., 2012. Econometric measures of connectedness and systemic risk in the finance and insurance sectors. J. financ. econ. 104, 535–559. 

Blanchard, O., Dell’Ariccia, G., Mauro, P., 2010. Rethinking macroeconomic policy. J. Money Credit Bank 42, 199–215. 

Boeckx, J., Dossche, M., Peersman, G., 2017. Effectiveness and transmission of the ECB’s balance sheet policies. Int. J. Cent. Bank 13, 297–333. 

Brunnermeier, M., Rother, S., Schnabel, I., 2000. Asset price bubbles and systemic risk. Revi. Financ. Stud. 33, 4272–4317. 

Campos, N.F., Macchiarelli, C., 2016. Core and periphery in the European Monetary Union: boyuoumi and Eichengreen 25 years later. Econ. Lett. 147, 127–130. 

Campos, N.F., Macchiarelli, C., 2021. The dynamics of core and periphery in the European monetary union: a new approach. J. Int. Money. Finance 112, 102325. 

- Casagrande, S., Dallago, B., 2023. The European core-periphery divide: towards a new narrative. Eur. J. Econ. Econ. Polic.: Interv. 20, 125–147. 

Cesaroni, T., Elia, E.D., Santis, De, 2019. Inequality in EMU: is there a core-periphery dualism? J. Econ. Asymmetries. 20, e00121. 

Chiang, S., Chen, C., 2023. Macroprudential policy and the real estate market: effectiveness and repercussions. J. Asian Econ. 88, 101625. 

Chow, G.C., Lin, A.-L., 1971. Best linear unbiased interpolation, distribution and extrapolation of time series by related series. Rev. Econ. Stat. 53, 372–375. 

Del Negro, M., Otrok, C., 2007. 99 Luftballons: monetary policy and the house price boom across U.S. states. J. Monet. Econ. 54, 1962–1985. 

Dell’Ariccia, G., Rabanal, P., Sandri, D., 2018. Unconventional monetary policies in the euro area, Japan and the United Kingdom. J. Econ. Perspect. 32, 147–172. 

De Santis, R., Cesaroni, T., 2016. Current account ‘core-periphery dualism’ in the EMU. World Econ. 39, 1514–1538. 

Diebold, F.X., Yilmaz, K., 2009. Measuring financial asset return and volatility spillovers, with application to global equity markets. Econ. J. 119, 158–171. 

Diebold, F.X., Yilmaz, K., 2012. Better to give than to receive: predictive directional measurement of volatility spillovers. Int. J. Forecast. 28, 57–66. 

Diebold, F.X, Yilmaz, K., 2014. On the network topology of variance decompositions: measuring the connectedness of financial firms. J Econ. 182, 119–134. 

Duca, J.V., Popoyan, L., Wachter, S.M., 2019. Real estate and the Great Crisis: lessons for macroprudential policy. Contemp. Econ. Policy. 37, 121–137. 

Eickmeier, S., Hofmann, B., 2013. Monetary policy, housing booms and financial (im) balances. Macroecon. Dyn. 17, 830–860. 

Fischer, M.M., Huber, F., Pfarrhofer, M., Staufer-Steinnocher, P., 2019. The dynamic impact of monetary policy on regional housing prices in the United States. Real Estate Econ. 49, 1039–1068. 

Fratantoni, M., Schuh, S., 2003. Monetary policy, housing and heterogeneous regional markets. J. Money Credit Bank 35, 557–589. 

Gamber, W., Graham, J., Yadav, A., 2023. Stuck at home: housing demand during the COVID-19 pandemic. J. Hous. Econ. 59, 101908. 

Geanakoplos, J., Axtell, R., Farmer, J.D., Howitt, P., Conlee, B., Goldstein, J., Hendry, M., Palmer, N.M., Yang, C., 2012. Getting at systemic risk via an agent-based model of the housing market. Am. Econ. Rev. 102, 53–58. 

Georgiadis, G., 2015. Examining asymmetries in the transmission of monetary policy in the euro area: evidence from a mixed cross-section global VAR model. Eur. Econ. Rev. 75, 195–215. 

Giuliodori, M., 2005. The role of house prices in the monetary transmission mechanism across European countries. Scott. J. Polit. Econ. 52, 519–543. 

Hallett, A.H., Mavrodimitrakis, C., 2019. Cooperation vs. leadership in a core-periphery monetary union: inter-country vs. inter-institutional policy coordination. 

J. Macroecon. 59, 103–122. 

Hoynck, C., Roma, M., Schlieker, K., 2025. Developments in the recent euro area house price cycle. In: ECB Economic Bulletin, 2025/2. 

Hulsewig, O., Rottmann, H., 2021. Euro area housing prices and unconventional monetary policy surprises. Econ. Lett. 205, 1099602. 

Jorda, ` O., Schularick, M., Taylor, A.M., 2016. The great mortgaging: housing finance,<sup>`</sup> crises and business cycles. Econ. Policy 31, 107–152. 

Klobner, S., Wagner, S., 2013. Exploring all VAR orderings for calculating spillovers? Yes, we can! A note on Diebold and Yilmaz (2009).  J. Appl. Econom. 29, 172–179. 

Krippner, L., 2020. A note of caution on shadow rate estimates. J. Money Credit Bank 52, 951–962. 

19 

_Journal of Housing Economics 69 (2025) 102090_ 

Kuttner, K., 2012. Low Interest Rates and Housing Bubbles: Still No Smoking Gun. Department of Economics Working Papers 2012-01. Department of Economics, Williams College. 

Mankiw, G.N., Weil, D.N., 1989. The baby boom, the baby bust and the housing market. Reg. Sci. Urban. Econ. 19, 235–258. Monnet, E., Wolf, C., 2017. Demographic cycles, migration and housing investment. J. Hous. Econ. 38, 38–49. 

Ouerk, S., Boucher, C., Lubochinsky, C., 2020. Unconventional monetary policy in the Euro area: shadow rate and light effects. J. Macroecon. 65, 103219. Peersman, G., Smets, F., 2005. The industry effects of monetary policy in the Euro area. Econ. J. 115, 319–342. 

Pesaran, M.H., Shin, Y., Smith, R.J., 2001. Bounds testing approaches to the analysis of level relationships. J. Applied Econom. 16, 289–326. 

Rafiq, M.S., Mallick, S.K., 2008. The effect of monetary policy on output in EMU3: a sign restriction approach. J. Macroecon. 30, 1756–1791. Reinhart, C.M., Rogoff, K.S., 2008. Is the 2007 US sub-prime financial crisis so different? An international historical comparison. Am. Econ. Rev. 98, 339–344. Rodriguez-Fuentes, C.J., Dow, S.C., 2003. EMU and the regional impact of monetary policy. Reg. Stud. 37, 969–980. 

Wachter, S., 2015. The housing and credit bubbles in the United States and Europe: a comparison. J. Money Credit Bank 47, 37–42. 

Wu, J., Xia, F., 2016. Measuring the macroeconomic impact of monetary policy at the zero lower bound. J. Money Credit Bank 48, 253–291. 

Wu, J., Xia, F., 2020. Negative interest rate policy and yield curve. J. Appl. Econom. 35, 653–672. 

20 

