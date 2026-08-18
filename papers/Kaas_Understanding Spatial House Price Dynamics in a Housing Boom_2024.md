---
title: Kaas_Understanding Spatial House Price Dynamics in a Housing Boom_2024
type: paper
source_pdf: raw/papers/Kaas_Understanding Spatial House Price Dynamics in a Housing Boom_2024.pdf
converted: 2026-08-18
---



## 11286 2024 

August 2024 

# **Understanding Spatial House Price Dynamics in a Housing Boom** 

_Leo Kaas, Georgi Kocharkov, Nicolas Syrichas_ 

###### **<u>Impressum:</u>** 

CESifo Working Papers ISSN 2364-1428 (electronic version) Publisher and distributor: Munich Society for the Promotion of Economic Research - CESifo GmbH The international platform of Ludwigs-Maximilians University’s Center for Economic Studies and the ifo Institute Poschingerstr. 5, 81679 Munich, Germany Telephone +49 (0)89 2180-2740, Telefax +49 (0)89 2180-17845, email office@cesifo.de Editor: Clemens Fuest <u>https://www.cesifo.org/en/wp</u> 

An electronic version of the paper may be downloaded 

· from the SSRN website: <u>www.SSRN.com</u> · from the RePEc website: <u>www.RePEc.org</u> · from the CESifo website: <u>https://www.cesifo.org/en/wp</u> 

CESifo _Working Paper No. 11286_ 

### Understanding Spatial House Price Dynamics in a Housing Boom 

##### Abstract 

We examine the evolution of spatial house price dispersion during Germany’s recent housing boom. Using a dataset of sales listings, we find that house price dispersion has significantly increased, which is driven entirely by rising price variation across postal codes. We show that both price divergence across labor market regions and widening spatial price variation within these regions are important factors for this trend. We propose and estimate a directed search model of the housing market to understand the driving forces of rising spatial price dispersion, highlighting the role of housing supply, housing demand and frictions in the matching process between buyers and sellers. While both shifts in housing supply and housing demand matter for overall price increases and for regional divergence, we find that variation in housing demand is the primary factor contributing to the widening spatial dispersion within labor market regions. 

JEL-Codes: D830, R210, R310. 

Keywords: house price dispersion, spatial housing markets, search frictions in housing markets. 

_Leo Kaas Goethe University Frankfurt / Germany kaas@wiwi.uni-frankfurt.de_ 

_Georgi Kocharkov Deutsche Bundesbank, Frankfurt / Germany georgi.kocharkov@bundesbank.de_ 

_Nicolas Syrichas Free University Berlin / Germany nicolas.syrichas@fu-berlin.de_ 

August 7, 2024 

We thank SAFE (project 21529) for financial support. We also thank Murat Alp Celik, Gueorgui Kambourov, Rachel Ngai, Nawid Siassi, Tuuli Vanhapelto, as well as audiences at EUI, Goethe University Frankfurt, University of Toronto, TU Wien, FAU/IAB Macro Seminar and the 2024 “Search in Housing Markets” Conference at the Imperial College Business School. The views expressed in this paper represent the authors’ personal opinions and do not necessarily reflect the views of the Deutsche Bundesbank or the Eurosystem. 

###### **1 Introduction** 

A striking feature of many housing markets is the large and often rising dispersion of house prices and rents across locations. Spatial dispersion of housing costs has several important social and economic consequences, such as widening wealth inequality between households, increasing residential segregation with spillovers on children’s human capital (Fogli et al., 2023), or regional misallocation of capital and labor with detrimental effects on economic growth (Herkenhoff et al., 2018; Hsieh and Moretti, 2019). The existing literature on widening spatial price dispersion focuses on differences in house prices across metropolitan areas or municipalities (e.g. Van Nieuwerburgh and Weill, 2010; Gyourko et al., 2013), while house price dispersion at more granular levels remains largely unexplored. 

This paper analyzes the trends and determinants of spatial house price dispersion during Germany’s recent housing boom over the period 2009–2018. Different from other industrialized countries, real house prices in Germany did not exhibit any upward trends in the four decades prior to 2010.<sup>1</sup> Since then, however, real house prices increased overall and at varying speeds in different geographic subsamples, as is visible in panel (a) of Figure 1. At the same time, panel (b) illustrates that the spatial dispersion of house prices has widened sharply, even in rural regions where average house prices went up by much less than in urban regions. Also within the relatively homogeneous group of the largest seven metropolitan areas that saw the largest overall increase of house prices, a large increase of spatial price dispersion can be observed. 

After documenting the main empirical patterns of Germany’s housing boom and the simultaneous rise in spatial price dispersion, we build and estimate a simple spatial housing search model whose parameters can be identified from the price, contact-per-listing, and duration data at the postal code level. We use the estimated model to analyze the separate roles of housing supply, housing demand, and matching frictions for the observed price trends. 

In Section 2 we describe a dataset of sales listings from Germany’s largest housing online platform and document the contribution of location to the observed house price trends since the year 2009. We calculate inflation- and quality-adjusted house prices and find that the cross-sectional variance has increased substantially during 2009–2018. We first document that the entire increase of this variance is accounted for by an increase of dispersion between postal codes which we use as our granular location measure (cf. Figure 1.b), whereas within postal codes there is no change of house price dispersion. Second, we dissect spatial price dispersion into between and within labor market region components. For the full sample, the between-region component accounts for about two thirds of the between-location variance 

> 1See Kindermann et al. (2024) for the historic house price development on the basis of different datasets. The doubling of nominal house prices during 1975–1995 shown in their paper is almost exactly offset by a doubling of the CPI during this period. 

1 



<!-- Start of picture text -->
2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018<br>Full sample Top−7 regions Urban Rural Full sample Top−7 regions Urban Rural<br>(a) Mean (b) Variance<br>1.6 2.5<br>1.4 2<br>1.2<br>1.5<br>1<br>1<br><!-- End of picture text -->

Figure 1: Mean and spatial dispersion of house prices 

Notes: House prices are the residuals of hedonic regressions of inflation-adjusted prices in sales listings. Panel (a) shows the mean of these residuals, panel (b) shows the variance across postal codes, where all series are normalized to unity in the year 2009. See Section 2 for further details about the data, calculation of the variables and definition of the geographic subsamples. 

and is responsible for about three quarters of the rise in spatial dispersion. We find similar results when we restrict the sample to only rural or urban regions. When focusing only on the more homogeneous Top-7 labor market regions, we find that rising dispersion within labor market regions accounts for about a half of the overall increase. We further document an overall tightening of the housing market, as evidenced by a decline of the duration of a listing and a substantial increase of the contact-per-listing-day ratio, which point to a surge of housing demand during the observation period. 

In Sections 3 and 4, we propose and estimate a spatial housing search model that helps to understand the separate roles of demand, supply and matching frictions for rising spatial price dispersion, both between and within labor market regions. The model features homogeneous buyers and sellers whose house price valuations vary across space and over time. We further introduce time-invariant location premia that control the average market shares at the location level. While sellers choose the number of listings and the posted prices, buyers decide in which locations to search and which sellers to contact. In line with standard competitive search theory (cf. Moen, 1997), both sellers and buyers trade off prices and matching probabilities. 

Importantly, our housing search model is a highly stylized, not fully structural approach to describe price setting and price variation in spatial housing markets. While abstracting from the underlying reasons for demand or supply changes, a key advantage of our model is 

2 

that all structural parameters can be uniquely identified on the basis of our house listings data. Thus, the model serves the purpose to quantify the respective contributions of demand, supply and market frictions for the observed house price dynamics. 

In the equilibrium of our model, prices, listing duration and tightness in a local housing market respond to the time and space variation of buyers’ and sellers’ house valuations and to a rent-sharing term that reflects housing market frictions. While the buyer valuation stands for the willingness to pay in certain locations, the seller valuation represents the outside option of a housing unit for sale which may reflect the construction cost of a new unit or the outside value of renting out an existing unit.<sup>2</sup> These two components capture the contributions of housing demand and supply, respectively. Additionally, differential trends in house prices could reflect differences in buyer-seller rent sharing between housing locations. Although ubiquitous in labor economics, this channel is mostly absent in the quantitative housing literature. Rent sharing here refers to the additional compensation that buyers pay in excess of the reservation price of sellers. In hot housing markets, sellers may exert more bargaining power over their buyers. 

The model estimation uses a two-step procedure. First, we estimate matching functions on the basis of duration and contact-per-listing data. These parameters are estimated separately for each labor market region, where matching efficiency is additionally allowed to vary over time. The latter is required by our data which indicate an increase of matching efficiency in the second half of our observation period in most labor market regions. The second step is to jointly estimate the time- and location-specific valuations of buyers and sellers as well as the time-invariant location premia, using our data on prices, tightness, the estimates of matching functions, and the market shares. Within larger labor market regions, our model has several thousand parameters that include over 100 postal codes and 40 quarters. Nonetheless, this estimation step can be performed rather efficiently since our model is linear in nearly all parameters that are estimated at the second step. 

In Section 5 we use the estimated model to quantify the driving forces behind the observed house price dynamics during the period 2009–2018. Through the lens of the model, three factors generate variation in house prices over time: housing supply via the valuation of sellers, housing demand via the valuations of buyers, or rent sharing between buyers and sellers which reflects trends in matching frictions and changes in market tightness. A simple counterfactual exercise is used to quantify the respective contribution of each of these factors for the increasing trend of house prices and their dispersion in the Top-7 labor market regions and for the between- and within-region variation. 

> 2Regulatory constraints and geographic barriers could impose hurdles in some premium locations driving sellers’ valuations up (e.g. Saiz, 2010; Hsieh and Moretti, 2019). 

3 

We find that the majority of the rise of house prices in the Top-7 regions is accounted for by stronger housing demand, which accounts for around 80 percent of the price increase. Changes in supply have a secondary impact on the increase of prices, whose contribution to the overall increase varies between 5 and 30 percent. The rent-sharing factor has only a minor effect on the evolution of prices in any of the Top-7 labor market regions. House price dispersion increases in all but one region (Berlin) throughout the period 2009-2018. Rising within-region dispersion is mostly accounted for by differential changes in demand, while supply and rent sharing play a rather modest role. 

We also use the estimated model to decompose the between-location variance into withinand between-region components, paralleling our data decomposition of Section 2. Similar to our findings for the Top-7 regions, the majority of within-region dispersion is attributed to demand-side changes. Nonetheless, a sizable share of between-region divergence is accounted for by housing supply, which possibly reflect the expansion of construction activity in relatively less demanded regions during this period. Changes in rent sharing have little impact on within-region dispersion and even a dampening effect on the rise of between-region price differences. The latter can be explained by the regional convergence of housing market tightness over time. 

###### **1.1 Related Literature** 

**Spatial dispersion.** Our work relates to Van Nieuwerburgh and Weill (2010) and Gyourko et al. (2013), who study reasons why house price dispersion across U.S. metropolitan areas increased over time. Van Nieuwerburgh and Weill (2010) use a dynamic spatial equilibrium model in the spirit of Rosen (1979) and Roback (1982) to show that high-ability households move into metropolitan areas with high wages and stringent regulatory housing supply. Likewise, Gyourko et al. (2013) argue that house price differentials in large metropolitan cities can be attributed to inelastic supply combined with an increasing sorting of highincome households. Our article differs from these two studies in two dimensions. First, we consider house price variation at a much more granular level. In particular, we show that house prices exhibit increasing dispersion over time, not only across labor market regions (i.e metropolitan areas) but also at the postal code level within labor market regions. Second, to use information on listing duration and contact-per-listing data, we employ a spatial directed search matching model that accounts for frictions in local housing markets instead of the frictionless island-type model of Van Nieuwerburgh and Weill (2010). 

Our paper is related to recent empirical studies explaining differential house price trends during a housing boom. Kindermann et al. (2024) study regional disparities in house prices across German labor markets in the same ten-year period, focusing on the role of regional differences in expectation formation. Amaral et al. (2024) study the relationship between 

4 

price and rent divergence across metropolitan areas in 15 advanced economies during a period of low-interest rates. They find that house prices have increased at a much faster pace compared to rents, both in major metropolitan areas but also on the national level. Again the focus of this paper is on house price trends at a more granular spatial level. While we do not consider rents in our main analysis, we document in Appendix D, Tables D.1D.4 and Figure D.1, that rent dispersion has also increased over time across postal codes, especially within the Top-7 labor market regions. 

**Housing market search.** On the modelling side our paper relates to a literature employing directed search models to explain salient features of housing markets (Albrecht et al., 2016; Hedlund, 2016; Rekkas et al., 2022; Moen et al., 2021; Jiang et al., 2024; Garriga and Hedlund, 2020). Closest to our work is Rekkas et al. (2022) who use a directed search model with heterogeneous buyers which they estimate using listings data from the Vancouver area. Similar to us, they find that heterogeneous tastes of buyers explain much of house price dispersion, whereas search frictions matter only little for dispersion (although contribute to the price stickiness observed in their data). Our paper mainly differs in two dimensions. First, we use our model to disentangle the respective contributions of buyers’ and sellers’ valuations, next to search frictions, for house price dynamics. Second, we seek to explain the factors that account for spatial dispersion between and within labor market regions. 

Another closely related paper is Vanhapelto and Magnac (2024) who utilize listings and transactions data from Finland to estimate a model of segmented housing search. In their model, better liquidity in some markets is either due to higher matching efficiency or to differences in popularity among buyers (market tightness). Model-based results show that differences in market tightness contribute more to explaining differences in liquidity across markets than differences in matching technology. Our paper is different because it deals with the evolution of price dispersion across time and space. Moreover, we evaluate both supply and demand changes along with matching efficiency changes for the observed dynamics of house prices. 

Our paper further relates to a literature that uses online listings data to study the role of imperfect and costly information frictions to house price variation (Ben-Shahar and Golan, 2022; Jiang et al., 2024; Guren, 2018). Our paper differs from this literature in its focus on the structural factors that explain residual variation across locations, rather than frictions that generate variation in the prices of similar houses within locations. 

5 

###### **2 Empirical Patterns** 

###### **2.1 Data** 

We use sales listings of residential housing units in Germany that were posted at the online platform _ImmobilienScout24_ during January 2009 and December 2018.<sup>3</sup> The raw data are further prepared, geo-referenced and labeled by the RWI Essen within the RWI-GEO-RED dataset which can be accessed for research purposes. Next to the posted prices, the dataset contains a large number of housing characteristics, including geographical location at the square-kilometer level. It further contains information on the duration of a listing in days, the number of views that a listing received and the number of contact attempts of potential buyers. 

A limitation of these data is that only listed prices are available, but not the actual transaction prices. However, comparing posted prices aggregated at the city level with the newly created German Real Estate Indices (GREIX) across cities, we find striking similarities of the levels and the evolution of these two series over time.<sup>4</sup> Moreover, earlier studies using both transaction and listing price data show that on average a property sells within 1.6% of its listed price (Guren, 2018). Nonetheless, we do observe if the same property has been listed multiple times within a short horizon with marginal changes. In those cases, we keep only the last listing.<sup>5</sup> For further details about the data, data cleaning procedures, and the number of listings across time and space, see Appendix A. 

###### **2.2 Hedonic Regressions** 

Since we are interested in spatial variation of house prices over time, rather than changes in the composition of housing units for sale, we control for any observable differences in the characteristics of these housing units. To this end, we estimate a standard hedonic house price regression for our sample of sales listings. We pool all observations and estimate the OLS regression 



> 3 _ImmobilienScout24_ is the largest real estate listing website in Germany with a self-reported market share of over 50 percent (Georgi and Barkow, 2010). 

> 4See Appendix C for further details. 

> 5Another issue is the presence of phishing or fraud listings which usually look like legitimate listings, often at below market prices to attract potential buyers. _ImmobilienScout24_ has developed a sophisticated algorithm to detect and remove those listings. It is also a fee-based platform, so that the cost for listing a fake offer is high. To alleviate remaining concerns, we remove ultra-popular offers (i.e. listings with hits or contacts beyond the 99th percentile) in our data cleaning process. 

6 

where log _pht_ is the (log) inflation-adjusted listed price per _m_<sup>2</sup> of housing unit _h_ posted at time _t_ , _Xht_ is a vector of housing characteristics of that property which includes a set of categorical variables for the number of rooms, dummy variables for guest toilet and cellar, age of the property in five-year categorical intervals, 22 categories indicating the type of the property, and quarterly dummies to take care of seasonal variation. Appendix B provides further details about the control variables. 

We are interested in the residuals _εht_ of this hedonic regression which we aggregate at the location level in a quarterly panel. Note that these residuals include not only location premia but also their variation over time. 

###### **2.3 Baseline Sample** 

Since we are interested in the spatial distribution of house prices and its changes over time, we construct a quarterly panel which builds on postal codes as our main geographical unit.<sup>6</sup> We restrict the sample to those postal codes that contain at least ten listing observations in all quarters of our ten-year period. 

As a larger aggregate geographic unit, we use the labor market regions categorized by Kosfeld and Werner (2012). These regions, which usually combine several municipalities and districts, are characterized according to commuter links to local labor market centers. Since some rural labor market regions are not well represented, we drop all labor market regions with less than 14 postal codes. 

Both restrictions mitigate the impact of regions or postal codes which are sparsely populated and contain only few listings. In the following, we refer to postal codes as _locations_ , while _regions_ denote the labor market regions in our classification. The final balanced panel contains 2,161 locations in 99 regions over 40 quarters. It is important to note that none of our empirical findings is sensitive to these sample restrictions. 

###### **2.4 Descriptive Statistics** 

Table 1 shows descriptive statistics of our baseline sample, reporting the means of selected variables, separate for five two-year periods. The first two rows illustrate the sharp rise in house prices over the ten-year horizon. The average inflation-adjusted house listed for sale in the 2009-2010 period cost around e1451 per _m_<sup>2</sup> . Ten years later the posted sales price increased around 36% to e1978 per _m_<sup>2</sup> . Note that this increase cannot be attributed to changes in housing characteristics, as the hedonic house prices _εt_ exhibit a similar increase 

> 6Relative to the _km_ 2 grid information provided in the RWI-GEO-RED data, postal codes are larger and more homogeneous in population size. Germany has about 40.9m households and 8,200 postal code locations, so that a postal code includes on average about 5,000 households. 

7 

as the raw prices (in log points). When restricted to the largest seven labor market regions, house prices grew by 58% (from e1863 to e2951 per _m_<sup>2</sup> ), indicating a widening of crossregional house price dispersion which we elaborate on in the next section.<sup>7</sup> 

The bottom four rows of Table 1 indicate a tightening of the German housing market over the same period. The average number of listings in a location per quarter decreased by 35 percent, while the average duration of a listing fell from 56 to 45 days, and the number of contacts (i.e. buyers clicking the contact button) increased by 73 percent. The last row reports the number of contacts per listing day as a flow-based measure of housing market tightness. This number almost quadrupled which indicates a substantial tightening of the German housing market over this ten-year period.<sup>8</sup> 

Table 1: Descriptive statistics 

|Variable|2009-10|2011-12|2013-14|2015-16|2017-18|
|---|---|---|---|---|---|
|Log price ln_p_|7.28|7.29|7.35|7.48|7.59|
|Price residual _ε_|-0.13|-0.12|-0.07|0.03|0.17|
|Listings _S_|71|69|73|58|46|
|Duration in days _d_|56|52|44|48|45|
|Contacts _C_|169|209|280|305|292|
|Flow tightness<br>_C_<br>_dS_|0.05|0.07|0.11|0.16|0.19|
|Observations|17,288|17,288|17,288|17,288|17,288|



Notes: Means of selected variables for the baseline sample of location-quarter observations. Prices are in euros and adjusted for inflation using the CPI of the federal states in Germany. 

###### **2.5 House Price Dispersion Across Space and Time** 

Not only has the average house price gone up during 2009-2018, there is also a substantial widening of house price dispersion over the same period. To document this phenomenon, we go back to the level of individual listings and consider the residual posted price per _m_<sup>2</sup> , 

> 7Tables D.1 and D.2 in Appendix D display similar patterns for the rental market. Listed rents per _m_ 2 increased by 18 log points all over Germany and by 23 log points in the Top-7 labor market regions over the same period. 

> 8Trends in the absolute number of listings _S_ and contacts _C_ may principally reflect changes in the market share of _ImmobilienScout24_ over this ten-year period that could also vary between locations. However, to the extent that this platform is representative of the German housing market, such changes in market shares should not matter for the other two measures, namely listing duration _d_ and flow tightness _C/_ ( _dS_ ). Our identification strategy in Section 4 uses only these latter two variables. Hence, it builds on the assumption of representativeness of the platform, regardless of potential changes in its market share (between locations or over time). 

8 

denoted _εht_ for listing _h_ at time _t_ , as obtained from the hedonic regression described above. Across listings, the variance of residual prices has increased by over 50 percent, see Table 2. 

To understand the spatial dimension of rising dispersion, we first decompose the variance of residual prices into within- and between-location components.<sup>9</sup> Suppressing the time index, the variance of residual prices is split into 



where _L_ is the set of locations (postal codes) with index _i_ , _ε_ ¯ _i_ = _n_ <u>1</u> _i_ � _nh_ =1 _i_<sup>_εh_istheaver-</sup> age residual price in location _i_ with number of listings _ni_ , and _si_ = _ni/_ (<sup>�</sup> _j∈L_<sup>_nj_)isthe</sup> ¯ listing share of location _i_ . _ε_ is the average residual price across all of Germany. The within-location term on the right-hand side is the listing-weighted average of the variances var _i_ ( _εh_ ) = _n_ <u>1</u> _i_ � _nh_ =1 _i_<sup>(</sup><sup>_εh−ε_¯</sup><sup>_i_)2 over all locations</sup><sup>_i_.The second term is the listing-weighted vari-</sup> ance of location-level prices, i.e. the between-location variance. We calculate this additive decomposition separately for each year. 

Table 2: Within- and between-location variance decomposition 

||Tot|al varia|nce|With|in loca|tions|Betw|een loca|tions|
|---|---|---|---|---|---|---|---|---|---|
||2009|2013|2018|2009|2013|2018|2009|2013|2018|
|**Full sample**|0.190|0.237|0.290|0.115|0.113|0.111|0.075|0.123|0.179|
|**West Germany**|0.187|0.234|0.283|0.114|0.112|0.107|0.073|0.122|0.176|
|**East Germany**|0.188|0.239|0.295|0.132|0.136|0.161|0.055|0.103|0.134|
|**Top-7 regions**|0.184|0.199|0.230|0.115|0.101|0.091|0.069|0.098|0.139|
|**Urban**|0.193|0.246|0.298|0.117|0.114|0.109|0.077|0.132|0.189|
|**Rural**|0.180|0.208|0.265|0.111|0.113|0.114|0.069|0.095|0.151|



Notes: “Full sample” contains the listings in all quarter-location observations in our baseline sample. “West Germany” and “East Germany” include all listings located in districts (NUTS-3) which belonged to the FRG or GDR, respectively, before the German reunification. The “Top-7 regions” comprise the labor market regions of Berlin, Munich, Hamburg, Frankfurt am Main, Cologne, Stuttgart and Dusseldorf. “Urban” denotes all units belonging to a district indicated either as “Kreis”, “Kreisfreie Stadt” or “Stadtkreis” and “Rural” all housing units located in a “Landkreis”. 

> 9We also perform the variance decompositions in (2) and (3) with the raw prices instead of the price residuals and obtain rather similar results. 

9 

Table 2 reports the three terms in equation (2) separately for the years 2009, 2013 and 2018. Starting from the full sample, we see that the entire increase in variance is accounted for by the between-location component which increased steeply during 2009– 2018, whereas the average within-location variance has not changed over time. In fact, while the within-location variance accounts for about 60 percent of the total variance in 2009, it merely contributes 38 percent to overall house price dispersion in 2018. Focusing on different geographic subsamples, this result is largely robust with some minor differences. In East German locations, house price dispersion has also gone up within locations, possibly reflecting rising disparities between unrenovated and modernized housing units (a housing characteristic that we cannot control in the hedonic regressions). In contrast, within urban and Top-7 locations, within-location dispersion has fallen, so that more than the entire increase of the variance is due to the between-location component. 

The rising spatial dispersion of house prices is also illustrated in Figure 2 which shows the distribution of residual posted prices, averaged at the postal code level, in the four years 2009, 2012, 2015 and 2018. During 2009–2015, the mode of these distributions remains rather stable, while the rise of the average house price is driven by a widening of house prices in the upper half of the distribution. During 2015–2018, the bottom half of the distribution has also widened substantially. 



Figure 2: Distribution of residual prices across locations 

Notes: Between-location distributions of residual log prices in the years 2009 (blue), 2012 (orange), 2015 (green) and 2018 (red). The residuals are obtained from hedonic house price regressions as described in the main text and averaged in each location (postal code). 

10 

In light of the important role of location for rising house price dispersion, we are now asking to what extent these trends are driven by house price divergence between labor market regions or rising differences between locations within these regions. To do so, we decompose the between-location variance (i.e., the last term in equation (2)) into a betweenand within-region component, 



where _R_ is the set of regions, _σr_ =<sup>�</sup> _i∈r_<sup>_si_is the listing weight of region</sup><sup>_r_, and</sup><sup>_ε_¯</sup><sup>_r≡_�</sup> _i∈r σsri_<sup>_ε_¯</sup><sup>_i_</sup> is the mean residual price of region _r_ . The first term is the listing-weighted average of the within-region variances var _r_ (¯ _εi_ ) _≡_<sup>�</sup> _i∈r σsri_<sup>(¯</sup><sup>_εi−ε_¯</sup><sup>_r_)2,sothatthistermmeasurestowhat</sup> extent spatial house price differences are accounted for by differences between locations within labor market regions. The second term is the listing-weighted variance of average regional prices, i.e. the between-region variance. As before, this decomposition is calculated separately for each year. See Appendix E for derivations of the variance decompositions in equations (2) and (3). 

Table 3: Within- and between-region variance decomposition 

||Betwee|n-locatio|n variance|Wit|hin regi|ons|Bet|ween reg|ions|
|---|---|---|---|---|---|---|---|---|---|
||2009|2013|2018|2009|2013|2018|2009|2013|2018|
|**Full sample**|0.075|0.123|0.179|0.032|0.048|0.054|0.043|0.076|0.125|
|**West Germany**|0.073|0.122|0.176|0.032|0.047|0.055|0.041|0.075|0.121|
|**East Germany**|0.055|0.103|0.134|0.031|0.053|0.048|0.024|0.049|0.086|
|**Top-7 regions**|0.069|0.098|0.139|0.044|0.060|0.073|0.025|0.037|0.066|
|**Urban**|0.077|0.132|0.189|0.034|0.049|0.053|0.043|0.083|0.136|
|**Rural**|0.069|0.095|0.151|0.018|0.027|0.033|0.051|0.068|0.118|



Notes: See the notes to Table 2 for definitions of the different samples. 

Table 3 shows the results of this decomposition for different years and geographic units. Two interesting patterns emerge. First, in the full sample about 70 percent of the house price variance between locations in the year 2018 is accounted for by the between-region variance. Moreover, over three quarters of the rise in house price dispersion during 2009 and 2018 is driven by an increase in the variance of house prices between labor market regions, while less than a quarter of the increase is attributed to greater house price dispersion within labor 

11 

market regions. Similar results are observed for the West and East German subsamples, and also if we divide the sample into rural and urban regions. On the other hand, zooming into the Top-7 subsample, we find that almost half of the increase in variance is driven by diverging house prices within the labor market regions. Furthermore, the within-location component accounts for the majority of overal spatial dispersion. Intuitively, labor market regions in this subsample are more comparable, so that a greater share of the variance (and its increase) is accounted for by the within-region variance (and its increase).<sup>10</sup> 

These empirical patterns do not, of course, settle the question of what caused rising house prices and a widening of spatial house price dispersion in the first place. In Section 5 we revisit this decomposition through the lens of our structural model that we estimate on our data and that sheds light on the relative role of demand, supply and rent-sharing factors for the observed house price developments. 

###### **3 Model** 

We propose a simple model that can be estimated on our data so as to analyze the driving forces behind the diverging house price trends documented in the last section. In particular, we aim to quantify the respective roles of supply, demand and rent-sharing shifters in house prices at the location, region and aggregate level during the ten-year horizon covered in our data. The model describes a given labor market region that is divided into locations (postal codes). In each location, potential sellers decide about entry and the posted price of the housing unit for sale. Buyers decide in which location to search and which sellers to contact at their posted prices where trade is subject to search frictions. The housing market is characterized by directed search (Moen, 1997; Wright et al., 2021), while location decisions respond to taste shocks that are common in spatial dynamic choice models (e.g. Aguirregabiria and Mira, 2010; Caliendo et al., 2019). House prices and housing market tightness endogenously depend on the time and space variation of buyers’ and sellers’ housing valuations. 

We deliberately keep the model parsimonious, abstracting from tenure choice, mortgage financing, differentiation of housing units by size or quality, and migration between labor market regions. While these simplifications leave out many important aspects of housing 

> 10In Appendix D, Tables D.3-D.4 and Figure D.1, we repeat the analysis of this section for the rental market where the increase in dispersion over this ten-year period is less pronounced than in the sales market. Similarly to house prices, we find that most of the increase in variance is attributed to rising disparities across locations (postal codes), although rental dispersion also increases within locations. Furthermore, as for house sales, the increase in the cross-location variance is attributed to both within-region and betweenregion components where the latter plays a more important role. 

12 

markets, they permit estimation of all key parameters on the basis of the listings data described in the previous section. 

###### **3.1 Environment** 

We consider a labor market region with a finite number of locations _i_ (postal codes) over discrete time periods _t ≥_ 1 (quarters). The region is populated by house buyers and sellers whose trade is subject to search frictions. Buyers and sellers aim to maximize discounted utility values with common quarterly discount factor _β_ . All prices, values and costs in the model are understood as quality- and inflation-adjusted prices, values and costs per square meter of a housing unit. 

###### **3.1.1 Sellers** 

There is a free entry of sellers whose housing unit has exogenous outside value _Kit_ in location _i_ in period _t_ , which represents either the construction cost of a new unit or the value of an existing unit under alternative use, such as the discounted value of a lease or the monetized value of owner occupancy. Free entry requires that the endogenous value of a seller _Vit_<sup>_S_equals</sup> _Kit_ in all local markets ( _i, t_ ). A housing unit for sale involves cost _c_ per period, reflecting the utility costs of a vacant unit as well as sales costs which are assumed to be constant across time and space. 

###### **3.1.2 Buyers** 

There is an exogenous inflow of new buyers into the region at time _t_ , denoted _Bt_<sup>_n_,sothat</sup> the total number of buyers in the region, denoted _Bt_ , is composed of unmatched buyers from the last period and the new buyers, where the stock of buyers in the first period _B_ 1 is predetermined. Every buyer chooses in which location _i_ to search in period _t_ .<sup>11</sup> Search in location _i_ yields utility value _Vit_<sup>_B_+</sup><sup>_φit_+</sup><sup>_τi_where</sup><sup>_φit_is an idiosyncratic (buyer-specific) taste</sup> shock which is type-I extreme value distributed with zero mean, and _τi_ is a time-invariant location premium for location _i_ that is common for all buyers and constant over time. _Vit_<sup>_B_is</sup> the discounted utility value of a buyer searching in market _i_ at time _t_ , net of the taste shock and the location premium. If a buyer remains unmatched in market _i_ , she decides in which location to search next period after drawing new idiosyncratic taste shocks. If a buyer is matched in period _t_ , she pays the posted price and leaves the market with discounted utility value _Ait_ . These values are exogenous to the model and represent the values that buyers attach to a (quality and size adjusted) housing unit in location _i_ when bought at time _t_ . In 

> 11We rule out simultaneous search in multiple locations as we do not have enough information to discipline such a model feature. 

13 

any period of search, we assume that the buyer pays a cost _rt_ which represents the rental cost in the region. 

###### **3.1.3 Search and Matching** 

Sellers post prices and buyers direct search to the sales listings, so that the housing market in a given location potentially segments into submarkets that are differentiated by posted prices and buyer-seller ratios. Both sides of the housing market trade off matching probabilities and prices, as is standard in markets with competitive search (Moen, 1997). When _θ_ is the buyer-seller ratio (tightness) in a submarket, a seller is matched with probability _qt_ ( _θ_ ) and a buyer is matched with probability _ft_ ( _θ_ ) = _qt_ ( _θ_ ) _/θ_ . _qt_ is a strictly increasing and strictly concave function, so that _ft_ is decreasing in tightness. We allow matching efficiency to vary over time which is why both functions are indexed by the time index _t_ . Since all buyers and sellers searching in a given market ( _i, t_ ) share the same respective values, only one submarket is active in this market which has posted price _pit_ and market tightness _θit_ , both of which are equilibrium outcomes as described below.<sup>12</sup> 

###### **3.2 Value Functions and Equilibrium** 

The Bellman equations of sellers and buyers in market _i_ and period _t_ are 



A seller pays flow cost _c_ in the current period and is matched with probability _qt_ ( _θit_ ) in which case she sells the house and hence leaves the market with continuation value _pit_ . Otherwise, she either continues to search in the same market or stops searching, yielding in both cases continuation utility _Vi,t_<sup>_S_</sup> +1<sup>=</sup><sup>_Ki,t_+1.A buyer pays flow cost</sup><sup>_rt_and is matched with</sup> probability _ft_ ( _θit_ ), yielding continuation utility _Ait − pit_ . Otherwise, an unmatched buyer has continuation utility 



where the expectation is over the realization of next period’s idiosyncratic taste shocks _φj,t_ +1. 

> 12Although dispersion in residual prices exists _within_ locations in our data, the within-location component exhibits no time trend, see Table 2 in Section 2. Given our interest in widening spatial house price dispersion over time, our model abstracts from this feature in the data. 

14 

In every local market ( _i, t_ ), sellers post prices and buyers direct their search to the posted prices. Let ( _p, θ_ ) denote the price-tightness combination in a potential submarket. Let Ω _it_ denote the expected buyer surplus from searching in market ( _i, t_ ) which is identical for all (homogeneous) buyers in that market. Buyers must be offered at least surplus Ω _it_ to be willing to search in submarket ( _p, θ_ ). A seller chooses ( _p, θ_ ) to maximize the expected gain from trade, 



The constraint says that sellers must offer at least surplus Ω _it_ to attract buyers to the submarket. Substituting the price and the matching function _ft_ ( _θ_ ) = _qt_ ( _θ_ ) _/θ_ yields the first-order condition 



Because the matching function _qt_ is strictly concave, all sellers in market ( _i, t_ ) choose the same price _pit_ , so that only one submarket is active with tightness _θit_ . Using Ω _it_ = _ft_ ( _θit_ )[ _Ait − pit − βV_<sup>¯</sup> _t_<sup>_B_</sup> +1<sup>]and</sup><sup>_ft_(</sup><sup>_θ_)</sup><sup>_θ_=</sup><sup>_qt_(</sup><sup>_θ_)givestheequilibriumprice</sup> 



with matching function elasticity _ζt_ ( _θ_ ) = _qt_<sup>_′_(</sup><sup>_θ_)</sup><sup>_θ/qt_(</sup><sup>_θ_)</sup><sup>_∈_(0</sup><sup>_,_1).Thisequationdemonstrates</sup> how the posted price in market ( _i, t_ ) depends on housing supply (the sellers’ valuation _βVi,t_<sup>_S_</sup> +1<sup>),housingdemand(thebuyers’gainfromtrade</sup><sup>_Ait−β_¯</sup><sup>_V_</sup> _t_<sup>_B_</sup> +1<sup>),andtherentshar-</sup> ing factor _ζt_ ( _θit_ ) which responds to features of the matching technology and housing market tightness in market ( _i, t_ ). We build on this equation for our decomposition analysis in Section 5. 

Substituting the equilibrium price into the Bellman equations gives 



At the beginning of a period, all buyers _Bt_ in a labor market region draw idiosyncratic taste shocks _φit_ after which fraction 



15 

decide to search in location _i_ . Over time, the number of buyers in the labor market region adjusts according to 



where _Bt_<sup>_n_</sup> +1<sup>is the exogenous inflow of new buyers into the labor market region in period</sup><sup>_t_+1</sup> which adds to the number of unmatched buyers from the previous period. 

###### **Equilibrium Definition** 

Given an initial stock of buyers _B_ 1 and buyer inflow _Bt_<sup>_n_in periods</sup><sup>_t ≥_2, a</sup><sup>_spatial competitive_</sup> _search equilibrium_ describes, for all periods _t ≥_ 1 and locations _i_ , posted house prices _pit_ , market tightness _θit_ , discounted values of sellers and buyers _Vit_<sup>_S_,</sup><sup>_V_¯</sup> _t_<sup>_B_,</sup><sup>_V_</sup> _it_<sup>_B_,locationchoices</sup> – _πit_ and buyer stocks _Bt_ satisfying equations (4) (9) and the free-entry conditions of sellers _Vit_<sup>_S_=</sup><sup>_Kit_.</sup> 

###### **4 Estimation** 

In this section, we explain how we estimate the parameters of this model for a given labor market region with _i_ = 1 _, . . . , N_ locations (postal codes) and _t_ = 1 _, . . . , T_ periods (quarters).<sup>13</sup> We use for estimation the baseline sample described in Section 2.3 with variables aggregated at the location-quarter level. These are the residualized average hedonic price _pit_ ,<sup>14</sup> the number of listings _Sit_ which we identify with the number of sellers,<sup>15</sup> average duration of a listing in days _dit_ and the number of buyer contacts _Cit_ . Note that the stock of buyers, and therefore market tightness, is not observed. We explain below our identifying assumptions that allow us to back out these values and to estimate a matching function from information on listing duration _dit_ and the numbers of contacts _Cit_ and listings _Sit_ . 

Three model parameters are calibrated outside the model. _β_ is a standard discount factor at quarterly frequency that equals 0 _._ 995 to match an annual interest rate of 2%. _c_ is 

> 13We choose a quarterly period length to smooth out very short-term volatility at the local level that might partly arise due to a low number of observations. Further, a quarter plausibly reflects the typical planned transaction time for buyers and sellers in the housing market. In the data, we assign the day of first listing to a specific quarter so that some days of an active listing may fall into the next quarter. 

> 14 2 Specifically, we take the residual of the hedonic, inflation-adjusted log prices per _m_ at the listing level _εht_ as defined in Section 2.1, delog and multiply them with the average price in Euros, and average to the listing level to obtain _pit_ . 

> 15Multiple listings of the same seller should not raise concerns since they show up as independent listings on the _ImmobilienScout24_ platform. Note that we only consider listings of single residential housing units in our analysis. 

16 

set to an estimate for service charges per square meter, e.g. 6.50 Euros per quarter.<sup>16</sup> For the quarterly costs of an unmatched buyer _rt_ , we use the average, inflation-adjusted rental rate per _m_<sup>2</sup> in the region which we take from the rental listings in the RWI-GEO-RED dataset. 

The model estimation proceeds in two steps. First, we estimate a matching function, separate for each region, using the data on listing duration, number of listings and contacts. Second, we back out the buyer and seller valuations _Ait_ and _Kit_ that are consistent with the observed variation of prices, tightness and matching rates across time and space, and we estimate the location premia _τi_ which control the distribution of buyers across locations. 

###### **4.1 Matching Function** 

In the data, we measure the stock of sellers by the number of listings _Sit_ , but we do not observe the stock of buyers in a given market ( _i, t_ ), denoted _Bit_ . Hence market tightness _θit_ = _Bit/Sit_ is unobserved. However, we build on the assumption that the search intensity of every active buyer is the same so that every buyer contacts a given number of listings per day.<sup>17</sup> Therefore, we estimate an _auxiliary matching function_ using the contact-per-listingday ratio _ϑit_ = _Cit/_ ( _ditSit_ ) as an auxiliary flow-based measure of market tightness, which is then transformed into a matching function that depends on the buyer-seller ratio, as will be further explained below. 

We first regress log duration of a listing on the contact-per-listing-day ratio, pooling all locations and quarters in a labor market region. That is, we estimate 



where _εit_ is an error term and _gt_ is a time fixed effect. The latter takes care of any time trends in the listing duration relationship, as well as seasonality in the housing markets as documented in previous literature (cf. Ngai and Tenreyro, 2014). 

Table 4 shows the estimates of parameters _a_ 0 and _a_ 1 for each of the Top-7 labor market regions. As expected, in all cases parameter _a_ 1 is negative, showing that more contacts per listing day relate negatively to the duration of the listing. The estimates show that a doubling of contacts per listing day goes together with a decrease of duration between 15 and 25 percent (i.e. duration is multiplied with 2<sup>_−_0</sup><sup>_._24</sup> in Cologne and with 2<sup>_−_0</sup><sup>_._41</sup> in Munich), 

> 16See https://www.mieterbund.de/service/betriebskostenspiegel.html which reports a monthly cost of 2.17 Euros per month and square meter in 2018. This includes utilities, insurance, property tax, among others, and may be a lower bound as it does not include any additional sales costs. 

> 17Here we follow the logic of matching function estimation in labor market models where typically the stock of unemployed workers is observed, but flow measures of search intensity (e.g. the number of applications sent per day) are not observed. In our data, we only observe the flow of contacts, but not the stock of buyers. 

17 

Table 4: Matching function estimation 

|y=ln(_dit_)|Berlin|Munich|Hamburg|Frankfurt|Stuttgart|Dusseldorf|Cologne|
|---|---|---|---|---|---|---|---|
|_a_1|-0.32<sup>_∗∗∗_</sup>|-0.41<sup>_∗∗∗_</sup>|-0.31<sup>_∗∗∗_</sup>|-0.25<sup>_∗∗∗_</sup>|-0.35<sup>_∗∗∗_</sup>|-0.28<sup>_∗∗∗_</sup>|-0.24<sup>_∗∗∗_</sup>|
||(0.01)|(0.01)|(0.01)|(0.01)|(0.01)|(0.01)|(0.01)|
|_a_0|2.70<sup>_∗∗∗_</sup>|2.70<sup>_∗∗∗_</sup>|2.97<sup>_∗∗∗_</sup>|3.04<sup>_∗∗∗_</sup>|3.06<sup>_∗∗∗_</sup>|3.02<sup>_∗∗∗_</sup>|3.21<sup>_∗∗∗_</sup>|
||(0.05)|(0.04)|(0.04)|(0.04)|(0.04)|(0.04)|(0.04)|
|Time FE|Yes|Yes|Yes|Yes|Yes|Yes|Yes|
|_R_<sup>2</sup>|0.216|0.419|0.330|0.306|0.501|0.361|0.433|
|N|5,440|3,440|3,760|3,960|2,800|3,680|2,720|



Notes: Standard errors in parentheses.<sup>_∗_</sup> _p <_ 0 _._ 10,<sup>_∗∗_</sup> _p <_ 0 _._ 05,<sup>_∗∗∗_</sup> _p <_ 0 _._ 01 

depending on the labor market region. Figure 3 shows the distribution of the estimates of _a_ 1 across all labor market regions in Germany. 

The regression constant also varies between regions, showing that listing duration is about 51 log points longer in Cologne than in Berlin or Munich in the first quarter of 2009 (the reference category for the time fixed effect) for a given contacts-per-listing-day ratio. The time trends, which are shown in Appendix D, Table D.5, for the Top-7 regions, also show some heterogeneity between regions, but generally remain rather flat until 2014 after which listing duration has increased, conditional on the same contacts-per-listing-day ratio. 

We can now explain how we measure buyer-seller ratios and the original matching function which maps buyer-seller ratios into matching probabilities for both market sides. Since the daily matching probability of a seller is the inverse of average duration, _qit_<sup>_d_=1</sup><sup>_/dit_,</sup> the estimates of the auxiliary matching function relationship imply that _qit_<sup>_d_=</sup><sup>_qtϑµ_</sup> _it_<sup>where</sup> _qt_ = _e_<sup>_−a_0</sup><sup>_−gt_</sup> and _µ_ = _−a_ 1. 

While the number of buyers _Bit_ and their daily matching probability _fit_<sup>_d_are unobserved,</sup> we assume that a buyer contacts a given number of listings per day equal to _k_ . Then the <u>1</u> total number of contacts in market ( _i, t_ ) is _Cit_ = _kBit_<sup>abuyersearchesonaverage</sup> _fit_<sup>_d_since</sup> 1 _/fit_<sup>_d_days.Itfollowsthatthecontacts-per-listing-dayratiois</sup> 



where the last equality uses that the number of matched sellers per day is identical to the number of matched buyers per day, _qit_<sup>_dSit_=</sup><sup>_f_</sup> _it_<sup>_dBit_.Therefore,wecaninfertheunobserved</sup> buyer-seller ratio _θit_ and the number of buyers from the auxiliary tightness measure as 

18 



Figure 3: Distribution of estimates of _a_ 1 across labor market regions 

Notes: The distribution includes all estimates of _a_ 1 which are statistically different from zero. 

follows: 



Together with the estimated daily matching probability of a seller, we obtain quarterly matching probabilities for buyers and sellers, i.e. the matching function relationships used in Section 3: 



We set parameter _k_ such that _ft_ ( _θ_ ) is a probability for all plausible data observations. Specifically we winsorize extreme observations of _ϑit_ outside a large enough interval [ _ϑmin, ϑmax_ ] and set _k_ such that _f_ (( _ϑmin/k_ )<sup>1</sup><sup>_/_2</sup> ) = 0 _._ 99.<sup>18</sup> 

> 18We set _ϑmin_ = _eM −_ 3 _σ_ and _ϑmax_ = _eM_ +3 _σ_ where _M_ and _σ_ are the mean and standard deviation of ln _ϑit_ . Note that our estimates imply that _q_ (( _ϑmax/k_ )<sup>1</sup><sup>_/_2</sup> ) _<_ 1, so that _q_ is also a probability for all valid observations. 

19 

###### **4.2 Location Premia and Valuations of Buyers and Sellers** 

The second step of our estimation procedure is to simultaneously estimate the time-invariant location premia _τi_ and the time-varying buyer and seller valuations of a housing unit, _Ait_ and _Kit_ . The latter two objects can be uniquely pinned down to exactly match the observed prices _pit_ and tightness levels _θit_ which are both measured from our data as described above. Location premia are set to match the average buyer market shares in all locations. We demonstrate that this joint estimation can be implemented as the solution of a highdimensional, yet tractable equation system. 

ˆ Let _π_ ˆ _it_ = _<u>B</u>_ ˆ _<u>it</u> Bt_<sup>denote the share of buyers in market</sup><sup>_i_at time</sup><sup>_t_in the data where buyers in</sup> market ( _i, t_ ) and the total buyer stock are measured as explained in the previous subsection. The market shares in the model _πit_ and in the data differ according to 



where _ηit_ is an error term. We choose location premia _τi_ to minimize<sup>�</sup> _i,t_<sup>_η_</sup> _it_<sup>2subjecttothe</sup> requirement that the average location premium is zero,<sup>�</sup> _i_<sup>_τi_= 0.</sup> From (4) and (8) follows 



so that we can write 



Minimization of<sup>�</sup> _i,t_<sup>_η_</sup> _it_<sup>2subjecttotheconstraint</sup> 



with respect to _τi_ has the first-order conditions<sup>19</sup> 



where _λ_ is the multiplier on the constraint. 

Since our model is set up as an infinite-horizon model, we need to make an assumption about the forecasts of continuation values of buyers and sellers in the last observation period _T_ . We do this by linearly extrapolating the values during the observation period, namely 

> 19The minimization takes the values _V_ ¯ _tB_ as given, and hence ignores the impact of _τi_ on the values of unmatched buyers, see equation (4). This approximation is innocuous when the number of locations is large so that the impact of each _τi_ on _V_<sup>¯</sup> _t_<sup>_B_</sup> is negligible. 

20 

_Vit_<sup>_S_and</sup><sup>_V_</sup> _it_<sup>_B_for</sup><sup>_t_= 1</sup><sup>_, . . . , T_,tothefirstquarterthereafter.Theanalyticexpressionsofthis</sup> extrapolation procedure are: 



We are now ready to describe how the unknown valuation parameters ( _Ait, Kit_ ) and location premia _τi_ can be calculated. From our data, we use the (quality- and inflation-adjusted, per square meter) prices _pit_ , tightness _θit_ as calculated above, the estimated (time-varying) ˆ matching function relationships, and the buyer market shares _πit_ as defined above. Then the pricing equations (5), the two Bellman equations (6) and (7), the extrapolation equations (16) and (17), the optimality conditions (14) and (15), and the continuation utilities of unmatched buyers (4) constitute a system of (3 _N_ +1)( _T_ +1)+1 equations in (3 _N_ +1)( _T_ +1)+1 unknowns: ( _Ait_ )<sup>_T_</sup> _t_ =1<sup>,(</sup><sup>_V_</sup> _it_<sup>_B, V_</sup> _it_<sup>_S_)</sup><sup>_T_</sup> _t_ =1<sup>+1,</sup><sup>_τi_for</sup><sup>_i_=1</sup><sup>_, . . . , N_,</sup><sup>_λ_,and(¯</sup><sup>_V_</sup> _t_<sup>_B_)</sup><sup>_T_</sup> _t_ =1<sup>+1.Exceptthe</sup><sup>_T_+ 1</sup> equations (4), these are all linear equations. Their joint solution is straightforward to implement, with further details described in Appendix F. The solution gives the buyer and seller valuations _Ait_ , _Kit_ = _Vit_<sup>_S_,andlocationpremia</sup><sup>_τi_.</sup> 

###### **5 Results** 

In this section, we use the estimated model to study what factors contribute to house price dynamics in terms of the observed rise in house prices and their spatial dispersion. We distinguish between three contributing forces: _(i)_ housing supply factors related to the locationand time-specific seller valuations _Kit_ , _(ii)_ housing demand factors represented by the buyer gains from trade _Ait − βV_<sup>¯</sup> _r,t_<sup>_B_</sup> +1<sup>,and,</sup><sup>_(iii)_rent-sharing factors associated with the region- and</sup> time-specific matching frictions through the matching function _qrt_ ( _·_ ).<sup>20</sup> After describing how we perform the counterfactual experiments in Section 5.1, we focus in Section 5.2 on the Top7 labor market regions, which exhibited the strongest house price growth during 2009–2018, and document the contribution of the three factors for house price dynamics separately for each of these metropolitan areas. In Section 5.3 we turn to the between- and within-region variance decomposition considered in Section 2 and investigate the contribution of supply, demand, and rent sharing for the observed changes. 

> 20 We add the subscript _r_ to variables which are common across markets ( _i, t_ ) within a labor market region _r_ but differ across regions. 

21 

###### **5.1 Model-Based Decomposition** 

We use the hedonic prices _pit_ , tightness levels _θit_ , the estimated valuation parameters _Kit_ , _Ait_ and _V_<sup>¯</sup> _rt_<sup>_B_, and the estimated matching functions</sup><sup>_qrt_(</sup><sup>_·_) to isolate the role of factors</sup><sup>_(i)_-</sup><sup>_(iii)_for</sup> generating the observed house price dynamics. Building on the equilibrium pricing equation (5), we express the price in location _i_ at time _t_ into the following terms: 



To measure the respective contributions of the three factors, we proceed as follows. Regarding the contribution of housing supply, we fix housing demand via the buyers’ gain and the rentsharing factor to their initial 2009 values, _Ai,_ 1 _− βV_<sup>¯</sup> _r,_<sup>_B_</sup> 2<sup>and</sup><sup>_ζr,_1(</sup><sup>_θi,_1),whileallowinghousing</sup> supply via the sellers’ valuations _βKi,t_ +1 to evolve. By doing so, we derive counterfactual prices _p_<sup>supply</sup> _it_ through the pricing equation which reflect only the shifts in housing supply. Similarly, fixing housing supply and rent-sharing to their initial values, while letting housing demand evolve, we derive another set of counterfactual prices _p_<sup>demand</sup> _it_ which reflect only shifts in housing demand. Finally, the constructed prices _p_<sup>rent</sup> _it_ summarize only changes in the rent-sharing factor _ζrt_ ( _θit_ ). 

Note that the rent-sharing factor varies across space and across time for different reasons: First, the estimated matching function elasticity parameters are allowed to differ across regions, while they are identical across locations (postal codes) and over time. Second, the matching function scale varies over time and across regions but not between locations within a region. Hence, these parameters only matter for between-region components considered in Section 5.3. Third, the matching function elasticity _ζrt_ ( _._ ) is not constant but decreases in market tightness which itself varies across locations and over time. Intuitively, a tighter housing market (from the buyers’ point of view) intensifies the congestion externality on the buyers’ side and relaxes the congestion externality on the sellers’ side which contributes to a price increase without changes of buyers’ or sellers’ valuations. 

###### **5.2 House Price Dynamics in the Top-7 Regions** 

As seen in Figure 1, the Top-7 labor market regions experienced much stronger house price growth than the rest of Germany during the housing boom 2009–2018. Moreover, the increase of within-region spatial dispersion was stronger than in other geographic subsamples, cf. Table 3. Our model can shed light on the separate roles of supply, demand and matching frictions for these trends. Beginning with mean price growth, Table 5 summarizes the contribution of factors _(i)_ - _(iii)_ to the average price change in each of the Top-7 labor market ¯ ¯ regions between 2009 and 2018, _pT − p_ 1. Housing supply in isolation produces a price change 

22 

¯ ¯ ¯ ¯ _p_<sup>supply</sup> _T − p_ 1, while housing demand contributes _p_<sup>demand</sup> _T − p_ 1. Finally, changes in rent-sharing ¯ ¯ account for _p_<sup>rent</sup> _T − p_ 1. The numbers in parentheses show the percent of the overall price change generated by the different factors, separately for each region. Note that these percentages do not add to 100 since the three counterfactual scenarios build on a non-linear equation. 

Table 5: Decomposition of average price changes, 2009-2018 

||¯_pT −_¯_p_1|¯_p_<sup>supply</sup><br>_T_<br>_−_¯_p_1|¯_p_<sup>demand</sup><br>_T_<br>_−_|¯_p_1|¯_p_<sup>rent</sup><br>_T_<br>_−_¯_p_1|
|---|---|---|---|---|---|
|Munich|0.643|0.185|0.520||-0.014|
||(100)|(29)|(81)||(-2)|
|Frankfurt|0.312|0.012|0.268||-0.044|
||(100)|(4)|(86)||(-14)|
|Berlin|0.574|0.049|0.505||-0.073|
||(100)|(9)|(88)||(-13)|
|Stuttgart|0.491|0.158|0.361||-0.015|
||(100)|(32)|(74)||(-3)|
|Cologne|0.285|0.022|0.241||-0.030|
||(100)|(8)|(85)||(-11)|
|Hamburg|0.446|0.115|0.369||0.009|
||(100)|(26)|(83)||(2)|
|Dusseldorf|0.262|0.048|0.221||0.001|
||(100)|(18)|(84)||(0.4)|



Notes: The supply, demand and rent-sharing contributions to the change of average log prices between 2008 and 2019 in Top-7 labor market regions are derived as described in the text. Percentages of the total log price change for each region are shown in parentheses. 

The highest average price increase over the period is 90 percent (0.643 log points) with respect to the initial price and occurs in Munich, while the lowest is in Dusseldorf, 30 percent. In all regions, the demand-driven price change contributes the most to the average price increase. For instance, in Berlin, shifts in housing demand have the highest contribution and account for around 88 percent of the overall price increase, while in Stuttgart this number is the lowest, 74 percent. Housing supply factors produce much smaller contributions to the average price changes. In Stuttgart, their contribution is 32 percent, while it is only 4 percent in Frankfurt. A stronger expansion of housing construction in Frankfurt relative to Stuttgart could be a likely explanation for these differences. Finally, changes in rent-sharing factors have a relatively small effect on average price changes between 2009 and 2018. In most regions, their contribution is negative, i.e. market frictions alone produce a price 

23 

decrease. Despite housing markets becoming tighter overall (see Section 2), the increase is relatively weaker in locations with initially high buyer valuations, so that ultimately rent sharing component contributes negatively. Only in Hamburg and Dusseldorf, changes in rent-sharing factors contribute positively to the price increase, although by a negligible amount. 

Turning to the second moment of house prices, Table 6 displays the contribution of factors _(i)_ - _(iii)_ to the 2008-2019 change in spatial price dispersion as measured by the variance of prices across locations within a region. There is some heterogeneity in the change of dispersion across labor market regions. In Berlin, price dispersion has even slightly declined over time (see also Figure D.2 in Appendix D), while dispersion widened significantly in Cologne, Stuttgart, Dusseldorf, Frankfurt and Hamburg (in descending order of the increase). In Munich, dispersion did not change by much between 2008 and 2019. This fact masks an inverted U-shaped pattern in the evolution of the price dispersion in this region, which can be seen in Figure D.2. 

There is also heterogeneity in the contribution of each factor across the Top-7 regions. Changes in housing demand account for a sizable fraction of the overall dispersion change in all regions. In Munich and Hamburg, housing demand can account for more than the observed increase in price dispersion. In Stuttgart, Cologne, Dusseldorf and Frankfurt changes in demand can generate between 28 and 89 percent of the observed increase in dispersion. In Berlin, demand factors contribute to the decline in dispersion but they are not the leading factor. 

In Berlin, Munich and Hamburg, changes in housing supply contribute to declining dispersion. A likely explanation is that supply expanded relatively more in high-price locations which had a dampening impact on spatial dispersion. In the other regions, supply factors play only a secondary role. In Stuttgart, Frankfurt, Dusseldorf and Cologne, shifts in supply generate less than a fifth of the observed rise in dispersion. Finally, in most cases changes in rent-sharing factors relating to changes in spatial dispersion of market tightness have a small effect on the evolution of price dispersion over time. 

###### **5.3 Within- and Between-Region Price Dispersion** 

We further use the counterfactual model-generated house prices due to changes in demand, supply and rent-sharing factors to decompose the variance of house prices into within- and between-region components as in equation (3). First, we perform the original variance decomposition exercise of Section 2.5 for the same subsets of different geographic units used in Table 3.<sup>21</sup> Second, using the counterfactual prices which capture the contribution of factors 

> 21These numbers are not exactly identical to those of Table 3 which is due to three reasons. First, the sample for this decomposition is slightly smaller than in the one used in Section 2.5 because we excluded 

24 

Table 6: Decomposition of changes in house price dispersion, 2009-2018 

||var(_pT_)_−_var(_p_1)|var(_p_<sup>supply</sup><br>_T_<br>)_−_var(_p_1)|var(_p_<sup>demand</sup><br>_T_<br>)_−_var(_p_1)|var(_p_<sup>rent</sup><br>_T_<br>)_−_var(_p_1)|
|---|---|---|---|---|
|Munich|0.003|-0.014|0.011|-0.007|
||(100)|(-467)|(367)|(-233)|
|Frankfurt|0.035|0.002|0.031|-0.002|
||(100)|(6)|(89)|-6|
|Berlin|-0.011|-0.018|-0.007|-0.007|
||(100)|(164)|(64)|(64)|
|Stuttgart|0.076|0.002|0.021|0.001|
||(100)|(3)|(28)|(1)|
|Cologne|0.086|0.016|0.071|0.007|
||(100)|(19)|(83)|(8)|
|Hamburg|0.020|-0.003|0.022|-0.001|
||(100)|(-15)|(110)|(-5)|
|Dusseldorf|0.062|0.011|0.053|0.003|
||(100)|(18)|(85)|(5)|



Notes: The supply, demand and rent-sharing contributions to the change of price dispersion (variance of log prices) between 2008 and 2019 in Top-7 labor market regions are derived as described in the text. Percentage of the total variance change for each region are shown in parentheses. 

- _(i) (iii)_ to the 2008-2019 change in price dispersion, we can identify the share of within- and between-region price dispersion stemming from each of these factors alone. 

Table 7 summarizes these results. The data decomposition is presented in a bold text for each geographical aggregation. The rows “Percent” depict the percent of the variance in each position in the prior bold rows relative to the initial level of the between-location variance in 2009. For instance, the between-location variance in 2018 for the full sample is 224.5 percent of the initial 2009 variance (compare 0.0758 and 0.1701). The within-regions variance for the full sample in 2009 is 41 percent of the between-location variance (compare 0.0758 and 0.0312). 

The subsequent rows “Demand”, “Supply” and “Rent sharing” for each geographical aggregation show the percent of the variances based on each of the corresponding counterfactual model-generated house price series due to changes in demand, supply and rent-sharing factors relative to the initial level of the between-location variance in 2009. For instance, for the full sample changes in demand factors between 2009 and 2018 alone can generate 196 percent 

few locations that span multiple labor regions in our dataset. Second, the decomposition in Section 2.5 is implemented at an annual frequency whereas here we use quarterly observations. Third, the data in the model-implied decomposition are smoothed to reduce short-run volatility. 

25 

Table 7: Model-based within- and between-region decomposition 

||Between|-location|variance|W|ithin regio|ns|Bet|ween regi|ons|
|---|---|---|---|---|---|---|---|---|---|
||2009|2013|2018|2009|2013|2018|2009|2013|2018|
|**Full sample**|**0.0758**|**0.1205**|**0.1701**|**0.0312**|**0.0455**|**0.0529**|**0.0446**|**0.0749**|**0.1172**|
|Percent|100.0|159.0|224.5|41.1|60.1|69.8|58.9|98.9|154.7|
|Demand|100.0|144.0|195.9|41.1|55.6|66.0|58.9|88.5|130.0|
|Supply|100.0|102.2|118.6|41.1|42.5|41.2|58.9|59.7|77.6|
|Rent sharing|100.0|92.8|93.8|41.1|41.3|40.7|58.9|51.4|53.0|
|**West Germany**|**0.0737**|**0.1203**|**0.1711**|**0.0311**|**0.0453**|**0.0532**|**0.0426**|**0.0750**|**0.1179**|
|Percent|100.0|163.2|232.0|42.2|61.5|72.2|57.8|101.7|159.9|
|Demand|100.0|147.4|202.1|42.2|56.8|68.2|57.8|90.6|133.9|
|Supply|100.0|102.8|118.2|42.2|43.4|42.0|57.8|59.4|76.3|
|Rent sharing|100.0|92.6|92.3|42.2|42.2|41.5|57.8|50.3|50.6|
|**East Germany**|**0.0565**|**0.0883**|**0.0998**|**0.0320**|**0.0499**|**0.0478**|**0.0245**|**0.0384**|**0.0521**|
|Percent|100.0|156.3|176.7|56.6|88.3|84.6|43.4|68.0|92.2|
|Demand|100.0|142.4|157.9|56.6|81.5|79.4|43.4|60.9|78.6|
|Supply|100.0|98.6|109.8|56.6|62.4|60.1|43.4|35.6|49.8|
|Rent sharing|100.0|93.7|97.1|56.6|61.2|59.9|43.4|31.7|36.7|
|**Top-7 regions**|**0.0693**|**0.0956**|**0.1381**|**0.0435**|**0.0575**|**0.0693**|**0.0258**|**0.0380**|**0.0688**|
|Percent|100.0|138.0|199.4|62.8|83.1|100.0|37.2|54.9|99.3|
|Demand|100.0|127.0|182.2|62.8|79.1|98.6|37.2|47.9|83.7|
|Supply|100.0|96.5|116.2|62.8|62.1|62.4|37.2|34.3|54.1|
|Rent sharing|100.0|90.0|101.3|62.8|62.0|65.5|37.2|27.8|35.7|
|**Urban**|**0.0747**|**0.1195**|**0.1700**|**0.0327**|**0.0471**|**0.0539**|**0.0420**|**0.0724**|**0.1162**|
|Percent|100.0|160.1|227.7|43.7|63.1|72.1|56.3|97.0|155.6|
|Demand|100.0|144.9|198.7|43.7|58.5|68.5|56.3|86.4|130.3|
|Supply|100.0|102.6|119.8|43.7|45.0|43.8|56.3|57.6|76.3|
|Rent sharing|100.0|93.2|94.8|43.7|43.9|43.6|56.3|49.2|51.1|
|**Rural**|**0.0456**|**0.0722**|**0.1174**|**0.0156**|**0.0279**|**0.0443**|**0.0301**|**0.0443**|**0.0730**|
|Percent|100.0|158.3|257.3|34.1|61.2|97.2|65.9|97.0|160.1|
|Demand|100.0|141.5|219.6|34.1|53.4|87.3|65.9|88.1|132.3|
|Supply|100.0|98.2|124.2|34.1|35.1|39.5|65.9|63.1|84.8|
|Rent sharing|100.0|88.8|94.6|34.1|32.1|34.3|65.9|56.7|60.2|



Notes: See the notes to Table 2 for definitions of the different geographic units subsamples. 

26 

of the initial between-location variance. A similarly dominant role of demand can also be observed for the other geographic subsamples. Changes in supply factors hardly matter for widening within-region dispersion (with the exception of rural and East German subsamples), although they contribute to rising between-region variation. Overall, our results point out that changes in demand factors are the most important driver of price dispersion over time at any level of geographical aggregation, between regions, or within regions. 

Figure 4 reports graphically the results for each quarter for the full sample of all regions of the model-based variance decomposition. The top-left plot shows the variance decomposition using the actual location- and time-specific prices. It reiterates the results from Table 3 and Table 7. Both within- and between-regions dispersion increase over time. However, withinregions dispersion contributes more to the overall variance increase than the between-regions dispersion. 









Figure 4: Variance decomposition of within- and between-region price changes 

Notes: Model-based variance decomposition of equation (3) for all the regions in 2009-2018. Within (red line) depicts the within-region dispersion, whereas Between (yellow line) refers to dispersion coming from across labor market regions. The sum of within- and between-regions dispersion equals the total variance (blue line). 

27 

The top-right plot of Figure 4 displays the time evolution of the overall variance as well its within- and between-regions components coming from changes in the rent-sharing factor, while the two bottom panels depict the same thing but in the cases in which only housing demand or housing supply changes are at work. The results clearly show that mostly changes in housing demand contribute to the rise of price dispersion. 

###### **6 Conclusions** 

Using a dataset of sales listings for Germany in the recent housing boom between 2009 and 2018, we document a significant rise in house price dispersion driven entirely by differences in prices across postal codes. A simple variance decomposition reveals that the majority of the observed increase in house price heterogeneity across all postal codes in Germany is accounted for by an increase in price dispersion between labor market regions but that price dispersion has also gone up within labor market regions, especially in larger metropolitan areas. 

We propose and estimate a simple directed search model of the housing market in order to quantify the relative contributions of housing supply, housing demand and frictions in the matching process between buyers and sellers to the observed house price trends. We find that differential changes in housing demand across postal codes within the Top-7 regions are the main contributors to the increase in house prices and their dispersion in these regions between 2008 and 2019. Housing demand is also the main factor behind the overall rise in between-location price dispersion, while housing supply plays a secondary contribution for between-region price divergence. 

While we identify demand-related factors as the primary driving force behind increasing price dispersion in the housing market of Germany, our stylized model cannot address the underlying fundamental reasons for these demand shifts. Notably, the diverse impact of monetary policy on house prices, as evidenced in the U.S. by Gorea et al. (2023), offers one potential explanation. Additionally, the influx of refugees to Germany during 2015 and 2016 has been associated with a notable decrease in nearby neighborhood listing prices in Berlin by 3-4% (Hennig, 2021), suggesting another contributing factor to demand dynamics. Moreover, recent research highlights the trend of assortative matching: high-ability workers are increasingly sorted into highly productive firms situated predominantly in large urban areas (Dauth et al., 2022). This phenomenon has likely contributed to spatial disparities in earnings in Germany, potentially influencing the housing market. Future research could leverage on further micro-level datasets and develop richer structural models to quantify the relative contributions of these factors for house price dynamics. 

28 

###### **References** 

- Aguirregabiria, Victor and Pedro Mira (2010), “Dynamic discrete choice structural models: A survey.” _Journal of Econometrics_ , 156, 38–67. 

- Albrecht, James, Pieter A Gautier, and Susan Vroman (2016), “Directed search in the housing market.” _Review of Economic Dynamics_ , 19, 218–231. 

- Amaral, Francisco, Martin Dohmen, Sebastian Kohl, and Moritz Schularick (2024), “Interest rates and the spatial polarization of housing markets.” _American Economic Review: Insights_ , 6, 89–104. 

- Amaral, Francisco, Martin Dohmen, Moritz Schularick, and Jonas Zdrzalek (2023), “German real estate index (GREIX).” ECONtribute Discussion Paper No. 231. 

- Ben-Shahar, Danny and Roni Golan (2022), “Price dispersion and time-on-market in the housing market.” _Journal of Housing Economics_ , 58, 101875. 

- Caliendo, Lorenzo, Maximiliano Dvorkin, and Fernando Parro (2019), “Trade and labor market dynamics: General equilibrium analysis of the China trade shock.” _Econometrica_ , 87, 741–835. 

- Dauth, Wolfgang, Sebastian Findeisen, Enrico Moretti, and Jens Suedekum (2022), “Matching in cities.” _Journal of the European Economic Association_ , 20, 1478–1521. 

- Fogli, Alessandra, Veronica Guerrieri, Mark Ponder, and Marta Prato (2023), “The end of the American dream? Inequality and segregation in US cities.” Mimeo. 

- Garriga, Carlos and Aaron Hedlund (2020), “Mortgage debt, consumption, and illiquid housing markets in the Great Recession.” _American Economic Review_ , 110, 1603–1634. 

- Georgi, Sabine and Peter Barkow (2010), “Wohnimmobilien-Indizes: Vergleich Deutschland – Grossbritannien.” ZIA Projektbericht, Zentraler Immobilienausschuss, Berlin. 

- Gorea, Denis, Oleksiy Kryvtsov, and Marianna Kudlyak (2023), “House price responses to monetary policy surprises: Evidence from the U.S. listings data.” CEPR Discussion Paper No. 17595. 

- Guren, Adam M (2018), “House price momentum and strategic complementarity.” _Journal of Political Economy_ , 126, 1172–1218. 

- Gyourko, Joseph, Christopher Mayer, and Todd Sinai (2013), “Superstar cities.” _American Economic Journal: Economic Policy_ , 5, 167–199. 

29 

- Hedlund, Aaron (2016), “Illiquidity and its discontents: Trading delays and foreclosures in the housing market.” _Journal of Monetary Economics_ , 83, 1–13. 

- Hennig, Jakob (2021), “Neighborhood quality and opposition to immigration: Evidence from German refugee shelters.” _Journal of Development Economics_ , 150, 102604. 

- Herkenhoff, Kyle F, Lee E Ohanian, and Edward C Prescott (2018), “Tarnishing the golden and empire states: Land-use restrictions and the US economic slowdown.” _Journal of Monetary Economics_ , 93, 89–109. 

- Hsieh, Chang-Tai and Enrico Moretti (2019), “Housing constraints and spatial misallocation.” _American Economic Journal: Macroeconomics_ , 11, 1–39. 

- Jiang, Erica Xuewei, Nadia Kotova, and Anthony L Zhang (2024), “Liquidity in residential real estate markets.” Mimeo. 

- Kindermann, Fabian, Julia Le Blanc, Monika Piazzesi, and Martin Schneider (2024), “Learning about housing cost: Theory and evidence from the German house price boom.” Mimeo. 

- Kosfeld, Reinhold and Alexander Werner (2012), “Deutsche Arbeitsmarktregionen – Neuabgrenzung nach den Kreisgebietsreformen 2007–2011.” _Raumforschung und Raumordnung_ , 70, 49–64. 

- Moen, Espen R (1997), “Competitive search equilibrium.” _Journal of Political Economy_ , 105, 385–411. 

- Moen, Espen R, Plamen T Nenov, and Florian Sniekers (2021), “Buying first or selling first in housing markets.” _Journal of the European Economic Association_ , 19, 38–81. 

- Ngai, L Rachel and Silvana Tenreyro (2014), “Hot and cold seasons in the housing market.” _American Economic Review_ , 104, 3991–4026. 

- Rekkas, Marie, Randall Wright, and Yu Zhu (2022), “How well does search theory explain housing prices?” Mimeo. 

- Roback, Jennifer (1982), “Wages, rents, and the quality of life.” _Journal of Political Economy_ , 90, 1257–1278. 

- Rosen, Sherwin (1979), “Wage-based indexes of urban quality of life.” In _Current issues in urban economics_ (P Mieszkowski and M Straszheim, eds.), 74–104, Johns Hopkins Univ. Press. 

- Saiz, Albert (2010), “The geographic determinants of housing supply.” _Quarterly Journal of Economics_ , 125, 1253–1296. 

30 

- Van Nieuwerburgh, Stijn and Pierre-Olivier Weill (2010), “Why has house price dispersion gone up?” _Review of Economic Studies_ , 77, 1567–1606. 

- Vanhapelto, Tuuli and Thierry Magnac (2024), “Housing search and liquidity in spatial equilibrium.” Mimeo. 

- Wright, Randall, Philipp Kircher, Benoˆıt Julien, and Veronica Guerrieri (2021), “Directed search and competitive search equilibrium: A guided tour.” _Journal of Economic Literature_ , 59, 90–148. 

31 

#### **Appendix** 

###### **A Data Description** 

**Background.** Immobilienscout24 is the largest online real estate listing platform in Germany, catering to real estate providers, owners, tenants, and buyers. Operating in three countries - Germany, Austria, and Spain - the platform and its mobile app collectively attract approximately 20 million visitors per month. As of the end of 2019, Immobilienscout24 boasted around 450 million active listings, underscoring its prominent position in the real estate market. 

The online portal can be accessed at https://www.immobilienscout24.de. Upon entering the German-language website, users are presented with the interface illustrated in Figure A.1. The platform prompts users to select their country, specify the location for their search (city, address, or postal code), indicate the transaction type (buy or rent) and define the property type (house, flat or other types). 

Additionally, the platform offers a range of filtering options, allowing users to refine their search by specifying property characteristics beyond geographical constraints. Users have the flexibility to set price ranges by providing a lower bound, an upper bound, or both. Furthermore, there is an option to specify the desired number of rooms. 



Figure A.1: Immobilienscout24 web portal 

**Dataset.** Our analysis relies on version 5.1 of the RWI-GEO-RED dataset, curated by the Research Data Centre ( _Forschungsdatenzentrum_ or FDZ Ruhr) at the Rheinisch-Westf¨alisches Institut f¨ur Wirtschaftsforschung (RWI Essen), covering the period from January 2007 to July 2021. The dataset comprises listings of residential properties on the Immobilien- 

32 

Scout24 website across Germany, categorized into four classes: house sales, flat sales, house rents and flat rents.<sup>22</sup> 

In addition to listed prices and rents, buyer contacts and the duration of the listings, the dataset incorporates user-contributed information that influences the valuation and location of each listing. Users provide details about their listings through a guided online questionnaire, subsequently transforming their input into an advertisement on the ImmobilienScout24 website. While essential information such as location, price (rent), and space of the listed property is mandatory, the remaining questionnaire fields are optional. There are a total of 76 distinct entries available for users to provide information, categorized into eight groups by RWI Essen. 

**Locations.** ImmobilienScout24 does not provide the address of the offered real estate. Instead, they geo-code addresses when available according to their own Mercator.<sup>23</sup> In turn, the RWI Essen converts the projected locations into the European standard ETRS89-LAEA based on INSPIRE which is a grid of 1- _km_<sup>2</sup> raster cells covering the whole territory of Germany. Subsequently, the grids are then assigned to broader administrative regions, in particular postal codes, municipalities, districts or local labor market regions. This is done based on the 2015 geographical shapefiles provided by the Federal Agency for Cartography and Geodesy. 

To compare the geographic house price/rent dispersion across time, we pool the housing units together in terms of postal codes. We choose postal codes rather than 1- _km_<sup>2</sup> cells because the former are sufficiently large to contain enough housing units but also small enough to exhibit spatial heterogeneity within city boundaries. The highest level of geographical aggregation we use is the labor market regions categorized by Kosfeld and Werner (2012). Labor market regions combine one or more districts and are characterized according to the commuter links to local labor centres. 

**Basic cleaning** : We allow for a two-year burn-in period at the beginning and end of the sample. This allows us to properly identify new listings and to also exclude the possibility of active listings at the end of the sample. To this end, we include in our dataset all listings that appear on the Immobilienscout24 platform between January 1, 2009 and December 31, 2018. Then we erase multiple entries that correspond to the same property within a short window.<sup>24</sup> In particular, we only keep the last price and we drop all previous listings for the 

> 22ImmobilienScout24 claims a market share of approximately 50% of all advertised real estate objects in Germany (Georgi and Barkow, 2010). 

> 23In the initial years covered by the dataset, it was not mandatory for users to provide the address of the real estate. They could show only urban districts or municipalities for public use. Only for the most recent years, it is obligatory to provide the property address in the offer. 

> 24According to the RWI-GEO-RED data manual duplicate entries occur for several reasons: _“First, since we obtain spells that have not been concluded at the time of data delivery, these will also occur in the next_ 

33 

same item if it was posted more than once within a six-month period. We treat spells with starting dates at least six months from each other as different postings.<sup>25</sup> Second, we drop properties with missing mandatory information such as the geo-coded location, number of rooms, size or the age of the property. We also drop properties classified as “castles” or properties built before the year 1900. Finally, we remove all postings listed for less than a day. 

**Censoring.** We exclude all postings with unreasonable price/rent entries. These entries include ultra-luxurious properties that form a market of their own and are likely to contaminate our analysis. We drop all units with a sale price of more than e6,000,000 or a rental price that exceeds e6000 per month. On the other hand, under-market value properties might be indicative of fraudulent listings or an attempt of the sellers to manipulate in their favor the Immobilienscout24 listing algorithm. This can happen only in the case the potential buyers list the property by price/rent in ascending order.<sup>26</sup> We remove all listings with a sale price of less than e10000 and a rental price of less than e130. 

Moreover, we censor the price of a property per _m_<sup>2</sup> . House and flats for sales are censored between e150 and e20000 per _m_<sup>2</sup> and rental units between e2.5 and e25 per _m_<sup>2</sup> . The living area is restricted between 25 and 400 _m_<sup>2</sup> for flats and between 45 and 800 _m_<sup>2</sup> for houses. On top, we omit flats with more than 8 rooms and houses with more than 15 rooms. Finally, we drop all properties where the number of contacts or the number of clicks is beyond the 99-th percentile. Lastly, we drop listings with a duration longer than the 99-th percentile separately for sale and rental houses and flats. 

Finally, we restrict the dataset to postal codes that contain at least 10 postings within a quarter and labor market regions that contain at least 14 postal codes. We run this procedure separately for the rental and sales market. 

**Inflation adjustments.** The house prices and rents in our dataset are in nominal terms. We compute the inflation-adjusted prices and rents by deflating the nominal values with the 

_delivery which continues from the time of the previous delivery. Moreover, users can make small changes to the advertisement in order to attract more people. In the data, we only observe the status of the advertisement at the time of data delivery. Hence, the same advertisement might appear twice but with slightly different features in the data when a change was made after the delivery date. Fourth, users can temporarily set an object as inactive. This may be reasonable when a prospective buyer has committed to buying an object, but the deal has not yet been finalized. While inactive, objects will not be included in queries of potential buyers and will thus not be included in the dataset. However, if the potential buyer withdraws their offer to buy, the user might decide to activate the advertisement again. Lastly, users might decide to use an old advertisement as a template for a new ad, e.g. when renting two similar flats in the same house with only a short period in between.”_ 

> 25RWI Essen has developed an automatized procedure to identify multiple entries at the same time. 

> 26An example for this are properties listed with very low rent but then much higher than normal utilities. 

34 

respective state-specific consumer price index at the monthly level obtained from the Federal Statistical Office. 

**Location adjustments.** The vast majority of geo-code coordinates and their respective administrative match are consistent but some challenges remain. First, some administrative districts have been merged or changed over time. To address this problem, we obtain from https://www.geodaten-deutschland.de a 2019 file that contains up-to-date geo-referenced administrative information. 

Several districts have changed names or were merged into a different district in 2011. Table A.1 shows the mapping from these changed 2011 districts to their 2015 versions. 

Table A.1: Changes of districts, 2011-2015 

|2011 District|2011 District Number|2015 District|2015 District Number|
|---|---|---|---|
|SK Aachen and LK Aachen|5313, 5354|St¨adteregion Aachen|5334|
|Nordvorpommern|13107|Vorpommern-R¨ugen|13073|
|S¨udvorpommern|13108|Vorpommern-Greifswald|13075|
|Bremerhaven|4021|Bremerhaven, Stadt|4012|
|Rostock|13101|Rostock|13003|
|Mittleres Mecklenburg|13104|Landkreis Rostock|13072|
|Mecklenburgische Seenplatte|13103|Mecklenburgische Seenplatte|13071|
|Nordwestmecklenburg|13106|Nordwestmecklenburg|13074|
|Schwerin|13102|Schwerin|13004|
|S¨udwestmecklenburg|13105|Ludwigslust-Parchim|13076|



Finally, we drop listings without information regarding the postal code (0.2% of all listings). For the remaining listings, we matched the postal code and the municipality of the RWI Essen dataset with the https://www.geodaten-deutschland.de updated dataset.<sup>27</sup> Around 98% of the listings match perfectly in both dimensions. All the unmatched entries are dropped. 

**Listings over time and space.** Table A.2 shows the numbers of listings of our baseline dataset across the years for each of the four property classes. Figure A.2 presents the number of listings across districts in Germany. 

> 27One might expect that the postal code areas are coherent and disjoint. However, this is not the case. There are postal code areas where one area lies entirely inside another area (e.g. 53879 in Euskirchen is enclosed by 53881). There are even cases where an area contains more than one other area. 

35 

Table A.2: Number of listings over time, 2009-2018 

||House sales|Flat sales|House rents|Flat rents|
|---|---|---|---|---|
|2009|337,837|291,180|27,830|457,210|
|2010|324,249|281,170|27,651|487,036|
|2011|306,922|285,790|26,081|469,685|
|2012|298,577|306,469|28,720|456,756|
|2013|290,145|328,521|30,958|481,183|
|2014|286,395|361,004|31,350|626,024|
|2015|271,651|294,087|22,256|531,284|
|2016|211,567|224,835|16,397|421,648|
|2017|207,644|202,533|15,717|370,768|
|2018|189,633|187,725|15,087|356,733|
|N|2,724,620|2,763,314|242,047|4,658,327|



**Sales** 





Figure A.2: Listings across space, 2009-2018 

36 

###### **B Hedonic Regressions** 

In the hedonic regression (1), we control for observed variable characteristics that determine the quality of the listed property. We have at our disposal a set of 76 variables many of which contain missing entries or are sparsely filled. 

We divide the nominal listed price by the monthly CPI and then by the property area to create inflation-adjusted property price per _m_<sup>2</sup> , which is the dependent variable. Second, we use the following explanatory variables: 

- **Number of rooms.** In Germany, the number of rooms excludes kitchens, baths, or corridors. In several cases, the number of rooms is not a natural number, which is not necessarily due to a faulty entry. In Germany, there is the concept of half rooms. Following the DIN 283 norm, a half room is defined as a room with a size between 6 and 10 _m_<sup>2</sup> . While this definition is outdated, it is still frequently in use. In these cases, we round up to the nearest natural integer. Then we created 14 separate dummies (excluding properties with 1 room). 

- **Age of the property.** We deduct the year the listing was posted from the year it was built. Then we create 5-year age dummies. On several occasions the seller lists the price before the property is constructed. We include these entries in the first age category. 

- **Type of property.** We control for 22 detailed types of property: Not specified house, Single-family house (detached), Two-family house, Semi-detached house, Terraced house, Terraced house (middle unit), Terraced house (end unit), Bungalow, Farmhouse, Mansion, Block of flats, Other property for living, Special property, Attic flat, Flat, Raised ground floor flat, Maisonette, Penthouse, Souterrain, Flat with terrace, Other Flat, and Not specified flat. 

- **Cellar.** A dummy variable which indicates that the property has a cellar. 

- **Guest toilet.** A dummy variable which indicates that the property has a guest toilet. 

- **Quarterly dummies.** A set of dummies indicating the quarter the ad was listed. 

37 

###### **C Comparison with Transaction Prices** 

A general concern related to listings data is the lack of transaction prices and information about whether or not a listing resulted in an actual sale or rent. If final transaction prices differ systematically from listing prices, the findings of our paper could potentially be biased. To deal with this issue, we compare our dataset with a transaction-based dataset from an alternative source. We find that levels and trends of these prices, aggregated at the city level, are broadly comparable. 

**German Real Estate Index (GREIX).** A recent study by Amaral et al. (2023) compiles and disseminates quarterly transaction-level real estate data for 18 cities and their neighborhoods in Germany. The German Real Estate Index (GREIX) is based on this work. The raw micro data are collected from historical notarial archives and are then processed and aggregated at the city level across market segments (flats, single-family houses and multi-family houses).<sup>28</sup> 

We compare the transaction-based data from the project with our listings data. Specifically, for every city in their data, we retrieve the average nominal price per square meter from inflation-unadjusted data, separately for flats and single-family houses. We exclude multi-family houses from our comparison due to the challenges in reconciling this market segment in GREIX with the multi-family units in our data. 

In this exercise, we use our raw Immobilienscout24 listings data and apply the same cleaning procedure as Amaral et al. (2023). The goal is to make the two datasets comparable and limit any discrepancy that might arise due to the fact that our cleaning process is more elaborate and restrictive. 

**Flats.** For this comparison, we use the raw data which contains all sale listings for flats in Immobilienscout24. Following the documentation of Amaral et al. (2023), we first remove the listings containing missing prices or living area for each year. Properties already listed on the market but with construction date three years or longer in the future are excluded. Additionally, we winsorize the data at the 1st and 99th percentiles of purchase price and living area in order to remove outliers. We also remove duplicate entries using flats IDs, keeping only the last listed record with identical price and features within a close time frame. Lastly, any repeated entries for the same property within a short period that show price discrepancies are also removed. 

**Single-family houses.** We use the raw data which contains all sale listings for houses in Immobilienscout24. Then, we restrict the data to the following house types: singlefamily house (detached), single-family house, and semi-detached house. We also use listings 

> 28For more information about the data and access, see https://greix.de. 

38 

with missing entries into the house type variable (9% of all listings) as it is likely that the vast majority of these entries may be single-family houses.<sup>29</sup> Further, we impose the same restrictions as in the case of flats. 

Figures C.1 and C.2 show the time series of the average prices per squared meter of flats and single-family houses, both for the listings data and for the transaction data for all cities covered by GREIX. While there are some deviations, the levels and trends are rather similar. 

> 29We also replicate our analysis excluding missing entries and find that the results appear almost identical. 

39 



































Figure C.1: Flats sales prices - transactions vs listings 

40 

























Figure C.2: Single-family house sales prices - transactions vs listings 

41 

###### **D Additional Results** 

###### **D.1 Rental Market** 

Table D.1: Descriptive statistics for Germany, rents 

||2009-10|2011-12|2013-14|2015-16|2017-18|
|---|---|---|---|---|---|
|Log rent ln _r_|1.89|1.91|1.94|1.99|2.07|
|Rent residual _ε_|-0.04|-0.03|-0.01|0.03|0.10|
|Listings _S_|74|73|87|73|56|
|Duration in days _d_|32|27|25|23|22|
|Contacts _C_|484|628|945|1,254|1,490|
|Flow tightness<br>_C_<br>_dS_|0.30|0.47|0.66|1.30|2.02|
|Observations|13,520|13,520|13,520|13,520|13,520|



Notes: Means of selected variables for the baseline sample of location-quarter observations. Rents are in euros and adjusted for inflation using the CPI of the federal states in Germany. 

Table D.2: Descriptive statistics for Top-7 regions, rents 

||2009-10|2011-12|2013-14|2015-16|2017-18|
|---|---|---|---|---|---|
|Log rent ln _r_|2.05|2.08|2.13|2.18|2.28|
|Rent residual _ε_|0.09|0.12|0.15|0.20|0.28|
|Listings _S_|92|86|96|71|51|
|Duration in days _d_|28|24|22|20|18.73|
|Contacts _C_|744|969|1,389|1,718|1,898|
|Flow tightness<br>_C_<br>_dS_|0.43|0.68|0.95|1.83|2.75|
|Observations|5,888|5,888|5,888|5,888|5,888|



Notes: Means of selected variables for the baseline sample of location-quarter observations. Rents are in euros and adjusted for inflation using the CPI of the federal states in Germany. 

42 

Table D.3: Within- and between-location variance decomposition, rents 

||Tot|al varia|nce|With|in loca|tions|Betw|een loca|tions|
|---|---|---|---|---|---|---|---|---|---|
||2009|2013|2018|2009|2013|2018|2009|2013|2018|
|**Full sample**|0.088|0.093|0.106|0.030|0.034|0.035|0.058|0.059|0.071|
|**West Germany**|0.085|0.090|0.104|0.031|0.034|0.037|0.054|0.056|0.068|
|**East Germany**|0.033|0.042|0.043|0.025|0.027|0.025|0.008|0.016|0.018|
|**Top-7 regions**|0.093|0.084|0.098|0.032|0.037|0.040|0.061|0.047|0.058|
|**Urban**|0.091|0.098|0.107|0.030|0.034|0.034|0.062|0.064|0.072|
|**Rural**|0.063|0.066|0.098|0.032|0.032|0.038|0.031|0.034|0.060|



Notes: See the notes to Table 2 for definitions of the different samples. 



Figure D.1: Distribution of residual rents across locations 

Notes: Between-location distributions of residual log rents in the years 2009 (blue), 2012 (orange), 2015 (green) and 2018 (red). The residuals are obtained from hedonic regressions of posted rents per _m_<sup>2</sup> and averaged in each location (postal code). 

43 

Table D.4: Within- and between region variance decomposition, rents 

||Betwee|n-locatio|n variance|Wit|hin regi|ons|Bet|ween reg|ions|
|---|---|---|---|---|---|---|---|---|---|
||2009|2013|2018|2009|2013|2018|2009|2013|2018|
|**Full sample**|0.058|0.059|0.071|0.018|0.021|0.021|0.040|0.039|0.050|
|**West Germany**|0.054|0.056|0.068|0.019|0.022|0.024|0.035|0.034|0.044|
|**East Germany**|0.008|0.016|0.018|0.006|0.010|0.006|0.003|0.006|0.012|
|**Top-7 regions**|0.061|0.047|0.058|0.025|0.031|0.037|0.036|0.017|0.022|
|**Urban**|0.062|0.064|0.072|0.016|0.019|0.019|0.046|0.045|0.054|
|**Rural**|0.031|0.034|0.060|0.009|0.010|0.011|0.022|0.024|0.049|



Notes: See the notes to Table 2 for definitions of the different samples. 

###### **D.2 Further Results for Top-7 Regions** 

Table D.5 shows estimates of the time dummies in the matching function regression (10). Figure D.2 shows time series of the variance of house prices, separate for each of the Top-7 labor market regions. 

44 

Table D.5: Estimates of time fixed effects in equation (10) 

|**t**|**Top-7**|**Berlin**|**Munich**|**Hamburg**|**Frankfurt**|**Stuttgart**|**Dusseldorf**|**Cologne**|
|---|---|---|---|---|---|---|---|---|
|1|0|0|0|0|0|0|0|0|
|2|0.04|0.02|0.07|0.06|0.05|-0.06|0.06|0.06|
|3|-0.01|-0.05|0.06|0.04|-0.01|0|-0.03|-0.04|
|4|-0.1|-0.1|-0.01|-0.01|-0.12|-0.15|-0.16|-0.13|
|5|-0.02|-0.06|0.02|0.05|0|-0.1|0.02|0.02|
|6|0.03|-0.04|0.11|0.17|0.09|-0.06|0.03|0.01|
|7|0.07|-0.02|0.08|0.21|0.17|-0.02|0.13|0.07|
|8|0.07|-0.02|0.1|0.25|0.14|-0.07|0.14|0.08|
|9|0.03|-0.02|0.11|0.09|0.03|-0.02|0.11|0.04|
|10|0.01|-0.06|0.06|0.09|0.03|-0.08|0.11|0.04|
|11|-0.01|0|0.02|0.06|-0.05|-0.15|0.08|0.1|
|12|-0.01|-0.07|-0.04|0.08|0.06|-0.14|0.08|0.07|
|13|0.02|-0.04|0.08|0.06|0.13|-0.09|0.03|0.1|
|14|0.01|-0.06|0.08|0.07|0.07|-0.15|0.11|0.08|
|15|0.02|-0.09|0.12|0.11|0|-0.08|0.15|0.12|
|16|0.01|-0.09|0.12|0.15|-0.03|-0.1|0.1|0.15|
|17|-0.04|-0.15|0.07|0.13|0|-0.19|0.03|0|
|18|-0.03|-0.14|0.06|0.16|0.01|-0.13|0.03|-0.04|
|19|-0.05|-0.17|0.09|0.08|0.01|-0.16|0|-0.01|
|20|-0.05|-0.16|0.1|0.12|0.02|-0.09|-0.1|0|
|21|-0.04|-0.15|0.16|0.11|-0.03|-0.01|-0.04|-0.01|
|22|0.01|-0.05|0.19|0.1|0.01|0.01|0.05|-0.06|
|23|0.04|-0.03|0.23|0.16|0.11|0.03|0.03|-0.05|
|24|0.06|-0.03|0.23|0.15|0.21|0.07|0.05|-0.04|
|25|0.11|0.07|0.21|0.24|0.11|0.1|0.21|0.09|
|26|0.09|0.05|0.13|0.2|0.17|0.04|0.2|0.13|
|27|0.07|-0.02|0.18|0.24|0.14|0.1|0.14|-0.04|
|28|0.08|0.01|0.3|0.25|0.04|0.06|0.18|0|
|29|0.13|0.07|0.35|0.21|0.19|0.07|0.15|0.12|
|30|0.19|0.2|0.36|0.26|0.21|0.1|0.27|0.18|
|31|0.24|0.26|0.46|0.3|0.15|0.16|0.33|0.24|
|32|0.22|0.37|0.36|0.24|0.17|0.14|0.24|0.19|
|33|0.2|0.26|0.39|0.22|0.2|0.09|0.29|0.12|
|34|0.21|0.26|0.39|0.2|0.28|0.18|0.21|0.12|
|35|0.18|0.24|0.45|0.22|0.21|0.09|0.12|0.09|
|36|0.18|0.22|0.44|0.16|0.23|0.13|0.18|0.07|
|37|0.2|0.28|0.42|0.24|0.28|0.11|0.12|0.1|
|38|0.25|0.37|0.41|0.17|0.37|0.17|0.23|0.11|
|39|0.22|0.36|0.45|0.19|0.24|0.17|0.17|0.11|
|40|0.21|0.39|0.4|0.24|0.23|0.13|0.14|0.04|



Notes: This table shows the estimated _gt_ (time-fixed effects for quarters 2009Q1–2018Q4) in equation (10) separately for each Top-7 labor market region. 

45 













Figure D.2: Price dispersion in selected regions 

Notes: This figure shows the dispersion of the residualized log prices from the first quarter of 2009 to the last quarter of 2018. The blue solid lines show the unweighted dispersion and the black dashed lines the weighted dispersion based on the number of listings in each postal code. 

46 

###### **E Variance Decomposition Derivations** 

###### **Proof of Decomposition (2)** 

Write _H_ for the set of listings and _Hi_ for the set of listings in location _i_ . Write _n_ for the cardinality of _H_ and _ni_ for the cardinality of _Hi_ . 



###### **Proof of Decomposition (3)** 



47 

###### **F Numerical Solution of the Model** 

The equations which characterize the solution of the model as explained in Sections 3 and 4 are: 



This is a high-dimensional system of (3 _N_ + 1)( _T_ + 1) + 1 equations with (3 _N_ + 1)( _T_ + 1) + 1 unknowns which are ( _Ait_ )<sup>_T_</sup> _t_ =1<sup>, (</sup><sup>_V_</sup> _it_<sup>_B, V_</sup> _it_<sup>_S_)</sup><sup>_T_</sup> _t_ =1<sup>+1,</sup><sup>_τi_for</sup><sup>_i_= 1</sup><sup>_, . . . , N_,</sup><sup>_λ_, and (¯</sup><sup>_V_</sup> _t_<sup>_B_)</sup><sup>_T_</sup> _t_ =1<sup>+1.All equations</sup> except (4) are linear. So for a given guess of _V_<sup>¯</sup> _t_<sup>_B_</sup> +1<sup>for</sup><sup>_t_=1</sup><sup>_, ..., T_+ 1,webackoutallthe</sup> remaining unknowns by elementary linear algebra. 

The steps of the solution procedure are: 

1. Start with an arbitrary guess of _V_<sup>¯</sup> _t_<sup>_B_</sup> +1<sup>for</sup><sup>_t_= 1</sup><sup>_, ..., T_+ 1.</sup> 

- – – 

- 2. Solve equations (5) (7) , (16) (17) and (14) (15) with matrix inversion. 

3. Use the values of _τi_ together with _Vi,t_<sup>_B_for all</sup><sup>_i_and</sup><sup>_t_= 1</sup><sup>_, . . . , T_+1 to obtain new values</sup> of _V_<sup>¯</sup> _t_<sup>_B_</sup> +1<sup>for</sup><sup>_t_= 1</sup><sup>_, ..., T_+ 1</sup> 

4. Using the new values of _V_<sup>¯</sup> _t_<sup>_B_</sup> +1<sup>,repeatsteps2-3untiltheroutineconverges.</sup> 

48 

