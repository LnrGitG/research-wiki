---
title: **RESEARCH ARTICLE**
type: paper
source_pdf: raw/papers/Chen_Forecasting House Prices The Role of Market Interconnectedness_2026.pdf
converted: 2026-07-26
---

**_Journal of Forecasting_** 



## **RESEARCH ARTICLE** 

# **Forecasting House Prices: The Role of Market Interconnectedness** 

Zac Chen<sup>1</sup> |  George Milunovich<sup>2</sup> |  Shuping Shi<sup>2</sup> |  Ben Wang<sup>2</sup> 

1CleanCo Queensland, Brisbane, Australia | 2Macquarie University, Sydney, Australia 

**Correspondence:** George Milunovich (george.milunovich@mq.edu.au) 

**Received:** 11 October 2024 | **Revised:** 16 January 2026 | **Accepted:** 20 January 2026 

**Keywords:** connections | housing prices | large dimension | model confidence set | out- of- sample forecasting | shrinkage | sparsity 

## **ABSTRACT** 

While the existing research uncovers interconnections between various housing markets, it largely ignores the question of whether such linkages can improve house price predictions. To address this issue, we proceed in two steps. First, we forecast disaggregated house price growth rates from Australia and China to determine whether incorporating price links can improve out- of- sample predictions. We find that accounting for within- city house price interconnectivity in Sydney and Melbourne can indeed improve house price predictions. However, when forecasting city- level prices from China, univariate models produce superior predictions. Second, in order to shed light on our empirical findings, we conduct simulation experiments calibrated to reflect the connections estimated from the data. The predictive ability of house price connectivity hinges on the sparsity and strength of the connections between interconnected markets. In the presence of stronger and denser connections, connectivity information is crucial for improving short- term forecasts. On the other hand, when the connections are sparse and weak (as in the Chinese housing data), the univariate models outperform. Our study shows that finding evidence of significant price interconnections does not always lead to forecasting gains. 

**JEL Classification:** R39, C32, C51, C53 

## **1   |   Introduction** 

The residential real estate sector is a key driver of economic growth and affects many important macroeconomic variables. The literature shows that house prices influence consumption (Case et al. 2005; Campbell and Cocco 2007), employment (Abraham and Hendershott 1996), income (Case and Shiller 1990; Malpezzi 1999; Favilukis et al. 2017), interest rates (Muellbauer and Murphy 1997), and inflation (Abelson et al. 2005). Furthermore, financial markets transmit shocks from the housing sector to other seemingly unrelated parts of the economy, as evidenced by the worldwide financial meltdown of 2007. Given the important role that house prices play in a globally connected economy, they are closely monitored, and accurate predictions of future real estate market conditions are sought after by both private and public sector institutions. In this paper, we extend the literature on forecasting house 

prices by examining whether utilizing the interconnectedness between disaggregated house prices can improve the accuracy of their out- of- sample forecasts. 

An important empirical finding is that house prices exhibit connectivity across various domains. The observation that house prices move in tandem has been tested on national (Hirata et al. 2013; Milunovich 2020b), regional (DeFusco et al. 2018; Gupta and Miller 2012; Flor and Klarl 2017) and within- city (Hurn et al. 2022) levels. Such relationships can form through a number of different mechanisms, including macroeconomic and financial market dependencies, geographic and cultural proximity, as well as through regional development plans in the case of within- metropolitan connectivity (Carleton et al. 2022). Although existing research provides ample evidence for the presence of interconnectedness in various housing markets, see also Cotter et al. (2015), Tsai (2015), Zhang and Fan (2019) and 

This is an open access article under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. 

© 2026 The Author(s). Journal of Forecasting published by John Wiley & Sons Ltd. 

1 

_Journal of Forecasting,_ 2026; 0:1–31 https://doi.org/10.1002/for.70121 

Antonakakis et al. (2018), the literature largely ignores the question of whether uncovered connections can improve house price forecasts. 

The literature on modeling and predicting house prices is extensive and has been reviewed in several surveys, including Gatzlaff and Tirtiroğlu (1995), Ghysels et al. (2013), Duca et al. (2021), and Meszaros (2024). Although a comprehensive review of this work is beyond the scope of our paper, we highlight several findings that are particularly relevant to our discussion. The focus of early research on the predictability of house prices was on testing market efficiency and assessing the effectiveness of various predictors based on in- sample analysis. The key finding of this literature is that real house price growth rates exhibit positive serial correlation and predictability over short horizons (e.g., Case and Shiller 1989, 1990; Gau 1984, 1985; Schindler 2013). This predictability is linked to various measures of income, interest rates, population, inflation, rent, and labor market variables (see, e.g., Abraham and Hendershott 1996; Cho 1996; Johnes and Hyclak 1999). However, as noted in Rapach and Strauss (2007, 2009), it is difficult to choose a priori a set of variables that are consistently effective for out- of- sample house price forecasting because their predictive power can vary over time. Next, there is evidence to suggest that large- scale models tend to outperform smaller specifications in forecasting house price growth (e.g., Gupta 2013), especially models accounting for geographic proximity (e.g., Gupta and Das 2010), economic fundamentals (e.g., Bork and Müller 2018), and financial liquidity factors (e.g., Ellington et al. 2023). 

In this paper, we analyze within- city house prices in Australia and city- level prices in China, directly addressing the question of whether accounting for house price connections can help improve their out- of- sample predictions. We make a twofold contribution to the literature. First, in our empirical analysis, we study house price growth rates for Local Government Areas (LGAs)<sup>1</sup> within Sydney (32 LGAs) and Melbourne (31 LGAs), the two largest cities in Australia, and for city- level house price growth rates across 88 cities in China. House price within these markets is analyzed in Hurn et al. (2022), who find evidence of increasing price connectedness over time. However, they do not explore whether this connectedness can enhance out- of- sample predictions of disaggregated house prices, compared to models that do not consider connectivity. To answer this question, we capture within- region price connectivity using large- dimensional vector autoregressive (LDVAR) models separately for each of the three markets. Due to the high number of parameters present in these models, we employ the least absolute shrinkage and selection operator (LASSO) technique for coefficient estimation. 

The combined LDVAR- LASSO method produces sparse models, where only a subset of the coefficients are nonzero and thus functions as a variable selection device. Our LDVAR- LASSO approach is related to the NETS framework of Barigozzi and Brownlees (2019). However, while NETS imposes sparsity on both the VAR dynamics and the inverse covariance matrix of the innovations to uncover contemporaneous network structures, our approach imposes sparsity only on the VAR coefficients. Such models have been shown to produce good forecasting performance in macroeconomic applications; see, for example, De Mol et al. (2008), and in finance, see, for example, Chinco 

et al. (2019). While the LDVAR- LASSO method has been employed to evaluate connectedness among house price growth series in Gabauer et al. (2024) and Balcilar et al. (2022), it has not yet been used to determine whether the observed connectedness can enhance out- of- sample predictions in this context. Thus, we specify the models with and without connectivity and measure the impact of accounting for price interdependencies on the prediction accuracy. We generate out- of- sample forecasts for 1- , 3- , 6- , and 12- months ahead house price growth rates and employ the squared forecast error loss function and the model confidence set (MCS) procedures of Hansen et al. (2011) to evaluate the predictions. 

Our second contribution to the literature expands the understanding of LDVAR- LASSO methods in the context of out- ofsample forecasting and is thus largely methodological in nature. Namely, we are interested in uncovering the conditions under which house price interconnectedness can improve out- ofsample forecasts. Since we capture connectedness via LDVAR models, we propose investigating the effects of sparsity and connectivity strength of the LDVAR coefficient matrices on predictive efficacy. In particular, we define sparsity by the proportion of zero elements in the parameter matrices, while connectivity strength is gauged by the magnitude of the lagged connections. Although the statistical properties of LASSO estimators for LDVAR models have been examined in the literature, see, for example, Basu and Michailidis (2015) and Kock and Callot (2015), there are few systematic investigations of their out- of- sample forecasting performance and the relationship with the underlying interdependency structure. We address this issue by conducting a simulation study calibrated to our empirical results. 

We summarize our results as follows. The LDVAR model outperforms univariate models across all horizons for Sydney and at short horizons (1–6 months) for Melbourne, while univariate models consistently dominate in the Chinese housing markets. Robustness checks with alternative model specifications and evaluation criteria confirm that our results remain largely unchanged. Our simulation study highlights several key findings. While both sparsity and connectivity strength affect the predictive performance of LDVAR models, connectivity strength plays the dominant role. When connectivity is weak, univariate models outperform LDVAR across all horizons. When connectivity is strong, ignoring interdependence leads to poorer forecasts, though the impact diminishes at longer horizons. These results are robust to different loss functions (squared and absolute errors) and estimation methods (LASSO and adaptive LASSO). 

The paper is structured as follows. Section 2 outlines our modeling approach, while Section 3 introduces the data and presents our primary empirical findings. This discussion is expanded in Section 4, where we consider a number of alternative specifications and robustness tests. In Section 5, we provide an explanation for our empirical findings by conducting a simulation study. Finally, Section 6 contains our concluding remarks. 

## **2   |   The Econometric Method** 

This section presents our empirical framework for incorporating connectivity into large- dimensional multivariate time series 

2 

_Journal of Forecasting,_ 2026 

forecasting and evaluating its effectiveness in improving out- ofsample predictions. In Section 2.1, we introduce the dynamic forecasting models utilized in our study, and in Section 2.2, we elaborate on the estimation methods used to fit these models. After estimating the models, we generate out- of- sample predictions and assess their performance using the techniques detailed in Section 2.3. Following our main analysis using these methods, we perform several robustness checks, as explained in Section 2.4. Lastly, we conduct a simulation study, calibrated to our empirical findings, to explore the impact of different levels of connectedness on the predictive effectiveness of our models, as outlined in Section 2.5. 

## **2.1   |   Forecasting Models** 

� Let **_y_** _t_ = [ _yt_<sup>(1),</sup><sup>_y_</sup> _t_<sup>(2), …,</sup><sup>_y_</sup> _t_<sup>(</sup><sup>_N_)</sup> ] be a _N_ - dimensional multivariate time series of the variable of interest in period _t_ , _t_ = 1, …, _T_ and _yt_<sup>(</sup><sup>_i_),</sup><sup>_i_= 1, …,</sup><sup>_N_, denote the</sup><sup>_i_th element of</sup><sup>**_y_**</sup><sup>_t_. In our</sup> empirical applications, _yt_<sup>(</sup><sup>_i_) represents the real housing</sup> growth rate/return at period _t_ for the cross- section unit (i.e., city or LGA) _i_ . It is computed from the prices _Pt_<sup>(</sup><sup>_i_) as fol-</sup> lows _yt_<sup>(</sup><sup>_i_)</sup> = 100 × ln ( _Pt_<sup>(</sup><sup>_i_)∕</sup><sup>_P_</sup> _t_<sup>(</sup> −<sup>_i_)</sup> 1<sup>).</sup> We use two univariate models as benchmarks to judge the performance of more complicated models against. The first one is the autoregressive (AR) model, defined as _p yt_<sup>(</sup><sup>_i_)</sup> = _휙_<sup>(</sup> 0<sup>_i_)+</sup> ∑ _휙_<sup>(</sup> _j_<sup>_i_)</sup> _yt_<sup>(</sup> −<sup>_i_)</sup> _j_<sup>+</sup><sup>_휀_</sup> _t_<sup>(</sup><sup>_i_),</sup> (1) _j_ = 1 while the second model is the autoregressive moving average (ARMA) model, given by _p q yt_<sup>(</sup><sup>_i_)</sup> = _휙_<sup>(</sup> 0<sup>_i_)+</sup> ∑ _휙_<sup>(</sup> _j_<sup>_i_)</sup> _yt_<sup>(</sup> −<sup>_i_)</sup> _j_<sup>+</sup> ∑ _휃_<sup>(</sup> _k_<sup>_i_)</sup><sup>_휀_(</sup> _t_ −<sup>_i_)</sup> _k_<sup>+</sup><sup>_휀_</sup> _t_<sup>(</sup><sup>_i_),</sup> (2) _j_ = 1 _k_ = 1 

where _휙_<sup>(</sup> _j_<sup>_i_) are the parameters of AR terms and</sup><sup>_휃_</sup> _k_<sup>(</sup><sup>_i_) are the pa-</sup> rameters of moving average (MA) terms. In particular, the AR(1) and ARMA(1,1) models have proven to be robust choices for predicting housing returns (Crawford and Fratantoni 2003; Rapach and Strauss 2009; Balcilar et al. 2015). It is important to highlight that the forecasting models mentioned above rely solely on the _i_ th element of **_y_** _t_ for predictions and do not take into account the influence of cross- market links represented by the other elements in **_y_** _t_ . 

The vector autoregressive (VAR) model is an extension of the univariate AR model and is commonly employed as a multivariate time series model in macroeconomics and finance. In contrast to the AR( _p_ ) model, the VAR( _p_ ) model allows for the incorporation of temporal interdependencies among the constituent time series in **_y_** _t_ . It is defined as 





<!-- Start of picture text -->
�<br>where  횽 0 = [ 휙 (1) 0 ,  휙 (2) 0 , …,  휙 ( 0 N ) ]  is an  N - dimensional inter-<br>cept vector allowing for nonzero means,  휺 t  represents an  N<br>- dimensional residual vector with nonsingular covariance ma-<br>�<br>trix  횺 휺 , and  Z t = [ y � t  − 1 ,  y � t  − 2 , …,  y t �  − p ]  is a  Np - dimensional<br>vector that contains all the lagged  y t .  횽 j  is a  N  ×  N  endogenous<br>parameter matrix at lag  j , j  = 1, 2, …,  p , defined as<br>⎡⎢ Φ (1) j ⎤⎥ ⎡⎢ 휙 (1) 1 j 휙 (1) 2 j ⋯ 휙 (1) Nj ⎤⎥<br>횽 j = ⎢⎢⎢⎢ Φ⋮ (2) j ⎥⎥⎥⎥ = ⎢⎢⎢⎢ 휙 ⋮ (2) 1 j 휙 (2) 2 j ⋱ 휙 ⋮ (2) Nj ⎥⎥⎥⎥, (5)<br>⎢⎣Φ ( j N ) ⎥⎦ ⎢⎣ 휙 ( 1 N j ) 휙 ( 2 N j ) ⋯ 휙 ( Nj N ) ⎥⎦<br>and  횽 = [ 횽 1,  횽 2, …,  횽 p ] is a  N  ×  Np  parameter matrix. While<br>the off- diagonal elements of  횽 j  are crucial for comprehending<br>the intertemporal connections within the data, the high level of<br>parameterization required can potentially hinder the practical<br>usefulness of the VAR model.<br>To isolate the effect of connectivity between the various com-<br>ponents of  y t , we break down the matrix  횽 j  into two parts:<br>횽 d j , which contains the diagonal elements of  횽 j  representing<br>the influence of each variable's own lagged information, and<br>횽 od j , which includes the off- diagonal elements that capture the<br>interactions between different elements in  y t . These matrices<br>are defined as follows:<br>⎡⎢ 휙 (1) 1 j 0 ⋯ 0 ⎤⎥ ⎡⎢ 0 휙 (1) 2 j ⋯ 휙 (1) Nj ⎤⎥<br>횽 d j = ⎢⎢⎢⎢ 0⋮ 휙 (2) 2 j ⋱ 0⋮ ⎥⎥⎥⎥ and  횽 od j = ⎢⎢⎢⎢ 휙 ⋮ (2) 1 j 0 ⋱ 휙 ⋮ (2) Nj ⎥⎥⎥⎥.<br>⎢⎣ 0 0 ⋯ 휙 ( Nj N ) ⎥⎦ ⎢⎣ 휙 ( 1 N j ) 휙 ( 2 N j ) ⋯ 0 ⎥⎦<br>By separating the diagonal and off- diagonal elements of  횽 j  as<br>above, the VAR( p ) model given in (3) can be decomposed as<br>p p<br>y t =  횽 0 + j ∑ = 1 횽 d j y t  − j + j ∑ = 1 횽 od j y t  − j +  휺 t . (6)<br>⏟⏞⏞⏞⏞⏟⏞⏞⏞⏞⏟ ⏟⏞⏞⏞⏞⏞⏟⏞⏞⏞⏞⏞⏟<br>Autoregressive Effects Connectivity Effects<br>This model specification shares similarities with the one ex-<br>plored in Zhu et al. (2017). In their study, Zhu et al. (2017) link<br>the intercepts to unit- specific (time- invariant) exogenous vari-<br>ables and assume that the system affects unit  i  through an aggre-<br>N<br>gated quantity defined as follows:  y ( t  − i ) j = n 1 i m ∑ = 1 wmj ( i ) y t (  − m ) j , where<br>w ( i )<br>sj  represents the connection strength between unit  m  and  i  at<br>period  t  − j  and assumed to be known and  ni = ∑ wsj ( i ).2 In con-<br>s  ≠ i<br>trast, we refrain from imposing those constraints on model co-<br>efficients to fully leverage the flexibility of VAR for forecasting.<br>Furthermore, we extend our model to include exogenous vari-<br>ables capturing observable unit- specific and common factors in<br>Section 4.1.<br><!-- End of picture text -->

3 

_Journal of Forecasting,_ 2026 

While VAR( _p_ ) model, as shown in equation (4), can be estimated through multivariate least squares in low- dimensional settings, that is, where the number of predictors is smaller than the time series length _T_ (Lütkepohl 2005), estimation becomes challenging in large- dimensional settings. This leads to the so- called “curse of dimensionality” which in the context of LDVAR models relates to a loss of degrees of freedom and poor forecasting performance caused by the large number of parameters to be estimated (De Mol et al. 2008). As demonstrated in Equation (5), the parameter space of VAR grows quadratically with the dimension of **_y_** _t_ and linearly with the VAR order, leading to a large number of parameters even for moderate dimensions. In such cases, standard estimation techniques like least squares become computationally infeasible. 

Various methods have been proposed in the literature to tackle the issue of high dimensionality in VAR models. These methods include reduced- rank techniques (Reinsel 1983; Ahn and Reinsel 1988; Carriero et al. 2011), factor models (Canova and Ciccarelli 2009; Stock and Watson 2016; Koop and Korobilis 2019), Bayesian methods (Karlsson 2013; Koop 2017; Koop and Korobilis 2016), and penalized estimation of sparse VAR (Wilms and Croux 2016; Davis et al. 2016; Smeekes and Wijler 2018; Camehl 2023). Among these methods, the penalized estimation approach has gained significant attention due to its ability to handle large- dimensional data and identify relevant predictors. In this study, we use the LASSO estimator introduced by Tibshirani (1996) to estimate the LDVAR model and uncover the underlying system structure. LASSO can handle a large number of predictors, produces sparse and interpretable models, and has been shown to have good forecasting performance in various applications. We have also explored the adaptive LASSO method introduced by Zou (2006). However, in our time series simulation settings, the LASSO estimator consistently outperformed the adaptive LASSO estimator. Therefore, we concentrate our discussion on the LASSO estimator and relegate the outcomes of utilizing the adaptive LASSO in the Appendix. The next subsection introduces the LASSO estimation method. 

## **2.2   |   LASSO Estimation** 

LASSO has been employed as a model selection device to maintain relevant variables while removing irrelevant predictors under various model specifications (Leeb and Pötscher 2005; Zhao and Yu 2006; Meinshausen and Bühlmann 2006; Bickel et al. 2009; Loh and Wainwright 2011; Masini et al. 2022; Masini et al. 2021). In particular, Nardi and Rinaldo (2011) showed its estimation, selection, and prediction consistency for AR models, while Loh and Wainwright (2011), Kock and Callot (2015) and Basu and Michailidis (2015). provided the nonasymptotic estimation and prediction error bounds and proved the estimation and prediction consistency for the LASSO in Gaussian VAR models. 

It is conventional to apply LASSO estimation equation by equation within the VAR system, as opposed to applying it to the entire system in one step (Kock and Callot 2015; Medeiros and Mendes 2016; Han and Tsay 2020; Masini et al. 2022). This technique has the potential to enhance estimation accuracy while reducing the dimensionality of the parameter space. We adhere 

to this established practice. To illustrate the mechanism of LASSO, we rewrite (4) for the unit _i_ as follows: 

**_y_**<sup>(</sup><sup>_i_)</sup> = **_휾_** _휙_<sup>(</sup> 0<sup>_i_)+</sup><sup>**_Z_횽**(</sup><sup>_i_) +</sup><sup>**_휺_**(</sup><sup>_i_).</sup> (7) � In this equation, **_y_**<sup>(</sup><sup>_i_)</sup> = [ _y_ 1<sup>(</sup><sup>_i_),</sup><sup>_y_</sup> 2<sup>(</sup><sup>_i_), …,</sup><sup>_y_</sup> _T_<sup>(</sup><sup>_i_)</sup> ] contains all the observations for _i_ th variable, **_휾_** is a _T_ - dimensional vector of one, � **횽**<sup>(</sup><sup>_i_)</sup> = [Φ<sup>(</sup> 1<sup>_i_), ⋯, Φ(</sup> _p_<sup>_i_)</sup> ] is a _Np_ - dimensional coefficient vector, **_Z_** = [ **_Z_** 1, ⋯ , **_Z_** _T_ ]<sup>�</sup> is of dimensions _T_ × _Np_ , and **_휺_**<sup>(</sup><sup>_i_)</sup> = [ _휀_<sup>(</sup> 1<sup>_i_), ⋯,</sup><sup>_휀_</sup> _T_<sup>(</sup><sup>_i_)]</sup> is a _T_ - dimensional vector of error terms. The number of parameters in the vector **횽**<sup>(</sup><sup>_i_)</sup> might significantly exceed the sample size, but only a subset of these parameters may actually be nonzero, resulting in a sparse true parameter vector denoted as **횽**<sup>∗(</sup><sup>_i_)</sup> . This means that the connectivity between the variable **_y_**<sup>(</sup><sup>_i_)</sup> and other variables **_y_**<sup>(</sup><sup>_j_)</sup> , where _j_ ≠ _i_ , may exist only between certain variables or at specific lags. In this scenario, applying LASSO becomes essential for selecting nonzero coefficients, effectively identifying the most relevant variables for each equation within the VAR model and enhancing forecasting accuracy. The LASSO estimator for Equation (7) is obtained by solving [ _휙_ (0 _i_ )<sup>,</sup><sup>**횽**</sup> ( _i_ )�<sup>]�</sup> = _argmin_ 21 _T_ ‖‖‖ **_y_** ( _i_ ) − **_휾_** _휙_ (0 _i_ )<sup>−</sup><sup>**_Z_횽**(</sup><sup>_i_)‖‖</sup> ‖2퓁2<sup>+</sup><sup>_휆_</sup> ‖<sup>‖‖</sup><sup>**횽**(</sup><sup>_i_)‖‖</sup> ‖퓁1<sup>,</sup> _휙_<sup>(</sup> 0<sup>_i_),</sup><sup>**횽**(</sup><sup>_i_)</sup> (8) _n n_ where ‖ _a_ ‖퓁1 = ∑ �� _ai_ �� and ‖ _a_ ‖퓁2 = ∑ _ai_<sup>2, respectively, denote</sup> _i_ = 1 ~~�~~ _i_ = 1 the 퓁1 and 퓁2 norms, for any vector _a_ ∈ ℝ<sup>_n_</sup> . Equation (8) can be regarded as a least squares objective function augmented with an additional term that penalizes coefficients in **횽**<sup>(</sup><sup>_i_)</sup> . Here, _휆_ is a nonnegative tuning parameter, which can be estimated through cross- validation or information criteria. The intercept _휙_<sup>(</sup> 0<sup>_i_) is not</sup> penalized and assumed to be nonsparse. Several papers have explored the nonasymptotic upper bounds for prediction and estimation errors of LASSO for the VAR model (3) under different model assumptions. Among them, _p_ Kock and Callot (2015) assumes that all roots of _IN_ − ∑ **횽** _jz_<sup>_j_��</sup> lie ����� _j_ = 1 ��� outside the unit circle and the error term _휀t_ follows an independent and identically distributed Gaussian distribution. On the other hand, Basu and Michailidis (2015) presents a more general assumption that allows both the predictors and the errors to be generated from stable Gaussian processes. Let _Si_ denote the set of nonzero parameters in the _i_<sup>_th_</sup> equation of the VAR system, _si_ its cardinality, and _휙_<sup>(</sup> min<sup>_i_)the minimum nonzero entry (in absolute</sup> value) of Φ<sup>∗(</sup><sup>_i_)</sup> . Additionally, define _휎_<sup>(</sup> _y_<sup>_i_) and</sup><sup>_휎_</sup> _휀_<sup>(</sup><sup>_i_) as the standard</sup> deviations of _yt_<sup>(</sup><sup>_i_) and</sup><sup>_휀_(</sup> _t_<sup>_i_), and let</sup><sup>_휅i_represent the restricted ei-</sup> genvalue of the population covariance matrix Γ = 피<sup>(</sup> _ZtZt_<sup>�</sup> ). It is assumed that _휅i_ is strictly positive, ensuring the sample Gram matrix _휓 T_ = _Z_<sup>�</sup> _Z_ ∕ _T_ approximates Γ.<sup>3</sup> 

Let _휎T_ = max1≤ _i_ ≤ _N_ ( _휎_<sup>(</sup> _y_<sup>_i_)∨</sup><sup>_휎_</sup> _휀_<sup>(</sup><sup>_i_)</sup> ), _휆T_ = ~~√~~ 8ln(1 + _T_ )<sup>5</sup> ln(1 + _N_ )<sup>4</sup> ln(1 + _p_ )<sup>2</sup> ln<sup>~~(~~</sup> _N_<sup>2</sup> _p_<sup>~~)~~</sup> _휎_<sup>4</sup> _T_<sup>∕</sup><sup>_T_,</sup> and 0 _< q <_ 1. Kock and Callot (2015) show that for all _i_ = 1, ⋯ , _N_ , 

4 

_Journal of Forecasting,_ 2026 

independence among observations (Kock and Callot 2015; Kock 2015; Kock ; Kock et al. 2020; Nicholson et al. 2017). However, recent studies have shown that 2020; Nicholson et al. 2017). However, recent studies have ; Nicholson et al. 2017). However, recent studies have shown that 2020; Nicholson et al. 2017). However, recent studies have ; Nicholson et al. 2017). However, recent studies have _K_ - fold cross- validation can be effective for autore-2017). However, recent studies have ). However, recent studies have gressive models, provided that the residuals are not highly cor-related (Bergmeir et al. 2018). As a result, it has been widely used in empirical studies (Nardi and Rinaldo 2011; Milunovich 2020a; 2018). As a result, it has been widely used ). As a result, it has been widely used 2011; Milunovich 2020a; ; Milunovich 2020a; 2020a; ; related (Bergmeir et al. 2018). As a result, it has been widely used in empirical studies (Nardi and Rinaldo 2011; Milunovich 2020a; 2018). As a result, it has been widely used ). As a result, it has been widely used 2011; Milunovich 2020a; ; Milunovich 2020a; 2020a; ; in empirical studies (Nardi and Rinaldo 2011; Milunovich 2020a; 2018). As a result, it has been widely used ). As a result, it has been widely used 2011; Milunovich 2020a; ; Milunovich 2020a; 2020a; ; Panagiotelis et al. 2019). To select the penalty parameter 2019). To select the penalty parameter ). To select the penalty parameter _휆_ in the LASSO implementation, we used the Panagiotelis et al. 2019). To select the penalty parameter 2019). To select the penalty parameter ). To select the penalty parameter `glmnet` package (Qian et al. 2013) and performed 10- fold cross- validation (i.e., 2013) and performed 10- fold cross- validation (i.e., ) and performed 10- fold cross- validation (i.e., _K_ = 10). 10).). 

with a probability of at least _p_<sup>∗</sup> = 1 − 2<sup>(</sup> _N_<sup>2</sup> _p_<sup>)1 −ln(1+</sup><sup>_T_)</sup> − 2(1 + _T_ )<sup>−1∕</sup><sup>_A_</sup> independence among observations (Kock and Callot 2015; Kock 2015; Kock ; Kock − _휋q_ ( _si_ ), we have et al. 2020; Nicholson et al. 2017). However, recent studies have shown that 2020; Nicholson et al. 2017). However, recent studies have ; Nicholson et al. 2017). However, recent studies have _K_ - fold cross- validation can be effective for autore-2017). However, recent studies have ). However, recent studies have _T_ 1 ‖‖‖‖ **_Z_ 횽** ( _i_ ) − **_Z_ 횽** ∗( _i_ )‖‖‖‖2퓁2 ≤ _q_<sup>16</sup> _휅_<sup>2</sup> _i si휆_<sup>2</sup> _T_<sup>,</sup> (9) gressive models, provided that the residuals are not highly cor-related (Bergmeir et al. 2018). As a result, it has been widely used in empirical studies (Nardi and Rinaldo 2011; Milunovich 2020a; 2018). As a result, it has been widely used ). As a result, it has been widely used 2011; Milunovich 2020a; ; Milunovich 2020a; 2020a; ; **횽** ( _i_ ) − **횽** ∗( _i_ ) ≤<sup>16</sup> _si휆T_ , (10) LASSO implementation, we used the Panagiotelis et al. 2019). To select the penalty parameter 2019). To select the penalty parameter ). To select the penalty parameter `glmnet` package (Qian _휆_ in the ‖‖‖‖ ‖‖‖‖퓁1 _q휅_<sup>2</sup> _i_ et al. 2013) and performed 10- fold cross- validation (i.e., 2013) and performed 10- fold cross- validation (i.e., ) and performed 10- fold cross- validation (i.e., _K_ = 10). 10).). where _휋q_ ( _si_ ) is a constant depending on _q_ and _si_ and _A_ is a positive constant. Moreover, with at least probability _p_<sup>∗</sup> , no relevant **2.3   |   Generating and Evaluating Forecasts** variables will be excluded from the equation if In this study, we adopt the direct forecasting method to compute _𝜙_<sup>(</sup> min<sup>_i_)</sup><sup>_>_16</sup> _si𝜆_<sup>2</sup> _T_<sup>.</sup> the _h_ - step- ahead predictions for all models. Direct forecasts are _q𝜅_<sup>2</sup> _i_ based on a horizon- specific estimation model, with the dependent Inequality (9) provides an upper bound on the prediction error, variable being the _h_ - step- ahead forecast value. Specifically, the while inequality (10) presents an upper bound for the param- _h_ - step- ahead direct forecast of VAR(( _p_ ) model model<sup>4</sup> is given as eter estimation error. The error bounds are influenced by the _p_ value of the restricted eigenvalue _휅i_ : The farther it is from zero, **_y_** _t_ + _h_ = **횽** 0( _h_ ) + ∑ **횽** _j_ ( _h_ ) **_y_** _t_ − _j_ +1, (14) the smaller the upper bounds become. On the other hand, the _j_ = 1 bounds increase with denser connections, represented by a � larger given probability, the minimum strength of the connection _si_ value. For a variable to be selected by LASSO with the _휙_<sup>(</sup> min<sup>_i_)</sup> where _�_ **_y_** _t_ + _h_ = [ _y_<sup>(1)</sup> _t_ + _h_<sup>,</sup><sup>_y_(2)</sup> _t_ + _h_<sup>, …,</sup><sup>_y_(</sup> _t_<sup>_N_</sup> + _h_<sup>)</sup> ] denotes the _N_ - dimensional _h_ must exceed 16 _si휆_<sup>2</sup> _T_<sup>∕(</sup><sup>_q휅_2</sup> _i_<sup>). The estimation and prediction consis-</sup> - step- ahead forecasts vector, **횽** 0( _h_ ) and **횽** _j_ ( _h_ ) are parameter estitency are achieved if _휆T_ → 0 as _T_ → ∞. mates from LASSO regression. The effectiveness of LASSO in variable selection depends Thus, to generate an _h_ - step- ahead out- of- sample forecast at on the careful choice of its tuning parameter, _휆_ , which ditime period _t_ , the parameter matrices **횽** 0( _h_ ), **횽** 1( _h_ ), …, **횽** _p_ ( _h_ ) rectly impacts the number of variables included in the model of Equation (14) are first estimated using _n_ most recent obserin finite sample. In this study, we adopt the coordinate devations spanning the interval [ _t_ − _n_ + 1, _t_ ]. Following this estiscent algorithm (Friedman et al. 2010) and employ _K_ - fold mation, a forecast _yt_ + _h_ is calculated by substituting the values cross- validation to select the optimal penalty parameters. of the lagged variables on the right- hand side of the equation, Specifically, considering Equation (7) as an example, we parwhich are known at time _t_ . For example, in generating a onetition the data set [ **_y_** ( _i_ ), **_Z_** ] into _K_ disjoint subsets along the step- ahead forecast ( _h_ = 1) using a VAR(1) model ( _p_ = 1), the time dimension, denoted as _J_ =<sup>[</sup> _J_ 1, _J_ 2, …, _JK_ ]. During each prediction would be as follows: cross- validation run, we use one of these subsets, say _Jk_ (with _k_ = 1, 2, …, _K_ ), as the validation set and the remaining subsets, **_y_** _t_ +1 = **횽** 0(1) + **횽** 1(1) **_y_** _t_ . (15) that is, _Jk_ − = ∪ _j_ ≠ _kJj_ , for model fitting. Let Λ be the sets of all possible values of _휆_ . For each _휆_ ∈Λ, the prediction error over the test set _Jk_ is An alternative forecasting technique often encountered in the literature is the recursive approach where forecasts are gener( _i_ )<sup>**횽**</sup> ( _i_ ) 2 ated by iteratively applying a one- step- ahead model for _h_ periods. PE<sup>(</sup> _휆_ , _Jk_ ) = **_y_**<sup>(</sup><sup>_i_)</sup> − **_휾_** _̂ 휙_ 0<sup>(</sup><sup>_휆_,</sup><sup>_Jk_−) −</sup><sup>**_Z_**</sup> _휆_<sup>(</sup><sup>_휆_,</sup><sup>_Jk_−)‖‖</sup> . (11) While direct forecasts are generally considered to be more ro‖‖‖‖ ‖‖퓁2 bust to misspecifications, the evidence regarding which method In this equation, _̂휙_ (0 _i_ )<sup>(</sup><sup>_휆_,</sup><sup>_Jk_−) and</sup><sup>**횽**</sup> ( _휆i_ )<sup>(</sup><sup>_휆_,</sup><sup>_Jk_−) are the LASSO es-</sup> Sorjamaa et al. is superior is mixed (Marcellino et al. 2007). We favor the direct forecasting approach 2006; Pesaran et al. 2011; timators obtained from set _Jk_ − with penalty parameter _휆_ , while because it eliminates the need to forecast the exogenous varithe 퓁2 norm is computed for the subset _Jk_ . The _K_ - fold crossables used in our empirical analysis. validation error for each _휆_ ∈Λ is then computed as _K_ When comparing forecasts from multiple models, their rankings CV( _휆_ ) = ∑ PE<sup>(</sup> _휆_ , _Jk_ ), (12) are determined by the loss function, which measures the dis-tance between the forecasted value and the actual value. In this _k_ = 1 paper, we use the squared forecast error (SFE) defined as and the tuning parameter _휆_ is solved by 2 _휆_ = argmin CV( _휆_ ). (13) SFE: _Lt_<sup>(</sup><sup>_i_</sup> +<sup>)</sup> _h_<sup>=</sup> ( _y_<sup>(</sup> _t_<sup>_i_</sup> +<sup>)</sup> _h_<sup>−</sup><sup>_y_</sup> _t_<sup>(</sup> +<sup>_i_)</sup> _h_ ) . (16) _휆_ ∈Λ Ranking the computed loss measures can help distinguish beThere has been a debate on the applicability of cross- validation tween competing models. However, the rankings may vary to dependent time series data, as the procedure assumes depending on the data sets used, and hence, it is important to 

In this study, we adopt the direct forecasting method to compute the _h_ - step- ahead predictions for all models. Direct forecasts are based on a horizon- specific estimation model, with the dependent variable being the _h_ - step- ahead forecast value. Specifically, the _h_ - step- ahead direct forecast of VAR(( _p_ ) model model<sup>4</sup> is given as 

Ranking the computed loss measures can help distinguish between competing models. However, the rankings may vary depending on the data sets used, and hence, it is important to 

5 

_Journal of Forecasting,_ 2026 

investigate the statistical significance of the loss differentials. Multiple statistical tests have been developed in the literature in the last three decades. The Diebold and Mariano (1995, DM) test has incontestably been the most commonly used among many early research works, which provides an approach to test for equal predictive ability (EPA). It has been applied widely to compare the accuracy of forecasting models, even though the DM test was not originally designed for model comparison (Diebold 2015). Several extensions and modifications centered around the DM test have been introduced later on (West 1996; Harvey et al. 1998; Clark and McCracken 2001, 2009; Giacomini and White 2006; White 2000; Hansen 2005). 

This paper employs the MCS procedure developed by Hansen et al. (2011) to evaluate the performance of multiple forecasting models. The MCS approach provides a set of models that are deemed to be statistically equivalent in terms of forecasting performance, at a given level of confidence. This is achieved by comparing standardized loss differentials, that is, loss differences scaled by their sampling variability, between pairs of models through a sequence of tests. In essence, the MCS allows for the identification of best performing models within a set, while also acknowledging the uncertainty associated with model selection. Given a full set of competing models ℳ =<sup>[</sup> ℳ1, …, ℳ _m_ ], the pair- wise loss differentials between models ℳ _j_ and ℳ _k_ , _j_ ≠ _k_ , for forecasting _yt_<sup>(</sup> +<sup>_i_)</sup> _h_<sup>are calculated as</sup> 



The null hypothesis of EPA is given by 



If _H_ 0 is rejected at the significance level _훼_ using the _Tmax_ statistic of Hansen et al. (2011), the underperforming model will be removed and the process will continue until nonrejection occurs, leading to a set of surviving models that are statistically equivalent. 

## **2.4   |   Robustness Analysis** 

We evaluate the robustness of our study by incorporating exogenous variables, using alternative evaluation metrics and applying a alternative strategy for constructing MCSs. 

### **2.4.1** | **Accounting for Exogenous Macroeconomic Variables** 

First, we consider the inclusion of macroeconomic variables in the forecasting models. The univariate AR model with exogenous variables is commonly referred as the “ARX“ model, while the multivariate VAR specification that includes exogenous variables is known as the “VARX” model. We can easily extend the AR equation for each variable given in (1) as follows: 

where **_x_** _t_ is an _M_ - dimensional vector of exogenous variables at time _t_ and Λ<sup>(</sup><sup>_i_)</sup> _s_<sup>are the corresponding parameter vectors. The ex-</sup> tended model is referred to as ARX( _p_ , _k_ ). If we incorporate these exogenous variables into the VAR( _p_ ) model in Equation (4), we can similarly obtain the VARX( _p_ , _k_ ) model, which is expressed as follows: 



<!-- Start of picture text -->
p k<br>y t =  횽 0 + ∑ 횽 j y t  − j  + ∑ 횲 s x t  − s  +  휺 t . (20)<br>j  = 1 s  = 1<br><!-- End of picture text -->

### **2.4.2** | **Absolute Forecast Error** 

It is well- known that the SFE loss, as defined in (16), is sensitive to outliers. An alternative loss function which weighs small and large forecast errors equally is the absolute forecast error (AFE) given by 



### **2.4.3** | **Conditional Superior Predictive Ability (CSPA)** 

The CSPA test, as outlined by Li et al. (2022), posits that the benchmark predictive model's conditional expected loss should be as good as or better than that of any rival models across all conditioning states. This test accounts for heterogeneity across sample periods, such as housing market expansion or collapsing, thereby taking the state of the market into consideration when evaluating forecasting performances. The null hypothesis of the CSPA test involves the loss differential _d_<sup>(</sup><sup>_i_)</sup> _t_ + _h_ , _jk_<sup>between the bench-</sup> mark model _k_ and the competing model _j_ defined in Equation (17) as follows: 



where 풲 _t_ + _h_ is a conditioning variable. We form the confidence set for the most superior (CSMS) by rotating the benchmark role across all models, comprising all nonrejected benchmarks. 

## **2.5   |   Simulation Study** 

We perform simulation experiments calibrated to the results of our empirical study in order to explore the impact of different levels of system sparsity and connectivity strength on forecast accuracy. Our analysis utilizes a VAR(1) framework for its simplicity and also due to its effectiveness on our actual data. We formulate our Data Generating Process (DGP) as follows: 



We assume that **_휺_** _t_ is a martingale difference sequence, and all eigenvalues of **횽** 1 have modulus less than one. These assumptions result in a weakly stationary process and are commonly found in similar studies. The matrix **횽** 0 is set equal to the intercept obtained from a VAR(1) model estimated for the first 30 LGAs (in the order listed in Appendix A2) within the Sydney region from August 2005 to February 2022. Σ **_휺_** is diagonal and contains values obtained from the same estimation. 

_p k yt_<sup>(</sup><sup>_i_)</sup> = _휙_<sup>(</sup> 0<sup>_i_)+</sup> ∑ _휙_<sup>(</sup> _j_<sup>_i_)</sup> _yt_<sup>(</sup> −<sup>_i_)</sup> _j_<sup>+</sup> ∑ Λ<sup>(</sup> _s_<sup>_i_)</sup><sup>**_x_**</sup><sup>_t_−</sup><sup>_s_+</sup><sup>_휀_(</sup> _t_<sup>_i_),</sup> (19) _j_ = 1 _s_ = 1 

6 

_Journal of Forecasting,_ 2026 

The elements of **횽** 1 control the levels of sparsity and connectivity strength and are also calibrated to the results of our empirical results as detailed in Section 5.1. 

Having described the DGP, we next enumerate the steps of our simulation study. As can be seen, Step 1 involves generating the data from the DGP, while Steps 2 and 3 closely mimic our empirical methodology to generate the forecasts and compute MCSs. Finally, Step 4 averages the results across all replications, allowing us to assess the effectiveness of the competing models on the synthetic data. 

- Step 1: Simulate the dataset **_y_**<sup>(</sup> _t_<sup>_b_),</sup><sup>_b_= 1, …,</sup><sup>_B_using the DGP</sup> from (23) for each considered value of **횽** 1. The number of simulations is set to _B_ = 300. 

- Step 2: Calculate the _h_ - step- ahead out- of- sample predictions for **_y_**<sup>(</sup> _t_<sup>_b_) using a number of different forecasting models.</sup> The forecasts are computed based on a rolling window forecasting scheme with the estimation window size _t_ 0 set to 70% of the dataset. 

- Step 3: Let _yt_<sup>(</sup><sup>_i_</sup> +<sup>,</sup><sup>_b_</sup> _h_<sup>,</sup><sup>_m_)</sup> , _t_ = _t_ 0, …, _T_ , be the forecast from model _m_ for the _i_ th variable of **_y_**<sup>(</sup> _t_<sup>_b_</sup> +<sup>)</sup> _h_<sup>. We first compute the forecast</sup> loss _Lt_<sup>(</sup><sup>_i_</sup> +<sup>,</sup><sup>_b_</sup> _h_<sup>,</sup><sup>_m_)</sup> for all models and then implement the MCS test in order to obtain a set of “superior” models at a given confidence level, which we set to 90%. 

- Step 4: Given the MCS test results for all the simulated data, we compute the average proportion of time that a model _m_ has been included in a MCS across all variables and replications 



where 

- 핀<sup>(</sup> _m_<sup>_i_,</sup><sup>_b_)</sup> = 1, if model _m_ is in a MCS for the _i_ th variable in the _b_ th replication 

- {0, otherwise. 

## **3   |   Data and Empirical Study** 

In this section, we forecast disaggregated house price growth rates from three housing markets, namely, within- city house price growth rate for Sydney and Melbourne (Australia) and city- level house price growth rates from China. We evaluate out- of- sample predictions generated by our LDVAR models, which incorporate price interconnectedness, and compare their predictive performance against univariate models which ignore regional linkages. 

## **3.1   |   Data** 

For the Australian markets, we use monthly house prices at the LGA level for Sydney and Melbourne from August 2005 to February 2022. As the two largest cities in Australia and the respective capitals of New South Wales and Victoria, Sydney and 

Melbourne represent the most prominent housing markets in the Australian economy. The LGAs, which encompass areas greater than a single suburb but smaller than a capital city, constitute the lowest tier of government in Australia. Consistent with Hurn et al. (2022), our analysis encompasses 32 LGAs for Sydney and 31 LGAs for Melbourne, which are listed in Table A2. The house price data are obtained from the CoreLogic RP database of the Securities Industry Research Centre of Asia- Pacific (SIRCA) and are adjusted for inflation using the CPI (excluding shelter) obtained from the Australian Bureau of Statistics. 

Regarding the Chinese market, we use monthly city- level house price indices which have been compiled by Fang et al. (2016). The sample period used in the empirical analysis is January 2003 to March 2013. The conversion of nominal prices to real prices is performed using the city- level urban consumer price indices obtained from the China Statistical Yearbook. A comprehensive list of the 88 cities included in this study, comprising of 4 Tier 1, 26 Tier 2, and 58 Tier 3 cities, is presented in Table A3 of Appendix A2. 

While our housing price series are available monthly, the CPI data we collected are at the quarterly frequency. To synchronize these series and compute real house prices, we convert both the Australian and Chinese price indices from quarterly to monthly frequency via linear interpolation as in Hurn et al. (2022) and Sekine and Tsuruga (2018). Thus, our subsequent analysis is conducted on real house price series that are derived by this method. Figure 1 depicts the natural logarithm of real house prices in the Australian and Chinese markets, accompanied by the average autocorrelation function (ACF) for the log growth rates. We make three key observations here. 

First, as evident by the time series plots for the LGA house price indices in Sydney and Melbourne, there are strong cyclical comovements within these two cities. Given the narrower spread (variability) in the first plot, it appears that the interconnectedness is somewhat stronger within the Sydney region. Concerning the plot for the city- level house prices in the Chinese market, we observe an overall upward pattern over the time period of investigation but also a substantial amount of noise. 

Second, we note that our sample period includes several crises that could have led to instability in the data- generating process (DGP). For instance, the Australian data sample extends from August 2005 to February 2022. As such, it includes the Global Financial Crisis (2007–2008), the European Debt Crisis (2010– 2013), and the recent COVID- 19 pandemic period (2020). Some of the effects of those events are observable in Figure 1, where they correspond with the house prices in Sydney and Melbourne exhibiting local troughs and a tighter grouping of the log price series. To account for this observation, we apply the rolling window estimation technique which excludes relatively “old” data points from the estimation dataset and uses only the most recent subset of observations to estimate the parameters. This method helps prevent the contamination of model forecasts with outdated information, thereby reducing the likelihood of biased forecasts.<sup>5</sup> 

Our third observation is regarding the average ACFs computed for the house price growth rates and presented in the second column of Figure 1. Here, we note substantially more 

7 

_Journal of Forecasting,_ 2026 



<!-- Start of picture text -->
1 0.6<br>0.8<br>0.4<br>0.6<br>0.4<br>0.2<br>0.2<br>0<br>0<br>-0.2<br>-0.4 -0.2<br>2006 2008 2010 2012 2014 2016 2018 2020 2022 0 10 20 30 40 50<br>1 0.6<br>0.8<br>0.4<br>0.6<br>0.4 0.2<br>0.2<br>0<br>0<br>-0.2 -0.2<br>2006 2008 2010 2012 2014 2016 2018 2020 2022 0 10 20 30 40 50<br>2 0.3<br>1.5<br>0.2<br>1<br>0.1<br>0.5<br>0<br>0<br>-0.5<br>-0.1<br>-1<br>-1.5 -0.2<br>2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 0 10 20 30 40 50<br><!-- End of picture text -->

**FIGURE 1** |    The left panel shows the time series plot of logarithmic real monthly house prices for the Australian and Chinese markets, spanning the period August 2005 to February 2022 for the Australian market and January 2003 to March 2013 for the Chinese market. The right panel displays the averaged ACF computed on log growth rates (returns). The analysis includes data from 32 LGAs in Sydney, 31 LGAs in Melbourne, and 88 cities in China, with each line representing one LGA or city. 

persistence in the monthly data for Sydney and Melbourne LGAs relative to the Chinese data. This is indicative of more complex and richer dynamics in the house return returns for the LGAs in Sydney and Melbourne, relative to the series for the Chinese cities. 

Based on the above discussion, we can hypothesize that the LGA housing markets within Sydney and Melbourne exhibit more connections (i.e., less sparsity) which are of greater magnitude (i.e., connectivity strength) relative to the Chinese city- level markets. This hypothesis is partly supported by the findings of Hurn et al. (2022), which indicate that by 2017, approximately 50% of all possible interconnections within both 

the Sydney and Melbourne housing markets were active. In contrast, the Chinese housing market had only 20% active connections in 2013—significantly lower to the figures recorded in Australia. These differences may impact the accuracy and usefulness of the multivariate LDVAR models used in our subsequent analysis. 

## **3.2   |   Results: Out- of- Sample Forecasting** 

In this section, we consider price connectedness from two perspectives. First, we evaluate whether incorporating connectedness through LDVAR models enhances house price forecasts 

8 

_Journal of Forecasting,_ 2026 

compared to univariate models that do not account for connectedness. Second, we investigate the degree of connectedness captured in the estimated models for each of the three housing markets under investigation. We treat each of the three housing markets as a separate system and perform rolling window estimation of the LDVAR model by applying the LASSO method, as outlined in Section 2.2. In addition to three LDVAR models (with 1, 2, and 3 lag terms, respectively), we also produce forecasts from three AR specifications and the ARMA(1,1) model. These univariate models do not account for the interconnectedness of house prices and are used to evaluate whether incorporating this interconnectedness can improve out- of- sample forecasts. 

The estimation (training) of the models is performed on 70 % of the available data, which translates into a window size of 138 observations for Sydney and Melbourne markets and 85 data points for the Chinese markets. Forecasts are then constructed for 1- , 3- , 6- and 12- month ahead periods and evaluated on independent test data. This provides us with (i) sixty 1- month ahead forecasts for each LGA in the Sydney and Melbourne markets and 37 predictions for each city in China, (ii) 58 and 35 respective forecasts for 3- month ahead, (iii) 55 and 32 predictions for 6- month ahead predictions, and finally, (iv) forty- nine and twenty- six 12- month ahead forecasts, respectively. For each rolling window estimation, out- of- sample forecast errors are computed and the MCS procedure performed, that is, see (18) to obtain the best model set for each LGA or city at the given forecasting horizon. We then calculate the frequency that a particular model is in the set of best performing models for each market and present these figures in Table 1. Note that the MCS may include several models so that the sum of the frequencies across each row in Table 1 can easily exceed one. 

Focusing on the Sydney and Melbourne markets, multivariate models clearly outperform the univariate specifications at all forecasting horizons. The only exception is in the case of the 12- month ahead forecast for Melbourne when the AR(1) slightly outperforms. The VAR(1) model performs particularly well at 1- month ahead forecasting and is present in all computed MCSs, as indicated by the selection frequency of 100%. In contrast, AR(1) which is the simplest of the models applied here, is in the MCS only 43. 8 % and 29. 0 % of the time for the Sydney and Melbourne markets. 

For the Chinese market, the AR(1) specification performs better at all horizons except the 12- month ahead forecast, when the VAR(1) model marginally outperforms (63.6% versus 61.4%). These findings are in line with the initial observations about the time series plots for the three markets provided above. These results are also consistent with our simulations discussed in Section 5, where we report that LDVAR models forecast better in relatively dense systems with strong connectivity, while univariate models tend to outperform in sparse systems with weak connectivity strengths. 

After evaluating how accounting for connectedness impacts forecasting performance in Table 1, we now turn our attention to assess the degree of connectedness in the estimated equations. As previously discussed, we characterize connectedness with the sparsity and connectivity strength of the lagged parameter matrices. Figures 2 and 3 summarize this information by showing the average selection frequencies for each regional unit within the three housing markets and the magnitudes of the estimated parameters. These values are calculated from VAR(1) models used for one- step- ahead predictions, as described in (15). 

**TABLE 1** |    Out- of- sample results for the Australian and Chinese housing markets at various forecasting horizons based on 90% MCS test results. 

||**AR(1)**|**AR(2)**|**AR(3)**|**ARMA(1, 1)**|**VAR(1)**|**VAR(2)**|**VAR(3)**|
|---|---|---|---|---|---|---|---|
|Sydney||||||||
|_h_=1|43.8|50.0|40.6|50.0|**100.0**|81.3|78.1|
|_h_=3|68.8|78.1|78.1|59.4|**87.5**|**87.5**|87.5|
|_h_=6|65.6|56.3|56.3|78.1|**84.4**|56.3|56.3|
|_h_=12|68.8|59.4|40.6|78.1|75.0|**81.3**|71.9|
|Melbourne||||||||
|_h_=1|29.0|38.7|38.7|38.7|**100.0**|58.1|61.3|
|_h_=3|71.0|77.4|71.0|51.6|80.6|87.1|**93.5**|
|_h_=6|77.4|67.7|61.3|77.4|**93.5**|90.3|71.0|
|_h_=12|**83.9**|80.6|80.6|77.4|67.7|80.6|80.6|
|China||||||||
|_h_=1|**83.0**|62.5|51.1|63.6|55.7|44.3|42.0|
|_h_=3|**75.0**|65.9|62.5|64.8|60.2|54.5|58.0|
|_h_=6|**73.9**|61.4|56.8|65.9|61.4|52.3|53.4|
|_h_=12|61.4|56.8|44.3|60.2|**63.6**|55.7|55.7|



_Note:_ The table displays the percentage of inclusion of each competing model in the MCSs, which are based on the SFE loss function. 

9 

_Journal of Forecasting,_ 2026 



<!-- Start of picture text -->
LGA 1 Average = 0.310 LGA 1<br>0.35<br>LGA 11<br>LGA 11<br>0.3<br>LGA 21<br>LGA 21<br>0.25<br>LGA 32<br>LGA 32<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 LGA 1 LGA 11 LGA 21 LGA 32 0.2<br>LGA 1<br>LGA 1<br>0.15<br>LGA 11 LGA 11<br>0.1<br>LGA 21 LGA 21<br>0.05<br>LGA 31 Average = 0.413 LGA 31 0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 LGA 1 LGA 11 LGA 21 LGA 31<br><!-- End of picture text -->

**FIGURE 2** |    Average connection frequency and average parameter strength in the VAR(1) model ( _h_ = 1) for the Australian markets. The figure displays the average selection frequency and the heat map of the average estimated parameter strength across the rolling window for the Australian market in the VAR(1) model for the 1- month ahead forecast. 



<!-- Start of picture text -->
City 1 City 1<br>0.45<br>0.4<br>City 22 City 22 0.35<br>0.3<br>0.25<br>City 44 City 44<br>0.2<br>0.15<br>City 66 City 66<br>0.1<br>0.05<br>Average = 0.106<br>City 88 City 88 0<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 Cyti 1 Cyti 22 Cyti 44 City 66 City 88<br><!-- End of picture text -->

**FIGURE 3** |    Averaged parameter connection frequency and averaged parameter strength in the VAR(1) model ( _h_ = 1) for the Chinese market. The figure displays the averaged selection frequency and the heat map of the average estimated parameter strength across the rolling window for the Chinese market in the VAR(1) model for the one- step- ahead forecast. 

10 

_Journal of Forecasting,_ 2026 

Average selection frequencies represent the proportion of time an LGA/city plays a role in forecasting 1- month ahead house price in all other LGAs/cities within their region. They are calculated as the frequencies of relevant nonzero coefficients estimated by the LASSO technique and are indicative of the level of sparsity in the estimated parameter matrix. The averaged percentages (across all rolling windows) are displayed in the left panel of Figures 2 and 3. In general, all LGAs/cities have been selected as relevant predictors by LASSO, albeit some areas are selected more often than others. The averaged selection frequencies range between 10. 7 % and 60. 2 % for different LGAs in Sydney, 23. 1 % and 65. 8 % for Melbourne, and 5 % and 25 % for the cities in China. The higher the average selection frequency, the lower the sparsity of the lagged parameter matrix. Thus, the housing markets in Sydney and Melbourne appear to be more densely connected compared to the Chinese markets, with the mean link being 31. 0 % (41. 3 %) for Sydney (Melbourne) and only 10. 6 % for China. This result is consistent with the evidence provided in Hurn et al. (2022), who use a different method to conclude that within- city housing networks in Sydney and Melbourne are more interconnected than those found in the cross- city housing markets of China. 

Plots illustrating the magnitudes of the estimated lagged coefficients, which indicate our second measure of connectedness—connectivity strength—are provided in the right columns of Figures 2 and 3. These values are calculated by averaging the estimated VAR parameters for each pair of LGAs (cities) across the rolling window estimations, resulting in total 726 and 793 links in Sydney and Melbourne, respectively, and 4251 connection links for China. The computed average strengths range between 0.00 and 0.32 for Sydney, 0.00 and 0.37 for Melbourne, and between 0.00 and 0.45 for China. The minimum and maximum average connection strengths discussed above, however, do not fully capture the distribution of these strengths within each market. To gain a better understanding of the estimated connectivity strengths, it is useful to calculate the frequencies with which the estimated linkages fall into weak, moderate, and strong ranges. For this purpose, we define the weak range of connectedness to be the [ − 0. 05, 0. 05] interval and find that 75. 9 % , 71. 6 %, and 92. 1 % of the links for Sydney, Melbourne, and China, respectively, are weak. In the moderate range of links, as given by the parameter interval [ − 0. 15, − 0. 05] ∪[0. 05, 0. 15], we find 17. 5 % , 21. 7 %, and 7. 3 % of connections for Sydney, Melbourne, and China, respectively. Finally, in the range of strong connections (less than − 0. 15 or greater than 0.15), we have 6. 6 % , 6. 7 %, and 0. 7 % of the connections within the same three regions. Thus, we observe that housing markets for Sydney and Melbourne exhibit higher frequencies of moderate and strong connectivity strengths relative to the Chinese housing network. 

In summary, our results presented here show that not only Sydney and Melbourne markets are more densely connected (exhibit less sparsity in the lagged LDVAR parameter matrix), but that they also have higher proportions of moderate/strong connections relative to the Chinese markets. This may explain why the LDVAR model is preferred for forecasting in the Sydney and Melbourne LGA markets, while the univariate AR specification is more suitable for predicting house price returns in 

Chinese city markets, even though all three markets exhibit a degree of within- market interconnectedness. However, we will defer making this conclusion until we present the results of our simulation study in Section 5. 

## **4   |   Robustness Analysis** 

In the previous section, we provide results derived from a pure LDVAR model, that is, without taking into account any exogenous variables. However, given that house prices are influenced by key macroeconomic factors, it is worth exploring if including such factors can affect our results and how. In this section, we conduct a number of sensitivity checks and demonstrate that our results are robust to (i) the inclusion of macroeconomic variables in the forecasting models, (ii) the use of alternative loss functions, and (iii) the use of an alternative test that considers the prevailing state of the market to evaluate the relative predictive capabilities of various models. 

## **4.1   |   Predictive Models With Exogenous Macroeconomic Variables** 

A number of studies have shown that incorporating exogenous macroeconomic variables such as interest rates and unemployment figures into housing price forecasting models can increase their accuracy; see, for example, Rapach and Strauss (2007) and Bork and Müller (2018). In this section, we expand on both the AR and VAR models by integrating a set of exogenous variables as described in (19) and (20) to assess whether our previously reported findings are sensitive to the introduction of exogenous predictors. 

Table 2 presents the lists of exogenous variables included in the models for the two Australian city markets and the Chinese housing market, which are provided in the top and bottom panels, respectively. As shown in the table, we include a variety of both national and regional/local variables that may be useful in predicting disaggregated house price growth rates. Nearly all of the included variables, or their variations, appear in the list of predictors considered in the existing literature, including studies such as Rapach and Strauss (2007, 2009), Gupta (2013), and Shi and Phillips (2023). As noted in the third column, these variables are collected at monthly, quarterly, and annual frequencies. In order to synchronize their values with the house prices, we convert all variables to monthly frequency using linear interpolation. This is further discussed in the Data Section (Section 3.1). 

All variables are expressed in real terms, except for the credit supply growth rate in the Australian market and the M2 money supply growth rate in the Chinese market. Regarding these nominal variables, empirical research has now shown that changes in nominal prices can influence and help predict real house prices. Studies that utilize inflation to model real house prices and growth rates include Rapach and Strauss (2007, 2009); Plakandaras et al. (2015) for the US market, Abelson et al. (2005); Milunovich (2020a) for Australia, and Stevenson (2000) for the United Kingdom, among others. In addition to inflation, it is also important to account for the stance of macroprudential regulation in Australia—a policy implemented by the Australian Prudential Regulation 

11 

_Journal of Forecasting,_ 2026 

**TABLE 2** |    List of macroeconomic variables included in models (19) and (20) for the empirical analysis. 

|**Macroeconomic variable**|**Source**|**Frequency**|**Area**|
|---|---|---|---|
|Australian market||||
|Real mortgage rate|RBA|Monthly|National|
|Credit supply growth Rate|RBA|Monthly|National|
|10- year to 3- month bond spread|RBA|Monthly|National|
|Population growth rate|ABS|Quarterly|State|
|Unemployment growth rate|ABS|Monthly|State|
|Housing completion growth rate|ABS|Quarterly|State|
|Real state final demand growth rate|ABS|Quarterly|State|
|Real house rental growth rate|SIRCA|Monthly|LGA|
|House listing growth rate|SIRCA|Monthly|LGA|
|Chinese market||||
|Real interest rate|FRED database|Monthly|National|
|M2 money supply growth rate|FRED database|Monthly|National|
|Real GDP per capital growth rate|China City Statistical Yearbook|Yearly|City|
|Population growth rate|China City Statistical Yearbook|Yearly|City|
|Unemployment growth rate|China City Statistical Yearbook|Yearly|City|



_Note:_ This table provides a list of the macroeconomic variables used in the empirical analysis of the Australian and Chinese markets. Note that annually and quarterly frequency data are converted to monthly frequency via linear interpolation. 

**TABLE 3** |    MCS results for the ARX( _p_ , _k_ ) and VARX( _p_ , _k_ ) models, _p_ = 1, 2, 3 and _k_ = 6, for the Australian and Chinese housing markets. 

||**ARX(1)**|**ARX(2)**|**ARX(3)**|**VARX(1)**|**VARX(2)**|**VARX(3)**|
|---|---|---|---|---|---|---|
|Sydney|||||||
|_h_=1|21.9|37.5|40.6|**93.8**|65.6|59.4|
|_h_=3|46.9|71.9|71.9|59.4|59.4|**78.1**|
|_h_=6|65.6|68.8|53.1|68.8|68.8|**84.4**|
|_h_=12|84.4|81.3|59.4|78.1|78.1|**87.5**|
|Melbourne|||||||
|_h_=1|25.8|54.8|51.6|**90.3**|77.4|77.4|
|_h_=3|45.2|64.5|67.7|74.2|71.0|**93.5**|
|_h_=6|51.6|51.6|45.2|71.0|**96.8**|93.5|
|_h_=12|87.1|74.2|77.4|74.2|80.6|**90.3**|
|China|||||||
|_h_=1|**77.3**|62.5|51.1|62.5|50.0|59.1|
|_h_=3|76.1|60.2|58.0|64.8|**77.3**|67.0|
|_h_=6|70.5|59.1|61.4|69.3|69.3|**71.6**|
|_h_=12|**69.3**|56.8|47.7|**69.3**|67.0|63.6|



_Note:_ The table displays the percentage of time each model is included in the 90% MCS based on the SFE loss. The maximum value among all the competing models is highlighted in boldface. 

Authority (APRA) through adjustments to lending conditions. APRA has actively used credit controls to influence housing market outcomes. For example, in December 2014, APRA 

introduced a 10% annual growth cap on investor housing credit for banks, which had a significant impact on housing demand and, consequently, prices. In our predictive models, 

12 

_Journal of Forecasting,_ 2026 

the effects of inflation and credit conditions on the housing market are jointly captured through the variable representing the nominal credit supply growth rate. 

In this robustness check, we maintain a fixed lag order of _k_ = 6 for the exogenous variables in all models. The lag order for the macroeconomic variables is based on the understanding that 

**TABLE 4** |    Out- of- sample forecasting results for the Australian and Chinese housing markets at different forecasting horizons based on 90% MCS test results with the AFE loss function. 

||**AR(1)**|**AR(2)**|**AR(3)**|**ARMA(1, 1)**|**VAR(1)**|**VAR(2)**|**VAR(3)**|
|---|---|---|---|---|---|---|---|
|Sydney||||||||
|_h_=1|40.6|56.3|50.0|59.4|**93.8**|71.9|78.1|
|_h_=3|53.1|53.1|53.1|34.4|**84.4**|75.0|65.6|
|_h_=6|65.6|65.6|53.1|78.1|**84.4**|62.5|71.9|
|_h_=12|71.9|62.5|53.1|68.8|71.9|**78.1**|**78.1**|
|Melbourne||||||||
|_h_=1|41.9|51.6|38.7|58.1|**96.8**|77.4|74.2|
|_h_=3|64.5|71.0|67.7|54.8|71.0|83.9|**90.3**|
|_h_=6|74.2|61.3|54.8|67.7|**90.3**|80.6|61.3|
|_h_=12|**90.3**|80.6|67.7|77.4|74.2|83.9|87.1|
|China||||||||
|_h_=1|**88.6**|71.6|61.4|62.5|62.5|47.7|50.0|
|_h_=3|**73.9**|64.8|62.5|58.0|64.8|63.6|56.8|
|_h_=6|**75.0**|63.6|55.7|68.2|56.8|64.8|59.1|
|_h_=12|**70.5**|62.5|45.5|64.8|65.9|61.4|56.8|



_Note:_ The table displays the percent of the time that each model is included in the 90% MCSc under the AFE loss function. The maximum value among all the competing models is highlighted in boldface. **TABLE 5** |    Out- of- sample forecasting results for the Australian and Chinese housing markets based on the 90% CSPA test and the SFE loss function. 

||**AR(1)**|**AR(2)**|**AR(3)**|**ARMA(1, 1)**|**VAR(1)**|**VAR(2)**|**VAR(3)**|
|---|---|---|---|---|---|---|---|
|Sydney||||||||
|_h_=1|40.6|59.4|56.3|50.0|**93.8**|78.1|81.3|
|_h_=3|43.8|68.8|**71.9**|56.3|**71.9**|68.8|68.8|
|_h_=6|50.0|53.1|46.9|56.3|**78.1**|43.8|53.1|
|_h_=12|25.0|37.5|25.0|50.0|81.3|**90.6**|68.8|
|Melbourne||||||||
|_h_=1|25.8|51.6|58.1|64.5|93.5|93.5|**96.8**|
|_h_=3|29.0|58.1|41.9|35.5|71.0|**90.3**|**90.3**|
|_h_=6|32.3|32.3|29.0|25.8|**93.5**|80.6|80.6|
|_h_=12|54.8|38.7|22.6|41.9|51.6|83.9|**90.3**|
|China||||||||
|_h_=1|**78.4**|67.0|61.4|71.6|69.3|67.0|60.2|
|_h_=3|70.5|69.3|69.3|67.0|**72.7**|**72.7**|**72.7**|
|_h_=6|75.0|**77.3**|71.6|70.5|73.9|68.2|65.9|
|_h_=12|**71.6**|69.3|60.2|68.2|70.5|70.5|60.2|



_Note:_ The table displays the percentage of the time that each model is included in the 90% CSPA- based most superior confidence set under the SFE loss. The maximum value among all the competing models is highlighted in boldface. 

13 

_Journal of Forecasting,_ 2026 

housing markets may react to economic factors with some delay. Here, we follow the literature to incorporate six lags of macroeconomic variables which account for the lagged effects of the economic variables for up to two quarters as in Dungey and Pagan (2009) and Robstad (2018). 

at all forecasting horizons. For the Chinese city markets, the ARX(1) model performs better in the immediate 1- month ahead and ranks equally with VARX(1) at the 12- month ahead forecast. The multivariate models perform better at the 3- and 6- month ahead forecasts. 

Following the inclusion of the exogenous variables in the expanded information set, we recompute the MCS and provide a ranking of our models. Table 3 shows that the MCS results are broadly consistent with those from Table 1, where we do not include any exogenous variables. For the Sydney and Melbourne markets, multivariate models outperform univariate models 

## **4.2   |   Absolute Forecast Errors** 

Here we re- evaluate real housing returns predictions using the AFE loss provided in (21), rerank the forecasting models accordingly, and present our new results in Table 4 below. 





















**FIGURE 4** |    The heat map of parameter matrices for the VAR(1) model constructed under different connection strengths and sparsity levels. The connection strengths are classified into three categories: Weak, Moderate, and Strong where the degree of shading represents the magnitude of the coefficients, with darker colors indicating larger magnitudes. The sparsity levels range from 90% to 40%. 

14 

_Journal of Forecasting,_ 2026 

Overall, we observe a pattern that is similar to what we have in Table 1. Namely, multivariate LDVAR models appear most appropriate for forecasting LGA house price returns in the Sydney and Melbourne markets, while for the Chinese citylevel series, the univariate AR(1) specification is included in the MCS most often. Additionally, there is a decrease in the frequency of LDVAR models being selected in the MCS, relative to the SFE results; however, this reduction is only marginal. The only exception is the 12- month ahead forecast for the Chinese housing markets where there is a reversal in the best ranking model in favor of AR(1). To summarize, we can conclude that our model rankings are relatively robust to the application of alternative loss functions as demonstrated using the AFE loss. 

## **4.3   |   CSPA Test** 

Next, we examine the sensitivity of our results to the MCS procedure by employing a different statistical test that evaluates the predictive capabilities of our models based on conditional expected loss, as outlined in Equation (22). The chosen conditioning variables for the Sydney and Melbourne markets are the first principal components of the price–rent ratios across their respective LGAs, which reflect the overall states of each market. Since the rent data are not available for the Chinese market, we use income data to replace the rent, leading to the price–income ratio. Thus, the conditioning variable for the Chinese market is the first principal component of the price– income ratio. Those measures are often used to evaluate housing affordability and have been employed to identify housing bubbles (see, for example, Shi et al. 2020; Chen et al. 2022; Shi and Phillips 2023). 

Table 5 shows the forecasting performance using the CSPA test. In general, our results for the Sydney and Melbourne housing markets remain unchanged, except that AR(3) in Sydney is now as good as the VAR(1) model for the 3- month ahead forecast. Concerning the Chinese market, our results are again qualitatively consistent with our previous findings with the univariate models outperforming the multivariate specifications, except at the 3- month ahead forecasting horizon. 

## **5   |   Simulation Study** 

Given our empirical results, it remains uncertain what conditions of within- market connectedness, as captured by LDVAR systems, lead to improved forecast accuracy compared to univariate models. The LASSO estimation technique functions as a variable selection device, eliminating zero- value coefficients and retaining only those parameters that are nonzero. As nonzero coefficients represent interrelationships among variables, LASSO estimation is an effective method for identifying such connections in a large- dimensional setting. Yet, the upper bound of the forecast error of the VAR system increases with the number of nonzero coefficients and diminishes with restricted eigenvalue, as given in Equation (9). In this section, we explore how different levels of sparsity and connectivity strength impact out- of- sample prediction accuracy by conducting simulation experiments under a range of connectivity scenarios. 

## **5.1   |   Generating the Data** 

We simulate data using the model described in Equation (23). The dimension of the multiple time series **_y_** _t_ is set to 30, that is, _N_ = 30, which is close to the number of LGAs in Sydney and Melbourne. The length of the simulated time series is set to 250, that is, _T_ = 250, equivalent to approximately 20 years of monthly data. Given that this simulation study explores the effects of sparsity and connectivity strength on the forecasting performance, special attention needs to be given to the construction of the parameter matrix **횽** 1. Sparsity pertains to the proportion of zero parameters in a matrix; that is, a sparsity of 90% implies that 90% of all matrix elements are zeros, whereas connectivity strength relates to the magnitude of the off- diagonal parameters. To investigate these effects, we construct nine parameter matrices with varying levels of sparsity and strength. 

We explore three tiers of connectivity strength—weak, moderate, and strong—each accompanied by varying degrees of sparsity (90%, 70%, and 40% for weak and moderate and 90%, 70%, and 55% for strong).<sup>6</sup> Since the diagonal elements of **횽** 1 do not play a role in our definition of connectivity 

**TABLE 6** |    Summary statistics of simulated datasets under varying strength and sparsity settings. 

|**Strength**|**Sparsity**|**_흁_**|**_흈_**|**_max_(****_흍T_)**|**_L_1**|**_L_5**|**_L_10**|
|---|---|---|---|---|---|---|---|
|Weak|90%|0.001|0.009|0.275|0.012|- 0.005|- 0.004|
||70%|0.001|0.009|0.269|0.011|- 0.005|- 0.004|
||40%|0.001|0.009|0.287|0.011|- 0.004|- 0.004|
|Moderate|90%|0.001|0.009|0.304|0.013|- 0.005|- 0.004|
||70%|0.001|0.010|0.402|0.012|- 0.004|- 0.004|
||40%|0.001|0.010|0.512|0.016|- 0.001|- 0.004|
|Strong|90%|0.001|0.010|0.523|0.022|- 0.002|- 0.005|
||70%|0.000|0.014|0.880|0.071|0.037|0.018|
||55%|0.001|0.023|0.951|0.079|- 0.015|0.058|



_Note:_ The table displays the mean ( _휇_ ), standard deviation ( _휎_ ), and the maximum eigenvalue ( _max_ ( _휓 T_ )) of **횽** 1 for the simulated data. Additionally, the averaged autocorrelation function (ACF) at Lags 1, 5, and 10 is also reported. 

15 

_Journal of Forecasting,_ 2026 

**TABLE 7** |    The averaged percentage of one model being included in a 90% MCS at different forecasting horizons, built on the SFE loss function. 

|||**Uni**|**variate**|**Multiv**|**ariate**|
|---|---|---|---|---|---|
|**Strength**|**Sparsity**|**AR(1)**|**ARMA(1,1)**|**VAR(1)**|**VAR(2)**|
|_h_=1||||||
|Weak|90%|**86.8**|77.4|75.5|74.4|
||70%|**87.3**|77.7|77.1|74.9|
||40%|**87.5**|77.6|77.5|74.6|
|Moderate|90%|**84.4**|75.0|79.9|74.7|
||70%|77.9|69.3|**86.8**|74.6|
||40%|60.6|55.2|**93.9**|71.7|
|Strong|90%|37.5|33.5|**93.6**|74.7|
||70%|0.9|0.8|**97.6**|59.4|
||55%|0.0|0.0|**99.5**|35.3|
|_h_=3||||||
|Weak|90%|**83.5**|77.4|83.2|82.0|
||70%|82.4|77.6|**84.7**|82.8|
||40%|83.5|77.6|**83.9**|82.7|
|Moderate|90%|83.3|77.8|**83.5**|82.1|
||70%|82.5|77.4|**83.7**|82.4|
||40%|83.0|77.5|**83.5**|81.4|
|Strong|90%|83.0|77.2|**84.0**|81.7|
||70%|56.9|53.8|**91.8**|76.3|
||55%|2.5|2.4|**98.3**|55.8|
|_h_=6||||||
|Weak|90%|**83.3**|78.5|82.6|81.3|
||70%|82.6|78.8|**83.2**|81.7|
||40%|82.9|77.9|**83.7**|82.0|
|Moderate|90%|**82.5**|78.3|81.8|81.0|
||70%|82.8|79.0|**83.4**|82.7|
||40%|83.9|78.8|**84.4**|82.3|
|Strong|90%|**83.0**|78.4|82.8|82.2|
||70%|81.0|76.8|**83.3**|80.4|
||55%|37.6|36.1|**95.3**|72.2|
|_h_=12||||||
|Weak|90%|**84.5**|79.4|82.4|80.8|
||70%|**83.3**|80.1|82.5|81.0|
||40%|**82.9**|79.4|82.7|81.1|
|Moderate|90%|**83.9**|79.4|82.6|81.4|
||70%|**83.5**|79.2|82.2|81.3|
||40%|**82.9**|79.4|82.8|81.3|



(Continues) 

16 

_Journal of Forecasting,_ 2026 

**TABLE 7** |    (Continued) 

|||**Un**|**ivariate**|**Multiv**|**ariate**|
|---|---|---|---|---|---|
|**Strength**|**Sparsity**|**AR(1)**|**ARMA(1,1)**|**VAR(1)**|**VAR(2)**|
|Strong|90%|**84.0**|80.0|82.6|80.9|
||70%|**82.7**|78.7|81.7|80.2|
||55%|75.8|73.3|**84.3**|83.1|



_Note:_ The percentage is calculated based on the 300 replications. The result in boldface indicates the maximum value among all the competing models. 



<!-- Start of picture text -->
2 2 2<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7 8 9 10 7 8 9 10 7.5 8 8.5 9 9.5<br>2 2 2<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>8 8.5 9 9.5 10 8 9 10 11 8 9 10 11 12<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>8 9 10 11 12 10 15 20 25 10 20 30 40 50 60 70<br><!-- End of picture text -->

**FIGURE 5** |    The kernel density plots show distributions of the MSFEs of the AR(1) and VAR(1) models across 300 simulations at a 1- step- ahead horizon under varying connection strengths and sparsity levels. The VAR(1) model is estimated using LASSO. 

strength, they are set to the values of the first 30 LGAs in the estimated Sydney VAR system from the entire sample period in all simulations. These values range from − 0. 275 to 0.263, with an average value of 0.0154. The parameter values for the nonzero off- diagonal entries are randomly drawn from a uniform distribution within three interval ranges. For the weak connectivity strength, the interval is [ − 0. 05, 0. 05], while for the moderate and strong connectivity strengths, the parameter ranges are [ − 0. 15, − 0. 05] ∪[0. 05, 0. 15] and [ − 0. 35, − 0. 15] ∪[0. 15, 0. 35], respectively. Finally, the nonzero parameters are randomly distributed across the 

matrix **횽** 1. Figure 4 provides a visual illustration of the nine parameter matrices constructed for three levels of connectivity strength and three levels of sparsity. 

For each of the nine constructed parameter matrices, we perform 300 simulations resulting in a total of 2700 simulated datasets. Table 6 provides the summary statistics for these datasets. As illustrated by the first two columns in the table, the mean of the simulated series are small and close to zero, while the standard deviations range from about 9 to 23 times the size of the mean values. The magnitude of the standard deviations increases with 

17 

_Journal of Forecasting,_ 2026 

the level of connectivity strength. We also observe how the maximum eigenvalue of the coefficient matrix **횽** 1 increases with connectivity strength but is inversely related to sparsity. When the connectivity is weak or moderate, the system tends to be stable regardless of the sparsity level. However, when the connectivity strength is high, then low levels of sparsity result in unstable systems with maximum eigenvalues approaching the value of one. 

Finally, the last three columns of Table 6 display the average autocorrelation coefficients for the simulated series. We can see that the autocorrelation coefficients at lag one are positively linked to the level of connectivity strength and negatively related to sparsity. Furthermore, at longer time lags, that is, 5 and 10, the average autocorrelations are mostly negligable, except for some cases of high connectivity and low sparsity. 

## **5.2   |   Simulation Results** 

Table 7 presents the frequencies of model inclusion _f m_ based on the out- of- sample results obtained using the SFE loss function. These are computed using the simulation algorithm outlined in Section 2.5. In addition, the results for the absolute forecast error (AFE) loss function can be found in Table A1 in Appendix 

A1. As indicated across the top row of the table, the forecasting models evaluated comprise AR(1), ARMA(1, 1), VAR(1), and VAR(2) specifications. The LDVAR models are estimated via LASSO, as described in Section 2.2. Figures 5–8 depict the estimated kernel densities of mean squared forecast errors (MSFEs, across 300 replications) for two superior forecasting models at various forecasting horizons. We also perform the forecasting exercise using the adaptive LASSO method for LDVAR. Our results reveal that the conventional LASSO outperforms the adaptive version in this study. For a more detailed discussion, refer to Appendix A2. 

The findings presented in the top panel of Table 7 and Figure 5 demonstrate the importance of connectivity strength for shortterm multivariate forecasting. When the connectivity strength is weak, we observe that all VAR- type models underperform the simple AR(1) model, irrespective of the level of sparsity in the lagged parameter matrix. In particular, the MCS results indicate that in over 85% of the simulations with weak connectivity strength, the AR(1) model is found in the set of “superior” forecasting models, whereas the percentage for the VAR(1) model is about 75%. Therefore, weak connectivity, as represented by small off- diagonal elements in the parameter matrix **횽** 1 of (23), results in estimation errors that offset the advantages 



<!-- Start of picture text -->
2 2 2<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7 8 9 10 8 8.5 9 9.5 10 8 8.5 9 9.5 10<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>8 8.5 9 9.5 10 8 9 10 11 8 9 10 11 12<br>1.5 0.5 0.25<br>0.4 0.2<br>1<br>0.3 0.15<br>0.2 0.1<br>0.5<br>0.1 0.05<br>0 0 0<br>9 10 11 12 16 18 20 22 24 26 20 40 60 80<br><!-- End of picture text -->

**FIGURE 6** |    The kernel density plot compares the MSFEs of the AR(1) and VAR(1) models across 300 simulations at a three- step- ahead horizon under varying connection strengths and sparsity levels. 

18 

_Journal of Forecasting,_ 2026 



<!-- Start of picture text -->
2 2 2<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7 8 9 10 7.5 8 8.5 9 9.5 10 7.5 8 8.5 9 9.5 10<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7.5 8 8.5 9 9.5 10 8 9 10 11 8 9 10 11 12<br>1.5 0.3 0.1<br>0.25<br>0.08<br>1 0.2<br>0.06<br>0.15<br>0.04<br>0.5 0.1<br>0.02<br>0.05<br>0 0 0<br>9 10 11 12 15 20 25 30 20 40 60 80 100<br><!-- End of picture text -->

**FIGURE 7** |    The kernel density plot compares the MSFEs of the AR(1) and VAR(1) models across 300 simulations at a six- step- ahead horizon under varying connection strengths and sparsity levels. 

of accounting for interconnectedness between the forecasted variables. 

As the connectivity strength increases to moderate and strong levels, the VAR(1) model starts to exhibit forecasting advantage. Furthermore, lower levels of sparsity are associated with stronger performance of the VAR(1) model. For the sparsity levels of 70% and 40% (55%) for moderate (strong) connectivity, the averaged inclusion proportion of the VAR(1) model (i.e., _f m_ as defined in (2.5)) reaches between 87% and 100%. The percentage for univariate models gradually decreases and eventually reaches 0% under strong connectivity strength and 55% sparsity settings. These patterns are further illustrated in Figure 5. The first row of the figures illustrates the outperformance of AR(1) for weak connectivity, while the second potion of the figure demonstrates moderate and strong levels of connectivity when VAR(1) gains forecasting advantage. The columns of the figure suggest that as sparsity declines, that is, more series are interconnected, the multivariate model produces forecasting gains (except in the case when such connections are small in magnitude). 

The forecasting results at midterm prediction horizons exhibit a similar pattern to those of short- term, as presented in the 

middle section of Table 7. Although the VAR(1) model with LASSO regression outperforms the AR(1) for _h_ = 3, 6 when the sparsity levels are 70% and 40% for moderate (strong) connectivity, the differences between the two models are relatively small for all three connectivity strengths. This is also illustrated in Figures 6 and 7, where the estimated MSFE densities are very similar except in the case of strong connectivity and low sparsity. In fact, when the connectivity is strong reducing the level of sparsity in the parameter matrix, **횽** 1 increases the outperformance of the multivariate model relative to the AR(1) specification. On the other hand, when the parameter matrix is sparse enough (i.e., very few linkages exist between the variables), the univariate model provides better predictions. 

At longer forecasting horizons, conditional predictions approach their unconditional values. We see that when _h_ = 12, the AR(1) model ranks better than VAR(1). This trend is evident from the bottom panel of Table 7, which shows that the AR(1) model consistently outperforms the VAR(1) model in terms of forecasting performance, irrespective of the connectivity strength and connectivity level. An exception to this trend is apparent in the case of strong connectivity strength and 55% sparsity, as depicted in Figure 8. However, it should be noted that the performance of 

19 

_Journal of Forecasting,_ 2026 



<!-- Start of picture text -->
2 2 2<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7 8 9 10 7.5 8 8.5 9 9.5 10 7.5 8 8.5 9 9.5 10<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7.5 8 8.5 9 9.5 10 8 9 10 11 8 9 10 11 12<br>1.2 0.3 0.06<br>1 0.25 0.05<br>0.8 0.2 0.04<br>0.6 0.15 0.03<br>0.4 0.1 0.02<br>0.2 0.05 0.01<br>0 0 0<br>9 10 11 12 15 20 25 30 20 40 60 80 100<br><!-- End of picture text -->

**FIGURE 8** |    The kernel density plot compares the MSFEs of the AR(1) and VAR(1) models across 300 simulations at a 12- step- ahead horizon under varying connection strengths and sparsity levels. 

the VAR(1) model with LASSO is only marginally inferior to that of the AR(1) specification and maintains its stability across all forecast horizons. 

In summary, the simulation study provides evidence that both connectivity strength and the level of sparsity have a significant impact on the forecasting performance of the VAR models estimated using LASSO, particularly in short- and midterm forecast horizon scenarios. Nevertheless, the results suggest that connectivity strength appears to exert a greater influence on the forecasting ability than sparsity. These findings can provide valuable insight into forecasting applications where innterconnectedness between relevant factors needs to be accounted for and especially in large- dimensional systems where both connectivity strength and sparsity need to be considered. 

## **6   |   Conclusion** 

Forecasting house prices is essential for informed decision making in real estate investment, mortgage lending, and policy formulation. Accurate predictions aid homebuyers and sellers in making optimal financial choices, while policymakers rely on 

such forecasts to develop housing policies that address affordability and market stability. 

In this paper, we investigate the efficacy of incorporating connectivity information to accurately forecast housing price growth rates. We employ an LDVAR model to forecast the growth rate of house prices in a given area, leveraging its historical data and considering all conceivable interactions with other regions within the system. This framework is also be extended to incorporate exogenous predictors. The large dimensional model is estimated using shrinkage techniques, and its predictive capability is compared to that of widely recognized benchmark models for predicting house prices, i.e., AR(1) and ARMA(1,1). Given that we model connectedness using LDVAR specifications, we also examine the relationship between the degree of connectedness captured by the models and their predictive accuracy. More specifically, we characterize connectedness by sparsity and connectendess strength. We define sparsity by the ratio of zero elements in the parameter matrices, while connectivity strength is measured by the magnitude of the lagged coefficients. While the statistical characteristics of the LASSO estimators for LDVAR models have been studied, systematic investigations of their out- of- sample forecasting performance and its relationship with the underlying interdependency structure 

20 

_Journal of Forecasting,_ 2026 

are limited. To address this gap, we conduct a simulation study that investigates the impact of sparsity and connectivity strength on the forecasting efficacy of LDVAR models. 

We consider three housing market systems (within- city areas for Sydney and Melbourne and the city- level markets for China) and conduct rolling window forecasts for each LGA and city within the systems. Our forecasting exercises reveal that the multivariate LDVAR models outperform univariate forecasting specifications when forecasting LGA- level house prices within Sydney and Melbourne. In the case of Chinese city house price returns, univariate AR models consistently outperform the LDVAR specification. Upon closer inspection of the estimated LDVAR parameter matrices, we find that within- city housing markets in Sydney and Melbourne are more densely and strongly connected, whereas the links among Chinese cities are sparse and weak. We conduct a series of robustness analyses to confirm the stability of our empirical findings. These checks include examining the impact of alternative loss functions, considering the inclusion of macroeconomic variables, and computing MCSs using an alternative procedure. The results of these tests support and reinforce our main findings. This raises the question about the role that sparsity and connectivity strength play in forecasting applications of large- dimensional systems and under what configurations of these two parameters can within- system interconnectness lead to forecasting gains. We address this issue by conducting simulation experiments calibrated to reflect the linkages estimated from the data. 

The simulation study reveals that the forecasting performance of LDVAR specifications is significantly influenced by both the sparsity of the parameter matrices and the connectivity strength of the system. Interestingly, univariate models, which disregard connectivity information, demonstrate strong performance in cases where interconnectedness exists, but the connections are sparse and weak. On the other hand, in the presence of strong connections, incorporating information about interdependencies via LDVAR models becomes important for improving out- ofsample forecasts. In addition, the significance of such relationships is particularly evident when making shorter term forecasts. As the forecast horizon extends to longer periods, the impact of cross- market connectivity gradually diminishes. When the connectivity strength is moderate, connection information proves to be considerably beneficial for short- term forecasts and denser coefficient matrices, but its impact is somewhat diminished for longer forecasting horizons. The effect of sparsity in the LDVAR parameter matrices follows a pattern where the performance of multivariate forecasting models improves, relative to univariate specifications, when the sparsity is low, and vice versa. This effect however is conditional on the connectivity strength, so that when connectivity is weak univariate models outperform at all levels of sparsity considered here. The simulation results are robust to the choice of loss functions (squared and absolute forecast errors) and estimation techniques (LASSO and adaptive LASSO). 

Concerning the implications of our study and recommendations, we make the following points. Our results suggest that identifying connectivity within a system does not guarantee improved forecasting performance when detected connections are incorporated into predictive models. Instead, any potential gains in forecasting accuracy depend on the degree of 

sparsity and the strength of connectedness within the system. This issue is especially challenging because the sparsity and connectivity strength, which are critical for choosing the right modeling approach, are usually not known before fitting the model. Thus, our recommendation is to acknowledge the potential differences in each housing network and adopt a flexible modeling strategy that involves testing various models and basing decisions on out- of- sample results. Additionally, we recommend that forecasters strive to understand why their chosen model performs best in terms of sparsity and connectivity strength. This insight can guide the ongoing evaluation and adjustments to the model. 

Finally, we note some limitations of our study and propose directions for future research. Specifically, we use large- dimensional linear models estimated with shrinkage methods to capture the connectedness within systems of disaggregated house prices. While we account for potential nonlinearity through the use of a rolling window algorithm in forecasting, an alternative approach would be to explicitly incorporate nonlinearity into the model specification, either through a large- dimensional timevarying coefficient network as in Chen et al. (2025) or via a more general nonparametric model estimated using popular machine learning algorithms such as random forests. We leave a systematic comparison between our modeling strategy, and these alternative approaches to future research. 

#### **Acknowledgments** 

The authors acknowledge research support from the Australian Research Council (project no. DP190102049). Open access publishing facilitated by Macquarie University, as part of the Wiley - Macquarie University agreement via the Council of Australian University Librarians. 

#### **Conflicts of Interest** 

The authors declare no conflicts of interest. 

#### **Data Availability Statement** 

The data that support the findings of this study are available from the corresponding author upon reasonable request. 

#### **Endnotes** 

- <sup>1</sup> The LGAs consist of areas greater than a single suburb and represent the lowest tier of government in Australia. 

- <sup>2</sup> In Zhu et al. (2017), the authors investigate conditions to ensure the strict stationarity of the model and develop an ordinary least squarestype estimator for the model coefficients. 

> <sup>3</sup> The restricted eigenvalue condition required imposes a lower bound on the minimum eigenvalue of matrix Γ subject to some restrictions on the eigenvectors. It ensures that the predictor variables exhibit sufficient variability and separation, preventing severe multicollinearity and enhancing the stability of the LASSO estimates. When _Np > T_ , the sample Gram matrix is singular and the restricted eigenvalue equals zero. 

> <sup>4</sup> We have chosen to focus on the VAR( _p_ ) model as an example due to its simplicity, as generalizing to more complex models such as VARX( _p_ , _k_ ) and ARMA- type models is straightforward. 

- <sup>5</sup> An alternative approach to recursive estimation is to use the expanding window estimation. However, this method puts equal weight on all observations from the beginning of the sample to the point of the 

21 

_Journal of Forecasting,_ 2026 

forecast, which can lead to biased forecasts when model instability is a concern. Furthermore, in Hansen et al. (2011), rolling window estimation is adopted in the forecasting application to satisfy the stationarity assumptions required by the MCS bootstrap, while recursive or expanding window results are reported only as supplementary pseudoMCS evidence. Therefore, we employ the rolling window estimation technique, and while expanding window estimation may also be of interest, we leave this approach to future research. 

- <sup>6</sup> Initially, we additionally examined a 40% sparsity for strong connectivity. However, even with all eigenvalues below one, the resulting data showed traits resembling nonstationary patterns, which is not surprising given findings in Bauwens et al. (2023). Consequently, the minimum sparsity for strong connectivity was adjusted to 55%. 

- <sup>7</sup> If the LASSO estimator in the initial regression classifies a parameter as zero, then it is not included in the second step of the adaptive LASSO, resulting in a smaller optimization problem. This can lead to computational efficiency and improved accuracy in estimating the nonzero parameters. 

#### **References** 

Abelson, P., R. Joyeux, G. Milunovich, and D. Chung. 2005. “Explaining House Prices in Australia: 1970–2003.” _Economic Record_ 81: S96–S103. 

Abraham, J. M., and P. H. Hendershott. 1996. “Bubbles in Metropolitan Housing Markets.” _Journal of Housing Research_ 7, no. 2: 191. 

Ahn, S. K., and G. C. Reinsel. 1988. “Nested Reduced- Rank Autogressive Models for Multiple Time Series.” _Journal of the American Statistical Association_ 83, no. 403: 849. 

Antonakakis, N., I. Chatziantoniou, C. Floros, and D. Gabauer. 2018. “The Dynamic Connectedness of UK Regional Property Returns.” _Urban Studies_ 55, no. 14: 3110–3134. 

Balcilar, M., R. Gupta, and S. M. Miller. 2015. “The Out- of- Sample Forecasting Performance of Nonlinear Models of Regional Housing Prices in the US.” _Applied Economics_ 47, no. 22: 2259–2277. 

Balcilar, M., O. Usman, M. Yulek, B. Agan, and B. Erdal (2022). “House Price Dynamics and Consumer Sentiment in an Era of Destabilizing Macroeconomic Conditions: Empirical Evidence From Türkiye.” _Available at SSRN 4311520_ . 

Barigozzi, M., and C. Brownlees. 2019. “Nets: Network Estimation for Time Series.” _Journal of Applied Econometrics_ 34, no. 3: 347–364. 

Basu, S., and G. Michailidis. 2015. “Regularized Estimation in Sparse High- Dimensional Time Series Models.” _Annals of Statistics_ 43, no. 4: 1535–1567. 

Bauwens, L., G. Chevillon, and S. Laurent. 2023. “We Modeled Long Memory With Just One Lag!” _Journal of Econometrics_ 236, no. 1: 105467. 

Bergmeir, C., R. J. Hyndman, and B. Koo. 2018. “A Note on the Validity of Cross- Validation for Evaluating Autoregressive Time Series Prediction.” _Computational Statistics & Data Analysis_ 120: 70–83. 

Bickel, P. J., Y. Ritov, and A. B. Tsybakov. 2009. “Simultaneous Analysis of Lasso and Dantzig Selector.” _Annals of Statistics_ 37, no. 4: 1705–1732. 

Bork, L., and S. V. Müller. 2018. “Housing Price Forecastability: A Factor Analysis.” _Real Estate Economics_ 46, no. 3: 582–611. 

Camehl, A. 2023. “Penalized Estimation of Panel Vector Autoregressive Models: A Panel Lasso Approach.” _International Journal of Forecasting_ 39, no. 3: 1185–1204. 

Campbell, J. Y., and J. F. Cocco. 2007. “How Do House Prices Affect Consumption? Evidence From Micro Data.” _Journal of Monetary Economics_ 54, no. 3: 591–621. 

Canova, F., and M. Ciccarelli. 2009. “Estimating Multicountry VAR Models.” _International Economic Review_ 50, no. 3: 929–959. 

Carleton, L., R. Joyeux, and G. Milunovich. 2022. “Rail Stations and Residential Sorting: The Case of Sydney Metropolitan Area.” _Urban Studies_ 59, no. 15: 3132–3149. 

Carriero, A., G. Kapetanios, and M. Marcellino. 2011. “Forecasting Large Datasets With Bayesian Reduced Rank Multivariate Models.” _Journal of Applied Econometrics_ 26, no. 5: 735–761. 

Case, K. E., J. M. Quigley, and R. J. Shiller. 2005. “Comparing Wealth Effects: The Stock Market Versus the Housing Market.” _Topics in Macroeconomics_ 5, no. 1: 20121001. https:// doi. org/ 10. 2202/ 1534- 6013. 1235. 

Case, K. E., and R. J. Shiller. 1989. “The Efficiency of the Market for Single- Family Homes.” _American Economic Review_ 79, no. 1: 125–137. 

Case, K. E., and R. J. Shiller. 1990. “Forecasting Prices and Excess Returns in the Housing Market.” _Real Estate Economics_ 18, no. 3: 253–273. 

Chen, J., D. Li, Y.- N. Li, and O. Linton. 2025. “Estimating Time- Varying Networks for High- Dimensional Time Series.” _Journal of Econometrics_ 249: 105941. 

Chen, Y., P. C. Phillips, and S. Shi. 2022. “Common Bubble Detection in Large Dimensional Financial Systems.” _Journal of Financial Econometrics_ 21, no. 4: nbab027. 

Chinco, A., A. D. Clark- Joseph, and M. Ye. 2019. “Sparse Signals in the Cross- Section of Returns.” _Journal of Finance_ 74, no. 1: 449–492. 

Cho, M. 1996. “House Price Dynamics: A Survey of Theoretical and Empirical Issues.” _Journal of Housing Research_ 7, no. 2: 145–172. 

Clark, T. E., and M. W. McCracken. 2001. “Tests of Equal Forecast Accuracy and Encompassing for Nested Models.” _Journal of Econometrics_ 105, no. 1: 85–110. 

Clark, T. E., and M. W. McCracken. 2009. “Tests of Equal Predictive Ability With Real- Time Data.” _Journal of Business & Economic Statistics_ 27, no. 4: 441–454. 

Cotter, J., S. Gabriel, and R. Roll. 2015. “Can Housing Risk Be Diversified? A Cautionary Tale From the Housing Boom and Bust.” _Review of Financial Studies_ 28, no. 3: 913–936. 

Crawford, G. W., and M. C. Fratantoni. 2003. “Assessing the Forecasting Performance of Regime- Switching, Arima and Garch Models of House Prices.” _Real Estate Economics_ 31, no. 2: 223–243. 

Davis, R. A., P. Zang, and T. Zheng. 2016. “Sparse Vector Autoregressive Modeling.” _Journal of Computational and Graphical Statistics_ 25, no. 4: 1077–1096. 

De Mol, C., D. Giannone, and L. Reichlin. 2008. “Forecasting Using a Large Number of Predictors: Is Bayesian Shrinkage a Valid Alternative to Principal Components?” _Journal of Econometrics_ 146, no. 2: 318–328. 

DeFusco, A., W. Ding, F. Ferreira, and J. Gyourko. 2018. “The Role of Price Spillovers in the American Housing Boom.” _Journal of Urban Economics_ 108: 72–84. 

Diebold, F. X. 2015. “Comparing Predictive Accuracy, Twenty Years Later: A Personal Perspective on the Use and Abuse of Diebold– Mariano Tests.” _Journal of Business & Economic Statistics_ 33, no. 1: 1–1. 

Diebold, F. X., and R. S. Mariano. 1995. “Comparing Predictive Accuracy.” _Journal of Business & Economic Statistics_ 13, no. 3: 253–263. 

Duca, J. V., J. Muellbauer, and A. Murphy. 2021. “What Drives House Price Cycles? International Experience and Policy Issues.” _Journal of Economic Literature_ 59, no. 3: 773–864. 

Dungey, M., and A. Pagan. 2009. “Extending a SVAR Model of the Australian Economy.” _Economic Record_ 85, no. 268: 1–20. 

22 

_Journal of Forecasting,_ 2026 

Ellington, M., X. Fu, and Y. Zhu. 2023. “Real Estate Illiquidity and Returns: A Time- Varying Regional Perspective.” _International Journal of Forecasting_ 39, no. 1: 58–72. 

Fang, H., Q. Gu, W. Xiong, and L.- A. Zhou. 2016. “Demystifying the Chinese Housing Boom.” _NBER Macroeconomics Annual_ 30, no. 1: 105–166. 

Favilukis, J., S. C. Ludvigson, and S. Van Nieuwerburgh. 2017. “The Macroeconomic Effects of Housing Wealth, Housing Finance, and Limited Risk Sharing in General Equilibrium.” _Journal of Political Economy_ 125, no. 1: 140–223. 

Flor, M. A., and T. Klarl. 2017. “On the Cyclicity of Regional House Prices: New Evidence for US Metropolitan Statistical Areas.” _Journal of Economic Dynamics and Control_ 77: 134–156. 

Friedman, J., T. Hastie, and R. Tibshirani. 2010. “Regularization Paths for Generalized Linear Models via Coordinate Descent.” _Journal of Statistical Software_ 33, no. 1: 1. 

Gabauer, D., R. Gupta, H. A. Marfatia, and S. M. Miller. 2024. “Estimating Us Housing Price Network Connectedness: Evidence From Dynamic Elastic Net, Lasso, and Ridge Vector Autoregressive Models.” _International Review of Economics & Finance_ 89: 349–362. 

Gatzlaff, D., and D. Tirtiroğlu. 1995. “Real Estate Market Efficiency: Issues and Evidence.” _Journal of Real Estate Literature_ 3, no. 2: 157–189. 

Gau, G. W. 1984. “Weak Form Tests of the Efficiency of Real Estate Investment Markets.” _Financial Review_ 19, no. 4: 301–320. 

Gau, G. W. 1985. “Public Information and Abnormal Returns in Real Estate Investment.” _Real Estate Economics_ 13, no. 1: 15–31. 

Ghysels, E., A. Plazzi, R. Valkanov, and W. Torous. 2013. “Forecasting Real Estate Prices.” _Handbook of Economic Forecasting_ 2: 509–580. 

Giacomini, R., and H. White. 2006. “Tests of Conditional Predictive Ability.” _Econometrica_ 74, no. 6: 1545–1578. 

Gupta, R. 2013. “Forecasting House Prices for the Four Census Regions and the Aggregate US Economy in a Data- Rich Environment.” _Applied Economics_ 45, no. 33: 4677–4697. 

Gupta, R., and S. Das. 2010. “Predicting Downturns in the US Housing Market: A Bayesian Approach.” _Journal of Real Estate Finance and Economics_ 41: 294–319. 

Gupta, R., and S. M. Miller. 2012. “Ripple Effects and Forecasting Home Prices in Los Angeles, Las Vegas, and Phoenix.” _Annals of Regional Science_ 48: 763–782. 

Han, Y., and R. S. Tsay. 2020. “High- Dimensional Linear Regression for Dependent Data With Applications to Nowcasting.” _Statistica Sinica_ 30, no. 4: 1797–1827. 

Hansen, P. R. 2005. “A Test for Superior Predictive Ability.” _Journal of Business & Economic Statistics_ 23, no. 4: 365–380. 

Hansen, P. R., A. Lunde, and J. M. Nason. 2011. “The Model Confidence Set.” _Econometrica_ 79, no. 2: 453–497. 

Harvey, D. I., S. J. Leybourne, and P. Newbold. 1998. “Tests for Forecast Encompassing.” _Journal of Business & Economic Statistics_ 16, no. 2: 254–259. 

Hirata, H., M. A. Kose, C. Otrok, and M. E. Terrones. 2013. “Global House Price Fluctuations: Synchronization and Determinants.” In _NBER International Seminar on Macroeconomics_ , vol. 9, 119–166. University of Chicago Press. 

Hurn, S., S. Shi, and B. Wang. 2022. “Housing Networks and Driving Forces.” _Journal of Banking & Finance_ 134: 106318. 

Johnes, G., and T. Hyclak. 1999. “House Prices and Regional Labor Markets.” _Annals of Regional Science_ 33: 33–49. 

Karlsson, S. 2013. “Forecasting With Bayesian Vector Autoregression.” In _Handbook of Economic Forecasting_ , 791–897. Elsevier. 

Kock, A. B., and L. Callot. 2015. “Oracle Inequalities for High Dimensional Vector Autoregressions.” _Journal of Econometrics_ 186, no. 2: 325–344. 

Kock, A. B., M. Medeiros, and G. Vasconcelos. 2020. “Penalized Time Series Regression.” In _Macroeconomic Forecasting in the Era of Big Data_ , 193–228. Springer. 

Koop, G. 2017. “Bayesian Methods for Empirical Macroeconomics With Big Data.” _Review of Economic Analysis_ 9, no. 1: 33–56. 

Koop, G., and D. Korobilis. 2016. “Model Uncertainty in Panel Vector Autoregressive Models.” _European Economic Review_ 81: 115–131. 

Koop, G., and D. Korobilis. 2019. “Forecasting With High- Dimensional Panel Vars.” _Oxford Bulletin of Economics and Statistics_ 81, no. 5: 937–959. 

Leeb, H., and B. M. Pötscher. 2005. “Model Selection and Inference: Facts and Fiction.” _Econometric Theory_ 21, no. 1: 21–59. 

Li, J., Z. Liao, and R. Quaedvlieg. 2022. “Conditional Superior Predictive Ability.” _Review of Economic Studies_ 89, no. 2: 843–875. 

Loh, P.- L., and M. J. Wainwright. 2011. “High- Dimensional Regression With Noisy and Missing Data: Provable Guarantees With Non- Convexity.” _Advances in Neural Information Processing Systems_ 24: 1–9. 

Lütkepohl, H. 2005. _New Introduction to Multiple Time Series Analysis_ . Springer Science & Business Media. 

Malpezzi, S. 1999. “A Simple Error Correction Model of House Prices.” _Journal of Housing Economics_ 8, no. 1: 27–62. 

Marcellino, M., J. H. Stock, and M. W. Watson. 2006. “A Comparison of Direct and Iterated Multistep AR Methods for Forecasting Macroeconomic Time Series.” _Journal of Econometrics_ 135, no. 1–2: 499–526. 

Masini, R. P., M. C. Medeiros, and E. F. Mendes. 2021. “Machine Learning Advances for Time Series Forecasting.” _Journal of Economic Surveys_ 37, no. 1: 76–111. 

Masini, R. P., M. C. Medeiros, and E. F. Mendes. 2022. “Regularized Estimation of High- Dimensional Vector Autoregressions With Weakly Dependent Innovations.” _Journal of Time Series Analysis_ 43, no. 4: 532–557. 

Medeiros, M. C., and E. F. Mendes. 2016. “1- Regularization of High- Dimensional Time- Series Models With Non- Gaussian and Heteroskedastic Errors.” _Journal of Econometrics_ 191, no. 1: 255–271. 

Meinshausen, N., and P. Bühlmann. 2006. “High- Dimensional Graphs and Variable Selection With the Lasso.” _Annals of Statistics_ 34, no. 3: 1436–1462. 

Meszaros, J. 2024. “A Brief Review of House Price Forecasting Methods.” _CRE Real Estate Issues_ 48, no. 4: 1–8. 

Milunovich, G. 2020a. “Forecasting Australia's Real House Price Index: A Comparison of Time Series and Machine Learning Methods.” _Journal of Forecasting_ 39, no. 7: 1098–1118. 

Milunovich, G. 2020b. “Mapping Out Network Connections Between Residential Property Markets.” _Economics Letters_ 189: 109006. 

Muellbauer, J., and A. Murphy. 1997. “Booms and Busts in the UK Housing Market.” _Economic Journal_ 107, no. 445: 1701–1727. 

Nardi, Y., and A. Rinaldo. 2011. “Autoregressive Process Modeling via the Lasso Procedure.” _Journal of Multivariate Analysis_ 102, no. 3: 528–549. 

Nicholson, W. B., D. S. Matteson, and J. Bien. 2017. “Varx- L: Structured Regularization for Large Vector Autoregressions With Exogenous Variables.” _International Journal of Forecasting_ 33, no. 3: 627–651. 

Panagiotelis, A., G. Athanasopoulos, R. J. Hyndman, B. Jiang, and F. Vahid. 2019. “Macroeconomic Forecasting for Australia Using a Large Number of Predictors.” _International Journal of Forecasting_ 35, no. 2: 616–633. 

23 

_Journal of Forecasting,_ 2026 

Pesaran, M. H., A. Pick, and A. Timmermann. 2011. “Variable Selection, Estimation and Inference for Multi- Period Forecasting Problems.” _Journal of Econometrics_ 164, no. 1: 173–187. 

Plakandaras, V., R. Gupta, P. Gogas, and T. Papadimitriou. 2015. “Forecasting the Us Real House Price Index.” _Economic Modelling_ 45: 259–267. 

Qian, J., T. Hastie, J. Friedman, R. Tibshirani, and N. Simon (2013). Glmnet for Matlab. 2013. http:// www. stanf ord. edu/ ~ hastie/ glmnet_ matlab. 

Rapach, D. E., and J. K. Strauss. 2007. “Forecasting Real Housing Price Growth in the Eighth District States.” _Federal Reserve Bank of St. Louis. Regional Economic Development_ 3, no. 2: 33–42. 

Rapach, D. E., and J. K. Strauss. 2009. “Differences in Housing Price Forecastability Across US States.” _International Journal of Forecasting_ 25, no. 2: 351–372. 

Reinsel, G. 1983. “Some Results on Multivariate Autoregressive Index Models.” _Biometrika_ 70, no. 1: 145–156. 

Robstad, Ø. 2018. “House Prices, Credit and the Effect of Monetary Policy in Norway: Evidence From Structural VAR Models.” _Empirical Economics_ 54, no. 2: 461–483. 

Schindler, F. 2013. “Predictability and Persistence of the Price Movements of the S&P/Case- Shiller House Price Indices.” _Journal of Real Estate Finance and Economics_ 46, no. 1: 44–90. 

Sekine, A., and T. Tsuruga. 2018. “Effects of Commodity Price Shocks on Inflation: A Cross- Country Analysis.” _Oxford Economic Papers_ 70, no. 4: 1108–1135. 

Shi, S., and P. C. Phillips. 2023. “Diagnosing Housing Fever With an Econometric Thermometer.” _Journal of Economic Surveys_ 37, no. 1: 159–186. 

Shi, S., A. Rahman, and B. Z. Wang. 2020. “Australian Housing Market Booms: Fundamentals or Speculation?” _Economic Record_ 96, no. 315: 381–401. 

Smeekes, S., and E. Wijler. 2018. “Macroeconomic Forecasting Using Penalized Regression Methods.” _International Journal of Forecasting_ 34, no. 3: 408–430. 

Sorjamaa, A., J. Hao, N. Reyhani, Y. Ji, and A. Lendasse. 2007. “Methodology for Long- Term Prediction of Time Series.” _Neurocomputing_ 70, no. 16–18: 2861–2869. 

Stevenson, S. 2000. “A Long- Term Analysis of Regional Housing Markets and Inflation.” _Journal of Housing Economics_ 9, no. 1–2: 24–39. 

Stock, J., and M. Watson. 2016. “Dynamic Factor Models, FactorAugmented Vector Autoregressions, and Structural Vector Autoregressions in Macroeconomics.” In _Handbook of Macroeconomics_ , 415–525. Elsevier. 

Tibshirani, R. 1996. “Regression Shrinkage and Selection via the Lasso.” _Journal of the Royal Statistical Society: Series B (Methodological)_ 58, no. 1: 267–288. 

Tsai, I.- C. 2015. “Spillover Effect Between the Regional and the National Housing Markets in the UK.” _Regional Studies_ 49, no. 12: 1957–1976. 

West, K. D. 1996. “Asymptotic Inference About Predictive Ability.” _Econometrica: Journal of the Econometric Society_ 64, no. 5: 1067–1084. 

White, H. 2000. “A Reality Check for Data Snooping.” _Econometrica_ 68, no. 5: 1097–1126. 

Wilms, I., and C. Croux. 2016. “Forecasting Using Sparse Cointegration.” _International Journal of Forecasting_ 32, no. 4: 1256–1267. 

Zhang, D., and G.- Z. Fan. 2019. “Regional Spillover and Rising Connectedness in China's Urban Housing Prices.” _Regional Studies_ 53, no. 6: 861–873. 

Zhao, P., and B. Yu. 2006. “On Model Selection Consistency of Lasso.” _Journal of Machine Learning Research_ 7: 2541–2563. 

Zhu, X., R. Pan, G. Li, Y. Liu, and H. Wang. 2017. “Network Vector Autoregression.” _Annals of Statistics_ 45, no. 3: 1096–1123. 

Zou, H. 2006. “The Adaptive Lasso and Its Oracle Properties.” _Journal of the American Statistical Association_ 101, no. 476: 1418–1429. 

#### **Appendix A** 

#### **Simulation Study** 

In this section, we present robustness analyses for the simulation study (1) using the AFE loss function and (2) using the adaptive LASSO estimation method instead of LASSO. 

#### **A1** | **Simulation Results Based on AFE Loss** 

Table A1 presents the results of the simulation analysis using the AFE loss function, analogous to Table 7 in Section 5. Notably, the results obtained using the AFE loss function align with the findings derived from the utilization of the SFE loss function. The strength of connectivity has a noteworthy influence on short- term forecasting. In the case when the connectivity strength is weak, the univariate model outperformed the multivariate model. However, as the connectivity strength increases, the multivariate model excels. In terms of long- term forecasting, the univariate AR model generally outperforms the multivariate VAR model, although the difference is typically small. An exception to this pattern occurs for strong connectivity strength combined with 55% sparsity, where the multivariate VAR model performs slightly better. The simulation results present a mixed outcome for midterm forecasting horizons. Specifically, the univariate model demonstrates superior performance when the sparsity level is high, but this advantage is observed primarily when the connectivity strength is weak or moderate. Conversely, the multivariate model exhibits improved performance when the connectivity strength is strong. 

#### **A2** | **Robustness Check: Adaptive LASSO** 

The LASSO method has found widespread use in regression analysis for variable selection. Nevertheless, it applies a uniform penalty to all parameters, which might not be the most effective strategy for accurate forecasting. Specifically, applying a more pronounced penalty to parameters near zero and a relatively minor penalty to those of greater magnitude (irrespective of their sign) has the potential to yield a more parsimonious model and enhance forecasting accuracy. This is the precise role fulfilled by the adaptive Lasso technique (Zou 2006). The objective function of the adaptive LASSO is specified as follows: 



where _휔i_ , _j_ = | _휙ij_<sup>(</sup><sup>_i_)| −</sup><sup>_훾_is the weight factor for coefficient</sup><sup>_휙_(</sup> _ij_<sup>_i_), with</sup> _i_ = 1, …, _N_ , _j_ = 1, …, _p_ . The parameter _훾_ is a positive constant, taking typical values of 0.5, 1, and 2. The value _휙ij_<sup>(</sup><sup>_i_) is an estimate of</sup><sup>_휙_(</sup> _ij_<sup>_i_) obtained</sup> from an initial regression method, such as OLS, Ridge, or LASSO.<sup>7</sup> This weight function establishes an inverse relationship with the absolute magnitude of the coefficient. Consequently, the adaptive LASSO technique facilitates more assertive reduction of coefficients associated with less significant variables. 

Figures A.1–A.4 depict the average MSFEs for the VAR(1) model using LASSO and adaptive Lasso across various forecast horizons. The plot reveals that LASSO exhibits comparable forecasting performance to adaptive Lasso, with instances where LASSO outperforms its counterpart. 

24 

_Journal of Forecasting,_ 2026 

**TABLE A1** |    The averaged percentage of one model being included in a 90% MCS at different forecasting horizons, built on the AFE loss function. 

|||**Univariate**|**Multiva**|**riate**|
|---|---|---|---|---|
|**Strength**|**Sparsity**|**AR(1)**<br>**ARMA(1,1)**|**VAR(1)**|**VAR(2)**|
|_h_=1|||||
|Weak|90%|**85.8**<br>78.1|77.3|76.0|
||70%|**86.3**<br>78.3|77.3|75.9|
||40%|**86.2**<br>78.3|78.5|75.8|
|Moderate|90%|**83.4**<br>75.3|80.3|76.0|
||70%|77.9<br>70.5|**86.2**|75.8|
||40%|64.0<br>58.9|**92.5**|73.7|
|Strong|90%|42.8<br>39.6|**92.7**|77.3|
||70%|1.9<br>1.9|**97.1**|65.6|
||55%|0.0<br>0.0|**99.2**|44.6|
|_h_=3|||||
|Weak|90%|**83.1**<br>78.0|82.2|82.3|
||70%|81.3<br>77.9|**83.3**|81.6|
||40%|83.1<br>78.1|**83.3**|82.6|
|Moderate|90%|83.0<br>78.4|**83.0**|82.5|
||70%|81.9<br>77.9|**83.3**|81.7|
||40%|82.5<br>78.2|**83.9**|81.8|
|Strong|90%|82.6<br>78.4|**83.6**|81.6|
||70%|60.8<br>57.7|**90.8**|78.1|
||55%|4.4<br>4.4|**97.5**|61.6|
|_h_=6|||||
|Weak|90%|**82.6**<br>79.3|82.5|81.6|
||70%|82.3<br>78.9|**82.7**|81.6|
||40%|83.2<br>78.7|**83.5**|81.7|
|Moderate|90%|**82.6**<br>79.1|82.5|81.5|
||70%|82.5<br>79.4|**83.1**|81.6|
||40%|82.7<br>78.4|**83.3**|81.8|
|Strong|90%|82.2<br>78.6|**82.3**|81.8|
||70%|81.4<br>77.8|**83.3**|81.3|
||55%|42.1<br>41.0|**94.4**|75.7|
|_h_=12|||||
|Weak|90%|**83.2**<br>79.9|82.4|80.7|
||70%|**82.9**<br>79.4|81.6|80.7|
||40%|**82.9**<br>79.9|82.0|80.7|
|Moderate|90%|**82.7**<br>79.7|82.2|81.2|
||70%|**83.6**<br>79.8|82.6|81.3|
||40%|**82.7**<br>79.7|82.6|81.6|
|Strong|90%|**83.7**<br>80.1|82.2|81.0|
||70%|**83.2**<br>79.5|81.8|80.7|
||55%|76.8<br>73.9|**83.8**|83.0|



_Note:_ The percentage is calculated based on the 300 replications. The result in boldface indicates the maximum value among all the competing models. 

25 

_Journal of Forecasting,_ 2026 



**FIGURE A.1** |    The kernel density plots illustrate the average MSFEs for one- step- ahead forecasts of the VAR(1) model with different estimation methods (LASSO and adaptive LASSO). The parentheses indicate the initial regression method employed in the adaptive Lasso approach. 

26 

_Journal of Forecasting,_ 2026 



<!-- Start of picture text -->
2 2 2<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7.5 8 8.5 9 9.5 10 7.5 8 8.5 9 9.5 10 7.5 8 8.5 9 9.5 10<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7.5 8 8.5 9 9.5 10 8 9 10 11 8 9 10 11 12<br>1.2 0.5 0.25<br>1<br>0.4 0.2<br>0.8<br>0.3 0.15<br>0.6<br>0.2 0.1<br>0.4<br>0.1 0.05<br>0.2<br>0 0 0<br>9 10 11 12 14 16 18 20 22 20 25 30 35<br><!-- End of picture text -->

**FIGURE A.2** |    The kernel density plots illustrate the average MSFEs for three- step- ahead forecasts of the VAR(1) model with different estimation methods (LASSO and adaptive LASSO). The parentheses indicate the initial regression method employed in the adaptive Lasso approach. 

27 

_Journal of Forecasting,_ 2026 



<!-- Start of picture text -->
2 2 2<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7.5 8 8.5 9 9.5 10 7.5 8 8.5 9 9.5 10 7.5 8 8.5 9 9.5 10<br>1.5 1.5 1.5<br>1 1 1<br>0.5 0.5 0.5<br>0 0 0<br>7.5 8 8.5 9 9.5 10 8 9 10 11 8 9 10 11 12 13<br>1.2 0.3 0.1<br>1 0.25<br>0.08<br>0.8 0.2<br>0.06<br>0.6 0.15<br>0.04<br>0.4 0.1<br>0.02<br>0.2 0.05<br>0 0 0<br>9 10 11 12 16 18 20 22 24 26 20 30 40 50 60 70<br><!-- End of picture text -->

**FIGURE A.3** |    The kernel density plots illustrate the average MSFEs for six- step- ahead forecasts of the VAR(1) model with different estimation methods (LASSO and adaptive LASSO). The parentheses indicate the initial regression method employed in the adaptive Lasso approach. 

28 

_Journal of Forecasting,_ 2026 



**FIGURE A.4** |    The kernel density plots illustrate the average MSFEs for six- step- ahead forecasts of the VAR(1) model with different estimation methods (LASSO and adaptive LASSO). The parentheses indicate the initial regression method employed in the adaptive Lasso approach. 

29 

_Journal of Forecasting,_ 2026 

**Appendix B** 

#### **Lists of LGAs and Cities** 

**TABLE B1** |    List of LGAs included in the empirical analysis for Sydney and Melbourne; LGAs are grouped by region. 

|**Sydney**||**Melbourne**||
|---|---|---|---|
|**Western City**|Blue Mountains|**Eastern Region**|Knox|
||Hawkesbury||Manningham|
||Penrith||Maroondah|
||Camden||Monash|
||Campbelltown||Whitehorse|
||Fairfield||Yarra Ranges|
||Liverpool|**Inner Metro Region**|Melbourne|
||Wollondilly||Port Phillip|
|**Central City**|Blacktown||Yarra|
||Cumberland|**Inner South East Region**|Bayside|
||Parramatta||Boroondara|
||The Hills Shire||Glen Eira|
|**Eastern City**|Burwood||Stonnington|
||Canada Bay|**Northern Region**|Banyule|
||Inner West||Darebin|
||Randwick||Hume|
||Strathfield||Moreland|
||Woollahra||Nillumbik|
||Waverley||Whittlesea|
||Sydney|**Southern Region**|Cardinia|
|**North District**|Hornsby||Casey|
||Hunters Hill||Frankston|
||Kuringgai||Greater Dandenong|
||Lane Cove||Kingston|
||Northern Beaches||Mornington Peninsula|
||Mosman|**Western Region**|Brimbank|
||Willoughby||Hobsons Bay|
||Ryde||Maribyrnong|
||North Sydney||Melton|
|**South District**|Georges River||Moonee Valley|
||Canterbury–Bankstown<br>Sutherland||Wyndham|



30 

_Journal of Forecasting,_ 2026 

**TABLE B2** |    List of Tiers 1–3 cities for the Chinese housing market. 

|**Tier 1 cities**||||
|---|---|---|---|
|**Beijing**|**Guangzhou**|**Shanghai**|**Shenzhen**|
|**Tier 2 cities**||||
|Changchun|Changsha|Chengdu|Chongqing|
|Dalian|Haikou|Hangzhou|Harbin|
|Hefei|Hohhot|Jinan|Nanchang|
|Nanjing|Nanning|Ningbo|Qingdao|
|Shenyang|Shijiazhuang|Suzhou|Tianjin|
|Wenzhou|Wuxi|Xi'An|Xiamen|
|Xining|Zhengzhou|||
|**Tier 3 cities**||||
|Anqing|Anshan|Baoding|Baotou|
|Bengbu|Changde|Changzhou|Chuzhou|
|Dandong|Deyang|Dongguan|HuaiAn|
|Huzhou|Jiaxing|Jieyang|Jingdezhen|
|Jinhua|Jiujiang|Kaifeng|Langfang|
|Leshan|Lianyungang|Luohe|Luoyang|
|Luzhou|Mianyang|Nanchong|Nantong|
|Nanyang|Ningde|Qinhuangdao|Quanzhou|
|Rizhao|Shangrao|Shantou|Shaoxing|
|Songyuan|Suqian|Taizhou|Tangshan|
|Tieling|Wuhu|Huludao|Xingtai|
|Xinxiang|Xuancheng|Xuzhou|Yancheng|
|Yangzhou|Yichun|Yingkou|Zaozhuang|
|Zhangjiakou|Zhangzhou|Zhaoqing|Zhenjiang|
|Zhongshan|Zhumadian|||



31 

_Journal of Forecasting,_ 2026 

