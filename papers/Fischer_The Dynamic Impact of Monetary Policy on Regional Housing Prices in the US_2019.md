---
title: Fischer_The Dynamic Impact of Monetary Policy on Regional Housing Prices in the US_2019
type: paper
source_pdf: raw/papers/Fischer_The Dynamic Impact of Monetary Policy on Regional Housing Prices in the US_2019.pdf
converted: 2026-08-18
---



**2021 V49 4: pp. 1039–1068 DOI: 10.1111/1540-6229.12274** 

REAL ESTATE ECONOMICS 



# **The Dynamic Impact of Monetary Policy on Regional Housing Prices in the United States** 

Manfred M. Fischer,* Florian Huber,** Michael Pfarrhofer** and Petra Staufer-Steinnocher* 

This article uses a factor-augmented vector autoregressive model to examine the impact of monetary policy shocks on housing prices. To simultaneously estimate the model parameters and unobserved factors, we rely on Bayesian estimation and inference. Policy shocks are identified using high-frequency surprises around policy announcements as an external instrument. Impulse response functions reveal differences in regional housing price responses, which in some cases are substantial. The heterogeneity in policy responses is found to be significantly related to local regulatory environments and housing supply elasticities. Moreover, housing prices responses tend to be similar within states and adjacent regions in neighboring states. 

## **Introduction** 

The housing market is one of the most important, but at the same time most volatile sectors of the economy, and hence of crucial concern for economic policy makers in general, and central banks in particular (Moulton and Wentland 2018). The notion of a national housing market disregards the fact that housing activities substantially vary across the United States. Moench and Ng (2011) emphasize that of the four regions defined by the United States Census Bureau, the West Region (including California, Nevada and Arizona) and the Northeast Region (including New York and Massachusetts) have, from a historical perspective, shown more active housing markets than the Midwest Region (including Illinois, Ohio and Minnesota) and the South 

> *Vienna University of Economics and Business, Welthandelsplatz 1, A-1020 Vienna or manfred.fischer@wu.ac.at, petra.staufer-steinnocher@wu.ac.at. 

> **Paris Lodron University of Salzburg, Moenchsberg 2A, A-5020 Salzburg or florian.huber@sbg.ac.at, michael.pfarrhofer@sbg.ac.at. 

_⃝_ C 2019 The Authors. Real Estate Economics published by Wiley Periodicals, Inc. on behalf of American Real Estate and Urban Economics Association 

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. 

**1040** Fischer et al. 

Region (including Florida, Texas and North Carolina). Another factor motivating regional disaggregation of the housing market is the volatility of regional housing markets relative to macroeconomic fluctuations (Fratantoni and Schuh 2003). 

The literature on the impact of monetary policy–related variables on housing is fairly limited, in particular at the regional level. Previous work generally relies on two competing approaches. The first uses structural models to analyze the relationship (see Iacoviello and Minetti 2003, Iacoviello and Neri 2010, Ungerer 2015, Bahadir and Gumus 2018). The major strength of this model-based approach is to provide a theoretically grounded answer to the question of interest. However, such models necessarily strongly impose a priori restrictions on crucial parameters. The second, evidence-based approach, focuses on empirics and relies less directly on economic theory. Microeconomic event studies, for example, provide answers using information on individual transactions to identify causal effects of monetary policy shocks in short time frames around monetary policy announcements (Moulton and Wentland 2018). Macroeconomists instead typically use vector autoregressive (VAR) models to measure the impact of monetary policy innovations and other macroeconomic shocks over longer time horizons, exploiting information contained in time series data. Examples include Fratantoni and Schuh (2003), Iacoviello (2005), Del Negro and Otrok (2007), Jarocinski and Smets (2008), Iacoviello and Minetti (2008), Vargas-Silva (2008a,b), Moench and Ng (2011) and Choudhry (2018). VAR models are dynamic models of time series that allow the data rather than the researcher, to specify the dynamic structure of the model, and provide a plausible assessment of macroeconomic variables to monetary policy shocks without the need of a fully specified structural model. 

This article lies in the tradition of the second approach, and differs from previous work in terms of both its focus and methodology. Like Fratantoni and Schuh (2003) and Del Negro and Otrok (2007), we focus on regional differences in response of housing prices. The coarseness of quarterly statelevel observations used in previous research, however, may conceal important variations that is key for researchers to identify cross-regional differences in policy responses. Hence, we use monthly observations on housing prices and provide a comprehensive coverage of the United States at the level of metroand micropolitan statistical areas,<sup>1</sup> to appropriately identify a monetary policy shock and the associated regional reactions. 

> 1For the definition of metropolitan and micropolitan statistical areas, see section “Regions and Data” along with Appendix A. 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1041** 

Similar to Vargas-Silva (2008a) and Moench and Ng (2011), we rely on a factor-augmented vector autoregressive (FAVAR) model to identify the impact of a monetary policy shock on housing prices, but use a fully Bayesian FAVAR model, based on a set of macroeconomic and financial variables, to explore regional housing price responses to a national monetary policy shock. In particular, we apply Markov chain Monte Carlo (MCMC) methods to estimate the model parameters and unobserved factors simultaneously, in contrast to previous approaches. Bayesian inference is advantageous because it directly addresses uncertainty surrounding latent factors and model parameters. Policy shocks are identified using high-frequency surprises around policy announcements as external instrument, where policy surprises are measured within a tight window of 30 minutes around the announcements by the Federal Reserve (see Kuttner 2001, G¨urkaynak, Sack and Swanson 2005, Gertler and Karadi 2015). 

The effects of monetary policy on housing prices in the regions are analyzed using the FAVAR model estimated over the period 1997:04 to 2012:06. Impulse response functions from the estimated model reveal a rich picture about how an expansionary monetary policy shock affects regional housing prices. Differences are evident, and in some cases, substantial. Regions within California, Florida and Nevada are found to be the most sensitive to monetary policy changes, exhibiting effects two times as large as the average response across the country. By contrast, some regions, for example, within Mississippi, Tennessee, Oklahoma and North Carolina are found to be the least responsive, showing no significant impact or even slightly negative responses. By linking the results to the housing supply elasticity literature (Gyourko, Saiz and Summers 2008, Saiz 2010, Howard and Liebersohn 2018, Vinson 2018), this article provides evidence that the measured cumulative cross-regional differential responses can partly be explained by housing supply elasticities and local regulatory environments. 

The remainder of the article is organized as follows. The next section presents the FAVAR model along with the Bayesian approach for estimation, and specifics about identification of monetary policy shocks. Section “Data and Model Implementation” describes the data and the sample of regions, and outlines the model specification. The results are presented in section “Econometric Results,” combined with a brief discussion about the question why housing prices in some regions are more sensitive to monetary policy shocks than others. The section concludes. 

**1042** Fischer et al. 

## **Methodology** 

## _The FAVAR Model_ 

The econometric approach we employ in this study is a FAVAR model, as introduced by Bernanke, Boivin and Eliasz (2005). In our implementation, we let **_H_** _t_ denote an _R_ × 1 vector of housing prices at time _t_ ( _t_ = 1 _, . . . , T_ ) for _R_ regions. The model postulates that regional housing prices depend on a number of latent factors, monetary and macroeconomic national aggregates and region-specific shocks. This relationship, henceforth termed the measurement equation, can be written as 



where **_F_** _t_ is an _S_ × 1 vector of latent (unobservable) factors, which capture comovement at the regional level. **_M_** _t_ is a _K_ × 1 vector of economic and monetary national aggregates that are treated as observable factors, and **_ϵ_** _t_ is an _R_ × 1 vector of normally distributed zero mean disturbances with an _R_ × _R_ variance–covariance matrix **_�_** _ϵ_ = diag( _σ_ 1<sup>2</sup><sup>_, . . . , σ_2</sup> _R_<sup>).Thesedisturbancesarise</sup> from measurement errors and special features that are specific to individual regional time series. **_�_**<sup>_F_</sup> is an _R_ × _S_ matrix of factor loadings, while **_�_**<sup>_M_</sup> denotes a coefficient matrix of dimension _R_ × _K_ . The number of latent factors is much smaller than the number of regions, that is, _S_ ≪ _R_ . Note that the diagonal structure of **_�_** _ϵ_ implies that any comovement between the elements in **_H_** _t_ and **_M_** _t_ stems exclusively from the presence of the latent factors. 

The evolution of the factors **_y_** _t_ = ( **_F_**<sup>′</sup> _t_<sup>_,_</sup><sup>**_M_**′</sup> _t_<sup>)′isgivenbythestateequation,</sup> governed by a VAR process of order _Q_ , 



with **_x_** _t_ = ( **_y_**<sup>′</sup> _t_ −1<sup>_, . . . ,_</sup><sup>**_y_**′</sup> _t_ − _Q_<sup>)′</sup> and the associated ( _S_ + _K_ ) × _Q_ ( _S_ + _K_ )- dimensional coefficient matrix **_A_** . Moreover, **_u_** _t_ is an ( _S_ + _K_ )-dimensional vector of normally distributed shocks, with zero mean and variance– covariance matrix **_�_** _u_ . 

The parameters **_�_**<sup>_F_</sup> , **_�_**<sup>_M_</sup> and **_A_** as well as the latent dynamic factors **_F_** _t_ are unknown and have to be estimated. To econometrically identify the model, we follow Bernanke, Boivin and Eliasz (2005) and assume that the upper _S_ × _S_ -dimensional submatrix of **_�_**<sup>_F_</sup> equals an identity matrix **_I_** _S_ while the first _S_ rows of **_�_**<sup>_M_</sup> are set equal to zero. This identification strategy implies that the first _S_ elements in **_H_** _t_ are effectively the factors plus noise. 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1043** 

## _A Bayesian Approach to Estimation_ 

The model described above is highly parameterized, containing more parameters as can reasonably be estimated with the data at hand. In this study, we use a Bayesian estimation approach to incorporate knowledge about parameter values via prior distributions. It is convenient to stack the free elements of the factor loadings in an _L_ -dimensional vector **_λ_** = vec[( **_�_**<sup>_F_</sup> _,_ **_�_**<sup>_M_</sup> )<sup>′</sup> ] with _L_ = _R_ ( _S_ + _K_ ), and the VAR coefficients in a _J_ -dimensional vector **_a_** = vec( **_A_** ) with _J_ = ( _S_ + _K_ )<sup>2</sup> _Q_ . 

_Prior distributions for the state equation._ For the VAR coefficients _a j_ ( _j_ = 1 _, . . . , J_ ) we impose the normal-gamma shrinkage prior proposed in Griffin and Brown (2010, 2017), and applied in a VAR framework by Huber and Feldkircher (2019), 



that is controlled by gamma priors on _τaj_<sup>2(</sup><sup>_j_= 1</sup><sup>_, . . . , J_)and</sup><sup>_ξa_,</sup> 



with hyperparameters _d_ 0, _d_ 1 and _ϑa_ , respectively. _ξa_ operates as global shrinkage parameter, and _τaj_<sup>2aslocalscalingparameter.Thishierarchicalprior</sup> shows two convenient features. First, _ξa_ applies to all _J_ elements in **_a_** . Higher values of _ξa_ yield stronger global shrinkage toward the origin whereas smaller values induce only little shrinkage. Second, the local scaling parameters _τaj_<sup>2placesufficientpriormassof</sup><sup>_a j_awayfromzerointhepresenceof</sup> strong overall shrinkage involved by large values for _ξa_ , in cases where the likelihood suggests nonzero values. 

The hyperparameter _ϑa_ in Equation (5) controls the excess kurtosis of the marginal prior, 



obtained after integrating over the local scales. Lower values of _ϑa_ generally place increasing mass on zero, but at the same time lead to heavy tails, allowing for large deviations of _a j_ from zero, if necessary. The hyperparameters _d_ 0 and _d_ 1 in Equation (4) are usually set to rather small values to induce heavy overall shrinkage. See Griffin and Brown (2010) for more details. 

For the variance–covariance matrix **_�_** _u_ we use an inverted Wishart prior, 



**1044** Fischer et al. 

with _v_ denoting prior degrees of freedom, while **_<u>�</u>_** is a prior scaling matrix of dimension ( _S_ + _K_ ) × ( _S_ + _K_ ). 

_Prior distributions for the observation equation._ For the factor loadings _λℓ_ ( _ℓ_ = 1 _, . . . , L_ ) we employ a normal-gamma prior similar to the one used for the VAR coefficients in **_a_** . The set-up follows Kastner (2018) with a single global shrinkage parameter _ξλ_ that applies to all free elements _λℓ_ in the factor loadings matrix. Specifically, we impose a hierarchical Gaussian prior on _λℓ_ that depends on gamma priors for _τλℓ_<sup>2(</sup><sup>_ℓ_= 1</sup><sup>_, . . . , L_)and</sup><sup>_ξλ_,</sup> 



The hyperparameters _c_ 0, _c_ 1 and _ϑλ_ control the tail behavior and overall degree of shrinkage of the prior. For the measurement error variances _σr_<sup>2(</sup><sup>_r_=</sup> 1 _, . . . , R_ ), we rely on a sequence of independent inverted gamma priors, 



where the hyperparameters _e_ 0 and _e_ 1 are typically set to small values to reduce prior influence on _σr_<sup>2.</sup> 

Estimation of the model parameters and the latent factors is based on the MCMC algorithm described in Appendix B. More specifically, we use Gibbs sampling to simulate a chain consisting of 20,000 draws, where we discard the first 10,000 draws as burn-in. It is worth noting that the MCMC algorithm shows fast mixing and satisfactory convergence properties. 

## _Identification of Monetary Policy Shocks_ 

The standard approach to identify monetary policy shocks in a VAR framework involves imposing a set of zero restrictions via a Cholesky identification scheme. This approach relies on the assumption that macroeconomic quantities in the system react to changes in the monetary policy instrument with a time lag. Timing restrictions on the impact of the policy indicator may be reasonable for the interactions between the funds rate and macroeconomic variables, but becomes problematic if financial variables are present in addition. Policy shifts not only influence financial quantities, but may also respond to them, directly or indirectly (Gertler and Karadi 2015). To circumvent the problem of simultaneity, we follow Gertler and Karadi (2015) and use highfrequency surprises as external instrument to identify monetary policy shocks. 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1045** 

The high-frequency variant of the external instruments identification approach employed in this article is based on surprises in the prices of three-monthsahead futures contracts of the federal funds rate that reflect expectations on interest rate movements further into the future, measured within a 30 minutes time window surrounding announcements by the Federal Open Market Committee (FOMC), the governing council of the Federal Reserve (Kuttner 2001, G¨urkaynak, Sack and Swanson 2005, Gertler and Karadi 2015). The tight time frame around these announcements is chosen to reduce the likelihood of other events affecting prices of the futures contracts. 

Financial markets internalize the behavior of the Federal Reserve (Fed) by anticipating changes in the policy instrument based on predicted movements in key macroeconomic quantities. For instance, facing a weakening economic outlook, federal funds rates futures would decline in advance of the policy announcement by the Fed. Depending on the specific monetary policy action conducted by the central bank, futures markets may either correctly predict the enacted policies or react to unexpected changes in the policy rate precisely around official announcements. G¨urkaynak, Sack and Swanson (2005) provide evidence that the adjustment of the prices of futures contracts happens almost instantaneously, in contrast to fully anticipated changes that do not cause observable reactions. A convenient by-product of this approach is that it also reflects Fed information shocks in the context of forward guidance. 

For illustrative purposes, the evolution of the effective federal funds rate over the observation period 1997:04 to 2012:06 is shown in Figure 1 (upper panel) along with the corresponding policy surprises around announcements (lower panel). The dashed red line refers to the zero line, while the light blue shaded vertical bars represent the recessions dated by the Business Cycle Dating Committee of the National Bureau of Economic Research. Large monetary policy surprises tend to occur in recessionary economic episodes, evidenced by unexpected innovations for both the period between 2001 and 2002, as well as during the Great Recession. Notice that decreases in the federal funds rate not necessarily reflect expansionary shocks. In June 2001, for instance, markets expected the Fed to further decrease the target rate, while the rate was decreased only slightly, translating into a contractionary monetary policy shock. The contrary is observable in the first half of 1997 or June 2006. Here, the Fed left the target rate unchanged while markets expected further increases, resulting in expansionary monetary policy shocks. 

To implement the approach, we follow Paul (2018) and use high-frequency surprises as a proxy for the monetary policy shock. This is achieved by 

**1046** Fischer et al. 

**Figure 1** ■ The federal funds rate and exogenous monetary policy surprises. [Color figure can be viewed at wileyonlinelibrary.com] 



<!-- Start of picture text -->
8<br>6<br>4<br>2<br>0<br>1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013<br>Date<br>10<br>0<br>−10<br>−20<br>−30<br>1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013<br>Date<br>f laddFtr seanreeu<br>)st<br>S( sniosisbsirparepu−<br><!-- End of picture text -->

_Notes_ : The dashed red line refers to the zero line, while the light blue shaded vertical bars denote the recessions dated by the Business Cycle Dating Committee of the National Bureau of Economic Research (www.nber.org). Surprises are measured within an half-hour window, starting 10 minutes before and ending 20 minutes after release of the FOMC policy statement. The data for monetary policy surprises between 1997:04 and 2012:06 come from Gertler and Karadi (2015). 

integrating the surprises into Equation (2) as an exogenous variable **_z_** _t_ , to yield 



Hereby, **_ζ_** is a _Q_ ( _S_ + _K_ )-dimensional vector of regression coefficients that collects the impulses of the shocks. Paul (2018) shows that under mild conditions, the contemporaneous relative impulse responses can be estimated consistently.<sup>2</sup> Note that the impact response of **_y_** _t_ to changes in **_z_** _t_ is given by **_ζ_** . Higher order responses are obtained recursively by exploiting the state space representation of the VAR model in Equation (2). 

> 2 Relative impulse responses are obtained by normalizing the absolute impulse responses, that is, the change in **_y_** _t_ + _h_ to a change in **_z_** _t_ , by the contemporaneous response of some element in **_y_** _t_ . 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1047** 

## **Data and Model Implementation** 

## _Regions and Data_ 

To explore regional differences in the impact of monetary policy on housing prices, we need to define our notion of regions. Throughout the article, we use _R_ = 417 regions, a subsample of the 917 core-based statistical areas (CBSAs).<sup>3</sup> These 417 regions include 263 metropolitan and 154 micropolitan statistical areas. They have been selected based on the availability of the data over time. For the list of regions in the sample, see Appendix A. 

Our data set consists of a panel of monthly time series ranging from 1997:04 to 2012:06. The _R_ × 1 vector of housing prices **_H_** _t_ is constructed using the Zillow Home Value Index.<sup>4</sup> A key advantage of this index is to provide a comprehensive coverage of CBSAs across the country, in contrast to the Federal Housing Finance Agency (FHFA) Index and the Standard & Poor’s Case-Shiller Index. The Zillow Home Value Index does not use a repeat sales methodology, but statistical models along with information from sales assessments to generate valuations for all homes (single family houses, town houses, apartments, condos and properties that are typically associated with the residential market) in any given region. These valuations are aggregated to determine the Zillow Home Value Index, measured in U.S. dollars. 

We include _K_ = 7 variables in the vector of observable national aggregates **_M_** _t_ : three economic variables, namely, housing investment (measured in terms of housing starts), the industrial production index and the consumer price index. The one-year government bond rate serves as policy indicator of the Fed. The advantage of using this longer rate rather than the federal funds 

> 3A CBSA is a U.S. geographic area—defined by the Office of Management and Budget—that consists of one or more counties anchored by an urban center of at least 10,000 people plus adjacent counties that are socioeconomically tied to the urban center. The term CBSA refers collectively to both metropolitan and micropolitan statistical areas. 

4The Zillow Home Value Index uses detailed information about hundreds of millions of real estate transactions across the United States to provide a comprehensive coverage of the CBSAs. The set of data we use in this study is available for download at https://www.zillow.com/research/data/. Note that no data are available for Maine and South Dakota because these states do not require mandatory disclosure for sale prices. CBSAs within Montana, Vermont and Wyoming had to be eliminated due to limited availability of time series data. Previous VAR/FAVAR-based studies on monetary transmission via house prices rely on different price indices. Fratantoni and Schuh (2003) use the Metropolitan Statistical Area (MSA)-level index from the Fannie Mae Repeat Transactions Database, Iacoviello (2005) the Freddie Mac House Price Index, Del Negro and Otrok (2007) the FHFA/OFHEO house prices indices and Jarocinski and Smets (2008) the S&P/Case-Shiller Index. 

**1048** Fischer et al. 

rate is that it incorporates—as Gertler and Karadi (2015) argue—measures of forward guidance and hence remains a valid measure of the monetary policy stance also in situations when the federal funds rate is constrained by the zero lower bound.<sup>5</sup> 

The FAVAR model developed in this article extends a standard macroeconomic autoregressive model with a set of three credit-spreads: the 10-year treasury yield minus the federal funds rate, the prime mortgage spread calculated over 10-year government bond yields and the Gilchrist and Zakrajˇsek (2012) excess bond premium. The excess bond premium may roughly be seen as the component of the spread between an index of yields on corporate fixed income securities and a similar maturity government bond rate that is left after removing the component due to default risk (Gertler and Karadi 2015). Gilchrist and Zakrajˇsek (2012) show that this variable provides a convenient summary of additional information that may be relevant to economic activity. 

The economic variables capture housing, price and output movements. The mortgage spread is relevant to the cost of housing finance, and the excess bond premium to the cost of long-term credit in the business sector, while the term spread measures expectations on short-term interest rates (Gertler and Karadi 2015). All observable national aggregates are taken from the FRED database (McCracken and Ng 2016), with the exception of the excess bond premium and the mortgage spread that have been obtained from the data set provided in Gertler and Karadi (2015). All data series are seasonally adjusted, if applicable, and transformed to be approximately stationary. 

## _Model Implementation_ 

For implementation of the FAVAR, we have to specify the lag order _Q_ of the VAR process and the number of latent factors, _S_ . As is standard in the literature, we pick _Q_ = 2 lags of the endogenous variables. To decide on the number of factors, we use the deviance information criterion (Spiegelhalter _et al._ 2002) where the full data likelihood is obtained by running the Kalman filter and integrating out the latent states. This procedure yields _S_ = 1, a choice that is also consistent with traditional criteria, for instance, the Bayesian information criterion or the Kaiser criterion, for selecting the number of factors. 

A brief word on hyperparameter selection for the prior setup is in order. We specify _ϑa_ = _ϑλ_ = 0 _._ 1, a choice that yields strong shrinkage but, at the same 

> 5To support this view, we estimated the model using the federal funds rate as policy indicator for a robustness check. The results—available upon request—suggest similar responses compared to the one-year government bond rate. 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1049** 

time, leads to heavy tails in the underlying marginal prior. Recent literature (see, for example, Huber and Feldkircher 2019) integrates out _ϑa, ϑλ_ and finds that, for U.S. data, the posterior is centered on values between 0.10 and 0.15. The hyperparameters on the global shrinkage parameters are set equal to _c_ 0 = _c_ 1 = _d_ 0 = _d_ 1 = 0 _._ 01, a choice that is consistent with heavy shrinkage toward the origin representing a standard in the literature (Griffin and Brown 2010). The prior on **_�_** _u_ is specified to be weakly informative, _i.e._ , _ν_ = _S_ + _K_ + 1 and **_<u>�</u>_** = 10<sup>−2</sup> **_I_** _S_ + _K_ . Similarly for the inverted gamma prior on _σr_<sup>2(</sup><sup>_r_= 1</sup><sup>_, . . . , R_)weset</sup><sup>_e_0=</sup><sup>_e_1= 0</sup><sup>_._01torendertheprioronly</sup> weakly influential. 

## **Econometric Results** 

## _The Dynamic Factor and Its Loadings_ 

We briefly consider the estimated latent factor and its loadings, with two aims in mind: first, to provide a rough intuition on how the latent factor captures co-movement in regional house price variations, and second, to indicate the relative importance of individual regions shaping the evolution of the common factor. The posterior mean of the negative latent factor (in solid red) shown in Figure 2 provides evidence that the common factor co-moves with the average growth rate of housing prices (in solid blue, calculated using the arithmetic mean of the individual regional housing prices) nearly perfectly. The figure illustrates that during the 2001 recession, housing price declines have been mild, while being substantial during the Great Recession, with large variations 

**Figure 2** ■ Comovement of the negative latent dynamic factor and national housing prices over time. [Color figure can be viewed at wileyonlinelibrary.com] 



_Notes_ : The solid red line denotes the posterior mean of the negative latent factor, _i.e._ , − _Ft_ , the solid blue line the national housing prices, calculated as mean of the individual regions. The dashed black line refers to the zero line, while the light blue shaded vertical bars represent the recessions dated by the Business Cycle Dating Committee of the National Bureau of Economic Research (www.nber.org). Sample period: 1997:04 to 2012:06. Vertical axis: growth rates. Front axis: months. 

**1050** Fischer et al. 

**Figure 3** ■ Region-specific factor loadings. [Color figure can be viewed at wileyonlinelibrary.com] 



_Notes_ : Visualization is based on a classification scheme with equal-interval breaks. The number of regions is allocated to the classes in squared brackets. Thinner lines denote the boundaries of the regions, while thicker lines represent U.S. state boundaries. Results are based on 10,000 posterior draws. Sample period: 1997:04 to 2012:06. For the list of regions see Appendix A. 

across space. It is worth noting that home prices fell the most during the late 2000s in regions with the largest declines in economic activity (Beraja _et al._ 2017). 

While Figure 2 provides intuition on the shape of the latent housing factor, the question on how individual regions are linked to it still needs to be addressed. For this purpose, Figure 3 reports the posterior mean of the region-specific factor loadings in the form of a geographic map in which thinner lines denote the boundaries of the regions, while thicker lines signify U.S. state boundaries. Visualization is based on a classification scheme with equal-interval breaks. We see that the great majority of regions exhibit negative loadings, and only 23 regions show positive values. Eighty regions have zero loadings or loadings where the 16th and 84th credible sets (68% posterior coverage) of the respective posterior distributions include zero. The pattern of factor loadings, evidenced by the map, indicates that the latent factor is largely 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1051** 

driven by regions located in California, Arizona and Florida. Regions in the rest of the country, with loadings being either small in absolute terms or not significantly different from zero, tend to play only a minor role in shaping national housing prices. 

## _Impulse Responses of Macroeconomic Quantities_ 

Impulse response functions represent the standard way to summarize the dynamic impact of policy shocks. We first consider the dynamic evolution of the endogenous variables included in **_M_** _t_ in response to a monetary policy shock to illustrate that the results of the model are consistent with established findings in the literature. An expansionary monetary policy shock is modeled by taking the one-year government bond rate as the relevant policy indicator, rather than the federal funds rate that is commonly used in the literature. Gertler and Karadi (2015) show that the one-year bond rate has a stronger impact on market interests than the funds rate does, based on the assertion that forward guidance is more adequately reflected in the longer maturity yield. Normalization is achieved by assuming that a monetary policy shock yields a five basis points decrease in the policy indicator. 

The impulse response functions of all the endogenous variables to the monetary policy shock are presented in Figure 4. All plots include the median response (in blue) for 72 months after impact along with 68% posterior coverage intervals reflecting posterior uncertainty. An unanticipated decrease in the government bond rate by five basis points causes a significant increase in real activity, with industrial production, housing investment and consumer prices all increasing over the next months after the impact. From a quantitative standpoint, the effects of the monetary shock on industrial production and consumer prices are considerably larger than the impact on housing investment, although uncertainty surrounding the size of impacts is large and posterior coverage intervals include zero during the first months after impact. Housing investment shows a reaction similar in shape to real activity measured in terms of the industrial production index, suggesting a positive relationship between expansionary monetary policy and housing investment at the national level. 

Turning to the responses of financial market indicators, it should be noted that the one-year government bond rate falls by five basis points on impact by construction, then increases significantly before it turns nonsignificant after about nine months. The term spread reacts adversely on impact, and we find significant deviations from zero that die out after about 16 months. This result points toward an imperfect pass-through of monetary policy on long-term rates, implying that long-term yields display a weaker decline as compared 

**1052** Fischer et al. 

**Figure 4** ■ Impulse responses of macroeconomic fundamentals to a monetary policy shock. [Color figure can be viewed at wileyonlinelibrary.com] 







_Notes_ : The solid blue line denotes the median response, the dashed red line the zero line, and the shaded bands (in light blue) the 68% posterior coverage interval. Results are based on 10,000 posterior draws. Sample period: 1997:04 to 2012:06. Vertical axis: percentage changes for indices and housing investment; otherwise percentage points. Front axis: months after impact. 

to short-term rates. The prime mortgage spread does not show a significant effect on impact, while responses between 10 and 20 months ahead indicate a slightly negative overall reaction to expansionary monetary policy. Consistent with Gilchrist and Zakrajˇsek (2012), one implication of this finding is that movements in key short-term interest rates tend to impact credit markets, with mortgage spreads showing a tendency to decline. The responses of the excess bond premium almost perfectly mirror the reaction of the mortgage spread. The effects, however, are much larger from a quantitative point of view. 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1053** 

To sum up, the results obtained by the impulse response analysis provide empirical support that monetary policy shocks, identified by using highfrequency surprises around policy announcements as external instrument, generate impulse responses of the endogenous variables that are consistent with economic theory and the findings of previous empirical studies.<sup>6</sup> 

## _Impulse Responses of Housing Prices_ 

Figure 5 displays the impulse response function of the latent factor over 72 months after impact to an expansionary monetary policy shock. The latent factor reacts positively after the shock, but the posterior coverage interval includes zero for the time horizon considered. Nevertheless, sufficient posterior mass is shifted away from zero reflecting positive reactions. This is consistent with economic theory, suggesting decreases in the cost of financing a home purchase via expanding the availability of credit, thereby increasing the demand for housing. As a result, real housing prices tend to increase. 

**Figure 5** ■ Reaction of the negative latent factor, following a monetary policy shock. [Color figure can be viewed at wileyonlinelibrary.com] 



_Notes_ : The solid blue line denotes the median response, the dashed red line the zero line and the shaded bands (in light blue) the 68% posterior coverage interval. Results are based on 10,000 posterior draws. Vertical axis: percentage points. Front axis: months after impact. 

> 6To allay potential concerns of the policy rate reaching the zero lower bound, we conducted various robustness checks (results are available upon request). Using a shadow rate to capture unconventional monetary policy actions leaves the results qualitatively unchanged. The same holds true when using the federal funds rate rather than the one-year government bond rate as policy indicator. 

**1054** Fischer et al. 

**Figure 6** ■ Long-run responses of regional housing prices to a monetary policy shock, i.e., cumulative 72 months responses. [Color figure can be viewed at wileyonlinelibrary.com] 



_Notes_ : Visualization is based on a classification scheme that generates breaks in standard deviation measures ( _SD_ = 0 _._ 61) above or below the mean of 0.71. The number of regions is allocated to the classes in squared brackets. The responses based on 10,000 posterior draws have been accumulated. Thinner lines denote the boundaries of the regions, while thicker lines represent U.S. state boundaries. Sample period: 1997:04 to 2012:06. For the list of regions, see Appendix A. 

While for reasons of space, we do not report the housing price responses of all the 417 regions, we summarize the long-run regional house price responses ( _i.e._ , cumulative 72 months responses, expressed in percentage points) in the form of a geographic map with a classification scheme that generates class breaks in standard deviation measures ( _SD_ = 0.61) above and below the mean of 0.71 (see Figure 6).<sup>7</sup> Again thinner lines denote the boundaries of the regions and thicker lines those of the U.S. states. Some few regions show no significant impact or even negative responses. In more than 91% of the regions, however, the cumulative response of housing prices is positive. 

Monetary policy shocks affect regions asymmetrically. Differences in policy responses are evident, and in some cases, substantial. The largest 

7The results are robust to an alternative identification scheme based on sign-restrictions (see Appendix C). Concerns on the validity of the identification scheme using external instruments, that may come from the period where interest rates nearly reached zero, are thus alleviated. 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1055** 

response among regions (Las Vegas–Henderson–Paradise, Nevada) exceeds the smallest (Tahlequah, Oklahoma) by 3.2 percentage points. Regions within California, Florida and Nevada—commonly referred to as Sand States—are noticeably more responsive to monetary policy changes. The top 10 most responsive regions are dominated by six Californian regions: Riverside–San Bernadino–Ontario, Madera, Merced, Clearlake, Modesto and Bakersfield. The first two slots in the ranking, however, are occupied by Las Vegas– Henderson–Paradise and Fernley, a micropolitan region (both within Nevada). Port St. Lucie, Clewiston and Key West (all Florida) round out the top 10, and bring the coastal eastern regions into picture. 

By contrast, certain regions of the country are much less sensitive to monetary policy shocks (±0.25 standard deviation from zero). These regions are not concentrated in only a few states or areas. Rather, they span 14 states and 24 metro- and micropolitan regions. Given the narrowness of our definition, this emphasizes the point that less responsive regions, in terms of reactions to monetary policy shocks, are spread throughout much of the country. Clarksville (Tennessee–Kentucky), Tulsa, Enid and Bartlesville (Oklahoma), as well as Hickory–Lenoir–Morgenton and Fayetteville (North Carolina), and Baton Rouge (Louisiana) are found to be the least responsive. Note that 5% of the regions do not show significant results, while 3.6% (including, _e.g._ , Salt Lake City, Utah) exhibit negative responses. 

Metropolitan regions like Chicago–Naperville–Elgin (Illinois–Indiana– Wisconsin), Boston–Cambridge–Newton (Massachusetts–New Hampshire), Portland–Vancouver–Willsborough (Oregon–Washington), Savannah (Georgia) and San Jose–Sunnyvale–Santa Clara (California) respond to monetary policy changes in ways that closely mirror the average dynamic response across the United States (±0.25 standard deviation). 

Figure 6 reveals substantial heterogeneity in the magnitude of the dynamic responses, but also indicates that regional responses tend to be similar within states and adjacent neighboring states. This spatial autocorrelation phenomenon becomes particularly evident in the case of Californian regions and is most likely due to the importance of new house construction industries, along with the spatial influence the Californian housing market has on regions in neighboring states, especially Nevada and Arizona. 

## _Explanation for the Differential Housing Price Responses_ 

Housing price responses vary substantially over space, with size and modest sign differences among the regions, as evidenced by Figure 6. This raises the question why housing prices in some regions are more responsive to monetary 

**1056** Fischer et al. 

policy shocks than in others. To address this issue, we link our results to the housing supply elasticity literature (Gyourko, Saiz and Summers 2008, Saiz 2010, Howard and Liebersohn 2018), more specifically, to local land use regulation as captured by the Wharton Residential Land Use Regulatory Index (WRLURI), and a measure of housing supply elasticity developed by Howard and Liebersohn (2018). 

The WRLURI created by Gyourko, Saiz and Summers (2008) is an index comprised of 11 subindices that summarize information on different aspects of the local regulatory environment. The index calculated for our regions shows that much heterogeneity in land use regulatory environments exists across the regions.<sup>8</sup> The two Michigan metropolitan regions, Ann Arbor and Jackson, and the Michigan micropolitan region, Adrian, represent the most heavily regulated markets, with WRLURI scores at least 2.9 standard deviation above the national mean of −0.18. The next most heavily regulated regions, according to the index, are Seattle–Tacoma–Bellevue (Washington), San Diego–Carlsbad and San Francisco–Oakland–Hayward (both within California), being about one standard deviation above the mean. Dallas–Fort Worth–Arlington (Texas) is a typical housing market near the mean in terms of land use regulatory environments. Bartlesville (Oklahoma), Lewiston (Idaho– Washington), Toledo (Ohio) and Tahlequah (Oklahoma) are examples for the least regulated regions, having WRLURI scores that are at least one standard deviation below the mean. All these examples emphasize that local land use regulation is neither uniformly high nor uniform across the country. 

Figure 7 presents the estimated local land use regulation in form of a geographic map with a classification scheme that generates class breaks in standard deviation (0.82) measures above and below the mean of −0.18 (left panel), while the comparison with the corresponding cumulative impulse responses of housing prices is shown in the right panel. The figure clearly suggests that there exists a positive relationship between the sensitivity of housing price reactions and land use regulation. Regions characterized by tight regulations also tend to feature strong reactions of local housing markets. This can be attributed to the positive relationship between regulatory measures and housing prices that has previously been identified in the literature (see, for instance, Ihlanfeldt 2007, Glaeser and Ward 2009). We conjecture that this relationship directly translates into increased responsiveness of housing prices, leading to stronger reactions to national monetary policy shocks. 

> 8We calculated WRLURI scores for the regions by taking a population-weighted average for all counties within a region. Note that the WRLURI does not provide full coverage for the United States, and systematically undercovers micropolitan regions. Hence, scores are missing for 15% of the regions in our sample. 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1057** 

**Figure 7** ■ Estimated local land use regulation, captured by WRLURI, and comparison with the housing price responses. [Color figure can be viewed at wileyonlinelibrary.com] 



<!-- Start of picture text -->
2<br>1<br>0<br>−2 −1 0 1 2<br>Regulatory index<br>less than −1.0 SD −0.5 to 0.5 SD greater or equal to 1.0 SD<br>−1.0 to −0.5 SD 0.5 to 1.0 SD not available<br>Cumulative impulse response<br><!-- End of picture text -->

_Notes_ : The left-hand panel presents the estimated local land use regulation (visualized in form of a geographic map based on a classification scheme with equal-interval breaks around the mean of −0.18), while the right panel shows the correlation between cumulative impulse responses of housing prices and the corresponding WRLURI scores (the circles represent the regions, with their size indicating population density). Thinner lines denote the boundaries of the regions, while thicker lines represent U.S. state boundaries. The solid red line in the right-hand panel denotes the correlation. For the list of regions see Appendix A. 

In the next step, we assess how housing supply elasticity is linked to housing price responses in Figure 8. We use Howard and Liebersohn’s housing supply elasticity measure for commuting zones to construct elasticities for the regions. The elasticity measure estimates the effect of a change in housing units on housing prices, projecting this relationship onto three measures associated with land availability: the WRLURI index, population density and the coastal status (Howard and Liebersohn 2018).<sup>9</sup> Estimated housing supply elasticities for the regions reveal that San Francisco–Oakland– Hayward, San Diego–Carlsbad, Santa Rosa, Napa and Vallejo–Fairfield (all within California) belong to the top 10 most inelastic regions, with elasticities below 0.72. The three Michigan regions Ann Arbor, Adrian and Jackson along with Philadelphia–Camden–Wilmington (Pennsylvania–New Jersey–Delaware–Maryland) and Trenton (New Jersey) complete the top 10 list. Housing supply is estimated to be quite elastic (3.73, with a standard deviation of 2.78) for the average region, represented by Salt Lake City (Utah). By contrast, Las Vegas–Henderson–Paradise (Nevada) and Santa Fe 

> 9To classify coastal regions, we used NOAA’s (National Oceanic and Atmospheric Administration) definition of coastal counties. Any region that contains a coastal county was coded as coastal. 

**1058** Fischer et al. 

**Figure 8** ■ Estimated elasticities and comparison with the housing price responses. [Color figure can be viewed at wileyonlinelibrary.com] 



<!-- Start of picture text -->
2<br>1<br>0<br>0 2 4 6 8<br>Supply elasticity<br>less than −1.0 SD −0.5 to 0.5 SD greater or equal to 1.0 SD<br>−1.0 to −0.5 SD 0.5 to 1.0 SD not available<br>Cumulative impulse response<br><!-- End of picture text -->

_Notes_ : The left-hand panel presents the estimated housing supply elasticities (visualized in form of a geographic map based on a classification scheme with equal-interval breaks around the mean of 3.73), while the right panel shows the correlation between cumulative impulse responses of housing prices and the corresponding elasticities (the circles represent the regions, with their size indicating population density). Thinner lines denote the boundaries of the regions, while thicker lines represent U.S. state boundaries. The solid red line in the right-hand panel denotes the correlation. For the list of regions see Appendix A. 

(New Mexico) stand out as prominent examples with most elastic housing supply, with at least one standard deviation above the national mean. 

On the right in Figure 8, one observes a negative relationship between housing supply elasticities and price responses. In our specific example, we find that expansionary monetary policy directly translates into cheaper credit, leading to upward movements in housing demand. This increase in housing demand in face of a rather steep supply curve for housing yields a strong price reaction. This finding corroborates and extends the results in Glaesera, Gyourko and Saiz (2008), who report a negative relationship between supply elasticities and movements in property prices, especially in the context of excessive increases in housing prices. These results indicate higher effectiveness of monetary policy to influence housing prices by the central bank in regions characterized by low levels of supply elasticities. 

## **Closing Remarks** 

This article uses a Bayesian FAVAR model to examine the impact of monetary policy shocks on housing prices across the United States. Bayesian inference is advantageous because it directly addresses uncertainty surrounding latent factors and model parameters. Monetary policy shocks are identified making 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1059** 

use of high-frequency surprises around policy announcements as external instrument. Impulse response functions reveal that monetary policy shocks affect regions asymmetrically. There is substantial heterogeneity in the magnitude of the regional housing price responses. The largest response exceeds the smallest by 3.2 percentage points. Regions within California, Florida and Nevada are noticeably more responsive than others. By contrast, the least responsive regions are spread throughout much of the country. 

This heterogeneity in responses may be due to varying sensitivity of housing to interest rates across space, and regional differences in housing markets such as different local regulatory environments and supply elasticities. The article links the results to the housing supply elasticity literature and provides evidence that the variation in housing responses across space can be explained partly by different supply elasticities and regulatory environments. 

Finally, it is worth noting that our analysis is confined to a linear setting, implying the underlying transmission mechanism to be constant over time. This assumption simplifies the analysis, but may be overly simplistic in turbulent economic times such as the collapse of the housing market around the Great Recession. Hence, an extension of the linear setting to allow for nonlinearities—in the spirit of Huber and Fischer (2018)—might be a promising avenue for future research. 

_The authors thank the Vienna University of Economics and Business for research support and gratefully acknowledge funding by the Austrian National Bank, Jubilaeumsfond Grant No. 17650. Our specific gratitude goes to Greg Howard (University of Illinois) for providing commuting zone-based data for calculating the regional housing supply elasticities and WRLURI scores. This article is a substantially revised version of a paper circulated under the title “The dynamic impact of monetary policy on regional housing prices in the US: Evidence based on factor-augmented vector autoregressions,” Working Paper Series in Regional Science No. 2018-1, WU Vienna University of Economics and Business, Vienna._ 

## **References** 

Arias J., J. Rubio-Ramirez and D. Waggoner. 2014. Inference Based on SVAR Identified with Sign and Zero Restrictions: Theory and Applications. Working Paper Series No. 1, Federal Reserve Bank of Atlanta. 

Bahadir B. and I. Gumus. 2018. Transmission of Household and Business Credit Shocks in Emerging Markets: The Role of Real Estate. _Real Estate Economics_ . First published online, https://doi.org/10.1111/1540-6229.12273 

Beraja M., A. Fuster, E. Hurst and J. Vavra. 2017. Regional Heterogeneity and Monetary Policy. Staff Report No. 731, Federal Reserve Bank of New York. 

**1060** Fischer et al. 

Bernanke B.S., J. Boivin and P. Eliasz. 2005. Measuring the Effects of Monetary Policy: A Factor-Augmented Vector Autoregressive (FAVAR) Approach. _The Quarterly Journal of Economics_ 120(1): 387–422. 

Carter C.K. and R. Kohn. 1994. On Gibbs Sampling for State Space Models. _Biometrika_ 81(3): 541–553. 

Choudhry T. 2018. Economic Policy Uncertainty and House Prices: Evidence from Geographical Regions of England and Wales. _Real Estate Economics_ . First published online, https://doi.org/10.1111/1540-6229.12266 

Dedola L. and S. Neri. 2007. What Does a Technology Shock Do? A VAR Analysis with Model-Based Sign Restrictions. _Journal of Monetary Economics_ 54(2): 512–549. Del Negro M. and C. Otrok. 2007. 99 Luftballons: Monetary Policy and the House Price Boom across U.S. States. _Journal of Monetary Economics_ 54(7): 1962–1985. 

Fratantoni M. and S. Schuh. 2003. Monetary Policy, Housing, and Heterogeneous Regional Markets. _Journal of Money, Credit, and Banking_ 34(4): 557–589. 

Fr¨uhwirth-Schnatter S. 1994. Data Augmentation and Dynamic Linear Models. _Journal of Time Series Analysis_ 15(2): 183–202. 

George E.I., D. Sun and S. Ni. 2008. Bayesian Stochastic Search for VAR Model Restrictions. _Journal of Econometrics_ 142(1): 553–580. 

Gertler M. and P. Karadi. 2015. Monetary Policy Surprises, Credit Costs, and Economic Activity. _American Economic Journal: Macroeconomics_ 7(1): 44–76. 

Gilchrist S. and E. Zakrajˇsek. 2012. Credit Spreads and Business Cycle Fluctuations. _The American Economic Review_ 102(4): 1692–1720. 

Glaeser E.L. and B.A. Ward. 2009. The Causes and Consequences of Land Use Regulation: Evidence from Greater Boston. _Journal of Urban Economics_ 65(3): 265– 278. 

———, J. Gyourko and A. Saiz. 2008. Housing Supply and Housing Bubbles. _Journal of Urban Economics_ 64(2): 198–217. 

Griffin J.E. and P.J. Brown. 2010. Inference with Normal-Gamma Prior Distributions in Regression Problems. _Bayesian Analysis_ 5(1): 171–188. 

———. 2017. Hierarchical Shrinkage Priors for Regression Models. _Bayesian Analysis_ 12(1): 135–159. 

G¨urkaynak R.S., B. Sack and E. Swanson. 2005. The Sensitivity of Long-Term Interest Rates to Economic News: Evidence and Implications for Macroeconomic Models. _The American Economic Review_ 95(1): 425–436. 

Gyourko J., A. Saiz and A. Summers. 2008. A New Measure of the Local Regulatory Environment for Housing Markets: The Wharton Residential Land Use Regulatory Index. _Urban Studies_ 45(3): 693–729. 

Howard G. and J. Liebersohn. 2018. The Geography Channel of House Price Appreciation. Fisher College of Business Working Paper No. 2018(17). 

Huber F. and M. Feldkircher. 2019. Adaptive Shrinkage in Bayesian Vector Autoregressive Models. _Journal of Business & Economic Statistics_ 37(1): 27–39. 

——— and M.M. Fischer. 2018. A Markov Switching Factor-Augmented VAR Model for Analyzing US Business Cycles and Monetary Policy. _Oxford Bulletin of Economics and Statistics_ 80(3): 575–604. 

Iacoviello M. 2005. House Prices, Borrowing Constraints, and Monetary Policy in the Business Cycle. _The American Economic Review_ 95(3): 739–764. 

——— and R. Minetti. 2003. Financial Liberalization and the Sensitivity of House Prices to Monetary Policy: Theory and Evidence. _The Manchester School_ 71(1): 20– 34. 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1061** 

——— and R. Minetti. 2008. The Credit Channel of Monetary Policy: Evidence from the Housing Market. _Journal of Macroeconomics_ 30(1): 69–96. 

——— and S. Neri. 2010. Housing Market Spillovers: Evidence from an Estimated DSGE Model. _American Economic Journal: Macroeconomics_ 2(2): 125–164. Ihlanfeldt K.R. 2007. The Effect of Land Use Regulation on Housing and Land Prices. _Journal of Urban Economics_ 61(3): 420–435. 

Jarocinski M. and F. Smets. 2008. House Prices and the Stance of Monetary Policy. ECB Working Paper 891, European Central Bank, Frankfurt. 

Kastner G. 2018. Sparse Bayesian Time-Varying Covariance Estimation in Many Dimensions. _Journal of Econometrics_ . First published online, https://doi.org/10.1016/ j.jeconom.2018.11.007 

Kuttner K.N. 2001. Monetary Policy Surprises and Interest Rates: Evidence from the Fed Funds Futures Market. _Journal of Monetary Economics_ 47(3): 523–544. McCracken M.W. and S. Ng. 2016. FRED-MD: A Monthly Database for Macroeconomic Research. _Journal of Business & Economic Statistics_ 34(4): 574–589. 

Moench E. and S. Ng. 2011. A Hierarchical Factor Analysis of U.S. Housing Market Dynamics. _The Econometrics Journal_ 14(1), C1–C24. 

Moulton J.G. and S.A. Wentland. 2018. Monetary Policy and the Housing Market: Evidence from National Microdata. Paper presented at the 2018-SF Fed-UCLA Conference on Housing Financial Markets and Monetary Policy. 

Paul P. 2018. The Time-Varying Effect of Monetary Policy on Asset Prices. Working Paper 2017-09, Federal Reserve Bank of San Francisco. 

Rubio-Ramirez J.F., D.F. Waggoner and T. Zha. 2010. Structural Vector Autoregressions: Theory of Identification and Algorithms for Inference. _The Review of Economic Studies_ 77(2): 665–696. 

Saiz A. 2010. The Geographic Determinants of Housing Supply. _The Quarterly Journal of Economics_ 125(3): 1253–1296. 

Spiegelhalter D.J., N.G. Best, B.P. Carlin and A. van der Linde. 2002. Bayesian Measures of Model Complexity and Fit. _Journal of the Royal Statistical Society: Series B_ 64(4): 583–639. 

Uhlig H. 2005. What Are the Effects of Monetary Policy on Output? Results from an Agnostic Identification Procedure. _Journal of Monetary Economics_ 52(2): 381–419. 

Ungerer C. 2015. Monetary Policy, Hot Housing Markets and Leverage. Finance and Economics Discussion Series 2015-048, Divisions of Research & Statistics and Monetary Affairs, Federal Reserve Board, Washington, D.C. 

Vargas-Silva C. 2008a. The Effect of Monetary Policy on Housing: A FactorAugmented Vector Autoregression (FAVAR) Approach. _Applied Economics Letters_ 15(10): 749–752. 

———. 2008b. Monetary Policy and the US Housing Market: A VAR Analysis Imposing Sign Restrictions. _Journal of Macroeconomics_ 30(3): 977–990. 

Vinson P. 2018. House Prices and Consumption in the United States. _Real Estate Economics_ . First published online, https://doi.org/10.1111/1540-6229.12271 

## **Appendix A: Regions Used in the Study** 

Regions in this study are defined as CBSAs that—by definition of the United States Office of Management and Budget—are based on the concept of a core area of at least 10,000 population, plus adjacent counties having at least 25% of employed residents of the county who work in the core area. CBSAs 

**1062** Fischer et al. 

**Table A1** ■ The list of metropolitan statistical areas used. 

|State (Census<br>Bureau Region)|Region|
|---|---|
|Alabama (South)|Birmingham–Hoover, Daphne–Fairhope–Foley, Mobile,<br>Montgomery, Tuscaloosa|
|Arizona (West)|Flagstaff, Lake Havasu City–Kingman,<br>Phoenix–Mesa–Scottsdale, Prescott, Sierra Vista–Douglas,<br>Tucson, Yuma|
|Arkansas (South)|Fayetteville–Springdale–Rogers*, Fort Smith*, Hot<br>Springs, Jonesboro, Little Rock–North Little<br>Rock–Conway|
|California (West)|Bakersfeld, Chico, El Centro, Fresno, Hanford–Corcoran,<br>Los Angeles–Long Beach–Anaheim, Madera, Merced,<br>Modesto, Napa, Oxnard–Thousand Oaks–Ventura,<br>Redding, Riverside–San Bernardino–Ontario,<br>Sacramento–Roseville–Arden–Arcade, Salinas, San<br>Diego–Carlsbad, San Francisco–Oakland–Hayward, San<br>Jose–Sunnyvale–Santa Clara, San Luis Obispo–Paso<br>Robles–Arroyo Grande, Santa Cruz–Watsonville, Santa<br>Maria–Santa Barbara, Santa Rosa, Stockton–Lodi,<br>Vallejo–Fairfeld, Visalia–Porterville, Yuba City|
|Colorado (West)|Boulder, Colorado Springs, Denver–Aurora-Lakewood,<br>Fort Collins, Grand Junction, Greeley, Pueblo|
|Connecticut|Bridgeport–Stamford–Norwalk, Hartford–West|
|(Northeast)|Hartford–East Hartford, New Haven–Milford,<br>Norwich–New London|
|Delaware (South)|Dover|
|District of Columbia<br>(South)|Washington–Arlington–Alexandria*|
|Florida (South)|Cape Coral–Fort Myers, Crestview–Fort Walton<br>Beach–Destin, Deltona–Daytona Beach–Ormond Beach,<br>Gainesville, Homosassa Springs, Jacksonville,<br>Lakeland–Winter Haven, Miami–Fort Lauderdale–West<br>Palm Beach, Naples–Immokalee-Marco Island, North<br>Port–Sarasota–Bradenton, Ocala,<br>Orlando–Kissimmee–Sanford, Palm|
||Bay–Melbourne–Titusville, Panama City, Pensacola–Ferry<br>Pass–Brent, Port St. Lucie, Punta Gorda, Sebastian–Vero<br>Beach, Sebring, Tallahassee, Tampa–St.<br>|
||Petersburg–Clearwater, The Villages|
|Georgia (South)|Albany, Athens–Clarke County, Atlanta–Sandy<br>Springs–Roswell, Augusta–Richmond County*,<br>Columbus*, Dalton, Gainesville, Hinesville, Macon,<br>Savannah, Valdosta, Warner Robins|
|Hawaii (West)|Kahului–Wailuku–Lahaina, Urban Honolulu|
|Idaho (West)|Boise City, Idaho Falls, Lewiston*|



The Dynamic Impact of Monetary Policy on Regional Housing Prices **1063** 

**Table A1** ■ Continued. 

|State (Census<br>Bureau Region)|Region|
|---|---|
|Illinois (Midwest)|Bloomington, Chicago–Naperville–Elgin*,<br>Davenport–Moline–Rock Island*, Kankakee, Springfeld|
|Indiana (Midwest)|Bloomington, Elkhart–Goshen, Evansville*, Fort Wayne,<br>Lafayette–West Lafayette, Muncie, South<br>Bend–Mishawaka*, Terre Haute|
|Iowa (Midwest)|Des Moines–West Des Moines|
|Kansas (Midwest)|Lawrence|
|Kentucky (South)|Lexington-Fayette, Louisville–Jefferson County*|
|Louisiana (South)|Alexandria, Baton Rouge, Houma–Thibodaux, Lafayette,<br>Lake Charles|
|Maryland (South)|Baltimore–Columbia–Towson, California–Lexington Park,<br>Cumberland*, Hagerstown–Martinsburg*, Salisbury*|
|Massachusetts|Barnstable Town, Boston–Cambridge–Newton*, Pittsfeld,|
|(Northeast)|Springfeld, Worcester*|
|Michigan (Midwest)|Ann Arbor, Battle Creek, Bay City, Grand<br>Rapids–Wyoming, Jackson, Lansing–East Lansing,<br>Midland, Monroe, Muskegon, Saginaw|
|Minnesota (Midwest)|Mankato–North Mankato, Minneapolis-St.<br>Paul–Bloomington*, Rochester|
|Mississippi (South)|Hattiesburg, Jackson|
|Missouri (Midwest)|Columbia, Joplin, Springfeld, St. Louis*|
|Nebraska (Midwest)|Grand Island, Lincoln, Omaha–Council Bluffs*|
|Nevada (West)|Las Vegas–Henderson–Paradise, Reno|
|New Hampshire|Manchester–Nashua|
|(Northeast)||
|New Jersey<br>|Ocean City, Trenton, Vineland-Bridgeton|
|(Northeast)||
|New Mexico (West)|Albuquerque, Las Cruces, Santa Fe|
|New York|Albany–Schenectady–Troy, Binghamton, Elmira, Glens|
|(Northeast)|Falls, Ithaca, Kingston, New York–Newark–Jersey City*,<br>Rochester, Syracuse, Watertown–Fort Drum|
|North Carolina|Asheville, Burlington, Charlotte-Concord–Gastonia*,|
|(South)|Durham–Chapel Hill, Fayetteville, Greensboro–High<br>Point, Hickory–Lenoir–Morganton, Raleigh, Rocky<br>Mount, Wilmington, Winston–Salem|
|North Dakota|Fargo*|
|(Midwest)||
|Ohio (Midwest)|Akron, Canton–Massillon, Cincinnati*, Cleveland–Elyria,<br>Columbus, Dayton, Lima, Springfeld, Toledo,<br>Youngstown–Warren–Boardman*|
|Oklahoma (South)|Oklahoma City, Tulsa|



**1064** Fischer et al. 

**Table A1** ■ Continued. 

|State (Census<br>Bureau Region)|Region|
|---|---|
|Oregon (West)|Albany, Bend–Redmond, Corvallis, Eugene, Grants Pass,<br>Medford, Portland–Vancouver–Hillsboro*,<br>Salem|
|Pennsylvania|Allentown–Bethlehem-Easton*, Altoona, Erie,|
|(Northeast)|Harrisburg–Carlisle, Lancaster,<br>Philadelphia–Camden–Wilmington*, Pittsburgh, Reading,<br>Scranton–Wilkes–Barre–Hazleton, State College,<br>York–Hanover|
|Rhode Island|Providence–Warwick*|
|(Northeast)||
|South Carolina|Columbia, Florence, Greenville–Anderson–Mauldin,|
|(South)|Hilton Head Island–Bluffton–Beaufort, Myrtle<br>|
||Beach–Conway–North Myrtle Beach*, Spartanburg|
|Tennessee (South)|Chattanooga*, Clarksville*, Cleveland, Jackson, Johnson<br>City, Kingsport–Bristol–Bristol*, Knoxville,<br>Nashville–Davidson–Murfreesboro–Franklin|
|Texas (South)|Amarillo, Brownsville–Harlingen, College Station-Bryan,<br>Dallas–Fort Worth–Arlington, El Paso, Killeen–Temple,<br>Laredo, Midland, Texarkana*|
|Utah (West)<br>|Ogden–Clearfeld, Provo–Orem, Salt Lake City, St. George<br>|
|Virginia (South)|Charlottesville, Harrisonburg, Richmond, Roanoke,<br>Staunton–Waynesboro, Virginia Beach–Norfolk–Newport<br>News*, Winchester*|
|Washington (West)|Bellingham, Kennewick–Richland, Longview,<br>Olympia–Tumwater, Seattle–Tacoma–Bellevue,<br>Spokane–Spokane Valley, Walla Walla, Yakima|
|West Virginia<br>(South)|Charleston|
|Wisconsin (Midwest)|Appleton, Eau Claire, Fond du Lac, Janesville–Beloit, La<br>Crosse–Onalaska*, Madison, Oshkosh–Neenah,<br>Racine|



_Note:_ Asterisks indicate that the metropolitan area lies mainly in the indicated state, but parts of it cross state borders. 

may be categorized as being either metropolitan or micropolitan. The 917 CBSAs include 381 metropolitan statistical areas, which have an urban core population of at least 50,000, and 536 micropolitan statistical areas, which have an urban core population of at least 10,000 but less than 50,000. In this study, we use 263 metropolitan and 154 micropolitan statistical areas, due to limited availability of data. These 417 regions represent contiguous states (excluding Maine, Montana, South Dakota, Vermont and Wyoming) plus the District of Columbia and Hawaii. 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1065** 

**Table A2** ■ The list of micropolitan statistical areas. 

|State (Census<br>Bureau Region)|Region|
|---|---|
|Arizona (West)|Nogales, Payson, Safford|
|Arkansas (South)|Batesville, Harrison, Paragould, Russellville, Searcy|
|California (West)|Clearlake, Eureka–Arcata–Fortuna, Red Bluff,<br>Susanville, Truckee–Grass Valley|
|Colorado (West)<br>|Durango, Glenwood Springs, Montrose, Sterling<br>|
|Connecticut<br>|Torrington|
|(Northeast)||
|Florida (South)|Clewiston, Key West, Lake City, Okeechobee,<br>Palatka|
|Georgia (South)|Bainbridge, Calhoun, Cedartown, Dublin, Jesup,<br>Moultrie, St. Marys, Thomaston, Tifton, Vidalia,<br>|
||Waycross|
|Hawaii (West)|Hilo|
|Idaho (West)|Burley|
|Illinois (Midwest)<br>|Effngham, Jacksonville<br>|
|Indiana (Midwest)|Angola, Auburn, Bedford, Connersville,<br>Crawfordsville, Decatur, Frankfort, Greensburg,<br>Huntington, Jasper, Kendallville, Logansport,<br>Madison, Marion, New Castle, North Vernon, Peru,<br>Plymouth, Richmond, Seymour, Vincennes,<br>Wabash, Warsaw, Washington|
|Kansas (Midwest)<br>|Garden City<br>|
|Kentucky (South)<br>|Danville, Murray<br>|
|Louisiana (South)|Opelousas|
|Maryland (South)|Cambridge, Easton<br>|
|Massachusetts<br>|Greenfeld Town, Vineyard Haven|
|(Northeast)||
|Michigan|Adrian, Hillsdale, Holland, Ionia, Ludington,|
|(Midwest)|Owosso|
|Minnesota|Owatonna, Willmar, Winona|
|(Midwest)||
|Mississippi (South)|Cleveland, Columbus, Corinth, Grenada, Laurel,<br>Oxford, Picayune, Tupelo, Vicksburg|
|Missouri (Midwest)|Mexico|
|Nebraska|North Platte|
|(Midwest)||
|Nevada (West)|Elko, Fernley, Gardnerville Ranchos|
|New Hampshire|Concord, Keene, Laconia|
|(Northeast)||
|New York<br>|Amsterdam, Batavia, Corning, Cortland,<br>|
|(Northeast)|Gloversville, Hudson, Olean, Oneonta, Plattsburgh,<br>Seneca Falls|



**1066** Fischer et al. 

**Table A2** ■ Continued. 

|State (Census<br>Bureau Region)|Region|
|---|---|
|North Carolina<br>(South)|Albemarle, Morehead City, Sanford, Wilson|
|Ohio (Midwest)|Ashtabula, Coshocton, Defance, Findlay, Jackson,<br>New Philadelphia–Dover, Portsmouth, Sandusky,<br>Urbana, Wooster|
|Oklahoma (South)|Ardmore, Bartlesville, Durant, Enid, Marion,<br>McAlester, Tahlequah|
|Oregon (West)|Coos Bay, Hermiston–Pendleton, Klamath Falls,<br>Ontario*, Roseburg, The Dalles|
|Pennsylvania<br>(Northeast)|Indiana, Lock Haven, Oil City, Pottsville|
|South Carolina<br>(South)|Orangeburg|
|Tennessee (South)|Cookeville, Lawrenceburg, Lewisburg, Martin,<br>Paris, Sevierville, Shelbyville,<br>Tullahoma–Manchester|
|Virginia (South)|Danville, Martinsville|
|Washington (West)|Oak Harbor, Port Angeles, Shelton|
|Wisconsin<br>(Midwest)|Baraboo, Marinette*, Whitewater-Elkhorn|



_Note_ : Asterisks indicate that the micropolitan area lies mainly in the indicated state, but parts of it cross state borders. 

## **Appendix B: The MCMC Algorithm** 

We estimate the model by running an MCMC algorithm. The full conditional posterior distributions are available in closed form implying that we can apply Gibbs sampling to obtain draws from the joint posterior distribution. More specifically, our MCMC algorithm involves the following steps: 

- (i) Simulate the VAR coefficients _a j_ ( _j_ = 1 _, . . . , J_ ) conditional on the factors and remaining model parameters from a multivariate Gaussian distribution that takes a standard form (see, for instance, George, Sun and Ni 2008, for further information). 

- (ii) Simulate the latent factors **_F_** _t_ by using forward filtering backward sampling (Carter and Kohn 1994, Fr¨uhwirth-Schnatter 1994). 

- (iii) The error variance–covariance matrix **_�_** _u_ is simulated from an inverted Wishart posterior distribution with degrees of freedom equal to _ν_ ¯ = _v_ + _T_ and scaling matrix equal to **_P_** =<sup>�</sup> _t_<sup>_T_</sup> =1<sup>(</sup><sup>**_y_**</sup><sup>_t_−</sup> **_Ax_** _t_ )<sup>′</sup> ( **_y_** _t_ − **_Ax_** _t_ ) + **_<u>�</u>_** <u>.</u> 

The Dynamic Impact of Monetary Policy on Regional Housing Prices **1067** 

- (iv) Simulate the factor loadings _λℓ_ ( _ℓ_ = 1 _, . . . , L_ ) from Gaussian posteriors (conditioned on the remaining parameters and the latent factors) by running a sequence of ( _R_ − _S_ ) unrelated regression models. 

- (v) The measurement error variances _σr_<sup>2for</sup><sup>_r_=</sup><sup>_S_+ 1</sup><sup>_, . . . , R_are</sup> simulated independently from an inverse Gamma distribution _σr_<sup>2|</sup><sup>_�_∼</sup><sup>_G_−1(</sup><sup>_αr, βr_)with</sup><sup>_αr_=</sup><sup><u>1</u></sup> 2<sup>_T_+</sup><sup>_e_0and</sup><sup>_βr_=</sup><sup><u>1</u></sup> 2 � _tT_ =1<sup>(</sup><sup>_Hrt_−</sup> **_�_** _r_<sup>_F_</sup> •<sup>**_F_**</sup><sup>_t_−</sup><sup>**_�_**</sup> _r_<sup>_M_</sup> •<sup>**_M_**</sup><sup>_t_)2 +</sup><sup>_e_1.Thenotation</sup><sup>**_�_**</sup> _r_<sup>_F_</sup> •<sup>indicatesthatthe</sup><sup>_r_th</sup> row of the matrix concerned is selected, and _�_ stands for conditioning on the remaining parameters and the data. 

- (vi) Simulate _τaj_<sup>2(</sup><sup>_j_= 1</sup><sup>_, . . . , J_) from a generalized inverted Gaussian</sup> distributed posterior distribution with 



- (vii) Draw _ξa_ from a Gamma distributed posterior given by 



- (viii) Simulate the posterior of _τλℓ_<sup>2(</sup><sup>_ℓ_= 1</sup><sup>_, . . . , L_)fromageneralized</sup> inverted Gaussian distribution, 



- (ix) Finally, the global shrinkage parameter _ξλ_ associated with the prior on the factor loadings is simulated from a Gamma distribution, 



Steps described above are iterated for 20,000 cycles, where we discard the first 10,000 draws as burn-in. 

## **Appendix C: Robustness Check—Comparing with an Identification Scheme Imposing Sign Restrictions** 

To assess the sensitivity of our results with respect to identification of the monetary policy shock, we use an alternative strategy based on contemporaneous sign restrictions (see Uhlig 2005, Dedola and Neri 2007). Technical implementation is achieved by adopting the algorithm proposed in Arias, Rubio-Ramirez and Waggoner (2014) that collapses to the procedure outlined in Rubio-Ramirez, Waggoner and Zha (2010) in the absence of zero restrictions. For each iteration of the MCMC algorithm, we draw a rotation matrix 

**1068** Fischer et al. 

and assess whether the following set of sign restrictions is satisfied. Consistent with economic common sense, output (measured in terms of the industrial production index), housing investment (measured in terms of housing starts) and consumer prices (measured in terms of the consumer price index) are bound to increase on impact. Moreover, we assume that the term-spread also widens on impact. Finally, consistent with the normalization adopted when using an external instrument, we assume that the one-year yield declines. If this is the case, we keep the rotation matrix and store the associated structural coefficients, while if the sign restrictions are not met, we reject the draw and repeat the procedure. 

The results are displayed in form of a geographic map with a classification scheme that generates class breaks in standard deviation measures above and below the mean, see Figure C1. A comparison with Figure 6 provides evidence of the robustness of our results. 

**Figure C1** ■ Robustness check: Cumulative responses of regional housing prices to a monetary policy shock identified using sign restrictions. [Color figure can be viewed at wileyonlinelibrary.com] 



_Notes_ : Visualization is based on a classification scheme that generates breaks in standard deviation measures. The number of regions is allocated to the classes in squared brackets. The responses based on 10,000 posterior draws have been accumulated. Thinner lines denote the boundaries of the regions, while thicker lines represent U.S. state boundaries. Sample period: 1997:04–2012:06. For the list of regions see Appendix A. 

