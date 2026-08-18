---
title: Beyeler_Factor augmented VAR revisited A sparse dynamic factor model approach_2017
type: paper
source_pdf: raw/papers/Beyeler_Factor augmented VAR revisited A sparse dynamic factor model approach_2017.pdf
converted: 2026-08-18
---

# - Factor VAR revisited A augmented sparse dynamic factor model approach 

Simon Beyeler<sup>_∗_</sup> and Sylvia Kaufmann<sup>_†‡_</sup> 

January 2017 

##### Abstract 

We combine the factor augmented VAR framework with recently developed estimation and identication procedures for sparse dynamic factor models. Working with a sparse hierarchical prior distribution allows us to discriminate between zero and non-zero factor loadings. The non-zero loadings identify the unobserved factors and provide a meaningful economic interpretation for them. Applying our methodology to US macroeconomic data reveals indeed a high degree of sparsity in the data. We use the estimated FAVAR to study the eect of a monetary policy shock and a shock to the term premium. Factors and specic variables show sensible responses to the identied shocks. 

JEL classication: C32, C55, E32, E43, E52 Key words: Bayesian FAVAR; sparsity; factor identication 

> _∗_ Study Center Gerzensee and University of Bern, Dorfstrasse 2, CH-3115 Gerzensee, simon.beyeler@szgerzensee.ch 

> _†_ Study Center Gerzensee, Dorfstrasse 2, CH-3115 Gerzensee, sylvia.kaufmann@szgerzensee.ch 

> _‡_ We thank Luca Benati, Mark Watson and seminar participants at the University of Bern and Newcastle University Business School for valuable comments and discussions. Omissions and errors are ours. 

1 

## 1 Introduction 

The use of factor models has become a common tool in macroeconomic analysis, it facilitates the work when a wide range of data is used to study the properties of an economy. In recent times with the extraordinary developments in information technology the ability to handle large amounts of data has become crucial in the eld of economics. Extracting relevant information from many dierent time series measuring dierent aspects of an economy and compressing it using factor analysis is a neat way to circumvent the curse of dimensionality without ignoring possibly important features. 

Bernanke et al. (2005) (henceforth BBE05) suggested augmenting standard small scale vector autoregression (VAR) models by adding unobserved latent factors estimated from a large macro dataset to include additional information in the analysis. They motivated the framework by observing that some economic concepts like output gap, the business cycle stance or ination sometimes may not be observed without error by the econometrician (and maybe neither by the policy maker). By extracting the relevant information from a large dataset covering the main areas of the economy into factors would address the issue. On the other hand, variables observable in a timely manner and without large errors, could be dened as observed factors and included without transformation into the factor augmented VAR (FAVAR) system. 

To estimate the unobserved factors, BBE05 apply two frameworks. In the rst and their preferred one, factors are extracted by principal components (Stock and Watson 2002). To ensure that unobserved factors are purged from the information content of observed factors for all other variables, factors are estimated in a two-step procedure. In the rst step, factors are extracted from all variables including the observed factors. These rst-stage estimates are then purged from the information content of the observed factors conditioning on factors extracted from so-called slow moving variables by a regression-based approach. Later studies purged the initial estimates of common factors by a regression-based approach and iterated the procedure up to convergence (Boivin and Giannoni 2007). In the parametric framework (Stock and Watson 1989, Geweke and Zhou 1996), factor estimation conditions on observed factors. However, additional restrictions have to be imposed to exclude that estimated unobserved factors contain linear combinations of observed factors. BBE05 achieve this by imposing restrictions on the leading square matrix of factor loadings, and estimate unobserved factors by Bayesian Markov chain Monte Carlo (MCMC) methods. However, factors estimated parametrically usually lack proper interpretation, which is inherently the case for factors estimated by principal components. Bai and Ng (2013) propose to obtain an interpretation of factors by ex-post rotation and re-ordering of series. In the Bayesian approach, BBE05 suggest to assign some of the variables exclusively to one of the factors (in addition to the identication restrictions) to obtain an interpretation of factors as economic concepts. 

In the present paper, we propose to estimate a sparse dynamic factor model for the FA part in the FAVAR approach. Sparse factor models have been traditionally applied in gene expression analysis (West 2003, Carvalho et al. 2008). They are based on the idea that a single factor is not necessarily related to all the variables in the underlying data set. Rather, it may only account for the co-movement in a subset of variables. We proceed along the lines of Kaufmann and Schumacher (2013) (henceforth KS13), who propose to estimate the factors independently of variable 

2 

ordering, and identify factor positions and sign after estimation by processing the posterior MCMC output. We estimate factors in a parametric way by Bayesian MCMC methods and propose an alternative identication scheme. First, to exclude that unobserved factors contain linear combinations involving observed factors, we assume that observed and unobserved factors are contemporaneously independent. This is implemented by restricting the error covariance between unobserved and observed factors to be block-diagonal, see also Bai et al. (2016). To identify the space of unobserved factors, we basically rely on the fact that the estimated factor loading matrix is sparse. A factor will be identied and obtain an interpretation by those series that load on this specic factor. Factor interpretation is additionally strengthened if groups of series like series related to production, to nancial markets, to prices etc. load on the same factor. Hence, factor interpretation is obtained by model estimation rather than by imposing additional restrictions on variable ordering and timing restrictions of variables' responses to shocks in factors (Boivin et al. 2016). Conditional on the sparse loading matrix, we can estimate an unrestricted error covariance matrix of unobserved factors (Conti et al. 2014), in which we restrict the factor-specic error variance to unity for scaling purposes. Empirical results in KS13, Kaufmann and Schumacher (2017) and in the present paper document that there is a lot of sparsity in large economic datasets. After estimation and identication of factor position and sign, we can assess identication by comparing the factor loading structure to identication schemes commonly used in the literature (Geweke and Zhou 1996; Aguilar and West 2010; Frühwirth-Schnatter and Lopes 2010). 

The estimated sparse FAVAR model provides a basis for further structural analysis. The identied factors allow for a richer, factor-specic interpretation of results from structural FAVAR models. In studies analyzing monetary policy transmission and related issues like price stickiness (Boivin et al. 2009; Boivin et al. 2011; Baumeister et al. 2013), the results usually focus on the response in the common component of specic (groups of) variables to the identied monetary policy shock. Factor identication allows us to discriminate between factor-specic response. Working with a sparse factor loading matrix may help identifying structural shocks in FAVAR models allowing for time-varying parameters (Korobilis 2013) and combining series of mixed-frequency (Marcellino and Sivec 2016). 

In the next section, we describe the model specication and discuss the identication strategy. Section 3 presents the Bayesian MCMC sampling scheme and in particular the estimation of the factors. The nal subsection briey presents the post-processing procedure to identify factor position and factor sign. To illustrate the method, we work with a panel of series for the US macroeconomy for which we estimate and identify seven unobserved factors next to the federal funds rate (FFR) that we include as observed factor. We nd evidence for a substantial amount of sparsity in this dataset and the structure of non-zero entries in the factor loading matrix gives an economic interpretation to all unobserved factors. Despite the amount of sparsity and the small number of factors, the common component explains a large fraction of the sample variance. We proceed with a structural VAR analysis to study the eects of monetary policy and an innovation in the term-premium factor. The estimated factors and specic variables all show sensible responses to the identied monetary policy shock. In line with the ndings in Kurmann and Otrok (2013), our results suggest that a shock to the term premium generates very similar impulse responses as a news shock. We briey show how the identication strategy described 

3 

in Uhlig (2003) can be adapted to the FAVAR environment to identify shocks in the factor VAR that act as main driver of a specic variable in the data set. Section 5 concludes. 

## 2 Model specication and identication 

### 2.1 The model 

The framework proposed in BBE05 collects _N_ non-trending observed variables in a _N ×_ 1 vector _Xt_ , where _t_ = 1 _, . . . , T_ . These variables are assumed to contain information on some pervasive _k_ , _k << N_ , economic factors _ft_<sup>_∗_whicharenot</sup> directly observable to the econometrician but are relevant determinants of some _m_ observed series _Yt_ . The FAVAR representation for [ _ft_<sup>_∗′Y_</sup> _t_<sup>_′_]writes</sup> 



where _λ_<sup>_∗f_</sup> and _λ_<sup>_∗Y_</sup> are the factor loading matrices with dimension _N × k_ and _N × m_ , respectively, and _Im_ represents the identity matrix of dimension _m_ . A AR process of order _p_ characterizes the process of [ _ft_<sup>_∗′Y_</sup> _t_<sup>_′_].Weassumethatthecommonco-</sup> movement in _Xt_ is fully explained by _ft_<sup>_∗_and</sup><sup>_Yt_.Therefore,commonandidiosyn-</sup> cratic shocks are uncorrelated, i.e. _E_ ( _ηt_<sup>_∗ε′_</sup> _t_<sup>)=0,andidiosyncraticcomponents</sup><sup>_ξt_</sup> follow series-specic independent VAR processes, i.e. Ψ( _L_ ) and Ω are, respectively, diagonal processes and diagonal with elements _{_ Ψ( _L_ ) _,_ Ω _}_ = _{ψi_ ( _L_ ) _, ωi_<sup>2</sup><sup>_|ψi_(</sup><sup>_L_)=</sup> 1 _− ψi_ 1 _L −· · · − ψiqL_<sup>_q_</sup> _, i_ = 1 _, . . . , N }_ . 

The<sup>_∗_</sup> in model (1) indicates that we work with a sparse factor model and estimate sparse factor loading matrices _λ_<sup>_∗f_</sup> and _λ_<sup>_∗Y_</sup> , i.e. matrices that potentially contain zero loadings. This extends the framework of BBE05 in the sense that the non-zero loadings in columns potentially yield an explicit interpretation of unobserved factors _ft_<sup>_∗_.Forexample,afactoronlyloadingonpricevariablesmayreect</sup> nominal conditions of an economy while a factor loading mostly on real variables may reect business cycle conditions. On the other hand, rows of zero loadings in _λ_<sup>_∗f_</sup> indicate variables that are irrelevant for the estimation of the factors. As shown in KS13, such variables do not contain relevant information for estimating the factors and deteriorate estimation eciency if included for estimation. Sparsity in _λ_<sup>_∗Y_</sup> captures the idea that the observed variables _Yt_ also reect (observable) information common to specic groups of variables. For example, changes in the policy interest rate, if included in _Yt_ , may aect other interest rates included in _Xt_ , while not contemporaneously aecting real variables like consumption or investment. 

In this paper, we estimate model (1) in a Bayesian parametric framework based on Gibbs sampling. In their paper, BBE05 prefer the non-parametric two-step estimation based on principal components analysis over parametric estimation. They achieve structural identication of shocks by imposing a recursive scheme on Σ<sup>_∗_</sup> . They argue that structural identication in the parametric framework is more di- cult to establish, in particular because structural identication is ultimately linked to factor identication in the sense of factor interpretation. They suggest to obtain 

4 

factor identication by restricting additionally the factor loading matrix _λ_<sup>_∗f_</sup> . For example, those series perceived to be related to business cycle conditions would be restricted to load onto the factor dened to reect business cycle conditions, etc. This procedure would come close to conrmatory factor analysis or to a dedicated factor model, see e.g. Lawley and Maxwell (1971) or more recently Conti et al. (2014). 

We show that using a sparse parametric approach eventually yields factor identication, not by imposing variable-factor association a priori but by letting the data tell us the variable-specic factor association. After estimation, structural identication of shocks is ultimately obtained by factor interpretation. Our experience with economic data is very promising in that respect. 

### 2.2 Implementing sparsity 

The sparse factor loading matrices _λ_<sup>_∗f_</sup> and _λ_<sup>_∗Y_</sup> will be estimated freely, i.e. without imposing identication restrictions, see also section 2.3. To induce sparsity, we work with a hierarchical point mass-normal mixture prior distribution on the factor loadings _λ_<sup>_∗_</sup> _ij_<sup>,</sup><sup>_i_=1</sup><sup>_, . . . , N_,</sup><sup>_j_=1</sup><sup>_, . . . , k_+</sup><sup>_m_(seee.g.West2003,Carvalhoetal.</sup> 2008) 



where _δ_ 0 is a Dirac delta function that assigns all probability mass to zero and _B_ ( _uv, u_ (1 _− v_ )) denotes a beta distribution with mean _v_ and precision _u_ . For _τj_ , we assume an inverse Gamma prior distribution _IG_ ( _g_ 0 _, G_ 0) . The factor-independent parametrization of the hyperparameters renders the prior distribution invariant with respect to factor ordering an sign. This is useful to apply random permutation sampling to draw from the unconstrained multimodal posterior distribution. Posterior mode identication, i.e. identifying factor position and sign, is obtained by processing the posterior output, see section 3.4. 

Setting up the prior in this way implies a common probability across series of a non-zero loading on factor _j_ equal to _ρjb_ . With appropriate parametrization of layer (3), we can implement the viewpoint that for many variables the probability of association with anyone factor is zero, while for a few it will be high. 

The point mass-normal mixture prior (2)-(4) explicitly discriminates between zero and non-zero loadings. This allows us to perform variable selection simultaneously while estimating the model, see e.g. George and McCulloch (1997). In this way, we can avoid proceeding in a two-step manner to identify the relevant variables (Forni et al. 2001, Bai and Ng 2008). 

### 2.3 Identication 

As well known in factor analysis, conditional on the idiosyncratic processes, model (1) is identied up to rotation (Lawley and Maxwell 1971). For any non-singular ma- _Qf Q_<sup>_fY_</sup> trix _Q_ = ,<sup>1</sup> we can rotate representation (1) into an observationally <u>�</u> _Q_<sup>_Y f_</sup> _Q_<sup>_Y_</sup> <u>�</u> 

1 We save on notation by using single superscripts for the diagonal submatrices. 

5 

equivalent one: 



Unrestricted rotation yields 



It seems obvious to require that observed variables remain observed after rotation. This is ensured by restricting _Q_<sup>_Y f_</sup> = 0 and _Q_<sup>_Y_</sup> = _Im_ . For identication, we thus need _k_<sup>2</sup> + _km_ restrictions (Bai et al. 2016). 

We proceed as follows. We rule out the possibility that unobserved factors involve linear combinations of observed variables like in (6), for which we obtain _λ_<sup>ˆ</sup><sup>_f_</sup> = _λ_<sup>_∗f_</sup> ( _Q_<sup>_f_</sup> )<sup>_−_1</sup> and _λ_<sup>ˆ</sup><sup>_Y_</sup> = _λ_<sup>_∗Y_</sup> _− λ_<sup>_∗f_</sup> ( _Q_<sup>_f_</sup> )<sup>_−_1</sup> _Q_<sup>_fY_</sup> for the loadings. For any nonsingular _k × k_ matrix _Q_<sup>_f_</sup> , the requirement can be achieved by restricting the _k × m_ matrix _Q_<sup>_fY_</sup> = 0 . For _Q_<sup>_f_</sup> = _Ik_ , the restriction implies _E_ ( _ft_<sup>_∗Y_</sup> _t_<sup>_′|It−_1) = 0, with</sup><sup>_It−_1denoting</sup> information up to period _t −_ 1 . Therefore, we assume that conditional on past information, unobserved factors _ft_<sup>_∗_becontemporaneouslyuncorrelatedtoobserved</sup> 



us with _km_ restrictions. 

With remaining _k_<sup>2</sup> restrictions, we have to identify the factor space of the unobserved factors. We scale factors by assuming the diagonal elements of Σ<sup>_∗_</sup> _f_<sup>to equal 1,</sup> _σfj_<sup>_∗_= 1,</sup><sup>_j_= 1</sup><sup>_, . . . , k_,andkeepitotherwiseunrestricted.Hence,Σ</sup><sup>_∗_</sup> _f_<sup>isinterpretable</sup> as a correlation matrix. The corresponding identication scheme usually proposed in the literature is then to restrict the leading _k × k_ matrix in the factor loading matrix _λ_<sup>_∗f_</sup> to a diagonal matrix _D_ , _λ_<sup>_∗_</sup> 1<sup>_f_</sup> = _D_ . Requiring a specic ordering and a positive sign for the diagonal elements of _D_ simultaneously identies factor position and factor sign. This obviously needs careful choice of the leading _k_ variables in the panel, because these in fact are the factors when estimating the model in the parametric framework (1). Variable ordering is usually not perceived as an issue in factor estimation. Few papers address the issue and present ways of determining relevant leading variables, the so-called factor founders, while estimating the model (Carvalho et al. 2008; Frühwirth-Schnatter and Lopes 2010). We proceed in a dierent way and estimate the factor model independently of variable ordering and do not set _k_ ( _k −_ 1) restrictions on the factor loading matrix _λ_<sup>_∗f_</sup> a priori. We exploit the fact that _λ_<sup>_∗f_</sup> is sparse, i.e. contains loadings equal to 0. Given that usually _k << N_ , we expect that more than _k_ ( _k −_ 1) elements in _λ_<sup>_∗f_</sup> will be 0, and that the structure of the zero loadings will identify the factor model. 

Model estimation identies the factors and all factor-specic parameters up to factor position and sign. The unconstrained posterior distribution will display 2<sup>_k_</sup> _k_ ! modes. We identify factor position and sign ex-post by processing the posterior Gibbs output, see section 3.4. 

6 

Having estimated the model, we may evaluate the structure of _λ_<sup>_∗f_</sup> to nally assess model identication.<sup>2</sup> For example, after estimation, we dene a variable re-ordering matrix _B_ , which would rank rst all variables loading only on the rst factor, then rank those variables only loading on the second factor, and so on, _X_<sup>ˆ</sup> _t_ = _BXt_ . Our experience with empirical economic datasets is that such an ordering can usually be dened ex-post. Then, a leading submatrix of _λ_<sup>ˆ</sup><sup>_∗f_</sup> = _Bλ_<sup>_∗f_</sup> has a generalized diagonal structure, which would conrm that the estimated model is an identied one. 

## 3 Bayesian estimation 

To outline model estimation, we introduce additional notation. We stack factor observations and initial values _f_<sup>_∗p_</sup> into the vector _F_<sup>_∗_</sup> = ( _f_<sup>_∗p′_</sup> _, f_ 1<sup>_∗′, ..., f_</sup> _T_<sup>_∗′_)</sup><sup>_′_.While</sup> _Xt_ denotes observations in period _t_ , _X_<sup>_t_</sup> indicates observations up to period _t_ , and similarly for other variables. All parameters and hyperparameters are included in _θ_ = _{λ_<sup>_∗f_</sup> _, λ_<sup>_∗Y_</sup> _,_ **Φ**<sup>_∗_</sup> _,_ **Ψ** _,_ Ω _,_ Σ<sup>_∗_</sup> _f_<sup>_,_Σ</sup> _Y_<sup>_∗, ϑ}_,where</sup><sup>**Φ**</sup><sup>_∗_=</sup><sup>_{φ∗_</sup> _ij,l_<sup>_|i, j_=1</sup><sup>_, . . . , k_+</sup><sup>_m,l_=</sup> 1 _, . . . , p}_ , **Ψ** = _{ψil|i_ = 1 _, . . . , N, l_ = 1 _, . . . , q}_ , and _ϑ_ = _{β, ρ, τ }_ with _β_ = _{βij|i_ = 1 _, . . . , N, j_ = 1 _, . . . , k_ + _m}_ , _{ρ, τ }_ = _{ρj, τj|j_ = 1 _, . . . , k_ + _m}_ . 

### 3.1 Likelihood and prior specication 

Conditional on factors, the likelihood takes the form 



with multivariate normal observation densities 



The prior density of unobserved factors is formulated conditional on observed factors _Yt_ 

_π_ ( _F_<sup>_∗_</sup> _|Y_<sup>_T_</sup> _, θ_ ) = _N_ (0 _,_ **F** 0) (11) 

where **F**<sup>_−_</sup> 0<sup>1</sup> = **Φ**<sup>_f′_</sup> **Σ**<sup>_−_</sup> _f_<sup>1</sup><sup>**Φ**</sup><sup>_f_,with</sup><sup>**Φ**</sup><sup>_f_and</sup><sup>**Σ**</sup><sup>_f_appropriatelybandedmatrices,seesec-</sup> tion 3.3. For the model parameters, we assume independent priors 



The hierarchical sparse prior distribution _π_ ( _λ_<sup>_∗_</sup> _|ϑ_ ) _π_ ( _ϑ_ ) is given in (2)-(4). Except for Σ<sup>_∗_allremainingparametershavestandardpriordistributions,seeappendix</sup> _f_<sup>,</sup> A. As discussed in section 2.3, our identication scheme treats Σ<sup>_∗_</sup> _f_<sup>ascorrelation</sup> 

> 2An alternative is to assess model identication while estimating the model by checking at the end of each iteration of the sampler whether the sampled factor loading matrix, which maybe has to be appropriately re-ordered by factors and by variables, fullls standard identication criteria (Anderson and Rubin 1956, Geweke and Zhou 1996, Bai and Wang 2014). 

7 

matrix, i.e. with 1s on the diagonal and unrestricted otherwise. Instead of dening a prior distribution for the correlation matrix, which is not trivial, we use parameter extension as proposed in Conti et al. (2014). Dening the working parameter _V_ , a _k × k_ non-singular diagonal matrix, we expand the correlation matrix to a regular <u>1 1</u> covariance matrix Σ<sup>ˆ</sup> _f_ = _V_ 2 Σ<sup>_∗_</sup> _f_<sup>_V_</sup> 2 , which allows us to formulate a conjugate inverse Wishart prior distribution _π_ ˆΣ _f |Sf ∼ IW_ ( _νf , Sf_ ) . � � 

### 3.2 Posterior sampler 

To obtain a sample from the posterior distribution 



we repeatedly draw from: 

(i) the sparse posterior of factor loadings _π_ � _λ_<sup>_f∗_</sup> _, λ_<sup>_∗Y_</sup> _|X_<sup>_T_</sup> _, Y_<sup>_T_</sup> _, F_<sup>_∗_</sup> _,_ **Ψ** _,_ Ω� , and update the hyperparameters _π_ ( _ϑ|λ_<sup>_∗f_</sup> _, λ_<sup>_∗Y_</sup> ) , (ii) the posterior of factors: _π_ � _F_<sup>_∗_</sup> _|X_<sup>_T_</sup> _, Y_<sup>_T_</sup> _, θ_ � (iii) the posterior distribution of model parameters _π_ � **Φ**<sup>**_∗_**</sup> _,_ **Ψ** _,_ Ω _,_ Σ<sup>_∗_</sup> _f_<sup>_,_Σ</sup><sup>_Y |XT , YT , F ∗, λ∗f, λ∗Y_�</sup> , 

and 

(iv) permute factor position and signs. 

Most of the posterior distributions for model parameters are standard and derived in detail in appendix B. Given the new proposal to estimate factors parametrically in the FAVAR framework, we briey expose the sampler in the following section. 

### 3.3 Sampling the factors 

To draw from the posterior of factors in (ii), _π_ ( _F_<sup>_∗_</sup> _|X_<sup>_T_</sup> _, Y_<sup>_T_</sup> _, θ_ ) we rst condition on observed variables _Yt_ : 



where _µf ∗|Y t−_ 1 = Φ<sup>_∗_</sup> 1<sup>_fY_</sup> _Yt−_ 1 + _..._ + Φ<sup>_∗_</sup> _p_<sup>_fY_</sup> _Yt−p_ . Then, we condense the conditional system: 



where _⊙_ and _⊗_ represent the Hadamar and the Kronecker product, respectively. **1** 1 _×k_ is a row vector containing _k_ ones as elements. Stack all observations to obtain the matrix representation 



8 

˜ _′_ ¯ _′_ where **X**<sup>**˜**</sup> = � _Xq_<sup>_′_</sup> +1<sup>_, . . . ,X_˜</sup> _T_<sup>_′_</sup> � contains all data, _F_<sup>¯</sup> = � _fq_<sup>_′_</sup> +1 _−_ max( _p,q_ )<sup>_, . . . ,f_¯</sup> _q_<sup>_′_</sup> +1<sup>_, . . . ,f_¯</sup> _T_<sup>_′_</sup> � stacks all unobserved factors, including initial states. The matrices **Λ**<sup>_f_</sup> and **Φ**<sup>_f_</sup> are respectively of dimension ( _T − q_ ) _N ×_ ( _T_ + _d_ ) _k_ and square ( _T_ + _d_ ) _k_ , with _d_ = ( _p − q_ ) _I {p > q}_ . Typically, these matrices are sparse and banded around the main diagonal (Chan and Jeliazkov 2009) 



where Σ _f_ 0 represents the variance of the initial states of the unobserved factors (see appendix B.2). 

Combining the prior (11) with the likelihood _π_ ( **_X_**<sup>**˜**</sup> _|F, θ_<sup>¯</sup> ) _∼ N_ ( **Λ**<sup>_f_</sup> _F, I_<sup>¯</sup> _T −q ⊗_ Ω) we obtain the posterior distribution 



In order to avoid the full inversion of **F** we take the Cholesky decomposition, **F**<sup>_−_1</sup> = _L_<sup>_′_</sup> _L_ , then **F** = _L_<sup>_−_1</sup> _L_<sup>_−_1</sup><sup>_′_</sup> . We obtain a draw _F_<sup>¯</sup> by setting _F_<sup>¯</sup> = **_µ_** _f_ ¯ + _L_<sup>_−_1</sup> **_ν_** , where **_ν_** is a ( _T_ + _d_ ) _k_ vector of independent draws from the standard normal distribution. We retrieve a draw _F_<sup>_∗_</sup> by adding back the conditional mean to _f_<sup>¯</sup> _t_ , _ft_<sup>_∗_=</sup><sup>_f_¯</sup><sup>_t_+</sup><sup>_µ_</sup> _f_<sup>_∗_</sup> _|Y_<sup>_t−_1.</sup> Model estimation does not identify factor position and factor sign. Given that we formulate a factor-invariant prior distribution on the loadings and on the factorspecic parameters, the prior is invariant with respect to factor ordering and sign. Therefore, the posterior (13) will also be invariant with respect to factor and sign permutations _ρ_ ( _·_ ) , _π_ � _F_<sup>_∗_</sup> _, θ|X_<sup>_T_</sup> _, Y_<sup>_T_�</sup> = _π_ � _ρ_ ( _F_<sup>_∗_</sup> _, θ_ ) _|X_<sup>_T_</sup> _, Y_<sup>_T_�</sup> . To explore the full unconditional distribution, we apply random permutation of factor order and factor sign at the end of each sampler sweep (Frühwirth-Schnatter 2001). The posterior output will have 2<sup>_k_</sup> _k_ ! modes. We identify factor order and sign ex-post by sorting out the multimodal posterior output, see the next section. 

### 3.4 Ex post mode identication 

Model estimation yields _G_ draws out of the multimodal posterior distribution. Postprocessing the draws denes factor position and factor sign. We proceed as in 

9 

Kaufmann and Schumacher (2013, section 3.3) who suggest to identify factor position based on the posterior draws of the factors rather than using the loadings as usually done in the literature. 

In brief, we rst identify _κ_ relevant factor representatives, _f_<sup>_∗c_</sup> , _c_ = 1 _, . . . , κ_ , which form the basis to identify factor positions. To determine factor representatives, we form clusters of highly correlated (in absolute terms) factor draws. From those clusters which contain a signicant number of draws, say e.g. 0 _._ 9 _G_ draws, we estimate a factor representative by the mean of the (sign-adjusted) clustered draws. 

The intuition behind the procedure is the following. Assume that all _k_ factors in the estimated model are relevant, i.e. model estimation is not overtting the number of factors. Then, the posterior output should contain _G_ posterior draws for each of the _k_ factors, whereby the respective _G_ draws should be relatively highly correlated. Therefore, we should be able to identify _κ_ = _k_ factor representatives. On the other hand, if an estimated model is overtting the number of factors, _k > k_<sup>_true_</sup> , then _G_ ( _k − k_<sup>_true_</sup> ) factor draws will be sampled out of the prior, given that the data are uninformative for the _k − k_<sup>_true_</sup> redundant factors. At most, these _G_ ( _k − k_<sup>_true_</sup> ) factor draws would be loosely correlated. The clustering procedure will then identify _κ < k_ factor representatives. 

After determining the factor representatives, we then re-order each posterior draw according to maximum correlation with the _κ_ factor representatives. Concretely, we determine the permutation _ϱ_<sup>(</sup><sup>_g_)</sup> = ( _ϱ_<sup>(</sup> 1<sup>_g_)</sup><sup>_, . . . , ϱ_(</sup> _k_<sup>_g_))of</sup><sup>_{_1</sup><sup>_, . . . , k}_for draw</sup><sup>_g_= 1</sup><sup>_, . . . , G_:</sup> 



where _fj_<sup>_∗_(</sup><sup>_g_)</sup> = ( _fj_<sup>_∗_</sup> 1<sup>(</sup><sup>_g_)</sup><sup>_, . . . , f_</sup> _jT_<sup>_∗_(</sup><sup>_g_))</sup><sup>_′_represents the</sup><sup>_g_th draw of the</sup><sup>_j_th factor.If</sup><sup>_ϱ_(</sup><sup>_g_)is a</sup> unique permutation of _{_ 1 _, . . . , k}_ , we retain draw _g_ for posterior inference. The permutation is applied as detailed in Kaufmann and Schumacher (2013, equation (10)) to factors, factor loadings _λ_<sup>_∗f_</sup> and factor-specic parameters and hyperparameters. The permutation step is completed by sign-permuting each factor draw negatively correlated to the factor representative. Appropriate sign-adjustment also applies to factor loadings _λ_<sup>_∗f_</sup> and dynamic parameters **Φ**<sup>_∗_</sup> . The permutation step is slightly adjusted in case we identify fewer factor representatives than estimated factors, i.e. _κ < k_ . This is an indication that the model may be re-estimated conditional on a lower number of factors. Nevertheless, we may perform posterior inference on the _κ_ relevant factors. In this case, permutation (19) is re-dened. After determining _ϱ_<sup>(</sup><sup>_g_)</sup> as in (19), the factor draws lowest correlated with factor representatives are ranked last, in no specic order, _ϱ_<sup>(</sup><sup>_g_)</sup> := � _ϱ_<sup>(</sup><sup>_g_)</sup> _, {_ 1 _, . . . , k} \ ϱ_<sup>(</sup><sup>_g_)�</sup> . 

## 4 Application to the US economy 

In this section, we apply our methodology to a large panel of series for the US economy to illustrate estimation and identication of the sparse FAVAR. We nd evidence for a high degree of sparsity and indeed, given the structure of estimated zero loadings, we achieve model identication. In addition to one observed factor, 

10 

i.e. the federal funds rate (FFR), we estimate seven unobserved factors. The variance share explained by the common component amounts to 52 percent. Further, we perform a structural analysis to study how structural shocks like a monetary policy shock or a productivity shock aect the economy. Against the background of estimating an unrestricted factor error covariance matrix, this exercise illustrates how to apply traditional structural identication schemes to the sparse FAVAR model. The FAVAR oers an advantage over small scale VAR models in that it allows us to include much more information and to extend the analysis to a much broader set of variables. 

### 4.1 Data and prior specication 

We work with the FRED-QD database available for download from the website of the Federal Reserve Bank of St. Louis. The data is a quarterly companion to the Monthly Database for Macroeconomic Research (FRED-MD) assembled by McCracken and Ng (2015). It consists of 253 macroeconomic time series for the US economy which are regularly updated and reported at a quarterly frequency starting in 1959Q1. The FRED-QD database has been constructed along the lines of the data set used in Stock and Watson (2012). In addition, we include the utilization adjusted total factor productivity (TFP) series from Fernald (2012). In our analysis, we focus on the period 1965Q1 - 2015Q2 and drop the series with missing observations, which leaves us with 224 variables in total.<sup>3</sup> Where necessary, series are transformed to nontrending series by applying rst dierences either to logs or to levels. For an easier understanding of the results and given our Bayesian estimation setup, we depart from the transformations suggested in FRED-QD and avoid second dierences. A complete list with all included series and performed transformations is available in appendix F. 

Following BBE05 we treat the FFR as the only observed factor, given its role as a policy instrument and the fact that it is observed without error. The preferred specication sets the number of unobserved factors to _k_ = 7 , which seems to capture quite well the structure of the underlying data. The choice of _k_ is justied in various ways. First, _k_ = 7 mirrors well the number of groups into which the series may be classied, like e.g. economic activity variables, prices, interest rates and so on. Second, the average variance share explained by the common component lies above 50 percent and does not increase substantially any more when increasing the number of unobserved factors, see gure 11 in appendix E. As a last device, we apply the eigenvalue-ratio based criterion proposed by Lam and Yao (2012). The right panel of gure 11 in appendix E shows that the minimum ratio is at ( _k_ +1) = 2 . However, there are further local minima at 5, 8 and 11, which indicates that next to two strong factors there is evidence for additional weaker factors. Taking this all together, evidence for setting _k_ = 7 seems pretty strong. 

The parametrization for the prior distributions is listed in table 1. For the two layer sparse prior we set the mean _s_ 0 = 0 _._ 35 , the precision _r_ 0 = 200 .<sup>4</sup> We allow 

> 3The series with missing observations stem from various larger groups of series. After removing them, each group keeps a representative number of series. Therefore, we expect no signicant data information loss by removing series with missing observations. 

> 4Changing the prior degree of sparsity has almost no inuence on the results. As expected, a higher sparsity degree slightly increases the number of estimated zero elements in _λ_<sup>_∗_</sup> , but leaves the results qualitatively unchanged. 

11 

for two lags in the dynamics of the factors as well as the idiosyncratic components, _p_ = _q_ = 2 .<sup>5</sup> The sampler converges quickly, we draw 8000 times from the posterior, discard the rst 3000, and retain every second one. We are left with _G_ = 2500 draws to perform posterior inference. 

### 4.2 Results 

Figure 1 shows a heatmap of the mean posterior probabilities of a non-zero factor loading.<sup>6</sup> It nicely reveals the sparsity in the data. While for some variables the probability of loading on a given factor is high (red entries) there are also a lot of zero elements in the factor loading matrix (white entries). To create this gure, the factors have rst been ordered in decreasing order of the number of non-zero factor loadings. In addition, the variables have been reordered such that variables loading only on the rst factor (with probability larger than 0.5) are ordered rst, followed by those that load only on factor 2 and on factors 1 and 2 and so on. In doing so, we get a generalized lower triangular structure, which reveals that the structure of the estimated factor loading matrix yields an identied model. 



Figure 1: Posterior probabilities of non-zero factor loading. 

The estimated sparse factor loading matrix yields a clear economic interpretation for all seven unobserved factors. Figure 2 plots the posterior mean estimates of the 7 unobserved factors along with the 68 percent highest posterior density interval<sup>7</sup> (HPDI) and the FFR as well. The rst three latent factors are all related to the real part of the economy. The rst factor represents production as it loads on production and output series like real GDP, real investment, industrial production measures, manufacturing sales as well as new orders for durable manufacturing 

> 5Again, increasing the number of lags does not alter the results as the coecient estimates for _p, q >_ 2 are close to zero. 

> 6It is computed as the average number of nonzero draws for _λ∗ij_<sup>,</sup><sup>_P_(</sup><sup>_λ∗_</sup> _ij_<sup>= 0</sup><sup>_|·_) =</sup> _G_<sup><u>1</u></sup> � _Gg_ =1<sup>_I{λ_(</sup> _ij_<sup>_g_)= 0</sup><sup>_}_.</sup> 

> 7This applies to all plots of impulse responses if not stated otherwise. 

12 

goods. It further loads on real consumption expenditures as well as various employment and unemployment variables. The second unobserved factor is positively correlated to the rst factor. We interpret it as employment factor given that it mostly loads on employment and unemployment data, including employees in dierent sectors, the unemployment rate and hours worked. Further, it positively loads on some credit variables such as consumer loans as well as commercial and industrial loans, indicating that credit is co-moving with employment. The third latent factor represents the housing market. It mostly loads on variables like building permits and housing starts. In addition, it is informative for stock market variables. The fourth and the fth factor capture nominal features of the US economy. While the fourth factor loads mostly on consumer price ination series, the fth factor takes up producer price ination series as well as energy price ination such as the changes of the oil price. The sixth factor loads on interest rates and partly explains spreads between long and short term interest rates. It happens to be highly correlated with measures of the term premium for government bonds as computed in Adrian et al. (2013). Therefore, we interpret it as a term premium factor. To further motivate this interpretation, gure 3 plots the estimate of our term premium factor along with the 90 percent HPDI against dierent measures of the term premium for government bonds computed with the method of Adrian et al. (2013) and available on the website of the Federal Reserve Bank of New York. For expositional convenience, all series including the factor estimate have been standardized. Excluding the period 1965Q1 - 1969Q4, the correlations between the median estimate of the factor and the ve dierent measures are between 0.7 and 0.8. The last unobserved factor is taking up productivity, as it loads positively on TFP and on real output per hour as well. It also loads negatively on unit labor costs and positively on several measures of output. Finally, the FFR explains a large fraction of co-movement between interest rates. Table 3 lists those series most correlated with each factor. According to these, we obtain essentially the same interpretation for factors as just given. 

Despite the small number of factors, the common component explains on average more than 50 percent of data variation. Table 2 shows the variance share explained by the common component for some selected variables from seven dierent groups, the number shown is the median over all MCMC draws. The model does a good job in explaining real GDP and industrial production growth. The common component accounts for 99 and 95 percent of, respectively, GDP growth and industrial production growth variation. The common component further explains 56 percent of the variance in real consumption expenditures and 37 percent of TFP variation. However, the factors do a poor job in explaining capacity utilization in the manufacturing sector (CUMFNS), for which more than 90 percent of variance remains unexplained. The common component also accounts for a large variance share in employment variables but government employees. However, this is not surprising, as the number of government employees is not expected to highly correlate with the economic situation. Overall, the common component accounts for a large share of variance in variables linked to the housing market, to sales, prices as well as interest rates. On the other hand, the common component explains only a minor share of variance in variables of the nancial sector such as loans or stock market prices, which indicates that additional driving forces are captured by the idiosyncratic component. 

13 



<!-- Start of picture text -->
Production Employment<br>4 10<br>2<br>0 0<br>-2<br>-4 -10<br>-6<br>-8 -20<br>1965:3 1975:3 1985:3 1995:3 2005:3 1965:3 1975:3 1985:3 1995:3 2005:3<br>Housing Cons. Prices<br>5 10<br>5<br>0<br>0<br>-5<br>-5<br>1965:3 1975:3 1985:3 1995:3 2005:3 1965:3 1975:3 1985:3 1995:3 2005:3<br>Prod. Prices Term Premium<br>2<br>5<br>0<br>-2<br>0<br>-4<br>-6<br>-8 -5<br>1965:3 1975:3 1985:3 1995:3 2005:3 1965:3 1975:3 1985:3 1995:3 2005:3<br>Productivity FFR<br>4<br>15<br>2<br>10<br>0<br>5<br>-2<br>0<br>1965:3 1975:3 1985:3 1995:3 2005:3 1965:3 1975:3 1985:3 1995:3 2005:3<br><!-- End of picture text -->

Figure 2: Estimated unobserved factors. 

### 4.3 Monetary policy 

One of the main reasons why BBE05 proposed to combine the VAR methodology with factor analysis was the probable lack of important information in a small scale VAR to obtain structural identication of e.g. monetary policy shocks. A well known example is the price puzzle, i.e. the positive reaction of ination in response to an unexpected interest rate hike. According to Sims (1992), a rationale for the price puzzle may be that the policy maker's information set includes more variables of high forecasting power than the econometrician's small VAR does. Another rationale is given by Giordani (2004), who thinks that biased measures of the output gap may lead to a price puzzle. Since the FFR is the only included observed factor and given that we assume independence between innovations in unobserved and observed factors, _ηt_<sup>_Y_</sup> can be interpreted as a monetary policy shock. Unanticipated changes in the FFR do not 

14 



<!-- Start of picture text -->
4<br>ACMTP01<br>ACMTP03<br>ACMTP05<br>ACMTP08<br>3 ACMTP10<br>2<br>1<br>0<br>-1<br>-2<br>-3<br>1965:3 1970:3 1975:3 1980:3 1985:3 1990:3 1995:3 2000:3 2005:3 2010:3<br><!-- End of picture text -->

Figure 3: Factor 6 and term premia 

aect any of the unobserved factors on impact, at the same time the FFR does not respond contemporaneously to innovations in the unobserved factors. In that sense the identication scheme here is somewhat more restrictive than the often used recursive Cholesky restrictions, as they allow for a contemporaneous response of the FFR to other innovations. However, we do not expect that this artefact stemming from the factor identication will have a dramatic impact on the results. We exploit our data rich model to study how these monetary policy shocks aect the rest of the economy. Figure 4 plots the impulse response functions of the estimated factors to a monetary policy shock. First, we note that the shock to the FFR (factor 8) dies out gradually over time. Factors 1 to 3, i.e. the production, employment and housing factors, all show an inverse humped shaped pattern. As expected, an increase in the FFR leads to a transitory slowdown in economic activity. The eect on the two price factors (factors 4 and 5) is positive on impact. So, even though our model includes a broad range of information, the price puzzle still remains. It takes three to ve quarters until the eect turns quite persistently negative. Compared to other factors, the uncertainty surrounding the impulse response function of the consumer price factor turns out to be much higher. We further observe that the response of producer and energy prices falls more rapidly into negative territory and dies out more quickly than the response of consumer prices. This indicates that consumer prices are somewhat stickier than producer and energy prices. The productivity factor does not show a strong reaction in response to the monetary policy shock. 

Figure 5 plots the impulse responses to a FFR shock for some selected variables along with the 68 percent HPDI. Clearly, an interest rate hike has an adverse eect on economic activity and leads to a temporary decrease in industrial production. The eect dies out after about 15 quarters. For consumer as well as producer prices the short term eect is positive, the median response (black line) falls below zero only after several quarters. However the negative eect is only signicant for producer prices. The response of the ve year government bond yield indicates that a hike in 

15 



<!-- Start of picture text -->
0.1 Production 0.5 Employment 0.2 Housing 0.2 Cons. Prices<br>0 0<br>0 0<br>-0.1 -0.2<br>-0.5 -0.2<br>-0.2 -0.4<br>-0.3 -1 -0.6 -0.4<br>0 20 40 0 20 40 0 20 40 0 20 40<br>0.2 Prod. Prices 0.4 Term Premium 0.1 Productivity 1.5 FFR<br>0.05 1<br>0.1 0.2<br>0 0.5<br>0 0<br>-0.05 0<br>-0.1 -0.2 -0.1 -0.5<br>0 20 40 0 20 40 0 20 40 0 20 40<br><!-- End of picture text -->

Figure 4: Impulse responses of the factors to an unanticipated change in the FFR. 

the FFR also translates into a persistent increase in longer term interest rates. The negative eect on both the monetary base and M2 reects a liquidity eect. Figure 14 in the appendix contains the shares of forecast error variance (FEV) explained by the monetary policy shock for the same eight variables. The shares are highest for the three interest rates, while the shock explains relatively small portions of the variance of the remaining series. 

16 



<!-- Start of picture text -->
FFR IP CPI PPI<br>1.5 0.5 0.5 0.5<br>0<br>1 0<br>0<br>-0.5<br>0.5 -0.5<br>-1<br>-0.5<br>0 -1<br>-1.5<br>-0.5 -1 -2 -1.5<br>0 20 40 0 20 40 0 20 40 0 20 40<br>5y TBills M2 3m TBills<br>0.2 0.4 Monetary Base 1 0.3<br>0.15 0.2<br>0.5 0.2<br>0.1 0<br>0 0.1<br>0.05 -0.2<br>-0.5 0<br>0 -0.4<br>-0.05 -0.6 -1 -0.1<br>0 20 40 0 20 40 0 20 40 0 20 40<br><!-- End of picture text -->

Figure 5: Impulse responses of selected variables to an unanticipated change in the FFR. 



<!-- Start of picture text -->
PCED PCE LFE CPI<br>1 1 0.5<br>0<br>0 0<br>-0.5<br>-1 -1<br>-1<br>-2 -2<br>-1.5<br>-3 -3 -2<br>0 20 40 0 20 40 0 20 40<br>PPIACO Commodity Prices S&P500<br>0.5 0.1 0.2<br>0<br>0<br>0<br>-0.1<br>-0.5<br>-0.2<br>-0.2<br>-1<br>-0.3<br>-1.5 -0.4 -0.4<br>0 20 40 0 20 40 0 20 40<br><!-- End of picture text -->

Figure 6: Impulse responses of selected price variables to an unanticipated change in the FFR. 

17 

Considering that the price puzzle is still present in the estimates, we may evaluate the responses of other price ination series to a FFR shock. Figure 6 plots the impulse responses for six selected price indices. The upper panel contains the responses of three dierent measures of consumer prices, namely the personal consumption expenditures (PCED), PCED excluding food and energy (PCE LFE) and, for comparison, the consumer price index reproduced from gure 5. While the eect of a FFR increase on the CPI is strongly positive in the short run, this is less the case for the other two series. Nevertheless, they have in common that it takes a while (again several quarters) until the median response reaches negative territory. The lower panel of gure 6 plots the impulse responses of producer prices (PPIACO), commodity prices and the S&P 500. While the reaction of producer prices is similar to those of consumer prices, commodity prices take a shorter time to contract. The response of stock prices is typical for a FFR shock. They considerably fall on impact and follow an inverted hump shaped pattern. Our results stand in contrast to those of Baumeister et al. (2013), who do not report a price puzzle for aggregate price level measures. Their model allows for time varying parameters and is estimated over a shorter sample period which excludes recent years. Figure 12 in appendix E reveals that the positive response of prices is partly linked to the great recession, during which interest rates were lowered to the zero lower bound. We plot the same impulse responses obtained when the model is estimated with data ending in 2007Q2. We observe that prices still take a while to decrease after a FFR hike, but only CPI still shows a slight positive reaction in the short run. This may reect some degree of time variation in price responses to FFR shocks. Given the recent introduction of unconventional monetary policy measures, this instability does not come as a big surprise. It is further interesting to note that the response of the S&P 500 is also quite dierent when the model is estimated without the great recession. In this case the negative eect of an interest rate hike is much weaker compared to the full sample estimation, and at a longer horizon the median response stays persistently on a positive level. This points towards a much stronger reaction of stock markets to monetary policy shocks during and after the nancial crisis. 

An alternative explanation for the observed price puzzle would be that our identied monetary policy shocks are in fact no monetary policy shocks. To check this we compare our identied shock series to the monetary shock measure of Romer and Romer (2004), and nd a considerable similarity between the two series for the available time period<sup>8</sup> . Figure 13 in the Appendix plots the two measures against each other over the available time span of the original Romer and Romer data, the estimated correlation coecient between the series is 0.63. Our identied shock series seems to be consistent with their ndings. 

Given that the FFR is the monetary policy instrument and the observed factor in the FAVAR, we are implicitly estimating a reaction function for monetary policy and can compute a prediction of the FFR conditional on the observed data. The prediction can be seen as a sort of Taylor interest rate implied by the model<sup>9</sup> . Figure 7 plots the prediction for the FFR along with the actual values (in blue). The plot reveals some interesting insights. First, during the late 1970s, the actual FFR lies clearly below our estimate, indicating that monetary policy has been relatively 

> 8We took the original series that covers the time span from March 1969 to December 1996 and converted it to quarterly data. 

> 9In analogy to the interest rate feedback rule proposed in Taylor (1993). 

18 



<!-- Start of picture text -->
20<br>15<br>10<br>5<br>0<br>-5<br>-10<br>1965:3 1970:3 1975:3 1980:3 1985:3 1990:3 1995:3 2000:3 2005:3 2010:3<br><!-- End of picture text -->

Figure 7: Predicted FFR along with actual values. 

loose during that period. At the beginning of the 1980s during the Volcker era, the opposite is true. During this period, relative to the model based interest rate monetary policy was tight in order to ght against high ination rates. Otherwise, the dierences between the predicted and the actual value remain small, although there is a tendency for the actual value to exceed the former during boom phases. This is particularly the case in 2005 before the beginning of the nancial crisis. We also see how monetary policy has been trapped at the lower bound after the outbreak of the great recession. The model based prediction of the FFR dives deep into negative territory in response to the nancial crisis, but also shows a much earlier and faster tapering thereafter. 

### 4.4 Term premium shock 

We suggested that one of the identied unobserved factors seems to be special as it mainly loads on interest rate spreads and highly correlates with measures of the term premium, see gure 3. To get a better understanding of its role, we identify a structural shock that only aects the term premium factor on impact, leaving the other factors unaected. 

A shock to the term premium factor leads to pro-cyclical responses in GDP, consumption, investment, housing, employment and hours worked, see gures 8 and 9. Consumer as well as producer prices fall in response to this shock, while stock prices increase. Consumer condence measured by the University of Michigan's consumer sentiment index increases, while the VOX volatility index falls. The spread of the 10 year government bond over the 3 month treasury bills increases as the bond return increases more strongly. In gure 9, we observe that the spread between 1 year and 3 month treasuries also transitorily increases. The spread between Moody's seasoned BAA corporate bond yield and the return on 10 year treasuries falls, which indicates a higher risk appetite of investors. We further observe an increase in the amount of total outstanding consumer credit, the same is true for commercial and 

19 

industrial loans. TFP is unaected on impact, which is by construction so. Then, it starts increasing as well. 

The impulse responses of consumption, TFP, CPI and the spread between long and short term interest rates to the term premium shock closely mirror those of a slope shock in Kurmann and Otrok (2013) (KO13 henceforth). In KO13 the slope shock is identied as the shock that maximizes the FEV of the slope of the term structure. Both their and our shock lead to similar impulse responses of key macroeconomic variables, which seems quite natural as the slope of the term structure and our term premium factor capture the same economic concept linked to expectations about the future state of the economy. KO13 point out the strong similarities between the impulse responses of a TFP news shock<sup>10</sup> and a slope shock, which leads them to conclude that the main driver of movements in the slope of the term structure are in fact TFP news shocks. Further, for this observation they assign a key role to the endogenous response of monetary policy "...the news shock seems to be a major determinant of movements in the slope through its inuence on monetary policy at the short end of the term structure." (KO13 p. 2623). In their impulse responses, the increase in the spread results from a decrease in short term interest rates while long term interest rates barely move. In contrast, our impulse responses document an increase in both short term and long term interest rates, whereby the latter react more strongly. Hence, our ndings show that an unanticipated shock that also leads to a change at the longer end of the term structure can produce the same responses of key macroeconomic variables as in KO13. Economically, an increase of interest rates in response to a news shock is also plausible. In anticipation of a future technology shock consumption starts to increase, which might put savings under pressure and lead to an increase in interest rates. 

### 4.5 Identication of interpretable shocks 

Sparsity in the factor loading matrix helps identifying and interpreting factors and factor innovations in FAVAR models. However, we may want to identify a shock in the factor VAR that acts as the main driver of a certain variable in the underlying data set. For this, we can rely on the method proposed by Uhlig (2004) which identies an orthogonal shock based on the explained fraction of the FEV of a given variable. Concretely, the method determines the impact eects of a shock that maximizes the FEV of the variable of interest over a given forecast horizon. This identication strategy can easily be adapted to the FAVAR framework, in which the observed variables do not enter the VAR directly, see appendix C for computational details. To illustrate the method, we identify a technology shock as the main driver of TFP, i.e. the shock which accounts for the highest fraction of the FEV of TFP at a horizon up to four quarters. The identied shock permanently raises TFP, see gure 10. The shock leads to a permanent increase in GDP and a permanent decrease in the CPI. Interestingly, total hours worked fall on impact as higher productivity seems to lower the demand for labor. Consumption increases quite persistently, the eect dying out only slowly. Interest rates fall gradually, while the spread between long and short term interest rates increases slightly in response to a technology shock. The impulse response of hours worked are in line with ndings in Gali (1999). They nd that the conditional correlations of hours worked and productivity are negative 

> 10KO13 identify the TFP news shock along the lines of Barsky and Sims (2011) in a VAR framework. 

20 



<!-- Start of picture text -->
GDP Consumption Hours CPI<br>1.2 1.2 1.4 0<br>1 1 1.2<br>1 -0.5<br>0.8 0.8<br>0.8<br>0.6 0.6<br>0.6 -1<br>0.4 0.4<br>0.4<br>0.2 0.2<br>0.2 -1.5<br>0 0 0<br>-0.2 -0.2 -0.2 -2<br>0 20 40 0 20 40 0 20 40 0 20 40<br>S&P500 Cons. Confidence VOX Spread 10y-3m<br>0.5 0.06 0.06 0.25<br>0.4 0.05 0.04 0.2<br>0.04 0.15<br>0.3 0.02<br>0.03 0.1<br>0.2 0<br>0.02 0.05<br>0.1 -0.02<br>0.01 0<br>0 0 -0.04 -0.05<br>-0.1 -0.01 -0.06 -0.1<br>0 20 40 0 20 40 0 20 40 0 20 40<br><!-- End of picture text -->

Figure 8: Impulse Responses of selected variables to an unanticipated change in the term premium. 



<!-- Start of picture text -->
Spread 1y-3m Spread BAA Housing Investment<br>0.5 0.05 0.8 1<br>0.4 0.8<br>0 0.6<br>0.3 0.6<br>-0.05 0.4<br>0.2 0.4<br>-0.1 0.2<br>0.1 0.2<br>-0.15 0<br>0 0<br>-0.1 -0.2 -0.2 -0.2<br>0 20 40 0 20 40 0 20 40 0 20 40<br>TFP Cons. Loans 3m T-Yields 10y T-Yields<br>0.6 1.4 0.08 0.2<br>0.5 1.2 0.06<br>0.15<br>1<br>0.4<br>0.04<br>0.3 0.8 0.1<br>0.6 0.02<br>0.2 0.4 0.05<br>0<br>0.1<br>0.2<br>0<br>0 0 -0.02<br>-0.1 -0.2 -0.04 -0.05<br>0 20 40 0 20 40 0 20 40 0 20 40<br><!-- End of picture text -->

Figure 9: Impulse Responses of selected variables to an unanticipated change in the term premium. 

21 

for technology shocks and that hours worked show a persistent decline in response to a positive technology shock. The technology shock explains almost all the FEV of TFP up to a horizon of 40 quarters and nearly 30 percent of the FEV of GDP (see gure 15 in the Appendix). 



<!-- Start of picture text -->
FFR Hours Consumption GDP<br>0.2 0.2 0.5 0.8<br>0.1 0.4<br>0 0.6<br>0 0.3<br>-0.2 0.4<br>-0.1 0.2<br>-0.4 0.2<br>-0.2 0.1<br>-0.3 -0.6 0 0<br>0 20 40 0 20 40 0 20 40 0 20 40<br>CPI Spread 5y TBills TFP<br>1 0.1 0.05 0.8<br>0 0.6<br>0.05 0<br>-1 0.4<br>0 -0.05<br>-2 0.2<br>-3 -0.05 -0.1 0<br>0 20 40 0 20 40 0 20 40 0 20 40<br><!-- End of picture text -->

Figure 10: Impulse responses of selected variables to a technology shock. 

22 

## 5 Conclusion 

In the present paper we combine the FAVAR framework with the estimation and identication procedures for sparse dynamic factor models. Sparse factor models are widely used in other elds and we think they are very valuable to analyze economic data. Introducing sparsity in the context of FAVAR provides one solution to the identication problem common to all factor models. It further allows us to assign a meaningful economic interpretation to the identied factors due to the sparse structure in the factor loading matrix. An additional distinction to traditional factor models is that we depart from the strong assumption of orthogonal common shocks and work with correlated factor shocks instead. This allows us to identify structural shocks using dierent strategies that have been proposed in the structural VAR literature. We apply our methodology to an empirical data set for the US macro economy (FRED QD) and nd that there is indeed a high degree of sparsity present in the data. The proposed estimation and identication procedure is successful in identifying seven unobserved factors representing production, employment, the housing market, consumer and producer prices, productivity and term premia. Together, they account for about 52 percent of variation in the data. We utilize the role of the FFR, the monetary policy instrument, as observed factor to study the eects of monetary policy on the economy. The estimated factors as well as specic variables all show reasonable responses to an unanticipated interest rate hike. However, we nd that the monetary policy shock exhibits a mild price puzzle which seems to be linked to the great recession, as it nearly vanishes when the period after 2007Q3 is excluded from the sample. One of the estimated unobserved factors is partly explaining the term premia in government bond yields. The impulse responses to an innovation in the term premium factor closely mirror those to the slope shock in KO13, and are in fact very similar to those of the news shock identied in Barsky and Sims (2011). However, the main dierence to KO13 is that in response to the term premium shock short and long term interest rates increase, whereas KO13 report a decrease in short term interest rates and no eect at the longer end of the yield curve. Finally, we identify the technology shock as the one which maximizes the explained fraction of FEV in TFP by adapting the methodology of Uhlig (2004) to the FAVAR environment. In line with the ndings in Gali (1999), the impulse response of hours to a technology shock decline and hence, show a negatively correlated reaction to TFP. 

## References 

- Adrian, T., R. K. Crump, and E. Moench (2013). Pricing the term structure with linear regressions. Journal of Financial Economics 110 (1), 110138. 

- Aguilar, O. and M. West (2010). Bayesian dynamic factor models and portfolio allocation. Journal of Business & Economic Statistics 18 (3), 338357. 

- Anderson, T. and H. Rubin (1956). Statistical inference in factor analysis. In J. Neyman (Ed.), Proceedings of the Third Berkeley Symposium on Mathematical Statistics and Probability, Volume 5: Contributions to Economectrics, Industrial Research, and Psychometry, pp. 111150. Berkeley, California: University of California Press. 

- Bai, J., K. Li, and L. Lu (2016). Estimation and inference of FAVAR models. 

23 

Journal of Business & Economic Statistics 34 (4), 620641. 

- Bai, J. and S. Ng (2008). Forecasting economic time series using targeted predictors. Journal of Econometrics 146, 304317. 

- Bai, J. and S. Ng (2013). Principal components estimation and identication of static factors. Journal of Econometrics 176, 1829. 

- Bai, J. and P. Wang (2014). Identication theory for high dimensional static and dynamic factor models. Journal of Econometrics 178, 794804. 

- Barsky, R. B. and E. R. Sims (2011). News shocks and business cycles. Journal of Monetary Economics 58 (3), 273289. 

- Baumeister, C., P. Liu, and H. Mumtaz (2013). Changes in the eects of monetary policy on disaggregate price dynamics. Journal of Economic Dynamics and Control 37, 543560. 

- Bernanke, B. S., J. Boivin, and P. Eliasz (2005). Measuring the eects of monetary policy: A factor-augmented vector autoregressive (FAVAR) approach. The Quarterly Journal of Economics 120 (February), 387422. 

- Boivin, J., M. Giannoni, and D. Stevanovi¢ (2016). Dynamic eects of credit shocks in a data-rich environment. mimeo. 

- Boivin, J. and M. P. Giannoni (2007). Global forces and monetary policy eectiveness. In J. Galí and M. Gertler (Eds.), International Dimensions of Monetary Policy, pp. 42978. Cambridge, MA: National Bureau of Economic Research. 

- Boivin, J., M. P. Giannoni, and I. Mihov (2009). Sticky prices and monetary policy: Evidence from disaggregated us data. American Economic Review 99, 35084. 

- Boivin, J., M. T. Kiley, and F. S. Mishkin (2011). How has the monetary transmission mechanism evolved over time? In B. M. Friedman and M. Woodford (Eds.), Handbook of Monetary Economics, Volume 3A, pp. 369422. Elsevier B.V. 

- Carvalho, C. M., J. Chang, J. E. Lucas, J. R. Nevins, W. Quanli, and M. West (2008). High-dimensional sparse factor modeling: Applications in gene expression genomics. Journal of the American Statistical Association 103, 14381456. 

- Chan, J. and I. Jeliazkov (2009). Ecient simulation and integrated likelihood estimation in state space models. International Journal of Mathematical Modelling and Numerical Optimisation 1 (1), 101120. 

- Conti, G., S. Frühwirth-Schnatter, J. J. Heckman, and R. Piatek (2014). Bayesian exploratory factor analysis. Journal of Econometrics 183 (1), 3157. 

- Fernald, J. (2012). A quarterly, utilization-adjusted series on total factor productivity. Federal Reserve Bank of San Francisco Working Paper Series . 

- Forni, M., M. Hallin, M. Lippi, and L. Reichlin (2001). Coincident and leading indicators for the euro area. The Economic Journal 111, C62C85. 

- Frühwirth-Schnatter, S. (2001). MCMC estimation of classical and dynamic switching and mixture models. Journal of the American Statistical Association 96, 194209. 

- Frühwirth-Schnatter, S. and H. F. Lopes (2010). Parsimonious Bayesian factor analysis when the number of factors is unknown. Technical report, The University of Chicago Booth School of Business. 

24 

- Gali, J. (1999). Technology, employment, and the business Cycle: Do technology shocks explain aggregate uctuations? American Economic Review 89 (1), 249271. 

- George, E. I. and R. E. McCulloch (1997). Approaches for Bayesian variable selection. Bayesian Statistics 5, 609620. 

- Geweke, J. and G. Zhou (1996). Measuring the pricing error of the arbitrage pricing theory. The Review of Financial Studies 9, 557587. 

- Giordani, P. (2004). An alternative explanation of the price puzzle. Journal of Monetary Economics 51 (6), 12711296. 

- Huang, A. and M. P. Wand (2013). Simple marginally noninformative prior distributions for covariance matrices. Bayesian Analysis 8 (2), 439452. 

- Kaufmann, S. and C. Schumacher (2013). Bayesian estimation of sparse dynamic factor models with order-independent identication. Study Center Gerzensee Working Paper 13.04. 

- Kaufmann, S. and C. Schumacher (2017). Identifying relevant and irrelevant variables in sparse factor models. Journal of Applied Econometrics, forthcoming. 

- Korobilis, D. (2013). Assessing the transmission of monetary policy using timevarying parameter dynamic factor models. Oxford Bulletin of Economics and Statistics 75, 157179. 

- Kurmann, A. and C. Otrok (2013). News shocks and the slope of the term structure of interest rates. American Economic Review 103 (6), 26122632. 

- Lam, C. and Q. Yao (2012). Factor modeling for high-dimensional time series: inference for the number of factors. The Annals of Statistics 40 (2), 694726. 

- Lawley, D. and A. Maxwell (1971). Factor analysis as a statistical method (Second edition ed.). London: Butterworth & Co (Publishers) Ltd. 

- Marcellino, M. and V. Sivec (2016). Monetary, scal and oil shocks: Evidence based on mixed frequency structural FAVARs. Journal of Econometrics, . 

- McCracken, M. W. and S. Ng (2015). FRED-MD: A monthly database for macroeconomic research. Working Paper 2015-012B . 

- Romer, C. D. and D. H. Romer (2004). A new measure of monetary shocks: Derivation and implications. American Economic Review 94 (4), 10551084. 

- Sims, C. A. (1992). Interpreting the macroeconomic time series facts: the eects of monetary policy. European Economic Review 36 (5), 9741011. 

- Stock, J. and M. Watson (1989). New indexes of coincident and leading economic indicators. In O. Blanchard and S. Fischer (Eds.), NBER Macroeconomics Annual, pp. 351409. Cambridge, Mass.: MIT Press. 

- Stock, J. and M. Watson (2002). Forecasting using principal components from a large number of predictors. Journal of the American Statistical Association 97 (460), 11671179. 

- Stock, J. and M. Watson (2012). Disentangling the channels of the 2007-2009 recession. NBER Working Paper Series 18094. 

- Taylor, J. B. (1993). Discretion practice versus policy rules in. Carnegie-Rochester Conference Series on Public Policy 39, 195214. 

- Uhlig, H. (2003). What moves real GNP? Unpublished Manuscript. Humbolt University, Berlin, 2003 . 

25 

- Uhlig, H. (2004). Do technology shocks lead to a fall in total hours worked? Journal of the European Economic Association 2 (2-3), 361371. 

- West, M. (2003). Bayesian factor regression models in the large p, small n paradigm. Bayesian Statistics 7, 723732. 

26 

## A Prior distributions 

The idiosyncratic components are independent. Therefore we formulate variablespecic prior distributions for _ψi_ = ( _ψi_ 1 _, . . . , ψiq_ )<sup>_′_</sup> and _ωi_<sup>2,</sup> 



where _I_ is an indicator function that takes on the value one if the roots of the _{·}_ characteristic polynomial of the underlying process lie outside the unit circle. 

For the factor autoregressive parameters _vec_ (Φ<sup>_∗′_</sup> ) , where Φ<sup>_∗_</sup> = [Φ<sup>_∗_</sup> 1<sup>_, . . . ,_Φ</sup><sup>_∗_</sup> _p_<sup>],we</sup> assume multivariate normal priors truncated to the stationary region 



We formulate an inverse Wishart prior on the error covariance matrix of observed variables _Yt_ , Σ _Y ∼ IW_ ( _νY , SY_ ) . 

## B Posterior distributions 

### B.1 The factor loadings _λ_<sup>_∗_</sup> 

To simplify notation let _λ_<sup>_∗_</sup> = [ _λ_<sup>_∗f_</sup> _λ_<sup>_∗Y_</sup> ] and _Ft_<sup>_∗_=[</sup><sup>_f_</sup> _t_<sup>_∗′_</sup> _Yt_<sup>_′_]</sup><sup>_′_.Therststepto</sup> get the posterior for the factor loadings _π_ ( _λ_<sup>_∗_</sup> _ij_<sup>_|F∗T , XT , YT ,_Ψ(</sup><sup>_L_)</sup><sup>_,_Ω)istointegrate</sup> out the variable specic prior probability of zero loading for each factor _j_ . The prior described above implies a common base rate of non-zero factor loading of _E_ ( _βij_ ) = _ρjb_ across variables. The marginal then becomes 



To isolate the eect of factor _j_ on variable _i_ we transform the variables to 



Now we combine the marginal prior with data to sample independently across i from 



with observation density _π_ ( _x_<sup>_∗_</sup> _it_<sup>_|·_) =</sup><sup>_N_(</sup><sup>_λ∗_</sup> _ij_<sup>_ψi_(</sup><sup>_L_)</sup><sup>_F_</sup> _jt_<sup>_∗, ω_</sup> _i_<sup>2)andwhere</sup> 



27 

To obtain the posterior odds _P_ ( _λ_<sup>_∗_</sup> _ij_<sup>= 0</sup><sup>_|·_)</sup><sup>_/P_(</sup><sup>_λ∗_</sup> _ij_<sup>= 0</sup><sup>_|·_)the prior odds of the non-zero</sup> factor loading are updated: 



Conditional on _λ_<sup>_∗_</sup> _ij_<sup>thevariablespecicprobabilities</sup><sup>_βij_areupdatedandsampled</sup> from _π_ ( _βij|λ_<sup>_∗_</sup> _ij_<sup>_, ·_).When</sup><sup>_λ∗_</sup> _ij_<sup>= 0</sup> 



That is, with posterior odds (1 _− b_ ) _ρj/_ (1 _− ρj_ ) we sample from _B_ ( _ab, a_ (1 _− b_ ) + 1) and set _βij_ equal to zero otherwise. Conditional on _λ_<sup>_∗_</sup> _ij_<sup>= 0weobtain</sup> 



In this case we sample _βij_ from _B_ ( _ab_ + 1 _, a_ (1 _− b_ )) . 

The posterior update of the hyperparameters _τj_ and _ρj_ is sampled from an inverse Gamma, _π_ ( _τj_ ) _|·_ ) _∼ IG_ ( _gj, Gj_ ) and a Beta distribution _π_ ( _ρj|·_ ) _∼ B_ ( _r_ 1 _j, r_ 2 _j_ ) , respectively, with 





where _Sj_ =<sup>�</sup><sup>_N_</sup> _i_ =1<sup>_I{β_</sup> _ij_<sup>=0</sup><sup>_}_</sup> 

### B.2 Sampling the factors: Covariance of initial states 

If Σ _f_ 0 in **Σ** _f_ is not chosen to be diuse, we may set it equal to the stationary variance. From the companion form of a VAR( _p_ ) process, _F_<sup>¯</sup> _t_ = **Φ**<sup>**˜**</sup><sup>_f_</sup> _F_<sup>¯</sup> _t−_ 1 + **_η_**<sup>_f_</sup> _t_<sup>,</sup> **_η_**<sup>_f_</sup> _t_<sup>_∼N_</sup> �0 _,_ � Σ _∗f_ 0 _k_ ( _p_ 0 _−k×_ 1) _k×_ ( _kpp−_ 1) �� , with 



_f f ′ f f ′_ we obtain _E_ ( _F_<sup>¯</sup> _tF_<sup>¯</sup> _t_<sup>_′_)=</sup><sup>**˜Φ**</sup> _E_ ( ¯ _Ft−_ 1 ¯ _F ′t−_ 1<sup>)</sup><sup>**˜Φ**</sup> + Σ **_η_** _f_ and Σ ¯ _F_ = **˜Φ** Σ ¯ _F_ **˜Φ** + Σ **_η_** _f_ . The vec operator yields 



from which we can retrieve the corresponding values for Σ _f_ 0 . 

28 

### B.3 The idiosyncratic components 

The posterior simulation of the parameters is divided in two blocks. The dynamics of the idiosyncratic components _ψi_ = ( _ψi_ 1 _, ..., ψiq_ )<sup>_′_</sup> are sampled individually. 



where 



The variance of the idiosyncratic component, _ωi_<sup>2,issimulatedfromindependent</sup> inverse Gamma distributions _IG_ ( _ui, Ui_ ) , _i_ = 1 _, ..., N_ with _ui_ = _u_ 0 + 0 _._ 5( _T − p_ ) and _Ui_ = _U_ 0 + 0 _._ 5( _X_<sup>˜</sup> _i − X_<sup>˜</sup> _i_<sup>_−ψi_)</sup><sup>_′_( ˜</sup><sup>_Xi −X_˜</sup> _i_<sup>_−ψi_).</sup> 

### B.4 The parameters for the factor dynamics 

The dynamics of the unobserved factors _ft_<sup>_∗_andobservedvariables</sup><sup>_Yt_arejointly</sup> sampled from 



where 



_′_ where _f_<sup>_∗_</sup> = � _Fp_<sup>_∗_</sup> +1<sup>_, . . . , F_</sup> _T_<sup>_∗_</sup> � and 



### B.5 The error covariance matrix of factors Σ<sup>_∗_</sup> 

We depart from the assumption of independent factor innovations and require only that the innovations of the unobserved factors be orthogonal to those of the observed ones. The two blocks Σ<sup>_∗_</sup> _f_<sup>andΣ</sup><sup>_Y_arethusfullmatrices.Whiletheelementsofthe</sup> latter are unrestricted, we set the diagonal elements of Σ<sup>_∗_</sup> _f_<sup>to one in order to normal-</sup> ize factor scale. Sampling Σ<sup>_∗_</sup> _f_<sup>isthusequivalenttosampleacorrelationmatrixfor</sup> the unobserved factors, for which we lack a standard distribution. Following Conti et al. (2014) we rely on marginal data augmentation techniques and temporarily expand the parameter space of the model with the variances of the unobserved latent 

29 

factors as working parameters when it comes to sampling Σ<sup>_∗_</sup> _f_<sup>.Usingthedecompo-</sup> <u>1 1</u> sition Σ<sup>ˆ</sup> _f_ = _V_ 2 Σ<sup>_∗_</sup> _f_<sup>_V_</sup> 2 , any covariance matrix can be decomposed into two parts, a correlation matrix Σ<sup>_∗_</sup> _f_<sup>andamatrix</sup><sup>_V_thatcontainsthevariancesonitsdiagonal.</sup> Assuming a hierarchical inverse Wishart prior distribution Σ<sup>ˆ</sup> _|Sf ∼ IW_ ( _νf , Sf_ ) , the joint distribution of _V_ and _Sf_ can be factored as _p_ ( _V, Sf |_ Σ<sup>_∗_</sup> _f_<sup>)=</sup><sup>_p_(</sup><sup>_V |Sf,_Σ</sup><sup>_∗_</sup> _f_<sup>)</sup><sup>_p_(</sup><sup>_Sf_),</sup> and it can be shown that each diagonal element of _V_ , _vj_ , follows an inverse Gamma distribution 



where _sj_ and _σfj_<sup>_∗−_arethe</sup><sup>_j_thdiagonalelementsof,respectively,</sup><sup>_Sf_andΣ</sup><sup>_∗_</sup> _f −_ 1 . For _Sf_ we impose the Huang and Wand (2013) prior as in Conti et al. (2014), hence _Sf_ is a nonsingular diagonal matrix with its non-zero elements following a Gamma distribution<sup>11</sup> 



At iteration ( _m_ ) , we proceed as follows: 

(i) Sample _Vprior_ from (41) and (42). 

(ii) Expand the model 



ˆ In this expanded model the residuals are distributed as _ηt_<sup>_f_(</sup><sup>_m_)</sup> _∼ N_ �0 _,_ Σ<sup>ˆ</sup><sup>_∗_</sup> _f_<sup>(</sup><sup>_m_)</sup> � with 



(iii) Update the covariance matrix 



and update the working parameter _Vpost_ by setting it to the diagonal elements of Σ<sup>ˆ</sup><sup>_∗_(</sup><sup>_m_)</sup> . _f_ 

(iv) Transform back to the identied model 



We then proceed with the second block of the covariance matrix, which is left unrestricted and can be drawn from an inverse Wishart distribution. 



> 11It is parametrized such that _ν∗_ = _ν − k_ + 1 and _E_ ( _sj_ ) = _ν∗Cj_ 2 

30 

## C Identication of structural shocks by maxithe share of the forecast error mizing explained variance 

This approach to identify structural shocks in a VAR was originally proposed by Uhlig (2003,2004). The idea is to identify _s ≤ k_ orthogonal shocks that explain the maximum fraction of the forecast error variance (FEV) over a given prediction horizon _t_ + _<u>h</u>_ to _t_ + _h_<sup>¯</sup> for one variable included in the VAR. In the present paper, we adapt the approach to the FAVAR framework. The target will not be to explain a maximum share of the FEV for a factor. Rather, we maximize the explained share in the FEV of a selected variable in _Xt_ , for example TFP. In this section, we use notation similar to Uhlig (2003) for a better understanding. The VAR for factors writes 



where _ηt_<sup>_∗_aretheonestepaheadpredictionerrorswithvariance-covariancematrix</sup> Σ<sup>_∗_</sup> . If the VAR is stationary, we can write the moving average representation: 



where 



To identify the structural shocks, we need to nd a matrix _A_ which fullls _ηt_<sup>_∗_=</sup><sup>_Aυt_</sup> and _E_ [ _υtυt_<sup>_′_]=</sup><sup>_Ik_+</sup><sup>_m_.Notethatinoursetupthelastelementin</sup><sup>_η_</sup> _t_<sup>_∗_,themonetary</sup> policy shock, is orthogonal to the other elements by construction (all o-diagonal elements in the last row and column of Σ<sup>_∗_</sup> are set to zero). To identify additional structural shocks, we are interested in nding a _k × k_ submatrix, _A_ 1 , of _A_ , such that _A_ 1 _ηt_<sup>_∗f_</sup> = _υt_<sup>1,</sup><sup>_E_[</sup><sup>_υ_</sup> _t_<sup>1</sup><sup>_υ_</sup> _t_<sup>1</sup><sup>_′_] =</sup><sup>_Ik_and</sup> 



The impulse responses to the structural shocks are then computed as 



An obvious candidate for _A_ 1 is the Cholesky decomposition of the leading _k × k_ submatrix of Σ<sup>_∗_</sup> . But using any orhtogonal matrix _Q_ 1 satisfying _Q_ 1 _Q_<sup>_′_</sup> 1<sup>=</sup><sup>_Ik_,yields</sup> another valid candidate _A_<sup>˜</sup> 1 = _A_ 1 _Q_ 1 with impulse responses 



Call _et_ + _h|t−_ 1 the _h_ -step ahead prediction error of _Ft_ + _h_ given all the data up to _t −_ 1 , 



31 

with covariance matrix 



were _qj_ is the jth vector of the matrix _Q_ . The last term represents the covariance matrix as the sum of each (orthogonal) shock's covariance component. 

In Uhlig (2003) the goal is to nd the vector _q_ 1 that explains the maximum share of the FEV over a pre-dened horizon of a variable _i_ included in the VAR 



This vector is given by the eigenvector associated with the largest eigenvalue of the matrix 



where _ιi_ is the selection vector with a 1 at position of variable _i_ . 

Our focus lies on the object 



which is the forecast error variance of variable _i_ in _Xt_ . Therefore, the vector _q_ 1 will be the eigenvector corresponding to the largest eigenvalue of the matrix 



32 

## D Tables 

|Factor loadings|_r_0 = 200, _s_0 = 0_._35, _τj ∼IG_(2_,_0_._125),|
|---|---|
||_a_= 0_._01, _b_= 0_._4|
|Factor VAR|_vec_(Φ)_∼N_(0_, P_0),_P_0: Minnesota with prior|
||diagonal variance 0.25 and shrink factor for|
||o-diagonals 0.025,|
||_ν_ =_k_+_m_+ 1, _ν_<sup>_∗_</sup>=_ν −_(_k_+_m_) + 1|
|Idiosyncratic component|_ψi ∼N_(0_,_0_._25), _σ_<sup>2</sup><br>_i _<sup>_∼IG_(2</sup><sup>_,_ 0</sup><sup>_._25)</sup>|



Table 1: Prior specication 

#### NIPA and Production 

#### Prices 

|GDPC96|0.99|
|---|---|
|PCECC96|0.56|
|GPDIC96|0.74|
|FPIx|0.77|
|PRFIx|0.67|
|INDPRO|0.95|
|CUMFNS|0.10|
|TFP|0.37|



|PCECTPI<br>0.98|
|---|
|DGOERG3Q086SBEA<br>0.89|
|CPIAUCSL<br>0.96|
|PPIACO<br>0.79|
|OILPRICEx<br>0.58|
|DNDGRG3Q086SBEA<br>0.96|



#### Interest Rates 

|Employment|
|---|
|PAYEMS<br>0.93|
|USPRIV<br>0.97|
|MANEMP<br>0.91|
|UNRATE<br>0.87|
|USGOVT<br>0.03|
|HOABS<br>0.84|



|TB3MS|0.99|
|---|---|
|GS1|0.99|
|GS5|0.95|
|GS10|0.84|
|AAA|0.62|
|TB3SMFFM|0.81|
|GS10TB3Mx|0.64|



|Housing||
|---|---|
|HOUST|0.78|
|PERMIT|0.84|
|Sales||
|CMRMTSPLx|0.81|



|Credit and|Stocks|
|---|---|
|BUSLOANSx|0.24|
|CONSUMERx|0.11|
|REALLNx|0.16|
|TOTALSLx|0.46|
|S0x26P500|0.27|



Table 2: Median variance share explained by the common component. 

33 

||IPMANSICS(0.98)<br>INDPRO(0.97)<br>IPMAT(0.94)|
|---|---|
|Factor 1|IPDMAT(0.93)<br>IPFINAL(0.91)<br>CMRMTSPLx(0.88)<br>HOANBS(0.85) NAPMPI(0.85)|
|Factor 2|USPRIV(0.93)<br>PAYEMS(0.92)<br>USWTRADE(0.91)<br>USTPU(0.91)<br>USGOOD(0.90)<br>SRVPRD(0.87)<br>DMANEMP(0.86) MANEMP(0.86)|
||PERMIT(0.93)<br>HOUST(0.89)<br>PERMITS(0.88)<br>PER-|
|Factor 3|MITW(0.80)<br>HOUSTS(0.78)<br>PERMITMW(0.77)<br>HOUSTW(0.75) PRFIx(0.74)|
|Factor 4|PCEPILFE(0.99)<br>DSERRG3Q086SBEA(0.97)<br>GDPCTPI(0.96)<br>DHCERG3Q086SBEA(0.96)<br>IPDBS(0.94)<br>CPILFESL(0.92)<br>PCECTPI(0.92)<br>DDURRG3Q086SBEA(0.89)|
|Factor 5|DGOERG3Q086SBEA(0.94)<br>DNDGRG3Q086SBEA(0.92)<br>CPITRNSL(0.90)<br>CUSR0000SAC(0.87)<br>PPIFCG(0.86)<br>PPIACO(0.85) PPIIDC(0.84) DGDSRG3Q086SBEA(0.81)|
||GS1TB3Mx(0.79)<br>GS10(0.59)<br>AAA(0.58)<br>BAA(0.57)|
|Factor 6|T5YFFM(0.56)<br>GS5(0.56)<br>TB6M3Mx(0.51)<br>GS10TB3Mx(0.47)|
||OPHPBS(0.83)<br>OPHNFB(0.80)<br>GDPC96(0.67)|
|Factor 7|OUTBS(0.66) OUTNFB(0.63) TFP(0.58) UNLPNBS(0.54)<br>GCEC96(0.40)|



Table 3: Series most correlated with unobserved factors, correlation coecient in brackets. 

34 

## E Figures 

### E.1 Choosing the number of factors 



<!-- Start of picture text -->
0.6 1<br>Median<br>Mean 0.9<br>0.55<br>0.8<br>0.5 0.7<br>0.6<br>0.45<br>0.5<br>0.4<br>0.4<br>0.35 0.3<br>0.2<br>0.3<br>3 4 5 6 7 8 9 10 11 12 2 4 6 8 10 12 14 16 18 20<br>k k+1<br>k+1<br>/e<br>ek+2<br>Variance share<br><!-- End of picture text -->

Figure 11: Left: Variance shares explained by the common component conditional on _k_ = 3 _, . . . ,_ 12 estimated unobserved factors. Right: Eigenvalue-ratio based criterion for the number of factors. The global maximum indicates 2 strong factors, the local minima at 5, 8, 11 and 13 indicate further so-called weaker factors. We cut o at a ratio of 0.7. 

35 

### E.2 Additional impulse responses and variance decompositions 



<!-- Start of picture text -->
PCED PCE LFE CPI<br>2 2 1<br>0<br>0 0<br>-1<br>-2 -2<br>-2<br>-4 -4 -3<br>0 20 40 0 20 40 0 20 40<br>PPIACO S&P500<br>1 0.2 Commodity Prices 0.4<br>0 0 0.2<br>-1 -0.2 0<br>-2 -0.4 -0.2<br>-3 -0.6 -0.4<br>0 20 40 0 20 40 0 20 40<br><!-- End of picture text -->

Figure 12: Impulse responses of selected price indices to a FFR shock when the estimation sample ends in 2007Q2, i.e. when we exclude the great recession. 



<!-- Start of picture text -->
1.5<br>1<br>0.5<br>0<br>-0.5<br>-1<br>-1.5<br>1969:2 1974:2 1979:2 1984:2 1989:2 1994:2<br><!-- End of picture text -->

Figure 13: Identied monetary policy shock vs. Romer and Romer (2004) monetary shock (blue line). 

36 



<!-- Start of picture text -->
FFR IP CPI 3m TBills<br>1.5 0.15 0.15 1<br>0.8<br>1 0.1 0.1<br>0.6<br>0.4<br>0.5 0.05 0.05<br>0.2<br>0 0 0 0<br>0 20 40 0 20 40 0 20 40 0 20 40<br>5y TBills Monetary Base M2 PPI<br>0.6 0.1 0.2 0.08<br>0.08<br>0.15 0.06<br>0.4<br>0.06<br>0.1 0.04<br>0.04<br>0.2<br>0.05 0.02<br>0.02<br>0 0 0 0<br>0 20 40 0 20 40 0 20 40 0 20 40<br><!-- End of picture text -->

Figure 14: Share of the forecast error variance in selected variables explained by the FFR shock. 



<!-- Start of picture text -->
Hours Consumption GDP CPI<br>0.15 0.3 0.5 0.15<br>0.4<br>0.1 0.2 0.1<br>0.3<br>0.2<br>0.05 0.1 0.05<br>0.1<br>0 0 0 0<br>0 20 40 0 20 40 0 20 40 0 20 40<br>Spread 5y TBills Hourly Comp. TFP<br>0.08 0.08 0.05 1<br>0.04 0.8<br>0.06 0.06<br>0.03 0.6<br>0.04 0.04<br>0.02 0.4<br>0.02 0.02<br>0.01 0.2<br>0 0 0 0<br>0 20 40 0 20 40 0 20 40 0 20 40<br><!-- End of picture text -->

Figure 15: Share of the forecast error variance in selected variables explained by the technology shock. 

37 

### E.3 Factor loadings 

The following gures contain the factor loadings with a posterior probability of a non-zero entry lareger than 0.5 for each factor. 



<!-- Start of picture text -->
GDPC96 DMANEMP DRCARG3Q086SBEA<br>PCECC96 NDMANEMP NAPMPRI<br>PCDGx USCONS AHETPIx<br>PCESVx USPBS CES3000000008x<br>PCNDx USLAH OPHNFB<br>GPDIC96 USMINE OPHPBS<br>FPIx USTPU ULCBS<br>Y033RC1Q027SBEAx USTRADE ULCNFB<br>PNFIx USWTRADE BAA10YM<br>PRFIx CES9092000001 TLBSHNOx<br>FGRECPTx CE16OV UMCSENTx<br>EXPGSC96 UNRATE B021RE1Q156NBEA<br>IMPGSC96 UNRATESTx IPMANSICS<br>DPIC96 UNRATELTx<br>IPFUELS<br>OUTNFB LNS14000012<br>NAPMPI<br>OUTBS LNS14000025<br>UEMPMEAN<br>INDPRO LNS14000026<br>CES0600000007<br>IPFINAL UEMPLT5<br>NAPMEI<br>IPCONGD UEMP5TO14<br>IPMAT UEMP15T26 NAPM<br>IPDMAT LNS12032194 NAPMNOI<br>IPNMAT HOABS PPICRM<br>IPDCONGD HOANBS PPICMM<br>IPB51110SQ AWHMAN CLAIMSx<br>IPNCONGD AWHNONAG BUSINVx<br>IPBUSEQ AWOTMAN ISRATIOx<br>CUMFNS CMRMTSPLx CONSPI<br>PAYEMS RSAFSx CP3M<br>USPRIV AMDMNOx TNWMVBSNNCBBDIx<br>MANEMP AMDMUOx TNWBSNNBBDIx<br>SRVPRD NAPMSDI CNCFx<br>USGOOD DONGRG3Q086SBEA TFP<br>-0.6 -0.4 -0.2 0 0.2 0.4 0.6 -0.6 -0.4 -0.2 0 0.2 0.4 0.6 -0.6 -0.4 -0.2 0 0.2 0.4 0.6<br><!-- End of picture text -->

Figure 16: Non-zero loadings for factor 1. 



<!-- Start of picture text -->
PCESVx CE16OV CPF3MTB3Mx<br>FPIx CIVPART BUSLOANSx<br>Y033RC1Q027SBEAx UNRATE CONSUMERx<br>PNFIx UNRATELTx NONREVSLx<br>A014RE1Q156NBEA LNS14000012 REALLNx<br>FGRECPTx LNS14000025 TOTALSLx<br>IPCONGD LNS14000026 VXOCLSX<br>IPDCONGD UEMPLT5 NAPMPI<br>IPB51110SQ UEMP15T26 UEMPMEAN<br>IPBUSEQ UEMP27OV CES0600000007<br>CUMFNS HOABS NAPMEI<br>PAYEMS HOANBS NAPM<br>USPRIV AWHMAN NAPMNOI<br>MANEMP AWHNONAG NAPMII<br>SRVPRD AWOTMAN TB3SMFFM<br>USGOOD HOUST5F CPIMEDSL<br>DMANEMP AMDMUOx DTCTHFNM<br>NDMANEMP NAPMSDI INVEST<br>USCONS DONGRG3Q086SBEA CLAIMSx<br>USEHS NAPMPRI BUSINVx<br>USFIRE OPHNFB ISRATIOx<br>USINFO OPHPBS CONSPI<br>USPBS ULCBS NIKKEI225<br>USLAH ULCNFB TTAABSNNCBx<br>USSERV UNLPNBS TNWMVBSNNCBx<br>USTPU BAA NNBTASQ027Sx<br>USTRADE BAA10YM TNWBSNNBx<br>USWTRADE GS10TB3Mx S0x26PPERatio<br>-0.2 -0.1 0 0.1 0.2 -0.2 -0.1 0 0.1 0.2 -0.2 -0.1 0 0.1 0.2<br><!-- End of picture text -->

Figure 17: Non-zero loadings for factor 2. 

38 



<!-- Start of picture text -->
PCECC96 CPILFESL<br>PCDGx NAPMPRI<br>PCESVx TB3MS<br>PCNDx TB6MS<br>GPDIC96 BAA<br>FPIx BAA10YM<br>PRFIx TB6M3Mx<br>A014RE1Q156NBEA GS1TB3Mx<br>INDPRO GS10TB3Mx<br>IPFINAL CPF3MTB3Mx<br>IPMAT AMBSLREALx<br>IPDMAT M1REALx<br>IPBUSEQ M2REALx<br>CUMFNS MZMREALx<br>MANEMP TABSHNOx<br>DMANEMP TNWBSHNOx<br>USCONS TARESAx<br>USLAH TFAABSHNOx<br>USGOVTUSMINE VXOCLSX<br>CES9091000001 IPMANSICS<br>AWHMAN TOTRESNS<br>HOUST TB3SMFFM<br>HOUST5F CUSR0000SAS<br>PERMIT CPIULFSL<br>HOUSTMW CUSR0000SA0L5<br>HOUSTNE INVEST<br>HOUSTS ISRATIOx<br>HOUSTW CP3M<br>CMRMTSPLx PERMITNE<br>RSAFSx PERMITMW<br>AMDMNOx PERMITS<br>GPDICTPI PERMITW<br>DSERRG3Q086SBEA NIKKEI225<br>DHCERG3Q086SBEA S0x26P500<br>DFSARG3Q086SBEA S0x26P0x3AIndust<br>DIFSRG3Q086SBEA S0x26PDivYield<br>CPIAUCSL S0x26PPERatio<br>-0.6 -0.4 -0.2 0 0.2 0.4 0.6 -0.6 -0.4 -0.2 0 0.2 0.4 0.6<br><!-- End of picture text -->

Figure 18: Non-zero loadings for factor 3. 



<!-- Start of picture text -->
PCDGx CPIAUCSL<br>IPDMAT CPILFESL<br>USMINE PPIFGS<br>UNRATE PPIACO<br>UNRATESTx PPIFCG<br>UNRATELTx PPIFCF<br>LNS14000012 PPIIDC<br>LNS14000025 PPIITM<br>LNS14000026 NAPMPRI<br>UEMP15T26 AHETPIx<br>UEMP27OV ULCBS<br>RSAFSx ULCNFB<br>PCECTPI UNLPNBS<br>PCEPILFE TB6M3Mx<br>GDPCTPI GS1TB3Mx<br>GPDICTPI CPF3MTB3Mx<br>IPDBS M2REALx<br>DGDSRG3Q086SBEA MZMREALx<br>DNDGRG3Q086SBEADDURRG3Q086SBEADHCERG3Q086SBEADSERRG3Q086SBEA NONREVSLxTOTALSLxNAPMPI<br>DMOTRG3Q086SBEA CPIAPPSL<br>DFDHRG3Q086SBEA CPITRNSL<br>DREQRG3Q086SBEA CPIMEDSL<br>DODGRG3Q086SBEA CUSR0000SAC<br>DFXARG3Q086SBEA CUUR0000SAD<br>DCLORG3Q086SBEA CUSR0000SAS<br>DONGRG3Q086SBEA CPIULFSL<br>DHUTRG3Q086SBEA CUUR0000SA0L2<br>DHLCRG3Q086SBEA CUSR0000SA0L5<br>DTRSRG3Q086SBEA CES0600000008<br>DRCARG3Q086SBEA BUSINVx<br>DFSARG3Q086SBEA CONSPI<br>DIFSRG3Q086SBEA TLBSNNCBBDIx<br>DOTSRG3Q086SBEA NNBTILQ027SBDIx<br>-0.3 -0.2 -0.1 0 0.1 0.2 0.3 -0.3 -0.2 -0.1 0 0.1 0.2 0.3<br><!-- End of picture text -->

Figure 19: Non-zero loadings for factor 4. 

39 



<!-- Start of picture text -->
PCECC96 RCPHBS IMPGSC96<br>PCNDx BAA10YM IPCONGD<br>PRFIx AMBSLREALx IPNCONGD<br>EXPGSC96 M1REALx IPDBS<br>DPIC96 M2REALx DFXARG3Q086SBEA<br>DGOERG3Q086SBEA<br>IPCONGD MZMREALx DFSARG3Q086SBEA<br>IPDMAT BUSLOANSx PPIFGS<br>RSAFSx REALLNx PPIFCG<br>AMDMNOx LIABPIx WPU0561<br>PCECTPI VXOCLSX TB3MS<br>GDPCTPI EXCAUSx TB6MS<br>GPDICTPI B020RE1Q156NBEA GS1<br>IPDBS B021RE1Q156NBEA GS10<br>DGDSRG3Q086SBEA NAPMPI AAA<br>BAA<br>DNDGRG3Q086SBEA NAPMEI BAA10YM<br>DFXARG3Q086SBEA NAPMNOI TB6M3Mx<br>DGOERG3Q086SBEA TOTRESNS GS1TB3Mx<br>DRCARG3Q086SBEA PPICRM GS10TB3Mx<br>CPIAUCSL PPICMM NAPMPI<br>PPIFGS CPIAPPSL NAPM<br>PPIACO CPITRNSL NAPMNOI<br>PPIFCG CUSR0000SAC GS5<br>PPIFCF CPIULFSL TB3SMFFM<br>PPIIDC CUUR0000SA0L2 T5YFFM<br>AAAFFM<br>PPIITM CUSR0000SA0L5<br>CPITRNSL<br>NAPMPRI INVEST CP3M<br>WPU0561 BUSINVx COMPAPFF<br>OILPRICEx ISRATIOx TNWMVBSNNCBBDIx<br>COMPRNFB COMPAPFF TNWBSNNBBDIx<br>-0.5 0 0.5 -0.5 0 0.5 -0.4 -0.2 0 0.2 0.4<br><!-- End of picture text -->

Figure 20: Non-zero loadings for factor 5 (left and middle) and factor 6 (right). 



<!-- Start of picture text -->
GDPC96 CIVPART<br>PCECC96 DONGRG3Q086SBEA<br>PCDGx DHLCRG3Q086SBEA<br>PCNDx CPIAUCSL<br>GPDIC96 CPILFESL<br>FPIx TB3MS<br>A014RE1Q156NBEA TB6MS<br>GCEC96 GS1<br>A823RL1Q225SBEA GS10<br>SLCEx AAA<br>EXPGSC96 BAA<br>DPIC96 BAA10YM<br>OUTNFB<br>TB6M3Mx<br>OUTBS<br>GS10TB3Mx<br>PAYEMS<br>CPF3MTB3Mx<br>USMINE<br>AMBSLREALx<br>CMRMTSPLx<br>M1REALx<br>RSAFSx<br>OPHNFB TOTRESNS<br>OPHPBS GS5<br>ULCBS TB3SMFFM<br>ULCNFB T5YFFM<br>UNLPNBS AAAFFM<br>B021RE1Q156NBEA CPIMEDSL<br>ISRATIOx CUSR0000SAS<br>TLBSNNCBx CUUR0000SA0L2<br>TNWMVBSNNCBBDIx CUSR0000SA0L5<br>TNWBSNNBBDIx DTCTHFNM<br>CNCFx CP3M<br>TFP COMPAPFF<br>-0.5 0 0.5 -0.3 -0.2 -0.1 0 0.1 0.2 0.3<br><!-- End of picture text -->

Figure 21: Non-zero loadings for factor 7 (left) and 8 (right). 

40 

## F Data 

Table 4: Time series. Transformations: level (lv), rst dierence (fd), rst log dierence () 

|ID<br>|MNEMONIC<br>|Description<br><br>|TCode<br>|
|---|---|---|---|
|1|GDPC96|Real Gross Domestic Product, 3 Decimal (Billions of Chained 2009<br>Dollars)||
|2|PCECC96|Real Personal Consumption Expenditures (Billions of Chained 2009<br>Dollars)||
|3|PCDGx|Real personal consumption expenditures: Durable goods (Billions of<br>Chained 2009 Dollars), deated using PCE||
|4|PCESVx|Real Personal Consumption Expenditures: Services (Billions of 2009<br>Dollars), deated using PCE||
|5|PCNDx|Real Personal Consumption Expenditures: Nondurable Goods (Bil-<br>lions of 2009 Dollars), deated using PCE||
|6|GPDIC96|Real Gross Private Domestic Investment, 3 decimal (Billions of<br>Chained 2009 Dollars)||
|7|FPIx|Real private xed investment (Billions of Chained 2009 Dollars), de-<br>ated using PCE||
|8|Y033RC1Q027SBEAx|Real Gross Private Domestic Investment: Fixed Investment: Nonresi-<br>dential: Equipment (Billions of Chained 2009 Dollars), deated using<br>PCE||
|9|PNFIx|Real private xed investment:<br>Nonresidential (Billions of Chained<br>2009 Dollars), deated using PCE||
|10|PRFIx|Real private xed investment: Residential (Billions of Chained 2009<br>Dollars), deated using PCE||
|11|A014RE1Q156NBEA|Shares of gross domestic product: Gross private domestic investment:<br>Change in private inventories (Percent)|lv|
|12|GCEC96|Real Government Consumption Expenditures & Gross Investment<br>(Billions of Chained 2009 Dollars)||
|13|A823RL1Q225SBEA|Real Government Consumption Expenditures and Gross Investment:<br>|lv|
|||Federal (Percent Change from Preceding Period)||
|14|FGRECPTx|Real Federal Government Current Receipts (Billions of Chained 2009<br>||
|||Dollars), deated using PCE||
|15|SLCEx|Real government state and local consumption expenditures (Billions<br>||
|||of Chained 2009 Dollars), deated using PCE||
|16|EXPGSC96|Real Exports of Goods & Services, 3 Decimal (Billions of Chained<br>2009 Dollars)||
|17|IMPGSC96|Real Imports of Goods & Services, 3 Decimal (Billions of Chained<br>2009Dollars)||
|18|DPIC96|<br>Real Disposable Personal Income (Billions of Chained 2009 Dollars)||
|19<br>20|OUTNFB<br>OUTBS|Nonfarm Business Sector: Real Output (Index 2009=100)<br>Business Sector: Real Output (Index 2009=100)|<br>|
|21|INDPRO|Industrial Production Index (Index 2012=100)||
|22|IPFINAL|Industrial Production:<br>Final Products (Market Group) (Index||
|||2012=100)||
|23|IPCONGD|Industrial Production: Consumer Goods (Index 2012=100)||
|24|IPMAT|Industrial Production: Materials (Index 2012=100)||
|25|IPDMAT|IndustrialProduction:DurableMaterials(Index2012=100)||
|26|IPNMAT|<br>Industrial Production: Nondurable Materials (Index 2012=100)|<br>|
|27|IPDCONGD|Industrial Production: Durable Consumer Goods (Index 2012=100)||
|28|IPB51110SQ|Industrial Production: Durable Goods: Automotive products (Index||
|||2012=100)||
|29|IPNCONGD|Industrial<br>Production:<br>Nondurable<br>Consumer<br>Goods<br>(Index<br>2012=100)||
|30|IPBUSEQ|Industrial Production: Business Equipment (Index 2012=100)||
|31|IPB51220SQ|Industrial Production: Consumer energy products (Index 2012=100)||
|32<br>33|CUMFNS<br>PAYEMS|Capacity Utilization: Manufacturing (SIC) (Percent of Capacity)<br>All Employees: Total nonfarm (Thousands of Persons)|lv<br>|
|34|USPRIV|AllEmloees:TotalPrivateIndustries(ThousandsofPersons)||
|35|MANEMP|py      <br>All Employees: Manufacturing (Thousands of Persons)|<br>|
|36|SRVPRD|All Employees: Service-Providing Industries (Thousands of Persons)<br>||
|37|USGOOD|All Employees: Goods-Producing Industries (Thousands of Persons)||
|38|DMANEMP|All Employees: Durable goods (Thousands of Persons)||
|39|NDMANEMP|All Employees: Nondurable goods (Thousands of Persons)||
|40<br>41|USCONS<br>USEHS|All Employees: Construction (Thousands of Persons)<br>AllEmloees:Education&HealthServices(ThousandsofPersons)|<br>|
|42|USFIRE|py       <br>All Employees: Financial Activities (Thousands of Persons)|<br>|



41 

Table 4: Time series, continued. 

|ID<br>43|MNEMONIC<br>USINFO|Description<br><br>AllElIftiSiThdfP|TCode<br>|
|---|---|---|---|
|44|USPBS|mpoyees: normaon ervces (ousans o ersons)<br>All Employees: Professional & Business Services (Thousands of Per-<br>|<br>|
|45|USLAH|sons)<br>All Employees: Leisure & Hospitality (Thousands of Persons)||
|46|USSERV|All Employees: Other Services (Thousands of Persons)||
|47|USMINE|All Employees: Mining and logging (Thousands of Persons)||
|48|USTPU|All Employees: Trade, Transportation & Utilities (Thousands of Per-<br>sons)||
|49|USGOVT|All Employees: Government (Thousands of Persons)||
|50|USTRADE|All Employees: Retail Trade (Thousands of Persons)||
|51|USWTRADE|AllEmployees:WholesaleTrade(ThousandsofPersons)||
|52|CES9091000001|<br>All Employees: Government: Federal (Thousands of Persons)|<br>|
|53|CES9092000001|All Employees: Government: State Government (Thousands of Per-<br>||
|54|CES9093000001|sons)<br>All Employees: Government: Local Government (Thousands of Per-<br>||
|55|CE16OV|sons)<br>Civilian Employment (Thousands of Persons)||
|56|CIVPART|Civilian Labor Force Participation Rate (Percent)|fd|
|57|UNRATE|CivilianUnemploymentRate(Percent)|fd|
|58|UNRATESTx|<br>Unemployment Rate less than 27 weeks (Percent)|fd|
|59|UNRATELTx|Unemployment Rate for more than 27 weeks (Percent)|fd|
|60<br>61|LNS14000012<br>LNS14000025|Unemployment Rate - 16 to 19 years (Percent)<br>UnemploymentRate-20yearsandoverMen(Percent)|fd<br>fd|
|62|LNS14000026|,  <br>Unemployment Rate - 20 years and over, Women (Percent)|fd|
|63|UEMPLT5|Number of Civilians Unemployed - Less Than 5 Weeks (Thousands of<br>P||
|64|UEMP5TO14|ersons)<br>Number of Civilians Unemployed for 5 to 14 Weeks (Thousands of||
|||Persons)||
|65|UEMP15T26|Number of Civilians Unemployed for 15 to 26 Weeks (Thousands of<br>P||
|66|UEMP27OV|ersons)<br>Number of Civilians Unemployed for 27 Weeks and Over (Thousands<br>ofPersons)||
|67|LNS12032194|<br>Employment Level - Part-Time for Economic Reasons, All Industries<br>(ThousandsofPersons)||
|68|HOABS|<br>Business Sector: Hours of All Persons (Index 2009=100)||
|69|HOANBS|NonfarmBsinessSectorHorsofAllPersons(Inde2009=100)||
|70|AWHMAN|u : u    x <br>Average Weekly Hours of Production and Nonsupervisory Employees:<br>Manufacturin(Hours)|<br>lv|
|71|AWHNONAG|g <br>Average Weekly Hours Of Production And Nonsupervisory Employ-<br>ees:Totalrivate(Hours)|fd|
|72|AWOTMAN|p <br>Average Weekly Overtime Hours of Production and Nonsupervisory<br>Emploees:Manufacturin(Hours)|fd|
|73|HOUST|y g <br>Housing Starts: Total: New Privately Owned Housing Units Started<br>(ThousandsofUnits)||
|74|HOUST5F|<br>Privately Owned Housing Starts: 5-Unit Structures or More (Thou-<br>sandsofUnits)||
|75|PERMIT|<br>New Private Housing Units Authorized by Building Permits (Thou-<br>sandsofUnits)||
|76|HOUSTMW|<br>Housing Starts in Midwest Census Region (Thousands of Units)||
|77|HOUSTNE|Housing Starts in Northeast Census Region (Thousands of Units)||
|78<br>79|HOUSTS<br>HOUSTW|Housing Starts in South Census Region (Thousands of Units)<br>HousingStartsinWestCensusRegion(ThousandsofUnits)|<br>|
|80|CMRMTSPLx|<br>Real Manufacturing and Trade Industries Sales (Millions of Chained<br>2009Dollars)|<br>|
|81|RSAFS|<br>RlRildFdSiSlMillifChid2009Dl||
||x|ea eta an oo ervces aes (ons o ane  o-<br>lars)deatedbyCorePCE||
|82|AMDMNO|,     <br>RlMft&NOdDblGdMillif2009||
||x|ea anuacurers ew rers: urae oos (ons o <br>Dollars)deatedbyCorePCE||
|83|AMDMUO|,     <br>RlVlfMft&UlldOdfDblGd||
||x|ea aue o anuacurers n e rers or urae oos<br>Industries (Million of 2009 Dollars) deated by Core PCE||
|84|NAPMSDI|,<br>ISMMftiSliDliiIdli|l|
|85|PCECTPI|anuacurng: upper everes nex (n)<br>Personal Consumption Expenditures: Chain-type Price Index (Index<br>2009=100)|v<br>|
|86|PCEPILFE|Personal Consumption Expenditures Excluding Food and Energy<br>ChiTPiIdId||
|87|GDPCTPI|(an-ype rce nex) (nex 2009=100)<br>Gross Domestic Product: Chain-type Price Index (Index 2009=100)||



42 

Table 4: Time series, continued. 

|ID<br>88|MNEMONIC<br>GPDICTPI|Description<br><br>GPitDtiIttChitPiIdId|TCode<br>|
|---|---|---|---|
|||ross rvae omesc nvesmen: an-ype rce nex (nex<br>||
|89|IPDBS|2009=100)<br>BusinessSector:ImplicitPriceDeator(Index2009=100)||
|90|DGDSRG3Q086SBEA|<br>Personal consumption expenditures: Goods (chain-type price index)|<br>|
|91|DDURRG3Q086SBEA|Personal consumption expenditures: Durable goods (chain-type price<br>id||
|92|DSERRG3Q086SBEA|nex)<br>Personal consumption expenditures: Services (chain-type price index)||
|93|DNDGRG3Q086SBEA|<br>Personal consumption expenditures: Nondurable goods (chain-type<br>riceindex)||
|94|DHCERG3Q086SBEA|p <br>Personal consumption expenditures: Services: Household consump-<br>tionexpenditures(chain-typepriceindex)||
|95|DMOTRG3Q086SBEA|<br>Personal consumption expenditures: Durable goods: Motor vehicles<br>and parts (chain-type price index)||
|96|DFDHRG3Q086SBEA|Personal consumption expenditures: Durable goods: Furnishings and<br>durablehouseholdequipment(chain-typepriceindex)||
|97|DREQRG3Q086SBEA|<br>Personal consumption expenditures:<br>Durable goods:<br>Recreational<br>goods and vehicles (chain-type price index)||
|98|DODGRG3Q086SBEA|Personal consumption expenditures: Durable goods: Other durable<br>goods (chain-type price index)||
|99|DFXARG3Q086SBEA|Personal consumption expenditures: Nondurable goods: Food and<br>beverages purchased for o-premises consumption (chain-type price<br>index)||
|100|DCLORG3Q086SBEA|Personal consumption expenditures: Nondurable goods: Clothing and<br>footwear (chain-type price index)||
|101|DGOERG3Q086SBEA|Personal consumption expenditures: Nondurable goods: Gasoline and<br>other energy goods (chain-type price index)||
|102|DONGRG3Q086SBEA|PersonalconsmtioneenditresNondrableoodsOthernon-||
|||up xpu: u g:  <br>durablegoods(chain-typepriceindex)||
|103|DHUTRG3Q086SBEA|<br>Personal consumption expenditures: Services: Housing and Utilities<br>(chain-type price index)||
|104|DHLCRG3Q086SBEA|Personal consumption expenditures:<br>Services:<br>Health care (chain-<br>iid||
|105|DTRSRG3Q086SBEA|type prce nex)<br>Personal consumption expenditures: Transportation Services (chain-<br>iid||
|106|DRCARG3Q086SBEA|type prce nex)<br>Personal consumption expenditures: Recreation Services (chain-type<br>riceindex)||
|107|DFSARG3Q086SBEA|p <br>Personal consumption expenditures: Services: Food Services and ac-<br>commodations(chain-tericeindex)||
|108|DIFSRG3Q086SBEA|yp p <br>Personal consumption expenditures: Financial Services and insurance<br>(chain-tericeindex)||
|109|DOTSRG3Q086SBEA|yp p <br>Personal consumption expenditures: Other Services (chain-type price<br>index)||
|110|CPIAUCSL|Consumer Price Index for All Urban Consumers: All Items (Index<br>1982-84=100)||
|111|CPILFESL|Consumer Price Index for All Urban Consumers: All Items Less Food<br>&Energy(Index1982-84=100)||
|112|PPIFGS|<br>Producer Price Index by Commodity for Finished Goods (Index<br>1982=100)||
|113|PPIACO|ProducerPriceIndexforAllCommodities(Index1982=100)||
|<br>114|<br> PPIFCG|<br>Producer Price Index by Commodity for Finished Consumer Goods<br>|<br>|
|||(Index 1982=100)<br>||
|115|PPIFCF|Producer Price Index by Commodity for Finished Consumer Foods<br>(Index1982=100)||
|116|PPIIDC|<br>Producer Price Index by Commodity Industrial Commodities (Index<br>1982=100)||
|117|PPIITM|Producer Price Index by Commodity Intermediate Materials: Supplies<br>&Components(Index1982=100)||
|118 <br>119|NAPMPRI<br> WPU0561|<br>ISM Manufacturing: Prices Index (Index)<br>Producer Price Index by Commodity for Fuels and Related Prod-<br>ucts and Power:<br>Crude Petroleum (Domestic Production) (Index<br>|lv<br>|
|120|OILPRICE|1982=100)<br>RlCdOilPiWtTItditWTIChi||
||x|ea rue  rces: es exas nermeae () - usng,<br>Oklahoma (2009 Dollars per Barrel), deated by Core PCE||
|121|AHETPI|Rl A Hl Ei f Pdti d Ni E||
||x|ea verage oury arnngs o roucon an onsupervsory m-<br>ployees: Total Private (2009 Dollars per Hour), deated by Core PCE||
|122|CES2000000008x|<br>Real Average Hourly Earnings of Production and Nonsupervisory Em-<br>||
|||ployees: Construction(2009 Dollarsper Hour), deated byCore PCE||



43 

Table 4: Time series, continued. 

|ID<br>123|MNEMONIC<br>CES3000000008|Description<br><br>Rl A Hl Ei f Pdti d Ni E|TCode<br>|
|---|---|---|---|
||x|ea verage oury arnngs o roucon an onsupervsory m-<br>ployees: Manufacturing (2009 Dollars per Hour), deated by Core<br>PCE||
|124|COMPRNFB|Nonfarm Business Sector:<br>Real Compensation Per Hour (Index<br>2009=100)||
|125|RCPHBS|Business Sector: Real Compensation Per Hour (Index 2009=100)||
|126|OPHNFB|Nonfarm Business Sector: Real Output Per Hour of All Persons (Index<br>2009100||
|127|OPHPBS|=)<br>Business Sector:<br>Real Output Per Hour of All Persons (Index<br>2009100||
|128|ULCBS|=)<br>Business Sector: Unit Labor Cost (Index 2009=100)||
|129|ULCNFB|Nonfarm Business Sector: Unit Labor Cost (Index 2009=100)||
|130|UNLPNBS|Nonfarm Business Sector: Unit Nonlabor Payments (Index 2009=100)||
|131|FEDFUNDS|<br>Eective Federal Funds Rate (Percent)<br>|lv|
|132|TB3MS|3-Month Treasury Bill: Secondary Market Rate (Percent)|lv|
|133 <br>134|TB6MS<br> GS1|6-Month Treasury Bill: Secondary Market Rate (Percent)<br>1-Year Treasury Constant Maturity Rate (Percent)|lv<br>lv|
|135 <br>|GS10<br>|10-Year Treasury Constant Maturity Rate (Percent)<br>|lv<br>|
|136|AAA|Moodys Seasoned Aaa Corporate Bond Yield (Percent)|lv|
|137 <br>|BAA<br>|Moodys Seasoned Baa Corporate Bond Yield (Percent)<br>|lv<br>|
|138|BAA10YM|Moodys Seasoned Baa Corporate Bond Yield Relative to Yield on<br>10-YearTreasuryConstantMaturity(Percent)|lv|
|139|TB6M3Mx|<br>6-Month Treasury Bill Minus 3-Month Treasury Bill, secondary mar-<br>ket (Percent)|lv|
|140|GS1TB3Mx|1-Year Treasury Constant Maturity Minus 3-Month Treasury Bill, sec-<br>ondary market (Percent)|lv|
|141|GS10TB3Mx|10-Year Treasury Constant Maturity Minus 3-Month Treasury Bill,<br>|lv|
|142|CPF3MTB3Mx|secondary market (Percent)<br>3-MonthCommercialPaperMinus3-MonthTreasuryBillsecondary|lv|
|||, <br>market (Percent)||
|143|AMBSLREALx|St. Louis Adjusted Monetary Base (Billions of 1982-84 Dollars), de-<br>dbCPI||
|144|M1REALx|ate y <br>Real Ml Money Stock (Billions of 1982-84 Dollars), deated by CPI||
|145 <br>146|M2REALx<br>MZMREALx|Real M2 Money Stock (Billions of 1982-84 Dollars), deated by CPI<br>Real MZM Money Stock (Billions of 1982-84 Dollars) deated by CPI|<br>|
|<br>147|<br> BUSLOANSx|,<br>Real Commercial and Industrial Loans, All Commercial Banks (Bil-<br>lionsof2009U.S.Dollars)deatedbyCorePCE|<br>|
|148|CONSUMER|,     <br>Rl C L t All Cil Bk Billi f 2009 US||
||x|ea onsumer oans a  ommerca ans (ons o  ..<br>Dollars), deated by Core PCE||
|149|NONREVSLx|TotalRealNonrevolvinCreditOwnedandSecuritizedOutstandin||
|||g    , g<br>(Billions of Dollars) deated by Core PCE||
|150|REALLNx|,<br>Real Real Estate Loans, All Commercial Banks (Billions of 2009 U.S.<br>||
|151|TOTALSLx|Dollars), deated by Core PCE<br>TotalConsumerCreditOutstandingdeatedbyCorePCE||
|<br>152|<br> TABSHNOx|,     <br>Real Total Assets of Households and Nonprolit Organizations (Billions<br>of2009Dollars)deatedbCorePCE|<br>|
|153|TLBSHNOx|,   y  <br>Real Total Liabilities of Households and Nonprolit Organizations (Bil-<br>lionsof2009Dollars)deatedbCorePCE||
|154|LIABPI|,   y  <br>Libiliti f Hhld d Nlit Oiti Rlti t P||
||x|aes o ouseos an onpro rganzaons eave o er-<br>sonalDisposableIncome(Percent)||
|155|TNWBSHNOx|<br>RealNetWorthofHouseholdsandNonrolitOranizations(Billions||
|||p g <br>of 2009 Dollars), deated by Core PCE||
|156|NWPIx|Net Worth of Households and Nonprolit Organizations Relative to<br>|lv|
|157|TARESAx|Disposable Personal Income (Percent)<br>Real Assets of Households and Nonprolit Organizations excluding<br>||
|158|HNOREMQ027Sx|Real Estate Assets (Billions of 2009 Dollars), deated by Core PCE<br>Real Real Estate Assets of Households and Nonprolit Organizations<br>||
|159|TFAABSHNOx|(Billions of 2009 Dollars), deated by Core PCE<br>Real Total Financial Assets of Households and Nonprolit Organiza-<br>f||
|160|VXOCLSX|tions (Billions o 2009 Dollars), de ated by Core PCE<br>CB OE S&P 100 Volatility Index: VXO|lv|
|161|EXSZUS|SitldUSFiEhRt|l|
|<br>162|x<br> EXJPUSx|wzeran / .. oregn xcange ae<br>Japan /U.S. Foreign Exchange Rate|v<br>lv|
|163|EXUSUKx|US/UKForeinExchaneRate|lv|
|<br>164|<br> EXCAUSx|..  .. g g <br>Canada / U.S. Foreign Exchange Rate|lv|
|165|UMCSENTx|University of Michigan:<br>Consumer Sentiment (Index Ist Quarter<br>|lv|
|||1966=100)||



44 

Table 4: Time series, continued. 

|ID<br>166|MNEMONIC<br>B020RE1156NBEA|Description<br><br>Sh f  di dE f d d Si P|TCode<br>fd|
|---|---|---|---|
||Q|ares o gross omestc prouct: xports o goos an ervces (er-<br>cent)||
|167|B021RE1Q156NBEA|Shares of gross domestic product: Imports of goods and Services (Per-<br>cent)|fd|
|168 <br>|IPMANSICS<br>|Industrial Production: Manufacturing (SIC) (Index 2012=100)<br>|<br>|
|169|IPB51222S|Industrial Production: Residential Utilities (Index 2012=100)||
|170|IPFUELS|Industrial Production: Fuels (Index 2012=100)||
|171 <br>172|NAPMPI<br>UEMPMEAN|ISM Manufacturing: Production Index<br>Average(Mean)DurationofUnemployment(Weeks)|lv<br>fd|
|<br>173|<br> CES0600000007|<br>Average Weekly Hours of Production and Nonsupervisory Employees:<br>Goods-Producing|fd|
|174|NAPMEI|ISM Manufacturing: Employment Index|lv|
|175|NAPM|ISM Manufacturing: PMI Composite Index|lv|
|176|NAPMNOI|ISM Manufacturing: New Orders Index|lv|
|177|NAPMII|ISM Manufacturing: Inventories Index|lv|
|178|TOTRESNS|Total Reserves of Depository Institutions (Billions of Dollars)||
|179|GS5|5-Year Treasury Constant Maturity Rate|lv|
|180|TB3SMFFM|3-Month Treasury Constant Maturity Minus Federal Funds Rate|lv|
|181|T5YFFM|5-Year Treasury Constant Maturity Minus Federal Funds Rate|lv|
|182 <br>|AAAFFM<br>|Moodys Seasoned Aaa Corporate Bond Minus Federal Funds Rate<br>|lv<br>|
|183|PPICRM|Producer Price Index: Crude Materials for Further Processing (Index||
|||1982=100)||
|184|PPICMM|Producer Price Index: Commodities: Metals and metal products: Pri-<br>marynonferrousmetals(Index1982=100)||
|185|CPIAPPSL|<br>Consumer Price Index for All Urban Consumers:<br>Apparel (Index<br>1982-84=100)||
|1|CPITRNSL|CPiIdfAllUbCTiI||
|86||onsumer rce nex or  ran onsumers: ransportaton (n-<br>dex 1982-84=100)||
|187|CPIMEDSL|Consumer Price Index for All Urban Consumers: Medical Care (Index||
|188|CUSR0000SAC|Consumer Price Index for All Urban Consumers: Commodities (Index||
|||<br>1982-84=100)||
|189|CUUR0000SAD|Consumer Price Index for All Urban Consumers: Durables (Index<br>1982-84=100)||
|190|CUSR0000SAS|Consumer Price Index for All Urban Consumers:<br>Services (Index<br>1982-84=100)||
|191|CPIULFSL|Consumer Price Index for All Urban Consumers: All Items Less Food<br>(Index1982-84=100)||
|192|CUUR0000SA0L2|<br>Consumer Price Index for All Urban Consumers: All items less shelter<br>(Index1982-84=100)||
|193|CUSR0000SA0L5|<br>Consumer Price Index for All Urban Consumers: All items less med-<br>ical care (Index 1982-84=100)||
|194|CES0600000008|AHlEifPdidNiEl||
|||verage oury arnngs o roucton an onsupervsory mpoy-<br>ees: Goods-Producing (Dollars per Hour)||
|195|DTCOLNVHFNM|Consumer Motor Vehicle Loans Outstandin Owned b Finance Com-||
|||g  y<br>panies(MillionsofDollars)||
|196|DTCTHFNM|<br>TotalConsumerLoansandLeasesOutstandingOwnedandSecuri-||
|||<br>tized by Finance Companies (Millions of Dollars)||
|197|INVEST|Securities in Bank Credit at All Commercial Banks (Billions of Dol-<br>||
|198|CLAIMSx|lars)<br>Initial Claims||
|199|BUSINVx|Total Business Inventories (Millions of Dollars)||
|200|ISRATIOx|TotalBusiness:InventoriestoSalesRatio|fd|
|<br>201|<br> CONSPI|<br>Nonrevolving consumer credit to Personal Income|fd|
|202|CP3M|3-Month AA Financial Commercial Paper Rate|fd|
|203|COMPAPFF|3-Month Commercial Paper Minus Federal Funds Rate|lv|
|204|PERMITNE|New Private Housing Units Authorized by Building Permits in the<br>NthtCRiThdSAAR||
|205|PERMITMW|oreas ensus egon (ousans, )<br>New Private Housing Units Authorized by Building Permits in the<br>MidtCRi(ThdSAAR)||
|206|PERMITS|wes ensus egon ousans, <br>New Private Housing Units Authorized by Building Permits in the<br>SouthCensusReion(ThousandsSAAR)||
|207|PERMITW|g , <br>New Private Housing Units Authorized by Building Permits in the<br>WestCensusRegion(ThousandsSAAR)||
|208|NIKKEI225|, <br>Nikkei Stock Average||
|209|TLBSNNCBx|Real Nonnancial Corporate Business Sector Liabilities (Billions of<br>||
|||2009 Dollars), Deated by Implicit Price Deator for Business Sector<br>IPDBS||



45 

Table 4: Time series, continued. 

|ID|MNEMONIC|Description<br>|TCode|
|---|---|---|---|
|210|TLBSNNCBBDIx|Nonnancial Corporate Business Sector Liabilities to Disposable Busi-<br>ness Income (Percent)|lv|
|211|TTAABSNNCBx|Real Nonnancial Corporate Business Sector Assets (Billions of 2009<br>Dollars), Deated by Implicit Price Deator for Business Sector<br>IPDBS||
|212|TNWMVBSNNCBx|Real Nonnancial Corporate Business Sector Net Worth (Billions of<br>2009 Dollars), Deated by Implicit Price Deator for Business Sector<br>IPDBS||
|213|TNWMVBSNNCBBDIx|Nonnancial Corporate Business Sector Net Worth to Disposable<br>Business Income (Percent)|fd|
|214|NNBTILQ027Sx|Real Nonnancial Noncorporate Business Sector Liabilities (Billions<br>of 2009 Dollars), Deated by Implicit Price Deator for Business Sec-<br>tor IPDBS||
|215|NNBTILQ027SBDIx|Nonnancial Noncorporate Business Sector Liabilities to Disposable<br>Business Income (Percent)|lv|
|216|NNBTASQ027Sx|Real Nonnancial Noncorporate Business Sector Assets (Billions of<br>2009 Dollars), Deated by Implicit Price Deator for Business Sector<br>IPDBS||
|217|TNWBSNNBx|Real Nonnancial Noncorporate Business Sector Net Worth (Billions<br>of 2009 Dollars), Deated by Implicit Price Deator for Business Sec-<br>tor IPDBS||
|218|TNWBSNNBBDIx|Nonnancial Noncorporate Business Sector Net Worth to Disposable<br>Business Income (Percent)|fd|
|219|CNCFx|Real Disposable Business Income, Billions of 2009 Dollars (Corporate<br>cash ow with IVA minus taxes on corporate income, deated by<br>Implicit Price Deator for Business Sector IPDBS)||
|220|SP500|S&P Common Stock Price Index: Composite||
|221|SPIndust|S&P Common Stock Price Index: Industrials||
|222|SPDivYield|S&P Composite Common Stock: Dividend Yield|fd|
|223|SPPERatio|S&P Composite Common Stock: Price-Earnings Ratio||
|224|TFP|Total Factor Productivity||



46 

