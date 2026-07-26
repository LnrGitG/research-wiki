---
title: **University of Pretoria**
type: paper
source_pdf: raw/papers/Gupta_The Effect of Monetary Policy on House Price Inflation FAVAR approach_2009.pdf
converted: 2026-07-26
---



### **University of Pretoria** 

**_Department of Economics Working Paper Series_** 

**The Effect of Monetary Policy on House Price Inflation: A Factor Augmented Vector Autoregression (FAVAR) Approach** Rangan Gupta University of Pretoria Alain Kabundi University of Johannesburg Working Paper: 2009-03 January 2009 

__________________________________________________________ Department of Economics University of Pretoria 0002, Pretoria South Africa Tel: +27 12 420 2413 Fax: +27 12 362 5207 

# THE EFFECT OF MONETARY POLICY ON HOUSE PRICE INFLATION: A FACTOR AUGMENTED VECTOR AUTOREGRESSION (FAVAR) APPROACH 

Rangan Gupta<sup>∗</sup> and Alain Kabundi<sup>#</sup> 

**Abstract** This paper assesses the impact of monetary policy on house price inflation for the nine census divisions of the US economy using a factor-augmented VAR (FAVAR), estimated a large data set comprising of 126 quarterly series over the period 1976:01 to 2005:02. The results based on the impulse response functions indicate that, in general, house price inflation responds negatively to monetary policy shock, but the responses are heterogeneous across the census divisions. In addition, our findings suggests the importance of South Atlantic, East South Central, West South Central, Mountain and the Pacific divisions, in particular, in shaping the dynamics of US house price inflation. 

Keywords: Monetary Policy; House Price Inflation; FAVAR. JEL Classification Codes: C32; E52; R2. 

> ∗ Associate Professor, Department of Economics, University of Pretoria, Pretoria, 0002, South Africa, Email: <u>Rangan.Gupta@up.ac.za. Phone: +27 12 420 3460, Fax: +27 12 362 5207.</u> 

> # To whom correspondence should be addressed. Senior Lecturer, University of Johannesburg, Department of Economics, Johannesburg, 2006, South Africa, Email: <u>akabundi@uj.ac.za. Phone: +27 11 559 2061,</u> Fax: +27 11 559 3039. 

1 

## **1. Introduction** 

The recent global economic downturn attributed to the sub-prime crisis in the US with rapid contagion worldwide, has attracted the attention of academics, policymakers, and economic agents at large, to the developments in the housing sector. Stock and Watson (2003) pointed out that housing prices are leading indicators for real activity, inflation, or both, and, hence, can serve as an indicator as to where the real economy is heading. Evidence in the recent literature, for example, Iacoviello (2005), Case et al. (2005), Iacoviello and Neri (2008) and Vargas-Silva (2008a,b) amongst others, show a strong link between the housing market and economic activity in the US. Moreover, the recent emergence of boom-bust cycles in house prices have been an issue of concern for policy markers (Borio, Kennedy, and Prowse, 1994; Bernanke and Gertler, 1995, 1999), since the bust of the house prices bubble is always followed by significant contractions in the real economy. Given this, it is crucial for central banks to analyze thoroughly the effects of monetary policy on asset prices in general, and real estate in particular, which, in turn, would lead to the understanding of the effects of policy on the economy at large. 

In this backdrop, this paper assesses the impact of monetary policy shocks on house price inflation for the nine census divisions of the US economy<sup>1</sup> by exploiting a data-rich environment which includes 126 quarterly series over the period 1976:01 to 2005:02. For this purpose, the framework used in this paper is a factor-augmented vector autoregressive (FAVAR) model proposed by Bernanke et al. (2005). As Bernanke et al. (2005) indicates, monetary authorities analyze literally thousands of variables in their decision-making process, hence, it is aberrant for anyone, who tries to mimic actions of a central bank, to ignore this fact. Furthermore, the recent literature (Stock and Watson, 2004; and Rapach and Strauss, 2007, 2008, Das et al. (2008a,b, 2009)) gives evidence of the fact that numerous economic variables are potential predictors of house price growth. Intuitively, the FAVAR approach boils down to extracting a few latent common factors from a large matrix of many economic variables, with the former maintaining the same information contained in the original data set without running into the risk of the degrees of freedom problem.<sup>2</sup> Note, the motivation to use regional data emanates from the fact that the impact of monetary policy on the US economy differs according to regions, since economic conditions prevailing during a monetary policy shock are not necessarily the same across the regions (Carlino and DeFina (1998, 1999), and Vargas-Silva (2008b)).. 

It must, be pointed out that though this is the first study<sup>3</sup> to analyze the effect of monetary policy house price inflation in the nine census divisions of the US economy using a FAVAR model, by no means is this current study the first one to analyze the impact of monetary policy on house prices. See for example, Iacoviello (2002), McCarthy and Peach (2002), Iacoviello and Minetti (2003, 2008), Ndahiriwe and Gupta (2008) and Vargas-Silva (2008a) for analyses of the effect of monetary policy shocks on 

> 1 The US Census bureau organizes the fifty states into five census regions, and further into nine divisions, which, from the east to west coast, are: New England, Middle Atlantic, South Atlantic, East South Central, West South Central, West North Central, East North Central, Mountain, and Pacific.. 2 See Section 2 for further details. 

> 3 The only other study that we know of which uses a FAVAR approach to analyze the effect of monetary policy on the US housing market is that of Vargas-Silva (2008b). However, the author studied the impact of monetary policy on housing starts, housing permits and mobile home shipments using a dataset of 120 monthly indicators. 

2 

house price in the US, Europe and South Africa.<sup>4</sup> However, all these studies are based on either a reduced-form Vector Autoregressive (VAR) model, a Vector Error Correction Model (VECM) or a Structural VAR (SVAR) model, which, in turn, limits them to at the most 8 to 12 variables to conserve the degrees of freedom. Arguably, and as indicated above, there are a large number of variables that affects monetary policy and the housing market, and not including them often leads to puzzling results that are not in line with economic theory due to the small information set (Walsh, 2000). Moreover, in these studies, the authors often arbitrarily accept specific variables as the counterparts of the theoretical constructs (for example the gross domestic product as a measure of economic activity or the first difference of the logarithm transformed consumer price index as a measure of inflation), which, in turn, may not be perfectly represented by the selected variables. In addition, previous studies can only obtain the impulse response functions (IRFs) from those few variables included in the model, implying that in each VAR, VECM or SVAR, the IRFs are typically obtained with respect to only one variable related to the housing market. Given its econometric construct, the FAVAR model solves all these problems. 

The remainder of the paper is organized as follows: Section 2 briefly discusses the FAVAR framework, while, Section 3 discusses the data and the identification structure. Section 4 reports and analyzes the impulse response functions, and Section 5 concludes. 

## **2. The FAVAR**<sup>**5**</sup> 

Let<sup>_Y_</sup> _t_<sup>be a</sup> _M_ × 1 vector of observable economic variable assumed to drive the dynamics of the economy, in our  case, this happens to be the Federal funds rate (FFR) only. As in VARs, the monetary policy instrument is allowed to have a pervasive effect throughout the economy. Further assume that<sup>_F_</sup> _t_<sup>is a</sup> _K_ × 1 vector of unobserved factors that summarizes additional important information, such as potential output not fully captured by<sup>_Y_</sup> _t_<sup>. Note</sup><sup>_F_</sup> _t_<sup>can also represent theoretical concepts such as price pressures, credit</sup> conditions, or even economic activity that are a combination of economic variables which cannot be represented by one particular series. 

Assume that the joint dynamics of ( _Ft_ ′ ,<sup>_Y_</sup> _t_ ′) are given by the following equation: 





> where Φ ( _L_ ) is a conformable lag polynomial of finite order _p_ and<sup>_v_</sup> _t_<sup>is the error term</sup> 

> with zero mean and a covariance matrix _Q_ . 

> 4 Note, besides the empirical part of the paper, Iacoviello and Minetti (2003) uses a calibrated Dynamic Stochastic General Equilibrium (DSGE) model to analyze the impact of monetary policy on house prices. More recently, Iacoviello and Neri (2008) used a more elaborate estimated DSGE model for this purpose. However, the model is restricted in the sense that it used only 10 macroeconomic variables including only a few housing market variables. 

> 5 This paper follows the econometric framework of the FAVAR model described in Bernanke et al. (2005). 

3 

Equation 1 is a standard VAR. However, the difficulty here, compared to standard VARs, is that the vector of factors<sup>_F_</sup> _t_<sup>is unobserved, which means that the model cannot</sup> be estimated based on standard econometric techniques, such as the ordinary least squares (OLS). The proper estimation of the model entails  the use of factor analysis, as proposed by Stock and Watson (1998). For this purpose, we assume that the factors summarize information contained in a large panel of economic time series. Let _X t_ be a _N_ × 1 vector of informational variables, where _N_ is large, such that _N_ > _K_ + _M_ . Assume _X t_ is related to both the observed variables<sup>_Y_</sup> _t_<sup>and unobserved factors</sup><sup>_F_</sup> _t_<sup>as follows:</sup> 





_f y_ where Λ is a _N_ × _K_ matrix of factor loadings, Λ is _N_ × _M_ , and<sup>_e_</sup> _t_<sup>is a</sup> _N_ × 1 vector of the error term, which, in turn, is weakly correlated with mean zero. In essence<sup>_Y_</sup> _t_<sup>and</sup><sup>_F_</sup> _t_ are common forces that drive the dynamics of _X t_ . Note, it is not restrictive to assume in principle, that _X t_ is dependent on current value of<sup>_F_</sup> _t_<sup>, as factors can always capture</sup> arbitrary lags of some fundamental factors. Excluding the observable factors from Equation 2, we have what Stock and Watson (1998) refer as a dynamic factor model. In this paper, we follow a realistic framework by assuming that the central bank and the econometrician observe only the monetary policy instrument, the Federal funds rate, i.e., _Yt_ = _FFRt_ . 

The estimation procedure consists of a two-step approach proposed by Bernanke et al. (2005), which, in turn, provides a way of uncovering the common space spanned by the factors of _X t_ , _C_ ( _Ft_ ,<sup>_Y_</sup> _t_ ) . In the first step, the space spanned by the factors is estimated using the first _K_ + _M_ principal components of _X t_ , _C_<sup>ˆ</sup> ( _Ft_ ,<sup>_Y_</sup> _t_ ) . Stock and Watson (2002) demonstrates that with a large _N_ , and if the number of principal components is at least as large as the number of factors, the principal component recover the space spanned by both<sup>_F_</sup> _t_<sup>and</sup><sup>_Y_</sup> _t_<sup>. However,</sup><sup>_F_ˆ</sup> _t_<sup>is obtained as the part of</sup> _C_<sup>ˆ</sup> ( _Ft_ ,<sup>_Y_</sup> _t_ ) , which is is not spanned by<sup>_Y_</sup> _t_<sup>. In the second step, the FAVAR model is estimated by a standard VAR method</sup> with<sup>_F_</sup> _t_<sup>replaced by</sup><sup>_F_ˆ</sup> _t_<sup>. As in standard a VAR, measuring the effect of monetary policy,</sup> the Federal funds rate is ordered last with the assumption that unobserved factors do not react to monetary policy shocks contemporaneously, which, in turn, produces orthogonal residuals. The reduced form VAR, based on Equation 1, then has the following structural form: 



> where Γ ( _L_ ) is a conformable lag polynomial of finite order _p_ and<sup>_u_</sup> _t_<sup>is a vector of</sup> structural innovations. Given this, we compute the IRFs of<sup>_F_ˆ</sup> _t_<sup>and</sup><sup>_Y_</sup> _t_<sup>as follows:</sup> 

4 

(4) 



− 1 where Ψ ( _L_ ) is a lag polynomial of order _h_ and Ψ ( _L_ ) = Γ ( _L_ ) . 

Given that _X t_ is estimated by _X_ ˆ _t_ = Λ ˆ _f F_ ˆ _t_ + Λ ˆ _yYt_ + _et_ , based on Equation 2, the IRFs of _X_<sup>ˆ</sup> _t_ are given by: 



## **3. Data** 

The data set contains 116 quarterly macroeconomic series of the US economy used by Boivin et al. (2008), and covers the period of 1976:01 to 2005:02.<sup>6</sup> The data set includes measures of industrial production, several price indices, interest rates, employment as well as other key macroeconomic and financial variables. To this data set, we added the national house price, as well as, the house price of the nine census divisions of the US<sup>7</sup> , making it a dataset of 126 variables.<sup>8</sup> Following Bernanke et al. (2005), we divide the data set into two categories, _slow moving_ and _fast moving_ . _Slow moving_ variables are those that do not respond contemporaneously to unanticipated monetary policy shocks. They include variables such as industrial production, consumption, employment, and prices. In contrast, _fast moving_ variables respond contemporaneously to policy shocks. They mainly comprise of financial variables. All series are seasonally adjusted and transformed to induce stationarity. For the aggregate and census division house prices, stationarity required us to transform the data into their respective growth rates, generated by taking the first difference of the log-transformed data. As in Bernanke et al. (2005), we include five common factors in the estimation of the FAVAR with a lag length ( _p_ ) of 4. Similar to these authors, we find that increasing the number of factors further does not change the results substantially. To account for uncertainty in the estimation of the factors, a bootstrap technique based on Kilian (1998) is implemented. This is necessary in constructing the 90 percent confidence intervals of the impulse respones. 

## **4. Empirical Results** 

Figure 1 displays the impulse response functions of house price inflation of the nine census divisions over 20 quarters, resulting from an increase in the FFR. The FFR 

> 6 Given that only quarterly data for house prices of the census divisions are available at the start of the sample period of the date set used by Boivin et al. (2005),  the 116 monthly macroeconomic variables taken from this data set, were converted to their quarterly values by calculating averages of the monthly data. 7 The house price indexes correspond to Freddie Mac's Conventional Mortgage Home Price Index (CMHPI), which, in turn, provides a measure of typical price inflation for houses within the US. In this paper, following Das et al. (2009), we use the purchase-transactions only series of the CMHPI, which dates back as far as 1970:02. 

> 8 Please refer to Boivin et al. (2008) for further information on the data set. 

5 

increases to approximately 0.25 percent, and stays significant for a short period. Following the contractionary monetary policy, the impact on house price inflation across the regions and, hence, the aggregate economy is negative in general. These results are in line with theory and are opposite to the so-called _home price puzzle_ observed by McCarthy and Peach (2002). Note, the authors observed an increase in home price following a positive interest rate shock for a part of their sub-sample. We attribute this difference to misspecification in small-scale VARs due to their inability to take into account various potential predictors of house prices. The gain witnessed here suggests that a FAVAR methodology, which exploits a large set of information, improves the accuracy of econometric models in predicting the effects of monetary policy, and, therefore, could address puzzling effects observed otherwise. 



<!-- Start of picture text -->
FFR New England Middle Atlantic South Atlantic East South Central West South Central<br>0.1 0.4 0.1 0.1<br>0.2 0.1<br>0 0.2 0 0<br>0.1 0<br>-0.1 0 -0.1 -0.1<br>0 -0.1<br>-0.2 -0.2 -0.2 -0.2<br>-0.1 -0.2<br>-0.2 -0.3 -0.3 -0.4 -0.3 -0.3<br>0 20 0 20 0 20 0 20 0 20 0 20<br>West North Central East North Central Mountain Pacific USA Total<br>0.4 0.4 0.4 0.4<br>0<br>0.2 0.2 0.2 0.2<br>-0.1<br>0 0 0 0<br>-0.2<br>-0.2 -0.2 -0.2 -0.2<br>-0.3<br>-0.4 -0.4 -0.4 -0.4 -0.4<br>0 20 0 20 0 20 0 20 0 20<br><!-- End of picture text -->

Figure 1: IRFs of House Price Inflation following a Contractionary Monetary Policy Shock 

However, the reaction of house price inflation to a contractionary monetary policy shock is different across regions, hence, vindicating the justification of looking at regional level data. New England and Middle Atlantic displays a positive, but insignificant, response at the impact. However, unlike in the case of the _home price puzzle_ the effect is not at all persistent. The positive response is followed by a negative and significant short-lived effect. The contraction of New England reaches 0.1 percent before recovering, while the drop in Middle Atlantic is somewhat small. The initial positive effect in New England and Middle Atlantic is possibly because of the reluctance of the sellers in realizing losses during a downturn due to loss aversion (Genesove and Mayer, 2001). Given the dominance of real estate in the states that are covered by these two regions,<sup>9</sup> such a behavior on part of the sellers are well-justified, at least for a short while.  The initial impact in the South Atlantic region is virtually non-existent, but negative afterward. Contrary to the first two regions, South Atlantic does display a 

> 9 See Carlino and DeFina (1998, 1999) for further details. 

6 

prolonged effect. The rest of regions follow the same pattern: a negative response after the policy shock, followed by long lasting effects that die out progressively. Importantly the response of house price inflation at the national level is similar to most of regions, excepting New England and Middle Atlantic. This implies that the dynamics of house price in the US are not determined by either New England or Middle Atlantic. 



Figure 2: Layout of the Nine Census Divisions of the US. (Source: US Department of Commerce, Economics and Statistics Administration, US Census Bureau.)<sup>10</sup> 

These findings seem to be in line with Carlino and DeFina (1999) and Vargas-Silva (2008a). Carlino and DeFina (1999) indicate that the dominant industries in the states under New England and Middle Atlantic are mainly finance, insurance and real estate in nature, which, in turn, are less sensitive to monetary policy. Hence, the short-lived effect on house prices, as seen above is quite understandable. In addition, Carlino and DeFina (1999) also points out that the interest sensitivity of a state’s industries is likely to increase if a prominent percent of a state’s total gross state product (GSP) is accounted for by construction. Besides this, they also indicated that consumer spending on housing tends to be interest sensitive as well.  Moreover, Vargas-Silva (2008a) suggests that most of the housing activity in the US is taking place in the South, which includes South Atlantic, East South Central and West South Central. So given the observations made by Carlino and DeFina (1999) and Vargas-Silva (2008a), it is most probable that the dynamics of the US housing market is driven by the South, and the similarity of the reaction of the national house price inflation with the southern regions tends to vindicate this point as well. Further note that the Pacific region, in particular, and Mountain census division also seems to play an important role in shaping the movement of the US house 

> 10 Please refer to: http://commons.wikimedia.org/wiki/File:Census_Regions_and_Divisions.PNG. 

7 

price inflation following a monetary policy shock. This is most likely due to the importance of new-home construction industries in California and Arizona, which, respectively, belongs to these regions (Carlino and DeFina, 1999, California Building Industry Association<sup>11</sup> ). In addition, given the importance of the housing market of California, the spatial influence it could have on Oregon, belonging to the Pacific division, and on especially Nevada and Arizona and other states falling under the Mountain region cannot be ignored as well (Kuethe and Pede, 2008 and Gupta and Miller, 2009).<sup>12</sup> Given, this the movement in the housing price of California in response to a monetary policy shock is likely to have an impact on the other states of the region, as well as, on the states of its neighboring region(s), especially where housing is an important part of the GSP. All these effects taken together, in turn, is likely to impact the overall US house price inflation. Figure 2 above presents the nine census divisions of the US to provide a general idea about their layout and the states they include in an attempt to assist the reader to follow better the explanations provided above. 

## **5. Conclusions** 

This paper assesses the impact of a positive monetary policy shock on house price inflation for the aggregate US economy, as well as, the nine census divisions of the of the economy using a FAVAR estimated with 126 variables spanning the period of 1976:Q1 to 2005:Q2. 

Overall, the results show that house price inflation responds negatively to a positive monetary policy shock, suggesting that the framework does not experience the widely observed _price puzzle_ , encountered while analyzing monetary policy shocks with smallscale VARs. It, thus, points to the benefit gained by using a large information set. Not surprisingly, the reaction of house price inflation is found to differ across regions, indicating the fact that economic conditions prevailing during a monetary policy shock are not necessarily the same across the regions. Specifically, we find the New England and Middle Atlantic census divisions to display a small, insignificant and non-persistent positive response immediately after the shock, which is then followed by a small and short-lived negative effect. In contrast, the rest of the regions depict negative responses at the impact, and subsequently these responses die out progressively, though they are found to last relatively longer, when compared to New England and Middle Atlantic. Finally, given that the house price inflation at the national level is found to display the same pattern as most regions, especially, the South (South Atlantic, East South Central and West South Central), the Mountain and the Pacific, we conclude that New England and 

> 11 See: http://www.cbia.org/go/cbia/newsroom/press-releases/housing-industry-in-california-fundamentalto-economic-recovery/ for further details, where it is pointed out that when one accounts for all related activities that complement new-home construction, it is the single largest industry in California, accounting for 11 percent of all economic activity in the state. 

> 12 Gupta and Miller (2009) argues that residents of Southern California sell their local homes, cash out significant equities, and move (retire) to Las Vegas and Phoenix, where they significantly upgrade the quality of their homes. Moreover, they point out that other Mountain Southwest Metropolitan Statistical Areas (MSAs) may also respond to home prices in Los Angeles and San Francisco. Recently, the Brookings Institution (2008) has released a report on the rapid growth in the Mountain Southwest, identifying Las Vegas, Phoenix, Denver, Salt Lake City and Albuquerque as five megapolitan areas. 

8 

Middle Atlantic plays a negligible role in explaining the dynamics of US house price inflation. This is likely to be the case, given the dominance of interest-insensitive industries in the GSP of the states under the latter two regions and the importance of the interest-elastic construction industry in the South and the Pacific regions. As part of future research, it would be interesting to analyze the robustness of the results based on a Bayesian VAR (BVAR), developed recently by Banbura et al. (2008), since just like the FAVAR, the BVAR, given its estimation methodology, can also handle a data set of any size. Moreover, unlike the FAVAR, the large-scale BVAR, via appropriate design of the interaction matrix of the variables, can account for spatial influences of neighboring regions and also asymmetric effects of regional variables and national variables on each other. Note regional variables are likely to have minor effects on national variables, while, the national variables are more prone to affect the regional variables strongly. 

## **References** 

Banbura, M., Gianonne, D., & Reichlin, L. (2008). Bayesian VARs with Large Panels. ECB, Working Paper, 966. 

- Bernanke, B.S., & Gertler, M. (1995). Inside the black box: The credit channel of monetary policy transmission. _The Journal of Economic Perspectives_ 9, 27–48. 

- Bernanke, B.S., & Gertler, M.. (1999). Monetary Policy and Asset Volatility. _Federal Reserve Bank of Kansas City, Economic Review,_ 84(4), 17-52. 

- Bernanke, B. S., Boivin, J. & Eliazs, P. (2005). Measuring the effects of monetary policy: A Factor Augmented Vector Autoregressive (FAVAR) Approach. _The Quarterly Journal of Economics_ , 120, 387–422. 

Boivin, J., Giannoni, M., & Mihov, I. (2008). Sticky Prices and Monetary Policy: Evidence from Disaggregated U.S. Data. _Mimeo_ 

- Borio, C.E.V., Kennedy, N., & Prowse, S.D. (1994). Exploring Aggregate Asset Price Fluctuations Across Countries: Measurement, Determinants, and Monetary Policy Implications. BIS Economics Paper No. 40. 

- Brookings Institution, (2008). Mountain Megas: America’s Newest Metropolitan Places 

   - and a Federal Partnership to Help Them Prosper. Metropolitan Policy Program, available at: 

   - http://www.brookings.edu/~/media/Files/rc/reports/2008/0720_intermountain_west_s arzynski/IMW_full_report.pdf 

- Carlino, G.A., & DeFina, R.H. (1998). The differential regional effects of monetary policy. _The Review of Economics and Statistics_ 80, 572–587. 

- Carlino, G.A., & DeFina, R.H. (1999). Do states respond differently to changes in monetary policy? _Business Review,_ Federal Reserve Bank of Philadelphia (July/August), 17–27. 

- Case, K., Shiller, R., & Quigley, J. (2005). Comparing wealth effects: The stock market versus the housing market. _Advances in Macroeconomics_ , 5(1), 1-32. 

- Das, S., Gupta, S.,  & Kabundi, A. (2008a). “Is a DFM Well-Suited for Forecasting Regional House Price Inflation?” _Working Paper No. 85_ , Economic Research Southern Africa. 

- Das, S., Gupta, S.,  & Kabundi, A. (2008b). Could We Have Forecasted the Recent Downturn in the South African Housing Market? _Working Paper No. 200831_ , 

9 

Department of Economics, University of Pretoria. 

Das, S., Gupta, S.,  & Kabundi, A.  (2009). Forecasting Real House Price Growth in the Nine Census Divisions of the US. _Working Paper No. 200902_ , Department of Economics, University of Pretoria. 

Genesove, D., & Mayer, C.J..  (2001), Loss Aversion and Seller Behavior: Evidence from the Housing Market. NBER Working Paper no. 8143, March. 

Gupta, R., & Miller, S.M. (2008). Ripple Effects” and Forecasting Home Prices in Los Angeles, Las Vegas and Phoenix. _Working Paper No. 200901_ , Department of Economics, University of Pretoria. 

Iacoviello, M. (2002). House Prices and Business Cycles in Europe: A VAR Analysis. _Working Paper No. WP540_ , Department of Economics, Boston College, US. 

Iacoviello, M. (2005). House prices, borrowing constraints, and monetary policy in the business cycle. _American Economic Review_ 95, 739–764. 

Iacoviello, M., & Minetti, R. (2003). Financial liberalisation and the sensitivity of house prices to monetary policy: theory and evidence. _The Manchester School,_ 71(1), pp. 20-34. 

Iacoviello, M., & Minetti, R. (2007). The Credit Channel of Monetary Policy: Evidence from the Housing Market. _Journal of Macroeconomics_ , Vol. 30 (1): 69-96. 

Iacoviello, M., & Neri, S. (2008). Housing Market Spillovers: Evidence from an Estimated DSGE Model. _Working Paper No. 659_ , Boston College Department of Economics. 

Kilian, L, (1998). Small-Sample Confidence Intervals for Impulse Response Functions. _Review of Economics and Statistics_ , 80(2), 218-230. 

McCarthy, J., Peach, R., 2002. Monetary policy transmission to residential investment. _Economic Policy Review_ , 139–158. 

Kuethe, T. H., & Pede, V. (2008). Regional housing Price Cycles: A Spatio-Temporal Analysis Using US State Level Data. Working Paper #08-14, Department of Agricultural Economics, Purdue University. 

Ndahiriwe, K., & Gupta, R. (2008). Financial Liberalization and the Effectiveness of Monetary Policy on House Prices in South Africa, _Working Paper No. 200803_ , Department of Economics, University of Pretoria. 

Rapach, D.E., & Strauss, J.K. (2007). Forecasting Real Housing Price Growth in the Eighth District States. _Federal Reserve Bank of St. Louis. Regional Economic Development_ . 3(2): 33–42. 

Rapach, D.E., & Strauss, J.K. (2008). Differences in Housing Price Forecast ability Across U.S. States. Mimeo, Department of Economics, St. Louis University. 

Sims, C. (1992). Interpreting the Macroeconomic Time Series Facts: The Effects of Monetary Policy. _European Economic Review_ , 36(5), 975-1000. 

Stock, J.H., & Watson, M.W. (1998). Diffusion Indexes. NBER Working Paper No. 6702 Stock, J.H., & Watson, M.W. (2002). Macroeconomics forecasting using diffusion indexes. _Journal of Business and Economic Statistics,_ 20, 147–62. 

Stock, J.H., & Watson, M.W. (2003). Forecasting Output and Inflation: The Role of Asset Prices”. _Journal of Economic Literature_ , 41(3), 788-829. 

Stock, J.H., & Watson, M.W. (2004). “Combination Forecasts of Output Growth in a Seven-Country Data Set. _Journal of Forecasting_ , 23(6), 405-430 

10 

Vargas-Silva, C. (2008a). Monetary policy and the US housing market: A VAR analysis imposing sign restrictions. _Journal of Macroeconomics_ 30, 977–990 

Vargas-Silva, C. (2008b). The Effect of Monetary Policy on Housing: A FactorAugmented Vector Autoregression (FAVAR) Approach. _Applied Economics Letters_ , 15(10), 749 - 752. 

Walsh, C.E. (2000). Monetary Theory and Policy, The MIT Press, Cambridge: Massachusetts. 

11 

