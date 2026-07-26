---
title: The housing supply channel of monetary policy
type: paper
source_pdf: raw/papers/Albuquerque_The house supply channel of the monetary policy_2024.pdf
converted: 2026-07-26
---

Working Paper Series  | 59 |  2024 



<!-- Start of picture text -->
Bruno Albuquerque<br><!-- End of picture text -->

Bruno Albuquerque International Monetary Fund, Univ. of Coimbra, CeBER 

Martin Iseringhausen European Stability Mechanism 

Frederic Opitz European Commission, Ghent University 

###### Disclaimer 

This working paper should not be reported as representing the views of the ESM. The views expressed in this Working Paper are those of the authors and do not necessarily represent those of the ESM or ESM policy. 



Working Paper Series  |  59  |  2024 

# The housing supply channel of monetary policy 

Bruno Albuquerque<sup>1</sup> International Monetary Fund, Univ. of Coimbra, CeBER Martin Iseringhausen<sup>2</sup> European Stability Mechanism Frederic Opitz<sup>3</sup> European Commission, Ghent University 

### Abstract 

We study the role of regional housing markets in the transmission of US monetary policy. Using a FAVAR model over 1999q1–2019q4, we find sizeable heterogeneity in the responses of US states to a contractionary monetary policy shock. Part of this regional variation is due to differences in housing supply elasticities, household debt overhang, and housing wealth (volatility). Our analysis indicates that house prices and consumption respond more in supply-inelastic states and in states with large household debt imbalances, where negative housing wealth effects bite more strongly and borrowing constraints become more binding. Moreover, financial stability risks increase sharply in these areas as mortgage delinquencies and foreclosures surge, worsening banks’ balance sheets. Finally, monetary policy may have a stronger effect on housing tenure decisions in supply-inelastic states, where the homeownership rate and price-to-rent ratios decline by more. Our findings stress the importance of regional housing supply conditions in assessing the macrofinancial effects of rising interest rates. 

**Keywords:** Credit conditions, FAVAR, house prices, monetary policy, regional data, supply elasticities 

###### **JEL codes:** C23, E32, E52, R31 

> 1 balbuquerque@imf.org 

> 2 m.iseringhausen@esm.europa.eu 

> 3 frederic.opitz@ec.europa.eu 

##### Disclaimer 

This Working Paper should not be reported as representing the views of the ESM. The views expressed in this Working Paper are those of the authors and do not necessarily represent those of the ESM or ESM policy. No responsibility or liability is accepted by the ESM in relation to the accuracy or completeness of the information, including any data sets, presented in this Working Paper. 

> **© European Stability Mechanism, 2024** All rights reserved. Any reproduction, publication and reprint in the form of a different publication, whether printed or produced electronically, in whole or in part, is permitted only with the explicit written authorisation of the European Stability Mechanism. 

ISSN 2443-5503 

## **The housing supply channel of monetary policy**<sup>*</sup> 

Bruno Albuquerque<sup>†</sup> _International Monetary Fund Univ. of Coimbra, CeBER_ 

Martin Iseringhausen<sup>‡</sup> Frederic Opitz<sup>§</sup> _European Stability Mechanism European Commission Ghent University_ 

January 20, 2024 

###### **Abstract** 

We study the role of regional housing markets in the transmission of US monetary policy. Using a FAVAR model over 1999q1–2019q4, we find sizeable heterogeneity in the responses of US states to a contractionary monetary policy shock. Part of this regional variation is due to differences in housing supply elasticities, household debt overhang, and housing wealth (volatility). Our analysis indicates that house prices and consumption respond more in supply-inelastic states and in states with large household debt imbalances, where negative housing wealth effects bite more strongly and borrowing constraints become more binding. Moreover, financial stability risks increase sharply in these areas as mortgage delinquencies and foreclosures surge, worsening banks’ balance sheets. Finally, monetary policy may have a stronger effect on housing tenure decisions in supply-inelastic states, where the homeownership rate and price-to-rent ratios decline by more. Our findings stress the importance of regional housing supply conditions in assessing the macrofinancial effects of rising interest rates. 

**Keywords:** Credit conditions, FAVAR, house prices, monetary policy, regional data, supply elasticities **JEL classification:** C23, E32, E52, R31 

> *The views expressed in this paper represent only our own and should therefore not be reported as representing the views of the International Monetary Fund, its Executive Board, IMF management, the European Stability Mechanism, or the European Commission. We would like to thank Katharina Bergant (discussant), Nina Biljanovska, Romain Bouis, Eugenio Cerutti, Selien De Schryder, Daniel A. Dias, Jo˜ao B. Duarte, Freddy Heylen, Deniz Igan (discussant), Antonio Garcia Pascual, Gert Peersman, Sebastian K. R¨uth, Frank Smets, Konstantinos Theodoridis, Isabel Vansteenkiste, the participants at the Central Bank of Ireland conference ‘Financial stability policies in a changing lending landscape’, the 9<sup>_th_</sup> Ghent University Workshop on Empirical Macroeconomics, and seminar participants at the BIS, ESM, IMF, and Ghent University for helpful comments and suggestions. Frederic Opitz gratefully acknowledges financial support from Ghent University’s Special Research Fund (BOF). 

> †balbuquerque@imf.org. Address: 709 19th Street NW, Washington, D.C. 20431, United States. 

> ‡m.iseringhausen@esm.europa.eu. Address: 6a Circuit de la Foire Internationale, L-1347, Luxembourg. 

> §frederic.opitz@ec.europa.eu. Address: Rue de la Loi 200, B-1040 Brussels, Belgium. 

#### **1 Introduction** 

Housing plays a central role for macroeconomic fluctuations: two-thirds of US households own a home, housing consumption accounts for around one third of total private consumption expenditures,<sup>1</sup> and the marginal propensity to consume (MPC) out of housing wealth is much larger than the one out of financial wealth (Carroll et al. 2011). Mortgagors also display a higher MPC than renters or outright owners (Cloyne et al. 2020). In addition, housing is highly sensitive to interest rate changes (Iacoviello 2005, Hedlund et al. 2016, Bhutta and Ringo 2021), but with considerable regional variation due to differences in housing market attributes (Ferreira and Gyourko 2012, Piazzesi and Schneider 2016). In particular, differences in housing supply elasticities—how supply responds to demand-driven house price changes—imply that house prices in inelastic areas are more responsive to expansionary monetary policy shocks as builders face tighter geographical and regulatory constraints to expand supply (Fischer et al. 2021, Aastveit and Anundsen 2022, Cooper et al. 2022, Aastveit et al. 2023).<sup>2</sup> There is also recent evidence that the responsiveness of house prices to monetary policy may have increased over time in light of declining supply elasticities (Herkenhoff et al. 2018, Albuquerque et al. 2020, Aastveit et al. 2023). This underscores the prominent role of housing supply in the transmission of monetary policy, which remains understudied.<sup>3</sup> 

The literature referred to above has made the case for a link between _expansionary_ monetary policy shocks and a stronger responsiveness of house prices in supply-constrained areas. While modelling the asymmetric effects of monetary policy—conditional on housing supply constraints—is beyond the scope of our analysis, we argue throughout the paper that the house price reaction to _contractionary_ demand shocks is also not independent of supply restrictions in the presence of financial-accelerator effects. Let us illustrate this point. Figure 1 shows that California—an area with inelastic housing supply—has experienced more pronounced boom-bust housing cycles in the last two decades, which contrasts with Oklahoma—an area with elastic housing supply. House prices in California increased substantially in the run-up to the Global Financial Crisis (GFC), which coincided with a large increase in mortgage debt, followed by a stronger bust as the credit crunch started to bite more strongly in these 

> 1According to the 2021 US Census survey, and to the 2021 Consumer Expenditures Survey from the BLS. 

> 2Other structural features of the housing market, such as the share of adjustable-rate mortgages (ARM) and the homeownership rate, also play a role in explaining the regional effects of monetary policy on house prices (Calza et al. 2013, Corsetti et al. 2022, Pica 2023). 

> 3 The literature has focused mostly on how monetary policy influences housing demand. First, an expansionary monetary policy stimulates borrowing and consumption through the credit-supply channel, whereby lower borrowing costs and higher inflation reduce the real value of debt (Jord`a et al. 2015, Bhutta and Ringo 2021, Wong 2021). Second, the household balance sheet channel, or home equity loan/collateral channel, posits that monetary policy has important housing wealth effects that encourage existing mortgagors to extract equity to finance consumption expenditures and investment (Iacoviello 2005, Del Negro and Otrok 2007, Jaroci´nski and Smets 2008, Bhutta and Keys 2016, Aladangady 2017, Beraja et al. 2019, Cloyne et al. 2020, Garriga and Hedlund 2020, Andersen and Leth-Petersen 2021). Third, changes in mortgage-related costs may affect demand for real estate services, thereby affecting economic activity (Best and Kleven 2018, Bhutta and Ringo 2021, Anenberg and Ringo 2022, Benmelech et al. 2023). 

1 

areas (Huang and Tang 2012, Anundsen and Heebøll 2016, Chodorow-Reich et al. 2024). This translated into a large increase in the foreclosure rate, amplifying the initial contraction in house prices (Figure 1). 

Understanding the role of housing supply constraints in the transmission of negative demand shocks to the housing market is particularly important in an environment of rapidly rising interest rates. For instance, we conjecture that higher interest rates may lead to a stronger fall in house prices in inelastic areas, followed by larger consumption cuts, and reduced economic activity more generally. The fall in mortgagors’ housing equity may also raise financial stability risks in these low-supply elasticity areas due to the surge in mortgage delinquencies and foreclosures. 

Figure 1: Real house prices and foreclosure rate in California and Oklahoma 

















**Note:** Real house prices and the foreclosure rate are re-scaled to an index equal to 100 in 2000q1. 

Against this background, we explore the regional heterogeneity in the transmission of (contractionary) monetary policy to the real economy through differences in US state-level housing markets, focusing primarily on housing supply elasticities—which we call the _housing supply channel of monetary policy_ . Our main contribution is threefold. First, we trace out the impact of monetary policy not only on regional house prices—as investigated in the related literature (Fratantoni and Schuh 2003, Fischer et al. 2021, Aastveit and Anundsen 2022, Cooper et al. 2022, Aastveit et al. 2023)—but also on the real economy and on financial variables. Second, we place the focus on differences in housing supply constraints across states for the transmission of (contractionary) monetary policy shocks. This allows us to assess the regional macrofinancial impact of monetary policy shocks conditional on differences in the supply side of housing. Third, we include a rich set of housing market variables, covering both the owner-occupied segment and the rental market. In contrast to most of the existing literature, this allows us to study how monetary policy may affect households’ housing tenure decisions, which may amplify or dampen the effects of monetary policy (Dias and Duarte 2019, 2022, Koeniger et al. 2022). 

We estimate a factor-augmented VAR (FAVAR) model (Bernanke et al. 2005), using a large quarterly dataset for the 50 US states over 1999q1–2019q4. The model summarizes the dynamic relationships 

2 

within the economy and includes several state-level (and US aggregate) variables on the real economy, labor market, financial sector, public finances, and the housing market. The housing market block encompasses rich information on both prices and quantities, namely house prices and rental prices, building permits and housing starts, as well as homeownership rates and vacancy rates, both for homes for sale and for rent. Our measure of monetary policy shocks follows the state-of-the-art high-frequency identification of unexpected changes in the Fed policy rate around FOMC announcements (G¨urkaynak et al. 2005, Gertler and Karadi 2015, Nakamura and Steinsson 2018). We then rely on the exogenous variable approach of Paul (2020) to identify the effects of monetary policy shocks in the FAVAR model. 

Our main findings are as follows. First, we find significant heterogeneity in the transmission of an aggregate US contractionary monetary policy shock to the US states. The heterogeneity is particularly large among housing market variables, supporting recent findings in the literature (Fischer et al. 2021, Aastveit and Anundsen 2022, Cooper et al. 2022, Corsetti et al. 2022, Koeniger et al. 2022, Aastveit et al. 2023). Moreover, as homeownership costs increase due to the tightening of monetary policy, we find that house prices fall while rent prices increase in most states, suggesting a reallocation of demand from the owner-occupied market to the rental market (Dias and Duarte 2019, 2022). In this regard, our contribution is to show that monetary policy may have a differential effect on households’ housing tenure decisions across states. For instance, the fall in the house price-to-rent ratio varies widely across states, and the homeownership rate remains unchanged or declines only marginally in some states, while falling more markedly in others. The response of housing supply may help explain the differences across states in the shift from the owner-occupied to the rental market: home vacancy rates decline and rental vacancy rates increase in some states, which contrasts with the US aggregate evidence. 

Second, we find that differences in housing supply restrictions, or in supply elasticities, across states can help explain the heterogeneity in the responses to monetary policy. We use the state-level landuse restriction index (LRI) of Herkenhoff et al. (2018) as our baseline measure of housing supply constraints. Specifically, exploring the cross-sectional distribution of this indicator allows us to compare the responses to monetary policy between high- and low-regulated states. We find that house prices are more responsive in areas where housing supply is more constrained, in line with recent evidence (Gyourko et al. 2008, Saiz 2010, Glaeser et al. 2014, Herkenhoff et al. 2018, Aastveit and Anundsen 2022, Cooper et al. 2022, Aastveit et al. 2023). Our contribution here is to show that tighter housing supply constraints, which imply lower supply elasticities, not only impact the house price response to monetary policy, but also have broader macrofinancial implications. In particular, our results show that states with more inelastic housing supply experience a stronger fall in economic activity following a contractionary monetary policy shock. We rationalize this result with a larger decline in housing wealth for households in these areas, which induces a greater fall in private consumption. In addition, we find that financial stability risks increase more sharply in low-supply elasticity areas as mortgage delinquencies 

3 

and foreclosures increase more strongly, and other indicators proxying the health of the banking sector deteriorate more considerably. 

Third, household debt overhang also matters for explaining the heterogeneous effects of monetary policy. We find evidence that housing markets, economic activity and financial variables are more sensitive to contractionary monetary policy shocks in states with higher household debt imbalances, as measured by the so-called _debt gap_ (Albuquerque 2019, Alpanda and Zubairy 2019). This underlines the role that debt overhang can have in amplifying business cycles (Schularick and Taylor 2012, Jord`a et al. 2013, 2015, 2022, Dell’Ariccia et al. 2016, Mian et al. 2017, Albuquerque and Krustev 2018, Albuquerque 2019, Greenwood et al. 2022). States with larger household debt gaps tend to be those with lower housing supply elasticities, which may explain why our results depart from the conventional view that the response of house prices to contractionary demand shocks is independent of supply restrictions (Glaeser and Gyourko 2005, Glaeser et al. 2008, Aastveit and Anundsen 2022). We argue that areas experiencing stronger credit booms during economic expansions and credit busts during downturns typically tend to fall in places with low-supply elasticities. This makes house prices more sensitive to changes in housing demand, both increases and decreases. This is in line with a recent strand of research showing that more inelastic US areas experienced a stronger housing boom in the run-up to the GFC, followed by a stronger bust as the contraction in credit amplified the initial fall in house prices in these areas (Huang and Tang 2012, Anundsen and Heebøll 2016, Chodorow-Reich et al. 2024). In particular, recent studies have stressed the role of financial-accelerator effects (Huang and Tang 2012, Anundsen and Heebøll 2016), households’ overoptimism during housing booms (Chodorow-Reich et al. 2024), and a price-foreclosure spiral during housing busts (Guren and McQuade 2020, Chodorow-Reich et al. 2024) to explain why supply-inelastic areas had more pronounced housing cycles. Overall, our findings emphasize the interaction between household debt overhang and housing supply constraints in amplifying the macrofinancial effects of contractionary monetary policy. All this evidence is consistent with our view that house prices may not be independent of the housing supply elasticity in the presence of negative demand shocks when financial-accelerator effects and misaligned household expectations are at play. 

Fourth, differences in housing wealth across states—both in terms of level and volatility—could explain the heterogeneity in the transmission of monetary policy to the housing market. While the role of housing wealth and the ability of mortgagors to extract home equity to finance consumption has been well documented (see the household balance sheet channel in Bhutta and Keys 2016, Aladangady 2017, Beraja et al. 2019, Andersen and Leth-Petersen 2021), we know less about the role of housing wealth volatility. Presumably, as housing wealth volatility increases, households may reduce their demand for real estate services such as realtors, loan officers, and mortgage brokers, leading to an overall reduction in economic activity (Best and Kleven 2018, Bhutta and Ringo 2021, Anenberg and Ringo 2022, 

4 

Benmelech et al. 2023). Relatedly, uncertainty about the future evolution of house prices can affect the tenure choice of households (Henderson and Ioannides 1983, Rosen et al. 1984, Fu 1995). We find that the differential response of states to monetary policy shocks can be, to some extent, accounted for by differences in housing wealth (volatility). 

Finally, we find that monetary policy may have a stronger influence on housing tenure decisions in low-supply elasticity areas. Differences in market segmentation across states, i.e. the adjustment costs of converting owner-occupied housing to rental units, may help explain this finding (Greenwald and Guren 2021). The larger fall in house prices in inelastic states is accompanied by a larger decline in the homeownership rate. At the same time, the rental vacancy rate remains relatively unchanged in more inelastic states, and rent prices increase by less relative to more elastic areas. We interpret this as evidence that the rental market has more capacity, and probably faces lower adjustment costs in absorbing rising demand for rental units as homeownership costs increase. We speculate that more stringent regulation to build new housing units in some areas, which are typically associated with greater house price volatility, may indirectly create incentives for homeowners or investors to lower adjustment costs of converting owner-occupied units to rental units when negative housing demand shocks hit. An alternative explanation for the weaker response of rent prices in inelastic areas may be related to a level-effect, as rent prices are typically higher in these areas. This may limit the scope for further rent price increases when housing demand falls. 

Our main result—states with more inelastic housing supply are hit harder by contractionary monetary policy shocks—does neither imply that housing supply constraints are the sole determinant of such heterogeneity, nor does it necessarily posit a causal relationship. We acknowledge that other characteristics, such as state-level differences in the industry composition, demography, income levels, and in the quality of institutions, may also explain regional heterogeneity in the responses to monetary policy. While it is arguably challenging to establish causality, we run cross-sectional regressions that control for several state-specific characteristics that may explain the regional heterogeneity in the responses to monetary policy. We find that also in this setting housing supply restrictions remain highly relevant to account for this heterogeneity. 

Our main findings remain robust along several dimensions, including: i) using alternative monetary policy (forward guidance) surprises that have a stronger effect on the long end of the yield curve (Swanson 2021); ii) controlling for central bank information effects in monetary policy (Jaroci´nski and Karadi 2020); (iii) considering alternative measures of state-specific housing supply restrictions (Saiz 2010, Aastveit et al. 2023); and iv) using an alternative measure of state-level inflation (Hazell et al. 2022). 

Our paper is related to a growing literature on the role of housing supply constraints for the trans- 

5 

mission of demand shocks—such as monetary policy shocks—to housing markets (Gyourko et al. 2008, Saiz 2010, Glaeser et al. 2014, Herkenhoff et al. 2018, Albuquerque et al. 2020, Fischer et al. 2021, Cooper et al. 2022, Aastveit and Anundsen 2022, Aastveit et al. 2023). We add to this literature by tracing out the differential macrofinancial effects of monetary policy on US states, which go beyond only analysing the dynamics of house prices. Our paper also relates to recent research on the monetary policy effects on households’ housing tenure decisions, particularly that contractionary monetary policy may disadvantage renters and mortgagors (Dias and Duarte 2019, 2022, Koeniger et al. 2022). Our contribution is to document empirically that monetary policy may influence housing tenure decisions heterogeneously across states, conditional on differences in supply constraints, housing market segmentation, and household debt imbalances. Finally, our paper can be placed in the literature documenting regional and cross-country differences in the responses of macroeconomic variables to monetary policy (Carlino and DeFina 1998, 1999, Fratantoni and Schuh 2003, Francis et al. 2012, Calza et al. 2013, Albuquerque 2019, Fischer et al. 2021, Corsetti et al. 2022, Aastveit and Anundsen 2022, Aastveit et al. 2023, Pica 2023). 

#### **2 Data** 

We use state-level data to explore the regional heterogeneity in the US economy. Although we would prefer to use more granular data, such as metropolitan statistical areas (MSA) or city-level data, in this case data availability issues on a set of economic and financial indicators become more severe. US states are characterized by significant variation across key macroeconomic variables (Figure B.1 in Appendix B). In particular, the heterogeneity in the dynamics of housing market variables is consistent with the notion that housing markets are local and exhibit their own cyclical movements, possibly decoupled from the national cycle (Ghent and Owyang 2010, Ferreira and Gyourko 2012, Hern´andez-Murillo et al. 2017). We also note the substantial variation over time in house prices relative to rents, indicating that house prices may not move in line with rents over the long term—the no-arbitrage condition—as predicted by theory (Poterba 1984).<sup>4</sup> 

For the FAVAR analysis, we use a quarterly dataset of 26 state-specific series for 50 US states over 1999q1–2019q4. We complement the dataset with 47 aggregate national variables, including standard macroeconomic, financial, and housing market variables, to control for the state of the US business cycle, for a total of over 1,200 time series. When extracting the factors, we exclude those US variables 

> 4Standard theory predicts that the price of a house should be determined by the present value of cumulated future rents. The run-up to the GFC, however, showed that house prices can deviate from rents for an extended period of time. Glaeser and Gyourko (2007) also show empirically that the no-arbitrage condition does not hold given the substantial differences between owning and renting, while renters and owners also differ dramatically from each other. More recently, Amaral et al. (2024) find that house prices inequality has increased more than rent prices inequality across (US and other international) cities, as house prices rose more than rents, especially in areas with high house price-to-rent ratios. 

6 

that are already included at the state level (e.g. GDP) or whose sub-components are included, resulting in 1,221 series from which the factors are extracted (see also Table B.1 in Appendix B). At the state level, we include variables related to the real economy, the labor market, the financial sector, public finances, and the housing market. The rich information on state-specific housing market conditions includes house prices and rental prices, supply-side variables, such as permits and housing starts, and other important characteristics encompassing the homeownership rate and vacancy rates. If necessary, we take first (log-)differences of the variables to guarantee stationarity (see Table B.1 in Appendix B for detailed information on the variables’ transformation and definitions, and data sources). 

To measure price developments in state-level rental markets, we use a new rent price index developed by Howard and Liebersohn (2021). The authors build annual rent price indices for a large panel of US MSAs by resorting to data on rental incomes of multifamily residential properties taken from mortgage-backed securities data from Trepp. Their repeat-rent index (quality-adjusted) is conceptually similar to the consumer price index (CPI), which makes it comparable to the rent series in the CPI, but with the advantage of a much wider geographical coverage. We aggregate the original MSA rent index at the state level using population weights for each MSA.<sup>5</sup> 

Our measure of monetary policy surprises follows the recent literature relying on high-frequency identification (G¨urkaynak et al. 2005, Gertler and Karadi 2015, Nakamura and Steinsson 2018). Specifically, we take the surprises in interest rates for 3-month ahead contracts on Fed funds futures in a 30minute window surrounding FOMC meetings. We then sum up all daily surprises within the respective quarter. Since the surprises may not capture the ‘true’ structural monetary policy shock—for instance due to monetary policy relevant news outside the FOMC announcement window—we use the oneyear treasury rate as the monetary policy indicator, which also captures forward guidance effects about the future path of interest rates (Gertler and Karadi 2015). Several recent papers have emphasized the importance of further purging the high-frequency surprises from the so-called _central bank information effect_ (e.g. Jaroci´nski and Karadi 2020, Miranda-Agrippino and Ricco 2021, Bauer and Swanson 2023). In Section 6 we test the robustness of our baseline results by controlling for possible information effects. Overall, our main state-level responses remain robust to these alternative monetary policy surprises. 

> 5We interpolate the annual series to obtain quarterly data with the Denton method, using the rent of primary residence from the US CPI series as the indicator. We decided not to use rents data from Zillow given the shorter time dimension (data starting only in 2015). The rent index from Howard and Liebersohn (2021) is available for 217 MSAs, which contrasts with only 25 MSAs published by the Bureau of Economic Analysis. Data on rents are not available for four states (Alaska, Hawaii, New Hampshire, and Vermont). 

7 

#### **3 Factor-augmented VAR(X) model** 

The FAVAR approach chosen for our analysis has several advantages compared to alternative models. For instance, traditional small and medium-scale VAR models can suffer from the problem of information deficiency, while the FAVAR processes a much larger information set, providing a more complete overview of the economy (Bernanke et al. 2005). Specifically, the FAVAR extracts a small number of common factors from the full dataset. Similarly, and in contrast to individual VARs estimated for each state, the FAVAR provides a parsimonious framework to jointly analyze heterogeneous responses to a common monetary policy shock. We also prefer the FAVAR model over a panel VAR due to the lower estimation costs and fewer required specification assumptions. 

The FAVAR model has a simple state-space representation. The observation equation reflects the assumption that the dynamics of a large set of _N_ observed time series depend linearly on a smaller number of common (un)observed factors. In particular, the observation equation is given by: 



where _Xt_ = ( _X_ 1 _t_ , ..., _XNt_ )<sup>_′_</sup> is a vector of data observations, _Ht_ = ( _F_ 1 _t_ , ..., _Fqt_ , _R_ 1 _t_ , ..., _Rkt_ )<sup>_′_</sup> is a vector of _q_ unobserved factors ( _F_ ) and _k_ observed factors ( _R_ ), and Λ is a _N ×_ ( _q_ + _k_ ) matrix of factor loadings. In our case, there is only one observed factor ( _k_ = 1), which is the one-year treasury rate used to scale the monetary policy shock. Finally, _νt_ is a vector of normally distributed and uncorrelated error terms with diagonal covariance matrix Ω. The transition equation of the FAVAR model assumes that the factors follow a VAR(X) process given by: 



where Φ = (Φ1, ..., Φ _p_ ) is the ( _q_ + 1) _× p_ matrix containing the VAR coefficients and _zt_ is the ‘preidentified’ monetary policy surprise computed from intra-daily financial market data. _A_ is a vector of coefficients and _ut_ are the ‘non-monetary policy’ disturbances assumed to be normally distributed with full covariance matrix Σ. We include _p_ = 2 lags in the VAR, a fairly common choice for data at the quarterly frequency (see, for example, Baumeister et al. 2013, Mumtaz and Theodoridis 2017). 

To identify monetary policy shocks, we use the exogenous variable approach of Paul (2020). This identification strategy relies on including the set of ‘pre-identified’ monetary policy surprises _zt_ (see Section 2) as an exogenous variable in the VAR Equation (2). Under the assumption that _zt_ is a noisy measure of the true monetary policy shock _ϵmp_ , _t_ , i.e. _zt_ = _αϵmp_ , _t_ + _ηt_ , with _ηt_ orthogonal to all other variables, Paul (2020) shows that this approach consistently estimates the relevant impulse response 

8 

functions. Specifically, the contemporaneous reaction of factor _j_ to a one-unit increase in the policy rate _Rt_ is given by _Aj_ / _AR_ . For the remaining horizons, the relative impulse responses are derived by tracing the shock in the policy rate through the system described by Equation (2). As the surprise series _zt_ is only identified up to sign and scale, we normalize the coefficient vector _A_ such that a contractionary monetary policy shock corresponds to a median increase in the policy rate of 25 basis points (bps). On a methodological note, the _exogenous variable_ approach of Paul (2020) shares similarities with the _external instrument_ approach of Stock and Watson (2018). Paul (2020) shows analytically that the contemporaneous impulse responses obtained from both approaches are identical. For further details on the exogenous variable approach, we refer to Paul (2020). 

As outlined in Bernanke et al. (2005), the FAVAR model can be estimated in two ways: (i) using a fully likelihood-based (Bayesian) approach, in which the unobserved factors are sampled alongside the other model parameters; or (ii) by a two-step approach that first estimates the unobserved factors and then the remaining parameters conditional on these factors. In this paper, we follow Stock and Watson (2005), Korobilis (2013), and Corsetti et al. (2022) and use the two-step approach that is based on principal component analysis, which is easier to implement and computationally less demanding. 

In the first step, we extract, based on the Bayesian information criterion (BIC) of Bai and Ng (2002), five principal components from the set of state-level and aggregate US variables. Following common practice, the principal components are obtained from the standardized data after subtracting the mean of each series and dividing by the respective standard deviation. We address the issue that the principal component representation of the data is only identified up to rotation by imposing the standard normalization Λ<sup>_′_</sup> _F_<sup>Λ</sup><sup>_F_=</sup><sup>_Iq_.For the subsequent estimation of the remaining model parameters and the impulse</sup> response functions, we use the demeaned, but not fully standardized data. This allows us to interpret the impulse response functions directly and not just in relation to the variables’ standard deviations. In the second step, conditional on the estimated principal components to proxy _F_ , the observation Equation (1) collapses to _N_ univariate regressions (Korobilis 2013). Moreover, the transition Equation (2) constitutes a standard VAR(X) model. We estimate all parameters using Bayesian MCMC methods. In particular, we rely on an established Gibbs sampling algorithm, using a total of 10,000 draws and dropping the first 5,000 draws as ‘burn-in’. We refer to Appendix A for details on the estimation procedure and prior choices, which are overall standard with the exception of a somewhat tighter prior for the covariance matrix of the VAR innovations, Σ, given the relatively short time dimension of our sample. 

Figure C.1 in Appendix C shows the first five principal components together with the monetary policy indicator, which is the observed factor. To better understand the explanatory power of the factors, we regress each variable in our dataset on the six factors—both one factor at a time and all factors jointly— and report the respective R-squared values. Table C.1 lists the top five variables that are best 

9 

explained by each factor. Even though it is generally not possible to assign a structural interpretation to the unobserved factors, these results provide some evidence of what the factors may capture. While the first factor appears to relate closely to (mortgage) loan performance, the second, third, fourth, and fifth factor seem to contain information about the homeownership rate, the state-level rent price index, US prices and personal expenditures, as well as the state-level GDP deflator and personal bankruptcies, respectively. 

#### **4 The transmission of monetary policy to the housing market** 

In this section we start by presenting the responses of aggregate US variables to a monetary policy tightening with a particular focus on the housing market. We then move to the core of our analysis centered around the heterogeneity of the state-level responses. 

##### **4.1 US aggregate evidence** 

The aggregate responses of US variables allow us to check if our model is able to replicate a set of stylized facts on the effects of monetary policy. All variables are expressed in real terms, with the exception of permits, interest rates and ratios. Figure 2 presents the cumulative impulse response functions (IRFs) of selected US variables. Overall, we find that our results are in line with standard economic theory (Christiano et al. 1996, 1999). Following a monetary policy tightening calibrated to increase the one-year treasury rate by 25bps on impact, we find that economic activity falls quickly, with real GDP decreasing by around 0.5 percent after two years, and reaching a trough of around 0.8 percent after three to four years. The temporary rise in the one-year treasury rate—which lasts for about seven quarters—leads to a decline in inflation over the medium term, as measured by the consumer price index (CPI). 

Turning to housing market variables, a tightening of monetary policy decreases both house prices and housing supply, measured by the number of building permit authorizations. Specifically, we find that house prices fall on impact, declining by roughly 3 percent after two years, and 4 percent after five years, while building permits contract by almost 1 percent after two years, and by 1.5-2 percent after five years. These relatively large estimates, including the impact on real activity, fall on the high side of those reported in a meta-analysis by Williams (2015), who reviews eleven papers on the effects of monetary policy shocks on house prices and activity. Williams (2015) finds that a 100bps monetary policy shock leads average house prices to decline between 1.7 percent and 10.8 percent after two years, which compares with 12 percent in our estimates. In turn, Williams (2015) finds that real activity falls between 0.3 percent and 9.3 percent after two years, which compares with 2 percent in our analysis. 

10 

Figure 2: Impulse response functions of selected US variables 

























**Note:** Cumulative IRFs of selected US variables after a monetary policy tightening that increases the one-year treasury rate by 25bps. The solid black line is the median response and the shaded grey areas represent the 68% highest density interval (HDI). 

The large drop of house prices is consistent with recent evidence that house prices may have become more responsive to monetary policy since the GFC due to a decline in housing supply elasticities (Albuquerque et al. 2020, Aastveit et al. 2023), a long-term increase in the investor share of home purchases, or a prolonged period of ultra-low interest rates (Chudik and Kumar 2023).<sup>6</sup> 

We find suggestive evidence that monetary policy may affect both the intensive and extensive mar- 

> 6 Moreover, there is an ongoing debate about whether house prices may have become less responsive to contractionary monetary policy during the pandemic due to the increase in the share of fixed-rate mortgages. To be sure, the US mortgage market is increasingly dominated by mortgagors locked in (fixed) low-interest rate mortgages that originated before the 2022 tightening cycle started: the share of fixed-rate mortgages rose to 96.4% in 2023q2, up from 94.5% in 2019q4. Higher interest rates therefore only affect directly new mortgages. We remain silent on this issue since we are mostly interested in the cross-sectional variation of housing supply constraints. In addition, there is little variation in the share of fixed-rate mortgages across states. 

11 

gins of housing. On the intensive margin, the literature has documented how homeowners’ housing wealth effects may transmit to consumption (Iacoviello 2005, Bhutta and Keys 2016, Aladangady 2017, Beraja et al. 2019, Cloyne et al. 2020, Garriga and Hedlund 2020). In turn, the extensive margin can be seen in the fall in housing demand from prospective homeowners due to tighter credit conditions—measured with the net percentage share of banks reporting tightening standards for mortgage loans from the Senior Loan Officer Opinion Survey (SLOOS). As house purchases are typically debtfinanced, tighter credit conditions lead to a decline in the homeownership rate (Bhutta and Ringo 2021). In this context, some housing demand presumably shifts to the rental market, as also evidenced by an increase in the home vacancy rate, and a fall in the rental vacancy rate. We further explore this reallocation of housing demand in the following section. 

##### **4.2 Transmission of monetary policy to state-level housing markets** 

We take a closer look at the heterogeneity of housing market responses to a contractionary monetary policy shock across US states.<sup>7</sup> Figure 3 summarizes the posterior median responses of all US states. The solid black line is the response of the median state, while the grey areas refer to different percentiles of the states’ median responses. Two main findings emerge. First, there is sizeable heterogeneity across US states in the responses to a contractionary monetary policy shock; while economic activity, house prices, housing supply, and the homeownership rate all fall across the board, the magnitude of those declines varies widely.<sup>8</sup> Differences in the housing market structure, which we explore later, may explain part of this heterogeneity. Overall, our results confirm a large degree of heterogeneity in the transmission of monetary policy or demand shocks to the housing market (Paciorek 2013, Fischer et al. 2021, Aastveit and Anundsen 2022, Corsetti et al. 2022, Cooper et al. 2022, Koeniger et al. 2022, Aastveit et al. 2023). 

Second, we find that real rents increase over the horizon, which contrasts with the house price dynamics. This suggests that housing demand shifts from the owner-occupied segment to the rental market as the cost of homeownership goes up following a contractionary monetary policy shock. This is in line with recent research arguing that monetary policy influences the housing tenure decisions of households (Dias and Duarte 2019, 2022, Koeniger et al. 2022). We contribute to this literature by showing that, despite the synchronized fall in house prices and the increase in rent prices, monetary policy seems to exert a differential impact on households’ housing tenure decisions across states. For instance, 

> 7Our FAVAR model assumes symmetry regarding the monetary policy effects, i.e. contractionary and expansionary monetary policy shocks give rise to effects of the same magnitude, but with different signs. Recent literature, however, finds that there may be important asymmetries in the regional responses to monetary policy shocks: areas with more inelastic housing supply are more responsive to expansionary monetary policy shocks than to contractionary shocks (Aastveit and Anundsen 2022). These findings, however, are based on a sample that starts in the early-80s and stops in 2007. During this period, real house prices were mostly on an upward trend. We leave the study of such asymmetric effects of shocks for future work. 

> 8Considerable dispersion is also present in the state-level responses for unemployment, employment, and nominal rents (Figure C.2 in Appendix C). 

12 

the magnitude of the fall in the house price-to-rent ratio (HPI/rents)—typically used to summarize how expensive the owner-occupied segment is relative to renting—varies markedly across states, presumably influencing differently households’ decision to buy or rent.<sup>9</sup> 

Figure 3: Dispersion of state-level impulse response functions 

























**Note:** Distribution of the median (cumulative) IRFs across US states after a monetary policy tightening that increases the one-year treasury rate by 25bps. The black line is the median response of all state-level (median) responses. The grey areas include 30% (35–65 percentile), 60% (20–80 percentile) and 90% (5–95 percentile) of the median responses, respectively, going from dark to lighter grey. 

Other factors that should influence households’ housing tenure decisions are the cost of debt or credit conditions more generally. We indeed find that the tightening in credit conditions leads to a contraction in mortgage debt and an increase in mortgage delinquencies. Consistent with this, the reallocation of demand from the owner-occupied market to the rental market does not seem to evolve at the 

> 9We are simplifying the discussion, as regional heterogeneity in house price/rent ratios should reflect differences in housing risk, and in expectations on house and rent prices. But expectations about future house prices can be reasonably captured by current house prices in a context of extrapolative expectations (Glaeser et al. 2008). 

13 

same pace across states. In fact, we find that the homeownership rate declines only marginally for some states, while falling more markedly for others. In addition, housing market differences across states can also be seen in the responses of housing supply: home (rental) vacancy rates actually decline (increase) for some states, which contrasts with the median state response and the US aggregate evidence in Figure 2. The persistence in the decline of the rental vacancy rate indicates a high degree of segmentation in the US housing market, as increasing demand for rental units may not be fully met by supply, thus explaining the increase in rent prices (Greenwald and Guren 2021).<sup>10</sup> 

The shift from the owner-occupied to the rental market is consistent with recent evidence that contractionary monetary policy may disadvantage renters and homeowners with a mortgage (Dias and Duarte 2022). Our results indeed suggest that the combination of tighter credit conditions with lower house prices and higher rent prices could have disproportionate effects on these households. This questions the view that monetary policy may have little impact on renters (Aladangady 2017, Wong 2021) and bears relevance as mortgagors, and to a lesser extent renters, tend to be associated with the largest MPC (Cloyne et al. 2020). Moreover, by affecting house prices differently, and thus housing wealth and consumption, monetary policy may have important distributional effects (Coibion et al. 2017, Holm et al. 2021, Amberg et al. 2022, Bonifacio et al. 2022, Amaral et al. 2024). Overall, our results suggest that the monetary policy transmission depends on state-specific characteristics. As we will see, differences in housing supply elasticities, and in credit and housing wealth conditions may account for a portion of this regional variation. 

#### **5 Regional characteristics and the transmission of monetary policy** 

In this section we investigate the relevance of possible channels and state-specific characteristics in explaining the heterogeneous transmission of monetary policy. We follow the spirit of Corsetti et al. (2022), who look at institutional characteristics of selected euro area member states and their correlations with the strength of euro area monetary policy transmission. Given our larger cross section of US states, we focus on the average responses of states, grouping them by state-specific characteristics. Specifically, we compare the posterior distributions of the average response between states belonging to the top and bottom deciles of selected characteristics (Figures 5-8). We also show in Appendix C the posterior distributions of the differences between the groups’ average IRFs (Figures C.3-C.5), as well as the responses of the individual IRFs (Figures C.6-C.8) and the average quintiles (Figures C.9-C.11). We 

> 10The theoretical and empirical predictions in Greenwald and Guren (2021) suggest that rental and owner-occupied housing in the US are highly segmented. Their model generates house price dynamics that are close to those under perfectly segmented markets, reflecting large frictions in rental markets. The segmentation between owneroccupied and rental markets implies that credit supply shocks that shift the housing demand curve lead to higher house price-to-rent ratios, while the homeownership rate remains relatively unchanged. 

14 

then complement this analysis with a conditional (regression-based) correlation analysis. Table B.2 in the appendix contains the (average) values of selected characteristics for each state, highlighting those states that belong to the top/bottom deciles. 

##### **5.1 Transmission channels** 

###### **Housing supply channel** 

Recent research has shown that housing supply elasticities can play an important role in the transmission of demand shocks (e.g. from expansionary monetary policy) to the housing market (Gyourko et al. 2008, Saiz 2010, Glaeser et al. 2014, Albuquerque et al. 2020, Fischer et al. 2021, Aastveit and Anundsen 2022, Aastveit et al. 2023). According to this strand of research, house prices in areas with lower housing supply elasticities are more responsive to an expansion in demand than in high-supply elasticity areas. This finding is predicated on tighter land-use regulation and geographical restrictions that characterize a typical US low-supply elasticity area—found predominantly in coastal areas and in high-productivity and high-income places. These supply constraints make it more difficult and expensive to expand supply in the face of rising demand, resulting in a stronger increase of house prices to absorb demand. 

While there is growing evidence on the aforementioned link between monetary policy, supply elasticities and house prices, the literature has not yet assessed, to the best of our knowledge, the wider macrofinancial implications of monetary policy conditional on regional differences in housing supply—the _housing supply channel_ of monetary policy. This is particularly important given the recent rise of interest rates, where an expected larger fall in house prices in inelastic areas may amplify the contraction in economic activity, while raising financial stability risks. 

We use the land-use restriction index (LRI) constructed by Herkenhoff et al. (2018) as our measure of housing supply constraints. This indicator is based on a general equilibrium spatial model of the United States augmented with state-level data on employment, workers’ output, house prices and the amount of usable land. It is available for 48 states, excluding Alaska and Hawaii, and for each decade since 1950: 1950, 1960,..., 2000, and 2014. We split the states based on their indicator value in 2014, which should capture more accurately the prevailing stringency of land-use regulation during our estimation sample. Moreover, we divide the indicator by its standard deviation and change its sign so that higher values reflect states with tighter land-use regulation. There is a strong link between stringent land-use regulation and low housing supply elasticities, so we use these two terms interchangeably to refer to states with inelastic housing supply (Figure 4). We opted for the LRI of Herkenhoff et al. (2018) as our baseline measure of supply constraints since the other measures available in the literature (Saiz 

15 

2010, Aastveit et al. 2023) are computed at the MSA level, and thus need to be aggregated at the state level using population weights. The LRI is also available for an additional state (New Hampshire). In addition, the Saiz (2010) elasticities are estimated over 1970-2000, so they do not take into account the changes in supply elasticities over the last two decades. 

Figure 4: Herkenhoff et al. (2018) land-use restrictions in 2014 vs Saiz (2010) housing supply elasticities 





We find evidence of an important role played by differences in housing supply restrictions in the transmission of monetary policy (Figure 5).<sup>11</sup> States with tighter land-use regulation (blues lines) experience a larger decline in house prices and permits after a contractionary monetary policy shock compared to states with less stringent regulation (red lines). The shaded areas represent the 68% highest density interval (HDI) of the average responses within the two groups across all MCMC draws. The HDI of the differences between the average IRFs across groups excludes zero for most variables (Figure C.3 in Appendix C).<sup>12</sup> We further add to the literature by documenting that the macrofinancial implications of monetary policy shocks are felt more strongly in areas with inelastic supply. A larger decline in housing wealth for households in these areas leads to a greater fall in consumption. Consistent with the fall in consumption, the unemployment rate increases more substantially in inelastic states (Figure C.15 in Appendix C). 

Financial stability risks may also increase more sharply in inelastic states. Mortgage debt falls more 

> 11Our results remain robust to exploring the cross-sectional distribution of the LRI taking 2000, instead of 2014, as the reference year (Figure C.12 in Appendix C). Moreover, the same holds when exploring the cross-sectional distribution of house values and house price-to-rent ratios, as low-supply elasticity states tend to have higher house prices (see Figures C.13 and C.14). 

> 12Despite our relatively short sample that comes with sizeable estimation uncertainty, this result reinforces our view that the differences we uncover between supply elasticity groups are an underlying characteristic of the economy. 

16 

Figure 5: Impulse responses across Herkenhoff et al. (2018) LRI: decile averages 



















**Note:** Posterior distributions of the average (cumulative) IRFs across US states after a monetary policy tightening that increases the one-year treasury rate by 25bps. The blue (red) line with circles (crosses) indicates the median (over all MCMC draws) of the average responses of the states belonging to the top (bottom) decile of the respective state characteristic. Shaded areas reflect the 68% HDI. The dashed black line is the median of the average IRFs across all the other states. 

strongly, arguably reflecting a combination of lower demand and tighter credit conditions. Mortgage delinquencies rise more sharply, and foreclosures and other indicators proxying the health of the banking sector also deteriorate more considerably (Figure 6). Overall, this is suggestive evidence of interlinkages between credit and supply elasticities in amplifying the macrofinancial effects of contractionary monetary policy shocks. 

Our results should not be driven by differences in the share of adjustable-rate mortgages across states. ARM mortgages are fairly uncommon in the US economy, which contrasts with Europe, where the share of ARM varies considerably across countries, and therefore the pass-through of monetary policy to mortgage markets also varies widely (Calza et al. 2013, Corsetti et al. 2022, Pica 2023). In addition, according to data from the Federal Housing Finance Agency, there is very little variation in the ARM share across US states: for instance, the ARM share stood at 5.5% of all outstanding mortgages nationally in 2019q4, with a standard deviation of 1.8 percentage points across all states. 

17 

Figure 6: Impulse responses of selected bank indicators across Herkenhoff et al. (2018) LRI: decile averages 

|Banks’ ROA<br>Banks’ NPLs<br>Foreclosure rate|
|---|









**Note:** See Figure 5. 

Our finding that house prices decline more in inelastic states may, at face value, be surprising. Housing supply is rigid downwards, given the durability of housing, thus the house price response to negative demand shocks should be independent of supply restrictions (Glaeser and Gyourko 2005, Glaeser et al. 2008, Aastveit and Anundsen 2022). We rationalize this result with findings on (i) the role of credit boom-busts in driving housing market cycles in more inelastic areas during the 2000s US housing boom-bust (Huang and Tang 2012, Anundsen and Heebøll 2016), and on (ii) household overoptimism during the housing boom phase due to diagnostic expectations (Chodorow-Reich et al. 2024). This strand of research shows that more inelastic US areas had a stronger housing boom-bust during the 2000s, followed by a sharper post-GFC rebound (Chodorow-Reich et al. 2024). 

On (i) above, Huang and Tang (2012) find that households in cities with tighter supply constraints also relied more on credit, particularly subprime mortgages, which may explain why these cities recorded both a larger boom in house prices in the run-up to the GFC, and a subsequent larger bust in house prices during the crisis as the credit crunch started to bite. Anundsen and Heebøll (2016) also document that both financial-accelerator effects and price-to-price feedback loops may explain why low-supply elasticity areas recorded a stronger contraction in house prices in the aftermath of the GFC. 

Finally, on (ii) above, Chodorow-Reich et al. (2024) show empirically and theoretically that highgrowth price areas (low-supply elasticity areas) experienced a larger boom in house prices in the run-up to the GFC due to households’ overoptimism, giving rise to a larger bust when beliefs started to correct. The fall in house prices in these low-supply elasticity areas was also amplified by excessive borrowing and a price-foreclosure spiral as foreclosures increased the stock of housing available for sale, further depressing prices (also in line with the theoretical predictions in Guren and McQuade 2020). House prices may thus not be independent of the supply elasticity in the presence of negative demand shocks when important financial-accelerator effects and misaligned household expectations are at play. This can then rationalize our finding of a stronger credit crunch and rising financial stability risks in inelastic 

18 

states, amplifying the house price responses after a tightening in monetary policy.<sup>13</sup> 

Our findings also speak to research documenting the impact of monetary policy on households’ housing tenure decisions (Dias and Duarte 2019, 2022, Koeniger et al. 2022). Our contribution is to show that monetary policy may have a stronger influence on housing tenure decisions in states where supply is more constrained.<sup>14</sup> In particular, we draw this implication from the larger fall in house prices, coupled with signs of a larger decline in homeownership rates for inelastic states. In addition, we document a smaller increase in rent prices in inelastic states, which may be related to differences in market segmentation across states, i.e. the frictions and adjustment costs in converting owner-occupied housing units to rental properties (Greenwald and Guren 2021). While we cannot observe the degree of segmentation across markets, the rental market in these states seems to have more capacity to absorb demand than in elastic states, further illustrated by a relatively unchanged rental vacancy rate for inelastic states (Figure C.17 in Appendix C). Overall, we speculate that more stringent regulation to build new housing units in some areas may indirectly create incentives for homeowners to reduce adjustment costs in converting owner-occupied units to rental units in the face of shocks. An alternative explanation for the weaker response of rent prices in inelastic areas could be the initially already high rent levels in these areas (according to Zillow data), which potentially limit the scope for further increases. Stringent rent controls in several cities in two inelastic states, California and Maryland (according to the National Multifamily Housing Council and RentPrep), may also explain the more muted response of rent prices. 

Finally, the larger decline in house prices in low-supply elasticity states, which lead to negative housing wealth effects and lower housing equity of existing homeowners, suggest important distributional effects _across_ states. These are high-income states where households tend to have larger housing wealth and higher consumption/income per capita (Figures C.18–C.20). The larger decline in housing wealth in inelastic states can be mapped to a larger fall in overall consumption expenditures, and therefore in economic activity in these states. Although it is outside of the scope of our paper, we find that contractionary monetary policy shocks may have a non-negligible role in reducing regional consumption and housing wealth inequality. This chimes with Amaral et al. (2024), who suggest that higher interest rates can decrease the dispersion and thus inequality in house prices across US cities. 

Let us conclude this section by stressing that the presented exercise does neither imply that housing 

> 13A complementary explanation relies on the relationship between house prices and minimum profitable construction costs (MPPC). Glaeser and Gyourko (2018) argue that the shape of the housing supply curve depends on house prices relative to MPPC. Building on this notion, Aastveit and Anundsen (2022) find that house prices are typically above the MPPC in supply-inelastic areas, which theoretically makes it possible for house prices to decline by more than in (elastic) areas where house prices are close to the MPCC. This is consistent with our results: low-supply elasticity areas, typically found in coastal areas (e.g. California), characterized by high house prices relative to MPPC, experience a stronger fall in house prices after a contractionary monetary policy shock. 

> 14Over longer horizons, the persistent decline in the house price-to-rent ratio, which makes buying cheaper relative to renting, may encourage some renters to transition to the owner-occupied segment. 

19 

supply constraints are the only driver of regional heterogeneity in the responses to monetary policy shocks, nor does it prove a causal relationship. For instance, differences across states in the industry composition, demography, income levels, and in the quality of institutions may also explain the documented heterogeneity. While our empirical approach and data have limitations that prevent us from investigating further a possible causal link running from housing supply constraints (or elasticities), we take comfort from well-established findings in the literature documenting the strong relevance of constraints on housing supply for explaining the regional response of house prices to demand shocks (Saks 2008, Saiz 2010, Aastveit and Anundsen 2022, Aastveit et al. 2023). Moreover, Section 5.2 attempts to analyze the joint relevance of various state-specific characteristics, including housing supply constraints, for the differential responses to monetary policy shocks across states. Overall, we believe that the interaction of housing demand changes with housing supply frictions plays an important role in driving the differential behavior of the real economy across US states. 

###### **Debt overhang channel** 

Another possible source of cross-sectional heterogeneity in the response to monetary policy shocks is differences in households’ debt imbalances, or debt overhang in the spirit of Eggertsson and Krugman (2012). In theory, as the cost of borrowing goes up, borrowing constraints become more binding for households with larger debt imbalances, i.e. whose debt deviates more from fundamentals, leading to a larger contraction in housing demand and house prices, consumption, and economic activity (Iacoviello 2005, Calza et al. 2013, Hedlund et al. 2016, Bhutta and Ringo 2021, Bosshardt et al. 2023, Pica 2023). We proxy household debt overhang for each state with the concept of a debt gap (Albuquerque 2019, Alpanda and Zubairy 2019). We compute the debt gap with the Hamilton (2018) filter on the statelevel mortgage debt-to-income ratio using standard values for financial variables at quarterly frequency ( _p_ = 1 and _h_ = 20). Specifically, we compare states that fall in the top and bottom deciles of the debt gap distribution, using the maximum value of the debt gap over time for each state.<sup>15</sup> 

We find that contractionary monetary policy shocks transmit more strongly to states with larger debt gaps: house prices, housing supply, mortgage debt, and consumption fall by considerably more than in states with smaller debt imbalances (Figure 7). Financial stability risk may also increase more prominently in areas with larger household debt imbalances (Figure C.21 in Appendix C). These findings are in line with research that finds that changes in interest rates affect more households and regions closer to the borrowing constraint (Hedlund et al. 2016, Bhutta and Ringo 2021, Bosshardt et al. 2023). Furthermore, we find that the responses of high-debt gap states are qualitatively similar to the previous results we saw for low-supply elasticity areas. This is not a surprise given the positive correlation be- 

> 15Our results remain qualitatively similar when proxying debt imbalances with the state-level debt-to-income ratio. 

20 

tween supply constraints and household debt gaps (Figure C.22 in Appendix C).<sup>16</sup> This reinforces the view that the interconnectedness between household debt overhang and housing supply constraints may amplify the macrofinancial effects of contractionary monetary policy shocks. 

Figure 7: Impulse responses across debt gap: decile averages 



















**Note:** See Figure 5. 

###### **Housing wealth volatility and household balance sheet channel** 

The ability of mortgagors to extract home equity to finance consumption should also be relevant to explain the differential effects of monetary policy (Bhutta and Keys 2016, Aladangady 2017, Beraja et al. 2019, Andersen and Leth-Petersen 2021). According to this strand of the literature, the fall in house prices and in housing equity reduces housing equity extraction for existing homeowners, which leads to a contraction in housing demand that reinforces the decline in house prices and in economic activity. As a corollary, households with large housing wealth are in a better position to smooth their 

> 16Although the correlation is sizeable (around 0.6), we generally capture different states in the high/low bins of the LRI and the debt gap, with some overlap: California appears in both the top LRI and debt gap bins, while North Dakota and Oklahoma both fall in the bottom bins of the LRI and debt gap (see also Table B.2). This suggests that our results overall capture more the differential effects of groups of states with low/high supply elasticities and household debt imbalances, rather than being driven by particular states. 

21 

consumption expenditures in the face of interest rate shocks, as the probability of going _underwater_ , i.e. the value of their houses falling below their mortgage commitments, is lower than for low-housing wealth households. This is indeed what we see in Figure C.13 in Appendix C. 

What is less studied is how the volatility of housing wealth—irrespective of its level—may affect households’ housing demand and consumption decisions in the face of a monetary policy tightening. We posit that higher uncertainty or volatility of housing wealth may lead households to reduce more their demand for real estate services or postpone their house purchase, leading to an overall stronger reduction in economic activity. This conjecture relates to research that has found a link between uncertainty about future house prices and households’ housing tenure decisions (Henderson and Ioannides 1983, Rosen et al. 1984, Fu 1995). We use the standard deviation of housing wealth over the sample period as a proxy for housing wealth volatility. We follow Albuquerque and Krustev (2018) and compute housing wealth for each state _j_ and quarter _t_ as: (homeownership rate _j_ , _t ×_ total occupied housing units _j_ , _t_ ) _×_ house price index _j_ , _t ×_ median house price in 2000 _j_ . 

Figure 8: Impulse responses across housing wealth volatility: decile averages 



















**Note:** See Figure 5. 

Figure 8 suggests that states with larger fluctuations in housing wealth may indeed react more 

22 

strongly to monetary policy: house prices fall by more than in states with lower housing wealth volatility, which goes hand-in-hand with a larger fall in consumption expenditures. Interestingly, while we find a significant and positive correlation between housing wealth volatility and the consumption reaction, this is not the case when considering average housing wealth (see the unconditional pairwise correlations in Table C.2), despite the housing wealth level and its volatility being highly correlated (around 0.9). In addition, for most of the remaining variables, the correlation between the strength of the response and the volatility of housing wealth appears to be stronger compared to the housing wealth level. Overall, these findings suggest that larger uncertainty about housing wealth could strengthen the transmission of monetary policy. 

##### **5.2 Cross-sectional multivariate analysis** 

In this section we use cross-sectional regressions to simultaneously analyse the drivers of heterogeneity in the responses of economic activity and housing markets to monetary policy. Specifically, we follow Mumtaz et al. (2018) and regress the IRFs of key variables on a set of state-level characteristics: 



where _IRFh_<sup>_y_</sup> , _i_<sup>denotes the cumulative response of variable</sup><sup>_y_in state</sup><sup>_i_after</sup><sup>_h_quarters. The 1</sup><sup>_× K_vector</sup><sup>_Xi_</sup> includes state-specific variables that potentially explain the heterogeneity in the responses, _β_ is a _K ×_ 1 vector of regression coefficients, _α_ is the regression constant, and _regionsi_ is a vector of dummies for the eight divisions defined by the Bureau of Economic Analysis. While this exercise allows us to jointly analyze the importance of several variables, we stress that the results should be taken with a pinch of salt given the relatively small cross section of US states. In addition, and differently from Section 5.1 that explored the differential responses between groups of states, the cross-sectional regressions focus on the _average_ relationship between monetary policy and selected state characteristics. 

On top of the variables discussed in Section 5.1, here we also control for other state-level characteristics that may play a role in explaining the heterogeneity in the regional responses to a tightening in monetary policy. First, the so-called _sand states_ (Arizona, California, Florida and Nevada) are known to have a more sensitive housing cycle (Ben-David et al. 2024). Second, we explore the role of _labor market rigidities_ . A more rigid labor market may cushion the effects of an adverse monetary policy shock, leading to a smaller decline in income and potentially reducing the transmission to the housing market. We follow Mumtaz et al. (2018) and use the existence of the right-to-work legislation as a proxy for such rigidities. States which have implemented this legislation are considered to have a more flexible labor market. Third, we consider the share of manufacturing in state-level GDP and the share of small firms 

23 

in total employment. States with more manufacturing-intensive sectors and areas with a larger share of small firms have been found to be more sensitive to interest rates (Carlino and DeFina 1998, 1999). Finally, we also control for the overall house price dynamics in a state by including the cumulative house price growth over the sample. 

Table 1: Cross-sectional regression results ( _h_ = 12) 

|Dependent<br>variables:|(1)<br>GDP|(2)<br>PCE|(3)<br>HPI|(4)<br>Rents|(5)<br>Permits|(6)<br>HOR|
|---|---|---|---|---|---|---|
|LRI|**-0.347**<sup>_∗_</sup>|**-0.339**<sup>_∗∗∗_</sup>|**-0.868**<sup>_∗∗_</sup>|**-0.834**<sup>_∗_</sup>|-0.006|-0.021|
||(0.200)|(0.091)|(0.335)|(0.418)|(0.089)|(0.069)|
|Debt Gap|-0.002|-0.004|-0.022|0.000|**-0.013**<sup>_∗∗_</sup>|**-0.005**<sup>_∗_</sup>|
||(0.011)|(0.005)|(0.020)|(0.024)|(0.005)|(0.002)|
|HW (avg.)|**0.012**<sup>_∗∗_</sup>|0.000|**0.022**<sup>_∗_</sup>|**0.018**<sup>_∗_</sup>|0.003|0.001|
||(0.005)|(0.003)|(0.012)|(0.009)|(0.003)|(0.002)|
|HW (std.)|-0.006<br>(0.004)|0.001<br>(0.003)|-0.013<br>(0.008)|0.000<br>(0.007)|-0.001<br>(0.002)|-0.000<br>(0.001)|
|Sand state|**-1.330**<sup>_∗∗∗_</sup>|**-0.496**<sup>_∗∗_</sup>|**-2.434**<sup>_∗∗_</sup>|-0.759|-0.409|-0.003|
||(0.482)|(0.243)|(1.001)|(1.020)|(0.255)|(0.083)|
|RTW|**-0.454**<sup>_∗∗_</sup>|**-0.588**<sup>_∗∗∗_</sup>|-0.736|-0.522|**0.387**<sup>_∗∗∗_</sup>|-0.008|
||(0.220)|(0.138)|(0.477)|(0.644)|(0.113)|(0.068)|
|Manufacturing|**-0.039**<sup>_∗_</sup>|**0.017**<sup>_∗_</sup>|**0.098**<sup>_∗∗_</sup>|0.070|0.002|0.004|
||(0.021)|(0.010)|(0.036)|(0.043)|(0.011)|(0.006)|
|Small frms|-0.024|-0.012|**-0.055**<sup>_∗_</sup>|-0.014|**0.017**<sup>_∗_</sup>|0.002|
||(0.020)|(0.010)|(0.029)|(0.044)|(0.008)|(0.004)|
|HPI growth|**0.072**<sup>_∗∗∗_</sup>|**0.035**<sup>_∗∗∗_</sup>|**0.051**<sup>_∗_</sup>|0.006|**0.016**<sup>_∗∗_</sup>|0.008|
||(0.019)|(0.010)|(0.030)|(0.031)|(0.007)|(0.005)|
|Observations|48|48|48|46|48|48|
|Adjusted_R_<sup>2</sup>|0.657|0.664|0.861|0.232|0.720|0.443|



**Note:** The table shows the point estimates and standard errors for the regression shown in Eq. 3. GDP = Real GDP. PCE = Real personal consumption expenditure. HPI = Real house price index. HOR = Homeownership rate. LRI = Land-use regulation index of Herkenhoff et al. (2018) for the year 2014. Debt gap = Average of Hamilton-filtered mortgage debt-to-income ratio from 1999-2019. HW (avg.) = 100*log(Average housing wealth over 1999-2019). HW (std.) = 100*log(Standard deviation of housing wealth over 1999-2019). Sand state = Dummy variable for Arizona, California, Florida, and Nevada. RTW = Dummy variable for right-to-work states. Manufacturing = Share of manufacturing in state-level GDP. Small firms = Share of small firms employment in total employment. HPI growth = Growth rate of house prices over 1999-2019. All regressions include regional dummies. Robust standard errors in parentheses. _∗ p <_ 0.1, _∗∗ p <_ 0.05, _∗∗∗ p <_ 0.01. 

Table 1 presents our main results. While we focus on the variables’ (medium-term) cumulative response after _h_ = 12 quarters, our results remain qualitatively similar when using _h_ = 8 and _h_ = 20. We highlight several key results. For instance, the degree of land-use regulation in a state stands out as an important driver of the transmission of monetary policy to the housing market and the broader 

24 

economy. A state in which land-use regulation is one standard deviation higher, exhibits a 0.9 percentage point larger house price drop following a surprise tightening of 25bps. Our results also indicate that this translates into lower economic activity and consumption. In addition, real rents increase by 0.8 percentage points less after three years. 

When inspecting the evidence of a potential debt overhang channel, measured with the debt gap, we find that the coefficients mostly have the expected signs, but are only significant for the reactions of permits and the homeownership rate. This suggests that household debt imbalances still add some extra explanatory power for the differential effects of monetary policy on the housing market once we account for differences in housing supply constraints. Regarding a possible housing wealth channel, differences in the first moment of housing wealth over the sample can explain some degree of heterogeneity, but this does not hold for the second moment once controlling for other variables. 

For other state characteristics—whether a state is a so-called sand state or has the right-to-work legislation in place— the results are broadly consistent with our prior assumptions. The same holds for the small firms share, where the larger the proportion of small firms in total employment, the stronger the fall in economic activity, as illustrated by consumption and house prices (Carlino and DeFina 1998, Furceri et al. 2019). Regarding the role of a higher manufacturing share in an area, the results are somewhat mixed, with GDP reacting stronger but consumption and house prices weaker. 

#### **6 Robustness checks** 

In this section, we carry out three main exercises to check the robustness of our baseline results. First, we use alternative monetary policy surprise series from the literature. We first depart from the conventional monetary policy shocks by also using shocks that capture more the long end of the yield curve. Specifically, we use shocks on forward guidance (FG) from Swanson (2021). Inspecting the cross-state dispersion of the IRFs of consumption, house prices, and permits, as well as the reactions sorted by the land-use restriction index of Herkenhoff et al. (2018), we find that the results remain qualitatively very similar (Figure C.23 in Appendix C). We also replace our baseline series of monetary policy surprises with the one from Jaroci´nski and Karadi (2020) that controls for central bank information effects. The new results also remain qualitatively similar (Figure C.24). 

Second, we take alternative measures of the elasticity of housing supply from the existing literature. In particular, we replace the land-use restriction index of Herkenhoff et al. (2018) with the housing supply elasticity series from Aastveit et al. (2023), and Saiz (2010). These supply elasticity series are available for a large set of US MSAs, so we aggregate them at the state level using population weights 

25 

(results are very similar when using income weights). When using the housing supply elasticities computed by Aastveit et al. (2023), available as average elasticities over 1996-2006 (Figure C.25) or over 2012-2019 (Figure C.26), we find that—with some exceptions—the results remain broadly comparable to our baseline findings in Figure 5. The same holds true when using Saiz (2010) housing supply elasticities (Figure C.27). 

Third, we replace the state-specific GDP deflator, used throughout the paper, with an alternative state-level inflation series computed by Hazell et al. (2022). We find that our results for the cross-state dispersion of the IRFs of inflation and output remain comparable to our baseline case (Figure C.28). While the state-level inflation data of Hazell et al. (2022) ends in 2017q4, this series is smoother for a few states compared to the GDP deflator series. 

#### **7 Conclusion** 

We use a FAVAR model and a large set of state-level (and aggregate US) variables over 1999q1–2019q4 to trace out the role of regional housing markets in the transmission of monetary policy. Our main findings point to significant heterogeneity in the transmission of an aggregate contractionary monetary policy shock to the US states. We find that the regional variation in responses to monetary policy can be partly accounted for by state-specific characteristics, most prominently by differences in housing supply elasticities, but also household debt overhang and housing wealth (volatility). In particular, we show that low-supply elasticity areas, where land-use regulation is more stringent, record a larger fall in house prices and in economic activity more generally. In addition, financial stability risks appear to increase more sharply in these areas, as evidenced by a surge in mortgage delinquencies and foreclosures, while indicators proxying bank health also deteriorate faster. We find similar results for areas with higher imbalances in household debt—presumably where household borrowing constraints become more binding. Our findings thus show that the interaction between household debt overhang and housing supply constraints can amplify the macrofinancial effects of monetary policy. 

We also show that our results are consistent with recent findings in the literature that monetary policy can influence households’ housing tenure decisions: the rise in homeownership costs induced by higher interest rates leads to a decline in house prices but an increase in rental prices. The resulting fall in house price-to-rent ratios, however, varies substantially across states. We speculate that this may depend on housing supply elasticities and on the degree of market segmentation. Overall, this implies that the monetary policy effects on housing tenure decisions may be heterogeneous across states. 

Our results shed more light on the possible macrofinancial effects of monetary policy in the context 

26 

of recently rapidly rising interest rates to tame inflationary pressures. It is well-established that housing is highly sensitive to interest rates, but we have shown that its sensitivity varies across US states, particularly resulting from differences in supply conditions in the housing market, and in household indebtedness. Although the Federal Reserve conducts monetary policy with a dual mandate of price stability and full employment for the US economy as a whole, our paper shows that monetary policy can nonetheless have differential macrofinancial effects across states within the country. 

Our results have policy implications. If housing markets, and the wider macroeconomy, are more sensitive to monetary policy in areas with more inelastic housing supply, it could be advisable for financial supervision to tighten more in these areas to limit excessive house price volatility (Glaeser 2019). Since house purchases are mostly financed by mortgage debt, there is a case for strengthening macroprudential measures aimed at taming borrowing, such as limits on loan-to-income or/and debtservice ratios, before debt imbalances start to emerge. In addition, the relaxation of land-use restrictions should make an area less prone to boom-bust cycles in house prices as builders are less constrained to expand supply during an expansion. By smoothing the cycle during an expansion, less stringent regulation should help an economy be more resilient to contractionary demand shocks. 

On a different note, our results suggest that monetary policy may have important distributional effects. For instance, Amaral et al. (2024) suggest that higher interest rates can decrease the dispersion in house prices across US cities if the real discount rate increases again. This is consistent with our results: we find that contractionary monetary policy shocks cause a larger decline in house prices in low-supply elasticity states, which lead to negative housing wealth effects and lower housing equity for homeowners. These are typically high-income states where households tend to have larger housing wealth and higher consumption per capita. Against this background, we interpret our result as suggesting that contractionary monetary policy shocks may help decrease consumption and housing wealth inequality across states. We leave a more formal investigation of this topic for future research. 

27 

#### **Appendix A: Estimation procedure** 

This appendix contains details on the Markov Chain Monte Carlo (MCMC) algorithm used to estimate the FAVAR model. 

##### **Block 1: Sample the factor loadings** Λ **from** _p_ (Λ _|X_ , _H_ , Ω) **and the error covariance matrix** Ω **from** _p_ (Ω _|X_ , _H_ , Λ) 

Conditional on the estimated factors (principal components), sampling the elements of the matrix of factor loadings in Equation (1) and the error covariance matrix Ω reduces to _N_ standard linear Bayesian regression problems (see e.g. Koop 2003). The conditional posterior of the loadings in each of the _N_ rows of Λ, denoted by Λ _i_ = ( _λ_ 1<sup>_F_</sup> _i_<sup>, ...,</sup><sup>_λ_</sup> _qi_<sup>_F_,</sup><sup>_λ_</sup> _i_<sup>_R_) for</sup><sup>_i_= 1, ...,</sup><sup>_N_, under the normal prior Λ</sup><sup>_i∼N_(Λ</sup><sup>_i_,0, ΣΛ</sup> _i_<sup>,0),</sup> is: 



where _H_ = ( _F_ 1, ..., _Fq_ , _R_ ) , _Xi_ = ( _Xi_ 1, ..., _XiT_ )<sup>_′_</sup> , and _ωi_<sup>2isthe</sup><sup>_i_thdiagonalelementofΩ.Aftersam-</sup> pling Λ _i_ , the corresponding element of Ω, _ωi_<sup>2,canbesampled,undertheinverse-gammaprior</sup><sup>_ω_</sup> _i_<sup>2</sup><sup>_∼_</sup> _IG_ ( _c_ 0, _C_ 0), from 



where notation follows Chan and Hsiao (2014) and where _C_ is defined as: 



Finally, the prior values are set to Λ _i_ ,0 = 0( _q_ +1) _×_ 1, ΣΛ _i_ ,0 = 4 _× I_ ( _q_ +1), _c_ 0 = 0.2, and _C_ 0 = 0.2. 

##### **Block 2: Sample the VAR(X) coefficients** Φ **and** _A_ **from** _p_ (Φ, _A|H_ , _z_ , Σ) 

The VAR(X) coefficients _θ_ = _vec_ ((Φ, _A_ )), assuming a normal prior distribution _θ ∼N_ ( _θ_ 0, _Vθ_ ,0), have the following conditional posterior distribution (see, for example, Blake and Mumtaz 2012): 





and where _H_<sup>�</sup> = ( _Ht−_ 1, ..., _Ht−p_ , _z_ ) and _θ_<sup>¯</sup> OLS is the OLS estimate of the VAR(X) coefficients. The prior configuration is relatively uninformative, i.e. _θ_ 0 = 0[( _q_ +1) _×_ (1+ _p×_ ( _q_ +1))] _×_ 1 and _Vθ_ ,0 = _I_ ( _q_ +1) _×_ (1+ _p×_ ( _q_ +1)). 

28 

##### **Block 3: Sample the VAR(X) innovation covariance matrix** Σ **from** _p_ (Σ _|H_ , _z_ , Φ, _A_ ) 

The covariance matrix of the VAR innovations, assuming an inverse-Wishart prior distribution Σ _∼ IW_ (Σ0, _ν_ Σ), has the following conditional posterior distribution (see, for example, Blake and Mumtaz 2012): 



where _u_ = ( _u_ 1, ..., _uT_ )<sup>_′_</sup> are the ‘non-monetary policy’ VAR residuals with each _ut_ = _Ht −_ Φ1 _Ht−_ 1 _−_ ... _−_ Φ _p Ht−p − Azt_ , and the prior scale matrix and prior degrees of freedom are set to Σ0 = _λ_ 0 _Iq_ +1 (with _λ_ 0 = 3<sup>_−_1</sup> ) and _ν_ Σ = _q_ + 1, respectively. 

#### **Appendix B: Data description** 

We use seasonally adjusted quarterly data from 1999q1 to 2019q4 and deflate all nominal data using the US consumer price index. To avoid double-counting in the factor estimation (PCA), we do not include some of the aggregate variables such as GDP, since all its components are already included. We also do not include US aggregate variables if the same variable is included at the state level (e.g. the homeownership rate). The last column of Table B.1 indicates which variables are included in the PCA. 

###### <u>Transformations:</u> 

- 1 – no transformation 

- 2 – first (log-)differences 

- 3 – logarithm 

Table B.1: Data and transformations 

|Code|Description<br>T|ransform.<br>Source|PCA|
|---|---|---|---|
||**US variables**|||
|_Rates and spreads_||||
|BaaAaa spread|Difference<br>between<br>Moody’s<br>sea-<br>soned<br>Baa<br>corporate<br>bond<br>yield<br>(DBAA) and Moody’s seasoned Aaa<br>corporate bondyield (DAAA)|1<br>FRED|Y|
|FEDFUNDS|Federal funds rate|1<br>FRED||
|GS1|One-year treasuryrate|1<br>FRED||
|GZ spread|Excess bond premium|1<br>Gilchrist and<br>Zakrajˇsek(2012)|Y|
|Mortgage spread|Difference between 30y mortgage<br>rate at Market Yield on U.S. Treasury<br>Securities at 30-Year Constant Matu-<br>rity, Quoted on an Investment Basis<br>(DGS30)|1<br>FRED|Y|



29 

Table B.1: Data and transformations 

|Code|Description<br>|Transform.|Source|PCA|
|---|---|---|---|---|
|Prime spread|Difference between bank prime loan<br>rate (MPRIME) and Federal funds<br>rate|1|FRED|Y|
|Term spread|Difference between GS10 and GS1|1|FRED|Y|
|_Housing variables_|||||
|CUSR0000SEHA|Rents: CPI for all urban consumers:<br>Rent of primary residence in US city<br>average|2|FRED||
|CSUSHPISA|S&P/Case-Shiller<br>U.S.<br>National<br>Home Price Index|2|FRED||
|HOUST|New privately-owned housing units<br>started|3|FRED||
|PERMIT|New privately-owned housing units<br>authorized inpermit-issuing places|3|FRED||
|RHVRUSQ156N|Home vacancyrate|1|FRED||
|RRVRUSQ156N|Rental vacancyrate|1|FRED||
|RSAHORUSQ156S|Homeownershiprate|1|FRED||
|_Financial market variables_|||||
|BUSLOANS|Commercial and industrial loans, all<br>commercial banks|2|FRED|Y|
|CMDEBT|Households and nonproft organiza-<br>tions; Debt securities and loans; Lia-<br>bility, level|2|FRED|Y|
|DRSFRMACBS|Delinquency rate on single-family<br>residential mortgages, booked in do-<br>mestic offces, all commercial banks|1|FRED||
|HHMSDODNS|Households and nonproft Organiza-<br>tions; One-to-four family residential<br>mortgages; Liability, level|2|FRED|Y|
|M2SL|M2 moneystock|2|FRED|Y|
|NPTLTL|Nonperforming total loans (past due<br>90+ days plus nonaccrual) to total<br>loans|1|FRED||
|REALLN|Real estate loans,<br>all commercial<br>banks|2|FRED|Y|
|SLOOS|Net percentage share of banks report-<br>ing tightening standards for mort-<br>gage loans (Senior Loan Offcer Opin-<br>ion Surveyon Bank Lending)|1|Haver||
|SP500|S&P 500|2|FRED|Y|
|TLAACBW027SBOG|Total assets, all commercial banks|2|FRED||
|TOTBKCR|Bank credit, all commercial banks|2|FRED|Y|
|TWEXMMTH|Trade-weighted US Dollar index: Ma-<br>jor currencies,goods|1|FRED|Y|
|USROA|Return on average assets for all US<br>banks|1|FRED||



30 

Table B.1: Data and transformations 

|Code|Description|Transform.<br>Source|PCA|
|---|---|---|---|
|VIX|CBOE volatilityindex|1<br>FRED|Y|
|_Real variables_||||
|CBI|Change inprivate inventories|1<br>FRED|Y|
|DSPI|Disposablepersonal income|2<br>FRED||
|EXPGS|Exports ofgoods and services|2<br>FRED|Y|
|FDEFX|Federal government:<br>National de-|2<br>FRED|Y|
||fense consumption expenditures and<br>gross investment|||
|FNDEFX|Federal government:<br>Nondefense<br>consumption expenditures and gross<br>investment|2<br>FRED|Y|
|GDPC1|Realgross domesticproduct|2<br>FRED||
|IMPGS|Imports ofgoods and services|2<br>FRED|Y|
|INDPRO|Industrialproduction: Total index|2<br>FRED|Y|
|PCE|Personal consumption expenditures|2<br>FRED||
|PCEDG|Personal consumption expenditures:<br>Durablegoods|2<br>FRED|Y|
|PCENDG|Personal consumption expenditures:<br>Nondurablegoods|2<br>FRED|Y|
|PCES|Personal consumption expenditures:<br>Services|2<br>FRED|Y|
|PINCOME|Personal income|2<br>FRED||
|PNFI|Private nonresidential fxed invest-<br>ment|2<br>FRED|Y|
|PRFI|Private residential fxed investment|2<br>FRED|Y|
|SLCE|State and local consumption expendi-<br>tures andgross investment|2<br>FRED||
|UNRATE|Unemployment rate|1<br>FRED||
|_Other variables_||||
|CPI|Consumer Price Index for All Urban<br>Consumers:<br>All Items in U.S. City<br>Average (CPIAUCSL)|2<br>FRED|Y|
|SENTIMENT|University of Michigan:<br>Consumer<br>sentiment|2<br>FRED|Y|
|_Housing variables_|**State-level variables**|||
|HOMEOWN_i_|Homeownershiprate|1<br>Haver|Y|
|HOMEVAC_i_|Home vacancyrate|1<br>Haver|Y|
|HPI_i_|All-transactions house price index<br>(ALSTHPI)|2<br>FRED|Y|
|HPIINC_i_|House price-to-income ratio calcu-<br>lated bydividingHPI<br>~~i~~byINC_i_|1<br>Own calculations||



31 

Table B.1: Data and transformations 

|Code|Description<br>|Transfor|m.<br>Source|PCA|
|---|---|---|---|---|
|HPIRENT_i_|House price-to-rent ratio calculated<br>bydividingHPI<br>~~i~~byRENT_i_|1|Own calculations||
|HSTARTS_i_|New privately-owned housing units<br>started|3|Haver|Y|
|PERMITS_i_|New private housing units autho-<br>rized by building permit (ALBP-<br>PRIVSA)|3|FRED|Y|
|RENT_i_|State-level aggregation of the MSA-<br>level rent index (interpolated with<br>Denton<br>method<br>using<br>rent<br>of<br>primary<br>residence<br>from<br>US<br>CPI:<br>CUSR0000SEHA)|2|Howard and<br>Liebersohn(2021)|Y|
|RENTVAC_i_|Rental vacancyrate|1|Haver|Y|
|_Financial variables_|||||
|BA_i_|Total assets for commercial banks<br>(ALTAST)|2|FRED|Y|
|FORECL_i_|All foreclosures started|2|Haver|Y|
|MDR_i_|All mortgagespast due (in %)|1|Haver|Y|
|MORTDEBT_i_|State-level mortgage debt per capita<br>(interpolated with Denton method<br>usingUS data)|2|Haver|Y|
|NBBANK_i_|Nonbusiness bankruptcyflings|2|Haver|Y|
|NPL_i_|Nonperforming loans (past due 90+<br>days plus nonaccrual) to total loans<br>for banks: ALNPTL)|1|FRED|Y|
|ROA_i_|Return on average assets for banks<br>(ALROA)|1|FRED|Y|
|_Real variables_|||||
|GOVEXP_i_|Total governmental state expendi-<br>ture taken from the Annual Survey<br>of State Government Finances (inter-<br>polated with Denton method using<br>US government total expenditures:<br>W068RCQ027SBEA)|2|US Census Bureau|Y|
|GOVREV_i_|State tax collections:<br>Total taxes<br>(QTAXTOTALQTAXCAT3ALNO)|2|FRED|Y|
|GDP_i_|Real GDP. Starting 2005q1 ALRQGSP<br>for Alabama. Before 2005q1 interpo-<br>lated with Denton method with using<br>US real GDP (GDPC1).|2|FRED|Y|
|INC_i_|Personal income (ALOTOT)|2|FRED|Y|
|NFC_i_|All employees:<br>construction (AL-<br>CONS)|2|FRED|Y|
|NFP_i_|All<br>employees:<br>Total<br>nonfarm<br>(ALNA)|2|FRED|Y|



32 

Table B.1: Data and transformations 

|Code|Description<br>|Transfor|m.<br>Source|PCA|
|---|---|---|---|---|
|STATEDEFL_i_|State-level<br>GDP<br>defator<br>(before<br>2005q1 calculated based on interpo-<br>lated nominal and real GDP)|2|FRED|Y|
|STATEINFL_i_|State-level infation|1|Hazell et al.(2022)||
|STATEPCE_i_|State-level personal consumption ex-<br>penditure: ALPCE (interpolated with<br>Denton method usingUS data)|2|FRED|Y|
|UEB_i_|State-level<br>unemployment<br>benefts<br>(ALOBEN)|2|FRED|Y|
|UR_i_|State-level<br>unemployment<br>rate<br>(ALUR)|1|FRED|Y|
||**State-level variables for cross-sectional**|**regress**|**ion**||
|Debt gap|Calculated by applying theHamilton<br>(2018) flter to the state-level mort-<br>gage debt-to-income series, using the<br>standard values for quarterly vari-<br>ables (p= 1 and h = 20)|1|Own calculations||
|HPI growth|Cumulative growth of the real house<br>price index over 1999–2019|1|Own calculations||
|HW (avg.)|Average housing wealth over 1999–<br>2019. HW = (Homeownership rate x<br>Housing units) x HPI x Median house<br>price in 2000|1|Own calculations||
|HW (std.)|Standard deviation of housing wealth<br>over 1999–2019|1|Own calculations||
|LRI|Land-use regulation index (in 2014)|1|Herkenhoff et al.<br>(2018)||
|Manufacturing|Share of manufacturing in state-level<br>GDP|1|Own calculations,<br>Bureau of<br>Economic<br>Analysis||
|RTW|Dummy<br>variable<br>for<br>states<br>with<br>right-to-work legislation|1|National Right to<br>Work Legal<br>Defense||
||||Foundation||
|Sand state|Dummy variable for Arizona, Cali-<br>fornia, Florida, and Nevada|1|Own calculations||
|Small frms|Share of employees in frms with less<br>than 250 employees divided by to-<br>tal number of employees in that state<br>(average over 1999–2019)|1|Own calculations,<br>US Bureau of<br>Labor Statistics||



33 

Table B.2: Values of selected state characteristics (sample averages) 

|State|LRI|Debtgap|HW (avg.)|HW (std.)<br>|Sand state|RTW<br>|Manufacturing|Small frms|HPIgrowth|
|---|---|---|---|---|---|---|---|---|---|
|AL|-1.6|10.0|34575.3|2680.8|0|1|16.9|77.2|3.0|
|AK|–|20.9|46293.9|3970.5|0|0|2.9|77.2|10.7|
|AZ|-0.9|58.7|48327.7|11721.2|1|1|10.0|66.1|17.7|
|AR|-2.6|3.2|23412.1|1671.7|0|1|16.8|73.6|3.6|
|CA|-0.3|76.7|95388.2|23708.3|1|0|12.1|75.3|26.8|
|CO|-0.7|47.6|83949.5|10840.5|0|0|7.5|78.8|22.1|
|CT|-0.3|19.0|88095.2|13926.8|0|0|13.5|75.1|3.5|
|DE|-0.7|33.8|82772.9|12971.6|0|0|7.7|69.5|9.5|
|FL|-1.0|39.1|53897.7|13862.7|1|1|5.4|74.2|21.4|
|GA|-1.4|32.2|43434.8|6194.0|0|1|11.7|73.5|6.7|
|HI|–|55.8|123974.9|27701.1|0|0|2.0|75.9|26.7|
|ID|-1.3|33.9|41584.8|6466.8|0|1|12.5|80.9|18.7|
|IL|-1.6|24.6|56062.8|7630.4|0|0|13.4|68.3|0.4|
|IN|-2.6|11.5|35715.6|2911.5|0|1|28.1|70.6|1.0|
|IA|-3.7|8.9|30652.7|1624.2|0|1|19.4|75.0|4.7|
|KS|-2.8|5.2|27845.3|2285.8|0|1|15.7|74.7|6.1|
|KY|-2.5|8.3|34795.7|2447.1|0|1|18.9|74.6|4.9|
|LA|-1.6|5.5|27668.1|3156.1|0|1|19.9|79.0|9.1|
|ME|-1.1|17.5|77794.9|9091.6|0|0|10.7|80.1|15.8|
|MD|-0.4|45.1|81152.2|15671.4|0|0|6.1|77.6|14.5|
|MA|-0.2|29.8|146481.5|20720.6|0|0|11.2|71.8|18.3|
|MI|-2.4|22.2|53730.8|8098.9|0|0|19.9|68.3|-0.9|
|MN|-1.4|33.6|61391.1|8284.7|0|0|14.4|70.7|12.3|
|MS|-2.3|-1.5|23941.7|1641.5|0|1|16.0|74.9|1.6|
|MO|-2.1|12.3|36887.9|3089.4|0|0|13.4|73.6|5.9|
|MT|-1.0|15.2|45454.9|5232.7|0|0|6.3|90.7|19.2|
|NE|-3.9|8.8|32839.0|1876.8|0|1|11.7|73.7|6.7|
|NV|-1.4|70.6|46727.7|14477.1|1|1|4.2|65.9|14.6|
|NH|-0.4|29.5|82126.1|12054.2|0|0|12.0|79.6|15.9|
|NJ|-0.3|26.8|98786.8|17296.3|0|0|10.2|73.7|13.2|
|NM|-1.0|18.9|39574.8|4350.5|0|0|7.0|79.7|5.1|
|NY|-0.9|14.6|84779.7|12255.1|0|0|5.8|68.8|17.5|
|NC|-1.2|16.3|47495.6|3983.4|0|1|20.7|75.4|6.7|
|ND|-3.6|-0.1|28846.2|3621.0|0|1|7.7|82.3|19.1|
|OH|-2.4|11.0|38901.0|4479.3|0|0|18.3|73.1|-1.9|
|OK|-3.0|-2.8|19922.3|981.3|0|1|10.8|77.6|7.7|
|OR|-0.7|34.3|75455.6|11661.2|0|0|16.1|80.4|20.1|
|PA|-1.1|6.2|51352.5|4847.8|0|0|13.8|73.0|10.6|
|RI|-0.5|31.0|78369.0|15649.9|0|0|9.5|78.4|17.2|
|SC|-1.2|17.3|44551.8|3875.8|0|1|17.3|74.9|8.4|
|SD|-3.4|13.8|33969.7|3052.4|0|1|9.9|80.8|13.4|
|TN|-1.4|10.5|37205.9|3138.8|0|1|16.5|69.3|9.9|
|TX|-2.6|4.8|21499.6|2044.7|0|1|13.9|72.8|17.9|
|UT|-0.9|40.6|57734.2|7684.4|0|1|12.1|76.0|15.0|
|VT|-1.1|10.4|76772.0|10910.2|0|0|11.6|80.3|14.2|
|VA|-0.7|42.4|67313.7|9866.5|0|1|9.8|75.6|16.1|
|WA|-0.6|34.6|90072.7|15094.9|0|0|13.2|76.0|22.9|
|WV|-2.8|-1.6|24635.9|1759.7|0|1|10.9|79.9|1.8|
|WI|-1.8|16.5|50970.8|4821.8|0|1|20.2|72.6|5.5|
|WY|-1.3|7.9|34747.0|4277.5|0|1|5.8|89.5|17.6|



**Note:** Debt gap is the maximum value over the sample period while HPI growth is the cumulative real growth rate over the sample period. Values in blue (red) indicate states belonging to the top (bottom) decile of the respective characteristic. 

34 

Figure B.1: Dispersion of variables across US states 

























**Note:** Distribution of selected variables across US states. The black line is the median realization, and the grey areas include 30% (35–65 percentile), 60% (20–80 percentile) and 90% (5–95 percentile) of the realizations, going from dark to lighter grey. 

35 

#### **Appendix C: Additional tables and figures** 

_TABLES_ 

Table C.1: Explanatory power of factors for variables 

||Series|_R_<sup>2</sup>|
|---|---|---|
||Non performing loan share: Michigan|0.9790|
||New housing units started: US|0.9789|
|All factors|Mortgage delinquency rate: California|0.9784|
||Non performing loan share: Montana|0.9761|
||Newpermits issued: US|0.9756|
||Non performing loan share: Minnesota|0.9406|
||Mortgage delinquency ratio: California|0.9359|
|Factor 1|<br>Non performing loan share: Florida|0.9340|
||<br>Non performing loan share: Georgia|0.9328|
||Nonperformingloan share: Illinois|0.9300|
||Homeownership rate: Nevada|0.7876|
||Homeownership rate: US|0.7763|
|Factor 2|Homeownership rate: California|0.7066|
||<br>Homeownership rate: Florida|0.6838|
||Homeownershiprate: Colorado|0.6818|
||Rents: Washington|0.6124|
||Rents: Oregon|0.5002|
|Factor 3|Rents: California|0.4986|
||Rents: North Carolina|0.4981|
||Rents: Utah|0.4689|
||Consumer price index: US|0.6005|
||<br>Personal expenditures: US|0.5690|
|Factor 4|Personal expenditures: Ohio|0.5348|
||Personal expenditures: Michigan|0.5256|
||Personal expenditures: Kentucky|0.5251|
||GDP defator: New Hampshire|0.4529|
||Non business bankruptcies: Pennsylvania|0.4201|
|Factor 5|<br>Non business bankruptcies: Texas|0.4190|
||<br>GDP defator: Vermont|0.4174|
||<br>GDP defator: New Mexico|0.4047|
||<br>FFR|0.9728|
||Return on bank assets: Wyoming|0.7094|
|One-year rate|Unemployment rate Virginia|0.6051|
||Unemployment rate: Connecticut|0.6049|
||Unemployment rate: New Mexico|0.6036|



**Note:** List of series that are best explained by the extracted factors, according to the R-squared of a linear regression of the (transformed) series on the respective factor. 

36 

Table C.2: Pairwise correlations with state-level responses after three years 

||GDP|PCE|HPI|Rents|Permits|HOR|HPI/rents|MDR|Mortg. debt|
|---|---|---|---|---|---|---|---|---|---|
|LRI|-0.11|-0.42***|-0.64***|-0.17|-0.33**|-0.02|-0.61***|0.59***|-0.35**|
||(0.47)|(0.00)|(0.00)|(0.27)|(0.02)|(0.91)|(0.00)|(0.00)|(0.01)|
|Debt gap|-0.36***|-0.55***|-0.77***|-0.09|-0.57***|-0.44***|-0.78***|0.62***|-0.76***|
||(0.01)|(0.00)|(0.00)|(0.54)|(0.00)|(0.00)|(0.00)|(0.00)|(0.00)|
|HW (avg.)|0.16|-0.13|-0.54***|-0.07|-0.19|0.13|-0.50***|0.53***|-0.51***|
||(0.27)|(0.37)|(0.00)|(0.63)|(0.19)|(0.35)|(0.00)|(0.00)|(0.00)|
|HW (std.)|-0.11|-0.33**|-0.78***|-0.21|-0.32**|-0.06|-0.73***|0.66***|-0.67***|
||(0.44)|(0.02)|(0.00)|(0.17)|(0.02)|(0.67)|(0.00)|(0.00)|(0.00)|
|Sand state|-0.55***|-0.55***|-0.65***|-0.28*|-0.53***|-0.43***|-0.60***|0.51***|-0.59***|
||(0.00)|(0.00)|(0.00)|(0.06)|(0.00)|(0.00)|(0.00)|(0.00)|(0.00)|
|RTW|-0.33**|-0.16|0.32**|0.01|0.28*|-0.14|0.32**|-0.27*|0.28*|
||(0.02)|(0.27)|(0.02)|(0.96)|(0.05)|(0.33)|(0.03)|(0.05)|(0.05)|
|Manufacturing|-0.05|0.31**|0.55***|0.20|0.04|0.02|0.47***|-0.19|0.45***|
||(0.76)|(0.03)|(0.00)|(0.17)|(0.77)|(0.91)|(0.00)|(0.18)|(0.00)|
|Small frms|0.09|0.04|0.16|0.15|0.49***|0.37***|0.12|-0.42***|0.26*|
||(0.54)|(0.76)|(0.27)|(0.32)|(0.00)|(0.01)|(0.44)|(0.00)|(0.07)|
|HPI growth|-0.01|-0.27*|-0.53***|0.00|0.08|0.07|-0.53***|0.20|-0.45***|
||(0.93)|(0.06)|(0.00)|(0.99)|(0.59)|(0.62)|(0.00)|(0.16)|(0.00)|



**Note:** GDP = Real GDP. PCE = Real personal consumption expenditure. HPI = Real house price index. HOR = Homeownership rate. MDR = Mortgage delinquency rate. LRI = Land-use regulation index of Herkenhoff et al. (2018) for the year 2014. Debt gap = Average of Hamilton-filtered mortgage debt-to-income ratio over 1999-2019. HW (avg.) = Average housing wealth over 1999-2019. HW (std.) = Standard deviation of housing wealth over 1999-2019. Sand state = Dummy variable for Arizona, California, Florida, and Nevada. RTW = Dummy variable for right-to-work states. Manufacturing = Share of manufacturing in state-level GDP. Small firms = Share of small firms in total employment. HPI growth = Growth rate of house prices over 1999-2019. Standard errors in parentheses. _∗ p <_ 0.1, _∗∗ p <_ 0.05, _∗∗∗ p <_ 0.01. 

37 

###### _FIGURES_ 

Figure C.1: Principal components and one-year US treasury rate 













**Note:** Five unobserved factors obtained from the normalized data as described in Table B.1 as well as the single observed factor (one-year treasury rate). 

Figure C.2: Dispersion of additional state-level impulse response functions 







**Note:** See Figure 3. 

38 

Figure C.3: Differences in IRFs across Herkenhoff et al. (2018) LRI: decile averages 



















**Note:** Posterior distribution of the differences between the average (cumulative) IRFs across US states that belong to the top and bottom decile of the respective state characteristic. The shaded area reflects the 68% HDI. 

Figure C.4: Differences in IRFs across the debt gap distribution: decile averages 



















**Note:** See Figure C.3. 

39 

Figure C.5: Differences in IRFs across housing wealth volatility: decile averages 



















**Note:** See Figure C.3. 

Figure C.6: Impulse responses across Herkenhoff et al. (2018) LRI 



















**Note:** Median (cumulative) IRFs across US states after a monetary policy tightening that increases the one-year treasury rate by 25bps. The blue (red) lines with circles (crosses) show the responses of the states belonging to the top (bottom) decile of the respective state characteristic. 

40 

Figure C.7: Impulse responses across the debt gap distribution 



















**Note:** See Figure C.6. 

Figure C.8: Impulse responses across housing wealth volatility 



















**Note:** See Figure C.6. 

41 

Figure C.9: Impulse responses across Herkenhoff et al. (2018) LRI: quintile averages 



















**Note:** Posterior distributions of the average (cumulative) IRFs across US states after a monetary policy tightening that increases the one-year treasury rate by 25bps. The blue (red) line with circles (crosses) indicates the median (over all MCMC draws) of the average responses of the states belonging to the top (bottom) quintile of the respective state characteristic. Shaded areas reflect the 68% HDI. The dashed black line is the median of the average IRFs across all the other states. 

42 

Figure C.10: Impulse responses across the debt gap distribution: quintile averages 



















**Note:** See Figure C.9. 

Figure C.11: Impulse responses across housing wealth volatility: quintile averages 



















**Note:** See Figure C.9. 

43 

Figure C.12: Impulse responses across Herkenhoff et al. (2018) LRI in 2000: decile averages 



















**Note:** See Figure 5. 

Figure C.13: Impulse responses across home values in 2000: decile averages 



















**Note:** See Figure 5. 

44 

Figure C.14: Impulse responses across the house price-to-rent ratio: decile averages 



















**Note:** See Figure 5. 

Figure C.15: Impulse responses for unemployment across state characteristics: decile averages 







**Note:** See Figure 5. 

Figure C.16: Impulse responses of housing wealth across state characteristics: decile averages 







**Note:** See Figure 5. 

45 

Figure C.17: Impulse responses of house vacancy rates across Herkenhoff et al. (2018) LRI: decile averages 





**Note:** See Figure 5. 

Figure C.18: Correlation between land-use restrictions in 2014 (Herkenhoff et al. 2018) and housing wealth per capita (avg. 1999–2019) 





46 

Figure C.19: Correlation between land-use restrictions in 2014 (Herkenhoff et al. 2018) and consumption per capita (avg. 1999–2019) 





Figure C.20: Correlation between land-use restrictions in 2014 (Herkenhoff et al. 2018) and personal disposable income per capita (avg. 1999–2019) 





47 

Figure C.21: Impulse responses of selected banks’ indicators across the debt gap distribution: decile averages 







**Note:** See Figure 5. 

Figure C.22: Correlation between land-use restrictions in 2014 (Herkenhoff et al. 2018) and the debt gap 





48 

Figure C.23: Alternative monetary policy surprises: Swanson (2021) forward guidance 













**Note:** The first row of this figure shows the distribution of the median (cumulative) IRFs across US states after a monetary policy tightening that increases the one-year treasury rate by 25bps. The black line is the median response of all state-level (median) responses. The grey areas include 30% (35–65 percentile), 60% (20–80 percentile) and 90% (5–95 percentile) of the median responses, respectively, going from dark to lighter grey. The second row shows the posterior distributions of the average (cumulative) IRFs across US states. The blue (red) line with circles (crosses) indicates the median (over all MCMC draws) of the average responses of the states belonging to the top (bottom) decile of the land-use restriction index in 2014 (Herkenhoff et al. 2018). Shaded areas reflect the 68% HDI. The dashed black line is the median of the average IRFs across all the other states. 

Figure C.24: Alternative monetary policy surprises: Jaroci´nski and Karadi (2020) 













**Note:** See Figure C.23. 

49 

Figure C.25: Impulse responses across Aastveit et al. (2023) supply elasticities over 1996-2006: decile averages 



















**Note:** See Figure 5. 

Figure C.26: Impulse responses across Aastveit et al. (2023) supply elasticities over 2012-19: decile averages 



















**Note:** See Figure 5. 

50 

Figure C.27: Impulse responses across Saiz (2010) supply elasticities: decile averages 



















**Note:** See Figure 5. 

Figure C.28: Alternative state-level inflation series: Hazell et al. (2022) 

Data: inflation IRFs: inflation IRFs: GDP 







**Note:** See Figures B.1 (first chart) and 3 (second and third chart). 

51 

#### **References** 

- Aastveit, K. A., Albuquerque, B. and Anundsen, A. (2023), ‘Changing Supply Elasticities and Regional Housing Booms’, _Journal of Money, Credit, and Banking_ **55** (7), 1749–1783. 

- Aastveit, K. A. and Anundsen, A. (2022), ‘Asymmetric Effects of Monetary Policy in Regional Housing Markets’, _American Economic Journal: Macroeconomics_ **14** (4), 499–529. 

- Aladangady, A. (2017), ‘Housing Wealth and Consumption: Evidence from Geographically-Linked Microdata’, _American Economic Review_ **107** (11), 3415–46. 

- Albuquerque, B. (2019), ‘One Size Fits All? Monetary Policy and Asymmetric Household Debt Cycles in U.S. States’, _Journal of Money, Credit and Banking_ **51** (5), 1309–1353. 

- Albuquerque, B., Iseringhausen, M. and Opitz, F. (2020), ‘Monetary policy and US housing expansions: The case of time-varying supply elasticities’, _Economics Letters_ **195** , 109471. 

- Albuquerque, B. and Krustev, G. (2018), ‘Debt Overhang and Deleveraging in the US Household Sector: Gauging the Impact on Consumption’, _Review of Income and Wealth_ **64** (2), 459–481. 

- Alpanda, S. and Zubairy, S. (2019), ‘Household Debt Overhang and Transmission of Monetary Policy’, _Journal of Money, Credit and Banking_ **51** (5), 1265–1307. 

- Amaral, F., Dohmen, M., Kohl, S. and Schularick, M. (2024), ‘Interest Rates and the Spatial Polarization of Housing Markets’, _American Economic Review: Insights_ (forthcoming). 

- Amberg, N., Jansson, T., Klein, M. and Picco, A. R. (2022), ‘Five facts about the distributional income effects of monetary policy shocks’, _American Economic Review: Insights_ **4** (3), 289–304. 

- Andersen, H. Y. and Leth-Petersen, S. (2021), ‘Housing Wealth or Collateral: How Home Value Shocks Drive Home Equity Extraction and Spending’, _Journal of the European Economic Association_ **19** (1), 403–440. 

- Anenberg, E. and Ringo, D. R. (2022), ‘The Propagation of Demand Shocks through Housing Markets’, _American Economic Journal: Macroeconomics_ **14** (3), 481–507. 

- Anundsen, A. K. and Heebøll, C. (2016), ‘Supply restrictions, subprime lending and regional US house prices’, _Journal of Housing Economics_ **31** (C), 54–72. 

- Bai, J. and Ng, S. (2002), ‘Determining the number of factors in approximate factor models’, _Econometrica_ **70** (1), 191– 221. 

- Bauer, M. D. and Swanson, E. T. (2023), ‘A reassessment of monetary policy surprises and high-frequency identification’, _NBER Macroeconomics Annual_ **37** , 87–155. 

- Baumeister, C., Liu, P. and Mumtaz, H. (2013), ‘Changes in the effects of monetary policy on disaggregate price dynamics’, _Journal of Economic Dynamics and Control_ **37** (3), 543–560. 

- Ben-David, I., Towbin, P. and Weber, S. (2024), ‘Expectations During the U.S. Housing Boom: Inferring Beliefs from Observables’, _The Review of Economics and Statistics_ (forthcoming). 

- Benmelech, E., Guren, A. and Melzer, B. T. (2023), ‘Making the House a Home: The Stimulative Effect of Home Purchases on Consumption and Investment’, _Review of Financial Studies_ **36** (1), 122–154. 

- Beraja, M., Fuster, A., Hurst, E. and Vavra, J. (2019), ‘Regional Heterogeneity and the Refinancing Channel of Monetary Policy’, _The Quarterly Journal of Economics_ **134** (1), 109–183. 

- Bernanke, B. S., Boivin, J. and Eliasz, P. (2005), ‘Measuring the effects of monetary policy: a factor-augmented vector autoregressive (FAVAR) approach’, _The Quarterly Journal of Economics_ **120** (1), 387–422. 

52 

- Best, M. C. and Kleven, H. J. (2018), ‘Housing Market Responses to Transaction Taxes: Evidence From Notches and Stimulus in the U.K.’, _The Review of Economic Studies_ **85** (1), 157–193. 

- Bhutta, N. and Keys, B. J. (2016), ‘Interest Rates and Equity Extraction during the Housing Boom’, _American Economic Review_ **106** (7), 1742–1774. 

- Bhutta, N. and Ringo, D. (2021), ‘The effect of interest rates on home buying: Evidence from a shock to mortgage insurance premiums’, _Journal of Monetary Economics_ **118** , 195–211. 

- Blake, A. P. and Mumtaz, H. (2012), ‘Applied Bayesian Econometrics for Central Bankers’, _Handbooks, Centre for Central Banking Studies, Bank of England, No. 36_ . 

- Bonifacio, V., Brandao-Marques, L., Budina, N., Csonto, B., Fratto, C., Engler, P., Furceri, D., Igan, D., Mano, R., Narita, M., Omoev, M. and Pasrich, G. K. (2022), Distributional Effects of Monetary Policy, _in_ L. Paganetto, ed., ‘Economic Challenges for Europe After the Pandemic’, Springer Proceedings in Business and Economics, Springer, pp. 187–232. 

- Bosshardt, J., Di Maggio, M., Kakhbod, A. and Kermani, A. (2023), The credit supply channel of monetary policy tightening and its distributional impacts, Working Paper 31464, National Bureau of Economic Research. 

- Calza, A., Monacelli, T. and Stracca, L. (2013), ‘Housing finance and monetary policy’, _Journal of the European Economic Association_ **11** (s1), 101–122. 

- Carlino, G. A. and DeFina, R. H. (1998), ‘The Differential Regional Effects Of Monetary Policy’, _The Review of Economics and Statistics_ **80** (4), 572–587. 

- Carlino, G. A. and DeFina, R. H. (1999), ‘The Diferential Regional Effects of Monetary Policy: Evidence from the U.S. States’, _Journal of Regional Science_ **39** (2), 339–358. 

- Carroll, C. D., Otsuka, M. and Slacalek, J. (2011), ‘How Large Are Housing and Financial Wealth Effects? A New Approach’, _Journal of Money, Credit and Banking_ **43** (1), 55–79. 

- Chan, J. C. and Hsiao, C. Y. (2014), Estimation of Stochastic Volatility Models with Heavy Tails and Serial Dependence, _in_ I. Jeliazkov and X.-S. Yang, eds, ‘Bayesian Inference in the Social Sciences’, Wiley-Blackwell, pp. 155– 176. 

- Chodorow-Reich, G., Guren, A. M. and McQuade, T. J. (2024), ‘The 2000s Housing Cycle with 2020 Hindsight: A Neo-Kindlebergerian View’, _The Review of Economic Studies_ (forthcoming). 

- Christiano, L. J., Eichenbaum, M. and Evans, C. (1996), ‘The Effects of Monetary Policy Shocks: Evidence from the Flow of Funds’, _The Review of Economics and Statistics_ **78** (1), 16–34. 

- Christiano, L. J., Eichenbaum, M. and Evans, C. L. (1999), ‘Monetary policy shocks: What have we learned and to what end?’, _Handbook of Macroeconomics_ **1** , 65–148. 

- Chudik, A. and Kumar, A. (2023), Location, location, location: Mortgage rate impact varies by metro, Technical report, Federal Reserve Bank of Dallas – Dallas Fed Economics. 

- Cloyne, J., Ferreira, C. and Surico, P. (2020), ‘Monetary Policy when Households have Debt: New Evidence on the Transmission Mechanism’, _The Review of Economic Studies_ **87** (1), 102–129. 

- Coibion, O., Gorodnichenko, Y., Kueng, L. and Silvia, J. (2017), ‘Innocent Bystanders? Monetary policy and inequality’, _Journal of Monetary Economics_ **88** (C), 70–89. 

- Cooper, D. H., Luengo-Prado, M. J. and Olivei, G. P. (2022), ‘Monetary policy and regional house-price appreciation’, _International Journal of Central Banking_ **18** (3), 173–227. 

- Corsetti, G., Duarte, J. B. and Mann, S. (2022), ‘One Money, Many Markets’, _Journal of the European Economic Association_ **20** (1), 513–548. 

53 

- Del Negro, M. and Otrok, C. (2007), ‘99 Luftballons: Monetary policy and the house price boom across U.S. states’, _Journal of Monetary Economics_ **54** (7), 1962–1985. 

- Dell’Ariccia, G., Igan, D., Laeven, L. and Tong, H. (2016), ‘Credit booms and macrofinancial stability’, _Economic Policy_ **31** (86), 299–355. 

- Dias, D. A. and Duarte, J. B. (2019), ‘Monetary policy, housing rents, and inflation dynamics’, _Journal of Applied Econometrics_ **34** (5), 673–687. 

- Dias, D. A. and Duarte, J. B. (2022), Monetary policy and homeownership: Empirical evidence, theory, and policy implications, International Finance Discussion Papers 1344, Washington: Board of Governors of the Federal Reserve System. 

- Eggertsson, G. and Krugman, P. (2012), ‘Debt, Deleveraging, and the Liquidity Trap: A Fisher-Minsky-Koo Approach’, _The Quarterly Journal of Economics_ **127** (3), 1469–1513. 

- Ferreira, F. and Gyourko, J. (2012), ‘Heterogeneity in Neighborhood-Level Price Growth in the United States, 19932009’, _American Economic Review_ **102** (3), 134–140. 

- Fischer, M. M., Huber, F., Pfarrhofer, M. and Staufer-Steinnocher, P. (2021), ‘The Dynamic Impact of Monetary Policy on Regional Housing Prices in the United States’, _Real Estate Economics_ **49** (4), 1039–1068. 

- Francis, N., Owyang, M. T. and Sekhposyan, T. (2012), ‘The Local Effects of Monetary Policy’, _The B.E. Journal of Macroeconomics_ **12** (2), 1–38. 

- Fratantoni, M. and Schuh, S. (2003), ‘Monetary Policy, Housing, and Heterogeneous Regional Markets’, _Journal of Money, Credit and Banking_ **35** (4), 557–589. 

- Fu, Y. (1995), ‘Uncertainty, liquidity, and housing choices’, _Regional Science and Urban Economics_ **25** (2), 223–236. 

- Furceri, D., Mazzola, F. and Pizzuto, P. (2019), ‘Asymmetric effects of monetary policy shocks across US states’, _Papers in Regional Science_ **98** (5), 1861–1891. 

- Garriga, C. and Hedlund, A. (2020), ‘Mortgage debt, consumption, and illiquid housing markets in the great recession’, _American Economic Review_ **110** (6), 1603–34. 

- Gertler, M. and Karadi, P. (2015), ‘Monetary Policy Surprises, Credit Costs, and Economic Activity’, _American Economic Journal: Macroeconomics_ **7** (1), 44–76. 

- Ghent, A. C. and Owyang, M. T. (2010), ‘Is housing the business cycle? Evidence from US cities’, _Journal of Urban Economics_ **67** (3), 336–351. 

- Gilchrist, S. and Zakrajˇsek, E. (2012), ‘Credit spreads and business cycle fluctuations’, _American Economic Review_ **102** (4), 1692–1720. 

- Glaeser, E. and Gyourko, J. (2018), ‘The Economic Implications of Housing Supply’, _Journal of Economic Perspectives_ **32** (1), 3–30. 

- Glaeser, E. L. (2019), The Macroeconomic Implications of Housing Supply Restrictions, _in_ R. Nijskens, M. Lohuis, P. Hilbers and W. Heeringa, eds, ‘Hot Property: The Housing Market in Major Cities’, Springer International Publishing, pp. 99–108. 

- Glaeser, E. L. and Gyourko, J. (2005), ‘Urban Decline and Durable Housing’, _Journal of Political Economy_ **113** (2), 345– 375. 

- Glaeser, E. L. and Gyourko, J. (2007), Arbitrage in Housing Markets, NBER Working Papers 13704, National Bureau of Economic Research, Inc. 

54 

- Glaeser, E. L., Gyourko, J., Morales, E. and Nathanson, C. G. (2014), ‘Housing dynamics: An urban approach’, _Journal of Urban Economics_ **81** (C), 45–56. 

- Glaeser, E. L., Gyourko, J. and Saiz, A. (2008), ‘Housing supply and housing bubbles’, _Journal of Urban Economics_ **64** (2), 198–217. 

- Greenwald, D. and Guren, A. M. (2021), Do Credit Conditions Move House Prices?, NBER Working Papers 29391, National Bureau of Economic Research, Inc. 

- Greenwood, R., Hanson, S. G., Shleifer, A. and Sørensen, J. A. (2022), ‘Predictable Financial Crises’, _Journal of Finance_ **77** (2), 863–921. 

- Guren, A. M. and McQuade, T. J. (2020), ‘How Do Foreclosures Exacerbate Housing Downturns?’, _The Review of Economic Studies_ **87** (3), 1331–1364. 

- G¨urkaynak, R. S., Sack, B. and Swanson, E. (2005), ‘Do Actions Speak Louder Than Words? The Response of Asset Prices to Monetary Policy Actions and Statements’, _International Journal of Central Banking_ **1** (1), 55–93. 

- Gyourko, J., Saiz, A. and Summers, A. (2008), ‘A New Measure of the Local Regulatory Environment for Housing Markets: The Wharton Residential Land Use Regulatory Index’, _Urban Studies_ **45** (3), 693–729. 

- Hamilton, J. D. (2018), ‘Why You Should Never Use the Hodrick-Prescott Filter’, _The Review of Economics and Statistics_ **100** (5), 831–843. 

- Hazell, J., Herreno, J., Nakamura, E. and Steinsson, J. (2022), ‘The slope of the Phillips Curve: evidence from US states’, _The Quarterly Journal of Economics_ **137** (3), 1299–1344. 

- Hedlund, A., Karahan, F. and Ozkan, K. M. S. (2016), Monetary Policy, Heterogeneity and the Housing Channel, 2016 Meeting Papers 663, Society for Economic Dynamics. 

- Henderson, J. V. and Ioannides, Y. M. (1983), ‘A model of housing tenure choice’, _The American Economic Review_ **73** (1), 98–113. 

- Herkenhoff, K. F., Ohanian, L. E. and Prescott, E. C. (2018), ‘Tarnishing the golden and empire states: Land-use restrictions and the U.S. economic slowdown’, _Journal of Monetary Economics_ **93** , 89–109. 

- Hern´andez-Murillo, R., Owyang, M. T. and Rubio, M. (2017), ‘Clustered Housing Cycles’, _Regional Science and Urban Economics_ **66** , 185–197. 

- Holm, M. B., Paul, P. and Tischbirek, A. (2021), ‘The transmission of monetary policy under the microscope’, _Journal of Political Economy_ **129** (10), 2861–2904. 

- Howard, G. and Liebersohn, J. (2021), ‘Why is the rent so darn high? The role of growing demand to live in housing-supply-inelastic cities’, _Journal of Urban Economics_ **124** , 103369. 

- Huang, H. and Tang, Y. (2012), ‘Residential land use regulation and the US housing price cycle between 2000 and 2009’, _Journal of Urban Economics_ **71** (1), 93–99. 

- Iacoviello, M. (2005), ‘House prices, borrowing constraints, and monetary policy in the business cycle’, _American Economic Review_ **95** (3), 739–764. 

- Jaroci´nski, M. and Karadi, P. (2020), ‘Deconstructing Monetary Policy Surprises – The Role of Information Shocks’, _American Economic Journal: Macroeconomics_ **12** (2), 1–43. 

- Jaroci´nski, M. and Smets, F. (2008), ‘House Prices and the stance of monetary policy’, _Federal Reserve Bank of St. Louis Review_ **90** (Jul), 339–366. 

- Jord`a, O., Kornejew, M., Schularick, M. and Taylor, A. M. (2022), ‘Zombies at Large? Corporate Debt Overhang and the Macroeconomy’, _The Review of Financial Studies_ **35** (10), 4561–4586. 

55 

- Jord`a, O., Schularick, M. and Taylor, A. M. (2013), ‘When Credit Bites Back’, _Journal of Money, Credit and Banking_ **45** (s2), 3–28. 

- Jord`a, O., Schularick, M. and Taylor, A. M. (2015), ‘Betting the house’, _Journal of International Economics_ **96** (S1), S2– S18. 

- Koeniger, W., Lennartz, B. and Ramelet, M.-A. (2022), ‘On the transmission of monetary policy to the housing market’, _European Economic Review_ **145** , 104107. 

- Koop, G. M. (2003), _Bayesian Econometrics_ , John Wiley & Sons Inc. 

- Korobilis, D. (2013), ‘Assessing the Transmission of Monetary Policy Using Time-varying Parameter Dynamic Factor Models’, _Oxford Bulletin of Economics and Statistics_ **75** (2), 157–179. 

- Mian, A., Sufi, A. and Verner, E. (2017), ‘Household Debt and Business Cycles Worldwide’, _Quarterly Journal of Economics_ **132** (4), 1755–1817. 

- Miranda-Agrippino, S. and Ricco, G. (2021), ‘The transmission of monetary policy shocks’, _American Economic Journal: Macroeconomics_ **13** (3), 74–107. 

- Mumtaz, H., Sunder-Plassmann, L. and Theophilopoulou, A. (2018), ‘The state-level impact of uncertainty shocks’, _Journal of Money, Credit and Banking_ **50** (8), 1879–1899. 

- Mumtaz, H. and Theodoridis, K. (2017), ‘Common and country specific economic uncertainty’, _Journal of International Economics_ **105** , 205–216. 

- Nakamura, E. and Steinsson, J. (2018), ‘High-Frequency Identification of Monetary Non-Neutrality: The Information Effect’, _The Quarterly Journal of Economics_ **133** (3), 1283–1330. 

- Paciorek, A. (2013), ‘Supply constraints and housing market dynamics’, _Journal of Urban Economics_ **77** (C), 11–26. 

- Paul, P. (2020), ‘The Time-Varying Effect of Monetary Policy on Asset Prices’, _The Review of Economics and Statistics_ **102** (4), 690–704. 

- Piazzesi, M. and Schneider, M. (2016), _Housing and Macroeconomics_ , Vol. 2 of _Handbook of Macroeconomics_ , Elsevier, pp. 1547–1640. 

- Pica, S. (2023), Housing markets and the heterogeneous effects of monetary policy across the euro area, Available at https://ssrn.com/abstract=4060424, SSRN. 

- Poterba, J. M. (1984), ‘Tax Subsidies to Owner-Occupied Housing: An Asset-Market Approach’, _The Quarterly Journal of Economics_ **99** (4), 729–752. 

- Rosen, H. S., Rosen, K. T. and Holtz-Eakin, D. (1984), ‘Housing tenure, uncertainty, and taxation’, _The Review of Economics and Statistics_ pp. 405–416. 

- Saiz, A. (2010), ‘The geographic determinants of housing supply’, _The Quarterly Journal of Economics_ **125** (3), 1253– 1296. 

- Saks, R. E. (2008), ‘Job creation and housing construction: Constraints on metropolitan area employment growth’, _Journal of Urban Economics_ **64** (1), 178–195. 

- Schularick, M. and Taylor, A. M. (2012), ‘Credit Booms Gone Bust: Monetary Policy, Leverage Cycles, and Financial Crises, 1870-2008’, _American Economic Review_ **102** (2), 1029–61. 

- Stock, J. H. and Watson, M. W. (2005), Implications of Dynamic Factor Models for VAR Analysis, NBER Working Papers 11467, National Bureau of Economic Research, Inc. 

- Stock, J. H. and Watson, M. W. (2018), ‘Identification and Estimation of Dynamic Causal Effects in Macroeconomics Using External Instruments’, _The Economic Journal_ **128** (610), 917–948. 

56 

Swanson, E. T. (2021), ‘Measuring the effects of federal reserve forward guidance and asset purchases on financial markets’, _Journal of Monetary Economics_ **118** , 32–53. 

Williams, J. C. (2015), ‘Measuring monetary policy’s effect on house prices’, _FRBSF Economic Letter_ **2015-28** . 

Wong, A. (2021), Refinancing and The Transmission of Monetary Policy to Consumption, Working Papers 2021-57, Princeton University. Economics Department. 

57 





6a Circuit de la Foire Internationale L-1347 Luxembourg 



Tel: +352 260 292 0 

www.esm.europa.eu info@esm.europa.eu 

©European Stability Mechanism 2024 

