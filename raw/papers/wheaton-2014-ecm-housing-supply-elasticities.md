---
source_url: /tmp/wheaton-2014-ecm-supply.pdf
ingested: 2026-07-16
sha256: 6bf2b7963795beec
---

**2nd Draft** :  December 30, 2014 

# **Error Correction Models of MSA Housing “Supply” Elasticities: Implications for Price Recovery** 

By 

William C. Wheaton Department of Economics Center for Real Estate MIT* Cambridge, Mass 02139 <u>wheaton@mit.edu</u> 

Serguei Chervachidze Capital Markets Economist CBRE Econometric Advisers <u>serguei.chervachidze@cbre.com</u> 

Gleb Nechayev Senior Vice President Berkshire Group - <u>gleb.nechaev@berkshire group.com</u> 

The authors are indebted to, the MIT Center for Real Estate, and CBRE.  They remain responsible for all results and conclusions derived there from. * Corresponding Author 

1 

JEL Code: R. Keywords: Housing 

## **ABSTRACT** 

MSA-level estimates of a housing supply schedule must offer a solution to the twin problems of simultaneity and non-stationarity that plague the time series data for local housing prices and stock. A Vector Error Correction Model (VECM) is suggested to handle both the non-stationarity and endogeneity problems. This model also nicely distinguishes between (very) long-run elasticities and a variety of short-term impacts. We estimate this model separately for 68 US MSAs using quarterly data on housing prices and residential construction permits since 1980. We also estimate a single-equation Error Correction Model (ECM) for house prices in which stock is exogenous in order to test the robustness of prices to alternative stock growth scenarios.  The results of both models provide long-run supply elasticity estimates for each market that are better bounded than previous panel-based attempts and also correspond with much conventional thought. We find these elasticities are well explained by geographic and regulatory barriers, and that inelastic markets exhibit greater price volatility over the last two decades.  Using the models’ short- run dynamics we make several forecasts of prices over the next decade. In current dollars, some MSAs will still not recover to recent peak (2007) house price levels by 2024, while others should exceed it by as much as 40%. 

2 

## **I. Introduction** 

There has been a revival of interest in the supply schedule that characterizes urban housing markets. It has been argued that variation in the elasticity of this schedule may explain the wide differences observed across US metropolitan statistical areas (MSA) in house price levels, their growth and also volatility [(Campbell-Davis-Martin (2009), Capozza-Hendershott-Mack (2004), Cannon-Miller-Pandher (2006), Glaeser-GyourkoSaiz (2005), Paciorek (2013), Davidoff (2013)]. It has also been argued that housing supply elasticities impact the allocation of labor across MSAs and hence can affect aggregate productivity [Nieuwerburgh-Weil (2009), Eckhout-Pinheiro-Schmidheiny (2010)]. Thus there is much interest in the possible “determinants” of local housing supply elasticities, be they related to intrinsic geographic land supply [Saiz (2010)], local land use regulations [Gyourko-Saiz-Summers (2008)], or the organizational structure of the homebuilding industry [Somerville (1999)]. Despite all this interest, much of the discussion is conducted in an empirical vacuum, for there are no _individual time series_ estimates of long or short run housing supply elasticities in San Francisco versus Dallas or any of the other 300 US MSAs. The literature review section that follows will make this more apparent. 

One purpose of this study therefore is to apply modern time series analysis to quarterly data on MSA constant dollar (repeat sale) house prices, new housing construction and the growth of the stock – covering 1980:1 through 2014:3. We do this individually for each of the largest 68 MSAs. At the start, we find that (real) house price levels and stock are not stationary - in all but a few MSAs. This calls into question much of the early empirical research on this topic. Both series, however, are stationary in differences, or I(1). Most importantly house prices and stock (measured in levels) are cointegrated (again in all but a handful of markets). This suggests that an error-correction methodology is the proper framework for understanding the relationship between these two variables – at least at the MSA level. 

Within this framework we estimate a Vector Error Correction Model (VECM) in which both prices and stock are simultaneously determined as well as determining. The cointegrating vector between the two variables yields a consistent estimate of the long-run 

3 

elasticity of supply, and across our 68 MSAs, the results are extremely plausible: ranging from .2 to 3.1. We also estimate a single equation Error Correction Model (ECM) in which stock is exogenous and determines prices. The short-run dynamic impacts estimated through both models are also significant and provide us with several alternative shorterrun measures of housing supply elasticity (decade long).  With the VECM we simply do an out-of-sample forecast of both stock and price for the next 10 years -. from their current (2014:3) levels. The ratio of the stock/price forecasts then provides a measure of the effective short run elasticity to be observed over the next decade. With the ECM we are able to provide a robustness check on the recovery in prices by using a more conservative (exogenous) estimate new supply over the next decade. To allow for the possibility that slower population growth will dampen the long-run demand for housing from its historic trend, we set the anticipated new supply at 80% of that built in previous decades, in line with Census population projections. 

We find great consistency between these various supply elasticities, with correlations in the .9 range. We also find that they relate statistically to those “determinants” of supply elasticity recently hypothesized in the literature. Larger cities, with geographic land constraints, that have high scores on a survey of regulatory barriers have significantly lower supply elasticities – as we have measured them. 

We then investigate the role of supply elasticity in an MSA’s price experiences over the 2000-2012 period characterized by the housing “boom” and “bust”. Consistent with the conventional thinking that this period was marked by housing demand shocks, markets with more _in_ elastic supply exhibit greater price increases over 2000-2007, but smaller price declines from 2007 to 2012. 

Finally, we use the short-run forecasts generated by the models to assess the degree of housing price growth and eventual price recovery that is likely across our 68 MSAs, beginning in 2014:4. We find that markets with inelastic supply will experience faster price growth between 2014 and 2024, thus exhibiting similar dynamics to the prior decade. Inelastic markets also will generally have greater price recoveries (to or above previous peak levels) – controlling for the magnitude of the 2007-2012 price decline. 

4 

Markets will recover most where both the decline was least and where housing supply is most inelastic. 

In the next section we review the empirical literature on housing supply and its determinants. Section III reviews the standard model of land development that underlies much of the supply elasticity discussion, while Section IV then examines the data series available on prices, construction and the stock – testing for stationarity and cointegration. Section V lays out our VECM and ECM models, along with some alternative estimation strategies. Section VI presents results from estimating the various models, and displays their long and short-run implied elasticities. In section VII, we examine whether these elasticities line up with often used supply “instruments”. Section VIII examines the relationship between these elasticity estimates and market behavior from 2000 through 2012, while Section IX examines the magnitude and patterns in housing price recovery over the next decade that is likely across our 68 MSA. 

## **II. Housing Supply Literature** 

There is an early literature on housing supply [Alberts (1962), Burns-Grebbler (1982)] that looks at housing construction as a “business” in which the level of price relative to some opportunity cost (including credit) drives housing “investment” or unit flows (permits, starts or completions). The most recent elaboration of this approach is Topel-Rosen (1988) in which great attention is given to the expectation mechanism for future prices. Following Abel-Blanchard (1986), DiPasquale-Wheaton (1992, 1994) add to this approach with the notion that expected price levels determine a “desired” stock towards which the actual stock adjusts slowly with new investment. In this approach the existing stock is a critical additional variable (to prices) in explaining new investment. Much of this early literature is summarized in Blackley (1999), who notes that it contains little or no application of true time series analysis. For example the series are rarely tested for stationarity or cointegration, and regressions contain mixed I(0) and I(1) series. 

Mayer-Somerville (2000) redefines the entire discussion of supply elasticity and links it more explicitly to land development. In their framework the key ingredient necessary for cities to grow through new construction is the development of additional 

5 

land. Following a long and voluminous literature on urban spatial models - this requires higher land values which are simply a residual from housing prices. Thus like DiPasqualeWheaton the underlying “supply” relationship is between housing price levels and housing stock, rather than price levels and housing flows. They also argue that any empirically estimated  relationship between house price levels and stock is likely to be miss specified as both variables are I(1) and not I(0). They present estimates of a relationship between _changes_ in both housing stock and price that they argue better reflects that between housing price and stock _levels_ . We return to this specification issue in the next section. 

All of the literature above uses US national data to estimate some supposed national supply elasticity. But if the supply elasticity is really about land development, then surely there should be significant variation across cities of different sizes, with different geographies, transportation systems and regulatory processes. The availability of widespread MSA-level housing price indices has prompted a series of more recent analysis of differences in price movements across MSA. Capozza-Hendershott-Mack (2004), Cannon-Miller-Pandher (2006) and Campbell-Davis-Martin (2009) all examine the movement in prices to see if there is any relationship between price appreciation and price volatility across (respectively) MSA, ZIP codes and US census regions. None of these studies explicitly include study of housing supply or stock. 

Harter-Drieman (2004) opens up a new line of inquiry by using panel data analysis from 1980 to 1998 to compare 49 MSA. She develops a VECM model relating prices to _income_ (rather than stock or households) and does not test for cointegration between these two variables. By allowing for a market specific constant term in the long run 

cointegrating relationship, she is able to calculate a price response to an income shock that is unique to each market. Then _assuming_ a common price elasticity of demand, she is able calculate an implicit estimate of each market’s supply elasticity. Not surprising, the result is a very narrow range of implicit supply elasticities; for example, she finds that no markets are inelastic. 

Saiz (2010) adopts a similar panel approach, but with limited time series: there are only 3 decadal changes (observations) for each MSA. He develops an estimating equation wherein price changes are predicted using household (housing stock) changes, fixed 

6 

effects, and two variables that logically would impact a supply elasticity: the Wharton Land Use Regulatory Index (WLURI) [Gyourko-Saiz-Summers (2008)] and a newly constructed measure of geographic land _un_ availability. By interacting these variables with household changes he again is able to calculate an implicit supply elasticity for each market – yielding estimates of between .6 and 5.0. 

Over this time span there is only one attempt to separately estimate a supply elasticity uniquely by market: Green-Malpezzi-Mayo (2011). Their paper simply presents the elasticity resulting from a series of simple bivariate regressions with no statistical specification tests, and no resulting statistics. The elasticities vary widely (-.3 to 29.0) and half are reported as insignificant. A second stage cross-section regression explaining the elasticities contains 9 variables, most of which likely to be endogenous to a housing supply process. The approach of this paper is in principle similar to Green-MalpezziMayo, but with far greater series detail and testing. Such testing suggests the need for a very different model – one following an error correction framework. 

## **III. Long-Run models of Local Housing Supply** 

As discussed above, newer models of housing supply are actually models of land development and city expansion – rather than of “investment” in housing.  In this literature, monocentric land use models yield relationships between equilibrium city size (housing stock) and the difference between central housing prices and edge housing prices<sup>1</sup> . This latter can be thought of as a crude “average” city price. This relationship begins with the set of variable definitions in (1) below. 

> 1 Here we use the most simple of monocentric models where transport costs are constant and exogenous, and where land consumption is similarly. The voluminous literature on such models often has land consumption determined by agent utility and prices, while congestion can make transport costs non-linear and endogenous. 

7 

_B_ : travel distance from the urban center to edge in a circular city. _T_ : capitalized cost of traveling a unit distance (fixed across locations) _L_ :lot size of house (fixed across location) K : Capital cost of a house (fixed across location) _ra_ : price of ubiquitous agricultural land outside the circle _P_ 0 , _PB_ :house Prices at urban center and edge _S_ : stock of housing (population) _A_ : fraction of land (at  all locations) that  is developable (1) 

The equations below derive a set of equilibrium relationships between these variables. Equation (2) requires that house price differences between the center and edge equal the capitalized value of traveling from the edge to center. This is a spatial equilibrium condition. Equation (3) links edge prices to replacement costs using capital and agricultural land (both exogenous), while (4) links the urban border with total housing stock. Combining equations, we get the result in (5) where equilibrium average house prices (the difference between center and edge prices) depend positively on the size of the housing stock. While (5) expresses price as a function of stock, it is equally true that to provide a larger stock of urban land prices must rise and hence stock is a function of price; in other words equilibrium implies joint causality. Expression (5) has often been interpreted as an inverse housing “supply” schedule [Saiz (2010), Mayer and Somerville (2000)]. Expression (5) illustrates that the long term relationship between house prices and stock may also depend on land availability and the efficiency of the city transportation system (Saiz, 2010). 



Economists also have modeled a competitive system of cities [Weil and Nieuwerburgh-Weil (2009), Eckhout-Pinheiro-Schmidheiny (2010)]. In these models a “national” population selects where to reside among cities. Jobs or employment do 

8 

likewise. In addition to productivity and amenity considerations, these choices are influenced in no small part by house prices. Thus through the migration of population and the relocation of employment there can arise a parallel (but negative) “demand” relationship D(…) between prices and stock. _Ceteris paribus_ , _lower_ prices eventually attract an expanding population and job base (E). In equilibrium this base must equal the stock (S). Expressions (6) and (7) can be combined with (5) to complete any full model of a city in a system of cities competing for employment. 



In recent years monocentric models have given away to “polycentric” theory wherein a city has multiple centers or locations of economic activity. Each such center however behaves like a “sub-center” – following similar conditions as in (2)-(5). The main difference from the monocentric framework is that some sub centers compete with each other over land, rather than just with agricultural uses. Some theory of “agglomeration” is also necessary to determine whether the city is composed of many small sub centers or a few very large ones. With endogenous employment location, this family of models does not always yield the same comparative static results as with single centered city models. For example, in monocentric models higher transportation costs raise land rent and generate more dense cities. In polycentric models, higher transportation costs lead to greater employment dispersal and little or no increase in land rents [McMillen-Smith (2003), Helsley-Sullivan (1991)]. The empirical implication of these models is that often they have almost infinite long run housing (land) supply. With a single fixed center, increasing the supply of land requires greater commuting and hence land rent. With multiple endogenous centers more land can be had by expanding the number of centers with little attendant increase in commuting since the dominant pattern of commutes is within a center and not between centers. Hence land rents need also not increase. 

Finally, it is important to remember that (1) – (7) inform us only about long-run equilibrium relationships and provide very little guidance in terms of short-term dynamics. Short-run dynamics are often thought to involve the capital portion of housing rather than 

9 

land: the difficulty of constructing new structures and their durability once built. GlaeserGyourko (2005) for example convincingly show that even over decade-long intervals, the derivative of house prices with respect to stock is asymmetric: falling prices do little to shrink the stock, but rising prices are needed to expand it. Put differently, the identity between S and E in (6) rarely holds over short run intervals, when the stock of housing adjusts slowly. 

While this discussion is certainly not new, it does highlight a range of important issues that any empirical study of _local_ housing supply elasticities must address. The first such issue is that estimation must be flexible enough to accommodate a full range of potential long-run elasticity values, matching the variation anticipated from polycentric as opposed to monocentric urban models. Secondly, the estimation should allow for short run dynamic effects that may be distinct from long-run equilibrium impacts. For example, if the stock increases from a true “supply shock”, then prices may fall in the short run rather than rise along the long-run schedule. Finally, stock and prices are jointly determined in equilibrium, and so there is a high likelihood of simultaneity between the series Using local economic data as an instrument to resolve this simultaneity is certainly not valid in the long run. Given that structural identification is difficult, non-structural macroeconomic time series analysis may offer more viable solutions. 

## **IV. Empirical Tests of MSA House Price and Housing Stock Series** 

The data used in this analysis consists of two time series for each of 68 US metropolitan areas, at quarterly frequency, covering 1980:1 through 2014:3. The first is the Federal Housing Finance Agency’s (FHFA) all-transactions house price index (HPI) based on repeat transactions involving conventional mortgages purchased or securitized by Fannie Mae and Freddie Mac. The second is a series of total housing stock, starting with the 2010 Decennial Census and adding (for post 2010) or subtracting (for pre 2010) housing permits each quarter. It should be noted that this estimated stock series will not produce values for 1980, 1990, or 2000 stock that match the Decennial Census unit counts for those years, due largely to the effects of demolitions and undercounting. It would be possible to calculate a 3-decade average quarterly stock adjustment for each MSA and 

10 

apply this to the estimated stock series, but such scalar adjustment would not impact the statistical results, although it could alter slightly the estimated elasticities. 

To test for stationarity we undertake augmented Dickey-Fuller tests (ADF)<sup>2</sup> of house price in real inflation-adjusted dollars and stock in levels, using 4 and then 8 lags. For house prices, we can reject the null of a unit root in only 15 of 68 MSA – using 4 lags and a liberal 10% criterion<sup>3</sup> . With 8 lags the null is rejected in only 16 of 68 MSA. With the housing stock, the results are not much better, with only 18 of 68 MSA exhibiting stationarity using 4 lags and 14 of 68 using 8 lags (again applying a 10% criterion). However, the first differences of both the stock and price series are stationary in all but a handful of MSA (7 and 6 with the 4 and 8 lags respectively). These are clearly very noisy series with surprisingly little mean reversion in levels. We note that this contrasts sharply with the much smoother national time series on prices and stock (Case and Shiller (1988)). 

With two non-stationary series, any direct regressions of prices on stock would be subject to a range of problems – as would any derived estimates of a long-run elasticity (such as in much of early literature). Recognizing this possibility, Mayer-Somerville (2000) suggest a regression (using national data) in first differences, but obtain a very small short-run elasticity since only a few lags of price (changes) are included. With a model estimated in differences a permanent change in price levels impacts the stock only during the period in which prices change. This provides consistent estimates of a long run price elasticity only if the market is always at equilibrium with no internal dynamics. In our MSA level data most of the series are I(1), or stationary in differences, but using such an approach would preclude estimating our main objective - a true long run elasticity. 

An alternative approach for using statistical analysis with variables that are still measured in levels would be to apply an error-correction framework. This approach does not require that each variable be stationary in levels, but does necessitate that they exhibit co-integration. To this end, Appendix 1 presents the results of several augmented cointegration tests. The first two columns essentially test for whether the residuals from a 

> 2 For a general discussion of Dickey-Fuller tests, see Hamilton (1994), Chapter 17. 

> 3 For these ADF tests we used the following critical values from Mackinnon (1996): 1% 3.49, 5% 2.89, 10% 2.58, 20% 2.21. 

11 

regression of price on stock (usually called a first-stage regression) – a simplified version of equation (5) - are stationary. This is accomplished by applying a version of the ADF test on the residuals from this first stage to check for stationarity, which if stationary, would imply cointegration between the levels of price and stock (our first-stage regression variables). The critical values for this test are different from the critical values used in standard ADF statistics and are taken from simulation-derived values in MacKinnon (1996). 

As is usually the case with ADF-related tests, results depend considerably on the number of lags used – a common dilemma when testing for stationarity. We experimented using both the Akaike Information Criteria (AIC) for the number of lags, as well as selecting the number of lags that gives the highest test statistic. These two criteria yielded very similar results in terms of lag selection which is shown in the 1st column of Appendix 1. In the 2<sup>nd</sup> column we present the R2 of the error regression and in the next two columns the coefficient on lagged error level (the cointegration test) and its T value. It’s clear that in 63 of 68 markets, the series are cointegrated at a 10% or higher criteria. In 2 markets the results suggest some weak cointegration (passing at between 10% and 20%), while in just 3 markets there is little or no evidence of cointegration.<sup>4</sup> 

## **V. Error Correction Models of Housing Supply** 

With these tests validating cointegration for most all of the markets, the simplest approach would be to estimate a version of equation (5) directly – ignoring the possible specification issue raised by equations (6) and (7). This has not been done in the literature, despite the fact the application of an ECM not only gets around the issue of nonstationarity, but also nicely separates long run relationships from short run dynamics. Our statistical ECM version of equation (5) is illustrated in (8), where the β parameters represent the long run cointegrating relationship between the variables in levels. The parameter α0 estimates the speed (or degree) of reversion back to the cointegrating 

> 4 We use the following test statistic critical values [MacKinnon (1996)]: 1% 4.02, 5% 3.39, 10% 3.07, 20% 2.71. 

12 

relationship. The αi and λi account for short-run impacts on price movements that arise from lagged price movements or stock changes. 



Of course, the issue with this single equation ECM is that it assumes the right hand variable (stock) is exogenous. There are two reasons why this is not likely to be true. First, while (5) expresses price as a function of stock (households must be compensated for farther commutes), it is equally true that to provide a larger stock of urban land prices must be higher. Here stock is a function of price. Secondly, if long run equilibrium exists between cities, equations (6) and (7) suggest a negative relationship between prices and stock. An approach that is far more agnostic regarding causality is the application of a Vector Error Correction Model (VECM). This is represented in (9). In this system, we allow for the same single cointegrating vector (with parameters β), but there are two sets of adjustment coefficients (with parameters α, λ versus α’, λ’). 



The estimation of equation (8) or the pair of equations (9) generally can be done in one of two ways, both of which are found in the literature. The first is to estimate the β parameters with a first-stage OLS (where we regress price on stock and a constant), and then use the actual residuals from this first stage in our second stage equations (i.e. equations in (9)) to estimate the α (and λ) parameters, again by OLS. This two-step procedure, originally suggested by Engle and Granger (1987)<sup>5</sup> , provides super-consistent 

> 5 The original Engle-Granger procedure was developed in the context of the single-equation error correction model (ECM). Subsequently, it has been suggested for use in the vector error correction model (VECM), particularly when the standard likelihood-based Johansen (1995) methodology doesn’t work very well due to the violation of distribution assumptions, as is the case in our analysis. For more information, see Lutkepohl (2007). 

13 

estimates of the β values (in the first stage) – provided that P and S are cointegrated. It is also reasonable to assume that number of lags in either (8) or (9) should be the same or similar to that which was used to establish cointegration (for example as in the previous section). This same 2-stage procedure is suggested more recently by Lutkepohl (2007) as a simple and consistent way to estimate the vector system in (9). He refers to this an OLSVECM. 

An alternative has been developed by Johansen (1995) who devises a single-step Maximum Likelihood Estimator (MLE) since both (8) and (9) are nonlinear in their parameters. The one-step procedure has the advantage of also testing for cointegration at the same time as estimating the model. In this procedure the model is often re-estimated multiple times, each with a different lag structure, until some criteria is met and cointegration determined (or not). A problem with the Johansen MLE estimator, however, is that its statistical properties are known _only under the assumption that the errors of (8) and (9) are normally distributed._ We initially experimented with the MLE estimator and achieved results that were often insignificant, and with model parameters that frequently led to instability. To further investigate we applied a test for error normality (Jarque and Bera (1987)). The p-values for this test statistic are reported in Appendix 2 and they represent the probability that the null (normality) is true given observed data. It is clear that there are just a very few market/equations that have even a modest likelihood of normal errors. More than 90% of the market/equations fail the test by a wide margin. 

Since OLS estimation in general is quite robust to the assumption of error normality, we proceed to estimate both models (8) and (9) with the OLS 2-step procedure originally suggested by Engle and Granger (1987) and then subsequently by Lutkepohl (2007). Our OLS-VECM results exhibit none of the stability or significance problems we encountered with the Johansen procedure. 

## **VI. Estimation Results: VECM, ECM** 

Appendix 3 presents the estimates of the OLS-VECM model for 68 MSA. We present the R2 of the price equation, the convergence coefficient αo, in that equation and 

14 

its t statistic, as well as the number of lags used on stock and price changes (in our case we use the same number of lags as used to test for cointegration). We also provide two measures of the “elasticity of supply”. The first elasticity measure is simply equal to the coefficient β2 **,** estimated in the first stage and converted into an elasticity using current stock and price values. 

The second is a more a “short-run” elasticity and is derived from undertaking a 40 period (10 year) price forecast that begins in 2014:3.  While ten years may seem like a long time, in the history of most of these MSAs, ten years of construction normally represents less than 15% of the area’s stock. With a forecast of price and stock changes, we simply divide the change in one by the change in the other to obtain our “short-run” elasticity. It is important to remember that if current prices are below the long-run cointegrating relationship, they will have to “catch up” a bit to provide the new supply that is jointly forecast. Conversely, if current prices are above the cointegrating relationship, little if any price increases may be needed to generate the forecast supply. Thus this 10 year forecast elasticity could differ considerably from the long run estimates. 

On the surface, the VECM elasticities look gratifyingly reasonable. Looking over the results we draw the following observations. 

1). There are 6 negative long-run elasticities, which occur in most Texas markets and two other south central cities. All these markets display continual real price declines over the last 30 years despite significant stock increases. These negative relationships, however, still exhibit cointegration. Presumably cities like Dallas are able to expand with just nominal appreciation because some combination of the real travel costs, real construction costs, or the value of edge rural land has fallen over time. 

2). Other than the negative elasticities in 6 Texas/south central markets there are just a few other “anomalies”. Houston’s long run elasticity is huge, but this seems consistent with the negative short-run elasticity. Prices in Houston are so far above long run trend that they can fall and still generate anticipated future supply. This forecast paradox also holds in many other Texas markets. Finally, Memphis has a negative LR elasticity but a positive SR forecast elasticity. 

3). As for the rest of the markets, the short run elasticities (SR) are all well below their long run elasticity value. Excluding the negative and anomaly markets, the R<sup>2</sup> 

15 

between short and long run is .15 and the average market short run elasticity is 36% of its long run value (.57 versus 1.58). _This results because virtually all markets have prices that are currently well below values implied by their cointegrating relationship; therefore to meet even modest forecast increases in supply, the forecast of price growth has to be quite pronounced (generating a lower forecast elasticity)._ 

4). Overall, the estimated VECM elasticity values seem readily plausible. The long-run values generally are between .20 and 8.1, with the usual list of hypothesized inelastic markets (New York, Boston, the LA and San Francisco regions). Many markets in the South and Mid-West region have much more elastic supply. 

5). The adjustment coefficient in the price equation is statistically significant at the 5% level or higher in all but 2 markets and even in these MSA it passes a 10% test. Adjustment speeds back to the underlying cointegrating relationship average about 5% per quarter or 20% per annum. “Error correction” is an important feature of the relationship between stock and price. 

6). We find that the stock equation within the OLS-VECM does not have the stock re-equilibrating around the cointegrating relationship - as do prices in the price equation. In 60 of 68 markets the cointegrating coefficient in the stock equation is insignificant. In 5 markets it is significant negative and in 3 markets significant positive. A significant negative coefficient implies that when prices are above the value implied by the long term cointegrating value the stock tends to grow more slowly (or declines). This would be illustrative of the migration relationship hypothesized in (6)-(7). A significant positive relationship would be consistent with supply “mean reversion”. In general there is no strong pattern as to how the stock behaves - other than to short run price shocks and its own momentum. 

With respect to the results of the ECM, the LR cointegrating relationship (as estimated in the first stage by regressing price on stock and a constant) is by construction the same as with the OLS-VECM. The price forecast, however, could be quite different as now the stock is treated as exogenous. The stock trajectory assumed is the same as the average growth in each market’s housing stock during the decade before the recent housing “bubble”: 1993:1-2003:1, but scaled by 80%. This latter figure is derived from national estimates of household formation expected over the coming decade relative to 

16 

that of 1993-2003 [U.S. Census (2012)]. In effect, we ask what increase in price will be generated as a result of the growth in stock equal to 80% of the amount it did during the pre-bubble decade – starting from where prices and stock are in 2014:2. The required price change relative to this assumed supply is then converted into a “short run” forecast elasticity. 

In Figures 1 and 2 below, we illustrate the OLS-VECM and ECM forecasts for two very different markets: Boston and Phoenix. The right vertical axis has real price levels, while the left has housing stock.  Boston is like many coastal markets with a strong long run positive real price trend, while Phoenix is like many “sand” states (California, Arizona, Florida and Nevada) where there is little long-run real trend and the “bubble” was most extreme. In Appendix 4 we compare the ECM model with the OLS-VECM model for all markets. Our observations continue below. 

17 

## **Figure 1:  VECM, ECM Forecasts** 



<!-- Start of picture text -->
Boston<br>VECM joint price-stock forecast ECM price forecast given stock<br>2700000 350 2600000 350<br>Boston<br>2600000 2500000<br>300 300<br>2500000<br>2400000<br>2400000<br>2300000<br>250 250<br>2300000<br>2200000<br>2200000<br>200 200<br>2100000<br>2100000<br>2000000<br>2000000<br>150 150<br>1900000 1900000<br>1800000 100 1800000 100<br>1985 1990 1995 2000 2005 2010 2015 2020 1985 1990 1995 2000 2005 2010 2015 2020<br>STK RHPI STKV RHPIV<br><!-- End of picture text -->

## **Figure 2:  VECM, ECM Forecasts** 



<!-- Start of picture text -->
Phoenix<br>VECM joint price-stock forecast ECM price forecast given stock<br>2200000 350 2200000 350<br>Phoenix<br>2000000 325 2000000 325<br>1800000 300 1800000 300<br>1600000 275 1600000 275<br>1400000 250 1400000 250<br>1200000 225 1200000 225<br>1000000 200 1000000 200<br>800000 175 800000 175<br>600000 150 600000 150<br>1985 1990 1995 2000 2005 2010 2015 2020 1985 1990 1995 2000 2005 2010 2015 2020<br>STK RHPI STKV RHPIV<br><!-- End of picture text -->

18 

7). Despite including estimation results for stock, the overall OLS-VECM produces remarkably similar forecast elasticity estimates to the ECM model with its exogenous stock targets. Excluding the 7 markets with “anomalies” and negative elasticities, the simple average forecast price appreciation between 2014:3 and 2024:3 is 39.5%, with the ECM using an average assumed stock growth of 10.6% (based on the 80% rule discussed in the previous section). Under the OLS-VECM framework the average forecast price appreciation is 46.2%, with an endogenous average forecast growth in stock of 11.9%. The OLS-VECM has generally greater price appreciation since it forecasts slightly greater stock growth - as opposed that we assumed based on a national demographic slowdown in household formation. 

8). Despite these differences in the supply forecasts, the two models produce very similar short-run supply elasticity estimates. The average forecast-based supply elasticity with the ECM is .39 as opposed to .46 with the OLS-VECM. Furthermore the correlation between the two elasticities (excluding the 7 anomalies) is .906.  This degree of similarity is interesting because the OLS-VECM derived elasticity is theoretically a different concept from the ECM elasticity. The former is a general equilibrium based derivative as opposed to a partial derivative for a structural equation in the ECM. This suggests that perhaps joint endogeneity makes little difference. 

## **VII. Correlates of Market Supply Elasticity** 

This paper develops several alternative ways of estimating supply elasticities at the MSA level when the underlying data is non-stationary, and arguably subject to bidirectional causality. The error-correction framework also allows us to distinguish between true long run elasticities and short run ones (here 10 years). The results provide a wide range of elasticities across our 68 MSA, and again open up the question of what determines the housing market elasticity in any given area. 

The literature on this question completely focuses on barriers to the development of land: Saiz (2010) on natural geographic barriers, and Gyourko et. al (2008) on regulatory barriers. Several authors also have argued that larger metropolitan markets have inherently smaller elasticities, although in a simple circular monocentric model (such as in 

19 

equation 5), the elasticity turns out to be scale invariant. In our analysis, population is never significant and is not included here. 

In Table 1, we examine how our elasticity estimates vary with the two hypothesized supply-related variables. WRI is the Gyourko et. al. regulatory index, and the land availability variable is actually the reciprocal of the Saiz measure of land _un_ availability. We report equations for both the long run (LR) cointegrating relationship and the short run measure based on the OLS-VECM 10 year forecasts. We use only a subset of the 61 MSA with non-negative elasticities. The results are in the anticipated direction and all but one coefficient is significant statistically. The fact that the LR elasticity is better explained also seems plausible. As discussed before, the SR elasticity is highly impacted by the degree to which prices must mean revert – to get back to the LR supply schedule.  As such, it embodies current market disequilibrium effects and not just longer-term structural factors. Using the equation for the long-run elasticity, the difference in geographic land availability between Boston (index value of .029) and Washington DC (index value of .071) lowers the Boston housing supply elasticity by -.36. Similarly, the regulatory differences between these two markets (1.7 versus .3) generate a further reduction in the elasticity of -.11. The actual elasticity in the Boston MSA is .37 versus Washington’s .77 

**Table 1: Cross Section Determinants of Elasticities** 

## **(t statistics in parenthesis)** 

|Equation|LR Elasticity|SR Elasticity|
|---|---|---|
|R2 (N=45)*|0.384|0.180|
|Constant|1.07  (3.61)|.67  (7.85)|
|WRI|-.686  (-2.30)|-.242 (-2.82)|
|Land Availability (Saiz)|9.75  (3.66)|.208  (.26)|



***** The WRI and Saiz data overlap in only 45 of our 61 MSA 

20 

## **VIII. The role of House Price Elasticities in the Housing “Bubble/Bust”** 

In virtually all of our 68 markets, the period from 2000:1 through 2007:2 exhibits an unprecedented rise in real house prices, followed by a huge decline over 2007:2 to 2012:2.  In this sample of MSAs, the average increase in real prices over 2000:1-2007:2 is 48%. The decline from 2007:2 to 2012:2 is 31% - leaving the average market value in the 2012:2 “trough” at about 2% above 2000:1 levels (in constant dollars).<sup>6</sup> Both Paciorek (2013), and Davidoff (2013), attempt to link this volatility to metrics that _approximate_ a local supply elasticity. Since 2012:2, price rebounds have begun in almost all markets. 

There seems to be consensus that much of the volatility of the last two decades resulted from a positive shock to housing ownership, although there is disagreement over whether this shock originated with the relaxation of mortgage underwriting standards, or simply altered expectations about the returns from housing [Foote-Gerardi-Willen (2012)]. With a national housing finance system, these shocks are widespread, impacting all markets to some extent. In such a case we should expect that the degree of housing price rise and then fall would depend (negatively) on the supply elasticity of each market. The relationship, however, could be quite imperfect as there were nuances to the rise and fall that were unique to each area. For example, second home havens seem to have experienced a larger “bubble” [Chinco-Mayer (2012)]. 

In equation (10) we regress each market’s price rise (2007:2 / 2000:1) in real dollars against our LR measure of supply elasticity from the OLS-VECM. We exclude 7 markets with negative elasticities as conceptually these markets have high elasticities, while numerically a negative elasticity is closest in value to complete inelasticity. Despite a low R2 there is a strong and significantly negative relationship to the estimated LR elasticity.  Where supply elasticity is largest, the “bubble” was smaller. 

> 6 For ease, we have assumed a common period across markets of peak prices (2007:2) as well a trough prices (2012:2) in constant dollars. 

21 



In equation (11) we regress each market’s real price fall (2012:2 / 2007:2) against our LR measure of supply elasticity from the OLS-VECM. We also include the magnitude of the real price rise over the prior 7 years. The fit of this equation is much stronger and, overwhelmingly, markets that had the largest price bubble also experience the largest price drop during 2007:2-2012:2.  The role of a market’s supply elasticity over this period, however, is much harder to anticipate. Our results indicate that markets with higher long run elasticities (LR) had greater price declines – a result which is quite significant. Since little construction was occurring over this period, one can question why the LR elasticity should matter at all! One interpretation of our results is that markets with high LR elasticities have difficultly contracting their supply during downturns. Hence, against negative demand shocks – price declines are greater. Following the framework of GlaeserGyourko (2005), we might alternatively say that markets with elastic upward supply rotate that supply counter-clockwise the greatest in the presence of negative demand shocks – again creating steeper price declines. 



## **IX. House Price Appreciation and Recovery from the Great Recession** 

The advantage of the error correction approach is not confined solely to its ability to provide consistent estimates of long-run parameters, but also in the fact that it offers an excellent mechanism for out of sample forecasting with its flexible handling of short-run dynamics. The unprecedented rise in house prices from 2000 to 2007 and the almost equal fall over 2007-2012 has many asking whether, when, and by how much prices will recover. This is not just of academic interest, for as many as 21% of American homes may have mortgage balances that exceed their current prices (Core Logic, 2012). Furthermore, 

22 

the future balance sheets of many financial institutions, as well as Federal housing policy certainly will be influenced by the shape and extent of the housing price recovery. 

Against this background, we take our preferred model (the OLS-VECM approach) and examine its joint forecast of housing stock and prices in each of our 68 MSAs. The forecast is for a decade beginning in 2014:3. In almost all markets, the forecasts look as realistic and plausible as the left-hand frames of Figures 1 and 2. The results for each market are presented in Appendix 5. The first 3 columns provide price levels in 2007:2 (the assumed “peak”), 2012:2 (the assumed “trough”) and currently (2014:3). Then there are a series of price ratios – the first of which is the extent of the price rebound over the last 2 years. Since 2012:2 there have been price rebounds in most markets with 31 out of 68 markets exceeding the average market rebound of 11%. 

Following the rebound to date, the next ratio is the forecast of 2024:2 price levels relative to 2014:3 in real dollars. This gives the remaining _forecast_ rebound through 2024:2, and its average across the 68 markets is 21% (again in real dollars). Thus, by 2024, the average market will have prices that are 33% above the 2012:2 trough – in real terms<sup>7</sup> . This significant price rebound, however, can be quite different than the recovery of prices to previous 2007:2 peak levels. 

The next to final column gives the ratio of 2024:2 forecast prices to those in 2007:2 – again in constant dollars. The average market by then will have prices that are still 6% _below_ 2007:2 in real terms. The average, however, hides significant differences, with some area prices being as much as 35% below the previous peak (e.g. Fort Lauderdale) while others are 10% or more above (e.g. New York).  In general, it appears that the so-called “sand states”, which had the largest price drops, will recover the least by 2024. The final columns in Appendix 5 examines the ratio of forecast prices in 2024:2 to those in 2007 – in current and nominal dollars. This conversion uses actual CPI inflation from 2007.2 to 2014:3 and assumes 2% annual CPI inflation from 2014:3 through 2024:2. 

> 7 This forecast assumes that stock and prices revert to their long-term equilibrium relationship, as represented by the VECM, absent any exogenous shocks. In practical terms, the forecast should generally be of the correct magnitude and direction, absent any _large_ exogenous shocks (as the economy will inevitably experience exogenous shocks of some sort). 

23 

Given current yields on Treasuries and TIPS, this estimate of future inflation is a bit conservative, but our analysis is only meant to be illustrative of what might happen to nominal house prices over the next decade. This is the more relevant metric for assessing the future of US mortgage leverage ratios. 

In Appendix 5, we can see that out of 68 markets, _nominal_ prices will fail to get back to 2007:2 levels by 2024:2 in only 7 markets. Four of these markets are in Florida, while the other three are in Arizona, Nevada and inland California. Many of these markets are forecasts to have quite high price appreciation between 2012 and 2024. Their lack of a full recovery seems due to the enormous drop in prices between 2007 and 2012. Given this bleak outlook, it will be instructive to see if strategic foreclosures become more common in such areas. 

To help see these patterns across markets, we present two final regressions. In the first one, we attempt to explain the cross section variation in price rebound. In the second, the cross section variation in price recovery. All price changes are again real. 



In both equations (12) and (13), we see that a market’s rebound and recovery will be hindered by higher supply elasticity. Since construction will be occurring during this period, this is an expected result and also in line with the negative impact of supply elasticity on price gains during the 2007/2000 boom period. It also makes sense that if a market had a greater price boom during 2000-2007, its rebound as well as recovery will be less. Where the two equations differ is in the impact of the price drop (or bust). A greater price drop (smaller 2012/2007 ratio) will lead to a stronger price rebound, but to a lower eventual price recovery. Recovery ratios (new price peaks) will be stronger in inelastic markets with smaller booms and smaller busts. Rebounds will be strongest in inelastic markets with smaller booms and larger busts. 

24 

With these forecasts, it is instructive to ask if housing generally will be a good investment in the next decade. To answer this question, we should focus on the price rebounds. Across our 68 markets, cumulative _nominal_ price inflation will average 62% between the 2012 trough and 2024<sup>8</sup> . This ranges from just 10% in many Texas markets to 70% or more in _two_ types of markets. The first are traditional inelastic costal markets (LA, SF, Boston, NY). The second are areas hard hit by the “bubble” years (Phoenix, Florida…). In the former there will be price recovery while in the latter generally not.  In Poterba (1984), as well as other more recent theoretical models of housing demand, the long-run cost of owning a home is approximately equal to the after-tax mortgage rate (and opportunity cost of equity) minus nominal (untaxed) house price appreciation. With housing capital gains currently untaxed, mortgage rates in the 4.5% range and the mortgage interest deduction continuing, the annual long run cost of owning a should again turn negative as it did in the late 1970s, late 1990s and mid-2000s. This should clearly help to spur future home ownership, housing consumption as well as new housing construction. 

> 8 Again, this assumes unhindered mean-reversion without exogenous shocks. 

25 

## **References** 

Abel, Andrew and Olivier Blanchard, (1986), "The present value of profits and cyclic movements in investment" _, Econometrica_ , 54,2, 249-73. 

Alberts, W. W.(1962), "Business Cycles, Residential Construction Cycles, and the Mortgage Market," _The Journal of Political Economy_ , LXX,1, 263-281. 

Blackley, D.M., (1999) “The Long Run Elasticity of new housing Supply in the U.S.: Empirical Evidence for 1950 to 1994”, _Journal of Real Estate Finance and Economics_ , 18 (1) pp 25-42. 

Campbell, S., M. Davis, J. Gallin, R. Martin, (2009), “What moves Housing Markets: A variance decomposition of the Price-Rent Ratio”, _Journal of Urban Economics_ 66(2), 90102. 

Cannon, S., N. Miller, G. Pandher (2006),“Risk and Return in the US Housing Market: A Cross-Section Asset-Pricing Approach”, _Real Estate Economics_ , 34, 4, 519-552. 

Case, Karl and Robert Shiller (1989), “The Efficiency of Market for Single-Family Homes,” _American Economic Review_ , Vol79, no.1, 125-137. 

Capozza, D., P. Hendershott, C. Mack (2004), “An Anatomy of Price Dynamics in Illiquid Markets: Analysis and Evidence from Local Housing Markets”, _Real Estate Economics_ , 32, 1, 1-21. 

Chinco, A. and Mayer, C. (2012) “Distant Speculators and Asset Bubbles in the Housing Market”, Stern School, NYU. 

Core Logic, “Equity Report: 2012:Q4”, Irvine, Ca. 

Davidoff, T. (2013) “Supply Elasticity and the Housing Cycle of the 2000s”, _Real Estate Economics_ , 41,4, pp793-813. 

DiPasquale, D. and W. Wheaton, (1992) "The Cost of Capital, Tax Reform, and the Future of the Rental Housing Market," _Journal of Urban Economics_ , 31, 337-359. 

DiPasquale, D. and W. Wheaton, 1994, "Housing Market Dynamics and the Future of Housing Prices", _Journal of Urban Economics_ ,35,1, 1-27. 

Eckhout, Jan, R. Pinheiro, K. Schmidheiny, "Spatial Sorting…”, CESIFO Working Paper 3274 (December, 2010). 

Engle, R. and Granger, C.,(1987) ”Co-integration and Error Correction: Representation, estimation and Testing”, _Econometrica_ , 55 (2) pp 252-276. 

26 

Foote, C., Gerardi, K. and Willen, P, “Why Did So Many People Make So Many Ex Post bad Decisions? Causes of the Foreclosure Crisis”, Federal Reserve Bank of Atlanta, Working Paper 2012-7. 

Glaeser, E., Gyrouko, J. (2005), “Urban Decline and Durable Housing”, _Journal of Political Economy_ , 113 (2), pp. 345-375. 

Glaeser, E., Gyrouko, J. (2005), and Saiz A. “Housing Supply and Housing Bubbles” _Journal of Urban Economics_ ,  64 (2), pp 9180217. 

Gyrouko, J., Saiz, A. and Summers, A. (2008), “A new measure of the local Regulatory Environment for Housing Markets: the Wharton Residential Land Use Index” _Urban Studies_ , 45, pp 693-729. 

Granger, C.W. and Newbold, P.  (1974), “Spurious Regressions in Econometrics”, _Journal of Econometrics,_ 2, pp111-120 

Grebler, L., and W. Burns,(1982), "Construction cycles in the U.S.", _AREUEA Journal,_ 10,2, 201-222. 

Green, R.K., Malpezzi, S. and Mayo, S.K., (2005) “Metropolitan Specific estimates of the price elasticity of Housing supply and their sources”, _American Economic Review_ ,  95 (2) pp 334-339. 

Hamilton, J. D. 1994. _Time Series Analysis_ . Princeton: Princeton University Press. 

Harter-Dreiman, M. (2004) “Drawing Inferences about Housing Supply Elasticity from house price responses to income shocks”, _Journal of Urban Economics, 55,_ 2, 316-337. 

Helsley, R. & Sullivan, A. (1991). "Urban subcenter formation," _Regional Science and Urban Economics_ ,  vol. 21(2), pages 255-275. 

Jarque, C.M. and Bera, A.K., (1987), “Tests for normality of observations and regression residuals”, _International Statistical Review,_ 2, pp 163-172. 

Johansen, S. (1995), _Likelihood-Based Inference in Cointegrated Vector Autoregressive Models_ , Oxford, Oxford University Press. 

Lutkepohl, H. (2007), _New Introduction to Multiple Time Series_ , New York, Springer, 2<sup>nd</sup> Edition. 

Mackinnon, J., (1996) “Numerical Distribution Functions for Unit Root and Cointegration Tests”, _Journal of Applied Econometrics_ , 11 (6), pp 212-243. 

McMillen, D. and Smith S. (2003), "The Number of Subcenters in large Urban Areas”, _Journal of Urban Economics_ , 53, 3, pp. 321-339. 

27 

Mankiw, G. and D. Weil, (1989), “The Baby Boom, the Baby Bust, and the Housing Market”, _Regional Science and Urban Economics_ , 19(2), 235-258. 

Mayer, C. and T. Somerville,( 2000), “Residential Construction: Using the Urban Growth Model to estimate Housing Supply”, _Journal of Urban Economics_ , 48, 5, 85-109. 

Ortalo-Magne, F. and S. Rady , 2006, “Housing Market Dynamics: On the contribution of Income Shocks and Credit Constraints,” _Review of Economic Studies,_ 73, 459-485. 

Paciorek, A. (2013) “Supply Constraints and Housing Market Dynamics” _Journal of Urban Economics_ , 77 (1), pp 11-26. 

Poterba, J., (1984) “Tax Subsidies to owner occupied housing: an asset market approach”, _Quarterly Journal of Economics_ , 99, pp 729-752. 

Saiz, A., (2010). “The Geographic Determinants of Housing Supply”, _Quarterly Journal of Economics_ , 100, 3 500-530. 

Somerville,  T. (1999), “The Industrial Organization of Housing Supply:…”, _Real Estate Economics,_ 27, 4,  pp 669-695. 

Stijn Van Nieuwerburgh, Pier Olivier-Weil, (2009) “Why has House Price Dispersion Gone up?”, NYU Working Paper FIN 06-010. 

Topel, R. and S. Rosen,(1988), "Housing Investment in the United States," _Journal of Political Economy_ , 96, 3, 718-740. 

U.S. Census, 2012 Population Projections, Washington, D.C. 

28 

## **Appendix 1: Cointegration Tests: Price on Stock** 

|MSA|Lags|R2|lagged error|"t"|
|---|---|---|---|---|
|Albuquerque|6|0.32024|‐0.0673|‐3.82901|
|Atlanta|8|0.41297|‐0.06548|‐4.64027|
|Austin|8|0.16587|‐0.07455|‐3.34747|
|Baltimore|5|0.51984|‐0.03385|‐3.6828|
|BatonRouge|12|0.20189|‐0.0439|‐3.0811|
|Birmingham|11|0.11265|‐0.08477|‐3.04278|
|Boston|7|0.59112|‐0.03356|‐3.65046|
|Buffalo|9|0.14438|‐0.06353|‐3.51855|
|Charlotte|7|0.26587|‐0.07148|‐3.87351|
|Chicago|8|0.51213|‐0.05238|‐4.25278|
|Cincinnati|10|0.31233|‐0.03598|‐2.47888|
|Cleveland|11|0.28861|‐0.03515|‐2.79672|
|ColoradoSprings|14|0.26347|‐0.04729|‐2.8921|
|ColumbiaSC|9|0.09237|‐0.06877|‐2.7065|
|Columbus|8|0.25696|‐0.04527|‐3.12586|
|Dallas|7|0.33074|‐0.02565|‐2.50102|
|Dayton*|4|0.0294|‐0.00489|‐0.36047|
|Denver|6|0.38252|‐0.03689|‐3.68002|
|Detroit|7|0.56745|‐0.02589|‐3.78181|
|Edison|4|0.64295|‐0.02579|‐3.43147|
|FortLauderdale|4|0.62783|‐0.03962|‐4.42915|
|FortWorth|11|0.28922|‐0.02849|‐2.47666|
|Greensboro|9|0.16877|‐0.07978|‐3.1936|
|Hartford|4|0.51551|‐0.03303|‐3.47075|
|Honolulu|5|0.57154|‐0.03953|‐3.88178|
|Houston|6|0.4142|‐0.02983|‐3.28142|
|Indianapolis*|6|0.16624|‐0.02208|‐1.5903|
|Jacksonville|6|0.42967|‐0.04313|‐3.74103|
|KansasCity|10|0.31835|‐0.03785|‐3.07308|
|LasVegas|5|0.63266|‐0.04412|‐4.30161|
|LongIsland|5|0.55139|‐0.0306|‐3.75965|
|LosAngeles|3|0.70792|‐0.02674|‐3.60621|
|Louisville|9|0.15082|‐0.04877|‐2.62587|
|Memphis|10|0.26859|‐0.0937|‐2.84539|
|Miami|4|0.62738|‐0.03769|‐4.09719|
|Minneapolis|7|0.50772|‐0.04676|‐4.71245|
|Nashville|7|0.30665|‐0.07921|‐4.33257|
|Newark|12|0.59066|‐0.03288|‐2.61944|
|NewOrleans*|5|0.16261|‐0.0218|‐1.90423|



29 

|NewYork|5|0.64177|‐0.03023|‐3.67381|
|---|---|---|---|---|
|Norfolk|6|0.57995|‐0.0284|‐3.50379|
|Oakland|3|0.66258|‐0.03102|‐3.81129|
|OklahomaCity|11|0.32611|‐0.03503|‐3.24388|
|OrangeCounty|3|0.67675|‐0.02681|‐3.46117|
|Orlando|4|0.5906|‐0.03422|‐3.5475|
|Philadelphia|6|0.44645|‐0.03228|‐3.24411|
|Phoenix|6|0.61922|‐0.04171|‐3.68124|
|Pittsburgh|5|0.15525|‐0.08314|‐2.34172|
|Portland|6|0.56075|‐0.06262|‐4.74833|
|Providence|8|0.62474|‐0.03551|‐3.6358|
|Raleigh|7|0.35982|‐0.07692|‐4.37828|
|Richmond|7|0.40817|‐0.05157|‐4.1355|
|Riverside|4|0.68481|‐0.02953|‐3.24296|
|Sacramento|4|0.68015|‐0.03142|‐3.77033|
|SaltLakeCity|6|0.39831|‐0.05486|‐3.59059|
|SanAntonio|11|0.39942|‐0.05062|‐3.18296|
|SanDiego|3|0.60435|‐0.02671|‐3.26442|
|SanFrancisco|3|0.57729|‐0.0314|‐3.37153|
|SanJose|3|0.54941|‐0.03675|‐3.31414|
|Seattle|6|0.5824|‐0.05088|‐4.27402|
|StLouis|9|0.44595|‐0.04976|‐3.91582|
|Tampa|5|0.5124|‐0.03648|‐3.45092|
|Tucson|5|0.38834|‐0.06784|‐3.8429|
|Tulsa|6|0.17356|‐0.03769|‐3.23281|
|Ventura|3|0.63214|‐0.03168|‐3.62981|
|WashingtonDC|5|0.59373|‐0.03306|‐3.3776|
|WestPalmBeach|4|0.66319|‐0.03109|‐3.74414|
|Wilmington|6|0.50791|‐0.04117|‐4.0306|



* Market not cointegrated 

30 

**Appendix 2:  Jarque‐Bera Test on Null of Normality in Residuals*** 

||P‐Value for Eqn|P‐Value for Eqn||
|---|---|---|---|
|Market|D_rhpi|D_stk|P‐Value for Joint Test on Both Eqns|
|Albuquerque|0.002264966|6.01E‐86|2.77E‐86|
|Atlanta|4.8299E‐05|0.382991668|0.000220088|
|Austin|2.3787149211e‐316|0.007115151|1.2400815401e‐315|
|Baltimore|5.81E‐06|1.49E‐47|1.05E‐50|
|Baton Rouge|0.960285202|1.32E‐65|1.90E‐63|
|Birmingham|0.006731155|0.000753312|6.68924E‐05|
|Boston|1.28E‐08|1.04E‐27|1.09E‐33|
|Buffalo|0.262237226|0.010431756|0.018879451|
|Charlotte|9.49E‐12|0.009049121|2.67E‐12|
|Chicago|7.06E‐12|0.005474005|1.23E‐12|
|Cincinnati|5.99716E‐05|6.80E‐13|1.58E‐15|
|Cleveland|0.008833102|0.023350473|0.001956635|
|Colorado Sprgs|0.001259587|0.093055686|0.001178157|
|Columbia SC|0.000169894|0.784358993|0.00132235|
|Columbus|0.00543286|0.287783242|0.011664915|
|Dallas|6.31E‐06|7.85E‐08|1.45E‐11|
|Dayton|0|1.47E‐08|0|
|Denver|2.62E‐06|0.000890351|4.87E‐08|
|Detroit|3.71E‐94|9.12E‐07|7.79E‐98|
|Edison|8.40E‐06|0.002533053|3.97E‐07|
|FortLauderdale|5.90E‐11|5.84E‐111|9.60E‐119|
|FortWorth|0.889067301|0.00141103|0.009635842|
|Greensboro|0.122385037|0.865577726|0.343748837|
|Hartford|0.936205833|3.16E‐34|2.31E‐32|
|Honolulu|0|6.41995E‐05|0|
|Houston|0.003938721|7.45E‐06|5.39E‐07|
|Indianapolis|6.64E‐224|0.244704997|8.39E‐222|
|Jacksonville|0.000735122|0.26168822|0.001838328|
|Kansas City|0.000881334|0.20280275|0.001721165|
|Las Vegas|4.24E‐11|0.001066571|1.44E‐12|
|Long Island|4.56E‐10|1.09467E‐05|1.69E‐13|
|Los Angeles|2.11E‐34|1.03E‐54|4.41E‐86|
|Louisville|1.69803E‐05|0.944645102|0.000193132|
|Memphis|0.000121858|0.292256695|0.000400398|
|Miami|1.22E‐15|2.88E‐83|7.94E‐96|
|Minneapolis|0.122685371|0.629407004|0.274985414|
|Nashville|1.44E‐21|0.020202206|1.54E‐21|



31 

|New Orleans|0.056541011|1.04E‐18|2.67E‐18|
|---|---|---|---|
|New York|7.94E‐14|0|0|
|Newark|3.36E‐08|0.005575325|4.38E‐09|
|Norfolk|0.00177531|0.333603315|0.004993599|
|Oakland|1.88E‐19|0.002270435|2.14E‐20|
|Oklahoma City|0.184399551|2.75E‐06|7.85E‐06|
|Orange County|9.13E‐33|0.429493243|2.97E‐31|
|Orlando|3.42E‐06|0.73614544|3.4949E‐05|
|Philadelphia|0.000325059|0.285431848|0.000954289|
|Phoenix|3.73E‐08|0.003743776|3.30E‐09|
|Pittsburgh|0.277957752|0.235160837|0.243664971|
|Portland|3.48E‐08|0.030131595|2.27E‐08|
|Providence|0.002348382|5.20E‐31|9.38E‐32|
|Raleigh|0.005760123|0.000339034|2.76258E‐05|
|Richmond|0.001199553|0.002920793|4.75154E‐05|
|Riverside|4.03E‐14|6.26E‐22|2.04E‐33|
|Sacramento|1.43E‐09|5.73E‐12|3.87E‐19|
|Salt Lake City|4.31E‐33|0.128949954|4.31E‐32|
|San Antonio|4.45E‐38|0.000912799|3.82E‐39|
|San Diego|7.67E‐34|2.31E‐10|1.77E‐41|
|San Francisco|5.50E‐14|0.589145806|1.04E‐12|
|San Jose|2.26E‐08|0.000314474|1.89E‐10|
|Seattle|1.04E‐29|0.043541031|3.22E‐29|
|St Louis|5.33E‐11|0.000339227|5.90E‐13|
|Tampa|1.03E‐12|0.535734153|1.62E‐11|
|Tucson|1.02E‐29|0.297427577|2.10E‐28|
|Tulsa|2.68256E‐05|9.76E‐13|1.03E‐15|
|Ventura|2.35E‐64|0.02918028|1.04E‐63|
|Washington DC|4.05E‐13|0.897212944|1.08E‐11|
|West P Beach|4.61E‐07|0.230991055|1.81E‐06|
|Wilmington|0.117280726|4.82E‐14|1.91E‐13|



* This test is based on the test as discribed in Lutkepohl (2005, p 174‐ 181) as applied to the augmented VAR in first differences (i.e. VECM) and is implemented in Stata software. 

32 

## **Appendix 3: VECM Results, LR and Forecast Elasticities** 

||||||LR|Price|Stock|VEC|
|---|---|---|---|---|---|---|---|---|
|MSA|Lag|R2 Price|α coef.|"t"|Elasticity|Forecast|forecast|Elasticity|
|Albuquerque|6|0.352|‐0.062|‐3.244|1.851|0.129|0.175|0.739|
|Atlanta|8|0.474|‐0.124|‐4.895|5.287|0.197|0.242|0.814|
|Austin|8|0.287|‐0.092|‐3.269|2.361|0.151|‐0.041|‐3.705|
|Baltimore|5|0.515|‐0.034|‐3.564|0.631|0.075|0.243|0.310|
|BatonRouge|12|0.375|‐0.163|‐4.245|2.635|0.114|0.022|5.222|
|Birmingham|11|0.154|‐0.094|‐2.377|1.204|0.126|0.308|0.410|
|Boston|7|0.665|‐0.030|‐2.997|0.377|0.080|0.357|0.225|
|Buffalo|9|0.177|‐0.062|‐2.478|1.158|0.046|0.071|0.639|
|Charlotte|7|0.326|‐0.118|‐3.958|2.787|0.145|0.157|0.924|
|Chicago|8|0.583|‐0.054|‐3.175|0.604|0.118|0.466|0.252|
|Cincinnati|10|0.402|‐0.063|‐2.880|2.227|0.146|0.400|0.365|
|Cleveland|11|0.332|‐0.043|‐2.389|1.518|0.087|0.609|0.144|
|ColoradoSprings|14|0.352|‐0.055|‐2.179|1.643|0.186|0.270|0.688|
|ColumbiaSC|9|0.136|‐0.094|‐2.678|3.153|0.155|0.236|0.655|
|Columbus|8|0.324|‐0.094|‐4.137|2.347|0.159|0.274|0.583|
|Dallas|7|0.342|‐0.030|‐2.200|‐2.803|0.125|‐0.201|‐0.623|
|Dayton|4|0.160|‐0.067|‐3.736|7.529|0.091|0.304|0.298|
|Denver|6|0.403|‐0.053|‐3.349|1.221|0.174|0.118|1.480|
|Detroit|7|0.566|‐0.028|‐2.588|0.758|0.070|0.851|0.083|
|Edison|4|0.678|‐0.020|‐2.476|0.591|0.122|0.408|0.299|
|FortLauderdale|4|0.610|‐0.040|‐4.183|0.997|0.074|0.102|0.730|
|FortWorth|11|0.375|‐0.026|‐1.434|‐1.907|0.131|‐0.150|‐0.874|
|Greensboro|9|0.307|‐0.220|‐4.764|6.554|0.115|0.184|0.621|
|Hartford|4|0.577|‐0.031|‐2.489|1.121|0.076|0.287|0.266|
|Honolulu|5|0.601|‐0.041|‐3.815|0.527|0.080|0.128|0.623|
|Houston|6|0.458|‐0.041|‐3.008|84.103|0.121|‐0.172|‐0.708|
|Indianapolis|6|0.221|‐0.106|‐3.336|6.519|0.162|0.192|0.845|
|Jacksonville|6|0.574|‐0.084|‐5.058|1.428|0.189|0.362|0.523|
|KansasCity|10|0.397|‐0.033|‐2.430|3.252|0.140|0.232|0.603|
|LasVegas|5|0.641|‐0.057|‐4.665|8.145|0.236|0.255|0.926|
|LongIsland|5|0.596|‐0.028|‐3.196|0.226|0.051|0.426|0.121|
|LosAngeles|3|0.720|‐0.028|‐3.524|0.356|0.067|0.186|0.362|
|Louisville|9|0.236|‐0.141|‐4.126|1.070|0.118|0.284|0.417|
|Memphis|10|0.340|‐0.183|‐3.807|‐12.193|0.151|0.173|0.872|
|Miami|4|0.675|‐0.048|‐4.481|0.651|0.125|0.304|0.411|
|Minneapolis|7|0.544|‐0.042|‐3.819|0.968|0.123|0.324|0.381|
|Nashville|7|0.447|‐0.143|‐5.777|1.798|0.163|0.111|1.475|
|Newark|12|0.670|‐0.044|‐2.657|0.386|0.072|0.358|0.201|
|NewOrleans|5|0.159|‐0.022|‐1.385|1.542|0.085|0.045|1.879|
|NewYork|5|0.725|‐0.037|‐3.604|0.222|0.074|0.567|0.130|



33 

|Norfolk|6|0.556|‐0.027|‐3.138|0.994|0.109|0.259|0.421|
|---|---|---|---|---|---|---|---|---|
|Oakland|3|0.673|‐0.033|‐3.887|0.491|0.074|0.170|0.436|
|OklahomaCity|11|0.382|‐0.027|‐1.731|‐2.090|0.097|‐0.171|‐0.564|
|OrangeCounty|3|0.686|‐0.028|‐3.502|0.590|0.099|0.151|0.654|
|Orlando|4|0.645|‐0.037|‐3.314|2.360|0.229|0.297|0.770|
|Philadelphia|6|0.488|‐0.025|‐2.271|0.432|0.060|0.238|0.251|
|Phoenix|6|0.599|‐0.049|‐3.096|1.968|0.174|0.172|1.007|
|Pittsburgh|5|0.166|‐0.108|‐2.806|0.740|0.052|0.094|0.559|
|Portland|6|0.578|‐0.049|‐3.217|0.701|0.124|0.215|0.578|
|Providence|8|0.650|‐0.034|‐3.258|0.357|0.054|0.409|0.132|
|Raleigh|7|0.441|‐0.066|‐2.619|3.236|0.182|0.130|1.401|
|Richmond|7|0.438|‐0.046|‐3.516|1.292|0.126|0.176|0.717|
|Riverside|4|0.711|‐0.039|‐3.471|1.384|0.135|0.188|0.717|
|Sacramento|4|0.697|‐0.041|‐4.026|1.019|0.108|0.228|0.473|
|SaltLakeCity|6|0.439|‐0.075|‐3.925|1.436|0.224|0.210|1.069|
|SanAntonio|11|0.410|‐0.047|‐2.007|‐4.984|0.079|‐0.150|‐0.525|
|SanDiego|3|0.599|‐0.028|‐3.206|0.621|0.096|0.183|0.524|
|SanFrancisco|3|0.632|‐0.036|‐3.758|0.224|0.051|0.227|0.225|
|SanJose|3|0.577|‐0.038|‐3.300|0.416|0.094|0.247|0.382|
|Seattle|6|0.591|‐0.048|‐3.762|0.684|0.120|0.209|0.575|
|StLouis|9|0.434|‐0.039|‐2.711|1.271|0.104|0.295|0.352|
|Tampa|5|0.562|‐0.041|‐3.285|1.171|0.130|0.247|0.526|
|Tucson|5|0.318|‐0.067|‐3.102|1.186|0.145|0.333|0.435|
|Tulsa|6|0.180|‐0.035|‐1.943|‐2.302|0.095|‐0.089|‐1.074|
|Ventura|3|0.646|‐0.033|‐3.643|0.589|0.094|0.207|0.456|
|WashingtonDC|5|0.607|‐0.031|‐2.804|0.771|0.132|0.244|0.540|
|WestPalmBeach|4|0.666|‐0.032|‐3.758|1.534|0.103|0.110|0.936|
|Wilmington|6|0.530|‐0.038|‐3.459|0.812|0.091|0.305|0.299|



34 

## **Appendix 4: ECM comparison with VECM** 

|||||Stock|Price|VECM|Stock|Price|ECM|
|---|---|---|---|---|---|---|---|---|---|
|MSA|Lags|Price|Stock|forcst|forcst|Elasticity|forcst|forcst|Elasticity|
|Albuquerque|6|155.51|381972|0.129|0.175|0.739|0.125|0.181|0.691|
|Atlanta|8|158.87|2211493|0.197|0.242|0.814|0.205|0.195|1.048|
|Austin|8|241.43|769978.2|0.151|‐0.041|‐3.705|0.166|‐0.052|‐3.191|
|Baltimore|5|209.44|1156768|0.075|0.243|0.310|0.080|0.246|0.326|
|BatonRouge|12|194.17|342961.8|0.114|0.022|5.222|0.090|‐0.019|‐4.855|
|Birmingham|11|162.71|510400.7|0.126|0.308|0.410|0.089|0.217|0.410|
|Boston|7|245.76|2414701|0.080|0.357|0.225|0.053|0.313|0.168|
|Buffalo|9|159.02|525393|0.046|0.071|0.639|0.043|0.063|0.680|
|Charlotte|7|167.96|780906.8|0.145|0.157|0.924|0.184|0.167|1.101|
|Chicago|8|159.52|3531471|0.118|0.466|0.252|0.085|0.410|0.208|
|Cincinnati|10|146.14|930424.9|0.146|0.400|0.365|0.108|0.199|0.543|
|Cleveland|11|128.81|963485.8|0.087|0.609|0.144|0.058|0.266|0.217|
|ColoradoSprings|14|178.92|275842.9|0.186|0.270|0.688|0.165|0.221|0.746|
|ColumbiaSC|9|157.57|346365.8|0.155|0.236|0.655|0.114|0.152|0.748|
|Columbus|8|154.86|817160.7|0.159|0.274|0.583|0.134|0.192|0.695|
|Dallas|7|186.45|1757347|0.125|‐0.201|‐0.623|0.146|‐0.185|‐0.786|
|Dayton|4|123.3|388169.6|0.091|0.304|0.298|0.078|0.218|0.356|
|Denver|6|226.04|1223285|0.174|0.118|1.480|0.160|0.127|1.267|
|Detroit|7|135.88|1961835|0.070|0.851|0.083|0.083|0.790|0.105|
|Edison|4|214.66|972324.9|0.122|0.408|0.299|0.089|0.309|0.288|
|FortLauderdale|4|215.84|809980|0.074|0.102|0.730|0.125|0.148|0.846|
|FortWorth|11|172.31|869676.6|0.131|‐0.150|‐0.874|0.112|‐0.142|‐0.785|
|Greensboro|9|147.77|690052|0.115|0.184|0.621|0.095|0.127|0.754|
|Hartford|4|170.26|510835.6|0.076|0.287|0.266|0.054|0.118|0.454|
|Honolulu|5|201.1|341987|0.080|0.128|0.623|0.063|0.072|0.878|
|Houston|6|217.94|2461999|0.121|‐0.172|‐0.708|0.113|‐0.177|‐0.635|
|Indianapolis|6|147.48|842612.5|0.162|0.192|0.845|0.144|0.152|0.946|
|Jacksonville|6|189.78|620535.3|0.189|0.362|0.523|0.138|0.193|0.716|
|KansasCity|10|166.01|901939.5|0.140|0.232|0.603|0.119|0.183|0.652|
|LasVegas|5|144.32|867921.5|0.236|0.255|0.926|0.261|0.282|0.926|
|LongIsland|5|244.33|1043503|0.051|0.426|0.121|0.041|0.376|0.108|
|LosAngeles|3|273.27|3474897|0.067|0.186|0.362|0.028|0.051|0.552|
|Louisville|9|169.23|572533.4|0.118|0.284|0.417|0.107|0.224|0.480|
|Memphis|10|142.41|562005.6|0.151|0.173|0.872|0.131|0.126|1.039|
|Miami|4|230.36|995622|0.125|0.304|0.411|0.095|0.195|0.490|
|Minneapolis|7|197.35|1384600|0.123|0.324|0.381|0.121|0.315|0.384|
|Nashville|7|192.78|701561.7|0.163|0.111|1.475|0.140|0.094|1.481|
|Newark|12|205.13|865777.4|0.072|0.358|0.201|0.051|0.137|0.370|
|NewOrleans|5|201|543708.8|0.085|0.045|1.879|0.067|0.029|2.338|



35 

|NewYork|5|226.95|4763956|0.074|0.567|0.130|0.029|0.207|0.140|
|---|---|---|---|---|---|---|---|---|---|
|Norfolk|6|209.78|708264.5|0.109|0.259|0.421|0.099|0.232|0.429|
|Oakland|3|263.82|993496.5|0.074|0.170|0.436|0.069|0.143|0.482|
|OklahomaCity|11|186.72|559530.5|0.097|‐0.171|‐0.564|0.080|‐0.169|‐0.474|
|OrangeCounty|3|283.39|1068968|0.099|0.151|0.654|0.079|0.120|0.659|
|Orlando|4|176.6|980297.2|0.229|0.297|0.770|0.181|0.199|0.909|
|Philadelphia|6|218.79|2172730|0.060|0.238|0.251|0.057|0.205|0.278|
|Phoenix|6|209.47|1846218|0.174|0.172|1.007|0.186|0.172|1.082|
|Pittsburgh|5|178.96|1115075|0.052|0.094|0.559|0.047|0.077|0.607|
|Portland|6|220.84|952531.4|0.124|0.215|0.578|0.138|0.247|0.557|
|Providence|8|198.3|697802.9|0.054|0.409|0.132|0.050|0.419|0.118|
|Raleigh|7|165.11|742905.3|0.182|0.130|1.401|0.183|0.134|1.364|
|Richmond|7|189.82|544267.9|0.126|0.176|0.717|0.116|0.175|0.664|
|Riverside|4|224.75|1519250|0.135|0.188|0.717|0.106|0.057|1.836|
|Sacramento|4|204.39|878541.2|0.108|0.228|0.473|0.125|0.216|0.579|
|SaltLakeCity|6|204.86|437668.2|0.224|0.210|1.069|0.210|0.197|1.064|
|SanAntonio|11|187.93|865591.3|0.079|‐0.150|‐0.525|0.101|‐0.134|‐0.751|
|SanDiego|3|265.82|1181679|0.096|0.183|0.524|0.079|0.145|0.545|
|SanFrancisco|3|317.34|772670.5|0.051|0.227|0.225|0.036|0.159|0.228|
|SanJose|3|312.08|668043.2|0.094|0.247|0.382|0.078|0.207|0.375|
|Seattle|6|233.53|1514628|0.120|0.209|0.575|0.113|0.197|0.576|
|StLouis|9|168.66|1257476|0.104|0.295|0.352|0.081|0.265|0.305|
|Tampa|5|197.86|1374229|0.130|0.247|0.526|0.109|0.183|0.597|
|Tucson|5|167.09|448819|0.145|0.333|0.435|0.132|0.309|0.426|
|Tulsa|6|170.69|423259.1|0.095|‐0.089|‐1.074|0.077|‐0.092|‐0.843|
|Ventura|3|250.01|281674.2|0.094|0.207|0.456|0.084|0.183|0.460|
|WashingtonDC|5|237.52|2291547|0.132|0.244|0.540|0.118|0.214|0.551|
|WestPalmBeach|4|207.76|660408.9|0.103|0.110|0.936|0.130|0.123|1.054|
|Wilmington|6|178.92|291394.8|0.091|0.305|0.299|0.092|0.301|0.306|



36 

### **Appendix 5: Prices Declines and Forecast Recoveries (VECM)** 

|||||2014/|2024/|2024/|2024/|
|---|---|---|---|---|---|---|---|
|MSA|2007:2|2012:2|2014:3|2012|2014|2007|2007nom|
|Albuquerque|207.26168|155.5972|155.51|1.00282|1.17461|0.88132|1.15453|
|Atlanta|211.20114|139.1576|158.87|1.15017|1.24217|0.93438|1.22404|
|Austin|215.84738|204.3886|241.43|1.16716|0.95936|1.07306|1.40571|
|Baltimore|292.67834|204.6678|209.44|1.03235|1.2426|0.8892|1.16486|
|BatonRouge|214.26001|192.6121|194.17|1.00597|1.0218|0.92599|1.21305|
|Birmingham|201.82755|163.4447|162.71|1.00839|1.3081|1.05457|1.38148|
|Boston|305.22666|233.4112|245.76|1.0719|1.35689|1.09253|1.43121|
|Buffalo|162.94281|153.9015|159.02|1.04262|1.07135|1.04555|1.36968|
|Charlotte|198.8382|157.8615|167.96|1.09072|1.15693|0.97727|1.28022|
|Chicago|237.7577|152.9193|159.52|1.06632|1.46635|0.98383|1.28881|
|Cincinnati|183.30053|146.9431|146.14|0.9998|1.40049|1.11657|1.46271|
|Cleveland|174.45993|127.8773|128.81|1.01116|1.60881|1.18784|1.55607|
|ColoradoSprings|216.03276|169.8758|178.92|1.0663|1.27017|1.05196|1.37807|
|ColumbiaSC|193.68215|162.0799|157.57|0.97641|1.23642|1.00589|1.31772|
|Columbus|181.82902|146.7363|154.86|1.06113|1.27374|1.08482|1.42111|
|Dallas|187.46013|166.805|186.45|1.12961|0.79853|0.79422|1.04043|
|Dayton|160.19678|126.0162|123.3|0.98389|1.30351|1.00328|1.3143|
|Denver|229.172|193.7391|226.04|1.19788|1.11791|1.10263|1.44445|
|Detroit|204.15647|117.8481|135.88|1.18962|1.85072|1.23178|1.61363|
|Edison|305.59743|213.6734|214.66|1.01401|1.40763|0.98875|1.29527|
|FortLauderdale|371.98884|177.5786|215.84|1.24562|1.10169|0.63923|0.8374|
|FortWorth|181.49301|160.8909|172.31|1.0737|0.84963|0.80665|1.05671|
|Greensboro|176.63821|146.2814|147.77|1.01347|1.18444|0.99086|1.29803|
|Hartford|229.9599|176.1311|170.26|0.96133|1.28726|0.95307|1.24852|
|Honolulu|221.58276|183.5031|201.1|1.10317|1.12841|1.02411|1.34158|
|Houston|204.96753|194.0182|217.94|1.13582|0.82843|0.88086|1.15393|
|Indianapolis|170.33508|143.2209|147.48|1.04674|1.1922|1.03224|1.35223|
|Jacksonville|309.38626|172.8536|189.78|1.11164|1.36211|0.83553|1.09455|
|KansasCity|207.08788|162.7934|166.01|1.02313|1.23159|0.98729|1.29335|
|LasVegas|294.41633|104.2519|144.32|1.43893|1.25533|0.61535|0.80611|
|LongIsland|342.55879|244.6915|244.33|1.00844|1.42642|1.01739|1.33278|
|LosAngeles|389.76273|226.4115|273.27|1.23181|1.18582|0.8314|1.08914|
|Louisville|193.3809|166.133|169.23|1.02558|1.28353|1.12323|1.47144|
|Memphis|180.99479|139.5918|142.41|1.01901|1.17291|0.92287|1.20896|
|Miami|395.77619|189.2621|230.36|1.24508|1.30364|0.75878|0.994|
|Minneapolis|269.53983|178.5505|197.35|1.13134|1.32446|0.96973|1.27035|
|Nashville|211.0621|177.1651|192.78|1.09128|1.11051|1.01432|1.32876|
|Newark|282.72542|203.3547|205.13|1.02527|1.35794|0.98525|1.29068|



37 

|NewOrleans|241.46542|197.2855|201|1.01366|1.04539|0.8702|1.13997|
|---|---|---|---|---|---|---|---|
|NewYork|312.29451|223.6922|226.95|1.04|1.56719|1.13891|1.49197|
|Norfolk|292.30757|212.8566|209.78|0.97826|1.25878|0.90339|1.18344|
|Oakland|358.78008|203.944|263.82|1.32521|1.16961|0.86004|1.12665|
|OklahomaCity|198.86137|181.1974|186.72|1.04065|0.82865|0.77805|1.01925|
|OrangeCounty|383.7261|234.4969|283.39|1.22629|1.15078|0.84988|1.11334|
|Orlando|325.43375|150.1276|176.6|1.19441|1.29677|0.70371|0.92185|
|Philadelphia|268.48545|217.4472|218.79|1.00391|1.23763|1.00855|1.3212|
|Phoenix|338.00524|160.4256|209.47|1.32587|1.17229|0.7265|0.95171|
|Pittsburgh|183.42798|172.1918|178.96|1.04388|1.09358|1.06694|1.3977|
|Portland|276.19056|188.6108|220.84|1.20164|1.21502|0.97152|1.27269|
|Providence|294.82186|198.2884|198.3|1.00988|1.40939|0.94797|1.24184|
|Raleigh|186.03497|157.5099|165.11|1.05301|1.12997|1.00287|1.31376|
|Richmond|250.95487|183.0585|189.82|1.05273|1.17642|0.88983|1.16568|
|Riverside|380.41232|170.0826|224.75|1.33974|1.18754|0.7016|0.9191|
|Sacramento|314.14837|157.0033|204.39|1.33371|1.22753|0.79865|1.04623|
|SaltLakeCity|242.21855|178.7367|204.86|1.17004|1.20994|1.02332|1.34056|
|SanAntonio|195.8025|179.8223|187.93|1.04|0.85022|0.81603|1.069|
|SanDiego|361.71149|218.3468|265.82|1.23583|1.18272|0.86918|1.13862|
|SanFrancisco|355.87183|251.2777|317.34|1.29905|1.22715|1.09428|1.43351|
|SanJose|359.82287|247.1729|312.08|1.29133|1.24709|1.08162|1.41693|
|Seattle|299.75777|201.2972|233.53|1.19049|1.20902|0.9419|1.23389|
|StLouis|216.20656|170.186|168.66|0.99776|1.29473|1.01|1.3231|
|Tampa|333.5328|170.9304|197.86|1.17709|1.24746|0.74002|0.96943|
|Tucson|276.72354|153.5396|167.09|1.11845|1.33301|0.80489|1.05441|
|Tulsa|188.20167|171.1062|170.69|0.99937|0.91128|0.82649|1.0827|
|Ventura|361.28279|206.2084|250.01|1.23097|1.2068|0.83511|1.094|
|WashingtonDC|323.60306|220.5697|237.52|1.08804|1.24372|0.91287|1.19586|
|WestPalmBeach|355.97611|168.1285|207.76|1.27335|1.11031|0.64802|0.8489|
|Wilmington|247.84966|178.6333|178.92|1.01144|1.30548|0.94241|1.23456|



38 


