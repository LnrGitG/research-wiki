---
source_url: /tmp/saiz-2010.pdf
ingested: 2026-07-16
sha256: 8f0483ca43a15208
---

# THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY<sup>∗</sup> 

# ALBERT SAIZ 

I process satellite-generated data on terrain elevation and presence of water bodies to precisely estimate the amount of developable land in U.S. metropolitan areas. The data show that residential development is effectively curtailed by the presence of steep-sloped terrain. I also find that most areas in which housing supply is regarded as inelastic are severely land-constrained by their geography. Econometrically, supply elasticities can be well characterized as functions of both physical and regulatory constraints, which in turn are endogenous to prices and demographic growth. Geography is a key factor in the contemporaneous urban development of the United States. 

# I. INTRODUCTION 

The determinants of local housing supply elasticities are of critical importance in explaining current trends in the shape of urban development and the evolution of housing values.<sup>1</sup> The existing literature on this topic has focused on the role that local land use regulations play in accounting for differences in the availability of land. The large variance in housing values across locales can indeed be partially explained by man-made regulatory constraints. However, zoning and other land-use policies are multidimensional, difficult to measure, and endogenous to preexisting land values. In this context, it is uncontroversial to argue that predetermined geographic features such as oceans, lakes, mountains, and wetlands can also induce a relative scarcity of developable land. Hence their study merits serious consideration: to what extent, if at all, does geography determine contemporaneous patterns of urban growth?<sup>2</sup> 

This paper gives empirical content to the concepts of land scarcity and abundance in urban America. Using geographic information system (GIS) techniques, I precisely estimate the area that is forgone to the sea within 50-kilometer radii from metropolitan 

> ∗Enestor Dos Santos and Blake Willmarth provided superb research assistance. The editor, three referees, Matt White, Joe Gyourko, Jeff Zabel, and participants at the 2008 ASSA, EEA, and NBER meetings provided helpful input. All errors are my sole responsibility. I gratefully acknowledge financial help from the Zell–Lurie Center Research Sponsors Fund. 

> 1. Glaeser, Gyourko, and Saks (2006); Saks (2008). 

> 2. An important step in this direction has been taken by Burchfield et al. (2006), who relate terrain ruggednes and access to underground water to the density and compactness of _new_ real estate development. 

> ⃝C 2010 by the President and Fellows of Harvard College and the Massachusetts Institute of Technology. 

> _The Quarterly Journal of Economics_ , August 2010 

1253 

1254 

_QUARTERLY JOURNAL OF ECONOMICS_ 

central cities. I then use satellite-based geographic data on land use provided by the United States Geographic Service (USGS) to calculate the area lost to internal water bodies and wetlands. Using the USGS Digital Elevation Model (DEM) at 90–square meter cell grids, I also create slope maps, which allow me to calculate how much of the land around each city exhibits slopes above 15%. Combining all the information above, the paper provides a precise measure of exogenously undevelopable land in cities. I then turn to studying the links between geography and urban development. 

To do so, I first develop a conceptual framework that relates land availability to urban growth and housing prices. Using a variation of the Alonso–Muth–Mills model (Alonso 1964; Mills 1967; Muth 1969), I show that land-constrained cities not only should be more expensive _ceteris paribus,_ but also should _display lower housing supply elasticities_ with respect to citywide demand shocks, a somewhat _ad hoc_ claim in the existing literature. I also show that, in equilibrium, consumers in geographically constrained metropolitan areas should require higher wages or higher amenities to compensate them for more expensive housing. 

Empirically, all of these facts are corroborated by the data. I find that most areas that are widely regarded as supply-inelastic are, in fact, severely land-constrained by their geography. Rose (1989b) showed a positive correlation between coastal constraints and housing prices for a limited sample of forty-five cities. Here I show that restrictive geography, including the presence of mountainous areas and internal water, was a very strong predictor of housing price levels and _growth_ for all metropolitan statistical areas (MSA) during the period 1970–2000, even after controlling for regional effects. This association was not solely driven by coastal areas, as it is present even _within_ coastal markets. I next deploy the Wharton Residential Urban Land Regulation Index recently created by Gyourko, Saiz, and Summers (2008). The index is constructed to capture the stringency of residential growth controls. Using alternate citywide demand shocks, I estimate metropolitanspecific housing supply functions and find that housing supply elasticities can be well characterized as functions of both physical and regulatory constraints. 

These associations, however, do not take into account feedback effects between prices and regulations. Homeowners have stronger incentives to protect their housing investments where land values are high initially. The homevoter hypothesis (Fischel 

# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1255 

2001) implies a reverse causal relationship from initially high land values to increased regulations. Empirically, I find that antigrowth local land policies are more likely to arise in growing, land-constrained metropolitan areas and in cities where preexisting land values were high and worth protecting. Hence, I next endogeneize the regulatory component of housing supply elasticity. I posit and estimate an empirical model of metropolitan housing markets with endogenous regulations. As exogenous land-use regulatory shifters, I use measures shown to be associated with local tastes for regulation. Both geography and regulation are important to account for housing supply elasticities, with the latter showing themselves to be endogenous to prices and past growth. 

Finally, I use the results to provide operational estimates of local supply elasticities in all major U.S. metropolitan areas. These estimates, based on land-availability fundamentals, should prove useful in calibrating general equilibrium models of interregional labor mobility and in predicting the response of housing markets to future demand shocks. Housing supply is estimated to be quite elastic for the average metropolitan area (with a populationweighted elasticity of 1.75). In land-constrained large cities, such as cities in coastal California, Miami, New York, Boston, and Chicago, estimated elasticities are below one. These elasticity estimates display a very strong correlation of .65 with housing prices in 2000. Quantitatively, a movement across the interquartile range in geographic land availability in an average-regulated metropolitan area of 1 million is associated with shifting from a housing supply elasticity of approximately 2.45 to one of 1.25. Moving to the ninetieth percentile of land constraints (as in San Diego, where 60% of the area within its 50-km radius is not developable) pushes average housing supply elasticities down further to 0.91. The results in the paper ultimately demonstrate that geography is a key factor in the contemporaneous urban development of the United States. 

# II. GEOGRAPHY AND LAND IN THE UNITED STATES: A NEW DATA SET 

The economic importance of geography for local economic development is an underexplored topic. Previous research has examined the correlation between housing price levels and proxies for the arc of circle lost to the sea in a limited number of cities (Rose 1989a, 1989b; Malpezzi 1996; Malpezzi, Chun, and Green 1998) but the measures proved somewhat limited. Recent papers 

1256 

_QUARTERLY JOURNAL OF ECONOMICS_ 

in urban economics, such as Burchfield et al. (2006), Rosenthal and Strange (2008), and Combes et al. (2009), underline the relevance of geographic conditions as economic fundamentals explaining local population density. 

Here, I develop a comprehensive measure of the area that is unavailable for residential or commercial real estate development in MSAs. Architectural development guidelines typically deem areas with slopes above 15% severely constrained for residential construction. Using data on elevation from the USGS Digital Elevation Model (DEM) at its 90-m resolution, I generated slope maps for the continental United States. GIS software was then used to calculate the exact share of the area corresponding to land with slope above 15% within a 50-km radius of each metropolitan central city. 

Residential development is effectively constrained by the presence of steep slopes. To demonstrate this, I focus on Los Angeles (LA). Median housing values there are among the highest in the United States and the incentives to build on undeveloped land are very strong. Using GIS software to delineate the intersection between steep-slope zones and the 6,456 census block groups (as delimited in 2000) that lie within a 50-km radius of LA’s city centroid, I calculated the share of the area in each block group with slope above 15%. Then I defined steep-slope block groups as those with a share of steep-sloped terrain of more than 50%. Steep-slope block groups encompassed 47.62% of the land area within 50 km of LA’s geographic center in year 2000. However, only 3.65% of the population within this 50-km radius lived in them. These magnitudes clearly illustrate the deterrent effect of steep slopes on housing development. 

The next step to calculate land availability involved estimating the area within the cities’ 50-km radii that corresponds to wetlands, lakes, rivers, and other internal water bodies. The 1992 USGS National Land Cover Dataset is a satellite-based GIS source containing information about land cover characteristics at 30 by 30–m cell resolutions. The data were processed by the Wharton GIS lab to produce information on the area apportioned to each of the land cover uses delimited by the USGS by census tract. Next, the distance from each central city centroid to the centroid of all census tracts was calculated, and Census tracts within 50 km were used to compute water cover shares. 

Last, I used digital contour maps to calculate the areas within the 50-km radii that are lost to oceans and the Great Lakes. The 

# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1257 

final measure combines the area corresponding to steep slopes, oceans, lakes, wetlands, and other water features. This is the first comprehensive measure of truly undevelopable area in the literature. The use of a radius from the city centroid makes it a measure of original constraints, as opposed to one based on _ex post_ ease of development (e.g., density). 

Table I displays the percentages of undevelopable area for all MSAs with population over 500,000 in the 2000 Census for which I also have regulation data (those included in the later regressions). Of these large metro areas, Ventura (CA) is the most constrained, with 80% of the area within a 50-km radius rendered undevelopable by the Pacific Ocean and mountains. Miami, Fort Lauderdale, New Orleans, San Francisco, Sarasota, Salt Lake City, West Palm Beach, San Diego, and San Jose complete the list of the top 10 most physically constrained major metropolitan areas in the United States. Many large cities in the South and Midwest (such as Atlanta, San Antonio, and Columbus) are largely unconstrained. 

Table II studies the correlates of the newly constructed land unavailability variable. To do so, I run a number of independent regressions. The variables in Table II’s rows appear on the left-hand side in each sequential regression, and the geographicunavailability variable is always the main right-hand side control. Regional fixed effects (Northeast, South, Midwest, West) are included in all regressions. Each column shows the coefficient of the variable of reference on the unavailable land share, and its associated standard error appears in parentheses. A second set of regressions (2) also controls for a coastal status dummy, which identifies metropolitan areas that are within 100 km of the ocean or Great Lakes. The significant coefficients reveal that geographically land-constrained areas tended to be more expensive in 2000, to have experienced faster price growth since 1970, to have higher incomes, to be more creative (higher patents per capita), and to have higher leisure amenities (as measured by the number of tourist visits).<sup>3</sup> Observed metropolitan population levels were largely orthogonal to natural land constraints. 

Interestingly, note that none of the major demand-side drivers of recent urban demographic change (immigration, education, 

> 3. Carlino and Saiz (2008) demonstrate that the number of tourist visits is strongly correlated with other measures of quality of life and a strong predictor of recent city growth. 

1258 _QUARTERLY JOURNAL OF ECONOMICS_ 

|ndevelopable<br>area (%)<br>WRI|37_._54<br>0_._27<br>36_._69<br>1_._34<br>36_._13<br>0_._32<br>33_._90<br>1_._70<br>33_._80<br>0_._29<br>33_._52<br>−0_._81<br>32_._07<br>−0_._69<br>31_._53<br>−0_._69<br>30_._50<br>0_._68<br>30_._46<br>−0_._06<br>30_._02<br>0_._10<br>29_._32<br>−1_._00<br>28_._78<br>0_._01<br>27_._08<br>0_._72<br>24_._52<br>0_._05<br>24_._21<br>0_._40<br>24_._02<br>0_._54<br>23_._33<br>−0_._09<br>23_._29<br>0_._49<br>23_._07<br>1_._52<br>22_._27<br>0_._87<br>21_._87<br>1_._60<br>20_._86<br>0_._02<br>19_._23<br>0_._38<br>19_._05<br>−0_._23|
|---|---|
|(METROAREAS WITHPOPULATION_>_500,000)<br>U<br><br>MSA/NECMA name|Portland–Vancouver, OR–WA<br>Tacoma, WA<br>Orlando, FL<br>Boston–Worcester–Lawrence, MA–NH<br>Jersey City, NJ<br>Baton Rouge, LA<br>Las Vegas, NV–AZ<br>Gary, IN<br>Newark, NJ<br>Rochester, NY<br>Pittsburgh, PA<br>Mobile, AL<br>Scranton–Wilkes-Barre–Hazleton, PA<br>Springfeld, MA<br>Detroit, MI<br>Bakersfeld, CA<br>Harrisburg–Lebanon–Carlisle, PA<br>Albany–Schenectady–Troy, NY<br>Hartford, CT<br>Tucson, AZ<br>Colorado Springs, CO<br>Baltimore, MD<br>Allentown–Bethlehem–Easton, PA<br>Minneapolis–St. Paul, MN–WI<br>Buffalo–Niagara Falls, NY|
|INTS <br> Rank|26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50|
|TCONSTRA<br>le<br>WRI|1_._21<br>0_._94<br>0_._72<br>−1_._24<br>0_._72<br>−0_._03<br>0_._92<br>0_._31<br>0_._21<br>0_._46<br>0_._62<br>−0_._81<br>0_._12<br>0_._49<br>0_._96<br>−0_._02<br>0_._19<br>0_._92<br>0_._46<br>−0_._22<br>−0_._16<br>0_._65<br>0_._02<br>−0_._37<br>0_._53|
|DEVELOPMEN<br>Undevelopab<br>area (%)|79_._64<br>76_._63<br>75_._71<br>74_._89<br>73_._14<br>71_._99<br>66_._63<br>64_._01<br>63_._80<br>63_._41<br>61_._67<br>60_._45<br>59_._77<br>52_._47<br>49_._16<br>47_._33<br>45_._01<br>43_._63<br>41_._78<br>41_._64<br>40_._50<br>40_._42<br>40_._01<br>38_._53<br>37_._90|
|PHYSICAL ANDREGULATORY<br>k<br>MSA/NECMA name|Ventura, CA<br>Miami, FL<br>Fort Lauderdale, FL<br>New Orleans, LA<br>San Francisco, CA<br>Salt Lake City–Ogden, UT<br>Sarasota–Bradenton, FL<br>West Palm Beach–Boca Raton, FL<br>San Jose, CA<br>San Diego, CA<br>Oakland, CA<br>Charleston–North Charleston, SC<br>Norfolk–Virginia Beach–Newport<br>News, VA–NC<br>Los Angeles–Long Beach, CA<br>Vallejo–Fairfeld–Napa, CA<br>Jacksonville, FL<br>New Haven–Bridgeport–Stamford, CT<br>Seattle–Bellevue–Everett, WA<br>Milwaukee–Waukesha, WI<br>Tampa–St. Petersburg–Clearwater, FL<br>Cleveland–Lorain–Elyria, OH<br>New York, NY<br>Chicago, IL<br>Knoxville, TN<br>Riverside–San Bernardino, CA|
|Ran|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25|



_THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1259 

|ble<br>WRI|−0_._23<br>−0_._38<br>−0_._40<br>0_._64<br>0_._07<br>−0_._78<br>−0_._79<br>0_._73<br>−0_._27<br>−0_._53<br>0_._03<br>−0_._28<br>−0_._56<br>−0_._21<br>−0_._29<br>−1_._22<br>0_._26<br>−0_._37<br>−1_._19<br>−0_._74<br>−0_._50<br>−0_._45|
|---|---|
|Undevelopa<br>area (%)|9_._16<br>8_._81<br>8_._40<br>8_._11<br>6_._45<br>6_._29<br>5_._82<br>5_._13<br>4_._91<br>4_._69<br>4_._08<br>3_._76<br>3_._34<br>3_._17<br>3_._12<br>2_._56<br>2_._50<br>2_._46<br>1_._66<br>1_._44<br>1_._04<br>0_._93|
|MSA/NECMA name|Dallas, TX<br>Richmond–Petersburg, VA<br>Houston, TX<br>Raleigh–Durham–Chapel Hill, NC<br>Akron, OH<br>Tulsa, OK<br>Kansas City, MO–KS<br>El Paso, TX<br>Fort Worth–Arlington, TX<br>Charlotte–Gastonia–Rock Hill,<br>NC–SC<br>Atlanta, GA<br>Austin–San Marcos, TX<br>Omaha, NE–IA<br>San Antonio, TX<br>Greensboro–Winston–Salem–<br>High Point, NC<br>Fort Wayne, IN<br>Columbus, OH<br>Oklahoma City, OK<br>Wichita, KS<br>Indianapolis, IN<br>Dayton–Springfeld, OH<br>McAllen–Edinburg–Mission, TX|
|Rank|74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95|
|ble<br> <br>WRI|−0_._57<br>−0_._59<br>0_._84<br>−0_._76<br>0_._47<br>−0_._23<br>0_._61<br>0_._31<br>1_._89<br>−0_._85<br>0_._91<br>−0_._94<br>−0_._41<br>−0_._47<br>1_._18<br>0_._59<br>0_._37<br>−0_._73<br>−0_._38<br>−0_._58<br>1_._13<br>0_._31<br>−0_._15|
|Undevelopa<br>area (%)|18_._96<br>17_._85<br>16_._72<br>15_._23<br>14_._67<br>14_._35<br>13_._95<br>13_._95<br>13_._87<br>13_._71<br>12_._88<br>12_._87<br>12_._83<br>12_._69<br>12_._18<br>12_._05<br>11_._63<br>11_._08<br>10_._52<br>10_._30<br>10_._16<br>9_._71<br>9_._28|
|MSA/NECMA name|Toledo, OH<br>Syracuse, NY<br>Denver, CO<br>Columbia, SC<br>Wilmington–Newark, DE–MD<br>Birmingham, AL<br>Phoenix–Mesa, AZ<br>Washington, DC–MD–VA–WV<br>Providence–Warwick–Pawtucket, RI<br>Little Rock–North Little Rock, AR<br>Fresno, CA<br>Greenville–Spartanburg–<br>Anderson, SC<br>Nashville, TN<br>Louisville, KY–IN<br>Memphis, TN–AR–MS<br>Stockton–Lodi, CA<br>Albuquerque, NM<br>St. Louis, MO–IL<br>Youngstown–Warren, OH<br>Cincinnati, OH–KY–IN<br>Philadelphia, PA–NJ<br>Ann Arbor, MI<br>Grand Rapids–Muskegon–Holland, MI|
|Rank|51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73|



1260 

_QUARTERLY JOURNAL OF ECONOMICS_ 

## TABLE II 

PARTIAL CORRELATES OF UNAVAILABLE LAND SHARE (50-KM RADIUS) 

||Share of area una|vailable for development|
|---|---|---|
||OLS-regional FE<br>_β_|Adds coastal dummy<br>_β_|
||(1)|(2)|
|Log population in 2000|0_._443<br>(0_._336)|−0_._01<br>(0_._364)|
|Log median house value in 2000|0_._592<br>(0_._081)<sup>∗∗∗</sup>|0_._41<br>(0_._085)<sup>∗∗∗</sup>|
|_�_Log median house value|0_._240|0_._122|
|(1970–2000)|(0_._054)<sup>∗∗∗</sup>|(0_._057)<sup>∗∗</sup>|
|Log income in 2000|0_._233<br>(0_._056)<sup>∗∗∗</sup>|0_._164<br>(0_._060)<sup>∗∗∗</sup>|
|_�_Log income (1990–2000)|−0_._002<br>(0_._020)|0_._006<br>(0_._022)|
|_�_Log population (1990–2000)|−0_._027<br>(0_._027)|−0_._043<br>(0_._029)|
|Immigrants (1990–2000)/population<br>(1990)|0_._009<br>(0_._011)|−0_._007<br>(0_._012)|
|Share with bachelor’s degree (2000)|0_._006<br>(0_._020)|−0_._004<br>(0_._022)|
|Share workers in manufacturing<br>(2000)|−0_._01<br>(0_._021)|0_._005<br>(0_._023)|
|Log(patents/population) (2000)|0_._762<br>(0_._260)<sup>∗∗∗</sup>|0_._771<br>(0_._287)<sup>∗∗∗</sup>|
|January monthly hours of sun<br>(average 1941–1970)|−3_._812<br>(11_._252)|−12_._047<br>(12_._318)|
|Log tourist visits per person (2000)|0_._493<br>(0_._261)<sup>∗</sup>|0_._719<br>(0_._286)<sup>∗∗</sup>|



_Notes_ . Standard errors in parentheses. Rows present the coefficients ( _β_ ) and standard errors of separate regressions, where the variable described in the row is the dependent variable on the left-hand side and the unavailable land share (geographic constraint) is the explanatory variable on the right-hand side. The regressions in column (1) include regional fixed effects as controls, whereas those in column (2) also include a coastal dummy for metropolitan areas within 100 km of the oceans or Great Lakes (as defined in Rappaport and Sachs [2003]).<sup>∗</sup> significant at 10%;<sup>∗∗</sup> significant at 5%;<sup>∗∗∗</sup> significant at 1%. 

manufacturing orientation, and hours of sun) was actually correlated with geographic land constraints. 

All results hold after controlling for the coastal dummy, indicating that the new land-availability variable contains information above and beyond that used in studies that focus on coastal status (Rose 1989a, 1989b; Malpezzi 1996). Taking into account the standard deviations of the different components of land unavailability, mountains contribute 42% of the variation in this variable, whereas coastal and internal water loss account for 

# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1261 

31% and 26% of the variance in land constraints, respectively. After controlling for region fixed effects, as I do throughout the paper, there is no correlation in the data between coastal area loss and the extent of land constraints begotten by mountainous terrain. The loss of developable land due to the presence of large bodies of internal water (70% of which is attributable to wetlands, as in the Everglades) tends to be positively associated with coastal area loss and, not surprisingly, negatively associated with mountainous terrain. 

The other major data set used in the paper is obtained from the 2005 Wharton Regulation Survey. Gyourko, Saiz, and Summers (2008) use the survey to produce a number of indexes that capture the intensity of local growth control policies in a number of dimensions. Lower values in the Wharton Regulation Index, which is standardized across all municipalities in the original sample, can be thought of as signifying the adoption of more laissez-faire policies toward real estate development. Metropolitan areas with high values of the Wharton Regulation Index (WRI henceforth), conversely have zoning regulations or project approval practices that constrain new residential real estate development. I process the original municipal-based data to create average regulation indexes by metropolitan area using the probability sample weights developed by Gyourko, Saiz, and Summers (2008).<sup>4</sup> 

Table I displays the average WRI values for all metropolitan areas with populations greater than 500,000 and for which data are available. A clear pattern arises when the regulation index is contrasted with the land-availability measure. Physical land scarcity is associated with stricter regulatory constraints to development. Of the twenty most land-constrained areas, fourteen have positive values of the regulation index (which has a mean of − 0.10 and a s.e. of 0.81 across metro areas). Conversely, sixteen of the twenty least land-constrained metropolitan areas have negative regulation index values. 

Other data sources are used throughout the paper: the reader is referred to Appendices I–III for descriptive statistics and the meaning and provenance of the remaining variables. 

> 4. Note that, because of different sample sizes across cities, in regressions where the WRI is used on the left-hand side (Table IV), heteroscedasticity could be an issue, and therefore Feasible Generalized Least Squares (FGLS) are used. In fact, however, the results in Table IV are very robust to all reasonable weighting schemes and the omission of metro areas with smaller number of observations in the WRI. 

1262 

_QUARTERLY JOURNAL OF ECONOMICS_ 

# III. GEOGRAPHY AND LOCAL DEVELOPMENT: A FRAMEWORK 

Why should physical or man-made land availability constraints have an impact on housing supply _elasticities_ ? How does geography shape urban development? To characterize the supply of housing in a city, I assume developers to be price takers in the land market. Consumers within the city compete for locations determining the price of the land input. Taking land values and construction outlays as given, developers supply housing at cost. All necesary model derivations and the proofs of propositions are in the mathematical appendix, Appendix I. 

The preferences of homogeneous consumers in city _k_ are captured by the utility function _U_ ( _Ck_ ) = ( _Ck_ )<sup>_ρ_</sup> . Consumption in the city ( _Ck_ ) is the sum of the consumption of city amenities ( _Ak_ ) and private goods. Private consumption is equal to wages in the city minus rents, minus the (monetized) costs of commuting to the central business district (CBD), where all jobs are located. Each individual is also a worker and lives in a separate house, so that the number of housing units equals population ( _Hk_ = POP _k_ ). Utility can be expressed as _U_ ( _Ck_ ) = ( _Ak_ + _wk_ − _γ_ · _r_<sup>′</sup> − _t_ · _d_ )<sup>_ρ_</sup> , where _wk_ stands for the wage in the city, _γ_ for the units of land/housingspace consumption (assumed constant), _r_<sup>′</sup> for the rent _per unit of housing-space consumption_ , _t_ for the monetary cost per distance commuted, and _d_ for the distance of the consumer’s residence to the CBD. As in conventional Alonso–Muth–Mills models (Brueckner 1987), a nonarbitrage condition defines the rent gradient: all city inhabitants attain utility _Uk_ via competition in the land markets. Therefore the total rent paid by an individual ( _r_ = _γ_ · _r_<sup>′</sup> ) takes the functional form _r_ ( _d_ ) = _r_ 0 − _td_ . 

Consider a circular city with radius _�k_ . Geographic or regulatory land constraints make construction unfeasible in some areas: only a sector (share) _�k_ of the circle is developable.<sup>5</sup> The city radius is thus a function of the number of households and land availability: _�k_ = � _γ Hk/�kπ_ . 

Developers are price takers and buy land at market prices. They build and sell homes at price _P_ ( _d_ ). The construction sector is competitive and houses are sold at the cost of land, LC( _d_ ), plus construction costs, CC, which include the profits of the builder: _P_ ( _d_ ) = CC + LC( _d_ ). In the asset market steady state equilibrium 

> 5. This feature appears in conventional urban economic models that focus on a representative city (Capozza and Helsley 1990). Here, I add heterogeneity in the land availability parameter across cities and derive explicit housing supplies elasticities from it. 

_THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1263 

there is no uncertainty and prices equal the discounted value of rents: _P_ ( _d_ ) = _r_ ( _d_ ) _/i_ , which implies that _r_ ( _d_ ) = _i_ · CC + _i_ · LC( _d_ ). At the city’s edge there is no alternative use for land so, without loss of generality, LC( _�k_ ) = 0. Therefore _r_ ( _�k_ ) = _i_ · CC, which implies that _r_ 0 = _i_ · CC + _t_ · � _γ Hk/�kπ_ . 

In this setup, average housing rent in the city,� _rk_ , can be shown to be equivalent to the rent paid by the household living two-thirds of the distance from the CBD to the city’s edge: � _rk_ = _r_ ( 3<sup><u>2</u></sup><sup>_�k_)(see</sup> Derivation 1 in Appendix II). The final housing supply equation in the city has average housing values ( _P_<sup>�</sup> _k_<sup>_S_) expressed as a function</sup> of the number of households: 



I next define the aggregate demand function for housing in the city. In a system of open cities, consumers can move and thus equalize utility across locations, which I normalize to zero (i.e., the spatial indifference condition is _Uk_ = 0 ∀ _k_ ). Furthermore, in all cities, _wk_ and _Ak_ are functions of population. I model the level of amenities as _Ak_ =<sup>�</sup> _Ak_ − _α_<sup>~~√~~</sup> POP _k_ . The parameter _α_ mediates the marginal congestion cost (in terms of rivalry for amenities, traffic, pollution, noise, social capital dilution, crime, etc.). _α_ could also be interpreted in the context of an alternative but isomorphic model with taste heterogeneity: people with greater preferences for the city are willing to pay more and move in first, but later marginal migrants display less of a willingness to pay for the city (e.g., � Saiz [2007]). Labor demand is modeled as _wk_ = _wk_ − _ψ_<sup>√</sup> POP _k_ and is assumed to be downward sloping; marginal congestion costs weakly increase with population ( _ψ, α_ ≥ 0).<sup>6</sup> Recalling that _Hk_ = POP _k_ , substituting into the intercity spatial equilibrium equation, and focusing w.o.l.o.g. on the spatial indifference condition of consumers living in the CBD, I obtain the demand schedule for housing in the city: 



6. Of course, cities may display agglomeration economies up to some congestion point (given predetermined conditions, these may be captured by<sup>�</sup> _Ak_ + � _wk_ ). It is necessary only that, in equilibrium, the _marginal_ effect of population on wages and amenities be (weakly) negative. This is a natural assumption that avoids a counterfactual equilibrium where all activity is concentrated in one single city with _�k_ = 1. 

1264 

_QUARTERLY JOURNAL OF ECONOMICS_ 

Note that relative shocks to labor productivity or to amenities (<sup>�</sup> _Ak_ + � _wk_ ) shift the city’s demand curve upward, _which I will use to identify supply elasticities later_ . 

I can now combine the expression for home values in the CBD via the supply equation and the city-demand equation (2) to obtain the equilibrium number of households in each city, 



Note that amenities and wages have to at least cover the annuitized physical costs of construction for a potential site to be inhabitable. 

Within this setup, I first study the supply response to growth in the demand for housing that is induced by productivity and amenity shocks. Its is clear that _∂_<sup>�</sup> _PkS_<sup>_/∂�k <_0.</sup><sup>_Other things equal_,</sup> more land availability shifts down the supply schedule. Do land constraints also have an effect with respect to supply _elasticities_ ? Defining the city-specific supply inverse elasticity of average housing prices as _βk_<sup>_S_≡</sup><sup>_∂_ln</sup> _P_<sup>�</sup> _k_<sup>_S/∂_ln</sup><sup>_Hk_one can demonstrate</sup> 

- PROPOSITION 1. The inverse elasticity of supply (that is, the price sensitivity to demand shocks) is decreasing in land availability. Conversely, as land constraints increase, positive demand shocks imply stronger positive impacts on the the growth of housing values. 

Proposition 1 tells us that land-constrained cities have more inelastic housing supply and helps us understand how housing prices react to exogenous demand shocks. In addition, two interesting further questions arise from the general equilibrium in the housing and labor markets: Why is there any population in areas with difficult housing supply conditions? Should these areas be more expensive _ex post_ in equilibrium? Assume that the covariance between productivity, amenities, and land availability is zero across all locales. Productivity–amenity shocks are _ex ante_ independent of physical land availability, which is consistent with random productivity shocks and Gibrat’s Law explanation for parallel urban growth (Gabaix 1999). Assume further that the relevant upper tail of such shocks is drawn from a Pareto distribution. I can now state 

- PROPOSITION 2. Metropolitan areas with low land availability tend to be more productive or to have higher amenities; in 

# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1265 

the observable distribution of metro areas the covariance between land availability and productivity–amenity shocks is negative. 

The intuition for Proposition 2 is based on the nature of the urban development process. As discussed by Eeckhout (2004), existing metropolitan areas are a truncated distribution of the upper tail of inhabited settlements. In order to compensate for the higher housing prices that are induced by locations with more difficult supply conditions, consumers need to be rewarded with higher wages or urban amenities. Although costly land development reduced _ex ante_ the desirability of marshlands, wetlands, and mountainous areas for human habitation, those land-constrained cities _that thrived ex post_ must be more productive or attractive than comparable locales. Observationally, this implies a positive association between attractiveness and land constraints, conditional on metropolitan status. Conversely, land-unconstrained metropolitan areas must be, on average, observationally less productive and/or amenable. 

Note that because the spatial indifference condition has to hold, this implies that expected home values are also decreasing in land availability: metropolitan areas with lower land availability tend to be more expensive in equilibrium. These conclusions are reinforced if the _ex ante_ covariance between productivity/ amenities and land availability is negative, albeit this is not a necessary condition.<sup>7</sup> 

Although, due to a selection effect, land-constrained metropolitan areas have higher amenities, productivity, and prices, they are not necessarily larger. In fact, if productivity–amenity shocks are approximately Pareto-distributed in the upper tail (consistent with the empirical evidence on the distribution of city sizes in most countries), one can posit 

PROPOSITION 3. Population levels in the existing distribution of metropolitan areas should be independent of the degree of land availability. 

Proposition 3 tells us that population levels in metropolitan areas are expected to be orthogonal to initial land availability. In equilibrium, higher productivity and/or amenities are required 

> 7. Glaeser (2005a, 2005b) and Gyourko (2005) emphasize the importance of access to harbors (a factor that limits land availability) for the earlier development of some of the larger oldest cities in the United States: Boston, New York, and Philadelphia. 

1266 

## _QUARTERLY JOURNAL OF ECONOMICS_ 

in more land-constrained cities, which further left-censors their observed distribution of city productivities. With a Pareto distribution of productivity shocks, this effect exactly compensates for the extra costs imposed by a difficult geography. 

In sum, the model tells us that one should expect those geographically constrained metropolitan areas _that we observe in the data_ to be more productive or to have higher amenities (Proposition 2) and the correlation between land availability and population size to be zero (Proposition 3), precisely the data patterns found in the preceding section. In addition, due to Proposition 1, one should expect metropolitan areas with lower land availability not only to be more expensive in equilibrium, but also to display _lower housing supply elasticities_ , as I will demonstrate in the next sections. 

# IV. GEOGRAPHY AND HOUSING PRICE ELASTICITIES 

I now move to assessing how important geographic constraints are in explaining local housing price elasticities. Recall from the model that, on the supply side, average housing prices in a city are the sum of construction costs plus land values _P_ � _k_ = CC(themselves + LC( _Hk_ ). Totallya functiondifferentiatingof the numberthe logof housingof this expres-units): sion, and manipulating, I obtain 



For now, I assume changes in local construction costs to be exogenous to local changes in housing demand: the prices of capital and materials (timber, cement, aluminum, and so on) are determined at the national or international level, and construction is an extremely competitive industry with an elastic labor supply. The assumption is consistent with previous research (Gyourko and Saiz, 2006), but I relax it later. Defining _σk_ = CC _/P_<sup>�</sup> _k_ as the initial share of construction costs on housing prices, and assuming that _dP_<sup>�</sup> _k/dHk_ = _d_ LC( _Hk_ ) _/dHk_ , one obtains _d_ ln _P_<sup>�</sup> _k_ = _σk_ · _d_ CC _/_ CC + _βk_<sup>_S_·</sup><sup>_dHk/Hk_.Asdefinedearlierinthemodel,</sup><sup>_β_</sup> _k_<sup>_S_</sup> is the inverse elasticity of housing supply with respect to average home values. I can reexpress this as the empirical log-linearized supply equation: _d_ ln _P_<sup>�</sup> _k_ = _σk_ · _d_ ln CC + _βk_<sup>_S_·</sup><sup>_d_ln</sup><sup>_Hk_.Notethatby</sup> considering changes in values and quantities, initial scale differences across cities are differenced out (Mayer and Somerville 

# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1267 

2000). Throughout the rest of the paper I use long differences (between 1970 and 2000) and hence focus on long-run housing dynamics, as opposed to high-frequency volatility.<sup>8</sup> However, I will also later briefly discuss results at higher (decadal) frequencies. The empirical specification also includes region fixed effects ( _Rk_<sup>_j_,</sup> for _j_ = 1 _,_ 2 _,_ 3) and an error term ( _εk_ ), and estimates the supply equation in discrete changes: 



_P_ � _k_ is measured by median housing prices in each decennial Census.<sup>9</sup> The city-specific parameter _σk_ (construction cost share in 1970) is calculated using the estimates in Davis and Heathcote (2007) and Davis and Palumbo (2008) and data on housing prices. Combined with existing detailed information about the growth of construction costs in each city from published sources, the cityspecific intercept _σk_ · _�_ ln CC is thus known and calibrated into the model. Changes in the housing stock are, of course, endogenous to changes in prices via the demand side. Therefore, I instrument for _�_ ln _Hk_ using a shift-share of the 1974 metropolitan industrial composition, the log of average hours of sun in January, and the number of new immigrants (1970 to 2000) divided by the population in 1970. The first variable, as introduced by Bartik (1991) and recently used by Glaeser, Gyourko, and Saks (2006) and Saks (2008), is constructed using early employment levels at the twodigit SIC level and using national growth rates in each industry to forecast city growth due to composition effects. Hours of sun capture a well-documented secular trend of increasing demand for high-amenity areas (Glaeser, Kolko, and Saiz 2001; Rappaport 2007). Finally, previous research (Saiz 2003, 2007; Ottaviano and Peri 2007) has shown international migration to be one of the strongest determinants of the growth in housing demand and prices in a number of major American cities. Immigration inflows 

> 8. Short-run housing adjustments involve considerable dynamic aspects, such as lagged construction responses and serial correlation of high-frequency price changes (Glaeser and Gyourko 2006). 

> 9. A long literature, summarized by Kiel and Zabel (1999), demonstrates that the evolution of self-reported housing prices generally mimics that of actual prices (for a recent confirmation of this fact, see Pence and Bucks [2006]). The correlation between the change in log median census values and the change in the log of the Freddie Mac repeat sales index between 1980 and 2000 is 0.9 across the 147 cities for which the measures were available. The repeat sales index, obtained from Freddie Mac, is unavailable in 1970, and its coverage in our application is limited to the 147 aforementioned cities. Therefore, in this context, I prefer to use the higher coverage of the Census measure. 

1268 

_QUARTERLY JOURNAL OF ECONOMICS_ 

_have been shown to be largely unrelated to other citywide economic shocks,_ and very strongly associated with the predetermined settlement patterns of immigrant communities (Altonji and Card 1989). 

The instruments for demand shocks prove to be strong, with an _F_ -test 47.75 compared to the critical 5% value in Stock and Yogo (2005) of 13.91. The instruments also pass conventional exogeneity tests (with a _p_ -value of .6 in the Sargan–Hansen _J_ test). Note that the specification explicitly controls for all factors that drive physical construction costs. Equation (3) is estimated using 2SLS, with the assumptions _E_ ( _εk_ · _Zk_ ) = 0, and with _Zk_ denoting the exogenous variables: the demand instruments, evolution of construction costs, the constant, and regional fixed effects in (3). 

In Table III, column (1), I start exploring the data by imposing a common supply inverse-elasticity parameter for all cities ( _βk_<sup>_S_=</sup><sup>_β S_∀</sup><sup>_k_). The estimates of</sup><sup>_β S_suggest a relatively elastic hous-</sup> ing supply on average, with an elasticity of 1.54 (1/0.65). This is well within the range of 1 to 3 proposed by the existing literature at the national level (for a review see Gyourko [2008]). Importantly, unreported regressions where I use each of the demand IV separately always yield similar and statistically significant results. 

From the model in Section III, I know that the inverse of supply elasticities should be a function of land availability with _∂βk/∂�k <_ 0. A first-degree linear approximation to this relationship can be posited as _βk_<sup>_S_=</sup><sup>_β_�</sup><sup>_S_+ (1 −</sup><sup>_�k_) ·</sup><sup>_β_LAND.10Thesupply</sup> equation becomes 



In Table III, column (2), as in all specifications thereafter, (1 − _�k_ )—the share of area _unavailable_ for development—is considered predetermined and exogenous to supply-side shocks in the period 1970–2000. Of course, mountains and coastal status could potentially be drivers for increased housing demand in the period under consideration. Note, however, that equation (4) is 

> 10. Nonlinear versions of the functional relationship between _βk_<sup>LAND</sup> and _�k_ did not add any improvement of economic or statistical significance to the fit of the supply equation in this small sample of 269 cities. Note that the specific functional form of _∂βk/∂�k_ in the model is driven by the assumptions on the nature of Ricardian land rents: these are solely due to commuting to the CBD, and commuting costs are linear. 

_THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1269 

|(6)<br>−5_._329<br>(0_._904)∗∗∗<br>0_._481<br>(0_._117)∗∗∗<br>0_._301<br>(0_._066)∗∗∗<br>0_._002<br>(0_._049)<br>−0_._115<br>(0_._048)∗∗<br>0_._035<br>(0_._046)<br>0_._061<br>(0_._045)∗∗∗<br>y to explain changes<br>anatory endogenous<br>us variable with the<br>for demand shocks<br>tifying assumptions<br>.|
|---|
|(5)<br>0_._516<br>(0_._116)∗∗∗<br>0_._268<br>(0_._068)∗∗∗<br>−0_._009<br>(0_._050)<br>−0_._116<br>(0_._050)∗∗<br>0_._069<br>(0_._063)<br>0_._601<br>(0_._046)∗∗∗<br>n the left-hand side, I tr<br>and side, the main expl<br> interact that endogeno<br>e. The instruments used<br> hours of sun. The iden<br>5%; ∗∗∗signifcant at 1%|
|ULATIONS<br>1970–2000<br>(4)<br>0_._060<br>(0_._215)<br>0_._511<br>(0_._214)∗∗∗<br>0_._237<br>(0_._130)∗<br>−0_._015<br>(0_._055)<br>−0_._129<br>(0_._069)∗<br>0_._059<br>(0_._072)<br>0_._528<br>(0_._058)∗∗∗<br>g supply equation. O<br>ext). On the right-h<br> Some specifcations <br>ogenous in this tabl<br>g of January average<br>0%; ∗∗signifcant at|
|III<br>NDLANDUSEREG<br>_�_log(_P_) (supply):<br>(3)<br>0_._305<br>(0_._146)∗∗∗<br>0_._449<br>(0_._140)∗∗∗<br>0_._106<br>(0_._065)<br>−0_._022<br>(0_._054)<br>−0_._163<br>(0_._062)∗∗∗<br>−0_._022<br>(0_._054)<br>0_._594<br>(0_._052)∗∗∗<br>of a metropolitan housin<br> costs (see theory and t<br>etween 1970 and 2000. <br>I), which we treat as ex<br>tion shocks, and the lo<br>re zero. ∗signifcant at 1|
|TABLE<br>HOUSINGSUPPLY: GEOGRAPHY A<br>(1)<br>(2)<br>_�_log(_Q_)<br>0_._650<br>0_._336<br>(0_._107)∗∗∗<br>(0_._116)∗∗∗<br>Unavailable land×_�_log(_Q_)<br>0_._560<br>(0_._118)∗∗∗<br>Log(1970 population)×<br>unavailable land×_�_log(_Q_)<br>log(WRI)×_�_log(_Q_)<br>_�_log(_Q_)×ocean<br>Midwest<br>−0_._099<br>−0_._041<br>(0_._054)∗<br>(0_._052)<br>South<br>−0_._236<br>−0_._170<br>(0_._065)∗∗∗<br>(0_._062)∗∗∗<br>West<br>0_._016<br>0_._057<br>(0_._076)<br>(0_._072)<br>Constant<br>0_._550<br>0_._594<br>(0_._055)∗∗∗<br>(0_._052)∗∗∗<br>_Notes_. Standard errors in parentheses. The table shows the coeffcient of 2SLS estimation<br>in median housing prices by metro area between 1970 and 2000, adjusted for construction <br>variable is the change in housing demand [the log of the number of households −log(_Q_)] b<br>unavailable land share (due to geography) and the log of the Wharton Regulation Index (WR<br>are a shift-share of the 1974 metropolitan industrial composition, the magnitude of immigra<br>are that the covariance between the residuals of the supply equations and the instruments a|



1270 

_QUARTERLY JOURNAL OF ECONOMICS_ 

consistently estimated even if demand shocks _�_ ln _Hk_ are also correlated with (1 − _�k_ ). Intuitively, land unavailability can be safely included in both the supply and demand equations insofar as there are enough exclusion restrictions specific to the supply equation. 

The results in Table III, column (2), strongly suggest that the impact of demand on prices is mediated by physical land unavailability. Moving within the interquartile range of land unavailability (9% to 39%), the estimates show the impact of demand shocks on prices to increase by about 25%. 

Are the results simply capturing the fact that cities with less land availability tend to be coastal? Table III, column (3), allows the impact of demand shocks to vary for coastal and noncoastal areas. Coastal areas are defined as MSAs within 100 km of the ocean (as calculated by Rappaport and Sachs [2003]). Formally _βk_<sup>_S_=</sup><sup>_β_�</sup><sup>_S_+ (1 −</sup><sup>_�k_) ·</sup><sup>_β_LAND + COAST</sup><sup>_k_·</sup><sup>_β_COAST,whereCOASTis</sup> a coastal status dummy. The results show the coastal variable not to be significant. Land unavailability is important within coastal (and noncoastal) areas. 

In column (4) of Table III, the inverse elasticity parameter is approximated by a linear function of land use regulations and geographic constraints: _βk_<sup>_S_=</sup><sup>_β_�</sup><sup>_S_+ (1 −</sup><sup>_�k_) ·</sup><sup>_β_LAND + ln WRI</sup><sup>_k_·</sup><sup>_β_REG.</sup> In this specification, ln WRI _k_ stands for the natural log of the WRI.<sup>11</sup> The supply equation becomes 



For now, ln WRI is assumed to be predetermined and exogenous to changes in housing prices through the period 1970–2000. As in all specifications hereafter, I cannot reject that _β_<sup>�</sup><sup>_S_</sup> = 0: the impact of demand shocks on prices is solely mediated by geographic and regulatory constraints, which is the assumption that I carry forward. In Table III, column (5), I explicitly present results of the model with the constraint _β_<sup>�</sup><sup>_S_</sup> = 0, which largely leaves the coefficients of interest unchanged. 

It is important to remark that independent regressions that consider changes in prices and housing units in the three decades 

> 11. I added three to the original index to ensure that log(WRI) always has positive support, which is consistent with the theoretical predictions of a positive supply parameter across the board. Alternative (unreported) normalizations never had major quantitative impacts on the estimates. 

_THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1271 

separately (1970s, 1980s, 1990s) cannot reject the coefficients on geography and regulations to be statistically equivalent across decades.<sup>12</sup> 

It is apparent that the elasticity of housing supply depends critically on both regulations and physical constraints. However, standard errors on the land unavailability parameter are larger. This can be explained by heterogeneity in how binding physical constraints are. Whereas regulatory constraints matter regardless of the existing level of construction, physical constraints may not be important until the level of development is high enough to render them binding. Using the model in the preceding section, it is straightforward to show that _∂_ ( _∂βk/∂�k_ ) _/∂_ POP _k <_ 0: the (negative) impact of land availability on inverse elastiticies should be stronger in larger metro areas. The most parsimonious way to capture this effect is to model the impact of physical constraints on elasticities as an interacted linear function of predetermined initial log population levels. In this specification _βk_<sup>_S_= (1 −</sup><sup>_�k_) ·</sup> _β_<sup>LAND</sup> + (1 − _�k_ ) · ln(POP _T_ −1) · _β_<sup>LAND</sup><sup>_,_POP</sup> + ln WRI · _β_<sup>REG</sup> . Hence the supply equation becomes 



The results in Table III, column (6), strongly suggest that physical constraints matter more in larger metropolitan areas, consistent with the theory. Figure I depicts the difference in the inverse of _βk_<sup>_S_(thatis,thesupplyelasticity)acrosstheinterquar-</sup> tile range of land availability as a function of initial population levels. In the graph, I assign the median level of regulation to all cities in order to create counterfactuals with respect to differences in land unavailability exclusively. At the lowest population levels supply elasticity is mostly determined by regulations: the difference between the seventy-fifth and twenty-fifth percentiles in the distribution of physical land constraints is not large. Nonetheless, geographic constraints become binding and have a strong 

> 12. The average coefficients across decades are _β_<sup>LAND</sup> = 0 _._ 29 and _β_<sup>REG</sup> = 0 _._ 21. Due to the strong mean-reversion of prices at decadal frequencies, the topography coefficient is closer to zero in the 1990s, but larger in the 1980s, whereas the opposite pattern is apparent for the regulation coefficient. They are close to the mean in the 1970s. 

# 1272 

## _QUARTERLY JOURNAL OF ECONOMICS_ 



<!-- Start of picture text -->
2.500<br>2.000<br>1.500<br>1.000<br>0.500<br>0.000<br>0 500 1,000 1,500 2,000 2,500 3,000 3,500 4,000<br>Population (1,000s)<br>Elasticity with low geographic constraints Elasticity with high geographic constraints<br>FIGURE I<br>Impact of Geography on Elasticities by Population<br>Elasticity<br><!-- End of picture text -->

impact on prices as metropolitan population becomes larger. In metropolitan areas above 1,000,000 inhabitants, moving from the twenty-fifth to the seventy-fifth percentile of land unavailability implies supply elasticities that are 40% smaller. 

# V. THE INDIRECT EFFECTS OF GEOGRAPHY 

# _V.A. Endogenous Regulations_ 

The previous results confirm the well-known empirical link between land use regulations and housing price growth. Recent examples in this literature include Glaeser, Gyourko, and Saks (2005a, 2005b), Quigley and Raphael (2005), and Saks (2008). However, the existing evidence has arguably not fully established a _causal_ link: regulations may be endogenous to the evolution of housing prices. 

In the theoretical literature, zoning and growth controls have long been regarded as endogenous devices to keep prices high in areas with valuable land (Hamilton 1975; Epple, Romer, and Filimon 1988; Brueckner 1995). In a review of much of this literature, Fischel (2001) develops the _homevoter hypothesis_ , according to which zoning and local land use controls can be largely understood as tools for local homeowners to maximize land prices. 

_THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1273 

To discuss these issues, consider a stylized version of the supply equation: 



Housing supply inverse elasticities are modeled here as an invariant coefficient ( _β_ ) plus a linear function of regulatory constraints (the log of the WRI). Assume that, in fact, the local supply elasticity varies for other reasons than regulation that are uncontrolled for in the model, 



where _βk_<sup>_δ_isalocaldeviationfromaveragesupplyelasticitiesun-</sup> related to regulation. Even with suitable instruments for _�_ ln _Hk_ , consistent estimates will not be obtained if ln WRI _k_ is correlated with _ξk_ . Consider as a working hypothesis the following empirical equation describing the optimal choice of voters with regard to land use policies: 



What are the potential sources of regulation endogeneity in equation (9), which includes an independent error term denoted by _μk_ ? In Ortalo-Magn´e and Prat (2007), voters may explicitly restrict the supply of land in order to keep its value high, but only have an incentive to do so in areas where land was initially dear. The only source of supply constraints in Ortalo-Magn´e and Prat (2007) comes from regulation, but there are additional reasons that in areas that were initially land-constrained voters may want _further_ limits on development (implying _ϕ_ 1 _>_ 0 in equation (9)). Consider the problem of a voter trying to maximize future land price growth. From the model in Section II, equilibrium housing prices in an initial steady state may be obtained as a function of local amenity–productivity levels. Assume now that we introduce some uncertainty about future amenity–productivity shocks, which are assumed to be uncorrelated with factors that condition initial population, such as geographic land availability (Gabaix 1999). In this context, expected changes to housing prices ( _E_ ( _�P_<sup>�</sup> _k_ )) are a function of expected productivity shocks ( _E_ ( _�χk_ )), as mediated by land availability. It is staightforward to show (see 

1274 

_QUARTERLY JOURNAL OF ECONOMICS_ 

Derivation 3 in Appendix II) that _dE_ ( _�P_<sup>�</sup> _k_ ) _/d�k <_ 0. Reduced land availability amplifies the effects of productivity shocks on home values. Conversely, productivity shocks largely translate into population growth in unconstrained cities. 

Moreover, _d_<sup>2</sup> _E_ ( _�P_<sup>�</sup> _k_ ) _/_ ( _d�k_ )<sup>2</sup> _>_ 0: the _marginal impact_ of additional land constraints on expected price growth is _larger in areas that already had lower land availability_ initially. The intuition for this result comes from the geometry of land development. Recall from the model that the average city radius corresponds to _�k_ = ~~�~~ _γ_ POP _k/�kπ_ ; decreasing land availability has a stronger impact in pushing away the city boundary at low initial values, thereby further increasing Ricardian land rents. In the presence of positive marginal costs of restrictive zoning, voters in landconstrained regions have more of an incentive to pass such regulations. Conversely, marginal changes in zoning regulations do not have much of an expected impact on home values in areas where land is naturally abundant, thereby reducing their strategic value. 

Furthermore, strategic growth-management considerations should be less of an issue in shrinking cities, where new constraints on growth are not binding, suggesting also that _ϕ_ 2 _>_ 0. 

Restrictive land use policies are not exclusively enacted in order to limit the supply of housing, however. Citizens’ demands for antigrowth regulations partially stem from the perceived nuisances of development, such as increased traffic, school congestion, and aesthetic impact on the landscape (Rybczynski 2007). These issues only arise in growing cities, and may be more salient in congested areas, where population densities are initially high. Therefore, restrictive nuisance zoning may be more prevalent in growing, land-constrained metro areas, which implies again that _ϕ_ 2 _>_ 0. 

The existing literature offers additional reasons to expect reverse causality from growing prices to higher regulations ( _ϕ_ 3 _>_ 0 in equation (9)). Recent examples include Fischel (2001) and Hilber and Robert-Nicoud (2006), who argue for a demand-side link from higher prices to increased growth controls. Several mechanisms have been identified that imply such a reverse causal link. 

Rational voters may want to enact restrictive zoning policies in regions with valuable land _even when they do not aim to increase metropolitan housing prices_ . Changes in the future local best-andhighest use of land are highly uncertain. Such uncertainty generates considerable wealth _risk_ for homeowners who are unsure 

# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1275 

about the nature of future neighborhood change (Breton 1973). Therefore “since residents cannot insure against neighborhood change, zoning offers a kind of second-best institution” (Fischel 2001, p. 10). In regions with high land values, voters limit the scope and extent of future land development in their jurisdiction in order to reduce housing wealth risk. Because all jurisdictions in a region try to deflect risks and compete `a la Tiebout, the equilibrium outcome at the metropolitan level implies stricter development constraints everywhere. Conversely, concerns about the variability of land values are absent in regions where home prices are close to, and pinned down by, structural replacement costs. 

Similarly, voters have vested interests in fiscal zoning (Hamilton 1975, 1976). In areas with very cheap land, development usually happens at relatively low densities. However, as land values in a metropolitan area or jurisdiction increase, new entrants into the community want to consume less land. Simultaneously, in metropolitan areas where the land input is relatively expensive, developers want to use less of it and build at higher densities. However, existing homeowners do not want new arrivals to pay lower-than-average taxes, which may induce them to mandate large lot sizes on new development. According to the fiscal-zoning theories, land use regulations should become more restrictive in areas with expensive land. 

In order to see whether the above theories have empirical content, I start by asking whether natural geographic constraints beget regulatory constraints. Table IV, column (1), displays regressions similar to equation (9) with the log of the WRI on the left-hand side. The main explanatory variable is the measure of undevelopable area. Geographic constraints were strongly associated with regulatory constraints in 2005, evidence consistent with _ϕ_ 1 _>_ 0 in equation (9). The regression includes other controls, such as regional fixed effects, the percentage of individuals older than 25 with a bachelor’s degree, and lagged white non-Hispanic shares.<sup>13</sup> 

Regardless of the evolution of local housing markets, there are regional differences in the propensity of local governments to regulate economic activity (Kahn 2002). As a proxy for preferences for 

> 13. A previous working paper version (Saiz 2008) explored other potential correlates of land use regulations across metropolitan areas. Alternative hypotheses based on local politics, optimal regulation of externalities, and snob-zoning do not change the importance of reverse causation and original land constraints to account for regulations and are never quantitatively large. 

1276 

_QUARTERLY JOURNAL OF ECONOMICS_ 

governmental activism (as opposed to laissez-faire), regressions in Table IV control for the log of the public expenditure on protective inspection and regulation by local governments at the MSA level as a share of total public revenues. The government expenditure category “Protective inspection and regulation” in the Census of Governments includes local expenditures in building inspections; weights and measures; regulation of financial institutions; taxicabs; public service corporations; private utilities; licensing, examination, and regulation of professional occupations; inspection and regulation or working conditions; motor vehicle inspection and weighting; and regulation and enforcement of liquor laws and sale of alcoholic beverages. As expected, areas that tended to regulate economic activity in other spheres also regulated residential land development more strongly. 

Regressions in Table IV also control for the share of Christians in nontraditional denominations in 1970, defined as one minus the Catholic and mainline protestant Christian shares.<sup>14</sup> Political scientists, economists, and historians of religion have claimed that the ethics and philosophy of nontraditional Christian denominations (especially those self-denominated Evangelical) are deeply rooted in individualism and the advocacy of limited government role.<sup>15</sup> Column (1) in Table IV (which controls for region fixed effects) finds that a one–standard deviation increase in the nontraditional Christian share in 1970 was associated with a − 0.21-standard deviation change in land use regulations. 

In column (2) of Table IV, I examine another source of endogeneity in equation (9), namely the possibility that _ϕ_ 2 _>_ 0. Landconstrained areas that have been declining or stagnating for a long time do not seem to display strong antigrowth policies. Consider the case of Charleston, West Virginia: 71% of its 50-km radius area is undevelopable according to our measure, yet the WRI’s value is −1.1. Similar examples are New Orleans (LA), Asheville (NC), Chattanooga (TN), Elmira (NY), Erie (PA), and Wheeling (WV). In order to capture the fact that antigrowth regulations may not be important in declining areas, I interact the geographicconstraints variable with a dummy for MSA in the bottom quartile of urban growth between 1940 and 1970 (column (2) in Table IV). 

> 14. Mainline Protestant denominations are defined as United Church of Christ, American Baptist, Presbyterian, Methodist, Lutheran, and Episcopal. 15. See Moberg (1972), Hollinger (1983), Magleby (1992), Holmer Nadesan (1999), Kyle (2006), Barnett (2008), and Swartz (2008). Crowe (2009) points to a negative correlation between housing price volatility and the Evangelical share, which could be explained by looser land use regulations in Evangelical areas. 

_THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1277 

||(4)|−0_._241<br>(0_._132)∗<br>0_._375<br>(0_._154)∗∗<br>0_._198<br>(0_._088)∗∗<br>0_._041<br>(0_._015)∗∗∗<br>−0_._291<br>(0_._090)∗∗∗<br>0_._089<br>(0_._404)<br>−0_._017<br>(0_._120)|
|---|---|---|
||(3)|−0_._174<br>(0_._125)<br>0_._451<br>(0_._158)∗∗∗<br>0_._051<br>(0_._015)∗∗∗<br>−0_._314<br>(0_._084)∗∗∗<br>0_._867<br>(0_._328)∗∗∗<br>−0_._069<br>(0_._116)|
|ONS|Log WRI<br>(2)|0_._165<br>(0_._069)∗∗<br>−0_._054<br>(0_._153)<br>−0_._076<br>(0_._051)<br>0_._047<br>(0_._015)∗∗∗<br>−0_._304<br>(0_._084)∗∗∗<br>0_._538<br>(0_._342)<br>0_._08<br>(0_._110)|
|ANDUSEREGULATI|(1)|0_._134<br>(0_._067)∗∗<br>0_._051<br>(0_._015)∗∗∗<br>−0_._308<br>(0_._086)∗∗∗<br>0_._983<br>(0_._332)∗∗∗<br>0_._036<br>(0_._113)|
|ENDOGENEITY OFL||Unavailable land, 50-km radius<br>Unavailable land in growing cities (1940–1970)<br>Unavailable land in declining cities (1940–1970)<br>Declining cities dummy (1940–1970)<br>Unavailable land, 50-km radius×<br>_�_log housing units (1970–2000)<br>_�_Log housing price (1970–2000)=log housing price (1970)<br>Log (inspection expenditures/local tax revenues) (1982)<br>Share of Christian “nontraditional” denominations (1970)<br>Share with bachelor’s degree in 1970<br>Non-Hispanic white share in 1980|



1278 

## _QUARTERLY JOURNAL OF ECONOMICS_ 

|TABLE IV<br>(CONTINUED)|Log WRI|(1)<br>(2)<br>(3)<br>(4)|Midwest<br>−0_._266<br>−0_._307<br>−0_._289<br>−0_._266<br>(0_._039)∗∗∗<br>(0_._039)∗∗∗<br>(0_._039)∗∗∗<br>(0_._044)∗∗∗<br>South<br>−0_._19<br>−0_._222<br>−0_._261<br>−0_._196<br>(0_._054)∗∗∗<br>(0_._053)∗∗∗<br>(0_._058)∗∗∗<br>(0_._066)∗∗∗<br>West<br>−0_._029<br>−0_._08<br>−0_._096<br>−0_._088<br>(0_._050)<br>(0_._050)<br>(0_._054)∗<br>(0_._056)<br>Constant<br>1_._425<br>1_._471<br>1_._578<br>−0_._759<br>(0_._137)∗∗∗<br>(0_._135)∗∗∗<br>(0_._144)∗∗∗<br>(1_._055)<br>Observations<br>269<br>269<br>269<br>269<br>_R_2<br>_._43<br>_._46<br>—<br>—<br>Method<br>FGLS<br>FGLS<br>2SLS<br>3SLS<br>_Notes_. Standard errors in parentheses. The dependent variable in all regressions is the log of the WRI for each metro area. To deal with heterogeneous sample sizes (strong<br>correlation of WRI values within MSA) columns (1) and (2) use a Feasible Generalized Least Squares (FGLS) procedure, where each observation is weighted proportionally to the<br>inverse of the square error of OLS estimates (which are actually always very close in magnitude and signifcance). In columns (3) and (4), changes in the log of local housing prices<br>and quantities are instrumented using the demand shocks in Table III (industry shift-share, hours of sun, and immigrant shocks), plus the land unavailability variable. ∗signifcant<br>at 10%; ∗∗signifcant at 5%; ∗∗∗signifcant at 1%.|
|---|---|---|---|



# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1279 

Lagged growth rates in a period that is, on the average, 45 years in the past are unlikely to be caused by the regulation environment in 2005. But they are likely to be good predictors of future growth, because of the permanence of factors that drove productivity during the second half of the 20th century, such as reliance on manufacturing or mining or relative scarcity of institutions of higher education. Similarly, in column (3) of Table IV, I interact the change in housing growth _between 1970 and 2000_ with the geographic land-unavailability variable. Of course, housing construction is endogenous to regulations in this equation. Hence I use the demand shock instruments in Table III and interactions with geographic land unavailability as instrumental variables for the interacted endogenous variable. The results suggest that regulations are stricter in land-constrained metro areas that are thriving ( _ϕ_ 2 _>_ 0). In declining cities, however, regulations are insensitive to previous factors that made housing supply inelastic. 

Finally, in column (4) of Table IV, I test for reverse causation from price levels to higher regulation ( _ϕ_ 3 _>_ 0 in equation (9)). Because _Pt_ = _�Pt,t_ − _n_ + _Pt_ − _n_ , I express the log of housing values in 2000 as the sum of the change in the log of prices plus the log of initial prices in 1970 (for comparability with Table III) and constrain the coefficient on both variables to be the same.<sup>16</sup> The instruments now are hours of sun, immigration shocks, and the Bartik (1991) employment shift-share and their interactions with geographic land unavailability. There are two endogenous variables: lagged changes in housing prices, and household growth interacted by the geographic constraints. The equation is estimated via 3SLS and strongly suggests that _both_ a constraining geography _in growing cities_ and higher housing prices led to a more regulated supply environment circa 2005. 

In sum, the regulation equations in Table IV demonstrate that higher housing prices, demographic growth, and natural constraints beget more restrictive land-use regulations. 

# _V.B. Endogeneizing Regulations in the Supply Equation_ 

Because regulations are endogenous to _εk_ in equations (5) and (6), one needs to use additional identifying exclusions to estimate housing supply elasticities. As suggested by the results in Table IV, the local public expenditure share in protective inspection and 

16. In unconstrained equations, I cannot reject that the separate coefficients on _�P_ 2000 _,_ 1970 and _P_ 1970 are statistically equivalent. 

1280 

_QUARTERLY JOURNAL OF ECONOMICS_ 

the nontraditional Christian share in 1970 can be used as instruments for the 2005 WRI: although they predict land use regulations, they are unlikely to impact land supply otherwise (note that the supply equation controls for the evolution of construction costs). As seen in Table IV, these variables prove also to be strong instruments.<sup>17</sup> Note that even if these variables were correlated with demand shocks, the regression have more supply-specific exclusion restrictions than endogenous variables and all parameters are fully identified. In fact, because the two endogenous variables appear in interacted form, I can now also include in the IV list the interactions of the instruments used for changes in quantities (hours of sun, employment shift-share, and immigration shocks) with those used for the regulation index (municipal inspections expenditure share and nontraditional Christian share). Importantly, _the results are very similar when I simply use each one of the regulation instruments separately._ 

Column (1) in Table V reestimates the specification in Table III, column (5) (elasticities as linear functions of regulations and geographic constraints), this time allowing for endogenous regulations. The coefficient on the WRI declines to about 60% of its previous value. However, when the model in equation (6) is reestimated (land constraints matter more in large cities), the coefficient on the regulation index takes a value that is only 8% smaller than in the earlier estimates. Therefore, parameters from previous research are bound to somewhat overestimate the impact of regulations on prices, but it is still true that more regulated areas tend to be relatively more inelastic, and this impact is quantitatively large. In Table V, column (2), a move across the interquartile range in the WRI of a city of one million inhabitants with average land availability is associated with close to a 20% reduction in supply elasticity: from 1.76 to 1.38. 

The impact of constrained geography is larger, especially in larger cities. For example, in a metro area with average regulations and a population of one million, the interquartile change in the share of unavailable land (from 0.09 to 0.38) implies a 50% reduction in supply elasticity (from 2.45 to 1.25). 

In a separate Online Appendix, the interested reader can further see that endogeneizing construction costs (which could be themselves a function of geography) and immigration shocks does not change the main parameters of interest. 

17. Partial _R_<sup>2</sup> of .074 in the first stage and _F_ -test of 10.413, above the 20% maximal bias threshold (8.75) in Stock and Yogo (2005). 

# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1281 

## TABLE V 

HOUSING SUPPLY: ENDOGENOUS REGULATIONS 

||_�_log(_P_) (s<br>|upply)<br>|
|---|---|---|
||(1)|(2)|
|Unavailable land×_�_log(_Q_)|0_._581<br>(0_._119)<sup>∗∗∗</sup>|−5_._260<br>(1_._396)<sup>∗∗∗</sup>|
|Log(1970 population)×unavailable||0_._475|
|land×_�_log(_Q_)||(0_._119)<sup>∗∗∗</sup>|
|Log(WRI)×_�_log(_Q_)|0_._109<br>(0_._078)<sup>∗</sup>|0_._280<br>(0_._077)<sup>∗∗∗</sup>|
|Midwest|−0_._009|0_._002|
||(0_._049)|(0_._048)|
|South|−0_._075|−0_._109|
||(0_._049)|(0_._049)<sup>∗∗</sup>|
|West|0_._149|0_._059|
||(0_._063)|(0_._065)|
|Constant|0_._659<br>(0_._048)<sup>∗∗∗</sup>|0_._577<br>(0_._048)<sup>∗∗∗</sup>|



_Notes._ Standard errors in parentheses. The table shows the coefficient of 2SLS estimation of a metropolitan housing supply equation. The specification and instruments used for demand shocks are as in Table III. Demand shocks are interacted with the unavailable land share (due to geography) and the log of the WRI. The latter variable is treated as endogenous using the share of local public expenditures on “protective inspections” and the share of nontraditional Christian denominations as instruments. Because we are instrumenting for log(WRI)× _�_ log( _Q_ ), I also include the interaction between the regulation and the demand instruments in the IV list.<sup>∗</sup> significant at 10%;<sup>∗∗</sup> significant at 5%;<sup>∗∗∗</sup> significant at 1%. 

# _V.C. Estimated Elasticities_ 

In this section, I use the coefficients in Table V, column (2), to estimate supply elasticities at the metro area level. Such estimates are simple nonlinear combinations of the available data on physical and regulatory constraints, and predetermined population levels in 2000. These elasticities are thus based on economic fundamentals related to natural and man-made land constraints and should prove useful in calibrating general equilibrium models of interregional labor mobility and in predicting the response of housing markets to future demand shocks. 

The population-weighted average elasticity of supply is estimated to be 1.75 in metropolitan areas (2.5 unweighted). The results for metropolitan areas with population over 500,000 in 2000 can be found in Table VI. Estimated elasticities using only the geographic, regulatory, and initial population variables agree with perceptions about supply-constrained areas. Miami, Los Angeles, San Francisco, Oakland, New York, San Diego, Boston, Chicago, 

1282 

## _QUARTERLY JOURNAL OF ECONOMICS_ 

and Seattle are among the top fifteen in the list of the most inelastic cities. Houston, Austin, Charlotte, Kansas City, and Indianapolis are among the large metro areas with highly elastic housing supply. 

Estimated elasticities (this time using predetermined 1970 population in order to avoid obvious endogeneity issues) also correlate very strongly with housing price levels in 2000 and changes over the 1970–2000 period. Figure II presents plots relating housing prices (Panel 1) or changes (Panel 2) on the vertical axis and the inverse of the estimated supply elasticity by metropolitan area on the horizontal axis. It is clear that a simple linear combination of physical and regulatory constraints goes very far to explain the evolution of prices, even without taking into account the differential demand shocks that cities experienced. 

# VI. CONCLUSION 

The paper started by providing empirical content to the concept of land availability in metropolitan areas. Using satellitegenerated data, I calculated an exact measure of land unavailable for real estate development in the metropolitan United States. This geographic measure can be used in future work exploring topics as diverse as housing and mortgage markets, labor mobility, urban density, transportation, and urban environmental issues. 

I then developed a model for the impact of land availability on urban development and housing prices. In _ex post_ equilibrium, land-constrained metro areas should have more expensive housing and enjoy higher amenities or productivity, as confirmed by the data. The model demonstrates that land constraints should also decrease housing supply _elasticities_ , a somewhat _ad hoc_ assumption in previous literature. 

Empirically, most areas that are widely regarded as supplyinelastic were found, in fact, to be severely land-constrained by their geography. Deploying a new comprehensive survey on residential land use regulations, I found that highly regulated areas tend to be geographically constrained also. More generally, I found recent housing price and population growth to be predictive of more restrictive residential land regulations. The results point to the endogeneity of land use controls with respect to the housing market equilibrium. 

Hence I next estimated a model where regulations are both causes and consequences of housing supply inelasticity. Housing 

_THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1283 

|POPULATION_>_500,000)<br>MSA/NECMA name<br>Supply elasticity|Vallejo–Fairfeld–Napa, CA<br>1.14<br>Newark, NJ<br>1.16<br>Charleston–North Charleston, SC<br>1.20<br>Pittsburgh, PA<br>1.20<br>Tacoma, WA<br>1.21<br>Baltimore, MD<br>1.23<br>Detroit, MI<br>1.24<br>Las Vegas, NV–AZ<br>1.39<br>Rochester, NY<br>1.40<br>Tucson, AZ<br>1.42<br>Knoxville, TN<br>1.42<br>Jersey City, NJ<br>1.44<br>Minneapolis–St. Paul, MN–WI<br>1.45<br>Hartford, CT<br>1.50<br>Springfeld, MA<br>1.52<br>Denver, CO<br>1.53<br>Providence–Warwick–Pawtucket, RI<br>1.61<br>Washington, DC–MD–VA–WV<br>1.61<br>Phoenix–Mesa, AZ<br>1.61<br>Scranton–Wilkes-Barre–Hazleton, PA<br>1.62<br>Harrisburg–Lebanon–Carlisle, PA<br>1.63<br>Bakersfeld, CA<br>1.64<br>Philadelphia, PA–NJ<br>1.65<br>Colorado Springs, CO<br>1.67<br>Albany–Schenectady–Troy, NY<br>1.70|
|---|---|
|OAREAS WITH<br>city<br>Rank|26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50|
|SUPPLYELASTICITIES(METR<br>MSA/NECMA name<br>Supply elasti|Miami, FL<br>0.60<br>Los Angeles–Long Beach, CA<br>0.63<br>Fort Lauderdale, FL<br>0.65<br>San Francisco, CA<br>0.66<br>San Diego, CA<br>0.67<br>Oakland, CA<br>0.70<br>Salt Lake City–Ogden, UT<br>0.75<br>Ventura, CA<br>0.75<br>New York, NY<br>0.76<br>San Jose, CA<br>0.76<br>New Orleans, LA<br>0.81<br>Chicago, IL<br>0.81<br>Norfolk–Virginia Beach–Newport<br>0.82<br>News, VA–NC<br>West Palm Beach–Boca Raton, FL<br>0.83<br>Boston–Worcester–Lawrence–Lowell–<br>0.86<br>Brockton, MA–NH<br>Seattle–Bellevue–Everett, WA<br>0.88<br>Sarasota–Bradenton, FL<br>0.92<br>Riverside–San Bernardino, CA<br>0.94<br>New Haven–Bridgeport–Stamford–<br>0.98<br>Danbury–Waterbury, CT<br>Tampa–St. Petersburg–Clearwater, FL<br>1.00<br>Cleveland–Lorain–Elyria, OH<br>1.02<br>Milwaukee–Waukesha, WI<br>1.03<br>Jacksonville, FL<br>1.06<br>Portland–Vancouver, OR–WA<br>1.07<br>Orlando, FL<br>1.12|
|Rank|1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25|



1284 

_QUARTERLY JOURNAL OF ECONOMICS_ 

|(CONTINUED)<br>ticity Rank MSA/NECMA name<br>Supply elasticity|74<br>Atlanta, GA<br>2.55<br>75<br>Akron, OH<br>2.59<br>76<br>Richmond–Petersburg, VA<br>2.60<br>77<br>Youngstown–Warren, OH<br>2.63<br>78<br>Columbia, SC<br>2.64<br>79<br>Columbus, OH<br>2.71<br>80<br>Greenville–Spartanburg–Anderson, SC<br>2.71<br>81<br>Little Rock–North Little Rock, AR<br>2.79<br>82<br>Fort Worth–Arlington, TX<br>2.80<br>83<br>San Antonio, TX<br>2.98<br>84<br>Austin–San Marcos, TX<br>3.00<br>85<br>Charlotte–Gastonia–Rock Hill, NC–SC<br>3.09<br>86<br>Greensboro–Winston–Salem–High Point, NC<br>3.10<br>87<br>Kansas City, MO–KS<br>3.19<br>88<br>Oklahoma City, OK<br>3.29<br>89<br>Tulsa, OK<br>3.35<br>90<br>Omaha, NE–IA<br>3.47<br>91<br>McAllen–Edinburg–Mission, TX<br>3.68<br>92<br>Dayton–Springfeld, OH<br>3.71<br>93<br>Indianapolis, IN<br>4.00<br>94<br>Fort Wayne, IN<br>5.36<br>95<br>Wichita, KS<br>5.45|
|---|---|
|pply elas|1.74<br>1.74<br>1.76<br>1.83<br>1.84<br>1.86<br>1.99<br>2.04<br>2.07<br>2.11<br>2.11<br>2.14<br>2.18<br>2.21<br>2.21<br>2.24<br>2.29<br>2.30<br>2.34<br>2.35<br>2.36<br>2.39<br>2.46|
|k MSA/NECMA name<br>Su|Gary, IN<br>Baton Rouge, LA<br>Memphis, TN–AR–MS<br>Buffalo–Niagara Falls, NY<br>Fresno, CA<br>Allentown–Bethlehem–Easton, PA<br>Wilmington–Newark, DE–MD<br>Mobile, AL<br>Stockton–Lodi, CA<br>Raleigh–Durham–Chapel Hill, NC<br>Albuquerque, NM<br>Birmingham, AL<br>Dallas, TX<br>Syracuse, NY<br>Toledo, OH<br>Nashville, TN<br>Ann Arbor, MI<br>Houston, TX<br>Louisville, KY–IN<br>El Paso, TX<br>St. Louis, MO–IL<br>Grand Rapids–Muskegon–Holland, MI<br>Cincinnati, OH–KY–IN|
|Ran|51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73|



# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1285 



<!-- Start of picture text -->
13 (a)<br>12.5<br>12<br>11.5<br>11<br>0 .5 1 1.5 2<br>Inverse of supply  elasticity<br>Log median house value Fitted values<br><!-- End of picture text -->



<!-- Start of picture text -->
3 (b)<br>2.5<br>2<br>1.5<br>0 .5 1 1.5 2<br>Inverse of supply elasticity<br>Log price 2000 – log price 1970 Fitted values<br><!-- End of picture text -->

FIGURE II 

Estimated Elasticities and Home Values (2000) (a) Levels, (b) changes. 

1286 

_QUARTERLY JOURNAL OF ECONOMICS_ 

demand, construction, and regulations are all determined endogenously. Housing supply elasticities were found to be well characterized as functions of both physical and regulatory land constraints, which in turn are endogenous to prices and past growth. 

Geography was shown to be one of the most important determinants of housing supply inelasticity: directly, via reductions in the amount of land availability, and indirectly, via increased land values and higher incentives for antigrowth regulations. The results in the paper demonstrate that geography is a key factor in the contemporaneous urban development of the United States, and help us understand why robust national demographic growth and increased urbanization has translated mostly into higher housing prices in San Diego, New York, Boston, and Los Angeles, but into rapidly growing populations in Atlanta, Phoenix, Houston, and Charlotte. 

APPENDIX I DESCRIPTIVE STATISTICS 

||Mean<br>(standard dev.)|
|---|---|
|Log population in 2000|12_._893<br>(1_._060)|
|Log median house value in 2000|11_._592<br>(0_._342)|
|_�_log median house value (1970–2000)|1_._937<br>(0_._213)|
|Log income in 2000|10_._200<br>(0_._184)|
|_�_log(income per capita) (1990–2000)|0_._401<br>(0_._063)|
|Log population (1990–2000)|0_._123<br>(0_._099)|
|Immigrants (1990–2000)/population (2000)|0_._034<br>(0_._038)|
|Share with bachelor’s degree (2000)|0_._198<br>(0_._063)|
|Share workers in manufacturing (2000)|0_._174<br>(0_._071)|
|Log(patents/population) (2000)|−8_._978<br>(0_._866)|
|January monthly hours of sun (average 1941–1970)|151_._342<br>(38_._199)|
|Log tourist visits per person (2000)|−12_._679<br>(0_._830)|



# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1287 

APPENDIX I (CONTINUED) 

||Mean<br>(standard dev.)|
|---|---|
|Ocean dummy|0_._331<br>|
||(0_._471)|
|Unavailable land, 50-km radius|0_._261<br>(0_._212)|
|Log(WRI)|1_._025|
||(0_._278)|
|_�_log housing units (1970–2000)|0_._599<br>(0_._319)|
|Log housing price (1970)|9_._655<br>(0_._228)|
|Log (inspection expenditures/local tax revenues)|−5_._826<br>(0_._971)|
|Share of Christian “nontraditional” denominations|0_._351<br>(0_._209)|
|Share with bachelors degree in 1970<br>|0_._111<br>(0_._042)|
|Non-Hispanic white share in 1980|0_._827<br>(0_._138)|
|Midwest|0_._264|
||(0_._442)|
|South|0_._383|
||(0_._487)|
|West|0_._201<br>(0_._401)|
|Unionization in construction sector|0_._208<br>(0_._146)|
|_�_log(income per capita) (1970–2000)|1_._965<br>(0_._116)|



# APPENDIX II: DERIVATIONS AND PROOFS 

_Derivation 1._ First, note that a share of 2 _πd�k/γ_ POP _k_ households live in the sector of the circle at a distance _d_ from the CBD. Average housing rents in the city, conditional on population, can thus be obtained as � _rk_ = �0 _�k_<sup>(2</sup><sup>_πx�k/γ_POP</sup><sup>_k_) ·</sup><sup>_r_(</sup><sup>_x_) ·</sup><sup>_dx_,which</sup> � _�k_ implies that _rk_ = (2 _π�k/γ_ POP _k_ ) �0<sup>(</sup><sup>_r_0</sup><sup>_x_−</sup><sup>_tx_2)</sup><sup>_dx_,andso�</sup><sup>_rk_=</sup> (2 _π�k/γ_ POP _k_ ) · [ 2<sup><u>1</u></sup><sup>_r_0</sup><sup>_x_2 −</sup><sup><u>1</u></sup> 3<sup>_tx_3]</sup> 0<sup>_�k_.Therefore�</sup><sup>_rk_= (2</sup><sup>_π�k/γ_POP</sup><sup>_k_) ·</sup> [ 2<sup><u>1</u></sup><sup>_r_0</sup><sup>_�_</sup> _k_<sup>2−</sup><sup><u>1</u></sup> 3<sup>_t�_</sup> _k_<sup>3] = (</sup><sup>_�_2</sup> _k_<sup>_π�k/γ_POP</sup><sup>_k_) · [</sup><sup>_r_0−</sup><sup><u>2</u></sup> 3<sup>_t�k_] = {[(</sup><sup>_γ_POP</sup><sup>_k/_(</sup><sup>_�kπ_)) ·</sup> _π�k_ ] _/γ_ POP _k_ } · [ _r_ 0 −<sup><u>2</u></sup> 3<sup>_t�k_] = [</sup><sup>_r_0 −</sup><sup>_t_</sup><sup><u>2</u></sup> 3<sup>_�k_],</sup> which corresponds to rents in the location that is two-thirds of the way between the 

1288 

_QUARTERLY JOURNAL OF ECONOMICS_ 

CBD and the city’s fringe. Substituting for the value of _r_ ( 3<sup><u>2</u></sup><sup>_�k_)</sup> yields � _rk_ = _i_ CC +<sup><u>1</u></sup> 3<sup>_t_</sup> ~~�~~ _γ_ POP _k/�kπ_ . 

_Derivation 2._ Recall that 



Substituting into the intercity spatial equilibrium equation, I obtain _r_ (POP _k, d_ ) =<sup>�</sup> _Ak_ + � _wk_ − ( _ψ_ + _α_ )<sup>~~√~~</sup> POP _k_ − _td_ . Because all consumers are indifferent, I can focus w.o.l.o.g. on consumers living in the CBD. Recalling that _Hk_ = POP _k_ yields _r_ 0 =<sup>�</sup> _Ak_ + _w_ � _k_ − ( _ψ_ + _α_ )<sup>~~√~~</sup> _Hk_ . Defining _P_ (0) = _r_ 0 _/i_ , one obtains the demand schedule for housing in the city: 



Note also that changes in _P_ (0) shift all prices within a city vertically by the same amount and so, denoting _P_<sup>�</sup> _k_ as the average housing price in city _k_ , the city demand equation implies that _∂_ ln( _Hk_ ) _/∂ P_<sup>�</sup> _k_ = _∂_ ln( _Hk_ ) _/∂ P_ (0). Now recall the expression for rents in the CBD from the supply of land: _r_ 0 = _i_ CC + _t_ ~~�~~ _γ Hk/�kπ,_ which implies that _P_ (0) = CC + _i_<sup>_<u>t</u>_</sup> ~~�~~ _γ Hk/�kπ_ . 

I can combine this supply-side price equation at the CBD with equation (11) to obtain<sup>�</sup> _Ak_ + � _wk_ − ( _ψ_ + _α_ )<sup>~~√~~</sup> _Hk_ = _i_ CC + _t_ (<sup>~~√~~</sup> _γ/�kπ_ )<sup>√</sup> _Hk_ . Solving for housing yields 



_Proof of Proposition 1._ The city-specific inverse elasticity of supply is _βk_<sup>_S_=</sup><sup>_∂_ln</sup> _P_<sup>�</sup> _k/∂_ ln _Hk_ =<sup><u>1</u></sup> 2<sup>[</sup> 3<sup><u>1</u></sup> _i_<sup>_t_(</sup> ~~�~~ _γ Hk/�kπ_ ) _/P_<sup>�</sup> _k_ ], and therefore 



_Proof of Proposition 2._ I focus on relevant joint amenity and productivity shocks net of annuitized construction costs that are compatible with habitation: _χk_ ≡<sup>�</sup> _Ak_ + � _wk_ − _i_ CC _>_ 0. I further normalize the minimum city size that classifies a population center as metropolitan to one (POP _k_ = _Hk_ = 1). The unit 

# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1289 

of population measurement could be, for instance, 50,000 people, which is the actual population level that qualifies an urban area for metropolitan status in the United States. The minimum necessary net wage–amenity shock observed in metropolitan areas ( _<u>χ</u>_ <u>)</u> is obtained with _�k_ = 1 (all land is developable) and therefore _<u>χ</u>_ = ( _ψ_ + _α_ ) + _t_<sup>~~√~~</sup> _γ/π_ . Similarly, I denote the minimum amenity–productivity shock that a city with land availability ( _� j_ ) requires to reach metropolitan status as _χ_ ( _�_ _<u>j</u>_ ) = _<u>χ</u>_ + _t_<sup>~~√~~</sup> _γ/π_ [(1 _/_<sup><u>�</u></sup> _� j_ ) − 1]. Start by defining _ε_ ( _� j_ ) = _χ_ ( _�_ _<u>j</u>_ ) − _<u>χ</u>_ , to obtain _ε j_ = _t_<sup>~~√~~</sup> _γ/π_ [(1 _/_<sup>�</sup> _� j_ ) − 1]. By assumption, conditional on qualifying as a metropolitan area, amenity–productivity shocks in land-unconstrained cities ( _�k_ = 1) are drawn from the Pareto cdf: _λ λ_ +1 _f_ ( _χ/χ_ ≥ _<u>χ, λ</u>_ ) = _λχ /χ_ , with _λ >_ 2. Thus the expected value of shocks in such cities is _E_ ( _χ/χ_ ≥ _<u>χ</u> , λ_ ) = _λχ/_ ( _λ_ − 1). 

In turn, amenity–productivity shocks in land-constrained metropolitan areas with _� j <_ 1 will be drawn ( _ex post_ ) from distributions with support <u>[</u> _<u>χ</u>_ + _ε_ ( _� j_ ) _,_ ∞]. The Pareto cdf implies that _F_ ( _<u>χ</u>_ + _ε_ ( _� j_ )) = 1 − <u>(</u> _<u>χ/χ</u>_ + _ε_ ( _� j_ ))<sup>_λ_</sup> , and so the upper tail truncated at _<u>χ</u>_ + _ε_ ( _� j_ ) has mass ( _<u>χ/χ</u>_ + _ε_ ( _� j_ ))<sup>_λ_</sup> . Therefore 



which is itself Pareto distributed. Note that _E_ ( _χ/χ_ ≥ _<u>χ</u>_ + _ε_ ( _� j_ )) = _E_ ( _χ/_ POP _j_ ≥ 1 _� j_ ), and therefore _E_ ( _χ/_ POP _j_ ≥ 1 _, � j_ ) = _λ_ [ _<u>χ</u>_ + _ε j_ ( _� j_ )] _/_ [ _λ_ − 1], which is a decreasing function in land availability. 

_Proof of Proposition 3._ Recall that POP _k_ = {( _χk/_ [( _ψ_ + _α_ ) + _t_ _<u>γ</u>_ ~~�~~ _�kπ_<sup>)}2. Using the relevant pdf:</sup> 





1290 _QUARTERLY JOURNAL OF ECONOMICS_ 



Because the first part of the equation defines the minimum population level normalized at one: _E_ (POP _j/_ POP _j_ ≥ 1 _, � j_ ) = _λ/_ ( _λ_ − 2). 

_Derivation 3._ Recall the equilibrium population level: 



Substituting back into the supply equation, we obtain the equilibrium average price 



_THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1291 

Therefore changes in productivity–amenities imply 



The expectation of changes in housing prices is therefore 



which, given the independence assumption of productivity shocks, implies that 



Now, we can demonstrate that 



More importantly, 



Therefore the expected price change is a decreasing convex function of land availability: wherever land availability is high initially, further changes in land availability do not change expected price growth much. Conversely, in areas with initially low land availability, further constraints on land development have greater impacts on future prices. 

1292 

## _QUARTERLY JOURNAL OF ECONOMICS_ 

|Notes<br> <br>See_Data_section in text.<br>A dummy that takes value 1 if growth is in the<br>lowest quartile of the metro areas in our sample.<br>The difference in the number of foreign-born<br>individuals between 1970 and 2000, divided by<br>the metro area population in 1970.<br>Calculated as one minus the share of Catholic<br>Church adherents and mainline Protestants<br>(United Church of Christ, American Baptist,<br>Presbyterian, Methodist, Lutheran, and<br>Episcopal).|
|---|
|Source<br>Calculated by author from elevation and land<br>use GIS data from USGS<br>Gyourko, Saiz, and Summers (2008)<br>Calculated by author from data in Historical<br>Census Browser—University of Virginia<br>HUD State of the Cities database (from the<br>Census)<br>HUD State of the Cities database (from the<br>Census)<br>HUD State of the Cities database (from the<br>Census)<br>Carlino and Saiz (2008)<br>Glaeser and Saiz (2004)<br>HUD State of the Cities database (from the<br>Census)<br>HUD State of the Cities database (from the<br>Census)<br>HUD State of the Cities database (from the<br>Census)<br>HUD State of the Cities database (from the<br>Census)<br>Churches and church membership in the<br>United States, 1971—the Association of<br>Religion data archives<br>County and City Data Book 1983|
|availability<br>Regulation Index<br>g metro area: 1950–1970<br>panic white share (1970)<br>hare (1970)<br>born share (1970)<br>visits per person (2000)<br>nts per capita<br>tion shock<br>workers in manufacturing<br><br>housing price (1970, 2000)<br>of housing units (1970,<br>ge of Christians in<br>aditional” denominations,<br>for Carter (1980)|
|Variable<br>Land un<br>Wharton<br>Declinin<br>Non-His<br>BA/BS s<br>Foreign-<br>Tourist<br>Log pate<br>Immigra<br>Share of<br>(1970)<br>Median<br>Number<br>2000)<br>Percenta<br>“nontr<br>1971<br>% voting|



# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1293 

|Notes<br>2000 county-based metropolitan defnitions were used to<br>aggregate at the metro level.<br>A dummy that takes value 1 if the minimum distance in an<br>MSA’s county is below 100 km.<br>Davis and Heathcote (2007) calculate the average share of<br>land for residential real estate in the United States in 1970<br>to be 20%. In 1984 (the frst year for which their<br>metropolitan data series is available) Davis and Palumbo<br>(2008) suggest national and metropolitan land shares to be<br>very similar. We therefore adapt an unweighted average<br>20% land share_across metropolitan areas_in 1970. We then<br>calculate differences in the structure cost/value ratio by<br>dividing the average construction cost in 1970 for a 2,000<br>sq. ft. home (the average home size) by the median home<br>value in each metro area. The fnal metropolitan-level<br>estimate of structural shares in 1970 (_αit_−1) is proportional<br>to the aforementioned ratio, and such that its unweighted<br>mean across metro areas is 80%.|
|---|
|Source<br>Census of Governments 1982<br>Census of Governments 1982<br>Rappaport and Sachs (2003)<br>Natural Amenities Scale—USDA<br>Economic Research Service<br>Gyourko and Saiz (2006)—originally<br>from Means et al.<br>x Freddie Mac purchase-only<br>conventional mortgage home price<br>index<br>Davis and Heathcote (2007); Davis<br>and Palumbo (2008)<br>County and City Data Books 1972,<br>2002|
|Variable<br>Local tax revenues (1982)<br>Inspection expenditures/local<br>tax revenues (1982)<br>Coastal metro area dummy<br>January monthly hours of sun<br>(average 1941–1970)<br>Construction costs<br>(single-family, average<br>quality)<br>Housing price repeat sales inde<br>Land value shares<br>Central city areas (1970, 2000)|



1294 

_QUARTERLY JOURNAL OF ECONOMICS_ 

THE WHARTON SCHOOL, UNIVERSITY OF PENNSYLVANIA 

# REFERENCES 

- Alonso, W., _Location and Land Use_ (Cambridge, MA: Harvard University Press, 1964). 

Altonji, Joseph, and David Card, “The Effects of Immigration on the Labor Market Outcome of Less-Skilled Natives,” Princeton University, Department Of Economics, Industrial Relations Section, Working Paper 636, 1989. Barnett, Timothy, “Evangelicals and Economic Enlightment,” paper for the 2008 Annual Conference of the American Political Science Association, 2008. 

Bartik, Timothy, “Who Benefits from State and Local Economic Development Policies?” W. E. Upjohn Institute For Employment Research, Kalamazoo, MI, 1991. Breton, Albert, “Neighborhood Selection and Zoning,” in _Issues In Urban Public Economics,_ Harold Hochman, ed. (Saarbrucken: Institute Internationale De Finance Publique, 1973). 

Brueckner, Jan K., “The Structure of Urban Equilibria: A Unified Treatment of the Muth–Mills Model,” in _Handbook Of Regional And Urban Economics_ , Volume II, E. S. Mills. ed. (Princeton, NJ: Elsevier, 1987). 

- Brueckner, Jan K., “Strategic Control of Growth in a System of Cities,” _Journal of Public Economics_ , 57 (1995), 393–416. 

- Burchfield, Marcy, Henry G. Overman, Diego Puga, and Matthew A. Turner, “Causes of Sprawl: A Portrait from Space,” _Quarterly Journal of Economics,_ 121 (2006), 587–633. 

- Capozza, Dennis R., and Robert W. Helsley, “The Stochastic City,” _Journal of Urban Economics,_ 28 (1990), 187–203. 

- Carlino, Jerry, and Albert Saiz, “Beautiful City: Leisure Amenities and Urban Growth,” Federal Reserve Bank of Philadelphia Working Paper SSRN1280157, 2008. 

- Combes, Pierre-Philippe, Gilles Duranton, Laurent Gobillon, and S´ebastien Roux, “Estimating Agglomeration Economies with History, Geology, and Worker Effects,” Groupement de Recherche en Economie Quantitative d’Aix-Marseille Working Paper, 2009. 

- Crowe, Christopher, “Irrational Exuberance in the U.S. Housing Market: Were Evangelicals Left Behind?” IMF Working Paper 09/57, 2009. 

- Davis, Morris, and Jonathan Heathcote, “The Price and Quantity of Residential Land in the United States,” _Journal of Monetary Economics_ , 54 (2007), 2595– 2620. 

- Davis, Morris, and Michael G. Palumbo, “The Price of Residential Land in Large U.S. Cities,” _Journal of Urban Economics_ , 63 (2008), 352–384. 

- Eeckout, Jan, “Gibrat’s Law for (All) Cities,” _American Economic Review,_ 94 (2004), 1429–1451. 

- Epple, Dennis, Thomas Romer, and Radu Filimon, “Community Development with Endogenous Land Use Controls,” _Journal of Public Economics_ , 35 (1988), 133– 162. 

- Fischel, William A., _The Homevoter Hypothesis: How Home Values Influence Local Government_ (Cambridge, MA: Harvard University Press, 2001). 

- Gabaix, Xavier, “Zipf’s Law for Cities: An Explanation,” _Quarterly Journal of Economics,_ 114 (1999), 739–767. 

- Glaeser, Edward, “Reinventing Boston: 1640–2003,” _Journal of Economic Geography_ , 5 (2005a), 119–153. 

- ——, “Urban Colossus: Why New York Is America’s Largest City,” _Federal Reserve Bank of New York Economic Policy Review_ , 11 (2005b), 7–24. 

- Glaeser, Edward, and Joseph Gyourko, “Housing Cycles.” NBER Working Paper 12787, 2006. 

- Glaeser, Edward, Joseph Gyourko, and Raven Saks, “Why Have Housing Prices Gone Up?” _American Economic Review_ , 95 (2005a), 329–333. 

- ——, “Why Is Manhattan So Expensive? Regulation and Rise in Housing Prices,” _Journal of Law and Economics_ , 48 (2005b), 331–370. 

- ——, “Urban Growth and Housing Supply,” _Journal of Economic Geography_ , 6 (2006), 71–89. 

# _THE GEOGRAPHIC DETERMINANTS OF HOUSING SUPPLY_ 1295 

Glaeser, Edward L., Jed Kolko, and Albert Saiz, “Consumer City,” _Journal of Economic Geography,_ 1 (2001), 27–50. 

Glaeser, Edward, and Albert Saiz, “The Rise of the Skilled City,” _Brookings– Wharton Papers on Urban Affairs_ , 1 (2004), 47–105. 

Gyourko, Joseph, “Looking Back to Look Forward: What Can We Learn about Urban Development from Philadelphia’s 350-Year History?” _Brookings–Wharton Papers on Urban Affairs_ , 1 (2005), 1–58. 

- ——, “Housing Supply,” Zell–Lurie Real Estate Center, The Wharton School, University of Pennsylvania Working Paper, 2008. 

Gyourko, Joseph, and Albert Saiz, “Construction Costs and the Supply of Housing Structure,” _Journal of Regional Science_ , 46 (2006), 661–680. 

Gyourko, Joseph, Albert Saiz, and Anita A. Summers, “A New Measure of the Local Regulatory Environment for Housing Markets: The Wharton Residential Land Use Regulatory Index,” _Urban Studies_ , 45 (2008), 693–729. 

- Hamilton, Bruce W., “Zoning and Property Taxation in a System of Local Governments,” _Urban Studies_ , 12 (1975), 205–211. 

- ——, “Capitalization of Intrajurisdictional Differences in Local Tax Prices,” _American Economic Review_ , 99 (1976), 743–753. 

- Hilber, Christian, and Fr´ed´eric Robert-Nicaud, “Owners of Developed Land versus Owners of Undeveloped Land: Why Land Use Is More Constrained in the Bay Area Than in Pittsburgh,” CEP Discussion Paper No. 760 (LSE), 2006. 

- Hollinger, Dennis P., _Individualism and Social Ethics: An Evangelical Syncretism_ (Boston: University Press of America, 1983). 

- Holmer Nadesan, Majia, “The Discourses of Corporate Spiritualism and Evangelical Capitalism,” _Management Communication Quarterly: MCQ,_ 13 (1999), 3– 42. 

- Kahn, Matthew, “Demographic Change and the Demand for Environmental Regulation,” _Journal of Policy Analysis and Management_ , 21 (2002), 45–62. 

- Kiel, Katherine A., and Jeffrey E. Zabel, “The Accuracy of Owner-Provided House Values: The 1978–1991 American Housing Survey,” _Real Estate Economics,_ 27 (1999), 263–298. 

- Kyle, Richard G., _Evangelicalism: An Americanized Christianity_ (New Brunswick, NJ: Transaction Publishers, 2006). 

- Magleby, Daniel B., “Political Behavior,” in _The Encyclopedia of Mormonism_ , D. Ludlow, ed. (New York: Macmillan, 1992). 

- Malpezzi, Stephen, “Housing Prices, Externalities, and Regulation in U.S. Metropolitan Areas,” _Journal of Housing Research_ , 7 (1996), 209–241. 

- Malpezzi, Stephen, Gregory H. Chun, and Richard K. Green, “New Place-to-Place Housing Price Indexes for U.S. Metropolitan Areas, and Their Determinants,” _Real Estate Economics_ , 26 (1998), 235–274. 

- Mayer, Christopher J., and C. Tsuriel Somerville, “Residential Construction: Using the Urban Growth Model to Estimate Housing Supply,” _Journal of Urban Economics_ , 48 (2000), 85–109. 

- Mills, Edwin, “An Aggregative Model of Resource Allocation in a Metropolitan Area,” _American Economic Review_ , 57 (1967), 197–210. 

- Moberg, David O., _The Great Reversal: Evangelism and Social Concern_ (Philadelphia: Lippincott, 1972). 

- Muth, Richard, _Cities and Housing_ (Chicago: University of Chicago Press, 1969). 

- Ortalo-Magn´e, Francois, and Andrea Prat, “The Political Economy of Housing Supply: Homeowners, Workers, and Voters,” LSE: STICERD—Theoretical Economics Paper Series No. /2007/514, 2007. 

- Ottavianno, Gianmarco, and Giovanni Peri, “The Effects of Immigration on US Wages and Rents: A General Equilibrium Approach,” CEPR Discussion Papers 6551 (revised), 2007. 

- Pence, Karen M., and Brian Bucks, "Do Homeowners Know Their House Values and Mortgage Terms?" FEDS Working Paper No. 2006-03, 2006. 

- Quigley, John M., and Steven Raphael, “Regulation and the High Cost of Housing in California,” _American Economic Review_ , 94 (2005), 323–328. 

- Rappaport, Jordan, “Moving to Nice Weather,” _Regional Science and Urban Economics,_ 37 (2007), 375–398. 

- Rappaport, Jordan, and Jeffrey D. Sachs, “The United States as a Coastal Nation,” _Journal of Economic Growth_ , 8 (2003), 5–46. 

# 1296 

## _QUARTERLY JOURNAL OF ECONOMICS_ 

Rose, Louis A., “Topographical Constraints and Urban Land Supply Indexes,” _Journal of Urban Economics_ , 26 (1989a), 335–347. 

——, “Urban Land Supply: Natural and Contrived Reactions,” _Journal of Urban Economics_ , 25 (1989b), 325–345. 

Rosenthal, Stuart, and William C. Strange, “The Attenuation of Human Capital Spillovers,” _Journal of Urban Economics_ , 64 (2008), 373–389. 

Rybczynski, Witold, _Last Harvest: How a Cornfield Became New Daleville_ (Scribner: New York, 2007). 

Saiz, Albert, “Room in the Kitchen for the Melting Pot: Immigration and Rental Prices,” _Review of Economics and Statistics_ , 85 (2003), 502–521. 

——, “Immigration and Housing Rents in American Cities,” _Journal of Urban Economics_ , 61 (2007), 345–371. 

- ——, “On Local Housing Supply Elasticity,” The Wharton School, University of Pennsylvania Working Paper SSRN No. 1193422, 2008. 

Saks, Raven, “Job Creation and Housing Construction: Constraints on Metropolitan Area Employment Growth,” _Journal of Urban Economics,_ 64 (2008), 178– 195. 

Stock, James H., and Motohiro Yogo, “Testing for Weak Instruments in Linear IV Regression,” in _Identification and Inference for Econometric Models: Essays in Honor of Thomas Rothenberg,_ D. W. K. Andrews and J. H. Stock, eds. (Cambridge, UK: Cambridge University Press, 2005). 

Swartz, David R., “Left Behind: The Evangelical Left and the Limits of Evangelical Politics: 1965–1988,” Ph.D. Dissertation, University of Notre Dame, 2008. 


