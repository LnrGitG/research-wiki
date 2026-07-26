---
title: 1 Introduction
type: paper
source_pdf: raw/papers/Garmider. Ispolzovanie-modeli-favar-dlya-prognozirovaniya-rossiyskih-makroekonomicheskih-ryadov.pdf
converted: 2026-07-26
---

Национальный исследовательский университет 

“Высшая школа экономики“ 

Факультет экономических наук 

Департамент Прикладной экономики 

Выпускная квалификационная работа 

“Использование модели FAVAR для прогнозирования российских макроэкономических рядов“. 

Гармидер Пётр, БЭК 165 

Научный руководитель: 

Борис Демешев, Старший преподаватель Факультета Экономических Наук, Департамента Прикладной Экономики 

Москва 

17 Апреля 2020 

# Contents 

|1|Intr|oduction<br>3|
|---|---|---|
||1.1|Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>3|
||1.2|Literature review<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>5|
||1.3|Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>7|
|2|Mod|el<br>8|
||2.1|VAR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>8|
||2.2|FAVAR . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>9|
||2.3|Estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>12|
||2.4|Model specifcations . . . . . . . . . . . . . . . . . . . . . . .<br>17|
|3|Dat|a<br>17|
|4|Res|ults<br>18|
|5|Con|clusion<br>21|
|A|Dat|a Description<br>22|



2 

### Abstract 

There are several models used for time series forecasts that focus on incorporating a huge set of information. Conventional VAR fails to employ such an approach because of the "degrees of freedom" problem. The focus of this paper is to examine factor-augmented VAR’s (FAVAR’s) ability to forecast the main Russian macroeconomic indicators. Results will be displayed in a table of RMSEs for different horizons using time series cross-validation procedure for each one. I discovered that FAVAR, indeed, has potential in forecasting and create particularly accurate forecasts for long-horizons. FAVAR’s cross-validation error is compared with benchmark models such as ETS, ARIMA, and VAR. Latent factors in model, surely, delivers additional information, that standard VAR fails to recover. 

# 1 Introduction 

## 1.1 Overview 

Forecasting of macroeconomic time series is an important task for different economic institutions. Accurate forecasts for main macro indicators allow central banks to timely react to possible dangers for the economy. Proper actions conducted by the central bank may prevent a possible recession or the same way, wrong actions may result in initiating one. 

Macro indicators forecasts are useful for commercial companies as well. There are many scenarios in which corporations are particularly interested in understanding possible future macro factor outcomes, such as: choosing the right price policy, signing long-term contracts with counterparties, making decisions on the possibility of entering a new market, etc. One cannot deny that a huge amount of financial instruments heavily dependent on macroeconomic situation within the country. Investors in attempts to value a particular financial asset always build a forecast of its determinants. In 

3 

this way, almost everything to some extent shows comovement with one or another macro factor. This demonstrates that forecasting macroeconomic time series is an extremely crucial part of quite a huge range of spheres. 

There are a number of models used for time series prediction. Each model uses a different approach to dealing with time series. Some approaches do not require any assumptions about data and aimed to minimize proper loss function in a specific manner. The other includes restrictions on data, assuming, for example, the presence of the data-generating process with parameters that are to be estimated. State-of-the-art models, usually employ mixed approaches where forecast is based on the results of the two mentioned methods. Models of the first type show high accuracy of prediction, however, they are hard to interpret and are prone to outliers. Models of the second type, on the contrary, show moderate accuracy, though give information about moving forces and produce quite robust results. The last approach, tries to balance between advantages and disadvantages of the two previous approaches. Of course, there are plenty of other models with different views on data. 

One can divide the parametric of models onto two subcategories: univariate and multivariate. To make a forecast for the considered time series more accurate, the last method tries to use additional data, while first assumes the data generating process of a particular series to be a function of past realizations of itself and only. This paper mostly deals with multivariate models vector autoregression (VAR) suggested by Sims (1980) and its variation factor-augmented VAR that aimed to eliminate drawbacks of classical version. 

In this paper I will consider factor-augmented vector autoregression (FAVAR): method of estimation, its application for forecasting purposes, and accuracy evaluation of produced forecast. The goal is to understand, 

4 

whether the factor model outperform univariate approach. One also may be interested in comparing classical VAR with its augmented version. It will be shown, that VAR is a restricted model of FAVAR, therefore it is possible to test whether the difference between the two is statistically significant. 

## 1.2 Literature review 

Several studies discuss FAVAR model and employ its potential for particular purposes. Bernanke et al. (2005) were first to introduce a model to incorporate a huge set of information to assess structural shocks effect on monetary policy. They discuss Sims (1992) and his interpretation of the "price puzzle" when several papers showed that VAR models predict that contractionary monetary policy shock is followed by a rise in a price level, rather than decrease as traditional macroeconomic theory suggests. Authors believe that the explanation proposed by the inventor of VAR yet had weak points, therefore suggest their way to deal with "price puzzle". In the paper authors used 120 monthly time series pointing out that central banks while making decisions on interest rate act in a "data-rich environment", considering a larger set of time series than standard VAR approach allows to include. Therefore, econometrician, ignoring this fact, faces a problem of biased estimates. They suggested two ways of how FAVAR can be estimated and one of them will be presented as pseudo-code in this work. The main goal of model inventors was to obtain correct impulse responses for variables of interest rather than producing forecasts for them. 

Nevertheless, there are some works focused on applying considered model for prediction task as well, for example, M¨onch (2008) in his work uses FAVAR to forecast yield curve. The author mentions that state-of-the-art models in this sphere have a large number of parameters to estimate, which 

5 

means that users cannot simply include as many explanatory variables as one wishes, so there is a risk to lose important information. Therefore, the author used the approach of latent factor extraction described in Bernanke et al. (2005) and mixed it with traditional models for yield curve prediction. 

Most of the papers agree, that for the time series prediction factoraugmented VAR shows better performance for long-term forecasts. In Figueiredo and Guill´en (2013) FAVAR is used for time series forecasting of Brazilian consumer inflation (IPCA). Authors found that factor-based models outperform traditional AR models on long horizons. They also considered estimation methods pointing out that ML approach strictly outperforms two-step PCA method, that is the focus of study in this paper. Pang (2010) employed a factor model for predicting GDP growth rate, unemployment, and inflation rates of the Hong Kong economy. Author’s results are in line with those obtained in Figueiredo and Guill´en (2013) – FAVAR performs better than simple VAR and AR models especially for long horizons. The author used 76 monthly variables that are believed to reflect the economic situation in Hong Kong. Transforming original data, the author followed the methodology suggested in Stock and Watson (2005). 

Berggren and Lodenius (2016) in their paper computed Diebold-Mariano test of equal predictive accuracy, comparing FAVAR with benchmark models. The authors found, that the forecast performance of FAVAR was not statistically better than traditional VAR or AR models. Nonetheless, they claim that further research should be done towards an optimal number of lags for the factors, since they found that FAVAR with only one lag for factors performed statistically better than with twelve. 

Overall, the literature suggests that the potential of FAVAR model for time series prediction task still is not fully unlocked. There is still space for improvements and experiments, for example, employing FAVAR for non- 

6 

economic time series. 

## 1.3 Methods 

There are several approaches to measure the quality of time series prediction models. Each method, however, captures one side of the model. Traditional train test split is quite sensitive to split proportion and also to structural changes that occurred after the end of a training set. For this reason, it is not fully accurate to perform this method in their traditional form. 

Nonetheless, it is possible to account for h-horizon prediction power performing time-series cross-validation and treat a forecast for each horizon separately. Still results of such procedure may be argued, since a robust estimate of a model’s accuracy requires a large number of observations that is problematic for Russian data available. For this reason, I will measure models’ performance using time series cross-validation with expanding window. 

Forecasts are measured on RMSE (root of mean square error) metric as it is quite interpretable. The chosen measure will be evaluated for different horizons separately. The formula for h-th horizon as follows: 



� – – where _J_ hold-out set size, _yt|t−h_ forecast for period t having available information up to the moment _t − h_ . 

There are several ways to estimate FAVAR model. Bernanke et al. (2005) in their work consider two, which are two-step estimation using principal components analysis to recover latent factors and one-step Bayesian likelihood approach estimation. Authors stated that they found no obvious evidence of one method being superior to another and whether the computational cost of the first one worths it. Since cross-validation requires multiple 

7 

reestimation, I simply choose the approach that is less time-consuming. 

Particular properties of the two-step approach estimation make unclear distribution of estimated coefficients, therefore building right confident intervals becomes a separate task. Bernanke et al. (2005) use a bootstrap procedure for obtaining impulse response function intervals, the same way one may obtain predictive confident interval, however that is out of the scope of this paper. 

# 2 Model 

## 2.1 VAR 

Lets _Yt_ be _M ×_ 1 vector of variables under consideration. It is said that _Yt_ is a VAR(d) process if it has the following dynamic equation: 



– – – where _A_ 0 _M ×_ 1 vector; _∀i_ = 0 _Ai M × M_ matrix; _εt M ×_ 1 error vector with zero mean; components of _Yt_ are integrated of the same order. _A_<sup>ˆ</sup> _i_ can be obtained by equation-by-equation least squares. One can easily check that number of parameters to be estimated equals _M_ ( _Md_ + 1) = _O_ ( _M_<sup>2</sup> ) , _M →_ ∞ . For example, an econometrician should estimate 57 coefficients if one wants to use VAR(6) model with 3 variables for forecasting purposes. This means, that M is strictly limited by the number of periods. In practice, it is uncommon to see more than 6 variables included in a VAR equation. This problem is particularly relevant while dealing with short time series, which is the case with Russian economic data. It is hard to believe that econometrician is able to select six variables without missing an important one. Consequently, researcher generally gets biased estimates which may result, for example, in 

8 

popular VAR issue that is called "price puzzle". In Bernanke et al. (2005) authors propose an explanation to this problem which completely relies on omitted equation assumption. Thus, ignoring one variable may result in incorrect economic dynamics modeling that may lead to weak forecasting performance. In order to address this issue, one can estimate FAVAR model, which allows incorporating a huge set of economic indicators without losing degrees of freedom<sup>1</sup> . 

## 2.2 FAVAR 

This section will be based on II.A part in Bernanke et al. (2005). Let _Yt_ be _M ×_ 1 vector of observable economic variables that are believed to reflect the dynamics of the economy. Standard VAR approach implies that _Yt_ contains price indicator, observable variable reflecting the economy’s real output and policy instrument. Such a specification of _Yt_ is mainly used for structural analysis. As discussed earlier, one may argue that barely information captured by _Yt_ reflects the dynamics of the whole economy. Let _Ft_ be _K ×_ 1 vector of unobservable variables, where in some way K is a small number, that are assumed to summarise all the information that is not captured by _Yt_ . These factors are said to reflect movements of theoretical concept variable, such as: "economic activity", "investment environment", "price pressure" and etc. 

Assume also that dynamics of vector ( _Ft_<sup>_′,Y_</sup> _t_<sup>_′_)followstheequation:</sup> 



– where Φ( _L_ ) = (Φ0 + Φ1 _L_ + Φ2 _L_<sup>2</sup> + _..._ + Φ _dL_<sup>_d_</sup> ) ; d – finite number; Φ _i_ ( _K_ + _M_ ) _×_ ( _K_ + _M_ ) matrix; _vt_ – error term vector, such that: E( _vt_ ) = 0 , E( _vtvt_<sup>_′_) =</sup> 

> 1Number of observations - number of model’s parameters 

9 

– _Q_ ; _Q_ is symmetric positive semi-definite ( _K_ + _M_ ) _×_ ( _K_ + _M_ ) matrix; _L_ lag operator: _LYt_ = _Yt−_ 1 . 

One may see, that if components of Φ( _L_ ) that relate _Yt_ to _Ft−_ 1 are zeros, then _Yt_ is simply a VAR process. Otherwise, equation (2) is VAR in ( _Ft_<sup>_′,Y_</sup> _t_<sup>_′_).</sup> The fact, that econometrician may obtain VAR in _Yt_ from (2) makes model (2) unrestricted to VAR in _Yt_ . This makes it possible to perform statistical tests, for instance, the likelihood ratio test, that allows to check whether an unrestricted model is statistically different from a restricted one. Model (2) is commonly called factor-augmented vector autoregression, or simply FAVAR. In the paper Bernanke et al. (2005) authors correctly note that if the true model is FAVAR, but instead VAR in _Yt_ is estimated, then econometrician generally gets biased estimates, that may lead to poor forecasting power of an estimated model. 

Coefficients of Φ( _L_ ) cannot be estimated directly since vector _Ft_ is unobservable. If one was provided with real values of _Ft_ , he could apply conventional techniques of VAR estimation, equation-by-equation least squares, for example, in order to estimate (2). 

It is obvious, that real dynamics of _Yt_ is affected by a huge number of time series, such as exchange rate, price indices, investment climate situation, – import/export shocks, and many more. Let us introduce _N ×_ 1 vector _Xt_ set of "informational" variables, where _N_ is in some way a "large" number, specifically such that _K_ + _M << N_ . Unlike _Ft_ , vector _Xt_ is assumed to be observable. It is also believed that _Xt_ is a linear function of observable _Yt_ and unobservable _Ft_ : 



– – – where Λ<sup>_f_</sup> _N × K_ matrix; Λ<sup>_y_</sup> _N × M_ ; _et_ error term vector, such that: 

10 

E( _et_ ) = 0 , E( _etiet j_ ) _≈_ 0 _∀i_ = _j_ .<sup>2</sup> Equation (3) reflects the idea that economy can be precisely described by just _K_ + _M_ main indicators. All the other variables that we may observe are generated from those key ones. The main point in (3) is that _Ft_ is still vector of unobservable variables and the idea is to exploit the fact that ( _Ft_<sup>_′,X_</sup> _t_<sup>_′_)isobservedtogetestimatesof</sup><sup>_Ft_vector.</sup> Having in some sense accurate _F_<sup>ˆ</sup> _t_ , econometrician is able to estimate (2) in ( _F_<sup>ˆ</sup> _t_<sup>_′_</sup> _,Yt_<sup>_′_).It is important to note, that</sup><sup>_Xt_depends only on</sup><sup>_Ft_and</sup><sup>_Yt_, not from</sup> lags of these vectors. 

If _N_ is a small number, it is possible to include _Xt_ directly in (2) and estimate VAR in ( _Xt_<sup>_′,Y_</sup> _t_<sup>_′_).However, barely it is the truth, that central bank, for</sup> example, monitor only three or four variables, setting the key rate. Though, if a researcher wants to incorporate an additional variable in a model, it is quite unlikely that he would have enough observations to get coefficients’ estimates. 

There are several possible FAVAR models may be constructed depending on what a researcher initially assume. For example, it is possible to include in _Yt_ variables such as CPI, GDP growth, and central bank key rate, which means that researcher is uncertain about the rest structure of the economy and believe in the presence of a finite number of latent factors that fill possible model misspecification. One may also argue, that in reality we don’t observe truth GDP growth and CPI. Instead, we are provided with these series estimations by some federal institutions, that are still noisy measures for true variables. Such model specification is in line with the fact, that GDP growth and CPI series are subjects for several corrections, even in a year. However, for sure, we observe the truth central bank key rate. 

> 2One can find formal requirements on _et_ in Stock and Watson (2002) 

11 

## 2.3 Estimation 

Authors in Bernanke et al. (2005) propose two ways of FAVAR estimation. The first is based on Gibbs sampling approach, which is not applicable if one desires to obtain a cross-validation model’s error, since such an approach is enormously time-costly. Estimation of one model may take even an hour. The second approach is referred in Bernanke et al. (2005) as two-step principal component method, that is much more computationally efficient in time and easy in implementation. Moreover, the last approach does not require special assumptions on error-terms distributions, as well as allows some crosscorrelation in it, which is more likely the truth dealing with real data. 

Two-stage estimation approach includes: 

1. Extraction of factors _Ft_ from _Xt_ , purifying it from the influence of _Yt_ .<sup>3</sup> 

2. Estimation of model (2), using obtained _F_<sup>ˆ</sup> _t_ by standard VAR methods. 

In order to perform stage 1 one should use the equation (3) and exploit the fact that _X_<sup>_′_isobservablevectorforeachperiodt.Letusremindonce</sup> ( _t_<sup>_,Y_</sup> _t_<sup>_′_)</sup> again the equation (3): 



We can rewrite (3) as: 





> 3To get only additional information about economy dynamics, that is not captured by _Yt_ 

12 

ˆ ˆ The idea is simple. If we have estimated Λ<sup>ˆ</sup> , _αt_ and _et_ is a small number for all t, then the estimates of parameters are "good". Assume _Xt_ is normal- _′_ ized to have zero mean: ∑ _t_<sup>_T_</sup> =1<sup>_Xt_=</sup> 0 _..._ 0<sup>Then, let us set the following</sup> � � _N×_ 1<sup>.</sup> minimization task: 



It is worth noting that (6) has in total ( _K_ + _M_ ) _N_ +( _K_ + _M_ ) _T_ parameters for estimation. It is also important to note, that there are infinite number of solutions for this optimization task. If we came up with a solution to (6) in form (Λ<sup>˜</sup> _,_ � _α_ ) then for any _Z_ : _Z_<sup>_′_</sup> _Z_ = _I_ follows (Λ<sup>˜</sup> _Z_<sup>_′_</sup> _,Zα_ �) is also solution of (6). Thus let us impose restriction on Λ : Λ<sup>_′_</sup> Λ = _I_ , which basically means we are trying to obtain orthogonal and normalised unit-scale vectors. Problem (6) transforms to:  



Assuming solution Λ<sup>ˆ</sup> being known, optimal _α_ ˆ _t_ = (Λ<sup>_′_</sup> Λ)<sup>_−_1</sup> Λ<sup>_′_</sup> _Xt_ . Since _αt_ does not affect other periods error, then we can treat (6) as _T_ independent minimization problems, such for fixed period _t_ : 



With known Λ , problem (8) becomes nothing but a simple least-squares task with known analytical solution. Thus, (7) transforms to: 



13 

Let _L_ = ∑ _t_<sup>_T_</sup> =1<sup>(</sup><sup>_Xt −_ΛΛ</sup><sup>_′Xt_)</sup><sup>_′_(</sup><sup>_Xt −_ΛΛ</sup><sup>_′Xt_),then:</sup> 







Thus, problem (10) is equivalent to: 



Let _L_<sup>˜</sup> = ∑ _t_<sup>_T_</sup> =1<sup>_Xt_ΛΛ</sup><sup>_′Xt_,then:</sup> 



where (*) follows from the trace property: _tr_ ( _AB_ ) = _tr_ ( _BA_ ) , if _A_ and _B_ are matrices of suitable sizes. 

_′_ Let us remind that if _XT ×N_ = _X_ 1 _X_ 2 _... XT_ is matrix that has zero mean by � � columns, then _SX_ = _T_<sup><u>1</u>∑</sup> _t_<sup>_T_</sup> =1<sup>_XtX_</sup> _t_<sup>_′_– is empirical covariance matrix of</sup><sup>_Xt_vector.</sup> 



Thus (10) problem becomes equivalent to: 



14 

Still (12) has _N_ ( _K_ + _M_ ) parameters that should be estimated. Though, this optimization task has an exact analytical solution. One should compute the first _K_ + _M_ eigenvectors of _SX_ corresponding to the largest eigenvalues. These vectors are columns of Λ<sup>ˆ</sup> that solves maximization task (12) The fact that _SX_ is a symmetric positive semi-definite matrix guarantees that it has real-valued eigenvector and eigenvalues. Columns of Λ<sup>ˆ</sup> are nothing but the first _K_ + _M_ principal components of _X_ . Knowing solution to (12) one can easily find _α_ ˆ _t_ from (8). Stock and Watson (2002) showed that under certain conditions on N, that should be "large", econometrician may use only first K principle components and obtain consistent estimator of space spanned by _Yt_ and _Ft_ . It is important to note, that at this moment we did not rely on the fact that _Yt_ is observable. For now we got _K_ linear combinations of _Ft_ and _Yt_ . In Bernanke et al. (2005) authors then perform purification procedure, which consists in "removing" _Yt_ from the space spanned by the first _K_ principal component of _Xt_ . 

For stage 2 authors divide variables into two groups: fast-moving and slow-moving. The first group assumed to contemporaneously react to unexpected shocks in _Yt_ , whereas the second one does not respond to unanticipated fluctuations in _Yt_ at a period _t_ . Such variables’ separation is necessary for obtaining purified factors _Ft_ , that contains all the information apart from that in _Yt_ . Since impulse response functions are the main focus in Bernanke et al. (2005), an absence of immediate response in _Ft_ to shocks in _Yt_ is one of the requirements in some SVAR identification schemes, such as recursive identification including Cholesky decomposition of residuals covariance matrix. However, there is a place for experiments if one tries to employ FAVAR methodology for forecasting purposes. In literature, there are several ways to remove dependence of obtained in stage 1 factors from _Yt_ . The one used in Bernanke et al. (2005) will be described below. 

15 

ˆ (8) (12) Let _C_<sup>ˆ</sup> ( _Ft,Yt_ )<sup>def</sup> = Λ<sup>ˆ</sup> _α_ ˆ _t_ = (Λ<sup>ˆ</sup><sup>_′_ˆ</sup> Λ)<sup>_−_1 ˆ</sup> Λ<sup>_′_</sup> _Xt_ = Λ<sup>_′_</sup> _Xt_ . The authors estimate the following model: 



– – where _C_<sup>ˆ</sup> ( _Ft,Yt_ ) are the first _K_ principle components of _Xt_ ; _C_<sup>ˆ</sup><sup>_slow_</sup> ( _Ft_ ) the – – first _K_ principle components of _Xt_<sup>_slow_</sup> ; _b_ 0 _K ×_ 1 vector; _b−_ 0 _K × K_ matrix; – – _γ K × M_ vector ; _νt K ×_ 1 error vector. Though, at this step one may include subset of _Yt_ variables. One can obtain _β_<sup>ˆ</sup> and _γ_ ˆ using simple OLS method by rows. 



The estimates of _Ft_ allows us to substitute _Ft_ by _F_<sup>ˆ</sup> _t_ in (2), which result in: 



Note once again that (14) in a standard VAR model in ( _F_<sup>ˆ</sup> _t,Yt_ ) , therefore Φ( _L_ ) can be estimated using traditional VAR techniques. Summarising all, we finally get: 

Algorithm 1 FAVAR estimation 

_C_ ( _Ft,Yt_ ) _←_ the first K components of _Xt_ 

_C_<sup>_slow_</sup> ( _Ft_ ) _←_ the first K components of _Xt_<sup>_slow_</sup> 

OLS estimation results _← C_<sup>ˆ</sup> ( _Ft,Yt_ ) = _β_<sup>ˆ</sup> 0 + _β_<sup>ˆ</sup> _−_ 0 _C_<sup>ˆ</sup><sup>_slow_</sup> ( _Ft_ )+ ˆ _γYt_ 

ˆ ˆ ˆ _− Ft ← β−_ 0 _C_ ˆ<sup>_slow_</sup> ( _Ft_ ) _γYt_ 

_d ←_ VAR ( _F_<sup>ˆ</sup> _t,Yt_ ) lag selection according to AIC 



The explained procedure was used in Bernanke et al. (2005) for producing impulse response functions to policy shock. Purification is necessary for producing factors that do not respond contemporaneously to a policy shock, 

16 

since authors used recursive identification with FFR (Federal Funds Rate) ordering last. For forecasting purposes, one may try to remove the impact of other variables (from _Xt_ ) or skip factor purification procedure at all. 

## 2.4 Model specifications 

Once an econometrician has estimated Φ<sup>ˆ</sup> ( _L_ ) in (14), h-horizon forecast for ( _F_<sup>ˆ</sup> _t−_ 1 _,Yt−_ 1) is the following: 



For a particular variable forecast, a researcher takes the corresponding component of _Y_<sup>ˆ</sup> _t_ + _h−_ 1 vector. One should also specify parameter _K_ representing a number of latent factors. I find, that _K_ = 1 is sufficient in most cases. However, _K_ = 2 sometimes helps to obtain more accurate results in short-term prediction, Interesting that _K ≥_ 3 generally increases the model’s error for almost all horizons. There is a space for experiments still, one may receive more accurate results at some horizons selecting proper variables for _Yt_ . 

Another approach, is to treat variable of interest _zt_ as "informational" (included in _Xt_ ), but I found no clear evidence that such a method is more preferable than assuming _zt_ being observed. These different FAVARs produce quite similar results, however, there is a still place for experiments in the choice of _Yt_ vector components. 

# 3 Data 

Data was collected from the Thomson Reuters database. Dataset includes 199 monthly variables, that represent the economic situation in Russia, start- 

17 

ing from 01/01/2000 and contains 240 observations maximum. Variables with missing values were dropped before the estimation procedure. To be in line with Bernanke et al. (2005) original time series were transformed (one or two times differencing) to assure stationarity according to KPSS test. In addition, for convenience original time series were standardized to have zero mean and unit standard deviation. Though, in order to obtain fair results, a seasonal component in considered time series was not removed, since benchmark models are capable of handling seasonality in data. One can still decompose original time series on seasonal and trend components, though FAVAR methodology cannot be applied to produce seasonal component forecasts, so it becomes a mix of FAVAR and another model for a seasonal component. Probably such an approach will yield more accurate forecasts, but the goal of this paper to check pure FAVAR model prediction power. 

Depending on the variable being forecasted different number of observations were used: 238 in case of CPI and unemployment rate, 138 in case of GDP Y/Y % change forecasts. 

# 4 Results 

In order to understand FAVAR model’s predictive power I decided to compare its results on cross-validation with popular univariate models, such as ETS, ARIMA, and simple random walk with drift; and restricted to FAVAR model – standard VAR ( _K_ = 0) . I treat variable of interest as being observed, so include it directly in _Yt_ vector. For ARIMA and ETS optimal model selection I used auto-ARIMA and auto-ETS functions in the "forecast" R package, that select best model specification according to AIC. Optimal lag of VAR models is also selected using AIC. 

18 

|||FAVAR|ARIMA|ETS|VAR|RWD|
|---|---|---|---|---|---|---|
|h|=1|0.70*|0.86|0.76|0.83|0.93|
|h|=2|0.95*|1.09|1.02|1.07|1.37|
|h|=3|1.01*|1.07|1.06|1.12|1.54|
|h|=4|0.96*|1.03|1.10|1.13|1.58|
|h|=5|0.91*|1.03|1.05|1.13|1.49|
|h|=6|0.95*|1.07|1.07|1.15|1.47|
|h|=7|1.00*|1.05|1.19|1.17|1.65|
|h|=8|1.06|0.96*|1.24|1.19|1.78|
|h|=9|1.05|0.99*|1.26|1.18|1.75|
|h|=10|0.94*|0.98|1.21|1.02|1.57|
|h|=11|0.90*|0.99|1.23|0.97|1.35|
|h|=12|0.90*|1.04|1.16|0.98|1.08|



Table 1: RMSE _×_ 100 for CPI forecasts 

Table 1 shows cross-validation results for CPI forecasting. FAVAR specification includes two variables in _Yt_ = ( _aRUCPIt, RUCBIR_ = _ECIt_ )<sup>_′_</sup> and one latent factor _K_ = 1 . Interesting that expanding number of factors deteriorates the model’s quality. One can see, that such FAVAR specification completely outperforms other models almost at each horizon. 

||FAVAR|ARIMA|ETS|VAR|RWD|
|---|---|---|---|---|---|
|h=1|10.31|6.97*|9.90|7.13|11.39|
|h=2|10.25|6.95|9.75|6.74*|10.97|
|h=3|8.68|6.56|9.90|6.52*|10.06|
|h=4|8.04|6.60|9.86|6.36*|12.06|
|h=5|6.88|5.86|10.02|6.22*|12.00|



19 

|h=|6|6.10|5.94*|9.70|6.44|11.36|
|---|---|---|---|---|---|---|
|h=|7|5.74*|6.00|9.27|6.56|12.64|
|h=|8|5.71*|6.09|9.57|6.44|10.90|
|h=|9|6.15*|6.15|9.66|6.17|10.40|
|h=|10|5.90*|5.96|9.21|6.42|10.10|
|h=|11|5.86*|5.89|9.67|6.52|9.32|
|h=|12|6.43|5.70*|9.51|6.43|9.09|



Table 2: RMSE _×_ 100 for unemployment rate forecasts 

Table 2 shows models’ cross-validation errors in attempts to forecast unemployment rate in Russia. In this FAVAR specification _Yt_ = ( _aRUCPIt, RUUNR_ = _ECIt_ )<sup>_′_</sup> and _K_ = 1 . As with CPI, increasing of _K_ leads to weak performance. As one can see, for unemployment rate FAVAR produces best forecasts only on long horizons. Yet one can experiment with proper _Yt_ selection to obtain lower error at short-term forecasts. 

||FAVAR|ARIMA|ETS|VAR|RWD|
|---|---|---|---|---|---|
|h=1|19.88*|22.34|21.67|20.10|38.56|
|h=2|20.44*|23.22|22.07|20.79|25.65|
|h=3|21.92*|23.79|22.59|22.37|35.73|
|h=4|22.40|23.13|22.35|22.31*|31.02|
|h=5|22.96|23.49|22.94|22.90*|34.74|
|h=6|22.75|22.98|22.82|22.68*|30.00|
|h=7|23.06*|23.66|23.15|23.17|35.66|
|h=8|23.46*|24.45|23.53|23.51|34.69|
|h=9|24.52|25.21|24.29|24.25*|33.81|
|h=10|22.74|25.06|22.72*|22.75|33.99|



20 

|h=11|22.98|24.59|22.74|22.70*|33.43|
|---|---|---|---|---|---|
|h=12|23.09*|24.29|23.15|23.17|25.37|



Table 3: RMSE _×_ 100 for GDP forecasts 

In table 3 one can find cross-validation errors of compared models, that are used for GDP growth rate forecasts. It is important to mention again, that for GDP only 168 observations were used, because of missing values. That might be one reason for explaining the model’s performance. Surprisingly, FAVAR produces best forecasts mostly for short-term, rather than for long-term horizons as was expected. FAVAR in _Yt_ = ( _RUGDP_ = _ECIt, RUCBIR_ = _ECIt_ )<sup>_′_</sup> with _K_ = 2 shows best performance on 6 out of 12 horizons, though difference is significant only for _h_ = 1 _,_ 3 . 

# 5 Conclusion 

Results showed that FAVAR is quite competitive model in a forecasting task, even though it was initially developed as the solution for "price puzzle", that is more about impulse response functions, rather than predictions. For some series FAVAR can completely outperform traditional univariate models as well as multivariate VAR. Besides, FAVAR allows incorporating as many variables as one wants and there are reasons to believe that this will improve the model’s performance. Nevertheless, it remains a question whether the cost of data collection outweighs potential forecast improvement for standard VAR. 

21 

# Appendixes 

# A Data Description 

The table below provides information about the used dataset. An asterisk (*) after mnemonic of some series shows that such variables were assumed to be slow-moving. Each time series is provided with the transformation code – – applied to the original data: _l_ no transformations, ∆ first difference and – ∆<sup>2</sup> second difference. 

|Mnemonic|Description||
|---|---|---|
|1. aRUPTTTT/C*|Passenger Transport Turnover, Price Index|_l_|
|2. aRUFTTCTT/C*|Freight Transport Turnover, Cargo transport,<br>Volume Index|_l_|
|3. aRUCEXBA*|Exports of Goods, Balance of Payments Basis,<br>Standardized, Current Prices|∆|
|4. aRUCIMBA*|Imports of Goods, Balance of Payments Basis,<br>Standardized, Current Prices|∆|
|5. aRUCBOPA*|Visible Trade Balance, Balance of Payments Ba-<br>sis, Standardized, Current Prices|_l_|
|6. aRUCEXBPA*|Exports of Goods, Balance of Payments Basis,<br>% month on month, Standardized, Chg P/P,<br>Current Prices|_l_|
|7. aRUCIMBPA*|Imports of Goods, Balance of Payments Basis,<br>% month on month, Standardized, Chg P/P,<br>Current Prices|_l_|
|8. aRUCBOPPA*|Visible Trade Balance, Balance of Payments Ba-<br>sis, month on month, Standardized, Absolute<br>change, Current Prices|_l_|



22 

|9. aRUCEXBYA*|Exports of Goods, Balance of Payments Basis,|∆|
|---|---|---|
||% year on year, Standardized, Chg Y/Y, Cur-<br>rent Prices||
|10. aRUCIMBYA*|Imports of Goods, Balance of Payments Basis,<br>% year on year, Standardized, Chg Y/Y, Cur-<br>rent Prices|∆|
|11. aRUCBOPYA*|Visible Trade Balance, Balance of Payments<br>Basis, year on year, Standardized, Absolute<br>change, Current Prices|_l_|
|12. RUCBIR=ECI|Central bank key rate|∆|
|13. aRUBCFBNKA|Bank Lending: Loans to banks (in frgn. cur.),<br>Current Prices|∆|
|14. aRUDOMDET|Domestic Debt, Current Prices|∆<sup>2</sup>|
|15. aRUBCDBNKA|Bank Lending: Loans to banks (in rubles), Cur-<br>rent Prices|∆|
|16. RUCPIY=ECI*|CPI, Chg Y/Y|∆|
|17. aRUCPI*|CPI, Price Index|∆|
|18. aRUCCPIYF*|CPI, % year on year, Standardized, Chg Y/Y,<br>Price Index|∆|
|19. aRUCCPIF/C*|CPI, Standardized, Price Index|∆|
|20. aRUCPFYYF*|CPI, Food products, Chg Y/Y|∆|
|21. aRUCPCORIF*|CPI, Core infation, Chg Y/Y|∆|
|22. aRUCCPIYE/A*|CPI, % year on year, Standardized, Chg Y/Y,<br>Price Index, SA|∆|
|23. aRUCCPIPF*|CPI, % month on month, Standardized, Chg<br>P/P, Price Index|∆|



23 

|24. aRUCCORYE/A*|Core CPI, Standardized, Chg Y/Y, Price Index,<br>SA|∆|
|---|---|---|
|25. aRUCCPIPE/A*|CPI, % month on month, Standardized, Chg<br>P/P, Price Index, SA|∆|
|26. aRUCPNYYF*|CPI, Non-food products, Chg Y/Y|_l_|
|27. aRUCPIF*|CPI, Food and beverages, Price Index|_l_|
|28. aRUCPISERV*|CPI, Services, Price Index|∆|
|29. aRUCPIXF*|CPI, Non-food goods, Price Index|_l_|
|30. aRUCPGOODF/C*|CPI, Goods, Price Index|_l_|
|31. aRUGOODSF*|CPI, Goods, Chg Y/Y|∆|
|32. aRUCPFPFVF/C*|CPI, Food products without fruits and vegeta-<br>bles, Price Index|∆|
|33. aRUCCPIE/CA*|CPI, Standardized, Price Index, SA|∆|
|34. aRUCCORF/C*|Core CPI, Standardized, Price Index|∆|
|35. aRUCCORE/CA*|Core CPI, Standardized, Price Index, SA|∆|
|36. aRUCCORPF*|Core CPI, Standardized, Chg P/P, Price Index|∆|
|37. aRUCCORPE/A*|Core CPI, Standardized, Chg P/P, Price Index,<br>SA|∆|
|38. aRUCCORYF*|Core CPI, Standardized, Chg Y/Y, Price Index|∆|
|39. RUCPIY=ECIX*|CPI, Chg Y/Y|∆|
|40. aRUCPFWFVF*|CPI, Food products without fruits .and vegeta-<br>bles, Chg Y/Y|∆|
|41. aRUCPICORY/C*|CPI, Core CPI, Price Index|∆|
|42. aRUCPNPSVF*|CPI, Paid services, Chg Y/Y|∆|
|43. aRUCPICOR/C*|CPI, Core CPI, Price Index|∆|
|44. aRUCLEAD|Composite leading indicators, Trend restored,<br>SA|∆|



24 

|45. aRUEMPLMT*|Employment, Volume|∆|
|---|---|---|
|46. aRUBISRXBR|BIS, Real Broad Efective Exchange Rate Index|∆|
|47. aRUCXTWF/C|Trade Weighted nominal exchange rate, Stan-<br>dardized, Price Index|∆|
|48. aRUCXTWPF|Trade Weighted nominal exchange rate,<br>%<br>month on month, Standardized, Chg P/P, Price<br>Index|_l_|
|49. aRUCXTWYF|Trade Weighted nominal exchange rate, % year<br>on year, Standardized, Chg Y/Y, Price Index|_l_|
|50. aRUCXTRF/C|Trade Weighted real exchange rate, Standard-<br>ized, Price Index|∆|
|51. aRUCXTRPF|Trade Weighted real exchange rate, % month on<br>month, Standardized, Chg P/P, Price Index|_l_|
|52. aRUCXTRYF|Trade Weighted real exchange rate, % year on<br>year, Standardized, Chg Y/Y, Price Index|_l_|
|53. aRUIRECE/C|Real efective exchange rate (REER) based on<br>consumer price index, 2010=100, Not SA, Price<br>Index|∆|
|54. aRUINECE/C|Nominal efective exchange rate (NEER) based<br>on consumer price index, 2010=100, Not SA,<br>Price Index|∆|
|55. aRUBISNXBR|BIS, Nominal Broad Efective Exchange Rate<br>Index|∆|
|56. aRUXRUSD|Russian roubles to US $|∆|
|57. RUGDP=ECI*|GDP, Chg Y/Y|∆|
|58. aRUTREV*|Revenue, Federal budget, Current Prices|∆|
|59. aRUPFEXP*|Expenditure, Current Prices|∆|



25 

|60. aRUCBUDIC*|Revenue, Consolidated budget, incomes total,|∆|
|---|---|---|
||Current Prices||
|61. aRUEXPDT*|Expenditure, Current Prices|∆|
|62. aRUGDEF*|Defcit/Surplus, Federal budget, Current Prices|_l_|
|63. aRUCGOVA*|Central government Defcit/Surplus, Standard-<br>ized, Current Prices|_l_|
|64. aRUCGOVPA*|Central government Defcit/Surplus, month on<br>month, Standardized, Absolute change, Current<br>Prices|_l_|
|65. aRUCGOVYA*|Central government Defcit/Surplus, year on<br>year, Standardized, Absolute change, Current<br>Prices|_l_|
|66. aRSCGOVBLA*|Public Finances, Central Government, Budget,<br>Balance, Defcit/Surplus, Current Prices|_l_|
|67. aRUDSCBUD*|Defcit/Surplus, Consolidated budget, Current<br>Prices|_l_|
|68. aRUDCTDA|Dwellings Commenced, Total dwellings area,<br>Volume|∆|
|69. aRUDCTI|Dwellings Commenced, Total dwellings area,<br>Price Index|∆|
|70. aRUPPICONS*|Producer Prices, Investment products, Chg P/P|∆|
|71. RUTRD=ECI*|Trade Balance, Total, Free On Board, Current<br>Prices|_l_|
|72. aRUEXP*|Exports, FOB, Current Prices|∆|
|73. aRUIMP*|Imports, FOB, Current Prices|∆|
|74. aRUTBAL*|Trade Balance, FOB, Current Prices|_l_|
|75. aRUEXPNGC*|Exports, Natural gas, Current Prices|_l_|



26 

|76. aRUEXPCRD*|Exports, Crude oil, Current Prices|_l_|
|---|---|---|
|77. aRUEXPDIESL*|Exports, Diesel fuel, Current Prices|_l_|
|78. aRUIMPPRO*|Exports, Petroleum products, Current Prices|_l_|
|79. aRUIMPMED*|Imports, Medicines, Current Prices|_l_|
|80. aRUIMPMNEQ*|Imports, Machinery and equipment, Current<br>Prices|_l_|
|81. aRUIMPCLOTH*|Imports, Clothing, Current Prices|∆|
|82. aRUEXPMOM*|Exports, Ferrous metals, Current Prices|_l_|
|83. aRUCEXPB/A*|Merchandise Exports, Standardized, Current<br>Prices, SA|∆|
|84. aRUCIMPB/A*|Merchandise Imports, Standardized, Current<br>Prices, SA|∆|
|85. aRUCEXPPB/A*|Merchandise Exports, % month on month, Stan-<br>dardized, Chg P/P, Current Prices, SA|_l_|
|86. aRUCEXPYB/A*|Merchandise Exports, % year on year, Standard-<br>ized, Chg Y/Y, Current Prices, SA|∆|
|87. aRUCIMPPB/A*|Merchandise Imports, % month on month, Stan-<br>dardized, Chg P/P, Current Prices, SA|_l_|
|88. aRUCIMPYB/A*|Merchandise Imports, % year on year, Standard-<br>ized, Chg Y/Y, Current Prices, SA|∆|
|89. aRUCVISB/A*|Visible Trade Balance, Standardized, Current<br>Prices, SA|_l_|
|90. aRUCVISPB/A*|Visible Trade Balance, month on month, Stan-<br>dardized, Absolute change, Current Prices, SA|_l_|
|91. aRUCVISYB/A*|Visible Trade Balance, year on year, Standard-<br>ized, Absolute change, Current Prices, SA|_l_|
|92. RUTRD=ECIX*|Trade Balance, Total, Free On Board|_l_|



27 

|93. RUIP=ECI*|Production, IP Total , Chg Y/Y|_l_|
|---|---|---|
|94. aRUIP*|Production, Chg Y/Y|_l_|
|95. aRUIPOIL*|Production, Oil output, including gas conden-<br>sate, Volume|∆|
|96. aRUCINDG/A*|Industrial Production Index, Standardized, Vol-<br>ume Index, SA|∆|
|97. aRUIPNAG*|Production, Natural gas output, Volume|_l_|
|98. aRUIPMANH/C*|Production, Manufacturing, Volume Index|_l_|
|99. aRUIPMANG*|Production, Manufacturing, Chg Y/Y|_l_|
|100. aRUINP/C*|Production, Industry, Volume Index|∆|
|101. aRUCINDPG/A*|Industrial Production Index, Standardized, Chg<br>P/P, Volume Index, SA|_l_|
|102. aRUCINDYG/CA*|Industrial Production Index, % year on year,<br>Standardized, Chg Y/Y, Volume Index, SA|_l_|
|103. RUIP=ECIX*|Production, IP Total, Chg Y/Y|_l_|
|104. aRUPRATE|Policy Rates, Minimum Rate on 7 Day Repo|∆|
|105. aRUINTRES|Reserves, Gross international, Current Prices|∆|
|106. aRUFXRES|Reserves, Foreign currency reserves, Current<br>Prices|∆|
|107. aRUFCRES|Reserves, Foreign currency, Current Prices|∆|
|108. aRUCRESA|Ofcial international reserves,<br>Standardized,<br>Current Prices|∆|
|109. aRURESGLD|Reserves, Gold, Current Prices|∆|
|110. aRUCRESPA|Ofcial international reserves, % month on<br>month, Standardized, Chg P/P, Current Prices|∆|
|111. aRUCRESYA|Ofcial international reserves, % year on year,|∆|
||Standardized, Chg Y/Y, Current Prices||



28 

|112. aRURTM1A1A|Ofcial reserve assets, Foreign currency, Current<br>Prices|∆<sup>2</sup>|
|---|---|---|
|113. aRURESSDR|Reserves,<br>Special Drawing Rights,<br>Current<br>Prices|∆|
|114. aRURTM1AA|Ofcial reserve assets, Overall, Current Prices|∆|
|115. aRURESIMF|Reserves, Reserve position in the IMF, Current<br>Prices|∆|
|116. aRUM2|Money supply M2 by national defnition, Cur-<br>rent Prices|∆|
|117. aRUM0|Money supply M0, Current Prices|∆|
|118. aRUNM1|Money Supply - M1, Current Prices|∆|
|119. aRUMNBAS|Monetary base (narrow defnition), Current<br>Prices|∆|
|120. aRUMBASMOC|Monetary<br>base<br>(broad<br>defnition),<br>Current<br>Prices|∆|
|121. aRUMSMBBRA|Broad money liabilities, Current Prices|∆|
|122. aRUCMS2B/A|Money<br>Supply<br>M2,<br>Standardized,<br>Current<br>Prices, SA|∆|
|123. aRUCMS2PB/A|Money Supply M2, % month on month, Stan-<br>dardized, Chg P/P, Current Prices, SA|_l_|
|124. aRUCMS2YB/A|Money Supply M2, % year on year, Standard-<br>ized, Chg Y/Y, Current Prices, SA|∆|
|125. aRUCMS1B/A|Money<br>Supply<br>M1,<br>Standardized,<br>Current<br>Prices, SA|∆|
|126. aRUCMS0B/A|Money<br>Supply<br>M0,<br>Standardized,<br>Current<br>Prices, SA|∆|



29 

|127. aRUCMS1PB/A|Money Supply M1, Standardized, Chg P/P,<br>Current Prices, SA|_l_|
|---|---|---|
|128. aRUCMS0PB/A|Money Supply M0, Standardized, Chg P/P,<br>Current Prices, SA|_l_|
|129. aRUCMS1YB/A|Money Supply M1, Standardized, Chg Y/Y,|∆|
||Current Prices, SA||
|130. aRUCMS0YB/A|Money Supply M0, Standardized, Chg Y/Y,|∆|
||Current Prices, SA||
|131. RUPPI=ECI*|Producer Prices, Chg P/P|_l_|
|132. RUPPIY=ECI*|Producer Prices, Chg Y/Y|_l_|
|133. aRUPPI/C*|Producer Prices, Price Index|∆|
|134. aRUPPITCP*|Producer Prices, Chg P/P|_l_|
|135. aRUPPIF*|Producer Prices, Chg Y/Y|_l_|
|136. aRUCPPIE/CA*|Producer Prices, PPI, Standardized, Price In-<br>dex, SA|∆|
|137. aRUPPIAR*|Producer Prices, Chg P/P|_l_|
|138. aRUCPPIF/C*|Producer Prices, PPI, Standardized, Price Index|∆|
|139. aRUCPPIPE/A*|Producer Prices, PPI, % month on month, Stan-<br>dardized, Chg P/P, Price Index, SA|_l_|
|140. aRUCPPIPF*|Producer Prices, PPI, % month on month, Stan-<br>dardized, Chg P/P, Price Index|_l_|
|141. aRUCPPIYE/A*|Producer Prices, PPI, % year on year, Standard-<br>ized, Chg Y/Y, Price Index, SA|∆|
|142. aRUCPPIYF*|Producer Prices, PPI, % year on year, Standard-<br>ized, Chg Y/Y, Price Index|∆|
|143. RUPPI=ECIX*|Producer Prices, Chg P/P|_l_|
|144. RUPPIY=ECIX*|Producer Prices, Chg Y/Y|_l_|



30 

|145. aRUPPIYAR*|Producer Prices, Chg Y/Y|_l_|
|---|---|---|
|146. aRUPPITC*|Producer Prices, Price Index|∆|
|147. RURSLY=ECI*|Retail Sales YY, Price Index|∆|
|148. aRURSLS*|Retail Trade Turnover, Current Prices|∆|
|149. aRURSLSTO*|Retail Trade Turnover, Price Index|∆|
|150. aRUCRETF/C*|Retail Sales, Standardized, Price Index|∆|
|151. aRUCRETE/CA*|Retail Sales, Standardized, Price Index, SA|∆|
|152. aRUCRETPF*|Retail Sales, Standardized, Chg P/P, Price In-<br>dex|_l_|
|153. aRUCRETPE/A*|Retail Sales, Standardized, Chg P/P, Price In-<br>dex, SA|∆|
|154. aRUCRETYF*|Retail Sales, Standardized, Chg Y/Y, Price In-<br>dex|∆|
|155. aRUCRETYE/A*|Retail Sales, Standardized, Chg Y/Y, Price In-<br>dex, SA|∆|
|156. RURSLY=ECIX*|Retail Sales YY|∆|
|157. aRURTTNFC*|Retail Trade Turnover, Non-food commodities,<br>Current Prices|∆|
|158. aRURSLS/C*|Retail Trade Turnover, Volume Index|_l_|
|159. aRURTTFC*|Retail Trade Turnover, Food commodities, Cur-<br>rent Prices|∆|
|160. aRUGBOND|Bid|∆|
|161. aRUSHRPRCF|MICEX, Composite Index, Price Index|∆|
|162. aRUWANMAVWG*|Wages, Nominal average monthly per worker,<br>Current Prices|∆|
|163. aRUWSAMTCPP*|Wages, Real average monthly, Volume Index|∆|
|164. aRUCWAGF/C*|Wages, total, Standardized, Price Index|∆|



31 

|165. aRUCWAGPF*|Wages, total, % month on month, Standardized,<br>Chg P/P, Price Index|_l_|
|---|---|---|
|166. aRUCWAGYF*|Wages, total, % year on year, Standardized, Chg<br>Y/Y, Price Index|∆|
|167. aRUAVGMANW*|Average monthly accrued nominal wages, Cur-<br>rent Prices|∆|
|168. RUUNR=ECI*|Unemployment, Rate|∆|
|169. RURWGE=ECI*|Real Wages YY, Chg Y/Y|∆|
|170. aRUUNR*|Unemployment, Rate|∆|
|171. aRUUNTOTR*|Uneployment rate, ILO|∆|
|172. aRUPOPEA*|Economically active population - Unemployed,<br>Volume|∆|
|173. aRUCUNPQ/A*|Unemployment rate, Standardized, SA|∆|
|174. aRUUEMPILO*|Unemployment, Total persons (ILO), aged 15<br>and over, Volume|∆|
|175. aRUUEMP*|Unemployment, Ofcially registered, Volume|∆|
|176. aRUUNRAR*|Unemployment, Rate|∆|
|177. aRUCUNPPQ/A*|Unemployment rate, month on month, Stan-<br>dardized, SA|_l_|
|178. aRUCUNPYQ/A*|Unemployment rate, year on year, Standard-<br>ized, SA|_l_|
|179. aRUCUNPO*|Unemployment Level, Standardized, Volume|∆|
|180. aRUCUNPP*|Unemployment Level, Standardized, Volume|∆|
|181. aRUCUNPPO/A*|Unemployment Level, % month on month, Stan-<br>dardized, Chg P/P, Volume, SA|_l_|
|182. aRUCUNPPP*|Unemployment Level, % month on month, Stan-|_l_|
||dardized, Chg P/P, Volume||



32 

|183. aRUCUNPYO*|Unemployment Level, % year on year, Standard-|_l_|
|---|---|---|
||ized, Chg Y/Y, Volume||
|184. aRUCUNPYP*|Unemployment Level, % year on year, Standard-<br>ized, Chg Y/Y, Volume|_l_|
|185. RURWGE=ECIX*|Real Wages YY, Chg Y/Y|∆|
|186. RUUNR=ECIX*|Unemployment, Rate|∆|
|187. aRUUNRRILO*|Unemployment,<br>Rate,<br>Ofcially<br>registered<br>(ILO)|∆|
|188. .IRTS|RTS Index|∆|
|189. .IMOEX|MOEX Russia Index|∆|
|190. .RTSOG|RTS Oil & Gas Index|∆|
|191. .RTSTL|RTS Telecom Index|∆|
|192. BrentP|Brent Price nominal|∆|
|193. BrentPP|Brent Price (%)|_l_|
|194. WTIP|WTI Price nominal|∆|
|195. WTIPP|WTI Price (%)|_l_|
|196. RUEURP|Russian roubles to EU e, Close|∆|
|197. RUEURMAX|Russian roubles to EsU e, Max|∆|
|198. RUEURMIN|Russian roubles to EU e, Min|∆|
|199. RUEURPP|Russian roubles to EU e, % change|_l_|



33 

# References 

- Berggren, E. and Lodenius, E. (2016). Can favar improve swedish inflation forecasting? 

- Bernanke, B. S., Boivin, J., and Eliasz, P. (2005). Measuring the effects of monetary policy: a factor-augmented vector autoregressive (favar) approach. The Quarterly journal of economics, 120(1):387–422. 

- Figueiredo, F. M. R. and Guill´en, O. (2013). Forecasting brazilian consumer inflation with favar models using target variables. Technical report, mimeo. 

- M¨onch, E. (2008). Forecasting the yield curve in a data-rich environment: A no-arbitrage factor-augmented var approach. Journal of Econometrics, 146(1):26–43. 

- Pang, I. A. J. (2010). Forecasting hong kong economy using factor augmented vector autoregression. 

- Sims, C. A. (1980). Martingale-like behavior of prices. 

- Sims, C. A. (1992). Interpreting the macroeconomic time series facts: The effects of monetary policy. European economic review, 36(5):975–1000. 

- Stock, J. H. and Watson, M. W. (2002). Macroeconomic forecasting using diffusion indexes. Journal of Business & Economic Statistics, 20(2):147– 162. 

- Stock, J. H. and Watson, M. W. (2005). Implications of dynamic factor models for var analysis. Technical report, National Bureau of Economic Research. 

34 

