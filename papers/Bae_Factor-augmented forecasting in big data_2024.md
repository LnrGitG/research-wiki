---
title: Bae_Factor-augmented forecasting in big data_2024
type: paper
source_pdf: raw/papers/Bae_Factor-augmented forecasting in big data_2024.pdf
converted: 2026-08-18
---

International Journal of Forecasting 40 (2024) 1660–1688 



Contents lists available at ScienceDirect International Journal of Forecasting journal homepage: www.elsevier.com/locate/ijforecast 



# Factor-augmented forecasting in big data<sup>✩</sup> 

## Juhee Bae 



_University of Glasgow, University Avenue, G12 8QQ, UK_ 

|a r t i c l e<br>i n f o|a b s t r a c t|
|---|---|
|_Keywords:_<br>Factor models<br>Forecasting<br>Partial Least Squares (PLS)<br>Dimension reduction<br>Diffusion index<br>Big data|This paper evaluates the predictive performance of various factor estimation methods in<br>big data. Extensive forecasting experiments are examined using seven factor estimation<br>methods with 13 decision rules determining the number of factors. The out-of-sample<br>forecasting results show that the first Partial Least Squares factor (1-PLS) tends to be the<br>best-performing method among all the possible alternatives. This finding is prevalent in<br>many target variables under different forecasting horizons and models. This significant<br>improvement can be explained by the PLS factor estimation strategy that considers the<br>covariance with the target variable. Second, using a consistently estimated number of<br>factors may not necessarily improve forecasting performance. The greatest predictive<br>gain often derives from decision rules that do not consistently estimate the true number<br>of factors.<br>©2024 The Author(s). Published by Elsevier B.V. on behalf of International Institute of<br>Forecasters. This is an open access article under the CC BY-NC-ND license<br>(http://creativecommons.org/licenses/by-nc-nd/4.0/).|



### **1. Introduction** 

A trend in economics is toward harnessing hundreds of economic time series. By introducing a small number of factors that govern comovement in data, parsimonious models can be achieved while preserving the important information. In this way, factor models have also enabled significant improvements in forecasting. Many studies have found encouraging empirical evidence for factor-augmented forecasts, also known as diffusion index forecasts. (Angelini, Camba-Mendez, Giannone, Reichlin, and Rünstler (2011), Artis, Banerjee, and Marcellino (2005), Barhoumi et al. (2008), Cristadoro, Forni, Reichlin, and Veronese (2005), Forni, Hallin, Lippi, and Reichlin (2003), Giannone, Reichlin, and Small (2008), Stock 

✩ I would like to thank Seung C. Ahn for his guidance and support. I am also grateful to Marine Carrasco, Raffaella Giacomini, Dimitris Korobilis, Domenico Ferraro, Nicolai Kuminoff, Seth Pruitt, Berthold Herrendorf, Bart Hobijn, Nazım Tamkoç, and Gustavo Ventura for their suggestions and comments. This paper was presented in seminars and workshops at NBER-NSF Time Series Conference 2021 at Rice University, European Winter Meeting of the Econometric Society 2021 at the University of Barcelona School of Economics, Arizona State University, the University of Glasgow, Northeastern University, and the Korea Institute for International Economic Policy (KIEP). I would like to thank the participants in the seminars and workshops. 

_E-mail address:_ Juhee.Bae@glasgow.ac.kr. 

and Watson (1999, 2002a, 2002b), and Schumacher and Breitung (2008), among many). 

There have been many attempts to estimate the latent factors, most commonly via Principal Components Analysis (PCA), which estimates the factors that best explain the variance of predictors. However, many alternative factor estimation methods aim to improve upon PCA. Although certain sets of factor estimation methods and decision rules to determine the number of factors are routinely used, large choice sets of possible factor-augmented forecasts are available. 

Despite this variety, there is no consensus on their relative predictive ability. For instance, Schumacher (2007) finds that dynamic principal components outperform static principal components but are sensitive to parameter choice. Boivin and Ng (2005) find that the static principal components with unrestricted forecasts work systematically better in empirical analysis. D’Agostino and Giannone (2012) show that the two methods provide similar performance. Beyond principal components, comparing factor estimation methods is more challenging, as each method has different advantages and disadvantages. The question then arises as to how predictive these factor models are in typical big data. Further, what are their common empirical properties and what unexpected features should be considered in forecasting? More importantly, which factor 

https://doi.org/10.1016/j.ijforecast.2024.02.004 

0169-2070/© 2024 The Author(s). Published by Elsevier B.V. on behalf of International Institute of Forecasters. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/). 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

estimation method and decision rule tend to provide the most accurate predictions? 

Accordingly, this paper contributes to the literature by extensively comparing the performance of widely used factor estimation methods. First, our paper aims to combine various factor estimation methods, compare their predictive performance, propose the best-performing method, and serve as guideposts for forecasting macroeconomic and financial variables. Our findings show that the first Partial Least Squares factor (1-PLS) tends to be the best forecasting method. To our knowledge, this is a new finding in the forecasting literature. Second, this paper documents novel empirical properties and their implications for factor-augmented forecasts. For instance, we provide an empirical finding that consistently estimated numbers of factors may not always produce the best forecasts, which is particularly important given their popular use. 

Specifically, seven factor estimation methods are tested: Principal Component Analysis, Weighted Principal Components (Boivin & Ng, 2006), one-sided estimation (Forni, Hallin, Lippi, & Reichlin, 2005), forecasting using targeted predictors (Bai & Ng, 2008), Partial Least Squares (Kelly and Pruitt (2015) and Ahn and Bae (2022)), two-step estimator (Doz, Giannone, & Reichlin, 2011), and quasimaximum likelihood estimator (Doz, Giannone, & Reichlin, 2012). We construct a big dataset of 178 monthly U.S. macroeconomic and finance variables. Our dataset is in line with the conventional ‘‘big data’’ or so-called Stock– Watson data used in a vast macroeconomic literature, such as Bernanke and Boivin (2003), Bernanke, Boivin, and Eliasz (2005), McCracken and Ng (2016), Medeiros, Vasconcelos, Veiga, and Zilberman (2021), Stock and Watson (1996, 1998, 2002b) and Ludvigson, Ma, and Ng (2021) among many. In this extensive out-of-sample forecasting experiment, 148 target variables are forecasted using three forecasting equations across four forecasting horizons, using the seven factor estimation methods with 13 decision rules. 

This paper reports two main findings. First, we find that Partial Least Squares (PLS) often outperforms other factor estimation methods: 1-PLS tends to show the largest predictive improvement and often becomes the bestperforming method among all alternatives. The strong performance of 1-PLS is found in many target variables under various forecasting models and horizons. More specifically, 1-PLS is often the dominant decision rule for PLS to forecast a wide range of target variables, contrary to other factor estimation methods without strongly dominant decision rules. The strong predictive power of PLS derives from its factor estimation strategy. PLS estimates factors that have the maximum covariance with a target variable, which explains the significant forecasting improvement. 

PLS was developed by Wold (1966, 1973, 1982) and the large- _N_ and _T_ properties of PLS factors are studied by Kelly and Pruitt (2015) and Groen and Kapetanios (2016). Recently, Ahn and Bae (2022) established the asymptotically optimal number of PLS factors under a general model and showed their general asymptotic and finite-sample properties. Lately, a growing body of literature analyses economic and finance variables using 

PLS; see Kelly and Pruitt (2013), Lin (2018) and Huang, Jiang, Tu, and Zhou (2015) for forecasting stock market returns, Zhang, He, Wang, and Liang (2022) for forecasting crude oil market volatility, Giglio, Kelly, and Pruitt (2016) and Bu, Rogers, and Wu (2021) for constructing systemic risk index and measure of monetary policy shocks, Light, Maslov, and Rytchkov (2017) for estimating expected returns on individual stocks, Hepenstrick and Marcellino (2019) and Marcellino and Sivec (2021) for nowcasting GDP growth using mixed-frequency data, Fuentes, Poncela, and Rodríguez (2015) for comparison of Sparse Partial Least Squares, PLS, and other alternatives including PCA. Despite this increasing popularity, it was not fully investigated how predictive PLS factors are in the typical big data, compared to a vast set of other widelyused factor estimation methods. This paper contributes to the existing literature by showing the strong performance of PLS in extensive out-of-sample forecasting experiments in the popular big data with macroeconomic and financial variables. 

Second, a consistently estimated number of factors does not always lead to the best predictive performance in empirical practice. We examine the forecasting performance of 13 decision rules to determine the number of estimated factors. Many are consistent for the true number of latent factors that govern predictors, such as methods proposed by Alessi, Barigozzi, and Capasso (2010), Bai and Ng (2002, 2007), Hallin and Liška (2007), Onatski (2010) and Ahn and Horenstein (2013). However, decision rules that do not necessarily estimate the true number of factors consistently often provide better predictive accuracy. One possible explanation for this finding is the existence of irrelevant factors that govern predictors but do not strongly explain the target variable. The presence of irrelevant factors has been considered in the literature (Ahn and Bae (2022), Kelly and Pruitt (2015) and Huang, Jiang, Li, Tong, and Zhou (2022)). While the existing literature focuses on theoretical aspects of irrelevant factors, the novelty of our finding comes from providing empirically supporting evidence. In this sense, the first finding of encouraging forecasting performance of 1-PLS can also be explained by the fact that PLS can filter away the irrelevant factors that do not explain the target variable. 

Also, another notable finding is that the determined numbers of factors vary significantly across decision rules, even among consistently estimated numbers of factors. Due to this reason, forecasting accuracy changes substantially among decision rules, even for the same factor estimation method. Therefore, choosing the factor estimation method and decision rule is crucial. However, despite this variety, 1-PLS tends to be the best-performing method among all the alternatives. 

Some empirical evidence on the strong forecasting performance of PLS is proposed in the literature; see Ahn and Bae (2022) and Fuentes et al. (2015) among many others. While the former investigates the predictive performance of PLS on a set of macroeconomic variables to reassure their theoretical results, the latter compares the forecasting performance of PLS and Sparse Partial Least Squares. This paper aims to document the empirical properties of general factor-augmented forecasts, as well as 

1661 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

the forecasting behaviour of conventional decision rules. In addition, the relative forecasting performances across different factor estimation methods and decision rules are extensively compared. 

This paper is organized as follows. Section 2 discusses the econometric framework and introduces factor estimation methods. Section 3 explains the data and forecasting experiments. Section 4 reports and interprets the empirical results, and Section 5 concludes. Throughout this paper, **1** _a_ denotes _a_ × 1 vector of ones. _P_ ( _B_ ) = _B_ ( _B_<sup>′</sup> _B_ )<sup>−1</sup> _B_<sup>′</sup> and _Q_ ( _B_ ) = _Ia_ − _P_ ( _B_ ) for _a_ × _b_ full-column rank matrix _B_ . 

### **2. Forecasting model and factor estimation methods** 

### _2.1. Approximate dynamic factor model_ 

We briefly introduce a simple approximate dynamic factor model that motivates our main forecasting framework. Let _yt_ +1 be the one-period ahead forecast target being forecasted. The _N_ × 1 vector of predictors at time _t_ is denoted as _xt_ = ( _x_ 1 _t , . . . , xNt_ )<sup>′</sup> . Both forecast target _yt_ +1 and predictors _xt_ have mean zero for all _t_ = 1 _, . . . , T_ . The following dynamic factor model is assumed. 





where the dynamic factor _ft_ is a _q_ ×1 vector and _β_ ( _L_ ) _, γ_ ( _L_ ) and _λi_ ( _L_ ) are lag polynomials. More specifically, assuming _β_ ( _L_ ) and _λi_ ( _L_ ) having finite orders of at most _s_ , the 1 × _q_ vectors _β_ ( _L_ ) and _λi_ ( _L_ ) are defined as _β_ ( _L_ ) = _β_ 0+ _β_ 1 _L_ +· · ·+ _βsL_<sup>_s_</sup> and _λi_ ( _L_ ) = _λi_ 0 + _λi_ 1 _L_ + · · · + _λisL_<sup>_s_</sup> with 1 × _q_ vectors _βj_ and _λj_ for _j_ = 0 _,_ 1 _, . . . , s_ . Then we can represent the above dynamic factor model (1) into a static form: 



where _Ft_ = ( _ft_<sup>′</sup><sup>_, . . . , f_′</sup> _t_ − _s_<sup>)′and</sup><sup>_β_=(</sup><sup>_β_0</sup><sup>_, . . . , βs_)′are</sup><sup>_r_× 1</sup> vectors with _r_ = ( _s_ + 1) _q_ and _λi_ = ( _λi_ 0 _, . . . , λis_ ) is a 1 × _r_ vector. Alternatively, the model (3) can also be written as 



where _et_ = ( _e_ 1 _t , . . . , eNt_ )<sup>′</sup> is a _N_ × 1 vector and _N_ × _r_ matrix _Λ_ is defined as _Λ_ = [ _Λ_<sup>′</sup> 1<sup>_, . . . , Λ_</sup> _N_<sup>′]′.Letting</sup><sup>_X_=</sup> [ _x_ 1 _, . . . , xT_ ]<sup>′</sup> and _y_ = [ _y_ 2 _, . . . , yT_ +1]<sup>′</sup> be the _T_ × _N_ matrix of predictors and _T_ × 1 vector of a target variable, our model is thus 



where _F_ = ( _F_ 1 _, . . . , FT_ )<sup>′</sup> , _u_ = ( _u_ 2 _, . . . , uT_ +1)<sup>′</sup> , and _E_ = ( _e_ 1 _, . . . , eT_ )<sup>′</sup> . 

Empirically, the static framework in (3) estimates factors by a time domain analysis, and the dynamic factors in model (1) are estimated by the frequency domain method. This paper also compares factor estimation methods based on both models (1) and (3). 

The main empirical experiments focus on _h_ -step forecasts in which the _h_ -step-ahead projection is used directly 

to make the forecast. The multistep-ahead version of (3) gives the main econometric forecasting framework, 



where _y_<sup>_h_</sup> _t_ + _h_<sup>isthe</sup><sup>_h_-step-aheadtargetvariable.Notethat</sup> the forecasting model (5) involves additional lags of _Ft_ , denoted by _βh_ ( _L_ ). As the static representation of (2) shows, the static factors _Ft_ already incorporate the past dynamic factors _ft , . . . , ft_ − _s_ . However, many studies often incorporate the lagged static factors, denoted by _βh_ ( _L_ ) in (5) to detect possible effects of past static factors, such as Stock and Watson (2002b) and McCracken and Ng (2016), among many. Therefore, this paper also considers such a framework as one of the three main forecasting models in Section 3.2. 

### _2.2. Factor estimation methods_ 

We introduce a _d_ dimensional factor _Gt_ such that _β_<sup>′</sup> _Ft_ = _δ_<sup>′</sup> _Gt_ holds with a _d_ × 1 vector _δ_ . Then, _yt_ +1 in the model (1) and (3) can be replaced as follows. _yt_ +1 = _δ_<sup>′</sup> _Gt_ + _γ_ ( _L_ ) _yt_ + _ut_ +1 (6) 

For forecasting, estimation of _Ft_ is not essential, but rather _β_<sup>′</sup> _Ft_ which explains _yt_ +1 is needed. Many factor estimation methods estimate _Gt_ = _AFt_ asymptotically, with an invertible _r_ × _r_ matrix _A_ , which also makes _β_<sup>′</sup> _A_<sup>−1</sup> _AFt_ = _β_<sup>′</sup> _Ft_ . Then, _Gt_ = _AFt_ , _δ_<sup>′</sup> = _β_<sup>′</sup> _A_<sup>−1</sup> with _d_ = _r_ . However, some factor estimation methods, such as Partial Least Squares, can recover _β_<sup>′</sup> _Ft_ with _Gt_ where _d_ ≤ _r_ (Ahn and Bae (2022), Kelly and Pruitt (2015), and Helland (1988, 1990)). To summarize, _Gt_ are the factors being estimated; they do not need to be the same or have the same dimension as _Ft_ , even asymptotically. 

### _1. Principal Component Analysis (PCA)_ 

Principal Components Analysis (hereafter ‘‘PCA’’) is popular, as discussed by Ahn and Horenstein (2013), Bai (2003), Bai and Ng (2002, 2006), Bernanke et al. (2005), Stock and Watson (2002a, 2002b, 2006) and Jurado, Ludvigson, and Ng (2015) among others. PCA estimates factor loadings _Λ_ and factors _F_ 1 _, F_ 2 _, . . . , FT_ by solving the following least-squares problem, 



_Λ_ subjectˆ<sup>_PCA_</sup> reducesto a normalizationto the scaledof _r N_ eigenvectors<sup>−1</sup> _Λ_<sup>′</sup> _Λ_ = _Ir_ .ofThethesolution,sample covariance matrix of predictors _Σ_<sup>ˆ</sup> _X_ = _T_<sup>−1</sup> _X_<sup>′</sup> _X_ , corresponding to the largest _r_ eigenvalues. The estimated PCA factors are _F_<sup>ˆ</sup><sup>_PCA_</sup> = _N_<sup>−1</sup> _XΛ_<sup>ˆ</sup><sup>_PCA_</sup> . 

### _2. Partial least squares (PLS)_ 

PCA is an unsupervised method and estimates factors that explain predictors most, not the target variable of interest. In contrast, PLS described in Table 1 is a supervised method that estimates factors that have the maximum covariance with the target variable and hence can improve the forecasting performance of PCA. 

1662 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table 1** 

PLS iteration. 

|1.|_j_ denotes the number of iterations.|
|---|---|
|2.|For _j_= 1, find _α_1 such that _α_1 = argmax<br>_α_<br>1<br>_T_<br>_T_∑<br>_t_=1<br>(_α_<sup>′</sup>_xtyt_+1)<sup>2 </sup>subject to _N_<sup>−1</sup>_α_<sup>′</sup>_α_ = 1.<br>The first PLS factor is <sup>ˆ</sup>_F _<sup>_PLS_</sup><br>1<br>= _Xα_1 = _XX_<sup>′</sup>_y_.|
|3.|For _j >_ 1, update predictors to _X_<sup>∗</sup>,<br>where _X_<sup>∗</sup><br>_j_ <sup>=</sup> <sup>_Q_ (ˆ</sup><sup>_F PLS_</sup><br>1 <sup>_, . . . ,_ ˆ</sup><sup>_F PLS_</sup><br>_j_−1<sup>)</sup><sup>_X_ and</sup> <sup>_X_∗</sup><br>_j_ <sup>= [</sup><sup>_x_∗</sup><br>_j,_1<sup>_, . . . , x_∗</sup><br>_j,T_<sup>]′.</sup>|
|4.|Find _αj_ that is _αj_ = argmax<br>_α_<br>1<br>_T_<br>_T_∑<br>_t_=1<br>(_α_<sup>′</sup>_x_<sup>∗</sup><br>_j,t_<sup>_yt_+1)2, subject to</sup> <sup>_N_−1</sup><sup>_α_′</sup><sup>_α_ = 1.</sup><br>The _j_th PLS factor is <sup>ˆ</sup>_F _<sup>_PLS_</sup><br>_j_<br>= _X_<sup>∗</sup><br>_j _<sup>_αj_. For the</sup> <sup>_j_ + 1 iteration, repeat Steps 3 and 4.</sup>|



This table describes PLS iterations. Strictly, the first PLS factor in Step 2 should be _F_<sup>ˆ</sup> 1<sup>_PLS_</sup> = _Xα_ 1 = _XX_<sup>′</sup> _y/_<sup>~~√~~</sup> _y_<sup><u>′</u></sup> _XX_<sup><u>′</u></sup> _<u>y</u>_ because _α_ 1 = _X_<sup>′</sup> _y/_<sup>~~√~~</sup> _y_<sup><u>′</u></sup> _XX_<sup><u>′</u></sup> _y_ . Since the scalar in the denominator of _α_ 1 is for normalization,<sup>~~√~~</sup> _y_<sup><u>′</u></sup> _XX_<sup><u>′</u></sup> _y_ does not affect projection. Therefore, the denominator is omitted for simplicity as it does not change forecasts. 

PLS was first developed by Wold (1966, 1973, 1982). The large- _N_ and large- _T_ properties of PLS factors have been studied (Kelly and Pruitt (2015) and Groen and Kapetanios (2016)), and more general properties of PLS are documented by Ahn and Bae (2022). Recently, PLS has been popularly used in economics and finance; see Bu et al. (2021), Fuentes et al. (2015), Giglio et al. (2016), Hepenstrick and Marcellino (2019), Huang et al. (2015), Kelly and Pruitt (2013), Light et al. (2017), Lin (2018), Marcellino and Sivec (2021) and Zhang et al. (2022), among many. 

Specifically, Ahn and Bae (2022) show the asymptotic properties of PLS in a general environment. They assume that _T_<sup>−1</sup> _F_<sup>′</sup> _F_ = _T_<sup>−1</sup> [ _F_ (1) _, . . . , F_ ( _J_ )]<sup>′</sup> [ _F_ (1) _, . . . , F_ ( _J_ )] → _p diag_ ( _σ_ 1<sup>2</sup><sup>_Ir_(1)</sup><sup>_, . . . , σ_2</sup> _J_<sup>_Ir_(</sup><sup>_J_))and</sup><sup>_N_−1</sup><sup>_Λ_′</sup><sup>_Λ_→</sup><sup>_pIr_,where</sup> for _j_ = 1 _, . . . , J_ , the _T_ × _r_ ( _j_ ) matrix _F_ ( _j_ ) is defined as _F_ ( _j_ ) = [ _f_ ( _j_ ) _,_ 1 _, . . . , f_ ( _j_ ) _,T_ ]<sup>′</sup> with _r_ ( _j_ )×1 vector _f_ ( _j_ ) _,t_ , _r_ = _ΣjJ_ =1<sup>_r_(</sup><sup>_j_)</sup> and _σ_ 1<sup>2</sup> _> σ_ 2<sup>2</sup> _>_ · · · _> σJ_<sup>2</sup> _>_ 0. This assumption implies that _r_ dimensional factors _F_ consist of _J_ groups of factors { _F_ ( _j_ )} _Jj_ =1<sup>,wherethe</sup><sup>_r_(</sup><sup>_j_)dimensionalsubsetof</sup> factors _F_ ( _j_ ) in the _j_ th group shares the same asymptotic variance _σj_<sup>2. Therefore, among</sup><sup>_r_factors, only</sup><sup>_J_≤</sup><sup>_r_factors</sup> have distinct asymptotic variance. They further generalize the assumption to _β_ ( _j_ ) = 0 _r_ ( _j_ )×1 for _j_ = ( _R_ + 1) _, . . . , J_ , so that only the first _R_ groups of factors affect the target variable. 

Then _β_<sup>′</sup> _Ft_ in Eq. (3) is equivalent to **1**<sup>′</sup> _R_<sup>_Gt_,wherethe</sup> _R_ × 1 vector _Gt_ is defined as _Gt_ = ( _f_ (1)<sup>′</sup> _,t_<sup>_β_(1)</sup><sup>_, . . . , f_</sup> (<sup>′</sup> _R_ ) _,t_<sup>_β_(</sup><sup>_R_))′,</sup> which implies _δ_ = **1** _R_ in Eq. (6). Ahn and Bae (2022) show that the first to _R_ th PLS factors can asymptotically span _Gt_ , so that only the first _R_ PLS factors are enough to recover _β_<sup>′</sup> _Ft_ where _R_ ≤ _J_ ≤ _r_ . They further prove that using more than _R_ PLS factors can reduce out-ofsample forecasting accuracy while inflating in-sample fit, even asymptotically. However, no method is known to estimate _R_ consistently. The first PLS factor (1-PLS) tends to give the best result in their simulation results, even when 1 _< R_ . Therefore, 1-PLS, _F_<sup>ˆ</sup> 1<sup>_PLS_</sup> = _XX_<sup>′</sup> _y_ , is explicitly considered here as a decision rule for PLS. 

### _3. Targeted predictors_ 

Bai and Ng (2008) propose using targeted predictors to improve forecasting performance, reasoning that PCA does not consider the predictive ability of each predictor 

_xit_ for the target variable in factor estimation. Accordingly, they propose first selecting a group of ‘targeted’ predictors with high predictive power for the target variable using LASSO (least absolute shrinkage and selection operator) or LARS (least angle regression). Second, PCA factors are estimated only from these targeted predictors. Similarly, the idea of combining factor estimation and shrinkage is also used in Kim and Swanson (2014) and Zhang, Wahab, and Wang (2023), among many others. 

### _Generalized principal components (generalized PC)_ 

Generalized principal components (hereafter ‘‘generalized PC’’) share the same intuition as generalized least squares (GLS). They can improve the efficiency of PCA, especially given heteroskedastic errors or idiosyncratic errors with cross-correlation. Let _Σe_ be the true covariance matrix of idiosyncratic errors; then, generalized PC solves the weighted version of (7), 



subject to a normalization. The estimated factor loadings ˆ ′ are the _r_ scaled eigenvectors of _Σe_<sup>−1</sup><sup>_/_2</sup> _ΣX Σ_<sup>−</sup> _e_<sup>1</sup><sup>_/_2</sup> , corresponding to the _r_ largest eigenvalues. The factors can be estimated by _F_<sup>ˆ</sup><sup>_GPC_</sup> = _N_<sup>−1</sup> _XΛ_<sup>ˆ</sup><sup>_GPC_</sup> . Choi (2012) shows that generalized PC can provide a smaller forecasting error variance than PCA factors. 

However, the above solution is infeasible because the true variance matrix of idiosyncratic errors _Σe_ is unknown. A feasible generalized PC estimator is obtained by replacing _Σe_ with the estimated _Σ_<sup>ˆ</sup> _e_ . Two studies are considered that propose different _Σ_<sup>ˆ</sup> _e_ , Boivin and Ng (2006) and Forni et al. (2005). 

### _4. Weighted principal component (weighted PC)_ 

Boivin and Ng (2006) propose generating a two-step diagonal weight matrix. First, PCA factors are estimated. Second, generalized PC factors are estimated that solve (8) with a diagonal matrix of _Σ_<sup>ˆ</sup> _e_ , whose diagonal elements are the sample variance of estimated idiosyncratic error, _e_ ˆ _t_ in the first step. A similar idea is also considered in Jones (2001). 

1663 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

### _5. One-sided estimation_ 

Forni et al. (2005) propose one-sided estimation that uses the decomposition of the variance matrix of predictors, _ΣX_ = _ΣΛF_ + _Σe_ , where _ΣΛF_ is the variance of the common _Σ_ ˆ _ΛF_ , wherecomponent _Σ_ ˆ _ΛF_ is estimatedfrom Eq. (3)by. Thisthe dynamicgives _Σ_<sup>ˆ</sup> _e_ principal= _Σ_<sup>ˆ</sup> _X_ − component analysis of Forni, Hallin, Lippi, and Reichlin (2000), which is based on Eq. (1). More specifically, denote a consistent lag-window or periodogram-smoothing estimator of the _N_ × _N_ spectral density matrix of predictors _Σ_ ( _θ_ ) as _Σ_<sup>ˆ</sup> ( _θ_ ) for _θ_ ∈[− _π, π_ ]. The first _q_ eigenvalues and eigenvectors of _Σ_<sup>ˆ</sup> ( _θ_ ) provide estimates of the spectral density and variance matrix of the common component, _ΣΛF_ . In this paper, we estimate _Σ_<sup>ˆ</sup> ( _θ_ ) as 



where _w_ , _Γ_<sup>ˆ</sup> _u_ and _MT >_ 0 are a window function, the _u_ -lag sample cross-covariance matrix and truncation parameter, respectively. We use the window size _MT_ = _T_<sup>1</sup><sup>_/_2</sup> and the triangular window for _w_ . The one-sided estimation is studied, developed and used widely, including forecasting economic variables; see Barigozzi and Hallin (2017, 2020), Forni, Giovannelli, Lippi, and Soccorsi (2018), Forni, Hallin, Lippi, and Zaffaroni (2015, 2017) and Trucíos, Mazzeu, Hotta, Pereira, and Hallin (2021). 

### _Hybrid models_ 

While maximum likelihood estimation (MLE) of dynamic factor models was applied to small models (Geweke (1977), Geweke and Singleton (1981), Sargent, et al. (1977), Watson and Engle (1983) and Stock and Watson (1989)), hybrid methods estimate factors by combining the efficiency improvement of the state space approach with PCA that can be used with many predictors. This approach can be implemented in real-time, and both crosssectional and time-series averaging are considered in factor estimation, contrary to PCA, which solely considers cross-sectional averages. However, hybrid models rely on assumptions regarding factor structure and distribution of idiosyncratic errors because of the state space representation of factor models. Here, two hybrid estimation methods are considered, namely Doz et al. (2011) and Doz et al. (2012). A survey on the related literature in nowcasting can be found in Bańbura, Giannone, Modugno, and Reichlin (2013) and on factor estimation using Kalman filter and smoothing in Poncela, Ruiz, and Miranda (2021). 

### _6. Two-step estimation_ 

Doz et al. (2011) propose two-step estimation for the model in Giannone et al. (2008). First, PCA factors are obtained, and the model parameters are estimated using the PCA factors. Second, the factors are updated using the Kalman smoother. In this sense, the PCA factors and the corresponding parameters initiate the maximum likelihood estimation algorithm. The two-step estimation and framework of Giannone et al. (2008) are applied by Angelini et al. (2011), Bańbura and Rünstler (2011) and Hindrayanto, Koopman, and de Winter (2016). 

### _7. Quasi-maximum likelihood estimation (QMLE)_ 

Maximum likelihood estimation is not feasible for largedimensional data since it involves estimating too many parameters. Doz et al. (2012) propose first estimating the factors by MLE, assuming an exact factor model with zero correlation between idiosyncratic errors, where MLE is feasible. 

They show that the estimated factors are consistent for the true factor space, even when the true model is an approximate factor model. In this sense, their model is the quasi-maximum likelihood estimation (hereafter ‘‘QMLE’’) of White (1982). QMLE repeats the two-step estimation until convergence. Their approach has been widely applied and studied; see Banbura, Giannone, and Reichlin (2010), Bańbura and Modugno (2014) and Hindrayanto et al. (2016). 

### **3. Data and forecasting procedure** 

### _3.1. Data description and transformation_ 

This paper follows the forecasting schemes of Stock and Watson (2002b). The forecasting experiment mimics real-time forecasting of 148 monthly macroeconomic and financial target variables in the United States. Factors and parameters are estimated, and forecasts are made recursively at every time period. 

The dataset covers monthly variables from 1959:01 to 2019:12, containing 178 variables from FRED-MD (McCracken & Ng, 2016), FRED and ISM (Institute for Supply Management). The data set includes eight major categories, namely output and income (‘‘Output & Income’’) , labour market, housing, consumption, orders and inventories (‘‘Consumption’’), money and credit, interest and exchange rates (‘‘Int & Exch Rates’’), prices, and stock market: See Appendix B for additional detail. 

Four forecasting horizons, _h_ = 1 _,_ 6 _,_ 12 _,_ 24, are tested. The first out-of-sample forecast is made at 1970:01 for a _h_ -period ahead target variable at 1970:01+ _h_ . The forecasts are obtained by regressing _h_ -step-ahead target variable _y_<sup>_h_</sup> _t_ + _h_<sup>onregressorsat</sup><sup>_t_,whichmayincludefactors,</sup> lagged factors, and lagged target variables. Some variables are transformed to be stationary. For instance, real variables are assumed to be I(1) in logarithms. Since industrial production (IP) is a real variable, the following transformation is applied. 



In the main forecasting Eq. (5), _y_<sup>_h_</sup> _t_ + _h_<sup>and</sup><sup>_yt_from(10)</sup> are used as the target variable and lagged dependent variable, respectively. In contrast, price-related variables are assumed to be I(2) in logarithms. For example, CPI and other nominal variables are transformed to construct the target and lagged variables: 



1664 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

Then, the transformed variables are standardized to have unit variance and mean zero. Finally, the data are screened for outliers: Any observations whose values exceed ten times the interquartile range from the median are treated as missing values. Factors are estimated only from the balanced panel with 108 predictors. 

PLS and forecasting with targeted predictors require target variables while factors are estimated. However, some variables have missing values in their initial observations. Therefore, only variables with more than 80% of observations in the first factor estimation period are chosen as targets. Accordingly, there are 144 target variables for 1-, 6- and 12-month ahead forecasting, and 148 for 24-month ahead prediction. 

### _3.2. Parameter estimation and model selection_ 

At a given time _T_<sup>¯</sup> , the following procedure yields ˆ _y_<sup>_h_</sup> _T_ ¯ + _h_<sup>_._First,asequenceoffactors{ˆ</sup><sup>_Ft_}</sup><sup>_T_</sup> _t_<sup>¯</sup> =1<sup>areestimated,</sup> using all the available sample data { _xt_ }<sup>_T_</sup> _t_<sup>¯</sup> =1<sup>.Second,the</sup> estimated parameters, _δ_<sup>ˆ</sup> _h, β_<sup>ˆ</sup> _h_ ( _L_ ) and _γ_ ˆ _h_ ( _L_ ) are obtained by regressing _y_<sup>_h_</sup> _t_ + _h_<sup>onregressorsandestimatedfactors.</sup> The _δ_ ˆ _h_ +forecast _β_ ˆ _h_ ( _L_ ) _F_ ˆ _T_ ¯ +for _γ_ ˆ _hy_ ( _L_<sup>_h_</sup> _T_ ¯)+ _yhT_ ¯<sup>,</sup> .<sup>_y_ˆ</sup> Accordingly,<sup>_h_</sup> _T_ ¯ + _h_ |¯ _T_<sup>isconstructed</sup> differently<sup>as</sup> estimated<sup>_y_ˆ</sup><sup>_h_</sup> _T_ ¯ + _h_ |¯ _T_<sup>=</sup> factors lead to different forecasts. 

Regarding the parameter and factor estimation window, two forecasting schemes are examined: recursive and rolling estimation. Starting from 1970:01, both schemes forecast the _h_ -period ahead target variable at 1970:01+ _h_ . First, the recursive scheme expands the estimation window every month. Second, the rolling scheme uses a fixed estimation window of 10 years, following Molodtsova and Papell (2009), Stock and Watson (2007), Swanson (1998) and Forni et al. (2018), among many. Forecasting results from both estimation schemes are reported. 

Based on Eq. (5), three different forecasting equations are tested, where _k_ , _p_ and _m_ denote the number of contemporaneous factors, lagged dependent variables and lagged estimated factors, respectively. First, the equation termed DI includes only _k_ contemporaneous factors, where 1 ≤ _k_ ≤ 12, _m_ = 1, and _p_ = 0. The second forecasting equation is denoted DIAR, which combines DI forecast with the AR process. The DIAR model incorporates _k_ dimensional contemporaneous factors and _p_ lagged dependent variables. For the DIAR forecast, _m_ = 1, 0 ≤ _p_ ≤ 6 is chosen by BIC, and 1 ≤ _k_ ≤ 12. The last forecast is DIAR-LAG, in which _m_ lagged estimated factors are included in the DIAR model. In the DIAR-LAG model, 1 ≤ _m_ ≤ 3, 0 ≤ _p_ ≤ 6 are chosen by BIC, and 1 ≤ _k_ ≤ 4. 

All three forecasting equations involve choosing the number of contemporaneous factors, _k_ , in a certain range. Other parameters, such as _m_ and _p_ , are chosen by BIC if they are included. In this sense, decision rules are used to determine _k_ . At each time period, the number of factors is determined by decision rules and updated recursively. This experiment shows the predictive power of decision rules. 

### _3.3. Decision rules_ 

In this paper, decision rules are the methods that determine the number of estimated factors for forecasting. This experiment incorporates decision rules popularly used in practice: Bai and Ng (2002) (hereafter ‘‘BN’’), Onatski (2010) (hereafter ‘‘ON’’), Alessi et al. (2010) (hereafter ‘‘ABC’’), and Ahn and Horenstein (2013) (hereafter ‘‘AH’’), Bayesian Information Criteria implemented by Stock and Watson (2002b) (hereafter ‘‘BIC’’), as well as the supervised method proposed by Giovannelli and Proietti (2016) (hereafter ‘‘GP’’). Since the BN estimator requires a penalty function, four penalty functions are tested. BN− _p_ 1, BN− _p_ 2, BN− _p_ 3, and BN− _BIC_ denote BN estimators, using _ICp_ 1, _ICp_ 2, _ICp_ 3, and _BIC_ 3 of Bai and Ng (2002), respectively. Also, ABC− _L_ and ABC− _S_ are ABC estimators with large and small windows. Finally, Holm’s method is used for the GP estimator. 

Since some factor estimation methods involve distinct decision rules, three decision rules are applied only to certain factor estimation methods. First, ‘‘1-PLS’’ is forecasting with only the first PLS factor ( _k_ = 1 for all time series), suggested by Ahn and Bae (2022). Second, the GP estimator can be applied to certain cases. First, the GP estimator is only used for PCA or PCA-related estimation that ensures orthogonality between estimated factors. That is, PCA, targeted predictors, and Weighted PC (Rule B) explained in Section 4. Second, the GP estimator is only used in DI and DIAR models, as the original work of Giovannelli and Proietti (2016) does not consider the DIAR-LAG model. 

Third, one-sided estimation is applied in two versions: static with _k_ = _q_ and dynamic with _q_ ( _s_ + 1) ≤ _k_ . Dynamic one-sided estimation needs information about the number of dynamic factors, _q_ , and static factors, _k_ . Bai and Ng (2007) (hereafter ‘‘BN2007’’) propose a methodology that simultaneously determines both _q_ and _k_ ; hence, their method is only applied to dynamic one-sided forecasts. On the other hand, since the method of Hallin and Liška (2007) (hereafter ‘‘HL2007’’) estimates only _q_ , both versions are tested. Denote the estimated number of dynamic factors by HL2007 as _q_ ˆ _HL_ 2007. In the static model, we let ˆ _k_ = _qHL_ 2007. Second, the dynamic version is assuming ˆ _s_ = 1, so we determine _k_ as _k_ = 2 _qHL_ 2007. 

To summarize, BIC, BN, ON, ABC, and AH are applied to all the factor estimation methods except dynamic onesided estimation. In contrast, 1-PLS is only applied to PLS. Also, GP is used only for PCA, Targeted Predictors and Weighted PC (Rule B) in DI and DIAR models. Finally, BN2007 and HL2007 are applied only to the one-sided estimation. Among all the decision rules, BN− _p_ 1, BN− _p_ 2, BN− _p_ 3, ON, ABC and AH estimators are consistent for the true number of factors _r_ . Similarly, BN2007 and HL2007 are consistent for _q_ (and _r_ for BN2007, as it involves BN estimator for estimation of _r_ ). In contrast, 1-PLS, BN− _BIC_ , BIC and GP may not be consistent. For instance, 1-PLS is inconsistent unless _r_ = 1 or all the relevant factors that explain _y_ have the same asymptotic variance. 

1665 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

### **4. Empirical results** 

This section reports and interprets empirical results. All reported results are obtained in the recursive scheme unless mentioned otherwise. Relative mean squared error (RMSE) is used to measure the forecasting accuracy of factor-augment forecasts. RMSE here is defined as the mean squared error (MSE) of a method relative to that of an autoregressive model where the lag _p_ is determined by BIC (AR(BIC)). 



where _y_ ˜<sup>_h_</sup> _t_ + _h_ | _t_<sup>istheforecastbyAR(BIC)attime</sup><sup>_t_.RMSE</sup> larger than one implies that an AR forecast of the given target variable is better than the factor-augmented forecast. Therefore, a lower RMSE indicates greater forecasting improvements over an AR forecast. 

Next, Diebold and Mariano (1995) test (hereafter ‘‘DM’’) is implemented to compare the predictive accuracy difference between AR(BIC) and factor-augmented forecasts from a statistical point of view. The null hypothesis is that the given factor-augmented and AR(BIC) forecasts have equal forecast accuracy against the alternative of the factor-augmented forecast being more accurate than AR(BIC). The results are displayed in asterisks along with RMSEs. For<sup>∗</sup> _p <_ 0 _._ 1,<sup>∗∗</sup> _p <_ 0 _._ 05,<sup>∗∗∗</sup> _p <_ 0 _._ 01, the null hypothesis of equal predictive ability between the two is rejected based on the DM statistics, implying the significance under _α_ = 0 _._ 1, 0.05 and 0.01, respectively. 

Factor estimation methods are implemented as in the original work to the extent that the econometric model in this paper allows. For instance, Bai and Ng (2008) use softthresholding using the elastic net estimator of Zou and Hastie (2005), a convex combination of ridge and LASSO regression that satisfies the following equation. 



where _RSS_ is sum of squared residuals from a regression of _y_<sup>_h_</sup> _t_ + _h_<sup>onallavailableregressors.If</sup><sup>_λ_1islarger,the</sup> regression approaches LASSO, and when _λ_ 2 is larger, it approaches ridge regression. Bai and Ng (2008) report _λ_ 2 = 1 _._ 5 _,_ 0 _._ 5 _,_ 0 _._ 25. Following the original work, the three values of _λ_ 2 are implemented here, using the elastic net estimator of Zou and Hastie (2005). 

In contrast, Boivin and Ng (2006) try several weighting matrices used in (8). The two weighting matrices that outperform others are chosen here: Rule SWa and SWb. For Rule SWa, the weight matrix _Σ_<sup>ˆ</sup> _e_ is a diagonal matrix whose elements are the estimated variances of idiosyncratic errors, which is also considered in Jones (2001). For Rule SWb, the weight matrix is a diagonal matrix whose elements are the sample average of absolute values of estimated covariances between idiosyncratic errors. While the two rules focus on residuals, they also estimate PCA factors only from specific groups of predictors, not 

from the whole data. Four rules are tested, and the most predictive (Rule B) is used here. Rule B estimates PCA factors only from nominal variables, which corresponds to Category 5 (Money and Credit), 6 (Interest and Exchange Rates), and 7 (Prices) in this paper.<sup>1</sup> Therefore, the most predictive three rules in Boivin and Ng (2006) are implemented: Rule SWa and SWb for the weight matrix and Rule B that estimates PCA factors only from nominal variables. 

### _4.1. Major findings_ 

### _4.1.1. Strong forecasting performance of 1-PLS_ 

This section suggests which factor estimation method and decision rule provide the best predictions. Overall, 1- PLS often yields the best forecasting performance among all possible alternatives. 

First, as Ahn and Bae (2022) show theoretically and from simulation results, the number of PLS factors significantly affects forecasting performance, compared to other factor estimation methods such as PCA. Figs. 1 and 2 show how the number of PLS and PCA factors affects the mean RMSE over all the target variables, according to the forecasting horizon, forecasting model and forecasting scheme. 

The figures calculate the mean RMSE of each _k_ over all target variables. The figures reveal three implications for PLS. First, in contrast to PCA, PLS shows a more dramatic increase in Mean RMSE as the number of PLS factors increases in many situations. Also, 1-PLS tends to show the lowest mean RMSE than any other number of PLS factors. Therefore, the figures imply that the number of PLS factors should be chosen with care, supporting the importance of decision rules for PLS. 

Second, 2-PLS generally performs better than 1-PLS in the DI model under a recursive scheme, especially for shorter forecasting horizons of _h_ = 1 or 6. But even in this case, using three or more PLS factors shows worse forecasting performance. It is possible that 1-PLS may not be sufficient to capture enough dynamics of the target variable, especially when the lagged target variable is not incorporated (DI model) and on shorter forecasting horizons where dynamic matters ( _h_ = 1 or 6). 

Third, when _h_ is short, 1- or 2-PLS perform similarly across all models in rolling estimation. Moreover, 2-PLS slightly outperforms 1-PLS in the DIAR-LAG model at _h_ = 1. But as the forecasting horizon _h_ increases, overfitting of PLS becomes more severe on average, in contrast to recursive estimation, where overfitting of PLS becomes mitigated over _h_ . 

Considering that Figs. 1–2 highlight the importance of decision rules for PLS, Fig. 3 reports the performance of each decision rule for PLS and PCA from various perspectives. More specifically, Fig. 3 shows the percentage of 

1 Boivin and Ng (2005) estimate three PCA factors from nominal variables in Rule B estimation. However, the number of factors can also be determined by decision rules for Rule B estimation. Forecasting with targeted predictors and Rule B estimates PCA factors only from subsets of predictors. Therefore, when decision rules are applied for these methods, the number of factors is decided using only these subsets of predictors, not the whole data. 

1666 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 





**Fig. 1.** Mean RMSE of _k_ -PCA according to the forecasting scheme. 

target variables that a decision rule outperforms all others for each forecasting model. The horizontal axis denotes the decision rules introduced in Section 3.3, and the vertical axis represents the percentage that the corresponding decision rule outperforms. 

For PLS, the decision rule that gives the best results most frequently is shown by a dark red bar with the name of the decision rule bolded. For PCA, each forecasting model’s three most dominant decision rules are shown 

in dark red bars with their names in bold. The figures imply that PCA does not have a strictly dominant decision rule for all forecasting models. For instance, _BN_ − _BIC_ is the second best method in the DIAR model but not in the DI and DIAR-LAG model. _BN_ − _p_ 3 exhibits good performance in the DI model but not in the DIAR and DIAR-LAG models. _BN_ − _p_ 1 is the second-dominant decision rule in the DIAR-LAG model but not in the DI and DIAR models. However, 1-PLS is the dominant decision 

1667 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 





**Fig. 2.** Mean RMSE of _k_ -PLS according to the forecasting scheme. 

rule in all three forecasting models. For all models, 1-PLS gives the best results for around 50% of all target variables. Other decision rules can give better forecasting results than 1-PLS, but the difference is significant compared to the PCA case. Similar results are obtained under rolling estimation, demonstrated in Fig. 6 in Appendix A. 

Next, Table 2 compares the relative forecasting accuracy of 1-PLS among all the possible alternatives for _h_ = 

1 _,_ 6 _,_ 12 _,_ 24. The left two columns of Table 2 show the top 5 methods, with decision rules in parentheses that perform best most frequently. On the other hand, the methods that perform closest to the best possible method on average are shown in the right two columns. The ‘Ratio’ of a given method represents _RMSE_ ( _Method_ ) _/RMSE_ ( _Best_ ) − 1, namely the percentage difference between the RMSEs of the best and the corresponding method. Therefore, 

1668 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 



**Fig. 3.** Percentage of target variables that a decision rule outperforms 

over the rest of the decision rules using the forecasting model: PLS and PCA. 

Mean(Ratio) denotes the average percentage difference between the best forecasts and the given method. Table 2 considers all target variables and forecasting models. 

Table 2 documents that 1-PLS gives the best results most frequently in forecasting around 6%–24% of all target variables, as the left two columns show. The second-best 

1669 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table 2** 

Top 5 methods, PLS with other decision rules excluded. 

||Methods Giving the Best Results Mo|st Frequently|Methods Giving Results Closest|to the Best|
|---|---|---|---|---|
||Methods|Percentage (%)|Methods|Mean(Ratio)|
||**1-PLS**|**6.02**|OS-Static(BIC)|0.06|
||Targeted Predictors, _λ_= 1_._5(AH)|4.17|OS-Static(BN-p3)|0.062|
|_h_ 1|OS-Dynamic(HL2007)|3.47|Targeted Predictors, _λ_= 1_._5(BIC)|0.065|
|=|Weighted PC, Rule B(GP)|3.24|QMLE(BIC)|0.066|
||PCA(GP)|2.55|Targeted Predictors, _λ_= 0_._5(BIC)<br>**1-PLS**|0.069<br>**0.232**|
||**1-PLS**|**16.67**|Targeted Predictors, _λ_= 1_._5(BIC)|0.1|
||PCA(BN-BIC)|4.86|PCA(BIC)|0.103|
|_h_=6|Targeted Predictors, _λ_= 0_._25(BN-BIC)|3.24|OS-Static(BIC)|0.105|
||Weighted PC, Rule B(GP)|3.24|Targeted Predictors, _λ_= 0_._5(BIC)|0.105|
||Weighted PC, Rule B(BIC)|3.01|Targeted Predictors, _λ_= 0_._25(BIC)<br>**1-PLS**|0.107<br>**0.142**|
||**1-PLS**|**19.21**|**1-PLS**|**0.102**|
||PCA(BN-BIC)|4.4|PCA(BN-BIC)|0.121|
|_h_= 12|OS-Dynamic(HL2007)|4.4|PCA(BIC)|0.121|
||Weighted PC, SWa(AH)|3.24|PCA(ABC-L)|0.121|
||Weighted PC, Rule B(BIC)|2.78|PCA(ABC-S)|0.124|
||**1-PLS**|**24.1**|**1-PLS**|**0.076**|
||Weighted PC, SWa(ON)|4.73|PCA(BN-BIC)|0.128|
|_h_= 24|Weighted PC, Rule B(AH)|2.7|PCA(ABC-L)|0.13|
||Targeted Predictors, _λ_= 0_._5(AH)|2.48|Weighted PC, SWb(ABC-L)|0.134|
||Targeted Predictors, _λ_= 1_._5(AH)|2.48|Two-step(BN-BIC)|0.136|



This table presents the top 5 methods for each forecasting horizon giving the best results most frequently and giving results closest to the best results on average in the left and right columns respectively. 1-PLS is represented in bold and dashed line represents the case that 1-PLS is not the top 5 methods. PLS with other decision rules are excluded. For each forecasting horizon, all target variables in DI, DIAR and DIAR-LAG models are considered. 

methods tend to vary depending on the forecasting horizon. Also, the results indicate that 1-PLS delivers the best forecasts more frequently and performs closer to the best methods as the horizons extend. For instance, 1-PLS is the best method in forecasting around 6% of target variables at _h_ = 1. In this case, 1-PLS exhibits 23% larger RMSE than the best possible method, on average. While 1-PLS still provides the best results most frequently, Mean(Ratio) is relatively larger on a shorter horizon. This result implies that 1-PLS tends to perform best for many target variables in a shorter horizon but may have weaker forecasting results for others, increasing Mean(Ratio). 

However, the Mean(Ratio) value of 1-PLS decreases with longer forecasting horizons. All methods except 1- PLS show higher ‘Ratio’ on average when forecasting longrun target variables. For instance, when forecasting 24month ahead variables, 1-PLS is the best method for 24% target variables and shows only 7% larger RMSE than the best possible method. This can be explained by evidence that 1-PLS produces the best results more frequently given longer forecasting horizons. Since the best method has a zero Ratio value for the target variable, Mean(Ratio) decreases as 1-PLS becomes the best method more frequently. The same results can be found in Table 14 in Appendix A obtained under the rolling scheme: 1-PLS again remains one of the most dominating methods. 

The predictive improvement of 1-PLS over longer _h_ may be due to its supervised factor estimation strategy. Note that an unsupervised method, for instance, PCA, estimates factors regardless of the forecasting horizon _h_ . As a result, even when _h_ becomes larger, the factors used 

for forecasting remain the same for unsupervised methods. However, since PLS is estimated by the covariance between the target _y_<sup>_h_</sup> _t_ + _h_<sup>andpredictors</sup><sup>_xt_,as</sup><sup>_h_extends,</sup> the relative predictive gain of PLS can become larger. 

More detailed results of the relative forecasting accuracy of 1-PLS are presented in Tables 15–19 in Appendix A. Tables 3 and 4 decompose the forecasting results across the eight categories, focusing on 1-PLS. More specifically, the tables break down the results of 1-PLS by category that a target variable belongs to. While Table 3 includes PLS with other decision rules than 1-PLS, Table 4 excludes PLS with other decision rules. All forecasting horizons, target variables and forecasting models are considered. The percentage columns present the percentage of target variables in a given category in which 1-PLS achieves the best results among all the alternatives. The Mean(Ratio) reports the average predictive difference between the best possible method and 1-PLS in the category. 

Table 3 documents that 1-PLS delivers the best forecasts more frequently for real variables under the recursive scheme. For example, 1-PLS provides the best prediction for around 26% of the target variables in the Output and Income category. On the other hand, 1-PLS tends to show better forecasting results for nominal variables under the rolling scheme. When a PLS with different decision rules than 1-PLS is excluded, the relative improvement of 1-PLS over the remaining competing methods becomes more evident in Table 4. Predictive improvement is greater for nominal variables. For instance, 1-PLS delivers the best results in forecasting 50% of price-related variables under the rolling scheme. 

1670 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table 3** 

1-PLS & best <u>possible</u> results by category, PLS with all decision rules. 

||Recursive||Rolling||
|---|---|---|---|---|
||Percentage (%)|Mean(Ratio)|Percentage (%)|Mean(Ratio)|
|Overall|11.15|0.15|9.71|0.26|
|1. Output & Income|25.93|0.06|17.13|0.13|
|2. Labor Market|13.24|0.16|8.58|0.24|
|3. Housing|20.93|0.63|10.08|1.07|
|4. Consumption|7.92|0.15|3.75|0.31|
|5. Money and Credit|5|0.08|9.44|0.13|
|6. Int & Exch Rates|7.54|0.11|14.68|0.19|
|7. Prices|3.79|0.09|4.55|0.15|
|8. Stock Market|0|0.08|17.65|0.08|



This table breaks down the results of 1-PLS by category that a target variable belongs to, according to forecasting scheme. The Percentage represents the percentage of target variables that 1-PLS achieves the best results among all the alternatives in a given category. Mean(Ratio) reports the average predictive difference between the best possible method and 1-PLS. PLS with other decision rules are all considered. All target variables, forecasting horizons and forecasting models (1,740 combinations) are considered. 

**Table 4** 

1-PLS & best <u>possible</u> results by category, PLS with other decision rules excluded. 

||Recursive||Rolling||
|---|---|---|---|---|
||Percentage (%)|Mean(Ratio)|Percentage (%)|Mean(Ratio)|
|Overall|16.55|0.14|29.54|0.21|
|1. Output & Income|39.35|0.04|32.41|0.1|
|2. Labor Market|18.38|0.13|37.25|0.17|
|3. Housing|27.13|0.61|12.4|1.06|
|4. Consumption|13.33|0.14|11.67|0.3|
|5. Money and Credit|7.22|0.07|24.44|0.07|
|6. Int & Exch Rates|9.13|0.11|26.19|0.15|
|7. Prices|9.47|0.07|47.35|0.05|
|8. Stock Market|0|0.07|25.49|0.07|



This table breaks down the results of 1-PLS by category that a target variable belongs to, according to forecasting scheme. The Percentage represents the percentage of target variables that 1-PLS achieves the best results among all the alternatives in a given category. Mean(Ratio) reports the average predictive difference between the best possible method and 1-PLS. PLS with other decision rules are excluded. All target variables, forecasting horizons and forecasting models (1,740 combinations) are considered. 

Next, the predictive performance of 1-PLS is examined in Table 5 from a statistical point of view. The table lists how often 1-PLS forecasts show significant DM statistics under different significance levels _α_ , for _α_ = 0 _._ 1, 0.05 and 0.01, by forecasting scheme and target variable’s category. For all _α_ , DM statistics of 1-PLS under the rolling scheme are more often significant for variables in the labour market (2. Labor Market) and housing (3. Housing). Also, rolling estimation demonstrates improvement in forecasting nominal variables: 5. Money and Credit, 7. Prices and 8. Stock Market. The improvement can also be attributed to a reduction in parameter instability. For instance, the parameter instability of economic variables is studied by many works, including but not limited to Giacomini and White (2006), Stock and Watson (1996, 2007, 2009) and Inoue, Jin, and Rossi (2017), among others. Since nominal variables are more prone to instabilities, the forecasting improvement of 1-PLS in rolling estimation can be explained. 

Finally, Tables 6–7 compare 1-PLS and PCA. These results are particularly important given the widespread use 

of PCA. Only PCA and 1-PLS are considered here. Table 6 compares the predictive ability of 1-PLS and _k_ -PCA for all target variables, according to the forecasting model, where _k_ is fixed as 1 ≤ _k_ ≤ _kmax_ . Each forecasting model considers all target variables and forecasting horizons, giving the 580 variable-horizon combinations. Frequency counts how often the given method achieves the minimum RMSE among the 580 combinations. The percentage is the frequency divided by 580 and multiplied by 100. Table 6 demonstrates that 1-PLS outperforms other PCA forecasts with given _k_ = 1 _,_ 2 _, . . . , kmax_ , around 230 times out of 580 combinations (around 40%). Similarly, Table 7 compares 1-PLS and PCA with decision rules, from PCA : _BIC_ to PCA : _GP_ by forecasting model. Again, the table shows that 1-PLS dominates PCA forecasts with ten decision rules, around 210 times out of 580 combinations on average. 

The Fluctuation test proposed by Giacomini and Rossi (2010) is implemented to compare predictive accuracy between 1-PLS and PCA in the presence of possible instabilities. This test analyzes the change in relative performance between 1-PLS and PCA over time in the sample 

1671 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table 5** 

Significant DM statistics of 1-PLS by category. 

||Method|Recursive||Rolling||
|---|---|---|---|---|---|
|||Frequency|Percentage (%)|Frequency|Percentage (%)|
||Overall|597|34.31|823|47.3|
||1. Output & Income|153|70.83|125|57.87|
||2. Labor Market|218|53.43|306|75|
||3. Housing|18|13.95|30|23.26|
|_α_ = 0_._1|4. Consumption|76|31.67|70|29.17|
||5. Money and Credit|22|12.22|55|30.56|
||6. Int & Exch Rates|94|37.3|70|27.78|
||7. Prices|14|5.3|154|58.33|
||8. Stock Market|2|3.92|13|25.49|
||Overall|429|24.66|682|39.2|
||1. Output & Income|109|50.46|83|38.43|
||2. Labor Market|173|42.4|291|71.32|
||3. Housing|11|8.53|22|17.05|
|_α_ = 0_._05|4. Consumption|48|20|51|21.25|
||5. Money and Credit|11|6.11|44|24.44|
||6. Int & Exch Rates|70|27.78|52|20.63|
||7. Prices|7|2.65|131|49.62|
||8. Stock Market|0|0|8|15.69|
||Overall|193|11.09|486|27.93|
||1. Output & Income|38|17.59|43|19.91|
||2. Labor Market|116|28.43|242|59.31|
||3. Housing|1|0.78|9|6.98|
|_α_ = 0_._01|4. Consumption|12|5|35|14.58|
||5. Money and Credit|4|2.22|33|18.33|
||6. Int & Exch Rates|20|7.94|31|12.3|
||7. Prices|2|0.76|90|34.09|
||8. Stock Market|0|0|3|5.88|



This table breaks down the DM statistics results of 1-PLS by category that a target variable belongs to, according to significance level ( _α_ ) and forecasting scheme. The Frequency represents how often 1-PLS shows significant DM statistics in forecasting a target variable in a given category. The Percentage divides the Frequency by the number of target variables belong to the category. Note that summing all values in the frequency columns over the eight categories is identical to the frequency in ‘Overall’. All target variables, forecasting horizons and forecasting models (1,740 combinations) are considered. 

under the rolling scheme. Fig. 4 reports the (Giacomini & Rossi, 2010) Fluctuation test on 1-PLS and PCA with the best possible decision rule for forecasting 1. Industrial Production and 2. CPI at _h_ = 1 and _h_ = 12 in rolling estimation. 

The blue line of G-R test statistics graphically demonstrates the relative measure of local performance over the sample path. The null hypothesis is that the two models, 1-PLS and PCA, perform equally well at each point of time, against the alternative that 1-PLS outperforms PCA at some point in time. When the test statistic in the blue line is above the red critical value line, 1-PLS significantly perform better than PCA forecasts in Fig. 4. 

Several empirical implications can be drawn from the figures. First, we are not able to reject the null hypothesis in forecasting the Industrial Production during the forecasting period for _h_ = 1 and _h_ = 12. In contrast, 1-PLS performs significantly better forecasting CPI than PCA(Best). Especially when forecasting 12 months ahead of CPI, 1-PLS shows considerable improvement upon PCA(BEST) for almost all periods. This finding also aligns with Fuentes et al. (2015), which indicates that PLS factors tend to forecast inflation based on CPI better than PCA or Targeted Predictor forecasts. 

Why does 1-PLS perform better than PCA? Again, it can be explained by its supervised method that estimates the 

factors with the highest covariance with the target variable. To illustrate this difference in detail, Fig. 5 shows the contribution of each predictor to 1-PLS and PCA factors in heat maps. Specifically, the two graphs show the squared loadings for _k_ -PCA and 1-PLS, where _k_ = 1 _, . . . ,_ 12. Since PLS factors and loadings vary between forecasting horizons _h_ and target variables, we select eight target variables in every category from 1. Real Personal Income to 8. S&P 500. The number next to the target variable’s name denotes the category that it belongs to. While the top graph shows the squared loadings of _k_ -PCA, the graph at the bottom of Fig. 5 illustrates the squared loadings of 1-PLS of the eight variables for _h_ = 12. 

Fig. 5 shows that 1-PLS and PCA loadings can be clearly distinguished. First, real variables in the first four categories mainly load on the first PCA factor. In contrast, the second, third, fourth and fifth PCA factors have the largest loadings on variables belong to 6. Interest and Exchange Rates, 7. Prices, 8. Stock Market and 1. Output & Income categories, respectively. However, the second graph of Fig. 5 shows that the 1-PLS factors of certain target variables often have the largest loadings on predictors from the same category. For instance, the target variables of Nonagriculture Employment, Housing starts, Monetary Base, 10-Year Treasury Rate, CPI and S&P 500 are explained more by predictors from the same category. 

1672 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table 6** 

1-PLS & _k_ -PCA. 

||DI||DIAR||DIAR-LAG||
|---|---|---|---|---|---|---|
||Frequency|Percentage (%)|Frequency|Percentage (%)|Frequency|Percentage (%)|
|1-PLS|**246**|**42.41**|**209**|**36.03**|**230**|**39.66**|
|1-PCA|59|10.17|88|15.17|99|17.07|
|2-PCA|19|3.28|33|5.69|74|12.76|
|3-PCA|30|5.17|46|7.93|72|12.41|
|4-PCA|36|6.21|62|10.69|105|18.1|
|5-PCA|20|3.45|28|4.83|||
|6-PCA|14|2.41|26|4.48|||
|7-PCA|30|5.17|35|6.03|||
|8-PCA|11|1.9|8|1.38|||
|9-PCA|13|2.24|21|3.62|||
|10-PCA|12|2.07|6|1.03|||
|11-PCA|23|3.97|3|0.52|||
|12-PCA|67|11.55|15|2.59|||



1-PLS and _k_ -PCA, _k_ = 1 _,_ 2 _, . . . ,_ 12, for all target variables in 1-, 6-, 12- and 24-month ahead DI, DIAR and DIAR-LAG forecasting are considered. For DIAR-LAG, the maximum _k_ is 4, so DIAR-LAG _k_ -PCA forecasts with 4 _< k_ are left empty. The frequency is how often the given method achieves the minimum RMSE in 580 variable-horizon combinations. The percentage is the frequency divided by 580 and multiplied by 100. 

**Table 7** 

1-PLS & PCA with decision rules. 

||DI||DIAR||DIAR-LAG||
|---|---|---|---|---|---|---|
||Frequency|Percentage (%)|Frequency|Percentage (%)|Frequency|Percentage (%)|
|1-PLS|**216**|**37.24**|**202**|**34.83**|**198**|**34.14**|
|_PCA_: _BIC_|37|6.38|28|4.83|48|8.28|
|_PCA_: _BN_ −_p_1|25|4.31|30|5.17|62|10.69|
|_PCA_: _BN_ −_p_2|14|2.41|15|2.59|35|6.03|
|_PCA_: _BN_ −_p_3|70|12.07|9|1.55|5|0.86|
|_PCA_: _BN_ −_BIC_|34|5.86|77|13.28|38|6.55|
|_PCA_: _AH_|12|2.07|42|7.24|50|8.62|
|_PCA_: _ON_|42|7.24|81|13.97|75|12.93|
|_PCA_: _ABC_ −_L_|27|4.66|41|7.07|38|6.55|
|_PCA_: _ABC_ −_S_|27|4.66|20|3.45|31|5.34|
|_PCA_: _GP_|76|13.1|35|6.03|||



1-PLS and PCA with decision rules, for all target variables in 1-, 6-, 12- and 24-month ahead DI, DIAR and DIAR-LAG forecasting are considered. The frequency is how often the given method achieves the minimum RMSE in 580 variable-horizon combinations. The percentage is the frequency divided by 580 and multiplied by 100. As GP is not used in DIAR-LAG model, the corresponding entries remain empty. 

Second, it is interesting that the 1-PLS loadings reveal economic relationships between several variables. For instance, Real Consumption has the highest loadings from variables in 6. Interest and Exchange Rates: this observation is consistent with the well-known relationship between real interest rates and household consumption patterns. Also, the CPI has the highest loadings from the Real M2 Money Stock (M2REAL), as expected. Therefore, Fig. 5 emphasizes the differences in factor estimation strategies between PLS and PCA and hence explains the stronger forecasting performance of PLS. 

To summarize, 1-PLS shows the strongest forecasting performance among all the possible alternatives. The significant predictive accuracy of PLS in these extensive experiments can be explained by its factor estimation strategy that estimates factors having the maximum covariance with a target variable, as explained in Table 1.<sup>2</sup> 

> 2 Then why the first PLS factor, in particular, shows the best forecasting performance than any other number of the PLS factors? Ahn 

### _4.1.2. Decision rules and forecasting performance_ 

It may be unclear how many contemporaneous factors should be used in forecasting. Using the available data, researchers should often decide the number of factors according to the research design. Accordingly, this section evaluates the performance of decision rules introduced in Section 3.3. 

The forecasting results with all the decision rules and factor estimation methods are summarized in Tables 8 to 9 for the eight variables in Stock and Watson (2002b) by forecasting horizons. The RMSE panel compares the RMSEs between the best method and 1-PLS. For<sup>∗</sup> _p <_ 0 _._ 1, 

and Bae (2022) gives some possible explanation of this finding as the ill-conditioned properties of Vandermonde matrices. They show that theoretically, the first _R_ number of PLS factors asymptotically estimates _Gt_ in Section 2.2, but under rotation of Vandermonde matrices. It is well known that the Vandermonde matrices are ill-conditioned (see Dax (2017)), implying that in the finite sample, the first PLS factor may explain most of the forecasting power that the rest of the PLS factors have. 

1673 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table 8** 

DIAR forecasts, real variables. 

||RMSE: Best vs 1-PLS||||
|---|---|---|---|---|
||_h_= 1|_h_= 6|_h_= 12|_h_= 24|
|Industrial Production|Best<br>0.86<br>1-PLS<br>0.876|0.727<br>0.745|0.684|0.679|
||Name: Best Method||||
||TP, _λ_= 0_._5<br>(BN-BIC)|PCA<br>(ON)|1-PLS|1-PLS|
||RMSE: Best vs 1-PLS||||
||_h_= 1|_h_= 6|_h_= 12|_h_= 24|
|PersonalIncome|Best<br>0.943|||0.812|
||1-PLS<br>0.952|0.771|0.7|0.818|
||Name: Best Method||||
||PCA|1-PLS|1-PLS|PLS|
||(BN-BIC)|||(ON)|
||RMSE: Best vs 1-PLS||||
||_h_= 1|_h_= 6|_h_= 12|_h_= 24|
|Mfg & Trade Sales|Best<br>0.9|0.679|0.623|0.703|
||1-PLS<br>0.932|0.683|0.646|0.77|
||Name: Best Method||||
||PCA|PLS|WPC, SWa|WPC, SWa|
||(AH)|(ON)|(ON)|(ON)|
||RMSE: Best vs 1-PLS||||
||_h_= 1|_h_= 6|_h_= 12|_h_= 24|
|Nonag.Employment|Best||0.768|0.768|
||1-PLS<br>0.848|0.792|0.79|0.779|
||Name: Best Method||||
||1-PLS|1-PLS|PCA|OS-S|
||||(BN-BIC)|(BIC)|



Tables 8–9 summarize the forecasting accuracy of all factor estimation methods with decision rules by forecasting horizons. The RMSE panel shows the relative mean squared errors (RMSE) of the best possible forecast and 1-PLS. The Name panel presents the name of the best method. The eight target variables, 1. Industrial Production to 8. Producer Price Index, are forecasted by _h_ -month-ahead DIAR forecasting. For<sup>∗</sup> _p <_ 0 _._ 1,<sup>∗∗</sup> _p <_ 0 _._ 05,<sup>∗∗∗</sup> _p <_ 0 _._ 01, the null hypothesis of equal predictive ability between 1-PLS and best method is rejected based on Diebold–Mariano test. 

> ∗∗ _p <_ 0 _._ 05, ∗∗∗ _p <_ 0 _._ 01, the null hypothesis of equal predictive ability between 1-PLS and the best forecast is rejected based on Diebold–Mariano test. The Name panel shows the name of the best method. 

The two tables show that 1-PLS provides the best forecasts most often, in 25% of the variable-horizon combinations. Even when 1-PLS does not produce the best results, the predictive difference between the best method and 1- PLS is usually not statistically significant. Second, the two tables imply that even when we restrict our attention to the eight variables, the same factor estimation method can provide fairly different forecasts depending on the decision rules. 

Additionally, the determined number of factors varies significantly across decision rules. Table 10 reports summary statistics of the determined number of static and dynamic factors, _k_<sup>ˆ</sup> and _q_ ˆ, by decision rules. The table shows the mean, standard deviation, maximum, and minimum of recursively determined _k_<sup>ˆ</sup> and _q_ ˆ. _k_<sup>ˆ</sup> varies significantly across decision rules, from an average minimum of 1.34 to a maximum of 12. Even when the same decision rule is applied, different specifications of the rule, such as the choice of a penalty function ( _k_<sup>ˆ</sup> _BN_ ) or tuning parameter ( _k_<sup>ˆ</sup> _ABC_ ), results in quite different numbers of factors. 

The number of factors also widely differs among decision methods that consistently estimate the true number of factors. 

Tables 11 and 12 describe the relative forecasting performances of decision rules for a given factor estimation method. In general, no specific decision rule tends to deliver the best results for many target variables for most factor estimation methods. Table 11 reports the percentage of target variables that a decision rule outperforms all the rest of the decision rules for PCA by category. For example, _k_<sup>ˆ</sup> _ON_ yields the best results for 38.89% of target variables in the output and income category when PCA factors are used for forecasting. _k_<sup>ˆ</sup> _ON_ also outperforms in forecasting consumption and stock market variables. However, _k_<sup>ˆ</sup> _AH_ appears to dominate in the housing category,ˆ _k_<sup>ˆ</sup> _BN_ − _BIC_ in variables related to the labour market andˆ ˆ _kABC_ − _L_ in interest or exchange rate variables. _kGP_ and _kBIC_ perform well in forecasting price-related variables and money and credit variables, respectively. 

When taken together, the results may suggest that a target variable can be governed by a subset of factors that affect predictors. These relevant factors can vary across target variables and may not always best explain predictors, as Kelly and Pruitt (2015) and Ahn and Bae 

1674 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table 9** 

DIAR forecasts, <u>price-related</u> variables. 

RMSE: Best vs 1-PLS 

|_h_= 1|_h_= 6|_h_= 12|_h_= 24|
|---|---|---|---|
|CPI<br>Best<br>0.939<br>1-PLS<br>0.998|0.966<br>0.972|0.883|0.781<br>0.796|
|Name: Best Method||||
|TP, _λ_= 1_._5<br>(BN-BIC)|PLS<br>(ON)|1-PLS|TP, _λ_= 1_._5<br>(AH)|
|RMSE: Best vs 1-PLS||||
|_h_= 1|_h_= 6|_h_= 12|_h_= 24|
|Consumption Deflator<br>Best<br>0.959<sup>∗∗∗</sup><br>1-PLS<br>1.035|1.016<br>1.019|0.968<br>0.974|0.842<br>0.88|
|Name: Best Method||||
|TP, _λ_= 1_._5<br>(BN-BIC)|PLS<br>(BN-BIC)|WPC, SWa<br>(BN-BIC)|OS-S<br>(BN-BIC)|
|RMSE: Best vs 1-PLS||||
|_h_= 1|_h_= 6|_h_= 12|_h_= 24|
|CPI exc. Food<br>Best<br>0.951<br><br>||0.899<br>|0.829<br>|
|1-PLS<br>1.019|0.98|0.91|0.839|
|Name: Best Method||||
|WPC, SWb|1-PLS|TP, _λ_= 0_._25|PLS|
|(BN-p1)||(AH)|(AH)|
|RMSE: Best vs 1-PLS||||
|_h_= 1|_h_= 6|_h_= 12|_h_= 24|
|Producer Price Index<br>Best<br>0.963<sup>∗∗∗</sup>|0.993|0.959|0.879|
|1-PLS<br>1.013|1.028|0.995|0.928|
|Name: Best Method||||
|TP, _λ_= 0_._5<br>(AH)<br>**able 10**<br>tatistics of number of factors determined by decision rules.|WPC, Rule B<br>(BN-p2)|PCA<br>(GP)|WPC, Rule B<br>(BN-BIC)|
|Mean<br>Std<br>Max<br>Min||Mean<br>Std|Max<br>Min|
|ˆ_kBN_−_p_1<br>8.7<br>1.19<br>11<br>4|ˆ_kON_|1.34<br>0.49|3<br>1|
|ˆ_kBN_−_p_2<br>6.91<br>2.24<br>10<br>2|ˆ_kABC_−_L_|4.96<br>0.87|8<br>2|
|ˆ_kBN_−_p_3<br>12<br>0<br>12<br>12<br>ˆ|ˆ_kABC_−_S_|8.19<br>0.87|11<br>5|
|_kBN_−_BIC_<br>3.3<br>0.6<br>4<br>2|ˆ_qBN_2007|5.25<br>1.5|7<br>2|
|ˆ_kAH_<br>1.72<br>0.45<br>2<br>1|ˆ_qHL_2007|2.37<br>0.56|4<br>1|



**Table 10** 

Statistics of number of factors determined by decision rules. 

Statistics of all decision rules are obtained from DIAR model. _q_ ˆ _BN_ 2007 and _r_ ˆ _BN_ 2007 denote the estimated number of dynamic and static factors, _q_ and ˆ ˆ _r_ by Bai and Ng (2007). Note that _rBN_ 2007 is not displayed because _rBN_ 2007 = _k_<sup>ˆ</sup> _BN_ − _p_ 2. 

#### **Table 11** 

Percentage of target variables that a decision rule outperforms the rest decision rules: PCA. 

||ˆ_kBIC_|ˆ_kBN_−_p_1|ˆ_kBN_−_p_2|ˆ_kBN_−_p_3|ˆ_kBN_−_BIC_|ˆ_kAH_|ˆ_kON_|ˆ_kABC_−_L_|ˆ_kABC_−_S_|ˆ_kGP_|
|---|---|---|---|---|---|---|---|---|---|---|
|1. Output & Income|5.56|9.26|5.09|6.02|15.28|6.48|**38.89**|5.09|1.85|6.48|
|2. Labor Market|12.25|4.66|5.88|6.62|**26.96**|3.19|17.89|10.78|5.15|6.62|
|3. Housing|7.75|3.1|4.65|24.03|0|**34.11**|16.28|5.43|0.78|3.88|
|4. Consumption|4.58|12.92|3.33|5|8.75|14.58|**23.75**|4.58|14.58|7.92|
|5. Money and Credit|**21.11**|6.11|2.22|1.11|15|9.44|18.33|14.44|3.33|8.89|
|6. Int & Exch Rates|9.52|12.7|8.73|7.14|13.49|6.75|13.49|**13.89**|11.11|3.17|
|7. Prices|9.09|14.02|6.44|9.85|4.92|3.41|17.42|3.41|7.95|**23.48**|
|8. Stock Market|3.92|9.8|0|3.92|11.76|0|**50.98**|7.84|0|11.76|



This table shows the percentage of target variables in a category that a given decision rule delivers the best result in forecasting using PCA. For a given category, a decision rule that gives the best result most frequently is denoted in **bold** . All target variables in 1-, 6-, 12- and 24-month ahead DI, DIAR and DIAR-LAG forecasting are considered. 

1675 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 





**Fig. 4.** Fluctuation test: 1-PLS and PCA(BEST) at _h_ = 1 and _h_ = 12 for 1. industrial production and 2. CPI. _Source:_ Giacomini and Rossi (2010). 

(2022) suggest. In other words, some elements in _β_ in the main econometric model (3) can be zero, while the corresponding factors affect the predictors _xt_ . Therefore, the PCA factors that explain most variations of predictors 

do not necessarily best predict the target variables. Incorporating weak PCA factors that explain less variation in predictors can produce better predictions for certain target variables. 

1676 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 







**Fig. 5.** Heat map of squared factor loadings: PCA and PLS. 

In contrast, Table 12 shows that 1-PLS tends to be a significantly dominant decision rule for PLS. For all the eight categories, 1-PLS delivers the best forecasting performance most frequently. For most categories, 1-PLS is the best decision rule for around 60% of target variables. It is also shown that theoretically, PLS estimates the relevant factor space with priority rather than the set of 

factors that only govern predictors (Ahn and Bae (2022) and Kelly and Pruitt (2015)). There can be additional predictive gains as additional PLS factors are included, suggested as _k_<sup>ˆ</sup> _ON_ , but those gains are often small in these typical macro data. 

Another notable finding is that a consistently estimated number of factors may not always result in the 

1677 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table 12** 

Percentage of target variables that a decision rule outperforms the rest decision rules: PLS. 

||1-PLS|ˆ_kBIC_|ˆ_kBN_−_p_1|ˆ_kBN_−_p_2|ˆ_kBN_−_p_3|ˆ_kBN_−_BIC_|ˆ_kAH_|ˆ_kON_|ˆ_kABC_−_L_|ˆ_kABC_−_S_|
|---|---|---|---|---|---|---|---|---|---|---|
|1. Output & Income|**57.87**|0|0|0.46|0|20.83|7.87|9.72|1.39|1.85|
|2. Labor Market|**55.88**|0.49|0.98|2.21|0.49|10.29|8.09|17.4|3.43|0.74|
|3. Housing|**45.74**|15.5|2.33|8.53|8.53|3.88|0|6.98|6.98|1.55|
|4. Consumption|**67.92**|0|0.42|0|0.42|8.33|11.25|10.83|0.42|0.42|
|5. Money and Credit|**58.33**|1.11|0|7.78|0.56|11.11|8.33|10.56|2.22|0|
|6. Int & Exch Rates|**51.59**|0|0|1.19|0|4.76|10.32|31.75|0|0.4|
|7. Prices|**31.82**|0.38|1.14|16.67|0|24.62|4.17|13.26|6.44|1.52|
|8. Stock Market|**54.9**|7.84|0|7.84|0|3.92|1.96|23.53|0|0|



This table shows the percentage of target variables in a category that a given decision rule delivers the best result in forecasting using PLS. For a given category, a decision rule that gives the best result most frequently is denoted in **bold** . All target variables in 1-, 6-, 12- and 24-month ahead DI, DIAR and DIAR-LAG forecasting are considered. 

#### **Table 13** 

Average forecasting performance of each factor estimation method by forecasting horizon and model. 

||||**DI**|||**DIAR**|||**DIAR-LA**|**G**|
|---|---|---|---|---|---|---|---|---|---|---|
|||Best|Worst|Mean|Best|Worst|Mean|Best|Worst|Mean|
||1-PLS|6.2|6.2|6.2|0.98|0.98|0.98|0.97|0.97|0.97|
||PLS|4.74|8.42|6.28|0.96|1.79|1.29|0.96|1.26|1.11|
||PCA|4.66|8.08|6.35|0.93|1|0.96|0.94|0.97|0.96|
||Targeted Predictors|2.57|7.4|4.03|0.93|1.03|0.97|0.94|0.99|0.96|
|_h_= 1|Weighted PC|4.47|8.73|6.39|0.93|1.04|0.97|0.94|1.02|0.97|
||Two Step|4.73|8.06|6.26|0.94|0.99|0.96|0.94|0.97|0.96|
||QMLE|4.82|8.08|6.3|0.94|1|0.97|0.94|0.98|0.96|
||One-sided|3.25|8.13|5.8|0.93|0.99|0.96|0.94|0.98|0.96|
||1-PLS|2.54|2.54|2.54|0.91|0.91|0.91|0.92|0.92|0.92|
||PLS|2.22|3.44|2.73|0.89|1.56|1.14|0.9|1.18|1.05|
||PCA|1.97|2.87|2.42|0.87|0.99|0.92|0.87|0.93|0.9|
||Targeted Predictors|1.54|2.77|1.96|0.88|1.04|0.95|0.87|0.98|0.92|
|_h_= 6|Weighted PC|1.91|3.13|2.44|0.86|1.05|0.94|0.87|1.01|0.94|
||Two Step|2.05|2.86|2.42|0.88|0.97|0.92|0.88|0.94|0.91|
||QMLE|2.12|2.91|2.47|0.89|1.03|0.95|0.89|0.95|0.92|
||One-sided|1.73|2.89|2.33|0.87|0.97|0.92|0.88|0.95|0.92|
||1-PLS|1.83|1.83|1.83|0.88|0.88|0.88|0.89|0.89|0.89|
||PLS|1.66|2.78|2.09|0.86|1.68|1.16|0.86|1.21|1.04|
||PCA|1.53|2.01|1.76|0.84|1.02|0.91|0.85|0.92|0.88|
|_h_ 12|Targeted Predictors|1.37|1.99|1.61|0.85|1.07|0.94|0.85|0.99|0.92|
|=|Weighted PC|1.48|2.18|1.78|0.84|1.06|0.92|0.84|0.99|0.91|
||Two Step|1.59|2|1.78|0.85|0.97|0.91|0.85|0.92|0.89|
||QMLE|1.64|2.09|1.83|0.86|1.06|0.94|0.87|0.94|0.91|
||One-sided|1.47|2.02|1.74|0.84|0.98|0.91|0.85|0.94|0.9|
||1-PLS|1.48|1.48|1.48|0.88|0.88|0.88|0.88|0.88|0.88|
||PLS|1.32|2.51|1.75|0.85|1.8|1.18|0.84|1.2|1.02|
||PCA|1.35|1.67|1.49|0.87|1.06|0.94|0.88|0.95|0.91|
||Targeted Predictors|1.26|1.72|1.47|0.87|1.14|0.99|0.87|1.03|0.95|
|_h_= 24|Weighted PC|1.3|1.8|1.5|0.86|1.12|0.95|0.87|1.01|0.94|
||Two Step|1.38|1.68|1.51|0.88|1.02|0.94|0.88|0.96|0.92|
||QMLE|1.42|1.75|1.55|0.89|1.12|0.98|0.89|0.97|0.94|
||One-sided|1.33|1.69|1.5|0.86|1.04|0.94|0.87|0.98|0.92|



This table shows the average predictive performance of each factor estimation method by forecasting horizon and model. Dashed lines are used to denote 1-PLS. For a given factor estimation method, the best and worst RMSEs are calculated, as well as mean RMSE over all decision rules under each forecasting horizon and model. For _h_ = 1 _,_ 6 _,_ 12 _,_ 24, Mean of best (Best), worst (Worst), and mean (Mean) over all target variables for each method are presented. 

best forecasting. This is shown in Tables 11–12, and Fig. 3. For PLS, a consistently estimated number of factors often gives worse predictions than a naive 1-PLS. Table 11 shows that even for PCA, predictive gain often arises from decision rules that do not consistently estimate the true number of factors. For instance, _k_<sup>ˆ</sup> _BIC_ is not theoretically proven as a consistent estimator for _r_ . _k_<sup>ˆ</sup> _BN_ − _BIC_ may not be a consistent estimator, as shown by Bai and Ng (2002). _k_<sup>ˆ</sup> _GP_ is not a consistent estimator either, as the method proposed by Giovannelli and Proietti (2016) selects a subset of factors from all the possible _N_ PCA 

components in a supervised way. This finding again supports the possible existence of irrelevant factors that do not explain the target variable. Empirically, predictive gain can often be obtained if the irrelevant factors are not used for forecasting. For instance, on average, _k_<sup>ˆ</sup> _BN_ − _BIC_ is estimated as 3.3, which is smaller than the number ofˆ factors determined by consistentˆ estimators, such as _kBN_ − _p_ 1 _,_ ˆ _kBN_ − _p_ 2 _,_ ˆ _kBN_ − _p_ 3 _,_ ˆ _kABC_ − _L_ , and _kABC_ − _S_ . 

Table 13 summarises the predictive ability of each factor estimation method across decision rules. First, for each target variable, the best, worst, and average forecasts 

1678 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

of a given factor estimation method across decision rules are collected. Each column in Table 13 is the average of the lowest, highest, and mean RMSEs of the given method over 144 (148) target variables by horizon.<sup>3</sup> Note that 1-PLS is displayed separately from PLS. Therefore, 1-PLS rows show the same values for all the columns. The PLS rows consider all decision rules applied to PLS, including 1-PLS. 

Table 13 demonstrates several empirical features. First, for all factor models and forecasting horizons, the DI models’ average RMSE is larger than one. Even the best possible decision rules for each factor estimation method produce worse forecasting results than the benchmark AR(BIC), indicated by RMSEs larger than one in the Best column. Therefore, forecasting with only estimated factors without the lagged target variable may not be more accurate than the AR forecasts in the recursive scheme. 

Second, the best forecasts of all factor estimation methods are very similar given the forecasting horizon, especially once the dynamics of the target variable, such as DIAR and DIAR-LAG models, are considered. The best forecasting performance one can obtain does not vary drastically depending on the factor estimation method if a proper decision rule is chosen, as indicated by the small variation in the Best column. This is because most of the seven factor estimation methods are proven consistent estimators for the true factors up to rotation. 

Third, forecasting performance varies widely among decision rules, even when using the same factor estimation method. This finding is emphasized by the large differences between the Best and Worst columns for all methods except 1-PLS. For example, in 12-months ahead DIAR forecasting, the worst PCA forecasts give, on average, 1.02 RMSE while the best possible PCA forecasts with a properly chosen decision rule significantly improve upon AR(BIC) as denoted by 0.84 in the Best column. Notably, all methods show larger differences between the Best and Worst results with longer forecasting horizons in DIAR and DIAR-LAG models. 

This experiment demonstrates the sensitivity of the factor estimation methods to the decision rule in practice. This implies that the choice of the factor estimation method and decision rule is crucial in empirical forecasting. As shown by larger RMSEs than 1 in DI models and the Worst columns on DIAR and DIAR-LAG models, factoraugmented forecasting does not always guarantee better forecasting results than the traditional AR process. 

Fourth, on the other hand, no factor estimation method, except PLS, exhibits dominant decision rules, as found in Fig. 3. Accordingly, the Mean columns represent the average predictive ability of the given method. Note that 1-PLS tends to show the mean value closest to the smallest mean value among all methods, especially at longer horizons and in DIAR and DIAR-LAG models, which again supports the strong forecasting performance of 1-PLS. 

> 3 A method could have several specifications, such as targeted predictors ( _λ_ 2), weighted PC, and one-sided estimation (static and dynamic version). Then, the best, worst, and mean are calculated considering all the specifications. 

### **5. Conclusion** 

This paper investigates the empirical performance of factor-augmented forecasts, whose factors are estimated by various methods. First, 1-PLS tends to give the best forecasting performance among all possible alternatives. The strong forecasting performances of 1-PLS are found in many target variables, especially when the lagged target variable is incorporated and at longer forecasting horizons. The predictive gains of 1-PLS compared to other alternatives are significant. PLS estimates factors by considering the maximum covariance with a target variable. Therefore, the strong performance of PLS can be explained by its incorporation of past information on the target variable in its factor estimation steps. 

Second, a consistently estimated number of factors does not necessarily lead to the best forecasts for many factor estimation methods, including PCA. The determined number of factors varies widely, even among decision rules that consistently estimate the true number of factors. It is difficult to find a dominant decision rule that tends to deliver the best results for a wide range of target variables for all factor estimation methods except for PLS. Also, when a proper decision rule is chosen, the best forecasts do not vary by factor estimation methods. If an appropriate decision rule is applied, the best predictions do not significantly depend on the factor estimation method. However, depending on the decision rule, the same factor estimation methods can yield somewhat different accuracy. Therefore, the factor estimation method and decision rule are important in forecasting performance. 

### **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

### **Appendix A** 

See Tables 14–19 and Fig. 6. 

### **Appendix B** 

The variables used in this study and their categories are presented here. The tcode column denotes the transformation type. Denote the time series at _t_ as _xt_ . 1 = no transformation, 2 = first difference, 3 = second difference, 4 = logarithm, 5 = first difference of logarithms 6 = second difference of logarithms, 7 = _∆_ ( _xt /xt_ −1 − 1). The data is taken from FRED, FRED-MD (McCracken & Ng, 2016) and ISM. The source column indicates where the variable is taken from. The source is denoted as FRED if a variable belongs to both FRED and FRED-MD. If a variable in FREDMD is adjusted from the raw data available in FRED, the source is denoted as FRED-MD. See Tables B.20–B.27. 

1679 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 



**Fig. 6.** Percentage of Target Variables That a Decision Rule Outperform the Rest Decision Rules by Forecasting Model in **Rolling** Estimation: PLS and PCA. 

1680 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

#### **Table 14** 

Top 5 methods in **Rolling** estimation, PLS with other decision rules excluded. 

||Methods Giving the Best Results Mo|st Frequently|Methods Giving Results Closest to|the Best|
|---|---|---|---|---|
||Methods|Percentage (%)|Methods|Mean(Ratio)|
||**1-PLS**|**16.44**|Targeted Predictors, _λ_= 0_._25(BN-p1)|0.118|
||Weighted PC, Rule B(BIC)|5.32|Targeted Predictors, _λ_= 0_._25(BN-p2)|0.118|
|_h_ 1|QMLE(BN-p3)|5.32|Targeted Predictors, _λ_= 0_._5(BN-p2)|0.123|
|=|PCA(GP)|4.17|Targeted Predictors, _λ_= 0_._5(BN-p1)|0.129|
||Targeted Predictors, _λ_= 0_._25(BN-p3)|3.94|Targeted Predictors, _λ_= 0_._5(BIC)<br>**1-PLS**|0.13<br>**0.42**|
||**1-PLS**|**27.55**|Targeted Predictors, _λ_= 0_._25(ABC-L)|0.167|
||Weighted PC, Rule B(AH)|6.94|Targeted Predictors, _λ_= 0_._5(ABC-L)|0.17|
|_h_ 6|Weighted PC, Rule B(BIC)|6.71|Targeted Predictors, _λ_= 1_._5(ABC-L)|0.172|
|=|Weighted PC, Rule B(ON)|4.17|Targeted Predictors, _λ_= 0_._5(ON)|0.173|
||PCA(BN-BIC)|3.24|Targeted Predictors, _λ_= 0_._5(AH)|0.179|
||||**1-PLS**|**0.184**|
||**1-PLS**|**38.19**|**1-PLS**|**0.13**|
||Weighted PC, Rule B(AH)|5.32|Weighted PC, SWb(AH)|0.191|
|_h_= 12|PCA(BN-BIC)|4.17|Weighted PC, SWa(AH)|0.196|
||Weighted PC, Rule B(ON)|3.47|PCA(ABC-L)|0.196|
||Weighted PC, Rule B(BIC)|2.55|PCA(AH)|0.201|
||**1-PLS**|**35.81**|**1-PLS**|**0.119**|
||Weighted PC, Rule B(AH)|9.68|Weighted PC, SWa(AH)|0.182|
|_h_= 24|Weighted PC, Rule B(BIC)|6.76|OS-Static(AH)|0.187|
||Weighted PC, Rule B(ON)|3.15|Weighted PC, SWb(AH)|0.187|
||Weighted PC, Rule B(GP)|3.15|Weighted PC, Rule B(ON)|0.19|



This table presents the top 5 methods for each forecasting horizon giving the best results most frequently and giving results closest to the best results on average in the left and right columns respectively. 1-PLS is represented in bold and dashed line represents the case that 1-PLS is not the top 5 methods. PLS with other decision rules are excluded. For each forecasting horizon, all target variables in DI, DIAR and DIAR-LAG models are considered. 

**Table 15** 

Top 10 methods : DI, DIAR and DIAR-LAG. 

||**Recursiv**|**e**||
|---|---|---|---|
|Methods Giving the|Best Results Most Frequently|Methods Giving Resul|ts Closest to the Best|
|Methods|Percentage (%)|Methods|Mean(Ratio)|
|**1-PLS**|**11.15**|PCA(BIC)|0.131|
|PLS(BN-BIC)|5.69|OS-S(BIC)|0.131|
|PLS(ON)|5.57|WPC, SWb(BIC)|0.135|
|PLS(BN-p2)|3.33|Two-step(BIC)|0.137|
|OS-D(HL2007)|2.64|OS-D(BN2007)|0.138|
|PCA(BN-BIC)|2.59|TP, _λ_= 1_._5(BIC)|0.14|
|TP, _λ_= 1_._5(AH)|2.41|PCA(BN-p3)|0.142|
|WPC, SWa(ON)|2.3|WPC, SWa(BIC)|0.142|
|PLS(AH)|2.01|TP, _λ_= 0_._5(BIC)|0.144|
|PLS(ABC-L)|1.95|OS-S(BN-p3)|0.144|
|||**1-PLS**|**0.153**|
||**Rolling**|||
|Methods Giving the|Best Results Most Frequently|Methods Giving Resul|ts Closest to the Best|
|Methods|Percentage (%)|Methods|Mean(Ratio)|
|PLS(AH)|14.08|**1-PLS**|**0.26**|
|**1-PLS**|**9.71**|TP, _λ_= 0_._5(ON)|0.273|
|PLS(BN-BIC)|6.38|TP, _λ_= 0_._25(ON)|0.276|
|WPC, Rule B(AH)|5.57|TP, _λ_= 1_._5(ON)|0.28|
|PLS(ON)|5.17|PCA(ABC-L)|0.285|
|WPC, Rule B(BIC)|4.08|PCA(BN-BIC)|0.288|
|WPC, Rule B(ON)|2.64|TP, _λ_= 0_._5(AH)|0.289|
|PLS(BN-p1)|2.36|TP, _λ_= 0_._25(AH)|0.289|
|PLS(BN-p2)|2.3|WPC, SWb(AH)|0.29|
|PLS(ABC-L)|2.07|PCA(BN-p2)|0.291|



This table presents the top 10 methods giving the best results most frequently and giving results closest to the best results on average according to forecasting scheme. Forecasting starts from 1970:01 and recursive scheme uses an increasing window, while rolling scheme uses a fixed window of 10 years. WPC, OS-S and OS-D stand for Weighted PC, OS-Static and OS-Dynamic. 1-PLS is represented in bold and dashed line represents the case that 1-PLS is not the top 10 methods. All target variables, forecasting horizons and forecasting models (1,740 combinations) are considered. 

1681 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

#### **Table 16** 

Top 10 methods : DIAR and DIAR-LAG. 

||**Recu**|**rsive**||
|---|---|---|---|
|Methods Giving the Best Results|Most Frequently|Methods Giving Results Closest|to the Best|
|Methods|Percentage (%)|Methods|Mean(Ratio)|
|**1-PLS**|**10.78**|**1-PLS**|**0.081**|
|PLS(ON)|5.52|PCA(BN-BIC)|0.085|
|PLS(BN-BIC)|5.43|PCA(ABC-L)|0.085|
|PCA(BN-BIC)|3.19|WPC, SWb(ON)|0.085|
|OS-D(HL2007)|3.19|PCA(ON)|0.087|
|WPC, SWa(ON)|2.76|WPC, SWa(ON)|0.088|
|TP, _λ_= 1_._5(AH)|2.41|PCA(AH)|0.088|
|QMLE(ON)|1.98|OS-S(ON)|0.089|
|TP, _λ_= 0_._25(BN-BIC)|1.81|Two-step(ON)|0.09|
|TP, _λ_= 1_._5(ON)|1.81|Two-step(BN-BIC)|0.091|
||**Rol**|**ling**||
|Methods Giving the Best Results|Most Frequently|Methods Giving Results Closest|to the Best|
|Methods|Percentage (%)|Methods|Mean(Ratio)|
|PLS(AH)|12.93|**1-PLS**|**0.216**|
|**1-PLS**|**8.97**|PLS(AH)|0.24|
|PLS(BN-BIC)|8.45|PLS(ON)|0.266|
|WPC, Rule B(AH)|6.29|TP, _λ_= 0_._5(ON)|0.288|
|PLS(ON)|5.43|WPC, SWb(AH)|0.289|
|WPC, Rule B(ON)|3.71|TP, _λ_= 1_._5(ON)|0.293|
|PLS(BN-p1)|3.28|TP, _λ_= 0_._25(ON)|0.294|
|PLS(BN-p2)|2.76|PCA(AH)|0.295|
|PLS(ABC-S)|2.76|WPC, SWa(AH)|0.296|
|PLS(ABC-L)|2.67|TP, _λ_= 0_._5(AH)|0.299|



This table presents the top 10 methods giving the best results most frequently and giving results closest to the best results on average according to forecasting scheme. Forecasting starts from 1970:01 and recursive scheme uses an increasing window, while rolling scheme uses a fixed window of 10 years. WPC, OS-S and OS-D stand for Weighted PC, OS-Static and OS-Dynamic. All target variables and forecasting horizons in DIAR and DIAR-LAG forecasting models (1,160 combinations) are considered. 

#### **Table 17** 

Top 10 methods : DI, DIAR and DIAR-LAG, PLS with other decision rules excluded. 

|**Recursive**||
|---|---|
|Methods Giving the Best Results Most Frequently<br>Methods Giving Resu|lts Closest to the Best|
|Methods<br>Percentage (%)<br>Methods|Mean(Ratio)|
|**1-PLS**<br>**16.55**<br>PCA(BIC)|0.114|
|PCA(BN-BIC)<br>3.05<br>OS-S(BIC)|0.115|
|OS-D(HL2007)<br>2.7<br>WPC, SWb(BIC)|0.118|
|TP, _λ_= 1_._5(AH)<br>2.64<br>OS-D(BN2007)|0.12|
|WPC, SWa(ON)<br>2.59<br>Two-step(BIC)|0.121|
|WPC, Rule B(GP)<br>2.41<br>TP, _λ_= 1_._5(BIC)|0.124|
|WPC, Rule B(BIC)<br>2.18<br>PCA(BN-p3)|0.125|
|TP, _λ_= 1_._5(ON)<br>2.13<br>WPC, SWa(BIC)|0.125|
|TP, _λ_= 0_._5(AH)<br>1.84<br>PCA(BN-p1)|0.127|
|TP, _λ_= 1_._5(BN-p1)<br>1.78<br>PCA(BN-p2)|0.127|
|**1-PLS**|**0.137**|
|**Rolling**||
|Methods Giving the Best Results Most Frequently<br>Methods Giving Resu|lts Closest to the Best|
|Methods<br>Percentage (%)<br>Methods|Mean(Ratio)|
|**1-PLS**<br>**29.54**<br>**1-PLS**|**0.213**|
|WPC, Rule B(AH)<br>6.49<br>TP, _λ_= 0_._5(ON)|0.219|
|WPC, Rule B(BIC)<br>5.34<br>TP, _λ_= 0_._25(ON)|0.221|
|WPC, Rule B(ON)<br>2.93<br>TP, _λ_= 1_._5(ON)|0.225|
|PCA(BN-BIC)<br>2.53<br>PCA(ABC-L)|0.23|
|WPC, Rule B(GP)<br>2.07<br>PCA(BN-BIC)|0.232|
|WPC, Rule B(BN-BIC)<br>1.72<br>TP, _λ_= 0_._5(AH)|0.234|
|TP, _λ_= 0_._25(BN-p3)<br>1.67<br>TP, _λ_= 0_._25(AH)|0.234|
|TP, _λ_= 1_._5(AH)<br>1.61<br>PCA(BN-p2)|0.235|
|QMLE(BN-p3)<br>1.55<br>WPC, SWb(AH)|0.235|



This table presents the top 10 methods giving the best results most frequently and giving results closest to the best results on average according to forecasting scheme. Forecasting starts from 1970:01 and recursive scheme uses an increasing window, while rolling scheme uses a fixed window of 10 years. WPC, OS-S and OS-D stand for Weighted PC, OS-Static and OS-Dynamic. PLS with other decision rules are excluded. 1-PLS is represented in bold and dashed line represents the case that 1-PLS is not the top 10 methods. All target variables, forecasting horizons and forecasting models (1,740 combinations) are considered. 

1682 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

#### **Table 18** 

Top 10 methods : DIAR and DIAR-LAG, PLS with other decision rules excluded. 

||**Recu**|**rsive**|
|---|---|---|
|Methods Giving the Best Result|s Most Frequently|Methods Giving Results Closest to the Best|
|Methods|Percentage (%)|Methods<br>Mean(Ratio)|
|**1-PLS**|**16.64**|**1-PLS**<br>**0.072**|
|PCA(BN-BIC)|3.71|PCA(BN-BIC)<br>0.074|
|OS-D(HL2007)|3.28|PCA(ABC-L)<br>0.074|
|WPC, SWa(ON)|3.19|WPC, SWb(ON)<br>0.075|
|TP, _λ_= 1_._5(AH)|2.59|PCA(ON)<br>0.076|
|TP, _λ_= 1_._5(ON)|2.16|PCA(AH)<br>0.078|
|WPC, SWa(AH)|2.07|WPC, SWa(ON)<br>0.078|
|QMLE(ON)|1.98|OS-S(ON)<br>0.079|
|TP, _λ_= 0_._25(BN-BIC)|1.9|Two-step(ON)<br>0.08|
|PCA(ON)|1.81|Two-step(BN-BIC)<br>0.08|
||**Roll**|**ing**|
|Methods Giving the Best Result|s Most Frequently|Methods Giving Results Closest to the Best|
|Methods|Percentage (%)|Methods<br>Mean(Ratio)|
|**1-PLS**|**32.93**|**1-PLS**<br>**0.156**|
|WPC, SWb(ON)|7.67|WPC, SWa(ON)<br>0.219|
|WPC, SWb(ABC-L)|4.14|TP, _λ_= 0_._25(ABC-L)<br>0.22|
|PCA(BN-BIC)|2.41|TP, _λ_= 0_._5(ABC-L)<br>0.225|
|WPC, SWb(AH)|2.41|PLS(AH)<br>0.225|
|TP, _λ_= 0_._5(ON)|1.72|PCA(ABC-L)<br>0.226|
|WPC, SWb(BN-p1)|1.72|TP, _λ_= 1_._5(ON)<br>0.226|
|PLS(BN-BIC)|1.64|WPC, Rule B(ON)<br>0.229|
|Two-step(BN-p3)|1.64|TP, _λ_= 0_._25(ON)<br>0.23|
|WPC, SWb(ABC-S)|1.47|PLS(ABC-L)<br>0.232|



This table presents the top 10 methods giving the best results most frequently and giving results closest to the best results on average according to forecasting scheme. Forecasting starts from 1970:01 and recursive scheme uses an increasing window, while rolling scheme uses a fixed window of 10 years. WPC, OS-S and OS-D stand for Weighted PC, OS-Static and OS-Dynamic. PLS with other decision rules are excluded. All target variables and forecasting horizons in DIAR and DIAR-LAG forecasting models (1,160 combinations) are considered. 

**Table 19** 

Top 10 methods <u>giving</u> significant DM statistics most frequently by significance level <u>(</u> _α_ <u>).</u> 

||Recursive||Rolling||
|---|---|---|---|---|
||Method|Percentage (%)|Method|Percentage (%)|
||WPC, SWb(ON)|38.74|**1-PLS**|**47.3**|
||PCA(ON)|38.45|PLS(AH)|42.47|
||WPC, SWa(ON)|38.28|PLS(ON)|40.11|
||OS-S(ON)|37.01|WPC, SWb(AH)|37.53|
|_α_=01|Two-step(ON)|36.55|WPC, SWa(AH)|37.47|
|_._|PCA(AH)|36.03|OS-S(AH)|36.9|
||WPC, SWb(AH)|34.66|PCA(AH)|36.78|
||QMLE(ON)|34.6|Two-step(AH)|36.32|
||**1-PLS**|**34.31**|QMLE(AH)|35.98|
||WPC, SWa(AH)|33.97|WPC, Rule B(AH)|35.4|
||PCA(ON)|27.93|**1-PLS**|**39.2**|
||WPC, SWb(ON)|27.24|PLS(AH)|36.15|
||WPC, SWa(ON)|25.92|PLS(ON)|34.2|
||OS-S(ON)|25.8|WPC, SWb(AH)|31.84|
|005|PCA(AH)|25.4|WPC, SWa(AH)|31.38|
|_α_ = _._|Two-step(ON)|25.4|OS-S(AH)|30.92|
||**1-PLS**|**24.66**|PCA(AH)|30.69|
||PCA(BN-BIC)|24.66|WPC, SWb(ON)|30.23|
||QMLE(ON)|23.51|Two-step(AH)|29.77|
||OS-S(AH)|23.51|WPC, SWa(ON)|29.37|



( _continued on next page_ ) 

1683 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table 19** <u>(</u> _continued_ <u>).</u> 

||Recursive||Rolling||
|---|---|---|---|---|
||Method|Percentage (%)|Method|Percentage (%)|
||OS-S(ON)|11.9|**1-PLS**|**27.93**|
||WPC, SWb(ON)|11.84|PLS(ON)|26.44|
||PCA(BN-BIC)|11.72|PLS(AH)|25.86|
||PCA(ON)|11.44|WPC, SWb(ON)|22.36|
|001|**1-PLS**|**11.09**|WPC, SWa(AH)|21.95|
|_α_ = _._|PCA(AH)|10.98|WPC, SWb(AH)|21.84|
||WPC, SWa(ON)|10.98|WPC, SWa(ON)|21.72|
||Two-step(BN-BIC)|10.8|PCA(ON)|21.15|
||Two-step(ON)|10.8|PCA(AH)|20.98|
||Two-step(AH)|10.57|Two-step(AH)|20.69|



This table presents the top 10 methods giving significant DM statistics most frequently, according to significance level ( _α_ ) and forecasting scheme. Forecasting starts from 1970:01 and recursive scheme uses an increasing window, while rolling scheme uses a fixed window of 10 years. WPC, OS-S and OS-D stand for Weighted PC, OS-Static and OS-Dynamic. Note that the case with smaller _α_ is also counted in larger _α_ . For instance, if a DM statistic is significant under _α_ = 0 _._ 05, it is also counted in _α_ = 0 _._ 1. All target variables, forecasting horizons and forecasting models (1,740 combinations) are considered. 

**Table B.20** 

Category 1: Output and Income. 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|1|RPI|5|Real Personal Income|1959:01–2019:12|1, 6, 12, 24|FRED|
|2|W875RX1|5|Real personal income excl. transfer receipts|1959:01–2019:12|1, 6, 12, 24|FRED|
|6|INDPRO|5|IP: Total Index|1959:01–2019:12|1, 6, 12, 24|FRED|
|7|IPFPNSS|5|IP: Final Products and Nonindustrial Supplies|1959:01–2019:12|1, 6, 12, 24|FRED|
|8|IPFINAL|5|IP: Final Products|1959:01–2019:12|1, 6, 12, 24|FRED|
|9|IPCONGD|5|IP: Consumer Goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|10|IPDCONGD|5|IP: Durable Consumer Goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|11|IPNCONGD|5|IP: Nondurable Consumer Goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|12|IPBUSEQ|5|IP: Equipment: Business Equipment|1959:01–2019:12|1, 6, 12, 24|FRED|
|13|IPMAT|5|IP: Materials|1959:01–2019:12|1, 6, 12, 24|FRED|
|14|IPDMAT|5|IP: Durable Goods Materials|1959:01–2019:12|1, 6, 12, 24|FRED|
|15|IPNMAT|5|IP: Nondurable Goods Materials|1959:01–2019:12|1, 6, 12, 24|FRED|
|16|IPMANSICS|5|IP: Manufacturing|1959:01–2019:12|1, 6, 12, 24|FRED|
|17|IPB51222S|5|IP: Utilities|1959:01–2019:12|1, 6, 12, 24|FRED|
|18|IPFUELS|5|IP: Fuels|1959:01–2019:12|1, 6, 12, 24|FRED|
|19|CUMFNS|2|Capacity Util: Manufacturing|1959:01–2019:12|1, 6, 12, 24|FRED|
|129|IPNMAN|5|IP: Nondurable Manufacturing|1972:01–2019:12||FRED|
|130|IPDMAN|5|IP: Durable Manufacturing|1972:01–2019:12||FRED|
|131|IPMINE|5|IP: Mining|1959:01–2019:12|1, 6, 12, 24|FRED|
|132|TCU|1|Capacity Util: Total Index|1967:01–2019:12||FRED|
|133|CAPUTLGMFDS|1|Capacity Util: Durable Manufacturing|1967:01–2019:12||FRED|
|134|CAPUTLGMFNS|1|Capacity Util: Nondurable Manufacturing|1967:01–2019:12||FRED|
|135|CAPUTLG21S|1|Capacity Util: Mining|1967:01–2019:12||FRED|
|136|CAPUTLG2211A2S|1|Capacity Util: Utilities|1967:01–2019:12||FRED|
|173|ISM \MAN_PROD|1|Manufacturing Production Index|1959:01–2019:12|1, 6, 12, 24|ISM|



#### **Table B.21** 

Category 2: Labor market. 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|20|HWI|2|Help-Wanted Index for US|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|21|HWIURATIO|2|Ratio of Help Wanted/No. Unemployed|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|22|CLF16OV|5|Civilian Labor Force Level|1959:01–2019:12|1, 6, 12, 24|FRED|
|23|CE16OV|5|Employment Level|1959:01–2019:12|1, 6, 12, 24|FRED|
|24|UNRATE|2|Unemployment Rate|1959:01–2019:12|1, 6, 12, 24|FRED|
|25|UEMPMEAN|2|Avg Weeks Unemployed|1959:01–2019:12|1, 6, 12, 24|FRED|
|26|UEMPLT5|5|Number Unemployed for Less Than 5 Weeks|1959:01–2019:12|1, 6, 12, 24|FRED|
|27|UEMP5TO14|5|Number Unemployed for 5-14 Weeks|1959:01–2019:12|1, 6, 12, 24|FRED|
|28|UEMP15OV|5|Number Unemployed for 15 Weeks & over|1959:01–2019:12|1, 6, 12, 24|FRED|
|29|UEMP15T26|5|Number Unemployed for 15-26 Weeks|1959:01–2019:12|1, 6, 12, 24|FRED|
|30|UEMP27OV|5|Number Unemployed for 27 Weeks & over|1959:01–2019:12|1, 6, 12, 24|FRED|
|31|CLAIMSx|5|Initial Claims|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|32|PAYEMS|5|All Employees, Total Nonfarm|1959:01–2019:12|1, 6, 12, 24|FRED|
|33|USGOOD|5|All Employees, Goods-Producing|1959:01–2019:12|1, 6, 12, 24|FRED|
|34|CES1021000001|5|All Employees, Mining, Quarrying, and Oil and Gas Extraction|1959:01–2019:12|1, 6, 12, 24|FRED|
|35|USCONS|5|All Employees, Construction|1959:01–2019:12|1, 6, 12, 24|FRED|
||||||(_continued_|_on next page_)|



1684 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table B.21** <u>(</u> _continued_ <u>).</u> 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|36|MANEMP|5|All Employees, Manufacturing|1959:01–2019:12|1, 6, 12, 24|FRED|
|37|DMANEMP|5|All Employees, Durable Goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|38|NDMANEMP|5|All Employees, Nondurable Goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|39|SRVPRD|5|All Employees, Service-Providing|1959:01–2019:12|1, 6, 12, 24|FRED|
|40|USTPU|5|All Employees, Trade, Trans. & Utilities|1959:01–2019:12|1, 6, 12, 24|FRED|
|41|USWTRADE|5|All Employees, Wholesale Trade|1959:01–2019:12|1, 6, 12, 24|FRED|
|42|USTRADE|5|All Employees, Retail Trade|1959:01–2019:12|1, 6, 12, 24|FRED|
|43|USFIRE|5|All Employees, Financial Activities|1959:01–2019:12|1, 6, 12, 24|FRED|
|44|USGOVT|5|All Employees, Government|1959:01–2019:12|1, 6, 12, 24|FRED|
|45|CES0600000007|1|Avg Weekly Hours, Goods-Producing|1959:01–2019:12|1, 6, 12, 24|FRED|
|46|AWOTMAN|2|Avg Weekly Overtime Hours, Manufacturing|1959:01–2019:12|1, 6, 12, 24|FRED|
|47|AWHMAN|1|Avg Weekly Hours, Manufacturing|1959:01–2019:12|1, 6, 12, 24|FRED|
|120|CES0600000008|6|Avg Hourly Earnings, Goods-Producing|1959:01–2019:12|1, 6, 12, 24|FRED|
|121|CES2000000008|6|Avg Hourly Earnings, Construction|1959:01–2019:12|1, 6, 12, 24|FRED|
|122|CES3000000008|6|Avg Hourly Earnings, Manufacturing|1959:01–2019:12|1, 6, 12, 24|FRED|
|137|USPRIV|5|All Employees, Total Private|1959:01–2019:12|1, 6, 12, 24|FRED|
|138|CES5552000001|5|All Employees, Finance and Insurance|1990:01–2019:12||FRED|
|139|CES5553100001|5|All Employees, Real Estate|1990:01–2019:12||FRED|
|140|SRVPRD|5|All Employees, Service-Providing|1959:01–2019:12|1, 6, 12, 24|FRED|
|141|AWHNONAG|1|Avg Weekly Hours, Total Private|1964:01–2019:12||FRED|
|166|AHETPI|6|Avg Hourly Earnings, Total Private|1964:01–2019:12||FRED|
|167|CES4000000008|6|Avg Hourly Earnings, Trade, Trans. & Utilities|1964:01–2019:12||FRED|
|168|CES4200000008|6|Avg Hourly Earnings, Retail Trade|1972:01–2019:12||FRED|
|169|CES4142000008|6|Avg Hourly Earnings, Wholesale Trade|1972:01–2019:12||FRED|
|170|CES5500000008|6|Avg Hourly Earnings, Financial Activities|1964:01–2019:12||FRED|
|171|CES0800000008|6|Avg Hourly Earnings, Private Service-Providing|1964:01–2019:12||FRED|
|174|ISM \MAN_EMPL|1|Manufacturing Employment Index|1959:01–2019:12|1, 6, 12, 24|ISM|



#### **Table B.22** 

Category 3: Housing. 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|48|HOUST|4|Housing Starts: Total|1959:01–2019:12|1, 6, 12, 24|FRED|
|49|HOUSTNE|4|Housing Starts: Northeast|1959:01–2019:12|1, 6, 12, 24|FRED|
|50|HOUSTMW|4|Housing Starts: Midwest|1959:01–2019:12|1, 6, 12, 24|FRED|
|51|HOUSTS|4|Housing Starts: South|1959:01–2019:12|1, 6, 12, 24|FRED|
|52|HOUSTW|4|Housing Starts: West|1959:01–2019:12|1, 6, 12, 24|FRED|
|53|PERMIT|4|New Private Housing Permits: Total|1960:01–2019:12|1, 6, 12, 24|FRED|
|54|PERMITNE|4|New Private Housing Permits: Northeast|1960:01–2019:12|1, 6, 12, 24|FRED|
|55|PERMITMW|4|New Private Housing Permits: Midwest|1960:01–2019:12|1, 6, 12, 24|FRED|
|56|PERMITS|4|New Private Housing Permits: South|1960:01–2019:12|1, 6, 12, 24|FRED|
|57|PERMITW|4|New Private Housing Permits: West|1960:01–2019:12|1, 6, 12, 24|FRED|
|150|HSN1F|4|New One Family Houses Sold: US|1963:01–2019:12|24|FRED|
|151|HSN1FNE|4|New One Family Houses Sold, Northeast|1973:01–2019:12||FRED|
|152|HSN1FMW|4|New One Family Houses Sold, Midwest|1973:01–2019:12||FRED|
|153|HSN1FS|4|New One Family Houses Sold, South|1973:01–2019:12||FRED|
|154|HSN1FW|4|New One Family Houses Sold, West|1973:01–2019:12||FRED|
|155|MSACSR|4|Monthly Supply of New Houses, US|1963:01–2019:12|24|FRED|
|156|HNFSEPUSSA|4|New One Family Homes for Sale, US|1963:01–2019:12|24|FRED|
|157|UNDCONTSA|4|New Privately-Owned Housing Under Construction: Total|1970:01–2019:12||FRED|



#### **Table B.23** 

Category 4: Consumption, orders, and inventories. 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|3|DPCERA3M086SBEA|5|Real personal consumption expenditures|1959:01–2019:12|1, 6, 12, 24|FRED|
|4|CMRMTSPLx|5|Real Manu. and Trade Industries Sales|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|5|RETAILx|5|Retail and Food Services Sales|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|58|ACOGNO|5|Manufacturers’ New Orders: Consumer Goods|1992:02-2019:12||FRED|
|59|AMDMNOx|5|New Orders for Durable Goods|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|60|ANDENOx|5|New Orders for Nondefense Capital Goods|1968:02-2019:12||FRED-MD|
|61|AMDMUOx|5|Unfilled Orders for Durable Goods|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|62|BUSINVx|5|Total Business Inventories|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|63|ISRATIOx|2|Total Business: Inventories to Sales Ratio|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|123|UMCSENTx|2|Consumer Sentiment Index|1959:05-2019:12||FRED-MD|
|142|USASLMNTO02MLSAM|5|Sales: Manufacturing: Total Manufacturing: Value for US|1960:01–2019:12|1, 6, 12, 24|FRED|
|143|USASLRTTO02MLSAM|5|Sales: Retail Trade: Total Retail Trade: Value for US|1960:01–2019:12|1, 6, 12, 24|FRED|
|144|USASLWHTO02MLSAM|5|Sales: Wholesale Trade: Total Wholesale Trade: Value for US|1960:01–2019:12|1, 6, 12, 24|FRED|
|145|USASARTMISMEI|1|Total Retail Trade in US|1960:01–2019:12|1, 6, 12, 24|FRED|
|146|DDURRA3M086SBEA|5|Real pers. consump. expnd.: Durable goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|147|DNDGRA3M086SBEA|5|Real pers. consump. expnd.: Nondurable goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|148|DSERRA3M086SBEA|5|Real pers. consump. expnd.: Services|1959:01–2019:12|1, 6, 12, 24|FRED|
|149|DGDSRA3M086SBEA|5|Real pers. consump. expnd.: Goods|1959:01–2019:12|1, 6, 12, 24|FRED|



( _continued on next page_ ) 

1685 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

#### **Table B.23** <u>(</u> _continued_ <u>).</u> 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|158|INVCMRMTSPL|5|Real Manufacturing and Trade Inventories|1967:01–2019:12||FRED|
|159|SOANDI|1|CFNAI: Sales, Orders and Inventories|1967:03-2019:12||FRED|
|160|USAODMNTO02MLSAM|5|Orders: Manufacturing: Total Orders: Value for US|1960:01–2019:12|1, 6, 12, 24|FRED|
|172|ISM \MAN_PMI|1|PMI Composite Index|1959:01–2019:12|1, 6, 12, 24|ISM|
|175|ISM \MAN_NEWORDERS|1|Manufacturing New Orders Index|1959:01–2019:12|1, 6, 12, 24|ISM|
|176|ISM \MAN_DELIV|1|Manufacturing Supplier Deliveries Index|1959:01–2019:12|1, 6, 12, 24|ISM|
|177|ISM \MAN_INVENT|1|Manufacturing Inventories Index|1959:01–2019:12|1, 6, 12, 24|ISM|



#### **Table B.24** 

Category 5: Money and credit. 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|64|M1SL|6|M1|1959:01–2019:12|1, 6, 12, 24|FRED|
|65|M2SL|6|M2|1959:01–2019:12|1, 6, 12, 24|FRED|
|66|M2REAL|5|Real M2 Money Stock|1959:01–2019:12|1, 6, 12, 24|FRED|
|67|BOGMBASE|6|Monetary Base; Total|1959:01–2019:12|1, 6, 12, 24|FRED|
|68|TOTRESNS|6|Reserves of Depository Institutions: Total|1959:01–2019:12|1, 6, 12, 24|FRED|
|69|NONBORRES|7|Reserves of Depository Institutions, Nonborrowed|1959:01–2019:12|1, 6, 12, 24|FRED|
|70|BUSLOANS|6|Commercial and Industrial Loans|1959:01–2019:12|1, 6, 12, 24|FRED|
|71|REALLN|6|Real Estate Loans, All Commercial Banks|1959:01–2019:12|1, 6, 12, 24|FRED|
|72|NONREVSL|6|Total Nonrevolving Credit|1959:01–2019:12|1, 6, 12, 24|FRED|
|73|CONSPI|2|Nonrevolving consumer credit to Personal Income|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|124|MZMSL|6|MZM Money Stock|1959:01–2019:12|1, 6, 12, 24|FRED|
|125|DTCOLNVHFNM|6|Consumer Motor Vehicle Loans Outstanding|1959:01–2019:12|1, 6, 12, 24|FRED|
|126|DTCTHFNM|6|Total Consumer Loans and Leases Outstanding|1959:01–2019:12|1, 6, 12, 24|FRED|
|127|INVEST|6|Securities in Bank Credit, All Commercial Banks|1959:01–2019:12|1, 6, 12, 24|FRED|
|162|USGSEC|5|Treasury and Agency Securities, All Commercial Banks|1959:01–2019:12|1, 6, 12, 24|FRED|



#### **Table B.25** 

Category 6: Interest and exchange rates. 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|78|FEDFUNDS|2|Federal Funds Effective Rate|1959:01–2019:12|1, 6, 12, 24|FRED|
|79|CP3Mx|2|3-Month AA Financial Commercial Paper Rate|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|80|TB3MS|2|3-Month Treasury Bill , Discount Basis|1959:01–2019:12|1, 6, 12, 24|FRED|
|81|TB6MS|2|6-Month Treasury Bill , Discount Basis|1959:01–2019:12|1, 6, 12, 24|FRED|
|82|GS1|2|1-Year Treasury Rate, Quoted on an Investment Basis|1959:01–2019:12|1, 6, 12, 24|FRED|
|83|GS5|2|5-Year Treasury Rate, Quoted on an Investment Basis|1959:01–2019:12|1, 6, 12, 24|FRED|
|84|GS10|2|10-Year Treasury Rate, Quoted on an Investment Basis|1959:01–2019:12|1, 6, 12, 24|FRED|
|85|AAA|2|Moody’s Seasoned Aaa Corporate Bond Yield|1959:01–2019:12|1, 6, 12, 24|FRED|
|86|BAA|2|Moody’s Seasoned Baa Corporate Bond Yield|1959:01–2019:12|1, 6, 12, 24|FRED|
|87|COMPAPFFx|1|3-Month Commercial Paper Minus FEDFUNDS|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|88|TB3SMFFM|1|3-Month Treasury Bill Minus FEDFUNDS|1959:01–2019:12|1, 6, 12, 24|FRED|
|89|TB6SMFFM|1|6-Month Treasury Bill Minus FEDFUNDS|1959:01–2019:12|1, 6, 12, 24|FRED|
|90|T1YFFM|1|1-Year Treasury Constant Maturity Minus FEDFUNDS|1959:01–2019:12|1, 6, 12, 24|FRED|
|91|T5YFFM|1|5-Year Treasury Constant Maturity Minus FEDFUNDS|1959:01–2019:12|1, 6, 12, 24|FRED|
|92|T10YFFM|1|10-Year Treasury Constant Maturity Minus FEDFUNDS|1959:01–2019:12|1, 6, 12, 24|FRED|
|93|AAAFFM|1|Moody’s Seasoned Aaa Corporate Bond Minus FEDFUNDS|1959:01–2019:12|1, 6, 12, 24|FRED|
|94|BAAFFM|1|Moody’s Seasoned Baa Corporate Bond Minus FEDFUNDS|1959:01–2019:12|1, 6, 12, 24|FRED|
|95|TWEXAFEGSMTHx|5|Trade Weighted U.S. Dollar Index|1973:01–2019:12||FRED-MD|
|96|EXSZUSx|5|Switzerland/U.S. Foreign Exchange Rate|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|97|EXJPUSx|5|Japan/U.S. Foreign Exchange Rate|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|98|EXUSUKx|5|U.S./U.K. Foreign Exchange Rate|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|99|EXCAUSx|5|Canada/U.S. Foreign Exchange Rate|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|161|RNUSBIS|5|Real Narrow Effective Exchange Rate for US|1964:01–2019:12||FRED|



#### **Table B.26** 

Category 7: Prices. 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|100|WPSFD49207|6|PPI: Finished Goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|101|WPSFD49502|6|PPI: Finished Consumer Goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|102|WPSID61|6|PPI: Processed Intermediate Goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|103|WPSID62|6|PPI: Unprocessed Intermediate Goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|104|OILPRICEx|6|Crude Oil, spliced WTI and Cushing|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|105|PPICMM|6|PPI: Metals and Metal Products|1959:01–2019:12|1, 6, 12, 24|FRED|
|106|CPIAUCSL|6|CPI: All Items|1959:01–2019:12|1, 6, 12, 24|FRED|
|107|CPIAPPSL|6|CPI: Apparel|1959:01–2019:12|1, 6, 12, 24|FRED|
|108|CPITRNSL|6|CPI: Transportation|1959:01–2019:12|1, 6, 12, 24|FRED|
|109|CPIMEDSL|6|CPI: Medical Care|1959:01–2019:12|1, 6, 12, 24|FRED|
|110|CUSR0000SAC|6|CPI: Commodities|1959:01–2019:12|1, 6, 12, 24|FRED|



( _continued on next page_ ) 

1686 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

**Table B.26** <u>(</u> _continued_ <u>).</u> 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|111|CUSR0000SAD|6|CPI: Durables|1959:01–2019:12|1, 6, 12, 24|FRED|
|112|CUSR0000SAS|6|CPI: Services|1959:01–2019:12|1, 6, 12, 24|FRED|
|113|CPIULFSL|6|CPI: All Items Less Food|1959:01–2019:12|1, 6, 12, 24|FRED|
|114|CUSR0000SA0L2|6|CPI: All Items Less Shelter|1959:01–2019:12|1, 6, 12, 24|FRED|
|115|CUSR0000SA0L5|6|CPI: All Items Less Medical Care|1959:01–2019:12|1, 6, 12, 24|FRED|
|116|PCEPI|6|PCE: Chain Index|1959:01–2019:12|1, 6, 12, 24|FRED|
|117|DDURRG3M086SBEA|6|PCE: Durable goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|118|DNDGRG3M086SBEA|6|PCE: Nondurable goods|1959:01–2019:12|1, 6, 12, 24|FRED|
|119|DSERRG3M086SBEA|6|PCE: Services|1959:01–2019:12|1, 6, 12, 24|FRED|
|163|WPSFD49209|6|PPI: Finished Goods, Excluding Foods|1967:01–2019:12||FRED|
|164|CPIUFDSL|6|CPI: Food|1959:01–2019:12|1, 6, 12, 24|FRED|
|165|CPIHOSSL|6|CPI: Housing|1967:01–2019:12||FRED|
|178|ISM \MAN_PRICES|1|Manufacturing Prices Index|1959:01–2019:12|1, 6, 12, 24|ISM|



#### **Table B.27** 

Category 8: Stock market. 

|ID|Variable|tcode|Description|Period|Target|Source|
|---|---|---|---|---|---|---|
|74|SP_500|5|S&P’s Common Stock Price Index: Composite|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|75|SP_indust|5|S&P’s Common Stock Price Index: Industrials|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|76|SP_div_yield|2|S&P’s Composite Common Stock: Dividend Yield|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|77|SP_PE_ratio|5|S&P’s Composite Common Stock: Price-Earnings Ratio|1959:01–2019:12|1, 6, 12, 24|FRED-MD|
|128|VXOCLSx|1|VXO|1962:07-2019:12|24|FRED-MD|



### **References** 

- Ahn, S. C., & Bae, J. (2022). Forecasting with partial least squares using many predictors. Available at SSRN 4248450. 

- Ahn, S. C., & Horenstein, A. R. (2013). Eigenvalue ratio test for the number of factors. _Econometrica_ , _81_ (3), 1203–1227. 

- Alessi, L., Barigozzi, M., & Capasso, M. (2010). Improved penalization for determining the number of factors in approximate factor models. _Statistics & Probability Letters_ , _80_ (23–24), 1806–1813. 

- Angelini, E., Camba-Mendez, G., Giannone, D., Reichlin, L., & Rünstler, G. (2011). _Short-term forecasts of Euro area GDP growth_ . Oxford, UK: Oxford University Press. 

- Artis, M. J., Banerjee, A., & Marcellino, M. (2005). Factor forecasts for the UK. _Journal of Forecasting_ , _24_ (4), 279–298. 

Bai, J. (2003). Inferential theory for factor models of large dimensions. _Econometrica_ , _71_ (1), 135–171. Bai, J., & Ng, S. (2002). Determining the number of factors in approximate factor models. _Econometrica_ , _70_ (1), 191–221. 

- Bai, J., & Ng, S. (2006). Confidence intervals for diffusion index forecasts and inference for factor-augmented regressions. _Econometrica_ , _74_ (4), 1133–1150. 

- Bai, J., & Ng, S. (2007). Determining the number of primitive shocks in factor models. _Journal of Business & Economic Statistics_ , _25_ (1), 52–60. 

- Bai, J., & Ng, S. (2008). Forecasting economic time series using targeted predictors. _Journal of Econometrics_ , _146_ (2), 304–317. 

- Bańbura, M., Giannone, D., Modugno, M., & Reichlin, L. (2013). Nowcasting and the real-time data flow. In _Handbook of economic forecasting_ : _vol. 2_ , (pp. 195–237). Elsevier. 

- Banbura, M., Giannone, D., & Reichlin, L. (2010). Nowcasting. ECB working paper. 

- Bańbura, M., & Modugno, M. (2014). Maximum likelihood estimation of factor models on datasets with arbitrary pattern of missing data. _Journal of Applied Econometrics_ , _29_ (1), 133–160. 

- Bańbura, M., & Rünstler, G. (2011). A look into the factor model black box: publication lags and the role of hard and soft data in forecasting GDP. _International Journal of Forecasting_ , _27_ (2), 333–346. 

- Barhoumi, K., Benk, S., Cristadoro, R., Den Reijer, A., Jakaitiene, A., Jelonek, P., et al. (2008). Short-term forecasting of GDP using large monthly datasets–A pseudo real-time forecast evaluation exercise. National Bank of Belgium Working Paper133. 

- Barigozzi, M., & Hallin, M. (2017). Generalized dynamic factor models and volatilities: Estimation and forecasting. _Journal of Econometrics_ , _201_ (2), 307–321. 

- Barigozzi, M., & Hallin, M. (2020). Generalized dynamic factor models and volatilities: Consistency, rates, and prediction intervals. _Journal of Econometrics_ , _216_ (1), 4–34. 

- Bernanke, B. S., & Boivin, J. (2003). Monetary policy in a data-rich environment. _Journal of Monetary Economics_ , _50_ (3), 525–546. 

Bernanke, B. S., Boivin, J., & Eliasz, P. (2005). Measuring the effects of monetary policy: A factor-augmented vector autoregressive (FAVAR) approach. _The Quarterly Journal of Economics_ , _120_ (1), 387–422. 

- Boivin, J., & Ng, S. (2005). Understanding and comparing factor-based forecasts. _International Journal of Central Banking_ , _1_ (3). 

- Boivin, J., & Ng, S. (2006). Are more data always better for factor analysis? _Journal of Econometrics_ , _132_ (1), 169–194. 

- Bu, C., Rogers, J., & Wu, W. (2021). A unified measure of fed monetary policy shocks. _Journal of Monetary Economics_ , _118_ , 331–349. 

- Choi, I. (2012). Efficient estimation of factor models. _Economic Theory_ , _28_ (2), 274–308. 

Cristadoro, R., Forni, M., Reichlin, L., & Veronese, G. (2005). A core inflation indicator for the Euro area. _Journal of Money, Credit and Banking_ , 539–560. 

D’Agostino, A., & Giannone, D. (2012). Comparing alternative predictors based on large-panel factor models. _Oxford Bulletin of Economics and Statistics_ , _74_ (2), 306–326. 

- Dax, A. (2017). The numerical rank of Krylov matrices. _Linear Algebra and its Applications_ , _528_ , 185–205. 

- Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. _Journal of Business & Economic Statistics_ , 253–263. 

- Doz, C., Giannone, D., & Reichlin, L. (2011). A two-step estimator for large approximate dynamic factor models based on Kalman filtering. _Journal of Econometrics_ , _164_ (1), 188–205. 

- Doz, C., Giannone, D., & Reichlin, L. (2012). A quasi–maximum likelihood approach for large, approximate dynamic factor models. _Review of Economics and Statistics_ , _94_ (4), 1014–1024. 

- Forni, M., Giovannelli, A., Lippi, M., & Soccorsi, S. (2018). Dynamic factor model with infinite-dimensional factor space: Forecasting. _Journal of Applied Econometrics_ , _33_ (5), 625–642. 

- Forni, M., Hallin, M., Lippi, M., & Reichlin, L. (2000). The generalized dynamic-factor model: Identification and estimation. _Review of Economics and Statistics_ , _82_ (4), 540–554. 

- Forni, M., Hallin, M., Lippi, M., & Reichlin, L. (2003). Do financial variables help forecasting inflation and real activity in the Euro area? _Journal of Monetary Economics_ , _50_ (6), 1243–1255. 

- Forni, M., Hallin, M., Lippi, M., & Reichlin, L. (2005). The generalized dynamic factor model: One-sided estimation and forecasting. _Journal of the American Statistical Association_ , _100_ (471), 830–840. 

- Forni, M., Hallin, M., Lippi, M., & Zaffaroni, P. (2015). Dynamic factor models with infinite-dimensional factor spaces: One-sided representations. _Journal of Econometrics_ , _185_ (2), 359–371. 

1687 

_International Journal of Forecasting 40 (2024) 1660–1688_ 

_J. Bae_ 

- Forni, M., Hallin, M., Lippi, M., & Zaffaroni, P. (2017). Dynamic factor models with infinite-dimensional factor space: Asymptotic analysis. _Journal of Econometrics_ , _199_ (1), 74–92. 

- Fuentes, J., Poncela, P., & Rodríguez, J. (2015). Sparse partial least squares in time series for macroeconomic forecasting. _Journal of Applied Econometrics_ , _30_ (4), 576–595. 

- Geweke, J. (1977). The dynamic factor analysis of economic time series. In _Latent variables in socio-economic models_ . North-Holland. 

- Geweke, J. F., & Singleton, K. J. (1981). Maximum likelihood ‘‘confirmatory’’ factor analysis of economic time series. _International Economic Review_ , 37–54. 

- Giacomini, R., & Rossi, B. (2010). Forecast comparisons in unstable environments. _Journal of Applied Econometrics_ , _25_ (4), 595–620. 

- Giacomini, R., & White, H. (2006). Tests of conditional predictive ability. _Econometrica_ , _74_ (6), 1545–1578. 

- Giannone, D., Reichlin, L., & Small, D. (2008). Nowcasting: The real-time informational content of macroeconomic data. _Journal of Monetary Economics_ , _55_ (4), 665–676. 

- Giglio, S., Kelly, B., & Pruitt, S. (2016). Systemic risk and the macroeconomy: An empirical evaluation. _Journal of Financial Economics_ , _119_ (3), 457–471. 

- Giovannelli, A., & Proietti, T. (2016). On the selection of common factors for macroeconomic forecasting. In _Dynamic factor models_ (pp. 593–628). Emerald Group Publishing Limited. 

- Groen, J. J., & Kapetanios, G. (2016). Revisiting useful approaches to data-rich macroeconomic forecasting. _Computational Statistics & Data Analysis_ , _100_ , 221–239. 

- Hallin, M., & Liška, R. (2007). Determining the number of factors in the general dynamic factor model. _Journal of the American Statistical Association_ , _102_ (478), 603–617. 

- Helland, I. S. (1988). On the structure of partial least squares regression. _Communications in Statistics-Simulation and Computation_ , _17_ (2), 581–607. 

- Helland, I. S. (1990). Partial least squares regression and statistical models. _Scandinavian Journal of Statistics_ , 97–114. 

- Hepenstrick, C., & Marcellino, M. (2019). Forecasting gross domestic product growth with large unbalanced data sets: the mixed frequency three-pass regression filter. _Journal of the Royal Statistical Society: Series A (Statistics in Society)_ , _182_ (1), 69–99. 

- Hindrayanto, I., Koopman, S. J., & de Winter, J. (2016). Forecasting and nowcasting economic growth in the Euro area using factor models. _International Journal of Forecasting_ , _32_ (4), 1284–1305. 

- Huang, D., Jiang, F., Li, K., Tong, G., & Zhou, G. (2022). Scaled PCA: A new approach to dimension reduction. _Management Science_ , _68_ (3), 1678–1695. 

- Huang, D., Jiang, F., Tu, J., & Zhou, G. (2015). Investor sentiment aligned: A powerful predictor of stock returns. _The Review of Financial Studies_ , _28_ (3), 791–837. 

- Inoue, A., Jin, L., & Rossi, B. (2017). Rolling window selection for out-of-sample forecasting with time-varying parameters. _Journal of Econometrics_ , _196_ (1), 55–67. 

- Jones, C. S. (2001). Extracting factors from heteroskedastic asset returns. _Journal of Financial economics_ , _62_ (2), 293–325. 

- Jurado, K., Ludvigson, S. C., & Ng, S. (2015). Measuring uncertainty. _American Economic Review_ , _105_ (3), 1177–1216. 

- Kelly, B., & Pruitt, S. (2013). Market expectations in the cross-section of present values. _The Journal of Finance_ , _68_ (5), 1721–1756. 

- Kelly, B., & Pruitt, S. (2015). The three-pass regression filter: A new approach to forecasting using many predictors. _Journal of Econometrics_ , _186_ (2), 294–316. 

- Kim, H. H., & Swanson, N. R. (2014). Forecasting financial and macroeconomic variables using data reduction methods: New empirical evidence. _Journal of Econometrics_ , _178_ , 352–367. 

- Light, N., Maslov, D., & Rytchkov, O. (2017). Aggregation of information about the cross section of stock returns: A latent variable approach. _The Review of Financial Studies_ , _30_ (4), 1339–1381. 

- Lin, Q. (2018). Technical analysis and stock return predictability: An aligned approach. _Journal of Financial Markets_ , _38_ , 103–123. 

- Ludvigson, S. C., Ma, S., & Ng, S. (2021). Uncertainty and business cycles: Exogenous impulse or endogenous response? _American Economic Journal: Macroeconomics_ , _13_ (4), 369–410. 

- Marcellino, M., & Sivec, V. (2021). Nowcasting GDP growth in a small open economy. _National Institute Economic Review_ , _256_ , 127–161. 

- McCracken, M. W., & Ng, S. (2016). FRED-MD: A monthly database for macroeconomic research. _Journal of Business & Economic Statistics_ , _34_ (4), 574–589. 

- Medeiros, M. C., Vasconcelos, G. F., Veiga, Á., & Zilberman, E. (2021). Forecasting inflation in a data-rich environment: the benefits of machine learning methods. _Journal of Business & Economic Statistics_ , _39_ (1), 98–119. 

- Molodtsova, T., & Papell, D. H. (2009). Out-of-sample exchange rate predictability with Taylor rule fundamentals. _Journal of International Economics_ , _77_ (2), 167–180. 

- Onatski, A. (2010). Determining the number of factors from empirical distribution of eigenvalues. _The Review of Economics and Statistics_ , _92_ (4), 1004–1016. 

- Poncela, P., Ruiz, E., & Miranda, K. (2021). Factor extraction using Kalman filter and smoothing: This is not just another survey. _International Journal of Forecasting_ , _37_ (4), 1399–1425. 

- Sargent, T. J., Sims, C. A., et al. (1977). Business cycle modeling without pretending to have too much a priori economic theory. _New Methods in Business Cycle Research_ , _1_ , 145–168. 

- Schumacher, C. (2007). Forecasting German GDP using alternative factor models based on large datasets. _Journal of Forecasting_ , _26_ (4), 271–302. 

- Schumacher, C., & Breitung, J. (2008). Real-time forecasting of German GDP based on a large factor model with monthly and quarterly data. _International Journal of Forecasting_ , _24_ (3), 386–398. 

- Stock, J. H., & Watson, M. W. (1989). New indexes of coincident and leading economic indicators. _NBER Macroeconomics Annual_ , _4_ , 351–394. 

- Stock, J. H., & Watson, M. W. (1996). Evidence on structural instability in macroeconomic time series relations. _Journal of Business & Economic Statistics_ , _14_ (1), 11–30. 

- Stock, J. H., & Watson, M. W. (1998). _Diffusion indexes_ . Mass., USA: National bureau of economic research Cambridge. 

- Stock, J. H., & Watson, M. W. (1999). Forecasting inflation. _Journal of Monetary Economics_ , _44_ (2), 293–335. 

- Stock, J. H., & Watson, M. W. (2002a). Forecasting using principal components from a large number of predictors. _Journal of the American statistical association_ , _97_ (460), 1167–1179. 

- Stock, J. H., & Watson, M. W. (2002b). Macroeconomic forecasting using diffusion indexes. _Journal of Business & Economic Statistics_ , _20_ (2), 147–162. 

- Stock, J. H., & Watson, M. W. (2006). Forecasting with many predictors. In _Handbook of economic forecasting_ : _vol. 1_ , (pp. 515–554). Elsevier. 

- Stock, J. H., & Watson, M. W. (2007). Why has US inflation become harder to forecast? _Journal of Money, Credit and Banking_ , _39_ , 3–33. 

- Stock, J. H., & Watson, M. (2009). Forecasting in dynamic factor models subject to structural instability. In _The methodology and practice of econometrics. A Festschrift in honour of David F. Hendry_ : _vol. 173_ , (p. 205). Oxford University Press Oxford. 

Swanson, N. R. (1998). Money and output viewed through a rolling window. _Journal of Monetary Economics_ , _41_ (3), 455–474. Trucíos, C., Mazzeu, J. H., Hotta, L. K., Pereira, P. L. V., & Hallin, M. (2021). Robustness and the general dynamic factor model with infinite-dimensional space: Identification, estimation, and forecasting. _International Journal of Forecasting_ , _37_ (4), 1520–1534. 

- Watson, M. W., & Engle, R. F. (1983). Alternative algorithms for the estimation of dynamic factor, mimic and varying coefficient regression models. _Journal of Econometrics_ , _23_ (3), 385–400. 

- White, H. (1982). Maximum likelihood estimation of misspecified models. _Econometrica_ , 1–25. 

Wold, H. (1966). Estimation of principal components and related models by iterative least squares. _Multivariate analysis_ , 391–420. 

- Wold, H. (1973). Nonlinear iterative partial least squares (NIPALS) modelling: Some current developments. In _Multivariate analysis–III_ (pp. 383–407). Elsevier. 

- Wold, H. (1982). Soft modeling: The basic design and some extensions. In _Systems under indirect observation_ : _vol. 2_ , (p. 343). 

- Zhang, Y., He, M., Wang, Y., & Liang, C. (2022). Global economic policy uncertainty aligned: An informative predictor for crude oil market volatility. _International Journal of Forecasting_ . 

- Zhang, Y., Wahab, M., & Wang, Y. (2023). Forecasting crude oil market volatility using variable selection and common factor. _International Journal of Forecasting_ , _39_ (1), 486–502. 

- Zou, H., & Hastie, T. (2005). Regularization and variable selection via the elastic net. _Journal of the Royal Statistical Society: Series B (Statistical Methodology)_ , _67_ (2), 301–320. 

1688 

