---
title: **Classical time-varying FAVAR models – estimation, forecasting and structural analysis**
type: paper
source_pdf: raw/papers/Eickmeier_Classical time-varying FAVAR models - estimation, forecasting and structural analysis_2011.pdf
converted: 2026-07-26
---



# **Classical time-varying FAVAR models – estimation, forecasting and structural analysis** 

# Sandra Eickmeier 

(Deutsche Bundesbank) 

# Wolfgang Lemke 

(European Central Bank and Deutsche Bundesbank) 

# Massimiliano Marcellino 

(European University Institute, Florence, Università Bocconi, Milano and CEPR) 

# Discussion Paper 

# Series 1: Economic Studies 

# No 04/2011 

Discussion Papers represent the authors’ personal opinions and do not necessarily reflect the views of the Deutsche Bundesbank or its staff. 

**Editorial Board:** Klaus Düllmann Frank Heid Heinz Herrmann Karl-Heinz Tödter 

Deutsche Bundesbank, Wilhelm-Epstein-Straße 14, 60431 Frankfurt am Main, Postfach  10 06 02, 60006 Frankfurt am Main 

Tel +49  69 9566-0 Telex within Germany  41227, telex from abroad  414431 

Please address all orders in writing to: Deutsche Bundesbank, 

Press and Public Relations Division, at the above address or via fax  +49 69 9566-3077 

Internet http://www.bundesbank.de 

Reproduction permitted only if source is stated. 

ISBN  978-3–86558–692–6 (Printversion) ISBN  978-3–86558–693–3 (Internetversion) 

#### **Abstract** 

We propose a classical approach to estimate factor-augmented vector autoregressive (FAVAR) models with time variation in the factor loadings, in the factor dynamics, and in the variance-covariance matrix of innovations. When the time-varying FAVAR is estimated using a large quarterly dataset of US variables from 1972 to 2007, the results indicate some changes in the factor dynamics, and more marked variation in the factors' shock volatility and their loading parameters. Forecasts from the time-varying FAVAR are more accurate than those from a constant parameter FAVAR for most variables and horizons when computed insample, for some variables in pseudo real time, mostly financial indicators. Finally, we use the time-varying FAVAR to assess how monetary transmission to the economy has changed. We find substantial time variation in the volatility of monetary policy shocks, and we observe that the reaction of GDP, the GDP deflator, inflation expectations and long-term interest rates to an equally-sized monetary policy shock has decreased since the early-1980s. 

**JEL** : C3, C53, E52 

**Key Words** : FAVAR, time-varying parameters, monetary transmission, forecasting 

#### **Non-technical summary** 

The recent macroeconometric literature has seen an increasing interest in the application of factor-augmented vector autoregressive (FAVAR) models for forecasting and structural analysis. These models provide a means to exploit large information sets and handle the omitted-variable problem often encountered in standard small-scale vector autoregressive (VAR) models. FAVARs model a large number of variables as the sum of a common component and an idiosyncratic component. The common component of a variable is the product of a few common factors, representing the main driving forces underlying most economic variables, and variable-specific factor loadings. The factors are assumed to follow a VAR process. The parameters are typically assumed to be constant over time in this literature. 

Another recent strand of literature has focused on small models with time-varying parameters, to explicitly take into consideration the changing sources of economic fluctuations, i.e. changes in the sizes of shocks and in their transmission to the economy. This literature therefore meets concerns about structural changes in the economy stemming from sources such as financial deepening, globalization or institutional changes. 

A few papers have attempted to combine the FAVAR and the time-varying parameter approaches, introducing FAVAR models with time-varying parameters, hence combining the benefits of using lots of variables and allowing for a time-varying model structure. All existing contributions use Bayesian procedures for estimation. Instead, in this paper we propose a fully classical approach to estimating a FAVAR model with time-varying parameters. Our time-varying version is fairly flexible, as it can accommodate smooth changes in the factor loadings, in the autoregressive coefficients of the factor VAR, in the contemporaneous relationships between the factors, and in the volatility of the common shocks. 

We estimate the time-varying FAVAR (TV-FAVAR) in two stages. The first stage involves estimating the factors with principal components (PC). The PC estimator is consistent for the factors even if the loadings mildly vary over time. The second stage involves estimating the time-varying loading coefficients, the autoregressive matrices of the factor VAR as well as the time-varying variances and correlations. A representation for the VAR with a lowertriangular matrix of contemporaneous relations is employed, which renders the VAR 

equations conditionally independent, and the common shock volatilities are modelled as functions of lagged factors. The model is then estimated equation-wise by Maximum Likelihood based on the Kalman filter. 

As an empirical example, we fit our TV-FAVAR to a large quarterly US dataset with more than 300 macroeconomic and financial variables, observed between 1972 and 2007. Our estimation results imply substantial time variation in the variance of the shocks but also in the system dynamics, as represented by the factor loadings and factor dynamics. 

We then use the model to produce in- and out-of-sample forecasts of various macroeconomic and financial variables. In general, it turns out that for most variables and forecast horizons the forecasts from the TV-FAVAR are more accurate than those from a constant-parameter FAVAR. The results deteriorate somewhat in a post-1995 pseudo real time analysis, but the TV-FAVAR still dominates for most monetary and financial variables. 

Finally, we contribute to the growing literature on time variation in the monetary transmission mechanism by identifying monetary policy shocks and assessing their transmission to the US economy over time. We confirm the finding of previous studies that the volatility of the monetary shocks is substantially smaller after the early-1980s. The negative impact of a samesized contractionary shock on most activity and price measures has declined over time. The effects on activity variables do not appear to be different during recessionary phases compared to expansions. Finally, the negative impact of monetary policy shocks on inflation expectations and long-term interest rates has weakened over time. This could be due to changes in the conduct of monetary policy which reacts since the beginning of the 1980s more strongly to output and price fluctuations which, in turn, has led to better anchored inflation expectations. Another possible explanation is globalization in the course of which the effect of domestic shocks on long-term interest rates has decreased at the expense of foreign shocks. Both the declined impact on inflation expectations and long-term rates may have contributed to the decline in the impact on activity and prices. 

#### **Nichttechnische Zusammenfassung** 

Die jüngere makroökonometrische Literatur interessiert sich zunehmend für Anwendungen so genannter ‚factor-augmented vector autoregressive (FAVAR) models’ für die Prognose und strukturelle Analysen. Diese Modelle sind in der Lage, umfangreiche Datenmengen zu nutzen und insofern Probleme aufgrund ausgelassener Variablen zu vermeiden, welche häufig in kleineren Vektor-autoregressiven Modellen (VARs) auftreten. In FAVAR-Modellen wird die gemeinsame Entwicklung einer Vielzahl von Variablen erfasst. Dabei wird jede Variable als Summe einer gemeinsamen und einer variablenspezifischen Komponente modelliert. Die gemeinsame Komponente ist das Produkt weniger gemeinsamer Faktoren, die die wesentlichen ökonomischen Einflussgrößen erfassen, und sog. Faktorladungen, die variablenspezifisch sind. Die zeitliche Entwicklung der Faktoren wird mit Hilfe eines VARs abgebildet. Es wird in der Literatur üblicherweise angenommen, dass die Modellparameter über die Zeit konstant sind. 

Ein anderer Literaturstrang nutzt kleine Modelle mit zeitvariierenden Parametern, um explizit sich verändernde Ursachen und Mechanismen wirtschaftlicher Schwankungen zu untersuchen. Diese Änderungen beziehen sich auf die Größe der ‚Schocks’ (unerwartete Änderungen der betrachteten Variablen) sowie deren direkte und mittelbare Auswirkungen auf die Volkswirtschaft. Diese Literatur trägt somit der Existenz struktureller Veränderungen Rechnung, wie beispielsweise einer stärkeren Bedeutung des Finanzsektors, der Globalisierung oder institutioneller Änderungen. 

Einige wenige Papiere haben FAVAR-Modelle und die zeitvariierenden Parameteransätze kombiniert und FAVAR-Modelle mit zeitvariierenden Parametern (TV-FAVAR) eingeführt. Alle existierenden Beiträge verwenden Bayesianische Schätzmethoden. In diesem Papier schlagen wir stattdessen ein vollständig klassisches Schätzverfahren für FAVAR-Modelle mit zeitvariierenden Parametern vor. Unser zeitvariables Model ist recht flexibel, denn es erlaubt graduelle Veränderungen in den Faktorladungen, in den autoregressiven Koeffizienten des Faktor-VARs, in den kontemporären Beziehungen zwischen den Faktoren sowie der Volatilität der gemeinsamen Schocks. 

Wir schlagen vor, das TV-FAVAR in zwei Schritten zu schätzen. In einem ersten Schritt werden die Faktoren mit Hilfe einer Hauptkomponentenanalyse (HK) bestimmt. Der HK- 

Schätzer ist konsistent für die Faktoren, selbst wenn die Faktorladungen sich über die Zeit (begrenzt) verändern. In einem zweiten Schritt werden die zeitvariierenden Ladungen, die autoregressiven VAR-Parameter, die Korrelationen und Schockvarianzen geschätzt. Wir wählen eine Repräsentation des VARs, bei der die kontemporären Beziehungen zwischen den Faktoren einer unteren Dreiecksmatrix entsprechen, so dass die einzelnen Gleichungen des VARs (bedingt) unabhängig voneinander sind. Die Volatilitäten der gemeinsamen Schocks werden als Funktionen der verzögerten Faktoren modelliert. Das Modell kann dann Gleichung für Gleichung mit Maximum Likelihood, basierend auf dem Kalman Filter geschätzt werden. 

Wir wenden unser TV-FAVAR auf einen großen vierteljährlichen Datensatz mit über 300 US-amerikanischen makroökonomischen und Finanzmarktvariablen zwischen 1972 und 2007 an. Unsere Schätzergebnisse zeigen ausgeprägte Zeitvariation in der Varianz der gemeinsamen Schocks, aber auch im Transmissionsmechanismus, welcher durch die Ladungen und die Faktordynamik abgebildet wird. 

Das Modell wird anschließend genutzt, um verschiedene makroökonomische und Finanzmarktvariablen zu prognostizieren. Für die meisten betrachteten Variablen und Vorhersagehorizonte ist die Prognosegüte des TV-FAVAR der von FAVAR Modellen mit konstanten Parametern überlegen. In einer (‚pseudo’-) Echtzeit-Prognose für die Quartale ab 1995 verschlechtert sich die relative Vorhersagequalität des TV-FAVAR etwas, allerdings dominiert das Modell alternative Ansätze bei der Vorhersage der meisten monetären Aggregate und Finanzmarktvariablen. 

Schließlich untersuchen wir, wie sich die geldpolitische Transmission auf die US-Wirtschaft mit der Zeit verändert hat. Wie auch vorangegangene Studien finden wir, dass die Volatilität geldpolitischer Schocks ab Mitte der Achtziger Jahre geringer ist als davor. Der negative Effekt eines kontraktiven geldpolitischen Schocks (vergleichbarer Größe) auf die Realwirtschaft und auf Preise ist im Allgemeinen mit der Zeit kleiner geworden. Wir finden keinen Hinweis darauf, dass sich geldpolitischer Schocks stärker auf die Realwirtschaft in Rezessionen als in konjunkturellen Aufschwungphasen übertragen. Schließlich scheinen sich der negative Effekt kontraktiver geldpolitischer Schocks auf Inflationserwartungen und der positive Effekt auf Langfristzinsen über die Zeit abgeschwächt zu haben. Dies liegt möglicherweise in Veränderungen in der Politik der Zentralbank begründet, die seit Beginn der Achtziger Jahre aggressiver auf Schwankungen in der Realwirtschaft und bei den Preisen 

reagiert, was wiederum zu stärker verankerten Inflationserwartungen geführt haben mag. Ein weiterer Erklärungsfaktor könnte die Globalisierung sein, in deren Folge der Einfluss heimischer Schocks zu Lasten globaler Schocks abgenommen haben könnte. Der geringere Effekt auf Inflationserwartungen und Langfristzinsen kann möglicherweise auch den rückläufigen Effekt geldpolitischer Schocks auf Aktivität und Preise erklären. 

#### **Contents** 

|1  Introduction|1|
|---|---|
|2  The TV-FAVAR model: representation and estimation|4|
|2.1  The TV-FAVAR model|4|
|2.2  Estimating the TV-FAVAR|6|
|2.3  Comparison with related approaches|9|
|3  A large dataset for the US|10|
|4  Estimation results|11|
|4.1  Estimated factors|11|
|4.2  Time variation in parameters and volatility|12|
|4.3  Diagnostic checking|13|
|5  Forecasting with the TV-FAVAR|13|
|5.1  In-sample forecasts|14|
|5.2  Out-of-sample forecasts|16|
|6  Structural analysis|17|
|6.1  Possible reasons for changes in the monetary transmission mechanism<br>and existing empirical evidence|17|
|6.2  Monetary policy shock identification|18|
|6.3  Computing time-varying impulse responses|19|
|6.4  Monetary policy shocks and transmission in our TV-FAVAR|20|
|7  Conclusions|22|
|References|23|



#### **Tables and Figures** 

|Table 1:  Tests for autocorrelation of the idiosyncratic errors|27|
|---|---|
|Table 2:  In-sample forecast results|28|
|Table 3:  Out-of-sample forecast results|31|
|Table 4:  Overview of existing studies on changes in the<br>monetary transmission mechanism in the US|34|
|Figure 1:  Factor estimates|36|
|Figure 2:  Autocorrelation function of the standardized VAR residuals|36|
|Figure 3:  Time-varying volatility of the monetary policy shock|36|
|Figure 4:  Impulse response functions of key variables|37|
|Figure 5:  Impulse response functions of additional activity and price variables|38|
|Figure 6:  Impulse  response functions of inflation expectations and long-term<br>government bond yields|40|
|Appendix:  Data|41|



### 1 Introduction<sup>*</sup> 

The recent macroeconometric literature has seen an increasing interest in the application of factor-augmented vector autoregressive (FAVAR) models for forecasting and structural analysis.<sup>1</sup> They provide a means to exploit a large information set and handle the omitted-variable problem often encountered in standard vector autoregressive (VAR) models. FAVARs were originally suggested by Bernanke et al. (2005), who modeled a large number of variables as the sum of a common component and an idiosyncratic component. The common component of a variable is the product of a few common factors and variable-specific factor loadings. The factors, the driving forces underlying most economic variables, are assumed to follow a VAR process. 

Another recent strand of literature has focused on small models with time-varying parameters, including evolving variances, to explicitly take into consideration the changing sources and sizes of shocks, and their transmission to the economy, see e.g. Cogley and Sargent (2005) and Sims and Zha (2006). 

A few papers have attempted to combine the FAVAR and the time-varying parameter approaches, introducing FAVAR models with time-varying parameters, hence combining the benefits of using lots of variables and allowing for a time-varying model structure. Examples include Baumeister et al. (2010) and Korobilis (2009), whose applications concern the transmission mechanism of monetary policy in the US, as well as Del Negro and Otrok (2008), Liu and Mumtaz (2009) and Mumtaz and Surico (forthcoming), who fit time-varying FAVAR models to study international business cycle and inflation comovements. A common feature of all these contributions is the use of Bayesian procedures. Instead, in this paper we propose a fully classical approach to estimate a FAVAR model with time-varying parameters. Our time-varying version is fairly flexible, as it can ac- 

> *0The views expressed in this paper do not necessarily represent the view of the European Central Bank or the Deutsche Bundesbank. Sandra Eickmeier thanks the Monetary Policy Strategy Division of the ECB for its hospitality. We thank Christiane Baumeister for useful discussions and for providing us with commodity and PCE price data. We thank Herman van Dijk, Hashem Pesaran, Lucrezia Reichlin, Jim Stock, Harald Uhlig, Giovanni Urga, Mark Watson, as well as participants at the NBER Summer Institute 2010 (Boston) and the conference on ‘High-dimensional econometric modelling’ at Cass Business School (London) and seminar participants at the Deutsche Bundesbank and the European Central Bank for useful discussions. Many thanks go also to Guido Schultefrankenfeld and Michael Richter for their help on the datasets. 

> 1 For forecasting applications see, e.g., Stock and Watson (2002a), Stock and Watson (2002b), Stock and Watson (2006), Eickmeier and Ziegler (2008). Regarding structural analysis see, e.g., Bernanke, Boivin, and Eliasz (2005), Boivin, Kiley, and Mishkin (forthcoming), Baumeister, Liu, and Mumtaz (2010) (for monetary policy applications) and Kose, Otrok, and Whiteman (2003), Kose, Otrok, and Whiteman (2008), Eickmeier (2007), Mumtaz and Surico (2009), Liu and Mumtaz (2009), Del Negro and Otrok (2008), Beck, Hubrich, and Marcellino (2009) (for applications on international business cycle and inflation comovements). 

1 

commodate smooth changes in the factor loadings, in the autoregressive coe�cients of the factor VAR, in the contemporaneous relationships between the factors, and in the volatility of the common shocks. 

We suggest to estimate the time-varying FAVAR (TV-FAVAR) in two stages. The first stage involves estimating the factors with principal components (PC). As argued by Stock and Watson (2008) and Banerjee, Marcellino, and Masten (2008), the PC estimator is consistent for the factors even if the loadings mildly vary over time. The second stage involves estimating the time-varying loading coe�cients, the autoregressive matrices of the factor VAR as well as the time-varying variances and correlations. Treating the estimated factors as given, the relations between the observable variables and the factors are represented as a set of univariate regression models with time-varying parameters, which evolve as independent random walks. As such, the model is estimated equation-wise by converting each equation into state space form, estimating the hyperparameters by maximum likelihood, and applying the Kalman filter to back out the time-varying parameter paths, see e.g. Nyblom (1989). Regarding the time-varying factor VAR, we employ a representation with a lower-triangular matrix of contemporaneous relations, which renders the VAR equations conditionally independent. This again enables us to estimate the model equation-wise, applying standard methods for univariate regression models with time-varying parameters. Concerning the volatility specification, we deviate from the common assumption in the literature that volatility is driven by an additional latent factor. We rather specify it as an (exponentially a�ne) function of lagged factors, which makes our VAR equations conditionally linear. The resulting estimated pattern of volatility is similar to that returned by models, in which time-varying volatility is captured by additional latent variables. Moreover, we think that linking the evolution of volatility to the underlying economic forces, namely, the factors, is a sensible modeling choice. 

As an empirical example, we fit our TV-FAVAR to a large quarterly US dataset with more than 300 macroeconomic and financial variables, observed between 1972 and 2007. Our estimation results imply substantial time variation in the variance of the shocks but also in their transmission mechanism, as represented by the factor loadings and factor dynamics. However, time variation is ‘sparse’ in the sense that changes in only a few parameters govern the time variation of the system, while most parameters turn out to be essentially constant over time. 

We then use the model to produce in- and out-of-sample forecasts of various macroeconomic and financial variables. In the in-sample analysis, we not only look at average forecast errors over the entire sample period but also forecasts for recession periods only, which are notoriously hard to predict with small constant-parameter approaches, as well as forecasts for the post-1995 period for which many models have been shown to perform particularly badly, see D’Agostino, Giannone, and Surico (2007). In general, it turns out that for most variables and forecast horizons the in-sample forecasts from the TV-FAVAR 

2 

are more accurate than those from a constant-parameter FAVAR. The results deteriorate in a post-1995 pseudo real time analysis, since estimation uncertainty increases for the TVFAVAR, while recursive estimation introduces a form of parameter time variation in the constant-parameter FAVAR. However, the TV-FAVAR still dominates for most monetary and variables. 

Finally, we contribute to the growing literature on time variation in the monetary transmission mechanism by identifying monetary policy shocks and assessing their transmission to the US economy over time.<sup>23</sup> 

Boivin et al. (forthcoming) comprehensively overview the existing literature and show that a consensus on how the monetary transmission mechanism in the US has evolved is still lacking. The time-varying framework also allows us to examine the evolution of the volatility of monetary policy shocks. We focus on three questions regarding the monetary transmission. (i) Has the transmission to key macroeconomic variables changed over time and, if yes, how? (ii) Can we detect asymmetries or, more specifically, are monetary policy shocks transmitted to economic activity more strongly during recessions than during booms? (iii) Has the transmission to inflation expectations changed over time and, if yes, how? 

The results highlight interesting patterns of time variation. In particular, the volatility of the monetary shocks is substantially smaller after the early-1980s. The negative impact of a same-sized shock on most activity and price measures has declined over time. The e�ects on activity variables do not appear to be di�erent during recessionary phases compared to expansions. Finally, the negative impact of monetary policy shocks on inflation expectations and long-term interest rates has weakened over time. This could be due to changes in the conduct of monetary policy or to globalization and may have contributed to the decline in the impact on activity and prices. 

The paper is organized as follows. In section 2 we present the model and estimation methodology and compare our approach with related TV-FAVARs. In section 3 we present the data. In section 4 we fit the TV-FAVAR to the data and present evidence on time variation in the parameters. In section 5 we evaluate the forecasting performance of the TV-FAVAR model. In section 6 we assess changes in the monetary transmission mechanism in the US over time. Finally, in section 7 we summarize the main results and conclude. 

> 2 Especially with this application in view, our sample ends before the onset of the 2007-09 financial crisis. As the Federal Reserve employed a number of non-standard monetary policy measures in reaction to the crisis, it would probably be intricate to interpret results based on shocks to the Federal Funds Rate as the monetary policy instrument during the crisis period. 

> 3 In a companion paper, Eickmeier, Lemke, and Marcellino (2011), we use the TV-FAVAR to trace the e�ects of US financial shocks on several advanced economies, with a focus on the 2008-2009 financial crisis. 

3 

### 2 The TV-FAVAR model: representation and estimation 

In this section we introduce the TV-FAVAR model, discuss its estimation, and compare it to related approaches. 

#### 2.1 The TV-FAVAR model 

Our starting specification is the FAVAR model as proposed by Bernanke et al. (2005). Let ��<sup>0=(�1�����������)denotealargevectorof�zero-meanstationaryvariables,for</sup> � = 1������ , where both � and � can go to infinity. In the standard dynamic factor model, each element of �� is assumed to be the sum of a linear combination of � common factors ��<sup>0= (�1�����������)andanidiosyncraticcomponent����.Hence,</sup> 



where �<sup>0</sup> �<sup>= (�1�����������).Weassumethatthefactorsareorthonormalanduncorrelated</sup> with the idiosyncratic errors, and �(��) = 0, �(���<sup>0</sup> �<sup>) =�,where�isadiagonalmatrix.</sup> These assumptions identify the model and are common in the FAVAR literature. They can be partly relaxed when the goal of the analysis is purely factor estimation by means of non-parametric methods, see e.g. Stock and Watson (2002b) and Stock and Watson (2002a). 

The dynamics of the factors are then modeled as a VAR(�), 



Since each ���� is assumed to be a zero-mean process (and the respective data are demeaned), equations (2.1) and (2.2) do not contain intercepts. 

The VAR equation (2.2) can be interpreted as a reduced-form representation of a system of the form 



where � is lower-triangular with ones on the main diagonal, and � is a diagonal matrix. The relation to the reduced-form parameters in (2.2) is �� = �<sup>�1</sup> K� and � = �<sup>�1</sup> ��<sup>�10</sup> . This system of equations may in other contexts be referred to as a ‘structural VAR’ (SVAR) representation. While we will actually use a triangular contemporaneous relation in our structural analysis in section 6, we emphasize that the chosen representation (2.3) mainly serves to render its � equations conditionally independent. This representation is particularly useful for estimating the time-varying version outlined below, but after estimation of the system matrices other forms of shock identification besides the specific triangular one may be applied. 

Having introduced the standard FAVAR model with a constant parameter structure, we now relax the assumption of parameter constancy in four dimensions. Specifically, we 

4 

allow for time variation in: (i) the autoregressive dynamics of the factors (K1����� K�), (ii) the contemporaneous relations captured by the matrix � , (iii) the variances of factor innovations, i.e., the elements of � in (2.3), and (iv) the factor loadings in (2.1). Thus, we consider the following time-varying version of (2.1) and (2.3): 



and 



where again �� is lower-triangular with ones on the main diagonal, and �� is diagonal. In addition, we specify the idiosyncratic components in (2.4) to follow a first-order autoregressive process<sup>4</sup> : 



Again, the elements of �� � (�1�����������)<sup>0</sup> are assumed to be contemporaneously uncorrelated. 

Let the time-varying parameters {��� K1������� K���� �1������� ����} be collected in a vector ��. Note that the dimension of this vector is � · (� � 1) · 0�5 + � · �<sup>2</sup> + � · �, which can be fairly large. As is common in time-varying parameter regression models, see e.g. Nyblom (1989), we assume the parameters to vary slowly over time, as independent random walks 



where � is a diagonal matrix. All elements of (��������) are assumed to be uncorrelated contemporaneously and over time. 

In practice, the matrix � could be non-diagonal, capturing commonality in some parameter movements. Our estimation procedure, described below, remains consistent also in this case, though not e�cient. As an alternative, a specific structure could be imposed on � (to reduce the number of free parameters), or a di�erent model used for parameter evolution, e.g., a factor model. However, both these approaches impose precise patterns of commonality in parameter movements, which we prefer to avoid given the lack of a priori information on this issue. 

Our TV-FAVAR specification is fairly parsimonious, in the sense that the number of parameters governing the innovation variances of time-varying parameters equals the number of parameters in constant-parameter FAVAR models.<sup>5</sup> Moreover, our time-varying 

> 4 Accommodating a higher lag order for the idiosyncratic components would be straightforward. 

> 5 In addition, the Kalman filter needs to be initialized, so that for all time-varying parameters we need to specify the distribution at time � = 0. Here we follow the frequently used strategy to initialize the time-varying parameters with their OLS estimates. Alternatively, initialization could be based on a di�use prior approach (as we specify random walk dynamics for parameters). 

5 

model nests the standard constant-parameter FAVAR, since when all the elements of the � matrix are equal to zero the former reduces to the latter. 

We will estimate the VAR and the factor loading relations equation by equation. As we will discuss in section 2.2, this is possible as each of these equations with time-varying parameters can be cast into a linear Gaussian state space model. The crucial point is how to model time variation in factor innovation volatility: if it were assumed to be governed by another latent process, say ��, such that e.g. ����� = exp(��) and �� = �� + �����1 + ����, this would make the model nonlinear in the state vector, preventing estimation based on linear Gaussian state space models, and requiring linear approximation approaches or simulation-based methods. In addition, as the factors �� are assumed to represent the main driving forces of the economy, they may be considered a natural choice for the drivers of volatility as well. 

Due to these considerations, we assume volatility to be a function of lagged factors, ���1. This guarantees that each single VAR equation with time-varying parameters and such-specified time-varying innovation volatility can be represented by a linear (conditionally) Gaussian state space model. To be specific, for each of the VAR equations we write innovation volatility as an exponential-a�ne function of the last period’s factors: 



Obviously, if �� = 0 we are back to the homoscedastic case. When only the �<sup>��</sup> element of �� di�ers from zero, innovation volatility for factor � depends on lagged levels of this factor only.<sup>6</sup> 

We will see that empirically this approach produces volatility estimates in line with those generated by models with additional latent variables capturing the time variation in volatility. 

#### 2.2 Estimating the TV-FAVAR 

The elements of �� are estimated as the first � PCs of ��. We then treat them as observable, which is justified when � grows faster than �<sup>0�5</sup> , see Bai and Ng (2006), and estimate the time-varying-parameter factor VAR and the loading equations. Note that, as argued by Stock and Watson (2008) and Banerjee et al. (2008), the factors are still estimated consistently even if there is some time variation in the loading parameters. The intuition underlying this result is that factor estimates at time � are weighted averages of the ��� variables at time � only. We will come back to this issue in section 4.1, when presenting the empirical results. 

> 6 The approach can be modified by allowing exogenous variables to be determinants of volatility; for an application, see Eickmeier et al. (2011). Moreover, instead of the exponential-a�ne specification, volatility may be modeled as a function of squared past changes in variables, or other functional forms can be chosen. 

6 

Regarding the cross-sectional relations, we put each of the � equations (2.4) into ˜ state space form. For the �th equation the state vector is ��<sup>(�)</sup> = [�<sup>0</sup> ��<sup>����]0.Sincethe</sup> idiosyncratic component in (2.4) follows an AR(1) process, rather than being white noise, it becomes part of the state vector besides the time-varying loading parameters. The transition equation is given by 



0 ˜ where �� = diag([1����]), ��<sup>(�)</sup> = ��<sup>(�)��</sup> �� , where ��<sup>(�)</sup> are the respective elements of �� h i in (2.7), hence, �(˜�<sup>(</sup> �<sup>�))=0,and�(˜�</sup> �<sup>(�)˜�</sup> �<sup>(�)0</sup> ) = diag([�<sup>(�)</sup> ��<sup>2</sup> �<sup>]).Thatis,�(�)containsthe</sup> random-walk innovation variances of the time-varying parameters (i.e. the respective elements of � in (2.7)) and �<sup>2</sup> �<sup>istheinnovationvarianceoftheidiosyncraticcomponent</sup> process. The measurement equation is 



where �� = [��<sup>0�1].Weestimatethe�+ 2hyperparameters(�</sup> �<sup>��(�)���)ofthe�thloading</sup> equation by maximum likelihood. We then back out the path of time-varying loading parameters using the Kalman smoother. 

Since our assumptions imply independence between the � equations of (2.5), we can likewise estimate the time-varying parameters contained in the �� and K��� matrices equation-wise. For the �<sup>��</sup> equation in state space form, the state vector containing the time-varying parameters is given by 

0 �<sup>�</sup> � = (����1������� ������1��� K��1�1������ K����1��� K��1�2������ K����2������� K��1�������� K�������)� 

where for � = 1, there are no � parameters showing up. Note that due to the di�erent number of elements coming from the triangular � matrix, the dimensions of the state vectors are di�erent for each of the � equations. 

The state equation is the random walk for �<sup>�</sup> �<sup>,</sup> 



The measurement equation is given by 



where 



and ����� is given by (2.8). 

In a first step, we estimate for each equation the ‘hyper-parameters’ (��������) by maximum likelihood. In a second step, we filter out the time-varying parameters of each 

7 

equation by the Kalman Filter. However, when taking the filtered states �<sup>1</sup> �|�<sup>�������</sup> �|�<sup>from</sup> each equation and reconstructing the respective VAR matrices, ��� K1��|������ K���|�, the resulting local VAR dynamics at time � may imply explosive behavior. In order to avoid this, we ensure that at each point in time, all eigenvalues of the autoregressive matrix corresponding to the reduced-form VAR representation in companion form are inside the unit circle. To achieve this, we run the following restricted filtering algorithm, instead of � independent and unrestricted Kalman filters. In essence, the algorithm runs the � Kalman filters and performs an updating step only if the VAR structure implied by the filtered states jointly satisfies the stationarity condition. 

Let � denote the mapping from the family of estimated state vectors {�<sup>1</sup> �|�<sup>�������</sup> �|�<sup>} =:</sup> A�|� into the respective VAR matrices ��|�� K1��|������ K���|�. The algorithm (� Kalman filters with joint nonlinear restrictions on filtered states) runs as follows: 

1. Maximize the likelihood associated with each of the � state space models (2.10)(2.11), and obtain the estimates (ˆ��� �ˆ��<sup>ˆ</sup> ��) of (�<sup>�</sup> ������), � = 1������. 

2. Given the hyper-parameters, initialize the � state space models by some A0 such that {�0� K1�0����� K��0} = �(A0) implies a VAR structure without explosive eigenvalues. Set the set of corresponding variance-covariance matrices of initial states {�<sup>1</sup> 0<sup>�������</sup> 0<sup>} =: S0.</sup> Set � � 1 = 0, set A��1|��1 = A0 and S��1|��1 = S0. 

3. For each of the � state space models do a Kalman filter prediction step, i.e. compute 



for � = 1�����. 

4. For each of the � state space models, do a Kalman updating step, i.e. 



for � = 1�����. 

5. Compute the corresponding VAR matrices {��� K1��|������ K���|�} = �(A�|�). If the VAR structure satisfies the non-explosiveness condition, set � := � +1 and go to Step 3. If not, set A�|� := A��1|��1 and S�|� := S��1|��1 set � := � + 1 and go to Step 3. 

8 

Note that if an updating step is not performed due to failure of the non-explosiveness condition, this does not mean the respective states (parameters) will be stuck at their � � 1-magnitudes henceforth. Rather, as new observations on the ���� come in, an updating step may be feasible in the next or one of the following periods. For the initialization of the filter, we choose the OLS estimates taken over the whole sample and their respective variance-covariance matrices. They turn out to give rise to a VAR structure that satisfies the stationarity conditions. For obtaining smoothed estimates of the time-varying parameters we apply the standard Kalman (fixed-interval) smoothing algorithm but based on the filtered estimates that have been obtained by the restricted filter in the first step. Although it is not guaranteed per se that the thus-constructed smoothed estimates satisfy the non-explosiveness conditions (even if the restricted filtered estimates satisfy them by construction), they turn out to do so in our empirical application. 

#### 2.3 Comparison with related approaches 

Unlike the bulk of the existing literature on time-varying FAVAR models, which employs Bayesian approaches, we estimate our model by classical (i.e. Maximum Likelihood) methods. The likelihood-based approach (using the Kalman filter) is feasible and straightforward in our context, as we use a model representation that allows equation-by-equation estimation, where each equation with time-varying parameters is represented as a linear state space model. It is important to note that the model could be likewise estimated by Bayesian methods. Conversely, many of the other time-varying FAVAR models in the literature may be estimated by classical approaches, but these would require simulationbased techniques (just like their Bayesian counterparts) or linearizations. Hence, using a frequentist rather than a Bayesian approach here is not a consequence of the model structure per se but a convenient choice, as it allows for analytic rather than simulation-based estimation. 

In addition, owing to the two-stage approach described above, our model is relatively flexible in the sense that it allows for various sources of parameter time variation. In previously employed models either only the factor loadings, Del Negro and Otrok (2008), Liu and Mumtaz (2009), or only the autoregressive parameters of the VAR on the factors, Baumeister et al. (2010), Mumtaz and Surico (forthcoming), are allowed to vary over time, but not both as in our approach. An exception is Korobilis (2009), who also adopts a twostage approach similar to ours where the first step involves estimating the factors with PC and the second stage involves estimating the parameters with Bayesian methods. The two-step approach enables one to circumvent the problem of simultaneously identifying factors and loadings. 

All of the papers cited above allow for time-varying volatility in the factors, and Baumeister et al. (2010), Liu and Mumtaz (2009), Mumtaz and Surico (forthcoming) 

9 

and Korobilis (2009) also allow for time variation in the contemporaneous relationships across the factors. As described above, we also feature both sorts of variation, but changes in volatility are modeled di�erently and explained by the evolution of the underlying economic forces rather than left unspecified. 

Of the papers listed above, Del Negro and Otrok (2008), Liu and Mumtaz (2009) and Mumtaz and Surico (forthcoming) allow for serial correlation in the idiosyncratic components, which we also do. In addition, Mumtaz and Surico (forthcoming), Del Negro and Otrok (2008) and Korobilis (2009) allow for time-varying volatility in the idiosyncratic components, which our model does not allow for. 

### 3 A large dataset for the US 

In order to assess the empirical performance of our TV-FAVAR, we have constructed a large balanced dataset containing 803 quarterly US time series observed from 1972Q1 to 2007Q2. The variables are transformed as usual in dynamic factor analysis. Specifically, series that were not already available in seasonally adjusted form are seasonally adjusted using the Census X12 method. Variables showing a non-stationary behaviour are made stationary through di�erencing. Most series enter in di�erences of their logarithms except for interest rates, ratios and expectations which enter in levels. Following Stock and Watson (2005), outliers are defined as observations of each (stationary) variable with absolute median deviations larger than six times the interquartile range. They are replaced by the median value of the preceding five observations. Finally, the series are demeaned and standardized to have a unit variance. The data appendix contains details on the data, the transformations and the sources. 

We drop from this dataset those series that have a low commonality, i.e. a low share of variation explained by the common factors, for two reasons. As shown by Boivin and Ng (2006), factors can be estimated accurately with PC only if the dataset has a strong factor structure. One important condition is that variables in the large dataset need to be highly correlated among each other. Another advantage of dropping variables which largely evolve in an idiosyncratic manner is that fewer factors are needed to explain the bulk of variation in the reduced dataset. Given that in our approach the number of parameters quickly increases with the number of factors, a specification with a small number of factors is preferable since it limits the computational e�orts and allows us to estimate parameters more precisely. 

The construction of the (selected or reduced) dataset proceeds as follows. We define a core set of variables based on two criteria. First, the core set should include key variables of interest in empirical macroeconomic analyses. Second, it should be roughly balanced between real, price and monetary/financial variables. We then decide upon a threshold which defines how much of the variation in the core dataset is at least explained by the 

10 

common factors. We set the threshold at 60 percent, associated with a reasonable degree of comovement, and find that � = 5 factors are needed to explain 60 percent of the variation in the core dataset. We next regress each ‘non-core’ variable on the factors and estimate the variance shares explained by the factors for each of these variables. When the variance share is larger than or equal to 60 percent, we include the variable in the dataset. 

After this procedure we are left with 336 series. 114 of them are measures of real economic activity (e.g. GDP and components, industrial production, employment measures, capacity utilization, retail sales), 134 series are price measures (e.g. deflators of GDP and components as well as of personal consumption expenditures, consumer and producer prices, commodity prices), 76 series represent monetary and financial variables (e.g. interest rates, stock prices, house prices, money and credit aggregates, exchange rates) and 12 series capture (inflation and activity) expectations (all suitably transformed). Note that asset prices and credit and monetary aggregates were divided by the GDP deflator and enter in real terms. Five factors now explain 69 percent of the variation in this reduced dataset, which suggests that some of the non-core variables added to the core set of variables have a commonality considerably larger than the chosen threshold of 60 percent. 

### 4 Estimation results 

We estimate the time-varying FAVAR model along the lines described in section 2. We use a VAR(2) for the factor dynamics. The choice of the lag length is suggested both by the need of reducing the number of parameters, and by the consideration that allowing for parameter time variation likely reduces the need of longer lags. We document the estimated factors and provide evidence that the two-step procedure (estimate factors as PCs, then estimate time-varying parameters given factors) is adequate. We then summarize the extent of time variation in the FAVAR system, and finally provide some diagnostic checking. 

#### 4.1 Estimated factors 

Figure 1 shows the estimated factor paths. To assess whether the PC approach is adequate for estimating factors in the presence of time variation in the factor loadings, we derive an alternative factor estimate from a cross-sectional regression of the � variables ���� on the estimated time-varying loadings �<sup>ˆ</sup> ���|� , for each period �. The estimated factors resulting from this exercise (displayed in the same figure in red) show a strong similarity to those estimated from the PC analysis, the respective correlation coe�cients all exceed 0.99. 

In addition, we can also run a full filtering exercise, treating our estimated parameter paths as fixed, now treating the factors as unobservable states, and then using the Kalman smoother to re-estimate them. For this exercise, the transition equation of the resulting 

11 

state space model is: 



and the measurement equation is 



where objects with hats and subscript �|� denote the parameter paths estimated in the first step, in which the factors had been kept fixed at their PC estimates.<sup>7</sup> Running the Kalman smoother on the state space model (4.1)-(4.2) delivers factor estimates that are likewise very close to the PC estimates, and accordingly also close to the factors obtained from the cross-section regression. 

Overall, this exercise provides (heuristic) support for our assumption to keep PC-based factor estimates fixed when estimating the time-varying parameters. 

#### 4.2 Time variation in parameters and volatility 

One may wonder whether a constant-parameter specification would su�ce or whether time variation in the parameters is really needed and, if yes, which sources of parameter variation are most important. One way to quantify the overall degree of time variation in the autoregressive matrix K�, the contemporaneous-relations matrix ��, and the loadings ���, is to count the number of occasions when the standard deviation of the innovations of the time-varying parameters — the respective elements of diag(�) in (2.7) — are significant. However, conducting such a multitude of individual significance tests in the usual fashion may lead to a biased assessment of the overall degree of time variation.<sup>8</sup> Moreover, a further complication arises as under the null hypothesis of no variation, the respective parameter lies on the boundary of the allowable parameter space. Accordingly, we resort to a more direct approach of gauging the overall degree of time variation in the system: we count the number of parameters, for which the time evolution estimated by the Kalman smoother is ‘a straight line’, i.e for which the standard deviation of the smoothed parameter series is essentially zero. 

> 7 The ‘dual’ state space representation (4.1)-(4.2) of a time-varying FAVAR is only valid if the idiosyncratic components in (2.6) are serially uncorrelated, i.e. �� = 0 for all �. In the relevant case with autocorrelated idiosyncratic errors the idiosyncratic components would enter the state vector which would be of dimension 2� + � instead of 2� as in (4.2). We abstain from conducting the exercise with this large (346)-dimensional state vector, but instead use the mis-specified state space representation (4.1)-(4.2), where we ignore the autoregressive structure of the measurement error in (4.2). 

> 8 If these tests are conducted with an e�ective size of, say, 5%, then even in the extreme case of no time variation at all, one would expect to reject the null hypothesis of no time variation 5% of the time. 

12 

It turns out that there is actual time variation (i.e. no ‘straight-line’ parameter paths) for: 6 out of the 50 parameters of the K autoregressive matrix (containing the dynamics of the VAR(2) for the 5 factors); 1 out of the 10 (= 0�5 · 5 · 4) parameters of the � matrix of contemporaneous relationships of the VAR; and 845 out of the 1680 loadings (since there are 5 loadings, one for each factor, for each of the 336 variables). 

Finally, we have assessed whether there is indeed time variation in the volatilies of the shocks, i.e. whether the elements of �� in equation (2.8) are significant. The corresponding t-statistics are based on the estimated standard errors which are obtained from the negative inverse of the Hessian of the likelihood function. We find that 5 out of 25 parameters are indeed significant at the 5% level, 2 more parameters are significant at the 10% level. 

In summary, the results in this section based on our estimated TV-FAVAR indicate that most of the time variation in the behaviour of US macroeconomic and financial variables over 1972-2007 is associated with changes in the impact of the factors on the variables under analysis and with changes in the volatility of the shocks (which is linked to lagged factors in our model). The degree of variation in the contemporaneous or dynamic relationships across factors is more subdued. 

#### 4.3 Diagnostic checking 

We first want to check the adequacy of the chosen VAR lag length. If longer lags were needed, the estimated residuals would be correlated over time. Hence, in Figure 2 we report the estimated autocorrelation function (ACF) for the standardized VAR residuals, together with asymptotic 95% confidence bands. Overall, Figure 2 does not provide any major evidence against the assumption of no correlation of the VAR(2) errors. 

Similarly, one may wonder whether our assumption of AR(1) idiosyncratic components, while standard in the literature, is su�cient to clean from temporal correlation. Formal statistical testing is complicated since the joint null hypothesis has a large number of components. To provide at least some indication of the existence of possible problems, in Table 1 we report the percentage of the 336 idiosyncratic residuals (one for each of the variables under analysis) for which a given lag of the ACF is outside the asymptotic bands. For example, only 6 percent of the residuals have the first lag of the ACF outside the bands. Hence, this informal diagnostic check does not provide evidence against our assumption of AR(1) idiosyncratic components. 

### 5 Forecasting with the TV-FAVAR 

In this section we evaluate the forecasting performance of our proposed TV-FAVAR approach for a set of key variables. We predict variables representing real activity (including growth of GDP, consumption, investment, industrial production, employment as well as 

13 

the unemployment rate and capacity utilization), inflation (changes of the GDP deflator, the CPI, the personal consumption deflator, the PPI, and unit labor costs), and a number of financial and monetary variables. 

The factors are estimated as the first � = 5 PCs of our dataset, and they are then modeled together with each target variable as a time-varying VAR whose parameters evolve as independent random walks. The TV-FAVAR forecasting model thus includes overall 6 endogenous variables/factors, and its lag length is, again, set to 2. Hence, for each variable of interest ����, we have ���� := (�������), with 



where each element of �1���� and �2���� evolves as an independent random walk and the volatility of ���� is modeled as in (2.8).<sup>9</sup> Note that with respect to the TV-FAVAR specification in section 2, the forecasting model allows for a feedback from the target variable to the factors, and for a direct e�ect of past values of the target variable on its current evolution. Both features are fairly standard in forecasting models and represent a direct extension of the TV-FAVAR from section 2. 

#### 5.1 In-sample forecasts 

We first conduct an in-sample forecast exercise for the whole sample period. Given smoothed estimates of �1���� and �2���� for some time �, forecasts for horizons of one to four quarters are computed as the conditional expectations implied by the associated VAR. In-sample evaluation is fairly common in the literature on the forecasting performance of time-varying models, see e.g. Stock and Watson (2008). 

In addition to the full sample forecast evaluation, we also assess how well the TVFAVAR predicts each variable when it goes through recessions, which has proven particularly di�cult with constant-parameter models. The recessionary periods are defined according to the NBER chronology. Moreover, the forecast evaluation is also separately applied for the subsample 1995-2007, since there is evidence of a worsening in the performance of several forecasting methods (relative to naive predictors) over the more recent years, see e.g. D’Agostino et al. (2007). 

We take an AR model as the benchmark and compare its root mean squared forecast error (RMSE) with RMSEs resulting from a FAVAR with constant parameters, an AR with time-varying (random walk) parameters, the TV-FAVAR assuming constant volatility, and the full TV-FAVAR. This exercise allows us to assess whether there are gains not only from using a large information set as summarized by the estimated factors, but also from moving from a constant to a time-varying parameter setup, and from explicitly modeling volatility. 

> 9 We take the five lagged latent factors as volatility regressors in the first five equations. The last equation’s volatility features these factors as well, but in addition the lagged variable of interest. 

14 

For comparability, we set the lag length of the benchmark AR model, the TV-AR, the constant-parameter FAVAR and the TV-FAVAR with constant volatility also to 2. 

The three panels of Table 2 report the results for, respectively, the real activity, inflation and interest rate and monetary, credit and asset price variables. Each panel contains five groups of results. The first group reports the RMSEs resulting from the benchmark constant-parameter AR model. The second to fifth groups contain relative RMSEs of the constant-parameter FAVAR, the TV-AR and the TV-FAVARs without and with changing volatility vis-à-vis the benchmark AR. 

Each group has three columns, referring to the full sample, the sample containing recessions only, and the sample as of 1995, respectively. Shaded areas indicate the smallest value for the respective evaluation period (full, since 1995, recessions), if the respective relative RMSE is smaller than 1. Otherwise, i.e. when no model beats the constantparameter AR, no result is shaded. 

It turns out that the constant-parameter FAVAR generally outperforms the AR model, suggesting that there are gains from exploiting information from a large number of variables. For most variables, gains from using a FAVAR compared to an AR model are larger during recessions than over the entire sample period (including both recessions and expansions). This pattern seems to be due to the marked increase of the RMSE of the benchmark AR model during recessions. However, the relative performance of the FAVAR tends to deteriorate substantially after 1995, in line with previous studies. 

The performance of the TV-AR is in general very similar to that of the benchmark. In fact, for some variables, where the ML estimates of parameter innovation variances are ‘small’, the Kalman smoother essentially estimates the (potentially) time-varying parameters as constant and sets them equal to their counterparts from the constant AR(2) — in turn generating the same forecasts. There are some gains for a few variables, such as employment growth and CPI inflation, and some large losses for the Federal Funds rate. Thus, the constant-parameter AR cannot be improved much by allowing time variation in the same univariate model, but rather by using a a large information set as in the constant-parameter FAVAR. 

On average over the whole sample period, the TV-FAVAR outperforms the FAVAR with constant parameters for a vast majority of the considered variables and horizons. Over the whole evaluation sample, keeping the volatility of the FAVAR constant in general helps for real activity and inflation variables, but not for financial indicators. Time-varying volatility seems to matter even more after 1995. Over this more recent period, the gains with respect to the benchmark AR still shrink as for the constant-parameter FAVAR, but in general they remain positive and often sizeable. 

Finally, the TV-FAVAR with or without time-varying volatility appears to perform best also during recessions, with large and systematic gains for virtually all variables. 

15 

#### 5.2 Out-of-sample forecasts 

We complement these results with a pure pseudo out-of-sample assessment, where in each quarter of the evaluation period, which ranges from 1995Q1 to 2007Q2, each model is reestimated and forecasts for one to four quarters ahead are computed.<sup>1011</sup> The results are reported in Table 3, whose structure resembles that of Table 2, but omits the distinction between evaluation periods. 

On average, the performance of the TV-FAVAR deteriorates by about 20 percent with respect to the in-sample analysis evaluated over the period since the mid-1990s. Since the behaviour of the benchmark is virtually the same, such a deterioration is due to the use of the filtered rather than the smoothed parameter estimates for the TV-FAVAR, and possibly also due to undesirable swings in hyperparameters. 

The gains with respect to the constant-parameter FAVAR also shrink. Besides the mentioned estimation issue with the TV-FAVAR, a second reason for this finding is that recursive estimation of the constant-parameter FAVAR introduces by itself a form of parameter time variation, which is instead absent in the in-sample analysis. Of course, the improved forecasting performance of the constant-parameter FAVAR when recursively estimated is at odds with the underlying assumption of parameter stability, making the resulting estimators biased and inconsistent, though more useful for forecasting. 

Notwithstanding the mentioned problems, the TV-FAVAR with constant or changing volatility still works reasonably well for some variables such as capacity utilization, CPI inflation, changes in unit labor costs, and several financial indicators, e.g., changes in loans and in house prices. 

In summary, the results suggest that there are gains from both exploiting a large information set and modeling time variation in the parameters. The in-sample analysis indicates that the TV-FAVAR gains remain when forecasting during recessions, which is often complex and problematic, and also in the post-1995 period, when typically standard constant-parameter factor models do not perform so well. For the latter result, allowing for changes in volatility is important. Finally, when forecasting in the post-1995 period in an out-of-sample context, the performance of the TV-FAVAR deteriorates by about 20 percent, mostly due to higher estimation uncertainty, while that of the constant-parameter FAVAR improves in relative terms, due to recursive estimation, which introduces a form of parameter time variation. However, the TV-FAVAR still produces the best forecasts for a few variables and for several indicators. 

> 10 The estimation window is expanded quarter by quarter. The first estimation window reaches until 1994Q1. 

> 11 The out-of-sample period is too short to focus on recessions only. 

16 

### 6 Structural analysis 

In this section we examine how the transmission of monetary policy in the US has changed over time. We first discuss why changes in the transmission mechanism of monetary policy may have occurred over the sample period and provide an overview of the existing empirical evidence. We then present new evidence based on our TV-FAVAR. We explain how we estimate the latent factors in the structural setting, how we identify monetary policy shocks, and how we compute impulse response functions and standard errors around them. Finally, we provide evidence on the time variation in the volatility of monetary policy shocks and assess the evolution in the transmission of monetary policy shocks. 

#### 6.1 Existing empirical evidence and possible reasons for changes in the monetary transmission mechanism 

The monetary transmission mechanism in the US may have changed over the period under investigation (1972-2007) as a consequence of several structural changes which comprise three major aspects. First, there was some variation in the conduct and strategy of monetary policy in the late-1970s/early-1980s with a greater emphasis on price stability and, hence, a better anchoring of long-run inflation expectations, see Boivin and Giannoni (2002) and Galvao and Marcellino (2010) for evidence. Second, liberalization and innovation in financial markets is certainly relevant, which also mostly occured in the late 1970s/early 1980s.<sup>12</sup> Third, globalization, i.e. greater trade and financial openness, may have resulted in capital market interest rates being increasingly determined by global developments, see e.g. Boivin and Giannoni (2010), rather than by domestic forces such as monetary policy. 

Despite numerous studies on this topic, the empirical literature is still lacking a consensus on how the transmission of monetary policy shocks in the US has changed over time. Table 4 overviews recent time-series work on monetary transmission on inflation and activity. The evidence is based on a variety of methods which di�er in the way time-variation in the parameters is modeled (split-sample versus smooth parameter changes), in the way monetary policy shocks are identified (recursive identification versus sign restrictions), and in the amount of information exploited (small-scale VARs which use a handful variables versus FAVARs which exploit hundreds of variables). VAR-based papers generally focus on the e�ect of monetary policy on a single measure of real activity and a single inflation 

> 12 On the one side, it subsumes the phasing out of regulation Q and the growth of securitization which may have weakened the balance sheet and bank capital channels and, hence, the transmission of monetary policy to the economy. On the other side, financial market liberalization and innovation comprise the introduction of risk-oriented capital adequacy requirements, the creation of an interstate banking system, the promotion of fair-value accounting and the democratization of credit, which may have strengthened the balance sheet channel. See Boivin et al. (forthcoming). 

17 

measure whereas FAVAR-based analyses assess a wider spectrum of activity, inflation but also financial measures. The table shows that the evidence on how the transmission of monetary policy shocks on output and inflation has changed is inconclusive ranging e.g. for inflation from a decline in the transmission over time, e.g. Boivin, Giannoni, and Mihov (2009), over no change, e.g. Primiceri (2005), to an increase (e.g. Baumeister et al. (2010). 

Despite of inconclusive results regarding the transmission of monetary policy shocks there exists, however, a broad consensus that monetary policy shocks have been large in the early 1980s during the Volcker disinflation and have become smaller since then, e.g. Boivin and Giannoni (2002), Eickmeier and Hofmann (2010), Primiceri (2005), Canova and Gambetti (2009). 

In addition to the above mentioned structural changes that have occurred either relatively quickly (in the case of institutional changes or changes in the conduct of policy) or gradually (in the case of globalization) and probably have permanent e�ects on the monetary transmission mechanism, economic frictions may lead to asymmetric responses of the economy to monetary policy shocks over the business cycle. Peersman and Smets (2002), for instance, show for the euro area that monetary policy shocks have a stronger e�ect on output and prices in recessions than in booms. Results for the US are missing to our knowledge. 

While it would certainly be very interesting to shed light on all these possible changes, we need to restrict ourselves in this application of our TV-FAVAR. We focus on changes in the transmission to activity, prices, inflation expectations and long-term interest rates, thus tackling the first and third types of permanent structural changes as well as the asymmetry question mentioned above, and we leave changes related to financial markets to future research. 

#### 6.2 Monetary policy shock identification 

For the structural analysis, it is now assumed that �� is driven by a (� + 1) × 1-vector consisting of � latent factors ��<sup>�and the Federal Funds rate ��as the (�+1)th observable</sup> factor as in Bernanke et al. (2005). We will use � = 5 factors. We estimate the space spanned by the factors using the first � +1 PCs of the data ��. To remove the observable factor from the space spanned by all � + 1 factors we split our dataset into slow-moving variables, i.e. variables that are expected to move with delay after an interest rate shock, and fast-moving variables, i.e. variables that move instantaneously in response to an interest rate shock. The slow-moving variables comprise, e.g., real activity measures, consumer and producer prices, deflators of GDP and its components and wages, whereas the fast-moving variables are financial variables such as asset prices, interest rates or commodity prices (for details see the appendix table). We estimate the first � PCs from 

18 

the set of slow-moving variables, denoted by �<sup>b</sup> �<sup>����</sup> . We then carry out a multiple regression of �� on �<sup>b</sup> �<sup>����</sup> and on ��, i.e. 



An estimate of ��<sup>�isthengivenby�ˆ�b</sup> �<sup>����</sup> . In the joint factor vector �� � [ �<sup>ˆ</sup> �<sup>����],the</sup> Federal Funds rate �� is ordered last. Given this ordering, the VAR representation of our (TV-)VAR with lower-triangular contemporaneous-relation matrix �� directly identifies the monetary policy shock as the last element of the innovation vector �� in (2.5). Hence, the shock identification works via a Cholesky decomposition, which is here readily given by the lower triangular ��<sup>�</sup> |�<sup>1.</sup> 

The methodology also allows for other identification approaches, such as sign restrictions which need to be satisfied at each point in time. We have checked that, based on our Cholesky identification scheme, non-borrowed reserves and monetary aggregates decline after an unexpected monetary policy tightening at all points in time. Hence, our results are consistent with the sign restrictions imposed, e.g., in Uhlig (2005) and Benati and Mumtaz (2007), and also with the 1979-1982 period when the Federal Reserve temporarily targeted non-borrowed reserves as opposed to the Federal Funds rate. 

#### 6.3 Computing time-varying impulse responses 

The impulse responses are based on the assumption that the system (shock propagation) remains at its time � estimate from time � henceforth. This is common practice and consistent with our assumption of random walk parameter evolution.<sup>13</sup> 

That is, at time �, we compute impulse responses in the usual fashion from the estimated VAR 



in conjunction with the estimated loading equations 



Confidence bands for the impulse response functions at time � are computed as follows. Recall that we have obtained from the Kalman smoother the estimates of the states 

> 13 More specifically, for computing the e�ect of the shock at time �, one takes conditional expectations also on the future evolution of parameters, where the information set at time � contains the best (smoothed) estimate of the model parameters at that point. Given the random walk assumption of parameters and the assumed independence of parameter innovations from factor innovations, it is straightforward to see that impulse responses (di�erence of conditional expectations of variables at � + � with and without shock) can be computed as in constant-parameter VARs, replacing the constant parameters by the time-� estimates of time-varying parameters. As an alternative (not chosen here), one may take the view that we actually know how shock propagation has changed after time �, so one may condition on the (estimated) future evolution of system parameters when computing the response to the shock. 

19 

�<sup>�therespectiveelementsoftherowsof�andK),andthecorrespond-</sup> �|�<sup>(containing</sup> ing variance-covariance matrices �<sup>�</sup> �|�<sup>foreachVARequation�=1������+ 1.Moreover,</sup> we have for the loading equations the smoothed �<sup>ˆ</sup> ���|� with the corresponding variancecovariance matrices ����|� . We generate draws of �<sup>�</sup> �� = 1������ + 1 from � (�<sup>�</sup> �|�<sup>���</sup> �|�<sup>).If</sup> the VAR matrices implied by the set of draws satisfy the non-explosiveness condition, we keep the draw, otherwise we discard it and repeat the previous step. We draw until we have gathered � = 1000 successful draws. We then draw � times �� from � (�<sup>ˆ</sup> ���|� �����|� ). For a given time �, variable � and horizon �, the desired quantiles of the impulse response function are then obtained from the � draws. A caveat of this approach is that we ignore the uncertainty associated with the estimation of the hyperparameters. 

#### 6.4 Monetary policy shocks and transmission in our TV-FAVAR 

We have reported in section 4 to what extent the volatility estimates of the VAR innovations to unidentified factors were varying over time. Figure 3 now shows the estimated volatility of the monetary policy shock. Consistent with the literature, the volatility peaks in the early-1980s which is generally labeled the ‘Volcker disinflation’ and declines thereafter. We also observe a peak around 1974. One explanation might be that, possibly due to overestimation of the negative e�ects on activity of the oil embargo in October 1973, the output gap was substantially underestimated and, hence, the Federal Funds rate was much lower than that implied by a simple Taylor rule, see Orphanides (2003). We find indeed a large sequence of expansionary monetary policy shocks around 1974 (not shown) and heightened volatility of the shocks which might reflect this mis-perception. 

Based on the TV-FAVAR and the described identification scheme we now assess the evolution of selected impulse response functions to a monetary policy shock over time. We focus on three questions. (i) Has the transmission to key macroeconomic variables changed over time and, if yes, how? (ii) Can we detect asymmetries in the monetary transmission, and, more specifically, are monetary policy shocks transmitted to economic activity more strongly during recessions than during booms? (iii) Has the transmission to inflation expectations and long-term interest rates changed over time and, if yes, how? 

Figures 4, 5 and 6 show impulse response functions of three key macroeconomic variables (the Federal Funds rate, GDP, and the GDP deflator), of additional activity and price variables (consumption, investment, industrial production, employment, GDP deflator, PPI finished goods, the PCE deflator, unit labor costs), of two inflation expectation measures (taken from the Survey of Professional Forecasters (SPF) and the survey conducted by the university of Michigan) and the 10-year government bond rate, respectively. To focus on transmission only, we show estimates of impulse response functions to a monetary policy shock which raises the Federal Funds rate on impact by 1 percentage point. Panels (a) show averages of point estimates of impulse responses over the entire sample 

20 

1972-2007 (dotted line) and, for comparison, impulse responses derived from a constant parameter FAVAR (solid line). In the (b)-panels we present impulse responses obtained from the TV-FAVAR for each point in time and horizons 0-20 quarters, and, for better visibility of time variation, we present in the (c)-panels point estimates and 90% confidence bands of impulse responses for each point in time and selected horizons (1, 4 and 8 quarters). 

Focusing first on panels (a) of the figures, the constant-parameter impulse responses have the expected shape. After an unexpected increase in the Federal Funds rate, GDP and other activity variables decline temporarily and in a hump-shaped manner. The impulse responses then turn to zero after three to five years, depending on the activity measure, consistent with real long-run neutrality of monetary policy. The GDP deflator declines persistently. There is no ‘price puzzle’, i.e. a significantly positive response of prices after a monetary policy tightening, unlike what is found in many empirical monetary studies which use small-dimensional models, see Bernanke et al. (2005) for a discussion. The graphs for the CPI, the PPI and unit labor costs display a similar pattern. Inflation expectations also decline after the shock, although the SPF measure first temporarily increases, a pattern also found by Boivin et al. (forthcoming). Long-term interest rates, reflecting expected future short-term rates and possibly term premia, increase by less than the Federal Funds rate. The (a)-panels also reveal that averages of the time-varying impulse responses are similar to their constant parameter counterparts. 

Let us now answer the questions related to time variation raised at the beginning of this section. 

(i) Figures 4 (a) and (b) reveal that while the impact of monetary policy shocks on the Federal Funds rate itself has not changed much, there are notable changes in the impulse responses of GDP and the GDP deflator over time. While the e�ects on GDP and the GDP deflator after one quarter have barely changed, the e�ects at longer horizons are estimated to have considerably weakened since the 1980s, in line with Boivin and Giannoni (2010) and Eickmeier and Hofmann (2010). 

The pattern observed for GDP carries over to investment and employment, but not to the other real activity variables. The impact on consumption has only started to weaken notably in the mid-1990s. The pattern observed for the GDP deflator is also apparent in the graphs for CPI, the PCE deflator and unit labor costs, but not for PPI (Figure 5). 

(ii) Inspection of the time-varying impulse responses of the activity variables, see panel (c) of Figures 4 and 5, does not point to sizeably di�erent e�ects of monetary policy shocks during recessions versus expansions. Hence, unlike Peersman and Smets (2002) for the euro area, we do not find evidence of asymmetry in the monetary transmission for the US. One possible explanation of this discrepancy between the findings for the two regions is that 

21 

there are less frictions in the US than in the euro-area economy.<sup>14</sup> Another explanation might be that Peersman and Smets (2002) model parameter variation di�erently allowing parameters only to take two values, one for recessions and one for booms, whereas we also allow for gradual changes and trending parameters over time. 

(iii) Figure 6 finally shows that the negative impact on inflation expectations has become smaller over time, in line with Boivin et al. (forthcoming). The decline starts in the 1970s for both inflation expectation measures. The changes for the SPF measure is mostly apparent for longer horizons. The timing of the decline is roughly consistent with a change in the conduct of monetary policy towards more aggressive reactions to output and inflation and, consequently, a better anchoring of long-term inflation expectations. A smaller response of inflation expectations may have also contributed to a decline in the e�ect on the term premium and, hence, long-term interest rates which is, however, only apparent for short horizons. Interestingly, also, this decline started in the mid-1980s, and — at least the timing — is consistent with the initial years of globalization, see Kose, Prasad, and Terrones (2006). A smaller e�ect on long-term rates and inflation expectations may also have contributed to the weakening of the negative responses of output and price measures. 

Summing up, our results confirm previous findings in the literature that the size of monetary policy shocks is smaller since the early-1980s than before. We find weaker e�ects on activity and prices, which could partly be due to a better conduct of monetary policy and, consequently, a better anchoring of inflation expectations and, possibly, globalization. Finally, we do not find evidence for di�erent reactions of activity variables to monetary policy shocks in recessions versus non-recession periods. 

### 7 Conclusions 

In this paper we have proposed a FAVAR specification that is suited to model large datasets allowing for general patterns of time variation in the factor loadings, the factor dynamics, and their innovation variance-covariance structure. Contrary to previous literature, which is mostly Bayesian, we propose a fully classical (i.e. maximum-likelihood-based) approach for estimation, inference, forecasting and structural analysis. 

The three main technical features underlying our approach are, first, the use of PCbased factor estimates (justified by the theoretical results in Stock and Watson (2002a), Stock and Watson (2002a), Stock and Watson (2008)); second, a representation of the factor dynamics as a VAR with triangular contemporaneous structure, which renders equation-by-equation estimation feasible; and, third, a specification of volatility as a function of past factors. 

> 14 For another view see Smets and Wouters (2005) who find, based on estimated DSGE model parameters, that frictions in the US and the euro area are remarkably similar. 

22 

When our TV-FAVAR is employed to model a large dataset of US variables over the period 1972-2007, several interesting results emerge. First, we identify minor changes in the factor dynamics and contemporaneous relationships, but much more marked variation in factor volatility and their direct impact on key macroeconomic variables. Therefore, according to our model, both changes in the volatility of the shocks and in their transmission to the economy matter. Second, in-sample forecasts from the TV-FAVAR are more accurate than those from a constant parameter FAVAR for most variables and horizons, and for a few of them the gains are confirmed in a pseudo-real time evaluation, in particular for financial indicators. Third, we illustrate how the TV-FAVAR can be used to identify monetary policy shocks and their transmission to the economy. We find that the volatility of monetary shocks is substantially smaller after the early-1980s and that a constant size shock appears to have smaller e�ects on GDP, prices, inflation expectations, and long-term interest rates over the more recent period, consistent with changes in the conduct of monetary policy and, consequently, a better anchoring of inflation expectations and, possibly, globalization. Moreover, we do not find evidence for the real economy to react di�erently to monetary policy shocks in recession periods compared to expansions. 

### References 

- Bai, J. and Ng, S. (2006). Confidence intervals for di�usion index forecasts with a large number of predictors and inference for factor-augmented regressions. Econometrica, 74:1133—1150. 

- Banerjee, A., Marcellino, M., and Masten, I. (2008). Forecasting macroeconomic variables using di�usion indexes in short samples with structural change. In M. E. Wohar and D. E. Rapach, editors, Forecasting in the Presence of Structural Breaks and Model Uncertainty. Elsevier. 

- Baumeister, C., Liu, P., and Mumtaz, H. (2010). Changes in the transmission of moneetary policy: Evidence from a time-varying factor-augmented VAR. Bank of England Working Paper. 

- Beck, G., Hubrich, K., and Marcellino, M. (2009). Regional inflation dynamics within and across euro area countries and a comparison with the US. Economic Policy, 57:141—184. 

- Benati, L. and Mumtaz, H. (2007). U.S. evolving macroeconomic dynamics - a structural investigation. ECB Working Paper , No. 746. 

- Bernanke, B., Boivin, J., and Eliasz, P. (2005). Measuring the e�ects of monetary policy: a factor-augmented vector autoregressive (FAVAR) approach. The Quarterly Journal of Economics, 120:387—422. 

23 

- Boivin, J. and Giannoni, M. P. (2002). Assessing changes in the monetary transmission mechanism. FRBNY Economic Policy Review , May:97—111. 

- (2006). Has monetary policy become more e�ective? Review of Economics and Statis- 

- tics, 88:445—462. 

- (2010). Global forces and monetary policy e�ectiveness. In J. Galí and M. Gertler, 

- editors, NBER volume on International Dimensions of Monetary Policy, chapter 8, pages 429—488. University of Chicago Press. 

- Boivin, J., Giannoni, M. P., and Mihov, I. (2009). Sticky prices and monetary policy: evidence from disaggregated US data. American Economic Review , 99:350—384. 

- Boivin, J., Kiley, M. T., and Mishkin, F. S. (forthcoming). How has the monetary transmission mechanism changed over time? mimeo, prepared for the Handbook of Monetary Economics. 

- Boivin, J. and Ng, S. (2006). Are more data always better for factor analysis? Journal of Econometrics, 132:169—194. 

- Canova, F. and Gambetti, L. (2009). Structural changes in the US economy: is there a role for monetary policy? Journal of Economic Dynamics and Control , 33:477—490. 

- Cogley, T. and Sargent, T. J. (2005). Drifts and volatilities: monetary policies and outcomes in the post WWII US. Review of Economic Dynamics, 8:262—302. 

- D’Agostino, A., Giannone, D., and Surico, P. (2007). (Un)predictability and macroeconomic stability. CEPR Discussion Paper , No. 6595. 

- Del Negro, M. and Otrok, C. (2008). Dynamic factor models with time-varying parameters: measuring changes in international business cycles. mimeo. 

- Eickmeier, S. (2007). Business cycle transmission from the US to Germany U a structural<sup>˝</sup> factor approach. European Economic Review , 51:521—551. 

- Eickmeier, S. and Hofmann, B. (2010). Monetary policy, housing booms and financial (im)balances. ECB Working Paper , No. 1178. 

- Eickmeier, S., Lemke, W., and Marcellino, M. (2011). The Changing International Transmission of Financial Shocks: Evidence from a Classical Time-Varying FAVAR. Deutsche Bundesbank Discussion Paper 05/2011 . 

- Eickmeier, S. and Ziegler, C. (2008). How successful are dynamic factor models at forecasting output and inflation? A meta-analytic approach. Journal of Forecasting, 27:237—265. 

24 

- Galvao, A. and Marcellino, M. (2010). Endogenous monetary policy regimes and the Great Moderation. CEPR Discussion Paper , No. 7827. 

- Korobilis, D. (2009). Assessing the transmission of monetary policy shocks using dynamic factors models. The Rimini Centre for Economic Analysis Working Paper, No. 35-09. 

- Kose, A., Prasad, E., and Terrones, M. (2006). How do trade and financial integration a�ect the relationship between growth and volatility? Journal of International Economics, 69:176—202. 

- Kose, M. A., Otrok, C., and Whiteman, C. H. (2003). International business cycles: world, regions and country specific factors. American Economic Review , 93:1216—1239. 

- (2008). Understanding the evolution of world business cycles. Journal of International 

- Economics, 75:110—130. 

- Liu, P. and Mumtaz, H. (2009). International transmission of shocks: a time-varying factor augmented VAR approach to the open economy. mimeo. 

- Mumtaz, H. and Surico, P. (2009). The transmission of international shocks: a factoraugmented VAR approach. Journal of Money, Credit and Banking, 41:71—100. 

- (forthcoming). Evolving international inflation dynamics: World and country-specific 

- factors. Journal of the European Economic Association. 

- Nyblom, J. (1989). Testing for the constancy of parameters over time. Journal of the American Statistical Association, 84:223—230. 

- Orphanides, A. (2003). Historical Monetary Policy Analysis and the Taylor Rule. Journal of Monetary Economics, 50:983—1022. 

- Peersman, G. and Smets, F. (2002). Are the e�ects of monetary policy greater in recessions than in booms? In L. Mahadeva and P. Sinclair, editors, Monetary Transmission in Diverse Economies, pages 36—55. Cambridge University Press. 

- Primiceri, G. (2005). Time varying structural vector autoregressions and monetary policy. Review of Economic Studies, 72:821—852. 

- Sims, C. A. and Zha, T. (2006). Were there regime switches in monetary policy? American Economic Review , 96:54—81. 

- Smets, F. and Wouters, R. (2005). Comparing shocks and frictions in US and euro area business cycles: A Bayesian DSGE approach. Journal of Applied Econometrics, 20(2):161—183. 

25 

- Stock, J. and Watson, M. (2002a). Forecasting using principal components from a large number of predictors. Journal of the American Statistical Association, 97:1167— 1179. 

- (2002b). Macroeconomic forecasting using di�usion indexes. Journal of Business and 

- Economic Statistics, 20:147—162. 

- (2005). Implications of dynamic factor models for VAR analysis. NBER Working 

- Paper , No. 11467. 

- (2006). Forecasting with many predictors. In G. Elliott, C. W. Granger, and A. Tim- 

- mermann, editors, Handbook of economic forecasting, volume 1, pages 515—554. Elsevier. 

- (2008). Forecasting in dynamic factor models subject to structural instability. In 

- J. Castle and N. Shepard, editors, The Methodology and Practice of Econometrics, a Festschrift in Honour of Professor David F. Hendry. Oxford University Press. 

- Uhlig, H. (2005). What are the e�ects of monetary policy on output? Results from an agnostic identification approach. Journal of Monetary Economics, 52(2):381—419. 

26 

**Table 1: Tests for autocorrelation of the idiosyncratic errors** 

|Lag|1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|
|Shares of significant autocorrelations|0.06|0.11|0.09|0.11|0.10|0.05|0.04|0.09|0.05|0.05|
|Lag|11|12|13|14|15|16|17|18|19|20|
|Shares of significant autocorrelations|0.04|0.11|0.02|0.03|0.04|0.07|0.06|0.07|0.02|0.04|



Notes: Shares of (N) shocks to the idiosyncratic components for which autocorrelations are significant, i.e. abs(ACF) > 2/sqrt(T). 

28 27 

|ce1995|0.99<br>0.95<br>0.99<br>1.01<br>0.92<br>1.00<br>0.96<br>0.93<br>0.82<br>0.89<br>0.99<br>0.98<br>0.86<br>0.91<br>0.99<br>1.02<br>0.72<br>0.56<br>0.48<br>0.44<br>0.77<br>0.76<br>0.80<br>0.85<br>0.81<br>0.73<br>0.74<br>0.75|
|---|---|
|recessions<br>sin<br>FAVAR,tvvola<br>vs.const.AR|0.67<br>0.70<br>0.79<br>0.82<br>0.67<br>0.86<br>0.86<br>0.85<br>0.50<br>0.69<br>0.78<br>0.84<br>0.61<br>0.66<br>0.79<br>0.83<br>0.72<br>0.60<br>0.54<br>0.55<br>0.70<br>0.63<br>0.74<br>0.82<br>0.69<br>0.63<br>0.69<br>0.73|
|allperiods<br>tv|0.82<br>0.84<br>0.90<br>0.93<br>0.80<br>0.89<br>0.92<br>0.91<br>0.62<br>0.80<br>0.86<br>0.91<br>0.70<br>0.77<br>0.85<br>0.89<br>0.78<br>0.70<br>0.64<br>0.62<br>0.76<br>0.74<br>0.78<br>0.83<br>0.73<br>0.70<br>0.71<br>0.72|
|ce1995|1.01<br>0.96<br>1.00<br>1.01<br>0.95<br>1.02<br>0.99<br>0.97<br>0.83<br>0.90<br>0.99<br>0.98<br>0.91<br>0.93<br>1.00<br>1.01<br>0.77<br>0.61<br>0.52<br>0.49<br>0.80<br>0.80<br>0.80<br>0.82<br>0.87<br>0.79<br>0.78<br>0.75|
|ecessions<br>sin<br>AR,const.vola<br>.const.AR|0.62<br>0.62<br>0.76<br>0.80<br>0.65<br>0.85<br>0.87<br>0.86<br>0.48<br>0.64<br>0.75<br>0.83<br>0.56<br>0.64<br>0.79<br>0.83<br>0.67<br>0.48<br>0.43<br>0.46<br>0.65<br>0.56<br>0.69<br>0.79<br>0.57<br>0.53<br>0.63<br>0.68|
|allperiods<br>r<br>tvFAV<br>vs|0.82<br>0.83<br>0.88<br>0.93<br>0.81<br>0.90<br>0.93<br>0.92<br>0.61<br>0.79<br>0.84<br>0.91<br>0.69<br>0.76<br>0.85<br>0.88<br>0.78<br>0.70<br>0.64<br>0.62<br>0.76<br>0.72<br>0.75<br>0.81<br>0.68<br>0.65<br>0.66<br>0.69|
|nce1995|1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>0.96<br>0.91<br>0.92<br>0.93<br>0.99<br>0.98<br>0.97<br>0.97|
|ecessions<br>si<br>tvAR<br>.const.AR|1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>0.99<br>0.99<br>0.99<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00|
|lperiods<br>r<br>vs|1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>0.99<br>0.98<br>0.98<br>0.98<br>1.00<br>1.00<br>0.99<br>0.99|
|nce1995<br>al|1.02<br>0.97<br>1.07<br>1.10<br>0.97<br>1.16<br>1.12<br>1.13<br>0.88<br>0.92<br>1.06<br>1.08<br>1.01<br>1.00<br>1.07<br>1.10<br>0.79<br>0.65<br>0.57<br>0.56<br>0.78<br>0.84<br>0.89<br>0.95<br>1.02<br>0.97<br>0.95<br>0.89|
|recessions<br>si<br>nst.FAVAR<br>s.const.AR|0.62<br>0.66<br>0.81<br>0.84<br>0.65<br>0.84<br>0.86<br>0.85<br>0.48<br>0.67<br>0.81<br>0.87<br>0.65<br>0.69<br>0.81<br>0.84<br>0.66<br>0.51<br>0.48<br>0.52<br>0.65<br>0.60<br>0.74<br>0.83<br>0.68<br>0.60<br>0.70<br>0.76|
|allperiods<br><br>co<br>v|0.82<br>0.84<br>0.92<br>0.95<br>0.82<br>0.93<br>0.96<br>0.95<br>0.64<br>0.81<br>0.87<br>0.94<br>0.78<br>0.82<br>0.89<br>0.92<br>0.78<br>0.71<br>0.66<br>0.65<br>0.75<br>0.75<br>0.80<br>0.87<br>0.77<br>0.75<br>0.75<br>0.76|
|e1995|0.61<br>0.59<br>0.62<br>0.61<br>0.58<br>0.58<br>0.59<br>0.61<br>0.61<br>0.61<br>0.61<br>0.61<br>0.52<br>0.62<br>0.66<br>0.67<br>0.14<br>0.24<br>0.31<br>0.41<br>0.32<br>0.42<br>0.54<br>0.60<br>0.15<br>0.30<br>0.42<br>0.55|
|t.AR(RMSE)<br>essions<br>sinc|1.42<br>1.53<br>1.65<br>1.68<br>1.61<br>1.67<br>1.72<br>1.74<br>1.67<br>1.70<br>1.73<br>1.74<br>1.45<br>1.68<br>1.74<br>1.80<br>0.36<br>0.68<br>0.90<br>1.06<br>0.97<br>1.47<br>1.68<br>1.78<br>0.47<br>0.86<br>1.04<br>1.21|
|cons<br>llperiods<br>rec|0.93<br>0.96<br>0.98<br>0.99<br>0.93<br>0.94<br>0.95<br>0.96<br>0.98<br>1.00<br>1.00<br>1.00<br>0.88<br>0.96<br>0.98<br>0.99<br>0.20<br>0.38<br>0.53<br>0.65<br>0.59<br>0.83<br>0.93<br>0.98<br>0.26<br>0.47<br>0.62<br>0.73|
|a|1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4|
|h<br>|�GDP<br>�Consumption<br>�Investment<br>�Industrialproduction<br>Unemploymentrate<br>�Employment<br>Capitalutilization|



28 

|ce1995<br>0.91<br>0.94<br>0.84<br>0.90<br>0.84<br>0.82<br>0.92<br>0.87<br>0.80<br>0.82<br>0.92<br>0.86|0.99<br>0.90<br>0.91<br>0.90<br>0.81<br>0.88<br>0.94<br>0.98<br>0.44<br>0.47<br>0.53<br>0.59<br>0.91<br>0.84<br>0.75<br>0.70|
|---|---|
|ecessions<br>sin<br>0.54<br>0.60<br>0.66<br>0.69<br>0.89<br>0.88<br>0.86<br>0.79<br>0.69<br>0.85<br>0.83<br>0.75<br>AVAR,tvvola<br>.const.AR|0.68<br>0.83<br>0.84<br>0.80<br>0.76<br>0.85<br>0.80<br>0.81<br>0.82<br>0.81<br>0.71<br>0.66<br>0.97<br>0.90<br>0.82<br>0.76|
|allperiods<br>r<br>0.78<br>0.78<br>0.77<br>0.74<br>0.83<br>0.84<br>0.88<br>0.81<br>0.77<br>0.82<br>0.87<br>0.81<br>tvF<br>vs|0.81<br>0.83<br>0.85<br>0.83<br>0.79<br>0.84<br>0.86<br>0.89<br>0.76<br>0.77<br>0.73<br>0.73<br>0.93<br>0.89<br>0.84<br>0.80|
|ce1995<br>0.92<br>0.98<br>0.95<br>1.04<br>0.82<br>0.79<br>0.90<br>0.85<br>0.63<br>0.73<br>0.91<br>0.83|0.98<br>0.92<br>0.92<br>0.93<br>0.82<br>0.88<br>0.94<br>0.98<br>0.77<br>0.64<br>0.60<br>0.62<br>0.94<br>0.86<br>0.79<br>0.73|
|ecessions<br>sin<br>0.54<br>0.60<br>0.63<br>0.65<br>0.87<br>0.83<br>0.85<br>0.80<br>0.54<br>0.69<br>0.75<br>0.73<br>AR,const.vola<br>.const.AR|0.67<br>0.79<br>0.79<br>0.76<br>0.77<br>0.83<br>0.77<br>0.79<br>1.01<br>1.02<br>1.01<br>0.81<br>0.93<br>0.84<br>0.78<br>0.69|
|allperiods<br>r<br>0.77<br>0.76<br>0.75<br>0.72<br>0.82<br>0.81<br>0.85<br>0.79<br>0.62<br>0.68<br>0.78<br>0.77<br>tvFAV<br>vs|0.81<br>0.83<br>0.83<br>0.81<br>0.82<br>0.85<br>0.85<br>0.89<br>0.89<br>0.96<br>0.93<br>0.91<br>0.92<br>0.88<br>0.84<br>0.80|
|nce1995<br>0.94<br>0.93<br>0.92<br>0.89<br>1.00<br>1.00<br>1.00<br>1.00<br>0.89<br>0.93<br>1.03<br>0.95|0.99<br>0.99<br>1.00<br>0.99<br>1.00<br>1.00<br>1.00<br>1.01<br>0.78<br>0.89<br>1.09<br>1.35<br>1.00<br>1.00<br>1.00<br>1.00|
|ecessions<br>si<br>0.86<br>0.96<br>0.87<br>0.92<br>1.00<br>1.00<br>1.00<br>1.00<br>0.90<br>0.92<br>0.86<br>0.92<br>tvAR<br>.const.AR|1.00<br>0.99<br>0.99<br>0.99<br>1.00<br>1.00<br>1.00<br>1.00<br>1.19<br>1.62<br>4.41<br>6.39<br>1.00<br>1.00<br>1.00<br>1.00|
|lperiods<br>r<br>0.91<br>1.01<br>1.15<br>1.28<br>1.00<br>1.00<br>1.00<br>1.00<br>0.90<br>0.90<br>0.91<br>0.92<br>vs|0.99<br>0.99<br>1.00<br>0.99<br>1.00<br>1.00<br>1.00<br>1.00<br>1.21<br>1.70<br>2.56<br>4.09<br>1.00<br>1.00<br>1.00<br>1.00|
|nce1995<br>al<br>1.04<br>1.15<br>1.17<br>1.32<br>0.95<br>1.00<br>1.11<br>1.13<br>0.87<br>0.90<br>1.04<br>1.02|0.99<br>0.94<br>0.95<br>0.98<br>0.84<br>0.92<br>0.97<br>1.01<br>0.99<br>0.80<br>0.70<br>0.65<br>0.93<br>0.85<br>0.77<br>0.72|
|cessions<br>si<br>0.55<br>0.61<br>0.68<br>0.73<br>0.86<br>0.85<br>0.84<br>0.80<br>0.65<br>0.77<br>0.77<br>0.74<br>st.FAVAR<br>const.AR|0.70<br>0.84<br>0.85<br>0.82<br>0.79<br>0.86<br>0.81<br>0.81<br>0.76<br>0.80<br>0.76<br>0.69<br>0.92<br>0.84<br>0.76<br>0.68|
|lperiods<br>re<br>0.82<br>0.82<br>0.82<br>0.83<br>0.87<br>0.90<br>0.92<br>0.88<br>0.79<br>0.81<br>0.86<br>0.84<br>con<br>vs.|0.82<br>0.86<br>0.87<br>0.86<br>0.84<br>0.88<br>0.87<br>0.90<br>0.79<br>0.84<br>0.83<br>0.83<br>0.92<br>0.88<br>0.84<br>0.80|
|e1995<br>al<br>0.28<br>0.28<br>0.30<br>0.33<br>0.43<br>0.47<br>0.42<br>0.48<br>0.58<br>0.56<br>0.51<br>0.58|0.66<br>0.71<br>0.70<br>0.75<br>0.87<br>0.85<br>0.84<br>0.81<br>0.11<br>0.22<br>0.32<br>0.41<br>0.16<br>0.24<br>0.28<br>0.34|
|t.AR(RMSE)<br>essions<br>sinc<br>0.52<br>0.73<br>0.86<br>0.98<br>0.59<br>0.75<br>0.86<br>1.09<br>0.84<br>0.93<br>0.96<br>1.19|1.13<br>1.19<br>1.28<br>1.43<br>0.93<br>0.96<br>1.15<br>1.17<br>0.48<br>0.78<br>0.71<br>0.91<br>0.33<br>0.43<br>0.51<br>0.62|
|cons<br>lperiods<br>rec<br>0.41<br>0.50<br>0.55<br>0.60<br>0.48<br>0.56<br>0.57<br>0.66<br>0.60<br>0.67<br>0.66<br>0.76|0.74<br>0.80<br>0.80<br>0.87<br>0.78<br>0.79<br>0.80<br>0.81<br>0.29<br>0.46<br>0.54<br>0.61<br>0.22<br>0.33<br>0.40<br>0.48|
|al<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4|1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4|
|h<br>�GDPdeflator<br>�Personalconsumptiondeflator<br>�CPI<br>|�PPI<br>�Unitlaborcostmanufacturing<br>Federalfundsrate<br>10�yeargovernmentbondyield|



29 

|1995|0.69<br>0.83<br>0.98<br>0.93|0.95<br>1.00<br>0.96<br>0.98<br>0.78<br>0.73<br>0.76<br>0.77<br>0.70<br>0.67<br>0.83<br>0.82<br>0.93<br>0.95<br>0.94<br>0.94<br>0.80<br>0.91<br>0.94<br>0.94|
|---|---|---|
|recessions<br>since<br>FAVAR,tvvola<br>vs.const.AR|1.05<br>1.09<br>0.99<br>0.98|0.73<br>0.72<br>0.70<br>0.71<br>0.70<br>0.72<br>0.83<br>0.93<br>0.70<br>0.68<br>0.74<br>0.71<br>0.84<br>0.95<br>0.97<br>0.98<br>0.65<br>0.78<br>0.77<br>0.81|
|allperiods<br>tv|0.72<br>0.80<br>0.84<br>0.83|0.88<br>0.89<br>0.84<br>0.83<br>0.78<br>0.79<br>0.78<br>0.80<br>0.72<br>0.69<br>0.78<br>0.76<br>0.92<br>0.95<br>0.95<br>0.96<br>0.76<br>0.88<br>0.89<br>0.88|
|ce1995|0.72<br>0.87<br>1.02<br>0.96|0.88<br>0.97<br>0.92<br>0.93<br>0.84<br>0.76<br>0.73<br>0.72<br>0.59<br>0.63<br>0.86<br>0.87<br>0.95<br>0.96<br>0.93<br>0.93<br>0.80<br>0.90<br>0.93<br>0.93|
|ecessions<br>sin<br>AR,const.vola<br>.const.AR|0.95<br>1.05<br>1.01<br>1.01|0.72<br>0.65<br>0.67<br>0.69<br>0.76<br>0.72<br>0.75<br>0.89<br>0.70<br>0.66<br>0.73<br>0.67<br>0.88<br>0.95<br>0.98<br>0.98<br>0.66<br>0.76<br>0.75<br>0.79|
|allperiods<br>r<br>tvFAV<br>vs|0.73<br>0.81<br>0.85<br>0.84|0.84<br>0.85<br>0.80<br>0.79<br>0.84<br>0.79<br>0.76<br>0.77<br>0.66<br>0.67<br>0.80<br>0.80<br>0.93<br>0.95<br>0.95<br>0.96<br>0.78<br>0.88<br>0.90<br>0.89|
|nce1995|1.00<br>1.00<br>1.00<br>1.00|1.00<br>1.00<br>1.00<br>1.00<br>0.99<br>0.98<br>0.98<br>0.99<br>0.88<br>0.85<br>0.96<br>0.93<br>1.00<br>1.00<br>1.00<br>1.00<br>0.96<br>1.00<br>1.00<br>0.99|
|ecessions<br>si<br>tvAR<br>.const.AR|1.00<br>1.00<br>1.00<br>1.00|1.00<br>1.00<br>1.00<br>1.00<br>0.99<br>0.99<br>1.00<br>1.01<br>1.01<br>1.05<br>1.04<br>0.97<br>1.00<br>1.00<br>1.00<br>1.00<br>1.01<br>1.01<br>1.00<br>1.00|
|allperiods<br>r<br>vs|1.00<br>1.00<br>1.00<br>1.00|1.00<br>1.00<br>1.00<br>1.00<br>1.00<br>0.99<br>0.99<br>0.99<br>0.90<br>0.88<br>0.94<br>0.93<br>1.00<br>1.00<br>1.00<br>1.00<br>0.97<br>0.98<br>0.98<br>0.98|
|nce1995|0.89<br>0.99<br>1.08<br>1.06|0.93<br>0.99<br>0.94<br>0.96<br>0.91<br>0.86<br>0.83<br>0.83<br>0.89<br>0.89<br>0.95<br>0.93<br>1.00<br>1.04<br>1.03<br>1.01<br>0.89<br>0.92<br>0.96<br>0.96|
|recessions<br>si<br>nst.FAVAR<br>s.const.AR|1.07<br>1.12<br>1.07<br>1.08|0.74<br>0.70<br>0.72<br>0.73<br>0.84<br>0.84<br>0.86<br>0.95<br>0.85<br>0.73<br>0.77<br>0.76<br>0.89<br>0.99<br>0.98<br>0.99<br>0.69<br>0.76<br>0.75<br>0.79|
|allperiods<br><br>co<br>v|0.82<br>0.90<br>0.92<br>0.89|0.88<br>0.88<br>0.84<br>0.83<br>0.90<br>0.88<br>0.86<br>0.86<br>0.91<br>0.90<br>0.92<br>0.90<br>0.95<br>0.98<br>0.98<br>0.99<br>0.82<br>0.89<br>0.90<br>0.91|
|e1995|0.62<br>0.68<br>0.63<br>0.66|0.81<br>0.82<br>0.89<br>0.90<br>0.54<br>0.66<br>0.78<br>0.85<br>0.95<br>1.08<br>1.00<br>1.02<br>0.88<br>0.90<br>0.91<br>0.92<br>0.90<br>0.90<br>0.93<br>0.93|
|t.AR(RMSE)<br>essions<br>sinc|0.60<br>0.64<br>0.70<br>0.69|0.69<br>0.91<br>1.01<br>1.09<br>0.80<br>1.09<br>1.13<br>1.07<br>0.57<br>0.75<br>0.77<br>0.80<br>1.33<br>1.39<br>1.39<br>1.40<br>0.79<br>0.80<br>0.80<br>0.81|
|cons<br>allperiods<br>rec|0.74<br>0.86<br>0.87<br>0.91|0.65<br>0.75<br>0.86<br>0.92<br>0.60<br>0.76<br>0.83<br>0.87<br>0.69<br>0.85<br>0.87<br>0.92<br>0.99<br>1.00<br>1.00<br>1.00<br>0.93<br>0.92<br>0.98<br>0.98|
||1<br>2<br>3<br>4|1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4<br>1<br>2<br>3<br>4|
|h|�M2|�Consumerloans<br>�C&Iloans<br>�Realestateloans<br>�S&P500<br>�Houseprice|



30 

#### **Table 3: Out-of-sample forecast results** 

#### **(a) Real activity variables** 

|h||RMSE<br>const.AR<br>allperiods|const.FAVAR<br>vs.const.AR<br>allperiods|tvAR<br>vs.const.AR<br>allperiods|tvFAVAR,const.vola<br>vs.const.AR<br>allperiods|tvFAVAR,tvvola<br>vs.const.AR<br>allperiods|
|---|---|---|---|---|---|---|
|�GDP|||||||
||1|0.61|1.11|1.00|1.13|1.14|
||2|0.60|1.08|1.00|1.05|1.11|
||3|0.62|1.22|1.00|1.10|1.08|
||4|0.61|1.27|1.00|1.14|1.12|
|�Consumption|||||||
||1|0.58|1.06|1.00|1.08|1.06|
||2|0.58|1.32|1.00|1.23|1.17|
||3|0.60|1.27|1.00|1.21|1.14|
||4|0.61|1.29|1.00|1.24|1.17|
|�Investment|||||||
||1|0.61|0.99|1.00|0.99|1.03|
||2|0.61|0.99|1.00|1.01|1.05|
||3|0.61|1.19|1.00|1.12|1.08|
||4|0.61|1.24|1.00|1.14|1.13|
|�Industrialproduction|||||||
||1|0.52|1.21|1.00|1.11|1.07|
||2|0.63|1.15|1.00|1.15|1.10|
||3|0.66|1.27|1.00|1.31|1.22|
||4|0.67|1.31|1.00|1.39|1.27|
|Unemploymentrate|||||||
||1|0.14|0.86|1.00|0.93|0.88|
||2|0.25|0.74|1.00|0.81|0.77|
||3|0.32|0.66|1.00|0.68|0.73|
||4|0.42|0.67|1.00|0.62|0.71|
|�Employment|||||||
||1|0.33|0.87|0.99|0.87|0.89|
||2|0.44|1.02|0.98|1.01|1.01|
||3|0.55|1.18|0.97|1.08|1.08|
||4|0.61|1.25|0.98|1.16|1.17|
|Capitalutilization|||||||
||1|0.15|1.14|1.00|1.07|1.14|
||2|0.31|1.05|1.00|0.96|1.06|
||3|0.45|1.01|1.00|0.92|1.03|
||4|0.58|0.96|1.00|0.90|1.02|



32 31 

#### **(b) Inflation and interest rates** 

|h||RMSE<br>const.AR<br>allperiods|const.FAVAR<br>vs.const.AR<br>allperiods|tvAR<br>vs.const.AR<br>allperiods|tvFAVAR,const.vola<br>vs.const.AR<br>allperiods|tvFAVAR,tvvola<br>vs.const.AR<br>allperiods|
|---|---|---|---|---|---|---|
|�GDPdeflator|||||||
||1|0.29|1.17|1.05|1.12|1.09|
||2|0.29|1.30|1.10|1.15|1.20|
||3|0.30|1.35|1.14|1.16|1.19|
||4|0.34|1.51|1.21|1.26|1.24|
|�Personalconsumptiondeflator|||||||
||1|0.44|1.05|1.00|0.99|0.96|
||2|0.47|1.12|1.00|1.01|0.98|
||3|0.42|1.26|1.00|1.13|1.05|
||4|0.48|1.28|1.00|1.13|1.04|
|�CPI|||||||
||1|0.60|0.95|1.04|0.87|0.87|
||2|0.58|0.97|1.08|0.93|0.89|
||3|0.50|1.16|1.16|1.12|1.07|
||4|0.59|1.12|1.19|1.07|1.00|
|�PPI|||||||
||1|0.66|1.07|1.00|1.07|1.08|
||2|0.72|1.02|1.00|1.00|1.00|
||3|0.70|1.02|1.00|0.99|0.98|
||4|0.75|1.06|1.00|1.01|1.02|
|�Unitlaborcostmanufacturing|||||||
||1|0.90|0.90|1.01|0.97|0.94|
||2|0.85|0.97|1.03|0.97|0.96|
||3|0.85|1.01|1.03|1.01|0.99|
||4|0.80|1.06|1.03|1.06|1.07|
|Federalfundsrate|||||||
||1|0.12|1.15|1.12|0.96|0.74|
||2|0.23|0.91|1.24|0.85|0.80|
||3|0.33|0.77|1.39|0.78|0.85|
||4|0.42|0.71|1.62|0.76|0.87|
|10�yeargovernmentbondyield|||||||
||1|0.16|1.02|1.06|1.02|1.06|
||2|0.25|0.91|1.13|0.94|1.05|
||3|0.29|0.83|1.18|0.89|1.00|
||4|0.36|0.77|1.19|0.83|0.95|



33 32 

#### **(c) Money, credit and asset prices** 

|h||RMSE<br>const.AR<br>allperiods|const.FAVAR<br>vs.const.AR<br>allperiods|tvAR<br>vs.const.AR<br>allperiods|tvFAVAR,const.vola<br>vs.const.AR<br>allperiods|tvFAVAR,tvvola<br>vs.const.AR<br>allperiods|
|---|---|---|---|---|---|---|
|�M2|||||||
||1|0.63|0.96|1.03|0.99|0.95|
||2|0.69|1.06|1.04|1.06|1.08|
||3|0.64|1.15|1.05|1.21|1.26|
||4|0.67|1.13|1.04|1.15|1.25|
|�Consumerloans|||||||
||1|0.89|0.94|1.02|0.98|0.94|
||2|0.84|1.03|1.00|1.02|1.02|
||3|0.92|0.98|1.00|0.98|0.97|
||4|0.92|1.03|1.01|1.03|0.98|
|�C&Iloans|||||||
||1|0.55|0.98|1.00|0.98|1.11|
||2|0.69|0.91|1.00|0.91|1.06|
||3|0.81|0.85|1.01|0.82|0.97|
||4|0.88|0.86|1.02|0.82|0.96|
|�Realestateloans|||||||
||1|1.00|0.97|0.94|0.86|0.90|
||2|1.16|0.96|0.94|0.79|0.85|
||3|1.06|1.02|0.99|1.02|0.99|
||4|1.09|1.02|0.98|0.98|0.95|
|�S&P500|||||||
||1|0.90|1.13|1.00|1.12|1.08|
||2|0.91|1.15|1.00|1.09|1.07|
||3|0.92|1.10|1.00|1.04|1.01|
||4|0.92|1.07|1.00|1.05|1.07|
|�Houseprice|||||||
||1|0.92|0.97|0.98|0.95|0.92|
||2|0.90|0.94|1.00|0.95|0.94|
||3|0.92|0.99|1.00|0.99|0.97|
||4|0.93|0.98|0.99|0.99|0.96|



Notes: A shaded area indicates the minimum of the relative RMSE in the specific row if it is below 1. 

34 33 

|Results<br> Reactions of GDP, consumption and investment have weakened over time.<br>Effect on prices has become stronger until the mid-1990s and roughly unchanged<br>thereafter. Impact on the Federal Funds rate has become stronger and longer-<br>lasting.<br> Rise in the contemporaneous impact on inflation over time.<br>Significant short-run decline in output growth in 1997 and 1992, decline in<br>output growth not significant anymore in 2002. More persistent impact on<br>the Federal Funds rate over time.<br> Strong significant decline in output only in first sample, weak significant responses<br>thereafter. Stronger response of inflation in first compared to the second sample,<br> and slightly stronger response in third compared to second the sample. However,<br>inflation impulse responses are never significant. More persistent rise in Federal<br>Funds rate in third sample than in previous sample periods.<br> Weaker output, inflation and interest rate responses over time.<br> No differences of interest rate, activity and price responses at short horizons.<br> At medium horizons, Federal Funds rate increases more, GDP, investment<br>and prices decline less after a monetary tightening. Responses of consumption<br>for all horizons unchanged.|
|---|
|Period(s)<br>1960-2008 <br>s 1959-2005 <br>1963-1979,<br>1980-1997,<br>1994-1997 <br>1959-1979,<br>1979-2002<br>1984-1999 <br>2000-2005|
|Identification<br>Recursive<br>Sign restriction<br>Recursive<br>Recursive<br>Recursive|
|Model<br>TV-FAVAR<br>TV-VAR<br>VAR, sample split<br>VAR, sample split<br>FAVAR, sample split|
|dy<br>meister et al. (2010)<br>ati and Mumtaz (2007)<br>vin and Giannoni (2002)<br>vin and Giannoni (2006)<br>vin and Giannoni (2010)|
|Stu<br>Bau<br>Ben<br>Boi<br>Boi<br>Boi|



34 

|rease becomes more persistent over time, but less<br>st period. GDP response weakens over time but becomes<br>t period. CPI response is weaker in 1984-2008 than in the<br>nflation and output growth is higher in the 1990s<br>s and 1980s. The largest responses are found for 1996|r responses.become slightly weaker over time.|Funds rate slightly more persistent in 1981 than in<br>er GDP response in 1981 than in 1975 and 1996.<br>become weaker in 1981 compared to 1975 and<br>, but less strong than in 1975.|inflation and unemployment responses over time.|
|---|---|---|---|
|Results<br>Federal Funds rate inc<br>persistent again in late<br>stronger again in lates<br> other sample periods.<br> Short-term impact on i<br>compared to the 1970<br>and 2006.|GDP and GDP deflato|Impact on the Federal<br>1975 and 1996. Weak<br>Inflation response has<br>stronger again in 1996|No notable changes in|
|Period(s)<br>1966-1979,<br>1979-2008,<br>1984-2008,<br>1994-2008 <br> 1967-2006|1975-2007,<br>1987-2007|1959-2006|1953-2001|
|Identification<br>Recursive<br>Sign restrictions|Combination of<br>recursive and<br>sign restrictions|Recursive|Recursive|
|Model<br>FAVAR, sample split<br>TV-VAR|FAVAR, sample split|TV-FAVAR|TV-VAR|
|al. (2009)<br>and Gambetti (2009)|er and Hofmann (2010)|(2009)|i (2005)|
|et<br>a|ei|lis|er|
|Study<br>Boivin<br>Canov|Eickm|Korobi|Primic|



35 

**Figure 1: Factor estimates** 



<!-- Start of picture text -->
Factor 1 Factor 2 Factor 3 Factor 4 Factor 5<br>2<br>1 2 3 2<br>0 10 10 2 10<br>1 -1<br>-1 Principal component -1 -1<br>Re-est regression 0 -2<br>-2 Re-est state space -2 -2 -1 -3<br>-3 -3 -4<br>1980 1990 2000 1980 1990 2000 1980 1990 2000 1980 1990 2000 1980 1990 2000<br><!-- End of picture text -->

**Figure 2: Tests for autocorrelation of the standardized VAR residuals** 



<!-- Start of picture text -->
Factor 1 Factor 2 Factor 3 Factor 4 Factor 5<br>0.5 0.5 0.5 0.5 0.5<br>0 0 0 0 0<br>-0.5 -0.5 -0.5 -0.5 -0.5<br>5 10 15 20 5 10 15 20 5 10 15 20 5 10 15 20 5 10 15 20<br>Lag k<br><!-- End of picture text -->

Notes: The blue bars are the autocorrelations. The red lines are the approximate two standard error bounds computed as 2/sqrt(T). 

**Figure 3: Time-varying volatility of the monetary policy shock** 



<!-- Start of picture text -->
0.8<br>0.7<br>0.6<br>0.5<br>0.4<br>0.3<br>0.2<br>0.1<br>1975 1980 1985 1990 1995 2000 2005<br><!-- End of picture text -->

37 36 

#### **Figure 4: Impulse response functions of key variables** 

#### **(a) from a constant parameter FAVAR (solid) and the TV-FAVAR (averages over all periods) (dotted)** 



<!-- Start of picture text -->
Federal funds rate GDP GDP deflator<br>0<br>0.8 0 -0.2<br>-0.1<br>0.6 -0.4<br>-0.2<br>0.4<br>-0.6<br>-0.3<br>0.2<br>-0.8<br>-0.4<br>0<br>-0.5 -1<br>-0.2<br>0 5 10 15 20 0 5 10 15 20 0 5 10 15 20<br><!-- End of picture text -->

#### **(b) from the TV-FAVAR (all horizons and points in time)** 



<!-- Start of picture text -->
Federal funds rate GDP GDP deflator<br>1 0.4<br>0.2 -0.2<br>0.5 0 -0.4<br>-0.2 -0.6<br>-0.4 -0.8<br>0 -0.6 -1<br>-0.8 -1.2<br>2000 20 2000 20 2000 20<br>1990 1990 1990<br>10 10 10<br>1980 1980 1980<br>0 0 0<br><!-- End of picture text -->

#### **(c) from the TV-FAVAR (selected horizons)** 



Notes: Impulse responses to an unexpected increase of the monetary policy rate by 1 percentage point. Impulse responses of GDP and the GDP deflator are in percent. The dotted lines in panel (c) are 90% confidence bands. Shaded areas are NBER recessions. 

38 

37 

**Figure 5: Impulse response functions of additional activity and price variables** 

**(a) from a constant parameter FAVAR (solid) and the TV-FAVAR (averages over all periods) (dotted)** 



<!-- Start of picture text -->
Consumption Investment Industrial production Employment<br>0.3 0<br>0 0<br>0.2 -0.1<br>-0.2<br>-0.5<br>0.1 -0.4 -0.2<br>-1 -0.3<br>0 -0.6<br>-1.5 -0.4<br>-0.1 -0.8<br>-2 -0.5<br>-0.2 -1<br>-2.5 -0.6<br>-0.3 -1.2<br>0 5 10 15 20 0 5 10 15 20 0 5 10 15 20 0 5 10 15 20<br>CPI PPI finished goods PCE deflator Unit labor costs<br>0 0 0 0<br>-0.2 -0.5 -0.2 -0.2<br>-0.4 -0.4 -0.4<br>-0.6 -1<br>-0.6 -0.6<br>-0.8<br>-1.5 -0.8 -0.8<br>-1<br>-1.2 -2 -1 -1<br>-1.4 -1.2 -1.2<br>0 5 10 15 20 0 5 10 15 20 0 5 10 15 20 0 5 10 15 20<br><!-- End of picture text -->

#### **(b) from the TV-FAVAR (all horizons and points in time)** 



<!-- Start of picture text -->
Consumption Investment Industrial production Employment<br>0.4 1<br>1 0<br>0.2 0<br>-0.2<br>-1 0<br>0 -2 -0.4<br>-0.2 -3 -1 -0.6<br>2000 20 2000 20 2000 20 2000 20<br>1990 10 1990 10 1990 10 1990 10<br>1980 1980 1980 1980<br>0 0 0 0<br>CPI PPI finished goods PCE deflator Unit labor costs<br>0 0 0<br>-0.5<br>-0.5 -1 -0.5 -0.5<br>-1 -1.5<br>-1.5 -2 -1 -1<br>-2.5<br>2000 20 2000 20 2000 20 2000 20<br>1990 10 1990 10 1990 10 1990 10<br>1980 1980 1980 1980<br>0 0 0 0<br><!-- End of picture text -->

39 38 

#### **(c) from the TV-FAVAR (selected horizons)** 





Notes: Impulse responses to an unexpected increase of the monetary policy rate by 1 percentage point. The dotted lines in panel (c) are 90% confidence bands. Impulse responses are in percent. Shaded areas are NBER recessions. 

40 39 

#### **Figure 6: Impulse response functions of inflation expectations and long-term government bond yields** 

#### **(a) from a constant parameter FAVAR (solid) and the TV-FAVAR (averages over all periods) (dotted)** 



<!-- Start of picture text -->
Inflexp 1y SPF Inflexp 1y Mich 10y government bond yield<br>0<br>0.1<br>0.4<br>-0.05<br>0.05<br>0.3<br>-0.1<br>0<br>0.2<br>-0.15<br>-0.05<br>0.1<br>-0.1 -0.2<br>0<br>-0.15 -0.25<br>-0.1<br>0 5 10 15 20 0 5 10 15 20 0 5 10 15 20<br><!-- End of picture text -->

#### **(a) from the TV-FAVAR (all horizons and points in time)** 



<!-- Start of picture text -->
Inflexp 1y SPF Inflexp 1y Mich 10y government bond yield<br>0.1 0.4<br>0.05 0 0.3<br>0 -0.1 0.2<br>-0.05 0.1<br>-0.1 -0.2 0<br>-0.15 -0.3 -0.1<br>2000 20 2000 20 2000 20<br>1990 1990 1990<br>10 10 10<br>1980 1980 1980<br>0 0 0<br><!-- End of picture text -->

#### **(c) from the TV-FAVAR (selected horizons)** 



Notes: Impulse responses to an unexpected increase of the monetary policy rate by 1 percentage point. Impulse responses are in percentage points. The dotted lines in panel (c) are 90% confidence bands. Shaded areas are NBER recessions. 

41 

40 

41 

|Transf. Slow/Fast Core?<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>C<br>lv<br>S<br>C<br>lv<br>S<br>C<br>lv<br>S<br>C<br>lv<br>S<br>C<br>lv<br>S<br>C<br>lv<br>S<br>C<br>lv<br>S<br>lv<br>S<br>lv<br>S<br>lv<br>S<br>lv<br>S<br>lv<br>S<br>lv<br>S<br>lv<br>S<br>lv<br>S<br>lv<br>S<br>lv<br>S<br>lv<br>S|
|---|
|Source<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>Bureau of Census<br>Bureau of Census<br>Bureau of Census<br>Bureau of Census<br>Bureau of Census<br>Bureau of Census<br>Bureau of Census<br>Bureau of Census<br>Bureau of Census<br>Bureau of Census<br>Bureau of Census<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB|
|# Variable<br>41 Leather and allied product  NAICS=316, SA<br>42 Paper  NAICS=322, SA<br>43 Petroleum and coal products  NAICS=324, SA<br>44 Chemical  NAICS=325, SA<br>45 Plastics and rubber products  NAICS=326, SA<br>46 Plastics product  NAICS=3261, SA<br>47 Nondurable manufacturing (NAICS), SA<br>48 Mining  NAICS=21, SA<br>49 Oil and gas extraction  NAICS=211, SA<br>50 Mining (except oil and gas)  NAICS=212, SA<br>51 Support activities for mining  NAICS=213, SA<br>52 New orders, construction supplies<br>53 New orders, consumer goods<br>54 New orders, durables excluding capital goods<br>55 New orders, durables excluding defense<br>56 New orders, durable goods total<br>57 New orders, nondurable goods total<br>58 New orders, total manufacturing<br>59 New orders, manufacturing excluding defense<br>60 New orders, manufacturing excluding transportation<br>61 New orders, capital goods<br>62 Estimated Monthly Retail Sales-Retail sales, total, ($mil., SA)<br>63 Capacity utilization, Manufacturing (SIC)<br>64 Capacity utilization, Total index<br>65 Capacity utilization, Crude processing<br>66 Capacity utilization, Primary & semifinished processing<br>67 Capacity utilization, Finished processing<br>68 Capacity utilization, Mining  NAICS=21<br>69 Capacity utilization, Nonmetallic mineral mining and quarrying  NAICS=2123<br>70 Capacity utilization, Textiles and products  NAICS=313,4<br>71 Capacity utilization, Textile product mills  NAICS=314<br>72 Capacity utilization, Apparel  NAICS=315<br>73 Capacity utilization, Apparel and leather goods  NAICS=315,6<br>74 Capacity utilization, Wood product  NAICS=321<br>75 Capacity utilization, Paper  NAICS=322<br>76 Capacity utilization, Petroleum and coal products  NAICS=324<br>77 Capacity utilization, Chemical  NAICS=325<br>78 Capacity utilization, Plastics and rubber products  NAICS=326<br>79 Capacity utilization, Nonmetallic mineral product  NAICS=327<br>80 Capacity utilization, Primary metal  NAICS=331|



42 

43 

|Transf. Slow/Fast Core?<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>F<br>C<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S|
|---|
|Source<br>BEA, NIPA<br>BEA, NIPA<br>BEA, NIPA<br>BEA, NIPA<br>BEA, NIPA<br>BEA, NIPA<br>BEA, NIPA<br>BEA, NIPA<br>BEA, NIPA<br>BEA, NIPA<br>BEA, NIPA<br>Bureau of Census<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)<br>Baumeister et al. (2010)|
|# Variable<br>121 Deflator, Private Investment<br>122 Deflator, Private fixed investment<br>123 Deflator, Private fixed investment, Nonresidential<br>124 Deflator, Private fixed investment, Nonresidential, Equipment and software<br>125 Deflator, Exports<br>126 Deflator, Exports, Goods<br>127 Deflator, Exports, Services<br>128 Deflator, Exports, Imports<br>129 Deflator, Imports, Goods<br>130 Deflator, Government expenditure<br>131 Deflator, Government expenditure, State and local<br>132 Residential Property Price, cst quality Laspeyres price index of new one-family houses sold<br>133 Deflator, PCE, Total<br>134 Deflator, PCE, Video and audio goods including musical instruments and computer goods (91)<br>135 Deflator, PCE, Other foods<br>136 Deflator, PCE, Elementary and secondary school lunch<br>137 Deflator, PCE, Higher education school lunch<br>138 Deflator, PCE, Other purchased meals<br>139 Deflator, PCE, Food supplied civilians<br>140 Deflator, PCE, Food supplied military<br>141 Deflator, PCE, Standard clothing issued to military personnel<br>142 Deflator, PCE, Other personal hygiene goods<br>143 Deflator, PCE, Prescription drugs<br>144 Deflator, PCE, Nonprescription drugs<br>145 Deflator, PCE, Gynecological goods<br>146 Deflator, PCE, Less: Personal remittances in kind to nonresidents<br>147 Deflator, PCE, Tenant occupied stationary homes<br>148 Deflator, PCE, Clubs and fraternity housing<br>149 Deflator, PCE, Rental value of farm dwellings less household insurance benefits paid<br>150 Deflator, PCE, Rug and furniture cleaning<br>151 Deflator, PCE, Motor vehicle repair<br>152 Deflator, PCE, Physicians (47)<br>153 Deflator, PCE, Nonprofit<br>154 Deflator, PCE, Proprietary<br>155 Deflator, PCE, Government<br>156 Deflator, PCE, Nursing homes<br>157 Deflator, PCE, Casino gambling<br>158 Deflator, PCE, Drycleaning<br>159 Deflator, PCE, Laundry and garment repair<br>160 Deflator, PCE, Miscellaneous personal services|



44 

45 

|Transf. Slow/Fast Core?<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>S<br>C<br>dln<br>F|
|---|
|Source<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>BLS<br>OECD (MEI)<br>OECD (MEI)<br>OECD (MEI)<br>OECD (MEI)<br>OECD (MEI)<br>OECD (MEI)<br>OECD (MEI)<br>OECD (MEI)<br>Baumeister et al. (2010)|
|# Variable<br>201 CPI: Urban Consumer - All items less shelter, (1982-84=100, SA)<br>202 CPI: Urban Consumer - All items less medical care, (1982-84=100, SA)<br>203 CPI: Urban Consumer - Commodities less food, (1982-84=100, SA)<br>204 CPI: Urban Consumer - Nondurables, (1982-84=100, SA)<br>205 CPI: Urban Consumer - Energy, (1982-84=100, SA)<br>206 CPI: Urban Consumer - All items less energy, (1982-84=100, SA)<br>207 CPI: Urban Consumer - All items less food and energy, (1982-84=100, SA)<br>208 CPI: Urban Consumer - Commodities less food and energy commodities, (1982-84=100, SA)<br>209 CPI: Urban Consumer - Services less energy services, (1982-84=100, SA)<br>210 CPI: Urban Wage Earner - All items, (1982-84=100, SA)<br>211 CPI: Urban Wage Earner - Food away from home, (1982-84=100, SA)<br>212 CPI: Urban Wage Earner - Housing, (1982-84=100, SA)<br>213 CPI: Urban Wage Earner - Household furnishings and operations, (1982-84=100, SA)<br>214 CPI: Urban Wage Earner - Motor vehicle maintenance and repair, (1982-84=100, SA)<br>215 CPI: Urban Wage Earner - Medical care, (1982-84=100, SA)<br>216 CPI: Urban Wage Earner - Medical care commodities, (1982-84=100, SA)<br>217 CPI: Urban Wage Earner - Medical care services, (1982-84=100, SA)<br>218 CPI: Urban Wage Earner - All items less energy, (1982-84=100, SA)<br>219 CPI: Urban Wage Earner - All items less food and energy, (1982-84=100, SA)<br>220 CPI: Urban Wage Earner - Commodities less food and energy commodities, (1982-84=100, SA)<br>221 CPI: Urban Wage Earner - Services less energy services, (1982-84=100, SA)<br>222 PPI: Stage of processing - Finished goods, (Index 1982=100, SA)<br>223 PPI: Stage of processing - Finished consumer goods, (Index 1982=100, SA)<br>224 PPI: Stage of processing - Finished consumer foods, (Index 1982=100, SA)<br>225 PPI: Stage of processing - Finished consumer goods excluding foods, (Index 1982=100, SA)<br>226 PPI: Stage of processing - Consumer nondurable goods less food, (Index 1982=100, SA)<br>227 PPI: Stage of processing - Capital equipment, (Index 1982=100, SA)<br>228 PPI: Stage of processing - Intermediate materials;supplies and components, (Index 1982=100, SA)<br>229 PPI: Stage of processing - Crude materials, (Index 1982=100, SA)<br>230 PPI: Stage of processing - Finished goods; excluding foods, (Index 1982=100, SA)<br>231 PPI: Stage of processing - Intermediate materials less foods and feeds, (Index 1982=100, SA)<br>232 Labour compensation, Earnings, Manufacturing, Hourly<br>233 Labour compensation, Earnings, Private sector, Hourly<br>234 Unit Labour Costs, Total<br>235 Unit Labour Costs, Manufacturing<br>236 Unit Labour Costs, Industry<br>237 Unit Labour Costs, Construction<br>238 Unit Labour Costs, Market Services<br>239 Unit Labour Costs, Business Sector<br>240 Commodity prices, Hardware|



46 

47 

|Transf. Slow/Fast Core?<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>C<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>C<br>lv<br>F<br>C<br>lv<br>F<br>C<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>dln<br>F<br>C<br>dln<br>F<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>dln<br>F<br>dln<br>F<br>C<br>dln<br>F<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>C<br>dln<br>F<br>C|
|---|
|Source<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>FRB<br>FRB<br>FRB<br>FRB<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>Global Financial Data<br>FRB<br>FRB<br>FRB<br>FRB<br>FRB|
|# Variable<br>281 Moody's BAA Utility Bond Yield<br>282 Moody's AA Utility Bond Yield<br>283 Moody's Corporate BAA Yield<br>284 Moody's Corporate A Yield<br>285 Moody's Corporate AA Yield<br>286 Moody's A Industrial Bond Yield<br>287 Moody's BAA Industrial Bond Yield<br>288 30-year Fixed Mortgage Lending Rate<br>289 Finance Company: Interest Rate New Car Loan, (%)<br>290 Finance Company: Interest Rate Used Car Loan, (%)<br>291 C&I loan rate<br>292 24 m personal loan rate<br>293 Moody's 10-year AAA Municipal Bonds Yield<br>294 Moody's 10-year AA Municipal Bonds Yield<br>295 Moody's 20-year AAA Municipal Bond Yield<br>296 Moody's 20-year BAA Municipal Bond Yield<br>297 Moody's 20-year A Municipal Bond Yield<br>298 Moody's 20-year AA Municipal Bond Yield<br>299 Moody's Municipal Bond 20-year Composite Yield<br>300 S&P 500® Composite Price Index<br>301 Nasdaq: Composite Index, (Index Feb 05 1971=100)<br>302 S&P 500® Consumer Discretionary (25)<br>303 S&P 500® Retailing (255)<br>304 S&P Retail Composite<br>305 S&P 500® Apparel<br>306 S&P 500® Textiles<br>307 S&P 500® Consumer Staples (30)<br>308 S&P 500® Oil<br>309 S&P 500® Industrials (20)<br>310 S&P 500® Building Products (2012)<br>311 S&P 500® Industrial Conglomerates (2015)<br>312 S&P 500® Capital Goods (201)<br>313 S&P 500® Chemicals Composite (1511)<br>314 S&P Chemical Composite<br>315 S&P 500® Utilities (55)<br>316 Reserves: Total reserves adjusted for changes in reserve requirements, (Mil. $, SA)<br>317 Reserves: Nonborrowed reserves adjusted for changes in reserve requirements, (Mil. $, SA)<br>318 Reserves: Monetary base adjusted for changes in reserve requirements, (Mil. $, SA)<br>319 Money Stock; M1, (SA Billions $)<br>320 Money Stock; M2, (SA Billions $)|



48 

|Core?<br>C<br>C<br>C<br>C<br>C<br>C<br>C<br>C<br>C<br>C<br>C<br>C<br>set of|
|---|
|Transf. Slow/Fast<br>dln<br>F<br>dln<br>F<br>dln<br>F<br>dln<br>F<br>dln<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>dln<br>F<br>dln<br>F<br>dln<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>lv<br>F<br>variable belong to the|
|Source<br>FRB<br>FRB<br>FRB<br>FRB<br>OECD (MEI)<br>OECD (MEI)<br>OECD (MEI)<br>OECD (MEI)<br>BIS<br>BIS<br>BIS<br>Federal Reserve Bank of Philadelphia<br>Federal Reserve Bank of Philadelphia<br>Federal Reserve Bank of Philadelphia<br>SPF<br>University of Michigan<br>F) variable in fifth column; whether a|
|Industrial Loans at All Commercial Banks<br>idual) Loans at All Commercial Banks<br>ns at All Commercial Banks<br>Credit Outstanding<br>Confidence indicator sa / Quantum (non-additive or stock figures) SA<br>Employment: tendency sa / Quantum (non-additive or stock figures) SA<br>Orders inflow/Demand: tendency sa / Quantum (non-additive or stock figures) SA<br>Production: tendency sa / Quantum (non-additive or stock figures) SA<br>ng indicator<br>in manufacturing<br>ctations index<br>Outlook Survey: New Orders - 6 months ahead vs. current month, (Diffusion Index, SA)<br>Outlook Survey: Prices paid - 6 months ahead vs. current month, (Diffusion Index, SA)<br>Outlook Survey: Prices received - 6 months ahead vs. current month, (Diffusion Index, SA)<br>pectations PGDP 1 year<br>tion expectations 1 year<br>in fourth column: lv: level, dln: differences of logarithm; slow- (S) or fast-moving (<br>er a variable is included_a priori_in the dataset (C), or not (empty space).|
|# Variable<br>321 Commercial and<br>322 Consumer (Indiv<br>323 Real Estate Loa<br>324 Total Consumer<br>325 Manufacturing -<br>326 Manufacturing -<br>327 Manufacturing -<br>328 Manufacturing -<br>329 Composite leadi<br>330 Business activity<br>331 Consumer expe<br>332 Phila Fed Bus.<br>333 Phila Fed Bus.<br>334 Phila Fed Bus.<br>335 SPF Inflation ex<br>336 U Michigan Infla<br>Notes: Transformations<br>core variables, i.e. wheth|



49 

## **The following Discussion Papers have been published since 2010:** 

#### **Series 1: Economic Studies** 

|01|2010|Optimal monetary policy in a small open<br>economy with financial frictions|Rossana Merola|
|---|---|---|---|
|02|2010|Price, wage and employment response<br>to shocks: evidence from the WDN survey|Bertola, Dabusinskas<br>Hoeberichts, Izquierdo, Kwapil<br>Montornès, Radowski|
|03|2010|Exports versus FDI revisited:<br>Does finance matter?|C. M. Buch, I. Kesternich<br>A. Lipponer, M. Schnitzer|
|04|2010|Heterogeneity in money holdings<br>across euro area countries:|Ralph Setzer<br>Paul van den Noord|
|||the role of housing|Guntram Wolff|
|05|2010|Loan supply in Germany<br>during the financial crises|U. Busch<br>M. Scharnagl, J. Scheithauer|
|06|2010|Empirical simultaneous confidence<br>regions for path-forecasts|Òscar Jordà, Malte Knüppel<br>Massimiliano Marcellino|
|07|2010|Monetary policy, housing booms<br>and financial (im)balances|Sandra Eickmeier<br>Boris Hofmann|
|08|2010|On the nonlinear influence of<br>Reserve Bank of Australia|Stefan Reitz<br>Jan C. Ruelke|
|||interventions on exchange rates|Mark P. Taylor|
|09|2010|Banking and sovereign risk<br>in the euro area|S. Gerlach<br>A. Schulz, G. B. Wolff|
|10|2010|Trend and cycle features in German<br>residential investment before and after<br>reunification|Thomas A. Knetsch|



50 

|11|2010|What can EMU countries’ sovereign<br>bond spreads tell us about market||
|---|---|---|---|
|||perceptions of default probabilities|Niko Dötz|
|||during the recent financial crisis?|Christoph Fischer|
|12|2010|User costs of housing when households face<br>a credit constraint – evidence for Germany|Tobias Dümmler<br>Stephan Kienle|
|13|2010|Extraordinary measures in extraordinary times–||
|||public measures in support of the financial|Stéphanie Marie Stolz|
|||sector in the EU and the United States|Michael Wedow|
|14|2010|The discontinuous integration of Western<br>Europe’s heterogeneous market for||
|||corporate control from 1995 to 2007|Rainer Frey|
|15|2010|Bubbles and incentives:|Ulf von Kalckreuth|
|||a post-mortem of the Neuer Markt in Germany|Leonid Silbermann|
|16|2010|Rapid demographic change and the allocation<br>of public education resources: evidence from||
|||East Germany|Gerhard Kempkes|
|17|2010|The determinants of cross-border bank flows<br>to emerging markets–new empirical evidence|Sabine Herrmann|
|||on the spread of financial crisis|Dubravko Mihaljek|
|18|2010|Government expenditures and unemployment:<br>a DSGE perspective|Eric Mayer, Stéphane Moyen<br>Nikolai Stähler|
|19|2010|NAIRU estimates for Germany: new evidence<br>on the inflation-unemployment trade-off|Florian Kajuth|
|20|2010|Macroeconomic factors and|Claudia M. Buch|
|||micro-level bank risk|Sandra Eickmeier, Esteban Prieto|



51 

|21|2010|How useful is the carry-over effect<br>for short-term economic forecasting?|Karl-Heinz Tödter|
|---|---|---|---|
|22|2010|Deep habits and the macroeconomic effects<br>of government debt|Rym Aloui|
|23|2010|Price-level targeting<br>when there is price-level drift|C. Gerberding<br>R. Gerke, F. Hammermann|
|24|2010|The home bias in equities<br>and distribution costs|P. Harms<br>M. Hoffmann, C. Ortseifer|
|25|2010|Instability and indeterminacy in|Michael Krause|
|||a simple search and matching model|Thomas Lubik|
|26|2010|Toward a Taylor rule for fiscal policy|M. Kliem, A. Kriwoluzky|
|27|2010|Forecast uncertainty and the||
|||Bank of England interest rate decisions|Guido Schultefrankenfeld|
|01|2011|Long-run growth expectations|M. Hoffmann|
|||and “global imbalances”|M. Krause, T. Laubach|
|02|2011|Robust monetary policy in a||
|||New Keynesian model with imperfect|Rafael Gerke|
|||interest rate pass-through|Felix Hammermann|
|03|2011|The impact of fiscal policy on<br>economic activity over the business cycle –|Anja Baum|
|||evidence from a threshold VAR analysis|Gerrit B. Koester|
|04|2011|Classical time-varying FAVAR models –|S. Eickmeier|
|||estimation, forecasting and structural analysis|W. Lemke, M. Marcellino|



52 

#### **Series 2: Banking and Financial Studies** 

|01|2010|Deriving the term structure of banking|Stefan Eichler|
|---|---|---|---|
|||crisis risk with a compound option|Alexander Karmann|
|||approach: the case of Kazakhstan|Dominik Maltritz|
|02|2010|Recovery determinants of distressed banks:<br>Regulators, market discipline,|Thomas Kick<br>Michael Koetter|
|||or the environment?|Tigran Poghosyan|
|03|2010|Purchase and redemption decisions of mutual<br>fund investors and the role of fund families|Stephan Jank<br>Michael Wedow|
|04|2010|What drives portfolio investments of<br>German banks in emerging capital markets?|Christian Wildmann|
|05|2010|Bank liquidity creation and<br>risk taking during distress|Berger, Bouwman<br>Kick, Schaeck|
|06|2010|Performance and regulatory effects of<br>non-compliant loans in German synthetic||
|||mortgage-backed securities transactions|Gaby Trinkaus|
|07|2010|Banks’ exposure to interest rate risk, their<br>earnings from term transformation, and||
|||the dynamics of the term structure|Christoph Memmel|
|08|2010|Completeness, interconnectedness and<br>distribution of interbank exposures–<br>a parameterized analysis of the stability||
|||of financial networks|Angelika Sachs|
|09|2010|Do banks benefit from internationalization?|C. M. Buch|
|||Revisiting the market power-risk nexus|C. Tahmee Koch, M. Koetter|



53 

|10|2010|Do specialization benefits outweigh<br>concentration risks in credit portfolios<br>of German banks?|Rolf Böve<br>Klaus Düllmann<br>Andreas Pfingsten|
|---|---|---|---|
|11|2010|Are there disadvantaged clienteles<br>in mutual funds?|Stephan Jank|
|12|2010|Interbank tiering and money center banks|Ben Craig, Goetz von Peter|
|13|2010|Are banks using hidden reserves<br>to beat earnings benchmarks?|Sven Bornemann, Thomas Kick<br>Christoph Memmel|
|||Evidence from Germany|Andreas Pfingsten|
|14|2010|How correlated are changes in banks’ net<br>interest income and in their present value?|Christoph Memmel|
|01|2011|Contingent capital to strengthen the private<br>safety net for financial institutions:||
|||Cocos to the rescue?|George M. von Furstenberg|
|02|2011|Gauging the impact of a low-interest rate<br>environment on German life insurers|Anke Kablau<br>Michael Wedow|
|03|2011|Do capital buffers mitigate volatility<br>of bank lending? A simulation study|Frank Heid<br>Ulrich Krüger|
|04|2011|The price impact of lending relationships|Ingrid Stein|



54 

## **Visiting researcher at the Deutsche Bundesbank** 

The Deutsche Bundesbank in Frankfurt is looking for a visiting researcher. Among others under certain conditions visiting researchers have access to a wide range of data in the Bundesbank. They include micro data on firms and banks not available in the public. Visitors should prepare a research project during their stay at the Bundesbank. Candidates must hold a PhD and be engaged in the field of either macroeconomics and monetary economics, financial markets or international economics. Proposed research projects should be from these fields. The visiting term will be from 3 to 6 months. Salary is commensurate with experience. 

Applicants are requested to send a CV, copies of recent papers, letters of reference and a proposal for a research project to: 

Deutsche Bundesbank Personalabteilung Wilhelm-Epstein-Str. 14 

60431 Frankfurt GERMANY 

55 

