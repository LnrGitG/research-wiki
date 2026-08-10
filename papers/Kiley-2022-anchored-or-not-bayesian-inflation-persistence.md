---
title: "Anchored or Not: How Much Information Does 21st Century Data Contain on Inflation Dynamics?"
authors: Michael T. Kiley
year: 2022
doi: 10.17016/FEDS.2022.016
publisher: Federal Reserve Board, FEDS Working Paper
url: https://www.federalreserve.gov/econres/feds/anchored-or-not-how-much-information-does-21st-century-data-contain-on-inflation-dynamics.htm
type: paper
tags: ['inflation', 'bayesian', 'persistence', 'phillips-curve', 'monetary-policy', 'FED', 'FEDS-notes']
---

# Anchored or Not: How Much Information Does 21st Century Data Contain on Inflation Dynamics?

**Авторы:** Michael T. Kiley
**Год:** 2022
**DOI:** 10.17016/FEDS.2022.016
**Источник:** Federal Reserve Board, FEDS Working Paper
**URL:** https://www.federalreserve.gov/econres/feds/anchored-or-not-how-much-information-does-21st-century-data-contain-on-inflation-dynamics.htm
**PDF:** `raw/papers/kiley_2022_anchored.pdf`

## Аннотация (EN)

Inflation was low and stable in the United States during the first two decades of the 21st century and broke out of its stable range in 2021. Experience in the early 21st century differed from that of the second half of the 20th century, when inflation showed persistent movements including the "Great Inflation" of the 1970s. This analysis examines the extent to which the experience from 2000-2019 should lead a Bayesian decisionmaker to update their assessment of inflation dynamics. Given a prior for inflation dynamics consistent with 1960-1999 data, a Bayesian decisionmaker would not update their view of inflation persistence in light of 2000-2019 data unless they placed very low weight on their prior information. In other words, 21st century data contains very little information to dissuade a Bayesian decisionmaker of the view that inflation fluctuations are persistent, or "unanchored". The intuition for, and implications of, this finding are discussed.

## Аннотация (RU)

Инфляция в США была низкой и стабильной в первые два десятилетия XXI века и вышла за пределы своего стабильного диапазона в 2021 г. Опыт начала XXI века отличается от второй половины XX века, когда инфляция демонстрировала устойчивые движения, включая «Великую инфляцию» 1970-х гг. Данный анализ исследует, в какой степени опыт 2000–2019 гг. должен побудить байесовского решающее лицо обновить свою оценку динамики инфляции. При априорном распределении, согласованном с данными 1960–1999 гг., байесовский решающий субъект не обновил бы своё представление о персистентности инфляции с учётом данных 2000–2019 гг., если только он не придавал бы очень низкий вес своей априорной информации. Иными словами, данные XXI века содержат очень мало информации, чтобы разубедить байесовского решающего субъекта в том, что колебания инфляции являются персистентными, или «неанкерированными».

## Полный текст

Finance and Economics Discussion Series
Federal Reserve Board, Washington, D.C.
ISSN 1936-2854 (Print)
ISSN 2767-3898 (Online)
Anchored or Not: How Much Information Does 21st Century
Data Contain on Inﬂation Dynamics?
Michael T. Kiley
2022-016
Please cite this paper as:
Kiley, Michael T. (2022).
“Anchored or Not:
How Much Information Does 21st
Century Data Contain on Inﬂation Dynamics?,” Finance and Economics Discussion
Series 2022-016.
Washington:
Board of Governors of the Federal Reserve System,
https://doi.org/10.17016/FEDS.2022.016.
NOTE: Staﬀworking papers in the Finance and Economics Discussion Series (FEDS) are preliminary
materials circulated to stimulate discussion and critical comment. The analysis and conclusions set forth
are those of the authors and do not indicate concurrence by other members of the research staﬀor the
Board of Governors. References in publications to the Finance and Economics Discussion Series (other than
acknowledgement) should be cleared with the author(s) to protect the tentative character of these papers.

 
i 
 
 
Anchored or Not: How Much Information Does 21st Century Data Contain on 
Inflation Dynamics? 
 
Michael T. Kiley* 
Version 2 
February 22, 2022 
Abstract 
Inflation was low and stable in the United States during the first two decades of the 21st century and 
broke out of its stable range in 2021.  Experience in the early 21st century differed from that of the 
second half of the 20th century, when inflation showed persistent movements including the “Great 
Inflation” of the 1970s.  This analysis examines the extent to which the experience from 2000-2019 
should lead a Bayesian decisionmaker to update their assessment of inflation dynamics.  Given a prior 
for inflation dynamics consistent with 1960-1999 data, a Bayesian decisionmaker would not update their 
view of inflation persistence in light of 2000-2019 data unless they placed very low weight on their prior 
information.  In other words, 21st century data contains very little information to dissuade a Bayesian 
decisionmaker of the view that inflation fluctuations are persistent, or “unanchored”.  The intuition for, 
and implications of, this finding are discussed. 
 
JEL codes: E31, C11, E50 
Keywords: Inflation; Phillips Curve; Econometric Modeling.
 
* Federal Reserve Board, Washington DC. Email: mkiley@frb.gov. Michael Kiley is Deputy Director of the Division of 
Financial Stability of the Federal Reserve Board. The views expressed herein are those of the author, and do not 
reflect those of the Federal Reserve Board or its staff. 

 
1 
 
 
1. Introduction 
Consumer price inflation in the United States, as measured by the Consumer Price Index, jumped to just 
above 7 percent in the twelve months ending in December 2021.  Inflation in 2021 reached the highest 
level seen since the early 1980s.  The jump in inflation outside of the range experienced over several 
decades has raised questions regarding the speed with which, or the degree to which, inflation may 
return to the 2-percent range consistent with the Federal Reserve’s inflation objective.  The answers to 
these questions hinge on the nature of the inflation process, including its persistence and the impact of 
economic slack on the inflation outlook.   
A critical consideration in any work pursuing these questions is how to weigh data from different time 
periods.  For example, one approach would involve specifying a (set of) model(s) and examining the 
stability of the inflation process across time periods as indicated by statistical tests.  An alternative 
approach would involve a (set of) model(s) in which the parameters of the inflation process evolve over 
time (a time-varying parameter model) and would combine the model and data to estimate the 
evolution of parameters and resulting implications for the inflation outlook.  Substantial bodies of 
research have considered both approaches.   
This research pursues a different tack.  The approach herein is the one a Bayesian decisionmaker would 
follow.  The decisionmaker is endowed with a prior regarding the inflation process consistent with 
observed U.S. inflation data over the second half of the 20th century.  The analysis examines how the 
Bayesian decisionmaker would use data since 2000 to update his prior view.  The approach of the 
Bayesian decisionmaker has several advantages relative to other approaches.  The first advantage is that 
the approach has not been used to inform an assessment of inflation dynamics and hence provides a 
new (and different) perspective.  The second advantage is that the approach is a natural way to combine 
prior information/experience with recent data, in two senses: the approach flows directly from the 

 
2 
 
 
standard approach to combining prior information with subsequent data laid out by Thomas Bayes 250 
years ago (Bayes and Price, 1763); and the approach allows for flexibility in the strength assigned to the 
20th century experience in the assessment of the 21st century Phillips Curve.  Heuristically, this strength 
could be termed the degree of conviction in the prior information.  In the limiting case of essentially 
zero conviction in such prior experience, the Bayesian approach is equivalent to the approach in which a 
break is assumed in the Phillips Curve in the 21st century and only post-1999 data is used to estimate the 
inflation process (i.e., the first approach above).  Finally, the approach yields insights regarding the 
information in macroeconomic data that are likely broadly relevant in macroeconomics—and therefore 
can inform future research on other questions.  For example, the findings highlight the importance of 
assessing the strength of information in the data for assessing the evolution of other macroeconomic 
concepts, building on similar results in Kiley (2020a,b). 
The results that emerge from the analysis are very clear.  Data over the period 2000-2019 provide very 
little information with which to update prior views on the inflation process, at least with respect to 
inflation persistence or the “anchoring” of inflation.  As a result, a Bayesian decisionmaker aware of the 
inflation process from 1960-1999—that is, endowed with a prior consistent with that process—would 
view the current inflation process as similar to that from 1960-1999 unless they place very little weight 
on the prior information.  A direct implication of this result is that the inflation process may signal 
substantial persistence, suggesting the high inflation of 2021 may continue in 2022.  The intuition for 
this finding is straightforward.  Inflation was very stable from 2000-2019, which means the data 
witnessed few substantive deviations from its average or lagged values.  Because the data contain few 
sizable deviations of inflation from its average or lagged values, the data provide little information 
regarding what would happen if inflation were to deviate sizably from its average or lagged values—an 
intuitive insight that also follows directly from the mathematics of a Bayesian least-squares regression.  
The lack of information in the data from 2000-2019 contrast sharply with the precision of the prior view 

 
3 
 
 
of the role of lagged inflation in the inflation process that is consistent with experience from 1960-1999, 
when inflation saw sizable swings away from its average value and experience suggests a sizable role for 
lagged inflation in the Phillips curve.  This combination—low information in 2000-2019 data and an 
informative prior consistent with 1960-1999 experience—implies that the empirical analysis results in 
substantial inflation persistence unless the prior experience receives very little weight in the Bayesian 
decisionmaker’s calculus.  These findings highlight how researchers may find it valuable to assess the 
information in their recent data using Bayesian methods in cases where there is prior information, as an 
approach to complement approaches such as time-varying parameter models or structural-break 
analyses. 
Previous literature: The analysis is related to the empirical literature examining the factors that 
determine the inflation process and how the importance of such factors may have shifted over time to 
explain high and variable inflation in the 1970s and low and stable inflation in the 21st century.1  These 
include the degree to which the inflation process is “anchored” (i.e., the degree to which lagged inflation 
influences current inflation), the effect of unemployment on inflation (i.e., the slope of the Phillips 
curve), and the path of “supply shocks” or other supply factors that shift the relationship between 
inflation and economic slack.  While alternative approaches are possible, a common—and simple—
approach is to use a reduced-form Phillips curve relating inflation to its lags and the unemployment rate 
(e.g., Ball and Mazumder, 2011 & 2019; Gordon, 2013; Kiley, 2015; or Blanchard, 2016). 
In this taxonomy, an “anchored” inflation process shows little effect of current inflation on subsequent 
inflation.  The empirical work herein links anchoring to the persistence in inflation, which could reflect a 
variety of structural factors.  For example, a sizable body of research has suggested that inflation 
persistence may have fallen in the 21st century. (e.g., Williams, 2006a,b; Kiley, 2008b; Ball and 
 
1 Theoretical modeling has also considered possible factors, e.g., Kiley (2007). 

 
4 
 
 
Mazumder, 2011, 2019; Stock, 2011; Watson, 2014; Coibion and Gorodnichenko, 2015; Kiley, 2015b; 
Blanchard, 2016; Jorgenson and Lansing, 2019; and Carvalho et al, 2021).  A prominent line of thought in 
this research is that inflation expectations (in the Phillips Curve) followed an accelerationist structure in 
the decades before 2000—responding strongly to recent inflation experience—and that inflation 
expectations were anchored in the years after 2000—responding little to lagged inflation.  But much of 
this work is similar to the approach herein, focusing on inflation persistence with little direct attention 
to expectations.  Future work can consider the implications of the approach herein for expectations per 
se.  Some research also has questioned the decline in inflation persistence (e.g., Pivetta and Reis, 2007—
although this study predates the low and stable inflation of the first two decades of the 21st century). 
Research has also suggested a weaker relationship between unemployment and inflation in recent 
decades—that the Phillips curve has flattened in the 21st century or earlier (Atkeson and Ohanian, 2001).  
Ball and Mazumder (2011) suggest that "menu cost" models of nominal price and wage rigidity imply 
that such rigidities increase as the average rate of inflation falls, implying that more of the adjustment in 
nominal aggregate demand falls on output and less on inflation when inflation is low; this is exactly the 
finding emphasized in Kiley (2000), which analyzed support for this prediction across a large sample of 
countries. Research exploring the effects of downward nominal-wage rigidity points to a reduced effect 
of labor-market weakness on inflation in a low-inflation environment (Daly and Hobijn, 2014). Kiley 
(2008b) and Boivin, Kiley, and Mishkin (2010) present evidence that a clear commitment to price 
stability in recent decades, in the form of a monetary policy rule with a more sizable response to 
inflation, acts to substantially stabilize inflation expectations and mitigate fluctuations in inflation.  Such 
a shift in monetary policy behavior is consistent with an observed flattening in the Phillips curve in the 
21st century.  Del Negro et al (2020) find a similar role for monetary policy but find a large role of for 
structural factors related to aggregate supply in the flattening of the Phillips Curve. 

 
5 
 
 
The literature pursues different empirical approaches, within or outside a Phillips curve approach.  Much 
of the literature considers reduced-form Phillips curves estimated across subsamples of the data—i.e., 
considers breaks in estimated equations.  Examples include Williams (2006), Kiley (2008b and 2015), 
Blanchard (2016), and Ball and Mazumder (2019).  Other work explicitly models time variation in 
parameters, for example in vector autoregressions as in Cogley and Sargent (2005) and Primiceri (2005).  
A particularly influential class of time-varying parameter models are time-varying parameter unobserved 
component models (Stock and Watson, 2007; and Kiley, 2008a).  In this approach, it is common for 
results to suggest that the variance of the permanent drift components was lower in the 2000-2019 
period than earlier—i.e., that inflation was anchored in the 21st century. 
The approach herein uses the textbook approach to Bayesian regression (e.g., Kim and Nelson 1999, 
Chapter 7) to examine the information content of the data for parameters of a Phillips Curve relative to 
the information in a reasonable prior.  This approach has not been used in discussions of inflation 
dynamics.  Bayesian approaches are often used in estimation of time-varying parameter models, as in 
Primiceri (2005)—but these analyses do not focus on the information content in the data relative to that 
in the prior; rather, they emphasize the value of Bayesian methods given the complexity of estimating 
such models.  Kiley (2020a, 2020b) highlights how macroeconomic relationships may be poorly informed 
by aggregate time-series data and how the available data may not lead posterior assessments to differ 
from prior views in an examination of the equilibrium real interest rate.2 
The analysis also raises questions regarding why inflation was more stable from 2000 onward.  The 
Bayesian approach indicates that the data do not contain information to suggest a very large change in 
inflation persistence relative to pre-2000 experience.  Under this view, the post-2000 inflation 
 
2 Given limited information in aggregate time-series data, Fitzgerald and Nicolini (2014) and Kiley (2015a) analyze 
Phillips curves using city-level and state-level data, respectively.  Hooper et al (2019) and Hazell et al (2020) build 
on this approach. 

 
6 
 
 
experience would be ascribed to “luck” that resulted in smaller shocks to inflation.  Previous research 
has noted the challenges associated with distinguishing “luck” from structural changes (e.g., Ahmed, 
Levin, and Wilson, 2004). 
Structure of the remaining sections: Section 2 discusses data and the framework a Bayesian 
decisionmaker endowed with a prior for the inflation process in the United States consistent with data 
over the second half of the 20th century would use to incorporate the information from the data over 
the 2000-2019 period in their view on the inflation process. Section 3 presents results, intuition, and 
implications. Section 4 concludes. 
2. Data and approach 
2.1 Data 
The study analyses inflation in the United States.  The analysis focuses on the Consumer Price Index 
(CPI), produced monthly by the U.S. Bureau of Labor Statistics.  The focus of the investigation is the 
evolution of the persistence of inflation and, to a lesser extent, the slope of the Phillips Curve.  To 
abstract from the volatility induced by fluctuations in food and energy prices, the empirical work uses 
the CPI excluding food and energy (core CPI), which is available from January 1957 to December 2021.  
The results are generally similar for the overall CPI, reflecting the correlation between overall and core 
CPI (e.g., Kiley, 2008a).  The results are also similar when the price index considered is the chain-
weighted price index for personal consumption expenditures (PCE prices).  Note that the Federal Open 
Market Committee (FOMC) of the Federal Reserve System has defined its inflation objective of 2 percent 
in terms of PCE prices since 2012 and inflation as measured by the CPI index has averaged a few tenths 
above inflation as measured by PCE prices in recent decades; for this reason, we will refer to the 
inflation objective in the United States, as measured by the CPI, as in the range of 2 percent. 

 
7 
 
 
The Phillips Curve framework relates inflation to a measure of economic slack.  The analysis uses the 
unemployment rate of the civilian noninstitutional population aged 16 and over (the unemployment 
rate), produced monthly by the U.S. Bureau of Labor Statistics. 
Figure 1 presents the data on inflation and the unemployment rate.  The inflation measure presented is 
the 12-month change in the natural logarithm of the core CPI (upper panel).  Inflation was low and 
stable in the late 1950s and early 1960s.  Inflation rose over the late 1960s and was both higher and 
more volatile over the 1970s.  After the tightening in monetary policy associated with the Volcker 
disinflation that began in late 1979, inflation drifted lower over the course of the 1980s and early 1990s.  
Over this period from the late 1950s through the mid-1990s, inflation appeared to be persistent—that 
is, years in which inflation exceeded the average over this period tended to be followed by years in 
which inflation was above its average.  From 2000 until 2019, inflation was generally low—near 2 
percent—and stable.  Inflation jumped out of its 2000-2019 range in 2021, reaching about 5½ percent in 
a twelve-month basis in December 2021.  The unemployment rate (the bottom panel) rises sharply 
during recessions and declines during expansions, highlighting how it is a good measure of the state of 
the U.S. business cycle. 
Table 1 presents some summary statistics on inflation and the unemployment rate.  Statistics are 
presented for monthly data and for data on an annual average basis, as the Phillips Curve analysis will 
consider data at both the monthly and annual frequency as one robustness check.  Statistics are shown 
for three sample periods: late 1950s-2019, late 1950s-1999, and 2000-2019.  These three sample 
periods will be referred to as the full sample, the pre-2000 sample, and the post-1999 sample.  The 
years 2020 and 2021 are excluded from the table and the estimation sample, reflecting the 
unprecedented (and unusual) effects of the COVID-19 pandemic; econometric work will almost surely 

 
8 
 
 
explore various ways to treat these unusual years in emerging research.3  Two aspects of the summary 
statistics will prove important in understanding the results.  First, inflation was much more volatile in the 
pre-2000 period than in the post-1999 period, as can be seen in the standard deviations of the series 
during the periods.  Second, inflation was much more persistent in the pre-2000 period than in the post-
1999 period, as can be seen in the autocorrelation of the series. 
2.2 Empirical Approach 
The analysis considers estimates of a Phillips Curve in which inflation (∆𝑝(𝑡)) depends on its own lags 
and the (lagged) unemployment rate (𝑢(𝑡)) as in equation (1) (in which a constant term is suppressed): 
(1) 
∆𝑝(𝑡) = ෍𝑏(𝑗) ∙∆𝑝(𝑡−𝑗)
ேିଵ
௝ୀଵ
+ 𝑎∙𝑢(𝑡−1) + 𝑒(𝑡). 
b(j) are the coefficients governing persistence, 𝑎 is the slope of the Phillips curve, and e(t) is the residual 
reflecting “supply” shocks and other unmodeled factors which follows a Normal distribution 
(𝑒(𝑡)~N(0,σଶ)).  An anchored Phillips Curve would tend to have small b(j), whereas an unanchored 
Phillips Curve will tend to have large b(j).  The sum of these coefficients, ∑
𝑏(𝑗)
ே
௝ୀଵ
, will be the statistic of 
focus, with a sum near 1 representing an unanchored accelerationist Phillips Curve. 
The vector of coefficients in equation (1) is denoted by Γ.  The matrix containing the dependent variable 
(inflation) will be denoted Y (Tx1, where T is the number of observations), the matrix of right-hand side 
variables will be denoted X (TxN), and the matrix of error terms will be denoted E (Tx1), yielding 
(2)
𝑌= 𝑋Γ + 𝐸.
The classical approach to inference would estimate Γ by least squares as Γ௅ௌ= (𝑋′𝑋)ିଵ𝑋ᇱ𝑌. 
 
3  Lenza and Primiceri (2020) and Schorfheide and Song (2021) highlight the potential sensitivity of 
macroeconometric estimates to the COVID-19 pandemic period, with the former suggesting some approaches to 
handling these issues. 

 
9 
 
 
The decisionmaker herein follows a Bayesian approach.  The decisionmaker is endowed with a prior for 
Γ that is given by the Normal distribution with mean Γ෨ and variance-covariance matrix V—i.e., a prior 
distribution Γ~N(Γ෨,V).  The analysis proceeds under the assumption that the decisionmaker knows the 
variance of e(t) (σଶ), so the Bayesian estimation is conditional on σଶ  and the assumed prior is the 
natural conjugate prior for Γ conditional on σଶ.  An alternative approach would also specify a prior view 
on σଶ and jointly estimate the posterior distributions of Γ and σଶ.  This alternative approach yields 
essentially identical results for reasonable priors on σଶ, but yields more complicated algebraic 
expressions that slightly impede intuition for those less familiar with Bayesian least squares.  As a result, 
the simpler approach is adopted herein. 
Given the prior information, the decisionmaker estimates Γ by combining their prior information and 
the data—i.e., the prior distribution and the likelihood function of the data—to form the posterior 
distribution for Γ and estimates Γ to maximize this posterior distribution.  This is a textbook example of 
Bayesian regression (Kim and Nelson 1999, Chapter 7), with the resulting estimate Γ෠ given by 
(3)
Γ෠= (𝑉ି
ଵ+ σିଶ𝑋ᇱ𝑋)ିଵ(𝑉ି
ଵΓ෨+ σିଶ𝑋ᇱ𝑋Γ௅ௌ). 
Notice in equation (3) that the Bayesian decisionmaker estimates the parameters as the matrix-
weighted average of their prior information and the least-squares estimate, with weights given by the 
precision of the information in the prior and the data (e.g., by the inverses of the variance-covariance 
matrices of Γ෨ and Γ௅ௌ, V and σଶ(𝑋ᇱ𝑋)ିଵ). 
Equation (3) suggests a natural approach to considering different degrees of conviction regarding the 
prior information.  The Bayesian decisionmaker can further “weight” their prior by a factor 𝑤, as in 
(4)
Γ෠= (𝑤𝑉ି
ଵ+ (1 −𝑤)σିଶ𝑋ᇱ𝑋)ିଵ(𝑤𝑉ି
ଵΓ෨+ (1 −𝑤)σିଶ𝑋ᇱ𝑋Γ௅ௌ). 

 
10 
 
 
Intuitively, essentially zero weight on the prior information returns the least-squares estimate.  This 
“weighting” terminology is convenient.  Mathematically, it is equivalent to considering a less informative 
prior.  Specifically, estimates with a weight of 𝑤 on the prior information are equivalent to estimates 
with a prior for Γ with the same mean and a variance-covariance matrix equal to 
ଵି௪
௪V.  For example, a 
weight on the prior equal to 20 percent (𝑤=0.2) is equivalent to a prior with a four-times looser 
variance-covariance matrix 4V. 
With this background, the approach involves choosing the lag specification in the Phillips Curve, a choice 
of the prior distribution and consideration of alternative weights on this prior distribution. 
 
Lag specification in the Phillips Curve: In the estimates using monthly data, the lag length 
equals 12 (N=13) and the coefficients on the 1st through 12th lag are equal—i.e., 
∑
𝑏(𝑗) ∙∆𝑝(𝑡−𝑗)
ேିଵ
௝ୀଵ
= 𝑏(1) ∑
∆𝑝(𝑡−𝑗)/12
ଵଶ
௝ୀଵ
;  alternative choices for the lag structure 
yielded similar results (see section 3.3), and this specification is simplest.  For the estimates 
using annual data, the lag length equals 1 (N=2). 
 
Choice for prior 𝚪~𝐍(𝚪෨,V): The prior distribution used to inform estimates of the 21st century 
Phillips curve is given by the values consistent with the pre-2000 sample.  Γ෨ is given by the least-
squares estimate for this sample and V is the associated variance-covariance matrix.  This is akin 
to an empirical Bayesian approach.  The thought experiment is one in which the decisionmaker 
was endowed with information on the Phillips Curve in the latter half of the 20th century and 
chooses to update their view following the realization of data from 2000-2019. 
 
Choice of weights 𝒘: To consider decreasing levels of conviction in the relevance of the 20th 
century prior (i.e., looser priors), four values for weights on the prior are considered, with the 

 
11 
 
 
factor 𝑤 taking values of 0.5, 0.2, 0.05, or (approximately) 0—corresponding to variance 
covariance matrices for the prior equal to V, 4V,19V, and an uninformative prior. 
Figure 2 presents the prior distributions for the coefficient on the lags of inflation and the slope of the 
Phillips Curve for these alternative weights.  The priors show high values of persistence (a central 
tendency for the sum on inflation lags near 1) and a notable slope to the Phillips Curve (i.e., a negative 
slope with a degree of precision in the prior distribution).4 
3. Results 
3.1 Estimates 
The results for posterior estimates of the Phillips Curve parameters conditional on data from 2000-2019 
by the Bayesian decisionmaker are shown in figure 3 and table 2.  Two results emerge clearly.   
First, the degree of persistence in the posterior estimates is high in all cases except those with very little 
weight on the 20th century prior.  In the monthly estimates, the coefficient on lagged inflation exceeds 
0.9 with equal weights on prior and data, exceeds 0.85 when the weight on the prior is 0.20, and is near 
0.7 when the weight on the prior is 0.05; in the limiting case of essentially no weight on the prior, the 
coefficient on the lags is small at about 0.2 (in line with simple least squares for the 2000-2019 period).  
For the annual data, the coefficient on lagged inflation in the posterior is about 7/8, ¾, and ½ for 
weights on the prior of 0.5, 0.2, and 0.05—whereas the coefficient is 0 for the uninformative prior. 
Second, the slope of the Phillips Curve is consistently smaller in absolute value in the posterior estimates 
of the parameters—irrespective of the weight on the prior.  For example, the slope of the Phillips Curve 
 
4 The estimates use inflation data expressed at annual rates.  This convention makes the slope coefficients 
somewhat more comparable (albeit still not strictly comparable, reflecting how time-averaging would affect 
impact estimates at different frequencies). 

 
12 
 
 
is less than ½ the prior value (the pre-2000 data value from least squares) in the posterior estimates for 
all weights on the prior. 
These results suggest that the approach of a Bayesian decisionmaker confirms the finding in the 
literature that the Phillips Curve is “flatter”.  In contrast, the approach of a Bayesian decisionmaker does 
not find the degree of “anchored” inflation as would be implied by an estimate using only recent data, in 
the sense that the coefficient on lagged inflation is substantial when prior information is incorporated.  
Nonetheless, the coefficient on the lags of inflation is less than one—so the process is not of the 
“accelerationist” type and would generally imply that deviations of inflation from its average may be 
long-lived but are ultimately transitory. 
3.2 Intuition 
The results are clear—but they are also very intuitive.  Recall from equation (4) that the posterior 
estimates are the matrix-weighted average of the prior mean and least-squares estimate for the post-
1999 period, with weights given by the inverse of the variance-covariance matrices. 
For the slope of the Phillips Curve, the variance-covariance matrix of the post-1999 least-squares 
estimate implies a fair degree of precision.  Recall that this matrix is σଶ(𝑋ᇱ𝑋)ିଵ and its inverse is 
σିଶ𝑋ᇱ𝑋.  The component of this matrix that “weights” the least-squares estimate is dominated by the 
sum of squared deviations of the unemployment rate from its mean (assuming a modest covariance 
between inflation and unemployment).  The summary statistics in table 1 show that this sum of squares 
remains sizable relative to its pre-2000 value, as indicated by the standard deviation of the 
unemployment rate.  As a result, the least-squares estimate receives considerable weight in the 
Bayesian decisionmaker’s calculus. 
In contrast, inflation is quite stable in the post-1999 period.  Its sum of squared deviations from the 
mean are modest relative to the pre-2000 experience, as indicated by the standard deviation.  This 

 
13 
 
 
implies the data for 2000-2019 receive relatively little weight in a Bayesian decisionmaker’s calculus 
when assessing the persistence of inflation.  In words, inflation did not deviate from its average value 
much over 2000-2019, and hence a Bayesian decisionmaker does not weigh experience over that period 
highly when evaluating how persistent a deviation of inflation from its mean is likely to be.  This is 
intuitive—the data do not provide examples of what would happen should inflation deviate from its 
mean, and hence the data are not informative about what would happen following such a deviation. 
A look at measures of fit provides some intuition for why models with such different dynamic 
properties—the estimates with different weights on the prior—emerge.  Figure 4 presents a dynamic 
simulation of the estimates from 2000-2019 in the top panel and the residuals implied by each estimate 
in the bottom panel, in both cases for the monthly-data specification.  All the estimates lead to a 
dynamic simulation of relatively low and stable inflation—although the case with a weight of 0.5 on the 
prior information shows more variability and a worse “fit” than the others.  Looking at one-period 
misses, the residuals are all very highly correlated.  The residuals are highly correlated across 
specifications with a large coefficient on the lag and a small coefficient on the lag because inflation has 
been stable and the contribution of the lag is small, irrespective of the coefficient.  This intuition is the 
same as that above—inflation has been stable and hence the data do not differentiate much between a 
specification with a large or small coefficient on lagged inflation. 
This intuition also provides insight into the comparison of the full sample results from least squares 
(reported in table 2) with the results from a Bayesian approach.  The full sample results are similar to 
those of a Bayesian decisionmaker that places weight on the pre-2000 experience—inflation is 
persistent, and the Phillips Cure is flatter than in the pre-2000 period.  The pre-2000 experience 
dominates the variation in the data and hence drive the full sample estimates of persistence.  This 
comparison also highlights a potential weakness of the approach of a Bayesian decisionmaker for a 
researcher that views a structural break as likely.  The Bayesian decisionmaker views the parameters as 

 
14 
 
 
drawn from a stable distribution and allows the data to move them away from their prior view.  This 
approach is consistent with the notion that the future may look different than embedded in prior 
information, but not consistent with a structural break—which would imply prior information has no 
value.  The findings herein suggest that a researcher may wish to entertain the possibility that 
experience from 2000-2019 is consistent with a sizable degree of persistence in inflation, but also may 
wish to consider alternative approaches that allow for structural breaks or time-varying parameters. 
3.3 Robustness and Implications 
As noted above, the basic results do not depend upon the specific lag structure assumed for inflation in 
the results reported in table 2.  To illustrate the robustness of the results to alternative specifications, 
table 3 considers a slightly more flexible lag structure, as in  
∆𝑝(𝑡) = 𝑏(1) ෍∆𝑝(𝑡−𝑗)
3
ଷ
௝ୀଵ
+ 𝑏(2) ෍∆𝑝(𝑡−𝑗)
9
ଵଶ
௝ୀସ
+ 𝑎∙𝑢(𝑡−1) + 𝑒(𝑡). 
In this alternative, the sum of the coefficients on the lags of inflation (𝑏(1) + 𝑏(2)) gives a rough gauge 
of the persistence of inflation.  The results are substantially similar to those for the simpler specification 
in table 2, with 𝑏(1) + 𝑏(2) estimated at essentially the same values as those for 𝑏(1) in table 2. 
The implications of the results for inflation forecasts are direct.  A Phillips Curve based on post-1999 
data alone would imply a sharp deceleration of inflation in 2022, as there is very little persistence 
estimated in that case.  In contrast, the Bayesian estimates imply that inflation will remain quite high in 
2022 in the absence of unexpected shocks.  Generally speaking, the results herein suggest a higher 
degree of persistence is plausible, pointing to potentially higher inflation in 2022. 
4. Conclusions 
This analysis examined the extent to which the experience from 2000-2019 should lead a Bayesian 
decisionmaker to update their assessment of inflation dynamics.  Given a prior for inflation dynamics 

 
15 
 
 
consistent with 1960-1999 data, a Bayesian decisionmaker would not update their view of inflation 
persistence in light of 2000-2019 data unless they placed very low weight on their prior information.  In 
other words, 21st century data contains very little information to dissuade a Bayesian decisionmaker of 
the view that inflation fluctuations are persistent, or “unanchored”. 
The idea that data over short sample periods may provide limited information regarding macroeconomic 
relationships may be relevant for other areas in macroeconomics.  For example, Kiley (2020a,b) finds 
modest information in the data for estimates of the equilibrium real interest rate.  These findings 
suggest macroeconomists may find useful a Bayesian approach that examines the information in the 
data more thoroughly than is common in empirical macroeconomics. 
 
 

 
16 
 
 
References 
Ahmed, Shaghil, Levin, Andrew and Wilson, Beth Anne, (2004), Recent U.S. Macroeconomic Stability: 
Good Policies, Good Practices, or Good Luck?, The Review of Economics and Statistics, 86, issue 3, p. 
824-832, https://EconPapers.repec.org/RePEc:tpr:restat:v:86:y:2004:i:3:p:824-832. 
Atkeson, A. and L. E. Ohanian, 2001. “Are Phillips Curves Useful for Forecasting Inflation?” Federal 
Reserve of Minneapolis Quarterly Review, 25(1), 2–11. 
Ball, Laurence, & Mazumder, Sandeep, 2011. "Inflation Dynamics and the Great Recession." In: 
Brookings Papers on Economic Activity (Spring), pp. 337–381. 
Ball, Laurence, & Mazumder, Sandeep, 2019. “A Phillips Curve with Anchored Expectations and Short-
Term Unemployment,” Journal of Money, Credit and Banking, 51, 111–137. 
Bayes, Thomas & Price, Richard (1763). "An Essay towards solving a Problem in the Doctrine of Chance. 
By the late Rev. Mr. Bayes, communicated by Mr. Price, in a letter to John Canton, A. M. F. R. S." 
Philosophical Transactions of the Royal Society of London. 53: 370–418. doi:10.1098/rstl.1763.0053. 
Blanchard, O., 2016. “The Phillips Curve: Back to the ’60s?” American Economic 
Review, 106, 31–34. 
Boivin, Jean & Kiley, Michael T. & Mishkin, Frederic S., 2010. "How Has the Monetary Transmission 
Mechanism Evolved Over Time?," Handbook of Monetary Economics, in: Benjamin M. Friedman & 
Michael Woodford (ed.), Handbook of Monetary Economics, edition 1, volume 3, chapter 8, pages 369-
422 Elsevier. 
Carvalho, Carlos; Eusepi, Stefano; Moench, Emanuel; Preston, Bruce, 2021. Anchored inflation 
expectations. Available at SSRN 3018198.  
 
Cogley, Timothy & Thomas J. Sargent, 2005. "Drift and Volatilities: Monetary Policies and Outcomes in 
the Post WWII U.S," Review of Economic Dynamics, Elsevier for the Society for Economic Dynamics, vol. 
8(2), pages 262-302, April.  
Coibion, Olivier & Yuriy Gorodnichenko, 2015. "Is the Phillips Curve Alive and Well after All? Inflation 
Expectations and the Missing Disinflation," American Economic Journal: Macroeconomics, American 
Economic Association, vol. 7(1), pages 197-232, January. 
Daly, Mary C. & Bart Hobijn. 2014. "Downward Nominal Wage Rigidities Bend the Phillips Curve." FRB 
San Francisco Working Paper 2013-08. 
Fitzgerald, T. J. and J. P. Nicolini (2014): “Is There a Stable Relationship between Unemployment and 
Future Inflation? Evidence from U.S. Cities,” Working Papers 713, Federal Reserve Bank of Minneapolis. 
Gordon, Robert J., 2013. "The Phillips Curve is Alive and Well: Inflation and the NAIRU During the Slow 
Recovery." NBER Working Paper No. 19390, August. 
Hooper, Peter; Mishkin, Frederic S; Sufi, Amir, 2020. Prospects for inflation in a high pressure economy: 
Is the Phillips curve dead or is it just hibernating? Research in Economics 74(1):26-62. Elsevier. 
Jorgensen, Peter; Lansing, Kevin J., 2019. Anchored inflation expectations and the flatter Phillips curve.   

 
17 
 
 
Kiley, Michael T., 2000. "Endogenous Price Stickiness and Business Cycle Persistence," Journal of Money, 
Credit and Banking, Blackwell Publishing, vol. 32(1), pages 28-53, February. 
Kiley, Michael T., 2007. "Is Moderate-to-High Inflation Inherently Unstable?," International Journal of 
Central Banking, International Journal of Central Banking, vol. 3(2), pages 173-201, June.  
Kiley, Michael T., 2008a. "Estimating the common trend rate of inflation for consumer prices and 
consumer prices excluding food and energy prices," Finance and Economics Discussion Series 2008-38, 
Board of Governors of the Federal Reserve System (U.S.). 
Kiley, Michael T., 2008b. "Inflation expectations, Uncertainty, the Phillips curve, and Monetary Policy - 
Comments," in Fuhrer, Jeffrey et al (eds), Understanding Inflation and the Implications for Monetary 
Policy: A Phillips Curve Retrospective. The MIT Press, Cambridge, MA. 
Kiley, Michael T., 2015a. "An evaluation of the inflationary pressure associated with short- and long-
term unemployment," Economics Letters, Volume 137, December, Pages 5-9, ISSN 0165-1765, 
http://dx.doi.org/10.1016/j.econlet.2015.10.005 
Kiley, Michael T., 2015b. "Low Inflation in the United States: A Summary of Recent Research," FEDS 
Notes. Washington: Board of Governors of the Federal Reserve System, November 23, 2015. 
https://doi.org/10.17016/2380-7172.1665 
Kiley, Michael T., 2020a. "The Global Equilibrium Real Interest Rate: Concepts, Estimates, and 
Challenges," Annual Review of Financial Economics, Annual Reviews, vol. 12(1), pages 305-326, 
December.  
Kiley, Michael T., 2020b. "What Can the Data Tell Us about the Equilibrium Real Interest Rate?," 
International Journal of Central Banking, International Journal of Central Banking, vol. 16(3), pages 181-
209, June. 
Lenza, Michele & Giorgio E. Primiceri, 2020. "How to Estimate a VAR after March 2020," NBER Working 
Papers 27771, National Bureau of Economic Research, Inc.  
Pivetta, Frederic and Reis, Ricardo, (2007), The persistence of inflation in the United States, Journal of 
Economic Dynamics and Control, 31, issue 4, p. 1326-1358, 
https://EconPapers.repec.org/RePEc:eee:dyncon:v:31:y:2007:i:4:p:1326-1358. 
Primiceri, Giorgio E., 2005. "Time Varying Structural Vector Autoregressions and Monetary Policy," 
Review of Economic Studies, Oxford University Press, vol. 72(3), pages 821-852.  
Schorfheide, Frank & Dongho Song (2021) REAL-TIME FORECASTING WITH A (STANDARD) MIXED-
FREQUENCY VAR DURING A PANDEMIC. NBER WORKING PAPER SERIES Working Paper 29535. 
http://www.nber.org/papers/w29535 
Stock, James, 2011. "Comment on Inflation Dynamics and the Great Recession." In: Brookings Papers on 
Economic Activity (Spring), pp. 387–402.  
Stock, James H. & Mark W. Watson, 2007. "Why Has U.S. Inflation Become Harder to Forecast?," 
Journal of Money, Credit and Banking, Blackwell Publishing, vol. 39(s1), pages 3-33, February.  

 
18 
 
 
Watson, Mark W., 2014. "Inflation Persistence, the NAIRU, and the Great Recession." In: American 
Economic Review (Papers and Proceedings), May. 
Williams, John C., 2006. Inflation persistence in an era of well-anchored inflation expectations. FRBSF 
Economic Letter. Federal Reserve Bank of San Francisco. 
Williams, John C., 2006. The Phillips curve in an era of well-anchored inflation expectations. unpublished 
working paper, Federal Reserve Bank of San Francisco, September. 
 

 
19 
 
 
Table 1: Data Summary Statistics 
Observations
Mean
(annual rate) 
Std. 
Deviation
Auto-
Correlation
Monthly data 
 
 
 
Full sample 
CPI inflation (percent) 
744
3.6
0.25
0.66
Unemployment rate (percent) 
- 
6.0
1.6
0.99
Pre-2000 sample 
CPI inflation (percent) 
504
4.3
0.27
0.62
Unemployment rate (percent) 
- 
6.0
1.5
0.99
Post-1999 sample 
CPI inflation (percent) 
240
2.0
0.08
0.21
Unemployment rate (percent) 
- 
5.9
1.8
0.99
Annual data 
 
 
 
Full sample 
CPI inflation (percent) 
61
3.6
2.4
0.88
Unemployment rate (percent) 
- 
6.0
1.6
0.80
Pre-2000 sample 
CPI inflation (percent) 
41
4.4
2.6
0.83
Unemployment rate (percent) 
- 
6.0
1.5
0.78
Post-1999 sample 
CPI inflation (percent) 
20
2.0
0.4
0.42
Unemployment rate (percent) 
- 
5.9
1.8
0.77
Source: Bureau of Labor Statistics and author’s calculations.  Full sample: Jan. 1958-Dec. 2019 (monthly) 
and 1959-2019 (annual); Pre-2000 sample: Jan. 1958-Dec. 1999 (monthly) and 1959-1999 (annual); Post-
1999 sample: Jan. 2000-Dec. 2019 (monthly) and 2000-2019 (annual).

 
20 
 
 
Table 2: Estimation of posterior of parameters 
∆𝑝(𝑡) = 𝑏(1) ෍∆𝑝(𝑡−𝑗)/𝑁
ே
௝ୀଵ
+ 𝑎∙𝑢(𝑡−1) + 𝑒(𝑡). 
Monthly data (lag length N = 12) 
 Estimates of a Bayesian decisionmaker
Classical least-squares estimates
Weight on 
prior=0.5 
Weight on 
prior=0.2 
Weight on 
prior=0.05 
Uninformative 
prior 
Full sample
Pre-2000 
sample 
Post-2000 
sample 
b(1)
0.92
0.86
0.66
0.17
0.95
0.97
0.17 
s.e. 
0.03 
0.05 
0.10 
0.16 
0.03 
0.04 
0.16 
a
-0.07
-0.04
-0.06
-0.13
-0.19
-0.32
-0.13 
s.e. 
0.03 
0.03 
0.03 
0.04 
0.05 
0.07 
0.04 
Annual data (lag length N = 1) 
b(1)
0.86
0.74
0.43
-0.05
0.92
0.94
-0.05
s.e. 
0.05 
0.10 
0.17 
0.24 
0.06 
0.08 
0.24 
a 
-0.05
-0.05
-0.09
-0.16
-0.23
-0.41
-0.16
s.e. 
0.04 
0.04 
0.05 
0.05 
0.09 
0.15 
0.05 
Source: Bureau of Labor Statistics and author’s calculations. 
Note: Full sample: Jan. 1958-Dec. 2019 (monthly) and 1959-2019 (annual); Pre-2000 sample: Jan. 1958-Dec. 1999 (monthly) and 1959-1999 
(annual); Post-1999 sample: Jan. 2000-Dec. 2019 (monthly) and 2000-2019 (annual). 
 
 

 
21 
 
 
Table 3: Estimation of posterior of parameters—alternative lag specification 
∆𝑝(𝑡) = 𝑏(1) ෍∆𝑝(𝑡−𝑗)
3
ଷ
௝ୀଵ
+ 𝑏(2) ෍∆𝑝(𝑡−𝑗)
9
ଵଶ
௝ୀସ
+ 𝑎∙𝑢(𝑡−1) + 𝑒(𝑡). 
Monthly data 
 Estimates of a Bayesian decisionmaker
Classical least-squares estimates
Weight on 
prior=0.5 
Weight on 
prior=0.2 
Weight on 
prior=0.05 
Uninformative 
prior 
Full sample
Pre-2000 
sample 
Post-2000 
sample 
b(1)
0.52
0.47
0.39
0.24
0.53
0.52
0.24 
s.e. 
0.05 
0.07 
0.09 
0.10 
0.05 
0.06 
0.10 
b(2)
0.40
0.39
0.28
-0.05
0.41
0.44
-0.05 
s.e.
0.05 
0.08 
0.11 
0.15 
0.06 
0.07 
0.15 
a
-0.05
-0.03
-0.06
-0.13
-0.12
-0.21
-0.13 
s.e. 
0.03 
0.03 
0.03 
0.04 
0.05 
0.08 
0.04 
Source: Bureau of Labor Statistics and author’s calculations. 
Note: Full sample: Jan. 1958-Dec. 2019 (monthly); Pre-2000 sample: Jan. 1958-Dec. 1999 (monthly); Post-1999 sample: Jan. 2000-Dec. 2019 
(monthly). 
 
 
 

 
22 
 
 
Figure 1: CPI Inflation and the Civilian Unemployment Rate 
 
Source: Bureau of Labor Statistics and author’s calculations. 
 
 

 
23 
 
 
Figure 2: Prior Information 
 
Source: Bureau of Labor Statistics and author’s calculations. 
 
 

 
24 
 
 
Figure 3: Posterior Estimates 
 
Source: Bureau of Labor Statistics and author’s calculations. 
 
 

 
25 
 
 
Figure 4: Visual Assessments of Fit 
 
Source: Bureau of Labor Statistics and author’s calculations. 
 

