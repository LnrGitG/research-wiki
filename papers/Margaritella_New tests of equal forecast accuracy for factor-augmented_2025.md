---
title: Margaritella_New tests of equal forecast accuracy for factor-augmented_2025
type: paper
source_pdf: raw/papers/Margaritella_New tests of equal forecast accuracy for factor-augmented_2025.pdf
converted: 2026-08-18
---

**<mark>ARTICLE IN PRESS</mark>** 

International Journal of Forecasting xxx (xxxx) xxx 



Contents lists available at ScienceDirect 

# International Journal of Forecasting 

journal homepage: www.elsevier.com/locate/ijforecast 



# New tests of equal forecast accuracy for factor-augmented regressions with weaker loadings 

## Luca Margaritella<sup>a</sup> , Ovidijus Stauskas<sup>b,∗</sup> 

a _Lund University, Department of Economics, Sweden_ b _BI Norwegian Business School, Department of Economics, Norway_ 

|a r t i c l e i n f o|a b s t r a c t|
|---|---|
|_Article_ _history:_<br>|We provide the theoretical foundation for the recent tests of equal forecast accuracy|
|Dataset link:GitHub - New Tests of Equal F<br>orecast Accuracy for Factor-Augmented Reg<br>ressions with Weaker Loadings|and encompassing by Pitarakis (2023) and Pitarakis (2025), when the competing forecast<br>specification is that of a factor-augmented regression model. This should be of interest<br>to practitioners, as there is no theory justifying the use of these simple and powerful<br>|
|_Keywords:_<br>Forecast accuracy<br>Factor-augmented regressions<br>Weak loadings|tests in such a context. In pursuit of this, we employ a novel theory to incorporate<br>the empirically well-documented fact of homogeneously/heterogeneously weak factor<br>loadings, and track their effect on the forecast comparison problem.<br>© 2025 The Author(s). Published by Elsevier B.V. on behalf of International Institute of|
|Principal component analysis (PCA)<br>|Forecasters. This is an open access article under the CC BY license|
|Nested models|(http://creativecommons.org/licenses/by/4.0/).|



### **1. Introduction** 

Assessing the _out-of-sample_ forecast performance of different models is fundamental for practitioners deciding which specification to employ. Central banks, investment banks, and government economic planning agencies routinely employ forecasting models to make informed decisions and implement effective policies. Therefore, evaluating the _population_ predictive ability of various alternative models is for them essential.<sup>12</sup> Competing forecasts may differ in setup (e.g. forecasting inflation via linear regression or exponential smoothing), but the focus is often on augmenting a linear model with additional predictors. In such cases, models are nested under the null hypothesis of equal forecast accuracy. Nesting comes naturally in the validation of economic theories. For instance, inflation ( _πt_ ) can be forecast using an AR(1) 

∗ Corresponding author. 

model, or alternatively, using an ARX(1) model as _πt_ = _γ_ 1 + _γ_ 2 _πt_ −1 + _γ_ 3 _ιt_ −1 + _νt_ , where interest rates ( _ιt_ ) serve as exogenous input. Under the null hypothesis then, _γ_ 3 = 0. Another example of this is forecast accuracy comparisons against random walk models in the field of exchange rates, as considered by Rossi (2005) (see Pitarakis, 2025 for an overview). 

While natural, nested comparisons nowadays go hand in hand with a high-dimensional setting. With the availability of large contemporary datasets, researchers and practitioners face an abundance of potential predictors that may or may not improve forecasts beyond standard autoregressive specifications. By far the most popular approach to condense the predictive information is to employ the factor structure (see the survey by Eickmeier & Ziegler, 2008). Here, a large number of potential predictors load on a small number of latent series (factors) that drive their co-movement.<sup>3</sup> Therefore, a factor-augmented forecast is the hallmark example of a nested setup. It 

_E-mail address:_ ovidijus.stauskas@bi.no (O. Stauskas). 

1 We stress the _out-of-sample_ and _in-population_ because ‘in-sample’ mean-squared-error-based forecasts, and the horse races thereof, are void of statistical grounds; see among others (Diebold, 2015). 

2 The numerical results presented in this manuscript were reproduced by the Editor-in-Chief on 12 November 2025. The results may be sensitive to the Matlab version being used to run the code. 

3 To be precise, factor models are not a dimension-reduction technique per se; it is only the reduced rank assumption on the common component, combined with white noise-like assumptions on the idiosyncratics, which have the desired reduction effect (see e.g. Barigozzi & Hallin, 2024, for an excellent discussion). However, for macroeconomic applications, these are often reasonable assumptions. 

https://doi.org/10.1016/j.ijforecast.2025.11.005 

0169-2070/© 2025 The Author(s). Published by Elsevier B.V. on behalf of International Institute of Forecasters. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). 

Please cite this article as: L. Margaritella and O. Stauskas, New tests of equal forecast accuracy for factor-augmented regressions with weaker loadings. International Journal of Forecasting (2026), https://doi.org/10.1016/j.ijforecast.2025.11.005. 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

also constitutes a whole research industry with applications in macroeconomics and finance, where principal component analysis (PCA) is the predominant method of factor estimation to extract eigenvectors corresponding to the largest eigenvalues of the sample covariance matrix (see Bai & Ng, 2002, or Bai & Ng, 2006). Hence, it is not surprising to see two parallel strands of econometric literature. The first focuses on the robustness of the principal components procedure itself, while the second develops tests to evaluate out-of-sample forecasts with estimated factors. An important example of the former is empirically well documented and it concerns risks when the loadings through which the factors weight on the high-dimensional set of observables are weak (see the examples in Stock & Watson, 2002b, or Ludvigson & Ng, 2009). Technically, the eigenvalues diverge at a sublinear rate (see e.g. Uematsu & Yamagata, 2022, and Bai & Ng, 2023). Practically, it limits the informativeness of a dataset and may cloud forecast comparisons. Indeed, the key examples of the second strand are built only on the strong-loadings assumption, and they are the seminal work of Gonçalves et al. (2017) and Stauskas and Westerlund (2022).<sup>4</sup> They derive conditions under which (highly non-standard) asymptotic distributions of the tests of Clark and McCracken (2001) continue to hold when the competing model is augmented with estimated factors. In the current study, we merge both strands. Firstly, we re-establish standard normal inference by borrowing from the recent developments in the theory of nested environments by Pitarakis (2023, 2025). Next, we introduce the possibility of weaker loadings to quantify their effect on the forecast comparison problem. 

Statistical comparisons of nested models typically result in a non-standard inference. Particularly, under the null, the population errors of the two competing specifications are identical, leading to zero out-of-sample mean square error (MSE) differentials in the limit, as well as zero asymptotic variances. As a result, the test statistics become asymptotically ill defined. On the contrary, these problems are bypassed in the non-nested case, and asymptotic normality is relatively easy to establish (see Diebold, 2015). Such challenges motivated early works by Clark and McCracken (2001) and McCracken (2007), who introduced adaptive normalizations of the MSEs to recover well-defined asymptotic distributions of the test statistics. However, these distributions are highly nonstandard and follow stochastic integrals of Brownian motion that depend on the relative growth rate of in-sample versus out-of-sample observations. Simulation-based approaches for estimating asymptotically valid critical values exist (see Clark & McCracken, 2012, or Hansen & Timmermann, 2015), but their practical implementation is very challenging, which makes the results of Gonçalves et al. (2017) elegant, but impractical. 

More recently, Jean-Yves Pitarakis (JYP) proposed a set of tests for predictive accuracy and encompassing 

> 4 Their study, however, exploits the common correlated effects estimator by Pesaran (2006). While this method has elegant properties when the data admit a specific structure (e.g. blocks), we focus on PCA, due to its versatility. 

in nested models, avoiding the non-standardness of the asymptotic distribution of the statistics under the null, as well as the variance degeneracy issue of existing procedures. Pitarakis (2025) proposes a forecast accuracy test, still based on the MSE comparison across two nested models. However, in comparing MSEs, it uses partially overlapping out-of-sample segments to compute them, rather than the whole, same out-of-sample span. The intuition goes that as long as the fractions of out-of-sample squared forecast errors associated with the two competing specifications are different, the variance of a suitably normalized test statistic involving the MSEs cannot be degenerate. JYP then proves the asymptotic normality of two types of tests under a set of general, nonrestrictive assumptions (more details are provided in Section 2). 

Pitarakis (2023) instead offers an encompassing test— meaning that it is based on the forecast encompassing principle (see Hendry & Richard, 1982), for which if one forecast offers no additional value over another, thenyield ana loweroptimalsquaredconvexerrorcombinationloss. Definingof the˜ _u_ 1 _,t_ +two1 _,_ ˜ _u_ 2cannot _,t_ +1 as the one-step-ahead forecast errors associated with two alternative forecasts, this principle boils down to testing the population moment restriction: E( _u_ 1 _,t_ +1( _u_ 1 _,t_ +1 − _u_ 2 _,t_ +1)) = 0. However, suitably normalized sample statistics to test such a restriction are also plagued by the same issues that plague the equal predictive ability tests: variance degeneracy and the nonstandardness of asymptotics. To circumvent these, the simple and brilliant idea of Pitarakis (2023) is to consider the linear combination of two subsample means, in place of a unique sample mean, as additive sample counterparts of the population quantities. Simply enough, if [1 : _k_ 0] is the set of in-sample observations and [ _k_ 0 +1 : _T_ ] the out-of-sample’s, this means thatto bethe( _T_ −sample _k_ 0)<sup>−1 ∑</sup> counterpart<sup>_T_</sup> _t_ =<sup>−</sup> _k_<sup>1</sup> 0<sup>˜</sup><sup>_u_1</sup><sup>_,t_+1˜</sup><sup>_u_</sup> of<sup>2</sup><sup>_,t_</sup> E<sup>+</sup> [<sup>1</sup> _u_ 1<sup>but</sup> _,t_ +1<sup>1</sup> _u_<sup>_/_</sup> 2<sup>2(</sup> _,t_ +<sup>_m_</sup> 1]<sup>−</sup> 0 is<sup>1</sup> ∑not _mt_ =0 _k_ going+0 _k_ 0−1 ˜ ˜ _u_ 1 _,t_ +1 _u_ 2 _,t_ +1 + ( _T_ − _k_ 0 − _m_ 0)<sup>−1 ∑</sup><sup>_T_</sup> _t_ =<sup>−</sup> _m_<sup>1</sup> 0+ _k_ 0<sup>˜</sup><sup>_u_1</sup><sup>_,t_+1˜</sup><sup>_u_2</sup><sup>_,t_+1),</sup> for _m_ 0 being a split point that should be different from ( _T_ − _k_ 0) _/_ 2. The two subgroups of units will have slightly different variances, and that is the key to circumventing the variance degeneracy issue. As for the previous tests, JYP proves asymptotic normality of his proposed encompassing test statistics under a set of general, high-level assumptions. 

For their simplicity, robustness, and generality, JYP’s tests should be considered the new standard procedures to test for forecast accuracy and encompassing. Crucially, they have the potential to make the out-of-sample evaluation of factor-augmented forecasts much more practical. However, as of now, there is no theory formally justifying their appealing properties in this setting, as his high-level assumptions accommodate only observed, but not estimated, factors. Pitarakis (2023) only considers a factor-augmented data generating process (cf. DGP2) as a robustness check in the simulations.<sup>5</sup> Moreover, given 

> 5 Also, upon reviewing his simulations, it appears that the factors are not re-estimated at every roll of the out-of-sample window, but are just estimated once, prior to the recursion, over the whole out-ofsample span. This neglects the very out-of-sample nature of the setting (Pitarakis (2023) simulation scripts are available on the author’s GitHub page at https://github.com/jpitarakis/Multi-Step_Encompassing). 

2 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

the potential for wide applicability, it is only natural to provide the justification by reflecting the risks that occur in practice. Indeed, various routes have been taken to accommodate the weakness of factor loadings, which include local factors (see Freyaldenhoven, 2022) or sparsity, which prescribes a sparse principal component estimator as an alternative (see Uematsu & Yamagata, 2022). Only recently, Bai and Ng (2023) provided a comprehensive theory for the usual principal component estimator to determine the impact of the loading weakness. It is also more general than in the latter studies. Particularly, if the assumptions of Uematsu and Yamagata (2022) were applied to the usual principal components setting, factor loadings would need to be stronger for the factors to be identified. 

As the key contribution, we provide the theoretical framework that justifies the use of the whole set of JYP’s tests of forecast accuracy and encompassing, when the competing specification is that of a factor-augmented autoregression. The factors are estimated at every roll of the out-of-sample window (recursively), and the factor loadings are allowed to be strong, as well as homogeneously or heterogeneously weak. This leads to a technical contribution, where we re-work the weaker loadings theory in Bai and Ng (2023) to the recursive-estimation setting, which can be of independent interest. We spell out and discuss the assumptions required to show how, in all these settings, JYP’s test statistics maintain a Gaussian asymptotic distribution and appealing power properties, as long as the loadings are at most moderately weak. This extra informativeness condition is required to take into account the recursive estimation of factors. 

Finally, a few words on the notation we use throughout. Firstly, _a_ is a scalar, **a** is a vector, and **A** _t_ is a matrix with _t_ rows. For any <u>generic</u> matrix **A** , the spectral norm is ∥ **A** ∥ _sp_ =<sup>~~√~~</sup> _λ_ max( **A**<sup><u>′</u></sup> **A** ), while ∥ **A** ∥=<sup>√</sup> tr( **A**<sup><u>′</u></sup> **A** ) is the Frobenius norm with tr( _._ ) being the trace operator. The vectorization of a matrix **A** is denoted by vec( **A** ), and _λ_ min(max)( **A** ) denotes the smallest (largest) eigenvalue. Next, ⌊ _x_ ⌋ represents the integer part of _x_ , and _M_ is a positive constant, while sup _a_ ≤ _t_ ≤ _b_ (inf _a_ ≤ _t_ ≤ _b_ ) is the supremum (infimum). Moreover, _k_ 0 represents the in-sample observations, while _T_ − _k_ 0 = _n_ denotes the out-of-sample observations. Convergence in distribution and probability arevergencegivenisbygiven→ _d_ byand⇒→. Ultimately, _p_ , respectively,˜ _a_ andwhileˆ _a_ areweakquantitiesconestimated under the observed and estimated **f** _t_ . 

### **2. Econometric setup & tests** 

For _t_ = 1 _, . . . , T_ , let us consider the following forecasting model: 



where **w** _t_ ∈ R<sup>_k_</sup> , **f** _t_ ∈ R<sup>_r_</sup> , which are stacked into **z** _t_ ∈ R<sup>_k_+</sup><sup>_r_</sup> with conformable parameter vectors: **_θ_** , **_β_** , and **_δ_** . We consider **w** _t_ the ‘known factors’, and this can contain both lags of _yt_ , as well as an intercept, seasonal dummies, or time-period dummies. Instead, **f** _t_ is a vector of ‘unknown factors’. In particular, we assume that there exists a panel of _N_ series (which excludes _yt_ ) whose 

components _xi,t , i_ = 1 _, . . . , N_ , can be decomposed into two unobservable and mutually orthogonal components: a common component _χi,t_ and an idiosyncratic component _ei,t_ . Respectively, they represent the co-movements and the individual features of the series. For _χi,t_ , we assume it to be of low rank, i.e. to be driven linearly by an _r_ -dimensional vector of common static factors **f** _t_ , such that _χi,t_ = **_λ_**<sup>′</sup> _i_<sup>**f**</sup><sup>_t_,with</sup><sup>**_λ_**</sup><sup>_i_being,forevery</sup><sup>_i_,an</sup><sup>_r_dimensional</sup> vector of factor loadings. Thus, the decomposition takes the following form: 





where **F** = ( **f** 1 _, . . . ,_ **f** _T_ )<sup>′</sup> ∈ R<sup>_T_×</sup><sup>_r_</sup> , **_Λ_** = ( **_λ_** 1 _, . . . ,_ **_λ_** _N_ )<sup>′</sup> ∈ R<sup>_N_×</sup><sup>_r_</sup> is the matrix of individual factor loadings, and **E** ∈ R<sup>_T_×</sup><sup>_N_</sup> is the matrix of idiosyncratic components. 

We are interested in understanding whether the factor-augmented model ( **_β_** = **0** _r_ , ‘unrestricted’) is on average better in terms of out-of-sample forecast accuracy than a simple, possibly autoregressive model ( **_β_** = **0** _r_ , ‘restricted’). For this purpose, we split the sample _T_ into _T_ = _k_ 0 + _n_ , where _k_ 0 and _n_ are the in- and out-of-sample periods, respectively. Conveniently, we let _k_ 0 = ⌊ _T π_ 0⌋ for _π_ 0 ∈ (0 _,_ 1). Then, we produce recursive pseudo-outof-sample forecasts for the restricted and unrestricted models for _t_ = _k_ 0 _, . . . , T_ − 1 and compare their errors ˜ ′ ˜of′ the form˜′ _u_ 1 _,t_ +1 = _yt_ ˜+1′ −<sup>˜</sup> **_θ_** _t_<sup>**w**</sup><sup>_t_against˜</sup><sup>_u_2</sup><sup>_,t_+1=</sup><sup>_yt_+1 −</sup> **_θ_** and **w** _t_ henceforth,− **_β_ f** _t_ = _y_ the _t_ +1 notation− **_δ_** _t_<sup>**z**</sup><sup>_t_for</sup> ˜ _a_ (<sup>_t_</sup> ˆ _a_ )<sup>=</sup> indicates<sup>_k_0</sup><sup>_, . . . , T_</sup> an<sup>−</sup> infeasible<sup>1.Here</sup> (feasible) estimator; as such, the least squares estimator _t_ −1 −1 _t_ −1 ˜ **_δ_** _t_ = ∑ **z** _s_ **z**<sup>′</sup> _s_ ∑ **z** _sys_ +1 _,_ (2.4) ( _s_ =1 ) _s_ =1 

is indeed infeasible, given that the factors **f** _t_ are unobserved. However, we are first going to proceed as if **f** _t_ was given. The reason being that the expansions of the feasible test statistics reveal how the key component in thissibleanalysisand feasibleis indeedforecasttheerror:difference˜ _u_ 2 _,t_ +1between − ˆ _u_ 2 _,t_ +1,thesimilarlyinfeato Gonçalves et al. (2017) and Stauskas and Westerlund (2022). The boundedness of functions of this quantity is indeed the key to the main theoretical results in this paper. 

_2.1. Tests for forecast encompassing and accuracy: observed factors_ 

To begin with, we consider a total of three tests of equal forecast accuracy and encompassing. The test for forecast encompassing is given by Pitarakis (2023) and it has the following form: 



3 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

where _m_ 0 = ⌊ _nµ_ 0⌋= ⌊( _T_ − _k_ 0) _µ_ 0⌋ is a cut-off point toandsplit˜ _ω_ 1 isthetheaverageestimatedforstandard _µ_ 0 ∈ (0deviation _,_ 1), withof _µ_ the0 =limiting1 _/_ 2; distribution of the test statistic. 

Two further tests of forecast accuracy come from (Pitarakis, 2025): 



and 



Here, _l_<sup>0</sup> _j_<sup>=⌊</sup><sup>_nλ_0</sup> _j_<sup>⌋for</sup><sup>_j_=1</sup><sup>_,_2and</sup><sup>_λ_0</sup> _j_<sup>∈(0</sup><sup>_,_1)controls</sup> the two portions of the out-of-sample period over which the forecast errors of both models are compared. One can have _l_<sup>0</sup> 1<sup>_>l_0</sup> 2<sup>orviceversa,whichmeansthatbothportions</sup> are overlapping. However, an equality is ruled out in order to avoid the asymptotic degeneracy of variance. This test has a slight disadvantage when compared to that of Pitarakis (2023), because of the overlapping evaluation over the effective sample size. Some data, though in principle minimal data, are lost in the MSE comparison. Note also how (2.7) is simply an average of (2.6) over some chosen feasible set of _l_ 1 for the fixed _l_<sup>0</sup> 2<sup>(orfixed</sup><sup>_λ_0</sup> 2<sup>).The</sup> tuning parameter _τ_ 0 ∈ (0 _,_ 1) helps to pick that set.<sup>6</sup> The intuition behind the averaging is the following: if _l_<sup>0</sup> 2<sup>is</sup> fixed and _l_ 1 changes, then the MSE of the restricted model accumulates. In effect, the uncertainty over the possible choices of _l_ 1 is integrated. 

Pitarakis (2025) makes several suggestions for different avenues of averaging. One that is significant both practically and theoretically is averaging over _l_ 2 while _l_<sup>0</sup> 1 is fixed, such that the MSE of the unrestricted model accumulates. Because in practice the feasible version of the unrestricted model will contain a factor estimation error, we can track whether it interferes with an integration of the uncertainty around _l_ 2. This results in a new statistic: 



This statistic is not present in Pitarakis (2025), so as an additional contribution, we provide its full analysis. Lastly, ˜ _ω_<sup>2for</sup><sup>_j_=1</sup><sup>_, . . . ,_4representsthevarianceestimatorsof</sup> _j_ the four statistics. 

respectiveAlgorithmvariance1, below,estimatorssummarizes˜ _ω_ 1<sup>2</sup><sup>_, . . . ,_</sup> _gf ,_ 1<sup>˜</sup><sup>_ω_</sup> to4<sup>2.</sup> _gf_<sup>It</sup> _,_ 4<sup>also</sup> and their<sup>pro-</sup> vides recommendations for the tuning parameter values, which serve to boost the statistical power of the tests. The recommendations stem from a theoretical and simulation-based investigation by Pitarakis (2025), while in our simulations, we experiment with different values to explore the balance of size and power. 

**Algorithm 1** Operationalizing test statistics. 



Note that for _j_ = 1 _, . . . ,_ 4, we have _ωj_<sup>2=</sup><sup>_φ_2</sup><sup>_γ_2</sup> _j_<sup>,where</sup> _γj_<sup>2isknown.Weonlyneedtoestimate</sup><sup>_φ_2with</sup> 



where in practice we use the feasible estimator<sup>ˆ</sup> _φ_<sup>2</sup> . Similar sample variance estimators have been widely used in different exercises for factor-augmented regressions (see e.g. Bai & Ng, 2006, Gonçalves et al., 2017, or Yan & Cheng, 2022) 

For further exposition, it is convenient to split (2.5)– (2.8) into two components, such that for _j_ = 1 _, . . . ,_ 4 we have 



where _gf ,j,_ 1 generates the distribution under the null, and _g_ ∞ _f ,j_ , _,_ 2wegenerateshave that,powerunderunderthethenull,alternative.the ˜ _ωj_<sup>−</sup> Then,<sup>1</sup> -scaledas _T_ first→ component converges in distribution to a standard Gaussian density function. To see its key difference from the tests in Clark and McCracken (2001), let _σ_<sup>2</sup> = V _ar_ ( _ut_ +1) (unconditional variance). Then, the process { _u_<sup>2</sup> _t_ +1<sup>−</sup><sup>_σ_2}</sup> generates the distribution, instead of the predictors. For the local power analysis in _gf ,j,_ 2, we impose **_β_** = **_β_**<sup>0</sup> _T_<sup>−1</sup><sup>_/_4</sup> as the local alternative, similarly to Pitarakis (2023, 2025). 

6 For further discussion on how to choose the tuning parameters, we refer the reader to Pitarakis (2025), Section 3. 

4 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

Thus, we require the following assumptions on the forecast error (A.1) and on the factors and predictors (A.2). They are slightly more primitive than in the original studies in order to make them compatible with and sufficient for the feasible setup explored below. 

**A.1 (Forecast error)** 

- (i) { _ut_ } is a martingale difference sequence with respect to the filtration _Ft_ −1 = _σ_ ( **z** _t_ −1 _, . . . ,_ **X** _t_ −1 _, . . . , yt_ −1 _, . . ._ ). 

- (ii) E( _u_<sup>2</sup> _t_<sup>|</sup><sup>_Ft_−1)=</sup><sup>_σ_</sup> _t_<sup>2,sup</sup> _k_ 0≤ _t_ ≤ _T_ −1<sup>_σ_2</sup> _t_ = _Op_ (1), _σ_<sup>2</sup> = E( _σt_<sup>2).</sup> 

- (iii) sup _k_ 0≤ _t_ ≤ _T_ −1 E( _u_<sup>4</sup> _t_<sup>)</sup><sup>_<M_.</sup> 

- (iv) _ut_ is independent of all other primitives of the model ∀ _i, t, s_ . 

### **A.2 (Factors and predictors)** 



A.1(i) considers the filtration at _t_ −1. Hence, this implicitly means that we are looking at the one-step-ahead forecast. As we provide a unified theory for all of JYP’s tests, and those in Pitarakis (2025) are only for one step ahead, this choice allows us to treat them all at once. The martingale difference sequence (MDS) assumption is natural in this setting (see the same assumption in Stauskas & Westerlund, 2022 and an equivalent one in Bai & Ng, 2006, Cheng & Hansen, 2015, and Karabiyik & Westerlund, 2021). However, we note that this is merely for convenience, as further steps ahead and serial correlation can be considered. In particular, we comment on how to relax the MDS requirement in Remark 1. As it is likely to occur in practice, we can also allow for conditional heteroskedasticity (e.g. _ut_ = _σt εt_ , where _εt_ is IID(0 _,_ 1), and _σt_<sup>2representsanARCH/GARCHeffect)intheforecast</sup> error if (2.9) is replaced by a consistent HAC estimator, since { _u_<sup>2</sup> _t_ +1<sup>−</sup><sup>_σ_2}isnotMDSanymore.A.1(ii)and</sup> A.1(iv) are absent in Gonçalves et al. (2017), but they are fairly standard and allow us to bring down moment requirements on factors and idiosyncratics. Indeed, in the equivalent assumption of A.2 in Gonçalves et al. (2017), 16th moments of factors are required. In our case, it is sufficient to have 8th moments. Generally, parts (i)–(iii) of A.2 ensure that the tests of Pitarakis (2023, 2025) are asymptotically normal as required, but under lower-level conditions. For example, part (iii) is similar to the one in Clark and McCracken (2001) and Stauskas and Westerlund (2022), where {vec( **z** _t_ **z**<sup>′</sup> _t_<sup>−</sup><sup>**_Σ_z**)}</sup><sup>_T_</sup> _t_ =<sup>−</sup> _k_<sup>1</sup> 0<sup>followsamixing</sup> sequence of specific size (see Hansen, 1992). 

Proposition 1 below gives the said results for _gf ,j,_ 1 _, gf ,j,_ 2 under the above assumptions, whereas in Pitarakis (2023, 2025), they are obtained under high-level conditions. 

**Proposition 1.** _Under Assumptions A.1 and A.2, for j_ = 1 _, . . . ,_ 4 _as T_ →∞ _, one has_ 



**Proof.** Online Supplement, Section 2. 

Recall the nulls for the encompassing test, E( _u_ 1 _,t_ +1 ( _u_ 1 _,t_ +1 − _u_ 2 _,t_ +1)) = 0, and for the forecast accuracy tests, E( _u_<sup>2</sup> 1 _,t_ +1<sup>−</sup><sup>_u_2</sup> 2 _,t_ +1<sup>)=0.Bothimplythat</sup><sup>**_β_**=</sup><sup>**0**</sup><sup>_r_,and</sup> thus that _gf ,j,_ 2 → _p_ 0. Under the alternatives instead, _gf ,j,_ 2 converges to an expression that explicitly depends on the difference between the diagonal matrix **_I_** _r_ and the quadratic form of the covariances between known and unknown factors with the precision matrix of the known factors: **_Σ_**<sup>′</sup> **wf**<sup>**_Σ_**−</sup> **w**<sup>1</sup><sup>**_Σ_wf**.Notethatbydenotingalimitof</sup> _gf ,j,_ 2 by _ψ_ , we can give credence to the suggested values in Algorithm 1. For a standard normal CDF _Φ_ ( _._ ) and a quantile related to size _α_ , the power function for each test is 1 − _Φ_ ( _qα_ − _ωj_<sup>−1</sup><sup>_ψ_).As</sup><sup>_ω_</sup> _j_<sup>−1</sup> ∝ _γj_<sup>−1</sup> for a _γj_ that depends on the tuning parameters, we see that the suggestions in Algorithm 1 increase precision and boost the power. Before we move on to the case of the estimated factors, a word on the further compact notation. We note that the components of (2.5)–(2.8) can be expressed as ∑⌊ _t_ =⌊ _f_ 2( _Tf_ 1)(⌋ _T_ )⌋<sup>_du_(˜</sup><sup>_u_1</sup><sup>_,t_+1</sup><sup>_,_˜</sup><sup>_u_2</sup><sup>_,t_+1)</sup> for a loss differential _du_ ( _._ ), where ⌊ _fj_ ( _TT_ )⌋ → _qj_ for _j_ = 1 _,_ 2, such that _q_ 2 _> q_ 1. This helps conduct the analysis uniformly over different out-of-sample paths. Therefore, we compactly formulate the results in terms of ~~√~~ <u>1</u> _dT_ ∑⌊ _t_ =⌊ _f_ 2( _Tf_ 1)(⌋ _T_ )⌋<sup>_du_(</sup><sup>_._),where</sup><sup>_dT_=</sup> (⌊ _f_ 2( _T_ )⌋−⌊ _f_ 1( _T_ )⌋+ 1). Then, they apply to (2.5)–(2.8) simultaneously. **Example 1.** In the case of (2.5), the first component has ⌊ _f_ 1( _T_ )⌋= ⌊ _T π_ 0⌋= _k_ 0 and ⌊ _f_ 2( _T_ )⌋= _T_ − 1 with _q_ 1 = _π_ 0 and _q_ 2 = 1. The second component has ⌊ _f_ 1( _T_ )⌋= ⌊ _T π_ 0⌋= _k_ 0, _q_ 1 = _π_ 0, while ⌊ _f_ 2( _T_ )⌋= ⌊ _T π_ 0⌋+ ⌊( _T_ − _k_ 0) _µ_ 0⌋− 1 = _k_ 0 + _m_ 0 − 1, _<u>q</u>_ <u>2</u> = _π_ 0 + (1 − _π_ 0) _µ_ 0, and so _dT_ = _m_ 0. Then, let _MT_ = ~~√~~ _mn_ <u>0</u><sup>,suchthatwecananalyze</sup> 



_2.2. Tests for forecast encompassing and accuracy: Estimated factors_ 



where ˆ **z** _t_ = ( **w**<sup>′</sup> _t_<sup>_,_ˆ</sup> **f** _t_ ′)′. Therefore, to use (2.11) in the ‘for’ loop of Algorithm 1, we additionally obtain<sup>ˆ</sup> **F** _t_ by PCA in 

5 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

the same loop, whose procedure is defined as 



where **U** _Nt,r_ is a _t_ × _r_ matrix of eigenvectors of ( _Nt_ )<sup>−1</sup> **X** _t_ **X**<sup>′</sup> _t_<sup>.</sup> For the minimization, the usual required normalizations ′ are that _t_<sup>−1ˆ</sup> **F**<sup>′</sup> _t_<sup>ˆ</sup><sup>**F**</sup><sup>_t_=</sup><sup>**I**</sup><sup>_r_and</sup><sup>**_Λ_**ˆ</sup> _t_<sup>**_Λ_**ˆ</sup><sup>_t_isdiagonal,as</sup><sup>**_Λ_**and</sup><sup>**F**</sup> are not identified separately. We stress that **_Λ_**<sup>ˆ</sup> _t_ is indexed by _t_ , because we estimate a different loading matrix for each recursion. This implies that the forecast error for the ˆ unrestricted model is given by _u_ 2 _,t_ +1 = _yt_ +1 −<sup>ˆ</sup> _δt_<sup>′ˆ</sup><sup>**z**</sup><sup>_t_=</sup> _yt_ +1 −<sup>ˆ</sup> **_θ_** ′ _t_<sup>**w**</sup><sup>_t_−ˆ</sup><sup>**_β_**</sup> ′ _t_<sup>ˆ</sup> **f** _t_ . This estimated forecast error is used in the feasible versions of (2.5)–(2.8). 

**Example 2.** The feasible version of (2.6) is given by 



where ˆ _ω_ 2<sup>2isthefeasiblevarianceestimator.</sup> 

Our goal is now to show that (2.5)–(2.8) have the same null asymptotic distribution and power properties as in the original references of Pitarakis (2023, 2025). This applies both when **f** _t_ is observed (infeasible setting) and when the factors are estimated (feasible setting) where the loadings are allowed to be strong or weak. This means that the _r_ eigenvalues of the common component covariance matrix can diverge at a sub-linear rate in _N_ , i.e. at rate _N_<sup>_α_</sup> , for _α_ ∈ (0 _,_ 1]. Accommodation of weaker loadings will require specific assumptions, and we follow Bai & Ng, 2023, who require that _N_<sup>−</sup><sup>_α_</sup> **_Λ_**<sup>′</sup> **_Λ_** has a positive definite limit. To provide intuition, _α_ = 1 gives the usual strong loading case. Within this setting, factors and loadings can be consistently estimated with principal components yielding the usual rate of _Op_ (max(1 _/_ √ _N,_ 1 _/_ √ _T_ )). Instead, _α_ = 0 leads to absolutely uninformative loadings, similarly to Onatski (2012). For instance, let _r_ = 1, then if _N_<sup>−</sup><sup>_α_</sup> **_Λ_**<sup>′</sup> **_Λ_** =<sup>∑</sup><sup>_N_</sup> _i_ =1<sup>_λ_2</sup> _i_<sup>_<_∞,wehavesquare-summable</sup> loadings, which implies that individual loadings are practically zero for highly indexed individuals. All situations in-between give weaker (or ‘weakly influential’) loadings (see De Mol et al., 2008; Onatski, 2012). This means that as _N_ →∞ the loadings are too small or too sparse for the corresponding eigenvalues to diverge at rate _N_ (see Barigozzi & Hallin, 2024). Because of this sub-linear divergence, consistent estimation of the common component with PCA is less straightforward. As we also prove below, in the recursive estimation setup, PCA only allows us to recover the factors associated with eigenvalues that diverge at least at a rate equal to _N_<sup>_α_</sup> , for _α >_ 1 _/_ 2, which is a new result in the PCA literature (see also: Bai & Ng, 2023; Freyaldenhoven, 2022). 

Recall that<sup>ˆ</sup> **F** _t_ is the matrix of _r_ eigenvectors corresponding to the _r_ largest eigenvalues of ( _Nt_ )<sup>−1</sup> **X** _t_ **X**<sup>′</sup> _t_<sup>,and</sup> 



which accommodates the fact that we employ the usual principal components procedure when the loadings can be weaker. The next assumption imposes structure on the weaker loadings. 

**A.3 (Loadings)** 



We treat the loadings as random and make them independent from **F** _t_ in order to simplify some arguments. Alternatively, we can impose E( **f** _t_ **f**<sup>′</sup> _t_<sup>|</sup><sup>**_Λ_**)=</sup><sup>**I**</sup><sup>_r_.Theycanalsobe</sup> treated as fixed, similarly to Gonçalves et al. (2017). Moreover, as in the latter study, we impose a convergence rate to facilitate the quantification of our analysis (under _α_ = 1, it coincides with the natural _N_<sup>−1</sup><sup>_/_2</sup> rate) in the recursive setup. Naturally, this slightly strengthens the original assumption of Bai and Ng (2023). In general, (i) is a central assumption that allows us to conduct an asymptotic analysis uniformly in loading strength. A similar formulation is used by Uematsu and Yamagata (2022), but in the context of the sparse principal component estimator, and by He et al. (2025), who exploit the minimization of the Huber loss function to estimate the loadings. However, neither of these studies deals with hypothesis testing in a forecasting setting. Recently, Boot and Keijsers (2025) used the assumptions of Bai and Ng (2023) to compare 

> 7 Let us note that the singular value decomposition (and the subsequent decomposition) is here conducted on the _t_ × _t_ covariance for **X**<sup>′</sup> i.e. _Nt_<sup><u>1</u></sup><sup>**XX**′,followingtheworkofBaiandNg(2023).The</sup> same decomposition and asymptotic expansions below can be done in the (more traditional) case of taking eigenvectors of the _N_ × _N_ covariance _Nt_<sup><u>1</u></sup><sup>**X**′</sup><sup>**X**(seeBarigozzietal.,2024;Stock&Watson,2002a).</sup> Both singular value decompositions return the same set of singular values and nothing changes as long as the interest is in modeling static principal eigenvectors. 

6 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

principal components forecasts with ridge regression and random projections. The remaining assumptions are the higher-level conditions from both Gonçalves et al. (2017) (e.g. iii) and Bai and Ng (2023) (iv and v). The latter are also utilized by Boot and Keijsers (2025), but they would be directly implied if **f** _t_ and _ei,s_ were independent for all _i, s, t_ . The equivalent of (iii) in Gonçalves et al. (2017) requires 16th moments, whereas we deem it very strong and bring it down due to A.1(iv). 

### _2.2.1. Homogeneous weak loadings_ 

ingWefurtherobtainmodificationsan expansionfromof<sup>ˆ</sup> **F** _t_ −both **F** _t_ **H** Bai<sup>′</sup> _Nt,r_ and<sup>byimplement-</sup> Ng (2023) and Gonçalves et al. (2017). We start with the case of homogeneous loadings and move in the next section to the case of heterogeneous loadings, i.e. when the loadings are allowed to be weaker to different degrees. We define the following scalar quantities: 





Note that only the terms that depend on **_λ_** _i_ are directly scaled by _N_<sup>−</sup><sup>_α_</sup> . Since (2.15) and (2.16) are functions of the idiosyncratics only, _N/N_<sup>_α_</sup> can be seen as a ‘penalty’ term on the overall rate, as we estimate potentially weaker loadings with principal components. Therefore, we obtain the following decomposition for a row _s_ : 



˜This is anˆ important term, appearing when expanding _u_ 2 _,t_ +1 − _u_ 2 _,t_ +1, that is, the difference between the infeasible and feasible estimated forecast errors. Specifically, let **_Φ_** _Nt,r_ = diag( **I** _k,_ **H** _Nt,r_ ) ∈ R<sup>(</sup><sup>_k_+</sup><sup>_r_)×(</sup><sup>_k_+</sup><sup>_r_)</sup> , where **H** _Nt,r_ is the rotation matrix defined in (2.14). Then, in line with Gonçalves et al. (2017) and Stauskas and Westerlund (2022), we obtain 



Because it is a scalar, we have that _III_ = (<sup>ˆ</sup> **f** _t_ − **H** _Nt,r_ **f** _t_ )<sup>′</sup> (der **H**<sup>−</sup> _Nt_<sup>1</sup> _,_ the _r_<sup>)′</sup><sup>**_β_**,</sup> null).<sup>and</sup><sup>_III_</sup> The<sup>istherefore</sup> component<sup>absent</sup> _I_ , instead,<sup>when</sup><sup>**_β_**</sup> reveals<sup>=</sup><sup>**0**</sup><sup>_r_(un-</sup> that the asymptotic equivalence is ensured when the factors are estimated consistently and the infeasible forecasting model is well-specified (∥<sup>˜</sup> **_δ_** _t_ − **_δ_** ∥ = _op_ (1)). Term _II_ additionally requires that the feasible OLS estimator of the 

parameters is asymptotically equivalent to the infeasible one. Because<sup>ˆ</sup> **_δ_** _t_ employs the factors which are only identified up to a rotation, the former is naturally rotated as well.<sup>8</sup> 

The expression (2.19) is the integral part of the feasible versions of (2.5)–(2.8). To demonstrate their asymptotic equivalence, it is useful to introduce the following quantities: 





where _qj_ ( _._ ) is a function, such thatˆ | _qj_ ( _A, B, C, D_ )| = _op_ (1) if _A_ , _B_ , and _C_ are negligible and _ωj_ = ˜ _ωj_ + _op_ (1). Therefore, the asymptotic equivalence holds for _j_ = 1 _, . . . ,_ 4 if (2.20)–(2.23) are negligible. The expansion of all the infeasible statistics can be found in the Online Supplement. 

**Example 3.** Let us examine the feasible versions of (2.7) and (2.8): 



Contrary to _j_ = 3, the factor estimation error accumulates over the choices of _l_ 2 under _j_ = 4. Clearly, in both cases for | _qj_ ( _A, C, D_ )| = _op_ (1), it is sufficient˜ to have | _A_ | = _op_ (1) and | _C_ | = _op_ (1). Additionally, if | _ωj_<sup>2−ˆ</sup><sup>_ω_</sup> _j_<sup>2|=</sup><sup>_op_(1),</sup> then _g_ ˆ _f ,j_ = _gf ,j_ + _op_ (1) for _j_ = 3 _,_ 4. 

The structure of (2.20)–(2.22) reveals how the behavior of the out-of-sample average of (2.19) dictates the overall asymptotic analysis. For this, we state more assumptions regarding the idiosyncratic components. 

**A.4 (Idiosyncratics)** 



> 8 Indeed, by the Frisch–Waugh–Lovell argument, the second componentthe projectionis ( **H**<sup>−</sup> _Nt_<sup>1</sup> _,_ matrix _r_<sup>)′˜</sup><sup>**_α_**</sup><sup>_t_=</sup> onto<sup>(</sup><sup>**H**′</sup> _Nt,_ the _r_<sup>**F**</sup> _t_<sup>′</sup><sup>**M**</sup> orthogonal<sup>**WF**</sup><sup>_t_</sup><sup>**H**</sup><sup>_Nt,r_)−</sup> complement<sup>1</sup><sup>**H**′</sup> _Nt,r_<sup>**F**</sup> _t_<sup>′</sup><sup>**MWy**</sup><sup>_t_</sup> of<sup>,where</sup> the observed<sup>**MW**is</sup> predictors. 

7 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 



<!-- Start of picture text -->
⎧( j  = 3) gf , 3 +  gf , 3 ( ˜ˆ ωω 33 − 1 )<br>⎛ k 0+ l 0 2 −1 k 0+ l 0 2 −1<br>+ ˆ ω 1  3 ln 0 2 ( nn  −⌊(1 − nττ 00⌋) ) ⎝ √ 2 n t ∑= k 0 ˜ u 2 ,t +1(˜ u 2 ,t +1 −ˆ u 2 ,t +1) − √ 1 n t ∑= k 0 (˜ u 2 ,t +1 −ˆ u 2 ,t +1) 2 ⎞⎠ ,<br>  <br>g ˆ f ,j = ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨( j  = 4) gf , 4 +  gf , 4 ( ˜ˆ ωω 44 − 1 ) q 3( A,C,D )<br>1 1 n n k 0+ l 2−1˜ ˜ ˆ 1 k 0+ l 2−1 ˜ ˆ<br>+ n (1 − τ 0) ˆ ω 4 l 2=⌊∑ nτ 0⌋ l 2 ⎛⎝ √ 2 n t ∑= k 0 u 2 ,t +1( u 2 ,t +1 − u 2 ,t +1) − ˆ ω 1  4 √ n t ∑= k 0 ( u 2 ,t +1 − u 2 ,t +1) 2 ⎞⎠ .<br>  <br>⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩ q 4( A,C,D )<br><!-- End of picture text -->

**Box I.** 



A.4 is similar to the conditions applied by Gonçalves et al. (2017), except for the lower moment requirement. This allows the idiosyncratics to be weakly dependent over time and cross-sectionally. Part (vii) is the same as in Bai and Ng (2023), but it is required to hold uniformly in _t_ . We formulate it in terms of _T_ , because _t_ = ⌊ _sT_ ⌋ for some _s_ ∈ (0 _,_ 1), due to the recursive setup. It is primarily used to simplify proofs when the loading weakness is heterogeneous, but it also helps to improve convergence rates. 

Lemma 1 below formalizes the asymptotic behavior of the out-of-sample average of (2.19) by providing the rate of the average square factor approximation error over the recursive samples, when the loadings are weaker. In addition, it provides the uniform rate of the in-sample factor approximation error. 

**Lemma 1.** _Under A.1–A.4, as_ ( _N, T_ ) →∞ _,_ 



### **Proof.** Online Supplement, Section 3.2. 

Lemma 1 can be seen as an extension of Theorem 4.1 in Gonçalves et al. (2017) to the case of weaker loadings and different alternative out-of-sample paths. If _α_ = 1 (strong loadings), we return to the usual rate of _Op_ (max{1 _/N,_ 1 _/T_ }), which coincides with the result 

in the latter study. Note that the result immediately <u>1</u> implies that we must have _N_<sup>_<u>Nα</u>_</sup> ~~√~~ _T_ → 0 and _α >_ 0 _._ 5 to consistently estimate the factor space in both in- and out-of-sample cases. In contrast, the theory in Bai and Ng (2023) requires a lower bound of _α_ different from 0 only for inference exercises, but not consistency. The difference arises because in part (i), we consider a recursive setup where the rotation matrix in (2.14) changes for every _t_ = _k_ 0 _, . . . , T_ − 1, and therefore this extra informativeness condition needs to be satisfied. Part (ii) of Lemma 1 deals with the average square in-sample factor estimation error, where we average over _s_ = 1 _, . . . , t_ ˆas<sup><u>1</u></sup> _t_ ˆ **F** _t_ − **F** _t_ **H** ′ _Nt,r_ 2 = <u>1</u> _t_ ∑ _ts_ =1 ˆ **f** ˆ _s_ − **H** _Nt,r_ **f** _s_ 2. We use **F** _t_ −1 when obtaining the feasible **_δ_** _t_ for each recursion. Interestingly, _α >_ 0 _._ 5 is sufficient but not necessary for part (ii) to hold, since we average for a given **H** _Nt,r_ . Hence, the approximation rate can be improved with higherlevel conditions in both homogeneous and heterogeneous cases, as we point out in Remark 2. However, part (i) is responsible for the general out-of-sample approximation and determines the behavior of _g_ ˆ _f ,j_ for _j_ = 1 _, . . . ,_ 4. 

The following result employs part (ii) of Lemma 1 to demonstrate the uniform equivalence of feasible and infeasible OLS estimators. 

**Lemma 2.** _Under Assumptions A.1–A.4, as_ ( _N, T_ ) →∞ _we have_ 



**Proof.** Online Supplement, Section 4.2. 

Similarly to Lemmas 1 and 2 can be seen as a generalization of Lemma 4.1 of Gonçalves et al. (2017) to weaker loadings. This follows from the direct application of our Lemma 1(ii) when establishing the uniform consistency of<sup>ˆ</sup> **_δ_** _t_ for (the rotated)<sup>˜</sup> **_δ_** _t_ . Hence, _α >_ 0 _._ 5 plays a role as well. The implication of the lemma is that the rate of consistency is _op_ ( _T_<sup>−1</sup><sup>_/_4</sup> ), unlike in the latter study, where it is _op_ ( _T_<sup>−1</sup><sup>_/_2</sup> ). The difference arises through two related channels. Firstly, the tests of Pitarakis (2023, 2025) have different local power properties. Indeed, we specify 

8 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

**_β_** = **_β_**<sup>0</sup> _T_<sup>−1</sup><sup>_/_4</sup> , while the tests of Clark and McCracken (2001) explored by Gonçalves et al. (2017) require **_β_** = **_β_**<sup>0</sup> _T_<sup>−1</sup><sup>_/_2</sup> . Secondly, we chose a different proving technique, since we only needed to demonstrate consistency, but the exact rate is less important, due to the different asymptotic properties of our tests. 

In order to move on to the main results, we introduce the last assumption. 





A.5(i) should be seen as a device to make convergence rates more transparent when the loadings are indeed weaker. Specifically, to prove that _B_ and _C_ in (2.21) and (2.22) are negligible, we need _N_<sup>_<u>Nα</u>_</sup> ~~√~~ <u>1</u> _T_<sup>=</sup><sup>_o_(1)asbefore,</sup> but at the same time _T_<sup>1</sup><sup>_/_4</sup> _N_<sup>_<u>Nα</u>_</sup> ~~√~~ <u>1</u> _T_ = _O_ (1). Thus, under A.4(i), _N_<sup>_<u>Nα</u>_</sup> ~~√~~ <u>1</u> _T_<sup>=</sup><sup>_Op_(</sup><sup>_T_−1</sup><sup>_/_4),whichistheratethatcanbe</sup> incorporated in the subsequent analysis. Requirements in the spirit of A.5(ii) are often met in the PCA literature, and it helps to ensure that the factor estimation error does not accumulate too fast with the expansion of _N_ and _T_ . Here, it is identical to the assumption needed for inference in Lemma 4 of Bai and Ng (2023). Under _α_ = 1 (strong loadings), this naturally coincides with the requirement of √ _TN_<sup>−1</sup> = _o_ (1) in Gonçalves and Perron (2014) or Gonçalves et al. (2017). Both here and in the latter study, this requirement targets sums over an MDS process {(<sup>ˆ</sup> **f** _t_ − **H** _Nt,r_ **f** _t_ ) _ut_ +1}<sup>_T_</sup> _t_ =<sup>−</sup> _k_<sup>1</sup> 0<sup>andmakessurethat</sup> they remain asymptotically negligible. Such terms appear by applying (2.19) to components _B_ and _C_ in (2.21) and (2.22), respectively. 

Lemma 3, below, is the central outcome that utilizes the interim results discussed above. 

**Lemma 3.** _Under Assumptions A.1–A.5, as_ ( _N, T_ ) →∞ _, we have that A–D are asymptotically negligible._ 

### **Proof.** Online Supplement, Section 4.2. 

To our knowledge, this is the first result that controls the factor estimation error in the out-of-sample context uniformly in loading strength and alternative outof-sample paths. Apart from the desired results on _A, B_ and _C_ , we can also see that the feasible variance estimator is asymptotically equivalent to the infeasible one, because 



under our assumptions. Note that _A_ - _D_ remain negligible under conditional heteroskedasticity. However, we leave the full analysis of HAC version of _D_ for future research. This provides the last missing piece to establish the equivalence result. 

**Theorem 1.** _Under Assumptions A.1–A.5, as_ ( _N, T_ ) →∞ _, we have_ 



**Proof.** The proof follows from the application of Lemma 3. 

The main message of Theorem 1 is not only that we are able to use the battery of new statistics (2.5)–(2.8) in the popular context of factor-augmented forecasts, but also that they are robust to weaker factor loadings, as long as _α >_ 0 _._ 5. This result is a companion to Theorem 4.2 in Gonçalves et al. (2017). While it does not necessarily nest their results, due to different statistics and their local power properties, we have the same approximation rates under strong loadings ( _α_ = 1). 

Before we generalize our results to the heterogeneously weak loadings, it is important to illustrate how Theorem 1 can be used to improve the statistics. The tests of equal forecast accuracy in (2.6) and (2.7) depend on the tuning parameters _λ_<sup>0</sup> 1<sup>and</sup><sup>_λ_0</sup> 2<sup>.Naturally,whilesuggestions</sup> on their values are provided in Algorithm 1, your choice still alters the power properties of the tests, as argued by Pitarakis (2025). To bypass this issue, power-enhanced versions of the statistics are presented, e.g. 



where<sup>˜</sup> _ζ_ ( _λ_<sup>0</sup> 1<sup>_, λ_0</sup> 2<sup>)=</sup> ˜ _ω_ <u>12</u> _λ_ <u>1</u><sup>0</sup> 2 ~~√~~ <u>1</u> _n_ ∑ _kt_ =0+ _k_ 0 _l_<sup>0</sup> 2<sup>−1</sup> (˜ _u_ 1 _,t_ +1 − ˜ _u_ 2 _,t_ +1)<sup>2</sup> in the spirit of Fan et al. (2015). Clearly, the poweradjustment term is infeasible and we must replace it with<sup>ˆ</sup> _ζ_ ( _λ_<sup>0</sup> 1<sup>_, λ_0</sup> 2<sup>).Proposition2belowdemonstratesthatthe</sup> power enhancement procedures remain valid. 

**Proposition 2.** _Under Assumptions A.1–A.5, as_ ( _N, T_ ) → ∞ _, we have_ 

_g_ ˆ _fadj ,_ 2<sup>=</sup><sup>_g_ˆ</sup> _f ,_ 2<sup>+ˆ</sup><sup>_ζ_(</sup><sup>_λ_0</sup> 1<sup>_, λ_0</sup> 2<sup>) =</sup><sup>_gf ,_2 +˜</sup><sup>_ζ_(</sup><sup>_λ_0</sup> 1<sup>_, λ_0</sup> 2<sup>) +</sup><sup>_op_(1)</sup><sup>_,_</sup> _and the same holds for g_ ˆ _fadj ,_ 3<sup>_andg_</sup> ˆ _fadj ,_ 4<sup>_,wheretheadjustment_</sup> _term is an appropriate average of_<sup>ˆ</sup> _ζ_ ( _λ_<sup>0</sup> 1<sup>_, λ_0</sup> 2<sup>)</sup><sup>_._</sup> 

### **Proof.** Online Supplement, Section 4.4. 

The adjustment term _g_ ˆ _fadj ,_ 4<sup>concernsournewstatistic</sup> _g_ ˆ _f ,_ 4 in (2.8). We relegate its asymptotic analysis together with a broader discussion on how the power adjustment terms are constructed to Section 4.4 of the Online Supplement. 

**Remark 1.** Assumption A.1 implies that the forecast errors are uncorrelated, and so the model is dynamically correctly specified. In practice, we may encounter measurement errors, for example, which force { _ut_ } to be correlated over time. Moreover, if we consider _h_ -stepahead forecasts, _ut_ + _h_ typically follows a moving average process of order _h_ − 1 (see Assumption R in Cheng & Hansen, 2015). To account for such possibilities for any _h_ ≥ 1, we can introduce three high-level conditions instead of Assumption A.1(i) that go beyond moving average processes: 



9 

**_<mark>ARTICLE IN PRESS</mark>_** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 



Conditions (i) and (ii) often appear in the literature when the forecast errors are dependent over time (see e.g. Pitarakis, 2025). For instance, they can be implied if { **z** _sus_ + _h_ }<sup>_t_</sup> _s_ =<sup>−</sup> 1<sup>_h_isamixingofarelevantsize.Part(</sup><sup>_iii_)</sup> mainly concerns the term analyzed in Lemma 2. Note that part (iii) resembles an object that converges weakly to a stochastic integral (see Hansen, 1992). Similar terms are uncovered when sums over an MDS process {(<sup>ˆ</sup> **_δ_** _t_ − ( **_Φ_**<sup>−</sup> _Nt_<sup>1</sup> _,r_<sup>)′˜</sup><sup>**_δ_**</sup><sup>_t_)′</sup><sup>**z**</sup><sup>_tut_+1}</sup><sup>_T_</sup> _t_ =<sup>−</sup> _k_<sup>1</sup> 0<sup>areanalyzedinLemma3inaone-</sup> step-ahead context. For our purposes, it is sufficient for them to remain bounded to accommodate some weak dependence in { _ut_ + _h_ }. 

Parts (i)–(iii) above are enough for _A_ – _C_ of Lemma 3. However, the MDS assumption legitimizes the use of (2.25) as the estimator of _φ_<sup>2</sup> that enters _D_ . The full analysis of HAC-type estimators is beyond the scope of this study. However, under serial dependence, and because ˆ _u_ jecture<sup>2</sup> 2 _,t_ + _h_<sup>=</sup> that<sup>˜</sup><sup>_u_2</sup> 2 _,t_ the+ _h_<sup>+</sup> HAC<sup>_op_(1)</sup> estimator<sup>underour</sup> of<sup>conditions,</sup> _φ_<sup>2</sup> as proposed<sup>wecon-</sup> by both Pitarakis (2023) and Pitarakis (2025) will remain consistent (see also the discussion by Fosten (2016) or Su et al. (2025), where HAC is applied after the first-step factor estimation). 

_αr_ (in the interim, the absence of a subscript _α_ ( _αr_ ) means that there is no scaling in terms of _N_ ). Next, to accommodate heterogeneity in loading weakness, we redefine 





To handle heterogeneous weak loadings, we require adaptations of the former assumptions A.3 and A.5. More specifically, 

- **A.3* (Heterogeneously weak loadings)** 

### _2.2.2. Heterogeneous weak loadings_ 

In the previous section, we imposed that the loadings are weaker to the same degree, or homogeneously. Alternatively, we can allow for heterogeneously weak loadings by employing the normalizing matrix **B** _N_ = diag( _N_<sup>_α_1</sup><sup>_/_2</sup> _, . . . , N_<sup>_αr/_2</sup> ), where 1 ≥ _α_ 1 _> α_ 2 _>_ · · · _> αr >_ 0, and where the weakest loading cannot still be absolutely uninformative. This means that as _N_ →∞, some loadings are too small or too sparse for the corresponding eigenvalues to diverge at rate _N_ , while others are relatively stronger or right-out strong such that the corresponding eigenvalues diverge at a slightly sub-linear rate or a linear rate in _N_ . Clearly, the heterogeneous case nests the homogeneous one when _α_ 1 = · · · = _αr_ . Note that ∥ **B** _N_ ∥≤ _MN_<sup>_α_1</sup><sup>_/_2</sup> and ∥ **B**<sup>−</sup> _N_<sup>1∥≤</sup><sup>_mN_−</sup><sup>_αr/_2forsome</sup> positive constants _M_ and _m_ , which means that the order of (the inverse of) this normalization matrix is dominated by the (weakest) strongest factor loading. Again, recall thatrelationship.<sup>ˆ</sup> **F** _t_ **D**<sup>2</sup> _Nt,r_<sup>=</sup> Then, _Nt_ <u>1</u><sup>**X**</sup> by<sup>_t_</sup><sup>**X**</sup> _t_<sup>′ˆ</sup><sup>**F**</sup> using<sup>_t_bythe</sup> the<sup>eigenvalue–eigenvector</sup> fact that both **B** _N_ and ˆ **DF** _t_<sup>2</sup> _Nt_ **B** _,Nr_ ( **B**<sup>are−</sup> _N_<sup>2</sup><sup>**D**diagonal,2</sup> _Nt,r_<sup>) =</sup> _Nt_ <u>1</u><sup>we</sup><sup>**X**</sup><sup>_t_</sup><sup>**X**obtain</sup> _t_<sup>′ˆ</sup><sup>**F**</sup><sup>_t_</sup><sup>**B**−</sup> _N_<sup>1ˆ</sup><sup>**F**.</sup><sup>_t_</sup><sup>**D**2</sup> _Nt,r_<sup>**B**−</sup> _N_<sup>1</sup> =<sup>ˆ</sup> **F** _t_ **B**<sup>−</sup> _N_<sup>1</sup><sup>**D**2</sup> _Nt,r_<sup>=</sup> 

As for the above, we are after an expansion of<sup>ˆ</sup> **F** _t_ − **F** _t_ **H**<sup>′</sup> _Nt,r_<sup>.9Hence,weusethesamedefinitionsofthescalar</sup> quantities in (2.15)–(2.17). However, we replace _α_ with 

9 To be precise, we are after the expansion of (ˆ **F** _t_ **B** _N_ − **F** _t_ **B** _N_ **H** ~~′~~ _Nt,r_<sup>)</sup><sup>**B**−</sup> _N_<sup>1,</sup> for **H** _Nt,r_ := ( _N_ **B**<sup>−</sup> _N_<sup>2</sup><sup>**D**2</sup> _Nt,r_<sup>)−1</sup><sup>**B**−</sup> _N_<sup>1</sup><sup>_t_−1ˆ</sup><sup>**F**</sup> _t_<sup>′</sup><sup>**F**</sup><sup>_t_</sup><sup>**_Λ_**′</sup><sup>**_Λ_B**−</sup> _N_<sup>1.However,asweex-</sup> plain in the Online Supplement, the component **B**<sup>−</sup> _N_<sup>1</sup><sup>_t_−1ˆ</sup><sup>**F**</sup> _t_<sup>′</sup><sup>**F**</sup><sup>_t_</sup><sup>**_Λ_**′</sup><sup>**_Λ_B**−</sup> _N_<sup>1is</sup> bounded in probability for _t_ = _T_ , as argued by Bai and Ng (2023), and we also show that it is uniformly bounded in Lemma 1 of the mathematical Online Supplement. Furthermore, using the fact that the 



**A.5** * ( _N, T_ **expansion rates for heterogeneously weak loadings** ) 

_<u>N</u>_ <u>1</u> (i) _N_<sup>_<u>αr</u>_</sup> _T_<sup>1</sup><sup>_/_4</sup> → _c >_ 0, as ( _N, T_ ) → ∞, (ii) √ _TN_<sup>−</sup><sup>_αr_</sup> → 0, for _αr_ ∈ (0 _._ 5 _,_ 1). 

Finally, Lemma 4, whose proofs are in the Online Supplement, Sections 3.2.2 & 4.2, links the results of Lemmas 1, 2 and 3 to the heterogeneous loadings context. With this, the results in Theorem 1 follow directly. 

**Lemma 4.** _Under A.1, A.2, A.3*, A.4, A.5*, and with heterogeneous loadings (_ 1 ≥ _α_ 1 ≥· · · ≥ _αr >_ 1 _/_ 2 _), as_ ( _N, T_ ) →∞ _, the results of Lemmas_ 1 _,_ 2 _,_ 3 _, and Proposition_ 2 _continue to hold with αr in place of α._ 

product **H** _Nt,r_ . of **B** _N_ and **D**<sup>2</sup> _Nt,r_<sup>commutes,wecanshowhow</sup><sup>**B**−</sup> _N_<sup>1</sup> **H** _Nt,r_ **B** _N_ = 

10 

**_<mark>ARTICLE IN PRESS</mark>_** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

**Proof.** Online Supplement, Sections 3.2 and 4.2 as counterparts to the homogeneous case. 

**Remark 2.** It is possible to improve the rate of convergence of the in-sample estimated factors in Lemma 1 (ii.). As Lemma 8 in the Online Supplement reveals, we have for the homogeneous and heterogeneous cases, respectively, 



which does not immediately restrict _α_ ( _αr_ ). Consequently, the rates in Lemma 2 are improved as well. This can be achieved by following (Bai & Ng, 2023) and employing a high-level assumption in A.4(vii). In this case, we do not need to analyze the sums of (2.18) and employ summability conditions on the idiosyncratics (the usual approach, as in e.g. Bai & Ng, 2002). This technique is unavoidable in Lemma 1(i) due to the out-of-sample design. For (ii), instead, we can focus on the norm of the whole time stack, and this gives the same rates as in Proposition 1 of Bai and Ng (2023). Nevertheless, the out-of-sample rates – part (i) of Lemma 1 – dictate the behavior of _A_ – _D_ of Lemma 3. Therefore, _α >_ 0 _._ 5 cannot be dispensed with. 

Importantly, this improvement could not be achieved if the assumptions of Uematsu and Yamagata (2022) were applied to the usual principal components. This occurs due to their unspecified restrictions between **F** _t_ and **H** _Nt,r_ that strongly moderate the relationship between _α_ 1 and _αr_ (see also footnote 2 in Bai & Ng, 2023). 

### **3. Monte Carlo summary** 

We design a DGP similar to DGP2 in Pitarakis (2025), but where the factors are specified in the same way as DGP2 of Bai and Ng (2023) with strong/weak homogeneous/heterogeneous loadings. Throughout, we set the number of factors _r_ = 3. 





where **G** _i_ ∼ _N_ (0 _,_ **I** 3), **D**<sup>2</sup> = diag(3 2 1); **B** _N_ = diag ( _N_<sup>_α_1</sup><sup>_/_2</sup> _N_<sup>_α_2</sup><sup>_/_2</sup> _N_<sup>_α_3</sup><sup>_/_2</sup> ), ( _α_ 1 _, α_ 2 _, α_ 3) = (1 _,_ 1 _,_ 1) for strong homogeneous loadings, (0 _._ 51 _,_ 0 _._ 51 _,_ 0 _._ 51) for weak homogeneous loadings, and (0 _._ 51 _,_ 0 _._ 7 _,_ 1) for mixed strong/weak 

heterogeneous loadings.<sup>10</sup> The cross-sectional and time dimensions are ( _N, T_ ) = (800 _,_ 500). For the practical implementations, following Pitarakis (2025), we set _c_ = 1 _._ 25, _θ_ 1 = 0 _._ 5, _ρi_ = 0 _._ 3+ _N_ (0 _,_ 1) _i_ ×0 _._ 5, **_β_** = (0 _,_ 0 _,_ 0)<sup>′</sup> , and _π_ = 24 for size; and **_β_** = ( _j, j, j_ )<sup>′</sup> for _j_ ∈ {0 _._ 1 _,_ 0 _._ 2 _,_ 0 _._ 3 _,_ 0 _._ 35 _,_ 0 _._ 4 _,_ 0 _._ 45 _,_ 0 _._ 5 _,_ 0 _._ 55 _,_ 0 _._ 6} for power. Before we go to the results, let us mention how we performed the same simulations using the Bai and Ng (2002) criterion, _ICp_ 1 (see their Eq. 9), to actively select the number of factors. We select this number once during the in-sample period to reflect the assumption that _r_ is fixed over time. Since there is no recursion in the selection of the number of factors, this choice is justified by the results in Bai and Ng (2023), who find that in order to estimate factors with weakly convergent loadings ( _α >_ 0), the criteria in Bai and Ng (2002) remain valid. This turned out to be identical to the results presented here, as _ICp_ 1 always correctly estimates the number of factors.<sup>11</sup> 

### _3.1. Baseline results_ 

We here report a summary of the Monte Carlo in the form of power curves for the different test statistics considered. The setting is the baseline, meaning that _ut_ +1 is uncorrelated over time and _ei,t_ is uncorrelated crosssectionally. In Figs. 1–4, we find that both the encompassing and forecast accuracy tests to display satisfactory sizes and powers when factors are included in the alternative forecasting model. In terms of the choice of the parameters _µ_ 0 _, τ_ 0 _, λ_<sup>0</sup> 1<sup>_, λ_0</sup> 2<sup>,weherereportthebest-</sup> performing size-wise (i.e. the closest to nominal level 5%; see Online Supplement, Section 5 for the extended results). As expected, weaker loadings have a dampening effect on power, especially, of course, when the signal ( **_β_** value) is low. This effect is more pronounced when looking at the forecast accuracy tests _g_ ˆ _f ,_ 2 _, g_ ˆ _fadj ,_ 2<sup>_, g_ˆ</sup> _f ,_ 3<sup>_, g_</sup> ˆ _fadj ,_ 3<sup>,</sup> _g_ ˆ _f ,_ 4, and _g_ ˆ _fadj ,_ 4<sup>,whicharealreadyaffected–power-wise</sup> – by the data loss due to the sample overlapping discussed above. The power adjustment for _g_ ˆ _f ,_ 2 _, g_ ˆ _f ,_ 3 _, g_ ˆ _f ,_ 4 is paramount, because the unadjusted versions can lead to severely undersized tests, as seen in the tables in the Online Supplement, Section 5. The _g_ ˆ _fadj ,_ 4<sup>,whichaveragesover</sup> the second coordinate to let the MSE of the unrestricted model accumulate, has entirely analogous behavior as _g_ ˆ _fadj ,_ 3 with some slightly higher power for lower **_β_** . Overall, we show how all the tests have good finite sample performances when factors are included in the alternative model specification, and loadings can be either strong or weak, homogeneous or heterogeneous. We refer the reader to the Online Supplement, Section 5 for all the results, including the heterogeneous ones. 

10 Note that **_λ_** _i_ is simulated differently from in Bai and Ng (2023). The reason is that the rate of ∥ **B**<sup>−</sup> _N_<sup>1</sup><sup>**_Λ_**′</sup><sup>**_Λ_B**−</sup> _N_<sup>1−</sup><sup>**_ΣΛ_**∥playsanimportant</sup> role in our asymptotic analysis, whereas it did not matter for Bai and Ng (2023). This simulation method mimics A.3(i), because we can show that under such a design, **B**<sup>−</sup> _N_<sup>1</sup><sup>**_Λ_**′</sup><sup>**_Λ_B**−</sup> _N_<sup>1</sup> = **D**<sup>2</sup> + _Op_ ( _N_<sup>−</sup><sup>_αr /_2</sup> ) as desired. 11 We shall mention, however, that others of the Bai and Ng (2002) criteria did not perform as well as _ICp_ 1 in selecting the factors; we report _ICp_ 1, as it is the most remarkable. 

11 

**_<mark>ARTICLE IN PRESS</mark>_** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

**Fig. 1.** _g_ ˆ _f ,_ 1, encompassing. 



<!-- Start of picture text -->
Fig. 2. g ˆ fadj , 2 , forecast accuracy.<br><!-- End of picture text -->

**Fig. 3.** _g_ ˆ _fadj ,_ 3<sup>,forecastaccuracy.</sup> 

12 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 



<!-- Start of picture text -->
Fig. 4. g ˆ fadj , 4 , forecast accuracy.<br><!-- End of picture text -->

**Fig. 5.** _g_ ˆ _f ,_ 1, encompassing. 

### _3.2. Cross-section dependence_ 

In Figs. 5–8, we introduce weak cross-section dependence in _ei,t_ similarly to Stauskas and Westerlund (2022). We see that the results are virtually the same as in the baseline scenario. This signals robustness to both temporal and, for example, spatial dependence structures in idiosyncratics. 

### _3.3. Conditional heteroskedasticity_ 

In Figs. 9–12, we introduce, on top of the cross-section dependence of the idiosyncratics, conditional heteroskedasticity in the forecast errors _ut_ +1, in the form of a GARCH(1 _,_ 1), as specified above. Throughout the simulations, we still use (2.25) to estimate _φ_<sup>2</sup> . The main effect for all tests is a mild inflation of the size,<sup>12</sup> which is however milder for _g_ ˆ _fadj ,_ 4<sup>comparedto</sup><sup>_g_ˆ</sup> _f ,_ 1<sup>,</sup><sup>_g_</sup> ˆ _fadj ,_ 2<sup>,and</sup><sup>_g_</sup> ˆ _fadj ,_ 3<sup>.Thepower</sup> is instead higher for lower values of the coefficient **_β_** 

> 12 As one would expect, if the persistence of the past conditional variance of _ut_ is high(er), i.e. the _η_ of the GARCH(1 _,_ 1) is large(r), the size would suffer more. In such cases HAC-type corrections of the variance are recommended. 

(e.g. **_β_** = [0 _._ 10 _, . . . ,_ 0 _._ 30]) if compared to the previous results, though this might just be a byproduct of the size increase or of the GARCH time-varying variance structure, which potentially makes certain periods in the sample more informative. At the same time, even though (2.25) estimates unconditional variance, it can be sensitive to conditional heteroskedasticity, especially as it utilizes 4th moments. While a theoretical justification for HAC-type corrections in our testing framework is left for future research, we experimented with the practical implementations proposed by Pitarakis (2023) for _g_ ˆ _f ,_ 1, specifically using Newey–West and Andrews standard errors. These methods demonstrate good empirical performance in our simulations and are thus recommended for practitioners, particularly in settings where conditional heteroskedasticity – such as GARCH-type volatility – is likely present in the forecast errors. The Online Supplement contains heterogeneous weakness results as well. 

**Remark 3.** The large combinations of ( _N, T_ ) in our experiments are selected to demonstrate the asymptotic properties of the tests and the effect of weaker loadings. In Section 5.2 of the Online Supplement, we provide a full set of simulations for smaller samples (e.g. _N_ = 100 _,_ 

13 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 



<!-- Start of picture text -->
Fig. 6. g ˆ fadj , 2 , forecast accuracy.<br><!-- End of picture text -->



<!-- Start of picture text -->
Fig. 7. g ˆ fadj , 3 , forecast accuracy.<br><!-- End of picture text -->

**Fig. 8.** _g_ ˆ _fadj ,_ 4<sup>,forecastaccuracy.</sup> 

_T_ = 200 _,_ 350) to reflect more practical scenarios. While natural, the loss in power is not substantial. Nevertheless, small sample performance can be improved by bootstrap, because Assumptions 1–5 in Gonçalves and Perron (2014) are analogous to ours. Also, their requirement ~~√~~ _TN_<sup>−1</sup> → 

_c_ for 0 ≤ _c <_ ∞ is analogous to, for _c_ = 0, our current Assumption A.5, where √ _TN_<sup>−</sup><sup>_α_</sup> → 0 for _α_ ∈ (0 _._ 5 _,_ 1). As such, their best-case (i.e. without any asymptotic bias term) bootstrap can be used in our context too. The bootstrap DGP in this case can be constructed 

14 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

**Fig. 9.** _g_ ˆ _f ,_ 1, encompassing. 



<!-- Start of picture text -->
Fig. 10. g ˆ fadj , 2 , forecast accuracy.<br><!-- End of picture text -->



<!-- Start of picture text -->
Fig. 11. g ˆ fadj , 3 , forecast accuracy.<br><!-- End of picture text -->

using the wild bootstrap scheme described in Section 4 ˆ **z** _t_ = ( **w**<sup>′</sup> _t_<sup>_,_ˆ</sup><sup>**f**′</sup> _t_<sup>)′,whileˆ</sup><sup>**f**</sup><sup>_t_,</sup><sup>**_Λ_**ˆandˆ</sup><sup>**_δ_**=(ˆ</sup><sup>**_θ_**</sup> ′ _,_ ˆ **_β_** ′)′ are the initial of their study. Specifically, before Algorithm 1 starts, we estimates obtained using the whole time series sample generate **X**<sup>∗</sup> _t_<sup>=</sup><sup>**_Λ_**ˆˆ</sup><sup>**f**</sup><sup>_t_+</sup><sup>**e**∗</sup> _t_<sup>and</sup><sup>_y_∗</sup> _t_ +1<sup>= ˆ</sup><sup>**_δ_**</sup> ′ˆ **z** _t_ + _u_ ∗ _t_ +1<sup>,where</sup> _t_ = 1 _, . . . , T_ . Next, **e**<sup>∗</sup> _t_ = ( _ν_ 1 _,t_ ˆ _e_ 1 _,t , . . . , νN,t_ ˆ _eN,t_ )<sup>′</sup> and 

15 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

**Fig. 12.** _g_ ˆ _fadj ,_ 4<sup>,forecastaccuracy.</sup> 

_u_<sup>∗</sup> _t_ +1<sup>=</sup><sup>_ηt_+1ˆ</sup><sup>_ut_+1,where</sup><sup>_νi,t_and</sup><sup>_ηt_areIID(0</sup><sup>_,_1)mutually</sup> independent variables that scale the residuals from the initial regression. Eventually, Algorithm 1 is implemented for _b_ = 1 _, . . . , B_ bootstrap samples generated according to the wild scheme. 

### **4. Empirical applications** 

### _4.1. Inflation forecasting_ 

We partially replicate the inflation forecast exercise conducted by Pitarakis (2023). Our focus here is to explore whether _global_ inflation can enhance the accuracy of country-level inflation forecasts. This debate is not new; previous studies have provided evidence that global inflation trends can significantly improve domestic inflation forecasts (see among others Ciccarelli & Mojon, 2010; Monacelli & Sala, 2009). However, other research suggests that the relevance of global inflation in forecasting domestic rates may stem solely from its ability to capture slow-moving trends in inflation (Mikolajun & Lodge, 2016), or that a global inflation factor improves forecasting accuracy primarily at longer horizons (Gillitzer & McCarthy, 2019). The question is, also, how to measure global inflation. One approach is to calculate a grand average of country-level inflation rates, represented as _π_ ¯ _t_ = _N_<sup>−1 ∑</sup><sup>_N_</sup> _i_ =1<sup>_πi,t_.Anothermethodinvolvestreatingglobal</sup> inflation as a few latent factors that can be estimated using principal components from the pool of countrylevel inflation rates. The former approach is employed by Pitarakis (2023) to illustrate his encompassing test, while we will utilize the latter method to demonstrate how JYP’s encompassing tests work in an empirically relevant context where principal component factors are considered. There are several reasons why a PCA of global inflation serves as a more accurate measure than a simple grand average of inflation rates. A straightforward sample mean does not consider differences in economic size, inflation volatility, or other factors that may make some countries’ inflation rates more indicative of global trends than others. In contrast, principal components can uncover patterns of co-movement in inflation rates that 

might not be evident from the raw data. Additionally, it is more robust to potential outliers and can adapt to timevarying relationships among countries’ inflation rates. However, one could argue that if we assume the existence of only one factor, then all the information contained in that factor is effectively the same as a cross-sectional average of the countries’ inflation rates. This would be true, upon essentially three assumptions: (i) the existence of an exact factor model underlying the data, i.e. _πi,t_ = **_λ_**<sup>′</sup> _i_<sup>**_f_**</sup> _t_<sup>+</sup><sup>_ei,t_with</sup><sup>_Cov_(</sup><sup>_ei,t, ej,s_)=0,</sup><sup>_t, s_∈Z,</sup><sup>_i, j_=1</sup><sup>_, . . . , N_,</sup> _i_ = _j_ ; (ii) a large cross-sectional dimension _N_ (in principle, _N_ →∞); (iii) all or most of the loadings being nonzero (i.e. the pervasiveness of factors). Assume that the loadings are fixed. If all these are satisfied, it is clear how _Var_ ( ¯ _πt_ ) = _N_<sup>−2</sup> (<sup>∑</sup> _i_<sup>_λi_)2</sup><sup>_Var_(</sup><sup>_ft_) +</sup><sup>_N_−2</sup><sup>_Var_(∑</sup> _i_<sup>_ei,t_)→¯</sup><sup>_λ_2=</sup> _Var_ ( ¯ _χt_ ), as _N_ →∞, meaning how the aggregation of the observed data recovers the same information contained in the factor. Now, (i) is clearly too strong (see also our A.4(v)), (ii) is what is referred to as the ‘blessing of dimensionality’ but in practice it clearly depends on the available data, and (iii) is precisely what is challenged by the weaker loadings treated in Section 2. Hence, there are good reasons to re-run this exercise using factors and employing JYP’s tests to check whether global inflation computed by means of principal component factors improves the country-level inflation forecast. We employ the same dataset provided in Pitarakis (2023),<sup>13</sup> based on the World Bank’s global inflation database and covering the period from 1970–2023 for 23 countries at quarterly frequency. We choose the tuning parameters in line with the simulations to balance the power and size.<sup>14</sup> 

The base-line model is an _AR_ (1), while the alternative model is a factor-augmented _AR_ (1), where factors are recursively estimated and their number is determined via the Bai and Ng (2002) information criterion ( _ICp_ 1, max number = 10).<sup>15</sup> In Table 4.1, we find patterns of significance across the four test statistics, though rarely 

> 13 Freely available on JYP’s GitHub page: https://github.com/ jpitarakis/Multi-Step_Encompassing. 

> 14 For the exact treatment and transformations of the raw data, see Pitarakis (2023), Section 7. 

16 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

**Table 4.1** 

_<u>p</u>_ -values: One <u>quarter</u> ahead. 

|Country|_p_-value _g_ˆ_f ,_1|_p_-value _g_<br>_adj_<br>ˆ_f ,_2|_p_-value _g_<br>_adj_<br>ˆ_f ,_3|_p_-value _g_<br>_adj_<br>ˆ_f ,_4|
|---|---|---|---|---|
|United States of America (USA)|**0.007**|0.469|**0.008**|0.983|
|United Kingdom (GBR)|0.408|0.767|0.742|**0.003**|
|Japan (JPN)|0.284|0.388|0.094|**0.007**|
|France (FRA)|**0.003**|**0.023**|**0.010**|0.877|
|Germany (DEU)|0.863|0.186|0.539|0.540|
|Spain (ESP)|**0.000**|**0.000**|**0.000**|0.936|
|Italy (ITA)|0.859|0.306|0.845|0.392|
|Netherlands (NLD)|**0.001**|**0.000**|**0.002**|0.192|
|Luxembourg (LUX)|**0.000**|0.194|**0.044**|0.372|
|Canada (CAN)|0.070|0.711|0.142|0.736|
|Ireland (IRL)|0.196|0.574|0.067|0.110|
|Finland (FIN)|0.898|0.972|0.956|0.121|
|New Zealand (NZL)|0.998|0.971|0.969|0.336|
|Greece (GRC)|**0.004**|0.359|0.525|**0.013**|
|Portugal (PRT)|0.241|0.355|0.329|**0.000**|
|Norway (NOR)|0.257|0.905|0.866|0.168|
|South Korea (KOR)|0.459|0.714|0.569|**0.004**|
|Denmark (DNK)|0.414|0.473|0.527|**0.000**|
|Sweden (SWE)|0.496|0.855|0.787|**0.000**|
|Australia (AUS)|0.635|0.793|0.869|**0.022**|
|Austria (AUT)|**0.002**|**0.003**|**0.009**|**0.000**|
|Belgium (BEL)|0.233|0.173|0.485|0.348|
|Switzerland (CHE)|**0.000**|0.138|**0.000**|0.312|



Notes: _AR_ (1) vs. factor-augmented _AR_ (1); number of factors selected with Bai and Ng (2002) _ICp_ 1, _µ_ 0 = 0 _._ 40, and _τ_ 0 = 0 _._ 8 for _g_ ˆ _fadj ,_ 2<sup>:</sup><sup>_λ_0</sup> 1<sup>=1</sup><sup>_, λ_0</sup> 2<sup>=0</sup><sup>_._65;for</sup><sup>_g_</sup> ˆ _fadj ,_ 3<sup>:</sup><sup>_λ_0</sup> 2<sup>=0</sup><sup>_._6;for</sup><sup>_g_</sup> ˆ _fadj ,_ 4<sup>:</sup><sup>_λ_0</sup> 1<sup>=0</sup><sup>_._6.</sup> 

all of them at once (only AUT). _g_ ˆ _fadj ,_ 4<sup>findssignificantbet-</sup> ter forecast accuracy one quarter ahead when using a PCA of global inflation in nine of the 23 countries. It is followed by the encompassing test _g_ ˆ _f ,_ 1 with eight countries (nine with CAN if considering a 10% nominal level), _g_ ˆ _fadj ,_ 3<sup>withsevenand</sup><sup>_g_</sup> ˆ _fadj ,_ 2<sup>withfour.Noticeably,forsome</sup> large economies such as the USA, FRA, and ESP, at least two test statistics of the four are found to be significant (JPN too, if considering a 10% nominal level). Some other large/medium-to-large economies like GBR, DEU, and ITA have only one or no significance at all. Overall, this paints a mixed picture with regard to the use of global inflation to better forecast country-level inflation, which clearly seems to be a country-specific issue. These tests can therefore be used to gain a sense as to whether a PCA of global inflation might help beyond the simple AR specification. In the Online Supplement, Section 6, we repeat the exercise without factors but using a grand average of country-level inflations (which excludes the country of reference each time) as global inflation. What comes out is an overly suspicious abundant significance across most countries and all tests. Outliers and multicollinearity are likely to affect these results, as evident from the boxplots and pairwise correlation heatmap in 

> 15 It is well known how the Bai and Ng (2002) criteria depend quite substantially on the maximum number of factors as selected by the practitioner, as well as by the relative magnitude of _N, T_ (see e.g. Forni et al., 2009). In this case, we find on average that all criteria, including _ICp_ 1 but excluding _AIC_ 3, return the maximum as the estimated number of factors. We experimented using _AIC_ 3 and the ABC criterion of Alessi et al. (2010) too, which both on average estimated 4/5 common factors, but we found a completely similar picture in terms of significance, with only slightly higher _p_ -values. 

Fig. 13 and Fig. 14, respectively. It is therefore safe to say that the analysis, including the PCA of global inflation, is much more trustworthy. 

**Remark 4.** We suggest that the potential macroeconomics practitioners interpret the outcomes of the four tests as some sort of battery of checks to be used jointly in understanding whether the factor augmentation is worth it to improve the quality of the forecast. As outlined above, acknowledging that each test has its own nuance, _g_ ˆ _f ,_ 1 should be given more weight in the decision. This is because, as explained above, due the overlapping evaluation over the effective sample size for the case of _g_ ˆ _fadj ,_ 2<sup>,</sup> _g_ ˆ _fadj ,_ 3<sup>,and</sup><sup>_g_</sup> ˆ _fadj ,_ 4<sup>,somedataarelostintheMSEcomparison,</sup> which does not occur for _g_ ˆ _f ,_ 1. As such, a joint significance of _g_ ˆ _f ,_ 1 and at least one of _g_ ˆ _fadj ,_ 2<sup>,</sup><sup>_g_</sup> ˆ _fadj ,_ 3<sup>,and</sup><sup>_g_</sup> ˆ _fadj ,_ 4<sup>should</sup> possibly be taken as a solid indication that considering a factor-augmented specification can increase the forecast accuracy (see Table 4.1). 

### _4.2. FRED-MD forecasting_ 

We continue the empirical exercise by considering more macroeconomic series, this time from an even larger pool of series. Table 4.2 collects the _p_ -values for the tests of encompassing and forecast accuracy described in Section 2, using the same tunings as in the previous application in Section 4.1, for 14 important macroeconomic series taken from the FRED-MD dataset McCracken and Ng (2016) (July 2024 vintage, starting in January 1960). The FRED-MD dataset includes a wide range of U.S. macroeconomic series, such as output (e.g. industrial 

17 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 



**Fig. 13.** Inflation boxplot. 



**Fig. 14.** Correlation heatmap. 

production), income, labor market indicators (e.g. unemployment rate, payrolls), consumer and producer prices, money supply, interest rates, exchange rates, and financial variables like stock indices and spreads. These series capture economic activity, inflation dynamics, monetary policy, and financial market conditions. All series are cleaned and stationary transformed, as prescribed by the Matlab routines provided with FRED-MD. After the necessary cleaning of NAs and outliers, the final dataset contains 117 series for 772 data points. Again, we choose the tuning parameters in line with the simulations to balance the power and size (see our extensive simulations in the Online Supplement). 

We forecast these 14 macroeconomic series one month ahead using the principal component factors in the alternative forecasting specification (i.e. _AR_ (1) vs. factoraugmented _AR_ (1), where factors are estimated via Bai 

and Ng (2002) _ICp_ 1 with max number= 15).<sup>1617</sup> With an average of seven estimated common factors, the results are overwhelmingly significant across the four tests. Apart from ‘Real personal consumption expenditures’ (DPCERA3M086SBEA), all the series have at least one significant (at a nominal level of 5%) test statistic. This shows how even in a high(er) dimensional dataset such as the FRED-MD, these test statistics are very useful for assessing 

16 We choose to follow a common convention in the factor modeling literature by setting a relatively high maximum number of factors, from which the optimal number is selected using IC. The goal of this is to ensure that the true number of factors is not underestimated due to an arbitrarily restrictive upper bound. 

17 We collect the full names of the 14 FRED-MD macroeconomic time series in the Online Supplement (Section 6, Table 6.2). 

18 

**<mark>ARTICLE IN PRESS</mark>** 

_L. Margaritella and O. Stauskas_ 

_International Journal of Forecasting xxx (xxxx) xxx_ 

**Table 4.2** 

FRED-MD forecast accuracy & encompassing. 

|Series|_p_-value _g_ˆ_f ,_1|_p_-value _g_<br>_adj_<br>ˆ_f ,_2|_p_-value _g_<br>_adj_<br>ˆ_f ,_3|_p_-value _g_<br>_adj_<br>ˆ_f ,_4|
|---|---|---|---|---|
|UNRATE|**0.000**|**0.000**|**0.000**|0.628|
|CPIAUCSL|**0.004**|**0.029**|**0.000**|1.000|
|DPCERA3M086SBEA|0.168|0.112|0.510|0.219|
|S&P 500|**0.030**|**0.021**|0.118|0.898|
|PAYEMS|**0.000**|**0.000**|**0.014**|0.566|
|INDPRO|**0.000**|**0.000**|**0.000**|0.919|
|TB3SMFFM|0.986|0.885|0.885|**0.000**|
|HOUST|**0.002**|**0.000**|**0.000**|0.999|
|M1SL|**0.000**|**0.000**|**0.000**|0.999|
|M2SL|**0.000**|**0.003**|**0.018**|0.796|
|OILPRICEx|**0.000**|**0.000**|**0.003**|0.893|
|GS10|0.999|0.963|0.985|**0.000**|
|RPI|0.066|**0.012**|**0.034**|0.836|
|BUSLOANS|0.117|**0.037**|0.109|0.881|



Notes: One month ahead, _AR_ (1) vs. factor-augmented _AR_ (1); number of factors selected with Bai and Ng (2002) _ICp_ 1, _µ_ 0 = 0 _._ 40, and _τ_ 0 = 0 _._ 8, for _g_ ˆ _fadj ,_ 2<sup>:</sup><sup>_λ_0</sup> 1<sup>=1</sup><sup>_, λ_0</sup> 2<sup>=0</sup><sup>_._65;for</sup><sup>_g_</sup> ˆ _fadj ,_ 3<sup>:</sup><sup>_λ_0</sup> 2<sup>=0</sup><sup>_._6;for</sup><sup>_g_</sup> ˆ _fadj ,_ 4<sup>:</sup><sup>_λ_0</sup> 1<sup>=0</sup><sup>_._6.</sup> 

whether principal component factors could be employed to improve the forecast of macroeconomic series. 

### **5. Conclusion** 

We developed a theoretical framework that allows the forecast accuracy and encompassing tests proposed by Pitarakis (2023, 2025) to be applied when the alternative forecasting model incorporates estimated principal component factors. These factors can have loadings that are either strong or weak, whether homogeneously or heterogeneously distributed. Our theoretical findings were supported by both a Monte Carlo simulation and two empirical applications in macroeconomic forecasting. 

### **CRediT authorship contribution statement** 

**Luca Margaritella:** Writing – original draft, Software, Methodology, Formal analysis, Data curation. **Ovidijus Stauskas:** Writing – original draft, Validation, Project administration, Methodology, Investigation, Formal analysis, Conceptualization. 

### **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

### **Appendix A. Supplementary data** 

Supplementary material related to this article can be found online at https://doi.org/10.1016/j.ijforecast.2025. 11.005. 

### **Data availability** 

The detailed replication package can be found in this GitHub repository: GitHub - New Tests of Equal Forecast Accuracy for Factor-Augmented Regressions with Weaker Loadings. 

### **References** 

Alessi, L., Barigozzi, M., & Capasso, M. (2010). Improved penalization for determining the number of factors in approximate factor models. _Statistics & Probability Letters_ , _80_ (23–24), 1806–1813. 

- Bai, J., & Ng, S. (2002). Determining the number of factors in approximate factor models. _Econometrica_ , _70_ (1), 191–221. 

- Bai, J., & Ng, S. (2006). Confidence intervals for diffusion index forecasts and inference for factor-augmented regressions. _Econometrica_ , _74_ (4), 1133–1150. 

- Bai, J., & Ng, S. (2023). Approximate factor models with weaker loadings. _Journal of Econometrics_ , _235_ (2), 1893–1916. 

- Barigozzi, M., Cho, H., & Owens, D. (2024). FNETS: Factor-adjusted network estimation and forecasting for high-dimensional time series. _Journal of Business & Economic Statistics_ , _42_ (3), 890–902. 

- Barigozzi, M., & Hallin, M. (2024). The dynamic, the static, and the weak factor models and the analysis of high-dimensional time series. arXiv preprint arXiv:2407.10653. 

Boot, T., & Keijsers, B. (2025). Diffusion index forecasts under weaker loadings: PCA, ridge regression, and random projections. arXiv preprint arXiv:2506.09575. 

Cheng, X., & Hansen, B. E. (2015). Forecasting with factor-augmented regression: A frequentist model averaging approach. _Journal of Econometrics_ , _186_ (2), 280–293. 

Ciccarelli, M., & Mojon, B. (2010). Global inflation. _The Review of Economics and Statistics_ , _92_ (3), 524–535. 

Clark, T. E., & McCracken, M. W. (2001). Tests of equal forecast accuracy and encompassing for nested models. _Journal of Econometrics_ , _105_ (1), 85–110. 

Clark, T. E., & McCracken, M. W. (2012). Reality checks and comparisons of nested predictive models. _Journal of Business & Economic Statistics_ , _30_ (1), 53–66. 

De Mol, C., Giannone, D., & Reichlin, L. (2008). Forecasting using a large number of predictors: Is Bayesian shrinkage a valid alternative to principal components? _Journal of Econometrics_ , _146_ (2), 318–328. 

- Diebold, F. X. (2015). Comparing predictive accuracy, twenty years later: A personal perspective on the use and abuse of Diebold– Mariano tests. _Journal of Business & Economic Statistics_ , _33_ (1), 1–1. 

Eickmeier, S., & Ziegler, C. (2008). How successful are dynamic factor models at forecasting output and inflation? A meta-analytic approach. _Journal of Forecasting_ , _27_ (3), 237–265. 

Fan, J., Liao, Y., & Yao, J. (2015). Power enhancement in highdimensional cross-sectional tests. _Econometrica_ , _83_ (4), 1497–1541. 

Forni, M., Giannone, D., Lippi, M., & Reichlin, L. (2009). Opening the black box: Structural factor models with large cross sections. _Econometric Theory_ , _25_ (5), 1319–1347. 

Fosten, J. (2016). Forecast evaluation with factor-augmented models. _UEA School of Economics Working Paper_ , _5_ , 110. 

19 

**<mark>ARTICLE IN PRESS</mark>** 

_International Journal of Forecasting xxx (xxxx) xxx_ 

_L. Margaritella and O. Stauskas_ 

Freyaldenhoven, S. (2022). Factor models with local factors – determining the number of relevant factors. _Journal of Econometrics_ , _229_ (1), 80–102. 

Gillitzer, C., & McCarthy, M. (2019). Does global inflation help forecast inflation in industrialized countries? _Journal of Applied Econometrics_ , _34_ (5), 850–857. 

- Gonçalves, S., McCracken, M. W., & Perron, B. (2017). Tests of equal accuracy for nested models with estimated factors. _Journal of Econometrics_ , _198_ (2), 231–252. 

Gonçalves, S., & Perron, B. (2014). Bootstrapping factor-augmented regression models. _Journal of Econometrics_ , _182_ (1), 156–173. 

Hansen, B. E. (1992). Convergence to stochastic integrals for dependent heterogeneous processes. _Econometric Theory_ , _8_ (4), 489–500. Hansen, P. R., & Timmermann, A. (2015). Equivalence between outof-sample forecast comparisons and wald statistics. _Econometrica_ , _83_ (6), 2485–2505. 

He, Y., Li, L., Liu, D., & Zhou, W.-X. (2025). Huber principal component analysis for large-dimensional factor models. _Journal of Econometrics_ , _249_ , Article 105993. 

- Hendry, D. F., & Richard, J.-F. (1982). On the formulation of empirical models in dynamic econometrics. _Journal of Econometrics_ , _20_ (1), 3–33. 

Karabiyik, H., & Westerlund, J. (2021). Forecasting using cross-section average–augmented time series regressions. _The Econometrics Journal_ , _24_ (2), 315–333. 

Ludvigson, S. C., & Ng, S. (2009). Macro factors in bond risk premia. _The Review of Financial Studies_ , _22_ (12), 5027–5067. 

McCracken, M. W. (2007). Asymptotics for out of sample tests of Granger causality. _Journal of Econometrics_ , _140_ (2), 719–752. McCracken, M. W., & Ng, S. (2016). FRED-MD: A monthly database for macroeconomic research. _Journal of Business & Economic Statistics_ , _34_ (4), 574–589. 

Mikolajun, I., & Lodge, D. (2016). Advanced economy inflation: The role of global factors. ECB working paper no. 1948. 

- Monacelli, T., & Sala, L. (2009). The international dimension of inflation: Evidence from disaggregated consumer price data. _Journal of Money, Credit and Banking_ , _41_ , 101–120. 

- Onatski, A. (2012). Asymptotics of the principal components estimator of large factor models with weakly influential factors. _Journal of Econometrics_ , _168_ (2), 244–258. 

- Pesaran, M. H. (2006). Estimation and inference in large heterogeneous panels with a multifactor error structure. _Econometrica_ , _74_ (4), 967–1012. 

- Pitarakis, J.-Y. (2023). Direct multi-step forecast based comparison of nested models via an encompassing test. arXiv preprint arXiv: 2312.16099. 

- Pitarakis, J.-Y. (2025). A novel approach to predictive accuracy testing in nested environments. _Econometric Theory_ , _41_ (1), 35–78. 

- Rossi, B. (2005). Testing long-horizon predictive ability with high persistence, and the Meese–Rogoff puzzle. _International Economic Review_ , _46_ (1), 61–92. 

- Stauskas, O., & Westerlund, J. (2022). Tests of equal forecasting accuracy for nested models with estimated CCE factors. _Journal of Business & Economic Statistics_ , _40_ (4), 1745–1758. 

- Stock, J. H., & Watson, M. W. (2002a). Forecasting using principal components from a large number of predictors. _Journal of the American Statistical Association_ , _97_ (460), 1167–1179. 

- Stock, J. H., & Watson, M. W. (2002b). Macroeconomic forecasting using diffusion indexes. _Journal of Business & Economic Statistics_ , _20_ (2), 147–162. 

- Su, L., Wang, F., & Wang, Y. (2025). Estimation and inference for unbalanced panel data models with interactive fixed effects. Available at SSRN 5176534. 

- Uematsu, Y., & Yamagata, T. (2022). Inference in sparsity-induced weak factor models. _Journal of Business & Economic Statistics_ , _41_ (1), 126–139. 

- Yan, Y., & Cheng, T. (2022). Factor-augmented forecasting regressions with threshold effects. _The Econometrics Journal_ , _25_ (1), 134–154. 

20 

