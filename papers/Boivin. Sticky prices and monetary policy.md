---
title: Boivin. Sticky prices and monetary policy
type: paper
source_pdf: raw/papers/Boivin. Sticky prices and monetary policy.pdf
converted: 2026-08-18
---





Boivin, Jean; Giannoni, Marc P.; Mihov, Ilian 

###### **Working Paper** 

Sticky prices and monetary policy: Evidence from disaggregated US data 

CFS Working Paper, No. 2007/14 

###### **Provided in Cooperation with:** 

Center for Financial Studies (CFS), Goethe University Frankfurt 

_Suggested Citation:_ Boivin, Jean; Giannoni, Marc P.; Mihov, Ilian (2006) : Sticky prices and monetary policy: Evidence from disaggregated US data, CFS Working Paper, No. 2007/14, Goethe University Frankfurt, Center for Financial Studies (CFS), Frankfurt a. M., https://nbn-resolving.de/urn:nbn:de:hebis:30-38244 

This Version is available at: 

https://hdl.handle.net/10419/25515 

###### **Standard-Nutzungsbedingungen:** 

Die Dokumente auf EconStor dürfen zu eigenen wissenschaftlichen Zwecken und zum Privatgebrauch gespeichert und kopiert werden. 

Sie dürfen die Dokumente nicht für öffentliche oder kommerzielle Zwecke vervielfältigen, öffentlich ausstellen, öffentlich zugänglich machen, vertreiben oder anderweitig nutzen. 

Sofern die Verfasser die Dokumente unter Open-Content-Lizenzen (insbesondere CC-Lizenzen) zur Verfügung gestellt haben sollten, gelten abweichend von diesen Nutzungsbedingungen die in der dort genannten Lizenz gewährten Nutzungsrechte. 

###### **Terms of use:** 

_Documents in EconStor may be saved and copied for your personal and scholarly purposes._ 

_You are not to copy documents for public or commercial purposes, to exhibit the documents publicly, to make them publicly available on the internet, or to distribute or otherwise use the documents in public._ 

_If the documents have been made available under an Open Content Licence (especially Creative Commons Licences), you may exercise further usage rights as specified in the indicated licence._ 





#### No. 2007/14 

**Sticky Prices and Monetary Policy: Evidence from Disaggregated U.S. Data** 

Jean Boivin, Marc P. Giannoni, and Ilian Mihov 





### **Center for Financial Studies** 

The _Center for Financial Studies_ is a nonprofit research organization, supported by an association of more than 120 banks, insurance companies, industrial corporations and public institutions. Established in 1968 and closely affiliated with the University of Frankfurt, it provides a strong link between the financial community and academia. 

The CFS Working Paper Series presents the result of scientific research on selected topics in the field of money, banking and finance. This paper was presented at the International Research Forum on Monetary Policy 2006 which was held at the Federal Reserve Board in Washington DC and jointly organized by the Federal Reserve Board, the European Central Bank, the BMW Center for German and European Studies at Georgetown University and the Center for Financial Studies at Frankfurt University. 

If you would like to know more about the _Center for Financial Studies_ , please let us know of your interest. 





Prof. Dr. Jan Pieter Krahnen 

Prof. Volker Wieland, Ph.D. 



#### CFS Working Paper No. 2007/14 

#### **Sticky Prices and Monetary Policy: Evidence from Disaggregated U.S. Data*** 

Jean Boivin<sup>1</sup> , Marc P. Giannoni<sup>2</sup> , and Ilian Mihov<sup>3</sup> 

#### November 10, 2006 

##### **Abstract:** 

This paper uses factor-augmented vector autoregressions (FAVAR) estimated using a large data set to disentangle fluctuations in disaggregated consumer and producer prices which are due to macroeconomic factors from those due to sectorial conditions. This allows us to provide consistent estimates of the effects of US monetary policy on disaggregated prices. While sectorial prices respond quickly to sector-specific shocks, we find that for a large number of price series, there is a significant delay in the response of prices to monetary policy shocks. In addition, price responses display little evidence of a “price puzzle,” contrary to existing studies based on traditional VARs. The observed dispersion in the reaction of producer prices is relatively well explained by the degree of market power, as predicted by models with monopolistic competition. 

##### **JEL Classification:** E32, E52 

**Keywords:** Sticky Prices, Monetary Policy, Disaggregated Prices, Imperfect Competition, Factor-Augmented Vector Autoregression Model (FAVAR) 

> * We thank Piotr Eliasz for valuable discussions and participants at the NBER Monetary Economics summer institute for valuable comments. We also thank Rashid Ansari, Guilherme Martins, Mehmet Pasaogullari and Mauro Roca for excellent research assistance. Boivin and Giannoni thank the National Science Foundation for financial support (SES-0518770). 

> 1 HEC Montréal, 3000, chemin de la Côte-Sainte-Catherine, Montréal (Québec), Canada H3T 2A7; Email: jean.boivin@hec.ca 

> 2 Columbia Business School, 824 Uris Hall, 3022 Broadway, New York, NY 10027; Email: mg2190@columbia.edu 

3 INSEAD, 77300 Fontainebleau, France, Email: ilian.mihov@insead.edu 

## 1 Introduction 

In this paper, we document the e�ects of macroeconomic fluctuations on disaggregated prices. Whether prices are generally flexible or sticky has been for a long time the subject of considerable controversy in macroeconomics. A proper assessment of the speed of price adjustment is crucial to understand the sources of business cycle fluctuations, as well as the e�ects of monetary policy on the economy. 

Numerous studies focusing on specific wholesale or retail items have found evidence of prices maintained fixed for several months, in the U.S.<sup>1</sup> Surveys of firms also suggest that a large fraction of prices remain constant for many months (Blinder, Canetti, Lebow, and Rudd, 1998). In addition, studies involving vector autoregressions (VAR) usually provide evidence of stickiness of the aggregate price level. For instance, under a wide range of identifying assumptions, following an unexpected monetary policy tightening, aggregate price indices are commonly found to remain unchanged for about a year and a half, and start declining thereafter (see, e.g., Christiano, Eichenbaum and Evans, 1999). Largely motivated by this evidence, a broad class of macroeconomic models including models used for policy analysis rests on the assumption that prices are sticky. Such models, sometimes augmented with mechanisms to increase the persistence in inflation, have been argued to replicate many features of aggregate data (e.g., Rotemberg and Woodford, 1997; Christiano, Eichenbaum and Evans, 2005; Smets and Wouters 2004), and in particular the delayed and persistent e�ects of monetary policy shocks on prices. 

However, recent evidence on disaggregated prices series has cast doubts on the validity of existing models with price rigidities. For instance, Bils and Klenow (2004) find that disaggregated consumer prices are much more volatile than conventionally assumed in studies based on aggregate data. In fact, looking at 350 categories of consumer goods and services 

> 1See for instance Carlton (1986), Cecchetti (1986), Kashyap (1995), Levy, Bergen, Dutta and Venable (1997), MacDonald and Aaronson (2001), and Kackmeister (2001). 

2 

that cover about 70% of U.S. consumer expenditure, Bils and Klenow (2004) estimate that the median time between price changes is 4.3 months.<sup>2</sup> The duration between price changes varies however considerably across sectors.<sup>3</sup> Bils and Klenow (2004) argue that sectorial inflation rates are much more volatile and short-lived than implied by simple sticky-price models. Klenow and Kryvtsov (2004) document that when prices change, they change by more than 13% on average, or by 8.5% when adjusting for temporary sales. Golosov and Lucas (2003), in turn, calibrate a menu-cost model with both aggregate and idiosyncratic shocks to match these facts, and find that monetary policy shocks have large and rapid e�ects on aggregate prices but only very little e�ect on economic activity. 

The evidence about relatively flexible individual prices thus contrasts sharply with the evidence obtained from aggregate price indices. While simple sticky-price models designed to explain aggregate price behavior appear to explain poorly the behavior of more disaggregated price series, models with relatively flexible sectorial prices do not seem to explain the empirical evidence obtained from aggregate series. 

How then, can the facts just laid out be reconciled? One possibility is that studies based on aggregate series mistakenly assume that prices are sticky in the face of macroeconomic fluctuations, when in fact prices adjust more frequently to changes in economic conditions. In such a case, sectorial prices would be expected to respond on average rapidly to macroeconomic disturbances such as monetary policy shocks. And they would be expected to respond more rapidly in sectors that adjust prices more frequently. Another possibility is that prices respond di�erently to sectorial and macroeconomic shocks. In that case, individual prices may respond rapidly and strongly to shocks specific to the particular price categories, but 

> 2The median duration remains below 5 months when they account for temporary sales. More recently, however, Nakamura and Steinsson (2006), analyzing CPI microdata, argue that the median duration is 11 months when they exclude sales and price changes due to product substitutions. Such a median duration is then similar to the one found in Euro area data (see, e.g., Dhyne et al., 2005, and several other studies which are part of the Eurosystem Inflation Persistence Network). 

> 3It ranges from less than a month (for gasoline prices) to more than 80 months (coin-operated apparel laundry and dry-cleaning). 

3 

may be more slow to adjust to aggregate macroeconomic factors. 

In addition, while aggregate inflation is often argued to be persistent over long samples,<sup>4</sup> disaggregated series appear much more transient. Several authors have argued that the apparent persistence of aggregate inflation may reflect an aggregation bias or a structural break in the mean inflation during the sample.<sup>5</sup> Yet, as another possible explanation, the di�erences in inflation persistence at the aggregate and disaggregate level may also be due to di�erent responses to macroeconomic and sector-specific shocks. 

One limitation of the existing evidence such as that of Bils and Klenow (2004), Klenow and Kryvtsov (2004) is that while they provide a careful description of individual prices movements, they do not distinguish between sector-specific and aggregate sources of fluctuations. It thus not possible to infer from these studies whether sectorial prices respond rapidly or slowly, strongly or moderately to macroeconomic shocks. Such distinctions would however provide crucial insights on the determination of prices, hence guidance for the development of appropriate macroeconomic models. 

In this paper, we disentangle the fluctuations in disaggregated U.S. consumer and producer prices which are due to aggregate macroeconomic factors from those due to sectorial conditions. We do so by estimating factor-augmented vector autoregressions (FAVAR) that relate a large panel of economic indicators and individual price series to a relatively small number of estimated common factors. This framework allows us to assess the relative importance of macroeconomic and sectorial disturbances in determining disaggregate price fluctuations. It also permits a decomposition of the persistence in inflation in terms of macroeconomic and sector-specific factors. 

> 4See, e.g., Fuhrer and Moore (1995), Gali and Gertler (1999), Cogley and Sargent (2001, 2003), Sims (2001), Stock (2001), Pivetta and Reis (2003), Levin and Piger (2003), Clark (2003). 

> 5Pesaran and Smith (1995) and Imbs, Mumtaz, Ravn and Rey (2005) argue that heterogeneity – across categories – in the persistence individual series may result in a large estimated persistence of the aggregate even if individual series display on average little persistence. Cogley and Sargent (2001, 2003), Levin and Piger (2003) and Clark (2003) find that inflation persistence drops when they allow for changes in mean over time. 

4 

We then estimate the e�ects of U.S. monetary policy on disaggregated prices, after identifying monetary policy shocks using all of the information available. We study in particular the magnitude of the prices responses to monetary policy shocks, and whether monetary policy has delayed e�ects on prices. While extensive research has attempted to characterize the e�ects of monetary policy on macroeconomic indicators, little research has analyzed its e�ects on disaggregated prices. Two exceptions are Bils, Klenow and Kryvtsov (2003), and Balke and Wynne (2003). In these papers, the authors estimate the response of individual prices to monetary policy shock by appending individual price series to a separately-estimated VAR. They however find that individual price responses display a considerable “price puzzle”, i.e., a price increase following an unexpected monetary policy tightening, which stands in sharp contrast to predictions of conventional models. As argued in Sims (1992) and Bernanke, Boivin and Eliasz (2005), such evidence of price puzzle may be indicative of VAR misspecification due, e.g., to the lack of information considered in the VAR estimation. In the context of our data-rich FAVAR, this risk of misspecification is considerably reduced, as we use all of the available information in the estimation. Consistency of our estimates is furthermore guaranteed by the fact that we estimate within the same framework the parameters describing the dynamics of the common factors and the parameters that relate the individual price series to common factors. 

After documenting the responses of prices to a monetary policy shock, we attempt to provide an explanation for the cross-sectional dispersion of price responses. To this end, we collect data on industry characteristics that are related to various theories of price stickiness. In general, models that allow for imperfect competition and variable speed of price adjustment predict that firms in very competitive industries will react quickly to changes in the economic environment (see Barro, 1972). The standard workhorse monetary model with Calvo pricing assumes a fixed degree of price stickiness as measured by the probability of re-optimizing prices, so that industry characteristics do not a�ect this probability. Ex- 

5 

tensions of this model allow di�erences in probabilities of re-optimizing prices across sectors (see, e.g., Aoki, 2003; Benigno, 2003; Woodford, 2003, Chap. 3, Carvalho, 2006), but these models do not explain why such di�erences might emerge as part of the optimizing behavior of firms. Nevertheless, in these New Keynesian models, one industry characteristic – the – degree of competition a�ects directly the degree of strategic complementarity (or “real rigidity” as in Ball and Romer, 1990) in price setting, and therefore the magnitude of price adjustments. 

Our main findings can be summarized as follows: 

First, most of the fluctuations in sectorial inflation rates are due to sector-specific factors. On average, only about 15% of inflation fluctuations are due to macroeconomic factors (17% for personal consumption expenditure prices and 13% for producer prices). Thus, the relative flexibility of sectorial prices found by Bils and Klenow (2004) is to a large extent due to sector-specific disturbances. Consistent with the evidence on disaggregated price series, we also find considerable disparities in the magnitude of price changes and in the persistence of inflation across price categories, both for consumer and producer prices. These disparities are due to a large extent to di�erences in the volatility of sector-specific components, and only little to di�erent responses to macroeconomic factors. 

Second, fluctuations in sectorial inflation rates are somewhat persistent, but this persistence is essentially due to the very high degree of persistence in the common components, and not to sector specific disturbances. While sector-specific shocks may cause large fluctuations in the individual inflation rates, these fluctuations are short-lived on average. In contrast, aggregate macroeconomic shocks tend to have more persistent e�ects on a wide range of sectorial inflation rates. 

Third, in the context of our estimated FAVAR, the responses of disaggregated prices to a monetary policy shock display very little evidence of a price puzzle, in agreement with conventional economic models, but in contrast to the results routinely obtained in VAR 

6 

studies. This suggests that by exploiting a large information set in the estimation, we may obtain more accurate estimates of the e�ects of monetary policy. 

Fourth, while individual price series reveal some heterogeneity in their responses to an unexpected monetary policy tightening, a striking feature is that most indices respond very little for several months following the shock, and start falling only later. 

The picture that emerges then, is one in which many prices do in fact fluctuate considerably in response to sector-specific shocks, even though, they tend to respond only sluggishly to aggregate macroeconomic shocks such as monetary policy shocks. This di�erence in responses to various shocks can explain why, at the disaggregated level, individual prices are found to be adjusted relatively frequently, while estimates of the degree of price rigidity are much higher when based on aggregate data. This explains why models that assume considerable price stickiness have often been successful at replicating the e�ects of monetary policy shocks. 

Fifth, we document that responses of producer prices to monetary policy shocks are strongly correlated with the degree of imperfect competition. In more competitive industries (i.e., those with relatively low average profit rates), we observe a relatively rapid response of prices to monetary policy. 

The rest of the paper is organized as follows. Section 2 reviews the econometric framework, by discussing the formulation and estimation of the FAVAR. In Section 3, we discuss various data sets that we use in our estimation. Section 4 presents our empirical results including the e�ects of monetary policy on a very wide range of prices. Section 5 investigates cross-sectional relationships, and links the price responses of producer prices in various sectors to industry characteristics. Section 6 concludes. 

7 

## 2 Econometric Framework: FAVAR 

The empirical framework that we consider is based on the factor-augmented vector autoregression model (FAVAR) described in Bernanke, Boivin and Eliasz (2005) (BBE). One of its key features is to provide estimates of macroeconomic factors that a�ect the data of interest, by systematically and consistently exploiting all information from a large set of economic indicators. In our application, we estimate the empirical model by exploiting information from a large number of macroeconomic indicators, as well as from disaggregated data. This framework is particularly well suited to decompose the fluctuations of each series into a common and a series-specific component. It also allows us to characterize the response of all data series to macroeconomic disturbances, such as monetary policy shocks. As BBE argue, this framework should lead to a better identification of the policy shock than standard VARs, because it explicitly recognizes the large information set that the Federal Reserve and financial market participants exploit in practice, and also because it does not require to take a stand on the appropriate measures of prices and real activity which can simply be treated as latent common components. A natural by-product of the estimation is to obtain impulse response functions for any variables included in the data set. In particular, this allows us to document the e�ect of monetary policy on disaggregated prices. 

We only provide here a general description of our implementation of the empirical framework and refer the interested reader to BBE for additional details. We assume that the economy is a�ected by a vector �� of common components to all variables entering the data set. Since we will be interested in characterizing the e�ects of monetary policy, this vector of common components includes a measure of the stance of monetary policy. As in most related VAR applications, we assume that the Federal funds rate, ��, is the policy instrument. It will be allowed to have pervasive e�ect throughout the economy and will thus be considered as a common component of all variables entering the data set. The rest of the common dynamics are captured by a � × 1 vector of unobserved factors ��� where � is 

8 

relatively small. These unobserved factors may reflect general economic conditions such as “economic activity,” the “general level of prices,” the level of “productivity,” which are not easily captured by a few time series, but rather by a wide range of economic variables. We assume that the joint dynamics of �� and �� are given by 



where 



and �(�) is a conformable lag polynomial of finite order �� which may contain a priori restrictions, as in standard structural VARs. The error term �� is i.i.d. with mean zero and covariance matrix �� 

The system (1) is a VAR in ��. The additional di�culty, with respect to standard VARs, however, is that the factors �� are unobservable. We assume that the factors summarize the information contained in a large number of economic variables. We denote by �� this � × 1 vector of “informational” variables, where � is assumed to be “large,” i.e., ��� + 1� We assume furthermore that the large set of observable “informational” series �� is related to the common factors according to 



where � is an � ×(� + 1) matrix of factor loadings, and the � ×1 vector �� contains (meanzero) sector-specific components that are uncorrelated with the common components ��. These sector-specific components are allowed to be serially correlated and weakly correlated across indicators. Equation (2) reflects the fact that the elements of ��� which in general are correlated, represent pervasive forces that drive the common dynamics of ��� Conditional on the observed Federal funds rate ��� the variables in �� are thus noisy measures of the 

9 

underlying unobserved factors ��� Note that it is in principle not restrictive to assume that �� depends only on the current values of the factors, as �� can always capture arbitrary lags of some fundamental factors.<sup>6</sup> 

— To estimate the system (1) (2), we follow the two-step principal component approach described in BBE. In the first step, the space spanned by the common components, ��� is estimated using the first � + 1 principal components of ��� While the estimation does not exploit the fact that �� is observed, Stock and Watson (2002) show that the principal components consistently recover the space spanned by both �� and ��, when � is large and the number of principal components used is at least as large as the true number of factors. In the second step, a structural VAR is estimated on these common components, after imposing that �� is one of the common components. 

This procedure has the advantages of being computationally simple and easy to implement. As discussed by Stock and Watson (2002), it also imposes few distributional assumptions and allows for some degree of cross-correlation in the idiosyncratic error term ��� Boivin and Ng (2005) document the good forecasting performance of this estimation approach compared to some alternatives.<sup>7</sup> 

## 3 Data 

The data set used in the estimation of our FAVAR is a balanced panel of 653 monthly series, for the period running from 1976:1 to 2005:6. All data have been transformed to induce stationarity. The details for this data set, as well as the transformation applied to each particular series, are in Appendices A — D. The data set includes 111 updated macroeconomic indicators used by BBE, and listed in Appendix A, which involve several 

> 6This is why Stock and Watson (1998) refer to (2) as a dynamic factor model. 

> 7Note that this two-step approach implies the presence of "generated regressors" in the second step. According to the results of Bai (2002), the uncertainty in the factor estimates should be negligible when � is large relative to � . Still, the confidence intervals on the impulse response functions reported below are based on a bootstrap procedure that accounts for the uncertainty in the factor estimation. 

10 

measures of industrial production, various price indices, interest rates, employment as well as other key macroeconomic and financial variables. These indicators have been found to collectively contain useful information about the state of the economy for the appropriate identification of monetary policy. We expanded the data set of BBE in two directions. 

First, we appended disaggregated data published by the Bureau of Economic Analysis on personal consumption expenditure (PCE). Specifically, we collected 335 series on PCE prices and an equal number of series on real consumption. Among these series, 35 price series and 35 real consumption series were removed because of missing observations. In order to capture data for all expenditures reported, we removed the other series in the same categories and retained the series at the immediately higher level of aggregation. However, we removed from our data set aggregate price and real consumption series (except for overall aggregates), so as to count only once each category in the disaggregated data. We thus ended up with 190 disaggregated PCE price series and the 190 corresponding consumption series. At the level of disaggregation considered, we have for instance data on new domestic autos, bicycles, jewelry and watches, shoes, cereals, taxicabs, and so on. In addition, we also included 4 price indices and 4 consumption aggregates (overall PCE, durable goods, nondurable goods, and services). Further details on these series are provided in Appendix B. 

Second, in order to obtain a more detailed picture of the characteristics of price responses, we also collected over 600 series for producer prices at the 6-digit level of NAICS codes (corresponding to 4-digit SIC codes). Because of changes in definitions and data coverage, we managed to obtain only 154 series for a longer period starting in January 1976 and ending in June 2005. Appendix C provides a brief description of these series. 

Besides the series just described, which we used to estimate the FAVAR, we also collected data on industry characteristics, which could help us validate or reject assumptions underlying models of price determination. We start with the C4 ratio provided by the Bureau of the Census. This ratio reports the percentage of total sales attributable to the four largest 

11 

firms in the industry. As yet another measure of competition, we use also data on average gross profit rates from the Annual Survey of Manufacturing. This data is available on an annual basis from 1997 to 2001. The cross-sectional industry data is described in Appendix D. 

## 4 Empirical Evidence on Disaggregated Prices 

We estimated the system (1) — (2) for the period 1976:1- 2005:6, using the data just described, and assuming 5 latent factors in the vector ��� We experimented with more factors, but none of our conclusions were a�ected. We used 13 lags in estimating (1). The estimated system allows us to analyze the sources of fluctuations in sectorial inflation rates. Note that for all of the price series considered (2) implies that 



where ��� contains the monthly log change in the respective price series. This formulation allows us to disentangle the fluctuations in sectorial inflation rates due to the macroeconomic factors – represented here by the common components �� which have a di�use e�ect on all data series – from those due to sector specific conditions represented by the term ���� It also allows us to study to what extent the persistence in sectorial inflation rates is due to macroeconomic or sectorial shocks. Note that since �� is a vector which may contain elements with very di�erent dynamics and the vectors of loadings �� may di�er across sectors, each sector-specific inflation rate may have di�erent dynamics in response to macroeconomic disturbances. Recall also, that the sector-specific terms ��� are allowed to be serially correlated and weakly correlated across sectors. 

12 

#### 4.1 Sources of fluctuations and persistence 

Table 1 reports various summary statistics on the volatility and the persistence of both aggregate and disaggregated monthly inflation series. As is indicated in the first column, the standard deviation of aggregate inflation amounts to 0.24% for the overall PCE series, and ranges between 0.24% and 0.42% for the inflation rates of durable goods, nondurable goods and services. Most of the volatility in aggregate inflation is due to fluctuations in common macroeconomic factors. In fact, the �<sup>2</sup> statistic, which measures the fraction of the variance in inflation explained by the common component �<sup>0</sup> �<sup>��liesabove 0.5for allofthe aggregate</sup> measures. 

The picture is however quite di�erent for more disaggregated inflation series. As the lower panel of Table 1 shows, disaggregated inflation series have been on average much more volatile than aggregate series. On average (across sectors), the standard deviation of monthly inflation has been 1.15% for all price series considered (0.97% for PCE inflation and 1.36% for PPI inflation).<sup>8</sup> As the columns two to four reveal, most of the inflation volatility is however due to sector-specific disturbances. In fact while the mean volatility of the common component to inflation lies at 0.33%, the volatility of the sector specific component is more than three times as large. The results are roughly similar for PCE and PPI inflation rates. As a result, the �<sup>2</sup> statistic amounts to 0.15 on average (0.17 for PCE and 0.13 for PPI). 

Table 1 also reveals a considerable amount of heterogeneity across sectors in the volatility of disaggregated inflation series. Whereas some series such inflation of tenant-occupied rent fluctuate even less than the inflation rate of the aggregate index, some such as the consumption category “insurance for other user-operated transportation” or the production category “other oilseed processing” have monthly standard deviations close to 10%. This heterogeneity is due to a large extent to di�erences in the volatility of sector-specific condi- 

> 8The average volatility of disaggregated PCE inflation series, weighted with expenditure shares, is somewhat lower than the unweighted average, but the overall picture remains the same for the volatility as well as for other statistics described below. 

13 

tions. It is due much less so to di�erences in the response to macroeconomic fluctuations. As the sector-specific components tend to cancel each other out, inflation in the aggregate price indices ends up being less volatile than most sector-specific inflation rates. 

One interesting fact revealed by Figure 1 is that the volatility of the common and the sector-specific components to inflation are strongly positively correlated across sectors. Sectors that experience volatile inflation rates due to changes in sectorial conditions are also sectors that experience a volatile inflation rate in response to changes in aggregate conditions. Several explanations can rationalize this fact. One possible explanation is that firms which adjust their prices frequently due to large sectorial shocks, may take the opportunity of changing their price to respond also to changed macroeconomic conditions. 

One characteristic of aggregate inflation often discussed is its persistence. To assess the degree of persistence, we fit for each inflation series ��� and each of its components, �<sup>0</sup> �<sup>��</sup> and ��� an AR(�) process, of the form 



where the lag-length � is selected on the basis of BIC, and we measure the degree of persistence by the sum of the coe�cients on all lags, � (1) � Not surprisingly, as we report on Table 1, fluctuations in aggregate inflation are persistent with a measure � (1) of 0.9 for the PCE inflation rate, and ranging between 0.44 and 0.91 for the three main components of PCE inflation. This measured persistence likely su�ers from an upward bias. In fact, as argued in Pesaran and Smith (1995) and Imbs, Mumtaz, Ravn, and Rey (2006), the estimated persistence is likely biased upward when the components of the aggregate index display heterogenous dynamics, and the persistence of the individual series and their variance are positively correlated. Another possible source of bias has to do with a possible change in mean inflation during the sample. 

As Clark (2003) noted, the sectorial inflation series display much less persistence than 

14 

the aggregated series over the long sample. Similarly, Altissimo, Mojon and Za�aroni (2004) who estimated a factor model on disaggregated CPI inflation series in Europe also found that inflation rates of individual categories are on average more volatile and less persistent than the aggregate inflation rate, and display widespread heterogeneity across categories. In our data set, the persistence is 0.29 on average over all sectors (0.30 for PCE inflation and 0.28 for PPI inflation). The inflation persistence varies importantly across sectors. While it is negative for some producer and consumer prices, it gets above 0.9 for the “health insurance” category of “worker’s compensation” and for “rental value of farm dwellings.” Interestingly, while the inflation persistence is in some cases due to series-specific factors, such as in the categories just mentioned, the inflation persistence is for most series due to fluctuations in common factors in the economy. In fact, while the average persistence of the common components reaches 0.91, the individual components display on average almost no persistence. There is however considerable heterogeneity in the persistence of the sectorspecific component across sectors. 

Overall these results suggest that there is a much higher volatility of sectorial inflation rates than of aggregate inflation rates, and that changes in sector-specific conditions are the most important determinants of sectorial inflation rates. Fluctuations in the common components, however, are responsible for a significant fraction of the volatility of sectorial inflation rates, and generate most of the fluctuations in aggregate inflation. In addition, the persistence in sectorial inflation is primarily due to the very high degree of persistence in the common components, and not to sector specific disturbances. While sector-specific shocks may cause large fluctuations in sectorial inflation, these fluctuations are typically short lived. Aggregate macroeconomic shocks instead tend to have more persistent e�ects on a wide range of sectorial inflation rates. 

15 

#### 4.2 E�ects of monetary policy shocks 

Prices may change for all sorts of reasons, including changes in costs, in productivity, or changes in demand for goods. While Bils and Klenow (2004) and Klenow and Kryvtsov (2005) provide very valuable evidence that most prices are changed relatively frequently, and on average by large amounts, their study does not identify the source of these changes. It is therefore not clear from these studies whether prices which tend to change frequently and by large amounts – e.g., due to large and frequent changes in sector specific conditions – also change readily to macroeconomic shocks. Clarifying this issue is particularly relevant to understand the e�ects of monetary policy. If fact, if prices were adjusting rapidly to monetary shocks, monetary policy would have little and only short-lived e�ects on economic activity, as in the model of Golosov and Lucas (2004). Our paper thus complements Bils and Klenow’s (2004) study by documenting when and by how much various prices are changed following a monetary policy shock. 

Since Bernanke and Blinder (1992) and Sims (1992), it is common to use VARs to trace out the e�ects of monetary policy innovations on macroeconomic variables. VARs are particularly convenient for this as they merely require the identification of monetary policy shocks, leaving the rest of the macroeconomic model unrestricted. To maintain enough degrees of freedom, estimated VARs are typically low-dimensional, involving in general no more than six to eight variables.<sup>9</sup> The small size of traditional VARs has however been criticized. In fact estimated monetary policy innovations are likely to be biased in small-sized VARs to the extent that central banks and the private sector make decisions on the basis of information not considered in these VARs. A common illustration of this problem is the “price-puzzle”, i.e., the finding that the price level tends to increase slightly after a contractionary money policy shock, which contradicts most standard theories (see Sims, 1992). Another problem with small-sized VARs is that they don’t allow us to understand the e�ects of monetary 

> 9Leeper, Sims and Zha (1996), using Bayesian priors consider slightly larger VARs containing up to about 20 variables. 

16 

policy shocks on a large number of variables of interest. 

Fortunately, as argued in BBE, the FAVAR described above allows us to address both of these shortcomings of traditional VAR. BBE provide a characterization of the e�ects of monetary policy on about twenty macroeconomic variables using estimated factors. In this paper, we focus on the e�ects of monetary policy on our large panel of prices. 

##### 4.2.1 Identification of monetary policy shocks 

To identify the monetary policy shock, we follow the strategy described in BBE. The assumption is that none of the latent common components of the economy responds within a month to unanticipated changes in monetary policy. This is the FAVAR extension of the standard recursive identification of monetary policy shock in standard VARs. To implement it in a FAVAR, we need to account for the added di�culty that the principal components are not associated with any particular economic concepts. However, when the number of data series � is large, the principal components estimated from the entire data set, �<sup>ˆ</sup> (�����), have the property that they should consistently recover � + 1 independent, but arbitrary, linear combinations of the latent factors �� and the observed common factor, i.e., the Federal funds rate ��. Since �� is not explicitly imposed as a common component in the first step, any of the linear combinations underlying �<sup>ˆ</sup> (�����) could involve the Fed’s policy instrument, ��. It would thus not be valid to simply estimate a VAR in �<sup>ˆ</sup> (�����) and ��, and identify the policy shock recursively. Instead, the direct dependence of �<sup>ˆ</sup> (�����) on �� must first be removed, which is achieved by exploiting a subset of the variables – prices and real-activity measures, but not financial variables – that are assumed not to respond within the month to changes in monetary policy. We refer readers to BBE for details on the implementation of the 

17 

##### 4.2.2 Responses to monetary policy shocks 

We proceed with a description of the response of our data series to a monetary policy shocks, i.e., an unexpected increase (of one standard deviation) of the Federal funds rate. Figure – 2a shows the response of the Federal funds rate, the index of industrial production as an aggregate measure of economic activity –, and an aggregate price index (PCE deflator). The solid line shows the responses generated by our FAVAR and the dashed lines show the responses obtained from a standard VAR that include these three variables only.<sup>10</sup> Figure 2b shows similar impulse responses except that the VAR is estimated using the consumer price index (CPI) instead of the PCE deflator. 

One important feature of this figure is that the responses of the price index and industrial production are very di�erent for the FAVAR and the VAR. The VAR displays a price puzzle and a large e�ect of monetary policy on industrial production after four years, which is inconsistent with long-run money neutrality. The price puzzle is especially important for the VAR using the CPI data, in Figure 2b. Instead the FAVAR displays a more conventional response of industrial production, and essentially no response of the price index for the first few months following a monetary policy shock. As discussed in BBE, since the FAVAR nests the VAR specification, this suggests that the FAVAR is able to exploit the relevant information from the data set, that Sims (1992) argued may be missing from small-sized VARs. Note that if the additional series added to the dataset were irrelevant, they should not bias the estimated response, but they should rather result in less precise estimates. As a result, the fact that the responses of the price index and the industrial production are di�erent for both specifications suggests that the FAVAR is exploiting relevant information, especially for the CPI data, in Figure 2b. 

We now turn to the responses of more disaggregated price series to the monetary policy shock. The FAVAR is perfectly suited for such an exercise as it allows us to compute directly 

> 10The VAR includes 13 lags as is the case for the estimated equation (1) in the FAVAR. 

18 

the responses of all of the variables in the data set. The Figures 3a-3h show the responses of the disaggregated price indices. (For lack of space we didn’t include in this figure all of the PCE price responses; we present only the responses constructed for the higher level aggregates; the responses of the most disaggregated series look similar and are all reported on the Figure 4, which we discuss below). As can be seen from the first row of plots in Figure 3a, the aggregate prices of nondurable goods and services show little response for several months following the shock, and then fall progressively. The prices of durable goods however start falling more rapidly than nondurables and services, a fact noted by Erceg and Levin (2002) and Barsky, House and Kimball (2003), and attributed to the greater interest-rate sensitivity of durable goods. These price indices do not reveal a price puzzle. 

Looking at the other, more disaggregated price responses, while we observe some heterogeneity in the responses, a striking feature is that most indices respond very little for several months following the shock, and start falling only later. In addition, only very few sectors display an important price puzzle. Recall that in order to identify the monetary policy shock, we assume that individual prices do not respond within the same month to changes in the Federal funds rate. However nothing in the estimated FAVAR constrains the response of price series in all months following the monetary policy shock. We report in Figures 3c-3i the responses of PPI components to the same monetary policy shock. As for consumer prices, most components of the PPI respond only several months after the monetary policy shock. 

Figure 4a summarizes the price responses. The left panels of the figure report on the same graph all of the disaggregated price responses to the monetary shock, along with the unweighted average response (thick solid line) and the response of the overall price index (thick dashed line). It is interesting to note that the average price responses to a monetary shock and the response of the aggregate price indices are very similar. This suggests that the weights used in aggregate price indices do not play an important role in characterizing the response in the overall price indices. The figure makes it clear that 

19 

most of the disaggregated prices move little in the 6 months following the monetary shock, and start decreasing thereafter. As reported in Table 2, the cumulative decline in prices is only 0.09% over the first 6 months, but reaches 0.43% when cumulated over the first 12 months. The drop in prices is more pronounced for producer prices with a cumulated decline of 0.78% over the first year than for consumer prices (cumulated decline of 0.15%). When they start falling following the monetary shock, prices tend to decline fairly steadily for a couple of years. This results in quite a persistent inflation rate. As reported in Table 2, the autocorrelation coe�cients of inflation conditional on a monetary shock are all very high. 

Figure 4b represents the impulse responses of the PCE quantities to the same monetary policy shock. While on average the real consumption responses tend to fall subsequent to the monetary shock, before reverting back to the initial level, there is considerable variation across sectors. As for the price responses, the average real consumption responses displays some persistence. Interestingly, sectors in which prices fall the most following a monetary shock tend to be sectors in which quantities fall the least, as indicated in Figure 5. This figure displays the scatter plot across PCE categories of the cumulated responses of prices and quantities following the monetary shock, and the regression line reveals a significant and negative slope. Similar pictures are obtained for longer horizons. 

To the extent that one is interested in characterizing the behavior of the economy in response to monetary policy actions, our results provide empirical support for features such as price rigidities and inflation persistence often embedded in monetary models. Our findings, however, contrast sharply with those of Bils, Klenow, and Kryvtsov (2003) and Balke and Wynne (2003) which call for a rejection of conventional sticky-price models. These authors found the opposite conclusion mainly because they estimate an important price puzzle. 

Bils, Klenow, and Kryvtsov (2003) estimate the responses of 123 components of the CPI to a Federal funds innovation, where the latter innovations are extracted from a 7-variable monthly VAR. As the VAR is estimated independently from the disaggregated price data, 

20 

the responses obtained constitute only a rough estimates of the price responses. Based on frequencies of price adjustments reported in Bils and Klenow (2004), they consider two – – categories of price responses the flexible price and sticky price categories and they report the responses of the prices in both categories as well as their ratio. They argue that the movements in relative prices are inconsistent with a popular sticky-price model. Following an expansionary monetary policy shock, their estimated relative price (of flexible prices relative to sticky prices) declines initially and then increases, while in the model, the relative price increases temporarily before reverting back to zero. However, the main reason for their finding of an unconventional relative price response in the data is related to the fact that their estimate of flexible-price responses display a price puzzle: the flexible prices fall initially in response a monetary policy expansion, and increase only later. In contrast, sticky prices do not show significant dynamics in the first 20 months. 

Balke and Wynne (2003), instead, focus on components of the producer price index. After estimating a small-sized VAR and the response of components of the PPI to an identified monetary policy shock, they also find a substantial price puzzle in individual series, and thus conclude similarly to Bils, Klenow and Kryvtsov (2003) that the implied estimated evolution of relative prices in inconsistent with that predicted by sticky price models. 

These studies make two key assumptions about the behavior of the macro-economy: i) that the macroeconomic dynamics can be properly uncovered from a small set of macroeconomic indicators, and ii) that macroeconomic dynamics can be modeled separately from the disaggregated prices. Based on the results of BBE, and as argued above, the first assumption does not seem to be empirically valid and could be responsible for finding a price puzzle. The second assumption implies that disaggregated prices only have an e�ect on the macroeconomy through an observed aggregate index. The FAVAR framework that we consider in this paper relaxes these two assumptions as it allows us to incorporate more information in the estimation of the macroeconomic dynamics, and to model the disaggregated dynamics in 

21 

a more flexible fashion. Interestingly, in contrast to these studies, we don’t find any evidence of price puzzle in our estimated FAVAR. This implies that the ratio of flexible to sticky prices behaves as predicted by sticky price models. 

##### 4.2.3 Responses to other shocks 

One advantage of studying the responses of prices to monetary shocks is that this can be done with a minimum amount of identifying restrictions in the FAVAR. To investigate the e�ects of other macreconomic shocks would require arguably more controversial identifying assumptions. To get a sense whether the results just described apply more generally for other macroeconomic shocks, we determine the responses of each sectorial price to an innovation (of minus one standard deviation) to its common component �<sup>0</sup> �<sup>���We report these responses</sup> of all price series in the middle column of Figure 4a, and do the same for the PCE quantities in Figure 4b. As for the monetary shock, the prices fall by a relatively moderate amount in the first couple of months after the shock, but then continue to fall over the subsequent months. This reveals again some sluggishness in the responses of prices to macroeconomic disturbances. Of course, as we don’t identify any structural macroeconomic shock in this exercise, the results are only suggestive. They don’t allow us to exclude the possibility that there exist macroeconomic disturbances which cause a rapid and permanent change in prices. 

While disaggregated prices appear to respond with a long lag to monetary policy shocks, and then decline steadily for a while, these prices respond sharply and very promptly to sector-specific disturbances, and tend to reach their new equilibrium level shortly after the shock. This can be seen from the two right panels of Figure 4a which report the (log) price level responses to an adverse sector-specific shock, i.e., a drop in ��� by one standard deviation. Inflation rates show no persistence in response to the sector-specific shock, in contrast to the response to monetary shocks. Our analysis does not allow us to uncover the structural disturbances that a�ect sectorial prices, so that we cannot disentangle to what extent the 

22 

di�erences in responses to monetary shocks and sector specific shocks are attributable to the shocks themselves and to the price responses to these shocks. These results do however suggest that prices respond di�erently to macroeconomic shocks (such as monetary policy shocks) and to sector specific shocks. 

## 5 Sectorial Results 

This section is organized in the following way: We first describe cross-sectional results from the FAVAR both for PCE deflators and for PPI, and then we report results from regressions of PPI impulse responses on various industry characteristics, including some of those derived from the FAVAR. 

#### 5.1 Correlations for consumer and producer prices 

In Tables 3, 4, and 5 we report the correlation matrices for key statistics from the FAVAR analysis. In the first table we calculate correlations by using both PCE deflators and PPI data, and the next two focus on PCE and PPI data separately. 

##### 5.1.1 Volatility of common and sectorial components 

Not surprisingly, the volatility of inflation is highly correlated both with the volatility of sectorial inflation shocks and with the volatility of the common components. As we documented in Figure 1, there is also a very high correlation between the volatility of idiosyncratic shocks (Sd(ei)) and the volatility of the common component (Sd(com)). This correlation is high both for PCE deflators (0.69) and for PPI data (0.78). From a statistical point of view, there is no reason to expect that the portion of inflation volatility explained by the regression (common component) and the portion of inflation volatility explained by the error terms should be correlated across industries (or samples). Therefore, Figure 1 presents an 

23 

interesting result that requires structural interpretation. It might be useful to note that the inflation variance explained by the macroeconomic factors depends on the loadings represented by the matrix �. One interpretation is that these loadings reflect the price setting behavior of firms in various industries. Under this interpretation, Figure 1 reveals that firms in industries with volatile idiosyncratic shocks do also respond strongly to macroeconomic shocks. As we mentioned, this is the case if frequent price adjustments necessitated by idiosyncratic volatility are also used as an opportunity to adjust to changes in the macroeconomic environment. That would be consistent, for instance, with a sticky price model a la Calvo with heterogeneity in the frequency of price adjustment across sectors as in Carvalho (2006). An alternative interpretation might be that industries with significant inherent volatility are riskier so that the degree of asymmetric information between firms and lenders is more acute (since it is more di�cult for lenders to determine the state of the world). In this case, more idiosyncratic volatility should make firms more vulnerable to changes in monetary policy, which is known to a�ect the wedge between internal and external financing (e.g. Bernanke and Gertler, 1995). In any case, the correlation is too strong to be ignored. Furthermore, it is suggestive of what price-setting assumptions might be more consistent with the data. 

##### 5.1.2 Persistence and volatility 

Bils and Klenow (2004) emphasize that, for a particular process for marginal costs, the Calvo model predicts that a higher degree of price stickiness reduces the impact of exogenous shocks on current inflation, but that it increases the persistence inflation. Thus everything else equal, in sectors with high price stickiness, the inflation rate should display a relatively low volatility and a relatively high persistence. Bils and Klenow (2004) argue that models such as the Calvo model are rejected by the data as they predict a strong negative correlation across sectors between the frequency of price adjustment and the persistence in sectorial inflation, while this correlation is positive in their data covering 123 consumer goods over 

24 

the period 1995-2000, and only mildly negative in their longer data set. 

While we do not have estimates of the frequency of price adjustment, as in Bils and Klenow (2004), we can nevertheless compare the correlations of inflation volatility and inflation persistence across sectors in our data set. Similarly to Bils and Klenow, we find a weakly negative correlation (-0.08) between volatility and persistence in the sector-specific component of inflation, as Table 3 indicates. Once we look at the common component of inflation, however, the persistence and the volatility of inflation are much more negatively correlated (-0.46). This explains in part why the Calvo model is more successful in describing the volatility and persistence of inflation fluctuations generated by macroeconomic disturbances, than those generated by sector-specific shocks. 

##### 5.1.3 Cumulated impulse responses and volatility of sectorial shocks 

Another set of interesting correlations pertains to the cumulative sum of the impulse responses to a monetary shocks over the first 6 months (sum6 ) and over the first 12 months (sum12 ). Two striking results are the strongly negative correlations of the cumulative sums (in the last two columns) with the volatility (Sd(ei)) and persistence of idiosyncratic shocks (rho(idio)). To interpret these correlations, we should point out that the sums of impulse responses are calculated for a contractionary monetary policy and therefore more negative numbers imply more price flexibility, i.e. faster price adjustment. 

As illustrated further in Figure 6, in sectors with small enough sectorial shocks there is almost no price response to monetary shocks over the first 6 months. However the larger the sector-specific volatility the higher the price responses to monetary policy shocks. This result confirms the interpretation of Figure 1, that industries with high inherent volatility adjust also faster to macroeconomic disturbances. Similar pictures are found for when we consider longer horizons. Such a finding appears consistent with the prediction of the state-dependent model of Gertler and Leahy (2006). In this model, firms are a�ected by idiosyncratic shocks 

25 

and face a cost of adjusting prices. The model predicts that the more firms are a�ected by idiosyncratic shocks, the more they adjust prices conditional on a monetary policy shock. Alternatively, by referring to the costs of processing information, Reis (2006) presents a model of inattentive producers in which a higher volatility of shocks requires more frequent price updating. 

In addition, we note that from Tables 3 — 5 that the persistence of the idiosyncratic shocks is again negatively related to the responses of prices to monetary policy shocks. One possible interpretation is that in industries where we observe more persistence of the idiosyncratic component, firms adjust immediately to any shock because both common and idiosyncratic components are persistent. Those firms that experience rather transient idiosyncratic shocks wait to see if the current shock is persistent (macroeconomic) or not (idiosyncratic) and adjust only with a delay. Of course, these are raw correlations and it is not clear whether any of these relationships will remain significant after controlling for example for the degree of competition in the industry. Accordingly, we turn now to regression analysis. 

#### 5.2 Cross-sectional variation in the producer price indices 

For the producer price series we have collected data on industry characteristics by NAICS codes. We can match now the responses of prices to these characteristics. Our goal is to provide evidence on the main explanatory factors for the dispersion in price responses observed in Figure 4. To address this question we start with the following specification of the cross-industry price responses: 



where �������� is the cumulative deviation of the price level in industry � after a monetary policy shock, � periods after the shock. We present results for the deviation of prices 6 

26 

and 12 months after the shock. ����� denotes the degree of competition. We also use two variables from the factor analysis: ��(�)� is a measure of the volatility of the idiosyncratic component and ���(�)� is the persistence of this component. To check robustness we will also add other controls and deterministic components like dummy variables. 

We start in Table 6 by using as a dependent variable the cumulative sum of price responses over the first six months. Column (1) reports that profit rates are strongly and positively correlated with price responses. Since our price variable is on average negative and higher flexibility implies more negative cumulative deviation, the result implies that more competitive industries (lower profit rates) have higher price flexibility. The mean profit rate is about 25% and a movement from the mean to a profit rate of 35% implies 0.15 percentage points smaller cumulated price change 6 months following a policy shock. This is consistent with standard sticky price models (see e.g., Woodford, 2003), as well as with theories based on rational inattention (Reis, 2006). In column (5), we include three dummy variables to control — for potentially di�erent average price dynamics. We use three broad categories food and textiles (NAICS codes starting with 31; dummy is coded as d1 ); paper, wood, chemicals (codes with 32; dummy is denoted by d2 ); and metallurgy, electronics and machinery (codes with 33; dummy is denoted by d3 ). In all three cases the intercepts are negative signifying the absence on average of a price puzzle. Notably the extra flexibility of the model improves the fit, but does not alter the coe�cient on profit rates. In column (6), by including an interaction term we test whether the relationship between market power and price flexibility di�ers across major industry categories, but we find little evidence of changes across major categories. 

This positive relationship between price stickiness and competition within each sector contrasts with Bils and Klenow’s finding (2004) that their preferred measure of market – – power the C4 ratio becomes insignificant once they control for prices of raw material goods. As in Bils and Klenow, we also find that the C4 ratio is not a robust predictor of 

27 

price dynamics. We use the inverse of the ratio as a measure of elasticity of demand, and we report in column (2) that the inverse of the C4 ratio is not significantly related to price dynamics. However, our results based on mean profit rates imply that for producer prices, market power is robustly related to price dynamics in response to monetary shocks. 

— Columns (3) and (4) confirm the correlation from the correlation matrix both idiosyncratic volatility and persistence are negatively related to price impulse responses. This implies that firms in industries with persistent and volatile idiosyncratic shocks adjust rapidly to changes in the macroeconomic environment. Interestingly, the result survives once we include as controls profit rates (column (7)) and the three dummy variables defined above (not shown in this table). 

As a robustness check, we turn now to the results based on the cumulative response over the first 12 months. The results confirm the importance of market power as measured by profit rates and also confirm the importance of the volatility of the idiosyncratic shocks (�� (��)) and its persistence measure (��� (�)�). As before, the C4 is insignificant. Finally, in Table 8 we report regressions results for the price impulse responses from the 7th to the 12th month after the shock, and find again similar results. In column (8) we include also the sum of the impulse responses in the initial 6 months. The coe�cient is highly significant and positive indicating that a larger portion of the price adjustment occurs in this second 6-month period. 

To sum up, our sectorial analysis indicates that as predicted by models based on monopolistic competition, prices adjust more sluggishly in industries in which market power is higher. In addition we uncovered two other important: idiosyncratic volatility, and the persistence of industry-specific shocks. 

28 

## 6 Conclusion 

In this paper, we disentangle the fluctuations in disaggregated U.S. consumer and producer prices which are due to aggregate macroeconomic shocks from those due to shocks to individual price series. We do so by estimating a factor-augmented VAR that relates a large panel of economic indicators and of individual price series to a relatively small number of estimated common factors. After identifying monetary policy shocks using all of the information available, we estimate consistently the e�ects of U.S. monetary policy on disaggregated prices. This is important not only to get a better understanding of the nature of the fluctuations in disaggregated prices, and of how prices react to macroeconomic shocks, but also to assess the impact of monetary policy on prices in various sectors. 

We obtain several empirical results that can be summarized as follows: 

First, at the level of disaggregation considered, most of the sectorial prices fluctuations appear to be due to sector-specific factors, and only about 15% of individual sectorial price fluctuations, on average, are due to aggregate macroeconomic factors. 

Second, individual price fluctuations are relatively persistent, but this persistence is essentially due to the very high degree of persistence in the components driven by common or macroeconomic shocks, and not to sector-specific disturbances. While sector-specific shocks may cause large fluctuations in the individual prices, these fluctuations are typically short lived. Aggregate macroeconomic shocks instead tend to have more persistent e�ects on a wide range of sectorial prices. 

Third, in the context of our estimated FAVAR, the responses of disaggregated prices to a monetary policy shock display very little evidence of a price puzzle, in agreement with conventional economic models, but in contrast to the results routinely obtained in VAR studies. This suggests that by exploiting a large information set in the estimation, we may obtain more accurate estimates of the e�ects of monetary policy. 

Fourth, while individual price series reveal some heterogeneity in their responses to an 

29 

unexpected monetary policy tightening, a striking feature is that most indices respond very little for several months following the shock, and start falling only later. PCE categories in which prices fall the most tend furthermore to be those in which quantities consumed fall the least. 

Fifth, we find that price responses to monetary policy shocks tend to display larger changes the more volatile and persistent are sector-specific shocks. 

Finally, we document that price responses are strongly correlated with the degree of imperfect competition. In industries with low average profit rates, we observe a rapid response of prices to monetary policy. 

This paper has attempted to present stylized facts on the response of disaggregated U.S. prices to various shocks for the period 1976-2005. An evaluation of various models on the basis of stylized facts provided here is beyond the scope of this paper. We hope however that these stylized facts will help researchers develop improved models of price determination. Our findings suggest that sectorial prices respond di�erently to macroeconomic and sectorspecific shocks. This may explain why sticky-price models such as the Calvo model have been so popular in characterizing the e�ects of monetary policy actions on aggregate variables, while they have been sharply criticized at the same time by authors focused on disaggregate price series. 

Clearly, is would be desirable to have models that can fully account for the responses of aggregate and disaggregated prices to both macroeconomic and sector-specific disturbances. Some recent papers are very promising in this respect. Carvalho (2006) generalizes the Calvo model to allow for heterogeneity in price stickiness across sectors. He finds that in the presence of strategic complementarities, firms which adjust prices infrequently have a disproportionately large e�ect on the decisions of other firms, and thus on the aggregate price level. Even if most sectors have relatively flexible prices, and thus respond quickly to sector-specific disturbances, they may respond sluggishly to nominal shocks. Gertler 

30 

and Leahy (2006) propose a simple state-dependent pricing model that involves volatile prices due to idiosyncratic shocks, but that predicts sluggish price responses to a monetary shock, as reported here, due to real rigidities. The model also predicts that a high volatility of idiosyncratic shocks should be associated with more volatile prices and a more volatile response to monetary shocks, as we found in the data. In yet another direction, recent models on rational inattention such as those proposed by Reis (2006) and Ma´ckowiak and Wiederholt (2006) are also able to generate di�erent responses of sectorial prices to sectorspecific shocks and aggregate shocks. The model of Reis (2006), for instance predicts that (i) stickiness is higher in industries with low price elasticity of demand; (ii) costs of processing information are positively related with inattentiveness; (iii) volatility of shocks requires more frequent updating. We leave for future work a direct comparison of the prediction of these models. 

31 

## References 

- [1] Altissimo, Filippo, Benoît Mojon, and Paolo Za�aroni (2004), “Fast Micro and Slow Macro: Can Aggregation Explain the Persistence of Inflation?” manuscript, European Central Bank. 

- [2] Aoki, Kosuke (2001), “Optimal Monetary Policy Responses to Relative Price Changes,” Journal of Monetary Economics 48: 55-80. 

- [3] Bai, Jushan (2003), “Inferential Theory for Factor Models of Large Dimensions,” Econometrica 71(1): 135-72. 

- [4] Balke, Nathan S., and Mark A. Wynne (2003), “The Relative Price E�ects of Monetary Shocks,” FRB Dallas, Working Paper no. 0306. 

- [5] Ball, Laurence, and David Romer (1990), “Real Rigidities and the Non-Neutrality of Money,” Review of Economic Studies 57: 183-203. 

- [6] Barro, Robert J. (1972), “A Theory of Monopolistic Price Adjustment,” Review of Economic Studies 39: 17-26. 

- [7] Barsky, Robert, Christopher L. House, and Miles Kimball (2003), “Do Flexible Goods Prices Undermine Sticky Price Models?” NBER Working Paper 9832. 

- [8] Benigno, Pierpaolo (2003), “Optimal Monetary Policy in a Currency Area,” Journal of International Economics. 

- [9] Bernanke, Ben S., and Alan S. Blinder (1992), “The Federal Funds Rate and the Channels of Monetary Transmission,” American Economic Review 82(4): 901-921. 

- [10] Bernanke, Ben S., Jean Boivin and Piotr Eliasz (2005), “Measuring Monetary Policy: A Factor Augmented Vector Autoregressive (FAVAR) Approach,” Quarterly Journal of Economics 120(1): 387-422. 

32 

- [11] Bernanke, Ben S. and Mark Gertler (1995), “Inside the Black Box: The Credit Channel of Monetary Policy Transmission,” Journal of Economic Perspectives 9, 27-48. 

- [12] Bils, Mark, and Peter J. Klenow (2004), “Some Evidence on the Importance of Sticky Prices,” Journal of Political Economy 112(5): 947-985. 

- [13] Bils, Mark, Peter J. Klenow, and Oleksiy Kryvtsov (2003), “Sticky Prices and Monetary Policy Shocks,” Federal Reserve Bank of Minneapolis Quarterly Review 27(1): 2-9. 

- [14] Blinder, Alan S., Elie R. D. Canetti, David E. Lebow, and Jeremy B. Rudd (1998), Asking About Prices: A New Approach to Understanding Price Stickiness, Russell Sage Foundation, New York. 

- [15] Boivin, Jean, and Serena Ng (2005), “Understanding and Comparing Factor-Based Forecasts,” International Journal of Central Banking 1(3): 117-151. 

- [16] Carlton, Dennis W. (1986), “The Rigidity of Prices,” American Economic Review 76, 637-658. 

- [17] Carvalho, Carlos (2006), “Heterogeneity in Price Stickiness and the New Keynesian Phillips Curve,” Manuscript, Princeton University. 

- [18] Cecchetti, Stephen G. (1986), “The Frequency of Price Adjustment: A Study of the Newsstand Prices of Magazines,” Journal of Econometrics 31, 255-274. 

- [19] Christiano, Lawrence J., Martin Eichenbaum, and Charles Evans (1999), “Monetary Policy Shocks: What Have We Learned and to What End?” in J. Taylor and M. Woodford, eds., Handbook of Macroeconomics, Vol. 1A, Chap. 2. Amsterdam: North-Holland. 

- [20] Christiano, Lawrence J., Martin Eichenbaum, and Charles Evans (2005), “Nominal Rigidities and the Dynamic E�ect of a Shock to Monetary Policy,” Journal of Political Economy 113(1): 1-45. 

33 

- [21] Clark, Todd E. (2003), “Disaggregate Evidence on the Persistence of Consumer Price Inflation,” manuscript, Federal Reserve Bank of Kansas City. 

- [22] Cogley, Timothy, and Thomas J. Sargent (2001), “Evolving Post-World War II U.S. Inflation Dynamics,” NBER Macroeconomics Annual 16: 331-373. 

- [23] Cogley, Timothy, and Thomas J. Sargent (2005), “Drifts and Volatilities: Monetary Policies and Outcomes in the Post WWII US,” Review of Economic Dynamics 8: 262— 302. 

- [24] Dhyne, E., L. Álvarez, H. Le Bihan, G. Veronese, D. Dias, J. Ho�man, N. Jonker, P. Lünnemann, F. Rumler and J. Vilmunen (2005), “Price Setting in the Euro Area: Some Stylised Facts from Individual Consumer Price Data,” European Central Bank Working Paper no. 524. 

- [25] Erceg, Christopher, and Andrew T. Levin (2002), “Optimal Monetary Policy with Durable Consumption Goods,” International Finance Discussion Paper #748, Board of Governors of the Federal Reserve System. 

- [26] Fougere, Le Bihan, Servestre (2005), “Heterogeneity in Consumer Price Stickiness: A Microeconometric Investigation,” CEPR DP5300. 

- [27] Fuhrer, Je�rey C. and George R. Moore (1995), “Inflation Persistence,” Quarterly Journal of Economics 110, 127-159. 

- [28] Galí, Jordi, and Mark Gertler (1999), “Inflation Dynamics: A Structural Econometric Analysis,” Journal of Monetary Economics 44, 195-222. 

- [29] Gertler, Mark, and John Leahy (2006), “A Phillips Curve with an SS Foundation,” NBER Working Paper 11971. 

34 

- [30] Golosov, Mikhail, and Robert E. Lucas (2003), “Menu Costs and Phillips Curves,” NBER Working Paper 10187. 

- [31] Imbs, Jean, Haroon Mumtaz, Morten O. Ravn, and Helene Rey (2005), “PPP Strikes Back: Aggregation and the Real Exchange Rate,” forthcoming in Quarterly Journal of Economics. 

- [32] Kackmeister, Alan (2001), “Has Retail Price Behavior Changed Since 1889? Evidence from Microdata,” manuscript, University of California, Berkeley. 

- [33] Kashyap, Anil K. (1995), “Sticky Prices: New Evidence from Retail Catalogs,” Quarterly Journal of Economics 110, 245-274. 

- [34] Klenow, Peter J. and Oleksiy Kryvtsov (2005) “State-dependent or Time-dependent Pricing: Does It Matter for Recent US Inflation?” NBER WP 11043. 

- [35] Levin, Andrew T., and Jeremy Piger (2003), “Is Inflation Persistence Intrinsic in Industrial Economies?” Working Paper 2002-023B, Federal Reserve Bank of St. Louis. 

- [36] Levy, Daniel, Mark Bergen, Shantanu Dutta, and Robert Venable (1997), “The Magnitude of Menu Costs: Direct Evidence from Large U.S. Supermarket Chains,” Quarterly Journal of Economics 112 (3), 791-823. 

- [37] MacDonald, James N. and Daniel Aaronson (2001), “How Do Retail Prices React to Minimum Wage Increases?” manuscript, U.S. Department of Agriculture. 

- [38] Ma´ckowiak, Bartosz, and Mirko Wiederholt (2006), “Optimal Sticky Prices under Rational Inattention,” manuscript, Humboldt University, Berlin. 

- [39] Nakamura, Emi, and Jón Steinsson (2006), “Five Facts About Prices: A Reevaluation of Menu Cost Models,” manuscript, Harvard University. 

35 

- [40] Pesaran, M. Hashem, and Ron Smith (1995), “Estimating Long-Run Relationships From Dynamic Heterogenous Panels,” Journal of Econometrics 68: 79-113. 

- [41] Pivetta, Frederic, and Ricardo Reis (2003), “The Persistence of Inflation in the United States,” manuscript, Harvard University. 

- [42] Reis, Ricardo (2006), “Inattentive Producers,” Review of Economic Studies 73(1): 1-29. 

- [43] Rotemberg, Julio J., and Michael Woodford (1997), “An Optimization-Based Econometric Framework for the Evaluation of Monetary Policy,” NBER Macroeconomics Annual, 297-346. 

- [44] Sims, Christopher A. (1992), “Interpreting the Macroeconomic Time Series Facts: The E�ects of Monetary Policy,” European Economic Review, 36(5), 975-1000. 

- [45] Sims, Christopher A. (2001), “Comment on ‘Evolving Post-World War II U.S. Inflation Dynamics,” NBER Macroeconomics Annual 16, 373-79. 

- [46] Smets, Frank, and Raf Wouters (2004), “Shocks and Frictions in US Business Cycles: A Bayesian DSGE Approach,” manuscript, April. 

- [47] Stock, James H. (2001), “Comment on ‘Evolving Post-World War II U.S. Inflation Dynamics,” NBER Macroeconomics Annual 16, 379-87. 

- [48] Stock, James H., and Mark W. Watson (1999), “Forecasting Inflation,” Journal of Monetary Economics 44, 293-335. 

- [49] Stock, James H., and Mark W. Watson (2002), “Macroeconomic Forecasting Using Di�usion Indexes,” Journal of Business Economics and Statistics 20(2), 147-162. 

- [50] Woodford, Michael (2003), Interest and Prices: Foundations of a Theory of Monetary Policy, Princeton, Princeton University Press. 

36 

###### **Table 1: Volatility and persistence of inflation series** 

|||Stand|ard deviati|on||P|ersistence||
|---|---|---|---|---|---|---|---|---|
|||Inflation|Common<br>comp.|Sector-<br>specific|R2|Inflation|Common<br>comp.|Sector-<br>specific|
|**_Aggre_**|**_gated series_**||||||||
|**PCE**|Total|0.24|0.21|0.11|0.77|0.90|0.95|0.13|
||Durables|0.33|0.25|0.21|0.60|0.88|0.97|0.08|
||Nondurables|0.42|0.30|0.30|0.50|0.44|0.91|0.22|
||Services|0.24|0.19|0.14|0.63|0.91|0.98|0.01|
|**_Disag_**|**_gregated series_**||||||||
|**All**|Average|1.15|0.33|1.08|0.15|0.29|0.91|-0.03|
||Median|0.75|0.27|0.71|0.12|0.30|0.93|-0.02|
||Minimum|0.23|0.08|0.13|0.01|-2.32|0.39|-1.83|
||Maximum|11.67|1.85|11.59|0.68|0.96|0.99|0.87|
||Std|1.14|0.22|1.13|0.12|0.39|0.06|0.33|
|**PCE**|Average|0.97|0.29|0.92|0.17|0.30|0.92|-0.05|
||Average (weighted)|0.88|0.31|0.80|0.27|0.47|0.93|0.04|
||Median|0.65|0.23|0.60|0.12|0.36|0.95|-0.02|
||Minimum|0.23|0.08|0.13|0.01|-2.32|0.39|-1.83|
||Maximum|11.67|1.85|11.59|0.68|0.96|0.99|0.87|
||Std|1.10|0.23|1.09|0.15|0.44|0.07|0.37|
|**PPI**|Average|1.36|0.38|1.29|0.13|0.28|0.90|0.01|
||Median|0.92|0.30|0.87|0.11|0.27|0.91|-0.01|
||Minimum|0.35|0.08|0.29|0.01|-0.76|0.61|-0.93|
||Maximum|7.73|1.15|7.66|0.43|0.91|0.98|0.63|
||Std|1.15|0.21|1.15|0.08|0.31|0.06|0.27|



Note: Weighted average of statistics for disaggregated PCE series is obtained using expenditure shares in year 2005 as weights. 

**Table 2: Response of price series to a monetary policy shock** 

|||Autocorrel|ation of �it|conditional|on shock|Cumul. price r|esponses|
|---|---|---|---|---|---|---|---|
|||1st-order|3rd-order|6th-order|12th-order|6 mths|12 mths|
|**_Aggre_**|**_gated series_**|||||||
|**PCE**|Total|0.97|0.91|0.82|0.63|-0.02|-0.21|
||Durables|0.97|0.90|0.80|0.61|-0.06|-0.21|
||Nondurables|0.98|0.93|0.84|0.67|-0.05|-0.54|
||Services|0.96|0.88|0.76|0.54|0.01|-0.02|
|**_Disag_**|**_gregated series_**|||||||
|**All**|Average|0.97|0.90|0.80|0.58|-0.09|-0.43|
||Median|0.97|0.91|0.81|0.62|0.00|-0.14|
||Minimum|0.93|0.79|0.54|0.18|-1.96|-6.23|
||Maximum|1.00|0.98|0.93|0.78|0.83|1.68|
||Std|0.01|0.04|0.07|0.13|0.35|1.00|
|**PCE**|Average|0.97|0.89|0.78|0.55|-0.01|-0.15|
||Average (weighted)|0.97|0.89|0.78|0.55|-0.02|-0.20|
||Median|0.97|0.90|0.79|0.58|0.02|-0.05|
||Minimum|0.93|0.79|0.54|0.19|-0.91|-4.15|
||Maximum|1.00|0.98|0.93|0.78|0.61|1.48|
||Std|0.01|0.04|0.08|0.14|0.20|0.64|
|**PPI**|Average|0.97|0.92|0.82|0.63|-0.19|-0.78|
||Median|0.97|0.92|0.83|0.65|-0.05|-0.41|
||Minimum|0.94|0.82|0.62|0.18|-1.96|-6.23|
||Maximum|0.99|0.97|0.91|0.77|0.83|1.68|
||Std|0.01|0.03|0.06|0.11|0.46|1.23|



Note: Weighted average of statistics for disaggregated PCE series is obtained using expenditure shares in year 2005 as weights. 

|**sum12**<br>-0.49<br>-0.64<br>-0.48<br>0.13<br>-0.06<br>0.32<br>-0.26<br>-0.55<br>-0.54<br>-0.53<br>-0.52<br>0.90<br>1|
|---|
|**sum6**<br>-0.52<br>-0.49<br>-0.51<br>0.19<br>0.00<br>0.31<br>-0.19<br>-0.44<br>-0.42<br>-0.39<br>-0.39<br>1<br>0.90|
|**AC12**<br>0.16<br>0.21<br>0.15<br>-0.10<br>0.04<br>-0.20<br>0.13<br>0.84<br>0.92<br>0.97<br>1<br>-0.39<br>-0.52|
|**AC6**<br>0.20<br>0.24<br>0.20<br>-0.14<br>0.03<br>-0.21<br>0.15<br>0.93<br>0.98<br>1<br>0.97<br>-0.39<br>-0.53|
|**AC3**<br>0.26<br>0.28<br>0.26<br>-0.20<br>0.00<br>-0.27<br>0.17<br>0.98<br>1<br>0.98<br>0.92<br>-0.42<br>-0.54|
|**AC1**<br>0.30<br>0.30<br>0.30<br>-0.24<br>-0.02<br>-0.31<br>0.20<br>1<br>0.98<br>0.93<br>0.84<br>-0.44<br>-0.55|
|**rho(idio)**<br>-0.07<br>0.12<br>-0.08<br>0.27<br>0.59<br>-0.02<br>1<br>0.20<br>0.17<br>0.15<br>0.13<br>-0.19<br>-0.26<br>hock<br>hock<br>hock<br>icy shock|
|**o(Com)**<br>-0.57<br>-0.46<br>-0.57<br>0.38<br>0.41<br>1<br>-0.02<br>-0.31<br>-0.27<br>-0.21<br>-0.20<br>0.31<br>0.32<br>y policy s<br>ry policy s<br>ry policy s<br>netary pol|
|**ho(�_it) rh**<br>-0.38<br>-0.11<br>-0.40<br>0.65<br>1<br>0.41<br>0.59<br>-0.02<br>0.00<br>0.03<br>0.04<br>0.00<br>-0.06<br>it<br>a monetar<br>n a moneta<br>n a moneta<br>al on a mo<br>ds<br>iods|
|**R2**<br>**r**<br>-0.42<br>-0.12<br>-0.44<br>1<br>0.65<br>0.38<br>0.27<br>-0.24<br>-0.20<br>-0.14<br>-0.10<br>0.19<br>0.13<br>onent of �_<br>t of �_it<br>f �_it<br>t<br>nditional on<br>onditional o<br>nditional o<br>it condition<br>first 6 perio<br>first 12 per|
|**Sd(idio)**<br>1.00<br>0.74<br>1<br>-0.44<br>-0.40<br>-0.57<br>-0.08<br>0.30<br>0.26<br>0.20<br>0.15<br>-0.51<br>-0.48<br>_it<br>mmon comp<br>io componen<br>ponent �_it<br>component o<br>onent of �_i<br>on of  �_it co<br>on of  �_it c<br>on of  �_it co<br>elation of  �_<br>F of p_it over<br>F of p_it over|
|**Sd(Com)**<br>0.76<br>1<br>0.74<br>-0.12<br>-0.11<br>-0.46<br>0.12<br>0.30<br>0.28<br>0.24<br>0.21<br>-0.49<br>-0.64<br>viation of �<br>viation of co<br>viation of id<br>mmon com<br>of �_it<br>of common<br>of idio comp<br>utocorrelati<br>utocorrelati<br>utocorrelati<br>er autocorr<br>sum of IR<br>sum of IR|
|**Sd(�_it)**<br><br>1<br>0.76<br>1.00<br>-0.42<br>-0.38<br><br>-0.57<br>-0.07<br>0.30<br>0.26<br>0.20<br>0.16<br>-0.52<br>-0.49<br>Standard de<br>Standard de<br>Standard de<br>R2 of the co<br>Persistence<br>Persistence<br>Persistence<br>First-order a<br>Third-order a<br>Sixth-order a<br>Twelveth-ord<br>Cummulative<br>Cummulative|
|**Sd(�_it)**<br>**Sd(Com)**<br>**Sd(ei)**<br>**R2**<br>**rho(�_it)**<br>**rho(Com)**<br>**rho(idio)**<br>**AC1**<br>**AC3**<br>**AC6**<br>**AC12**<br>**sum6**<br>**sum12**<br>Sd(�_it)<br>Sd(Com)<br>Sd(ei)<br>R2<br>rho(�_it)<br>rho(Com)<br>rho(idio)<br>AC1<br>AC3<br>AC6<br>AC12<br>sum6<br>sum12|



|**sum12**<br>-0.36<br>-0.60<br>-0.34<br>0.03<br>-0.02<br>0.22<br>-0.13<br>-0.34<br>-0.38<br>-0.42<br>-0.47<br>0.76<br>1|
|---|
|**sum6**<br>-0.29<br>-0.26<br>-0.29<br>0.10<br>0.03<br>0.27<br>-0.10<br>-0.23<br>-0.26<br>-0.29<br>-0.35<br>1<br>0.76|
|**AC12**<br>0.18<br>0.16<br>0.18<br>-0.10<br>-0.06<br>-0.19<br>0.00<br>0.85<br>0.91<br>0.97<br>1<br>-0.35<br>-0.47|
|**AC6**<br>0.23<br>0.17<br>0.23<br>-0.14<br>-0.07<br>-0.18<br>0.01<br>0.94<br>0.98<br>1<br>0.97<br>-0.29<br>-0.42|
|**AC3**<br>0.25<br>0.18<br>0.25<br>-0.19<br>-0.10<br>-0.24<br>0.03<br>0.99<br>1<br>0.98<br>0.91<br>-0.26<br>-0.38|
|**AC1**<br>0.23<br>0.18<br>0.23<br>-0.22<br>-0.10<br>-0.26<br>0.06<br>1<br>0.99<br>0.94<br>0.85<br>-0.23<br>-0.34|
|**ho(idio)**<br>-0.23<br>-0.03<br>-0.24<br>0.33<br>0.63<br>0.15<br>1<br>0.06<br>0.03<br>0.01<br>0.00<br>-0.10<br>-0.13<br>ock<br>ock<br>ock<br>y shock|
|**o(Com)**<br>**r**<br>-0.61<br>-0.47<br>-0.61<br>0.35<br>0.55<br>1<br>0.15<br>-0.26<br>-0.24<br>-0.18<br>-0.19<br>0.27<br>0.22<br>y policy sh<br>ry policy sh<br>ry policy sh<br>netary polic|
|**rho(�_it) rh**<br>-0.48<br>-0.23<br>-0.49<br>0.65<br>1<br>0.55<br>0.63<br>-0.10<br>-0.10<br>-0.07<br>-0.06<br>0.03<br>-0.02<br>�_it<br>on a monetar<br>on a moneta<br>on a moneta<br>onal on a mo<br>riods<br>eriods|
|**R2**<br>-0.37<br>-0.08<br>-0.40<br>1<br>0.65<br>0.35<br>0.33<br>-0.22<br>-0.19<br>-0.14<br>-0.10<br>0.10<br>0.03<br>onent of<br>t of �_it<br>of �_it<br>it<br>nditional<br>onditional<br>onditional<br>_it conditi<br>first 6 pe<br>first 12 p|
|**Sd(idio)**<br>1.00<br>0.69<br>1<br>-0.40<br>-0.49<br>-0.61<br>-0.24<br>0.23<br>0.25<br>0.23<br>0.18<br>-0.29<br>-0.34<br>_it<br>ommon comp<br>io componen<br>ponent �_it<br>component<br>ponent of �_<br>on of  �_it co<br>ion of  �_it c<br>ion of  �_it c<br>relation of  �<br>F of p_it over<br>F of p_it over|
|**Sd(Com)**<br>0.73<br>1<br>0.69<br>-0.08<br>-0.23<br>-0.47<br>-0.03<br>0.18<br>0.18<br>0.17<br>0.16<br>-0.26<br>-0.60<br>viation of �<br>viation of c<br>viation of id<br>mmon com<br>of �_it<br>of common<br>of idio com<br>utocorrelati<br>autocorrelat<br>utocorrelat<br>der autocor<br>e sum of IR<br>e sum of IR|
|**Sd(�_it)**<br>1<br>0.73<br>1.00<br>-0.37<br><br>-0.48<br>**)**<br>-0.61<br>-0.23<br>0.23<br>0.25<br>0.23<br>0.18<br>-0.29<br>-0.36<br>Standard de<br>Standard de<br>Standard de<br>R2 of the co<br>Persistence<br><br>Persistence<br>Persistence<br>First-order a<br>Third-order<br>Sixth-order a<br>Twelveth-or<br>Cummulativ<br>Cummulativ|
|**Sd(�_it)**<br>**Sd(Com)**<br>**Sd(ei)**<br>**R2**<br>**rho(�_it)**<br>**rho(Com**<br>**rho(idio)**<br>**AC1**<br>**AC3**<br>**AC6**<br>**AC12**<br>**sum6**<br>**sum12**<br>Sd(�_it)<br>Sd(Com)<br>Sd(ei)<br>R2<br>rho(�_it)<br>rho(Com)<br>rho(idio)<br>AC1<br>AC3<br>AC6<br>AC12<br>sum6<br>sum12|



|**sum12**<br>-0.57<br>-0.72<br>-0.56<br>0.17<br>-0.14<br>0.36<br>-0.40<br>-0.75<br>-0.70<br>-0.62<br>-0.56<br>0.93<br>1|
|---|
|**sum6**<br>-0.66<br>-0.66<br>-0.65<br>0.26<br>-0.03<br>0.34<br>-0.28<br>-0.63<br>-0.55<br>-0.46<br>-0.41<br>1<br>0.93|
|**AC12**<br>0.00<br>0.19<br>-0.01<br>0.08<br>0.30<br>-0.08<br>0.35<br>0.78<br>0.92<br>0.98<br>1<br>-0.41<br>-0.56|
|**AC6**<br>0.06<br>0.24<br>0.05<br>0.05<br>0.29<br>-0.11<br>0.39<br>0.87<br>0.97<br>1<br>0.98<br>-0.46<br>-0.62|
|**AC3**<br>0.18<br>0.33<br>0.17<br>-0.03<br>0.26<br>-0.20<br>0.44<br>0.96<br>1<br>0.97<br>0.92<br>-0.55<br>-0.70|
|**AC1**<br>0.32<br>0.42<br>0.32<br>-0.12<br>0.21<br>-0.28<br>0.47<br>1<br>0.96<br>0.87<br>0.78<br>-0.63<br>-0.75|
|**ho(idio)**<br>0.13<br>0.35<br>0.12<br>0.19<br>0.53<br>-0.31<br>1<br>0.47<br>0.44<br>0.39<br>0.35<br>-0.28<br>-0.40<br>ock<br>ock<br>ock<br>y shock|
|**o(Com)**<br>**r**<br>-0.48<br>-0.39<br>-0.48<br>0.39<br>0.13<br>1<br>-0.31<br>-0.28<br>-0.20<br>-0.11<br>-0.08<br>0.34<br>0.36<br>y policy sh<br>ry policy sh<br>ry policy sh<br>netary polic|
|**ho(�_it) rh**<br>-0.24<br>0.11<br>-0.26<br>0.68<br>1<br>0.13<br>0.53<br>0.21<br>0.26<br>0.29<br>0.30<br>-0.03<br>-0.14<br>_it<br>n a monetar<br>n a moneta<br>n a moneta<br>al on a mo<br>ods<br>iods|
|**R2**<br>**r**<br>-0.50<br>-0.13<br>-0.53<br>1<br>0.68<br>0.39<br>0.19<br>-0.12<br>-0.03<br>0.05<br>0.08<br>0.26<br>0.17<br>onent of �<br>t of �_it<br>of �_it<br>it<br>nditional o<br>onditional o<br>onditional o<br>_it condition<br>first 6 peri<br>first 12 per|
|**Sd(idio)**<br>1.00<br>0.78<br>1<br>-0.53<br>-0.26<br>-0.48<br>0.12<br>0.32<br>0.17<br>0.05<br>-0.01<br>-0.65<br>-0.56<br>_it<br>ommon comp<br>io componen<br>ponent �_it<br>component<br>ponent of �_<br>on of  �_it co<br>ion of  �_it c<br>ion of  �_it c<br>relation of  �<br>F of p_it over<br>F of p_it over|
|**Sd(Com)**<br>0.80<br>1<br>0.78<br>-0.13<br>0.11<br>-0.39<br>0.35<br>0.42<br>0.33<br>0.24<br>0.19<br>-0.66<br>-0.72<br>viation of �<br>viation of c<br>viation of id<br>mmon com<br>of �_it<br>of common<br>of idio com<br>utocorrelati<br>autocorrelat<br>utocorrelat<br>der autocor<br>e sum of IR<br>e sum of IR|
|**Sd(�_it)**<br>1<br>0.80<br>1.00<br>-0.50<br><br>-0.24<br>**)**<br>-0.48<br>0.13<br>0.32<br>0.18<br>0.06<br>0.00<br>-0.66<br>-0.57<br>Standard de<br>Standard de<br>Standard de<br>R2 of the co<br>Persistence<br><br>Persistence<br>Persistence<br>First-order a<br>Third-order<br>Sixth-order a<br>Twelveth-or<br>Cummulativ<br>Cummulativ|
|**�_it)**<br>**Com)**<br>**i)**<br>**�_it)**<br>**Com**<br>**idio)**<br><br><br><br>**2**<br>**6**<br>**12**<br>_it)<br>om)<br>i)<br>�_it)<br>Com)<br>dio)<br><br><br><br>2<br>6<br>12|
|**Sd(**<br>**Sd(**<br>**Sd(e**<br>**R2**<br>**rho(**<br>**rho(**<br>**rho(**<br>**AC1**<br>**AC3**<br>**AC6**<br>**AC1**<br>**sum**<br>**sum**<br>Sd(�<br>Sd(C<br>Sd(e<br>R2<br>rho(<br>rho(<br>rho(i<br>AC1<br>AC3<br>AC6<br>AC1<br>sum<br>sum|



|(7)|-0.151<br>(0.132)<br>1.013<br>(0.449)*<br>-22.549<br>(3.769)**<br>-0.243<br>(0.116)*<br>149<br>0.50<br>t at 1%|
|---|---|
|(6)|-0.643<br>(0.161)**<br>-0.677<br>(0.282)*<br>-0.554<br>(0.225)*<br>1.454<br>(0.447)**<br>1.857<br>(0.864)*<br>1.699<br>(0.874)<br>149<br>0.27<br>otes significan|
|(5)|1.598<br>(0.368)**<br>-0.681<br>(0.138)**<br>-0.608<br>(0.138)**<br>-0.529<br>(0.103)**<br>149<br>0.27<br>5%; (**) den|
|(4)|-0.195<br>(0.036)**<br>-0.524<br>(0.129)**<br>151<br>0.09<br>significant at|
|(3)|0.142<br>(0.039)**<br>-25.932<br>(4.157)**<br>151<br>0.42<br>(*) denotes|
|(2)|-0.156<br>(0.072)*<br>-0.683<br>(2.034)<br>149<br>0.00<br>parentheses.|
|(1)|-0.569<br>(0.106)**<br>1.540<br>(0.355)**<br>149<br>0.13<br>ndard errors in|
||Constant<br>Gross Profit<br>Invc4<br>Sd(e)<br>rho(e)<br>d1<br>d2<br>d3<br>d1*profit<br>d2*profit<br>d3*profit<br>Observations<br>R-squared<br>Robust sta|



|(7)|-0.878<br>(0.319)**<br>2.973<br>(0.998)**<br>-47.903<br>(12.032)**<br>-1.105<br>(0.270)**<br>149<br>0.46<br>nt at 1%|
|---|---|
|(6)|-1.846<br>(0.323)**<br>-1.812<br>(0.404)**<br>-2.357<br>(0.692)**<br>3.909<br>(0.818)**<br>4.045<br>(1.163)**<br>6.876<br>(2.644)*<br>149<br>0.42<br>otes significa|
|(5)|4.699<br>(0.883)**<br>-2.055<br>(0.321)**<br>-1.987<br>(0.294)**<br>-1.822<br>(0.278)**<br>149<br>0.41<br>5%; (**) den|
|(4)|-0.774<br>(0.093)**<br>-1.844<br>(0.323)**<br>151<br>0.15<br>ignificant at|
|(3)|0.002<br>(0.134)<br>-59.502<br>(13.709)**<br>151<br>0.31<br>(*) denotes s|
|(2)|-0.629<br>(0.181)**<br>-3.023<br>(4.752)<br>149<br>0.00<br>parentheses.|
|(1)|-1.890<br>(0.264)**<br>4.597<br>(0.882)**<br>149<br>0.16<br>dard errors in|
||Constant<br>Gross Profit<br>Invc4<br>Sd(e)<br>rho(e)<br>d1<br>d2<br>d3<br>d1*profit<br>d2*profit<br>d3*profit<br>Observations<br>R-squared<br>Robust stan|



|(8)|-0.515<br>(0.110)**<br>0.541<br>(0.383)<br>6.242<br>(7.000)<br>-0.522<br>(0.152)**<br>1.401<br>(0.175)**<br>149<br>0.73|
|---|---|
|(7)|-0.727<br>(0.201)**<br>1.960<br>(0.604)**<br>-25.355<br>(8.914)**<br>-0.862<br>(0.180)**<br>149<br>0.40<br>nt at 1%|
|(6)|-1.203<br>(0.185)**<br>-1.134<br>(0.225)**<br>-1.802<br>(0.472)**<br>2.455<br>(0.428)**<br>2.189<br>(0.649)**<br>5.177<br>(1.787)**<br>149<br>0.47<br>otes significa|
|(5)|<br>3.101<br>(0.596)**<br> <br>-1.374<br>(0.207)**<br>-1.378<br>(0.193)**<br>-1.293<br>(0.193)**<br>149<br>0.45<br>5%; (**) den|
|(4)|-0.579<br>(0.061)**<br>-1.320<br>(0.212)**<br>151<br>0.18<br>ignificant at|
|(3)|-0.140<br>(0.100)<br>-33.570<br>(10.107)**<br>151<br>0.23<br>(*) denotes s|
|(2)|-0.472<br>(0.117)**<br>-2.340<br>(2.879)<br>149<br>0.00<br>parentheses.|
|(1)|-1.321<br>(0.180)**<br>3.057<br>(0.599)**<br>149<br>0.16<br>dard errors in|
||Constant<br>Gross Profit<br>Invc4<br>Sd(e)<br>rho(e)<br>Sum6<br>d1<br>d2<br>d3<br>d1*profit<br>d2*profit<br>d3*profit<br>Observations<br>R-squared<br>Robust stan|





<!-- Start of picture text -->
2<br>1.8<br>1.6<br>1.4<br>1.2<br>St.dev.(ei) = -0.14 + 3.70 * St.dev.(lambda_i*C) R2 = 0.54<br>1<br>0.8<br>0.6<br>Standard deviation of common components (lambda_i'*C)<br>Figure 1: Volatility of common and sector-specific components 0.4<br>0.2<br>0<br>14 12 10 8 6 4 2 0<br>Standard deviation of idio components (e_it)<br><!-- End of picture text -->



<!-- Start of picture text -->
Federal Funds Rate Industrial Production<br>0.1 0.2<br>0.08 0.1<br>0.06 0<br>0.04 -0.1<br>0.02 -0.2<br>0 -0.3<br>-0.02 -0.4<br>-0.04 -0.5<br>0 12 24 36 48 0 12 24 36 48<br>Price Level (PCE)<br>0.1<br>Baseline (FAVAR, 5 factors)<br>0 VAR [Ind. Prod., Price (PCE), FFR]<br>VAR [Ind. Prod., Price (PCE), FFR] & 1 factor<br>-0.1<br>-0.2<br>-0.3<br>-0.4<br>-0.5<br>-0.6<br>0 12 24 36 48<br><!-- End of picture text -->

Figure 2a: Estimated impulse responses to an identified monetary policy shock 



<!-- Start of picture text -->
Federal Funds Rate Industrial Production<br>0.1 0.3<br>0.08 0.2<br>0.06 0.1<br>0.04 0<br>0.02 -0.1<br>0 -0.2<br>-0.02 -0.3<br>-0.04 -0.4<br>0 12 24 36 48 0 12 24 36 48<br>Price Level (CPI)<br>0.2<br>Baseline (FAVAR, 5 factors)<br>VAR [Ind. Prod., Price (CPI), FFR]<br>0 VAR [Ind. Prod., Price (CPI), FFR] & 1 factor<br>-0.2<br>-0.4<br>-0.6<br>0 12 24 36 48<br><!-- End of picture text -->

Figure 2b: Estimated impulse responses to an identified monetary policy shock (CPI) 

|PCEP:NEW.AUTOS||0<br>48|PCEP:FURNITURE...|0<br>48|0<br>48<br>PCEP:OTHER.DUR|0<br>48<br>CEP:CLOTHING&SHOES|0<br>48<br>PCEP:TOBACCO|
|---|---|---|---|---|---|---|---|
|0.5|-0.5<br>0|-1|-0.5<br>0<br>0.5|-1|-1<br>-0.5<br>0<br>0.5|-1<br>-0.5<br>0<br>0.5<br>P|-1<br>-0.5<br>0<br>0.5<br>ck|
|0.5<br>PCEP:VEHICLES&PARTS|-0.5<br>0|0<br>48<br>-1|-0.5<br>0<br>0.5<br>PCEP:FURNITURE,TOT|0<br>48<br>-1|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:MISC.DUR.HOUSE|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:BOOKS&MAPS|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:OTHER.NONDUR<br>fed monetary policy sho|
|0.5<br>PCEP:SERVICES|-0.5<br>0|0<br>48<br>-1|-0.5<br>0<br>0.5<br>PCEP:TIRES...|0<br>48<br>-1|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:VIDEO&AUDIO|O<br>0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:JEWELRY&WATCHES|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:CLOTHING(M+B)<br>ulse responses to an identi|
|0.5<br>PCEP:NONDUR|-0.5<br>0|0<br>48<br>-1|-0.5<br>0<br>0.5<br>PCEP:OTHER.VEHICLES|0<br>48<br>-1|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:TABLEWARE...|DIC<br>0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:WHEEL,SPORTS&PHOT|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:CLOTHING(W+C)<br>Figure 3a: Estimated imp|
|PCEP:DUR||0<br>48|PCEP:USED.AUTOS|0<br>48|0<br>48<br>PCEP:KITCHEN...|0<br>48<br>OPHTHALMIC&ORTHOPE|0<br>48<br>PCEP:SHOES|
|0.5|-0.5<br>0|-1|-0.5<br>0<br>0.5|-1|-1<br>-0.5<br>0<br>0.5|-1<br>-0.5<br>0<br>0.5<br>PCEP:|-1<br>-0.5<br>0<br>0.5|



|PCEP:TOYS&SPORT||0<br>48<br>CEP:FLOWERS&PLANTS|0<br>48|0<br>48<br>PCEP:OTHER.HOUSING<br>0<br>48<br>CEP:LOCAL.TRANSPORT<br>0<br>48<br>PCEP:OTHER.PROFES.|
|---|---|---|---|---|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5<br>P|-1|-1<br>-0.5<br>0<br>0.5<br><br>T<br><br>-1<br>-0.5<br>0<br>0.5<br>P<br><br>-1<br>-0.5<br>0<br>0.5<br><br>ck|
|PCEP:DRUG...||48<br>PCEP:MAGAZINES...|48|48<br>PCEP:FARM.RENT<br>48<br>USER-OPER.TRANSPOR<br>48<br>PCEP:DENTISTS<br>onetary policy sho|
|0.5|-0.5<br>0|0<br>-1<br><br>-0.5<br>0<br>0.5<br>|0<br>-1|0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:<br>0<br>-1<br>-0.5<br>0<br>0.5<br>ifed m|
|0.5<br>PCEP:CLEANING...|-0.5<br>0|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:REMIT.IN.KIND.NONRES.|0<br>48<br>-1|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:TENANT-OCC.RENT<br>0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:TRANSPORT<br>0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:PHYSICIANS<br>ulse responses to an ident|
|0.5<br>PCEP:SEMIDUR.HOUSE|-0.5<br>0|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:EXP.ABROAD.BY.U.S.|0<br>48<br>-1|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:OWNER-OCC.RENT<br>0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:OTHER.H.OPERATION<br><br>0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:MEDICAL.CARE<br>Figure 3b: Estimated imp|
|PCEP:TOILET...||48<br>PCEP:STATIONERY...|48|48<br>PCEP:HOUSING<br><br>48<br>PCEP:HOUSE.OPER.<br><br>48<br>P:INTERCITY.TRANSPORT|
|0.5|-0.5<br>0|0<br>-1<br>-0.5<br>0<br>0.5|0<br>-1|0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>PCE|



|EP:OTHER.RECREATION||0<br>48|EP:RELIGIOUS&WELFARE|0<br>48|0<br>48<br>PPI  3<br>0<br>48<br>PPI  8<br>0<br>48<br>PPI 13|
|---|---|---|---|---|---|
|0.5<br>PC|-0.5<br>0|-1|H<br>-0.5<br>0<br>0.5<br>PC|-1|-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>ock|
|PCEP:CONCERTS...||48|:EDUCATION&RESEARC|48|48<br>PPI  2<br><br>48<br>PPI  7<br><br>48<br>PPI 12<br>monetary policy sh|
|0.5|-0.5<br>0|0<br>-1|-0.5<br>0<br>0.5<br>PCEP|0<br>-1|0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>tifed|
|CEP:RECREATION||48|PERSONAL.BUSINESS|48|48<br>PPI  1<br>48<br>PPI  6<br>48<br>PPI 11<br>ponses to an iden|
|P||0|EP:|0|0<br>0<br>0<br>res|
|0.5|-0.5<br>0|-1|-0.5<br>0<br>0.5<br>PC|-1|-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>pulse|
|0.5<br>PCEP:HEALTH.INSURANCE|-0.5<br>0|0<br>48<br>-1|-0.5<br>0<br>0.5<br>PCEP:PERSONAL.CARE|0<br>48<br>-1|0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PCEP:US.EXP.NONRES.<br>0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PPI  5<br>0<br>48<br>-1<br>-0.5<br>0<br>0.5<br>PPI 10<br>Figure 3c: Estimated im|
|PCEP:HOSPITALS...||48|CEP:OTHER.SERVICES|48|48<br>PCEP:TRAVEL<br><br>48<br>PPI  4<br><br>48<br>PPI  9|
|0.5|-0.5<br>0|0<br>-1|-0.5<br>0<br>0.5<br>P|0<br>-1|0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5|



|||48|48<br>48<br>48<br>48|
|---|---|---|---|
|PPI 18||PPI 23|PPI 28<br>PPI 33<br>PPI 38|
|||0<br>|0<br>0<br><br>0<br><br>0<br>|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>k|
|||48|48<br>48<br>48<br>48<br>y shoc|
|PPI 17||PPI 22|PPI 27<br>PPI 32<br>PPI 37<br>etary polic|
|||0|0<br>0<br>0<br>0<br>on|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>ifed m|
|||48|48<br>48<br>48<br>48<br> ident|
|PPI 16||PPI 21|PPI 26<br>PPI 31<br>PPI 36<br>nses to an|
|||0<br><br>|0<br>0<br><br><br>0<br><br><br>0<br><br><br>espo|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>ulse r|
|||48|48<br>48<br>48<br>48<br>ed imp|
|PPI 15||PPI 20|PPI 25<br>PPI 30<br>PPI 35<br> Estimat|
|||0|0<br>0<br>0<br>0<br> 3d:|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>Figure|
|||48|48<br>48<br>48<br>48|
|PPI 14||PPI 19|PPI 24<br>PPI 29<br>PPI 34|
|||0<br><br>|0<br>0<br><br><br>0<br><br><br>0<br><br>|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5|



|||48<br>48<br>48<br>48<br>48|
|---|---|---|
|PPI 43||PPI 48<br>PPI 53<br>PPI 58<br>PPI 63|
|||0<br>0<br><br>0<br><br>0<br><br>0<br>|
|0.5|-0.5<br>0|-1<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>k|
|||48<br>48<br>48<br>48<br>48<br>y shoc|
|PPI 42||PPI 47<br>PPI 52<br>PPI 57<br>PPI 62<br>netary polic|
|||0<br>0<br>0<br>0<br>0<br>o|
|0.5|-0.5<br>0|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>ifed m|
|||48<br>48<br>48<br>48<br>48<br> ident|
|PPI 41||PPI 46<br>PPI 51<br>PPI 56<br>PPI 61<br>onses to an|
|||0<br>0<br>0<br>0<br>0<br>sp|
|0.5|-0.5<br>0|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>ulse re|
|||48<br>48<br>48<br>48<br>48<br>ed imp|
|PPI 40||PPI 45<br>PPI 50<br>PPI 55<br>PPI 60<br> Estimat|
|||0<br>0<br>0<br>0<br>0<br> 3e:|
|0.5|-0.5<br>0|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>Figure|
|||48<br>48<br>48<br>48<br>48|
|PPI 39||PPI 44<br>PPI 49<br>PPI 54<br>PPI 59|
|||0<br>0<br><br><br>0<br><br><br>0<br><br><br>0<br><br>|
|0.5|-0.5<br>0|-1<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5|



|||48<br>48<br>48<br>48<br>48|
|---|---|---|
|PPI 68||PPI 73<br>PPI 78<br>PPI 83<br>PPI 88|
|||0<br>0<br><br>0<br><br>0<br><br>0<br>|
|0.5|-0.5<br>0|-1<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>k|
|||48<br>48<br>48<br>48<br>48<br>y shoc|
|PPI 67||PPI 72<br>PPI 77<br>PPI 82<br>PPI 87<br>netary polic|
|||0<br>0<br>0<br>0<br>0<br>o|
|0.5|-0.5<br>0|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>fed m|
|||48<br>48<br>48<br>48<br>48<br> identi|
|PPI 66||PPI 71<br>PPI 76<br>PPI 81<br>PPI 86<br>ponses to an|
|||0<br>0<br>0<br>0<br>0<br>s|
|0.5|-0.5<br>0|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>ulse re|
|||48<br>48<br>48<br>48<br>48<br>d imp|
|PPI 65||PPI 70<br>PPI 75<br>PPI 80<br>PPI 85<br> Estimate|
|||0<br>0<br>0<br>0<br>0<br> 3f:|
|0.5|-0.5<br>0|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>Figure|
|||48<br>48<br>48<br>48<br>48|
|PPI 64||PPI 69<br>PPI 74<br>PPI 79<br>PPI 84|
|||0<br>0<br><br><br>0<br><br><br>0<br><br><br>0<br><br>|
|0.5|-0.5<br>0|-1<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5|



|||48|48<br>48<br>48<br>48|
|---|---|---|---|
|PPI 93||PPI 98|PPI103<br><br>PPI108<br><br>PPI113|
|0.5|-0.5<br>0|0<br>-1<br>-0.5<br>0<br>0.5|0<br>-1<br>0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>k|
|||48|48<br>48<br>48<br>48<br>y shoc|
|PPI 92||PPI 97|PPI102<br>PPI107<br>PPI112<br>etary polic|
|||0|0<br>0<br>0<br>0<br>on|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>ifed m|
|||48|48<br>48<br>48<br>48<br> ident|
|PPI 91||PPI 96|PPI101<br>PPI106<br>PPI111<br>onses to an|
|0.5|-0.5<br>0|0<br>-1<br>-0.5<br>0<br>0.5|0<br>-1<br>0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>ulse resp|
|||48|48<br>48<br>48<br>48<br>ed imp|
|PPI 90||PPI 95|PPI100<br>PPI105<br>PPI110<br> Estimat|
|||0|0<br>0<br>0<br>0<br> 3g:|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>Figure|
|||48|48<br>48<br>48<br>48|
|PPI 89||PPI 94|PPI 99<br>PPI104<br>PPI109|
|||0<br><br>|0<br>0<br><br><br>0<br><br><br>0<br><br>|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5|



|||48|48<br>48<br>48<br>48|
|---|---|---|---|
|PPI118||PPI123|PPI128<br><br>PPI133<br><br>PPI138|
|0.5|-0.5<br>0|0<br>-1<br>-0.5<br>0<br>0.5|0<br>-1<br>0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>k|
|||48|48<br>48<br>48<br>48<br>y shoc|
|PPI117||PPI122|PPI127<br>PPI132<br>PPI137<br>netary polic|
|||0|0<br>0<br>0<br>0<br>o|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>ifed m|
|||48|48<br>48<br>48<br>48<br> ident|
|PPI116||PPI121|PPI126<br>PPI131<br>PPI136<br>onses to an|
|||0|0<br>0<br>0<br>0<br>sp|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>ulse re|
|PPI115||48<br>PPI120|48<br>48<br>PPI125<br>48<br>PPI130<br>48<br>PPI135<br> Estimated imp|
|||0|0<br>0<br>0<br>0<br> 3h:|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>Figure|
|||48|48<br>48<br>48<br>48<br>|
|PPI114||PPI119|PPI124<br>PPI129<br>PPI134|
|||0<br><br>|0<br>0<br><br><br>0<br><br><br>0<br><br>|
|0.5|-0.5<br>0|-1<br>-0.5<br>0<br>0.5|-1<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5|



||48<br>48<br>48|
|---|---|
|PPI143|PPI148<br>PPI153|
||0<br><br>0<br><br><br>0<br><br>|
|0.5|-1<br>-0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>k|
||48<br>48<br>48<br> shoc|
|PPI142|PPI147<br>PPI152<br>etary policy|
||0<br><br>0<br><br><br>0<br><br><br>mon|
|0.5|-1<br>-0.5<br>0<br>-1<br>-0.5<br>0<br>0.5<br>-1<br>-0.5<br>0<br>0.5<br>fed|
||48<br>48<br>48<br>identi|
|PPI141|PPI146<br>PPI151<br>ponses to an|
||0<br>0<br>0<br>s|
|0.5|-1<br>-0.5<br>0<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>ulse re|
||48<br>48<br>48<br> imp|
|PPI140|PPI145<br>PPI150<br> Estimated|
||0<br>0<br>0<br> 3i:|
|0.5|-1<br>-0.5<br>0<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br>Figure|
||48<br>48<br>48<br>48|
|PPI139|PPI144<br>PPI149<br>PPI154|
||0<br>0<br>0<br>0|
|0.5|-1<br>-0.5<br>0<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5<br><br>-1<br>-0.5<br>0<br>0.5|





<!-- Start of picture text -->
PCE prices: Monetary shock Common component Sector-specific<br>0.5 0 0<br>0<br>-5 -5<br>-0.5<br>-1<br>-10 -10<br>-1.5<br>-2 -15 -15<br>0 12 24 36 48 0 12 24 36 48 0 12 24 36 48<br>PPI prices: Monetary shock Common component Sector-specific<br>0.5 0 0<br>-2<br>0 -5<br>-4<br>-6<br>-0.5 -10<br>-8<br>-1 -15 -10<br>0 12 24 36 48 0 12 24 36 48 0 12 24 36 48<br><!-- End of picture text -->

Figure 4a. Estimated impulse responses of (log) sectorial prices to an identified monetary policy shock (left panels), to a shock to the common component (middle panels), and to a sector-specific shock (right panels). Fat lines represent unweighted average responses. Fat dashed lines represent the response of the aggregate PCE and PPI (finished) price indices to a monetary policy shock. 



<!-- Start of picture text -->
PCE Quantities: Monetary shock Common component Sector-specific<br>1.5 0 0<br>-5<br>1 -5<br>-10<br>-15<br>0.5 -10<br>-20<br>-25<br>0 -15<br>-30<br>-35<br>-0.5 -20<br>-40<br>-1 -25 -45<br>0 12 24 36 48 0 12 24 36 48 0 12 24 36 48<br><!-- End of picture text -->

Figure 4b. Estimated impulse responses of (log) sectorial PCE quantities to an identified monetary policy shock (left panel), to a shock to the common component (middle panel), and to a sector-specific shock (right panel). Fat lines represent unweighted average responses. The fat dashed line represents the response of the aggregate PCE quantity to a monetary policy shock. 



<!-- Start of picture text -->
0.80<br>0.60<br>0.40<br>0.20<br>0.00<br>1.5 1 0.5 0 -0.5 -1 -1.5 -2 -2.5<br>-0.20<br>-0.40<br>Responses of PCE prices cumulated for first 6 months<br>-0.60<br>Figure 5: Impulse responses of PCE prices and quantities to monetary shock<br>-0.80<br>IRFCUQ6 = -0.257 - 0.593 * IRFCUP6                    (0.033)  (0.167) R2 = 0.06<br>-1.00<br><!-- End of picture text -->



<!-- Start of picture text -->
12<br>PPI PCE<br>10<br>8<br>IRFCU6 = 0.082 - 0.16 * St.dev.(ei)                (0.023)  (0.014) R2 = 0.26<br>6<br>4<br>Standard deviation of idio components (e_it)<br>2<br>Figure 6: Impulse responses to monetary shock and volatility of sector-specific components<br>0<br>1 0.5 0 -0.5 -1 -1.5 -2 -2.5<br>Impulse responses cumulated for first 6 months<br><!-- End of picture text -->

###### **APPENDIX A – Main Data Set** 

Format is as in Stock and Watson (2002) paper: series number; series mnemonic; data span; transformation code and series description as appears in the database. The transformation codes are: 1 – no transformation; 2 – first difference; 4 – logarithm; 5 – first difference of logarithm. Second differencing of logarithms was not used. Our main data set contains 230 monthly series with no missing observations. Series were directly taken from DRI/McGraw Hill Basic Economics Database. 

|1|OUT ----------- re<br>IPS11|al output and incom<br>1976:1 - 2005:6|e<br>5<br>INDUSTRIAL PRODUCTION INDEX - PRODUCTS TOTAL|
|---|---|---|---|
|<br>2|<br>IPS299|<br>1976:1 - 2005:6|<br>,<br>5<br>INDUSTRIAL PRODUCTION INDEX - FINAL PRODUCTS|
|3|IPS12|1976:1 - 2005:6|5<br>INDUSTRIAL PRODUCTION INDEX - CONSUMER GOODS|
|4|IPS13|1976:1 - 2005:6|5<br>INDUSTRIAL PRODUCTION INDEX - DURABLE CONSUMER GOODS|
|5|IPS18|1976:1 - 2005:6|5<br>INDUSTRIAL PRODUCTION INDEX - NONDURABLE CONSUMER GOODS|
|6<br>|IPS25<br>|1976:1 - 2005:6<br>|5<br>INDUSTRIAL PRODUCTION INDEX - BUSINESS EQUIPMENT<br> <br>|
|7|IPS32|1976:1 - 2005:6|5<br>INDUSTRIAL PRODUCTION INDEX - MATERIALS|
|8|IPS34|1976:1 - 2005:6|5<br>INDUSTRIAL PRODUCTION INDEX - DURABLE GOODS MATERIALS|
|<br>9|<br>IPS38|<br>1976:1 - 2005:6|<br> <br>5<br>INDUSTRIAL PRODUCTION INDEX - NONDURABLE GOODS MATERIALS|
|10|IPS43<br>|1976:1 - 2005:6<br>|5<br>INDUSTRIAL PRODUCTION INDEX - MANUFACTURING (SIC)<br>|
|11|IPS67e|1976:1 - 2005:6|5<br>INDUSTRIAL PRODUCTION INDEX - MINING NAICS=21|
|12|IPS68e|1976:1 - 2005:6|5<br>INDUSTRIAL PRODUCTION INDEX - ELECTRIC AND GAS UTILITIES|
|<br>13|<br>IPS10|<br>1976:1 - 2005:6|<br> <br>5<br>INDUSTRIAL PRODUCTION INDEX - TOTAL INDEX|
|14<br>15|PMI<br>PMP|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>PURCHASING MANAGERS' INDEX (SA)<br>5<br>NAPM PRODUCTION INDEX (PERCENT)|
|16|PYQ|1976:1 - 2005:6|<br>5<br>PERSONAL INCOME (CHAINED) (BIL2000$,SAAR)|
|17|MYXPQ|1976:1 - 2005:6|5<br>PERSONAL INCOME LESS TRANSFER PAYMENTS (CHAINED)  (BIL 2000$,SAAR)|
|18|<br>IPS307|1976:1 - 2005:6|<br>5<br>INDUSTRIAL PRODUCTION INDEX - RESIDENTIAL UTILITIES|
|19|IPS316|1976:1 - 2005:6|5<br>INDUSTRIAL PRODUCTION INDEX - BASIC METALS|
||EMP -------------|employment and ho|urs|
|20|<br>LHEL|<br>1976:1 - 2005:6|<br>5<br>INDEX OF HELP-WANTED ADVERTISING IN NEWSPAPERS (1967=100;SA)|
|21<br>|LHELX<br>|1976:1 - 2005:6<br>|<br>4<br>EMPLOYMENT: RATIO; HELP-WANTED ADS:NO. UNEMPLOYED CLF<br> <br>|
|22|LHEM|1976:1 - 2005:6|5<br>CIVILIAN LABOR FORCE: EMPLOYED, TOTAL (THOUS.,SA)|
|23|LHNAG|1976:1 - 2005:6|5<br>CIVILIAN LABOR FORCE: EMPLOYED NONAGRICINDUSTRIES (THOUSSA)|
|<br>24|<br>LHUR|<br>1976:1 - 2005:6|<br>, . .,<br>1<br>UNEMPLOYMENT RATE: ALL WORKERS, 16 YEARS & OVER (%,SA)|
|25|LHU680|1976:1 - 2005:6|1<br>UNEMPLOY.BY DURATION: AVERAGE(MEAN)DURATION IN WEEKS (SA)<br>|
|26|LHU5|1976:1 - 2005:6|1<br>UNEMPLOY.BY DURATION: PERSONS UNEMPL.LESS THAN 5 WKS (THOUS.,SA)|
|27|LHU14|1976:1 - 2005:6|1<br>UNEMPLOY.BY DURATION: PERSONS UNEMPL.5 TO 14 WKS (THOUS.,SA)|
|28|LHU15|1976:1 - 2005:6|1<br>UNEMPLOY.BY DURATION: PERSONS UNEMPL.15 WKS + (THOUS.,SA)|
|29|LHU26|1976:1 - 2005:6|<br>1<br>UNEMPLOY.BY DURATION: PERSONS UNEMPL.15 TO 26 WKS (THOUS.,SA)<br>|
|30|BLS_LPNAG|1976:1 - 2005:6|5<br>Total Nonfarm Employment - Seasonally Adjusted - CES0000000001|
|31|<br>BLS_LP|1976:1 - 2005:6|<br>5<br>Total Private Employment - Seasonally Adjusted - CES0500000001|
|32|BLSLPGD|1976:1 - 2005:6|5<br>Goods-producing Employment - Seasonally Adjusted - CES0600000001|
|33|_<br>BLS_LPMI|1976:1 - 2005:6|<br>5<br>Natural Resources and Mining Employment - Seasonally Adjusted - CES1000000001|
|34|BLSLPCC|1976:1 - 2005:6|5<br>Construction Employment - Seasonally Adjusted - CES2000000001|
|<br>35|_<br>BLS_LPEM|<br>1976:1 - 2005:6|<br> <br>5<br>Manufacturing Employment - Seasonally Adjusted - CES3000000001|
|36|BLSLPED|1976:1 - 2005:6|5<br>Durable Goods Manufacturing Employment - Seasonally Adjusted - CES3100000001|
|37|_<br>BLS_LPEN|1976:1 - 2005:6|<br>5<br>Nondurable Goods Manufacturing Employment - Seasonally Adjusted - CES3200000001|
|38<br>|BLS_Ser.-EMP<br>|1976:1 - 2005:6<br>|5<br>Service-providing Employment - Seasonally Adjusted - CES0700000001<br> <br>|
|39|BLS_Tra.EMP|1976:1 - 2005:6|5<br>Trade, Transportation, and Utilities Employment - Seasonally Adjusted - CES4000000001|
|40<br>|BLS_Ret.- EMP<br>|1976:1 - 2005:6<br>|5<br>Retail Trade Employment - Seasonally Adjusted - CES4200000001<br> <br>|
|41|BLS_Whol. EMP|1976:1 - 2005:6|5<br>Wholesale Trade Employment - Seasonally Adjusted - CES4142000001|
|42|BLSFin-EMP|1976:1 - 2005:6|5<br>Financial Activities Emloment - Seasonall Adjusted - CES5500000001|
|<br>43|_.<br>BLS_P-ser.EMP|<br>1976:1 - 2005:6|<br>py  y<br>5<br>Private Service-providing Employment - Seasonally Adjusted - CES0800000001|
|44<br>|BLS_LPGOV<br>|1976:1 - 2005:6<br>|<br>5<br>Government Employment - Seasonally Adjusted - CES9000000001<br> <br>|
|45|BLSLPHRM|1976:1 - 2005:6|1<br>Manufacturing Average Weekly Hours of Production Workers - Seasonally Adjusted - CES30|
|46|_<br>BLSLPMOSA|19761 - 20056|<br>1<br>Mfti A Wkl Oti f Pdti Wk - Sll Adtd -CE|
|<br>47|_<br>PMEMP|:  :<br>1976:1 - 2005:6|<br>anuacurng verage eey verme o roucon orers  easonay juse <br>NAPM EMPLOYMENT INDEX (PERCENT)|
||HSS -------------|- housing starts and|<br>sales|
|48|<br>HSFR|<br>1976:1 - 2005:6|<br>4<br>HOUSING STARTS:NONFARM(1947-58);TOTAL FARM&NONFARM(1959-)(THOUS.,SA|
|49<br>|HSNE<br>|1976:1 - 2005:6<br>|4<br>HOUSING STARTS:NORTHEAST (THOUS.U.)S.A.<br> <br>|
|50<br>51|HSMW<br>HSSOU|1976:1 - 2005:6<br>1976:1 - 2005:6|4<br>HOUSING STARTS:MIDWEST(THOUS.U.)S.A.<br>4<br>HOUSING STARTS:SOUTH (THOUS.U.)S.A.|
|<br>52|<br>HSWST|<br>1976:1 - 2005:6|<br> <br>4<br>HOUSING STARTS:WEST (THOUS.U.)S.A.|
|53|HSBR|1976:1 - 2005:6|4<br>HOUSING AUTHORIZED: TOTAL NEW PRIV HOUSING UNITS (THOUSSAAR)|
|<br>54|<br>HMOB|<br>1976:1 - 2005:6|<br>.,<br>4<br>MOBILE HOMES: MANUFACTURERS' SHIPMENTS (THOUS.OF UNITS,SAAR)|
||INV --------------|-- real inventories an|d inventory-sales ratios|
|55|PMNV|1976:1 - 2005:6|1<br>NAPM INVENTORIES INDEX (PERCENT)|
||ORD--------------|- orders and unfilled|orders|
|56|<br>PMNO|<br>1976:1 - 2005:6|<br>1<br>NAPM NEW ORDERS INDEX (PERCENT)|



|57<br>58|PMDEL<br>MOCMQ|1976:1 - 2005:6<br>1976:1 - 2005:6|1<br>NAPM VENDOR DELIVERIES INDEX (PERCENT)<br>5<br>NEW ORDERS (NET) - CONSUMER GOODS & MATERIALS 1996 DOLLARS (BCI)|
|---|---|---|---|
|<br>59|<br>MSONDQ|<br>1976:1 - 2005:6|<br>,<br>5<br>NEW ORDERS, NONDEFENSE CAPITAL GOODS, IN 1996 DOLLARS (BCI)|
||SPR -----------|---- stock prices||
|60|FSPCOM|1976:1 - 2005:6|5<br>S&P'S COMMON STOCK PRICE INDEX: COMPOSITE (1941-43=10)|
|61|FSPIN|1976:1 - 2005:6|<br>5<br>S&P'S COMMON STOCK PRICE INDEX: INDUSTRIALS (1941-43=10)|
|62<br>63|FSDXP<br>FSPXE|1976:1 - 2005:6<br>19761  20056|1<br>S&P'S COMPOSITE COMMON STOCK: DIVIDEND YIELD (% PER ANNUM)<br>1<br>S&P'S COMPOSITE COMMON STOCK PRICEEARNINGS RATIO %NSA|
|<br>64|<br>FSDJ|: - :<br>1976:1 - 2005:6|<br>: -  (,)<br>COMMON STOCK PRICES: DOW JONES INDUSTRIAL AVERAGE|
||EXR -----------|----- exchange rates||
|65<br>|EXRSW<br>|1976:1 - 2005:6<br>|5<br>FOREIGN EXCHANGE RATE: SWITZERLAND (SWISS FRANC PER U.S.$)<br> <br>|
|66|EXRJAN|1976:1 - 2005:6|5<br>FOREIGN EXCHANGE RATE: JAPAN (YEN PER U.S.$)|
|67|EXRUK|1976:1 - 2005:6|5<br>FOREIGN EXCHANGE RATE: UNITED KINGDOM (CENTS PER POUND)|
|<br>68|<br>EXRCAN|<br>1976:1 - 2005:6|<br> <br>5<br>FOREIGN EXCHANGE RATE: CANADA (CANADIAN $ PER U.S.$)|
||INT -----------|----- interest rates||
|69|FYFF|1976:1 - 2005:6|1<br>INTEREST RATE: FEDERAL FUNDS (EFFECTIVE) (% PER ANNUM,NSA)|
|70<br>|FYGM3<br>|1976:1 - 2005:6<br>|<br>1<br>INTEREST RATE: U.S.TREASURY BILLS,SEC MKT,3-MO.(% PER ANN,NSA)<br> <br>|
|71|FYGM6|1976:1 - 2005:6|1<br>INTEREST RATE: U.S.TREASURY BILLS,SEC MKT,6-MO.(% PER ANN,NSA)|
|72<br>|FYGT1<br>|1976:1 - 2005:6<br>|1<br>INTEREST RATE: U.S.TREASURY CONST MATURITIES,1-YR.(% PER ANN,NSA)<br> <br>|
|73|FYGT5|1976:1 - 2005:6|1<br>INTEREST RATE: U.S.TREASURY CONST MATURITIES,5-YR.(% PER ANN,NSA)|
|74|FYGT10|1976:1 - 2005:6|1<br>INTEREST RATE: U.S.TREASURY CONST MATURITIES10-YR.(% PER ANNNSA)|
|75|<br>FYAAAC|<br>1976:1 - 2005:6|,  ,<br>1<br>BOND YIELD: MOODY'S AAA CORPORATE (% PER ANNUM)|
|76|FYBAAC|1976:1 - 2005:6|1<br>BOND YIELD: MOODY'S BAA CORPORATE (% PER ANNUM)|
|77|SFYGM3|19761 - 20056|<br>1<br>Sd FYGM3 - FYFF|
|<br>78|<br>SFYGM6|:  :<br>1976:1 - 2005:6|<br>prea<br>1<br>Spread FYGM6 - FYFF|
|79<br>|SFYGT1<br>|1976:1 - 2005:6<br>|1<br>Spread FYGT1 - FYFF<br> <br>|
|80|SFYGT5|1976:1 - 2005:6|1<br>Spread FYGT5 - FYFF|
|81<br>|SFYGT10<br>|1976:1 - 2005:6<br>|1<br>Spread FYGT10 - FYFF<br> <br>|
|82<br>83|SFYAAAC<br>SFYBAAC|1976:1 - 2005:6<br>1976:1 - 2005:6|1<br>Spread FYAAAC - FYFF<br>1<br>Spread FYBAAC - FYFF|
||MON ----------|------ money and credi|t quantity aggregates|
|84<br>|<br>FM1<br>|<br>1976:1 - 2005:6<br>|<br>5<br>MONEY STOCK: M1(CURR,TRAV.CKS,DEM DEP,OTHER CK'ABLE DEP)(BIL$,SA)<br> <br>|
|85|FM2|1976:1 - 2005:6|5<br>MONEY STOCK:M2(M1+O'NITE RPS,EURO$,G/P&B/D MMMFS&SAV&SM TIME DEP(BIL$,|
|86|FM3|1976:1 - 2005:6|5<br>MONEY STOCK: M3(M2+LG TIME DEPTERM RP'S&INST ONLY MMMFS)(BIL$SA)|
|<br>87|<br>FM2DQ|<br>1976:1 - 2005:6|<br>,   ,<br>5<br>MONEY SUPPLY - M2 IN 1996 DOLLARS (BCI)|
|88|FMFBA|1976:1 - 2005:6|5<br>MONETARY BASE ADJ FOR RESERVE REQUIREMENT CHANGES(MIL$SA)|
|<br>89|<br>FMRRA|<br>1976:1 - 2005:6|<br>,     ,<br>5<br>DEPOSITORY INST RESERVES:TOTAL,ADJ FOR RESERVE REQ CHGS(MIL$,SA)|
|90|FMRNBA|1976:1 - 2005:6|5<br>DEPOSITORY INST RESERVES:NONBORROWED,ADJ RES REQ CHGS(MIL$,SA)|
|91|FCLBMC|19761 - 20056|<br>1<br>WKLY RP LG COM'L BANKSNET CHANGE COM'L & INDUS LOANSBIL$SAAR|
|<br>92|<br>CCINRV|:  :<br>1976:1 - 2005:6|<br>:     (,)<br>5<br>CONSUMER CREDIT OUTSTANDING - NONREVOLVING(G19)|
|93|IMFCLNQ|1976:1 - 2005:6|<br>COMMERCIAL & INDUSTRIAL LOANS OUSTANDING IN 1996 DOLLARS|
||PRI ------------|--- price indexes||
|94|<br>PMCP|<br>1976:1 - 2005:6|1<br>NAPM COMMODITY PRICES INDEX (PERCENT)|
|95|PWFSA|1976:1 - 2005:6|5<br>PRODUCER PRICE INDEX: FINISHED GOODS (82=100,SA)|
|96<br>97|PWFCSA<br>PWIMSA|1976:1 - 2005:6<br>1976:1 - 2005:6|<br>5<br>PRODUCER PRICE INDEX:FINISHED CONSUMER GOODS (82=100,SA)<br>5<br>PRODUCER PRICE INDEX:INTERMED MAT.SUPPLIES & COMPONENTS(82=100,SA)|
|98<br>|PWCMSA<br>|1976:1 - 2005:6<br>|<br>5<br>PRODUCER PRICE INDEX:CRUDE MATERIALS (82=100,SA)<br> <br>|
|99<br>100|PUNEW<br>PU83|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>CPI-U: ALL ITEMS (82-84=100,SA)<br>5<br>CPI-U: APPAREL & UPKEEP (82-84=100SA)|
|<br>101|<br>PU84|<br>1976:1 - 2005:6|<br>,<br>5<br>CPI-U: TRANSPORTATION (82-84=100,SA)|
|102|PU85|1976:1 - 2005:6|5<br>CPI-U: MEDICAL CARE (82-84=100SA)|
|<br>103|<br>PUC|<br>1976:1 - 2005:6|<br>,<br>5<br>CPI-U: COMMODITIES (82-84=100,SA)|
|104|PUCD|1976:1 - 2005:6|5<br>CPI-U: DURABLES (82-84=100SA)|
|<br>105|<br>PUXF|<br>1976:1 - 2005:6|<br>,<br>5<br>CPI-U: ALL ITEMS LESS FOOD (82-84=100,SA)|
|106|PUXHS|1976:1 - 2005:6|5<br>CPI-U: ALL ITEMS LESS SHELTER (82-84=100,SA)|
|107<br>|PUXM<br>|1976:1 - 2005:6<br>|<br>5<br>CPI-U: ALL ITEMS LESS MIDICAL CARE (82-84=100,SA)<br> <br>|
|108|PSCCOM|1976:1 - 2005:6|5<br>SPOT MARKET PRICE INDEX:BLS & CRB: ALL COMMODITIES(1967=100)|
||AHE -----------|-- average hourly earn|ings|
|109|BLSLEHCC|1976:1 - 2005:6|5<br>Construction Average Hourly Earnings of Production Workers - Seasonally Adjusted -CE|
|<br>110|_<br>BLS_LEHM|<br>1976:1 - 2005:6|<br>  <br>5<br>Manufacturing Average Hourly Earnings of Production Workers - Seasonally Adjusted - C|
||OTH|ill||
|111|-----------<br>HHSNTN|-- msceaneous<br>1976:1 - 2005:6|1<br>U. OF MICH. INDEX OF CONSUMER EXPECTATIONS(BCD-83)|



###### **APPENDIX B - Personal Consumption Expenditures (price indexes and nominal expenditure)** 

Format is as above: series number; series; data span; transformation code and series description as appears in the database. The transformation for all data was first difference of logarithms, which is coded as 5. This data set contains 194 monthly price series on Personal Consumption Expenditures with no missing observations, and 194 monthly real consumption series on Personal Consumption Expenditures. We describe here the 194 price series. The 194 corresponding real consumption series were ordered and transformed in a similar fashion. Series were downloaded from the underlying tables of the Bureau of Economic Analysis. 

|1|P1NDCG3|1976:1 - 2005:6|5|New domestic autos|
|---|---|---|---|---|
|2|P1NFCG3|1976:1 - 2005:6|5|New foreign autos|
|3|P1NETG3|1976:1 - 2005:6|5|Net transactions in used autos|
|4|P1MARG3|1976:1 - 2005:6|5|Used auto margin|
|5|P1REEG3|1976:1 - 2005:6|5|Employee reimbursement|
|6|P1TRUG3|1976:1 - 2005:6|5|Trucks, new and net used|
|7|P1REVG3|1976:1 - 2005:6|5|Recreational vehicles|
|8|P1TATG3|1976:1 - 2005:6|5|Tires and tubes|
|9|P1PAAG3|1976:1 - 2005:6|5|Accessories and parts|
|10|P1FNRG3|1976:1 - 2005:6|5|Furniture, including mattresses and bedsprings (29)|
|11|P1MHAG3|1976:1 - 2005:6|5|Major household appliances|
|12|P1SEAG3|1976:1 - 2005:6|5|Small electric appliances|
|13|P1CHNG3|1976:1 - 2005:6|5|China, glassware, tableware, and utensils (31)|
|14|P1RADG3|1976:1 - 2005:6|5|Video and audio goods, including musical instruments, and computer goods (91)|
|15|P1FLRG3|1976:1 - 2005:6|5|Floor coverings|
|16|P1CLFG3|1976:1 - 2005:6|5|Clocks, lamps, and furnishings|
|17|P1TEXG3|1976:1 - 2005:6|5|Blinds, rods, and other|
|18|P1WTRG3|1976:1 - 2005:6|5|Writing equipment|
|19|P1HDWG3|1976:1 - 2005:6|5|Tools, hardware, and supplies|
|20|P1LWNG3|1976:1 - 2005:6|5|Outdoor eqpt and supplies|
|21|P1OPTG3|1976:1 - 2005:6|5|Ophthalmic products and orthopedic appliances (46)|
|22|P1GUNG3|1976:1 - 2005:6|5|Guns|
|23|P1SPTG3|1976:1 - 2005:6|5|Sporting equipment|
|24|P1CAMG3|1976:1 - 2005:6|5|Photographic equipment|
|25|P1BCYG3|1976:1 - 2005:6|5|Bicycles|
|26|P1MCYG3|1976:1 - 2005:6|5|Motorcycles|
|27|P1BOAG3|1976:1 - 2005:6|5|Pleasure boats|
|28|P1AIRG3|1976:1 - 2005:6|5|Pleasure aircraft|
|29|P1JRYG3|1976:1 - 2005:6|5|Jewelry and watches (18)|
|30|P1BKSG3|1976:1 - 2005:6|5|Books and maps (87)|
|31|P1GRAG3|1976:1 - 2005:6|5|Cereals|
|32|P1BAKG3|1976:1 - 2005:6|5|Bakery products|
|33|P1BEEG3|1976:1 - 2005:6|5|Beef and veal|
|34|P1PORG3|1976:1 - 2005:6|5|Pork|
|35|P1MEAG3|1976:1 - 2005:6|5|Other meats|
|36|P1POUG3|1976:1 - 2005:6|5|Poultry|
|37|P1FISG3|1976:1 - 2005:6|5|Fish and seafood|
|38|P1GGSG3|1976:1 - 2005:6|5|Eggs|
|39|P1MILG3|1976:1 - 2005:6|5|Fresh milk and cream|
|40|P1DAIG3|1976:1 - 2005:6|5|Processed dairy products|



|41|P1FRUG3<br>1976:1|- 2005:6|5|Fresh fruits|
|---|---|---|---|---|
|42|P1VEGG3<br>1976:1|- 2005:6|5|Fresh vegetables|
|43|P1PFVG3<br>1976:1|- 2005:6|5|Processed fruits and vegetables|
|44|P1JNBG3<br>1976:1|- 2005:6|5|Juices and nonalcoholic drinks|
|45|P1CTMG3<br>1976:1|- 2005:6|5|Coffee, tea and beverage materials|
|46|P1FATG3<br>1976:1|- 2005:6|5|Fats and oils|
|47|P1SWEG3<br>1976:1|- 2005:6|5|Sugar and sweets|
|48|P1OFDG3<br>1976:1|- 2005:6|5|Other foods|
|49|P1PEFG3<br>1976:1|- 2005:6|5|Pet food|
|50|P1MLTG3<br>1976:1|- 2005:6|5|Beer and ale, at home|
|51|P1WING3<br>1976:1|- 2005:6|5|Wine and brandy, at home|
|52|P1LIQG3<br>1976:1|- 2005:6|5|Distilled spirits, at home|
|53|P1ESLG3<br>1976:1|- 2005:6|5|Elementary and secondary school lunch|
|54|P1HSLG3<br>1976:1|- 2005:6|5|Higher education school lunch|
|55|P1OPMG3<br>1976:1|- 2005:6|5|Other purchased meals|
|56|P1APMG3<br>1976:1|- 2005:6|5|Alcohol in purchased meals|
|57|P1CFDG3<br>1976:1|- 2005:6|5|Food supplied civilians|
|58|P1MFDG3<br>1976:1|- 2005:6|5|Food supplied military|
|59|P1FFDG3<br>1976:1|- 2005:6|5|Food produced and consumed on farms|
|60|P1SHUG3<br>1976:1|- 2005:6|5|Shoes (12)|
|61|P1WGCG3<br>1976:1|- 2005:6|5|Clothing for females|
|62|P1WICG3<br>1976:1|- 2005:6|5|Clothing for infants|
|63|P1WSGG3<br>1976:1|- 2005:6|5|Sewing goods for females|
|64|P1WUGG3<br>1976:1|- 2005:6|5|Luggage for females|
|65|P1MBCG3<br>1976:1|- 2005:6|5|Clothing for males|
|66|P1MSGG3<br>1976:1|- 2005:6|5|Sewing goods for males|
|67|P1MUGG3<br>1976:1|- 2005:6|5|Luggage for males|
|68|P1MICG3<br>1976:1|- 2005:6|5|Standard clothing issued to military personnel (n.d.)|
|69|P1GASG3<br>1976:1|- 2005:6|5|Gasoline and other motor fuel|
|70|P1LUBG3<br>1976:1|- 2005:6|5|Lubricants|
|71|P1OILG3<br>1976:1|- 2005:6|5|Fuel oil|
|72|P1LPGG3<br>1976:1|- 2005:6|5|Liquified petroleum gas and other fuel|
|73|P1TOBG3<br>1976:1|- 2005:6|5|Tobacco products (7)|
|74|P1SOAG3<br>1976:1|- 2005:6|5|Soap|
|75|P1CSMG3<br>1976:1|- 2005:6|5|Cosmetics and perfumes|
|76|P1OPHG3<br>1976:1|- 2005:6|5|Other personal hygiene goods|
|77|P1SDHG3<br>1976:1|- 2005:6|5|Semidurable house furnishings (33)|
|78|P1CLEG3<br>1976:1|- 2005:6|5|Cleaning preparations|
|79|P1LIGG3<br>1976:1|- 2005:6|5|Lighting supplies|
|80|P1PAPG3<br>1976:1|- 2005:6|5|Paper products|
|81|P1RXDG3<br>1976:1|- 2005:6|5|Prescription drugs|
|82|P1NRXG3<br>1976:1|- 2005:6|5|Nonprescription drugs|
|83|P1MDSG3<br>1976:1|- 2005:6|5|Medical supplies|
|84|P1GYNG3<br>1976:1|- 2005:6|5|Gynecological goods|
|85|P1DOLG3<br>1976:1|- 2005:6|5|Toys, dolls, and games|
|86|P1AMMG3<br>1976:1|- 2005:6|5|Sport supplies, including ammunition|
|87|P1FLMG3<br>1976:1|- 2005:6|5|Film and photo supplies|
|88|P1STSG3<br>1976:1|- 2005:6|5|Stationery and school supplies|
|89|P1GREG3<br>1976:1|- 2005:6|5|Greeting cards|
|90|P1ARTG3<br>1976:1|- 2005:6|5|Government expenditures abroad|



|91|P1ARSG3<br>1976:1|- 2005:6|5|Other private services|
|---|---|---|---|---|
|92|P1REMG3<br>1976:1|- 2005:6|5|Less: Personal remittances in kind to nonresidents|
|93|P1MGZG3<br>1976:1|- 2005:6|5|Magazines and sheet music|
|94|P1NWPG3<br>1976:1|- 2005:6|5|Newspapers|
|95|P1FLOG3<br>1976:1|- 2005:6|5|Flowers, seeds, and potted plants (95)|
|96|P1OMHG3<br>1976:1|- 2005:6|5|Owner occupied mobile homes|
|97|P1OSTG3<br>1976:1|- 2005:6|5|Owner occupied stationary homes|
|98|P1TMHG3<br>1976:1|- 2005:6|5|Tenant occupied mobile homes|
|99|P1TSPG3<br>1976:1|- 2005:6|5|Tenant occupied stationary homes|
|100|P1TLDG3<br>1976:1|- 2005:6|5|Tenant landlord durables|
|101|P1FARG3<br>1976:1|- 2005:6|5|Rental value of farm dwellings (26)|
|102|P1HOTG3<br>1976:1|- 2005:6|5|Hotels and motels|
|103|P1HFRG3<br>1976:1|- 2005:6|5|Clubs and fraternity housing|
|104|P1HHEG3<br>1976:1|- 2005:6|5|Higher education housing|
|105|P1HESG3<br>1976:1|- 2005:6|5|Elem and second education housing|
|106|P1TGRG3<br>1976:1|- 2005:6|5|Tenant group room and board|
|107|P1TGLG3<br>1976:1|- 2005:6|5|Tenant group employee lodging|
|108|P1ELCG3<br>1976:1|- 2005:6|5|Electricity (37)|
|109|P1NGSG3<br>1976:1|- 2005:6|5|Gas (38)|
|110|P1WSMG3<br>1976:1|- 2005:6|5|Water and sewerage maintenance|
|111|P1REFG3<br>1976:1|- 2005:6|5|Refuse collection|
|112|P1LOCG3<br>1976:1|- 2005:6|5|Local and cellular telephone|
|113|P1INCG3<br>1976:1|- 2005:6|5|Intrastate toll calls|
|114|P1ITCG3<br>1976:1|- 2005:6|5|Interstate toll calls|
|115|P1DMCG3<br>1976:1|- 2005:6|5|Domestic service, cash|
|116|P1DMIG3<br>1976:1|- 2005:6|5|Domestic service, in kind|
|117|P1MSEG3<br>1976:1|- 2005:6|5|Moving and storage|
|118|P1FIPG3<br>1976:1|- 2005:6|5|Household insurance premiums|
|119|P1FIBG3<br>1976:1|- 2005:6|5|Less: Household insurance benefits paid|
|120|P1RCLG3<br>1976:1|- 2005:6|5|Rug and furniture cleaning|
|121|P1EREG3<br>1976:1|- 2005:6|5|Electrical repair|
|122|P1FREG3<br>1976:1|- 2005:6|5|Reupholstery and furniture repair|
|123|P1PSTG3<br>1976:1|- 2005:6|5|Postage|
|124|P1MHOG3<br>1976:1|- 2005:6|5|Household operation services, n.e.c.|
|125|P1ARPG3<br>1976:1|- 2005:6|5|Motor vehicle repair|
|126|P1RLOG3<br>1976:1|- 2005:6|5|Motor vehicle rental, leasing, and other|
|127|P1TOLG3<br>1976:1|- 2005:6|5|Bridge, tunnel, ferry, and road tolls|
|128|P1AING3<br>1976:1|- 2005:6|5|Insurance|
|129|P1IMTG3<br>1976:1|- 2005:6|5|Mass transit systems (79)|
|130|P1TAXG3<br>1976:1|- 2005:6|5|Taxicab (80)|
|131|P1IRRG3<br>1976:1|- 2005:6|5|Railway (82)|
|132|P1IBUG3<br>1976:1|- 2005:6|5|Bus (83)|
|133|P1IAIG3<br>1976:1|- 2005:6|5|Airline (84)|
|134|P1TROG3<br>1976:1|- 2005:6|5|Other (85)|
|135|P1PHYG3<br>1976:1|- 2005:6|5|Physicians (47)|
|136|P1DENG3<br>1976:1|- 2005:6|5|Dentists (48)|
|137|P1OPSG3<br>1976:1|- 2005:6|5|Other professional services (49)|
|138|P1NPHG3<br>1976:1|- 2005:6|5|Nonprofit|
|139|P1FPHG3<br>1976:1|- 2005:6|5|Proprietary|
|140|P1GVHG3<br>1976:1|- 2005:6|5|<br>Government|



|141|P1NRSG3|1976:1 - 2005:6|5|Nursing homes|
|---|---|---|---|---|
|142|P1MING3|1976:1 - 2005:6|5|Medical care and hospitalization|
|143|P1IING3|1976:1 - 2005:6|5|Income loss|
|144|P1PWCG3|1976:1 - 2005:6|5|Workers' compensation|
|145|P1MOVG3|1976:1 - 2005:6|5|Motion picture theaters|
|146|P1LEGG3|1976:1 - 2005:6|5|Legitimate theaters and opera, and entertainments of nonprofit institutions (except athletics)|
|147|P1SPEG3|1976:1 - 2005:6|5|Spectator sports|
|148|P1RTVG3|1976:1 - 2005:6|5|Radio and television repair|
|149|P1CLUG3|1976:1 - 2005:6|5|Clubs and fraternal organizations|
|150|P1SIGG3|1976:1 - 2005:6|5|Sightseeing|
|151|P1FLYG3|1976:1 - 2005:6|5|Private flying|
|152|P1BILG3|1976:1 - 2005:6|5|Bowling and billiards|
|153|P1CASG3|1976:1 - 2005:6|5|Casino gambling|
|154|P1OPAG3|1976:1 - 2005:6|5|Other comml participant amusements|
|155|P1PARG3|1976:1 - 2005:6|5|Pari-mutuel net receipts|
|156|P1REOG3|1976:1 - 2005:6|5|Other|
|157|P1SCLG3|1976:1 - 2005:6|5|Shoe repair|
|158|P1DRYG3|1976:1 - 2005:6|5|Drycleaning|
|159|P1LGRG3|1976:1 - 2005:6|5|Laundry and garment repair|
|160|P1BEAG3|1976:1 - 2005:6|5|Beauty shops, including combination|
|161|P1BARG3|1976:1 - 2005:6|5|Barber shops|
|162|P1WCRG3|1976:1 - 2005:6|5|Watch, clock, and jewelry repair|
|163|P1CRPG3|1976:1 - 2005:6|5|Miscellaneous personal services|
|164|P1BROG3|1976:1 - 2005:6|5|Brokerage charges and investment counseling (61)|
|165|P1BNKG3|1976:1 - 2005:6|5|Bank service charges, trust services, and safe deposit box rental (62)|
|166|P1IMCG3|1976:1 - 2005:6|5|Commercial banks|
|167|P1IMNG3|1976:1 - 2005:6|5|Other financial institutions|
|168|P1LIFG3|1976:1 - 2005:6|5|Expense of handling life insurance and pension plans (64)|
|169|P1GALG3|1976:1 - 2005:6|5|Legal services (65)|
|170|P1FUNG3|1976:1 - 2005:6|5|Funeral and burial expenses (66)|
|171|P1UNSG3|1976:1 - 2005:6|5|Labor union expenses|
|172|P1ASSG3|1976:1 - 2005:6|5|Profession association expenses|
|173|P1GENG3|1976:1 - 2005:6|5|Employment agency fees|
|174|P1AMOG3|1976:1 - 2005:6|5|Money orders|
|175|P1CLAG3|1976:1 - 2005:6|5|Classified ads|
|176|P1ACCG3|1976:1 - 2005:6|5|Tax return preparation services|
|177|P1THEG3|1976:1 - 2005:6|5|Personal business services, n.e.c.|
|178|P1PEDG3|1976:1 - 2005:6|5|Private higher education|
|179|P1GEDG3|1976:1 - 2005:6|5|Public higher education|
|180|P1ESCG3|1976:1 - 2005:6|5|Elementary and secondary schools|
|181|P1NSCG3|1976:1 - 2005:6|5|Nursery schools|
|182|P1VEDG3|1976:1 - 2005:6|5|Commercial and vocational schools|
|183|P1REDG3|1976:1 - 2005:6|5|Foundations and nonprofit research|
|184|P1POLG3|1976:1 - 2005:6|5|Political organizations|
|185|P1MUSG3|1976:1 - 2005:6|5|Museums and libraries|
|186|P1FOUG3|1976:1 - 2005:6|5|Foundations to religion and welfare|
|187|P1WELG3|1976:1 - 2005:6|5|Social welfare|
|188|P1RELG3|1976:1 - 2005:6|5|Religion|
|189|P1FTRG3|1976:1 - 2005:6|5|Foreign travel by U.S. residents (110)|
|190|P1EXFG3|1976:1 - 2005:6|5|Less: Expenditures in the United States by nonresidents (112)|



191 P1TDGG3 1976:1 - 2005:6 5 Durable goods 192 P1TNDG3 1976:1 - 2005:6 5 Nondurable goods 193 P1TSSG3 1976:1 - 2005:6 5 Services 194 PPCE 1976:1 - 2005:6 5 Personal Consumption Expenditures (all items) 

###### **APPENDIX C – Producer Price indices** 

Format is as in Stock and Watson (2002) paper: series number; series mnemonic (NAICS code); data span; transformation code and series description as appears in the database. The transformation for all data was first difference of logarithms, which is coded as 5. This data set contains 154 monthly series with no missing observations. All series are downloaded from the website of BLS. 

|1<br>2|311119<br>311119p|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Other animal food manufacturing<br>5<br>Other animal food manufacturing (primary products)|
|---|---|---|---|
|3|<br>311211|1976:1 - 2005:6|<br>5<br>Flour Milling|
|4|311212|1976:1 - 2005:6|5<br>Rice milling|
|5|311213|1976:1 - 2005:6|5<br>Malt mfg|
|6|311223a|1976:1 - 2005:6|5<br>Other oilseed processing (Cottonseed cake and meal and other byproducts)|
|7|311225p|1976:1 - 2005:6|5<br>Fats and oils refining and blending (Primary products)|
|8|311311|1976:1 - 2005:6|5<br>Sugarcane mills|
|9|311313|1976:1 - 2005:6|5<br>Beet sugar manufacturing|
|10|311412|1976:1 - 2005:6|<br>5<br>Frozen specialty food manufacturing|
|11|311520|1976:1 - 2005:6|<br>5<br>Ice cream and frozen dessert mfg|
|12|311920|1976:1 - 2005:6|5<br>Coffee and tea manufacturing|
|13|312140|1976:1 - 2005:6|5<br>Distilleries|
|14|32211-|1976:1 - 2005:6|5<br>Pulp mills|
|15|32213-|1976:1 - 2005:6|<br>5<br>Paperboard mills|
|16|325620p|1976:1 - 2005:6|5<br>Toilet preparation mfg (Primary products)|
|17|325920|1976:1 - 2005:6|5<br>Explosives manufacturing|
|18|32731-|1976:1 - 2005:6|5<br>Cement mfg|
|19|327320|1976:1 - 2005:6|<br>5<br>Ready mixed concrete mfg and dist|
|20|327410|1976:1 - 2005:6|5<br>Lime|
|21|327420|1976:1 - 2005:6|5<br>Gypsum building products manufacturing|
|22|327910|1976:1 - 2005:6|5<br>Abrasive product manufacturing|
|23|331210|1976:1 - 2005:6|<br>5<br>Iron steel pipe & tube mfg from purch steel|
|24|333210|1976:1 - 2005:6|<br>5<br>Sawmill & woodworking machinery mfg|
|25|334310|1976:1 - 2005:6|5<br>Audio & video equipment mfg|
|26|335110|1976:1 - 2005:6|<br>5<br>Electric lamp bulb & part mfg|
|27|336370|1976:1 - 2005:6|5<br>Motor vehicle metal stamping|
|28|337910|1976:1 - 2005:6|<br>5<br>Mattress mfg|
|29|311421|1976:1 - 2005:6|5<br>Fruit and vegetable canning|
|30|311423|1976:1 - 2005:6|5<br>Dried and dehydrated food manufacturing|
|31|311513|1976:1 - 2005:6|5<br>Cheese manufacturing|
|32|311611|1976:1 - 2005:6|5<br>Animal except poultry slaughtering|
|33|311612|1976:1 - 2005:6|<br>5<br>Meat processed from carcasses|
|34|311613|1976:1 - 2005:6|5<br>Rendering and meat byproduct processing|
|35|311711|1976:1 - 2005:6|<br>5<br>Seafood canning|
|36|311712|1976:1 - 2005:6|<br>5<br>Fresh & frozen seafood processing|
|37|311813p|1976:1 - 2005:6|5<br>Frozen cakes pies & other pastries mfg (Primary products)|
|38|3118233|1976:1 - 2005:6|5<br>Dry pasta manufacturing ( Macaroni  spaghetti  vermicelli  and noodles)|
|39|312111p|1976:1 - 2005:6|5<br>Soft drinks manufacturing (Primary products)|
|40|<br>312221|1976:1 - 2005:6|<br>5<br>Cigarettes|
|41|3122291|1976:1 - 2005:6|5<br>Other tobacco product mfg (Cigars)|
|42|313111|1976:1 - 2005:6|<br>5<br>Yarn spinning mills|
||||<br>Broadwoven fabric finishing mills|
|43|3133111|1976:1 - 2005:6|5<br>( Finished cotton broadwoven fabrics  not finished in weaving mills)|
|44|315111|1976:1 - 2005:6|<br>5<br>Sheer hosiery mills|
|45|315191|1976:1 - 2005:6|5<br>Outerwear knitting mills|
|46|315223|1976:1 - 2005:6|<br>5<br>Men's boy's cut & sew shirt  exc work  mfg|
|47|315224|1976:1 - 2005:6|5<br>Men's boy's cut & sew trouser slack jean mfg|
|48|315993|1976:1 - 2005:6|<br>5<br>Men's and boys' neckwear mfg|
|<br>49|<br>316211|<br>1976:1 - 2005:6|<br> <br>5<br>Rubber and plastic footwear manufacturing|
|50|316213|1976:1 - 2005:6|<br>5<br>Men's footwear  exc athletic  mfg|
|51|316214|1976:1 - 2005:6|<br>5<br>Women's footwear  exc athletic  mfg|
|52|316992|1976:1 - 2005:6|5<br>Women's handbag & purse mfg|
|53|321212|1976:1 - 2005:6|5<br>Softwood veneer or plywood  mfg|
|54|3212191|1976:1 - 2005:6|5<br>Reconstituted wood product mfg (Particleboard  produced at this location)|
|55|3219181|1976:1 - 2005:6|<br>5<br>Other millwork  including flooring|



|56|321991|1976:1 - 2005:6|(Wood moldings  except prefinished moldings made from purchased moldings)<br>5<br>Manufactured homes  mobile homes  mfg|
|---|---|---|---|
|<br>57<br>|<br>3221211<br>|<br>1976:1 - 2005:6<br>|<br> <br>5<br>Paper  except newsprint  mills (Clay coated printing and converting paper)<br> <br>|
|58<br>59|322214<br>324121|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Fiber can  tube  drum & oth products mfg<br>5<br>Asphalt paving mixture & block mfg|
|<br>60|<br>324122|<br>19761 - 20056|<br> <br>5<br>Ahlt hil & ti til f|
|<br>61|<br>324191p|:  :<br>1976:1 - 2005:6|<br>spa snge  coang maeras mg<br>5<br>Petroleum lubricating oils and greases ( Primary products)|
|62|325181|1976:1 - 2005:6|5<br>Alkalies and chlorine|
|63<br>|3251881<br>|1976:1 - 2005:6<br>|5<br>All other basic inorganic chemical manufacturing (Sulfuric acid  gross  new and fortified)<br> <br>|
|64|3251921|1976:1 - 2005:6|5<br>Cyclic crude and intermediate manufacturing (Cyclic  coal tar  intermediates)|
|65|325212|1976:1 - 2005:6|5<br>Synthetic rubber manufacturing|
|66<br>|325222<br>|1976:1 - 2005:6<br>|<br>5<br>Manufactured noncellulosic fibers<br> <br>|
|67<br>68|325314<br>3254111|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Fertilizer  mixing only  manufacturing<br>5<br>Medicinal & botanical mfg (Synthetic organic medicinal chemicals  in bulk)<br>Unsupported plastics film sheet  excluding packaging  manufacturing|
|69<br>|3261131<br>|1976:1 - 2005:6<br>|5<br> <br>( Unsupported plastics film and sheet)<br> <br>|
|70<br>71|326192<br>326211|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Resilient floor covering manufacturing<br>5<br>Tire manufacturing  except retreading|
|<br>72|<br>327111|<br>19761 - 20056|<br> <br>5<br>Vit lbi fit  ft f|
|<br>73|<br>327121|:  :<br>1976:1 - 2005:6|<br>reous pumng xures access g mg<br>5<br>Brick and structural clay tile|
|74<br>75|327122<br>327124|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Ceramic wall and floor tile<br>5<br>Cla refractories|
|<br>76|<br>327125|<br>1976:1 - 2005:6|<br>y<br>5<br>Nonclay Refractory Manufacturing|
|77<br>78|327211<br>327213|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Flat glass manufacturing<br>5<br>Glass container manufacturing|
|<br>79|<br>327331|<br>1976:1 - 2005:6|<br> <br>5<br>Concrete block and brick manufacturing|
|80<br>81|3279931<br>331111|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Mineral wool manufacturing<br>5<br>Iron and steel mills|
|<br>82|<br>331112|<br>19761  20056|<br> <br>5<br>Elllil fll d f|
|<br>83|<br>331221|: - :<br>1976:1 - 2005:6|<br>ectrometaurgca erroaoy prouct mg<br>5<br>Rolled steel shape manufacturing|
|84<br>85|331312<br>331315|1976:1 - 2005:6<br>19761  20056|5<br>Primary aluminum production<br>5<br>Ali ht  lt & fil f|
|<br>|<br>|: - :<br>|<br>umnum see  pae  o mg<br> <br>|
|86|331316|1976:1 - 2005:6|5<br>Aluminum extruded products|
|87|331421|1976:1 - 2005:6|5<br>Copper rolling  drawing & extruding|
||||<br> <br>Other nonferrous metal roll draw extruding<br>|
|88|3314913|1976:1 - 2005:6|5<br>(Titanium and titanium base alloy mill shapes  excluding wire)|
|89|3314923|1976:1 - 2005:6|5<br>Other nonferrous secondary smelt refine alloying (Secondary lead)|
|90|331511|1976:1 - 2005:6|<br>5<br>Iron foundries<br>Hand and edge tools  except machine tools and handsaws<br>|
|91|3322121|1976:1 - 2005:6|5<br>(Mechanics' hand service tools)|
|92|332213|1976:1 - 2005:6|<br>5<br>Saw blade & handsaw mfg<br>|
||||<br>Prefabricated metal building and component manufacturing (Prefabricated<br>|
|93|3323111|1976:1 - 2005:6|5<br>metal building systems  excluding farm service bldgs  & residential buildings)|
|94<br>95|332321<br>332431|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Metal window and door manufacturing<br>5<br>Metal can mfg<br>|
|96|324393|1976:1 - 2005:6|5<br>Other metal container manufacturing<br>( Steel shipping barrels & drums  exc  beer barrels  more than 12 gallon capacity)|
|97<br>|332611<br>|1976:1 - 2005:6<br>|<br>5<br>Spring  heavy gauge  mfg<br> <br>|
|98|3326122|1976:1 - 2005:6|5<br>Spring  light gauge  mfg ( Precision mechanical springs)|
|99<br>|3327224<br>|1976:1 - 2005:6<br>|5<br>Bolt  nut  screw  rivet & washer mfg<br>( Externally threaded metal fasteners  except aircraft)<br> <br>|
|100<br>|332913<br>|1976:1 - 2005:6<br>|5<br>Plumbing fixture fitting & trim mfg<br>|
|101<br>102|332991<br>332992|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Ball and roller bearings<br>5<br>Small arms ammunition mfg|
|<br>103<br>|<br>332996<br>|<br>1976:1 - 2005:6<br>|<br> <br>5<br>Fabricated pipe & pipe fitting mfg<br> <br>|
|104|332998|1976:1 - 2005:6|5<br>Enameled iron & metal sanitary ware mfg|
|105|333111|1976:1 - 2005:6|5<br>Farm machinery & equipment mfg|
|<br>106|<br>333131|<br>19761 - 20056|<br> <br>5<br>Mii hi & it f|
|<br>|<br>|:  :<br>|<br>nng macnery  equpmen mg<br> <br>|
|107|333132|1976:1 - 2005:6|5<br>Oil and gas field machinery and equipment mfg|
|108|333292|1976:1 - 2005:6|5<br>Textile machinery|
|109|333293|1976:1 - 2005:6|<br>5<br>Printin machiner & euiment mf|
|<br>110|<br>3332941|<br>1976:1 - 2005:6|<br>g y  qp g<br>5<br>Food products machinery mfg ( Dairy and milk products plant machinery)|
|111|3332981|1976:1 - 2005:6|5<br>All other industrial machinery mfg<br>(Chemical manufacturing machinery  equipment  and parts)<br>|
|112|3333111|1976:1 - 2005:6|5<br>Automatic vending machine mfg<br>( Automatic merchandising machines  coin operated  excluding parts)|
|113<br>11|333512<br>1|1976:1 - 2005:6<br>11  2|5<br>Machine tool  metal cutting types  mfg<br> <br>hi l  l fi   f|
|4|33353|976: - 005:6|5<br>Macne too  meta ormng types  mg<br>|
|115|3335151|1976:1 - 2005:6|5<br>Cutting tool & machine tool accessory mfg<br>(Small cutting tools for machine tools and metalworking machinery)|
|116<br>|333612<br>|1976:1 - 2005:6<br>|<br>5<br>Speed changer  industrial high speed drive  & gear mfg<br> <br>|
|117|333618|1976:1 - 2005:6|5<br>Other engine equipment mfg|
|118<br>|3339111<br>|1976:1 - 2005:6<br>|5<br>Pump & pumping equipment mfg<br>( Industrial pumps  except hydraulic fluid power pumps)<br> <br>|
|119<br>120|333922<br>3339233|1976:1 - 2005:6<br>1976:1 - 2005:6|5<br>Conveyor & conveying equipment mfg<br>5<br>Overhead crane  hoist & monorail system mfg|



||||( Overhead traveling cranes and monorail systems)|
|---|---|---|---|
||||Industrial truck  tractor  trailer  stacker machinery mfg|
|121|3339241|1976:1 - 2005:6|5<br>( Industrial trucks and tractors  motorized and hand powered)|
|122|333992|1976:1 - 2005:6|5<br>Welding & soldering equipment mfg (Welding & soldering equipment mfg)|
|123|333997|1976:1 - 2005:6|5<br>Scale & balance  except laboratory  mfg|
|124|334411|1976:1 - 2005:6|5<br>Electron tube mfg|
|125|334414|1976:1 - 2005:6|5<br>Electronic capacitor mfg|
|126|334415|1976:1 - 2005:6|5<br>Electronic resistor mfg|
|127|334417|1976:1 - 2005:6|5<br>Electronic connector mfg|
||||Electricity measuring testing instrument mfg|
|128|3345153|1976:1 - 2005:6|5<br>( Test equipment for testing electrical  radio & communication circuits & motors)|
|129|334517p|1976:1 - 2005:6|5<br>Irradiation apparatus manufacturing ( Primary products)<br>Residential electric lighting fixture mfg|
|130|3351211|1976:1 - 2005:6|5<br>( Residential electric lighting fixtures  except portable  & parts)|
|131|335122|1976:1 - 2005:6|5<br>Commercial electric lighting fixture mfg|
|132|335129|1976:1 - 2005:6|5<br>Other lighting equipment mfg|
|133|335212|1976:1 - 2005:6|5<br>Household vacuum cleaner mfg|
|134|335221|1976:1 - 2005:6|5<br>Household cooking appliance mfg|
|135|335311|1976:1 - 2005:6|5<br>Power distribution specialty transformer mfg|
|136|335312|1976:1 - 2005:6|5<br>Motor & generator mfg|
|137|335314p|1976:1 - 2005:6|5<br>Relay & industrial control mfg ( Primary products)|
|138|335911|1976:1 - 2005:6|5<br>Storage battery mfg|
||||Other communication and energy wire mfg|
|139|3359291|1976:1 - 2005:6|5<br>( Power wire and cable  made in plants that draw wire)|
|140|335932|1976:1 - 2005:6|5<br>Noncurrent carrying wiring device mfg|
|141|335991p|1976:1 - 2005:6|5<br>Carbon & graphite product mfg ( Primary products)|
|142|336321p|1976:1 - 2005:6|5<br>Vehicular lighting equipment mfg ( Primary products)|
|143|337121|1976:1 - 2005:6|5<br>Upholstered household furniture mfg|
|144|337122|1976:1 - 2005:6|5<br>Wood household furniture  except upholstered|
|145|337124|1976:1 - 2005:6|5<br>Metal household furniture|
|146|337211|1976:1 - 2005:6|5<br>Wood office furniture mfg|
|147|3372141|1976:1 - 2005:6|5<br>Nonwood office furniture ( Office seating  including upholstered  nonwood)<br>Jewelry  except costume  mfg|
|148|3399111|1976:1 - 2005:6|5<br>( Jewelry made of solid platinum metals and solid karat gold)|
|149|3399123|1976:1 - 2005:6|<br>5<br>Silverware & hollowware mfg ( Flatware and carving sets made wholly of metal)|
|150|339931|1976:1 - 2005:6|<br>5<br>Doll & stuffed toy mfg|
|151|339932|1976:1 - 2005:6|<br>5<br>Game  toy  & children's vehicle mfg|
|152|339944|1976:1 - 2005:6|5<br>Carbon paper & inked ribbon mfg<br>Fastener  button  needle  & pin mfg|
|153|3399931|1976:1 - 2005:6|5<br>( Buttons and parts  except for precious or semiprecious metals and stones)|
|154|3399945|1976:1 - 2005:6|5<br>Broom  brush  & mop mfg ( Other brushes)|



###### **APPENDIX D – Cross-Sectional Industry characteristics** 

For the cross-sectional regressions we use the following data sources: 

**C4** - Concentration ratio. Represents the percentage of sales made by the largest 4 firms in the industry. Source. Bureau of the Census 1997. 

**Profit rates** – average gross profit rates for 1997-2001 based on tax accounting. Source: 2001 Annual Survey of Manufacturers. 

# **CFS Working Paper Series:** 

|**No.**|**Author(s)**|**Title**|
|---|---|---|
|2007/13|**Virgiliu Midrigan**|Menu Costs, Multi-Product Firms, and Aggregate<br>Fluctuations|
|2007/12|**Michael Woodford**|Robustly Optimal Monetary Policy with Near-<br>Rational Expectations|
|2007/11|**Lars E. O. Svensson**<br>**Noah Williams**|Bayesian and Adaptive Optimal Policy under<br>Model Uncertainty|
|2007/10|**Alessandro Calza**<br>**Tommaso Monacelli**<br>**Livio Stracca**|Mortgage Markets, Collateral Constraints, and<br>Monetary Policy: Do<br>Institutional Factors Matter?|
|2007/09|**Mark Gertler**<br>**Antonella Trigari**|Unemployment Fluctuations with Staggered<br>Nash Wage Bargaining|
|2007/08|**Olivier Blanchard**<br>**Jordi Galí**|A New Keynesian Model with Unemployment|
|2007/07|**Kai Christoffel**<br>**Keith Kuester**<br>**Tobias Linzert**|Identifying the Role of Labor Markets for<br>Monetary Policy in an Estimated DSGE Model|
|2007/06|**Gauti B. Eggertsson**<br>**Banjamin Pugsley**|The Mistake of 1937: A General Equilibrium<br>Analysis|
|2007/05|**Michael Bordo**<br>**Christopher Erceg**<br>**Andrew Levin**<br>**Ryan Michaels**|Three Great American Disinflations|
|2007/04|**Michael Sonnenholzner**<br>**Achim Wambach**|On the Role of Patience in an Insurance Market<br>with Asymmetric Information|



Copies of working papers can be downloaded at http://www.ifk-cfs.de 

