---
title: Broxterman-Larson-Yezer-2026-w35144
type: paper
source_pdf: raw/papers/Broxterman-Larson-Yezer-2026-w35144.pdf
converted: 2026-08-18
---

# NBER WORKING PAPER SERIES 

CHARACTERISTICS OF A SUFFICIENT STATISTIC TO MEASURE CITY HOUSING PRICES 

Daniel Broxterman William Larson Anthony Yezer 

Working Paper 35144 http://www.nber.org/papers/w35144 

NATIONAL BUREAU OF ECONOMIC RESEARCH 1050 Massachusetts Avenue Cambridge, MA 02138 April 2026 

Views and opinions expressed are those of the authors and do not necessarily represent official positions or policy of the Office of Financial Research, the U.S. Department of the Treasury, or the National Bureau of Economic Research. We are grateful for comments from participants at the NBER/CRIW Conference on Measurement of Housing and the Housing Sector, held in Alexandria, Virginia, on March 12–13, 2026, and to Tom Davidoff for his thoughtful discussant comments both before and during the conference. 

NBER working papers are circulated for discussion and comment purposes. They have not been peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies official NBER publications. 

© 2026 by Daniel Broxterman, William Larson, and Anthony Yezer. All rights reserved. Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, including © notice, is given to the source. 

Characteristics of a Sufficient Statistic to Measure City Housing Prices Daniel Broxterman, William Larson, and Anthony Yezer NBER Working Paper No. 35144 April 2026 JEL No. R14, R21 

# **<u>ABSTRACT</u>** 

Characterizing the level and change of housing prices in cities is central to many empirical questions, whether prices are measured using rents or asset values. The task is complicated by the heterogeneity of the housing stock, the joint consumption of housing and neighborhood, and differences in accessibility. This paper focuses on intra-city location which, based on economic theory, is systematically related to housing prices. The final conclusion is that a sufficient statistic to describe both the level of and change in the average housing price requires that prices be aggregated from relatively homogeneous market areas and weighted by housing quantities such as dwelling units or interior space. Common repeat-sales and hedonic indexes are generally not weighted in this fashion but could be modified to do so. 

Daniel Broxterman Florida State University Herbert Wertheim College of Business dbroxterman@fsu.edu 

Anthony Yezer The George Washington University Department of Economics yezer@gwu.edu 

William Larson U.S. Department of the Treasury Office of Financial Research larsonwd@gmail.com 

# **1. Introduction** 

Hedonic and repeat-sales indexes are the two principal approaches used in OECD countries to address the fundamental index-number problem of separating price change from quality change in metropolitan house price measurement. A substantial literature evaluates the strengths and limitations of these approaches and proposes econometric refinements to the empirical estimator. In contrast, this paper uses urban spatial theory to develop conditions under which an index recovers the average citywide price change. Spatial equilibrium imposes two distinct restrictions: one governing the aggregation of price changes within a city, and another governing the definition of the housing quantity to be indexed. We derive the first restriction in this paper and integrate the second from existing results. 

This paper shows that the iso-utility condition in the standard monocentric city model implies that housing price changes vary systematically with distance from the city center. Absent highly restrictive assumptions on preferences and transportation technology, appreciation rates cannot be spatially invariant. Empirical evidence is broadly consistent with this implication, documenting that housing price and rent dynamics vary substantially within metropolitan areas, including along center-to-suburban gradients (Ahlfeldt, Heblich, and Seidel 2023; Glaeser, Gottlieb, and Tobio 2012; Bogin, Doerner, and Larson 2019a; Bogin, Doerner, and Larson 2019b; Edlund, Machado, and Sviatschi 2022; Seagraves and Gatzlaff 2025). Spatial heterogeneity is also evident in responses to localized shocks: infrastructure investments, energy price changes, monetary policy shocks, and the COVID-19 pandemic have each generated pronounced within-city variation in appreciation patterns (Molloy and Shan 2013; Larson and Zhao 2020; Fischer et al. 2021; Liu and Su 2021; D’Lima, Lopez, and Pradhan 2022). BaumSnow and Han (2024) show that housing supply elasticity also varies substantially across census 

2 

tracts, consistent with the view that differential price responses in the demand shock literature may reflect systematic within-city differences in local supply conditions. 

When transaction probabilities are correlated with location-specific appreciation, standard citylevel house price indexes need not recover average citywide housing price change. We show that recovering this object requires constructing the index as a weighted aggregation of submarket price indexes, where submarkets satisfy an appreciation-homogeneity condition and aggregation weights are proportional to each submarket’s share of the housing stock. We use Laspeyres indexes for illustration, but the restrictions follow from spatial equilibrium rather than the econometric features of a particular estimator. Under these conditions, the resulting index constitutes a sufficient statistic for average citywide housing price change. 

In practice, standard house price indexes are not constructed in this way. Most hedonic and repeat-sales indexes estimate metropolitan-level appreciation using a single model applied to all transactions within the metro. Explicit geographic or compositional weighting is typically introduced only at higher levels of aggregation, such as when regional indexes are combined into a national series. When appreciation patterns differ systematically within a city and are correlated with transaction propensity, the resulting metropolitan estimate may reflect the spatial distribution of transactions rather than that of the housing stock. Such approaches therefore implicitly assume either that appreciation is spatially invariant within the city or that observed transactions are proportionally representative of the housing stock. Urban theory provides little justification for the former assumption, and transaction-based sampling provides no guarantee of the latter. Consequently, commonly used metropolitan indexes may fail to satisfy the sufficientstatistic conditions implied by spatial equilibrium unless explicit stock-based spatial weighting is imposed. 

3 

A second restriction imposed by spatial equilibrium concerns the definition of the housing quantity being indexed. Because housing services are not directly observable, empirical work must rely on measurable proxies. The prevailing practice is to index housing units. Urban spatial theory implies that this choice can affect measured responsiveness and appreciation patterns. Liu (2018) shows theoretically and empirically that, when housing consumption adjusts along the intensive margin, supply elasticity measured in square footage exceeds elasticity measured in housing units. In standard urban spatial models, household location choice is framed as a tradeoff between commuting costs and the price per unit of space, rather than the price per dwelling. This implies that unit-based indexes may understate supply responsiveness and overstate the price effects of demand shocks. 

Interior living space provides a tractable proxy for housing services. Space is observable, central to production costs, and closely tied to land use in standard urban models. Because unit size varies systematically across locations and over time, indexes based on housing units conflate price appreciation with shifts in the size distribution of the housing stock. Indexing interior space better isolates the price of housing on the intensive margin and is therefore more consistent with spatial equilibrium, except in applications focused narrowly on household formation. 

Implementation of these index-construction conditions requires confronting spatial heterogeneity in unit size. Unit size varies substantially across space, so price per room or per square foot may diverge markedly from unit-level prices. As well, rental prices are not observed for owneroccupied housing, and asset prices are not generally available for rental units. Because the distribution of rental and owner-occupied housing—and the distribution of unit sizes—is highly uneven within cities, aggregation that ignores these dimensions may fail to reflect the spatial distribution of housing services implied by theory. 

4 

These considerations may justify constructing separate indexes for rental and owner-occupied housing or choosing between indexes based on unit prices versus space prices. The appropriate approach is ultimately empirical and depends on city-specific characteristics, including the prevalence of rental housing and the degree of variation in unit size. Using publicly available data, this paper illustrates how these definitional choices affect housing price indexes across U.S. metropolitan areas. Although the empirical application focuses on the U.S., the underlying measurement issues apply broadly to city-level index construction in other countries. 

Complementary evidence indicates that measurement and aggregation choices materially affect inferred housing price appreciation. In rental markets, Ambrose, Coulson, and Yoshida (2023) show that rent growth measured using newly signed leases diverges sharply from estimates based on surveys of existing tenants. In owner-occupied markets, Anenberg and Laufer (2017) 

demonstrate that repeat-sales indexes constructed from contract prices can produce different appreciation paths than those based on closing prices. Most directly related, Contat and Larson (2024) show that alternative aggregation of tract-level repeat-sales indexes yields materially different citywide appreciation measures when submarket growth rates differ. These findings underscore that aggregation is not a secondary technical detail but central to accurate measurement. 

This paper makes three primary contributions. First, it derives sufficient-statistic conditions for metropolitan house price indexes from the standard monocentric city model of Alonso (1964), Mills (1967), and Muth (1969). Second, it shows that both spatial aggregation and the definition of the housing good (units versus space), together with tenure heterogeneity, affect the 

construction of theoretically consistent price indexes. Third, it presents empirical examples illustrating that aggregation consistent with theory yields materially different measures of 

5 

appreciation across metropolitan areas. Even modest differences in aggregation and quantity definition can meaningfully alter measured appreciation for individual cities. 

The remainder of the paper is organized as follows. The next section formalizes the sufficient statistic requirements for a Laspeyres index. Section 3 reviews the strengths and limitations of hedonic and repeat sales indexes. Section 4 shows that, under standard urban equilibrium conditions, price changes must be modeled as a function of distance from the city center and weighted by the housing stock at each distance band; deviations implicitly assume zero income elasticity of housing demand. Sections 5 and 6 present empirical comparisons that aggregate subindexes using theoretically justified weights, drawing on data from the American Housing Survey and the Federal Housing Finance Agency. These comparisons reveal substantial differences in appreciation by tenure and centrality. Section 7 concludes with implications for the empirical measurement of house price change. 

# **2. Sufficient Statistics for a Laspeyres Index** 

Housing price measures can be based on either rental or asset prices and the basis of quantity 

measurement can be the housing unit or housing services provided, i.e., a measure such as interior space which may be adjusted for quality. These details of measurement are consequential but not the focus of this paper. Regardless of the price or quantity measure chosen, the index number problems we identify are mathematically identical. 

Laspeyres (1871) would answer the index number problem for measuring the average housing price and its rate of change by recognizing that price and quantity vary with location and constructing a price index treating housing in each location as a distinct good, see also, Balk (2012). Let denote the city-level log price change of housing (rents or asset prices, ), and 𝑝𝑝 𝑟𝑟 𝑁𝑁 

6 

denote city-level housing units that are split into market areas each with housing units. The quantity of housing services is denoted as 𝑘𝑘∈𝐾𝐾ℎ. The geometric Laspeyres index is then, 𝑖𝑖∈𝐼𝐼 



This formulation is advantageous in the study of housing prices because the index can be calculated using price changes, , and weights that are based on home values, 𝑖𝑖,𝑘𝑘,𝑡𝑡 𝑖𝑖,𝑘𝑘,𝑡𝑡−1 × ℎ . This avoids requirements for data on the many dimensions of housing services, 𝑟𝑟 / 𝑟𝑟 𝑖𝑖,𝑘𝑘,𝑡𝑡−1 𝑖𝑖,𝑘𝑘,𝑡𝑡−1 𝑟𝑟which cannot be fully captured even in hedonic models because of unobservables. 

The sufficient statistic implications of Equation (1) are demanding: The marginal distributions of either both housing prices and quantities, or expenditures, over various distances, , must be known. 𝑘𝑘 

There are two assumptions that may simplify the computation of (1). First, if the percentage change in the price of housing is constant in expectation within , then and it 𝑖𝑖,𝑘𝑘,𝑡𝑡 𝑖𝑖,𝑘𝑘,𝑡𝑡−1 𝑘𝑘 follows from (1) that a sufficient statistic for measuring the rate of housing price increase in a 𝑘𝑘 𝑟𝑟 / 𝑟𝑟 = 𝜃𝜃 neighborhood is a measure of which may occur for any sample of houses within . Then, if 𝑘𝑘 the percentage change in the price of housing is constant in expectation across all 𝜃𝜃 , then 𝑘𝑘 𝑘𝑘 and it also follows from (1) that a sufficient statistic for measuring the rate of housing price 𝑘𝑘 𝜃𝜃 = 𝜃𝜃 increase is a measure of which may occur at any (Contat and Larson 2024). For example, in small cities with relatively flat appreciation gradients in many periods, this assumption may 𝜃𝜃 𝑘𝑘 

commonly hold. The spatial distribution of housing may vary, but it is not consequential to the computation of a sufficient statistic for measurement of the percentage change in housing cost. 

7 

A second assumption may also yield the targeted Laspeyres index. If the weights used in the index construction are proportional to , then the resulting index will be a geometric 𝑖𝑖,𝑘𝑘,𝑡𝑡−1 Laspeyres index. For example, this circumstance can occur if an index is calculated using 𝑤𝑤 observed transactions, and transaction shares are proportional to housing value shares.<sup>1</sup> 

The discussion thus far has assumed agreement on the fundamental nature of the housing good being priced. While it is common to construct indexes based on the price of housing units, this approach treats a highly heterogeneous good as uniform. However, the quantity of space in housing units varies substantially over time and across location. If the objective is to measure the price of housing units or housing space, not housing services, then the definitions of ℎ in the preceding equations should reflect units or interior square feet rather than value. The empirical examples in later sections will illustrate the importance of differences in weighting by measures of space, units, and value. 

# **3. Conventional House Price Indexes** 

Constructing a price index requires comparing prices for identical assets across time. In real estate markets, this task is complicated by two challenges. First, properties are highly heterogeneous, and many price-relevant attributes—especially locational amenities—are imperfectly observed, making it difficult to fully control for cross-sectional variation in quality. Second, even when the same property transacts multiple times, its price-determining 

characteristics may change over time due to depreciation, renovation, or alteration. Isolating true 

> 1 It should also be noted that if we assume ℎ is constant, the geometric Laspeyres gives a Tornquvist index. 𝑖𝑖,𝑘𝑘 

8 

market-wide price movements therefore requires accounting for both unobserved heterogeneity across properties and within-property quality change over time.<sup>2</sup> 

# **3.1 Weighted Repeat-Sales Methods** 

In the United States, residential property price indexes are overwhelmingly based on the repeatsales method, which addresses unobserved heterogeneity by comparing prices for the same unit across multiple transactions, under the assumption that unit characteristics are time invariant. A repeat-sales index is constructed by estimating a pooled regression of log price differences for repeat-sale pairs on time-period indicators that take the value +1 in the resale period, −1 in the original sale period, and zero otherwise. Because error variance increases with the interval between transactions, observations with longer holding periods are typically down-weighted to account for heteroskedasticity (Case and Shiller 1987; Calhoun 1996). The price index is recovered by exponentiating the estimated time-period coefficients. 

Although Bailey, Muth, and Nourse (1963, hereafter BMN) provide the foundational regression formulation of the repeat-sales estimator, the underlying structure is closely related to the geometric mean index proposed by Jevons (1865). The principal contribution of BMN is to 

demonstrate that price relatives from arbitrary combinations of periods can be embedded within a regression framework, producing a geometrically aggregated index. The adoption of repeat- 

2 An additional complication arises when transaction prices reflect the option value of land rather than the value of the existing structure. In dense or supply-constrained urban markets, properties are often purchased with the intention of demolition or substantial redevelopment, such that observed prices primarily capitalize land value, zoning constraints, and redevelopment options rather than current housing services—e.g., see Rosenthal and Helsley (1994); Clapp, Bardos, and Wong (2012); and Gedal and Ellen (2018). In these cases, price changes may reflect shifts in land or option values rather than market-wide housing appreciation, complicating interpretation of standard house price indexes. 

9 

sales house price indexes in the U.S. followed the seminal contribution of Case and Shiller (1987), which extended the BMN framework and established the methodology used in practice today.<sup>3</sup> 

The primary advantage of the repeat-sales approach is its minimal data requirements: only a property identifier, transaction price, and sale date are needed. To the extent that difficult-tomeasure attributes, such as locational amenities, are time invariant, their effects are differenced out by construction. However, repeat-sales indexes face several well-documented limitations. Most fundamentally, observed price changes between transactions may reflect unobserved quality evolution—depreciation, renovation, or alteration—rather than pure market appreciation, a threat to identification. 

Additional concerns relate to sample representativeness and temporal stability. Properties that transact repeatedly may differ systematically from the broader housing stock, giving rise to selection bias and limiting external validity. Moreover, because properties that sell only once do not contribute to estimation, a large share of transactions is excluded, reducing statistical efficiency, which becomes problematic in thin markets. Finally, because repeat-sale pairs are only observed upon resale, new transactions reveal information about past market conditions, resulting in continual historical revision of the index.<sup>4</sup> 

3 The realization that standard repeat-sales price indices are essentially Jevons indices invites analysis of the representativeness of the implicit transaction (and holding period) weighting in a house price index for a large area (e.g., city or state). Under certain proportionality and/or homogeneity conditions, these regression-based Jevons-like formulations may produce unbiased estimates of geometric Laspeyres or Tornqvist indices. 

4 A substantial literature developed following Case and Shiller (1987), that addresses sample selection bias and issues related to transaction interval. This literature is reviewed in Nagaraja, Brown, and Wachter (2014). Practitioner-oriented discussions of sample size and coverage issues 

10 

A further issue concerns the index-number characteristics of the repeat-sales estimator. The standard repeat-sales framework constitutes an elementary price index, meaning it aggregates price relatives across transactions without explicit expenditure or quantity weights. Because each transaction pair enters the regression as a single observation, the estimator implicitly assigns equal weight to price relatives, apart from interval-based adjustments. As Diewert (2012) notes, such elementary indices can be inconsistent with economic index theory unless strong proportionality or homogeneity conditions hold; Keynes (1930, 57) similarly criticized unweighted geometric indices for their lack of proportional weighting. In the housing context, this implies that standard repeat-sales indexes are transaction-weighted rather than weighted by the distribution of housing units or housing services, raising concerns about representativeness when constructing metropolitan or national measures of appreciation. 

To implement this adjustment in a repeat-sales framework entails partitioning the metropolitan area into mutually exclusive submarkets (e.g., distance bands, census tracts, or other geographically defined units), estimating standard repeat-sales indexes within each submarket, and then aggregating these subindexes using weights proportional to base-period housing quantities in each submarket. This produces a Laspeyres-consistent index when weights reflect the spatial distribution of the housing stock. 

The two primary U.S. indexes—the S&P Cotality (formerly CoreLogic) Case-Shiller Home Price Indices and the Federal Housing Finance Agency (FHFA) House Price Index (HPI)—are each released as suites of indexes spanning multiple levels of geographic aggregation. While 

appear in Eurostat (2013). Additional research examining index revision and temporal instability includes Clapp and Giaccotto (1999), Clapham et al. (2006), and Deng and Quigley (2008). 

11 

both indexes rely on repeat-sales methods to control for unobserved, time-invariant heterogeneity, they differ along several dimensions, including data coverage, the treatment of heteroskedasticity, and weighting schemes used to aggregate indexes. 

The FHFA HPI is constructed from repeat transactions of single-family homes financed with conforming mortgages that are purchased or securitized by Fannie Mae and Freddie Mac. Because the index relies exclusively on conforming mortgage transactions acquired by the GSEs, it excludes nonconforming (e.g., Alt-A, jumbo, and subprime) loans and cash purchases and therefore does not represent the full universe of housing transactions. Price changes are estimated using generalized least squares, with observations spanning longer intervals between transactions down-weighted to account for increasing error variance over time, resulting in a geometrically weighted index. The national index is formed by combining separate indexes for the nine Census divisions using fixed weights based on the distribution of the housing stock. See Calhoun (1996) for details. 

The S&P Cotality Case-Shiller indices are constructed from a wider set of arms-length housing transactions obtained from public deed records and are estimated using an arithmetic repeat-sales framework. Individual sales pairs receive weights proportional to the initial transaction value, with additional adjustments that account for greater dispersion in price changes over longer holding periods.<sup>5</sup> The national index is formed by aggregating the nine Census division indexes 

5 If expected appreciation were homogeneous across properties within a city, such weighting could improve efficiency. However, if appreciation varies systematically within metropolitan areas, interval-based weighting may amplify disproportionate representation of high-turnover submarkets, increasing ex ante bias. Case and Shiller (1987), Sagi (2021), and others document that real estate returns are correlated with holding periods. 

12 

using estimates of the aggregate value of the single-family housing stock, yielding a transactionvalue-weighted measure of house price dynamics. See S&P Dow Jones (2025) for details. 

Taken together, these features underscore that standard repeat-sales indexes rely on observed transaction pairs and implicitly treat those transactions as representative of the broader housing stock. This assumption is restrictive within metropolitan areas, where both transaction intensity and appreciation vary systematically across space. 

Existing repeat-sales indexes implicitly treat observed transactions as representative of the metropolitan housing stock, despite systematic intra-city variation in transaction intensity and appreciation rates. To address this limitation, metro-level indexes can be constructed by first estimating repeat-sales subindexes for neighborhoods defined by distance from the city center and then aggregating these subindexes using weights proportional to the housing stock at each distance. This approach aligns index construction with urban economic theory and provides a principled way to account for spatial heterogeneity in appreciation when measuring average citylevel price change. 

While repeat-sales indexes can, in principle, be estimated within geographic strata as recommended here, doing so raises feasibility and selection-bias concerns. Repeat-sales methods rely on a relatively small and non-random subset of properties that transact more than once, and further spatial disaggregation can quickly erode sample sizes and exacerbate resale selection 

13 

bias, implying that aggregation of such submarket indexes to the metropolitan level would likely require estimation at a lower temporal frequency.<sup>6</sup> 

# **3.2 Hedonic Regression Methods** 

With the exception of the United States, most OECD countries have demonstrated a preference for hedonic price indexes over repeat sales methods. Hedonic price indexes use regression techniques to estimate the implicit prices of the housing characteristics that contribute to a property’s value. Relative to repeat-sales methods, this approach is more data-efficient because it considers both single- and repeat-sale properties. Provided that sufficiently detailed data on property attributes are available, hedonic models can account for changes in quality at the property level, addressing the fundamental limitation inherent in repeat-sales approaches. 

The primary limitations of hedonic price indexes stem from their data and modeling requirements. Effective implementation requires comprehensive and consistently measured information on property characteristics, and empirical results may be sensitive to specification choices, including functional form and the selection of covariates.<sup>7</sup> This computational 

complexity tends to reduce transparency relative to simpler index construction methods, posing challenges for routine production by statistical agencies and comparisons across countries. 

According to the _Handbook on Residential Property Price Indices (RPPIs)_ (Eurostat 2013), the hedonic literature distinguishes three approaches to constructing constant-quality property price 

6 Although their analysis focuses on producing indexes for specific market segments rather than aggregating subindexes, Bogin, Doerner, and Larson (2019) provide a useful discussion of the tradeoff between temporal frequency and geographic granularity in repeat-sales estimation. 7 Sirmans, Macpherson, and Zietz (2005) and Owusu-Ansah (2011) provide helpful reviews and discussions on explanatory variables and functional forms. 

14 

indexes.<sup>8</sup> The time-dummy method estimates a pooled regression with period indicators that capture constant-quality price changes. The characteristic-pricing approach instead revalues a representative bundle of housing attributes using hedonic coefficients from different periods, producing Laspeyres-, Paasche-, or Fisher-type indexes depending on whether base-period characteristics, current-period characteristics, or a geometric mean of the two is held fixed. Lastly, the imputation approach operates at the level of individual properties rather than an average bundle, using hedonic coefficients to predict counterfactual prices across periods: imputing base-period prices for current-period properties corresponds to a Laspeyres-type index, current-period prices for base-period properties yields a Paasche-type index, and a symmetric combination produces a Fisher-type index.<sup>9</sup> 

The RPPI Handbook contemplates stratification (also called mix adjustment) to reduce sample 

selection bias arising from compositional change in observed housing transactions.<sup>10</sup> Under this 

> 8 The _RPPI Handbook_ was developed under the coordination of the Statistical Office of the European Union (Eurostat) to establish international standards and published jointly by Eurostat, the International Labor Organization (ILO), the International Monetary Fund (IMF), the Organization for Economic Co-operation and Development (OECD), the United Nations Economic Commission for Europe (UNECE), and the Inter-Secretariat Working Group on Price Statistics (IWGPS) at the World Bank. 

9 The time-dummy hedonic approach, while simple and widely used, relies on restrictive assumptions—most notably time-invariant characteristic prices—and offers limited scope for transparent and economically meaningful weighting. By contrast, Silver (2018) shows that, under consistent choices of functional form and aggregation, the characteristics/repricing and imputation approaches can yield numerically equivalent Laspeyres-, Paasche-, and Fisher-type indexes. On this basis, Silver (2018) argues that the practical choice between hedonic approaches is less about correctness per se and more about transparency, weighting, and how individual transactions enter the index, ultimately favoring weighted imputation, or the equivalent characteristics-based formulation, over time-dummy methods. 

10 For example, the text is direct about misspecification from pooling heterogeneous markets, e.g., “When using hedonic regression techniques to adjust for quality (mix) changes, stratification is highly recommended. It is very unlikely that a single hedonic model holds true for all market segments, hence separate regressions should be run for different types of properties, different locations, etc.” (p. 55). 

15 

approach, properties are partitioned into relatively homogeneous strata—such as by location, dwelling type, or size—price change is measured within each stratum, and the resulting subindexes are aggregated using explicit weights. The arguments advanced here are theory-based rather than data-driven and suggest stratification based on location within the city. The reason for this conclusion is that rates of change in hedonic prices should not be uniform across locations. This same argument suggests that using time dummies from pooled hedonic equations will not produce equivalent results. 

In a hedonic framework, the same principle can be implemented either by estimating separate hedonic models within spatial strata and aggregating the resulting submarket price indexes using stock-based weights, or incorporating spatial interactions (e.g., location-specific time effects) and then reweighting predicted price changes using the spatial distribution of housing quantities. In both cases, the key requirement is that aggregation reflects the joint distribution of housing characteristics and location rather than the distribution of observed transactions. 

# **4. Urban Spatial Theory and Sufficient Housing Price Statistics** 

Section 2 suggests that if the percentage change in housing price is not a function of location, then measurement of housing price change does not require a spatially random measure of housing prices. In this case, it is not necessary to account for spatial differences in housing density or differences in location where housing price change is measured. Accordingly, the measurement of housing prices can be geographically concentrated. This section considers the relation between this assumption of constant rates of price change across space and standard urban economic theory. Specifically, under what circumstances is it reasonable to expect that the rate of change in house prices in cities is not a function of location? 

16 

In a neoclassical city, such as the classic monocentric model reviewed by Brueckner (1987), households achieve an iso-utility equilibrium from consumption of a composite commodity, , whose price is normalized to unity and constant throughout the city, and housing, ℎ, with price, 𝑐𝑐 . Each of these values vary by location which is expressed as the distance from the CBD, . 𝑟𝑟Households must either commute to a city center where they earn income, , or commute shorter 𝑘𝑘 distances where they face an urban wage gradient which is reduced by the amount of commuting 𝑦𝑦 cost saved. Therefore, the households’ problem is to 



where is commuting cost per unit distance. 𝜏𝜏 The iso-utility of households implies that d d is determined by Muth’s (1969) equation requiring that d d d d . The only general constraint on d𝑟𝑟/ 𝑘𝑘 d is the logical requirement that it is greater than zero; however, the further simplification that it is constant will 𝑟𝑟/ 𝑘𝑘= −( 𝜏𝜏/ 𝑘𝑘)/ℎ 𝜏𝜏/ 𝑘𝑘 be maintained here.<sup>11</sup> Housing consumption, ℎ, is determined by the iso-utility condition and earnings. 

The essential question of determining a sufficient statistic for measuring house price change 

reduces to a simple question: What constraint does Muth’s equation and the requirement that (d d constant place on the housing demand function? 𝑟𝑟/ 𝑘𝑘)/𝑟𝑟= = 𝜃𝜃 

> 11 The units of d d must be chosen so that they are consistent with the measurement of rental price. This issue has been discussed extensively in the literature. The simplification that this measure is not a function of location is adopted here because if that is not true, it would further 𝜏𝜏/ 𝑘𝑘 complicate the measure of housing price differences as discussed below. 

17 

Dividing through Muth’s equation by yields 𝑟𝑟 



But this implies that for both Muth’s equation and (d d constant to hold, then 𝑟𝑟/ 𝑘𝑘)/𝑟𝑟= = 𝜃𝜃 (d d d d . 𝑟𝑟/ 𝑘𝑘)/𝑟𝑟= −( 𝜏𝜏/ 𝑘𝑘)/𝑟𝑟ℎ= 𝜃𝜃 



Thus, for the percentage change in the rental price of housing to be constant across all locations and be consistent with Muth’s equation, the ratio of the marginal rise in transportation 𝑘𝑘≤𝑘𝑘cost with distance to total housing expenditure must be constant.<sup>∗</sup> 

**Proposition 1** . _If commuting cost per mile is constant and the iso-utility_ 

_condition of households holds, constancy of the elasticity of housing price change with distance from the city center implies that the household utility function must be quasi-linear._ 

Clearly if d d is constant, then total expenditure on housing must be constant. If the price of the composite commodity does not vary systematically with location, as is commonly assumed, 𝜏𝜏/ 𝑘𝑘 this implies that the utility function of households takes a specific quasi-linear form, 



Maximization of (5) as constrained in (2) produces a housing demand function in which 





18 

which satisfies the criterion in (4) that both the marginal increase in commuting cost with distance and total housing expenditure do not vary with location. Thus, Proposition (1) is proved. 

**Proposition 2** . _The assumption of iso-utility that is not quasi-linear implies that a sufficient statistic for constructing a Laspeyres index of price change in a city_ 

_requires that rates of price change be measured as a function of distance from the city center and weighted by the fraction of housing at each distance interval._ 

This proposition follows directly from Proposition (1), the empirical evidence on demand for a primary residence, and the definition of a Laspeyres index from Equation (1) and so no proof is given.<sup>12</sup> 

This section shows that spatially constant appreciation arises only under a joint structure linking preferences and commuting costs. Muth’s equation implies that a constant proportional rent 

gradient requires the ratio of marginal commuting cost to total housing expenditure to be invariant with distance. This condition obtains when commuting costs are linear in distance and preferences eliminate income effects, implying constant housing expenditure across locations. Both conditions are needed and both are restrictive. 

On the preference side, spatially constant appreciation requires that income effects in housing demand are absent. Quasi-linearity delivers this property, but primarily as a tractable benchmark 

12 Related theoretical work reinforces these implications. Broxterman, Liu, and Yezer (2026) show that housing supply elasticity varies systematically with intra-urban location, linking observed price responses to underlying spatial structure. 

19 

rather than as an empirically plausible description of housing demand. Empirical work instead points to positive income effects, although estimates of the income elasticity vary.<sup>13</sup> 

On the commuting cost side, departures from linearity break the proportional mapping between distance and marginal cost required for a constant rent gradient. Characterizing the resulting implications for price gradients generally requires numerical analysis. Existing work shows that incorporating features such as endogenous congestion only weakens the iso-elastic benchmark relative to the case of exogenous, constant commuting costs (Larson, Yezer, and Zhao 2022). Taken together, relaxing either condition leads generically to distance-dependent appreciation rates. 

# **5. An Illustration of Bias from Ignoring Spatial Heterogeneity** 

As a motivating empirical example, we use the American Housing Survey Metropolitan Sample (AHS-MS) to illustrate the potential effects of failing to consider spatial variation in constructing an index of city housing price changes. Both rental and asset prices are examined. Rental prices are important for measuring cost of living and value of current use, whereas asset prices also incorporate expectations and option value. The AHS-MS is well suited for this purpose for several reasons. First, it surveys households in both renter- and owner-units and classifies housing by central-city and suburban location. This allows comparison of price indexes by tenure status and centrality where differences are likely substantial. In addition, the AHS-MS is a panel 

13 A review of the literature finds estimates of housing’s income elasticity of demand ranging from 0.18 to 0.99 (Rosenthal, Duca, and Gabriel 1991; Hansen, Formby, and Smith 1996; Rapaport 1997; Glaeser, Kahn, and Rappaport 2008; Ioannides and Zabel 2008; Davis and Ortalo-Magné 2011; Albouy, Ehrlich, and Liu 2014). The estimates in these works cover rental and owner-occupied housing, and land for housing. 

20 

dataset, so that price changes can be calculated based on the same units in the same locations over time. As a result, changes in median values and rents can be interpreted as Laspeyres-like proxies under the approximation that the underlying set of sampled housing units is held constant over time. 

The central-city versus suburban location indicator within metropolitan areas is not available in the public-use microdata files of the AHS-MS. Accordingly, we rely on published summary tabulations, in which median values and rents are reported in interval form. To compute compound annual growth rates, we assign each reported interval its midpoint. This approach introduces substantial approximation error, and the resulting growth rates will not exactly match those constructed from the restricted micro-data. For the present illustrative purpose, however, the midpoint approximation provides a consistent basis for comparing growth across central-city and suburban locations. 

Using AHS-MS tabulations, we first measure changes in city house prices by calculating the annual growth rate in the median estimate of value and rent (both reported in ranges) based on all sample units in the metro area regardless of location. The results of this exercise are displayed in the first two columns of Table 1 for 25 U.S. cities for the years 2015 to 2019. This period was characterized by rapid growth in housing prices. The median value of owner-occupied homes grew at a compound annual rate ranging from 1.4% to 13.6%, with an average of 7.1%. For median rent, the range was 1.6% to 7.9%, with an average of 4.8%. 

***[Table 1 about here]*** 

Like most large-scale surveys, AHS-MS is a stratified sample. The nine sampling categories pertain primarily to tenure and structure type, not to location within the metropolitan area. The 

21 

survey weights are designed to match metropolitan-level totals published independently, but they do not necessarily recover the distribution of strata across within-metro locations. As explained in Section 2, this matters only if appreciation rates vary across tenure, location, or their 

interaction. In that case, measured citywide price change is a weighted average of group-specific appreciation rates and therefore depends on how the weighted sample represents those groups across space. Accordingly, we next examine growth rates of asset values and rents in the AHSMS separately for owner-occupied and renter-occupied units in the central city and the suburbs. Based on the literature cited in Section 1, 2015 to 2019 was a period during which centrality became a more highly valued amenity. Our first hypothesis is therefore that the growth rates of rental and asset prices reported in Table 1 differ between the central city and the suburbs. Columns three through six confirm substantial differences in rates of change across these two broad intra-metropolitan locations. Although the suburbs outperformed in some metros, average growth in asset values and rents was 137 and 15 basis points higher, respectively, in the central city, consistent with the pre-COVID urban resurgence narrative. 

The estimates in Table 1 therefore indicate that appreciation rates are not spatially invariant within cities. This matters for measurement because average citywide price change is a weighted average of group-specific growth rates. Taken to the logical extreme, an estimator based only on central-city units or only on suburban units would generally differ substantially from citywide appreciation. More generally, when growth rates vary across locations, accurate measurement requires that the weighted sample recover the spatial distribution relevant for the metropolitan housing stock. To the extent that the AHS-MS weights approximate that benchmark, of course, a weighted average of location-specific changes should approximate average citywide price change. 

22 

We next consider two alternative ways of characterizing housing price change at the metro level using annual growth rates in median value and rent from the AHS-MS. In the first construction, we simply average the rates for the central city and suburbs. These naïve indexes, which appear in the first two columns of Table 2, indicate that the median value of owner-occupied homes grew at an average of 7.8% and rents by 5.4% in the 25 cities covered. These results can be compared with the alternative index in columns three and four that weights the growth rates by all units, renter and owner, in each location as suggested by Proposition 2, which implies that a sufficient statistic for a Laspeyres index requires weighting location-specific price changes by the fraction of housing at each distance interval. 

***[Table 2 about here]*** 

The alternative index provides a useful reference point because it is consistent with well-known price index formulations. Differences between the alternative and simple average indexes appear in columns five and six of Table 2. On average, growth rates based on the alternative (sufficient statistic) index are 43 and 4 BPS lower, respectively, than their simple average analogs. (Relative to the metrowide growth rates in Table 1, values for the alternative indexes are 29 and 53 BPS higher.) For particular cities, the differences are much more substantial. For example, house price growth is 495 BPS lower in Atlanta and rent growth is 205 BPS lower in Pittsburgh relative to the simple average of the central city and suburbs rates for those metros. 

The median-based growth rates reported in Tables 1and 2 are not directly comparable to stratified or mix-adjustment methods described in Eurostat (2013). Instead, they should be interpreted as simple within-sample comparisons constructed using uniform definitions and procedures. This exercise illustrates that when appreciation rates vary systematically across locations and tenure types, failure to weight group-specific growth rates by the composition of 

23 

the metropolitan housing stock—as required by Proposition 2 for a Laspeyres-consistent index— can generate estimates that depart from average citywide price change. More generally, consistent measurement requires weights that recover the joint distribution of tenure and location in the metropolitan housing stock, rather than matching metropolitan totals. The differences shown in Table 2 underscore that the magnitude of this departure is not merely theoretical but quantitatively meaningful. More broadly, the results demonstrate that spatial heterogeneity is not a secondary refinement to index construction but a necessary component of any measure intended to sufficiently characterize aggregate price change within a city. 

# **6. The Sufficiency of the Weighted Repeat-Sales Index** 

The primary empirical illustration in this paper relies on the most widely used method for measuring city-level housing asset price changes in the U.S.: a weighted repeat-sales index estimated from transaction prices. Baum-Snow and Han (2024) document that repeat sales-based appreciation rates vary substantially across census tracts within the same city. They further demonstrate that estimates of housing price change and supply elasticity differ depending on whether they are based on housing units or interior space—findings consistent with the propositions advanced in this paper. Standard city-level index construction (e.g. FHFA or CaseShiller) using repeat-sales methods aggregates all available transaction pairs for the same housing unit and weights each pair’s price change by the time between transactions. This method, though ubiquitous, is _ex ante_ unlikely to be proportional to any relevant housing stock quantity measure, and thus to yield a Laspeyres index. Because Proposition 2 requires weights proportional to the spatial distribution of housing quantities, standard repeat-sales aggregation need not satisfy the sufficiency condition implied by spatial equilibrium. 

24 

Our strategy is to follow Contat and Larson (2024) and aggregate submarket appreciation rates using the geometric Laspeyres formulation. This requires a key assumption regarding submarket appreciation homogeneity. Equation (1) shows the city-level price index requires price relatives for each housing unit in the city. Under the assumption that housing units within each submarket appreciate at the same rate, in expectation, , can be estimated using any one of the classic 𝑘𝑘 BNM, Case-Shiller, or Jevons formulations, or some reasonable alternative. Then, these 𝜃𝜃<sup>�</sup> submarket appreciation rates are used to construct the geometric Laspeyres index, 



Because tract-level repeat-sales estimates are available for a large set of U.S. metropolitan areas (Contat and Larson 2024), this approach can, in principle, be implemented broadly by combining tract-level appreciation estimates with Census-based measures of housing quantities. Contat and Larson (2024) provide annual price changes for 63,122 census tracts across 581 core-based statistical areas from 1989 to 2021. These measures are designed to provide prices for 

exhaustive, mutually-exclusive submarkets within each city, making them well suited for aggregation based on spatial characteristics such as distance from the city center. Because these measures pertain exclusively to housing asset prices and do not include rental price changes, our empirical illustration focuses on how asset price appreciation responds to alternative aggregation schemes. This framework allows us to test whether different aggregation rules satisfy the sufficiency condition in Proposition 2. 

Census data provide information on the number of rental and owner-occupied units in each tract, as well as average unit size (in rooms) and reported value. Consequently, results for asset price 

25 

change weighted by total number of units versus those weighted by only owner or only renter aggregations can be evaluated and compared with Laspeyres-type aggregations weighted by measures of units, unit size, or value. 

These Census variables can be used to create different renditions of the Laspeyres price index under alternative definitions of housing quantities. In the neoclassical city, the quantity of housing is given by a single attribute, ℎ, the quantity of housing services. In real-world applications, however, housing is typically observed in two alternative ways: (1) In Leontief terms, with housing consumption represented simply as a unit; (2) along the intensive margin of the housing structure, as square feet. Each of these can be approximated using Census data on the number of units and size of units (via number of rooms). The housing services approach is possible via the traditional value-weighted formulation. 

# **6.1 Illustration of Index Differences** 

The effects of location and alternative measures of housing services are illustrated using examples from Boston and Houston. These cities represent opposite ends of the spectrum among large metropolitan areas in terms of rental share and land-use regulation. In Boston, nearly 65% of the housing stock is renter-occupied, compared to about 40% in Houston. Boston also enforces more restrictive planning policies, while Houston is known for its minimal regulatory environment. Given these contrasts, we expect not only differences in appreciation rates by location and housing service measure within each city, but also distinct spatial and temporal patterns between them. 

Figure 1 presents tract-level estimates of price appreciation for the full 1990-2020 period, as well as for two subperiods corresponding to the housing boom (2001-2006) and bust (2006-2011). 

26 

The maps display census tracts whose centroids fall within a 15-mile radius of each city’s City Hall. As expected, both cities exhibit substantial within-city variation in appreciation rates across census tracts across each time interval. 

***[Figure 1 about here]*** 

The temporal dynamics, however, differ markedly across the two cities. In Boston, the pattern is consistent with mean reversion: tracts that experienced the highest appreciation during the boom tended to see the steepest declines during the bust. This suggests that price increases in those areas outpaced fundamentals and were subsequently corrected. In contrast, Houston shows considerable persistence: tracts that appreciated more during the boom continued to outperform during the bust. This pattern is consistent with relatively elastic housing supply and more stable, fundamentals-driven price dynamics across neighborhoods. In both cases, the presence of systematic spatial gradients implies that aggregation weights correlated with tract characteristics will affect measured citywide appreciation, as predicted by the sufficiency condition. 

Figure 2 displays the share weights used to aggregate census tracts into city-level indexes for the two sample cities. These weights—based on the number of housing units, number of rooms, or total housing value—are derived from various Decennial Census American Community Survey datasets.<sup>14</sup> For both Boston and Houston, the spatial distributions of unit and room shares, shown in panels (a) and (b), are broadly similar, suggesting that appreciation rates weighted by these measures are likely to yield comparable results. In contrast, the value-based weights in panel (c) 

14 1990, 2000, and 2020 tract definitions are converted to 2010 definitions using crosswalk files available from the National Historical Geographic Information System at https://www.nhgis.org/geographic-crosswalks. For inter-census years, straight-line imputation is used for imputation. 

27 

exhibit a markedly different spatial pattern, indicating that indexes based on value weighting may diverge substantially from those based on physical housing characteristics. 

***[Figure 2 about here]*** 

Figure 3 presents estimates of annual and cumulative house price changes under the three alternative weighting schemes. An equally weighted index—constructed by averaging 

appreciation rates across tracts without regard to housing characteristics or value—is included for comparison. 

***[Figure 3 about here]*** 

Panels (a) and (c) show that annual appreciation rates are similar across weighting methods. However, this similarity does not extend to cumulative changes shown in panels (b) and (d): even small annual differences compound over time when appreciation patterns are persistent. The cumulative rate of appreciation varies materially with the choice of weighting scheme. Relative to equal weighting or weighting by number of units, room-weighted indexes tend to show lower cumulative appreciation, suggesting that larger (typically newer) units appreciated more slowly over the sample period. Value-weighted indexes exhibit greater volatility and diverge more sharply across cities, reflecting spatial differences in price levels. These differences arise precisely because the alternative weights place different mass on submarkets with systematically different appreciation rates, violating the aggregation restrictions required for sufficiency. 

# **6.2 Index Differences by City Type** 

Differences in index values across cities are highly associated with city attributes. Table 3 shows 

estimates of six models related to three different Laspeyres formulations, each with two different 

28 

samples. The alternative formulations include city-level aggregations of tract-level indices using housing units, rooms, and value, and these are compared to an index created using uniform tract weights. 

***[Table 3 about here]*** 

Across all three Laspeyres formulations, covariates indicative of large, growing cities are most highly associated with larger negative index gaps. Why is city size so impactful? Recall that index differences arise when (1) submarket appreciation rates differ and (2) aggregation weights are correlated with those differences (Malone and Redfearn 2022; Contat and Larson 2024). These are the two necessary conditions embedded in Proposition 2. 

Cities with relatively elastic and homogeneous housing stocks and uncongested commutes tend to have small index value differences (Bogin, Doerner, and Larson 2019). This tends to occur in small and medium-sized cities. By contrast, large and supply-inelastic cities exhibited negative appreciation gradients, with center-city housing appreciating faster than suburban housing. In such cities, weighting schemes that do not reflect the spatial distribution of housing quantities systematically mis-measure aggregate appreciation. 

In the case where appreciation gradients do exist, they indicate a correlation between high-valued tracts and appreciation, and higher average city value. Because new housing is more prevalent in suburban locations where appreciation is lower, unit-weighted indices produce less city-level appreciation, echoing results in the previous section using AHS data. New homes also tend to be larger, so when considering the intensive margin of housing, index differences become even 

29 

more apparent. Overall, these attributes combine to give negative gaps between a uniformweighted aggregation and each of the three Laspeyres formulations.<sup>15</sup> 

These results underscore the difficulty of constructing long-run repeat-sales indexes in cities with substantial spatial heterogeneity. Differences in appreciation rates across locations matter for aggregate measurement, and the choice of weighting scheme is consequential. 

Consistent with Proposition 2, a city-level price index constitutes a sufficient statistic only when appreciation is aggregated using weights proportional to the spatial distribution of housing quantities. In the presence of persistent spatial gradients, naive aggregation schemes—such as uniform tract weighting or transaction-based weighting—systematically depart from this condition. In the United States over the past three decades, such departures would have understated appreciation in large or supply-inelastic cities. 

# **7. Conclusions** 

Precise measurement of housing price changes, including both rental and asset prices, is critical for a wide range of research and practical applications. Over time, numerous refinements to commonly used hedonic and repeat sales index methods have been proposed. This research advances that effort by incorporating intra-city location and unit characteristics, which, 

according to both economic theory and empirical evidence, are systematically related to housing price. 

> 15 For regressions of individual covariates on index gaps, see Tables A.1, A.2, and A.3 in the Appendix. 

30 

Previous studies have shown that price changes are not uniform within cities. In particular, shifts in commuting cost—especially those associated with changes in gasoline prices or the introduction of new transportation infrastructure—have been shown to generate non-uniform appreciation patterns. This is the first paper to explore how basic urban economic theory can inform the construction of city-level housing price indexes. The results are that there are theoretical reasons, in addition to the empirical evidence, suggesting that rates of appreciation vary systematically with distance from the city center and that weighting observations by housing units produces different results than considering housing services. 

The implications for constructing Laspeyres-type indexes are clear. Given that appreciation rates vary across space, researchers must account for the spatial distribution of data used to create a housing price index. Whether that data come from survey responses or transactions, observations should be weighted by the fraction of housing services at each distance from the city center in order for the index to sufficiently characterize the average rate of change for that city. 

Conventional repeat sales and hedonic measures of price change are generally not weighted in this fashion. Fortunately, implementing such measures, particularly in repeat sales indexes, is straightforward when submarket-level price estimates can be combined with Census-based measures of housing quantities to construct stock-weighted aggregates. This process may result in meaningful changes to observed growth rates, as we illustrate using data for 25 U.S. cities from the Metropolitan Sample of the American Housing Survey and repeat sales price estimates for Boston and Houston. 

31 

# **References** 

Ahlfeldt, Gabriel M, Stephan Heblich, and Tobias Seidel. 2023. “Micro-Geographic Property 

Price and Rent Indices.” _Regional Science and Urban Economics_ 98: 103836. 

Albouy, David, Gabriel Ehrlich, and Yingyi Liu. 2014. “Housing Demand and Expenditures: 

How Rising Rent Levels Affect Behavior and Cost-of-Living over Space and Time.” University of Illinois Working Paper. 

Alonso, William. 1964. _Location and Land Use: Toward a General Theory of Land Rent_ . Harvard University Press. 

Ambrose, Brent W, N Edward Coulson, and Jiro Yoshida. 2023. “Housing Rents and Inflation 

Rates.” _Journal of Money, Credit and Banking_ 55 (4): 975–92. 

Anenberg, Elliot, and Steven Laufer. 2017. “A More Timely House Price Index.” _Review of Economics and Statistics_ 99 (4): 722–34. 

Bailey, Martin J, Richard F Muth, and Hugh O Nourse. 1963. “A Regression Method for Real Estate Price Index Construction.” _Journal of the American Statistical Association_ 58 (304): 933–42. 

Balk, Bert M. 2012. _Price and Quantity Index Numbers: Models for Measuring Aggregate Change and Difference_ . Cambridge University Press. 

Baum-Snow, Nathaniel, and Lu Han. 2024. “The Microgeography of Housing Supply.” _Journal of Political Economy_ 132 (6): 1897–1946. 

Bogin, Alexander N, William M Doerner, and William D Larson. 2019a. “Local House Price Paths: Accelerations, Declines, and Recoveries.” _The Journal of Real Estate Finance and Economics_ 58 (2): 201–22. 

Bogin, Alexander, William Doerner, and William Larson. 2019b. “Local House Price Dynamics: New Indices and Stylized Facts.” _Real Estate Economics_ 47 (2): 365–98. 

32 

Broxterman, Daniel A, Yishen Liu, and Anthony M Yezer. 2026. “Why We Still Don’t Know Much about Housing Supply Elasticity.” _Real Estate Economics_ . 

Brueckner, Jan K. 1987. “The Structure of Urban Equilibria: A Unified Treatment of the MuthMills Model.” In _Handbook of Regional and Urban Economics_ , 2:821–45. Elsevier. 

Calhoun, Charles A. 1996. “OFHEO House Price Indexes: HPI Technical Description.” _Office of Federal Housing Enterprise Oversight_ 20552: 1–15. 

Case, Karl E., and Robert J. Shiller. 1987. “Prices of Single-Family Homes Since 1970: New Indexes for Four Cities.” NBER Working Paper 2393. National Bureau of Economic Research. 

Clapham, Eric, Peter Englund, John M Quigley, and Christian L Redfearn. 2006. “Revisiting the Past and Settling the Score: Index Revision for House Price Derivatives.” _Real Estate Economics_ 34 (2): 275–302. 

Clapp, John M, Katsiaryna Salavei Bardos, and Siu Kei Wong. 2012. “Empirical Estimation of the Option Premium for Residential Redevelopment.” _Regional Science and Urban Economics_ 42 (1-2): 240–56. 

Clapp, John M, and Carmelo Giaccotto. 1999. “Revisions in Repeat-Sales Price Indexes: Here Today, Gone Tomorrow?” _Real Estate Economics_ 27 (1): 79–104. 

Contat, Justin, and William D Larson. 2024. “A Flexible Method of Housing Price Index 

Construction Using Repeat-Sales Aggregates.” _Real Estate Economics_ 52 (6): 1551–83. D’Lima, Walter, Luis Arturo Lopez, and Archana Pradhan. 2022. “Covid-19 and Housing Market Effects: Evidence from Us Shutdown Orders.” _Real Estate Economics_ 50 (2): 303–39. 

33 

Davis, Morris A, and François Ortalo-Magné. 2011. “Household Expenditures, Wages, Rents.” _Review of Economic Dynamics_ 14 (2): 248–61. 

Deng, Yongheng, and John M Quigley. 2008. “Index Revision, House Price Risk, and the 

Market for House Price Derivatives.” _The Journal of Real Estate Finance and Economics_ 37 (3): 191–209. 

Diewert, W. Erwin. 2012. “Consumer Price Statistics in the UK.” Office for National Statistics. Edlund, Lena, Cecilia Machado, and Maria Sviatschi. 2022. “Gentrification and the Rising 

Returns to Skill.” _Economica_ 89 (354): 258–92. 

Eurostat. 2013. _Handbook on Residential Property Price Indices_ . OECD Publishing. 

Fischer, Manfred M, Florian Huber, Michael Pfarrhofer, and Petra Staufer-Steinnocher. 2021. “The Dynamic Impact of Monetary Policy on Regional Housing Prices in the United States.” _Real Estate Economics_ 49 (4): 1039–68. 

Gedal, Michael, and Ingrid Gould Ellen. 2018. “Valuing Urban Land: Comparing the Use of 

Teardown and Vacant Land Sales.” _Regional Science and Urban Economics_ 70: 190– 203. 

Glaeser, Edward L, Joshua D Gottlieb, and Kristina Tobio. 2012. “Housing Booms and City 

Centers.” _American Economic Review_ 102 (3): 127–33. 

Glaeser, Edward L., and Joseph Gyourko. 2005. "Urban Decline and Durable Housing." _Journal of Political Economy_ 113 (2): 345-375. 

Glaeser, Edward L, Matthew E Kahn, and Jordan Rappaport. 2008. “Why Do the Poor Live in Cities? The Role of Public Transportation.” _Journal of Urban Economics_ 63 (1): 1–24. Guren, Adam M., Alisdair McKay, Emi Nakamura, and Jón Steinsson. 2021. "Housing Wealth Effects: The Long View." _The Review of Economic Studies_ 88 (2): 669-707. 

34 

Hansen, Julia L, John P Formby, and W James Smith. 1996. “The Income Elasticity of Demand 

for Housing: Evidence from Concentration Curves.” _Journal of Urban Economics_ 39 (2): 173–92. 

Ioannides, Yannis M, and Jeffrey E Zabel. 2008. “Interactions, Neighborhood Selection and Housing Demand.” _Journal of Urban Economics_ 63 (1): 229–52. 

Jevons, W Stanley. 1865. “On the Variation of Prices and the Value of the Currency Since 

1782.” _Journal of the Statistical Society of London_ 28 (2): 294–320. 

Keynes, John Maynard. 1930. _The Pure Theory of Money_ . Macmillen. 

Larson, William D, and Weihua Zhao. 2020. “Oil Prices and Urban Housing Demand.” _Real Estate Economics_ 48 (3): 808–49. 

Larson, William, Anthony Yezer, and Weihua Zhao. 2022. “Urban Planning Policies and the 

Cost of Living in Large Cities.” _Regional Science and Urban Economics_ 96: 103802. Laspeyres, E. 1871. “Die Berechnung Einer Mittleren Waaren.” _Jahrbücher für_ 

_Nationalökonomie Und Statistik_ 16: 296. 

Liu, Sitian, and Yichen Su. 2021. “The Impact of the Covid-19 Pandemic on the Demand for Density: Evidence from the Us Housing Market.” _Economics Letters_ 207: 110010. 

Liu, Yishen. 2018. “Estimating the Elasticity of Supply of Housing Space Rather Than Units.” _Regional Science and Urban Economics_ 68: 1–10. 

Malone, Thom, and Christian L Redfearn. 2022. “To Measure Globally, Aggregate Locally: Urban Land, Submarkets, and Biased Estimates of the Housing Stock.” _Real Estate Economics_ 50 (3): 656–71. 

Mills, Edwin S. 1967. “An Aggregative Model of Resource Allocation in a Metropolitan Area.” _The American Economic Review_ 57 (2): 197–210. 

35 

Molloy, Raven, and Hui Shan. 2013. “The Effect of Gasoline Prices on Household Location.” 

_Review of Economics and Statistics_ 95 (4): 1212–21. 

Muth, Richard F. 1969. _Cities and Housing: The Spatial Pattern of Urban Residential Land Use._ University of Chicago Press. 

Nagaraja, Chaitra, Lawrence Brown, and Susan Wachter. 2014. “Repeat Sales House Price Index Methodology.” _Journal of Real Estate Literature_ 22 (1): 23–46. 

Owusu-Ansah, Anthony. 2011. “A Review of Hedonic Pricing Models in Housing Research.” 

_Journal of International Real Estate and Construction Studies_ 1 (1): 19. 

Rapaport, Carol. 1997. “Housing Demand and Community Choice: An Empirical Analysis.” 

_Journal of Urban Economics_ 42 (2): 243–60. 

Rosenthal, Stuart S, John V Duca, and Stuart A Gabriel. 1991. “Credit Rationing and the 

Demand for Owner-Occupied Housing.” _Journal of Urban Economics_ 30 (1): 48–63. Rosenthal, Stuart S, and Robert W Helsley. 1994. “Redevelopment and the Urban Land Price Gradient.” _Journal of Urban Economics_ 35 (2): 182–200. 

Sagi, Jacob S. 2021. “Asset-Level Risk and Return in Real Estate Investments.” _The Review of Financial Studies_ 34 (8): 3647–94. 

Seagraves, Cayman, and Dean H Gatzlaff. 2025. “Examining House Price Movements Within the Metropolitan Market.” _Available at SSRN 5296393_ . 

Silver, Mick S. 2018. “How to Measure Hedonic Property Price Indexes Better.” _Eurostat_ 

_Review on National Accounts and Macroeconomic Indicators (EURONA)_ , no. 1: 35–66. Sirmans, Stacy, David Macpherson, and Emily Zietz. 2005. “The Composition of Hedonic 

Pricing Models.” _Journal of Real Estate Literature_ 13 (1): 1–44. 

36 

S&P Dow Jones. 2025. “S&p Cotality Case-Shiller Home Price Indices Methodology.” S&P 

Dow Jones. 

37 

Table 1: Compound annual growth rates in median values (2015–2019) 

||Metro|wide|Centr|al City|Sub|urbs|Diffe|rence|
|---|---|---|---|---|---|---|---|---|
||Value<br>[1]|Rent<br>[2]|Value<br>[3]|Rent<br>[4]|Value<br>[5]|Rent<br>[6]|Value<br>[7]|Rent<br>[8]|
|Atlanta|13.6|5.7|24.5|7.8|11.3|5.7|13.3|2.0|
|Boston|8.2|6.2|11.7|4.5|8.2|8.8|3.5|-4.3|
|Chicago|5.7|3.8|9.7|4.1|4.7|3.4|5.1|0.8|
|Cincinnati|4.7|5.7|7.0|7.5|5.4|8.3|1.6|-0.9|
|Cleveland|3.2|2.0|0.0|1.8|4.1|6.9|-4.1|-5.1|
|Dallas|11.0|6.1|10.1|6.1|10.1|6.7|0.0|-0.6|
|Denver|9.2|7.5|12.5|4.8|10.4|6.2|2.1|-1.4|
|Detroit|7.5|2.7|10.7|3.5|7.0|2.7|3.6|0.7|
|Houston|9.3|3.9|9.5|4.3|8.1|5.1|1.4|-0.8|
|Kansas City|6.2|3.4|5.6|3.4|5.2|2.7|0.3|0.7|
|Los Angeles|5.5|6.7|6.2|7.4|6.8|6.2|-0.6|1.2|
|Memphis|9.2|3.9|5.1|3.9|6.8|3.6|-1.7|0.3|
|Miami|6.9|4.5|8.8|5.6|7.5|4.3|1.3|1.3|
|Milwaukee|5.0|2.7|5.1|1.9|6.1|5.4|-1.0|-3.6|
|New Orleans|4.1|1.6|5.6|1.6|5.7|3.2|-0.1|-1.6|
|New York City|4.3|4.1|4.7|3.8|4.0|4.5|0.6|-0.7|
|Philadelphia|5.3|4.1|7.5|5.6|4.7|4.2|2.9|1.4|
|Phoenix|11.1|7.0|11.5|7.5|10.7|4.6|0.8|3.0|
|Pittsburgh|5.3|2.0|13.6|7.7|5.1|2.1|8.5|5.6|
|Portland|9.4|7.9|9.8|10.1|9.3|7.5|0.5|2.6|
|Raleigh|4.7|4.9|1.5|9.3|8.0|6.1|-6.5|3.2|
|Riverside|6.8|6.8|7.5|8.7|6.6|5.7|0.8|3.0|
|San Francisco|8.7|6.6|9.3|7.0|9.5|8.5|-0.2|-1.5|
|Seattle|10.7|7.2|13.6|6.8|10.0|7.4|3.7|-0.6|
|Washington DC|1.4|2.7|1.0|1.6|2.7|2.7|-1.6|-1.1|
|Average|7.1|4.8|8.5|5.5|7.1|5.3|1.4|0.1|
|Deviation|2.8|1.9|4.9|2.4|2.3|1.9|3.8|2.4|



Notes: Values in percents. Approximately 2,000 housing units are interviewed for each metro area. Differences in growth rates are calculated as central city minus suburbs. 

Source: Authors' calculations using reported median values from the American Housing Survey Metropolitan Sample. 

Table 2: Compound annual growth rates in median values (2015–2019) 

||Simpl|e Avg|Altern|ative|Diffe|rence|
|---|---|---|---|---|---|---|
||Value<br>[1]|Rent<br>[2]|Value<br>[3]|Rent<br>[4]|Value<br>[5]|Rent<br>[6]|
|Atlanta|17.91|6.75|12.96|5.99|-4.95|-0.75|
|Boston|9.92|6.64|9.03|7.72|-0.89|1.09|
|Chicago|7.20|3.77|6.65|3.69|-0.55|-0.08|
|Cincinnati|6.20|7.90|5.69|8.18|-0.51|0.28|
|Cleveland|2.03|4.32|3.05|5.60|1.02|1.28|
|Dallas|10.13|6.37|10.13|6.36|0.00|-0.01|
|Denver|11.41|5.53|11.23|5.65|-0.18|0.12|
|Detroit|8.85|3.10|8.25|2.98|-0.60|-0.12|
|Houston|8.83|4.74|8.71|4.82|-0.13|0.07|
|Kansas City|5.40|3.07|5.37|3.01|-0.03|-0.06|
|Los Angeles|6.50|6.77|6.46|6.85|-0.04|0.08|
|Memphis|5.99|3.79|5.97|3.79|-0.02|0.00|
|Miami|8.12|4.93|7.78|4.59|-0.34|-0.34|
|Milwaukee|5.58|3.65|5.62|3.80|0.04|0.15|
|New Orleans|5.67|2.40|5.67|2.41|0.00|0.00|
|New York City|4.35|4.13|4.32|4.16|-0.03|0.03|
|Philadelphia|6.09|4.86|5.45|4.54|-0.64|-0.31|
|Phoenix|11.11|6.05|11.19|6.37|0.08|0.32|
|Pittsburgh|9.38|4.92|6.29|2.87|-3.09|-2.05|
|Portland|9.57|8.81|9.54|8.64|-0.03|-0.17|
|Raleigh|4.73|7.71|4.88|7.64|0.15|-0.07|
|Riverside|7.05|7.24|6.87|6.61|-0.17|-0.63|
|San Francisco|9.44|7.78|9.43|7.72|-0.01|-0.06|
|Seattle|11.79|7.10|11.46|7.16|-0.33|0.06|
|Washington DC|1.85|2.14|2.24|2.40|0.40|0.25|
|Average|7.80|5.38|7.37|5.34|-0.43|-0.04|
|Deviation|3.30|1.80|2.70|1.90|1.15|0.58|



Notes: Values in percents. The simple average index is the mean of the central city and suburbs growth rates from Table 1. The alternative index weights the growth rates by the total number of units, renter and owner, in each location. Differences between the indexes are calculated as alternative  minus simple average. 

Source: Authors' calculations using reported median values from the American Housing Survey Metropolitan Sample. 

|Table 3: Index differences ac<br>Dependent variable:𝑃2020<br>𝐿𝐿𝐿|ross cities v<br>𝐿𝐿/𝑃2020<br>𝑈𝑈𝑈𝐿𝑈|s uniform weigh<br>−1|ts||||
|---|---|---|---|---|---|---|
|Laspeyres formulation||Units|R|ooms||Value|
||[1]|[2]|[3]|[4]|[5]|[6]|
|Housing units<br>(log, 2019)|-0.689***|<br>-0.342***|-1.189***|-0.693***|-0.946|-0.427*|
||(0.167)|(0.079)|(0.222)|(0.113)|(0.516)|(0.201)|
|Housing supply elasticity<br>(Saiz, 2010)|-0.156|-0.080|-0.610*|-0.180*|-1.323**|-0.509**|
||(0.251)|(0.055)|(0.285)|(0.070)|(0.466)|(0.155)|
|Structure age<br>(mean)|-0.010|0.037|0.032|0.064**|0.160|0.133**|
||(0.040)|(0.021)|(0.043)|(0.024)|(0.085)|(0.044)|
|Urban decline<br>(G&G, 2005)|1.712*||2.034||2.341||
||(0.822)||(1.114)||(2.729)||
|Housing value<br>(mean, log, 2019)|-0.252|-0.546*|-1.855*|-1.337***|-3.285**|-1.668**|
||(0.604)|(0.249)|(0.726)|(0.335)|(1.237)|(0.595)|
|Household income<br>(mean, log, 2019)|3.544**|1.361|4.548**|1.573|8.131*|3.306*|
||(1.321)|(0.785)|(1.469)|(0.888)|(3.108)|(1.520)|
|Constant|-24.530|-3.290|-8.947|8.152|-31.129|-8.365|
||(12.927)|(6.993)|(14.264)|(7.760)|(24.918)|(13.565)|
|N|72|245|72|245|72|245|
|R²|0.208|0.113|0.458|0.297|0.277|0.121|
|Notes: *, **, and *** indicate<br>errors in parentheses. The<br>calculated as𝑃2020<br>𝐿𝐿𝐿𝐿𝐿/𝑃20<br>𝑈|p<0.1, p<0.<br>dependent v<br>20<br>𝑈𝑈𝐿𝑈−1.|05, and p<0.01,<br>ariable is the 30<br>Housing units (l|respectively.<br>-year accumu<br>og), housing v|Heteroskedasti<br>lated gap in th<br>alue (log), inco|city-consiste<br>e house pric<br>me (log), an|nt standard<br>e index,<br>d structure age|



are CBSA averages from the 5-year American Community Survey in 2019. Urban decline is the share of housing units below replacement costs in 1990 from Glaeser and Gyourko (2005); supply elasticity is from Saiz (2010). 

Sources: Contat and Larson (2024); Glaeser and Gyourko (2005); Saiz (2010); Guren et al. (2021); Baum-Snow and Han (2024); Census, American Community Survey; Authors' analysis. 

Figure 1: Within-city appreciation differences (annual average) 



<!-- Start of picture text -->
(10,15]<br>(5,10]<br>(0,5]<br>(-5,0]<br>(-10,-5]<br>[-15,-10]<br><!-- End of picture text -->



<!-- Start of picture text -->
(10,15]<br>(5,10]<br>(0,5]<br>(-5,0]<br>(-10,-5]<br>[-15,-10]<br><!-- End of picture text -->



<!-- Start of picture text -->
(6,7]<br>(5,6]<br>(4,5]<br>(3,4]<br>[2,3]<br><!-- End of picture text -->



<!-- Start of picture text -->
(10,15] (10,15]<br>(5,10] (5,10] (6,7]<br>(0,5] (0,5] (5,6]<br>(-5,0]  (-5,0]  (4,5]<br>(-10,-5]  (-10,-5]  (3,4]<br>[-15,-10]  [-15,-10]  [2,3]<br><!-- End of picture text -->

_Notes_ : Maps show the annual geometric average nominal appreciation rate for Census tracts (2010 defi-nitions). The maps display census tracts whose centroids lie within 15 miles of the centroid of the tract containing the respective city’s City Hall. 

_Sources_ : Contat and Larson (2024); Authors’ analysis. 

Figure 2: Shares used in city index calculation (2010 values) 



<!-- Start of picture text -->
(.2,.3]<br><!-- End of picture text -->



<!-- Start of picture text -->
(.2,.3]<br><!-- End of picture text -->



<!-- Start of picture text -->
(.2,.3]<br><!-- End of picture text -->



<!-- Start of picture text -->
(.2,.3] (.2,.3] (.2,.3]<br>(.1,.2] (.1,.2] (.1,.2]<br>(.05,.1] (.05,.1] (.05,.1]<br>[0,.05] [0,.05] [0,.05]<br><!-- End of picture text -->

_Notes_ : Maps show the shares used in CBSA-level house price index construction, by Census tract (2010 definitions). Tracts shown have centroids within 15 miles of the centroid of the Census tract containing the respective city’s City Hall. 

_Sources_ : Census/ACS; Authors’ analysis. 

Figure 3: Appreciation index differences 



<!-- Start of picture text -->
(a) Boston, MA, Annual appreciation (b) Boston, MA, Cumulative difference<br><!-- End of picture text -->





































_Notes_ : The figures present alternative city-level house price indices. Each index type (shown in the legend) is constructed by aggregating Census tract (2010 definitions)-level house price appreciation rates using time-varying tract-level weights. The equally-weighted index assigns each tract the same weight. 

_Sources_ : Contat and Larson (2024); Census/ACS; Authors’ analysis. 

Table A.1: Index differences across cities, housing unit vs uniform weights, single correlate Dependent variable: 30-year cumulative index gap (percent) 

||Housing<br>Units|Value|Income|Structure<br>Age|Elasticity|Decline|Guren γ|Units γ|Space γ|
|---|---|---|---|---|---|---|---|---|---|
||[1]|[2]|[3]|[4]|[5]|[6]|[7]|[8]|[9]|
|||||A. Sma|ll sample|||||
|Column<br>Variable|-0.458**|-0.699*|-0.275|0.049|0.227|1.565**|-0.776**|1.265|1.404|
||(0.145)|(0.347)|(1.211)|(0.033)|(0.165)|(0.559)|(0.281)|(1.183)|(1.185)|
|Constant|6.033**|8.199|2.467|-1.068*|-0.882*|-0.896***|0.337|-0.691*|-1.077|
||(2.082)|(4.307)|(12.617)|(0.484)|(0.376)|(0.242)|(0.332)|(0.275)|(0.546)|
|N|76|76|76|80|75|80|80|80|80|
|R²|0.096|0.040|0.001|0.027|0.023|0.071|0.054|0.013|0.016|
|||||B. Larg|e sample|||||
|Column<br>Variable|-0.325***|-0.594**|-0.641|0.059**|0.105*|1.658**|-0.366|0.035|0.080|
||(0.068)|(0.200)|(0.590)|(0.019)|(0.047)|(0.585)|(0.206)|(0.615)|(0.618)|
|Constant|4.134***|7.121**|6.510|-0.863**|-0.358*|-0.989***|0.215|-0.108|-0.142|
||(0.887)|(2.427)|(6.089)|(0.266)|(0.165)|(0.264)|(0.179)|(0.205)|(0.355)|
|N|245|245|245|249|249|75|247|244|244|
|R²<br>|0.069<br>|0.035<br>|0.004<br>|0.045<br>|0.012<br>|0.079<br>|0.015<br><br>|0.000<br>|0.000|
|Notes: *, **<br>The depen<br>units (log),<br>2019. Urba<br>elasticity i<br>mean supp<br>CBSA’s wit|, and *** indic<br>dent variable<br>housing valu<br>n decline is t<br>s from Saiz (2<br>ly elasticities<br>h a G&G (200|ate p<0.1, p<<br>is the 30-year<br>e (log), incom<br>he share of ho<br>010), Guren γ<br>from Baum-S<br>5) decline val|0.05, and p<0<br>accumulated<br>e (log), and st<br>using units be<br>is the sensitiv<br>now and Han<br>ue and Saiz (2|.01, respective<br>gap in the ho<br>ructure age ar<br>low replacem<br>ity parameter<br>(2024) using<br>010) elasticity|ly. Heteroske<br>use price inde<br>e CBSA avera<br>ent costs in 1<br>in Guren et a<br>gamm01a for<br>value, respec|dasticity-cons<br>x, calculated a<br>ges from the 5<br>990 from Glae<br>l. (2021), and<br>mulation. Smal<br>tively|istent standar<br>s𝑃2020<br>𝐿𝐿𝐿𝐿𝐿/𝑃<br>-year America<br>ser and Gyour<br>the new units<br>l sample and|d errors in pa<br>2020<br>𝑈𝑈𝑈𝐿𝑈−1.<br>n Communit<br>ko (2005); su<br>and space γ’s<br>large sample|rentheses.<br>Housing<br>y Survey in<br>pply<br>are CBSA<br>include all|



Sources: Contat and Larson (2024); Glaeser and Gyourko (2005); Saiz (2010); Guren et al. (2021); Baum-Snow and Han (2024); Census, American Community Survey; Authors' analysis. 

Table A.2: Index differences across cities, rooms vs uniform weights, single correlate 

Dependent variable: 30-year cumulative index gap (percent) 

||Housing<br>Units|Value|Income|Structure<br>Age|Elasticity|Decline|Guren γ|Units γ|Space γ|
|---|---|---|---|---|---|---|---|---|---|
||[1]|[2]|[3]|[4]|[5]|[6]|[7]|[8]|[9]|
|||||A. Sma|ll sample|||||
|Column<br>Variable|-1.076***|-2.271***|-3.644*|0.145***|0.362|3.091***|-1.033*|2.459|2.719|
||(0.215)|(0.522)|(1.654)|(0.042)|(0.231)|(0.830)|(0.428)|(1.923)|(1.941)|
|Constant|13.757***|26.577***|36.431*|-3.265***|-2.069***|-2.264***|-0.292|-1.850***|-2.593**|
||(3.072)|(6.462)|(17.222)|(0.539)|(0.527)|(0.343)|(0.466)|(0.483)|(0.946)|
|N|76|76|76|80|75|80|80|80|80|
|R²|0.263|0.212|0.063|0.115|0.029|0.137|0.047|0.025|0.029|
|||||B. Larg|e sample|||||
|Column<br>Variable|-0.754***|-1.617***|-2.910***|0.114***|0.254***|3.327***|-0.551*|1.222|1.379|
||(0.092)|(0.293)|(0.801)|(0.025)|(0.067)|(0.863)|(0.250)|(0.942)|(0.959)|
|Constant|9.249***|19.092***|29.415***|-2.036***|-1.193***|-2.471***|-0.083|-0.947**|-1.346*|
||(1.206)|(3.553)|(8.256)|(0.332)|(0.229)|(0.367)|(0.222)|(0.325)|(0.565)|
|N|245|245|245|249|249|75|247|244|244|
|R²<br>|0.203<br>|0.143<br>|0.049<br>|0.091<br>|0.039<br>|0.161<br>|0.018<br><br>|0.008<br>|0.011|
|Notes: *, *<br>The depen<br>(log), hous<br>Urban dec<br>from Saiz<br>elasticities<br>G&G (2005|*, and *** ind<br>dent variable<br>ing value (log<br>line is the sha<br>(2010), Guren<br>from Baum-S<br>) decline valu|icate p<0.1, p<br>is the 30-year<br>), income (log<br>re of housing<br>γ is the sensi<br>now and Han<br>e and Saiz (2|<0.05, and p<<br>accumulated<br>), and structu<br>units below r<br>tivity parame<br>(2024) using<br>010) elasticity|0.01, respecti<br>gap in the hou<br>re age are CB<br>eplacement c<br>ter in Guren e<br>gamm01a fo<br>value, respec|vely. Heterosk<br>se price index<br>SA averages f<br>osts in 1990 f<br>t al. (2021), a<br>rmulation. Sm<br>tively|edasticity-con<br>, calculated as<br>rom the 5-yea<br>rom Glaeser a<br>nd the new un<br>all sample an|sistent stand<br> 𝑃2020<br>𝐿𝐿𝐿𝐿𝐿/𝑃<br>r American C<br>nd Gyourko (<br>its and space<br>d large sampl|ard errors in<br>2020<br>𝑈𝑈𝑈𝐿𝑈−1. H<br>ommunity Sur<br>2005); supply<br>γ’s are CBSA<br>e include all C|parentheses.<br>ousing units<br>vey in 2019.<br>elasticity is<br>mean supply<br>BSA’s with a|



Sources: Contat and Larson (2024); Glaeser and Gyourko (2005); Saiz (2010); Guren et al. (2021); Baum-Snow and Han (2024); Census, American Community Survey; Authors' analysis. 

Table A.3: Index differences across cities, value vs uniform weights, single correlate Dependent variable: 30-year cumulative index gap (percent) 

||Housing<br>Units|Value|Income|Structure<br>Age|Elasticity|Decline|Guren γ|Units γ|Space γ|
|---|---|---|---|---|---|---|---|---|---|
||[1]|[2]|[3]|[4]|[5]|[6]|[7]|[8]|[9]|
|||||A. Sma|ll sample|||||
|Column<br>Variable|-0.625|-2.029|-0.561|0.295***|-0.243|4.494*|0.272|0.737|0.770|
||(0.452)|(1.110)|(2.932)|(0.075)|(0.387)|(2.138)|(0.938)|(3.503)|(3.487)|
|Constant|8.600|24.762|5.648|-4.157***|0.324|-1.543**|-0.321|-0.249|-0.450|
||(6.496)|(13.889)|(30.655)|(1.015)|(0.715)|(0.580)|(0.847)|(0.681)|(1.503)|
|N|76|76|76|80|75|80|80|80|80|
|R²|0.030|0.056|0.000|0.159|0.004|0.097|0.001|0.001|0.001|
|||||B. Larg|e sample|||||
|Column<br>Variable|-0.279|-0.872|0.332|0.177***|-0.146|4.776*|0.946*|-0.340|-0.401|
||(0.159)|(0.474)|(1.226)|(0.041)|(0.099)|(2.194)|(0.454)|(1.380)|(1.377)|
|Constant|3.872|10.841|-3.173|-2.042***|0.657|-1.787**|-0.493|0.374|0.495|
||(2.059)|(5.805)|(12.667)|(0.548)|(0.340)|(0.622)|(0.368)|(0.444)|(0.778)|
|N|245|245|245|249|249|75|247|244|244|
|R²<br>|0.010<br>|0.016<br>|0.000<br>|0.082<br>|0.005<br>|0.108<br>|0.020<br><br>|0.000<br>|0.000|
|Notes: *, **<br>The depen<br>units (log),<br>2019. Urba<br>elasticity is<br>mean supp<br>CBSA’s wit|, and *** indi<br>dent variable<br>housing valu<br>n decline is t<br>from Saiz (2<br>ly elasticities<br>h a G&G (200|cate p<0.1, p<<br>is the 30-year<br>e (log), incom<br>he share of ho<br>010), Guren γ<br>from Baum-S<br>5) decline val|0.05, and p<0.<br>accumulated<br>e (log), and st<br>using units be<br>is the sensitiv<br>now and Han<br>ue and Saiz (2|01, respective<br>gap in the ho<br>ructure age ar<br>low replacem<br>ity parameter<br>(2024) using<br>010) elasticity|ly. Heteroske<br>use price inde<br>e CBSA avera<br>ent costs in 19<br>in Guren et al<br>gamm01a for<br>value, respec|dasticity-cons<br>x, calculated a<br>ges from the 5<br>90 from Glae<br>. (2021), and<br>mulation. Sma<br>tively|istent standar<br>s𝑃2020<br>𝐿𝐿𝐿𝐿𝐿/𝑃<br>-year Americ<br>ser and Gyour<br>the new units<br>ll sample and|d errors in pa<br>2020<br>𝑈𝑈𝑈𝐿𝑈−1.<br>an Communit<br>ko (2005); su<br>and space γ’s<br>large sample|rentheses.<br>Housing<br>y Survey in<br>pply<br>are CBSA<br>include all|



Sources: Contat and Larson (2024); Glaeser and Gyourko (2005); Saiz (2010); Guren et al. (2021); Baum-Snow and Han (2024); Census, American Community Survey; Authors' analysis. 

