---
title: Smith_Forecasting Investment and House Prices in NZ using Dynamic Factor Models_2025
type: paper
source_pdf: raw/papers/Smith_Forecasting Investment and House Prices in NZ using Dynamic Factor Models_2025.pdf
converted: 2026-08-18
---





**April 2025 –  AN2025-02** 

# **Analytical Note** 

## **Forecasting Investment and House Prices in New Zealand using . Dynamic Factor Models** 

**Tyler Smith*, Trent Lockyer** 

**Reserve Bank of New Zealand** **_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models_** 

ISSN 2230-5505 

The Analytical Note series encompasses a range of types of background papers prepared by Reserve Bank staff. Unless otherwise stated, views expressed are those of the authors, and do not necessarily represent the views of the Reserve Bank. 

Reserve Bank of New Zealand PO Box 2498 Wellington NEW ZEALAND 

www.rbnz.govt.nz 

* Tyler Smith is no longer employed at the Reserve Bank of New Zealand – Te Pūtea Matua. This _Note_ does not represent the views of his current employers. 

Ref #22330012 v1.1 

1 

##### **Disclaimer** 

We produce a variety of publications and research about monetary policy, financial stability and related economic and financial issues. Most are available without charge as part of our public information service. 

We have made every effort to ensure that information published in this paper is accurate and up to date. However, we take no responsibility and accept no liability arising from: 

- errors or omissions 

- the way in which any information is interpreted 

- reliance upon any material. 

We are not responsible for the contents or reliability of any linked websites and do not necessarily endorse the views expressed within them. 

<u>Privacy Policy - Reserve Bank of New Zealand - Te Pūtea Matua (rbnz.govt.nz)</u> 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

1 

2 

##### **Key Findings** 

- We develop dynamic factor models to forecast three important economic variables: business investment, residential investment, and house prices. Accurate and timely forecasts of these variables are important for appropriately setting monetary policy. 

- Dynamic factor models provide a systematic framework for incorporating various types of economic data into the policy process and provide a robust complement to human judgement in the forecast process. These models are particularly useful for extracting information from large datasets with both official statistics and high frequency New Zealand data. 

- We find these models are a useful addition to the suite of tools we use to forecast the New Zealand economy, consistently outperforming simple benchmarks. Their forecast performance is broadly comparable to our Monetary Policy Statement _(MPS)_ forecasts, although their performance was worse during the COVID-19 pandemic when data volatility was extremely high. 

- We decompose our dynamic factor model forecasts to show which data sources are driving changes in the forecasts. This can inform judgement on how much signal to take from different data types and support communication to the Monetary Policy Committee (MPC) and the public. 

### **1. Introduction**<sup>**1**</sup> 

Accurately assessing the current and future state of the economy is crucial to formulating monetary policy effectively. At the Reserve Bank of New Zealand (RBNZ), the MPC’s operational objective is to maintain future annual inflation between 1 and 3 percent over the medium term, with a focus on keeping future inflation near the 2 percent mid-point. This _Note_ constructs forecasting models for three macroeconomic variables, namely business investment, residential investment, and house prices. These models can handle large datasets – including high-frequency indicators such as credit data – and identify which data series are most relevant for forecasting the variable of interest. We assess whether forecasts from these models outperform our historical forecasts for these variables. 

Accurate economic forecasting is made more difficult by the lagged and infrequent release of most national statistics. In New Zealand, key macroeconomic variables including gross domestic product (GDP) and investment, are only available quarterly and with a delay of around 3 months after the quarter has finished. Furthermore, this data can be substantially revised in quarters after it is first released, clouding its initial usefulness to policymakers. Over time, general improvements in technology have facilitated the development of new sources of data, often of a high frequency, which can assist in monitoring the state of the economy in real time and forecasting future changes. However, higher volumes of data also lead to new challenges; most significantly, the need to discern between signal and noise across the many data sources, to collate a consolidated and consistent view on the state of the economy. 

____________ 

> 1  The authors would like to thank colleagues across the RBNZ for their feedback on and support for this work. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

2 

3 

To address this challenge, we use an approach which has become common in the forecasting literature by constructing dynamic factor models (DFMs) to forecast business investment, residential investment, and house prices. Business investment and residential investment comprise around 16% and 6% of GDP, respectively. House prices are important for economic activity as a major component of household wealth in New Zealand, and as a key determinant of residential investment. As DFMs can handle large datasets, we can include a wider range of indicators to predict these variables than most other forecasting approaches. We compare the forecast performance of the DFMs to a standard benchmark model and the historically published _MPS_ forecasts to assess whether these models can add value to our existing forecasting approaches. 

Our results suggest these models can be a useful addition to the suite of tools we use for forecasting the New Zealand economy, with forecast performance consistently superior to a standard benchmark model, and broadly comparable to our _MPS_ forecasts outside of periods of extreme economic volatility. The ability to decompose the DFM forecasts enables us to understand which data series is driving the forecasts and supports communication of the forecasts to policymakers. 

The rest of this _Note_ is organised as follows. Section 2 reviews related literature. Section 3 outlines the data we use, and Section 4 sets out the methodology we use. Section 5 details key findings. Section 6 discusses robustness of our results. Section 7 concludes. 

### **2. Related Literature** 

Our work touches on two significant strands of academic literature. The first is the use of DFMs for forecasting. Factor models have long featured in the econometric and statistical literature. However, only recently have these models begun to be applied to forecasting problems with big data. Giannone et al. (2008) illustrates how DFMs are useful for nowcasting and understanding the macroeconomy in real-time. In a similar vein, Bok et al. (2018) detail the work of the New York Fed to forecast real GDP growth in the United States, using a DFM to handle a large dataset in an internally consistent way. The results from this model are regularly published on the New York Federal Reserve website.<sup>2</sup> Another example is provided by Hartigan and Rosewall (2024) of the Reserve Bank of Australia, who use a DFM to forecast real GDP growth, finding the model performs best during the COVID-19 pandemic period – highlighting the benefits of using this model framework even during periods of heightened uncertainty. Our work is closely based on the model of Bok et al. (2018). 

The literature using DFMs in economic forecasting in New Zealand is relatively sparse. The Reserve Bank uses a dynamic factor model to measure core inflation, identifying tradable and non-tradable components of inflation (Kirker, 2010; Price, 2013).<sup>3</sup> <u>Matheson (2006) provides another example of</u> using this methodology, for the purpose of forecasting GDP, consumer price inflation, interest rates and the exchange rate. This work suggests the out-of-sample forecasts from factor models outperformed the RBNZ’s forecasts at the time over longer horizons – one year and beyond. Our work builds on this work with a specific focus on incorporating more disaggregated variables and new data sources, which have been introduced since 2005. Closely related to our work, Bayarmagnai (2025) uses the DFM framework to nowcast real GDP growth in New Zealand. Bayarmagnai finds that while the DFM does not outperform the Reserve Bank’s nowcast in a 

____________ 

> 2 <u>newyorkfed.org/research/policy/nowcast#/overview</u> 

> 3 <u>rbnz.govt.nz/statistics/series/economic-indicators/prices</u> 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

3 

4 

pseudo real-time forecasting exercise, it nonetheless provides valuable insights that improve overall forecast accuracy. 

The second strand of literature our work relates to is the use of ‘novel’ or less frequently used data sources in macroeconomic forecasting. Data such as credit, financial and surveyed data have become more detailed and available over time. For instance, prior to the Global Financial Crisis (GFC), credit variables had a limited role in how central banks assessed the economic outlook. <u>Bloor et al. (2008) summarises how central banks, including the RBNZ, incorporated credit</u> variables into their monetary policy assessments, finding that central banks generally used credit measures for “corroborating information about demand pressures” (pg. 7), with little formal use in forecasting models. 

Since the GFC, credit variables have played a larger role in central banks’ assessment of the economic outlook, partially due to the increasing granularity of such variables. One example of this is Chen and Ranciere (2019), who explore the ability of credit variables to explain macroeconomic variables. They show that including credit growth alongside other financial variables in a simple model provides significantly better forecasts than the IMF’s World Economic Outlook for more than two thirds of the countries in their sample, including New Zealand. They also find that using information from other countries in forecasting the New Zealand economy improves performance. Work has also shown that in the United States (Albuquerque, Baumann & Seitz, 2016) and Turkey (Ermişoğlu, Akçelik & Oduncu, 2013) there is a significant link between credit data and GDP growth. Similarly, Rünstler et al. (2009) evaluate a range of models for forecasting GDP in ten European countries, incorporating credit and other financial variables. The authors find the best forecasts were provided by factor models, and models which exploited higher frequency monthly data rather than models which only used quarterly data. These findings support our approach of using data sources such as credit information in the DFMs we construct, which is collected at a monthly frequency in New Zealand. 

### **3. Data** 

We forecast three series: the quarterly growth rate of business investment (excluding non-market investment); the quarterly growth rate of residential investment; and the quarterly growth rate of the national house price index (from CoreLogic). All variables are seasonally adjusted. 

To forecast our variables of interest, we require a large dataset of time series variables to use as input variables. The factor model literature dedicates significant attention to how input variables should be selected, and the optimal size of the variable dataset. Some papers find the forecast accuracy of factor models to be sensitive to the data included, which supports including more variables, rather than less, and allowing the DFM to weight variables as it sees fit (see Bai and Ng, <u>2008 for more information). However, using too many variables in a DFM has also been shown to</u> reduce forecast performance in some cases (see Boivin and Ng, 2006). 

To determine how many variables to include in our dataset, we follow Boivin and Ng (2006) and consider the quality of the data being included. This is done according to the following process for each dependent variable: 

**1. Create an extended dataset.** We compile a large number of variables which have been used in past forecasting exercises for the relevant dependent variable or based on our judgement. This dataset includes a mix of quarterly and monthly variables, as well as both aggregated and 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

4 

5 

disaggregated measures (for example, BusinessNZ’s Performance of Manufacturing Index (PMI) as well as the sub-indices for production, new orders and employment). We trim all data to start at January 1995, due to the limited number of series with data available before this point (see Appendix A for further information about our dataset). 

**2. Apply data transformations.** Where appropriate, we make transformations to the data such that the time series are stationary, following  Bok et al. (2018).<sup>4</sup> We standardise variables to have a zero mean and unit variance. Data is seasonally adjusted where relevant. 

**3. Filter out uninformative variables using a hard thresholding approach.** The ability for the DFMs to weight variables by their value in forecasting the dependent variable means these models are largely robust to including uninformative variables. Having said this, all variables in the model must receive a positive, non-zero, weight, and including many uninformative variables may affect the forecast performance of the model. For this reason, we follow a modified version of the approach first outlined by Bai and Ng (2008) and later extended by <u>Hartigan and Rosewall (2024), performing a hard-thresholding approach to remove</u> uninformative variables. To do this, we first regress each variable in the extended dataset and its first four lags on the dependent variable, including a constant term, a dummy variable for the COVID-19 period, and lags of the dependent variable as controls.<sup>5</sup> This is captured in the following regression, where 𝐷𝑉𝑗,𝑡 represents dependent variable 𝑗 in time 𝑡 , and 𝐼𝑉𝑖 represents independent variable 𝑖 (from the extended dataset) in time 𝑡 : 

𝐷𝑉𝑗,𝑡 = 𝛼+ 𝛽1𝐼𝑉𝑖,𝑡 + 𝛽2𝐼𝑉𝑖,𝑡−1 + 𝛽3𝐼𝑉𝑖,𝑡−2 + 𝛽4𝐼𝑉𝑖,𝑡−3 + 𝛽5 𝐼𝑉𝑖,𝑡−4 + 𝛽6𝐶𝑂𝑉𝐼𝐷𝐷𝑢𝑚 + 𝛽7𝐷𝑉𝑗,𝑡−1 + 𝛽8𝐷𝑉𝑗,𝑡−2 + 𝛽9𝐷𝑉𝑗,𝑡−3 + 𝛽10 𝐷𝑉𝑗,𝑡−4 + 𝜖 

Where the independent variables are of a monthly frequency, we use a quarterly average series in this regression. We use the latest vintage of all variables as of August 2024. Where variables do not have historical time series back to Q1 1995, we shorten the data range for the regression accordingly. 

**4.** For each regression, we calculate the heteroskedasticity and autocorrelation consistent (HAC) covariance matrix. Using the HAC matrix, we conduct a Wald test to test for joint linear significance of the coefficients of the independent variable and its four lags (HAC-adjusted versions of 𝛽1, 𝛽2, 𝛽3, 𝛽4, 𝛽5 ). We rank the Wald test statistics for all variables in the extended dataset and retain variables which are significant at the 10% level. The retained variables form the ‘restricted dataset’ we use in the DFM for that dependent variable. As a robustness check, the results from using the full extended dataset for each DFM is discussed in Section 6. 

The number of variables in the restricted datasets for each of the dependent variables are displayed in table 1. The ranked Wald statistics and threshold value for each extended dataset are plotted in Appendix A1. Broadly, the number of variables in each of the restricted dataset matches the number suggested as appropriate in Bai and Ng (2008), Hartigan and Rosewall (2024) and Bayarmagnai (2025). 

____________ 

> 4  Series are transformed either by first differencing or by taking a percentage change. 

> 5  We use a COVID-19 dummy for the period 2020Q2 to 2020Q4, capturing the early pandemic period, where data was the most volatile, and the largest deviations from normal patterns occurred. 

_AN - Forecasting Investment and House Prices in NZ_ 

5 

_using Dynamic Factor Models –_ AN2025-02 

6 

**_Table 1: Dataset sizes_** 

|**Dependent variable**|**Number of variables in**<br>**restricted dataset**|**Percentage of variables**<br>**in extended dataset**|
|---|---|---|
|Business investment|34|62%|
|Residential investment|22|50%|
|House prices|33|69%|



After completing the threshold analysis, we have three restricted datasets which include a range of forward- and backward-looking variables. Tables A1 to A3 in the Appendix outline the type of variables, and their relative shares in each dataset. Several variables do not have time series available until after January 1995, however, our methodological approach, which we explain in Section 4, is robust to including variables with shorter historical time series. 

### **4. Methodology** 

#### **4.1. Dynamic factor models** 

We construct our dynamic factor models following Bok et al. (2018), used by the Federal Reserve Bank of New York.<sup>6</sup> The modelling approach we implement assumes that most of the variation across a wide range of economic data can be explained by a few common factors (Bok et al., <u>2018). We illustrate this idea by considering a set of</u> 𝑁 time series variables: {𝑦1,𝑡𝑦2,𝑡, … 𝑦𝑁,𝑡} , which have two (unobserved) common factors, {𝐾1,𝑡, 𝐾2,𝑡} . Using a DFM framework, we can express variable 𝑦1 in period 𝑡 as follows: 



Where 𝐾1,𝑡 and 𝐾2,𝑡 are the common factors in period 𝑡 , and 𝜆𝐾1 and 𝜆𝐾2 are the degree to which variable 𝑦1 is related to common factors 𝐾1 and 𝐾2 , respectively. The data movements which are unrelated to 𝐾1 and 𝐾2 are captured by the idiosyncratic error term, 𝜀1,𝑡 . 

Alongside being able to parse many variables, there are several features of DFMs which make them a suitable framework for real-time forecasting. In formulating forecasts, we often want to use more traditional data (such as national accounts statistics), alongside higher frequency data (such as surveys and credit statistics). Since these data have varying frequencies and are released with different lags, most forecasting frameworks cannot incorporate all this data in the same model. This means a forecaster must apply expert judgement in weighting the signal from different data sources and models. The dynamic factor framework we implement can incorporate variables both of different frequencies and of varying release lags. This means it is an effective way to _collectively_ parse a wide range of data and understand how these data are weighted within the forecasts. The ability for DFMs to manage data with different frequencies and release lags are a result of using Kalman filtering and maximum likelihood estimation to estimate the common factors ( 𝐾𝑖 ) and idiosyncratic errors ( 𝜀𝑛 ) in equation (1) above. As per the model of Bok et al. (2018), we model the 𝐼 common factors and 𝑁 error terms as Gaussian autoregressive processes: 

###### ____________ 

> 6 The code to implement the dynamic factor model of Bok et al. (2018) can be accessed at the linked Github page. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

6 

7 



The common factors and factor loadings of the above model are not directly observed, and are estimated using the iterative expectation-maximisation algorithm, as follows: 

**1.** Compute the principal components of the dataset. 

**2.** Estimate the model parameters using an Ordinary Least Squares (OLS) regression, with the principal components estimated in step 1 assumed to be the common factors. 

**3.** Using the parameters from step 2, compute the common factors using the Kalman smoother. 

**4.** Iterate steps 1-3 until the model converges on the maximum likelihood parameters. 

In applying the Kalman filter, the model infers the future path of all variables in the dataset such that all variables have the same end point. We illustrate how this works in practice using a simplified example dataset shown in table 2. This example dataset has similar features to the datasets used in our DFMs; there is both monthly and quarterly data, and variables have different release lags. At a given point in time (the 31<sup>st</sup> of October in table 2), there is missing data for several historical periods, as well as future periods (illustrated with shaded cells). 

**_Table 2: Example dataset as at 31st of October 2024_** 

|**Date**|**Bank**<br>**lending**<br>**variable**|**Interest rate**<br>**variable**|**Heavy traffic**<br>**variable**|**Business survey**<br>**variable**|**Business**<br>**investment**|
|---|---|---|---|---|---|
|**Frequency**|**Monthly**|**Monthly**|**Monthly**|**Quarterly**|**Quarterly**|
|Units|$|%|Index|Index|qpc^, %|
|May 2024|2,500,000|5.2|78|85|2.1|
|June 2024|2,300,000|5|75|||
|July 2024|2,600,000|5.3|80|||
|Aug. 2024|2,450,000|5.1|79|88||
|Sept. 2024|2,700,000|5.6|82|||
|Oct. 2024|2,800,000|||||
|Nov. 2024||||||
|Dec. 2024||||||



Note: data in this table is randomly generated for illustrative purposes and does not correspond to real-world variables. Shaded cells represent missing data as at 31 October 2024. ^Quarterly percentage change. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

7 

8 

**_Table 3: Example dataset as at 31st of October 2024, with forecast data_** 

|**Date**|**Bank**<br>**lending**<br>**variable**|**Interest rate**<br>**variable**|**Heavy traffic**<br>**variable**|**Business survey**<br>**variable**|**Business**<br>**investment**|
|---|---|---|---|---|---|
|**Frequency**|**Monthly**|**Monthly**|**Monthly**|**Quarterly**|**Quarterly**|
|Units|$|%|Index|Index|qpc^, %|
|May 2024|2,500,000|5.2|78|||
|||||85|21|
|June 2024|2,300,000|5|75||.|
|July 2024|2,600,000|5.3|80|||
|Aug. 2024|2,450,000|5.1|79|88|**2.4**|
|Sept. 2024|2,700,000|5.6|82|||
|Oct. 2024|2,800,000|**5.8**|**84**|||
|Nov. 2024|**2,850,000**|**5.5**|**85**|**87**|**2**|
|Dec. 2024|**2,900,000**|**5.5**|**87**|||



Note: data in this table is randomly generated for illustrative purposes and does not correspond to real-world variables. Shaded cells represent missing data as at 31 October 2024. ^Quarterly percentage change. 

Suppose that in the week following the 31<sup>st</sup> October, new data is released for the heavy traffic variable for the month of October (shaded blue in table 4). Following this, the DFM based on this dataset can be re-estimated, producing updated forecasts for _all missing data_ (shaded purple in table 4). The forecasts for the other variables missing data are updated based on: 

**1.** How far the actual October outturn for the heavy traffic variable (in table 3) differed from the forecast October outturn (in table 4). 

**2.** How useful the heavy traffic variable is for forecasting each variable. 

This means the revision to the business investment ( 𝐵𝐼 ) forecast following the release of the heavy traffic variable ( 𝐻𝑇𝑉 ) for October can be expressed as follows: 

ΔBIQ2 2024 = (𝐻𝑇𝑉 𝐴𝑐𝑡𝑢𝑎𝑙𝑀10 2024 −𝐻𝑇𝑉 𝐹𝑜𝑟𝑒𝑐𝑎𝑠𝑡𝑀10 2024 ) ∗ 𝑊𝑒𝑖𝑔ℎ𝑡𝐻𝑇𝑉 𝑋 𝐵𝐼 (4) 

If the blue term in equation 4 is close to zero, (that is, the actual October outturn for the heavy traffic variable is very similar to the forecast outturn), the revision to the forecast for business investment will be small. If there _is_ a material difference in the actual and forecast outturns for the heavy traffic variable, the extent of the forecast revision to business investment depends on the magnitude of the weight term (highlighted pink in equation 4). That is, how useful the heavy traffic variable has been historically for forecasting business investment. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

8 

9 

We can extend the horizon over which to forecast data out to up to 12 months, or four quarters, ahead of the current end point. Given we only have data for the independent variables up to a few months ahead of the dependent variable, the DFM assumes data autoregressively converges to its’ historical mean. 

**_Table 4: Example dataset as at 7th of November 2024, with forecast data_** 

|**Date**|**Bank**<br>**lending**<br>**variable**|**Interest rate**<br>**variable**|**Heavy traffic**<br>**variable**|**Business survey**<br>**variable**|**Business**<br>**investment**|
|---|---|---|---|---|---|
|**Frequency**|**Monthly**|**Monthly**|**Monthly**|**Quarterly**|**Quarterly**|
|Units|$|%|Index|Index|qpc^, %|
|May2024|2,500,000|5.2|78|85|2.1|
|June 2024|2,300,000|5|75|||
|July2024|2,600,000|5.3|80|88|**2.3**|
|Aug. 2024|2,450,000|5.1|79|||
|Sept. 2024|2,700,000|5.6|82|||
|Oct. 2024|2,800,000|**5.7**|82|**86**|**1.9**|
|Nov. 2024|**2,830,000**|**5.6**|**84**|||
|Dec. 2024|**2,870,000**|**5.5**|**86**|||



Note: data in this table is randomly generated for illustrative purposes and does not correspond to real-world variables. Shaded cells represent missing data as at 31 October 2024. ^Quarterly percentage change. 

#### **4.2. Out-of-sample forecast construction** 

To evaluate the forecast performance of the DFMs we perform an out-of-sample forecasting exercise. This is common in the forecasting literature, simulating the experience of a real-time forecaster, and involves the following steps: 

**1.** Dividing the available data into an estimation sample and a hold-out sample. The estimation sample is based on the data available at month 𝑡 . 

**2.** Estimate the DFM using the estimation sample. 

**3.** Use the estimated model to generate forecasts for the target variable, based on the end point of the target variable in the estimation sample. If the target variable ends in quarter 𝑛 for the estimation sample that ends in month 𝑡 , forecasts are made for quarter 𝑛+ 1 , through to quarter 𝑛+ 4 . 

**4.** Evaluate the accuracy of the forecasts (which are based on real-time data vintages) using standard measures, based on the data in the hold-out sample. We compare forecasts for a given quarter to both the initially published data for a that quarter, as well as to data for that quarter 12 months following its’ initial publication, at which point revisions may have occurred. 

**5.** Step forward the end of the estimation sample by one month and repeat steps 2-4, until the forecasts reach the end of the hold-out sample (where forecast accuracy can still be evaluated). 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

9 

10 

Our estimation sample always starts at January 1995. The initial sample cutoff (month 𝑡 ) is December 2017. For business and residential investment, data is released in March, June, September and December, for the previous quarter. As of December 2017, the last available observation was Q3 2017. Simulating a real-time forecasting exercise, we use the vintage data available in December 2017 to forecast the business and residential investment from Q4 2017 to Q3 2018. We then move the estimation sample cutoff forward one month to January 2018 ( 𝑡+ 1 ) and re-estimate the DFM model. At 𝑡+ 1 , the end point 𝑛 for business and residential investment is still Q3 2017, and we forecast the same four quarters ahead as the initial estimation sample. Once the estimation sample cutoff reaches March 2018, the Q4 2017 data is released, and we start forecasting Q1 2018 to Q4 2018. We continue to step forward the estimation sample cutoff by 1 month at a time, making four-quarter ahead forecasts each time. We stop when 𝑡 reaches August 2023, as the four quarter ahead forecasts reach the end of the hold-out sample (Q2 2024). This out-of-sample forecasting process is illustrated in figure 1. The same process is applied to forecast house prices, adapted to fit with the data being released in January, April, July and October. 

**_Figure 1: Out of sample forecast exercise methodology_** 



_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

10 

11 

We estimate each DFM using an expanding window of data, always starting at January 1995, rather than a rolling window of fixed length. Using a rolling window may better accommodate shifts in the underlying data-generating process if the sample size were longer. However, as some of our data has a relatively short historical sample, a rolling window sample may cause an excess sensitivity to individual observations. 

As we are estimating a quarterly variable at a monthly frequency, the four quarters we forecast for the target variable in each month are _month-ahead_ forecasts rather than _quarter-ahead_ forecasts. Depending on the month, the four forecasts made each month represent different month-ahead forecasts. Table 5 shows the month-ahead forecasts made in each month for business and residential investment, where data is released in March, June, September and December.<sup>7</sup> 

**_<mark>Table 5: Definition of month ahead forecasts for business and residential investment</mark>_** 

|**Month**|**Forecast**<br>**quarter 1**|**Forecast**<br>**quarter 2**|**Forecast**<br>**quarter 3**|**Forecast**<br>**quarter 4**|
|---|---|---|---|---|
|**March, June,**<br>**September, December**<br>_3 months till next_<br>_quarterly release_|3-month ahead<br>forecast|6-month ahead<br>forecast|9-month ahead<br>forecast|12-month<br>ahead forecast|
|**January, April, July,**<br>**October**<br>_2 months till next_<br>_quarterly release_|2-month ahead<br>forecast|5-month ahead<br>forecast|8-month ahead<br>forecast|11-month<br>ahead forecast|
|**February, May,**<br>**August, November**<br>_1 month till next_<br>_quarterly release_|1-month ahead<br>forecast|4-month<br>ahead forecast|7-month ahead<br>forecast|10-month<br>ahead forecast|



#### **4.3. Evaluation of out-of-sample forecasts** 

To evaluate the out-of-sample forecast performance of the DFMs, we compare to two benchmarks; a simple AR(1) forecast, and the real-time forecasts produced by RBNZ staff that are published alongside the Reserve Bank’s _MPS._ The AR(1) benchmark represents a simple test of whether the DFM forecasts offer improvements over a model solely capturing autoregressive dynamics. If it cannot, then this would suggest that the DFMs’ more sophisticated modelling approach does not provide additional information than just looking at the past movements of the respective series. The _MPS_ forecasts represent a more sophisticated benchmark, with these forecasts subject to rigorous internal discussion among staff and members of the MPC and based on a wide range of information and models before publications in the _MPS_ . 

###### ____________ 

> 7  For house prices, data is released in January, April, July and October. This means the month-ahead forecasts made in each month are different to Table 5. Refer to Table B1 in Appendix B for the corresponding table for house price forecasts. 

_AN - Forecasting Investment and House Prices in NZ_ 

11 

_using Dynamic Factor Models –_ AN2025-02 

12 

To measure forecasting performance, we use a **four-quarter rolling average of the relative root mean squared errors** (RRMSEs), between the DFM and the benchmark forecasts. 

The rationale for using a _four-quarter rolling average_ of the RRMSE (as opposed to an average over the whole out-of-sample forecast period) is to avoid overweighting the pandemic period in our analysis (as a fixed window RRMSE may do). Using the four-quarter rolling average means we can still assess how the DFM forecasts compare to the benchmark forecasts over a period of substantial volatility, while also appropriately comparing performance when data patterns are more standard. 

The RRMSE is calculated as follows: 

###### 𝑅𝑀𝑆𝐸 𝐷𝐹𝑀<sup>𝑥</sup> 

###### 𝑅𝑅𝑀𝑆𝐸= 𝑅𝑀𝑆𝐸 𝑏𝑒𝑛𝑐ℎ𝑚𝑎𝑟𝑘 

where 𝑅𝑀𝑆𝐸 𝑏𝑒𝑛𝑐ℎ𝑚𝑎𝑟𝑘 is the root mean squared error (RMSE) from the forecasts of either the AR(1) model or the _MPS_ and 𝑅𝑀𝑆𝐸 𝐷𝐹𝑀<sup>𝑥</sup> is the RMSE of each alternative DFM. RMSEs are calculated using the formula 



where ŷ𝑡+ℎ is the forecast of the dependent variables by the relevant model, 𝑦𝑡+ℎ is the actual data for that dependent variable, and 𝑇 is the number of replications (for the forecasting exercise). We compare to the initial release of 𝑦𝑡+ℎ . As a robustness check, we also compare to the revised value of 𝑦𝑡+ℎ (released 12 months afterwards), in the appendix. 

The benchmark for each month-ahead DFM forecast is shown in table 6. 

**_Table 6: Benchmark forecasts_** 

|**DFM month-ahead forecast**|**AR(1) & MPS benchmark forecast**|
|---|---|
|1-month ahead, 2-month ahead, 3-month ahead|1-quarter ahead|
|4-month ahead, 5-month ahead, 6-month ahead|2-quarter ahead|
|7-month ahead, 8-month ahead, 9-month ahead|3-quarter ahead|
|10-month ahead, 11-month ahead, 12-month ahead|4-quarter ahead|



### **5. Results** 

#### **5.1. AR(1) benchmark** 

We find the near-term forecast performance of the three DFMs to consistently exceed that of a simple AR(1) model. We include this material in Appendix C. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

12 

13 

#### **5.2. Business Investment** 

##### **_MPS_ forecast benchmark** 

We compare the DFM and _MPS_ forecasts for business investment in figures 2 through 5. Relative to _MPS_ forecasts, the performance of the DFM for business investment has varied: 

- **2017-2019** , prior to the pandemic, the DFM’s forecast accuracy was comparable to that of MPS forecasts. The DFM forecasts one to three months ahead were slightly more accurate than one quarter ahead MPS forecasts over 2018, and slightly worse during 2019. The DFM forecasts four to six months ahead and seven to nine months ahead were on average more accurate than the relevant MPS benchmarks. 

- **2020-2022** , following significant shocks to the New Zealand economy during the pandemic, the purely data-based DFM provides considerably worse near-term forecasts than the MPS benchmarks, which benefit from expert judgement. We do not observe the same deterioration in relative forecast accuracy at longer horizons, seven to 12 months ahead. However, this reflects that both the MPS and DFM forecasts for 2020, as of 2019, did not anticipate the pandemic shocks, which is unsurprising, given the nature of the shock. 

- **2023-2024** , following a period of material shocks, more normal data patterns have returned and the DFM forecast accuracy improves relative to the pandemic period. Near-term forecasts from the DFM outperform the MPS forecasts 1-quarter ahead, while forecasts further ahead are somewhat mixed, performing better than the MPS at times, and worse at other times, depending on the forecast horizon. 

**_Figure 2: RRMSE using MPS forecasts 1-quarter ahead as a benchmark (Bus. Inv. DFM)_** 

**_Figure 3: RRMSE using MPS forecasts 2-quarters ahead as a benchmark (Bus. Inv. DFM)_** 



_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

13 

14 

###### **_Figure 4: RRMSE using MPS forecasts 3-quarters ahead as a benchmark (Bus. Inv. DFM)_** 

**_Figure 5: RRMSE using MPS forecasts 4-quarters ahead as a benchmark (Bus. Inv. DFM)_** 



##### **Decompositions** 

One benefit of the DFM framework is the ability to analyse how the model weights data, and which data releases have led to revisions in the business investment forecast over time. This improves understanding of the data underpinning the forecasts, and aids communication. We plot the relative weighting of different data categories at different forecast horizons in figure 6. Here, the weighting of variable categories for each month-ahead forecast are averaged to find the _average_ weightings for forecasts one to four-quarters ahead. 

These decompositions illustrate that survey-based measures such as the ANZ Business Outlook (ANZBO) survey (shaded pink) and the Quarterly Survey of Business Opinion (QSBO) (shaded orange) tend to be relatively highly weighted. These datasets tend to be timely relative to other ‘official’ measures of economic activity such as national accounts, with ANZBO variables receiving lower weightings at shorter horizons as more official data is released. Both surveys include variables which measure businesses’ current and future investment intentions, and our results suggest these can be a useful indicator for business investment. This is consistent with Fitchett & <u>Robinson (2021), who find the QSBO investment intentions variables to improve forecasts of</u> aggregate GDP growth. 

Since late 2020, the ‘Other’ category of variables (shaded green) has grown substantially in importance. The most heavily weighted variable in this category is the business investment variable itself, signalling that business investment more recently has demonstrated auto-regressive dynamics. Also included in this category is the Reserve Bank’s real-time estimate of the output gap, indicating the additional value that expert judgement played in forecast accuracy during this period. Given the procyclicality of business investment, we find this result unsurprising. Intuitively, businesses would be expected to expand production by investing in new plant, machinery and equipment when aggregate demand in the economy is high, and supply cannot keep pace. 

Finally, we note that when forecasting one-quarter ahead, the DFM gives weight to construction variables (shaded purple). Compared to survey-based variables, these data are more tightly linked to business investment being realised, including variables such as ready-mix concrete and building 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

14 

15 

consents. As such, it makes sense these variables are more useful for forecasting business investment at shorter horizons. 

**_Figure 6: Relative Weighting of Variable Categories (Bus. Inv. DFM)_** 





Note: The weight for each category is a sum of the weights on the individual variables within that category. PMI is BusinessNZ’s Performance of Manufacturing Index. PSI is BusinessNZ’s Performance of Services Index. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

15 

16 

The DFM also reports which data has driven revisions to the forecasts over time. Using Q3 2023 as an example, figure 7 plots how the quarterly percentage change forecast for business investment for Q3 2023 evolved between the 12-month ahead forecast and the 1-month ahead forecast. In figure 8, we plot the change in the forecast from figure 7 with stacked bars showing the variable categories contributing to the change. 

**_Figure 7: Forecast for Q3 2023 Figure 8: Decomposition of Forecast Revisions (12 to 1 month ahead)_** 





To understand this decomposition, we refer to equation (4) from section 4.1, which shows how an input variable such as 𝐻𝑇𝑉 leads to a revision in the business investment forecast. Importantly, the contribution of a data release to a revision in the business investment forecast depends on two dimensions: 1) the difference between the actual data outturn and the DFM forecast for the outturn, and 2) the weight of the variable in business investment forecasts. 

Over the first half of figure 7, new ANZBO data regularly pulled down the forecast for business investment in Q3 2023. This is due to the relatively high weight on the ANZBO variables at longer forecast horizons for business investment (figure 6), which mean even small misses in the DFM’s forecast for ANZBO variables lead to relatively material revisions to the business investment forecast. As the forecast horizon shortens, ANZBO is weighted much less in business investment forecasts (figure 6) and subsequently becomes less prominent as a driver of forecast revisions. Interestingly, the QSBO variables are weighted similarly to the ANZBO variables at longer horizons (figure 6), but do not feature as a driver of forecast revisions in figure 8. This suggests the DFM can more reliably forecast QSBO outturns than ANZBO outturns, that is, the blue term in the equation above is generally smaller for QSBO variables. This likely results from the ANZBO being timelier than the QSBO (monthly vs quarterly frequency) and these series being correlated. 

In the second half of figure 8, construction data being weaker than the DFM forecast put downward pressure on the business investment forecast for Q3 2023, while stronger than expected business investment outturns offset some of this weakness. Notably, vehicle data led to a material downward revision in the business investment forecast four months ahead, and a large upward revision three months ahead. This is despite having a relatively low weight in business investment forecasts compared to other variables (figure 6), suggesting the DFM forecasts for the vehicle variables were particularly poor for these outturns. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

16 

17 

#### **5.3. Residential Investment** 

##### **_MPS_ forecast benchmark** 

Figures 9 to 12 highlight that relative to the _MPS_ forecasts, the forecast performance of the residential investment DFM model has varied over time. 

**_Figure 9: RRMSE using MPS forecasts 1-quarter ahead as a benchmark (Res. Inv. DFM)_** 

**_Figure 10: RRMSE using MPS forecasts 2-quarters ahead as a benchmark (Res. Inv. DFM)_** 



**_Figure 11: RRMSE using MPS forecasts as a benchmark, 3-quarters ahead (Res. Inv. DFM)_** 



**_Figure 12: RRMSE using MPS forecasts as a benchmark, 4-quarters ahead (Res. Inv. DFM)_** 



- **2018-2019** , prior to the pandemic, the DFM’s forecast accuracy was broadly comparable to MPS forecasts, performing slightly better or slightly worse depending on the forecast horizon. 

- **2020-2021** , during the pandemic period, the forecast performance of the DFM deteriorates significantly. As identified, with normal data patterns significantly disrupted, this period highlights the benefit of overlaying modelled forecasts with expert judgement, as is the case with the _MPS_ forecasts, when data doesn’t appropriately capture volatility. 

- **2022-2024** , the DFM forecast accuracy significantly improves at all horizons and has been comparable to the _MPS_ forecasts in the last quarters of our analysis period at all horizons. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

17 

18 

##### **Decompositions** 

Figure 13 shows the relative weightings of variables in the residential investment restricted dataset at each forecast horizon. 

**_Figure 13: Relative Weighting of Variable Categories (Res. Inv. DFM)_** 



_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

18 

19 

A common theme across all four horizons is the role of the real-time output gap and lagged residential investment, categorised as ‘Other’. Residential investment is persistent and procyclical, implying this relationship is unsurprising. Alongside this, indicators from the ANZBO, QSBO and housing and construction variables receive considerable weight in forecasting residential investment. Interestingly, credit data is not particularly highly weighted (as was the case with the business investment DFM. 

Figures 14 and 15 highlight the evolution of the DFM’s forecast for Q2 2023. This forecast remained negative in growth terms for almost the entire forecast period, however outturns from the monthly ANZBO survey resulted in large changes. This is consistent with our observations from the business investment DFM, with ANZBO survey data often differing materially from the DFM’s internal forecasts for this survey data, leading to large forecast revisions. 

**_Figure 14: Forecast for Q3 2023 (12 to 1 month ahead)_** 

**_Figure 15: Decomposition of Forecast Revisions_** 

#### **5.4. House Prices** 

##### **_MPS_ forecast benchmark** 

Figure 16 to 19 compare the forecast performance of the house prices DFM relative to the _MPS_ forecasts. Like the previous models, the relative performance varies. 

- **2019** , prior to the pandemic, the forecast performance of the DFM was generally worse than that of the _MPS._ 

- **2020-2021** , the forecast performance of the DFM improves upon the benchmark at all forecast horizons. This contrasts to the DFMs for business and residential investment which tended to perform poorly relative to the _MPS_ forecasts over this period. 

- **2022-2024** , the forecast performance of the DFM deteriorates considerably relative to the _MPS_ benchmark over 2021 and 2022, while starting to improve more recently. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

19 

20 

**_Figure 16: RRMSE using MPS forecasts 1-quarter ahead as a benchmark (House Prices DFM)_** 



**_Figure 17: RRMSE using MPS forecasts 2-quarters ahead as a benchmark (House Prices DFM)_** 



**_Figure 18: RRMSE using MPS forecasts 3-quarters ahead as a benchmark (House Prices DFM)_** 

**_Figure 19: RRMSE using MPS forecasts 4-quarters ahead as a benchmark (House Prices DFM)_** 



##### **Decompositions** 

Figure 20 shows the relative weightings of the variables in the house prices restricted dataset. Forecasts from the house price DFM are heavily determined by lagged house prices, monthly house price estimates from the Real Estate Institute of New Zealand (REINZ) and credit variables. One-quarter ahead, forecasts tend to be driven mostly by the monthly REINZ releases, consistent with how the RBNZ incorporates this data. In forecasts two- to four-quarters ahead, the number of house sales and interest rates becomes considerably more important. This is aligned with our priors, given that activity in the housing market is aligned with house price growth. Furthermore, the Housing TWG (2022) find changes in interest rates have been shown to be a key driver of house prices (albeit in the context of constrained land supply). Credit variables have a relatively smaller weighting but are still important in this DFM, particularly at longer horizons. This is intuitive as most house purchases are financed by mortgages, the stock of which is captured in the credit variables we include. The amount of new mortgage lending is one measure of housing demand, 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

20 

21 

reflecting housing market conditions and how households are perceiving the outlook, with demand for housing directly affecting price dynamics. 

Figure 20: Relative Weighting of Variable Categories (House Prices DFM) 





Figures 21 and 22 indicate the progression of a forecast from the DFM for Q3 2023. Initially, the DFM was estimating house price growth in this quarter would be relatively strong at 4 percent. However, as new data was released particularly from REINZ and number of sales this forecast was 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

21 

22 

revised lower until reaching a trough near -3 percent 9-months ahead. Later releases of REINZ data were the main contributors to the model eventually settling at a forecast of flat growth. 

**_Figure 21: Forecast for Q3 2023 Figure 22: Decomposition of Forecast Revisions (12 to 1 month ahead)_** 





#### **5.5. Summary** 

While each of our three DFMs performs differently, some common themes emerge: 

- The DFMs consistently outperform forecasts from a simple AR(1) model at all forecast horizons. This highlights the benefit of incorporating a wide range of economic data and implementing a framework which can incorporate longer lag structures. 

- Prior to the pandemic and more recently, the forecast performance of the DFMs is broadly comparable to the published MPS forecasts. However, forecast performance deteriorated during the pandemic period following disruption to normal data patterns. This suggests these models perform best when nowcasting in periods where data volatility is normal. It is important to note that the MPS forecasts are a difficult benchmark to outperform. These forecasts incorporate many different data sources and often include judgement about one-off type factors which data series can struggle to accurately reflect. However, given DFMs aggregate lots of information in a statistically consistent way, these models can be a useful addition to the suite of tools we use for forecasting key macroeconomic variables. 

- The ANZBO is weighted relatively highly in the DFM model for forecasting business and residential investment. This is one example of how non-standard indicators of economic activity can add value, particularly in frameworks such as the DFM, where the cost of adding these additional indicators is marginal. 

- The weighting of different variable categories can change depending on the forecast horizon. Procyclical variables in our dataset, with cyclicality matching that of our target variables, were weighted particularly highly. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

22 

23 

Our findings are consistent with similar studies that find that forecast performance of DFMs was significantly better than the simple benchmark models (e.g., Bayarmagnai (forthcoming) for real GDP in New Zealand, Bok et al. (2018) for the United States and Hartigan & Rosewall (2024) for Australia). In addition, other work such as Matheson (2006) also illustrates that there is a trade-off between model size and accuracy, motivating our approach to use restricted datasets of only the most valuable variables. We also observe that timely data sources, such as business surveys, tend to have larger impacts at the start of the forecasting period which diminish somewhat as official data is released (Bok et al., 2018). While Bayarmagnai (forthcoming) finds the DFM is unable to outperform the Reserve Banks’ nowcast for real GDP, we find stronger evidence that DFMs focussed on forecasting the subcomponents of GDP can outperform _MPS_ forecasts in ‘normal’ times. Consistent with Bayarmagnai, we find considerable value in the ability to decompose the DFM forecasts into its drivers. 

### **6. Conclusion** 

We construct three dynamic factor models to nowcast business investment, residential investment and house prices in New Zealand, building off the model of Bok et al. (2018). These models can quickly and collectively process large datasets containing variables of different frequencies and with different release lags. We evaluate the forecast performance of these models against a simple AR(1) benchmark and the RBNZ-published _MPS_ forecasts to assess whether they can provide accurate assessments. Our results suggest these models can be a useful addition to the suite of tools we use for forecasting key macroeconomic variables, with forecast performance consistently superior to an AR(1), and broadly comparable to that of our _MPS_ forecasts during periods of normal data volatility. 

The ability to decompose the DFM forecasts also adds considerable value to these models, enabling forecasters to understand which data is driving the forecasts and how much signal to take from these models, supporting communication of the forecasts to policymakers. By processing a wide range of data, the models provide a counterfactual weighting of different data. This counterfactual weighting can be compared with the judgement-based weighting of forecasting analysts. We will continue to refine these models further, adding or removing data sources to maximise their value to forecasting analysts. 

There are several areas for future work, including expanding our dataset and selection approach to consider a wider range of variables and forecasting other macroeconomic variables of interest. In particular, we could consider adding international data in line with Chen and Ranieri (2019), who find these data improve their forecasts of the New Zealand economy. There is also scope to update the methodological approach, following the recent work of Almuzara et al. (2023) to introduce a more robust version of the original Bok et al. (2018) model which is more robust to data volatility. This could be particularly useful for improving the forecast performance of the model during periods of significant economic volatility, which remains a weakness of the current models. Finally, we could combine our DFMs with more novel machine learning techniques following the work of Ishaak et al. (2024) to improve forecast performance. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

23 

24 

### **References** 

Almuzara, M., Baker, K., O’Keeffe, H., & Sbordone, A. M. (2023). Reintroducing the New York Fed Staff Nowcast. _Federal Reserve Bank of New York._ (No. 20230908). - - - - - - <u>https://libertystreeteconomics.newyorkfed.org/2023/09/reintroducing the new york fed staff nowcast/</u> 

Albuquerque, B., Baumann, U., & Seitz, F. (2016). What does money and credit tell us about real activity in the United States? _The North American Journal of Economics and Finance_ , _37_ , 328-347. <u>https://doi.org/10.1016/j.najef.2016.05.011</u> 

Bai, J., & Ng, S. (2008). Forecasting economic time series using targeted predictors. _Journal of Econometrics_ , _146_ (2), 304-317. https://doi.org/10.1016/j.jeconom.2008.08.010 

Bayarmagnai, G. (2025). Nowcasting New Zealand GDP using a dynamic factor model. _Reserve Bank of New Zealand Analytical Note,_ 2025-01. 

Bloor, C., Hunt, C., Ng, T., & Pepper, H. (2008). The use of money and credit measures in contemporary monetary policy. _Reserve Bank of New Zealand Bulletin_ , _71_ (1), 5-15. <u>https://www.rbnz.govt.nz/-/media/6ae9781f65354b0989db721a8b4e47f2.ashx?sc_lang=en</u> 

Bok, B., Caratelli, D., Giannone, D., Sbordone, A. M., & Tambalotti, A. (2018). Macroeconomic nowcasting and forecasting with big data. _Annual Review of Economics_ , _10_ (1), 615-643. - - - <u>https://doi.org/10.1146/annurev economics 080217 053214</u> 

Boivin, J., & Ng, S. (2006). Are more data always better for factor analysis? _Journal of Econometrics_ , _132_ (1), 169-194. https://doi.org/10.1016/j.jeconom.2005.01.027 

Chen, S., & Ranciere, R. (2019). Financial information and macroeconomic forecasts. _International Journal of Forecasting_ , _35_ (3), 1160-1174. https://doi.org/10.1016/j.ijforecast.2019.03.005 

Ermişoğlu, E., Akçelik, Y., & Oduncu, A. (2013). Nowcasting GDP growth with credit data: Evidence from an emerging market economy. _Borsa Istanbul Review_ , 13(4), 93-98. <u>https://doi.org/10.1016/j.bir.2013.10.009</u> 

Fitchett, H., Robinson, F., (2021). Down to business: Which QSBO measures are the best at - forecasting? _Reserve Bank of New Zealand Analytical Note_ , AN2021/01. https://www.rbnz.govt.nz/ - - <u>/media/project/sites/rbnz/files/publications/analytical notes/2021/an2021 01.pdf</u> 

Giannone, D., Reichlin, L., & Small, D. (2008). Nowcasting: The real-time informational content of macroeconomic data. _Journal of monetary economics_ , _55_ (4), 665-676. <u>https://doi.org/10.1016/j.jmoneco.2008.05.010</u> 

Hartigan, L., & Rosewall, T. (2024). Nowcasting Quarterly GDP Growth during the COVID-19 Crisis Using a Monthly Activity Indicator. _Reserve Bank of Australia_ . (No. 2024-15). - <u>https://doi.org/10.47688/rdp2024 04</u> 

Housing Technical Working Group. (2022). Assessment of the Housing System: With insights from - - the Hamilton-Waikato area. https://www.treasury.govt.nz/sites/default/files/2022 <u>08/htwg</u> - - - - - <u>assessment housing system hamilton waikato aug22.pdf</u> 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

24 

25 

Ishaak, F., Liu, P., Hardeman, E., & Remoy, H. (2024). Forecasting house prices and rents: Combining dynamic factor models and machine learning (No. 2024-207). _European Real Estate Society_ . http://dx.doi.org/10.15396/eres2024-207 

Kirker, M. (2010). What drives core inflation? A dynamic factor model analysis of tradable and nontradable prices.  Reserve Bank of New Zealand Discussion Paper Series DP2010/13, Reserve Bank of - - New Zealand. https://www.rbnz.govt.nz/ <u>/media/project/sites/rbnz/files/publications/discussion</u> - <u>papers/2010/dp10 13.pdf</u> 

Matheson, T. D. (2006). Factor model forecasts for New Zealand. _International Journal of Central Banking_ , _2(2)_ . https://www.ijcb.org/journal/ijcb06q2a6.pdf 

Price, G. (2013). Some revisions to the sectoral factor model of core inflation.  Reserve Bank of New Zealand Analytical Note Series AN2013/06, Reserve Bank of New Zealand. - - <u>https://www.rbnz.govt.nz/ /media/project/sites/rbnz/files/publications/analytical</u> - <u>notes/2013/an2013 06.pdf</u> 

Rünstler, G., Barhoumi, K., Benk, S., Cristadoro, R., Den Reijer, A., Jakaitiene, A., ... & Van Nieuwenhuyze, C. (2009). Short-term forecasting of GDP using large datasets: a pseudo real-time forecast evaluation exercise. _Journal of Forecasting_ , _28_ (7), 595-611. https://doi.org/10.1002/for.1105 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

25 

26 

### **Appendix** 

#### **Appendix A: Dataset Selection** 

**_Table A1: Restricted dataset for the business investment DFM_** 

|**Data types**|**Number of variables**|
|---|---|
|Activity surveys|22|
|Vehicles|5|
|Housing|2|
|Credit|2|
|Other|3|



**_Table A2: Restricted dataset for the residential investment DFM_** 

|**Data types**|**Number of variables**|
|---|---|
|Activity surveys|12|
|Credit|4|
|Housing|3|
|Interest rates|1|
|Other|2|



**_Table A3: Restricted dataset for the house price DFM_** 

|**Data types**|**Number of variables**|
|---|---|
|Credit|15|
|Housing|7|
|Prices|4|
|Interest rates|3|
|Activity surveys|3|
|Other|1|



_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

26 

27 

**_Figure A1: Ranked Wald Statistics and Threshold Value – Business Investment Extended Dataset_** 





_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ 

UNCLASSIFIED 

27 

AN2025-02 

28 

###### **_Figure A2: Ranked Wald Statistics and Threshold Value – Residential Investment Extended Dataset_** 





Note: QES is the ‘Quarterly Employment Survey’ from StatsNZ. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ 

UNCLASSIFIED 

28 

AN2025-02 

29 

**_Figure A3: Ranked Wald Statistics and Threshold Value – House Prices Extended Dataset_** 





Note: HLFS is the ‘Household Labour Force Survey’ from StatsNZ. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ 

UNCLASSIFIED 

29 

AN2025-02 

30 

#### **Appendix B: Month ahead forecasts for house prices** 

**_Table B1: Definition of N-month ahead forecasts for house prices_** 

|**Month**|**Forecast**<br>**quarter 1**|**Forecast**<br>**quarter 2**|**Forecast**<br>**quarter 3**|**Forecast**<br>**quarter 4**|
|---|---|---|---|---|
|**January, April, July,**<br>**October**<br>_3 months till next_<br>_quarterly release_|3-month ahead<br>forecast|6-month ahead<br>forecast|9-month ahead<br>forecast|12-month<br>ahead forecast|
|**February, May, August,**<br>**November**<br>_2 months till next_<br>_quarterly release_|2-month ahead<br>forecast|5-month ahead<br>forecast|8-month ahead<br>forecast|11-month<br>ahead forecast|
|**March, June, September,**<br>**December**<br>_1 month till next_<br>_quarterly release_|1-month ahead<br>forecast|4-month<br>ahead forecast|7-month ahead<br>forecast|10-month<br>ahead forecast|



_AN - Forecasting Investment and House Prices in NZ_ 

UNCLASSIFIED 

30 

_using Dynamic Factor Models –_ AN2025-02 

31 

#### **Appendix C: AR(1) benchmark** 

##### **Business Investment** 

When comparing the forecast performance of the business investment DFM with the AR(1) forecasts, for brevity, we average the month-ahead RRMSEs in each quarter and plot the _quarterly average_ four-quarter rolling RRMSE in figure C1. 

We observe the RRMSE of DFM forecasts at all horizons are well below 1 throughout our analysis period, where 1 represents the RMSE of the AR(1) forecasts one quarter ahead. This indicates the DFM is able to consistently provide more accurate near-term forecasts for business investment than an AR(1). 

##### **Residential Investment** 

As with business investment we start by comparing the DFM forecasts for residential investment to a simple AR(1) benchmark using the quarterly average rolling RRMSE in figure C2. As before, the DFM consistently outperforms the AR(1) model, baring a temporary deterioration in performance in mid-2021. 

##### **House Prices** 

As with the other two DFMs, the house prices DFM consistently outperforms the forecasts from an AR(1) model at all horizons, except in 2024 (figure C3). 

**_Figure C1: Quarterly average rolling RRMSE using AR(1) Figure C2: RRMSE using AR(1) forecasts as a forecasts as a benchmark (Business Investment DFM) benchmark (Residential investment. DFM)_** 





_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

UNCLASSIFIED 

31 

32 

###### **_Figure C3: RRMSE using AR(1) forecasts 1-quarter ahead as a benchmark (House Prices DFM)_** 



_AN - Forecasting Investment and House Prices in NZ_ 

UNCLASSIFIED 

32 

_using Dynamic Factor Models –_ AN2025-02 

33 

#### **Appendix D: Robustness Test – Forecasting revised data** 

##### **Dataset Selection** 

While we follow Boivin and Ng (2006) in determining which variables to include in our final dataset, this is one of several approaches used in the literature, with little consensus on the optimal approach (Hartigan & Rosewall, 2024). As a simple test of the robustness of the results to our approach to dataset selection, we consider how the DFMs perform using the extended datasets for our three variables of interest. We do this by calculating the rolling RRMSE of the baseline DFMs (which use the restricted datasets) using the _RMSE of the DFMs using the extended dataset_ as our benchmark – as we did with AR(1) and MPS forecast RMSEs in Section 5. For brevity, we take an average of the RRMSE for the three forecasts made in each quarter and plot these series in figures D1 to D3. 

For business investment, we observe that the longer-term forecast accuracy is broadly comparable between the two DFM variants (figure D1). For near-term forecasts, the RMSE of the baseline DFM is generally larger than the RMSE of the extended dataset DFM 1-quarter ahead between 2020 and 2023. The 2-quarter ahead RMSE is also larger than the benchmark since 2023. This indicates that the extended dataset DFM for business investment has given better near-term forecasts over this period. 

The baseline residential investment DFM, on the other hand, consistently performs similarly or better than the extended dataset DFM, with the rolling RRMSE progressively getting progressively lower than 1 since 2021, at all forecast horizons (figure D2). Similarly, the baseline house price DFM using the restricted dataset generally produces more accurate forecasts. 

In the case of the residential investment and house price DFMs, removing data deemed uninformative for forecasting the target variable using our selection criteria means there was relatively more weight placed informative variables, leading to largely better forecasts. However, in the case of the business investment DFM, this exercise demonstrates that our selection criteria led to variables being removed which would have improved the forecast performance of the DFM had they been included. This could be for several reasons. The time period we use for our dataset selection regressions includes the pandemic period. If a variable was well correlated with our target variable during normal times, but was particularly disrupted during the pandemic, it may have been removed. As in related literature, we do not update the variables in our dataset before making a forecast each month; we use the current vintage of data to determine which variables to include in our dataset, and the variables in our dataset are fixed throughout our evaluation period. A potential improvement to this approach would be to run the dataset selection exercise for each month we estimate the model and update the dataset accordingly. 

_AN - Forecasting Investment and House Prices in NZ using Dynamic Factor Models –_ AN2025-02 

UNCLASSIFIED 

33 

34 

###### **_Figure D1: Quarterly average RRMSE using extended dataset DFM forecasts as a benchmark (Business Investment DFM)_** 

**_Figure D2: Quarterly average RRMSE using extended dataset DFM forecasts as a benchmark (Residential Investment DFM)_** 



**_Figure D3: Quarterly average RRMSE using extended dataset DFM forecasts as a benchmark (House Prices DFM)_** 



##### **Revised Data** 

In Section 5, we evaluate the forecast performance of the three DFMs based on how well they forecast the initial release of the three variables of interest. However, historical business investment, residential investment, and (to a lesser extent) house prices, are frequently revised in future releases.<sup>8</sup> While the largest revisions tend to occur in the quarters immediately following the initial release of a datapoint, small revisions to historical data can continue to occur for several years. We now consider how the DFMs perform at forecasting revised data. To ensure the revision window is consistent across our evaluation period, we consider each data point 12 months after its 

____________ 

> 8 Historical house prices index data is revised to a small extent due to seasonal adjustment. 

_AN - Forecasting Investment and House Prices in NZ_ 

UNCLASSIFIED 

34 

_using Dynamic Factor Models –_ AN2025-02 

35 

initial release as our revised data series. We include the results of this robustness test in figures D4 to D6, finding little material difference between the forecast accuracy of the three DFMs in forecasting the initial release of data and the revised release. 

###### **_Figure D4: Quarterly average RRMSE using RMSE of revised data forecasts as a benchmark (Business Investment DFM)_** 

###### **_Figure D5: Quarterly average RRMSE using RMSE of revised data forecasts as a benchmark (Residential Investment DFM)_** 



**_Figure D6: Quarterly average RRMSE using RMSE of revised data forecasts as a benchmark (House Prices DFM)_** 



_AN - Forecasting Investment and House Prices in NZ_ 

UNCLASSIFIED 

35 

_using Dynamic Factor Models –_ AN2025-02 

