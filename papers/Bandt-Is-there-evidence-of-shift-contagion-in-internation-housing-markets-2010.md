---
title: DIRECTION GÉNÉRALE DES ÉTUDES ET DES RELATIONS INTERNATIONALES
type: paper
source_pdf: raw/papers/Bandt_Is there evidence of shift-contagion in internation housing markets_2010.pdf
converted: 2026-07-26
---

# DOCUMENT 

# DE TRAVAIL 

# N° 295 

**IS THERE EVIDENCE OF SHIFT-CONTAGION IN INTERNATIONAL HOUSING MARKETS?** Olivier de Bandt and Sheheryar Malik October 2010 



DIRECTION GÉNÉRALE DES ÉTUDES ET DES RELATIONS INTERNATIONALES 

##### DIRECTION GÉNÉRALE DES ÉTUDES ET DES RELATIONS INTERNATIONALES 

**IS THERE EVIDENCE OF SHIFT-CONTAGION IN INTERNATIONAL HOUSING MARKETS?** Olivier de Bandt and Sheheryar Malik October 2010 

Les Documents de travail reflètent les idées personnelles de leurs auteurs et n'expriment pas nécessairement la position de la Banque de France. Ce document est disponible sur le site internet de la Banque de France « <u>www.banque-france.fr</u> ». 

Working Papers reflect the opinions of the authors and do not necessarily express the views of the Banque de France. This document is available on the Banque de France Website “www.banque-france.fr”. 

## Is there Evidence of Shift-Contagion in International Housing Markets?<sup>�</sup> 

Olivier de Bandt<sup>y</sup> , Sheheryar Malik<sup>z</sup> 

> �The opinions expressed are not necessarily those of the Banque de France or the Eurosystem.We are grateful to F. Canova, J. Hamilton and F. Ferroni, as well as participants in the French Economic Association (AFSE) Annual Conference and ISF 2010 Conference for helpful comments. 

> yBanque de France, E-mail olivier.debandt@banque-france.fr 

> zBanque de France and University of Warwick, E-mail sheheryar.malik@banque-france.fr 

1 

###### Abstract 

The paper attempts to provide, for housing markets, evidence of “shift-contagion” at the international level, i. e. regime shifts in the transmission of asset prices during crisis periods. The focus is in particular on UK and Spain. We use a Markov Switching FAVAR framework and regime-dependent impulse response functions. The ‘Crisis’ regime which we identify endogenously is shown to also correspond to an exogenously determined index of frequency of …nancial crises in OECD countries, which peaked in the early 1990s and in the more recent Subprime crisis. Furthermore, we …nd that the response of domestic house price to a shock to a common (global) house price factor during a ‘Crisis’regime is relatively more ampli…ed than in a ‘Normal’(more tranquil) regime. Less compelling evidence is found for France. 

Key words : contagion, housing market, regime shifts, FAVAR model JEL : R31,G15,C32 

###### Résumé 

L’article cherche à mettre en évidence, sur les marchés immobiliers, des cas de "shift-contagion" au niveau international, c’est à dire de changements de régime dans la transmission des prix d’actifs durant les périodes de crise. L’accent est mis en particulier sur le Royaume Uni et l’Espagne. Nous avons recours à un modèle de type FAVAR avec des changements de régime de type Markovien et des fonctions de réponse qui di¤èrent selon les régimes. Nous montrons que le régime de ’crise’, que nous identi…ons de façon endogène, est très proche d’un indicateur exogène mesurant la fréquence des crises …nancières dans les pays de l’OCDE et qui présente notamment un pic au début des années 90 et plus récemment lors de la crise des subprimes. De plus, nous trouvons que la réponse des prix immobiliers nationaux à un choc sur le facteur immobilier commun (mondial) est relativement plus marqué en régime de ’crise’que dans le régime ’normal’(ou régime de tranquilité). Les resultats sur la France sont moins clairs 

Mots-clés : contagion, marché immobilier, changement de régime, modèle FAVAR Classi…cation JEL : R31,G15,C32. 

2 

### 1 Introduction 

The simultaneity of adjustments in housing markets during the 2007-2008 Subprime crisis, that originated in the US before hitting the UK and Spain as well as other countries have triggered new questions about possible vulnerability to contagion effects given international shocks to the domestic real economies.. The objective of the paper is to show that housing markets in the UK and Spain are characterized by a change in the transmission mechanism of international house price shocks during periods of crisis, resulting in an ampli…cation in the response of domestic house price dynamics; a situation that can be identi…ed as contagion. 

Indeed, many papers have since the late 1980s considered the possibility of contagion in asset markets, starting from the 1987 stock market crash and then episodes such as the Mexican, Asian and Russian crises in the 1990s. Several de…nitions of contagion have been suggested, largely stressing the signi…cant increase in cross-market linkages after a shock to a single country or ‘group of countries’(Forbes and Rigobon (2002)). Subsequently, Gravelle et al. (2006) formalized the concept of so-called “shift-contagion”focusing on cases of increased co-movement between asset returns driven by changes in the structural transmission of shocks rather than just a change in the size of the shock. Both de…nitions encapsulate the idea that contagion is different from the simple transmission of shocks across interdependent markets which would also occur in normal or tranquil periods.<sup>1</sup> 

The investigation of contagion is important in terms of policy implications insofar it allows us to identify changes in the transmission mechanisms of shocks. This is particularly relevant given the most recent crisis which has been characterized by shocks of substantially large magnitude. If markets are contagious, economic policy should focus on structural reforms ensuring the smooth functioning of domestic markets (competition policy, policies to address the e¤ects of asymmetric information, etc.) in order to limit the ampli…cation of shocks between housing markets. In contrast, the dynamics of interdependent markets will depend on the degree of correlation of fundamentals, for which economic policy may be less potent in a globalized world. The paper by Gravelle et al. (2006) is the closest in spirit to our approach in terms of considering time-varying transmission mechanisms in a multivariate Markov switching environment. Speci…cally, our approach is to employ the framework of Markov Switching VAR (MS-VAR) models with the aim of …rstly identifying periods of contagion and then, and equally as importantly, studying the evolution of regime-dependent impulse responses. Derivation of the latter provides us with a dual assessment of the 

> 1The distinction between interdependence and contagion is, however, sometimes di¢ cult to delineate, and another de…nition of contagion would include the analysis of the dynamic process of transmission of shocks. In that alternative approach, used by de Bandt, Barhoumi and Bruneau (2010), and coined as the “pandemic”view of contagion, contagion is associated with the generalisation of shocks, with a process of globalization of local shocks and its repercussion at the local level, with a double process “from local to global”and “global to local”. In contrast, the approach we follow in the current paper investigates changes over time of the transmission channels. 

3 

susceptibility of a country to contagion and impact thereof, thus proving an invaluable tool for obtaining policy-relevant predictions. 

There are di¤erent theoretical models analyzing international contagion in banking and …nancial markets (Claessen and Forbes, 2001; Pavlova and Rigobon, 2008). The majority of these usually revolve around the revision of expectations based on a signal (fundamental- or sunspot-based) given some form of market incompleteness, liquidity constraint or frictions. In housing markets, loan contracts may be viewed as a source of frictions, as households may default on their debt. An essential question is therefore to what extent contagion in housing markets is likely to occur in the same way as in …nancial markets. Arguably housing markets are di¤erent from stock and bond markets in terms of being to some extent, more local, less standardized, and facing higher transaction costs and associated with rigidities, partly associated with higher public intervention.<sup>2</sup> However, they share common features with …nancial markets. 

First, there is evidence of international exposure to foreign housing markets, as evidenced by the share of foreign investors in domestic markets that may arbitrage across markets.<sup>3</sup> Second, housing wealth usually represents approximately half of total wealth (see Arrondel and Savignac (2009), de Bandt et al, 2010b). In addition, securitization has broadened the number and types of investors, which go beyond the direct bene…ciaries of housing services. The diversity of actors is housing markets, is also observed in other markets that behave like asset markets. For instance the oil market, where arbitrageurs increase the liquidity of the market and a¤ect prices, without any physical delivery of the good. It remains that adjustments in housing markets are likely to take place over a more prolonged period since price quotation do not take place in quasi-continuous time as in …nancial markets.<sup>4</sup> Indeed, house price indices themselves are generally available with a substantial delay.<sup>5</sup> This is also the consequence of the absence of organized housing markets with a lack of harmonized indices across countries. One should acknowledge, however, the compilation of data 

> 2We refer the reader to the abundant literature on the heterogeneity of housing markets in the US, with, amongst others, Goodman and Thibodeau (2008). 

> 3Non residents represented around 4% of the number of housing transactions in France in 2004, concentrating on higher value units (Fauvet, 2007; Friggit, 2007). In Spain, non residents accounted for 9% of transactions in 2006, but 4,2% in 2009 (source: Estadistica Registral Immobiliara). Foreign direct investment in residential construction in Spain amounted to 0.5% of GDP in average over the 1995-2009 period, with a peak at 0.9% in 2003. The equivalent …gures fror France are 0.2% of GDP over the 1990-2009 period, with a maximum of 0.6% in 2007. UK stands a bit higher at 1.4%, but including also non residential real estate. These …gures are small with respect to overall GDP but they have a substantial impact on the housing market as the share of housing investment in GDP was 5% in France and the UK and 6% in Spain in average over that period. 

> 4See DiPasquale et Wheaton (1994) and the numerous references thereafter on rigidities of price adjustements in housing markets. 

> 5Prolonged adjustment, notwithstanding the low frequency nature of the housing market data relative to high frequency …nancial data, reinforces the utility of employing impulse response analysis in our context. 

4 

on house prices that has been undertaken by the BIS, the OECD and is underway by Eurostat. We partially rely on the data produced by these institutions. 

Another relevant issue is whether contagion needs to be considered on a countryby-country basis, looking at pairwise comparisons, or from a more global perspective. In the case of housing markets, one can conclude the absence of a leading role of a given market but also noting that the US may have a somewhat prominent role. The local nature of housing markets, as mentioned before, argue in favour of considering possible contagion from global prices to local prices, rather than looking at bivariate causal links for two di¤erent countries as has been the convention in most of the literature on stocks, bonds or currency prices. In this respect we suggest considering world aggregates or global indices of house prices. In our case this is achieved by deriving a common house price factor as a measure of global house prices dynamics. Therefore our approach may be thought of as factor-augmented, structural MS-VAR model. In essence this approach bridges the gap between multivariate Markov switching with elements of the now fairly well established structural FAVAR literature pioneered by Stock and Watson (2005) and Bernanke, Eliasz and Boivin (2006).<sup>6</sup> In short, for each country we consider bivariate VAR models constituted of :(i) global house price factor and (ii) the growth of domestic real house prices. We allow the parameters of the VAR to display regime switching behavior and investigate if and how the impact of the global factor on the latter changes over time; or more appropriately, within different regimes. To the best of our knowledge such a methodology has not previously been considered for investigating contagion in international housing markets. 

The result of the paper is to provide evidence in favour of “shift-contagion” in the case of Spain and the UK. Preceding the impulse response analysis we identify, on statistical and economically intuitive grounds, two di¤erent regimes labelled as ‘Normal’and ‘Crisis’. The timing/spans of Crisis regimes (endogenously determined by the model) corresponds adequately to periods usually documented in the literature as …nancial crises; the de…nition of which goes beyond encompassing just business cycles phases. It is found that in the latter regime, the impact of innovations to the global factor on domestic real house prices is signi…cantly more pronounced. We view this as evidence of contagion, in a similar vein to the signi…cant increase in the slope coe¢ cient investigated in much of the earlier contagion literature. However, contagion is not expected to materialize in all countries and in the case of France, we …nd less compelling evidence in favour of the identi…cation of a Crisis regime. 

The remainder of this paper is as follows. In section 2 we review the literature in order to focus in on the de…nition of contagion we use in this analysis and also introduce the data we employ. In section 3 we describe the methodology, section 4 presents and discusses the results for UK and Spain. The case of France is described in section 5 and section 6 concludes. 

> 6We mention below one exception, namely Kaminsky and Reinhart (2001) that use Principal Component Analysis on di¤erent asset classes. 

5 

### 2 De…ning Contagion 

We survey the de…nitions of contagion available in the economic literature before introducing the data that are available for investigating contagion for house prices. 

#### 2.1 Empirical Studies of Contagion 

There have recently been a large number of studies dealing with the empirical modelling and/or identi…cation of contagion,<sup>7</sup> the vast majority of which have revolved around global …nancial markets. Depending on the de…nition of contagion accepted, these studies can be classi…ed broadly in several categories. We brie‡y document some earlier studies below. 

The ‘unanticipated shock’models of contagion consider transmission of unanticipated shocks between countries and the impact thereof in increasing (or decreasing) the covariance between variables in crisis and non-crisis periods. In order to test for the presence of contagion the framework developed was that of a factor structure by Dungey, Fry, Gonzalez-Hermosillo and Martin (2005). 

Another strand of the literature provides a test of contagion by assessing whether there is a signi…cant increase in correlation between two variables during crisis periods. King and Wadhwani (1990), Baig and Goldfajn (1998) and Loretan and English (2000) were amongst the …rst to use correlation analysis in testing for contagion. Forbes and Rigobon (2002) note, comparing the correlations between asset returns, that estimates will tend to be biased upwards given that crisis periods are characterized by higher volatility and correlations are a positive function of volatility; thus providing evidence of spurious contagion. The author provide a framework using an adjusted (unconditional) correlation in order to circumvent this bias. In the pairwise correlation tests that they perform it is assumed that the source country from which contagion spreads is exogenous (i.e. there is no feedback). Corsetti, Pericoli and Sbracis (2002) extend this framework and cast it as a factor structure. The correlation-based approach is extended to a multivariate setting in Rigobon (2003 a,b) and also Dungey et al. (2005) which consider the change in the reduced-form covariance matrix (of the underlying structural model) between tranquil and crisis periods. This framework requires the prior speci…cation of crisis periods, mis-speci…cation of which will lead to inconsistent estimates. 

There have also been strategies looking at modelling contagion within a probabilistic, binary choice setting. Basically, in these models the underlying continuous variable takes a value of unity if a certain threshold is reached, i.e. indicating that the market is in crisis. Contagion is captured by including a dummy variable as a covariate which takes a value of unity if the other market under consideration is in crisis. This approach has been adopted by Eichengreen et al. (1996), Kruger et al. (1998) and Stone and Weeks (2001). 

> 7See Dugney et al. (2005) for an excellent survey. 

6 

A number of other papers focus on modelling contagion as being represented by how the transmission mechanism between asset markets di¤ers in crises versus tranquil times; more speci…cally allowing for the transmission process to be nonlinearly di¤erent. These are borne out of the observation that contagion in the presence of interdependencies cannot be distinguished in pure correlation-based tests of contagion. In the approach proposed by Favero and Giavazzi (2002), the author estimate a VAR model to control for interdependencies between asset returns across countries. They identify outliers via inspection of the residuals which they interpret as unanticipated shocks which may be transmitted across markets; thus resulting in contagion. Essentially, the residual outliers enable the identi…cation of crisis period for which dummies are inserted into a linear simultaneous structural equation system. Tests of contagion involve testing the signi…cance of these dummies in explaining other asset returns.<sup>8</sup> Pesaran and Pick (2007) advanced a canonical model of contagion based on a two-equation non-linear model with endogenous dummy variables and essentially extends a threshold autoregressive (TAR) type model (see Tong (1990)) within a system framework. The endogenous nature of dummy variables (indicator functions) lead to potentially inconsistent parameter estimates and a thus a caveat of this variety of models. 

Authors such as Chou et al. (1994) and Hamao et al. (1990) have looked at testing contagion within a multivariate ARCH/GARCH framework. In noting that these variety of models do not adequately capture the asymmetric nature of volatility and cross-market correlations during crises, a further approach employed in the literature is that of using Markov-switching models (see Hamilton, 1990; Kim and Nelson, 1998; Krolzig, 1998 and 2001). This approach, both univariate and multivariate versions, has become well established in the literature on business cycle modelling; speci…cally with regards to identifying turning points in economic activity, which occur through a shift in the means or some what equivalently, the intercepts. In modelling contagion this approach has been followed inter alia by Bekaert and Harvey (1995)<sup>9</sup> , Fratzsher (2003), Billio et al. (2005), Gravelle et al. (2006). The hidden state variable follows a Markov Chain and enables the endogenous identi…cation of di¤erent regimes (i.e. crisis and tranquil) from the data sample and this circumvents the issue of regime windows being exogenously assigned ex post. These approaches can also be seen as ones of ‘identi…cation through heteroscedasticity’(see Rigobon,2003a) given the models specify the timing of movement from low volatility to high volatility regimes; which is, to re-iterate, endogenously estimated. These papers have, like other papers empirically investigating contagion, sought to look at …nancial markets and testing increases in co-movements between them during periods of crises. Our work is closely associated with that literature. 

> 8This approach is ex post in nature given that it requires the a priori identi…cation of crisis periods and is similar to what one would encounter in Rigobon (2003 a,b) and Dungey et al. (2005). 

> 9They employ the term time-varying market integration as opposed to contagion in their work. The asset allocation implications of which are considered in Ang and Bekaert (1999). 

7 

Alternatively, Kaminsky and Reinhart (2001) employ principal component analysis (PCA) as a means by which to study the co-movement between di¤erent asset classes among a set of markets. The approach of PCA has been employed in contexts such as dimension reduction, i.e. by summarizing the information in large data sets into just a few factors. The underlying idea is that the higher the degree of co-movement in the original series, the fewer the number of principal components (factors) required to explain the large proportion of variance in the original series.<sup>10</sup> 

On the basis of the empirical literature and in light of the fact that there is no single universally accepted de…nition of contagion, we shall build upon the de…nition provided by Forbes and Rigobon (1999, 2002) in which contagion is de…ned as a signi…cant increase in cross-market linkages after a shock to one country or ‘group of countries’- and Gravelle et al (2006)’s extension to “shift contagion”. 

#### 2.2 Data 

We use data on house prices constructed by de Bandt, Barhoumi and Bruneau (2010). The data are issued by national statistical institutes or private sources and are consistent with the data assembled by the OECD. Countries included are Australia, Canada, Finland, France, Germany, Ireland, Italy, Japan, Netherlands, Norway, New Zealand, Spain, United Kingdom, United States, hence a total of 14 countries. It turned out that they are very close to the OECD for the period starting in 1980. The period of analysis is 1980Q1 to 2008Q4, where the data are the most reliable. Series are seasonally adjusted. Based on the real house price data (de‡ated by the harmonized consumption price index<sup>11</sup> ) for 14 countries, we construct a common real house factor using the Stock and Watson’s (1999) approach, after demeaning and standardizing the quarterly growth rates on nominal prices. The factor ‡uctuates within the range of the growth rates of domestic real house prices (see Figure A0 in the Appendix). However, in order to avoid spurious correlation, the common factor that we used in estimations for a given country is computed from a database that excludes that country. For instance the factor for the UK is computed with all house (real) prices, except the UK, hence a total of 13 countries. In what follows, this is labelled as FACxUK and accordingly FACxESP for Spain and FACxFRA for France. The corresponding series on real domestic house price growth are labelled HPIUK, HPIESP and HPIFR (see Figures A1a, b and c in the Appendix). It turns out that the factors computed out of 13 countries are not very di¤erent from the factor computed on the 14 countries. Another piece of data that we use for ex-post evaluation of our endogenously determined Crisis periods is an index of the global intensity of 

> 10Essentially, if the original series were perfectly collinear (i.e. identical), then the …rst prinicpal component would explain 100% of the variation in the original series. On the other extreme, if the all series were orthogonal to on another then we would require as many principal components as there are original series; i.e. no common factors exist. 11 Source : OECD 

8 

the …nancial crisis, also used by de Bandt, Barhoumi and Bruneau (2010). It is constructed from Reinhart and Rogo¤ (2008) on OECD countries and compiled by the International Monetary Fund.<sup>12</sup> The indicator tallies the number of countries facing a …nancial crisis at a given point in time and dividing by the number of countries, one gets the proportion of countries in crisis. The indicator is updated at the end of the observation period and it is assumed that from 2008Q2 to 2008Q4, all countries in the sample were experiencing a …nancial crisis. 

### 3 Methodology 

In order to describe the econometric methodology adopted in this paper we follow closely the treatment in Ehrmann, Ellison and Valla (2003). In (1) below we represent a general Markov-Switching Vector Autoregression (MS-VAR), with K endogenous variables Yt, t = 1; :::; T; which are functions of intercepts �i, autoregressive terms with lag order p and residuals Biut:The parameters of the system can move between M di¤erent regimes. 



Here ut is a K-dimensional vector of normally distributed fundamental disturbances uncorrelated at all leads and lags; the variance of each fundamental disturbance is normalized to unity. But given that fundamental disturbances are premultiplied by a regime-dependent matrix Bi which imply that the variance-covariance matrix of the �i will also be regime-dependent. It follows that, 



The state st is assumed to be governed by a hidden M -state Markov-chain. The probability �ij of being in regime j next period conditional on being in regime i this period is assumed exogenous and constant. Speci…cally �ij = Pr(st+1 = jjst = i) with<sup>PM</sup> j=1<sup>�</sup> ij<sup>=1andi; j�f1; :::; Mgde…nedintheM�MtransitionmatrixP</sup> below. 



The MS-VAR model parameters in both regimes are estimated jointly with the transition probabilities that are constant and assumed exogenous. The vector of 

> 12See World Economic Outlook, April 2009, chapter 3, P. 107. 

9 

regimes st is unobserved, maximizing the likelihood function of the model entails using iterative estimation techniques. Following Hamilton (1990) and Krolzig (1997), the Expectations Maximization (EM) algorithm originally introduced by Dempster, Laird and Rubin (1977) is employed to perform this task. 

It should be highlighted since that this apparatus is constituted of a single Markov chain for the entire vector of processes, Yt; that comprise the VAR. Hence it can most appropriately be deemed a method by which to aggregate ‘turning points’across individual series. As will become clear in subsequent sections we will use this particular feature of the MS-VAR methodology in order to validate our models. 

#### 3.1 Regime-dependent Impulse Response Functions 

Our aim is to compare the relationship between the fundamental disturbances in the model and the endogenous variables across regimes. A prior hypothesis is that the impact of a global house price shock on a speci…c country may di¤er strongly across regimes. The essence of the identi…cation problem is that we obtain estimates of the covariance matrices �1; :::; �M but not unique estimates of matrices B1; :::; BM which would be necessary to uncover the variance covariance matrix of fundamental disturbances determining the paths of impulse response functions. Thus we need to impose restrictions on the parameter estimates of the unrestricted model in order to identify the B1; :::; BM .<sup>13</sup> 

There can be many choices of restriction schemes drawn from within the structural VAR literature, e.g. Sims (1980) to Uhlig (2005). The natural restriction is to impose that external shocks are exogenous with respect to domestic house price developments and that a given country is too small to have an instantaneous e¤ect on the global factor. Domestic house prices may a¤ect the global house price factor but only with a lag. This is consistent with the more protracted e¤ect of house prices, as compared to …nancial markets. We employ the recursive identi…cation scheme aimed at the contemporaneous impact multiplier matrix proposed by Sims (1980) . Essentially, each matrix Bi has K<sup>2</sup> identi…able elements for which K<sup>2</sup> restrictions need to be imposed. The identity BiBi<sup>0= �iimposes K(K +1)=2 restrictions resulting from the</sup> symmetry of the variance covariance matrix. The remaining K(K � 1)=2 restrictions are achieved by imposing a recursive structure on the model with Bi being a lower triangular and exact identi…cation is achieved. This can be recovered from a Choleski decomposition of matrix �i: This naturally will have implications for the ordering of variables in our VAR system. Speci…cally, a fundamental disturbance to a variable 

> 13The methodology of Ehrmann et al. (2003) is di¤erent from that proposed by Krolzig and Torro(1999) in which they emphasize responses of the economy given transitions between regimes. It is closer in spirit to Generalized Impulse Response functions of Koop, Pesaran and Potter (1996) (KPP) which advocates how impulses may di¤er depending on which state the shock occurs; although di¤ers in that KPP present the impulse reponses in terms of densities owing to their stochastic treatment of the histories. 

10 

has a contemporaneous impact on the variable itself and the variables ordered below it. 

The regime-dependent impulse responses functions (RDIRF) generated in the MS-VARs framework describe the responses of endogenous variables to fundamental shocks within a particular regime. RDIRFs are in e¤ect conditional on a given regime prevailing at the time of the disturbance and throughout its entire duration (see Ehrmann et al., 2003). 

The general model set-up described encapsulates MK<sup>2</sup> RDIRFs; i.e. responses of K variables to K disturbances in M regimes. Let the expected change in endogenous variables at time t + h to a one standard deviation shock to the k�th fundamental disturbance at time t; conditional on regime i; be given by, 



Here, the series of K-dimensional response vectors 'ki;1; :::; 'ki;h dictate the response of the endogenous variables. It follows that the response vectors are estimated with estimate of matrix B<sup>b</sup> i (i.e. regime-dependent) obtained through identifying restrictions. Denoting u0 as the initial disturbance vector<sup>14</sup> the response vectors can estimated as, 



Furthermore, standard bootstrap techniques are employed in order to judge the precision (i.e. generate con…dence bands) of the estimated RDIRFs; but this task is complicated by the presence of a hidden Markov-chain determining the regime. We refer the reader to Ehrmann et al. (2003, pg 12) for a detailed description of the bootstrap procedure which involves creating arti…cial histories for the regimes. 

### 4 Evidence of Contagion 

We present now results for two countries, namely Spain (ESP) and United Kingdom (UK) that illustrate our approach and provide evidence of an heightened repercussion of international house price shocks on domestic house prices during crisis periods, that we interpret as contagion. These countries are among those who have been identi…ed by IMF (2004) as exhibiting rapid house price growth in the years 2000. Visual inspection of the charts given in Annex A1, for these two countries indicates an evident co-movement of the domestic house prices (i.e. HPIESP, HPIUK) vis-a-vis the corresponding common factors (i.e. FACxESP and FACxUK). Other candidate countries 

> 14This is a vector of zeros except for the kth element which is unity. 

11 

could also be used as long as they have a signi…cant degree of synchronization with the common factor over the whole sample, as in the case of Australia, the USA, etc. Arguably, even for these countries, the match is far for being perfect.<sup>15</sup> In particular, the US is usually a leading indicator of house prices in the rest of the world. As a consequence, contagion is not expected to occur in all countries and we study more in detail the case of France in section 5. 

#### 4.1 Model Selection 

We assume the presence of two distinct regimes namely Crisis and Normal (M = 2) in all the speci…cations we consider. Modelling in a two regime framework has been the convention in the literature on contagion thus far. Furthermore, our small sample size prevents us from extending either the number of states beyond M = 2, or the dimension of the VAR by including additional macroeconomic variables. Our main objective is to provide, from a statistical point of view, robust results on the potential existence of contagion. The detailed analysis of the channels of contagion is left for future work. We compare two speci…cations, ‘MSIA(2)’, in which we allow the intercepts and autoregressive parameters to change between regimes and ‘MSIAH(2)’ in which additionally the variance covariance matrix of residuals is also allowed to ’<sup>17</sup> change.<sup>16</sup> Firstly we establish the appropriate lag length for the VAR by comparing the traditionally used information criteria, looking at lags 1 to 4. As can be seen from Tables 1 and 2 below, for Spain and UK the information criteria support MSIA(2)-VAR(2) and MSIAH(2)-VAR(2) speci…cation. Furthermore, the chosen lag length also ensures that there is no serial correlation in the residuals (speci…cally standardized Gaussian residuals). This can be seen from Figures A2 and A3 in the appendix indicate that the residuals are statistically well-behaved showing no serial correlation and/or signi…cant non-normality. We do not explicitly test for the number of regimes in this work and it is well known that this can be di¢ cult enterprise in a Markov switching framework given the presence of nuisance parameters under the null of linearity of the model.<sup>18</sup> ’<sup>19</sup> For our purposes we would like to select between, 

> 15 Charts are available from the authors upon request. 

> 16We are extremely grateful to Martin Ellison for making the program in Ox 2.10 to calculate the regime dependent impulse response functions and bootstrapping associated con…dence bands available (see Ehrmann et al, 2003). This aforementioned program and related estimations draw on functions contained within the excellent MSVAR class for Ox 2.10 developed by Hans-Martin Krolzig (see Krolzig (1998)). 

> 17In order to clarify the convention we use; MSIAH(2): Markov Switching (MS) in Intercept (I), Autoregressive parameters (A) and Heteroskedasticity (H) for 2 regimes. This is essentially the terminology as in Krolzig (1997). 

> 18For instance if we test for the regime invariance of all the estimated parameters across regimes 1 and 2, i.e. I1 = I2; A1 = A2 and/or depending on the model �1 = �2, then it follows that the transition probablilities �ij; i; j 2 f1; 2gare unidenti…ed. 

> 19Formal tests of MS vesus linear alternatives have been proposed by Hansen (1992, 1996) and Garcia (1998) which are essentially standardized likelihood ratio tests designed to deliver asymptoti- 

12 

||VAR(1)|VAR(2)|VAR(3)|VAR(4)|
|---|---|---|---|---|
|||MSIA(2)|||
|AIC criterion|-2.925|-3.247*|-3.119|-3.067|
|HQ criterion|-2.757|-3.000*|-2.794|-2.858|
|SC criterion|-2.511|-2.639*|-2.318|-2.554|
|||MSIAH(2|)||
|AIC criterion|-3.123|-3.359*|-3.297|-3.276|
|HQ criterion|-2.925|-3.082*|-2.941|-2.840|
|SC criterion|-2.635|-2.676*|-2.419|-2.203|



Table 1: Spain. Information Criteria. (*) indicates selected speci…cation. 

speci…cally, MSIA(2)-VAR(2) and MSIAH(2)-VAR(2) models. In addition we also report results when testing between MSIH(2)-VAR(2) and MSIAH(2)-VAR(2) speci…cations. In Table 3 we provide the results for likelihood ratio tests.<sup>20</sup> Under the null 

||VAR(1)|VAR(2)|VAR(3)|VAR(4)|
|---|---|---|---|---|
|||MSIA(2)|||
|AIC criterion|-1.435|-1.567*|-1.547|-1.549|
|HQ criterion|-1.266|-1.320*|-1.320|-1.143|
|SC criterion|-1.021*|-0.957|-0.957|-0.548|
|||MSIAH(2|)||
|AIC criterion|-1.588|-1.614*|-1.516|-1.522|
|HQ criterion|-1.336|-1.389*|-1.159|-1.086|
|SC criterion|-0.930|-1.099*|-0.637|-0.448|



Table 2: UK. Information Criteria. (*) indicates selected speci…cation. 

hypothesis of regime invariance of the variance covariance matrix, �1 = �2, the regime dependent autoregressive parameters and intercepts ensure the statistical identi…cation of the model under the null. Similarly, for the hypothesis A1 = A2; identi…cation is gained through the regime-dependence of the intercepts and variance-covariance matrix. Given that these tests are nuisance parameter free classical likelihood theory can be invoked with the tests being asymptotically �<sup>2</sup> (r); r being the number of linearly independent restrictions in the test. In all cases, the null of regime invariance 

cally valid inference. As noted by Krolzig (2000), these can be computationally infeasible in systems approaches in addition to being overly conservative and displaying low power. 

> 20Note that subscripts f1; 2g in �1; �2 and A1; A2 correspond to the labels fCrisis; Normalg: 

13 

|Like|lihood|ratio test|
|---|---|---|
|Null hypothesis||Test statistic|
|(i) �1 = �2|Spain|�<sup>2</sup>(3) = 11.09 **|
||UK|�<sup>2</sup>(3)= 15.26 **|
|(ii) A1 =A2|Spain|�<sup>2</sup>(8) = 25.01 **|
||UK|�<sup>2</sup>(8)= 111.9 **|



Table 3: Testing between alternative speci…cations.(i)MSIA(2)-VAR(2) vs MSIAH(2)VAR(2), and (ii)MSIH(2)-VAR(2) vs MSIAH(2)-VAR(2). (**) indicates signi…cance at the 5% critical level. 

of certain sets of parameters is rejected at a 5% critical level and we conclude that the MSIAH(2)-VAR(2) speci…cation is justi…ed for the cases of Spain and UK. 

The presence of regime switching variance-covariance matrix, in addition to being supported in our case on statistical grounds of model selection, is in line with the well established observation that periods of contagion (or Crisis) are those characterized with higher volatility. See Rigobon (2003 a,b). In this regard, a large proportion of multivariate contagion testing literature essentially focuses on analyzing exclusively the reduced form variance-covariance matrix of returns processes across markets; see Dungey, Fry, Gonzalez-Hermosillo and Martin (2005) for a comprehensive summary. Given the data frequency and prolonged adjustment periods typically seen in macroeconomic data our …nal assessment of contagion (as we shall demonstrate subsequently) will have less of a role for the regime-switching variance covariance matrix. 

The estimated transition matrices for Spain and UK are, 



respectively.<sup>21</sup> These are fairly persistent given we have quarterly observations; expected durations for the crisis and normal regimes being 16 quarters and 44 quarters in the case of Spain and 9 quarters and 34 quarters in the case of UK.<sup>22</sup> Figures 1 and 2 below plot the estimated …ltered and smooth probabilities attained from our chosen models. 

#### 4.2 Regime Switching 

We begin by assessing the models results with respect to identifying regimes (and /or turning points) that the system has moved through over the time period con- 

> 21MS-VAR output provided is in Tables 4 and 5 in the Appendix. 

> 22 The expected duration are for state 1 (state 2) � 1=(1 � �11) (� 1=(1 � �22)): See Hamilton (1989, pg 374). 

14 

sidered. Figures 1 and 2 below plot the estimated …ltered and smooth probabilities attained from our chosen models. The …ltered probability is interpreted as the optimal inference using information up till time t, i.e. Pr(st = ijYt); whereas the smooth probability; Pr(st = ijYT ) takes into account the entire sample observations. 



<!-- Start of picture text -->
1.00 Probabilities of Crisis Regime<br>filtered smoothed<br>predicted<br>0.75<br>0.50<br>0.25<br>1985 1990 1995 2000 2005 2010<br>1.00 Probabilities of Normal Regime<br>0.75<br>0.50<br>0.25<br>1985 1990 1995 2000 2005 2010<br><!-- End of picture text -->

Figure 1: Spain. Estimated regime probabilities for MSIAH(2)-VAR(2) model. 

In the case of Spain, we identify with near certainty (i.e. estimated smooth probabilities being at or close to unity) two main crisis periods. The early 1990s and the 2007-2008 period. For the United Kingdom, in addition to these two periods, two smaller crisis periods are also identi…ed in the early 1980s and in 1995. We return to this issue in the subsequent subsection. 

15 



<!-- Start of picture text -->
1.00 Probabilities of Crisis Regime<br>filtered smoothed<br>predicted<br>0.75<br>0.50<br>0.25<br>1980 1985 1990 1995 2000 2005 2010<br>1.00 Probabilities of Normal Regime<br>0.75<br>0.50<br>0.25<br>1980 1985 1990 1995 2000 2005 2010<br><!-- End of picture text -->

Figure 2: UK. Estimated regime probabilities for MSIAH(2)-VAR(2) model. 

#### 4.3 Economic Validation 

Before proceeding to analyze the impulse responses we subject our chosen models to another level of screening. This is crucial in order to assess whether the estimated regimes are economically meaningful with respect to identifying or being consonant to periods in which contagion occurred or was highly probable. Over the same period, a time series capturing the proportion of countries in …nancial crisis denoted “…nan_crises” (see section on Data) is overimposed to the plots of smooth probabilities estimated via the modelling procedure. The Figures 3 and 4 below are encouraging in that the model appears to identify with near certainty periods in which a high proportion of countries in our sample (speci…cally in excess of a threshold of 0.28) were facing a …nancial crises. 

16 



<!-- Start of picture text -->
1.0 Probabilities of Crisis Regime<br>smoothed finan_crises<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>1980 1985 1990 1995 2000 2005 2010<br><!-- End of picture text -->

Figure 3: Spain. Correspondance of identi…ed Crisis regimes (via smoothed probabilities) with the index of global intensity of …nancial crises (…nan_crises). 

These major episodes of …nancial crisis took place in the early 1990s -which triggered large adjustments of house prices around the world, in the US, Europe and Japan- and during the 2008 subprime crisis. It is also interesting to investigate further the other episodes that do not coincide exactly. First of all the Asian crisis in the late 1990s appears to have no e¤ect on house markets in UK and Spain, while a signi…cant proportion of Asian countries were in a deep recession. In addition, in the case of the UK, another spike appears in 1994-1995, that we can interpret as a late e¤ect of the early 1990s …nancial crisis. Finally, the early 1980s also triggered a …nancial crisis of smaller dimension but without a sharp decline of nominal house prices in the UK and Spain. In both cases of additional spikes signalling crisis periods, house prices stagnated in nominal terms and even slightly decreased, but were reduced more signi…cantly in real terms in the UK as well as in the rest of OECD countries. Indeed, the shock was rather an in‡ation shock, that reduced real house prices but did not turn into what could be categorized as a full-‡edged …nancial crisis in these two countries. However, the 1979-80 “oil price shock”did create a recession in a few countries as indicated by the crisis index in 1980. 

In order to look at this from another standpoint, the …gures also illustrate that the phases of the two regimes are appropriately aggregated via a single, common Markov chain. This can be taken as evidence of synchronous movement of the global house price factor and the house price developments in the speci…c country. 

17 



<!-- Start of picture text -->
1.0 Probabilities of Crisis Regime<br>smoothed finan_crises<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>1980 1985 1990 1995 2000 2005 2010<br><!-- End of picture text -->

Figure 4: UK. Correspondance of identi…ed Crisis regimes (via smoothed probabilities) with the index of global intensity of …nancial crises (…nan_crises). 

#### 4.4 Analyzing Impulse Responses 

We now consider the response of real house prices within the two regimes to a shock in the global house price factor. We normalize the size of this shock to unity for both regimes. By controlling for the size of the shock we can trace out the change in the transmission mechanism across regimes, consistently with our goal of investigating shift-contagion. Moreover, given that we are essentially estimating reduced form systems, our choice of variables, i.e. domestic house price series and global house price factor is aligned with our choice of ‘within regime’identi…cation strategy. 

To elaborate, given that the Choleski decomposition is lower triangular, our global factor which is ordered …rst implies that the channel of shock propagation on impact, i.e. in the same quarter, can only run from the rest of the world (as captured by the factor) to an individual country; not the contrary. In many ways this structure and choice of variables circumvents the issue of determining causality encountered in much of pairwise testing.<sup>23</sup> In addition, the approach provides more ‡exibility, since using a global factor (which may be capturing developments in a group of countries instead of a speci…c country) allows us to integrate possible changes in our sample 

> 23For example, Forbes and Rigobon (2002) perform their correlation tests on pairs of countries under the the assumption that contagion spreads from one country to another with the source country being exogenous. But this test can then be performed in the reverse direction with the implicit assumption of exogeneity on the two asset returns reversed. On statistical ground performing the two tests in this way is inappropriate as it clearly ignores the simultaneity bias. In order to circimvent this problem Forber and Rigobon, inter alia, are very explicit in their exogeneity assumptions. 

18 

regarding the sources of contagion across countries . 

As shown in Figures 5 and 6, we observe that the response to the global house factor is signi…cant in both regimes, which provides evidence of international transmission of house prices. This runs against the idea of purely local house markets, consistent with the …ndings of Beltratti and Morana (2010) who …nd a signi…cant impact of a global factor on house prices in the Euro area -even if their global factor is computed di¤erently with a large share of macroeconomic variables other than house prices. 

Secondly, the scale of the response of domestic house prices (measured in terms of real growth), is ampli…ed in the ‘Crisis’regime relative to the ‘Normal’regime. By the second quarter, the response function records the maximum impact of 0.0065 versus 0.002 in the case of Spain. In the comparatively more subdued case of the UK it is 0.006 versus 0.004. 



<!-- Start of picture text -->
0.0075<br>Crisis Regime - Response of HPIESP<br>0.0050<br>0.0025<br>0.0000<br>0 5 10 15 20 25 30 35 40<br>0.004<br>0.003<br>Normal Regime - Response of HPIESP<br>0.002<br>0.001<br>0.000<br>0 5 10 15 20 25 30 35 40<br><!-- End of picture text -->

Figure 5: Spain. Regime dependent impulse responses of real house price changes to an international house price shock, in Crisis or Normal regimes. Dotted lines represents one standard deviation con…dence bands based on 1000 bootstrap replications. Time on horizontal axis in quarters. 

Thirdly, the response appears to be rather persistent over time and this is also consistent with Beltratti and Morana (2010), who indicate that global shocks are more relevant for house price ‡uctuations in the medium run (with a peak at 20 quarters) than in the short run, contrarily to what is found for stock prices and interest rates (typically peaking at around 5 quarters). 

Fourthly, one can nevertheless notice a di¤erence in the shape of the response, with a more protracted response in the case of Spain relative to the UK. In the latter case, the response is close to zero after 10 quarters, while it remains slightly positive after 30 quarters in the case of Spain. This may be viewed as evidence of a 

19 

more reactive housing market in the UK, based on its higher level of securitization<sup>24</sup> and hence resembling more closely the typical reaction expected of stocks and bond markets.<sup>25</sup> 



<!-- Start of picture text -->
0.0075<br>Crisis Regime - Response of HPIUK<br>0.0050<br>0.0025<br>0.0000<br>0 5 10 15 20 25 30 35 40<br>0.006<br>0.004 Normal Regime - Response of HPIUK<br>0.002<br>0.000<br>0 5 10 15 20 25 30 35 40<br><!-- End of picture text -->

Figure 6: UK. Impulse responses of real house price changes to an international house price shock within Crisis and Normal regimes. See Figure 5 for details. 

### 5 No Contagion in France? 

We now describe another example for which we implement the same statistical and economic assessment as conducted previously for Spain and UK. However, as indicated by Figure A1c (see Appendix), the degree of synchronization between real house prices in France and the common global house price factor appears much smaller than for UK and Spain.<sup>26</sup> For example, in OECD countries house prices started to decelerate sharply in 1988-1989, but only in 1990-1991 in France. 

The model for France according to the previously employed information criteria was MSIAH(2)-VAR(1). Inspection of the residuals revealed that there was serial correlation present at this lag length. This was recti…ed when the lag length was increased to p = 2 and hence we selected the model MSIAH(2)-VAR(2) as in the cases described above. The patterns of estimated regime probabilities did not change substantially in either case. 

> 24According to the European Securitization Forum, total outstanding of Residential Mortgage Based Securities (RMBS) in 2008Q4 amounted to 162.5 billion euros in Spain and 455.8 billion in the UK (and only 12.9 billion in France). Even if the Spanish RMBS market is one of the most developed in the euro area (see ECB Monthly Bulletin, Feb 2008), its share in GDP was at the end of our sample period only 60% of that of the UK. 

> 25Constraining �1 = �2, did not have any signi…cant e¤ect on the impulse responses. 

> 26The lower development of securitization in France (see section 4.4 above) may also be a reason behind the lack of apparent synchronization with the global house factor. 

20 

We proceed to the next stage of validation and investigate if the results of the model, speci…cally, the estimated regime probabilities (see Figure 7 below) were economically meaningful in terms of identifying periods when contagion was conjectured to have occurred. As can be observed from Figure 8 below, there appears to be weak evidence of correspondence between the periods of the Crisis regime estimated via the modelling procedure and our selected ex-post dating measure. The evidence provided by the model appears to suggest somewhat extended spans of crisis regimes which do not seem plausible within a historical perspective. Indeed France was characterized by two housing crises : one in the early 1980’s and another one in the early 1990’s, followed by a protracted period with house prices below trend. The latter period is properly identi…ed as a housing crisis period but does not correspond to the usual view of relatively short lived crisis. In addition, the probabilities of being in the Normal regime are suggestive of a more volatile pattern with several short lived spikes. The estimated transition matrix below suggests that the durations for both Crisis and Normal regimes are roughly symmetric at approximately 9 quarters for each. 



The pattern suggests that France was experiencing a crisis regime approximately half of the considered span which we suggest is not justi…able on economic or historical grounds. We tentatively conclude therefore that there is an absence of a contagion e¤ect in the case of France, at least until the end the 1990s. 



<!-- Start of picture text -->
1.00 Probabilities of Crisis Regime filtered smoothed<br>predicted<br>0.75<br>0.50<br>0.25<br>1985 1990 1995 2000 2005 2010<br>1.00 Probabilities of Normal Regime<br>0.75<br>0.50<br>0.25<br>1985 1990 1995 2000 2005 2010<br><!-- End of picture text -->

Figure 7: France. Estimated regime probabilities for MSIAH(2)-VAR(2) model. 

The reason for this may be attributed to the fact that such a modelling procedure assumes the existence of a single Markov chain for the entire vector of endogenous 

21 

variables Yt: The MS-VAR apparatus essentially aggregates the cycles across the individual series, in our case the country and factor. The pattern we see in the case of France, as shown in Figure A1c does not indicate any discernible co-movement of the series, at least till the end of 1999 when the ‡uctuations of our series seem to be more synchronized with the global developments in house prices. 



<!-- Start of picture text -->
1.0 Probabilities of Crisis Regime smoothed finan_crises<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>1980 1985 1990 1995 2000 2005 2010<br><!-- End of picture text -->

Figure 8: France. Correspondance of identi…ed Crisis regimes (via smoothed probabilities) with the index of global intensity of …nancial crises (…nan_crises). 

In the post-1999 period, the increase in the correlation of house prices between France and the international house factor may be partly explained by the introduction of EMU, with more correlation among the largest Euro area countries and in particular for France, as shown by Alvarez et al. (2010). However there is a persistent lag between France and the UK and the US in the second half of the years 2000. 

### 6 Conclusion 

The paper attempts to provide evidence of international “shift-contagion”in housing markets for Spain and the UK via a Markov Switching VAR framework and regimedependent impulse response functions. We …nd that the identi…ed ‘Crisis’regimes correspond to an exogenously determined index of …nancial crisis which peaked in the early 1990s and more recently during the Subprime crisis, where asymmetric information on house prices as well as mortgage based securities was pervasive. Furthermore, we …nd that the response of domestic house prices to a shock to a common (global) house price factor during a ‘Crisis’regime is relatively more ampli…ed as opposed to what is observed in a ‘Normal’regime. Quite di¤erent results are observed 

22 

in the case of France, characterized by what is conjectured to be a lower degree of synchronization before EMU and the persistence of divergence with the UK and the US afterwards. Our approach is consistent with former de…nitions of shift-contagion, and appears to be powerful in providing evidence of the heightened repercussion of house price shocks in times of crisis, that go beyond the larger size of the shocks. 

A salient point that we highlight from our analysis here is that contagion in housing markets is viewed as a phenomenon which is closely associated with global trends in international housing cycles, rather than country-by-country spillovers, with possible shifts in existing channels of transmission in times of ‘Crisis’. 

Further research would imply extending the analysis to a larger set of countries. Taking into account more variables in the MS-FAVAR model would also be fruitful, on the basis of a richer set of identi…cation restrictions for the orthogonalization of shocks. 

23 

### References 

- [1] Alvarez, L., G. Bulligan, A. Cabrero, L. Ferrara and H. Stahl (2009). Housing and Macroeconomic Cycles in the Major Euro Area Countries. Banque de France, Working Paper, No. 269. 

- [2] Ang, A. and Bekaert, G. (1999). International Asset Allocation with TimeVarying Correlations. NBER Working Paper, 7056. 

- [3] Arrondel, L. and Savignac, F. (2009). Stockholding: Does Housing Wealth Matter. Banque de France, Working Paper, No. 266. 

- [4] de Bandt, O., K. Barhoumi and C. Bruneau (2010a). The International Transmission of House Price Shocks. Banque de France, Working Paper, No. 274. 

- [5] de Bandt, O., T. Knetsch, J. Penalosa and F. Zollino (2010b) "Housing markets in Europe: a Macroeconomic Perspective", Springer Verlag. 

- [6] Baig, T. and Goldfajn, I. (1998). Financial Markets Contagion in the Asian Crises. IMF Mimeo. 

- [7] Bekaert, G. and Harvey, C. (1995). Time-Varying World Market Integration. Journal of Finance, 50, 403-444. 

- [8] Beltratti, A and C. Morana (2010) International House prices and Macroeconomic Fluctuations, Journal of Banking and Finance, 34, 533-545. 

- [9] Bernanke, B. S., Boivin, J. and Eliasz, P. (2006). Measuring the E¤ect of Monetary Policy: A Factor-Augmented Vector Autoregressive (FAVAR) Approach. The Quarterly Journal of Economics, 120:1, 387-422. 

- [10] Billio, M. Lo Duca, M. and Pelizzon, L. (2005). Contagion Detection with Switching Regimes: A Short and Long run Analysis. GRETA Working Paper 0501. 

- [11] Chou, R., Ng, V. and Pi, L. (1994). Cointegration of International Stock Market Indices. IMF Working Paper, WP/94/94. 

- [12] Claessen, S. and K. Forbes (2001) International Financial Contagion, Kluwer Academic Publisher. 

- [13] F Corsetti, G., Pericoli, M. and Sbracia, M. (2005). Some Contagion, Some Interdependence: More Pitfalls in Tests for Financial Contagion. Journal of International Money and Finance, 24(8), 1177-1199. 

- [14] de Bandt, O., K. Barhoumi and C. Bruneau (2010b). The International Transmission of House Price Shocks. Banque de France, Working Paper, No. 274. 

24 

- [15] Dempster, A. P., Laird, N. M. and Rubin, D. B. (1977). Maximum Likelihood Estimation from Incomplete Data via the EM Algorithm. Journal of the Royal Statistical Society, 39, Series B, 1-38. 

- [16] DiPasquale, D. and W. Wheaton (1994) Housing Market Dynamics and the Future of Housing Prices, Journal of Urban Economics, 35, 1-27. 

- [17] Dungey, M., Fry, R., Gonzalez-Hermosillo and Martin, V. L. (2005). Empirical Modelling of Contagion: A Review of Methodologies. Quantitative Finance, 5(1), 9-24. 

- [18] Ehrmann, M., Ellison, M. and Valla, N. (2003). Regime-dependent Impulse Response Functions in a Markov Switching Vector Autoregression Model. Economics Letters, 78, 295-299. 

- [19] Eichengreen, B., Rose, A. K. and Wyplosz, C. (1996). Contagious Currency Crises: First Tests. Scandinavian Journal of Economics, 98(4), 463-484. 

- [20] Gravelle, T., Kinchan, M. and Morely, J. (2006). Detecting Shift-contagion in Currency and Bond Markets. Journal on International Economics, 68, 409-423. 

- [21] Favero, C. A. and Giavazzi, F. (2002). Is the International Propagation of Shocks Non-linear? Evidence from the ERM. Journal of International Economics, 57(1), 231-246. 

- [22] Fauvet, L. (2007) Les achats de logements par des étrangers, Etudes Foncières, octobre. 

- [23] Friggit, J. (2007) Home purchases by foreigners in France : notes on L. Fauvet’s article. CGEDD-Meeddm, available at http://www.cgedd.developpementdurable.gouv.fr/rubrique.php3?id_rubrique=137 

- [24] Forbes, K. and Rigobon, R. (2002). No Contagion, Only Interdependence: Measuring Stock Market Comovements. Journal of Finance, 57(5), 2223-2261. 

- [25] Fratzscher, M. (2003). On Currency Crises and Contagion. International Journal of Finance and Economics, 8(2), 109-129. 

- [26] Garcia, R. (1998). Asymptotic Null Distribution of the Likelihood Ratio Test in Markov Switching Models. International Economic Review, 39. 

- [27] Gravelle, T., Kichian, M. and Morely, J. (2006). Detecting Shift-Contagion in Currency and Bond Markets. Journal of International Economics, 68, 409-423. 

- [28] Goodman, A. C. and T. G. Thibodeau Where are the speculative bubbles in US housing markets? Journal of Housing Economics, 17, 117-137. 

25 

- [29] Hamao, Y., Masulis, R. and Ng, V. (1990). Correlation in Price Changes and Volatility across International Stock Markets. Review of Financial Studies, 3, 281-308. 

- [30] Hamilton, J. D. (1989). A New Approach to the Econometric Analysis of Nonstationary Time Series and the Business Cycle. Econometrica, 57, 357-384. 

- [31] Hamilton, J. D. (1990). Analysis of Time Series Subject to Changes in Regime. Journal of Econometrics, 45: 39-70. 

- [32] Hansen, B. E. (1992). The Likelihood Ratio Test under Non-standard Conditions: Testing the Markov-Switching Model of GNP. Journal of Applied Econometrics, 7, 61-82. 

- [33] Hansen, B. E. (1996). Erratum: The Likelihood Ratio Test under Non-standard Conditions: Testing the Markov-Switching Model of GNP. Journal of Applied Econometrics, 11, 195-199. 

- [34] International Monetary Fund (2004) World Economic Outlook, April. 

- [35] Kaminsky, G. L. and Reinhart, C. M. (2001). Financial Markets in Times of Stress. NBER Working Paper No. 8569. 

- [36] King, M. A. and Wadhwani, S. (1990). Transmission of Volatility between Stock Markets. The Review of Financial Studies, 3(1), 5-33. 

- [37] King, R. G., Plosser, C. I., Stock, J. H. and Watson, M. W. (1991). Stochastic Trends and Economic Fluctuations. American Economic Review, 81: 819-840. 

- [38] Kim, C.-J and Nelson, C. (1998). State-Space Models with Regime Switching: Classical and Gibbs Sampling Approaches with Applications. MIT Press. 

- [39] Koop, G., Pesaran, M. H. and Potter, S. M. (1996). Impulse Response Analysis in Nonlinear Multivariate Models. Journal of Econometrics, 74: 119-147. 

- [40] Krolzig, H.-M. (1998). Econometric Modelling of Markov-Switching Vector Autoregressions using MSVAR for Ox. Discussion Paper, Department of Economics, University of Oxford. 

- [41] Krolzig, H.-M. and Torro, J. (1999). A New Approach to the Analysis of Shocks and the Cycle in a Model of Output and Employment. EUI Working Paper ECO, No. 99/30. 

- [42] Krolzig, H.-M. (2000). Markov-Switching Procedures for Dating the Euro-zone Business Cycle. Quarterly Journal of Economic Research, 70, 339-351. 

26 

- [43] Krolzig, H.-M. (2001). Business Cycle Measurement in the Presence of Structural Change: International Evidence. International Journal of Forecasting, 17 (3), 349-368. 

- [44] Kruger, M., Osakwe, P. N. and Page, J. (1998). Fundamentals, Contagion and Currency Crises: An Empirical Analysis. Bank of Canada Working Paper, 98-10. 

- [45] Pesaran, M. H. and Pick, A. (2007). Econometric Issues in the Analysis of Contagion. Journal of Economics Dynamics and Control, 31(4), 1245-1277. 

- [46] Loretan, M. and English, W. (2000). Evaluating "Correlation Breakdowns" During Periods of Market Volatility. Board of Governors of the Federal Reserve System, International Finance Discussion Paper, No. 658 

- [47] Reinhart, C. and K. Rogo¤ (2008). Is the 2007 US Subprime Crisis So Di¤erent? An International Historical Comparison. NBER Working Paper 13761. 

- [48] Rigobon, R. (2003a). Identi…cation Through Heteroscedasticity. Review of Economics and Statistics, 85(4), 777-792. 

- [49] Rigobon, R. (2003b). On the Measurement of International Propagation of Shocks: Is the Transmission Stable? Journal of International Economics, 61(2), 261-283. 

- [50] Pavlova, A and Rigobon, R (2008) The Role of Portfolio Constraints in the International Propagation of Shocks, Review of Economic Studies, Blackwell Publishing, vol. 75(4), pages 1215-1256, October. 

- [51] Sims, C. A. (1980). Macroeconomics and Reality. Econometrica, 48: 1-48. 

- [52] Stock, J. H. and Watson, M. W. (2005). Implications of Dynamic Factor Models for VAR Analysis. NBER Working Paper,11467. 

- [53] Stone, M. R. and Weeks, M. (2001). Systemic Financial Crises, Balance Sheets, and Model Uncertainty. IMF Working Paper, 01/162. 

- [54] Tong, H. (1990). Non-Linear Time Series: A Dynamical Systems Approach. Oxford University Press, Oxford. 

- [55] Uhlig, H. (2005).What Are the E¤ects of Monetary Policy on Output? Results from an Agnostic Identi…cation Procedure. Journal of Monetary Economics, 52, pp. 381-419. 

27 

### A Appendix 



<!-- Start of picture text -->
.20 12<br>.15<br>8<br>.10<br>4<br>.05<br>0<br>.00<br>-.05 -4<br>-.10<br>1980 1985 1990 1995 2000 2005<br><!-- End of picture text -->

Figure A0: Thick black line illustrates the common house price factor. 



<!-- Start of picture text -->
8<br>6<br>4<br>2<br>0<br>-2<br>-4<br>-6<br>-8<br>1980 1985 1990 1995 2000 2005<br>HPIESP FACxESP<br><!-- End of picture text -->

Figure A1a: Spain. Thick line illustrates the common house price factor. 

28 



<!-- Start of picture text -->
12<br>10<br>8<br>6<br>4<br>2<br>0<br>-2<br>-4<br>-6<br>1980 1985 1990 1995 2000 2005<br>HPIUK FACxUK<br><!-- End of picture text -->

Figure A1b: UK Thick line illustrates the common house price factor. 



<!-- Start of picture text -->
6<br>4<br>2<br>0<br>-2<br>-4<br>-6<br>-8<br>1980 1985 1990 1995 2000 2005<br>HPIFRA FACxFRA<br><!-- End of picture text -->

Figure A1c: France. Thick line illustrates the common house price factor. 

29 



<!-- Start of picture text -->
1.0 Correlogram: Standard resids Density: Standard resids<br>ACF-HPIESP stdresid-HPIESP N<br>0.4<br>0.5<br>0.3<br>0.0<br>0.2<br>-0.5 0.1<br>1 5 9 13 -3 -2 -1 0 1 2 3 4<br>1.0 40<br>ACF-FACxESP stdresid-FACxESP N<br>0.5 30<br>0.0 20<br>-0.5 10<br>1 5 9 13 -0.050 -0.025 0.000 0.025 0.050<br><!-- End of picture text -->

Figure A2: Spain. Diagnostic check for residual serial correlation and non-normality. 



<!-- Start of picture text -->
1.0 Correlogram: Standard resids Density: Standard resids<br>ACF-HPIUK stdresid-HPIUK N<br>0.5<br>0.4<br>0.0<br>0.2<br>-0.5<br>1 5 9 13 -2 0 2 4<br>1.0 0.5<br>ACF-FACxUK stdresid-FACxUK N<br>0.4<br>0.5<br>0.3<br>0.0<br>0.2<br>-0.5<br>0.1<br>1 5 9 13 -4 -3 -2 -1 0 1 2 3 4<br><!-- End of picture text -->

Figure A3: UK. Diagnostic check for residual serial correlation and non-normality. 

30 

||Re|gime 1||Reg|ime 2|
|---|---|---|---|---|---|
|Dep. variable|HPIESPt|FACxESPt|HPIE|SPt|FACxESPt|
|||Coe|¢ cients|||
|Constant|0.002 (0.008)|1.876 (0.623)|0.001|(0.001)|0.085 (0.081)|
|HPIESPt�1|0.145 (0.216)|11.14 (13.26)|0.276|(0.079)|10.10 (4.71)|
|HPIESPt�2|0.382 (0.249)|-0.834 (13.63)|0.591|(0.080)|6.722 (4.98)|
|FACxESPt�1|-0.010 (0.003)|0.485 (0.221)|-0.004|(0.002)|0.435 (0.221)|
|FACxESPt�2|0.004 (0.002)|-0.076 (0.159)|0.002|(0.003)|0.163 (0.158)|
|Error variance�100|0.078|56.86|0|.006|49.14|



Table 4: Spain. Estimation output for MSIAH(2)-VAR(2). Standard errors in parantheses. 

||Reg|ime 1|Reg|ime 2||
|---|---|---|---|---|---|
|Dep. variable|HPIUKt|FACxUKt|HPIUKt|FAC|xUKt|
|||C|oe¢ cients|||
|Constant|-0.008 (0.003)|-1.155 (0.289)|0.009 (0.003)|0.089|(0.118)|
|HPIUKt�1|0.413 (0.192)|-1.156 (17.30)|0.309 (0.112)|5.701|(4.79)|
|HPIUKt�2|-0.060 (0.148)|-23.86 (14.30)|0.056 (0.108)|3.142|(5.041)|
|FACxUKt�1|0.002 (0.002)|0.439 (0.183)|0.004 (0.002)|0.353|(0.113)|
|FACxUKt�2|0.003 (0.002)|0.413 (0.207)|0.009 (0.002)|0.241|(0.104)|
|Error variance�100|0.008|80.64|0.002|4|7.61|



Table 5: UK. Estimation output for MSIAH(2)-VAR(2). Standard errors in parantheses. 

31 

###### **Documents de Travail** 

280. D. Durant et L. Frey, “Une Première comparaison des droits à pension des ménages français et américains,” Avril 2010 

281. G. Bertola, A. Dabusinskas, M. Hoeberichts, M. Izquierdo, C. Kwapil, J. Montornès and D. Radowski, “Price, Wage and Employment Response to Shocks: Evidence from the WDN Survey,” May 2010 

282. J. Montornès and J-B. Sauner-Leroy, “Wage-setting Behavior in France: Additional Evidence from an Ad-hoc Survey,” May 2010 

283. R. Bourlès, G. Cette, J. Lopez, J. Mairesse and G. Nicoletti, “Do product market regulations in upstream sectors curb productivity growth? Panel data evidence for OECD countries,” June 2010 

284. Ph. Askenazy, Th. Breda and D. Irac, “Innovation and Advertising: Theory and Evidence,” May 2010 

285. M. Lemoine and C. Mougin, “The Growth-Volatility Relationship: New Evidence Based on Stochastic Volatility in Mean Models,” July 2010 

286. C. Bouthevillain and G. Dufrénot, “Are the effects of fiscal changes different in times of crisis and non-crisis? The French Case,” July 2010 

287. S. Avouyi-Dovi, D. Fougère and E. Gautier, “Wage rigidity, collective bargaining and the minimum wage: evidence from french agreement data,” July 2010 

288. P. Askenazy, C. Célérier et D. Irac, “Vente à distance, internet et dynamiques des prix,” juillet 2010 

289. G. Dufrénot, P. Frouté and C. Schalck, “The French Regions’ Borrowing Behaviours,” july 2010 

290. C. Bordes and L. Clerc, “The ECB art of central banking and the separation principle,” August 2010 

291. R. Jimborean and J-S. Mésonnier, “Banks' financial conditions and the transmission of monetary policy: a FAVAR approach,” September 2010 

292. G. Dufrénot and L. Paul, “Fiscal development in the euro aera beyond the crisis: some lessons drawn from fiscal reaction functions,” October 2010 

293. R. Cooper, H. Kempf and D. Peled, “Insulation impossible: monetary policy and regional fiscal spillovers in a federation,” October 2010 

294. C. Célérier, “Compensation in the financial sector: are all bankers superstars?,” October 2010 

295. O. de Bandt and S. Malik, “Is there evidence of shift-contagion in international housing markets?,” October 2010 

Pour accéder à la liste complète des Documents de Travail publiés par la Banque de France veuillez consulter le site : - <u>http://www.banque france.fr/fr/publications/documents_de_travail/documents_de_travail_10.htm</u> For a complete list of Working Papers published by the Banque de France, please visit the website: - <u>http://www.banque france.fr/fr/publications/documents_de_travail/documents_de_travail_10.htm</u> 

Pour tous commentaires ou demandes sur les Documents de Travail, contacter la bibliothèque de la Direction Générale des Études et des Relations Internationales à l'adresse suivante : 

For any comment or enquiries on the Working Papers, contact the library of the Directorate General Economics and International Relations at the following address : 

BANQUE DE FRANCE 49- 1404  Labolog 75049 Paris Cedex 01 tél : 0033 (0)1 42 92 49 55 ou 62 65 ou 48 90 ou 69 81 email : <u>jeannine.agoutin@banque-france.fr michaelbrassart@banque-france.fr veronique.jan-antuoro@banque-france.fr nathalie.bataille-salle@banque-france.f</u> 

