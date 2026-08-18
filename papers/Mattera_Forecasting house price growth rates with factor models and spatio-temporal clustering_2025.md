---
title: Mattera_Forecasting house price growth rates with factor models and spatio-temporal clustering_2025
type: paper
source_pdf: raw/papers/Mattera_Forecasting house price growth rates with factor models and spatio-temporal clustering_2025.pdf
converted: 2026-08-18
---

International Journal of Forecasting 41 (2025) 398–417 



Contents lists available at ScienceDirect 

# International Journal of Forecasting 

journal homepage: www.elsevier.com/locate/ijforecast 



# Forecasting house price growth rates with factor models and spatio-temporal clustering<sup>✩</sup> 



## Raffaele Mattera<sup>a,∗</sup> , Philip Hans Franses<sup>b</sup> 

a _Department of Social and Economic Sciences, Sapienza University of Rome, Rome, Italy_ b _Econometric Institute, Erasmus School of Economics, Rotterdam, The Netherlands_ 

### a r t i c l e i n f o a b s t r a c t 

_Article history:_ This paper proposes to use factor models with cluster structure to forecast growth rates Dataset link: https://github.com/raffmattera of house prices in the US. We assume the presence of global and cluster-specific factors /stcfm/ and that the clustering structure is unknown. We adopt a computational procedure that automatically estimates the number of global factors, the clustering structure and _Keywords:_ Panel VAR the number of clustered factors. The procedure enhances spatial clustering so that the Cluster analysis nature of clustered factors reflects the similarity of the time series in the time domain Principal components and their spatial proximity. Considering house prices in 1975–2023, we highlight the Spatio-temporal modelling existence of four main clusters in the US. Moreover, we show that forecasting approaches House prices growth rates incorporating global and cluster-specific factors provide more accurate forecasts than models using only global factors and models without factors. © 2024 The Author(s). Published by Elsevier B.V. on behalf of International Institute of Forecasters. This is an open access article under the CC BY license <u>(http://creativecommons.org/licenses/by/4.0/).</u> 

#### **1. Introduction** 

Fluctuations in house prices provide important signals for consumption, inflation and financial stability, making the housing sector a critical leading indicator for the economy. Given the strong interlinkages between the regional housing market and the national business cycle, house price forecasting is paramount for policymakers. Previous studies have employed various methodologies to predict house prices at the regional level, but those based on factor models are among the most common ( _e.g._ see Das, Gupta, & Kabundi, 2011; Emiris, 2016; Moench & Ng, 2011). Factor models assume that house prices can be modelled as a sum of two components: a global component driven by an unobserved factor common to all the regions and an idiosyncratic component specific to each region. 

✩ The numerical results presented in this manuscript were reproduced by the Editor-in-Chief (up to minor discrepancies) on the 15th of September 2024. 

∗ Corresponding author. _E-mail addresses:_ raffaele.mattera@uniroma1.it (R. Mattera), franses@ese.eur.nl (P.H. Franses). 

We conjecture that it is restrictive to assume that all the regions are affected by the same latent factors when dealing with regional house prices. In the US, house prices are notably affected by spillovers from neighbouring states<sup>1</sup> (Brady, 2014; Kuethe & Pede, 2011) and are best described by clusters (Kim & Rous, 2012). The distinction into clusters also explains why previous studies found differences in the forecastability of housing price growth rates across the US states. For example, interior states appear easier to forecast than coastal states (Rapach & Strauss, 2009). Therefore, it seems useful from a forecasting perspective to use models based on global ( _e.g._ country-level) and regional (or cluster-level) latent factors. 

Regional factor models, which have become increasingly popular in empirical studies conducted by central banks ( _e.g._ Aastveit, Bjørnland, & Thorsrud, 2016; Beck, Hubrich, & Marcellino, 2009; Breitung & Eickmeier, 2014) 

1 Similar findings are common also for other housing markets outside the US, such as Germany (Otto & Schmid, 2018), Italy (Cipollini & Parla, 2020), the Netherlands (Van Dijk, Franses, Paap, & Van Dijk, 2011) and the UK (Blatt, Chaudhuri, & Manner, 2023) among others. 

https://doi.org/10.1016/j.ijforecast.2024.09.003 

0169-2070/© 2024 The Author(s). Published by Elsevier B.V. on behalf of International Institute of Forecasters. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

are particular types of factor models with cluster structure, where the clustering structure is known and depends on spatial information. These methods allow for the estimation of both global and cluster-specific factors. For example, using a two-step procedure based on the principal components method, Beck et al. (2009) proposed to model the regional inflation dynamics in the Euro Area countries by distinguishing between national and regional ( _i.e._ NUTS 2) factors. Eickmeier, Gambacorta, and Hofmann (2014), considering financial and macroeconomic variables from twenty-four economies, adopted a similar two-step procedure to study the determinants of global liquidity using global factors and two cluster-specific factors for developed and not developed countries. Aastveit et al. (2016) extended the global factor model of Mumtaz and Surico (2009), used for studying the international transmission of structural shocks, to include regional factors for thirty-two countries worldwide. Moench and Ng (2011) adopted a Factor-Augmented VAR (FAVAR) model, distinguishing between global and regional factors, for studying the effect of housing shocks on consumption in the US. Other papers have proposed alternative approaches for including the spatial dimension in factor models ( _e.g._ see Aquaro, Bailey, & Pesaran, 2021; Bailey, Holly, & Pesaran, 2016; Ciccarelli & Elhorst, 2018; Yang, 2021), but these generally consider global factors only or assume known spatial cluster structures. Lopes, Salazar, and Gamerman (2008) and Ippoliti, Valentini, and Gamerman (2012) proposed using spatially structured factor loadings to identify groups of spatial sites with common factors. These methods have been mainly applied for environmental modelling ( _e.g._ see Gamerman, Ippoliti, & Valentini, 2022), but also for housing market modelling (Valentini, Ippoliti, & Fontanella, 2013). However, these models have not been proposed with the aim of clustering and do not fully account for the role played by the clusters in the forecasting task. 

In this paper, we study cluster-specific factor models’ ability to forecast house price growth rates in the US under the assumption of unknown spatio-temporal clustering. We estimate the cluster structure of the US states directly from the data and assume that all the states in the same cluster share the cluster-specific latent factors. Moreover, we assume all the US states share the same global factor. We notice that the cluster structure depends on spatial information and the similarity of the temporal pattern in housing prices. 

In doing so, we follow a recent strand of the literature proposing approaches for estimating global and clustered factors under the assumption of unknown cluster membership. Ando and Bai (2017) develop a model for asset pricing that includes observable factors and global and cluster-specific latent factors. The (Ando & Bai, 2017) procedure requires, as in _k_ -means clustering, the ex-ante specification of the correct number of clusters and the knowledge of the number of global and cluster-specific factors within each cluster. This can be inconvenient. An additional model-searching algorithm is therefore used to tune these parameters. Alonso, Galeano, and Peña (2020) consider an alternative robust procedure for estimating global and cluster-specific factors. The authors overcome 

the problem of deciding on the number of clusters ex-ante by adopting a hierarchical procedure. Taking inspiration from the time series clustering literature, the authors adopt a cross-correlation distance (Alonso & Peña, 2019) in determining the clustering structure of the units. However, neither study includes a spatial dimension while updating the clusters and determining the nature of the cluster-specific factors, which is relevant in the case of regional house prices. 

In this paper, we, therefore, adopt a computational procedure for estimating global and cluster-specific factors that account for spatial clustering. We then estimate factor-augmented models, using the estimated factors, and predict future house price growth rates. 

The contribution of our paper is threefold. First, we show that cluster-specific factors can achieve more accurate forecasts of house price growth rates. Forecasting models based on global factors only provide less accurate forecasts out-of-sample. This evidence is confirmed by considering the results of predictive accuracy tests. Second, we adopt an unsupervised learning approach to build the clusters. We indeed consider an iterative procedure similar to Alonso et al. (2020), based on hierarchical clustering, that estimates the number of clusters and the number of factors within the algorithm. Different from (Alonso et al., 2020), who propose a fourstep procedure, we adopt an algorithm that iteratively solves the problem until convergence. Third, we introduce the spatial dimension in the problem to enhance spatial clustering in estimating the cluster-specific factors. The amount of spatial penalty introduced in the algorithm is also chosen in a data-driven manner, but it can also be set manually by the user. 

The rest of the paper is structured as follows. Section 2 presents the data about house prices in the US states and the forecasting model based on a Panel VAR with factors. Section 3 discusses the computational procedure for estimating the clusters and global and cluster-level factors. In contrast, Section 4 shows the outcomes of simulation experiments used to support the validity of the proposed computational procedure. Section 5 shows the main results, distinguishing between in-sample goodnessof-fit and out-of-sample forecasting accuracy and some robustness checks. Section 6 concludes with final remarks and future research directions. 

#### **2. Forecasting house prices growth rates in the US states** 

We now present the approach adopted for forecasting house price growth in the US states. Section 2.1 briefly describes the data, while Section 2.2 discusses the forecasting methodology. 

#### _2.1. Data_ 

We consider the average house prices in the 48 continental US states for the period 1975–2023. Alaska and Hawaii are not included in the sample. The data source is the Federal House Finance Agency website.<sup>2</sup> The time 

2 Data can be retrieved at the following link https://www.fhfa.gov/. 

399 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 



**Fig. 1.** Temporal evolution of regional house prices in the US (1975 = 100). 

series are sampled quarterly, so we have _T_ = 193 temporal observations for _N_ = 49 cross-sectional units. The temporal evolution of the regional house prices in the US is shown in Fig. 1. 

All the price indices show a clear positive trend, with a large downturn in correspondence with the 2007–2008 great financial crisis. Due to the nonstationarity of the prices time series, we consider the growth rates. The data we consider are georeferenced. 

#### _2.2. Forecasting model_ 

In this paper, we adopt a suitably augmented Panel VAR model, which includes global and cluster-specific factors. A Panel VAR is a popular tool in macroeconomic forecasting ( _e.g._ see Bai, Carriero, Clark, & Marcellino, 2022; Dées & Güntner, 2017; Feldkircher, Huber, & Pfarrhofer, 2020). This allows for the introduction of US state-specific fixed effects to capture the time-invariant state-specific factors not considered by the global and cluster-specific factors. 

Let **y** _i,t_ be a _P_ -dimensional vector including a set of _P_ endogenous variables for the _i_ th ( _i_ = 1 _, . . . , N_ ) US state at time _t_ ( _t_ = 1 _, . . . , T_ ). The Panel VAR( _L_ ) can be written as follows 



where **_µ_** _i_ is an _P_ -dimensional vector of time-invariant fixed effects, specific to each _i_ th US State, **A** _l_ is the _P_ × _P_ matrix of coefficients for the _l_ th lag, **y** _it_ − _l_ is the _P_ - dimensional vector associated with the _l_ th lag of **y** _it_ and there are _εi,t_ i.i.d. disturbances. We assume that all roots of **A** are outside the unit circle, and hence, we deal with a stationary Panel VAR. 

Let us denote _xit_ the house price growth rates in the _i_ th US state at time _t_ . We define **f** 0 _t_ the _R_ -dimensional vector ( _r_ = 1 _, . . . , R_ ) with global factors at time _t_ affecting all the series _xit_ , and **f** _kt_ the _Rk_ dimensional vector ( _rk_ = 1 _, . . . , Rk_ ) of latent factors at time _t_ , affecting only the 

units belonging to the _k_ th cluster. We can estimate a Panel VAR given **y** _it_ = [ _xit ,_ **f**<sup>′</sup> 0 _t_<sup>_,_</sup><sup>**f**′</sup> _kt_<sup>]′.</sup> 

The parameters are estimated using the fixed-effects approach, and the fixed effects are then estimated following (Sigmund & Ferstl, 2021). To choose the optimal number of lags to include, we rely on the minimization of the BIC criterion ( _e.g._ see Han, Phillips, & Sul, 2017). 

In the case of a Panel VAR(1), the forecasts for _t_ + 1 are given by 



where **y** _i,t_ = [ _xit ,_ **f**<sup>′</sup> 0 _t_<sup>_,_</sup><sup>**f**</sup> _kt_<sup>′]′.Asimilarequationcanbe</sup> used for larger Panel VAR orders. We then compare, from both in-sample fitting and out-of-sample forecasting, the following models 

1. (m1): a Panel VAR with both global and clusterspecific factors **y** _it_ = [ _xit ,_ **f**<sup>′</sup> 0 _t_<sup>_,_</sup><sup>**f**′</sup> _kt_<sup>]′;</sup> 

2. (m2): constrained version of (m1) where only the global latent factors are considered and the clustered factors are excluded **y** _it_ = [ _xit ,_ **f**<sup>′</sup> 0 _t_<sup>]′;</sup> 

3. (m3): baseline model where only the lags of house price growth rates are considered for forecasting. 

We are interested in evaluating if the information included in the cluster-specific factors helps out-of-sample forecasting the house price growth rates. Therefore, we consider the m1 model as the main benchmark. We find evidence favouring cluster-specific factors in house price forecasting if the model m1 provides better forecasts outof-sample than the alternatives, which are all restricted versions. 

The cluster structure and the factors need to be estimated before forecasting the house price growth rates with the Panel VAR (1). The following section discusses the computational procedure for estimating the factors and the clustering structure. In particular, our computational procedure accounts for the spatial dimension while clustering US states to enhance the cluster-specific factors capturing spatial information. 

400 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

#### **3. Estimating latent factors with spatio-temporal clustering** 

Let us define with **X** a _T_ × _N_ a matrix of time series ( _xi,t_ ; _i_ = 1 _, . . . , N_ ; _t_ = 1 _, . . . , T_ ). We assume that **X** can be written as a linear combination of _R_ ( _r_ = 1 _, . . . , R_ ) global factors, _Rk_ ( _rk_ = 1 _, . . . , Rk_ ) specific factors that differ for each of the _K_ ( _k_ = 1 _, . . . , K_ ) clusters and an idiosyncratic noise **_η_** , that is, 



**F** 0 is the matrix of _T_ × _R_ global factors, while **_Λ_** 0 = [ **_Λ_**<sup>′</sup> 01<sup>| · · · |</sup><sup>**_Λ_**′</sup> 0 _k_<sup>| · · · |</sup><sup>**_Λ_**′</sup> 0 _K_ ]′ is the _N_ × _R_ matrix of global factor loadings, with **_Λ_** 0 _k_ the _Nk_ × _R_ global factor loadings for the time series belonging to the _k_ th cluster. Moreover, **F** _k_ is _T_ × _Rk_ matrix of the _Rk_ factors specific to the _k_ th ′ cluster and **_Λ_** _k_ =<sup>[</sup> **0**<sup>′</sup> _k_ 1<sup>| · · · |</sup><sup>**_Λ_**</sup> _kk_<sup>′| · · · |</sup><sup>**0**′</sup> _kK_ ] is the _N_ × _Rk_ matrix of cluster-specific factor loadings, with **_Λ_** _kk_ be the loading matrix for the factors affecting only the _Nk_ time series in the _k_ th cluster. Without loss of generality, we assume that the columns of **X** are ordered by cluster. We call (3) a Clustered Factor Model (CFM). 

Following (Alonso et al., 2020), we consider the usual model assumptions required for the existence and identification of global and cluster-specific factors.<sup>3</sup> 

First, we assume a fixed number of clusters _K >_ 1. Then, we assume orthonormal loading matrices, that is, **_Λ_**<sup>′</sup> 0<sup>**_Λ_**0=</sup><sup>**I**</sup><sup>_R_,where</sup><sup>**I**</sup><sup>_R_istheidentitymatrixoforder</sup><sup>_R_,</sup> **_ΛΛ_**<sup>′</sup> _k_<sup>′</sup> 0 _,_<sup>**_Λ_**</sup> _k_<sup>**_Λ_**</sup><sup>_kk_=</sup><sup>_,k_=</sup><sup>**_Λ_**′</sup> _k_<sup>**0**</sup> _,k_<sup>_R_</sup><sup>**_Λ_**×</sup><sup>_Rk_</sup> _k_<sup>_,k_,and=</sup><sup>**I**</sup><sup>_R_diagonal</sup> _k_<sup>for</sup><sup>_k_=covariance1</sup><sup>_, . . . , K_matrixand</sup><sup>**_Λ_**′</sup> 0<sup>of</sup><sup>**_Λ_**</sup><sup>_k_the=</sup> factors. Furthermore, cross-loadings are not allowed, and thus **_Λ_**<sup>′</sup> _k_<sup>**_Λ_**</sup><sup>_k_′=</sup><sup>**0**</sup><sup>_R_</sup> _k_<sup>×</sup><sup>_R_</sup> _k_ ′<sup>,for</sup><sup>_k_=</sup><sup>_k_′.Weassumetheidiosyn-</sup> cratic terms to have some weak forms of dependency, as discussed in Bai (2003) and Wang (2010). In particular, we allow for temporal and cross-sectional dependence and heteroskedasticity. 

#### _3.1. Computational procedure_ 

Under the assumption that _R_ global and _Rk_ clustered factors exist, two issues need to be addressed. First, we must estimate the unknown parameters: the unobservable factor structure and corresponding loadings. Second, we must estimate the number of _K_ clusters and the corresponding factors. These two problems are inevitably related. Indeed, the number of clustered factors depends on the global factors as they represent the latent variables explaining fluctuations of the time series in a cluster, which is not explained by the global factors. However, consistent estimation of a global factor cannot assume the absence of any clustered (local) factor. Indeed, we could get biased identification of the global factors if we ignore clustered factors in the estimation process. Thus, the two problems have to be solved iteratively. In what follows, 

> 3 Following (Alonso et al., 2020), we refer to the assumptions A, B, C, D and E of Wang (2010), which extends (Bai, 2003) to the case of group-specific factors. 

we propose an iterative procedure for overcoming this issue. 

First of all, we estimate a suitable initial number of global factors _R_ in the absence of a clustering structure. According to Bai and Ng (2002), this can be obtained by minimizing 



where **_λ_** _i_ 0 is the _R_ -dimensional vector of global factor loadings for the _i_ th unit and **f** 0 _t_ the _R_ -dimensional vector of the global factors at time _t_ . By assuming _T > N_ , the _R_ global factors can be consistently estimated with the Principal Component Estimator (PCE), 



given that **_Λ_**<sup>ˆ</sup> 0 is estimated by ~~√~~ _N_ times the eigenvectors of **X**<sup>′</sup> **X** associated with the _R_ largest eigenvalues. Note that (6) equals the solution of the minimization problem (4) given the number of factors _R_ . To estimate the _Rk_ clustered factors, we consider the ′ residuals<sup>ˆ</sup> **E** = **X** −<sup>ˆ</sup> **F** 0 **_Λ_**<sup>ˆ</sup> 0<sup>.Thematrixˆ</sup><sup>**E**containsthe</sup> information of **X** , which is not explained by the global factor structure. Thus, we estimate the clustering structure based on<sup>ˆ</sup> **E** and identify the factors within each cluster. 

In principle, any clustering approach can be used to determine the clustering structure of the residuals<sup>ˆ</sup> **E** . In our case, we suppose that<sup>ˆ</sup> **E** is a matrix of georeferenced time series, and thus either spatial, temporal or spatial– temporal approaches can be used. Therefore, we obtain a _spatially clustered factor model_ if only the spatial dimension is considered, a _clustered factor model_ if only the temporal dimension is considered and a _spatio-temporal clustered factor model_ if both are included. The following sub-section provides more details on clustering. For each _k_ th cluster, the _Rk_ number of factors needs to be estimated. The cluster-specific counterpart of (6) can be used for this aim, and the corresponding _Rk_ factors can be estimated as 



′ ′ with **_Λ_**<sup>ˆ</sup> _k_ = **0**<sup>′</sup> _k_ 1<sup>| · · · | ˆ</sup><sup>**_Λ_**</sup> _kk_<sup>| · · · |</sup><sup>**0**′</sup> _kK_ and, by defining<sup>ˆ</sup> **E** _k_ <u>[</u> ] the columns of **_Λ_** ˆ _kk_ as<sup>√</sup> _Nk_ times<sup>ˆ</sup> **E** belonging to thethe eigenvectors _k_ th cluster, we computeof the matrix<sup>ˆ</sup> **E**<sup>′</sup> _k_<sup>ˆ</sup><sup>**E**</sup><sup>_k_</sup> associated with the _Rk_ largest eigenvalues. 

As previously highlighted, stopping at this stage would not guarantee an optimal solution. Indeed, we need to estimate the number of global factors under the presence of suitably identified cluster-specific factors. In other words, we need to remove the information of the clustered factors from the whole data matrix **X** . A suitable operation is 



401 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

The number of factors can be estimated by a modified version of (4), that is, 



The identification of the new global factors<sup>˜</sup> **F** 0 relies on the matrix<sup>ˆ</sup> **U** so we use the PCE in (6). Subsequently, the new cluster-specific factors<sup>˜</sup> **F** _k_ are identified considering the updated residuals<sup>˜</sup> **E** . However, we first need to remove the effect of previously identified clustered factors, so we consider 



and the estimation procedure continues until convergence. 

A few remarks on the iterative procedure are needed. First, we note that the loss function adopted in the iterative procedure, consistent with (Ando & Bai, 2017) and Alonso et al. (2020), is least squares based and is similar to the Iterative PCA adopted in Wang (2010). Second, it relates to the EM algorithm in that it alternates two main steps, the cluster assignment (the E-step) and the parameter ( _i.e._ factors and loadings) estimation (the M-step), iteratively until convergence. However, the clustering assignment in the E-step depends on a hierarchical procedure discussed in Section 3.2. Third, we intuitively set that if a _k_ th cluster is a singleton, there is no local factor to estimate in that cluster. Even though we assume that a clustered factorial structure exists within each cluster, more sophisticated rules can be easily considered for testing whether a factorial structure at the cluster level exists. Moreover, alternative procedures can also be used for estimating the number of factors (Ahn & Horenstein, 2013). Fourth, we assume a static approximate factor structure (Bai & Ng, 2002; Stock & Watson, 2002). As shown in Wang (2010), including a finite number of lagged factors does not invalidate the properties of the Iterative PCA. However, other approaches for dynamic factors estimation, such as the dynamic principal component (DPCA, Brillinger, 2001; Forni, Hallin, Lippi, & Reichlin, 2000, 2005) and the generalized dynamic principal component (GDPCA, Peña & Yohai, 2016) may be used in this setting. Then, we notice that the proposed approach is computationally feasible if _N > T_ and _T > N_ . As we intend to cluster housing prices of US states where _T > N_ , the procedure highlighted so far is computationally very fast. When _N > T_ , instead, a computationally suitable approach estimates the factor matrix as √ _T_ times the eigenvectors corresponding to the _R_ largest eigenvalues of the matrix **XX**<sup>′</sup> and **_Λ_** 0 = **F**<sup>′</sup> 0<sup>**X**thematrixofglobal</sup> factor loadings. The same applies to clustered factors. This second solution is recommended when dealing with, for example, housing prices in metropolitan areas where the cross-sectional dimension _N_ is usually larger than _T_ . The above-described procedure is better suited when (relatively long) georeferenced time series are considered. 

Finally, we briefly remark that the main consequence of enhancing spatial clustering is an increase in the crosssectional correlation of idiosyncratic errors within each 

cluster. As discussed in the introduction, this is a typical feature in regional factor models. Given that a very general form of cross-sectional dependence is allowed, introducing spatial clustering does not invalidate the properties of the principal component approach for global and cluster-specific factor estimation once the cluster structure has been identified. 

#### _3.2. Hierarchical spatio-temporal clustering_ 

In what follows, we discuss the procedure while clustering residuals in the computational estimation of the CFM. Different approaches can be used for this task. The clustering approach adopted defines the nature of the clustered factor model considered, which is spatial, temporal, or spatio-temporal. Spatially clustered factor models are quite simple and define the partition based only on the spatial dimension. The CFM algorithm becomes a two-step procedure in this simple case because the clustering structure does not change with the iterations. Temporally clustered factor models, such as Ando and Bai (2017) and Alonso et al. (2020), do not consider the spatial dimension, which can be less appropriate in some empirical instances. Therefore, we propose a suitable spatio-temporal clustering approach in updating the CFM algorithm. 

The use of partitional approaches is not recommended in this context to reduce the computational burden of the procedure. Indeed, these algorithms, such as _k_ -means or _k_ -medoids, require the apriori selection of the number of clusters _G_ . Therefore, as in Alonso et al. (2020), we prefer hierarchical algorithms to reduce the degree of freedom of the problem. 

Following Chavent, Kuentz-Simonet, Labenne, and Saracco (2018), Mattera and Franses (2023) and Bucci, Ippoliti, Valentini, et al. (2023), we consider a Wardlike spatio-temporal hierarchical clustering algorithm for updating the clustering structure at each iteration. Let us consider a set of _N_ ( _i_ = 1 _, . . . , N_ ) statistical units and let **D** = [ _dij_ ] be the _N_ × _N_ dissimilarity matrix associated with the _N_ units, with _dij_ being the dissimilarity measure between two units _i_ and _j_ . Let us define _PK_ = ( _C_ 1 _, . . . , CK_ ) a partition of the dataset into _K_ clusters. In the standard cross-sectional clustering, we can express the within-clusters inertia _Ck_ ( _k_ = 1 _, . . . , K_ ) as follows: 



with _wi_ the weight associated to the _i_ th statistical unit. Without any a priori information, it is common to set _wi_ = 1 _/N_ . The dissimilarity matrix **D** is computed in the attribute space, considering a set of _P_ ( _p_ = 1 _, . . . , P_ ) variables describing the _N_ statistical units. In spatio-temporal data, the attribute space is represented by observing an attribute over _T_ ( _t_ = 1 _, . . . , T_ ) time periods and by the spatial dimension. 

We define the spatio-temporal inertia of a _Ck_ ( _k_ = 1 _, . . . , K_ ) cluster as the convex combination between the attribute inertia and the inertia of spatial clusters. In 

402 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

other words, in the case of spatio-temporal clustering, (11) becomes: 



where _d_<sup>2</sup> _ij,t_<sup>isthesquareddistancebetweenunits</sup><sup>_i_and</sup><sup>_j_</sup> over the (temporal) attribute space and _d_<sup>2</sup> _ij,g_<sup>is the squared</sup> distance in the geographical space. The smaller the inertia _I (Ck)_ is, the more homogenous are the observations in cluster _Ck_ . Note that the spatio-temporal inertia (12) is a convex combination of temporal inertia and spatial inertia. Moreover, spatio-temporal inertia depends on the so-called _mixing parameter α_ , which in our case can be interpreted as the relevance of spatial information relative to the temporal information. 

The resulting hierarchical clustering approach considers an initial partition with _N_ clusters of singletons. Then, the algorithm aggregates two clusters at each step according to an objective function related to the withincluster inertia. The procedure adopted in determining spatial weights _α_ aims at finding a value representing the best compromise between loss in the temporal space and loss of geographical homogeneity. The procedure adopted in our paper is explained with more details in Chavent et al. (2018) and Mattera and Franses (2023). Let us define 



the spatio-temporal inertia of a _k_ th cluster for a given value of the mixing parameter _α_ . The total spatio( _α_ ) temporal inertia _W PK_ equals the sum of the within( ) ( _α_ ) cluster inertia of its _K_ clusters, _I Ck_ . To choose _α_ , we ( ) compare the proportion of the total inertia explained by the partition obtained with the temporal dimension 



with the proportion associated with the spatial dimension 



for different _S_ values of _α_ . For example, we can consider _α_ = { _α_ 1 = 0 _, α_ 2 = 0 _._ 01 _, . . . , αS_ −1 = 0 _._ 99 _, αS_ = 1}. We notice that _Wt (P_ 1 _)_ and _Wg (P_ 1 _)_ are the total inertia using ( _α_ ) temporal and geographical distance only, _i.e. W PK_ ( ) with _α_ = 0 and _α_ = 1, respectively. 

The difference between the two criteria for all the _S_ values of _α_ provides a simple way for choosing the mixing parameter, that is, when the difference between the loss of temporal homogeneity and larger geographical cohesion, obtained through increasing values of _α_ , is minimum. 

We need only to define both temporal and spatial dissimilarity measures. A suitable choice, which is very common for clustering economic time series, is the 

correlation-based distance (Maharaj, D’Urso, & Caiado, 2019) 



with _ρ_ ˆ _i,j_ being the sample correlation coefficient between the two time series _i_ and _j_ . Notice that the correlationbased distance is meaningful if stationary time series are considered. Other dissimilarity measures for time series data can also be considered, such as cross-correlationbased (Alonso & Peña, 2019). For nonstationary series, suitable alternative distances are the ARIMA (Piccolo, 1990) or the feature-DTW (Franses & Wiemann, 2020) distances. Spatial clustering, instead, can be achieved in different ways, depending mainly on the measure used to quantify proximity. Here, we consider a spatial dissimilarity based on the geographical distances among the statistical units, measured in terms of latitude and longitude 



Using dissimilarity (14) ensures that statistical units closer in the geographical space are clustered together. The distance (14) is not the only possible approach for enhancing spatial clustering (Bucci et al., 2023; Fouedjio, 2016; Mattera, 2022). Nevertheless, as shown in Chavent et al. (2018), if combined with another non-spatial dissimilarity, it can be successfully used to provide a soft spatial constraint to the final partition. 

#### **4. Simulation study** 

In what follows, we assess the performance of the proposed computational procedure through a simulation study. In particular, we assess the accuracy in clustering and forecasting the statistical units. Moreover, we evaluate the suitability of the Elbow criterion in correctly choosing the number of clusters _K_ and shed light on the mechanism behind the selection of the mixing parameter _α_ . The proposed approach is compared with the (Ando & Bai, 2017) which does not account for the spatial dimension in the clustering task. The clustering accuracy is evaluated in terms of the Rand index (RI, Hubert & Arabie, 1985), which lies between 0 and 1. The higher the value of RI is, the better the clustering accuracy. Given that the true labels of the units are known in the simulated environment, we have that the RI equals 1 in the case of perfect overlap in clustering obtained by the method and the true partition. The forecasting ability is evaluated ˆ 2<sup>]</sup> by computing the loss _L_ **X** ˆ _,_ **X** ˜ = _E_ [( **X** _T_ +1| _T_ −˜ **X** _T_ +1| _T_ ) , that is the expectation of the squared difference between the one-step-ahead forecast obtained with the estimated factors˜ **X**<sup>ˆ</sup> _T_ +1| _T_ and those obtained with the true values **X** accuracy. _T_ +1| _T_ . Hence, the lowerTo obtain one-step-ahead _L_ **X** ˆ _,_ **X** ˜ , the better is the forecastingforecasts, we use the Panel VAR(1) model (2) with the fixed-effects estimator as discussed in Section 2.2. We simulate 1000 datasets, averaging the results over the simulations. 

To include a spatial dimension in the simulation study consistent with our empirical application to house prices, 

403 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 





**Fig. 2.** Clustering structures considered for the simulation experiments. 

we simulate _N_ = 49 statistical units representing the US states with their spatial coordinates. We assume the presence of _K_ = 3 and _K_ = 4 clusters, respectively, which are shown in Fig. 2 

Given the _N_ = 49 units, we consider one global factor and one local factor for each cluster. Following (Ando & Bai, 2017), under the DGP as in (3), we simulate the global factor from a uniform [0 _,_ 1] distribution and the factor loadings as uniform [−2 _,_ 2] variables. Moreover, each element of the cluster-specific factors is simulated from standard Normal variables _N_ (0 _,_ 1) and each element of the factor-loading matrix follows also _N_ (0 _,_ 1). Then, we consider two alternative specifications for the error term. In the first scenario (Scenario I), we allow some crosssectional correlation between the errors within each cluster, which are simulated from a multivariate normal distribution with zero mean and covariance matrix with constant correlation _ρij_ = 0 _._ 3 if _i_ and _j_ belong to the 

same cluster, and _ρij_ = 0 otherwise. The errors associated with statistical units placed in different clusters are independent. 

In the second scenario (Scenario II), we assume that correlations depend on geographical proximity. In particular, we assume that the correlation between two units _i_ and _j_ increases with smaller geographical distances. To be more precise, let us define<sup>˜</sup> _dij,g_ the normalized geographical distance, that is<sup>˜</sup> _dij,g_ = _dij,g /_ max( _dij,g_ ), such that all the values ofthe correlation<sup>˜</sup> _dij,g_ betweenfall in the intervalunits _i_ and [0 _j,_ 1equals]. We assume that ˜ _ρij_ = _ρ_ ˜ _ijdij,g_ . In this way, we simulate a covariance matrix where the actual correlations ˜ _ρij_ depend on the spatial correlation ( _ρij_ ), which increases faster with decreasing geographical distance. Indeed, large values of<sup>˜</sup> _dij,g_ indicate that the time series associated with the states _i_ and _j_ are very far in the geographical space. For<sup>˜</sup> _dij,g_ → 1, so for very large distances, we have that ˜ _ρij_ → _ρij_ while for<sup>˜</sup> _dij,g_ → 0, so 

404 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

**Table 1** 

Simulation study results under Scenario I. Rand Index is the accuracy ofis athemeasureclusteringof resultingforecastingfromaccuracy.the approachThe resultson thearerows,obtainedwhilewith _L_ **X** ˆ _,_ **X** ˜ an average of 1000 simulations; standard deviations are shown in <u>parentheses.</u> 

|Panel A: _T_ = 100|||||
|---|---|---|---|---|
||Rand Ind|ex|_L_ˆ**X**_,_˜**X**||
||_K_ = 3|_K_ = 4|_K_ = 3|_K_ = 4|
|Ando and Bai (2017)|0.539|0.596|5.646|5.200|
||(0.03)|(0.03)|(3.719)|(3.270)|
|Our method|0.674|0.731|5.534|5.197|
||(0.03)|(0.03)|(3.702)|(3.316)|
|Panel B: _T_ = 200|||||
||Rand Ind|ex|_L_ˆ**X**_,_˜**X**||
||_K_ = 3|_K_ = 4|_K_ = 3|_K_ = 4|
|Ando and Bai (2017)|0.533|0.587|4.025|3.731|
||(0.03)|(0.04)|(2.687)|(2.209)|
|Our method|0.675|0.732|3.915|3.567|
||(0.03)|(0.03)|(2.660)|(2.223)|
|Panel C: _T_ = 400|||||
||Rand Ind|ex|_L_ˆ**X**_,_˜**X**||
||_K_ = 3|_K_ = 4|_K_ = 3|_K_ = 4|
|Ando and Bai (2017)|0.529|0.576|2.799|2.608|
||(0.02)|(0.04)|(1.868)|(1.568)|
|Our method|0.677|0.733|2.673|2.521|
||(0.03)|(0.03)|(1.796)|(1.617)|



for small distances, we have that ˜ _ρij_ → 1. In what follows, we show the results assuming _ρij_ = 0 _._ 1.<sup>4</sup> 

Given the two scenarios, we consider different time series lengths, that is, _T_ = 100 _,_ 200 _,_ 400, and we keep _N_ = 49 fixed. The results of the simulations under Scenario I are shown in Table 1, while those under Scenario II are in Table 2. The column Rand Index measures the (average) accuracyforecasting accuracy. DGP1 assumes independence amongof the clustering, while _L_ **X** ˆ _,_ **X** ˜ is a measure of error terms, while DGP2 assumes some cross-sectional correlation exists. The results are averaged over 1000 simulated datasets, while the standard deviations of the results are in parentheses. 

Considering the results of both simulated scenarios, we note that the clustering accuracy does not vary much when increasing the sample size from _T_ = 100 to _T_ = 400. The proposed spatio-temporal approach shows better clustering accuracy than the temporal approach proposed by Ando and Bai (2017). Indeed, the rate of correct classification is 0.7 for our spatio-temporal approach, while it is about 0.5 for the (Ando & Bai, 2017) method. Moreover, in the case of Scenario II, the clustering accuracy improves compared to the case of Scenario I due to the increasing importance of the spatial dimension. In terms of forecasting accuracy, both Tables 1 and 2 show that our proposed spatio-temporal approach provides better results. Moreover, forecast accuracy improves in both simulated scenarios with increasing _T_ , while the standard deviation decreases with increasing temporal observations. 

Finally, we evaluate the accuracy of the Elbow criterion in selecting the number of clusters _K_ , and the (Chavent 

> 4 The results assuming _ρij_ = 0 _._ 05 and _ρij_ = 0 _._ 01 are available upon request, and lead to qualitatively similar findings. 

**Table 2** 

Simulation study results under Scenario II. Rand Index is the accuracy ofis athemeasureclusteringof resultingforecastingfromaccuracy.the approachThe resultson thearerows,obtainedwhilewith _L_ **X** ˆ _,_ **X** ˜ an average of 1000 simulations; standard deviations are shown in <u>parentheses.</u> 

|Panel A: _T_ = 100|||||
|---|---|---|---|---|
||Rand Ind|ex|_L_ˆ**X**_,_˜**X**||
||_K_ = 3|_K_ = 4|_K_ = 3|_K_ = 4|
|Ando and Bai (2017)|0.551|0.616|10.327|10.155|
||(0.02)|(0.02)|(6.239)|(5.907)|
|Our method|0.696|0.772|10.222|10.181|
||(0.03)|(0.03)|(6.469)|(6.210)|
|Panel B: _T_ = 200|||||
||Rand Ind|ex|_L_ˆ**X**_,_˜**X**||
||_K_ = 3|_K_ = 4|_K_ = 3|_K_ = 4|
|Ando and Bai (2017)|0.551|0.614|7.086|7.244|
||(0.02)|(0.02)|(4.173)|(4.669)|
|Our method|0.696|0.772|6.981|7.236|
||(0.03)|(0.03)|(4.359)|(4.781)|
|Panel C: _T_ = 400|||||
||Rand Ind|ex|_L_ˆ**X**_,_˜**X**||
||_K_ = 3|_K_ = 4|_K_ = 3|_K_ = 4|
|Ando and Bai (2017)|0.548|0.612|5.189|5.221|
||(0.02)|(0.02)|(3.365)|(3.114)|
|Our method|0.697|0.771|5.070|5.201|
||(0.03)|(0.03)|(3.339)|(3.321)|



et al., 2018) procedure in choosing the mixing parameter _α_ . Fig. 3 summarizes the results on the choice of the number of clusters _K_ . We consider the values _T_ = 100, _T_ = 200 and _T_ = 400, and both _K_ = 3 and _K_ = 4 for both the considered scenarios. 

Fig. 3 indicates that the median of the boxplot equals the correct number of factors using the Elbow method. This holds for all the considered values of _T_ . The variability of the results reduces for larger _T_ . Regarding the mixing parameter _α_ choice, the boxplots with the results of the simulations for the different scenarios are shown in Fig. 4. 

We find that _α_ is lower when the correlations, used for computing the distance in the temporal domain _dij,t_ , do not depend on the spatial information. This is the case of Scenario I. When the correlations lead to some spatial clustering, for instance, because they depend on the spatial dimension as in Scenario II, we find the mixing parameter _α_ to be more important. These results confirm that the procedure adopted in the paper for selecting _α_ is appropriate. It also suggests that the selected value of _α_ provides relevant information on the importance of spatial dimension in a given dataset. The larger the _α_ , the more relevant the spatial dimension for determining the clustering structure of the data. 

#### **5. Forecasting US house price growth rates: results** 

We now empirically evaluate the usefulness of clusterspecific factors in forecasting the house price growth rates in the US states. For the out-of-sample forecasting experiment, a rolling-window procedure is adopted. The sample is divided into a train and a test sample. We leave the last eight years of observations for testing. A fixed window of forty years ( _M_ = 160) quarters is adopted, and the 

405 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 







**Fig. 3.** Optimal _K_ selection with the Elbow criterion (our procedure), for different Scenarios ( _T_ = 100 _,_ 200 _,_ 400). ‘‘K3.1’’ means _K_ = 3 under Scenario I, while ‘‘K3.2’’ means _K_ = 3 under Scenario II. ‘‘K4.1’’ means _K_ = 4 under Scenario I, and ‘‘K4.2’’ means _K_ = 4 under Scenario II. 







**Fig. 4.** Optimal _α_ selection for different Scenarios ( _T_ = 100 _,_ 200 _,_ 400). ‘‘A3.1’’ means _K_ = 3 under Scenario I, while ‘‘A3.2’’ means _K_ = 3 under Scenario II. ‘‘A4.1’’ means _K_ = 4 under Scenario I, and ‘‘A4.2’’ means _K_ = 4 under Scenario II. 

406 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 



**Fig. 5.** Spatio-temporal clustering of the US house prices growth. 

automatic model selection is performed to determine the optimal number of lags to include in each recursion. The number and the composition of clusters are allowed to vary during the rolling window procedure, and the global and clustered factors are re-estimated at each step. Given the estimated parameters, a one-step-ahead forecast is produced. Then, a new observation is included in the sample while the oldest one is removed. The procedure is repeated until no new observation is available. 

the forecasting process. Therefore, we adopt the (Clark & West, 2007) test based on adjusted errors for accurate testing. Given a generic _i_ th unit (we omit the _i_ th subscript for easy reading), let us define _e_ ˆ1 _,t_ and _e_ ˆ2 _,t_ , _t_ = _M_ + 1 _, . . . , T_ , the one-step-ahead forecast errors of the parsimonious model and the alternative one, reˆ ˆ 2<sup>]</sup> spectively. Let _f_<sup>ˆ</sup> _t_ = _e_<sup>2</sup> 1 _,t_<sup>−</sup> [ _e_<sup>2</sup> 2 _,t_<sup>−(</sup><sup>_x_ˆ1</sup><sup>_,t_−ˆ</sup><sup>_x_2</sup><sup>_,t_</sup> ) be the so-called adjusted-MSE (Clark & West, 2006). Let _f_<sup>¯</sup> be the corresponding sample average, that is, _f_<sup>¯</sup> = ( _T_ − _M_ )<sup>−1 ∑</sup><sup>_T_</sup> _t_ = _M_ +1<sup>_f_ˆ</sup><sup>_t_.The(Clark&West,2007)teststatisticis</sup> 

To evaluate forecasting accuracy, we rely on two commonly employed accuracy metrics, namely the Root Mean Squared Error (RMSE), that is 



with _V_ [·] be the variance. Under the null hypothesis, the two models provide equally good forecasts. Clark and West (2007) recommend constructing the usual onetailed t-test to assess if the adjusted difference in mean squared errors is zero. For the sake of robustness, we also consider the (Diebold & Mariano, 2002) predictive accuracy test. 

where ˆ _xi,t_ represents the forecast at time _t_ for the _i_ th US state’s house price growth rate and _xi,t_ the realized value, and the Mean Absolute Error (MAE), that is, 



#### _5.1. Clustering results_ 

Notice that the models (m2) and (m3) are nested into (m1). It is interesting, therefore, to test if the additional information considered in the full models has a statistically significant role in more accurately forecasting house price growth rates. We conjecture that the model with global and cluster-specific factors provides more accurate out-of-sample forecasts than the nested models. Put differently, the cluster-specific factors are useful for forecasting purposes. As highlighted by Clark and West (2006), the parsimonious models should have smaller prediction errors than more complex ones in which they are nested. Indeed, parsimonious models gain accuracy by setting the parameters that are zero in the population to zero, while the more complex models introduce noise into 

The number of clusters is estimated through the Elbow criterion, and the resulting partition into _K_ = 4 clusters is shown in Fig. 5. 

The spatial weight computed in the spatio-temporal clustering algorithm is _α_ = 0 _._ 6, thus suggesting that the spatial dimension is more relevant than the temporal one in discriminating the data and determining the nature of the clustered factors. At the same time, the temporal dimension is not negligible. Thus, our spatio-temporal approach is recommended instead of a pure spatial or pure temporal approach. Moreover, we find that _R_ = 1 for the global factor and _Rk_ = 1 for all four clusters. The partition in Fig. 5 highlights that local factors arise in the 

407 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 



**Fig. 6.** Temporal evolution of the estimated factors: both global and local. 

west (Cluster 2) and in the north-east of the US (Cluster 4), as well as two distinct clustering factorial structures that exist in the centre of the US territory. In particular, it is interesting to notice that in Cluster 4 we have urban states with higher population densities, like New York, Massachusetts, and New Jersey, which tend to have more competitive housing markets with higher property prices. 

Cluster 2, instead, includes Pacific states with higher housing price growth rates than the national average. California, in particular, is known for its high-priced housing market, with cities like San Francisco and Los Angeles experiencing some of the highest home price changes in the country. Oregon, Washington, and Nevada also have areas with relatively high housing price growth rates, especially in major metropolitan cities such as Portland and Seattle. Cluster 1 includes most coastal states compared with Cluster 3, but differences between the two clusters can be better exploited considering the estimated factors in Fig. 6. The solid black line in Fig. 6 represents the global factor, while the local factors have the same colours as in Fig. 5. The local factor of Cluster 1 is characterized by large volatility in the first years of the sample compared to other clusters. In contrast, Clusters 2 and 3 local factors show larger variability for most of the considered time span. Instead, the local factor of Cluster 1 shows the lowest level of variability compared to the others. Moreover, while most of the clusters show an increase in the local factors since 2020, Cluster 3 is the only one with a local factor with negative values. 

#### _5.2. In sample fit_ 

Given the estimated latent (global and clustered) factors, we estimate the optimal lag length of the Panel VAR. Considering the values of the BIC-type criterion ( _e.g._ Han et al., 2017) for different values of _L_ ∈ 1 _, . . . ,_ 5, we choose _L_ = 1 as it minimizes the BIC. We compare the Panel 

VAR(1) models ( _i.e._ m1–m3) in terms of in-sample RMSE and MAE, given the cluster structure into _K_ = 4 groups. Fig. 7(a) shows the distribution of the _N_ = 49 US states in terms of in-sample fit under RMSE loss, while Fig. 7(b) in terms of MAE loss. Both figures consider the relative accuracy, given by the ratio between the in-sample fit of the competing models to the main benchmark, that is, the m1 model. Values larger than 1, highlighted with the red dashed line, indicate that model m1 provides a better insample fit ( _i.e._ lower RMSE or MAE) than the competing model. 

Fig. 7 shows that both boxplots, comparing the different models m2 and m3 with the full model m1, are above the dashed red line, and as such, indicating a better in-sample fit of the full Panel VAR model including both global and cluster-specific factors. Moreover, we consider the in-sample fit obtained in the rolling window procedure. We estimate the optimal lag order of the Panel VAR models in each iteration. Figs. 7(c) and 7(d) show the average distributions, that is, the average RMSE and MAE for each US state across all the rolling windows. The results are similar to those obtained considering the full sample, thus suggesting that using both global and cluster-specific factors improves the in-sample fit of the Panel VAR model. 

#### _5.3. Out of sample results_ 

Next, we investigate the accuracy of the model’s outof-sample forecasting. Figs. 8(a) and 8(b) show the distributions of the RMSE and MAE for each US state in the testing set. Also, in this case, the results are reported in terms of relative accuracy, where the accuracy of the full model, m1, is compared with those of the competing restricted Panel VAR models m2 and m3. Values larger than 1, indicated with a dashed red line, highlight that the 

408 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 





**Fig. 7.** Relative accuracy measures (RMSE and MAE) of the competing models compared with the model m1. Both full-sample and (averaged) rolling-window experiments are considered. Values larger than 1 (the red dashed line) indicate that m1 provides a better in-sample fit compared to the competing model. 

model, including cluster-specific factors, provides more accurate forecasts. 

In both figures, the boxplots are above the dashed red line, and therefore, the full model provides the most accurate out-of-sample forecasts for most US states. In particular, the median of the boxplots in terms of both accuracy measures is about 1.1. The cluster-specific factors are, however, not equally relevant across the US states. While these are very important in some states in predictive terms, they are not in others. Table 3 allows us to evaluate the differences at the state level. 

According to Table 3, we highlight that the clusterspecific factors provide better accuracy for the US states in all the clusters, except for those in Cluster 3. For these states, _i.e._ , the mountain states in the US centre, we find that the model with global factors only performs worse than the baseline model. However, the differences in terms of average losses are not very large. In fact, the average loss for the states in Cluster 3 is equal to 0.0221 for the full model (m1), 0.0211 for the model with global factors only (m2) and 0.0212 for the baseline model (m3). The cluster-specific factors allow for considerable improvements in out-of-sample forecasting accuracy for the remaining states. For instance, the RMSE for the full model in Cluster 1 equals 0.0159, while it takes values 0.0187 and 0.0188 for the restricted models m2 and m3, respectively. Therefore, we find that global factors alone perform worse than the baseline model for US states in the east of the US. Including cluster-specific factors significantly improves the forecasting performance. Similar 

findings are obtained for the US states in Cluster 2 and Cluster 4, for which the model with cluster-specific factors provides an average RMSE of 0.0199 for Cluster 2 and 0.0150 for Cluster 4,. In contrast, the model m2 performs worse than the baseline in both clusters. Interestingly, such regional differences in forecastability have also been acknowledged in other previous studies ( _e.g._ see Rapach & Strauss, 2009). 

Finally, we test the equality in the predictive accuracy of the full model m1 compared to both m2 and m3. In this setting, we also consider differences across the states. Table 4 shows the results of both the (Clark & West, 2007) test for nested models, and the (Diebold & Mariano, 2002) test. The results confirm that the differences in terms of forecasting accuracy described in Table 3 are statistically significant. Indeed, we reject the null hypothesis of the predictive accuracy tests for the US states in Clusters 1, 2 and 4. For the states in Cluster 3, however, we do not reject the null hypothesis of equal predictive accuracy. 

#### _5.4. Results with observable factors_ 

The results obtained in previous sub-sections consider lagged values of the house price growth rates and lags of latent factors, estimated with the computational procedure discussed in Section 3. However, the accuracy of the forecasts can be improved, including observable factors. For instance, Holly, Pesaran, and Yamagata (2010) found that real per capita income, the long-term interest rates 

409 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 





**Fig. 8.** Relative accuracy of the competing models with m1. 

and the global inflation rate are relevant predictors for house prices. In what follows, we include this source of additional information in the Panel VAR (1) and evaluate if cluster-specific factors are still useful even if observable factors are included in the forecasting model. 

Let us define by **z** _i,t_ the vector of _P_ observable factors for the _i_ th state at time _t_ . We consider the real per capita income, the long-term interest rates and the global inflation rate, and we estimate the following additional models 

1. (m4): Panel VAR where **y** _i,t_ = [ _xi,t ,_ **z**<sup>′</sup> _i,t_<sup>_,_</sup><sup>**f**′</sup> 0 _,t_<sup>_,_</sup><sup>**f**</sup> _k_<sup>′</sup> _,t_<sup>]′;</sup> 

2. (m5): constrained version of m4 without clustered factors, that is, **y** _i,t_ = [ _xi,t ,_ **z**<sup>′</sup> _i,t_<sup>_,_</sup><sup>**f**′</sup> 0 _,t_<sup>]′</sup> 

3. (m6): constrained version of m4 without factors, whereVAR; **y** _i,t_ = [ _xi,t ,_ **z**<sup>′</sup> _i,t_<sup>]′.ThisisthestandardPanel</sup> 

The difference between models m1 and m4 is that the last also includes observable factors, while the first does not. Fig. 9 shows the comparison in terms of relative accuracy measures between the models m5 and m6 with model m4. Both in-sample (Figs. 9(a) and 9(b)) and out-of-sample (Figs. 9(c) and 9(d)) results from the 

rolling-window experiments are considered. Values larger than 1 (the red dashed line) indicate that m4 provides better results than the competing model. 

The results shown in Fig. 9 align with those discussed in the previous subsection. The medians of the boxplots are consistently above the threshold of 1, suggesting that model m4, including cluster-specific factors, provides better results both in-sample and out-of-sample. This result holds for both RMSE and MAE accuracy measures. Table 5 shows the out-of-sample accuracy results for each state, while Table 6 shows the results of predictive accuracy tests. Regarding regional differences, we find that model m4, including cluster-specific factors, provides more accurate out-of-sample forecasts than models m5 and m6 for all the states in Clusters 1, 2 and 4. For states in these clusters, the relative accuracy measures (RMSE and MAE) are larger than 1, while for states placed in Cluster 3, we find relative accuracy measures lower than 1. The best results can be found for the states in Cluster 1, like in the previous experiment, without observable factors. Also, regarding statistical significance, we reject the null hypothesis of equal predictive accuracy for both CW and DM tests while comparing model m4 with m5 and m6 in 

410 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 





**Fig. 9.** Relative accuracy measures (RMSE and MAE) of the models m5 and m6 compared to m4. Both in-sample and out-of-sample results from the rolling-window experiments are considered. Values larger than 1 (the red dashed line) indicate that m4 provides better results compared to the competing model. 

the case of states in Clusters 1, 2 and 4. In contrast, we do not reject the null hypothesis for the states in Cluster 3. 

Finally, we compare the forecasting accuracy of the models, including observable factors, with model m1. The results are summarized by Fig. 10. Interestingly, we find that, while in-sample the model including observable factors m4 provides the best results, out-of-sample, we find that the model m1 has the lowest RMSE and MAE. Therefore, the model m1 is the most accurate out-of-sample. The results thus confirm that including global and clusterspecific factors allows for good forecasting performance. Moreover, Fig. 10 also suggests that model m4 provides better results than models m5 and m6. This highlights again that including both cluster factors and observable factors in the model significantly enhances its accuracy. 

#### **6. Final remarks** 

In this paper, we study cluster-specific factor models’ ability to forecast house price growth rates in the US, assuming unknown spatio-temporal clustering. We estimate the cluster structure of the US states directly from the data and assume that all the states in the same cluster share the cluster-specific latent factors. Moreover, we assume all the US states share the same global factor. In doing so, we follow the idea behind regional factor models, which have become increasingly popular in empirical studies conducted by central banks. Regional factor models are a particular type of factor model with a known 

clustering structure based on spatial information. Differently, however, we notice that the cluster structure depends not only on spatial information but also on the similarity of the temporal pattern of the housing market and propose a novel computational procedure. 

Our method provides a structured way of estimating the factors and the clusters. This is accomplished by estimating a factor model, boosting along the residuals, estimating a type of guided hierarchical clustering model, and estimating additional ‘‘local’’ clusters. The described process, which automatically estimates the number of global factors, the clustering structure and the number of clustered factors, is then iterated. In doing so, we combine the principal components approach for estimating factors and guided hierarchical clustering. The proposed dimension reduction implied by the algorithm is sensible, particularly when the spatial indexes can be clustered geographically, and geographic clusters have corresponding factors that predict the outcome. 

The novelties can be summarized as follows. First, we show that more accurate forecasts of house price growth rates can be achieved using cluster-specific factors. Forecasting models based on global factors only and models without factors provide less accurate forecasts out-ofsample. This evidence is confirmed by considering the results of predictive accuracy tests. Second, we adopt an unsupervised learning approach to build the clusters and propose a computational procedure that enhances spatial clustering. The main strength of the proposed method is that it does not require prior knowledge of the number 

411 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 









**Fig. 10.** Relative accuracy measures (RMSE and MAE) of the Panel VAR models with observable factors (m4–m6) compared to the Panel VAR with latent factors only (m1). Both in-sample and out-of-sample results from the rolling-window experiments are considered. Values larger than 1 (the red dashed line) indicate that m1 provides better results than competing models, including observable factors. 

of clusters in the dataset, as it is based on a hierarchical procedure. Moreover, we estimate the number of global and clustered factors within the algorithm, so the user does not need to specify these quantities too. 

Considering the full sample of quarterly data on house prices in the period 1975–2023, we identify four clusters of US states characterized by their own clustered factor structure, given the presence of a single latent factor affecting the whole set of US states. Moreover, we show the results obtained using a Panel VAR approach for both in-sample and out-of-sample predictions. Still, we also study how the results change if separate models for each US state are estimated.<sup>5</sup> The conclusions we get for the relevance of cluster-specific factors are the same. Indeed, we find that the inclusion of cluster factors, estimated with the computational procedure discussed in Section 3, allows for more accurate forecasting of house price growth rates, even if state-specific univariate models are considered rather than the Panel VAR. 

Several future research directions can be highlighted. First, the spatial structure considered in this paper could be extended to include an alternative distance across variables (Elhorst, 2013). Within this framework, a different definition of the distance (14) should also be considered. For instance, the geographical distance (14) can be replaced with a distance between multivariate time 

series ( _e.g._ see, D’Urso, 2000). Future research may investigate if cluster-specific factors estimated using distances based on socio-economic variables have a larger predictive power than the geographical distance. Second, the proposed approach is effective if global factors dominate over cluster-specific factors, typically when there are a few large clusters among many smaller ones. However, in the opposite case, there is a risk of confounding global and cluster-specific factors, particularly when the variance of the global factors is relatively small compared to that of the cluster factors. Further investigation in this direction is needed, and methods for the principal component approach for factor estimation should be developed to address this issue. Third, the methods discussed in this paper rely on the stationarity assumption. While stationarity is commonly studied in the literature, nonstationary factor models present a promising topic for future research, especially when considering clustering structures. A possible solution to estimate factors in this context is the Generalized PCA (Peña & Yohai, 2016), which is suitable for nonstationary time series. The properties related to factor reconstruction have been studied by Smucler (2019), but further research seems needed in this direction. Finally, we admit that the proposed approach provides a limited understanding of how uncertainty in estimating groups, loadings, and latent factors propagates in the temporal forecasting model. These limitations could potentially be mitigated by using Bayesian spatial dynamic factor models. Gamerman et al. (2022), Ippoliti et al. (2012), Lopes et al. (2008). 

5 Results are available upon request. 

412 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

##### **Table 4** 

##### **Table 3** 

Predictive accuracy tests results: (Clark & West, 2007) (CW) and Diebold and Mariano (2002) (DM) with squared errors. The p-values are shown, and the full model m1 is compared with the models m2 and m3 for each US state. 

Relative accuracy measures for each US state (out-of-sample). Values larger than 1 indicate that the full model, including global and cluster-specific factors, <u>provides</u> more accurate forecasts. 

|States|RMSE||MAE||and m3 <br>|or each US sta<br>|te.|||
|---|---|---|---|---|---|---|---|---|---|
||m2/m1|m3/m1|m2/m1|m3/m1|States|CW test||DM test||
|AL|1.2541|1.2480|1.1773|1.1643||m1 vs m2|m1 vs m3|m1 vs m2|m1 vs m3|
|AR|1.2187|1.2079|1.1693|1.1502|AL|0.03|0.03|0.05|0.05|
|AZ|1.1946|1.2055|1.1879|1.2030|AR|0.04|0.04|0.05|0.05|
|CA|1.2552|1.2592|1.2243|1.2344|AZ|0.02|0.01|0.03|0.03|
|CO|0.9307|0.9352|0.9594|0.9613|CA|0.02|0.02|0.05|0.05|
|CT|1.1318|1.1295|1.1042|1.0925|CO|0.83|0.79|0.96|0.96|
|DC|0.9939|1.0057|1.0067|1.0208|CT|0.02|0.01|0.03|0.03|
|DE|1.1650|1.1424|1.1369|1.1122|DC|0.14|0.12|0.59|0.38|
|FL|1.1248|1.1376|1.0963|1.1206|DE|0.03|0.04|0.04|0.05|
|GA|1.1505|1.1598|1.0893|1.0913|FL|0.05|0.03|0.05|0.05|
|IA|1.2534|1.2460|1.2595|1.2361|GA|0.05|0.03|0.06|0.05|
|ID|0.9661|0.9746|1.0084|1.0184|IA|0.02|0.03|0.05|0.05|
|IL|1.2175|1.2127|1.1954|1.1773|ID|0.70|0.63|0.93|0.89|
|IN|1.1850|1.1873|1.1178|1.1121|IL|0.02|0.02|0.05|0.05|
|KS|1.1460|1.1478|1.0867|1.0819|IN|0.03|0.03|0.06|0.06|
|KY|1.2722|1.2657|1.2029|1.1798|KS|0.03|0.03|0.06|0.06|
|LA|0.8882|0.8883|0.9251|0.9305|KY|0.03|0.03|0.05|0.05|
|MA|1.1471|1.1409|1.1831|1.1694|LA|0.60|0.57|0.98|0.98|
|MD|1.0902|1.0868|1.0740|1.0624|MA|0.03|0.03|0.03|0.03|
|ME|1.1333|1.1338|1.1270|1.1134|MD|0.07|0.06|0.09|0.08|
|MI|1.1639|1.1651|1.1297|1.1235|ME|0.02|0.01|0.03|0.04|
|MN|1.1193|1.1156|1.0917|1.0818|MI|0.03|0.03|0.04|0.03|
|MO|1.1611|1.1555|1.1637|1.1514|MN|0.07|0.07|0.05|0.04|
|MS|1.2851|1.3088|1.1920|1.2249|MO|0.03|0.03|0.04|0.04|
|MT|0.9272|0.9378|0.9650|0.9860|MS|0.04|0.03|0.05|0.05|
|NC|1.1441|1.1498|1.0811|1.0771|MT|0.84|0.78|0.95|0.95|
|ND|0.9340|0.9352|0.9873|1.0124|NC|0.04|0.04|0.05|0.05|
|NE|0.9633|0.9560|0.9787|0.9694|ND|0.58|0.53|0.98|0.97|
|NH|1.1333|1.1303|1.0907|1.0812|NE|0.55|0.56|0.92|0.92|
|NJ|1.1707|1.1687|1.1562|1.1394|NH|0.02|0.02|0.05|0.05|
|NM|0.9503|0.9543|1.0295|1.0524|NJ|0.01|0.01|0.03|0.03|
|NV|1.1929|1.2043|1.1591|1.1773|NM|0.58|0.52|0.94|0.92|
|NY|1.2424|1.2435|1.2401|1.2580|NV|0.02|0.01|0.02|0.02|
|OH|1.1704|1.1676|1.1380|1.1307|NY|0.02|0.01|0.02|0.03|
|OK|0.9305|0.9323|0.9389|0.9394|OH|0.03|0.03|0.04|0.04|
|OR|1.1849|1.1892|1.1740|1.1803|OK|0.65|0.61|0.95|0.94|
|PA|1.1980|1.1950|1.1490|1.1353|OR|0.03|0.02|0.03|0.03|
|RI|1.1218|1.1180|1.1317|1.1257|PA|0.02|0.01|0.03|0.03|
|SC|1.2108|1.2161|1.1854|1.1740|RI|0.02|0.02|0.04|0.04|
|SD|0.9324|0.9337|0.9548|0.9569|SC|0.03|0.02|0.04|0.04|
|TN|1.1687|1.1794|1.1115|1.1261|SD|0.73|0.70|0.95|0.95|
|TX|0.9321|0.9403|0.9439|0.9544|TN|0.03|0.02|0.05|0.04|
|UT|0.9730|0.9808|1.0418|1.0566|TX|0.78|0.72|0.96|0.95|
|VA|1.1170|1.1123|1.0823|1.0646|UT|0.61|0.55|0.86|0.80|
|VT|1.1187|1.1189|1.1190|1.1140|VA|0.04|0.04|0.07|0.07|
|WA|1.1688|1.1753|1.1882|1.1934|VT|0.02|0.01|0.06|0.06|
|WI|1.1908|1.1894|1.1604|1.1467|WA|0.02|0.02|0.03|0.02|
|WV|1.2222|1.1931|1.1563|1.1340|WI|0.03|0.03|0.04|0.04|
|WY|0.9186|0.9155|0.9193|0.9062|WV|0.04|0.05|0.05|0.05|
||||||WY|0.75|0.73|1.00|1.00|



413 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

##### **Table 5** 

##### **Table 6** 

Relative accuracy measures for each US state (out-of-sample). Values larger than 1 indicate that the full model, including global and cluster-specific factors, provides more accurate forecasts. The compared models include observable factors. 

Predictive accuracy tests results: (Clark & West, 2007) (CW) and Diebold and Mariano (2002) (DM) with squared errors. The p-values are shown, and the full model m1 is compared with the models m2 and m3 for each US state. The compared models include observable factors. 

|States|RMSE||MAE||factors.<br>|||||
|---|---|---|---|---|---|---|---|---|---|
||m5/m4|m6/m4|m5/m4|m6/m4|States|CW test||DM test||
|AL|1.2111|1.2188|1.1372|1.1332||m5/m4|m6/m4|m5/m4|m6/m4|
|AR|1.1650|1.1684|1.1064|1.0982|AL|0.05|0.04|0.05|0.05|
|AZ|1.1825|1.1999|1.1886|1.2122|AR|0.07|0.07|0.05|0.05|
|CA|1.2073|1.2206|1.2452|1.2682|AZ|0.01|0.01|0.03|0.03|
|CO|0.9556|0.9661|0.9714|0.9766|CA|0.03|0.02|0.04|0.04|
|CT|1.1311|1.1413|1.0912|1.0792|CO|0.74|0.65|0.94|0.92|
|DC|0.9635|0.9824|0.9455|0.9667|CT|0.02|0.01|0.04|0.04|
|DE|1.1198|1.1110|1.0950|1.0767|DC|0.33|0.24|0.86|0.77|
|FL|1.1094|1.1318|1.0781|1.1113|DE|0.08|0.08|0.06|0.07|
|GA|1.1276|1.1448|1.1014|1.1107|FL|0.05|0.02|0.05|0.04|
|IA|1.1748|1.1885|1.1318|1.1296|GA|0.06|0.04|0.05|0.05|
|ID|0.9851|0.9986|1.0098|1.0232|IA|0.03|0.02|0.07|0.06|
|IL|1.1530|1.1629|1.0950|1.0830|ID|0.54|0.40|0.87|0.55|
|IN|1.1655|1.1798|1.1056|1.1094|IL|0.04|0.03|0.07|0.07|
|KS|1.1134|1.1293|1.1206|1.1245|IN|0.05|0.04|0.07|0.06|
|KY|1.2015|1.2089|1.1217|1.1142|KS|0.03|0.02|0.05|0.04|
|LA|1.0041|1.0166|0.9744|0.9830|KY|0.06|0.05|0.05|0.04|
|MA|1.1250|1.1353|1.1423|1.1381|LA|0.25|0.21|0.44|0.27|
|MD|1.0701|1.0784|1.0348|1.0374|MA|0.03|0.03|0.03|0.03|
|ME|1.1268|1.1420|1.0923|1.0849|MD|0.12|0.10|0.11|0.10|
|MI|1.1249|1.1378|1.1506|1.1536|ME|0.02|0.01|0.05|0.05|
|MN|1.0801|1.0906|1.1261|1.1255|MI|0.03|0.02|0.03|0.03|
|MO|1.1333|1.1406|1.1339|1.1360|MN|0.07|0.06|0.03|0.03|
|MS|1.1820|1.2166|1.1271|1.1659|MO|0.04|0.04|0.04|0.04|
|MT|0.9530|0.9708|0.9577|0.9822|MS|0.07|0.04|0.05|0.06|
|NC|1.1320|1.1484|1.1027|1.1088|MT|0.74|0.61|0.94|0.94|
|ND|1.0058|1.0259|1.0182|1.0466|NC|0.05|0.03|0.05|0.04|
|NE|0.9987|1.0052|0.9852|0.9853|ND|0.24|0.16|0.40|0.25|
|NH|1.1239|1.1338|1.0661|1.0654|NE|0.35|0.33|0.54|0.36|
|NJ|1.1585|1.1712|1.1232|1.1084|NH|0.02|0.02|0.06|0.06|
|NM|1.0373|1.0544|0.9981|1.0296|NJ|0.03|0.02|0.04|0.05|
|NV|1.1671|1.1867|1.1543|1.1763|NM|0.19|0.13|0.08|0.08|
|NY|1.1967|1.2183|1.1977|1.2236|NV|0.01|0.01|0.02|0.02|
|OH|1.1460|1.1559|1.1387|1.1401|NY|0.02|0.01|0.04|0.04|
|OK|0.9875|1.0016|0.9506|0.9644|OH|0.03|0.03|0.04|0.03|
|OR|1.1557|1.1683|1.2066|1.2184|OK|0.36|0.28|0.73|0.46|
|PA|1.1662|1.1819|1.1325|1.1386|OR|0.02|0.02|0.03|0.03|
|RI|1.1081|1.1168|1.1003|1.1041|PA|0.03|0.02|0.04|0.04|
|SC|1.1761|1.1915|1.1432|1.1463|RI|0.02|0.02|0.05|0.05|
|SD|0.9665|0.9829|0.9510|0.9721|SC|0.05|0.03|0.04|0.04|
|TN|1.1509|1.1711|1.1096|1.1327|SD|0.55|0.44|0.94|0.87|
|TX|0.9674|0.9845|0.9731|0.9945|TN|0.04|0.03|0.04|0.04|
|UT|1.0015|1.0155|1.0449|1.0654|TX|0.61|0.48|0.91|0.82|
|VA|1.1028|1.1131|1.0744|1.0644|UT|0.37|0.26|0.45|0.09|
|VT|1.1211|1.1328|1.0956|1.0910|VA|0.06|0.05|0.08|0.08|
|WA|1.1403|1.1534|1.1812|1.1909|VT|0.02|0.02|0.08|0.08|
|WI|1.1789|1.1944|1.2085|1.2053|WA|0.01|0.01|0.02|0.02|
|WV|1.1573|1.1445|1.0621|1.0464|WI|0.02|0.02|0.04|0.04|
|WY|0.9625|0.9705|0.9263|0.9189|WV|0.07|0.08|0.08|0.08|
||||||WY|0.49|0.44|0.99|0.98|



414 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

#### **Algorithm 2** Hierarchical spatio-temporal clustering 

#### **Algorithm 1** Clustered factor model 

Fix the maximum iterations _max.iter_ and a convergence rule _ε_ ; Estimate a suitable initial _R_ ; Estimate _R_ factors<sup>ˆ</sup> **F** 0 with PCE; Take the residuals<sup>ˆ</sup> **E** and provide an initial suitable partition; **for** k=1,...,K **do if** _Nk >_ 1 **then** Estimate the number of within-cluster factors _Rk_ ; Estimate _Rk_ factors<sup>ˆ</sup> **F** _k_ with cluster-wise PCE; **else** No local factor; **end if end for** Store the initial loss: 

_T K Nk_ 2 _ℓ_ 0 = ∑ ∑ ∑ ( _xit_ −<sup>ˆ</sup> _λ_<sup>′</sup> _i_ 0<sup>ˆ</sup><sup>_f_0</sup><sup>_t_−ˆ</sup><sup>_λ_′</sup> _ik_<sup>ˆ</sup><sup>_fkt_</sup> ) (18) _t_ =1 _k_ =1 _i_ =1 **repeat** ˆ Compute the residuals based on cluster-wise factors **U** ; Update _R_ ; Estimate the new _R_ factors<sup>˜</sup> **F** 0 with PCE; Take the newly adjusted residuals<sup>˜</sup> **E** and update the clusters with Algorithm 2; **for** k=1,...,K **do if** _Nk >_ 1 **then** Estimate the number of within-cluster factors _Rk_ ; Estimate _Rk_ factors<sup>˜</sup> **F** _k_ with cluster-wise PCE; **else** No local factor; **end if end for** Store the loss: 







#### **end for** 

Choose _α_<sup>∗</sup> ∈ _U_ (Chavent et al., 2018): 



Given _K_ = _N_ , start with an initial partition with singletons _PN_ ; **for** _K_ = _N_ − 1 _, . . . ,_ 2 **do** 

Aggregate two merged clusters _A_ ∪ _B_ with a cluster _C_ by means of the modified (Lance & Williams, 1967) equation 



#### **end for** 

Stop when _K_ = 1, thus the partition is _P_ 1. 

415 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

#### **CRediT authorship contribution statement** 

**Raffaele Mattera:** Writing – review & editing, Writ– ing original draft, Visualization, Validation, Software, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. **Philip Hans Franses:** Writing – review & editing, Writing – original draft, Visualization, Supervision, Methodology, Investigation, Conceptualization. 

#### **Declaration of competing interest** 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### **Data availability** 

The replication files (data and R codes) can be accessed by the GitHub repository at the following link: https:// github.com/raffmattera/stcfm/. 

#### **Acknowledgments** 

The authors thank the Associate Editor and the two anonymous reviewers for the very helpful comments. 

#### **References** 

Aastveit, K. A., Bjørnland, H. C., & Thorsrud, L. A. (2016). The world is not enough! small open economies and regional dependence. _Scandinavian Journal of Economics_ , _118_ (1), 168–195. 

Ahn, S. C., & Horenstein, A. R. (2013). Eigenvalue ratio test for the number of factors. _Econometrica_ , _81_ (3), 1203–1227. 

Alonso, A. M., Galeano, P., & Peña, D. (2020). A robust procedure to build dynamic factor models with cluster structure. _Journal of Econometrics_ , _216_ (1), 35–52. 

Alonso, A. M., & Peña, D. (2019). Clustering time series by linear dependency. _Statistics and Computing_ , _29_ (4), 655–676. 

Ando, T., & Bai, J. (2017). Clustering huge number of financial time series: A panel data approach with high-dimensional predictors and factor structures. _Journal of the American Statistical Association_ , _112_ (519), 1182–1198. 

Aquaro, M., Bailey, N., & Pesaran, M. H. (2021). Estimation and inference for spatial models with heterogeneous coefficients: an application to US house prices. _Journal of Applied Econometrics_ , _36_ (1), 18–44. 

Bai, J. (2003). Inferential theory for factor models of large dimensions. _Econometrica_ , _71_ (1), 135–171. 

Bai, Y., Carriero, A., Clark, T. E., & Marcellino, M. (2022). Macroeconomic forecasting in a multi-country context. _Journal of Applied Econometrics_ , _37_ (6), 1230–1255. 

Bai, J., & Ng, S. (2002). Determining the number of factors in approximate factor models. _Econometrica_ , _70_ (1), 191–221. 

Bailey, N., Holly, S., & Pesaran, M. H. (2016). A two-stage approach to spatio-temporal analysis with strong and weak cross-sectional dependence. _Journal of Applied Econometrics_ , _31_ (1), 249–280. 

Beck, G. W., Hubrich, K., & Marcellino, M. (2009). Regional inflation dynamics within and across euro area countries and a comparison with the united states. _Economic Policy_ , _24_ (57), 142–184. 

Blatt, D., Chaudhuri, K., & Manner, H. (2023). A changepoint analysis of UK house price spillovers. _Regional Studies_ , _57_ (7), 1223–1238. 

Brady, R. R. (2014). The spatial diffusion of regional housing prices across US states. _Regional Science and Urban Economics_ , _46_ , 150–166. Breitung, J., & Eickmeier, S. (2014). Analyzing business and financial cycles using multi-level factor models. Deutsche Bundesbank Discussion Paper. 

Brillinger, D. (2001). Time series: Data analysis and theory. In _Classics in applied mathematics_ . USA, Philadelphia: Society for Industrial and Applied Mathematics. 

Bucci, A., Ippoliti, L., Valentini, P., et al. (2023). Analysing spatiotemporal patterns of covid-19 confirmed deaths at the nuts-2 regional level. _Regional Statistics_ , _13_ (2), 214–239. 

Chavent, M., Kuentz-Simonet, V., Labenne, A., & Saracco, J. (2018). Clustgeo: an r package for hierarchical clustering with spatial constraints. _Computational Statistics_ , _33_ (4), 1799–1822. 

Ciccarelli, C., & Elhorst, J. P. (2018). A dynamic spatial econometric diffusion model with common factors: The rise and spread of cigarette consumption in Italy. _Regional Science and Urban Economics_ , _72_ , 131–142. 

Cipollini, A., & Parla, F. (2020). Housing market shocks in Italy: A gvar approach. _Journal of Housing Economics_ , _50_ , Article 101707. 

Clark, T. E., & West, K. D. (2006). Using out-of-sample mean squared prediction errors to test the martingale difference hypothesis. _Journal of Econometrics_ , _135_ (1–2), 155–186. 

Clark, T. E., & West, K. D. (2007). Approximately normal tests for equal predictive accuracy in nested models. _Journal of Econometrics_ , _138_ (1), 291–311. 

Das, S., Gupta, R., & Kabundi, A. (2011). Forecasting regional house price inflation: a comparison between dynamic factor models and vector autoregressive models. _Journal of Forecasting_ , _30_ (2), 288–302. 

Dées, S., & Güntner, J. (2017). Forecasting inflation across euro area countries and sectors: A panel var approach. _Journal of Forecasting_ , _36_ (4), 431–453. 

Diebold, F. X., & Mariano, R. S. (2002). Comparing predictive accuracy. _Journal of Business & Economic Statistics_ , _20_ (1), 134–144. 

D’Urso, P. (2000). Dissimilarity measures for time trajectories. _Journal of the Italian Statistical Society_ , _9_ , 53–83. 

Eickmeier, S., Gambacorta, L., & Hofmann, B. (2014). Understanding global liquidity. _European Economic Review_ , _68_ , 1–18. 

Elhorst, J. P. (2013). _Spatial econometrics: from cross-sectional data to spatial panels_ . Germany, Heidelberg: Springer. 

Emiris, M. (2016). A dynamic factor model for forecasting house prices 

in belgium. National Bank of Belgium Working Paper (313). 

Feldkircher, M., Huber, F., & Pfarrhofer, M. (2020). Factor augmented vector autoregressions, panel vars, and global vars. (pp. 65–93). Macroeconomic Forecasting in the Era of Big Data: Theory and Practice. 

Forni, M., Hallin, M., Lippi, M., & Reichlin, L. (2000). The generalized dynamic-factor model: Identification and estimation. _The Review of Economics and Statistics_ , _82_ (4), 540–554. 

Forni, M., Hallin, M., Lippi, M., & Reichlin, L. (2005). The generalized dynamic factor model: one-sided estimation and forecasting. _Journal of the American Statistical Association_ , _100_ (471), 830–840. 

Fouedjio, F. (2016). A hierarchical clustering method for multivariate geostatistical data. _Spatial Statistics_ , _18_ , 333–351. 

Franses, P. H., & Wiemann, T. (2020). Intertemporal similarity of economic time series: An application of dynamic time warping. _Computational Economics_ , _56_ (1), 59–75. 

Gamerman, D., Ippoliti, L., & Valentini, P. (2022). A dynamic structural equation approach to estimate the short-term effects of air pollution on human health. _Journal of the Royal Statistical Society. Series C. Applied Statistics_ , _71_ (3), 739–769. 

Han, C., Phillips, P. C., & Sul, D. (2017). Lag length selection in panel autoregression. _Econometric Reviews_ , _36_ (1–3), 225–240. 

Holly, S., Pesaran, M. H., & Yamagata, T. (2010). A spatio-temporal model of house prices in the USA. _Journal of Econometrics_ , _158_ (1), 160–173. 

Hubert, L., & Arabie, P. (1985). Comparing partitions. _Journal of Classification_ , _2_ , 193–218. 

Ippoliti, L., Valentini, P., & Gamerman, D. (2012). Space–time modelling of coupled spatiotemporal environmental variables. _Journal of the Royal Statistical Society. Series C. Applied Statistics_ , _61_ (2), 175–200. 

Kim, Y. S., & Rous, J. J. (2012). House price convergence: Evidence from us state and metropolitan area panels. _Journal of Housing Economics_ , _21_ (2), 169–186. 

Kuethe, T. H., & Pede, V. O. (2011). Regional housing price cycles: A spatio-temporal analysis using us state-level data. _Regional Studies_ , _45_ (5), 563–574. 

416 

_R. Mattera and P.H. Franses_ 

_International Journal of Forecasting 41 (2025) 398–417_ 

Lopes, H. F., Salazar, E., & Gamerman, D. (2008). Spatial dynamic factor analysis. _Bayesian Analysis_ , _3_ (4), 759–792. 

- Maharaj, E. A., D’Urso, P., & Caiado, J. (2019). _Time series clustering and classification_ . USA, Boca Raton: Chapman and Hall/CRC. 

- Mattera, R. (2022). A weighted approach for spatio-temporal clustering of covid-19 spread in Italy. _Spatial and Spatio-temporal Epidemiology_ , _41_ , Article 100500. 

- Mattera, R., & Franses, P. H. (2023). Are african business cycles synchronized? evidence from spatio-temporal modeling. _Economic Modelling_ , _128_ , Article 106485. 

- Moench, E., & Ng, S. (2011). A factor analysis of housing market dynamics in the US and the regions. _The Econometrics Journal_ , _14_ , C1–C24. 

Mumtaz, H., & Surico, P. (2009). The transmission of international shocks: a factor-augmented var approach. _Journal of Money, Credit and Banking_ , _41_ , 71–100. 

- Otto, P., & Schmid, W. (2018). Spatiotemporal analysis of german real-estate prices. _The Annals of Regional Science_ , _60_ (1), 41–72. 

Peña, D., & Yohai, V. J. (2016). Generalized dynamic principal components. _Journal of the American Statistical Association_ , _111_ (515), 1121–1131. 

- Piccolo, D. (1990). A distance measure for classifying arima models. _Journal of Time Series Analysis_ , _11_ (2), 153–164. 

Rapach, D. E., & Strauss, J. K. (2009). Differences in housing price forecastability across us states. _International Journal of Forecasting_ , _25_ (2), 351–372. 

Sigmund, M., & Ferstl, R. (2021). Panel vector autoregression in r with the package panelvar. _The Quarterly Review of Economics and Finance_ , _80_ , 693–720. 

- Smucler, E. (2019). Consistency of generalized dynamic principal components in dynamic factor models. _Statistics & Probability Letters_ , _154_ , Article 108536. 

Stock, J. H., & Watson, M. W. (2002). Forecasting using principal components from a large number of predictors. _Journal of the American Statistical Association_ , _97_ (460), 1167–1179. 

Valentini, P., Ippoliti, L., & Fontanella, L. (2013). Modeling us housing prices by spatial dynamic structural equation models. _The Annals of Applied Statistics_ , _7_ (2), 763–798. 

- Van Dijk, B., Franses, P. H., Paap, R., & Van Dijk, D. (2011). Modelling regional house prices. _Applied Economics_ , _43_ (17), 2097–2110. 

Wang, P. (2010). _Large dimensional factor models with a multi-level factor structure: identification, estimation and inference_ : _Working paper_ , Department of Economics, HKUST. 

Yang, C. F. (2021). Common factors and spatial dependence: An application to US house prices. _Econometric Reviews_ , _40_ (1), 14–50. 

#### **Further reading** 

Lance, G. N., & Williams, W. T. (1967). A general theory of classificatory sorting strategies: 1. hierarchical systems. _The Computer Journal_ , _9_ (4), 373–380. 

417 

