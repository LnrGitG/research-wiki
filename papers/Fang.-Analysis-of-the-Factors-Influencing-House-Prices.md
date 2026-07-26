---
title: **Analysis of the Factors Influencing House Prices Based on the Var Model**
type: paper
source_pdf: raw/papers/Fang. Analysis of the Factors Influencing House Prices.pdf
converted: 2026-07-26
---

**WEP International Journal of Global Economics and Management Warwick Evans** ISSN: 3005-9690 (Print), ISSN: 3005-8090 (Online) | Volume 4, Number 1, Year 2024 DOI: https://doi.org/10.62051/ijgem.v4n1.29 **Publishing** Journal homepage: https://wepub.org/index.php/IJGEM/index 



# **Analysis of the Factors Influencing House Prices Based on the Var Model** 

Jiayu Fang<sup>*</sup> 

Department of Probability and Statistics, Wuhan University, Wuhan, China *Corresponding Author: 2682038367@qq.com 

### **ABSTRACT** 

Var model is established to study the relationship between house price, inflation rate and GDP in this article. By using Granger causality test, cointegration test, impulse response function and variance decomposition to analyze, we conclude that the value of inflation rate and GDP can be predicted by the past data of house price, and GDP has a significant impact on house price. 

### **KEYWORDS** 

Var model; Granger causality test; Co-integration test; Impulse response function; House price 

## **1. INTRODUCTION** 

The issue of housing is of great importance to everyone. In the traditional mindset of Chinese people, purchasing one's own home is one of the essential aspects of a happy life. The government is striving to ensure that all people have access to adequate housing. Consequently, the fluctuations in real estate prices are a matter of great concern to us. Studying the relationship between inflation rates, economic growth, and real estate prices can provide a theoretical reference for the government to adjust economic policies and address people's housing issues. Changes in the real estate market also impact the national economy, thus regulating real estate prices is crucial for steady economic development. 

There are numerous articles examining factors influencing the real estate market, but most of them focus on the effects of monetary policy and interest rates, with few delving into the relationship between economic growth and real estate prices. The government is strengthening policy regulations to safeguard people's housing needs, demonstrated by the reduction of mortgage interest rates by 25 basis points at the beginning of 2024, aiming to alleviate the financial burden on homebuyers. This study can serve as a reference for future government economic policies aimed at regulating the real estate market and even accelerating economic growth, ensuring the effectiveness of such policies. 

In this paper, VaR model is used to do empirical analysis. VaR model can help us to study the relationship between different time series variables and predict more accurately, which has been widely used in the prediction analysis of financial markets and various commodity markets, so it has high academic and application value. Due to the late introduction of VaR model in China, the study on VaR model is not deep enough in China, and VaR does not satisfy the subadditivity and insufficiency of tail loss measurement in the famous axiom of consistency. The research on VaR model abroad started earlier and has a deep research background. Therefore, the research methods and scope are more extensive, and the content and logical level of the research are more deep and organized. While China's research on VaR started relatively late, as VaR has gained recognition and adoption by most international financial institutions, China has also intensified its efforts in studying 

Content from this work may be used under the terms of CC BY-NC 4.0 licence (https://creativecommons.org/licenses/by-nc/4.0/). Published by Warwick Evans Publishing. 

VaR theory. The VaR model can be applied to analyze even more commodity markets, thereby continuously expanding its application value. 

## **2. LITERATURE REVIEW** 

Through the collation of domestic and foreign literature, there are many studies on real estate price forecasting. Wang Laifu (2007) [1] addressed the issue of the impact of monetary policy on real estate prices by utilizing quarterly data since the reform of the housing allocation system in 1998. Based on the VAR model and methods of impulse response functions and variance decomposition, the study found that changes in money supply have a long-term and sustained positive impact on real estate prices, while interest rates have a negative impact on real estate prices that diminishes over time and eventually returns to the origin. Notably, the influence of money supply changes was found to be more significant than that of interest rates. Luo Xiaoling (2012) [2] investigated the various macroeconomic factors influencing real estate prices using quarterly data from 2001 to 2010. Employing the VAR model, impulse response functions, and variance decomposition methods, the study found that real estate prices are significantly influenced by past prices and money supply. Furthermore, the study revealed a bidirectional Granger causality between real estate prices and GDP, as well as interest rates on loans. Additionally, there exists a unidirectional Granger causality between real estate prices and consumer spending. Meng Qingbin (2014) [3] explored the long-term and shortterm impacts of macroeconomic factors on real estate prices. Using vector autoregression (VAR) model decomposition techniques, the study concluded that an increase in interest rates has a longterm negative effect on housing prices and tends to exacerbate fluctuations in prices in the short term. Furthermore, the study found that when economic growth accelerates, it has a certain inhibitory effect on investment and speculation in the real estate industry. Deokho Cho (1999) [4] examined the longterm relationship between housing values and interest rates in the Korean housing market. Employing methods such as cointegration tests, spectral analysis, and Granger causality tests, the study found a long-term negative equilibrium relationship between housing values and interest rates. Additionally, the study identified a unidirectional causality running from interest rates to housing value changes, which can be useful in predicting future changes in housing values. Peter Gustafsson (2016) [5], amidst a backdrop of Swedish real estate prices roughly doubling over 15 years, addressed the macroeconomic implications of a significant housing price decline. Using a Bayesian VAR model, he found that a 20% drop in housing prices would have recession-like effects on household consumption and unemployment, with even more pronounced impacts if the decline coincides with a global economic recession. This finding holds relevance for policymakers. Luca  Benati (2021) [6] found out that the impact of monetary policy on housing prices is 3-5 times greater than that on GDP based on the SVaR model. The analysis of foreign literature shows that there are many researches on the influencing factors of housing prices abroad, and the model application is more abundant. 

Analyzing the existing research results on the law of real estate prices, we found that there are abundant studies on the impact of interest rates, and many different models have been used in the research. However, there are relatively few articles studying inflation rates, economic growth rates, and real estate prices based on VaR models. We understand that economic growth rates and inflation rates can have varying degrees of impact on real estate prices. Studying the relationship between these three factors can help the government conduct macroeconomic regulation and control based on economic situations, ensuring that everyone has a place to live. 

212 

## **3. MODEL AND VARIABLE SELECTION** 

### **3.1. Var Model** 

When we study the time series, it is inevitable to consider the interaction between multiple variables. Vector autoregression (VaR) is a model established based on the statistical nature of the data. Each endogenous variable in the system is constructed as a function of the lag value of all endogenous variables in the system, and the univariate autoregression (AR) model is extended to the "vector" autoregressive model composed of multivariate time series variables. When we aim to study the time series of interactions among d variables Y_1, ..., Y_d, we can consider any one of these variables as a linear function of the past values of all the other variables, i.e 



Write in matrix form 𝑌𝑡=θ+𝛽1𝑌𝑡−1+𝛽2𝑌𝑡−2+....+𝛽𝑘𝑌𝑡−𝑘 + 𝜀𝑡, Where 𝛽𝑖 is a d×d matrix, and θ, 𝑌𝑡−𝑖 and𝜀𝑡 are d×1 matrices. 

### **3.2. Variable Selection** 

(1) The housing price (HP) of commercial residential buildings in China 

(2) China's inflation rate 

(3) Chinese GDP 

## **4. DATA PROCESSING** 

The data in this paper are from the China database. 

(1) The housing price (HP) of commercial residential buildings in China. This paper selects the data from the first quarter of 2018 to the first quarter of 2024, and obtains the average sales price from the difference between the cumulative amount of commercial housing divided by the difference in the cumulative sales area of commercial housing. Since the initial data is monthly data, the average of each quarter is selected to represent the data of this quarter. 

(2) Rate of inflation. The monthly data of consumer price index (CPI) from January 2017 to March 2024 was selected, and the year-on-year inflation rate from January 2018 to March 2024 is calculated by (current CPI - previous CPI) / previous CPI × 100%, and the quarterly data is obtained by averaging the data for each quarter. 

(3) GDP. Select the data from the first quarter of 2018 to the first quarter of 2024. 

## **5. EMPIRICAL RESULTS AND ANALYSIS** 

### **5.1. Simple Data Analysis** 

First of all, we can see from the pairwise scatter plot of three variables that gdp has an obvious positive correlation with house price, and house price has a certain negative correlation with inflation rate, while there is no obvious linear relationship between gdp and inflation rate. 

Secondly, from the timing chart, the trend of the housing price and the gdp is the same, so we can guess that there is a positive correlation between the two, that is, when the housing price rises, the gdp will also rise, and when the gdp rises, the housing price will also rise immediately. Obviously, 

213 

both house prices and gdp are unstable time series, which we will use a more rigorous mathematical method to analyze. 



**Figure 1.** Scatter Plot 



**Figure 2.** Timeline Diagram 

214 

### **5.2. Stabilization Analysis** 

We did the unit root test for the three variables, and the test results showed that (with 0.01 as the given significance level), all three sequences are non-stationary sequences. After applying the firstorder difference to each of the three series, the resulting series become stationary, indicating that they are all first-order integrated. After applying the first-order difference to the housing price, inflation rate, and GDP, we denote them as del_hp, del_inflation, and del_gdp, respectively. 

**Table 1.** Test of unit roots 

|variable|P-value|conclusion|P-value (first-order difference)|conclusion|
|---|---|---|---|---|
|housing price|0.759|Not smooth|≤0.01|steady|
|rate of inflation|0.0397|Not smooth|≤0.01|steady|
|GDP|0.693|Not smooth|≤0.01|steady|



### **5.3. Cointegration Test** 

After conducting a fourth-order cointegration test on housing prices, inflation rates, and GDP, the results indicate the presence of two cointegration relationships among the three variables, suggesting that there is a long-term mutual influence between housing prices, inflation rates, and GDP. Therefore, we can proceed to establish a VAR model based on these findings. 

The first cointegration relationship obtained after the standardized processing is: price. l4= - 2.307605e+01* inflation. l4 +1.120106e-02* gdp.l4 + 8.983152e+03 

This equation implies that when the inflation rate rises by one percentage point, the price drops by about 23 yuan, when the gdp rises by 100 million yuan, the price rises by 0.011 yuan. 

**Table 2.** Cointegration test for trace statistics 

|H0|Test the<br>statistical<br>value|The critical value<br>at a significance<br>level of 0.1|The critical value at<br>a significance level<br>of 0.05|The critical value at<br>a significance level<br>of 0.01|conclusion|
|---|---|---|---|---|---|
|r ≤2|4.07|7.52|9.24|12.97|accept|
|r ≤1|22.38|17.85|19.96|24.60|refuse|
|r =0|76.39|32.00|34.91|41.07|refuse|



**Table 3.** cointegration coefficients 

||HP(-4)|
|---|---|
|HP(-4)|1.00|
|Inflation(-4)|23.07605|
|GDP(-4)|-1.120106×10<sup>−2</sup>|
|constant|-8.983152×10<sup>3</sup>|



### **5.4. Establish the Var Model** 

After performing the unit root test, it was found that housing prices, inflation rates, and GDP are all first-order integrated. The Var model was built with the differential data del _ hp, del_inflation and del _ gdp. By the minimum information criterion, the Var (3) model should be selected, but after the unit root test, there is a root outside the unit circle, the model is unstable, so we choose the second smallest Var (1) model according to the minimum information criterion. 

215 

Then from the unit root test, it can be seen that all the roots are in the unit circle, and the first order Var model is established. The residual white noise test also passes, indicating that the information is fully extracted. 

**Table 4.** Var (1) 

|Unit root test|P-value of the residual white noise test|
|---|---|
|0.57909928|0.1674|
|0.57909928||
|0.07073789||



### **5.5. Granger Causality Test** 

Table 5 shows that housing price is the reason for GDP in the sense of granger, that is, the past data of housing price will affect the value of current GDP. 

GDP is not the Granger cause for house price, but we note that first-order difference of GDP is the Granger cause of the first-order difference of housing prices, that is to say, the change of GDP will lead to the change of house price. 

We then do granger test based on the Var model established by the non-stationary original but firstorder integrated sequence, which can see that housing prices are a Granger cause of GDP and inflation rates, but do not have an instantaneous causal relationship. 

**Table 5.** Granger the causality test 

|null hypothesis|P price|conclusion|
|---|---|---|
|Housing prices are not the Granger cause of GDP|0.03466|Refusing the null<br>hypothesis|
|GDP are not the Granger cause of Housing prices|0.1671|Accept the null<br>hypothesis|
|inflation rate are not the Granger cause of Housing prices|0.1045|Accept the null<br>hypothesis|
|Housing prices are not the Granger cause of inflation rate|0.5999|Accept the null<br>hypothesis|
|inflation rate are not the Granger cause of GDP|0.8943|Accept the null<br>hypothesis|
|GDP rate are not the Granger cause of inflation|0.9543|Accept the null<br>hypothesis|
|Housing prices are not the Granger cause of inflation rate<br>and GDP|0.0001462|Refusing the null<br>hypothesis|
|Housing prices are not the instantaneous Granger cause of<br>inflation rate and GDP|0.4201|Accept the null<br>hypothesis|
|Del_gdp rate are not the Granger cause of del_hp|0.01443|Refusing the null<br>hypothesis|



In conclusion, we can say that there is a bidirectional granger causal relationship between housing prices and GDP, and that housing prices has an impact on GDP and inflation rate. 

### **5.6. Impulse Response Function** 

Using the VAR model established earlier, we conduct an impulse response function analysis. First, let's observe the results with del_hp as the response variable. When the impulse variable is del_hp itself, the initial response is 475.76, indicating that upon receiving an impulse, the price will 

216 

immediately rise and then rapidly decline over time, reaching its lowest point in period 2, subsequently fluctuating around the 0 value.When the impulse variable is del_inflation, the impulse response of del_hp in the first period is 0, indicating no immediate reaction, which suggests that there is a lag in the impact of del_inflation on del_hp. Subsequently, it decreases to a low point of -157.06 in the second period, showing that an increase in del_inflation leads to a decrease in del_hp. After that, the response value rises to 0 and fluctuates around this point. When del_gdp is the impulse variable, the response value is 0 in the first period. It then declines to -174.2 in the second period, rises to 152.5 in the third period, and subsequently fluctuates around 0 over the following periods. 

When del_inflation is the response variable and del_hp is the impulse variable, the initial response of del_inflation in the first period is -0.54, indicating an immediate negative response. This suggests that when del_hp rises, del_inflation declines. The response then rises towards 0 and fluctuates around this value in subsequent periods. When del_gdp is used as the impulse variable, the initial response in the first period is 0, and in subsequent periods, it fluctuates around 0 before gradually decaying to 0. 

Finally, when del_gdp is the response variable and del_hp is the impulse variable, the first period is negative, indicating that the increase in del_hp will immediately cause del_gdp to decrease. The second period reaches a maximum of 12982.5, indicating that after a period of time, del_gdp will rise with the shock of del_hp, and then fluctuate around 0 in subsequent periods. Finally, when del_inflation is the impulse variable, the response in the first three periods is negative, indicating that when del_inflation rises, del_gdp will first decrease, reaching a peak in the fourth period, indicating that after a period of time, del_gdp will rise due to the shock of del_inflation. 







**Figure 3.** del _ hp is the response variable 

217 







**Figure 4.** del_inflation is the response variable 







**Figure 5.** del _ gdp is the response variable 

In conclusion, we see that both del _ hp and del _ gdp have negative impulse responses to each other, and then over a while to a positive response, 

The reciprocal impulse response of del _ hp and del_inflation is both clearly negative. That is to say, when the price changes greatly, the change of GDP will first become smaller and then larger, and then tend to stabilize. When the increase of GDP becomes larger, the increase of price will first become smaller and then larger, and then tend to stabilize, which has a relatively long-term impact. When the increase in the inflation rate increases, the increase in prices will decrease, and the impact is short-term. 

218 

### **5.7. Variance Decomposition** 



**Figure 6.** variance decomposition of del_gdp 



**Figure 7.** variance decomposition of del_hp 

219 



**Figure 8.** variance decomposition of del_inflation 

Based on the Var model established above, we can do the variance decomposition. First, let's look at the variance decomposition of del_gdp. It is evident that the largest contribution comes from itself, with a decline from 98% to 78.9% and then stabilizing. Del_hp initially contributes 2% in the first period, rising to 19.5% by the fourth period, and then stabilizes. In contrast, del_inflation contributes the least, consistently remaining below 2%. 

Now, turning to the variance decomposition of del_hp, we observe that its own contribution is the largest, decreasing from 100% to 72.4% by the fourth period. The proportion of del_gdp follows, rising from 0 to 18.8% by the fifth period and then stabilizing. The influence of del_inflation is the smallest, increasing from 0 to 8.9% by the fourth period and then stabilizing. 

Lastly, examining the variance decomposition of del_inflation, we find that once again, its own contribution is the largest, decreasing from 89.5% in the first period to 86.4% by the fourth period and then stabilizing. The contribution of del_price follows, rising from 10.5% to 13.1% by the fourth period. The contribution of del_gdp is the smallest, remaining below 1%. 

In short, we can say that GDP has a great impact on the housing price, and the inflation rate also has an impact on the housing price, but it is a little smaller, and the housing price has a relatively obvious impact on both the gdp and the inflation rate. 

## **6. CONCLUSIONS AND SUGGESTIONS** 

(1) In the long run, the interaction between housing price and gdp is more obvious, especially the growth of gdp will drive the growth of housing price. Therefore, while promoting industrial development and improving gdp, China should also stabilize the housing price from other aspects and guarantee people's housing demand. 

(2) From the result of the Impulse Response Function, we know that when the growth of GDP becomes larger, the growth of the housing price will become smaller and then larger in the short term, so it reserves a certain time for the government and the people to react. The government timely adjusts the policy to restrain the housing price, and people can buy a house as early as possible to avoid rising more housing prices in the later stage. 

220 

(3) In the long run, the inflation rate has little impact on the housing price, which can be seen from the results of the granger test. However, from the impulse response analysis, when the inflation rate increases, the increase of the housing price will decrease, that is, adjusting the inflation rate can restrain the rise of the housing price to a certain extent. 

(4) Housing prices have a great impact on GDP. When housing prices rise, they will attract investment from all sides and promote the flow of the capital market, thus driving GDP growth. Therefore, the healthy development of real estate is of great significance to the economic development, and the country should pay more attention to regulating the real estate market and controlling housing prices. 

(5) There is a Granger causality between housing prices and GDP as well as inflation rates, but there is no Granger causality between housing prices and inflation rates alone, indicating that the impact of housing prices on inflation rates is indirect and needs to be reflected through their interaction with GDP. 

(6) In short, the growth of GDP can indicate the rise of the housing price. The restraining effect of regulating the inflation rate on the housing price is not long-term, and other economic and policy measures should be combined to restrain the housing price. At the same time, the government needs to control housing prices to prevent housing price imbalances from affecting the macro economy. The influencing factors of interest rates for housing prices, money supply, real estate investment amount, and can also be studied to gain a more comprehensive understanding of the fluctuation of housing prices. 

## **REFERENCES** 

- [1] Wang Laifu, & Guo Feng. (2007). Study on the dynamic impact of monetary policy on real estate prices —— empirical based on var model. Financial issues research (11), 5. 

- [2] Luo Xiaoling, Hongbo, & Ma Shichang. (2012). Research on the influencing factors of real estate price based on var model. Journal of Central South University: Social Science Edition, 18 (4), 7. 

- [3] Meng Qingbin, & Rong Chen. (2014). Long-term and short-term impact of macroeconomic factors on real estate prices. Statistical studies (6), 8. 

- [4] Cho, D., & Ma, S. (2004). A Study of Dynamic Relationship between Housing Values and Interest Rate in the Korean Housing Market. 

- [5] Gustafsson, P., Stockhammar, P., & Österholm, P. (2016). Macroeconomic effects of a decline in housing prices in Sweden. Journal of Policy Modeling, 38, 242-255. 

- [6] Benati, L. (2021). Leaning against house prices: A structural VAR investigation. Journal of Monetary Economics. 

221 

