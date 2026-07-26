---
title: The of shocks on time-varying impact uncertainty the co-movement of regional housing prices of the United Kingdom
type: paper
source_pdf: raw/papers/Cepni_The time varying impact of uncertainty shocks on the comovement of regional housing prices of the United Kingdom_2025.pdf
converted: 2026-07-26
---



## ARTICLE 



> https://doi.org/10.1057/s41599-025-04494-8 **OPEN** 

# The of shocks on time-varying impact uncertainty the co-movement of regional housing prices of the United Kingdom 

Oguzhan Cepni 1,2,3✉, Hardik A. Marfatia4 & Rangan Gupta5 

The housing markets in districts across the United Kingdom (UK) co-move over time. We use the dynamic factor model to decompose the co-movement in house prices of the smallest possible geographical unit into national, regional, and idiosyncratic factors. Using the Bayesian time-varying parameter VAR (TVP-VAR) model, we study the dynamic impact of uncertainty shocks on synchronization in housing markets. We find that the estimated national factor accurately tracks the overall housing market cycles in the UK and explains nearly all the variations in East, South–East, and South–West districts. Furthermore, the results from TVP-VAR indicate that the estimated response of the national factor to uncertainty shocks is negative. However, the magnitude of the effect is more pronounced and persists longer in the case of housing price uncertainty shocks compared to overall economic uncertainty. Overall, our results suggest that uncertainty about house prices is a primary driver of the national factor. 

> 1 Copenhagen Business School, Frederiksberg, Denmark. 2 Ostim Technical University, Ankara, Türkiye. 3 University of Edinburgh Business School, Centre for Business, Climate Change, and Sustainability, Edinburgh, United Kingdom.<sup>4</sup> Northeastern Illinois University, Chicago, IL, USA.<sup>5</sup> University of Pretoria, Pretoria, South Africa.<sup>✉</sup> email: oce.eco@cbs.dk 

1 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

### Introduction 

he turmoil of the global financial crisis (GFC), resulting in heightened volatility and uncertainty, had its roots in the Tsubprime mortgage crisis within the housing market of the United States (US), as outlined by Leamer (2007, 2015), before affecting the world economy (Hirata et al. 2013). Given this, several studies perform structural vector autoregressive (VAR) model-based analysis to highlight the effect of uncertainty shocks on international and US state-level house price movements (André et al. 2017; Antonakakis et al. 2016, 2015; Aye, 2018; Aye et al. 2019; Balcilar et al. 2021; Bouri et al. 2021; Choudhry, 2020; Chow et al. 2018; Christou et al. 2017, 2019; Christidou and Fountas, 2018; El Montasser et al. 2016; Gabauer et al. 2024; Gupta et al. 2021; Huang et al. 2020; Nguyen Thanh et al. 2020; Strobel et al. 2020; Su et al. 2016; van Eyden et al. 2022). There is also evidence in the literature for both in- and out-of-sample predictability of house prices emanating from uncertainty. 

The papers mentioned above outline multiple channels through which uncertainty can affect the housing market. First, increased uncertainty in housing demand or the cost of financing can cause developers to postpone new construction. This reduces supply due to the irreversible nature of housing investment decisions and the inelasticity of supply caused by geographical constraints. Second, increased uncertainty about future employment, income, and wealth might cause households to postpone their home-buying decision and instead increase precautionary savings. Third, when uncertainty about employment and income increases the probability of default on mortgages, lenders may reduce or deny mortgages to riskier borrowers. Taken together, these decisions in response to uncertainty can cause a decrease in demand and prices in the housing markets unless demand for other assets is more sensitive to uncertainty. Fourth, the user cost of housing is equal to the sum of the depreciation rate of the dwelling, the maintenance and repair costs as a fraction of the current value, the marginal income tax rate, the nominal interest rate, the property tax rate, and the expected nominal housing price inflation rate. The last component is likely influenced by uncertainty surrounding various determinants of housing price, including income, interest and tax rates, and housing market regulations, among others. Therefore, it is reasonable to expect an empirical link between uncertainty and housing prices and/or returns. The existing literature suggests that this effect is negative, and uncertainty is characterized as an adverse demand shock. 

Against this backdrop, this study contributes to the existing literature by analyzing the co-movement of housing markets across the United Kingdom (UK). Specifically, we examine the role of housing market-related uncertainty shocks in driving synchronous movements in regional housing markets, while controlling for standard macroeconomic shocks. We employ a Bayesian time-varying parameter VAR (TVP-VAR) model to analyze quarterly data from 1996:Q2 to 2019Q2. Within this framework, we also analyze the impact of aggregate macroeconomic uncertainty shocks over the period 1998:Q1 to 2020:Q3, comparing their effect to those of sector-specific uncertainty-specifically, housing uncertainty in driving regional housing price co-movement over the common sample of 1998:Q1 to 2019:Q2.<sup>1</sup> The decision to focus on the UK is primarily driven by the availability of data on housing market uncertainty, as developed by Yusupova et al. (2020), available in the public domain. Moreover, our sample period spanning multiple business cycles, the GFC, the European sovereign debt crisis, and the recent Brexit process provides a compelling case for studying the time-varying impact of uncertainty shocks on the evolution of house price movements in the UK. 

This is an interesting case study, as the Brexit process likely affected the UK housing market by reducing foreign 

investment and deferring purchases, thereby increasing uncertainty in both the housing market and the broader economy. Furthermore, recent studies suggest that the effect of uncertainty on the economy is state-dependent, varying according to factors such as the business cycle (recessions or expansions), credit constraints, and the stance of monetary policy (conventional or unconventional) (see, for example, Alessandri and Mumtaz, 2019, Andreasen et al. 2024, Caggiano et al. 2014, 2017a, b, 2020, 2021a, b, 2022, Pellegrino et al. 2023). In other words, the effect of uncertainty on the economy is likely nonlinear across regimes, as defined by the initial state of economic and financial variables. 

By using a time-varying approach, we model each point in time as a specific state or regime that characterizes the underlying variables of the economic system. This approach enables us to trace the evolution of uncertainty shocks over time without the need to explicitly define the regime or the underlying drivers of the economy. In this sense, a time-varying method offers a flexible and general framework for capturing the nonlinearity in the relationship between uncertainty and our variables of interest, including the housing market. To this end, we draw on the theoretical framework of Andreasen et al. (2024), who estimated a New Keynesian model with recursive preferences to replicate state-contingent responses approximating them to third order around the risky steady state. This state arises from a stronger upward nominal pricing bias during economic downturns, relative to upswings. 

At this stage, it is important to explain why we focus on the comovement of regional housing prices and how we capture this synchronicity econometrically. First, there is broad consensus that the UK housing market is segmented (see, for example, Antonakakis et al. 2016; Montagnoli and Nagayasu, 2015; Tsai, 2015; Zhang et al. 2021). Our own demographic analysis of the UK further supports this consensus. As a result, the market’s response to aggregate macroeconomic shocks should not be analyzed as a single, homogeneous market based on the national house price index (Gupta et al. 2023). Second, to account for this segmentation, we examine the synchronization of housing prices at the smallest geographic level for which data are available Nomenclature of Territorial Units for Statistics (NUTS) level 3, which includes counties, districts, or groups of unitary authorities (referred to as “districts” henceforth). In doing so, we build on the work of Del Negro and Otrok (2007), Fairchild et al. (2015), Gupta et al. (2021), Marfatia (2021), Sheng et al. (2021), and Luo and Ma 2016, who have studied state-level housing markets in the US and across OECD countries. 

We employ a Bayesian dynamic factor model (DFM) to decompose the movement in real house prices across all NUTS-3 level districts in the UK into three components: a national factor that captures fluctuations common to all districts; 10 NUTS-1 level regional factors that capture regional dynamics; and 144 district-specific factors unique to each district. The segmentation of the UK housing market is also well-established through the “Ripple Effect” literature, which shows that local shocks significantly influence local house prices. This further underscores the need to disaggregate overall house price movements into national, regional, and local components-a task we achieve using the DFM, especially when analyzing the impact of national-level shocks. 

In other words, we analyze the effects of various aggregate macroeconomic and uncertainty factors on the portion of housing prices that reflects a common structure–i.e., synchronicity across all 144 districts. This decomposition does not negate market segmentation; rather, it explicitly accounts for it by isolating the national factor (the synchronous component) and 

2 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

examining the role of economy-wide shocks in driving it. The DFM allows us to explicitly quantify the contributions of national, regional, and local components in driving overall housing prices in each district. However, our primary focus is on the common factor (which explains a significant portion of the variation in overall housing prices) and the national shocks that drive its movement. Naturally, regional and local variables are necessary to explain the corresponding regional and districtspecific housing factors. 

This modeling strategy enables us to study the nature of synchronization over time and assess the relative importance of each latent factor in influencing housing price dynamics in each district. By distinguishing the national factor from local factors in the housing market, we can use the TVP-VAR model to analyze the impact of aggregate macroeconomic and uncertainty shocks on the common factor, thereby providing reliable inferences. The movement in local factors is likely driven by circumstances specific to each geographic market, and if overall house prices are not decomposed into national and local components, the effects of macroeconomic and housing uncertainties are underestimated. 

Given the well-established historical role of housing prices as a leading indicator in the UK (Plakandaras et al. 2020), our analysis holds significant importance. Understanding the relative importance of macroeconomic and uncertainty shocks driving the housing market, particularly the national/common factor–is crucial for policymakers seeking to avoid the catastrophic recessionary effects observed during the GFC. In this context, identifying the time-varying drivers of the national component of house prices across the UK would allow policymakers to devise state-contingent, national-level monetary and fiscal policies. Such measures could mitigate the adverse effects of uncertainty shocks on the housing sector-both at the national and regional levels through the common factor and help stabilize the broader economy. 

We find that the unobserved national factor we model effectively captures the aggregate movements in UK house prices, providing evidence of the accuracy of our modeling approach. Our results also suggest a synchronized housing market across the UK. National-level factors, such as monetary policy and economic growth, explain 80% or more of the variation in house prices in several districts. Indeed, the national factor accounts for nearly all the variation in house prices in districts across the East, South-East, and South-West regions. This contrasts with districts in the North East, North West, Yorkshire the Humber, and Wales, where regional factors explain a substantial portion of the variation (ranging from 25% to 55%). District-specific factors explain >30% of the variation in house prices in only three of the 143 districts: Shropshire, Breckland South Norfolk, and Wandsworth. While the national or common factor plays a dominant role in shaping overall house prices in each district, it is important to note that the concept of the “Ripple Effect” likely still exists. Regional and local shocks to housing prices can lead to districtspecific behavior that does not necessarily produce a homogeneous effect across the broader UK housing market. 

The results from the TVP-VAR model show that the estimated response of the national factor to uncertainty shocks is negative. However, the magnitude of the effect is more pronounced in the presence of housing price uncertainty (HPU) shocks. On the other hand, the national factor responds more quickly to economic policy uncertainty shocks, but the subsequent decrease in the national factor is not long-lasting and dissipates within ten quarters. When both types of uncertainty are included in the TVP-VAR model simultaneously, the response of the national factor to economic policy uncertainty shocks becomes statistically insignificant. In contrast, the negative impact of HPU shocks on housing returns remains statistically significant. This result 

suggests that uncertainty about house prices is the primary driver of the national factor. 

To the best of our knowledge, this is the first paper to provide a time-varying analysis of the housing market and overall macroeconomic uncertainties in the UK and their impact on the comovements of house prices. In this regard, the only related work is that of Nguyen Thanh et al. (2020), in which the authors developed and used a real estate-based uncertainty index for the US to highlight its stronger negative impact, compared to macroeconomic uncertainty, on the aggregate housing market in a constant-parameter VAR setting over the period 1970–2017.<sup>2</sup> We also provide a methodological contribution, as Nguyen Thanh et al. (2020) used vector autoregressions and Granger-causality analysis to highlight the role of their new uncertainty measure. However, we go a step further. The contribution of our paper is to uncover the time-varying role of uncertainty shocks in driving latent co-movements in UK house price changes. Furthermore, our modeling approach, unlike Nguyen Thanh et al. (2020), enables us to uniquely uncover the impact of HPU shocks in driving the co-movement of house prices, especially during the GFC and Brexit referendum. Regarding our findings, while it is intuitive to find HPUs driving house price co-movements at the national level, we provide a more natural way to capture the latent co-movements and the time-specific responses of these latent co-movements in house prices across districts. The paper also provides the precise response time path for different measures of uncertainty—an insight that is valuable for real estate consumers and investors as well as policymakers. 

The rest of the paper is organized as follows: “Data” describes the data, while “Methodologies” is devoted to the TVP-VAR and DFM methodologies; “Empirical Results” presents the empirical results, and “Robustness Check” concludes. 

### Data 

One major obstacle to constructing accurate house price indices is the high degree of heterogeneity of real estate properties. To account for price differences in homes with varying characteristics, the Housing Observatory Price Indices (HOPIs) is based on the popular repeat sales methodology. Repeat sales methodologies control for property characteristics by assessing how valuations of the same property change over time and are recognized as one of the most reliable means of measuring house price inflation. The construction of HOPIs employs data from the HM Land Registry Price Paid database, which covers all property sales in England and Wales that are sold for value and lodged with the HM Land Registry for registration. The data for the 144 districts under NUTS-3 is available for download from the website of the UK Housing Observatory.<sup>3</sup> 

To transform the data into real values, each series is deflated with the consumer price index (CPI), derived from the main economic indicators (MEI) database of the OECD, which is also the source of the real gross domestic product (GDP) data. Note that, while analyzing the impact of uncertainty shocks (the details of which we describe below) on the national real house price growth factor, we control for quarter-on-quarter real GDP growth and CPI-based inflation, in addition to a uniform measure of both conventional and unconventional monetary policy decisions. To measure the stance of monetary policies, we consider the shadow-short rate (SSR) developed by Wu and Xia 2016 (2016; SSRWX),<sup>4</sup> given that our period of analysis involves the zero lower bound (ZLB) scenario in the wake of the Great Recession and the GFC.<sup>5</sup> 

We now turn to the descriptions of the housing market-related and aggregate macroeconomic uncertainties.<sup>6</sup> We gather the quarterly HPU index from the UK Housing Observatory as well, 

3 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

just like the HOPIs.<sup>7</sup> The HPU index is constructed by Yusupova et al. (2020) using the methodology suggested by Baker et al. (2016). The HPU is an index of search results from five large newspapers in the UK: The Guardian, The Independent, The Times, Financial Times, and Daily Mail. In particular, the authors use LexisNexis digital archives of these newspapers to obtain a quarterly count of articles that contain the following three terms: ‘uncertainty’ or ‘uncertain’; ‘housing’ or ‘house prices’ or ‘real estate’; and one of the following: ‘policy’, ‘regulation’, ‘Bank of England’, ‘mortgage’, ‘interest rate’, ‘stamp-duty’, ‘tax’, ‘bubble’ or ‘buy-to-let’ (including variants like ‘uncertainties’, ‘housing market’ or ‘regulatory’). To meet the search criteria, an article must contain terms in all three categories. The resulting search counts are then scaled by the total number of articles in the given newspaper and in the given quarter. Finally, to obtain the HPU index, Yusupova et al. (2020) average across the five newspapers by quarter and normalize the index to a mean of 100. As far as the overall uncertainty index of the UK is concerned, we utilize the economic policy uncertainty (EPU) index of Baker et al. (2016). This measure is based on the number of news articles containing the terms uncertain or ‘uncertainty’, ‘economic’ or ‘economy’, as well as policy-relevant terms: ‘policy’, ‘tax’, ‘spending’, ‘regulation’, ‘Bank of England’, ‘budget’, and ‘deficit’.<sup>8</sup> 

Based on data availability, our analysis involving the HPU runs from 1996:Q2 to 2019:Q2, while that of EPU from 1998:Q1 to 2020:Q3, and for both HPU and EPU over 1998:Q1 to 2019:Q2, with the start and end dates are driven primarily by the real housing price growth factor and the uncertainty indexes. The national factor is stationary by design, while we work with GDP growth and inflation to ensure stationarity, but the SSRs and natural logarithms of HPU and EPU are found to have no unit root issues, and are thus used in levels. 

Table 1 presents the summary statistics of house price growth in NUTS-3 districts. The results show that the average house price growth across districts is ~3.75%. However, housing returns in southern districts are higher than their northern counterparts. One explanation for this could be the proximity to London. Miles (2020) finds that regions near London exhibit the most comovement, while those further from London show the most divergence. This is also expected given the north-south divide in the UK. The results also reveal significant volatility in housing markets across districts. The housing markets in the West Midlands and most of the East are relatively less volatile than those in the rest of the UK. Despite potential synchronizations between housing markets, we find wide variations in housing returns across different regions. These preliminary findings motivate the central idea of the paper to understand the dynamic role of uncertainty in driving regional housing prices. 

The size (area, population, etc.) and demographic composition vary across the districts in the UK. Take, for example, population distribution. The most recent data from the Office for National Statistics (ONS) indicates that the UK’s population of 67 million (mid-2022) is unevenly spread across districts. Populous districts like Birmingham and Leeds have over a million people, while others have much smaller populations. With a median age of 40 years, the demographic composition shows higher proportions of younger people in urban areas and higher proportions of older populations in rural areas. The greatest proportions of people aged 65 years or over are predominantly located in the SouthWest region. These disparities are also evident at the economic level. Urban areas like London, Manchester, and Birmingham generally have higher average incomes compared to their rural counterparts. However, challenges such as housing affordability, congestion, and higher living costs persist in the urban landscape. In contrast, rural districts in the NorthEast and South-West often rely on agriculture, tourism, and small-scale manufacturing for 

growth, resulting in lower population densities and below-average incomes. In these regions, the absence of high-quality jobs, healthcare infrastructure, and educational facilities is a major challenge. These demographic and economic disparities motivate the main idea of the paper: to explore the national, regional, and district-specific factors that drive house price variations across the UK and study how these dynamically respond to uncertainty surrounding housing markets in comparison to other forms of uncertainty. 

Zooming in on the selected five largest and smallest districts based on geographical area provides additional insights (Table 2). Household income in geographically smaller districts is at least three times higher than in larger ones. This income disparity may help explain why smaller districts attract more foreign-born residents, who make up an average 45.7% of the population in these districts, compared to just 7.7% in larger ones. Consequently, the proportion of the white population is significantly lower in smaller districts (59.2%) than in larger districts (94.5%). Admittedly, these disparities are found at the two extremes of the distribution; nevertheless, they reinforce the paper’s main argument: decomposing geographical disparities in house price movements and analyzing the dynamic impact of uncertainty on the common factor that drives house prices. 

### Methodologies 

Dynamic factor model. The movement of house prices and their relationship with macroeconomic developments are central to the understanding of housing markets. It is well-established that house prices in different geographical segments within a country or region move together. However, how this co-movement relates to a wide array of macroeconomic and financial forces (beyond just monetary policy, for instance, as in Del Negro and Otrok (2007)) has gained attention only recently (Gupta et al. 2023, 2021; Marfatia, 2021; Sheng et al. 2021). One hurdle in this regard is the unobserved nature of the forces that drive the comovement of house prices. While we observe that house prices move together, the exact reasons for their co-movement remain latent. Thus, we employ a DFM which, prima facie, assumes that the exact forces behind the synchronous pattern in the housing market are unobserved. 

More specifically, we decompose NUTS-3 level real house price growth into national, regional, and unit-specific factors. The national factor captures shocks, such as monetary policy shocks, that affect housing markets across the country, albeit to varying degrees. In addition to the national factor, house prices in North West UK, for example, have risen significantly post-2009 compared to South West UK. Thus, regional dynamics play an important role in driving house prices in particular geographic segments. Finally, there is a district-specific factor unique to each district. One limitation of this decomposition is that the districtspecific factor may also include house-specific effects. However, in our case, we do not see this as a binding limitation. Results show that any further segmentation to capture house-specific effects is unlikely to produce valuable insights. As discussed in the results section below, the variance decomposition shows little role for district-specific factors in most cases. The proposed decomposition strategy is, therefore, appropriate in the present context. Moreover, it is consistent with the widely used modeling approach in the literature (Del Negro and Otrok, 2007, and subsequent works). Thus, the real house price growth rate (hi,t) for each i unit at NUTS-3 (i = 1, . . . , N) is decomposed into three latent factors. 



In the above equation, the subscript i represents each of the N unit at NUTS-3 level. The degree to which the national and regional-level 

4 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

|Table 1 Summary st<br>|atisti<br>Mean|cs.<br><br>Median|SD||Mean|Median|SD||Mean|Median|SD|
|---|---|---|---|---|---|---|---|---|---|---|---|
|North East<br>Hartlepool and<br>Stockton|1.79|0.46|7.71|West Midlands<br>Herefordshire|4.19|5.32|6.85|South East<br>Berkshire|3.97|5.27|7.05|
|S Teesside<br>|3.49<br>|2.79<br>|7.16<br>|Worcestershire<br>|3.42<br>|3.02<br>|6.51<br>|Milton Keynes<br>|4.43<br>|4.86<br>|6.42<br>|
|Darlington<br>|2.03<br>|0.88<br>|7.83<br>|Warwickshire<br>|3.68<br>|3.51<br>|6.25<br>|Buckinghamshire<br>|4.87<br>|5.18<br>|7.23<br>|
|Durham<br>Numberland|1.92<br>268|0.83<br>220|7.70<br>757|Telford and Wrekin<br>Shropshire|3.30<br>509|2.98<br>629|6.64<br>720|Oxfordshire<br>BrightonandHove|3.94<br>546|4.44<br>639|7.17<br>752|
|Tid|.<br>531|.<br>604|.<br>706|Stk--Tt|.<br>497|.<br>548|.<br>722|<br>ES|.<br>423|.<br>411|.<br>694|
|ynese<br>|.<br>|.<br>|.<br>|oeonren<br>|.<br>|.<br>|.<br>|ussex<br>|.<br>|.<br>|.<br>|
|Sunderland<br>|2.72|1.89|7.45|Staffordshire<br>|3.29|2.99|6.45|W Surrey|3.87|4.48|6.66|
|North West<br>WCumbria|301|166|698|Birmingham<br>Solihull|3.47<br>368|3.18<br>392|6.66<br>658|E Surrey<br>WSussex(SW)|4.40<br>438|5.48<br>555|6.79<br>716|
|<br>E Cumbria<br>Manchester|.<br>2.89<br>4.50|.<br>1.71<br>4.72|.<br>6.90<br>8.40|Coventry<br>Dudley|.<br>3.85<br>3.21|.<br>4.29<br>3.19|.<br>6.85<br>6.36|<br>W Sussex (N E)<br>Portsmouth|.<br>3.90<br>3.98|.<br>2.82<br>4.30|.<br>7.01<br>6.99|
|Manchester S W<br>MhtSE|3.45<br>399|4.18<br>402|6.05<br>648|Sandwell<br>Wlll|3.01<br>307|2.91<br>302|6.95<br>674|Sampton<br>IlfWiht|3.77<br>403|3.78<br>414|6.55<br>696|
|anceser  <br>Manchester N W|.<br>2.71|.<br>2.25|.<br>7.19|asa<br>Wolverhampton|.<br>2.60|.<br>2.16|.<br>7.49|se o g<br>S Hampshire|.<br>3.58|.<br>2.92|.<br>7.63|
|Manchester N E|2.88|2.88|6.92|East||||Central Hampshire|4.08|4.78|6.59|
|Blackburn|213|095|733|Peterborough|512|621|734|NHampshire|428|515|683|
|Blackpool<br>|.<br>4.09<br>|.<br>2.81<br>|.<br>7.41<br>|Cambridgeshire<br>|.<br>4.21<br>|.<br>5.22<br>|.<br>6.67<br>|<br>Medway<br>|.<br>3.59<br>|.<br>3.58<br>|.<br>6.71<br>|
|Lancaster and Wyre|1.80|1.88|7.71|Suffolk|4.13|4.53|6.88|Kent Thames Gateway|4.39|4.26|7.23|
|Mid Lancashire|2.53|1.47|7.15|Norwich and E Norfolk|4.20|4.42|6.65|E Kent|4.59|4.88|7.10|
|E Lancashire<br>|2.27<br>|1.88<br>|7.08<br>|N and W Norfolk<br>|3.51<br>|3.39<br>|6.89<br>|Mid Kent<br>|4.51<br>|4.92<br>|7.62<br>|
|Chorley and W<br>|2.49|1.69|7.50|Breckland and S Norfolk|2.26|1.06|7.65|W Kent|4.04|4.30|7.00|
|Lancashire<br>Warrington|184|040|759|Luton|321|332|689|SouthWest||||
|ChhiE|.<br>323|.<br>297|.<br>620|Htfdhi|.<br>467|.<br>549|.<br>697|<br>BitlCitf|524|607|743|
|esre <br>Cheshire W and<br>|.<br>3.04|.<br>2.58|.<br>6.42|erorsre<br>Bedford|.<br>4.34|.<br>5.02|.<br>7.39|rso, y o<br>Bath, Somerset|.<br>4.29|.<br>4.96|.<br>7.10|
|Chester<br>E Merseyside<br>|2.80<br>|2.66<br>|7.14<br>|Central Bedfordshire<br>|5.91<br>|6.54<br>|7.34<br>|Gloucestershire<br>|2.62<br>|1.73<br>|7.23<br>|
|Liverpool<br>|4.95<br>|5.42<br>|7.17<br>|Send-on-Sea<br>|3.77<br>|3.81<br>|7.28<br>|Swindon<br>|4.05<br>|3.45<br>|6.88<br>|
|Sefton<br>Wirral|2.74<br>3.18|2.23<br>2.72|7.69<br>7.22|Thurrock<br>EssexHavenGateway|4.23<br>4.06|5.94<br>4.36|7.25<br>7.41|Wiltshire<br>BournemouthandPoole|4.30<br>4.11|5.03<br>4.22|7.30<br>7.13|
|Yorkshire and the<br>||||<br>W Essex|4.39|5.01|6.81|<br>Dorset|3.97|4.38|6.88|
|Humber<br>Kingston upon Hull,<br>Citof|3.45|3.01|6.59|Heart of Essex|4.64|5.26|6.90|Somerset|3.71|3.29|7.03|
|y <br>dfYkh||||h||||lldlf||||
|E Riing o orsire|2.94|1.66|7.52|Essex Tames Gateway|4.72|5.21|7.12|Cornwa an Ises o<br>|3.93|3.32|7.04|
|N and N E Lincolnshire|2.70|1.76|7.53|London||||Scilly<br>Plymouth|3.51|4.17|7.31|
|York|3.16|3.33|6.75|Camden and City of<br>|5.69|6.66|7.06|Torbay|2.84|2.23|7.12|
|N Yorkshire|3.25|2.83|6.84|London<br>Wminster|4.08|4.35|7.40|Devon|4.95|5.56|6.70|
|Barnsley, Doncaster<br>Sheffeld<br>|2.67<br>5.08<br>|1.74<br>5.53<br>|7.64<br>7.58<br>|Kensington, Chelsea<br>Wandsworth<br>|6.06<br>2.56<br>|7.23<br>1.82<br>|7.80<br>7.24<br>|Wales<br>Isle of Anglesey<br>|3.44<br>|3.49<br>|7.39<br>|
|Bradford|2.31|1.46|6.89|Haringey and Islington|4.15|4.47|7.18|Gwynedd|3.11|2.11|7.22|
|Leeds|3.72|2.59|7.58|Lewisham and Swark|3.21|1.98|7.63|Conwy and Denbighshire|3.99|4.11|7.43|
|Calderdale and Kirklees|274|208|726|Lambeth|569|624|780|SWWales|287|218|757|
|<br>Wakefeld<br>|.<br>3.15|.<br>2.45|.<br>6.80|Bexley and Greenwich<br>|.<br>5.03<br>|.<br>5.62<br>|.<br>7.04<br>|<br>Central Valleys<br>|.<br>2.96<br>|.<br>2.66<br>|.<br>6.87<br>|
|East Midlands<br>Derby|3.44|2.81|7.45|Barking & Dagenham<br>Redbridge and Waltham<br>F|4.64<br>5.68|4.05<br>5.86|7.79<br>7.49|Gwent Valleys<br>Bridgend and Neath Port<br>Tlb|4.12<br>2.74|5.06<br>2.31|6.53<br>7.06|
|E Derbyshire<br>S and W Derbyshire|3.13<br>3.49|2.66<br>3.03|7.31<br>6.91|orest<br>Enfeld<br>Bromley|5.91<br>5.02|5.83<br>6.01|7.03<br>7.12|aot<br>Swansea<br>Monmouthshire and<br>Nt|3.54<br>3.19|3.17<br>2.95|6.99<br>7.22|
|Nih|334|276|724|Cd|497|541|790|ewpor<br>CdiffdVlf|363|323|650|
|ottngam|.|.|.|royon|.|.|.|ar an ae o<br>|.|.|.|
|N Nottinghamshire|3.66|3.52|6.79|Merton, Kingston|4.01|4.35|7.19|Glamorgan<br>Flintshire and Wrexham|2.99|2.20|7.08|
|S Nottinghamshire<br>|1.99<br>|1.17<br>|7.37<br>|Barnet<br>|4.88<br>|5.20<br>|7.37<br>|Powys|2.79|1.94|6.92|
|Leicester<br>Leicestershire and|3.65<br>3.33|3.73<br>2.53|6.81<br>6.84|Brent<br>Ealing|4.16<br>4.92|4.31<br>5.77|7.12<br>6.69|||||
|Rutland<br>WNthi|320|314|724|HdHillid|536|615|721|||||
|amponsre<br>N Namptonshire|.<br>3.92|.<br>4.35|.<br>6.87|arrow an ngon<br>Hounslow and<br>|.<br>5.05|.<br>6.08|.<br>7.55|||||
|Leicestershire and<br>|3.33|2.53|0.69|Richmond<br>Ealing|4.92|5.77|0.68|||||
|Rutland<br>||||||||||||
|W Namptonshire|3.20|3.14|0.73|Harrow and Hillingdon|5.36|6.15|0.73|||||
|N Namptonshire|3.92|4.35|0.69|Hounslow and<br>Rihd|5.05|6.08|0.76|||||
|Lincolnshire<br>This table reports the summar|3.47<br>y statisti|3.27<br>cs (mean, me|7.15<br>dian, and s|cmon<br>tandard deviations) of real house|prices at|NUT-3 distric|t level.|||||



factors affect house price is captured by factor loadings, β<sup>n</sup> i<sup>andβr</sup> i<sup>,</sup> respectively. The housing market factors unique to NUTS-3 level units are captured by the idiosyncratic component, ϵi,t. Our particular interest lies in the national-level factor, f<sup>n</sup> t<sup>, as it measures</sup> the role of common factor that affects all the markets. 

To model the latent factors, f<sup>n</sup> t<sup>,f r</sup> t<sup>,andϵi,t,wefollowthe</sup> standard assumption in the literature of an autoregressive (AR) process. Thus, 

f<sup>n</sup> t<sup>¼ ϕ</sup> 1<sup>nf n</sup> t�1<sup>þ ::: þ ϕn</sup> p<sup>f n</sup> t�p<sup>þ υn</sup> t<sup>; υn</sup> t<sup>�i:i:d:N</sup> �<sup>0; σ2</sup> n�; ð2Þ 

5 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

Table 2 Demographic overview: largest and smallest districts (by geographical area). 

||Geographical|Gross disposable|White population (%)|Foreign-born|Full employment (%)|
|---|---|---|---|---|---|
|District/area<br>Largest districts (by geograph|Area (sq km)<br>ical area)|household income (£)|White population (%)|Population (%)|Share of (%)|
|North Yorkshire|8040|28,184|94.2|11.4|79|
|Northumberland|5032|20,380|97.6|3.5|69.8|
|Cornwall|3549|19,760|96.8|5.3|73.8|
|Somerset|3452|21,317|95.4|8.4|76.5|
|Wiltshire|3255|22,645|90.3|9.9|81.3|
|Average||22,457|94.9|7.7|76.0|
|Smallest districts (by geograp|hical area)|||||
|City of London|3|192,005|53.8|49.6|75.0|
|Kensington and Chelsea|12|90,917|63.7|53.9|63.3|
|Islington|15|37,422|62.2|39.9|75.1|
|Hammersmith and Fulham|16|44,040|63.2|45.5|77.0|
|Hackney|19|29,655|53.1|39.7|81.2|
|Average||78,808|59.2|45.7|74.3|





We need two additional restrictions for a meaningful identification of latent components and their loadings. First, we assume that the shocks are orthogonal contemporaneously as well as at all leads and lags. Thus, Eðυ<sup>n</sup> t<sup>; υn</sup> t�s<sup>Þ ¼ Eðυr</sup> t<sup>; υr</sup> t�s<sup>Þ ¼ Eðυ</sup> i;t<sup>; υ</sup> i;t�s<sup>Þ ¼ 0. Second, we</sup> impose sign and scale restrictions. Here again, we follow the strategy established in the literature (Kose et al. 2003, 2008; Neely and Rapach, 2011).<sup>9</sup> 

Naturally, given the latent nature of factors, the usual regression apparatus is not available for estimating the model. Thus, we use the Bayesian procedure developed by Otrok and Whiteman (1998). We derive the complete posterior distribution of all the parameters, together with the latent factors, from a series of conditional distributions using a Markov chain Monte Carlo procedure.<sup>10</sup> To study the role of the three latent factors in house price movements, we also estimate the fraction of variance due to the national ðθ<sup>n</sup> i<sup>Þ,regionalðθr</sup> i<sup>Þ,andunit-specificðθs</sup> i<sup>Þ</sup> factors in the overall variation as follows: 





The estimates of θ<sup>n</sup> i<sup>, θr</sup> i<sup>, and θs</sup> i<sup>show the proportion of variance in</sup> the national, regional, and unit-specific factors, respectively, relative to the overall variance in house price movements for each state. 

Time-varying Bayesian VAR model. To examine the effects of housing sector-specific and economy-wide uncertainty shocks on the housing market, we adopt a time-varying Bayesian VAR model, which allows for time variation in both the VAR coefficients and residual covariance matrix. In particular, we employ the following model: 



where εt denotes residuals with distribution N �0; Σt�. yt is vector of n endogenous variables, which includes the HPU (alternatively; EPU or both EPU and HPU), real GDP growth and CPI-based inflation, national real housing returns common factor (f<sup>n</sup> t<sup>;Factor),andtheshadowrate(SSRWXorSSRK).</sup> 

Note that, the ordering of the RGDP, CPI, Factor, and SSRs are in line with standard monetary VAR models, whereby all the variables respond with a lag to monetary policy shocks, i.e., when monetary policy is identified using standard Cholesky decomposition (see Caraiani et al. (2021) for a detailed discussion of this literature). 

In addition, when we add the two metrics of uncertainty, they are ordered first, since uncertainty is recognized as a leading indicator of macroeconomic variables (Bloom, 2009; Christou et al. 2020; Jurado et al. 2015), and housing prices as well, following the related work of Nguyen Thanh et al. (2020). Note that when we use HPU and EPU together in the model, the latter, being a more general measure of uncertainty, is ordered first. With our focus primarily on the identification of uncertainty shocks, we also consider a case of reverse ordering as a robustness check, where the order is: SSRWX, Factor, CPI, RGDP, HPU, and EPU. 

The lag-length p is selected based on the Schwarz information criterion (SIC). Ai,t is a time-varying coefficient vector. We can formulate the model for each period in a more compact form: 



where X<sup>�</sup> t ¼ In � Xt where ⊗ represents the Kronecker product and In is n-dimensional identity matrix. If we denote Xt ¼ � y<sup>0</sup> t�1 y<sup>0</sup> t�2 ��� y<sup>0</sup> t�p � and B<sup>0</sup> t<sup>¼</sup> � A1;t A2;t ��� Ap;t � then the VAR coefficients βt ¼ vec �Bt� are assumed to follow driftless random walks: 



Following Dieppe et al. (2018) and Cogley and Sargent (2005), we also assumed that Σt can be decomposed as: 



where F is a n × n lower triangular matrix with ones its diagonal. Λt denotes the period-specific diagonal matrix with diag �Λt� ¼ ��s1 exp�λ1;t�;�s2 exp�λ2;t�; ��� ;�sn exp�λn;t��. While λ1,t, λ2,t, ⋯ticity,, λn�s,t1;are�s2; ���dynamic;�sn areprocessesknownyieldingscaling theterms.modelIn’sparticular,heteroscedas-we suppose that the λi,t terms follow AR process: 



where the shocksassumption that β v,i,ft<sup>−</sup> are i.i.d across periods<sup>1</sup> , and λ are independent, t = 1,Bayes ⋯ , TRules. Given thecan be 

6 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

written as: 





The priors for the parameters are set by closely following the specification of Dieppe et al. (2018). We assume that the prior for the VAR coefficients β has a normal distribution with πðβjΩÞ � Nð0; ΩÞ and is given by: πðβjΩÞ ¼ π�β1jΩ�QTt¼2<sup>π</sup> �<sup>β</sup> t<sup>jΩ; β</sup> t�1�. Hence, the conditional formulation can be formulated as: 



where Ω is a diagonal matrix with each term ωi pursuing an inverse-Gamma distribution with the following parameters: 





ð15Þ Furthermore, the conditional prior distribution of λ can be T defined as π�λijϕi� ¼ π�λi;1jϕi�Qt¼2<sup>π</sup> �<sup>λ</sup> i;t<sup>jλ</sup> i;t�1<sup>; ϕ</sup> i� which gives: 



Finally, the prior for each heteroscedasticity variance parameter ϕ is inverse gamma with shape α0 and δ0 which yields: 



Considering all prior distributions, Bayes rule, and the likelihood function, the joint posterior distribution is given by: 





Since the posterior does not admit analytical posteriors, we consider the Gibbs sampling algorithm with a total number of iterations of 2000 and a burn-in sample of 1000.<sup>11</sup> 

### Empirical results 

The national factor and its role in co-movement. Figure 1 plots the aggregate national-level factor. We find that this aggregate factor, common across all districts, closely captures the housing cycles in the UK. During the 1996–2002 period, the national factor rose steadily overall, with cyclical patterns lasting ~2–3 years. This trend reversed during the 2002–2007 period, followed by a sharp dip during the GFC and a recovery over the next 5 years. Since then, the national factor has hovered at sub-zero levels. This overall pattern of common components accurately reflects the housing cycles in the UK. Thus, the otherwise unobserved national factor in our model effectively captures the aggregate movements in UK house prices. 

Figure 1 also shows the national factor decreasing in magnitude during the 2002–2007 period, whereas, in the United States, house prices hit record highs during this time. There are a couple of explanations for this. Throughout the 2004–2007 period, the Bank of England (BoE) increased interest rates several times to curb inflationary pressures. This significantly impacted housing affordability and dampened house prices. The UK is also highly integrated with global markets, including the EU. From 2002 to 2007, economic uncertainty outside the UK potentially spilled over, negatively impacting investor confidence and the availability of credit in the UK. Furthermore, the early 2000s saw relatively rapid growth in housing construction. These demand- and supply-side forces often have a dampening effect on house prices. Since national factors capture the broad forces that drive comovement in house prices, it is intuitive to find national factors decreasing in magnitude during this period. It is not uncommon in the literature to find that housing market dynamics in major cities or metropolitan areas dominate aggregate-level movements (see, for example, Akimov et al. 2015, and Cohen et al. 2023). The UK is no exception. 

Between 2002 and 2006, a range of external factors contributed to a decline in the national factor. During this period, the US subprime mortgage market expanded rapidly, and by late 2005–2006, rising defaults began raising concerns about global financial stability. In response to domestic inflationary pressures, the US Federal Reserve raised interest rates from 1.0% to 5.25%, and the BoE followed suit with its own rate hikes. These actions, combined with tighter credit conditions, increased economic uncertainty and negatively impacted the UK housing market. Geopolitical instability from the Iraq War and oil price shocks further exacerbated inflationary pressures, while a weakening US dollar made UK property less attractive to foreign investors. Additionally, global financial market volatility in 2005–2006 heightened economic uncertainty, undermining investor confidence in property as a safe asset class. Together, these factors explain the downward trend in the national factor during this period. 

The DFM modeling strategy chosen in the paper, however, is equipped to tackle this aspect of the UK’s housing market. We do not directly use the national-level index but instead rely on much more granular geographic data. The model imposes no a priori restriction on what drives house prices-perhaps economic activity and housing wealth in London and the southern regions, but perhaps not. Instead, the contemporaneous orthogonalization of shocks ensures that one can distinctly decompose the movement in house prices into national- and regional-level latent factors. While the national factor may include the “big cities” effect that you highlight, the model distinctly identifies regional and 

7 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 1 The UK national factor. The plot presents the aggregate national UK factor obtained from the dynamic factor model. 

district-specific factors after controlling for national-level forces, including the big city effects. 

Table 3 presents the results of the variance decomposition obtained from the DFM. We find that the national factor, such as monetary policy and economic growth, explains a significant portion of the variation in house prices across all districts in the UK. The national factor explains 80% or more of the variation in house prices in South Teesside in the Northeast, Manchester in the Northwest, Kingston, Sheffield in Yorkshire and the Humber, North Nottinghamshire in the East Midlands, nearly half of the West Midlands, and London, and nearly the whole of the East, South East, and South-West regions. In contrast, regional forces play a sizable role (25% to 55%) in the housing markets of the North East, North West, Yorkshire, and the Humber and Wales regions. Some good examples of specific housing markets include Durham (47%), Hartlepool and Stockton (53%), West Cumbria (48%), the Barnsley area (46%), Blackburn (55%), and Central Valley (47%). District-specific factors play a minor role in the UK, with the exception of districts such as Shropshire, Breckland South Norfolk, and Wandsworth. The district-specific factor explains over 30% of the variation in these districts. These results suggest that the housing market in the UK is well-integrated nationally, for the most part, and regionally in selected areas. 

There are several demand- and supply-side reasons that explain the variation in house prices. For example, income is one of the main drivers of housing demand (Kishor and Marfatia, 2017, 2018). Regional income and economic disparities (McCann, 2019) potentially drive the diverse behavior of house prices at the district level. Housing demand also has a regional dimension. For instance, the commuter belt orbiting London leads to comovement in house prices around that region. The regional pull of major cities explains the dominant role of regional factors in variations in house prices. Furthermore, supply constraints, such as housing regulations, also impact how property prices react to adjustments in credit markets and macroeconomic conditions. For example, Favara and Imbs (2015) find that house prices in the US are well-explained by credit expansion induced by deregulation. Zooming in further, district-level factors such as transportation links, preferred school catchments, local amenities, and green spaces potentially explain the significant role of district-specific factors in areas like Shropshire, Breckland, South Norfolk, and Wandsworth. 

The results of the DFM are significant because they extract the common hidden movements in house prices across districts in a more realistic and natural setting. This leads to a much cleaner and more accurate identification of national-level forces that drive house prices. The aggregate national price trend is limited by its 

inability to recognize the diversity in house price growth across districts, as it averages out widespread housing market disparities. 

Furthermore, it is intuitive to observe the dominance of housing market uncertainty over other forms of uncertainty in driving the national-level factor. However, our approach precisely traces the impact of such shocks on the common movement in house prices at each point in time. This is highly relevant for real estate consumers and investors, as it provides insight into the timing of housing investments, which is critical for making informed investment decisions. 

Note that one can argue that geographical connectedness may or may not be similar to economic connectedness. That is, housing markets can be segmented based on economic commonalities rather than geographical regions. However, any classification scheme is bound to involve subjective choices. For example, segmenting housing markets on an economic basis would also require the subjective selection of economic variables. Furthermore, we use a geographical decomposition scheme to remain consistent with the housing market literature. Several studies find that geographical proximity dominates economic ties in driving house price movements (Marfatia, 2021; Pomogajko and Voigtländer, 2012; Sheng et al. 2021). Consistent with our finding of the significant role of the national factor, Lin and Robberts (2023) also find that all regions in the UK converge to one club during the inflation-targeting regime until the GFC. 

The effects of uncertainty shocks on the national factor. The need to understand the impact of uncertainty shocks on housing markets is highlighted by several potential rationales. Uncertainty, whether economic or otherwise, affects both the demand and supply sides of the housing market. Consumer confidence and investor sentiment are pivotal in housing market dynamics. Concerns about future economic growth, job security, geopolitical stability, or adverse global shocks erode consumer confidence and negatively affect investor sentiment. Both uncertain consumers and investors delay making large financial commitments or investments, thereby dampening house prices. Uncertainty also influences the availability and cost of credit due to cautious lending practices. Since housing heavily relies on credit financing, such cautious lending practices depress house prices. 

On the supply side, heightened uncertainty often prompts developers to delay or cancel new construction projects and adjust completion times for existing projects based on their perceptions of market conditions. Economic and housing-related uncertainties can also lead to labor shortages and supply chain disruptions, thereby increasing construction costs. Consequently, 

8 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

|Table 3 Variance dec|ompos<br>Fact1|ition.<br>Fact2|Fact3||Fact1|Fact2|Fact3||Fact1|Fact2|Fact3|
|---|---|---|---|---|---|---|---|---|---|---|---|
|NthEt||||WtMidld||||SthEt||||
|or as<br>Hartlepool and Stockton|0.40|0.53|0.07|es ans<br>Herefordshire|0.89|0.08|0.03|ou as<br>Berkshire|0.88|0.10|0.02|
|S Teesside<br>Darlington|0.88<br>0.55|0.06<br>0.39|0.06<br>0.05|Worcestershire<br>Warwickshire|0.93<br>0.95|0.05<br>0.02|0.02<br>0.02|Milton Keynes<br>Buckinghamshire|0.93<br>0.84|0.05<br>0.12|0.02<br>0.04|
|Durham|050|047|004|Telford&Wrekin|084|011|005|Oxfordshire|092|004|004|
|Numberland|.<br>0.61|.<br>0.35|.<br>0.04|<br>Shropshire|.<br>0.36|.<br>0.27|.<br>0.37|Brighton & Hove|.<br>0.86|.<br>0.07|.<br>0.07|
|Tyneside|0.44|0.12|0.44|Stoke-on-Trent|0.95|0.00|0.05|E Sussex|0.98|0.00|0.02|
|Sunderland|0.69|0.28|0.03|Staffordshire|0.79|0.18|0.02|W Surrey|0.97|0.01|0.03|
|North West<br>WCbi|043|048|009|Birmingham<br>Slihll|0.86<br>093|0.10<br>002|0.03<br>005|E Surrey<br>WSSW|0.86<br>097|0.12<br>002|0.01<br>001|
|umra<br>E Cumbria|.<br>0.59|.<br>0.37|.<br>0.05|ou<br>Coventry|.<br>0.88|.<br>0.07|.<br>0.05|ussex ( )<br>W Sussex (N E)|.<br>0.89|.<br>0.02|.<br>0.09|
|Manchester<br>|0.91|0.01|0.08|Dudley<br>|0.76|0.20|0.05|Portsmouth<br>|0.98|0.00|0.02|
|Manchester SW|0.71|0.14|0.15|Sandwell|0.68|0.26|0.06|Sampton|0.97|0.00|0.03|
|Manchester SE<br>Manchester NW|0.78<br>0.58|0.16<br>0.39|0.07<br>0.04|Walsall<br>Wolverhampton|0.73<br>0.61|0.20<br>0.30|0.07<br>0.09|Isle of Wight<br>S Hampshire|0.96<br>0.82|0.00<br>0.10|0.04<br>0.08|
|Manchester NE|0.56|0.39|0.04|East||||Central Hampshire|0.95|0.03|0.02|
|Blackburn|0.36|0.55|0.10|Peterborough|0.71|0.13|0.16|N. Hampshire|0.82|0.16|0.02|
|Blackpool|0.85|0.07|0.08|Cambridgeshire|0.97|0.00|0.03|Medway|0.76|0.17|0.08|
|Lancaster & Wyre<br>Mid Lancashire|0.57<br>0.64|0.37<br>0.33|0.07<br>0.03|Suffolk<br>Norwich, E Norfolk|0.98<br>0.90|0.00<br>0.03|0.02<br>0.07|Kent Thames Gateway<br>E Kent|0.95<br>0.96|0.00<br>0.01|0.05<br>0.03|
|E. Lancashire|0.43|0.47|0.11|N & W Norfolk|0.72|0.15|0.13|Mid Kent|0.95|0.00|0.05|
|Chorley and W<br>Lhi|0.58|0.39|0.03|Breckland and S Norfolk|0.43|0.24|0.33|W Kent|0.98|0.00|0.02|
|ancasre<br>Warrington|0.52|0.42|0.06|Luton|0.82|0.10|0.08|South West||||
|CheshireE|087|010|003|Hertfordshire|091|005|005|Bristol|093|001|006|
|<br>Cheshire W and<br>Chester|.<br>0.81|.<br>0.16|.<br>0.03|Bedford|.<br>0.96|.<br>0.01|.<br>0.03|Bath, Somerset|.<br>0.98|.<br>0.00|.<br>0.02|
|E. Merseyside|0.67|0.27|0.05|Central Bedfordshire|0.72|0.12|0.15|Gloucestershire|0.62|0.22|0.16|
|Liverpool|0.71|0.12|0.17|Send-on-Sea|0.95|0.00|0.05|Swindon|0.86|0.07|0.08|
|Sefton|0.49|0.44|0.07|Thurrock|0.92|0.04|0.04|Wiltshire|0.95|0.02|0.03|
|Wirral<br>Yorkshireandthe|0.68|0.28|0.04|Essex Haven Gateway<br>WEssex|0.98<br>094|0.00<br>002|0.02<br>004|Bournemouth & Poole<br>Dorset|0.96<br>096|0.00<br>000|0.04<br>004|
|<br>Humber||||.|.|.|.||.|.|.|
|KingstonuponHull|087|008|005|HeartofEssex|097|001|002|Somerset|094|004|002|
|<br>E. Riding of Yorkshire|.<br>0.63|.<br>0.33|.<br>0.04|<br>Essex Thames Gateway|.<br>0.94|.<br>0.00|.<br>0.06|Cornwall and Isles of<br>Scill|.<br>0.92|.<br>0.05|.<br>0.03|
|N. & NE Lincolnshire|0.53|0.42|0.05|London||||y<br>Plymouth|0.89|0.05|0.06|
|York|0.74|0.19|0.07|Camden and City of<br>d|0.61|0.34|0.05|Torbay|0.78|0.15|0.06|
|N Yorkshire|0.80|0.17|0.02|Lonon<br>Wminster|0.93|0.01|0.06|Devon|0.77|0.09|0.14|
|Barnsley, Doncaster|0.51|0.46|0.02|Kensington, Chelsea|0.55|0.37|0.07|Wales||||
|Sheffeld|0.90|0.01|0.08|Wandsworth|0.46|0.21|0.33|Isle of Anglesey|0.90|0.05|0.05|
|Bradford|054|039|006|HaringeyandIslington|096|000|004|Gwynedd|065|030|006|
|Leeds|.<br>0.51|.<br>0.39|.<br>0.10|<br>Lewisham and Swark|.<br>0.54|.<br>0.21|.<br>0.25|Conwy & Denbighshire|.<br>0.75|.<br>0.14|.<br>0.10|
|Calderdale&Kirklees|059|039|002|Lambeth|051|039|009|SWWales|051|040|009|
|<br>Wakefeld|.<br>0.80|.<br>0.14|.<br>0.05|Bexley and Greenwich|.<br>0.88|.<br>0.06|.<br>0.05|<br>Central Valleys|.<br>0.50|.<br>0.44|.<br>0.06|
|East Midlands<br>||||Barking, Dagenham<br>|0.87<br>|0.00<br>|0.13<br>|Gwent Valleys<br>|0.90<br>|0.06<br>|0.04<br>|
|Derby|0.80|0.18|0.03|Redbridge, Waltham<br>Forest|0.89|0.06|0.04|Bridgend, Neath Port<br>Talbot|0.47|0.46|0.07|
|EDbhi|||2|Efld||14|1|S||2|2|
|erysre<br>S & W Derbyshire|0.68<br>0.80|0.30<br>0.19|0.0<br>0.01|ne<br>Bromley|0.76<br>0.82|0.<br>0.15|0.0<br>0.03|wansea<br>Monmouthshire,<br>|0.75<br>0.54|0.3<br>0.42|0.0<br>0.04|
|||||||||Newport<br>||||
|Nottingham|0.65|0.30|0.06|Croydon|0.84|0.11|0.05|Cardiff, Vale of<br>Gl|0.86|0.10|0.04|
|N. Nottinghamshire|0.85|0.10|0.05|Merton, Kingston|0.96|0.01|0.03|amorgan<br>Flintshire, Wrexham|0.71|0.25|0.03|
|S. Nottinghamshire<br>|0.57<br>|0.32<br>|0.11<br>|Barnet<br>|0.84<br>|0.09<br>|0.06<br>|Powys|0.66|0.30|0.04|
|Leicester<br>Leicestershire and<br>|0.90<br>0.64|0.09<br>0.22|0.01<br>0.14|Brent<br>Ealing|0.82<br>0.34|0.14<br>0.42|0.04<br>0.24|||||
|Rutland<br>W. Namptonshire|0.78|0.14|0.08|Harrow, Hillingdon|0.75|0.18|0.08|||||
|N. Namptonshire<br>|0.97|0.00|0.03|Hounslow and Richmond|0.79|0.20|0.01|||||
|Lincolnshire<br>This table reports the variance d|0.84<br>ecomposit|0.16<br>ion of real|0.01<br> house pric|es into the national (Fact1), regional|(Fact2),|and distric|t-specifc id|iosyncratic factors (Fact3).||||



9 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 2 Impulse responses to house price uncertainty shock. This figure shows the impulse responses to one unit shock to the house price uncertainty index. The dashed lines are 68% probability bands. 

uncertainty can constrain housing supply by undermining developer confidence, altering project completion schedules, escalating construction costs, and introducing potential regulatory hurdles. 

On the policy front, a precise estimate of the impact of uncertainty shocks on national-level movements in house prices can provide crucial guidance to policymakers interested in safeguarding the real estate market against risks and uncertainties. Our findings on the dominance of housing-related uncertainty over other forms of uncertainty can also aid in designing appropriate policy responses based on the nature of the uncertainty shocks-housing-related uncertainty versus economic uncertainty. 

Time-invariant impulse responses. Figure 2 presents the estimated impulse responses due to the HPU shocks to the four endogenous variables yt = [HPU, GDP, CPI, Factor, SSRWX] for the period of 1996:Q2–2019:Q2. We call this specification our baseline model. The initial reaction of the national factor to HPU shock is 

negative, and the response becomes statistically significant after the third quarter. We find the response drops to its lowest value around six quarters and then returns to its initial level after fifteen quarters. 

The negative reaction of the national factor to an HPU shock can be attributed to both a decrease in housing demand and a wait-and-see approach by developers and sellers amidst heightened uncertainty. This cautious behavior can lead to a temporary reduction in housing market transactions, which is reflected in the negative response of the national factor. While fewer transactions might suggest a potential for price increases in the long run due to reduced supply, the immediate effect of heightened uncertainty is a decline in market activity. This decline, combined with a simultaneous decrease in demand due to increased precautionary savings and tighter credit conditions, results in an overall negative impact on the housing market in the short term (Bernanke, 1983; Iacoviello, 2005). Our findings also align with the theoretical predictions of Berkovec and Goodman (1996), who show that sluggish price adjustment in response to 

10 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 3 Impulse responses to economic policy uncertainty shock. This figure shows the impulse responses to one unit shock to the economic policy uncertainty index. The dashed lines are 68% probability bands. 

demand shocks, due to imperfect information among market participants, further amplifies the negative impact of uncertainty shocks on housing markets. 

Figure 2 also suggests that the reaction of GDP growth to house price uncertainty shocks is negative and statistically significant for about four quarters after the shock. This is intuitive. On the demand side, increased house price uncertainty might cause households to postpone their home-buying decisions. On the supply side, increased uncertainty causes real estate firms to delay house-building and investment activities, which contribute directly to GDP (Balcilar et al. 2021; Choudhry, 2020). Given that central banks closely monitor developments in the housing market due to the risk of tightening credit conditions and widening mortgage spreads, one potential response of central banks to uncertainty shocks is to cut interest rates. This explains the negative reaction of SSRWX in the plot. 

In Fig. 3, we present the impulse responses from the baseline model, substituting HPU with EPU. While the national factor’s response to an EPU shock is negative, the effect is less pronounced compared to an HPU shock. Additionally, the 

national factor reacts more quickly to an EPU shock, but the subsequent decline is short-lived, dissipating within ten quarters. Given that EPU has a broader impact, directly influencing economic decisions made by households, firms, and governments (see Bloom, 2009; Cepni et al. 2020; Kang et al. 2014), central banks may implement quicker and more aggressive credit easing policies. These could include measures such as lowering policy rates, purchasing significant volumes of corporate bonds, and expanding funding for lending schemes to mitigate the adverse effects of uncertainty on the economic outlook. Consequently, the negative reaction of SSRWX to EPU shocks is more pronounced than to HPU shocks. Furthermore, as shown in Fig. 3, the response of GDP growth to an EPU shock is also negative, mirroring the pattern observed with HPU shocks. 

We extend our baseline specification by adding EPU to the model with the following ordering: yt = [EPU, HPU, GDP, CPI, Factor, SSRWX]. We refer to this specification as our extended model. Columns 1–2 of Fig. 4 reveal that the response of the national factor to an EPU shock becomes statistically 

11 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 4 Impulse responses to uncertainty shocks: HPU vs. EPU–extended model. This figure shows the impulse responses to uncertainty shocks. The dashed lines are 68% probability bands. 

insignificant, while the negative impact of an HPU shock on housing returns remains statistically significant when EPU is included in the model. This result suggests that uncertainty about house prices is the primary driver of the national factor. The reason might be that house price uncertainty shocks directly affect the housing market through both housing 

demand and real-options channels, thereby influencing the real option values of residential investment projects (Clapp et al. 2013). Similarly, an uncertainty shock to house prices increases the risks associated with mortgage debt and homeownership, reducing housing prices due to a decrease in housing market activity (Noh, 2020). 

12 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 5 Time-varying impulse responses to house price uncertainty shock. This figure shows the evolution of impulse responses to house price uncertainty shock variable along 16 quarters horizons and the time period from 1996:Q2 to 2019:Q2. The X axis of each panel represents the time periods, the Y axis is the horizon in quarters, while the Z axis is the impulse responses. 

Overall, our results highlight that using a housing sectorspecific uncertainty measure is crucial for understanding house price dynamics. This underscores the importance of incorporating housing-specific information into the construction of uncertainty measures. Furthermore, our findings validate those of Salisu et al. (2021), who show that using HPU to predict housing returns results in better predictive performance than models with EPU. These results are also consistent with findings from the US housing market. For instance, Kallberg et al. (2014) find that the price co-movement of U.S. residential real estate markets increased significantly, particularly in the late 1990s, and that this increase is largely attributable to underlying systematic real and financial factors. Additionally, Gupta et al. (2021) find 

that macroeconomic uncertainty accurately forecasts the comovement of house prices in the US. 

Time-varying impact of uncertainty shocks on the UK housing market. Figure 5 presents the median impulse responses to housing uncertainty shocks over 16 quarters during the 1996:Q2–2019:Q2 period. The x axis of each sub-graph shows the periods, the y axis represents the horizon in quarters, and the z axis denotes the period-specific impulse responses. We find that the dynamic response of the model, i.e., the impulse response functions, has changed over the analyzed period. After a house price uncertainty shock, the decline in the national factor is more persistent at the beginning of the sample, while the national factor 

13 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 6 Time-varying impulse responses to economic policy uncertainty shock. This figure shows the evolution of impulse responses to economic policy uncertainty shock variable along 16 quarters horizons and the time period from 1998:Q1 to 2020:Q3. The X axis of each panel represents the time periods, the Y axis is the horizon in quarters, and the Z axis is the impulse responses. 

recovers faster after 2015. Although HPU intensified following the UK’s decision to leave the EU (23 June 2016), the BoE quickly implemented measures to mitigate the amplification of the uncertainty effect via the housing market by adopting a credit easing policy at its first monetary policy meeting after Brexit. Accordingly, house price uncertainty shocks have become less persistent over time due to easing financial conditions facilitated by unconventional monetary policies. Similarly, while the initial reaction of the national factor to a one-unit shock in house price uncertainty is negative and reaches its lowest value in the fifth quarter, this occurs faster than in previous periods, and the national factor recovers more quickly to its initial level after 2016. 

Figure 6 shows the impulse responses capturing the timevarying effects of EPU shocks on the national factor and macroeconomic variables during the 1998:Q1–2020:Q3 period. 

The impulse responses to uncertainty shocks exhibit time variation, particularly during recession periods. The reaction of the national factor to EPU shocks is negative and more stable compared to its response to HPU shocks. On the other hand, Fig. 7 presents the reactions of the national factor using the extended model. Column 1 of Fig. 7 shows the impulse responses to an EPU shock, while Column 2 illustrates the impulse responses to an HPU shock. 

Figure 7 provides several insights. First, the estimated responses of the national factor to uncertainty shocks are always negative, but the effect is more pronounced in the case of HPU shocks, especially during the GFC and the Brexit referendum. Second, the reaction of the national factor to HPU shocks displays a more persistent response over the sample period than that of EPU shocks. Thus, households react more strongly to 

14 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 7 Time-varying impulse responses to uncertainty shocks: HPU vs. EPU - combined model. This figure shows the evolution of impulse responses to uncertainty shocks variable along 16 quarters horizons and the time period from 1998:Q1 to 2019:Q2. The X axis of each panel represents the time periods, the Y axis is the horizon in quarters, while the Z axis is the impulse responses. 

housing sector-specific uncertainty, perhaps due to the irreversibility of housing investment decisions and the inelastic nature of housing supply caused by geographical constraints (see, for example, Saiz (2010) and related studies). Further, an increase in 

overall economic policy uncertainty might cause higher demand for houses if the demand for other financial assets is more sensitive to uncertainty (El Montasser et al. 2016), thereby mitigating the negative effect of EPU shocks. Banks might also 

15 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

|SSRWX|0.000<br>0.002<br>0.004<br>0.008<br>0.017<br>0.027<br>0.037<br>0.044<br>0.046<br>0.047<br>0.047<br>0.047<br>0.049<br>0.049<br>0.050<br>0.050||
|---|---|---|
|Factor|0.909<br>0.876<br>0.837<br>0.792<br>0.749<br>0.705<br>0.670<br>0.651<br>0.647<br>0.644<br>0.642<br>0.638<br>0.637<br>0.634<br>0.632<br>0.629||
|CPI|0.014<br>0.019<br>0.036<br>0.058<br>0.078<br>0.090<br>0.096<br>0.095<br>0.092<br>0.091<br>0.089<br>0.090<br>0.093<br>0.093<br>0.092<br>0.093||
|GDP|0.014<br>0.034<br>0.044<br>0.044<br>0.044<br>0.042<br>0.043<br>0.044<br>0.045<br>0.044<br>0.044<br>0.043<br>0.043<br>0.043<br>0.044<br>0.044||
|d model<br>HPU|0.014<br>0.012<br>0.015<br>0.022<br>0.032<br>0.045<br>0.060<br>0.070<br>0.074<br>0.076<br>0.077<br>0.077<br>0.078<br>0.079<br>0.080<br>0.080||
|Extende<br>EPU|0.010<br>0.013<br>0.015<br>0.018<br>0.020<br>0.023<br>0.027<br>0.031<br>0.033<br>0.034<br>0.035<br>0.036<br>0.036<br>0.036<br>0.036<br>0.037||
|SSRWX|0.000<br>0.002<br>0.004<br>0.007<br>0.015<br>0.025<br>0.034<br>0.043<br>0.047<br>0.047<br>0.048<br>0.048<br>0.049<br>0.050<br>0.051<br>0.051||
|Factor|0.872<br>0.811<br>0.770<br>0.738<br>0.702<br>0.669<br>0.647<br>0.633<br>0.627<br>0.628<br>0.628<br>0.626<br>0.626<br>0.621<br>0.619<br>0.617|are in percent.|
|EPU<br>CPI|0.047<br>0.057<br>0.082<br>0.109<br>0.132<br>0.147<br>0.156<br>0.156<br>0.153<br>0.150<br>0.149<br>0.152<br>0.153<br>0.154<br>0.155<br>0.155|variable. Entries|
|model with<br>GDP|0.028<br>0.068<br>0.072<br>0.066<br>0.066<br>0.067<br>0.072<br>0.074<br>0.075<br>0.076<br>0.077<br>0.076<br>0.075<br>0.076<br>0.078<br>0.078|to each of the|
|Baseline <br>EPU|0.016<br>0.024<br>0.027<br>0.028<br>0.029<br>0.030<br>0.032<br>0.033<br>0.034<br>0.034<br>0.034<br>0.035<br>0.034<br>0.034<br>0.034<br>0.034|by the shocks|
|SSRWX|0.000<br>0.001<br>0.003<br>0.009<br>0.021<br>0.035<br>0.049<br>0.055<br>0.058<br>0.058<br>0.058<br>0.058<br>0.059<br>0.061<br>0.062<br>0.063|s horizon explained|
|Factor|0.945<br>0.905<br>0.851<br>0.795<br>0.739<br>0.689<br>0.652<br>0.635<br>0.633<br>0.635<br>0.634<br>0.631<br>0.627<br>0.625<br>0.625<br>0.623|r at 16 quarter|
|CPI|0.017<br>0.025<br>0.046<br>0.070<br>0.091<br>0.107<br>0.113<br>0.111<br>0.108<br>0.104<br>0.104<br>0.105<br>0.105<br>0.106<br>0.106<br>0.106|of forecast erro|
|PU<br>GDP|0.008<br>0.026<br>0.039<br>0.043<br>0.042<br>0.043<br>0.043<br>0.043<br>0.042<br>0.043<br>0.043<br>0.043<br>0.043<br>0.043<br>0.043<br>0.044|n of the variance|
|Baseline model with H<br>Horizon<br>HPU|1<br>0.009<br>2<br>0.012<br>3<br>0.019<br>4<br>0.033<br>5<br>0.053<br>6<br>0.072<br>7<br>0.090<br>8<br>0.102<br>9<br>0.106<br>10<br>0.106<br>11<br>0.105<br>12<br>0.107<br>13<br>0.106<br>14<br>0.106<br>15<br>0.107<br>16<br>0.108|This table reports the fractio|



apply tighter credit scoring criteria in processing mortgage loan applications, particularly among high loan-to-value borrowers, due to elevated house price uncertainty, thereby reducing housing demand.<sup>12</sup> 

Variance decomposition. This section examines the changes in the historical and forecast error variance decompositions of the national factor due to uncertainty shocks. Table 4 illustrates the share of variance contributions to the national factor. The first column lists different time horizons, while the other columns show the fraction of the forecast error variance of the national factor attributable to the corresponding shock under different model specifications. The variance decomposition analysis reveals that HPU shocks play a significant role in explaining the variance in the national factor. In the baseline model using the house price uncertainty index, HPU shocks account for a non-negligible portion of the variability in the national factor, explaining approximately 10% of the forecast error variance.<sup>13</sup> In contrast, EPU shocks have lower importance for the variability of the national factor, with their share relatively low (~3%) in both the baseline and expanded models at a 16-quarter forecast horizon. Overall, the results of the variance decomposition analysis confirm that HPU is relatively more important than EPU in explaining the variation in the national factor. 

In Fig. 8, we investigate how the contributions of each uncertainty shock to the historical dynamics of the national factor change over time. Specifically, we decompose the value of each variable into its different components for every period in the sample, with each component attributed to one structural shock of the model.<sup>14</sup> In doing so, we identify the historical contribution of each shock to the national factor. Note that the impact of a shock on a variable corresponds to the accumulated effects of current and past shocks when interpreting the historical decomposition. An examination of all the subgraphs in Fig. 8 highlights the central role of uncertainty shocks on the national factor, especially during periods of financial stress. Interestingly, HPU shocks explain a non-negligible fraction of the national factor between 2009 and 2010, as well as during the Eurozone sovereign debt crisis in 2012. In contrast, the contribution of HPU shocks is positive at the beginning of the sample, coinciding with the house price boom period in the early 2000s. 

Our findings for the UK are comparable to those of other EU countries pre-Brexit. While this study investigates the UK market, there are several lessons for the EU as well as other regionally connected economies around the world. Housing markets in Euro-area countries, like the UK, are influenced by both national and regional factors. In the case of the EU, common union factors, such as monetary policy, have led to significant comovement of housing prices at the EU level. At the same time, there is a significant regional divide in the EU, which affects house prices at the regional level. Furthermore, country-specific diversity in policy actions, political events, or economic crises triggers uncertainty shocks that affect the EU’s housing markets. 

Our results based on the UK suggest that housing markets in the EU likely exhibit significant co-movement due to national and regional factors, with some countries experiencing the dominance of country-specific factors in house price movements. Additionally, we find pronounced effects of HPU shocks in the UK, particularly during the GFC and the Brexit referendum, with HPU shocks dominating EPU shocks. Among EU nations, policies designed to stabilize housing markets should pay particular attention to uncertainty related to housing markets relative to broader economic uncertainty shocks. 

16 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 8 Historical decomposition of the national factor. The black solid line is the actual national factor. The colored stacked bars represent the (median of the posterior) contribution of the identified structural shocks to the national factor. 

The results of this study provide several key insights into housing markets globally. Housing market synchronization has been increasing, with uncertainty shocks significantly impacting house prices in the G7 countries (Haritia et al., 2012). However, there remains considerable heterogeneity in the degree of synchronization across different countries and cities (Katagiri, 2018). EU housing markets, in particular, display distinct characteristics. While the shared influence of the European Union-such as common monetary policies and international shocks-can lead to some common trends in housing markets among member states, country-specific factors remain crucial and cannot be ignored. 

In Germany, for example, the federal government plays a key role in regulating the housing market through building laws, such as the German Building Code, and by overseeing urban planning and development activities. The individual states are responsible for designing development plans (state spatial planning programs) and implementing building regulations. Meanwhile, municipalities influence urban development within their jurisdictions through their own land-use and development plans. This hierarchical yet flexible regulatory framework makes the DFM 

used in our paper particularly well-suited for understanding the German housing market. Brausewetter et al. (2024) employ a different approach and find significant and growing regional disparities in housing prices across German districts, with regional fundamentals explaining up to 67% of between-region and 77% to 87% of within-region variations in price growth. In contrast, Klarl (2018) finds that the Dutch housing market is highly localized, despite the existence of a common housing cycle that drives house price co-movement across all regions. 

While there are studies examining common and idiosyncratic business cycle movements in the EU (Florian et al., 2020), research on housing markets remains relatively scarce. Our work fills this gap in the European context, offering new insights into housing market dynamics in countries like France and Germany. It also provides a solid foundation for future research on EU housing markets. 

### Robustness check 

Given that a range of unconventional monetary policies (such as large-scale asset purchases, a maturity extension program, and 

17 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 9 An alternative measure of shadow policy rate–robustness check. See notes in Fig. 4. 

forward guidance to manage expectations of a prolonged period of low policy rates) are pursued during the ZLB condition, one can argue the need to use a uniform and coherent measure of the monetary policy stance. Thus, we use the SSR, which measures 

the nominal interest rate that would prevail in the absence of its effective lower bound. As a matter of robustness analysis, we also use the SSR developed by Krippner (2013, 2015, 2020), which is considered to be an improvement over those obtained by Wu and 

18 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 



Fig. 10 Reverse ordering of variables–robustness check. See notes in Fig. 4. 

Xia (2016), as discussed in detail by Krippner (2020).<sup>15</sup> In this regard, we estimate the extended model by replacing SSWRK with SSRK. The results presented in Fig. 9 of the appendix show that the estimated responses of national factors to house price uncertainty shocks are always negative and statistically 

significant. The other impulse responses are qualitatively similar to our main findings. 

Furthermore, to ensure that the ordering imposed in the extended model does not affect our results, we estimate the extended model using a reverse ordering of endogenous variables 

19 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

within the TVP-VAR model. In this arrangement, the variable EPU is considered the most endogenous in the system. The impulse response functions are presented in Fig. 10 of the appendix. Consistent with our baseline results, the response of the national factor to a shock in EPU is insignificant. The remaining results also align with our previous findings, indicating that our results are not sensitive to the ordering of the endogenous variables. 

### Conclusion 

Using a DFM, we disentangle the co-movement in house prices in the smallest geographic units into unobserved factors: the national factor, which affects all markets; the regional factor, which drives house prices in districts within a particular region; and the unique district-specific factor. This framework allows us to investigate how housing market-related uncertainty shocks affect synchronous movements in regional housing markets. We use a Bayesian TVP-VAR model to estimate the dynamic impact of aggregate macroeconomic and uncertainty shocks on the common factor. 

Our results show that the national factor accurately tracks the overall housing market cycles in the UK. Furthermore, the national factor explains nearly all the variation in districts in the East, South-East, and South-West regions. We find a sizable role for regional factors in the housing markets of the North East, North West, Yorkshire and the Humber, and Wales. Additionally, the Bayesian TVP-VAR model results indicate that the impulse responses to uncertainty shocks exhibit time variation, particularly during recession periods. Specifically, the estimated responses of the national factor to uncertainty shocks are always negative, but the effect is more pronounced in the case of HPU shocks, especially during the GFC and the Brexit referendum. 

The housing market acts as a key barometer of the economy and an important amplifier of shocks to the broader economy, intensifying the amplitude of business and credit cycles. The GFC demonstrated the impact and importance of developments in the housing market. Its overheating and the resulting downturn in the US were catalysts for a financial crisis that spread globally through linkages in the financial system. Thus, a deeper understanding of housing market dynamics could help institutions, such as central banks, monitor the market and take timely and appropriate measures. For instance, the BoE could exert greater control over banks’ mortgage underwriting standards for newly written mortgages and recommend appropriate interest rate stress tests for mortgage affordability assessments. Such measures could increase the resilience of banks and households to potential declines in housing returns during periods of heightened uncertainty. 

While policy responses, such as credit easing by the Bank of England, can mitigate the immediate negative impact of uncertainty shocks on the housing market, it is important to acknowledge that such interventions may not always be valueneutral. A growing body of literature highlights the potential drawbacks of policy responses. For instance, prolonged low interest rates can fuel asset bubbles (Diamond and Rajan, 2012) and exacerbate income inequality (Rajan, 2011). Furthermore, unconventional monetary policies like quantitative easing may lead to unintended consequences, such as distortions in financial markets and inflationary pressures (Baumeister and Benati, 2010). Therefore, while acknowledging the potential positive short-term effects of policy interventions on the housing market, future research should carefully examine their long-term implications and potential trade-offs. 

Considering that the regional effects of Brexit are less clearcut than those on the overall housing market, it would be 

interesting to analyze the impact of uncertainty shocks on regional housing factors. For instance, the provision of international financial services is concentrated in London, creating greater sensitivity to economic policy uncertainty. Conversely, localized demand effects can aggregate to influence the overall housing market. Put differently, friction in one part of the housing market such as London, can affect other regions as housing market chains are disrupted. Therefore, our analysis highlights potential avenues for future research on the housing market. 

The findings of this paper can also serve as an impetus for future investigations into the underlying mechanisms driving the results, particularly the effects of uncertainty shocks on housing markets. Additionally, we added a discussion on the economic relevance of our findings, including the translation of results into real economic outcomes at both the micro and macro levels, as well as their policy implications. 

### Data availability 

The datasets generated and analyzed during the current study are included in this published article and its supplementary data files. 

Received: 7 February 2024; Accepted: 27 January 2025; 



### Notes 

- 1 In addition to linking housing market dynamics with macroeconomic variables, several studies also associate housing market fluctuations with unconventional factors such as electoral performance (Cifci et al. 2023) and initial public offerings (Nguyen et al. 2022). This underscores the role of macroeconomic shocks in driving movements in housing markets. 

- 2 However, this real estate uncertainty index data runs only until 2017 and is no longer updated. 

- 3 See: https://uk.housing-observatory.com/dashboard.html. Ideally, we would want to include Scotland and Northern in our analysis. However, district-level data for Scotland and Northern Ireland is unavailable. 

- 4 The data is available for download from the website of Professor Jing Cynthia Wu at: https://sites.google.com/view/jingcynthiawu/shadow-rates?authuser=0. 

- 5 The SSR is based on models of the term structure, which essentially removes the effect that the option to invest in physical currency (at an interest rate of zero) has on yield curves, resulting in a hypothetical “shadow yield curve" that would exist if the physical currency were not available. The process allows one to answer the question: “What policy rate would generate the observed yield curve if the policy rate could be taken negative?" The “shadow policy rate" generated in this manner, therefore, provides a measure of the monetary policy stance after the actual policy rate reaches zero. The main advantage of the SSRWX is that it is not constrained by the ZLB and thus allows us to combine the data from the ZLB period with that of the non-ZLB era, using it as the common metric of monetary policy stance across both conventional and unconventional monetary policy episodes. 

- 6 Uncertainty is latent by nature and hence, measuring it is a challenge. Besides alternative metrics of uncertainty associated with financial markets (such as the implied-volatility indices (popularly called the VIX), realized volatility, idiosyncratic volatility of equity returns, and corporate spreads), there are primarily three broad approaches to quantifying uncertainty (Gupta et al. 2018). First, a news-based measure where the idea is to perform searches of major newspapers for terms related to uncertainty, and then to use the results to construct uncertainty indices. Second, derive uncertainty from stochastic-volatility estimates of various types of small and large-scale structural models related to macroeconomics and finance. And third, use the dispersion or disagreement among professional forecasters to measure uncertainty. In this paper, we use the news-based measure. This measure has the merit of not requiring any complicated estimation of a large-scale model to generate it in the first place and, hence, is not model-specific. In addition, the data is available publicly for download. 

- 7 See: https://uk.housing-observatory.com/dashboard.html. 

- 8 The data is downloadable from: http://policyuncertainty.com/uk_monthly.html. 

- 9 In particular, for sign identification, the national factor for Camden and the City of London is restricted to be positive, whereas the sign restriction on regional factor loadings is chosen arbitrarily. We achieve scale normalization by following Sargent and Sims (1977), Stock and Watson (1989, 1993), and Del Negro and Otrok (2007) 

20 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

and restrict σ<sup>2</sup> n<sup>andσ2</sup> r<sup>tounity.Thesignandscalenormalizationdoesnothaveany</sup> economic content and does not affect any economic inference (Neely and Rapach, 2011). 

- 10 We use the standard priors, similar to those in Kose et al. (2003) and Del Negro and Otrok (2007). Idiosyncratic shocks follow an inverse-gamma distribution with parameters 6 and 0.001. The AR polynomial follows a normal distribution with tighter centering on zero. The factor loadings are standard normal. 

- 11 All estimations are obtained using the Dieppe et al. (2018) BEAR Matlab-based toolbox. 

- 12 We replicate the analysis by restricting the sample to 1998Q1–2019Q2, ensuring consistency across all estimations. The results remain robust, with some even demonstrating stronger effects. In particular, the impact of housing uncertainty shocks on the national factor became more pronounced, underscoring the robustness of our findings. These results, available from the authors upon request, confirm that excluding the quarters associated with the Asian Financial Crisis (1997) and the initial stages of the COVID-19 pandemic (2020) does not alter the conclusions. 

- 13 Contrary to the frequentist framework, forecast error variance decomposition components may not add up to 1 because the Bayesian approach is based on the full distribution rather than a single-point estimate. 

- 14 The historical decompositions are obtained from the posterior median draw. 

- 15 The data is downloadable from: https://www.ljkmfa.com/test-test/united-statesshadow-short-rate-estimates/. 

### References 

Akimov A, Stevenson S, Young J (2015) Synchronisation and commonalities in metropolitan housing market cycles. Urban Stud 52(9):1665–1682 

Alessandri P, Mumtaz H (2019) Financial regimes and uncertainty shocks. J Monet Econ 101:31–46 

- André C, Bonga-Bonga L, Gupta R, Mwamba JWM (2017) Economic policy uncertainty, US real housing returns and their volatility: a nonparametric approach. J Real Estate Res 39(4):493–513 

- Andreasen M, Caggiano G, Castelnuovo E, Pellegrino G (2024) Does risk matter more in recessions than in expansions? Implic Monet Policy J Monet Econ 143:103533 

- Antonakakis N, André C, Gupta R (2016) Dynamic spillovers in the United States: stock market, housing, uncertainty and the macroeconomy. South Econ J 83(2):609–624 

- Antonakakis N, Chatziantoniou I, Floros C, Gabauer D (2018) The dynamic connectedness of UK regional property returns. Urban Stud 55(14): 3110–3134 

- Antonakakis N, Gupta R, André C (2015) Dynamic co-movements between economic policy uncertainty and housing market returns. J Real Estate Portf Manag 21(1):53–60 

- Aye GC (2018) Causality between economic policy uncertainty and real housing returns in emerging economies: a cross-sample validation approach. Cogent Econ Financ 6(1):1473708 

- Aye GC, Clance MW, Gupta R (2019) The effect of economic uncertainty on the housing market cycle. J Real Estate Portf Manag 25(1):67–75 

- Baker SR, Bloom NA, Davis SJ (2016) Measuring economic policy uncertainty. Q J Econ 131(4):1593–1636 

- Balcilar M, Roubaud D, Uzuner G, Wohar ME (2021) Housing sector and economic policy uncertainty: a GMM panel VAR approach. Int Rev Econ Financ 76:114–126 

- Baumeister C, Benati L (2010) Unconventional monetary policy and the great recession. European Central Bank Working Paper, No:1258 

- Berkovec JA, Goodman Jr JL (1996) Turnover as a measure of demand for existing homes. Real Estate Econ 24(4):421–440 

- Bloom NA (2009) The impact of uncertainty shocks. Econometrica 77(3): 623–685 

Bouri E, Gupta R, Kyei CK, Shivambu R (2021) Uncertainty and daily predictability of housing returns and volatility of the United States: evidence from a higherorder nonparametric causality-in-quantiles test. Q Rev Econ Financ 82:200–206 

- Brausewetter L, Thomsen SL, Trunzer J (2024) Regional supply and demand fundamentals in the german housing price boom. Ger Econ Rev 25(1):1–36 

Caggiano G, Castelnuovo E, Nodari G (2022) Uncertainty and monetary policy in good and bad times: a Replication of the VAR investigation by Bloom (2009). J Appl Econ 37(1):210–217 

Caggiano G, Castelnuovo E, Delrio S, Kima R (2021) Financial uncertainty and real activity: the good, the bad, and the ugly. Eur Econ Rev 136: 103750 

Caggiano G, Castelnuovo E, Pellegrino G (2021) Uncertainty shocks and the great recession: nonlinearities matter. Econ Lett 198:109669 

Caggiano G, Castelnuovo E, Figueres JM (2020) Economic policy uncertainty spillovers in booms and busts. Oxf Bull Econ Stat 82(1):125–155 

- Caggiano G, Castelnuovo E, Pellegrino G (2017) Estimating the real effects of uncertainty shocks at the zero lower bound. Eur Econ Rev 100:257–272 

- Caggiano G, Castelnuovo E, Figueres JM (2017) Economic policy uncertainty and unemployment in the United States: a nonlinear approach. Econ Lett 151:31–34 

- Caggiano G, Castelnuovo E, Groshenny N (2014) Uncertainty shocks and unemployment dynamics in U.S. recessions. J Monet Econ 67:78–92 

- Caraiani P, Gupta R, Lau CKM, Marfatia HA (2021) Effects of conventional and unconventional monetary policy shocks on housing prices in the United States: the role of sentiment. J Behav Finance https://doi.org/10.1080/ 15427560.2020.1865963 

- Cepni O, Guney IE, Swanson NR (2020) Forecasting and nowcasting emerging market GDP growth rates: the role of latent global economic policy uncertainty and macroeconomic data surprise factors. J Forecast 39(1):18–36 

- Choudhry T (2020) Economic policy uncertainty and house prices: evidence from geographical regions of England and Wales. Real Estate Econ 48(2):504–529 

- Chow S-C, Cunado J, Gupta R, Wong W-K (2018) Causal relationships between economic policy uncertainty and housing market returns in China and India: evidence from linear and nonlinear panel and time series models. Stud Nonlinear Dyn Econ 22(2):1–15 

- Christou C, Gabauer D, Gupta R (2020) Time-Varying impact of uncertainty shocks on macroeconomic variables of the united kingdom: evidence from over 150 years of monthly data. Financ Res Lett 37:101363 

- Christou C, Gupta R, Hassapis C (2017) Does economic policy uncertainty forecast real housing returns in a panel of OECD countries? A Bayesian approach. Q Rev Econ Financ 65:50–60 

- Christou C, Gupta R, Nyakabawo W (2019) Time-varying impact of uncertainty shocks on the US housing market. Econ Lett 180:15–20 

- Christidou M, Fountas S (2018) Uncertainty in the housing market: evidence from US states. Stud Nonlinear Dyn Econ 22(2):1–17 

- Cifci E, Tidwell A, Clements JS, Jauregui A (2023) Housing performance and the electorate. J Real Estate Res 45:462–484 

- Clapp JM, Eichholtz P, Lindenthal T (2013) Real option value over a housing market cycle. Reg Sci Urban Econ 43(6):862–874 

- Cogley T, Sargent TJ (2005) Drift and volatilities: monetary policies and outcomes in the post WWII U.S. Rev Econ Dyn 8(2):262–302 

- Cohen J, Coughlin C, Soques, D (2023) Housing price cycle interdependencies and comovement: a Markov-Switching Approach. J Real Estate Res, 1–30 

- Del Negro M, Otrok C (2007) 99 Luftballons: monetary policy and the house price boom across US states. J Monet Econ 54(7):1962–1985 

- Diamond DW, Rajan RG (2012) Illiquid banks, financial stability, and interest rate policy. J Polit Econ 120(3):552–591 

- Dieppe A, Legrand R, van Roye B (2018). The Bayesian Estimation, Analysis and Regression (BEAR) toolbox. Technical Guide. Version 4.2. European Central Bank, Frankfurt. Available at: https://www.ecb.europa.eu/pub/research/ working-papers/html/bear-toolbox.en.html 

- El Montasser G, Ajmi AN, Chang T, Simo-Kengne BD, André C, Gupta R (2016) Cross-country evidence on the causal relationship between policy uncertainty and house prices. J Hous Res 25(2):195–211 

- Fairchild J, Ma J, Wu S (2015) Understanding housing market volatility. J Money Credit Bank 47:1309–1337 

- Gabauer D, Gupta R, Marfatia HA, Miller SM (2024) Estimating US housing price network connectedness: Evidence from dynamic Elastic Net, Lasso, and ridge vector autoregressive models. Int Rev Econ Financ 89:349–362 

- Gupta R, Ma J, Theodoridis K, Wohar ME (2023) Is there a national housing market bubble brewing in the United States? Macroecon Dyn 27(8): 2191–2228 

- Gupta R, Ma J, Risse M, Wohar ME (2018) Common business cycles and volatilities in US states and MSAs: the role of economic uncertainty. J Macroecon 57:317–337 

- Gupta R, Marfatia HA, Pierdzioch C, Salisu AA (2021) Machine learning predictions of housing market synchronization across US states: the role of uncertainty. J Real Estate Finance Econ https://doi.org/10.1007/s11146-02009813-1 

- Hirata H, Kose MA, Otrok C, Terrones ME (2013) Global house price fluctuations: synchronization and determinants. NBER Int Semin Macroecon Univ Chic Press 9(1):119–166 

- Huang W-L, Lin W-Y, Ning S-L (2020) The effect of economic policy uncertainty on China’s housing market. North Am J Econ Financ 54:100850 

- Huber F, Pfarrhofer M, Piribauer P (2020) A multi country dynamic factor model with stochastic volatility for euro area business cycle analysis. J Forecast 39(6):911–926 

- Jurado K, Ludvigson SC, Ng S (2015) Measuring uncertainty. Am Econ Rev 105(3):1177–1216 

21 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

ARTICLE 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | https://doi.org/10.1057/s41599-025-04494-8 

Kallberg JG, Liu CH, Pasquariello P (2014) On the price comovement of US residential real estate markets. Real Estate Econ 42(1):71–108 

- Kang W, Lee K, Ratti RA (2014) Economic policy uncertainty and firm-level investment. J Macroecon 39:42–53 

- Katagiri M (2018) House price synchronization and financial openness: a dynamic factor model approach. International Monetary Fund 

- Klarl T (2018) Housing is local: applying a dynamic unobserved factor model for the Dutch housing market. Econ Lett 170:79–84 

Kose MA, Otrok C, Whiteman CH (2003) International business cycles: world, region, and country-specific factors. Am Econ Rev 93(4):1216–39 

- Kose MA, Otrok C, Whiteman CH (2008) Understanding the evolution of world business cycles. J Int Econ 75(1):110–130 

- Krippner L (2013) Measuring the stance of monetary policy in zero lower bound environments. Econ Lett 118:135–38 

Krippner L (2015). Zero lower bound term structure modeling: a practitioner’s guide. Palgrave-Macmillan 

Krippner L (2020) A note of caution on shadow rate estimates. J Money Credit Bank 52(4):951–962 

Leamer EE (2007) Housing is the business cycle. Proceedings - Economic Policy Symposium - Jackson Hole, Federal Reserve Bank of Kansas City, 149–233 Leamer EE (2015) Housing really is the business cycle: what survives the lessons of 2008-09? J Money Credit Bank 47(1):43–50 

Lin PT, Robberts, A (2023). Regional house price convergence: implications of monetary policy. Reg Stud, 1–13 

- Luo S, Ma J (2016). Global housing markets and monetary policy spillovers: evidence from OECD countries. J Money Credit Bank 

Marfatia HA (2021) Modeling house price synchronization across the U.S. states and their time-varying macroeconomic linkages. J Time Ser Econ 13(1): 73–117 

Miles W (2020) Regional UK house price co-movement. Appl Econ 52(45): 4976–4991 

- Montagnoli A, Nagayasu J (2015) UK house price convergence clubs and spillovers? J Hous Econ 30:50–58 

- Neely CJ, Rapach DE (2011) International comovements in inflation rates and country characteristics. J Int Money Financ 30(7):1471–1490 

- Nguyen T, Staer A, Yang J (2022) Initial public offerings and local housing markets. J Real Estate Res 44(2):184–218 

- Nguyen Thanh B, Strobel J, Lee G (2020) A new measure of real estate uncertainty shocks. Real Estate Econ 48(3):744–771 

- Noh S (2020) The effects and origins of house price uncertainty shocks. Available at SSRN 3530350 

- Otrok C, Whiteman CH (1998) Bayesian leading indicators: measuring and predicting economic conditions in Iowa. Int Econ Rev 39(4):997–1014 

- Pellegrino G, Castelnuovo E, Caggiano G (2023) Uncertainty and monetary policy during the great recession. Int Econ Rev 64(2):577–606 

Plakandaras V, Gupta R, Katrakilidis C, Wohar ME (2020) Time-varying role of macroeconomic shocks on house prices in the US and UK: evidence from over 150 years of data. Empir Econ 58(5):2249–2285 

Pomogajko K, Voigtländer M (2012) Co movement of house price cycles-a factor analysis. Int J Hous Mark Anal 5(4):414–426 

Watson MW (Eds.), Business cycles, indicators and forecasting. NBER Studies in Business Cycles, 28, University of Chicago Press for the NBER, Chicago 

- Strobel J, Nguyen Thanh B, Lee G (2020) Effects of macroeconomic uncertainty and labor demand shocks on the housing market. Real Estate Econ 48(2):345–372 

- Su D, Li X, Lobon t OR, Zhao Y (2016) Economic policy uncertainty and housing returns in Germany: evidence from a bootstrap rolling window. Zb Rad Ekonomskog fakulteta u Rijeci 34(1):43–61 

- Tsai I-C (2015) Spillover effect between the regional and the national housing markets in the UK. Reg Stud 49(12):1957–1976 

- van Eyden R, Gupta R, André, Sheng X (2022) The effect of macroeconomic uncertainty on housing returns and volatility: evidence from US state-level data. handbook of real estate and macroeconomics, Edited by Leung Ka Yui Charles 

- Wu JC, Xia FD (2016) Measuring the macroeconomic impact of monetary policy at the zero lower bound. J Money Credit Bank 48(2-3):253–291 

- Yusupova A, Pavlidis EG, Paya I, Peel DA (2020) UK Housing Price Uncertainty Index (HPU). UK Housing Observatory, Department of Economics, Lancaster University Management School 

- Zhang D, Ji Q, Zhao W-L, Horsewood NJ (2021) Regional housing price dependency in the UK: a dynamic network approach. Urban Stud 58(5):1014–1031 

### Author contributions 

All authors equally contributed to the submitted manuscript. 

### Competing interests 

The authors declare no competing interests. 

### Ethical approval 

This article does not report new results of any studies with human participants performed by the authors, so ethical approval is not applicable. 

### Informed consent 

This article does not report new results of any studies with human participants performed by the authors, so informed consent is not applicable. 

### Additional information 

Supplementary information The online version contains supplementary material available at https://doi.org/10.1057/s41599-025-04494-8. 

Correspondence and requests for materials should be addressed to Oguzhan Cepni. 

Reprints and permission information is available at http://www.nature.com/reprints 

Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Rajan RG (2011) Fault lines: how hidden fractures still threaten the world economy. Princeton University Press 

Saiz A (2010) The geographic determinants of housing supply. Q J Econ 125(3):1253–1296 

Salisu A, Gupta R, Ogbonna A, Wohar M (2021) Uncertainty and predictability of real housing returns in the United Kingdom: a regional analysis. University of Pretoria Department of Economics Working Paper Series, (No. 202102) 

Sargent T, Sims CA (1977) Business cycle modeling without pretending to have too much a priori economic theory. In New Methods in Business Cycle Research: Proceedings From a Conference, 45D109, Federal Reserve Bank of Minneapolis 

Sheng X, Marfatia HA, Gupta R, Ji Q (2021) House price synchronization across the US states: the role of structural oil shocks. North Am J Econ Financ 56:101372 

Stock JH, Watson MW (1989) New indexes of coincident and leading economic indicators. NBER Macroecon Annu 4:351–409 

Open Access This article is licensed under a Creative Commons AttributionNonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/. 

© The Author(s) 2025 

- Stock JH, Watson MW (1993) A procedure for predicting recessions with leading indicators: econometric issues and recent experience. In: Stock JH, 

22 

HUMANITIES AND SOCIAL SCIENCES COMMUNICATIONS | (2025) 12:195 | https://doi.org/10.1057/s41599-025-04494-8 

