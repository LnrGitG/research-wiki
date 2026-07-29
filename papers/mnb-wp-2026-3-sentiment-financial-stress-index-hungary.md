

BEÁTA HORVÁTH, TAMÁS BERKI, LÍVIA RÉKA ÓNOZÓ, CSANÁD TEMESVÁRI 

### **SENTIMENT‐BASED FINANCIAL STRESS INDEX FOR HUNGARY** 

MNB WORKING PAPERS | 3 

2026 J U L Y 



### **SENTIMENT‐BASED FINANCIAL** 

### **STRESS INDEX FOR HUNGARY** 

MNB WORKING PAPERS | 3 

2026 J U L Y 

The views expressed are those of the authors’ and do not necessarily reflect the official view of the central bank of Hungary (Magyar Nemzeti Bank). 

MNB Working Papers 2026/3 

###### **Sentiment‐based Financial Stress Index for Hungary** 

(Szentiment alapú pénzügyi stressz index magyar híradatokon) 

Written by Beáta Horváth , Tamás Berki, Lívia Réka Ónozó, Csanád Temesvári 

Budapest, July 2026 

Published by the Magyar Nemzeti Bank 

Publisher in charge: Milán Farkas 

Szabadság tér 8‐9., H‐1054 Budapest 

www.mnb.hu ISSN 1585‐5600 (online) 

We would like to thank dr. Katalin Varga for her helpful suggestions and Dániel Horváth, Balázs Jenei, Zalán Kocsis and Mónika Mátrai‐Pitz for their comments and cooperation. 

Central Bank of Hungary, Szabadság tér 8‐9., 1054 Budapest, Hungary 

CONTENTS 

# **Contents** 

|**Abstract**|4|
|---|---|
|**1 Introducton**|5|
|**2 Literature Review**|7|
|2.1 From Hard to Sof Data|7|
|2.2 From Global to Local Perspectves|7|
|**3 Data and Index Constructon**|9|
|3.1 Data Source|9|
|3.2 Data Filtering|9|
|3.3 Constructon of a Sentment Index|11|
|**4 Performance of the SFSI index**|14|
|4.1 Validaton results ‐ Comparison of the Index with Existng Chronologies|14|
|4.2 Robustness analysis|16|
|4.3 Empirical analysis|17|
|**5 Conclusion**|25|
|**References**|27|
|**Appendix A**<br>**Data**|29|
|**Appendix B**<br>**Empirical analysis**|30|
|B.1 Statonarity tests|30|
|B.2 Optmal lag length|30|
|B.3 VAR specifcatons|30|
|**Appendix C**<br>**Technical appendix**|32|
|C.1 The Toda–Yamamoto procedure testng Granger causality|32|
|C.2 Generalized Spillover and Connectedness Measure|32|



MNB WORKING PAPERS 3 • 2026 **3** 

MAGYAR NEMZETI BANK 

# **Abstract** 

This paper proposes a sentiment‐based financial stress indicator for Hungary based on occurrence of financial crisis related terms and explores its relationship with macrofinancial variables related to financial uncertainty. Sentiment analysis was con‐ ducted on textual data from two major Hungarian news portals covering the period from 2005 to 2020. The terms used in the analysis carry negative connotations, making them suitable for capturing financial instability and stress. The index successfully identifies stress periods that are not adequately reflected by other available sentiment indices related to Hungary. Overall, we propose a novel type of index that enables timely, even real‐time monitoring of financial stress situation in Hungary across different time frequencies. 

JEL Classification: C32, E44, G01 

Keywords: sentiment, financial stress, text analysis 

# **Összefoglaló** 

Jelen tanulmány egy szövegelemzésen alapuló szentiment pénzügyi stressz indikátor előállítását, és annak pénzügyi aktivitással való összefüggéseit vizsgálja. A szentiment elemzést két meghatározó magyar hírportál adatain végeztük 2005 és 2020 között. Az elemzésben használt kifejezések negatív jelentéssel bírnak, így alkalmasak a pénzügyi instabilitás és stressz mérésére. Az index‐ szel azokat az időszakokat is jól megfogtuk, amikre egyéb Magyarországra vonatkozó vagy regionálisan elérhető szentiment indexek nem alkalmasak. Összességében egy olyan új típusú index előállítására teszünk javaslatot, amivel időszerűen, akár valós időben, különböző frekvenciákon követhetjük nyomon a pénzügyi stressz helyzetét Magyarországon. 

**4** MNB WORKING PAPERS 3 • 2026 

INTRODUCTION 

# **1 Introduction** 

Monitoring and quantifying systematic risks in the financial system is crucial for supporting sound policy decisions. Financial stress can be conceived as the amount of risk that has materialized. In this sense, financial stress can be represented by an interval (continuous) variable where extremely high values can be considered as crisis periods. In addition, such indices are suitable for assessing potential negative impact of stress periods on real economic activity. (Szendrei & Varga, 2017) 

The main methodology typically involves the aggregation of numerous financial variables into a single composite indicator, using dimensionality reduction techniques such as principal component analysis or factor analysis. In addition to several country‐ or regional‐level studies (e.g Illing & Liu, 2006, Hakkio & Keeton, 2009, Cevik et al., 2013), supranational bodies such as the ECB (Hollo et al., 2012), the EIB (Dim et al., 2022), or the IMF (Ahir, 2023) have recently developed indices related to financial stress covering relatively long periods of time based on uniform methodologies to ensure comparability between countries, which are continuously updated to monitor financial stability. 

As vast amounts of unstructured, primarily textual data have become more accessible and more convenient to acquire, update, and process, a new strand of empirical research has emerged, focusing on measuring financial stress through the extraction of sentiments from various textual sources. These sentiment‐based proxies can capture increased uncertainty or growing in‐ formational asymmetries (changing risk preferences) in financial markets that can also be driven by irrational behavior and market anomalies, which often contribute to rapidly developing financial instability. In line with these theoretical considera‐ tions, some researches highlighted the role of sentiment influencing stock market performance (see, e.g., M. Baker & Wurgler, 2007; García, 2013) providing a foundational overview on how investors’ sentiments drive market fluctuations and bubbles. Fur‐ thermore, news‐based sentiments proved to have predictive power for potential financial instability and asset price bubbles (see Krishnamurthy & Li, 2025; Maghyereh & Abdoh, 2022). Empirical research showed that article titles in leading newspapers can more accurately signal upcoming financial crises than conventional confidence indicators (Ristolainen et al., 2024) or the newspaper‐based daily sentiment indicator can be used to monitor economic activity in real time (see, e.g., Aguilar et al., 2021). 

Early empirical researches that relied on extracting and incorporating news‐ or social media activity based sentiments when constructing financial stress indices started in the late 2010s thus it is a relatively new field of scientific investigation. Püttmann, 2018 constructed a stress index for the US extracting sentiments from the news title, Stolbov & Shchepeleva, 2025 for Russia using volumes of Internet searches, and Fernandez et al., 2021 for Mexico using tweets. Others focused on tracking global financial instability (see, e.g., Borovkova et al., 2017; Correa et al., 2020; Stolbov et al., 2022). 

Sentiment‐based stress indices for Central and Eastern European countries are still relatively scarce, despite the substantial increase in the number of financial stress indices constructed (Stolbov & Shchepeleva, 2025), especially for Central and Eastern Europe. To addressthe lack of research in this area forpost‐socialist economies in Central and Eastern Europe, we propose alocal sentiment‐based financial index for Hungary. Our index is based on vast amount of textual data from two major Hungarian news portals that sufficiently represent domestic online news media. The analysis covered news articles published between January 2005 and December 2020, a period marked by several turbulent phases ‐ Global Financial Crisis (GFC), events of sovereign debt crisis in Hungary and Europe, COVID‐19 pandemic ‐ in the financial market, making it particularly suitable for testing and validating our sentiment‐based financial stress indicator. As a result, the index successfully captures the event‐related spikes in financial instability observed in the Hungarian economy during this period. 

Our sentiment‐based financial stress index (SFSI) is constructed using a keyword‐driven, Boolean rule‐based algorithmic ap‐ proach. This idea is adapted from S. R. Baker et al., 2016. We examined two sets of expressions: one consists of lexical items related to financial crisis, the other with different areas of the financial system. The scoring at the article level is based on the occurrence of any combination of expressions from the two sets. This procedure rather reflects the extent to which the topic stress/uncertainty in the financial system dominates the text itself. To obtain the composite index time series, a simple arithmetic mean is calculated on all scores of articles deemed relevant and normalized by the number of articles for each period. 

MNB WORKING PAPERS 3 • 2026 **5** 

MAGYAR NEMZETI BANK 

It should be emphasized that the filtering of articles for economic content is of great importance. We used the Latent Dirichlet Allocation (LDA, Blei et al., 2001) algorithm for this purpose which is in line with the empirical literature. This procedure ensures the removal of noise from the news corpus that is irrelevant to the analysis, thereby ensuring that the index is constructed on a solid and relevant dataset. 

We also examine both the predictive relationships and dynamic interactions of the SFSI among key financial and uncertainty‐ related variables using classical econometrics methods. The variables used in the analysis include the 5‐year sovereign CDS spread for Hungary (CDS), the Factor Based Index of Systematic Stress (FISS), the Economic Policy Uncertainty (EPU) index for the EU, and the geopolitical risk index (GPRI) for Hungary. While Granger causality tests indicate that our sentiment‐based financial stress index (SFSI) contains statistically significant information about future CDS spread values, also, VAR analysis shows that the SFSI tends to precede CDS spread variable and has lasting, significant effect on the CDS spread ‐ outperforming all other indicators included in the VAR analysis where all variables are included. The forecast error variance decomposition (FEVD) reveals that a substantial proportion of the variance in the CDS spread is explained by our index. 

The Diebold–Yilmaz spillover analysis applies the connectedness framework to examine how financial stress affects CDS across different forecast horizons. It captures both the magnitude and direction of interconnectedness and shock transmission among the VAR variables and highlights the increasing systemic importance of the SFSI over time. According to the directional spillover results, the SFSI exhibits strong explanatory power for the CDS spread over both short‐ and long‐term horizons. 

In summary, our study may contribute to the existing literature in many ways. We demonstrated that the feasibility of incor‐ porating sentiment into financial stress index from limited number of online sources for Hungary. The results confirm that news‐based sentiment tools can effectively capture turbulent periods in the Hungarian financial and economic system just as an earlier country‐specific stress index did (FISS, see Szendrei & Varga, 2017), but other sentiment indicators for Hungary (EPU, GRPI) had not. Our index has a relatively strong performance in tracking financial stress compared to other contender in‐ dices using standard macroeconomic evaluation methods. Thus, considering a sentiment‐based stress index not as substitutes, but rather as complementary tools in understanding the multifaceted nature of financial stress alongside indicators based on numerous high frequency financial variables. Based on these findings, we consider the SFSI a valuable indicator to monitor financial stability in Hungary. 

The paper is organized as follows. Section 2 gives a brief overview of the empirical literature measuring financial stress based on sentiments extracted from non‐conventional, unstructured data sources. Section 3 describes the data source, provides a picture of the data filtering approach, and gives a detailed view of the index construction methodology. Section 4 outlines the methods used to assess the performance of the index before concluding the paper in the last section. 

**6** MNB WORKING PAPERS 3 • 2026 

LITERATURE REVIEW 

# **2 Literature Review** 

#### **2.1 FROM HARD TO SOFT DATA** 

Since the Global Financial Crisis, the issue of systemic risk has captured the attention of academics, regulators, and private agents in the financial system. Financial stress and risk indices have been derived by machine learning and text mining tech‐ niques, allowing the process and handling of increasing volumes of unstructured (text) data. Besides the arm of literature relying on „hard data” (Hollo et al., 2012) which mostly consists of various high‐frequency financial market indicators, an in‐ creasing amount of research analyzes ‘soft information’ to capture financial risk, systemic financial risk, or uncertainty related to economic policy, geopolitics (Caldara & Iacoviello, 2022) and volatility (Engle & Campos‐Martins, 2023). 

#### **2.2 FROM GLOBAL TO LOCAL PERSPECTIVES** 

Borovkova et al., 2017 developed a sentiment‐based risk indicator for the global financial system that is constructed by aggre‐ gating news sentiment about systemically important financial institutions. Their index, SenSR consistently leads traditional risk indicators and macroeconomic signals by up to 12 weeks. One of the first studies aimed to construct a historical stress index focusing on global level and US stress, Püttmann, 2018 compiled a high‐frequency Financial Panic Index spanning 1889–2016 by analyzing more than 35 million U.S. newspaper titles in five major newspapers. He concludes that changes in the use of crisis ‐‐related language in terms of sentiment in the print media offer a robust, historically informed early warning signal of financial instability. Correa et al., 2020 developed a Financial Stability Sentiment (FSS) index using textual analysis of central banks’ Financial Stability Reports (FSRs) in 30 countries from 2005 to 2017, to investigate how central bank messaging reflects and predicts the financial cycle. A custom dictionary was compiled where words were classified as positive or negative, and these were aggregated to generate time series of FSS for each country. As a result, indices move in sync with financial cycle indi‐ cators, that is, central bank sentiment in official communication can be an early warning indicator of financial fragility. Stolbov et al., 2022 introduces a novel sentiment‐based index of global financial stress by combining central bank research outputs with Google search data. The study employs text mining and machine learning techniques to quantify the intensity of negative sentiment related to financial instability as reflected in both expert and public attention. The resulting index demonstrates strong correlations with traditional financial stress indicators and offers a timely, high‐frequency measure to monitor global financial conditions. Dim et al., 2022 introduce the News‐Implied Sovereign Risk Index (NSRI), constructed through natural language processing of approximately 10 million news articles across more than 100 countries, offering a high‐frequency proxy for sovereign default risk. The NSRI exhibits strong contemporaneous and predictive correlations with sovereign CDS spreads, serves as an early warning indicator for sovereign credit rating downgrades, and captures aspects of risk not fully reflected in CDS spreads data. 

A country‐level study (Fernandez et al., 2021) proposed a sentiment‐based risk indicator (SRI) for the Mexican financial sector by systematically analyzing the tone of tweets regarding financial institutions. Using natural language processing and machine learning techniques, they extract sentiment from domestic media sources to construct an index that measures the prevalence of negative sentiment over time. The results demonstrate that the SRI effectively identifies periods of financial distress and serves as a valuable complement to traditional market‐based indicators. Stolbov & Shchepeleva, 2025 presents a sentiment‐based fi‐ nancial stress index for Russia derived from the volumes of internet searches in financial terms with a negative connotation about financial stability. The constructed index quantifies negative market sentiment and is systematically validated against conventional stress indicators ‐ including exchange rate volatility, interest rate spreads, and equity market fluctuations ‐ to demonstrate its responsiveness to worsening financial conditions. Their index provides a supplementary tool for macropru‐ dential monitoring within the Russian financial environment. Bernal & Pedraz, 2020 conduct a sentiment analysis of the Bank of Spain’s FSRs to assess the relationship between institutional tone and financial market developments. Their findings indicate that changes in the sentiment of the report are significantly correlated with financial stress indicators, highlighting the potential of central bank communication as a forward‐looking tool to monitor systemic risk. In addition, their index has a strong negative correlation with the Spanish GDP and a strong positive correlation with stock market volatility and CDS spreads. 

MNB WORKING PAPERS 3 • 2026 **7** 

MAGYAR NEMZETI BANK 

The evidence in the empirical and theoretical literature suggests that social media activity or news content may influence agents in the financial market, thus underlying the role of sentiment in financial crises. The use of news‐based textual data to quantify financial risk/stress is based on the assumption that news media are observed at a high frequency and contain timely information about developments in domestic and international financial markets which is likely to influence the perceptions and expectations of economic agents. In short, general sentiment distilled from relevant news can depict the dynamics of popular narrative about financial system. 

**8** MNB WORKING PAPERS 3 • 2026 

DATA AND INDEX CONSTRUCTION 

# **3 Data and Index Construction** 

#### **3.1 DATA SOURCE** 

Our study focuses on textual data acquired from two major Hungarian news portals, which were selected due to their ability to adequately represent domestic online media. The data acquisition process, including the extraction, processing and storage of the information, was carried out in full compliance with current legal regulations and in consent with the respective media organizations.¹ 

The analysis covered news articles published between January 2005 and December 2020, with a daily average of 95 articles, all published in Hungarian. The average length of the articles per year is shown in Figure A in Appendix A. This period included several financially turbulent phases and major global and domestic economic events, such as the global financial crisis of 2008– 2009, the Greek sovereign debt crisis of the 2010s, the mandatory settlement and conversion of foreign currency‐denominated household loans into forints in Hungary, and the onset of the COVID‐19 pandemic. As all of these events are associated with financial and economic instability and stress, this period is well‐suited for testing and validating our sentiment‐based financial stress indicator. 



<!-- Start of picture text -->
Figure 1<br>Number of filtered articles from two major Hungarian news portals between 2005 and 2020<br><!-- End of picture text -->





<!-- Start of picture text -->
Source: MNB.<br><!-- End of picture text -->

#### **3.2 DATA FILTERING** 

In preparing the dataset for modeling, several preprocessing steps were implemented to ensure data quality and consistency. Duplicate articles were identified and eliminated from the corpus to prevent redundancy that could skew our results and in‐ 

¹ These procedures ensured that the study adhered to relevant copyright, privacy, and data protection laws. 

MNB WORKING PAPERS 3 • 2026 **9** 

MAGYAR NEMZETI BANK 

troduce unexplainable variance into our processes. The articles underwent comprehensive cleaning through the removal of non‐linguistic elements including extra hyphens, line breaks and email addresses to standardize the dataset and eliminate un‐ necessary noise that could interfere with further elements of the computational pipeline. As a next step, the whole dataset went through lemmatization. This step consolidates words and phrases into their root representations, standardizing the contents for downstream tasks and reducing the dimensionality of the feature space while preserving semantic meaning². 

After the data preprocessing, we conducted a preliminary exploratory analysis to better understand the information content of the articles. To be able to create a metric to model financial stress in the economy, it is essential that the news articles we analyze are relevant to this matter. The news corpus was varied in terms of topics, ranging from tabloid journalism to meteorological reports, which resulted in a low signal‐to‐noise ratio in SFSI index. To combat this, a topic modeling approach was employed to filter out and retain economically relevant articles. We experimented with multiple different unsupervised machine learning algorithms, namely LDA, HDBSCAN³ and K‐Means over BERT⁴ embeddings, out of which LDA gave the best results in terms of topic cohesion. The LDA algorithm, applied to the preprocessed dataset, treats individual articles as discrete documents within a probabilistic framework. The model estimation creates a probability distribution for each article over a number of latent ” _topics_ ”, fixed at the start of the training, while also creating a distribution for each topic over all the available words in the dataset, based on word counts and co‐occurrences. The model’s hyperparameters (the number of topics, the parameters of the initial distributions and the batch size) were optimized through grid search. We evaluated the goodness‐of‐fit of each model by measuring the perplexity, which measures how well the model generalizes to new data. 

To assess which category to keep, we examined the top 20 words of each category to find relevant keywords. The final model contained 16 topics, 13 of which were found relevant to our analysis having a predominantly economic and/or financial focus. 

###### **Figure 2** 

**The constructed index from the unfiltered and filtered data at weekly and monthly frequency (See Section 3.3 for the index construction)** 



<!-- Start of picture text -->
Source: MNB.<br><!-- End of picture text -->

The effect of the data filtering can be seen in Figure 2. The plots show the indices resulting from the boolean method, aggregated to weekly and monthly frequency. Clearly, the index constructed from unfiltered set of articles is extremely volatile with a low signal‐to‐noise ratio. However, after LDA filtering, the resulting index resembles the CDS spread times series much better. 

> ² We also filtered out any word which was not a noun, adjective, verb, adverb or a proper noun. The data cleaning was carried out using regular expressions, while the lemmatization was done using the Spacy software library (Ver. 3.5.4) (Honnibal et al., 2020), using the _hu_core_news_lg_ model (Ver. 3.5.2) (Orosz et al., 2023) 

> ³ Hierarchical Density‐Based Spatial Clustering of Applications with Noise 

> ⁴ Bidirectional Encoders Representations from Transformers 

**10** MNB WORKING PAPERS 3 • 2026 

DATA AND INDEX CONSTRUCTION 

#### **3.3 CONSTRUCTION OF A SENTIMENT INDEX** 

The construction of a sentiment indicators may be categorized into four main methodological approaches: survey‐based meth‐ ods, keyword‐based algorithmic techniques, Boolean rule‐based algorithms, and machine learning models. 

Survey‐based methods rely on direct collection of data from individuals or businesses, typically through questionnaires or struc‐ tured interviews, to gain insight into subjective opinions and expectations. One of the best‐known examples is the Economic Sentiment Indicator (ESI), compiled by European Commission, 2025. 

Keyword‐based algorithmic techniques use predefined dictionaries of positive and negative words to quantify sentiment by counting the frequency of these terms in textual data. (see, e.g., Kalamara et al., 2022) 

Boolean rule‐based algorithms apply logical operators such as AND, OR, and NOT to detect the presence or co‐occurrence of specific terms, phrases, or structural patterns within a text. These systems are manually constructed using expert knowledge or domain‐specific heuristics. (see, e.g., S. R. Baker et al., 2016) 

Deep learning methods, as state‐of‐the‐art approaches within machine learning, leverage labeled datasets to train models that classify sentiment (positive, neutral, negative) based on patterns learned from the data. These models can capture contextual nuances and achieve higher predictive accuracy. (see, e.g., Kanelis & Siklos, 2025) 

Each of these methodologies presents unique strengths and limitations. Survey‐based methods benefit from direct human input but can be costly and time consuming. Algorithm‐based methods, such as keyword‐ or rule‐based approaches, are interpretable and easier to implement but may lack contextual understanding. Deep learning models, while powerful, require substantial amount of labeled data and computational resources. The choice of the appropriate methodology may depend on the specific research context, the availability and nature of the data, and the trade‐off between interpretability and predictive performance. 

#### **BOOLEAN ALGORITHM** 

In our research, we sought a method that is easy to interpret, explain, and implement. Based on these considerations, we selected a Boolean rule‐based approach from the algorithmic methods. 

With the involvement of subject‐matter experts, we compiled a set of expressions related to financial instability and stress. Based on this, we created two sets: one consisting of terms referring to the financial system, such as _finance, economy_ and another comprising negative sentiment expressions associated with stress and instability, such as _risk, uncertainty_ . 

#### **CONSTRUCTING THE INDEX** 

The SFSI index used in our analysis is based on articles filtered using the LDA algorithm; see Section 3.2. For each article 𝐴 , we define indicator variables to represent the presence of unique keywords from the two predefined sets: financial system keywords: 𝐹= {𝑓1, 𝑓2, … , 𝑓𝐹 } and stress‐related keywords: 𝑆= {𝑠1, 𝑠2, … , 𝑠𝑆} . 

For each 𝑓∈𝐹 let 𝐼𝑓<sup>𝐴be the indicator variable defined as</sup> 



Similarly, for each 𝑠∈𝑆 : 



Based on these indicators, we compute for each article 𝐴 : 

MNB WORKING PAPERS 3 • 2026 **11** 

MAGYAR NEMZETI BANK 

- the number of unique financial system keywords: 



- and the number of unique stress‐related keywords: 

The composite index is then defined as the average, over a collection of 𝐾 articles {𝐴1, 𝐴2, … , 𝐴𝐾} , of the co‐occurrence measured by the product of the previously calculated counts. 



The index can be computed for any chosen temporal frequency (e.g., daily, weekly, or monthly). This formulation ensures that each article contributes proportionally to the index value based on the keywords it contains. It is important to note that each keyword is counted only once per article, regardless of how many times it appears. Thus, the SFSI index does not reflect mere frequency of occurrence, but rather the extent to which concepts related to the financial system and stress are jointly present in the text corpus. 

Some examples of the calculation of the SFSI index are shown in Table 1. 

|**Table 1**<br>**Examples for calculaton of the ind**<br>|**ex**⁵<br>⁶|||||
|---|---|---|---|---|---|
|News originally in Hungarian|News translated into English|source|Keywords for f‐<br>nancial system|Keywords<br>for<br>stress|Score|
|”... Bank<br>fokozot óvatosságra int a<br>felhasználókat ... . Ezek a hamisí‐<br>tot internetes tartalmak amellet,<br>hogy egy pénzügy<br>i csalás részét is<br>képezhetk, informatkai‐biztonsági<br>kockázat<br>okat is jelenthetnek...”|”... Bank<br>urges users to exercise in‐<br>creased cauton... . These fake on‐<br>line contents may not only be part<br>of afnancial<br>fraud scheme, but also<br>pose cybersecurityrisk<br>s. ...”|mt.hu,<br>2020|bank, fnance|risk|2|
|...<br>Az új vámintézkedések mi‐<br>at<br>világszerte<br>megnövekedet<br>a<br>gazdaság<br>i<br>és<br>pénzpiac<br>i<br>bizonytalan<br>ság ….<br>a vámháború<br>miat az alacsonyabb növekedési<br>és a magasabb infációskockázat<br>ok<br>Magyarországra is hatással lehet‐<br>nek...”<br>_Source:_ MNB.|”...Due<br>to<br>the<br>new<br>customs<br>measures,<br>economic<br>and<br>fnancial market<br>uncertainty<br>has increased worldwide.<br>As a<br>result of the trade war, therisk<br>sof<br>lower growth and higher infaton<br>may also afect Hungary. ...”|Facebook,<br>2025|economy,<br>fnan‐<br>cial market|uncertain, risk|4|



By construction, the index is bounded due to the finite number of keywords and articles. Consequently, a long‐term trend is not expected to materialize, the index is assumed to exhibit mean‐reverting dynamics, returning to its baseline level once extraordinary events fade out. Nevertheless, some short‐term persistence may occur, reflecting the at ude of journalists to focus on certain news topics for a while. 

#### **KEYWORD SENSITIVITY ANALYSIS ‐ FINAL SET OF KEYWORDS** 

The objective was to identify and remove redundant terms in order to derive a transparent and interpretable model that accu‐ rately preserves the dynamic properties of the original full system. To evaluate the sensitivity of the keyword‐based method, we applied a two‐stage analysis based on Autoregressive Moving Average (ARMA) modeling. 

> ⁵ Examples are drawn from online news sources other than those underlying the index. 

> ⁶ translated with ChatGPT 

**12** MNB WORKING PAPERS 3 • 2026 

DATA AND INDEX CONSTRUCTION 

The ARMA model specification was determined using an automatic selection procedure, where the maximum orders were restricted to ARMA(4,4). The procedure also incorporated automated testing for differencing and log transformation. The final specification was selected based on the Akaike information criterion (AIC) in all cases. This approach ensures that model selection is comparable across all examined time series. 

For the baseline model, which includes all keywords, an ARMA(2,3) specification was identified. Although stationarity was borderline (see 4.3 and A.1 in Appendix B), diagnostic tests indicated that neither differencing nor transformation was required in this field of analysis. This is supported also by the Durbin–Watson statistic and the fact that the inverted AR and MA roots lie within the unit circle, confirming the stability of the estimated model. 

In the first stage, each keyword was removed individually from the original full keyword set. For each removal the corresponding output time series was generated and an ARMA model was fitted. The order of the resulting ARMA model and its estimated coefficients were then compared to those of the baseline model obtained using the full keyword set. Differences in model order were interpreted as indications of changes in the underlying dynamics, while coefficient stability was evaluated relative to the 95% confidence intervals of the baseline estimates. If the removal of a keyword resulted in a different model order or in parameter estimates falling outside these confidence intervals, the keyword was classified as influential and retained; otherwise, it was provisionally classified as non‐influential and added to a candidate pool for further analysis. 

The second stage assessed whether combinations of the provisionally non‐influential keywords from the candidate pool could jointly influence the model’s behavior. The procedure began by identifying a pair of keywords whose simultaneous removal did not cause differences in the ARMA order or the estimated coefficients to fall outside the baseline confidence intervals. Starting from this pair, additional keywords from the candidate pool were added to the removal set, one at a time. After each addition, the corresponding time series was generated, and the ARMA model was re‐estimated to verify that the model order and coefficient stability was preserved. This iteration continued until joint removals produced statistically significant deviations from the baseline model. 

The two‐stage analysis resulted in a reduced yet sufficient set of keywords, containing only those that non‐negligibly influence the temporal behavior of the original system. The final set offers a clearer and more interpretable representation, while still preserving the essential characteristics of the full original, expert‐defined model. 

MNB WORKING PAPERS 3 • 2026 **13** 

MAGYAR NEMZETI BANK 

# **4 Performance of the SFSI index** 

#### **4.1 VALIDATION RESULTS ‐ COMPARISON OF THE INDEX WITH EXISTING CHRONOLOGIES** 

Evaluation of SFSI performance is not straightforward. One of the most commonly used methods to assess the performance of an index is whether its peak values coincide with the timing of certain ’well‐defined’ crisis events. Since the time interval of evaluation is fairly long and there were several turbulent periods between 2005 and 2021, we have divided the SFSI chart into two for better presentation. Figure 3 shows the period between 2005 and 2012, while Figure 4 presents the period between 2013 and 2020. It covers pre‐GFC events with the building up of subprime mortgage crisis followed by the period of GFC and European sovereign bond crisis. After 2013 there is a long period of post crisis where several notable events occurred that induced mostly minor turbulences in the financial market. We closely follow the selection of events involving turbulence in the Hungarian financial market (Szendrei & Varga, 2020), who benchmark their FISS using in a similar manner when evaluating the FISS as is customary in the literature (e.g. Hollo et al., 2012). 



<!-- Start of picture text -->
Figure 3<br>Timeline of events between 2005 and 2012<br><!-- End of picture text -->



<!-- Start of picture text -->
Source: MNB.<br><!-- End of picture text -->

_By July 2007 it became apparent that confidence in mortgage‐backed securities evaporated_ when Bear Stearns announced that two of its hedge funds had virtually bankrupted. This announcement heightened global risk aversion due to growing uncertainty, which is reflected in the movement of the SFSI, in parallel with the harsh reaction in the FX and capital markets. On November 15, 2007 Standard & Poor downgraded the investment bank amid concerns of their solvency. As a reaction, the index rose significantly at the same time. 

**14** MNB WORKING PAPERS 3 • 2026 

PERFORMANCE OF THE SFSI INDEX 

_Subprime crisis caused turbulence on the Hungarian government bond market in March 2008_ , while SFSI reached a new high and its value did not drop off significantly after March. 

_Bankruptcy of Lehman Brothers in September 2008_ marked the era of widespread uncertainty on financial markets globally. Deepening of GFC lead to sudden spike in the SFSI. During October 2008 record‐breaking falls happened on the stock markets especially in the US. 

_Turbulence on the Hungarian foreign exchange spot markets in January‐March 2009._ Significant depreciation happened in the HUF/EUR exchange rate with heightened volatility. In parallel, there was a spike in the SFSI. This turbulence reflected concerns about the large exposure of Hungarian banks to FX‐denominated credits to domestic debtors. 

The _European sovereign bond crisis_ started with the major event of downgrading Greece’s credit rating to junk bond category by Standard & Poor rating agency in April 2010. Values of the SFSI elevated considerably as concerns about the increased volatility on FX and government bond market in Hungary also fueled by ambivalent statements of prominent politicians regarding public finances by the newly formed Hungarian government. 

_Heightened concerns about euro are sovereign debt problems (May‐August 2011),_ including downgrading of Greece, warning about Italy and downgrading I the US. In parallel, investors’ risk aversion rose, CHF/HUF exchange rate – relevant for considerable degree of household debtors having CHF denominated mortgage loans ‐ hit all time high. SFSI continuous increase in 2011 mirrored deteriorating macrofiscal and financial market conditions in Hungary. 

_Announcement of early repayment of FX denominated loans at a favorable exchange rate in September 2011._ Since losses from early repayment was to be borne by banks this event might contributed to further increase in SFSI that peaked at the end of 2011‐early 2012. 



<!-- Start of picture text -->
Figure 4<br>Timeline of events from 2013 to 2021<br><!-- End of picture text -->

_Source:_ MNB. 

New chapter of _Greek debt crisis_ emerged in the form of the resignation of Greek prime minister and elections failed to produce a stable government with a mandate to deliver the country’s austerity programme, which heightened concerns among investors. A small peak is observable for the SFSI in 2012 after the considerable hike in 2011. 

MNB WORKING PAPERS 3 • 2026 **15** 

MAGYAR NEMZETI BANK 

From 2013 SFSI can be characterized with a gradual declining trend as Euro sovereign debt problem alleviated, however, minor event could have had potentially negative impact: 

- Mandatory Conversion of remaining household foreign currency and foreign‐currency‐denominated loans into forints at a fixed exchange rate (December, 2014 – January 2015) 

- A Greek debt repayment debacle took place in June, 2015, newly elected Prime Minister Alexis Tsipras announced that he will push for a renegotiation of bailout terms, debt cancellation, and renewed public sector spending, causing excess volatility of the euro exchange rate against other important currencies. 

- Brexit referendum in June 2016, 

- US presidential election result in November 2016. 

A major shift was caused by the _outbreak of the Covid‐19 pandemic in March 2020_ that prompted countries to resort to emer‐ gency laws setting harsh restrictions (ban of gatherings, border closure, etc.). Financial markets reacted promptly, causing distress in many markets, raising concerns about company solvency due to earlier unprecedented corporate debt issuance and low cost of financing. SFSI remained at a high level until the beginning of 2021. 

#### **4.2 ROBUSTNESS ANALYSIS** 

Next, we are going to assess the robustness of the SFSI index. In particular, we want to evaluate the sensitivity with respect to the number of articles used to produce it. To achieve this, we conducted a simulation to create an alternative index by randomly removing a percentage of the original database of articles on two levels: 10 and 40 percent, the latter corresponding to the event of losing one medium⁷. Then, we calculated the sentiment financial stress index from the remaining articles in the way described in Section 3.3.2. We ran this simulation a thousand times and in the end we averaged out all the indices to arrive at the final alternative index. 



<!-- Start of picture text -->
Figure 5<br>Difference of the original index to the robust indices<br>Source: MNB.<br><!-- End of picture text -->

Figure 5 shows the differences of the values of the original index compared to the robustness index for both percentages. The plot shows how the maximum average difference does not exceed the thousandths for the index constructed with 60 percent 

⁷ Only in the sense of magnitude. We did not actually take the medium into account, each run is sampling from both media. 

**16** MNB WORKING PAPERS 3 • 2026 

PERFORMANCE OF THE SFSI INDEX 

of the data, with the 90 percent ”index” differing are one order of magnitude smaller, indicating an extreme robustness to the construction of the index. 

#### **4.3 EMPIRICAL ANALYSIS** 

To evaluate the economic relevance and informational content of the newly constructed sentiment‐based Financial Stress Index (FSI), we apply a set of multivariate time series techniques designed to capture both predictive relationships and dynamic interactions among key financial and uncertainty‐related variables. Specifically, empirical analysis includes Granger causality tests, Impulse Response Functions (IRF), Forecast Error Variance Decomposition (FEVD), and the Diebold–Yilmaz (DY) spillover index. These methods are complementary: Granger tests assess whether the sentiment index contains leading information about other financial risk indicators, while IRFs allow us to trace the transmission mechanism of shocks over time. FEVD is used to quantify how much variation in a given variable—such as the sovereign CDS spread — can be attributed to shocks in our index. Finally, the DY spillover framework enables us to evaluate the system‐wide connectedness of the index and whether it acts as a net transmitter or receiver of financial stress. Together, this methodological framework allows us to assess whether sentiment‐ based FSI provides additional information about the dynamics of financial risk ‐ complementing what is already captured by standard stress, policy, and geopolitical uncertainty indicators. 

To comprehensively evaluate the role of the Sentiment‐based Financial Stress Index (SFSI) in capturing financial risk dynamics, we consider the following key variables: 

- 5‐year Sovereign CDS spread (Hungary): This variable reflects the market assessment of Hungary’s sovereign credit risk, which is the price of insurance against sovereign default. An increase in the CDS spread indicates a higher perceived risk of default event, making it a direct market‐based indicator of financial stress at the country level. (hereinafter: CDS spread, datasource: Datastream (LSGE)) 

- Factor based Index of Systematic Stress (FISS): The FISS is as a measure of financial stress in the Hungarian financial system proposed by Szendrei and Varga (Szendrei & Varga, 2020). It provides a comprehensive picture of the contemporary level of systemic risk stress through a dynamic factor mdel based on 19 variables covering all core segments of the financial system (hereinafter: FISS, datasource: MNB). 

- Economic Policy Uncertainty (EPU) Index – European Union: The EPU index quantifies uncertainty related to economic policy by analyzing the frequency of newspaper articles mentioning economic, policy, and uncertainty. (S. R. Baker et al., 2016) In the absence of a country‐specific EPU index for Hungary, our analysis relies on the European Union‐wide EPU indicator. (hereinafter: EPU_EU, datasource: www.policyuncertainty.com) 

- Geopolitical Risk (GPR) Index – Hungary: Caldara et al. (Caldara & Iacoviello, 2022) construct both global and country‐ specific GPR indices using a dictionary‐based approach. Their methodology relies on a predefined set of keywords that are typically associated with the coverage of geopolitical events and threats in newspaper articles, such as war, terrorism. A Hungary‐specific GPR index is available from 1905 onwards. (hereinafter: GPRI_HU, datasource: https://www.matteoiacoviello.com/gpr.htm) 

In the analysis, sovereign CDS spreads are employed as the primary dependent variable, serving as a forward‐looking, market‐ based measure of credit and sovereign risk. Particularly over the examined period, CDS spreads proves to be an empirically relevant benchmark for financial stress. 

In addition to CDS spreads, the FISS, EPU, and GPRI indices capture different dimensions of stress and uncertainty. Their inclusion allows us to control for economic and financial stress and assess whether the proposed news‐based stress index provides additional explanatory power. 

#### **GRANGER CAUSALITY** 

The Granger causality is a widely used statistical method in economics to determine whether one time series can predict or ”cause” another. It tests whether the past values of one time series provide statistically significant information about the future 

MNB WORKING PAPERS 3 • 2026 **17** 

MAGYAR NEMZETI BANK 



<!-- Start of picture text -->
Figure 6<br>Variables assessed in the empirical analysis<br><!-- End of picture text -->

_Source:_ MNB. 

values of another time series. In other words to test whether 𝑌 does not Granger cause 𝑋 we use the following regression equation: 



The goal is to determine whether the lagged values of 𝑌 have any significant effect on contemporary values of 𝑋 . The null hypothesis 𝐻0 states that 𝑌 does not Granger cause 𝑋 , which is represented as: 



In other words, the coefficients 𝛽𝑗 for the lagged values of 𝑌 are zero, meaning that past values of Y have no effect on predicting X. If this hypothesis holds true, it suggests that 𝑌 does not provide any information for forecasting 𝑋 . In our case, we applied the test to examine the causal relationship between the CDS spread time series of Hungary and the SFSI index constructed above. The Granger causality test allows us to investigate whether past values of our SFSI index can predict or influence the current or future values of the CDS spread. 

Since Granger causality tests require stationary time series for valid inference, we began our analysis by testing the stationar‐ ity of the variables. To address this, we apply Augmented Dickey‐Fuller (ADF), Phillips‐Perron (PP) and Kwiatkowski–Phillips– Schmidt–Shin (KPSS) tests. The former two tests are used to check for the presence of a unit root in a time series, with the null hypothesis indicating non‐stationarity. In contrast, the KPSS test assumes stationarity under the null hypothesis, making it a useful complement to the ADF and PP tests. 

In case of our variables the ADF and PP tests suggest the presence of unit roots, while the KPSS test shows in most cases borderline evidence in favour of stationarity (see Table A.1 in Appendix B). Therefore, we follow the lag‐augmented approach proposed by Toda & Yamamoto, 1995, which allows us to test the Granger causality in levels, even when the underlying variables may be integrated or non‐stationary. 

**18** MNB WORKING PAPERS 3 • 2026 

PERFORMANCE OF THE SFSI INDEX 

To determine the optimal lag length, we examined both the Schwarz and Hannan‐Quinn (HQ) information criteria. As shown in Table A.2 in Appendix B, instead of the more parsimonious Schwarz criterion, which returned a value of 1 in all cases, we used the HQ results for the Granger causality tests. 

|**Table 2**<br>**Results of Toda‐Yamamoto Granger causality tests**<br>|||
|---|---|---|
|Null hyphothesis|𝜒<sup>2</sup>|Prob|
|CDS spread←SFSI index|19.014|0.000|
|SFSI index←CDS spread|0.092|0.761|
|CDS spread←FISS|16.199|0.001|
|FISS←CDS spread|7.665|0.0535|
|CDS spread←EPU EU|8.628|0.125|
|EPU EU←CDS spread|9.179|0.1021|
|CDS spread←GPRI HU|1.534|0.6743|
|GPRI HU←CDS spread|1.334|0.7209|
|_Source:_ MNB.|||



Table 2 presents the results of the Toda‐Yamamoto Granger causality test for the VAR models, considering pairwise relationships between the CDS spread and the SFSI index, the FISS, the EPU index for EU (EPU EU) and the geopolitical risk index for Hungary (GPRI HU). 

The Toda‐Yamamoto Granger causality tests indicate an unidirectional relationship from our index to the target variable, sug‐ gesting that it contains predictive information to the CDS spread. FISS exhibits a bidirectional relationship with the CDS spread, while the remaining indicators do not show significant causal links. 

In summary, the results suggest that our index contains relevant information one month in advance, allowing a more accurate explanation and prediction of the CDS spread. 

#### **GENERALISED IMPULSE RESPONSE FUNCTION** 

Impulse response functions trace the time path of the effect of a one‐time shock to one variable on the current and future values of the other variables in the system. They are particularly useful in assessing the dynamic behavior of macroeconomic variables in response to structural changes or innovations. IRFs help visualize both the direction and persistence of the impact across time horizons. 

The Generalized Impulse Response Function (GIRF), introduced by Pesaran & Shin, 1998, offers a robust extension to the tra‐ ditional impulse response analysis in a vector autoregressive (VAR) framework. Unlike the standard IRF, which requires or‐ thogonalised shocks often obtained through a recursive Cholesky decomposition, the GIRF approach does not depend on the ordering of variables. This characteristic makes GIRF particularly valuable when the theoretical justification for variable ordering is ambiguous. 

In the context of our research, where we analyze the influence of multiple related indices on the target variable, the GIRF methodology is especially appropriate. This approach allows us to compare how the CDS spread responds to one standard deviation shocks in the newly constructed SFSI, FISS, EPU, and GPRI indices, invariant to the ordering of variables. 

Before performing the generalized impulse response function (GIRF) analysis, it is necessary to ensure that the underlying VAR model is appropriately specified and satisfies standard assumptions regarding stationarity, lag length, stability, and the absence of substantial autocorrelation. 

MNB WORKING PAPERS 3 • 2026 **19** 

MAGYAR NEMZETI BANK 

Although formal stationarity tests (see Table A.1 in the Appendix) yield borderline results, the time series is retained in levels without transformation in the VAR specification. This choice is supported by the construction of the index: as discussed earlier, the index is bounded, precluding the emergence of a deterministic long‐term trend, and it is assumed to exhibit mean‐reverting dynamics, returning to its baseline level once extraordinary events fade out. 

The optimal lag length for the VAR model is determined based on the Schwarz (BIC) and Hannan‐Quinn (HQ) information criteria, indicating a VAR(1) specification (see Table A.3 in the Appendix). 

The coefficients of the estimated VAR(1) model are presented in the table A.4 in the Appendix. The VAR(1) model is stable, as all inverse roots lie within the unit circle (see Figure A.2 in the Appendix). Residual diagnostics, based on Durbin‐Watson statistics (see table A.4 in Appendix), indicate no substantial autocorrelation, supporting the validity of the estimated VAR(1) model for further analysis. 



<!-- Start of picture text -->
Figure 7<br>Response to Generalized One S.D. Innovations<br><!-- End of picture text -->



<!-- Start of picture text -->
Source: MNB.<br><!-- End of picture text -->

The generalized impulse response function (GIRF) analysis reveals the dynamic impact of a one‐standard‐deviation shock from each index on the CDS spread. The newly constructed SFSI index causes an immediate increase of approximately 12–13 basis points in the CDS spread. This effect intensifies in the subsequent months, peaking around the fifth month at nearly 30 basis points, before gradually diminishing over a horizon of around 24 months. The persistent and steadily increasing nature of this response suggests that the index provides valuable structural information with a lasting influence on the CDS spread. 

In comparison to the SFSI, the CDS response to a shock in the FISS index is slightly stronger at the initial point; its impact peaks earlier ‐around the second month‐ and diminishes more quickly, fading out by the tenth month. 

**20** MNB WORKING PAPERS 3 • 2026 

PERFORMANCE OF THE SFSI INDEX 

The EPU EU index displays a similar response pattern to FISS, with an early peak and relatively rapid decline. However, the magnitude of the response is less pronounced, reaching only about 9.8 basis points at its maximum, and becoming statistically insignificant around the fifth month. This suggests that its explanatory power is limited. 

The Hungarian geopolitical risk index exhibits a statistically insignificant effect, as indicated by the confidence interval in Figure 7. Therefore, we cannot reliably conclude that geopolitical risk has a significant impact on the Hungarian CDS spread. 

These results support the notion that our SFSI index contains structurally meaningful forward‐looking information capable of producing prolonged effects on the CDS spread beyond short‐term fluctuations. 

The newly constructed sentiment index can be particularly valuable for early forecasting and supporting decision making, as it provides important information that can be used for medium‐term risk assessments and strategic decisions. 

#### **FORECAST ERROR VARIANCE DECOMPOSITION** 

FEVD decomposes the forecast error variance of each variable in a VAR system into proportions attributable to shocks from each variable. This allows us to quantify the relative importance of each variable in explaining the forecast uncertainty of others, over short and long time horizons. FEVD is especially helpful for identifying the main drivers within a system of interrelated time series. 

The FEVD analysis shows how much variance in the forecast error of the CDS spread can be attributed to each index over different time horizons. Initially, the variance of the CDS spread can be explained by its own past values. However, over time, the explanatory power of the CDS spread decreases and converges to 30 % in the long term. 

Meanwhile, the sentiment index shows a notable and steady increase in its explanatory power. It begins by contributing 12% to the forecast error variance, then steadily increases, reaching 40% by the fifth month and converging to 60% in the long term. This growing contribution suggests that the sentiment index increasingly captures the underlying dynamics of the CDS spread. 

**Figure 8 The dynamics of the sentiment‐based financial stress index (SFSI) and the variables included in the VAR system** 





<!-- Start of picture text -->
Source: MNB.<br><!-- End of picture text -->

These results underscore the persistent and growing importance of the sentiment index, highlighting its ability to capture the underlying dynamics of CDS spread compared to the existing indicators. 

MNB WORKING PAPERS 3 • 2026 **21** 

MAGYAR NEMZETI BANK 

#### **SPILLOVER INDEX** 

The Diebold–Yilmaz spillover index (see Diebold & Yilmaz, 2012) provides a comprehensive measure of how shocks propagate across variables based on FEVD from vector autoregressive models. The total spillover index captures the overall extent of inter‐ connectedness and the transmission of shocks across all variables simultaneously. It is computed by summing all off‐diagonal elements of the forecast error variance decomposition matrix—which represent spillovers transmitted between variables—and expressing this sum as a proportion of the total forecast error variance in the system. The directional spillover, on the other hand, serves to identify how variance spillovers affect individual variables. In our case, we are interested in how different variables—such as the FISS, the Economic Policy Uncertainty (EPU) index, or the Geopolitical Risk (GPR) index—impact CDS spreads, which can be analyzed by summing the individual directional spillover effects targeting the CDS variable. The index was originally developed to capture geographical spillovers, but as Varga & Szendrei, 2025 highlights, the index can extend to interconnected markets, where turbulence in one market can cascade into others. 

|**Table 3**<br>**Direct connectedness to C**<br>Variables<br>|**DS spread acros**<br>h=1<br>|**s diferent variabl**<br>h=2<br>|**es and forecast h**<br>h=3<br>|**orizons**<br>h=6<br>|h=12<br>|
|---|---|---|---|---|---|
|FISS|19.95|22.33|24.56|30.36|38.35|
|SFSI|13.00|22.70|31.32|48.54|61.96|
|EPU EU|2.59|3.12|3.63|4.90|6.49|
|GPRI HU|0.25|0.75|1.02|1.33|1.49|
|SFSI+EPU+GPRI|15.90|26.79|35.57|51.28|62.56|
|FISS+EPU+GPRI|23.57|28.54|32.46|40.05|46.83|
|SFSI+FISS|24.45|33.99|41.91|56.67|67.21|
|SFSI+FISS+EPU+GPRI<br>_Source:_ MNB.|27.31|37.32|44.91|57.72|66.13|



The results ⁸ based on the full sample are presented in the Table 3 for different forecast horizons (h = 1, 2, 3, 6, and 12). We estimated separate VAR models for variables pairwise with the CDS spread, as well as for selected multivariate combinations. When comparing the FISS and the SFSI, clear differences emerge in their spillover behavior across horizons. At the very short‐ term horizon (h = 1), the FISS appears to transmit somewhat stronger spillovers to CDS spreads, suggesting that it may be a slightly more responsive to immediate market conditions or short‐term financial instability. However, by h = 2, this difference diminishes, and from the medium term onward (h ≥3), the SFSI becomes the dominant spillover source. This pattern suggests that, while the FISS may capture rapid shifts in financial sentiment, the SFSI has greater explanatory power for CDS spread dynamics over longer horizons, likely due to its more direct relationship to turbulences in public finances. 

Therefore, the combined use of the FISS and the SFSI offers a more robust representation of financial stress, as they capture partly distinct dimensions of stress across different time horizons. The FISS responds a slightly more extent to short‐term fluctuations, whereas the SFSI reflects more persistent and systemic forms of stress, making it more informative over longer horizons. 

As shown in Table 3, the spillover effects of the EPU and the GPRC remain consistently weak across all forecast horizons. 

Analyzing directional spillovers from a time‐varying perspective provides deeper insight into the evolving structure of interac‐ tions within the financial system. The dynamic spillover measure is particularly well‐suited for assessing whether a financial stress index accurately captures periods of systemic stress. By monitoring these changing transmission patterns, it effectively distinguishes true stress episodes from periods of relatively stable conditions. In our analysis, we applied a rolling window es‐ timation using a 60‐month (i.e., 5‐year) window, re‐estimating the VAR(1) model and the corresponding Generalized Forecast Error Variance Decompositions (GFEVD) at each step. 

> ⁸ To estimate different spillover and connectedness measures we use BINH PHAM (2025). Diebold and Yilmaz (2009, 2012,2014) Spillover Index (https://github.com/binhpham79/DYIndex) MatLab Library 

**22** MNB WORKING PAPERS 3 • 2026 

PERFORMANCE OF THE SFSI INDEX 



<!-- Start of picture text -->
Figure 9<br>Spillover to CDS spread at different forecast horizons<br><!-- End of picture text -->

_Source:_ MNB. 

Directional spillovers to sovereign CDS spreads were calculated on four different models and across forecast horizons of h=1, 3, 6, 12. As in the full‐sample analysis, both pairwise and multivariate model specifications were examined. The first model includes only the SFSI, the second includes the FISS, the third combines both SFSI and FISS, while the fourth incorporates SFSI, FISS, as well as EPU and GPR indices. 

The results indicate that at the short‐term horizon (h=1), different models display relatively similar dynamics in the early part of the sample, with a gradually declining trend in spillovers. This flattening and decline may be attributed to the notable decrease in CDS trading volume and transaction numbers observed since 2017, which may have been influenced by the 2012 regulation. This trend is distrupted during the onset of the COVID‐19 pandemic, which is associated with a period of elevated variability. During this time of heightened risk, all models exhibit sharp increases in the magnitude of directional spillovers, indicating an immediate and significant effect on CDS spreads. 

At medium and long‐term horizons, the results show broadly similar patterns. Across all forecast horizons, the models remain significant contributors to the transmission of financial stress to CDS spreads, indicating persistent and robust spillover effects. 

The results suggest that the SFSI plays an increasingly important role in explaining the spillover of financial stress to CDS spreads, particularly over longer forecast horizons. This persistent effect may be related to the fact that the SFSI is based on news senti‐ ment, where the impact of events tends to remain due to prolonged media attention and delayed policy responses. In contrast, the FISS effectively captures short‐term market sensitivities and reacts more sharply to immediate fluctuations, but its influence diminishes over longer horizons. While the SFSI alone serves as a robust indicator of systemic stress transmission, its combined use with the FISS further strengthens the model’s explanatory power. These results confirm that the two indicators, when used together, provide a more comprehensive and nuanced understanding of the dynamic stress transmission mechanisms within the financial system. 

MNB WORKING PAPERS 3 • 2026 **23** 

MAGYAR NEMZETI BANK 

While directional spillover indices provide valuable insights into the transmission of shocks between individual variables, it is nevertheless useful to also consider the total spillover index, which offers a complementary, system‐wide perspective. This index captures the overall degree of interconnectedness and shock transmission within the system, reflecting the intensity of spillovers across all variables included in the VAR model. 

**Figure 10 Total spillover effects at short and medium term horizons (h=1, h=6 month(s))** 





<!-- Start of picture text -->
Source: MNB.<br><!-- End of picture text -->

In the context of this study, where CDS spreads are modeled alongside systemic financial stress (SFSI), financial instability sen‐ timent (FISS), economic policy uncertainty (EPU), and geopolitical risk (GPR), the total spillover index enables us to assess the overall degree of interconnectedness among these risk and uncertainty indicators. Figure 10 displays the spillover dynamics for forecast horizons of h=1 and h=6. At short‐term horizon (h=1), the system appears relatively stable: both the FISS and SFSI indices contribute to the CDS spread to a similar extent, while the impact of the EPU and GPR indices remains negligible. At the h=6 horizon, the SFSI emerges as the main transmitter of shocks within the system, particularly towards both the FISS and CDS spreads. This suggests that the sentiment‐based financial stress index becomes the dominant source of risk transmission over a six‐month period, exerting a sustained and significant influence on FISS and sovereign credit risk. 

**24** MNB WORKING PAPERS 3 • 2026 

CONCLUSION 

# **5 Conclusion** 

This paper introduces a sentiment‐based financial stress index for Hungary from January 2005 to December 2020. The index builds on optimized keyword searches from two Hungarian online news portals combining two different sets of pre‐defined terms, one capturing terms related to elements of financial system and the other to those of crisis or uncertainty. Instead of relying on raw term counts, to each article previously identified as relevant is assigned a score reflecting the richness of term co‐occurrences, through which the dominance of a crisis‐ or uncertainity‐related narrative within the text is intended to be captured. 

The SFSI successfully gauges the episodes of financial turbulence in the Hungarian economy during the fairly long period of observation. These distinguished periods are associated with financial turmoils before 2008 September (beginning of the sub‐ prime crisis coupled with bankruptcies in the US) peak stress periods during GFC (2009‐2010) and the emerging sovereign debt crisis in Europe (2011‐2014). As a consequence of enduring financial vulnerabilities, Hungary was particularly hit hard by the GFC compared to other Central and Eastern European EU countries, causing recurring episodes of financial distress. Events after 2014 like the Brexit voting, or the outbreak of Covid‐19 pandemic also produced local peaks in the index. 

More importantly, the overall dynamics of SFSI closely mimics that of the FISS which latter is considered to be one of the most sophisticated financial stress index for Hungary complied so far. The FISS has the advantage of being able to capture the complex interconnectedness of financial markets. It aims to quantify the individual importance of a large number of indicators by a weighting procedure linked to their historical importance measured by the explained variance in the financial system. 

We show that our index is useful for financial stability analysis. In evaluating the performance of our news‐based stress indices, Granger causality tests showed that SFSI tends to lead the CDS spreads time series. According to impulse response analysis, there is a steadily increasing response of CDS spreads up to the 6th month to shock in SFSI which is also fairly persistent in nature. When generalized forecast error variance decomposition (GFEVD) was performed using VAR models with all variables included, the SFSI contributed clearly the most to the variation in CDS spreads. 

We also use the Diebold and Yilmaz’s connectedness approach to investigate the spillover of financial stress into CDS spreads over time. A relatively fast pace of impact is expected since CDS spreads are partly driven by speculative trading that also reacts quickly to changing sentiment. Our findings suggest that while FISS is superior for short‐term forecast horizon (up to three months), SFSI fares reasonably well in the long‐term forecast. 

Given our empirical findings, we conjecture that the novel news‐based sentiment stress index can be deployed to monitor financial stability in the Hungarian economy as it provides reliable and timely information on the magnitude of financial stress. Such sentiment‐based metrics can complement traditional stress indicators based on macrofinancial variables like the FISS for Hungary. 

Moreover, one of the key advantages of the index developed in this study is that it can be produced at any frequency and in near real time, offering a clear advantage over existing indices, which are often released only with significant delays. 

Despite the promising results of our proposed index to measure financial stress for Hungary, there are notable limitations that need to be addressed. First, although a vast new corpus is involved in the analysis for a long period, the number of sources for extracting sentiments from textual data is limited. Second, although we showed that Economic Policy Uncertainty for the EU or Geopolitical Risk index for Hungary does not contain information on the contemporary or future movement of the SFSI, it would be nice to know what international stress/uncertainty/risk indicators influence the dynamics of our sentiment‐based index (decomposing the variance of CDS spreads into global, regional and country‐specific components, there is a strong global factor underlying credit risk spreads, see Kocsis & Nagy, 2011). We advise for future research the study of the interaction between different indices of geopolitical, policy uncertainty, or volatility indices and sentiment‐based financial stress index. In addition, in future research, further analysis could be conducted to explore the direction of causality between our sentiment 

MNB WORKING PAPERS 3 • 2026 **25** 

MAGYAR NEMZETI BANK 

index and indicators of financial market risk in more detail. Moreover, future work could apply non‐parametric methods on higher‐frequency datasets, especially during crisis periods, in order to capture potentially nonlinear dynamics and short‐term stress propagation mechanisms that may remain hidden in analyses based on lower‐frequency data. 

**26** MNB WORKING PAPERS 3 • 2026 

References 

# **References** 

- Aguilar, P., Ghirelli, C., Pacce, M., & Urtasun, A. (2021). Can news help measure economic sentiment? an application in covid‐19 times. _Economics Letters_ , _199_ , 109730. doi: https://doi.org/10.1016/j.econlet.2021.109730 

- Ahir, H. (2023, 10). _Financial Stress and Economic Activity: Evidence from a New Worldwide Index_ (Vol. 2023; Tech. Rep. No. 217). International Monetary Fund (IMF). doi: http://doi.org/10.5089/9798400257636.001 

- Baker, M., & Wurgler, J. (2007, June). Investor sentiment in the stock market. _Journal of Economic Perspectives_ , _21_ (2), 129–152. doi: https://doi.org/10.1257/jep.21.2.129 

- Baker, S. R., Bloom, N., & Davis, S. J. (2016). Measuring economic policy uncertainty. _The Quarterly Journal of Economics_ , _131_ (4), 1593‐1636. doi: https://doi.org/10.1093/qje/qjw024 

- Bernal, Á. I. M., & Pedraz, C. G. (2020, Jul). _Sentiment analysis of the spanish financial stability report_ (Working Papers No. 2011). Banco de España. Retrieved from https://ideas.repec.org/p/bde/wpaper/2011e.html 

- Blei, D., Ng, A., & Jordan, M. (2001). Latent dirichlet allocation. In T. Dietterich, S. Becker, & Z. Ghahramani (Eds.), _Advances in neural information processing systems_ (Vol. 14). MIT Press. Retrieved from https://proceedings.neurips.cc/ paper_files/paper/2001/file/296472c9542ad4d4788d543508116cbc-Paper.pdf 

- Borovkova, S., Garmaev, E., & Lammers, P. (2017, 01). Sensr: A sentiment‐based systemic risk indicator. _SSRN Electronic Journal_ . doi: https://doi.org/10.2139/ssrn.2951036 

- Caldara, D., & Iacoviello, M. (2022, April). Measuring geopolitical risk. _American Economic Review_ , _112_ (4), 1194‐1225. doi: https://doi.org/10.1257/aer.20191823 

- Cevik, E. I., Dibooglu, S., & Kutan, A. M. (2013). Measuring financial stress in transition economies. _Journal of Financial Stability_ , _9_ (4), 597‐611. (Re‐examining the role of the state in the financial sector) doi: https://doi.org/10.1016/j.jfs.2012.10.001 

- Correa, R., Garud, K., Londono, J. M., & Mislang, N. (2020, 04). Sentiment in central banks’ financial stability reports. _Review of Finance_ , _25_ (1), 85‐120. doi: https://doi.org/10.1093/rof/rfaa014 

- Diebold, F. X., & Yilmaz, K. (2012). Better to give than to receive: Predictive directional measurement of volatility spillovers. _International Journal of Forecasting_ , _28_ (1), 57‐66. (Special Section 1: The Predictability of Financial Markets Special Section 2: Credit Risk Modelling and Forecasting) doi: https://doi.org/10.1016/j.ijforecast.2011.02.006 

- Dim, C., Koerner, K., Wolski, M., & Zwart, S. (2022). _Hot off the press: News‐implied sovereign default risk_ (EIB Working Papers No. 2022/06). European Investment Bank (EIB). doi: https://doi.org/10.2867/661002 

- Engle, R. F., & Campos‐Martins, S. (2023). What are the events that shake our world? measuring and hedging global covol. _Journal of Financial Economics_ , _147_ (1), 221‐242. doi: https://doi.org/10.1016/j.jfineco.2022.09.009 

- European Commission. (2025). _The joint harmonised eu programme of business and consumer surveys ‐ user guide._ European Commission. Retrieved from https://ec.europa.eu/economy_finance/db_indicators/surveys/ documents/methodological_guidelines/bcs_user_guide.pdf 

- Fernandez, R., Palma Guizar, B., & Rho, C. (2021). A sentiment‐based risk indicator for the mexican financial sector. _Latin American Journal of Central Banking (previously Monetaria)_ , _2_ (3). doi: https://doi.org/10.1016/j.latcb.2021.100036 

- García, D. (2013). Sentiment during recessions. _The Journal of Finance_ , _68_ (3), 1267‐1300. Retrieved from https://doi .org/10.1111/jofi.12027 

- Hakkio, C. S., & Keeton, W. R. (2009, None). Financial stress: what is it, how can it be measured, and why does it matter? _Economic Review_ , _94_ (Q II), 5‐50. Retrieved from https://ideas.repec.org/a/fip/fedker/y2009iqiip5 -50nv.94no.2.html 

- Hollo, D., Kremer, M., & Lo Duca, M. (2012). _Ciss ‐ a composite indicator of systemic stress in the financial system_ (Working Paper No. 1426). European Central Bank. doi: https://doi.org/10.2139/ssrn.2018792 

- Honnibal, M., Montani, I., Van Landeghem, S., & Boyd, A. (2020). _spaCy: Industrial‐strength Natural Language Processing in Python._ doi: https://doi.org/10.5281/zenodo.1212303 

- Illing, M., & Liu, Y. (2006). Measuring financial stress in a developed country: An application to canada. _Journal of Financial Stability_ , _2_ (3), 243‐265. doi: https://doi.org/10.1016/j.jfs.2006.06.002 

- Kalamara, E., Turrell, A., Redl, C., Kapetanios, G., & Kapadia, S. (2022). Making text count: Economic forecasting using newspaper text. _Journal of Applied Econometrics_ , _37_ (5), 896‐919. doi: https://doi.org/10.1002/jae.2907 

MNB WORKING PAPERS 3 • 2026 **27** 

MAGYAR NEMZETI BANK 

- Kanelis, D., & Siklos, P. L. (2025). The ecb press conference statement: deriving a new sentiment indicator for the euro area. _International Journal of Finance & Economics_ , _30_ (1), 652‐664. doi: https://doi.org/10.1002/ijfe.2940 

- Kocsis, Z., & Nagy, D. (2011, October). Variance decomposition of sovereign cds spreads. _MNB Bulletin (discontinued)_ , _6_ (3), 36‐50. Retrieved from https://ideas.repec.org/a/mnb/bullet/v6y2011i3p36-50.html 

- Krishnamurthy, A., & Li, W. (2025). Dissecting mechanisms of financial crises: Intermediation and sentiment. _Journal of Political Economy_ , _133_ (3), 935‐985. doi: https://doi.org/10.1086/733423 

- Maghyereh, A., & Abdoh, H. (2022). Global financial crisis versus covid‐19: Evidence from sentiment analysis. _International Finance_ , _25_ (2), 218‐248. doi: https://doi.org/10.1111/infi.12412 

- Orosz, G., Szabó, G., Berkecz, P., Szántó, Z., & Farkas, R. (2023). Advancing Hungarian Text Processing with HuSpaCy: Efficient and Accurate NLP Pipelines. In K. Ekštein, F. Pártl, & M. Konopík (Eds.), _Text, Speech, and Dialogue_ (pp. 58–69). Cham: Springer Nature Switzerland. 

- Pesaran, H. H., & Shin, Y. (1998). Generalized impulse response analysis in linear multivariate models. _Economics Letters_ , _58_ (1), 17‐29. doi: https://doi.org/10.1016/S0165‐1765(97)00214‐0 

- Püttmann, L. (2018). Patterns of panic: Financial crisis language in historical newspapers. _SSRN Electronic Journal_ . doi: https://doi.org/10.2139/ssrn.3156287 

- Ristolainen, K., Roukka, T., & Nyberg, H. (2024). A thousand words tell more than just numbers: Financial crises and historical headlines. _Journal of Financial Stability_ , _70_ , 101209. doi: https://doi.org/10.1016/j.jfs.2023.101209 

- Stolbov, M., & Shchepeleva, M. (2025). A sentiment‐based financial stress index for russia. _Borsa Istanbul Review_ , _25_ (2), 350‐359. doi: https://doi.org/10.1016/j.bir.2025.01.007 

- Stolbov, M., Shchepeleva, M., & Karminsky, A. (2022). When central bank research meets google search: A sentiment index of global financial stress. _Journal of International Financial Markets, Institutions and Money_ , _81_ (C). Retrieved from https://doi.org/10.1016/j.intfin.2022.101692 

- Szendrei, T., & Varga, K. (2017). _Fiss ‐ a factor based index of systemic stress in the financial system_ (MNB Working Papers No. 2017/9). Magyar Nemzeti Bank (Central Bank of Hungary). Retrieved from https://ideas.repec.org/p/mnb/ wpaper/2017-9.html 

- Szendrei, T., & Varga, K. (2020, March). Fiss ‐ a factor‐based index of systemic stress in the financial system. _Russian Journal of Money and Finance_ , _79_ (1), 3‐34. doi: https://doi.org/10.31477/rjmf.202001.03 

- Toda, H. Y., & Yamamoto, T. (1995). Statistical inference in vector autoregressions with possibly integrated processes. _Journal of Econometrics_ , _66_ (1‐2), 225‐250. doi: https://doi.org/10.1016/0304‐4076(94)01616‐8 

- Varga, K., & Szendrei, T. (2025, January). Non‐stationary financial risk factors and macroeconomic vulnerability for the uk. _International Review of Financial Analysis_ , _97_ , 103866. doi: https://doi.org/10.1016/j.irfa.2024.103866 

**28** MNB WORKING PAPERS 3 • 2026 

# **Appendix A Data** 

**Figure A.1 Evolution of average length of the filtered articles** 



Measured by the number of characters, including whitespaces. _Source:_ MNB. 

MNB WORKING PAPERS 3 • 2026 **29** 

# **Appendix B Empirical analysis** 

#### **B.1 STATIONARITY TESTS** 

|**Table A.1**<br>**ADF and KPSS test sta**|**tstcs for difer**<br>|**ent variables**<br>||||||
|---|---|---|---|---|---|---|---|
|Variables|ADF t<br>|‐statstc<br>|PP t‐<br>|statstc<br>|KPSS<br>|LM‐stat<br>|Order of In‐<br>tegraton|
||level|1st dif|level|1st dif|level|1st dif||
|CDS spread|‐2.06|‐11.32***|‐2.07|‐11.43***|0.37|0.12|I(1)|
|SFSI|‐2.62*|‐11.04***|‐2.33|‐15.63***|0.4|0.17|I(1)|
|FISS|‐2.52|‐11.53***|‐2.82|‐11.64***|0.82|0.04|I(1)|
|EPU EU|‐2.14|‐13.19***|‐4.24***||1.38|0.26|I(1)|
|GPRI HU<br>*** p<0.01, ** p<0.05, * p<<br>_Source:_ MNB.|‐4.71***<br>0.1||‐12.16||0.94|0.18|I(1)|



#### **B.2 OPTIMAL LAG LENGTH** 

|**Table A.2**<br>**Optmal lag len**|**gth for pairwise variables**<br>|**based on Schwarz and Han**<br>|**nan‐Quinn Informaton Criteria**<br>|
|---|---|---|---|
||Variables|Schwarz Informaton Criterion|Hannan‐Quinn Informaton Criterion|
||CDS spread ‐ SFSI|1|1|
||CDS spread ‐ FISS|1|3|
||CDS spread ‐ EPU EU|1|5|
||CDS spread ‐ GPRI HU|1|2|
|_Source:_ MNB.||||



#### **B.3 VAR SPECIFICATIONS** 

###### **Table A.3** 

**Optimal lag length for VAR model (CDS Spread, SFSI, FISS, EPU EU, GPRI HU) based on Schwarz and Hannan‐Quinn Infor‐ mation Criteria** 



<!-- Start of picture text -->
Schwarz Information Criterion Hannan‐Quinn Information Criterion<br>1 1<br>Source: MNB.<br><!-- End of picture text -->

**30** MNB WORKING PAPERS 3 • 2026 

APPENDIX B EMPIRICAL ANALYSIS 

###### **Table A.4** 

###### **VAR(1) specifications** 

|Variables|C|CDS(−1)|SFSI(−1)|FISS(−1)|EPU(−1)|GPRI(−1)|Durbin‐Watson<br>statstcs|
|---|---|---|---|---|---|---|---|
|CDS|‐16.3293*|0.7967***|116.0001***|0.1961|0.0376|‐79.8728|1.74|
|SFSI|0.0808***|0.0001|0.9523***|‐0.0915|‐0.0002*|‐0.3677|2.03|
|FISS|0.0463***|‐0.0002***|0.2044***|0.7883***|‐0.0001|‐0.3453**|1.63|
|EPU|71.0161***|0.0064|56.9808*|‐137.858***|0.7367***|‐98.5545|2.20|
|GPRI|0.0145**|0.0001|‐0.0249|0.0031|0.0001**|0.1722**|2.07|



*** p<0.01, ** p<0.05, * p<0.1 _Source:_ MNB. 

###### **Figure A.2 Inverse roots of AR characteristics polynomial** 



_Source:_ MNB. 

MNB WORKING PAPERS 3 • 2026 **31** 

# **Appendix C Technical appendix** 

#### **C.1 THE TODA–YAMAMOTO PROCEDURE TESTING GRANGER CAUSALITY** 

The Toda & Yamamoto, 1995 methodology provides a robust framework for testing Granger causality in vector autoregres‐ sive (VAR) models when the time‐series variables may be non‐stationary or cointegrated. The procedure ensures valid Wald inference by estimating an augmented VAR in levels. The steps of the procedure are as follows: 

##### **1. Determine the maximal order of integration** 

Identify 𝑑 max, the highest plausible order of integration among variables (usually via ADF, PP, or KPSS tests). 

##### **2. Select the optimal lag length of the VAR(** 𝑘 **)** 

Estimate a standard VAR in levels and select the optimal lag length 𝑘 using information criteria (AIC, BIC, HQ). Toda & Yamamoto, 1995 show that a lag‐selection procedure commonly used for stationary VAR models remains valid even when the underlying variables are non‐stationary or cointegrated, as long as 𝑘≥𝑑 , where 𝑘 denotes the order of the VAR model and 𝑑 the (maximal) order of integration of the variables. 

##### **3. Estimate an augmented VAR of order** 

Estimate the VAR model in levels with additional lags equal to the maximal integration order: 

VAR( 𝑘+ 𝑑 max ) 

The purpose of the extra lags is to correct the asymptotic distribution of the Wald statistics. 

##### **4. Conduct Wald tests on the coefficients of the first** 𝑘 **lags** 

To test Granger causality, restrictions are imposed exclusively on the coefficients of the first 𝑘 lag terms. 

For example, to assess whether 𝑋 Granger‐causes 𝑌 , the null hypothesis is 



The coefficients on the additional 𝑑 max lags (from 𝑘+ 1 to 𝑘+ 𝑑 max) are not part of the hypothesis test. 

Toda and Yamamoto demonstrate that, with the augmented specification, the Wald statistics follow their conventional chi‐ square distribution. 

#### **C.2 GENERALIZED SPILLOVER AND CONNECTEDNESS MEASURE** 

Diebold & Yilmaz, 2012 examine volatility spillovers across financial markets and introduce the _generalized spillover framework_ , which provides an ordering‐invariant, forecast–error–based, and directionally decomposable measure of interconnectedness. The approach relies on decomposing the ℎ ‐step‐ahead forecast error variance of a VAR system into components attributable to shocks in each variable. 

**32** MNB WORKING PAPERS 3 • 2026 

APPENDIX C TECHNICAL APPENDIX 

##### **VAR Model** 

Let 𝑌𝑡 = (𝑦1𝑡, … , 𝑦𝑁𝑡)<sup>′</sup> follow an 𝑁 ‐dimensional, covariance stationary VAR( 𝑝 ): 



where Φ𝑖 are the autoregressive coefficient matrices and Σ is the covariance matrix. 

##### **MA(** ∞ **) Representation** 

The VAR model has a moving‐average representation 



where the moving average coefficients Ψ𝑘 describe the dynamics of the system. They provide the basis for dynamic analyses, most notably impulse‐response functions and forecast error variance decompositions. 

Using this representation, the ℎ ‐step‐ahead forecast error of the 𝑖 ‐th variable is 



and its variance is 



where 𝑒𝑖 is the 𝑖 ‐th unit vector. This identifies the total uncertainty in forecasting 𝑦𝑖,𝑡+ℎ . 

##### **Generalized FEVD (GFEVD)** 

The generalized forecast error variance decomposition measures proposed by Pesaran & Shin, 1998 is invariant to the ordering of variables, where the contribution of shocks to variable 𝑗 to the ℎ ‐step forecast error variance of variable 𝑖 is: 



where 𝜎𝑗𝑗 is the variance of the 𝑗 ‐th innovation. 

Conceptually, 𝜃𝑖𝑗<sup>𝑔(ℎ)captures the share of𝑦</sup> 𝑖<sup>’s forecast error variance that is statistically attributable to shocks originating in𝑦</sup> 𝑗<sup>,</sup> independent of variable ordering. 

##### **Normalization** 

In the generalized framework, the row sums of 𝜃𝑖𝑗<sup>𝑔(ℎ)do not naturally sum to one.It is a common practice to normalize each</sup> row to obtain a proper variance‐share interpretation: 



The normalized quantities ̃ 𝜃𝑖𝑗<sup>𝑔(ℎ)can be interpreted as the fraction of the𝑖‐th variable’s forecast error variance caused by shocks</sup> to the 𝑗 ‐th variable. 

MNB WORKING PAPERS 3 • 2026 **33** 

MAGYAR NEMZETI BANK 

##### **Directional Spillovers** 

The normalized GFEVD allows for directional decomposition. 

1. Spillovers received by 𝑖 from all other markets (“from others”): 



2. Spillovers transmitted by 𝑖 to all other markets (“to others”): 



Directional spillovers provide more detailed information on how individual variables transmit and receive shocks from others. 

##### **Total Spillover Index** 

System‐wide connectedness is summarized by the total spillover index: 



which expresses the percentage of overall forecast error variance that is due to cross‐variables. This provides a compact and time‐varying measure of the extent to which shocks are transmitted in the system. 

**34** MNB WORKING PAPERS 3 • 2026 

**MNB Working Papers 2026/3** 

**Sentiment‐based Financial Stress Index for Hungary Budapest, July 2026** 



## mnb.hu 

©MAGYAR NEMZETI BANK 

1054 BUDAPEST, SZABADSÁG TÉR 8‐9. 

