---
title: NBER-CRIW-2026-Ch3-Bell-Geographic-PageRank
type: paper
source_pdf: raw/papers/NBER-CRIW-2026-Ch3-Bell-Geographic-PageRank.pdf
converted: 2026-08-18
---

# **Measuring Housing Quality Using Revealed Preference:** 

# **A Geographic PageRank Approach *** 

Alex Bell<sup>†1</sup> Sophie Calder-Wang<sup>‡2</sup> Shusheng Zhong<sup>¶3</sup> 

# **Abstract** 

This paper introduces Geographic PageRank (GPR), an innovative measure of place quality that is based on migration decisions, employing a recursive algorithm that leverages the full network of migration flows. Using various public data sources, we construct GPR rankings for U.S. counties and metropolitan areas. We also extend the rankings to capture changes over time and differences for population subgroups, providing a versatile data product. As an application, we show that GPR can serve as an “anti-instrument” for unobserved housing quality when pricing environmental amenities, recovering a correctly signed implicit price of air pollution that is in line with quasiexperimental benchmarks. 

_Keywords:_ PageRank, Housing and Neighborhood Quality, Amenities 

_JEL Code_ : R32, R31, C39 

# **1 Introduction** 

This paper introduces Geographic PageRank (GPR), a novel metric that leverages the network of migration flows as a revealed-preference mechanism to measure the quality ranking of a place. We begin with the well-known PageRank algorithm developed in computer science by Page (2001), the key innovation underlying Google’s search rankings. Instead of using the algorithm to model the network connections of webpages, we adapt it to model the network connections of places, as characterized by the migration flows that connect different places into a network. Intuitively, the 

> * We thank Joshua Boyd for excellent research assistance. Calder-Wang acknowledges financial support from the Zell/Lurie Real Estate Center at the Wharton School for research assistance. Detailed Geographic PageRank data for visualization and download are available at <u>https://sophieqzwang.github.io/geopagerank/.</u> 

> † Department of Economics, Georgia State University, _ambell@gsu.edu_ 

> ‡The Wharton School, University of Pennsylvania, _sophiecw@wharton.upenn.edu_ ¶Kellogg School of Management, Northwestern University, Kellogg School of Management, Northwestern University, _shusheng.zhong@kellogg.northwestern.edu_ 

> ¶Kellogg School of Management, Northwestern University, Kellogg School of Management, Northwestern University, 

1 

algorithm delivers a measure of the desirability of a particular location by computing it recursively: _locations that draw in migration are considered desirable, whereas locations that draw in migration from other desirable locations are considered even more desirable_ . Conversely, an undesirable location is characterized by out-migration and by population outflow to other undesirable locations. In doing so, the GPR measure effectively encapsulates information embedded in the _entire migration network_ , rather than conventional metrics such as net migration, which is defined based on the net flow of the focal location itself. 

The PageRank algorithm’s ability to characterize information from the entire network using a recursive method has proven effective across many domains. The original PageRank algorithm, developed by Larry Page, was extremely effective in producing informative rankings and was foundational to Google’s rise as the most popular search engine. In computer science, the use of PageRank-type algorithms has become pervasive and standard in many network problems (Berkhin 2005), and its uses have been extended to many other fields, including biology, chemistry, neuroscience, and physics (Gleich 2015). 

In economics, using PageRank to characterize network properties as a measure of economic features is emerging. In labor economics, a seminal paper is Sorkin (2018), which uses workers’ history of employer-to-employer transitions to characterize the network of firms and thereby a ranking of firm quality. The core intuition is that, excluding layoffs, workers who switch firms tend, on average, to move from worse to better firms, as revealed by their preferences. Such measures of firm or job quality then become an input to estimating the role of compensating differentials in labor markets. Related work in the labor literature has shown the effectiveness of migration-based measures in various job-ladder models to capture firm quality in several contexts (Bagger and Lentz 2019; Morchio and Moser 2020; Taber and Vejlin 2020). 

In urban economics, however, there has been no systematic effort in any published work to leverage PageRank as a measure of housing quality. We contribute to the literature by making the conceptual leap to identify a new context in which the ranking algorithm can be applied and, correspondingly, how the resulting rankings can be used.<sup>1</sup> As with the labor context, the core intuition is that, unless forced to, households, on average, move from worse to better locations, as revealed by their preferences. The attractiveness of a place is determined by its price (i.e., the cost of housing) and its amenities, much as the attractiveness of a firm is characterized by the wage it offers and its job amenities.<sup>2</sup> Recent developments in the housing literature, such as Epple, Quintero and Sieg (2020) and Landvoigt, Piazzesi and Schneider (2014, 2015), highlight the vertical measure of housing quality as the primary dimension where markets become segmented and differentiated. In this regard, Geographic PageRank can be used to capture the vertical dimension of the market. 

Concretely, we start with county-to-county migration data from the Internal Revenue Service (IRS) to produce the Geographic PageRank for all U.S. counties. We show that although it correlates with net migration rates, substantial differences remain. In addition, we apply the GPR framework to different spatial units and across different time periods to illustrate the changing dynamics of different places. More generally, if researchers have more granular data available to them, such as restricted census data, the GPR measure can be readily extended to greater levels of geographic granularity such as neighborhood or census tract-level rankings. 

1 We note that in contemporaneous unpublished work, Fogel (2021) applies a similar approach to estimate city values based on migration flows, with a particular focus on understanding its relationship with local labor demand shocks, which is found to be null. By contrast, our GPR measure not only greatly expands the scope of rankable places, but we also illustrate how GPR can be used for measuring housing quality, and thus becomes useful for studying local housing markets and the capitalization of amenities at the neighborhood level. 

2 That said, there are underlying structural differences in how prices are determined (e.g., housing supply constraints vs. worker productivity) and in how amenities are formed (e.g., endogenous amenities arising from positive or negative spillovers vs. a cost to a firm when offering amenities). 

While the IRS migration data captures the full population of tax return filers, it lacks detailed household information or finer measures of geographic delineation. To address this data limitation, we turn to the American Community Survey (ACS) 5-year microdata, which allows us to measure the PageRank of places by population subgroups such as age, education, race/ethnicity, household structure, and housing tenure. While subgroup rankings are generally highly positively correlated, important differences emerge. 

Lastly, to illustrate how GPR can correct biases in standard hedonic models, we provide an example by evaluating the implicit price of environmental amenities, specifically air quality, highlighting how GPR can serve as an effective “anti-instrument”, an identification and estimation strategy developed in Bell, Billings, Calder-Wang and Zhong (2024), to recover sensible estimates of the capitalization effect of air pollution on housing markets.<sup>3</sup> Notably, GPR allows us to produce implicit amenity prices using observational data alone, and we obtain estimates that are largely in line with Chay and Greenstone (2005), which offers the best evidence in the literature that relies on natural experiments. 

The remainder of the paper is organized as follows. Section 2 provides the mathematical foundations for the PageRank algorithm. Section 3 describes various sources of migration data used. Section 4 describes the rankings produced at the county and CBSA levels. It also describes how GPR can be extended in various ways. Section 5 presents an example of using GPR to price environmental amenities in the housing market. Section 6 concludes. 

# **2 Mathematical Foundations of Geographic PageRank** 

In this section, we describe the mathematical foundations of the PageRank algorithm. 

> 3 For a survey of related work in the labor context, see Bell (2020) and Bell (2025). 

The key idea behind “Geographic PageRank” is to capture a ranking of geographic locations using a recursive logic based on migration: by revealed preference, when households move, they must on average move to a “better” place than their previous place, and places that draw people from “better” places are considered “best” places. As such, we use a matrix of migration to arrive at a ranking of places based on this recursive definition of desirability. 

At a conceptual level, our proposed Geographic PageRank algorithm ranks a location by its share in the stationary distribution of household locations in accordance with the migration matrix. Specifically, let the migration matrix _Mi,j_ represent the fraction of population migrating from location _j_ to _i_ . In other words, the matrix specifies the destination locations for everyone from location _j_ , and _Mi,j_ represents a transition matrix (in a column format) such that every column sums to one 



In its simplest form, the PageRank algorithm computes the column vector _v_ such that 



Equivalently, _v_ represents the eigenvector associated with eigenvalue 1 for the transition matrix _M_ .<sup>4</sup> In this sense, the resulting eigenvector _v_ represents the stationary distribution of the population if they migrated according to the transition matrix _M_ indefinitely: namely, the transition matrix _M_ on the distribution _v_ recovers _v_ . As a last step, we obtain the ordinal “rank” of location _i_ based on the value of each element _vi_ . 

> 4 In practice, the PageRank algorithm also allows for a damping factor _d_ such that every period a small fraction 1 _− d_ from each node will be randomly redistributed to all other nodes to ensure numerical stability. We find that the ordinal ranks of the nodes are not sensitive to the choice of the damping factor. As such, the PageRank algorithm could be viewed as one of the spectral methods derived from eigenvector centrality in network analysis, but has properties to ensure desirable numerical stability, especially with disconnected graphs. 

To provide some intuition behind the PageRank algorithm, consider the following stylized example. In Panel (A) of Figure 1, there are three locations A, B, and C. Assume that they are equal-sized cities and we observe that 10% of C’s residents migrated to A and another 10% migrated to B. Performing the PageRank algorithm on the resulting migration matrix _M_ results in an equal ranking between A and B, which are both ranked above location C. 

In Panel (B) of Figure 1, we also consider three locations A, B, and C. However, in this case, we find 5% of C’s residents migrated to A, and 15% migrated to B. Moreover, we find that 5% of B’s residents also migrated to A. In this case, the PageRank algorithm ranks A above B, and then above C. Notably, the PageRank algorithm contains more information than simple counts of net-migration: even though both locations A and B see a net in-migration of 10% in both examples, the PageRank algorithm ranks A above B in the second example, as A is drawing residents from B, which is in turn more desirable than C. 

Figure 1: An Example of PageRank Algorithm 



_Notes:_ This figure illustrates a simple example of the PageRank algorithm. In the top panel (A), there are three locations A, B, and C, where there is a net migration from location C to both A and B in equal proportions. The adjacency matrix _Mi,j_ indicates the transition probabilities in the column format, namely, _Mi,j_ represents the fraction departing from node _j_ for node _i_ . As such, the normalization requires = 1. The resulting rank is _A_ = _B > C_ . By contrast, the bottom panel (B) illustrates another example where there is not only a migration from C, but also some 𝑖𝑖 𝑖𝑖,𝑗𝑗 ∀𝑗𝑗: ∑𝑀𝑀 migration from B to A. Note that the net in-migration for both examples for locations A and B is the same, namely, a net migration of 10%. However, because location A is drawing people from the more desirable location B, as opposed to C, the resulting rank has A being ranked above B, namely _A > B > C_ . 

Beyond its widespread application in computer science, Sorkin (2018) was the first to use the PageRank algorithm in economics, where he applied it to ranking a set of U.S. firms in the labor market context. Indeed, Sorkin (2018) proceeds to use the ranking of firms as a way to measure how much wage dispersion is due to job amenities. We highlight that there is a natural parallel between the challenges of the empirical valuation of job amenities and the empirical valuation of neighborhood amenities, even though there has not been much overlap between the two literatures in recent work. As such, our work fits into this important theoretical and methodological gap of estimating a hedonic price in the presence of hard-to-measure unobserved quality. 

# **3 Data** 

In this section, we describe the various data sources we use to measure geographic mobility, which serves as the basis for the PageRank algorithm. 

# **3.1 IRS County-to-County Migration** 

The first data source is the county-to-county migration data from the Internal Revenue Service (IRS) Statistics of Income (SOI) Division, which is “based on year-to-year address changes reported 

on individual income tax returns filed with the IRS.”<sup>5</sup> A key advantage of the IRS data is that it is publicly available and covers the entire universe of population with Forms 1040 filings. Another advantage is that it has a long time coverage, from 1991 to present. The main drawbacks are that it does not cover migration at a finer geographic level below the county level or by demographics, and it does not include non-filers. Furthermore, flows between counties with fewer than 20 returns are suppressed for confidentiality protection. 

# **3.2 ACS** 

A second data source we use is the migration information from the American Community Survey (ACS) microdata. A key advantage of the ACS microdata is that it contains a wide set of demographics of each member of the household, ranging from age, educational attainment, race/ethnicity, employment status, industry code, as well as household characteristics such as whether they are renters or owners. 

In terms of migration variables, the ACS asks respondents about their current home location and their home location one year ago. While a household’s current location is measured in Migration Public Use Microdata Area (PUMA), which are areas with at least 100,000 people, their past location is measured in Migration Public Use Microdata Area (MIGPUMA), which are larger geographic units that typically encompass several PUMAs and often cross county lines. As a result, the relatively large sizes of the MIGPUMA in the public dataset limit our ability to produce rankings with finer geographic granularity, and in practice, we aggregate rankings to the metropolitan level.<sup>6</sup> 

> 5 See the IRS 2018-2019 Migration Data Users Guide at https://www.irs.gov/pub/irssoi/1819inpublicmigdoc.pdf. 

> 6 We use the ACS field MIGMET131, which captures the metropolitan area of residence 1 year ago (using 2013 delineations). 

# **3.3 Data Sources for Future Work** 

Even though we have focused on producing Geographic PageRanks using publicly available data, we point out that the ranking algorithm is naturally portable to other datasets that are available to researchers to suit their needs. In particular, if a researcher has access to restricted census data, they would be able to produce rankings at finer geographic granularities, use custom boundaries such as Mast (2025), and/or cut by population subgroups that are most relevant to their research question. Further, if researchers have access to marketing datasets such as Data Axle or Infutor, which typically provide address-level information, rankings at finer geographic granularities can also be achieved, with the usual caveat that it is important to understand what population gets included in these commercial datasets over time. 

# **4 Geographic PageRank Estimates** 

# **4.1 A Ranking of U.S. Counties** 

To implement the Geographic PageRank algorithm at the national level, we use the outflow version of the IRS 2021-2022 county-to-county Migration Data, which records “the number of residents leaving a State or county and where they went.” Table 1 Panel A shows the summary statistics for the IRS migration data. Out of 3144 counties, the mean total outflow is 2081 with a standard deviation of 7389, and a median total outflow of 296. There are 53,770 origin-destination county pairs out of all 9,884,736 (= 3144<sup>2</sup> ) possible pairs. Within these county pairs, the mean migration flow is 122 with a standard deviation of 462, and the median migration flow is 41. 

Table 1: Summary Statistics for 2021-2022 IRS Migration Data 

|**Panel A: County-**|**to County Mig**<br>|**ration**<br>||
|---|---|---|---|
||County|County|Origin-Destination Pairs|
||Outflows|Inflows|Migration Flows|
||(1)|(2)|(3)|
|Mean|2081|2081|122|
|SD|7389|6624|462|
|25th Percentile|87|81|27|
|Median|296|312|41|
|75th Percentile|1020|1137|82|
|N|3144|3144|53770|
|**Panel B: Metro-t**|**o-Metro Migra**<br>|**tion**<br>||
||CBSA|CBSA|Origin-Destination Pairs|
||Outflows|Inflows|Total Movers|
||(1)|(2)|(3)|
|Mean|4050|4050|195|
|SD|14216|12026|709|
|25th Percentile|333|315|28|
|Median|761|835|54|
|75th Percentile|2228|2293|140|
|N|925|925|19175|



_Notes_ : This table uses county-to-county migration counts from the IRS from 2021 to 2022. Counties with fewer than 20 counts are suppressed in the data. Columns 1 and 2 report county (or CBSA) level summary statistics for total migration flows out of and into each county (or CBSA), respectively. Column 3 reports summary statistics for migration flows at the origin-destination pair level. 

Next, we obtain the corresponding rankings of all U.S. counties using the Geographic PageRank algorithm described above.<sup>7</sup> Figure 2 illustrates the rankings on the map: darker shades indicate higher-ranked (i.e., more desirable) counties and lighter shades indicate lower-ranked (i.e., less desirable) counties. We generally find higher-ranked counties along the coastal regions. Table 2 shows the top 50 counties by their Geographic PageRank, with the top ranked counties being Harris County, TX (with a county seat of Houston), Maricopa County, AZ (with a county seat of Phoenix), Bexar, 

> 7 Our specific implementation assumes a damping factor of _d_ = 0 _._ 85, which corresponds roughly to the average stay rate. 

TX (with a county seat of San Antonio), Cook County, IL (with a county seat of Chicago), Tarrant, TX (with a county seat of Fort Worth). 

Figure 2: County-level PageRank using IRS County Migration Data 



_Notes_ : This map shows geographic PageRank at the county level constructed using nationwide IRS county migration flow data in 2021. Darker shades indicate better-ranked counties and lighter shades indicate worse-ranked counties. For a more interactive way to view the map, please visit https://sophieqzwang.github.io/geopagerank/. 

Table 2: Top Ranked Counties in the U.S. (2021-2022) 

|Ranking|FIPS Code|County Name|MSA Name|
|---|---|---|---|
|1|48201|Harris|Houston-Pasadena-The Woodlands, TX|
|2|4013|Maricopa|Phoenix-Mesa-Chandler, AZ|
|3|48029|Bexar|San Antonio-New Braunfels, TX|
|4|17031|Cook|Chicago-Naperville-Elgin, IL-IN|
|5|48439|Tarrant|Dallas-Fort Worth-Arlington, TX|
|6|48113|Dallas|Dallas-Fort Worth-Arlington, TX|
|7|6037|Los Angeles|Los Angeles-Long Beach-Anaheim, CA|
|8|19153|Polk|Des Moines-West Des Moines, IA|
|9|27053|Hennepin|Minneapolis-St. Paul-Bloomington, MN-WI|
|10|40109|Oklahoma|Oklahoma City, OK|
|11|39049|Franklin|Columbus, OH|
|12|48303|Lubbock|Lubbock, TX|
|13|37183|Wake|Raleigh-Cary, NC|
|14|40143|Tulsa|Tulsa, OK|



|15|53033|King|Seattle-Tacoma-Bellevue, WA|
|---|---|---|---|
|16|32003|Clark|Las Vegas-Henderson-North Las Vegas, NV|
|17|5119|Pulaski|Little Rock-North Little Rock-Conway, AR|
|18|18097|Marion|Indianapolis-Carmel-Greenwood, IN|
|19|21111|Jefferson|Louisville/Jefferson County, KY-IN|
|20|46099|Minnehaha|Sioux Falls, SD-MN|
|21|20173|Sedgwick|Wichita, KS|
|22|31109|Lancaster|Lincoln, NE|
|23|51059|Fairfax|Washington-Arlington-Alexandria, DC-VA-MD-WV|
|24|16001|Ada|Boise City, ID|
|25|38017|Cass|Fargo, ND-MN|
|26|2020|Anchorage|Anchorage, AK|
|27|49035|Salt Lake|Salt Lake City-Murray, UT|
|28|6073|San Diego|San Diego-Chula Vista-Carlsbad, CA|
|29|31055|Douglas|Omaha, NE-IA|
|30|37119|Mecklenburg|Charlotte-Concord-Gastonia, NC-SC|
|31|47157|Shelby|Memphis, TN-MS-AR|
|32|29077|Greene|Springfield, MO|
|33|51041|Chesterfield|Richmond, VA|
|34|8041|El Paso|Colorado Springs, CO|
|35|48453|Travis|Austin-Round Rock-San Marcos, TX|
|36|35001|Bernalillo|Albuquerque, NM|
|37|29095|Jackson|Kansas City, MO-KS|
|38|12031|Duval|Jacksonville, FL|
|39|13121|Fulton|Atlanta-Sandy Springs-Roswell, GA|
|40|22033|East Baton Rouge|Baton Rouge, LA|
|41|53063|Spokane|Spokane-Spokane Valley, WA|
|42|21067|Fayette|Lexington-Fayette, KY|
|43|30111|Yellowstone|Billings, MT|
|44|48381|Randall|Amarillo, TX|
|45|20091|Johnson|Kansas City, MO-KS|
|46|47037|Davidson|Nashville-Davidson–Murfreesboro–Franklin, TN|
|47|13153|Houston|Warner Robins, GA|
|48|47065|Hamilton|Chattanooga, TN-GA|
|49|47093|Knox|Knoxville, TN|
|50|12057|Hillsborough|Tampa-St. Petersburg-Clearwater,FL|



_Notes_ : Geographic PageRanks are computed from IRS migration data in 2021–2022. 

# **4.2 A Ranking of U.S. Metros** 

Beyond the county-level rankings, it is useful to consider rankings with different geographic granularity. Here, we consider an example of Geographic PageRank for metropolitan areas. Since the US Census assigns the entire county to a single CBSA (Core Based Statistical Area), it prevents a 

county from being split between two CBSAs, and thus allows us to aggregate the IRS county-tocounty moves to metro-to-metro moves. Table 1 Panel B summarizes the moves at the CBSA level. Compared to the county-level moves, metros are significantly larger, with an average number of moves (outflow) at 4050, and a standard deviation of 14,216. Table 3 reports the top 50 CBSAs in the US, with the top ones being Dallas-Fort-Worth-Arlington, TX, Phoenix-Mesa-Chandler, AZ, Houston-Pasadena-The Woodlands, TX, Seattle-Tacoma-Bellevue, WA, and Atlanta-Sandy SpringsRoswell, GA. 

Table 3: Top Ranked CBSAs in the U.S. (2021-2022) 

|Ranking|CBSA Code|Metro Name|
|---|---|---|
|1|19100|Dallas-Fort Worth-Arlington, TX|
|2|38060|Phoenix-Mesa-Chandler, AZ|
|3|26420|Houston-The Woodlands-Sugar Land, TX|
|4|42660|Seattle-Tacoma-Bellevue, WA|
|5|12060|Atlanta-Sandy Springs-Alpharetta, GA|
|6|16980|Chicago-Naperville-Elgin, IL-IN-WI|
|7|33460|Minneapolis-St. Paul-Bloomington, MN-WI|
|8|35620|New York-Newark-Jersey City, NY-NJ-PA|
|9|31080|Los Angeles-Long Beach-Anaheim, CA|
|10|26900|Indianapolis-Carmel-Anderson, IN|
|11|18140|Columbus, OH|
|12|38900|Portland-Vancouver-Hillsboro, OR-WA|
|13|41700|San Antonio-New Braunfels, TX|
|14|36420|Oklahoma City, OK|
|15|28140|Kansas City, MO-KS|
|16|14460|Boston-Cambridge-Newton, MA-NH|
|17|16740|Charlotte-Concord-Gastonia, NC-SC|
|18|47900|Washington-Arlington-Alexandria, DC-VA-MD-WV|
|19|34980|Nashville-Davidson–Murfreesboro–Franklin, TN|
|20|33100|Miami-Fort Lauderdale-Pompano Beach, FL|
|21|45300|Tampa-St. Petersburg-Clearwater, FL|
|22|19820|Detroit-Warren-Dearborn, MI|
|23|39580|Raleigh-Cary, NC|
|24|29820|Las Vegas-Henderson-Paradise, NV|
|25|37980|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|
|26|30780|Little Rock-North Little Rock-Conway, AR|
|27|19780|Des Moines-West Des Moines, IA|
|28|14260|Boise City, ID|
|29|24340|Grand Rapids-Kentwood, MI|
|30|41740|San Diego-Chula Vista-Carlsbad, CA|
|31|12420|Austin-Round Rock-Georgetown, TX|



|32|43620|Sioux Falls, SD-MN|
|---|---|---|
|33|41860|San Francisco-Oakland-Berkeley, CA|
|34|19740|Denver-Aurora-Lakewood, CO|
|35|41180|St. Louis, MO-IL|
|36|10740|Albuquerque, NM|
|37|36740|Orlando-Kissimmee-Sanford, FL|
|38|32820|Memphis, TN-MS-AR|
|39|41620|Salt Lake City, UT|
|40|40900|Sacramento-Roseville-Folsom, CA|
|41|23060|Fort Wayne, IN|
|42|46140|Tulsa, OK|
|43|33340|Milwaukee-Waukesha, WI|
|44|27260|Jacksonville, FL|
|45|38300|Pittsburgh, PA|
|46|48620|Wichita, KS|
|47|39900|Reno, NV|
|48|13820|Birmingham-Hoover, AL|
|49|36540|Omaha-Council Bluffs, NE-IA|
|50|10580|Albany-Schenectady-Troy,NY|



_Notes_ : Geographic PageRanks are computed from IRS migration data in 2021–2022. 

As discussed earlier, another advantage of the IRS data is that it comes with a long historical sample. Thus, we recomputed the metro-level rankings from two decades ago using tax returns filed back in 2001. Table 4 lists what used to be the top 30 ranked metros in 2001, ranked in the order of how their rankings have since changed from 2001 to 2021, from those whose ranking improved the most to those whose ranking declined the most. At the top, we see that Charlotte-Concord-Gastonia, NC-SC (+8), Nashville-Davidson-Murfreesboro-Franklin, TN (+8), Raleigh-Cary, NC (+7), San Antonio-New Braunfels, TX (+6) have improved the most from 2001, corresponding to the growing popularity of the sunbelt; whereas Denver-Aurora-Centennial, CO (-24), San Diego-Chula VistaCarlsbad, CA (-14), Sacramento-Roseville-Folsom, CA (-14), St. Louis, MO-IL (-11) experience the most decline in ranking, some of which reflects a decline in the popularity of California. We report the full top 50 metros from 2001, 2011, and 2021 in Appendix Table A.9. 

Table 4: <u>Changes in Geographic PageRank from 2001 to 2021</u> 

|Top 30 Metros in 2001–2002:<br>|Rank Cha<br>|nge by 2021–2022<br>|
|---|---|---|
|Metro|Rank 2001|–2002 Rank 2021–2022 Improvement|
|Charlotte-Concord-Gastonia, NC-SC|25|17<br>+8|
|Nashville-Davidson–Murfreesboro–Franklin, TN|27|19<br>+8|
|Raleigh-Cary, NC|30|23<br>+7|
|New York-Newark-Jersey City, NY-NJ|14|8<br>+6|
|San Antonio-New Braunfels, TX|19|13<br>+6|
|Boston-Cambridge-Newton, MA-NH|21|16<br>+5|
|Atlanta-Sandy Springs-Roswell, GA|8|5<br>+3|
|Oklahoma City, OK|17|14<br>+3|
|Columbus, OH|13|11<br>+2|
|Tampa-St. Petersburg-Clearwater, FL|23|21<br>+2|
|Seattle-Tacoma-Bellevue, WA|5|4<br>+1|
|Indianapolis-Carmel-Greenwood, IN|11|10<br>+1|
|Dallas-Fort Worth-Arlington, TX|1|1<br>0|
|Phoenix-Mesa-Chandler, AZ|2|2<br>0|
|Houston-Pasadena-The Woodlands, TX|3|3<br>0|
|Chicago-Naperville-Elgin, IL-IN|6|6<br>0|
|Miami-Fort Lauderdale-West Palm Beach, FL|20|20<br>0|
|Detroit-Warren-Dearborn, MI|22|22<br>0|
|Boise City, ID|28|28<br>0|
|Los Angeles-Long Beach-Anaheim, CA|7|9<br>-2|
|Minneapolis-St. Paul-Bloomington, MN-WI|4|7<br>-3|
|Portland-Vancouver-Hillsboro, OR-WA|9|12<br>-3|
|Kansas City, MO-KS|12|15<br>-3|
|Washington-Arlington-Alexandria, DC-VA-MD-WV|15|18<br>-3|
|San Francisco-Oakland-Fremont, CA|29|33<br>-4|
|Las Vegas-Henderson-North Las Vegas, NV|18|24<br>-6|
|St. Louis, MO-IL|24|35<br>-11|
|San Diego-Chula Vista-Carlsbad, CA|16|30<br>-14|
|Sacramento-Roseville-Folsom, CA|26|40<br>-14|
|Denver-Aurora-Centennial, CO|10|34<br>-24|



_Notes_ : Geographic PageRanks are computed from IRS migration data in 2001–2002 and 2021– 2022. 

# **4.3 Interpretation of Rankings** 

Given both the county-level and metro-level rankings over time, it is worth discussing how to interpret a “high-ranked” place. Conceptually, because the realized migration decision is based on a host of considerations, including the value of amenities (exogenous and endogenous), local wages, 

and housing costs, the resulting Geographic PageRank is inherently driven by the combination of all these factors. Said differently, the Geographic PageRank represents an equilibrium object that captures both demand-side factors (e.g., the attributes of a place, including its labor market attributes) and supply-side factors (e.g., housing costs due to supply constraints). 

To better understand the statistical properties of the ranking, we show that places with population growth are ranked higher on average. The top panel of Figure 3 shows the binscatter between Geographic PageRank and the population growth rate at the county level, clearly indicating a positive relationship, at least up to a certain level of population growth. However, there remains significant dispersion at the same level of population growth, as shown in the bottom panel of Figure 3. In particular, notice that places with extremely positive values of population growth are unlikely to have the highest ranking; also, notice that among those with the highest rankings, they tend to have positive population growth, but there are also many other places with similar population growth rates with much lower rankings. Such remaining dispersion suggests that the recursive nature of the PageRank algorithm synthesizes more information from the full migration matrix _M_ , than the simple summation operation that computes the net migration alone. 

Figure 3: Geographic PageRank vs. Net Migration 



_Notes_ : The binscatter (top panel) and the scatter plot (bottom panel) show the relationship between Geographic PageRank and net migration. The y-axis represents the logarithm of the elements of the PageRank eigenvector, generated from IRS tax migration flow data in 2021. The x-axis is the county growth rates from 1-year ACS. In general, places that see population growth are ranked higher on average. However, there remains significant dispersion for the same level of net migration, and the average relationship is also nonlinear. 

In addition, when considering the long differences between rankings in 2001 and 2021, we regress changes in the underlying eigenvector on changes in log home prices at the MSA level. Table 5 shows that an increase in home price is associated with a _decline_ in the eigenvector, and correspondingly a _lowering_ of the ranking, consistent with the interpretation that growing housing costs can drive households away. Across the columns, when we restrict to the top 100 or 200 ranked MSAs, we see that changes in housing prices have greater predictive power as measured by R<sup>2</sup> . 

|Table 5:Estimationof LogHo|mePrice Change o<br>2001-20|nGeographicPage<br>21 Log Home Price|RankChange<br>Change|
|---|---|---|---|
||(1)|(2)|(3)|
||Full sample|Top 200|Top 100|
|PageRank Change, 2001-2021|-200.9162**|-285.2910***|-191.1490**|
||(89.1361)|(87.3845)|(88.7183)|
|Constant|0.7398***|0.7200***|0.7621***|
||(0.0107)|(0.0156)|(0.0221)|
|Observations<br>|461|200|100|
|R<sup>2</sup>|0.0109|0.0511|0.0452|



_Notes:_ This table shows the OLS regression of home price changes between 2001 and 2021 on the change in the Geographic PageRank, measured using the element of the eigenvector. Home price changes are based on the Zillow Home Value Index (ZHVI) from Zillow Research. The Geographic PageRank is computed using IRS migration data in 2001-2002 and 2021-2022. Each observation is - a CBSA. Columns represent different samples of CBSAs by their overall 2021 2022 ranking. 

Thus, GPR provides an easy-to-compute approach to characterize the relative desirability of places that are _inclusive_ of costs without the need to fully specify and estimate a model of household preferences and their weights. How to map the resulting ranking to a full structural model embedded in a spatial equilibrium is beyond the scope of this paper, and we leave it to future research. 

# **4.4 Ranking by Population Subgroups** 

Given the richness of household demographics available in the ACS data, we can also compute measures of Geographic PageRank that are based on certain types of migration flows. Specifically, we consider rankings based on different age groups, levels of education attained, household structure, race/ethnicity, housing tenure, and industry.<sup>8</sup> 

With the ACS data, as discussed before, we focus on rankings of metros. One computational issue to address is when ACS does not report a household’s metropolitan name one year ago because they did not live in an MSA, or because the migration PUMA is poorly matched to an MSA.<sup>9</sup> In this case, we do not drop such moves, as it would otherwise bias the result towards places that are more attractive to more urban households as opposed to rural households. Instead, all such households are considered to have moved from a “non-metro” category for each state. We make a similar adjustment when a household does not currently live in a metropolitan statistical area. These 51 extra “metros” are then kept during the PageRank algorithm when computing the ranking for all MSAs. To ensure such adjustment makes sense, we compare the MSA rankings using the ACS data with the ranking using the population-level IRS data, and make sure that they are indeed similar. 

Next, turning to the metro-level rankings by population subgroups, we re-run the algorithm based on moves among each of the population subgroups.<sup>10</sup> We describe our findings in greater detail below. 

8 Note that for the purpose of this analysis, we only have their information measured at the destination location from the ACS data. For demographics such as age, education, race/ethnicity, household structure, it is unlikely to matter whether they are measured at the origin or the destination location. However, for choice variables such as housing tenure or industry, we are limited in terms of our measurement at the destination. If such data is available at scale, an interesting and open question is to measure the combined ranking of industry-location pairs, such as a ranking between public-sector-in-Washington, DC and finance-in-New York, NY, which we leave to future research. 

9 See details of match error handling here: https://usa.ipums.org/usa-action/variables/MIGMET131. 10 For characteristics available at the individual level (e.g., age, education, race, ethnicity, and industry), we use individual-level migration; for characteristics at the household level (e.g., having 

Regarding Geographic PageRank by age groups, Figure 4 shows that the metro-level rankings are highly correlated across age groups (90%+), but they do become more different as the age differences grow. The rankings for 25-35 year-olds are 96% correlated with those from 35-65, but only 91% correlated with those who are 65 years or older. Table A.1 shows the top ranked metros by each age group. We note that New York-Newark-Jersey City, NY-NJ-PA is ranked at the very top for those aged 25 to 35, but is ranked lower for older age groups. On the other hand, Miami-Fort LauderdalePompano Beach, FL is ranked at number 5 for those older than 65, but is ranked lower for those from 35 to 65 (ranked at 11) and further lower for those from 25 to 35 (ranked 20). 

Figure 4: Correlation of Geographic PageRank by Age Groups, 2023 5-year ACS 



Source: American Community Survey (2023) 5-year estimates 

Regarding Geographic PageRank by levels of educational attainment, Figure 5 shows the correlation matrix for those without college, with some college, with a Bachelor’s degree, and with 

children), we use household-level migration. Alternatively, we could use the demographics of the head of households. The findings are substantively similar. 

an advanced degree. Again, the correlation is higher when education levels are more similar. Table A.2 shows that the top ranked metro for those with graduate degrees is Washington-ArlingtonAlexandria, DC-VA-MD-WV, followed by New York-Newark-Jersey City, NY-NJ-PA, both of which are ranked much lower for those without college degrees. 

Figure 5: Correlation of Geographic PageRank by Educational Attainment, 2023 5-year ACS 



Source: American Community Survey (2023) 5-year estimates 

Regarding Geographic PageRank by household structure, we separately rank metros for households with kids under 18 and those without kids under 18. Figure 6 shows the correlation and Table A.3 shows that New York-Newark-Jersey City, NY-NJ-PA, Seattle-Tacoma-Bellevue, WA, and Los Angeles-Long Beach-Anaheim, CA stand among the top 5 metros for those without kids under 18, but they fall out of the top 5 for those with kids under 18. 

Figure 6: Correlation of Geographic PageRank by Household Structure, 2023 5-year ACS 



Source: American Community Survey (2023) 5-year estimates 

Regarding Geographic PageRank by race and ethnicity, we notice that the correlations are markedly lower. Figure 7 shows that the correlation between the rankings for Whites and Blacks stands at 0.84, the correlation between Hispanics and Whites stands at 0.82, and the correlation between Blacks and Hispanics stands at 0.74. Table A.4 reveals that Atlanta-Sandy Springs-Alpharetta, GA ranks at the top based on moves of Blacks, but it is ranked at number 6 for Whites, and much lower at number 16 for Hispanics. On the other hand, San Antonio-New Braunfels, TX is ranked as the number 3 metro for Hispanics, but it is not even among the top 30 for Blacks or Whites; a similar pattern is true for Miami-Fort Lauderdale-Pompano Beach, FL as well. 

Figure 7: Correlation of Geographic PageRank by Race and Ethnicity, 2023 5-year ACS 



Source: American Community Survey (2023) 5-year estimates 

Regarding Geographic PageRank by housing tenure, Figure 8 reports the correlation and Table A.5 reports the ranking for owners and renters. Notably, metros such as Los Angeles-Long BeachAnaheim, CA and New York-Newark-Jersey City, NY-NJ-PA are ranked in the top 5 for renters, but are ranked much lower for owners. 

Figure 8: Correlation of Geographic PageRank by Housing Tenure, 2023 5-year ACS 



Source: American Community Survey (2023) 5-year estimates 

Lastly, regarding Geographic PageRank by industry, we produce ranks based on the NAICS code of the industry at the destination location. Figure 9 illustrates much greater variations in the correlation matrix. Certain industry groups such as natural resources (NAICS 11) have much lower correlation with rankings in other industry groups. We also report the detailed rankings for them in Table A.6, A.7, and A.8. Metros such as New York-Newark-Jersey City, NY-NJ-PA stand out as number 1 ranked for those in Information, finance, and real estate (NAICS 51-56), but not for other industries. 

Figure 9: Correlation of Geographic PageRank by Industry (2-digit NAICS), 2023 5-year ACS 



Source: American Community Survey (2023) 5-year estimates 

# **5 Application: Using GPR to Price Air Quality** 

In this section, we illustrate an application of Geographic PageRank, where the rankings can be used as a measure of unobserved housing quality to obtain sensible estimates of the price of air pollution. Methodologically, it uses the idea of an “anti-instrument” for housing quality as described in Bell, Billings, Calder-Wang and Zhong (2024), leveraging the ranking as an anti-IV to address the endogeneity from unobserved housing quality. 

Here, the key identifying assumption is (i) _relevance_ , namely, the candidate anti-IV is on average informative of the latent housing quality, and (ii) _conditional independence_ , namely, after conditioning on the latent housing quality, the anti-IV becomes independent of the focal amenity.<sup>11</sup> In our context, even though GPR may itself be correlated with the focal amenity unconditionally, as long as it satisfies conditional independence, it can still serve as a valid anti-IV. We demonstrate how it works in both the general nonlinear case and the more specific linear case. We show that the antiIV estimates not only solve the “wrong-signed” problems that are pervasive in the estimation of similar environmental amenities, but moreover, the estimates are in line with other existing reducedform estimates from natural experiments. 

# **5.1 Data** 

Our house price data comes from the Zillow Home Value Index (ZHVI), which reflects the typical value for homes in the 35th to 65th percentile range. We collect monthly ZHVI for single-family residences with 1, 2, 3, 4, and 5+ bedrooms at the county level and take the monthly average over the year. We use 2019 as our measurement year to avoid market movements and amenity value changes during the COVID period. For constructing Geographic PageRank, accordingly, we use the IRS county-to-county data from 2019. 

The main amenity data we use for our analysis is the Air Quality Index (AQI) from EPA’s Air Quality System, which is an aggregate measure of five pollutant levels. We collect daily county-level AQI data in 2019 from EPA Air Data and use the median across all days in the year. Since the AQI 

11 𝑐 <u>�Φ</u><sup>⊥P</sup> <u>�</u> = 𝑐 <u>�H</u><sup>⊥P</sup> <u>�</u> In a linear model, conditional independence is satisfied when , 𝑐 ) 𝑐 ) 𝑐𝑐 ,𝑍𝑍<sup>⊥𝑃𝑃</sup> 𝑐𝑐 ,𝑍𝑍<sup>⊥𝑃𝑃</sup> where H denotes the candidate anti-IV, P denotes price, Z denotes the focal amenity, and Φ denotes 𝑐𝑐(Φ<sup>⊥Z</sup> ,𝑃𝑃<sup>⊥𝑍𝑍</sup> 𝑐𝑐(H<sup>⊥Z</sup> ,𝑃𝑃<sup>⊥𝑍𝑍</sup> the latent housing quality. See Bell, Billings, Calder-Wang and Zhong (2024) for more details for the derivation. Code to implement the anti-IV estimator is available as a Stata package on GitHub at https://github. com/ZhongShusheng/aivreg_stata_package, or can be installed directly on Stata via _ssc install aivreg_ . 

data is only available for 1063 counties out of the total 3033 counties, we interpolate the AQI using the inverse distance weighting method commonly used in the economics literature on air pollution (Neidell 2004; Currie and Neidell 2005). For these counties, the interpolated AQI is calculated as the average of AQI readings from other counties weighted by the inverse of the squared distance between the counties. We complement our data with county-level socio-demographics (e.g., median household income) from the 2019 American Community Survey (ACS) 5-year data. 

# **5.2 Empirical Results** 

First, we show that we obtain an intuitively signed negative price for air pollution in the general setting without assuming linearity of the index mapping function, as shown in Figure 10. Specifically, the estimation procedure is as follows: we divide both price and amenities into quantiles, and in this case, we have divided them each into _N_ = 11 equally sized quantiles. Then, the Cartesian product of each price quantile and each air pollution quantile generates a total of _N_<sup>2</sup> cells. For each cell, we collect all households who belong to that cell and compute the average Geographic PageRank of members of the cell, which captures the predicted GPR conditional on price and amenity. 

The pattern in Figure 10 indicates a trade-off between home price and air quality. It shows a clear increase in the predicted Geographic PageRank in the diagonal direction: the best-ranked places (i.e. darker shades) are in the upper-right hand corner and the worst-ranked places (i.e. lighter shades) are in the bottom-left corner. As such, the upward-sloping line in Figure 10 indicates the direction of improving average PageRank, which corresponds to improving unobserved housing quality, whereas the perpendicular direction shows the “level sets”: the set of cells all with the same average PageRank, which corresponds to the same level of unobserved housing quality, but with varying combinations of price and amenity. In other words, the vector perpendicular to the direction of quality expansion shows the implied trade-off between home price and clean air: places with cleaner air are priced 

higher than places with more polluted air, conditioning on being in the same housing quality segment, 

which can now be adequately controlled for using the average Geographic PageRank. 

Figure 10: 3D Binscatter of Predicted PageRank by Price and Air Pollution 



_Notes_ : This figure categorizes the counties into 121 (11 _×_ 11) cells. Each cell represents counties that lie within a certain house price quantile and air pollution quantile. For example, the upper-right cell represents counties in the top price quantile and top air pollution quantile. The shade of each cell represents the median Geographic PageRank ranking of all counties in that cell. The PageRank algorithm ranks the most desirable place as number 1. Darker shades represent higher-ranked (i.e., more desirable) places and lighter shades represent lower-ranked (i.e., less desirable) places. Home prices are based on the Zillow Home Value Index (ZHVI) from Zillow Research. Median AQI data are from the US Environmental Protection Agency. The Geographic PageRank uses the 2019 nationwide version constructed using IRS migration inflow data. 

Next, if we adopt the lens of linearity, then we can use the “ratio-of-coefficients” estimator to obtain a single coefficient estimate of the amenity price. To visually benchmark the magnitude of our estimate in a linear model, Figure 11 compares the estimated price elasticity with known estimates in the literature, specifically, with Chay and Greenstone (2005). The shaded region indicates plausible point estimates of the housing price elasticity with respect to total suspended particulates (TSPs), which range from -0.20 to -0.35. The first two dots in Figure 11 show that conventional OLS with typical controls appears to generate wrong-signed and downward-biased estimates. 

The third dot shows that when PageRank is itself added as a control, while it does reduce the wrongsigned OLS estimate, it still remains positive. However, the last dot in Figure 11 shows a significantly negative elasticity of -.40 estimated by our anti-IV approach, and the confidence interval overlaps with the range of point estimates in Chay and Greenstone (2005). Though it should not necessarily be expected ex ante that they are the same given the nuances in how price is conceptualized, the fact that our estimate of the price of air pollution is indistinguishable from the range of estimates in the quasi-experimental literature lends some support to the credibility of our approach. Furthermore, future research could investigate the potential to apply Geographic PageRank as an anti-instrument to estimate the price of other housing amenities. 

Figure 11: Pricing Air Pollution Using Anti-IV Approach 



_Notes_ : The estimated coefficients in this figure correspond to the estimated price elasticity with respect to median AQI from regression results in Table 6. Home prices are based on the Zillow Home Value Index (ZHVI) from Zillow Research. Median AQI data are from the US Environmental Protection Agency. The Geographic PageRank uses the 2019 nationwide version constructed using IRS migration inflow data. 

|Ta|ble 6:Estimatio<br>OLS|nof HomePric<br>Inc|eElasticity toM<br>ome|edian AQI<br>Page|Rank|
|---|---|---|---|---|---|
||(1)|(2)|(3)|(4)|(5)|
|||Control|Anti-IV|Control|Anti-IV|
|Air Pollution|0.146***|0.0380***|-|0.0759***|-|
|(2019)|||0.0794***||0.406***|
||(0.0109)|(0.00841)|(0.0121)|(0.0124)|(0.0550)|
|HH<br>Median<br>||1.380***|2.882***|||
|Income||||||
|||(0.0344)|(0.0710)|||
|PageRank||||0.210***|1.661***|
|||||(0.0162)|(0.143)|
|Constant|11.59***|-3.809***|-<br>20.57***|13.26***|24.75***|
||(0.0213)|(0.384)|(0.790)|(0.124)|(1.164)|
|Room<br>Fixed|Y|Y|Y|Y|Y|
|Effects||||||
|Observations|8322|8322|8322|8322|8322|
|AdjustedR<sup>2</sup>|0.410|0.692||0.485||



_Notes_ : This table shows the estimated price elasticity of the median Air Quality Index (AQI) at the county level in 2019. Home prices are based on the Zillow Home Value Index (ZHVI) from Zillow Research. Median AQI data are from the US Environmental Protection Agency. Column 1 shows the OLS result from regressing the house price index on median AQI. Columns 2 and 4 regress the house price index, controlling for household median income and Geographic PageRank, respectively. Columns 3 and 5 apply the anti-IV method, using household median income and Geographic PageRank as the anti-IV, respectively. The Geographic PageRank uses the 2019 nationwide version constructed using IRS migration inflow data, and the household median income comes from the ACS. Standard errors are clustered at the county level. 

# **6 Conclusion** 

This paper introduces Geographic PageRank (GPR) as a novel, network-based measure of place quality, leveraging migration flows to capture locational desirability. By adapting the recursive logic of the PageRank algorithm, GPR synthesizes information from the full migration network, providing a more robust measure of housing quality than conventional approaches based on net migration or hedonic regressions. 

Since GPR can be measured at multiple geographic scales, this flexibility makes it particularly valuable for applications in urban and environmental economics, where housing quality and amenity values vary at a highly localized level. In this paper, we also show how GPR could be used as an antiinstrument (Bell, Billings, Calder-Wang and Zhong 2024), offering an effective strategy to address endogeneity issues in pricing housing and neighborhood amenities when housing quality is unobserved. 

Because GPR produces a single ranking of all places based on realized migration choices, it inherently captures factors such as housing prices, labor market conditions, amenities, and changing preferences in a model-free way. We leave it to future research ways to potentially micro-found the measure, or to incorporate GPR into other common models of residential and migration choices (Bayer et al. 2016; Kennan and Walker 2011) and other measures of housing market constraints (Glaeser and Gyourko 2018; Gyourko, Hartley and Krimmel 2021; Baum-Snow and Duranton 2025). 

We expect the use cases for Geographic PageRank to be broad, ranging from descriptive statistics to capture changes in urban dynamics to analyses that unpack factors affecting the growth or decline of places, and potentially many more. We have made the rankings readily available for visualization and download.<sup>12</sup> Overall, as migration patterns continue to evolve, tools like Geographic PageRank can offer valuable insights into urban dynamics, housing markets, and spatial inequality. 

12 To download, go to Geographic Pagerank at https://sophieqzwang.github.io/geopagerank/. 

# **References** 

**Bagger, Jesper, and Rasmus Lentz.** 2019. “An Empirical Model of Wage Dispersion with Sorting.” 

_The Review of Economic Studies_ , 86 (1): 153–190. 

**Baum-Snow, Nathaniel, and Gilles Duranton.** 2025. “Housing Supply and Housing Affordability.” 

**Bayer, Patrick, Robert McMillan, Alvin Murphy, and Christopher Timmins.** 2016. “A Dynamic 

Model of Demand for Houses and Neighborhoods.” _Econometrica_ , 84 (3): 893–942. 

**Bell, Alex.** 2020. “Job Amenities and Earnings Inequality,” _Working Paper_ . 

**Bell, Alex.** 2025. “Pricing Job Amenities: A Practitioner’s Manual,” _Working Paper._ 

**Bell, Alex, Stephen B. Billings, Sophie Calder-Wang, and Shusheng Zhong.** 2024. “An Anti-IV Approach for Pricing Residential Amenities: Applications to Flood Risk,” _Working Paper._ 

**Berkhin, Pavel.** 2005. “A Survey on PageRank Computing.” _Internet Mathematics_ , 2 (1): 73–120. 

**Chay, Kenneth Y., and Michael Greenstone.** 2005. “Does Air Quality Matter? Evidence from the Housing Market.” _Journal of Political Economy_ , 113 (2): 376–424. Publisher: The University of Chicago Press. 

**Currie, Janet, and Matthew Neidell.** 2005. “Air Pollution and Infant Health: What Can We Learn from California’s Recent Experience?*.” _The Quarterly Journal of Economics_ , 120 (3): 1003–1030. **Epple, Dennis, Luis Quintero, and Holger Sieg.** 2020. “A New Approach to Estimating Equilibrium Models for Metropolitan Housing Markets.” _Journal of Political Economy_ , 128 (3): 948–983. Publisher: The University of Chicago Press. 

**Fogel, Jamie.** 2021. “Valuing American Cities: A Revealed Preference Approach.” 

**Glaeser, Edward, and Joseph Gyourko.** 2018. “The Economic Implications of Housing Supply.” _Journal of Economic Perspectives_ , 32 (1): 3–30. 

**Gleich, David F.** 2015. “PageRank Beyond the Web.” _SIAM Review_ , 57 (3): 321–363. 

**Gyourko, Joseph, Jonathan S. Hartley, and Jacob Krimmel.** 2021. “The Local Residential Land 

Use Regulatory Environment across U.S. Housing Markets: Evidence from a New Wharton Index.” _Journal of Urban Economics_ , 124: 103337. 

**Kennan, John, and James R. Walker.** 2011. “The Effect of Expected Income on Individual Migration Decisions.” _Econometrica_ , 79 (1): 211–251. 

**Landvoigt, Tim, Monika Piazzesi, and Martin Schneider.** 2014. “Housing Assignment with Restrictions: Theory and Evidence from Stanford University’s Campus.” _American Economic Review_ , 104 (5): 67–72. 

**Landvoigt, Tim, Monika Piazzesi, and Martin Schneider.** 2015. “The Housing Market(s) of San Diego.” _American Economic Review_ , 105 (4): 1371–1407. 

**Mast, Evan.** 2025. “Off the Beaten Tract: Constructing a New Neighborhood Geography from Migration Data.” 

**Morchio, Iacopo, and Christian Moser.** 2020. “The Gender Pay Gap: Micro Sources and Macro Consequences.” Social Science Research Network SSRN Scholarly Paper ID 3176868, Rochester, NY. 

**Neidell, Matthew J.** 2004. “Air pollution, health, and socio-economic status: the effect of outdoor 

air quality on childhood asthma.” _Journal of Health Economics_ , 23 (6): 1209–1236. 

**Page, Lawrence.** 2001. “Method for node ranking in a linked database.” 

**Sorkin, Isaac.** 2018. “Ranking Firms Using Revealed Preference*.” _The Quarterly Journal of Economics_ , 133 (3): 1331–1393. 

**Taber, Christopher, and Rune Vejlin.** 2020. “Estimation of a Roy/Search/Compensating Differential Model of the Labor Market.” _Econometrica_ , 88(3): 1031–1069. 

# **Appendix Tables** 

# Table A.1: Top 30 Ranked Metros by Age Groups, 2023 5-year ACS 

|Rank|Age 25–35|Age 35–65|Age 65+|
|---|---|---|---|
|1|New York-Newark-Jersey City, NY-NJ-PA|Dallas-Fort Worth-Arlington, TX|Phoenix-Mesa-Chandler, AZ|
|2|Dallas-Fort Worth-Arlington, TX|Atlanta-Sandy Springs-Alpharetta, GA|Dallas-Fort Worth-Arlington, TX|
|3|Chicago-Naperville-Elgin, IL-IN-WI|Houston-The Woodlands-Sugar Land, TX|Atlanta-Sandy Springs-Alpharetta, GA|
|4|Houston-The Woodlands-Sugar Land, TX|Phoenix-Mesa-Chandler, AZ|Houston-The Woodlands-Sugar Land, TX|
|5|Los Angeles-Long Beach-Anaheim, CA|Washington-Arlington-Alexandria, DC-VA-MD-WV|Tampa-St. Petersburg-Clearwater, FL|
|6|Atlanta-Sandy Springs-Alpharetta, GA|Tampa-St. Petersburg-Clearwater, FL|Miami-Fort Lauderdale-Pompano Beach, FL|
|7|Washington-Arlington-Alexandria, DC-VA-MD-WV|New York-Newark-Jersey City, NY-NJ-PA|New York-Newark-Jersey City, NY-NJ-PA|
|8|Seattle-Tacoma-Bellevue, WA|Charlotte-Concord-Gastonia, NC-SC|Washington-Arlington-Alexandria, DC-VA-MD-WV|
|9|Phoenix-Mesa-Chandler, AZ|Chicago-Naperville-Elgin, IL-IN-WI|Chicago-Naperville-Elgin, IL-IN-WI|
|10|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Los Angeles-Long Beach-Anaheim, CA|Boston-Cambridge-Newton, MA-NH|
|11|Denver-Aurora-Lakewood, CO|Miami-Fort Lauderdale-Pompano Beach, FL|Charlotte-Concord-Gastonia, NC-SC|
|12|Boston-Cambridge-Newton, MA-NH|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|North Port-Sarasota-Bradenton, FL|
|13|Charlotte-Concord-Gastonia, NC-SC|Boston-Cambridge-Newton, MA-NH|Los Angeles-Long Beach-Anaheim, CA|
|14|Austin-Round Rock-Georgetown, TX|Las Vegas-Henderson-Paradise, NV|Detroit-Warren-Dearborn, MI|
|15|San Francisco-Oakland-Berkeley, CA|Seattle-Tacoma-Bellevue, WA|Portland-Vancouver-Hillsboro, OR-WA|
|16|Minneapolis-St. Paul-Bloomington, MN-WI|Denver-Aurora-Lakewood, CO|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|
|17|Portland-Vancouver-Hillsboro, OR-WA|Detroit-Warren-Dearborn, MI|Seattle-Tacoma-Bellevue, WA|
|18|Tampa-St. Petersburg-Clearwater, FL|Orlando-Kissimmee-Sanford, FL|Las Vegas-Henderson-Paradise, NV|
|19|Kansas City, MO-KS|Nashville-Davidson–Murfreesboro–Franklin, TN|Kansas City, MO-KS|
|20|Miami-Fort Lauderdale-Pompano Beach, FL|Kansas City, MO-KS|Riverside-San Bernardino-Ontario, CA|
|21|Nashville-Davidson–Murfreesboro–Franklin, TN|Austin-Round Rock-Georgetown, TX|Greenville-Anderson, SC|
|22|Detroit-Warren-Dearborn, MI|San Antonio-New Braunfels, TX|Minneapolis-St. Paul-Bloomington, MN-WI|
|23|San Diego-Chula Vista-Carlsbad, CA|Portland-Vancouver-Hillsboro, OR-WA|Denver-Aurora-Lakewood, CO|
|24|San Antonio-New Braunfels, TX|Indianapolis-Carmel-Anderson, IN|San Antonio-New Braunfels, TX|
|25|Orlando-Kissimmee-Sanford, FL|Riverside-San Bernardino-Ontario, CA|St. Louis, MO-IL|
|26|St. Louis, MO-IL|Greenville-Anderson, SC|Austin-Round Rock-Georgetown, TX|
|27|Las Vegas-Henderson-Paradise, NV|Jacksonville, FL|Nashville-Davidson–Murfreesboro–Franklin, TN|
|28|Indianapolis-Carmel-Anderson, IN|St. Louis, MO-IL|Cape Coral-Fort Myers, FL|
|29|Columbus, OH|Minneapolis-St. Paul-Bloomington, MN-WI|Orlando-Kissimmee-Sanford, FL|
|30|Riverside-San Bernardino-Ontario, CA|Oklahoma City, OK|San Francisco-Oakland-Berkeley, CA|



_Notes_ : Geographic PageRanks are computed from American Community Survey (2023) 5-year estimates. 

Table A.2: Top 30 Ranked Metros by Education Attainment, 2023 5-year ACS 

|Rank|No college|Some college|Bachelor’s|Graduate|
|---|---|---|---|---|
|1|Dallas-Fort Worth-Arlington, TX|Phoenix-Mesa-Chandler, AZ|New York-Newark-Jersey City, NY-NJ-PA|Washington-Arlington-Alexandria, DC-VA-MD-<br>W|
|2|Houston-The Woodlands-Sugar Land, TX|Dallas-Fort Worth-Arlington, TX|Dallas-Fort Worth-Arlington, TX|New York-Newark-Jersey City, NY-NJ-PA|
|3|Atlanta-Sandy Springs-Alpharetta, GA|Atlanta-Sandy Springs-Alpharetta, GA|Chicago-Naperville-Elgin, IL-IN-WI|Atlanta-Sandy Springs-Alpharetta, GA|
|4|Phoenix-Mesa-Chandler, AZ|Houston-The Woodlands-Sugar Land, TX|Atlanta-Sandy Springs-Alpharetta, GA|Dallas-Fort Worth-Arlington, TX|
|5|Chicago-Naperville-Elgin, IL-IN-WI|<br>Los Angeles-Long Beach-Anaheim, CA|<br>Los Angeles-Long Beach-Anaheim, CA|<br>Chicago-Naperville-Elgin, IL-IN-WI|
|6|New York-Newark-Jersey City, NY-NJ-PA|New York-Newark-Jersey City, NY-NJ-PA|Washington-Arlington-Alexandria, DC-VA-MD-WV|Houston-The Woodlands-Sugar Land, TX|
|7|Charlotte-Concord-Gastonia, NC-SC|Washington-Arlington-Alexandria, DC-VA-MD-WV|Houston-The Woodlands-Sugar Land, TX|Los Angeles-Long Beach-Anaheim, CA|
|8|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Tampa-St. Petersburg-Clearwater, FL|Denver-Aurora-Lakewood, CO|Seattle-Tacoma-Bellevue, WA|
|9|Washington-Arlington-Alexandria, DC-VA-MD-WV|Chicago-Naperville-Elgin, IL-IN-WI|Phoenix-Mesa-Chandler, AZ|Boston-Cambridge-Newton, MA-NH|
|10|Boston-Cambridge-Newton, MA-NH|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Seattle-Tacoma-Bellevue, WA|San Francisco-Oakland-Berkeley, CA|
|11|Los Angeles-Long Beach-Anaheim, CA|Charlotte-Concord-Gastonia, NC-SC|Boston-Cambridge-Newton, MA-NH|Philadelphia-Camden-Wilmington,<br>PA-NJ-DE<br>MD|
|12|Tampa-St. Petersburg-Clearwater, FL|Seattle-Tacoma-Bellevue, WA|Charlotte-Concord-Gastonia, NC-SC|Phoenix-Mesa-Chandler, AZ|
|13|San Antonio-New Braunfels, TX|Boston-Cambridge-Newton, MA-NH|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Denver-Aurora-Lakewood, CO|
|14|Seattle-Tacoma-Bellevue, WA|Orlando-Kissimmee-Sanford, FL|Austin-Round Rock-Georgetown, TX|Miami-Fort Lauderdale-Pompano Beach, FL|
|15|Miami-Fort Lauderdale-Pompano Beach, FL|Austin-Round Rock-Georgetown, TX|Tampa-St. Petersburg-Clearwater, FL|Charlotte-Concord-Gastonia, NC-SC|
|16|Las Vegas-Henderson-Paradise, NV|Miami-Fort Lauderdale-Pompano Beach, FL|San Francisco-Oakland-Berkeley, CA|Austin-Round Rock-Georgetown, TX|
|17|Kansas City, MO-KS|San Antonio-New Braunfels, TX|Nashville-Davidson–Murfreesboro–Franklin, TN|Minneapolis-St. Paul-Bloomington, MN-WI|
|18|Detroit-Warren-Dearborn, MI|Denver-Aurora-Lakewood, CO|Portland-Vancouver-Hillsboro, OR-WA|Tampa-St. Petersburg-Clearwater, FL|
|19|Nashville-Davidson–Murfreesboro–Franklin, TN|Portland-Vancouver-Hillsboro, OR-WA|Miami-Fort Lauderdale-Pompano Beach, FL|Portland-Vancouver-Hillsboro, OR-WA|
|20|Riverside-San Bernardino-Ontario, CA|Nashville-Davidson–Murfreesboro–Franklin, TN|Kansas City, MO-KS|San Diego-Chula Vista-Carlsbad, CA|
|21|St. Louis, MO-IL|Detroit-Warren-Dearborn, MI|Minneapolis-St. Paul-Bloomington, MN-WI|Kansas City, MO-KS|
|22|Orlando-Kissimmee-Sanford, FL|Kansas City, MO-KS|San Diego-Chula Vista-Carlsbad, CA|San Jose-Sunnyvale-Santa Clara, CA|
|23|Denver-Aurora-Lakewood, CO|Las Vegas-Henderson-Paradise, NV|Orlando-Kissimmee-Sanford, FL|Nashville-Davidson–Murfreesboro–Franklin, TN|
|24|Austin-Round Rock-Georgetown, TX|<br>Oklahoma City, OK|San Antonio-New Braunfels, TX|Detroit-Warren-Dearborn, MI|
|25|<br>Indianapolis-Carmel-Anderson, IN|<br>Virginia Beach-Norfolk-Newport News, VA-NC|<br>Detroit-Warren-Dearborn, MI|<br>Raleigh-Cary, NC|
|26|<br>Oklahoma City, OK|<br>St. Louis, MO-IL|<br>Indianapolis-Carmel-Anderson, IN|<br>Las Vegas-Henderson-Paradise, NV|
|27|<br>Virginia Beach-Norfolk-Newport News, VA-NC|Columbus, OH|<br>Las Vegas-Henderson-Paradise, NV|<br>Orlando-Kissimmee-Sanford, FL|
|28|Greenville-Anderson, SC|San Diego-Chula Vista-Carlsbad, CA|St. Louis, MO-IL|Baltimore-Columbia-Towson, MD|
|29|Columbus, OH|Sacramento-Roseville-Folsom, CA|Baltimore-Columbia-Towson, MD|St. Louis, MO-IL|
|30|Minneapolis-St. Paul-Bloomington,MN-WI|Minneapolis-St. Paul-Bloomington,MN-WI|Raleigh-Cary,NC|Columbus,OH|



_Notes_ : Geographic PageRanks are computed from American Community Survey (2023) 5-year estimates. 

Table A.3: Top 30 Ranked Metros by Household Structure, 2023 5-year ACS 

|Rank|Has kid (_<_18)|No kid|
|---|---|---|
|1|Houston-The Woodlands-Sugar Land, TX|New York-Newark-Jersey City, NY-NJ-PA|
|2|Dallas-Fort Worth-Arlington, TX|Dallas-Fort Worth-Arlington, TX|
|3|Atlanta-Sandy Springs-Alpharetta, GA|Seattle-Tacoma-Bellevue, WA|
|4|Chicago-Naperville-Elgin, IL-IN-WI|Los Angeles-Long Beach-Anaheim, CA|
|5|Phoenix-Mesa-Chandler, AZ|Houston-The Woodlands-Sugar Land, TX|
|6|Washington-Arlington-Alexandria, DC-VA-MD-WV|Washington-Arlington-Alexandria, DC-VA-MD-WV|
|7|New York-Newark-Jersey City, NY-NJ-PA|Atlanta-Sandy Springs-Alpharetta, GA|
|8|Charlotte-Concord-Gastonia, NC-SC|Chicago-Naperville-Elgin, IL-IN-WI|
|9|Seattle-Tacoma-Bellevue, WA|Phoenix-Mesa-Chandler, AZ|
|10|Boston-Cambridge-Newton, MA-NH|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|
|11|Los Angeles-Long Beach-Anaheim, CA|Boston-Cambridge-Newton, MA-NH|
|12|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Austin-Round Rock-Georgetown, TX|
|13|Tampa-St. Petersburg-Clearwater, FL|Charlotte-Concord-Gastonia, NC-SC|
|14|San Antonio-New Braunfels, TX|Denver-Aurora-Lakewood, CO|
|15|St. Louis, MO-IL|Nashville-Davidson–Murfreesboro–Franklin, TN|
|16|Kansas City, MO-KS|Portland-Vancouver-Hillsboro, OR-WA|
|17|Detroit-Warren-Dearborn, MI|Tampa-St. Petersburg-Clearwater, FL|
|18|Austin-Round Rock-Georgetown, TX|Miami-Fort Lauderdale-Pompano Beach, FL|
|19|Las Vegas-Henderson-Paradise, NV|San Francisco-Oakland-Berkeley, CA|
|20|Denver-Aurora-Lakewood, CO|Kansas City, MO-KS|
|21|Minneapolis-St. Paul-Bloomington, MN-WI|San Antonio-New Braunfels, TX|
|22|Nashville-Davidson–Murfreesboro–Franklin, TN|Minneapolis-St. Paul-Bloomington, MN-WI|
|23|Portland-Vancouver-Hillsboro, OR-WA|Virginia Beach-Norfolk-Newport News, VA-NC|
|24|Miami-Fort Lauderdale-Pompano Beach, FL|Detroit-Warren-Dearborn, MI|
|25|Virginia Beach-Norfolk-Newport News, VA-NC|San Diego-Chula Vista-Carlsbad, CA|
|26|Orlando-Kissimmee-Sanford, FL|St. Louis, MO-IL|
|27|Indianapolis-Carmel-Anderson, IN|Columbus, OH|
|28|Riverside-San Bernardino-Ontario, CA|Cincinnati, OH-KY-IN|
|29|Oklahoma City, OK|Orlando-Kissimmee-Sanford, FL|
|30|Baltimore-Columbia-Towson, MD|Oklahoma City, OK|



_Notes_ : Geographic PageRanks are computed from American Community Survey (2023) 5-year estimates. 

Table A.4: Top 30 Ranked Metros by Race and Ethnicity, 2023 5-year ACS 

|Rank|White|Black|Hispanic|
|---|---|---|---|
|1|Dallas-Fort Worth-Arlington, TX|Atlanta-Sandy Springs-Alpharetta, GA|Houston-The Woodlands-Sugar Land, TX|
|2|New York-Newark-Jersey City, NY-NJ-PA|Houston-The Woodlands-Sugar Land, TX|Dallas-Fort Worth-Arlington, TX|
|3|Phoenix-Mesa-Chandler, AZ|Dallas-Fort Worth-Arlington, TX|San Antonio-New Braunfels, TX|
|4|Chicago-Naperville-Elgin, IL-IN-WI|Washington-Arlington-Alexandria, DC-VA-MD-WV|Phoenix-Mesa-Chandler, AZ|
|5|Boston-Cambridge-Newton, MA-NH|Chicago-Naperville-Elgin, IL-IN-WI|New York-Newark-Jersey City, NY-NJ-PA|
|6|Atlanta-Sandy Springs-Alpharetta, GA|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Miami-Fort Lauderdale-Pompano Beach, FL|
|7|Washington-Arlington-Alexandria, DC-VA-MD-WV|New York-Newark-Jersey City, NY-NJ-PA|Chicago-Naperville-Elgin, IL-IN-WI|
|8|Tampa-St. Petersburg-Clearwater, FL|Charlotte-Concord-Gastonia, NC-SC|Los Angeles-Long Beach-Anaheim, CA|
|9|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Phoenix-Mesa-Chandler, AZ|Austin-Round Rock-Georgetown, TX|
|10|Charlotte-Concord-Gastonia, NC-SC|Detroit-Warren-Dearborn, MI|Washington-Arlington-Alexandria, DC-VA-MD-WV|
|11|Houston-The Woodlands-Sugar Land, TX|Los Angeles-Long Beach-Anaheim, CA|Denver-Aurora-Lakewood, CO|
|12|Denver-Aurora-Lakewood, CO|Virginia Beach-Norfolk-Newport News, VA-NC|Tampa-St. Petersburg-Clearwater, FL|
|13|Seattle-Tacoma-Bellevue, WA|Las Vegas-Henderson-Paradise, NV|San Diego-Chula Vista-Carlsbad, CA|
|14|Los Angeles-Long Beach-Anaheim, CA|Seattle-Tacoma-Bellevue, WA|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|
|15|Nashville-Davidson–Murfreesboro–Franklin, TN|Miami-Fort Lauderdale-Pompano Beach, FL|Riverside-San Bernardino-Ontario, CA|
|16|Kansas City, MO-KS|St. Louis, MO-IL|Atlanta-Sandy Springs-Alpharetta, GA|
|17|Portland-Vancouver-Hillsboro, OR-WA|Baltimore-Columbia-Towson, MD|Orlando-Kissimmee-Sanford, FL|
|18|Austin-Round Rock-Georgetown, TX|Minneapolis-St. Paul-Bloomington, MN-WI|Las Vegas-Henderson-Paradise, NV|
|19|Minneapolis-St. Paul-Bloomington, MN-WI|Kansas City, MO-KS|Oklahoma City, OK|
|20|St. Louis, MO-IL|Indianapolis-Carmel-Anderson, IN|Boston-Cambridge-Newton, MA-NH|
|21|Detroit-Warren-Dearborn, MI|Nashville-Davidson–Murfreesboro–Franklin, TN|Seattle-Tacoma-Bellevue, WA|
|22|Cincinnati, OH-KY-IN|Columbus, OH|Charlotte-Concord-Gastonia, NC-SC|
|23|Greenville-Anderson, SC|Memphis, TN-MS-AR|Kansas City, MO-KS|
|24|Oklahoma City, OK|Boston-Cambridge-Newton, MA-NH|Tucson, AZ|
|25|Indianapolis-Carmel-Anderson, IN|Portland-Vancouver-Hillsboro, OR-WA|Detroit-Warren-Dearborn, MI|
|26|Orlando-Kissimmee-Sanford, FL|Orlando-Kissimmee-Sanford, FL|Greenville-Anderson, SC|
|27|Pittsburgh, PA|Riverside-San Bernardino-Ontario, CA|El Paso, TX|
|28|Columbus, OH|Birmingham-Hoover, AL|Nashville-Davidson–Murfreesboro–Franklin, TN|
|29|Miami-Fort Lauderdale-Pompano Beach, FL|San Francisco-Oakland-Berkeley, CA|Portland-Vancouver-Hillsboro, OR-WA|
|30|San Diego-Chula Vista-Carlsbad, CA|Richmond, VA|Minneapolis-St. Paul-Bloomington, MN-WI|



_Notes_ : Geographic PageRanks are computed from American Community Survey (2023) 5-year estimates. 

Table A.5: Top 30 Ranked Metros by Housing Tenure, 2023 5-year ACS 

|Rank|Owner|Renter|
|---|---|---|
|1|Atlanta-Sandy Springs-Alpharetta, GA|Dallas-Fort Worth-Arlington, TX|
|2|Dallas-Fort Worth-Arlington, TX|Los Angeles-Long Beach-Anaheim, CA|
|3|Houston-The Woodlands-Sugar Land, TX|Houston-The Woodlands-Sugar Land, TX|
|4|Phoenix-Mesa-Chandler, AZ|New York-Newark-Jersey City, NY-NJ-PA|
|5|Chicago-Naperville-Elgin, IL-IN-WI|Atlanta-Sandy Springs-Alpharetta, GA|
|6|Washington-Arlington-Alexandria, DC-VA-MD-WV|Chicago-Naperville-Elgin, IL-IN-WI|
|7|Charlotte-Concord-Gastonia, NC-SC|Washington-Arlington-Alexandria, DC-VA-MD-WV|
|8|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Seattle-Tacoma-Bellevue, WA|
|9|New York-Newark-Jersey City, NY-NJ-PA|Phoenix-Mesa-Chandler, AZ|
|10|Tampa-St. Petersburg-Clearwater, FL|Denver-Aurora-Lakewood, CO|
|11|Detroit-Warren-Dearborn, MI|Boston-Cambridge-Newton, MA-NH|
|12|Boston-Cambridge-Newton, MA-NH|Charlotte-Concord-Gastonia, NC-SC|
|13|St. Louis, MO-IL|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|
|14|San Antonio-New Braunfels, TX|Austin-Round Rock-Georgetown, TX|
|15|Kansas City, MO-KS|Tampa-St. Petersburg-Clearwater, FL|
|16|Miami-Fort Lauderdale-Pompano Beach, FL|San Francisco-Oakland-Berkeley, CA|
|17|Denver-Aurora-Lakewood, CO|Miami-Fort Lauderdale-Pompano Beach, FL|
|18|Riverside-San Bernardino-Ontario, CA|Las Vegas-Henderson-Paradise, NV|
|19|Nashville-Davidson–Murfreesboro–Franklin, TN|Nashville-Davidson–Murfreesboro–Franklin, TN|
|20|Minneapolis-St. Paul-Bloomington, MN-WI|Portland-Vancouver-Hillsboro, OR-WA|
|21|Seattle-Tacoma-Bellevue, WA|Kansas City, MO-KS|
|22|Los Angeles-Long Beach-Anaheim, CA|Orlando-Kissimmee-Sanford, FL|
|23|Indianapolis-Carmel-Anderson, IN|San Antonio-New Braunfels, TX|
|24|Greenville-Anderson, SC|San Diego-Chula Vista-Carlsbad, CA|
|25|Orlando-Kissimmee-Sanford, FL|Minneapolis-St. Paul-Bloomington, MN-WI|
|26|Austin-Round Rock-Georgetown, TX|Oklahoma City, OK|
|27|Las Vegas-Henderson-Paradise, NV|Columbus, OH|
|28|Jacksonville, FL|Detroit-Warren-Dearborn, MI|
|29|Portland-Vancouver-Hillsboro, OR-WA|Indianapolis-Carmel-Anderson, IN|
|30|Cincinnati, OH-KY-IN|Sacramento-Roseville-Folsom, CA|



_Notes_ : Geographic PageRanks are computed from American Community Survey (2023) 5-year estimates. 

Table A.6: Top 30 Ranked Metros by Industry <u>(Part 1 of 3), 2023 5-year ACS</u> 

|Rank|Natural resources (NAICS 11)|Mining, utilities, construction (NAICS 21–23)|Manufacturing (NAICS 31–33)|
|---|---|---|---|
|1|Charlotte-Concord-Gastonia, NC-SC|Houston-The Woodlands-Sugar Land, TX|Dallas-Fort Worth-Arlington, TX|
|2|Spartanburg, SC|Charlotte-Concord-Gastonia, NC-SC|Atlanta-Sandy Springs-Alpharetta, GA|
|3|Miami-Fort Lauderdale-Pompano Beach, FL|Dallas-Fort Worth-Arlington, TX|Chicago-Naperville-Elgin, IL-IN-WI|
|4|Gulfport-Biloxi, MS|Phoenix-Mesa-Chandler, AZ|Houston-The Woodlands-Sugar Land, TX|
|5|Greenville-Anderson, SC|Atlanta-Sandy Springs-Alpharetta, GA|Phoenix-Mesa-Chandler, AZ|
|6|Portland-Vancouver-Hillsboro, OR-WA|Denver-Aurora-Lakewood, CO|Los Angeles-Long Beach-Anaheim, CA|
|7|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Tampa-St. Petersburg-Clearwater, FL|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|
|8|State College, PA|Miami-Fort Lauderdale-Pompano Beach, FL|Charlotte-Concord-Gastonia, NC-SC|
|9|Toledo, OH|Chicago-Naperville-Elgin, IL-IN-WI|Detroit-Warren-Dearborn, MI|
|10|Jackson, TN|Washington-Arlington-Alexandria, DC-VA-MD-WV|Seattle-Tacoma-Bellevue, WA|
|11|Sheboygan, WI|Los Angeles-Long Beach-Anaheim, CA|Minneapolis-St. Paul-Bloomington, MN-WI|
|12|Los Angeles-Long Beach-Anaheim, CA|Seattle-Tacoma-Bellevue, WA|Portland-Vancouver-Hillsboro, OR-WA|
|13|Lubbock, TX|New York-Newark-Jersey City, NY-NJ-PA|Boston-Cambridge-Newton, MA-NH|
|14|Gainesville, GA|Nashville-Davidson–Murfreesboro–Franklin, TN|New York-Newark-Jersey City, NY-NJ-PA|
|15|Seattle-Tacoma-Bellevue, WA|Orlando-Kissimmee-Sanford, FL|Kansas City, MO-KS|
|16|Tampa-St. Petersburg-Clearwater, FL|Minneapolis-St. Paul-Bloomington, MN-WI|Denver-Aurora-Lakewood, CO|
|17|Phoenix-Mesa-Chandler, AZ|Boston-Cambridge-Newton, MA-NH|Greenville-Anderson, SC|
|18|Lakeland-Winter Haven, FL|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|San Jose-Sunnyvale-Santa Clara, CA|
|19|Dallas-Fort Worth-Arlington, TX|Greenville-Anderson, SC|St. Louis, MO-IL|
|20|Bakersfield, CA|Austin-Round Rock-Georgetown, TX|Cincinnati, OH-KY-IN|
|21|Yuma, AZ|Kansas City, MO-KS|Austin-Round Rock-Georgetown, TX|
|22|Nashville-Davidson–Murfreesboro–Franklin, TN|Indianapolis-Carmel-Anderson, IN|San Francisco-Oakland-Berkeley, CA|
|23|Greensboro-High Point, NC|Portland-Vancouver-Hillsboro, OR-WA|Nashville-Davidson–Murfreesboro–Franklin, TN|
|24|Washington-Arlington-Alexandria, DC-VA-MD-WV|San Antonio-New Braunfels, TX|Milwaukee-Waukesha, WI|
|25|Oklahoma City, OK|Detroit-Warren-Dearborn, MI|Tampa-St. Petersburg-Clearwater, FL|
|26|New York-Newark-Jersey City, NY-NJ-PA|Las Vegas-Henderson-Paradise, NV|Cleveland-Elyria, OH|
|27|Fresno, CA|Columbus, OH|Riverside-San Bernardino-Ontario, CA|
|28|Visalia, CA|St. Louis, MO-IL|Columbus, OH|
|29|Salinas, CA|Oklahoma City, OK|Birmingham-Hoover, AL|
|30|Atlanta-SandySprings-Alpharetta, GA|North Port-Sarasota-Bradenton, FL|Washington-Arlington-Alexandria, DC-VA-MD-WV|



_Notes_ : Geographic PageRanks are computed from American Community Survey (2023) 5-year estimates. 

Table A.7: Top 30 Ranked Metros by Industry <u>(Part 2 of 3), 2023 5-year ACS</u> 

|Rank|Wholesale, retail, transport, warehousing (NAICS 42–49)|Information, finance, real estate, admin (NAICS 51–56)|Education & health (NAICS 61–62)|
|---|---|---|---|
|1|Dallas-Fort Worth-Arlington, TX|New York-Newark-Jersey City, NY-NJ-PA|New York-Newark-Jersey City, NY-NJ-PA|
|2|Atlanta-Sandy Springs-Alpharetta, GA|Dallas-Fort Worth-Arlington, TX|Houston-The Woodlands-Sugar Land, TX|
|3|Houston-The Woodlands-Sugar Land, TX|Atlanta-Sandy Springs-Alpharetta, GA|Dallas-Fort Worth-Arlington, TX|
|4|Phoenix-Mesa-Chandler, AZ|Washington-Arlington-Alexandria, DC-VA-MD-WV|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|
|5|Chicago-Naperville-Elgin, IL-IN-WI|Los Angeles-Long Beach-Anaheim, CA|Atlanta-Sandy Springs-Alpharetta, GA|
|6|Seattle-Tacoma-Bellevue, WA|Chicago-Naperville-Elgin, IL-IN-WI|Boston-Cambridge-Newton, MA-NH|
|7|New York-Newark-Jersey City, NY-NJ-PA|Phoenix-Mesa-Chandler, AZ|Phoenix-Mesa-Chandler, AZ|
|8|Los Angeles-Long Beach-Anaheim, CA|Houston-The Woodlands-Sugar Land, TX|Chicago-Naperville-Elgin, IL-IN-WI|
|9|Charlotte-Concord-Gastonia, NC-SC|Seattle-Tacoma-Bellevue, WA|Los Angeles-Long Beach-Anaheim, CA|
|10|Tampa-St. Petersburg-Clearwater, FL|Denver-Aurora-Lakewood, CO|Washington-Arlington-Alexandria, DC-VA-MD-WV|
|11|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Charlotte-Concord-Gastonia, NC-SC|Charlotte-Concord-Gastonia, NC-SC|
|12|Washington-Arlington-Alexandria, DC-VA-MD-WV|San Francisco-Oakland-Berkeley, CA|Tampa-St. Petersburg-Clearwater, FL|
|13|Austin-Round Rock-Georgetown, TX|Tampa-St. Petersburg-Clearwater, FL|Seattle-Tacoma-Bellevue, WA|
|14|Miami-Fort Lauderdale-Pompano Beach, FL|Austin-Round Rock-Georgetown, TX|Portland-Vancouver-Hillsboro, OR-WA|
|15|Nashville-Davidson–Murfreesboro–Franklin, TN|Boston-Cambridge-Newton, MA-NH|Denver-Aurora-Lakewood, CO|
|16|Denver-Aurora-Lakewood, CO|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Minneapolis-St. Paul-Bloomington, MN-WI|
|17|Boston-Cambridge-Newton, MA-NH|Miami-Fort Lauderdale-Pompano Beach, FL|Nashville-Davidson–Murfreesboro–Franklin, TN|
|18|Las Vegas-Henderson-Paradise, NV|Nashville-Davidson–Murfreesboro–Franklin, TN|Austin-Round Rock-Georgetown, TX|
|19|San Antonio-New Braunfels, TX|Kansas City, MO-KS|Kansas City, MO-KS|
|20|Portland-Vancouver-Hillsboro, OR-WA|Las Vegas-Henderson-Paradise, NV|Miami-Fort Lauderdale-Pompano Beach, FL|
|21|Kansas City, MO-KS|Portland-Vancouver-Hillsboro, OR-WA|San Antonio-New Braunfels, TX|
|22|Detroit-Warren-Dearborn, MI|San Diego-Chula Vista-Carlsbad, CA|San Francisco-Oakland-Berkeley, CA|
|23|Orlando-Kissimmee-Sanford, FL|Minneapolis-St. Paul-Bloomington, MN-WI|Columbus, OH|
|24|Oklahoma City, OK|San Antonio-New Braunfels, TX|Detroit-Warren-Dearborn, MI|
|25|Minneapolis-St. Paul-Bloomington, MN-WI|Orlando-Kissimmee-Sanford, FL|Indianapolis-Carmel-Anderson, IN|
|26|Columbus, OH|Detroit-Warren-Dearborn, MI|Orlando-Kissimmee-Sanford, FL|
|27|Indianapolis-Carmel-Anderson, IN|Indianapolis-Carmel-Anderson, IN|Pittsburgh, PA|
|28|St. Louis, MO-IL|St. Louis, MO-IL|St. Louis, MO-IL|
|29|Cincinnati, OH-KY-IN|Columbus, OH|San Diego-Chula Vista-Carlsbad, CA|
|30|Riverside-San Bernardino-Ontario, CA|Raleigh-Cary, NC|Greenville-Anderson, SC|



_Notes_ : Geographic PageRanks are computed from American Community Survey (2023) 5-year estimates. 

Table A.8: Top 30 Ranked Metros by Industry <u>(Part 3 of 3), 2023 5-year ACS</u> 

|Rank|Arts, entertainment, food, accommodation (NAICS 71–72)|Other services (NAICS 81)|Public administration (NAICS 92)|
|---|---|---|---|
|1|New York-Newark-Jersey City, NY-NJ-PA|Washington-Arlington-Alexandria, DC-VA-MD-WV|Washington-Arlington-Alexandria, DC-VA-MD-WV|
|2|Los Angeles-Long Beach-Anaheim, CA|Houston-The Woodlands-Sugar Land, TX|Virginia Beach-Norfolk-Newport News, VA-NC|
|3|Dallas-Fort Worth-Arlington, TX|Dallas-Fort Worth-Arlington, TX|San Diego-Chula Vista-Carlsbad, CA|
|4|Atlanta-Sandy Springs-Alpharetta, GA|Los Angeles-Long Beach-Anaheim, CA|San Antonio-New Braunfels, TX|
|5|Phoenix-Mesa-Chandler, AZ|Chicago-Naperville-Elgin, IL-IN-WI|Seattle-Tacoma-Bellevue, WA|
|6|Houston-The Woodlands-Sugar Land, TX|New York-Newark-Jersey City, NY-NJ-PA|Chicago-Naperville-Elgin, IL-IN-WI|
|7|Charlotte-Concord-Gastonia, NC-SC|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Atlanta-Sandy Springs-Alpharetta, GA|
|8|Boston-Cambridge-Newton, MA-NH|Phoenix-Mesa-Chandler, AZ|Kansas City, MO-KS|
|9|Washington-Arlington-Alexandria, DC-VA-MD-WV|Atlanta-Sandy Springs-Alpharetta, GA|Fayetteville, NC|
|10|Chicago-Naperville-Elgin, IL-IN-WI|Miami-Fort Lauderdale-Pompano Beach, FL|Oklahoma City, OK|
|11|Las Vegas-Henderson-Paradise, NV|Seattle-Tacoma-Bellevue, WA|Baltimore-Columbia-Towson, MD|
|12|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Boston-Cambridge-Newton, MA-NH|Urban Honolulu, HI|
|13|Orlando-Kissimmee-Sanford, FL|Austin-Round Rock-Georgetown, TX|New York-Newark-Jersey City, NY-NJ-PA|
|14|Seattle-Tacoma-Bellevue, WA|Charlotte-Concord-Gastonia, NC-SC|Riverside-San Bernardino-Ontario, CA|
|15|Tampa-St. Petersburg-Clearwater, FL|Nashville-Davidson–Murfreesboro–Franklin, TN|Phoenix-Mesa-Chandler, AZ|
|16|Austin-Round Rock-Georgetown, TX|Denver-Aurora-Lakewood, CO|Houston-The Woodlands-Sugar Land, TX|
|17|Denver-Aurora-Lakewood, CO|Minneapolis-St. Paul-Bloomington, MN-WI|Dallas-Fort Worth-Arlington, TX|
|18|Oklahoma City, OK|Tampa-St. Petersburg-Clearwater, FL|Colorado Springs, CO|
|19|Portland-Vancouver-Hillsboro, OR-WA|Portland-Vancouver-Hillsboro, OR-WA|Austin-Round Rock-Georgetown, TX|
|20|Miami-Fort Lauderdale-Pompano Beach, FL|Detroit-Warren-Dearborn, MI|Tampa-St. Petersburg-Clearwater, FL|
|21|Kansas City, MO-KS|San Francisco-Oakland-Berkeley, CA|Los Angeles-Long Beach-Anaheim, CA|
|22|San Antonio-New Braunfels, TX|Kansas City, MO-KS|Columbia, SC|
|23|Cincinnati, OH-KY-IN|Orlando-Kissimmee-Sanford, FL|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|
|24|Nashville-Davidson–Murfreesboro–Franklin, TN|Columbia, SC|Richmond, VA|
|25|Columbus, OH|Indianapolis-Carmel-Anderson, IN|Bremerton-Silverdale-Port Orchard, WA|
|26|Columbia, SC|St. Louis, MO-IL|Jacksonville, FL|
|27|San Francisco-Oakland-Berkeley, CA|Oklahoma City, OK|Las Vegas-Henderson-Paradise, NV|
|28|St. Louis, MO-IL|San Antonio-New Braunfels, TX|Pensacola-Ferry Pass-Brent, FL|
|29|Pittsburgh, PA|Columbus, OH|Boston-Cambridge-Newton, MA-NH|
|30|Greenville-Anderson, SC|San Diego-Chula Vista-Carlsbad, CA|Charlotte-Concord-Gastonia, NC-SC|



_Notes_ : Geographic PageRanks are computed from American Community Survey (2023) 5-year estimates. 

## Table A.9: Top 50 Ranked CBSAs (2001, 2011, and 2021) 

|Rank|Top 50 Metros, 2001-2002|Top 50 Metros, 2011-2012|Top 50 Metros, 2021-2022|
|---|---|---|---|
|1|Dallas-Fort Worth-Arlington, TX|Dallas-Fort Worth-Arlington, TX|Dallas-Fort Worth-Arlington, TX|
|2|Phoenix-Mesa-Chandler, AZ|Houston-Pasadena-The Woodlands, TX|Phoenix-Mesa-Chandler, AZ|
|3|Houston-Pasadena-The Woodlands, TX|Atlanta-Sandy Springs-Roswell, GA|Houston-Pasadena-The Woodlands, TX|
|4|Minneapolis-St. Paul-Bloomington, MN-WI|Phoenix-Mesa-Chandler, AZ|Seattle-Tacoma-Bellevue, WA|
|5|Seattle-Tacoma-Bellevue, WA|Seattle-Tacoma-Bellevue, WA|Atlanta-Sandy Springs-Roswell, GA|
|6|Chicago-Naperville-Elgin, IL-IN|Chicago-Naperville-Elgin, IL-IN|Chicago-Naperville-Elgin, IL-IN|
|7|Los Angeles-Long Beach-Anaheim, CA|Los Angeles-Long Beach-Anaheim, CA|Minneapolis-St. Paul-Bloomington, MN-WI|
|8|Atlanta-Sandy Springs-Roswell, GA|Miami-Fort Lauderdale-West Palm Beach, FL|New York-Newark-Jersey City, NY-NJ|
|9|Portland-Vancouver-Hillsboro, OR-WA|Minneapolis-St. Paul-Bloomington, MN-WI|Los Angeles-Long Beach-Anaheim, CA|
|10|Denver-Aurora-Centennial, CO|New York-Newark-Jersey City, NY-NJ|Indianapolis-Carmel-Greenwood, IN|
|11|Indianapolis-Carmel-Greenwood, IN|Portland-Vancouver-Hillsboro, OR-WA|Columbus, OH|
|12|Kansas City, MO-KS|Indianapolis-Carmel-Greenwood, IN|Portland-Vancouver-Hillsboro, OR-WA|
|13|Columbus, OH|Washington-Arlington-Alexandria, DC-VA-MD-WV|San Antonio-New Braunfels, TX|
|14|New York-Newark-Jersey City, NY-NJ|Columbus, OH|Oklahoma City, OK|
|15|Washington-Arlington-Alexandria, DC-VA-MD-WV|Kansas City, MO-KS|Kansas City, MO-KS|
|16|San Diego-Chula Vista-Carlsbad, CA|Oklahoma City, OK|Boston-Cambridge-Newton, MA-NH|
|<br>17|<br>Oklahoma City, OK|<br>San Antonio-New Braunfels, TX|<br>Charlotte-Concord-Gastonia, NC-SC|
|<br>18|<br>Las Vegas-Henderson-North Las Vegas, NV|Tampa-St. Petersburg-Clearwater, FL|Washington-Arlington-Alexandria, DC-VA-MD-WV|
|19|San Antonio-New Braunfels, TX|San Francisco-Oakland-Fremont, CA|Nashville-Davidson–Murfreesboro–Franklin, TN|
|20|Miami-Fort Lauderdale-West Palm Beach, FL|Detroit-Warren-Dearborn, MI|Miami-Fort Lauderdale-West Palm Beach, FL|
|21|Boston-Cambridge-Newton, MA-NH|Boston-Cambridge-Newton, MA-NH|Tampa-St. Petersburg-Clearwater, FL|
|22|Detroit-Warren-Dearborn, MI|Nashville-Davidson–Murfreesboro–Franklin, TN|Detroit-Warren-Dearborn, MI|
|23|Tampa-St. Petersburg-Clearwater, FL|Las Vegas-Henderson-North Las Vegas, NV|Raleigh-Cary, NC|
|24|St. Louis, MO-IL|San Diego-Chula Vista-Carlsbad, CA|Las Vegas-Henderson-North Las Vegas, NV|
|25|Charlotte-Concord-Gastonia, NC-SC|Austin-Round Rock-San Marcos, TX|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|
|26|Sacramento-Roseville-Folsom, CA|Charlotte-Concord-Gastonia, NC-SC|Little Rock-North Little Rock-Conway, AR|
|27|Nashville-Davidson–Murfreesboro–Franklin, TN|Denver-Aurora-Centennial, CO|Des Moines-West Des Moines, IA|
|28|Boise City, ID|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Boise City, ID|
|29|San Francisco-Oakland-Fremont, CA|St. Louis, MO-IL|Grand Rapids-Wyoming-Kentwood, MI|
|30|Raleigh-Cary, NC|Raleigh-Cary, NC|San Diego-Chula Vista-Carlsbad, CA|
|31|Philadelphia-Camden-Wilmington, PA-NJ-DE-MD|Little Rock-North Little Rock-Conway, AR|Austin-Round Rock-San Marcos, TX|
|<br>32|<br>Albuquerque, NM|<br>Salt Lake City-Murray, UT|Sioux Falls, SD-MN|
|33|Riverside-San Bernardino-Ontario, CA|Boise City, ID|San Francisco-Oakland-Fremont, CA|
|34|Salt Lake City-Murray, UT|Sacramento-Roseville-Folsom, CA|Denver-Aurora-Centennial, CO|
|<br>35|<br>Memphis, TN-MS-AR|Memphis, TN-MS-AR|St. Louis, MO-IL|
|<br>36|<br>Orlando-Kissimmee-Sanford, FL|<br>Orlando-Kissimmee-Sanford, FL|Albuquerque, NM|
|<br>37|<br>Sioux Falls, SD-MN|<br>Grand Rapids-Wyoming-Kentwood, MI|<br>Orlando-Kissimmee-Sanford, FL|
|<br>38|<br>Austin-Round Rock-San Marcos, TX|<br>Tulsa, OK|<br>Memphis, TN-MS-AR|
|<br>39|<br>Grand Rapids-Wyoming-Kentwood, MI|<br>Riverside-San Bernardino-Ontario, CA|<br>Salt Lake City-Murray, UT|
|<br>40|<br>Milwaukee-Waukesha, WI|<br>Albuquerque, NM|<br>Sacramento-Roseville-Folsom, CA|
|41|Little Rock-North Little Rock-Conway, AR|Pittsburgh, PA|Fort Wayne, IN|
|42|Tulsa, OK|Des Moines-West Des Moines, IA|Tulsa, OK|
|43|Jacksonville, FL|Sioux Falls, SD-MN|Milwaukee-Waukesha, WI|



|44|Des Moines-West Des Moines, IA|Milwaukee-Waukesha, WI|Jacksonville, FL|
|---|---|---|---|
|45<br>|Pittsburgh, PA<br>|Birmingham, AL<br>|Pittsburgh, PA<br>|
|46|Tucson, AZ|Fort Wayne, IN|Wichita, KS|
|47<br>|Reno, NV<br>|Jacksonville, FL<br>|Reno, NV<br>|
|48|Madison, WI|Omaha, NE-IA|Birmingham, AL|
|49|Omaha, NE-IA|Reno, NV|Omaha, NE-IA|
|50|Fort Wayne,IN|Baltimore-Columbia-Towson,MD|Albany-Schenectady-Troy,NY|



_Notes_ : Geographic PageRanks are computed from IRS tax returns in 2001-2002, 2011-2012, and 2021–2022. 

