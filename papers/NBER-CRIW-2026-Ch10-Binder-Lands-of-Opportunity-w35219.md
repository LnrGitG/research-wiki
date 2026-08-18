---
title: NBER-CRIW-2026-Ch10-Binder-Lands-of-Opportunity-w35219
type: paper
source_pdf: raw/papers/NBER-CRIW-2026-Ch10-Binder-Lands-of-Opportunity-w35219.pdf
converted: 2026-08-18
---

## NBER WORKING PAPER SERIES 

## LANDS OF OPPORTUNITY: DIFFERENCES IN THE GEOGRAPHY OF WEALTH AND INCOME MOBILITY IN THE UNITED STATES 

Ariel J. Binder Max Risch John L. Voorheis 

Working Paper 35219 http://www.nber.org/papers/w35219 

## NATIONAL BUREAU OF ECONOMIC RESEARCH 

1050 Massachusetts Avenue Cambridge, MA 02138 May 2026 

We thank Eirik Eylands Brandsaas for providing an excellent discussion of the initial version of this paper at the NBER CRIW Conference on Measurement of Housing and the Housing Sector. We thank Thesia Garner, Joseph Gyourko, and Sonya Porter for additional comments and for organizing the conference. The views expressed herein are those of the authors and do not necessarily reflect the views of the National Bureau of Economic Research. 

NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications. 

© 2026 by Ariel J. Binder, Max Risch, and John L. Voorheis. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source. 

Lands of Opportunity: Differences in the Geography of Wealth and Income Mobility in the United States 

Ariel J. Binder, Max Risch, and John L. Voorheis NBER Working Paper No. 35219 May 2026 JEL No. D31, E24, O18 

## **<u>ABSTRACT</u>** 

We provide new county-level estimates of intergenerational mobility, covering multiple economic concepts: total income, labor income, homeownership, housing wealth, and total wealth. This is possible via small-area estimation techniques and linked survey and administrative data covering millions of U.S. children born between 1978 and 1986. We find that relative mobility in wealth concepts shows less spatial clustering and more spatial variation than relative mobility in income concepts. Many cities and their suburbs exhibit lower relative mobility (i.e. higher intergenerational persistence) in wealth concepts than in income concepts. Next, we show that various local characteristics are associated with some concepts of economic mobility but not with others. For example, we estimate a strong negative association between the local severity of the Great Recession and child income, regardless of parent position in the income distribution. However, the negative association between recession severity and wealth only exists among children from poorer families. We provide a public-use data package to facilitate further research. 

Ariel J. Binder John L. Voorheis U.S. Census Bureau U.S. Census Bureau ariel.j.binder@census.gov Department of Economics john.l.voorheis@census.gov 

Max Risch Carnegie Mellon University and NBER mwrisch@andrew.cmu.edu 

Download link for public-use data package is available at https://www2.census.gov/ces/misc/binder_risch_voorheis_county_mobility_stats.xlsx 

# **1. Introduction** 

It is widely acknowledged that children’s neighborhoods shape their long-run economic outcomes (Chyn and Katz, 2021). The evidence for this is based on a large literature analyzing the intergenerational mobility of income. This literature has produced many granular statistics, including choropleth maps of income mobility featured in Chetty et al. (2014); Chetty and Hendren (2018b); Chetty et al. (2020, 2026b) among others. These exercises tell a compelling story of where the “land of opportunity” lies in the United States. However, income is just one measure of economic well-being, and it obscures the holding of assets that do not generate regular income flows. For this reason, prominent observers (e.g. Piketty, 2014; Wolff, 2017) have argued that wealth is a better measure for understanding economic resources at the family level and inequality at the population level. There is thus a gap at the center of this evidence base. While we increasingly understand where and why disadvantaged children grow up to be _rich_ , we know less about where they grow up to be _wealthy_ . 

This paper seeks to fill this lacuna by producing a new set of intergenerational mobility statistics at the county level. We amass information on five concepts, including two definitions of income (total income and labor market income) and three concepts related to wealth (gross housing wealth, total gross wealth, and homeownership). These statistics have the virtue of being generated from the exact same sets of parents and children, a feature made possible by linking a wide variety of confidential data sources using the U.S. Census Bureau’s data linkage infrastructure. This facilitates a valid internal comparison across concepts. Moreover, the income data we use is similar to that used by Chetty et al. (2014) and following work. This enables us to replicate known facts about total-income mobility and examine how these facts change when focusing exclusively on labor income. We make this dataset available to the public via the following download link from the census.gov data repository. 

Using this new dataset, we begin by describing the geographic distribution of economic mobility, contrasting different mobility measures and different resource concepts. We focus 

1 

on measures of both “upward mobility,” or the average outcomes of children of parents at the bottom of the resource distribution, and “relative mobility,” or the difference in outcomes between children of parents lower and higher in the distribution. We then explore local correlates of economic mobility, comparing how different exposures shape income versus wealth mobility. 

Among the new facts we establish are the following. First, the prior emphasis on total income mobility potentially understates neighborhood variation: we estimate a higher degree of county variation in labor income, in housing wealth, and in homeownership mobility. Second, although our concepts of economic mobility are correlated across counties, the correlations between relative mobility of income-based and wealth-based concepts are below 0.5. Third, coastal areas and populous cities have a combination of both higher absolute mobility and lower relative mobility of housing wealth. There is therefore strong intergenerational persistence among wealthy families in these larger areas, a fact which is less apparent in income concepts. Fourth, some variables previously emphasized in the literature, such as income inequality, social capital, and racial composition, robustly predict economic mobility. Yet others, such as residential segregation, employment, violent crime, and home prices, associate with some economic mobility concepts but not with others. 

Fifth, we leverage the timing of our data around the Great Recession to provide evidence on the mobility implications of this episode. Our estimates can be interpreted as longrun associations because we measure child outcomes 10 years following the recession, in 2019-2021, when they were around 40 years old. Controlling for a large vector of preRecession covariates, we find a strong negative correlation between recession severity and absolute income mobility, but no relationship with relative income mobility. This implies lower average incomes across the parental distribution. However, we find evidence of a – “pivot” in the intergenerational mobility of housing we estimate declines in both upward and relative mobility of homeownership and housing wealth. This suggests that Millennial children raised by families at the bottom of the distribution experienced lingering adverse 

2 

wealth effects from the Great Recession. However, the wealth accumulation of those raised by rich families was largely insulated from the shock. 

This paper contributes to the literature in three ways. First, we offer new large-scale estimates of wealth and labor income persistence across U.S. counties. These results complement previous national analyses of wealth mobility using household surveys (e.g. Pfeffer and Killewald, 2017) or administrative records (e.g. Black et al. (2023) and Fagereng et al., 2020 in a Norwegian context and Binder et al., 2025 in a U.S. context), and granular spatial analyses of total income mobility mentioned above. Second, our county-level estimates broaden the scope of the “childhood exposure” literature which examines the impacts of neighborhoods on human capital formation and adulthood income (Chetty and Hendren, 2018a,b; Chyn and Katz, 2021). Third, we contribute to literature on the impact of exposure to recessions on long-run economic outcomes (e.g. Malmendier and Nagel, 2011; Oreopoulos et al., 2012; Yagan, 2019; Schwandt and von Wachter, 2019; Rinz, 2022; Stuart, 2022; Angelini and Ferrari, 2025). 

The rest of the paper is organized as follows. First, we outline the construction of our data, utilizing the Census Bureau’s data linkage infrastructure. Second, we outline our simple model of economic mobility, our concepts of economic resources, and our small area estimation strategy. Third, we describe geographic patterns of economic mobility via countylevel choropleth maps. Fourth, we describe relationships between county level characteristics, economic shocks related to the Great Recession and our county level mobility measures. Finally, we conclude, noting caveats and areas for future work. 

# **2. Data and Methods** 

Our approach is to combine survey data from the 2000 Decennial Census with administrative records on 1) property ownership and valuation, and 2) total income and its component sources. This allows us to observe both income and wealth variables for a very large sample of children born in the late 1970s - mid 1980s along with their parents. This is the most 

3 

comprehensive such dataset yet assembled in the United States, providing enough sample size and geographic coverage to produce granular geospatial statistics. We describe each step in the data construction process and how these components are linked together. Figure 1 visualizes our data linkage process in schematic form. 

## **2.1. Parent-child links** 

We leverage the U.S. Census Bureau’s data linkage infrastructure inside the Bureau’s secure computing environment. This infrastructure allows researchers to link survey, Census and administrative datasets over time and across generations. All files described here have had anonymized linkage keys for both individuals (Protected Identification Keys, or PIKs) and housing units (Master Address File IDs or MAFIDs) attached by Census Bureau staff. PIKs are essentially scrambled Social Security Numbers (SSNs), with information on name, date of birth and/or address sometimes used to produce a valid PIK when the former is not available. See Layne et al. (2014) for further background. 

We start from the “long form” of the 2000 Decennial Census, in which a 1-in-6 random sample of households in the country was surveyed on a broad set of economic and sociodemographic content.<sup>1</sup> Taking the universe of reference persons assigned PIKs, we identify all children of reference persons based on the relationship to reference person variable, who were aged 14-16 at survey response. In order to associate these children were their adulthood economic outcomes, we also require that they be assigned valid PIKs. 

We supplement this set of parent-child links with a set based on form 1040 tax returns from the Internal Revenue Service. These forms contain links between tax filers who claimed dependents and the dependents themselves (as discussed further in Chetty et al., 2014). We collect claimer-dependent links on the 1994 and 1998 tax returns for the sets of dependents aged 14-16 in those tax years. This allows us to increase our sample size and capture children who do not get assigned PIKs in survey data, as tax returns have near-perfect PIK 

> 1This content was later the basis for the annual American Community Survey (ACS). 

4 

assignment rates.<sup>2</sup> Moreover, these sets of children were born slightly earlier, enabling us to measure their housing outcomes at closer to peak ages of homeownership. 

The coverage of our resultant sample is similar to studies of intergnerational mobility that leverage administrative income data from tax or Social Security records. On the one hand, our usage of a nationally-representative survey means that we can include some individuals and their children who did not file taxes.<sup>3</sup> On the other hand, to associate children with parents and their housing portfolios, we must restrict focus to tax filers who were reference persons and were assigned a PIK in survey data. Bond et al. (2014) estimated PIK rates of prime-age adults on ACS data to be around 90%. 

The resulting sample includes over 3.4 million parent-child pairs, with children born – between the years of 1978-1986 and thus aged 34-42 in 2020 when we measure their adulthood economic outcomes. Parents have an average age of 46.3 in 2000 when we measure their income and housing assets. 

## **2.2. Economic outcomes** 

With parent-child links in hand, we develop an intergenerational dataset combining information on parental resources with children’s economic outcomes in adulthood. 

_Parental housing assets and income._ Parental housing information is taken directly from the 2000 long form, based on items recording ownership tenure and estimated market value of owned homes. We assign parental total income by linking the average adjusted gross income (AGI) reported on form 1040 from 1999-2001. For individuals not filing taxes in any of those years, we replicate an AGI concept with the sum of own and spouse’s personal incomes reported on the long form. As we include all long form responses after editing and 

> 2 Ideally we would have used the 1997 year to create a fully non-overlapping set of birth cohorts with the 1994 and 2000 years, but Census had not received 1996 or 1997 data from the Internal Revenue Service (IRS) at the time of our analysis. Although not all families file taxes in every tax year, we verified that including the 1995 and 1999 years would barely raise our sample size. This is due to i) the narrow age range of the dependents we need to consider, and ii) the child tax credit, which provides a strong incentive for claimers to file taxes. Gee et al. (2024) demonstrates the near-universal coverage of children on U.S. tax returns. 

> 3Binder et al. (2022a) observed that a prototypical intergenerational sample based on tax data, when restricted to children born in the United States, was nearly identical in composition and selected adulthood outcomes to the subsample of similarly-aged U.S. natives on the ACS. 

5 

imputation there are no missing values for this income concept, and we treat $0 income as as a true zero. We assign parental labor income as the wage-and-salary component of AGI averaged over 1999-2001. For nonfiling reference persons, we assign the wage and salary income recorded on W-2 forms averaged over these years.<sup>4</sup> 

_Child housing assets._ We capture child property ownership by linking all owned properties over the period 2019-2021, as recorded in property assessment and deed transfer records. These records cover the universe of deeded properties in the United States, and were provided to Census by Black Knight, LLC.<sup>5</sup> We assign home values for all owned properties based on automated valuation model estimates from Black Knight, which use recent sales of similar nearby properties to predict current market values of the given property.<sup>6</sup> As discussed further in Binder et al. (2025), our sample—especially the younger cohorts—is likelier to own property in 2021 than in 2019. Rather than average across years as is done for income flows, we generally choose the maximum owned value observed in the short panel, to account for the age-in phenomenon. 

_Child income._ We collect total and labor income information for children in an analogous manner as for the parents, using 1040 and W-2 records from 2019-2021. 

_Parent and child gross wealth._ We construct measures of total gross wealth using capitalization methods similar to Piketty et al. (2018) and Saez and Zucman (2016). For parents, we have information about dividends (flows from equities), interest income (flows from fixed income securities) and rents (flows from rental housing) from form 1040 returns; labor earnings from 1040s or W-2s; and information on business ownership from the 2000 long form 

> 4The voluntary nonfiling rate is around 15%, which is ameliorated substantially by including W-2 income, which is reported for all formally employed individuals. We only consider the reference person’s W-2 information for this assignment. This is reasonable because few married reference persons aged 35-54 in the long form do not file taxes, and these rare nonfilers often have peculiar finances that lead them not to pool spousal incomes. 

> 5Black Knight, now a subsidiary of Intercontinental Exchange, is one of several vendors of these types of data. Binder et al. (2022b) demonstrate a very high degree of comparability across two different vendors. 

> 6When these values are missing, as they are in a small share of cases, we impute them based on the most recent assessed value (adjusted to account for property tax base rules that vary across counties), the most recent sold value (adjusted for time since last sale), or the average of both. The Appendix of Binder et al. (2025) provides further detail. 

6 

itself. For children, we have the same information from 1040s/W-2s, and additionally have information on capital gains (from 1040s), income from sole proprietorships, partnerships and S-corporations (from Schedule C, form 1065-K1 and 1120S-K1 respectively) and retirement account balances from form 5498. Using capitalization factors from Smith et al. (2022) and Piketty et al. (2018), we convert each individual financial income flow into a wealth stock, and then sum all individual wealth stocks together. This yields a consistent measure of financial wealth covering equities, fixed income securities, business ownership and retirement accounts across both generations. We construct total gross wealth as the sum of capitalized financial wealth and housing wealth. We truncate negative capitalized wealth to zero before this final computation, and treat all other zero-wealth individuals as true zeroes (e.g. on the extensive margin of wealth). 

## **2.3. Rank-rank methodology** 

We use ranks instead of logs to model intergenerational mobility i) to conform with recent income mobility literature and ii) to incorporate individuals with zero wealth or labor income. We calculate ranks in the full sample for each of the resource concepts above. To make valid population statements, we use 2000 long form sampling weights for the parents. For children, we employ a composite weight that adjusts for imperfect assignment of PIKs in the property data and life-cycle bias, as described in detail in Binder et al. (2025). 

We begin with a standard rank-rank model: 



where _Rankc_ and _Rankp_ are the ranks of children and parents in their respective distributions for a given income or wealth concept, on a 0 to 100 quantile scale. The parameter _β_ captures _relative_ mobility: the effect on children’s average outcome of a one-rank gain in parent resources. Higher _β_ (i.e. a steeper rank-rank slope) implies more intergenerational persistence and lower mobility. The _α_ parameter is a measure of upward (or _absolute_ ) mo- 

7 

bility, representing the average the average outcome of children raised by the parents at the bottom of the distribution. 

There are sets of individuals with no housing wealth (renters) or with no gross wealth or wage and salary income. We assign these individuals a rank equal to half the size the extensive margin. For example, if the weighted proportion of parent renters is 20%, we assign each parent renter a rank of 10. For these concepts, we augment our model of intergenerational mobility: 



where _δp_ is a fixed effect associated with a parent being in the extensive margin category. This model allows the outcomes of children raised by parent renters, or parents without wage income, to be different than what would be predicted by a linear extrapolation of the rank-rank slope. Binder et al. (2025) found that for housing wealth, this “kinked” model fit the data considerably better than the standard linear model, as parent renters are a more heterogeneous group than poor parent owners with higher average income. 

In the augmented model, we define absolute mobility as _α_ = _γ_ + _P_ ( _EM_ ) _β_ , which represents the average outcome of children raised by the parents with the lowest value on the intensive margin (e.g. lowest earners, lowest-value homeowners). Relatedly, _α_ + _δ_<sup>˜</sup> is the average outcome of children raised by parents on the extensive margin (e.g. renters, non-earners), where _δ_<sup>˜</sup> = _δ − P_ ( _EM_ ) _β/_ 2.<sup>7</sup> 

Finally, to separately estimate the probability of child homeownership as a function of parental housing resources, we use the model: 



We refer to this outcome interchangeably as homeownership or as “extensive housing wealth.” 

Our primary focus is on comparing relative mobility ( _β_ ) and absolute mobility ( _α_ ) across 

> 7Thus, _δ_ ˜ is the absolute mobility difference between children raised by parents on the extensive margin versus on the bottom of the intensive margin. 

8 

resource measures. For housing, we also separately investigate the outcomes of children of parent renters ( _δ_ ). 

## **2.4. Small-area estimation** 

Binder et al. (2025) provide ample analysis of these measures at the national level. In this paper, we want to examine how they vary at lower levels of geography. To do this, we first produce direct estimates of the regression equations above for each childhood county of residence, calculating _α_ , _β_ and _δ_ , plus their associated standard errors. As these direct estimates can be noisy and pose disclosure risk in small counties, we employ a second modeling step. This involves Faye-Herriot small-area estimation regressions, which have a shrinkage property such that as the number of observations in a county direct estimate declines, the Faye-Herriot converges to the estimate at a larger nested geography. In our case, we use the commuting zone containing the given county, or a group of commuting zones with a total population of at least 500,000, per Census Bureau disclosure rules. 

This approach has the double virtue of minimizing risk of unintentional disclosure of microdata in small counties, while also increasing the signal to noise ratio in such counties. However, to avoid the de-facto imputation of a commuting-zone estimate to a tiny and potentially unrepresentative county within that larger geography, we suppress estimates for counties with less than 20 parent-child pairs in our sample. We make these small-area estimates available to researchers in an online data appendix alongside this paper. Overall, we produce mobility estimates for 3,133 U.S. counties—i.e. nearly all of them. 3,004 counties have a complete set of measures, while the remainder have missing gross total wealth mobility measures due to additional suppression of small counties required for this concept.<sup>8</sup> 

The full set of ( _α, β, δ_ ) parameters for each resource concept is included in the public data package associated with this paper, available for download here. 

> 8A small number of counties do not have enough non-zero wealth individuals to estimate the linear regressions used to generate the direct estimates of _α_ , _β_ and _δ_ . 

9 

# **3. Geospatial Variation in Wealth and Income Mobility** 

We are now in a position to describe and visualize patterns in intergenerational mobility across space, contrasting for the first time how these patterns differ across resource measures. 

As a reference point, the third column of Table 1 reports the average level of mobility across counties for each of our resource concepts and mobility measures. Note that the _α_ estimates are not directly comparable across concepts due to the differing percentages of parents on the intensive margin,<sup>9</sup> but the _β_ and _δ_ estimates are. We see that the average county experiences a higher level of intergenerational persistence (i.e. _β_ ) in housing concepts than in income concepts.<sup>10</sup> 

We also observe substantial differences across concepts in _δ_ . For example, in the average county, relative to the children of poorest homeowners, children of renters are 8.25 percentage points less likely to own a home. However, their average housing wealth rank is almost the same.<sup>11</sup> Meanwhile, children of parents without positive labor income are over 10 ranks higher in the child labor income distribution than children of the lowest-labor-income parents. This reflects that the absence of labor income often signals economic status such as business ownership. 

The last column of Table 1 begins to investigate geospatial variation by reporting the cross-county standard deviation of each mobility measure. As in Chetty et al. (2014) and Chetty et al. (2020), we note substantial spatial variation in total income mobility. For example, the standard deviation of intergenerational persistence ( _β_ ) in total income is 0.155, 

> 9For example, 78% of parents in our sample owned their residence and therefore had some housing wealth, whereas every single parent had a nonzero value of total income. As a consequence, for housing concepts, _α_ refers to the expected outcome of the child raised by the 22<sup>nd</sup> percentile parent, while for total income, _α_ is the expected outcome of the child raised by the 0<sup>th</sup> percentile parent. Because all ranks are defined at the population level, comparisons within resource concepts but across locations are valid. 

> 10The average _β_ across counties is lower than the population _β_ for housing wealth discussed in Binder et al. (2025) of 0 _._ 43 because there is more intergenerational persistence in higher population counties on average. This is in contrast to the income concepts, for which the cross-county averages are quite similar to the population estimates (0 _._ 35 for total income and 0 _._ 29 for labor income). 

> 11As discussed further in Binder et al. (2025), children of renters own more expensive homes than do children of poorest owners, despite owning homes at lower rates. This causes average attainments to be similar although the variance is higher for children of renters. 

10 

which is around 47% of its mean. We estimate a comparable standard deviation for total wealth. However, other resource concepts show nontrivially more spatial variation. The cross-county standard deviation of intergenerational persistence is 0.235 for homeownership (57% of the mean), 0.209 for gross housing wealth (60.2% of the mean), and 0.178 for labor income (54.1% of the mean). These simple facts suggest that there is even more spatial heterogeneity in economic opportunity than has previously been emphasized. Identifying and understanding this variation remains an important and incomplete task in the literature. 

## **3.1. Cross-county correlations** 

Table 2 continues to investigate differences in mobility measures and their spatial patterning. It reports two cross-county correlation matrices of our 5 economic concepts, one for each of the _α_ and _β_ measures of intergenerational mobility (Panel A and B, respectively). 

Looking at Panel A, we see that the county level of absolute mobility for a given economic concept is strongly correlated with that for every other concept. In the extreme, absolute mobility of labor income and total income are correlated across counties at nearly 0.9. However, the correlations between wealth and income concepts are smaller than this benchmark. Absolute mobility of housing wealth is correlated at 0.75 with labor income and 0.72 with total income. The correlations decline further when we consider the homeownership outcome. This measure is correlated at 0.6 with labor income and 0.56 with total income. It is also correlated at only 0.63 with gross housing wealth. As discussed further below, this plausibly reflects the effect of home price variation, whereby cheaper homes encourage upward homeownership mobility but lower the wealth returns to homeownership. 

Panel B shows that as we switch from absolute to relative mobility, the correlation coefficients decline in magnitude. Relative mobility of labor income _β_ and total income _β_ are now correlated at 0.77, and the correlations of _β_ between wealth and income concepts are all substantially smaller. Total wealth mobility is correlated at only 0.44 with labor income mobility and 0.50 with total income mobility; housing wealth mobility is correlated at 0.41 

11 

with labor income mobility and 0.43 with total income mobility.<sup>12</sup> Interestingly, the correlation between homeownership and housing wealth mobility strengthens from 0.63 to 0.68 when we switch from absolute to relative mobility measures. We discuss this further in the next section. 

Ultimately these statistics indicate that if one’s goal is to quantitatively analyze spatial variation in economic mobility—particularly, relative mobility, i.e. the association between a one-rank increase in a parent’s resources and the child’s rank in adulthood—it is likely not sufficient to rely exclusively on an income-based measure. 

## **3.2. Mapping mobility** 

To better visualize these patterns, we generate a series of choropleth maps showing the distribution of mobility measures across counties on a color scale from warm colors (low _α_ or _δ_ or high _β_ , corresponding to lower levels of absolute/relative mobility) to cool colors (high _α_ or _δ_ or low _β_ , corresponding to higher levels of absolute/relative mobility). 

Choropleth maps of counties can sometimes be misleading as counties are mostly similar in terms of land area but are highly variable in terms of population. As an extreme example, Loving County, TX has a population of under 100, while Los Angeles County, CA has a population of over 10 million. This can lead to the mistaken visual inference, upweighting the characteristics of lower population, rural areas (which take up more area on a map) and downweighting the characteristics of higher population urban areas (which take up relatively less area). To address this, we map percentiles of the county-level mobility distribution, weighted by the county’s sample size in our underlying microdata in each map. This ensures that the midpoint of the color scale corresponds to the mobility experience of the median – child in our underlying data and that warmer colors correspond to lower mobility than this median child, and cooler colors higher mobility. 

> 12The high correlations of _α_ likely reflect that at the bottom of the total income distribution, the vast majority of income is labor income and the majority of wealth is pension wealth, which is closely tied to labor income. Moving up the distribution, capital and business income become more important, as do housing and capital wealth. Differences in the intergenerational mobility of these sources of income and wealth across space are reflected by relatively lower correlations of _β_ between economic concepts. 

12 

We start with the relative mobility measure – _β_ . Recall that higher values of _β_ imply greater intergenerational persistence and thus _less_ relative mobility. Figure 2 maps this – parameter for our income concepts total income and labor market income (wages and salary). These maps look similar to the income mapping in Chetty et al. (2014), with notably lower relative mobility across the Southeast, and higher relative mobility in the Great Plains. Although the two income concepts have similar regional patterns, some differences do exist: for instance, there is lower mobility for labor income than for total income in Appalachia (especially southwest Pennsylvania) and higher mobility for labor income in Southeast Florida. 

Figure 3 summarizes relative mobility for our two key wealth measures: gross housing wealth and gross total wealth. Compared to income, there is much less geographic clustering, especially in the Southeast. The Great Plains are high in mobility for both income and wealth concepts, but some notable discrepancies arise in other regions. For example, the San Francisco Bay area, Massachusetts, and New Jersey appear to have higher wealth persistence than income persistence. Looking specifically at housing wealth versus income and zooming on various parts of the maps, one can discern a pattern whereby housing persistence exceeds income persistence in a variety of large urban areas, such as: New York City and surrounding counties, Los Angeles, Chicago, Houston, Phoenix, Dallas/Fort Worth, Seattle, Boston, DC, Miami, Atlanta, Charlotte, San Diego, San Antonio, Minneapolis, Denver, Las Vegas, Austin, and the Philadelphia suburbs. On the other hand, income persistence exceeds housing persistence throughout lower-population areas in the South. Zooming out, the fact that more of the area of the maps depicting wealth mobility is blue, relative to the maps depicting income mobility, again reflects that intergenerational persistence of wealth is higher in denser, more urban counties. While income mobility shows more spatial concentration, wealth mobility shows more concentration by density. 

Figure 4 maps the relative mobility of extensive margin housing wealth – i.e. the increase in a child’s homeownership probability associated with a a one-rank increase in the parent’s 

13 

housing wealth rank. Here some spatial clustering in the Southeast reappears, though to a lesser extent than in the income mobility case. We also note that a higher value of this measure (i.e. more intergenerational persistence) in many of the urban counties noted above for gross housing wealth, although the contrast with income is not always as strong. 

We next turn to the absolute mobility measure – _α_ . Recall that this is the average outcome of children with parents who are at the bottom of the resource distribution (conditional on possessing a positive amount of the given resource). Once again we start with income concepts, which are mapped in Figure 5. A similar broad pattern echoes that seen – for relative income mobility lower upward mobility is prevalent across the Southeast of the country, while higher upward income mobility appears much more common in the upper Midwest and Great Plains. Geographic patterns of upward mobility in labor income and total income are very closely aligned, more so than for relative mobility, as reflected with the correlation coefficients from Table 2. 

Figure 6 maps absolute mobility for the wealth concepts. Though again there are some broadly similar geographic patterns in the Southeast and upper Midwest, we see more upward wealth mobility in California, the DC metro area, New England, and (for gross total wealth) the Miami metro area compared to income mobility. The extensive margin of homeownership, however, looks substantially different, as shown in Figure 7. California has very low absolute mobility of homeownership, i.e., the children of the worst-off homeowners are much less likely to be homeowners as adults relative to the rest of the country. Moreover, many places that have low absolute mobility of income and gross wealth, such as Pennsylvania, western Michigan, and parts of Georgia, have relatively high absolute mobility of homeownership. Many areas, particularly in the Northeast and West Coast, that are characterized by high upward mobility of income are not accompanied by high upward mobility in homeownership rates.<sup>13</sup> 

> 13The reason there is relatively high upward mobility in housing wealth in some of these areas is likely associated with high home prices – though the probability of ownership is low, those who do own a home own a particularly valuable home. 

14 

Finally, we turn to the housing outcomes of children of parent renters, as summarized by _δ_ . Recall that this measure is the outcome difference relative to children of parent homeowners at the bottom of the value distribution. Figure 8 shows sharp contrasts in relative outcomes for children of renter parents along rural vs. urban lines. Panel (b) shows that children of parent renters are typically less likely to be homeowners than children of parents at the – bottom of the home value distribution (i.e., negative _δ_ ), but in many large metro areas e.g. Seattle, Denver, New York City and surrounding counties, Chicago, Boston, greater – DC, Miami, and in coastal California children of parent renters are more likely to be homeowners. These children of renters are also have more housing wealth as adults. 

# **4. Local Correlates of Economic Mobility** 

What can account for these geographic patterns in economic mobility? Chetty et al. (2014) and others have suggested a central role for neighborhood exposures in shaping upward income mobility. This evidence is typically based on descriptive regressions and “mover designs” that align cross-area variation in this mobility statistic with cross-area variation in neighborhood economic, demographic, and social factors. 

Building on this work, we explore here whether neighborhood factors affect intergenerational mobility _differently_ for different mobility measures and economic concepts. To do so, we estimate simple linear regressions of the form 



where _Mc_ is county _c_ ’s level of intergenerational mobility based on a given mobility measure _M_ . We consider _α_ and _β_ measures across all five economic resource concepts. _Xc_ is a vector of county characteristics, matched to parents’ counties of residence and measured at around the same time we measure parents’ economic resources. 

We source 16 county-level characteristics from the replication data associated with Chetty 

15 

et al. (2014). These authors collected county- and commuting-zone-level information circa 2000. This timing matches when we measure parental locations and economic outcomes in our dataset. We merge this information to our county-level dataset of mobility values<sup>14</sup> and group it into 6 categories: demographics, economic averages (or “fundamentals”), economic changes, economic inequality, local public investment, and social forces. We then append on two more economic fundamentals and one more economic change variable. The fundamentals are housing-market conditions, homeownership rate and median home value, derived from the 2000 Census summary file, which we accessed on IPUMS NHGIS.<sup>15</sup> The econoimc change is the Great Recession unemployment shock, which we source from Yagan (2019) and describe further in Section 4.2. In total, we consider 19 covariates. Of the 3,133 counties for which we have nonmissing mobility measures, 2,473 of them have a fully nonmissing set of covariaties. We consider this subsample throughout the rest of the paper. 

For ease of comparison across the variables, and following Chetty et al. (2014), we normalize all variables to have mean 0 and standard deviation 1 across counties. Thus, Γ coefficients from Equation (4) describe the mobility response to a one-standard deviation change in the given variable. Although these responses are not causal, they provide some indication of which variables may be most important in targeting economic opportunity. They may also suggest how different types of economic opportunities are related to different local circumstances. 

## **4.1. Exploratory analysis of demographic, economic, and social variables** 

Tables 3 and 4 report bivariate estimates of Equation (4) for each of the 19 variables. We start with Table 3, which considers absolute mobility ( _α_ ). The results show that most variables are economically significant predictors of most absolute mobility measures. However, there are some interesting within-variable differences. For example, the local marriage rate is strongly predictive of homeownership and gross wealth mobility, but is not significantly 

> 14When the given characteristic is measured at the commuting zone level, we merge it to our county-level mobility data based on the commuting zone in which each county lies. 

> 15 `https://data2.nhgis.org/main` . 

16 

associated with income mobility. The fraction Black is more strongly negatively associated with total income and wealth mobility than it is with housing wealth mobility. County median home values negatively predict absolute mobility in homeownership but are strongly positively associated with housing wealth and income mobility. In contrast, higher prevailing homeownership rates are strongly associated with absolute mobility of homeownership, but less so for income and housing wealth measures. Variables such as income segregation and violent crime strongly negatively predict homeownership mobility and wealth mobility, but are less associated with other economic concepts. 

We present partial _R_<sup>2</sup> ’s to help summarize the relationship of the various categories of local characteristics to different mobility measures. Demographic variables account for over 60% of cross-county variation in income mobility, but only around 30% of variation in housing wealth and homeownership mobility. Alternatively, economic fundamentals explain 40% of cross-county variation in homeownership mobility but 15-30% of variation in other mobility concepts. The other sets of factors also each explain a considerably larger share of variation in homeownership mobility than in other economic concepts, including for factors related to economic inequality and social forces. Overall, the full set of variables explains half of cross-county variation in housing wealth mobility, and 70%-75% of variation in other economic mobility concepts. 

Some of the same conclusions can be found in Table 4 as well, which reports associations between county characteristics and relative mobility ( _β_ ). Fraction married is still strongly associated with relative mobility of wealth but weakly associated with relative mobility of income. Income segregation is still strongly negatively associated with wealth mobility but less so with income mobility. The fraction Black and the Gini coefficient remain strong predictors of mobility. However, relative mobility is generally less well-explained by these county characteristics than is absolute mobility. The partial and overall _R_<sup>2</sup> values are nontrivially lower in this table than in the previous one, especially for the homeownership outcome. 

Figures 9 and 10 hone in on 5 of these covariates: Gini coefficient, income segregation, 

17 

labor-force participation rate, median home value, and fraction Black. To assess robustness of the bivariate results, we estimate multivariate models in which we control for all other variables outside of the given variable’s category. For example, we estimate Gini coefficient responses in which we hold constant demographics, economic fundamentals, economic changes, public investment, and social forces. We cycle through all 5 variables in this manner and plot the multivariate responses of each economic mobility measure as bars on the figure, with confidence intervals appearing as whiskers. 

– Looking at the two figures together, the Gini coefficient a leading measure of income – inequality is the textbook example of a variable that strongly (negatively) predicts economic mobility, regardless of mobility measure or economic concept. This “Great Gatsby” relationship has previously been identified in cross-national comparisons of income mobility (e.g. Corak, 2013) and in the Chetty et al. (2014) cross-county analysis of the US. Our results show that this relationship applies to wealth and housing measures of economic status as well. 

On the other hand, the other variables in the figures are candidate examples of variables that shape different mobility measures differently. For example, income segregation is not a significant predictor of homeownership or labor income mobility, but it is negatively – correlated with housing wealth and total wealth mobility especially the relative mobility measure. These results suggest that access to well-paying jobs may not be the primary mechanism through which residential segregation shapes economic mobility. We also find that the local labor-force participation rate (LFPR) is not significantly associated with income mobility, but is strongly predictive of upward wealth mobility and also moderately associated with relative wealth mobility. This result suggests that LFPR may signal more than just labor-market conditions, but also relate to inclusive social institutions and family investment preferences (see Chetty et al., 2026a for further discussion on this). 

As alluded to earlier, we find that areas with more expensive homes exhibit more upward mobility of wealth. However, this price mechanism discourages upward mobility of home- 

18 

ownership, highlighting the importance of considering the supply of housing when investing in local amenities and schools. Finally, we see that the fraction Black in an area is strongly negatively associated with income mobility, but is more ambiguously associated with wealth and homeownership mobility. 

## **4.2. Great Recession shock** 

In this subsection, we study how exposure to the Great Recession shaped intergenerational mobility patterns, with particular attention to differences across economic concepts. The timing of our underlying data is well-suited to such an exploration. We observe parents’ economic resources around 2000, before the housing bubble formed, collapsed, and caused a financial crisis in its wake. We observe children’s resources in adulthood in 2019-2021, following a long and sluggish recovery of the labor market. The average child in our sample was 39 years old in 2020, and thus spent their early career in this weak labor market. Combined with the potential loss of parental wealth during the recession and tightened lending standards thereafter, these disruptions may have affected children’s abilities to accumulate housing wealth. At the same time, home prices rapidly rebounded and continued to increase as these children reached typical home-buying ages, making housing a valuable investment for those able to afford it. 

As previously shown by Yagan (2019), there was substantial geographic variation in the severity of the Great Recession shock, allowing us to use cross-area regression (4) to test for downstream associations between the recession and economic mobility. While these associations are not necessarily causal, Yagan (2019) argued that the geographic distribution of shock severity was unrelated to local labor market trends. We take our estimates, particularly those that control for the host of pre-Recession covariates mentioned above, as indicative of the long-run effects of the Great Recession on Millennial children’s economic mobility. 

As our measure of the severity of the local shock, we use the county-level labor market 

19 

shock as in Yagan (2019), defined as the percentage point change in the unemployment rate from 2007-2011, roughly the peak to trough of the national labor market cycle. For our regression analyses, we standardize this measure to have mean 0 and standard deviation of 1, as in the previous analyses. 

Table 5 presents estimates of the relationship between the local recession shock and absolute mobility ( _α_ ) and relative mobility ( _β_ ) parameters for various resource measures. The top set of rows shows coefficients from bivariate regressions, and to explore the robustness of the correlations the second set of rows presents coefficients from multivariate regressions that includes controls for each of the variables presented in Tables 3 and 4. For all measures, we see that a more severe local shock is associated with lower absolute mobility – children of parents at the bottom of the distribution from more exposed counties have significantly lower homeownership rates, income and wealth than those from less exposed counties. 

On the other hand, the associations with relative mobility ( _β_ ) differs across resource measures. Differential exposure to local shocks has no association with the relative mobility – of income, but is associated with lower intergenerational mobility (higher _β_ ) for wealth in locations that were more exposed to the local shock, there is a steeper gradient between the wealth of children that were born to parents at the bottom and top of the distribution. 

Combing the magnitudes from the _α_ and _β_ estimates provides further context. For the income measures, more exposed locations experienced approximately level shifts down in the rank-rank slope, implying similarly lower average outcomes (by _α_ amount) for children regardless of where there parents were in the distribution. In contrast, for the wealth measures – the estimates imply a pivot of the rank-rank relationship the differences in average wealth for children of parents at the bottom of the distribution are significantly larger than they are for differentially exposed children from the top of the distribution. In fact, given the estimated values of the differences in _α_ and _β_ , the estimates suggest that children of parents at the top of the wealth distributions had very similar wealth outcomes on average regardless of how exposed to the local recession shock, whereas those of parents at the bottom had 

20 

significantly lower wealth on average.<sup>16</sup> 

While these relationships are descriptive rather than causal, they point to how neighborhood characteristics or local shocks could differentially impact intergenerational mobility of income and wealth. As found in Yagan (2019), local shocks were associated with long-run scarring. Parent inputs into human capital may be most important earlier in a child’s life. The children in this sample would have largely finished their education, but were starting their career trajectories at the time of the shock (they were turning 30 between 2008 and 2016). The relatively large reductions in average income that may be associated with this scarring. On the other hand, the influence of parents on the ability of children to acquire (valuable) homes may happen later, around the time of purchase (through direct financial assistance or knowledge). While children of parents from the bottom of the distribution experienced worse housing outcomes on average, those of parents higher in the distribution were had similar housing outcomes independent of the local exposure to the recession shock. 

# **5. Conclusion** 

In this paper, we have produced novel statistics on the distribution of economic mobility across U.S. counties, leveraging a new linked dataset of 3.4 million families and their wealth and income records across multiple generations. These statistics enable researchers to compare and contrast known facts about total income mobility and its spatial distribution with an internally consistent set of facts regarding other important economic outcomes such as labor income, housing wealth, homeownership, and total wealth. 

We have documented a set of spatial patterns in mobility and correlations between local economic and social characteristics and mobility measures that that differ across resource – concepts. These results are still incomplete along a few dimensions gaps which we believe can be filled in future work with expanded access to administrative data and a broader set of methods. First, we consider only rank-based statistics of intergenerational mobility, while 

> 16To approximate the difference at the top of the distribution, we use the formula _α_ +100 _∗_ (1 _− Pr_ ( _EM_ )), invoking the notation from Section 2.3. 

21 

other measures (e.g. “are you better off than your parents?”) may be of interest to some audiences. Second, our wealth results are incomplete—in both the sense that they omit assets not visible to the income or property tax systems, and in the sense that they cover only assets and not debts. Finally, our measurement of housing wealth covers only properties held directly by individuals, and potentially misses wealth held via pass through entities or limited liability companies. 

We believe these statistics have the potential to deepen our understanding of the processes underlying the intergenerational transmission of economic resources. As such, all the countylevel statistics described in this paper will be made available as a data appendix on the US Census Bureau website, freely available for subsequent research projects. There are many other potential determinants of economic mobility than the exercises engaged in this paper – our hope is that these county-level statistics will empower researchers to document these patterns more fully. 

22 

# **References** 

- Angelini, V. and I. Ferrari (2025): “Long-term effects of economic depressions on wealth,” _The Scandinavian Journal of Economics_ , n/a. 

- Binder, A., M. Risch, and J. Voorheis (2025): “Housing Capital and Intergenerational Mobility in the United States,” _Center for Economic Studies Working Paper Series_ . 

- Binder, A., C. Walker, M. Murray-Close, and J. Eggleston (2022a): “Race and Mobility in U.S. Marriage Markets: Quantifying the Role of Segregation,” Working Paper 22-59, Center for Economic Studies. 

- Binder, A. J., E. Molfino, and J. Voorheis (2022b): “Comparing the 2019 American Housing Survey to Contemporary Source of Property Tax Records: Implications for Survey Efficiency and Quality,” _JSM Proceedings_ , Survey Methods Research Section, 1487–1541. 

- Black, S. E., P. J. Devereux, F. Landaud, and K. G. Salvanes (2023): “Where Does Wealth Come From? Measuring Lifetime Resources in Norway,” _Journal of Economic Perspectives_ , 37, 115–36. 

- Bond, B., J. D. Brown, A. Luque, and A. O’Hara (2014): “The Nature of the Bias When Studying Only Linkable Person Records: Evidence from the American Community Survey,” _Center for Administrative Records Research and Applications Working Paper_ . 

- Chetty, R., W. Dobbie, B. Goldman, S. R. Porter, and C. S. Yang (2026a): “Changing Opportunity: Sociological Mechanisms Underlying Growing Class Gaps and Shrinking Race Gaps in Economic Mobility,” _The Quarterly Journal of Economics_ , 141, 1137–1210. 

- Chetty, R., J. N. Friedman, N. Hendren, M. R. Jones, and S. R. Porter (2026b): “The Opportunity Atlas: Mapping the Childhood Roots of Social Mobility,” _American Economic Review_ , 116, 1–51. 

- Chetty, R. and N. Hendren (2018a): “The Impacts of Neighborhoods on Intergenerational Mobility I: Childhood Exposure Effects,” _The Quarterly Journal of Economics_ , 133, 1107–1162. 

- ——— (2018b): “The Impacts of Neighborhoods on Intergenerational Mobility II: County-Level Estimates,” _The Quarterly Journal of Economics_ , 133, 1163–1228. 

- Chetty, R., N. Hendren, M. R. Jones, and S. R. Porter (2020): “Race and Economic Opportunity in the United States: an Intergenerational Perspective,” _The Quarterly Journal of Economics_ , 135, 711–783. 

- Chetty, R., N. Hendren, P. Kline, and E. Saez (2014): “Where is the land of Opportunity? The Geography of Intergenerational Mobility in the United States,” _The Quarterly Journal of Economics_ , 129, 1553–1623. 

- Chyn, E. and L. F. Katz (2021): “Neighborhoods Matter: Assessing the Evidence for Place Effects,” _Journal of Economic Perspectives_ , 35, 197–222. 

- Corak, M. (2013): “Income Inequality, Equality of Opportunity, and Intergenerational Mobility,” _Journal of Economic Perspectives_ , 27, 79–102. 

23 

- Fagereng, A., L. Guiso, D. Malacrino, and L. Pistaferri (2020): “Heterogeneity and Persistence in Returns to Wealth,” _Econometrica_ , 88, 115–170. 

- Gee, G., J. Goldin, J. Gray-Hancuch, I. Lurie, and V. Vohra (2024): “The Claiming of Children on U.S. Tax Returns,” Working Paper 33277, National Bureau of Economic Research. 

- Layne, M., D. Wagner, and C. Rothhaas (2014): “Estimating record linkage false match rate for the Person Identification Validation System,” _Center for Administrative Records Research and Applications Working Paper_ . 

- Malmendier, U. and S. Nagel (2011): “Depression Babies: Do Macroeconomic Experiences Affect Risk Taking?” _The Quarterly Journal of Economics_ , 126, 373–416. 

- Oreopoulos, P., T. von Wachter, and A. Heisz (2012): “The Short- and Long-Term Career Effects of Graduating in a Recession,” _American Economic Journal: Applied Economics_ , 4, 1–29. 

- Pfeffer, F. T. and A. Killewald (2017): “Generations of Advantage. Multigenerational Correlations in Family Wealth,” _Social Forces_ , 96, 1411–1442. 

- Piketty, T. (2014): _Capital in the Twenty-First Century_ , The Belknap Press of Harvard University Press. 

- Piketty, T., E. Saez, and G. Zucman (2018): “Distributional national accounts: methods and estimates for the United States,” _The Quarterly Journal of Economics_ , 133, 553–609. 

- Rinz, K. (2022): “Did Timing Matter? Life Cycle Differences in Effects of Exposure to the Great Recession,” _Journal of Labor Economics_ , 40, 703–735. 

- Saez, E. and G. Zucman (2016): “Wealth Inequality in the United States since 1913: Evidence from Capitalized Income Tax Data,” _The Quarterly Journal of Economics_ , 131, 519–578. 

- Schwandt, H. and T. von Wachter (2019): “Unlucky Cohorts: Estimating the Long-Term Effects of Entering the Labor Market in a Recession in Large Cross-Sectional Data Sets,” _Journal of Labor Economics_ , 37, S161–S198. 

- Smith, M., O. Zidar, and E. Zwick (2022): “Top Wealth in America: New Estimates Under Heterogeneous Returns,” _The Quarterly Journal of Economics_ , 138, 515–573. 

- Stuart, B. A. (2022): “The Long-Run Effects of Recessions on Education and Income,” _American Economic Journal: Applied Economics_ , 14, 42–74. 

- Wolff, E. N. (2017): _A century of wealth in America_ , Harvard University Press. 

- Yagan, D. (2019): “Employment Hysteresis from the Great Recession,” _Journal of Political Economy_ , 127, 2505–2558. 

24 

# **Tables and Figures** 

Table 1: Geospatial Summary Statistics, Intergenerational Economic Mobility Measures 

|Economic Resource|Mobility Measure|County Mean|County SD|
|---|---|---|---|
|Homeownership|Absolute Mobility (_α_)|55.37|26.00|
|Homeownership|Relative Mobility (_β_)|0.4122|0.2354|
|Homeownership|Extensive Margin/Renter Mobility (_δ_)|-8.25|14.33|
|Gross Housing Wealth|Absolute Mobility (_α_)|38.3|12.54|
|Gross Housing Wealth|Relative Mobility (_β_)|0.3474|0.2085|
|Gross Housing Wealth|Extensive Margin/Renter Mobility (_δ_)|-0.2122|8.16|
|Gross Total Wealth|Absolute Mobility (_α_)|40.16|11.64|
|Gross Total Wealth|Relative Mobility (_β_)|0.3254|0.1489|
|Gross Total Wealth|Extensive Margin/Renter Mobility (_δ_)|5.315|9.831|
|Labor Income|Absolute Mobility (_α_)|37.4|12.61|
|Labor Income|Relative Mobility (_β_)|0.3284|0.1777|
|Labor Income|Extensive Margin/Renter Mobility (_δ_)|10.29|7.95|
|Total Income|Absolute Mobility (_α_)|33.7|13.61|
|Total Income|Relative Mobility (_β_)|0.3287|0.1554|
|Total Income|Extensive Margin/Renter Mobility (_δ_)|||



Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: this table shows the average and standard deviation across counties of the three mobility concepts ( _α_ , _β_ and _δ_ ) for our five measures of family resources. The underlying _N_ is 3,004 counties for Gross Total Wealth and 3,133 counties for all other measures. 

25 

Table 2: Correlation Matrices of Intergenerational Economic Mobility Measures 

||Homeownership|Gross Housing Wealth|Gross Total Wealth|Labor Income|Total Income|
|---|---|---|---|---|---|
|**Panel A: Absolute M**|**obility** (_α_)|||||
|Homeownership|1.000|||||
|Gross Housing Wealth|0.629|1.000||||
|Gross Total Wealth|0.624|0.755|1.000|||
|Labor Income|0.601|0.753|0.791|1.000||
|Total Income|0.555|0.719|0.820|0.895|1.000|
|**Panel B: Relative M**|**obility** (_β_)|||||
|Homeownership|1.000|||||
|Gross Housing Wealth|0.677|1.000||||
|Gross Total Wealth|0.550|0.622|1.000|||
|Labor Income|0.522|0.405|0.443|1.000||
|Total Income|0.507|0.431|0.497|0.773|1.000|



Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: Entries are Pearson correlations estimated at the county level. Sample includes the 3,004 counties for which all mobility meaasures are nonmissing. 

26 

Table 3: Bivariate Regressions Across Resource Measures ( _α_ ) 

|||Dependent v|ariable: absolute mobi|lity (_α_)||
|---|---|---|---|---|---|
|Variable|Homeownership|Gross Housing Wealth|Gross Total Wealth|Labor Income|Total Income|
|**Demographics**||||||
|Percent Black|-3.215*** (0.462)|-2.086*** (0.310)|-3.487*** (0.260)|-2.799*** (0.340)|-3.694*** (0.392)|
|Percent Married|5.013*** (0.503)|0.550 (0.418)|1.740*** (0.378)|0.551 (0.520)|0.761 (0.584)|
|Teen Pregnancy Prevalence|-0.985** (0.496)|-2.154*** (0.257)|-3.431*** (0.207)|-4.244*** (0.199)|-4.510*** (0.188)|
|Percent Divorced|-0.521 (0.730)|-1.028*** (0.327)|-1.137*** (0.288)|-2.077*** (0.248)|-2.165*** (0.295)|
|Partial _R_<sup>2</sup>|0.326|0.286|0.427|0.617|0.611|
|**Economic Fundamentals**||||||
|Average HH Income|-2.498*** (0.321)|0.674* (0.356)|0.304 (0.243)|1.191*** (0.229)|1.180*** (0.282)|
|Labor Force Participation|0.782 (0.614)|1.361*** (0.301)|1.481*** (0.258)|1.395*** (0.322)|1.352*** (0.361)|
|Homeownership Rate, 2000|2.857*** (0.576)|-0.196 (0.273)|0.827*** (0.282)|0.700** (0.277)|0.615* (0.327)|
|Median Home Value, 2000|-2.280*** (0.536)|0.856*** (0.283)|0.643** (0.276)|1.272*** (0.291)|1.338*** (0.304)|
|Partial _R_<sup>2</sup>|0.408|0.154|0.193|0.295|0.232|
|**Economic changes**||||||
|In Migration Rate|-1.606*** (0.531)|0.087 (0.254)|0.180 (0.219)|-0.521** (0.238)|-0.452* (0.271)|
|2000-2010 Income Growth|1.851*** (0.497)|1.941*** (0.261)|2.833*** (0.243)|2.533*** (0.257)|3.217*** (0.287)|
|Recession Shock|-4.135*** (0.578)|-0.782* (0.409)|-1.520*** (0.342)|-1.325*** (0.320)|-1.494*** (0.404)|
|Partial _R_<sup>2</sup>|0.213|0.102|0.151|0.126|0.155|
|**Economic inequality**||||||
|Gini Coefcient|-3.819*** (0.372)|-0.947*** (0.354)|-2.083*** (0.381)|-1.847*** (0.389)|-2.026*** (0.450)|
|Fraction Middle Class|4.708*** (0.427)|0.737** (0.321)|2.069*** (0.348)|0.905** (0.411)|1.347*** (0.452)|
|Income Segregation|-4.123*** (0.470)|-0.048 (0.315)|-0.927*** (0.261)|-0.038 (0.315)|-0.198 (0.363)|
|Partial _R_<sup>2</sup>|0.499|0.082|0.232|0.214|0.198|
|**Public investment**||||||
|Efective Tax Rate|-2.023*** (0.591)|0.537 (0.384)|0.584* (0.313)|1.438*** (0.357)|1.603*** (0.398)|
|Local Government Spending|-3.327*** (0.918)|1.522*** (0.310)|1.394*** (0.209)|1.782*** (0.276)|2.044*** (0.303)|
|Student-Teacher Ratio|-3.157*** (0.440)|0.763*** (0.271)|0.452** (0.195)|0.614*** (0.216)|0.793*** (0.256)|
|Partial _R_<sup>2</sup>|0.278|0.097|0.045|0.090|0.098|
|**Social forces**||||||
|Social Capital|5.116*** (0.589)|1.096*** (0.370)|2.075*** (0.332)|2.023*** (0.375)|2.184*** (0.442)|
|Violent Crime Rate|-4.056*** (0.558)|-0.115 (0.381)|-1.068*** (0.383)|-0.590 (0.413)|-0.615 (0.484)|
|Partial _R_<sup>2</sup>|0.418|0.045|0.112|0.101|0.097|
|_R_<sup>2 </sup>full set|0.70|0.49|0.67|0.74|0.75|



Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. _Notes:_ This table shows estimates from linear bivariate regressions of county-level absolute mobility ( _α_ ) on one of 19 covariates. We consider the 2,473 counties that have nonmissing mobility measures and covariate values. All covariates are standardized to have mean 0 and standard deviation of 1 to allow comparability across measures. Each column reports results from mobility measures corresponding to different family resource concepts. While each coefficient is from a bivariate regression, below each grouped set of variables we report the adjusted _R_<sup>2</sup> from a multivariate regression that includes each variable in the group. The final row of the table reports the _R_<sup>2</sup> from a regression that includes the full set of variables included in the table. Standard errors clustered at the CZ level in parentheses. Significance levels: * p _<_ .1, ** p _<_ .05, *** p _<_ .01. 

27 

Table 4: Bivariate Regressions Across Resource Measures ( _β_ ) 

|||Dependent|variable: relative mobil|ity (_β_)||
|---|---|---|---|---|---|
|Variable|Homeownership|Gross Housing Wealth|Gross Total Wealth|Labor Income|Total Income|
|**Demographics**||||||
|Percent Black|0.035*** (0.005)|0.029*** (0.004)|0.027*** (0.003)|0.029*** (0.004)|0.034*** (0.003)|
|Percent Married|-0.011 (0.010)|-0.019** (0.008)|-0.025*** (0.004)|-0.006 (0.006)|-0.008* (0.005)|
|Teen Pregnancy Prevalence|0.031*** (0.005)|0.011*** (0.003)|-0.001 (0.003)|0.033*** (0.003)|0.028*** (0.002)|
|Percent Divorced|0.027*** (0.006)|0.015*** (0.005)|0.003 (0.004)|0.010*** (0.004)|0.007** (0.003)|
|Partial _R_<sup>2</sup>|0.220|0.118|0.143|0.285|0.324|
|**Economic fundamentals**||||||
|Average HH Income|0.000 (0.005)|0.012*** (0.005)|0.023*** (0.003)|-0.007** (0.003)|-0.004 (0.003)|
|Labor Force Participation|0.001 (0.006)|0.012*** (0.004)|0.016*** (0.003)|-0.007* (0.004)|-0.006* (0.003)|
|Homeownership Rate, 2000|0.002 (0.009)|-0.007 (0.010)|-0.012** (0.005)|-0.006 (0.005)|-0.006 (0.004)|
|Median Home Value, 2000|-0.010*** (0.003)|-0.002 (0.004)|0.008*** (0.002)|-0.013*** (0.003)|-0.009**|
|Partial _R_<sup>2</sup>|0.059|0.085|0.202|0.209|0.140|
|**Economic changes**||||||
|In Migration Rate|0.012*** (0.004)|0.007* (0.004)|-0.001 (0.003)|-0.003 (0.003)|-0.004 (0.003)|
|2000-2010 Income Growth|-0.034*** (0.004)|-0.031*** (0.004)|-0.029*** (0.003)|-0.021*** (0.003)|-0.020*** (0.003)|
|Recession Shock|0.017** (0.007)|0.009* (0.005)|0.010** (0.004)|0.001 (0.005)|0.000 (0.005)|
|Partial _R_<sup>2</sup>|0.095|0.080|0.096|0.066|0.072|
|**Economic inequality**||||||
|Gini Coefcient|0.018** (0.007)|0.024*** (0.007)|0.023*** (0.004)|0.017*** (0.006)|0.020*** (0.005)|
|Fraction Middle Class|-0.017*** (0.005)|-0.032*** (0.004)|-0.031*** (0.004)|-0.010** (0.004)|-0.016*** (0.004)|
|Income Segregation|0.010 (0.006)|0.024*** (0.006)|0.028*** (0.003)|0.002 (0.004)|0.005 (0.004)|
|Partial _R_<sup>2</sup>|0.063|0.182|0.283|0.125|0.178|
|**Public investment**||||||
|Efective Tax Rate|-0.009 (0.008)|0.009 (0.007)|0.011*** (0.004)|-0.008* (0.005)|-0.005 (0.004)|
|Local Government Spending|-0.014** (0.006)|-0.001 (0.005)|0.004 (0.004)|-0.021*** (0.004)|-0.018*** (0.004)|
|Student-Teacher Ratio|-0.004 (0.006)|-0.001 (0.005)|0.002 (0.004)|-0.015*** (0.003)|-0.014*** (0.002)|
|Partial _R_<sup>2</sup>|0.018|0.010|0.023|0.115|0.111|
|**Social forces**||||||
|Social Capital|-0.015** (0.007)|-0.013*** (0.005)|-0.005 (0.004)|-0.007 (0.005)|-0.008* (0.005)|
|Violent Crime Rate|0.006 (0.008)|0.007 (0.006)|0.010** (0.004)|0.000 (0.006)|0.003 (0.005)|
|Partial _R_<sup>2</sup>|0.016|0.017|0.026|0.010|0.015|
|_R_<sup>2 </sup>full set|0.36|0.41|0.52|0.53|0.59|



Source: 2019–2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994–2021 Census Databank. _Notes:_ This table shows estimates from linear bivariate regressions of county-level relative mobility ( _β_ ) on one of 19 covariates. We consider the 2,473 counties that have nonmissing mobility measures and covariate values. Covariates are standardized to mean 0 and SD 1. Standard errors clustered at the CZ level. Significance: * p _<_ 0.1, ** p _<_ 0.05, *** p _<_ 0.01. 

28 

Table 5: Local Recession Shocks and Intergenerational Economic Mobility 

||Homeownership|Gross Housing Wealth|Gross Total Wealth|Labor Income|Total Income|
|---|---|---|---|---|---|
|Bivariate||||||
|Absolute Mobility (_α_)|-4.135<sup>_∗∗∗_</sup>|-0.782<sup>_∗_</sup>|-1.520<sup>_∗∗∗_</sup>|-1.325<sup>_∗∗∗_</sup>|-1.494<sup>_∗∗∗_</sup>|
||(0.578)|(0.409)|(0.342)|(0.320)|(0.404)|
|Relative Mobility (_β_)|0.017<sup>_∗∗_</sup>|0.009<sup>_∗_</sup>|0.010<sup>_∗∗_</sup>|0.001|0.000|
||(0.007)|(0.005)|(0.004)|(0.005)|(0.005)|
|Multivariate||||||
|Absolute Mobility (_α_)|-1.315<sup>_∗∗∗_</sup>|-0.680<sup>_∗∗_</sup>|-0.937<sup>_∗∗∗_</sup>|-0.583<sup>_∗∗∗_</sup>|-0.886<sup>_∗∗∗_</sup>|
||(0.311)|(0.298)|(0.170)|(0.144)|(0.158)|
|Relative Mobility (_β_)|0.013<sup>_∗∗∗_</sup>|0.007<sup>_∗_</sup>|0.010<sup>_∗∗∗_</sup>|0.003|0.003|
||(0.005)|(0.004)|(0.003)|(0.002)|(0.002)|
|Observations|2,473|2 ,473|2,419|2,473|2,473|



Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

_Notes:_ This table shows estimates from linear regressions of county-level absolute mobility ( _α_ ) and relative mobility ( _β_ ) on county-level recession shocks as defined in Yagan (2019). These shocks are standardized to have mean 0 and SD 1. The first two rows present estimates of bivariate regressions of the indicated mobility measure on the recession shock. The last two rows show estimates of multivariate regressions that include as controls the other 18 covariates presented in Tables 3 and 4. Standard errors clustered at the CZ level in parentheses. Significance levels: * p _<_ 0.1, ** p _<_ 0.05, *** p _<_ 0.01. 

29 

Figure 1: Data Linkage Schematic 



<!-- Start of picture text -->
1994-2000 IRS Tax<br>Data (1040s, W2s)<br>Contains: Parent-Child<br>Links, Parent’s income<br>Parent PIK<br>Child PIK Child PIK<br>2000 Decennial<br>Census Long  Form<br>2019-2021 Black  Contains: Parent-Child  2019-2021 IRS Tax<br>Knight Property Tax  Links, Parent’s income,  Data (1040s, W2s,<br>Capitalized Parent<br>Data Wealth, Parent  and others)<br>Homeownership and<br>Contains: Child  Housing Wealth Contains: Child Labor<br>Homeownership, Child  Income, Child Total<br>Gross Housing Wealth Income, Child<br>Capitalized Wealth<br><!-- End of picture text -->

Notes: This figure shows a schematic for the data linkages described in Section 2. 

30 

Figure 2: County Level Map of Total Income and Labor Income _β_ Mobility 





(b) Total Income 

Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: These maps show the county-level variation in _β_ for total income and labor income, our measure of relative mobility for children of parents on the intensive margin (parents with the lowest non-zero amount of the resource concept in question). Cool colors correspond to higher relative mobility, warmer colors correspond to lower levels of relative mobility. 

31 

Figure 3: County Level Map of Gross Housing Wealth and Total Gross Wealth _β_ Mobility 





Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: These maps show the county-level variation in _β_ for gross housing wealth and total gross wealth, our measure of relative mobility. Cool colors correspond to higher relative mobility, warmer colors correspond to lower levels of relative mobility. 

32 

Figure 4: County Level Map of Extensive Margin Housing _β_ Mobility 



Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. Notes: These maps show the county-level variation in _β_ for extensive margin housing wealth, our measure of relative mobility . Cool colors correspond to higher relative mobility, warmer colors correspond to lower levels of relative mobility. 

33 

Figure 5: County Level Map of Labor Income and Total Income _α_ Mobility 





Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: These maps show the county-level variation in _α_ for total income and labor income, our measure of upward mobility for children of parents on the intensive margin (parents with the lowest non-zero amount of the resource concept in question). Cool colors correspond to higher upward mobility, warmer colors correspond to lower levels of upward mobility. 

34 

Figure 6: County Level Map of Gross Housing Wealth and Total Gross Wealth _α_ Mobility 





Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: These maps show the county-level variation in _α_ for gross housing wealth and total gross wealth, our measure of upward mobility for children of parents on the intensive margin (parents with the lowest non-zero amount of the resource concept in question). Cool colors correspond to higher upward mobility, warmer colors correspond to lower levels of upward mobility. 

35 

Figure 7: County Level Map of Extensive Margin Housing _α_ Mobility 



Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: These maps show the county-level variation in _α_ for extensive margin housing wealth, our measure of upward mobility for children of parents on the intensive margin (parents with the lowest non-zero amount of the resource concept in question). Cool colors correspond to higher upward mobility, warmer colors correspond to lower levels of upward mobility. 

36 

Figure 8: County Level Map of Gross Housing Wealth and Extensive Homeownership _δ_ Mobility 





Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: These maps show the county-level variation in _δ_ for housing wealth and total gross wealth, our measure of upward mobility for children of parents on the extensive margin (parents with the zero of the resource concept in question). Cool colors correspond to higher upward mobility, warmer colors correspond to lower levels of upward mobility. 

37 

Figure 9: Selected Correlates of Absolute Mobility ( _α_ ) 



Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: this figures shows estimates for selected covariates from a linear regression of county-level absolute mobility ( _α_ ) on county-level recession and housing price shocks, county and CZ characteristics from Chetty et al. (2014), and median home price and homeownership rate from the 2000 Long Form Decennial Census. All covariates are standardized to have mean 0 and standard deviation of 1 to allow comparability across measures. Each column reports results from a separate regression, with mobility measures corresponding to different family resource concepts. 

38 

Figure 10: Selected Correlates of Relative Mobility ( _β_ ) 



Source: 2019-2021 Black Knight property tax and deed records linked to 2000 Census Long Form and 1994-2021 Census Databank. 

Notes: this figures shows estimates for selected covariates from a linear regression of county-level relative mobility ( _β_ ) on county-level recession and housing price shocks, county and CZ characteristics from Chetty et al. (2014), and median home price and homeownership rate from the 2000 Long Form Decennial Census. All covariates are standardized to have mean 0 and standard deviation of 1 to allow comparability across measures. Each column reports results from a separate regression, with mobility measures corresponding to different family resource concepts. 

39 

