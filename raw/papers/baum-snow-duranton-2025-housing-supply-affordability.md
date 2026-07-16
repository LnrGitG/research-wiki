---
source_url: /tmp/w33694.pdf
ingested: 2026-07-16
sha256: 7d68b5e83e5639c0
---

NBER WORKING PAPER SERIES 

HOUSING SUPPLY AND HOUSING AFFORDABILITY 

Nathaniel Baum-Snow Gilles Duranton 

Working Paper 33694 http://www.nber.org/papers/w33694 

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 April 2025 

This work is supported by the Zell Lurie Center for Real Estate. It was in large part conducted while the second author visited CEMFI as part of the Maria de Maeztu Visitors Program. Their generous hospitality is gratefully acknowledged. The views expressed herein are those of the authors and do not necessarily reflect the views of the National Bureau of Economic Research. 

NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications. 

© 2025 by Nathaniel Baum-Snow and Gilles Duranton. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source. 

Housing Supply and Housing Affordability Nathaniel Baum-Snow and Gilles Duranton NBER Working Paper No. 33694 April 2025 JEL No. R31, R38 

## **<u>ABSTRACT</u>** 

The decline in housing affordability over recent decades has promoted an enhanced interest in housing supply. This chapter presents descriptive evidence about the evolution of us housing prices, quantities, and regulations since 1980, indicating that supply constraints appear to be increasingly binding. We then provide an overview of the various approaches used to model construction and land development for homogeneous and heterogeneous housing in static and dynamic contexts to understand housing supply. Our treatment incorporates empirical implementation and policy implications throughout. Finally, we provide an overview of quantitative evidence on the consequences of relaxing various types of supply constraints. 

Nathaniel Baum-Snow Rotman School of Management University of Toronto 105 St George St Toronto ON M5S 3E6 Canada nate.baum.snow@rotman.utoronto.ca 

Gilles Duranton University of Pennsylvania and NBER duranton@wharton.upenn.edu 

# **1. Introduction** 

Since 2000, housing costs have increased more rapidly than household incomes across the us and in many other countries around the world. Indeed, housing affordability is one of the great policy challenges of our time. A widely proposed remedy for improving housing affordability is to expand housing supply. Doing so effectively requires finding ways to reduce the costs of developing new housing and/or of maintaining existing housing. While there is little controversy about the link from reduced construction and maintenance costs to improved housing affordability, little is known about how to achieve this. Possible remedies include making more land available for development, reducing the costs of materials and labor, improving productivity in housing construction, and lowering regulatory limits. There is little consensus on which supply-side policies are most effective. Moreover, the targeting of different supply margins may have different distributional implications. 

Developing a policy consensus requires an understanding of both some key facts and the various that be the data these facts. This processes may generating underlying chapter endeavors to provide both. We thus start with an overview of relevant facts about various housing markets in the us. We present information on housing prices and quantities for four broad market We also demonstrate the evolution of land use definitions. regulation and the density of housing development as a function of location within cities. 

We then turn to various modeling approaches that have been used to rationalize these facts. We begin with a neoclassical treatment of housing construction, in which developers combine land and capital into units of housing services. We demonstrate how this static framework can be adapted to estimate the production function for units of housing services conditional on construction and recover the associated housing supply elasticities at the intensive margin. We also consider the role of tall buildings in housing supply and the challenge of stagnant or declining productivity in the construction sector. 

The static neoclassical framework is then extended in various directions, one at a time. We start with dynamic housing supply and real options, an active area of frontier research. We then turn to assignment models, in which new housing supply serves only select segments of the housing market in a commodity hierarchy. This leads to a natural process of newer units of higher quality inhabited by higher-income households filtering down the income distribution over time. The introduction of demand and housing unit heterogeneity naturally leads to a discussion of various externalities from new housing construction, including through the reduction of blight and the changing composition of neighborhood residents. Such externalities potentially justify roles for policy, among which we consider inclusionary zoning and spatially targeted development subsidies. 

We then review land development constraints, including topography and land use restrictions. Increasingly restrictive land use regulations and declines in available land for development in good locations have resulted in sharply declining housing supply elasticities 

1 

over time. The study of land use regulations faces the dual challenges of developing coherent and parsimonious measures and estimating their consequences in a well-identified way from contexts with strong external validity. This has led to a recent wave of research using boundary discontinuity empirical designs for the identification of impacts of various types of land use restrictions on property values while separating the capitalization of “own-lot” real option values, “external” density effects, and aggregate “supply” effects into property values. We highlight the role of quantitative models in facilitating the analysis of large-scale land use restrictions like urban growth boundaries. 

Local jurisdictions typically determine land use regulations. In the us, these same jurisdictions also provide various local public services, including schools, parks, and police, levying property taxes to pay for them. We discuss how these joint decisions incentivize municipalities to enact exclusionary zoning, which limits negative fiscal externalities from owners of relatively low-value properties. Local jurisdictions use a variety of fiscal instruments taxation. We discuss the of transfer beyond property consequences property taxes, which disincentivize moving and are mostly capitalized into lower housing values. we consider the for the of of low-income Finally, consequences supply housing housing policies, including tax credits for subsidized housing development, housing vouchers, and rent control. 

Finally, we review general equilibrium modeling frameworks that articulate linkages across a system of housing markets and labor markets. Recent examples incorporate either within-region neighborhood and household heterogeneity or dynamics, urban growth, and endogenous land use regulation. Such models have been quantified to isolate the motivations driving incumbent landowners to enact land use regulations and the welfare consequences associated with reducing the stringency of these regulations. 

Central to these quantifications are three types of forces. The migration elasticity (alternatively viewed as the population supply elasticity) to each market is central for determining the cost and of in housing affordability consequences reducing regulation. Heterogeneity amenities across residential locations means that reducing regulation influences welfare by allowing more people to live in high-amenity locations. Finally, heterogeneity in productivity across work locations and the nature of agglomeration forces influence welfare through the determination of wages. Then, in some modeling frameworks, eliminating regulation also improves welfare by reducing commuting costs. On the other side, incumbent property owners have an incentive to regulate in order to maintain their property values since deregulation allows the amount of housing in the market to increase, thereby bidding down prices. 

This is not the to summarize the literature on chapter certainly first attempt housing supply. Our overview reprises some of the ideas and results in Arnott’s highly technical overview of the theory of housing markets in Volume 2 of this _Handbook_ (Arnott, 1987) that 

2 

have fallen out of recognition. We also reiterate some elements of Olsen’s institutions and policy-focused overview of housing empirics in the same volume (Olsen, 1987). Twenty-five years ago, Denise DiPasquale (1999) lamented about the lack of research on housing supply. Her call went unheeded for many years, and it is only recently that research output on the topic increased, perhaps because of the growing housing affordability challenge. The literature on land use regulations prior to 2015 is masterfully discussed in the previous volume of this _Handbook_ by Gyourko and Molloy (2015). We only repeat what is strictly necessary here and refer the reader back to this chapter for more details. We also deemphasize issues surrounding the location of housing within cities and the earlier literature on housing durability, which are both reviewed by Duranton and Puga (2015). Finally, related discussions of the facts we present here appear in Molloy (2020) and Baum-Snow (2023). 

As housing affordability is of such policy concern, we find it important to incorporate considerations of various policy instruments that may influence housing supply and affordability. We distribute such discussions throughout the chapter as they relate to the substantive issues under review. In section 3, we consider the consequences of maximum floor area ratios, local building codes and permitting regimes, and unionization in the construction industry. In section 4, we consider potential justifications for subsidized housing construction aimed at low-income tenants, inclusionary zoning, and coordinated subsidies for neighborhood economic development. In section 5, we consider rent control, tax policy, and land use regulation, a topic to which we return in our review of quantitative general equilibrium approaches in section 6. Our policy discussions are meant to illustrate the substantive issues we review. They are not meant to be exhaustive, nor do we aim to cover “housing policy” in any systematic way. 

# **2. Facts** 

We begin by establishing a set of facts about housing affordability, housing costs, and housing quantities in the us since 1980, the first year with comprehensive microgeographic coverage in the Census. These facts motivate our review of the conceptual frameworks used to analyze housing supply and housing markets in the remaining sections. Undoubtedly, has been construction costs and stricter land use housing affordability declining. Rising regulations have resulted in lower rates of new construction, particularly in the most of the constraints and the increased of prosperous parts country. Geographical scarcity large tracts of undeveloped land in desirable locations also contribute to a weaker supply. While new constructions of larger units on smaller parcels are a crucial component of the supply of housing, it is not the only one. With fewer constructions, better maintenance and renovations are playing an increasingly important role in the supply of housing. We 

3 

also highlight that despite weaker demographic growth, the demand for housing remains strong due to smaller households, greater incomes, and possibly more work from home and demand for home offices. 

We present facts for four different types of locations. While these areas are probably too large for each to form a distinct housing market, our goal is to group locations with similar market conditions. We look separately at data for (i) small cities and rural areas, (ii) suburban areas, (iii) urban areas, and (iv) “superstar cities”.<sup>1</sup> 

To define these types of locations, we begin with the 2020 definition of Core Based Statistical Areas (cbsas) and the 2000 definition of central cities for these cbsas. “Small and Rural Counties” are all counties, either not part of a cbsa (2000 population: 18 million) or in the 846 cbsas with a central city with fewer 100,000 inhabitants in 2000 (2000 population: 89 million). “Suburbs” are the regions of the 81 cbsas with a central city of more than 100,000 that are outside of this central city (2000 population: 125 million). We assign the corresponding primary central city areas to “Central Cities” (2000 population: 49 million). Among Central Cities, we identify as “Superstar Cities” (Gyourko, Mayer, and Sinai, 2013) those with at least a 200,000 dollar gap between price and construction cost at their urban fringe following Duranton and Puga (2023). These superstar cities are New York, San Francisco, Washington, Boston, Seattle, and San Diego (2000 population: 15 million).<sup>2</sup> 

Of these four broad classes of locations, each has a unique profile of housing demand, built-up density, and regulatory environment. Small and Rural Counties have experienced the weakest demand growth, have the most land available for development, and have the laxest regulatory environment. Suburban areas have faced the most robust demand growth and still have some land available for development, but also have portions with the most restrictive regulatory environments. Central cities generally have only moderate demand but their densities make new construction more growth, high existing housing costly. Finally, superstar cities have a combination of high demand growth, high construction costs, and strong restrictions on land development. It is not surprising that these are the locations with the most rapid increases in housing costs and unaffordability. 

To put our facts in context, we first lay out a conceptual environment to ensure we understand our notations and measures of prices and quantities. 

## **_2.1 Measuring housing prices and quantities_** 

Conceptually, we would like to measure housing services _Hj_ , an index of observed and unobserved attributes. Housing services are what consumers consume and this index 

> 1Considering alternative geographies, including dividing the us into large regions, is also insightful. Due to length limits, we cannot look into other forms of heterogeneity here. However, our code and data are posted in this volume’s archive. Our code can be easily amended to consider alternative spatial groupings. 

> 2In short: Small and Rural Counties, Suburbs, Central Cities partition the country, while Superstar Cities are a subset of Central Cities. 

4 

constitutes a broad and convenient measure of the quantity of housing supplied to a market _j_ in each period. The flow of housing services from dwelling _i_ in market _j_ is _hij_ , and the average flow of housing services per dwelling in market _j_ is _hj_ . Aggregating yields _Hj_ = ∑ _i∈j hij_ = _Njhj_ , where _Nj_ is the number of dwellings in the market.<sup>3</sup> 

Aggregating housing services at the dwelling level to the market level is only informative about the total supply of housing under stringent conditions. It requires that the unit price of housing services, _Pj_ , be uniform across dwellings. Although dwellings may differ in size and quality, they must all offer housing services viewed as homogeneous among residents. As a result, dwellings vary only in the quantity of housing services they provide. Moreover, this aggregation should also be free from problems caused by the mainly indivisible nature of housing. Housing units may not be sensibly aggregated if they are too heterogeneous within a market area. Instead, it may be preferable to separately examine differentiated market segments for some questions (e.g., apartments versus single-family homes). 

In practice, data limitations abound. We usually have records for sales prices and only a few characteristics of dwellings, including the number of bedrooms in most data sets and floorspace in some data sets. The price of dwellings reflects the discounted sum of the value of future housing services, _Pjthijt_ , the product of the quantity of housing services and their unit price. Given these caveats, it is unclear how well the total number of dwellings or total floorspace in _j_ captures the supply of housing _Hj_ in this location, even after adjustment with a measure of observed quality. 

As the economic environment changes over time in _j_ (or elsewhere), for example following increases in population or income on the demand side, prices of housing services _Pj_ increase. In turn, higher prices lead to changes in the stock of housing. We can decompose changes in the housing stock into four sources: (i) new dwellings built on previously undeveloped land (“new developments”), (ii) new dwellings built on previously developed land (“redevelopment”), (iii) existing dwellings that fully depreciate or entirely disappear (“teardowns”), and (iv) existing dwellings that decay or are renovated (“renovations”). The first three forces are about changes in the number of dwelling units, and the last is about changes in the quality of dwelling units. Overall, the quantity of housing services in location _j_ changes by _∆Hj_ . Understanding ‘housing supply’ is about understanding how _∆Hj_ responds to changes in economic conditions and the channels through which these adjustments occur. This section aims to provide some evidence about the evolution of housing prices and quantities without wedding ourselves to particular processes that generate the data. 

> 3We note that under some conditions, it is more convenient to express housing quantities as a vector of attributes rather than as a single index. One can view _hij_ as the aggregation of such an underlying vector for dwelling _i_ in market _j_ . The weights used to aggregate up to the index of housing services would typically be estimated using hedonic analysis. 

5 

## **_2.2 Housing prices_** 

Figure 1 establishes our central motivating fact: housing affordability in the us has been since 2000 in all of locations for both renters and home with some declining types buyers, differences between types of location in the timing and magnitude of this decline. To show this, we present plots of average self-reported home values, gross rents, and household incomes in each location type for the 1980-2022 period. These quantities are calculated using household microdata from the 1980-2020 decennial censuses and the 2005-2022 annual American Community Surveys (acs, Ruggles _et al._ , 2024). Gross rents and home values are different measures of _Pjhj_ , which additionally capitalize an expected future stream of (usually implicit) rents. These self-reported values are perhaps subject to biases from homeowner ignorance about the state of the housing market. 

Each plot in figure 1 is indexed to 100 in Small and Rural Areas in 2000. We selected Small and Rural Counties as the reference location because this is where we see the lowest levels and growth rates of rents and home values, which, in turn, result from relatively weak demand growth and lax supply conditions. However, even in these areas, affordability declines after 2000. While average rents increased at an annualized rate of 5.0% between 2000 and 2022, nominal household incomes increased at an annualized rate of only 3.5%. The difference between these two is a rental that increased on figures “affordability gap” average by 1.5 percentage points per year (1.3 percentage points to 2018 before covid). Despite much greater volatility, home values increased at an annual rate of 6.9% between 2000 and 2022, leading to a growth in affordability gaps for home values close to or greater than those for rents. 

The story here is not just about lagging income growth. The growth of the consumer price index (cpi-u) in the economy was, on average, 3.2% per year, and the growth rate of income for rural households was similar to that of suburban incomes. Instead, the price of housing went in Small and Rural Counties between 2000 and 2022. These reverse the up patterns affordability increases that we observe for the 1980-2000 period when rental affordability gaps declined by two percentage points per year and value gaps declined by 0.5 percentage points per year in Small and Rural Counties. 

These same also exist in the other three of locations that we qualitative patterns types study. In 2000, Suburbs started with household incomes, gross rents, and home values that were 37%, 41%, and 59% higher than in Small and Rural Counties. However, after 2000, these prices grew at very similar rates as in rural areas, except during the covid-19 pandemic, when home values grew more rapidly in rural areas. The resulting growth in affordability gaps for Suburbs is very similar to that of Small and Rural Counties. However, the greater volatility in suburban home values is notable, perhaps reflecting lower housing supply elasticities (Davidoff, 2013). As incomes grew faster in suburbs during the 1980-2000 

6 

**Figure 1:** Housing affordability 



<!-- Start of picture text -->
Small and Rural Counties Suburbs<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>Central Cities Superstar Cities<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>value rent household income<br>400 400<br>300 300<br>200 200<br>100 100<br>0 0<br>400<br>700<br>300<br>500<br>200<br>300<br>100<br>100<br>0 0<br><!-- End of picture text -->

_Notes_ : This figure depicts descriptive evidence on self-reported nominal average log home values, log rents, and log household incomes for each indicated region over time. Plots are calculated using household level data from the 1980, 1990 and 2000 decennial censuses and the 2005-2022 acs. County Groups in 1980 and Public Use Microdata Areas in other years are mapped to county and central city geographies using year 2000 population allocation factors. These allocation factors are constructed through spatial joins of 2000 census tract geographies. All values are indexed to 100 in Small and Rural Counties (top left panel) in 2000. 

period, they experienced more rapidly declining home value-based affordability gaps than did rural areas in this period. 

Central cities have larger shares of income spent on housing than do other regions, especially Superstar Cities. In 2000, incomes were 6% higher in central cities than in rural areas, but rents were 22% higher and self-reported home values 25% higher. In Superstar Cities, 2000 rents and home values were 42% and 141% higher than in rural areas. While the growth in the rental affordability gaps in Central Cities over 2000-2022 is similar to those in other regions, home value gaps increased faster, especially in Superstar Cities. In these locations, the affordability gap for home values increased by 5.3 percentage points per year from 2000 to 2018 (3.9 percentage points per year from 2000 to 2022). Like in other regions, this is a reversal of the rental affordability gains of the 1980-2000 period. 

To confirm our findings from figure 1 regarding the ubiquitous increases in house values and rents, figure 2 shows the Federal Home Finance Agency home price index, which is a 

7 

**Figure 2:** Indexed housing costs, homes prices, and rents 



<!-- Start of picture text -->
Small and Rural Counties Suburbs<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>Central Cities Superstar Cities<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>FHFA price index rent index construction cost index CPI-U mid-year<br>300 300<br>200 200<br>100 100<br>0 0<br>300 400<br>300<br>200<br>200<br>100<br>100<br>0 0<br><!-- End of picture text -->

_Notes_ : This figure depicts the average census tract level Federal Housing Finance Agency price index, zip code level Zillow Observed Rent Index, municipality level RSMeans Construction Cost Index for a typical single-family home, and national Consumer Price Index (cpi-u). 

repeat sales index for single-family homes with prime mortgages, aggregated from census tracts.<sup>4</sup> Since 1980, the evolution of this measure of indexed housing prices, arguably a measure of _Pj_ , closely mirrors that of self-reported home values used in figure 1, a measure of _Pjhj_ . Since self-reported home values could reflect an increase in dwelling quality, this similarity between the two implies that the decline in observed affordability is driven primarily by prices, _Pj_ , and not by changes in the composition of the housing stock, _hj_ . 

As a measure of indexed rents, with regrettably limited time coverage, we use the Zillow Observed Rent Index, a ZIP-Code level repeat listed rent index that started in 2010.<sup>5</sup> The 1. evolution of this index generally confirms our findings using self-reported rents in figure 

The affordability burden is generally growing less rapidly for renters. Rents consistently 

> 4For areas with the same coverage, the Federal Home Finance Agency and Case-Schiller house price indexes are very similar. 

> 5This index is constructed using almost the same methodology as Ambrose, Coulson, and Yoshida’s (2015) repeat rent index calculated for a limited set of markets. 

8 

have lower growth rates and volatility than home values. With the us homeownership rate stable at 63%-68% since 1980, facilitating more renting may be one fruitful avenue to improve housing affordability. Forward-looking models, as in Molloy, Nathanson, and Paciorek (2022), can justify more rapid price than rent growth in supply-constrained regions like Superstar Cities, as rents are expected to grow only after housing supply constraints become even more binding. 

## **_2.3 Construction costs_** 

To measure construction costs, we use the municipality-level RSMeans Construction Cost Index, which measures the cost of building a typical single-family home, excluding land and permitting costs. Hence, the differences between the Federal Home Finance Agency and RSMeans indices reflect, at least in part, land acquisition and regulatory costs. The national cpi-u is also graphed as a basis for comparison in figure 2. 

Higher construction costs in Suburbs and Superstar Cities have existed since at least 1980. The main feature of figure 2 is that construction costs rose at about the same rate as the cpi-u until 2005 when they started growing about twice as fast in all four types of locations. Hence, the increase in construction costs is an essential part of the explanation of the patterns in Figure 1 since the cost of structures represents 60% of us house values on average in 2019 (Davis, Larson, Oliner, and Shui, 2021). 

To compare construction costs and house prices, we distinguish three periods. Between 1980 and 2000, construction costs increased at about the same pace as housing prices, or slightly less in Suburbs. As with affordability, we observe a first divergence between 2000 and 2018. The annualized growth in construction costs was 2.8 percentage points higher than the growth in housing prices in rural areas, 1.1 percentage points higher in suburbs, 0.4 percentage point higher in Central Cities, and 2.1 percentage points lower in Superstar Cities. However, these gaps closed or reversed after the onset of the covid-19 pandemic following rapid growth in housing prices in all locations except Superstar Cities. Overall and acknowledging some complications associated with their cyclical behavior, housing prices have increased at about the same pace as construction costs in Small and Rural Counties, slightly faster than construction costs in Suburbs and Central Cities, and much faster in Superstar Cities. 

Taken together, we find that land availability is a key source of supply constraints in the most expensive locations, such as Superstar Cities. In other locations, the increase in housing prices is driven chiefly by rising construction costs. This conclusion is, of course, consistent with the fact that in the most expensive locations, land represents a large share of the value of housing. 

9 

## **_2.4 Accounting for changes in housing supply_** 

Before exploring the evidence on quantities of housing supplied, we propose notations for the components of supply that we explore below. In the data, we observe measures of the stock of developed land in _j_ , _Lj_ , the stock of floorspace, _Sj_ , and the number of dwellings, _N_ . _j_ We focus on occupied dwellings so as to avoid overstating the housing stock to include units that are not habitable or in transition between occupants. Total housing is equal to the of services unit of land _h ≡_<sup>_Hj_bytheamountof</sup> average quantity housing per _j Lj_<sup>multiplied</sup> developed land _Lj_ . In turn, _hj_ can be decomposed further into housing services per unit of floorspace, _zj ≡_<sup>_H_</sup> _Sj_<sup>_<u>j</u>_(typicallyunobserved)timesaveragefloorspaceperdwelling</sup><sup>_mj≡_</sup> _N_<sup>_Sj_</sup> _j_ (typically observed). Also relevant is the average parcel size _lj ≡ N_<sup>_Lj_</sup> _j_<sup>(typicallyobserved).</sup> Using these objects, we can decompose the housing stock in three convenient ways: 





Equation (1) distinguishes between the intensity of development per unit of land and the extensive margin of land development. Equation (2) shows how dwelling units contribute to overall housing supply. Equation (3) shows how land and parcel size contribute. Taking natural logarithms and time differencing equations (1)-(3) leads to 



Equations (6) states that the growth of the housing stock sums up the (mostly unobserved) growth in housing quality (leading to more units of housing services per unit of floorspace), the growth of dwelling size minus the growth in parcel size, and the growth of developed land. The last two terms decompose the total growth in dwellings shown in equation (5). Renovations and possibly new constructions, when they are of higher quality, increase housing quality _zj_ , while depreciation reduces it. Newly built housing and the redevelopment _m_ . and renovation of existing dwellings affect floorspace per dwelling, _j_ New developments and redevelopments that impact the number of units in a parcel change the average size of the parcels. Finally, new developments also increase the stock of developed land. Equations (5) and (6) inform our next three empirical exercises. 

10 

In section 3, we will be interested in understanding both intensive and extensive margin factors driving the supply of housing services _Hj_ .<sup>6</sup> Equation (4) shows that the stock of housing services grows both at the intensive margin, through the growth in housing quality and size, and at the extensive margin, through the growth of developed land. Then, it follows that 



The elasticity of housing services to housing price sums the corresponding elasticities of housing quality at the intensive margin and land development at the extensive margin. 

## **_2. 5 Housing quantities: New constructions and depreciation_** 

We begin our empirical exploration of housing quantities with equation (5) by looking at the evolution of occupied housing units _Nj_ over time in different types of locations before turning to the evolution of other components of housing supply. 

The stock of housing units changes due to the full depreciation of dwellings (teardowns) and new construction _W_ . _jt_ 



which, after log differencing, can be written as, 



That is, the growth rate in the number of dwellings, “units growth”, is approximately the construction rate _w_ =<sup>_Wjt_thedwellingunitsdepreciationrate</sup><sup>_δjt_.Weemphasize</sup> _jt Njt_<sup>minus</sup> that for the purpose of our descriptive analysis, this is an equilibrium dwelling unit depreciation rate that incorporates the possibility that endogenous maintenance can keep dwellings in the housing stock longer. 

To measure trends in housing quantities, construction, and depreciation rates, we undertake a cohort analysis. We separately follow occupied dwellings that existed in the stock in 1980, 1990, 2000, or 2010.<sup>7</sup> Figure 3 reports the evolution of the stock of dwellings into each subsequent decade, which facilitates the joint visualization of changes in the overall stock due to depreciation and new construction. Our measure of depreciation is crude, as we can only measure it through tear-downs. 

These data are constructed using decennial censuses and aggregate census tract data for 2008-12 and 2018-22 acs, which are further aggregated into our four location types. To give 

> 6As _Hj_ is unobserved, researchers often use floorspace _Sj_ as a proxy. Even the stock of floorspace is empirically hard to obtain, as seen in section 2. We often need to work with an even cruder proxy: the number of dwellings. 

> 7We exclude vacant dwellings from calculations. The national vacancy rates were 9% in 1980, 11% in 1990, 12% in 2000, 14% in 2010, and 11% in 2020, indicating a tightening of the housing market in the 2010-2020 period (us Census Bureau, Current Population Survey/Housing Vacancy Survey). 

11 

**Figure 3:** Housing quantities and depreciation rates 



<!-- Start of picture text -->
Small and Rural Counties Suburbs<br>  annualized   annualized<br>  popu l at i on growth :   0.8%   popu l at i on growth :  1.8%<br>  net units growth: 1.3%   net units growth: 2%<br>  depreciation:  0.7%   depreciation: 0.4%<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>Central Cities Superstar Cities<br>  annualized   annualized<br>  popu l at i on growth :  0.5%   popu l at i on growth :   0.7%<br>  net units growth: 0.7%   net units growth: 0.6%<br>  depreciation: 0.5%   depreciation:  0.2%<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>built pre-1980 built pre-1990 built pre-2000 built pre-2010 built pre-2020 population<br>120 120<br>100 100<br>80<br>80<br>60<br>60<br>120 120<br>100 100<br>80 80<br>60 60<br><!-- End of picture text -->

_Notes_ : Downward sloping lines depict the number of housing units in the stock built prior to the indicated year that remain in the stock in the year on the horizontal axis. Stocks are measured using 100% count decadal census data. The upward sloping line is total population. All plots are indexed to the total housing stock or population in year 2000, which are assigned value 100. 

a sense of demand conditions, we also report trends in aggregate populations. Therefore, by comparing trends in population and occupied housing units, trends in household sizes can also be inferred from the graph. The stocks of dwellings and populations are separately indexed to 100 in 2000 in each panel of figure 3 for the same four types of locations shown in figures 1 and 2. 

During the 1980-2000 period, units growth, _∆_ log _Njt_ , equaled or exceeded population growth in all types of location, except Superstar Cities. In Small and Rural Counties, where land supply is the most elastic, the annualized unit growth of 1.3% exceeded population growth throughout the 1980-2020 period by 0.5 percentage points per year. 

In Suburbs, which experienced much greater demand growth, units growth surpassed population growth by just 0.2 percentage points per year. Since 2000, these two growth rates have been nearly identical. We also note that these two growth rates were also markedly lower during the 2010-2020 period (see Baum-Snow, 2023, for more details). In Suburbs, as 

12 

elsewhere, rising construction costs and increasingly stringent land use regulations imply that the growth in the demand for housing is increasingly accommodated through rising home prices rather than increased quantities of dwellings. 

Central Cities experienced weaker population growth that was also slightly outpaced by units growth by 0.2 percentage points per year, with a relatively high rate of units growth in 2010-2020 at 0.9% annualized, relative to 0.7% for the entire 1980-2020 period. 

In Superstar Cities, population growth exceeded units growth during the 1980-2000 period.<sup>8</sup> After 2000, units growth increased slightly in Superstar Cities to just offset population growth. Units growth has been declining in Suburbs and increasing in Central Cities in recent decades. However, these growth rates remain much lower in Central Cities, which also have a lower base stock of dwelling units. As a result, the vast majority of new dwellings are still built in suburban areas. 

One way to cope with high demand and inelastic supply of new dwellings is to keep existing units in the housing stock longer (Baum-Snow and Han, 2024). In Small and Rural Counties, where construction is relatively easy, figure 3 shows approximately parallel downward-sloping lines for depreciation for all cohorts over all decades. In a typical year, 0.7% of the dwelling units depreciate out of the stock in these locations.<sup>9</sup> Central cities also experienced relatively weak demand growth, manifested as average annualized population growth rates of only 0.5%. In this region, the depreciation rate was slightly lower at 0.5% per year, but with a marked slowdown in 2010-2020. Similar patterns of depreciation are seen in the suburbs. In Superstar Cities, where the pressure on the housing market is the the rates 0.2% Relative to rural areas with a greatest, depreciation averaged only per year. depreciation rate of 0.7% per year, Superstar Cities get an extra 0.5 percentage point in units growth from lower depreciation, about the same magnitude as units growth. 

Together with the evidence on housing costs, figure 3 also strongly suggests that the decrease in average household size has put demand-side pressure on the housing market (Overman, Puga, and Turner, 2008). The housing stock has grown at a higher rate than the population, yet housing prices and rents continue to rise above the rate of inflation. 

## **_2.6 Changes in dwelling attributes_** 

Although there were no discernible differences between the evolution of dwelling values reported in figure 1 and that of the house price index reported in figure 2, suggesting little 

> 8The ratio of the cost of replacement to the price of housing is at or below one for the majority of housing units in Small and Rural Counties in 2000 (Glaeser and Gyourko, 2018). When replacement costs are higher than house values, it is difficult to justify high volumes of new construction at market rates. Central Cities had an equally low ratio of replacement cost to price. Suburbs and Superstar Cities had much higher ratios. 

> 9Reported depreciation rates are calculated by averaging over all percentage reductions in the total initial stock across the four decades indicated in the figure, weighting by the stock at the beginning of the decade. 

13 

**Figure 4:** Attributes of housing units 



<!-- Start of picture text -->
Small and Rural Counties Suburbs<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>Central Cities Superstar Cities<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>rooms bedrooms floorspace/unit (000 sqft) mean lot size (acres) median lot size (acres)<br>6 15 6 5<br>5 12 5 4<br>4 9 4 3<br>count area<br>3 6 3 2<br>2 3 2 1<br>1 0 1 0<br>6 1 6 1<br>5 .8 5 .8<br>4 .6 4 .6<br>count area<br>3 .4 3 .4<br>2 .2 2 .2<br>1 0 1 0<br><!-- End of picture text -->

_Notes_ : Average rooms and bedrooms are calculated using decennial censuses and 2005-2022 acs data. Mean floorspace per unit and lot size variables are calculated from census tract level data in the replication archive associated with Baum-Snow and Han (2024) (original source: Zillow ztrax). The sample includes all census tracts with a count of dwelling units in 2000 with information on floorsapce and lot size that is within 10% of the number of occupied housing units reported in the 2000 census. This tract restriction retains 16%, 28%, 25% and 21% of all tracts in Small and Rural Counties, Suburbs, Central Cities, and Superstar Cities, respectively. See Baum-Snow and Han (2024) for further discussion about sample constraints in the Zillow data. Median lot sizes are calculated as the median across tract average lot sizes in each year, weighted by the number of dwelling units in the tract. 

change in housing quality, the evolution of the composition of the housing stock deserves a more detailed look. 

Figure 4 plots the average number of rooms and bedrooms across dwelling units over time in each type of location. These two quantities are calculated from decennial censuses and the acs following the same methodology as above. We view the average number of rooms and bedrooms as imperfect measures of housing services per dwelling, _hj_ = _mj × sj_ . We also report average square footage _sj_ for the 1999 to 2016 period only. This is computed from the Zillow data assembled by Baum-Snow and Han (2024), after restricting the sample to only include census tracts with year 2000 Zillow counts of dwellings that are within 10% of the 2000 census 100 % count of occupied housing units and have information on floorspace 

14 

and lot size .<sup>10</sup> 

Figure 4 shows that in Small and Rural Counties and in Suburbs, where most new housing units have been built, the average number of rooms, bedrooms, and square footage have all increased over time. Despite demand pressures and rising housing prices, the quality of the typical housing unit has also increased slightly. This intensive margin component does contribute, albeit modestly, to the growth in overall housing supply. 

A possible implication of larger housing units and smaller households is a possible mismatch between the two, as housing units are mostly indivisible. In particular, a “missing middle” of smaller single-family homes, townhouses, and larger apartments for middle-income families may be emerging as new homes are built disproportionately for the high-income segment of the market. We return to these issues below. 

Figure 4 also reports the evolution of mean and median lot sizes across properties in each type of location. We report both of these statistics to accommodate some imperfections in the lot size information in assessment data sets, including Zillow’s ztrax. In low-density areas, some of which are in our “Suburbs” region, many residential lots also include a large amount of non-residential land, including that in agriculture or completely undeveloped. For this reason, the lot size distribution for rural areas has a long right tail. In urban areas, multifamily buildings typically report the lot size of the entire building for each individual dwelling, greatly overstating average land per dwelling unit. This will artificially increase mean lot size in cities. As such, we also report medians of lot size distributions. 

With these data limitations in mind, there remains useful information in the lot size distributions. While the size of housing units increased slightly, mean lot sizes _lj_ decreased rapidly between 1999 and 2016 in rural and suburban areas. This is from a mix of full abandonment of on rural lots and new on dwellings very large housing developments smaller, newly subdivided lots. This decline comes with the high net rates of new dwellings in these areas. Mean lot sizes in these areas remain nonetheless In Small and very large. Rural Counties, the average housing unit still sits on a 9.9-acre lot, down 1.2 acres since 1999, while the median unit sits on a slightly declining 0.9-acre lot. In Suburbs, the average lot is 2.4 acres, down almost 0.5 acres since 1999, but the median lot size is stable at 0.4 acres. Lot sizes in Central Cities are, of course, much smaller, with median lot sizes at 0.15 acres (and even smaller in Superstar Cities), with little discernible trend. The offsetting trends of bigger houses vs. smaller lots are consistent with the parallel evolutions of average dwelling prices and the house price index documented above. 

> 10While this restriction has little effect on reported floorspace levels and trends, it improves the clarity of results about lot sizes. 

15 

**Figure 5:** Density of housing units and land use regulations 



<!-- Start of picture text -->
All CBSAs Superstar CBSAs<br>0 .5 1 1.5 2 0 .5 1 1.5 2<br>distance to CBD distance to CBD<br>central cities: 1980 2000 2020 WRLURI 2006 WRLURI 2018<br>suburbs: 1980 2000 2020 WRLURI 2006 WRLURI 2018<br>6000 1.25 12000 1.25<br>4000 .75 8000 .75<br>WRLUR index<br>2000 .25 4000 .25<br>housing units per sq km<br>0 0<br>-.25 -.25<br><!-- End of picture text -->

_Notes_ : Census tract level data from 1980, 2000 and 2020 is used to calculate average housing units per squared kilometer by distance to cbd separately for tracts in central city and suburban portions of cbsas. Distance to cbd is indexed to be 1 for the central city census tract furthest from the cbd. Most cbsas extend beyond index value 2, where the graphs cut off. Triangles and circles indicate the average Wharton Residential Land Use Regulation Index (wrluri) for central city municipalities from 2006 and 2018, respectively. Remaining lines trace out averages in suburban municipalities as a function of indexed cbd distance. 

## **_2.7 Land use regulations and spatial patterns of housing development_** 

To end our exploration of the data, figure 5 plots the density of housing units as a function of the distance to the central business district (cbd) across all cbsas included in our Suburbs and Central Cities location types (left panel) and their Superstar Cities counterparts (right panel), again using tract-level data from decennial censuses and the acs. The figure represents housing unit density plots for 1980, 2000, and 2020, separately in central cities and suburbs. The index on the horizontal axis scales the distance to the cbd to be between 0 and 1 for all census tracts within central cities. We cut the graph off at a distance index equal to 2, as the suburban density lines exhibit no discernible pattern of additional interest beyond this point. 

Figure 5 also represents the profiles of the Wharton Residential Land Use Regulation Index (wrluri) of Gyourko, Saiz, and Summers (2008) and Gyourko, Hartley, and Krimmel (2021) for 2006 and 2018 on the right axis. This index, which aggregates many types of land use restrictions, covers most large municipalities and is discussed further in Section 5.2. These two vintage indices are independently standardized in each year, and are thus measured relative to a municipality with average regulation. Gyourko and Krimmel (2021) indicate that the average locale increased regulation between 2006 and 2018. We note that land use regulation tends to fall towards the periphery of cbsas, beyond the right edge of 

16 

## the figure. 

The declining rate of new housing construction in the suburbs seen in figure 3 is also evident in figure 5. The bottom line of the graph shows the density of suburban housing units in 1980. The next line up is its 2000 counterpart. The line above this is its 2020 counterpart, which is only slightly above the line for 2000, with a much bigger gap between 1980 and 2000. This reduction in the rate of growth of suburban density has coincided with increasingly stringent land use regulation in suburban jurisdictions, also represented on the graph (see also Gyourko and Krimmel, 2021). While lot sizes in suburban areas are declining, they are still very large and provide ample opportunities for further densification. However, land use regulations impede densification in many suburban jurisdictions. One common type of regulation receiving a lot of attention in the literature is minimum lot size zoning, which explicitly limits housing unit densities, often with an exclusionary motive. We return to this impediment to construction later. 

Since 2000, central cities have been more successful than suburban jurisdictions at facilitating densification. In the cbd distance range of 0.2-0.4, considerable densification occurred, especially over 2000-2020. As the amount of land in central cities is much smaller than in suburban areas, this increased city densification comes with fewer new dwelling units entering the aggregate city housing stock than entered the suburban housing stock through its small increases in unit density. We also note that the density of central cities exceeds that of suburbs at all distances in which they overlap, likely because this aspect of zoning rules in central cities is more lax, despite their overall increases in land use regulation, seen in figure 5 as the circles above the triangles. 

Finally, we note that Superstar cbsas are about twice as dense as all cbsas and have stricter regulations. One result in the housing supply literature is that demand growth tends to beget more stringent land use regulations. This has been articulated in an overlapping generations model of urban development with agglomeration economies and endogenous regulation (Duranton and Puga, 2023) and empirically verified (Baum-Snow and Han, 2024). The reason is that regulations against densification make the housing supply less elastic. Then, demand growth is more strongly capitalized into housing values and thus benefits existing homeowners. Overall, there remains a lot of opportunity for increased densification. With housing unit densities roughly three times higher in central cities than in the next ring of suburbs, we see many well-functioning neighborhoods with high densities of dwelling units. 

# **. The economics of construction 3** 

In this section, we review the state of the literature on the production function for real estate. This treatment speaks primarily to the intensive margin of housing supply, the amount built 

17 

conditional on development. We leave treatments of redevelopment and new developments for later sections. 

Equation (7) above states that the elasticity of housing services with respect to housing price sums the “building elasticity” _ϵ_<sup>_h_</sup> _P_<sup>(</sup><sup>_t_)attheintensivemarginwiththe“landdevel-</sup> opment elasticity” _ϵ_<sup>_L_</sup> _P_<sup>(</sup><sup>_t_)attheextensivemargin.</sup> Generically, we can interpret both as “long-run” elasticities, as if each market area gets rebuilt from scratch in each long-run time period. These elasticities can be most naturally thought of in terms of cross-sectional comparisons of construction stocks and density of development across markets, given price differences. For example, if markets A and B both have _ϵ_<sup>_h_</sup> _P_<sup>(</sup><sup>_t_)=2and</sup><sup>_ϵL_</sup> _P_<sup>(</sup><sup>_t_)=0.5and</sup> _PA_ = 1.1 _PB_ , then each housing development in market _A_ will provide 20% more housing services than in _B_ , holding the amount of developed land fixed, and market A will also have 5% more land developed than _B_ . This results in 25% more housing services produced in market _A_ than in _B_ overall. We also want to make these elasticities a function of the initial time period _t_ to capture the fact that changes in technology and regulation can result in long-run elasticities that change over time. For example, as market _A_ is gradually built up, its development elasticity may fall from _ϵ_<sup>_L_</sup> _P_<sup>(</sup><sup>_t_) = 0.5 initially to zero when it is fully built</sup> up. 

While long-run housing supply elasticities are important, we often wish to measure the total of the stock to in over a of supply responses housing changes housing prices period time, be it a year or a decade. Hence, the estimation of shorter-run housing elasticities will depend on both when they are estimated and over what length of time. Furthermore, the building elasticity, as measured over a specific time period, requires incorporating the rate of the initial stock into the calculation. Markets with the same redevelopment housing amount of redevelopment but higher initial stocks will mechanically have lower building elasticities.<sup>11</sup> 

Putting this all together, we have that the intensive margin elasticity as measured between periods _t_ and _t_<sup>_′_</sup> equals the long-run elasticity for the period times the rate of redevelopment _R_ ( _t_ , _t_<sup>_′_</sup> _|_ **P** ). This rate is defined as the fraction of initial housing services that are redeveloped, which is typically the same as the fraction of initially developed land that is redeveloped. This redevelopment probability also depends on the price vector **P** from period _t_ into the future. Adding up, 



In this expression, we maintain the short-run land development elasticity _ϵ_<sup>_L_</sup> _P_<sup>(</sup><sup>_t_,</sup><sup>_t′_) as distinct</sup> from its long-run counterpart _ϵ_<sup>_L_</sup> _P_<sup>(</sup><sup>_t_) to account for land development frictions that may take</sup> 

> 11The vintage of the initial building stock also affects the building elasticity since redevelopment typically results in larger per-dwelling upgrades for older properties (Brueckner and Rosenthal, 2009). We return to this below. 

18 

time to resolve or for the behavior of profit-maximizing builders waiting for the optimal time to redevelop. 

We note some ambiguity in the notation of the elasticities _ϵ_<sup>_h_</sup> _P_<sup>and</sup><sup>_ϵL_</sup> _P_<sup>inequation(10)</sup> for two reasons. First, arguably, the entire sequence of current and future housing prices should matter for development decisions. We return to these issues in section 4, where we take a fully dynamic approach. Second, in general, these elasticities additionally depend on market _j_ , or more precisely, on market-specific factors that shape land availability. We return to these issues in section 5. We study the building elasticity in the rest of this section on construction. 

## **_.1 3 Modeling housing development_** 

We follow Muth’s (1969 and 1975) pioneering work and much of the literature, including Combes, Duranton, and Gobillon (2021) and Baum-Snow and Han (2024), from whom this exposition borrows. We view housing development as the result of a profit maximization problem by a competitive builder facing free entry. A housing production function or, its dual, a cost function for construction is at the core of this approach. This housing production function turns construction inputs, capital, labor, and land into housing. For simplicity, we lump together construction material (capital) and labor (which gets frozen into capital by the construction process) and only retain capital and land as factors of production. Housing is then produced according to the function _h_ ( _k_ , _l_ ), which we assume increases in both arguments and is strictly quasi-concave. 

The profit of the builder of dwelling _i_ is, 



where _rj_ is the price of capital in _j_ , _qj_ ( _li_ ) is the price of a parcel of size _li_ , and _cij_ is a fixed cost of housing development for the parcel over which dwelling _i_ sits. This fixed cost captures the physical cost of preparing a parcel for construction and all the regulatory taxes and fees needed to obtain a building permit (Glaeser and Gyourko, 2018, Duranton and Puga, 2023). 

Housing development occurs in three stages. First, parcels are delineated. Second, the builder decides whether to pay the fixed cost _cij_ to develop or redevelop a parcel. Third, the builder chooses how much capital to invest. We take the size of parcels as given for now.<sup>12</sup> In practice, parcel size is often predetermined (except for large subdivisions). The assembly 

> 12Builders in our setting resemble neoclassical firms, but some differences are worth noting. Parcel size (the land input) is typically assumed to be fixed from the perspective of individual builders. This leads to decreasing returns to scale and a naturally competitive market for real estate development, where the rents are dissipated into land prices. Because parcel size is exogenously given and the fact that builders only hold land parcels temporarily to develop and then sell housing, the role of the land input is quite different from that of the capital input in the neoclassical theory of the firm. 

19 

and reorganization of the land are notoriously challenging (Brooks and Lutz, 2016). The size of the parcels is also highly regulated, as discussed in Section 5.<sup>13</sup> 

Starting with the choice of capital investment, the builder’s first-order condition for profit maximization is: 



This implicit equation uniquely determines the optimal capital investment _ki_ given the concavity of _h_ ( _·_ , _·_ ). Then, free entry implies that the profit from construction is dissipated into the price of the parcel, 



where _αi ≡_<sup>_∂_lo</sup> _∂_<sup><u>g</u></sup> log<sup>_h_</sup><sup><u>(</u></sup><sup>_k_</sup> _k_<sup>_<u>i</u>_</sup> _i_<sup><u>,</u></sup><sup>_li_</sup><sup><u>)</u></sup> is the elasticity of housing production with respect to capital. The last equality is obtained after substituting for _rj_ using the first-order condition (12) and simplifying. 

Some comments are in order. First, a limitation of this approach is that it only considers the production of housing (services), and it is silent about how constructions are divided across different dwellings. 

Second, because the price of parcels is generally bounded from below by their next best use _<u>q</u>_<sup>landdevelopmentoccursonlyforparcelswithfixedcostsbelowathreshold</sup><sup>_cij≤_</sup> _~~j~~_<sup>_li_,</sup> _<u>cij</u> ≡_ (1 _− αi_ ) _Pjh_ ( _ki_ , _li_ ) _−_ _<u>q</u>_<sup>More parcels are then developed as housing prices increase or</sup> _~~j~~_<sup>_li_.</sup> the production technology improves. The distribution of fixed development costs, including regulatory costs, is central to determining housing development patterns at the extensive margin. At the intensive margin, applying the implicit function theorem to equation (12) also implies that higher prices lead to more capital investment, _∂Pj∂ki_<sup>_>_0,andthusmore</sup> intensive housing development<sup>_∂h_</sup> _∂Pj_<sup><u>(</u></sup><sup>_ki_</sup><sup><u>,</u></sup><sup>_li_</sup><sup><u>)</u></sup> _>_ 0. 

Third, although it is convenient to model land use restrictions as part of the fixed cost of building a dwelling, the regulation of housing development may have implications beyond this fixed cost. For instance, regulations often limit capital investment or certain forms of capital investment, such as building height or the maximum footprint per unit of land. Such 

> 13There are further complications associated with endogenous parcel size. When builders can choose the size of parcels in addition to capital to maximize profit, we can appeal to standard results from producer theory. If housing is produced with decreasing returns to scale, optimal lot size results from a trade-off between the decreasing returns to housing production on each parcel and its fixed cost of development. As we approach constant returns for all factors, the optimal size of parcels grows to infinity. Since, in practice, the production of single-family homes appears to be at or close to constant returns, this outcome seems implausible. A first resolution to this apparent contradiction is to appeal to the indivisible nature of housing. A huge house on a huge parcel is not a perfect substitute for ten smaller houses built on the same parcel. However, considering this feature would greatly complicate our modeling framework, and we reserve further discussion of it for later. A second possibility is that the returns to land are first increasing (it is hard to build on a tiny lot) and then decreasing (the tenth acre of a property likely provides little housing services). In a competitive equilibrium, builders operate at the point of constant returns. 

20 

constraints affect optimal capital investment in equation (12) and lead to more complex distortions when different forms of capital investment are available (Combes _et al._ , 2021). 

As a side note, it is also instructive, and as shown below in some cases useful, to consider the dual of the producer problem above and the variable cost function _Cj_ ( _hi_ ) for parcel _i_ in location _j_ . With fixed parcel size, the first-order condition for profit maximization and the chain rule imply that the marginal cost is given by<sup>d</sup><sup>_C_</sup> d<sup>_<u>j</u>_</sup> _h_<sup><u>(</u></sup><sup>_h_</sup><sup><u>)</u></sup> = _rj_ /<sup>_∂h_</sup> _∂k_<sup><u>(</u></sup><sup>_k_</sup><sup><u>,</u></sup><sup>_li_</sup><sup><u>)</u></sup> . In turn, after inserting this expression into the first-order condition (12) and using the resulting expression to substitute for _Pj_ into the zero profit condition, we find that the price of parcels in equation (13) can equivalently be written as, 



After accounting for the fixed development cost _cij_ , the fraction of total variable construction cost _Cj_ ( _hi_ ) capitalized into the price of land parcels is increasing in the convexity of the cost function, which itself is increasing in the intensity of land in production given the exogenous parcel size _li_ . Relative to equation (13), equation (14) is more general, as it accommodates multiple variable factors of production. 

## **_.2 3 Estimating housing production: Traditional approaches_** 

The simplest production function for housing to consider is the following Cobb-Douglas aggregation of land and capital, 



where _Bj_ is the total factor productivity of builders in location _j_ . 

Before going deeper into estimating this production function and to understand what is at stake with this estimation, note that with exogenous parcel sizes and this production function, following Baum-Snow and Han (2024), the housing supply function of parcel _i_ can be written as 



In turn, this expression can be aggregated across developed parcels within market _j_ to get 



Hence, conditional on building, the elasticity of housing production relative to housing prices is _ϵ_<sup>_h_</sup> _P_<sup>_≡_</sup> _∂_<sup>_∂_</sup> log<sup>log</sup> _P_<sup>_h_=</sup> 1 _−αα_<sup>atboththeparcelandthemarketlevels.Thisisalsotruefor</sup> the overall economy. This technological parameter estimated at the “micro” level is thus indicative of a “macro” elasticity of interest. 

After taking logs in equation (15), we note that the production function for housing could be estimated on and land: potentially by regressing log housing log capital log 

21 

log _hij_ = _α_ log _ki_ + _β_ log _li_ + log _Bj_ . Unfortunately, this regression cannot be estimated directly since units of housing services are not observed. Units of capital are also often not observed separately from their price. Instead, we can rely on the first-order condition for profit maximization above and estimate the following regression: 



where we add an idiosyncratic error term _ϵi_ , perhaps reflecting some mismeasurement of the dependent variable since a perfect fit is unlikely to occur. This error term could also reflect some unobserved heterogeneity in construction costs across parcels. This regression is estimated a cross-section of houses. It can also be estimated for a cross- naturally using section of cities or neighborhoods.<sup>14</sup> 

Estimating the regression described by equation (18) is challenging regardless of the spatial scale. Productivity _Bj_ is not observed and is treated as a residual. This generates a well-understood simultaneity problem. When the idiosyncratic error term _ϵi_ reflects parcel-specific construction costs, a builder who observes this term will adjust their choice of input accordingly. A related issue is that efficiency units of housing cannot be observed separately from their price in the dependent variable. Thus, any demand shock affecting _Pj_ is expected to be reflected in the choice of inputs. See Ackerberg, Benkard, Berry, and Pakes (2007) and Syverson (2011) for further discussion of this general problem that plagues the estimation of nearly all production functions. 

Land values are also difficult to observe. Separate transactions for residential land parcels are rarely observed. There are two exceptions. Thorsnes (1997) observes land values for large undeveloped parcels purchased by home builders. These parcels are then subdivided and developed before being sold to incoming residents. Combes _et al._ (2021) use data from France, where a standard arrangement between home builders and buyers of new homes is for the future resident to buy land before contracting with the builder to construct a house paid in several installments. This arrangement is fiscally advantageous for the buyer who minimizes taxes on real estate transaction, while gradual payment helps the builder finance construction. 

Land values can also be computed using land market transaction data from providers such as the CoStar Group. Because only transactions above a certain threshold are recorded, these transactions are spatially selected toward the urban fringe where large land parcels are available or toward trophy locations where land is the most valuable. The transactions may 

> 14Alternatively, the cost share parameters can also be calibrated as part of a larger model as in Albouy (2009) who finds a land share of 0.23, a capital share of 0.15, and a labor share of 0.62. The main pitfall of this type of exercise is that it relies on a model that makes many more assumptions, including functional form assumptions, than the simple framework proposed above requires. In addition, such calibrations often rely on available aggregate figures that may not coincide with the concepts used in the model. See also Muth (1975) for further discussion. 

22 

also select a specific type of house. Large parcels are generally subdivided before construction. New constructions in large new subdivisions are only a fraction of all constructions, perhaps a small one in some countries (Combes _et al._ , 2021). Finally, these transactions are rare, raising sampling issues in small cities. To limit these problems, Haughwout, Orr, and Bedoll (2008), Albouy, Ehrlich, and Shin (2018), and Davis _et al._ (2021) implement regression approaches to correct for the characteristics of the parcels, most notably for their location.<sup>15</sup> Using the resulting predicted land value as an explanatory variable to estimate a regression such as equation (18) like Albouy and Ehrlich (2018) is potentially problematic because the implicit smoothing of the data can introduce classical measurement error in the regression and lead to coefficients biased toward zero. 

Following Clapp (1979) and many others, the rest of the literature relies on appraised land values. Appraised land values are likely noisy and subject to various biases. For example, appraisers may compute land values by taking the difference between their estimated value of dwellings and the replacement cost of the structures before applying a discount to avoid disputes with the owners since these appraised values often form the property tax base. 

A major shortcoming of equation (18) is that it imposes a unit elasticity of substitution between land and capital. This need not be the case, and the economic cost of regulations that push toward either high or low density depends crucially on the value of this elasticity. Rather than attempting to estimate a Cobb-Douglas functional form, much of the literature has focused instead on constant-elasticity-of-substitution (ces) production functions: 



where _σ_ is the elasticity of substitution between land and capital, _υ_ is a factor share parameter, and _Bj_ remains a productivity shifter. Applying the ces functional form to the first-order condition for profit maximization in equation (12) and substituting the zero-profit conditions yields: 



after taking logs and simplifying. Assuming a constant cost of capital ( _rj_ = _r_ ) and some measurement error on the dependent variable, the previous equation leads to log � _<u>rklii</u>_ � = _C_ + _σ_ log<sup>_<u>q</u>_</sup> _li_<sup>_<u>i</u>_+</sup><sup>_ϵi_, where</sup><sup>_C_is a constellation of parameters.</sup> 

> 15There are important differences between these approaches. Albouy _et al._ (2018) estimate a ‘monocentric cone’ for each city with two key parameters: the price at the center and a distance gradient. Davis _et al._ (2021) rely instead on a ‘Kriging’ procedure where the prediction relies on the available information from the nearest neighbors. The former approach is perhaps more appropriate for city-level predictions, while the latter is likely to perform better for smaller spatial units such as ZIP Codes. It is also possible to predict the price of land as the difference between the value of a dwelling and the estimated cost of reconstructing the existing structure. Although this is a reasonable approach to generate aggregate land values (Davis and Palumbo, 2008), it would be problematic to introduce it into the regression derived from equation (18) as it would bias the estimation through a mechanical correlation between the value of a house and the value of its land. 

23 

This regression of the log of the capital-to-land ratio on the unit price of land has been estimated many times in the literature, with a review by McDonald as early as 1981. Ahlfeldt and McMillen (2013) and Combes _et al._ (2021) provide more recent estimates. The range for the estimates of the elasticity of substitution between land and other inputs, when estimating some version of equation (20), is extremely wide, from less than 0.1 in Muth (1964) to slightly above one in McDonald (1979), with a mean perhaps around 0.5. 

Sample heterogeneity is a first possible explanation for these differences in the estimated elasticity of substitution between land and capital. First, residential and commercial properties will likely differ in how they are built. There is also significant heterogeneity within each broad class: single-family houses differ greatly from large multifamily buildings within residential real estate; office towers require construction techniques different from big-box retail stores within commercial real estate, etc. Construction technologies also likely differ between countries (Yoshida, 2016). But even when they focus on us residential samples where single-family homes are likely to dominate, Ahlfeldt and McMillen (2013) estimate an elasticity of substitution between land and capital of 0.95 in Allegheny County pa with one data set and of 0.43 and 0.60 for two other data sets in Chicago. 

These differences may also be symptomatic of data measurement issues for the price of land. In the older literature, Thorsnes (1997), who used arguably better quality data than previously, estimates elasticities around 0.9, toward the upper end of the range. In Monte-Carlo simulations using synthetic data, Ahlfeldt and McMillen (2013) show that the estimation of equation (19) is sensitive to adding noise to the data. Even a moderate amount of mismeasurement for the price of land leads them to recover estimates of less than half the elasticity of substitution they used to generate the data. Combes _et al._ (2021) also show that when they estimate equation (19) after smoothing their land price data, the estimated elasticity of substitution about doubles from 0.49 to 0.99. 

Another possibility is that even accurate land price data may be ‘overly noisy’. Parcel prices may reflect a range of phenomena extraneous to how equation (19) is derived. Variations in the price of land may occur because some sellers may be in a hurry to sell, because some buyers and sellers lie about the actual amount of the transaction to evade taxes, or because buyers and sellers of land parcels in different locations may hold different expectations about future rents, etc. Put differently, the data-generating process may be richer than the simple model used here (and in most of the literature). As a result, equation (19) may be misspecified, and naive estimates of _σ_ in the regression corresponding to equation (19) will be biased downward. 

Unobserved construction costs at the parcel level are also likely to bias the estimated elasticity of substitution downward. More challenging parcels for builders require additional capital investments and, as a result, face lower land prices to retain zero profit. More generally, using land prices as an explanatory variable in equation (20) is problematic given 

24 

that the zero-profit condition (11) treats the price of the parcels as an outcome of the building process. 

Another potential difficulty is that a ces functional form may not capture the complexities of the production of housing. Albouy and Ehrlich (2018) propose estimating an even more cost function. us construction on flexible translog They regress metropolitan prices construction costs, land prices, various terms of higher order imposed by the translog specification, and geographical and regulatory constraints measures. They instrument land prices and construction costs with local amenities and estimated productivity for tradable goods under the assumptions that (i) they affect the demand for housing and (ii) are otherwise uncorrelated unobserved characteristics. While the condition about the supply first power of the instruments can be tested, the exclusion restriction may be more questionable. For example, natural amenities such as hills that make a location more attractive to residents could be correlated with unobserved housing productivity. However, the main limitation of the exercise is the size of the sample of metropolitan areas relative to the number of parameters to be estimated. This lack of power leads to imprecise estimates for the elasticity of substitution computed by Albouy and Ehrlich (2018).<sup>16</sup> 

## **_3.3 Estimating housing production: More recent work_** 

Following Epple, Gordon, and Sieg (2010) and Combes _et al._ (2021), more recent work has focused on developing new ways to separate prices from quantities to avoid biases arising from unobserved demand shocks when estimating the production function of housing. 

We follow the exposition of Combes _et al._ (2021) and build on the builder’s profit maximization approach derived above.<sup>17</sup> The key is to note that the first-order condition in equation (12) and the free-entry condition in equation (13) both contain the price of housing and its the cost of for now and the same quantity. Ignoring fixed development assuming cost of capital everywhere, it is possible to insert the zero-profit condition (13) into the first-order condition (12) to eliminate the price of housing _Pj_ . This yields the following partial differential equation: 



after simplification. Equation (21) shows that the elasticity of housing with respect to capital investment for a dwelling is equal to its share of capital in the total construction cost. All these quantities are measured at the private optimum of the builder, and we note the price of the land _q_ ( _ki_ , _li_ ) to reflect this. In French construction costs data, the price of land and 

> 16The coefficients on the role of land use regulation and geographic limits are much more precisely estimated. We return to them below. 

> 17The approach of Epple _et al._ (2010) is essentially the dual of that of Combes _et al._ (2021) and, empirically, it relies on different but equivalent observables. Combes _et al._ (2021) provide a detailed comparison of the two approaches within a unified framework. 

25 

capital investment are observed separately. Hence, the cost share on the right-hand side of equation (21) is readily measured. For any parcel of size _li_ , we can then compute the quantity of housing offered by dwelling _i_ by integrating equation (21) over _k_ : 



where _Z_ ( _li_ ) is an integration constant for parcels of size _li_ , and _<u>k</u>_ is the lowest level of capital investment observed in the data. In equation (22), housing production is calculated as the sum of marginal products. After a log transformation, the term to integrate is a simple cost share that is observed in the data. Then, after recovering _h_ non-parametrically, it is possible to estimate how _k_ into _h_ . This is a of the maps partial identification housing production function.<sup>18</sup> 

By construction, this approach removes any simultaneity between capital and housing production, working through the price of housing. However, some identification concerns remain. The most important of these regards factor heterogeneity, in particular the heterogeneity of land parcels. 

The estimation of the quantity of housing in equation (22) is based on the notion that builders want to more land with since more develop expensive greater capital intensity expensive land reflects higher housing prices. Although Combes, Duranton, and Gobillon (2019) provide evidence of a strong link between the price of housing and the price of land, land parcels also differ in how costly they are to develop due to, for example, their slope, how easy they are to excavate, any landscaping needed to avoid stormwater runoffs, etc. All else being equal, more difficult terrain will result in greater capital expenditure to build a given dwelling and a lower parcel price to satisfy the zero-profit condition. 

To address this problem, Combes _et al._ (2021) use residualized values for _k_ , _q_ , and _l_ , where these quantities are predicted only from variables that affect the demand for housing, but, arguably, not the unobserved development costs of parcels.<sup>19</sup> These demand predictors of parcel prices include the city’s population size and the distance to the center, conditionally on other local characteristics that may reflect unobserved supply conditions. 

The main findings of Combes _et al._ (2021) are an elasticity of housing production with respect to capital of 0.65 with little variation across house sizes. Consistent with this stability, estimate an of substitution between and land close to one. they elasticity capital Although they econometrically reject a Cobb-Douglas functional form (and more flexible ces and 

> 18Full identification is possible after duplicating the same approach to the first-order condition for land. Due to the zero-profit assumption, constant returns in housing production need to be assumed. Combes _et al._ (2021) econometrically reject constant returns in housing production, although in a way that is not economically meaningful. More importantly, in their data, most new constructions appear to be infills with severe constraints on dividing parcels. Taking parcels as given is arguably more appropriate than assuming some form of optimization in their delineation. 

> 19This last condition is an exclusion restriction. This approach to identification is in the same spirit as standard instrumental variables, but adapted to the specific case of equation (22). 

26 

translog forms), Cobb-Douglas provides a good first approximation. The main heterogeneity in their results is a lower capital elasticity in larger cities (0.54 in Paris vs. 0.71 in the smallest cities). After discarding several possible explanations, Combes _et al._ (2021) conclude that these differences are caused by expectations of stronger rent growth in larger cities combined with the opportunity to redevelop housing in the future. 

Importantly, as shown above, the elasticity of housing production relative to housing prices is _ϵ_<sup>_h_</sup> _P_<sup>=</sup> 1 _−αα_<sup>with a Cobb-Douglas production function.Hence, an elasticity of housing</sup> _α ≈_ production with respect to capital 0.65 implies a supply elasticity at the intensive margin <u>0.65</u> of _ϵ_<sup>_h_</sup> _P_<sup>=</sup> 1 _−_ 0.65<sup>_≈_1.86 or around two.</sup> 

## **_3.4 Estimating housing production: Tall buildings_** 

The literature on housing production mainly focuses on recovering the mix of land and capital chosen by profit-maximizing developers to build single-family houses. This framework works well to understand the intensive margin of housing supply in recently developed residential neighborhoods in the us and, to some extent, Europe. It is also appropriate for the redevelopment of single-family houses. However, it is less obvious that it carries over seamlessly to tall buildings. 

The cumulative height of buildings taller than 55 meters in cities across the world is above 16,000 kilometers. This is equivalent to 42,000 times the Empire State Building. About one third of this stock is in the developing world, and about 90% of it was built after 1980. Tall buildings make up over 10% of total building volumes in cities with a population larger than one million (Ahlfeldt, Baum-Snow, and Jedwab, 2023). 

Thus, any analysis of aggregate housing supply in large cities requires a conceptual framework that can accommodate tall structures. To model tall buildings, it is helpful to focus directly on the choice of building height _g_ by builders since data on building heights and volumes are readily available for the entire world on a consistent basis (Esch, Deininger, Jedwab, and Palacios-Lopez, 2024). This focus on building height is also useful when the of land use such as limits and analyzing consequences ubiquitous regulations height maximum floor-to-area ratios (fars). While we consider the implications of far restrictions in the following sub-section, we delay a broader discussion of land use regulation to section 5. 

Since the height of a building is roughly proportional to floorspace and housing services per land area, the ideas developed in section 3.2 above carry over to the analysis of tall buildings. For example, with Cobb-Douglas production for parcel _i_ in location _j_ and a common fixed parcel size of _li_ as in equation (15), the variable cost function for housing services is, 



27 

Then, the elasticity of the unit cost of housing, _C_ ( _h_ )/ _h_ , with respect to the amount of housing built is _θ ≡_<sup><u>1</u></sup><sup>_−_</sup> _α_<sup>_<u>α</u>_,theinverseofthesupplyelasticitygivenzeroprofit.Withheight</sup> given by _g ≡ h_ / _l_ , the unit cost elasticity with respect to _h_ , _θ_ , is also the elasticity of unit costs with respect to height. _θ >_ 0 captures the idea that structural engineering, material, elevator, and building foundation costs are collectively convex in building height. Relative to that on single-family houses, the tall buildings literature thinks about making the same model more off this baseline the cost of to across flexible by allowing elasticity height vary locations and height, and in considering the consequences of regulations that limit building heights. 

Cost data indicates that, while in general, costs are convex in height, there are regions of local increasing returns. Using data from RSMeans for apartment buildings in 50 us cities, Eriksen and Orlando (2022) trace the cost function for height. They find a declining marginal cost before discontinuous cost increases at 4 and 8 stories in buildings up to 12 stories tall. In addition, the marginal cost declines monotonically with floorplate size conditional on building height. For very tall buildings, the engineering evidence is that the “cost of height” elasticity _θ_ is increasing in height. 

Ahlfeldt and McMillen (2018) is the first study to explicitly estimate _θ_ using building level data on construction costs and heights. In the spirit of the Cobb-Douglas production function in equation (15), _θ_ can be estimated by regressing the log ratio of capital to floorspace on the log of building height. Identification requires variation in heights that are driven by demand-side forces rather than by unobserved location-specific cost differences. For example, one may worry that building heights reflect in part unobserved regulatory burdens and thus cannot be taken as unrelated to developers’ profit-maximizing choices of inputs and output. Measured construction costs per floorspace _k_ / _h_ could be lower in less regulated places that also have greater heights, thereby biasing estimates of the cost of height _θ_ downwards. 

Ahlfeldt and McMillen (2018) use microdata from Chicago on tall buildings from _Emporis_ (now integrated into CoStar products) to measure building height _g_ , construction cost _k_ , and real estate services _h_ (proxied by floorspace) for most tall buildings in Chicago over its history. Distance to the central business district is the demand side shifter used to generate variation in building height. This instrumentation strategy exploits insights from classical land use theory (Alonso, 1964, Muth, 1969, Mills, 1969) and its central result that better to the cbd into land values and more accessibility gets capitalized higher capital-intensive construction through demand side forces. Ultimately, Ahlfeldt and McMillen (2018) finds estimates of _θ_ of 0.54 for commercial buildings and 0.61 for residential buildings of 20 floors. These values imply estimates of _α_ for tall buildings of about 0.63, very similar to the capital 

28 

share of 0.65 found in Combes _et al._ (2021) for single-family homes.<sup>20</sup> 

An essential feature of the construction of tall buildings is that the cost of building higher varies between locations mainly due to the depth of the bedrock, as discussed in length in Barr (2016) in the context of New York City. Bedrock that is too close to the surface requires costly blasting to establish foundations for tall buildings. Bedrock that is too deep requires costly engineering for the foundations to be stable.<sup>21</sup> These features of the construction technology suggest a U-shaped relationship between _θ_ and the depth of the bedrock. 

Exploiting this insight, Ahlfeldt _et al._ (2023) specify a variable cost function for height per unit of land of the form 



This cost function is derived from a Cobb-Douglas production function in land and capital with exogenous parcel sizes as in equation (15). It assumes constant returns and that the ratio of floorspace to building height is constant but allows the share of capital to vary between parcels. The specification of equation (24) is built to focus on how the cost elasticity of height, _θi_ , varies with the depth of the bedrock. After taking logs for a chosen height _gi_ , this equation implies log( _Ci_ / _gi_ ) = _θi_ log _gi_ + log _νi_ , which can be estimated as a regression of cost of unit of on interacted with log building per floorspace log building height flexibly bedrock depth. In turn, _θi_ can be recovered as a function of bedrock depth. 

Using data from _Emporis_ for about 1,000 individual buildings taller than 55 meters, Ahlfeldt _et al._ (2023) estimate instrumental variables locally weighted regressions, smoothing across bedrock depths.<sup>22</sup> As with Ahlfeldt and McMillen (2018), distance to the cbd instruments for building height. The resulting estimates of _θ_ range from 0.2 at about a 17-meter bedrock depth to 0.8 at depths of both 0 and 30 meters.<sup>23</sup> These cost elasticities imply intensive margin supply elasticities _ϵ_<sup>_h_</sup> _P_<sup>of between 1.25 and 5.</sup> 

> 20More broadly, Ahlfeldt and McMillen (2018) explore a ces technology in capital and land, in which, in addition to _θ_ , they propose a parameter that defines the elasticity of the ratio of lot size to building footprint with respect to height: d lod logg( _l_ <u>/</u> _gf_ <u>)</u> _≡ λ_ , which they estimate to be 0.16. This can be viewed as a source of over-identification, as together with the definition of _θ_ , a Cobb-Douglas technology in land and capital ( _σ_ = 1) <u>1</u> is implied. Then, the elasticity of building height with respect to the unit price of land is 1+ _θ−λ_<sup>.</sup> 

> 21Foundation stability is achieved through deeply bored piles that go all the way down to the bedrock, a “raft” floating in subsoil built below deep piles, or many small, very deeply bored piles that do not reach the bedrock. 

> 22A few earlier papers also use the idea that favorable bedrock depths are cost shifters for building heights and density. Rosenthal and Strange (2008) and Combes, Duranton, Gobillon, and Roux (2010) use the depth of the bedrock as a source of plausibly exogenous variation in urban density to estimate the strength of local and city-level agglomeration forces. 

> 23Most of the Emporis data with construction cost information is for steel construction buildings in the us. However, most of the new tall buildings built after 2010 are framed in concrete. As these buildings are heavier, concrete construction buildings typically require deeper foundations than steel-framed buildings of the same height. As a result, the optimal depth of the bedrock is probably a few meters deeper for most tall buildings built in recent years. 

29 

Profit maximization by tall building developers to choose optimal heights incorporates the fact that both commercial and residential rents rise with height off the ground. Danton and Himbert (2018) and Ben-Shahar, Deng, Solganik, Somerville, and Hongjia (2022) estimate elasticities of rent with respect to height of about 0.03 for residential buildings while Liu, Rosenthal, and Strange (2018) and Koster, van Ommeren, and Rietveld (2013) estimate about 0.07 for office buildings. Developers’ choices of optimal building heights depends on the interaction between the local cost elasticity of height, _θi_ , and local real estate demand or idiosyncratic construction costs _νi_ . Lower cost elasticities of height imply taller building height choices in locations with stronger demand conditions and/or lower idiosyncratic construction costs. 

For a large cross-section of world cities, Ahlfeldt _et al._ (2023) estimate the relationship between their aggregate stock of tall building and their population and built-up footprint. These estimates reflect how differences across cities in the cost of height _θ_ affect building height. Differences in supply conditions, which drive the cost of height, generate variation in the stock of tall buildings, and, in turn, the stock of tall buildings affects the built areas of cities and their ability to accommodate residents. Ahlfeldt _et al._ (2023) find that the effects of bedrock depth (or, equivalently, _θ_ ) on heights are of larger magnitudes in bigger cities where demand for floorspace is stronger. In turn, this variation can be used over the 1975-2015 period to infer an elasticity of average city population with respect to the stock of tall building heights of 0.13 across cities in the developing world. The analogous elasticity for built area is -0.16.<sup>24</sup> 

Ahlfeldt _et al._ (2023) use these reduced-form results and inferred city-specific gaps between actual and unconstrained heights to calibrate a monocentric land use model for each city worldwide. Model counterfactuals show that expanding real estate supply through relaxing existing building height limits improves renter welfare, largely by facilitating more compact cities, thereby reducing intra-city travel costs. 

## **_. 3 5 Building height restrictions_** 

The result Ahlfeldt _et al._ (2023) that tall buildings lead to more compact cities echoes earlier results in the small literature looking at the costs of restricting building height. In the context of a simple monocentric city, Bertaud and Brueckner (2005) were the first to formally prove that restrictions on the height of buildings lead to urban sprawl and higher commuting costs. Brueckner, Fu, Gu, and Zhang (2017) also demonstrate the empirical importance of mechanism in the welfare costs of floor area ratio (far) restrictions in Indian cities. 

> 24Similar estimates are found by combining simple comparisons of 1975-2015 changes in log population, built area, and aggregate heights among cities over 1 million on favorable relative to unfavorable bedrock depths. 

30 

The costs of building height restrictions can also be inferred from the difference between the price of floorspace and its marginal cost of construction. To see the logic, note that unconstrained developers build until the price of one unit of housing services is equal to its marginal cost: _Pj_ = _C_<sup>_′_</sup> ( _h_ ). If no more than _h_<sup>_max_</sup> _< h_ units of housing services can be built, the height constraint is binding and _Pj > C_<sup>_′_</sup> ( _h_<sup>_max_</sup> ). Therefore, _Pj_ / _C_<sup>_′_</sup> ( _h_<sup>_max_</sup> ) _−_ 1 _>_ 0 can be viewed as reflecting the “regulatory tax” rate associated with the constraint _h_<sup>_max_</sup> . 

In early work, Glaeser, Gyourko, and Saks (2005 _a_ ) use hedonic analysis to compare the price per square foot of real estate to its construction cost and estimate the associated regulatory tax, driven by height limits and other restrictions. For Manhattan, they find that the price of floorspace is about twice its marginal cost. Cheshire and Hilber (2008) find even larger numbers for office markets in British cities.<sup>25</sup> Ben-Moshe and Genesove (2024) use a related frontier approach to trace out the marginal cost curve for height absent regulation for apartment buildings in Israel. This marginal cost curve is the lower envelope in sales in the the distribution of all sales to these price-height space. Comparing prices marginal costs, this paper finds a mean regulatory tax of 48% of the price. 

The costs of building height restrictions can also be inferred from the capitalization of floorspace into land values. Following Brueckner _et al._ (2017), a constraint on far means that the profit-maximizing amount of capital employed is essentially capped at _k_<sup>_max_</sup> given an exogenous parcel size, _li_ . The marginal capitalization associated with an additional unit of capital after partially relaxing a binding far constraint is thus _Pj ∂h_ <u>(</u> _k∂k_<sup>_max_</sup> <u>,</u> _li_ <u>)</u> _− rj >_ 0, where _rj_ is the cost of capital in market _j_ . Importantly, the relaxation of far restrictions gets capitalized into land values with an elasticity that increases with the stringency of these restrictions, reflecting diminishing marginal returns to capital in the production of housing. The capitalization of less stringent far restrictions is also increasing in the land share, an observation also made by Tan, Wang, and Zhang (2020) in the context of a richer production technology that additionally allows for a quantity-quality trade-off in inputs producing housing services. 

This theory suggests that regressing log land value on log far reveals the stringency of the far restrictions. All else being equal, if relaxing the far results in large increases in land values, this means that developers value the extra density and expect to build taller to exploit it. Using the procedure described above and data on land sales in Chinese cities, Brueckner _et al._ (2017) find that, on average, far restrictions result in building heights that are 62% of the free market level, with wide variation across cities and even within Beijing.<sup>26</sup> Evidence in Cai, Wang, and Zhang (2017) that building above the legal far limits is common 

> 25The standard explanation for markups of price over marginal cost is market power. However, given that prices in most housing markets are determined by many small bilateral transactions, it seems unlikely that developers could exploit market power to that extent. 

> 26Brueckner and Singh (2020) carry out an analogous analysis using data from five large us cities and find that, among them, Chicago is the least height constrained. 

31 

in high-demand areas (albeit coming at additional costs to developers) corroborates this evidence of binding far restrictions in most Chinese cities. Peng (2023) reaches a similar conclusion for New York City. 

These empirical exercises face identification challenges. One can imagine unobservables that drive both the stringency of far restrictions and land values. For example, locations with higher real estate demand may be more likely to enact tighter far restrictions to maintain the character of the neighborhood. In this example, cost and regulation-driven estimates of _∂∂_ loglog far _<u>q</u>_<sup>wouldbeunderstatedbyasimpleolsregression.</sup> To address this challenge, Brueckner and Singh (2020) and Tan _et al._ (2020) include fixed effects for small neighborhoods, with the idea that demand conditions are approximately constant within them. Cai _et al._ (2017) uses model structure and data on observable demand shifters to hold demand conditions constant. 

An alternative approach to estimating the stringency of far regulations is to calculate the amount of bunching at the far limit _F_ . Assuming a smooth distribution of unregulated building heights around _F_ , Brueckner, Leather, and Zerecero (2024) uses a bunching estimator to recover the counterfactual distribution of building heights absent far restrictions in New York City. Assuming a Cobb-Douglas production technology with a capital share of 0.65, marginal costs around the associated kink in the cost function can be recovered. Brueckner _et al._ (2024) find that New York City statutory far restrictions are overcome at an additional marginal cost of floorspace of 11% for both _F_ = 2 and _F_ = 0.5. Eliminating all far restrictions would result in 10% more floorspace in the New York City housing stock affected by both _F_ = 2 and _F_ = 0.5, and 3-4% for intermediate _F_ , given recent demand conditions. 

In conclusion, the tall building component of housing supply can be reasonably analyzed using the same production technology as that of single-family homes, with a capital share of 0.65. Evidence in the literature using such a framework indicates that relaxing restrictions on building tall remains a promising vehicle through which to accommodate rising housing demand in the world’s largest cities. 

## **_3.6 The productivity problem in construction_** 

We now turn to understanding how productivity in the construction industry changes over time. To start with an example, the Empire State Building was the tallest building in New York City in 2012 when it was surpassed by One World Trade Center.<sup>27</sup> The Empire State Building, which replaced the Waldorf-Astoria Hotel after its closure in May 1929, saw construction start on March 17, 1930. It opened 410 days later, on May 1, 1931, at a cost of 

> 27Sources for this paragraph are `https://en.wikipedia.org/wiki/Empire_State_Building` , `https://en. wikipedia.org/wiki/One_World_Trade_Center` , and `https://data.bls.gov/cgi-bin/cpicalc.pl` for inflation adjustments, all consulted on August 8, 2024. 

32 

681 million dollars (2024 dollars). One World Trade Center, which is admittedly 100 meters taller and contains about 50% more floorspace than the Empire State Building, replaced the original World Trade Center after it was destroyed in the terrorist attacks of September 11, 2001. Construction for One World Trade Center began in April 2006. The building opened after 3,112 days on November 3, 2014, at a cost of 5.19 billion dollars. Put differently, building One World Trade Center took nearly eight times as long and cost about five times as much per square meter of floor area as building the Empire State Building. 

Although perhaps extreme, this contrast between the Empire State Building and One World Trade Center is not an isolated case. Perhaps unsurprisingly to the casual observer, construction sites today look similar to those in 1950. Starting with Stokes (1981), Allen (1985), and more recently Sveikauskas, Rowe, Mildenberger, Price, and Young (2016), Garcia and Molloy (2023), Goolsbee and Syverson (2023), and D’Amico, Glaeser, Gyourko, Kerr, and Ponzetto (2024), economists have been puzzled by the poor apparent productivity performance of the construction industry measured through a wide range of metrics. 

As summarized by Goolsbee and Syverson (2023) using data from the Bureau of Economic Analysis, an index of value added per worker between 1950 and 2020 increased by 290% in the us but decreased in the construction This mild decline for economy slightly industry. construction incorporates a strong increase between 1950 and 1970 followed by a staggering 40% decline since 1970. Although we only discuss evidence from the us, Goolsbee and Syverson (2023) show that other developed countries had a similar experience, though perhaps less extreme.<sup>28</sup> This poor productivity performance of the construction industry with a decrease in the value added per worker over time is not due to lack of investment or to deterioration in labor quality (Goolsbee and Syverson, 2023). Instead, it appears to be driven by total factor productivity. 

Computing changes in labor productivity in an industry producing heterogeneous and durable tied to land is There are several measurement reasons an goods difficult. why observed decrease in productivity might be spurious. First, to compute value-added in construction, the value of land must be taken out. Although the price of land has increased dramatically, its share in construction appears stable, as noted by Garcia and Molloy (2023). Second, Garcia and Molloy (2023), Goolsbee and Syverson (2023), and D’Amico _et al._ (2024) provide convincing evidence that this decline in productivity is not an artifact of failing to account for faster unobserved quality growth in the construction industry’s output relative to other industries since 1970. Similarly, there is no evidence of increased output mismeasurement, again relative to other industries since 1970. Although profit margins in the construction industry have increased, this increase has been modest, ruling out another source of possible bias in calculating productivity growth. 

> 28Brooks and Liscow (2023) and Mehrotra, Turner, and Uribe (2024) provide a diagnostic for the costs of providing infrastructure in the us that echoes many of the points we make here for housing. 

33 

To avoid of the associated with values over many complications comparing aggregate time, Goolsbee and Syverson (2023) use information on the number of physical units produced and the labor employed to produce them to directly measure the physical productivity of labor in the industry over time. In the same spirit, Garcia and Molloy (2023) and D’Amico _et al._ (2024) use longitudinal information about the cost of building houses from RSMeans, a data provider and consulting firm that collects comprehensive cost data by task (or set of tasks, including whole houses) and geography. Although physical productivity does not decline as sharply as nominal productivity, the construction industry remains a clear laggard. Overall, the dismal productivity performance of the construction industry is, for the most part, something real and not a statistical illusion. Stokes (1981) already reached a similar conclusion many years ago. 

Due to the size of the construction industry, its weak productivity performance has sizeable aggregate implications. Goolsbee and Syverson (2023) calculate that if labor productivity had grown by a modest 1% a year instead of declining by 1% a year since 1970, aggregate labor productivity (and to a large extent income per capita) would be about 10% higher today. Taking into account the linkages between industries in a general equilibrium framework, Foerster, Hornstein, Sarte, and Watson (2022) find that changes in the productivity of the construction industry between 1950 and 1980 account for a full point of lower annual gdp growth between these dates. 

Given this, it is crucial to understand the deeper causes of the poor productivity performance of the construction industry. Before diving deeper into this issue, looking at the variation in the cost of building in the us cross-section provides a useful first pass. Gyourko and Saiz (2006) exploit the richness of the RSMeans data by looking at the cost of construction per square foot for a standard 2,000 square-feet “economy quality” house across 140 us markets (cities). They first highlight substantial variation in construction costs between cities. In 2003, building in New York was 80% more expensive than building in the North Carolina markets of Raleigh, Charlotte, and Greensboro. Even when outliers are ignored, differences remain large, with an interquartile range of about 20% of the unit cost. When Gyourko and Saiz (2006) regress unit construction costs on the number of permits and controls, they estimate a tiny elasticity. All else being equal, places that build more do not experience higher building costs. This is consistent with a flat supply curve for housing and a very fragmented industry. Gyourko and Saiz (2006) report that the number of establishments in the construction industry is nearly proportional to population size, with one construction establishment for every 1,200 residents. Unsurprisingly, they also estimate a strong association between construction costs and local wages. 

Interestingly, Gyourko and Saiz (2006) also find a strong association between construction costs and the share of unionized construction workers. An interquartile range in unionization (22 percentage points) is associated with 11% higher construction costs, or more than 

34 

half the interquartile variation in unit construction costs. Finally, they uncover a statistically significant association with some measures of construction regulations. 

There is little doubt that, through building codes, city governments and construction unions promote inefficient and expensive work practices, mandate questionable improvements, and restrict cost savings. Building codes throughout the us also increase construction costs because they impose high compliance costs, including excessive fees, lead to administrative delays in construction, and entail extensive and expensive inspections. On the other hand, building codes are arguably needed, given the asymmetries of information between housebuilders and residents and the risks such asymmetries entail for residents and their neighbors. Assessing the costs and benefits of building codes is thus inherently challenging. In their reviews of the literature, Listokin and Hattis (2005) and Dumm, Sirmans, and Smersh (2011) conclude that excessive and inappropriate building codes raise housing costs by, perhaps, around 5%. 

While we note that more up-to-date and better-identified evidence on the effects of building codes is needed, these effects are apparently smaller than those uncovered by Gyourko and Saiz (2006). These findings need not be inconsistent as Gyourko and Saiz (2006) measure an overall effect associated with unionization, of which inefficient building codes may be just one of the manifestations.<sup>29</sup> In any case, even the effects estimated by Gyourko and Saiz (2006) are somewhat modest. While remedying the excesses of building codes and high labor costs caused by unionization would be worthwhile, such small effects do not explain much of the poor productivity performance of the construction industry. 

Perhaps more crucially, building codes may prevent innovations in building technologies from diffusing or even happening in the first place. Schmitz (2020) provides a detailed historical narrative that blames construction unions acting in conjunction with various levels of government for the failure of housing to “industrialize” with more housing being produced off-site. Although they are undoubtedly an obstacle, institutional blockages in the us are only one element among the production and standardization challenges faced by modular housing.<sup>30</sup> The industrialization of housing is also slow to develop in countries such as Sweden, which are welcoming of the technology. Sweden even actively supports modular housing because of long winters that impede construction and the availability of cheap timber (Bayliss and Bergin, 2020). Another limiting factor of the potential for modular housing is that the legacy stock of houses and buildings will likely remain mainly out of reach for such new technologies for many years. While a complete discussion of 

> 29While construction unions may push for make-work, a more benign interpretation may deserve consideration. Increasingly stringent construction codes, requiring, for instance, additional levels of insulation or resistance to fire for structures, increase construction costs. In a world of lower interest, more demanding specifications face lower user costs and might be economically justified. Mehrotra _et al._ (2024) propose a defense of this argument to explain the inflation of the cost of the development of new road infrastructure. 

> 30For example, incompatible standards leave builders liable to being held up by their suppliers. In turn, this possible hold-up makes the funding of modular construction projects harder and more expensive. 

35 

the mechanization and automation of construction is beyond our scope, we note that new construction technologies and materials also hold great promises for decarbonization, as they provide better insulation and rely less on concrete than standard construction technologies (see Fernandes Rocha, Oliveira Ferreira, Pimenta, and Bento Pereira, 2022, for a broad introduction). 

Even if the importance of unions and city governments in preventing the emergence of radically new forms of construction is debatable, building codes prevent the diffusion of incremental innovations. In their classic work, Oster and Quigley (1977) show that four such incremental innovations regarding the intensity of material usage, the use of cheaper materials, and material pre-assembly were less likely to be permitted in jurisdictions where unionization rates were higher, where the chief planner was less educated, and where construction firms were smaller. Consistent with these micro findings, Goolsbee and Syverson (2023) note that, while the construction industry invests slightly more than the rest of the economy, it invests extremely little in intellectual property capital, which includes research and development and software. Productivity is more likely to be embedded into this kind of capital than in standard equipment and structure. At the very least, this lack of investment in intellectual property is a symptom of a broader malaise. 

In a different explanation, D’Amico _et al._ (2024) highlight the effects of an interaction between societal change and the nature of construction projects. Unlike manufacturing facilities, construction sites are highly visible and immobile. A permit is also needed before construction can start. These features made construction sites prime targets of increased “citizen voice” (Brooks and Liscow, 2023, Glaeser, Gyourko, and Saks, 2005 _b_ ). Then, compliance and approval for a new construction are more manageable for smaller, highly customized, and less locally disruptive construction projects.<sup>31</sup> In turn, these projects are more likely to be developed by small construction firms. As in most industries, smaller firms are less productive and invest less in productivity growth. 

To support their argument, D’Amico _et al._ (2024) show that the construction industry remains remarkably fragmented relative to manufacturing. Although construction has experienced some consolidation since the Great Recession (Quintero, 2023), it pales in comparison to the consolidation of retail or even multifamily rentals (Calder-Wang and Kim, 2024). D’Amico _et al._ (2024) also show that the size of residential projects has declined, that small firms work disproportionately on small projects, that small firms are less productive in the construction industry just like in most other sectors, and that cities with stricter land-use regulations have smaller construction firms. Interestingly, infrastructure construction has followed a similar path. Brooks and Liscow (2023) provide complementary evidence for this industry, which is consistent with what we observe for residential real estate. 

> 31For large buildings in the office market, another possible strategy is instead to propose trophy buildings designed by famous architects, as underscored by Cheshire and Dericks (2020) in the case of Central London. 

36 

Several further conjectures can be envisioned to explain the weak productivity performance of the construction industry. First, rather than institutional factors, it may have been available land that became scarce and limited new constructions. The evidence in Duranton and Puga (2023) suggests that this is undoubtedly the case for a number of coastal metropolitan areas. More systematic evidence on land scarcity, including the lack of large parcels to develop new subdivisions, is greatly needed. Second, an increasing share of residential construction work is about maintaining legacy houses, expanding them in some cases, or tearing them down and rebuilding them. Although increasingly required, maintenance and redevelopment are likely to appear as less productive in the data. In this case, it is the observed productivity growth in the construction industry prior to 1970 when construction work took place mainly at the extensive margin that may have been spurious, or at least unsustainable. Like the previous one, this conjecture remains to be verified of course. A further wrinkle to this argument is that lower-productivity maintenance is made more important by land use restrictions that prevent new constructions. Third, new constructions today are increasingly at the upper end of the market (Wang, 2022). Higher quality may be difficult to measure and may contribute to an apparent productivity decline.<sup>32</sup> 

At this stage, we draw the following conclusions about the economics of construction. The literature has made progress in our understanding of how factors in construction, land and capital (itself produced from labor and material), are combined to produce single-family homes and, in more recent research developments, tall buildings. There is an emerging consensus regarding how to frame the issues and some of the results. 

The key problem for construction is the slow growth of the technology used to assemble factors, not the price and quality of labor and materials. Productivity in construction be about a third of what it would be if in construction had followed the may technology same improvements as manufacturing technologies since 1950. We note here an important disconnect between a strand of research interested in identifying construction production functions (and thus supply responses for floorspace) earlier in this section and the more aggregate approaches used to study changes in construction productivity. 

Several explanations have been proposed to explain this dismal productivity performance. They include (i) the cumulative effects of restrictions imposed by unions and regulators, (ii) adverse effects of nimbyism pushing toward low-productivity projects and low-productivity construction firms, and (iii) more ‘natural’ causes arising from the need 

> 32We keep in mind that productivity can be either an aggregate, like value added per worker as used by Goolsbee and Syverson (2023), or the cost of building a specified house using data from RS Means data as in several contributions listed above. The evolution of the former productivity measure is much worse than that of the latter. Our conjecture about maintenance may explain part of this gap. Depending on the exact (but unknown) methodology of RS Means, an increased share of maintenance jobs in construction may also be able to contribute (or not) to the evolution of the RS Means series. For instance, for a given task such as installing shingles on a roof, RS Means may average its costs calculations over all such jobs even if doing this is much cheaper on a new house than as a replacement of old shingles on an existing house. 

37 

to maintain and repair an aging stock of housing and other mundane explanations of the same type mentioned above. Despite its appeal, the explanatory power of the first of these explanations is unclear. There are clear productivity inefficiencies caused by building codes ‘excesses’ and building height restrictions. However, these inefficiencies appear moderate, if not modest, in light of the poor productivity performance of the construction industry. Results in the literature suggest that they each add perhaps around 10% or less to construction costs. Relaxing these restrictions is a worthwhile endeavor, be it only because it will increase the quantity of housing produced, even if it does not lead to dramatic productivity changes, at least in the short run. Turning to the second explanation, nimbyism will also, of course, affect the volume of construction activity, which we explore in section 5. The third type of explanation is still largely unexplored. 

# **. 4 Beyond homogeneous housing services** 

The main limitations of the framework used in the previous section are that housing is: (i) durable, (ii) lumpy and differentiated, and (iii) subject to local spillovers. Here, we review the literature by considering each of these features. As these features can interact in interesting ways, we also consider the limited body of work that combines them. 

## **_4.1 Housing durability_** 

Building housing is an irreversible decision. Housing also takes time to develop and only slowly depreciates over time.<sup>33</sup> As a result, the development problem is not only about solving how much to build, as explored above, but also about deciding whether and when to build, when to rebuild, and, before rebuilding, how much to invest in maintenance to slow down depreciation. These decisions depend on market conditions today and far into the future. In turn, the aggregation of these decisions will affect current and future market conditions. This future is uncertain and requires forming expectations about it. For any given construction project, we also expect development, maintenance, and redevelopment decisions to be driven by unobserved idiosyncratic factors. 

To further motivate the importance of housing durability, we return to the headline figures for the elasticity of housing supply of section 3 with values of approximately two for homes and between 1.2 and for tall These are single-family five buildings. long-run elasticities that indicate how much is built after the decision to or floorspace develop redevelop is made. As indicated by equation (10), the long-run elasticity is multiplied by the 

> 33We take these features as self-evident. Evidence for the irreversibility of housing is provided by Burchfield, Overman, Puga, and Turner (2006) for the us between the mid-1970s and the early 1990s and by Combes, Duranton, Gobillon, and Gorin (2024) for France between circa 1860 and 2020. They all show that developed land rarely returns to an undeveloped state. Evidence of slow depreciation is reported above in figure 3. Construction delays will be familiar to all readers and do not require further evidence here. 

38 

probability of development to obtain the ‘short-run’ elasticity. In housing and construction, the long run is genuinely long. Hence, the ’short-run’ elasticity, often measured for periods of to 10 or 20 is the that is relevant to As we show up years, usually quantity policy. below in section 5.1, the estimated housing supply elasticities for, say, 10 years are often nearly an order of magnitude smaller than the long-run elasticities. The probability of development ultimately drives the magnitudes of supply elasticities that hold over the time intervals relevant to policy. Loosely speaking, the housing supply elasticities we care about are driven by the probability of development or redevelopment much more than by the long-run elasticities derived from the construction technology. 

A model of is still well our comprehensive dynamic aggregate housing supply beyond reach, given the difficulty of modeling decisions in rich, dynamic contexts. Partial approaches have nevertheless provided fundamental insights regarding (i) the development and redevelopment of specific parcels and (ii) the broader implications of the decisions to develop or redevelop for urban expansion and densification. We note that the earlier literature on housing durability is covered by Duranton and Puga (2015). Another class of spatial dynamic models is expertly reviewed in this _volume_ by Desmet and Parro (2025). The models they consider are more aggregated, sometimes covering the entire world, with a richer set of interactions through trade and migration, for instance. 

The first major insight from thinking dynamically about housing supply is the existence of an option value of development or redevelopment, leading to delays. The existence of real options associated with irreversible investments has been known for a long time and was discussed in the context of real estate development by Titman (1985). To understand this core issue, consider a risk-neutral builder facing an irreversible development opportunity over two periods on a parcel of unit size, with the same Cobb-Douglas housing production function as in equation (15): _h_ = _k_<sup>_α_</sup> after normalizing the productivity parameter _B_ = 1. There are no delays caused by the time to build. The rental price of housing in period 0 is known and equal to _P_ 0.<sup>34</sup> In period 0, the rental price of housing in period 1 is uncertain, with expected value **E** ( _P_ 1). The value of _P_ 1 is realized at the beginning of period 1. To keep matters simple, we ignore discounting and assume a constant unit cost for capital. We also postpone our discussion of the effects of construction on the rental price of housing. 

The builder chooses whether to develop in period 0 ( _d_ = 0) and collect rental income in both periods or wait and develop in period 1 ( _d_ = 1). While delaying development until period 1 implies foregoing the collection of rental income for period 0, it also allows the builder to build with the knowledge of the realized value of _P_ 1 rather than its expected value **E** ( _P_ 1). More formally, when developing in period 0, the expected profit of the builder is _π_ ( _d_ = 0) _≡ π_ ( _P_ 0, _k_ 0) + **E** ( _π_ ( _P_ 1, _k_ 0)) = _P_ 0 _k_ 0<sup>_α_+</sup><sup>**E**(</sup><sup>_P_1)</sup><sup>_k_</sup> 0<sup>_α−k_0.Thefirst-ordercondition</sup> with respect to profit maximization yields the profit-maximizing investment in capital. After 

> 34In static settings, the ‘price’ (asset value) of a dwelling and its rental value are confounded. 

39 

substituting for it into the profit function, we obtain, 



In the same way, choosing to delay and develop in period 1 yields a profit of _π_ ( _P_ 1) = (1 _− α_ ) _α_<sup>_α_/(1</sup><sup>_−α_)</sup> ( _P_ 1)<sup>1/(1</sup><sup>_−α_)</sup> . For a builder having to choose whether to build in period 0, the expected profit of delaying development until period 1 is 



From equations (25) and (26), it is easy to see that delaying development is profitable if and only if 



Because 0 _< α <_ 1, we know from Jensen’s inequality that this condition is satisfied when _P_ 0 = 0. More generally, this inequality will also be satisfied when _P_ 1 is large enough relative to _P_ 0 or, less obviously, when the variance of _P_ 1 is large enough. These two results suggest that delays are more likely when rental values are expected to grow and when uncertainty is higher.<sup>35</sup> 

To be clear, the value of waiting _π_ ( _d_ = 1) _− π_ ( _d_ = 0) is driven by the convexity of the profit function on the left side of the inequality in equation (27). When the variance of _P_ 1 increases, the profit of competitive builders who delay development increases (convexly) with _P_ 1. On the other hand, the value of building now on the right side of the inequality in equation (27) does not depend on the variance of _P_ 1. It depends only on its expected mean.<sup>36</sup> 

Although insightful, this framework may oversimplify matters and miss some key effects. This framework features only two periods but could easily be extended. Adding a fixed number of periods to the model above is conceptually straightforward. The burden is in the computations. As is well-known, infinite-horizon models are of a different nature because they can no longer be solved by backward induction, as above. They nonetheless seem appropriate to model housing development where decisions to develop or redevelop frequently occur while new constructions last for several decades and, in some cases, centuries. 

Let us turn to an infinite-horizon extension of the model presented above. Market _j_ is divided into _Lj_ 0 parcels of unit size that are initially undeveloped. Over time, the number 

> 35When investment takes a long time to implement, for example, because of construction lags, greater uncertainty can promote more rapid investment instead (Bar-Ilan and Strange, 1996). When projects take time to build, the probability of extreme outcomes increases. When builders can abandon their project, perhaps at a cost, the opportunity cost of waiting increases with uncertainty. This effect can be strong enough to more than compensate for the increase in benefits from waiting under greater uncertainty. 

> 36Although arguably less relevant in the context of real estate development, risk aversion provides another reason for delays by making outcomes with low prices in period 1 disproportionately costly. 

40 

of vacant parcels evolves according to _Ljt_ +1 = _Ljt − djt_ where _djt_ denotes the number of parcels developed at period _t_ . 

We consider the competitive builder who owns parcel _i_ in market _j_ . At each period, this builder chooses (i) whether to develop its parcel and (ii) how much housing _hijt_ to supply if it gets developed, i.e. if _dijt_ = 1. These decisions are irreversible. Undeveloped land does not generate revenue, while parcel _i_ , if developed at time _t_ , generates a rental income of _Pjthijt_<sup>for every period</sup><sup>_t ≥_</sup> _t_ , which is discounted by a factor 0 _<_ 1 _− δ <_ 1. 

Building on parcel _i_ is instantaneous but involves a fixed development cost _cijt_ , which is idiosyncratic. More specifically, and in line with much of the previous literature, we assume that _cijt_ is i.i.d. and follows a Type 1 Extreme Value distribution (or logit) every period. also incurs a variable cost. With the same function as Building Cobb-Douglas production in equation (15): _h_ = _k_<sup>_α_</sup> and following equation (23), the variable cost function is _Cjt_ ( _h_ ) = _rt h_<sup>1/</sup><sup>_α_</sup> after normalizing productivity _Bjt_ = 1 to ease the exposition. Then, the stock of housing in _j_ grows according to _Hjt_ +1 = _Hjt_ + _hjt_ where _hjt_ sums new housing produced across all newly developed parcels. Because parcels are all of the same size and face the same variable cost function: _hjt ≡_ ∑ _i dijt hijt_ = _djthijt_ . 

The evolution of housing in market _j_ is described by _Ljt_ for the number of vacant parcels and _Hjt_ for the stock of housing, the actions of developers _dijt_ and _hijt_ , the idiosyncratic fixed cost of development _cijt_ , and the rental price _Pjt_ of housing and _rt_ of capital. The rental price of housing is exogenous and, as above, uncertain. More precisely, at period _t_ , only _Pjt_ is known with certainty. For _t_ + 1 and beyond, developers form (rational) expectations. Given the fragmentation of the construction industry, this assumption of price-taking is reasonable in most cases. At the market level, new constructions affect the rental price of housing through their effect on demand. We return to this equilibrium effect in section 6. _Ξ_ . To keep our notations simple in what follows, we denote the set of state variables by _ijt_ 

The ex-ante value of (undeveloped) parcel _i_ is given by 



where the value of remaining undeveloped is: 



and the value of optimally developing this parcel is: 



where _Pjt hijt_ is the rental income of the current period, _rt h_<sup>1/</sup><sup>_α_</sup> is the variable cost of construction from above. In this expression, we also define _Πijt_ +1, the value of housing per unit at period _t_ + 1. It is the sum of the rental price of housing in _t_ + 1, which is known 

41 

at that point, and the expected value of the sum of discounted rental prices in _t_ + 2 and after: 



These expressions call for a few comments. First, the value function in equation (28) is written from the perspective of a builder with a vacant parcel. This vacant parcel generates zero income. Once a parcel has been developed, there is no remaining decision, and the parcel will bring a rental income for each future period. Second, if the builder chooses to leave the parcel vacant, the associated conditional value function from equation (29) repeats the value of a vacant parcel at the next period. This next-period situation implies the application of the discount factor 1 _− δ_ , knowledge of the realization of _Pjt_ +1, and a new draw of the fixed cost of development, _cijt_ +1. Third, if the builder chooses to develop the parcel in period _t_ , the associated conditional value in equation (30) includes the rental revenue for the period, the cost of construction, and the expected value of the discounted sum of future rental incomes. 

This model, which is closely related to Murphy (2018), Peng (2023), and Hsiao (2023), can now be solved for its two different margins: when to build and how much to build when building.<sup>37</sup> Starting with the latter, we can first insert equation (31) valued at period _t_ into equation (30) and write: 



after simplification. This expression shows clearly that the investment decision (i.e., how much to build) if made in _t_ , consists in maximizing the value of the house built, _Πijthijt_ , minus the variable and fixed costs of development. Taking the first-order condition, we obtain: 



which solves for the optimal investment after equating its marginal cost with its expected intertemporal marginal return. We note that this expression is the intertemporal analog of the optimal static investment in housing derived in equation (16). 

Estimating this equation is conceptually straightforward and implies regressing the log of how much housing is built on its unit price. However, this estimation is subject to 

> 37Before them, Paciorek (2013) estimated a city-aggregate analog to this model to show that more stringent land use regulations can lead to more price volatility through a real options mechanism. Another strand of literature models the decision of a single builder facing prices that follow a Brownian motion, following the pioneering work of Capozza and Helsley (1990) (see also Lebret, Liu, and Valentin, 2025, for an example of recent developments). These models provide nice insights about individual decisions relying on price uncertainty. A key limitation is that they are hard to aggregate to the market level because feedbacks of new constructions into prices affect their assumed Brownian motion. 

42 

the complications discussed in section 3 in the static case, including those that arise from the unobserved productivity term _Bjt_ , which is here hidden because it was normalized to unity for the sake of the exposition. The intertemporal nature of (33) adds additional complications because, in practice, the price of a new house is observed only if sold after it is built and not when the building decision was made. 

Working at the property level, Peng (2023) estimates a more complicated version of the simple framework we just described because she is looking at redevelopments, which, unlike the (simpler) decisions examined here, are not one-off decisions. Hence, her analog of equation (30) also contains an additional term associated with the effect of any current redevelopment on the cost of future redevelopments. This extra term is not observed. Then, using rent data, she only observed realized rents, not expected rents, at the time of the redevelopment decision. Using realized rents, in turn, introduces an expectation error, which leads to further complications in the estimation.<sup>38</sup> 

Also, working at the property level, Murphy (2018) implements an indirect approach. Because he considers that housing services are not observed, he cannot regress new supply on prices. Instead, he assumes that housing services result from house characteristics with a known functional form but with unknown parameters. He first regresses house prices on house characteristics using a standard hedonic approach. He then modifies equation (33) to obtain a marginal cost equation. This marginal cost can be reconstituted using the estimated coefficients of the house price regression and subsequently regressed on house characteristics to recover the analogs of _α_ /(1 _− α_ ) in equation (33). 

Turning to the decision to develop, this is a standard optimal stopping decision. Because the fixed cost of development follows a Type 1 Extreme Value distribution, the probability of development of parcel _i_ , is given by: 



where _χ_ is the scale parameter of the logit distribution of _cijt_ and _vijt_<sup>0and</sup><sup>_v_</sup> _ijt_<sup>1aredefined</sup> in equations (29) and (30), respectively. In turn, this equation can be aggregated across all (remaining) vacant parcels in market _j_ . 

Equation (34) recovers the responsiveness of new housing development with respect to the price of housing and the price of vacant land. In our decomposition of the elasticity of housing supply in equation (10), this loosely corresponds to the extensive supply elasticity _ϵ_<sup>_L_Akeydifferencewiththestaticmodelsofsection3.1,wherethedecisionto</sup> _P_<sup>(</sup><sup>_t_,</sup><sup>_t_+ 1).</sup> develop depends only on the price of housing, is that, in a dynamic setting, this decision depends on the price of housing relative to the price of vacant land. According to equation 

> 38To keep this section of manageable length, we only briefly describe how this dynamic framework gets implemented empirically but do not enter the details of the estimation strategies and their limitations. 

43 

(34), building on a vacant parcel is more likely when the value of a developed parcel increases relative to the value of vacant land, that is, when the rental value of housing at the current period _Pjt_ is higher. Like in the two-period model, the opportunity cost of delaying development is the loss of rental value at the current period. Similarly, the opportunity benefit of delaying is a higher future revenue from building more (or less) if future rental values turn out to be larger (or lower) than expected. Getting a good realization of the cost of is another factor of in our idiosyncratic fixed development delay infinite-horizon framework that we did not consider in the two-period model above. 

Estimating equation (34) (or its market-level analog) requires information about the development of parcels at period _t_ . Then, this estimation requires the knowledge of the conditional value functions _vijt_<sup>0and</sup><sup>_v_</sup> _ijt_<sup>1.</sup> In our simple case, the optimal supply of housing _hijt_ is known directly from the estimation of equation (33). It can be inserted into equation (32) so that _vijt_<sup>1depends only on the observed unit price of housing, the (previously</sup> estimated) parameters of the cost function, and the logit error term _cijt_ . In equation (29), _vijt_<sup>0is the continuation value associated with vacant land.Following Kalouptsidi (2014), we</sup> note that this continuation value is just the price of a vacant parcel, which can be estimated or read directly when the data is available. 

With neighborhood-level data, Hsiao (2023) employs a version of the strategy just described to estimate the responsiveness of housing supply to the price of housing and the price of vacant land. His estimation side-steps the direct estimation of equation (33) but accommodates it. Hsiao (2023) directly regresses a measure of new developments by neighborhood in Jakarta on local property prices. New constructions and property prices are likely to be simultaneously determined by unobserved local shocks, as already discussed. Hsiao (2023) instruments local property prices with local amenities viewed as demand shifters. We discuss additional demand shifters below in section 5.1. 

Peng (2023) uses a similar estimation strategy for redevelopment in New York City, where limits to the floor-to-area ratio changed over time and where building over the limit is possible at some additional costs, which are estimated. Murphy (2018) takes a slightly different two-step approach that does not rely on the values of developed and vacant land. Instead, he first estimates the probability of development and the transition probabilities for state variables from the difference _v_<sup>1thatis,fromtheperiodprofitratherthan</sup> _ijt_<sup>_−v_</sup> _ijt_<sup>0,</sup> the values of land, vacant and developed. The output of this regression can then be used to estimate an analog of equation (34) for market _j_ to retrieve the remaining structural parameters: 1 _− δ_ the discount rate, _<u>cijt</u>_ the mean fixed cost, and _χ_ the scale parameter of its 

44 

distribution, which measures its variance.<sup>39</sup> 

The payoff from this type of estimation is two-fold. First, a cost function can be retrieved with both the variable cost at the intensive margin and the fixed cost at the extensive margin. For single-family homes in Northern California, Murphy (2018) recovers variable costs per unit of floorspace close to the engineering estimates of RSMeans, with a similar evolution over time. His estimation also suggests large, highly dispersed fixed costs of development that increase over time. For multifamily and commercial properties in New York City, Peng (2023) estimates a convexity of the variable cost function in equation (32) of 1/ _α_ = 1.47, which implies _α_ = 0.68, a value close to those estimated in section 3. She also estimates a cost of construction close to the RSMeans estimates for in the same marginal buildings class in New York City. Importantly, regulatory costs at the intensive margin represent about a quarter of the marginal cost of construction. These variable costs are nonetheless dwarfed by large and highly dispersed fixed costs of redevelopment.<sup>40</sup> We note that the results of Murphy (2018) and Peng (2023) are convergent despite looking at different classes of buildings and different markets. Their cost functions are close to those estimated by static approaches, but the fixed costs they uncover are considerable. 

The second output of these studies is a short-run supply elasticity, which can be decomposed into a long-run elasticity supply at the intensive margin and a propensity to develop or redevelop at the extensive margin as in equation (10). Murphy (2018) shows a large wedge between the two elasticities, which appears to be driven by the builders’ expectations of future prices. Peng (2023) also highlights slow construction responses. In her case, a dramatic relaxation in maximum floor-to-area ratios in parts of New York City in the early 21st century only led to an increase of about 0.5% in the housing stock after 20 since the reform started. Here these to indicate nearly years again, papers converge extremely long development or redevelopment lags resulting from the high fixed costs that they also highlight. The persistence of buildings with floor-to-area ratios much below what is authorized need not reflect any form of misallocation. Instead, it may only reflect the normal operation of markets with durable goods or investments (Asker, Collard-Wexler, and De Loecker, 2014), at least in part. 

This type of framework can be enriched to allow further decisions to be made. Adding to the investment decision above seems exogenous depreciation housing straightforward, 

> 39Both Hsiao (2023) and Peng (2023) rely on asset values to estimate their version of equation (34). When the data is available, this approach only imposes minimal requirements regarding expectations since these are directly read in the price of vacant and developed parcels. Murphy (2018) uses a more involved strategy which differences out the value of vacant land to recover local time effects which can then be used to provide estimates of local values _vjt_<sup>0and</sup><sup>_v_</sup> _jt_<sup>1usedtoestimateanaggregatedversionofequation(34)followingArcidiaconoand</sup> Miller (2011). A full-solution estimation in the spirit Rust (1987) involves computing value functions using a (nested) fixed-point iteration for each guess of the parameters to be estimated. This type of approach is typically computationally prohibitive given the high dimensionality of the state space. 

> 40Hsiao (2023) focuses on the effect of flooding on construction as one input into his investigation of the importance of moral hazard. 

45 

but making depreciation endogenous adds another decision every period. Multiple investments are difficult to handle when they are additively separated because the first-order condition associated with equation (30) becomes highly non-linear. In a development context, Henderson, Regan, and Venables (2021) consider two building technologies for formal and informal housing and the transition between the two, depending on the location within a city (Nairobi). However, a key simplification they make is that informal housing is not durable. 

The framework above could be extended in a similar spirit to study the densification of neighborhoods from heterogeneous single-family homes to multifamily apartments with land assembly. This channel used to be the main way cities developed at the intensive margin. Despite repeated calls for urban densification, it now accounts for only a marginal share of new housing supply (Baum-Snow and Han, 2024). Understanding the key barriers to urban densification is an important challenge. Given the salience of the irreversibility of housing development and its durability, there is little doubt that extensions of this framework will be useful in exploring a variety of issues associated with housing development. 

Given the convexity of the cost of housing, the equilibrium of the builder’s problem is generally unique. However, complementarities, either on the supply or demand side, can this result. Due to the externalities from or change arising housing development redevelopment described below, future rental prices may increase when supply expands. This occurs, for instance, when redevelopment leads to increased neighborhood quality and, thus, desirability. As a result, two equilibria are possible. In the first, no redevelopment occurs because builders do not expect other builders to redevelop. In the second equilibrium, redevelopment occurs because builders expect other builders to redevelop, making redevelopment worthwhile. A similar issue arises with the emergence of subcenters or entire cities (Henderson and Venables, 2009). Such complementarities are an important reason why coordination mechanisms like masterplans are potentially desirable. We return to this issue below. 

Another key implication of the durability of housing is that it creates a fundamental asymmetry between situations with growing demand and situations with declining demand. With a growing demand in market _j_ , new housing is developed, with some lags, following the mechanics we just described. This corresponds to a gradual adjustment of the supply curve rotating clockwise. When demand declines, the housing stock cannot be unbuilt. The supply curve is thus kinked with a vertical portion at the current level of stock. Hence, when demand declines, most of the adjustment occurs through prices. These downward price adjustments can be considerable as the price of unwanted properties can fall to zero or close to it. Only in the very long run will the housing stock adjust through its depreciation. In turn, this argument implies that housing decline is often highly persistent following a large negative shock in a city or neighborhood. See Glaeser and Gyourko (2005) for the 

46 

original articulation of the issues and supportive empirical evidence. Duranton and Puga (2014) provide further discussion. 

## **_4.2 Lumpy and differentiated housing_** 

So far, we have assumed that a housing market is in equilibrium when the aggregate supply of housing services in this market is equal to its aggregate demand. This determines the unit price of housing, and, in turn, given this price, each household purchases a quantity of commensurate to its demand. useful for this housing Although many purposes, conceptualization of the housing market misses two critical features. First, housing is indivisible. Existing dwellings come as bundles of land and capital that are essentially fixed, at least in the short run. Second, housing is vertically differentiated, as these bundles differ in how much housing they offer. In simple words, some dwellings are nicer than others.<sup>41</sup> Rather than setting the unit price of housing and splitting the aggregate stock of housing services between residents, the operations of the housing market set the price of each dwelling and allow each household to be assigned to a dwelling.<sup>42</sup> 

Beyond its greater realism, this conception of housing is appealing a priori because it allows us to consider the entire housing market without arbitrarily partitioning it into separate segments. It also generates some interesting and non-trivial insights. For example, as we show below, adding high-quality dwellings affects the market differently than adding low-quality dwellings. Finally, for policy, we often care about understanding the effects of providing housing units of a certain type (in addition to housing services) and their distributional implications. Decisions by housing developers about the number of units to build on a given parcel are challenging to handle conceptually, as they reflect an interaction between heterogeneous demand by different types of households for different locations with the construction decision. Assignment models seem well-suited to handle these issues. 

Sweeney (1974) and Braid (1981) first proposed to model the housing market as an assignment process. See also Sattinger (1993) for an early introduction to assignment models with a focus on the labor market. While Määttänen and Terviö (2014) provide a more thorough treatment of the assignment equilibrium in the housing market in an exchange 41We also expect housing to be horizontally differentiated. Such differentiation typically implies (unpriced) benefits from the diversity of the housing stock as it allows residents to find accommodation more suited to their tastes. Zhang (2022) proposes a new empirical framework to explore this issue and suggests that real wages in New York City may be up to 15% higher than what a naive hedonic regression indicates when the benefits from housing diversity are taken into account. 

> 42As it turns out below, we can no longer define a market as a set of dwellings that face the same _unit_ price of housing since the latter varies across dwellings of different sizes. Instead, a housing market in an assignment model is a set of dwellings providing perfectly substitutable housing services, except for their size. 

47 

economy, we adapt Landvoigt, Piazzesi, and Schneider’s (2015) simplified model to keep the exposition simple.<sup>43,44</sup> 

Before turning to the analysis of the effects of changes in supply, we first consider the assignment of a set of households to a fixed stock of houses. Housing is vertically differentiated, and the quantity of housing services provided by a house, often referred to as its “quality”, is denoted by _h ∈_ [ _<u>h</u>_ <u>,</u> _h_ ]. There is a continuum of indivisible houses of unit mass described by its strictly increasing cumulative distribution function, _G_ ( _h_ ). 

There is also a continuum of households of unit mass. Households consume a composite numéraire good _c_ and one house offering housing services _h_ at price _P_ ( _h_ ). They maximize their utility function _u_ ( _c_ , _h_ ), which is strictly increasing in both arguments and quasi-concave, subject to the budget constraint _P_ ( _h_ ) + _c_ = _w_ . Income, _w ∈_ [ _<u>w</u>_ <u>,</u> _<u>w</u>_ ], differs across households. Its cumulative distribution function, _F_ ( _w_ ), is strictly increasing. 

The first-order conditions for utility maximization by households imply 



as the marginal rate of substitution of housing for the numéraire good is equal to the marginal price of a dwelling offering more housing services, _∂P_ ( _h_ )/ _∂h_ . We note that this condition is satisfied by households of different income levels along the distribution of dwellings. Thus, there is no reason for _∂P_ ( _h_ )/ _∂h_ to be constant and, consequently, for the price of a house to be proportional to the housing services it provides. This is the first major implication of housing indivisibility: the price of a house _P_ ( _h_ ) is no longer necessarily equal to _P × h_ and, instead, depends on the distributions of _h_ and _w_ . 

To prove this last point rigorously, we first note that our model features positive assortative matching by _h_ and _w_ . With quasi-concave utility, the marginal rate of substitution of housing for the numéraire good decreases in housing. In turn, diminishing marginal rates of substitution in equation (35) imply that richer households have a higher willingness to for more This can be derived pay dwellings offering housing. formally by differentiating _w_ the marginal rate of substitution with respect to after substituting in the budget constraint for _c_ .<sup>45</sup> Hence, in any equilibrium, richer households occupy bigger and more expensive 

> 43A key difference with Määttänen and Terviö (2014) is that we consider a two-sided heterogeneity framework. In contrast, theirs is a one-sided heterogeneity exchange economy where households of heterogeneous income are initially allocated heterogeneous dwellings. As a result, the budgets that households face are endogenous and depend on the price of their dwelling in equilibrium. This perhaps more realistic setting comes at the cost of additional complexity. 

> 44Models of vertically differentiated housing have also been used to understand house price dynamics following changes in the demand for housing and changes in the ability of households to obtain a mortgage to finance their house (Ortalo-Magné and Rady, 2006, Landvoigt _et al._ , 2015, Nikolakoudis, 2024). Behrens, Duranton, and Robert-Nicoud (2014) and Davis and Dingel (2020) have used assignment models to study the sorting of households across cities. 

> 45This amounts to a standard single-crossing solution ensuring the perfect separation of households of increasing _w_ across dwellings of increasing _h_ . 

48 

## dwellings. 

This intuitive property is an important step towards solving the model since the assignment of dwellings to households can now be described by a strictly increasing matching function _h_<sup>_∗_</sup> ( _w_ ) for _w ∈_ [ _<u>w</u>_ <u>,</u> _<u>w</u>_ ] with _h_<sup>_∗_</sup> ( _<u>w</u>_ ) = _<u>h</u>_ and _h_<sup>_∗_</sup> ( _<u>w</u>_ ) = _h_ . In what follows, it is convenient to work with its inverse, the assignment of households to dwellings, _w_<sup>_∗_</sup> ( _h_ ). With positive assortative matching, the market clearing condition can be expressed as _F_ ( _w_<sup>_∗_</sup> ( _h_ )) = _G_ ( _h_ ), as all households of rising income are assigned to the dwellings offering more housing services. In turn, this condition can be written as, 



Importantly, the assignment of households of higher incomes to larger dwellings only depends on their respective distributions and not on household preferences, unlike in standard models. Hence, “quantities” do not depend on preferences, but prices do. As made clear by equation (35), preferences determine the price of each dwelling. In turn, these prices make the allocation described by equation (36) sustainable in equilibrium. Intuitively, the household of income _w_ that occupies dwelling _h_ must pay enough to avoid being outbid by the household of income _w − ∂w_ who occupies dwelling _h − ∂h_ . In turn, the price of dwelling _h_ + _∂h_ must be high enough to discourage household _w_ from outbidding its current occupier of income _w_ + _∂w_ . Hence, the price of dwelling _h_ + _∂h_ depends on the price of dwelling _h_ , which in turn depends on the price of dwelling _h − ∂h_ . 

More formally, the price of dwelling _h_ is given by 



where the second equality is obtained from equation (35) after normalizing _P_ ( _<u>h</u>_ ) = 0 and changing the integration variable from dwellings to households. While we have not solved the equilibrium marginal rates of substitution yet, this equation delivers two important insights regarding the working of assignment models. First, the price of dwellings depends non-trivially on the distributions of houses _G_ ( _h_ ) and income, _F_ ( _w_ ). For example, dilating the distribution of incomes from [ _<u>w</u>_ <u>,</u> _<u>w</u>_ ] to [ _<u>w</u>_ <u>,</u> _<u>w</u>_<sup>_′_</sup> ] with _<u>w</u>_<sup>_′_</sup> _>_ _<u>w</u>_ raises the marginal rate of substitution of housing for the numéraire good. In turn, this increase makes the price of dwellings increase faster with _h_ , as the competition between the richest households for the best houses becomes more intense. 

Second, an increase in the income of the richest households in the distribution does not affect the price of the dwellings of other (poorer) households. On the other hand, an increase in the income of the poorest households (which preserves their ranking for simplicity) increases the price of all dwellings, including the largest one. These price effects are sometimes referred to as directional price spillovers. They occur because of the additive nature of the price of dwellings in equation (37). An increase in the income of the poorest 

49 

households raises their marginal rate of substitution and, thus, how much they are willing to pay for dwellings with a larger _h_ . As a result, richer households will need to pay more to retain their current dwelling, even if their income is unchanged. Simply put, demandinduced changes in the prices of dwellings ‘trickle up’ but do not ‘trickle down’. 

To keep our derivations simple, we consider the case where _u_ ( _c_ , _h_ ) = _c_<sup>1</sup><sup>_−η_</sup> _h_<sup>_η_</sup> and both income and housing services are uniformly distributed. From the Cobb-Douglas nature of preferences, we can rewrite equation (35) as 



after using the budget constraint and the inverse matching function _w_<sup>_∗_</sup> ( _h_ ) to substitute for the consumption of the numéraire good. From the uniform nature of the distributions of _w_ and _h_ , it is easy to show that the assignment of households to dwellings is described by 



Inserting equation (39) into equation (38) to substitute for _w_<sup>_∗_</sup> ( _h_ ) yields a first-order linear ordinary differential equation. Its solution is 



where the integration constant _c_ 1 is such that _c_ 1 = _a_ 0 _<u>h</u>_ (1 _−η_ )/ _η_ + (1 _− η_ ) _a_ 1 _<u>h</u>_ 1/ _η_ for _P_ ( _<u>h</u>_ ) = 0 to be satisfied. The price of dwellings is therefore increasing and concave in _h_ following the distributional assumptions made above. 

Wang (2022) and Nathanson (2023) allow for a change in the supply of dwellings in this type of framework.<sup>46</sup> We consider the addition of a small discrete set of new dwellings of mass _∆_ to the housing stock. The housing services of these dwellings are distributed over the subsegment [ _h_ 0, _h_ 1] with _h_ 0 _>_ _<u>h</u>_ and _h_ 1 _< h_ . Assuming for now a fixed set of residents, this increase in housing supply leads households with income _w < w_<sup>_∗_</sup> ( _h_ 1) in the original equilibrium to move to a larger dwelling. Hence, the increase in the stock of housing trickles down and benefits poorer households. To preserve positive assortative matching in the bottom part of the distribution, these moves to larger homes occur in a chain, with each household moving up by _∆_ (= _G_ ( _h_<sup>_′∗_</sup> ( _w_ )) _− G_ ( _h_<sup>_∗_</sup> ( _w_ ))) in the distribution of dwellings. Now occupied by poorer households, the price of smaller dwellings declines. This price decline is magnified in equilibrium as poorer households now enjoy a higher level of utility, which reduces how much they are willing to pay for more housing services. 

> 46Nathanson (2023) assumes a collection of discrete classes of dwellings with different levels of housing services rather than a continuum. The equilibrium is solved using boundary conditions between sets of dwellings with different levels of housing. Despite these differences, the key qualitative properties of the model appear similar. 

50 

**Figure 6:** Supply decision in assignment models 



<!-- Start of picture text -->
q(h)<br>h π h<br>C(h) P(h)<br>P<br><!-- End of picture text -->

_Notes_ : The vertical axis is in numéraire and the horizontal axis is in the quantity of housing services provided by a dwelling unit. The solid line is an example cost function _C_ ( _h_ ), and the dashed line is an example price function anticipated by developers prior to construction. The difference between the price and the construction cost of a dwelling results being _q_ ( _h_ ), the price of the land parcel. Following changes in fixed costs, _C_ ( _h_ ) could be shifted up or down with no resulting change in _h_<sup>_π_</sup> . 

Thus, poorer households now occupy larger dwellings at a lower price. At the very bottom of the distribution, there is now a surplus of dwellings. The smallest occupied _′ ′ ′_ dwelling _<u>h</u>_ is such that _G_ ( _<u>h</u>_ ) = _∆_ , the mass of new dwellings. Dwellings with _<u>h</u> ≤ h <_ _<u>h</u>_ are now empty and end up with _P_ ( _h_ ) = 0. At the same time, for the dwellings with _h > h_ 1, there is no change in their assignment. However, the price of these larger dwellings decreases. With households with lower income enjoying lower prices for _h < h_ 1, the price pressure they put on larger dwellings weakens. 

While from the addition of new two caveats are everyone eventually benefits dwellings, worth keeping in mind. First, we have considered so far that the set of households was fixed. If dwellings become cheaper in a market, they will attract newcomers. These newcomers will offset some of the benefits for residents of lower housing prices (Nathanson, 2023). The complication is that these newcomers will be selected in the income distribution depending on the utility they enjoy elsewhere, their moving costs, and the changes in the distribution of the price of local dwellings. At one extreme, if there is free mobility for all income levels at the initial equilibrium and if market _j_ is small relative to the economy, adding to the stock of housing in _j_ only implies an increase in population _∆_ , with income distributed over [ _w_<sup>_∗_</sup> ( _h_ 0), _w_<sup>_∗_</sup> ( _h_ 1)] matching exactly the distribution of new dwellings. 

The second caveat is that new dwellings may be produced, not as net additions, but by upgrading existing dwellings over _h ∈_ [ _h−_ 1, _h_ 0]. In this case, residents with income _w < w_<sup>_∗_</sup> ( _h−_ 1) do not experience any change, while richer households benefit from the upgrading of the stock of housing. When allowing for migrations in and out of the market, upgrading some dwellings will lead to the entry of new households and the exit (or homelessness) of some incumbents. 

51 

With a housing production function as in equation (15), builders face a trade-off between the convex marginal cost of construction and the fixed outlays associated with the acquisition of the parcel and the fixed cost to start construction. This cost function is represented on figure 6. The builder’s profit maximization problem is essentially the same as in section 3.1. The main difference is that the revenue from construction is no longer proportional to _h_ as the builder faces a non-linear equilibrium price schedule. However, if _P_ ( _h_ ) is concave in _h_ as in the example derived above, there is still a well-defined level of housing services _h_<sup>_π_</sup> that maximizes The difference between the of the built per dwelling profits. price dwelling and its costs is dissipated in the price of the land, as previously. Figure 6 illustrates this situation. 

Interestingly and perhaps surprisingly, all builders choose a similar level of housing services _h_<sup>_π_</sup> for newly built dwellings. This result comes from the uniqueness of the solution to the profit-maximizing choice of dwelling size. This unique dwelling size occurs despite the heterogeneity of residents’ income. In equilibrium, households reassign themselves across dwellings at no cost. Although we doubt this result holds in more realistic settings with frictions to re-assignment, this result highlights a powerful force that pushes towards homogeneous neighborhoods: the variable cost of construction is convex.<sup>47</sup> Allowing for land parcels of different sizes or other differences in parcel characteristics would also lead to the construction of heterogeneous dwellings in equilibrium. These caveats aside, the homogeneity of new developments is consistent with casual observation in many markets. 

Quite plausibly, new constructions may offer more housing services than existing dwellings (‘bigger and nicer homes’).<sup>48</sup> The effect of higher prices following an increase in demand is ambiguous. A proportional increase in _P_ ( _h_ ) leads to a higher _h_<sup>_π_</sup> . This would be illustrated by an anti-clockwise rotation of the price schedule in figure 6. However, changes in demand need not imply a proportional increase in the price of dwellings. For instance, with less binding credit constraints, demand may increase particularly strongly in the lower tail of the distribution, leading to strong price increases there. In turn, builders will also ‘follow the demand’ and may choose a lower _h_<sup>_π_</sup> . 

This approach can replicate two interesting features documented by Wang (2022). First, new constructions occur in markets such as Cleveland in the 2010s a over- despite general supply of housing and extremely low median prices. These new constructions are at the end of the distribution to serve households for whom several upper high-income cheap houses are no substitute for a luxury one. She also documents that new constructions in 

> 47As long as it remains below a certain threshold, the fixed cost is irrelevant to the choice of _hπ_ as it only affects land prices. Above this threshold, no profitable building occurs. Put differently, the fixed cost of development only affects the extensive margin of development. We return to this important point in section 5. 

> 48We do not model the dynamics of supply here, but the gradual decay of dwellings will push toward building new dwellings to be provided in the upper tail of the distribution – higher _h_<sup>_π_</sup> – be it only to “replenish the stock”. We develop this point in the next subsection. 

52 

San Diego during the boom of the early 2000s occurred for gradually smaller houses as the larger ones became unaffordable to all but the very richest households. 

The empirical implementation of assignment models presents several challenges. While ‘testing’ for positive assortative matching in the housing market is likely foolish since it will never hold exactly, assessing how strongly it holds is a worthwhile empirical exploration, following Epple, Quintero, and Sieg (2020). The correlation between deciles of household incomes and deciles of house prices is strong, and the ordering is often perfect (Määttänen and Terviö, 2014, Wang, 2022). However, house prices are forward-looking and may not always reflect the user cost of housing well (Nathanson, 2023, Nikolakoudis, 2024), especially when comparing across markets. We also expect households to make their (indivisible) housing decision based on their permanent income and not their current income. 

The of income shocks at the bottom of the income distribu- trickling up prices following tion and the absence of trickling down after income shocks at the top is another interesting and specific property of assignment models. It is at the heart of the quantification of Landvoigt _et al._ (2015) and explored more broadly by Wang (2022) and Nikolakoudis (2024). While limited, the evidence about the asymmetric propagation of prices is encouraging. The trickling down of price changes after supply shocks is another interesting property of assignment models. It is explored by Wang (2022), Nathanson (2023), and Mense (2025) who provide supportive evidence. Understanding more precisely how prices adjust even if, as discussed below, we do not observe a full chain of moves would be interesting as well. 

Consistent with the framework developed here, Handbury, Hugues, and Keys (2024) argue that since the Great Financial Crisis, the growth in demand for rental housing has been particularly strong in the higher tiers of the distribution. Supply responded by expanding in those tiers, taming growth in rental prices for this segment of the market. At the same time, demand growth for rental housing in lower tiers remained unmet. Price growth was disproportionate for this segment of the market as demand grew, but supply did not respond. These findings beg two important questions. How much do rental prices at the lower end need to increase for new constructions to occur in this segment of the market? How much new construction is needed in the tier for to start in the upper prices declining lower tiers? 

The existence of downward chains of moves between dwellings is another important prediction of assignment models. Obviously, the assumption of frictionless moves could only hold in the very long-run. As a result, a newly constructed dwelling with _h_ units of housing services may result in vacancy in a dwelling with less than _h_ , even if dwellings of even lower remain The is then the extent to which we quality occupied. empirical question observe chains with households the distribution after moving moving up housing quality new constructions. 

Using detailed address history data for 686 new large multifamily projects in the us, 

53 

Mast (2023) tracks the former residences of current tenants and those who moved to replace them, etc. He documents moving chains that are fairly long and deep. A new market-rate building with 100 dwellings eventually leads 45 to 70 households to move out of below-median-income after six rounds of moves. While moves are neighborhoods early generally local, after six rounds, the chains reach a much wider housing market, essentially the metropolitan area. These moving chains are also relatively fast, as most of the reported effects occur within three years. Using data from Finland, Bratu, Harjunen, and Saarimaa (2023) reach conclusions that are mostly similar to those of Mast (2023). The main difference is that moving chains in Helsinki go much deeper at each round, perhaps reflecting the more compressed nature of the Finnish housing stock. French and Gilbert (2024) also study vacancy chains in the us. Like Mast (2023), they find that moving chains deepen socially and broaden to the entire metropolitan area as the number of moves progresses. Unlike Mast (2023), they uncover short vacancy chains. It is unclear whether this difference is due to their much broader which include in the lower of the coverage, may dwellings segments distribution occupied by newly-formed households, or to difficulties in tracking movers and new housing. 

The unobserved nature of services constrains work on housing empirical assignment models. Existing research mostly takes for granted the one-to-one mapping between _P_ ( _h_ ) and _h_ to work around _h_ being unobserved. To quantify their model Landvoigt _et al._ (2015) had to take a stance on changes in the quality of houses on the market in 2000 and 2005. They do so using a repeat sales index, but this does not allow them to recover the underlying distribution of _h_ . The price of a house is a linear function of its _h_ in some cases, for instance, when the distributions of income and housing services are scaled versions of each other. These are, however, the situations where assignment models are the least interesting since they revert to the same properties as the models with divisible housing. In an innovative effort, Epple _et al._ (2020) explicitly treat housing services as a latent variable, which they estimate non-parametrically from repeated observations of the same market and a number of further identifying restrictions. 

## **_4.3 Filtering_** 

Filtering links together the durability of housing and its vertical differentiation through depreciation. As dwelling _i_ in market _j_ ages, it decays, and the housing services it provides evolve according to _hijt_ = (1 _− δ_ ) _hijt−_ 1 with _δ <_ 1. In the simplest formulations, the depreciation rate, _δ_ , is considered exogenous. Depreciation should nonetheless be viewed as a function of the owner’s maintenance effort. In turn, this maintenance effort depends on housing prices in market _j_ and the cost of maintenance. 

These features are illustrated above in figure 3, which documents the slow disappearance of older dwellings from the stock of housing. Although the notion of housing decay 

54 

**Figure 7:** Mean household income by structure age 



<!-- Start of picture text -->
Small and Rural Counties Suburbs<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>Central Cities Superstar Cities<br>1980 1990 2000 2010 2020 1980 1990 2000 2010 2020<br>0-10 11-20 21-30 31+<br>100 100<br>80 80<br>60 60<br>40 40<br>household income (thousands) household income (thousands)<br>20 20<br>100 100<br>80 80<br>60 60<br>40 40<br>household income (thousands) household income (thousands)<br>20 20<br><!-- End of picture text -->

_Notes_ : As in Figure 1, plots use individual level cenusus and acs micro data aggregated to the household level. Household income is deflated to 2000 dollars using the cpi-u. For 2005-2022, indicated age ranges are only approximate due to limitations on built year information. For 2005-2014 on the horizontal axis, “0-10” covers structures built after 1999, “11-20” covers structures built in the 1990s, “21-30” covers structures built in the 1980s, and “31+” covers structures built prior to 1980. For 2015-2020 on the horizontal axis, “0-10” covers structures built in the prior 10 years, “11-20” covers structures built between 2000 and the indicated year minus 10, “21-30” covers structures built in the 1990s, and “31+” covers structures built prior to 1990. This reclassification results in upward jumps in 2015. For 2021-2022 on the horizontal axis, “0-10” covers structures built after 2009, “11-20” covers structures built 2000-2009, “21-30” covers structures built in the 1990s, and “31+” covers structures built prior to 1990. 

is much broader than old dwellings taken out of the stock, the differences in exit rates documented by the various panels of the figure are striking: 0.7% per year in small and rural counties vs. 0.2% in superstar cities. See also Gyourko and Saiz (2004) for more systematic evidence about the endogeneity of housing investment and decay. While we discuss the strong correlation between household income and house prices above, there is also a strong correlation between the age of dwellings and the income of their residents, as illustrated by figure 7. See Brueckner and Rosenthal (2009) for further evidence on this. As a dwelling ages, not only does it decay, but it also hosts poorer households. This process is referred to as filtering. 

Conceptually, in the absence of any other change, a constant rate of housing decay implies a leftward shift of the cumulative distribution function _G_ ( _h_ ) of housing services: 

55 

_Gt_ ( _h_ ) = _Gt−_ 1 ( _h_ /(1 _− δ_ )).<sup>49</sup> Positive assortative matching remains, and residents occupy the same (decayed) dwelling from one period to the next. When all dwellings decay, the price schedule _P_ ( _h_ ) adjusts following the marginal rates of substitution as per equation (35). In the special case where this marginal rate of substitution is constant, such as with Cobb-Douglas preferences, the price schedule shifts leftward over time in figure 6 with _Pt_ ( _h_ ) = _Pt−_ 1 ( _h_ /(1 _− δ_ )). 

Any steady state must then be such that new constructions only happen for the best houses offering _h_ units of housing to replenish the stock of housing from above and keep the quantity of housing and its distribution constant. This level of housing services _h_ for newly built houses should also correspond to what builders provide in figure 6, _h_<sup>_π_</sup> . Hence, in the steady state of a simple assignment market with durable but decaying dwellings, the most profitable opportunities for builders are at the top of the market for the richest households. Newly built dwellings first serve this high-end market, after which they “filter” down the household income distribution as they age into lower-quality tiers. 

While extremely stylized, this steady-state equilibrium is helpful to think about a number of possible perturbations affecting it. First, as households get richer over time, the richest households will be willing to pay more for dwellings that offer more housing services. Hence, the best dwelling will increase in quality over time: _ht > ht−_ 1. As the upper tail of the distribution of income shifts to the right, so will the supply of new dwellings, which will move toward providing ever-higher housing services to their wealthy residents. In turn, these dwellings will take longer to filter down. 

It is also easy to understand how an increase in demand for middle- or lower-quality dwellings will not, in general, be directly served. As illustrated in figure 6, the price schedule in the body of the distribution or in the lower tail would need to increase a lot to make more affordable dwellings attractive to build. This situation is all the more difficult to reach since price increases for smaller dwellings are expected to percolate up and make new constructions at the upper end attractive again for builders. The more general point behind these two examples is that there are strong economic forces that push against building directly for poorer households. As a result, the supply of new housing in the lower tiers of the distribution may be highly inelastic, a fact noted by Handbury _et al._ (2024), among others. 

As the supply of housing in the lower tiers of the market is mostly unresponsive to prices, it only expands when dwellings in the upper tiers decay. This lack of supply response implies that the housing stock may not match well with demand outside of the highest tiers of the market. For instance, there may be a missing middle of dwellings for the middle class, and this missing middle may persist for a long time. 

> 49We assume here that a dwelling can decay all the way from _h_ to 0. In practice, multifamily apartment buildings are easier to reoccupy by poorer tenants, possibly after redividing units. This is harder for high-end single-family houses. 

56 

Restrictive land use have a role in this of regulations may particularly perverse type model. By drying up the supply of housing, they end up excluding the poorest households from the market as the number of “viable” units declines (say, below a certain threshold for _h_ ). Allowing for maintenance to slow down this decline can exacerbate the problem. If new supply at the top is scarce, the wealthiest residents will try to slow down the decay of their dwellings (or even improve them). In turn, these actions slow down or completely stop the arrival of newly available, lower-quality housing for less well-off residents.<sup>50</sup> 

An oft-considered solution to this problem is to mandate new lower-quality dwellings for new constructions through inclusionary zoning (iz). We discuss these policies below, but they seem to fail, as the lower cost of building at lower quality is dwarfed by much lower revenues for builders. Another approach is to make land use regulations less restrictive and reduce other impediments to new constructions. These new constructions happen in the upper tail of the quality distribution. In the short run, they allow lower-income residents to move up through moving chains. In the long run, the decay of these additional dwellings eventually filters down and increases the supply of lower-quality dwellings. The main limitations are that (i) moving chains may be too slow and shallow, and (ii) wealthy newcomers from different metropolitan areas may occupy new “luxury” housing.<sup>51,52</sup> 

We also note that housing decay also plays an important role in standard limitations of rent control policies Arnott (1995). With endogenous maintenance, landlords let rentcontrolled housing quality decay until controlled rents correspond to their market rents. In this case, the lack of middle-quality housing no longer arises from a lack of filtering from the top but instead from too much filtering to the bottom. 

At this stage, the question becomes how much filtering there is in the data. Despite a heated debate in the policy literature, very little is known about the rate at which housing “naturally” decays (say, with only minimal investment) and how maintenance and renovations affect decay. For instance, a 0.5% annual rate of decay over 50 years implies a decline in _h_ for a dwelling of 22%. This would be arguably insufficient for filtering to be a major source of housing supply in the lower tiers of the housing market. On the other hand, a 2.5% decay would imply a decline in _h_ of 70% over 50 years.<sup>53</sup> In figure 3, we crudely proxy filtering through the exit of dwellings from the housing stock. In path-breaking work, Rosenthal (2014) develops a “repeat-income” methodology to measure 

> 50See Arnott and Braid (1997) for an early related formalization. 

> 51As we show in section 6, having highly skilled workers moving to prosperous locations can generate large gains but does not solve the issue of insufficient housing for residents in the lower deciles of the income distribution. 

> 52A third option to provide affordable housing would be to greatly lower the variable cost of construction of such dwellings through, for instance, cheaper modular housing. 

> 53Using hedonic methods, Francke and van de Minne (2017) find that the typical housing structure in the Netherlands loses 43% of its value over 50 years gross of maintenance. 

57 

filtering. This approach essentially consists of following dwellings and measuring the change in the income of their successive residents as these dwellings age. 

We note that this metric does not capture the physical decay of dwellings per se, but instead captures changes in the assignment function of household income to dwellings. This is an analog to changes over time in the assignment function _w_<sup>_∗_</sup> ( _hijt_ ) _− w_<sup>_∗_</sup> ( _hijt−_ 1) in the model above. This metric is relative and captures both the decline of dwellings as they age and the possible movement of poorer households into higher-quality housing. Although not directly informative about changes in the housing stock, this is a relevant measure of A rate of 1% to of a 1% as filtering. filtering corresponds occupants dwelling being poorer the dwelling ages by one year. 

Rosenthal (2014) estimates annual filtering rates of 0.5% for owner-occupied dwellings and 2.5% for rentals in the us between 1975 and 2011. For owner-occupied housing, the filtering rate is high during the first years of the life of a dwelling before stabilizing. It is even increasing again for older dwellings, acknowledging the selection of dwellings that pass the 50-year mark. Importantly, dwellings often switch from owner-occupier to rental status Accounting for this, Rosenthal (2014) computes a 1.9% filtering rate overall, which corresponds to a 60% decline in household income over 50 years. This would make filtering an important source of housing supply for the lower tiers of the housing market. 

However, as noted by Rosenthal (2014), filtering is locally highly sensitive to market conditions, and to housing prices in particular, as should be expected. This finding is confirmed by Liu, McManus, and Yannopoulos (2022), who find annual filtering rates that vary from -1.6% in Topeka, Kansas to a positive 0.7% in San Francisco. Spader (2024) extends Rosenthal’s analysis to 2021 and finds that filtering essentially stopped in the us after 2011 when the housing market started to recover after the Great Financial Crisis while construction lagged. This finding suggests that filtering is highly responsive to prices and can only function when enough new housing gets built. In that case, filtering is a primary source of housing supply for the lower tiers of the housing market. When building activity slows down, however, filtering stops. 

## **_4.4 Housing externalities_** 

Another key feature of housing is that the value of a dwelling depends on the number and quality of nearby dwellings and the people living inside them. In other words, there are housing externalities. These externalities can occur directly from the supply side. Re-painting a house can increase the value of nearby houses, as they become more appealing to potential buyers. In turn, higher house values in a neighborhood may encourage further maintenance and improvements. Housing externalities may also arise from the demand side. Nicer houses nearby may attract more desirable neighbors, in turn making the neighborhood more attractive and leading to further increases in supply. Under a slightly 

58 

different causal chain, the arrival of more desirable neighbors may trigger improvements in the local housing stock, leading to further changes in the composition of residents in a neighborhood and more changes to the local stock of housing, a process sometimes referred to as gentrification. Regardless of their exact mechanics, as housing externalities affect property values, they also affect the supply of housing. We also keep in mind that, because they affect migrations across locations, housing externalities can have effects far from where they take place. Investing in housing somewhere can lead to housing decay elsewhere. 

Housing externalities may first occur at the construction stage. In his review, Brueckner (2000) distinguishes three market failures associated with the construction of new dwellings. First, new housing developments fail to account for the social value of open space. Open at the outskirts of cities are as recreational amenities dwellers. spaces enjoyed by city Open spaces are also desirable locations for new constructions. In turn, new constructions make less and reduce their values. This of open spaces open amenity negative externality urban sprawl is nonetheless more subtle than this simple story. Turner (2005) shows that preferences for open spaces nearby will lead to too little open space in equilibrium, that is, too much urban expansion. These preferences also imply an overly dense and populated urban core. The reason for this surprising result is that preferences for open spaces cut both ways. Some residents will rush to occupy peripheral urban spaces, but by doing so, they will destroy the appeal of these locations, and thus many will elect to live in the (oversized) core. More generally, spatial externalities associated with the construction or renovation of housing often generate subtle effects in equilibrium. 

The second market failure associated with new constructions is the failure to account for the traffic congestion they generate. Beyond congestion, driving also generates pollution, noise, and accidents. Poor parking pricing also generates too much cruising for parking, and before that, it also distorts incentives to drive to some locations. In short, residents do not pay the full social cost of their commutes and other errands. As a result, city residents will tend to live in overly remote locations. Cities will thus spread out inefficiently. There is an empirical literature documenting the patterns of housing development with notable contributions by Burchfield _et al._ (2006) and a lively literature in urban planning and remote sensing (Artmann, Inostroza, and Fan, 2019, provide a recent review). However, drawing convincing welfare estimates about the cost of urban sprawl and sound policy conclusions is still an open (and highly disputed) issue. 

The last market failure associated with new constructions highlighted by Brueckner (2000) is the failure to account for the cost of providing infrastructure and services to new development. In the us, this failure has been documented by Altshuler and Gómez-Ibáñez (2000) among others. This market failure also leads to the development of new housing 

59 

overly far from city centers and at suboptimally low levels of density.<sup>54</sup> 

For redevelopment and maintenance, another set of externalities becomes more salient. In their analysis of the local spillover effects of new Low Income Housing Tax Credit (lihtc) housing, Diamond and McQuade (2019) estimate that a new (multifamily) development in a poor neighborhood increases nearby house prices by 6.5% while lowering crime rates and attracting diverse populations. In a rich neighborhood, a new lihtc development reduces nearby house prices by 2.5% and attracts poorer residents. At least in poor neighborhoods, some local externality must be at play for a new housing development to raise the value of other dwellings despite an expansion of supply. It is harder to tell whether this externality is associated with the new building itself or with the residents living in it. 

In a radically different setting, Hornbeck and Keniston (2017) document the reconstruction of Boston after the great fire of 1872. They show that, after reconstruction, property prices are significantly higher for burned plots and nearby unburned plots, as new constructions and building improvements encouraged further improvements nearby. Spillovers of a similar sort are also documented in Davidoff, Pavlov, and Somerville (2022), which we discuss further below, and González-Pampillón (2022). 

In a setting where it is easier to distinguish between externalities arising from better housing with those coming from more desirable neighbors, Rossi-Hansberg, Sarte, and Owens (2010) report external land value gains of two to six dollars per dollar invested in housing renovation in a neighborhood improvement program in Richmond (va). These positive effects decline by half over 300 meters. The counterpart of these results is that we also expect the contagion of blight that leads to low maintenance, more abandonment, and underutilized land even in otherwise high-cost areas (Owens, Rossi-Hansberg, and Sarte, 2020).<sup>55</sup> 

There are also alleged externalities associated with bringing together housing units of different levels of within the same subdivision or the same quality multifamily complex. This practice is often referred to as inclusionary zoning (iz). Before discussing these externalities, some background about iz and some understanding of its mechanics are in order. Stacy, Hodge, Komarek, Davis, Noble, Morales-Burnett, and Rogin (2023) report the existence of iz laws in 886 jurisdictions in 25 states and the District of Columbia in the us in 2016. These restrictions are usually hard constraints on new developments. They mandate a share of “affordable” units to be sold below market prices in all new developments. In 

> 54One could also add externalities associated with local population density and other measures of urban form, either in terms of production or consumption. With such externalities, the equilibrium building stock will not be optimal, but the direction and magnitude of the inefficiencies differ across locations and are sensitive to functional forms. See Duranton and Puga (2015) for further discussion. We discuss the effects of neighborhoods and the composition of their housing stock below. 

> 55A related literature focuses on the effects of house foreclosures during the Great Financial Crisis. For instance, Gerardi, Rosenblatt, Willen, and Yao (2015) find that a foreclosed home lowers the price of nondistressed houses within a tenth of a mile by about one percent. 

60 

some cases, developers have the option to opt in and receive fiscal incentives for doing so (See Stacy _et al._ , 2023, for further descriptions and details). 

There is little doubt that these mandates act as a tax on the of new supply housing. Returning to figure 6 and our simple assignment framework, the builder would like to build dwellings offering _h_<sup>_π_</sup> units of housing services per unit of land in the absence of restrictions. An iz mandate will constrain the builder to devote a fraction _s_<sup>iz</sup> of the new developments to be ‘affordable’ dwellings with each _h_<sup>iz</sup> _< h_<sup>_π_</sup> units of housing services to be sold at a set price _P_<sup>iz</sup> . The cost for the builder is twofold. First, an iz forces the builder to build low-quality units. This is inefficient as land is not put to its highest and best use. Second, these dwellings are also generally sold at a set (or negotiated) price _P_<sup>iz</sup> , which is usually well below the corresponding market rate for such dwellings _P_ ( _h_<sup>_π_</sup> ). While the builder may make a loss on affordable dwellings, _P_<sup>iz</sup> _< C_ ( _h_<sup>iz</sup> ), a multi-dwelling project will remain profitable provided it remains profitable overall. If a housing project gets developed, the main cost is thus perhaps the small inefficiency associated with building low-quality units. else is a transfer from landowners to the of affordable units as Everything buyers housing we expect the reduced profits of the builder to be capitalized in the value of land. 

The main issue is whether such mandates reduce the supply of new housing as the implicit tax makes marginal projects unprofitable so that landowners will no longer sell their parcel for development (or redevelopment) or sell it for another use. Unfortunately, evaluating the effects of iz policies on housing supply is made difficult by the existence of multiple offsets, which are often adjusted after the introduction of an iz mandate. Among others in the literature, Schuetz, Meltzer, and Been (2011) find evidence of an adverse effect on housing supply for an iz mandate in Boston but not for San Francisco. Krimmel and Wang (2024) use a boundary discontinuity approach to show that, in some parts of Seattle, allowing for upzoning combined with an iz requirement led to a large decline in new construction in the treated parts. Less construction should lead to higher prices, a recurring finding in the literature. More subtly, iz aims to change the composition of what is built and should thus affect the entire price schedule _P_ ( _h_ ) in figure 6 through equilibrium effects. With relatively more units in the bulk of the distribution of housing services, we expect to see a decline in (relative) prices in this segment of the market, and following the assignment logic of section 4.2, a decline in prices of all dwellings offering more housing services as well. 

With these difficulties in mind, Soltas (2024 _b_ ) takes a less direct route and estimates instead the net cost of a New York iz mandate fiscal per dwelling City’s voluntary using builders’ responses to several changes in the fiscal exemption granted for new developments with affordable units. He estimates that the fiscal cost of the marginal dwelling under this program is 1.6 million dollars, which is many times the cost of other forms of housing assistance. There is, however, a lot of heterogeneity across neighborhoods, with costs of 

61 

more than two million dollars in parts of Manhattan and less than one-tenth that in many parts of Bronx, Queens, or Staten Island. 

These estimates at the lower end of the fiscal cost of new affordable housing are about the same magnitude as the lifetime undiscounted benefits for a child moving from a low- to a high-opportunity neighborhood as reported in Bergman, Chetty, DeLuca, Hendren, Katz, and Palmer (2024) and building on results from Chetty, Friedman, Hendren, Jones, and Porter (2018).<sup>56</sup> While a complete discussion of this type of externality is beyond our scope, we note that we should expect some equilibrium effects from changes in neighborhood characteristics both where iz residents live and where they are from (or where they would otherwise live). Fogli, Guerrieri, Ponder, and Prato (2024) and Eckert and Kleineberg (2021) examine these issues in a full general equilibrium setting. Unsurprisingly, they find reduced benefits from moving to high-opportunity neighborhoods in general equilibrium. 

Property developers also complain heavily about iz mandates and point to a direct negative effect of the presence of below-market-rate dwellings on the willingness to pay of market-rate buyers. We are not aware of any research about this issue and do not know if the results of Diamond, McQuade, and Qian (2019) about externalities across buildings also apply within buildings. This question is for future research to answer. 

The of externalities the estimation of the effects associated presence complicates price with an expansion of the housing stock. With no externality, any increase in the housing stock in a market leads to lower prices in that market and markets that are gross substitutes. With externalities, prices will also reflect how changes in the housing stock make neighborhoods more or less desirable. Housing prices in a market play two roles: they reflect the scarcity of housing in this market and desirability. The externalities we discuss here are expected to have a spatial decay, but so will supply effects in all likelihood. Hence, it will be challenging to distinguish between the price changes caused by supply effects and price changes caused by external effects. The examples above are cases where increasing the stock of housing increases prices as positive externalities from new constructions dominate the effects of increased Positive externalities a location more are supply. making appealing a with a caveat about distributional effects. It is also the case that arguably good thing, research has focused on situations where improving housing supply led to higher prices to provide evidence about externalities (and likely misses price changes in the market where new residents are coming from). 

The literature that examines the effects of new construction on housing prices generally finds negative effects. In a thorough study of how new apartment buildings affect housing rents in nearby apartment buildings, Asquith, Mast, and Reed (2023) find that a new apartment building lowers nearby rents in similar buildings by 5 to 7%, overwhelming any 

> 56This comparison should not be read as part of a cost-benefit calculation, however crude. The benefits from growing up in a high-opportunity neighborhood are not discounted, and it is not clear that iz dwellings are occupied by residents who would otherwise live in a low-opportunity neighborhood. 

62 

positive externality. Li (2021) finds a similar effect for new residential high-rises in New York City with an elasticity of the price close to -0.1 with evidence of positive spillover effects in the form of new restaurant openings, for instance.<sup>57</sup> The findings of Li (2021) also underscore that the popular perception that new constructions increase rents is likely driven by developers choosing to build where and when prices increase. Pennington (2021) finds again similar results for San Francisco, where new buildings, built (plausibly exogenously) following fire damage, lead to a 1.2-2.3% percent decline in nearby rents. Rents decline despite improving amenities, making (poor) incumbent residents less likely to relocate to another neighborhood. Finally, using German data, Mense (2025) also estimates an elasticity of prices with respect to quantities of about -0.2. This is lower than an elasticity of about -0.5 that we might expect by reverting the supply elasticity found for construction of about 2 for single-family homes in section 3. To explain this gap, we note that the supply elasticity for multifamily housing may be higher, that new constructions generate positive spillovers, and that price effects imperfectly percolate across tiers of the housing market. 

To assess the full effect of changes in housing supply in a market on prices and welfare a everywhere, complete general equilibrium framework is needed to model the direct price effects, the external effects, the effects on other tiers of the same geographic market, and other markets. Owens et al. (2020) show that the uncoordinated shrinking of Detroit is highly inefficient. Some areas with strong fundamentals may get trapped in low equilibrium following a small negative shock and the external effects of the blight that ensue. Builders and residents are unable to coordinate their actions. No resident wants to be first to move into a vacant neighborhood. No developer wants to be first to invest in a vacant neighborhood. Guerrieri, Hartley, and Hurst (2013) also develop a general equilibrium framework to understand gentrification. As richer neighborhoods no longer expand their supply of housing, the arrival of rich newcomers leads to the redevelopment of low-quality housing. Because the presence of rich neighbors nearby is desirable to these newcomers, these redevelopments will take place close to rich neighborhoods and will be spatially highly concentrated, leading to what is commonly known as gentrification. 

In mild cases, the externalities discussed here can lead to inefficient equilibria with, for instance, neighborhoods suffering from insufficient housing maintenance. When these externalities are hyperlocal, they are increasingly handled by homeowners associations (hoas) in the us. Clarke and Freedman (2019) estimate that being part of an hoa leads to a 4% higher price for a house. When these externalities are stronger, they lead to the existence of multiple equilibra and coordination failures. Rossi-Hansberg _et al._ (2010) argue that the housing improvement program they study in Richmond (va) was designed with some awareness of the need to concentrate the intervention spatially. Similarly, Wheeler 

> 57In a different context, Almagro and Domínguez-Iino (2025) provide a detailed estimation of the resorting and changes in amenities following a supply shock. 

63 

(2022) argues that one objective behind the concentration of investments into Opportunity Zones was to resolve coordination failures in blighted neighborhoods. 

# **. 5 Land use and regulatory constraints** 

The literature explored in the previous two sections is mostly about the intensive margin of supply, that is, how the quantity of housing services built responds to demand conditions conditional on development. In this section, we dig deeper into the land development margin. More formally, and returning to the decomposition of housing supply elasticities in equation (10), this section focuses on the elasticity of land development with respect to the price of housing between periods _t_ and _t_<sup>_′_</sup> , _ϵ_<sup>_L_</sup> _P_<sup>(</sup><sup>_t_,</sup><sup>_t′_).58</sup> 

Land availability has received a lot of attention in the literature as a central driver of variation in local housing supply elasticities. In addition to topography and natural features, a central determinant of land availability is land use regulation. For this reason, our discussion of the role of regulatory constraints in this section naturally pairs with our review of the literature on land development. A starting point is the excellent prior handbook chapter on land use regulation (Gyourko and Molloy, 2015), which we only briefly reprise. Since this chapter came out, there is extensive evidence, reviewed in Gyourko and Krimmel (2021) and shown in Figure 5 above, that land use regulations in the us have only become stricter between 2006 and 2018. More restrictive regulation and declines in land availability for development have resulted in generally declining housing supply elasticities over time. Land use planning restrictions have proven very difficult to change once “zoning straitjackets” are established, locking in initial development patterns for decades (Ellickson, 2020). 

## **_.1 5 Bottom-up approaches and the estimation of local supply elasticities_** 

To understand the determinants of the elasticity of land development _ϵ_<sup>_L_</sup> _P_<sup>(</sup><sup>_t_,</sup><sup>_t′_),considera</sup> market _j_ platted with lots of the same size, normalized to 1.<sup>59</sup> Within that market, the fixed cost of land development differs across lots and is described by its probability distribution function, _fj_ ( _x_ ), and its associated cumulative distribution functions, _Fj_ ( _x_ ). As discussed in section 3.1, under perfect competition, land development occurs for all lots with fixed costs below the cutoff _<u>cj</u>_ ( _Pj_ ) at which the parcel price is equal to the price associated with the 

> 58This is the percentage increase in developed land off of base development in period _t_ for a percentage increase in the local housing services price index up to period _t_<sup>_′_</sup> . Because of the irreversibility of land development for urban uses and associated kinked supply, we tend to think only of additional land developed given price increases. As discussed in section 4.1, land will typically not leave its developed state in response to price declines. 

> 59The analysis below goes through with variable lot sizes but is messier. The imposition of minimum lot sizes discussed below is an example of a mechanism through which fixed lot sizes may occur. 

64 

lot’s next best non-urban use _<u>q</u>_<sup>This cutoff is the variable profit given optimal development</sup> _~~j~~_<sup>.</sup> minus the opportunity cost of the marginal lot: 



we the cost function as on the _P_ . The Importantly, express depending indirectly price _j_ resulting fraction of land developed in market _j_ is _Fj_ ( _<u>cj</u>_ ). 

Unsurprisingly, an increase in the price of housing _Pj_ results in more land development since the higher marginal revenue allows builders to afford higher fixed costs. The amount of extra land developed depends on the thickness of the tail of the fixed cost distribution on the margin. A thicker tail, formally a larger _fj_ ( _<u>cj</u>_ )/ _Fj_ ( _<u>cj</u>_ ) leads to more land development given an increase in _Pj_ . In turn, the thicker the tail, the higher the elasticity of land development. 

Baum-Snow and Han (2024) consider the same Cobb-Douglas production function of housing with capital output elasticity _α_ as in equation (15), an opportunity cost of land _<u>q</u>_ _~~j~~_<sup>normalizedto0,andFréchetdistributedfixedcostswithdistributionfunction</sup><sup>_Fj_(</sup><sup>_x_)=</sup> _exp_ ( _−Γjx_<sup>_−λ_</sup> ). Each market _j_ has its own (inverse) scale parameter _Γj >_ 0, but the shape parameter _λ >_ 1 is common to all markets. 

The land development elasticity of market _j_ then takes the form 



where the equalities on the first line hold for any regular production function. With CobbDouglas, the two terms that contain elasticities cancel out to give the expression on the second line, where _ρj_ is a cluster of parameters that is increasing in the productivity of _B_ . housing _j_ 

As the price _Pj_ of housing or its productivity _Bj_ increases, there is a depletion effect of moving further into the thinning tail of the fixed cost distribution, thereby reducing the elasticity of land supply. An empirically observable proxy used by Baum-Snow and Han (2024) is the fraction of already developed land in the market.<sup>60</sup> In contrast, as the Fréchet (inverse) scale parameter _Γj_ rises, the fixed cost distribution for market _j_ has a higher mean and variance, thereby thickening the tail of the fixed cost distribution for any given fixed cost. Possible empirical proxies for _Γj_ include topographical features, such as slope and ruggedness, and observed land use regulations, measured, for example, by the 2006 Wharton Residential Land Use Regulation Index (Baum-Snow and Han, 2024). 

> 60Cosman, Davidoff, and Williams (2018) proposes a dynamic monocentric model with variable marginal land availability with some of the same intuition. 

65 

In equation (42), differences in land supply elasticities across markets follow from differences in prices and differences in the distributions of fixed costs, even given a common underlying housing production technology. Saiz (2010) was the first to formalize the idea that land availability can be a key force regulating housing supply elasticities. Saiz (2010) develops a motivating monocentric model in which the cost of acquiring land for development in a city increases with the unavailability of land in its metropolitan area, thereby generating reduced housing supply elasticities. This land constraint mechanism for generating variation in land supply elasticities is fundamentally the same as that studied through equation (42). 

Saiz (2010) proxies for land unavailability with the fraction of each metropolitan area that has a steep slope of over 15% or is covered by water within 50 kilometers of the central business district, since it is not possible (or extremely hard) to build in such areas. Constraints imposed by geography have also been used in various ways as direct proxies for metropolitan-level supply elasticities, with the idea that housing-demand shocks in more constrained metro areas will result in more rapid price increases due to less elastic housing supply (e.g. Diamond, 2016). 

Estimating housing supply elasticities comes down to relating housing prices and quantities using housing demand shocks as sources of identifying variation while also allowing for land availability and regulation to vary flexibly across markets. The estimation is typically performed for one long first difference. Commensurate with various decompositions of changes in housing quantities discussed in section 2, Baum-Snow and Han (2024) examine the 2000-2010 supply responses of total floorspace and total dwelling units to changes in prices. These responses are decomposed into additive components that come from flows of new constructions on already developed land (redevelopment) ( _∆Sj_<sup>_R>_0,</sup><sup>_∆N_</sup> _j_<sup>_R>_0),other</sup> new constructions ( _∆Sj_<sup>_U>_0,</sup><sup>_∆N_</sup> _j_<sup>_U>_0),teardowns(</sup><sup>_∆S_</sup> _j_<sup>_T<_0,</sup><sup>_∆N_</sup> _j_<sup>_T<_0),andrenovations</sup> ( _∆Sj_<sup>_E_,</sup><sup>_∆N_</sup> _j_<sup>_E_), respectively.For floorspace, this decomposition can be written as</sup> 



The difference between the floorspace elasticity, _∆_ log _Sj_ / _∆_ log _Pj_ , and the land development elasticity, _∆_ log _Lj_ / _∆_ log _Pj_ , yields the intensive margin component of the total housing supply elasticity, _ϵ_<sup>_h_</sup> _P_<sup>(</sup><sup>_t_,</sup><sup>_t′_)in equation (10).</sup> 

Baum-Snow and Han (2024) use microdata on local property assessments compiled by Zillow in the ztrax data set, to measure housing quantities in equation (43) and to construct tract-level housing price indices. For each component of housing supply, including those on both sides of equation (43), they estimate regression equations of the form 



66 

where _∆Q_<sup>_s_</sup> _j_<sup>is a housing quantity change in market</sup><sup>_j_, including the growth rate in floorspace</sup> and its components, the growth rate in dwelling units and its components, and the growth rate in developed land. The vector of variables _Zj_ 2000, which is interacted with the changes in housing prices, _∆Pj_ , contains variables that are either time-invariant (including the distance to the cbd and the local topography) or measured for the base year (the fraction of land developed). The vector _Xj_ 2000 controls for potential supply shifters that should include variables in _Z_ . The estimated vector of coefficients _γ_ ( _Z_ ) is the supply elasticity function. The simplest specification for the interaction is linear in _Z_ . More flexible specifications indexing parameters by one of two latent classes can also be considered.<sup>61</sup> 

The primary identification challenge is to find instruments that affect _∆_ log _Pj_ by shifting housing demand while remaining uncorrelated with the error term _uj_ . That is, these instruments should be orthogonal to the cost of construction and land availability, conditional on controls _X_ . To help identification, Baum-Snow and Han (2024) include metro area fixed effects in the specification. These controls require the identifying variation to come from comparisons between census tracts in the same metro area conditional on the distance to the cbd, topography, and the fraction of developed land.<sup>62</sup> 

A common approach is to use Bartik-style shift-shares as instruments. In the simplest case, the growth of the employment of the national industry, interacted with the shares of local employment by industry, likely predicts the growth in the local demand for housing. However, such a predictor, when computed for metropolitan areas, is collinear with metro area fixed effects and, in their absence, it is unlikely to be orthogonal to the unobserved drivers of land or housing development in regression (44). Rather, Baum-Snow and Han (2024) and Büchler, Ehrlich, and Schöni (2021) use industry shift-share shocks in potential commuting destinations filtered through the commuting time matrix. The idea is that labor demand shocks in labor markets outside of market _j_ generate shocks to housing demand in market _j_ if the former can be accessed from market _j_ through commuting. This approach can be justified with a quantitative spatial model. These housing demand shifters are then interacted with _Z_ to form a full set of instruments.<sup>63</sup> 

In separate reduced-form price and quantity growth regressions, Gorback and Keys (2023) uses foreign investment demand shift-shares across countries of origin as exogenous 

> 61The most flexible specification has _γir_ = _Λ_ ( _Zr_ 1) _Zir_ 2<sup>_µ_1+ (1</sup><sup>_−Λ_(</sup><sup>_Zr_1))</sup><sup>_Z_</sup> _ir_<sup>2</sup><sup>_µ_2,where</sup><sup>_Λ_(</sup><sup>_Zr_1)isthelogit</sup> probability of being in latent class 1, which depends on three variables in _Zr_<sup>2</sup> measured at the metro region _r_ level: the 2006 metro area Wharton Index (wrluri), the fraction of land within 50 kilometers of the cbd that was developed in 2001, and the fraction of space unavailable for development due to steep slopes or water coverage within 50 kilometers of the cbd. _Zir_<sup>2are tract-level measures of cbd distance, the fraction of flat land</sup> area, and a quadratic of the fraction of land area developed in 2001. 

62 Saiz (2010) estimates the inverse of regression (44), which delivers estimates of inverse-supply elasticities for the number of occupied dwellings. Except potentially for the calculation of standard errors, the estimation of equation (44) or its inverse are mathematically equivalent, but they differ econometrically. 

> 63One advantage of the Bartik style approach is that “placebo” checks can be performed by verifying that instruments do not predict changes in quantities or prices prior to the period of study. 

67 

demand shocks, with time variation driven by changes in foreign buyer taxes in countries outside the us. In the reverse regression of (44), Saiz (2010) uses such industry shift-shares along with immigration flows as instruments for quantity growth. 

For empirical settings in which regulation explicitly enters as a supply factor, another identification challenge is to find exogenous variation in such regulation. For this, Saiz (2010) uses the share of the population that belongs to non-traditional Christian denominations, with the idea that this group is more averse to government regulation, and Hilber and Vermeulen (2016) uses a discrete national policy change that lifted some limits on construction as sources of identifying variation. 

Three further issues need to be discussed. First, given the irreversibility of housing investment (Glaeser and Gyourko, 2005), inward housing demand shocks would tend to identify very small housing supply elasticities, as we expect the supply curve to be vertical below the current level of supply. Hence, the identification of supply elasticities requires isolating variation in price growth in equation (44) that is different for inward and outward housing demand shocks. 

Second, the theory developed throughout this chapter has treated a “market” _j_ as a set of dwellings that all face the same demand conditions. In equilibrium, they are perfect demand substitutes, and they face the same equilibrium price per unit of housing services _Pj_ . For this condition to hold, markets must arguably be small. For this reason, Baum-Snow and Han (2024) use us census tracts and Büchler _et al._ (2021) use 2 _×_ 2-kilometer tiles in Switzerland as spatial units of analysis. Under certain aggregation assumptions discussed below, one can rationalize the use of broader spatial units that include areas with different demand conditions. Other work estimating housing supply elasticities uses metropolitan areas (Saiz, 2010, Aastveit, Albuquerque, and Anundsen, 2023), zip codes (Gorback and Keys, 2023), and English local planning authority regions (Hilber and Vermeulen, 2016) as spatial units. 

Third, satellite-based measures of land development are imperfect. The us National Land Cover Database codes each 30 _×_ 30-meter pixel into one of four urbanized categories or one of various unurbanized categories. Urbanized categories are assigned on the basis of the ranges of the percentage of each pixel covered in impervious surfaces. As a result, small changes in land development are usually not observed in these data. This may cause studies this data set to understate land elasticities. As some using development redevelopment occurs on pixels with low levels of initial urbanization, estimated redevelopment elasticities could also be understated. 

All of the studies mentioned above find that more land available for development and less stringent regulations predict more elastic housing supply. Baum-Snow and Han (2024) find that these attributes matter both at the census tract and metropolitan area levels, so that all markets in more highly regulated and land-constrained metropolitan areas are themselves more supply-constrained, even conditional on land unavailability at the tract level. 

68 

Housing supply elasticities have fallen over time. For example, across 237 metro areas, Saiz (2010) finds an average supply elasticity for the number of occupied dwellings of 2.6 (1.6 weighted by the size of metropolitan areas) for the 1970-2000 period. Using Saiz’ methods and price and quantity measures for the 2000-2010 period instead, this number falls to 1.3 (1.1 weighted by metro size) (Baum-Snow and Han, 2024). Using a panel of metropolitan areas, Aastveit _et al._ (2023) finds declining supply elasticities over time of similar magnitudes. For these same metro areas, Baum-Snow and Han (2024) finds a supply elasticity for dwelling units of 0.5 for the 2000-2010 period (0.3 weighted by metro size). For the 2010-2020 period, Gorback and Keys (2023) find elasticities that are smaller by another 10%. Rapidly declining rates of new housing starts, as seen in figures 3 and 5 above, also this evidence of estimated elasticities. A in the fit declining supply key open question literature is to what extent these declines in housing supply elasticities can be attributed to reductions in land available for development (or, equivalently, the selection effect of moving further into the tails of local fixed development cost distributions), increases in land use regulation, and/or something else. In fact, both land unavailability and land use regulation have increased over time. 

Returning to the decompositions in equations (10) and (43), Baum-Snow and Han (2024) finds supply elasticities for average floorspace and the number of dwellings of 0.5 and 0.3, respectively, across all urban neighborhoods in the us. New constructions represent 69% of the supply response for average floorspace and 54% for the number of dwellings. In both cases, the remainder is approximately equally split between reduced teardowns and expansions. 

The average estimated elasticity of land development, _ϵ_<sup>_L_</sup> _P_<sup>(2000, 2010) is about 0.1, and the</sup> intensive margin elasticity _ϵ_<sup>_h_</sup> _P_<sup>(2000, 2010),computedusingequation(10),isthusupto0.4.</sup> The average estimated redevelopment elasticity is very low at 0.03. This tiny elasticity is consistent with the very small housing investment response to rent decontrol in Cambridge (ma) in 1995 documented in Autor, Palmer, and Pathak (2014). It is also consistent with the small changes in densification in New York City following changes in maximum floor-toarea ratios studied by Peng (2023) and discussed above. 

Another striking feature of supply elasticities is that they differ across space within metropolitan areas, actually even more than they vary across metropolitan areas. As redevelopment is estimated to be very costly (as discussed in section 4.1), most housing supply expansions must come on undeveloped land. Moreover, as seen in figure 5, inner suburbs tend to have quite restrictive land use regulations. The result is low floorspace supply elasticities of about 0.1 near cbds, where available land is scarce. These supply elasticities then rise to 0.6 at 25% of the way to the edges of metropolitan areas before inching up further and reaching 0.75 at urban peripheries, where loosely regulated land remains available for development. Similar profiles are seen for the number of dwellings 

69 

and new constructions. 

A difference among the studies discussed above is the time length over which elasticities are measured. Given how slow the redevelopment process is, ten years may not be enough to be considered “long-run”. To go deeper, note that, commensurate with equation (8), a steady state requires: 



where _δT_ is the _T_ year depreciation rate and _A_ is a supply shifter. We then define the long-run supply elasticity from the comparison of two different steady states with price difference _∆_ log _P_ .<sup>64</sup> After solving for the steady state we find the long-run elasticity to be, 



Glaeser and Gyourko (2005) find an annual depreciation rate of 3.5%. Using supply elasticity estimates over 10 years, we have 1 _− δ_ 10 = (1 _−_ 0.035)<sup>10</sup> = 0.7. So, a long-run elasticity is 3.33 times a 10-year elasticity and, by the same logic, 1.5 times a 30-year elasticity. After accounting for the length of time, the relative magnitudes of Saiz-type elasticities discussed above are quite similar for the 1970-2000 and 2000-2010 periods in elastic metropolitan areas but have fallen quickly in the relatively inelastic larger metropolitan areas. 

Spatial aggregation can also matter. Metropolitan areas contain less supply-elastic central areas and more elastic suburbs. If the identifying variation for a metropolitan area is primarily from suburban submarkets, where more land is available for development, the estimated supply elasticity is biased upward. To be more precise, consider regional market _r_ , which aggregates a number of submarket _j_ . The log change of housing supplied in this market can be decomposed as _∆_ log _Hr_ = ∑ _j∈r ωj∆_ log _Hj_ , where _ωj_ are submarket weights that add to one. After replacing for each submarket the change in quantity _∆_ log _Hj_ by the equilibrium response from the change in price, _ϵ_<sup>_H_</sup> _Pj_<sup>_∆_log</sup><sup>_Pj_, we can compute the supply</sup> elasticity for the aggregated regional market _r_ as, 



It is standard to specify _ωj_ = _Hj_ / _Hr_ . If markets are linked in a residential demand system, demand shocks are correlated across markets. In turn, this means that the aggregation of supply elasticities across markets depends crucially on the nature of the underlying demand shock. 

If markets are close substitutes, aggregate elasticities have a natural interpretation as average market elasticities. In the edge case of perfect substitutes, any price change must 

64To help calibrate a model predicting future rent and price growth across housing markets after the rise of work from home, Howard, Liebersohn, and Ozimek (2023) develop these ideas to construct long-run supply elasticities for neighborhoods across the us using decadal estimates from Baum-Snow and Han (2024). 

70 

be the same in all markets. From equation (47), the aggregate elasticity is thus the weighted average of elasticities across markets in _r_ . If markets are segmented, the aggregation is more complicated. The nature of the demand shock matters, and demand shocks that disproportionately hit more elastic market segments will result in elasticity estimates that are greater than the aggregate elasticity.<sup>65</sup> 

Market segmentation also occurs between the owner-occupied and rental markets. Greenwald and Guren (2021) demonstrate that the growth of housing demand driven by shocks to the supply of mortgage credit mostly affects the owner-occupied segment. In turn, these shocks increase the price-to-rent ratio of housing with little effect on the homeownership rate. That is, low aggregate housing supply elasticities can be understood in part through the limited conversion of rental units to Consistent with our discussion owner-occupancy. in section 4.3, housing units do not easily “filter up”.<sup>66</sup> 

After estimating supply elasticities in many markets, it is tempting to use them as instruments to predict housing prices. Davidoff (2015) provides evidence that, indeed, supply elasticities do predict price levels and growth. However, he also shows that supply elasticities are also correlated with the demand for housing. More supply-constrained markets tend to have stronger demand, perhaps because natural features that constrain supply also tend to be positive amenities. Moreover, demand growth tends to beget more stringent land use regulations. Hence, supply elasticities are not good instruments for prices in settings in which the goal is to estimate parameters governing housing or residential demand. 

To avoid this problem, Lutz and Sand (2023) propose the following alternative instrument for house price growth. They train the XGBoost machine learning algorithm for house price growth at the zip code level using predictive features built from satellite-based measures of land unavailability in and around each zip code and its cbsa. This model is trained on 80% of zip codes and is used to predict price growth in the remaining 20%. Repeating the process five times delivers out-of-sample predictions for all areas, which are then bootstrapped four more times. The resulting average predicted price growth at the zip code level can then be used as an instrument for actual price growth. Lutz and Sand (2023) provide evidence that this instrument is not correlated with local demand factors. 

> 65Imagine two equally-sized fully demand-segmented neighborhoods _A_ and _B_ with supply elasticities of 1 and 2, respectively. Neighborhood _A_ is richer, while neighborhood _B_ is poorer with more migrants. An employment shift-share may increase housing prices by 1% in both markets. In response, supply increases by 1% in _A_ and 2% in _B_ . In this case, the aggregate supply elasticity is 1.5. A second source of identification, such as an immigration shock, may boost prices by 2% in market _B_ only, where it leads to a 4% growth in housing supply. In this case, the average price increase is 1%, and the average quantity increase is 2%, resulting in an estimated aggregate supply elasticity of 2. 

> 66Diamond and McQuade (2019) examine the end of rent control in San Francisco in 1994. They find that rental supply was constrained by about 15% as a result of rent control. Some of the ‘disappearing’ rental units nonetheless “filtered up” due to building conversion to owner-occupancy. 

71 

Supply elasticity estimates are commonly used to make predictions about the home price responses to specific demand shocks. Using recently estimated supply elasticities, Davis, Ghent, and Gregory (2024) find that the growth in housing demand associated with the rise of remote work accounts for a large fraction of house price growth after the covid-19 pandemic, Couture, Gaubert, Handbury, and Hurst (2024) characterize the welfare costs of gentrification for incumbent renters, and Favilukis and Van Nieuwerburgh (2021) assess the importance of growth in foreign investor demand in the overall growth in the price of housing. Conclusions in these and other studies depend crucially on the flexibility to allow supply elasticities to be heterogeneous within and/or between different metropolitan areas. 

By definition, housing supply elasticities are aggregate quantities that measure changes over many types of housing markets with widely differing characteristics. The identification of these elasticities often relies on broad-based variation in demand exogenous housing shocks. In turn, these elasticities are determined by both geography and regulations. Separating between both types of effects remains challenging, given that areas with less land available for development tend to have stricter land use regulations. As a result, much remains to be learned from a closer look at how different specific types of regulation influence housing costs and local amenities. The remainder of this section reviews the recent literature on the of land use while of and consequences regulations incorporating conceptualizations evidence of motivations behind their enactment. 

## **_.2 5 Unpacking land use regulations_** 

A central challenge for research on regulation is that land use and real estate development restrictions take many forms. Each municipality’s zoning code is different and requires a unique process to navigate. Even with “as-of-right” developments that do not require zoning variance, developers must typically work closely with city planners to stay within rules that differ between jurisdictions. In many jurisdictions, this involves going through an uncertain, time-consuming, and costly process of permitting, inspection, and environmental reviews. In addition, zoning codes typically prescribe the land available for each specific type of development through zoning designations, and the intensity of development through density restrictions.<sup>67</sup> Then, the fraction of land or properties that require a more arduous process to develop or redevelop varies within each jurisdiction. Additional restrictions, such as requiring historic preservation, banning alcohol sales, or preserving open space, also limit developer flexibility. Development projects that require zoning variances typically must first undergo a series of uncertain reviews that require broad public support to pass, further influencing the time, cost, and probability of success. In all of these ways, stricter regulatory 

> 67Shertzer, Twinam, and Walsh (2018) and McMillen and McDonald (2002) demonstrate that most aspects of Chicago’s original 1923 zoning code and land use planning regime persist to today, durably influencing land use and housing values. 

72 

environments raise developers’ costs, thereby restricting housing supply and reducing its price elasticity. 

Given the many forms of regulations governing land use and real estate development, building succinct and informative summary measures of them is a challenge. As already mentioned, the Wharton Residential Land Use and Regulation Index (wrluri) is the most widely used summary measure encompassing the difficulty of development and restrictiveness of land use regulations.<sup>68</sup> The 2006 version of the wrluri (Gyourko _et al._ , 2008) is derived from a 15 multi-part question survey sent to the 6,896 us municipalities with available contact information listed by the International City Managers Association. The 2,649 responding municipalities tend to be larger, including 62% of the 241 municipalities with a population over 100,000. Only 28% of the 1,969 municipalities with a population under 5,000 responded. 

Eleven sub-indices are calculated to capture the restrictiveness due to approval delays, local political pressure, state political involvement, density restrictions, local project approval, open space requirements, local assembly approval, supply restrictions, exactions, state court involvement, and local zoning approval.<sup>69</sup> For the 2,611 municipalities with sufficient data, these sub-indices are then combined to compute the wrluri as their first factor using factor analysis. The wrluri is highly correlated with the sum of its standardized component indices. Factor loadings on sub-indices are in the same order as listed above, from largest positive to slightly negative. The wrluri is standardized to have a mean of 0 and standard deviation of 1 across the jurisdictions with enough data to compute the wrluri. 

Characterizing the national or metropolitan distribution of regulation requires the use of weights reflecting the probability of being sampled. These weights are constructed as the inverse predicted probability of being in the data from a logit regression of survey return on various municipality characteristics, estimated using the universe of census-designated places. Weighting can be used to correct for the fact that larger and more regulated locations were more likely to be sampled. Indeed, rural municipalities have an average wrluri of -0.46; unincorporated areas, which tend to have the laxest land use regulation, were not surveyed. More regulated municipalities tend to have higher median incomes and housing values and are better educated. The most regulated municipalities also tend to have lower population densities. 

The 2018 wrluri is constructed using a similar set of sub-indexes, with the addition of an affordable housing sub-index, based on survey responses from 2,472 mostly subur- 

> 68 See Jackson (2018) for a discussion of other land use regulation indices that have been used for the us. 

> 69So as to be comparable across municipalities, these questions ask city planners to rate various aspects of the zoning and approval process rather than for details specific to their jurisdictions. For example, one set of questions takes the form “On a scale of 1 to 5, please rate the importance of each of the following factors in regulating the rate of residential development in your community”. Two of the eleven factors subsequently listed are “supply of land” and “density restrictions”. 

73 

ban municipalities (Gyourko and Krimmel, 2021). Factor loadings on each sub-index are somewhat different for 2018, with all of them positive. As the resulting 2018 wrluri is also standardized, the two indices for 2006 and 2018 are not directly comparable, though metropolitan area rankings remain quite stable. Gyourko and Krimmel (2021)’s comparisons of common questions across the two surveys reveal that regulation is stable or increasing over time, with only a few lightly regulated areas as of 2006 that reduced regulation. 

Multiple efforts are currently underway to develop further disaggregated measures of land use regulation. One dimension of disaggregation is in expanding the list of variables used to measure the attributes of a jurisdiction’s zoning code. A further dimension of disaggregation is the partitioning of space within jurisdictions into zoning districts, developing a set of measures for each district. 

Following the first approach, The National Zoning Atlas project (Bronin, Markley, Fader, and Derickson, 2023) is in the process of painstakingly coding up a set of consistent variables by carefully reading zoning codes from multiple jurisdictions, with teams of researchers assigned to read municipalities’ zoning codes in different regions around the us toward this goal. This effort nationalizes the prior Pioneer Institute initiative in 2004 to consistently code the zoning codes of 187 municipalities in the Greater Boston area (Glaeser and Ward, 2009). 

Such manually coded data sets can be used as training data in the development of large language models (artificial intelligence) to automate the reading of zoning codes. The advantage is scalability, though it potentially comes with some loss of accuracy. For example, Bartik, Gupta, and Milo (2024) uses a large language model trained on the Pioneer Institute data and verified against elements of the 2018 wrluri to predict key aspects of the zoning code for 25% of us municipalities, covering 63% of the us population. The analysis feeds each municipality’s zoning code into a trained large language model (OpenAI GPT-4) and asks the same survey questions as in the Pioneer Institute study. This study then relates local supply growth to aspects of local zoning codes. 

Echoing the evidence in Baum-Snow (2023) and Burchfield _et al._ (2006), Bartik _et al._ (2024) find that a disproportionate amount of new housing development is greenfield development in unincorporated exurbs. Incorporated locales restrict densities through minimum lot size restrictions and bans on multifamily housing at very high rates. Two-thirds of incorporated locales have minimum lot sizes of at least 5,000 square feet and only 31% of the land area is zoned for multifamily housing. Using the AI-generated answers to questions about the zoning code as inputs, Bartik _et al._ (2024) undertake a revealing principal components analysis to draw out central attributes of zoning codes. The first principal component reflects regulatory complexity, which increases developers’ fixed costs. This attribute of zoning codes is more prevalent in higher-density areas of central municipalities. The second principal component encompasses policies that restrict development or exclusionary zoning. 

74 

This attribute is more prevalent in high-income suburban areas.<sup>70</sup> 

As real estate restrictions are so studies focus on development heterogeneous, many recovering the consequences of one common type of zoning restriction. In addition to maximum floor-to-area ratios explored in section 3.5, which are prevalent around the world, one very common regulation in the us is minimum lot size (mls) zoning. Zabel and Dalton (2011) pioneered the idea of automating the measurement of local mls restrictions using the modes of observed lot size distributions or equivalently by isolating the lot size at which the distribution function in each jurisdiction exhibits a structural break. This study shows a positive relationship between these inferred mls and property prices in Eastern Massachusetts. Song (2024) hones this method to characterize the distribution of mls restrictions in zoning districts across the us. She finds that for the 16,217 municipalities for which mls regulations can be inferred, the mean mls is 0.37 acres (16,000 sq ft), and 75% of a mls of at least one acre in at least one district or census municipalities impose zoning block group. 

One fruitful to summarize the of mls constraints demand condi- way stringency given tions, without even having to measure minimum lot sizes directly, is through the calculation of “regulatory taxes” (Glaeser and Gyourko, 2018). The idea is to compare the hedonic prices of a marginal unit of land as viewed by builders and homeowners. If the value of a unit of land to a homeowner is below its value to builders, we would expect the homeowner to subdivide and sell off part of her lot through a standard no-arbitrage argument. As a result, the greater the gap between the price of vacant and built-up land, _ceteris paribus_ , the greater the regulatory distortion that prevents this arbitrage. 

Using data on vacant land sales for development into single-family homes from CoStar and property transactions data from CoreLogic, Gyourko and Krimmel (2021) carry out a comprehensive analysis of regulatory taxes for 24 large us metropolitan areas. The study uses standard hedonic methods to recover homeowners’ implicit marginal willingness to pay for land by us metropolitan area. The study period is 2013-2018. Their results indicate regulatory taxes of 400,000 dollars per half-acre in San Francisco, 150,000-200,000 dollars per half-acre in New York, Los Angeles, and Seattle, and smaller numbers for other markets studied. Relatively elastic housing supply cities, including Atlanta, Charlotte, Dallas, and Cincinnati, are found to have very small regulatory taxes.<sup>71</sup> 

> 70In related work, Shanks (2021) uses the Latent Dirichlet Allocation unsupervised learning procedure to assign each municipality in Massachusetts zoning code probabilities of membership in various clusters generated based on the prevalence of various words in the zoning code, with three clusters chosen ex-ante. Using simpler keyword-based natural language processing on zoning codes in most 2006 wrluri municipalities to roughly replicate wrluri sub-indices, Mleczko and Desmond (2023) also construct an alternative zoning index. 

71In the same spirit is Duranton and Puga’s 2023 identification of highly regulated metro areas by looking at property values at urban fringes. At the upper end, their estimated values are close to those of Gyourko and Krimmel (2021). 

75 

## **_. 5 3 Estimating the consequences of land use regulation: border discontinuity approaches_** 

Land use restrictions generate winners and losers. Restrictive land use regulations reduce the option value of development by limiting the production of housing services from a parcel. However, restrictive regulations also protect against nearby developments and their potential external costs. This external effect follows the classic compensating differentials logic for local amenities, as in Roback (1982). In addition, restrictive regulations reduce aggregate supply and thus also increase property values through this channel. 

Because of their effect on property values, land use regulations are likely to reflect voter interests and, therefore, be endogenous to demand conditions. As a result, credible studies of the impacts of land use regulations require the use of identifying variation in land use regulation that is orthogonal to demand conditions. To resolve this endogeneity problem, one arguably credible identification strategy is to make comparisons across zoning districts at small spatial scales for which demand conditions are the same, a boundary discontinuity approach. 

In an important paper, Turner, Haughwout, and Van Der Klaauw (2014) exploit discontinuous changes in land use regulations across municipal boundaries to recover the effects of these regulations on the values of undeveloped lots. When crossing a boundary between two jurisdictions, the regulation changes but, right at the boundary, the existing or expected built environment is approximately the same on either side. Hence, the discontinuity in land values at the boundary primarily reflects how stricter land use regulations reduce the option value of of a which call the “own-lot effect”. As are development parcel, they developers assumed to be competitive, the full foregone value associated with restricting development gets capitalized into reduced land values rather than reduced developer profits, following the logic of equation (13) derived in section 3.1. 

While the “external effect” resulting from the regulation of nearby properties on land values is approximately the same at the boundary, exposure to stricter or less strict regulations changes as we move inside each jurisdiction. Hence, the comparison of land values within a jurisdiction between parcels close to the boundary and those far from the boundary, which are subject to the same own-lot effect, can thus isolate the external effect of land use regulations. 

Conceptually, stricter land use regulations can have ambiguous effects on land values. They are expected to reduce the option value of development (negative own-lot effect) but increase amenity values from regulations on other parcels (positive external effects). Through the “supply effect”, stricter land use regulations also contribute positively to land values. Using data on vacant land sales mostly from peripheries of us metropolitan areas, Turner _et al._ (2014) estimate an own-lot effect of minus one-third of value per standard deviation increase in the 2006 wrluri and an imprecise and much smaller external effect. With negligible estimated supply effects, the conclusion is that land use regulations reduce 

76 

land values. Of course, the magnitude of the supply effect in practice depends on the spatial reach of land use regulation within the market. 

Negative estimates for own-lot effects provide direct evidence that mls zoning constrains development. Using equation (16) with Cobb-Douglas housing production, the elasticity _<u>β</u>_ of housing services and property value with respect to lot size is 1 _−α_<sup>_≈_1,reflecting</sup> approximately constant returns to scale. Holding the supply and external effects constant, the elasticity of parcel value per unit of land with respect to lot size would thus be approximately 0, given small fixed development costs and no constraints on development. A negative estimated own-lot effect thus means that capital intensity, or the quantity of structure built per unit of land, is constrained to decline in lot size. This decline likely reflects developers’ optimal responses to prohibiting the construction of additional dwelling units on larger lots. 

Given this negative own-lot capitalization effect, it is worth considering why minimum lot size mls regulations exist. One possibility is that the supply effect is large enough that laxer land use regulation drives down land values through general equilibrium forces, thereby incentivizing property owners to support them. This logic is considered in Section 6. In addition, negative externalities may be large enough in some circumstances to outweigh the increase in real option values from the own-lot effect as regulations are relaxed. There is evidence, discussed below, that negative external effects of dwelling unit density may be larger and own-lot effects smaller in already built-up neighborhoods than in the undeveloped areas studied in Turner _et al._ (2014). Costly redevelopment limits the option value of already developed parcels. Moreover, the external effects of increased development in already built-up areas are current, whereas those in unbuilt areas mostly reflect future spillovers that are discounted back to the present. 

More recent studies use boundary discontinuity approaches to estimate own-lot, external, and supply effects for developed properties rather than vacant land. The use of developed properties has the advantage of covering a much wider and more representative range of contexts and locations. There is also the of more disadvantage challenging identification given potential unobserved heterogeneity in developed properties. Regressions like the following, using a sample of home transactions of properties close to zoning boundaries with boundary fixed effects, underlie this evidence. 



Equation (48) describes a regression in which the dependent variable is the log of the transaction price of home _i_ in zoning district _j_ at time _t_ , log ( _Pjthijt_ ). The explanatory variable of interest is the log of minimum lot size, log mls _jt_ . The estimated coefficient, _κ_<sup>mls</sup> , captures the impact of the regulation on the total value of housing services on each lot. The regression further conditions out boundary fixed effects, _ρb_ ( _i_ ), and municipality-time fixed effects, _λm_ ( _j_ ) _t_ . Boundary fixed effects control for location and local neighborhood amenities. 

77 

Boundary distance and/or local demographic controls are sometimes also included to improve accounting for such factors. Municipality-time fixed effects _λm_ ( _j_ ) _t_ control for local public goods and finances. Some studies must leave these out, as they only have more aggregated data with one observation per jurisdiction. 

Using regressions in the spirit of equation (48), Song (2024), Kulka, Sood, and Chiumenti (2022), and Gyourko and McCulloch (2024) all find that more binding mls regulations increase average dwelling unit prices and rents. Song (2024) finds that doubling the mls increases dwelling prices by 14% and rents by 9% using data from across the us. Using data from Massachusetts, Kulka _et al._ (2022) find similar estimates. In addition, they find that mls increases dwelling unit size, with an estimated floorspace elasticity with respect to mls of about 0.25, and reduces dwelling unit density. Looking across municipal borders, Gyourko and McCulloch (2024) find price elasticities of mls of about 0.27 for single-family homes.<sup>72</sup> If developers were unconstrained, the price elasticity would be one. 

Positive estimates of _κ_<sup>mls</sup> reflect a combination of differences in prices and quantities of housing services. By adding property characteristics and lot size to equation (48), Song (2024) finds that the coefficient on log mls declines by about three-quarters, indicating that quantities account for at least three-quarters of the effect. Residual price effects could occur due to (likely small) differences in local amenities across zoning district boundaries or unobserved housing quality differences. 

This evidence of positive property value and housing quantity effects along with Turner _et al._ ’s (2014) evidence of negative own-lot effects for land echoes earlier cross-sectional results in Ihlanfeldt (2007), finding own-let, external, and dwelling size responses to stricter land use regulation using data from 100 Florida cities. Been, Ellen, Gedal, Glaeser, and McCabe (2016) analyze the impact of historic preservation districts in New York City. They uncover positive property transaction price responses within these districts and just outside for outer boroughs where the option values of redevelopment are lower because of lower demand. These districts are local amenities but they also restrict redevelopment.<sup>73</sup> 

The main goal in Gyourko and McCulloch (2024) is to estimate the external effects of density, or the willingness to pay for lower density by different types of households. They propose a hedonic regression like in equation (48) that additionally controls for own-lot property characteristics and replaces log mls _jt_ with a flexible function of dwelling density within 500 meters of the focal dwelling unit _i_ . Differentiating the estimated dwelling density function reveals that residents are willing to pay a mean of 9,500 dollars to avoid an 

> 72More precisely, across boundaries for 2018 wrluri municipalities, Gyourko and McCulloch (2024) estimate average differences in mls of about 3,000 squared feet on a mean of 12,574 and in sales prices of about 30,000 dollars on a mean of 469,000 dollars. 

> 73In a similar empirical setting, Kahn, Vaughn, and Zasloff (2010) and Severen and Plantinga (2018) study the California Coastal Act of 1976, which restricts additional property development on a strip of land adjacent to the Pacific coast. Comparing property sales and rents across the boundary that defines the restricted region, these papers both find evidence that this regulation improves local amenities. 

78 

additional dwelling unit per two acres of surrounding land, with this amount increasing in magnitude with neighborhood income. Indeed, heterogeneity in the marginal willingness to for low matters for motivations to limit Sahn pay density really understanding density. (2021) and Cui (2024) provide evidence that many mls restrictions were enacted with exclusionary racial motives, which may also reflect exclusionary income-based motives. This is consistent with the pervasive evidence of negative external effects from neighbors with lower income and education and of other races (Bayer, Ferreira, and McMillan, 2007, Diamond _et al._ , 2019, Almagro, Chyn, and Stuart, 2023). Residents’ concerns about negative externalities can influence regulations, which in turn influence supply conditions. Kulka (2019) demonstrates that higher-income households sort into areas with larger minimum lot sizes, also consistent with an exclusionary motive for their enactment. 

There is less work using boundary discontinuity research designs to measure the supply effect. Doing so requires combining estimates of the impacts of regulation on housing quantities with a model that has sufficient structure to allow for recovery of welfare consequences. Anagol, Ferreira, and Rexer (2025) carries out such an exercise, using the 2016 relaxation of density constraints in various neighborhoods in Sao Paolo, Brazil, as a source of exogenous variation in supply. Sao Paolo is a good setting for this as strong demand means that many neighborhoods face binding constraints regarding maximal allowed construction. In areas where regulations were relaxed, there was a large supply response. As areas experiencing no change in regulation were already mostly built to the maximum density and experienced no change in construction with the implementation of this policy, there is little possibility that new construction in newly deregulated areas came from substitution across zoning district boundaries. Through the lens of a quantitative spatial equilibrium model of Sao Paolo’s housing markets estimated in part using the identifying variation from boundary discontinuities, the authors find large housing wealth transfers from current to future homeowners, with a net welfare gain of 0.76%. This loss in value for current homeowners, a theme we return to in Section 6, helps explain the opposition of homeowners to relaxing land use and density restrictions. 

## **_5.4 Urban growth boundaries_** 

Urban growth boundaries (ugbs), also known as green belts, are a common restriction on land use. They prevent any new development beyond a specified urban fringe. Many English cities, Toronto, Vancouver, Portland (or), Minneapolis-St Paul, Miami, Seattle, and most Chinese cities, impose some form of ugb. As the elasticities for redevelopment and infill are very low, the increased scarcity of large tracts of undeveloped land in desirable locations in markets with binding ugbs contributes to their weaker supply responses to demand growth and higher housing costs. 

79 

In early work, Cunningham (2007) provides evidence that the area around Seattle’s ugb, imposed in 1995, experienced less development on net. However, since the ugb was expected up to five years in advance, it also initially reduced the real option value of waiting to develop land beyond the boundary (as per our discussion in section 4.1). While the Seattle ugb eventually reduced new developments beyond the boundary, it nonetheless accelerated them during the period between its announcement and its implementation. ugbs can increase local amenities by preserving open space and reducing negative traffic externalities, given that higher-density cities have less aggregate travel (Ewing and Cervero, 2010, Duranton and Turner, 2018).<sup>74</sup> As each ugb affects the equilibrium of its entire housing market, quantitative spatial equilibrium models, similar to those discussed in Redding (2025) in this volume, can be used to perform welfare analysis. 

Using such a model, Koster (2024) reports quantitative evidence that in the English case, ugbs have large positive external effects. Using various identification strategies, he finds that being in a greenbelt raises house prices by about 12%, which is naturally interpreted as reflecting the amenity advantages of access to open space. In addition, the housing stock is much lower in greenbelts. A counterfactual of this quantitative spatial model developed and estimated for England in which all greenbelts are removed reveals that improved housing would not be to the associated reduction in consumer affordability large enough outweigh amenities. Central to this conclusion is that the capital share in housing production ( _α_ from section 3) is greater than 0.55, which means that existing residentially zoned land can be built more densely at a sufficiently low cost. Another caveat is that Koster (2024) estimates an extremely high distaste by residents for commuting, which limits the benefits of urban expansion. In contrast, the amenity value of greenbelts decays only slowly with distance. ugbs. This study also finds little role for productivity effects of 

Yu (2024) draws the opposite conclusion about the welfare consequences of a similar type of land use restriction that was imposed on Chinese cities in 1999. This restriction requires cities to maintain a constant stock of farmland nearby. As a result, each reclassification of land from rural to urban, which facilitates urban expansion, requires converting an equal amount of nominally urbanized land to farmland. While these are not strictly speaking ugbs, this restriction imposes a similar type of development constraint. This constraint is useful for empirical work because it varies across cities by the prevalence of rugged land at the urban fringe. Difference-in-differences evidence demonstrates that these development constraints reduce city population and gdp, raise prices, reduce productivity, and ultimately, through the lens of a quantitative model, reduce the welfare of workers. They also lead 

74There is a long-standing debate in urban economics about the role of land use restrictions, and in particular ugbs as a second-best instrument to mitigate the effects of traffic congestion (Pines and Sadka, 1985, Anas and Rhee, 2006, Anas and Pines, 2008). Brueckner (2007)’s calibrations of a monocentric model with endogenous congestion indicate that a ugb is a vastly inferior second-best alternative to optimal congestion pricing for internalizing congestion externalities. 

80 

to aggregate land misallocation, a cost of land use restrictions to which we return in the following section. 

## **_. 5 5 Evidence from upzoning_** 

Commensurate with the boundary discontinuity evidence discussed above, a number of additional studies use cross-sectional or panel variation across us jurisdictions to provide evidence that stricter land use regulation reduces new construction and/or increases housing costs (Mayer and Somerville, 2000, Quigley and Raphael, 2005, Kok, Monkkonen, and Quigley, 2014, Jackson, 2016). Episodes of large-scale upzoning in individual cities provide additional evidence to corroborate these observational studies. 

An empirical challenge in looking at such large-scale events is that general equilibrium effects generate spillovers from treated to potential control areas. As a result, comparison regions within the same city or metro area do not really exist. As upzoning typically happens in unique ways, it is also difficult to find valid counterfactual areas in other housing markets. This leaves a role for the use of set identification restrictions and/or quantitative modeling to assess upzoning’s impacts. Moreover, construction and price responses to upzoning depend, of course, on the details. Changes in zoning regimes that give more development flexibility will have more significant impacts. 

Greenaway-McGrevy and Phillips (2023) examines the impacts of the 2016 upzoning of three-quarters of the residential land in Auckland, New Zealand. While various changes in land use restrictions were implemented, a binary upzoning treatment is defined from the increases in the maximum allowed floor-to-area ratio. This study defines this treatment to be assigned at the New Zealand Statistical Area level, similar to us census tracts. The number of new building permits requested as a result of the upzoning represented 4% of the aggregate dwelling stock. It is implausible that this response was driven by substitution from areas that were not upzoned to upzoned areas. This study follows evidence in Greenaway-McGrevy, Pacheco, and Sorensen (2021) that upzoning primarily increased the values of underdeveloped properties, for which the option value of redevelopment increased the most.<sup>75</sup> 

Various us cities and states have recently become more involved in requiring municipalities to allow denser housing development. For example, Massachusetts’ 2021 “mbta Communities Law” compels municipalities who have not done so to establish zoning districts with multi-family housing development allowed “as of right” with densities of at least 

> 75Since 2009, the city of Minneapolis has undertaken several large-scale upzoning initiatives, including in single-family home neighborhoods and eliminating minimum parking requirements. While identification is more difficult in this Minneapolis case, evidence is a large development response, less rapid rent growth, and more rapid price growth for single-family homes, especially in lower-income neighborhoods. The latter price growth likely reflects the own-lot effect and the increased values of redevelopment options (Kuhlmann, 2021, Liang, Staveski, and Horowitz, 2024). 

81 

15 units per acre within 0.5 miles of a transit station. Municipalities that do not comply lose state infrastructure funding. Nonetheless, the high-income communities of Milton and Needham have voted to reject the rezoning proposals that meet this upzoning requirement.<sup>76</sup> 

One common upzoning policy is to require municipalities to allow accessory dwelling units (adus), additional small housing units added to existing properties. The state of California now requires all municipalities to allow the construction of adus with expedited permitting. As it is small in scale, this type of gentle densification is less likely to raise political opposition, as in the Massachusetts transit-oriented development example. Davidoff _et al._ (2022) examines the effects of the 2009 law that allowed adus (in the form of laneway homes) in 95% of single-family zoned areas in Vancouver, Canada. Interestingly, this study finds no “own-lot” effects of new laneway homes. In the Vancouver context, it seems that the construction cost of laneway homes is about the same as the present value of their net operating income. These units are so small that the fixed costs of development apparently make them poor investments. It is no wonder that there have not been many adu constructions after this law change. These adus are found to impart negative externalities on neighboring properties, as measured through hedonic price responses. Negative capitalization is about 2.5% of value for the priciest quartile of neighboring homes but near zero for the lowest value quartile. 

While the potential benefits from upzoning are arguably more significant for cities in developing economies, only a few studies examine such episodes. Gechter and Tsivanidis (2023) examines the redevelopment of the Mumbai Mills district, which covers 15% of the central area of Mumbai. These 60 textile mills were mostly replaced with high-rise residential and commercial developments, representing a large increase in Mumbai’s housing supply. The surrounding slum areas were not upzoned but could be redeveloped, with some compensation paid to incumbent residents. This study finds large positive externalities from the mills’ redevelopment, with property values increasing and slum redevelopment displacing low-income residents in adjacent neighborhoods. In the context of a quantitative spatial model, these responses can be rationalized with endogenous local amenities that positively depend on the skills mix of nearby residents. Overall, this redevelopment benefited high-skilled city residents who gained from increased housing supply and affordability at the of some low-skilled incumbent residents near the expense (displaced) redeveloped mills. This evidence of the gentrification cost of large-scale development in low-income neighborhoods perhaps helps to explain the opposition to neighborhood redevelopment seen in many contexts. 

> 76 `https://www.mass.gov/info-details/mbta-communities-law-qa` . The Canadian province of Ontario is one of the few jurisdictions in North America in which a high level of government can rule on specific development applications. The appointed Ontario Land Tribunal and its predecessors have overruled many local planning decisions, even for proposed developments that violate municipal zoning codes. This has contributed to the city of Toronto’s 4.9% annualized growth rate in dwellings in multifamily buildings over 2001-2021, far outpacing that for large us cities (ab Iorwerth, Baum-Snow, and Macek, 2025). 

82 

## **_5.6 Property taxation and the political economy of land use regulation_** 

We have seen how property owners have several motivations to restrict development and densification. Adverse external effects of density reduce local amenities, incentivizing property owners to resist and limit nearby development. Such negative spillovers can be greater in high-income neighborhoods. These are negative “external effects” in the language of Turner _et al._ (2014). However, “own-lot” effects incentivize owners of vacant land to oppose land use restrictions provided that the countervailing “supply effects” are not too large. 

Zoning rules are often set at the local level. In the us, zoning decisions are nominally made at the municipality level, although in practice even more local interests often dominate. For example, “aldermanic privilege” in Chicago means that almost all zoning proposals must receive the support of the local city alderman to be implemented. As the interests of local owner-occupants, renters, absentee landlords, and absentee owners of vacant land or properties ripe for redevelopment usually do not align, the interest group with the most political power often influences zoning rules and development approvals at the expense of some other groups. For this reason, areas of large cities that have many renters tend to be more at least for subsidized than suburbs that are development-friendly, housing, built-up households. Unbuilt areas at urban overwhelmingly populated by owner-occupant fringes with a lot of vacant land also tend to be development-friendly, given own-lot considerations.<sup>77</sup> 

Hilber and Robert-Nicoud (2013) is one attempt to conceptualize how two of these competing interests can lead to variation in development restrictions across locations. This study considers a game played by resident owners of developed properties and absentee owners of vacant land in a system of jurisdictions in which each jurisdiction makes its own decision about development restrictions. These two players have opposite incentives to advocate for land use regulation. The supply effect incentivizes developed property owners to support higher regulatory taxes (Glaeser _et al._ , 2005 _b_ , Glaeser and Gyourko, 2018) while the own-lot effect incentivizes owners of undeveloped land to oppose them. These two players influence the planning board by “bribing” them proportionately to aggregate gains or losses in property value associated with enacted regulatory taxes. In equilibrium, the planning board chooses regulation to maximize total land rents plus regulatory taxes, which only involves a choice of nonzero taxes because jurisdictions compete for residents. Locations in high residential demand (because of good amenities, for example) get more built in to less land and up equilibrium, thereby leading undeveloped higher regulation. This pattern is also observed in the data across us metropolitan areas. 

> 77Developers’ interests matter as well. Using a regression discontinuity empirical design for close elections, Yu (2022) finds that residential developers who donate to candidates elected mayor develop more housing. 

83 

The observation that strategic interactions across municipalities inhibit housing development is also supported by quasi-experimental evidence. Looking at forced amalgamations of municipalities of less than 5,000 inhabitants in France after 2010, Tricaud (2025) finds, in a difference-in-differences empirical setup, that construction permits increase by 12.5% in forcibly amalgamated municipalities. However, no such increase occurs after voluntary consolidation. Moreover, more urban municipalities that were amalgamated and had the greatest construction response experienced no change and housing values and, if anything, improvements in public services. Tricaud (2025) takes this as evidence that resistance to amalgamation was primarily about residents’ concerns about negative externalities from new housing development rather than about negative capitalization effects or reductions in the quality of local public goods. Mast (2024) demonstrates that us municipalities that move from at-large to ward-based representation in their city council reduce the number of approved permits for new housing units by 20%. Consistent with the idea that higher-income homeowners are most resistant to new are in development, responses larger high-income jurisdictions. 

When it comes to decisions about local land use restrictions, property taxes also play an important role. So does the quality of local public goods provision, including schools, parks, and police. Decisions about zoning, property taxes, and local public goods are typically made jointly. A line of thinking going back to Tiebout (1956) concludes that property taxes are not distortionary if they are used to fund local public goods. Households with heterogeneous demand for local public goods “vote with their feet” to live in the jurisdiction that is for them. This view does not consider or right explicitly zoning, housing supply, within-jurisdiction resident heterogeneity. However, standard logic from public economics is that taxation of elastically supplied capital (or structures) is distortionary (Harberger, 1954) and leads to an inefficiently small capital share in housing provision. For this reason, the “Henry George Theorem” states that property taxes should only be on the land component of housing, as the fixed supply of land means that such taxes are not distortionary.<sup>78</sup> 

Building on this Georgian idea, Hamilton (1975, 1976) articulates a positive role for land use regulation. Imagine an environment, as is standard, in which the provision of the local public good to each household has the same cost to the local government. A result extending back to Oates (1972) is that identical head taxes efficiently fund the provision of public goods. However, head taxes are not an option in most jurisdictions, which must fund operations using proportional property taxes. If properties are heterogeneous in value, under proportional property taxation, low-value properties pay less in tax and are 

> 78Given the common reality of fixed lot sizes, this logic clearly holds. With variable lot sizes, it only holds if there are no density externalities. Separate taxation of land and structure is common in Eastern Europe. In the us, Allegheny County (pa) used to assess the two separately. See also Behrens, Kanemoto, and Murata (2015) for the genesis of the modern versions of the Henry George Theorem, key references, and some limitations of the mechanism. 

84 

subsidized by the taxes levied on high-value properties. By stipulating that all properties in a community must be identical, zoning can eliminate this fiscal externality. That is, under a second-best environment in which head taxes are not possible, zoning can manipulate the built environment so that property taxes replicate head taxes. Brueckner (2023) formalizes these ideas, demonstrating efficiency with pre-zoned communities. However, inefficiencies arise if households can choose the amount of housing to consume/build for themselves. 

These ideas are developed further in the computational multi-community model with household heterogeneity developed by Calabrese, Epple, and Romano (2007). This model proceeds as a three-stage game. Households first buy land in one community. In the second stage, they choose the property tax rate and minimum housing requirement by majority vote. In the final stage, they relocate or adjust land holdings, build housing on their land, pay taxes, and consume. This timing structure skirts the problem of jointly determining an equilibrium community composition together with a zoning and taxation regime. The model analytically delivers endogenous equilibrium zoning in all but the lowest-income jurisdiction. Computationally, equilibrium zoning is very stringent but welfare-enhancing relative to an environment in which zoning is prohibited. However, zoning also induces stratification across communities, increasing inequality. Low-income households are zoned out of richer communities (“exclusionary zoning”) and are left with a low tax base and lowquality local public goods. Zoning eliminates the negative jurisdictional choice externality that the would if were able to a small amount of in a richer poor impose they buy housing community, However, it saddles them with lower-quality public goods.<sup>79</sup> As we discuss further in section 6, zoning in one jurisdiction can raise housing costs in other jurisdictions through aggregate land constraints. 

Fischel (2001) recasts this logic into a framework in which property owners vote to maximize the value of their own properties, the “homevoter hypothesis”. Given that areas are built up, this means enacting rules that limit negative externalities across properties. For these reasons, Fischel (2001)’s view is that “zoning is an essential ingredient of municipal formation and function”. Several studies evidence that owners empirical provide property vote to raise property taxes if it increases their property values in the context of vouchers for private schools and the construction of nearby stadiums (Brunner, Sonstelie, and Thayer, 2001, Brunner and Sonstelie, 2003, Dehring, Depken II, and Ward, 2008). Hilber and Mayer (2009) document that school spending is higher in districts with less vacant land, consistent with the idea that municipalities with less elastic housing supply are more incentivized to tax themselves to support local public goods. These taxes only pay off in higher property 

> 79Barseghyan and Coate (2016) develop a dynamic model with household income heterogeneity, two communities, and two possible home sizes with similar analytical conclusions. We also note that zoning regimes have been found to target racial exclusion. For example, when Chicago established its first zoning code in 1923, the city assigned industrial zoning to minority residential areas much more than to White areas (Shertzer, Twinam, and Walsh, 2016). 

85 

values if zoning rules restrict free-riding and reduce externalities across properties. 

Relatedly, Krimmel (2021) demonstrates how stricter zoning has been used to guard against the congestion of local public goods when municipalities lose control over property tax rates. After a reduction in California that came with municipalities’ taxing power school finance equalization in the 1970s, he shows that municipalities enacted stricter zoning regimes. These regimes required larger lots and more housing services per dwelling, thereby limiting the entry of new students into local school districts, with stronger such zoning responses in higher-spending localities. 

Still, in the spirit of the Henry George Theorem, property taxes can also fund local infrastructure like roads and transit. As infrastructure typically results in increases in property values through capitalization, a commonly proposed taxing model is “value capture”, in which capital gains that accrue because of new publicly provided infrastructure are taxed to fund it. For example, Gupta, Van Nieuwerburgh, and Kontokosta (2022) find that New York City’s 2nd Avenue subway construction could have been fully funded with full value capture. Given current tax rates, however, additional associated property tax revenue implied by this extension of the subway will be well below its construction cost. 

As property taxation funds most local services in the us, interesting political economy dynamics across levels of government ensue, with implications for housing supply. California’s Proposition 13, enacted in 1978, limits property taxes to 1% of assessed value and allows municipalities to raise assessed values by at most 2% per year on incumbent property owners. However, properties with new owners or that are new construction can be re-assessed to market values. Proposition 13 is thus a form of enforced centralization, in which some fiscal responsibility for local service provision is uploaded from municipalities to the state. Increases in property prices thus imply increases in the implicit cost of moving, which should lower mobility rates.<sup>80</sup> With higher property prices, there is also a related increase in the implicit cost of buying new homes, given that they come with higher property taxes and a disincentive for property redevelopment. The literature has not systematically examined the housing supply response to Proposition 13 to date. 

## **_5.7 Taxation and housing policy_** 

In addition to property taxes, common housing tax instruments include transfer taxes (stamp duties), which are usually levied on buyers and set to be progressive in the sales price, and capital gains taxes, which are also levied after transactions but are paid by sellers. Some countries also allow some tax filers to deduct mortgage interest from their tax liability and/or offer various tax incentives for home buying. Finally, there are tax subsidies for developers to build or renovate subsidized housing. In the us, the main program in this 

> 80In practice, there is mixed evidence on the mobility response to this law (Ferreira, 2010, ˙Imrohoro˘glu, Matoba, and Tüzel, 2018). 

86 

category is the Low Income Housing Tax Credit (lihtc). Newly constructed or renovated housing units subsidized through the lihtc program are subject to capped rents for at least 15 years and can only be rented to households with incomes below thresholds that depend on area median incomes. 

Transfer taxes (stamp duties) are universal in the United Kingdom and much of the Commonwealth, including Canada and Australia. They also exist in many European countries, and most us states. By disincentivizing housing transactions, these taxes can generate misallocation of households to dwelling units. The associated additional cost of moving may be expected to keep small families in large homes for longer, disincentivize moves across labor markets to look for and accept better employment opportunities and reduce the supply of potential movers into newly constructed dwellings. The reason is that some housing transactions that would be mutually agreeable to buyers and sellers absent the tax do not generate sufficient surplus to cover the cost of the tax. The result is reduced liquidity in the housing market. 

The existing literature on land transfer taxes finds sizable effects of such taxes on the number and pricing of transactions. Using variation in uk stamp duty schedules from changes that occurred over the 2003-2013 period, Best and Kleven (2018) uncover various pieces of evidence to this effect. Sharp increases in tax rates at each of five different price thresholds, meaning that buyers pay thousands of pounds more in tax for a one pound higher sales price, also facilitate identification of impacts of this tax.<sup>81</sup> These notches generate missing masses in the sales price distribution and bunching at just under the price threshold associated with each notch in the tax schedule. Bunching estimates in Best and Kleven (2018) indicate that these tax notches reduce sales prices of the most responsive transactions by two to five times the marginal tax paid at the notch, which ranges from 1,250 to 40,000 pounds. In addition, a temporary one percentage point reduction in stamp duties on homes sold for 125,000 to 175,000 pounds in 2008-2009 induced 20% more transactions, primarily because of time-shifting, but also from trades that were newly mutually beneficial between buyers and sellers (the “extensive margin” effect). As a result, this tax holiday was a successful fiscal stimulus.<sup>82</sup> 

In related work, Kopczuk and Munroe (2015) use the fact that New York and New Jersey impose a transaction tax of 1% on homes that sell for at least one million dollars and several other features of the nonlinear tax schedule in these states to study how transaction taxes influence housing market liquidity. Again using a bunching estimator, this study also finds that fewer total transactions take place as a result of this tax treatment. Unraveling can occur because potential matches with low surplus within the region of the notch can be abandoned 

> 81For example, the two percentage point increase in tax at 250,000 pounds increases the liability by 5,000 pounds for a one pound increase in price. 

> 82 Besley, Meads, and Surico’s (2014) earlier look at the same episode generally confirms these results. 

87 

by sellers waiting longer to receive higher prices or by buyers waiting longer for lower prices. Overall, Kopczuk and Munroe (2015) find that 0.7% of transactions do not occur because of this tax notch. Through the lenses of models of buyer-selling bargaining, both Besley _et al._ (2014) and Kopczuk and Munroe (2015) find that sellers have more bargaining power and face greater tax incidence than buyers as a result. 

Finally, Dachis, Duranton, and Turner (2012) examine the consequences of the imposition of a 1.1% land transfer tax in Toronto, Canada, in 2008. Using a difference in discontinuity empirical strategy, in which distance to the Toronto municipality border is the running variable, they find that these taxes led to a 14% decline in transactions each year and were capitalized into lower sales prices about one for one. As a result, land transfer tax revenue crowds out subsequent property tax revenue. In the context of a simple location choice model, an increased Toronto property tax rate would have been more efficient at raising the same amount of additional revenue. In particular, model calibrations indicate a 19.5 million dollar aggregate loss each year because of transactions that do not happen. This 12.5% of estimated land transfer tax revenue is a social loss that reflects distorted mobility decisions. Property taxes could have been set to raise the same amount of revenue without this distortion. This evidence is independently corroborated by Han, Ngai, and Sheedy (2022), who additionally argue through the structure of a search model that the tax generates an inefficient shift from owning to renting with associated deadweight losses of 32% of revenue. 

The other common transfer tax on real estate is the capital gains tax on primary residence. While most oecd countries fully exempt these capital gains from taxation, nine do levy this tax, including the us (Andrews, 2011). Using the shift in 1997 from a broader applicability of the tax to the current less stringent regime for identification, Cunningham and Engelhardt (2008) and Shan (2011) find large mobility and housing market liquidity impacts for affected properties. 

The connection between mobility frictions induced by taxation and housing supply is indirect but straightforward. As an example, transaction taxes lock in high-income retirees in San Francisco when they would otherwise move to Florida, where new housing can be built easily. This phenomenon will be strongest in locations with the most inelastic supply of available properties, as these are the locations with the highest prices and greatest capital gains. Hence, besides misallocating housing, transaction taxes reduce supply through mobility frictions. 

Many governments also provide various types of incentives to support housing demand. For example, half of oecd countries allow deductions of mortgage interest from taxable income in some situations (Andrews, 2011). In the us before 2017, when eligibility was tightened, the mortgage interest deduction amounted to a 90 billion dollar annual tax expenditure (Sommer and Sullivan, 2018). Other common policies are grants or tax credits 

88 

for first-time home buyers, direct provision of home loans at subsidized interest rates, taxpayer-backed mortgage securitization enterprises, including Fannie Mae and Freddie Mac, and subsidized mortgage insurance.<sup>83</sup> 

These policies that directly support housing demand will raise prices and reduce affordability, especially in supply-constrained markets (Favara and Imbs, 2015, Justiniano, Primiceri, and Tambalotti, 2019). They can also influence the types of new construction. As many of these policies work on the intensive margin, they subsidize the purchase of larger, more expensive homes. This demand is then fulfilled by builders with more such new constructions, which could contribute to affordability challenges. Moreover, they will tend to shift demand toward and from rental which can owner-occupied away properties, also influence the types of dwelling units that developers build. 

Evidence in the literature supports all of these claims. Hilber and Turner (2014) find that the us mortgage interest deduction boosts homeownership of higher-income households in elastically supplied markets yet reduces homeownership in inelastic markets. Sommer and Sullivan (2018)’s calibrations of a dynamic structural model of owning and renting for the us indicates that removing the mortgage interest deduction would result in substantially lower house prices, allowing for more lower-income households to become homeowners.<sup>84</sup> Using a reduction in the generosity in the mortgage interest deduction for medium- and high-income households in Denmark, Gruber, Jensen, and Kleven (2021) finds no evidence that this policy influences homeownership rates for these groups but compelling evidence that it increases house prices and incentivizes the purchase of larger homes. 

The tax code is also commonly used to incentivize the construction of rental housing, in the lihtc mentioned above. As these are including program housing developments more likely to be in low-income neighborhoods with market rents below levels needed to justify construction costs, it is logical that these subsidies may not crowd out much private construction. However, it is revealing that developers have a large amount of excess demand for these tax credits (Baum-Snow and Marion, 2009). This study finds up to 60% crowd out of market rental construction in gentrifying neighborhoods, though little crowd out in other settings at the census block group level. Eriksen and Rosenthal (2010) finds substantially greater crowd-out when looking at a 10-mile radius spatial scale. Using variation in developer application rates as a function of the size and availability of tax credits and detailed parcel-level information about development, Soltas (2024 _a_ ) estimates about 80% crowd-out at the parcel level and that about 50% of the tax credits ending up as developer profits. Across all subsidized housing programs, Sinai and Waldfogel (2005) find about 30%-50% crowd-out at the metropolitan area level, arguing that aggregate supply effects of 

> 83On the other side, some countries, including Canada, also limit demand for owner-occupied units by banning or taxing foreign buyers, requiring qualifying borrowers to pass mortgage stress tests, and limiting entry into mortgage credit markets. 

> 84A central parameter in this study is the housing supply elasticity, for which they use 0.9. 

89 

are more measured at the market level. we housing policies appropriately Conceptually, expect more crowd-out, the less elastic is rental housing demand. 

The lihtc has as the main source program replaced government-built public housing of project-based subsidized housing in the us. In recent decades, it has accounted for about one-fifth of all multifamily rental construction nationwide (Soltas, 2024 _a_ ). Overall, the us subsidized housing system covers about 8.5 million dwelling units, almost 20% of the overall rental stock. Of these, 3.6 million are lihtc units, with about 300,000 added each year, 0.9 million are public housing, 2.8 million are Section 8 person-based vouchers, and 1.3 million are Section 8 project-based vouchers (Department of Housing & Urban Development, 2023). These latter two categories are rental housing vouchers that cover the difference between apartment rent and 30% of household income, provided the former is at or below a fair market rent. Person-based vouchers are across designated portable apartments, whereas project-based vouchers are tied to dwelling units.<sup>85</sup> 

An alternative policy instrument to housing subsidies for low-income families is rent control or rent stabilization, which constrains rents to be below market levels. This policy is common around the world but has been eliminated in several us jurisdictions in recent decades, including three in the Boston area and in San Francisco. Because rent control depresses prices, it disincentivizes rental housing development. For this reason, New York and Toronto only limit rent growth in most dwellings constructed before 1974 and 2018, respectively. In addition, rent controls generate shortages and deadweight losses because some positive surplus rental market transactions are prohibited from taking place. Rent control is also likely to generate misallocation of renters to apartments. Some renters stay in apartments for which they are only willing to pay slightly more than controlled rents. Other potential renters have a much higher willingness to pay for these apartments. Glaeser and Luttmer (2003) find substantial evidence of such misallocation in New York City. 

One potential justification for rent control is the insurance value of predictable rents (Diamond _et al._ , 2019). Favilukis, Mabille, and Van Nieuwerburgh (2023) provides quantitative evidence that the neediest households enjoy substantial associated net welfare gains from rent control. Hilber and Schöni (2022) provides additional context and perspective about housing policy, including rent control, in the us and around the world. 

# **6. Top-down approaches to housing supply** 

When housing is unaffordable, households either consume less of it or elect to live in alternative locations where housing is cheaper, even though these locations may be less 

> 85Using identifying variation from updates in the calculation of metropolitan area-wide fair market rents, Collinson and Ganong (2018) provide evidence that landlords capture a large amount of the surplus from housing vouchers and that the supply of affordable apartments is thus generally quite inelastic, even in markets where new construction is elastically supplied. 

90 

productive or provide lower consumer amenities. In extreme cases, households become homeless, a topic we do not address in this chapter, or households fail to form in the first place. To capture the full social cost of the unaffordability of housing, a general equilibrium model is needed. Only a general equilibrium model can track the welfare consequences of to in land use as these will work migration responses changes regulations, responses through changes in housing prices, amenities, and productivity in all locations. 

We know of no assessment focusing on the aggregate effects of households consuming too little housing because of our inability to build housing cheaply and efficiently.<sup>86</sup> An extremely simple back-of-the-envelope calculation nonetheless suggests large effects. To be roughly consistent with the data and results established above, assume Cobb-Douglas preferences for housing with an expenditure share of 0.25 and a Cobb-Douglas production function for housing with a share of capital of 0.65. If construction was 20% more productive – a higher _B_ using our notations and a conservative figure given our discussion in section 3.6 – equation (17) then implies that builders would provide 68% more housing per unit of land. Following what is reported in figure 3, we also conservatively assume a growth in the number of net units of 1.5% annually or 16% after ten years. Under these assumptions, a 20% higher productivity in construction would amount to an extra 11% added to the stock of housing after ten years. In turn, this higher productivity in construction would lead to a 2.6% gain in welfare, only from being able to consume more housing. Obviously, this is only a partial equilibrium calculation, and a full general equilibrium setting would need to be developed to explore this question more fully. 

Recent work has focused on the misallocation effects of land use spatial regulations. This strand of research has attracted a lot of attention in recent Hsieh and years following Moretti’s (2019) initial impulse and subsequent research by Duranton and Puga (2023), Parkhomenko (2023), and other references cited below.<sup>87</sup> In this line of work, stringent land use in cities act as a barrier to from less regulations prosperous migration prosperous cities and create large aggregate costs. This feature is consistent with the results in Howard and Liebersohn (2021) who show that high housing prices in superstar cities are caused by increasingly stringent land use regulations aimed at fending off the arrival of newcomers. 

In the model proposed by Duranton and Puga (2023), cities face a trade-off between agglomeration economies and urban costs. Both the benefits and costs of cities increase with their populations. Per-capita consumption is hump-shaped in the number of residents. It initially increases with city population, as agglomeration economies dominate, before it 

> 86There are several reasons behind this lack of interest. The widespread realization that the productivity performance of the construction sector has been dismal, as discussed in section 3.6, is fairly recent. Most of the literature has instead focused on situations where some locations are heavily regulated and others less, which is more in line with the context surrounding land development reviewed in section 5. 

> 87There are several controversies around the results of Hsieh and Moretti (2019), with, in particular, a comment by Greaney (2019) making strong counter-claims. This debate has not been settled at the time of the writing of this chapter. 

91 

starts to decline as urban costs eventually dominate. This trade-off is resolved by incumbent residents who decide how large their city should be in each period. They unanimously choose the population of their city to maximize consumption per capita at the top of the hump, as in Albouy, Behrens, Robert-Nicoud, and Seegert (2019).<sup>88</sup> 

Residents then impose their preferred population size by making newcomers pay a wasteful permitting cost. The empirical counterpart of this cost is taken to be the wedge between the market price of an existing house and its replacement cost on unpermitted land. This political-economy mechanism is akin to the homevoter hypothesis of Fischel (2001) discussed above. It resolves the trade-off between the agglomeration benefits of cities and their urban costs in a privately optimal way for each city. The spatial equilibrium between cities is simple to construct. The location with the highest productivity fundamentals will develop the largest city, followed by the second highest, etc. This process of city creation continues until the remaining households prefer to live in a rural location operating under decreasing returns to scale rather than establish a new city on the most productive of the remaining potential locations for a city. 

By operating at their privately optimal scales enforced by permitting costs, cities – especially the most productive ones – generate an inefficiency, which, in turn, implies large social costs. To see why, consider the relocation of a small group of households from the least productive city or the residual rural area to the largest city. Given the gap in consumption between the largest city and rural area, this relocation generates a large discrete gain in consumption for relocating households and a small marginal loss for incumbent residents from whom urban costs grow marginally larger than agglomeration benefits. In equilibrium, the largest cities are too small, there are too many small cities, and the rural population is too large. 

The main counterfactual in Duranton and Puga (2023) considers what would have happened if the seven superstar cities defined in section 2 had built new housing between 1980 and 2010 at the same rate as the metropolitan area at the 75th percentile for building permits. That percentile corresponds to about 0.81 permits per dwelling since 1980 relative to, for instance, 0.22 in New York. Using estimated parameter values summarizing agglomeration forces and urban costs along with calibrated values from the literature capturing the magnitude of decreasing returns in rural areas, this counterfactual implies that an additional 17 million residents would live in these seven superstar cities. The largest increase in population occurs in New York, which would have received an additional 7.5 million residents between 1980 and 2010. 

> 88In the absence of a mechanism to regulate city creation and city population, multiple equilibria abound due to the coordination failure caused by agglomeration economies. The most productive locations may not develop as a city. In addition, the benefits of the most productive locations may get crowded out by newcomers moving in until consumption is equalized between that city and the location offering the lowest level of consumption, leading to possibly immense and wasteful overcrowding. See Behrens and Robert-Nicoud (2015) for further elaborations. 

92 

This (counterfactual) increase in population in the largest and most productive cities leads to an aggregate gain in total output close to 8%. This gain arises from (i) the relocation of 17 million people to more productive places, (ii) stronger agglomeration effects in superstar cities after the arrival of these newcomers, and (iii) a higher output per worker in (leftbehind) rural areas operating under decreasing returns to scale. However, a large part of these production gains are dissipated into increasing urban costs. The aggregate gain in consumption (welfare) is 2.1%.<sup>89</sup> Newcomers and rural dwellers experience consumption gains of 6.5%. However, incumbent residents of superstar cities experience consumption losses from increased urban costs, which more than offset higher agglomeration benefits. These losses are nonetheless minimal: 0.05% at most in New York. The reason behind these small losses is that the difference between the agglomeration elasticity and the urban cost elasticity is small, 0.04, with the parameter values used in Duranton and Puga (2023). Put differently, the hump shape of city consumption as a function of population size is fairly flat after its maximum. Cities can thus grow significantly larger than their privately optimal scale at a low net cost for their incumbent residents. 

Two further results are of interest. First, aggregate income and consumption inequalities decline as the income and consumption of (poorer) rural residents increase. Second, the relaxation of land use regulations in superstar cities to allow for more dwellings to be built also leads to a relaxation of land use regulations in other cities, as the migration pressure toward these cities is also being eased. 

The conclusion that relaxing restrictions on land development and new constructions could lead to large aggregate gains is pervasive in the literature. Magnitudes comparable to those of Duranton and Puga (2023), or larger, also appear in Ganong and Shoag (2017), Herkenhoff, Ohanian, and Prescott (2018), Hsieh and Moretti (2019), and Parkhomenko (2023).<sup>90</sup> This conclusion is, however, disputed by Glaeser and Gyourko (2018), who argue that the aggregate social cost of restrictive land use regulations is more like 2% instead of 10% or more, as implied by the rest of the literature. 

The key difference regards how local economies respond to a population shock. Glaeser and Gyourko (2018) argue that labor demand at the city level is fairly inelastic so that the large wage differences we observe between cities quickly disappear as we allow households to move from low-wage locations to high-wage but tightly regulated cities. In turn, the gains from such a reduction in spatial misallocation are limited and even vanish as labor demand becomes inelastic. It is true that the from land use totally gains weakening regulations 

> 89The standard distinction between output (gdp) and welfare (consumption) is particularly salient here given the importance of unavoidable urban costs when cities grow in population. 

> 90Favilukis _et al._ (2023) also find a large supply response from relaxing land use regulations in New York while taking into account that regulations detrimental to supply are also motivated by protecting incumbent renters from the price risks associated with renting as discussed above. Babalievsky, Herkenhoff, Ohanian, and Prescott (2023) explore the aggregate costs from the regulations of commercial real estate. They claim welfare gains of 3 to 6% from deregulating an asset class that represents about 20% to aggregate capital. 

93 

where they bind the most crucially depend on how local firms respond to the arrival of new workers.<sup>91</sup> The labor literature cited in Glaeser and Gyourko (2018) is supportive of a downward-sloping labor demand for existing local firms. However, these estimates are probably best viewed as “all else equal”: how many workers will firms hire for a given wage in a partial equilibrium setting? Instead, the relevant “labor demand curve” at the city level should include equilibrium effects since newcomers will bring their demand for local goods, some of them will create new firms, and they may induce some firms to relocate. In line with these effects, the data are supportive of a modestly upward-sloping city wage with city population, with at least some of this relationship being causal (Combes and Gobillon, 2015). This is what we should expect with agglomeration effects, at least in the long run. 

However, labor is not homogeneous and is not located proportionately by skill level across cities. The most productive cities are also where housing is the most expensive. As a result, these cities disproportionately attract highly skilled workers who benefit the most from their agglomeration effects and are able to pay the cost of living there (Behrens _et al._ , 2014). This sorting of workers across cities also implies that a large part of the urban wage premium is due to sorting. Urban amenities also play an important role in household location choices and are most likely affected by the skill composition of cities. Diamond (2016) proposes a model with endogenous city amenities that are increasing in the local fraction of college-educated households. After a skill-biased labor demand shock, endogenous amenities magnify changes in the skill composition of cities, making more skilled cities all the more attractive (and expensive) to other skilled workers. 

In turn, these features have implications for the analysis of land use regulations in general equilibrium. Macek (2024) incorporates endogenous local amenities in his quantitative evaluation of the consequences of relaxing minimum lot size (mls) zoning restrictions. He develops a static model with neighborhood and worker heterogeneity that is quantified to census block groups across the United States. The location choices of workers depend locally on housing costs, wages, and amenities, which are endogenous to neighborhood composition. mls restrictions negatively impact productivity and wages by limiting the population of the most productive locations. In addition, these restrictions induce the 

> 91While general equilibrium models of multiple cities often assume that labor is freely mobile across cities, a large literature on migrations reports large migration costs (see Jia, Molloy, Smith, and Wozniak, 2023, for a review). In a world where labor supply (population) is highly inelastic across cities, land use regulations might not be binding. This is unlikely given the evidence of a strong demand to live in large cities, in particular superstar cities (Howard and Liebersohn, 2021). Diamond’s (2016) preferred estimates for the elasticity of city population to city wages is 3.3 for non-college workers and 5.0 for college workers. Analogous estimates for rents are -2.9 for non-college workers and -2.2 for college workers. Given differences in housing prices across cities, these estimates are large enough to induce very significant population increases if housing was made more affordable in the most prosperous cities. See also Beaudry, Green, and Sand (2014) for additional estimates. In short, even though it ultimately limits how many households want to move to a city, the slope of the labor supply across cities is unlikely to be an issue in the type of counterfactual considered in Duranton and Puga (2023) and discussed above. 

94 

sorting of less skilled workers into less restrictively zoned neighborhoods.<sup>92</sup> By keeping less-skilled workers out of more productive locations, mls regulations cause more highskilled workers to prefer these locations. Hence, mls zoning tends to concentrate more skilled workers where they are the most productive, thereby enhancing aggregate output.<sup>93</sup> Unlike in the models previously discussed with homogeneous workers, eliminating mls zoning only marginally changes aggregate output because it induces a re-sorting of workers that counteracts agglomeration effects. Strikingly, eliminating mls zoning in a productive city like San Francisco induces less skilled workers to flow into the city, activating negative endogenous amenities, which encourage more skilled workers to leave. In turn, this exit of skilled workers depresses property values and leaves many worse off. Nonetheless, housing affordability and welfare improve for low- and middle-income renters. 

Because they limit the development of the most productive cities, stringent land use regulations may also have dynamic implications through their effects on long-term growth. Duranton and Puga (2023) in an overlapping-generations model and Crews (2024) with a more framework can the of land use developed dynamic explore consequences regulations for human capital accumulation. Larger cities offer better opportunities for learning and accumulating human capital. Large cities may attract more skilled workers, as just argued, but they will also produce them. 

Duranton and Puga (2023) first propose a dynamic accounting exercise. Agglomeration economies play two roles in the growth process. First, through faster learning when working in cities, they directly foster the accumulation of human capital. Second, the same agglomeration economies will also magnify the size of cities, which in turn promotes human capital acquisition and accumulation. Overall, Duranton and Puga (2023) find that agglomeration effects account for 14 basis points of annual growth or 7% of the annual growth rate between 1950 and 2010. While this is not directly informative of the dynamic costs of land use regulations in general equilibrium, it is indicative that there are long-term costs to the of the most cities because are limiting growth productive they key breeding grounds for learning and accumulating human capital. In another counterfactual exercise, Crews (2024) finds that lifting restrictions to moving to the most skilled cities would raise growth by 13 basis points annually. Although speculative, these results nonetheless point to costs to land use restrictions that potentially go well beyond the static costs explored above. 

> 92This sorting occurs because mls restrictions in desirable neighborhoods reduce housing affordability for less skilled workers, either by constraining them to purchase more housing services than they would otherwise choose or by reducing aggregate housing supply, thereby raising costs. 

> 93See Rossi-Hansberg, Sarte, and Schwartzman (2019) for a related model with strong complementarities between skills and local productivity. 

95 

# **. Conclusions and future research directions 7** 

Recent declines in have a renewed interest in research on housing affordability prompted housing supply. In the us, the rate of new construction has slowed considerably since 2010, and estimated housing supply elasticities have been declining, particularly in the most locations. Our of the literature reveals a number of reasons productive survey potential for these changes. Productivity in the construction sector has declined, land use regulation has grown more stringent, and there is less land available for development in the most productive and highest amenity locations. While incumbent property owners in the best locations are incentivized to enact land use regulations to protect their property values, countless others would benefit from reduced regulation through lower housing costs and improved access. 

Our overview of facts on quantities, prices, and housing densities in the us confirms casual observations about declining affordability. As housing prices and rents have risen more rapidly than household incomes, rates of new construction have fallen precipitously since 2010. To compensate, dwellings are being removed from the housing stock at lower rates, especially in the costliest housing markets. Relative to a baseline rate of dwelling unit teardowns and abandonment of 0.7 percent per year in small and rural us counties, the corresponding depreciation rate is 0.2 percent per year in the “superstar cities” where housing is most expensive. This 0.5 percentage point difference contributes about 50% of “new” housing supply in superstar cities in comparison to small and rural areas. Along with lower construction rates, there has been a rapid decline after 2000 in the rate of housing densification in suburban areas. In most locations, redevelopment into denser land use has become very rare, an observation also reflected in very low estimated housing supply elasticities for redevelopment. 

Our overview of the literature considers both the construction and land development components of housing supply responses to rising prices. We lay out a standard model of housing production in which competitive developers install capital on heterogeneous lots to build housing. Consensus estimates from this literature reveal approximately Cobb-Douglas production with a capital share of 0.65. This implies an intensive margin supply elasticity with respect to the price of housing services of about 2. An independent literature finds sharply declining productivity in the construction sector, which can help to explain reduced construction rates despite rising prices. More research is needed to better understand the reasons for this declining productivity and potential policy remedies. 

One challenge faced by this neoclassical approach is that it has nothing to say about the timing of construction. While there is a rich theoretical literature about real development options and qualitative forces influencing the timing of construction, there is less empirical and quantitative work on this topic. The small amount of empirical work that exists is not well-suited for aggregation or incorporation into a general equilibrium framework. As a 

96 

result, unlike their static counterparts, dynamic market-level supply elasticities have not been characterized. the literature has little of a handle on systematically Relatedly, very the mechanisms driving very low estimated housing redevelopment elasticities. With an emerging consensus that reductions in land use regulation are needed to promote more new construction, more research is needed on the redevelopment process, including its dynamics and aggregation to market supply elasticities. 

A different challenge for the existing literature is how to handle the fact that dwellings are discrete and of sizes and The use of models as a heterogeneous qualities. assignment vehicle to match heterogeneous households to heterogeneous dwellings is a start and has yielded some useful insights. However, existing research in this area still does not have a good command of the housing development decision. Little is known about the extent to which new constructions of different sizes and qualities can be rationalized with the same approach as has been developed for the construction of units of housing services. Additional research in this area would be particularly fruitful, as it would speak to price responsiveness to demand shocks across the distribution of housing quality. We also hope that future research develops tractable and empirically quantifiable frameworks for analyzing the efficacy of subsidized housing policies targeting groups for which developers do not find it profitable to build market-rate units. Complicating such inquiries are the existence of externalities across homes and households that operate within neighborhoods. Incorporating such spatial relationships and location choice into assignment models would further facilitate their broader application. 

Land development makes up the extensive margin of housing supply. A flood of recent research the of constraints land use empirical analyzes consequences supply through regulations. The literature has successfully confronted both systematic measurement and the credible estimation of the consequences of various types of land use regulation in targeted and A articulation of the idea that land use well-identified settings. convincing regulations can raise property values through an aggregate supply effect is critical for understanding the political economy of land use regulation. This motivation comes in addition to property owners’ incentives to restrict development in order to limit negative fiscal externalities from lower taxes levied on low-value properties in the same jurisdiction along with associated potential negative social and density externalities. There is a strong consensus in the empirical literature that stricter land use regulation impedes development. Conditional on development, regulations and the tax system push toward the construction of fewer and larger dwellings. 

reduced-form evidence on the of land use for Well-identified consequences regulations property values and construction feeds into an active literature that uses general equilibrium models to assess the welfare of This literature consequences reducing regulations. finds benefits, though the magnitude and composition of these benefits depend crucially on the 

97 

of elasticities across locations and the for local system migration data-generating processes productivities and amenities. Active research in progress extends these models with richer treatments of dynamics and richer agent heterogeneity. In future research, these classes of models could be successfully repurposed to evaluate the distribution of returns to investing in improvements in construction technology. In addition, research that applies similar models to evaluate possibilities for feasibly compensating incumbent property owners for losses from land use deregulation would be fruitful. 

98 

# **References** 

- Aastveit, Knut Are, Bruno Albuquerque, and André K. Anundsen. 2023. Changing supply elasticities and regional housing booms. _Journal of Money, Credit and Banking_ 55(7):1749– 1783. 

- ab Iorwerth, Aled, Nathaniel Baum-Snow, and James Macek. 2025. Housing supply and affordability in canada. _Canadian Journal of Economics_ 58. 

- Ackerberg, Daniel, C. Lanier Benkard, Steven Berry, and Ariel Pakes. 2007. Econometric tools for analyzing market outcomes. In James J. Heckman and Edward E. Leamer (eds.) _Handbook of Econometrics_ , volume 6A. Amsterdam: North-Holland, 4271–4276. 

- Ahlfeldt, Gabriel M., Nathaniel Baum-Snow, and Rémi Jedwab. 2023. The skyscraper revolution: Global economic development and land savings. CESifo Working Paper. 

- Ahlfeldt, Gabriel M. and Daniel P. McMillen. 2013. New estimates of the elasticity of substitution of land for capital. Processed, London School of Economics. 

- Ahlfeldt, Gabriel M. and Daniel P. McMillen. 2018. Tall buildings and land values: Height and construction cost elasticities in chicago, 1870–2010. _Review of Economics and Statistics_ 100(5):861–875. 

- Albouy, David. 2009. The unequal geographic burden of federal taxation. _Journal of Political Economy_ 117(4):635–667. 

- Albouy, David, Kristian Behrens, Frédéric Robert-Nicoud, and Nathan Seegert. 2019. The optimal distribution of population across cities. _Journal of Urban Economics_ 110:102–113. 

- Albouy, David and Gabriel Ehrlich. 2018. Housing productivity and the social cost of landuse restrictions. _Journal of Urban Economics_ 107(0):101–120. 

- Albouy, David, Gabriel Ehrlich, and Minchul Shin. 2018. Metropolitan land values. _Review of Economics and Statistics_ 100(3):454–466. 

- Allen, Steven G. 1985. Why construction industry productivity is declining. _Review of Economics and Statistics_ 67:601–669. 

- Almagro, Milena, Eric Chyn, and Bryan A Stuart. 2023. Urban renewal and inequality: Evidence from chicago’s public housing demolitions. Technical report, National Bureau of Economic Research. 

- Almagro, Milena and Tomás Domínguez-Iino. 2025. Location sorting and endogenous amenities: Evidence from Amsterdam. Technical report. 

- Alonso, William. 1964. _Location and Land Use; Toward a General Theory of Land Rent_ . Cambridge, ma: Harvard University Press. 

- Altshuler, Alan A. and José’ A. Gómez-Ibáñez. 2000. _Regulation for Revenue: The Political Economy of Land Use Exactions_ . Washington dc: Brookings Institution Press. 

99 

- Ambrose, Brent W., N. Edward Coulson, and Jiro Yoshida. 2015. The repeat rent index. _Review of Economics and Statistics_ 97(5):939–950. 

- Anagol, Santosh, Fernando Ferreira, and Jonah Rexer. 2025. Estimating the economic value of zoning reform. _American Economic Journal: Economic Policy_ accepted for publication. 

- Anas, Alex and David Pines. 2008. Anti-sprawl policies in a system of congested cities. _Regional Science and Urban Economics_ 38(5):408–423. 

- Anas, Alex and Hyok-Joo Rhee. 2006. Curbing excess sprawl with congestion tolls and urban boundaries. _Regional Science and Urban Economics_ 36(4):510–541. 

- Andrews, Dan. 2011. Housing markets and structural policies in oecd countries . 

- Arcidiacono, Peter and Robert A. Miller. 2011. Conditional choice probability estimation of dynamic discrete choice models with unobserved heterogeneity. _Econometrica_ 79(6):1823– 1867. 

- Arnott, Richard. 1987. Economic theory and housing. In Edwin S. Mills (ed.) _Handbook of Regional and Urban Economics_ , volume 2. North-Holland: Elsevier, 959–988. 

- Arnott, Richard. 1995. Time for revisionism on rent control? _Journal of economic perspectives_ 9(1):99–120. 

- Arnott, Richard J. and Ralph M. Braid. 1997. A filtering model with steady-state housing. _Regional Science and Urban Economics_ 27(4-5):515–546. 

- Artmann, Martina, Luis Inostroza, and Peilei Fan. 2019. Urban sprawl, compact urban development and green cities. How much do we know, how much do we agree? 

- Asker, John, Allan Collard-Wexler, and Jan De Loecker. 2014. Dynamic inputs and resource (mis) allocation. _Journal of Political Economy_ 122(5):1013–1063. 

- Asquith, Brian J., Evan Mast, and Davin Reed. 2023. Local effects of large new apartment buildings in low-income areas. _Review of Economics and Statistics_ 105(2):359–375. 

- Autor, David H., Christopher J. Palmer, and Parag A. Pathak. 2014. Housing market spillovers: Evidence from the end of rent control in Cambridge, Massachusetts. _Journal of Political Economy_ 122(3):661–717. 

- Babalievsky, Fil, Kyle F. Herkenhoff, Lee E. Ohanian, and Edward C. Prescott. 2023. The impact of commercial real estate regulations on US output. Technical report, National Bureau of Economic Research Working Paper 31985. 

- Bar-Ilan, Avner and William C. Strange. 1996. Investment lags. _American Economic Review_ 86(3):610–622. 

- Barr, Jason M. 2016. _Building the Skyline: The Birth and Growth of Manhattan’s Skyscrapers_ . New York City (ny): Oxford University Press. 

- Barseghyan, Levon and Stephen Coate. 2016. Property taxation, zoning, and efficiency in a dynamic tiebout model. _American Economic Journal: Economic Policy_ 8(3):1–38. 

100 

- Bartik, Alexander, Arpit Gupta, and Daniel Milo. 2024. The costs of housing regulation: Evidence from generative regulatory measurement. Technical report. Working Paper, New York University, Stern School of Business. 

- Baum-Snow, Nathaniel. 2023. Constraints on city and neighborhood growth: The central role of housing supply. _Journal of Economic Perspectives_ 37(2):53–74. 

- Baum-Snow, Nathaniel and Lu Han. 2024. The microgeography of housing supply. _Journal of Political Economy_ 132(6):1897–1946. 

- Baum-Snow, Nathaniel and Justin Marion. 2009. The effects of low income housing tax credit developments on neighborhoods. _Journal of Public Economics_ 93(5-6):654–666. 

- Bayer, Patrick, Fernando Ferreira, and Robert McMillan. 2007. A unified framework for measuring preferences for schools and neighborhoods. _Journal of Political Economy_ 115(4):588–638. 

- Bayliss, Simon and Rory Bergin. 2020. The modular world. In Simon Bayliss and Rory Bergin (eds.) _The Modular Housing Handbook_ . London (uk): RIBA Publishing, 116–139. 

- Beaudry, Paul, David A. Green, and Benjamin M. Sand. 2014. Spatial equilibrium with unemployment and wage bargaining: Theory and estimation. _Journal of Urban Economics_ 79(1):2–19. 

- Been, Vicki, Ingrid Gould Ellen, Michael Gedal, Edward Glaeser, and Brian J. McCabe. 2016. Preserving history or restricting development? The heterogeneous effects of historic districts on local housing markets in New York City. _Journal of Urban Economics_ 92:16–30. 

- Behrens, Kristian, Gilles Duranton, and Frédéric Robert-Nicoud. 2014. Productive cities: Sorting, selection, and agglomeration. _Journal of Political Economy_ 122(3):507–553. 

- Behrens, Kristian, Yoshitsugu Kanemoto, and Yasusada Murata. 2015. The Henry George Theorem in a second-best world. _Journal of Urban Economics_ 85:34–51. 

- Behrens, Kristian and Frédéric Robert-Nicoud. 2015. Agglomeration theory with heterogeneous agents. In Gilles Duranton, Vernon Henderson, and William Strange (eds.) _Handbook of Regional and Urban Economics, volume 5A_ . Amsterdam: Elsevier, 171–245. 

- Ben-Moshe, Dan and David Genesove. 2024. Regulation and frontier housing supply. Processed, The Hebrew University of Jerusalem. 

- Ben-Shahar, Danny, Yongheng Deng, Eyal Solganik, Tsur Somerville, and Zhu Hongjia. 2022. The value of vertical status: Evidence from the real estate market Processed, University of British Columbia. 

- Bergman, Peter, Raj Chetty, Stefanie DeLuca, Nathaniel Hendren, Lawrence F. Katz, and Christopher Palmer. 2024. Creating moves to opportunity: Experimental evidence on barriers to neighborhood choice. _American Economic Review_ 114(5):1281–1337. 

- Bertaud, Alain and Jan K. Brueckner. 2005. Analyzing building-height restrictions: Predicted impacts and welfare costs. _Regional Science and Urban Economics_ 35(2):109–125. 

101 

- Besley, Timothy, Neil Meads, and Paolo Surico. 2014. The incidence of transaction taxes: Evidence from a stamp duty holiday. _Journal of Public Economics_ 119:61–70. 

- Best, Michael Carlos and Henrik Jacobsen Kleven. 2018. Housing market responses to transaction taxes: Evidence from notches and stimulus in the uk. _The Review of Economic Studies_ 85(1):157–193. 

- Braid, Ralph M. 1981. The short-run comparative statics of a rental housing market. _Journal of Urban Economics_ 10(3):286–310. 

- Bratu, Cristina, Oskari Harjunen, and Tuukka Saarimaa. 2023. City-wide effects of new housing supply: Evidence from moving chains. _Journal of Urban Economics, Insights_ 133:103528. 

- Bronin, Sara C., Scott Markley, Aline Fader, and Evan Derickson. 2023. How to make a zoning atlas 2.0: The official methodology of the National Zoning Atlas. Technical report. Cornell University, Department of City and Regional Planning. 

- Brooks, Leah and Zachary Liscow. 2023. Infrastructure costs. _American Economic Journal: Applied Economics_ 15(2):1–30. 

- Brooks, Leah and Byron Lutz. 2016. From today’s city to tomorrow’s city: An empirical investigation of urban land assembly. _American Economic Journal: Economic Policy_ 8(3):69– 105. 

- Brueckner, Jan, Shihe Fu, Yizhen Gu, and Junfu Zhang. 2017. Measuring the stringency of land use regulation: The case of China’s building height limits. _Review of Economics and Statistics_ 99(4):663–677. 

- Brueckner, Jan K. 2000. Urban sprawl: Diagnosis and remedies. _International Regional Science Review_ 23(2):160–171. 

- Brueckner, Jan K. 2007. Urban growth boundaries: An effective second-best remedy for unpriced traffic congestion? _Journal of Housing Economics_ 16(3-4):263–273. 

- Brueckner, Jan K. 2023. Jue insight: Zoning and property taxation revisited—was hamilton right? _Journal of Urban Economics_ 133:103393. 

- Brueckner, Jan K., David Leather, and Miguel Zerecero. 2024. Bunching in real-estate markets: Regulated building heights in New York City. _Journal of Urban Economics_ 143:103683. 

- Brueckner, Jan K. and Stuart S. Rosenthal. 2009. Gentrification and neighborhood housing cycles: Will America’s future downtowns be rich? _Review of Economics and Statistics_ 91(4):725–743. 

- Brueckner, Jan K. and Ruchi Singh. 2020. Stringency of land-use regulation: Building heights in US cities. _Journal of Urban Economics_ 116:103239. 

- Brunner, Eric and Jon Sonstelie. 2003. Homeowners, property values, and the political economy of the school voucher. _Journal of Urban Economics_ 54(2):239–257. 

102 

- Brunner, Eric, Jon Sonstelie, and Mark Thayer. 2001. Capitalization and the voucher: an analysis of precinct returns from California’s Proposition 174. _Journal of Urban Economics_ 50(3):517–536. 

- Büchler, Simon, Maximilian v. Ehrlich, and Olivier Schöni. 2021. The amplifying effect of capitalization rates on housing supply. _Journal of Urban Economics_ 126:103370. 

- Burchfield, Marcy, Henry G. Overman, Diego Puga, and Matthew A. Turner. 2006. Causes of sprawl: A portrait from space. _Quarterly Journal of Economics_ 121(2):587–634. 

- Cai, Hongbin, Zhi Wang, and Qinghua Zhang. 2017. To build above the limit? Implementation of land use regulations in urban China. _Journal of Urban Economics_ 98:223–233. 

- Calabrese, Stephen, Dennis Epple, and Richard Romano. 2007. On the political economy of zoning. _Journal of Public Economics_ 91(1-2):25–49. 

- Calder-Wang, Sophie and Gi Heung Kim. 2024. Algorithmic pricing in multifamily rentals: Efficiency gains or price coordination? Working Paper, Wharton School, University of Pennsylvania. 

- Capozza, Dennis R. and Robert W. Helsley. 1990. The stochastic city. _Journal of Urban Economics_ 28(2):187–203. 

- Cheshire, Paul C. and Gerard H. Dericks. 2020. ‘Trophy architects’ and design as rentseeking: Quantifying deadweight losses in a tightly regulated office market. _Economica_ 87(348):1078–1104. 

- Cheshire, Paul C. and Christian A. L. Hilber. 2008. Office space supply restrictions in Britain: The political economy of market revenge. _Economic Journal_ 118(529):F185–F221. 

- Chetty, Raj, John N. Friedman, Nathaniel Hendren, Maggie R. Jones, and Sonya R. Porter. 2018. The opportunity atlas: Mapping the childhood roots of social mobility. Technical report, National Bureau of Economic Research. 

- Clapp, John M. 1979. The substitution of urban land for other inputs. _Journal of Urban Economics_ 6(1):122–134. 

- Clarke, Wyatt and Matthew Freedman. 2019. The rise and effects of homeowners associations. _Journal of Urban Economics_ 112:1–15. 

- Collinson, Robert and Peter Ganong. 2018. How do changes in housing voucher design affect rent and neighborhood quality? _American Economic Journal: Economic Policy_ 10(2):62–89. 

- Combes, Pierre-Philippe, Gilles Duranton, and Laurent Gobillon. 2019. The costs of agglomeration: House and land prices in French cities. _Review of Economic Studies_ 86(4):1556–1589. 

- Combes, Pierre-Philippe, Gilles Duranton, and Laurent Gobillon. 2021. The production function for housing: Evidence from France. _Journal of Political Economy_ 129(10):2766–2816. 

- Combes, Pierre-Philippe, Gilles Duranton, Laurent Gobillon, and Clément Gorin. 2024. Measuring land use changes by (machine) learning from historical maps. Mimeographed, University of Pennsylvania. 

103 

- Combes, Pierre-Philippe, Gilles Duranton, Laurent Gobillon, and Sébastien Roux. 2010. Estimating agglomeration economies with history, geology, and worker effects. In Edward L. Glaeser (ed.) _The Economics of Agglomeration_ . Cambridge (ma): National Bureau of Economic Research, 15–65. 

- Combes, Pierre-Philippe and Laurent Gobillon. 2015. The empirics of agglomeration economies. In Gilles Duranton, Vernon Henderson, and William Strange (eds.) _Handbook of Regional and Urban Economics_ , volume 5A. Amsterdam: Elsevier, 247–348. 

- Cosman, Jacob, Tom Davidoff, and Joe Williams. 2018. Housing appreciation and marginal land in monocentric cities with of British supply topography. Working paper, University 

- Columbia. 

- Couture, Victor, Cecile Gaubert, Jessie Handbury, and Erik Hurst. 2024. Income growth and the distributional effects of urban spatial sorting. _Review of Economic Studies_ 91(2):858–898. 

- Crews, Levi. 2024. A dynamic spatial knowledge economy. Working Paper, University of California Los Angeles. 

- Cui, Tianfang. 2024. Did race fence off the American city? The great migration and the evolution of exclusionary zoning. Working paper, New York University, Robert F. Wagner School of Public Service. 

- Cunningham, Christopher R. 2007. Growth controls, real options, and land development. _The Review of Economics and Statistics_ 89(2):343–358. 

- Cunningham, Christopher R and Gary V Engelhardt. 2008. Housing capital-gains taxation and homeowner mobility: evidence from the taxpayer relief act of 1997. _Journal of urban Economics_ 63(3):803–815. 

- Dachis, Ben, Gilles Duranton, and Matthew A. Turner. 2012. The effects of land transfer taxes on real estate markets: evidence from a natural experiment in Toronto. _Journal of Economic Geography_ 12(2):327–354. 

- D’Amico, Leonardo, Edward L. Glaeser, Joseph Gyourko, William Kerr, and Giacomo A.M. Ponzetto. 2024. Why has construction productivity stagnated? The role of land-use regulation. Working Paper, Harvard University. 

- Danton, Jayson and Alexander Himbert. 2018. Residential vertical rent curves. _Journal of Urban Economics_ 107:89–100. 

- Davidoff, Thomas. 2013. Supply elasticity and the housing cycle of the 2000s. _Real Estate Economics_ 41(4):793–813. 

- Davidoff, Thomas. 2015. Supply constraints are not valid instrumental variables for home prices because they are correlated with many demand factors. Working paper, University of British Columbia, Sauder School of Business. 

- Davidoff, Thomas, Andrey Pavlov, and Tsur Somerville. 2022. Not in my neighbour’s back yard? Laneway homes and neighbours’ property values. _Journal of Urban Economics_ 128:103405. 

104 

- Davis, Donald R. and Jonathan I. Dingel. 2020. The comparative advantage of cities. _Journal of International Economics_ 123:103291. 

- Davis, Morris A., Andra C. Ghent, and Jesse Gregory. 2024. The work-from-home technology boon and its consequences. _Review of Economic Studies_ 91:3362–3401. 

- Davis, Morris A., William D. Larson, Stephen D. Oliner, and Jessica Shui. 2021. The price of residential land for counties, ZIP Codes, and census tracts in the United States. _Journal of Monetary Economics_ 118:413–431. 

- Davis, Morris A. and Michael G. Palumbo. 2008. The price of residential land in large US cities. _Journal of Urban Economics_ 63(1):352–384. 

- Dehring, Carolyn A., Craig A. Depken II, and Michael R. Ward. 2008. A direct test of the homevoter hypothesis. _Journal of Urban Economics_ 64(1):155–170. 

- Department of Housing & Urban Development. 2023. _A picture of subsidized households in 2023_ . us Department of Housing & Urban Development, Office of Policy Development. 

- Desmet, Klaus and Fernando Parro. 2025. Spatial dynamics. In Dave Donaldson and Stephen J. Redding (eds.) _Handbook of Regional and Urban Economics_ , volume (this volume). Amsterdam: Elsevier. 

- Diamond, Rebecca. 2016. The determinants and welfare implications of US workers’ diverging location choices by skill: 1980-2000. _American Economic Review_ 106(3):479–524. 

- Diamond, Rebecca and Tim McQuade. 2019. Who wants affordable housing in their backyard? An equilibrium analysis of low-income property development. _Journal of Political Economy_ 127(3):1063–1117. 

- Diamond, Rebecca, Tim McQuade, and Franklin Qian. 2019. The effects of rent control expansion on tenants, landlords, and inequality: Evidence from San Francisco. _American Economic Review_ 109(9):3365–3394. 

- DiPasquale, Denise. 1999. Why don’t we know more about housing supply? _Journal of Real Estate Finance and Economics_ 18(1):9–23. 

- Dumm, Randy E., G. Stacy Sirmans, and Greg Smersh. 2011. The capitalization of building codes in house prices. _Journal of Real Estate Finance and Economics_ 42:30–50. 

- Duranton, Gilles and Diego Puga. 2014. The growth of cities. In Philippe Aghion and Steven Durlauf (eds.) _Handbook of Economic Growth_ , volume 2. Amsterdam: North-Holland, 781–853. 

- Duranton, Gilles and Diego Puga. 2015. Urban land use. In Gilles Duranton, J. Vernon Henderson, and William C. Strange (eds.) _Handbook of Regional and Urban Economics_ , volume 5A. Amsterdam: North-Holland, 467–560. 

- Duranton, Gilles and Diego Puga. 2023. Urban growth and its aggregate implications. _Econometrica_ 91(6):2219–2259. 

105 

- Duranton, Gilles and Matthew A. Turner. 2018. Urban form and driving: Evidence from US cities. _Journal of Urban Economics_ 108(0):171–191. 

- Eckert, Fabian and Tatjana Kleineberg. 2021. The geography of opportunity: Education, work, and intergenerational mobility across US counties. Working paper, University of California San Diego. 

- Ellickson, Robert C. 2020. The zoning straitjacket: The freezing of American neighborhoods of single-family houses. _Indiana Law Journal_ 96:395–427. 

- Epple, Dennis, Brett Gordon, and Holger Sieg. 2010. A new approach to estimating the production function for housing. _American Economic Review_ 100(3):905–925. 

- Epple, Dennis, Luis Quintero, and Holger Sieg. 2020. A new approach to estimating equilibrium models for metropolitan housing markets. _Journal of Political Economy_ 128(3):948–983. 

- Eriksen, Michael D. and Anthony W. Orlando. 2022. Returns to scale in residential construction: The marginal impact of building height. _Real Estate Economics_ 50(2):534–564. 

- Eriksen, Michael D and Stuart S Rosenthal. 2010. Crowd out effects of place-based subsidized rental housing: New evidence from the lihtc program. _Journal of Public Economics_ 94(11-12):953–966. 

- Esch, Thomas, Klaus W. Deininger, Rémi Jedwab, and Daniela Palacios-Lopez. 2024. Outward and upward construction: A 3D analysis of the global building stock. Working paper, World Bank Group. 

- Ewing, Reid and Robert Cervero. 2010. Travel and the built environment: A meta-analysis. _Journal of the American Planning Association_ 76(3):265–294. 

- Favara, Giovanni and Jean Imbs. 2015. Credit supply and the price of housing. _American economic review_ 105(3):958–992. 

- Favilukis, Jack, Pierre Mabille, and Stijn Van Nieuwerburgh. 2023. Affordable housing and city welfare. _The Review of Economic Studies_ 90(1):293–330. 

- Favilukis, Jack and Stijn Van Nieuwerburgh. 2021. Out-of-town home buyers and city welfare. _Journal of Finance_ 76(5):2577–2638. 

- Fernandes Rocha, Patrícia, Nuno Oliveira Ferreira, Fernando Pimenta, and Nelson Bento Pereira. 2022. Impacts of prefabrication in the building construction industry. _Encyclopedia_ 3(1):28–45. 

- Ferreira, Fernando. 2010. You can take it with you: Proposition 13 tax benefits, residential mobility, and willingness to pay for housing amenities. _Journal of Public Economics_ 94(910):661–673. 

- Fischel, William A. 2001. _The Homevoter Hypothesis_ . Cambridge (ma): Harvard University Press. 

106 

- Foerster, Andrew T., Andreas Hornstein, Pierre-Daniel G. Sarte, and Mark W. Watson. 2022. Aggregate implications of changing sectoral trends. _Journal of Political Economy_ 130(12):3286–3333. 

- Fogli, Alessandra, Veronica Guerrieri, Mark Ponder, and Marta Prato. 2024. The end of the American dream? Inequality and segregation in US cities. Working Paper, Federal Reserve Bank of Minneapolis. 

- Francke, Marc K. and Alex M. van de Minne. 2017. Land, structure and depreciation. _Real Estate Economics_ 45(2):415–451. 

- French, Robert and Valentine Gilbert. 2024. Suburban housing and urban affordability: Evidence from residential vacancy chains. Working paper, Harvard Kennedy School. 

- Ganong, Peter and Daniel Shoag. 2017. Why has regional income convergence in the US declined? _Journal of Urban Economics_ 102:76–90. 

- Garcia, Daniel and Raven Molloy. 2023. Can measurement error explain slow productivity growth in construction? Finance and Economics Discussion Series 2023-052, Federal Reserve Board. 

- Gechter, Michael and Nick Tsivanidis. 2023. Spatial spillovers from high-rise developments: Evidence from the Mumbai Mills. Working paper, University of California Berkeley, Haas School of Business. 

- Gerardi, Kristopher, Eric Rosenblatt, Paul S. Willen, and Vincent Yao. 2015. Foreclosure externalities: New evidence. _Journal of Urban Economics_ 87:42–56. 

- Glaeser, Edward and Joseph Gyourko. 2018. The economic implications of housing supply. _Journal of Economic Perspectives_ 32(1):3–30. 

- Glaeser, Edward L. and Joseph Gyourko. 2005. Urban decline and durable housing. _Journal of Political Economy_ 113(2):345–375. 

- Glaeser, Edward L., Joseph Gyourko, and Raven Saks. 2005 _a_ . Why is Manhattan so expensive? Regulation and the rise in housing prices. _Journal of Law and Economics_ 48(2):331–369. 

- Glaeser, Edward L., Joseph Gyourko, and Raven E. Saks. 2005 _b_ . Why have housing prices gone up? _American Economic Review_ 95(2):329–333. 

- Glaeser, Edward L. and Erzo F. P. Luttmer. 2003. The misallocation of housing under rent control. _American Economic Review_ 93(4):1027–1046. 

- Glaeser, Edward L. and Bryce A. Ward. 2009. The causes and consequences of land use regulation: Evidence from Greater Boston. _Journal of Urban Economics_ 65(3):265–278. 

- Nicolás. 2022. effects from new 

- González-Pampillón, Spillover housing supply. _Regional Science and Urban Economics_ 92:103759. 

- Goolsbee, Austan and Chad Syverson. 2023. The strange and awful path of productivity in the US construction sector. National Bureau of Economic Research Working Paper 30845. 

107 

- Gorback, Caitlin S. and Benjamin J. Keys. 2023. Global capital and local assets: House prices, quantities, and elasticities. Technical report. Working paper, University of Pennsylvania, Wharton School of Business. 

- Greaney, Brian. 2019. Housing constraints and spatial misallocation: Comment. Working paper, University of Washington, Department of Economics. 

- Greenaway-McGrevy, Ryan, Gail Pacheco, and Kade Sorensen. 2021. The effect of upzoning on house prices and redevelopment premiums in Auckland, New Zealand. _Urban Studies_ 58(5):959–976. 

- Greenaway-McGrevy, Ryan and Peter C.B. Phillips. 2023. The impact of upzoning on housing construction in Auckland. _Journal of Urban Economics_ 136:103555. 

- Greenwald, Daniel L. and Adam Guren. 2021. Do credit conditions move house prices? Technical report, National Bureau of Economic Research. 

- Gruber, Jonathan, Amalie Jensen, and Henrik Kleven. 2021. Do people respond to the mortgage interest deduction? quasi-experimental evidence from denmark. _American Economic Journal: Economic Policy_ 13(2):273–303. 

- Guerrieri, Veronica, Daniel Hartley, and Erik Hurst. 2013. Endogenous gentrification and housing price dynamics. _Journal of Public Economics_ 100:45–60. 

- Gupta, Arpit, Stijn Van Nieuwerburgh, and Constantine Kontokosta. 2022. Take the Q train: Value capture of public infrastructure projects. _Journal of Urban Economics_ 129:103422. 

- Gyourko, Joe and Jacob Krimmel. 2021. The impact of local residential land use restrictions on land values across and within single family housing markets. _Journal of Urban Economics_ 126(103374):1–14. 

- Gyourko, Joseph, Jonathan S. Hartley, and Jacob Krimmel. 2021. The local residential land use regulatory environment across us housing markets: Evidence from a new Wharton index. _Journal of Urban Economics_ 124:103337. 

- Gyourko, Joseph, Christopher Mayer, and Todd Sinai. 2013. Superstar cities. _American Economic Journal: Economic Policy_ 5(4):167–199. 

- Gyourko, Joseph and Sean E. McCulloch. 2024. The distaste for housing density. Technical report, National Bureau of Economic Research. 

- Gyourko, Joseph and Raven Molloy. 2015. Regulation and housing supply. In Gilles Duranton, Vernon Henderson, and William Strange (eds.) _Handbook of Regional and Urban Economics_ , volume 5B. Amsterdam: Elsevier, 1289–1337. 

- Gyourko, Joseph and Albert Saiz. 2004. Reinvestment in the housing stock: The role of construction costs and the supply side. _Journal of Urban Economics_ 55(2):238–256. 

- Gyourko, Joseph and Albert Saiz. 2006. Construction costs and the supply of housing structure. _Journal of Regional Science_ 46(4):661–680. 

108 

- Gyourko, Joseph, Albert Saiz, and Anita A. Summers. 2008. A new measure of the local regulatory environment for housing markets: The Wharton Residential Land Use Regulatory Index. _Urban Studies_ 45(3):693–729. 

- Hamilton, Bruce W. 1975. Zoning and property taxation in a system of local governments. _Urban Studies_ 12(2):205–211. 

- Hamilton, Bruce W. 1976. Capitalization of intrajurisdictional differences in local tax prices. _American Economic Review_ 66(5):743–753. 

- Han, Lu, Liwa Rachel Ngai, and Kevin D Sheedy. 2022. _To Own Or to Rent?: The Effects of_ . 

- _Transaction Taxes on Housing Markets_ Centre for Economic Policy Research. 

- Handbury, Jessie, Samuel K. Hugues, and Benjamin J. Keys. 2024. Segmentations and returns on rental housing. Working paper, University of Pennsylvania, Wharton School. 

- Harberger, Arnold C. 1954. Monopoly and resource allocation. _American Economic Review_ 44(2):77–87. 

- Haughwout, Andrew, James Orr, and David Bedoll. 2008. The price of land in the New York metropolitan area. _Current Issues in Economics and Finance_ 14(3). 

- Henderson, J. Vernon, Tanner Regan, and Anthony J. Venables. 2021. Building the city: From slums to a modern metropolis. _Review of Economic Studies_ 88(3):1157–1192. 

- Henderson, J. Vernon and Anthony J. Venables. 2009. The dynamics of city formation. _Review of Economic Dynamics_ 39(2):233–254. 

- Herkenhoff, Kyle F., Lee E. Ohanian, and Edward C. Prescott. 2018. Tarnishing the golden and empire states: Land-use restrictions and the us economic slowdown. _Journal of Monetary Economics_ 93:89–109. 

- Hilber, Christian and Frédéric Robert-Nicoud. 2013. On the origins of land use regulations: Theory and evidence from us metro areas. _Journal of Urban Economics_ 75(1):29–43. 

- Hilber, Christian and Olivier Schöni. 2022. _Housing policy and affordable housing_ . Centre for Economic Performance, London School of Economics and Political . . . . 

- Hilber, Christian A. L. and Christopher Mayer. 2009. Why do households without children support local public schools? Linking house price capitalization to school spending. _Journal of Urban Economics_ 65(1):74–90. 

- Hilber, Christian A. L. and Wouter Vermeulen. 2016. The impact of supply constraints on house prices in england. _Economic Journal_ 126(591):358–405. 

- Hilber, Christian AL and Tracy M Turner. 2014. The mortgage interest deduction and its impact on homeownership decisions. _Review of Economics and statistics_ 96(4):618–637. 

- Hornbeck, Richard and Daniel Keniston. 2017. Creative destruction: Barriers to urban growth and the Great Boston Fire of 1872. _American Economic Review_ 107(6):1365–1398. 

109 

- Howard, Greg and Jack Liebersohn. 2021. Why is the rent so darn high? The role of growing demand to live in housing-supply-inelastic cities. _Journal of Urban Economics_ 124:103369. 

- Howard, Greg, Jack Liebersohn, and Adam Ozimek. 2023. The short-and long-run effects of remote work on US housing markets. _Journal of Financial Economics_ 150(1):166–184. 

- Hsiao, Allan. 2023. Sea level rise and urban adaptation in Jakarta. Working paper, Princeton University. 

- Hsieh, Chang-Tai and Enrico Moretti. 2019. Housing constraints and spatial misallocation. _American Economic Journal: Macroeconomics_ 11(2):1–39. 

- Ihlanfeldt, Keith R. 2007. The effect of land use regulation on housing and land prices. _Journal of Urban Economics_ 61(3):420–435. 

- ˙Imrohoro˘glu, Ay¸se, Kyle Matoba, and ¸Selale Tüzel. 2018. Proposition 13: An equilibrium analysis. _American Economic Journal: Macroeconomics_ 10(2):24–51. 

- Jackson, Kristoffer. 2016. Do land use regulations stifle residential development? Evidence from California cities. _Journal of Urban Economics_ 91:45–56. 

- Jackson, Kristoffer Kip. 2018. Regulation, land constraints, and California’s boom and bust. _Regional Science and Urban Economics_ 68:130–147. 

- Jia, Ning, Raven Molloy, Christopher Smith, and Abigail Wozniak. 2023. The economics of internal migration: Advances and policy questions. _Journal of economic literature_ 61(1):144– 180. 

- Justiniano, Alejandro, Giorgio E Primiceri, and Andrea Tambalotti. 2019. Credit supply and the housing boom. _Journal of Political Economy_ 127(3):1317–1350. 

- Kahn, Matthew E., Ryan Vaughn, and Jonathan Zasloff. 2010. The housing market effects of discrete land use regulations: Evidence from the California coastal boundary zone. _Journal of Housing Economics_ 19(4):269–279. 

- Kalouptsidi, Myrto. 2014. Time to build and fluctuations in bulk shipping. _American Economic Review_ 104(2):564–608. 

- Kok, Nils, Paavo Monkkonen, and John M. Quigley. 2014. Land use regulations and the value of land and housing: An intra-metropolitan analysis. _Journal of Urban Economics_ 81:136–148. 

- Kopczuk, Wojciech and David Munroe. 2015. Mansion tax: The effect of transfer taxes on the residential real estate market. _American economic Journal: economic policy_ 7(2):214–257. 

- Koster, Hans R. A. 2024. The welfare effects of greenbelt policy: Evidence from England. _Economic Journal_ 134(657):363–401. 

- Koster, Hans R. A., Jos van Ommeren, and Piet Rietveld. 2013. Is the sky the limit? High-rise buildings and office rents. _Journal of Economic Geography_ 14(1):125–153. 

110 

- Krimmel, Jacob. 2021. Reclaiming local control: School finance reforms and housing supply restrictions. In _FRB Working Paper_ . 

- Krimmel, Jake and Betty X. Wang. 2024. Upzoning with strings attached: Evidence from Seattle’s Affordable Housing Mandate. Working paper, Federal Reserve Board. 

- Kuhlmann, Daniel. 2021. Upzoning and single-family housing prices: A (very) early analysis of the Minneapolis 2040 plan. _Journal of the American Planning Association_ 87(3):383–395. 

- Kulka, Amrita. 2019. Sorting into neighborhoods: The role of minimum lot sizes. In _Conference paper, APPAM 41st Annual Fall Research Conference, Denver, CO_ . 

- Kulka, Amrita, Aradhya Sood, and Nicholas Chiumenti. 2022. How to increase housing affordability: Understanding local deterrents to building multifamily housing. Technical report, Working Papers, Warwick University, Department of Economics. 

- Landvoigt, Tim, Monika Piazzesi, and Martin Schneider. 2015. The housing market (s) of San Diego. _American Economic Review_ 105(4):1371–1407. 

- Lebret, Daniel, Crocker H. Liu, and Maxence Valentin. 2025. Carrot and stick zoning. Working paper, Cornell University, SC Johnson College of Business. 

- Li, Xiaodi. 2021. Do new housing units in your backyard raise your rents? _Journal of Economic Geography_ 22(6):1309–1352. 

- Liang, Linlin, Adam Staveski, and Alex Horowitz. 2024. Minneapolis land use reforms offer a blueprint for housing affordability. Technical report, The Pew Charitable Trusts. 

- Listokin, David and David B. Hattis. 2005. Building codes and housing. _Cityscape_ 8(1):21–67. 

- Liu, Crocker, Stuart S. Rosenthal, and William C. Strange. 2018. The vertical city: Rent gradients and spatial structure. _Journal of Urban Economics_ 106:101–122. 

- Liu, Liyi, Doug McManus, and Elias Yannopoulos. 2022. Geographic and temporal variation in housing filtering rates. _Regional Science and Urban Economics_ 93:103758. 

- Lutz, Chandler and Ben Sand. 2023. Highly disaggregated land unavailability. Working paper, York University, Department of Economics. 

- Määttänen, Niku and Marko Terviö. 2014. Income distribution and housing prices: An assignment model approach. _Journal of Economic Theory_ 151(0):381–410. 

- Macek, James. 2024. Housing regulation and neighborhood sorting across the United States. Working Paper, University of Toronto, Rotman School of Business. 

- Mast, Evan. 2023. JUE Insight: The effect of new market-rate housing construction on the low-income housing market. _Journal of Urban Economics_ 133:103383. 

- Mast, Evan. 2024. Warding off development: Local control, housing supply, and nimbys. _Review of Economics and Statistics_ 106(3):671–680. 

111 

- Mayer, Christopher J. and C. Tsuriel Somerville. 2000. Land use regulation and new construction. _Regional Science and Urban Economics_ 30(6):639–662. 

- McDonald, John F. 1979. _Economic analysis of an urban housing market_ . New York: Academic Press. 

- McDonald, John F. 1981. Capital-land substitution in urban housing: A survey of empirical estimates. _Journal of Urban Economics_ 9(2):190–211. 

- McMillen, Daniel P. and John F. McDonald. 2002. Land values in a newly zoned city. _The Review of Economics and Statistics_ 84(1):62–72. 

- Mehrotra, Neil, Matthew A. Turner, and Juan Pablo Uribe. 2024. Does the US have an infrastructure cost problem? Evidence from the Interstate Highway System. _Journal of Urban Economics_ forthcoming. 

- Mense, Andreas. 2025. The impact of new housing supply on the distribution of rents. _Journal of Political Economy Macroeconomics_ 3(forthcoming). 

- Mills, Edwin S. 1969. The value of urban land. In Harvey S. Perloff (ed.) _The Quality of the Urban Environment_ . Baltimore md: Resources for the Future, 231–253. 

- Mleczko, Matthew and Matthew Desmond. 2023. Using natural language processing to construct a National Zoning and Land Use Database. _Urban Studies_ 60(13):2564–2584. 

- Raven. 2020. The effect of on A 

- Molloy, housing supply regulation housing affordability: review. _Regional Science and Urban Economics_ 80(C):1–5. 

- Molloy, Raven, Charles G. Nathanson, and Andrew Paciorek. 2022. Housing supply and affordability: Evidence from rents, housing consumption and household location. _Journal of Urban Economics_ 129. 

- Murphy, Alvin. 2018. A dynamic model of housing supply. _American Economic Journal: Economic Policy_ 10(4):243–267. 

- Muth, Richard F. 1964. The derived demand curve for a productive factor and the industry supply curve. _Oxford Economic Papers_ 16(2):221–234. 

- Muth, Richard F. 1969. _Cities and Housing_ . Chicago: University of Chicago Press. 

- Muth, Richard F. 1975. Numerical solution of urban residential land-use models. _Journal of Urban Economics_ 4(2):307–332. 

- Nathanson, Charles G. 2023. Trickle-down housing economics. Working paper, Northwestern University, Kellog School of Management. 

- Nikolakoudis, George. 2024. The economics of segmented housing markets. Unpublished, Princeton University. 

- Oates, Wallace E. 1972. Fiscal federalism. _HarcourtBrace Jovanovich Inc_ . 

112 

- Olsen, Edgar O. 1987. The demand and supply of housing service: a critical survey of the empirical literature. In Edwin S. Mills (ed.) _Handbook of Regional and Urban Economics_ , volume 2. North-Holland: Elsevier, 989–1022. 

- Ortalo-Magné, Francois and Sven Rady. 2006. Housing market dynamics: On the contribution of income shocks and credit constraints. _Review of Economic Studies_ 73(2):459–485. 

- Oster, Sharon M. and John M. Quigley. 1977. Regulatory barriers to the diffusion of innovation: Some evidence from building codes. _Bell Journal of Economics_ 8(2):361–377. 

- Overman, Henry G., Diego Puga, and Matthew A. Turner. 2008. Decomposing the growth in residential land in the United States. _Regional science and urban economics_ 38(5):487–497. 

- Owens III, Raymond, Esteban Rossi-Hansberg, and Pierre-Daniel Sarte. 2020. Rethinking Detroit. _American Economic Journal: Economic Policy_ 12(2):258–305. 

- Paciorek, Andrew. 2013. Supply constraints and housing market dynamics. _Journal of Urban Economics_ 77:11–26. 

- Parkhomenko, Andrii. 2023. Local causes and aggregate implications of land use regulation. _Journal of Urban Economics_ 138:103605. 

- Peng, Xuequan Elsie. 2023. The dynamics of urban development: Evidence from land use reform in New York. Working Paper, Department of Economics, University of Pennsylvania. 

- Pennington, Kate. 2021. Does building new housing cause displacement? The supply and demand effects of construction in San Francisco. Working paper, University of California, Berkeley. 

- Pines, David and Efraim Sadka. 1985. Zoning, first-best, second-best, and third-best criteria for allocating land for roads. _Journal of Urban Economics_ 17(2):167–183. 

- Quigley, John M. and Steven Raphael. 2005. Regulation and the high cost of housing in California. _American Economic Review_ 95(2):323–328. 

- Quintero, Luis. 2023. Fewer players, fewer homes: Concentration and the new dynamics of housing supply. Working Paper 18-18, Johns Hopkins University, Carey Business school. 

- Redding, Stephen J. 2025. Quantitative urban economics. In Dave Donaldson and Stephen J. Redding (eds.) _Handbook of Regional and Urban Economics_ , volume (this volume). Amsterdam: Elsevier. 

- Roback, Jennifer. 1982. Wages, rents and the quality of life. _Journal of Political Economy_ 90(6):1257–1278. 

- Rosenthal, Stuart S. 2014. Are private markets and filtering a viable source of low-income housing? Estimates from a “repeat income” model. _American Economic Review_ 104(2):687– 706. 

113 

- Rosenthal, Stuart S. and William C. Strange. 2008. The attenuation of human capital spillovers. _Journal of Urban Economics_ 64(2):373–389. 

- Rossi-Hansberg, Esteban, Pierre-Daniel Sarte, and Raymond Owens III. 2010. Housing externalities. _Journal of Political Economy_ 118(3):485–535. 

- Rossi-Hansberg, Esteban, Pierre-Daniel Sarte, and Felipe Schwartzman. 2019. Cognitive hubs and spatial redistribution. Technical report, National Bureau of Economic Research #26267. 

- Ruggles, Steven, Sarah Flood, Matthew Sobek, Daniel Backman, Annie Chen, Grace Cooper, Stephanie Richards, Renae Rodgers, and Megan Schouweiler. 2024. Ipums usa: Version 15.0 [dataset]. Technical report, IPUMS, Minneapolis, mn. 

- Rust, John. 1987. Optimal replacement of GMC bus engines: An empirical model of Harold Zurcher. _Econometrica_ :999–1033. 

- Sahn, Alexander. 2021. Racial diversity and exclusionary zoning: Evidence from the great migration. _Journal of Politics_ forthcoming. 

- Saiz, Albert. 2010. The geographic determinants of housing supply. _Quarterly Journal of Economics_ 125(3):1253–1296. 

- Sattinger, Michael. 1993. Assignment models of the distribution of earnings. _Journal of Economic Literature_ 19(1):831–880. 

- Schmitz, James A. 2020. Solving the housing crisis will require fighting monopolies in construction. Working Papers 773, Federal Reserve Bank of Minneapolis. 

- Schuetz, Jenny, Rachel Meltzer, and Vicki Been. 2011. Silver bullet or Trojan horse? The effects of inclusionary zoning on local housing markets in the United States. _Urban studies_ 48(2):297–329. 

- Severen, Christopher and Andrew J. Plantinga. 2018. Land-use regulations, property values, and rents: Decomposing the effects of the California Coastal Act. _Journal of Urban Economics_ 107:65–78. 

- Shan, Hui. 2011. The effect of capital gains taxation on home sales: Evidence from the taxpayer relief act of 1997. _Journal of Public Economics_ 95(1-2):177–188. 

- Shanks, Brendan. 2021. Land use regulations and housing development: Evidence from tax parcels and zoning bylaws in Massachusetts. Working paper, Ludwig Maximilien University Munich, Department of Economics. 

- Shertzer, Allison, Tate Twinam, and Randall P Walsh. 2016. Race, ethnicity, and discriminatory zoning. _American Economic Journal: Applied Economics_ 8(3):217–246. 

- Shertzer, Allison, Tate Twinam, and Randall P Walsh. 2018. Zoning and the economic geography of cities. _Journal of Urban Economics_ 105:20–39. 

114 

- Sinai, Todd and Joel Waldfogel. 2005. Do low-income housing subsidies increase the occupied housing stock? _Journal of public Economics_ 89(11-12):2137–2164. 

- Soltas, Evan. 2024 _a_ . Tax incentives and the supply of low-income housing. _Working paper,_ mit . 

- Soltas, Evan J. 2024 _b_ . The price of inclusion: Evidence from housing developer behavior. _Review of Economics and Statistics_ 106(6):1588–1606. 

- Sommer, Kamila and Paul Sullivan. 2018. Implications of us tax policy for house prices, rents, and homeownership. _American Economic Review_ 108(2):241–274. 

- Song, Jaehee. 2024. The effects of residential zoning in US housing markets. Working paper, University of Colorado-Boulder. 

- Spader, Jonathan. 2024. Has housing filtering stalled? Heterogeneous outcomes in the American Housing Survey, 1985–2021. _Housing Policy Debate_ :1–23. 

- Stacy, Christina, Timothy Hodge, Timothy Komarek, Chris Davis, Eleanor Noble, Jorge Morales-Burnett, and Amy Rogin. 2023. The impact of inclusionary zoning and rent control on housing affordability and access to opportunity. In _2023 APPAM Fall Research Conference_ . APPAM. 

- Stokes, H. Kemble. 1981. An examination of the productivity decline in the construction industry. _The Review of Economics and Statistics_ 64:495–502. 

- Sveikauskas, Leo, Samuel Rowe, James Mildenberger, Jennifer Price, and Arthur Young. 2016. Productivity growth in construction. _Journal of Construction Engineering and Management_ 142(10):1–8. 

- Sweeney, James L. 1974. Quality, commodity hierarchies, and housing markets. _Econometrica_ 42(1):147–167. 

- Syverson, Chad. 2011. What determines productivity? _Journal of Economic Literature_ 49(2):326–365. 

- Tan, Ya, Zhi Wang, and Qinghua Zhang. 2020. Land-use regulation and the intensive margin of housing supply. _Journal of Urban Economics_ 115:103199. 

- Thorsnes, Paul. 1997. Consistent estimates of the elasticity of substitution between land and non-land inputs in the production of housing. _Journal of Urban Economics_ 42(1):98–108. 

- Tiebout, Charles M. 1956. A pure theory of local expenditures. _Journal of Political Economy_ 64(5):416–424. 

- Titman, Sheridan. 1985. Urban land prices under uncertainty. _American Economic Review_ 75(3):505–514. 

- Tricaud, Clemence. 2025. Better alone? Evidence on the costs of intermunicipal cooperation. _American Economic Journal: Applied Economics_ 17(1):160–207. 

115 

- Turner, Matthew A. 2005. Landscape preferences and patterns of residential development. _Journal of Urban Economics_ 57(1):19–54. 

- Turner, Matthew A., Andrew Haughwout, and Wilbert Van Der Klaauw. 2014. Land use regulation and welfare. _Econometrica_ 82(4):1341–1403. 

- Wang, Xiao Betty. 2022. Housing market segmentation. Preprint, New York Universoty. 

- Wheeler, Harrison. 2022. Locally optimal place-based policies: Evidence from Opportunity Zones. Working paper, University of California Berkeley, Department of Economics. 

- Yoshida, Jiro. 2016. Structure depreciation and the production of real estate services. Processed, Smeal College of Business, Penn State University. 

- Yu, Rui. 2022. Returns to political contributions in local housing markets. Technical report, Working Paper, University of Pennsylvania. 

- Yu, Yue. 2024. The local and aggregate effects of land-use regulation on farmland protection. Working paper, University of Toronto. 

- Zabel, Jeffrey and Maurice Dalton. 2011. The impact of minimum lot size regulations on house prices in Eastern Massachusetts. _Regional Science and Urban Economics_ 41(6):571–583. 

- Howard. 2022. Consumer cities: The role of 

- Zhang, housing variety. Working paper, Columbia University. 

116 


