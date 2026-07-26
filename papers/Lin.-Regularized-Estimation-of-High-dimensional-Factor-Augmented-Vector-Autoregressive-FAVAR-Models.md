---
title: **Regularized Estimation of High-dimensional Factor-Augmented Vector Autoregressive (FAVAR) Models**
type: paper
source_pdf: raw/papers/Lin. Regularized Estimation of High-dimensional Factor-Augmented Vector Autoregressive (FAVAR) Models.pdf
converted: 2026-07-26
---

Journal of Machine Learning Research 21 (2020) 1-51 

Submitted 10/19; Revised 3/20; Published 6/20 

# **Regularized Estimation of High-dimensional Factor-Augmented Vector Autoregressive (FAVAR) Models** 

## **Jiahe Lin** 

jiahelin@umich.edu 

_Department of Statistics University of Michigan Ann Arbor, MI 48109, USA_ 

## **George Michailidis** 

gmichail@ufl.edu 

_Department of Statistics and the Informatics Institute University of Florida Gainesville, FL 32611, USA_ 

**Editor:** Xiaotong Shen 

# **Abstract** 

A factor-augmented vector autoregressive (FAVAR) model is defined by a VAR equation that captures lead-lag correlations amongst a set of observed variables _X_ and latent factors _F_ , and a calibration equation that relates another set of observed variables _Y_ with _F_ and _X_ . The latter equation is used to estimate the factors that are subsequently used in estimating the parameters of the VAR system. The FAVAR model has become popular in applied economic research, since it can summarize a large number of variables of interest as a few factors through the calibration equation and subsequently examine their influence on core variables of primary interest through the VAR equation. However, there is increasing need for examining lead-lag relationships between a large number of time series, while incorporating information from another high-dimensional set of variables. Hence, in this paper we investigate the FAVAR model under high-dimensional scaling. We introduce an appropriate identification constraint for the model parameters, which when incorporated into the formulated optimization problem yields estimates with good statistical properties. Further, we address a number of technical challenges introduced by the fact that estimates of the VAR system model parameters are based on estimated rather than directly observed quantities. The performance of the proposed estimators is evaluated on synthetic data. Further, the model is applied to commodity prices and reveals interesting and interpretable relationships between the prices and the factors extracted from a set of global macroeconomic indicators. 

**Keywords:** Model Identifiability; Compactness; Low-rank plus Sparse Decomposition; Finite-Sample Bounds 

# **1. Introduction** 

There is a growing need in employing a large set of time series (variables) for modeling social or physical systems. For example, economic policy makers have concluded based on extensive empirical evidence (e.g. Sims, 1980; Bernanke et al., 2005; Ba´nbura et al., 2010) that large scale models of economic indicators provide improved forecasts, together with better estimates of how current economic shocks propagate into the future, which produces better guidance for policy actions. Another reason for considering large number of time series in 

_⃝_ c 2020 Jiahe Lin and George Michailidis. 

License: CC-BY 4.0, see `https://creativecommons.org/licenses/by/4.0/` . Attribution requirements are provided at `http://jmlr.org/papers/v21/19-874.html` . 

Lin and Michailidis 

social sciences is that key variables implied by theoretical models for policy decisions<sup>1</sup> are not directly observable, but related to a large number of other variables that collectively act as a good proxy of the unobservable key variables. In other domains such as genomics and neuroscience, advent of high throughput technologies have enabled researchers to obtain measurements on hundreds of genes from functional pathways of interest (Shojaie and Michailidis, 2010) or brain regions (Seth et al., 2015), thus allowing a more comprehensive modeling to gain insights into biological mechanisms of interest. There are two popular modeling paradigms for such large panel of time series, with the first being the Vector Autoregressive (VAR) model (L¨utkepohl, 2005) and the second being the Dynamic Factor Model (DFM) (Stock and Watson, 2002; L¨utkepohl, 2014). 

The VAR model has been the subject of extensive theoretical and empirical work primarily in econometrics, due to its relevance in macroeconomic and financial modeling. However, the number of model parameters increases quadratically with the number of time series included for each lag period considered, and this feature has limited its applicability since in many applications it is hard to obtain adequate number of time points for accurate estimation. Nevertheless, there is a recent body of technical work that leveraging _structured sparsity_ and the corresponding regularized estimation framework has established results for consistent estimation of the VAR parameters under high dimensional scaling. Basu and Michailidis (2015) examined Lasso penalized Gaussian VAR models and proved consistency results, while at the same time providing technical tools useful for analysis of sparse models involving temporally dependent data. Melnyk and Banerjee (2016) extended the results to other regularizers, Lin and Michailidis (2017) to the inclusion of exogenous variables (the so-called VAR-X model in the econometrics literature), Hall et al. (2019) to models for count data and Nicholson et al. (2017) to the simultaneous estimation of time lags and model parameters. However, a key requirement for the theoretical developments is a spectral radius constraint that ensures the _stability_ of the underlying VAR process (see Basu and Michailidis, 2015; Lin and Michailidis, 2017, for details). For large VAR models, this constraint implies a smaller magnitude on average for all model parameters, which makes their estimation more challenging, unless one compensates with a higher level of sparsity. Nevertheless, very sparse VAR models may not be adequately informative, while their estimation requires larger penalties that in turn induce higher bias due to shrinkage, when the sample size stays fixed. 

The DFM model aims to decompose a large number of time series into a few common latent factors and idiosyncratic components. The premise is that these common factors are the key drivers of the observed data, which themselves can exhibit temporal dynamics. They have been extensively used for forecasting purposes in economics (Stock and Watson, 2002), while their statistical properties have been studied in depth (see Bai and Ng, 2008, and references therein). Despite their ability to handle very large number of time series, theoretically appealing properties and extensive use in empirical work in economics, DFMs aggregate the underlying time series and hence are not suitable for examining their individual cross-dependencies. Since in many applications researchers are primarily interested in understanding the interactions between key variables (Sims, 1980; Stock and Watson, 2016), 

> 1. such as the concept of output gap for monetary policy, the latter defined as the difference between the actual output of an economy and its potential output 

2 

Estimating High-Dimensional FAVAR Models 

while accounting for the influence of many others so as to avoid model misspecification that leads to biased results, DFMs may not be the most appropriate model. 

To that end, Bernanke et al. (2005) proposed a “fusion” model, namely the Factor Augmented VAR, that aims to summarize the information contained in a large set of time series by a small number of factors and includes those in a standard VAR model. Specifically, let _{Ft} ∈_ R<sup>_p_1</sup> be the latent factor and _{Xt} ∈_ R<sup>_p_2</sup> the observed sets of variables, they jointly form a VAR system given by 



In addition, there is a large panel of observed time series _Yt ∈_ R<sup>_q_</sup> , whose current values are influenced by both _Xt_ and _Ft_ ; i.e., the calibration equation: 



The primary variables of interest _Xt_ together with the unobserved factors _Ft_ —both are assumed to have small and fixed dimensions—drives the dynamics of the system, and the factors are inferred from (2). 

Even in the low-dimensional setting ( _p_ 2 fixed), there is very limited theoretical work (Bai et al., 2016) on the FAVAR model and some work on identification restrictions for the model parameters (e.g. Bernanke et al., 2005). However, the fixed dimensionality assumption is rather restrictive in many applications; in particular, the model has been extensively used in empirical work in economics and finance (e.g. Eickmeier et al., 2014; Caggiano et al., 2014), yet customarily a very small size block _Xt_ is considered. For example, in Bernanke et al. (2005) that introduces the FAVAR model, _Xt_ comprises of three “core” economic indicators (industrial production, consumer price index and the federal funds rate) and _Yt_ of 120 other economic indicators. The VAR system is augmented by one factor summarizing the macroeconomic indicators, and the augmented system shows 7-lag time dependence that significantly increases the sample size requirement for estimation purposes. In a recent application, Stock and Watson (2016) apply the FAVAR model to macroeconomics effects of oil supply shocks; the augmented VAR system consists of 8 times series (observed and latent), but due to the limitation in sample size to avoid non-stationarities ( _T_ = 120) the lag of the model is fixed to 1. Hence, as argued in Stock and Watson (2016), there is growing need for large scale FAVAR models and this paper aims to examine their estimation and theoretical properties in high-dimensions, leveraging sparsity constraints on key model parameters. 

The key contributions of this paper are twofold: (1) the introduction of an identifiability constraint compatible with the high-dimensional nature of the model, under sparsity assumptions on model parameters Γ and _{A_<sup>(</sup><sup>_k_)</sup> _}_ , and (2) the ensuing formulation of the optimization problem that leads to their estimators based on observational data and estimators’ high-probability error bounds. At the technical level there are two sets of challenges that are successfully resolved: (i) the calibration equation involves both an observed set of covariates and a set of latent factors, and their interactions require careful handling to enable accurate estimation of the factors that constitute part of the input to the augmented VAR system and are crucial for estimating the transition matrix; and (ii) with the presence 

3 

Lin and Michailidis 

of a block of variables in the VAR system that are subject to error due to being estimated rather than directly observed, a number of new technical challenges emerge and they are compounded by the presence of temporal dependence. Note that for ease of presentation, the main technical developments are shown for Gaussian data (all noise processes in (1) and (2) are assumed to be Gaussian), but the key theoretical results are also established for sub-Gaussian and sub-exponential error processes; see Appendix C for a result of independent theoretical interest, even for the standard sparse VAR model. 

_Outline of the paper._ The remainder of the paper is organized as follows. In Section 2, the model identifiability constraint is introduced, followed by formulation of the objective function to be optimized that obtains estimates of the model parameters. Theoretical properties of the proposed estimators, specifically, their high probability finite-sample error bounds, are investigated in Section 3. Subsequently in Section 4, we introduce an empirical implementation procedure for obtaining the estimates and present its performance evaluation based on synthetic data. An application of the model on interlinkages of commodity prices and the influence of world macroeconomic indicators on them is presented in Section 5, while Section 6 provides some concluding remarks. All proofs and other supplementary materials are deferred to Appendices. 

_Notations._ Throughout this paper, we use _|||A|||·_ to denote matrix norms for some generic matrix _A ∈_ R<sup>_m×n_</sup> . For example, _|||A|||_ 1 and _|||A|||∞_ respectively denote the matrix induced 1-norm and infinity norm, _|||A|||_ op the matrix operator norm and _|||A|||_ F the Frobenius norm. Moreover, We use _∥A∥_ 1 and _∥A∥∞_ respectively to denote the element-wise 1-norm and infinity norm. For two matrices _A_ and _B_ of commensurate dimensions, denote their inner product by _⟨⟨A, B⟩⟩_ = tr( _A_<sup>_⊤_</sup> _B_ ). Finally, we write _A_ ≳ _B_ if there exists some absolute constant _c_ that is independent of the model parameters such that _A ≥ cB_ ; and _A ≍ B_ if _A_ ≳ _B_ and _B_ ≳ _A_ hold simultaneously. 

# **2. Model and Problem Formulation** 

The FAVAR model proposed in Bernanke et al. (2005) has the following two components, as seen in Section 1: a system given in (1) that describes the dynamics of the latent block _Ft ∈_ R<sup>_p_1</sup> and the observed block _Xt ∈_ R<sup>_p_2</sup> that jointly follow a stationary VAR( _d_ ) model (the “VAR equation”); and the model in (2) that characterizes the contemporaneous dependence of the large observed informational series _Yt ∈_ R<sup>_q_</sup> as a linear function of _Xt_ and _Ft_ (the “calibration equation”). Further, _wt_<sup>_F_,</sup><sup>_w_</sup> _t_<sup>_X_</sup> and _et_ are all noise terms that are independent of the predictors, and we assume they are serially uncorrelated mean-zero Gaussian random vectors: _wt_<sup>_F_</sup> _∼N_ (0 _,_ Σ<sup>_F_</sup> _w_<sup>),</sup><sup>_w_</sup> _t_<sup>_X_</sup> _∼N_ (0 _,_ Σ<sup>_X_</sup> _w_<sup>)and</sup><sup>_et∼N_(0</sup><sup>_,_Σ</sup><sup>_e_).Inthis</sup> study we consider a potentially large VAR system that has many coordinates, hence in contrast to Bernanke et al. (2005) and Bai et al. (2016) where both _p_ 1 and _p_ 2 are fixed and small, we allow the size of the observed block, _p_ 2, to be large<sup>2</sup> and to grow with the sample size; yet the size of the latent block, _p_ 1, can not be too large and is still assumed fixed. Moreover, the size of the informational series, _q_ , can also be large and grow with the 

> 2. We do not impose the restriction that _p_ 2 is smaller than the available sample size. 

4 

Estimating High-Dimensional FAVAR Models 

sample size. Further, we assume that the transition matrices _{A_<sup>(</sup><sup>_i_)</sup> _}_<sup>_d_</sup> _i_ =1<sup>andtheregression</sup> coefficient matrix Γ are _sparse_ . Finally, the factor loading matrix Λ is assumed to be dense. 

## **2.1. Model considerations** 

The latent nature of _Ft_ leads to the following observational equivalence across the following two models encoded by (Λ _,_ Γ) and (Λ<sup>�</sup> _,_ Γ), respectively:<sup>�</sup> for any invertible matrix _Q_ 1 _∈_ R<sup>_p_1</sup><sup>_×p_1</sup> and _Q_ 2 _∈_ R<sup>_p_1</sup><sup>_×p_2</sup> , 



where 



In other words, the key model parameters (Λ _,_ Γ) and the latent factors _Ft_ are _not uniquely_ identified, a known problem even in classical factor analysis (Anderson, 1958). Thus, additional restrictions are required to overcome this indeterminacy, since there is an equivalence class parametrized by ( _Q_ 1 _, Q_ 2) within which individual models are not mutually distinguishable based on observational data. For the FAVAR model, a total number of _p_<sup>2</sup> 1<sup>+</sup><sup>_p_1</sup><sup>_p_2</sup> restrictions are needed for unique identification of Λ, Γ and _Ft_ . 

Various schemes have been proposed in the literature to address this issue. Specifically, Bernanke et al. (2005) impose the necessary restrictions through the coefficient matrices of the calibration equation, requiring Λ = � I _p∗_ 1 � and Γ[1: _p_ 1] _,·_ = 0; that is, the upper _p_ 1 _× p_ 1 block of Λ is set to the identity matrix and the first _p_ 1 rows of Γ to zero. Bai et al. (2016) consider different sets of restrictions that involve combinations of coefficients from the calibration equation and the noise term from the VAR equation. In the low-dimensional setting ( _p_ 2 fixed), one can proceed to estimate the parameters subject to these restrictions, by adopting either a single-step Bayesian likelihood approach (Bernanke et al., 2005) or an orthogonal projection-based approach by profiling out _Xt_ (Bai et al., 2016). However, neither approach is applicable in high-dimensional settings, due to the growing dimension _p_ 2 which would render a projection-based approach infeasible or add to the computational demands of a Bayesian procedure. 

To overcome these issues in high-dimensional settings, we introduce an alternative identification scheme “IR+Compactness” that is compatible with the model specification and can also be seamlessly incorporated in the estimation procedure, leveraging sparsity of the regression coefficient Γ. Specifically, we first impose constraint (IR): 

**(IR)** Λ = � I _p∗_ 1 �: the upper _p_ 1 _× p_ 1 block of Λ is an identity matrix, while the bottom block is left unconstrained. 

Note that (IR) imposes _p_<sup>2</sup> 1<sup>constraintsbutcruciallynotonthelatentfactors,giventheir</sup> subsequent utilization in the VAR system. Further, it yields uniquely identifiable Λ and _Ft_ , for any given product Λ _Ft_ , and the indeterminacy incurred by _Q_ 1 _∈_ R<sup>_p_1</sup><sup>_×p_1</sup> in (3) vanishes. However, the issue is not fully resolved, since for any _Q_ 2 _∈_ R<sup>_p_1</sup><sup>_×p_2</sup> , the following relationship holds: 



5 

Lin and Michailidis 

where 



All such models encoded by ( _F_<sup>ˇ</sup> _t,_ Γ),<sup>ˇ</sup> form an equivalence class parametrized by _Q_ 2 that specifies the transformation. We denote this equivalence class by _C_ ( _Q_ 2). If _Q_ 2 = _O_ , then _C_ ( _Q_ 2) degenerates to a singleton that contains only the true data-generating model, which requires the imposition of _p_ 1 _p_ 2 restrictions on primary model quantities. One applicable constraint out of theoretical consideration is to impose orthogonality on _Xt_ and _Ft_ — it yields the necessary _p_ 1 _p_ 2 restrictions; yet is excessively stringent and limits the appeal of the FAVAR model, while also being challenging to operationalize. Therefore as a good working alternative, we address the identifiability issue through a weaker constraint that effectively limits sufficiently the size of the _C_ ( _Q_ 2). 

To this end, let **X** _∈_ R<sup>_n×p_2</sup> , **Y** _∈_ R<sup>_n×q_</sup> and **F** _∈_ R<sup>_n×p_1</sup> be centered data matrices whose rows are samples of _Xt_ , _Yt_ and the latent process _Ft_ respectively, and **F**<sup>ˇ</sup> is analogously defined. The characterization of _C_ ( _Q_ 2) is through the sample versions of the underlying processes. Specifically, define the set of _factor hyperplanes_ induced by _C_ ( _Q_ 2) by 



and we let Θ<sup>_⋆_</sup> denote the factor hyperplane associated with the true data-generating model, to distinguish it from some generic element in _S_ (Θ)<sup>ˇ</sup> that is denoted by Θ.<sup>ˇ</sup> Note that Θ<sup>_⋆_</sup> _∈S_ (Θ)<sup>ˇ</sup> and Θ<sup>ˇ</sup> coincides with Θ<sup>_⋆_</sup> when _Q_ 2 = 0. Moreover, all elements in _S_ (Θ)<sup>ˇ</sup> are at most of rank _p_ 1, hence a low-rank component relative to their size _n × q_ . Next, in a similar spirit to Negahban and Wainwright (2012), we define the following constrained set: 



where _ϕR_ (Θ) is defined according to 



and _κ_ ( _R_<sup>_∗_</sup> ) := supΘ=0 � _|||_ Θ _|||_ F _/R_<sup>_∗_</sup> (Θ)� with _R_<sup>_∗_</sup> being the dual norm of some regularizer _R_ . Base on the above definition, _ϕR_ (Θ) captures the interaction between the factor space and the observed **X** -space; the product _κ_ ( _R_<sup>_∗_</sup> ) _R_<sup>_∗_</sup> (Θ) measures the spikiness of Θ w.r.t. _R_ , and in the case where _R_ corresponds to the sparsity-induced _ℓ_ 1-norm which would be the setup of interest in this paper (see Section 2.2), _R_<sup>_∗_</sup> (Θ) = _∥_ Θ _∥∞_ and _κ_ ( _R_<sup>_∗_</sup> ) =<sup>_√_</sup> _<u>nq</u>_ <u>.</u> With the definition of _Sφ_ (Θ),<sup>ˇ</sup> we impose the following compactness constraint on Θ<sup>ˇ</sup> to further encourage identifiability: 

**(Compactness)** Θ<sup>ˇ</sup> _∈Sφ_ (Θ)<sup>ˇ</sup> for some _φ_ ( _n, q_ ) satisfying _φ_ ( _n, q_ ) _≥ φ_<sup>_⋆_</sup> := _ϕR_ (Θ<sup>_⋆_</sup> ). 

(Compactness) effectively limits the spikiness of all possible Θ’s by imposing a<sup>ˇ</sup> _box constraint_ through the dual norm corresponding to the sparsity regularizer, and for an arbitrary set of fixed realizations, it restricts the factor hyperplane set induced by _C_ ( _Q_ 2) to its _φ_ -radius subset _Sφ_ (Θ).<sup>ˇ</sup> This in turn limits the size of the equivalence class _C_ ( _Q_ 2) under consideration, since there is a one-to-one correspondence at the set level between _C_ ( _Q_ 2) and the factor hyperplane set induced by it. This further implies that although the models encoded by ( _Ft,_ Γ) and ( _F_<sup>ˇ</sup> _t,_ Γ)<sup>ˇ</sup> may not be perfectly distinguishable based on observational data, at the 

6 

Estimating High-Dimensional FAVAR Models 

population level the discordance between the two models can not be too large. It is worth pointing out that the bound _φ_ ( _n, q_ ) is allowed to grow, but at a much slower rate than the size of Θ;<sup>ˇ</sup> specifically, we require _φ_ ( _n, q_ ) = _o_ ( _κ_ ( _R_<sup>_∗_</sup> )). For ease of presentation, we use _φ_ to denote this bound henceforth and further note that it is in fact a constant in any finite sample setting. 

In summary, our proposed identification scheme comprises of two parts: (IR) and (Compactness). The former provides exact identification within the factor hyperplane and narrows the scope of observationally equivalent models to _C_ ( _Q_ 2), while the latter limits its size; and they jointly incur _approximate identification_ of the true data generating model; and thus, for estimation purposes henceforth, it becomes adequate to focus on this restricted equivalence class, rather than its individual elements. The proposed scheme is suitable for the high-dimensional nature of the problem and can easily be incorporated in the formulation of the optimization problem for parameter estimation (see Section 2.2), which in turn yields estimates with tight error bounds (see Section 3). 

## **2.2. Proposed formulation** 

Without loss of generality, we focus on the case where _d_ = 1 in subsequent technical developments, so that _Zt_ := ( _Ft_<sup>_⊤, X_</sup> _t_<sup>_⊤_)</sup><sup>_⊤_followsaVAR(1)model</sup><sup>_Zt_=</sup><sup>_AZt−_1+</sup><sup>_Wt_:</sup> 



The generalization to the VAR( _d_ ) ( _d >_ 1) case is straightforward since for any generic VAR( _d_ ) process satisfying _Ad_ ( _L_ ) _Zt_ = _wt_ where _Ad_ ( _L_ ) := I _− A_<sup>(1)</sup> _L −· · · − A_<sup>(</sup><sup>_d_)</sup> _L_<sup>_d_</sup> , it can always be written in the form of a VAR(1) model for some _dp_ -dimensional process _Z_<sup>�</sup> _t_ (see L¨utkepohl, 2005, for details). 

Based on the introduced model identification scheme (IR+Compactness), we propose the following procedure to estimate the FAVAR model, whose parameters include a sparse coefficient matrix Γ, a dense loading matrix Λ, and a sparse transition matrix _A_ . Observed data matrices **X** and **Y** are identical to what have been previously defined, and to distinguish the responses from their lagged predictors when considering the VAR system, we let **X** _n−_ 1 := [ _x_ 1 _, . . . , xn−_ 1]<sup>_⊤_</sup> denote the predictor matrix and **X** _n_ := [ _x_ 2 _, . . . , xn_ ]<sup>_⊤_</sup> the response one; **F** _n,_ **F** _n−_ 1 _,_ **Z** _n,_ **Z** _n−_ 1 are analogously defined. Based on these notations, the sample versions of the VAR system and the calibration equation in (5) and (2) can be written as 



We propose the following estimators obtained from a two-stage procedure for the coefficient matrices Λ, Γ and subsequently the transition matrices _{Aij}i,j_ =1 _,_ 2. 

- Stage I: estimation of the calibration equation under (IR+Compactness). We formulate the following _constrained optimization_ problem using a least squares loss function and incorporating the sparsity-induced _ℓ_ 1 regularization of the sparse block Γ, the 

7 

Lin and Michailidis 

rank constraint on the hyperplane Θ, and (Compactness): 



Once Θ is obtained, under (IR), the estimated factors<sup>�</sup> **F**<sup>�</sup> and the corresponding loading matrix Λ<sup>�</sup> are extracted as follows: 



where Λ<sup>�PC</sup> 1 is the upper _p_ 1 sub-block of Λ<sup>�PC</sup> , with **F**<sup>�PC</sup> and Λ<sup>�PC</sup> being the PC estimators (Stock and Watson, 2002) given by **F**<sup>�PC</sup> :=<sup>_√_</sup> _<u>nU</u>_<sup>�</sup> and Λ<sup>�PC</sup> := _V_<sup>�</sup> _D/_<sup>�</sup><sup>_√_</sup> _<u>n</u>_ <u>.</u> The estimates _U,_<sup>�</sup> _D_<sup>�</sup> and _V_<sup>�</sup> are obtained from the SVD of Θ<sup>�</sup> = _U_<sup>�</sup> Θ<sup>�</sup> _V_<sup>�</sup><sup>_⊤_</sup> . Note that after these algebra, **F**<sup>�</sup> corresponds to the first _p_ 1 columns of Θ.<sup>�</sup> 

Of note, _|||_ **X** _/_<sup>_√_</sup> _<u>n|||</u>_<sup>2</sup> op<sup>=Λmax(</sup><sup>**X**</sup><sup>_⊤_</sup><sup>**X**</sup><sup>_/n_)anditcanbeshownthatforanyrandom</sup> realizations **X** , the latter can be bounded with high probability (see Lemma 5). 

- Stage II: estimation of the VAR equation based on **X** and **F**<sup>�</sup> . With the estimated factor **F**<sup>�</sup> as the surrogate for the true latent factor **F** , the transition matrix _A_ can be estimated by solving 



where **Z**<sup>�</sup> _n_ := [ **F**<sup>�</sup> _n,_ **X** _n_ ] and **Z**<sup>�</sup> _n−_ 1 is analogously defined. The _ℓ_ 1-norm penalty induces sparsity on _A_ according to the model assumption. 

In the presence of additional contemporaneous dependence amongst the coordinates for the error processes _wt_ , one may consider a maximum likelihood-based loss function, but the full estimation would require additional structural assumptions of Σ _w_ (or its inverse) given the high dimensionality; we do not further elaborate in this study, since our prime interest is estimating the coefficient/transition matrices of the FAVAR model. 

The formulation in (8) based on the least squares loss function and the surrogate **F**<sup>�</sup> is straightforward. However, the formulation for the calibration equation merits additional discussion. First, note that the factor hyperplane Θ has at most rank _p_ 1 and therefore has low rank structure relative to its size _n × q_ . We impose a rank constraint in the estimation procedure to enforce such structure. Together with the (IR+Compactness) constraint introduced above, the objective then becomes to estimate accurately the parameters of a model within the equivalence class _C_ ( _Q_ 2), in the sense that the estimate obtained by solving (6) effectively corresponds to recovering an arbitrary Θ<sup>ˇ</sup> _,_ Θ<sup>ˇ</sup> _∈C_ ( _Q_ 2); such an estimate, however, will be close to the true data generating Θ<sup>_⋆_</sup> . Once this goal is achieved, this would enable accurate estimation of the transition matrix of the VAR system. 

From an optimization perspective, the objective function admits a low-rank-plus-sparse decomposition and compactification is necessary for establishing statistical properties of 

8 

Estimating High-Dimensional FAVAR Models 

the global optima in the absence of explicitly specifying the interaction structure between the low rank and the sparse blocks (or the spaces they live in). Note that the form of the compactness constraint is dictated by the statistical problem under consideration. For example, Agarwal et al. (2012) study a multivariate regression problem, where the coefficient is decomposed to a sparse and a low rank block. In that setting, a compactness constraint is imposed through the entry-wise infinity norm bound of the low rank block. Chandrasekaran et al. (2012) study a graphical model with latent variables where the conditional concentration matrix is the parameter of interest. The marginal concentration matrix is decomposed to a sparse and a low rank block via the alignment of the Schur complement, and the compactness constraint is imposed on both blocks and manifests through the corresponding regularization terms in the resulting optimization problem. Hence, the compactness constraint takes different forms but ultimately serves the same goal, namely, to introduce an upper bound on the magnitude of the low rank–sparse block interaction, with the latter being an important component in analyzing the estimation errors. The compacteness constraint adopted for the FAVAR model serves a similar purpose, although the presence of temporal dependence introduces a number of additional technical challenges compared to the two aforementioned settings that consider independent and identically distributed data. Finally, we remark that the model identification scheme (IR+Compactness) incorporated in the optimization problem as a constraint, enables us to establish high-probability error bounds (relative to the true data generating parameters/factors) for the proposed estimators, as shown next in Section 3. Therefore, although (IR+Compactness) does not encompass the full _p_<sup>2</sup> 1<sup>+</sup><sup>_p_1</sup><sup>_p_2restrictions,itprovidessufficientidentifiabilityforestimation</sup> purposes. 

# **3. Theoretical Properties** 

In this section, we investigate the theoretical properties of the estimators proposed in Section 2.2. We focus on formulations (6) and (8), whose global optima correspond to (Θ<sup>�</sup> _,_ Γ)<sup>�</sup> and _A_<sup>�</sup> , respectively. 

Since (8) relies not only on prime observable quantities (namely _Xt_ ), but also on estimated quantities from Stage I (namely **F**<sup>�</sup> ), the analysis requires a careful examination of how the estimation error in the factor propagates to that of _A_<sup>�</sup> . We start by outlining a road map of our proof strategy together with a number of regularity conditions needed in subsequent developments. Section 3.1 establishes error bounds for Γ,<sup>�</sup> Θ<sup>�3</sup> and _A_<sup>�</sup> under certain regularity conditions and employing suitable choices of the tuning parameters, for _deterministic realizations_ from the underlying observable processes. Specifically when considering the error bound of _A_<sup>�</sup> , the error of the plug-in estimate **F**<sup>�</sup> is assumed non-random and given. Subsequently, Section 3.2 examines the probability of the events in which the regularity conditions are satisfied for _random realizations_ , and further establishes high-probability upper bounds for quantities to which the tuning parameters need to conform. Finally, the high-probability finite sample error bounds for the estimates obtained based on random realizations of the data generating processes readily follow after properly aligning the conditioning arguments, and the results are presented in Section 3.3. All proofs are deferred to Appendices A and B. 

> 3. Consequently, the error bounds of **F**<sup>�</sup> and Λ<sup>�</sup> under (IR) are also obtained. 

9 

Lin and Michailidis 

_Additional notations._ Throughout, we use superscript _⋆_ to denote the true value of the parameters of interest, and ∆for errors of the estimators; e.g., ∆ _A_ = _A_<sup>�</sup> _− A_<sup>_⋆_</sup> . For sample quantities (e.g., **X** and **F** ) and their corresponding error (e.g., ∆ **F** ), we use subscript ( _n −_ 1) to denote their first _n −_ 1 rows. We let _S_ **E** := _n_<sup><u>1</u></sup><sup>**E**</sup><sup>_⊤_</sup><sup>**E**denotethesamplecovariancematrix</sup> of **E** and the sample covariance of other quantities are analogously defined. Additionally, denote the density level of Γ<sup>_⋆_</sup> by _s_ Γ _⋆_ := _∥_ Γ<sup>_⋆_</sup> _∥_ 0, and that of _A_<sup>_⋆_</sup> by _sA⋆_ . _A road map for establishing consistency results._ As previously mentioned, the key steps are: 

- Part 1: analyses based on deterministic realizations using the optimality of the estimators, assuming the parameters of the objective function (e.g., the Hessian and the penalty parameter) satisfy certain regularity conditions; 

- Part 2: analyses based on random realizations that the probability of the regularity conditions being satisfied, primarily involving the utilization of concentration inequalities. 

In Part 1, note that the first-stage estimators obtained from the calibration equation are based on observed data and thus the regularity conditions needed are imposed on (functions of) the observed samples. On the other hand, the second-stage estimator relies on the plugged-in first-stage estimates that have bounded errors; therefore, the analysis is carried out in an analogous manner to problems involving error-in-variables. Specifically, the required regularity conditions on quantities appearing in the optimization (8) involve the error of the first stage estimates, with the latter assumed fixed. In Part 2, the focus shifts to the probability of the regularity conditions being satisfied under random realizations, again starting from the first stage estimates, with the aid of Gaussian concentration inequalities and proper accounting for temporal dependence. Once the required regularity conditions are shown to hold with high probability, combining the results established in Part 1 for deterministic realizations, the high-probability error bounds for Θ<sup>�</sup> and Γ<sup>�</sup> are established. The high-probability error bound of the estimated factors readily follows, which ensures that the variables which Stage II estimates rely upon are sufficiently accurate with high probability. Based on the latter result, the regularity conditions required for the Stage II estimates are then verified to hold with high probability at a certain rate. In the FAVAR model, since the estimation of the VAR equation is based on quantities among which one block is subject to error, to obtain an accurate estimate of the transition matrix requires more stringent conditions on population quantities (e.g., extremes of the spectrum), so that the regularity conditions hold with high probability. In essence, the joint process _Zt_ need to be adequately “regular” in order to get good estimates of the transition matrix , vis-a-vis the case of the standard VAR model where all variables are directly observed. 

Next, we introduce the following key concepts that are widely used in establishing theoretical properties of high-dimensional regularized _M_ -estimators (e.g. Negahban et al., 2012; Loh and Wainwright, 2012), as well as quantities that are related to processes exhibiting temporal dependence (see also Basu and Michailidis, 2015). 

10 

Estimating High-Dimensional FAVAR Models 

**Definition 1 (Restricted strong convexity (RSC))** _A matrix_ **X** _∈_ R<sup>_n×p_</sup> _satisfies the RSC condition with respect to norm_ Φ _with curvature αRSC >_ 0 _and tolerance τn ≥_ 0 _, if_ 



_In our setting, we consider the norm_ Φ(∆) = _∥_ ∆ _∥_ 1 _._ 

**Definition 2 (Deviation condition)** _For a regularized M -estimator given in the generic form of_ 



_with HA_ := _n_<sup><u>1</u></sup><sup>**X**</sup><sup>_⊤_</sup><sup>**X**</sup><sup>_denoting the Hessian and GA_:=</sup> _n_<sup><u>1</u></sup><sup>**Y**</sup><sup>_⊤_</sup><sup>**X**</sup><sup>_denoting the gradient,we define_</sup> _the tuning parameter λA to be selected in accordance with the deviation condition, if_ 



Under the current model setup, however, the exact form of the deviation bound becomes more involved and requires proper modifications to incorporate quantities associated with the factor hyperplane, as seen in Proposition 1. 

**Definition 3 (Spectrum and its extremes)** _For a p-dimensional stationary process Xt, its spectral density fX_ ( _ω_ ) _is defined as_ 



_where_ Σ _X_ ( _h_ ) := E( _XtXt_<sup>_⊤_</sup> + _h_<sup>)</sup><sup>_.Itsupperandlowerextremesaredefinedas_</sup> 



_The cross-spectrum for two generic stationary processes Xt and Yt is defined as_ 



_where_ Σ _X,Y_ ( _h_ ) := E( _XtYt_<sup>_⊤_</sup> + _h_<sup>)</sup><sup>_,anditsupperextremeisdefinedas_</sup> 



_where ∗ denotes the conjugate transpose._ 

� We �start by providing error bounds for Γ<sup>�</sup> and Θ,<sup>�</sup> as well as those of the corresponding **F** and Λ extracted under (IR). For the optimization problem given in (6), we assume that _r ≥ p_ 1 and _φ_ is always compatible with the true data generating mechanism, so that Θ<sup>_⋆_</sup> is always feasible. To this end, the error bounds of Θ<sup>�</sup> and Γ<sup>�</sup> for deterministic realizations 

11 

Lin and Michailidis 

crucially rely on two components: (i) **X** satisfying the RSC condition with curvature _α_ RSC<sup>**X**;</sup> and (ii) the tuning parameter _λ_ Γ being chosen in accordance with the deviation bound condition that is associated with the interaction between **X** and **E** , the strength of the noise, and the interaction between the space spanned by the factor hyperplane and the observed **X** . Upon the satisfaction of these conditions, the error bounds of Θ<sup>�</sup> and Γ<sup>�</sup> are given by 



and these conditions hold with high probability for random realizations of� � _Xt_ and _Yt_ . Since **F** is the first _p_ 1 columns of Θ, it possesses an error bound of the similar form. 

Next, we briefly sketch the error bounds of _A_<sup>�</sup> . For the optimization in (8), for deterministic realizations, the results in Basu and Michailidis (2015) can be applied with the corresponding RSC condition and deviation condition imposed on quantities associated with� � � **Z** _n_ and **Z** _n−_ 1, and the error for _A_ is in the form of 



Then, for random realizations, assuming ∆ **F** known and non-random, to satisfy the corresponding regularity conditions, we additionally require that the following functional involving the spectral density of the underlying joint process _Zt_ exhibits adequate curvature, that is, m( _fZ_ ) _/_ ~~�~~ _M_ ( _fZ_ ) _> c_ 0 _h_ 1(∆ **F** _n−_ 1) for constant _c_ 0 and some function _h_ 1 of the error ∆ **F** _n−_ 1 that captures its magnitude. Moreover, the deviation bound is of the form _h_ 2(∆ **F** ), which can be viewed as another function of the error<sup>4</sup> . Further, since ∆ **F** is bounded with high probability from the analysis in Stage I, it will be established that _h_ 1(∆ **F** ) and _h_ 2(∆ **F** ) are both upper bounded at a certain rate, thus ensuring that the RSC condition and the deviation conditions can both be satisfied unconditionally, by properly choosing the required constants. 

## **3.1. Statistical error bounds with deterministic realizations** 

Proposition 1 below gives the error bounds for the estimators in (6), assuming certain regularity conditions hold for deterministic realizations of the processes _Xt_ and _Yt_ , upon suitable choice of the regularization parameters. 

**Proposition 1 (Bound for** ∆Θ **and** ∆Γ **under fixed realizations)** _Suppose the fixed realizations_ **X** _∈_ R<sup>_n×p_2</sup> _of process {Xt ∈_ R<sup>_p_2</sup> _} satisfies the RSC condition with curvature αRSC_<sup>**X**</sup><sup>_>_0</sup><sup>_andatoleranceτ_</sup><sup>**X**</sup><sup>_forwhich_</sup> 



_Then, for any matrix pair_ (Θ<sup>_⋆_</sup> _,_ Γ<sup>_⋆_</sup> ) _satisfying the constraint ϕR_ (Θ<sup>_⋆_</sup> ) _≤ φ that generates_ **Y** _, for estimators_ (Θ<sup>�</sup> _,_ Γ)<sup>�</sup> _obtained by solving_ (6) _with regularization parameters λ_ Γ _satisfying_ 



> 4. note the deviation bound in principle also depends on other population quantities such as m( _fZ_ ), _M_ ( _fZ_ ), Λmax(Σ _w_ ) etc. 

12 

Estimating High-Dimensional FAVAR Models 

_the following bound holds:_ 



Based on Proposition 1, under fixed realizations of _Xt_ and _Yt_ , the error bounds of Γ<sup>�</sup> and Θ<sup>�</sup> are established. Using these Stage I estimates and the IR condition, estimates of the factors and their loadings can be calculated. In particular, since ∆ **F** corresponds to the first _p_ 1 columns of ∆Θ, the above bound automatically holds for ∆ **F** . Further, the following lemma provides the relative error of the estimated Λ under (IR) and the condition on Λ<sup>1</sup> max<sup>_/_2(</sup><sup>_S_</sup> **F**<sup>),withthelattertranslatingtotherequirementthattheleadingsignalof</sup><sup>**F**</sup> overrules the averaged row error of ∆Θ. 

**Lemma 1 (Bound of** ∆Λ **)** _The following error bound holds for_ Λ<sup>�</sup> _, provided that_ Λ<sup>1</sup> max<sup>_/_2(</sup><sup>_S_</sup> **F**<sup>)</sup><sup>_>_</sup> _|||_ ∆Θ _/_<sup>_√_</sup> _<u>n|||F:</u>_ 



Up to this point, error bounds have been obtained for all the parameters in the calibration equation. The following proposition establishes the error bound for the estimator obtained from solving (8), based on observed **X** and estimated **F**<sup>�</sup> , and assuming ∆ **F** is 

**Proposition 2 (Bound for** ∆ _A_ **under fixed realization and a non-random** ∆ **F)** _Consider the estimator A_<sup>�</sup> _obtained by solving_ (8) _. Suppose the following conditions hold:_ 

- _A1._ **Z**<sup>�</sup> _n−_ 1 := [ **F**<sup>�</sup> _n−_ 1 _,_ **X** _n−_ 1] _satisfies the RSC condition with curvature αRSC_<sup>**Z**�</sup><sup>_andtolerance_</sup> _τ_ **Z** _for which sA⋆τ_ **Z** _< αRSC_<sup>**Z**�</sup><sup>_/_64</sup><sup>_;_</sup> 

- _⋆ ⊤_ 

- _A2. ∥_ **Z**<sup>�</sup><sup>_⊤_</sup> _n−_ 1�� **Z** _n −_ **Z** _n−_ 1( _A_ ) � _/n∥∞ ≤ C_ ( _n, p_ 1 _, p_ 2) _where C_ ( _n, p_ 1 _, p_ 2) _is some function that depends on n, p_ 1 _and p_ 2 _._ 

_Then, for any λA ≥_ 4 _C_ ( _n, p_ 1 _, p_ 2) _, the following error bound holds for A_<sup>�</sup> _:_ 



Note that Proposition 2 applies the results in Basu and Michailidis (2015, Proposition 4.1) to� the setting� in this study, where Stage II estimation of the transition matrix is based on **Z** _n_ and **Z** _n−_ 1; consequently, the regularity conditions should be imposed on corresponding quantities associated with **Z**<sup>�</sup> _n_ and **Z**<sup>�</sup> _n−_ 1. 

Propositions 1 and 2 give finite sample error bounds for the estimators of the parameters obtained by solving optimization problems (6) and (8) based on fixed realizations of the observable processes _Xt_ and _Yt_ , and the regularity conditions outlined. Next, we examine and verify these conditions for random realizations of the processes, to establish high probability error bounds for these estimators. 

13 

Lin and Michailidis 

## **3.2. High probability bounds under random realizations** 

We provide high probability bounds or concentrations for the quantities associated with the required regularity conditions, for random realizations of _Xt_ and _Yt_ . Specifically, we note that when _Xt_ is considered separately from the joint system, it follows a high-dimensional VAR-X model (Lin and Michailidis, 2017) 



whose spectrum _fX_ ( _ω_ ) satisfies 

_fX_ ( _ω_ ) = � _A_<sup>_−_</sup> _X_<sup>1(</sup><sup>_e−iω_)</sup> �� _A_ 21 _fF_ ( _ω_ ) _A_<sup>_⊤_</sup> 21<sup>+</sup><sup>_f_</sup> _w_<sup>_X_(</sup><sup>_ω_) +</sup><sup>_f_</sup> _w_<sup>_X_</sup> _,F_<sup>(</sup><sup>_ω_)</sup><sup>_A⊤_</sup> 21<sup>+</sup><sup>_A_21</sup><sup>_f_</sup> _F,w_<sup>_X_(</sup><sup>_ω_)</sup> �� _A_<sup>_−_</sup> _X_<sup>1(</sup><sup>_e−iω_)</sup> � _∗,_ where _AX_ ( _L_ ) := I _− A_ 22 _L_ . Similar properties hold for _Ft_ . Throughout, we assume _{Xt}, {Ft}_ and _{Yt}_ are all mean-zero stable Gaussian processes. 

Lemmas 2 to 4 respectively verify the RSC condition associated with **X** and establish the high probability bounds for _∥_ **X**<sup>_⊤_</sup> **E** _/n∥∞_ , Λmax( _S_ **E** ) and Λmax( _S_ **X** ). 

**Lemma 2 (Verification of the RSC condition for X)** _Consider_ **X** _∈_ R<sup>_n×p_2</sup> _whose rows correspond to a random realization {x_ 1 _, . . . , xn} of the stable Gaussian {Xt} process, and its dynamics are governed by_ (5) _. Then, there exist positive constants ci >_ 0 _, i_ = 1 _,_ 2 _, such that with probability at least_ 1 _− c_ 1 exp( _−c_ 2 _n_ min _{γ_<sup>_−_2</sup> _,_ 1 _}_ ) _where γ_ := 54 _M_ ( _gX_ ) _/_ m( _gX_ ) _, the RSC condition holds for_ **X** _with curvature αRSC_<sup>**X**</sup><sup>_andtoleranceτ_</sup><sup>**X**</sup><sup>_satisfying_</sup> 



_provided that n_ ≳ log _p_ 2 _._ 

**Lemma 3 (High probability bound for** _∥_ **X**<sup>_⊤_</sup> **E** _/n∥∞_ **)** _There exist positive constants ci_ ( _i_ = 0 _,_ 1 _,_ 2) _such that for sample size n_ ≳ log( _p_ 2 _q_ ) _, with probability at least_ 1 _−c_ 1 exp( _−c_ 2 log( _p_ 2 _q_ )) _, the following bound holds:_ 



**Lemma 4 (High probability bound for** Λmax( _S_ **E** ) **)** _Consider_ **E** _∈_ R<sup>_n×q_</sup> _whose rows are independent realizations of the mean zero Gaussian random vector et with covariance_ Σ _e. Then, for sample size n_ ≳ _q, with probability at least_ 1 _−_ exp( _−n/_ 2) _, the following bound holds:_ 



**Lemma 5 (High probability bound for** Λmax( _S_ **X** ) **)** _Consider_ **X** _∈_ R<sup>_n×p_2</sup> _whose rows correspond to a random realization {x_ 1 _, . . . , xn} of the stable Gaussian {Xt} process, and its dynamics are governed by_ (5) _. There exist positive constants ci >_ 0 _, i_ = 0 _,_ 1 _,_ 2 _, such that for sample size n_ ≳ _p_ 2 _, with probability at least_ 1 _− c_ 1 exp( _−c_ 2 _n_ ) _, the following bound holds:_ 



14 

Estimating High-Dimensional FAVAR Models 

In the next two lemmas, we verify the RSC condition for random� realizations of **Z**<sup>�</sup> _n−_ 1 _⋆ ⊤_ and obtain the high probability bound _C_ ( _n, p_ 1 _, p_ 2) for _∥_ **Z**<sup>�</sup><sup>_⊤_</sup> _n−_ 1�� **Z** _n −_ **Z** _n−_ 1( _A_ ) � _/n∥∞_ , with the underlying truth **F** being random but the error ∆ **F** non-random. Note that this can be equivalently viewed as a _conditional_ RSC condition and deviation bound, when conditioning on some fixed ∆ **F** . 

**Lemma 6 (Verification of RSC for Z**<sup>�</sup> _n−_ 1 **)** _Consider_ **Z**<sup>�</sup> _n−_ 1 _given by_ 



_with rows of_ [ **F** _n−_ 1 _,_ **X** _n−_ 1] _being a random realization drawn from process {Zt} whose dynamics are given by_ (5) _. Suppose the lower and upper extremes of its spectral density fZ_ ( _ω_ ) _satisfy_ 



_for some constant c_ 0 _≥_ 6 _. Then, with probability at least_ 1 _− c_ 1 exp( _−c_ 2 _n_ ) _,_ **Z**<sup>�</sup> _n−_ 1 _satisfies the RSC condition with curvature_ 



_and tolerance_ 





� _⋆ ⊤_ **Lemma 7 (Deviation bound for** _∥_ **Z**<sup>�</sup><sup>_⊤_</sup> _n−_ 1�� **Z** _n −_ **Z** _n−_ 1( _A_ ) � _/n∥∞_ **)** _There exist positive constants ci_ ( _i_ = 1 _,_ 2) _and Ci_ ( _i_ = 1 _,_ 2 _,_ 3) _such that with probability at least_ 1 _− c_ 1 exp � _− c_ 2 log( _p_ 1 + _p_ 2)� _we have_ 



_where εn_ := ∆ **Z** _n −_ ∆ **Z** _n−_ 1( _A_<sup>_⋆_</sup> )<sup>_⊤_</sup> = [∆ **F** _n −_ ∆ **F** _n−_ 1( _A_<sup>_⋆_</sup> 11<sup>)</sup><sup>_⊤, −_∆</sup><sup>**F**</sup> _n−_ 1<sup>(</sup><sup>_A⋆_</sup> 21<sup>)</sup><sup>_⊤_]</sup><sup>_,and{W_+</sup> _t_<sup>_}_:=</sup> _{Wt_ +1 _} is the shifted Wt process._ 

**Remark 1** Before moving to the high probability error bounds of the estimates, we discuss the conditions and the various quantities appearing in Lemmas 6 and 7 that determine the error bound of the estimated transition matrix and underlie the between 

15 

Lin and Michailidis 

the original VAR estimation problem based on primal observed quantities (the “vanilla VAR problem” henceforth), and the present one in which one block of the variables enters the VAR system with errors. Note that the statements in the two lemmas are under the assumption that the error in the _Ft_ block is pre-determined and non-random. 

As previously mentioned, due to the presence of the error of the latent factor block, the corresponding regularity conditions need to be imposed and verified on quantities with the error incorporated, namely, **Z**<sup>�</sup> , instead of the original true random realizations **Z** . Lemma 6 shows that with high probability, the random design matrix although exhibits error-invariables, will still satisfy the RSC condition with some positive curvature as long as the spectrum of the process _Zt_ has sufficient regularity relative to the magnitude of the error, with the former determined by m( _fX_ ) _/M_<sup>1</sup><sup>_/_2</sup> ( _fX_ ) and the latter by Λ<sup>1</sup> max<sup>_/_2(</sup><sup>_S_</sup> ∆ **F** _n−_ 1<sup>).Inpar-</sup> ticular, the RSC curvature is pushed toward zero compared with that in the vanilla VAR problem, due to the presence of the second term in (13) that would be 0 if ∆ **F** _n−_ 1 = 0, i.e., there were no estimation errors. This curvature affects the constant scalar part of the ultimate high probability error bound obtained for the transition matrix. 

Lemma 7 gives the deviation bound associated with the Hessian and the gradient (both random), which comprises of three components attributed to the random samples observed, the non-random error, and their interactions, respectively. Further, it is the relative order of these components that determines the error rate (as a function of model dimensions and the sample size). In particular, for the vanilla VAR problem, only the first term in (14) exists and yields an error rate of _O_ ( ~~�~~ log( _p_ 1 + _p_ 2) _/n_ ) (see also Basu and Michailidis, 2015). For the current setting, as it is later shown in Theorem 1, since _|||_ ∆ **F** _/_<sup>_√_</sup> _<u>n|||</u>_ F _≍O_ (1), the dominating term of the three components is the one attributed to the non-random error<sup>5</sup> and it ultimately determines the error rate of _A_<sup>�</sup> , which will also be _O_ (1). 

## **3.3. High probability error bounds for the estimators** 

Given the results in Sections 3.1 and 3.2, we provide next high probability error bounds for the estimates, obtained by solving the optimization problems in (6) and (8) based on random snapshots from the underlying processes _Xt_ and _Yt_ . 

Theorem 1 combines the results in Proposition 1 and Lemmas 2 to 4 and provides the high probability error bound of the estimates, when Θ and<sup>�</sup> Γ are estimated based on random<sup>�</sup> realizations from the observable processes _Xt_ and _Yt_ , with the latter driven by both _Xt_ and the latent _Ft_ . 

**Theorem 1 (High probability error bounds for** Θ<sup>�</sup> **and** Γ<sup>�</sup> **)** _Suppose we are given some randomly observed snapshots {x_ 1 _, . . . , xn} and {y_ 1 _, . . . , yn} obtained from the stable Gaussian processes Xt and Yt, whose dynamics are described in_ (5) _and_ (2) _. Suppose the following conditions hold for some_ ( _CX,l, CX,u_ ) _and_ ( _Ce,l, Ce,u_ ) _:_ 

_C1. CX,l ≤_ m( _fX_ ) _≤M_ ( _fX_ ) _≤ CX,u;_ 

_C2. Ce,l ≤_ Λmin(Σ _e_ ) _≤_ Λmax(Σ _e_ ) _≤ Ce,u._ 

5. with the implicit assumption that log( _p_ 1 + _p_ 2) _/n_ = _o_ (1) which is satisfied for this study. 

16 

Estimating High-Dimensional FAVAR Models 

_Then, there exist universal constants {Ci} and {ci} such that for sample size n_ ≳ _q, by solving_ (6) _with regularization parameter_ 



_the solution_ (Θ<sup>�</sup> _,_ Γ)<sup>�</sup> _has the following bound with probability at least_ 1 _− c_ 1 exp( _−c_ 2 log( _p_ 2 _q_ )) _:_ 



_for some function ψ_ ( _·_ ) _that depends linearly on s_ Γ _⋆, p_ 1 _and r._ 

Note that the above bound also holds if we replace ∆Θ by ∆ **F** under (IR). Next, using the results in Proposition 2, Lemmas 6 and 7 and combine the bound in Theorem 1, we establish a high probability error bound for the estimated _A_<sup>�</sup> in Theorem 2. 

**Theorem 2 (High probability error bound for** _A_<sup>�</sup> **)** _Under the settings and with the procedures in Theorem 1, we additionally assume the following condition holds for the spectrum of the joint process Zt:_ 



_Then there exists universal constants {ci}, {c_<sup>_′_</sup> _i_<sup>_}and{Ci}suchthatforsamplesizen_≳</sup><sup>_q,_</sup> _such that the estimator A_<sup>�</sup> _obtained by solving for_ (8) _with λA satisfying_ 



_with probability at least_ 



_the following bound holds for_ ∆ _A:_ 



_for some function C_<sup>ˇ</sup> ( _K_ 1 _,_ m( _fZ_ ) _, M_ ( _fZ_ )) _that does not depend on n, p_ 2 _, q and ψ_<sup>ˇ</sup> ( _·_ ) _that depends linearly on sA⋆. Here K_ 1 _denotes the upper bound of the first stage error shown in_ (16) _._ 

**Remark 2 (Rate of convergence)** It is worth pointing out similarities in the formulation of the calibration equation and a matrix completion problem. Note that the factor hyperplane corresponds to the low-rank component one seeks to recover in the latter problem in a noisy setting. Hence, the resulting similarity in the rate obtained in our setting to that established for the matrix completion problem (Candes and Plan, 2010), is a consequence of absence of the restricted isometry property (RIP) (see also Gunasekar et al., 2015). 

17 

Lin and Michailidis 

**Remark 3 (Sample size requirement)** To establish the finite-sample high probability error bound for the estimated transition matrices _A_<sup>�</sup> , the proposed estimation procedure requires the sample size to satisfy _n_ ≳ _q_ ; this condition is more stringent compared to the standard VAR estimation problem under sparsity, given by _n_ ≳ �log( _p_ 1 + _p_ 2). However, this is due to the fact that in the FAVAR formulation the _Ft_ block is latent and needs to be estimated from the data and hence comes with “measurement error”. The more restrictive sample size requirement reflects the latter fact and is embedded in the factor recovery step in the calibration equation – specifically, the concentration of Λmax( _S_ **E** ) that is necessary for providing adequate control over ∆ **F** . 

**Remark 4 (Generalization to VAR(** _d_ **))** As a straightforward generalization, for a VAR( _d_ ) _, d >_ 1 system _Zt_ = ( _Ft_<sup>_⊤, X_</sup> _t_<sup>_⊤_)</sup><sup>_⊤_,asimilarerrorboundholdsbyconsideringthe</sup> augmented process _Z_<sup>�</sup> _t_<sup>_⊤_:= (</sup><sup>_Zt, Zt−_1</sup><sup>_, . . . , Zt−d_+1)thatsatisfies</sup> 



In particular, with probability at least 



the following bound holds for the estimate of _A_<sup>�</sup> : 



However, note that although the error bound is still of the same form, the stronger temporal dependence yields a larger _C_<sup>�</sup> ( _K_ 1 _,_ m( _fZ_ �) _, M_ ( _fZ_ �) through the RSC curvature parameter; specifically, a smaller value of m( _fZ_ �). Its impact on the deviation bound will not manifest itself in terms of the order of the error, since it only affects the constants in front of lower order terms in the expression of choosing _λA_ . 

# **4. Implementation and Performance Evaluation** 

We first discuss implementation issues of the proposed problem formulation for the highdimensional FAVAR model. Specifically, the formulation requires imposing the compactness constraint for identifiability purposes and for obtaining the necessary statistical guarantees for the estimates of the model parameters. However, the value _φ_ in the compactness constraint is hard to calibrate in any real data set. Hence, in the implementation we relax this constraint and assess the performance of the algorithm. Due to its importance in constraining the size of the equivalence class _C_ ( _Q_ 2), we examine in Appendix D certain relatively extreme settings where the proposed relaxation fails to provide accurate estimates of the model parameters. 

_Implementation._ The following relaxation of (6) is used in practice: 



18 

Estimating High-Dimensional FAVAR Models 

**Algorithm 1:** Computational <u>procedure</u> for estimating _A_ <u>,</u> Γ and Λ. 

**Input:** Time series data _{xi}_<sup>_n_</sup> _i_ =1<sup>and</sup><sup>_{yi}n_</sup> _i_ =1<sup>,(</sup><sup>_λ_Γ</sup><sup>_, r_),and</sup><sup>_λA_.</sup> 

- **1 Stage I:** recover the latent factors by solving (18), through iterating between (1.1) and (1.2) until _|f_ (Θ<sup>(</sup><sup>_m_)</sup> _,_ Γ<sup>(</sup><sup>_m_)</sup> ) _− f_ (Θ<sup>(</sup><sup>_m−_1)</sup> _,_ Γ<sup>(</sup><sup>_m−_1)</sup> ) _| <_ tolerance: 



- **3** – (1.2) Update Γ<sup>�(</sup><sup>_m_)</sup> with the plug-in Θ<sup>�(</sup><sup>_m_)</sup> so that each row _j_ is obtained with Lasso regression (in parallel) and solves 



- � � � 

- **4** Stage I output: Θ and Γ; the estimated factor **F** and Λ via (7) under (IR); 

- **5 Stage II:** estimate the transition matrix by solving (8): update each row of _A_ (in parallel) by solving the Lasso problem: 



- 

- **6** Stage II output: _A_ . 



which leads to Algorithm 1. The implementation of Stage I requires the pair of tuning parameters ( _λ_ Γ _, r_ ) as input, and the choice of _r_ is particularly critical since it determines the effective size of the latent block. In our implementation, we select the optimal pair based on the Panel Information Criterion (PIC) proposed in Ando and Bai (2018), which searches for ( _λ_ Γ _, r_ ) over a lattice that minimizes 



where _σ_ �<sup>2</sup> = <u>1</u> 2<sup>Analogously,theimplementationofStageIIrequires</sup><sup>_λA_</sup> _nq_<sup>_|||_</sup><sup>**Y**</sup><sup>_−_Θ�</sup><sup>_−_</sup><sup>**X**Γ�</sup><sup>_⊤|||_</sup> F<sup>.</sup> as input, and we select _λA_ over a grid of values that minimizes the Bayesian Information Criterion (BIC): 



where RSS _i_ := _∥_ ( **X** _n_ ) _·i −_ **X** _n−_ 1 _A_<sup>�</sup><sup>_⊤_</sup> _i·_<sup>_∥_2istheresidualsumofsquareofthe</sup><sup>_i_thregression.</sup> Extensive numerical work shows that these two criteria select very satisfactory values for the tuning parameters, which in turn yield highly accurate estimates of the model parameters. 

_Simulation setup._ Throughout, we assume Σ<sup>_X_</sup> _w_<sup>,Σ</sup><sup>_F_</sup> _X_<sup>andΣ</sup><sup>_e_arealldiagonalmatrices,and</sup> the sample size is fixed at 200, unless otherwise specified. We first generate samples of _Ft ∈_ R<sup>_p_1</sup> and _Xt ∈_ R<sup>_p_2</sup> recursively according to the VAR( _d_ ) model in (1), and then the samples of _Yt ∈_ R<sup>_q_</sup> are generated according to the linear model given in (2). Specifically, (IR) is imposed on the true value of the parameter, hence Λ<sup>_⋆_</sup> that is used for generating 

19 

Lin and Michailidis 

_Yt_ always satisfies the restriction Λ = � I _p∗_ 1 �. Unless otherwise specified, all error terms are generated according to some mean-zero Gaussian distribution. 

For the calibration equation, the density level of the sparse coefficient matrix Γ _∈_ R<sup>_q×p_2</sup> is fixed at 5 _/p_ 2 for each regression; thus, each _Yt_ coordinate is affected by 5 series (coordinates) from the _Xt_ block on average. The bottom ( _q − p_ 1) _× p_ 1 block of the loading matrix Λ _∈_ R<sup>_q×p_1</sup> is dense. The magnitude of nonzero entries of Γ and that of entries of Λ may vary to capture different levels of signal contributions to _Yt_ , and we adjust the standard deviation of _et_ to maintain the desired level of the signal-to-noise ratio for _Yt_ (averaged across all coordinates). 

For the transition matrix _A_ of the VAR equation, the density for each of its component block _{Aij}i,j_ =1 _,_ 2 varies across settings, so as to capture different levels of the influence from the lagged value of the latent block _Ft_ on the observed _Xt_ . Note that to ensure stability of the VAR system, the spectral radius of _A_ , _ϱ_ ( _A_ ), needs to be smaller than 1. In particular, _A_ when� is smallera VAR(than _d_ ) ( _d >_ 1<sup>6</sup> , 1)wheresystemwe letis considered, _p_ = _p_ 1 + _p_ 2weandneed to ensure that the spectral radius of 



Table 1 lists the simulation settings and their parameter setup. 

Table 1: Parameter setup for different simulation settings for the VAR equation. 

||_q_|_p_1|_p_2||_sA_11|_sA_12|_sA_21|_sA_22|SNR(_Yt_)|
|---|---|---|---|---|---|---|---|---|---|
|A1|100|5|50|||3_/_(_p_1 <br>|+ _p_2)<br>||1.5|
|A2|200|10|100|||3_/_(_p_1|+ _p_2)||1.5|
|A3|200|5|100||3_/p_1|2_/p_2|2_/p_1|2_/p_2|1.5|
|A4|300|5|500||3_/p_1|2_/p_2|0_._8|2_/p_2|1.5|
|B1<br>(_d_= 2)|200|5|100|_A_<sup>(1) </sup>:<br>_A_<sup>(2) </sup>:<br>||3_/_(_p_1 <br>2_/_(_p_1|+_p_2)<br>+ _p_2)||2|
|||||_A_<sup>(1) </sup>:<br>|0_._5|3_/p_2|0_._5|3_/p_2||
|B2<br>(_d_= 4)|200|5|100|_A_<sup>(2) </sup>:<br>_A_<sup>(3) </sup>:<br>_A_<sup>(4) </sup>:<br>|0_._2|2_/p_2<br>2_/_(_p_1 <br>2_/_(_p_1|0_._25<br>+_p_2)<br>+ _p_2)|2_/p_2|2|
|||||_A_<sup>(1) </sup>:<br>|0_._5|2_/p_2|0_._5|2_/p_2||
|B3<br>(_d_= 4)|100|5|25|_A_<sup>(2) </sup>:<br>_A_<sup>(3) </sup>:<br>_A_<sup>(4) </sup>:|0_._2|1_._5_/p_2<br>1_/_(_p_1 <br>0_._8_/_(_p_1|0_._1<br>+_p_2)<br> + _p_2)|1_._5_/p_2|2|
|C1<br>C2<br>C3<br>C4|same a<br>same a<br>same a<br>same a|s setting <br>s setting <br>s setting <br>s setting|A1 with _t_<br> B1 with _t_<br> B2 with s<br> B2 with s|4 noise fo<br>8 noise fo<br>ub-expon<br>ub-expon|r the V<br>r the V<br>ential n<br>ential n|AR system<br>AR system<br>oise for the<br>oise for the|VAR s<br> VAR s|ystem<br>ystem an|d 500 observations|



Specifically, in settings A1 – A4, ( _Ft_<sup>_⊤, X_</sup> _t_<sup>_⊤_)</sup><sup>_⊤_jointlyfollowsaVAR(1)model.The(av-</sup> erage) signal-to-noise ratio for each regression of _Yt_ is 1.5. For settings A1 and A2, the 

> 6. In practice, this can be achieved by first generating _A_<sup>(1)</sup> _, . . . , A_<sup>(</sup><sup>_d_)</sup> , align them in _A_<sup>�</sup> initial and obtain the scale factor _ζ_ := _ϱ_ target _/ϱ_ ( _A_<sup>�</sup> initial), then scale _A_<sup>(</sup><sup>_i_)</sup> by _ζ_<sup>_i_</sup> . The validity of this procedure follows from simple algebraic manipulations. 

20 

Estimating High-Dimensional FAVAR Models 

transition matrix _A_ is uniformly sparse, with A2 corresponding to a larger system; for settings A3 and A4, we increase the density level (the proportion of nonzero entries) for the transition matrices that govern the effect of _Ft−_ 1 on _Ft_ and _Xt_ . In particular, for setting A4, we consider a large system with 500 coordinates in _Xt_ , and the factor effect is almost pervasive on these coordinates (through the lags), as the density level of _A_ 21 is set at 0.8. Settings B1, B2 and B3 consider settings with more lags ( _d_ = 2 and _d_ = 4, respectively), and to compensate for the higher level of correlation between _Ft_ and _Xt_ , we elevate the signal-to-noise for each regression of _Yt_ to 2. For B1, the transition matrices for both lags ( _A_<sup>(1)</sup> and _A_<sup>(2)</sup> ) have uniform sparsity patterns, with _A_<sup>(2)</sup> being slightly more sparse compared to _A_<sup>(1)</sup> ; for B2, the transition matrices for the first two lags have higher density in the component that governs the _Ft−i → Xt_ cross effect, and those for the last two lags have uniform sparsity. B3 has approximately the same scale as observed in real data, and due to a small _p_ 2, the system exhibits a higher sparsity level in general. In settings C1 – C4, the error terms of the VAR system are generated from distributions with tails heavier than a Gaussian (e.g. _t_ -distributions, squares of Gaussian which have sub-exponential tails), and the joint process ( _Ft_<sup>_′, Xt_)</sup><sup>_′_willbeheavy-tailedasaresultoftherecursivedatagenerating</sup> mechanism. 

_Performance evaluation._ We consider both the estimation and the forecasting performance of the proposed estimation procedure. The performance metrics used for estimation are sensitivity (SEN), specificity (SPC) and the relative error in Frobenius norm (Err) for the sparse components (transition matrices _A_ and the coefficient matrix Γ), defined as 



We also track the estimated size of the latent component (i.e., the rank constraint in (6), jointly with _λ_ Γ is selected by PIC), as well as the relative errors of Θ,<sup>�</sup> **F**<sup>�</sup> and Λ.<sup>�</sup> For forecasting, we focus on evaluating the _h_ -step-ahead predictions for the _Xt_ block. Specifically, for settings where the VAR system is 1-lag dependent (A1–A4, C1), we consider _h_ = 1; for settings where the VAR system has more lag dependencies (B1–B3, C2–C4), we consider _h_ = 1 _,_ 2. We use the same benchmark model as in Ba´nbura et al. (2010) which is based on a special case of the Minnesota prior distribution (Litterman, 1986), so that the for any generic time series _Xt ∈_ R<sup>_p_</sup> , each of its coordinates _j_ = 1 _, . . . , p_ follows a centered random walk: 



For each forecast _x_ � _T_ + _h_ , its performance is evaluated based on the following two measures: 



where rel-err measures the _ℓ_ 2 norm of the relative error of the forecast to the true value; whereas for rel-err-ratio, it measures the ratio between the relative error of the forecast and the above described benchmark. In particular, its numerator and denominator respectively capture the averaged relative error of all coordinates of the forecast _x_ � _T_ + _h_ and that of the benchmark _x_ � _T_ + _h_ that evolves according to (19), while the ratio measures how much the 

21 

Lin and Michailidis 

forecast based on the proposed FAVAR model outperforms ( _<_ 1) or under-performs ( _>_ 1) compared to the benchmark. 

All tabulated results are based on the average of 50 replications. Tables 2, 3 and 4, respectively, depict the performance of the estimates of the parameters in the calibration and the VAR equations, as well as the forecasting performance under the settings considered. Based on the results listed in Tables 2 and 3, we notice that in all settings, the parameters in the calibration equation Θ and<sup>�</sup> Γ are well estimated, while the rank slightly underestimated.<sup>�</sup> Further, the SEN and SPC measures of Γ<sup>�</sup> show excellent performance regarding support recovery. It is worth pointing out that the estimation accuracy of the parameters in the calibration equation strongly depends on the signal-to-noise ratio of _Yt_ . In particular, if the signal-to-noise ratio in A1-A4 is increased to 1.8, the rank is always correctly selected by PIC, and the estimation relative error of Θ<sup>�</sup> further decreases(results omitted for space considerations)<sup>7</sup> . Under the given IR, we decompose the estimated factor hyperplane into the factor block and its loadings. The results show that both quantities exhibit a higher relative error compared to that of the factor hyperplane. Of note, the loadings estimates exhibit a lot of variability as indicated by the high standard deviation in the Table. 

Regarding the estimates in the VAR equation, for settings A1, A2 and B1 that are characterized by an adequate degree of sparsity, the recovery of the skeleton of the transition matrices is very good. However, performance deteriorates if the latent factor becomes “more pervasive” (settings A3 and A4), which translates to the _A_ 21 block having lower sparsity. On the other hand, this does not have much impact on the recovery of the _A_ 22 sub-block, as for these two settings, SEN and SPC of _A_ 22 still remain at a high level. For settings with more lags, performance deteriorates (as expected) although SEN and SPC remain fairly satisfactory. On the other hand, the relative error of the transition matrices increases markedly. Nevertheless, the estimates of the first lag transition matrix is better than the remaining ones. Further, the results indicate that smaller size VAR systems (B3) exhibit better performance than larger ones. Finally, in terms of forecasting (results depicted in Table 4), the one-step-ahead forecasting value yields approximately 50% to 90% rel-err (compared to the truth), depending on the specific setting and the actual SNR, while it outperforms the forecast of the benchmark by around 40% (based on the rel-err-ratio measure). Of note, the 2-step-ahead forecasting value for settings with more lags outperforms the benchmark by an even wider margin with the rel-err-ratio decreasing to less than 0.3. 

Finally, the proposed methodology is robust in the presence of heavier than Gaussian tails in the VAR processes. Further, note that in setting C3 wherein the temporal dependence is strong and the error terms are generated according to a sub-exponential distribution, the performance of the estimated transition matrices deteriorates significantly, as expected from the theoretical results outlined in Appendix C. Nevertheless, with proper compensation in terms of sample size (setting C4), the performance improves markedly. 

> 7. This also comes up when comparing the relative error of Θ<sup>�</sup> in the A1-A4 settings to that in the B1-B2 ones, where the latter two have a higher SNR. 

22 

Estimating High-Dimensional FAVAR Models 

Table 2: Performance evaluation of estimated parameters in the calibration equation. 

||PIC-selected _r_|Err(<sup>�</sup>Θ)|Err(<sup>�</sup>**F**)|Err(<sup>�</sup>Λ)|SEN(<sup>�</sup>Γ)|SPC(<sup>�</sup>Γ)|Err(<sup>�</sup>Γ)|
|---|---|---|---|---|---|---|---|
|A1|4.80(.40)|0.32(.010)|0.56(.074)|0.67(.345)|0.99(.007)|0.98(.003)|0.45(.013)|
|A2|9.96(.19)|0.32(.008)|0.90(.065)|2.54(1.30)|0.99(.005)|0.98(.001)|0.52(.010)|
|A3|4.78(.54)|0.33(.048)|0.73(.103)|2.59(1.59)|0.99(.003)|0.99(.001)|0.57(.009)|
|A4|4.42(.49)|0.38(.040)|0.84(.100)|2.66(2.14)|0.97(.009)|0.99(.001)|0.59(.015)|
|B1|5(0)|0.23(.004)|0.41(.043)|0.54(.020)|1.00(.000)|0.97(.011)|0.27(.014)|
|B2|5(0)|0.26(.007)|0.38(.047)|0.42(.087)|1.00(.000)|0.99(.002)|0.37(.007)|
|B3|5(0)|0.25(.007)|0.34(.031)|0.34(.080)|1.00(.000)|0.99(.001)|0.32(.012)|
|C1|4.96(.20)|0.32(.019)|0.58(.075)|0.86(.564)|0.99 (.001)|0.96(.009)|0.47(.017)|
|C2|5(0)|0.23(.005)|0.43(.042)|0.54(.155)|1.00 (.000)|0.96(.008)|0.27(.010)|
|C3|5(0)|0.21(.006)|0.39(.040)|0.41(.123)|1.00 (.000)|0.97(.003)|0.27(.052)|
|C4|5(0)|0.20(.007)|0.27(.028)|0.25(.041)|1.00 (.000)|0.97(.011)|0.18(.012)|



Table 3: Performance evaluation of the estimated transition matrices in the VAR equation. 

||coef|SEN( <sup>�</sup><br>_A_)|SPC( <sup>�</sup><br>_A_)|Err( <sup>�</sup><br>_A_)|SEN( <sup>�</sup><br>_A_22)|SPC( <sup>�</sup><br>_A_22)|Err( <sup>�</sup><br>_A_22)|
|---|---|---|---|---|---|---|---|
|A1|_A_|0.99(.003)|0.95(.012)|0.35(.019)|0.99(.001)|0.96(.013)|0.31(.022)|
|A2|_A_|0.98(.008)|0.97(.004)|0.46(.018)|0.99(.001)|0.98(.003)|0.39(.017)|
|A3|_A_|0.86(.050)|0.98(.006)|0.73(.029)|0.93(.032)|0.98(.005)|0.65(.034)|
|A4|_A_|0.75(.046)|0.92(.002)|0.71(0.024)|0.99(.001)|0.92(.002)|0.60(.018)|
|B1|_A_<sup>(1)</sup><br>|0.99(.003)|0.98(.002)|0.47(.017)|0.99(.002)|0.98(.002)|0.46(.017)|
||_A_<sup>(2)</sup><br>|0.97(.010)|0.98(.002)|0.55(.017)|0.98(.011)|0.98(.003)|0.55(.018)|
|B2|_A_<sup>(1)</sup><br>|0.89(.017)|0.88(.003)|0.71(.014)|0.90(.017)|0.99(.003)|0.70(.014)|
||_A_<sup>(2)</sup><br>|0.75(.028)|0.88(.003)|0.89(.020)|0.77(0.032)|0.88(.003)|0.90(.021)|
||_A_<sup>(3)</sup><br>|0.84(.025)|0.88(.003)|0.85(.015)|0.85(.027)|0.88(.004)|0.84(.018)|
||_A_<sup>(4)</sup><br>|0.72(.022)|0.88(.003)|0.99(.017)|0.73(.025)|0.88(.003)|0.98(.017)|
|B3|_A_<sup>(1)</sup><br>|0.93(.034)|0.96(.010)|0.61(.043)|0.94(.035)|0.97(.009)|0.60(.045)|
||_A_<sup>(2)</sup><br>|0.77(.078)|0.96(.010)|0.74(.044)|0.78(.084)|0.97(.010)|0.74(.046)|
||_A_<sup>(3)</sup><br>|0.80(.098)|0.96(.012)|0.75(.052)|0.81(.102)|0.97(.010)|0.74(.056)|
||_A_<sup>(4)</sup>|0.74(.122)|0.97(.011)|0.78(.059)|0.72(.134)|0.97(.009)|0.79(.065)|
|C1|_A_<br>|0.99(.007)|0.95(.012)|0.42(.024)|0.99(.002)|0.96(.011)|0.38(.024)|
|C2|_A_<sup>(1)</sup><br>|0.99(.004)|0.98(.002)|0.46(.013)|0.99(.003)|0.98(.002)|0.45(.015)|
||_A_<sup>(2)</sup><br>|0.98(.008)|0.97(.003)|0.54(.018)|0.98(.009)|0.98(.003)|0.54(.019)|
|C3|_A_<sup>(1)</sup><br>|0.93(.013)|0.42(.005)|1.54(.024)|0.93(.013)|0.42(.006)|1.61(.027)|
||_A_<sup>(2)</sup><br>|0.86(.019)|0.44(.006)|2.11(.029)|0.86(.023)|0.44(.006)|2.30(.032)|
||_A_<sup>(3)</sup>|0.88(.023)|0.44(.006)|2.06(.028)|0.89(.023)|0.44(.005)|2.07(.028)|
||_A_<sup>(4)</sup>|0.82(.023)|0.44(.006)|2.51(.043)|0.83(.025)|0.44(.006)|2.51(.041)|
|C4|_A_<sup>(1)</sup>|0.89(.016)|0.96(.002)|0.67(.013)|0.89(.016)|0.96(.002)|0.65(.014)|
||_A_<sup>(2)</sup><br>|0.73(.025)|0.96(.006)|0.78(.029)|0.74(.026)|0.96(.002)|0.79(.011)|
||_A_<sup>(3)</sup><br>|0.82(.027)|0.96(.002)|0.74(.015)|0.82(.028)|0.96(.002)|0.74(.017)|
||_A_<sup>(4)</sup>|0.60(.031)|0.96(.002)|0.87(.014)|0.60(.033)|0.96(.002)|0.87(.015)|



Table 4: Performance evaluation of forecasting. 

||_h_|= 1|_h_|= 2|
|---|---|---|---|---|
||rel-err|rel-err-ratio|rel-err|rel-err-ratio|
|A1|0.53(.117)|0.38(.065)|-|-|
|A2|0.60(.075)|0.38(.046)|-|-|
|A3|0.80(.075)|0.45(.064)|-|-|
|A4|0.56(.109)|0.40(.055)|-|-|
|B1|0.62(.060)|0.35(.171)|0.66(.127)|0.24(.071)|
|B2|0.89(.091)|0.42(.217)|0.94(.173)|0.29(.118)|
|B3|0.81(.094)|0.32(.129)|0.90(.402)|0.26(.174)|
|C1|0.59(.176)|0.50(.118)|-|-|
|C2|0.59(.121)|0.41(.350)|0.61(.270)|0.26(.089)|
|C3|1.25(.305)|0.19(.081)|1.26(.396)|0.15(.059)|
|C4|0.52(.073)|0.12(.071)|0.51(.168)|0.07(.034)|



23 

Lin and Michailidis 

# **5. Application to Commodity Price Interlinkages** 

Interlinkages between commodity prices represent an active research area in economics and have been a source of concern for policymakers. Commodity prices, unlike stocks and bonds, are determined more strongly by global demand and supply considerations. Nevertheless, other factors are also at play as outlined next. The key ones are: (i) the state of the global macro-economy and the state of the business cycle that manifest themselves as direct demand for commodities; (ii) monetary policy, specifically, interest rates that impact the opportunity cost for holding inventories, as well as having an impact on investment and hence production capacity that subsequently contribute to changes in supply and demand in the market; and (iii) the relative performance of other asset classes through portfolio allocation (see Frankel, 2006, 2014, and references therein). We employ the FAVAR model and the proposed estimation method to investigate interlinkages amongst major commodity prices. The _Xt_ block corresponds to the set of commodity prices of interest, while the _Yt_ block contains representative indicators for the global economic environment. We extract the factors _Ft_ based on the calibration equation and then consider the augmented VAR system of ( _Ft, Xt_ ), so that the estimated interlinkages amongst commodity prices are based on a larger information set that takes into account broader economic activities. 

_Data._ The commodity price data ( _Xt_ ) are retrieved from the International Monetary Fund, comprising of 16 commodity prices in the following categories: Metal, Energy (oil) and Agricultural. The set of economic indicators ( _Yt_ ) contain core macroeconomic variables and stock market composite indices from major economic entities including China, EU, Japan, UK and US, with a total number of 54 indicators. Specifically, the macroeconomic variables primarily account for: Output & Income (e.g. industrial production index), Labor Market (unemployment), Money & Credit (e.g. M2), Interest & Exchange Rate (e.g. Fed Funds Rate and the effective exchange rate), and Price Index (e.g. CPI). For variables that reflect interest rates, we use both the short-term interest rate such as 6-month LIBOR, and the 10-year T-bond yields from the secondary market. Further, to ensure stationarity of the time series, we take the difference of the logarithm for _Xt_ ; for _Yt_ , we apply the same transformation as proposed in Stock and Watson (2002). A complete list of the commodity prices and economic indicators used in this study is provided in Appendix E. For all time series considered, we use monthly data spanning the January 2001 to December 2016 period. Further, based on previous empirical findings in the literature related to the global financial crisis of 2008 (Stock and Watson, 2017), we break the analysis into the following three subperiods (Stock and Watson, 2017): pre-crisis (2001–2006), crisis (2007–2010) and post-crisis (2011–2016), each having sample size (available time points) 72, 48, and 72, respectively<sup>8</sup> . 

We apply the same estimation procedure for each of the above three sub-periods. Starting with the calibration equation, we estimate the factor hyperplane Θ and the sparse regression coefficient matrix Γ, then extract the factors based on the estimated factor hy- 

> 8. For each individual time series, we test for its normality using data spanning the pre-crisis, crisis, and post-crisis periods, respectively. Based on the Shapiro-Wilk test, the null hypothesis of normality is not rejected for selected time series (e.g., ALUMINUM) and rejected for others (e.g., OIL). However, when testing for multivariate normality of the joint distribution of all time series resp. across the three periods, we fail to reject the null hypothesis. The latter result may be due to inadequate power of the test given the relatively small sample size. 

24 

Estimating High-Dimensional FAVAR Models 

perplane under the (IR) condition. For each of the three sub-periods, 4, 3, and 3 factors are respectively identified based on the PIC criterion, with the key variable loadings (collapsed into categories) on each extracted factor listed in Table 5, after adjusting for Γ _Xt_ . Based 

Table 5: Composition of the factors identified for three sub-periods. +, _−_ and _∗_ respectively stand for positive (all economic indicators in that category have a positive sign in Λ), negative and mixed (sign) contribution. 

|||pre-c|risis|||crisis||post-cri|sis|
|---|---|---|---|---|---|---|---|---|---|
||F1|F2|F3|F4|F1|F2|F3|F1<br>F2|F3|
|bond return|_−_||+|+|_−_|+|||_−_|
|economic output|+||||||+|+||
|equity return|+||||_−_|_−_||_−_|+|
|interest/exchange rate|||_∗_|||||_∗_||
|labor||+|||_−_||_−_|||
|money & credit|||+||+|||+||
|price index||+|||||+||_−_|
|trade||_−_||||_∗_||_∗_||



on the composition of the factors, we note that the factors summarize both the macroeconomic environment and also capture information from the secondary market (bond & equity return), as suggested by economic analysis of potential contributors to commodity price movements (Frankel, 2006, 2014). Hence, the obtained factors summarize the necessary information to include in the VAR system that examines commodity price interlinkages over time. Further, across all three periods considered, Economic Output and Money & Credit indicators contribute positively to the factor composition. In particular, the positive contribution from the M2 measure of money supply for the US during the crisis period and that from the Fed Funds Rate post crisis are pronounced; hence, the estimated factors strongly reflect the effect of the Quantitative Easing policy adopted by the US central bank. The contribution of the other categories are mixed, with that from bond returns being noteworthy due to their role as a proxy for long-term interest rates, which impact both the cost of investment in increasing production capacity and on holding inventories, as well as on the composition of asset portfolios across a range of investment possibilities (stocks, bonds, commodities, etc.). 

Next, using these estimated factors, we fit a sparse VAR(2) model to the augmented ( _F_<sup>�</sup> _t_<sup>_⊤, X_</sup> _t_<sup>_⊤_)</sup><sup>_⊤_system.TheestimatedtransitionmatricesaredepictedinFigures1to3as</sup> networks<sup>9</sup> . It is apparent that the factors play an important role, both as emitters and receivers. The effects from the first lag are generally stronger to that from the second one. In particular, focusing on the first lag, the dominant nodes in the system have shifted over time from (OIL, SOYBEANS, ZINC) pre crisis to (SUGAR, WHEAT, COPPER) during the crisis, then to (OIL, SOYBEANS, RICE) post crisis. Based on node weighted degree, the role of OIL is dominant in both pre- and post-crisis periods, but is much weaker during the crisis. 

> 9. In all three figures, the left panel corresponds to _A_<sup>�(1)</sup> and the right panel corresponds to _A_<sup>�(2)</sup> . Node sizes are proportional to node weighted degrees. Positive edges are in red and negative edges are in blue. Edges with higher saturation have larger magnitudes. 

25 

Lin and Michailidis 

Figure 1: Estimated transition matrices for Pre-crisis period. 



<!-- Start of picture text -->
RICE ● COCOA ●<br>COPPER<br>●<br>COPPER ● RUBBER ●<br>● F3 ● ZINC ● F1LEAD ● ● F4 ● OIL TINSOYBEANS ● MAIZE ● WHEAT ● COTTON ● WHEAT ● COFFEERICE ●● RUBBER ● F3 ● NICKEL ● ● OIL<br>ALUMINIUM ●● F2 SUGAR ● NICKEL ● COTTON ● ● SOYBEANS ● ALUMINIUM ● ● F4 ● F2 ● LEAD ● TIN MAIZE ●<br>F1<br>COCOA ● ● SUGAR ●<br>COFFEE ● ZINC ●<br>Figure 2: Estimated transition matrices for the Crisis period.<br>SOYBEANS ● RICE ● COFFEE SUGAR ●<br>●<br>● TIN COCOA ● WHEAT ● MAIZE ● ● OIL NICKEL ● COCOA ● COFFEE ● ZINC ●<br>ALUMINIUM ● ● F2 WHEAT ● ● F3<br>SUGAR ● LEAD ● COPPER ● COTTON ● RUBBER ● ● F1 NICKEL ● RUBBER ● ● RICE ● F1 MAIZE ● LEAD ●<br>ZINC ● ● F2 ● OIL<br>SOYBEANS ● ● TIN ALUMINIUM ●<br>F3 COTTON ● COPPER ●<br>●<br>Figure 3: Estimated transition matrices for Post-crisis period<br>SOYBEANS ● WHEAT ● NICKEL ● COFFEE ● ZINC ●<br>COTTON ● ● RICE LEAD ● ● OIL ALUMINIUM ● RICE ●<br>● TIN COPPER ● RUBBER ● LEAD ● WHEAT ●<br>ALUMINIUM ● NICKEL ● ZINC ● ● OIL F1 ● TIN<br>● F2 COFFEE ● COCOA ● ● F1 ● F3 SUGAR ● ● COTTON ● F2<br>●<br>RUBBER<br>F3 ●<br>SUGAR ●<br>● MAIZE<br>●<br>SOYBEANS COCOA ●<br>●<br>MAIZE ● COPPER ●<br><!-- End of picture text -->

Another key feature of the interlinkage networks is their increased connectivity during the crisis period, vis-a-vis the pre- and post-crisis periods. The same empirical finding has been noted for stock returns (see Lin and Michailidis, 2017, and references therein). Before the global financial crisis of 2008, commodity prices were fast rising primarily due 

26 

Estimating High-Dimensional FAVAR Models 

to increased demand from China. Specifically, as Chinese industrial production quadrupled between 2001 and 2011, its consumption of industrial metals (Copper, Zinc, Aluminum, Lead) increased by 330%, while its oil consumption by 98%. This strong demand shock led to a sharp rise in these commodity prices, particularly accentuated beginning in 2006 (the onset of the crisis period considered in our analysis), briefly disrupted with a quick plunge of commodity prices in 2008 and their subsequent recovery in the ensuing period until late 2010, when demand from China subsided, which coupled with weak demand from the EU, Japan and the US in the aftermath of the crisis created an oversupply that put downward pressure on prices. These events induce strong inter-temporal and crosstemporal correlations amongst commodity prices, and hence are reflected in their estimated interlinkage network. 

# **6. Discussion** 

This paper considered the estimation of FAVAR model under the high-dimensional scaling. It introduced an identifiability constraint (IR+Compactness) that is suitable for highdimensional settings, and when such a constraint is incorporated in the optimization problem based upon the calibration equation, the global optimizer corresponds to model parameter estimates with bounded statistical errors. This development also allows for accurate estimation of the transition matrices of the VAR system, despite the plug-in factor block contains error due to the fact that it is an estimated quantity. Extensive numerical work illustrates the overall good performance of the proposed empirical implementation procedure, but also illustrates that the imposed constraint is not particularly stringent, especially in settings where the coefficient matrix Γ of the observed predictor variables in the calibration equation exhibits sufficient level of sparsity. 

The key advantage of the FAVAR model is that it can leverage information from a large number of variables, while modeling the cross-temporal dependencies of a smaller number of them that are of primary interest to the analyst. 

Recall that the nature of the FAVAR model results in estimating the transition matrix of a VAR system with one block of the observations (factors) being an estimated quantity, rather than conducting the estimation based on observed samples. Similar in flavor problems have been examined in the high-dimensional iid setting (e.g. Loh and Wainwright, 2012), as well as low dimensional time series settings; for example, Chanda et al. (1996) examine parameter estimation of a univariate autoregressive process with error-in-variables and in more recent work Komunjer and Ng (2014) investigate parameter identification of VAR-X and dynamic panel VAR models subject to measurement errors. 

# **Acknowledgments** 

The authors would like to thank two anonymous referees for constructive comments and suggestions. The work of GM was supported in part by NSF grants IIS 1632730, DMS 1821220 and DMS 1830175. 

27 

Lin and Michailidis 

# **Appendix A. Proofs for Theorems and Propositions** 

This section is divided into two parts. In the first part, we provide proofs for the proposition and theorem related to Stage I estimates, i.e., Θ and<sup>�</sup> Γ.<sup>�</sup> In the second part, we give proofs for the statements related to Stage II estimates, namely _A_<sup>�</sup> , with an emphasis on how to obtain the final high probability error bound through properly conditioning on related events. 

**Part 1.** Proofs for the Θ<sup>�</sup> and Γ<sup>�</sup> estimates. 

_Proof of Proposition 1._ Using the optimality of (Γ<sup>�</sup> _,_ Θ)<sup>�</sup> and the feasibility of (Γ<sup>_⋆_</sup> _,_ Θ<sup>_⋆_</sup> ), the following _basic inequality_ holds: 



which after rearranging terms gives 



The remainder of the proof proceeds in three steps: in Step (i), we obtain a lower bound for the left-hand-side (LHS) leveraging the RSC condition; in Step (ii), an upper bound for the right-hand-side (RHS) based on the designated choice of _λ_ Γ is derived; in Step (iii), the two sides are aligned to yield the desired error bound after rearranging terms. 

To complete the proof, we first define a few quantities that are associated with the support set of Γ and its complement: 



where _S_ Γ _⋆_ is the support of Γ<sup>_⋆_</sup> . Further, define ∆S and ∆S _c_ as 



and note that they satisfy 



and 



Step (i). Since **X** satisfies the RSC condition, the first term on the LHS of (21) is lower bounded by 



28 

Estimating High-Dimensional FAVAR Models 

To get a lower bound for (23), consider an upper bound for _||_ ∆Γ _||_ 1 with the aid of (20). Specifically, for the first two terms in the RHS of (20), by H¨older’s inequality, the following inequalities hold for the inner products: 



for the last term, since 



the following inequality holds: 



Using the non-negativity of the RHS in (20), by choosing 



the following inequality holds: 



Since ∆Θ = Θ<sup>�</sup> _−_ Θ<sup>_⋆_</sup> has rank at most _p_ 1 + _r_ , _|||_ ∆Θ _/_<sup>_√_</sup> _<u>n|||∗</u> ≤_<sup>_√_</sup> _<u>p</u>_ 1 <u>+</u> _<u>r|||</u>_ ∆Θ _/_<sup>_√_</sup> _<u>n|||</u>_ F. It follows that 



where the second line is obtained by adding<sup>_<u>λ</u>_</sup> 2<sup><u>Γ</u></sup><sup>_∥_∆Γ</sup><sup>_|_S</sup><sup>_∥_1on both sides, and the last inequality</sup> uses (22). Further, by the Cauchy-Schwartz inequality, we have 



that is, 



Combine (23) and (27), a lower bound for the LHS of (21) is given by 



29 

Lin and Michailidis 

Step (ii). For the first term in the RHS of (21), using the duality of _ℓ_ 1- _ℓ∞_ dual norm pair, the following inequality holds: 



Using the fact that both Θ<sup>_⋆_</sup> and Θ<sup>�</sup> are feasible and satisfy the box constraint _∥_ Θ _∥∞ ≤_ _<u>φ</u>_<sup>itfollowsthat</sup> _κ_ ( _R_<sup>_∗_</sup> ) _|||_ **X** _/_<sup>_~~√~~_</sup> _<u>n|||</u>_ op<sup>,</sup> 



2 _<u>φ</u>_ Consequently, (29) is upper bounded by _κ_ ( _R_<sup>_<u>∗</u>_</sup> )<sup>_· ∥_∆Γ</sup><sup>_∥_1.Byadditionallyrequiring</sup><sup>_λ_Γto</sup> satisfy _λ_ Γ _≥_ 4 _φ/κ_ ( _R_<sup>_∗_</sup> ) _,_ 

and combining (24), (25) and (26), the following upper bound holds for the RHS of (21): 



Step (iii). Combine (28) and (30), by rearranging terms and requiring _τ_ **X** to satisfy _τ_ **X** ( _p_ 1 + _r_ + 4 _s_ Γ _⋆_ ) _<_ min _{α_ RSC<sup>**X**</sup><sup>_,_1</sup><sup>_}/_16,thefollowinginequalityholds:</sup> 



which gives 



_Proof sketch for Theorem 1._ First we note that the requirement on the tuning parameter _λ_ Γ determines the leading term in the ultimate high probability error bound. By Lemma 4, to have adequate concentration for the leading eigenvalue Λmax( _S_ **E** ) of the sample covariance matrices, the requirement imposed on the sample size makes ~~�~~ log( _p_ 2 _q_ ) _/n_ a lower order term relative to Λmax<sup>1</sup><sup>_/_2(Σ</sup> _e_<sup>),withthelatterbeingan</sup><sup>_O_(1)term.Consequently,thechoiceof</sup> the tuning parameter effectively becomes 



30 

Estimating High-Dimensional FAVAR Models 

The conclusion readily follows as a result of Proposition 1. 

**Part 2.** This part contains the proofs for the results related to _A_<sup>�</sup> . 

_Proof sketch for Proposition 2._ The result follows along the lines of Basu and Michailidis (2015, Proposition 4.1). In particular, in Basu and Michailidis (2015), the authors consider estimation of _A_ based on the directly observed samples of the _Xt_ process, with the restricted eigenvalue (RE) condition imposed on the corresponding Hessian matrix and the tuning parameter selected in accordance to the deviation bound defined in Definition 2. On the other hand, in the current setting, estimation of the transition matrix is based on quantities that are surrogates for the true sample quantities. Consequently, as long as the required conditions are imposed on their counterparts associated with these surrogate quantities, the conclusion directly follows. 

Finally, we would like to remark that the RSC condition used is in essence identical to the RE condition required in Basu and Michailidis (2015) in the setting under consideration. 

_Proof of Theorem 2._ First, we note that under (IR), by Theorem 1, there exists some constant _K_ 1 that is independent of _n, p_ 1 _, p_ 2 and _q_ such that the following event holds with probability at least P1 := 1 _− c_ 1 exp( _−c_ 2 log( _p_ 2 _q_ )): 



Conditional on _E_ 1, by Proposition 2, Lemmas 6 and 7, with high probability, the following event holds: 



for some function _ϕ_ ( _·_ ) that not only depends on sample size and dimensions, but also on _K_ 1, provided that the “conditional” RSC condition is satisfied. What are left to be examined are: (i) what does _E_ 1 imply in terms of the RSC condition being satisfied _unconditionally_ ; and (ii) what does _E_ 1 imply in terms of the bound in _E_ 2, 

Towards this end, for (i), we note that since 



then as long as _CZ_ in condition C3 satisfies _CZ ≥ c_ 0 _K_ 1 with the specified _c_ 0 _≥_ 6 _√_ 165 _π_ , with probability at least _P_ 1 _P_ 2 _,_ RSC where we define P2 _,_ RSC := 1 _− c_<sup>_′_</sup> 1<sup>exp(</sup><sup>_−c′_</sup> 2<sup>_n_), by Lemma 6</sup> the required RSC condition is guaranteed to be satisfied with a positive curvature. For (ii), with the aid of Lemma 7, with probability at least P1P2 _,_ DB where we define P2 _,_ DB := 1 _− c_<sup>_′_</sup> 1<sup>exp(</sup><sup>_−c′_</sup> 2<sup>log(</sup><sup>_p_1 +</sup><sup>_p_2)),thefollowingboundholdsforthedeviationbound</sup><sup>_C_(</sup><sup>_n, p_1</sup><sup>_, p_2)</sup> _unconditionally_ :<sup>10</sup> 



10. Note that it can be shown that _|||εn|||_<sup>2</sup> F<sup>=</sup><sup>_O_(</sup><sup>_|||_∆</sup><sup>**F**</sup><sup>_|||_2</sup> F<sup>)</sup> 

31 

Lin and Michailidis 

where the constants _{Ci}_ have already absorbed the upper error bound _K_ 1 of the Stage I estimates, compared with the original expression in Proposition 2. With the required sample size, the constant becomes the leading term, so that there exists some constant _K_ 2 such that _unconditionally_ : 



Combine (i) and (ii), and with probability at least min _{_ P1P2 _,_ RSC _,_ P1P2 _,_ DB _}_ , the bound in Theorem 2 holds. 

# **Appendix B. Proof for Lemmas** 

In this section, we provide proofs for the lemmas in Section 3.2. 

_Proof of Lemma 1._ Note that 



Multiply the left inverse of **F**<sup>�</sup> which gives 



Since for some generic matrix _M_ , we have _|||M_<sup>_−_1</sup> _|||_ F _≥_ ( _|||M |||_ F)<sup>_−_1</sup> , an application of the triangle inequality gives 



where _S_ � :=<sup><u>1</u>and the numerator and the denominator of</sup> _<u>|||</u>_ **F**<sup>�</sup> _<u>|||</u>_ <u>F</u> **F** _n_<sup>**F**�</sup><sup>_⊤_</sup><sup>**F**�,</sup> _|||_ **F**<sup>�</sup><sup>_⊤_</sup> **F**<sup>�</sup> _|||_ F<sup>are respectively by</sup> 



2 Further, note that _|||_ **F**<sup>�</sup> _/_<sup>_√_</sup> _<u>n|||</u>_ op<sup>=Λmax(</sup><sup>_S_</sup> **F**<sup>�)=</sup><sup>_|||S_</sup> **F**<sup>�</sup><sup>_|||_</sup> op<sup>.Whatremainsistoobtainalower</sup> bound for Λmax<sup>1</sup><sup>_/_2</sup> � _S_ **F** � � = _|||_ ( **F** + ∆ **F** ) _/_<sup>_√_</sup> _n|||_ op _._ 

One such bound is given by 



32 

Estimating High-Dimensional FAVAR Models 

which leads to the following bound for _|||_ ∆Λ _|||_ F, provided that the RHS is positive: 



_Proof of Lemma 2._ First, suppose we have 



then, for all ∆ _∈_ R<sup>_p×p_</sup> , and letting ∆ _j_ denote its _j_ th column, the RSC condition automatically holds since 



Therefore, it suffices to verify that (31) holds. In Basu and Michailidis (2015, Proposition 4.2), the authors prove a similar result under the assumption that _Xt_ is a VAR( _d_ ) process. Here, we adopt the same proof strategy and state the result for a _more general process Xt_ . Specifically, by Basu and Michailidis (2015, Proposition 2.4(a)), _∀v ∈_ R<sup>_p_</sup> _, ∥v∥≤_ 1 and _η >_ 0, 



Applying the discretization in Basu and Michailidis (2015, Lemma F.2) and taking the union bound, define K(2 _s_ ) := _{v ∈_ R<sup>_p_</sup> _, ∥v∥≤_ 1 _, ∥v∥_ 0 _≤_ 2 _k}_ , and the following inequality holds: 



With the specified _γ_ = 54 _M_ ( _gX_ ) _/_ m( _gX_ ), set _η_ = _γ_<sup>_−_1</sup> , then apply results from Loh and Wainwright (2012, Lemma 12) with Γ = _S_ **X** _−_ Σ _X_ (0) and _δ_ = _π_ m( _gX_ ) _/_ 27, so that the following holds 



with probability at least 1 _−_ 2 exp � _−cn_ min _{γ_<sup>_−_2</sup> _,_ 1 _}_ +2 _k_ log _p_ � and note that min _{γ_<sup>_−_2</sup> _,_ 1 _}_ = _γ_<sup>_−_2</sup> since _γ >_ 1. Finally, let _k_ = min _{cnγ_<sup>_−_2</sup> _/_ ( _c_<sup>_′_</sup> log _p_ ) _,_ 1 _}_ for some _c_<sup>_′_</sup> _>_ 2, and conclude that with probability at least 1 _− c_ 1 exp( _−c_ 2 _n_ ), the inequality in (31) holds with 



and so does the RSC condition. 

33 

Lin and Michailidis 

_Proof of Lemma 3._ We note that 



where _ei_ is the _p_ -dimensional standard basis with its _i_ -th entry being 1. Applying Basu and Michailidis (2015, Proposition 2.4(b)), for an arbitrary pair of ( _i, j_ ), the following inequality holds: 



and note that _et_ is a pure noise term that is assumed to be independent of _Xt_ ; hence, there is no cross-dependence term to consider. Take the union bound over all 1 _≤ i ≤ p_ 2 _,_ 1 _≤ j ≤ q_ , and the following bound holds: 



Set _η_ = _c_<sup>_′_</sup><sup>~~�~~</sup> log _p/n_ for _c_<sup>_′_</sup> _>_ (1 _/c_ ) and with the choice of _n_ ≳ log( _p_ 2 _q_ ), min _{η_<sup>2</sup> _, η}_ = _η_<sup>2</sup> , then with probability at least 1 _− c_ 1 exp( _−c_ 2 log _p_ 2 _q_ ), there exists some _c_ 0 such that the following bound holds: 



_Proof of Lemma 4._ For **E** whose rows are iid realizations of a sub-Gaussian random vector _et_ , by Wainwright (2009, Lemma 9), the following bound holds: 



_<u>q q</u>_ 2 where _δ_ ( _n, q, η_ ) := 2�<sup>~~�~~</sup> _n_<sup>+</sup><sup>_η_</sup> � + �<sup>~~�~~</sup> _n_<sup>+</sup><sup>_η_</sup> � . In particular, by triangle inequality, with probability at least 1 _−_ 2 exp( _−nη_<sup>2</sup> _/_ 2), 



So for _n_ ≳ _q_ , by setting _η_ = 1, which yields _δ_ ( _n, q, η_ ) _≤_ 8 so that with probability at least 1 _−_ 2 exp( _−n/_ 2), the following bound holds: 



34 

Estimating High-Dimensional FAVAR Models 

_Proof of Lemma 5._ To prove this lemma, we use a similar strategy as in the proof of Negahban and Wainwright (2011, Lemma 3) while taking into consideration the temporal dependence present in the rows of **X** . In the remainder of the proof, we use _p_ (instead of _p_ 2) to denote generically the dimension of the process. 

Let _S_<sup>_p_</sup> = _{u ∈_ R<sup>_p_</sup> _|∥u∥_ = 1 _}_ denote the _p_ -dimensional unit sphere. Then, Λmax( _S_ **X** ) is the operator norm of _S_ **X** , which has the following variational representation form: 



For a positive scalar _s_ , define 



the goal is to establish an upper bound for Ψ(1) _/n_ . Let _A_ = _{u_<sup>1</sup> _, · · · , u_<sup>_A_</sup> _}_ denote the 1 _/_ 4 covering of _S_<sup>_p_</sup> . Negahban and Wainwright (2011) established that 



further, according to Anderson (2011), there exists a 1 _/_ 4 covering of _S_<sup>_p_</sup> with at most _|A| ≤_ 8<sup>_p_</sup> elements. Consequently, 



What remains to be bounded is<sup><u>1</u>By Basu and Michailidis</sup> _n_<sup>_u′_</sup><sup>**X**</sup><sup>_′_</sup><sup>**X**</sup><sup>_u_, for an arbitrary</sup><sup>_u ∈Sp_.</sup> (2015, Proposition 2.4(b)), we have 

and thus 



Therefore, it follows that 



With the specified choice of sample size _n_ , the probability vanishes by choosing _η_ = _c_<sup>_′_</sup> 0<sup>for</sup> constant _c_<sup>_′_</sup> 0<sup>sufficientlylarge.Finally,byProposition2.3inBasuandMichailidis(2015),</sup> _|||_ Σ _X_ (0) _|||_ op _≤_ 2 _πM_ ( _fX_ ), and thus the conclusion in Lemma 5 holds. 

35 

Lin and Michailidis 

_Proof of Lemma 6._ It suffices to show that the following inequality holds with high probability for some curvature _α_ RSC<sup>**Z**�</sup><sup>_>_0andtolerance</sup><sup>_τ_</sup><sup>**Z**,wherewedefine</sup><sup>_S_�</sup><sup>**Z**:=</sup> _n_<sup><u>1</u></sup><sup>**Z**�</sup> _n_<sup>_⊤_</sup> _−_ 1<sup>**Z**�</sup><sup>_n−_1:</sup> 



Define _S_ **Z** := _n_<sup><u>1</u></sup><sup>**Z**</sup> _n_<sup>_⊤_</sup> _−_ 1<sup>**Z**</sup><sup>_n−_1,then</sup><sup>_S_�</sup><sup>**Z**canbewrittenas</sup> 



First, notice that the last term satisfies the following natural lower bound _deterministically_ , since ∆ **F** is assumed non-random and ∆ **Z** = [∆ **F** _, O_ ]: 



which however, does not contribute to the “positive” part of curvature. For the first two terms, we adopt the following strategy, using Lemma 12 in Loh and Wainwright (2012) as an intermediate step. Specifically, Loh and Wainwright (2012, Lemma 12) proves that for any fixed generic matrix Γ _∈_ R<sup>_p×p_</sup> that satisfies _|θ_<sup>_⊤_</sup> Γ _θ| ≤ δ_ for any _θ ∈_ K(2 _s_ )<sup>11</sup> , the following bound holds 



Then, based on (33), consider Γ = Γ<sup>�</sup> _−_ Σ then rearrange terms, so that _θ_<sup>_⊤_</sup> Γ<sup>�</sup> _θ ≥ θ_<sup>_⊤_</sup> Σ _θ −_ <u>272</u> _<u>δ</u>_ � _∥θ∥_<sup>2</sup> 2<sup>+</sup> 2<sup><u>1</u></sup><sup>_∥θ∥_</sup> 1<sup>2</sup> �. The RE condition follows by setting _δ_ to be some quantity related to Λmin(Σ). 

In light of this, for the first two terms in (32), let 



denote their sum, in order to obtain an upper bound for �� _θ⊤_ �Ψ _−_ Σ _Z_ (0)� _θ_ ��, so that Lemma 12 in Loh and Wainwright (2012) can be applied. To this end, since 



we consider getting upper bounds for each of the two terms: 



For (i), we follow the derivation in Basu and Michailidis (2015, Proposition 2.4(a)), that is, for all _∥θ∥≤_ 1, 



11. K(2 _s_ ) := _{θ_ : _∥θ∥_ 0 = 2 _s}_ is the set of 2 _s_ -sparse vectors. 

36 

Estimating High-Dimensional FAVAR Models 

and further with probability at least 



the following bound holds: 



For (ii), the two terms are identical, with either one given by 



To obtain its upper bound, consider the following inequality, based on which we bound the two terms in the product separately: 



For the first term in (35), since rows of **Z** _n−_ 1 are time series realizations from (5), then if we let _ξ_ := **Z** _n−_ 1 _θ_ , _ξ ∼N_ (0 _n×_ 1 _, Qn×n_ ) is Gaussian with _Qst_ = _θ_<sup>_′_</sup> Σ _Z_ ( _t − s_ ) _θ_ . To get its upper bound, we bound its square, and use again (34), that is, 



For the second term _∥_ ∆ **Z** _n−_ 1 _θ/_<sup>_√_</sup> _<u>n∥</u>_ , this is non-random, and for all _∥θ∥≤_ 1, _∥_ ∆ **Z** _n−_ 1 _θ/_<sup>_√_</sup> _<u>n∥</u> ≤_ Λ<sup>1</sup> max<sup>_/_2</sup> � _S_ ∆ **Z** _n−_ 1 � = Λ<sup>1</sup> max<sup>_/_2</sup> � _S_ ∆ **F** _n−_ 1 �. Therefore, the following bound holds for (35): 





Now applying Loh and Wainwright (2012, Lemma 12) to Γ = Ψ _−_ Σ _Z_ (0), and _δ_ being the RHS of (37), then the following bound holds: 





37 

Lin and Michailidis 

Since we have required that m( _fZ_ ) _/M_<sup>1</sup><sup>_/_2</sup> ( _fZ_ ) _> c_ 0 _·_ Λ<sup>1</sup> max<sup>_/_2(</sup><sup>_S_</sup> ∆ **F** _n−_ 1<sup>)with</sup><sup>_c_</sup> 0<sup>_≥_6</sup> _√_ 165 _π_ , 2 _π_ m( _fZ_ ) _−_ 27 _δ >_ 0. Therefore, the RSC condition is satisfied with curvature 



and tolerance 27 _δ/_ (2 _s_ ), with probability at least 1 _−_ 2 exp _− cnω_<sup>_−_2</sup> + 2 _s_ log _p_ . Finally, � � set _s_ = _⌈cnω_<sup>_−_1</sup> _/_ 4 log _p⌉_ , we get the desired conclusion. 

_Proof of Lemma 7._ First, we note that the quantity of interest can be upper bounded by the following four terms: 



We provide bounds on each term in (38) sequentially. _T_ 1 is the standard Deviation Bound, which according to previous derivations (e.g., Basu and Michailidis (2015) for the expression specifically derived for VAR(1)) satisfies 



with probability at least 1 _− c_ 1 exp( _−c_ 2 log( _p_ 1 + _p_ 2)) for some _{ci}_ . For _T_ 2, since rows of **W** are iid realizations from _N_ (0 _,_ Σ _w_ ), then for ∆<sup>_⊤_</sup> **Z** _n−_ 1<sup>**W**</sup><sup>_∈_R(</sup><sup>_p_1+</sup><sup>_p_2)</sup><sup>_×_(</sup><sup>_p_1+</sup><sup>_p_2)whichhasatmost</sup> _p_ 1 _×_ ( _p_ 1 + _p_ 2) nonzero entries, each entry ( _i, j_ ) given by 



is Gaussian, and the following tail bound holds: 



Taking the union bound over all _p_ 1 _×_ ( _p_ 1 + _p_ 2) nonzero entries, the following bound holds: 



38 

Estimating High-Dimensional FAVAR Models 

log( _<u>p</u>_ 1( _<u>p</u>_ 1+ _<u>p</u>_ 2)) Choose _t_ = _c_ 0�Λmax<sup>1</sup><sup>_/_2(Σ</sup> _w_<sup>)</sup> _i_ =1<sup>max</sup> _,...,p_ 1<sup>_∥_∆</sup><sup>**F**</sup><sup>_·i/√_</sup> _<u>n∥</u>_ �<sup>~~�~~</sup> _n_ , the following bound holds with probability at least 1 _−_ exp � _− c_ 1 log � _p_ 1( _p_ 1 + _p_ 2)�<sup>�</sup> : 



For _T_ 3, let _εn_ := ∆ **Z** _n −_ ∆ **Z** _n−_ 1( _A_<sup>_⋆_</sup> )<sup>_⊤_</sup> = [∆ **F** _n −_ ∆ **F** _n−_ 1( _A_<sup>_⋆_</sup> 11<sup>)</sup><sup>_⊤, −_∆</sup><sup>**F**</sup> _n−_ 1<sup>(</sup><sup>_A⋆_</sup> 21<sup>)</sup><sup>_⊤_],theneach</sup> entry of _n_<sup><u>1</u></sup><sup>**Z**</sup> _n_<sup>_⊤_</sup> _−_ 1<sup>_εn_isgivenby</sup> 



and it has ( _p_ 1+ _p_ 2) _×_ ( _p_ 1+ _p_ 2) entries. Next, note that column _i_ of **Z** _n−_ 1 _∈_ R<sup>_n_</sup> can be viewed as a mean-zero Gaussian random vector with covariance matrix _Q_<sup>_i_</sup> where ( _Q_<sup>_i_</sup> ) _st_ = [Σ _Z_ ( _t−s_ )] _ii_ satisfying Λmax( _Q_<sup>_i_</sup> ) _≤_ Λmax(Σ _Z_ (0)) _≤_ 2 _πM_ ( _fZ_ ), so for any ( _i, j_ ), � _n_ <u>1</u><sup>**Z**</sup> _n_<sup>_⊤_</sup> _−_ 1<sup>_εn_</sup> � _ij_<sup>satisfies</sup> 



Again by taking the union bound over all ( _p_ 1 + _p_ 2)<sup>2</sup> entries, and let 



the following bound holds w.p. at least 1 _−_ exp( _−c_ 1 log( _p_ 1 + _p_ 2)): 



For _T_ 4, it is deterministic, and satisfies 



Combine all terms, and there exist some constant _C_ 1 _, C_ 2 _, C_ 3 and _c_ 1 _, c_ 2 such that with probability at least 1 _− c_ 1 exp � _− c_ 2 log( _p_ 1 + _p_ 2)�, the bound in (14) holds. 

# **Appendix C. Generalization of the Main Results to Sub-exponential Tailed Error Processes: a Sketch** 

In this section, we provide the counterpart of Theorem 1 for the case where the underlying processes are linear with generalized sub-exponential tails. Specifically, the stable joint 

39 

Lin and Michailidis 

VAR process _Zt_ = ( _Ft_<sup>_′, Xt_)</sup><sup>_′_has the following moving average representation with absolutely</sup> summable coefficients _Bℓ_ ’s (c.f. Rosenblatt (2012)): 



In the case where the process is Gaussian, the _wt_ ’s correspond to Gaussian white noise processes. Throughout this section, we relax the Gaussian assumption and assume _wt_ is a white noise process whose coordinates have the following _α_ -sub-exponential tail decay, that is, there exist two constants _a, b_ such that the following holds: 



Specifically, the case of sub-Gaussian tails corresponds to _α_ = 2, whereas for _α ∈_ (0 _,_ 1] it leads to distributions with heavier tails, such as the sub-exponential distribution ( _α_ = 1) or the Weibull distribution; see also Erd˝os et al. (2012); G¨otze et al. (2019). As a consequence, _Xt_ and _Ft_ deviate from being Gaussian due to the recursive data generating mechanism. Additionally, we assume the noise term of the calibration equation _et_ comes from the same _α_ -sub-exponential family. 

**Proposition 3 (High probability error bounds for** Θ<sup>�</sup> **and** Γ<sup>�</sup> **)** _Suppose we are given some randomly observed snapshots {x_ 1 _, . . . , xn} and {y_ 1 _, . . . , yn} obtained from the stable processes Xt and Yt, whose dynamics are described in_ (5) _and_ (2) _. Assume that the same conditions as in Theorem 1 hold. Then, there exist universal positive constants {Ci} and {ci} such that by solving_ (6) _with regularization parameter_ 



_the solution_ (Θ<sup>�</sup> _,_ Γ)<sup>�</sup> _has the following bound with probability at least_ 1 _−c_ 1 exp _{−c_ 2� log( _p_ 2 _q_ )�2 _/α}:_ 



_for a sufficiently large sample size and some function ψ_ ( _·_ ) _that depends linearly on s_ Γ _⋆, p_ 1 _and r._ 

Note that the bounds for each individual probabilistic event (e.g., RSC condition, deviation bound) differ from those in the Gaussian case, although their expressions in (41) do not exhibit marked differences compared to the Gaussian case; specifically, the bound for _|||_ ∆Θ _/_<sup>_√_</sup> _<u>n|||</u>_<sup>2</sup> F<sup>+</sup><sup>_|||_∆Γ</sup><sup>_|||_2</sup> F<sup>isgovernedbythemorestringentsamplesizerequirementamongst</sup> its building components (i.e., concentration in the operator norm) and the slowest term in terms of probability decay. 

In the rest of this section, we sketch the statements and proofs for key lemmas that underlie the high probability statements, assuming _α_ -sub-exponential tail decay where _α ∈_ (0 _,_ 1] _∪{_ 2 _}_ . In particular, one can verify that the rates obtained below would coincide with 

40 

Estimating High-Dimensional FAVAR Models 

the Gaussian case, if _α_ = 2. Similar arguments can be applied to the Stage II estimate to arrive at the counterpart of Theorem 2, which are omitted. 

Lemmas C.1 generalizes Hanson-Wright type concentration inequality to samples of _Xt_ . 

**Lemma C.1** _Consider some generic p-dimensional linear process given in the form of Xt_ :=<sup>�</sup><sup>_∞_</sup> _ℓ_ =0<sup>Φ</sup><sup>_ℓut−ℓ,whereutisi.i.dcomingfromtheα-sub-exponentialfamilydefined_</sup> _in_ (39) _. Denote its realization by_ **X** _∈_ R<sup>_n×p_</sup> _with n consecutive observations stacked in its rows. Then for a deterministic np × np matrix A, there exists some constant C such that the following bound holds:_ 



_where_ 



_Proof of Lemma C.1._ Let vec( **X**<sup>_⊤_</sup> ) =<sup>_d_</sup> Ω<sup>1</sup><sup>_/_2</sup> _Z_ where Ωis the covariance matrix of the _np_ - dimensional random vector vec( **X**<sup>_⊤_</sup> ) and _Z_ satisfies E _Z_ = 0 _,_ E( _ZZ_<sup>_⊤_</sup> ) = I _np_ . Applying G¨otze et al. (2019, Proposition 1.1) gives 



where 



both _c_ 0 and _M_ are constants that depend on _a, b_ . Next, we consider the bounds for various norms of Ω<sup>1</sup><sup>_/_2</sup> _A_ Ω<sup>1</sup><sup>_/_2</sup> : 

– _|||_ Ω<sup>1</sup><sup>_/_2</sup> _A_ Ω<sup>1</sup><sup>_/_2</sup> _|||_ op _≤|||_ Ω _|||_ op _|||A|||_ op _≤_ 2 _πM_ ( _fX_ ) _|||A|||_ op where the last inequality follows from Basu and Michailidis (2015, Proposition 2.3) which applies to general linear processes; 



Therefore, the last expression in (44) can be upper bounded by (43) and the claim in (42) follows. 

Lemma C.2 is a generalization of Proposition 2.4 in Basu and Michailidis (2015) to the case where the underlying processes come from the _α_ -sub-exponential family. 

**Lemma C.2** _Consider some generic linear processes given in the form of Xt_ :=<sup>�</sup><sup>_∞_</sup> _ℓ_ =0<sup>Φ</sup><sup>_ℓut−ℓ,_</sup> _where ut comes from the α-sub-exponential family. Let_ Σ _X_ (0) := _Cov_ ( _Xt, Xt_ ) _. Denote its realization by_ **X** _∈_ R<sup>_n×p_</sup> _and sample covariance by S_ := _n_<sup><u>1</u></sup><sup>**X**</sup><sup>_⊤_</sup><sup>**X**</sup><sup>_,respectively._</sup> 

41 

Lin and Michailidis 

- _(i) For unit vectors v_ 1 _and v_ 2 _satisfying ∥v_ 1 _∥≤_ 1 _, ∥v_ 2 _∥≤_ 1 _, the following bound holds:_ 

_and_ 



- _(ii) Consider the linear process Zt_ :=<sup>�</sup><sup>_∞_</sup> _ℓ_ =0<sup>Ψ</sup><sup>_ℓwt−ℓ∈_R</sup><sup>_qwithwtcomingfromthesame_</sup> _family of distributions as ut and satisfies Cov_ ( _Xt, Zt_ ) = 0 _;_ **Z** _is similarly defined. Then, the following bound holds:_ 



_where M_ ( _fX,Z_ ) _is identically defined to the quantity in Section 3._ 

_T_<sup>_′_</sup> _has the following functional form:_ 



_Proof of Lemma C.2._ First we note that with _A_ = I _n_ and the definition of _T_ ( _η, α, n_ ), the following holds for some constant _C >_ 0: 



Let _yt_ := _v_ 1<sup>_⊤Xt_and</sup><sup>**Y**=</sup><sup>**X**</sup><sup>_v_1</sup><sup>_∈_R</sup><sup>_n_be</sup><sup>_n_consecutive observations of the scalar process</sup><sup>_{yt}_,</sup> then 



Apply Lemma C.1 to process _{Yt}_ with _A_ = I _n_ (since moment properties are preserved under linear transformations), to obtain 



Further, by Lemma C.6 in Sun et al. (2018), it follows that _M_ ( _fY_ ) _≤∥v_ 1 _∥_<sup>2</sup> _M_ ( _fX_ ) = _M_ ( _fX_ ); hence, the following bound holds: 



This proves the first part in (i). The rest of the proof follows along similar lines to the derivation of Proposition 2.4 in Basu and Michailidis (2015), and we give an outline without getting into too many details. For _|v_ 1<sup>_′_(</sup><sup>_S −_Σ</sup><sup>_X_(0))</sup><sup>_v_2</sup><sup>_|_,oneconsidersthedecomposition</sup> 

2 _|v_ 1<sup>_′_(</sup><sup>_S −_Σ</sup><sup>_X_(0))</sup><sup>_v_2</sup><sup>_| ≤|v_</sup> 1<sup>_′_(</sup><sup>_S −_Σ</sup><sup>_X_(0))</sup><sup>_v_1</sup><sup>_|_+</sup><sup>_|v_</sup> 2<sup>_′_(</sup><sup>_S −_Σ</sup><sup>_X_(0))</sup><sup>_v_2</sup><sup>_|_+</sup><sup>_|_(</sup><sup>_v_1+</sup><sup>_v_2)</sup><sup>_′_(</sup><sup>_S −_Σ</sup><sup>_X_(0))(</sup><sup>_v_1+</sup><sup>_v_2)</sup><sup>_|_</sup> with _∥v_ 1 + _v_ 2 _∥≤_ 2. Repeating the steps above to each of the three terms yields the desired result. 

42 

Estimating High-Dimensional FAVAR Models 

For _|v_ 1<sup>_′_(</sup><sup>**X**</sup><sup>_⊤_</sup><sup>**Z**)</sup><sup>_v_2</sup><sup>_|_,let</sup><sup>_y_�</sup><sup>_t_=</sup><sup>_v_</sup> 2<sup>_⊤Zt_;then</sup><sup>_v_</sup> 1<sup>_′_(</sup><sup>**X**</sup><sup>_⊤_</sup><sup>**Z**)</sup><sup>_v_2=</sup> _n_ <u>1</u> � _nt_ =1<sup>_yty_�</sup><sup>_t_anditsatisfiesthe</sup> following decomposition 



� where _{gt_ := _yt_ + _yt}_ is the summation process; **G** and **Y**<sup>�</sup> are analogously defined to **Y** . Repeating the above steps to each term. Note that 



and this completes the proof. 

The following lemma considers the deviation bound. Of note, to ensure the deviation <u>2</u> bound vanishes, the sample size requirement would be _n_ ≳ (log _p_ + log _q_ ) _α_ . 

**Lemma C.3 (high probability deviation bound)** _There exist positive constants C and ci >_ 0 _such that the following deviation bound holds_ 



_with probability at least_ 



_for any random realizations_ **X** _∈_ R<sup>_n×p_</sup> _and_ **E** _∈_ R<sup>_n×q_</sup> _, drawn from the linear processes {Xt ∈_ R<sup>_p_</sup> _} and {εt ∈_ R<sup>_q_</sup> _} that are constructed as linear filters of the white noise processes coming from some α-sub-exponential family._ 

_Proof of Lemma C.3._ Apply Lemma C.2, so that for any standard basis vector _ek_ and _ej_ , the following holds: 



Taking the union bound across all _pq_ elements, with probability at least 1 _−_ 3( _pq_ ) _T_<sup>_′_�</sup> _η, α, n_ � = 1 _−_ 3 _c_ 1 exp _{−c_ 2 min _{nη_<sup>2</sup> _,_ ( _nη_ )<sup>_α/_2</sup> _}_ + log( _pq_ ) _}_ , the following bound holds: 



<u>1</u> Set _η_ := _c_ 0(log _p_ + log _q_ ) _α /_<sup>_√_</sup> _<u>n</u>_ <u>,</u> the desired result holds for some sufficiently large _c_ 0 provided that _n_<sup>_α/_4</sup> ≳ log( _pq_ )<sup>(2</sup><sup>_/α−_1</sup><sup>_/_2)</sup> (which ensures that min _{nη_<sup>2</sup> _,_ ( _nη_ )<sup>_α/_2</sup> _}_ ). Specifically, in the context of this problem, the most stringent sample size requirement is dictated by the concentration for the operator norm (see Lemma C.5), and therefore this sample size requirement is automatically fulfilled. 

The following lemma verifies the RSC condition. 

43 

Lin and Michailidis 

**Lemma C.4 (Verification of RSC)** _Consider a snapshot of random realizations_ **X** _∈_ R<sup>_n×p_</sup> _drawn from the linear process Xt_ :=<sup>�</sup><sup>_∞_</sup> _ℓ_ =0<sup>Φ</sup><sup>_ℓut−ℓwithutcomingfromtheα-sub-_</sup> _exponential family. Then RSC holds for_ **X** _with parameter αRSC_ = _π_ m( _fX_ ) _and tolerance τ_ := _c_ 0 _αRSC_ log _p/_ ( _n_<sup>_α/_2</sup> ) _, with probability at least_ 1 _− c_ 1 exp _{−c_ 2 _n_<sup>_α/_2</sup> _}._ 

_Proof of Lemma C.4._ Let _S_ = _n_<sup><u>1</u></sup><sup>**X**</sup><sup>_⊤_</sup><sup>**X**.First,supposewehave</sup> 



then, for all ∆ _∈_ R<sup>_pZ×pZ_</sup> , and letting ∆ _j_ denote its _j_ th column, the RSC condition automatically holds since 



Therefore, it suffices to verify that (46) holds. By Lemma C.2, _∀v ∈_ R<sup>_p_</sup> _, ∥v∥≤_ 1 and _η >_ 0, 



Applying the discretization argument in Basu and Michailidis (2015, Lemma F.2 & Lemma F.3), define K(2 _s_ ) := _{v ∈_ R<sup>_p_</sup> _, ∥v∥≤_ 1 _, ∥v∥_ 0 _≤_ 2 _s}_ , and taking the union bound in this 2 _s_ -sparse cone gives the following inequality: 



Let _η_ = m( _fX_ ) _/_ [54 _M_ ( _fX_ )], then apply results from Loh and Wainwright (2012, Lemma 12) with Γ = _S −_ Σ _X_ (0) and _δ_ = _π_ m( _fX_ ) _/_ 27, so that the following holds 



with probability at least 1 _−_ 2 min _{p_<sup>_s_</sup> _,_ (21 _e · p/s_ )<sup>_s_</sup> _}T_<sup>_′_</sup> ( _η, α, n_ ). By letting _s_ := _c_<sup>_′_</sup> 0<sup>_nα/_2</sup><sup>_/_log</sup><sup>_p_</sup> for some small constant _c_ 0, then _τ_ can be expressed as _τ_ = _c_ 0 _α_ RSC log _p/_ ( _n_<sup>_α/_2</sup> ) and the bound holds with probability at least 1 _− c_ 1 exp _{−c_ 2 _n_<sup>_α/_2</sup> _}_ . 

**Lemma C.5 (High probability bound for** Λmax( _S_ **E** ) **)** _Consider_ **E** _∈_ R<sup>_n×q_</sup> _whose rows are independent realizations drawn from some mean-zero α-sub-exponential distribution with covariance_ Σ _e. Then, the following holds for some constants ci >_ 0 _provided that the sample size satisfies n_<sup>_α/_2</sup> ≳ _q:_ 



_with probability at least_ 1 _− c_ 1 exp( _−c_ 2 _n_<sup>_α/_2</sup> ) _._ 

44 

Estimating High-Dimensional FAVAR Models 

_Proof of Lemma C.5._ The main arguments of the proof follow closely along the lines of those in the proof of Lemma 5, while ignoring the temporal dependence. Specifically, using similar covering arguments, with the tail decay as in Lemma C.2, there exists some constant _ci >_ 0 such that 



By choosing _η_ to be a sufficiently large constant, with _n_<sup>_α/_2</sup> ≳ _q_ , the statement in the lemma holds. 

**Remark 5** To ensure concentration of the operator norm, with the specified choice of _η_ , the sample size requirement in (C.5) is more stringent than that of the Gaussian case. In particular, for the case of sub-exponential tails with _α_ = 1, this would imply a sample size requirement<sup>_√_</sup> _<u>n</u>_ ≳ _<u>q</u>_ . If however, the elements of the random noise vector _et_ ’s are bounded, that is, _∥et∥_ 2 _≤ √C_ almost surely for some _C >_ 0, one can directly apply the matrix Bernstein inequality to obtain the following bound (Wainwright, 2019, Corollary 6.20): 



Depending on how _C_ grows with _q_ , the sample size requirement could potentially be more relaxed to attain concentration. 

# **Appendix D. Additional Numerical Studies** 

In this section, we investigate selected scenarios where the relaxed implementation on estimating the calibration equation may fail to produce good estimates, due to the absence of the compactness constraint. For illustration purposes, it suffices to consider the setting where _Xt_ and _Ft_ jointly follow a multivariate Gaussian distribution and are independent and identically distributed across samples. Throughout, we set _n_ = 200 _, p_ 1 = 5 _, p_ 2 = 50 _, q_ = 100, and � _XFtt_ � _∼N_ (0 _,_ Σ) with Σ _ij_ = 0 _._ 25 ( _i_ = _j_ ) and Σ _ii_ = 1. The noise level is fixed at _σe_ = 1. 

First, we note that based on the performance evaluation shown in Section 4, the estimates demonstrate good performance even without the compactness constraint. The simulation settings are characterized by adequate sparsity in Γ, which in turn limits the size of the equivalence class _C_ ( _Q_ 2) as mentioned in Section 2.1. Therefore, we focus on the following two issues: (i) whether sparsity encourages additional “approximate identification”; and (ii) whether a good initializer helps constrain estimates from subsequent iterations to a ball around the true value. 

We start by considering a non-sparse Γ. Specifically, for both Λ and Γ, their entries are generated from Unif _{_ ( _−_ 1 _._ 5 _, −_ 1 _._ 2) _∪_ (1 _._ 2 _,_ 1 _._ 5) _}_ . Additionally, we specify one alternative model in _C_ ( _Q_ 2) by setting _Q_ 2 = **5** _p_ 1 _×p_ 2, which will generate the corresponding **F**<sup>ˇ</sup> , Θ<sup>ˇ</sup> and Γ.<sup>ˇ</sup> Table 6 depicts the performance of the estimated Θ based on different initializers: 

The results in Table 6 show that the algorithm converges (if at all) to different local optima whose values may deviate markedly for the true ones. Specifically, initializer Θ<sup>_⋆_</sup> + 

45 

Lin and Michailidis 

Table 6: Performance evaluation of Θ obtained from different initializers under a non-sparse setting.<sup>�</sup> 

|initializer <sup>�</sup>Θ<sup>(0)</sup>|Θ<sup>_⋆_</sup>|**0**_n×q_|Θ<sup>_⋆_</sup>+ 0_._1_∗_**Z**_n×q_|ˇΘ|
|---|---|---|---|---|
|Rel.Err|0.09|0.63|fail to converge within 5000 iterations|1.82 (0.02, relative to <sup>ˇ</sup>Θ)|



0 _._ 1 _∗_ **Z** _n×q_ , where each entry Θ<sup>_⋆_</sup> is perturbed by an iid standard Gaussian random variable scaled by 0.1, fails to converge. Note that the perturbation is small, but the operator norm of the initializer far exceeds _φ_ 0. Initializer Θ<sup>ˇ</sup> yields an estimate that is far from the true data-generating factor hyperplane, yet close to its observationally equivalent one. This suggests that in non-sparse settings, without imposing the compactness constraint on the equivalence class, a good initializer is required for the actual relaxed implementation to produce a fairly good estimate of the true data generating parameters. 

However, this is not the case if there is sufficient sparsity in Γ. Specifically, using the same generating mechanism for Λ and Γ as in Section 4, we found that even with different initializers, the algorithm always produces estimates that are close to each other and also exhibit good performance. This finding strongly suggests that sparsity in Γ effectively shrinks the size of the equivalence class and the algorithm after a few iterations produces updates that are close to each other, irrespective of the initializer employed. Hence, the effective equivalence class is constrained to the one whose elements are encoded by Γ<sup>ˇ</sup> that have similar characteristics in terms of the location of the non-zero parameters to Γ. 

Finally, we consider a case that lies between the above two settings, that is, there is a structured sparsity pattern in Γ. Specifically, we set the last 5 columns of Γ to be dense while the remaining ones are sparse. The overall density level of Γ is fixed at 10%. Note that in this case, the size of the corresponding equivalence class is much larger to the one corresponding to a Γ with 10% uniformly distributed non-zeros entries, due to the presence of the dense columns. 

Table 7: Performance evaluation for Θ<sup>�</sup> with different initializers under structured sparsity. 

|initializer <sup>�</sup>Θ<sup>(0)</sup>|Θ<sup>_⋆_</sup>|**0**_n×q_|Θ<sup>_⋆_</sup>+ 0_._1_∗_**Z**_n×q_|**20**_n×q_|
|---|---|---|---|---|
|Rel.Err|0.65|0.65|0.65|0.68|



As the results in Table 7 indicate, when the initializer starts to deviate from the true value, there exist initializers that would yield inferior estimates. 

In summary, in a non-sparse setting without compactification of the equivalence class, different initializers yield drastically different estimates that are not close enough to the true data-generating model, as expected by the approximate (IR+) condition employed. The problem is largely mitigated for sufficiently sparse Γ, which leads to shrinking the equivalence class. However, an exact characterization of the equivalence class is hard to obtain in practice, since the location of the non-zero entries in Γ is unknown. 

46 

Estimating High-Dimensional FAVAR Models 

# **Appendix E. List of Commodities and Macroeconomic Variables** 

Table 8: List of commodities considered in this study. Data source: International Monetary Fund. 

|Commodity|Key|Description|
|---|---|---|
|ALUMINUM|PALUM|Aluminum, 99.5% minimum purity, LME spot price|
|COCOA|PCOCO|Cocoa beans, International Cocoa Organization cash price|
|COFFEE|PCOFFOTM|Cofee, Other Mild Arabicas, International Cofee Organization New York cash price|
|COPPER|PCOPP|Copper, grade A cathode, LME spot price|
|COTTON|PCOTTIND|Cotton, Cotton Outlook ’A Index’, Middling 1-3/32 inch staple|
|LEAD|PLEAD|Lead, 99.97% pure, LME spot price|
|MAIZE|PMAIZMT|Maize (corn), U.S. No.2 Yellow, FOB Gulf of Mexico, U.S. price|
|NICKEL|PNICK|Nickel, melting grade, LME spot price|
|OIL|POILAPSP|Crude Oil (petroleum), simple average of three spot prices|
|RICE|PRICENPQ|Rice, 5 percent broken milled white rice, Thailand nominal price quote|
|RUBBER|PRUBB|Rubber, Singapore Commodity Exchange, No. 3 Rubber Smoked Sheets, 1st contract|
|SOYBEANS|PSOYB|Soybeans, U.S. soybeans, Chicago Soybean futures contract (frst contract forward)|
|SUGAR|PSUGAUSA|Sugar, U.S. import price, contract no.14 nearest futures position|
|TIN|PTIN|Tin, standard grade, LME spot price|
|WHEAT|PWHEAMT|Wheat, No.1 Hard Red Winter, ordinary protein|
|ZINC|PZINC|Zinc, high grade 98% pure|



|Name|Description|tCode|Category|Region|
|---|---|---|---|---|
|IPI<br>~~U~~S|IP Index: total|5|Output & Income|US|
|CUM<br>~~U~~S|Capacity Utilization: manufacturing|2|Output & Income|US|
|UNEMP<br>~~U~~S|Civilian unemployment rate: all|2|Labor Market|US|
|HOUST<br>~~U~~S|Housing Starts: ttl new privately owned|4|Housing|US|
|ISR<br>~~U~~S|Total Business: inventories to sales ratio|2|Consumption|US|
|M2<br>~~U~~S|M2 Money Stock|6|Money & Credit|US|
|BUSLN<br>~~U~~S|Commericial and industrial loans|6|Money & Credit|US|
|REALN<br>US|Real estate loans at all commercial banks|6|Money & Credit|US|
|FFR<br>~~U~~S|Efective federal funds rate|2|Interest & Exchange Rates|US|
|TB10Y<br>~~U~~S|10-year treasury rate|2|Interest & Exchange Rates|US|
|BAA<br>~~U~~S|Moody’s Baa corporate bond yield|2|Interest & Exchange Rates|US|
|USDI<br>~~U~~S|Trade weighted U.S.dollar index|5|Interest & Exchange Rates|US|
|CPI<br>~~U~~S|CPI: all iterms|5|Prices|US|
|PCEPI<br>~~U~~S|Personal Consumption Expenditure: chain index|5|Prices|US|
|SP500<br>~~U~~S|S&P’s Common Stock Price Index: composite|5|Stock Market|US|
|CPI<br>~~E~~U|Consumer Price Indices, percent change|2|Prices|EU|
|IPI<br>~~E~~U|Industrial Production Index: total industry (excluding construction)|5|Output & Income|EU|
|IPICP<br>~~E~~U|Industrial Production Index: construction|5|Output & Income|EU|
|M3<br>~~E~~U|Monetary aggregate M3|6|Money & Credit|EU|
|LOANRES<br>~~E~~U|Credit to resident sectors, non-MFI excluding gov|6|Money & Credit|EU|
|LOANGOV<br>~~E~~U|Credit to general government sector|6|Money & Credit|EU|
|PPI<br>~~E~~U|Producer Price Index: total industry (excluding construction)|6|Prices|EU|
|UNEMP<br>~~E~~U|Unemployment rate: total|2|Labor Market|EU|
|IMPORT<br>~~E~~U|Total trade: import value|6|Trade|EU|
|EXPORT<br>~~E~~U|Total trade: export value|6|Trade|EU|
|EB1Y<br>~~E~~U|Euribor 1 year|2|Interest & Exchange Rates|EU|
|TB10Y<br>~~E~~U|10-year government benchmark bond yield|2|Interest & Exchange Rates|EU|
|EFFEXR<br>~~E~~U|ECB nominal efective exchange rate againt group of trading partners|2|Interest & Exchange Rates|EU|
|EUROSTOXX50<br>~~E~~U|Euro STOXX composite index|5|Stock Market|EU|
|IOP<br>~~U~~K|Index of Production|5|Output & Income|UK|
|CPI<br>~~U~~K|CPI Index|5|Prices|UK|
|PPI<br>~~U~~K|Output of manufactured products|5|Prices|UK|
|UNEMP<br>~~U~~K|Unemployment rate: aged 16 and over|2|Labor Market|UK|
|EFFEXR<br>~~U~~K|Efective exchange rate index, Sterling|2|Interest & Exchange Rates|UK|
|TB10Y<br>~~U~~K|10-year British government stock, nominal par yield|2|Interest & Exchange Rates|UK|
|LIBOR6M<br>~~U~~K|6 month interbank lending rate, month end|2|Interest & Exchange Rates|UK|
|M3<br>~~U~~K|Monetary aggregate M3|6|Money & Credit|UK|
|CPI<br>~~C~~N|CPI: all iterms|5|Prices|CN|



47 

Lin and Michailidis 

|PPI<br>~~C~~N|Producer price index for industrial products (same month last year = 100)|2|Prices|CN|
|---|---|---|---|---|
|M2<br>~~C~~N|Monetary aggregate M2|6|Money & Credit|CN|
|EFFEXR<br>~~C~~N|Real broad efective exchange rate|2|Interest & Exchange Rates|CN|
|EXPORT<br>~~C~~N|Value goods|6|Trade|CN|
|IMPORT<br>~~C~~N|Value goods|6|Trade|CN|
|INDGR<br>~~C~~N|Growth rate of industrial value added (last year = 100)|2|Output & Income|CN|
|SHANGHAI<br>~~C~~N|Shanghai Composite Index|5|Stock Market|CN|
|TB10Y<br>~~J~~P|10-year government benchmark bond yield|2|Interest & Exchange Rates|JP|
|EFFEXR<br>~~J~~P|Real broad efective exchange rate|2|Interest & Exchange Rates|JP|
|CPI<br>~~J~~P|CPI Index: all items|5|Prices|JP|
|M2<br>~~J~~P|Monetary aggregate M2|6|Money & Credit|JP|
|UNEMP<br>~~J~~P|Unemployment rate: aged 15-64|2|Labor Market|JP|
|IPI<br>~~J~~P|Production of Total Industry|5|Output & Income|JP|
|IMPORT<br>~~J~~P|Import price index: all commodities|6|Trade|JP|
|EXPORT<br>~~J~~P|Value goods|6|Trade|JP|
|NIKKEI225<br>~~J~~P|NIKKEI 225 composite index|5|Stock Market|JP|



Table 9: List of macroeconomic variables in this study. 

Data source: Fred St.Louis, ECB Statistical Data Warehouse, UK Office for National Statistics, Bank of England, National Bureau of Statistics of China, YAHOO!. tCode: 1: none; 2: ∆ _Xt_ ; 3: ∆<sup>2</sup> _Xt_ ; 4: log _Xt_ ; 5: ∆log _Xt_ ; 6: ∆<sup>2</sup> log _Xt_ ; 7: ∆( _Xt/Xt−_ 1 _−_ 1). 

# **References** 

- Alekh Agarwal, Sahand Negahban, Martin J Wainwright, et al. Noisy matrix decomposition via convex relaxation: optimal rates in high dimensions. _The Annals of Statistics_ , 40(2): 1171–1197, 2012. 

- Theodore W Anderson. _The Statistical Analysis of Time Series_ , volume 19. John Wiley & Sons, 2011. 

- Theodore Wilbur Anderson. _An Introduction to Multivariate Statistical Analysis_ , volume 2. Wiley New York, 1958. 

- Tomohiro Ando and Jushan Bai. Selecting the regularization parameters in highdimensional panel data models: Consistency and efficiency. _Econometric Reviews_ , 37 (3):183–211, 2018. 

- Jushan Bai and Serena Ng. Large dimensional factor analysis. _Foundations and Trends_ R _⃝ in Econometrics_ , 3(2):89–163, 2008. 

- Jushan Bai, Kunpeng Li, and Lina Lu. Estimation and inference of favar models. _Journal of Business & Economic Statistics_ , 34(4):620–641, 2016. 

- Marta Ba´nbura, Domenico Giannone, and Lucrezia Reichlin. Large Bayesian vector auto regressions. _Journal of Applied Econometrics_ , 25(1):71–92, 2010. 

- Sumanta Basu and George Michailidis. Regularized estimation in sparse high-dimensional time series models. _The Annals of Statistics_ , 43(4):1535–1567, 2015. 

- Ben S Bernanke, Jean Boivin, and Piotr Eliasz. Measuring the effects of monetary policy: a factor-augmented vector autoregressive (FAVAR) approach. _The Quarterly Journal of Economics_ , 120(1):387–422, 2005. 

48 

Estimating High-Dimensional FAVAR Models 

- Giovanni Caggiano, Efrem Castelnuovo, and Nicolas Groshenny. Uncertainty shocks and unemployment dynamics in us recessions. _Journal of Monetary Economics_ , 67:78–92, 2014. 

- Emmanuel J Candes and Yaniv Plan. Matrix completion with noise. _Proceedings of the IEEE_ , 98(6):925–936, 2010. 

- Kamal C Chanda et al. Asymptotic properties of estimators for autoregressive models with errors in variables. _The Annals of Statistics_ , 24(1):423–430, 1996. 

- Venkat Chandrasekaran, Pablo A Parrilo, and Alan S Willsky. Latent variable graphical model selection via convex optimization. _The Annals of Statistics_ , 40(4):1935–1967, 2012. 

- Sandra Eickmeier, Leonardo Gambacorta, and Boris Hofmann. Understanding global liquidity. _European Economic Review_ , 68:1–18, 2014. 

- L´aszl´o Erd˝os, Horng-Tzer Yau, and Jun Yin. Bulk universality for generalized Wigner matrices. _Probability Theory and Related Fields_ , 154:341–407, 2012. 

- Jeffrey A Frankel. The effect of monetary policy on real commodity prices. Technical report, National Bureau of Economic Research, 2006. 

- Jeffrey A Frankel. Effects of speculation and interest rates in a carry trade model of commodity prices. _Journal of International Money and Finance_ , 42:88–112, 2014. 

- Friedrich G¨otze, Holger Sambale, and Arthur Sinulis. Concentration inequalities for polynomials in _α_ -sub-exponential random variables. _arXiv preprint arXiv:1903.05964_ , 2019. 

- Suriya Gunasekar, Arindam Banerjee, and Joydeep Ghosh. Unified view of matrix completion under general structural constraints. In _Advances in Neural Information Processing Systems_ , pages 1180–1188, 2015. 

- Eric C Hall, Garvesh Raskutti, and Rebecca Willett. Learning high-dimensional generalized linear autoregressive models. _IEEE Transactions on Information Theory_ , 65(4):2401– 2422, 2019. 

- Ivana Komunjer and Serena Ng. Measurement errors in dynamic models. _Econometric Theory_ , 30(1):150–175, 2014. 

- Jiahe Lin and George Michailidis. Regularized estimation and testing for high-dimensional multi-block vector-autoregressive models. _Journal of Machine Learning Research_ , 18 (117):1–49, 2017. 

- Robert B Litterman. Forecasting with Bayesian vector autoregressions—five years of experience. _Journal of Business & Economic Statistics_ , 4(1):25–38, 1986. 

- Po-Ling Loh and Martin J Wainwright. High-dimensional regression with noisy and missing data: provable guarantees with nonconvexity. _The Annals of Statistics_ , 40(3):1637–1664, 2012. 

49 

Lin and Michailidis 

- Helmut L¨utkepohl. _New Introduction to Multiple Time Series Analysis_ . Springer Science & Business Media, 2005. 

- Helmut L¨utkepohl. Structural vector autoregressive analysis in a data rich environment. Technical report, Deutsches Institut f¨ur Wirtschaftsforschung, 2014. 

- Igor Melnyk and Arindam Banerjee. Estimating structured vector autoregressive models. In _International Conference on Machine Learning_ , pages 830–839, 2016. 

- Sahand Negahban and Martin J Wainwright. Estimation of (near) low-rank matrices with noise and high-dimensional scaling. _The Annals of Statistics_ , 39(2):1069–1097, 2011. 

- Sahand Negahban and Martin J Wainwright. Restricted strong convexity and weighted matrix completion: optimal bounds with noise. _Journal of Machine Learning Research_ , 13(53):1665–1697, 2012. 

- Sahand Negahban, Bin Yu, Martin J Wainwright, and Pradeep K Ravikumar. A unified framework for high-dimensional analysis of _M_ -estimators with decomposable regularizers. _Statistical Science_ , 27(4):538–557, 2012. 

- William B Nicholson, David S Matteson, and Jacob Bien. VARX-L: Structured regularization for large vector autoregressions with exogenous variables. _International Journal of Forecasting_ , 33(3):627–651, 2017. 

- Murray Rosenblatt. _Stationary Sequences and Random Fields_ . Springer Science & Business Media, 2012. 

- Anil K Seth, Adam B Barrett, and Lionel Barnett. Granger causality analysis in neuroscience and neuroimaging. _Journal of Neuroscience_ , 35(8):3293–3297, 2015. 

- Ali Shojaie and George Michailidis. Discovering graphical granger causality using the truncating lasso penalty. _Bioinformatics_ , 26(18):i517–i523, 2010. 

- Christopher A Sims. Macroeconomics and reality. _Econometrica: Journal of the Econometric Society_ , pages 1–48, 1980. 

- James H Stock and Mark W Watson. Forecasting using principal components from a large number of predictors. _Journal of the American Statistical Association_ , 97(460):1167–1179, 2002. 

- James H Stock and Mark W Watson. Dynamic factor models, factor-augmented vector autoregressions, and structural vector autoregressions in macroeconomics. In John B Taylor and Harald Uhlig, editors, _Handbook of Macroeconomics_ , volume 2A, chapter 8, pages 415–525. Elsevier, 2016. 

- James H Stock and Mark W Watson. Twenty years of time series econometrics in ten pictures. _Journal of Economic Perspectives_ , 31(2):59–86, 2017. 

- Yiming Sun, Yige Li, Amy Kuceyeski, and Sumanta Basu. Large spectral density matrix estimation by thresholding. _arXiv preprint arXiv:1812.00532_ , 2018. 

50 

Estimating High-Dimensional FAVAR Models 

- Martin J Wainwright. Sharp thresholds for high-dimensional and noisy sparsity recovery using _ℓ_ 1-constrained quadratic programming (Lasso). _IEEE Transactions on Information Theory_ , 55(5):2183–2202, 2009. 

- Martin J Wainwright. _High-dimensional Statistics: A Non-Asymptotic Viewpoint_ , volume 48. Cambridge University Press, 2019. 

51 

