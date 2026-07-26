---
title: DIRECTION GÉNÉRALE DES ÉTUDES ET DES RELATIONS INTERNATIONALES
type: paper
source_pdf: raw/papers/Bandt. The_international_transmission_of_house.pdf
converted: 2026-07-26
---

# DOCUMENT 

# DE TRAVAIL 

# N° 274 

**THE INTERNATIONAL TRANSMISSION OF HOUSE PRICE SHOCKS** O. de Bandt, K. Barhoumi and C. Bruneau January 2010 



DIRECTION GÉNÉRALE DES ÉTUDES ET DES RELATIONS INTERNATIONALES 

#### DIRECTION GÉNÉRALE DES ÉTUDES ET DES RELATIONS INTERNATIONALES 

**THE INTERNATIONAL TRANSMISSION OF HOUSE PRICE SHOCKS** O. de Bandt, K. Barhoum and C. Bruneau january 2010 

Les Documents de travail reflètent les idées personnelles de leurs auteurs et n'expriment pas nécessairement la position de la Banque de France. Ce document est disponible sur le site internet de la Banque de France « <u>www.banque-france.fr ».</u> 

Working Papers reflect the opinions of the authors and do not necessarily express the views of the Banque de France. This document is available on the Banque de France Website “www.banque-france.fr”. 

## The international transmission of house price shocks<sup>�</sup> 

O. de Bandt,<sup>y</sup> K. Barhoumi,<sup>z</sup> and C. Bruneau<sup>x</sup> 

> �Many thanks to Jean Ludovic Audret for helping assemble the database. Comments by C. André and G. Perez-Quiros are gratefully acknowledged. All errors remain ours. The opinions expressed are not necessarily those of the Banque de France or the Eurosystem. 

> yBanque de France, E-mail olivier.debandt@banque-france.fr 

> zBanque de France, E-mail karim.barhoumi@banque-france.fr. 

> xBanque de France and University of Paris X, E-mail cbruneau@u-paris10.fr. 

###### **Abstract** 

In order to assess transmission mechanisms between global and domestic house prices, and possibly contagion effects, we use a large database of macroeconomic variables for OECD countries. We extract common factors to summarize the comovements of the variables and include them in stationary FAVAR models. We mainly focus on the "pandemic" view of contagion where local shocks, originating from a country or a local housing market, spread out to other domestic housing markets. An interesting finding is that, even allowing for other channels of international transmission (through global interest rates, or activity), the US real house price, which appears to be exogenous in the US dynamics, unidirectionally causes the international house price factor, which in turn causes the domestic real house price growth for several countries. The channels of contagion from the US appears therefore to be either direct, through house prices (in particular in the UK or Spain), or indirect through other variables. 

###### **JEL Codes** : G33, E32, D21, C41 

**Keywords** : housing, factor models, Vector Autoregressive model 

###### **Résumé** 

L’objectif de cet article est d’analyser à la fois les mécanismes de transmission entre les prix de l’immobilier nationaux et internationaux et la possibilité d’effets de contagion entre les marchés immobiliers des pays de l’OCDE. Notre approche consiste à extraire, à partir d’une base de données de taille importante, des facteurs communs qui résument les co-mouvements entre les différentes variables utilisées ; puis à les utiliser dans un modèle FAVAR. Nous accordons une attention particulière à une contagion de type « pandémique », lorsqu’un choc local provenant d’un pays ou d’un marché de l’immobilier local affecte ensuite le marché immobilier des autres pays. Un résultat important est que le prix immobilier des États-Unis, qui apparaît lui-même comme exogène, est la principale source qui affecte le facteur prix immobilier international et, par là, les prix immobiliers des pays individuels, malgré la présence d’autres facteurs tels que le taux d’intérêt ou l’activité. Par ailleurs, la transmission de la contagion à partir des États-Unis s’effectue soit d’une manière directe par le biais du prix de l’immobilier (en particulier le Royaume-Uni et l’Espagne), soit de façon indirecte à travers les autres variables. 

###### **Codes JEL** : G33, E32, D21, C41 

**Mots clés** : marché immobilier, modèles à facteurs, Modèle Vectoriel Autorégressif 

### 1 Introduction 

The run-up of the housing bubble as well as the housing crisis that erupted in the USA in the summer of 2006, followed by the crisis in the UK and the sharp fall in house prices in Ireland and Spain, have raised questions of possible international transmission of shocks across countries (Terrones and Otrok, 2004). Arguably, price adjustments in housing markets are slower than in …nancial markets, given the existence of transaction costs and the absence of full comparability across units, which di¤er in terms of services they o¤er, notably location. As a consequence, housing markets are generally viewed as "local" markets, plagued with idiosyncrasies, even if "local" economic fundamentals (city-based, regional, or national) may also be a key component of it (see, among others, Ortalo-Magne <u>and Prat, 2009,</u> for such a "spatial" asset pricing point of view). Nevertheless, the recent period provides, at face value, evidence in favour of correlation across markets. Several dimensions are possible. In the long run, quality-corrected house prices should equalize, within a given economic area as a result of population movements. This may imply leads and lags of a few years between markets. Here, we rather focus on short or medium run links across markets. 

Di¤erent explanations are possible of an international transmission of house price shocks. First of all, house prices maybe driven by fundamentals that are either real macroeconomic or …nancial variables (see Goodhart and Ho¤man, 2004 for the role of credit variables). If the cycles of fundamentals are correlated, and house prices are driven by fundamentals, then house prices are likely to commove. Second, news on house prices in some countries may lead investors to revise their expectations on house prices in other countries. Third, in open economy, house prices may be directly a¤ected by international fundamentals (world activity, global liquidity, world interest rates) that a¤ect global investors arbitraging across domestic house markets (see e.g. Kiyotaki, Michaelides and Nikolov, 2008 for a model of domestic house prices determined by the world interest rate). A …nal possibility, is that the channel of transmission is time varying, leading to possible "contagion e¤ects" in case of crisis, and notably global crisis : house price changes are more signi…cant under some circumstances, e.g. when prices are decreasing, or during a crisis Another de…nition of contagion, closer to the previous explanation, is also, as in the case of a "pandemic", the occurrence of a double interaction occur, i.e. when local prices in one region a¤ect global prices, which in turn in‡uence local prices in other regions. 

We investigate the existence of such interactions across countries, notably the link between macroeconomic fundamentals and the dynamics of house prices and the relevance of international comovements, using factor analysis. 

The plan of the paper is the following. Section 2 recalls the main principles of the econometric models we have selected to investigate the question of contagion, namely the FAVAR and the LSTAR models. In section 3, we present the data. The results are discussed in section 3, as well as the main steps of the empirical analysis. 

2 

### 2 Empirical methods 

Based on the two de…nitions we have given above for contagion, we rely on two di¤erent tools. Favar models, as well as methods to assess non linearities in the reaction of house prices, in particular LSTAR models. We now present them successively. 

##### 2.1 Favar models for the analysis of the transmission of house prices 

House prices in many industrial countries have increased unusually rapidly in recent years and in some cases these increases do not seem to be fully explained by economic fundamentals. The dynamics of house prices has indeed been mainly studied at the national level (Tatsanoris and Zhu, 2004), housing markets being viewed as "local" in nature. Goodhart and Ho¤man (2004) stress the need to extend the set of fundamentals to money and credit variables. In that context, the transmission across markets is mainly national, between local and regional markets. However, Del Negro and Otrok (2007) conclude that the early 2000s in the US were di¤erent from before, with a much larger contribution of national as opposed to state level components. 

In contrast, the analysis of international transmission of housing prices is less developed with the exception of Vansteekiste and Hiebert (2009) who use a Global VAR approach to study comovements of house prices in the euro area and conclude to limited spillovers across countries. Earlier, Terrones and Otrok (2004) had developed a systematic analysis of the dynamics of house prices across a larger number of industrial countries. They show that house prices are highly synchronized and that the house price boom that took place in the early 2000 was unusual in both its strength and duration. Innovative aspects of the analysis are the use of dynamic factor (DFA) models to determine the extent to which house price comovements are explained by global or country-speci…c factors and of FAVAR models (for Factor Augmented Vector AutoRegressive models), that combine country-speci…c variables with factors in VAR-type frameworks. 

Before developing the FAVAR-based analysis, the authors investigate the extent to which fundamentals explain the dynamics of house prices. They indeed …nd empirical evidence in favor of the dependence of house prices on economic fundamentals (real income growth, interest rates), besides a signi…cant contribution of the autoregressive component: house prices appear to be highly persistent with a signi…cant autocorrelation of order one. 

The factor analysis consists in extracting factors from di¤erent variables (not only the growth rate of house price, but also real stock returns, per capita output, per capita consumption, per capita residential investment, and changes in the short- and long-term interest rates) for 13 industrial countries, over the period 1980-2004. The methods allows to identify complementary factors, namely, a global factor, which a¤ects all variables in all countries, capturing the common shocks a¤ecting these variables, a global housing factor, a¤ecting all house prices in all countries, but not other variables, similarly, a global interest rate factor, capturing common shocks to global interest rates but not to other variables, and so on for each type of variable in the data base. 

Moreover, country-speci…c factor are estimated, re‡ecting the common shocks to the country-speci…c variables. 

3 

The results are that a large share (about 40 percent on average) of house price movements appears to be due to global factors, which re‡ect global co-movements in interest rates, economic activity, and other macroeconomic variables, which in turn result from common underlying shocks. The overall global factor a¤ecting all variables explains (on average) about 15 percent of movements in house prices, while the global housing factor— capturing global shocks to housing markets alone— explains —on average— 25 percent of house price movements, with a clear heterogeneity in the contribution of the common 

Our aim is to estimate the same type of FAVAR models from our data base described hereafter. We use a slightly di¤erent database and extend the sample to include the burst of the housing bubble. We implement a more robust approach to assess the additional explanatory power of international house prices : we …rst estimate country-by-country models of real house prices based on domestic macroeconomic fundamentals, based on the usual view that housing market are "local" (i. e. respond to regional or national determinants); we then consider whether international house prices, derived from common factors, help provide better models. 

In the following section we recall brie‡y how to build a FAVAR model, which may be of two types, and explain how we implement such a methodology in our case. 

1. Model FAVAR in the lines of Stock and <u>Watson (2005)</u> 

One considers a set of n vectors X1t; :::; Xnt with a factor dynamics. The matrix Xt may include in our case, house prices as well as other indicators (GDP, short and long interest rates, prices, housing investment, etc) for a large set of countries. 



The idiosyncratic components "it may be serially correlated, for example obeying an AR model of order p: 



Transforming the model as following: 



allows to get white residuals. The R factors ft = (f1t; :::; fRt)<sup>0</sup> are dynamic factors obeying an AR model too: 



Finally, 

4 



If �(L) is a polynomial matrix of order q � 1, one can de…ne the R<sup>e</sup> - dimensional factor Ft, R � R<sup>e</sup> � Rq as: 

Ft = (ft<sup>0; f</sup> t<sup>0</sup> �1<sup>; :::; f</sup> t<sup>0</sup> �(q�1)<sup>)0</sup> 

such that: 



or, equivalently, in a VAR-type framework: 



It is worth emphasizing that the past values of the i<sup>th</sup> component do not directly in‡uence the dynamics of the j<sup>th</sup> component (j = i) because the lag operator D(L) is diagonal. 

The in‡uence of the i<sup>th</sup> component on the j<sup>th</sup> component (j = i), if it exists, is indirectly transmitted through the factors. 

The previous FAVAR model appears to be a constrained VAR model. It is di¤erent from the FAVAR models estimated by <u>Bernanke et al (2004),</u> or Del Negro and Otrok (2005) who do not impose constraints on the autoregressive parameters. 

2) The FAVAR model by <u>Bernanke et al. (2004)</u> 

The idea underlying the FAVAR models estimated by <u>Bernanke et al.(2004)</u> is the following: if a small number of estimated factors e¤ectively summarize large amounts of information about the economy, then a natural solution to the degrees-of-freedom problem in VAR analyses - which have to be of limited dimensions- is to augment standard VARs with estimated factors. 

One considers a M � 1 vector Yt of observable economic variables of interest, namely in our case, domestic macro variables (GDP, housing prices, short and long interest rates, 

5 

housing investment, etc.) for a given country. One assumes that additional economic information, not fully captured by the Y series, may also be relevant to modeling the dynamics of these series. More precisely, one assumes that this additional information can be summarized by an K � 1 vector of unobserved factors, F , where K is “small”. 

The joint dynamics of (Y; F ) is given by: 



with vt denoting a white noise process. 

The previous model provides a way of measuring the contribution of the additional information contained in the factors Ft. Besides, if the true system is a FAVAR, the estimation of a VAR model for Y , with the factors omitted, may lead to biased estimates of the VAR coe¢cients and the associated impulse response coe¢cients. 

The FAVAR model cannot be estimated directly because the factors Ft are unobservable. However, as the factors represent forces that potentially a¤ect many economic variables, one can suppose that it is possible to infer something about the factors from observations on a variety of economic “informational” time series, denoted by a N � 1 vector Xt . This includes house prices in other countries which may a¤ect domestic house prices. The number of informational time series N is “large” , generally assumed to be much greater than the number of factors (K + M << N ) and the series Xt are related to the unobservable factors Ft and the observable factors Yt by: 



where �<sup>f</sup> is an N � K matrix of factor loadings, �<sup>y</sup> is N � M , and the N � 1 vector of error terms et are mean zero and are assumed either weakly correlated or uncorrelated, depending on whether estimation is obtained by principal components or likelihood methods. 

Indeed, the model can be estimated in a two-step principal components approach or a single-step Bayesian likelihood approach. 

In the two-step procedure, (Ft; Yt) is estimated using the …rst K + M principal components of Xt .<sup>1</sup> . 

In the second step, a FAVAR model is estimated by standard methods, with Ft replaced by F<sup>b</sup> t . However, to account for the uncertainty in the factor estimation, it is generally recommended to implement a bootstrap procedure, in order to obtain accurate con…dence intervals on the impulse response functions deduced from the FAVAR, except if N is large enough relative to T . 

> 1 The estimation of the …rst step does not exploit the fact that Yt is observed. However, as shown in Stock and Watson (2002), when N is large and the number of principal components Ct used is at least asby largeboth asFt theandtrueYt . numberFbt is obtainedof factors,as thethe partprincipalof thecomponentsspace coveredconsistentlyby the componentsrecover theCspacet thatspannedare not covered by Yt, tanks to a speci…c identifying assumption used in the second step. 

6 

##### 2.2 Non linear single equations : the STAR model and the LSTAR speci…cation 

In order to detect possible regime shifts that can be associated with contagion, we rely on non linear speci…cations. 

###### 2.2.1 The STAR model 

Such a model is written as: 



with F (Zt; �; s) = [1 + exp(��(Zt � s))]<sup>�1</sup> 

Y is the endogeneous variable, X denotes (jointly) the lagged endogenous variable and an exogenous variable and Z the transition variable. In what follows, the exogenous variable is also the transition one 

Equivalently, the model can be written as: 



0 0 with �10 = �<sup>(1)</sup> 0<sup>;�</sup> 1<sup>= �(1)0;�20= �(2)</sup> 0 � �<sup>(1)</sup> 0<sup>; �</sup> 2<sup>= �(2)0��(1)0</sup> f� = 0g indicates that Yt is a linear process: 



Accordingly, Teräsvirta (1994) test the linear model against the non linear model by implementing the test: H0:f� = 0g against H1:f�> 0g 

He propose to implement a LM test, after solving out the identi…cation problem due to the fact that the parameters �20, �2 and s are not identi…ed under the null hypothesis. 

There are two usual choices of the transition function which lead to the LSTAR and the ESTAR models. 

###### 2.2.2 The LSTAR speci…cation 

The transition function is the logistic one, de…ned as: 



�If Zt < s and jZt - sj tends to in…nity, the transition function tends to 0 and the process Yt is characterized by: 



which corresponds to the …rst regime. 

� If Zt > s and jZt - sj tends to in…nity, the transition function tends to 0 and the process Yt is characterized by: 



7 

which corresponds to the …rst regime. 

Intermediate values of the transition variable implies a combination of both "regimes" in the dynamics of Y: 

The transition speed depends on the parameter �. If � tends to in…nity,one …nds an AR speci…cation with varying coe¢cients, depending on the impact of a dummy variable indicating a crisis event. 

Note that there is another usual speci…cation of the transition function: the exponential one corresponding to the de…nition: 



Thus, if jZt � sj is large, whatever the value of Zt compared to s, F tends to 1 and the dynamics of Yt is described by: 



On the contrary, Zt is near from the threshold s, la fonction F tends to 0 and the dynamics of Yt obeys: 



In what follows, we prefer to validate a LSTAR model, with two regimes - a normal one and a critical one- respectively associated with a low and an high value of the transition function compared to the threshold. Thus the LSTAR speci…cation allows an easier interpretations of the regimes from an economic point of view. 

The statistic procedure is as follows. First, the maximal lag order of the AR model is chosen by using the AIC criterion. Next, linearity is tested against non linearity. 

At a third step, one has to validate the LSTAR against the ESTAR speci…cation. Finally, one estimates the parameters of the LSTAR model. 

In the following sections, we build on the FAVAR literature by considering a slightly di¤erent set of house prices (for 15 OECD countries). We proceed in two steps. First, we extract common factors. We estimate these common factors from our database including house prices only. Following <u>Stock and Watson (2005),</u> we consider that the factors can be written in a VAR format. In a second step, we include our common factors into VAR systems for each country. These FAVAR models are estimated with real house prices in the country, as well as other domestic macroeconomic variables (interest rates, GDP, in‡ation, etc) and the common house price factors. We also test whether the relationship is non linear by estimating by estimating, extended AR-type model including dummies indicating crisis events or LSTAR model. 

### 3 Data 

As indicated before, the analysis concentrates on house prices, but we also used data for the real economy, using OECD quarterly national accounts (households’ investment, consumption prices, 3-month and 10-year interest rates). We exclude non residential investment (i.e commercial real estate, like o¢ces, warehouses, etc.). For house prices, 

8 

several database are available, either from the OECD or the BIS. In order to consider a larger (i. e. more recent) sample we rely therefore on national data on house price and checked whether are consistent with the data assembled by the OECD. We use data on Australia, Canada, Switzerland, Finland, France, Germany, Ireland, Italy, Japan, Netherlands, Norway, New Zealand, Spain, United Kingdom, United States, hence a total of 15 countries. It turned out that they are very close to the OECD for the period starting in 1980. We concentrate therefore on the period from 1980Q1 to 2008Q4, where the data are the most reliable. Series were seasonally adjusted. Based on the house price data for 15 countries, we constructed common factor using the Stock&Watson (1999)’s approach, after demeaning and standardizing the quarterly growth rates on nominal prices. The common factors are called fac1;t, fac2;t, etc for the …rst two factors. We also computed two world indices of nominal house prices, based on a geometric average of national house prices, the …rst one being unweighted, the second one weighted by the share of the country in world GDP. As indicated in Figure 1, the …rst factor is very close to the quarterly growth rate of the unweighted index. 

###### [ INSERT FIGURE 1 HERE] 

### 4 Modelling approach and empirical results 

To assess the likelihood of contagion e¤ects, we have considered two di¤erent de…nitions as mentioned before. According to the …rst de…nition, contagion occurs when the transmission is di¤erent, in particular more pronounced, during crisis events. This implies to investigate whether the results are di¤erently a¤ected across subsamples. In the second approach, we investigate whether global shocks, initially originating at the local level, spread out to other domestic housing markets. 

In both cases, the main objective is to investigate whether common factors have an e¤ect on domestic real house prices. We consider both linear and non linear models and di¤erent information sets, depending whether we extract common factors from a database including housing prices only, or whether we use a more complete database, in order to uncover other channels of transmissions of housing shocks. 

When we refer to the …rst de…nition of contagion, we estimate non linear single equations including dummies indicating crisis events or describing a smooth transition process according to a LSTAR speci…cation. Thus, the factor which is included as the transition variable is extracted from the whole data set (excluding the house prices) or is one of the factor extracted from the house prices only. 

For the second de…nition, we estimate FAVAR models for the di¤erent countries, with the factor extracted from the set of house prices only. In this case the transmission channel of contagion is exclusively based on the house prices. 

We start the analysis by adopting a simple single equation approach, where we explain the real house price growth by lagged values of domestic fundamentals -nominal interest rate and in‡ation rate- and lagged values of factors extracted from international house prices only. The regressions are thus linear; then, we introduce non linearity in two ways: 

9 

…rst, by introducing dummies indicating crisis periods, second, by looking for regimes and smooth transition mechanisms from a LSTAR speci…cation. 

##### 4.1 Univariate linear models 

We …rst estimate univariate models, using the General-to-Speci…c approach, as available in the Grocer software, by including factors extracted from the house prices only. 

###### 4.1.1 Linear single equations for each country 

We …rst estimate, for each country, a model with the autoregressive component, as well as domestic fundamentals (in‡ation, GDP growth with an expected positive impact, interest rates with an expected negative impact). We then add the …rst two common house prices based factors (fac1;t, fac2;t)<sup>2</sup> and test whether the factors have additional explanatory power. Notice that all time series are stationary in growth rates (real house prices, consumption de‡ator), as clearly indicated from unit root tests. The only exception is for the US, which is a more borderline case since only KPSS tests do not reject I(0) for the growth rate of real house prices. 

We have alternatively tested the factor lagged by one quarter or contemporaneously (but do not present the latter results to save space)<sup>3</sup> . 

The results are exhibited in Table 1 in Appendix. In all cases, it turns our that the best models, as selected by the General-to-Speci…c approach, include one-period lagged variables, for domestic fundamentals as well as for factors. All models end up including fundamentals (interest rate or in‡ation) , except for Australia and UK. A positive and signi…cant coe¢cient associated with fac1;t�1 means that increases in international house prices have a positive spillover on domestic prices.<sup>4</sup> 

Two groups of countries can be distinguished: 

- Australia, Spain and the UK, where the …rst common factor has a signi…cant e¤ect (at the level of 10%); 

> 2 Note that in order to avoid spurious correlations, when regressing a country house price on the common house price factor, we exclude the country’s price from the database of international house prices. As a result, fac1 should actually be written as fac1<sup>iforcountryiwhenconsideringthe…rstcommonfactor</sup> extracted from the database of all house prices excluding country i<sup>0</sup> s house price. fac1<sup>ienters all regressions</sup> involving country i, for example, fac1<sup>usa</sup> in the particular case of the USA. Even if it turns out that such a di¤erence is not very signi…cant, as shown in Figure 2 in Appendix ( fac1<sup>i' facj</sup> 1<sup>' fac</sup> 1<sup>all</sup> for all i = j, with fac1<sup>all</sup> the …rst common factor from the database of all house prices), using fac1<sup>iinsteadoffacall</sup> 1 provides more robust results. 

> 3 To avoid spurious correlations, the factors are computed for each country on a database of 14 countries, i.e. the 15 initial countries after exclusion of the country under study. As shown in Figure 2, the …rst common factors computed for the restricted database (ie with 15 instead of 14 countries) is quite close to the one computed from the whole database of 15 countries. 

> 4 Note that factors are estimated but this is not taken into account for statistical inference on the ground that they are e¢ciently estimated in the …rst (factor extraction) step. This is also consistent with Bernanke, Boivin and Eliasz (2005) who show that two-step Favar analysis yields very similar results to one step analysis. 

10 

- the other countries, namely USA, Germany, France and Ireland, where real house prices can be explained by domestic fundamentals only. 

The level of the interest rate (it�1) is associated with a signi…cantly negative coe¢cient for France, Germany, Ireland. However, when measured in …rst di¤erence (�it�1), in order to account for its persistence, it is no longer signi…cant .The coe¢cient of the (lagged) in‡ation rate is signi…cant only in the case of Germany. 

As announced before, we introduce dummies to account for crisis periods and we examine the robustness of the previous results to crisis events. 

###### 4.1.2 Robustness to crisis events 

In order to assess the robustness of the previous results to changes in the transmission mechanism of international house prices during speci…c events, notably crisis, we now test whether the sensitiveness is time varying. This is a measure of contagion of house prices, as we expect domestic prices to react more signi…cantly to international house prices during crisis periods. Here we test therefore 



where du_crisett is a dummy variable that takes the value of 1, during a crisis and 0 otherwise. Under such a speci…cation, �3I measures the di¤erential impact of the crisis on domestic house crisis. Testing for contagion implies rejecting the null hypothesis H0 : �3 = 0 vs H1 : �3 > 0: 

We need therefore to de…ne du_crisett: We use for that the de…nition of crisis in the World Economic Outlook, April 2009 (based on Rogo¤ and Reinhart, 2008), which provides the recession periods, associated with …nancial crisis. When at least one OECD country is in recession, the indicator is equal to one. An alternative index, would measure the proportion of countries in recession. We update such an index by introducing a recession period as from 2008Q2. The index appears in Figure 7 in Appendix. 

It turns out that for 4 countries, namely Australia, Spain, Ireland and United Kingdom, (See Appendix, Table 2), �2 is not statistically di¤erent from zero, while �3 is signi…cantly negative. This should be interpreted (given the normalization of the housing factor) as a stronger positive elasticity of domestic house prices to international house prices during a …nancial crisis period. 

Next, we extend the linear models by introducing factors extracted from a larger data base including prices, interest rates, GDP among other variables. 

###### 4.1.3 Transmission through other macroeconomic variables 

We now use the full database described in the data section to compute common factors with a view to consider various transmission channels of house price changes. Several alternatives are possible. Either we extract factors from the whole database of housing and macroeconomic variables. Or we consider subsamples of the variables. According to the …rst approach, we get orthogonal factors, and it is possible to constrain them in order 

11 

to identify these factors.<sup>5</sup> However, factors are linear combination of the variables and maybe di¢cult to interpret. This would argue in favour of the second approach, on which we focus here. We adopt therefore a three steps procedure. First, we extract 3 common factors from a larger database excluding the house prices. Secondly, we identify the factors (Glob1_price, Glob2_price and Glob3_price). Finally, we estimate for each country the appropriate model, by using one of these "global" factors or a factor extracted from the house prices only as in previous section. 

It turns out that the factors that we estimate from that extended database have a direct economic interpretation. As shown in Figure 3 to 5, the …rst factor of the database excluding house prices, denoted Glob1_pricet�1;is correlated with interest rates and captures the remaining non-stationarity in the database. The second factor, denoted Glob2_pricet�1is correlated with GDP growth. The third factor is an activity speci…c factor as it appears to be quite close to the world Output Gap. In contrast, when the factors are extracted from a complete database with interest rates in …rst di¤erences, but after exclusion of in‡ation, the …rst common factor is closely related both with the common house price factor as well as the Glob2_price common activity factor (see Figure 6). This con…rms our choice to concentrate on the common house price factor and Glob2_price in the remainder of the paper 

In Table 3, we present the results from the estimation of the same type of univariate regressions as in Table 1. The …rst factor is never associated with a signi…cant coe¢cient except in the case of Ireland. The second factor has now a negative impact in Australia but positive in Spain. The housing factor remains signi…cant in Australia and the UK. 

It now becomes signi…cant in the case of France, as from the new set of candidate regressors, Grocer selects a model with international house factor fac1;t.as the only regressor on top of the autoregressive component. 

Now we examine whether the dynamics could have di¤erent features depending on di¤erent regimes, by estimating LSTAR models. 

##### 4.2 LSTAR models 

When estimating the LSTAR models, we limit us to …ve countries at this step of the analysis, namely France, Germany, Spain, UK and USA. The investigation will be further extended to the other countries. We run through the di¤erent steps and …nd di¤erent transition variables, namely Glob1_prices for Spain and UK, Glob2_prices for France and Glob3_ prices for the USA. As indicated above, these factors can be interpreted, respectively, as a global interest rate, the growth rate of global GDP in OECD countries, the (inverted) lagged annual growth rate of GDP. 

In the following table, we summarize the main results about the instantaneous impact (denoted correlation) of the global factor which is also the transition variable. We just focus on the contemporaneous impact of the global factor. Indeed, it has its own dynamics, which cannot be characterized from the single equation which describes the dynamics of the endogenous variable (the house price). The MA type speci…cation obtained by 

> 5 See Kose, Otrok and Whiteman (2003), Del Negro and Otrok (2007). 

12 

inverting the AR type model including X (and Y ) involves an in…nite number of lags of the exogenous variable (that is the global factor). But contrary to standard impulse response analyses, one cannot consider any shock on the lagged values of the global factor as past innovations. The di¤erence comes from the intertemporal correlations between the di¤erent lags of the global factor. 

The results are summarized in Table 4 in the Appendix. 

The …rst result is that non linearity is clearly validated only for two countries, Spain and UK. In both cases, the two regimes are de…ned by the level of world interest rates: high level of interest rates versus low level. One observes a negative correlation between the level of world interest rates and the …rst di¤erences in log (real) house prices in these 2 countries. The negative coe¢cient is stronger when interest rates are low. 

For France and the USA, house prices respond to the world GDP cycle, but the results may be seen as a bit suspicious, since non linearity is borderline (the log- likelihood of the model with two regimes is not very di¤erent from the model with one regime only). For the USA, we observe a positive correlation between the output gap and the …rst di¤erence in log (real) house price with a higher correlation in expansion periods. House prices are therefore more sensitive to the world output gap when the latter is very positive, than when it is negative. For France, we …nd a positive (respectively negative) correlation between (contemporaneous) world GDP growth rate and the change in Log real house prices, in expansion periods (respectively recession) periods. For both countries, USA and France, house prices would therefore tend to respond more to activity in the upswing than in the downswing. One can conjecture that other factors than activity, notably …nancial variables, may explain the adjustment of prices in the downswing. 

In any case, it is not easy to interpret one or the other regime as a crisis regime. For Spain and UK, one could claim that the low level of interest rate is explained by lower risk premia, and accordingly, the corresponding regime could be viewed as a "critical" state. Thus we could conclude that we have …nd evidence of contagion, according to our …rst de…nition for both countries. We may rather conclude that we have actually identi…ed a more "speculative" behavior of housing markets in the second subperiods, with sharper reactions of house prices to interest rates. 

To summarize, at this stage of the analysis, the LSTAR approach does not provide a clear conclusion in terms of contagion e¤ects. Moreover, the analysis we have proposed up to now should be considered as a simple investigation preceding the multivariate analysis. Indeed, we will observe that the linear speci…cation of the equation describing the dynamics of the real house price growth rate is dramatically changed inside a FAVAR model, which tends to prove that the regressors of the single equations are not exogenous. 

In what follows, we focus on the multivariate analysis involving all factors extracted previously (including the …rst factor extracted from international house prices only) except the …rst global factor, which we drop because of its high persistence. However, as it is strongly related to interest rates, we decide to systematically include a national long term interest rate in the FAVAR models, after di¤erencing this variable to insure its stationarity. 

13 

##### 4.3 FAVAR models and causality analysis 

In this section, we present the results we have obtained for each country of the panel, by estimating a FAVAR model. It is worth emphasizing that we do not have any tool which allows us to choose the best FAVAR model. Our General-to-Speci…c approach, carried out through GROCER, in order to select the best speci…cations of the single equations for all countries, cannot be used in the VAR context. 

We postulate a special role for the USA and look whether the American housing market can trigger contagion channels to the rest of the world. We check that it is indeed the case using causality tests. The numerical results are detailed in Appendix. 

For the USA, we include three factors, fac1, Glob2_price and Glob3_price, on top of the domestic long term interest rate and house price growth rate. This allows to shed light on the maximum number of transmission channels. Indeed, according to our "pandemic" view of contagion once a factor is in‡uenced by one (or two) of the local variables, it can be associated with a contagion mechanism of a shock originating from the local house market or interest rate. Moreover, it is worth examining whether contagion e¤ects involve the house markets only or more global activity channels. 

For the other countries we limit the FAVAR model to four components, the interest rate, the real house price growth and two factors, the house price factor fac1 and Glob2_price or Glob3_price, depending on the country. 

Due to the limited number of observations, we aim at limiting the order of the FAVAR models. However, the persistence of the factors obviously increases the autoregressive order of the models. We test therefore di¤erent types of models, which mainly di¤er in terms of lags and estimation method and check the consistency of the results.<sup>6</sup> 

More precisely, our strategy is the following: 

First, as causal links can be measured equation by equation in a VAR model, we estimate FAVAR models with lower orders (see Tables 5 to 9 in Appendix), because it is easier to get white noise residuals from single equations taken separately and for which we test causality. To make sure that the results are not biased by persistence e¤ects, we increase the order of the FAVAR models, when necessary, as proposed by <u>Toda and Yamamoto (1995)</u> and Dolado and Lütkepohl (1996) for implementing causal analyses in non-stationary VAR models, without preliminary cointegration analyses. But this latter step does not seem to be necessary, as proved by the features of the generalized impulse responses which returns to zero after a su¢cient number of periods (about 36). 

Second, for each country, we estimate a FAVAR model of high order (about 12) in order to obtain residuals which de…ne a vectorial (weakly) white noise. Thus, we deduce from this FAVAR a system of equations, so as to limit the number of parameters to estimate: we just keep the regressors associated with signi…cant coe¢cients, by still checking that the residuals are white noises. This system is reestimated with a SUR estimation method. Then causal links are measured through the system. 

> 6 We also computed impulse responses, based on bootstraping using JMulti (see Lütkepohl and Krätzig, 2004). The results are quite similar across methods and con…rm the positive impact of the common factor on domestic house prices. 

14 

As mentioned before, both kinds of analyses provide rather close results about causal links. We decide to keep as "certain" the causal links jointly identi…ed through both analyses. 

It is worth emphasizing that the domestic interest rates and house price growth rates are both exogenous in the American model and in this model only. Moreover the house price factor (fac1) is unidirectionally caused by these two variables. Accordingly, one can imagine "exogenous" shocks impacting the American interest rates or the (real) house price growth rate and one can be sure that these shocks will a¤ect the (world) house price factor fac1. A second main result ,obtained from the FAVAR approach, is that the house price factor causes systematically the local house price growth for 5 of the 7 countries under review at the usual signi…cance level of 5% (See Table 9 in Appendix, 7% for Australia). The other two countries are Ireland and Germany. In the case of Ireland, the growth rate of real house prices appears to be exogenous in the FAVAR model of limited order estimated for that country (see Table 7 in Appendix). Moreover, it is worth noticing that, in the case of Germany, causality from the house price factor fac1 to the domestic house price growth rate is indirectly transmitted by the global factor Glob3_price, for which one cannot reject a causal link from fac1 (see Table 8 in Appendix). However when causality is investigated from systems of equations, we …nd strong evidence of causality from the house price factor to each domestic house price growth rate (See table 11 in Appendix) .Moreover in the second approach, exogeneity of both domestic variables (house price growth and interest rates) is con…rmed as well as causality from the domestic variables to the house price factor (See Table 10 in Appendix). 

These results tend to prove that contagion may occur from the USA house price market to all other house markets. One can also imagine contagion mechanisms for shocks originating from the American interest rate, which is an interesting …nding, if one refers to the recent subprime crisis, which was revealed after the increase in interest rates, which indeed took place in 2006. Accordingly, we could develop a stress test exercise replicating this increase in interest rate in order to examine its impact on all house markets and more generally on the global activity factors. 

### 5 Conclusion 

We have investigated contagion e¤ects among house prices across industrial countries by extracting factors and including these factors in linear multivariate models or non linear single equations, depending on the de…nition of contagion we have retained. 

We have introduced two di¤erent de…nitions of contagion. According to the …rst de…nition, contagion occurs when the transmission is di¤erent during crisis events. In the second approach, contagion is viewed as a "pandemic" transmission mechanism where local shocks, originating from a country or a local housing market, spread out to other domestic housing markets. 

In both cases, the main objective was to investigate whether common factors have an e¤ect on domestic house prices, through non linear equations for the …rst de…nition and FAVAR models or systems of equations derived from them, for the second one. 

15 

More precisely, referring to the …rst de…nition of contagion, we have estimated non linear single equations including dummies indicating crisis events or describing a smooth transition process according to a LSTAR speci…cation. In the latter case, the factor included as the transition variable has been extracted from the large data set, which provides three factors, mainly correlated to interest rates and activity. We have thus observed non linearity in the dynamics of two countries (Spain and UK), but the results we obtain are not very conclusive at this stage, given the small sample size, the two regimes correspond to two subperiods of high, respectively low interest rates, with the break occurring in the mid-1990’s. It is di¢cult to interpret them as a "normal" versus a "critical" regime. For France and the USA we provide evidence that the sensitiveness to the business cycle is more pronounced in the upswing than in the downswing, although non-linearity is less signi…cant. Thus, results obtained from this approach should be considered as preliminary and further completed. 

According to the second de…nition, we have focused on multivariate dynamics. 

Thus we have included factors, …rst extracted from international house prices only, second from a larger database, as components of a VAR model, on top of indicators of domestic economic fundamentals (namely, the growth of real house prices and the interest rates). When the factors are only derived from house prices speci…c, we provide evidence on the role of the common house price factor in the group made of the UK, Australia, Ireland and Spain, which means that contagion may occur, transmitted by a common component made of house prices. 

In the broader approach, allowing many channels of global transmission of shocks, including house price speci…c as well as global factors, an interesting …nding is that the US house price, which appears to be "independent" in the US dynamics, that is, not caused by any other variable, causes the international house price factor, which in turn causes the domestic house price of many other countries,within the associated model. This tends to prove that a local shock originating from the US housing market can spread out to the other domestic housing markets and that the most direct transmission channel seems to involve house markets only. 

16 

### References 

- " - 

- [1] <u>Ben S. Bernanke, Jean Boivin and Piotr Eliasz ( 2004), Measuring the e¤ects of mon etary policy:a factor augmented vector autoregressive (FAVAR) approach", NBER Working Paper 10220,http://www.nber.org/papers/w10220 and Quarterly Journal of Economics, February 2005.</u> 

- [2] <u>Beltratti, A and C. Morena (2009)</u> "International <u>House Prices and macroeconomic ‡uctuations", Forthcoming Journal of Banking and Finance.</u> 

- [3] <u>Dolado,J. J. and H. Lutkepohl. Making wald tests work for cointegrated var systems. Econometric Reviews, 15 :369–386,</u> 

   <u>1996.</u> 

- [4] <u>Del Negro, M. and C. Otrok (2007)</u> "99 <u>Luftballons: Monetary Policy and the house price boom across US states" Journal of Monetary Economics, 54, 1962-1985.</u> 

- [5] <u>Goodhart, C. and B. Hofmann (2008)</u> "House <u>prices, money, credit and the macroeconomy", Oxford Review of Economic Policy, vol. 24(1), 180-205</u> 

- [6] <u>Kiyotaki, N., Michaelides, A. and Nikolov, K. (2008) "Winners and Losers in Housing Markets", mimeo.</u> 

- [7] <u>Kose, A., Otrok, C.and C. Whiteman (2003),</u> “International <u>Business Cycles: World, Region, and Country-Speci…c Factors,” American Economic Review, Vol. 93 (Septem-</u> – 

- <u>ber), pp.1216 39.</u> 

- [8] Kose, A., Otrok, C.and C. Whiteman (1998),“Bayesian Leading Indicators: Measuring and Predicting Economic Conditions in Iowa”, International Economic Review, Vol. 39, No. 4, pp. 997–1014. 

- [9] <u>Lütkepohl, H. and M. Krätzig (2004) Applied Time Series Econometrics, Cambridge University Press.</u> 

- [10] <u>Ortalo-Magne, F. and Prat, A. (2009)</u> "Spatial <u>asset pricing : a …rst step", Mimeo.</u> 

- [11] <u>Stock, J.H. and M.W. Watson (2005), "Implications of dynamic factor models for VAR analysis", NBER, Working Paper n</u><sup>�</sup> <u>11467, http://www.nber.org/papers/w11467.</u> 

- [12] <u>Tatsaronis, K. and H. Zhu (2004) "What drives housing price dynamics: cross-country evidence", BIS Quarterly Review, March, 65-78.</u> 

- [13] Terrones, M. and C. Otrok (2004), “The global house price boom”, IMF, World Economic Outlook, September. 

- [14] <u>Toda, H. Y. and T. Yamamoto. Statistical inference in vector autoregressions with possibly integrated processes. Journal of Econometrics, 66 :225–250, 1995.</u> 

17 

- [15] Vansteenkiste, I. and P. Hiebert (2009) "Do house price developments spill over across euro area countries : evidence from a Global VAR", European Central Bank, Working Paper, 1026. 

18 

### A Single equation approach 

|Table 1:|Country Sin|gle Equation|s (1983:1-200|8:4)|
|---|---|---|---|---|
|Country|�Log(p<sup>r</sup><br>h;t�1<sup>)</sup>|�it�1|�Log(pc;t�1)|fac1;t�1|
|Australia|0.54 (5.16)|||0.002 (1.86)|
||R<sup>2</sup>=<br>|0.37<br>|||
|Germany|0.65(7.50)|0.001 (0.31)|0.40 (4.01)||
||R<sup>2</sup>=<br>|0.36|||
|Spain|0.49 (2.71)||0.19 (0.75)|0.004 (1.88)|
||R2=<br>|0.52<br>|||
|France|0.50 (4.16)|0.001 (0.40)||0.001(1.47)|
||R<sup>2</sup>=<br>|0.30<br>|||
|Ireland(*)|0.30 (4.09)|0.28 (2.96)||0.000(0.78)|
||R2=<br>|0.25|||
|United Kingdom|0.53 (4.85)|||0.004 (2.75)|
||R2=<br>|0.57<br>|||
|United States|0.90 (13.24)|�0.01 (-0.91)||0.001 (0.13)|
||R2=<br>|0.80<br>|||
|(*) we re|port here the lag|ged endogenous v|ariable at t-2 and|t-3.|
|Student t (exhibit|ed in parenthesis)|are based on Ne|wey-West HAC st|andard errors|



NB: �Log(p<sup>h</sup> r;t<sup>)isthedomesticrealhouseprice,itisthedomesticshorttermnominalinterestrate,</sup> �Log(pc;t) is the quarter-on-quarter domestic in‡ation rate computed with the consumption de‡ator. fac1;t is the …rst common factor from the international house price database. 

Table 2: Country Single Equations (1983:1-2008:4) 

|Country|�Log(p<sup>r</sup><br>h;t�1<sup>)</sup>|�Log(p<sup>r</sup><br>h;t�2<sup>)</sup>|�Log(p<sup>r</sup><br>h;t�3)|du_crisist�fac1;t�1|other|
|---|---|---|---|---|---|
|Australia|0.59 (5.26)|||0.004 (2.64)||
||R2=|0.44||||
|Spain|0.67 (5.12)|||0.003(1.60)|0.22 (1.39)|
||R2=|0.49|||(�Log(pc;t�1))|
|Ireland||0.32 (3.50)|0.21 (2.32)|0.006(1.88)|-0.003 (-0.82)|
||R2=|0.27|||(�it�1)|
|UK|0.56 (6.55)|||0.008 (4.64)||
||R2=|0.57||||
|||See Ta|ble 1 for details|||



19 

Table 3 : Country Single Equations with <u>global</u> factors <u>(1983:1-2008:4)</u> 

|Country|�Log(p<sup>r</sup><br>h;t�1<sup>)</sup>|Glob1_pricet�1|Glob2_pricet�1|Glob3_pricet�1|fac1;t�1|
|---|---|---|---|---|---|
|Australia|0.55 (4.92)||-0.002 (-2.54)||0.004 (2:84)|
||R2|=0.46||||
|Germany|0.35 (3.60 )|||-0.006 (-2.31 )||
||R2|=0.28||||
|Spain|0.53 (4.42 )||0.0021 (2.42 )|||
||R2|=0.48||||
|France|0.47 (3.60 )||||0.002 (1.94 )|
||R2<br>|=0.32<br>||||
|Ireland|0.24 (1.57)|-0.001 (-2.11)||||
||R2<br>|=0.13||||
|United Kingdom|0.50 (5.98)|||0.001 (1.96)|0.004 (3.39)|
||R2|=0.58||||
|United States|0.94 (14.10)||-0.001 (-0.52)|||
||R2|=0.84||||
|Student t|(exhibited in par|enthesis) are based|on Newey-West HA|C standard errors||



Table 4: Summary of the results obtained from LSTAR models 

||regime 1||regime 2||
|---|---|---|---|---|
|ES|Glob1 <�0:08|low interest rates (crisis)|Glob1 >�0:08|high interest rates|
||�0:675|stronger <0 corr.<br>with int. r.|�0:325|<0 corr. with int. r.|
|USA|Glob3 <0:11|high Output GAP|Glob3>0:11|low Output GAP (crisis)|
||�0:38|stronger >0 corr. with GAP|�0:08|>0 corr. with GAP|
|FR|Glob2 <�0:058|low contemp.<br>�<br>GDP|Glob2 >�0:58|high contemp.<br>�<br>GDP|
||�0:41|<0 correlation|0:29|>0 correlation|
|UK|Glob1 <0:11|low interest rates (crisis)|Glob3>0:11|high interest rates|
||�0:60|stronger <0 correlation|�0:20|<0 correlation|



� where GDP is quarterly GDP growth 

20 

### B CAUSALITY in FAVAR models of reduced orders 

The models include the growth of real house prices, the …rst di¤erence of the long term nominal interest rate and several common factors : fac1 (housing factor),Glob2_price and Glob3_price. The order is chosen in order to get white noise residuals, equation by equation. 

In the following tables, the maximum number of lags is given in parenthesis in column 1, row 1. Causality tests are run from the variables in the …rst column to the variables in the …rst row. P-values of the Chi-square test statistic are reported. 

<u>Table 5: USA</u> 

|USA/FAVAR(7)|House price growth|D(interest rate)|Fac1 (house price)|Glob2_price|
|---|---|---|---|---|
|House price growth|���|0:4067|0:0186|0:0938|
|D(interest rate)|0:9345|���|0:0287|0:6848|
|Fac1(house price)|0:6717|0:9833|���|0:0232|
|Glob2_price|0:5180|0:5070|0:7633|���|



Comments: for the USA, real house price growth and the …rst di¤erence of the interest rate are exogenous; and they unidirectionally cause the house price factor (fac1) and also the global factor Glob2, with a weaker causal link between real house price growth and the Glob2 factor. 

<u>Table 6: France</u> 

|FRANCE/FAVAR(6)|House price growth|D(interest rate|Fac1(house price)|Glob2_price|
|---|---|---|---|---|
|House price growth|���|0:1188|0:0018|0:8883|
|D(interest rate)|0:0617|���|0:1169|0:0414|
|Fac1(house price)|0:2206|0:0109|���|0:0053|
|Glob2_price|0:8456|0:0001|0:9766|���|



Comments: Evidence of indirect causality from the house price factor fac1 to real house price growth through the interest rate 

###### <u>Table 7: Ireland</u> 

|Ireland/FAVAR(5)|House price growth|D(interest rate|Fac1(house price)|Glob2_price|
|---|---|---|---|---|
|House price growth|���|0:1931|0:7275|0:0567|
|D(interest rate)|0:6136|���|0:0579|0:1801|
|Fac1(house price)|0:9709|0:1503|���|0:0023|
|Glob2_price|0:9676|0:1723|0:7865|���|



Comments: In the case of Ireland, real house price growth is exogenous. 

Table 8: Causality in FAVAR models in the case of Germany 

|Germany/FAVAR(4)|House price growth|D(interest rate)|Fac1(house price)|Glob3_price|
|---|---|---|---|---|
|House price growth|���|0:0010|0:2680|0:0269|
|D(interest rate)|0:0039|���|0:7268|0:0002|
|Fac1(house price)|0:3041|0:1367|���|0:0001|
|Glob3_price|0:0038|0:9902|0:0779|���|



Comments: Evidence of indirect causality from the house price factor fac1 to real house price growth through the global factor Glob3_price 

Table 9: Causality in FAVAR models in the case of Australia 

21 

|Australia/FAVAR(3)|House price growth|D(interest rate)|Fac1(house price)|Glob2_price|
|---|---|---|---|---|
|House price growth|���|0:1820|0:0199|0:4273|
|D(interest rate)|0:0011|���|0:0585|0:2210|
|Fac1(house price)|0:0682|0:5095|���|0:0246|
|Glob2_price|0:0678|0:3319|0:3862|���|



Comments: Direct causality from the house price factor fac1 to real house price growth 

Table 10: Causality in FAVAR models in the case of UK 

|UK/FAVAR(5)|House price growth|D(interest rate)|Fac1(house price)|Glob2_price|
|---|---|---|---|---|
|House price growth|���|0:0961|0:2631|0:8940|
|D(interest rate)|0:1533|���|0:0442|0:3108|
|Fac1(house price)|0:0010|0:8416|���|0:0248|
|Glob2_price|0:4941|0:0566|0:4515|���|



Comments: Direct causality from the house price factor fac1 to real house price growth 

Table 11: Causality in FAVAR models in the case of Spain 

|Spain/FAVAR(6)|House price growth|D(interest rate)|Fac1(house price)|Glob2_price|
|---|---|---|---|---|
|House price growth|���|0:2865|0:8252|0:0441|
|D(interest rate)|0:0266|���|0:0005|0:0070|
|Fac1(house price)|0:0001|0:0435|���|0:1072|
|Glob2_price|0:0476|0:0582|0:9217|���|



Comments: Direct causality from the house price factor fac1 to the growth rate of the real house price 

###### Table 12: Summary Table of Causality from house price factor to real domestic house price <u>in FAVAR models of limited order</u> 

|Countries|France|Spain|UK|Australia|Ireland|Germany|
|---|---|---|---|---|---|---|
|Fac1(house price)|0:0042|0:0001|0:0010|0:0682|0:9709|0:3041|
|p-values of|the chi-sq|uare test|statistic u|sed to test|for causal|ity|
|of the house|price factor|fac1 to|the domes|tic house p|rice growt|h rate|



### C CAUSALITY tested from systems of equations 

The systems are derived from FAVAR models of high order (12 or 13) including the growth rate of real house prices, the …rst di¤erence of the long term nominal interest rate and the factors fac1 (house prices), Glob2 _price and/or Glob_3 price. 

###### Table 13: System of equations for USA 

22 

|USA/system|equations|
|---|---|
|House price growth|0.000160+0.900258<sup>(���)</sup>*USA_IMMO_REAL_GT(-1)|
||Adjusted R-squared0:792669|
|D(interest rate)|-0.090912<sup>(���)</sup>+0.223769<sup>(���)</sup>*DUSA_IRL(-1)-0.199008<sup>(���)</sup>*DUSA_IRL(�7)|
||Adjusted R-squared0:108009|
|Fac1|-0.363979<sup>(���)</sup>-0.418632<sup>(���)</sup>* DUSA_IRL(-10)+29.76668<sup>(���)</sup>*USA_IMMO_REAL_GT(-1)|
||+0.497321<sup>(���)</sup>*Fac1_USA(-1)+0.317634<sup>(���)</sup>*Fac1_USA(-2)|
||+0.240408<sup>(���)</sup>*Fac1_USA(-10)-0.316671<sup>(���)</sup>*Fac1_USA(-12)|
||+0.189318<sup>(���)</sup>*GLOB2_PRICE(-10)+0.272204<sup>(���)</sup>* GLOB3_PRICE(-1)|
||Adjusted R-squared0:884742|
|Glob2_price|-0.286687+26.10069<sup>(���)</sup>*USA_IMMO_REAL_GT(-4)+ 0.762789<sup>(���)</sup>* GLOB2_PRICE(-1)<br>|
||+ 0.762789<sup>(���)</sup>*GLOB3_PRICE(-7)-0.268343 <sup>(���)</sup>*GLOB3_PRICE(-8)|
||Adjusted R-squared0:755615|
|Glob3_price|-0.155675-0.530828<sup>(���)</sup>* DUSA_IRL(-1)-0.541460<sup>(���)</sup>*DUSA_IRL(-3)|
||-0.259325<sup>(���)</sup>*DUSA_IRL(-6)-0.436491<sup>(���)</sup>*DUSA_IRL(-11)|
||-0.365732<sup>(���)</sup>*GLOB2_PRICE(-1)+ 0.172*G970<sup>(���)</sup>GLOB2_PRICE(-7)|
||+0.698491<sup>(���)</sup>* GLOB3_PRICE(-1)+ 0.358542<sup>(���)</sup>*GLOB3_PRICE(-3)|
||-19.34256<sup>(���)</sup>*USA_IMMO_REAL_GT(-4)+17.01177<sup>(���)</sup>*USA_IMMO_REAL_GT(-5)|
||Adjusted R-squared:0:746031|



USA_IMMO_REAL_GT is the growth rate of real house prices; DUSA_IRL is the …rst di¤erence of the long term interest rate for the USA; Fac1_USA is the …rst common factor from the database of house prices excluding the USA. 

The parameters are estimated by using the SUR estimation method, after whitening the residuals of the di¤erent equations. (���)indicates that the coe¢cients are statistically signi…cant at a level of 5%. 

Comments: The growth rate of real house prices rate and the …rst di¤erence of the interest rate are both exogeneous. They unidirectionnally cause the house price factor (Fac1_USA) .The global factor Glob2_price is caused by the global factor Glob3_price and the growth rate of real house prices. The global factor Glob3_price is caused by the other three variables. 

###### CAUSALITY tested from FAVAR models of order 12 

###### Table 14: USA 

|USA/FAVAR(12)|House price growth|D(interest rate)|Fac1 (house price)|Glob2_price|Glob3_price|
|---|---|---|---|---|---|
|House price growth|���|0:7569|0:0015|0:0004|0:4028|
|D(interest rate)|0:4283|���|0:2764|0:0492|0:0226|
|Fac1(house price)|0:5688|0:7467|���|0:0364|0:8715|
|Glob2_price|0:5681|0:1202|0:0610|���|0:0000|
|Glob3_price|0:0655|0:4670|0:0419|0:0144|���|



23 

Comments: The …rst di¤erence of the interest rate is exogenous; the house price growth unidirectionnally causes the house price factor (Fac1) and the global factor Glob2; the …rst di¤erence of the interest rate unidirectionaly causes the global factors Glob2 and Glob3. 

||Table|15: France|||
|---|---|---|---|---|
|FRANCE/FAVAR(12)|House price growth|D(interest rate|Fac1(house price)|Glob2_price|
|House price growth|���|0:0880|0:1964|0:9906|
|D(interest rate)|0:0496|���|0:0465|0:5334|
|Fac1(house price)|0:0037|0:1374|���|0:0054|
|Glob2_price|0:2324|0:0061|0:8972|���|



Comments: Evidence of direct causality from the house price factor fac1 to the growth rate of the real house price 

<u>Table 16: Ireland</u> 

|Ireland/FAVAR(12)|House price growth|D(interest rate|Fac1(house price)|Glob2_price|
|---|---|---|---|---|
|House price growth|���|0:2492|0:9127|0:3642|
|D(interest rate)|0:9227|���|0:0019|0:2139|
|Fac1(house price)|0:4928|0:2252|���|0:0034|
|Glob2_price|0:9242|0:0850|0:8709|���|
|Comments:|In the case of Irelan|d, the house pric|e growth rate is ex|ogenous.|



|Table 17: Ca<br>|usality in FAVA<br>|R models in t<br>|he case of Ger<br>|many<br>|
|---|---|---|---|---|
|Germany/FAVAR(12)|House price growth|D(interest rate)|Fac1(house price)|Glob3_price|
|House price growth|���|0:0685|0:1195|0:5814|
|D(interest rate)|0:0476|���|0:5853|0:1145|
|Fac1(house price)|0:5975|0:2565|���|0:0512|
|Glob3_price|0:2147|0:8931|0:4464|���|



Comments: Direct causality from the house price factor fac1 to Glob3; direct causality from the interest rate to the house price growth 

|Table 18:|Causality in F|AVAR models|in the case of|Australia|
|---|---|---|---|---|
|Australia/FAVAR(12)|House price growth|D(interest rate)|Fac1(house price)|Glob2_price|
|House price growth|���|0:7535|0:1004|0:2255|
|D(interest rate)|0:0508|���|0:3988|0:5505|
|Fac1(house price)|0:0470|0:0946|���|0:1335|
|Glob2_price|0:0061|0:0228|0:9634|���|



Comments: Direct causality from the house price factor fac1 to the growth rate of the real house price 

Table 19: Causality in FAVAR models in the case of UK 

24 

|UK/FAVAR(12)|House price growth|D(interest rate)|Fac1(house price)|Glob2_price|
|---|---|---|---|---|
|House price growth|���|0:5049|0:1334|0:1832|
|D(interest rate)|0:8829|���|0:0000|0:1000|
|Fac1(house price)|0:0041|0:6088|���|0:0074|
|Glob2_price|0:8142|0:3204|0:5304|���|



Comments: Direct causality from the house price factor fac1 to the growth rate of the real house price ; exogeneity of the interest rate 

Table 20: Causality in FAVAR models in the case of Spain 

|Spain/FAVAR(12)|House price growth|D(interest rate)|Fac1(house price)|Glob2_price|
|---|---|---|---|---|
|House price growth|���|0:3428|0:2482|0:7138|
|D(interest rate)|0:5606|���|0:0254|0:0902|
|Fac1(house price)|0:0158|0:0272|���|0:5404|
|Glob2_price|0:6813|0:0085|0:8032|���|
|Comments: Direct|causality from the <br>|house price factor <br>house price|fac1 to the growth|rate of the real|



Table 21: Summary Table of Causality from house price factor to real domestic house price in FAVAR models of higher order 

|Countries|France|Spain|UK|Australia|Ireland|Germany|
|---|---|---|---|---|---|---|
|Fac1(house price)|0:0037|0:0158|0:0041|0:0470|0:4928|0:5975|



p-values of the chi-square test statistic used to test for causality of the house price factor fac1 to the domestic house price growth rate 

25 

###### ��������� 

����������������������������������������������������������������������������������������� 



<!-- Start of picture text -->
5 8<br>4 6<br>3 4<br>2 2<br>1 0<br>0 -2<br>-1 -4<br>-2 -6<br>-3 -8<br>-4 -10<br>1980 1985 1990 1995 2000 2005<br>world index (unweighted)<br>world index (GDP weighted)<br>world housing prices factor 1<br><!-- End of picture text -->

- ������������������������������������������������ ������������������������������ 



<!-- Start of picture text -->
6 6<br>4 4<br>2 2<br>0 0<br>-2 -2<br>-4 -4<br>-6 -6<br>-8 -8<br>1980 1985 1990 1995 2000 2005<br>All countries Australia<br>Germany Spain<br>France United Kingdom<br>Ireland USA<br><!-- End of picture text -->

�������!���"#$%�#�&'(���������������������'������������������������ 



<!-- Start of picture text -->
16 20<br>14 16<br>12 12<br>10 8<br>8 4<br>6 0<br>4 -4<br>2 -8<br>1980 1985 1990 1995 2000 2005<br>GLOB1_w/o housing price (right)<br>World Long Term Interest Rates (unweighted, left)<br>World Short Term Interest Rates (unweighted, left)<br><!-- End of picture text -->

- �������)��"#$%�#�&'(���������������������������"*+����'������������������ 



<!-- Start of picture text -->
12 2.0<br>8 1.5<br>4 1.0<br>0 0.5<br>-4 0.0<br>-8 -0.5<br>-12 -1.0<br>-16 -1.5<br>-20 -2.0<br>1980 1985 1990 1995 2000 2005<br>GDP factor 1, inverted, left<br>World GDP (unweighted), right<br>GLOB2_w/o housing prices, left<br><!-- End of picture text -->

�������,���"#$%�#!&'(��������������������-�����������������������$������"������� 



<!-- Start of picture text -->
8 3<br>6 2<br>4 1<br>2 0<br>0 -1<br>-2 -2<br>-4 -3<br>-6 -4<br>-8 -5<br>1980 1985 1990 1995 2000 2005<br>GLOB3_PRICE (inverted scale, left scale)<br>WORLD Output Gap (unweighted, right scale)<br><!-- End of picture text -->

������������������������������������������������������������������������������ 



<!-- Start of picture text -->
8 10<br>4 5<br>0 0<br>-4 -5<br>-8 -10<br>-12 -15<br>-16 -20<br>1980 1985 1990 1995 2000 2005<br>AXE_FACTOT1_1<br>GLOB2_PRICE<br>AXE_IMMO1_ALL<br><!-- End of picture text -->

###### ������������������������� 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>1980 1985 1990 1995 2000 2005<br>DU_CRISIS FINAN_CRISIS<br><!-- End of picture text -->

����������������������������������� ����������������� �����������������������������!"��������������������������� 

###### **Documents de Travail** 

250. A. Monfort, «Une modélisation séquentielle de la VaR,» Septembre 2009 251. <u>A. Monfort, “Optimal Portfolio Allocation under Asset and Surplus VaR Constraints,” September 2009</u> 

252. <u>G. Cette and J. Lopez, “ICT Demand Behavior: An International Comparison,” September 2009</u> 253. <u>H. Pagès, “Bank Incentives and Optimal CDOs,” September 2009</u> 254. <u>S. Dubecq, B. Mojon and X. Ragot, “Fuzzy Capital Requirements, Risk-Shifting and the Risk Taking Channel of Monetary Policy,” October 2009</u> 

255. <u>S. Frappa and J-S. Mésonnier, “The Housing Price Boom of the Late ’90s: Did Inflation Targeting Matter?” October 2009</u> 

256. <u>H. Fraisse, F. Kramarz and C. Prost, “Labor Court Inputs, Judicial Cases Outcomes and Labor Flows: Identifying Real EPL,” November 2009</u> 

257. <u>H. Dixon, “A unified framework for understanding and comparing dynamic wage and price-setting models,” November 2009</u> 

258. <u>J. Barthélemy, M. Marx and A. Poisssonnier, “Trends and Cycles: an Historical Review of the Euro Area,” November 2009</u> 

259. <u>C. Bellégo and L. Ferrara, “Forecasting Euro-area recessions using time-varying binary response models for financial variables,” November 2009</u> 

260. <u>G. Horny and M. Picchio, “Identification of lagged duration dependence in multiple-spell competing risks models,” December 2009</u> 

261. <u>J-P. Renne, “Frequency-domain analysis of debt service in a macro-finance model for the euro area,” December 2009</u> 

262. <u>C. Célérier, “Forecasting inflation in France,” December 2009</u> 263. <u>V. Borgy, L. Clerc and J-P. Renne, “Asset-price boom-bust cycles and credit: what is the scope of macro-prudential regulation?,” December 2009</u> 

264. <u>S. Dubecq and I. Ghattassi, “Consumption-Wealth Ratio and Housing Returns,” December 2009</u> 265. <u>J.-C. Bricongne, L. Fontagné, G. Gaulier, D. Taglioni and V. Vicard, “Firms and the Global Crisis: French Exports in the Turmoil,” December 2009</u> 

266. <u>L. Arrondel and F. Savignac, “Stockholding: Does housing wealth matter?,” December 2009</u> 267. <u>P. Antipa and R. Lecat, “The “housing bubble”and financial factors: Insights from a structural model of the French and Spanish residential markets,” December 2009</u> 

268. <u>L. Ferrara and O. Vigna, “Cyclical relationships between GDP and housing market in France: Facts and factors at play,” December 2009</u> 

269. <u>L.J. Álvarez, G. Bulligan, A. Cabrero, L. Ferrara and H. Stahl, “Housing cycles in the major euro area countries,” December 2009</u> 

270. <u>P. Antipa and C. Schalck, “Impact of Fiscal Policy on Residential Investment in France,” December 2009</u> 

271. <u>G. Cette, Y. Kocoglu, and J. Mairesse, “Productivity Growth and Levels in France, Japan, the United Kingdom and the United States in the Twentieth Century,” January 2010</u> 

272. <u>E. Lavallée and V. Vicard, “National borders matter...where one draws the lines too,” January 2010</u> 273. <u>C. Loupias and P. Sevestre, “Costs, demand, and producer price changes,” January 2010</u> 274. <u>O. de Bandt, K.  Barhoumi and C. Bruneau, “The International Transmission of House Price Shocks,” January 2010</u> 

Pour accéder à la liste complète des Documents de Travail publiés par la Banque de France veuillez consulter le site : - <u>http://www.banque france.fr/fr/publications/documents_de_travail/documents_de_travail_10.htm</u> 

For a complete list of Working Papers published by the Banque de France, please visit the website: - <u>http://www.banque france.fr/fr/publications/documents_de_travail/documents_de_travail_10.htm</u> 

Pour tous commentaires ou demandes sur les Documents de Travail, contacter la bibliothèque de la Direction Générale des Études et des Relations Internationales à l'adresse suivante : 

For any comment or enquiries on the Working Papers, contact the library of the Directorate General Economics and International Relations at the following address : 

BANQUE DE FRANCE 49- 1404  Labolog 75049 Paris Cedex 01 tél : 0033 (0)1 42 92 49 55 ou 62 65 ou 48 90 ou 69 81 email : <u>thierry.demoulin@banque-france.fr jeannine.agoutin@banque-france.fr veronique.jan-antuoro@banque-france.fr nathalie.bataille-salle@banque-france.f</u> 

