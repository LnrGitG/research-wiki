---
title: What_drives_house_prices_in_Turkey_Evidence_from_B
type: paper
source_pdf: raw/papers/What_drives_house_prices_in_Turkey_Evidence_from_B.pdf
converted: 2026-08-18
---

Economic Change and Restructuring (2025) 58:8 https://doi.org/10.1007/s10644-024-09845-0 



# **What drives house prices in Turkey? Evidence from Bayesian SVAR model** 

#### **Mustafa Ozan Yildirim**<sup>**1,2**</sup> **· Özge Filiz Yildirim**<sup>**2,3**</sup> 

Received: 20 August 2024 / Accepted: 17 December 2024 / Published online: 8 January 2025 © The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2025 

#### **Abstract** 

Turkey has experienced one of the largest rises in house prices in the world, particularly after the COVID-19. Given the entangled relationship between house prices, macroeconomics, and financial markets, it is crucial to understand the causes of house price hikes from both academic and policy perspectives. This study aims to identify the determinants of house prices in Turkey. The analysis employs a Bayesian sign- and zero-restricted Structural Vector Autoregression (SVAR) model, utilizing monthly data spanning the period from January 2011 to December 2023. The model incorporates six shocks considered to affect house prices: housing supply, housing demand, credit conditions, mortgage rates, exchange rates, and market sentiment. The findings reveal that housing supply, mortgage rates and credit conditions are the primary drivers of house prices in Turkey. Prior to 2018, housing supply shocks accounted for nearly half of the observed increase in house prices. However, in the post-2018 period, mortgage rates and credit conditions emerged as the predominant drivers of house price dynamics. Moreover, consumer sentiment and exchange rate fluctuations also significantly contribute to house price variations. These findings offer valuable policy insights for mitigating the risk of housing market booms. 

**Keywords** House prices · Housing market · Sign and zero restrictions · Bayesian SVAR · Turkey 

**JEL Classification** C32 · E32 · E51 · R31 

> * Özge Filiz Yildirim 

> ozgefiliz.yagcibasi@ikc.edu.tr; ozge.yildirim@kcl.ac.uk 

> 1 Department of Economics, Pamukkale University, Denizli, Turkey 

> 2 Department of Banking and Finance, King’s Business School, King’s College London, London, UK 

> 3 Department of Economics, Izmir Katip Çelebi University, İzmir, Turkey 

Vol.:(0123456789) 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 2 of 24 

Economic Change and Restructuring (2025) 58:8 

### **1 Introduction** 

The housing market has been closely monitored by policymakers, academics, and financial markets, especially since the 2008 crisis, due to its significant macroeconomic implications (Kishor 2023). Housing crises in various economies, particularly in the United States, Europe, and Asia, have prompted a re-examination of the factors influencing house price dynamics and the appropriate macroeconomic policies to address housing booms and busts (Hanck and Prüser 2020). 

The importance of the housing sector for the wider macroeconomic context can be elucidated through a series of interrelated factors. Firstly, the housing sector’s contribution to gross domestic product (GDP) can reach up to 10 per cent (OECD 2024 ). As a significant share of household wealth is derived from housing, the housing market exerts an influence on aggregate demand through the wealth effect. As evidenced by the 2008 crisis, the housing market affects financial stability through several channels, including household indebtedness, the balance sheets of financial institutions, and assets such as mortgage-backed securities. Furthermore, house prices exacerbate the impacts of other economic crises on macroeconomic variables (Rosenberg 2020; Mian and Sufi 2011). It is therefore reasonable to conclude that the housing market (particularly housing prices) plays a pivotal role in household budgets and preferences, financial stability, and macroeconomic dynamics. 

In the last few years, following the COVID-19 pandemic, house prices have risen relentlessly, which was not the case in previous economic crises. This was largely attributable to interest rate cuts and fiscal subsidies introduced to stimulate economic activity (Lee et al. 2022; Melecky and Paksi 2024). Turkey was among the countries where house prices demonstrated a considerable increase. Figure 1 illustrates the upward trajectory in house prices that began during the period of the global pandemic and subsequently accelerated. Global house prices have soared by an average of 10.9% in the first quarter of 2022, according to the Knight Frank Global House Price Index (Knight 2022). During this period, Turkey experienced the highest growth among the countries analyzed, with nominal house prices increasing by 



<!-- Start of picture text -->
200.00<br>150.00<br>100.00<br>50.00<br>0.00<br>-50.00<br>Nominal Real<br>2011-01 2011-05 2011-09 2012-01 2012-05 2012-09 2013-01 2013-05 2013-09 2014-01 2014-05 2014-09 2015-01 2015-05 2015-09 2016-01 2016-05 2016-09 2017-01 2017-05 2017-09 2018-01 2018-05 2018-09 2019-01 2019-05 2019-09 2020-01 2020-05 2020-09 2021-01 2021-05 2021-09 2022-01 2022-05 2022-09 2023-01 2023-05 2023-09 2024-01<br><!-- End of picture text -->

**Fig. 1** House Price Index in Turkey (annual % change) 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 3 of 24 **8** 

110% and real prices rising by 49%.<sup>1</sup> Despite a subsequent decline in the global house price index, house prices in Turkey continued to rise toward their historical peaks. As of September 2022, house prices in Turkey had surged by 189% in nominal terms and 84% in real terms based on year-on-year comparison (CBRT, 2022). 

Over the past two decades, the Turkish economy has encountered significant supply and demand shocks in the housing market, driven by a combination of unique socio-economic factors and policy decisions. The mortgage financing system introduced in Turkey in 2007 significantly stimulated the housing market by increasing demand for housing, facilitated by long-term borrowing opportunities at relatively low interest rates and favorable exchange rates. This policy shift was instrumental in enabling Turkish households to access credit, thereby boosting the housing sector. On the other hand, the short-term international capital flows that entered the country after the global financial crisis resulted in an extraordinary flow of funds in the construction sector in Turkey, which contributed to economic growth significantly. In 2014, the annual number of housing units in Turkey reached a maximum of 1 million for the first time in history. In 2017, the production of residential buildings in Turkey peaked at an unprecedented 1.4 million units. Between 2010 and 2018, annual residential construction never fell below 600,000 units, reflecting sustained demand and a growing housing market (Yıldırım, 2023). Between 2010 and 2017, the construction sector in Turkey experienced a notable growth rate of 11%, driven by strong demand in the housing market and favorable policy conditions. 

However, from 2018 to 2022, the sector faced a contraction of −4.7%, reflecting the challenges posed by economic instability, rising interest rates, and currency depreciation during this period. The sudden deterioration in the housing market is the result of a confluence of different factors on both the supply and demand sides of the housing market. One significant factor is the continued depreciation of the Turkish lira, which has been ongoing since August 2018, reflecting a combination of domestic economic challenges and external pressures. The appreciation of the US dollar from 5.94 to 6.88 on the same day in August 2018, as a consequence of the political crisis between Turkey and the United States, exemplifies one of the recent crises in the Turkish economy. Consequently, the Central Bank of Republic of Turkey (CBRT) raised the policy rate by 625 basis points from 16.75 per cent to 24 per cent in September 2018. In August 2018, the exchange rate of the Turkish Lira against the US Dollar was 5.94, but by December 2023, it had risen to 29.5. This reflects a total depreciation of approximately 396.3% of the Turkish Lira against the US Dollar over the period. The sharp depreciation has resulted in a notable reduction in the supply of houses, largely due to the substantial increase in construction costs. 

Developments on the demand-side have been more complex. Despite the decline in per capita income due to the slowdown in economic growth, demand for housing has remained robust. One of the principal factors contributing to the enhanced housing demand and accelerated growth in asset prices (particularly real estate), was 

> 1 For further discussion on the existence of a real estate bubble in Turkey, see Özgüler et al. (2023), Vergili (2023), Akkaya (2024). 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 4 of 24 

Economic Change and Restructuring (2025) 58:8 

the series of political elections held in the country over the past five years. These elections were conducted under the influence of relatively loose monetary and fiscal policies. The expansionary policy stance characterized by historically low interest rates and fiscal stimulus, further amplified the demand for housing. Furthermore, the demographic shift toward urbanization, accompanied by migration from rural areas to cities, has contributed to strong housing demand. Meanwhile, the deterioration in inflation expectations has also contributed to the rise in house prices from 2020 onwards. Consequently, the high inflation environment in Turkey makes housing a significant component of wealth and a long-term investment tool for Turkish households (Özgüler et al. 2023). 

Additionally, external demand for real estate in Turkey has been considerable in the last decade. The influx of irregular migrants to Turkey from countries such as Syria, Afghanistan, Iran and Ukraine–Russia, coupled with the offer of citizenship to foreign nationals in exchange for the purchase of a property (Deniz and Çetinkaya 2024; Ghaedrahmati and Rezaei 2024), has also contributed to the notable surge in housing demand over the past decade. While the proportion of housing sales to nonresidents in total housing sales was 1.1% in 2013, following the removal of legal barriers to the acquisition of housing by non-residents, this ratio reached its highest value of 4.5% in 2022 (TURKSTAT, 2024). 

The primary objective of this paper is to identify the factors contributing to the fluctuations in housing prices in Turkey. This study contributes to the existing literature in several aspects. Firstly, as a developing country with the highest rate of house price growth in the world, Turkey presents an intriguing and highly favorable context for analysis. Turkey’s housing market stands out from many emerging economies experiencing rising housing prices due to its prolonged exposure to macroeconomic instability. High inflation, sharp currency depreciation, and unorthodox monetary policies have created an uncertain climate, exacerbated by the influx of refugees and soaring rigid inflation expectations. These factors have intensified demand-side pressures and disrupted housing supply chains, resulting in a market dynamic that is both volatile and complex. 

Secondly, to the best of our knowledge, this is the first study that examines the drivers of house prices in Turkey using an SVAR model with sign and zero identification restrictions. The development of house prices is decomposed into six structural shocks: housing supply, housing demand, mortgage rate, credit, sentiment, and exchange rate shocks. The model is estimated using Bayesian econometric methods based on data from January 2011 to December 2023. This approach allows for more precise identification of the structural shocks, facilitating a more accurate analysis of the impulse response functions when additional information is used. The Bayesian approach is gaining prominence in housing literature (see Wu et al. 2017; Rosenberg 2019, 2020; Lee et al. 2022; Ma and Zhang 2022; Lee 2023). 

The year 2018 marked a pivotal turning point for the Turkish economy, leading to substantial shifts in its macroeconomic landscape. In response, the study reestimates the model across two distinct sub-periods to investigate whether the key determinants of house prices evolved following this critical juncture. 

The remaining sections are structured as follows: The second section provides a brief review of the relevant literature. Following the presentation of data and the 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 5 of 24 **8** 

methodology, the fourth section presents the empirical findings. Robustness checks of the findings are demonstrated in the fifth section. Finally, the study concludes. 

### **2  Literature** 

A substantial body of literature exists on the drivers of house prices. Given the intimate interconnectivity between the housing sector and broader macroeconomic variables, it is reasonable to conclude that the housing market is susceptible to fluctuations in these macroeconomic factors. The relationship between housing demand, housing supply, monetary policy, credit conditions and house prices has been the focus of numerous studies, with the vector autoregression (VAR) models being the preferred method of analysis (Iacoviello and Minetti 2008; Bjørnland and Jacobsen 2010; Wadud et al. 2012 ). Additionally, some studies examine the influence of non-fundamental beliefs, such as expectations and preference shocks, on house price fluctuations. For example, Lambertini et al. (2017) demonstrate that expectations regarding macroeconomic developments influence both housing market cycles and business cycles. This study makes a further contribution in demonstrating that favorable credit conditions in the short term can give rise to housing booms. Similarly, Towbin and Weber (2015) demonstrate that price expectations positively influence house prices, with this effect being more pronounced than that of housing market fundamentals. 

Following the subprime mortgage crisis, many studies have concentrated on the impact of prolonged periods of low interest rates and credit conditions on house price dynamics. Bjørnland and Jacobsen (2010) highlight the existence of a simultaneous and reciprocal relationship between unexpected interest rate changes and house prices. Öhman and Yazdanfar (2018) identify the causal relationship between bank lending and real estate prices. Asal (2018) posits that an expansionary monetary policy engenders an expansion in mortgage lending, which contributes to real house price rises. 

Similarly, there is a literature using a Bayesian SVAR framework to explore house price dynamics. Several studies have explored the determinants of housing prices across various countries. For instance, Ma and Zhang (2022), Lee (2023), and Chen et al. (2024 ) analyze the factors influencing housing prices in the United States; while, Robstad (2018) investigates the Norwegian housing market. Additionally, research by Hanck and Prüser (2020) focuses on Germany, Rosenberg (2019, 2020) examines the housing market in the Nordic countries, and Nsafoah and Dery (2024) provide insights into Canada’s housing price dynamics. The findings indicate that financial conditions (credit supply, housing interest rate and monetary policy) have a considerable effect on real estate prices. Conversely, Lee et al. (2022) posits that the essential driver of housing prices in Korea is housing demand (sentiment) shocks, rather than financial variables, in both the long and short term. In contrast, Ma and Zhang (2022) and Chen et al. (2024) demonstrate that the impact of expectations shocks is comparatively limited. Lee (2023) posits that a housing supply shock is also an important contributing factor. Rosenberg 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 6 of 24 

Economic Change and Restructuring (2025) 58:8 

(2019) and Nsafoah and Dery (2024) emphasized the considerable role of unconventional monetary policy, in addition to that of conventional monetary policy. 

A large collection of literature analyzing the Turkish housing market is available. Studies on the Turkish housing market can be categorized into three main areas: 

1. Identifying the determinants of housing demand. Bekmez and Özpolat (2016), Lebe and Akbaş (2014), Uysal ve Yiğit (2015), Solak ve Kabadayı (2016), Özgüler et al. (2023). 

2. Investigating whether there is a bubble in the housing market. Vergili, (2023), Akkaya (2024), Coşkun vd (2017), (Cagli 2019). 

3. Examining the relationship between housing prices and various macroeconomic variables. 

This study primarily concentrates on the third category, which is most closely associated with the current study. Research on housing prices can be categorized into three key dimensions: methodological approaches, focal variables, and the spatial scope of analysis (city, regional, or national levels). The most preferred choice of methodology includes Causality (Şeyranlıoğlu 2023; Ovalı and Çayırlı, 2023; Korkmaz, 2020; Akçay et al. 2023; Kırca and Canbay 2022; Çalışkan et al. 2022), ARDL/NARDL (Salami et al. 2023; Akpolat 2024; Akça, 2022; Usta 2021; Kırıkkaleli et al. 2021; Özcan 2023; Çetin, 2021; Akkay, 2021; Karadaş ve Salihoğlu 2020; Varlık 2020) and VAR based studies (Akçay and Akyüz, 2024; Şıklar 2024; Bayır, 2019; Afşar and Yüksel 2022; Yıldırım and İvrendi 2017; Karakoyun and Yıldırım, 2017, Balcılar et al. 2024; Canoz and Kalkavan 2024; Şıklar 2024). 

Macro variables, particularly financial conditions, are the primary drivers of property prices, in line with the global literature. (Yıldırım and Yağcıbaşı 2019; Tunc 2020; Yıldırım and İvrendi 2021; Afşar and Yüksel 2022; Kırca and Canbay 2022; and Akcay 2023). Akgündüz et al. (2023) demonstrate that a one percentage point decline in annual housing interest rates results in a rise in real estate credits by 3.3% and a corresponding rise in house prices by 1.6%. Furthermore, Akçay et al. (2023) emphasized the presence of a strong unidirectional causal link between mortgage loans and house prices. Akçay and Akyuz (2024) validated a bidirectional relation between housing loans and real estate prices before COVID-19. However, their research revealed that this relationship disappeared with the onset of the pandemic. 

Studies conducted for Turkey show that factors other than financial conditions 2022), sentiments affect house prices, including exchange rates (Kırca and Canbay (Usta 2021 2023). ), and inflation and exchange rate uncertainties (Ovalı and Çayırlı, The asymmetric relationship between various macroeconomic variables and house prices is another area of interest. Among these, Varlık (2020) demonstrates that positive shocks in industrial production have a more pronounced impact on house prices than negative shocks; while, Akpolat (2024) illustrates that contractionary money supply influences real estate prices more than expansionary money supply. 

A further area of literature that analyses house prices in Turkey using Bayesian methods focuses on regional house prices. Balcılar et al. (2024) studied the 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 7 of 24 **8** 

interconnectedness of real estate prices in 26 regions in Turkey using a regional Lasso VAR model. Their findings revealed that house prices in 26 regions are interconnected in a structure that exhibits an even greater degree of interconnectedness in the aftermath of the crisis. Canoz and Kalkavan (2024) employed a Bayesian time-varying VAR model to study the rapid escalation of Istanbul real estate prices in the context of housing affordability. According to their findings, housing prices are driven by housing supply (construction costs) and housing demand (the sale of real estate to foreign nationals and the increase in refugee migration), as well as by fluctuations in mortgage rates. 

Overall, studies investigating the macroeconomic factors influencing housing prices in Turkey have produced inconsistent results, primarily attributable to variations in methodologies, sample periods, and the variables utilized. This study contributes to existing literature in several ways. By employing a detailed approach to shock decomposition, modeling monetary policy and credit conditions separately to observe their distinct effects on housing prices. It also incorporates sentiment and exchange rate shocks into a SVAR framework to account for external shocks and speculative demand in the Turkish economy, resulting in a comprehensive mediumsized model. This study introduces a novel methodological approach by employing a Bayesian framework with sign restrictions to analyze housing prices at the national level in Turkey for the first time. The Bayesian framework is particularly well-suited for small sample sizes, and the application of sign restrictions—a widely adopted and contemporary method—ensures that shock identification aligns with economic theory. Moreover, unlike existing studies, this research distinguishes between the pre- and post-COVID and currency crisis periods, enabling an investigation of the heterogeneity in the effects of macroeconomic shocks across these two distinct phases. 

### **3  Data and methodology** 

#### **3.1  Data** 

The study employs monthly data between the 2011m1-2023m12 period. The choice of data is relying on the beginning date of house prices. Six variables used in the study are as follows: house price index ( _hpi_ ) _,_ housing permits( _permits_ ),<sup>2</sup> consumer confidence index ( _sentiment_ ),<sup>3</sup> mortgage interest rate ( _hrate_ ) _,_ housing loan ( _hloan_ ) _,_ real effective exchange rate( _reer_ ).<sup>4</sup> The number of housing permits, house price index, and housing loans are seasonally adjusted with the Tramo/Seats method, and house prices and 

> 2 Two and more dwelling residential buildings (Total, Number of Dwelling Units) are used to represent the housing permit data as in line with Ozdemir ve Aksoy (2023). 

> 3 Consumer confidence index serves as a proxy variable for housing sentiments and expectation of future economic conditions. 

> 4 In this configuration, increases in the real effective exchange rate implies an appreciation of the Turkish lira in relation to foreign currencies. 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 8 of 24 

Economic Change and Restructuring (2025) 58:8 

housing loans are also deflated by the Consumer Price Index (CPI). Logarithmic differences have been taken for all data except for the mortgage interest rate. House prices, consumer confidence index, mortgage interest rate, housing loans and real effective exchange rates are retrieved from the Central Bank of the Republic of Turkey (CBRT), and housing permit is compiled from the Turkish Statistical Institute (TURKSTAT). The summary statistics of data and results of the unit root tests are available in "Appendix A". 

#### **3.2  Bayesian SVAR model** 

The SVAR analysis identifies housing market shocks and factors influencing house prices in Turkey. This methodology has become a standard tool in macroeconomics due to its advantages in analyzing the dynamic relationships among multiple time series variables. VAR models can be conceptualized as a system of equations in which each dependent variable is described by its own lags and the lags of the explanatory variables, which are themselves the dependent variables in the system (Sims, 1980). Instead of estimating parameters, VAR analysis aims to identify the relationships between variables. Some of the prominent features of VAR models include the elimination of the endogenous–exogenous variable distinction, flexibility, ease of interpretation, and robust forecasting capacities. 

Nevertheless, these models can comprise a large number of parameters, even for models of intermediate complexity, which gives rise to a phenomenon known as overparameterization. This ultimately results in the estimation of parameters that are not accurate (Öğünç, 2019). The Bayesian method addresses this issue by employing prior information about the parameters and combining it with the likelihood function based on the sampled data through the application of Bayes theorem (Rooj and Kaushik, 2023). This approach effectively addresses the issue of high dimensionality in estimation, offering the advantage of providing an empirical measure of the uncertainty surrounding the estimates. Consequently, this method utilizes a larger amount of information than frequentist econometrics. In recent years, the increase in computational power has led to a rise in the popularity of Bayesian inference as a shrinkage method to address over-parameterization problems, as first proposed by Doan et al. (1984). This estimation method is particularly advantageous in circumstances where data availability and quality are constrained, a scenario that frequently arises in emerging countries. In many respects, Bayesian vector autoregressions (VARs) are preferable to traditionally estimated VARs (Dieppe et al. 2016). 

� Our model consists of n = 6 endogenous variable _yt_ =<sup>[</sup> _y_ 1, _t_ , … , _yn_ , _t_ ] . For the model specification, following Dieppe et al. (2016): 



where _T_ represents the sample size, _p_ is the lag order, _A_ 0 is the invertible matrix of contemporaneous relationships between variables, _Al_ denotes the structural parameters at lag _l_ , _c_ is the vector of constant terms, and _휂t_ represents the structural shocks. 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 9 of 24 **8** 

Inference by multiplying Eq. (1) by _A_<sup>−1</sup> we reach the reduced form VAR which is more appropriate to use in Bayesian approach: 



Following the sign restriction literature, the VAR is assumed to be of finite order. The vector of endogenous variables _yt_ can be expressed as follows: 



The necessity for the data set to be stationary is waived by Bayesian analysis, as the likelihood function is maintained as a Gaussian distribution even in instances where unit roots are present (Sims et al. 1990. The lag length is set as 2 by using the Schwartz information criteria. 

#### **3.3  Identification scheme** 

This section presents the assumptions underlying the economic rationale and points out a novel identification scheme. This scheme imposes sign and zero restrictions and decomposes the fluctuations in real house prices into six distinct shocks. Sign restrictions permit the formulation of explicit a priori theorizing while simultaneously minimizing its usage (Uhlig, 2005). The incorporation of zero restrictions into the identification scheme, in conjunction with sign restrictions, serves to enhance the precision of the identification of structural shocks. The combination of sign and zero restrictions typically results in a reduction in the number of constraints required for identification, leading to more robust conclusions than those reached using the Cholesky identification scheme (Arias et al. 2018). 

Table 1 presents the relevant signs and zero restrictions on variables. All signs have been calibrated to produce a positive initial response in housing prices, implying that the positive shocks of housing demand, credit supply and sentiment correspond to house price appreciation expectations, a decline in mortgage rate and easing of credit standards, respectively, and lasting for two quarters. To ensure the robustness of the findings of the study while successfully identifying shocks, minimal restrictions were imposed, and all other responses were left undetermined. 

The empty cells indicate coefficients that are not restricted. 

_A positive shock in the demand for housing_ can be attributed to a rise in household income and/or a shift in demographic factors, such as migration or urbanization. This may shift the housing demand curve upward. Hence, enhanced demand puts upward pressure on prices at a given level of housing supply. Following BenDavid et al. (2019) and Lee (2023), it is assumed that an expansion in demand may also result in an expansion of the housing supply, driven by the incentive to generate greater profits for the housing construction market. It is further assumed that monetary policy is unresponsive to housing demand in the first period. 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 10 of 24 

Economic Change and Restructuring (2025) 58:8 

**Table 1** Identifying the shocks 

||Housing<br>demand|Housing supply|Mortgage Rate|Credit|Sentiment|Exchange rate|
|---|---|---|---|---|---|---|
|_hpi_|+|+|+|+|+|+|
|_permit_|+|−|+|+|+|−|
|_hrate_|0||−|0|||
|_hloan_||||+|||
|_sentiment_|||||+||
|_reer_||||||−|



_A negative shock in the supply of housing_ may occur because of an increase in land and construction costs, natural disasters such as earthquakes, or urban transformation. In the event of a negative supply shock, the housing supply curve shifts downwards. Consequently, as the number of building permits decrease, house prices will rise. From a supply perspective, builders may also be incentivized to build more homes as house prices rise. 

_A negative mortgage rate shock_ can be defined as a reduction in mortgage interest rates resulting from the easing of the monetary policy stance. It can be assumed that this decrease in the mortgage interest rate will diminish the opportunity cost of buying a house and stimulating credits for real estate purchases. These shocks may therefore have the effect of increasing house prices and the building permits, which in turn is conducive to an increase in the supply of new houses. 

_A positive credit shock_ is defined as a relaxation of credit standards, achieved through introducing new banking regulations or implementing macroprudential measures. It is crucial to differentiate between a shock to mortgage rates and credit conditions. Factors other than the mortgage rate that improve lending conditions should be considered in case of a positive credit shock. In the model, the decomposition of the shocks to the credit rate and the mortgage rate is carried out by placing a zero restriction on the impulse response of mortgage rate (Ma and Zhang 2022; Wu et al. 2017; Rosenberg 2019). Positive credit shock enables a broader pool of prospective homeowners to secure financing and, consequently, to purchase more residential properties, which in turn drives up house prices. 

_A positive sentiment shock_ is assumed to increase house prices through expectations. An optimistic environment may result from a variety of developments, including the relaxation of credit conditions, financial regulations, or shifts in price expectations (Bekiros et al. 2020; Kaplan et al. 2020; and Lee 2023). In a recent study, Chen et al. (2024) demonstrate that expansionary monetary policy can also stimulate housing demand by fostering an optimistic environment. Indeed, the rationale behind the assumption that house prices will rise may be non-fundamental. Shiller (2003) notes that rational economic factors do not sufficiently account for the current housing market fluctuations. Instead, psychological factors appear to play a notable role in this phenomenon. In any case, individuals expecting a rise in housing prices might prefer purchasing a real estate for speculative purposes. Consequently, 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 11 of 24 **8** 

elevated property values may prompt a greater influx of speculative investors, thereby precipitating a further surge in prices (Chen et al. 2024). 

_A negative exchange rate shock_ is defined as a depreciation of the local currency (the Turkish lira) against foreign currencies. A negative exchange rate shock may affect both the demand and supply of housing. As a small open economy, a significant proportion of economic activity in Turkey, including residential construction, is dependent on imported energy and inputs/raw materials. Consequently, changes in external variables, particularly energy prices, exert an influence on the domestic market through the exchange rate. This also increases the cost of construction and, consequently, housing prices (Akca, 2022). From the demand-side, a depreciation in the local currency makes Turkish property assets more affordable for foreign investors. Furthermore, the exchange rate pass-through may prompt some domestic savers to invest in real estate as a means of safeguarding their wealth and purchasing power against inflationary pressures. Consequently, a negative exchange rate shock can result in both domestic and external demand for housing. Following Bjornland and Jacobsen (2010), no simultaneous response of house prices to exchange rate fluctuations is assumed within the same quarter. 

### **4  Empirical findings and discussion** 

This section presents the study’s empirical findings and discusses the underlying factors contributing to the housing price surge. It aims to assess the plausibility of housing price responses to shocks and their magnitude and persistence. A Bayesian SVAR model was estimated with a normal-Wishart prior. This section begins by presenting the impulse response functions (IRFs) to illustrate the dynamic responses of housing prices to various shocks. Following this, the decomposition of house price fluctuations is analyzed through forecast error variance decomposition (FEVD), providing insights into the relative contributions of different shocks. Lastly, the findings from the historical decomposition are discussed to contextualize the temporal evolution of these impacts. 

#### **4.1  Impulse response functions** 

Figure 2 presents the impulse response function (IRF) graphs, constructed using the sign and zero restrictions outlined in the methodology section. Following Ben-David et al. (2016) and Ma and Zhang (2022), the magnitude of the shocks has been normalized to one; while, the sign of the shocks has been normalized to generate a positive initial response in house prices (negative housing supply shock, positive credit shock, etc.). 

The median responses of housing prices to the shocks are shown by the blue solid line. The shaded region encompassing the line represents the 68% credible interval for these responses. This interval differs from the conventional SVAR estimated using ordinary least squares (OLS), where these intervals are 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 12 of 24 

Economic Change and Restructuring (2025) 58:8 



**Fig. 2** Impulse response functions of shocks to real house prices 

interpreted as confidence intervals. The horizontal axis depicts the time or months following the initial impact of the shocks; while, the vertical axis illustrates the magnitude of the reaction to the explanatory shocks. Given that the model variables are defined in terms of natural logs, the y-axis represents the percentage change in the variable in response to a one-standard deviation shock. 

Firstly, all six shocks are significant in explaining house prices during the first five to ten months. Among the identified shocks, those related to mortgage rates and sentiments have the most long-lasting effect on housing prices. In response to a negative shock to the housing supply (a decline in construction permits), house prices initially rise over the first five months, then the response ceases to be statistically significant. Secondly, a negative shock to mortgage rates (i.e., a decrease in mortgage rates) results in a hike in real estate prices, which lasts approximately 10 months. Furthermore, positive shocks to credit and negative mortgage rate shocks are associated with a persistent rise in housing prices. The sensitivity of housing prices to financial conditions is not unanticipated, as this relationship is consistently documented in the literature (e.g., Yıldırım and İvrendi 2017; Akgündüz et al. 2023; Akçay et al. 2023). 

Figure 2 indicates an increase in consumer confidence, which can be defined as a positive sentiment shock, has the effect of driving up house prices over the short term, with a period of five months. As previously discussed, this behavior is primarily driven by speculative demand in the housing market. In periods of elevated consumer confidence, there is an anticipation that house price growth will persist over an extended period, thereby accelerating demand for housing and sustaining price increases (Anastasiou et al. 2023; Chen et al. 2024). Conversely, periods of declining house prices are associated with reduced consumer confidence. These findings are consistent with the conclusions drawn by Usta (2020), Uğur and Tosun (2021), and Akkaya (2024), who similarly highlight the interplay between housing market dynamics and consumer sentiment. 

Finally, consistent with existing literature, the IRFs demonstrate that depreciation in exchange rate results in a temporary increase in house prices (Kırca 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 13 of 24 **8** 

**Table 2** FEVD of the real house price fluctuations 

|Period|Housing supply|Housing demand|Mortgage rate|Credit|Sentiment|Exchange rate|
|---|---|---|---|---|---|---|
|Months|FEVD over entir|e sample|||||
|1–5|23.81|15.38|17.07|18.09|9.24|16.38|
|6–10|14.09|22.28|26.62|16.05|7.63|13.28|
|11–15|12.44|24.31|26.61|16.19|8.02|12.37|
|16–20|12.81|24.86|25.31|16.59|8.44|11.94|
|21–25|13.58|25.10|24.17|16.74|8.78|11.58|
|36|14.84|23.64|23.38|16.89|9.82|11.40|
|48|14.67|23.66|23.18|17.01|9.91|11.58|
|FEVD 2|011:1–2018:8||||||
|1–5|41.90|12.48|10.99|15.58|8.05|11.04|
|6–10|52.81|10.53|9.77|11.88|7.18|7.78|
|11–15|51.75|10.76|9.81|12.49|8.11|7.03|
|16–20|49.14|11.06|10.45|12.99|8.93|7.38|
|21–25|46.31|11.25|11.38|13.32|9.67|8.01|
|36|41.91|11.74|12.29|13.44|10.74|9.85|
|48|41.12|11.83|12.38|13.38|10.84|10.42|
|FEVD 2|018:9–2023:12||||||
|1–5|19.46|14.61|17.47|18.25|12.32|16.83|
|6–10|11.14|22.35|28.69|14.84|10.56|12.37|
|11–15|11.52|23.53|29.22|14.17|10.18|11.33|
|16–20|12.60|23.60|27.38|14.81|10.44|11.11|
|21–25|13.66|22.88|25.98|15.34|10.94|11.15|
|36|14.86|21.41|24.75|15.18|11.93|11.84|
|48|14.59|21.32|24.43|15.52|12.03|12.08|



and Canbay 2022; Şeyranlıoğlu 2023; Akpolat 2024; Canöz and Kalkavan 2024). Overall, IRF findings align with both economic intuition and a body of related literature, including studies by Nocera and Roma (2018), Robstad (2018), Lee (2023), and Chen et al. (2024). These studies support the plausibility of the SVAR model specification and identification assumptions in the present study. 

#### **4.2  Forecast error variance decomposition** 

Having presented information on the determinants of house prices using impulse response analysis, the study also investigated the extent to which these shocks explain the variability in real housing prices. Table 2 presents the relative contributions of various shocks to housing price dynamics in Turkey, based on the analysis of the full sample period as well as the two sub-sample periods (2011:1–2018:8 and 2018:8–2023:12). Table 2 reveals the percentage contribution of the structural shocks to the forecast error variance of house prices over horizons of 1–5, 6–10, 11–15, 16–20, 21–25, 36 and 48 months. 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 14 of 24 

Economic Change and Restructuring (2025) 58:8 

In the short term, changes in house prices are primarily influenced by housing supply shocks, which account for 23.8% of the variation, followed by credit shocks (18.1%), mortgage rate shocks (17%), and exchange rate shocks (16.3%). The contribution of the sentiment shock to the change in house prices is 9.2%. After 36 months, the impact of housing demand and mortgage rate fluctuations accounts for 23.6% and 23.3% of the observed variation in house prices, respectively. Credit shocks account for 16.8 per cent, housing supply shocks for 14.8 per cent, and exchange rate shocks for 11.4 per cent of the change in house prices. Finally, the FEVD of real house prices explained by sentiment shocks is the lowest for all periods, at 9.8%. Similarly, at longer horizons (e.g., 48 months or 4 years), the contributions of shocks on house prices remain almost constant. 

Next, Table 2, presents the results for the two sub-periods: 2011–2018 and 2019–2023. During the initial subperiod, the housing supply shock accounts for the majority of the observed house price fluctuations. This share rises to 52.8 per cent at the end of the tenth month and 41.9 per cent at the end of three years. Other shocks explain around 10–13 per cent of the change in house prices after three years. 

The weight of the shocks in the 2019–2023 period was found to be almost identical to the shares in the full sample. While almost all variables serve to the variation of house prices in close amounts in the short run, the effects of housing demand and the mortgage interest rate stand out in the long run. The forecast error variance decomposition (FEVD) reveals that mortgage rate shocks (24.7%), housing demand shocks (21.4%), credit shocks (15.1%), housing supply shocks (14.8%), sentiment shocks (11.9%), and exchange rate shocks (11.8%) all significantly impact house prices over the next 36 months. These factors, including income growth, consumer sentiment, credit availability, construction costs, land availability, regulatory policies, speculative demand, and currency fluctuations, collectively shape housing price dynamics. 

In the short run, supply shocks (changes in construction permits and cost pressures) typically have a more pronounced immediate impact on house prices because the housing market is often supply constrained (e.g., Lee 2023). These constraints imply that, even if demand for housing increases, the supply side may not be able to adjust promptly, resulting in substantial price fluctuations in the short term. For instance, rising construction costs, partly influenced by exchange rate depreciation, reduce the number of new housing projects, directly leading to upward pressure on prices in the short term. 

In contrast, demand shocks tend to have a more significant impact on house prices in the medium run as the housing market adjusts to shifts in economic conditions, such as changes in interest rates, income levels, or investor sentiment. These factors can alter the demand for housing, which, in turn, drives price dynamics more substantially over time. This dynamic is evident in Turkey, where strong demand for housing, driven by urbanization, migration, and inflation expectations, has sustained price increases in the medium run, even as supply gradually adjusts. 

Over the full sample, mortgage and housing demand shocks explain almost half of the variation; while, credit, housing supply, exchange rate and sentiment shocks capture relatively modest dispersion in real house prices, even over the long term. The period after 2018, however, reveals a noticeable shift. The sentiment shock 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 15 of 24 **8** 



<!-- Start of picture text -->
Real House Prices<br>0.3<br>0.2<br>0.1<br>0<br>-0.1<br>-0.2<br>2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023<br>Housing Supply Shock Housing Demand Shock Mortgage Rate Shock Credit Shock Sentiment Shock Exchange Rate Shock<br><!-- End of picture text -->

**Fig. 3** Historical decomposition of changes in real house prices 

becomes more prominent, accounting for a larger share of house price fluctuations than in the full sample. This shift underscores the growing importance of speculative demand and investor psychology in shaping housing markets, particularly in the post-crisis environment. This finding is also consistent with Şıklar, (2018). The heightened significance of sentiment shocks in Turkey following 2018 can be attributed to a multitude of contributing factors. Firstly, global pandemics, subsequent loose monetary policies, and the uncertainty of the global economic environment led households and investors to real estate as a perceived hedge against inflation and economic instability worldwide. Secondly, following the 2018 economic crisis, Turkey has experienced persistent high inflation and substantial currency depreciation, accompanied by an unorthodox monetary policy (Şıklar, 2024; Balcılar et al. 2024). Consequently, due to the economic turbulence and subsequent periods of monetary instability and uncertainty, real estate is perceived as a safer investment alternative to financial assets. Thirdly, the offer of citizenship in exchange for property investment and the influx of foreign buyers during this period may have further fueled speculative demand, amplifying the role of sentiment as a determinant of house prices. 

#### **4.3  Historical contribution of the housing prices** 

This section investigates the historical contributions of six identified shocks. Figure 3 shows the historical decomposition of monthly real house price changes from January 2011 to December 2023. The solid black line is the log of real house prices, the path that house prices would have taken if no shock had occurred since the start of the sample. The colored bars show the contribution of the six shocks to the observed path and the unexplained residual to the observed path. 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 16 of 24 

Economic Change and Restructuring (2025) 58:8 

It is worth noting that a significant proportion of the variation in housing prices can be accounted for by six shocks. Moreover, the historical contribution of the six shocks has varied noticeably over recent years. In general, in line with the findings drawn from the FEVD, the role of mortgage rate, exchange rate and credit supply shocks in real housing price fluctuations is larger than that of the sentiment shock. This is particularly true during periods of sharp increases in past years. The house price crash between 2017 and 2019 was caused by rising mortgage rates, reduced credit standards, and lowered expectations. Conversely, the housing boom between 2020 and 2023 was fueled by loosened credit, low interest rates, and the depreciation of the Turkish lira. It is also important to note that after 2022, the share of the housing market sentiment shock becomes larger, which contributes to the volatility of house prices to a certain extent. 

Meanwhile, it is also observed that housing supply shocks had a significant influence on housing prices in 2020, the year of the outbreak of COVID-19, and in 2023, the year of the Kahramanmaraş earthquake. In both instances, the reduction in the housing supply contributed to the escalation of house prices. Due to inflation and exchange rate impacts on construction costs, the rise in new housing units could not meet the strong demand, causing an imbalance in the housing market. 

The fluctuations in house prices became particularly evident with the COVID-19 pandemic effect. The rapid price increases in the housing market during these periods were caused by the mismatch between supply and demand, as the housing supply failed to keep pace with the growing demand. 

### **5  Robustness check** 

Robustness analysis is conducted to assess the sensitivity of the primary findings to alternative variable selection, data choices, and different priors. This analysis is presented in "Appendix A". This part provides the robustness checks of the results by estimating the baseline model with alternative variables. Following Vergili (2023) and Çalışkan et al. (2022), we replaced the HPI with the New House Price Index (NHPI), calculated using hedonic regression for houses built in the last two years (the current and previous years). To represent the Central Bank of Turkey’s monetary policy stance after 2011, we substituted the mortgage interest rate with the short-term interest rate, the weighted average funding rate commonly used in monetary policy literature. (as in Bulut, 2021 and Afşar and Yüksel 2022). Thirdly, to construct the sentiment of the housing market conditions, we included the economic confidence index.<sup>5</sup> Finally, as an alternative measure of foreign shocks to the housing market, the nominal exchange rate<sup>6</sup> is used in the model. 

> 5 The economic confidence index is a measure of consumers’ and producers’ expectations and tendencies with regard to the overall economic outlook. 

> 6 It is calculated as fifty percent dollar and fifty percent euro currencies. Therefore, in this paper, an appreciation of the exchange rate means a depreciation of the TRY against foreign currencies. 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 17 of 24 **8** 

The IRF, FEVD and historical decomposition under the alternative specification are presented in Figs. 4, 5 and Table 5, respectively, in "Appendix A." The analysis was also repeated with different priors. The results under different specifications, alternative variables and priors are consistent with the baseline results (Figs. 6 and 7 ). No significant change in the results was observed after the robustness checks. 

### **6  Conclusion** 

The interdependent relationship between house prices, the macroeconomy, and the financial market emphasizes the importance of understanding housing market fluctuations. This Bayesian SVAR model with sign and zero restrictions analyzes monthly housing price data from January 2011 to December 2023 to identify factors driving the accelerated increase in Turkey. IRFs, FEVD, and historical decomposition were used to evaluate the effect of potential determinants of real housing prices, identifying six shocks: housing supply shocks, housing demand shocks, mortgage rate shocks, credit shocks, sentiment shocks, and exchange rate shocks. 

The primary findings of the study are as follows. Firstly, changes in mortgage rates and increases in the volume of credit are the main drivers of real house prices, emphasizing the financially driven nature of the housing sector. Notably, consumer sentiment (confidence) has emerged as a crucial factor in explaining house price fluctuations in Turkey, particularly since 2018. Another key finding is the substantial role of exchange rate developments in determining house prices. The depreciation of the national currency influences house prices through both demand and supply channels. The results are robust across various variables, specifications, and priors. 

The findings of this study underscore the distinctive characteristics of Turkey’s housing market, which set it apart from other emerging economies. First and foremost, the sensitivity of housing prices to exchange rate fluctuations underscores the distinctive role of currency depreciation in affecting construction costs and speculative demand in Turkey. Second, the post-crisis dominance of sentiment and credit conditions as key drivers of house prices in Turkey’s housing market reflects the interplay between macroeconomic instability and consumer behavior. These findings not only deepen our comprehension of Turkey’s housing market but also enrich the broader literature by presenting a case study of an emerging market where external shocks, speculative activity, and policy interventions significantly influence housing price dynamics. 

These findings have substantial policy implications and suggest a comprehensive strategy for stabilizing housing prices in Turkey. The notable contribution of housing supply to the FEVD results suggests that economic policies should prioritize increasing housing supply to stabilize housing prices over the long period. In addition, policymakers should also focus on supply side factors, taking into account the impact of exchange rate-induced increases in construction costs. To address supply side constraints, policymakers should contemplate the implementation of tax incentives for developers and the streamlining of permitting processes to reduce construction delays. The role of the central bank and regulatory institutions is also critical, as monetary policy, credit conditions, and 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 18 of 24 

Economic Change and Restructuring (2025) 58:8 

exchange rates significantly influence house price fluctuations. This task is particularly challenging in light of the CBRT price and financial stability objectives. In the near term, macroprudential measures targeting credit conditions, such as more stringent loan-to-value (LTV) ratios and augmented risk-weighting for housing loans, can assist in curbing excessive price growth driven by credit supply shocks. Specifically, when shifts in consumer expectations serve as the primary determinant of price changes, reliance solely on credit regulation may be insufficient. Instead, targeted interventions addressing both market sentiment and broader economic conditions are necessary to ensure sustainable price stability. 

In contrast to the general trend of declining homeownership rates in Turkey in recent years, the significant increase in house prices demonstrates the pivotal influence of speculative and sentiment-driven shocks on the dynamics of the housing market. Given the significant role of speculative demand embodied in housing sentiments in recent house price increases, measures to temper expectations about future house prices are also necessary. In the medium to long term, policies designed to temper speculative demand—such as capital gains taxes on short-term transactions and financial literacy programs—have the potential to mitigate the influence of sentiment-driven price increases. Finally, transparent monetary policy communication and fiscal discipline will stabilize the broader economic landscape, reducing speculative behavior and exchange rate-driven supply shocks. 

This study analyzes factors driving house price fluctuations in Turkey. However, several avenues for future research remain open. Future research could explore regional variations in housing market behavior using spatial econometric methods, comparative studies with other emerging economies for a global perspective, and econometric techniques like Markov Switching SVAR or TimeVarying Parameter SVAR to capture structural parameter changes. Incorporating micro-level data and exploring the interplay between housing markets and environmental factors could also provide additional insights for policymakers. 

### **Appendix A** 

#### **Summary statistics** 

See Table 3. 

**Table 3** Summary statistics 

||N|Std. Dev|Minimum|Maximum|Mean|
|---|---|---|---|---|---|
|hpi|156|253.124|48.300|1163.3|191.524|
|Permits<br>|156|17,024.171|27,576.000|121,630|57,299.378|
|Confdence|156|7.84|63.360|97.969|86.222|
|Mortgage rate|156|6.322|8.297|42.15|15.329|
|Housing loan|156|92,171,386|58,515,732.00|4.044e + 08|1.767e + 08|
|Exchange rate|156|6.717|1.823|30.395|6.839|



Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 19 of 24 **8** 

#### **Preliminary analysis** 

#### See Table 4. 

**Table 4** Unit Root Test Results 

|Variable|Intercept||Intercept and tre|nd|
|---|---|---|---|---|
||Level|First diference|Level|First diference|
|ADF unit root test|||||
|_lrhpi_cpi_|−0.397|−3.09**|−1.318|−3.249*|
|_mrate_|0.021|−4.985***|−1.302|−5.182***|
|_lpermit_|−3.966***|−8.054***|−4.020***|−7.999***|
|_lconfdence_|−1.486|−6.453***|−2.983|−6.425***|
|_lhloan_|−0.253|−4.779***|−2.559|−4.767***|
|_lreer_|−0.529|−7.465***|−2.789|−7.466***|
|Phillips–Perron (PP)|unit root test||||
|_lrhpi_cpi_|1.554|−7.976***|−0.112|−8.375***|
|_mrate_|−0.061|−7.104***|−1.250|−7.167***|
|_lpermit_|−7.288***|−20.717***|−7.279***|−20.640***|
|_lconfdence_|−2.092|−12.845***|−3.997|−12.793***|
|_lhloan_|−0.495|−5.507***|−2.212|−5.491***|
|_lreer_|−0.881|−8.973***|−3.249*|−8.940***|



***, ** and * present the significance at 1%, 5%, and 10% levels, respectively. In both tests, the null hypothesis is that the series has a unit root and the optimal lag lengths are determined according to the Schwarz information criterion 

### **Robustness checks** 

See Table 5, Figs. 4, 5, 6 and 7 

**Table 5** FEVD of the real house price fluctuations for robustness specifications 

|Period|Housing supply|Housing demand|interest rate|Credit|Sentiment|Exchange rate|
|---|---|---|---|---|---|---|
|Months|FEVD over entire|sample|||||
|1–5|29.86|13.93|16.46|11.23|9.18|19.29|
|6–10|25.97|14.16|24.92|7.55|8.49|18.86|
|11–15|22.45|14.07|28.38|7.99|9.59|17.48|
|16–20|20.26|14.40|29.55|8.38|11.14|16.20|
|21–25|19.44|15.01|28.74|8.58|12.32|15.86|
|36|17.97|14.4|26.11|8.92|16.3|16.26|
|48|17.74|13.26|22.02|8.36|21.96|16.63|



Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 20 of 24 

Economic Change and Restructuring (2025) 58:8 



**Fig. 4** Impulse response functions of shocks to variables for robustness specifications. _Note_ : IRF findings of the model containing NHPI, short-term interest rate, economic confidence index, nominal exchange rate, permits and credit 



<!-- Start of picture text -->
0.25<br>0.2<br>0.15<br>0.1<br>0.05<br>0<br>-0.05<br>-0.1<br>-0.15<br>-0.2<br>-0.25<br>2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023<br>Housing Demand Shock Housing Supply Shock Monetary Policy Shock Credit Shock Sentiment Shock Exchange Rate Shock<br><!-- End of picture text -->

**Fig. 5** Historical decomposition of changes in real house prices for robustness specification 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 21 of 24 **8** 



**Fig. 6** Impulse response functions with Minnesota Priors 



**Fig. 7** Impulse response functions with Minnesota Priors 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 22 of 24 

Economic Change and Restructuring (2025) 58:8 

#### **Declarations** 

**Conflict of interests** The authors did not receive support from any organization for the submitted work. The authors have no relevant financial or non-financial interests to disclose. 

### **References** 

Afşar M, Yüksel GÖ (2022) Effectiveness of the housing channel in monetary policy. Eskişehir Osmangazi Univ J Econ Admin Sci 17(2):345–367 

Akça T (2023) House price dynamics and relations with the macroeconomic indicators in Turkey. Int J Hous Mark Anal 16(4):812–827 

Akçay SB, Akyüz M (2024) Why did house prices go up during COVID-19 pandemic? Policy-driven or market-driven? Int Real Estate Rev 27(2):303–328 

Akçay SB, Karul C, Akyuz M (2023) Mortgage credit and house prices: the Turkish case. Int J Hous Mark Anal 16(2):318–335 

Akgündüz YE, Dursun-de Neef HÖ, Hacihasanoğlu YS, Yılmaz F (2023) Cost of credit, mortgage demand and house prices. J Bank Finance 154:106953 

Akkaya M (2024) House price bubble and analysis of the factors affecting house price: Turkey case. Gazi J Econ Bus 10(1):33–45 Akpolat AG (2024) The asymmetric effects of real variables on real housing prices: a nonlinear ARDL analysis for Turkey. Int J Hous Mark Anal 17(3):565–590 

Anastasiou D, Kapopoulos P, Zekente KM (2023) Sentimental shocks and house prices. J Real Estate Finance Econ 67(4):627–655 

Asal M (2018) Long-run drivers and short-term dynamics of Swedish real house prices. Int J Hous Mark Anal 11(1):45–72 

Balcılar M, Usman O, Yülek M, Ağan B, Erdal B (2024) House price connectedness and consumer sentiment in an era of destabilizing macroeconomic conditions: empirical evidence from Türkiye. Borsa Istanbul Rev 24(1):14–34 

Bjørnland HC, Jacobsen DH (2010) The role of house prices in the monetary policy transmission mechanism in small open economies. J Financ Stab 6(4):218–229 

Canöz İ, Kalkavan H (2024) Forecasting the dynamics of the Istanbul real estate market with the Bayesian time-varying VAR model regarding housing affordability. Habitat Int 148:103055 

Chen SS, Lin TY, Wang JK (2024) Monetary policy and housing market cycles. Macroecon Dyn 1–33 

Deniz A, Çetinkaya SC (2024) Intermediaries of citizenship by investment and Türkiye: ‘global citizenship market grow with us’. Globalizations 1–21 

Ghaedrahmati S, Rezaei E (2024) Turkey, the second home for Iranians: push and pull motivations in the Turkish housing market. J Eur Real Estate Res 17(1):123–136. https:// doi. org/ 10. 1108/ JERER- 06- 2023- 0019 

Hanck C, Prüser J (2020) House prices and interest rates: Bayesian evidence from Germany. Appl Econ 52(28):3073–3089 

Iacoviello M, Minetti R (2008) The credit channel of monetary policy: evidence from the housing market. J Macroecon 30(1):69–96 

Karakoyun HD, Yıldırım N (2017) Demand-side factors of housing price increases in Turkey: BlanchardQuah SVAR model. Bus Econ Horizons 13(3):312–332 Kırca M, Canbay Ş (2022) Determinants of housing inflation in Turkey: a conditional frequency domain causality. Int J Hous Mark Anal 15(2):478–499 

Kishor NK (2023) Forecasting house prices: the role of fundamentals, credit conditions, and supply indicators. J Real Estate Finance Econ 1–23. 

Knight F (2022) Global house price index, research. Q3 https:// conte nt. knigh tfrank. com/ resea rch/ 84/ docum ents/ en/ global- house- price- index- q3- 2022- 9618. pdf 

Lambertini L, Mendicino C, Punzi MT (2017) Expectations-driven cycles in the housing market. Econ Model 60:297–312 

Lee J, Ann J, Park C (2022) What causes house prices to fluctuate? Evidence from South Korea. Asian Econ J 36(4):365–384 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

Economic Change and Restructuring (2025) 58:8 

Page 23 of 24 **8** 

Lee J (2023) What factors drive house prices in the USA? Sign restricted VAR approach. Empir Econ 1–24 

- Ma X, Zhang Z (2022) Expectations, credit conditions, and housing boom-bust: Evidence from SVAR with sign and zero restrictions. J Bank Finance 134:106330 

- Melecky A, Paksi D (2024) Drivers of European housing prices in the new millennium: demand, financial, and supply determinants. Empirica 1–23 

Mian A,  Sufi A (2011) House prices, home equity–based borrowing, and the us household leverage crisis. Am Econ Rev 101(5):2132–2156 Nsafoah D, Dery C (2024) Effect of conventional and unconventional monetary policy shocks on housing prices in Canada. J Hous Econ 64:101993 

- Öhman P, Yazdanfar D (2018) Organizational-level profitability determinants in commercial banks: Swedish evidence. J Econ Stud 45(6):1175–1191 

Organization for Economic Co-operation and Development (OECD), (2024) Data Explorer, National Accounts, Received; 7 July, 2024. https:// data- explo rer. oecd. org 

- Ovalı M, Çayırlı Ö (2023) Inflation and exchange rate uncertainties and housing prices: the case of Turkey. Izmir Journal of Economics 38(2):550–569 

- Özgüler İC, Büyükkara ZG, Küçüközmen CC (2023) Discovering the fundamentals of the Turkish housing market: a price convergence framework. Int J Hous Mark Anal 16(1):116–145 

- Robstad Ø (2018) House prices, credit and the effect of monetary policy in Norway: evidence from structural VAR models. Empir Econ 54(2):461–483 

- Rosenberg S (2019) The effects of conventional and unconventional monetary policy on house prices in the Scandinavian countries. J Hous Econ 46:101659 

- Rosenberg S (2020) Conventional and unconventional monetary policies: effects on the Finnish housing market. Baltic J Econ 20(2):170–186 

- Salami MA, Tanrivermis H, Aliefendioğlu Y (2023) Interdependence between foreigner housing acquisitions and housing price increase in Turkey during the COVID-19 pandemic era. Int J Hous Mark Anal 16(3):575–597 

- Şeyranlıoğlu O (2023) The relationship between housing prices and macroeconomic and financial indicators: bootstrap causality test. Nevşehir Hacı Bektaş Veli Üniversitesi SBE Dergisi 13(3):1713–1732 

- Siklar I (2024) The role of speculative demand in housing price changes in Turkey. Bus Econ Res 14(2):34–60 

- Sims CA, Stock JH, Watson MW (1990) Inference in linear time series models with some unit roots. Econometrica: J Econ Soc 58(1):113–144 

- Towbin P, Weber MS (2015) Price expectations and the US housing boom. IMF working papers, vol. 2015, issue 182, Int Mon Fund (available at https:// www. elibr ary. imf. org/ view/ journ als/ 001/ 2015/ 182/ 001. 2015. issue- 182- en.xml) 

- Tunc C (2020) The effect of credit supply on house prices: Evidence from Turkey. Hous Policy Debate 30(2):228–242 

- Uğur A, Tosun N (2021) Analysis of THE relationship housing price index and investor sentiment: an empirical evidence on Turkey. J Int Trade Econ Res 5(1):10–21 

- Usta A (2021) The role of sentiment in housing market with credit-led funding: the case of Turkey. J Hous Built Environ 36(2):577–600 

- Varlık N (2020) Asymmetric effect of economic growth on housing prices: NARDL application. Hitit J Soc Sci 13(2):352–367 

- Vergili G (2023) Bubble analysis in real housing prices: application across Türkiye, Istanbul, Ankara, and Izmir. J Appl Sci Mehmet Akif Ersoy Univ 7(1):44–66 

- Wadud IM, Bashar OH, Ahmed HJA (2012) Monetary policy and the housing market in Australia. J Policy Model 34(6):849–863 

- Yıldırım MO (2023) Housing affordability in Turkey: How big is it and who are the most vulnerable? In: Göçoğlu Volkan, Karkin Naci (eds) Citizen-centered public policy making in Turkey. Springer International Publishing, Switzerland AG 

- Yıldırım MO, İvrendi M (2017) House prices and the macroeconomic environment in Turkey: the examination of a dynamic relationship. Econ Ann 62(215):81–110 

- Yıldırım MO, İvrendi M (2021) Turkish housing market dynamics: an estimated DSGE model. Margin: J Appl Econ Res 15(2):238–267 

- Yıldırım MO, Yağcıbaşı ÖF (2019) The dynamics of house prices and fiscal policy shocks in Turkey. Econ Ann 64(220):39–59 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

**8** Page 24 of 24 

Economic Change and Restructuring (2025) 58:8 

**Publisher’s Note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. 

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law. 

Content courtesy of Springer Nature, terms of use apply. Rights reserved. 

## Terms and Conditions 

Springer Nature journal content, brought to you courtesy of Springer Nature Customer Service Center GmbH (“Springer Nature”). 

Springer Nature supports a reasonable amount of sharing of  research papers by authors, subscribers and authorised users (“Users”), for small-scale personal, non-commercial use provided that all copyright, trade and service marks and other proprietary notices are maintained. By accessing, sharing, receiving or otherwise using the Springer Nature journal content you agree to these terms of use (“Terms”). For these purposes, Springer Nature considers academic use (by researchers and students) to be non-commercial. 

These Terms are supplementary and will apply in addition to any applicable website terms and conditions, a relevant site licence or a personal subscription. These Terms will prevail over any conflict or ambiguity with regards to the relevant terms, a site licence or a personal subscription (to the extent of the conflict or ambiguity only). For Creative Commons-licensed articles, the terms of the Creative Commons license used will apply. 

We collect and use personal data to provide access to the Springer Nature journal content. We may also use these personal data internally within ResearchGate and Springer Nature and as agreed share it, in an anonymised way, for purposes of tracking, analysis and reporting. We will not otherwise disclose your personal data outside the ResearchGate or the Springer Nature group of companies unless we have your permission as detailed in the Privacy Policy. 

While Users may use the Springer Nature journal content for small scale, personal non-commercial use, it is important to note that Users may not: 

1. use such content for the purpose of providing other users with access on a regular or large scale basis or as a means to circumvent access control; 

2. use such content where to do so would be considered a criminal or statutory offence in any jurisdiction, or gives rise to civil liability, or is otherwise unlawful; 

3. falsely or misleadingly imply or suggest endorsement, approval , sponsorship, or association unless explicitly agreed to by Springer Nature in writing; 

4. use bots or other automated methods to access the content or redirect messages 5. override any security feature or exclusionary protocol; or 

6. share the content in order to create substitute for Springer Nature products or services or a systematic database of Springer Nature journal content. 

In line with the restriction against commercial use, Springer Nature does not permit the creation of a product or service that creates revenue, royalties, rent or income from our content or its inclusion as part of a paid for service or for other commercial gain. Springer Nature journal content cannot be used for inter-library loans and librarians may not upload Springer Nature journal content on a large scale into their, or any other, institutional repository. 

These terms of use are reviewed regularly and may be amended at any time. Springer Nature is not obligated to publish any information or content on this website and may remove it or features or functionality at our sole discretion, at any time with or without notice. Springer Nature may revoke this licence to you at any time and remove access to any copies of the Springer Nature journal content which have been saved. 

To the fullest extent permitted by law, Springer Nature makes no warranties, representations or guarantees to Users, either express or implied with respect to the Springer nature journal content and all parties disclaim and waive any implied warranties or warranties imposed by law, including merchantability or fitness for any particular purpose. 

Please note that these rights do not automatically extend to content, data or other material published by Springer Nature that may be licensed from third parties. 

If you would like to use or distribute our Springer Nature journal content to a wider audience or on a regular basis or in any other manner not expressly permitted by these Terms, please contact Springer Nature at 

<u>onlineservice@springernature.com</u> 

