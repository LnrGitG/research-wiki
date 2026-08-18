---
title: NBER-CRIW-2026-Ch8-Qin-Flood-Risk-Insurance-w35204
type: paper
source_pdf: raw/papers/NBER-CRIW-2026-Ch8-Qin-Flood-Risk-Insurance-w35204.pdf
converted: 2026-08-18
---

### NBER WORKING PAPER SERIES 

FLOOD RISK, INSURANCE, AND HOUSING IN THE UNITED STATES 

Suvy Qin John L. Voorheis Working Paper 35204 http://www.nber.org/papers/w35204 

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 May 2026 

Any opinions and conclusions expressed herein are those of the authors and do not represent the views of the U.S. Census Bureau. The Census Bureau has ensured appropriate access and use of confidential data and has reviewed these results for disclosure avoidance protection (Project 7505723:  CBDRBFY25-CES025-010, CBDRB FY26 045, and CBDRB-FY26-0145). The views expressed herein are those of the authors and do not necessarily reflect the views of the National Bureau of Economic Research. 

NBER working papers are circulated for discussion and comment purposes. They have not been peerreviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications. 

© 2026 by Suvy Qin and John L. Voorheis. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source. 

Flood Risk, Insurance, and Housing in the United States Suvy Qin and John L. Voorheis NBER Working Paper No. 35204 May 2026 JEL No. Q0, Q5, Q54, R30 

### **<u>ABSTRACT</u>** 

Flooding is among the most salient natural hazards facing households in the United States. A large body of evidence has documented a pattern of disproportionate social vulnerability in floodplains. However, little evidence exists on how household-level exposure to flood risk is distributed. We fill this gap by combining parcel-level flood risk with confidential linked survey and administrative data held at the US Census Bureau. Although net migration to Census blocks in floodplains has increased in recent years, there has been essentially no net migration to parcels with flood risk or change in the overall share of households living in floodplains. Income gradients in flood risk are highly non-linear at the household level, with slightly negative income gradients for the bottom 90 percentiles of the income distribution that are dwarfed by disproportionate exposure in the top decile, especially when considering multiple property ownership. This nonlinearity is largely driven by differences in building type and homeownership within narrow income groups. In contrast to the conclusions in the literature using aggregate data, our household-level analysis suggests that households in floodplains are less disadvantaged and increasingly protected from the impacts of flooding, even as a vulnerable subpopulation of low-income, uninsured homeowners remains. 

Suvy Qin University of California, Berkeley suvyq@berkeley.edu 

John L. Voorheis U.S. Census Bureau Department of Economics john.l.voorheis@census.gov 

# **1 Introduction** 

Flooding is one of the most common and costly natural disaster risks in the US. Yet, there is little to no work using household-level microdata to document _who_ is exposed to flood risk and invests in adaptation, the economic costs of flood risk exposure, and how these relationships have evolved over time and space. This paper is the first to fill this lacuna by providing granular household-level estimates of flood risk across socioeconomic characteristics, using novel linked administrative data. As flood risk is the product of both the likelihood of a flood event (exposure) and the potential impacts of flooding (vulnerability), this paper provides new evidence on how differences in exposure vs. vulnerability might translate to disparities in flood risk across household characteristics, while allowing for better measurement of the housing stock at risk of flooding. 

Until now, the main constraint in building this body of evidence has typically been the lack of high quality microdata that allow for the measurement of both flood risk exposure (which we define as being located in a floodplain) and household- and individual-level characteristics, resolved at the housing-unit level (Kousky, 2019). However, this paper leverages a new US Census Bureau microdata infrastructure—the Environmental Impacts Frame (Voorheis et al., 2023)—linked with surveys and administrative records to provide the first comprehensive household-level evidence nationally. These microdata allow us to measure and describe how flood risk exposure and insurance costs vary along individual-level household characteristics that are not historically available in this setting. Moreover, the granular microdata allow us to estimate insurance coverage rates among different households to understand who is uninsured and the implications for the housing sector. Using this linked microdata infrastructure, we evaluate how insurance coverage varies by owner or renter status, household income, race/ethnicity, flood risk exposure, and property attributes. 

We establish several key new facts about the distribution of flood risk exposure. First, while the total number of people exposed to flood risk has increased from 1999 to 2023, the _share_ of households exposed to flood risk has remained stable—largely due to offsetting migration flows between risky and non-risky homes. Secondly, we find that while there is generally a negative relationship between flood risk exposure and income for those in the bottom 90 percent of the income distribution, flood risk 

1 

exposure has increased among the highest income households, particularly in the past decade—a fact that is masked by aggregate data. We find that when we condition on housing tenure and building types, there is almost no relationship between flood risk and income for households in the bottom 90 percent of the income distribution. Third, we document several trends related to insurance and flood risk among homeowners: uninsurance rates are higher in flood-exposed areas; lower-income, Hispanic, and Black households are less likely to be insured; potential flood losses as a fraction of household income in a given year are highest for the lowest-income households. Given these descriptive facts, we conclude that the distribution of flood risk has become skewed towards high-income and/or less vulnerable individuals in the time period of our study. However, there exists a vulnerable subgroup of uninsured homeowners in risky areas (which tend to be lower income and more likely to be Hispanic or non-Hispanic Black) who may have limited ability to mitigate potential flood losses. 

_Contributions to the literature:_ Overall, this paper demonstrates that the use of household-level microdata allows us to avoid issues of aggregation bias and to provide new evidence on the national distribution of flood risk exposure and adaptation behaviors, how these relationships have varied over time, and the heterogeneity in these relationships by key demographic characteristics. Leveraging this data allows us to make several contributions to the literature studying flood risk exposure and its economic consequences. 

There are two competing narratives in this existing literature. One strand of literature has shown that lower-income and minority homeowners are more likely to be exposed or vulnerable to flood risk using climate modeling or discrete choice estimates (Wing et al., 2022; Tate et al., 2021; Bakkensen and Ma, 2020; Fox et al., 2024; Gandhi et al., 2022; Remo et al., 2016), yet these estimates often rely on publicly available aggregate demographic data or are limited to a specific region.<sup>1</sup> A second strand of literature has argued that high income individuals may sort into areas with flood risk because they are able to self-insure against this risk and they have preferences for the amenities that coincide with floodplains (Graff Zivin et al., 2023; Druckenmiller et al., 2024). 

> 1An exception is a one-time report produced by the Federal Emergency Management Agency (FEMA) that linked 2015 National Flood Insurance Program (NFIP) policyholder data with 2015 American Community Survey microdata to show that average household incomes are lower in flood zones (FEMA, 2018). 

2 

Given that flood risk and sociodemographic characteristics can vary at a fine geographic scale, the use of household-level data allows us to disambiguate these two narratives. Not only can we provide a more complete typology of flood risk exposure, but also we can show how the use of confidential microdata can avoid spurious correlations produced when using aggregate data. We leverage a combination of administrative and survey records to document the distribution of flood risk not only by income or race/ethnicity, but also by tenure, housing type, age, and over time. Moreover, this literature often focuses on measuring flood risk based on primary residences, yet we are able to provide the first evidence on how the inclusion of second or non-primary homes alters the distribution of flood risk. More importantly, the literature has demonstrated that the geographic scale of an analysis can alter the measurement of the distribution of flood risk, with potential undercounting of vulnerable populations (Hinojos et al., 2023; Tanir et al., 2021). We show that some socioeconomic relationships would be missed or wrong if one were to use aggregate data, highlighting the importance of using household-level microdata to accurately document who is exposed to flood risk and who faces greater vulnerability to flood risk. 

Additionally, a rapidly growing literature has focused on estimating the determinants of demand for flood insurance (Wagner, 2022; Mulder, 2024; Bradt et al., 2021; Ortega and Petkov, 2025; Petkov and Ortega, 2025; Netusil et al., 2021; Gallagher, 2014), finding that households have low willingnessto-pay and are sensitive to information about flood risk. Instead, we focus on measuring the flood risk protection gaps that have been studied in homeowner’s insurance (Sastry et al., 2024). Our paper is closest to Amornsiripanitch et al. (2025), which studies flood underinsurance gaps for single-family residences and how they correlate with tract-level income and minority population shares. Since we are able to directly observe households’ insurance purchase behavior and demographic information without relying on fuzzy linking methods, we are able to avoid issues of aggregation bias (more details below) and provide new evidence on underinsurance for the full income distribution and how this has evolved over time. 

3 

# **2 Measuring Flood Risk** 

To understand the characteristics of the population who may suffer flood losses, we need a workable definition of flood risk and tractable ways of assigning risk or related measures to individual households. Flood risk is ultimately the product of exposure to a physical hazard (the likelihood of flooding) and vulnerability to the hazard (the characteristics of people and housing units that increase the likelihood of damages). Rather than attempting to measure a single risk measure at the household level, our approach in this paper is to assign physical hazard exposure to households and then explore how the distribution of this exposure varies with economic, housing, and demographic characteristics, which in turn are related to the vulnerability of households. 

Our main way of capturing physical hazard exposure is the Federal Emergency Management Agency’s National Flood Hazard Layer (NFHL) data (commonly referred to as “FEMA Flood Maps”). NFHL maps delineate the likelihood of flooding across areas with more than negligible flooding potential. These maps only capture riverine and coastal flooding and do not capture areas likely to experience rainfall-driven flash flooding (pluvial flooding). The studies underlying these maps are purely backward-looking and consider the historical likelihood of flooding based on geography, hydrology, and historic weather patterns. FEMA defines three main areas or flood zones of interest: Zone A, which captures areas with at least a 1% chance of a riverine flooding event in a given year; Zone V, which captures areas with at least a 1% chance of a coastal flooding event in a given year, and “500 year floodplains,” which capture areas with less than 1% but greater than 0.2% chance of flooding in a given year. Areas in Zone A and V are designated by FEMA as “Special Flood Hazard Areas” (SFHA), and homes in these areas are subject to stricter rules around flood insurance purchase and mandated elevation of new construction. 

The NFHL geospatial data consist of very detailed polygons delineating the boundaries of all FEMA-defined flood zones. These maps are intended to map potential exposure to flood inundation at a very fine geographic scale. This means that assigning floodplain status to an individual household requires some nuance. Some but not all households live on properties entirely inside or outside of floodplains. However, in practice, many millions of households are on or near the boundary of 

4 

floodplains. To handle these cases, we consider two nested definitions of floodplain exposure: “parcel level exposure,” defined as any portion of the property associated with an address lying inside a floodplain; and “building level exposure,” defined as either the geocoded latitude and longitude of an address lying inside a floodplain, or any portion of the building footprint associated with an address lying inside a floodplain. Building-level floodplain exposure is relevant for flood insurance: conventional mortgage underwriting requires flood insurance (most often provided by the National Flood Insurance Program) if any part of the main building underlying the mortgage is in a SFHA floodplain. Parcel-level floodplain exposure captures a broader set of properties where backwardlooking estimates suggest the property, but not the dwelling, may be subject to flooding on a 100or 500-year time span; however, these are precisely the set of properties who would be exposed to flooding in the event of unexpected large floods driven by climate change. To demonstrate the nuances of our floodplain exposure definitions, Figure 1 zooms in on neighborhoods in Orange County, CA where we have overlaid NFHL flood maps on top of parcel boundaries (in gray) and building footprints (in black). In the figure, there are parcels that spatially intersect with a floodplain even though the building footprint does not intersect with a floodplain, which is the case for both types of floodplains (SFHA floodplains and 500-year floodplains). 

To construct these household-level exposure measures, we utilize the Census Bureau’s Master Address File (MAF) combined with property-level data from Lightbox. The MAF is the master list of the addresses and associated geographies (state, county, Census tract) and location information (latitude and longitude) of all housing units known to the Census Bureau. The MAF contains both housing units in single family buildings and multiunit structures. Lightbox contains detailed geospatial data on parcel boundaries and building footprints; these are derived from data used to administer local property taxes, and thus the unit of analysis is a tax parcel. For single family homes, tax parcels have a one-to-one mapping to housing units; for housing units in multiunit structures, parcel-to-unit relationships are more complicated. We combine the MAF and Lightbox data using geospatial methods, assigning the main tax parcel (and main building) in the Lightbox data associated with each address (Master Address File ID, MAFID) based on its latitude and longitude. We then 

5 

geospatially intersect the parcel boundaries and building footprints data with the NFHL flood maps, assigning parcel- and building-level exposure as described above. 

To supplement the exposure measures based on FEMA floodplains, we also use flood risk data produced by the First Street Foundation (FSF). The FSF flood maps are generated in a slightly different manner than the FEMA flood maps. Instead of a backward-looking calculation of flooding likelihood, the FSF maps utilize information from downscaled climate projections to estimate the likelihood of flooding (riverine, coastal, or pluvial) over the next 30 years (a timespan chosen to coincide with the average length of a conventional mortgage in the US). This approach takes into account the effect of climate change on increasing precipitation, which can increase the likelihood of pluvial and riverine flooding events. The FSF flood maps are then used to calculate a property-level “Flood Factor” risk score ranging from 1-10, where 1 corresponds to minimal flood risk and scores from 2-10 represent flood likelihood similar to the 100- and 500-year FEMA-defined floodplains. Because the FSF method not only captures different kinds of flooding events but also explicitly estimates future flood likelihood, substantial mismatch between FEMA floodplains and FSF flood risk exists at the property level. We also use their estimates of average annual losses (AALs) in later analyses as a measure of expected flood damages in dollars.<sup>2</sup> 

# **3 Data** 

To understand the distribution of flood risk exposure across people and households, we link the exposure data to multiple administrative records, property tax records and survey datasets in the Census Bureau’s data linkage infrastructure. The Census data linkage infrastructure assigns unique person-level and housing unit-level linkage keys (Personal Identification Keys, PIKs and MAFIDs) to confidential datasets, allowing researchers to link across multiple datasets and within datasets over time (Wagner and Lane, 2014). We construct two main analysis datasets for the purpose of this paper—one based on population-level administrative records, and a second based on the American 

> 2These AALs are produced using both established and FSF-specific depth damage functions that use various inputs (i.e. property characteristics) to predict what percent of a property’s improvement value is expected to be damaged due to flooding risks (FSF, 2021). 

6 

Community Survey, a large nationally representative sample survey of the population. 

The universe-level dataset is based on the Environmental Impacts Frame (EIF) microdata infrastructure (Voorheis et al., 2023). For each year from 1999-2023, we combine an enhanced version of the EIF residential history module<sup>3</sup> with the EIF demographic spine (which contains basic demographic information for all Social Security Number holders) and the Census Opportunity Project Databank (which harmonizes income information from IRS forms 1040, 1099, and W-2s) (Chetty et al., 2020). Because income and residence information has different reference periods in many of the key administrative records datasets used here, we merge each year _t_ of the EIF residential history information with year _t −_ 1 of the administrative tax data. We assign tax unit level information (the tax unit’s adjusted gross income) from form 1040 to the primary tax filer and individual-level information (wages from form W-2) to all wage earners. We then define a hybrid adjusted gross income (AGI) concept, which is equal to the tax unit’s AGI for all primary tax filers and equal to total wage income for individuals who are not primary or secondary tax filers. 

Our desired unit of analysis is the household level, necessitating aggregation steps from the merged person-level EIF and Databank files. We first assign the time-invariant demographic characteristics of the “householder” to each household (indexed by MAFID), where the householder is defined as the oldest member of the tax unit with the highest AGI in a MAFID. We then aggregate income to the household level by summing all unique hybrid AGI values within a MAFID, using the same rules used in the construction of the gridded EIF (Voorheis et al., 2024). For the purposes of our subsequent analysis, we exclude any households with zero or negative household hybrid AGI, including non-filer households.<sup>4</sup> 

For the period after 2013, we are able to add additional detail on homeownership and housing characteristics. To construct these household-level measures, we combine information from IRS form 1098 (an information return issued by mortgage lenders which allows us to identify homeowners with a mortgage), with assessment and deeds records from local property tax data (collected and 

> 3The EIF residential history module combines address information from IRS, CMS, SSA, USPS, and other administrative data to identify a best address for each person in the US in a given year, and then enhances this with additional commercial data and some cross-year imputation when an individual does not appear in other administrative records. 4 Given our analysis requires income information, we exclude households where all residents are non-filers. 

7 

made available to Census by Black Knight, LLC, now a subsidiary of Intercontinental Exchange). Combining these three datasets allows us to flag all occupied housing units as owned or rented. For all owned homes, we additionally assign a home value based on estimates of market value from local tax authorities, or, if this information is missing, estimated value from Black Knight’s automated valuation model. 

We also construct an indicator for whether a housing unit is a single family home or part of a multiunit structure by combining Lightbox parcel boundary data with the MAF. We intersect all geocoded MAFIDs with Lightbox parcels—this can result in a one-to-one relationship between a MAFID and parcel, a many-to-one relationship between a single parcel and many MAFIDs (which is common for rental apartment buildings), or a more complicated many-to-many relationship, where each of a set of MAFIDs is matched to multiple parcels, and each of the parcels matches to multiple MAFIDs (which is common for condominium buildings, which commonly have overlapping stacked parcel boundaries in the data, one for each unit in the building). Since we only have certainty about the first group, we identify any one-to-one match as a single-family home and assume all other MAFIDs are in multiunit buildings. We combine the EIF-Databank household file with the housing characteristics and this single family home indicator by MAFID and then merge the assignments of floodplain exposure described above. 

Finally, for some analyses, we require more detail that does not exist in the administrative records described above, so we utilize the 2005-2023 American Community Survey (ACS), which contain detailed information on housing and person-level characteristics, including homeowners’ insurance premiums. As the confidential version of the ACS is linkable by MAFID, we are able to merge the ACS microdata with the floodplain exposure measures described above and proceed with our analysis. Tables 1 and 2 show summary statistics of baseline characteristics for the households in FEMA floodplains vs. not in floodplains in the EIF and ACS data. 

8 

# **4 Facts About the Distribution of Flood Risk** 

With this unique constellation of data in hand, we are now able to provide new evidence on the household-level distribution of exposure to flood risk. We first take a broad view of how the population living in floodplains has evolved over time, and then we systematically examine how exposure to flood risk via residential locations varies by demographic, economic, and housing characteristics. We then examine how ownership of secondary properties affects these observed distributions. 

Our household-level data provide a unique lens into these issues: due to the extremely local nature of flood risk, existing evidence utilizing aggregate statistics on population characteristics may produce misleading results via aggregation bias. By focusing on households’ true exposure and building our analysis up from microdata, we avoid these biases and are able to uncover previously unobserved facts about the distribution of flood risk in the United States. 

## **4.1 Trends in Exposure** 

Coastal counties in the United States have seen increases in population in recent decades, and several recent studies have projected an increase in population in flood-prone areas globally (Hauer et al., 2024; Rogers et al., 2025; Neumann et al., 2015; Indaco and Ortega, 2024). However, since aggregate population data are almost always too coarse to match the granularity of flood risk mapping, these trends may not necessarily represent substantial changes in the population exposed to flood risk at the household level, and it is not clear that global trends will hold in all countries. 

Figure 2 shows the population level (upper panel) and share (lower panel) of households residing in floodplains from 1999-2023, for each of our floodplain exposure measures outlined in Section 2. Across all exposure definitions, the number of households has increased substantially. For our most expansive FEMA floodplain definition (parcel-level exposure to A, V, or 500-year floodplains), the number of households exposed has increased from around 11 million in 1999 to over 15 million in 2023; for the most restrictive definition (building-level exposure to SFHA floodplains), exposure has increased from around 3.8 million to over 4.9 million households over the same period. The First 

9 

Street Foundation Flood Factor exposure measure has similarly seen large increases, from around 13 million to over 17.5 million from 1999-2023. 

However, this increase in population in floodplains seems largely to represent overall population growth, not increasing relative exposure. If anything, as the bottom panel of Figure 2 shows, the share of households in floodplains has either not dramatically changed or slightly declined for all floodplain exposure definitions. The share of households in FSF floodplains is about 0.3 percentage points lower in 2023 compared to 1999 (falling from 17 percent to 16.7 percent); our preferred expansive FEMA floodplain definition (any parcel-level floodplain exposure) has remained between 14.2 and 14.4 percent over the same period. 

What can account for the seemingly contradictory trends that flood-prone areas seem to be increasing in population while the share of households actually exposed to flood risk has stayed stable or declined? We argue that some previous research has made erroneous inference from aggregate migration statistics, an example of aggregation bias (Colmer et al., 2026). 

To illustrate this problem and how these seemingly contradictory trends can be rationalized, we estimate year-to year migration flows in our microdata using two floodplain definitions: Census block flood exposure (defined as any household in a Census block lying in a floodplain) or household level exposure (any parcel-level floodplains concept we have used as our preferred measure). Figure 3 summarizes the results of this migration flow calculation—while there has been a consistent trend of more migration from non-floodplain blocks to floodplain blocks over the last two decades, this is not true at the parcel level. Inflows and outflows to and from floodplains have remained quite evenly matched over time—there has been no flood risk bias to migration flows since 1999. Figure 1 illustrates how aggregation at the Census block level (red boundaries) could hide variation in flood risk exposure _within_ the Census block geography, since not all parcels in a given Census block are actually inside the floodplain. 

However, the overall stability in net migration to flood-prone parcels may mask heterogeneity in _who_ is moving to and from these areas. Figure 4 summarizes the fraction of households who live in floodplains across different flood exposure definitions, split by percentile of the income distribution 

10 

(only the 25th, 50th, 75th and top percentile bins are shown for compactness). Across most risk definitions, the share of people in the lower income percentiles living in flood plains has remained quite stable over time. However, there have been large increases in the share of people exposed to floodplains at the top of the income distribution, especially since 2010. The share of top income earners living in floodplains by the FSF definitions has increased from about 16 percent in 2010 to 18.5 in 2023; our preferred measure shows increases from around 17 to around 19 percent over the same period. 

## **4.2 Who Is Exposed to Flood Risk?** 

The trends in rates of floodplain exposure over time imply important cross-sectional differences in who is exposed to flood risk, a topic which we now turn to. We will focus on five dimensions of interest: housing tenure (renters vs. homeowners), income, wealth (captured by gross housing value of owned homes), race and ethnicity, and building type (single vs. multifamily). Throughout this section, we will be interested in two related questions: how do baseline rates of exposure vary across demographic, economic, and housing characteristics? and what is the distribution of demographic, economic, and housing characteristics of the flood risk exposed household population? 

Figure 5 illustrates the first important distribution fact: renter households are exposed to higher levels of flood risk than homeowner households. This gap has been consistent over the last decade, slightly widening in the last 5 years. By the end of our sample, the gap is more than 5 percentage points—18 percent of renters live in floodplains, compared to around 12 percent for homeowners. Renter households face many of the same potential losses as homeowners—dislocation, health impacts, loss of personal property (though this may vary to some extent based on building type, a dimension we will explore further)—but importantly are not liable for flood-related damages on the physical building they reside in. 

Figure 6 picks up where Figure 4 left off, showing the distribution of flood risk across income percentiles for 2013 and 2023. These graphs plot at each point the average exposure (fraction of households in floodplains) within single percentile bins of the household income distribution. Several 

11 

features of these income gradients are immediately apparent. First, lower income households (in the bottom quartile of the income distribution) are exposed to higher flood risk than higher income households up until the top decile of income. Notably, the very top of the income distribution is exposed to much higher flood risk than any other income percentile—19 percent of the top 1 percent of income earners are in floodplains, compared to 16 percent of households around the 25th percentile and 13 percent of households around the 75th percentile. Additionally, the income gradients in flood risk have rotated counterclockwise over time—flood risk has increased for the top of the income distribution and decreased for the bottom 75 percent. 

Since we have already seen that there are stark differences across renters and owners in flood risk and homeownership is (weakly) increasing in income, it is logical to presume that there may be important heterogeneity underlying the baseline income gradients. Figure 7 illustrates this, splitting the previous income gradients in flood risk by tenure. Income gradients for renters in the bottom 90 percent are a bit flatter, but overall patterns remain largely consistent, with the outsized importance of the top 1% remaining salient throughout. 

Even within renters and homeowners in narrow income bins, there are still large differences in how floodplain exposure might impact individual households. One important dimension within these groups is the type of physical structure they reside in. Single family homes, absent interventions like elevating the structure, are at higher risk of inundation than housing units in most multiunit buildings, which are almost always on higher floors and thus physically protected from all but the most severe flooding events (and units higher up in larger buildings are protected for all conceivable flooding events). 

To explore this, Figure 8 splits the income gradients further into four categories: homeowners in single family homes, homeowners in multiunit structures (e.g. condos), renters in single family homes, and renters in multiunit structures (e.g. apartment buildings). Within tenure-by-building type groups, it is notable that with the exception of owners in multiunit buildings, the observed negative income gradient in the bottom 90 percent of the income distribution almost totally disappears; _only_ the large spike in flood risk for the top 1 percent remains a salient feature. Homeowners in multiunit 

12 

structures do seem to have important income gradients, but this may in part represent low-income, high wealth retirees living in retirement communities in high amenity, but flood-prone areas (e.g. coastal Florida). 

The age distribution of flood risk may thus be important— not only because of potential amenityseeking retirement locations, but also because age may be a dimension of vulnerability to flooding. Figure 9 shows the distribution of floodplain exposure by single year of age, race/ethnicity, and tenure. Black and Asian renters exhibit negative age gradients in exposure, while most other groups have at least weakly positive gradients—in 2013, Black renters in their twenties were about 4 percentage points more likely to be floodplains than Black renters in their 80s; White homeowners are almost completely opposite, with elderly White homeowners being about 4 percentage points more likely to be in floodplains than younger White homeowners. The increase in floodplain exposure for renters of all groups between 2013 and 2023 is concentrated in older renters, and this is particularly true for White renter households—White renters in their 80s are nearly 2 percentage points more likely to be in floodplains in 2023 relative to 2013. 

Our results so far have examined differential exposure to floodplains by narrow socioeconomic categories, but these different groups have varying population sizes, so these relationships do not cleanly map to an enumeration of who is exposed to flood risk. Figures 10 and 11 bridge this gap by showing the population totals in floodplain and non-floodplain areas by tenure, income, and race/ethnicity (Figure 11) or building type (Figure 10). First, we see the echo of the disproportionality in exposure at the top of the income distribution: there are many more people in floodplains in the top 5 percent of the income distribution than in any other income percentile group. Adding across these groups, we find that only a small fraction of households in floodplains are both vulnerable and face risk not compensated by their living arrangements—the vast majority of people in floodplains are either high income, live in structures that provide protection against flood risk, or are renters (and thus face only losses of personal property, not residential property). 

There is substantial heterogeneity in how flood risk interacts with the built environment across geographic areas. One particular dimension of this heterogeneity lies in coastal flood risk vs. inland 

13 

flood risk. To explore whether this heterogeneity affects inferences about income gradients in flood risk, we reproduce Figure 8 but split the sample into households in coastal counties vs. households in non-coastal counties, in Figure 12. The overall pattern of relatively flat income gradients in the bottom 90 percent of the income distribution and substantially higher flood risk for the top of the income distribution holds in both areas. However, there is both a higher baseline level of flood risk in coastal counties and a more pronounced spike in exposure for the top of the income distribution. 

To demonstrate the importance of using granular microdata to measure who is exposed to flood risk, we can also take one key relationship—income gradients—and show what is missed when using aggregate data on household income. Importantly, using publicly-available aggregate data produces slightly different relationships between flood risk exposure and household income, particularly for the upper tail of the income distribution, as shown in Figure 13. The income gradient on the left is constructed using Census block groups’ median household income and flood zones, while the income gradient on the right is constructed using First Street Foundation’s public data on the number of homes in each Flood Factor group for each Census tract. Both figures use the 5-year ACS to assign Census geometries into a household income vigintile. When comparing Figure 6 (which uses household-level microdata) to Figure 13, it is clear that aggregate data miss the sharp upward increase in flood risk exposure among the highest-income households. 

## **4.3 Housing Wealth and Flood Risk Exposure** 

Finally, we consider an alternate lens on the distribution of floodplain exposure. We have thus far considered how exposure varies across households on the basis of income and other characteristics, but what is relevant for policy considerations is not just the number of households exposed, but also the value of the homes that are exposed to flood risk (as property damage is the dominant dimension of loss due to flooding). Figure 14 shows the distribution of flood risk by race/ethnicity of homeowner and owner-occupied home value. Similar to income, the highest value homes are substantially more likely to be in floodplains—more than a quarter of the top 1 percent most valuable homes owned by White, Asian, and Hispanic homeowners are in floodplains (around 15 percent for Black owners of 

14 

the most valuable properties), whereas only 10-18 percent of median valued homes are in floodplains. There has been a slight downward trend in floodplain exposure for lower valued homes that is more pronounced for some subgroups—for instance, 15 percent of Hispanic homeowners owning a home around the 25th percentile in 2013 were in floodplains, compared to around 10 percent in 2023. The most valuable homes, on the other hand, uniformly have more flood risk exposure in 2023 vs. 2013 for all race/ethnicity groups. 

This exercise, however, has relied on only the primary occupancy to assign exposure. In principle, households can own multiple homes; this may be particularly common in areas with high flood risk (e.g. vacation homes near bodies of water). We can identify these secondary occupancy homes by combining our disparate data sources: by linking individual ownership of all properties (from the assessment records described above) with the EIF residential history file, we can identify properties owned by an individual that are not occupied by any individuals in the EIF. These properties we tag as “second homes.” Figure 15 extends one of our main results so far—the nonlinearity of income gradients in floodplain exposure—to accommodate second homes—where second home inclusive exposure is now the share of households in each income percentile bin who own _any_ home in a floodplain, primary or secondary occupancy. Exposure in this definition is higher at all percentiles, but particularly so at the bottom and top of the income distribution. Around 13 percent of the bottom percentile is exposed to floodplains in their primary home, but over 18 percent are exposed when considering all owned homes; this difference is driven by the fact that some individuals with low incomes (usually due to transitory business losses) are in practice high-wealth individuals. The top of the income distribution sees similar deviations: around 18 percent of households at the top of the distribution are in floodplains when considering primary homes only, while 27 percent are exposed to floodplains when considering all homes. 

The importance of second homes becomes increasingly apparent when we consider the total value of homes exposed to floodplains. Figure 16 shows the proportion of home value owned by individuals in each income percentile separately for floodplains and non-floodplain areas. Outside of floodplains, there is a definite pattern of inequality, but the top 1% of the income distribution only owns about 

15 

3.5% of the total home value—this is substantially more equally distributed than income, where the income share held by the top 1 percent is around 20.7% in 2023 (World Inequality Database, n.d.; Chancel et al., 2022). The distribution of home value by income in floodplains is substantially more unequal however: the top 1% share of income hold 7% of total home value. 

# **5 Insurance and Adaptation to Flood Risk** 

Given that insurance is an important margin for homeowners to mitigate flood risk exposure, we next turn to our analysis of the linked ACS sample. While flood insurance coverage is not directly measured in Census data, the ACS does ask homeowners about home insurance coverage more broadly.<sup>5</sup> We use this sample to answer these questions: (1) who is insured or protected against flood risk and how has this changed over time? (2) what are the potential economic consequences of these trends? 

To answer the first question, we calculate the share of homeowners that report no insurance coverage in the ACS. In this section, we focus exclusively on homeowners without a mortgage, as nearly all homeowners with a mortgage are required to purchase some form of homeowner’s insurance by their lender. Figure 17 plots the uninsured rate from 2005 to 2023, separately by floodplain status, showing that the share of homeowners who are uninsured has consistently been higher in floodplain areas. Figure 18 shows that uninsured homeowners are lower income than insured homeowners in both floodplain and non-floodplain areas, while Figure 19 shows that Black and Hispanic homeowners are more likely to be uninsured in both floodplain and non-floodplain areas. These relationships are persistent across nearly two decades. Additionally, using the overall floodplain exposure rates from the previous section we can back out the converse: flood risk exposure by insurance status—in 2023, uninsured homeowners without a mortgage were about 4 percentage points more likely to be in a floodplain than insured homeowners (about 15 percent vs. about 11 percent). 

Given the increasing concern about insurance affordability, we next examine how insurance premiums and expected damages have evolved, especially as a function of household income. We 

> 5The exact question asked of homeowners is: “What was the annual payment for fire, hazard, and flood insurance on this property?”, and homeowners with a mortgage are asked: “Does your regular monthly mortgage payment include payments for fire, hazard, or flood insurance on this property?” 

16 

first plot the average insurance premium over time by floodplain status in Figure 20, which shows that average insurance premiums are higher in flood-prone areas and have been steadily increasing over time. One criterion for insurance affordability is that the ratio of insurance premium to household income is no more than 1%, as considered by FEMA in its affordability report (FEMA, 2018)). Thus, we compute the average share of a household’s income that is paid out in annual insurance premiums, as shown in Figure 21, which illustrates that insurance costs have steadily risen as a share of household income with a sharp increase in recent years. However, Figure 22 shows that there is a sharp negative gradient with household income, as the average ratio of insurance premium to household income is below 1% for the top income vigintile of homeowners, while the average ratio is 10% to 15% for homeowners in the bottom income vigintile. Another way to show this is Figure 23, which plots the average uninsured rate by household income vigintile, separately by floodplain status. There is a clear negative gradient that underscores the high uninsured rates among lower-income households, which is consistent with research that finds households are sensitive to prices. Consistent with results in the previous section, the average insurance premium is higher for high-income homeowners, but the _relative_ financial burden is greater for low-income homeowners. 

Next, we consider the economic consequences of flood risk exposure using the average annual loss estimates produced by First Street Foundation’s climate modeling, and a similar pattern emerges. Figure 24 shows a negative income gradient between flood damages as a share of income and household income vigintiles, regardless of households’ insurance status and floodplain status. Households in a floodplain have a higher ratio of flood damage to income, but the ratio of expected losses relative to household income is pretty similar for both insured and uninsured households. Together, these figures underscore the fact that uninsured households are exposed to sizable losses, especially at the lower-end of the income distribution. 

While we have focused on purchasing insurance as the main way to adapt to flood risk, homeowners could alternatively choose to invest in “self-protection” (Ehrlich and Becker, 1972). One way for a household to self-insure against flood inundation is to relocate to an area protected by levees or other flood control technologies. Figure 25 shows the fraction of households who live in 

17 

levee-protected areas by income percentile. A very small fraction of households (around 1.5 percent nationally) live in levee-protected areas; through the bottom 90 percent of the income distribution, there is no monotonic patterns of levee-protection that would suggest a tradeoff between this type of protection and insurance. However, there is a marked decrease in prevalence at the top of the income distribution that is the mirror image of our previous income gradient results. 

The other main way that households who are located in non-leveed floodplains can engage in self-protection is by elevating their properties. NFIP participation requires homes in SFHAs built after a community’s adoption of its first flood map to be elevated above the “base flood elevation.”<sup>6</sup> We classify homes built in SFHAs as being adapted (i.e. elevated) if it was built after the first year in which a community adopts a flood hazard map.<sup>7</sup> We then merge this with the ACS sample to examine whether living in an elevated home is a complement or substitute to insurance. Table 3 describes the average uninsured rate among owners separately by floodplain status and home elevation status. The table suggests that homeowners who live in non-elevated homes are more likely to be uninsured overall for both floodplain and non-floodplain areas, which suggests that elevation and insurance seem to be complements and not substitutes. However, this pattern could reflect the different prices faced by different households in adapted vs. non-adapted homes. Table 3 also lists the average insurance premiums and household income, which shows that higher-income households are more likely to live in elevated homes in both floodplain and non-floodplain areas, suggesting that the higher average premiums for elevated homes could reflect the newer construction of elevated homes and/or higher willingness-to-pay for insurance among high-income households. Given the limitations of the survey data, these relationships are far from conclusive, but they suggest that the uninsurance gap might be even more consequential if uninsured homeowners are also less protected against flood risk via other adaptation methods. 

> 6The base flood elevation (BFE) is the elevation of surface water from a flood that has a 1% change of equaling or exceeding that level in any given year, according to FEMA. 

> 7For Florida, we have also collected public data on elevation certificates at the address-level from Florida’s Division of Emergency Management. 

18 

# **6 Discussion** 

In this paper, we leverage household-level administrative and survey microdata to provide new facts about the distribution of flood risk in the US. To summarize, we observe the following empirical regularities: 1) renter households are exposed to higher flood risk than homeowner households; 2) residents of multifamily buildings are exposed to higher flood risk than residents of single family homes; 3) high income households are more exposed to flood risk than lower-income homeowners, especially when considering multiple home ownership; 4) homeowners without homeowners insurance are more likely to be in floodplains; and 5) low-income homeowners face higher insurance premium cost burdens and are less likely to carry homeowners insurance. Together, these results allow us to define a typology of floodplain-exposed households along income, homeownership, structure type, and insurance lines. 

The first three of these facts highlight dimensions along which flood risk is _negatively_ related to vulnerability—renters, residents of multi-family structures, and higher income households all have some degree of protection against flood damages. High income households are to some extent selfinsured due to their economic resources; renter households are protected from residential property losses by their tenure (but still face potential losses of personal property and housing services); and residents of multifamily structures are physically protected from inundation in most cases (though this is only strictly true for units in multistory buildings in the second or higher floors). However, our final two facts highlight a vulnerable subpopulation living in floodplains—homeowners in single family homes who do not carry homeowners insurance and who are also more likely to be low income. 

Thus, our typology of flood risk-exposed households includes 12 different groups broken out by income, structure, or property damage vulnerability, as outlined in Table 4. Of these groups, only low-income, uninsured homeowners of single family homes experience vulnerability across all three dimensions. Yet, this group is quite small—only around 1.74 percent of households in floodplains are in this category.<sup>8</sup> This typology underlines a pattern we have observed throughout this paper: 

> 8For this calculation, we define a low-income/high-income binary based on median income. This number would be even smaller if one were to use income deciles, for example. 

19 

although some pockets of vulnerability exist, the population of households in floodplains is by and large not a vulnerable population. This stands in sharp contrast to an existing body of work that has documented a correlation between _community_ -level vulnerability and floodplain exposure.<sup>9</sup> 

Why do our results and typology deviate from the conclusions of the previous literature? We argue that the primary cause is a type of aggregation bias which we have observed several times in this paper. This aggregation bias arises due to within-geography variation in the characteristics of individuals, particularly along dimensions related to economic resources. Previous research on the distribution of air pollution (Colmer et al., 2024, 2026) have noted that even in cases where a natural hazard does not substantially vary within small geographies (as is the case for fine particulate matter), there can be large aggregation bias solely driven by the within-geography distribution of income. In the case of air pollution, even though there is little variation in PM2 _._ 5 within Census tracts, because there is a lot of variation in income, the individual-level income gradients in pollution exposure deviate meaningfully from neighborhood-level income gradients. In the case of flood risk, the aggregation bias is potentially more severe: unlike air pollution, there _is_ meaningful variation in floodplain exposure even within Census tracts (or blocks, as illustrated in Figure 1), _and this variation is related to variation in other socioeconomic characteristics like income and homeownership, which also vary within small geographies._ 

We have seen this bias throughout our investigation—our facts about flood risk document that the relationship between income and flood risk is non-monotonic, with high-income households experiencing substantially more flood risk. Failure to grapple with the risk of this bias can lead to incorrect inferences about the relationship between income and flood risk—any approach that estimates such a relationship at the Census tract (or block/block group/county) level will conclude that there is a sharp, monotonically decreasing gradient (as in Figure 13), suggesting that the incidence of environmental hazards falls on the most disadvantaged. This inference is misleading; when using high-quality population-level microdata, the most advantaged (highest income households) have substantially _higher_ levels of exposure to flood risk. When accounting for tenure and building type, 

> 9We recognize that there are other dimensions of vulnerability which we do not explore in this paper, but which we leave to future work. 

20 

there is almost _no_ relationship between flood risk and income for the bottom 90 percent of the income distribution (as seen in figure 8). We observe a similar instance of aggregation bias in the study of floodplain-related migration—any study of migration that does not account for aggregation bias will incorrectly conclude that households are moving to areas with flood risk, when in fact there has been essentially zero net migration to flood-risky _parcels_ in the last two decades. 

This study underlines the importance of using the highest quality individual-level microdata— such as the Census Environmental Impacts Frame (Voorheis et al., 2023)—when analyzing the distribution of environmental hazards and producing new evidence to inform decision-making by stakeholders. Many disaster preparedness and mitigation activities aim to ensure that those most vulnerable to natural hazards are prioritized for assistance or investment. However, to effectuate this goal, one must to be able to accurately describe the exposures and potential risks of vulnerable populations. Approaches that rely only on aggregated demographic data will only ever be able to provide an incomplete—and often erroneous—picture. Future work should use the highest quality microdata to contribute to our understanding of the distribution of environmental hazards beyond specific hazards—such as exposure to flood risk as in this paper or air pollution as in recent literature—to encompass the broadest set of natural and environmental hazards facing the people, households, and businesses of the United States. Future research can also provide evidence on how the adaptation methods we have highlighted might mitigate the natural hazard risks and losses experienced by households and businesses. 

21 

# **References** 

- **Amornsiripanitch, Natee, Siddhartha Biswas, John Orellana-Li, and David Zink** , “Measuring flood underinsurance in the USA,” _Nature Climate Change_ , September 2025, _15_ (9), 971–977. Publisher: Nature Publishing Group. 

- **Bakkensen, Laura A. and Lala Ma** , “Sorting over flood risk and implications for policy reform,” _Journal of Environmental Economics and Management_ , November 2020, _104_ , 102362. 

- **Bradt, Jacob T., Carolyn Kousky, and Oliver E.J. Wing** , “Voluntary purchases and adverse selection in the market for flood insurance,” _Journal of Environmental Economics and Management_ , 2021, _110_ , 102515. 

- **Chancel, Lucas, Thomas Piketty, Emmanuel Saez, and Gabriel Zucman** , “World Inequality Report 2022,” Technical Report, Cambridge, MA 2022. 

- **Chetty, Raj, Nathaniel Hendren, Maggie R Jones, and Sonya R Porter** , “Race and Economic Opportunity in the United States: an Intergenerational Perspective*,” _The Quarterly Journal of Economics_ , May 2020, _135_ (2), 711–783. 

- **Colmer, Jonathan, Jay Shimshack, and John Voorheis** , “Aggregation Bias Distorts Pollution Exposure Estimates,” _Mimeo_ , 2026. 

- **Colmer, Jonathan M, Suvy Qin, John L Voorheis, and Reed Walker** , “Income, Wealth, and Environmental Inequality in the United States,” Working Paper 33050, National Bureau of Economic Research October 2024. 

- **Druckenmiller, Hannah, Yanjun (Penny) Liao, Sophie Pesek, Margaret Walls, and Shan Zhang** , “Removing development incentives in risky areas promotes climate adaptation,” _Nature Climate Change_ , September 2024, _14_ (9), 936–942. Publisher: Nature Publishing Group. 

- **Ehrlich, Isaac and Gary S. Becker** , “Market Insurance, Self-Insurance, and Self-Protection,” _Journal of Political Economy_ , 1972, _80_ (4), 623–648. Publisher: The University of Chicago Press. 

- **Federal Emergency Management Agency (FEMA)** , “An Affordability Framework for the National Flood Insurance Program,” Technical Report 2018. 

- **First Street Foundation (FSF)** , “The Cost of Climate: America’s Growing Flood Risk,” Technical Report 2021. 

- **Fox, Sean, Felix Agyemang, Laurence Hawker, and Jeffrey Neal** , “Integrating social vulnerability into high-resolution global flood risk mapping,” _Nature Communications_ , April 2024, _15_ (1), 3155. Publisher: Nature Publishing Group. 

- **Gallagher, Justin** , “Learning about an Infrequent Event: Evidence from Flood Insurance Take-Up in the United States,” _American Economic Journal: Applied Economics_ , July 2014, _6_ (3), 206–33. 

- **Gandhi, Sahil, Matthew E. Kahn, Rajat Kochhar, Somik Lall, and Vaidehi Tandel** , “Adapting to Flood Risk: Evidence from a Panel of Global Cities,” June 2022. Issue: 30137. 

22 

- **Graff Zivin, Joshua, Yanjun Liao, and Yann Panassi´e** , “How hurricanes sweep up housing markets: Evidence from Florida,” _Journal of Environmental Economics and Management_ , 2023, _118_ , 102770. 

- **Hauer, Mathew E., Sunshine A. Jacobs, and Scott A. Kulp** , “Climate migration amplifies demographic change and population aging,” _Proceedings of the National Academy of Sciences_ , January 2024, _121_ (3), e2206192119. Publisher: Proceedings of the National Academy of Sciences. 

- **Hinojos, Selena, Lauren McPhillips, Peter Stempel, and Caitlin Grady** , “Social and environmental vulnerability to flooding: Investigating cross-scale hypotheses,” _Applied Geography_ , August 2023, _157_ , 103017. 

- **Indaco, Agust´ın and Francesc Ortega** , “Adapting to Climate Risk? Local Population Dynamics in the United States,” _Economics of Disasters and Climate Change_ , March 2024, _8_ (1), 61–106. 

- **Kousky, Carolyn** , “The Role of Natural Disaster Insurance in Recovery and Risk Reduction,” _Annual Review of Resource Economics_ , October 2019, _11_ (Volume 11, 2019), 399–418. Publisher: Annual Reviews. 

- **Mulder, Philip** , “Mismeasuring Risk: The Welfare Effects of Flood Risk Information,” September 2024. 

- **Netusil, Noelwah R., Carolyn Kousky, Shulav Neupane, Will Daniel, and Howard Kunreuther** , “The Willingness to Pay for Flood Insurance,” _Land Economics_ , 2021, _97_ (1), 17–38. Number: 1 Publisher: University of Wisconsin Press. 

- **Neumann, Barbara, Athanasios T. Vafeidis, Juliane Zimmermann, and Robert J. Nicholls** , “Future Coastal Population Growth and Exposure to Sea-Level Rise and Coastal Flooding - A Global Assessment,” _PLOS ONE_ , March 2015, _10_ (3), e0118571. Publisher: Public Library of Science. 

- **Ortega, Francesc and Ivan Petkov** , “To improve is to change: The effects of Risk Rating 2.0 on flood insurance demand,” _Journal of Environmental Economics and Management_ , November 2025, _134_ , 103228. 

- **Petkov, Ivan and Francesc Ortega** , “Learning from experience: Flooding and insurance take-up in the flood zone and its periphery,” _Journal of Risk and Insurance_ , 2025, _92_ (2), 312–356. ~~e~~ print: https://onlinelibrary.wiley.com/doi/pdf/10.1111/jori.70002. 

- **Remo, Jonathan W. F., Nicholas Pinter, and Moe Mahgoub** , “Assessing Illinois’s flood vulnerability using Hazus-MH,” _Natural Hazards_ , March 2016, _81_ (1), 265–287. 

- **Rogers, Justin S., Marco P. Maneta, Stephan R. Sain, Luke E. Madaus, and Joshua P. Hacker** , “The role of climate and population change in global flood exposure and vulnerability,” _Nature Communications_ , February 2025, _16_ (1), 1287. Publisher: Nature Publishing Group. 

- **Sastry, Parinitha, Ishita Sen, Ana-Maria Tenekedjieva, and Therese C. Scharlemann** , “The Insurance Protection Gap,” May 2024. 

23 

- **Tanir, Tugkan, Selina J. Sumi, Andre de Souza de Lima, Gustavo de A. Coelho, Sukru Uzun, Felicio Cassalho, and Celso M. Ferreira** , “Multi-scale comparison of urban socioeconomic vulnerability in the Washington, DC metropolitan region resulting from compound flooding,” _International Journal of Disaster Risk Reduction_ , July 2021, _61_ , 102362. 

- **Tate, Eric, Md Asif Rahman, Christopher T. Emrich, and Christopher C. Sampson** , “Flood exposure and social vulnerability in the United States,” _Natural Hazards_ , March 2021, _106_ (1), 435–457. 

- **Voorheis, John, Jonathan Colmer, Kendall Houghton, Eva Lyubich, Mary Munro, Cameron Scalera, and Jennifer Withrow** , “Building the Prototype Census Environmental Impacts Frame,” _US Census Bureau Center for Economic Studies Working Paper Series_ , 2023, (CES-23-20). 

   - **, , , , , , and** , “The Privacy-Protected Gridded Environmental Impacts Frame,” _US Census Bureau Center for Economic Studies Working Paper Series_ , 2024, (CES-24-74). 

- **Wagner, Deborah and Mary Lane** , “The Person Identification Validation System (PVS): Applying the Center for Administrative Records Research and Applications’(CARRA) Record Linkage Software,” _US Census Bureau Center for Economic Studies Working Paper Series_ , 2014, (CES14-01). 

- **Wagner, Katherine R. H.** , “Adaptation and Adverse Selection in Markets for Natural Disaster Insurance,” _American Economic Journal: Economic Policy_ , August 2022, _14_ (3), 380–421. 

- **Wing, Oliver E. J., William Lehman, Paul D. Bates, Christopher C. Sampson, Niall Quinn, Andrew M. Smith, Jeffrey C. Neal, Jeremy R. Porter, and Carolyn Kousky** , “Inequitable patterns of US flood risk in the Anthropocene,” _Nature Climate Change_ , February 2022, _12_ (2), 156–162. Publisher: Nature Publishing Group. 

- **World Inequality Database** , “World Inequality Database,” n.d. Accessed: April 2, 2026. 

24 

# **Figures and Tables** 

Figure 1: Example of Different Floodplain Exposure Definitions 



<!-- Start of picture text -->
33.824°N<br>33.822°N<br>Boundary Type<br>Building boundaries<br>Census block boundaries<br>33.820°N Parcel boundaries<br>Floodplain Type<br>500−year Floodplain<br>A or V Floodplain<br>33.818°N<br>33.816°N<br>117.814°W 117.812°W 117.810°W 117.808°W 117.806°W 117.804°W 117.802°W<br><!-- End of picture text -->

Source: National Flood Hazard Layer, USA Structures, and US Census Bureau. Notes: This figure plots the National Flood Hazard Layer from FEMA, parcel boundaries from Orange County, CA, building footprints from FEMA’s USA Structures dataset, and Census block boundaries from the US Census Bureau MAF/TIGER geographic database. 

25 

Figure 2: Population Level and Share Living in Floodplains in the US, 1999-2023 

#### (a) Households in floodplains 



<!-- Start of picture text -->
FSF Floodplain A or V Floodplain (Building) A or V Floodplain (Parcel)<br>10<br>17<br>4.8<br>16 9<br>4.4<br>15<br>8<br>14<br>4.0<br>13<br>2000 2005 2010 2015 2020 2000 2005 2010 2015 2020 2000 2005 2010 2015 2020<br>Any Floodplain (Building) Any Floodplain (Parcel)<br>10 15<br>14<br>9<br>13<br>12<br>8<br>11<br>2000 2005 2010 2015 2020 2000 2005 2010 2015 2020<br>Year<br>(b) Share of households in floodplains<br>FSF Floodplain A or V Floodplain (Building) A or V Floodplain (Parcel)<br>0.170 0.0505<br>0.0500 0.0960<br>0.169<br>0.0495 0.0955<br>0.168 0.0490<br>0.0950<br>0.0485<br>0.167<br>0.0945<br>0.0480<br>0.166<br>0.0475 0.0940<br>2000 2005 2010 2015 2020 2000 2005 2010 2015 2020 2000 2005 2010 2015 2020<br>Any Floodplain (Building) Any Floodplain (Parcel)<br>0.098<br>0.1440<br>0.097 0.1435<br>0.1430<br>0.096<br>0.1425<br>2000 2005 2010 2015 2020 2000 2005 2010 2015 2020<br>Year<br>Number of Households in Floodplain (in millions)<br>Fraction of Households in Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, First Street and National Flood Hazard Layer data. Notes: These figures plot the population levels and shares living in floodplains over time using the EIF and various definitions of floodplains based on the FEMA NFHL, Lightbox parcel and building boundaries, and FSF Flood Factor scores. 

26 

Figure 3: Migration Flows To and From Floodplains, Block vs. Parcel Exposure 



<!-- Start of picture text -->
FEMA, Block FEMA, Parcel<br>25<br>6.0<br>20<br>5.5<br>15<br>5.0<br>10<br>4.5<br>5<br>2000 2005 2010 2015 2020 2000 2005 2010 2015 2020 Flow Type<br>Floodplain to non−floodplain<br>FSF, Block FSF, Parcel<br>Non−floodplain to floodplain<br>20<br>7<br>15<br>10<br>6<br>5<br>2000 2005 2010 2015 2020 2000 2005 2010 2015 2020<br>Year<br>Population Migration Flow (in millions)<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the migration flows between floodplains and non-floodplains using various geographies to determine floodplain exposure. 

27 

Figure 4: Trends in the Share of the Population in Floodplains by Income, 1999-2023 



<!-- Start of picture text -->
A or V Floodplain (Building) A or V Floodplain (Parcel) Any Floodplain (Building)<br>0.07<br>0.14 0.12<br>0.06 0.11<br>0.12<br>0.10<br>0.05<br>0.10<br>0.09<br>0.04<br>0.08<br>0.08<br>2000 2005 2010 2015 2020 2000 2005 2010 2015 2020 2000 2005 2010 2015 2020<br>Any Floodplain (Parcel) FSF Floodplain<br>0.18 0.18 Income<br>Percentile<br>0.16 0.17<br>25<br>50<br>0.16<br>0.14 75<br>100<br>0.15<br>2000 2005 2010 2015 2020 2000 2005 2010 2015 2020<br>Year<br>Fraction of Households in Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the fraction of EIF households in floodplains over time, separately for 4 income percentiles. 

28 

Figure 5: Trends in the Share of the Population in Floodplains by Household Tenure, 1999-2023 



<!-- Start of picture text -->
A or V Floodplain (Building) A or V Floodplain (Parcel) Any Floodplain (Building)<br>0.20<br>0.15<br>0.10<br>0.05<br>2013 2015 2017 2019 2021 2023<br>Any Floodplain (Parcel) FSF Floodplain<br>0.20<br>0.15<br>Tenure<br>0.10 Homeowner<br>Renter<br>0.05<br>2013 2015 2017 2019 2021 20232013 2015 2017 2019 2021 2023<br>Year<br>Fraction of Households In Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the fraction of EIF households in floodplains by year, separately for homeowner and renter households. 

29 

Figure 6: Trends in the Share of the Population in Floodplains by Income Percentile: 2013 vs. 2023 



<!-- Start of picture text -->
A or V Floodplain (Building) A or V Floodplain (Parcel) Any Floodplain (Building)<br>0.07 0.14<br>0.12<br>0.06 0.12 0.11<br>0.10<br>0.05<br>0.10<br>0.09<br>0.04<br>0.08 0.08<br>0 25 50 75 100 0 25 50 75 100 0 25 50 75 100<br>Any Floodplain (Parcel) FSF Floodplain<br>0.19<br>0.18<br>0.18<br>Year<br>0.16<br>0.17<br>2013<br>0.14 0.16 2023<br>0.15<br>0.12<br>0 25 50 75 100 0 25 50 75 100<br>Income Percentile<br>Fraction of Households In Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox and National Flood Hazard Layer data. Notes: This figure plots the fraction of EIF households in floodplains across income percentiles, separately for 2013 and 2023. 

30 

Figure 7: Trends in the Share of the Population in Floodplains by Income Percentile & Tenure: 2013 vs. 2023 



<!-- Start of picture text -->
Homeowner Renter<br>0.18<br>0.250<br>0.16 0.225<br>Year<br>2013<br>0.200 2023<br>0.14<br>0.175<br>0.12<br>0 25 50 75 100 0 25 50 75 100<br>Income Percentile<br>Fraction of Households In Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the fraction of EIF households in floodplains across income percentiles, separately for 2013, 2023, and tenure status. 

31 

Figure 8: Trends in the Share of the Population in Floodplains by Income Percentile, Tenure, and Housing Type: 2013 vs. 2023 



<!-- Start of picture text -->
Homeowner, Multi−Family Homeowner, Single Family<br>0.22<br>0.16<br>0.20<br>0.14<br>0.18<br>0.12<br>0.16<br>0 25 50 75 100 0 25 50 75 100 Year<br>2013<br>Renter, Multi−Family Renter, Single Family 2023<br>0.32<br>0.20<br>0.28 0.18<br>0.16<br>0.24<br>0.14<br>0.20 0.12<br>0 25 50 75 100 0 25 50 75 100<br>Income Percentile<br>Fraction of Households In Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the fraction of EIF households in floodplains across income percentiles, separately for 2013, 2023, tenure status, and housing type. 

32 

Figure 9: Trends in the Share of the Population in Floodplains by Age, Tenure, and Race/Ethnicity: 2013 vs. 2023 



<!-- Start of picture text -->
Asian, Homeowner Asian, Renter Black, Homeowner<br>0.115<br>0.120 0.20<br>0.115 0.110<br>0.110 0.18 0.105<br>0.105 0.16 0.100<br>0.100<br>40 60 80 40 60 80 40 60 80<br>Black, Renter Hispanic, Homeowner Hispanic, Renter<br>0.19 0.18 0.23<br>0.22<br>0.17<br>0.16 0.21<br>0.15<br>0.14 0.20<br>0.13<br>40 60 80 40 60 80 40 60 80<br>White, Homeowner White, Renter Year<br>0.14<br>0.19 2013<br>0.13<br>0.12 0.18 2023<br>0.11 0.17<br>0.10 0.16<br>0.09<br>40 60 80 40 60 80<br>Age of Householder<br>Fraction of Households In Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the fraction of EIF households in floodplains across householder age, separately for 2013, 2023, tenure status, and race/ethnicity. 

33 

Figure 10: Trends in the Population in Floodplains by Income Percentile, Tenure, and Housing Type 



<!-- Start of picture text -->
In Any FEMA Floodplain Not In Floodplain<br>800<br>150<br>600<br>100 Household Type<br>Homeowner, Multi−Family<br>400<br>Homeowner, Single Family<br>Renter, Multi−Family<br>Renter, Single Family<br>50<br>200<br>0 0<br>0 25 50 75 100 0 25 50 75 100<br>Income Percentile<br>Number of Households (in thousands)<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the _number_ of EIF households in floodplains across income percentiles, separately for tenure status and housing type. 

34 

Figure 11: Trends in the Population in Floodplains by Income Percentile, Tenure, and Race/Ethnicity 



<!-- Start of picture text -->
In Any FEMA Floodplain Not In Floodplain<br>200<br>750<br>150<br>Household Type<br>Asian, Homeowner<br>500 Asian, Renter<br>Black, Homeowner<br>100<br>Black, Renter<br>Hispanic, Homeowner<br>Hispanic, Renter<br>White, Homeowner<br>250 White, Renter<br>50<br>0 0<br>0 25 50 75 100 0 25 50 75 100<br>Income Percentile<br>Number of Households (in thousands)<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the _number_ of EIF households in floodplains across income percentiles, separately for tenure status and race/ethnicity. 

35 

Figure 12: Share of the Population in Floodplains by Income Percentile, Tenure, and Housing Type, Split by Coastal vs. Non-coastal Counties 



Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the share of EIF households in floodplains across income percentiles, separately for tenure status and housing type, split by coastal vs. non-coastal counties. 

36 

Figure 13: Trends in the Share of the Population in Floodplains using Aggregate Data (a) Fraction of Population In A or V Floodplains (b) Fraction of Homes with Moderate Flood Risk (SFHA) using Census Block Group Centroids (FSF) in Census Tracts 



<!-- Start of picture text -->
9.0 20<br>8.5<br>18<br>8.0<br>16<br>7.5<br>14<br>7.0<br>25 50 75 100 25 50 75 100<br>Household income percentiles (2023 5−year ACS) Household income percentiles (2023 5−year ACS)<br>(Floodfactor score >2)<br>% of population in SFHA (CBG centroids) % of properties with at least moderate risk<br><!-- End of picture text -->

Source: American Community Survey, First Street Foundation data, and National Flood Hazard Layer data. Notes: The left panel is constructed by overlaying Census block group centroids with the National Flood Hazard Layer to identify which Census block groups are in A or V floodplains, and then the Census block group population shares are calculated as the Census block group population in a floodplain divided by the total population of all Census block groups in that income vigintile. The right panel is constructed using public First Street Foundation data that describes the total number of properties in each Flood Factor score (1-10) in a given Census tract, where the Census tract property shares are calculated as the total number of properties with a Flood Factor score greater than 2 divided by the total number of properties in all Census tracts in an income vigintile. Income vigintiles are constructed based on the median household income from the 2023 5-year ACS estimates for each respective Census geography. 

37 

Figure 14: Trends in the Share of the Population in Floodplains by Home Value Percentile and Race/Ethnicity: 2013 vs. 2023 



<!-- Start of picture text -->
Asian Black<br>0.25<br>0.150<br>0.20<br>0.125<br>0.15<br>0.100<br>0.10 0.075<br>0 25 50 75 100 0 25 50 75 100 Year<br>2013<br>Hispanic White 2023<br>0.25<br>0.25<br>0.20<br>0.20<br>0.15<br>0.15<br>0.10<br>0.10<br>0 25 50 75 100 0 25 50 75 100<br>Home Value Percentile<br>Fraction of Households In Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the _fraction_ of EIF households in floodplains in each home value percentile, separately for 2013, 2023, and race/ethnicity. 

38 

Figure 15: Trends in the Share of the Population in Floodplains by Income Percentile and Exposure Type 



<!-- Start of picture text -->
0.25<br>0.20 Exposure Type<br>Including Second Homes<br>Owner Occupied Homes Only<br>0.15<br>0 25 50 75 100<br>Income Percentile<br>Fraction of Households In Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the fraction of EIF households in floodplains in each income percentile, separately for whether second homes are included or excluded in the household exposure definition. For the second home inclusive definition, this figure plots the share of households in each income percentile bin who own _any_ home in a floodplain, primary or secondary occupancy 

39 

Figure 16: Trends in the Share of Total Housing Value Owned by Income Percentile and Floodplain Status 



<!-- Start of picture text -->
0.06<br>0.04 Floodplain Status<br>In Any FEMA Floodplain<br>Not In Floodplain<br>0.02<br>0 25 50 75 100<br>Income Percentile<br>Share of Total Housing Value Owned<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the fraction of total housing value owned (including second homes) that is in a FEMA floodplain and that is not in a FEMA floodplain. 

40 

Figure 17: Uninsured Rates by Floodplain Status, 2005-2023 



<!-- Start of picture text -->
0.30<br>0.25<br>Flood Risk<br>FEMA Floodplain<br>0.20 Not Floodplain<br>0.15<br>2005 2010 2015 2020<br>Year<br>Share Uninsured<br><!-- End of picture text -->

Source: American Community Survey, and National Flood Hazard Layer data. Notes: This figure plots the share of ACS households that are not insured over time, separately by floodplain status. 

Figure 18: Average Household Income by Insurance & Floodplain Status, 2005-2023 



<!-- Start of picture text -->
FEMA Floodplain Not Floodplain<br>100,000<br>Insurance<br>80,000<br>Coverage<br>Insured<br>Uninsured<br>60,000<br>40,000<br>2005 2010 2015 2020 2005 2010 2015 2020<br>Year<br>Average Income<br><!-- End of picture text -->

Source: Environmental Impacts Frame, American Community Survey, and National Flood Hazard Layer data. Notes: This figure plots the average household income of ACS households over time, separately by floodplain status and insurance status. 

41 

Figure 19: Uninsured Rates by Race/Ethnicity & Floodplain Status, 2005-2023 



<!-- Start of picture text -->
FEMA Floodplain Not Floodplain<br>0.4<br>Race/Ethnicity<br>0.3 Asian<br>Black<br>Hispanic<br>White<br>0.2<br>0.1<br>2005 2010 2015 2020 2005 2010 2015 2020<br>Year<br>Share Uninsured<br><!-- End of picture text -->

Source: Environmental Impacts Frame, American Community Survey, and National Flood Hazard Layer data. Notes: This figure plots the share of ACS households that are not insured over time, separately by floodplain status and race/ethnicity. 

Figure 20: Insurance Payment by Floodplain Status, 2005-2023 



<!-- Start of picture text -->
1400<br>1200<br>Flood Risk<br>FEMA Floodplain<br>Not Floodplain<br>1000<br>800<br>2005 2010 2015 2020<br>Year<br>Average Insurance Premium<br><!-- End of picture text -->

Notes: This figure plots the average insurance premium of ACS households over time, separately by floodplain status. 

42 

Figure 21: Insurance Payment as a Share of Household Income, 2005-2023 



<!-- Start of picture text -->
1.4<br>Floodplain Status<br>FEMA Floodplain<br>Not Floodplain<br>1.2<br>1.0<br>2005 2010 2015 2020<br>ACS Year<br>Average insurance payment to HH income ratio (%)<br><!-- End of picture text -->

Source: Environmental Impacts Frame, American Community Survey, and National Flood Hazard Layer data. Notes: This figure plots the average ratio of annual insurance premium to household income of ACS households over time, separately by floodplain status. 

43 

Figure 22: Insurance Payment as a Share of Household Income by Income Vigintiles & Floodplain Status, 2005-2023 



<!-- Start of picture text -->
0.100<br>0.075<br>Floodplain Status<br>FEMA Floodplain<br>0.050 Not Floodplain<br>0.025<br>0.000<br>25 50 75 100<br>Household Income Percentile<br>Average ratio of insurance payment to income<br><!-- End of picture text -->

Source: American Community Survey and National Flood Hazard Layer data. Notes: This figure plots the average ratio of annual insurance premium to household income of ACS households for each household income vigintile, separately by floodplain status. 

44 

Figure 23: Uninsured Rate by Income Vigintiles & Floodplain Status, 2005-2023 



<!-- Start of picture text -->
0.4<br>0.3<br>Floodplain status<br>FEMA Floodplain<br>Not Floodplain<br>0.2<br>0.1<br>25 50 75 100<br>Household Income Percentile<br>Average uninsured rate<br><!-- End of picture text -->

Source: Environmental Impacts Frame, American Community Survey and National Flood Hazard Layer data. Notes: This figure plots the average uninsured rate of ACS households for each household income vigintile, separately by floodplain status. 

45 

Figure 24: Average Flood Losses to Income Ratio by Income Percentile, Insurance Status, & Floodplain Status (Single-Family Buildings) 



<!-- Start of picture text -->
50<br>40<br>Floodplain<br>30 FEMA Floodplain<br>Not Floodplain<br>20 Insurance status<br>Insured<br>Uninsured<br>10<br>0<br>25 50 75 100<br>Household Income Percentile<br>Average AAL as % of HH Income<br><!-- End of picture text -->

Source: Environmental Impacts Frame, American Community Survey and National Flood Hazard Layer data. Notes: This figure plots the average ratio of expected annual flood losses to household income of ACS households for each household income vigintile, separately by floodplain status and insurance status. 

46 

Figure 25: Proportion of Households in Levee-protected Areas, by Income 



Source: Environmental Impacts Frame and National Flood Hazard Layer data. Notes: This figure plots the proportion of households in each income percentile who are located in a levee-protected area. 

47 

Table 1: Balance Table of Demographics and Housing by Floodplain Status (EIF Data) 

||FEMA Floodplain|Not Floodplain|Diference|
|---|---|---|---|
|Single Family Home|0.5655<br>(0.00012)|0.7186<br>(4.96e-05)|-0.1531|
|Homeowner|0.4981<br>(0.000129)|0.6103<br>(5.31e-05)|-0.1122|
|Coastline County|0.3965<br>(0.000115)|0.2455<br>(4.77e-05)|0.151|
|Household Income|126300<br>(226.1)|120600<br>(93.36)|5700|
|Home Value|592800<br>(187.8)|493300<br>(68.49)|99500|
|Age|57.46<br>(0.004689)|57.17<br>(0.001935)|0.29|
|Black|0.1175<br>(8.55e-05)|0.1203<br>(3.53e-05)|-0.0028|
|White|0.6237<br>(0.000125)|0.6614<br>(5.16e-05)|-0.0377|
|Asian|0.04097<br>(5.45e-05)|0.04559<br>(2.25e-05)|-0.00462|
|Hispanic|0.1651<br>(8.94e-05)|0.1278<br>(3.69e-05)|0.0373|
|Other Race Categories|0.05654<br>(5.67e-05)|0.04772<br>(2.34e-05)|0.00882|
|N|13,762,000|92,351,000||



Sources: Environmental Impacts Frame and National Flood Hazard Layer data. Notes: This table displays the average of various household characteristics from the Environmental Impacts Frame, separately by floodplain status, with the last column reporting the average difference between floodplain and non-floodplain households. 

48 

Table 2: Balance Table of Demographics and Housing by Floodplain Status (ACS Data) 

||FEMA Floodplain|Not Floodplain|Diference|
|---|---|---|---|
|Insurance payment|$1181|$994.2|-187<br>(_<_0.001)|
|Uninsured rate|0.12|0.08|-0.037<br>(_<_0.001)|
|Household income|$77,530|$82,430|4905<br>(_<_0.001)|
|Age|51.6|51.3|-0.32<br>(_<_0.001)|
|Monthly rent|$968|$934|-33.57<br>(_<_0.001)|
|Black|0.12|0.12|0.001<br>(0.002)|
|Hispanic|0.15|0.12|-0.039<br>(_<_0.001)|
|Asian|0.04|0.05|0.002<br>(_<_0.001)|
|Years in home|10.9|12.4|1.525<br>(_<_0.001)|
|Own (No Mortgage)|0.25|0.24|-0.010<br>(_<_0.001)|
|Own (With Mortgage)|0.36|0.45|0.096<br>(_<_0.001)|
|Renter|0.40|0.31|-0.086<br>(_<_0.001)|
|N|4,292,000|25,920,000||



Sources: Environmental Impacts Frame, American Community Survey and National Flood Hazard Layer data. Notes: This table displays the average of various household characteristics, separately by floodplain status, with the last column reporting the average difference and p-value in parentheses from a survey-weighted t-test. 

49 

Table 3: Household Characteristics by Floodplain and Adapted Status 

||In FEMA|Floodplain|Not In|Floodplain|
|---|---|---|---|---|
||Adapted|Not adapted|Adapted|Not adapted|
|Household Income|$101,700|$87,340|$118,200|$82,060|
||(154,600)|(116,700)|(190,900)|(96,740)|
|Uninsured Rate|0.14|0.17|0.11|0.12|
||(0.35)|(0.38)|(0.32)|(0.33)|
|Insurance Payment|$1,931|$1,690|$1,994|$1,434|
||(2,110)|(1,799)|(2,098)|(1,384)|
|N|216,000|190,000|8,700|731,000|



Sources: Environmental Impacts Frame, American Community Survey and National Flood Hazard Layer data. Notes: This table displays the average and standard deviations (in parentheses) of household characteristics, separately by elevation status and floodplain status. 

Table 4: A typology of flood-risk-exposed households across vulnerability dimensions 

|**Household Type**|**Income**|**Structure**|**Property Damage**|
|---|---|---|---|
|High Income, SFH Renter|×|✓|×|
|High Income, Multifamily Renter|×|×|×|
|High Income, Multifamily Owner, Insured|×|×|×|
|High Income, Multifamily Owner, Uninsured|×|×|✓|
|High Income, SFH Owner, Insured|×|✓|×|
|High Income, SFH Owner, Uninsured|×|✓|✓|
|Low Income, SFH Renter|✓|✓|×|
|Low Income, Multifamily Renter|✓|×|×|
|Low Income, Multifamily Owner, Insured|✓|×|×|
|Low Income, Multifamily Owner, Uninsured|✓|×|✓|
|Low Income, SFH Owner, Insured|✓|✓|×|
|**Low Income, SFH Owner, Uninsured**|✓|✓|✓|



✓ = vulnerable × = not vulnerable 

50 

# **A Appendix Figures** 

Figure A1: Trends in the Share of the Population in Floodplains by Income Percentile, Tenure, and Race/Ethnicity: 2013 vs. 2023 



<!-- Start of picture text -->
Asian, Homeowner Asian, Renter Black, Homeowner<br>0.14<br>0.16 0.22 0.13<br>0.14 0.20 0.12<br>0.11<br>0.12 0.18<br>0.10<br>0.10 0.16 0.09<br>0 25 50 75 100 0 25 50 75 100 0 25 50 75 100<br>Black, Renter Hispanic, Homeowner Hispanic, Renter<br>0.20 0.22<br>0.28<br>0.18 0.20<br>0.16 0.18 0.24<br>0.14 0.16 0.20<br>0 25 50 75 100 0 25 50 75 100 0 25 50 75 100<br>White, Homeowner White, Renter Year<br>0.18 0.250<br>2013<br>0.16 0.225 2023<br>0.14 0.200<br>0.12 0.175<br>0 25 50 75 100 0 25 50 75 100<br>Income Percentile<br>Fraction of Households In Floodplain<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the fraction of EIF households in floodplains across income percentiles, separately for 2013, 2023, tenure status, and race/ethnicity. 

A1 

Figure A2: Average Annual Expected Flood Damages and Insurance Payments by Income Percentile and Floodplain & Insurance Status 



<!-- Start of picture text -->
Insurance<br>10000<br>Insurance payment<br>Insured<br>Uninsured<br>3000<br>8000 Floodplain status<br>FEMA Floodplain<br>Not Floodplain<br>6000<br>2000<br>4000<br>1000<br>2000<br>25 50 75 100<br>Household Income Percentile<br>Average annual flood damages<br>Average annual insurance payment<br><!-- End of picture text -->

Source: Environmental Impacts Frame, IRS 1040s, Lightbox, and National Flood Hazard Layer data. Notes: This figure plots the average annual flood damages on the left y-axis, separately by insurance status, and the average annual insurance payment on the right y-axis (for the insured households by construction) across income percentiles, separately by floodplain status. 

A2 

