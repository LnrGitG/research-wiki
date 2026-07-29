## MNB Working Papers 2026/3

**Sentiment-based Financial Stress Index for Hungary**  
*Sentiment alapú pénzügyi stressz index magyar híradatokon*

---

### Abstract

This paper proposes a sentiment-based financial stress indicator for Hungary based on occurrence of financial crisis related terms and explores its relationship with macrofinancial variables related to financial uncertainty. Sentiment analysis was conducted on textual data from two major Hungarian news portals covering the period from 2005 to 2020. The terms used in the analysis carry negative connotations, making them suitable for capturing financial instability and stress. The index successfully identifies stress periods that are not adequately reflected by other available sentiment indices related to Hungary. Overall, we propose a novel type of index that enables timely, even real-time monitoring of financial stress situation in Hungary across different time frequencies.

**JEL Classification:** C32, E44, G01  
**Keywords:** sentiment, financial stress, text analysis

---

### Összefoglaló (Magyar)

Jelen tanulmány egy szövegelemzésen alapuló szentiment pénzügyi stressz indikátor előállítását, és annak pénzügyi aktivitással való összefüggéseit vizsgálja. A szentiment elemzést két meghatározó magyar hírportál adatain végeztük 2005 és 2020 között. Az elemzésben használt kifejezések negatív jelentéssel bírnak, így alkalmasak a pénzügyi instabilitás és stressz mérésére. Az index-szel azokat az időszakokat is jól megfogtuk, amikre egyéb Magyarországra vonatkozó vagy regionálisan elérhető szentiment indexek nem alkalmasak. Összességében egy olyan új típusú index előállítására teszünk javaslatot, amivel időszerűen, akár valós időben, különböző frekvenciákon követhetjük nyomon a pénzügyi stressz helyzetét Magyarországon.

---

### 1 Introduction

Monitoring and quantifying systematic risks in the financial system is crucial for supporting sound policy decisions. Financial stress can be conceived as the amount of risk that has materialized. In this sense, financial stress can be represented by an interval (continuous) variable where extremely high values can be considered as crisis periods. In addition, such indices are suitable for assessing potential negative impact of stress periods on real economic activity. (Szendrei & Varga, 2017)

The main methodology typically involves the aggregation of numerous financial variables into a single composite indicator, using dimensionality reduction techniques such as principal component analysis or factor analysis. In addition to several country- or regional-level studies (e.g Illing & Liu, 2006, Hakkio & Keeton, 2009, Cevik et al., 2013), supranational bodies such as the ECB (Hollo et al., 2012), the EIB (Dim et al., 2022), or the IMF (Ahir, 2023) have recently developed indices related to financial stress covering relatively long periods of time based on uniform methodologies to ensure comparability between countries, which are continuously updated to monitor financial stability.

As vast amounts of unstructured, primarily textual data have become more accessible and more convenient to acquire, update, and process, a new strand of empirical research has emerged, focusing on measuring financial stress through the extraction of sentiments from various textual sources. These sentiment-based proxies can capture increased uncertainty or growing informational asymmetries (changing risk preferences) in financial markets that can also be driven by irrational behavior and market anomalies, which often contribute to rapidly developing financial instability. In line with these theoretical considerations, some researches highlighted the role of sentiment influencing stock market performance (see, e.g., M. Baker & Wurgler, 2007; García, 2013) providing a foundational overview on how investors' sentiments drive market fluctuations and bubbles. Furthermore, news-based sentiments proved to have predictive power for potential financial instability and asset price bubbles (see Krishnamurthy & Li, 2025; Maghyereh & Abdoh, 2022). Empirical research showed that article titles in leading newspapers can more accurately signal upcoming financial crises than conventional confidence indicators (Ristolainen et al., 2024) or the newspaper-based daily sentiment indicator can be used to monitor economic activity in real time (see, e.g., Aguilar et al., 2021).

Early empirical researches that relied on extracting and incorporating news- or social media activity based sentiments when constructing financial stress indices started in the late 2010s thus it is a relatively new field of scientific investigation. Püttmann, 2018 constructed a stress index for the US extracting sentiments from the news title, Stolbov & Shchepeleva, 2025 for Russia using volumes of Internet searches, and Fernandez et al., 2021 for Mexico using tweets. Others focused on tracking global financial instability (see, e.g., Borovkova et al., 2017; Correa et al., 2020; Stolbov et al., 2022).

Sentiment-based stress indices for Central and Eastern European countries are still relatively scarce, despite the substantial increase in the number of financial stress indices constructed (Stolbov & Shchepeleva, 2025), especially for Central and Eastern Europe. To address the lack of research in this area for post-socialist economies in Central and Eastern Europe, we propose a local sentiment-based financial index for Hungary. Our index is based on vast amount of textual data from two major Hungarian news portals that sufficiently represent domestic online news media. The analysis covered news articles published between January 2005 and December 2020, a period marked by several turbulent phases — Global Financial Crisis (GFC), events of sovereign debt crisis in Hungary and Europe, COVID-19 pandemic — in the financial market, making it particularly suitable for testing and validating our sentiment-based financial stress indicator. As a result, the index successfully captures the event-related spikes in financial instability observed in the Hungarian economy during this period.

Our sentiment-based financial stress index (SFSI) is constructed using a keyword-driven, Boolean rule-based algorithmic approach. This idea is adapted from S. R. Baker et al., 2016. We examined two sets of expressions: one consists of lexical items related to financial crisis, the other with different areas of the financial system. The scoring at the article level is based on the occurrence of any combination of expressions from the two sets. This procedure rather reflects the extent to which the topic stress/uncertainty in the financial system dominates the text itself. To obtain the composite index time series, a simple arithmetic mean is calculated on all scores of articles deemed relevant and normalized by the number of articles for each period.

It should be emphasized that the filtering of articles for economic content is of great importance. We used the Latent Dirichlet Allocation (LDA, Blei et al., 2001) algorithm for this purpose which is in line with the empirical literature. This procedure ensures the removal of noise from the news corpus that is irrelevant to the analysis, thereby ensuring that the index is constructed on a solid and relevant dataset.

We also examine both the predictive relationships and dynamic interactions of the SFSI among key financial and uncertainty-related variables using classical econometrics methods. The variables used in the analysis include the 5-year sovereign CDS spread for Hungary (CDS), the Factor Based Index of Systematic Stress (FISS), the Economic Policy Uncertainty (EPU) index for the EU, and the geopolitical risk index (GPRI) for Hungary. While Granger causality tests indicate that our sentiment-based financial stress index (SFSI) contains statistically significant information about future CDS spread values, also, VAR analysis shows that the SFSI tends to precede CDS spread variable and has lasting, significant effect on the CDS spread — outperforming all other indicators included in the VAR analysis where all variables are included. The forecast error variance decomposition (FEVD) reveals that a substantial proportion of the variance in the CDS spread is explained by our index.

The Diebold–Yilmaz spillover analysis applies the connectedness framework to examine how financial stress affects CDS across different forecast horizons. It captures both the magnitude and direction of interconnectedness and shock transmission among the VAR variables and highlights the increasing systemic importance of the SFSI over time. According to the directional spillover results, the SFSI exhibits strong explanatory power for the CDS spread over both short- and long-term horizons.

In summary, our study may contribute to the existing literature in many ways. We demonstrated that the feasibility of incorporating sentiment into financial stress index from limited number of online sources for Hungary. The results confirm that news-based sentiment tools can effectively capture turbulent periods in the Hungarian financial and economic system just as an earlier country-specific stress index did (FISS, see Szendrei & Varga, 2017), but other sentiment indicators for Hungary (EPU, GRPI) had not. Our index has a relatively strong performance in tracking financial stress compared to other contender indices using standard macroeconomic evaluation methods. Thus, considering a sentiment-based stress index not as substitutes, but rather as complementary tools in understanding the multifaceted nature of financial stress alongside indicators based on numerous high frequency financial variables. Based on these findings, we consider the SFSI a valuable indicator to monitor financial stability in Hungary.

The paper is organized as follows. Section 2 gives a brief overview of the empirical literature measuring financial stress based on sentiments extracted from non-conventional, unstructured data sources. Section 3 describes the data source, provides a picture of the data filtering approach, and gives a detailed view of the index construction methodology. Section 4 outlines the methods used to assess the performance of the index before concluding the paper in the last section.

---

### 2 Literature Review

#### 2.1 From Hard to Soft Data

Since the Global Financial Crisis, the issue of systemic risk has captured the attention of academics, regulators, and private agents in the financial system. Financial stress and risk indices have been derived by machine learning and text mining techniques, allowing the process and handling of increasing volumes of unstructured (text) data. Besides the arm of literature relying on "hard data" (Hollo et al., 2012) which mostly consists of various high-frequency financial market indicators, an increasing amount of research analyzes 'soft information' to capture financial risk, systemic financial risk, or uncertainty related to economic policy, geopolitics (Caldara & Iacoviello, 2022) and volatility (Engle & Campos-Martins, 2023).

#### 2.2 From Global to Local Perspectives

Borovkova et al., 2017 developed a sentiment-based risk indicator for the global financial system that is constructed by aggregating news sentiment about systemically important financial institutions. Their index, SenSR consistently leads traditional risk indicators and macroeconomic signals by up to 12 weeks. One of the first studies aimed to construct a historical stress index focusing on global level and US stress, Püttmann, 2018 compiled a high-frequency Financial Panic Index spanning 1889–2016 by analyzing more than 35 million U.S. newspaper titles in five major newspapers. He concludes that changes in the use of crisis-related language in terms of sentiment in the print media offer a robust, historically informed early warning signal of financial instability. Correa et al., 2020 developed a Financial Stability Sentiment (FSS) index using textual analysis of central banks' Financial Stability Reports (FSRs) in 30 countries from 2005 to 2017, to investigate how central bank messaging reflects and predicts the financial cycle. A custom dictionary was compiled where words were classified as positive or negative, and these were aggregated to generate time series of FSS for each country. As a result, indices move in sync with financial cycle indicators, that is, central bank sentiment in official communication can be an early warning indicator of financial fragility. Stolbov et al., 2022 introduces a novel sentiment-based index of global financial stress by combining central bank research outputs with Google search data. The study employs text mining and machine learning techniques to quantify the intensity of negative sentiment related to financial instability as reflected in both expert and public attention. The resulting index demonstrates strong correlations with traditional financial stress indicators and offers a timely, high-frequency measure to monitor global financial conditions. Dim et al., 2022 introduce the News-Implied Sovereign Risk Index (NSRI), constructed through natural language processing of approximately 10 million news articles across more than 100 countries, offering a high-frequency proxy for sovereign default risk. The NSRI exhibits strong contemporaneous and predictive correlations with sovereign CDS spreads, serves as an early warning indicator for sovereign credit rating downgrades, and captures aspects of risk not fully reflected in CDS spreads data.

A country-level study (Fernandez et al., 2021) proposed a sentiment-based risk indicator (SRI) for the Mexican financial sector by systematically analyzing the tone of tweets regarding financial institutions. Using natural language processing and machine learning techniques, they extract sentiment from domestic media sources to construct an index that measures the prevalence of negative sentiment over time. The results demonstrate that the SRI effectively identifies periods of financial distress and serves as a valuable complement to traditional market-based indicators. Stolbov & Shchepeleva, 2025 presents a sentiment-based financial stress index for Russia derived from the volumes of internet searches in financial terms with a negative connotation about financial stability. The constructed index quantifies negative market sentiment and is systematically validated against conventional stress indicators — including exchange rate volatility, interest rate spreads, and equity market fluctuations — to demonstrate its responsiveness to worsening financial conditions. Their index provides a supplementary tool for macroprudential monitoring within the Russian financial environment. Bernal & Pedraz, 2020 conduct a sentiment analysis of the Bank of Spain's FSRs to assess the relationship between institutional tone and financial market developments. Their findings indicate that changes in the sentiment of the report are significantly correlated with financial stress indicators, highlighting the potential of central bank communication as a forward-looking tool to monitor systemic risk. In addition, their index has a strong negative correlation with the Spanish GDP and a strong positive correlation with stock market volatility and CDS spreads.

The evidence in the empirical and theoretical literature suggests that social media activity or news content may influence agents in the financial market, thus underlying the role of sentiment in financial crises. The use of news-based textual data to quantify financial risk/stress is based on the assumption that news media are observed at a high frequency and contain timely information about developments in domestic and international financial markets which is likely to influence the perceptions and expectations of economic agents. In short, general sentiment distilled from relevant news can depict the dynamics of popular narrative about financial system.

---

### 3 Data and Index Construction

#### 3.1 Data Source

Our study focuses on textual data acquired from two major Hungarian news portals, which were selected due to their ability to adequately represent domestic online media. The data acquisition process, including the extraction, processing and storage of the information, was carried out in full compliance with current legal regulations and in consent with the respective media organizations.

The analysis covered news articles published between January 2005 and December 2020, with a daily average of 95 articles, all published in Hungarian. The average length of the articles per year is shown in Figure A in Appendix A. This period included several financially turbulent phases and major global and domestic economic events, such as the global financial crisis of 2008–2009, the Greek sovereign debt crisis of the 2010s, the mandatory settlement and conversion of foreign currency-denominated household loans into forints in Hungary, and the onset of the COVID-19 pandemic. As all of these events are associated with financial and economic instability and stress, this period is well-suited for testing and validating our sentiment-based financial stress indicator.

**Figure 1:** Number of filtered articles from two major Hungarian news portals between 2005 and 2020

#### 3.2 Data Filtering

In preparing the dataset for modeling, several preprocessing steps were implemented to ensure data quality and consistency. Duplicate articles were identified and eliminated from the corpus to prevent redundancy that could skew our results and introduce unexplainable variance into our processes. The articles underwent comprehensive cleaning through the removal of non-linguistic elements including extra hyphens, line breaks and email addresses to standardize the dataset and eliminate unnecessary noise that could interfere with further elements of the computational pipeline. As a next step, the whole dataset went through lemmatization. This step consolidates words and phrases into their root representations, standardizing the contents for downstream tasks and reducing the dimensionality of the feature space while preserving semantic meaning.

After the data preprocessing, we conducted a preliminary exploratory analysis to better understand the information content of the articles. To be able to create a metric to model financial stress in the economy, it is essential that the news articles we analyze are relevant to this matter. The news corpus was varied in terms of topics, ranging from tabloid journalism to meteorological reports, which resulted in a low signal-to-noise ratio in SFSI index. To combat this, a topic modeling approach was employed to filter out and retain economically relevant articles. We experimented with multiple different unsupervised machine learning algorithms, namely LDA, HDBSCAN and K-Means over BERT embeddings, out of which LDA gave the best results in terms of topic cohesion. The LDA algorithm, applied to the preprocessed dataset, treats individual articles as discrete documents within a probabilistic framework. The model estimation creates a probability distribution for each article over a number of latent "topics", fixed at the start of the training, while also creating a distribution for each topic over all the available words in the dataset, based on word counts and co-occurrences. The model's hyperparameters (the number of topics, the parameters of the initial distributions and the batch size) were optimized through grid search. We evaluated the goodness-of-fit of each model by measuring the perplexity, which measures how well the model generalizes to new data.

To assess which category to keep, we examined the top 20 words of each category to find relevant keywords. The final model contained 16 topics, 13 of which were found relevant to our analysis having a predominantly economic and/or financial focus.

**Figure 2:** The constructed index from the unfiltered and filtered data at weekly and monthly frequency

The effect of the data filtering can be seen in Figure 2. The plots show the indices resulting from the boolean method, aggregated to weekly and monthly frequency. Clearly, the index constructed from unfiltered set of articles is extremely volatile with a low signal-to-noise ratio. However, after LDA filtering, the resulting index resembles the CDS spread times series much better.

> We also filtered out any word which was not a noun, adjective, verb, adverb or a proper noun. The data cleaning was carried out using regular expressions, while the lemmatization was done using the Spacy software library (Ver. 3.5.4) (Honnibal et al., 2020), using the hu_core_news_lg model (Ver. 3.5.2) (Orosz et al., 2023)

> HDBSCAN: Hierarchical Density-Based Spatial Clustering of Applications with Noise

> BERT: Bidirectional Encoders Representations from Transformers

#### 3.3 Construction of a Sentiment Index

The construction of a sentiment indicators may be categorized into four main methodological approaches: survey-based methods, keyword-based algorithmic techniques, Boolean rule-based algorithms, and machine learning models.

Survey-based methods rely on direct collection of data from individuals or businesses, typically through questionnaires or structured interviews, to gain insight into subjective opinions and expectations. One of the best-known examples is the Economic Sentiment Indicator (ESI), compiled by European Commission, 2025.

Keyword-based algorithmic techniques use predefined dictionaries of positive and negative words to quantify sentiment by counting the frequency of these terms in textual data. (see, e.g., Kalamara et al., 2022)

Boolean rule-based algorithms apply logical operators such as AND, OR, and NOT to detect the presence or co-occurrence of specific terms, phrases, or structural patterns within a text. These systems are manually constructed using expert knowledge or domain-specific heuristics. (see, e.g., S. R. Baker et al., 2016)

Deep learning methods, as state-of-the-art approaches within machine learning, leverage labeled datasets to train models that classify sentiment (positive, neutral, negative) based on patterns learned from the data. These models can capture contextual nuances and achieve higher predictive accuracy. (see, e.g., Kanelis & Siklos, 2025)

Each of these methodologies presents unique strengths and limitations. Survey-based methods benefit from direct human input but can be costly and time consuming. Algorithm-based methods, such as keyword- or rule-based approaches, are interpretable and easier to implement but may lack contextual understanding. Deep learning models, while powerful, require substantial amount of labeled data and computational resources. The choice of the appropriate methodology may depend on the specific research context, the availability and nature of the data, and the trade-off between interpretability and predictive performance.

##### BOOLEAN ALGORITHM

In our research, we sought a method that is easy to interpret, explain, and implement. Based on these considerations, we selected a Boolean rule-based approach from the algorithmic methods.

With the involvement of subject-matter experts, we compiled a set of expressions related to financial instability and stress. Based on this, we created two sets: one consisting of terms referring to the financial system, such as *finance, economy* and another comprising negative sentiment expressions associated with stress and instability, such as *risk, uncertainty*.

##### CONSTRUCTING THE INDEX

The SFSI index used in our analysis is based on articles filtered using the LDA algorithm; see Section 3.2. For each article A, we define indicator variables to represent the presence of unique keywords from the two predefined sets: financial system keywords: F = {f1, f2, ..., fF} and stress-related keywords: S = {s1, s2, ..., sS}.

For each f ∈ F let I_f^A be the indicator variable defined as 1 if f appears in article A, 0 otherwise.

Similarly, for each s ∈ S.

Based on these indicators, we compute for each article A:
- the number of unique financial system keywords: N_F^A = Σ_f I_f^A
- and the number of unique stress-related keywords: N_S^A = Σ_s I_s^A

The composite index is then defined as the average, over a collection of K articles {A1, A2, ..., AK}, of the co-occurrence measured by the product of the previously calculated counts.

SFSI_t = (1/K_t) Σ_{A∈articles_t} (N_F^A × N_S^A)

The index can be computed for any chosen temporal frequency (e.g., daily, weekly, or monthly). This formulation ensures that each article contributes proportionally to the index value based on the keywords it contains. It is important to note that each keyword is counted only once per article, regardless of how many times it appears. Thus, the SFSI index does not reflect mere frequency of occurrence, but rather the extent to which concepts related to the financial system and stress are jointly present in the text corpus.

**Table 1:** Examples for calculation of the index

| News originally in Hungarian | News translated into English | source | Keywords for financial system | Keywords for stress | Score |
|---|---|---|---|---|---|
| "... Bank fokozot óvatosságra int a felhasználókat ... Ezek a hamisított internetes tartalmak mellett, hogy egy pénzügyi csalás részét is képezhetk, informatikai-biztonsági kockázatokat is jelenthetnek..." | "... Bank urges users to exercise increased caution... These fake online contents may not only be part of a financial fraud scheme, but also pose cybersecurity risks. ..." | mt.hu, 2020 | bank, finance | risk | 2 |
| "... Az új vámintézkedések miatt világszerte megnövekedett a gazdasági és pénzpiaci bizonytalanság ... a vámháború miatt az alacsonyabb növekedési és a magasabb inflációs kockázatok Magyarországra is hatással lehetnek..." | "... Due to the new customs measures, economic and financial market uncertainty has increased worldwide. As a result of the trade war, the risks of lower growth and higher inflation may also affect Hungary. ..." | Facebook, 2025 | economy, financial market | uncertain, risk | 4 |

By construction, the index is bounded due to the finite number of keywords and articles. Consequently, a long-term trend is not expected to materialize, the index is assumed to exhibit mean-reverting dynamics, returning to its baseline level once extraordinary events fade out. Nevertheless, some short-term persistence may occur, reflecting the attitude of journalists to focus on certain news topics for a while.

##### KEYWORD SENSITIVITY ANALYSIS - FINAL SET OF KEYWORDS

The objective was to identify and remove redundant terms in order to derive a transparent and interpretable model that accurately preserves the dynamic properties of the original full system. To evaluate the sensitivity of the keyword-based method, we applied a two-stage analysis based on Autoregressive Moving Average (ARMA) modeling.

The ARMA model specification was determined using an automatic selection procedure, where the maximum orders were restricted to ARMA(4,4). The procedure also incorporated automated testing for differencing and log transformation. The final specification was selected based on the Akaike information criterion (AIC) in all cases. This approach ensures that model selection is comparable across all examined time series.

For the baseline model, which includes all keywords, an ARMA(2,3) specification was identified. Although stationarity was borderline (see 4.3 and A.1 in Appendix B), diagnostic tests indicated that neither differencing nor transformation was required in this field of analysis. This is supported also by the Durbin-Watson statistic and the fact that the inverted AR and MA roots lie within the unit circle, confirming the stability of the estimated model.

In the first stage, each keyword was removed individually from the original full keyword set. For each removal the corresponding output time series was generated and an ARMA model was fitted. The order of the resulting ARMA model and its estimated coefficients were then compared to those of the baseline model obtained using the full keyword set. Differences in model order were interpreted as indications of changes in the underlying dynamics, while coefficient stability was evaluated relative to the 95% confidence intervals of the baseline estimates. If the removal of a keyword resulted in a different model order or in parameter estimates falling outside these confidence intervals, the keyword was classified as influential and retained; otherwise, it was provisionally classified as non-influential and added to a candidate pool for further analysis.

The second stage assessed whether combinations of the provisionally non-influential keywords from the candidate pool could jointly influence the model's behavior. The procedure began by identifying a pair of keywords whose simultaneous removal did not cause differences in the ARMA order or the estimated coefficients to fall outside the baseline confidence intervals. Starting from this pair, additional keywords from the candidate pool were added to the removal set, one at a time. After each addition, the corresponding time series was generated, and the ARMA model was re-estimated to verify that the model order and coefficient stability was preserved. This iteration continued until joint removals produced statistically significant deviations from the baseline model.

The two-stage analysis resulted in a reduced yet sufficient set of keywords, containing only those that non-negligibly influence the temporal behavior of the original system. The final set offers a clearer and more interpretable representation, while still preserving the essential characteristics of the full original, expert-defined model.

---

### 4 Performance of the SFSI Index

#### 4.1 Validation Results - Comparison of the Index with Existing Chronologies

Evaluation of SFSI performance is not straightforward. One of the most commonly used methods to assess the performance of an index is whether its peak values coincide with the timing of certain 'well-defined' crisis events. Since the time interval of evaluation is fairly long and there were several turbulent periods between 2005 and 2021, we have divided the SFSI chart into two for better presentation. Figure 3 shows the period between 2005 and 2012, while Figure 4 presents the period between 2013 and 2020. It covers pre-GFC events with the building up of subprime mortgage crisis followed by the period of GFC and European sovereign bond crisis. After 2013 there is a long period of post crisis where several notable events occurred that induced mostly minor turbulences in the financial market. We closely follow the selection of events involving turbulence in the Hungarian financial market (Szendrei & Varga, 2020), who benchmark their FISS using in a similar manner when evaluating the FISS as is customary in the literature (e.g. Hollo et al., 2012).

**Figure 3:** Timeline of events between 2005 and 2012

**Figure 4:** Timeline of events from 2013 to 2021

Key events captured by SFSI:

- **July 2007:** Bear Stearns hedge fund collapse → evaporation → SFSI spike parallel with FX/capital market reaction
- **Nov 2007:** S&P downgrades investment bank → SFSI rises significantly
- **March 2008:** Subprime crisis turbulence on Hungarian gov bond market → SFSI new high, persistent
- **Sep 2008:** Lehman Brothers bankruptcy → Sudden SFSI spike during GFC deepening
- **Jan-Mar 2009:** HUF/EUR FX turbulence (high FX exposure of households) → SFSI spike
- **Apr 2010:** Greece downgraded to junk → SFSI elevated; Hungarian FX/bond volatility + political statements
- **May-Aug 2011:** Euro sovereign debt concerns escalate → CHF/HUF all-time high (CHF mortgages) → SFSI continuous increase
- **Sep 2011:** Early FX loan repayment announcement (banks bear losses) → SFSI peaks end-2011/early-2012
- **2012:** Greek election uncertainty → small SFSI peak
- **2013-2014:** Gradual SFSI decline as Euro sovereign debt problems alleviate
- **Dec 2014-Jan 2015:** Mandatory conversion of remaining FX household loans to HUF → minor SFSI bump
- **June 2015:** Greek debt renegotiation → euro volatility
- **June 2016:** Brexit referendum
- **Nov 2016:** US election
- **March 2020:** COVID-19 outbreak → SFSI high until early 2021

#### 4.2 Robustness Analysis

Next, we assess the robustness of the SFSI index. In particular, we want to evaluate the sensitivity with respect to the number of articles used to produce it. To achieve this, we conducted a simulation to create an alternative index by randomly removing a percentage of the original database of articles on two levels: 10 and 40 percent, the latter corresponding to the event of losing one medium. Then, we calculated the sentiment financial stress index from the remaining articles in the way described in Section 3.3.2. We ran this simulation a thousand times and in the end we averaged out all the indices to arrive at the final alternative index.

**Figure 5:** Difference of the original index to the robust indices

Figure 5 shows the differences of the values of the original index compared to the robustness index for both percentages. The plot shows how the maximum average difference does not exceed the thousandths for the index constructed with 60 percent of the data, with the 90 percent "index" differing by one order of magnitude smaller, indicating extreme robustness to the construction of the index.

#### 4.3 Empirical Analysis

To evaluate the economic relevance and informational content of the newly constructed sentiment-based Financial Stress Index (FSI), we apply a set of multivariate time series techniques designed to capture both predictive relationships and dynamic interactions among key financial and uncertainty-related variables. Specifically, empirical analysis includes Granger causality tests, Impulse Response Functions (IRF), Forecast Error Variance Decomposition (FEVD), and the Diebold–Yilmaz (DY) spillover index. These methods are complementary: Granger tests assess whether the sentiment index contains leading information about other financial risk indicators, while IRFs allow us to trace the transmission mechanism of shocks over time. FEVD is used to quantify how much variation in a given variable—such as the sovereign CDS spread — can be attributed to shocks in our index. Finally, the DY spillover framework enables us to evaluate the system-wide connectedness of the index and whether it acts as a net transmitter or receiver of financial stress. Together, this methodological framework allows us to assess whether sentiment-based FSI provides additional information about the dynamics of financial risk — complementing what is already captured by standard stress, policy, and geopolitical uncertainty indicators.

##### Variables Used

- **5-year Sovereign CDS spread (Hungary):** Market assessment of Hungary's sovereign credit risk. Increase = higher perceived default risk. (datasource: Datastream/LSGE)
- **Factor based Index of Systematic Stress (FISS):** Comprehensive measure of financial stress in Hungarian financial system (Szendrei & Varga, 2020). Dynamic factor model based on 19 variables covering all core segments. (datasource: MNB)
- **Economic Policy Uncertainty (EPU) Index – EU:** Quantifies uncertainty related to economic policy via newspaper frequency analysis (S. R. Baker et al., 2016). EU-wide index used (no Hungary-specific EPU). (datasource: policyuncertainty.com)
- **Geopolitical Risk (GPR) Index – Hungary:** Dictionary-based approach (Caldara & Iacoviello, 2022). Hungary-specific GPR from 1905. (datasource: matteoiacoviello.com/gpr.htm)

##### GRANGER CAUSALITY

Since Granger causality tests require stationary time series for valid inference, we began our analysis by testing the stationarity of the variables. To address this, we apply Augmented Dickey-Fuller (ADF), Phillips-Perron (PP) and Kwiatkowski–Phillips–Schmidt–Shin (KPSS) tests. The former two tests check for unit root (null = non-stationarity); KPSS assumes stationarity under null — useful complement.

In case of our variables the ADF and PP tests suggest the presence of unit roots, while the KPSS test shows in most cases borderline evidence in favour of stationarity (see Table A.1 in Appendix B). Therefore, we follow the lag-augmented approach proposed by Toda & Yamamoto, 1995, which allows us to test the Granger causality in levels, even when the underlying variables may be integrated or non-stationary.

To determine the optimal lag length, we examined both the Schwarz and Hannan-Quinn (HQ) information criteria. As shown in Table A.2 in Appendix B, instead of the more parsimonious Schwarz criterion, which returned a value of 1 in all cases, we used the HQ results for the Granger causality tests.

**Table 2:** Results of Toda-Yamamoto Granger causality tests

| Null hypothesis | χ² | Prob |
|---|---|---|
| CDS spread ← SFSI index | 19.014 | 0.000 |
| SFSI index ← CDS spread | 0.092 | 0.761 |
| CDS spread ← FISS | 16.199 | 0.001 |
| FISS ← CDS spread | 7.665 | 0.0535 |
| CDS spread ← EPU EU | 8.628 | 0.125 |
| EPU EU ← CDS spread | 9.179 | 0.1021 |
| CDS spread ← GPRI HU | 1.534 | 0.6743 |
| GPRI HU ← CDS spread | 1.334 | 0.7209 |

The Toda-Yamamoto Granger causality tests indicate a **unidirectional relationship from SFSI to CDS spread** (χ²=19.014, p<0.001), suggesting that SFSI contains predictive information for CDS spread. FISS exhibits a **bidirectional relationship** with CDS spread, while the remaining indicators (EPU EU, GPRI HU) do not show significant causal links.

In summary, the results suggest that our index contains relevant information one month in advance, allowing a more accurate explanation and prediction of the CDS spread.

##### GENERALISED IMPULSE RESPONSE FUNCTION

Impulse response functions trace the time path of the effect of a one-time shock to one variable on the current and future values of the other variables in the system. The Generalized Impulse Response Function (GIRF), introduced by Pesaran & Shin, 1998, offers a robust extension to the traditional impulse response analysis in a VAR framework. Unlike the standard IRF, which requires orthogonalised shocks often obtained through a recursive Cholesky decomposition, the GIRF approach does not depend on the ordering of variables. This characteristic makes GIRF particularly valuable when the theoretical justification for variable ordering is ambiguous.

Before performing GIRF analysis, it is necessary to ensure that the underlying VAR model is appropriately specified and satisfies standard assumptions regarding stationarity, lag length, stability, and the absence of substantial autocorrelation.

Although formal stationarity tests (see Table A.1 in the Appendix) yield borderline results, the time series is retained in levels without transformation in the VAR specification. This choice is supported by the construction of the index: as discussed earlier, the index is bounded, precluding the emergence of a deterministic long-term trend, and it is assumed to exhibit mean-reverting dynamics, returning to its baseline level once extraordinary events fade out.

The optimal lag length for the VAR model is determined based on the Schwarz (BIC) and Hannan-Quinn (HQ) information criteria, indicating a VAR(1) specification (see Table A.3 in the Appendix).

The coefficients of the estimated VAR(1) model are presented in Table A.4 in the Appendix. The VAR(1) model is stable, as all inverse roots lie within the unit circle (see Figure A.2 in the Appendix). Residual diagnostics, based on Durbin-Watson statistics (see table A.4 in Appendix), indicate no substantial autocorrelation, supporting the validity of the estimated VAR(1) model for further analysis.

**Figure 7:** Response to Generalized One S.D. Innovations

**GIRF Results:**

- **SFSI shock → CDS spread:** Immediate increase ~12-13 bps, intensifies over subsequent months, **peaks around month 5 at ~30 bps**, then gradually diminishes over ~24-month horizon. Persistent and steadily increasing response → structural information with lasting influence.
- **FISS shock → CDS spread:** Slightly stronger initial impact; peaks earlier (~month 2); fades by month 10.
- **EPU EU shock → CDS spread:** Similar early-peak pattern to FISS; max ~9.8 bps; statistically insignificant by month 5.
- **GPRI HU shock → CDS spread:** Statistically insignificant effect (confidence interval includes zero).

SFSI provides **prolonged effects beyond short-term fluctuations** — valuable for early forecasting and medium-term risk assessments.

##### FORECAST ERROR VARIANCE DECOMPOSITION

FEVD decomposes the forecast error variance of each variable in a VAR system into proportions attributable to shocks from each variable. This allows us to quantify the relative importance of each variable in explaining the forecast uncertainty of others, over short and long time horizons.

**Figure 8:** The dynamics of the sentiment-based financial stress index (SFSI) and the variables included in the VAR system

**FEVD Results for CDS spread:**

| Horizon | CDS own | SFSI | FISS | EPU EU | GPRI HU |
|---|---|---|---|---|---|
| Short | ~100% | 12% | ... | ... | ... |
| Medium (month 5) | ... | **40%** | ... | ... | ... |
| Long | **30%** | **60%** | ... | ... | ... |

- CDS own explanatory power decreases from ~100% to **30%** long-term
- **SFSI contribution grows from 12% to 60%** (steady increase)
- SFSI becomes the **dominant driver** of CDS spread forecast error variance

##### SPILLOVER INDEX

The Diebold–Yilmaz spillover index (Diebold & Yilmaz, 2012) provides a comprehensive measure of how shocks propagate across variables based on FEVD from VAR models. The total spillover index captures the overall extent of interconnectedness and the transmission of shocks across all variables simultaneously. The directional spillover identifies how variance spillovers affect individual variables.

**Table 3:** Direct connectedness to CDS spread across different variables and forecast horizons

| Variables | h=1 | h=2 | h=3 | h=6 | h=12 |
|---|---|---|---|---|---|
| FISS | 19.95 | 22.33 | 24.56 | 30.36 | 38.35 |
| **SFSI** | 13.00 | 22.70 | **31.32** | **48.54** | **61.96** |
| EPU EU | 2.59 | 3.12 | 3.63 | 4.90 | 6.49 |
| GPRI HU | 0.25 | 0.75 | 1.02 | 1.33 | 1.49 |
| SFSI+EPU+GPRI | 15.90 | 26.79 | 35.57 | 51.28 | 62.56 |
| FISS+EPU+GPRI | 23.57 | 28.54 | 32.46 | 40.05 | 46.83 |
| SFSI+FISS | 24.45 | 33.99 | 41.91 | 56.67 | 67.21 |
| SFSI+FISS+EPU+GPRI | 27.31 | 37.32 | 44.91 | 57.72 | 66.13 |

**Key Findings:**

1. **Short-term (h=1):** FISS transmits slightly stronger spillovers (19.95 vs 13.00) → more responsive to immediate market conditions
2. **Medium-term (h≥3):** **SFSI becomes dominant spillover source** (31.32 at h=3 → 61.96 at h=12)
3. EPU and GPRI effects remain consistently weak across all horizons
4. **SFSI + FISS combined** provides most robust representation (capturing distinct stress dimensions across horizons)

**Figure 9:** Spillover to CDS spread at different forecast horizons

**Dynamic (Rolling Window) Spillover Analysis:**

Applied 60-month (5-year) rolling window, re-estimating VAR(1) and GFEVD at each step.

- Short-term (h=1): FISS and SFSI contribute similarly; EPU/GPR negligible
- **h=6: SFSI emerges as main transmitter** of shocks to both FISS and CDS spreads
- COVID-19 period: sharp increases in directional spillovers across all models
- SFSI effect persists due to prolonged media attention and delayed policy responses

**Figure 10:** Total spillover effects at short and medium term horizons (h=1, h=6)

At h=6, SFSI becomes the **dominant source of risk transmission** in the system, exerting sustained significant influence on both FISS and sovereign credit risk.

---

### 5 Conclusion

This paper introduces a sentiment-based financial stress index for Hungary from January 2005 to December 2020. The index builds on optimized keyword searches from two Hungarian online news portals combining two different sets of pre-defined terms, one capturing terms related to elements of financial system and the other to those of crisis or uncertainty. Instead of relying on raw term counts, each article previously identified as relevant is assigned a score reflecting the richness of term co-occurrences, through which the dominance of a crisis- or uncertainty-related narrative within the text is intended to be captured.

The SFSI successfully gauges the episodes of financial turbulence in the Hungarian economy during the fairly long period of observation. These distinguished periods are associated with financial turmoils before September 2008 (beginning of the sub-prime crisis coupled with bankruptcies in the US) peak stress periods during GFC (2009-2010) and the emerging sovereign debt crisis in Europe (2011-2014). As a consequence of enduring financial vulnerabilities, Hungary was particularly hit hard by the GFC compared to other Central and Eastern European EU countries, causing recurring episodes of financial distress. Events after 2014 like the Brexit voting, or the outbreak of Covid-19 pandemic also produced local peaks in the index.

More importantly, the overall dynamics of SFSI closely mimics that of the FISS which latter is considered to be one of the most sophisticated financial stress index for Hungary complied so far. The FISS has the advantage of being able to capture the complex interconnectedness of financial markets. It aims to quantify the individual importance of a large number of indicators by a weighting procedure linked to their historical importance measured by the explained variance in the financial system.

We show that our index is useful for financial stability analysis. In evaluating the performance of our news-based stress indices, **Granger causality tests showed that SFSI tends to lead the CDS spreads time series**. According to **impulse response analysis, there is a steadily increasing response of CDS spreads up to the 6th month to shock in SFSI which is also fairly persistent in nature**. When **generalized forecast error variance decomposition (GFEVD) was performed using VAR models with all variables included, the SFSI contributed clearly the most to the variation in CDS spreads**.

We also use the Diebold and Yilmaz's connectedness approach to investigate the spillover of financial stress into CDS spreads over time. A relatively fast pace of impact is expected since CDS spreads are partly driven by speculative trading that also reacts quickly to changing sentiment. Our findings suggest that while **FISS is superior for short-term forecast horizon (up to three months), SFSI fares reasonably well in the long-term forecast**.

Given our empirical findings, we conjecture that the novel news-based sentiment stress index can be deployed to monitor financial stability in the Hungarian economy as it provides reliable and timely information on the magnitude of financial stress. Such sentiment-based metrics can complement traditional stress indicators based on macrofinancial variables like the FISS for Hungary.

Moreover, **one of the key advantages of the index developed in this study is that it can be produced at any frequency and in near real time**, offering a clear advantage over existing indices, which are often released only with significant delays.

Despite the promising results of our proposed index to measure financial stress for Hungary, there are notable limitations that need to be addressed. First, although a vast new corpus is involved in the analysis for a long period, the number of sources for extracting sentiments from textual data is limited. Second, although we showed that Economic Policy Uncertainty for the EU or Geopolitical Risk index for Hungary does not contain information on the contemporary or future movement of the SFSI, it would be nice to know what international stress/uncertainty/risk indicators influence the dynamics of our sentiment-based index (decomposing the variance of CDS spreads into global, regional and country-specific components, there is a strong global factor underlying credit risk spreads, see Kocsis & Nagy, 2011). We advise for future research the study of the interaction between different indices of geopolitical, policy uncertainty, or volatility indices and sentiment-based financial stress index. In addition, in future research, further analysis could be conducted to explore the direction of causality between our sentiment index and indicators of financial market risk in more detail. Moreover, future work could apply non-parametric methods on higher-frequency datasets, especially during crisis periods, in order to capture potentially nonlinear dynamics and short-term stress propagation mechanisms that may remain hidden in analyses based on lower-frequency data.

---

### References

- Aguilar, P., Ghirelli, C., Pacce, M., & Urtasun, A. (2021). Can news help measure economic sentiment? an application in covid-19 times. *Economics Letters*, 199, 109730.
- Ahir, H. (2023). *Financial Stress and Economic Activity: Evidence from a New Worldwide Index* (IMF Tech. Rep. No. 217).
- Baker, M., & Wurgler, J. (2007). Investor sentiment in the stock market. *Journal of Economic Perspectives*, 21(2), 129–152.
- Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring economic policy uncertainty. *The Quarterly Journal of Economics*, 131(4), 1593–1636.
- Bernal, Á. I. M., & Pedraz, C. G. (2020). *Sentiment analysis of the spanish financial stability report* (Working Papers No. 2011). Banco de España.
- Blei, D., Ng, A., & Jordan, M. (2001). Latent dirichlet allocation. In *Advances in neural information processing systems* (Vol. 14). MIT Press.
- Borovkova, S., Garmaev, E., & Lammers, P. (2017). Sensr: A sentiment-based systemic risk indicator. *SSRN Electronic Journal*.
- Caldara, D., & Iacoviello, M. (2022). Measuring geopolitical risk. *American Economic Review*, 112(4), 1194–1225.
- Cevik, E. I., Dibooglu, S., & Kutan, A. M. (2013). Measuring financial stress in transition economies. *Journal of Financial Stability*, 9(4), 597–611.
- Correa, R., Garud, K., Londono, J. M., & Mislang, N. (2020). Sentiment in central banks' financial stability reports. *Review of Finance*, 25(1), 85–120.
- Diebold, F. X., & Yilmaz, K. (2012). Better to give than to receive: Predictive directional measurement of volatility spillovers. *International Journal of Forecasting*, 28(1), 57–66.
- Dim, C., Koerner, K., Wolski, M., & Zwart, S. (2022). *Hot off the press: News-implied sovereign default risk* (EIB Working Papers No. 2022/06). European Investment Bank.
- Engle, R. F., & Campos-Martins, S. (2023). What are the events that shake our world? measuring and hedging global covol. *Journal of Financial Economics*, 147(1), 221–242.
- European Commission. (2025). *The joint harmonised eu programme of business and consumer surveys - user guide.*
- Fernandez, R., Palma Guizar, B., & Rho, C. (2021). A sentiment-based risk indicator for the mexican financial sector. *Latin American Journal of Central Banking*, 2(3).
- García, D. (2013). Sentiment during recessions. *The Journal of Finance*, 68(3), 1267–1300.
- Hakkio, C. S., & Keeton, W. R. (2009). Financial stress: what is it, how can it be measured, and why does it matter? *Economic Review*, 94(Q II), 5–50.
- Hollo, D., Kremer, M., & Lo Duca, M. (2012). *Ciss - a composite indicator of systemic stress in the financial system* (Working Paper No. 1426). European Central Bank.
- Honnibal, M., Montani, I., Van Landeghem, S., & Boyd, A. (2020). *spaCy: Industrial-strength Natural Language Processing in Python.*
- Illing, M., & Liu, Y. (2006). Measuring financial stress in a developed country: An application to canada. *Journal of Financial Stability*, 2(3), 243–265.
- Kalamara, E., Turrell, A., Redl, C., Kapetanios, G., & Kapadia, S. (2022). Making text count: Economic forecasting using newspaper text. *Journal of Applied Econometrics*, 37(5), 896–919.
- Kanelis, D., & Siklos, P. L. (2025). The ecb press conference statement: deriving a new sentiment indicator for the euro area. *International Journal of Finance & Economics*, 30(1), 652–664.
- Kocsis, Z., & Nagy, D. (2011). Variance decomposition of sovereign cds spreads. *MNB Bulletin*, 6(3), 36–50.
- Krishnamurthy, A., & Li, W. (2025). Dissecting mechanisms of financial crises: Intermediation and sentiment. *Journal of Political Economy*, 133(3), 935–985.
- Maghyereh, A., & Abdoh, H. (2022). Global financial crisis versus covid-19: Evidence from sentiment analysis. *International Finance*, 25(2), 218–248.
- Orosz, G., Szabó, G., Berkecz, P., Szántó, Z., & Farkas, R. (2023). Advancing Hungarian Text Processing with HuSpaCy: Efficient and Accurate NLP Pipelines. In *Text, Speech, and Dialogue* (pp. 58–69). Springer Nature Switzerland.
- Pesaran, H. H., & Shin, Y. (1998). Generalized impulse response analysis in linear multivariate models. *Economics Letters*, 58(1), 17–29.
- Püttmann, L. (2018). Patterns of panic: Financial crisis language in historical newspapers. *SSRN Electronic Journal*.
- Ristolainen, K., Roukka, T., & Nyberg, H. (2024). A thousand words tell more than just numbers: Financial crises and historical headlines. *Journal of Financial Stability*, 70, 101209.
- Stolbov, M., & Shchepeleva, M. (2025). A sentiment-based financial stress index for russia. *Borsa Istanbul Review*, 25(2), 350–359.
- Stolbov, M., Shchepeleva, M., & Karminsky, A. (2022). When central bank research meets google search: A sentiment index of global financial stress. *Journal of International Financial Markets, Institutions and Money*, 81(C).
- Szendrei, T., & Varga, K. (2017). *Fiss - a factor based index of systemic stress in the financial system* (MNB Working Papers No. 2017/9). Magyar Nemzeti Bank.
- Szendrei, T., & Varga, K. (2020). Fiss - a factor-based index of systemic stress in the financial system. *Russian Journal of Money and Finance*, 79(1), 3–34.
- Toda, H. Y., & Yamamoto, T. (1995). Statistical inference in vector autoregressions with possibly integrated processes. *Journal of Econometrics*, 66(1-2), 225–250.
- Varga, K., & Szendrei, T. (2025). Non-stationary financial risk factors and macroeconomic vulnerability for the uk. *International Review of Financial Analysis*, 97, 103866.

---

### Appendix A: Data

**Figure A.1:** Evolution of average length of the filtered articles (measured by number of characters, including whitespaces)

---

### Appendix B: Empirical Analysis

#### B.1 Stationarity Tests

**Table A.1:** ADF and KPSS test statistics for different variables

| Variables | ADF t-stat (level) | ADF t-stat (1st diff) | PP t-stat (level) | PP t-stat (1st diff) | KPSS LM-stat (level) | KPSS LM-stat (1st diff) | Order of Integration |
|---|---|---|---|---|---|---|---|
| CDS spread | -2.06 | -11.32*** | -2.07 | -11.43*** | 0.37 | 0.12 | I(1) |
| SFSI | -2.62* | -11.04*** | -2.33 | -15.63*** | 0.40 | 0.17 | I(1) |
| FISS | -2.52 | -11.53*** | -2.82 | -11.64*** | 0.82 | 0.04 | I(1) |
| EPU EU | -2.14 | -13.19*** | -4.24*** | - | 1.38 | 0.26 | I(1) |
| GPRI HU | -4.71*** | -0.1 | -12.16 | - | 0.94 | 0.18 | I(1) |

*** p<0.01, ** p<0.05, * p<0.1

#### B.2 Optimal Lag Length

**Table A.2:** Optimal lag length for pairwise variables based on Schwarz and Hannan-Quinn Information Criteria

| Variables | Schwarz Information Criterion | Hannan-Quinn Information Criterion |
|---|---|---|
| CDS spread - SFSI | 1 | 1 |
| CDS spread - FISS | 1 | 3 |
| CDS spread - EPU EU | 1 | 5 |
| CDS spread - GPRI HU | 1 | 2 |

#### B.3 VAR Specifications

**Table A.3:** Optimal lag length for VAR model (CDS Spread, SFSI, FISS, EPU EU, GPRI HU) — both Schwarz and HQ indicate **VAR(1)**.

**Table A.4:** VAR(1) specifications

| Variables | C | CDS(−1) | SFSI(−1) | FISS(−1) | EPU(−1) | GPRI(−1) | Durbin-Watson |
|---|---|---|---|---|---|---|---|
| CDS | -16.3293* | 0.7967*** | 116.0001*** | 0.1961 | 0.0376 | -79.8728 | 1.74 |
| SFSI | 0.0808*** | 0.0001 | 0.9523*** | -0.0915 | -0.0002* | -0.3677 | 2.03 |
| FISS | 0.0463*** | -0.0002*** | 0.2044*** | 0.7883*** | -0.0001 | -0.3453** | 1.63 |
| EPU | 71.0161*** | 0.0064 | 56.9808* | -137.858*** | 0.7367*** | -98.5545 | 2.20 |
| GPRI | 0.0145** | 0.0001 | -0.0249 | 0.0031 | 0.0001** | 0.1722** | 2.07 |

*** p<0.01, ** p<0.05, * p<0.1

**Figure A.2:** Inverse roots of AR characteristic polynomial — all within unit circle (stable VAR).

---

### Appendix C: Technical Appendix

#### C.1 The Toda–Yamamoto Procedure Testing Granger Causality

The Toda & Yamamoto, 1995 methodology provides a robust framework for testing Granger causality in VAR models when the time-series variables may be non-stationary or cointegrated. The procedure ensures valid Wald inference by estimating an augmented VAR in levels.

**Steps:**
1. Determine d_max, the highest plausible order of integration among variables (via ADF, PP, or KPSS tests)
2. Estimate a VAR(p) in levels with p + d_max lags
3. Test Granger causality using Wald test on the first p lags (ignoring the additional d_max lags)

#### C.2 Generalized Spillover and Connectedness Measure

The Diebold-Yilmaz spillover index uses Generalized Forecast Error Variance Decomposition (GFEVD) from a VAR model. Total spillover = sum of off-diagonal elements of FEVD matrix / total forecast error variance. Directional spillover = column sums (to) or row sums (from) of off-diagonal elements.

Estimated using Binh Pham (2025) MatLab Library for DY Index (github.com/binhpham79/DYIndex).

---

### Metadata

- **title:** Sentiment-based Financial Stress Index for Hungary
- **authors:** Beáta Horváth, Tamás Berki, Lívia Réka Ónozó, Csanád Temesvári
- **year:** 2026
- **journal:** MNB Working Papers 2026/3
- **institution:** Magyar Nemzeti Bank (Central Bank of Hungary)
- **method:** Sentiment analysis, Boolean keyword algorithm, LDA topic filtering, Granger causality (Toda-Yamamoto), VAR, GIRF, FEVD, Diebold-Yilmaz spillover index
- **data:** Two major Hungarian news portals, 2005-2020, ~95 articles/day; CDS spread, FISS, EPU EU, GPRI HU
- **key_result:** SFSI leads CDS spreads (Granger causality p<0.001), persistent IRF (peaks at 30bps, month 5), FEVD: SFSI explains 60% of CDS variance long-term, DY spillover: SFSI dominant transmitter at h≥3 (61.96% at h=12), outperforms FISS long-term; FISS better short-term (h≤3)
- **relevance:** high
- **status:** reviewed
- **tags:** [sentiment-analysis, financial-stress-index, Hungary, news-based, CDS, Granger-causality, VAR, spillover, MNB, Boolean-algorithm, LDA]
- **notes:** Key innovation: Boolean keyword co-occurrence (not frequency) + LDA filtering; real-time producible at any frequency; complements FISS (short-term vs long-term); limited to 2 news sources; no international stress decomposition yet