# The Microgeography of Housing Supply<sup>*</sup> 

Nathaniel Baum-Snow, University of Toronto Lu Han, University of Toronto 

December 8, 2019 

##### **Abstract** 

Housing supply elasticities are central parameters required for quantitative analysis addressing a wide range of questions in urban and real estate economics. Despite huge variation across neighborhoods within metro areas, researchers often employ metro area level supply elasticity estimates to analyze neighborhood level phenomena due to lack of neighborhood level estimates. Moreover, there exists scant quasi-experimental evidence about the components of new housing services supply. This paper reports housing supply elasticity estimates for most U.S. urban neighborhoods and demonstrates the importance of accounting for neighborhood level heterogeneity within metro areas. Supply elasticity estimates for housing services are decomposed into those for housing units on newly developed land, already developed land and the intensive margin of supply. Consistent with housing production function estimates from the literature, estimated neighborhood level elasticities of the supply of housing services with respect to price is between 2.5 and 4.3 on average across urban census tracts. The average price elasticity of quantity of new units supplied is 0.2 to 0.9, with about one-third of this response due to redevelopment. Supply elasticity increases with CBD distance, in part because of increasing neighborhood land availability from reductions in the fraction already developed. Tracts with flat land also exhibit more elastic supply. Conditional on census tract level measures of land unavailability, analogous metro area measures do not significantly influence tract level supply estimates. Identification comes from variation in labor demand shocks to commuting destinations, as aggregated using an urban economic geography model. Aggregation of neighborhood level supply elasticities yields metro area supply elasticities that are correlated with but smaller than those reported in Saiz (2010). 

> *We thank Camilo Acosta, Rolando Campusano and Ian Herzog for excellent research assistance. 

1 

## **1 Introduction** 

Housing supply conditions vary considerably both between and within urban areas. While the existing literature documents large differences in housing supply elasticities between cities (Saiz, 2010; Cosman, Davidoff, & Williams, 2018), little empirical evidence exists on how supply elasticities differ _within cities_ as a function of distance to the center, land availability, building densities and zoning restrictions. Knowledge of housing supply elasticities at a microgeographic scale is central to understanding spatial variation in booms and busts within housing markets (Glaeser, Gottlieb, & Tobio, 2012; Guerrieri, Hartley, & Hurst, 2013), growth patterns at urban fringes (Glaeser, Gyourko, & Saks, 2005), consequences of neighborhood specific labor or housing demand shocks (Calabrese, Epple, & Romano, 2011; Couture, Gaubert, Handbury, & Hurst, 2019) and implications of place-based policy interventions such as targeted neighborhood investment, land use restrictions, and transportation infrastructure investments (Busso, Gregory, & Kline, 2013; Hanson, 2009). The main aim of this study is to empirically characterize housing supply elasticities for all residential neighborhoods in 306 U.S. metro areas. We also decompose supply responses of total housing services into units and quality components. Within the units component, we further decompose into redevelopment of existing developed areas versus newly developed land. We demonstrate how housing supply conditions vary by neighborhood location, available land, topography and regulation. Finally, we consider aggregation of neighborhood housing supply elasticities to the metro area level. In this aggregation exercise, a number of pitfalls emerge, which highlight the difficulty of interpreting metro area level elasticities in many contexts. 

Average supply elasticity estimates are in the 0.2 to 0.9 range for housing units and in the 2.5 to 4.3 range for housing services across neighborhoods in our data, with about one-third of the unit supply response coming through land redevelopment. These supply responses grow with distance from central business districts (CBDs) such that unit and housing services supply elasticites at CBDs are on average 0.2 and 3.8 respectively, growing to 1.5 and 4.3 respectively at urban fringes. In addition, supply responds in expected directions to the fraction of neighborhood land area that is already developed and has steep slopes. Tracts in areas with more stringent regulation, as measured by Floor-Area-Ratio restrictions (Brueckner & Singh, 2018), are less responsive in supply. Resulting estimates range from 0.1 to 1.5 for the 5th and 95th percentile neighborhoods for unit supply and 2.2 to 5.2 respectively for housing services supply. While we face some sta- 

2 

tistical power constraints for isolating variation in supply elasticities between metros as functions of land developed fraction, topography, and regulation, we do not find evidence that metro level factors matter for local supply elasticities conditional on neighborhood topography and land development patterns. Using data from the US and Switzerland respectively, Orlando and Redfearn (2018) and von Ehrlich, Schöni, and Büchler (2018) find even smaller unit supply elasticities at the municipal level, though these papers also find that supply elasticities increase with CBD distance. 

Supply elasticity estimates for housing services are quantitatively consistent with housing production function estimates in the literature. These indicate approximately Cobb-Douglas form with a land share of 0.2-0.35 (Ahlfeldt & McMillen, 2014; Combes, Duranton, & Gobillon, 2019; Albouy & Ehrlich, 2012), implying housing services supply elasticities of 2-4. Our tract level unit supply estimates are mostly smaller than those found in Saiz (2010) for the metro level. One reason is that aggregation from micro to macro elasticities incorporates substitution patterns across neighborhoods in residents’ neighborhood demand system. As neighborhoods become stronger demand substitutes, a shock affecting (for example) labor market opportunities in one location affects housing demand in a wider range of areas as households are more willing to substitute across residential options to take advantage of lower housing prices in some places. This opens up more opportunities for supply elastic neighborhoods to be included. The result is aggregation to macro supply elasticities that are greater than tract level elasticities. However, we note that macro elasticities are specific to the nature of the demand shock. This motivates us to explore aggregation using estimated demand parameters and shocks generated by a specific place based policy in an urban market access model similar to that in Tsivanidis (2018) (in progress). 

We approach recovery of neighborhood level housing supply elasticities as the fundamentally reduced form problem of identifying coefficients in regressions of changes in tract level housing quantities on changes in a tract level house price index. The central challenge is to find an exogenous source of variation that shifts neighborhood level housing demand but not local fundamentals including construction costs. This identification challenge is particularly daunting for recovering within-city supply elasticities, as most shocks that impact housing demand in one neighborhood would also affect housing demand for nearby neighborhoods, making it difficult to trace out housing supply in any specific neighborhood. To achieve identification, similar to Severen (2019) we use Bartik (1991) type labor demand shocks to commuting destinations from 

3 

each residential location as the fundamental source of variation in housing demand shocks, which feed through the commute time matrix to generate exogenous variation in changes in house prices in residential locations. These labor demand shocks depend on 1990 industry shares in commuting destinations interacted with national industry-specific employment growth rates after year 2000. 

One practical challenge is in how to sensibly aggregate these labor demand shocks across all commuting destinations from each residential tract. To do this, we follow Tsivanidis (2018) and nest our reduced form estimation problem in an urban spatial equilibrium model in which residential demand in neighborhood _i_ depends on “resident market access” ( _RMAi_ ), a coherent measure of access to employment from tract _i_ . _RMAi_ amounts to the commute time discounted sum of employment in each commuting destination from location _i_ . Labor demand shocks in each potential commuting destination are used to generate a simulated counterpart to the change in _RMAi_ that, conditional on appropriate controls, is purged of shocks to tract housing productivity or changes in other unobserved tract level housing supply factors. 

Beyond contributing to the housing production function and supply elasticity literatures, we hope our supply estimates will be useful both for policy evaluation and to help improve understanding of patterns of neighborhood change. For example, our micro scale estimates provide a supply-side explanation for the recent finding that there was more price growth in the center of metro areas in the 2002-2007 housing boom (Glaeser et al., 2012; Genesove & Han, 2013). On the other hand, the greater house price fluctuations at metro area edges where housing is the most land intensive (Zhou & Haurin, 2010) seem most likely driven by demand fluctuations. A burgeoning literature examines policies and phenomena that only directly impact a few neighborhoods in cities in the context of general equilibrium urban models. These studies typically calibrate micro elasticities to macro estimates from the literature. Our evidence shows that this choice can lead to misleading conclusions about incidence. In particular, landowners in the supply inelastic neighborhoods nearer to CBDs may enjoy most of the gains or bear most of the burdens even if at the metro area level housing supply is elastic. We thus hope that our supply elasticity estimates are useful for improving quantitative evaluation of various policies that are targeted to particular neighborhoods. 

As an illustrative example, we explore the incidence of the recently implemented Opportunity 

4 

Zone (OZ) program, which was part of the “Tax Cuts and Jobs Act” (TCJA) of 2017. This program rebates capital gains taxes back to investors for real estate and other investments that occur in certain low income census tracts. We use our neighborhood level supply elasticity estimates coupled with structurally estimated housing demand parameters from our economic geography model to recover the impacts of the OZ program on consumer and producer surplus, and its deadweight loss at the tract level. Because of such variation in supply elasticities, we find a huge variation in these impacts across neighborhoods, even within metro areas. In downtown neighborhoods, where housing supply is relatively inelastic, we show that this program generates large gains for developers and investors and small gains for households (in progress). 

## **2 Data** 

For this analysis, we construct a data set that brings together information from a number of different sources. Using the Zillow ZTRAX transactions, assessments and historical assessments data files, we build quality-adjusted house price growth between 2000 and 2010 for census tracts in 306 metro areas using both repeat sales and hedonic approaches. We use the same data sources to construct a rich set of housing supply measures including changes in housing stocks, new construction, quality-adjusted changes in housing stocks, floorspace, and redevelopment through both renovation and teardowns, all at the tract level. Local labor demand conditions are measured using the place of work and journey to work tabulations in the 1990 and 2000 U.S. Censuses of Population and the 2006 and 2010 LODES data plus census tract aggregate data from 1990-2010. Finally, we use remote sensing information on land cover in 2001 to measure baseline tract development intensity, topography and prevalence of wetlands. All data are keyed to 2000 definition census tracts, covering 63,897 tracts in 306 metro areas (with some overlap across metros). Below we describe in more detail how we process each data source. 

### **2.1 Housing Prices** 

Our primary source for housing data is the Zillow ZTRAX data sets (Zillow, 2017). These come in the form of files for transactions, most recent assessments before 2017 and prior assessments. These data cover more of the U.S. over time from 2000 to 2010, going from coverage of at least 

5 

part of 267 metro areas and about two-thirds of sample tracts to the full study area by 2010, with a few exceptions noted below. Because of incomplete coverage, particularly in year 2000, we supplement Zillow data with decennial Census data, as is explained in further detail below. 

Transactions information is constructed from information in local Recorders of Deeds and includes the sale price, location and some property attributes. To fill out property attributes, we merge it with the most recent assessment data. We primarily use this data set to construct price indexes at the census tract level. For the purpose of building home price indexes, we only use arm’s length transactions for resale or new construction. This excludes deed transfers involving non-transactions such as foreclosure by banks or quitclaim deeds. We include all residential units, including single family houses, semi-detached and condominiums. We consider only homes that are bought by individual buyers and do not examine institutional buyers. We always exclude homes that sell more than 9 times over our sample period. Our main use of the ZTRAX data is to build home price indexes at the census tract level. 

A well-known challenge for constructing home price indexes is that homes are heterogeneous in observed and unobserved attributes. The goal of the indexes is to hold quality constant, eliminating all price variation due to differences in attributes. Leveraging the richness of assessment data on home characteristics, we use census tract-region-year fixed effects _airt_<sup>_HI_from the following</sup> hedonic regression to build our Hedonic Index (HI). 



Here, _h_ indexes homes in census tract _i_ , region _r_ , year _t_ and month _m_ . _Xhirtm_ includes a rich set of characteristics (including unit type, rooms, bedrooms, kitchens, bathrooms, heating and AC, elevator, fireplace, water, sewer, roof type, age, floorspace and lot size). Month of sale fixed effects _ρm_<sup>_HI_flexiblyaccountforseasonalityinmarketconditions.Inclusionofcontrolsforregionfixed</sup> effects throughout the main empirical analysis below ensures that comparisons are always made across locations within metro regions. Due to incomplete coverage in the ZTRAX data set and our inclusion of tracts with at least 10 valid home sales in relevant sample years, this index covers only about two-thirds of our full tract sample. 

To fill out the tract sample with some measure of house prices for 2000 and 2010 and to facilitate looking at pre-trends, we also build a lower quality hedonic price index using self-reported data from the 1990 and 2000 Censuses of Housing and the 2008-2012 ACS aggregated to the census 

6 

tract level. These are tract residuals _airt_<sup>_C_fromthefollowingcross-sectionalregressionsestimated</sup> separately for 1990, 2000 and 2010: 



Here, _Pirt_<sup>_C_istheaverageself-reportedvalueofowner-occupiedhomesinthetractandincluded</sup> in _X_<sup>_C_fractionsofthetract’sowner-occupiedunitsinvariousbuildingtypes,withvarious</sup> _irt_<sup>are</sup> numbers of bedrooms, and of various vintages. While it is of lower quality, this index covers all census tracts in our sample regions. 

Hedonic indexes do not account for unobserved heterogeneity in quality across homes. To account for this, we also use the ZTRAX data set to build a repeat sales index at the tract-year level. For this index, we exclude any sales fewer than 180 days after the prior sale. Inclusion of home fixed effects _αhir_<sup>_RS_inthefollowingregressionpurgesindividualhomeheterogeneitythatis</sup> fixed over time. Tract-year fixed effects _airt_<sup>_RS_from this regression are our repeat sales index.</sup> 



After homes are renovated, we treat them as new homes for the purpose of constructing this index. We recognize that this index may suffer from a more biased sample than the hedonic index and incorporate unwanted capitalization of unobserved home improvements. 

The top block in Table 1 presents summary statistics about changes in these three home price indexes for the primary estimation sample used for the empirical work. The Zillow hedonic price index growth is 0.89 on average across tracts relative to 0.95 for repeat sales index growth during the 2000-2006 periods. For 2000-2010, average growth rates are 0.37 and 0.45 respectively, reflecting the 2007-2008 housing market crash. Correlations between the two Zillow indexes is 0.63 for the 2000-2010 period but the correlation with the growth in the Census price index is only about 0.10 for both Zillow based indexes. Nevertheless, we will see below that all three price indexes generate similar housing supply elasticity estimates. 

### **2.2 Satellite Data** 

We use remote sensing information to measure tract level topography and land development intensity. Topography is one of the most important factors influencing construction costs and ulti- 

7 

mately housing supply. Land cover information is used to help determine whether new housing is built on previously undeveloped land. 

We use three remote sensing data sets to obtain land cover and slope. First, the “Scientific Investigations Map 3085” is derived from the US Geological Survey’s National Elevation Database. The Map 3085 data uses raster information on slope and elevation range for all 30X30 meter land pixels within a 0.56 km radius (1 sq. km) of each pixel to classify it into one of nine categories that describe how flat or hilly the surrounding area is. We aggregate these categories into “flat plains”, “flat non-plains” and “hilly”. Flat plains have a slope of less than 8% in more than half of these nearby pixels and an elevation range of less than 15 meters in this 1 km sq region. On average 41% of tract land area is flat plains. Flat non-plains have a slope of less than 8% in more than half of pixels within 1 sq km and a larger elevation range. On average, 45% of tract land area is flat non-plains. Remaining land is hilly. We take elevation range within 1 km of each pixel directly from the US Geological Survey National Elevation 1/9-1/3-1-2 arc second Database. 

Development costs not only depend on topographical conditions but also the initial developed state. We construct tract developed fraction from the National Land Cover Database (NLCDB) for 2001 and 2011. In particular, the NLCDB provides for each 30X30 meter cell one of 4 categories of development (0-19%, 20-49%, 50-79%, 80-100%). We construct the square meters of land in each tract by density of development and aggregate to impute developed fraction for the land area of each census tract. The average tract in our sample had 38% of land area developed in 2001 and 39% in 2011.<sup>1</sup> 

We aggregate the resulting tract level data to construct various land unavailability measures for each metro area. To be consistent with Saiz (2010), we calculate the fraction of area within 50 km of the CBD of each region that is undevelopable due to a steep slope (e.g. mountains), water or wetlands (e.g. oceans, lakes, etc) and that is developed. We also build variants of these two measures instead aggregating to the metro area level and within 50% or 100% radii from the CBD to the furthest tract in the metro area. As these measures are highly correlated, our estimation results are not sensitive to the choice of aggregation. 

> 1As satellite data has been documented to measure changes in land cover with high error rates ((Torchiana, Rosenbaum, Scott, & Souza-Rodrigues, n.d.)), we only use levels of this variable in the empirical analysis. 

8 

### **2.3 Housing Quantities** 

We construct six measures of housing quantity changes to cover different aspects of supply responses. As most of the existing literature on housing supply focuses on units in the housing stock, we begin with this measure. However, we also aim to explicitly measure new construction and to quality adjust the stock, which the detailed Zillow assessment data allows for. However, since the Zillow data has incomplete coverage at the beginning of the sample, most of our stock measures rely on 2000 census data for the base year. 

To organize our classification of stock measures, we begin by noting that the total quantity of efficiency units of housing services in census tract _i_ , _Hi_<sup>_e f_, is the number of housing units</sup><sup>_Hi_times</sup> the average quantity of services provided per housing unit _Si_ . Differentiating, the growth rate in the quantity of housing services over time can be written as follows: 



We separate out our measures of the total change in housing services in tract _i_ into these three _<u>i</u>_<sup>_dHR_</sup> components. New construction is broken into that on existing developed land _Hi_<sup>and on unde-</sup> _<u>i</u>_ veloped land<sup>_dH_</sup> _Hi_<sup>_U_.We call the former “redevelopment”.The third term is negative and captures</sup> teardowns and the housing units that fully depreciate away. Finally, the intensive margin component _d_ ln _Si_ is a residual that includes partial depreciation, remodeling and the quality of new construction units relative to that for units in the base period. 

#### **2.3.1 Housing Units and Total New Construction** 

The simplest quantity measures are the 1990-2000 and 2000-2010 growth rates in tract level housing occupied unit stock constructed using the 100% count Decennial Census data<sup>_dH_</sup> _Hi_<sup>_<u>i</u>_.Weuse</sup> occupied units instead of all units to be consistent with Saiz (2010) and because vacant units may be under-reported or not habitable. While it has the best neighborhood coverage, this measure is not an ideal new supply measure as it includes teardowns and depreciation. 

_<u>i</u>_<sup>+</sup><sup>_dH_</sup> _<u>i</u>_<sup>_UdHR_</sup> We separate out new construction _Hi_ using information on building age in the ACS and ZTRAX data sets. In the 2008-2012 ACS tract aggregates, we observe the number of units in the stock built between 2000 and 2009. Following the ZTRAX historical assessment data forward, we 

9 

record the earliest year built after 2000 for every housing unit in the ZTRAX data set.<sup>2</sup> Beause of incomplete ZTRAX coverage in the earlier part of our sample and to be consistent across measures, we use the occupied housing stock reported in the 2000 census as a base for both measures. As the ACS is based on a 5% sample of occupied units while ZTRAX in principle covers the universe of new construction, the ZTRAX measure is more accurate. 

Summary statistics for these three measures are presented in the second block of Table 1. Here we see that for the 2000-20009 calendar years, the average number of new construction units across tracts in our sample, counted using both the ACS and Zillow data, are very close at about 235, or about 11 percent growth over the base in 2000. The average census growth number for the same period, which incorporates fully depreciated or torn down units, is 181 or 7 percent growth. Pairwise correlations between these three measures are all over 0.91. 

#### **2.3.2 Redevelopment New Construction Units** 

Redevelopment ( _dHi_<sup>_R_)isanimportantcomponentofhousingsupply,asitmayhaveadifferent</sup> cost structure than new construction on undeveloped land. Moreover, in cities where building density is already high, builders can only increase housing supply through redevelopment. Urban redevelopment can take many forms, including teardowns and infills, which became widespread during the housing boom of the 2000s. At the peak, the number of demolitions and teardowns in the Chicago metropolitan area approached 40% of sales in 2005 (McMillen & O’Sullivan, 2013). In New York City, annual teardown activity increased almost eight-fold from 1994 to 2004 and peaked in 2005 (Been, Ellen, & Gedal, 2009). 

Lacking data on demolition permits or infill construction, we quantify the units built through redevelopment by imputing the number of units built on already developed land in the calendar years 2000 through 2009 as follows. We assume that each tract’s stock of units reported in the 2010 census is uniformly spatially distributed across the tract’s developed area as measured using the 2011 satellite data. We subtract off the number of ACS reported new construction units 2000-2009 that is imputed to be on newly developed land using this assumption from 2010/2011 about the spatial distribution of housing units in each tract. We infer that the remainder of 2000-2009 new 

> 2Some rental buildings only report total square footage and do not break out the number of units. In these cases, we impute the number of rental units using the average square footage of units in other rental and condominium buildings of similar size in the tract. 

10 

construction is from redevelopment. If this remainder is negative, we assign 0 units to redevelopment. Our measure indicates that about 40% of new construction in an average tract in our sample is redevelopment. 

#### **2.3.3 Efficiency Units of Housing** 

In the context of the model developed below, the tract efficiency units of housing services _Hi_<sup>_e f_,</sup> including the intensive margin of supply, is the most conceptually relevant measure. If recently built housing units are larger than those built in early 2000s, then using either the difference in stocks or new construction would underestimate the true housing supply response. Moreover, we wish to have some way of capturing upgrades to the existing stock.<sup>3</sup> 

We construct two such efficiency units meausres. First, we simply use the total floorspace of assessed housing units in each tract, as reported in the Zillow Historical Assessments data. Second, we use the Zillow data to construct a tract level quality-adjusted housing quantity index. We start by constructing weights for each housing attribute using transactions data from 2006 only. We choose 2006 because this is the first year with near universal coverage in our sample area. For all census tracts with at least 10 transactions, we estimate coefficients in the following hedonic regression: 



.Here, _Xhir_ includes property age, age squared, floorspace, floorspace squared and home type dummies and _ϵir_ are census tract fixed effects. _β_<sup>_W_</sup> is a vector of hedonic weights that indicate the amount of housing services provided by each attribute in 2006. These attribute prices that are common across locations and are applied in subsequent years. We take the universe of (assessed) housing units in each tract and year and calculate _Hhirt_<sup>_e f_=</sup><sup>_exp_(</sup><sup>_Xhirt_ˆ</sup><sup>_βW_).Thestockofhousing</sup> services in tract _i_ at time _t_ is then _Hirt_<sup>_e f_=∑</sup><sup>_hH_</sup> _hirt_<sup>_e f_.Thismeasureishighlycorrelatedwithtotal</sup> floorspace. 

3The challenge of separating between the price of housing per unit and the quality-adjusted amount of housing is well-established in the housing production literature Ahlfeldt and McMillen (2014); Combes et al. (2019); “Housing Productivity and the Social Cost of Land-Use Restrictions” (n.d.). As noted in Epple, Gordon, and Sieg (2010), “houses are viewed as differing only in the quantity of service they provide, with housing service being homogenous and indivisible.” 

11 

#### **2.3.4 Average Unit Quality** 

Our final measure of housing quantity change is the (residual) intensive margin of housing supply holding the number of units fixed _d_ ln _Si_ . Renovation is an important supply substitute for new construction. Choi, Hong, and Scheinkman (2014) report that American home improvement expenditures increased from about 1% of gross domestic product (GDP) ($229 billion) in 2003 to 2% of GDP ($326 billion) in 2007.<sup>4</sup> Despite its importance, renovation has often been ignored in the literature on housing supply (DiPasquale, 1999). We capture this important dimension (both renovation of existing units and upsizing in newly built units) by taking the difference between the quality-adjusted housing quantity change and the census-measured change in housing units. That is, _d_ ln _Si_ = _d_ ln _Hi_<sup>_e f−dlnHi_.</sup> 

### **2.4 Population, Employment and Commutes** 

The Census Transportation Planning Package (CTPP) reports tabulations of 1990 and 2000 census data by residential location, work location and commuting flow. 1990 CTPP geography determines our study regions. The 1990 CTPP assigns microgeographic units the size of census tracts or smaller to “regions”, which roughly correspond to metropolitan areas. These regions can overlap. Commuting flows and times are reported for pairs of census tracts, traffic analysis zones or block groups within each region only. Employment by place of work, sex and 18 industry groups are reported for these same geographic units. For Connecticut and New Jersey, which are fully contained in one large 1990 CTPP region each, we develop new regions that each have a 25 km radius around each CBD in each state. We map 1990 CTPP geography to 2000 definition census tracts by overlaying their digital maps and using land area as allocation weights. The 2000 CTPP is more spatially comprehensive and thus can be restricted to cover only 1990 region definition geography. The result is a total of 63,896 2000-definition census tracts in 306 regions. 

For most regions, central business district (CBD) locations are taken as the centroid of the set of census tracts reported as being in the CBD in the 1982 Economic Census. Remaining CBD assignment is done by eyeballing a location that is near city hall and the most historical bank 4According to Bendimerad (2007), Americans spent $280 billion on home remodeling in 2005, and this number was projected to increase at 3.7% in real terms by 2015. Plaut and Plaut (2010) further report that almost half of American home owners made some renovations during 2003-2004. 

12 

branches in the region’s largest city. 

Empirical implementation requires information on the commute time between each pair of census tracts in each region. Because they are based on only a sample and flows of fewer than 5 sampled workers are suppressed, commutes are not observed between about one-half of tract pairs in 1990 and two-thirds of tract pairs in 2000. To fill in the rest, we develop a forecasting model based on tract relative locations. In particular, we predict origin-destination commute times using out of sample predictions from a regression of log travel time on region fixed effects, log travel distance, log CBD distance of workplace and log CBD distance of residence. See Baum-Snow, Hartley, and Lee (2019) for details. 

For 2006 and 2010, we use the LEHD origin destination employment statistics (LODES) data to measure employment by place of work. As this data set does not have commute times, we maintain year 2000 commute times for these later years. 

We take census tract aggregates for 1970-2010 from the Neighborhood Change Database supplemented with some Summary Tape File 4 variables from 1980. We use these variables to measure aggregate outcomes and to control for pre-treatment trends in observables. 

### **2.5 WRLURI and FAR** 

The Wharton Residential Land Use Regulatory Index (WRLURI) is constructed from a battery of survey questions sent to a weighted random sample of municipalities nationwide in the US in year 2005. The index is expressed in population-weighted standard deviation units. While larger urban municipalities were sampled with higher probability, a large number of smaller suburban municipalities were also included in the sample. 261 of the 306 regions in our sample have at least one municipality surveyed. However, the municipality of the CBD is sampled in only 164 of our sample regions. Overall, our data includes 2,373 municipalities and 30,526 tracts with WRLURI information. 

We incorporate data on Floor Area Ratio (FAR) restrictions on residential development from the municipalities of Atlanta, Boston, Chicago, Denver, Los Angeles, New York, San Francisco, and Washington.<sup>5</sup> For each residential land parcel, local zoning maps provide the residential FAR. We use the average of these within each census tract, weighted by parcel area. 

> 5Most of these data were generously provided by Ruchi Singh (Brueckner & Singh, 2018). 

13 

### **2.6 Estimation Sample** 

Our analysis requires reliable information on housing quantities. To this end, we only include census tracts with Zillow unit counts that are close to 2010 100% census counts. In particular, we exclude all tracts from the estimation sample for which our 2010 Zillow unit stock is more than 20% above or below the occupied housing stock reported in the 2010 census. Unless the 2000 Zillow stock is within 20% of its 2000 census counterpart, we also exclude tracts in nondisclosure states for which Zillow reports they have incomplete coverage.<sup>6</sup> For these tracts, we are particularly concerned about under-measurement of 2000-2010 new construction. As a result, our sample is cut in about half, from 63,896 tracts in 306 regions to 31,242 tracts in 275 regions. Beyond this initial sample restriction, we lose about 7,000 additional observations because we lack ZTRAX based price index data for year 2000. Primary estimation sample sizes are reported in the top two blocks of Table 1. 

For building instruments and for structural estimation of the model, we also need information on labor market opportunities that are relevant to each sample census tract. Because the CTPP and LODES data sets fully cover our sample area, these data sets do not introduce any sample constraints for our analysis. 

## **3 Conceptual Framework** 

The main object of our analysis is to estimate housing supply elasticities that are allowed to differ flexibly across neighborhoods and regions. While we use the decomposition in (1), developed further below, to study different components of supply, we intentionally impose as little structure as possible on the form of the housing supply function. 

As such, we focus on estimating _γir_ in the following reduced form expression. _Hir_<sup>_s_denotes any</sup> of the quantity measures listed in (1). _Pir_ is the observed price per unit of housing services in our data. To accommodate ad-valorem taxes, we can think of the price developers receive per unit of housing sold _Pir_<sup>_s_as</sup><sup>_Pir_(1</sup><sup>_−tr_).Region fixed effects</sup><sup>_mr_thus capture potential tax wedges and other</sup> 

> 6These states are Alaska, Idaho, Kansas, Louisiana, Mississippi, Missouri, Montana, New Mexico, North Dakota, Texas, Utah, and Wyoming. 

14 

region-specific factors that influence construction costs. 



In the empirical work, _uir_ includes supply shifters and the error and we allow _γir_ to depend on tracts’ observed heterogeneity, including initial building density, geographic features and distance to the central business district. Because of the durability and immobility of housing, (2) is likely to hold with a greater _γir_ for price growth than for price declines Glaeser and Gyourko (2005). Largely for this reason, our analysis focuses on demand shocks in the 2000-2006 period. During this time, price growth was positive in over 98 percent of the tracts in our sample, more so than for any other time period in our data. 

In this section, we first lay out relevant microfoundations for housing supply in our context and then we lay out the theory behind the procedure we use to construct demand shocks necessary to pin down consistent estimates of _γir_ . 

### **3.1 A Theory of Neighborhood Housing Supply** 

While microfoundations are not required to use our supply elasticity results, they do help to understand magnitudes of our empirical results reported below. Indeed, conceptual development beyond simple aggregation of individual housing production functions is needed to justify our differing price elasticity estimates for different components of supply. To fix ideas about what our different elasticity measures deliver and how to combine them, here we sketch a model of housing supply to neighborhood _i_ . 

We begin with market structure and technology and then add land availability and redevelopment constraints. We assume that the amount of housing services on each parcel _Si_ is supplied by a developer in a perfectly competitive market. Developers combine land and capital with productivity that can differ across neighborhoods. Each building site _s_ in neighborhood _i_ has a fixed lot size _Mi_ and a heterogeneous fixed development cost of _fis_ . _fis_ captures development fees and permitting costs plus land preparation costs for development, be it demolition and environmental remediation of existing construction or grading and draining of undeveloped land. The fixed development lot size assumption reflects land assembly frictions that are likely to bind over the 5-10 year time horizon that is the focus of our empirical analysis (Brooks & Lutz, 2016). Demand conditions and the cost of capital determine the intensity of new development on any given plot in a 

15 

neighborhood. The price per unit of housing services _Pi_ is the same for all parcels in neighborhood _i_ . 

Following is a representative developer’s profit associated with building on parcel _s_ in neighborhood _i_ . 



Here _C_ ( _Si_ ) is the variable cost and _p_ ( _fis_ ) is the endogenous parcel acquisition price. Imposing 0 profits and perfect competition (marginal cost pricing), we have 



Because of the fixed lot size, the variable cost function is likely convex and so<sup>_<u>d</u>_</sup> _d_<sup><u>ln</u></sup> ln<sup>_<u>C</u>_</sup> _S_<sup>_>_1.The</sup> first term reflects the intuition that higher housing prices imply higher marginal costs and greater profits absent land costs. The second term reflects capitalization of fixed development cost into the parcel price. 

Consistent with housing production function estimates in the literature, we proceed assuming Cobb-Douglas production with a land share of _α_ and productivity _ρi_ . This implies a parcel-specific <u>1</u> _−α_ <u>1</u> housing services supply function of _Si_ ( _Pi_ ) = _ρiPi α_ and that _p_ ( _fis_ ) = _αρiPiα_<sup>_−fis_.7</sup><sup>_Si_canbe</sup> thought of as floorspace installed on a newly developed land parcel in tract _i_ . If the tract has a high price, the developer may find it optimal to partition that floorspace into multiple units. 

Each tract has a CDF of the fixed costs of development _Fi_ ( _x_ ) that depends on tract characteristics. Normalizing the opportunity cost per unit of land to 0, this means that the fraction of land <u>1</u> developed in each tract is _Fi_ ( _αρiPiα_<sup>).The resulting aggregate housing supply function in tract</sup><sup>_i_is:</sup> 



<u>1</u> _−α_ This function reflects the intensive and extensive margin of supply. The first part, _ρiPi α_ , is the <u>1</u> intensity of development on each developed plot. The second part, _MiFi_ ( _αρiPiα_<sup>),isthetotalde-</sup> veloped land area in the tract. Differentiating, the implied housing supply elasticity is 



> 7 _ρi_ = _ι_ _<u>α−α</u>_ <u>1</u> (1 _− α_ ) <u>1</u> _−α_ _<u>α</u> κiα_ <u>1</u> _Mi_ where _ι_ is the cost of capital and _κi_ is tract housing productivity. 

16 

which quantifies the intensive and extensive margin responses respectively. With _α_ estimated to be about 0.33 in the literature (Combes et al., 2019), this expression reflects a baseline supply elasticity of about 2 holding the amount of developed land fixed and an additional component reflecting the extensive margin associated with developing additional land or land redevelopment. For tracts in which the fixed cost of developing marginal land parcels is higher (the CDF _Fi_ ( _x_ ) rises more slowly with _x_ ), the extensive margin component of the supply elasticity is smaller.<sup>8</sup> 

Now that we have laid out the basis for intensive and extensive margin responses, we adjust the model to incorporate all of the margins of response we observe in the data. First, we explicitly break the extensive margin component into redevelopment (plus teardowns) and development of undeveloped land. Second, we capture the fact that floor-area ratio (FAR) restrictions may constrain the quantity of housing services developed per parcel to be below the preferred amount <u>1</u> _−α_ of _ρiPi α_ . Finally, we consider depreciation and multi-unit buildings. 

To capture the idea that redevelopment may be costlier than development of new land, we decompose _Fi_ ( _x_ ) into a component for redevelopment and a component for undeveloped land: _<u>i i</u> Fi_ ( _x_ ) =<sup>_M_</sup> _M_<sup>_R_</sup> _i_<sup>_F_</sup> _i_<sup>_R_(</sup><sup>_x_) +</sup><sup>_M_</sup> _M_<sup>_U_</sup> _i_<sup>_F_</sup> _i_<sup>_U_(</sup><sup>_x_), in which we think of</sup><sup>_F_</sup> _i_<sup>_R_(</sup><sup>_x_) as first-order stochastically dominating</sup> _Fi_<sup>_U_(</sup><sup>_x_).Since in any initial period, all housing units are on developed land by definition, using the</sup> <u>1 1</u> notation in (1) we have<sup>_dH_</sup> _<u>i</u>_<sup>_R_,</sup><sup>_s_</sup> _H_ + _idHi_<sup>_T_,</sup><sup>_s_</sup> = _F_<sup>_<u>f R</u>_</sup> _<u>ii</u>_<sup>_R_</sup><sup><u>((</u></sup><sup>_ααρρiiPP_</sup> _<u>iiαα</u>_ <u>1</u><sup><u>))</u></sup> _ρiPiα_ <u>1</u><sup>and</sup><sup>_dH_</sup> _Hi_<sup>_U_</sup> _i_<sup>,</sup><sup>_s_</sup> = _F_<sup>_<u>f U</u>_</sup> _<u>ii</u>_<sup>_U_</sup><sup><u>((</u></sup><sup>_ααρρiiPP_</sup> _<u>iiαα</u>_ <u>1</u><sup><u>))</u></sup> _ρiPiα_ <u>1</u><sup>.That is, because of</sup> variation in the cost of redevelopment, the supply of redeveloped units (net of teardowns) may exhibit a different price response to that of new developments on previously undeveloped land. 

Extending (4) with the identity (1), we have the following unified decomposition that forms the basis for our reduced form empirical work. 



_<u>i</u>_ / _Hi_ _<u>i</u>_ / _Hi_ The redevelopment elasticity<sup>_dH_</sup> _d_ ln<sup>_R_,</sup><sup>_s_</sup> _Pi_ may be smaller than the other new units elasticity<sup>_dH_</sup> _d_ ln<sup>_U_,</sup><sup>_s_</sup> _Pi_ because of additional teardown and land remediation costs. We assume that variation in depreciation of existing units across tracts in a metro area is unrelated to changes in prices. 

We model the tract-level FAR constraint _Di_ as<sup>_Si_</sup> _M_<sup><u>(</u></sup><sup>_P_</sup> _i_<sup>_<u>i</u>_</sup><sup><u>)</u></sup> _≤ Di_ . This constraint potentially impacts 

> 8If _Fi_ ( _x_ ) is distributed Frechet with tract-specific dispersion parameter _Ti_ , _Ffii_ <u>((</u> _ααρρiiPPii_<sup>1/1/</sup><sup>_αα_</sup> <u>))</u><sup>=</sup><sup>_Ti_(</sup><sup>_αρiP_</sup> _iα_ <u>1</u><sup>)</sup><sup>_−_1</sup><sup>_−Ti_andthe</sup> _Ti_ extensive margin component of the supply elasticity is _Tiα_<sup>_−_1</sup><sup>_−Ti_</sup> _ρi_<sup>_−Ti_</sup> _Pi_<sup>_−_</sup> _α_ . Here we see explicitly how the extensive margin of supply may depend on tract topography and developed fraction if _Ti_ depends on these objects. 

17 

both the extensive and intensive margins of development. On the extensive margin, a binding constraint inhibits some new construction response to a price increase. In addition, a binding FAR causes the intensive margin response to be 0.<sup>9</sup> 

We recognize that this simple model best describes the construction of single family homes, or one housing unit per land parcel. This type of construction makes up over 90 percent of new construction units in our sample area in 2000-2010. However, in some high price areas the intensive margin component _d_ ln _Si_ reflects both space per unit and the number of units in multifamily dwellings. We ignore depreciation because we think it is unlikely to differ by price changes. 

### **3.2 Housing Demand** 

We incorporate housing supply conditions that are allowed to differ across locations within cities into a version of the quantitative urban model developed by Ahlfeldt, Redding, Sturm, and Wolf (2015) and extended by Tsivanidis (2018). While tracing out housing supply functions is ultimately about estimating reduced form impacts of housing demand shocks on housing quantities and prices, this part of the theory is helpful in operationalizing this goal in three ways. 

First, the model shows how to leverage variation across space within cities in local labor demand shocks to isolate exogenous variation in housing demand shocks across census tracts. The model structure facilitates recovery of causal linkages from labor demand shocks to housing demand shocks, as filtered through the commuting time matrix. We show how housing demand conditions in each census tract _i_ can be summarized through “Resident Market Access” _RMAi_ , which is the sum of commute time discounted skill prices available to residents of tract _i_ . This object can be readily calculated with available data on the numbers of workers and residents in each tract. Shocks to skill prices in commuting destinations are reflected as shocks to _RMAi_ . 

Second, the model provides a way to convert the quantity of housing services, which we observe only noisily, to residential population, which we observe accurately. The cost of relying on the model to make this conversion for us is that it depends on assumptions about preferences over housing and requires joint estimation of model parameters that govern labor and population supply conditions to residential and work locations respectively. For these reasons, we show results 



18 

both from the housing market portion of the model, for which we measure housing quantities directly, and from more complete estimation. Both of these sets of results will use the same sources of identifying variation. However, even the more isolated housing market estimation results rely on using the structure of the model to partial out the equilibrium impacts of labor demand shocks on local prices. Because these shocks impact housing demand conditions in multiple locations simultaneously, the model is essential for delivering a scaling of relative housing demand shifts across tracts that result from these shocks. This motivation is line with Monte, Redding, and Rossi-Hansberg (2018)’s observation that two identical productivity shocks hitting different cities may impart different treatment effects on city level outcomes because of differences in inter-city commuting and trade linkages. 

Third, the model makes clear the conditions required for census tract level “Bartik” shocks to represent a valid source of econometric identification. These shocks are calculated by predicting 2000 to 2006 tract level growth in employment by industry using 1990 tract level employment shares by industry with national industry specific employment growth outside of the metro area in question. Originally proposed by Bartik (1989, 1991), this source of variation has been used at the metro area level in Saiz (2010), Notowidgdo (2013) and Diamond (2015) among many others. This and Baum-Snow et al. (2019) are among the first papers to use this source of variation for identification at the sub-metro level of geography. To help us do this in a sensible way, we explicitly introduce industries _k_ into the model. 

Finally, the model provides structure that can be used to aggregate neighborhood housing supply functions to the metro area given an array of shocks to neighborhood fundamentals and to perform welfare analysis of place based policies. 

#### **3.2.1 Setup** 

While our main empirical work uses data for 275 metropolitan areas, our empirical focus is on within-metro area variation in housing supply elasticities. As such, our model is of a single metro area specified with an eye toward exploiting within metro area variation in labor demand shocks. 

The model features a continuum of identical workers indexed by _ω_ who choose residential tract _i_ , work tract _j_ and industry of work _k_ within the metro area. They receive productivity shocks _zijkω_ over commute origin-destination and industry triplets and preference shocks _viω_ over 

19 

residential locations. We think of them as first choosing their residential location, anticipating the distribution of productivity shocks from which they draw, with these shocks only revealed after committing to a residential location. In practice, the shocks primarily serve to smooth things over such that the model can generate data in which people with different utility realizations can have the same expected utility. 

The indirect utility person _ω_ receives from living in tract _i_ and commuting to _j_ and working in industry _k_ is: 



where _Bi_ is a local amenity, _wjk_ is the price of a unit of skill in commuting destination _j_ and industry _k_ , _Pi_ is the price of one unit of housing services in _i_ and _e_<sup>_κτij_</sup> is the fraction of time spent commuting for those living in _i_ and working in _j_ . In the data, we observe the price _Pi_ in year 2000 and beyond and the commuting time _τij_ in 1990 and 2000. The productivity shock _zijω_ is drawn from the Frechet distribution with shape parameter _ε_ . 



Following Tsivanidis (2018) and Couture et al. (2019), we also introduce the nested preference shock over residential locations _viω_ . This shock is also distributed Frechet but with shape parameters _η_ and _φ_ . This nested structure allows individuals to have different elasticities of substitution in demand between neighborhoods within versus between municipalities, where municipalities are indexed by _m_ and _i_ ( _m_ ) refers to neighborhood _i_ in municipality _m_ . 



Incorporation of this second shock allows the model to generate situations in which people would choose to reside in tracts with lower expected utilities as calculated based on _BPii_<sup>1</sup> _z_<sup>_−_</sup> _ij_<sup>_β_</sup> _kωe_<sup>_κτ_</sup> _w_<sup>_ij_</sup> _<u>jk</u>_<sup>only.As a</sup> practical matter, it also delivers a convenient expression for mean income net of commuting cost in each tract, as is derived below. If the distribution functions for the two shocks are identical and _η_ = _φ_ = _ε_ , the utility shock becomes redundant and this model reduces to one more similar to that in Ahlfeldt et al. (2015). 

20 

#### **3.2.2 Resident Market Access** 

The Appendix walks through the model in more detail to show that _RMAi ≡_ ∑ _k_ ∑ _j_ � _wjke_<sup>_−κτij_�</sup><sup>_ε_</sup> is a convenient summary measure of the access to employment opportunities from residential neighborhood _i_ . In particular, many objects in the model are constant elasticity in _RMAi_ and it can be readily calculated with available data. 

Before the productivity shock is revealed, the expected income (wage net of commuting cost) _<u>yi</u>_ associated with residing in tract _i_ is 



As a result, population supply to tract _i_ is given by 



This expression reflects the attractiveness of neighborhood _i_ ’s amenities and labor market opportunities, as balanced against its housing cost. This attractiveness is relative to the attractiveness to other neighborhoods in the municipality _m_ ( _i_ ), captured by the object inside the summation, and the overall attractiveness of all neighborhoods in the metro region 1/ _λ_ . 

Equilibrium commute flows, calculated as _πij_ = _πij|iπi_ , follow a standard gravity equation in commute time _τ_ . _ij_ 



That is, a regression of log commute probabilities between each origin-destination pair on origin and destination fixed effects plus commute time _τij_ recovers an estimate of the parameter bundle _κε_ . 

Labor supply to tract _j_ is given by 



where “Firm Market Access” _FMAj_ is a measure of the access to workers enjoyed by firms in tract _j_ . Plugging into the definition of _RMAi_ , we have the following system of equations. 



21 



Using data on employment _Lj_ , residents _πi_ , the parameter cluster _κε_ and commute times _τij_ , we can calculate _FMAj_ and _RMAi_ by solving this system. 

_RMAi_ can be readily calculated (jointly with _FMAi_ ) using our tract level data on employment, population, commuting flows and commuting time. We observe spatial distributions of employment and population in 1990, 2000, 2006 and 2010 and commute flows and times in 1990 and 2000. We estimate _εκ_ � using separate flow-weighted commuting gravity regressions like (11) with origin and destination fixed effects in 2000 for each metropolitan region.<sup>10</sup> Because we do not observe tract-tract commute times after 2000, we hold commute times constant at 2000 times for the later years. This yields direct measures of _RMAi_ as in (14) for 2000, 2006 and 2010. 

_<u>yi</u>_ An individual who lives in _i_ and works in _j_ in industry _k_ has housing demand of (1 _− β_ ) _Pi_ from Cobb-Douglas preferences. We assume that all sites in each residential location _i_ are perfect demand substitutes, justifying the uniform price per unit of housing services _Pi_ . Adding up, the log aggregate housing demand in tract _i_ is thus 



This object is expressed in terms of units of housing services. It is increasing in RMA conditional on population _πi_ because greater _RMAi_ is associated with greater income for tract residents. Conditional on _Pi_ , equilibrium tract residential population _πi_ is also increasing in _RMAi_ , as seen in (10). Thus, shocks to _RMAi_ result in housing demand shocks. This is the key insight used for identification in the empirical work. 

The reduced form empirical work uses the housing supply equation (2) in tandem with the housing demand equation formed by substituting (10) into (15). Credible identifying variation in ln _Pi_ must come from a component of _RMAi_ that is cleansed of variation in housing productivities and lot sizes. Section 3.4 lays out how we isolate such variation using a simulated version of _RMAi_ based on Bartik type labor demand shocks in commuting destinations for residents of tract _i_ . 

> 10Across the 306 regions in our sample, the median estimated elasticity of commuting flow with respect to one-way commuting minutes in 2000 is -0.04, the minimum is -0.11 and the maximum is -0.01. In addition, estimates of _εκ_ are about twice as large in big cities like New York and Los Angeles than in small cities like Bryan-College Station, TX. This reflects the fact that households in bigger cities are willing to travel longer to reach work destinations. 

22 

### **3.3 Equilibrium** 

We write down equilibrium conditions primarily with an eye toward showing how to use local housing demand shocks to identify of tract-specific housing supply elasticities _γi_ . Quantitative analysis and aggregation at the end of the paper also makes use of the neighborhood demand system defined by the model. The following equilibrium conditions are useful in this regard as well. 

Combining conditions governing population supply to residential tracts (10), labor supply to work tracts (12) and imposing housing market clearing yields conditions describing equilibrium tract population and house prices. Differentiating the population condition over time yields the following structural equation. 



This equation incorporates an intuitive positive relationship between growth in employment opportunities and tract population. This relationship is stronger if housing supply in tract _i_ is more elastic and/or if there is less dispersion in idiosyncratic preferenes over locations ( _η_ is larger). In this equation, _v_<sup>_π_</sup> _m_<sup>isamunicipalityfixedeffectthatcapturescommonpopulationtrendsinall</sup> tracts in municipality _m_ that come through their correlation in neighborhood choices delivered by the outer nest in preferences over neighborhoods. The error term _ui_<sup>_π_isafunctionofshocks</sup> to amenities and housing productivity in tract _i_ . Mathematical details are in the appendix. We use (16) below as a basis for structural estimation of _η_ , recognizing that identifying variation in _d_ ln _RMAi_ must be uncorrelated with tract level shocks to amenities and housing productivity for 

Substituting for (16) in housing demand (15), setting it equal to housing supply (2), solving for price and differentiating yields the growth rate in tract house price, expressed as follows. 



This equation shows, as is intuitive, that positive shocks to employment opportunities get capitalized into home prices. The amount of capitalization is of course decreasing in the housing supply elasticity _γi_ and in the dispersion of amenity draws within municipality _m_ , an object which is negatively related to _η_ . Changes in housing productivity, average lot size and the local amenity _Bi_ 

23 

show up in the error term _ui_<sup>_P_.Because</sup><sup>_RMAi_itself depends on quantities and prices throughout</sup> the region, it is also a function of these objects. So, to restate, our empirical objective must be to pick out variation in _d_ ln _RMAi_ that are uncorrelated with local innovations to housing productivity (costs) and lot sizes. 

Finally, the model delivers the following implicit equation which describes the relationship between change in _d_ ln _RMAi_ and municipality level aggregates of tract population growth _d_ ln _πi_ . 



In this equation, _si_ is the base year share of municipality _m_ ’s population living in tract _i_ . As _φ_ rises, dispersion in preferences across municipalities falls. As a result, positive shocks to _RMA_ in any neighborhoods within _m_ result in more rapid population growth in this municipality. (18) is the estimation equation we use below to recover estimates of the preference parameter _φ_ . 

## **4 Empirical Implementation** 

Our main estimation equation amounts to the differenced counterpart to the simple tract level supply equation (2). 



Observations are for tract _i_ in metro region _r_ . To allow for observed heterogeneity in supply elasticities, we parameterize _γir_ to depend on metro region and tract-specific observables _Zr_<sup>1and</sup> _Z_<sup>2</sup> _ir_<sup>.</sup> 



As is detailed in Section 2, these sources of heterogeneity are topography, land use regulation and regulatory burden. 

The first two terms in (19) are included for identification reasons. Fundamental to our empirical strategy is inclusion of metro region fixed effects _θr_ . Their inclusion ensures that we compare different neighborhoods in the same labor market for identification. Robustness checks include these fixed effects interacted with 2-2.5 km CBD distance rings. In tract characteristics _Xir_ , our main specification includes lagged demographic attributes, a quadratic in CBD distance and controls for tract-specific labor demand conditions that we worry may spill over into housing supply 

24 

factors. Our controls for 1990 and 2000 tract demographic characteristics account for potential influencers of the tract regulatory environment that may be correlated with the instruments we lay out below. The CBD distance controls holds constant any potential spatial trends in price growth that are related to costs and are useful given the stronger 2000-2010 labor demand growth in suburban areas. 1990 and 2000 Census rent and price indexes help to account for decadal mean reversion in home price growth. Finally, 1990 employment and a tract-specific Bartik labor demand shock for the 2000-2006 (explained below) ensures that our IV implementation is only using variation from outside of tract _ir_ 

### **4.1 OLS Results** 

Table 2 presents basic OLS relationships between our various measures of post-2000 home quantity changes and contemporaneous price growth. Given that the 2007-2010 period saw mostly declining housing demand and therefore may not be not a good setting for estimating housing supply, we include a specification that focuses on the 2000-2006 period. In the first row, we see negative relationships between Census Hedonic price growth and quantity growth. Remaining rows, which are for our two Zillow price indexes, show small positive coefficients of up to 0.02 for quantity measures in housing units and only up to 0.12 for our quality-adjusted quantity measure. Such small (or negative) housing supply elasticities seem implausible and help to motivate our search for more convincing identifying variation in prices.<sup>11</sup> 

The implausibly low relationships between the housing price growth and quantity growth point to two identification challenges in estimating housing supply. First, neighborhoods that experience stronger demand shocks may follow with unobserved changes in housing regulation in part in order to cope with these demand shocks - a classical endogeneity problem discussed extensively in Davidoff (2016). To the extent that this phenomenon happens dynamically, it could generate the negative observed relationship between price and quantity growth. If endogenous positive supply shifts after 2000 loosen housing development restrictions in response to demand shocks from the 1990s, observed OLS relationships will trace out demand curves and be negative. Such a story would justify the negative serial correlation in decadal price growth seen in the 

11Ouazad and Ranciere (2019) find similarly small OLS relationships between price growth and quantity growth for the San Francisco metro region. 

25 

data at the tract level. One might also be concerned that positive productivity shocks outside of the construction sector boost both local housing demand through higher household earnings and construction costs at the same time. The result is inward shifts in housing supply that are correlated with outward shifts in housing demand. Moreover, our price index measure, while constructed as carefully as possible, is sure to be a noisy measure of the true price of housing services. Mechanical mean reversion in decadal house price growth that could reflect such measurement error would lead to a classic attenuation bias problem. 

The broad message is the possibility for a local unobserved history to drive both relative price declines and more construction, inducing a downward bias in OLS. Thus a valid identification strategy needs deal with the classical endogeneity concern of simultaneity in demand and supply by finding variation in local housing demand shocks across neighborhoods that are similar exante. To resolve this issue, we must isolate a source of tract-specific housing demand shocks which are uncorrelated with supply factors. This is the role of our instrument, which we develop next. 

### **4.2 Instrument Construction** 

We need a source of identifying variation in home price growth that driven by tract level housing demand shocks and is unrelated to shocks to local construction costs or housing productivity. To see where this can come from, consider the following tract level inverse housing demand equation from the model. 

ln _Pi_ = _ρ_ ˜ _HD_ + 1 _<u>φ</u>_ +/ _ηη−−ηβ_ 1<sup>ln ∑</sup><sup>_i_´</sup><sup>_∈m_(</sup><sup>_i_)</sup> _Bi′ Pi_<sup>_β′−_1</sup> _RMAi_ <u>1</u> _ε_<sup>_′_</sup> _η_ + 1+ _η_ <u>1</u> _−ηβ_ 1+ _ε_ _<u>η</u>_ ln( _RMAi_ ) � � _−_ 1+ _η_ <u>1</u> _−ηβ_<sup>ln</sup><sup>_H_</sup> _i_<sup>_d_,</sup><sup>_e f_</sup> + 1+ _ηη−ηβ_<sup>ln</sup><sup>_Bi_Thefactthatthehousingpriceintract</sup><sup>_i_isincreasingin</sup><sup>_RMAi_</sup> through impacts on housing demand is intuitive. Labor demand conditions relevant to neighborhood _i_ , as summarized in _RMAi_ , represent a key source of variation in house prices. However, any component of _RMAi_ that is correlated with tract housing productivity is endogenous to housing supply. Indeed, through its codetermination with _FMAi_ , _RMAi_ depends structurally on tract population which itself depends on tract housing productivity. As such, we develop instruments that pick out components of _d_ ln _RMAi_ that are likely orthogonal to shocks to productivity or other 

To build instruments, we start with (13) and (14) as a basis for calculating a simulated ver- 

26 

sion of _d_ ln _RMAi_ that plausbily excludes shocks to tract housing productivity and its correlates, � denoted ∆ ln _RMAi_ . This simulated instrument serves a dual purpose. First it is a reduced form housing demand shock that drives exogenous variation in tract level house price growth, as represented above. Second, it is a predictor of the structural object _d_ ln _RMAi_ that is unrelated to tract level shocks to local amenities or housing productivities. The latter use will allow us to recover estimates of structural parameters. 

Instead of using actual employment in all commuting destinations in these calculations, we use the employment predicted by national growth rates and initial industry composition in each � tract to solve for _RMAi_ , after evenly scaling up the residential population of each tract to maintain � labor market clearing and allowing us to solve jointly for _FMAj_ . For components of instruments, we impose 1990 commute times and initial employment shares by industry and use estimates of _εκ_ for 2000. We exclude all tracts within 2 km of origins in order to reduce the likelihood that nearby industry composition could be related to trends in tract productivity. For example, tracts near a concentration of construction employment may be subject to secular changes in shocks to construction productivity that would show up as part of the instrument. 

In particular, we calculate the year 2000 component _RMA_<sup>�</sup> 2000 _i_ of our main instrument is calculated as: 



In these expressions, _τij_<sup>90is the reported or forecast commute time from</sup><sup>_i_to</sup><sup>_j_in the 1990 CTPP.</sup><sup>_εκ_�</sup> is estimated separately for each region in year 2000 using gravity regressions of log reported commute flows on commute times and origin plus destination fixed effects using 2000 CTPP data.<sup>12</sup> Distances from residential to work locations _disij_ are calculated using tract centroids. Employment in industry _k_ in work location _j_ , _L_<sup>90</sup> _jk_<sup>, is measured from the 1990 CTPP.</sup><sup>_E_</sup> _r_<sup>2000</sup><sup>_′_</sup> ( _j_ ) _k_<sup>and</sup><sup>_E_</sup> _r_<sup>2000</sup><sup>_′_</sup> ( _j_ ) _k_<sup>are the 2000</sup> and 1990 nationwide employment in industry _k_ excluding the region of tract _j_ , respectively. That 12Details of these estimates are reported in (Baum-Snow et al., 2019). 

27 



1990 employment by industry grows at national rates to year 2000. ∑ _<u>j</u>_ ∑ _k L_<sup>90</sup> _jk_<sup>[</sup> ∑<sup>_E_</sup> _r_<sup>2000</sup><sup>_′_</sup> _L_ (<sup>90</sup> _jj_ ) _k_<sup>/</sup><sup>_E_</sup> _r_<sup>1990</sup><sup>_′_</sup> ( _j_ ) _k_<sup>]</sup> is a constant _j_ that captures the population growth rate needed to match the aggregate simulated employment in the region in year 2000. The 2006 component of the instrument is calculated analogously, with _Er_<sup>2000</sup><sup>_′_</sup> ( _j_ ) _k_<sup>in (21) and (22) replaced by</sup><sup>_E_</sup> _r_<sup>2006</sup><sup>_′_</sup> ( _j_ ) _k_<sup>.</sup> 

The log difference in _RMA_ � _i_ for 2000-2006, ∆ ln _RMA_<sup>�</sup> _i_ , is our main instrument for ∆ ln _Pi_ as measured for both the 2000-2006 and 2000-2010 time periods. We build our instrument for the 2000-2006 period only as this is the time period for which first stage predictive power is strongest, as we show below. 

### **4.3 Instrument Validity** 

The fundamental source of identifying variation used is the standard tract level “Bartik” (1991) type shocks in each employment location, written out as follows. 



� A prerequisite for the spatial aggregation of such shocks into ∆ ln _RMAi_ to successfully predict ∆ ln _RMAi_ is for the tract level counterparts to successfully predict tract level employment growth. We choose this time interval rather than 2000-2010 because of the stronger available identification during this boom period. The 2006-2010 period was associated with employment declines that are not well predicted by Bartik instruments. 

Table 3 presents evidence that our underlying identifying variation can successfully predict tract level employment growth. It presents regressions of 2000-2006 or 2000-2010 tract employment growth in tract _jr_ on _Bartikjr_ and controls for 1990 employment level, past demographic composition of tract residence, CBD distance and metro region fixed effects. This is a sort of tract level first stage regression which gets aggregated in the first stage of our main analysis. We control for past employment to isolate employment growth due only to variation in industry composition. Past demographic and CBD distance controls account for potentially differing labor supply conditions. Results indicate that we can plausbily isolate labor demand shocks at the tract level. A one-percentage point increase in the Bartik shock predicts a 0.2% increase in 2000-2006 tract em- 

28 

ployment and a 0.6% increase in 2000-2010 tract employment. Inclusion of 2-2.5 km CBD distance ring fixed effects interacted with metro region does not affect these conclusions.<sup>13</sup> 

One challenge we face when estimating the housing supply equation is that house price growth is negatively serially correlated across decades. The first two columns of Table 4 show this pattern. Also note the positive serial correlation in quantity growth, which likely reflects serially correlated positive demand shocks. Finally, note that quantity growth begets subsequent price declines. Commensurate with our discussion of the OLS results above, these patterns suggest that there could be local unobserved history that drives both relative price declines and more construction, inducing a downward bias in an OLS estimation of housing supply. One legitimate � potential concern is that our instrument ∆ ln _RMAi_ may be correlated with such unobserved history. We hope that results in the final two columns of Table 4 allay such concerns. They show that 1990-2000 price and quantity growth cannot predict subsequent growth in simulated RMA (our instrument). This suggests that IV estimates are unlikely to suffer from the sort of selection bias that we discuss above. Moreover, results in Table A1 show that our instrument does not predict 1990-2000 housing price growth for four sets of control variables and it does not predict 1990-2000 quantity growth for our primary specification. 

The top left panel in Table 5 presents the relationship between ∆ ln _RMA_<sup>�</sup> and ∆ ln _RMA_ for 2000-2006. It shows significant estimated elasticities of 0.5-0.7 that are robust to the specification used. This is a necessary prerequisite for ∆ ln _RMA_<sup>�</sup> to predict ∆ ln _P_ in (19) as an instrument. The next three blocks show first stage relationships between ∆ ln _RMA_<sup>�</sup> and our three primary measures of ∆ ln _P_ . First stage coefficients are strong and robust to the different specifications used. With metro area fixed effects, first stage coefficients are not significantly affected by inclusion or exclusion of lagged demographic and housing market controls, corroborating evidence from Table 4 that they are uncorrelated with these variables. Smaller first stage coefficients for the 2000-2010 relative to the 2000-2006 period reflects the fact that the 2007-2010 period mostly saw housing market declines. 

The bottom two blocks in Table 5 show strongly positive reduced form relationships between our instrument and 2000-2006 and 2000-2010 Zillow new construction. We note that while these reduced form quantity responses are slightly larger over this longer time period, the two are not 

13Results are also robust to lagging the demographic tract controls by one additional decade. 

29 

significantly different. We retain the longer 2000-2010 time horizon for two reasons. First, we have higher quality information about some housing quantity measures for 2010 than for 2006. Second, as discussed further below, the intensive margin responses do change from 2006-2010 and we find it important to incorporate these into the analysis. Ratios of reduced form to first stage coefficients from Table 5 preview the full IV results presented in the following section. 

Overall, we find that changes in simulated resident market access (∆ ln _RMA_<sup>�</sup> ) strongly predict nearby employment growth, home prices, and thereby housing demand growth. Moreover, they are not correlated with pre-trends in house prices conditional on appropriate controls. These findings provide reassuring support for the use of ∆ ln _RMA_<sup>�</sup> as a valid instrument in estimating housing supply elasticities. 

## **5 Main Results** 

In this section, we present our main reduced form housing supply estimates, estimating (19) by IV, and explore their heterogeneity as a function of CBD distance, initial year development intensity, topography, and regulation. 

### **5.1 Unified Supply Elasticity Estimates** 

To start, Table 6 presents unified regressions of housing quantity growth on house price growth, with ∆ ln _RMA_<sup>�</sup> as an instrument for ∆ ln _P_ using the same specification as the OLS regressions reported in Table 2. To ensure the robustness of the results, we use three measures of house price growth: hedonic price growth based on the Census data; hedonic price growth based on the Zillow data; and repeat sales price growth based on the Zillow data. And we show results using just region fixed effects in Panel A and with region-ring fixed effects in Panel B. As discussed further in Section 2.3, we also explore seven measures of house quantity changes: 2000-2006 or 20002010 new construction based on the Zillow data; 2000-2009 new construction based on the ACS; the 2000-2010 change in housing units based on census data; the 2001-2011 increase in floorspace and quality-adjusted housing units based on Zillow data; 2000-2010 increase in housing units through redevelopment only based on Zillow and satellite data. The top panel controls for the metropolitan area fixed effects, while the bottom panel further controls for the CBD distance rings 

30 

within metropolitan area fixed effects. The combination of different price and quantity measures, along with different fixed effects, yields 40 supply elasticity estimates in total. Equation (5) shows how to decompose the quality-adjusted elasticity into components. 

Before discussing the estimates, we highlight a few observations. First, unlike small and insignificant estimates from the OLS regressions, the estimated coefficients in Table 6 are positive across all specifications with magnitudes that are in line with other supply elasticity estimates from the literature. This is consistent with our narrative that OLS relationships between quantities and prices in part reflect movement along demand rather than supply curves. Second, estimated quantity responses to each measure of price changes are not significantly different, though quality adjusted measures in Columns 5 and 6 have large standard errors. Third, controlling for CBD distance ring fixed effects interacted with metro area (Panel B) yields similar though somewhat larger estimates than using metro area fixed effects only. We note that the source of identifying variation changes when including region-ring fixed effects. In particular, more variation is available within suburban rings where housing supply elasticities are larger – a result we show explicitly below. The fact that Table 6 reports local average treatment effects means that these estimates are not necessarily indicative of average supply elasticities across urban tracts nationwide. Indeed, we show below that average supply elasticities are somewhat larger. 

Comparisons of results in Columns 1 and 2 show the utility of allowing for longer adjustment periods. Over the longer time period, our estimated elasticity of new unit supply with respect to price more than doubles from 0.2 to 0.5. As seen in Table 5, this is primarily because of the more attenuated longer run price response, which reflects the 2007-2009 housing bust. Across the Zillow and ACS measures of unit construction, housing supply elasticity estimates are very stable (columns 2 and 3). The estimated elasticity for the census change (column 4) is not significantly different from the other two, even though this measure incorporates the negative impacts of teardowns and full depreciation. This indicates that price shocks have little impact on these two negative margins of response. 

In columns 5 and 6, we report quality-adjusted housing supply elasticities for the 2000-2010 period. These estimated elasticities are much larger than the unit supply elasticities shown in columns 2-4, at 2.6-3.8. Based on these estimates, we conclude that housing quality is an important margin of response to price changes. This can come through construction of higher quality 

31 

(larger) new units or the renovation of existing units. Indeed, it is clear that treating housing units as homogenous misses an important segment of supply and that our supply model reasonably approximates the intensive margin of supply.<sup>14</sup> The implication is that renovations and repairs are quite elastic with respect to price, contrary to DiPasquale (1999). Comparing the estimated _γ_ s in column 5 with those in column 4, we find that renovation and upsizing account for over 80% of the total supply increase. While these estimates may seem surprisingly large, they are consistent with the observations that almost half of American homeowners renovated their homes Plaut and Plaut (2010) and that total renovation expenses reached $326 billion in 2007 Choi et al. (2014). 

Column 7 reports estimated elasticities for the number of new units constructed 2000-2010 on land that was already developed in 2001. Comparing with results in columns 2 and 3, we find that at least one-third of newly built homes are through redevelopment of already-developed land, consistent with the findings in the urban literature that neighborhood renewal is largely driven by the deterioration and subsequent redevelopment of the existing housing stock (e.g. Rosenthal (2018); Brueckner and Rosenthal (2009)). The smaller estimated redevelopment elasticity supports the conjecture that redevelopment is costlier than development of new land. 

### **5.2 Tract Level Heterogeneity** 

#### **5.2.1 Unit Supply** 

The local average treatment effect tract-level supply estimates in Table 6 mask substantial variation across neighborhoods. This section presents how tract-level housing supply elasticities vary as a function of distance to CBD, land availability, topographical features, and land use regulations. 

Table 7 repeats the IV regressions in column 2 of Table 6 Panel A with the addition of a set of interactions between price growth and tract-level factors that may influence supply. Price growth is constructed using the repeat sales index for columns 1-6 and the hedonic index for columns 7-12. All specifications include CBD distance, CBD distance squared, an indicator for being over 

> 14Empirical work on the housing production function dates back to Muth (1964). The estimated land share in the recent literature ranges from 0.10 for Centre County, PA (Yoshida, 2016), to 0.14 for Alleghany County, PA (Epple, Gordon and Sieg, 2010, to 0.35 for France (Combes _et al._ , 2016), to 1/3 for the U.S. average housing market (ranging from 0.11 to 0.48 in low to high-value areas, as reported in Albouy and Ehrlich, 2012). Ahlfeldt and McMillen (2014) provide convincing empirical support for the Cobb-Douglas functional form as a reasonable approximation to the housing production function. 

32 

two-thirds of the way from the CBD to the region edge and these variables’ interactions with price growth. CBD distance is measured as the fraction of the way from the CBD to the furthest census tract in the region from the CBD, running from 0 to 0.66 only. We use this functional form as it fits the data better than extending CBD distance out beyond 0.66. Our identifying variation is weakest in CBD distance band 0.66-1, where census tracts are typically very large and there was not a lot of 1990 employment variation for identification and we found we could only reliably identify an average tract-level supply elasticity. Overall, results in Table 7 show that there is substantial within-region variation in local housing supply elasticities. In addition, results across the two measures of price growth are very consistent.<sup>15</sup> 

Results in column 1 show that estimated housing unit supply elasticities exhibit a monotonically increasing trend with the distance to the city edge at a marginally decreasing rate. At the CBD, on average, a one percent increase in house price increases the quantity of housing supplied by only 0.2%. This number increases to 1.0% at halfway to the city edge and 1.2% at 90% of the way to the city edge. These micro geography level estimates provide a supply-side explanation for the recent finding of more price growth in the center of metropolitan areas in the latest boom Glaeser et al. (2012); Yoshida (2016). They are also consistent with the observation that a given common increase in demand throughout an urban area leads to a relatively smaller price response and relative greater quantity response the further away from the center one gets Genesove and Han (2013). 

This CBD distance profile depends in part on the fact that land availability increases with CBD distance. Figure 1 shows that the average tract in our data is almost 60% developed at the CBD but only 25% developed at the region edge. However, the fraction of tract land that is flat also declines from 45% to 35% from CBDs to region edges. To see how much these factors matter, Table 7 column 2 expands the specification in column 1 by adding interactions between ∆ ln _P_ and the 2001 fraction of land developed in each tract, the fraction flat and their interaction. The resulting coefficient estimates are negative, positve and negative respectively with only slightly attenuated CBD distance coefficients. To get a sense of magnitudes, all else equal increasing developed fraction by 0.25 (one standard deviation) decreases the quantity of new housing units supplied by 0.2% per 

15HI results in Columns 7-12 have a slightly different specification in which CBD distance extends out to the edge of metros. As a lot of our investigation is about variation as a function of CBD distance, we focus on specifications that control for region but not region-ring fixed effects. 

33 

1% increase in price at the mean fraction flat of 0.4. However, increasing fraction flat by 0.42 (one standard deviation) does not increase the supply of new housing units at the mean developed fraction but increases unit supply by 0.2% per percent increase in price for undeveloped land. The negative interaction between these two factors indicates that flatness and lack of development are complements in lowering the cost of new construction. Additional inclusion of elevation range has no significant estimated impact on supply elasticity.<sup>16</sup> 

We find evidence that the CBD distance effect persists conditional on topography and developed fraction because regulations ease with CBD distance. With the idea that housing regulations mostly vary at the municipality level, we control for municipality fixed effects in Table 7 Column 3. Doing so results in attenuation of CBD distance effects by 66-77%. Second, we focus on the 1,512 tracts in 8 cities for which we have FAR information for residentially zoned parcels. Inclusion of the FAR restriction yields an expected positive interaction coefficient of 0.07. Increasing FAR by 2 (one standard deviation) thus increases the unit supply elasticity by 0.14.<sup>17</sup> CBD distance effects attenuate even more with this specification.<sup>18</sup> 

In column 5, we examine whether the estimates from the main specification in column 2 are robust to the inclusion of metro-level factors. In particular, we consider the fraction of developed land and the fraction of area that is lost to hills, water and wetland, both measured within the 50% of the maximum radius from the city center. With the tract-level factors controlled for, the metrolevel supply conditions are insignificant for repeat sales price growth and implausibly positive using hedonic adjusted price growth (column 11). However the effects of the tract-level factors are remarkably consistent and robust. 

In column 6, we focus on redevelopment. In particular, we repeat the main specification in column 2 but with redeveloped units as the dependent variable. These estimates are simply attenuated versions of those in column 2, with this attenuation differing with CBD distance. Conditional on developed fraction and topography, the redevelopment elasticity is about one-quarter of the full unit supply elasticity on average, and it declines with CBD distance. This is consistent 

> 16Exploration of additional interactions yielded low power and no significant coefficients. 

> 17We also tried interacting various 2006 Wharton Regulation sub-indices measured at the municipality level with price growth and found no significant effects, though impacts are negative as expected. Loss of about half the sample may explain the associated large standard errors. 

> 18We have not found plausible instruments for regulatory constraints, though controls for 1990 and 2000 tract level demographic characteristics may account for key determinants of the regulatory environment (Murphy (2018)). 

34 

with findings in the literature that prime teardowns are near public transportation and traditional village centers in Chicago Dye and McMillen (2007) and closer to the CBD and the coast in Miami Munneke and Womack (2015). Households attracted to redeveloped suburban housing can be quite different from central-city gentrifiers in that the former are likely to value high-quality public schools while the latter value new, larger housing relatively close to the CBD Charles (2013). In addition, land assembly for development may be easier with undeveloped parcels in more suburban areas. Together, the significant CBD distance effects, both in new construction and in redevelopment, emphasize the importance of examining housing supply through the lens of micro-geographic perspectives. 

Results using the hedonic index instead, reported in Table 7 Columns 7-12, are very similar to those for the repeat sales index. 

#### **5.2.2 Quality Adjusted Housing Supply** 

Table 8 focuses on quality-adjusted housing supply responses. Interestingly, CBD distance patterns are no longer evident, as the relevant coefficient estimates are insignificant. Intuitively, intensive margin improvements are mainly capital rather than land intensive, reducing dependence on land availability conditions and hence CBD distance. For this reason, we exclude CBD distance effects in our main specification for quality supply, only letting this supply response depend on initial land development and topographical features. As with the unit supply response, the quality adjusted supply is more responsive when when there is less developed land and when there is more flat land in a given tract. These effects represent the aggregation of their respective effects from unit supply. As noted above, quality-adjusted supply is 7-10 times more price elastic than is unit supply, though we have large standard errors on our estimates of this type of supply elasticity. Estimates are remarkably similar for floorspace and our housing quantity index. 

### **5.3 Metro Level Heterogeneity** 

In Table 9, we examine the role of metro-level supply conditions on local housing supply elasticities. Following Saiz (2010), we construct three measures of metro-level factors: the fraction of developed land within the 50 km radius from the city centre; the fraction of area that is lost to hills, water and wetland within the 50 km radius from the city centre; the metropolitan area 

35 

level WRLURI indices. To ensure the robustness of our results, we also reconstruct the first two variables within the 10 km, 20 km, 10%, 50% and 100% of the maximum radius from the CBD and for the entire metropolitan area. All results discussed below are consistent across these different measures. 

Column 1 repeats the baseline CBD distance specification in Table 7. In column 2, we add an interaction between ∆ ln _P_ and the fraction of developed land within the 50 km radius from the city centre. This coefficient is imprecisely estimated; moreover, the distance coefficients become more noisy. Depending on the size of a metropolitan area, 50 km might be far outside of the metropolitan boundary or only cover part of the area. In light of this, Column 3 reports estimates from a regression that includes an interaction between ∆ ln _P_ and the fraction of developed land within 50% of the maximum radius from the CBD. This coefficient is again insignificant, although including this variable does not significantly affect the CBD distance pattern in local supply elasticity. In columns 4 and 5, we run alternative regressions in which ∆ ln _P_ is interacted with the the fraction of area that is lost to hills, water and wetland within the 50 km radius from the city centre. In columns 6 and 7, we include both the metro-level initial development condition and metrolevel topographical conditions. Across these specifications, none of the metro-level factors appear statistically significant in explaining variations in local supply response. In column 8, we control for an interaction between ∆ ln _P_ and and the metro-level WRLURI. The coefficient is negative and marginally significant in the top panel, consistent with the expected effects of local regulation (Saiz, 2010). However, the usual endogeneity concern applies here. In column 9, we include all the metro-level supply conditions in addition to the CBD distance variables. None of the metro-level factors appear significant for local supply elasticity. 

While the previous housing supply literature has established the importance of the metrolevel topographical features and regulations on the metro-level housing supply, we cannot find evidence that they explain variation in neighborhood level supply elasticities across metros of different types. We caution that our empirical setting is not well suited for this sort of analysis, as our identification strategy explicitly compares tracts in the same metro region that receive different housing demand shocks. Interactions with metro level factors use between-metro variation in housing demand shocks for identification, which our empirical setup is not set up to deliver. As such, it is not surprising that standard errors in Table 9 are large and estimates are imprecise. 

36 

We do not conclude that metro level land availability conditions do not matter for housing supply in aggregate, as metros with more unavailable land have lower tract level supply elasticities which aggregate to more inelastic metro level housing supply. We demonstrate this carefully in the following section. The point remains, however, that when analyzing impacts of a local housing demand shock or a neighborhood-targeted policy, it is insufficient to use the metro-level supply elasticity. Instead, neighborhood level supply estimates are needed. 

### **5.4 The Distribution of Tract-Level Supply Elasticities** 

We use the specifications in Table 7 columns 2 or 8 and 6 or 12 to predict out tract-level total unit and unit redevelopment supply elasticities respectively for each tract. We use specifications in Table 8 columns 1, 3, 5 and 7 to predict out quality adjusted supply elasticities. While the estimation sample for Tables 7 and 8 are limited, we use coefficient estimates to predict supply elasticities for all census tracts in our data. 

Table 10 provides summary statistics of these imputed elasticities. Across all tracts, mean unit supply elasticities are about 0.8 of which one-quarter is from redevelopment. For qualityadjusted supply, analogous elasticities are 2.6-4.3 depending on the index used. These objects have standard deviations of 0.4-0.6 with the most supply elastic tracts having quality-adjusted elasticities of about 5.2. This dispersion is of similar magnitudes within metro areas. With the standard deviation of across region mean supply elasticities of only 0.1-0.3, more dispersion in supply elasticities exists within rather than between metro areas. Therefore, understanding such within region elasticity is really important. For the mean tract in our data, 77 percent of the total supply elasticity comes from the intensive margin with the remainder from new unit construction. We find no role for depreciation and teardowns. 

The three metropolitan areas with lowest average tract-level hedonic index based unit supply elasticities are Jersey City (0.9), Newark (1.0) and Los Angeles (1.0), respectively. On the other end, the three metropolitan areas with highest average tract-level supply elasticities are Dothan, AL, Gainesville, FL and Ocala, FL (1.7 each), respectively. For quality-adjusted supply, Newark (3.6), Jersey City (3.8) and San Diego (3.9) have the lowest average elasticities, with Los Angeles ranked sixth, while Jacksonville, NC, Florence and Ocala (5.3 each) have the highest. There is large variation in supply elasticities within metro areas. Within Los Angeles, the unit supply elasticity 

37 

ranges between 0.4 and 2.0 and quality-adjusted supply elasticities range from 3.0 to 5.7. The main cross-region source of variation in dispersion in supply elasticities comes from the bottom end of the distribution. In Ocala, unit supply elasticities range from 1.0 and 2.0 with the quality-adjusted counterpart ranging from 4.4 to 5.6. 

Our results indicate the remarkably consistent pattern that local supply elasticities increase with CBD distance, some of which is attributed to initial development density and topography. Figure 1 shows that the closer to city centers, there is a higher fraction of flat, plain and developed land, thereby contributing to the CBD distance gradient for supply elasticity. On average, the fraction of tract-level developed land ranges from 60% at the CBD to less than 10% at 90 percent of the way to the city edge. This pattern is consistent with the prediction from a monocentric model of urban land use that the density of construction declines as one moves away from the CBD (Duranton and Puga (2015)). Thus areas that are further away from the CBD effectively have more land in which to deliver housing, permitted both by initial development density and by topographical conditions. It is therefore tempting to conjecture that the CBD distance pattern in supply elasticities is mostly explained by the increasing availability of land as one moves away from the center. 

Figure 2 shows how much this is the case. The left panel presents smoothed predictions of four measures of unit supply and the right panel presents four measures of quality-adjusted supply based on repeat sales price growth. In the left panel, the flatter curves show the imputed _γ_ when holding the tract-level fraction of developed land and fraction of flat and plain land at each tract’s respective metropolitan area mean level. It is clear that even without spatial variation in initial density and topography, there is already a significant increasing CBD distance effect in local supply elasticities. This effect may be explained by local regulations which we do not control for in our main specification due to endogeneity concerns and associated required sample restrictions. Closer to city centers, building permits and zoning restrictions may be more stringent, making supply less elastic. Almost perfectly coinciding is imputed _γ_ when holding only the fraction of developed land at its metro-mean level, allowing for variation in topography across tracts. Local topographical features do not add much to spatial variation in supply elasticities within cities. The steeper curves plot the imputed _γ_ when fixing only the fraction of flat and plain land at its metro-mean level, allowing initial development density to vary across tracts. These curves are 

38 

much steeper and almost overlay the imputed overall _γ_ (marked by the blue curve). Thus, the monotonically declining development density with CBD distance, as shown in Figure 1, explains almost all of the additional relationship between supply elasticity and CBD distance that exists beyond that implied by the regression results in Table 6 Column 3. In the right panel of Figure 2, we see more of a role for both topography and development density in explaining the increasing profile of quality-adjusted supply elasticities with respect to CBD distance. 

We plot similar figures for select metropolitan areas (Log Angeles, New York, Madison and Pittsburgh) in Figure 3. Regardless whether a metropolitan area is considered elastic as a whole, its within-city variation in supply elasticities is always amplified by spatial variation in the fraction of developed land and, for quality-adjusted supply, topography. While there is a tendency for supply elasticity to increase with CBD distance, this effect gets mitigated in Pittsburgh and Los Angeles by the hilly topography at the edges of these metro regions. 

## **6 Aggregation** 

Much of the existing evidence on housing supply elasticities uses metro areas as the unit of analysis. In order to connect our estimates to these metro level estimates, in this section we aggregate the estimated tract-level housing supply elasticities to the metro area level. Aggregation brings up a number of conceptual and practical challenges. The typical approach, for example in Saiz (2010), has been to use metro level labor demand and/or population supply shocks to deliver housing demand shocks. However, as we show above in Section 3, positive labor demand shocks tend to be disproportionately oriented toward suburban areas where housing supply is relatively elastic. This means that metro level studies may find supply elasticities that weight the suburbs above their share of metro populations (though not necessarily land areas). Indeed, as neighborhoods are linked in the residential demand system, metro level demand shocks of the same size but aggregated from different combinations of changes in neighborhood fundamentals can imply different metro level housing supply elasticities. Because of this variance to setting, here we provide a few examples of the macro supply elasticities implied from some simple broad-based neighborhood-specific shocks. Context matters and neighborhood level supply elasticities must be aggregated as appropriate to the application at hand. 

To get a handle on aggregation, we first note that the tract level supply elasticity _γir_ generically 

39 

aggregates to a metro region level elasticity _γr_ as follows. Aggregating tract level supply growth to the metro level means taking a sum weighted by initial neighborhood shares of the housing stock: 



Comparison with its region level counterpart _d_ ln _Hr_ = _γrd_ ln _Pr_ , by definition the region level elasticity is given by 



Here, we see that the metro level elasticity depends on the mix of neighborhoods experiencing price growth that has been spurred by demand shocks. As neighborhoods are linked in spatial equilibrium, it is difficult to think how price changes in any two neighborhoods may occur in mutual isolation. 

If demand shocks were to generate the same price growth rate in every neighborhood, the macro level elasticity would simply be the average of micro elasticities weighted by shares. However, exactly because of differing supply elasticities across locations, the same demand shock in each location would typically generate different price changes and aggregation is thus not straightforward. The following sub-section provides some examples. 

### **6.1 Aggregation of Common Neighborhood Demand Shocks** 

In this sub-section we consider the case in which all neighborhoods simultaneously experience housing demand shocks. Because of differing housing supply elasticities, these shocks manifest themselves as different combinations of housing price and quantity changes, depending on the neighborhood. With Cobb-Douglas preferences, we have that tract level expenditure share on housing is<sup>_H_</sup> _Y_<sup>_<u>ir</u>_</sup> _ir_<sup>_Pir_</sup> = 1 _− β_ , where _Yir ≡_ _<u>yirπir</u>_ . Therefore, if the demand shock changes expected income by the same percentage in every neighborhood, _d_ ln _Hir_ + _d_ ln _Pir_ is a constant, call it _x_ . This could happen, for example, if a city experiences a change in the individual productivity dispersion parameter _ε_ . 

The resulting metro housing supply elasticity is a weighted average of tract-level elasticities, where the weight is the initial housing share adjusted for neighborhood supply elasticity. Using 

40 

_d_ ln _Pir_ = _x_ /(1 + _γir_ ) and using (24) to aggregate over tracts, we have 



This expression reflects the fact that tracts with more elastic supply will receive lower weight in aggregation because price growth is lower in these locations for a given demand shock. 

In reality, demand shocks are likely to hit some neighborhoods more than others as households move across tracts in search of lower housing costs. If this is the case, _γr_<sup>1would understate the true</sup> aggregate elasticity. As such, we now turn to the case in which we assume that aggregate housing demand shifts out in the city, but that people get distributed to neighborhoods only based on neighborhood-specific price increases. We further assume that that demand shock occurs in a way such that each tract has the same percentage change in price. This assumption can be justified in the context of a spatial equilibrium condition as in Roback (1982) in which each neighborhood differs in amenities but gets hit with the same income shock. In this case, the metro-level supply elasticity is the following: 



Tracts with higher initial housing stock are typically associated with smaller housing supply response, but these tracts are weighted more in _γr_<sup>2.Thus the resulting metro-level elasticity is likely</sup> to underestimate the true elasticity. 

Table 11 presents summary statistics about four versions of our two aggregate supply elasticity measures _γr_<sup>1and</sup><sup>_γ_</sup> _r_<sup>2.Becauseoursecondaggregationschemeallowsforsomeresidential</sup> substitution across tracts, the average of metro supply elasticities are slightly above grand tractlevel averages. All region level aggregate measures of supply elasticities are significantly lower in areas with a high fraction of land developed and most are also lower in regions with more unavailable land, with the hedonic price index based supply elasticities are more responsive in expected directions to land unavailability (unreported). The key observation here is that tract-level supply influencers also aggregate up to the metro level. Correlations between our metro level supply elasticity measures and those found by Saiz (2010) are all positive but they are stronger for our more broad-based hedonic indexes at 0.38. 

To this point, we have relied on arbitrary assumptions about housing demand to aggregate the tract-level supply elasticity into the metro-level supply elasticity. This approach, while useful, 

41 

cannot be used to perform an equilibrium analysis of the housing market nor a corresponding welfare analysis. 

### **6.2 Estimating the Neighborhood Demand System** 

We now turn to partial structural estimation of the model, which delivers parameters that govern demand substitution patterns across neighborhoods. To understand how neighborhood-specific demand shocks feed into price growth, we must first specify the housing demand system. We take this from the model in Section 3, using its structure to determine the substitution elasticities between neighborhoods. 

From (10) and (15), aggregate housing demand in each tract is given by 



Housing demand becomes more elastic as _η_ and<sup>_<u>φ</u>_</sup> _η_<sup>grow,as these objects reflect how fundamen-</sup> tally substitutible neighborhoods are for each other by residents. Therefore, understanding how much a given exogenous demand shock (through changes in _Bi_ for example) affects prices versus quantities requires knowledge of these parameters. Evident from the housing demand equation above, the elasticity of substitution between any two neighborhoods in the same municipality is _η_ (1 _− β_ ) + 1, increasing in _η_ . The elasticity of substitution between any two neighborhoods in different municipalities also depends on _φ_ . 

We develop an “estibration” strategy for _η_ and _φ_ using the structural equations (16) and (18) from the model for neighborhood and municipality population respectively. As inputs, we use estimates of _γir_ discussed above, estimates of ( _κε_ ) _r_ from gravity regressions and calibrated values for _β_ and _κ_ . The structural equations are estimated using GMM. (16) includes fixed effects for “municipalities”. After some experimentation with different definitions, we assign 5 municipalities to each region: one for the central city and one each for suburbs in north, south, east and westerly directions. We impose that the error term in (16) depends on all of the same control � variables as the regressions in Table 2 and is orthogonal to our main instrument _d_ ln _RMAi_ . To estimate (18), we build a municipality level data set and impose that its error term is orthogonal � to ∑ _i_ ( _m_ )[ _Si_ (1 _−_ 1<sup>1</sup> +<sup>_−_</sup> _γ_<sup>_<u>β</u>_</sup> _i_<sup>)]</sup><sup>_d_ln</sup> _RMAi_ , which only includes pre-determined objects. We calibrate _β_ to 0.2 

42 

and _κ_ to 0.005 or 0.01.<sup>19</sup> 

Table 13 presents these results. The first two columns show versions in which we assume preferences are not nested, and _φ_ = _η_ . The final two columns show results assuming fully nested preferences, each for different assumptions about _κ_ . We estimate _η_ to be between 1.5 and 3.5 and _φ_ to be between 3.8 and 8.8. Incorporation of nested choices reduces dispersion and raises substitutibility across neighborhoods. 

### **6.3 Opportunity Zones** 

Finally, we apply elasticity estimates to evaluate the 2017 Opportunity Zone (OZ) program. Among other incentives, this program reduces or eliminates capital gains taxes on real estate investments in certain poor census tracts nationwide in the US. We use our housing supply and demand elasticity estimates to calculate the incidence associated with this policy in different neighborhoods for residential housing only. Further impacts are beyond the scope of this analysis. We think of the capital gains tax as reducing the price that initial buyers are willing to pay per unit of housing services. When the capital gains tax is lifted, demand for affected neighborhoods increases due purely to investment motives. It is intuitive that neighborhoods with more elastic supply will draw in fewer new investors since potential returns are lower. 

This analysis is in progress. 

## **7 Conclusion** 

Since Rosenthal’s (1999) lament on the limited work on the supply side of housing, a number of studies have identified regulation and topographical conditions as determinants of supply elasticity. Saiz (2010) in his seminal work estimates housing supply elasticities at the metropolitan area level and characterizes them as a function of both physical and regulatory constraints. In this paper, we follow his insight and present the first set of estimates of the tract-level supply elasticities. Knowledge of local housing supply elasticities at a microgeographic scale is not only central to 

> 19 _κ_ = 0.005 implies that 1 minute of commuting in one direction reduces full income by 0.5%. We also tried estimating _κ_ jointly with neighborhood demand parameters, but this yielded implied values of _ε_ that were too low. This led us to our “estibration” strategy. 

43 

understanding within-city house price dynamics Glaeser et al. (2012); Guerrieri et al. (2013), but also important for evaluating place-based policy interventions Busso et al. (2013); Hanson (2009). 

We find that housing supply becomes more elastic further out from urban centers such that there is more variation within than between metro areas in housing supply elasticity. This pattern is in part but not entirely due to a larger fraction of land available for development. Initial development density, availability of flat land and zoning regimes are all important determinants of local housing supply. 

44 

## **References** 

- Ahlfeldt, G. M., & McMillen, D. P. (2014). New estimates of the elasticity of substitution of land for capital. _Louvain-la-Neuve: European Regional Science Association (ERSA)_ . 

- Ahlfeldt, G. M., Redding, S. J., Sturm, D. M., & Wolf, N. (2015). The economics of density: Evidence from the berlin wall. _Econometrica_ , _83_ (6), 2127–2189. 

- Albouy, D., & Ehrlich, G. (2012). _Metropolitan land values and housing productivity_ . Citeseer. 

- Bartik, T. J. (1991). Who benefits from state and local economic development policies? 

- Baum-Snow, N., Hartley, D. A., & Lee, K. O. (2019). The long-run effects of neighborhood change on incumbent families. 

- Been, V., Ellen, I., & Gedal, M. (2009). Teardowns and land values in new york city. In _Lincoln institute working paper._ 

- Bendimerad, A. (2007). _Developing a leading indicator for the remodeling industry_ . Joint Center for Housing Studies of Harvard University. 

- Brooks, L., & Lutz, B. (2016). From today’s city to tomorrow’s city: An empirical investigation of urban land assembly. _American Economic Journal: Economic Policy_ , _8_ (3), 69–105. 

- Brueckner, J. K., & Rosenthal, S. S. (2009). Gentrification and neighborhood housing cycles: Will america’s future downtowns be rich? _The Review of Economics and Statistics_ , _91_ (4), 725–743. 

- Brueckner, J. K., & Singh, R. (2018). Stringency of land-use regulation: Building heights in us cities. 

- Busso, M., Gregory, J., & Kline, P. (2013). Assessing the incidence and efficiency of a prominent place based policy. _American Economic Review_ , _103_ (2), 897–947. 

- Calabrese, S. M., Epple, D. N., & Romano, R. E. (2011). Inefficiencies from metropolitan political and fiscal decentralization: Failures of tiebout competition. _The Review of Economic Studies_ , _79_ (3), 1081–1111. 

- Charles, S. L. (2013). Understanding the determinants of single-family residential redevelopment in the inner-ring suburbs of chicago. _Urban Studies_ , _50_ (8), 1505–1522. 

- Choi, H.-S., Hong, H., & Scheinkman, J. (2014). Speculating on home improvements. _Journal of Financial Economics_ , _111_ (3), 609–624. 

- Combes, P.-P., Duranton, G., & Gobillon, L. (2019). The production function for housing: Evidence from france. 

45 

Cosman, J., Davidoff, T., & Williams, J. (2018). Housing appreciation and marginal land supply in monocentric cities with topography. 

- Couture, V., Gaubert, C., Handbury, J., & Hurst, E. (2019). _Income growth and the distributional effects of urban spatial sorting_ (Tech. Rep.). 

Davidoff, T. (2016). Supply constraints are not valid instrumental variables for home prices be- 

cause they are correlated with many demand factors. _Critical Finance Review_ , _5_ (2), 177–206. 

DiPasquale, D. (1999). Why don’t we know more about housing supply? _The Journal of Real Estate Finance and Economics_ , _18_ (1), 9–23. 

Duranton, G., & Puga, D. (2015). Urban land use. In _Handbook of regional and urban economics_ (Vol. 5, pp. 467–560). Elsevier. 

- Dye, R. F., & McMillen, D. P. (2007). Teardowns and land values in the chicago metropolitan area. _Journal of urban economics_ , _61_ (1), 45–63. 

- Epple, D., Gordon, B., & Sieg, H. (2010). A new approach to estimating the production function for housing. _American Economic Review_ , _100_ (3), 905–24. 

Genesove, D., & Han, L. (2013). A spatial look at housing boom and bust cycles. In _Housing and the financial crisis_ (pp. 105–141). University of Chicago Press. 

- Glaeser, E. L., Gottlieb, J. D., & Tobio, K. (2012). Housing booms and city centers. _American Economic Review_ , _102_ (3), 127–33. 

Glaeser, E. L., & Gyourko, J. (2005). Urban decline and durable housing. _Journal of political economy_ , _113_ (2), 345–375. 

- Glaeser, E. L., Gyourko, J., & Saks, R. E. (2005). Urban growth and housing supply. _Journal of economic geography_ , _6_ (1), 71–89. 

Guerrieri, V., Hartley, D., & Hurst, E. (2013). Endogenous gentrification and housing price dynamics. _Journal of Public Economics_ , _100_ , 45–60. 

- Hanson, A. (2009). Local employment, poverty, and property value effects of geographicallytargeted tax incentives: An instrumental variables approach. _Regional Science and Urban Economics_ , _39_ (6), 721–731. 

Housing productivity and the social cost of land-use restrictions. (n.d.). _Journal of Urban Economics_ , _107_ , 101. 

McMillen, D., & O’Sullivan, A. (2013). Option value and the price of teardown properties. _Journal_ 

46 

_of Urban Economics_ , _74_ , 71–82. 

- Monte, F., Redding, S. J., & Rossi-Hansberg, E. (2018). Commuting, migration, and local employment elasticities. _American Economic Review_ , _108_ (12), 3855-3890. 

- Munneke, H. J., & Womack, K. S. (2015). Neighborhood renewal: the decision to renovate or tear down. _Regional Science and Urban Economics_ , _54_ , 99–115. 

- Murphy, A. (2018). A dynamic model of housing supply. _American Economic Journal: Economic Policy_ , _10_ (4), 243–67. 

- Orlando, A., & Redfearn, C. (2018). What’s lost in the aggregate: Lessons from a local index of housing supply restrictions. _Unpublished Manuscript_ . 

- Ouazad, A., & Ranciere, R. (2019). City equilibrium with borrowing constraints: Structural estimation and general equilibrium effects. _International Economic Review_ , _60_ (2), 721-749. 

- Plaut, P., & Plaut, S. (2010). Decisions to renovate and to move. _Journal of Real Estate Research_ , _32_ (4), 461–484. 

- Rosenthal, S. S. (2018). Owned now rented later? housing stock transitions and market dynamics. Saiz, A. (2010). The geographic determinants of housing supply. _The Quarterly Journal of Economics_ , _125_ (3), 1253–1296. 

- Severen, C. (2019). _Commuting, labor, and housing market effects of mass transportation: Welfare and identification_ (Tech. Rep.). 

- Torchiana, A. L., Rosenbaum, T., Scott, P. T., & Souza-Rodrigues, E. (n.d.). _Improving estimates of transitions from satellite data: A hidden markov model approach_ (Tech. Rep.). 

- Tsivanidis, N. (2018). The aggregate and distributional effects of urban transit infrastructure: Evidence from bogotas transmilenio. _Unpublished manuscript_ . 

- von Ehrlich, M., Schöni, O., & Büchler, S. (2018). On the responsiveness of housing development to rent and price changes: Evidence from switzerland. 

- Yoshida, J. (2016). Structure depreciation and the production of real estate services. _Available at SSRN 2734555_ . 

- Zhou, Y., & Haurin, D. (2010). On the determinants of house value volatility. _Journal of Real Estate Research_ , _32_ (4), 377-395. 

- Zillow. (2017). _Ztrax: Zillow transaction and assessor dataset, 2017-q4._ (Zillow Group, Inc. http://www.zillow.com/ztrax/) 

47 

## **A Model Appendix** 

The fraction of residents of tract _i_ that work in _j Pr_ ( _viωPBi_<sup>1</sup><sup>_−_</sup> _iz_<sup>_β_</sup> _ijek_<sup>_κτ_</sup> _ω_<sup>_ij_</sup> _wjk >_ = max _j′_ , _k′ viωPBi_<sup>1</sup> _iz_<sup>_−_</sup> _i_<sup>_β_</sup> _<u>j′ekκτ′</u> ωijw′_ _<u>j′</u> k′_ ) can be determined using the properties of the Frechet draws _zijkω_ . 



We write this expression as a function of resident market access _RMAi ≡_ ∑ _k_ ∑ _j_ � _wjke_<sup>_−κτij_�</sup><sup>_ε_</sup> , which is a summary measure of the access to employment opportunities from residential neighborhood _i_ . 

Before the productivity shock is revealed, the expected income (wage net of commuting cost) _<u>yi</u>_ associated with residing in tract _i_ is _E_ (max _j_ , _k wjek_<sup>_<u>κτ</u>_</sup> _zi_<sup>_ij_</sup> _<u>jkω</u>_<sup>).Solving this through,</sup> 



This object is increasing in _RMAi_ and declining in _ε_ . As _ε_ increases, there is a smaller dispersion in skill prices across locations, reducing the probability of individuals receiving high wage offers in any location. 

The probability that _i_ is the highest utility residential location is the probability that the inclusive value of municipality m is the highest times the probability that neighborhood i is the highest utility neighborhood in municipality m. Using properties of the Frechet distribution, this _η η_ _<u>φ</u>_ <u>�</u> _Bi Pi_<sup>_β−_1</sup> _<u>yi</u>_ <u>�</u> ∑ _i_ ´ _∈m_ ( _i_ )� _Bi′ Pi_<sup>_β′−_1</sup> _<u>yi′</u>_ <u>�</u> ] _<u>η</u>_ second object is ∑ _i′_ <u>�</u> _Pi_<sup>_β′−_1</sup> _Bi′_ _<u>yi′</u>_ <u>�</u> _<u>η</u>_ . The second object is ∑ _m_ [∑ _i_ ´ _∈m_ ( _i_ )� _Bi′ Pi_<sup>_β′−_1</sup> _<u>yi′</u>_ <u>�</u> _η_ ] _<u>φη</u>_ ] Plugging in for _<u>yi</u>_ gives the population supply function in the text.. 

The probability that _j_ is the highest utility work location for a resident of any given tract i is _πij|i_ = ∑ _k_ <u>�</u> _wjke_<sup>_−κτij_</sup><sup><u>�</u></sup><sup>_ε_. Summing over the probability of living in</sup><sup>_i_, we recover the labor supply to</sup> ∑ _k_ ∑ _j′_ <u>�</u> _wj′ ke_<sup>_−κτij_</sup><sup><u>�</u></sup><sup>_<u>ε</u>_</sup> tract j in the text. 

48 

## **References** 

- Ahlfeldt, G. M., & McMillen, D. P. (2014). New estimates of the elasticity of substitution of land for capital. _Louvain-la-Neuve: European Regional Science Association (ERSA)_ . 

- Ahlfeldt, G. M., Redding, S. J., Sturm, D. M., & Wolf, N. (2015). The economics of density: Evidence from the berlin wall. _Econometrica_ , _83_ (6), 2127–2189. 

- Albouy, D., & Ehrlich, G. (2012). _Metropolitan land values and housing productivity_ . Citeseer. 

- Bartik, T. J. (1991). Who benefits from state and local economic development policies? 

- Baum-Snow, N., Hartley, D. A., & Lee, K. O. (2019). The long-run effects of neighborhood change on incumbent families. 

- Been, V., Ellen, I., & Gedal, M. (2009). Teardowns and land values in new york city. In _Lincoln institute working paper._ 

- Bendimerad, A. (2007). _Developing a leading indicator for the remodeling industry_ . Joint Center for Housing Studies of Harvard University. 

- Brooks, L., & Lutz, B. (2016). From today’s city to tomorrow’s city: An empirical investigation of urban land assembly. _American Economic Journal: Economic Policy_ , _8_ (3), 69–105. 

- Brueckner, J. K., & Rosenthal, S. S. (2009). Gentrification and neighborhood housing cycles: Will america’s future downtowns be rich? _The Review of Economics and Statistics_ , _91_ (4), 725–743. 

- Brueckner, J. K., & Singh, R. (2018). Stringency of land-use regulation: Building heights in us cities. 

- Busso, M., Gregory, J., & Kline, P. (2013). Assessing the incidence and efficiency of a prominent place based policy. _American Economic Review_ , _103_ (2), 897–947. 

- Calabrese, S. M., Epple, D. N., & Romano, R. E. (2011). Inefficiencies from metropolitan political and fiscal decentralization: Failures of tiebout competition. _The Review of Economic Studies_ , _79_ (3), 1081–1111. 

- Charles, S. L. (2013). Understanding the determinants of single-family residential redevelopment in the inner-ring suburbs of chicago. _Urban Studies_ , _50_ (8), 1505–1522. 

- Choi, H.-S., Hong, H., & Scheinkman, J. (2014). Speculating on home improvements. _Journal of Financial Economics_ , _111_ (3), 609–624. 

- Combes, P.-P., Duranton, G., & Gobillon, L. (2019). The production function for housing: Evidence from france. 

49 

Cosman, J., Davidoff, T., & Williams, J. (2018). Housing appreciation and marginal land supply in monocentric cities with topography. 

- Couture, V., Gaubert, C., Handbury, J., & Hurst, E. (2019). _Income growth and the distributional effects of urban spatial sorting_ (Tech. Rep.). 

Davidoff, T. (2016). Supply constraints are not valid instrumental variables for home prices be- 

cause they are correlated with many demand factors. _Critical Finance Review_ , _5_ (2), 177–206. 

DiPasquale, D. (1999). Why don’t we know more about housing supply? _The Journal of Real Estate Finance and Economics_ , _18_ (1), 9–23. 

Duranton, G., & Puga, D. (2015). Urban land use. In _Handbook of regional and urban economics_ (Vol. 5, pp. 467–560). Elsevier. 

- Dye, R. F., & McMillen, D. P. (2007). Teardowns and land values in the chicago metropolitan area. _Journal of urban economics_ , _61_ (1), 45–63. 

- Epple, D., Gordon, B., & Sieg, H. (2010). A new approach to estimating the production function for housing. _American Economic Review_ , _100_ (3), 905–24. 

Genesove, D., & Han, L. (2013). A spatial look at housing boom and bust cycles. In _Housing and the financial crisis_ (pp. 105–141). University of Chicago Press. 

Glaeser, E. L., Gottlieb, J. D., & Tobio, K. (2012). Housing booms and city centers. _American Economic Review_ , _102_ (3), 127–33. 

Glaeser, E. L., & Gyourko, J. (2005). Urban decline and durable housing. _Journal of political economy_ , _113_ (2), 345–375. 

- Glaeser, E. L., Gyourko, J., & Saks, R. E. (2005). Urban growth and housing supply. _Journal of economic geography_ , _6_ (1), 71–89. 

Guerrieri, V., Hartley, D., & Hurst, E. (2013). Endogenous gentrification and housing price dynamics. _Journal of Public Economics_ , _100_ , 45–60. 

- Hanson, A. (2009). Local employment, poverty, and property value effects of geographicallytargeted tax incentives: An instrumental variables approach. _Regional Science and Urban Economics_ , _39_ (6), 721–731. 

Housing productivity and the social cost of land-use restrictions. (n.d.). _Journal of Urban Economics_ , _107_ , 101. 

McMillen, D., & O’Sullivan, A. (2013). Option value and the price of teardown properties. _Journal_ 

50 

_of Urban Economics_ , _74_ , 71–82. 

- Monte, F., Redding, S. J., & Rossi-Hansberg, E. (2018). Commuting, migration, and local employment elasticities. _American Economic Review_ , _108_ (12), 3855-3890. 

- Munneke, H. J., & Womack, K. S. (2015). Neighborhood renewal: the decision to renovate or tear down. _Regional Science and Urban Economics_ , _54_ , 99–115. 

- Murphy, A. (2018). A dynamic model of housing supply. _American Economic Journal: Economic Policy_ , _10_ (4), 243–67. 

- Orlando, A., & Redfearn, C. (2018). What’s lost in the aggregate: Lessons from a local index of housing supply restrictions. _Unpublished Manuscript_ . 

- Ouazad, A., & Ranciere, R. (2019). City equilibrium with borrowing constraints: Structural estimation and general equilibrium effects. _International Economic Review_ , _60_ (2), 721-749. 

- Plaut, P., & Plaut, S. (2010). Decisions to renovate and to move. _Journal of Real Estate Research_ , _32_ (4), 461–484. 

- Rosenthal, S. S. (2018). Owned now rented later? housing stock transitions and market dynamics. Saiz, A. (2010). The geographic determinants of housing supply. _The Quarterly Journal of Economics_ , _125_ (3), 1253–1296. 

- Severen, C. (2019). _Commuting, labor, and housing market effects of mass transportation: Welfare and identification_ (Tech. Rep.). 

- Torchiana, A. L., Rosenbaum, T., Scott, P. T., & Souza-Rodrigues, E. (n.d.). _Improving estimates of transitions from satellite data: A hidden markov model approach_ (Tech. Rep.). 

- Tsivanidis, N. (2018). The aggregate and distributional effects of urban transit infrastructure: Evidence from bogotas transmilenio. _Unpublished manuscript_ . 

- von Ehrlich, M., Schöni, O., & Büchler, S. (2018). On the responsiveness of housing development to rent and price changes: Evidence from switzerland. 

- Yoshida, J. (2016). Structure depreciation and the production of real estate services. _Available at SSRN 2734555_ . 

- Zhou, Y., & Haurin, D. (2010). On the determinants of house value volatility. _Journal of Real Estate Research_ , _32_ (4), 377-395. 

- Zillow. (2017). _Ztrax: Zillow transaction and assessor dataset, 2017-q4._ (Zillow Group, Inc. http://www.zillow.com/ztrax/) 

51 

#### **Table 1:** Summary Statistics 

||Mean|||Growth|Rate||
|---|---|---|---|---|---|---|
|**Tract Home Price Changes (Estimation Sample)**|Growth|Mean|St Dev|Min|Max|Obs|
|Repeat Sales Index, 2000-2006||0.89|0.86|-1.77|69.07|24,773|
|Zillow Hedonic Index, 2000-2006||0.95|0.77|-2.04|15.28|24,975|
|Repeat Sales Index, 2000-2010||0.37|0.52|-3.20|17.52|23,877|
|Zillow Hedonic Index, 2000-2010||0.45|0.56|-10.11|8.57|24,697|
|Census Hedonic Index, 2000-2010||0.01|0.21|-3.63|2.30|31,263|
|Census Hedonic Index, 1990-2000||0.00|0.18|-2.38|2.15|31,263|
|**Tract Housing Quantity Changes (Estimation Sample)**|||||||
|Stock of Housing Units, Census, 2000-2010|181|0.07|0.23|-3.18|5.91|31,250|
|Stock of Housing Units, Census, 1990-2000|202|0.14|0.32|-3.94|4.91|31,124|
|New Units, ACS, 2000-2009|237|0.11|0.20|0.00|5.83|31,242|
|New Units, Zillow, 2000-2006|193|0.09|0.19|0.00|5.68|30,606|
|New Units, Zillow, 2000-2009|232|0.10|0.21|0.00|5.90|30,605|
|Stock of Quality Adjusted Housing, 2000-2006||0.33|1.03|0.00|9.73|21,198|
|Stock of Quality Adjusted Housing, 2000-2010||0.53|1.22|0.00|10.02|21,187|
|New Units on Developed Land, ACS, 2000-2010|87|0.05|0.11|0.00|4.93|31,250|
|Stock of Housing on the Intensive Margin, 2000-2010||0.47|1.20|0.00|9.18|21,180|
|**Tract Employment and Population Variables (Full Sample)**|||||||
|RMA, 2000-2006 (excludes 8 regions)||0.04|0.05|-0.88|0.76|59,752|
|Simulated RMA, 2000-2006||0.05|0.01|-0.02|0.09|63,897|
|Tract Employment, 2000-2006 (excl 8 regions)|53|-0.16|0.90|-8.96|6.04|61,359|
|Tract Employment, 2000-2010|78|-0.17|0.89|-11.25|6.39|63,616|
|Tract Level Bartik Instrument, 2000-2006||0.09|0.05|-0.13|0.25|63,897|
|Tract Population, 2000-2010|330|0.04|0.28|-5.56|7.37|63,578|
|**Tract Level Supply Infuencers (Full Available Sample)**|||||||
|Fraction of Land Area Developed, 2001||0.38|0.25|0.00|0.90|63,896|
|Fraction of Land Area Developed, 2011||0.39|0.24|0.00|0.90|63,896|
|Fraction of Land Area Flat||0.41|0.42|0.00|1.00|63,896|
|Fraction of Land Area Not Flat but Slope < 8%||0.45|0.37|0.00|1.00|63,896|
|Elevation Range (m)||64|147|0|4325|63,896|
|Wharton Real Estate Index (municipality level variation)||0.13|0.91|-2.02|4.22|30,526|
|Parcel Size Weighted Residential Floor Area Ratio (8 cities)||2.33|2.02|0.25|16.00|8,707|
|**Metro Level Supply Infuencers (Full Sample)**|||||||
|Fraction of Area Developed||0.05|0.04|0.00|0.38|306 metros|
|Fraction of Metro Area Unavailable for Development||0.26|0.20|0.00|0.87|306 metros|
|Fraction of Area Within 50 km of CBD Unavailable for Development||0.23|0.17|0.00|0.82|306 metros|
|Wharton Regulation Index (2008)||-0.08|0.82|-1.76|2.82|261 metros|



52 

**Table 2:** OLS Results for Housing Supply 

##### **(a)** Controls for Region Fixed Effects 

|Quantity Measure<br>Source<br>Time Period|New Units<br>Zillow<br>2000-2006|New Units<br>Zillow<br>2000-2010|New Units<br>ACS<br>2000-2010|∆Units<br>Census<br>2000-2010|∆Quantity Index<br>Zillow<br>2000-2010|∆Intensive Margin<br>Zillow & Census<br>2000-2010|New Units, Redev.<br>Zillow & USGS<br>2000-2010|
|---|---|---|---|---|---|---|---|
||(1)|(2)|(3)|(4)|(5)|(6)|(7)|
|Census Hedonic Index||-0.0908***|-0.0919***|-0.0921***|0.0198|0.0757**|-0.0306***|
|||(0.00508)|(0.00478)|(0.00556)|(0.0368)|(0.0364)|(0.00293)|
|Zillow Repeat Sales Index|0.00310**|0.0123***|0.0140***|0.0191***|0.0537**|0.0355*|0.0103***|
||(0.00131)|(0.00283)|(0.00266)|(0.00297)|(0.0211)|(0.0208)|(0.00158)|
|Zillow Hedonic Index|0.0136***|0.0161***|0.0151***|0.0104***|0.118***|0.110***|0.00903***|
||(0.00254)<br><br>|(0.00320)<br>**(b)**Contro<br>|(0.00302)<br>ls for Re<br>|(0.00337)<br>gion-Rin<br>|(0.0230)<br>g Fixed Effects<br>|(0.0227)<br> <br>|(0.00178)<br>|
|Quantity Measure|New Units|New Units|New Units|∆Units|∆Quantity Index|∆Intensive Margin|New Units, Redev.|
|Source|Zillow|Zillow|ACS|Census|Zillow|Zillow & Census|Zillow & USGS|
|Time Period|2000-2006|2000-2010|2000-2010|2000-2010|2000-2010|2000-2010|2000-2010|
||(1)|(2)|(3)|(4)|(5)|(6)|(7)|
|Census Hedonic Index||-0.0851***|-0.0874***|-0.0879***|-0.0518|0.00193|-0.0334***|
|||(0.00520)|(0.00493)|(0.00573)|(0.0366)|(0.0362)|(0.00306)|
|Observations||30,605|31,242|31,250|21,187|21,180|31,250|
|# of Regions Included||274|275|275|224|224|275|
|Zillow Repeat Sales Index|0.000803|0.00680**|0.00948***|0.0107***|0.0115|0.000683|0.00703***|
||(0.00132)|(0.00291)|(0.00276)|(0.00306)|(0.0212)|(0.0210)|(0.00164)|
|Observations|24,771|23,876|23,870|23,877|16,407|16,407|23,877|
|# of Regions Included|161|163|163|163|146|146|163|
|Zillow Hedonic Index|0.0108***|0.0106***|0.0109***|0.00129|0.0233|0.0254|0.00623***|
||(0.00274)|(0.00351)|(0.00332)|(0.00371)|(0.0237)|(0.0234)|(0.00197)|
|Observations|24,969|24,694|24,689|24,697|17,457|17,457|24,697|
|# of Regions Included|164|169|169|169|152|152|169|



Note: Each cell corresponds to the estimate from running an OLS regression of changes in housing quantities measured as in described in the column on changes in house price index measured as described in the row. All specifications include the 1990 and 2000 log employment, log house value, log rent, the distance to CBD and its square, 10 and 20 years lags of tract-level demographic controls such as population, average household income, the share of African American, the share of white people and the share of college graduate students. The top panel controls for the metropolitan area fixed effects and the bottom panel controls for the within-metropolitan-area ring fixed effects. 

53 

**Table 3:** Tract Level Regressions of Employment Growth on Bartik Shocks 

||∆ln Emp,|2000-2006|∆ln Emp|, 2000-2010|
|---|---|---|---|---|
|Tract Level Bartik Shock for 2000-2006|0.247***|0.172*|0.636***|0.626***|
||(0.0940)|(0.100)|(0.0920)|(0.0980)|
|Indicator for 0 Tract Employment in 2000|-0.00373|0.000515|0.0496**|0.0648***|
||(0.0209)|(0.0243)|(0.0204)|(0.0236)|
|Observations|61,359|61,359|63,616|63,616|
|R-Squared|0.058|0.050|0.055|0.047|
|Region Fixed Effects|298||306||
|Region-Ring Fixed Effects||4,392||4,523|



**Table 4:** Relationships Between 1990-2000 and 2000-2006/10 Tract Housing Dynamics 

||∆ln Ho|use Price|∆ln Hous|e Quantity|∆ln Si|m. RMA|
|---|---|---|---|---|---|---|
||2000|-2010|2000|-2010|2000|-2006|
|∆ln House Price, 1990-2000|-0.277***|-0.301***|-0.0162**|-0.0260***|4.81e-05|-4.04e-05|
||(0.00662)|(0.00706)|(0.00653)|(0.00675)|(7.49e-05)|(6.32e-05)|
|∆ln House Quantity, 1990-2000|0.0302**|0.0209*|0.121***|0.0779***|-5.75e-05|-0.000219**|
||(0.0119)|(0.0124)|(0.0109)|(0.0109)|(0.000131)|(0.000107)|
|Lagged Demographic Controls|Yes|Yes|Yes|Yes|Yes|Yes|
|FE|Metro|Ring|Metro|Ring|Metro|Ring|



54 

**Table 5:** First Stage and Reduced Form Results 

|||∆ln RMA,|2000-2006||∆Rep|eated Sales|Index, 200|0-2006|
|---|---|---|---|---|---|---|---|---|
|∆ln Simulated RMA, 2000-2006|0.694***|0.639***|0.586***|0.546***|12.43***|13.68***|7.966***|10.60***|
||(0.0510)|(0.0507)|(0.0532)|(0.0532)|(2.396)|(2.386)|(3.039)|(3.034)|
|Observations|28,381|28,381|28,381|28,381|24,773|24,773|24,773|24,773|
|R-squared|0.010|0.033|0.006|0.013|0.009|0.027|0.001|0.017|
||∆Rep|eated Sales|Index, 200|0-2010|∆Cens|us Hedonic|Index, 200|0-2010|
|∆ln Simulated RMA, 2000-2006|7.235***|6.983***|2.804*|5.019***|2.074***|1.818***|3.480***|2.138***|
||(1.382)|(1.273)|(1.690)|(1.576)|(0.519)|(0.495)|(0.691)|(0.654)|
|Observations|23,877|23,877|23,877|23,877|31,263|31,263|31,263|31,263|
|R-squared|0.016|0.174|0.004|0.144|0.003|0.099|0.004|0.1147|
||∆ln N|ew Units in|Zillow, 200|0-2006|∆ln N|ew Units in|Zillow, 200|0-2010|
|∆ln Simulated RMA, 2000-2006|2.341***|1.615***|2.764***|2.255***|2.557***|1.792***|3.058***|2.522***|
||(0.449)|(0.415)|(0.562)|(0.533)|(0.499)|(0.461)|(0.621)|(0.587)|
|Observations|30,606|30,606|30,606|30,606|30,605|30,605|30,605|30,605|
|R-squared|0.062|0.207|0.012|0.122|0.061|0.209|0.012|0.125|
|Lagged Demographic Controls|No|Yes|No|Yes|No|Yes|No|Yes|
|FE|Metro|Metro|Ring|Ring|Metro|Metro|Ring|Ring|



55 

**Table 6:** IV Result for Housing Supply 

|∆Quantity|New Units|New Units|New Units|∆Units|∆Space|∆Quality<br>-Adj.|Redev.|
|---|---|---|---|---|---|---|---|
|Source|Zillow|Zillow|ACS|Census|Zillow|Zillow|Zillow|
|||||||Census||
|Time Period|00-06|00-10|00-10|00-10|01-11|01-11|00-10|
||(1)|(2)|(3)|(4)|(5)|(6)|(7))|
|Census HI||1.01**|0.81**|1.25***|7.35|7.38***|0.33*|
|||(0.42)|(0.34)|(0.46)|(2.19)|(2.11)|(0.17)|
|1st-Stage F||11.63|13.23|13.29|14.23|1.76|13.29|
|Zillow RS|0.17***|0.40***|0.33***|0.41***|2.67***|2.62***|0.14***|
||(0.047)|(0.11)|(0.09)|(0.11)|(0.67)|(0.66)|(0.05)|
|1st-Stage F|32.73|30.09|30.09|30.09|20.75|5.47|30.09|
|Zillow HI|0.22***|0.51***|0.41***|0.54***|3.83***|3.83***|0.16**|
||(0.06)|(0.16)|(0.14)|(0.17)|(0.99)|(0.98)|(0.07)|
|1st-Stage F|66.29|19.59|19.48|19.57|17.92|9.69|19.57|
|FE|metro|metro|metro|metro|metro|metro|metro|
||(1)|(2)|(3)|(4)|(5)|(6)|(7)|
|Census HI||1.27**|0.87**|1.07**|7.35**|7.52***|0.23|
|||(0.55)|(0.39)|(0.47)|(2.19)|(2.25)|(0.18)|
|1st-Stage F||11.63|13.23|13.29|14.23|1.76|13.29|
|Zillow RS|0.28***|0.63***|0.51**|0.56**|4.58***|4.38***|0.17*|
||(0.10)|(0.23)|(0.20)|(0.22)|(1.69)|(1.67)|(0.09)|
|1st-Stage F|32.73|30.09|30.09|30.09|20.75|5.47|30.09|
|Zillow HI|0.21***|0.43***|0.35***|0.36***|3.15***|3.13****|0.11*|
||(0.06)|(0.13)|(0.11)|(0.17)|(0.12)|(0.67)|(0.06)|
|1st-Stage F|66.29|19.59|19.48|19.57|17.92|9.69|19.57|
|FE|ring|ring|ring|ring|ring|ring|ring|



Note: Each entry shows the estimate from an IV regression of change in the housing quantity measure in the column header on changes in the house price index measured indicated in each row. Panel A includes MSA fixed effects and Panel B includes MSA fixed effects interacted with CBD distance bands of 2 km width. All specifications include 1990 and 2000 log employment, log house value, log rent, the distance to CBD and its square, 10 and 20 years lags of the following tract-level demographic controls: log population, log average household income, share African American, share White, share college graduates. 

56 

**Table 7:** Unit Supply: Heterogeneity by CBD Distance and Tract-Level Supply Conditions 

||(1)|(2)<br>∆Qu|(3)<br>antity (Zi|(4)<br>llow)|(5)|(6)<br>∆Redev.|(7)|(8)<br>∆Qu|(9)<br>antity (Zi|(10)<br>llow)|(11)|(12)<br>∆Redev.|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|∆ln_P_|0.22*|0.51***|0.12***|-0.08|1.04**|0.18***|0.33**|1.06***|0.04|-0.46**|-0.02|0.37***|
||(0.12)|(-0.13)|(0.04)|(0.14)|(0.50)|(0.05)|(0.14)|(0.30)|(0.05)|(0.17)|(0.07)|(0.11)|
|∆ln_P ×_dis|2.01***|1.76***|0.62***|0.36**|1.73**|0.46**|1.46***|1.42***|0.14|0.16|0.43***|0.23|
||(0.51)|(0.58)|(0.22)|(0.16)|(0.76)|(0.21)|(0.34)|(0.46)|(0.11)|(0.22)|(0.18)|(0.17)|
|∆ln_P ×_dis_×_dis|-1.06***|-0.84***|-0.56**|-0.62***|-0.86**|-0.26**|-1.04***|-1.51***|0.07|0.37|0.09|-0.52***|
||(0.26)|(0.31)|(0.23)|(0.22)|(0.33)|(0.11)|(0.24)|(0.49)|(0.25)|(0.46)|(0.29)|(0.18)|
|∆ln_P ×_Edge|0.99**|0.88**|0.17*|0.003|0.87*|0.21|0.06*|0.05|-0.05|-0.02|-0.06*|0.03|
||(0.37)|(0.36)|(0.10)|(0.14)|(0.45)|(0.13)|(0.03)|(0.06)|(0.03)|(0.03)|(0.03)|(0.03)|
|∆ln_P ×_% Dev||-0.47***|-0.76***|-0.07**|-0.50***|-0.16***||-0.92***|-0.51***|0.07|-0.49***|-0.30***|
|||(0.07)|(0.03)|(0.03)|(0.19)|(0.02)||(0.16)|(0.04)|(0.06)|(0.04)|(0.06)|
|∆ln_P ×_% Flat||0.34***|0.52***|0.09**|0.28**|0.10***||0.35***|0.46***|0.17***|0.46***|0.08***|
|||(0.04)|(0.03)|(0.05)|(0.11)|(0.02)||(0.05)|(0.03)|(0.06)|(0.03)|(0.02)|
|∆ln P_×_% Dev_×_% Flat||-0.77***|-0.75***|-0.11*|-0.63**|-0.21***||-0.46***|-0.64***|-0.65***|-0.07**||
|||(0.12)|(0.05)|(0.06)|(0.31)|(0.05)||(0.10)|(0.04)|(0.04)|(0.03)||
|FARRM||||0.07***||||||0.09***|||
|||||(0.01)||||||(0.02)|||
|∆ln_P ×_MSA % Devr50|||||-1.17||||||-0.31||
|‘|||||(3.70)||||||(0.22)||
|∆ln_P ×_MSA % Unavr50|||||-2.77||||||0.18**||
||||||(4.35)||||||(0.07)||
|FE|Metro|Metro|Muni|Metro|Metro|Metro|Metro|Metro|Muni|Metro|Metro|Metro|
|∆ln_P_Measure|. RS|RS|RS|RS|RS|RS|HI|HI|HI|HI|HI|HI|
|Observations|23,874|23,874|22,822|1,512|23,874|23,875|24,690|24,690|23,649|2,021|23,649|24,693|



Note: All specifications include the 1990 and 2000 log employment, log house value, log rent, the distance to CBD and its square, 10 and 20 years lags of tract-level demographic controls such as population, average household income, the share of African American, the share of white people, the share of college graduate students and metropolitan area fixed effects. 

57 

**Table 8:** Quality-Adjusted Supply: Heterogeneity by Tract-Level Supply Conditions 

|∆Quality|∆Space|∆Space|∆Quality|∆Quality|∆Space|∆Space|∆Quality|∆Quality|
|---|---|---|---|---|---|---|---|---|
|Supply|||Adjusted|Adjusted|||Adjusted|Adjusted|
||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|
|∆ln_P_|2.97***|-0.23|2.95***|-0.22|5.43***|-0.32*|5.48***|-0.28*|
||(0.71)|(0.15)|(0.70)|(0.15)|(1.55)|(0.16)|(1.55)|(0.16)|
|∆ln_P ×_% Dev|-0.79***|-0.71***|-0.86***|-0.67***|-2.76***|-0.16|-2.82***|-0.17|
||(0.18)|(0.10)|(0.18)|(0.10)|(0.79)|(0.11)|(0.79)|(0.12)|
|∆ln_P ×_% Flat|-0.23|0.39***|-0.24|0.38***|0.12|0.63***|0.12|0.64***|
||(0.17)|(0.10)|(0.25)|(0.10)|(0.18)|(0.10)|(0.18)|(0.10)|
|∆ln P_×_% Dev_×_% Flat|0.11|0.07|0.24|0.17|0.29|-0.74***|0.33|-0.75***|
||(0.26)|(0.16)|(0.25)|(0.16)|(0.28)|(0.13)|(0.28)|(0.13)|
|FE|Metro|Muni|Metro|Muni|Metro|Muni|Metro|Muni|
|∆ln_P_Measure|RS|RS|RS|RS|HI|HI|HI|HI|
|Observations|22609|21650|22595|21635|23692|22745|23689|22741|



Note: All specifications include the 1990 and 2000 log employment, log house value, log rent, 10 and 20 years lags of tract-level demographic controls such as population, average household income, the share of African American, the share of white people, the share of college graduate students and metropolitan area fixed effects. 

58 

**Table 9:** Heterogeneity by CBD Distance and Metro-level Supply Conditions 

##### **(a)** Over Repeated-Sales Price Growth 

||(1)|(2)|(3)|(4)|(5)|(6)|(7)|(8)|(9)|
|---|---|---|---|---|---|---|---|---|---|
|||||∆Q|uantity(Zillo|w)||||
|∆ln_P_|0.209*|21.74|0.943|1.873|0.284|2.148|0.849|-1.133***|1.927|
||(0.111)|(199.9)|(0.573)|(2.748)|(0.521)|(11.85)|(0.672)|(0.412)|(4.627)|
|∆ln_P ×_dis|2.116***|6.633|2.509***|3.373|2.122***|4.719|2.508**|2.817***|1.197|
||(0.632)|(39.27)|(0.972)|(2.458)|(0.616)|(41.92)|(1.015)|(0.435)|(6.687)|
|∆ln_P ×_dis_×_dis|-0.897***|0.303|-1.083***|-0.886**|-0.874***|-1.196|-1.120**|-1.228***|-0.395|
||(0.239)|(12.72)|(0.377)|(0.438)|(0.296)|(8.932)|(0.529)|(0.196)|(1.268)|
|∆ln_P ×_MSA % Dev50||-119.9||||5.653|||-11.52|
|||(1,073)||||(166.8)|||(17.22)|
|∆ln_P ×_MSA % Devr50|||-5.820||||-5.938|||
||||(3.694)||||(4.292)|||
|∆ln_P ×_MSA % Unav50||||-13.47||-21.07|||-6.645|
|||||(22.27)||(254.2)|||(64.88)|
|∆ln_P ×_MSA % Unavr50|||||-0.580||0.840|||
||||||(4.098)||(5.864)|||
|WRLURI||||||||-0.511*|0.879|
|||||||||(0.266)|(3.124)|
|Observations|23,874|23,874|23,874|23,874|23,874|23,874|23,874|23,874|23,874|



##### **(b)** Over Hedonic-Adjusted Price Growth 

|||||∆Qua|ntity(Zillo|w)||||
|---|---|---|---|---|---|---|---|---|---|
|∆ln_P_|0.351**|-0.400|-0.502*|-0.494|1.935|-0.632|1.313|-0.688***|-1.024|
||(0.143)|(0.484)|(0.260)|(0.578)|(9.581)|(0.585)|(6.672)|(0.188)|(0.803)|
|∆ln_P ×_dis|1.390***|2.452***|2.430***|3.116**|6.762|2.908**|6.407|2.551***|-0.061|
||(0.327)|(0.533)|(0.443)|(1.250)|(16.20)|(1.171)|(13.77)|(0.638)|(1.045)|
|∆ln_P ×_dis_×_dis|-0.877***|-0.821***|-0.879***|-1.501**|-4.055|-1.557**|-3.670|-1.018***|-1.190|
||(0.200)|(0.149)|(0.177)|(0.728)|(10.69)|(0.607)|(8.555)|(0.354)|(0.823)|
|∆ln_P ×_MSA % Dev50||-1.254||||3.108|||2.210|
|||(3.608)||||(2.864)|||(2.142)|
|∆ln_P ×_MSA % Devr50|||-0.910||||-7.127|||
||||(1.335)||||(25.84)|||
|∆ln_P ×_MSA % Unav50||||-5.670||-4.797|||4.606|
|||||(3.929)||(3.794)|||(6.015)|
|∆ln_P ×_MSA % Unavr50|||||-36.24||-32.10|||
||||||(107.7)||(85.31)|||
|WRLURI||||||||-0.492|0.523*|
|||||||||(0.632)|(0.281)|
|Observations|24,690|24,690|24,690|24,690|24,690|24,690|24,690|24,690|24,690|



Note: All specifications include the 1990 and 2000 log employment, log house value, log rent, the distance to CBD and its square, 10 and 20 years lags of tract-level demographic controls such as population, average household income, the share of African American, the share of white people, the share of college graduate students and metropolitan area fixed effects. The top panel uses the repeated sales price growth and the bottom panel uses the hedonic price growth. 

59 

**Table 10:** Tract Level Supply Elasticities ( _γi_ ) 

||5%|25%|50%|75%|95%|Mean|S.D|obs|
|---|---|---|---|---|---|---|---|---|
|Based on|Repea|ted-Sal|es Pric|e Grow|th||||
|Unit Supply Elasticity|0.14|0.45|0.74|1.08|1.48|0.78|0.42|63,896|
|Redevelop Supply Elasticity|0.06|0.15|0.22|0.30|0.38|0.22|0.10|63,896|
|Space Supply Elasticity|2.21|2.38|2.56|2.73|2.90|2.56|0.21|63,896|
|Quality-Adjusted Supply Elasticity|2.20|2.37|2.53|2.70|2.87|2.53|0.21|63,896|
|Intensive Margin Supply Elasticity|1.77|1.92|1.98|2.07|2.14|1.98|0.11|63,896|
|Based|on He|donic P|rice G|rowth|||||
|Unit Supply Elasticity|0.26|0.62|0.91|1.12|1.36|0.87|0.38|63,896|
|Redevelop Supply Elasticity|0.06|0.16|0.23|0.29|0.40|0.23|0.10|63,896|
|Space Supply Elasticity|3.23|3.84|3.87|4.36|5.16|4.28|0.60|63,896|
|Quality-Adjusted Supply Elasticity|3.24|3.88|4.35|4.81|5.20|4.31|0.61|63,896|
|Intensive Margin Supply Elasticity|2.80|3.22|3.49|3.79|4.08|3.48|0.38|63,896|



Note; The tract-level supply elasticities reported in this table are imputed using the estimates from Specifications (2), (6), (8) and (12) in Table 7 and Specifications (1), (3), (5) and (7) in Table 8, combined with the tract-level data on cbd distance, developed fraction and topographical features. 

60 

**Table 11:** Summary Statistics of Imputed Metro-Level Supply Elasticities 

||Mean|StdDev|Min|Max|# Obs|Corr_ρ_|
|---|---|---|---|---|---|---|
||L<br>|. .<br>ess Neighb<br>|orhood Su<br>|bstitution<br>|<br>|. <br>|
|Unit Supply Elasticity (RS)|.8442|.1462|.3068|1.2012|306|0.2006**|
|Unit Supply Elasticity (HI)|.9987|.1262|.4364|1.2572|306|0.3791**|
|Quality Supply Elasticity (RS)|2.6283|.1037|2.3021|2.8229|306|0.3657**|
|QualitySupplyElasticity(HI)|4.6144|.2418|3.5023|5.0174|306|0.4251**|
|||More N|eighborh|ood Substit|ution||
|Unit Supply Elasticity (RS)|.9183|.1475|.3714|1.2672|306|0.2114**|
|Unit Supply Elasticity (HI)|1.0337|.1190|.4986|1.2919|306|0.3819**|
|Quality Supply Elasticity (RS)|2.6340|.1033|2.3097|2.8249|306|0.3571**|
|QualitySupplyElasticity(HI)|4.6493|.2318|3.5515|5.0272|306|0.4280**|
|Saiz SupplyElasticity|2.6093|S<br>1.4643|aiz Supply<br>.5953|Elasticity<br>12.1480|236|1|



Note: _ρ_ shows the pairwise correlation between the imputed metro-leve elasticities and the Saiz measure of metro-level housing supply elasticity. * indicates 10%; ** indicates 1% level significance for the null hypothesis of independency between _γ_ and the Saiz elasticity. 

61 

**Table 12:** Heterogeneity in Metro-level Supply Elasticities 

**(a)** Less Neighborhood Substitution 

||(1)|(2)|(3)|(4)|
|---|---|---|---|---|
||Unit|Unit|Quality|Quality|
||(RS)|(HI)|(RS)|(HI)|
|MSA % Devr50|0.14|-0.71***|-0.65***|-2.38***|
||(0.18)|(0.14)|(0.12)|(0.24)|
|MSA % Unavr50|-0.02|-0.04|0.11***|-0.05|
||(0.04)|(0.04)|(0.03)|(0.07)|
|WRLURI|-0.04***|-0.05***|-0.02***|-0.09***|
||(0.01)|(0.01)|(0.01)|(0.02)|
|Observations|306|306|306|306|
|**(b)**More|Neighbo|rhood S|ubstitutio|n|
||(1)|(2)|(3)|(4)|
||Unit|Unit|Quality|Quality|
||(RS)|(HI)|(RS)|(HI)|
|MSA % Devr50|0.07|-0.71***|-0.65***|-2.34***|
||(0.18)|(0.13)|(0.12)|(0.23)|
|MSA % Unavr50|-0.05|-0.06*|0.11***|-0.04|
||(0.05)|(0.04)|(0.03)|(0.06)|
|WRLURI|-0.03**|-0.04***|-0.02***|-0.08***|
||(0.01)|(0.01)|(0.01)|(0.02)|
|Observations|306|306|306|306|



Note: The dependent variable is the imputed metro-level supply elasticity. MSA % Devr50 indicates the fraction of developed land within 50% of maximum radius from the CBD; MSA % Unavr50 indicates the fraction of area that is lose to hills, water and wetland within 50% of maximum radius from the CBD; WRLURI indicates the metropolitanarea-level WRLURI indices. 

62 

**Table 13:** Demand Substitution Parameters from Estibration 

||(1)|(2)|(3)|(4)|
|---|---|---|---|---|
||One layer|One layer|Two layer|Two layer|
||choice|choice|nested choice|nested choice|
|_κ_|0.005|0.01|0.005|0.01|
|_η_|2.58|1.46*|3.45***|1.89***|
||(1.69)|(0.75)|(1.43)|(0.58)|
|_φ_|||8.78***|3.84***|
||||(0.62)|(0.24)|
|_ϵ_min|2.24|1.12|2.24|1.12|
|_ϵ_max|21.40|10.70|21.4|10.7|
|_ϵ_mean|5.60|2.80|8.1|4.05|



Standard errors in parentheses 

63 

**Figure 1:** CBD Distance Patterns in Tract-Level Supply Conditions 



<!-- Start of picture text -->
Tract-Level Density and Topography<br>0 .2 .4 .6 .8 1<br>Distance From CBD (%)<br>% flat land % developed land<br>.6<br>.5<br>.4<br>Fitted values<br>.3<br>.2<br><!-- End of picture text -->

**Figure 2:** CBD Distance Patterns in Supply Elasticities Across All Tracts 



<!-- Start of picture text -->
Unit Supply Elasticity (RS) Quality Supply Elasticity (RS)<br>0 .2 .4 .6 .8 1 0 .2 .4 .6 .8 1<br>pct_dis pct_dis<br>gamma gamma1 (fix density and topography)<br>gamma2 (fix density only) gamma3 (fix topography only)<br>1.5 2.7<br>2.6<br>1<br>2.5<br>Fitted values Fitted values<br>.5<br>2.4<br>0 2.3<br><!-- End of picture text -->

64 

**Figure 3:** CBD Distance Patterns in Selected MSAs 



<!-- Start of picture text -->
Los Angeles New York Madison Pittsburgh<br>0 .2 .4 pct_dis .6 .8 1 0 .2 .4 pct_dis .6 .8 1 0 .2 .4 pct_dis .6 .8 1 0 .2 .4 pct_dis .6 .8 1<br>Los Angeles New York Madison Pittsburgh<br>0 .2 .4 pct_dis .6 .8 1 0 .2 .4 pct_dis .6 .8 1 0 .2 .4 pct_dis .6 .8 1 0 .2 .4 pct_dis .6 .8 1<br>gamma gamma1 (fix density and topography)<br>gamma2  (fix density only) gamma3 (fix topography only)<br>1.5 1.5 1.5 1.5<br>Unit Supply Elasticity (RS) 1.5 Unit Supply Elasticity (RS) 1.5 Unit Supply Elasticity (RS) 1.5 Unit Supply Elasticity (RS) 1.5<br>0 0 0 0<br>2.7 2.7 2.8 2.8<br>2.6<br>2.6 2.5 2.7 2.7<br>2.5 2.4 2.6<br>Quality Supply Elasticity (RS) Quality Supply Elasticity (RS) Quality Supply Elasticity (RS) Quality Supply Elasticity (RS) 2.6<br>2.4 2.3 2.5<br>2.3 2.2 2.4 2.5<br><!-- End of picture text -->

65 

## **A Model Appendix** 

The fraction of residents of tract _i_ that work in _j Pr_ ( _viωPBi_<sup>1</sup><sup>_−_</sup> _iz_<sup>_β_</sup> _ijek_<sup>_κτ_</sup> _ω_<sup>_ij_</sup> _wjk >_ = max _j′_ , _k′ viωPBi_<sup>1</sup> _iz_<sup>_−_</sup> _i_<sup>_β_</sup> _<u>j′ekκτ′</u> ωijw′_ _<u>j′</u> k′_ ) can be determined using the properties of the Frechet draws _zijkω_ . 



We write this expression as a function of resident market access _RMAi ≡_ ∑ _k_ ∑ _j_ � _wjke_<sup>_−κτij_�</sup><sup>_ε_</sup> , which is a summary measure of the access to employment opportunities from residential neighborhood _i_ . 

Before the productivity shock is revealed, the expected income (wage net of commuting cost) _<u>yi</u>_ associated with residing in tract _i_ is _E_ (max _j_ , _k wjek_<sup>_<u>κτ</u>_</sup> _zi_<sup>_ij_</sup> _<u>jkω</u>_<sup>).Solving this through,</sup> 



Not surprisingly, this object is increasing in _RMAi_ and declining in _ε_ . As _ε_ increases, there is a smaller dispersion in skill prices across locations, reducing the probability of individuals receiving high wage offers in any location. 

The probability that _i_ is the highest utility residential location is the probability that the inclusive value of municipality m is the highest times the probability that neighborhood i is the highest utility neighborhood in municipality m. Using properties of the Frechet distribution, this _η η_ _<u>φ</u>_ <u>�</u> _Bi Pi_<sup>_β−_1</sup> _<u>yi</u>_ <u>�</u> ∑ _i_ ´ _∈m_ ( _i_ )� _Bi′ Pi_<sup>_β′−_1</sup> _<u>yi′</u>_ <u>�</u> ] _<u>η</u>_ second object is ∑ _i′_ <u>�</u> _Pi_<sup>_β′−_1</sup> _Bi′_ _<u>yi′</u>_ <u>�</u> _<u>η</u>_ . The second object is ∑ _m_ [∑ _i_ ´ _∈m_ ( _i_ )� _Bi′ Pi_<sup>_β′−_1</sup> _<u>yi′</u>_ <u>�</u> _η_ ] _<u>φη</u>_ ] Plugging in for _<u>yi</u>_ gives the population supply function in the text.. 

The probability that _j_ is the highest utility work location for a resident of any given tract i is _πij|i_ = ∑ _k_ <u>�</u> _wjke_<sup>_−κτij_</sup><sup><u>�</u></sup><sup>_ε_. Summing over the probability of living in</sup><sup>_i_, we recover the labor supply to</sup> ∑ _k_ ∑ _j′_ <u>�</u> _wj′ ke_<sup>_−κτij_</sup><sup><u>�</u></sup><sup>_<u>ε</u>_</sup> tract j in the text. 

66 

**Table 14:** Analysis of Pre-Treatment Trends 

||∆Censu|s Hedon|ic Index 19|90-2000|
|---|---|---|---|---|
|∆ln Sim. RMA, 2000-2006|0.360|0.277|-0.294|-0.361|
||(0.448)|(0.431)|(0.585)|(0.565)|
|Observations|31,263|31,263|31,263|31,263|
|R-Squared|0.003|0.083|0.002|0.073|
||∆ln H|ouse Qu|antity, 199|0-2000|
|∆ln Sim. RMA, 2000-2006|3.117***|-0.109|2.402***|-0.679**|
||(0.720)|(0.248)|(0.916)|(0.334)|
|Observations|31,124|31,124|31,124|31,124|
|R-Squared|0.093|0.893|0.037|0.872|
|Region All FE|275|275|||
|Region-Ring FE|||3,235|3,235|
|Demographic Controls|No|Yes|No|Yes|



67 

