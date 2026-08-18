---
title: NBER-CRIW-2026-Ch4-Chen-Positive-Spillovers
type: paper
source_pdf: raw/papers/NBER-CRIW-2026-Ch4-Chen-Positive-Spillovers.pdf
converted: 2026-08-18
---

# The Positive Spillovers to Risky Investments in Vacant, Abandoned, and Disinvested Properties 

Edward W. Chen<sup>1</sup> , Reagan L. Lengefeld<sup>2</sup> , and Omar Isaac Asensio<sup>2,3*</sup> 

> 1Princeton University, Operations Research and Financial Engineering 

> 2Georgia Institute of Technology, Jimmy and Rosalynn Carter School of Public Policy 

> 3Georgia Institute of Technology, Institute for Data Engineering & Science (IDEaS) 

> *Email: asensio@pubpolicy.gatech.edu 

February 6, 2026 

## **1 Introduction** 

Disadvantaged and underserved communities are disproportionately vulnerable to the effects of climate risk on property values (Clayton et al. (2021); Bunten and Kahn (2014)). These communities often have a high concentration of vacant, abandoned, and disinvested (VAD) properties, which discourage new investment and negatively affect public health and neighborhood quality of life (Liang et al. (2024)). One common housing policy response is infill development, a publicly funded redevelopment strategy that focuses on constructing new homes or revitalizing existing ones on VAD land within already developed urbanized areas (McConnell and Wiley (2011)). For example, across the 209 largest U.S. metropolitan areas over the past two decades, infill development accounted for up to 21% of new housing construction (U.S. Environmental Protection Agency (2014)). These policies are believed to generate important social and environmental benefits by mitigating urban sprawl and promoting economic stabilization (U.S. Environmental Protection Agency (2014, 2007)). Beyond these direct effects, scholars argue that infill policies may also create positive externalities, such as increases in surrounding property and land values (Rossi-Hansberg and Sarte (2012); Schwartz et al. (2006); Bourassa, Hoesli and Sun (2005); Redding and RossiHansberg (2017)). However, the magnitude of these spillovers remains debated, particularly in the context of large government-led revitalization projects, where public spending may crowd in, or crowd out, private investment in nearby areas (Rossi-Hansberg and Sarte (2012); Rossi-Hansberg, Sarte and Owens III (2010)). If private housing investment complements infill spending, theory predicts neighborhood revitalization. In contrast, if private investors view infill spending as a substitute for their own activity, theory predicts limited or no additional neighborhood revitalization, as public intervention replaces investment that might otherwise have occurred. 

1 

Despite its potential economic and environmental benefits, infill development often encounters significant obstacles (McConnell and Wiley (2011); Farris (2001)). Firstly, developers face complications in land assembly, including landowners’ unwillingness to sell or a higher likelihood of legal disputes arising from unclear property titles (Farris (2001); McConnell and Wiley (2011)). Secondly, developers frequently encounter neighborhood opposition driven by concerns about increased density, added pressure on local services, and perceived declines in neighborhood character and value (Flint (2005); Fischel (2000)). Behavioral factors may also contribute to resident resistance, including endowment effects and status quo bias that favor maintaining existing neighborhood conditions (McConnell and Wiley (2011)). 

These obstacles are further compounded by the difficulty in measuring and quantifying the potential benefits of infill development for nearby properties and, in turn, assessing its policy effectiveness and cost efficiency. Impact evaluation is highly information-intensive, and the relevant civic data are often fragmented across municipal information systems and other public data sources (Glaeser and Poterba (2020, 2021)). As a result, the broader spillover benefits of infill development are difficult to measure. Reliable cost estimates and investment return benchmarks are also limited, and the evidence base remains thin due to persistent barriers to data access and integration (Farris (2001); McConnell and Wiley (2011). 

This measurement uncertainty has led many investors and lenders to view infill development, particularly in climate-disadvantaged areas, as relatively risky (U.S. Environmental Protection Agency (2015)). More broadly, it reflects wider patterns of climate risk aversion, whereby climate-disadvantaged areas experience lower rates of private investment and greater inefficiencies in capital allocation (Lupton et al. (2019); Rao and Krol (2022); Xu, Huang and Li (2024); Arian and Naeen (2025)). 

In this study, we evaluate the long-run impact of infill development in Savannah, Georgia, a major U.S. port city. Although the city supports substantial economic activity, many of its neighborhoods have struggled with long-term climate-related challenges, particularly storm exposure and flood risk, alongside longstanding socioeconomic disparities (Binita, Shepherd and Gaither (2015)). According to program administrators, blighted properties in Savannah incur an estimated $5.6 million per year (approximately $1,300 per property) in maintenance and operational costs associated with overgrown vegetation, litter, illegal dumping, securing vacant structures, property demolition, and forgone property tax revenue (Partnership for Inclusive Innovation, Georgia (2020)). In response, the city implemented infill development strategies aimed at income-qualified residents, defined as households earning less than 80% of the area median income, and targeted distressed city blocks for revitalization. The program prioritized infill developments that aligned with existing neighborhood architectural styles, rather than pursuing large-scale projects that could appear out of place. Prior research suggests that similar government-led infill initiatives can expand home ownership opportunities and attract complementary retail and commercial activity (McConnell and Wiley (2011)). 

The structure of the City of Savannah’s infill development strategy presents unique opportunities to examine the co-benefits of public infill development. The city’s efforts primarily target blighted or abandoned properties, which helps to mitigate some of the common local opposition, such as concerns about aesthetics or preserving neighborhood character. In this context, redevelopment addresses parcels that already impose public maintenance costs and reduce neighborhood quality. Savannah’s infill program was designed to transform these 

2 

negative externalities into affordable housing opportunities through targeted public intervention (City of Savannah (2025, 2024)). The city’s DreamMaker program complements these efforts by helping to ensure that infill properties remain accessible to existing community members (City of Savannah (n.d.)). To do this, the program provides down payment and home purchase assistance (with deferred loan options) based on strict income qualification criteria, mitigating some concerns about gentrification pressure in historic neighborhoods. The city relies on an extensive network of public-private partnerships and diverse funding sources to advance its infill agenda. Multiple local entities coordinate closely with city officials to acquire, rehabilitate, and resell previously blighted properties to income-qualified individuals. Key non-governmental partners include the Land Bank Authority and the Community Housing Services Agency (City of Savannah (2024)). The city also leverages a mix of public financing streams including the Savannah Affordable Housing Fund, Georgia’s SpecialPurpose Local-Option Sales Tax (SPLOST), and federal programs such as the Community Development Block Grant and HOME Investment Partnerships Programs (Department of Housing and Urban Development (2024); City of Savannah (2024)). 

Through our partnership with the City of Savannah housing program administrators, we gained access to detailed administrative data and program information for impact evaluation. We used web scraping and record linkage procedures to analyze the infill development spillovers with large-scale civic data, comprising 2.43 million yearly records across 104,836 parcels from 2001-2022. Our analysis shows that parcels immediately surrounding infill sites experience the largest increases in appraised values for multiple years following the initial intervention. We estimate that infill policies generate substantial market appreciation, with treated areas experiencing up to 11.3% increase in appraised value. Notably, these indirect benefits to neighboring parcels accrue primarily within climate-disadvantaged communities at the block level, rather than at the broader neighborhood scale, as often theorized. To further examine underlying mechanisms, we test theories of agglomeration economies and find that spillover gains tend to be concentrated in city blocks with multiple closely located infill developments, and decline sharply in blocks where infill projects are more isolated. By leveraging granular parcel level data, we quantify socioeconomic benefits that would otherwise remain hidden from investors or administrators. 

## **2 Related Literature** 

Prior theory and evidence on infill development spillovers has been relatively mixed. Some studies document positive housing externalities and improved neighborhood perception through the “amenity effect” (Ooi and Le (2013); Ellen et al. (2001); Brunes et al. (2020); Ding, Simons and Baku (2000); Zheng, Li and Lv (2020); Kurvinen and Vihola (2020); Nordahl and Sommervoll (2020); Ellen and Voicu (2006); Zahirovich-Herbert and Gibler (2014)). For example, Ooi and Le find that in Singapore, sales prices of properties located within 500 meters of an infill site increased by 1.22% (Ooi and Le (2013)). Related work on housing policy interventions also identifies positive spillovers, such as nearby property appreciation following the elimination of rent control in the city of Boston (Autor, Palmer and Pathak (2014)). In contrast, other studies suggest that infill development can generate adverse effects, including increased traffic and congestion or the loss of neighborhood green space, which may prompt 

3 

resident resistance (Funderberg and MacDonald (2010); Newell (2010); Malpezzi (1996); Preez (2013)). For instance, Funderberg and MacDonald conducted a study in Polk County, Iowa and found that low-rise construction projects were associated with a 2 to 4 percent decrease in valuations for nearby single-family homes (Funderberg and MacDonald (2010)). Ooi and Lee further argue that nearby property values may decline near infill sites, not only because of perceived negative externalities, but also due to a “supply effect,” whereby an expansion of local housing stock offsets potential amenity gains (Ooi and Le (2013)). The supply effect can counteract increases in by introducing additional housing inventory into the market (Newell (2010); Grenadier (1996)). Other studies find negligible impacts of infill development on surrounding properties, suggesting that positive amenity effects and negative supply effects, may offset one another (Ahvenniemi et al. (2018); Blanchard, Clegg and Martin (2008)). The mixed findings in the literature likely reflect differences in outcome measurement, empirical design choices related to counterfactuals, often based on distance or proximity thresholds, and heterogeneity across infill programs themselves. We contribute to this literature by measuring spatial spillovers of infill development policies on a more granular block level, the spatial scale at which city administrators allocate investments, rather than the broader neighborhood scale emphasized in prior studies. This work also connects to the growing literature in urban analytics, which applies spatial network science to the measurement of social and economic change in cities (Boeing et al. (2021)). 

## **3 Hypotheses** 

We examine the extent to which government-funded revitalization generates measurable positive spillovers in the appraised property values of surrounding parcels. Firstly, we hypothesize that infill development will increase nearby appraised property values through amenity effects, particularly in climate-distressed and low-income communities. By mitigating VAD properties, infill development may enhance the desirability of surrounding parcels, reversing prior decline and encouraging complementary investments. Amenity effects have been documented in a broad range of contexts including aesthetic urban landscapes (e.g. parks, lakes, mountains, and rivers), the expansion of public transit infrastructure (e.g. bus stations and subways), and the redevelopment of environmentally distressed or brownfields sites (e.g. former waste disposal facilities and cemeteries) (Yuan, Wei and Wu (2020); Lee and Linneman (1998); Wen, Zhang and Zhang (2015); Hou et al. (2023); Haninger, Ma and Timmins (2017)). We expect these amenity effects to be strongest for properties located closest to the infill site, which is consistent with theories of land rents for revitalization policies (Rossi-Hansberg and Sarte (2012)). Our second hypothesis is that, infill development will also increase nearby appraised property values through agglomeration effects from infill clustering. Agglomeration dynamics operate not only at the neighborhood level but also finer, sub-neighborhood scales (Rosenthal and Strange (2020)). This aligns with urban planning and economic theories of public interventions reaching “tipping points”, whereby investments much reach a critical mass in order to achieve the desired community change (Redding and Rossi-Hansberg (2017); Grodzins (1957)). Finally, we consider an alternative hypothesis that, infill development will have a negligible effect on nearby appraised property values due to offsetting forces. While amenity and agglomeration effects may increase values, 

4 

expanded housing supply could eventually exert downard pressure by introducing additional markrt competition. Under this scenario, the positive and negative effects offset one another resulting in no statistically meaningful change in surrounding properties. (Nygaard, Galster and Glackin (2022)). 

## **4 Data** 

### **4.1 Data Sources** 

To evaluate program spillovers, including economic returns and selection criteria, we obtained historical data for all 396 publicly-funded infill projects in Savannah, Georgia, from 2004-2019. These projects are independently managed by the City Savannah Housing and Neighborhood Services, which administers housing repair, construction, and development projects, targeted to qualified households with modest and limited income. The program data includes the service address, parcel ID, the year receiving infill assistance/funding, and direct total program expenditures as tracked and provided to us by city administrators. 

To obtain detailed housing characteristics such as the square footage, year built, number of rooms, and yearly appraised building property values, we compiled data from the Chatham County Tax Assessor Database for the period 2001-2022. We accessed geospatial data from the Savannah Area Geographic Information System (SAGIS) to identify the location of target and surrounding properties. SAGIS maintains parcel and neighborhood-level geocoding and shape files (e.g. converting location descriptions into longitude and latitude) for all residential parcels in Chatham County. We also obtained socioeconomic characteristics at the Census block group level, including income, population density, educational attainment, age, etc., from the 2019-2023 5-year American Community Survey. 

Given our interest in the effects of infill development in climate-disadvantaged communities, we merged the federally recognized tracts provided by the Climate and Economic Justice Screening Tool (CEJST). A tract is defined to be climate disadvantaged if it meets both a climate burden threshold (climate change, energy, health, housing, legacy pollution, transportation, water and wastewater, workforce development) and an economic burden threshold (income less than or equal to twice the federal poverty level, not including students enrolled in higher education) (Council on Environmental Quality (2022)). 

### **4.2 Record Linkage and Automated Data Collection** 

The City of Savannah uses open data platforms to make property and neighborhood-level information publicly available. Through a collaborative partnership with the city, we obtained parcel- and address-level records on 104,836 residential properties in Chatham County. This includes 78,864 residential properties within the city limits. For program evaluation, we conducted record linkage using the 10-digit numeric parcel ID as the primary linking variable. We matched records across data sources by parcel ID because it is a unique and complete identifier, avoiding common errors associated with address-based string matching. Because the vast majority of parcels contain a single residential unit, we use the terms parcel and property interchangeably. During the study period, each infill project can only receive 

5 

funding once. We successfully merged all 396 documented infill projects with 104,936 residential parcels. Of the 104,440 parcels available for counterfactual analysis, approximately 5% (5,223 parcels) were not usable due to missing geocoded fields. We verified that this missingness did not statistically alter the distribution of our key performance outcomes (KS test p-value = 0.999). The final dataset yielded an unbalanced panel of 2.43 million recordlinked housing observations. We provide additional details on variables and data sources in Appendix Table A1. 

As part of our collaboration with the City of Savannah Housing and Neighborhood Services, we developed a custom web-scraping tool to automatically query and download relevant civic data from the Chatham County Tax Assessor database. We deployed two open-source Python libraries, namely Beautiful Soup and Selenium, to automatically parse, click, and store structured and unstructured data from web pages within the assessor database. To promote transparency and broader adoption, we released a user-friendly open source version of the tool. In ongoing collaboration with city officials, we conducted a workshop to pilot its integration in municipal data science workflows. This training enabled city managers to query custom parcels and reports tailored to their needs. We note that this type of capacity-building effort can be helpful, particularly since small- to mid-sized cities may not have dedicated in-house data science teams (materials here). 

## **5 Empirical Strategy** 

To estimate the spillover effects of infill development in Savannah, we implemented a propensity score weighted difference-in-differences (DiD) design that compares properties located within a specified distance from an infill site to those located beyond that distance. We expected covariate imbalances between properties closest to infill projects and other properties, particularly when observable characteristics may be correlated with outcomes. Under the conditional parallel trends assumption discussed in Abadie (2005), we incorporated propensity weighting and complementary matching procedures within staggered DiD estimators to identify the spillover effects of infill development (Abadie (2005)). In the absence of covariate balancing and matching, we observed pre-trend violations that produced negatively biased treatment effect estimates (see Figure A2). We also implemented alternative counterfactual analyses with synthetic control methods to quantitatively validate our program evaluation. 

### **5.1 Spatial Identification and Statistical Matching** 

To precisely identify properties that are close to infill developments, we created a variable, _Disti_ , as the distance (in meters) between property _i_ and the nearest infill project. We defined an infill zone as a perimeter area _k_ meters from the centroid of an infill site. We considered properties within an infill zone to be treated, and those outside an infill zone to be non-treated. To identify spillover effects as opposed to direct intervention effects, infill zones included neighboring parcels but excluded infill sites where _Disti_ = 0. We express parcels that are within _k_ meters from an infill site as a binary indicator: 



6 

In this study, we tested for potential spillovers at distances of _k_ = 25 _,_ 50 _,_ 75 _,_ 100. Increments of 25 meters were chosen since this is approximately equal to the average parcel length in Chatham County. This spatial cutoff allowed us to identify granular treatment effects at the city block level and down to the nearest neighbor. 

Prior studies have often constructed counterfactual zones by selecting adjacent reference properties or setting a broad geographic boundary such as neighborhoods or outer rings (Rossi-Hansberg and Sarte (2012); Ooi and Le (2013); Brunes et al. (2020)). This is typically under the assumption that properties closer together might be similar on observable characteristics. However, this choice of using adjacent properties or rings as counterfactual is subject to several critiques, discussed in Diamond and McQuade (2019). First, the choice of geographic boundaries for the counterfactual relies on an arbitrary cutoff in distance between treatment and control areas. Second, the use of inner and outer rings for spillover treatment areas also assumes that there is a negligible variation in housing prices or stock characteristics between the two groups. Not controlling for this time-invariant variation can add substantial variance to treatment effect estimates. To define more precise statistical comparison groups, we employed matching procedures that leverage any available parcels within the broader superpopulation of Chatham County to ensure pretreatment covariate balance between the infill zone (where we test for potential spillovers) and weighted counterfactual areas (see Figure 1). 

We evaluated both propensity score matching (PSM) and genetic matching procedures to achieve covariate balance between infill zone properties and our reference properties (Diamond and Sekhon (2013); Rosenbaum and Rubin (1983); Stuart et al. (2011)). Given substantial median bias across variables known to impact property values, we matched on property characteristics (i.e., year built, number of stories, quality, distance to nearest green space, type of building) and socioeconomic characteristics at the census block group level (i.e., population density, income level, % black population, % single female household). We included those variables for matching through a process of feature selection for overt bias (see Table A2). Given recent insights from the statistical literature, we did not match on pretreatment outcomes due to the known regression-to-the-mean effect, which can inject bias (Ham and Miratrix (2024)). We derived optimal matching parameters such as the caliper and ratio at each infill zone to ensure covariate balance. For comparative evaluation of the effectiveness of matching procedures and hyperparameters, we report standardized mean bias reduction across all matched covariates in Appendix Table A4. We chose genetic matching as our preferred procedure, as we found that genetic matching consistently achieves better performance with a 99-98% bias reduction across all infill zone distances from 25-100 meters (see Table A4). 

### **5.2 Treatment Effects Under Staggered Adoption** 

To estimate the spillover benefit of infill projects on surrounding properties, we employed a staggered DiD approach to compare changes in appraised property values before and after an infill site development. We used yearly appraised property values ($/sqft) instead of sales prices because sales data can be sparse and often have substantial missing values, especially for narrowly defined counterfactual areas (Diamond and McQuade (2019)). Infill projects in our dataset were administered over a 15 year period from 2004-2019 with yearly budget 

7 

cycles introducing 26.4 projects every year. For property _i_ in year _t_ , we estimate a baseline model using two way fixed effects (TWFE), 



where _yi,t_ is the appraised parcel value ($) normalized by dividing by living area (in sqft); _αi_ represents unit fixed effects; _λt_ represents yearly fixed effects; _Posti,t_ is a binary indicator for years post infill; _β_ is the estimated coefficient that represents the spillover effect within _k_ meters from an infill; and _ϵi,t_ is an error term. Given the staggered implementation of infill projects, one potential concern is that treatment effects estimated in a given year could be contaminated by cohort effects in previous years under treatment heterogeneity (GoodmanBacon (2021); Callaway and Sant’Anna (2021); Athey and Imbens (2022); de Chaisemartin and D’Haultfœuille (2020)). To address this issue, we implement the interaction-weighted DiD estimator proposed by Sun & Abraham, which uses cohort shares as weights to correct for these potential biases (Sun and Abraham (2021)). In Table A9 in Appendix, we show that a conventional TWFE estimator exhibits a downward bias in estimated treatment effects compared with the preferred staggered DiD estimator. 

To understand how the treatment effects may vary with years of exposure, we also estimated an extension of our baseline model that includes indicators for years prior to and after the treatment. The dynamic model for a given ring distance _k_ meters from the infill site is estimated as follows: 



where _l_ is relative year of the infill construction and _Di,t_<sup>_l_isadummyvariableforwhether</sup> property _i_ is _l_ years away from an infill’s year of construction at year _t_ . We use the year preceding the intervention as the reference year (l = -1). Our stacked regression includes all available years prior to the intervention (2-18 lags) and post intervention (0-19). Given the nature of reporting appraised property values for city and county tax purposes, our panel is highly balanced. To estimate Equation 3, we implement the dynamic model extension of the Sun Abraham estimator (Sun and Abraham (2021)). The model estimates _βl_ coefficients for leads and lags by comparing cohort average effects relative to never-treated units. The dynamic specification also provides visual evidence of parallel trends prior to treatment (see Figure 2). We note that in staggered DiD models, without matching, there are pre-trend violations, as described in Section 5.1. 

### **5.3 Aggregating to Blocks & Counterfactual** 

Infill developments are dispersed unevenly across Savannah, where some city blocks receive heavier investment than others. To analyze how the effect of the infill policy varies by infill density, we aggregated parcel data to the city block level. To measure the infill density of a city block j, we use: 



8 

We considered blocks that contain at least one infill development and split them into quintiles based on Equation 4. We then performed an aggregate analysis by taking averages of the parcel-level appraised values and pre-treatment covariates at the city block level. We do not include infill properties in the aggregate outcome. For the block-level analysis, we assign treated blocks into quintiles sorted by infill density. For example, the parcel share density can vary from as low as 4.5% infill properties in the bottom quintile to 76.9% in the top quintile. With an average of 22.68 properties per block in Savannah, this is 1 infill per block in the bottom quintile up to 17 infills per block in the top quintile. For each quintile, we employ a similar empirical strategy: we first deploy genetic matching to reduce bias and then estimate treatment effects with staggered DiD (Sun and Abraham (2021)). 

To validate our inference, we also explored alternative counterfactuals when aggregating from the parcel level to the block level. We constructed a counterfactual using the synthetic control method (SCM) by taking a weighted average from possible donor blocks that do not contain an infill. When parcel data is aggregated, researchers will often use the synthetic control method as an alternative to DiD (Abadie, Diamond and Hainmueller (2010)). For implementation, we used the partially pooled SCM available in the R package `augsynth` (Ben-Michael, Feller and Rothstein (2021)). Partially pooled SCM is a generalization of synthetic control strategies that allows for analysis in the staggered adoption setting by finding a weighted average of control units that minimizes pre-treatment imbalance for individual treated units and average pre-treatment imbalance across all treated units. We found a separate set of weights to construct counterfactuals for each quintile of blocks and then estimated quintile treatment effects by infill density. 

## **6 Results and Discussion** 

### **6.1 Infill Co-Location in Climate-Distressed Areas** 

We first explored the spatial distribution of all infill projects across the city with 20 years of program participation. In Figure 1, we provide a map of infill sites and adjacent parcels. We found that targeted blocks are most common in neighborhoods surrounding the central business district and in northwest Savannah within the city limits. This profile is expected given reports of dilapidated parcels in Savannah’s older, climate-disadvantaged neighborhoods. Properties surrounding infill sites are primarily single-story, single-family residences, with 2-3 bedrooms, about 1.5 bathrooms, and an average vintage of 1950. Areas surrounding the infill sites have an average per capita income of $20,295, which is above 63.4% of the city’s per capita income. These urbanized areas also have among the highest population densities in the city, with 5,495 persons per square mile, compared to about 1,503 persons per sq. mile for urban Savannah. This participation profile is consistent with economically distressed areas and Savannah’s intended housing interventions. Given the high population density, neighborhood improvements could provide positive externalities to a wide reach of the population. The distance of an infill development to the nearest green space for example is within a short walking distance, approximately 371 meters. Notably, 47.6% of nearby households are single female, and 84.5% of residents are non-Hispanic Black. For a more detailed summary of population statistics, see Appendix Tables A1 and A2. 

9 



<!-- Start of picture text -->
Climate Disadvantaged Tract<br>Infill Development Parcel<br>Spillover Area (100m) Parcel<br>Possible Counterfactual Parcel<br><!-- End of picture text -->

#### Figure 1: **Spatial distribution of infill development in climate disadvantaged communities** 

The map shows the spatial distribution of publicly-funded infill development in Savannah, Georgia. The shaded teal areas represent federally recognized census tracts that were designated as climate disadvantaged under climate and economic indicators, including energy, pollution, and transportation. We find that 95.2% of infill parcels and 90.8% of spillover area parcels are in tracts that were considered climate disadvantaged. The red markers represent an individual parcel that was selected by program administrators for infill development. The blue markers represent the potential spillover parcels within 100 meters, which is approximately one block length or four parcels. The gray markers represent parcels available for counterfactual analysis, outside of the spillover area. 

10 

Although vulnerability to climate impacts was not an explicit criteria for program selection by administrators, a significant share, over 95% of infill projects and 90% of surrounding properties (within 100 meters), are in climate-distressed areas (Figure 1). Using government-defined indicators for climate-distressed communities, the most common issues include physical climate-risks (e.g. flood risk), energy, health, legacy pollution, and workforce development<sup>1</sup> . For example, Census tract 13051000601, which contains the West Savannah neighborhood, is above the 90th percentile for multiple climate indicators, including projected wildfire risk, energy costs divided by household income, share of people with asthma, and legacy pollution as measured by the share of Risk Management Plan facilities within 5 kilometers. Additionally, it falls above the 90th percentile on the share of people with diabetes. An emerging literature has linked diabetes with climate-related risks due to impaired responses to heat stress (Ratter-Rieck, Roden and Herder (2023)). Other neighborhoods with large shares of infill projects, such as Cuyler/Brownville and Benjamin Van Clark Park contain Census tracts that are above the 90th percentile in low life expectancy, projected flood risk, and traffic proximity and volume. They are also above the 80th percentile in exposure to diesel particulate matter. This suggests that infill strategies managed by the Savannah Housing and Neighborhood Services are highly compatible as co-policies for community revitalization in response to the growing impacts of climate change such as economic loss to building value from natural hazards or projected flood risks from tides, rain, and river and storm surges within 30 years. The targeted intervention in areas with socioeconomic disadvantage will bring about outcomes to the same areas of climate-disadvantaged areas. 

Prior literature has highlighted a tension between infill development and climate-change adaptation strategies, particularly when supported by public intervention. Our findings suggest that there is not an inherent conflict between expanding affordable housing opportunities and attracting redevelopment funds in climate-distressed areas. We next evaluated how the benefits of infill development may be quantified and vary by distance from the site. 

### **6.2 Spatial Decay of Spillover Effects** 

In Table 1, we report estimates for the effects of infill development on appraised building values for properties that were within 25, 50, 75, and 100 meters from the infill site. Consistent with the amenity effect hypothesis, we find that properties adjacent to an infill development experienced a long-term 11% increase in appraised values between 2004-2022. Within approximately one parcel length from an infill development, at 25 meters, this translates to a premium of 3.61 $/sqft. At a distance of 50 and 75 meters, which is about two and three parcel lengths away, we find a 4-6% increase, or a premium of 1.961 $/sqft and 1.632 $/sqft, respectively, surrounding an infill site. These results suggest a decay in the amenity effect at a rate of 0.01-0.07 $/sqft per meter. At a distance of 100 meters, or approximately one block length away, the spillover effect tapers off and is no longer statistically different from zero. Over the full period of study, these treatment effects amount to statistically significant increases of $4 _,_ 696 _._ 40 per redevelopment project, and approximately $1 _._ 8 million in additional market value for city properties. Our granular results provide empirical evidence that block-level boundaries may be the more appropriate evaluation scale for spillovers from 

> 1Definitions of climate and economic burden and shapefiles by Census tract are archived here 

11 

Table 1: **Spillover treatment effects of infill development on nearby residential parcel values (2004-2022)** 

|||Distance to|nearest infll||
|---|---|---|---|---|
||25 meters<br>Approx. 1<br>parcel|50 meters<br>Approx. 2<br>parcels|75 meters<br>Approx. 3<br>parcels|100 meters<br>Approx. 4<br>parcels|
|Mean spillover efect|3.610**|1.961***|1.632***|0.635|
|($/sqft)|(1.440)|(0.680)|(0.512)|(0.511)|
|Percent increase|11.266%|5.696%|4.625%|-|
|Parcel fxed efects|Yes|Yes|Yes|Yes|
|Year fxed efects|Yes|Yes|Yes|Yes|
|No. of observations|57,464|112,995|197,00|149,211|
|No. of surrounding parcels|389|1,440|2,587|3,980|



Note: Significant to p _<_ *0.1, **0.05, ***0.01. The dependent variable is the appraised residential building value, divided by the living area square footage of residential properties as reported by the Chatham County Tax Assessors Database (2001-2022). Spillover areas include all parcels that are within a circular boundary. Spillover effects are estimated using the Sun and Abraham staggered DiD estimator versus a matched counterfactual of statistically similar parcels (Sun and Abraham (2021)). Standard errors are clustered by parcel ID. 

public investment projects, as opposed to neighborhood boundaries as previously theorized (Rossi-Hansberg and Sarte (2012); Rossi-Hansberg, Sarte and Owens III (2010); Ooi and Le (2013); Ellen and Voicu (2006)). For example, previous findings by Theodos, Galster, and Herman reported property value increases as far as 2,000 feet (about 600 meters) away from Community Development Block Grant spending sites (Theodos, Galster and Hermans (2024)). Prior theory and evidence has suggested that when positive spillovers occur, they often decay at the neighborhood boundaries (Rossi-Hansberg, Sarte and Owens III (2010); Rossi-Hansberg and Sarte (2012)). Our findings indicate a perhaps more limited impact area for indirect spillovers, but with long-term positive market value to surrounding properties. 

To understand how these effects might vary over time, we employed an event study analysis to estimate yearly program treatment effects. We present dynamic effects for properties within 25 meters from an infill development in Figure 2. Notably, we found that there is an immediate positive spillover effect on adjacent properties that last up to six years. We learn that government-investment projects can yield spillovers benefits for a period of six years or longer despite the perceived investment risks. Quantifying these hidden benefits is important because it has been argued that even when investors or developers are willing to take the risk of investing in climate-risky areas, they often have trouble securing financing as lenders view returns in these communities as too uncertain or risky (U.S. Environmental Protection Agency (2015)). 

12 



<!-- Start of picture text -->
20<br>15<br>10<br>5<br>0<br>−5<br>−10<br>−16−14−12−10 −8 −6 −4 −2 0 2 4 6 8 10 12 14 16<br>Years since intervention<br>Appraised value per sqft<br><!-- End of picture text -->

Figure 2: **Dynamic treatment effects of infill development on neighboring 25meters ring residential parcels.** The figure shows dynamic treatment effects of the intervention of neighboring infill development on the county assessed appraised values ($/sqft) relative to the intervention year. The analysis is based on a stacked regression where 0 is defined as the intervention year relative to a matched reference set that includes statistical adjustment for observable property and socioeconomic characteristics. To control for potential biases due to staggered program participation, we use Sun and Abraham’s staggered DiD estimator (Sun and Abraham (2021)). The standard errors are clustered by parcel ID, and the vertical lines represent the 95% confidence intervals. We find evidence of lasting positive treatment effects that persist for approximately six years after the initial investment, with a peak return between years two and three. The maximum return is in year three with a 2.017.18 $/sqft, which corresponds to a 4.81-17.17% premium. Given the quantity of the high resolution data and technical approach, we are able to measure significant yearly treatment effects and do not rely on cross-sectional results for inference. 

Our findings of lasting positive spillovers for at least six years following intervention indicate that infill development can be effective at bringing long-term benefits to disadvantaged communities. Greater visibility for these co-benefits might also help attract greater public and private investment. 

### **6.3 Geographic Clustering of Spillover Benefits** 

Prior theories of agglomeration economies have suggested that economic benefits in cities and industries tend to increase with density (Glaeser and Gottlieb (2009)). We tested the hypothesis that urban blocks receiving a higher density of infill investment experience higher returns. We found that 170 out of 4,392 city blocks contained at least one infill development, with an average infill density of 12.2% and a median infill density of 7.1% (see Equa- 

13 

Table 2: **Spillover treatment effects of infill development within blocks by infill density quintiles** 

||||Infll density|%||
|---|---|---|---|---|---|
||1|2|3|4|5|
||(0.4, 4.5)|(4.5, 6.3)|(6.3, 8.3)|(8.3, 16.7)|(16.7, 76.9)|
|Mean spillover efect,|2.852|2.779|4.691|0.223|11.046***|
|($/sqft)|(2.331)|(2.753)|(4.079)|(1.661)|(1.438)|
|Percent increase|-|-|-|-|35.8%|
|Parcel FE|Yes|Yes|Yes|Yes|Yes|
|Year FE|Yes|Yes|Yes|Yes|Yes|
|Clustered SE|Yes|Yes|Yes|Yes|Yes|
|No. of treated blocks|33|33|32|33|33|
|No. of matched blocks|119|182|172|119|61|
|No. of block-year observations|3,473|4,941|4,674|3,492|2,155|



Note: Significant to p _<_ *0.1, **0.05, ***0.01. The dependent variable is the block-level average appraised building value divided by the block-level average living area square footage of residential properties. Treated blocks include any block that contained at least one infill development, and quintiles are created by ranking treated blocks by infill density. Treatment effects are estimated using the Sun and Abraham staggered DiD estimator (Sun and Abraham (2021)). Standard errors are clustered by block ID. 

tion 4). Neighborhoods containing high infill density city blocks, in the highest quintile, include Savannah Gardens, Twickenham, Benjamin Van Clark Park, West Savannah, and Cuyler/Brownville. These neighborhoods have clusters of targeted blocks where 16.7-76.9% (around 2-9 parcels) of approximately 12 parcels in a single block are infill developments. In Table 2, we report treatment effects by quintile that are ordered by infill density. As expected, we find evidence of threshold effects, where treatment effects are highest in treated blocks with the highest infill density. At the top quintile, blocks with infill density between 16.7-76.9%, we report a long-run increase in spillover benefits of 11.046 $/sqft. For the other quintiles with lower infill density, the treatment effects are not statistically different from zero. We validated this result with alternative counterfactuals using the partially pooled synthetic control method. Consistent with the DiD analysis, we find that only the highest concentration of infill density quintile produced a statistically significant treatment effect, albeit at a lower magnitude than with DiD analysis (see Table A5). For the highest range of infill density, we report a statistically significant spillover benefit of 6.980-11.046 $/sqft. 

These results are consistent with prior work on thresholds for agglomeration economies (Theodos, Galster and Hermans (2025); Han (2019); Rosenthal and Strange (2020); Glaeser and Gottlieb (2009); Combes, Duranton and Gobillon (2011)) and “tipping point” theories for urban change (Grodzins (1957); Schelling (1978); Milkoreit et al. (2018)). For Savannah’s infill development policies, higher density is a direct result of higher targeted public investment and private co-investment in surrounding parcels within the same city block. We learn that heavy program targeting of individual blocks is necessary to experience economically significant effects in areas surrounding rehabilitation. 

14 

### **6.4 Placebo/Falsification Tests** 

To validate our results, we conducted falsification tests by restricting the analysis to those observations prior to the treatment and by selecting an arbitrary treatment date prior to the infill. In this way, we test for treatment effects versus our matched counterfactuals where none are logically possible. To do this with our DiD strategy, we arbitrarily set a new “treatment” year to be the mid-point between a property’s earliest year in the dataset and the year prior to treatment. For example, if a property was withing 25 meters from an infill property constructed in 2009, we only considered observations from 2001-2008 and reassigned its year of treatment as 2005 for the placebo test. We also restricted the years of the matched counterfactual to line up with the dates of the placebo test. We then estimated treatment effects accordingly. We provide a summary of these results at multiple distances between 25-100 meters in Appendix Table A6. As expected, our placebo tests recovered effects not statistically different from zero for all parcel distances. 

We also implemented placebo tests for our alternative analysis using partially pooled SCM. For implementation, we restricted observations to only possible donor units where we expect no treatment effects. We constructed a balanced panel of all donor blocks and randomly allocated a share of them with treatment years to mirror the distribution of treated years in the original sample. In this way, donor units that are “treated” are compared with a synthetic control constructed from the remaining donor units over the same time period. In Appendix Table A7, we confirm that our placebo test produced effects not statistically different from zero. Our findings are also see in Appendix Table A6. These falsification tests allowed us to validate our inferences. 

### **6.5 Cost-Benefit Ratios and Payback** 

We were able to generate cost-effectiveness estimates using direct project costs, supplied to us by Savannah program administrators, and the estimated tax revenues associated with direct and spillover benefits from our analysis. The aggregate cost across 361 infill projects was $52.37 million, which is an average cost per infill of $145,060 or $117 per sqft. The direct costs reported to us include funding sources from the U.S. Department of Housing and Urban Development, non-federal local funds (such as Georgia SPLOST funds), and private land bank and other financing. We found that for every public dollar invested, the program raised $2.07 in private matching funds. To estimate tax revenues associated with the direct effects infill projects, we considered the appraised values across post-infill years (2004-2022), the Georgia state assessment rate (40%), and the average millage rate across these years (12.67). To estimate increases in potential tax revenues due to spillover benefits, we considered properties within the 75 meter ring, or approximately three parcels, applying our treatment effect coefficient. Across all years of program participation, we found that infill development generated an additional $2.36 million in property tax revenues, leading to a tax revenue-to-cost ratio of 1.67. This translates to a payback period of around 8.32 years from direct infill intervention. We note that these numbers underestimate the true benefits, as they do not take into account the averted public costs in maintaining these properties and additional revenue generated from improved city housing. Taking into account these averted VAD maintenance costs and the increased value of neighboring properties results in an 

15 

approximate tax revenue-to-cost ratio of 2.42 and an implied payback period of around 5.76 years. These cost effectiveness estimates are quite favorable compared with prior reported estimates of payback schedules based on property tax revenue alone in the literature, which can span up to 20 years U.S. Environmental Protection Agency (2015). These payback estimates are also more favorable than other reported estimates of private return rates to infill development (Dickinson (2005); Rowley and Phibbs (2012)). 

The absence of evidence-based cost effectiveness estimates of previous infill developments, partially due to lack of data access and availability, has created uncertainty around the true benefits of infill strategies. Because Savannah’s policies were mostly supported by a mix of federal and private funds, the financial benefits derived from property taxes and averted public costs generate additional public revenue while also inducing additional local public spending from private investors in surrounding parcels. 

We note that these estimates do not include other socioeconomic benefits of having higherquality and expanded access to affordable housing in Savannah or other intangible benefits of redeveloping climate-disadvantaged areas. The strong return on public and private dollars invested, combined with a relatively short payback period of six years with indirect benefits, shows that infill development could be a financially attractive option for revitalization in disadvantaged, urban communities. It also presents a cost-effective alternative to high-density public housing developments by integrating single-unit, ”natural” housing into existing communities, without the typical risk of gentrification or displacing historic communities. 

## **7 Closing** 

In this study, we evaluated the impacts of city-led infill development for vacant, abandoned, or disinvested properties in climate-disadvantaged communities. We have emphasized the importance of positive economic and social spillover benefits that have been hidden from investors and the policy process. Prior theory and evidence has suggested that infill program spillovers often decay at the neighborhood boundaries (Rossi-Hansberg, Sarte and Owens III (2010); Rossi-Hansberg and Sarte (2012); Theodos, Galster and Hermans (2025)). Through more granular measurement, we find that positive spillovers benefits to surrounding properties can experience a sharp decline within the block boundary or a few parcels away. This evidence is consistent with neighborhood “tipping points” theories that suggest a critical density of intervention is necessary to produce lasting change. We also find evidence of lasting economic benefits that cover the cost of intervention, contrary to worries about the long payback periods for public or private infill development. 

Despite climate risk not being an explicit criterion for city redevelopment policy, our measurement shows that indirect benefits to climate-disadvantaged areas can co-exist in the targeted socioeconomic areas. Savannah’s intervention demonstrates that climate-disadvantaged areas, which investors may see as more risky, can yet generate lasting economic returns from neighborhood revitalization, despite climate risks. 

16 

## **8 Acknowledgments** 

We gratefully acknowledge funding by the National Science Foundation, award number 1945332 and the Partnership for Inclusive Innovation (PIN). For valuable discussions and collaboration, we thank Brian Brainerd and community partners in the City of Savannah Housing & Neighborhood Services Department, the City of Savannah Information Technology Department, Coastal Georgia Indicators Coalition (CGIC), Chatham County/City of Savannah Land Bank Authority, Inc. (LBA), Community Housing Services Agency, Inc (CHSA), Tolemi, and the Center for Community Progress. For valuable institutional support, we thank Deborah Lam and Steve Hodges. For valuable research assistance and pre-analysis, we thank Vincent Gu, Benjamin Harrison, and Nupur Kothari. 

17 

## **References** 

- Abadie, Alberto. 2005. “Semiparametric Difference-in-Differences Estimators.” _The Review of Economic Studies_ , 72(1): 1–19. 

- Abadie, Alberto, Alexis Diamond, and Jens Hainmueller. 2010. “Synthetic control methods for comparative case studies: Estimating the effect of California’s tobacco control program.” _Journal of American Statistical Association_ , 105(490): 493–505. 

- Ahvenniemi, Hennele, Ky¨osti Pennanen, Antti Knutti, and Anne Arvola. 2018. “Impact of infill development on prices of existing apartments in Finnish urban neighbourhoods.” _International Journal of Strategic Property Management_ , 22(3): 157–167. 

- Arian, Adam, and Muhammad Naeen. 2025. “Climate risk and corporate investment behavior in emerging economies.” _Emerging Markets Review_ , 1–21. 

- Athey, Susan, and Guido W. Imbens. 2022. “Design-based analysis in Difference-inDifferences settings with staggered adoption.” _Journal of Econometrics_ , 226(1): 62–79. 

- Autor, David, Christopher Palmer, and Parag Pathak. 2014. “Housing Market Spillovers: Evidence from the End of Rent Control in Cambridge, Massachusetts.” _Journal of Political Economy_ , 122: 661–717. 

- Ben-Michael, Eli, Avi Feller, and Jesse Rothstein. 2021. “Synthetic Controls with Staggered Adoption.” _Journal of Royal Statistical Society Series B: Statistical Methodology_ , 84(2): 351–381. 

- Binita, KC, Marshall Shepherd, and Cassandra Johnson Gaither. 2015. “Climate change vulnearability assessment in Georgia.” _Applied Georgraphy_ , 62: 62–74. 

- Blanchard, Christopher, Elaine Clegg, and Leslie Martin. 2008. “The Consequences of Residential Infill Development on Existing Neighborhoods in the Treasure Valley.” Idaho Smart Growth and Idaho Urban Land Institute. 

- Boeing, Geoff, Michael Batty, Shan Jiang, and Lisa Schweitzer. 2021. _Handbook of Spatial Analysis in the Social Sciences._ Cheltenham, England and Edward Elgar. 

- Bourassa, Steven C., Martin Hoesli, and Jian Sun. 2005. “The price of aesthetic externalities.” _Jounral of Real Estate Literature_ , 13(2): 167–187. 

- Brunes, Fredrik, Cecilia Hermansson, Han-Suck Song, and Mats Wilhelmsson. 2020. “NIMBYs for the rich and YIMBYs for the poor: Analyzing the property price effects of infill development.” _Journal of European Real Estate Research_ , 13(1): 55–81. 

- Bunten, Devin Michelle, and Matthew E. Kahn. 2014. “The impact of emerging climate risks on urban real estate price dynamics.” _National Bureau of Economic Research_ , Working Paper 20018, National Bureau of Economic Research. 

- Callaway, Brantly, and Pedro H.C. Sant’Anna. 2021. “Difference-in-Differences with multiple time periods.” _Journal of Econometrics_ , 225(2): 200–230. 

18 

City of Savannah. 2024. “Housing Services: Dashboard Reports.” 

City of Savannah. 2025. “Capital Improvement Projects, Blighted Prop Acq Redevelop.” 

- City of Savannah. n.d.. “DreamMaker Home Purchase Assistance.” 

- Clayton, Jim, Steven Devaney, Sarah Sayce, and Jon Van de Wetering. 2021. “Climate Risk and Real Estate Prices: What Do We Know?” _The Journal of Portfolio Management_ , 47(10): 75–90. 

- Combes, Pierre-Philippe, Gilles Duranton, and Laurent Gobillon. 2011. “The identification of agglomeration economies.” _Journal of economic geography_ , 11(2): 253–266. 

- Council on Environmental Quality. 2022. “Climate and Economic Justice Screening Tool. @ONLINE.” 

- de Chaisemartin, Cl´ement, and Xavier D’Haultfœuille. 2020. “Two-way fixed effects estimators with heterogeneous treatment effects.” _American Economic Review_ , 110(9): 2964– 2996. 

- Department of Housing and Urban Development. 2024. “HUD Awards and Allocations: Savannah, GA.” 

- Diamond, Alexis, and Jasjeet S. Sekhon. 2013. “Genetic matching for estimating causal effects: A general multivariate matching method for achieving balance in observational studies.” _The Review of Economics and Statistics_ , 95(3): 932–945. 

- Diamond, Rebecca, and Tim McQuade. 2019. “Who wants affordable housing in their backyard? An equilibrium analysis of low-income property development.” _Journal of Political Economy_ , 127(3): 1063–1117. 

- Dickinson, Christopher J. 2005. “Impediments to Infill Development: An Analysis of Infill Implementation Policies.” Master’s diss. California State University. 

- Ding, Chengri, Robert Simons, and Esmail Baku. 2000. “The effect of residential investment on nearby proiperty values: Evidence from Cleveland, Ohio.” _Journal of Real Estate Research_ , 19(1): 23–48. 

- Ellen, Ingrid Gould, and Ioan Voicu. 2006. “Nonprofit housing and neighborhood spillovers.” _Journal of Policy Analysis and Management_ , 25(1): 31–52. 

- Ellen, Ingrid Gould, Michael H. Schill, Scott Susin, and Amy Ellen Schwartz. 2001. “Building homes, reviving neighborhoods: spillovers from subsidized construction of owner-occupied housing in New York City.” _Journal of Housing Research_ , 12(2): 185–216. 

- Farris, J Terrence. 2001. “The barriers to using urban infill development to achieve smart growth.” _Housing Policy Debate_ , 12(1): 1–30. 

- Fischel, William A. 2000. “Zoning and land use regulation.” _Encyclopedia of law and economics_ , 2: 403–423. 

19 

- Flint, Anthony. 2005. “The density dilemma: appeal and obstacles for compact and transitoriented development.” _Lincoln Institute of Land Policy Working Paper, WP05AF1_ . 

- Funderberg, Richard, and Heather MacDonald. 2010. “Neighborhood valuation effects from new construction of low-income housing tax credit projects in Iowa: A natural experiment.” _Urban Studies_ , 47(8): 1745–1771. 

- Glaeser, Edward L., and James M. Poterba. 2020. _Economic Analysis and Infrastructure Investment._ The University of Chicago Press. 

- Glaeser, Edward L, and James Poterba. 2021. “Economic perspectives on infrastructure investment.” In _Rebuilding the Post-Pandemic Economy_ . Aspen Institute Press. 

- Glaeser, Edward L., and Joshua D. Gottlieb. 2009. “The wealth of cities: Agglomeration economies and spatial equilibrium in the United States.” _Jounral of Economic Literature_ , 47(4): 983–1028. 

- Goodman-Bacon, Andrew. 2021. “Difference-in-differences with variation in treatment timing.” _Journal of Econometrics_ , 225(2): 254–277. 

- Grenadier, Steven. 1996. “The Strategic Exercise of Options: Development Cascades and Overbuilding in Real Estate Markets.” _The Journal of Finances_ , 51: 1653–1679. 

- Grodzins, Morton. 1957. “Metropolitan Segregation.” _Scientific American_ , 197: 33–41. 

- Ham, Dae Woong, and Luke Miratrix. 2024. “Benefits and costs of matching prior to a Difference in Difference analysis when parallel trends does not hold.” _The Annals of Applied Statistics_ , 18(3): 2096–2122. 

- Han, Hye-Sung. 2019. “Explorinng Threshold Effects in the Impact of Housing Abandonment on Nearby Property Values.” _Urban Affairs Review_ , 55: 773–799. 

- Haninger, Kevin, Lala Ma, and Christopher Timmins. 2017. “The value of brownfield remediation.” _Journal of the Association of Environmental and Resource Economists_ , 4(1): 197– 241. 

- Hou, Deyi, Abir Al-Tabbaa, David O’Connor, Qing Hu, Yong-Guan Zhu, Liuwei Wang, Niall Kirkwood, Yong Sik Ok, Daniel CW Tsang, Nanthi S Bolan, et al. 2023. “Sustainable remediation and redevelopment of brownfield sites.” _Nature Reviews Earth & Environment_ , 4(4): 271–286. 

- Kurvinen, Antti Tapio, and Jaakko Vihola. 2020. “The impact of residential development on nearby housing prices.” _International Journal of Housing Markets and Analysis_ , 9(4): 671– 690. 

- Lee, Chang-Moo, and Peter Linneman. 1998. “Dynamics of the greenbelt amenity effect on the land market—The Case of Seoul’s greenbelt.” _Real Estate Economics_ , 26(1): 107–129. 

20 

- Liang, Xiaofan, Brian Brainerd, Tara Hicks, and Clio Andris. 2024. “Lessons from a humanin-the-loop machine learning approach for identifying vacant, abandoned, and deteriorated properties in Savannah, Georgia.” _Journal of Planning Education and Research_ . 

- Lupton, Nathaniel C, Alfredo Jimenez, Secil Bayraktar, and Dimitrios Tsagdis. 2019. “Climate risk and private participation projects in infrastructure: Mitigating the impact of locations (dis)advantages.” _Management Decision_ , 51–67. 

- Malpezzi, Stephen. 1996. “Housing prices, externativies, and regulation in U.S. Metropolitan Areas.” _Journal of Housing Research_ , 7(2): 209–241. 

- McConnell, Virginia, and Keith Wiley. 2011. “Infill development: Perspectives and evidence from economics and planning.” In _The Oxford Handbook of Urban Economics and Planning_ . Oxford Academic. 

- Milkoreit, Manjana, Jennifer Hodbod, Karina Benessaiah Jacopo Baggio3, Rafael CalderonContreras, Jonathan F Donges, Jean-Denis Mathias, Juan Carlos Rocha, Michael Schoon, and Saskia E Werners. 2018. “Defining tipping points for social -ecological systems scholarship - an interdisciplinary literature review.” _Environmental Research Letters_ , 1–12. 

- Newell, Thomas A. 2010. “Development and neighborhood revitalization: The effects of residential investment on property values in Durham, NC.” _The Michigan Journal of Business_ , 3: 97–120. 

- Nordahl, Berit Irene, and Dag Einar Sommervoll. 2020. “Reaping the premium in urban redevelopment.” _Cities_ , 141: 1–10. 

- Nygaard, Christian, George Galster, and Stephen Glackin. 2022. “The Size and Spatial Extent of Neighborhood Price Impacts of Infill Development: Scale Matters?” _Journal of Real Estate Finance and Economics_ , 69: 277–306. 

- Ooi, Joseph T.L., and Thao T.T. Le. 2013. “The spillover effects of infill developments on local housing prices.” _Regional Science and Urban Economics_ , 43(6): 850–861. 

- Partnership for Inclusive Innovation, Georgia. 2020. “City of Savannah Savannah Blight, Civic Data Science for Equitable Development.” 

- Preez, Mario Du. 2013. “The impact of social housing developments on nearby property prices: a Nelson Mandela Bay case study.” _South African Journal of Economics_ , 81(3): 451–466. 

- Rao, Gita, and Aaron Krol. 2022. “Investing and Climate Change.” 

- Ratter-Rieck, Jacqueline M, Michael Roden, and Christian Herder. 2023. “Diabetes and climate change: current evidence and implications for people with diabetes, clinicians and policy stakeholders.” _Diabetologia_ , 66(6): 1003–1015. 

- Redding, Stephen, and Esteban Rossi-Hansberg. 2017. “Quantitative Spatial Economics.” _Annual Review of Economics_ , 9: 21–58. 

21 

- Rosenbaum, Paul R., and Donald B. Rubin. 1983. “The central role of the propensity score in observational studies.” _Biometrika_ , 70(1): 41–55. 

- Rosenthal, Stuart S, and William C Strange. 2020. “How close is close? The spatial reach of agglomeration economies.” _Journal of economic perspectives_ , 34(3): 27–49. 

- Rossi-Hansberg, Esteban, and Pierre-Daniel Sarte. 2012. “Economics of housing externalities.” _International Encyclopedia of Housing and Home_ , 2: 47–50. 

- Rossi-Hansberg, Esteban, Pierre-Daniel Sarte, and Raymond Owens III. 2010. “Housing externalities.” _Journal of Political Economy_ , 118(3): 485–535. 

- Rowley, Steven, and Peter Phibbs. 2012. “Delivering diverse and affordable housing on infill development sites.” _Australian Housing Urban Research Institute_ , 40–70. 

- Schelling, Thomas C. 1978. _Micromotives and Macrobehavior._ The Journal of Politics. 

- Schwartz, Amy Ellen, Ingrid Gould Ellen, Ioan Voicu, and Michael H. Schill. 2006. “The external effects of place-based subsidized housing.” _Regional Science and Urban Economics_ , 36(6): 679–707. 

- Stuart, Elizabeth A., Gary King, Kosuke Imai, and Daniel Ho. 2011. “MatchIt: Nonparametric preprocessing for parametric causal inference.” _Journal of Statistical Software_ , 42(8): 1– 28. 

- Sun, Liyang, and Sarah Abraham. 2021. “Estimating dynamic treatment effects in event studies with heterogeneous treatment effects.” _Journal of Econometrics_ , 225(2): 175–199. 

- Theodos, Brett, George Galster, and Amanda Hermans. 2024. “Neighborhood Home Price Impacts of Community Development Block Grant Spending.” _Cityscape_ , 26: 25–52. 

- Theodos, Brett, Georgia Galster, and Amanda Hermans. 2025. “The Home Price Impacts of CDBG-Funded Investments: An Exploration into Nonlinear and Threshold Effects.” _Housing Policy Debate_ , 35: 422–451. 

- U.S. Environmental Protection Agency. 2007. “Measuring the Air Quality in Transportation Impacts of Infill Development.” 

- U.S. Environmental Protection Agency. 2014. “Investing in Infill Development.” 

- U.S. Environmental Protection Agency. 2015. “Attracing Infill Developments in Distressed Communities: 30 Strategies.” 

- Wen, Haizhen, Yan Zhang, and Ling Zhang. 2015. “Assessing amenity effects of urban landscapes on housing price in Hangzhou, China.” _Urban Forestry Urban Greening_ , 14(4): 1017–1026. 

- Xu, Weidong, Wenxuan Huang, and Donghui Li. 2024. “Climate risk and investment efficiency.” _Journal of International Financial Markets, Institutions and Money_ , 1–28. 

22 

- Yuan, Feng, Yehua Dennis Wei, and Jiawei Wu. 2020. “Amenity effects of urban facilities on housing prices in China: Accessibility, scarcity, and urban spaces.” _Cities_ , 96: 1–11. 

- Zahirovich-Herbert, Velma, and Karen Gibler. 2014. “The effect of new residential construction on housing prices.” _Journal of Housing Economics_ , 26: 1–18. 

- Zheng, Xian, Jun-xian Li, and Junyu Lv. 2020. “Multi-owned property, urban renewal and neighborhood proiperty value externailites: Revisiting the Hong Kong case.” _Cities_ , 107: 1–14. 

23 

**9 Appendix** 

24 

Table A1: Data dictionary 

||Data Type|Description|Source|||
|---|---|---|---|---|---|
|Property<br>Variables||||||
|Address<br>PARID|String<br>String|Full address for a property<br>Parcel ID for a property|City<br>City|||
|Type|String|Type of residential property (for example,<br>single-family residence, town house, etc.)|City|||
|Stories|Float|Number of stories|City|||
|Grade|Float|Discrete value refecting the condition of<br>the property. Values range from 1, 1.5, 2,<br>2.5,. . . , 6|Chatham<br>Database|Tax|Assessor|
|Year Built|Int|Year the property was built|Chatham<br>Database|Tax|Assessor|
|Living|Float|Building area of the property (sqft)|Chatham|Tax|Assessor|
|Area|||Database|||
|Land Area|Float|Land area of the parcel (sqft)|Chatham<br>Database|Tax|Assessor|
|Bedrooms|Int|Number of bedrooms|Chatham<br>Database|Tax|Assessor|
|Bathrooms|Int|Number of bathrooms|Chatham<br>Database|Tax|Assessor|
|Longitude|Float|Longitude value of the parcel’s centroid|Savannah <br>Informatio|Area G<br>n Syste|eographic<br>m|
|Latitude|Float|Latitude value of the parcel’s centroid|Savannah <br>Informatio|Area G<br>n Syste|eographic<br>m|
|Nearest<br>Park|String|Name of the nearest park|Savannah <br>Informatio|Area G<br>n Syste|eographic<br>m|
|Park<br>Dis-<br>tance|Float|Distance to the nearest park|Author de|rived||



|INFILL|Int|Binary indicator for receiving infll assis-<br>tance|City|
|---|---|---|---|
|Closest In-<br>fll|String|Parcel ID of the closest property that re-<br>ceived infll assistance|Author derived|
|Closest<br>Infll<br>Dis-<br>tance|Int|Straight line distance to the closest infll<br>property|Author derived|
|Census<br>Variables||||
|Blockgroup<br>Total Pop|String<br>Int|Blockgroup a property is in<br>Total population of the blockgroup|Census Reporter<br>Census Reporter|
|Male Pct|Float|Male %|Census Reporter|
|Female Pct|Float|Female %|Census Reporter|
|Pop<br>Den-|Int||Census Reporter|
|sity||||
|Median|Float|Median age|Census Reporter|
|Age||||
|Income|Float|Average income|Census Reporter|
|Pcp||||
|White Pct|Float|White %|Census Reporter|
|Black Pct|Float|Black %|Census Reporter|
|Native Pct|Float|Native %|Census Reporter|
|AAPI Pct|Float|AAPI %|Census Reporter|
|Hispanic<br>Pct|Float|Hispanic %|Census Reporter|
|Other Pct|Float|Other ethnicity %|Census Reporter|
|Married|Float|Married household %|Census Reporter|
|Single<br>Fe-<br>male|Float|Single female household %|Census Reporter|
|Single<br>Male|Float|Single male household %|Census Reporter|



|Non-|Float|Non-family household %|Census Reporter||
|---|---|---|---|---|
|Family|||||
|Total<br>Units|Float|Total units in the block group<br>|Census Reporter||
|Occupied<br>Vacant|Float<br>Float|Occupied units %<br>Vacant units %|Census Reporter<br>Census Reporter||
|Owner|Float|Owned units %|Census Reporter||
|Renter|Float|Rented units %|Census Reporter||
|High<br>School|Float|High school educated %|Census Reporter||
|Bachelors|Float|Bachelors educated %|Census Reporter||
|Time<br>Variant<br>Variables|||||
|Year|Int|Year of an observation|Chatham<br>Tax<br>Database/Savann|Assessor<br>ah<br>Area|
||||Geographic<br>In<br>System|formation|
|Appraised<br>Building|Int|Appraised building value of a property|Chatham<br>Tax<br>Database/Savann<br>Geographic<br>In<br>System|Assessor<br>ah<br>Area<br>formation|
|Appraised<br>Land|Int|Appraised land value of a parcel|Chatham<br>Tax<br>Database/ Savan<br>Geographic<br>In<br>System|Assessor<br>nah Area<br>formation|
|Infll Year|Int|Year of receiving infll assistance (N/A if<br>never received)|City||



Table A2: Covariate balance before matching, parcel-level 

|**Variable**|**Treated Mean**|**Control Mean**|**Mean Diference**|**t-Statistic**|
|---|---|---|---|---|
|Grade|2.548|3.380|-0.832|-81.398|
|Per capita income|20,294.81|36,606.26|-16.411.45|-84.182|
|Dist. nearest park|371.920|1,663.697|-1,291.777|-180.34|
|Year built|1950.411|1976.667|-26.256|-55.458|
|No. bath|1.374|1.923|-0.549|-55.461|
|No. bedrooms|2.669|2.940|-0.271|-13.495|
|No. stories|1.161|1.253|-0.092|-15.379|
|Population density|5,495.39|2,453.05|3,042.34|72.736|
|% single female|47.616|20.146|27.470|103.97|
|% black|84.5|32.6|51.961|174.05|



Table A3: Covariate balance after matching, parcel-level 

|**Variable**|**Treated Mean**|**Control Mean**|**Mean Diference**|**t-Statistic**|
|---|---|---|---|---|
|Grade|2.548|2.539|0.009|0.590|
|Per capita income|20,294.81|20,653.80|69.740|-0.244|
|Dist. nearest park|371.920|378.570|-6.650|-1.112|
|Year built|1950.411|1950.539|-0.128|-0.185|
|No. bath|1.374|1.372|0.002|0.117|
|No. bedrooms|2.669|2.680|-0.011|-0.398|
|No. stories|1.161|1.160|0.001|-0.039|
|Population density|5,495.39|5,503.692|-8.302|-0.129|
|% single female|47.616|47.540|0.127|-0.189|
|% black|84.5|84.4|0.076|-0.288|



Table A4: Median bias reductions for PSM versus genetic matching, parcel-level 

|**Distance**|**PSM**|**Gen Match**|
|---|---|---|
|25|94.390%|99.310 %|
|50|95.717%|98.699%|
|75|93.150%|99.190%|
|100|91.217%|99.115%|



28 

Table A5: Spillover treatment effects of infill development by infill density quintiles, blocklevel using synthetic control method 

||||Infll density|%||
|---|---|---|---|---|---|
||1|2|3|4|5|
||(0.4, 4.5)|(4.5, 6.3)|(6.3, 8.3)|(8.3, 16.7)|(16.7, 76.9)|
|Mean spillover efect,|0.816|2.510|0.175|-0.464|6.980**|
|($/sqft)|(2.215)|(2.436)|(3.607)|(1.706)|(3.099)|
|Percent increase in value|-|-|-|-|22.6%|
|_ν_|0.510|0.414|0.387|0.406|0.475|
|Global L2 imbalance|0.013|0.010|0.027|0.008|0.212|
|Individual L2 imbalance|2.197|0.357|1.229|0.455|2.121|
|No. of treated blocks|33|32|32|33|30|
|No. of donor blocks|119|181|169|118|61|
|No. of block-year observations|3,404|4,922|4,623|3,473|2,093|



Note: Significant to p _<_ *0.1, **0.05, ***0.01. The dependent variable is the block-level average appraised building value divided by the block-level average living area square footage of residential properties. Treated blocks include any blocks that contained at least one infill development, and quintiles are created by ranking treated blocks by infill density. Treatment effects are estimated using the staggered synthetic control method (SCM) proposed by BenMichael et al. (Ben-Michael, Feller and Rothstein (2021)). 

Table A6: Placebo tests, parcel-level 

|**Distance**|**Spillover efect**|
|---|---|
|25|-0.189|
||(0.659)|
|50|0.346<br>(0.330)|
|75|0.360<br>(0.257)|
|100|0.143<br>(0.306)|



29 

Table A7: Placebo tests, block-level 

||||Infll density|%||
|---|---|---|---|---|---|
||1|2|3|4|5|
||(0.4, 4.5)|(4.5, 6.3)|(6.3, 8.3)|(8.3, 16.7)|(16.7, 76.9)|
|Dif-in-dif placebo|1.962|1.403|-1.243|-0.154|0.540|
||(1.345)|(0.889)|(0.884)|(0.650)|(0.999)|
|Synthetic controls|-1.882|-2.832|1.545|-1.884|-2.604|
|placebo|(3.490)|(3.840)|(4.681)|(2.559)|(3.258)|



Note: Significant to p _<_ *0.1, **0.05, ***0.01. The dependent variable is the block-level average appraised building value divided by the block-level average living area square footage of residential properties. Treatment effects are estimated using the Sun & Abraham staggered difference-in-differences estimator and the synthetic control method with staggered adoption proposed by Ben-Michael et al. (Sun and Abraham (2021); Ben-Michael, Feller and Rothstein (2021)). Standard errors are clustered by block ID. 

30 

Figure A1 



31 

Figure A2: Event study without matching 



<!-- Start of picture text -->
25<br>20<br>15<br>10<br>5<br>0<br>−5<br>−10<br>−15<br>−16 −14 −12 −10 −8 −6 −4 −2 0 2 4 6 8 10 12 14 16<br>Years since intervention<br>Appraised value per Sqft<br><!-- End of picture text -->

32 

Table A8: TWFE versus Sun & Abraham spillover effects, parcel-level 

|**Distance**|**TWFE**|**SunAb**|
|---|---|---|
|25|0.762|3.610**|
||(1.215)|(1.440)|
|50|0.013|1.961***|
||(0.572)|(0.680)|
|75|-0.228|1.632***|
||(0.427)|(0.512)|
|100|-0.795*|0.635|
||(0.408)|(0.511)|



Table A9: TWFE versus Sun & Abraham spillover effects, block-level 

|**Quintile**|**TWFE**|**SunAb**|
|---|---|---|
|1|0.425|2.852|
||(2.321)|(2.331)|
|2|2.326|2.779|
||(2.645)|(2.753)|
|3|-0.242|4.691|
||(3.165)|(4.079)|
|4|-1.261|0.223|
||(1.536)|(1.661)|
|5|6.947***|11.046***|
||(2.170)|(1.438)|



33 

