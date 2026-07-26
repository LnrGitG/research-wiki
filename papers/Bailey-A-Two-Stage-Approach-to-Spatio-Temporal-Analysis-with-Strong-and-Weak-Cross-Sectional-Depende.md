---
title: A Two Stage Approach to Spatio-Temporal Analysis with Strong and Weak Cross-Sectional Dependence<sup>∗</sup>
type: paper
source_pdf: raw/papers/Bailey_A Two Stage Approach to Spatio Temporal Analysis with Strong and Weak Cross-Sectional Dependence_2014.pdf
converted: 2026-07-26
---

# A Two Stage Approach to Spatio-Temporal Analysis with Strong and Weak Cross-Sectional Dependence<sup>∗</sup> 

Natalia Bailey Sean Holly Queen Mary, University of London University of Cambridge M. Hashem Pesaran 

University of Southern California and Trinity College, Cambridge Revised July 2014 

##### Abstract 

An understanding of the spatial dimension of economic and social activity requires methods that can separate out the relationship between spatial units that is due to the effect of common factors from that which is purely spatial even in an abstract sense. The same applies to the empirical analysis of networks in general. We use cross unit averages to extract common factors (viewed as a source of strong cross-sectional dependence) and compare the results with the principal components approach widely used in the literature. We then apply multiple testing procedures to the de-factored observations in order to determine significant bilateral correlations (signifying connections) between spatial units and compare this to an approach that just uses distance to determine units that are neighbours. We apply these methods to real house price changes at the level of Metropolitan Statistical Areas in the USA, and estimate a heterogeneous spatio-temporal model for the de-factored real house price changes and obtain significant evidence of spatial connections, both positive and negative. 

Keywords: Spatial and factor dependence, spatio-temporal models, positive and negative connections, house price changes. JEL Classification: C21, C23 

> ∗The authors would like to thank Alex Chudik, George Kapetanios, Ron Smith, Vanessa Smith, Jushan Bai (guest editor), two anonymous referees and participants at the following conferences for valuable comments and suggestions: 2012 SEA conference, Salvador, Brazil, 2013 conference on CrossSectional Dependence in Panel Data Models, Cambridge, UK, 2013 Econometrics of Social Interaction Symposium, York, UK, 2013 SEA conference, Washington DC, US, 1st IAAE Annual Conference, June 2014, Queen Mary University of London, UK, and 20th International Panel Data Conference, July 2014, Tokyo, Japan. The authors also wish to acknowledge financial support under ESRC Grant ES/I031626/1. 

## 1 Introduction 

The nature and degree of spatial dependence in economic, geographical, epidemiological and ecological systems has long been the focus of intensive study. Geographers regard the fundamental question in economic geography to be what explains the uneven pattern of economic activity in space. Indeed the New Economic Geography starting with Krugman (1991) addresses exactly this question. But where we have a data rich environment with observations on many spatial units over many time periods there may be obstacles to understanding these uneven patterns in spatial data because of complex dependencies between spatial units that reflect both local (clustering) and common factors. Recent developments in spatial econometrics have generated a growing literature on methods for modelling and measuring spatial or cross-sectional dependence in data sets with a panel structure where there are observations over time (T ) and over space (N ). This in turn has identified a number of central research questions. What is the source of dependencies in space? To what extent are the observed dependencies between different spatial units due to common factors - for example, aggregate shocks - that affect different units rather than being the result of local interactions that generate spatial spill-over effects? Is the implementation of estimation procedures of panels that implicitly assume spatially correlated units justifiable when the degree of their cross dependence has not been established? Do existing methods of identifying neighbouring relationships fully reflect the spatial structure of the underlying data studied? 

To answer these and other related questions two basic approaches have been developed in the literature, namely spatial and common factor models. Spatial processes were pioneered by Whittle (1954) and developed further in econometrics by Anselin (1988), Kelejian and Prucha (1999), and Lee (2002), amongst others. Factor models were introduced by Hotelling (1933) and first applied in economics by Stone (1947), and have been developed further to deal with data sets where the cross section and time series dimensions are both relatively large, by Forni and Lippi (2001), Forni, Hallin, Lippi, and Reichlin (2000), and Stock and Watson (1998). These methods have been applied extensively in finance and macroeconomics, notably by Chamberlain and Rothschild (1983), Connor and Korajczyk (1993), Forni and Reichlin (1998), Stock and Watson (2002a,b), and Kapetanios and Pesaran (2007). 

Factors can be represented by cross-sectional averages at regional and/or national levels - Pesaran (2006), or can be estimated by Principal Components (PCs). The number of principal components can be determined, for example, using the various information criteria proposed by Bai and Ng (2002), amongst others. Estimation of panels with spatially correlated errors include the use of parametric methods based on maximum likelihood - Lee (2004), Yu, de Jong and Lee (2008), Lee and Yu (2010), or the GMM approach proposed by Kelejian and Prucha (1999, 2010), Kapoor, Kelejian and Prucha (2007), and Lin and Lee (2010). Furthermore, non-parametric methods using spatial HAC estimators have been applied by Conley (1999), Kelejian and Prucha (2007), and Bester, Conley and Hansen (2011). Chudik and Pesaran (2014) provide a review of recent literature on estimation and inference in large panel data models with cross-sectional dependence. 

The factor and spatial econometric approaches tend to complement one another, with the factor approach more suited to modelling strong cross-sectional dependence, whilst the spatial approach generally requires the spatial dependence to be weak. See, for ex- 

1 

ample, Chudik, Pesaran and Tosetti (2011). This presents a challenge as most panel data sets are subject to a combination of strong and weak cross dependencies, and a methodology that is capable of identifying and dealing with both forms of cross dependence is needed. This paper proposes a two-stage estimation and inference strategy, whereby in the first step tests of cross-sectional dependence are applied to ascertain if the crosssectional dependence is weak. If the null of weak cross-sectional dependence is rejected, the implied strong cross-sectional dependence is modelled by means of a factor model. Residuals from such factor models, referred to as de-factored observations, are then used to estimate possible connections amongst pairs of cross section units, and ultimately to model the remaining weak cross dependencies, making use of extant techniques from spatial econometrics or generalisations thereof. 

In our application of spatial econometric techniques, in addition to using standard spatial weights matrices based on contiguity and geodesic distance, we also consider the use of pair-wise correlations of the de-factored observations to identify if a given pair of cross section units is connected by testing whether the associated pair-wise correlation is non-zero. To avoid the multiple testing problem that such an approach entails we employ Bonferroni (1935) and Holm (1979) procedures discussed in Bailey, Pesaran and Smith (2014). Finally, following Aquaro, Bailey and Pesaran (2014), we consider a generalisation of the traditional spatial autoregressive model for large panel data sets that allows the spatial parameters to vary over the cross section units. 

The paper also provides a detailed application of the proposed two-step methodology to the analysis of real house price changes across different Metropolitan Statistical Areas (MSAs) in the US. We consider de-factoring of the observations using Principal Components applied to the full data set as well as by regions, and compare the results to de-factoring using simple national and regional cross-sectional averages. The de-factored observations are then used to estimate the patterns of connections across MSAs by the Holm multiple testing procedure applied to the N (N − 1)/2 pair-wise correlations, distinguishing between positively related N × N connection (weights) matrix, W<sup>ˆ+</sup> , and the negatively related connection matrix, W<sup>ˆ−</sup> . These positive and negative connection matrices are then compared to geodesic based spatial matrices, Wd, (d being the selected distance measure between different MSAs) and their closeness examined by means of contingency tables. A heterogeneous spatio-temporal model of de-factored house price changes is then estimated by the quasi maximum likelihood (QML). The results confirm important dynamics in the de-factored house price changes as well as statistically significant positive and negative spill-over effects across the MSAs, with the positive effects being more prevalent. 

The rest of the paper is organised as follows: Section 2 motivates and describes the first stage of the proposed two-step spatio-temporal modelling strategy. Section 3 focuses on the second stage of the proposed approach and suggests first a correlation based method for approximating network connections using de-factored observations from the first stage, and second introduces a heterogeneous version of the traditional spatial econometrics model. Section 4 presents the empirical application to the US real house price changes, with some concluding remarks provided in Section 5. Data specifications and sources are relegated to the Appendices. 

Notation: The largest and the smallest eigenvalues of the N × N matrix A = (aij) , are denoted by λmax (A) and λmin (A) , respectively, ∥A∥ = λ<sup>1</sup> max<sup>/2(A′A) is the spectral (or</sup> N operator) norm of A, ∥A∥1 = max1≤j≤N i=1<sup>|aij|</sup> is its maximum absolute column �� � 

2 

sum norm, and ∥A∥∞ = max1≤i≤N ��Nj=1<sup>|aij|</sup> � is its maximum absolute row sum norm. K is used to represent a finite generic positive constant. 

## 2 Cross-sectional dependence (CSD) in panels 

Cross-sectional dependence may be due to common effects coming from aggregate factors which are pervasive by nature, and/or can result from spatial interactions between units which are localised in character. In order to build a strategy for distinguishing between the two types of cross dependence it is useful first to analyse their properties with the help of two established and widely used econometric models: spatial and factor models. 

### 2.1 Spatial dependence - a form of weak CSD 

The standard spatial econometric model with a homogeneous spatial autoregressive coefficient, ψ, can be written as 



where x<sup>∗</sup> it<sup>=w</sup> i<sup>′x</sup> ◦<sup>t,x</sup> ◦<sup>t=(x1t, x2t, ..., xNt)′,wi=(wi1, wi2, ..., wiN)′istheN× 1vector</sup> of fixed weights attached to the neighbours of the i<sup>th</sup> unit, and uit is the idiosyncratic component of xit which is assumed to be serially and cross-sectionally independently distributed, with zero means and variances var(uit) = σ<sup>2</sup> ui<sup>, 0<σ2</sup> ui<sup><K<∞.Writing</sup> the above N equations in matrix notation we have 



where u◦t = (u1t, u2t, ..., uNt)<sup>′</sup> , W = (w1, w2, ..., wN )<sup>′</sup> , and var(u◦t) = Σu = diag �σ<sup>2</sup> ui<sup>,i = 1, 2, ..., N</sup> �. This model is commonly known as a first-order spatial autoregression, or SAR(1) for short. 

The N × N weight matrix, W, is typically sparse, with its non-zero elements set a priori, using physical or economic distance. In practice W is row-standardised so that Wτ = τ , where τ is a N × 1 vector of ones. A review of spatial econometrics literature is provided by Anselin (2001), and more recently by LeSage and Pace (2010). Many different choices of W are considered in the literature. Physical and economic distances have been used (Conley and Dupor (2003), Conley and Topa (2003), Pesaran, Schuermann and Weiner (2004)). In some instances trade flows might be relevant, whilst in the case of inter-industry dependencies input-output matrices might provide the appropriate ‘spatial’ metric - Holly and Petrella (2012). Alternatively, there may be dependencies between geographical areas that reflect cultural similarity, and migration or commuting relationships.<sup>1</sup> Using one of these distance metrics the W matrix is then constructed a priori and equation (2) is estimated directly.<sup>2</sup> 

Irrespective of the distance measure used, spatial dependence relates to spill-over effects that are not pervasive in nature. In other words it conforms to the notion of crosssectional weak dependence (CWD) as defined in Chudik, Pesaran and Tosetti (2011). 

> 1Interactions in social networks can also be ‘spatial’ in an abstract sense. For example Bhattacharjee and Holly (2013) explore interactions among members of a committee using a spatial analogy. 

> 2The regional science literature has long been aware of the potential problems with the prior specification of the W matrix. For recent contributions see Corrado and Fingleton (2012). 

3 

To see why, consider the SAR(1) model defined in (2). Assuming that (IN − ψW) is invertible, we have 



where G = (IN − ψW)<sup>−1</sup> . It is now easily seen that V ar (x◦t) = Σ = GΣuG<sup>′</sup> , and we have 



Suppose that |ψ| ∥W∥∞ < 1, then 



Similarly, ∥G∥1 < K < ∞, if it is further assumed that |ψ| ∥W∥1 < 1. Therefore, G has bounded row and column sum matrix norms if |ψ| < min (1/ ∥W∥1 , 1/ ∥W∥∞), and under the same condition, using (4), it follows that Σ will also be row (column) bounded. 

Denoting the correlation matrix of x◦t by R = (ρij) and assuming that var(xit) = σ<sup>2</sup> xi<sup>>0isboundedawayfromzero,thenR=D−1/2ΣD−1/2,whereD=diag(σ2</sup> xi<sup>,</sup> i = 1, 2, ..., N ). Hence 



Also, λmax(R) ≤∥R∥1 < K. Therefore, λmax(R) controls the degree of cross-sectional dependence and is bounded in the case of SAR(1) models so long as |ψ| < min (1/ ∥W∥1 , 1/ ∥W∥∞), a condition generally assumed in the spatial econometrics literature. This result readily extends to higher order SAR models. 

### 2.2 The factor model - a form of strong CSD 

At other end of the spectrum we consider the factor model as a form of strong crosssectional dependence. To this end we draw from the analysis in Pesaran (2014) which tests for weak cross-sectional dependence. Suppose that x◦t is generated according to the following m-factor model 



where f t = (f1t, f2t, ..., fmt)<sup>′</sup> is the m × 1 vector of unobserved common factors (m being fixed) with E(f t) = 0, Σff = Cov(f t) = Im, and Γ = (γ1, γ2, ..., γN )<sup>′</sup> is the N ×m matrix of the factor loadings γi = (γi1, γi2, ..., γim)<sup>′</sup> , for i = 1, 2, ..., N, ε◦t = (ε1t, ε2t, ..., εNt)<sup>′</sup> are idiosyncratic errors that are cross-sectionally and serially independent, with zero means and constant variances, ω<sup>2</sup> i<sup>,0<ω2</sup> i<sup><K,i=1, 2, ..., N.Asbefore,thedegreeofcross-</sup> sectional dependence of x◦t is governed by the largest eigenvalue of the correlation matrix of x◦t, R = (ρij). It is easily seen that under the above factor model 



4 

where δiℓ = γiℓ/�ω<sup>2</sup> i<sup>+ γ′</sup> i<sup>γ</sup> i<sup><u>,</u>and</sup><sup><u>ρ</u></sup> ii<sup>=1.Also,sinceω2</sup> i<sup>isafixednon-zeroconstant,</sup> then the scaling of γiℓ by ~~�~~ ω<sup>2</sup> i<sup>+ γ′</sup> i<sup>γ</sup> i<sup>ensuresthatγ</sup> iℓ<sup>andδiℓareofthesameorderof</sup> magnitude. For example, δiℓ = 0 if γiℓ = 0, and δiℓ = 0 if γiℓ = 0, and vice versa. 

Consider now the effects of the ℓ<sup>th</sup> factor, fℓt, on the i<sup>th</sup> unit, xit, as measured by δiℓ, and suppose that these factor loadings take non-zero values for Mℓ out of the N cross section units. Then, following Bailey, Kapetanios and Pesaran (2014 - BKP), the degree of cross-sectional dependence due to the ℓ<sup>th</sup> factor can be measured by αℓ = ln(Mℓ)/ ln(N ), and the overall degree of cross-sectional dependence by α = maxℓ(αℓ). They define α as the exponent of N that gives the maximum number of xit units, M = maxℓ(Mℓ), that are pair-wise correlated. The remaining N − M units are either uncorrelated or their correlations tend to zero at a sufficiently fast rate. BKP refer to α as the exponent of cross-sectional dependence and takes any value in the range 0 to 1, with 1 indicating the highest degree of cross-sectional dependence. 

The exponent of cross-sectional dependence of xit can be equivalently defined in terms of the scaled factor loadings, δi. Without loss of generality, suppose that only the first Mℓ elements of δiℓ over i are non-zero, and note that<sup>3</sup> 



where µℓ = Mℓ<sup>−1</sup> �Mi=1ℓ<sup>δiℓ= 0,andα = maxℓ(αℓ).</sup> 

### 2.3 Average pair-wise correlations as a measure of cross-sectional dependence 

As a statistical measure of cross-sectional dependence, λmax (R), can be difficult to analyse, especially for temporally and cross-sectionally dependent data sets. Instead, we can summarise the degree of cross-sectional dependence among the N units conveniently by their average pair-wise correlations, defined by 



which can be written equivalently in terms of the correlation matrix, R, as 



where τ is an N ×1 vector of ones. In general, noting that (τ<sup>′</sup> τ ) λmin(R) ≤ τ<sup>′</sup> Rτ ≤ (τ<sup>′</sup> τ ) λmax(R), we have 



> 3The main results in Pesaran (2014) and Bailey, Kapetanios and Pesaran (2014) remain valid even if �Ni=Mℓ+1<sup>δiℓ= O(1).Butforexpositionalsimplicityweassumethat�N</sup> i=Mℓ+1<sup>δiℓ= 0.</sup> 

5 

and 



Therefore, in the case of weakly cross correlated processes, such as the spatial autoregressive models, where λmax(R) is bounded in N , ρ¯N → 0, as N →∞. It is also clear that standard spatial econometric models cannot deal with cases where ρ¯N differs from zero for sufficiently large N .<sup>4</sup> 

In the case of the factor model given by (6), we have, 



¯ ′ ¯ where<sup>¯</sup> δN = N<sup>−1 �N</sup> i=1<sup>δi=</sup> �δ1N , ¯δ2N , ..., ¯δmN � , and δℓN is given by (8). Further, noting that m is fixed and using (8) we have 



where as before, α = maxℓ(αℓ). Similarly 



Hence ρ¯N = O(N<sup>2α−2</sup> ). 

The values of α in the range [0, 1/2) correspond to different degrees of weak crosssectional dependence. For these values of α, ρ¯N tends to zero very fast, at orders that range from N<sup>−2</sup> to N<sup>−1</sup> . The values of α in the range [1/2, 3/4) represent moderate degrees of cross-sectional dependence. In this case, ρ¯N tends to zero at rates ranging from N<sup>−1</sup> to N<sup>−1/2</sup> . ρ¯N converges to a non-zero value only if α = 1, although for values of α in the range of [3/4,1), cross-sectional dependence is still quite strong with ¯ρN tending to zero rather slowly. 

### 2.4 Degrees of cross-sectional dependence and the two-step approach 

Since in many applications cross-sectional dependence could be due to common factors as well as spatial or network dependence, it is important that both sources of cross-sectional dependence are taken into account. Mistaking factor dependence, as in (6), for spatial dependence can lead to spurious inference as to the pervasiveness and the degree of the cross-sectional dependence. In consequence, identifying the strength of such dependence is of special significance. 

> 4In cases where the degree of cross-sectional dependence is relatively high, one would expect λmax(R) associated with the correlation matrix of the spatial model to be relatively large when W is rowstandardized and ψ is close to unity. Using simulations we can confirm that in such cases λmax(R) rises with N but at a slower rate, such that αN = ln (λmax(R)) / ln(N ) tends to a value which is below 1/2. Also, as is expected, for each N , αN rises with |ψ| - see Bailey, Kapetanios and Pesaran (2014) for details regarding the specification of αN . 

6 

Suppose observations x◦t = (x1t, x2t, ..., xNt)<sup>′</sup> , t = 1, 2, ..., T, are available and the aim is to model the cross dependence between xit and xjt across i, j = 1, 2, ..., N, with N and T relatively large. A first step requires one to evaluate the strength of the cross-sectional correlation in x◦t. The application of spatial methods should only be considered if the cross-sectional exponent of the observations, α, is sufficiently small, and particularly not close to unity. Regarding temporal dependence, this can be modelled through common factors or unit-specific dynamics using autoregressive distributed lag models or GVAR specifications (Pesaran, Schuermann and Weiner (2004), and Dees, di Mauro, Pesaran and Smith (2007)). 

A two-step procedure suggests itself: 

- Step 1: Apply the cross-sectional dependence (CD) test developed in Pesaran (2004, 2014) to x◦t, t = 1, 2, ..., T . 

   - (a) Only proceed to spatial modelling if the null of weak cross dependence is not rejected. 

   - (b) If the null of weak dependence is rejected, model the (semi-) strong dependence implied by the test outcome using factor models and check that the residuals ˆ 

   - from (6), denoted by ε◦t = (ˆε1t, ..., ˆεNt)<sup>′</sup> and referred to as de-factored observations, are weakly cross-correlated (by applying the CD test now to ˆε◦t, t = 1, 2, ..., T ). 

- Step 2: Supposing that the analysis in the first step yields de-factored observations that are reasonably weakly cross-correlated, proceed to spatial or network modelling of the de-factored observations. The residuals ˆε◦t can also be used to estimate the strength of connections over the cross section units. 

In order to test for weak dependence, denote the sample estimates of the pair-wise correlations of the (i, j) units of x◦t, t = 1, 2, ..., T , by 



where x¯i = N<sup>−1 �N</sup> i=1<sup>xit.TheCDstatisticisthendefinedby</sup> 



where 



Pesaran (2014) shows that CD →d N (0, 1), under the null hypothesis that the crosssectional exponent of x◦t, t = 1, 2, ..., T, is α < (2 − ϵ)/4 as N →∞, such that T = κN<sup>ϵ</sup> , for some 0 ≤ ϵ ≤ 1, and a finite κ > 0. 

If the null hypothesis of weak dependence is rejected in step 1 of the above procedure, then according to BKP the exponent of cross-sectional dependence, α, can be estimated. 

7 

There are different ways of estimating this exponent if 1/2 < α ≤ 1. We refer to Bailey, Kapetanios and Pesaran (2014) for details. 

For de-factoring of the observations common factors can be estimated either by the Principal Components Analysis (PCA), or by cross-sectional averages. Both approaches can be applied to the data set as a whole, or to sub-groups of the data set separately. The grouping can in turn be based on some a priori criteria, or could be estimated using discriminant or some other suitable statistical analysis. In the empirical application we use the regional classifications of the MSAs in the USA, but it would also be interesting to apply the group membership procedure recently developed for factor models by Bai and Ando (2014). 

The success of de-factoring could be checked by the application of Pesaran’s CD test to the de-factored observations. The spatial modelling stage can then begin once we are satisfied that the de-factored observations do not exhibit strong forms of cross-sectional dependence. In the case where the spatial weight matrix is given a priori, it might be possible to combine the two steps in one meta approach that simultaneously deals with factor and spatial dependence. It is not clear that such a meta approach would also be possible if the spatial weights, wij, are to be endogenously determined. 

## 3 Spatial econometrics models revisited 

The de-factored observations can now be modelled using spatial econometric techniques that are available in the literature. However, in our application we consider two extensions of this literature, namely endogenising the choice of the spatial weights matrix, W, and allowing the spatial parameter, ψ, in the SAR model, (1), to be heterogeneous across i. 

### 3.1 Correlation-based specification of spatial weights matrices 

Typically W is constructed using geodesic, demographic or economic information brought in exogenously, and not contained in the data set under consideration, here {xit, i = 1, 2, ..., N ; t = 1, 2, ..., T }. Geographical contiguity can be used as in Holly, Pesaran and Yamagata (2011a,b). In economic applications, economic measures, such as commuting times, trade and migratory flows across geographical areas have been used. For example, in GVAR modelling trade weights are used in the construction of link matrices that relate individual economies to their trading partners in the global economy - Pesaran, Schuermann and Weiner (2004). Such measures are often preferable over geodesic measures - since they are closer to the decisions that underlie the observations, xit, and they allow also for possible time variations in the weighting matrix which of course is not possible if we use only physical distance measures in the construction of W. 

In practice, however, suitable economic distance might not be available in many applications,and it is desirable to see if W can be constructed without recourse to such exogenous information. In applications where the time dimension is reasonably large (around 60-80), it is possible to identify the non-zero elements of W with those elements of ρˆij, as expressed in (11), that are different from zero at a suitable significance level. There is a related literature that addresses the issue of identification of neighbours by non-zero elements of an assumed sparse covariance matrix or its inverse. The inverse covariance matrix is used in Markov networks defined as a graphical model that represents variables as nodes and ‘conditional’ dependencies (partial correlations) between variables 

8 

as (undirected) edges. Estimation then amounts to setting elements of the inverse covariance matrix to zero - Dempster (1972).<sup>5</sup> A number of estimation approaches have followed, using lasso type penalties applied to the estimation of the inverse covariance matrix directly. The main problem with this approach is that once de-factoring has taken place the interpretation of the resulting inverse covariance matrix is ambiguous. Furthermore, finding a good estimate of the inverse covariance matrix especially when N > T can be challenging. The second approach uses the so-called covariance graph at its focus which is the corresponding graphical model for ‘marginal’ dependencies (marginal correlations). Methods of estimating covariance matrices with zero elements include contributions by Chaudhuri, Drton and Richardson (2007), Khare and Rajaratnam (2011), Butte, Tamayo, Slonim, Golub and Kohane (2000), and Rothman, Bickel, Levina and Zhu (2008, 2010).<sup>6</sup> 

In this paper we follow the second approach and employ the multiple testing procedure recently developed in Bailey, Pesaran and Smith (2014, BPS) which tests the statistical significance of the pair-wise correlations of the de-factored observations, ρij. As shown below, it is simple to implement, is invariant to the ordering of the underlying units, and consistently estimates the true positive rate and the false positive rate of zeros and ones of the underlying W matrix. 

The multiple testing problem arises when we are faced with a number of (possibly) dependent tests and our aim is to control for the size of the overall test. Suppose we are interested in a family of null hypotheses, H01, H02, ..., H0n and we are provided with corresponding test statistics, Z1T , Z2T , ...., ZnT , with separate rejection rules given by (using a two sided alternative) 



where CViT is some suitably chosen critical value of the test, and piT is the observed p value for H0i. Consider now the family-wise error rate (FWER) defined by 



and suppose that we wish to control FWERT to lie below a pre-determined value, p. Bonferroni (1935, 1936) provides a general solution, which holds for all possible degrees of dependencies across the separate tests. By Boole’s inequality we have 



Hence, to achieve FWERT ≤ p, it is sufficient to set piT ≤ p/n. However, Bonferroni’s procedure can be quite conservative, particularly when the tests are highly correlated. This means that the procedure does not reject as often as it should and therefore lacks power. A step-down procedure is proposed by Holm (1979) which is more powerful than 

> 5A recent economic application of this approach is provided by Barigozzi and Brownlees (2013). 

> 6For further contributions in this area see Meinshausen and Buhlmann (2006), Peng, Wang, Zhou and Zhu (2009), and Bien and Tibshirani (2011), among others. 

9 

Bonferroni’s procedure, without imposing any further restrictions on the degree to which the underlying tests depend on each other. 

If we abstract from the T subscript and order the p-values of the tests, so that 



are associated with the null hypotheses, H(01), H(02), ..., H(0n), respectively, Holm’s procedure rejects H(01) if p(1) ≤ p/n, rejects H(01) and H(02) if p(2) ≤ p/(n − 1), rejects H(01), H(02) and H(03) if p(3) ≤ p/(n − 2), and so on.<sup>7</sup> 

In our application, we apply multiple testing procedures to distinct non-diagonal elements of the sample estimate of R = (ρij), namely R<sup>ˆ</sup> = (ˆρij), where ˆρij is the correlation of the de-factored price changes between i and j MSAs. BPS show that the application of the Bonferroni procedure to R<sup>ˆ</sup> yields a regularised version which converges to R at the rate of ~~�~~ mN N/T under the Frobenius norm, where mN is bounded in N , and represents the number of non-zero off-diagonal elements in each row of R. More importantly for the present application, BPS establish that the zeros of W = (wij) are consistently estimated by 



where Cp(N ) = Φ<sup>−1 �</sup> 1 − N (Np−1) � , p is the pre-specified overall size of the test (which we set to 5% in the empirical application), and Φ<sup>−1</sup> (·) is the inverse of the cumulative standard normal distribution. More specifically, consider the true positive rate (TPR) and the false positive rate (FPR) of ones/zeros in the W matrix as defined by 



BPS show that under certain plausible regularity conditions TPR → 1 and FPR → 0 as N and T →∞ with probability one, so long as ρmin = mini,j(ρij) > Cp(N )/√T . Similar results also hold if the Holm procedure is applied. Let n = N (N − 1)/2 and order the p-values of n individual tests in an ascending manner, which is equivalent to ordering ��ρˆij�� in a descending manner. Denote the largest value of ��ρˆij�� over all i = j, by ��ρˆ(1)��, the second largest value by ��ρˆ(2)��, and so on, to obtain the ordered sequence ��ρˆ(s)��, for s = 1, 2, ..., n. Then the (i, j) pair associated with ��ρˆ(s)�� are connected (i.e. wij = 0) if ��ρˆ(s)�� > T −1/2Φ−1<sup>�</sup> 1 − m−p/s2+1 �, otherwise disconnected (i.e. wij = 0), for s = 1, 2, ..., n . The resultant connection matrix will be denoted by W<sup>ˆ</sup> = ( ˆwij), where wˆij = 1 if the (i, j) ˆ pair are connected according to the Holm procedure, otherwise wij = 0. Connections can also be classified as positive ( wˆij<sup>+)ifρˆ</sup> ij<sup>> 0,andnegative(w ˆ</sup> ij<sup>−)ifρˆ</sup> ij<sup>< 0.</sup> 

> 7 Other multiple testing procedures can also be considered such as Hochberg (1988), Hommel (1988) and Hommel (1989) among others - we thank an anonymous referee for drawing our attention to these contributions to the multiple testing literature. Efron (2010) also provides a recent review. But most of these procedures tend to place undue prior restrictions on the dependence of the underlying test statistics while the Holm method is not subject to such restrictions. 

10 

### 3.2 A heterogeneous spatio-temporal model 

Almost all spatial econometric models estimated in the literature assume that the spatial parameters do not vary across the units. For example, in the case of the SAR(1) model defined by (1), the parameter ψ is restricted to be the same across i = 1, 2, ..., N . Such parameter homogeneity assumptions are unavoidable when T is very small, but need not be imposed in the case of large panels where T is sufficiently large. The evidence of parameter heterogeneity in panel data models is quite prevalent particularly in the case of cross county or country data sets. In such cases and when T is sufficiently large, reducing the spatial effects into a single parameter appears rather restrictive. Instead, Aquaro, Bailey and Pesaran (2014, ABP) allow the spatial effects to differ across the units, and derive the conditions needed for identification and consistent estimation under parameter heterogeneity.<sup>8</sup> ABP consider the following heterogeneous version of (1) 



where x<sup>∗</sup> it<sup>= w</sup> i<sup>′x</sup> ◦<sup>t,w</sup> i<sup>′denotes the ithrow of the N × Nrow-standardised spatialmatrix,</sup> W, which is taken as given. In the spatial econometrics literature it is assumed that all units have at least one neighbour (or connection), which ensures that wi<sup>′τ=1foralli,</sup> when W is row-standardised. But as we shall see, particularly when using correlationbased weights, it is possible for some units not to have any connections. In such cases x<sup>∗</sup> it<sup>= 0, and the associated coefficient, ψ</sup> i<sup>, is unidentified, and to resolve the identification</sup> problem, and without of loss of generality, we set ψi = 0. Notice that since for such units x<sup>∗</sup> it<sup>= 0,thechoiceofψ</sup> i<sup>willnotimpacttheresults.</sup> In matrix notation we have 



where Ψ = diag (ψ), and ψ = (ψ1, ψ2, . . . , ψN )<sup>′</sup> . An extension of (16), that incorporates richer temporal and spatial dynamics and accommodates negative as well as positive connections, is given by 



where hλ = max(hλ1, hλ2, ..., hλN ), h<sup>+</sup> ψ<sup>= max(h+</sup> ψ1<sup>, h+</sup> ψ2<sup>, ..., h+</sup> ψN<sup>), h−</sup> ψ<sup>= max(h−</sup> ψ1<sup>, h−</sup> ψ2<sup>, ..., h−</sup> ψN<sup>),</sup> Λj, Ψ<sup>+</sup> j<sup>andΨ−</sup> j<sup>areN × Ndiagonalmatriceswith λij,ψ+</sup> ij<sup>andψ−</sup> ij<sup>over iastheirdiago-</sup> nal elements. Also, W<sup>+</sup> and W<sup>−</sup> are N × N network matrices for positive and negative connections, respectively such that W = W<sup>+</sup> + W<sup>−</sup> . In this model the slope coefficients, λij, ψ<sup>+</sup> ij<sup>andψ−</sup> ij<sup>,andtheerrorvariances,σ2</sup> ui<sup>= var(uit)areallowedtodifferacrossi.In</sup> what follows for expositional simplicity we set hλ = h<sup>+</sup> ψ<sup>= h−</sup> ψ<sup>= 1.</sup> For consistent estimation of the parameters ABP propose a QML procedure, and suggest using the following concentrated log-likelihood function to simplify the computations: 



> 8The literature on panel data models with heterogeneous slopes is reviewed in Hsiao and Pesaran (2008). 

11 

� where xi = xi − ψ<sup>+</sup> i0<sup>x+</sup> i<sup>−ψ</sup> i<sup>−</sup> 0<sup>x−</sup> i<sup>,Mi=IT−Zi (Z′</sup> i<sup>Zi)−1 Z′</sup> i<sup>,Zi=</sup> �xi,−1, x<sup>+</sup> i,−1<sup>, x−</sup> i,−1� , ψ<sup>+</sup> 0<sup>=(ψ+</sup> 10<sup>, ψ+</sup> 20<sup>, . . . , ψ</sup> N<sup>+</sup> 0<sup>)′andψ−</sup> 0<sup>=(ψ−</sup> 10<sup>, ψ</sup> 20<sup>−, . . . , ψ</sup> N<sup>−</sup> 0<sup>)′.Theparametersofthelagged</sup> variables, λ1, ψ<sup>+</sup> 1<sup>andψ−</sup> 1<sup>,canbeestimatedbyleastsquaresappliedtotheequations</sup> for individual units conditional on ψ<sup>+</sup> i0<sup>andψ−</sup> i0<sup>.Inferenceonindividualcoefficientsare</sup> then carried out using second cross derivatives of the full likelihood function of (17), with ′ ′ respect to θ = (θ<sup>′</sup> 1<sup>, θ′</sup> 2<sup>, ..., θ′</sup> N<sup>)</sup> , where θi = �ψ<sup>+</sup> i0<sup>, ψ</sup> i<sup>−</sup> 0<sup>, ψ</sup> i<sup>+</sup> 1<sup>, ψ−</sup> i1<sup>, λi1, σ2</sup> ui� . The variancecovariance matrix of θ<sup>ˆ</sup> ML is computed as 



Further details regarding the econometric analysis of this model are provided in Aquaro, Bailey and Pesaran (2014). 

## 4 Application: US house prices 

The two-step procedure developed in this paper can be applied to different types of panel data sets so long as the time series dimension of the panel is reasonably large such that reliable estimates of pair-wise correlations, ρij, can be obtained. There are many such panels, covering regions or countries, that can be considered. Regional data in the United States have been studied by many including Cromwell (1992), Pollakowski and Ray (1997), Carlino and DeFina (1998, 2004), Carlino and Sill (2001), Del Negro (2002), Owyang, Piger and Wall (2005), and Partridge and Rickman (2005). The cross country data sets used in global modelling provide another example. 

Here we opt to study house price changes at the level of Metropolitan Statistical Areas in the US.<sup>9</sup> Metropolitan Statistical Areas (MSAs) are geographic entities delineated by the Office of Management and Budget and are used by Federal statistical agencies when collecting, tabulating, and publishing Federal statistics for spatial units in the USA. The MSA is defined by a core area with a large population concentration, together with adjacent areas that have a high degree of economic and social integration with that core through commuting and transport links. They range in size, as measured by population in 2008, from the smallest - Carson City - with a population of 55,000, to New York and its environs with a population of 18.97 million. Moreover, there can be considerable distances between MSAs. The pair-wise average distance is 1,156 miles, though of course this is exaggerated by the relative sparseness of the distribution of MSAs in the Midwest. Indeed, by comparison, the study of regional house prices in the UK by Holly, Pesaran and Yamagata (2011b) deals with distances of a much smaller magnitude. Distance is, therefore, likely to be an important factor for the spatial distribution of house prices, though size could play a role as well. 

> 9There already exists a large literature on the spatial dimension of house price changes, partly because of the availability of spatially disaggregated data, but also because of the role that housing plays in household wealth and in the transmission of monetary policy shocks, and more recently as a conduit for transmission of global shocks. Recent contributions include Rapach and Strauss (2007, 2009), Kadiyala and Bhattacharya (2009), Gupta and Das (2010), Gupta, Kabundi and Miller (2011a,b), Kuethe and Pede (2011), and Gupta and Miller (2012). These papers apply a number of models to house price data without prior assessment of their degree of cross-sectional dependence. 

12 

Our choice of house prices is also motivated by the role that housing plays in spatial equilibrium models (Glaeser, Gyourko and Saiz (2008), Glaeser and Gottlieb (2009)). The standard approach in urban and regional economics is to assume a spatial equilibrium. At the margin firms and households have to be indifferent between alternative locations. Firms employ labour up to the point at which the wage is equal to marginal product; construction companies supply housing up to the point at which marginal cost is equal to marginal product. Finally, households have to be indifferent about where they are located, taking into account wages, the price of houses and the local availability of amenities (proximity to schools, sea, mountains, temperature, etc.). The combination of the labour supply curve, the supply curve for housing and the labour demand determines simultaneously the population of say a locality, wages and the price of housing. Idiosyncratic differences in space in terms of productivity, particular characteristics of an area and the construction sector determine differences across space in population density, household incomes and the house prices. There are a number of equilibrating processes at work. Households tend to move across geographical areas in response to differences in wages, house prices and area characteristics. There can also be agglomeration effects due to economies of scale in relation to size and population density of cities. But, it should be clear that such equilibrating tendencies are likely to operate fully only in the long run, over a number of years rather than quarters. It takes time for households to relocate in response to changing economic circumstances. It also takes time for construction companies to increase the supply of housing. Any model of house price diffusion across MSAs must also adequately deal with dynamics, both within and across MSAs. 

We consider 363 MSAs in total, excluding three MSAs located in Alaska and Hawaii,<sup>10</sup> over the period 1975Q1 to 2010Q4 (T = 144). We denote the level of house prices in MSA i , located in State s, in quarter t, by Pist, for i = 1, ..., Ns, s = 1, ..., S, and t = 1, ..., T, where<sup>�S</sup> s=1<sup>Ns=N=363,S=49(comprisedof48contiguousStatesandthedistrict</sup> of Columbia), and T = 144 quarters. Then we compute real house prices as: 



where CPIst is the Consumer Price Index of State s in quarter t. Details on the sources of these data can be found in Appendix I. We ordered the MSAs by State, starting at the East Coast and moving towards the West Coast, following the list provided in Table A of Appendix II. Finally, we obtain seasonally adjusted changes in real house prices, πist, as residuals from regressing pist − pis,t−1, the seasonally unadjusted rate of change in real house prices, on an intercept and three quarterly seasonal dummies. Before modelling the spatial dimension of the price changes, πist, we first need to examine the extent to which these price changes are cross-sectionally strongly correlated and then de-factor such effects if necessary. (see sub-section 2.4) 

### 4.1 Cross-sectional dependence in house price changes and defactoring of observations 

To examine the degree of cross-sectional dependence in house price changes, we computed the CD statistic of Pesaran (2004, 2014) for price changes, πist, without any de-factoring. 

> 10Note that the District of Columbia is treated as a single MSA. 

13 

(See (12) and (13)). We obtained CDπ = 640.46 ��ρ¯π = 0.209� as compared to a critical value of 1.96 at the 5% significance level. The test outcome is statistically highly significant and suggests a high degree of cross-sectional dependence in house price changes, which could be due to common national and regional effects. Applying the method proposed by BKP we calculate the exponent of cross-sectional dependence (standard error in parenthesis) for house price changes and obtain ˚απ = 0.989 (0.03), which is very close to unity and suggests that house price changes are strongly correlated across MSAs. Clearly, it would be inappropriate to apply standard spatial modelling techniques directly to πist, as noted earlier since the maintained assumption of spatial econometric models is weak cross-sectional dependence as shown in sub-section 2.1. 

#### 4.1.1 De-factoring using cross-sectional averages 

The strong cross-sectional dependence in house price changes can be modelled using observed (national/regional income, unemployment and interest rates), or unobserved common factors (using principal components). Alternatively, one can use cross-sectional averages at the national and regional levels, which corresponds to assuming the existence of a national factor together with a number of region-specific factors.<sup>11</sup> The correspondence of cross-sectional averages and the national and regional factors can be established using arguments similar to the ones advanced in Pesaran (2006). In what follows we employ the Bureau of Economic Analysis classification and consider a total of R = 8 regions in the US containing an average of approximately 45 MSAs each. These are: (i) New England, (ii) Mid East, (iii) South East, (iv) Great Lakes, (v) Plains, (vi) South West, (vii) Rocky Mountains, and (viii) Far West. See Table A of Appendix II for more details. 

Accordingly, let πirt denote the rate of change of real house prices (after seasonal adjustments) in the i<sup>th</sup> MSA located in region r = 1, 2, ..., R, at time t, and consider the following hierarchical model 



¯ Nr Nr where , πrt = Nr<sup>−1</sup> �i=1<sup>πirt,andπ¯t=N −1 �R</sup> r=1 �i=1<sup>πirt,withN=�R</sup> r=1<sup>Nr.Write</sup> the above model more compactly as 



where πt is an N × 1 vector of house price changes partitioned by regions, namely 



Similarly 



B and Γ are N × N diagonal matrices with their ordered elements given by 



> 11We also considered using State level averages, but there were only a few MSAs in some States. 

14 

and 



respectively. Finally, QN and PN are N × N projection matrices such that QN πt give the regional means and PN πt the national mean of the local feature. More specifically, let τ Nr be an Nr × 1 vector of ones, and τ N an N × 1 vector of ones, then 



and 



where PNr = τ Nr(τ<sup>′</sup> Nr<sup>τ N</sup> r<sup>)−1τ ′</sup> Nr<sup>.ItisassumedthatRisfixed,andforeachr,Nr/N</sup> tends to a non-zero constant as N →∞. PNrπt, for r = 1, 2, ..., R, and PN πt can be viewed as regional and national factors that are consistently estimated by simple averages. They also represent the strong form of cross-sectional dependence in the real house price changes across MSAs. 

The de-factored real house price changes are then given by residuals from (21), namely 



To check if de-factoring has been successful (step 1(b) in sub-section 2.4), we apply the CD test to the residuals,<sup>ˆ</sup> ξt. The resulting CD statistic is much reduced, falling from 640.45 to −6.05, giving a very small estimate for the average pair-wise correlations,<sup>�</sup> ρ¯ˆξ = −0.002. Therefore, the simple hierarchical de-factoring procedure has managed to eliminate almost all of the strong cross-sectional dependence that had existed in house price changes, and what remains could be due to the local dependencies that need to be modelled using spatial techniques. Also, the estimate of the exponent of cross-sectional dependence, α, which stood at ˚απ = 0.989 (0.03) is now reduced to ˚αˆξ = 0.637 (0.03) which is close to the borderline value of 1/2, representing weak cross-sectional dependence. 

#### 4.1.2 De-factoring using Principal Components 

For comparison we repeat the de-factoring analysis by applying the method of principal components developed for large panels in Bai (2003) to price changes, to begin with without a regional classification. Consider the following m-factor model for πit 



where f t is an m × 1 vector of unobserved factors. For the time being suppose that m is known. Then the factors can be estimated by the first m principal components (PC) of real house price changes, and the de-factored observations can be obtained as residuals from regressions of πit on the m largest PCs. To select m we applied the six information criteria (IC) proposed in Bai and Ng (2002), specifying 8 as the maximum number of factors to match the number of cross-sectional averages used in the hierarchical specification of the previous sub-section. All six IC ended up selecting 8 as the optimal 

15 

number of factors. We increased the maximum number of factors in the procedure, but still ended up selecting the maximum as the optimal. In view of the failure of the IC to lead to any meaningful outcome, we decided to conduct the de-factoring analysis using m = 2, 3, ..., 8 principal components. We then computed CD statistics for the de-factored residuals for all 7 choices of m, and obtained the values of 53.39, 10.21, 2.73, 3.27, 2.31, −1.96 and −4.42 respectively, for m = 2, 3, ..., 8. The corresponding estimates of the ˚ ˚ exponent of cross-sectional dependence were α2pc = 0.932 (0.04), α3pc = 0.799 (0.04) , ˚ ˚ ˚ ˚ α4pc = 0.793 (0.03) , α5pc = 0.785 (0.03) , α6pc = 0.831 (0.02) , α7pc = 0.718 (0.02) , and ˚ α8pc = 0.622 (0.02) , respectively. It is evident that as more factors are added the strength of cross-sectional dependence of the resulting residuals diminishes progressively. 

However since the testing procedure for the determination of m appears inconclusive, and following a suggestion by an anonymous referee, we considered a hierarchical PCA, similar to the specification in (21), where the national factor is represented by the strongest principal component extracted from the full data set and the regional factor(s) are expressed as the strongest principal component(s) extracted from each of the eight regions separately. Such a hierarchical factor model can be written as 



where f rt is an mr ×1 vector of regional factors for r = 1, 2, ..., R, and fgt is the ‘global’ or ′ ‘national’ factor. βir = �βi1, βi2, ..., βimr� and γir are associated factor loadings. Again to select the number of PCs, mr, in each region we applied the six information criteria of Bai and Ng (2002). The results using as the maximum number of factors of 4 and 8 in their procedure, are shown in Table 1 below: 

Table 1: Number of factors selected at national and regional levels using the Bai and Ng information criteria 

||National|New Engl.|Mid East|South East<br>Gr. Lakes|Plains|South West|Rock. Mount.|Far West|
|---|---|---|---|---|---|---|---|---|
|||||Maximum number of facto<br><br>|rs assum<br>|ed = 8<br>|||
|PC1|8|8|7|8<br>7|7|6|7|8|
|PC2|8|8|6|8<br>7|6|5|7|7|
|PC3|8|8|8|8<br>8|8|8|8|8|
|IC1|8|8|4|8<br>7|4|2|2|8|
|IC2|8|8|4|6<br>3|2|2|2|4|
|IC3|8|8|8|8<br>8|6|5|7|8|
|||||Maximum number of facto<br><br>|rs assum<br>|ed = 4<br>|||
|PC1|4|4|4|4<br>4|4|4|4|4|
|PC2|4|4|4|4<br>4|4|3|3|4|
|PC3|4|4|4|4<br>4|4|4|4|4|
|IC1|4|4|4|4<br>4|4|2|2|4|
|IC2|4|4|4|4<br>3|2|2|2|4|
|IC3|4|4|4|4<br>4|4|4|4|4|
|Notes: <br>|The Bai ad Ng <br>|(2002) informatio<br>|n criteria are se|t out in what follows: PC1(mr) = <br><br> <sup>2</sup><br>|Vmr +mr�σ<sup>2</sup>|<sup>(T +Nr)</sup><br>(T Nr) <sup>ln</sup><br>~~�~~<br>T Nr<br>(T+Nr)<br><br><br><br>|~~�~~<br>,<br>||
|PC2(m<br>IC2(mr<br>(NrT)<sup>−</sup><br>and C<sup>2</sup><br>N|r) =Vmr +mr<br>) = ln (Vmr) +<br><sup>1 �N</sup><br>i=1<br>�T<br>t=1 <sup>E</sup><br>rT <sup>= T ∧Nr :=</sup>|�σ<sup>2(T +Nr)</sup><br>(T Nr) <sup>ln C2</sup><br>NT <br> mr<br>�(T +Nr)<br>T Nr<br>�<br>ln <br><sup>(ξ′</sup><br>irt<sup>) from πirt </sup><br><sup>min (T, Nr). Als</sup>|<sup>, PC3 (mr) = V</sup><br>C<sup>2</sup><br>NrT <sup>and IC3 (</sup><br><sup>= β′</sup><br>ir <sup>ˆ</sup><br>frt+ξ<sup>′</sup><br>irt<br><sup>o, Vmr</sup> <sup>= (NrT</sup>|<sup>mr</sup> <sup>+ mr�σ2</sup><br>�<br>lnC<br>T Nr<br>C<sup>2</sup><br>NrT<br>�<br>, IC1(mr)<br> <sup>mr) = ln (Vmr) + mr</sup><br>�<br>lnC<sup>2</sup><br>NrT<br>C<sup>2</sup><br>NrT<br>�<br>. <br><sup>, i = 1, 2, ..., Nr; r = 1, 2, ..., R; t = 2</sup><br><sup>)−1 �Nr</sup><br>i=1<br>�T<br>t=1<br>�<br>πirt−<sup>�mr</sup><br>j=1 <sup>�βj,i</sup> <sup>�f</sup>|= ln (Vmr) +<br>Here �σ<sup>2 </sup>is a <br> <sup>, ..., T,</sup><br><sup>j,t</sup><br>�2<br>, for r =|mr<br>�<br>(T +Nr)<br>T Nr<br>�<br>ln<br>�<br><br> consistent estimate <br>1, ..., R.|T Nr<br>(T+Nr)<br>�<br>,<br> of||



In the global and eight regional cases all six IC selected more than one PC though some variation in the number of PCs is evident across regions. Again given the lack of clear guidance as to the number of principal components to use in (24), and in order to strike 

16 

a balance between purging the house price changes of common effects and still leaving a sufficient degree of spatial dependence in the de-factored observations we decided to opt for one PC as the ‘national’ factor and mr = 2 for all regions considered. As before we computed the CD statistic of the de-factored residuals from regressions (24) which amounted to a value of 3.320 ��ρ¯ˆξpc = 0.001�, which is comparable to the results obtained using the national and regional cross-sectional averages. The estimate of the exponent ˚ of cross-sectional dependence in this case turned out to be αpc = 0.773 (0.03), which is somewhat larger than the estimate ˚αˆξ = 0.637 (0.03) obtained using the cross-sectional averages as factors. 

It is clear that both de-factoring methods (cross-sectional averages and PC) do reasonably well in purging price changes of common effects, although the hierarchical version of the PC seems preferable to the standard application of PC to house price changes without any regional classification. 

### 4.2 Estimation of spatial connections 

Having computed de-factored price changes,<sup>ˆ</sup> ξit - from (22), and<sup>ˆ</sup> ξit,pc - from (24), we are now in a position to apply the methodology developed in sub-section 3.1 to estimate the matrix of connections, W<sup>ˆ</sup> , using pair-wise correlations of de-factored price changes. 

#### 4.2.1 Spatial weights matrices based on distance 

We start our analysis with a standard specification of W based on contiguity measures, which we also use as a benchmark to examine the estimates of W that are based on pair-wise correlations, ˆρij. As noted above, MSAs are deliberately defined as one or more large cities with their core having a substantial influence over the surrounding region, with a high degree of economic and social integration through commuting or transport links. Hence, it can be argued that geographical distance can play an important role in the determination of connections across different MSAs. We consider the same 363 MSAs as before. We denote a weights matrix based on physical distance by Wd, and make use of data for geodesic distance (d) by applying the Haversine formula to data on the Latitude-Longitude of zip codes, cross referenced to each of the N = 363 MSAs.<sup>12</sup> We regard Wd (of dimension N × N ) to be symmetric. We identify as neighbours for each MSA, i (i = 1, ..., N ), all MSAs that lie within a radius of d miles. This pattern translates into a value of 1 for elements (i, j) and (j, i) of Wd if MSA i is a neighbour (falling within the given radius) of MSA j, or a value of 0 otherwise. Diagonal entries (i, i) take a value of 0, indicating that MSA i cannot be a neighbour of itself. Also under this specification all non-zero elements of Wd are viewed as representing a positive connection, which should be contrasted with connections that are based on economic factors that could lead to negative as well as positive connections. 

We study three cases: (i) MSAs within a radius of d = 50 miles, (ii) MSAs within a radius of d = 100 miles, and (iii) MSAs within a radius of d = 200 miles. These give rise to three Wd matrices, namely (i) W50m, (ii) W100m, and (iii) W200m, which are sparse by nature, but of different degree depending on the cut-off point set by the radius, d. We compare the degree of sparseness of W50m, W100m, and W200m in terms of their percentage of non-zero elements (excluding the diagonal elements). This percentage is 

> 12See Appendix III for details of this formula. 

17 

0.35% for W50m, 1.55% for W100m, and 5.39% for W200m. As expected, the number of non-zero elements increases when the radius within which MSAs are considered to be neighbours rises. Figure 1 displays all three Wd matrices. In this figure we have ordered the MSAs by States starting at the East Coast as before and following the list provided in Table A of Appendix II, from top to bottom and from left to right. The sparseness of the Wd matrices is captured by white areas in the graph when the relevant entries are equal to zero. As is to be expected there is considerable clustering along the diagonal, but because we are using a line to depict a plane, sometimes an MSA may lie at the edge of a State (or region) and fall within the radius of another State or region. Clearly, as the radius is increased from 50 to 200 miles the degree of leaching increases. 

Figure 1: Spatial weights matrices specified by distance 



<!-- Start of picture text -->
Radius=50 miles Radius=100 miles Radius=200 miles<br>0 0 0<br>50 50 50<br>100 100 100<br>150 150 150<br>200 200 200<br>250 250 250<br>300 300 300<br>350 350 350<br>0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350<br>nz = 462 nz = 2040 nz = 7084<br><!-- End of picture text -->

#### 4.2.2 Spatial weights matrices based on pair-wise correlations 

Next we make use of the de-factored price changes,<sup>ˆ</sup> ξit and<sup>ˆ</sup> ξit,pc, to estimate the matrix of connections. Focussing on<sup>ˆ</sup> ξit, first we obtain the sample correlation matrix of<sup>ˆ</sup> <u>ξt</u> = (<sup>ˆ</sup> <u>ξit),</u> ˆ ˆ ˆ ˆ ˆ ˆRξ = (ˆρˆξ,ij) from the residuals of regression (21), where ρˆξ,ij = ρˆξ,ji = σˆξ,ij/ σˆξ,iiσˆξ,jj, � ˆ and σˆξ,ij = T<sup>−1 �T</sup> t=1<sup>ˆξ</sup> it<sup>ˆξ</sup> jt<sup>.Next,weapplyHolm’smultipletestingtotheN (N−1) /2</sup> ˆ pair-wise correlation coefficients, ρˆξ,ij, for i = 1, 2, ..., N − 1, j = i + 1, ..., N , as described ˆ in sub-section 3.1. We denote the resultant connection matrix by W<sup>ˆ</sup> cs = �wcsij �. Here cs stands for multiple testing applied to residuals extracted from de-factoring using the cross-sectional averages approach. 

As in sub-section 4.2.1, measuring the degree of sparseness of W<sup>ˆ</sup> cs by the percentage of its non-zero elements we obtain the figure of 1.08% which is comparable to the 1.55% we obtained for W 100m, although as can be see from Figure 2 the pattern of sparseness of the two matrices, W100m and W<sup>ˆ</sup> cs, are quite different. In fact it is best to view the non-zero elements of W<sup>ˆ</sup> cs as connections rather than as neighbours (in a physical sense). According to W<sup>ˆ</sup> cs, the connections extend well beyond geographical boundaries, though distinct clusters are evident especially in the West Coast and parts of the East Coast regions.<sup>13</sup> Divisions of the connections into the East, the Middle and West of the country are also visible. 

> 13Recall that in these graphs MSAs are ordered by State, moving from East to West, from top to bottom and left to right. 

18 

Figure 2: Spatial weights matrix using multiple testing and W100m De-factoring using cross-sectional averages 



<!-- Start of picture text -->
Wˆ cs W100m<br>0 0<br>50 50<br>100 100<br>150 150<br>200 200<br>250 250<br>300 300<br>350 350<br>0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350<br>nz = 1414 nz = 2040<br><!-- End of picture text -->

#### 4.2.3 Positive and negative connections 

Unlike the distance based Wd weights matrices, the connections identified by the correlation based approach can be readily distinguished into positive and negative ones. This can be done by associating positive connections with statistically significant evidence of a positive correlation, and the negative connections with the evidence of statistically significant pair-wise negative correlations. Accordingly, we can now define the positively and negatively connected weights matrices, W<sup>ˆ</sup> cs<sup>+= (wˆ</sup> ij,cs<sup>+)and</sup> W<sup>ˆ</sup> cs<sup>−=</sup> �wˆij,cs<sup>−</sup> �, respectively, by 



Clearly, W<sup>ˆ</sup> cs = W<sup>ˆ</sup> cs<sup>++</sup> W<sup>ˆ</sup> cs<sup>−.Comparingthesewiththedistancebasedweightsmatrix,</sup> W100m, in Figure 3, at first glance we notice that W<sup>ˆ</sup> cs<sup>+ismorecloselyrelatedtoW100m</sup> than is W<sup>ˆ</sup> cs<sup>−.Further,itisevidentthatgeographicalproximityisnottheonlyfactor</sup> driving spatial connections between MSAs. There are significant correlations (positive or negative) well away from the diagonal, with a number of clusters suggesting connections at considerable distances. 

Figure 3: Spatial weights matrices - distance and correlation-based connections (CS) 



<!-- Start of picture text -->
W100m Wˆ cs + Wˆ cs −<br>0 0 0<br>50 50 50<br>100 100 100<br>150 150 150<br>200 200 200<br>250 250 250<br>300 300 300<br>350 350 350<br>0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350<br>nz = 2040 nz = 822 nz = 592<br><!-- End of picture text -->

19 

We also applied the multiple testing procedure to the de-factored house price changes using the hierarchical factor model, (24), and obtained the weights matrix W<sup>ˆ</sup> pc. The degree of sparseness of this matrix, as measured by the percentage of their non-zero elements, is 0.60%. Comparing W<sup>ˆ</sup> pc with the distance-based matrices W50m, W100m, and W200m, it appears that using the hierarchical principal components approach the degreeWˆ pc<sup>+and</sup> of sparsenessW<sup>ˆ</sup> pc<sup>−inline</sup> of<sup>with</sup> W<sup>ˆ</sup> pc<sup>the</sup> is mid-way<sup>procedure</sup> between<sup>described</sup> W50m<sup>earlier.</sup> and WWˆ100pc<sup>+</sup> m<sup>,</sup> . WWe<sup>ˆ</sup> pc<sup>−</sup> also<sup>and</sup> constructed<sup>W100mare</sup> plotted in Figure 4 below. As with the cross-sectional averages approach, the PC method suggests that positively correlated connections match more closely the distance-based connections than do the negatively correlated connections. 

Figure 4: Spatial weights matrices - distance and correlation-based connections (PCs) 



<!-- Start of picture text -->
W100m Wˆ pc + Wˆ pc −<br>0 0 0<br>50 50 50<br>100 100 100<br>150 150 150<br>200 200 200<br>250 250 250<br>300 300 300<br>350 350 350<br>0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350 0 50 100 150 200 250 300 350<br>nz = 2040 nz = 446 nz = 344<br><!-- End of picture text -->

#### 4.2.4 Statistical associations of different connection weights matrices 

We assess the closeness of the correlation-based estimates, W<sup>ˆ+</sup> and W<sup>ˆ−</sup> (using either cs or pc regressions for de-factoring) with the distance-based weight matrix, Wd, more formally by quantifying the statistical association of the two types of weights matrices. The analysis is complicated by the fact that these matrices are by nature sparse, and hence the probability of a zero realisation in both adjacency matrices W<sup>ˆ+</sup> (or W<sup>ˆ−</sup> ) and Wd is higher than obtaining a common entry of 1.<sup>14</sup> Given the symmetry of the weights matrices in our application, we focus on the upper triangular elements. We create contingency tables from these upper-triangular elements of the form 



where: 

- n11 equals the number of times W<sup>ˆ+</sup> (or W<sup>ˆ−</sup> ) displays entry of 1 when Wd displays 1. 

- n00 equals the number of times W<sup>ˆ+</sup> (or W<sup>ˆ−</sup> ) displays entry of 0 when Wd displays 0. 

> 14For more details regarding testing the dependence among multicategory variables see Pesaran and Timmermann (2009). 

20 

- n01 equals the number of times W<sup>ˆ+</sup> (or W<sup>ˆ−</sup> ) displays entry of 0 when Wd displays 1. 



Then, n11 + n00 + n01 + n10 = N (N − 1) /2, and Pearson’s chi-squared statistic - Pearson (1900) - is given by 



We set the significance level at 5%. We compare W<sup>ˆ+</sup> (or W<sup>ˆ−</sup> ) with the three versions of Wd, namely W50m, W100m, and W200m. For brevity of exposition we present the contingency tables for W<sup>ˆ</sup> cs<sup>+and</sup> W<sup>ˆ</sup> cs<sup>−versusW100only:</sup> 

Table 2: Contingency tables - W<sup>ˆ</sup> cs<sup>+and</sup> W<sup>ˆ</sup> cs<sup>−versusW100mspatialweightsmatrices</sup> 

|||W|100m||||W|100m||
|---|---|---|---|---|---|---|---|---|---|
|||1|0|�<br>rows|||1|0|�<br>rows|
||1|54|357|411||1|8|288|296|
|ˆ<br>W+<br>cs|0|966|64326|65292|ˆ<br>W−<br>cs|0|1012|64395|65407|
||�<br>cols|1020|64683|65703||�<br>cols|1020|64683|65703|



It is clear that W<sup>ˆ</sup> cs<sup>+has more elements in common with Wdthan does</sup> W<sup>ˆ</sup> cs<sup>−.The χ2</sup> 5% statistics for W<sup>ˆ</sup> cs<sup>+and</sup> W<sup>ˆ</sup> cs<sup>−versusW50m,W100m,andW200mrespectivelyareshownin</sup> Table 3 below (to be compared with a critical value of 3.84): 

Table 3: Pearson’s χ<sup>2</sup> 5%<sup>teststatistics</sup> 

|ˆ<br>W<sup>+</sup><br>cs <sup>and </sup>|<sup>ˆ</sup><br>W<sup>−</sup><br>cs <sup>versus </sup>|<sup>W</sup>d<sup>, d = 50, </sup>|<sup>100, 200m</sup>|
|---|---|---|---|
||W50m|W100m|W200m|
|ˆ<br>W<sup>+</sup><br>cs|267.24|363.27|298.41|
|ˆ<br>W<sup>−</sup><br>cs|0.89|2.57|4.30|



The chi squared test statistics are highly significant especially when W<sup>ˆ</sup> cs<sup>+is considered.</sup> Elements of W<sup>ˆ</sup> cs<sup>+aremuchmorecloselyassociatedwiththespatialweights,Wd,than</sup> the elements of W<sup>ˆ</sup> cs<sup>−.The association between</sup> W<sup>ˆ</sup> cs<sup>+and Wdis the largest when d = 100.</sup> Finally, we repeat these comparisons with weights based on de-factored price changes using the hierarchical PCs, and obtain similar results. See Tables 3 and 4 where W<sup>ˆ</sup> pc<sup>+</sup> and W<sup>ˆ</sup> pc<sup>−arecomparedwithWd,</sup> W<sup>ˆ</sup> cs<sup>+and</sup> W<sup>ˆ</sup> cs<sup>−.Theassociationbetween</sup> W<sup>ˆ</sup> cs<sup>+and</sup> W<sup>ˆ</sup> pc<sup>+</sup> is particularly high, and gives a chi-squared statistic of 9673.7 (compared with a critical value of 3.84). 

21 

Table 4: Pearson’s χ<sup>2</sup> 5%<sup>teststatistics</sup> 

|ˆ<br>W<sup>+</sup><br>pc <sup>and </sup>|<sup>ˆ</sup><br>W<sup>−</sup><br>pc <sup>versus </sup>|<sup>W</sup>d<sup>, d = 50, 100, 200m</sup>|
|---|---|---|
||W50m|W100m<br>W200m|
|ˆ<br>W<sup>+</sup><br>pc|86.70<br>|149.55<br>84.66|
|ˆ<br>W<sup>−</sup><br>pc|0.61|0.17<br>3.75|



Table 5: Contingency tables - W<sup>ˆ</sup> cs<sup>+/−</sup> versus W<sup>ˆ</sup> pc<sup>+/−</sup> spatial weights matrices 

||||ˆ<br>W<sup>+</sup><br>pc|||||ˆ<br>W<sup>−</sup><br>pc||
|---|---|---|---|---|---|---|---|---|---|
|||1|0|�<br>rows|||1|0|�<br>rows|
||1|117|106|223||1|71|101|172|
|ˆ<br>W+<br>cs|0|294|65186|65480|ˆ<br>W−<br>cs|0|225|65306|65531|
||�<br>cols|411|65292|65703||�<br>cols|296|65407|65703|



### 4.3 A heterogeneous spatio-temporal model of US house price changes 

Finally, we are in a position to illustrate the utility of the separate identification of positive and negative connections for the spatial analysis of house price changes. We model the de-factored house price changes,<sup>ˆ</sup> ξit, using the spatio-temporal model given by (17), with W<sup>+</sup> and W<sup>−</sup> replaced by their estimates W<sup>ˆ+</sup> and W<sup>ˆ−</sup> using de-factored residuals. The estimation results are similar for both approaches to de-factoring, and to save space we focus on the de-factored observations and W estimates using cross-sectional averages as factors (see (20)). We also restrict the lag orders, hλ, h<sup>+</sup> ψ<sup>andh−</sup> ψ<sup>,tounity(astheyseem</sup> adequate for capturing the temporal dynamics), and row-standardise the weight matrices to identify the spatial effects across the MSAs. This yields 



where W<sup>˜</sup> cs<sup>+and</sup> W<sup>˜</sup> cs<sup>−arethescaled(row-standardisedwhenapplicable)versionsof</sup> W<sup>ˆ</sup> cs<sup>+</sup> and W<sup>ˆ</sup> cs<sup>−,andaξ=(α1ξ, α2ξ, ..., αNξ)′istheN× 1vectorofintercepts.Λ=diag (λ) ,</sup> Ψ<sup>+</sup> 0<sup>=diag</sup> �ψ<sup>+</sup> 0 � , Ψ<sup>−</sup> 0<sup>=diag</sup> �ψ<sup>−</sup> 0 �, Ψ<sup>+</sup> 1<sup>=diag</sup> �ψ<sup>+</sup> 1 � , and Ψ<sup>−</sup> 1<sup>=diag</sup> �ψ<sup>−</sup> 1 �, where λ1 = (λ11, λ21, ..., λN 1)<sup>′</sup> , ψ<sup>+</sup> s<sup>= (ψ+</sup> 1s<sup>, ψ</sup> 2<sup>+</sup> s<sup>, ..., ψ+</sup> Ns<sup>)′,ψ−</sup> s<sup>= (ψ−</sup> 1s<sup>, ψ</sup> 2<sup>−</sup> s<sup>, ..., ψ−</sup> Ns<sup>)′,fors = 0and</sup> 1, and ζt = (ζ 1t, ζ 2t, ..., ζ Nt)<sup>′</sup> are the error terms. For quasi-maximum likelihood (QML) estimation of the parameters we assume that ζ it ∼ IIDN �0, σ<sup>2</sup> ς i�, for i = 1, 2, ..., N . Notice that we continue to have W<sup>˜</sup> cs<sup>++</sup> W<sup>˜</sup> cs<sup>−=</sup> W<sup>˜</sup> cs where W<sup>˜</sup> cs is the row-standardized version of W<sup>ˆ</sup> cs, and (25) reduces to the more familiar specification 



under the restrictions Ψ<sup>+</sup> j<sup>=Ψ−</sup> j<sup>=Ψj,forallj=0and1,arestrictionthatcanbe</sup> tested within our framework. 

22 

The model specification in (25) allows for a high degree of heterogeneity in dynamics and spatial dependence across the 363 MSAs. By comparison, the traditional spatial model assumes that the dynamic and spatial coefficients are homogeneous, namely λ1i = λ1, ψ<sup>+</sup> is<sup>=ψ+</sup> s<sup>,ψ−</sup> is<sup>=ψ−</sup> s<sup>,fors=0and1,andforalli.Theonlyformsofheterogeneity</sup> allowed in the literature are intercept and error variance heterogeneity. Furthermore, the existing spatial literature assumes that all units in Wd have at least one (positive) neighbour - see Kelejian and Prucha (1999, 2010) among others. This need not always hold. When applying the multiple testing procedure to the de-factored observations we find a relatively small number of units, N0 = 76 (out of 363), that are not connected to the remaining MSAs. There are also a number of MSAs with only negative connections, N− = 34, and a number with only positive connections, N+ = 90, with the remaining N+/− = 163 MSAs having both positive and negative connections, so that N = N+/− + N− + N+ + N0 = 363. The distribution of connections by the eight regions are given in Table 6. 

Table 6: Distribution of MSAs by connections across 8 regions in the US 

|Region\No. of MSAs|N+/−|N−|N+|N0|~~�~~<br>row|
|---|---|---|---|---|---|
|New England|9|1|1|4|15|
|Mid East|17|2|9|8|36|
|South East|63|10|25|16|114|
|Great Lakes|28|8|13|12|61|
|Plains|16|5|8|3|32|
|South West|14|3|7|14|38|
|Rocky Mountains|7|3|3|9|22|
|Far West|9|2|24|10|45|
|~~�~~<br>col|163|34|90|76|363|
||Proport|ional to|total no.|of MSAs|per region|
|New England|60.0%|6.7%|6.7%|26.7%|100.0%|
|Mid East|47.2%|5.6%|25.0%|22.2%|100.0%|
|South East|55.3%|8.8%|21.9%|14.0%|100.0%|
|Great Lakes|45.9%|13.1%|21.3%|19.7%|100.0%|
|Plains|50.0%|15.6%|25.0%|9.4%|100.0%|
|South West|36.8%|7.9%|18.4%|36.8%|100.0%|
|Rocky Mountains|31.8%|13.6%|13.6%|40.9%|100.0%|
|Far West|20.0%|4.4%|53.3%|22.2%|100.0%|



N+/− denotes the number of MSAs with both positive and negative connections; N− the no. of MSAs with only negative connections; N+ the no. of MSAs with only positive connections; finally N0 the no. of MSAs with no connections. 

It is clear that, for the most part, MSAs in all regions have both positive and negative connections. Also, more MSAs have exclusively positive connections than only negative connections across all regions, the most polarised regions being the South East and the Far West. On the other hand, a more balanced distribution of MSAs across N− and N+ can be seen for the Plains, South West and Rocky Mountains regions, with the latter two also having a proportionately larger number of MSAs with no connections at all. 

To estimate ψ<sup>+</sup> i0<sup>andψ−</sup> i0<sup>,fori=1, 2, ..., N,weusetheconcentratedlog-likelihood</sup> function (18), in which x�i is replaced by<sup>ˆ�</sup> ξi, and Zi is augmented by a T × 1 vector of ones, τ T . The intercepts, aiξ, and the parameters of the lagged values, λi1, ψ<sup>+</sup> i1<sup>and</sup> 

23 

ψ<sup>−</sup> i1<sup>canbeestimatedvialeastsquaresappliedtotheequationsforindividualMSAs</sup> conditional on the ML estimates of ψ<sup>+</sup> i0<sup>and ψ−</sup> i0<sup>,for i = 1, 2, ...., N.We also note that for</sup> the N0 units with no connections, we set ψ<sup>+</sup> i0<sup>=ψ−</sup> i0<sup>=ψ+</sup> i1<sup>=ψ−</sup> i1<sup>=0,andestimatethe</sup> remaining parameters, intercepts and λi1 by least squares. For MSAs with only negative or positive connections we impose the restriction that the corresponding ψ<sup>+</sup> i0<sup>,ψ+</sup> i1<sup>,ψ−</sup> i1<sup>,</sup> and ψ<sup>−</sup> i0<sup>coefficientsaresettozero.Thisrestrictionisneededforidentificationpurposes</sup> due to the simultaneity problem that arises in this case. Clearly these coefficients can be set to other values as well, such as the average of each coefficient within the region they belong to or even to the national average of each coefficient. For the purpose of inference, the variance-covariance matrix of the estimates is computed as in (19), again using the full log-likelihood with respect to the vector of parameters ′ ′ θ = (θ<sup>′</sup> 1<sup>, θ′</sup> 2<sup>, ..., θ′</sup> N<sup>)</sup> , where θi = �ψ<sup>+</sup> i0<sup>, ψ</sup> i<sup>−</sup> 0<sup>, ψ</sup> i<sup>+</sup> 1<sup>, ψ−</sup> i1<sup>, αiξ, λi1, σ2</sup> ς i� . For further details, see Aquaro, Bailey and Pesaran (2014). QML estimates for individual MSAs are available on request. In what follows we give median and mean estimates, and the proportion of MSAs with statistically significant parameters (at the 5% level). The results are summarized in Table 7, and give the median and the mean group (MG) estimates of λ<sup>ˆ</sup> i1, ψ<sup>ˆ</sup> +i0<sup>, ˆψ</sup> −i0<sup>, ˆψ</sup> +i1<sup>, ˆψ</sup> −i1<sup>andσˆς</sup> i<sup>.The standard errors</sup> of the MG estimates are given in parenthesis.<sup>15</sup> 

A number of general conclusions readily emerge from an examination of the results in Table 7. The mean and median estimates are very close suggesting that the estimates across the MSAs are approximately symmetrically distributed. All the mean estimates are + statistically significant at the 5% level, with the mean lagged spatial effects (ψ<sup>ˆ</sup> 1,MGE<sup>and</sup> ˆ − ψ1,MGE<sup>)beinglesspreciselyestimatedascomparedtotheothermeaneffects,namely</sup> λˆ1,MGE, ψˆ +0,MGE<sup>andψˆ</sup> −0,MGE<sup>.Thesizeofthemeantemporaleffect,λˆ1,MGE,at0.392</sup> (0.009) is reasonably large considering that de-factoring is likely to have removed some of the common dynamics in house price changes. With regard to the cross section dynamics, contemporaneous positive spill-over effects have a larger magnitude than their equivalent negative effects with the MG estimates of ψ<sup>+</sup> i0<sup>and ψ−</sup> i0<sup>given byψˆ</sup> +0,MGE<sup>= 0.345 (0.017) and</sup> ˆ − ψ0,MGE<sup>= −0.2763 (0.021) , respectively.The estimates in both cases are correctly signed</sup> and clearly reject the hypothesis that Ψ<sup>+</sup> j<sup>=Ψ−</sup> j<sup>,forj=0(andforj=1asdiscussed</sup> below). Also, the MG estimates of the lagged spatial effects, ψ<sup>ˆ</sup> +1,MGE<sup>=−0.040(0.015)</sup> and ψ<sup>ˆ</sup> −1,MGE<sup>=0.071(0.016),areoppositeinsigntotherespectivecontemporaneous</sup> effects, suggesting a certain degree of reversal of the effects. We also note that the mean spatial effects of positive connections at 0.345 is somewhat higher than the mean effects of negative connections at 0.276 (in absolute terms). 

With regard to the statistical significance of the estimates for individual MSAs (abstracting from multiple testing issues) we note that λ<sup>ˆ</sup> i1 is statistically significant in 90% of the MSAs, whilst the contemporaneous spatial effects is significant in 65% of MSAs with positive connections, and significant in 62% of MSAs with negative connections. In 

> 15The MG estimator is defined as the simple average of the estimates across the MSAs with nonzero coefficients. For example, the MGE of E �ψ<sup>+</sup> i0� = ψ<sup>+</sup> 0<sup>,isgivenbyψˆ</sup> +0,MGE<sup>=(1/N ∗</sup> +<sup>) �</sup> i<sup>N</sup> =1+<sup>∗ψˆ</sup> +i0<sup>,</sup> + where N+<sup>∗denotesthenumberofMSAswithpositiveconnections(N ∗</sup> +<sup>=N</sup> +/−<sup>+ N+),andψˆ</sup> i0<sup>isthe</sup> 

> + ˆ + QMLE of ψ<sup>+</sup> i0<sup>.Thenon-parametricestimatorofthevarianceofψˆ</sup> 0,MGE<sup>isgivenby:</sup> V ar<sup>�</sup> �ψ0,MGE� = 

> <u>1</u> N+<sup>∗</sup> ˆ + + 2 N+<sup>∗(N</sup> +<sup>∗−1)</sup> �i=1 �ψi0<sup>−ψˆ</sup> 0,MGE� . For more details see Pesaran and Smith (1995). 

24 

contrast, the lagged spatial effects turned out to be much weaker, with only 28 present of positive connections and 26% of negative connections being statistically significant. Overall, the estimates suggest there exists a reasonably rich temporal and cross-sectional dependence in US house price changes even after stripping them of strong, pervasive national and regional factors. 

Table 7: Quasi-ML estimates of spatio-temporal model (25) Applied to de-factored house price changes given by (21) 

||λ1|ψ<sup>+</sup><br>0|ψ<sup>−</sup><br>0|ψ<sup>+</sup><br>1|ψ<sup>−</sup><br>1|σζ|
|---|---|---|---|---|---|---|
||C|omputed o|ver non-zer|o parameter|coefcient|s|
|Median|0.3986|0.3124|-0.2493|-0.0430|0.0608|1.2416|
|Mean Group Estimates|0.3921|0.3454|-0.2763|-0.0398|0.0706|1.3056|
||(0.0086)|(0.0168)|(0.0209)|(0.0147)|(0.0156)|(0.0181)|
|% signifcant (at 5% level)|89.8%|64.8%|61.9%|28.1%|26.4%|-|
|Number of non-zero coef.|363|253|197|253|197|363|



> 1Restricted parameter coefficients are set to zero. ψˆ +i0<sup>=0andψˆ</sup> +i1<sup>=0ifMSAihasnopositiveconnections;</sup> ˆ − − + + − − ψi0<sup>=0andψˆ</sup> i1<sup>=0ifMSAihasnonegativeconnections;ψˆ</sup> i0<sup>=0,ψˆ</sup> i1<sup>=0,ψˆ</sup> i0<sup>=0andψˆ</sup> i1<sup>=0ifMSAi</sup> has no positive or negative connections, for i = 1, 2, ..., 363. 

> 2MGE standard errors are in brackets. 

To give an idea of the extent of parameter heterogeneity across MSAs, in Table 8 we provide median and mean estimates by regions. Interestingly enough the regional differences are not very pronounced, particularly if we focus on the more precisely estimated parameters. The regional estimates of λ1 range from the low value of 0.316 (0.021) for the Great Lakes to a high value of 0.458 (0.025) for the Rocky Mountains. The regional differences in the mean estimates of ψ<sup>+</sup> 0<sup>areevenslightlylowerandrangefrom0.264</sup> (0.082) in the South West to 0.374 (0.042) for the Plains. In contrast, the estimates of the negative connections, ψ<sup>−</sup> 0<sup>arelesspreciselyestimatedandrangefrom−0.078(0.099)</sup> for New England to −0.370 (0.053) in the South West. But one should consider such comparisons with care since in the case of some regions the number of non-zero estimates was quite small. Nevertheless, one of our main conclusions that positive and negative connections have opposite effects seems to be robust to the regional disaggregation. The estimates of ψ<sup>+</sup> 0<sup>andψ−</sup> 0<sup>arerespectivelypositiveandnegativeacrossallregions.The</sup> results in Table 8 also support our conclusion that lagged spatial effects are generally not that important and tend to be statistically insignificant in a number of regions. But once again we need to bear in mind that some of the regional estimates are based on a rather small number of non-zero estimates. 

Finally, to assess the importance of de-factoring of house price changes we also estimated the connection matrices W<sup>ˆ+</sup> and W<sup>ˆ−</sup> without de-factoring, using the hierarchical factor model (20). Not surprisingly we found W<sup>ˆ+</sup> to be much denser as compared to the estimates obtained based on de-factored price changes, and W<sup>ˆ−</sup> to be less dense. The many more connections that we are finding when using price changes without de-factoring reflect the presence of common factors rather than genuine spatial effects. In line with this result we also find an estimate of spatial effects, ψ<sup>+</sup> 0<sup>,whichisveryclosetounity</sup> when we use a estimated W<sup>ˆ+</sup> based on non-defactored price changes. Details of these results are available upon request. 

25 

Table 8: Quasi-ML estimates of spatio-temporal model (25) summarised by region Applied to de-factored house price changes given by (21) 

||C|omputed o<br>|ver non-zer|o paramete<br>|r coefcient|s|
|---|---|---|---|---|---|---|
||λ1|ψ<sup>+</sup><br>0|ψ<sup>−</sup><br>0|ψ<sup>+</sup><br>1|ψ<sup>−</sup><br>1|σζ|
||||New E|ngland|||
|Median|0.4064|0.2762|-0.0843|-0.0514|0.0209|1.1684|
|Mean Group Estimates|0.3944|0.3563|-0.0781|-0.0050|-0.0412|1.2704|
|% signifcant (5% level)|(0.0303)<br>86.7%|(0.0996)<br>60.0%|(0.0991)<br>50.0%|(0.0430)<br>0.0%|(0.0784)<br>30.0%|(0.0966)<br>-|
|Number of non-zero coef.|15|10|10|10|10|10|
||||Mid|East|||
|Median|0.4278|0.3439|-0.1904|-0.0096|0.0625|1.3977|
|Mean Group Estimates|0.3990|0.3603|-0.1938|-0.0755|0.1129|1.4368|
||(0.0319)|(0.0465)|(0.1163)|(0.0487)|(0.0747)|(0.0634)|
|% signifcant (5% level)|91.7%|65.4%|68.4%|30.8%|26.3%|-|
|Number of non-zero coef.|36|26|19|26|19|36|
||||South|East|||
|Median|0.4013|0.3242|-0.2686|-0.0538|0.0847|1.2384|
|Mean Group Estimates|0.4001<br>(0.0162)|0.3563<br>(0.0262)|-0.3062<br>(0.0326)|-0.0596<br>(0.0234)|0.0977<br>(0.0242)|1.3469<br>(0.0427)|
|% signifcant (5% level)|90.4%|64.8%|61.6%|27.3%|31.5%|-|
|Number of non-zero coef.|114|88|73|88|73|114|
||||Great|Lakes|||
|Median|0.3176|0.2660|-0.2227|0.0149|0.0361|1.2492|
|Mean Group Estimates|0.3160<br>(0.0209)|0.3304<br>(0.0463)|-0.2846<br>(0.0383)|0.0229<br>(0.0435)|0.0407<br>(0.0351)|1.3142<br>(0.0392)|
|% signifcant (5% level)|78.7%|63.4%|50.0%|31.7%|13.9%|-|
|Number of non-zero coef.|61|41|36|41|36|61|
||||Pla|ins|||
|Median|0.3808|0.3015|-0.2491|-0.1573|0.0597|1.1128|
|Mean Group Estimates|0.3751|0.3744|-0.2409|-0.1280|0.0825|1.1254|
||(0.0243)|(0.0427)|(0.0540)|(0.0290)|(0.0421)|(0.0324)|
|% signifcant (5% level)|93.8%|75.0%|57.1%|29.2%|28.6%|-|
|Number of non-zero coef.|32|24|21|24|21|32|
||||South|West|||
|Median|0.3935|0.2944|-0.3053|-0.1023|0.0077|1.2877|
|Mean Group Estimates|0.4024<br>|0.2642<br>|-0.3695<br>|-0.0576<br>|0.0377<br>|1.3385<br>|
||(0.0209)|(0.0823)|(0.0525)|(0.0630)|(0.0560)|(0.0301)|
|% signifcant (5% level)|94.7%|57.1%|82.4%|38.1%|23.5%|-|
|Number of non-zero coef.|38|21|17|21|17|38|
||||Rocky M|ountains|||
|Median|0.4435|0.3486|-0.2756|0.0155|0.1396|1.1618|
|Mean Group Estimates|0.4581|0.3177|-0.3086|0.0083|0.1033|1.2096|
||(0.0253)|(0.0667)|(0.0542)|(0.0430)|(0.0557)|(0.0409)|
|% signifcant (5% level)|100.0%|70.0%|80.0%|10.0%|40.0%|-|
|Numberofnon-zerocoef.|22|10|10|10|10|22|
||||Far|West|||
|Median|0.4672|0.3667|-0.2438|0.0330|0.0480|1.2158|
|Mean Group Estimates|0.4400|0.3591|-0.2673|0.0137|0.0155|1.2437|
||(0.0237)|(0.0488)|(0.0898)|(0.0428)|(0.0293)|(0.0336)|
|%signifcant(5%level)|91.1%|63.6%|63.6%|30.3%|18.2%|-|
|<br>Number of non-zero coef.|45|33|11|33|11|45|



> 1Restricted parameter coefficients are set to zero. ψˆ +i0<sup>= 0andψˆ</sup> +i1<sup>= 0ifMSAihasnopositive</sup> connections; ψ<sup>ˆ</sup> −i0<sup>=0andψˆ</sup> −i1<sup>=0ifMSAihasnonegativeconnections;ψˆ</sup> +i0<sup>=0,ψˆ</sup> +i1<sup>=0,</sup> ψˆ −i0<sup>= 0andψˆ</sup> −i1<sup>= 0ifMSAihasnopositiveornegativeconnections,fori = 1, 2, ..., 363.</sup> 

> 2MGE standard errors are in brackets below their respective Mean Group Estimates. 

26 

## 5 Conclusions 

An understanding of the spatial dimension of economic and social activity requires methods that can separate out the relationship between spatial units that is due to the effect of common factors from that which is purely spatial. We are able to distinguish between cross-sectional strong dependence and weak or spatial dependence. Strong dependence in turn suggests that there are common factors. We have proposed the use of cross unit averages to extract common factors and contrast this to a principal components approach widely used in the literature. We then use multiple testing to determine significant bilateral correlations (signifying connections) between spatial units and compare this to an approach that just uses distance to determine units that are neighbours. In a very data rich environment with observations on many spatial units over long periods of time a way of filtering the data to uncover spatial connections is crucial. We have applied these methods to real house price changes in the US at the level of the Metropolitan Statistical Area. Although there is considerable overlap between neighbours determined by distance and those by multiple testing, there is also considerable correlation between MSAs across the United States that suggests that other forces are at work. 

We also find that our analysis of connections based on pair-wise correlations of defactored house price changes clearly points to the existence of negative as well as positive connections. This feature is absent if we base the spatial analysis exclusively on contiguity. It is common in the literature to think of spatial relationships as involving spillover from one area to another with the (implicit) assumption that the spillover effects are positive. But this need not be the case. Migration across space could raise/lower wages or house prices in one locality and lower/raise them into another locality. 

Furthermore, we verify that basing the spatial analysis on house price changes without de-factoring ignores the possibility that there may be common national and regional factors and failing to condition on the common factors may bias the inferences that can be drawn. Our analysis strips out such common effects and allows us to focus on estimation of spillover effects (positive or negative) which is of primary interest in spatial analysis. Although proximity measured by distance is a useful metric for constructing the weights matrix, our analysis suggests that correlation analysis, once applied to defactored price changes with appropriate application of multiple testing techniques can lead to important new insights as to the nature of spatial connections. 

## Appendices 

### Appendix I: Data sources 

Monthly data for US house prices from January 1975 to December 2010 are taken from Freddie Mac. These data are available at: 

http://www.freddiemac.com/finance/fmhpi 

The quarterly figures are arithmetic averages of monthly figures. 

Annual CPI data at State level are obtained from the Bureau of Labor Statistics: 

http://www.bls.gov/cpi/ 

The quarterly figures are interpolated using the interpolation technique described in the appendix of GVAR toolbox 1.1 user guide. 

27 

The annual population data at MSA level are obtained from the Regional Economic Information System, Bureau of Economic Analysis, U.S. Department of Commerce: http://www.bea.gov/regional/docs/footnotes.cfm?tablename=CA1-3 

### Appendix II: Geographical classification of the United States 

Table A provides the geographical breakdown of the eight regions used in our analysis of US house price changes which is based on the Bureau of Economic Analysis classification (http://www.bea.gov/regional/docs/regions.cfm). Each region covers an average of 6 States, each of which contains 45 Metropolitan Statistical Areas on average. The classifications are shown in Table A together with the number of MSAs included in each State. Details of the MSAs by region are available upon request. 

### Appendix III: Calculation of distance 

The original data used were Latitude-Longitude of zip codes, cross referenced with each of the 366 Metropolitan Statistical Areas (MSAs). Any missing Latitude-Longitude coordinates were coded manually from Google searches. The geodesic distance between a pair of latitude/longitude coordinates was then calculated using the Haversine formula: 



where R is the radius of the earth in miles and d is the distance. ∆lat = lat2 − lat1, and ∆long = long2 − long1. 

28 

Table A: Geographical Classification of Regions, States and MSAs in the United States 

|Regions|States|No of MSAs|Regions|States|No of MSAs|Regions|States|No of MSAs|
|---|---|---|---|---|---|---|---|---|
|New England|Connecticut (CT)|4|Great Lakes|Illinois (IL)|9|South West|Arizona (AZ)|6|
||Maine (ME)|3||Indiana (IN)|13||New Mexico (NM)|4|
||Massachussetts (MA)|5||Michigan (MI)|14||Oklahoma (OK)|3|
||New Hampshire (NH)|1||Ohio (OH)|13||Texas (TX)|25|
||Rhode Island (RI)<br>Vermont (VT)|1<br>1||Wisconsin (WI)|12||||
|Mid-East|Delaware (DE)<br>|1|Plains|Iowa (IA)<br>|8|Rocky Mountains|Colorado (CO)<br>|7|
||District of Columbia (DC)|1||Kansas (KS)|4||Idaho (ID)|5|
||Maryland (MD)|4||Minnesota (MN)|5||Montana (MT)|3|
||New Jersey (NJ)|4||Missouri (MO)|8||Utah (UT)|5|
||New York (NY)|12||Nebraska (NE)|2||Wyoming (WY)|2|
||Pennsylvania (PA)|14||North Dakota (ND)|3||||
|||||South Dakota (SD)|2||||
|South East|Alabama (AL)|11||||Far West|California (CA)|26|
||Arkansas (AR)|6|||||Nevada (NV)|3|
||Florida (FL)<br>|20|||||Oregon (OR)<br>|6|
||Georgia (GA)|14|||||Washington (WA)|10|
||Kentucky (KY)|5|||||||
||Louisiana (LA)|8|||||||
||Mississippi (MS)|4|||||||
||North Carolina (NC)|14|||||||
||South Carolina (SC)|8|||||||
||Tennessee (TN)|10|||||||
||Virginia (VA)|9|||||||
||West Virginia (WV)|5|||||||



This geographical classification of the United States follows the Bureau of Economic Analysis specifications. 

## References 

- [1] Anselin, L. (1988). Spatial Econometrics: Methods and Models. Boston: Kluwer Academic Publishers. 

- [2] Anselin, L. (2001). Spatial Econometrics. In B. H. Baltagi (Ed.), A Companion to Theoretical Econometrics. Blackwell, Oxford. 

- [3] Aquaro, M., Bailey, N. and Pesaran, M. H. (2014). Quasi-Maximum Likelihood Estimation of Spatial Models with Heterogenous Coefficients. Under preparation. 

- [4] Bai, J. (2003). Inferential Theory for Factor Models of Large Dimensions. Econometrica, 71, 1, 135—171. 

- [5] Bai, J. and Ando, (2014). Panel Data Models with Grouped Factor Structure under Unknown Group Membership. MPRA Paper No. 52782, January 2014 05:46 UTC. 

- [6] Bai, J. and Ng, S. (2002). Determining the Number of Factors in Approximate Factor Models. Econometrica, 70, 191—221. 

- [7] Bailey, N., Kapetanios, G. and Pesaran, H. M. (2014). Exponent of Cross-Sectional Dependence: Estimation and Inference. Jan 2012, revised Apr 2014. Cambridge Working Paper 1206. 

- [8] Bailey, N., Pesaran, H. M. and Smith, L.V. (2014). A Multiple Testing Approach to the Regularisation of Sample Correlation Matrices. CESifo Working Paper no. 4834. 

- [9] Barigozzi, M. and Brownlees, C. (2013). NETS: Network Estimation for Time Series. SSRN Working Paper. Available at SSRN: http://ssrn.com/abstract=2249909 or http://dx.doi.org/10.2139/ssrn.2249909. 

- [10] Bester, C. A., Conley, T. G. and Hansen, C. B. (2011). Inference with Dependent Data Using Cluster Covariance Estimators. Journal of Econometrics, 165, 2, 137— 151. 

- [11] Bhattachajee, A. and Holly, S. (2013). Understanding Interactions in Social Networks and Committees. Spatial Economic Analysis, 8, 1, 23—53. 

- [12] Bien, J. and Tibshirani, R. J. (2011). Sparse Estimation of the Covariance Matrix. Biometrika, 98, 4, 807—820. 

- [13] Bonferroni, C. (1935). Il Calcolo delle Assicurazioni su Gruppi di Teste. Studi in Onore del Professore Salvatore Ortu Carboni, Rome, Italy, 13—60. 

- [14] Bonferroni, C. (1936). Teoria Statistica delle Classi e Calcolo delle Probabilità. Pubblicazioni del R Istituto Superiore di Scienze Economiche e Commerciali di Firenze, 8, 3—62. 

- [15] Butte, A. J., Tamayo, P., Slonim, D., Golub, T. R. and Kohane, I. S. (2000). Discovering Functional Relationships between RNA Expression and Chemotherapeutic Susceptibility using Relevance Networks. Proceedings of the National Academy of Sciences of the U.S.A., 97, 12182—12186. 

30 

- [16] Carlino, G. A. and DeFina, R. H. (1998). The Differential Regional Effects of Monetary Policy. Review of Economics and Statistics, 80, 4, 572—587. 

- [17] Carlino, G. A. and DeFina, R. H. (2004). How Strong Is Co-movement in Employment over the Business Cycle? Evidence from State/Sector Data. Journal of Urban Economics, 55, 2, 298—315. 

- [18] Carlino, G. and Sill, K. (2001). Regional Income Fluctuations: Common Trends and Common Cycles. Review of Economics and Statistics, 83, 3, 446—456. 

- [19] Chamberlain, G. and Rothschild, M. (1983). Arbitrage, Factor Structure and MeanVariance Analysis in Large Asset Markets. Econometrica, 51, 1305—1324. 

- [20] Chaudhuri, S., Drton, M. and Richardson, T. S. (2007). Estimation of a Covariance Matrix with Zeros. Biometrika, 94, 199—216. 

- [21] Chudik, A., Pesaran, M. H. and Tosetti, E. (2011). Weak and Strong Cross Section Dependence and Estimation of Large Panels. The Econometrics Journal, 14, C45— C90. 

- [22] Chudik, A. and Pesaran, M. H. (2014). Large Panel Data Models with CrossSectional Dependence: A Survey. Center for Applied Financial Economics (CAFE) Research Paper no. 13.15. In B. H. Baltagi (Ed.), forthcoming in The Oxford Handbook on Panel Data. Oxford University Press. 

- [23] Conley, T. G. (1999). GMM Estimation with Cross-Sectional Dependence. Journal of Econometrics, 92, 1—45. 

- [24] Conley, T. G. and Dupor, B. (2003). A Spatial Analysis of Sectoral Complementarity. Journal of Political Economy, 111, 311—352. 

- [25] Conley, T. G. and Topa, G. (2003). Identification of Local Interaction Models with Imperfect Location Data. Journal of Applied Econometrics, 18, 605—618. 

- [26] Connor, G. and Korajczyk, R. (1993). A Test for the Number of Factors in an Approximate Factor Model. The Journal of Finance, XLVIII, 4, 1263—1291. 

- [27] Corrado, L. and Fingleton, B. (2012). Where is the Economics in Spatial Econometrics? Journal of Regional Science, 52, 210—239. 

- [28] Cromwell B. (1992). Does California Drive the West? An Econometric Investigation of Regional Spillovers. Economic Review of the Federal Reserve Bank of San Francisco, 2, 13—23. 

- [29] Dees, S., di Mauro, F., Pesaran, M. H. and Smith, L. V. (2007). Exploring the International Linkages of the Euro Area: A Global VAR Analysis. Journal of Applied Econometrics, 22, 1—38. 

- [30] Del Negro, M. (2002). Asymmetric Shocks Among U.S. States. Journal of International Economics, 56, 2, 273—297. 

- [31] Dempster, A. P. (1972). Covariance Selection. Biometrics, 28, 157—175. 

31 

- [32] Efron, B. (2010). Large-Scale Inference: Empirical Bayes Methods for Estimation, Testing and Prediction, Cambridge. 

- [33] Forni, M., Hallin, M., Lippi, M., and Reichlin, L. (2000). The Generalised Dynamic Factor Model: Identification and Estimation. Review of Economics and Statistics, 82, 540—554. 

- [34] Forni, M. and Lippi, M. (2001). The Generalised Dynamic Factor Model: Representation Theory. Econometric Theory, 17, 1113—1141. 

- [35] Forni, M. and Reichlin, L. (1998). Let’s Get Real: A Factor Analytical Approach to Disaggregated Business Cycle Dynamics. Review of Economic Studies, 65, 453—473. 

- [36] Glaeser, E. L. and Gottlieb, J. D. (2009). The Wealth of Cities: Agglomeration Economies and Spatial Equilibrium in the United States. Journal of Economic Literature, 47, 983—1028. 

- [37] Glaeser, E. L., Gyourko, J. and Saiz, A. (2008). Housing Supply and Housing Bubbles. Journal of Urban Economics, 64, 2, 198—217. 

- [38] Gupta, R. and Das, S. (2010). Predicting Downturns in the US Housing Market. Journal of Real Estate Economics and Finance, 41, 3, 294—319. 

- [39] Gupta, R., Kabundi, A. and Miller, S. M. (2011a). Using Large Data Sets to Forecast Housing Prices: A Case Study of Twenty US States. Journal of Housing Research, 20, 2, 161—190. 

- [40] Gupta, R., Kabundi, A. and Miller, S. M. (2011b). Forecasting the US Real House Price Index: Structural and Non-structural Models with and without Fundamentals. Economic Modelling, 28, 4, 2013—2021. 

- [41] Gupta R. and Miller, S. M. (2012). The Time Series Properties on Housing Prices: A Case Study of the Southern California Market. Journal of Real Estate Finance and Economics, 44, 3, 2012. 

- [42] Hochberg, Y. (1988). A Sharper Bonferroni Procedure for Multiple Tests of Significance. Biometrika, 75, 800—802. 

- [43] Holly, S., Pesaran, H. M. and Yamagata, T. (2011a). A Spatio-Temporal Model of House Prices in the US. Journal of Econometrics, 158, 160—173. 

- [44] Holly, S., Pesaran, H. M. and Yamagata, T. (2011b). The Spatial and Temporal Diffusion of House Prices in the UK. Journal of Urban Economics, 69, 1, 2—23. 

- [45] Holly, S. and Petrella, I. (2012). Factor Demand Linkages, Technology Shocks and the Business Cycle. Review of Economics and Statistics, 94, 4, 948—963. 

- [46] Holm, S. (1979). A Simple Sequentially Rejective Multiple Test Procedure. Scandinavian Journal of Statistics, 6, 2, 65—70. 

- [47] Hommel, G. (1988). A Stagewise Rejective Multiple Test Procedure Based on a Modified Bonferroni test. Biometrika, 75, 383—386. 

32 

- [48] Hommel, G. (1989). A Comparison of Two Modified Bonferroni procedures. Biometrika, 76, 624—625. 

- [49] Hotelling, H. (1933). Analysis of a Complex of Statistical Variables with Principal Components. Journal of Educational Psychology, 24, 6, 417—441. 

- [50] Hsiao, C. and Pesaran, M. H. (2008). Random Coefficient Models. Chapter 6 in L. Matyas and Sevestre (eds.), The Econometrics of Panel Data, Springer-Verlag, Berlin, 185—213. 

- [51] Kadiyala, K.R. and Bhattacharya, R. (2009). Regional Housing Prices in the USA: An Empirical Investigation of Nonlinearity. The Journal of Real Estate Finance and Economics, 38, 4, 443—460. 

- [52] Kapetanios, G. and Pesaran, M. H. (2007). Alternative Approaches to Estimation and Inference in Large Multifactor Panels: Small Sample Results with an Application to Modelling of Asset Return. In Garry Phillips and Elias Tzavalis (eds.), The Refinement of Econometric Estimation and Test Procedures: Finite Sample and Asymptotic Analysis, Cambridge University Press, Cambridge. 

- [53] Kapoor, M., Kelejian, H. H. and Prucha, I. R. (2007). Panel Data Models with Spatially Correlated Error Components. Journal of Econometrics, 140, 97—130. 

- [54] Khare, K. and Rajaratnam, B. (2011). Wishart Distributions for Decomposable Covariance Graph Models. Annals of Statistics, 30, 514—555. 

- [55] Kelejian, H. H. and Prucha, I. R. (1999). A Generalized Moments Estimator for the Autoregressive Parameter in a Spatial Model. International Economic Review, 40, 509—533. 

- [56] Kelejian, H. H. and Prucha, I. R. (2007). HAC Estimation in a Spatial Framework. Journal of Econometrics, 140, 131—154. 

- [57] Kelejian, H. H. and Prucha, I. R. (2010). Specification and Estimation of Spatial Autoregressive Models with Autoregressive and Heteroskedastic Disturbances. Journal of Econometrics, 157, 53—67. 

- [58] Krugman, P. R. (1991). Increasing Returns and Economic Geography. Journal of Political Economy, 99, 483—499. 

- [59] Kuethe, T. and Pede, V. (2011). Regional Housing Price Cycles: A Spatio-Temporal Analysis Using US State-Level Data. Regional Studies, 45, 5, 563—574. 

- [60] Lee, L.-F. (2002). Consistency and Efficiency of Least Squares Estimation for Mixed Regressive, Spatial Autoregressive Models. Econometric Theory, 18, 2, 252—277. 

- [61] Lee, L.-F. (2004). Asymptotic Distributions of Quasi-Maximum Likelihood Estimators for Spatial Autoregressive Models. Econometrica, 72, 6, 1899—1925. 

- [62] Lee, L.-F. and Yu, J. (2010). Estimation of Spatial Autoregressive Panel Data Models with Fixed Effects. Journal of Econometrics, 154, 165—185. 

33 

- [63] LeSage, J. and Pace R. K. (2010). Introduction to Spatial Econometrics, Chapman & Hall/CRC, Boca Raton, Florida. 

- [64] Lin, X. and Lee, L.-F. (2010). GMM Estimation of Spatial Autoregressive Models with Unknown Heteroskedasticity. Journal of Econometrics, 157, 1, 34—52. 

- [65] Meinshausen, N. and Buhlmann, P. (2006). High-Dimensional Graphs and Variable Selection with the Lasso. Annals of Statistics, 34, 3, 1436—1462. 

- [66] Owyang, M. T., Piger, J. and Wall, H. J. (2005). Business Cycle Phases in U.S. States. Review of Economics and Statistics, 87, 4, 604—616. 

- [67] Partridge, M. D. and Rickman, D. S. (2005). Regional Cyclical Asymmetries in an Optimal Currency Area: An Analysis Using US State Data. Oxford Economic Papers, July, 57, 3, 373—397. 

- [68] Pearson, K. (1900). On the Criterion that a Given System of Deviations from the Probable in the Case of a Correlated System of Variables is Such That It Can Be Reasonably Supposed to Have Arisen from Random Sampling. Philosophical Magazine Series, 5, 50 (302), 157—175. 

- [69] Peng, J., Wang, W., Zhou, N. and Zhu, J. (2009). Partial Correlation Estimation by Joint Sparse Regression Models. Journal of the American Statistical Association, June, 104, 486, 735—746. 

- [70] Pesaran, M. H. (2004). General Diagnostic Tests for Cross Section Dependence in Panels. CESifo Working Paper Series No. 1229. Available at SSRN: http://ssrn.com/abstract=572504. 

- [71] Pesaran, M. H. (2006). Estimation and Inference in Large Heterogeneous Panels with a Multifactor Error Structure. Econometrica, 74, 4, 967—1012. 

- [72] Pesaran, M. H. (2014). Testing Weak Cross-Sectional Dependence in Large Panels. Forthcoming in Econometric Reviews. 

- [73] Pesaran, M. H., Schuermann, T. and Weiner, S. M. (2004). Modeling Regional Interdependencies using a Global Error-Correcting Macroeconomic Model. Journal of Business and Economics Statistics, 22, 2, 129—162. 

- [74] Pesaran, M. H. and Smith, R. P. (1995). Estimating Long-Run Relationships from Dynamic Heterogeneous Panels. Journal of Econometrics, 68, 79—113. 

- [75] Pesaran, M. H. and Timmermann, A. (2009). Testing Dependence Among Serially Correlated Multicategory Variables. Journal of American Statistical Association, 104, 485, 325—337. 

- [76] Pollakowski H. O. and Ray T. S. (1997). Housing Price Diffusion Patterns at Different Aggregation Levels: An Examination of Housing Market Efficiency. Journal of Housing Research, 8, 1, 107—124. 

- [77] Rapach, D. E. and Strauss, J. K. (2007). Forecasting Real Housing Price Growth in the Eighth District States. Federal Reserve Bank of St. Louis. Regional Economic Development, 3, 2, 33—42. 

34 

- [78] Rapach, D. E. and Strauss, J. K. (2009). Differences in Housing Price Forecast Ability Across U.S. States. International Journal of Forecasting, 25, 2, 351—372. 

- [79] Rothman, A. J., Bickel, P. J., Levina, E. and Zhu, J. (2008). Sparse Permutation Invariant Covariance Estimation. Electronic Journal of Statistics, 2, 494—515. 

- [80] Rothman, A. J., Bickel, P. J., Levina, E. and Zhu, J. (2010). Sparse Multivariate Regression with Covariance Estimation. Journal of Computational and Graphical Statistics, 19, 4, 947—962. 

- [81] Stock, J. H. and Watson, M. W. (1998). Diffusion Indexes. NBER Working Papers 6702, National Bureau of Economic Research, Inc. 

- [82] Stock, J. H. and Watson, M. W. (2002a). Forecasting Using Principal Components from a Large Number of Predictors. Journal of the American Statistical Association, 97, 460, 147—162. 

- [83] Stock, J. H. and Watson, M. W. (2002b). Macroeconomics Forecasting Using Diffusion Indexes. Journal of Business and Economic Statistics, 20, 2, 147—162. 

- [84] Stone, R. (1947). On the Interdependence of Blocks of Transactions. Journal of the Royal Statistical Society (Supplement), 9, 1, 1—45. 

- [85] Whittle, P. (1954). On Stationary Processes on the Plane. Biometrika, 41, 434—449. 

- [86] Yu, J., de Jong, R. M. and Lee, L.-F. (2008). Quasi-Maximum Likelihood Estimators for Spatial Dynamic Panel Data with Fixed Effects when both N and T are Large. Journal of Econometrics, 146, 1, 118—134. 

35 

