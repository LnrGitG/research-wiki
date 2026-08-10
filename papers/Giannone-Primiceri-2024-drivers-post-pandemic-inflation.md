---
title: "The Drivers of Post-Pandemic Inflation"
authors: Domenico Giannone, Giorgio E. Primiceri
year: 2024
doi: 10.3386/w32859
publisher: NBER Working Paper 32859
url: https://www.nber.org/papers/w32859
type: paper
tags: ['inflation', 'post-pandemic', 'demand-shocks', 'supply-shocks', 'SVAR', 'NBER']
---

# The Drivers of Post-Pandemic Inflation

**Авторы:** Domenico Giannone, Giorgio E. Primiceri
**Год:** 2024
**DOI:** 10.3386/w32859
**Источник:** NBER Working Paper 32859
**URL:** https://www.nber.org/papers/w32859
**PDF:** `raw/papers/giannone_2024_drivers.pdf`

## Аннотация (EN)

Post-covid inflation was predominantly driven by unexpectedly strong demand forces, not only in the United States, but also in the Euro Area. In comparison, the inflationary impact of adverse supply shocks was less pronounced, even though these shocks significantly constrained economic activity. With output already weakened by these unfavourable supply conditions, any attempt by the European Central Bank to further mitigate the demand-driven inflationary pressures---to maintain inflation near its 2-percent target---would have severely hampered an already anaemic recovery.

## Аннотация (RU)

Послековидная инфляция была преимущественно вызвана неожиданно сильными шоками спроса, не только в США, но и в еврозоне. Инфляционное влияние неблагоприятных шоков предложения было менее выраженным, хотя эти шоки существенно ограничивали экономическую активность. С помощью структурной VAR количественно оценивается относительный вклад шоков спроса и предложения, и показывается, что шоки спроса сыграли доминирующую роль.

## Полный текст

NBER WORKING PAPER SERIES
THE DRIVERS OF POST-PANDEMIC INFLATION
Domenico Giannone
Giorgio Primiceri
Working Paper 32859
http://www.nber.org/papers/w32859
NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
August 2024
We thank our discussant, Fernanda Nechio, an anonymous ECB referee, Philipp Hartmann, Jirka 
Slacalek, Carlo Altavilla, Giacomo Carboni, Jacopo Cimadomo, Chris Erceg, Pierre-Olivier 
Gourinchas, Davide Furceri, Kamil Koval, Michele Lenza, Matteo Luciani, Alberto Musso, Mario 
Porqueddu, Massimo Rostagno and Antonio Spilimbergo for helpful comments and discussions. 
Domenico Giannone started working on this project before joining the IMF. The views expressed 
here are those of the authors and do not necessarily represent those of the National Bureau of 
Economic Research, IMF, its Management and Executive Board, IMF policy.
At least one co-author has disclosed additional relationships of potential relevance for this research. 
Further information is available online at http://www.nber.org/papers/w32859
NBER working papers are circulated for discussion and comment purposes. They have not been 
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies 
official NBER publications.
© 2024 by Domenico Giannone and Giorgio Primiceri. All rights reserved. Short sections of text, 
not to exceed two paragraphs, may be quoted without explicit permission provided that full credit, 
including © notice, is given to the source.

The Drivers of Post-Pandemic Inflation
Domenico Giannone and Giorgio Primiceri
NBER Working Paper No. 32859
August 2024
JEL No. E30, E31, E32, E37, E52, E58
ABSTRACT
Post-covid inflation was predominantly driven by unexpectedly strong demand forces, not only in 
the United States, but also in the Euro Area. In comparison, the inflationary impact of adverse 
supply shocks was less pronounced, even though these shocks significantly constrained economic 
activity.  With output already weakened by these unfavourable supply conditions, any attempt by 
the European Central Bank to further mitigate the demand-driven inflationary pressures---to 
maintain inflation near its 2-percent target---would have severely hampered an already anaemic 
recovery.
Domenico Giannone
International Monetary Fund
700 19th Street
Washington, DC 20431
and CEPR
dgiannon2@gmail.com
Giorgio Primiceri
Department of Economics
Northwestern University
2211 Campus Drive
Evanston, IL 60208
and NBER
g-primiceri@northwestern.edu

The drivers of post-pandemic inﬂation*
Domenico Giannone†
Giorgio E. Primiceri‡
July 15, 2024. First version: May 2024
Abstract
Post-covid inﬂation was predominantly driven by unexpectedly strong demand forces,
not only in the United States, but also in the Euro Area. In comparison, the inﬂationary im-
pact of adverse supply shocks was less pronounced, even though these shocks signiﬁcantly
constrained economic activity. With output already weakened by these unfavourable supply
conditions, any attempt by the European Central Bank to further mitigate the demand-driven
inﬂationary pressures—to maintain inﬂation near its 2-percent target—would have severely
hampered an already anaemic recovery.
1
Introduction
The evolution of post-pandemic inﬂation has been remarkably similar in the United States (US)
and the Euro Area (EA). US inﬂation has accelerated in the ﬁrst half of 2021, it has reached its
peak in the second quarter of 2022, and it has been falling since. Inﬂation in the EA has followed
the very same path, only delayed by approximately six months. In this paper, we study the causes
of this high inﬂation episode—the ﬁrst of its kind since the Great Inﬂation of the 1970s—and the
trade-offs confronting the Federal Reserve (Fed) and the European Central Bank (ECB).
*We thank our discussant, Fernanda Nechio, an anonymous ECB referee, Philipp Hartmann, Jirka Slacalek, Carlo
Altavilla, Giacomo Carboni, Jacopo Cimadomo, Chris Erceg, Pierre-Olivier Gourinchas, Davide Furceri, Kamil Koval,
Michele Lenza, Matteo Luciani, Alberto Musso, Mario Porqueddu, Massimo Rostagno and Antonio Spilimbergo for
helpful comments and discussions. Domenico Giannone started working on this project before joining the IMF. The
views expressed here are those of the authors and do not necessarily represent those of the IMF, its Management and
Executive Board, or IMF policy.
†International Monetary Fund, University of Washington and CEPR
‡Northwestern University, CEPR and NBER

THE DRIVERS OF POST-PANDEMIC INFLATION
Figure 1: A simple AS-AD diagram.
Such similar inﬂation experiences across the Atlantic are unlikely to be mere coincidences.
In fact, we ﬁnd that inﬂation has been largely driven by demand forces in both regions. At the
beginning of the pandemic, both economies were knocked down by large negative supply and
demand shocks, severely depressing economic activity. Our empirical results suggest that, as
conditions began to recover, aggregate demand rebounded more rapidly than anticipated, out-
pacing aggregate supply and generating inﬂation. Figure 1 provides a graphical illustration of
this story using a simple diagram with aggregate demand (AD) and supply (AS) curves. Both
curves initially bounce to the left, and then move slowly back to their original position. But
the AD curve moves back faster than expected and overshoots its original position. This rapid
rebound of the AD curve may have been due to the possible combination of uncommonly ex-
pansionary ﬁscal policies and unexpectedly strong pent-up demand following the reopening
after the pandemic restrains. Another key contributing factor to the swift recovery in aggre-
gate demand might have been the unusually high degree of monetary policy accommodation of
inﬂationary pressures from all sources—including adverse supply shocks. Such unusual accom-
modation represents a deviation from the pre-covid conduct of monetary policy and, as such,
translates into an unexpectedly strong rebound of aggregate demand.
2

THE DRIVERS OF POST-PANDEMIC INFLATION
The result that inﬂation is mainly demand driven might seem at odds with a widely held view
that unfavourable supply shocks have played a major role for the run-up of inﬂation, especially
in Europe. But this popular narrative is difﬁcult to square with all the evidence. The easiest way
to understand why is to go back to the simple AD-AS diagram of ﬁgure 1. Notice that the AD
curve in the ﬁgure is quite ﬂat. It is important to realize that the slope of the AD curve is not an
exogenous object, but it depends on the systematic conduct of monetary policy. A ﬂat AD curve
is exactly what we should expect for economies with Central Banks that have established a strong
reputation of (near) inﬂation targeters, like the US and the EA. But if the demand curve is ﬂat,
left shifts in the supply curve depress output but cannot produce much inﬂation. For inﬂation
to climb, monetary policy must provide an unusually high degree of accommodation of these
adverse supply shocks, relative to its pre-covid conduct. Effectively, this extra accommodation—
along with all other expansionary demand shocks—causes an upward shift of the AD curve.
These simple arguments convey the essence of the intuition of why post-covid inﬂation must
have been largely fuelled by demand forces—a result that we obtain using a dynamic multivari-
ate statistical model, not simply the AD-AS diagram of ﬁgure 1. We use our statistical model
to also evaluate the policy trade-offs of the ECB. Speciﬁcally, we address the question: Despite
inﬂation primarily stemming from demand shocks, would it have been prudent for the ECB to
mitigate their impact on inﬂation? The answer to this question, of course, hinges on policy-
makers’ preferences for inﬂation versus output stabilization. We ﬁnd that striving to maintain
inﬂation close to the 2-percent target would have led to a cumulative GDP loss of roughly 4.5,
with economic activity in 2024 being 5 percent lower than actual. This is a signiﬁcant loss, given
that economic activity was already strained by adverse supply conditions.
Finally, we utilize the model to assess the prospects for inﬂation. At the time of writing, the
year-on-year headline HICP inﬂation in the EA is approximately 2.5 percent. Our model projec-
tions, corroborated by professional forecasters, suggest a positive outlook, anticipating a smooth
return to target in the coming quarters. Paraphs even more importantly, the ECB has not suffered
any signiﬁcant loss of credibility due to the recent inﬂation spike. In fact, our ﬁndings show that
the public believes that monetary policy has already returned to its pre-covid standards.
In the rest of the paper, we will explore all these issues in detail. But before moving to the
main body of the manuscript, we note that the recent run-up of inﬂation is an active area of
research. We will put our contribution in the context of this growing literature in section 4, after
discussing some of the details of our work.
3

THE DRIVERS OF POST-PANDEMIC INFLATION
2
Data and stylized facts
This section summarizes the dynamics of real activity and prices in the US and the EA since
the onset of the coronavirus pandemic. We organize the presentation of this empirical evidence
around three stylized facts.
Fact 1. The covid recession has been more severe in the EA than in the US, and the recovery
has been slower and more incomplete.
Fact 2. The evolution of headline inﬂation, instead, has been remarkably similar across the
Atlantic.
Fact 3. Total energy prices have also behaved very much alike in the US and the EA, although
the two components of energy prices, household and transportation energy, have evolved dif-
ferently in the two economies.
Figure 2 documents fact 1, by showing the evolution of real GDP and consumption expendi-
ture since 2018, both in the US and in the EA. To facilitate the comparison, all the variables are
plotted using a logarithmic scale and have been normalized to be equal to 0 in 2019:Q4. The ﬁg-
ure makes clear that the collapse of economic activity at the beginning of the pandemic has been
particularly pronounced in the EA, where GDP and consumption plummeted by roughly 16 and
18 percent relative to the end of 2019—approximately two-thirds more than in the US. Figure 2
also reports the pre-covid projections of the Fed, the ECB and the Survey of Professional Fore-
casters for GDP and consumption after 2020 (dotted and dashed lines).1 Notice that GDP and,
especially, consumption are still below these pre-covid projections in the EA. On the contrary,
the recovery has been considerably faster in the US.
Figure 3 provides support for fact 2. Panels (a) and (b) plot year-on-year inﬂation based on
the GDP and the consumption deﬂators, both in the US and in the EA. Panel (c) focuses on the
most widely monitored measure of EA inﬂation, based on the Harmonized Index of Consumer
Prices (HICP), and compares it to the US Consumer Price Index (CPI). To make such compari-
son more meaningful, CPI inﬂation in the US has been adjusted to exclude “Owners’ equivalent
rent of residences,” since the HICP in the EA does not comprise any rent imputation for owner
occupied houses. The data in the ﬁrst row of ﬁgure 3 tell a common story: The run-up of prices
has been delayed by a few quarters in the EA, relative to the US. But besides such delay, the
overall evolution of inﬂation has been remarkably similar in the two regions, especially if con-
1The annual projections are mapped into quarterly assuming a constant quarterly growth rate within each year.
4

THE DRIVERS OF POST-PANDEMIC INFLATION
2019
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
100 x log deviation from 2019:Q4
(a) US GDP
Actual
Survey of Professional Forecasters as of February 12, 2020
Fed Summary of Economic Projectos as of December 11, 2019
2019
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
100 x log deviation from 2019:Q4
(b) EA GDP
Actual
Survey of Professional Forecasters as of January, 24 2020
ECB Staff Macroeconomic Projections as of December 12, 2019
2019
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
100 x log deviation from 2019:Q4
(c) US Consumption
2019
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
100 x log deviation from 2019:Q4
(d) EA Consumption
Figure 2: Real GDP and consumption expenditure in the US and the EA. Sources: Data from Eurostat, the
European Central Bank, the Bureau of Economic Analysis, the Board of Governors of the Federal Reserve
System, and the Federal Reserve Bank of Philadelphia; accessed via Haver Analytics; computations by
authors.
5

THE DRIVERS OF POST-PANDEMIC INFLATION
2019
2020
2021
2022
2023
2024
0
2
4
6
8
10
percent change from year ago
(a) GDP deflator
US
EA
2019
2020
2021
2022
2023
2024
0
2
4
6
8
10
percent change from year ago
(b) Consumption deflator
2019
2020
2021
2022
2023
2024
0
2
4
6
8
10
percent change from year ago
(c) CPI / HICP
2019
2020
2021
2022
2023
2024
0
5
10
15
percent change from year ago
(d) CPI / HICP goods
2019
2020
2021
2022
2023
2024
0
5
10
15
percent change from year ago
(e) CPI / HICP services
Figure 3: Inﬂation in the US and the EA, based on several price indexes. Sources: Data from Eurostat, the
European Central Bank, the Bureau of Labor Statistics, and the Bureau of Economic Analysis; accessed
via Haver Analytics; computations by authors.
trasted with the different dynamics of economic activity during the same period. In addition,
notice that HICP inﬂation was already above 5 percentage points at the end of 2021, before the
outbreak of the Ukrainian war. Panels (d) and (e) corroborate the similarity of the US and EA
inﬂation experience, by distinguishing between inﬂation for consumption goods and services.
This distinction may be important because goods inﬂation has peaked earlier and higher than
services inﬂation, as it is well known. But the second row of ﬁgure 3 shows that these dynamics
too are common to the two regions across the Atlantic.
Figure 4 demonstrates fact 3. Panel (a) shows that energy-price inﬂation has gone up and
down in tandem in the US and the EA. It has peaked slightly higher and fallen with a delay in
the EA. But this discrepancy seems relatively small, compared to the size of the rise and fall of
energy-price inﬂation since 2020. Panel (b) of ﬁgure 4 plots year-on-year inﬂation excluding en-
ergy, which exhibits the usual similar but phase-shifted behaviour in the US and the EA. Despite
these similarities, the second row of ﬁgure 4 highlights some heterogeneity in the behaviour of
the two components of energy prices. Panel (c) shows that the price of household-utilities en-
ergy has increased a lot more in the EA than in the US, as also noted by Tenreyro (2023). This
pattern is surely due, at least in part, to the greater inﬂuence of the Ukrainian war on European
electricity and gas prices. On the contrary, the retail price of transportation fuels in panel (d)
6

THE DRIVERS OF POST-PANDEMIC INFLATION
2019
2020
2021
2022
2023
2024
-20
-10
0
10
20
30
40
percent change from year ago
(a) CPI / HICP  energy
US
EA
2019
2020
2021
2022
2023
2024
0
2
4
6
8
percent change from year ago
(b) CPI / HICP ex energy
2019
2020
2021
2022
2023
2024
-20
0
20
40
60
percent change from year ago
(c) CPI / HICP  household energy
2019
2020
2021
2022
2023
2024
-20
0
20
40
60
percent change from year ago
(d) CPI / HICP transportation energy
Figure 4: Energy-price inﬂation in the US and the EA, and CPI/HICP inﬂation excluding energy. Sources:
Data from Eurostat, the European Central Bank, and the Bureau of Labor Statistics; accessed via Haver
Analytics; computations by authors.
displays a considerably larger swing in the US, compared to the EA. As it turns out, the differ-
ences between the behaviour of household- and transportation-energy inﬂation almost exactly
balance out when considering the aggregate price of energy in panel (a).
In the rest of this paper, we investigate the drivers of these macroeconomic dynamics, fo-
cusing on the causes of the inﬂation surge. As a preview, we ﬁnd that the worse performance of
economic activity in the EA (fact 1) is due to a higher incidence of negative supply shocks. How-
ever, these supply shocks have had little impact on inﬂation, whose run-up (fact 2) has been
largely driven by unusually strong demand forces, both in the US and the EA. Finally, the rapid
increase of energy prices (fact 3) is a consequence of strong demand, not a primitive cause of
inﬂation. Understanding the relative contributions of demand and supply shocks is important
for the design of stabilization policies. The conventional view, grounded in monetary theory,
is that Central Banks should “look through supply shocks,” but suppress demand disturbances.
In the second part of the paper, we quantify the extent to which leaning against demand would
have hampered the recovery.
7

THE DRIVERS OF POST-PANDEMIC INFLATION
3
Demand- or supply-driven inﬂation?
To study the drivers of macroeconomic dynamics, we estimate the following Structural Vector
Autoregression (SVAR) model,
yt = c + B1yt−1 + ... + Bpyt−p + Γεt,
(1)
where yt is an n×1 vector of macroeconomic variables. They are assumed to evolve as a function
of their own lagged values (yt−1, ..., yt−p) and an n×1 vector of economically interpretable shocks
(εt). The vector c and the matrices B1, ..., Bp and Γ are objects of conformable dimensions that
consist of estimable parameters.
We begin by focusing on the simplest speciﬁcation of (1) that can speak to facts 1 and 2 of the
previous section. More speciﬁcally, we set n = 2 and let yt only include (the logarithm of) real
GDP and the CPI (in the case of the US) or the HICP (for the EA). We identify demand and sup-
ply disturbances using sign restrictions (Uhlig, 2005; Rubio-Ramirez, Waggoner and Zha, 2010),
assuming that demand shocks generate positive co-movement between real activity and prices,
while the co-movement induced by supply shocks is negative. In essence, supply shocks are
disturbances that create a trade-off between output and inﬂation stabilization, while demand
shocks do not.2 The model is estimated using four lags (p = 4) and quarterly data from 1997:Q1
to 2019:Q4. The analysis starts in 1997 because of data availability for the EA, and because there
is evidence of a change in US inﬂation dynamics since the 1990s (Cogley, Primiceri and Sar-
gent, 2010; Del Negro, Lenza, Primiceri and Tambalotti, 2020). The estimation sample ends in
2019 because we want to keep a clear distinction between pre- and post-pandemic dynamics.
In addition, macroeconomic volatility has been very elevated during the acute phase of the pan-
demic, and the inclusion of these data might distort inference (Lenza and Primiceri, 2022). To
address the curse of dimensionality due to the limited sample length, we adopt Bayesian infer-
ential methods with the Minnesota and the sum-of-coefﬁcients priors, following the technical
implementation of Giannone, Lenza and Primiceri (2015). Importantly, the sum-of-coefﬁcients
prior helps reducing the estimation uncertainty of the model deterministic component docu-
mented by Bergholt et al. (2024).
Using the model estimated on the 1997-2019 sample, we decompose the behaviour of out-
put and inﬂation since 2020:Q1 into demand- and supply-driven components. The results of
2Interestingly, Madeira, Madeira and Santos Monteiro (2023) document that supply shocks—identiﬁed using sign
restrictions like ours—increase dissent among FOMC voting members. Demand disturbances, instead, reduce it.
8

THE DRIVERS OF POST-PANDEMIC INFLATION
(a) US GDP
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
15
100 x log deviation from 2019:Q4
(b) EA GDP
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
15
100 x log deviation from 2019:Q4
(c) US CPI
2020
2021
2022
2023
2024
-5
0
5
10
100 x log change relative to year ago
Actual
Model forecast as of 2019:Q4
Demand
Supply
(d) EA HICP
2020
2021
2022
2023
2024
-5
0
5
10
100 x log change relative to year ago
Actual
Model forecast as of 2019:Q4
Demand
Supply
Figure 5: Historical decomposition of GDP and inﬂation dynamics. Sources: Data from Eurostat, the
European Central Bank, the Bureau of Labor Statistics, and the Bureau of Economic Analysis; accessed
via Haver Analytics; computations by authors.
this historical decomposition are reported in ﬁgure 5, for both the US and the EA. In all four
panels, the solid line corresponds to the actual realization of the data, while the dashed-dotted
line represents the model forecast for the corresponding variable as of 2019:Q4. It is essential
to stress that the GDP forecasts in panels (a) and (b) are not measures of potential output. This
is because supply disruptions since 2020 have certainly hampered the productive capacity of
both economies, reducing potential output relative to these pre-covid output forecasts. As a
consequence, the distance between actual GDP and these pre-covid projections cannot be in-
terpreted as an output gap. For example, the fact that actual GDP in the EA has been below the
dashed-dotted line in ﬁgure 5b does not at all imply a persistently negative output gap in the
“New-Keynesian sense,” which puts downward pressure on inﬂation. Instead, the discrepancy
between these two lines is simply the forecast error—the extent to which the data have turned
out to be different from the pre-pandemic model-based prediction. The estimated model in-
fers the shares of these forecast errors that have been driven by unexpected changes in demand
(yellow bars) or supply conditions (green bars).
Panel (a) illustrates that demand factors have boosted economic activity since 2021, while
supply shocks have been a substantive drag on output. When it comes to US inﬂation, more
9

THE DRIVERS OF POST-PANDEMIC INFLATION
than half of its rise and fall can be attributed to demand disturbances, as shown in panel (b). The
ﬁgure paints a similar picture for the EA, with the difference that supply factors exert a larger neg-
ative contribution to the EA GDP. On the contrary, demand shocks play an even more dominant
role for inﬂation in the EA, relative to the US. Adverse supply shocks contribute substantially to
EA inﬂation only in 2022, i.e. during the ﬁrst year of the Russian invasion of Ukraine.
In simpler terms, at the onset of the pandemic, both economies were severely impacted by
signiﬁcant negative supply and demand shocks, which drastically reduced economic activity. As
conditions started to improve, aggregate demand rebounded faster than predicted, and aggre-
gate supply slower than expected. But our results suggest that the former has contributed more
to the surge in inﬂation.
This ﬁnding might seem surprising and deserves further discussion, given the popular nar-
rative that negative supply forces have plagued the EA economy and are largely responsible for
the rise of inﬂation. We will explain the intuition of our result about the major role of demand
factors for EA inﬂation in the next section. For now, we stress that this is a robust ﬁnding. It holds
in many alternative speciﬁcations of the model with (i) other measures of real activity and prices
(appendix B); (ii) the addition of energy prices (section 5 and appendix C); (iii) the addition of
monetary variables (section 6 and appendix D); (iv) the explicit distinction between the price
and consumption of goods and services (appendix B).
4
Understanding the dominant role of demand factors for post-covid
inﬂation
This section explains how to interpret the ﬁnding that demand factors have played such a dom-
inant role for the rise of post-covid inﬂation, including, if not especially, in the EA.
To begin, we highlight an implicit assumption underlying the supply-demand decomposi-
tion of ﬁgure 5. The approach of section 3, in fact, assumes that covid has not altered the
transmission mechanism of demand and supply disturbances, although the size and relative
frequency of these disturbances might have changed during the pandemic. This is a standard
assumption for analyses based on time-series models, and we will explore its role for our re-
sults in the second part of this section. But if we believe this assumption, we can use the model
estimated with data from 1997 to 2019 to infer the slopes of the aggregate demand and supply
10

THE DRIVERS OF POST-PANDEMIC INFLATION
-10
-5
0
5
GDP: 100 x log deviation from trend
-2
0
2
4
6
8
10
12
inflation: percent change relative to year ago
US
AD (2019)
AS (2019)
AD (2022)
AS (2022)
2020
2021
2022
2023
-10
-5
0
5
GDP: 100 x log deviation from trend
-2
0
2
4
6
8
10
12
inflation: percent change relative to year ago
EA
AD (2019)
AS (2019)
AD (2022)
AS (2022)
2020
2021
2022
2023
Figure 6: AD and AS curves in the US and the EA. Sources: Data from Eurostat, the European Central
Bank, the Bureau of Labor Statistics, and the Bureau of Economic Analysis; accessed via Haver Analytics;
computations by authors.
curves determining the equilibrium also after 2019.3
Figure 6 depicts the estimated AD and AS curves, in the US and the EA. Initially, they cross
at a level of output’s deviation from trend normalized to 0, and inﬂation equal to 2 percentage
points. The ﬁgure also reports the average level of output’s deviations from its pre-covid trend
and inﬂation in 2020, 2021, 2022 and 2023, from ﬁgure 5. The ﬁrst thing to notice is that the AD
curve is quite ﬂat in both economies, and more so in the EA than in the US. This characteristic of
the AD curve should not be surprising, since it is due to the Fed and the ECB’s strong reputation
of (near) inﬂation targeters. To understand why being an effective inﬂation targeter results in
a ﬂat AD, think of the extreme situation of a Central Bank that never lets inﬂation deviate from
a 2-percent target, no matter the cost in terms of output deviations from trend. The resulting
slope of the AD curve would be exactly zero. In addition, in such an extreme case, supply shocks
shifting the AS curve would have a large impact on real activity, but no effect on inﬂation. And
the only way to experience higher inﬂation would be through an upward shift in the AD curve,
corresponding to demand disturbances that are either accommodated by the Central Bank, or
demand shocks that are directly engineered by the Central Bank through unexpected monetary
expansions.
The estimated AD curves depicted in ﬁgure 6 for the US and the EA are not as ﬂat as in our
extreme example of strict inﬂation targeting that we have just described, but they are not far
from that benchmark. For example, the ECB has a single mandate of price stability, and it is
3The slope of the demand curve is given by the relative change of inﬂation and GDP in response to supply shocks.
Similarly, the slope of the supply curve corresponds to the relative change of inﬂation and GDP in response to demand
shocks. To depict the static version of these curves in ﬁgure 5, we use the relative responses of year-on-year inﬂation
and GDP deviations from trend at a 1-year horizon.
11

THE DRIVERS OF POST-PANDEMIC INFLATION
intuitive that this priority has resulted into a fairly ﬂat AD curve in the EA until 2019. If this
curve has been as ﬂat also during the pandemic, the negative supply shocks experienced by
the EA economy since 2020 have likely had a large contractionary effect on real activity, but a
limited impact on inﬂation. This intuition is consistent with the empirical ﬁndings of ﬁgure 5.
Similarly, the only way for inﬂation to rise to the levels observed in 2022 is for the AD curve
to shift upwards, as shown by the dashed yellow line in ﬁgure 6, which explains our result that
demand factors have played a dominant role for post-pandemic inﬂation.
The intuition that we have just provided leverages the assumption that the transmission
mechanism of demand and supply shocks, and thus the slopes of the AD and AS curves, have
not changed after covid. But what if they did? Would our interpretation of the empirical ﬁndings
of section 3 be different? The answer to this question is “not a whole lot.” Let us understand why
in the context of ﬁgure 6. First, notice that a change in the slope of the AS curve after 2020 (Eg-
gertsson and Benigno, 2023) would not make much difference, because a shift of the AD curve
would still be required to explain the observed high level of inﬂation.
But what about a change in the slope of the AD curve? Mechanically, a steeper AD curve since
2021 could rationalize the observed dynamics of real activity and inﬂation with smaller demand
shocks, i.e. smaller shifts of the AD. But a steepening of the AD curve would correspond to a
weakening of the monetary policy systematic reaction to inﬂation, possibly reﬂecting “shocks
to the preferences of the monetary authority, perhaps due to [...] shifts in the relative weight
given to unemployment and inﬂation” (Christiano, Eichenbaum and Evans, 1999, pp. 71-72).
Therefore, for the purpose of interpreting the recent inﬂation run-up, a steepening of the AD
curve is essentially the same as its upward shift, since both cases involve monetary policy ac-
commodation of inﬂationary pressures. Put differently, compared to the pre-covid conduct of
monetary policy, both an AD curve becoming steeper or shifting upwards translate into unusu-
ally strong demand forces, the same forces ultimately driving inﬂation.4 In section 7, we will
discuss the extent to which such accommodation of the strong post-covid inﬂationary pressures
has represented an appropriate conduct of monetary policy.
4Cuciniello (2024) uses ﬁnancial daily data to infer the public perception of the ECB responsiveness to inﬂation,
and how it has changed over time. He ﬁnds that, if anything, the perceived short-run ECB responsiveness to inﬂation
has increased since 2022, not diminished. This result speaks against a possible rotation of the AD curve and in favour
of a shift.
12

THE DRIVERS OF POST-PANDEMIC INFLATION
4.1
Understanding the differences from the existing literature
Several studies have attempted to quantify the relative roles of demand and supply factors in
explaining inﬂation dynamics since the outbreak of the coronavirus pandemic.
Harding et al. (2022), Benigno and Eggertsson (2023), Jord`a and Nechio (2023) and Erceg et
al. (2024) discuss how such decomposition might be affected by the non-linearity of the sup-
ply curve. In their work, the pandemic brought about a series of large shocks that moved the
equilibrium of the economy to region characterized by a steeper supply curve. Relative to these
papers, we study the role of the slope of the demand curve, which depends on the monetary
policy reaction function.
Gonc¸alves and Koester (2022) and Lane (2022) estimate bi-variate vector autoregressive (VAR)
models like ours separately for many good and service categories, using EU data and a method-
ology developed by Shapiro (2022 and 2024) for the US economy. Their ﬁndings suggest that
demand and supply factors have had a comparable role in explaining inﬂation dynamics. These
studies, however, might underestimate the role of demand, since the sectoral demand curves
are less ﬂat than at the aggregate level, given that monetary policy responds to aggregate, not
sectoral, inﬂationary pressures.
Banbura, Bobeica and Martines Hernandez (2024) ﬁnd a large contribution of supply shocks
to EA inﬂation. Differently from us, their VAR includes a richer set of variables and several struc-
tural shocks. But their results are likely to overstate the inﬂuence of supply factors because their
model is saturated with both supply indicators and supply disturbances, and it is estimated us-
ing the approach of Korobilis (2022) in which few common shocks drive all the reduced-form
residuals. De Santis (2024), Ascari, Bonam and Smadu (2024), and Bai et al. (2024) highlight
the impact of global supply chain bottlenecks and disruptions for EA and US inﬂation. Yet,
their impulse responses do not adequately account for the effect of demand shocks on supply
chain pressure indexes. This appears inconsistent with the extensive literature cited in section
5, which documents the strong positive correlation between economic activity and commod-
ity prices, shipping costs, and delivery times. Furthermore, the model speciﬁcations in these
papers do not incorporate priors that discipline the behaviour of the deterministic component
and limit its estimation uncertainty (Giannone, Lenza and Primiceri, 2019; Bergholt et al., 2024).
As argued by Bergholt et al. (2024), this omission can signiﬁcantly affect the results of historical
decomposition analyses.5
5De Santis (2024) utilizes the dummy-initial observation prior, but this prior is ineffective at correcting the prob-
lem highlighted by Bergholt et al. (2024) if imposed on the coefﬁcients of a VAR speciﬁed in log levels (Giannone et
13

THE DRIVERS OF POST-PANDEMIC INFLATION
The papers closest to our work are Ascari et al. (2023), Bergholt et al. (2024), Faria e Castro
(2024), and Garcia-Revelo, Levieuge and Sahuc (2024), who point to demand shocks as central
factors for the rise of inﬂation in the US and the EA. Similarly, International Monetary Fund
(2022) and Koch and Noureldin (2024) show that the output and inﬂation forecast errors in many
advanced and emerging economies, relative to the predictions of the World Economic Outlook,
display a positive correlation, consistent with a stronger than anticipated demand recovery.
Our results on the sources of inﬂationary pressures are consistent with theirs. In addition,
we explain the intuition of these results, and why a chief role for demand disturbances is in-
evitable if the AD curve is as ﬂat as we would expect for Central Banks who are credible (near)
inﬂation targeters. Our results are also broadly in line with those of Comin, Johnson and Jones
(2023), Bocola et al. (2024) and Gagliardone and Gertler (2024), which we will discuss in sec-
tion 6, and Di Giovanni et al. (2022). The latter quantify the relative role of demand and supply
shocks based on a calibrated two-period multi-sector model with perfectly competitive factors
and good markets. Their analysis is limited to the cumulative inﬂation experience until 2021:Q4,
without modelling dynamics. Nevertheless, their calibrated closed-economy model attributes
more than 50 percent of the surge of inﬂation to demand forces, even in the EA.6 In subsequent
iterations of their work, Di Giovanni et al. (2023a and b) ﬁnd an even larger contribution of ag-
gregate demand shocks, fully consistent with our results. In addition, these articles decompose
demand disturbances into domestic and global components, like Ha et al. (2023), Aastveit et al.
(2024) and Forbes, Ha and Kose (2024), something that we do not attempt to do in this paper.
Guerrieri et al. (2024) present a comprehensive report on the behaviour of inﬂation in the US
and the EA. These authors study the price response to monetary policy and oil-supply shocks,
documenting that the former is more uniform across sectors than the latter. But this study does
not divide the recent dynamics of inﬂation into demand- and supply-driven components. Relat-
edly, Rubbo (2024) divides US inﬂation into components driven by industry-speciﬁc and aggre-
gate shocks. She ﬁnds that industry-speciﬁc demand and supply disturbances were key determi-
nants of inﬂation during the early phase of the pandemic, but aggregate factors have dominated
its dynamics since the beginning of 2021.
al., 2019). Bai et al. (2024) do not use any of the priors recommended by Bergholt et al. (2024), but they check the
robustness of their results using the prior-robust approach proposed by Giacomini and Kitagawa (2021).
6The open-economy version of their model attributes less than one half of EA inﬂation to domestic shocks. How-
ever, this share does not speak to the question whether inﬂation is demand or supply driven, because it is based on
the counterfactual assumption that “domestic goods demanded by Euro Area households can be substituted with
the goods produced abroad, and these regions (the US and RoW) have not been hit by expansionary demand shocks
or contractionary labor supply shocks, thus keeping prices of their goods (which are reﬂected in Euro Area import
prices) lower than domestic prices in the Euro Area” (Di Giovanni et al., 2022, pp. 48).
14

THE DRIVERS OF POST-PANDEMIC INFLATION
Bernanke and Blanchard (2023) evaluate the contribution of product- and labour-market
shocks for US post-covid inﬂation. Their approach has been applied by Arce et al. (2024) and
Vilmi and Oinonen (2024) to EA data, and by Menz (2024), De Walque and Lejeune (2024), Pisani
and Tagliabracci (2024), Aldama, Le Bihan and Le Gall (2024), Ghomi, Hurtado and Montero
(2024), Bonam, Hebbink and Pruijt (2024), Haskel, Martin and Brandt (2023), Bounajm, Roc and
Zhang (2023), and Nakamura at al. (2024) to data from Germany, Belgium, Italy, France, Spain,
the Netherlands, the UK, Canada and Japan. All these articles, whose results are summarized
by Bernanke and Blanchard (2024), ﬁnd a large impact of food and energy prices on aggregate
inﬂation. Similar insights emerge from the analysis of EA data by Lane (2022), and from the study
of the behaviour of headline and core inﬂation in 21 countries by Dao et al. (2024), who build
on earlier work of Ball, Leigh and Mishra (2022) for the US and Dao et al. (2023) for the EA. But
they all treat food and energy prices, as well as supply shortages, as exogenous variables, making
it difﬁcult to map their results into a demand-supply decomposition useful for policy analysis.
In the next section we will show that their conclusions are not necessarily in conﬂict with ours,
because energy prices are largely driven by the same ﬂuctuations in aggregate demand that have
ultimately generated inﬂation.
5
What about energy prices?
A widely held view is that the run-up of EA inﬂation was largely driven by supply disturbances
and, in particular, by the rise in energy and food prices. For example, Arce et al. (2023) estimate
that roughly two-thirds of the EA inﬂation deviations from the 2-percent target was due to the
behaviour of energy and food prices. This result is qualitatively similar to that of Bernanke and
Blanchard (2023) for the US, but it appears in contrast with our empirical ﬁnding that demand
factors played a more important role. How can we reconcile these seemingly conﬂicting views?
The short answer is that these two views are not necessarily in contrast with each other. In
fact, energy (and food) prices are largely endogenous to the world business cycle, and not its
main driver or the main primitive cause of post-covid inﬂation. The fact that ﬂuctuations in en-
ergy prices—and, more generally, in commodity prices, shipping costs, delivery times, etc.—are
strongly positively correlated with economic activity is widely documented in the literature, to
the point that these variables are often used to construct real time indexes of economic con-
ditions (for example, see Kilian, 2009, Kilian and Zhou, 2018, Baumeister and Hamilton, 2019,
Alquist, Bhattarai and Coibion, 2020, Delle Chiaie, Ferrara and Giannone, 2022, Baumeister and
15

THE DRIVERS OF POST-PANDEMIC INFLATION
Korobilis, 2022, and Bernanke and Blanchard, 2023). Therefore, even though energy (and food)
prices have increased substantially since 2021, and have thus played a large role for overall inﬂa-
tion in an accounting or reduced-form sense, it is mostly because both the US and the EA GDP
have bounced back from the collapse of the ﬁrst half of 2020, as also argued by Bernanke and
Blanchard (2023). The truly exogenous movements in energy prices, those for instance related
to the Russian invasion of Ukraine, were limited in comparison.
To substantiate these points, and to show the robustness of our results, in this section we es-
timate an augmented version of our model that explicitly includes energy prices. More precisely,
we replace headline inﬂation in our baseline model with two series measuring energy and non-
energy prices. In this 3-variable model, we can now identify three separate shocks: (i) demand
shocks, which are assumed to move GDP, energy and non-energy prices in the same direction;
(ii) non-energy-supply shocks, which are assumed to move non-energy prices in the opposite di-
rection relative to GDP and energy prices; (iii) and energy-supply shocks, which are assumed to
move energy prices in the opposite direction of GDP. Like in section 3, we estimate the model us-
ing data from 1997 to 2019, and then use the estimated parameters to decompose the observed
evolution of the three variables in the model after 2019.
Before presenting our estimation results, it is important to recognize that the evolution of
energy prices in a region of the world does not depend only on economic conditions locally, but
also abroad. The way our model catches disturbances in the rest of the world depends on the
extent to which they are correlated with those at home. Suppose that demand booms abroad, as
an example. If this boom is global—therefore, by deﬁnition, correlated with domestic demand—
it will be captured by shocks (i), because it stimulates both real activity and energy prices. If the
boom abroad is instead uncorrelated with domestic demand, its adverse effect on the home
economy through the hike in energy prices is captured by shocks (iii).
Figure 7 presents the results of this decomposition. The ﬁrst thing to notice is that the in-
crease in energy inﬂation since 2021 is largely driven by demand shocks, which is broadly con-
sistent with the ﬁndings of Baumeister (2023) concerning oil prices. As we have stressed in the
previous paragraph, such a large contribution of demand disturbances to energy inﬂation also
captures the role of unexpectedly strong global demand, not just domestic, given the correlation
of the two. In comparison, the contribution of energy-supply shocks to the evolution of energy
inﬂation is limited, although it reaches its peak in the ﬁrst quarter of 2022, around the start of
the Russian invasion of Ukraine.
Second, energy-supply shocks play a sizable negative role for real activity, as expected, es-
16

THE DRIVERS OF POST-PANDEMIC INFLATION
(a) US GDP
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
15
100 x log deviation from 2019:Q4
(b) EA GDP
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
15
100 x log deviation from 2019:Q4
(c) US CPI ex energy
2020
2021
2022
2023
2024
0
2
4
6
8
100 x log change relative to year ago
(d) EA HICP ex energy
2020
2021
2022
2023
2024
0
2
4
6
8
100 x log change relative to year ago
(e) US CPI energy
2020
2021
2022
2023
2024
-50
-25
0
25
50
percent change relative to year ago
Actual
Model forecast as of 2019:Q4
Demand
Non-energy supply
Energy supply
(f) EA HICP energy
2020
2021
2022
2023
2024
-50
-25
0
25
50
percent change relative to year ago
Actual
Model forecast as of 2019:Q4
Demand
Non-energy supply
Energy supply
Figure 7: Historical decomposition of GDP, non-energy and energy inﬂation dynamics. Sources: Data
from Eurostat, the European Central Bank, the Bureau of Labor Statistics, and the Bureau of Economic
Analysis; accessed via Haver Analytics; computations by authors.
17

THE DRIVERS OF POST-PANDEMIC INFLATION
pecially in the EA. Finally, the contribution of energy-supply shocks to inﬂation dynamics is
substantially smaller than that of demand disturbances, which conﬁrms our baseline ﬁndings
of section 3. Among other things, this result casts doubts on the narrative that the early, strong
recovery in the US has boosted energy prices worldwide, with negative repercussions on inﬂa-
tion in other regions, such as the EA. These developments are captured as energy-supply shocks
in the EA model. According to ﬁgure 7, they might have contributed to lowering economic ac-
tivity in the EA, but were not a major driver of EA inﬂation. Appendix C documents that these
insights continue to hold in a more complex model that distinguishes between household- and
transportation-energy prices.
6
The role of monetary policy
Our main result is that demand factors have played a crucial role in the recent run-up of inﬂa-
tion, both in the US and in the EA. The SVARs of sections 3 and 5, however, conﬂate monetary
and non-monetary demand disturbances into a single shock. Therefore, these models cannot
determine if the unexpected surge in demand after 2020 was due to an unusually accommoda-
tive conduct of monetary policy, relative to pre covid, or to other forces, such as those related to
ﬁscal policy or pent-up demand.
To study this question, we augment our baseline model with a measure of interest rates that
can capture the monetary policy stance. This exercise is thorny because the main US policy
rate—the federal funds rate (FFR)—has been stuck at the zero lower bound for many years since
2009. For this reason, we have opted to extend the model with the 1-year Treasury rate instead
of the FFR. Swanson and Williams (2014) argue that the 1- and 2-year Treasury yields appeared
surprisingly unconstrained until 2010, although they had become more constrained since 2011.
Consequently, the dynamics of the 1-year Treasury yield might not fully capture the effect of the
non-conventional policy measures implemented by the Fed during the early 2010s.7 This is a po-
tential limitation, but appendix D shows that the results in this section are robust to estimating
the model with FFR data that do not include the zero lower bound period. Short-term interest
rates in the EA budged below zero in the 2010s and were thus less constrained by the zero lower
bound. Nevertheless, we have chosen to use a 1-year rate for the EA as well, for symmetry with
7It is unclear in what direction this issue might distort our results on the importance of monetary policy shocks for
post-covid inﬂation. In fact, the reduced sensitivity of the 1-year rate to the state of the economy during part of the
estimation sample implies that we might underestimate the size of the monetary shocks after 2020, but overestimate
their impact. These two possible biases have an opposite sign.
18

THE DRIVERS OF POST-PANDEMIC INFLATION
the US, opting for the 1-year Euribor since it is available for the entire duration of our sample.
In this three-variable SVAR, we identify three types of disturbances: (i) demand shocks, which
are assumed to move GDP, prices and nominal interest rates in the same direction; (ii) supply
shocks, which are assumed to move GDP and prices in opposite directions; and (iii) monetary
policy shocks, which are assumed to move nominal interest rates in the opposite direction of
GDP and prices. The restriction on the sign of the interest rate to identify monetary policy shocks
is imposed for four consecutive periods, because we wish to identify meaningful, not just occa-
sional, deviations from the past conduct of monetary policy. As usual, we estimate the model
using data from 1997 to 2019, and then decompose the observed variation in the data after 2020.
The output of this decomposition is depicted in ﬁgure 8. The introduction of interest rates
into the model does not change the overall message of the paper that demand factors largely ex-
plain the behaviour of inﬂation. However, we can now gauge the relative role of the two demand
shocks—monetary and non-monetary demand disturbances. Panel (e) and (f) show that most
of the increase in interest rates was driven by non-monetary demand shocks in both regions. On
the contrary, monetary policy shocks have contributed negatively to the behaviour of interest
rates since early 2021, suggesting that both the Fed and the ECB have deviated from their pre-
2020 rule by keeping rates unusually low. Panels (a) and (b) make clear that these deviations,
i.e. monetary policy shocks, have helped GDP recover, especially in the EA. But this faster re-
covery entails a cost, as evident from panels (c) and (d). These expansionary monetary shocks
have played a sizable role in the run-up of inﬂation, a comparable one to that of non-monetary
demand disturbances. A related result on the importance of monetary policy shocks for the
increase of US inﬂation has been obtained by Comin et al. (2023). They use a nonlinear DSGE
model to argue that the impact of loose monetary policy by the Fed in 2021 was ampliﬁed by con-
straints on the economy productive capacity. Similarly, Bocola et al. (2024) and Gagliardone and
Gertler (2024) ﬁnd that accommodative monetary policy was a key driver of the post-pandemic
surge in US inﬂation.
7
The big elephant in the (ECB Governing Council) room
The EA economy has been subject to large unfavourable supply shocks since 2020, but these
shocks alone cannot explain the behaviour of inﬂation. Instead, according to our results, post-
covid inﬂation has been fuelled by surprisingly strong demand forces—a combination of un-
commonly expansionary ﬁscal policies, unexpectedly strong pent-up demand following the pan-
19

THE DRIVERS OF POST-PANDEMIC INFLATION
(a) US GDP
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
15
100 x log deviation from 2019:Q4
(b) EA GDP
2020
2021
2022
2023
2024
-20
-15
-10
-5
0
5
10
15
100 x log deviation from 2019:Q4
(c) US CPI
2020
2021
2022
2023
2024
-5
0
5
10
100 x log change relative to year ago
(d) EA HICP
2020
2021
2022
2023
2024
-5
0
5
10
100 x log change relative to year ago
(e) US interest rate
2020
2021
2022
2023
2024
-4
-2
0
2
4
6
percentage points
Actual
Model forecast as of 2019:Q4
Monetary
Non-monetary demand
Supply
(f) EA interest rate
2020
2021
2022
2023
2024
-4
-2
0
2
4
6
percentage points
Actual
Model forecast as of 2019:Q4
Monetary
Non-monetary demand
Supply
Figure 8: Historical decomposition of GDP, inﬂation and the 1-year interest rate dynamics. Sources:
Data from Eurostat, the European Central Bank, the Bureau of Labor Statistics, the Bureau of Economic
Analysis, and the Board of Governors of the Federal Reserve System; accessed via Haver Analytics; com-
putations by 

[... текст обрезан, всего 87613 символов ...]
